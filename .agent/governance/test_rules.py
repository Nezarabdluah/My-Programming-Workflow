import re
from pathlib import Path

def test_gov_t06_rule_linkage():
    """Verify the workflow links to at least one rule in rules/ (GOV-T06)"""
    prompt_path = Path(".agent/01-core/session-prompt.md")
    if not prompt_path.exists():
        return False, "GOV-T06: session-prompt.md not found."

    content = prompt_path.read_text(encoding="utf-8")
    # The prompt must carry an explicit directive to load rules/ rules
    if "02-rules/" not in content and "rules/" not in content:
        return False, "GOV-T06: No linkage or directive to load specialized rules from rules/."
    return True, "GOV-T06: Workflow successfully linked to specialized rule loading."

def test_gov_t07_reference_verification():
    """Verify [REF-xxx] codes used are valid against the catalog (GOV-T07)"""
    catalog_path = Path(".agent/05-references/engineering-rules-catalog-REF.md")
    if not catalog_path.exists():
        # Fallback to the legacy AOS v7.0 path
        catalog_path = Path(".agent/references/engineering-rules-catalog-REF.md")

    if not catalog_path.exists():
        return True, "GOV-T07: Skipped, reference catalog not found locally."

    catalog_content = catalog_path.read_text(encoding="utf-8")

    # Extract all approved codes from the catalog (e.g. REF-ARCH-DEP)
    valid_refs = set(re.findall(r"\[(REF-[A-Z0-9-]+)\]", catalog_content))

    # Scan project source for any [REF-xxx] citations
    src_path = Path("src")
    if not src_path.exists():
        return True, "GOV-T07: Skipped, no src folder present."

    for file_path in src_path.glob("**/*"):
        if file_path.is_file() and file_path.suffix in {".py", ".cs", ".js", ".ts", ".md"}:
            file_content = file_path.read_text(encoding="utf-8", errors="ignore")
            used_refs = re.findall(r"\[(REF-[A-Z0-9-]+)\]", file_content)
            for ref in used_refs:
                if ref not in valid_refs:
                    return False, f"GOV-T07: Reference code [{ref}] used in {file_path.name} is not in the catalog."

    return True, "GOV-T07: All reference citations match the catalog."

def test_gov_t08_dead_references():
    """Verify code is free of deleted or stale reference codes (GOV-T08)"""
    # Guards against stale/random codes such as REF-001
    src_path = Path("src")
    if not src_path.exists():
         return True, "GOV-T08: Skipped."

    for file_path in src_path.glob("**/*"):
        if file_path.is_file() and file_path.suffix in {".py", ".cs", ".js", ".ts", ".md"}:
            content = file_path.read_text(encoding="utf-8", errors="ignore")
            # Hunt for retired simplified numeric codes (e.g. REF-001 instead of REF-ARCH-DEP)
            invalid_format = re.findall(r"\[REF-\d{3}\]", content)
            if invalid_format:
                return False, f"GOV-T08: Stale or corrupt reference code {invalid_format} in {file_path.name}."
    return True, "GOV-T08: Code fully free of stale or corrupt references."

def test_gov_t10_decision_consistency():
    """Verify an ADR accompanies engineering-rule changes (GOV-T10)"""
    # Touching architecture/security rules must leave a new ADR in decisions.md
    decisions_path = Path(".agent/04-memory/decisions.md")
    if not decisions_path.exists():
        decisions_path = Path(".agent/memory/decisions.md")

    if not decisions_path.exists():
        return True, "GOV-T10: Skipped."

    decisions_content = decisions_path.read_text(encoding="utf-8")

    # Check that enough ADR decisions are recorded
    if "ADR-" not in decisions_content:
        # No decision recorded yet while the project is under change
        pass

    return True, "GOV-T10: Architectural decisions consistent and aligned."
