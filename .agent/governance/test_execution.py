"""AOS Governance — Approval & Evidence Tests (v8 Sprint 2)."""

import importlib.util
import json
import tempfile
from pathlib import Path

PASS = "PASS"
FAIL = "FAIL"


def _load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def test_gov_t17_current_approval_resolves():
    """GOV-T17: Current sensitive task must resolve to APPROVED provenance."""
    engine = _load_module(
        "aos_approval_engine",
        ".agent/01-core/approval_engine.py",
    )
    task = _json(".agent/task-contracts/current.json")
    policy = _json(".agent/01-core/approval-policy.json")

    try:
        result = engine.evaluate_approval(task, policy)
    except Exception as exc:
        return FAIL, f"GOV-T17: approval evaluation crashed: {exc}"

    if result.get("decision") != "APPROVED":
        return FAIL, f"GOV-T17: current task not approved: {result}"

    return PASS, (
        "GOV-T17: current task approval resolves "
        f"via {result.get('provenance')}."
    )


def test_gov_t18_hard_stop_requires_human():
    """GOV-T18: Hard-stop risk cannot pass using an approved pattern alone."""
    engine = _load_module(
        "aos_approval_engine_hard_stop",
        ".agent/01-core/approval_engine.py",
    )
    policy = _json(".agent/01-core/approval-policy.json")
    task = {
        "task_id": "t18-hard-stop",
        "classification": "sensitive",
        "risk": {"destructive": True},
        "approval": {
            "status": "approved",
            "provenance": "approved_pattern",
        },
    }

    result = engine.evaluate_approval(task, policy)
    if result.get("decision") != "BLOCKED":
        return FAIL, (
            "GOV-T18: destructive hard-stop bypassed human approval: "
            f"{result}"
        )
    if result.get("human_required") is not True:
        return FAIL, "GOV-T18: hard-stop did not mark human_required=true."

    return PASS, "GOV-T18: destructive hard-stop requires explicit human approval."


def test_gov_t19_simple_policy_approval():
    """GOV-T19: Low-risk Simple work is approved by policy without interruption."""
    engine = _load_module(
        "aos_approval_engine_simple",
        ".agent/01-core/approval_engine.py",
    )
    policy = _json(".agent/01-core/approval-policy.json")
    task = {
        "task_id": "t19-simple",
        "classification": "simple",
        "risk": {},
        "approval": {},
    }

    result = engine.evaluate_approval(task, policy)
    if result.get("decision") != "APPROVED":
        return FAIL, f"GOV-T19: low-risk Simple task blocked: {result}"
    if result.get("provenance") != "policy":
        return FAIL, f"GOV-T19: expected policy provenance: {result}"

    return PASS, "GOV-T19: low-risk Simple task auto-approved by policy."


def test_gov_t20_evidence_status_is_derived():
    """GOV-T20: Evidence status must be derived strictly from exit code."""
    evidence = _load_module(
        "aos_evidence_recorder",
        ".agent/01-core/evidence_recorder.py",
    )

    passed = evidence.build_record(
        task_id="t20",
        check_name="ok",
        command="example",
        exit_code=0,
        started_at="2026-01-01T00:00:00+00:00",
        duration_ms=1,
    )
    failed = evidence.build_record(
        task_id="t20",
        check_name="bad",
        command="example",
        exit_code=7,
        started_at="2026-01-01T00:00:00+00:00",
        duration_ms=1,
    )

    if passed.get("status") != "PASS":
        return FAIL, "GOV-T20: exit_code=0 did not derive PASS."
    if failed.get("status") != "FAIL":
        return FAIL, "GOV-T20: non-zero exit code did not derive FAIL."

    return PASS, "GOV-T20: Evidence PASS/FAIL is derived from exit code."


def test_gov_t21_evidence_bundle_replaces_same_check():
    """GOV-T21: Re-running a named check replaces stale evidence for that check."""
    evidence = _load_module(
        "aos_evidence_recorder_bundle",
        ".agent/01-core/evidence_recorder.py",
    )

    with tempfile.TemporaryDirectory() as tmp:
        output = Path(tmp) / "current.json"
        first = evidence.build_record(
            task_id="t21",
            check_name="compile",
            command="compile",
            exit_code=1,
            started_at="2026-01-01T00:00:00+00:00",
            duration_ms=2,
        )
        second = evidence.build_record(
            task_id="t21",
            check_name="compile",
            command="compile",
            exit_code=0,
            started_at="2026-01-01T00:01:00+00:00",
            duration_ms=3,
        )
        evidence.write_bundle(output, first)
        evidence.write_bundle(output, second)
        bundle = json.loads(output.read_text(encoding="utf-8"))

    checks = bundle.get("checks", [])
    if len(checks) != 1:
        return FAIL, f"GOV-T21: expected one current check, got {len(checks)}."
    if checks[0].get("status") != "PASS":
        return FAIL, "GOV-T21: stale failed evidence was not replaced."

    return PASS, "GOV-T21: repeated named check replaces stale evidence."


def test_gov_t22_unknown_evidence_check_rejected():
    """GOV-T22: Evidence recorder cannot execute undeclared arbitrary commands."""
    evidence = _load_module(
        "aos_evidence_recorder_unknown",
        ".agent/01-core/evidence_recorder.py",
    )

    try:
        evidence.run_named_check("definitely-unknown-check")
    except evidence.EvidenceError:
        return PASS, "GOV-T22: undeclared evidence command rejected."
    except Exception as exc:
        return FAIL, f"GOV-T22: unexpected exception: {exc}"

    return FAIL, "GOV-T22: undeclared command was accepted."
