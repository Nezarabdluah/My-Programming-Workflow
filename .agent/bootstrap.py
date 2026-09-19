"""AOS v8 one-command bootstrap.

One command performs:
preflight -> safe install/upgrade -> project discovery -> target-specific
initialization -> portable AOS verification.

Usage:
  python .agent/bootstrap.py /path/to/project
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path


SOURCE_AGENT = Path(__file__).resolve().parent
VERSION_FILE = SOURCE_AGENT / "VERSION"


class BootstrapError(ValueError):
    pass


def _load_installer():
    path = SOURCE_AGENT / "install.py"
    spec = importlib.util.spec_from_file_location("aos_installer", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _version() -> str:
    text = VERSION_FILE.read_text(encoding="utf-8")
    match = re.search(r"^aos_version:\s*(\S+)\s*$", text, re.MULTILINE)
    if not match:
        raise BootstrapError("aos_version missing from .agent/VERSION")
    return match.group(1)


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "project"


def _package_manager(root: Path) -> str:
    if (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (root / "yarn.lock").exists():
        return "yarn"
    return "npm"


def _npm_command(manager: str, script: str) -> str:
    if manager == "yarn":
        return f"yarn {script}"
    return f"{manager} run {script}"


def _json_file(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def discover_project(root: Path) -> dict:
    """Conservatively discover project facts from files that actually exist."""
    root = root.resolve()
    languages = set()
    ecosystems = set()
    commands = {
        "aos_compile": (
            "python -m compileall -q .agent/governance "
            ".agent/01-core/context_broker.py "
            ".agent/01-core/approval_engine.py "
            ".agent/01-core/evidence_recorder.py "
            ".agent/01-core/task_contract.py "
            ".agent/01-core/execution_gate.py"
        ),
        "aos_verify": "python .agent/governance/verify.py",
    }
    evidence = []

    package_json = root / "package.json"
    if package_json.exists():
        ecosystems.add("node")
        languages.add("javascript")
        evidence.append("package.json")
        if (root / "tsconfig.json").exists() or list(root.glob("*.ts")):
            languages.add("typescript")
        package = _json_file(package_json)
        scripts = package.get("scripts", {}) if isinstance(package, dict) else {}
        manager = _package_manager(root)
        for script, command_name in [
            ("build", "project_build"),
            ("test", "project_test"),
            ("lint", "project_lint"),
        ]:
            if isinstance(scripts, dict) and script in scripts:
                commands[command_name] = _npm_command(manager, script)

    solutions = list(root.glob("*.sln"))
    csprojs = list(root.rglob("*.csproj"))
    if solutions or csprojs:
        ecosystems.add("dotnet")
        languages.add("csharp")
        evidence.append(solutions[0].name if solutions else csprojs[0].name)
        if len(solutions) == 1:
            commands["project_build"] = f'dotnet build "{solutions[0].name}"'
            commands["project_test"] = f'dotnet test "{solutions[0].name}"'

    pyproject = root / "pyproject.toml"
    requirements = root / "requirements.txt"
    python_files = [
        path for path in root.glob("*.py")
        if path.name not in {"setup.py"}
    ]
    if pyproject.exists() or requirements.exists() or python_files:
        ecosystems.add("python")
        languages.add("python")
        evidence.append(
            "pyproject.toml" if pyproject.exists()
            else "requirements.txt" if requirements.exists()
            else python_files[0].name
        )
        pytest_evidence = False
        for candidate in [pyproject, requirements]:
            if candidate.exists():
                try:
                    if "pytest" in candidate.read_text(
                        encoding="utf-8", errors="ignore"
                    ).lower():
                        pytest_evidence = True
                except OSError:
                    pass
        if pytest_evidence or (root / "pytest.ini").exists():
            commands.setdefault("project_test", "python -m pytest")

    if (root / "go.mod").exists():
        ecosystems.add("go")
        languages.add("go")
        evidence.append("go.mod")
        commands.setdefault("project_build", "go build ./...")
        commands.setdefault("project_test", "go test ./...")

    if (root / "Cargo.toml").exists():
        ecosystems.add("rust")
        languages.add("rust")
        evidence.append("Cargo.toml")
        commands.setdefault("project_build", "cargo build")
        commands.setdefault("project_test", "cargo test")

    if (root / "gradlew").exists():
        ecosystems.add("gradle")
        evidence.append("gradlew")
        commands.setdefault("project_build", "./gradlew build")
        commands.setdefault("project_test", "./gradlew test")
    elif (root / "gradlew.bat").exists():
        ecosystems.add("gradle")
        evidence.append("gradlew.bat")
        commands.setdefault("project_build", "gradlew.bat build")
        commands.setdefault("project_test", "gradlew.bat test")

    if (root / "pom.xml").exists():
        ecosystems.add("maven")
        languages.add("java")
        evidence.append("pom.xml")
        if (root / "mvnw").exists():
            commands.setdefault("project_build", "./mvnw package")
            commands.setdefault("project_test", "./mvnw test")
        elif (root / "mvnw.cmd").exists():
            commands.setdefault("project_build", "mvnw.cmd package")
            commands.setdefault("project_test", "mvnw.cmd test")

    if not languages:
        languages.add("unknown")

    if len(ecosystems) > 1:
        project_type = "multi-stack"
    elif ecosystems:
        project_type = next(iter(ecosystems))
    else:
        project_type = "generic"

    technology_profiles = []
    if "node" in ecosystems and ecosystems.intersection(
        {"dotnet", "python", "go", "rust", "maven", "gradle"}
    ):
        technology_profiles.append("full-stack-web")

    area_rules = [
        {
            "prefix": ".github/workflows",
            "capabilities": ["deployment", "testing"],
        },
    ]
    for prefix in ["tests", "test", "spec"]:
        if (root / prefix).exists():
            area_rules.append({
                "prefix": prefix,
                "capabilities": ["testing"],
            })

    return {
        "project_id": _slug(root.name),
        "project_type": project_type,
        "languages": sorted(languages),
        "ecosystems": sorted(ecosystems),
        "technology_profiles": technology_profiles,
        "commands": commands,
        "area_capability_rules": area_rules,
        "discovery_evidence": evidence,
    }


def _write_json(path: Path, data: dict, *, overwrite: bool) -> bool:
    if path.exists() and not overwrite:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return True


def _write_text(path: Path, content: str, *, overwrite: bool) -> bool:
    if path.exists() and not overwrite:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def initialize_target(root: Path, discovery: dict, *, preserve_existing: bool) -> dict:
    version = _version()
    label = f"v{version}"
    overwrite = not preserve_existing
    agent = root / ".agent"

    profile = {
        "schema_version": 1,
        "project_id": discovery["project_id"],
        "project_type": discovery["project_type"],
        "languages": discovery["languages"],
        "technology_profiles": discovery["technology_profiles"],
        "architecture": {
            "style": "existing-project",
            "source_of_truth": "project-codebase",
        },
        "commands": discovery["commands"],
        "area_capability_rules": discovery["area_capability_rules"],
        "discovery": {
            "status": (
                "detected"
                if discovery["discovery_evidence"]
                else "needs_review"
            ),
            "evidence": discovery["discovery_evidence"],
        },
    }

    task = {
        "schema_version": 1,
        "task_id": "T000",
        "title": "AOS bootstrap baseline",
        "classification": "simple",
        "capabilities": ["testing"],
        "affected_areas": [".agent"],
        "risk": {},
        "approval": {},
        "verification": ["aos_compile", "aos_verify"],
    }

    memory = {
        "project-context.md": (
            f"# Project Context — AOS {label}\n"
            "- **Phase:** Initialized\n"
            "- **Task:** T000 — Done\n\n"
            "## Current\n"
            f"AOS bootstrap completed for {discovery['project_id']}. "
            "Project-specific engineering facts should be refined from code evidence.\n\n"
            "## Next\n"
            "Give the agent a normal project task; it will create/update the Task Contract.\n"
        ),
        "active-tasks.md": (
            f"# Active Tasks — AOS {label}\n\n"
            "## T000 — AOS Bootstrap Baseline 🟢\n"
            "- **State:** Done\n\n"
            "### Result\n"
            "- [x] Runtime installed safely.\n"
            "- [x] Project Profile initialized from repository evidence.\n"
            "- [x] Portable AOS verification configured.\n"
        ),
        "learned-mistakes.md": (
            f"# Learned Mistakes — AOS {label}\n\n"
            "> No active project mistakes recorded yet. Add only evidence-backed lessons.\n"
        ),
        "decisions.md": (
            "# Project Decisions\n\n"
            "> No project ADRs recorded yet. Runtime ADRs live in "
            ".agent/adr/system-decisions.md.\n"
        ),
        "project-knowledge.md": (
            "# Project Knowledge\n\n"
            "> Add durable, verified project-specific patterns here.\n"
        ),
        "codebase-map.md": (
            "# Codebase Map\n\n"
            f"- Project type: {discovery['project_type']}\n"
            f"- Languages: {', '.join(discovery['languages'])}\n"
            "- Discovery evidence: "
            f"{', '.join(discovery['discovery_evidence']) or 'none — review required'}\n"
        ),
    }

    written = []
    if _write_json(
        agent / "profiles" / "project.json",
        profile,
        overwrite=overwrite,
    ):
        written.append(".agent/profiles/project.json")

    if _write_json(
        agent / "task-contracts" / "current.json",
        task,
        overwrite=overwrite,
    ):
        written.append(".agent/task-contracts/current.json")

    for name, text in memory.items():
        if _write_text(
            agent / "04-memory" / name,
            text,
            overwrite=overwrite,
        ):
            written.append(f".agent/04-memory/{name}")

    return {
        "written": written,
        "preserved_existing": preserve_existing,
        "profile": profile,
    }


def run_portable_verification(root: Path) -> dict:
    command = [sys.executable, ".agent/governance/verify.py"]
    completed = subprocess.run(
        command,
        cwd=root,
        check=False,
        text=True,
        capture_output=True,
    )
    return {
        "command": " ".join(command),
        "exit_code": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "status": "PASS" if completed.returncode == 0 else "FAIL",
    }


def bootstrap(target_root: Path, *, verify: bool = True) -> dict:
    target_root = target_root.resolve()
    installer = _load_installer()

    preflight = installer.inspect_target(target_root)
    if preflight["mode"] == "conflict":
        raise BootstrapError(
            "Agent infrastructure conflict detected; nothing was changed. "
            + " | ".join(preflight["conflicts"])
        )

    install_result = installer.install(target_root)
    discovery = discover_project(target_root)

    initialized = initialize_target(
        target_root,
        discovery,
        preserve_existing=install_result["mode"] == "upgrade",
    )

    verification = None
    if verify:
        verification = run_portable_verification(target_root)
        if verification["status"] != "PASS":
            raise BootstrapError(
                "AOS was installed, but portable verification failed. "
                "Review the generated project state and verification output.\n"
                + verification["stdout"][-4000:]
                + verification["stderr"][-2000:]
            )

    discovery_status = initialized["profile"]["discovery"]["status"]
    return {
        "status": "READY" if discovery_status == "detected" else "NEEDS_REVIEW",
        "mode": install_result["mode"],
        "target": str(target_root),
        "project_id": discovery["project_id"],
        "project_type": discovery["project_type"],
        "languages": discovery["languages"],
        "commands": sorted(discovery["commands"]),
        "written": initialized["written"],
        "preserved_state": install_result["preserved_state"],
        "verification": verification,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Bootstrap AOS into a project with one safe command"
    )
    parser.add_argument("target", help="Target project root")
    parser.add_argument(
        "--preflight",
        action="store_true",
        help="Inspect conflicts/discovery only; make no changes.",
    )
    args = parser.parse_args()

    target = Path(args.target)
    installer = _load_installer()

    try:
        if args.preflight:
            preflight = installer.inspect_target(target)
            discovery = discover_project(target)
            print(json.dumps(
                {"preflight": preflight, "discovery": discovery},
                indent=2,
                ensure_ascii=False,
            ))
            return 2 if preflight["mode"] == "conflict" else 0

        result = bootstrap(target, verify=True)
    except (BootstrapError, installer.InstallError) as exc:
        print(f"AOS BOOTSTRAP BLOCKED: {exc}")
        return 2

    print("")
    print("AOS BOOTSTRAP COMPLETE")
    print("=" * 48)
    print(f"Status: {result['status']}")
    print(f"Mode: {result['mode']}")
    print(f"Target: {result['target']}")
    print(f"Project: {result['project_id']} ({result['project_type']})")
    print(f"Languages: {', '.join(result['languages'])}")
    print(f"Checks/commands: {', '.join(result['commands'])}")
    if result["status"] == "READY":
        print("Ready: open the project and give your coding agent a task.")
    else:
        print(
            "Needs review: no strong stack marker was detected. "
            "Open the generated Project Profile before the first non-trivial task."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
