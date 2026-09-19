"""AOS Governance — State Tests (v8.0-dev)

GOV-T01: Current task state validity
GOV-T02: Acceptance criteria for active non-trivial tasks
GOV-T09: Ordered state history for completed non-trivial tasks
"""
import re
from pathlib import Path

PASS = "PASS"
FAIL = "FAIL"
SKIP_EXPECTED = "SKIP_EXPECTED"
SKIP_UNSUPPORTED = "SKIP_UNSUPPORTED"

VALID_STATES = {
    "Draft", "Clarify", "Approved", "Planning", "Ready",
    "Executing", "Validating", "Done"
}

STATE_PATTERN = re.compile(
    r"(?:\*\*)?(?:SDD\s+)?State(?:\*\*)?\s*:\s*"
    r"(?:\*\*)?\[?([A-Za-z]+)\]?(?:\*\*)?",
    re.IGNORECASE,
)


def _read_file(rel_path):
    path = Path(rel_path)
    if path.exists():
        return path.read_text(encoding="utf-8")
    return None


def _task_sections(content):
    """Return Markdown sections that look like current task records."""
    sections = re.split(r"(?=^##\s+)", content, flags=re.MULTILINE)
    return [
        section for section in sections
        if re.search(r"^##\s+", section, flags=re.MULTILINE)
    ]


def _extract_state(section):
    match = STATE_PATTERN.search(section)
    if not match:
        return None
    raw = match.group(1)
    for state in VALID_STATES:
        if raw.lower() == state.lower():
            return state
    return raw


def _is_non_trivial(section):
    return bool(re.search(r"(?:🟡|🔴)", section))


def test_gov_t01_state_validity():
    """GOV-T01: Every current task with a State field uses a valid state."""
    content = _read_file(".agent/04-memory/active-tasks.md")
    if content is None:
        return FAIL, "GOV-T01: active-tasks.md not found."

    sections = _task_sections(content)
    states = []

    for section in sections:
        state = _extract_state(section)
        if state is not None:
            states.append(state)

    if not states:
        meaningful = [
            line for line in content.splitlines()
            if line.strip()
            and not line.lstrip().startswith(("#", ">", "---"))
        ]
        if len(meaningful) < 3:
            return SKIP_EXPECTED, (
                "GOV-T01: active-tasks.md contains no active task."
            )
        return FAIL, (
            "GOV-T01: Task content exists but no parseable State field was found."
        )

    invalid = [state for state in states if state not in VALID_STATES]
    if invalid:
        return FAIL, f"GOV-T01: Invalid state(s): {sorted(set(invalid))}"

    return PASS, f"GOV-T01: Current task state(s) valid: {states}"


def test_gov_t02_acceptance_criteria():
    """GOV-T02: Active 🟡/🔴 tasks past Clarify have acceptance criteria."""
    content = _read_file(".agent/04-memory/active-tasks.md")
    if content is None:
        return SKIP_EXPECTED, "GOV-T02: active-tasks.md not found."

    required_states = {"Approved", "Planning", "Ready", "Executing", "Validating"}
    candidates = []

    for section in _task_sections(content):
        state = _extract_state(section)
        if _is_non_trivial(section) and state in required_states:
            candidates.append(section)

    if not candidates:
        return SKIP_EXPECTED, (
            "GOV-T02: No active 🟡/🔴 task past Clarify requires criteria."
        )

    for section in candidates:
        has_heading = bool(re.search(
            r"^###\s+Acceptance Criteria\s*$",
            section,
            flags=re.IGNORECASE | re.MULTILINE,
        ))
        has_structured_language = bool(re.search(
            r"\b(?:Given|When|Then|must|shall|criterion|criteria)\b",
            section,
            flags=re.IGNORECASE,
        ))
        if not (has_heading and has_structured_language):
            return FAIL, (
                "GOV-T02: Active 🟡/🔴 task is missing structured "
                "Acceptance Criteria."
            )

    return PASS, (
        f"GOV-T02: Acceptance criteria present for {len(candidates)} "
        "active non-trivial task(s)."
    )


def test_gov_t09_workflow_integrity():
    """GOV-T09: Completed 🟡/🔴 tasks must record ordered SDD state history."""
    content = _read_file(".agent/04-memory/active-tasks.md")
    if content is None:
        return SKIP_EXPECTED, "GOV-T09: active-tasks.md not found."

    completed = []
    for section in _task_sections(content):
        if _is_non_trivial(section) and _extract_state(section) == "Done":
            completed.append(section)

    if not completed:
        return PASS, (
            "GOV-T09: No completed 🟡/🔴 task requires state-history validation."
        )

    required = [
        "Draft", "Clarify", "Approved", "Planning",
        "Ready", "Executing", "Validating", "Done",
    ]

    for section in completed:
        match = re.search(
            r"^###\s+State History\s*$\n(.*?)(?=^###\s+|^##\s+|\Z)",
            section,
            flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
        )
        if not match:
            return FAIL, (
                "GOV-T09: Completed 🟡/🔴 task is missing State History."
            )

        history = match.group(1)
        positions = [history.find(state) for state in required]
        if any(position < 0 for position in positions):
            missing = [
                state for state, position in zip(required, positions)
                if position < 0
            ]
            return FAIL, (
                "GOV-T09: Completed 🟡/🔴 task has incomplete State History; "
                f"missing: {', '.join(missing)}"
            )

        if positions != sorted(positions):
            return FAIL, (
                "GOV-T09: Completed 🟡/🔴 task State History is out of order."
            )

    return PASS, (
        f"GOV-T09: {len(completed)} completed 🟡/🔴 task(s) "
        "have ordered SDD state history."
    )
