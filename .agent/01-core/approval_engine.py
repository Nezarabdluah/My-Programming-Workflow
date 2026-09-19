"""AOS v8 Approval Engine.

Evaluates approval requirements from a structured Task Contract.
No free-text inference and no external dependencies.

Usage:
  python .agent/01-core/approval_engine.py
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_TASK = Path(".agent/task-contracts/current.json")
DEFAULT_POLICY = Path(".agent/01-core/approval-policy.json")


class ApprovalError(ValueError):
    pass


def load_json(path: Path) -> dict:
    if not path.exists():
        raise ApprovalError(f"Missing contract: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ApprovalError(f"Invalid JSON in {path}: {exc}") from exc


def evaluate_approval(task: dict, policy: dict) -> dict:
    classification = task.get("classification")
    if classification not in {"simple", "medium", "sensitive"}:
        raise ApprovalError("invalid task.classification")

    risk = task.get("risk", {})
    if not isinstance(risk, dict):
        raise ApprovalError("task.risk must be an object")

    approval = task.get("approval", {})
    if not isinstance(approval, dict):
        raise ApprovalError("task.approval must be an object")

    provenance = approval.get("provenance")
    hard_stop_keys = policy.get("hard_stop_risks", [])
    active_hard_stops = [
        key for key in hard_stop_keys if risk.get(key) is True
    ]

    if classification == "simple" and not active_hard_stops:
        return {
            "decision": "APPROVED",
            "provenance": "policy",
            "reason": "simple task with no hard-stop risk",
            "human_required": False,
        }

    if active_hard_stops:
        if provenance == "human" and approval.get("status") == "approved":
            return {
                "decision": "APPROVED",
                "provenance": "human",
                "reason": "hard-stop risk explicitly approved by Navigator",
                "human_required": True,
                "hard_stop_risks": active_hard_stops,
            }
        return {
            "decision": "BLOCKED",
            "provenance": provenance,
            "reason": "hard-stop risk requires explicit human approval",
            "human_required": True,
            "hard_stop_risks": active_hard_stops,
        }

    if classification == "medium":
        accepted = set(policy.get("accepted_medium_provenance", []))
        if provenance in accepted and approval.get("status") == "approved":
            return {
                "decision": "APPROVED",
                "provenance": provenance,
                "reason": "medium task covered by accepted approval provenance",
                "human_required": False,
            }
        return {
            "decision": "BLOCKED",
            "provenance": provenance,
            "reason": "medium task lacks accepted approval provenance",
            "human_required": False,
        }

    accepted = set(policy.get("accepted_sensitive_provenance", []))
    if provenance in accepted and approval.get("status") == "approved":
        return {
            "decision": "APPROVED",
            "provenance": provenance,
            "reason": "sensitive task covered by accepted approval provenance",
            "human_required": provenance == "human",
        }

    return {
        "decision": "BLOCKED",
        "provenance": provenance,
        "reason": "sensitive task requires human/ADR/pattern approval",
        "human_required": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate AOS task approval")
    parser.add_argument("--task", default=str(DEFAULT_TASK))
    parser.add_argument("--policy", default=str(DEFAULT_POLICY))
    args = parser.parse_args()

    try:
        result = evaluate_approval(
            load_json(Path(args.task)),
            load_json(Path(args.policy)),
        )
    except ApprovalError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2))
        return 1

    status = "PASS" if result["decision"] == "APPROVED" else "BLOCKED"
    print(json.dumps({"status": status, "approval": result}, indent=2))
    return 0 if result["decision"] == "APPROVED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
