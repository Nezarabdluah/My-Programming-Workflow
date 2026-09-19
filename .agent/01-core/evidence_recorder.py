"""AOS v8 Evidence Bundle recorder and history archiver.

Named checks come only from the Project Profile. PASS/FAIL is derived from
actual exit codes. Archived bundles carry a SHA-256 integrity hash.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shlex
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(".")
PROJECT_PROFILE = ROOT / ".agent/profiles/project.json"
TASK_CONTRACT = ROOT / ".agent/task-contracts/current.json"
DEFAULT_OUTPUT = ROOT / ".agent/evidence/current.json"
DEFAULT_HISTORY = ROOT / ".agent/evidence/history"


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


def default_source() -> str:
    return "github-actions" if os.getenv("GITHUB_ACTIONS") == "true" else "local"


def build_record(
    *,
    task_id: str | None,
    check_name: str,
    command: str,
    exit_code: int,
    started_at: str,
    duration_ms: int,
    source: str | None = None,
) -> dict:
    return {
        "task_id": task_id,
        "check": check_name,
        "command": command,
        "exit_code": exit_code,
        "status": status_from_exit_code(exit_code),
        "started_at": started_at,
        "duration_ms": duration_ms,
        "source": source or default_source(),
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


def canonical_bundle_bytes(bundle: dict) -> bytes:
    return json.dumps(
        bundle,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def bundle_sha256(bundle: dict) -> str:
    return hashlib.sha256(canonical_bundle_bytes(bundle)).hexdigest()


def archive_bundle(
    current: Path = DEFAULT_OUTPUT,
    history_dir: Path = DEFAULT_HISTORY,
) -> Path:
    bundle = load_json(current)
    task_id = bundle.get("task_id")
    checks = bundle.get("checks", [])
    if not isinstance(task_id, str) or not task_id.strip():
        raise EvidenceError("Current Evidence Bundle has no task_id.")
    if not isinstance(checks, list) or not checks:
        raise EvidenceError("Current Evidence Bundle has no checks.")

    digest = bundle_sha256(bundle)
    envelope = {
        "schema_version": 1,
        "task_id": task_id,
        "archived_at": datetime.now(timezone.utc).isoformat(),
        "bundle_sha256": digest,
        "bundle": bundle,
    }

    safe_task = "".join(
        char if char.isalnum() or char in {"-", "_"} else "_"
        for char in task_id
    )
    history_dir.mkdir(parents=True, exist_ok=True)
    target = history_dir / f"{safe_task}-{digest[:16]}.json"

    if target.exists():
        existing = load_json(target)
        if existing.get("bundle_sha256") != digest:
            raise EvidenceError(f"Archive collision with different hash: {target}")
        return target

    target.write_text(
        json.dumps(envelope, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return target


def verify_archive(path: Path) -> bool:
    envelope = load_json(path)
    bundle = envelope.get("bundle")
    expected = envelope.get("bundle_sha256")
    if not isinstance(bundle, dict) or not isinstance(expected, str):
        raise EvidenceError("Invalid Evidence History envelope.")
    actual = bundle_sha256(bundle)
    if actual != expected:
        raise EvidenceError(
            f"Evidence History integrity mismatch: expected {expected}, got {actual}"
        )
    return True


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
    argv = shlex.split(command)
    if not argv:
        raise EvidenceError(f"Project Profile command '{check_name}' is empty.")

    completed = subprocess.run(
        argv,
        cwd=ROOT,
        shell=False,
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
    parser = argparse.ArgumentParser(description="Run/archive AOS evidence")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check")
    group.add_argument("--archive-current", action="store_true")
    group.add_argument("--verify-archive")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--history-dir", default=str(DEFAULT_HISTORY))
    args = parser.parse_args()

    try:
        if args.check:
            record = run_named_check(
                args.check,
                output=Path(args.output),
            )
            print(json.dumps(record, indent=2, ensure_ascii=False))
            return 0 if record["status"] == "PASS" else 1

        if args.archive_current:
            archived = archive_bundle(
                Path(args.output),
                Path(args.history_dir),
            )
            print(json.dumps(
                {"status": "PASS", "archive": str(archived)},
                indent=2,
            ))
            return 0

        verify_archive(Path(args.verify_archive))
        print(json.dumps(
            {"status": "PASS", "archive": args.verify_archive},
            indent=2,
        ))
        return 0

    except EvidenceError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
