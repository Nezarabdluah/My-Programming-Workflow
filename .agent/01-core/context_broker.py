"""AOS v8 Context Broker.

Deterministically resolves task capabilities into the minimum resource set.
No external dependencies; uses JSON contracts and the standard library only.

Usage:
  python .agent/01-core/context_broker.py
  python .agent/01-core/context_broker.py --task .agent/task-contracts/current.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(".")
DEFAULT_MAP = ROOT / ".agent/01-core/context-map.json"
DEFAULT_PROJECT = ROOT / ".agent/profiles/project.json"
DEFAULT_TASK = ROOT / ".agent/task-contracts/current.json"


class ContextBrokerError(ValueError):
    pass


def load_json(path: Path) -> dict:
    if not path.exists():
        raise ContextBrokerError(f"Missing contract: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ContextBrokerError(f"Invalid JSON in {path}: {exc}") from exc


def _active_profiles(project: dict) -> set[str]:
    profiles = project.get("technology_profiles", [])
    if not isinstance(profiles, list):
        raise ContextBrokerError("project.technology_profiles must be a list")
    return {str(profile) for profile in profiles}


def resolve_context(task: dict, project: dict, context_map: dict) -> dict:
    classification = task.get("classification")
    if classification not in {"simple", "medium", "sensitive"}:
        raise ContextBrokerError(
            "task.classification must be one of: simple, medium, sensitive"
        )

    capabilities = task.get("capabilities", [])
    if not isinstance(capabilities, list):
        raise ContextBrokerError("task.capabilities must be a list")

    registry = context_map.get("capabilities", {})
    if not isinstance(registry, dict):
        raise ContextBrokerError("context-map.capabilities must be an object")

    profiles = _active_profiles(project)
    selected = []
    skipped = []
    seen = set()

    for capability in capabilities:
        if capability not in registry:
            raise ContextBrokerError(f"Unknown capability: {capability}")

        definition = registry[capability]
        required_profile = definition.get("requires_profile")
        if required_profile and required_profile not in profiles:
            skipped.append({
                "capability": capability,
                "reason": f"requires profile: {required_profile}",
            })
            continue

        for resource in definition.get("resources", []):
            path = resource.get("path")
            mode = resource.get("mode")
            key = (path, mode, tuple(resource.get("anchors", [])))
            if key in seen:
                continue
            seen.add(key)
            selected.append({
                "capability": capability,
                **resource,
            })

    return {
        "task_id": task.get("task_id"),
        "classification": classification,
        "active_profiles": sorted(profiles),
        "capabilities": capabilities,
        "resources": selected,
        "skipped": skipped,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve AOS task context")
    parser.add_argument("--task", default=str(DEFAULT_TASK))
    parser.add_argument("--project", default=str(DEFAULT_PROJECT))
    parser.add_argument("--map", dest="context_map", default=str(DEFAULT_MAP))
    args = parser.parse_args()

    try:
        task = load_json(Path(args.task))
        project = load_json(Path(args.project))
        context_map = load_json(Path(args.context_map))
        result = resolve_context(task, project, context_map)
    except ContextBrokerError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2))
        return 1

    print(json.dumps({"status": "PASS", "context": result}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
