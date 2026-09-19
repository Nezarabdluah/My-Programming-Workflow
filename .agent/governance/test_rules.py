"""AOS Governance — Rule Tests (v8.0.0-rc.1)

GOV-T06: Canonical boot contract links to task rules
GOV-T07: REF citation validity (project-agnostic source discovery)
GOV-T08: Dead/stale reference detection (project-agnostic)
GOV-T10: ADR consistency — actually verifies changes (not rubber-stamp)
"""
import json
import re
from pathlib import Path

PASS = "PASS"
FAIL = "FAIL"
SKIP_EXPECTED = "SKIP_EXPECTED"
SKIP_UNSUPPORTED = "SKIP_UNSUPPORTED"


def _is_aos_source_repo():
    path = Path(".agent/profiles/project.json")
    if not path.exists():
        return False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return (
        data.get("project_id") == "my-programming-workflow"
        and data.get("project_type") == "engineering-workflow-framework"
    )


def _find_source_files():
    """Discover source files without assuming a fixed directory name.

    Looks for common source file extensions in the project root,
    excluding .agent/, .git/, node_modules/, vendor/, and similar.
    """
    root = Path(".")
    exclude_dirs = {
        ".agent", ".git", ".hg", ".svn", "node_modules", "vendor",
        "__pycache__", ".venv", "venv", "env", ".env", "dist", "build",
        "target", "bin", "obj", ".next", ".nuxt", "coverage",
    }
    source_exts = {".py", ".cs", ".js", ".ts", ".jsx", ".tsx", ".go",
                   ".java", ".rs", ".rb", ".php", ".kt", ".swift", ".md"}

    source_files = []
    for f in root.rglob("*"):
        if f.is_file() and f.suffix in source_exts:
            # Skip excluded directories
            parts = set(f.parts)
            if not parts.intersection(exclude_dirs):
                source_files.append(f)
    return source_files


def test_gov_t06_rule_linkage():
    """GOV-T06: Verify canonical boot routes through the unified Execution Gate.

    Sprint 2 autonomy uses:
    Boot -> Execution Gate -> Task Contract / Approval / Context / Project Profile.
    """
    boot_path = Path(".agent/01-core/boot-manifest.md")
    gate_path = Path(".agent/01-core/execution_gate.py")
    if not boot_path.exists():
        return FAIL, "GOV-T06: canonical boot-manifest.md not found."
    if not gate_path.exists():
        return FAIL, "GOV-T06: execution_gate.py not found."

    boot = boot_path.read_text(encoding="utf-8")
    gate = gate_path.read_text(encoding="utf-8")

    missing = []
    if "execution_gate.py" not in boot:
        missing.append("boot→execution gate")

    gate_markers = {
        "task-contracts/current.json": "task contract",
        "approval_engine.py": "approval engine",
        "context_broker.py": "context broker",
        "profiles/project.json": "project profile",
        "approval-registry.json": "approval registry",
        "context-map.json": "context map",
    }
    for marker, label in gate_markers.items():
        if marker not in gate:
            missing.append(label)

    if missing:
        return FAIL, (
            "GOV-T06: Canonical execution routing incomplete: "
            + ", ".join(missing)
        )

    return PASS, (
        "GOV-T06: Boot routes through Execution Gate to validated task, "
        "approval, context, profiles, registry, and context map."
    )

def test_gov_t07_reference_verification():
    """GOV-T07: Verify [REF-xxx] codes used in source match the catalog.

    Uses project-agnostic source discovery (no hardcoded 'src/' path).
    """
    catalog_path = Path(".agent/05-references/engineering-rules-catalog-REF.md")
    if not catalog_path.exists():
        return SKIP_UNSUPPORTED, (
            "GOV-T07: Reference catalog not found — "
            "cannot validate REF citations."
        )

    catalog_content = catalog_path.read_text(encoding="utf-8")
    valid_refs = set(re.findall(r"\[(REF-[A-Z0-9-]+)\]", catalog_content))

    source_files = _find_source_files()
    if not source_files:
        return SKIP_EXPECTED, (
            "GOV-T07: No source files found in project — "
            "no REF citations to validate."
        )

    violations = []
    for fp in source_files:
        try:
            content = fp.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        used_refs = re.findall(r"\[(REF-[A-Z0-9-]+)\]", content)
        for ref in used_refs:
            if ref not in valid_refs:
                violations.append(f"[{ref}] in {fp.name}")

    if violations:
        return FAIL, (
            f"GOV-T07: Invalid REF citations: {'; '.join(violations[:5])}"
        )

    return PASS, "GOV-T07: All REF citations match the catalog."


