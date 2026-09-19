"""AOS v8 Context Broker.

Deterministically resolves explicit, risk-derived, and affected-area-derived
capabilities into the minimum resource set.
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


def _normalize_path(value: str) -> str:
    return value.replace("\\", "/").rstrip("/")


def derive_capabilities(task: dict, project: dict, context_map: dict) -> tuple[list[str], dict]:
    declared = task.get("capabilities", [])
    if not isinstance(declared, list):
        raise ContextBrokerError("task.capabilities must be a list")

    effective = []
    sources: dict[str, list[str]] = {}

    def add(capability: str, source: str) -> None:
        if not isinstance(capability, str) or not capability.strip():
            raise ContextBrokerError("capability must be a non-empty string")
        if capability not in effective:
            effective.append(capability)
        sources.setdefault(capability, [])
        if source not in sources[capability]:
            sources[capability].append(source)

    for capability in declared:
        add(capability, "explicit")

    risk = task.get("risk", {})
    if not isinstance(risk, dict):
        raise ContextBrokerError("task.risk must be an object")

    risk_map = context_map.get("risk_capability_map", {})
    if not isinstance(risk_map, dict):
        raise ContextBrokerError("context-map.risk_capability_map must be an object")

    for risk_key, capabilities in risk_map.items():
        if risk.get(risk_key) is True:
            if not isinstance(capabilities, list):
                raise ContextBrokerError(
                    f"risk capability mapping must be a list: {risk_key}"
                )
            for capability in capabilities:
                add(capability, f"risk:{risk_key}")

    affected_areas = task.get("affected_areas", [])
    if not isinstance(affected_areas, list):
        raise ContextBrokerError("task.affected_areas must be a list")

    area_rules = project.get("area_capability_rules", [])
    if not isinstance(area_rules, list):
        raise ContextBrokerError("project.area_capability_rules must be a list")

    for area in affected_areas:
        if not isinstance(area, str) or not area.strip():
            raise ContextBrokerError("affected area must be a non-empty string")
        normalized_area = _normalize_path(area)

        for rule in area_rules:
            if not isinstance(rule, dict):
                raise ContextBrokerError("area capability rule must be an object")
            prefix = rule.get("prefix")
            capabilities = rule.get("capabilities", [])
            if not isinstance(prefix, str) or not prefix.strip():
                raise ContextBrokerError("area capability rule prefix is invalid")
            if not isinstance(capabilities, list):
                raise ContextBrokerError("area capability rule capabilities must be a list")

            normalized_prefix = _normalize_path(prefix)
            matches = (
                normalized_area == normalized_prefix
                or normalized_area.startswith(normalized_prefix + "/")
            )
            if matches:
                for capability in capabilities:
                    add(capability, f"area:{normalized_prefix}")

    return effective, sources


def resolve_context(task: dict, project: dict, context_map: dict) -> dict:
    classification = task.get("classification")
    if classification not in {"simple", "medium", "sensitive"}:
        raise ContextBrokerError(
            "task.classification must be one of: simple, medium, sensitive"
        )

    declared = task.get("capabilities", [])
    effective, sources = derive_capabilities(task, project, context_map)

    registry = context_map.get("capabilities", {})
    if not isinstance(registry, dict):
        raise ContextBrokerError("context-map.capabilities must be an object")

    profiles = _active_profiles(project)
    selected = []
    skipped = []
    seen = set()

    for capability in effective:
        if capability not in registry:
            raise ContextBrokerError(f"Unknown capability: {capability}")

        definition = registry[capability]
        required_profile = definition.get("requires_profile")
        if required_profile and required_profile not in profiles:
            skipped.append({
                "capability": capability,
                "reason": f"requires profile: {required_profile}",
                "sources": sources.get(capability, []),
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
                "capability_sources": sources.get(capability, []),
                **resource,
            })

    return {
        "task_id": task.get("task_id"),
        "classification": classification,
        "active_profiles": sorted(profiles),
        "declared_capabilities": declared,
        "effective_capabilities": effective,
        "capabilities": effective,
        "capability_sources": sources,
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
