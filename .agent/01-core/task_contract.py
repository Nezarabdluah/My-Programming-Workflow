"""AOS v8 Task Contract validator."""

from __future__ import annotations

import json
from pathlib import Path

VALID_CLASSIFICATIONS = {"simple", "medium", "sensitive"}
VALID_PROVENANCE = {"policy", "approved_adr", "approved_pattern", "human", None}
RISK_KEYS = {
    "destructive",
    "irreversible",
    "new_architecture",
    "security_boundary",
    "production_change",
    "breaking_external_contract",
    "data_migration",
}


class TaskContractError(ValueError):
    pass


def load_json(path: Path) -> dict:
    if not path.exists():
        raise TaskContractError(f"Missing contract: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise TaskContractError(f"Invalid JSON in {path}: {exc}") from exc


def validate_task_contract(task: dict) -> dict:
    if not isinstance(task, dict):
        raise TaskContractError("task contract must be an object")

    task_id = task.get("task_id")
    if not isinstance(task_id, str) or not task_id.strip():
        raise TaskContractError("task_id must be a non-empty string")

    classification = task.get("classification")
    if classification not in VALID_CLASSIFICATIONS:
        raise TaskContractError("invalid task.classification")

    capabilities = task.get("capabilities", [])
    if not isinstance(capabilities, list) or any(
        not isinstance(item, str) or not item.strip() for item in capabilities
    ):
        raise TaskContractError("capabilities must be a list of non-empty strings")

    affected_areas = task.get("affected_areas", [])
    if not isinstance(affected_areas, list) or any(
        not isinstance(item, str) or not item.strip()
        for item in affected_areas
    ):
        raise TaskContractError(
            "affected_areas must be a list of non-empty strings"
        )

    risk = task.get("risk", {})
    if not isinstance(risk, dict):
        raise TaskContractError("risk must be an object")
    unknown_risks = sorted(set(risk) - RISK_KEYS)
    if unknown_risks:
        raise TaskContractError(
            "unknown risk flag(s): " + ", ".join(unknown_risks)
        )
    non_bool = sorted(key for key, value in risk.items() if not isinstance(value, bool))
    if non_bool:
        raise TaskContractError(
            "risk flag(s) must be boolean: " + ", ".join(non_bool)
        )

    approval = task.get("approval", {})
    if not isinstance(approval, dict):
        raise TaskContractError("approval must be an object")
    provenance = approval.get("provenance")
    if provenance not in VALID_PROVENANCE:
        raise TaskContractError(f"invalid approval provenance: {provenance}")

    if approval.get("status") not in {None, "approved", "pending", "rejected"}:
        raise TaskContractError("invalid approval.status")

    verification = task.get("verification", [])
    if not isinstance(verification, list) or any(
        not isinstance(item, str) or not item.strip() for item in verification
    ):
        raise TaskContractError("verification must be a list of named checks")

    return task