def test_gov_t08_dead_references():
    """GOV-T08: Detect stale/corrupt reference codes in source.

    Uses project-agnostic source discovery.
    """
    source_files = _find_source_files()
    if not source_files:
        return SKIP_EXPECTED, "GOV-T08: No source files found — nothing to check."

    violations = []
    for fp in source_files:
        try:
            content = fp.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        # Detect old numeric format (REF-001) instead of named (REF-ARCH-DEP)
        invalid_format = re.findall(r"\[REF-\d{3}\]", content)
        if invalid_format:
            violations.append(f"{invalid_format} in {fp.name}")

    if violations:
        return FAIL, (
            f"GOV-T08: Stale/corrupt REF codes: {'; '.join(violations[:5])}"
        )

    return PASS, "GOV-T08: No stale or corrupt reference codes found."


def test_gov_t10_decision_consistency():
    """GOV-T10: Runtime policy references real system/project ADRs."""
    sources = [
        Path(".agent/adr/system-decisions.md"),
        Path(".agent/04-memory/decisions.md"),
    ]

    existing = [path for path in sources if path.exists()]
    if not existing:
        return FAIL, "GOV-T10: no system/project ADR source exists."

    decisions_content = "\n\n".join(
        path.read_text(encoding="utf-8") for path in existing
    )
    adr_ids = set(re.findall(r"## .*?(ADR-\d+)", decisions_content))
    if not adr_ids:
        return FAIL, "GOV-T10: no ADR entries found in runtime/project sources."

    incomplete = []
    for adr_id in sorted(adr_ids):
        match = re.search(
            r"## .*?" + re.escape(adr_id) + r".*?(?=\n## |\Z)",
            decisions_content,
            flags=re.MULTILINE | re.DOTALL,
        )
        if not match:
            continue
        section = match.group(0)
        lowered = section.lower()
        required_labels = ("context", "decision", "consequences")
        missing = [label for label in required_labels if label not in lowered]
        if missing:
            incomplete.append(f"{adr_id} (missing: {', '.join(missing)})")

    if incomplete:
        return FAIL, "GOV-T10: Incomplete ADR(s): " + "; ".join(incomplete)

    policy_files = [
        ".agent/01-core/boot-manifest.md",
        ".agent/01-core/operating-contract.md",
        ".agent/01-core/wiring-registry.md",
        ".agent/02-rules/vertical-slice-governance.md",
    ]

    missing_refs = []
    checked_refs = set()
    for rel_path in policy_files:
        path = Path(rel_path)
        if not path.exists():
            continue
        refs = set(re.findall(r"ADR-\d+", path.read_text(encoding="utf-8")))
        checked_refs.update(refs)
        for ref in refs:
            if ref not in adr_ids:
                missing_refs.append(f"{ref} referenced by {rel_path}")

    if missing_refs:
        return FAIL, "GOV-T10: Policy references missing ADRs: " + "; ".join(missing_refs)

    return PASS, (
        f"GOV-T10: {len(adr_ids)} system/project ADR(s) valid; "
        f"{len(checked_refs)} runtime ADR reference(s) resolve."
    )

