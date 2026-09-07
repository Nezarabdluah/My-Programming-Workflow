import re
from pathlib import Path

VALID_STATES = {"Draft", "Clarify", "Approved", "Planning", "Ready", "Executing", "Validating", "Done"}

def test_gov_t01_state_validity():
    """Verify the current feature state matches the approved state machine (GOV-T01)"""
    path = Path(".agent/04-memory/active-tasks.md")
    if not path.exists():
        return False, "GOV-T01: active-tasks.md not found."

    content = path.read_text(encoding="utf-8")
    state_match = re.search(r"Current feature state.*:\s*\[?([A-Za-z]+)\]?", content)
    if not state_match:
        return False, "GOV-T01: No current feature state declared in active-tasks.md."

    state = state_match.group(1)
    if state not in VALID_STATES:
        return False, f"GOV-T01: Detected state '{state}' is invalid."
    return True, f"GOV-T01: Current feature state is valid and compliant: {state}"

def test_gov_t02_acceptance_criteria():
    """Verify acceptance criteria exist in Given/When/Then engineering form (GOV-T02)"""
    path = Path(".agent/04-memory/active-tasks.md")
    if not path.exists():
        return True, "GOV-T02: Skipped, active-tasks.md not created yet."

    content = path.read_text(encoding="utf-8")

    # A Draft/Clarify task may not carry complete acceptance criteria yet
    if "Current feature state: Draft" in content or "Current feature state: Clarify" in content:
        return True, "GOV-T02: Skipped, task is in Draft/Clarify state."

    # Check for the keyword trio
    has_given = "Given" in content or "given" in content
    has_when = "When" in content or "when" in content
    has_then = "Then" in content or "then" in content

    if not (has_given and has_when and has_then):
        return False, "GOV-T02: No complete Given / When / Then acceptance criteria found."
    return True, "GOV-T02: Given/When/Then acceptance criteria found."

def test_gov_t09_workflow_integrity():
    """Verify no illegal jumps across the state machine (GOV-T09)"""
    # Proactive guard: blocks the agent from jumping straight to Done without an approved plan
    active_path = Path(".agent/04-memory/active-tasks.md")
    context_path = Path(".agent/04-memory/project-context.md")

    if not (active_path.exists() and context_path.exists()):
        return True, "GOV-T09: Skipped, memory files incomplete."

    active_content = active_path.read_text(encoding="utf-8")
    context_content = context_path.read_text(encoding="utf-8")

    if "Current feature state: Done" in active_content:
        # A completed task must leave a trace of the approved technical plan
        plan_files = list(Path(".agent").glob("**/implementation_plan.md")) + list(Path().glob("specs/**/*.plan.md"))
        if not plan_files:
            return False, "GOV-T09: Task completed with no approved technical plan on record."

    return True, "GOV-T09: Sequence and state-machine integrity compliant."
