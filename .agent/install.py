"""AOS v8 safe installer for consumer projects.

Preflight runs before any write:
- fresh target -> sanitized install
- recognized AOS target -> safe runtime upgrade, preserving project state
- foreign/unknown agent infrastructure -> hard stop, no overwrite

Usage:
  python .agent/install.py /path/to/target-project
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SOURCE_ROOT = Path(__file__).resolve().parent.parent
SOURCE_AGENT = SOURCE_ROOT / ".agent"

RUNTIME_DIRS = [
    "01-core",
    "02-rules",
    "03-workflows",
    "05-references",
    "06-templates",
    "governance",
    "adr",
]

RUNTIME_FILES = [
    "INDEX.md",
    "AGENTS.md",
    "VERSION",
]

ROOT_ADAPTERS = [
    "AGENTS.md",
    "CLAUDE.md",
    ".cursorrules",
]

TECHNOLOGY_PROFILES = SOURCE_AGENT / "profiles" / "technology"
EVIDENCE_README = SOURCE_AGENT / "evidence" / "README.md"

PRESERVED_STATE = [
    ".agent/04-memory/",
    ".agent/profiles/project.json",
    ".agent/task-contracts/",
    ".agent/evidence/current.json",
    ".agent/evidence/history/",
]

AOS_MARKERS = [
    ".agent/VERSION",
    ".agent/01-core/boot-manifest.md",
]


class InstallError(ValueError):
    pass


def _is_aos_agent_dir(target_root: Path) -> bool:
    version = target_root / ".agent" / "VERSION"
    boot = target_root / ".agent" / "01-core" / "boot-manifest.md"
    if not version.exists() or not boot.exists():
        return False

    try:
        version_text = version.read_text(encoding="utf-8", errors="ignore")
        boot_text = boot.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False

    return "aos_version:" in version_text and "AOS" in boot_text


def _is_aos_adapter(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    return (
        "AOS" in text
        and ".agent/01-core/boot-manifest.md" in text
    )


def inspect_target(target_root: Path) -> dict:
    """Classify target before any write occurs."""
    target_root = target_root.resolve()
    if target_root == SOURCE_ROOT.resolve():
        raise InstallError(
            "Refusing to install consumer runtime over the AOS source repository."
        )

    target_agent = target_root / ".agent"
    agent_exists = target_agent.exists()
    aos_existing = agent_exists and _is_aos_agent_dir(target_root)

    conflicts = []

    if agent_exists and not aos_existing:
        conflicts.append(
            ".agent exists but is not a recognized AOS runtime"
        )

    for name in ROOT_ADAPTERS:
        path = target_root / name
        if path.exists() and not _is_aos_adapter(path):
            conflicts.append(
                f"{name} already exists and is not recognized as AOS-owned"
            )

    copilot = target_root / ".github" / "copilot-instructions.md"
    if copilot.exists() and not _is_aos_adapter(copilot):
        conflicts.append(
            ".github/copilot-instructions.md already exists and is not "
            "recognized as AOS-owned"
        )

    mode = "conflict" if conflicts else ("upgrade" if aos_existing else "fresh")
    return {
        "target": str(target_root),
        "mode": mode,
        "conflicts": conflicts,
        "aos_existing": aos_existing,
        "preserved_state": list(PRESERVED_STATE),
    }


def _copy_dir(source: Path, target: Path) -> None:
    if not source.exists():
        raise InstallError(f"Missing runtime directory: {source}")
    shutil.copytree(source, target, dirs_exist_ok=True)


def _copy_file(source: Path, target: Path) -> None:
    if not source.exists():
        raise InstallError(f"Missing runtime file: {source}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def _install_runtime(target_root: Path) -> None:
    target_agent = target_root / ".agent"
    target_agent.mkdir(parents=True, exist_ok=True)

    for name in RUNTIME_DIRS:
        _copy_dir(SOURCE_AGENT / name, target_agent / name)

    for name in RUNTIME_FILES:
        _copy_file(SOURCE_AGENT / name, target_agent / name)

    if TECHNOLOGY_PROFILES.exists():
        _copy_dir(
            TECHNOLOGY_PROFILES,
            target_agent / "profiles" / "technology",
        )

    if EVIDENCE_README.exists():
        _copy_file(
            EVIDENCE_README,
            target_agent / "evidence" / "README.md",
        )

    for name in ROOT_ADAPTERS:
        source = SOURCE_ROOT / name
        if source.exists():
            _copy_file(source, target_root / name)

    copilot = SOURCE_ROOT / ".github" / "copilot-instructions.md"
    if copilot.exists():
        _copy_file(
            copilot,
            target_root / ".github" / "copilot-instructions.md",
        )


def install(target_root: Path) -> dict:
    """Install or safely upgrade AOS after a write-free preflight."""
    target_root = target_root.resolve()
    report = inspect_target(target_root)

    if report["mode"] == "conflict":
        raise InstallError(
            "Agent infrastructure conflict detected; nothing was changed. "
            + " | ".join(report["conflicts"])
        )

    target_root.mkdir(parents=True, exist_ok=True)
    _install_runtime(target_root)

    return {
        **report,
        "runtime_installed": True,
        "runtime_upgraded": report["mode"] == "upgrade",
        "next": (
            "Initialize target-specific AOS state."
            if report["mode"] == "fresh"
            else "Existing project state preserved; revalidate project profile."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Safely install/upgrade AOS runtime")
    parser.add_argument("target", help="Target project root")
    parser.add_argument(
        "--preflight",
        action="store_true",
        help="Inspect collisions only; make no changes.",
    )
    args = parser.parse_args()

    target = Path(args.target)

    try:
        if args.preflight:
            result = inspect_target(target)
            print(f"AOS preflight: {result['mode']}")
            for conflict in result["conflicts"]:
                print(f"  CONFLICT: {conflict}")
            return 2 if result["mode"] == "conflict" else 0

        result = install(target)
    except InstallError as exc:
        print(f"INSTALL BLOCKED: {exc}")
        return 2

    action = "upgraded" if result["runtime_upgraded"] else "installed"
    print(f"AOS runtime {action} safely.")
    print(f"Target: {result['target']}")
    print("Preserved project state:")
    for item in result["preserved_state"]:
        print(f"  - {item}")
    print(result["next"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