def test_gov_t36_public_contract_sync():
    """GOV-T36: README public contract must match the current v8 runtime."""
    if not _is_aos_source_repo():
        return SKIP_EXPECTED, "test_gov_t36_public_contract_sync: AOS-source-only check."

    readme = Path("README.md")
    if not readme.exists():
        return FAIL, "GOV-T36: README.md missing."

    content = readme.read_text(encoding="utf-8")

    required = [
        "execution_gate.py",
        "context_broker.py",
        "evidence_recorder.py",
        "approval-registry.json",
        "Task Contract",
        "Evidence History",
        "46 governance checks",
        "33/33 mutation",
    ]
    forbidden = [
        "Nothing is optional",
        "Load ALL of it",
        "7 Mandatory Steps",
        "11/11 PASS",
        "6/6 detected",
        "runner.py before Done",
    ]

    missing = [marker for marker in required if marker not in content]
    stale = [marker for marker in forbidden if marker in content]

    if missing:
        return FAIL, (
            "GOV-T36: README missing current runtime marker(s): "
            + ", ".join(missing)
        )
    if stale:
        return FAIL, (
            "GOV-T36: README contains stale public-contract marker(s): "
            + ", ".join(stale)
        )

    return PASS, "GOV-T36: README matches the current v8 public runtime contract."


def test_gov_t38_release_contract_entrypoints():
    """GOV-T38: Public/runtime entrypoints must route through current v8 execution."""
    if not _is_aos_source_repo():
        return SKIP_EXPECTED, "test_gov_t38_release_contract_entrypoints: AOS-source-only check."

    files = {
        "root AGENTS": Path("AGENTS.md"),
        "nested AGENTS": Path(".agent/AGENTS.md"),
        "start.py": Path(".agent/start.py"),
        "init-project": Path(".agent/03-workflows/init-project.md"),
        "workflow": Path(".github/workflows/aos-verify.yml"),
    }
    missing_files = [label for label, path in files.items() if not path.exists()]
    if missing_files:
        return FAIL, (
            "GOV-T38: required release entrypoint(s) missing: "
            + ", ".join(missing_files)
        )

    root_agents = files["root AGENTS"].read_text(encoding="utf-8")
    nested_agents = files["nested AGENTS"].read_text(encoding="utf-8")
    start = files["start.py"].read_text(encoding="utf-8")
    init = files["init-project"].read_text(encoding="utf-8")
    workflow = files["workflow"].read_text(encoding="utf-8")

    problems = []
    for label, content in [
        ("root AGENTS", root_agents),
        ("nested AGENTS", nested_agents),
    ]:
        if "execution_gate.py" not in content:
            problems.append(f"{label}: missing Execution Gate")
        if "evidence_recorder.py" not in content:
            problems.append(f"{label}: missing Evidence Recorder")

    start_verify_path = 'str(agent_dir / "governance" / "verify.py")'
    start_runner_path = 'str(agent_dir / "governance" / "runner.py")'
    if start_verify_path not in start:
        problems.append("start.py: --check must execute full verify.py")
    if start_runner_path in start:
        problems.append("start.py: --check still executes runner.py")

    for required in ["profiles/", "task-contracts/", "evidence/README.md"]:
        if required not in init:
            problems.append(f"init-project: missing {required}")
    if "execution_gate.py" not in init:
        problems.append("init-project: missing Execution Gate validation")
    if "governance/verify.py" not in init:
        problems.append("init-project: missing full verification")

    if "- main" not in workflow or "workflow_dispatch:" not in workflow:
        problems.append("workflow: main/manual release verification trigger missing")
    if "aos-v8-convergence" in workflow:
        problems.append("workflow: stale convergence branch trigger remains")

    readme = Path("README.md").read_text(encoding="utf-8")
    for launcher in ["bootstrap.sh | sh", "bootstrap.ps1 | iex"]:
        if launcher not in readme:
            problems.append(f"README: one-command {launcher} entrypoint missing")
    if "Copy `.agent` into your project" in readme:
        problems.append("README: unsafe full-state copy onboarding remains")

    if "profiles/technology/" not in init:
        problems.append("init-project: Technology Profile install scope missing")
    for forbidden_state in [
        "profiles/project.json",
        "task-contracts/current.json",
        "04-memory/",
    ]:
        if forbidden_state not in init:
            problems.append(
                f"init-project: source-state exclusion missing for {forbidden_state}"
            )

    if problems:
        return FAIL, "GOV-T38: release contract drift: " + "; ".join(problems)

    return PASS, "GOV-T38: release entrypoints match the current v8 execution runtime."


