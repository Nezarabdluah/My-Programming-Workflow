"""AOS Governance — Context Broker Tests (v8 Sprint 2)."""

import importlib.util
import json
from pathlib import Path

PASS = "PASS"
FAIL = "FAIL"


def _load_broker():
    path = Path(".agent/01-core/context_broker.py")
    if not path.exists():
        raise RuntimeError("context_broker.py missing")
    spec = importlib.util.spec_from_file_location("aos_context_broker", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def test_gov_t12_context_broker_minimality():
    """GOV-T12: Security task must not load unrelated DB/API rule files."""
    broker = _load_broker()
    context_map = _json(".agent/01-core/context-map.json")
    project = _json(".agent/profiles/project.json")

    task = {
        "task_id": "mutation-free-t12",
        "classification": "sensitive",
        "capabilities": ["security"],
    }
    result = broker.resolve_context(task, project, context_map)
    paths = {resource["path"] for resource in result["resources"]}

    required = ".agent/02-rules/security-checklist.md"
    forbidden = {
        ".agent/02-rules/database-performance.md",
        ".agent/02-rules/network-and-api.md",
        ".agent/02-rules/architecture-and-design.md",
    }

    if required not in paths:
        return FAIL, "GOV-T12: security capability did not load security rule."
    leaked = sorted(paths.intersection(forbidden))
    if leaked:
        return FAIL, f"GOV-T12: unrelated resources leaked into context: {leaked}"

    return PASS, f"GOV-T12: minimal security context resolved ({len(paths)} paths)."


def test_gov_t13_profile_gate():
    """GOV-T13: Profile-gated resources load only when profile is active."""
    broker = _load_broker()
    context_map = _json(".agent/01-core/context-map.json")
    project = _json(".agent/profiles/project.json")

    task = {
        "task_id": "profile-gate-t13",
        "classification": "medium",
        "capabilities": ["full-stack-vertical"],
    }

    result = broker.resolve_context(task, project, context_map)
    paths = {resource["path"] for resource in result["resources"]}
    vertical = ".agent/02-rules/vertical-slice-governance.md"

    if vertical in paths:
        return FAIL, "GOV-T13: full-stack resource loaded without full-stack-web profile."
    if not result["skipped"]:
        return FAIL, "GOV-T13: broker did not record profile-gated skip."

    project_with_profile = dict(project)
    project_with_profile["technology_profiles"] = list(
        project.get("technology_profiles", [])
    ) + ["full-stack-web"]
    activated = broker.resolve_context(task, project_with_profile, context_map)
    active_paths = {resource["path"] for resource in activated["resources"]}

    if vertical not in active_paths:
        return FAIL, "GOV-T13: full-stack resource missing after profile activation."

    return PASS, "GOV-T13: profile-gated resource activation works correctly."


def test_gov_t14_current_contract_resolves():
    """GOV-T14: Current task contract resolves without unknown capabilities."""
    broker = _load_broker()
    task = _json(".agent/task-contracts/current.json")
    project = _json(".agent/profiles/project.json")
    context_map = _json(".agent/01-core/context-map.json")

    try:
        result = broker.resolve_context(task, project, context_map)
    except Exception as exc:
        return FAIL, f"GOV-T14: current task contract failed to resolve: {exc}"

    if not result["resources"]:
        return FAIL, "GOV-T14: current task resolved to empty context."

    return PASS, (
        f"GOV-T14: {task['task_id']} resolved "
        f"{len(result['resources'])} resource entries."
    )
