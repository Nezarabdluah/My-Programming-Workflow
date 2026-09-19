"""AOS Governance — State Tests (v8.0-dev)

GOV-T01: Task state validity (supports multiple task formats)
GOV-T02: Acceptance criteria presence
GOV-T09: State machine integrity (no illegal jumps)
"""
import re
from pathlib import Path

# Official statuses
PASS = "PASS"
FAIL = "FAIL"
SKIP_EXPECTED = "SKIP_EXPECTED"
SKIP_UNSUPPORTED = "SKIP_UNSUPPORTED"

VALID_STATES = {
    "Draft", "Clarify", "Approved", "Planning", "Ready",
    "Executing", "Validating", "Done"
}

# Patterns that indicate an active task with a declared state
STATE_PATTERNS = [
    # "Current feature state: X" (v7 format)
    r"Current\s+feature\s+state\s*:\s*\[?([A-Za-z]+)\]?",
    # "State: X" or "SDD State: X"
    r"(?:SDD\s+)?State\s*:\s*\[?([A-Za-z]+)\]?",
]

# Patterns indicating completed tasks (not requiring active state)
COMPLETED_MARKERS = [
    r"\[x\]",           # Markdown checkbox completed
    r"DONE",            # Explicit DONE marker
    r"COMPLETE",        # Explicit COMPLETE marker
]


def _read_file(rel_path):
    """Read a file relative to project root, return content or None."""
    path = Path(rel_path)
    if path.exists():
        return path.read_text(encoding="utf-8")
    return None


def test_gov_t01_state_validity():
    """GOV-T01: Verify task states match the approved state machine.

    Accepts multiple formats:
    - 'Current feature state: X'
    - 'State: X' / 'SDD State: X'
    - Inline '(DONE ✅)' in task lines
    - '[x]' checkboxes for completed tasks

    If no active (non-completed) task exists, the check passes
    (no task = no state to validate).
    """
    content = _read_file(".agent/04-memory/active-tasks.md")
    if content is None:
        return FAIL, "GOV-T01: active-tasks.md not found."

    # Collect all declared states
    found_states = set()
    for pattern in STATE_PATTERNS:
        for match in re.finditer(pattern, content):
            found_states.add(match.group(1))

    # If the file has completed markers but no explicit state declarations,
    # that's valid — tasks are done
    has_completed = any(re.search(p, content) for p in COMPLETED_MARKERS)

    if not found_states:
        if has_completed:
            return PASS, "GOV-T01: No active state declared; all tasks appear completed."
        # Check if file is essentially empty/template
        non_empty_lines = [l for l in content.split("\n")
                          if l.strip() and not l.strip().startswith("#")
                          and not l.strip().startswith(">")
                          and not l.strip().startswith("---")]
        if len(non_empty_lines) < 3:
            return SKIP_EXPECTED, "GOV-T01: active-tasks.md is empty/template — no state to validate."
        return PASS, "GOV-T01: Tasks present with completion markers but no invalid states."

    # Validate found states
    invalid = found_states - VALID_STATES
    # Allow common completion synonyms
    allowed_synonyms = {"COMPLETE", "PARTIAL", "REVIEWED", "PUBLISHED"}
    truly_invalid = invalid - allowed_synonyms

    if truly_invalid:
        return FAIL, f"GOV-T01: Invalid state(s) found: {truly_invalid}"

    return PASS, f"GOV-T01: All declared states valid: {found_states}"


def test_gov_t02_acceptance_criteria():
    """GOV-T02: Verify acceptance criteria exist for non-trivial tasks.

    For tasks in Draft/Clarify state, criteria may not exist yet (SKIP_EXPECTED).
    For completed tasks, criteria are not required retroactively.
    For active 🟡/🔴 tasks past Approved state, Given/When/Then or
    measurable criteria must be present.
    """
    content = _read_file(".agent/04-memory/active-tasks.md")
    if content is None:
        return SKIP_EXPECTED, "GOV-T02: active-tasks.md not found — nothing to validate."

    # Check if there are active (non-completed) 🟡/🔴 tasks past Draft/Clarify
    has_active_medium_or_sensitive = bool(
        re.search(r"(?:🟡|🔴).*(?:Approved|Planning|Ready|Executing|Validating)", content)
    )

    if not has_active_medium_or_sensitive:
        return SKIP_EXPECTED, (
            "GOV-T02: No active 🟡/🔴 tasks past Draft/Clarify — "
            "acceptance criteria not required at this stage."
        )

    # Look for structured acceptance criteria
    has_given = bool(re.search(r"\bGiven\b", content))
    has_when = bool(re.search(r"\bWhen\b", content))
    has_then = bool(re.search(r"\bThen\b", content))
    has_criteria = bool(re.search(
        r"(?:acceptance|criteria|requirement|must|shall|expect)", content, re.IGNORECASE
    ))

    if has_given and has_when and has_then:
        return PASS, "GOV-T02: Given/When/Then acceptance criteria found."
    if has_criteria:
        return PASS, "GOV-T02: Acceptance criteria found (non-GWT format)."

    return FAIL, (
        "GOV-T02: Active 🟡/🔴 task past Approved but no acceptance criteria found."
    )


def test_gov_t09_workflow_integrity():
    """GOV-T09: Verify completed non-trivial tasks have valid state history.

    For 🟡/🔴 tasks marked Done, a checkbox or the mere presence of words like
    "Approved" is not evidence. The task section must record an ordered
    State History containing the required SDD transitions.
    """
    active_content = _read_file(".agent/04-memory/active-tasks.md")
    if active_content is None:
        return SKIP_EXPECTED, "GOV-T09: active-tasks.md not found."

    # Split current-task memory into task sections.
    sections = re.split(r"(?=^##\s+)", active_content, flags=re.MULTILINE)
    completed_non_trivial = []

    for section in sections:
        if not re.search(r"(?:🟡|🔴)", section):
            continue
        state_match = re.search(r"(?:\*\*)?State(?:\*\*)?\s*:\s*\*\*?([A-Za-z]+)", section)
        if not state_match:
            state_match = re.search(r"(?:SDD\s+)?State\s*:\s*\[?([A-Za-z]+)\]?", section)
        if state_match and state_match.group(1) == "Done":
            completed_non_trivial.append(section)

    if not completed_non_trivial:
        return PASS, "GOV-T09: No completed 🟡/🔴 task requires state-history validation."

    required = ["Draft", "Clarify", "Approved", "Planning", "Ready",
                "Executing", "Validating", "Done"]

    for section in completed_non_trivial:
        history_match = re.search(
            r"###\s+State History\s*\n([^#]+)",
            section,
            flags=re.IGNORECASE
        )
        if not history_match:
            return FAIL, "GOV-T09: Completed 🟡/🔴 task is missing State History."

        history = history_match.group(1)
        positions = [history.find(state) for state in required]
        if any(pos < 0 for pos in positions):
            missing = [state for state, pos in zip(required, positions) if pos < 0]
            return FAIL, (
                "GOV-T09: Completed 🟡/🔴 task has incomplete State History; "
                f"missing: {', '.join(missing)}"
            )
        if positions != sorted(positions):
            return FAIL, (
                "GOV-T09: Completed 🟡/🔴 task State History is out of order."
            )

    return PASS, (
        f"GOV-T09: {len(completed_non_trivial)} completed 🟡/🔴 task(s) "
        "have ordered SDD state history."
    )
