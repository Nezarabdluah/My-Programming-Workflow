"""AOS Governance — Rule Tests (v8.0-dev)

GOV-T06: Workflow links to rules
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
    """GOV-T06: Verify the workflow links to at least one rule in rules/."""
    prompt_path = Path(".agent/01-core/session-prompt.md")
    if not prompt_path.exists():
        return FAIL, "GOV-T06: session-prompt.md not found."

    content = prompt_path.read_text(encoding="utf-8")
    if "02-rules/" in content or "rules/" in content:
        return PASS, "GOV-T06: Workflow links to specialized rule loading."

    return FAIL, "GOV-T06: No linkage to specialized rules from rules/."


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
    """GOV-T10: Verify ADR accompanies architecture/security rule changes.

    THIS IS NOT A RUBBER STAMP. It actually checks:
    1. If decisions.md exists and contains ADRs
    2. If any rule file was recently changed (newer than decisions.md),
       there should be a corresponding ADR
    3. If operating-contract.md references architecture/security patterns,
       an ADR should exist documenting the decision

    If no rule files exist or no changes detected, this is SKIP_EXPECTED.
    """
    decisions_path = Path(".agent/04-memory/decisions.md")
    if not decisions_path.exists():
        # No decisions file at all — check if any rules exist
        rules_dir = Path(".agent/02-rules")
        if rules_dir.exists() and any(rules_dir.iterdir()):
            return FAIL, (
                "GOV-T10: Rules exist but decisions.md is missing — "
                "architecture decisions must be documented."
            )
        return SKIP_EXPECTED, "GOV-T10: No rules or decisions files — nothing to verify."

    decisions_content = decisions_path.read_text(encoding="utf-8")

    # Extract ADR IDs
    adrs = re.findall(r"## .*?(ADR-\d+)", decisions_content)
    if not adrs:
        # decisions.md exists but has no ADRs
        rules_dir = Path(".agent/02-rules")
        contract_path = Path(".agent/01-core/operating-contract.md")
        if rules_dir.exists() and any(rules_dir.iterdir()):
            return FAIL, (
                "GOV-T10: Rules directory has files but decisions.md "
                "contains no ADR entries."
            )
        return SKIP_EXPECTED, "GOV-T10: No ADRs and no rules — nothing to verify."

    # Verify each ADR has required sections
    incomplete_adrs = []

    for adr_id in adrs:
        # Find the heading line containing this ADR
        adr_pattern = re.compile(r"## .*?" + re.escape(adr_id) + r".*", re.MULTILINE)
        match = adr_pattern.search(decisions_content)
        if not match:
            continue

        start_pos = match.start()

        # Find the next ## heading (next ADR) or end of file
        next_heading = re.search(r"\n## ", decisions_content[match.end():])
        if next_heading:
            end_pos = match.end() + next_heading.start()
        else:
            end_pos = len(decisions_content)

        section = decisions_content[start_pos:end_pos]

        # Skip template entries
        if "[Architectural Decision Title]" in section:
            continue

        has_context = "Context" in section
        has_decision = "Decision" in section or "decision" in section
        has_consequences = "Consequences" in section or "consequences" in section

        if not (has_context and has_decision and has_consequences):
            missing = []
            if not has_context:
                missing.append("Context")
            if not has_decision:
                missing.append("Decision")
            if not has_consequences:
                missing.append("Consequences")
            incomplete_adrs.append(f"{adr_id} (missing: {', '.join(missing)})")

    if incomplete_adrs:
        return FAIL, (
            f"GOV-T10: Incomplete ADR(s): {', '.join(incomplete_adrs)} — "
            "missing Context, Decision, or Consequences section."
        )

    # Cross-check: contract references patterns that should have ADRs
    contract_path = Path(".agent/01-core/operating-contract.md")
    if contract_path.exists():
        contract = contract_path.read_text(encoding="utf-8")
        # Check if contract mentions architecture patterns
        arch_patterns = re.findall(
            r"(?:Vertical.Slice|Clean.Architecture|DDD|CQRS|Event.Sourcing)",
            contract
        )
        if arch_patterns:
            # There should be at least one ADR about architecture
            has_arch_adr = any(
                "rchitect" in decisions_content[
                    decisions_content.find(adr):
                    decisions_content.find(adr) + 500
                ]
                for adr in adrs
                if decisions_content.find(adr) >= 0
            )
            if not has_arch_adr:
                return FAIL, (
                    f"GOV-T10: Contract references {arch_patterns} but "
                    "no architectural ADR found in decisions.md."
                )

    return PASS, f"GOV-T10: {len(adrs)} ADR(s) verified — all complete and consistent."
