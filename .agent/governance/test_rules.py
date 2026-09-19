"""AOS Governance — Rule Tests (v8.0-dev)

GOV-T06: Canonical boot contract links to task rules
GOV-T07: REF citation validity (project-agnostic source discovery)
GOV-T08: Dead/stale reference detection (project-agnostic)
GOV-T10: ADR consistency — actually verifies changes (not rubber-stamp)
"""
import re
from pathlib import Path

PASS = "PASS"
FAIL = "FAIL"
SKIP_EXPECTED = "SKIP_EXPECTED"
SKIP_UNSUPPORTED = "SKIP_UNSUPPORTED"


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
    """GOV-T10: Verify runtime policy references real approved ADRs.

    Deterministic checks:
    1. decisions.md exists and real ADR entries are structurally complete.
    2. ADR IDs referenced by active Core/rule policy files exist in decisions.md.
    3. v8 migration policy cannot cite a missing ADR.

    This check intentionally does not infer file chronology from filesystem
    modification timestamps because checkout/copy operations make that signal
    unreliable.
    """
    decisions_path = Path(".agent/04-memory/decisions.md")
    if not decisions_path.exists():
        return FAIL, "GOV-T10: decisions.md is missing."

    decisions_content = decisions_path.read_text(encoding="utf-8")
    adr_ids = set(re.findall(r"## .*?(ADR-\d+)", decisions_content))
    if not adr_ids:
        return FAIL, "GOV-T10: decisions.md contains no ADR entries."

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
        if "[Architectural Decision Title]" in section:
            continue
        required_labels = ("Context", "decision", "consequences")
        lowered = section.lower()
        missing = [label for label in required_labels if label.lower() not in lowered]
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
        content = path.read_text(encoding="utf-8")
        refs = set(re.findall(r"ADR-\d+", content))
        checked_refs.update(refs)
        for ref in refs:
            if ref not in adr_ids:
                missing_refs.append(f"{ref} referenced by {rel_path}")

    if missing_refs:
        return FAIL, "GOV-T10: Policy references missing ADRs: " + "; ".join(missing_refs)

    return PASS, (
        f"GOV-T10: {len(adr_ids)} ADR(s) structurally valid; "
        f"{len(checked_refs)} runtime ADR reference(s) resolve."
    )


def test_gov_t36_public_contract_sync():
    """GOV-T36: README public contract must match the current v8 runtime."""
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
        "39 governance checks",
        "26/26 mutation",
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

    if "governance/verify.py" not in start:
        problems.append("start.py: --check must use full verify.py")
    if "governance/runner.py" in start:
        problems.append("start.py: stale runner.py quick-check reference")

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
    if ".agent/install.py" not in readme:
        problems.append("README: sanitized installer entrypoint missing")
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
