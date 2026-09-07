import re
from pathlib import Path

def test_gov_t03_adr_structure():
    """Verify newly added architectural decisions follow the full ADR format (GOV-T03)"""
    path = Path(".agent/04-memory/decisions.md")
    if not path.exists():
        path = Path(".agent/memory/decisions.md")

    if not path.exists():
        return True, "GOV-T03: Skipped, decisions.md not found."

    content = path.read_text(encoding="utf-8")

    # Check whether any ADR is recorded
    adrs = re.findall(r"## (ADR-\d+)", content)
    for adr in adrs:
        # Every ADR must contain the core sections: context & problem, approved decision, consequences
        adr_section = content[content.find(adr):]
        has_context = "Context" in adr_section
        has_decision = "Decision" in adr_section
        has_consequences = "Consequences" in adr_section

        if not (has_context and has_decision and has_consequences):
            return False, f"GOV-T03: Decision {adr} does not follow the full ADR format."

    return True, "GOV-T03: All architectural decisions follow the standard ADR format."

def test_gov_t04_mistakes_cap():
    """Verify active mistakes do not exceed the 20-mistake cap (GOV-T04)"""
    path = Path(".agent/04-memory/learned-mistakes.md")
    if not path.exists():
        path = Path(".agent/memory/learned-mistakes.md")

    if not path.exists():
        return True, "GOV-T04: Skipped."

    content = path.read_text(encoding="utf-8")
    # Count table rows holding a recorded mistake (English type tags).
    # NOTE: "[Type B]" added 2026-09-07 — learned-mistakes.md uses English tags (ADR-005).
    rows = [line for line in content.split("\n") if line.strip().startswith("|") and "[Type B]" in line]

    if len(rows) > 20:
        return False, f"GOV-T04: Active-mistake cap exceeded (current: {len(rows)} | cap: 20)."

    return True, f"GOV-T04: Active mistakes under control (current: {len(rows)})."

def test_gov_t05_handoff_validity():
    """Verify cumulative memory files are complete and ready (GOV-T05)"""
    required_files = [
        "project-context.md",
        "learned-mistakes.md",
        "active-tasks.md",
        "decisions.md"
    ]

    memory_dirs = [Path(".agent/04-memory"), Path(".agent/memory")]

    # Locate the actual memory folder
    active_dir = None
    for d in memory_dirs:
        if d.exists():
            active_dir = d
            break

    if not active_dir:
        return False, "GOV-T05: No cumulative memory folder found (memory/)."

    for file_name in required_files:
        file_path = active_dir / file_name
        if not file_path.exists():
            return False, f"GOV-T05: Mandatory memory file {file_name} missing."

    return True, f"GOV-T05: Cumulative memory module complete in {active_dir.name}/."
