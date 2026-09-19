"""AOS v8 Execution Gate.

Single deterministic pre-execution decision:
Task Contract -> validation -> Approval Engine -> Context Broker -> named checks.

Exit codes:
  0 = execution may proceed (AUTO_EXECUTE or HUMAN_APPROVED)
  2 = HUMAN_REQUIRED
  1 = invalid contract/configuration
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


CORE_DIR = Path(".agent/01-core")
TASK_PATH = Path(".agent/task-contracts/current.json")
PROJECT_PATH = Path(".agent/profiles/project.json")
POLICY_PATH = CORE_DIR / "approval-policy.json"
REGISTRY_PATH = CORE_DIR / "approval-registry.json"
MAP_PATH = CORE_DIR / "context-map.json"


class ExecutionGateError(ValueError):
    pass


def _module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _json(path: Path) -> dict:
    if not path.exists():
        raise ExecutionGateError(f"Missing required file: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ExecutionGateError(f"Invalid JSON in {path}: {exc}") from exc


def evaluate_execution(
    task: dict,
    project: dict,
    policy: dict,
    registry: dict,
    context_map: dict,
) -> dict:
    task_contract = _module("aos_task_contract_gate", CORE_DIR / "task_contract.py")
    approval_engine = _module("aos_approval_gate", CORE_DIR / "approval_engine.py")
    context_broker = _module("aos_context_gate", CORE_DIR / "context_broker.py")

    try:
        task_contract.validate_task_contract(task)
        approval = approval_engine.evaluate_approval(task, policy, registry)
    except Exception as exc:
        raise ExecutionGateError(str(exc)) from exc

    if approval.get("decision") != "APPROVED":
        return {
            "status": "BLOCKED",
            "execution_mode": "HUMAN_REQUIRED",
            "task_id": task.get("task_id"),
            "approval": approval,
            "resources": [],
            "verification": [],
        }

    try:
        context = context_broker.resolve_context(task, project, context_map)
    except Exception as exc:
        raise ExecutionGateError(str(exc)) from exc

    project_commands = project.get("commands", {})
    requested_checks = task.get("verification", [])
    unknown_checks = [
        name for name in requested_checks
        if name not in project_commands
    ]
    if unknown_checks:
        raise ExecutionGateError(
            "Task Contract requests unknown verification check(s): "
            + ", ".join(sorted(unknown_checks))
        )

    return {
        "status": "READY",
        "execution_mode": approval.get("execution_mode"),
        "task_id": task.get("task_id"),
        "approval": approval,
        "resources": context.get("resources", []),
        "skipped_resources": context.get("skipped", []),
        "verification": requested_checks,
    }


def evaluate_current() -> dict:
    return evaluate_execution(
        _json(TASK_PATH),
        _json(PROJECT_PATH),
        _json(POLICY_PATH),
        _json(REGISTRY_PATH),
        _json(MAP_PATH),
    )


def main() -> int:
    try:
        result = evaluate_current()
    except ExecutionGateError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2))
        return 1

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "READY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