def test_gov_t40_version_consistency():
    """GOV-T40: Active runtime/public version markers match .agent/VERSION."""
    version_path = Path(".agent/VERSION")
    if not version_path.exists():
        return FAIL, "GOV-T40: .agent/VERSION missing."

    version_text = version_path.read_text(encoding="utf-8")
    match = re.search(r"^aos_version:\s*([^\s]+)\s*$", version_text, re.MULTILINE)
    if not match:
        return FAIL, "GOV-T40: aos_version missing from .agent/VERSION."

    version = match.group(1)
    label = f"v{version}"

    required = {
        "AGENTS.md": label,
        ".agent/AGENTS.md": label,
        ".agent/INDEX.md": label,
        ".agent/01-core/boot-manifest.md": label,
        ".agent/03-workflows/init-project.md": label,
        ".agent/03-workflows/end-session.md": label,
        ".agent/03-workflows/start-session.md": label,
        ".agent/05-references/books/00-master-index.md": label,
        ".agent/governance/runner.py": label,
        ".agent/04-memory/project-context.md": label,
        ".agent/04-memory/active-tasks.md": label,
        ".agent/04-memory/learned-mistakes.md": label,
    }
    if _is_aos_source_repo():
        required["README.md"] = label

    problems = []
    for rel, marker in required.items():
        path = Path(rel)
        if not path.exists():
            problems.append(f"{rel}: missing")
            continue
        content = path.read_text(encoding="utf-8")
        if marker not in content:
            problems.append(f"{rel}: missing {marker}")

    init = Path(".agent/03-workflows/init-project.md")
    if init.exists():
        content = init.read_text(encoding="utf-8")
        if f"aos_version: {version}" not in content:
            problems.append("init-project: VERSION example mismatch")

    if not version.endswith("-dev"):
        stale_markers = (
            "v8.0-" + "dev",
            "8.0.0-" + "dev",
            "version-8.0--" + "dev",
        )
        scan_files = set(required) | {
            ".agent/01-core/operating-contract.md",
            ".agent/01-core/session-prompt.md",
            ".agent/01-core/task-classification.md",
            ".agent/01-core/token-budget.md",
            ".agent/01-core/wiring-registry.md",
            ".agent/governance/test_memory.py",
            ".agent/governance/test_mutations.py",
            ".agent/governance/test_rules.py",
            ".agent/governance/test_state.py",
            ".agent/04-memory/decisions.md",
        }
        for rel in sorted(scan_files):
            path = Path(rel)
            if not path.exists():
                continue
            content = path.read_text(encoding="utf-8")
            for stale in stale_markers:
                if stale in content:
                    problems.append(f"{rel}: stale marker {stale}")
                    break

    if problems:
        return FAIL, "GOV-T40: version drift: " + "; ".join(problems)

    return PASS, f"GOV-T40: active runtime/public markers match {label}."

