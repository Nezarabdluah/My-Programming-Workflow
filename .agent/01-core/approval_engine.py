"""AOS v8 Approval Engine.

Evaluates structured Task Contracts against approval policy and verified
approval provenance. No free-text inference and no external dependencies.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
from pathlib import Path


CORE_DIR = Path(".agent/01-core")
DEFAULT_TASK = Path(".agent/task-contracts/current.json")
DEFAULT_POLICY = CORE_DIR / "approval-policy.json"
DEFAULT_REGISTRY = CORE_DIR / "approval-registry.json"


class ApprovalError(ValueError):
    pass


def load_json(path: Path) -> dict:
    if not path.exists():
        raise ApprovalError(f"Missing contract: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ApprovalError(f"Invalid JSON in {path}: {exc}") from exc


def _validate_task(task: dict) -> dict:
    path = CORE_DIR / "task_contract.py"
    spec = importlib.util.spec_from_file_location("aos_task_contract", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    try:
        return module.validate_task_contract(task)
    except Exception as exc:
        raise ApprovalError(str(exc)) from exc


def _verify_registry_source(entry: dict) -> None:
    source = entry.get("source")
    marker = entry.get("source_marker")
    if not isinstance(source, str) or not source.strip():
        raise ApprovalError("approval registry entry is missing source")
    if not isinstance(marker, str) or not marker.strip():
        raise ApprovalError("approval registry entry is missing source_marker")

    path = Path(source)
    if not path.exists():
        raise ApprovalError(f"approval source does not exist: {source}")

    content = path.read_text(encoding="utf-8")
    if marker not in content:
        raise ApprovalError(
            f"approval source marker not found: {marker} in {source}"
        )

    if entry.get("type") == "approved_adr":
        start = content.find(marker)
        next_heading = content.find("\n## ", start + len(marker))
        section = content[start: next_heading if next_heading != -1 else len(content)]
        if not re.search(
            r"\*\*Status\*\*\s*:\s*Approved\b",
            section,
            flags=re.IGNORECASE,
        ):
            raise ApprovalError(
                f"ADR approval source is not approved: {marker}"
            )


def _is_aos_source_repo() -> bool:
    path = Path(".agent/profiles/project.json")
    if not path.exists():
        return False
    try:
        profile = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return (
        profile.get("project_id") == "my-programming-workflow"
        and profile.get("project_type") == "engineering-workflow-framework"
    )


def _registry_entry(task: dict, registry: dict) -> dict | None:
    approval = task.get("approval", {})
    provenance = approval.get("provenance")
    if provenance not in {"approved_adr", "approved_pattern"}:
        return None

    reference = approval.get("reference")
    if not isinstance(reference, str) or not reference.strip():
        raise ApprovalError(
            f"{provenance} requires a non-empty approval.reference"
        )

    entries = registry.get("entries", [])
    if not isinstance(entries, list):
        raise ApprovalError("approval registry entries must be a list")

    source_repo = _is_aos_source_repo()
    matches = [
        entry for entry in entries
        if entry.get("id") == reference
        and entry.get("type") == provenance
        and entry.get("status") == "approved"
        and (
            entry.get("scope", "runtime") != "aos-source"
            or source_repo
        )
    ]
    if len(matches) != 1:
        raise ApprovalError(
            f"unverified approval provenance: {provenance}:{reference}"
        )

    entry = matches[0]
    _verify_registry_source(entry)

    task_caps = set(task.get("capabilities", []))
    allowed_caps = set(entry.get("capabilities", []))
    if not task_caps.issubset(allowed_caps):
        missing = sorted(task_caps - allowed_caps)
        raise ApprovalError(
            "approval reference does not cover capability/capabilities: "
            + ", ".join(missing)
        )

    active_risks = {
        key for key, value in task.get("risk", {}).items()
        if value is True
    }
    allowed_risks = set(entry.get("risk_allowlist", []))
    uncovered = sorted(active_risks - allowed_risks)
    if uncovered:
        raise ApprovalError(
            "approval reference does not cover risk(s): "
            + ", ".join(uncovered)
        )

    return entry


def _approved(*, provenance: str, reason: str, human_required: bool,
              execution_mode: str, **extra) -> dict:
    return {
        "decision": "APPROVED",
        "execution_mode": execution_mode,
        "provenance": provenance,
        "reason": reason,
        "human_required": human_required,
        **extra,
    }


def _blocked(*, provenance, reason: str, **extra) -> dict:
    return {
        "decision": "BLOCKED",
        "execution_mode": "HUMAN_REQUIRED",
        "provenance": provenance,
        "reason": reason,
        "human_required": True,
        **extra,
    }


def evaluate_approval(
    task: dict,
    policy: dict,
    registry: dict | None = None,
) -> dict:
    task = _validate_task(task)
    registry = registry if registry is not None else load_json(DEFAULT_REGISTRY)

    classification = task["classification"]
    risk = task.get("risk", {})
    approval = task.get("approval", {})
    provenance = approval.get("provenance")
    hard_stop_keys = policy.get("hard_stop_risks", [])
    active_hard_stops = [
        key for key in hard_stop_keys if risk.get(key) is True
    ]

    if classification == "simple" and not active_hard_stops:
        return _approved(
            provenance="policy",
            reason="simple task with no hard-stop risk",
            human_required=False,
            execution_mode="AUTO_EXECUTE",
        )

    if active_hard_stops:
        if provenance == "human" and approval.get("status") == "approved":
            return _approved(
                provenance="human",
                reason="hard-stop risk explicitly approved by Navigator",
                human_required=True,
                execution_mode="HUMAN_APPROVED",
                hard_stop_risks=active_hard_stops,
            )
        return _blocked(
            provenance=provenance,
            reason="hard-stop risk requires explicit human approval",
            hard_stop_risks=active_hard_stops,
        )

    verified = _registry_entry(task, registry)

    if classification == "medium":
        accepted = set(policy.get("accepted_medium_provenance", []))
        if provenance in accepted and approval.get("status") == "approved":
            if provenance in {"approved_adr", "approved_pattern"} and not verified:
                raise ApprovalError("approval provenance was not verified")
            mode = "HUMAN_APPROVED" if provenance == "human" else "AUTO_EXECUTE"
            return _approved(
                provenance=provenance,
                reason="medium task covered by accepted approval provenance",
                human_required=provenance == "human",
                execution_mode=mode,
                approval_reference=approval.get("reference"),
            )
        return _blocked(
            provenance=provenance,
            reason="medium task lacks accepted approval provenance",
        )

    accepted = set(policy.get("accepted_sensitive_provenance", []))
    if provenance in accepted and approval.get("status") == "approved":
        if provenance in {"approved_adr", "approved_pattern"} and not verified:
            raise ApprovalError("approval provenance was not verified")
        mode = "HUMAN_APPROVED" if provenance == "human" else "AUTO_EXECUTE"
        return _approved(
            provenance=provenance,
            reason="sensitive task covered by verified approval provenance",
            human_required=provenance == "human",
            execution_mode=mode,
            approval_reference=approval.get("reference"),
        )

    return _blocked(
        provenance=provenance,
        reason="sensitive task requires human/ADR/pattern approval",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate AOS task approval")
    parser.add_argument("--task", default=str(DEFAULT_TASK))
    parser.add_argument("--policy", default=str(DEFAULT_POLICY))
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    args = parser.parse_args()

    try:
        result = evaluate_approval(
            load_json(Path(args.task)),
            load_json(Path(args.policy)),
            load_json(Path(args.registry)),
        )
    except ApprovalError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2))
        return 1

    status = "PASS" if result["decision"] == "APPROVED" else "BLOCKED"
    print(json.dumps({"status": status, "approval": result}, indent=2))
    return 0 if result["decision"] == "APPROVED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
