"""AOS v8 Evidence Bundle recorder.

Runs only named verification commands declared in the Project Profile.
PASS/FAIL is derived from the actual process exit code.

Usage:
  python .agent/01-core/evidence_recorder.py --check governance_compile
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(".")
PROJECT_PROFILE = ROOT / ".agent/profiles/project.json"
TASK_CONTRACT = ROOT / ".agent/task-contracts/current.json"
DEFAULT_OUTPUT = ROOT / ".agent/evidence/current.json"


class EvidenceError(ValueError):
    pass


def load_json(path: Path) -> dict:
    if not path.exists():
        raise EvidenceError(f"Missing contract: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise EvidenceError(f"Invalid JSON in {path}: {exc}") from exc


def status_from_exit_code(exit_code: int) -> str:
    return "PASS" if exit_code == 0 else "FAIL"


def build_record(
    *,
    task_id: str | None,
    check_name: str,
    command: str,
    exit_code: int,
    started_at: str,
    duration_ms: int,
    source: str = "local",
) -> dict:
    return {
        "task_id": task_id,
        "check": check_name,
        "command": command,
        "exit_code": exit_code,
        "status": status_from_exit_code(exit_code),
        "started_at": started_at,
        "duration_ms": duration_ms,
        "source": source,
    }


def write_bundle(output: Path, record: dict) -> None:
    bundle = {
        "schema_version": 1,
        "task_id": record.get("task_id"),
        "checks": [],
    }

    if output.exists():
        existing = load_json(output)
        if existing.get("task_id") == record.get("task_id"):
            checks = existing.get("checks", [])
            if isinstance(checks, list):
                bundle["checks"] = [
                    item for item in checks
                    if item.get("check") != record.get("check")
                ]

    bundle["checks"].append(record)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def run_named_check(
    check_name: str,
    *,
    project_profile: Path = PROJECT_PROFILE,
    task_contract: Path = TASK_CONTRACT,
    output: Path = DEFAULT_OUTPUT,
) -> dict:
    project = load_json(project_profile)
    task = load_json(task_contract)

    commands = project.get("commands", {})
    if check_name not in commands:
        raise EvidenceError(
            f"Unknown check '{check_name}'. Use a named Project Profile command."
        )

    command = commands[check_name]
    if not isinstance(command, str) or not command.strip():
        raise EvidenceError(f"Project Profile command '{check_name}' is empty.")

    started = datetime.now(timezone.utc).isoformat()
    before = time.monotonic()
    completed = subprocess.run(
        command,
        cwd=ROOT,
        shell=True,
        check=False,
    )
    duration_ms = int((time.monotonic() - before) * 1000)

    record = build_record(
        task_id=task.get("task_id"),
        check_name=check_name,
        command=command,
        exit_code=completed.returncode,
        started_at=started,
        duration_ms=duration_ms,
    )
    write_bundle(output, record)
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description="Run and record project evidence")
    parser.add_argument("--check", required=True)
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    args = parser.parse_args()

    try:
        record = run_named_check(
            args.check,
            output=Path(args.output),
        )
    except EvidenceError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2))
        return 1

    print(json.dumps(record, indent=2, ensure_ascii=False))
    return 0 if record["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