def test_gov_t41_readme_complete_capability_map():
    """GOV-T41: README must preserve the complete colored-text capability showcase."""
    if not _is_aos_source_repo():
        return SKIP_EXPECTED, "test_gov_t41_readme_complete_capability_map: AOS-source-only check."

    path = Path("README.md")
    if not path.exists():
        return FAIL, "GOV-T41: README.md missing."

    content = path.read_text(encoding="utf-8")

    required_sections = [
        "# ⚡ Quick Start — One Command",
        "# What AOS gives you",
        "# How AOS works",
        "# What bootstrap does under the hood",
        "# Engineering lifecycle",
        "# Capability map",
        "# Core runtime",
        "# Security model",
        "# Testing, QA & evidence",
        "# DevOps, production & release discipline",
        "# Memory that learns without becoming stale",
        "# Knowledge system",
        "# Governance strength",
        "# Project structure",
        "# Source of truth",
        "## Visual legend",
    ]

    required_capabilities = [
        "Architecture", "Security", "Testing & QA", "DevOps",
        "Reliability", "Database & Performance", "API & Network",
        "Frontend & UX", "Mobile QA", "Memory & Learning",
        "Autonomous Execution", "Context Control", "Executable Evidence",
        "Governance", "Engineering Knowledge",
    ]

    required_diagrams = [
        "🟦 TASK",
        "🔎 1. PREFLIGHT",
        "🟦 INTAKE",
        "🤖 AOS v8",
        "🟦 NAMED CHECK",
    ]

    required_colors = ["🟦", "🟪", "🟨", "🟩", "🟥"]

    problems = []
    missing = [item for item in required_sections if item not in content]
    if missing:
        problems.append("sections: " + ", ".join(missing))

    missing = [item for item in required_capabilities if item not in content]
    if missing:
        problems.append("capabilities: " + ", ".join(missing))

    missing = [item for item in required_diagrams if item not in content]
    if missing:
        problems.append("text diagrams: " + ", ".join(missing))

    missing = [item for item in required_colors if item not in content]
    if missing:
        problems.append("visual colors: " + ", ".join(missing))

    mermaid_marker = "```" + "mermaid"
    if mermaid_marker in content:
        problems.append("Mermaid remains in README; colored text diagrams are the standard.")

    quick_start_markers = [
        "raw.githubusercontent.com/Nezarabdluah/My-Programming-Workflow/main/bootstrap.sh",
        "raw.githubusercontent.com/Nezarabdluah/My-Programming-Workflow/main/bootstrap.ps1",
        "inside your project",
        "BLOCKED before any write",
        "Safe upgrade",
        "NEEDS_REVIEW",
        "READY",
    ]
    missing_quick_start = [
        item for item in quick_start_markers if item not in content
    ]
    if missing_quick_start:
        problems.append(
            "quick start: " + ", ".join(missing_quick_start)
        )

    if "README is the complete user-facing overview" not in content:
        problems.append("README/source-of-truth boundary missing")
    if "Executable authority remains here:" not in content:
        problems.append("executable-authority table missing")

    if problems:
        return FAIL, "GOV-T41: incomplete README showcase: " + "; ".join(problems)

    return PASS, "GOV-T41: README preserves the complete colored-text capability showcase."


def test_gov_t46_zero_setup_launchers_are_thin_and_safe():
    """GOV-T46: Public launchers stay thin and route all target writes through bootstrap."""
    if not _is_aos_source_repo():
        return SKIP_EXPECTED, "GOV-T46: AOS-source-only launcher contract check."

    readme_path = Path("README.md")
    shell_path = Path("bootstrap.sh")
    powershell_path = Path("bootstrap.ps1")
    missing = [
        str(path) for path in [readme_path, shell_path, powershell_path]
        if not path.exists()
    ]
    if missing:
        return FAIL, "GOV-T46: missing public launcher file(s): " + ", ".join(missing)

    readme = readme_path.read_text(encoding="utf-8")
    shell = shell_path.read_text(encoding="utf-8")
    powershell = powershell_path.read_text(encoding="utf-8")
    quick_start = readme.split("# What AOS gives you", 1)[0]

    problems = []
    shell_markers = [
        "AOS_REPO_URL", "AOS_REF", "AOS_TARGET", "$(pwd -P)",
        "mktemp -d", "trap cleanup",
        '"$AOS_TEMP_DIR/.agent/bootstrap.py" "$AOS_TARGET"',
    ]
    powershell_markers = [
        "AOS_REPO_URL", "AOS_REF", "AOS_TARGET", "(Get-Location).Path",
        "GetTempPath", "finally",
        '$Bootstrap = Join-Path $AosTempDir ".agent/bootstrap.py"',
    ]
    for marker in shell_markers:
        if marker not in shell:
            problems.append(f"bootstrap.sh missing {marker}")
    for marker in powershell_markers:
        if marker not in powershell:
            problems.append(f"bootstrap.ps1 missing {marker}")

    for marker in ["bootstrap.sh | sh", "bootstrap.ps1 | iex"]:
        if marker not in quick_start:
            problems.append(f"Quick Start missing {marker}")
    if "python .agent/bootstrap.py /path/to/your-project" in quick_start:
        problems.append("Quick Start still requires a local AOS source checkout")

    if problems:
        return FAIL, "GOV-T46: " + "; ".join(problems)
    return PASS, "GOV-T46: zero-setup launchers are thin, temporary, and bootstrap-routed."
