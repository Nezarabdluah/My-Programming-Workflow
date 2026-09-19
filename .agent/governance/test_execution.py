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
    if result.get("execution_mode") != "HUMAN_APPROVED":
        return FAIL, f"GOV-T17: expected HUMAN_APPROVED: {result}"

    return PASS, (
        "GOV-T17: current task resolves HUMAN_APPROVED "
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
        "capabilities": ["architecture"],
        "risk": {"destructive": True},
        "approval": {
            "status": "approved",
            "provenance": "approved_pattern",
            "reference": "test-pattern-allows-destructive",
        },
        "verification": [],
    }
    registry = {
        "entries": [{
            "id": "test-pattern-allows-destructive",
            "type": "approved_pattern",
            "status": "approved",
            "capabilities": ["architecture"],
            "risk_allowlist": ["destructive"],
        }]
    }

    result = engine.evaluate_approval(task, policy, registry)
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
    if result.get("execution_mode") != "AUTO_EXECUTE":
        return FAIL, f"GOV-T19: expected AUTO_EXECUTE: {result}"

    return PASS, "GOV-T19: low-risk Simple task returns AUTO_EXECUTE."


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


def test_gov_t23_registered_adr_auto_execute():
    """GOV-T23: Verified in-scope ADR provenance enables AUTO_EXECUTE."""
    engine = _load_module(
        "aos_approval_engine_registered",
        ".agent/01-core/approval_engine.py",
    )
    policy = _json(".agent/01-core/approval-policy.json")
    registry = _json(".agent/01-core/approval-registry.json")
    task = {
        "task_id": "t23",
        "classification": "sensitive",
        "capabilities": ["architecture", "testing"],
        "risk": {},
        "approval": {
            "status": "approved",
            "provenance": "approved_adr",
            "reference": "ADR-008",
        },
        "verification": [],
    }

    try:
        result = engine.evaluate_approval(task, policy, registry)
    except Exception as exc:
        return FAIL, f"GOV-T23: registered ADR failed verification: {exc}"

    if result.get("execution_mode") != "AUTO_EXECUTE":
        return FAIL, f"GOV-T23: expected AUTO_EXECUTE: {result}"

    return PASS, "GOV-T23: verified ADR provenance enables AUTO_EXECUTE."


def test_gov_t24_forged_approval_reference_rejected():
    """GOV-T24: Forged approved_adr text must not count as provenance."""
    engine = _load_module(
        "aos_approval_engine_forged",
        ".agent/01-core/approval_engine.py",
    )
    policy = _json(".agent/01-core/approval-policy.json")
    registry = _json(".agent/01-core/approval-registry.json")
    task = {
        "task_id": "t24-forged",
        "classification": "sensitive",
        "capabilities": ["architecture"],
        "risk": {},
        "approval": {
            "status": "approved",
            "provenance": "approved_adr",
            "reference": "ADR-DOES-NOT-EXIST",
        },
        "verification": [],
    }

    try:
        engine.evaluate_approval(task, policy, registry)
    except engine.ApprovalError:
        return PASS, "GOV-T24: forged ADR provenance rejected."
    except Exception as exc:
        return FAIL, f"GOV-T24: unexpected exception: {exc}"

    return FAIL, "GOV-T24: forged ADR provenance was accepted."


def test_gov_t25_approval_scope_mismatch_rejected():
    """GOV-T25: Approval reference cannot cover undeclared capabilities."""
    engine = _load_module(
        "aos_approval_engine_scope",
        ".agent/01-core/approval_engine.py",
    )
    policy = _json(".agent/01-core/approval-policy.json")
    registry = _json(".agent/01-core/approval-registry.json")
    task = {
        "task_id": "t25-scope",
        "classification": "sensitive",
        "capabilities": ["security"],
        "risk": {},
        "approval": {
            "status": "approved",
            "provenance": "approved_adr",
            "reference": "ADR-008",
        },
        "verification": [],
    }

    try:
        engine.evaluate_approval(task, policy, registry)
    except engine.ApprovalError:
        return PASS, "GOV-T25: out-of-scope approval provenance rejected."
    except Exception as exc:
        return FAIL, f"GOV-T25: unexpected exception: {exc}"

    return FAIL, "GOV-T25: out-of-scope approval provenance was accepted."


def test_gov_t26_evidence_history_detects_tampering():
    """GOV-T26: Archived Evidence Bundle hash must detect content tampering."""
    evidence = _load_module(
        "aos_evidence_history",
        ".agent/01-core/evidence_recorder.py",
    )

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        current = root / "current.json"
        history = root / "history"
        record = evidence.build_record(
            task_id="t26",
            check_name="verify",
            command="verify",
            exit_code=0,
            started_at="2026-01-01T00:00:00+00:00",
            duration_ms=1,
            source="test",
        )
        evidence.write_bundle(current, record)
        archived = evidence.archive_bundle(current, history)

        try:
            evidence.verify_archive(archived)
        except Exception as exc:
            return FAIL, f"GOV-T26: valid archive failed verification: {exc}"

        envelope = json.loads(archived.read_text(encoding="utf-8"))
        envelope["bundle"]["checks"][0]["status"] = "FAIL"
        archived.write_text(json.dumps(envelope, indent=2) + "\n", encoding="utf-8")

        try:
            evidence.verify_archive(archived)
        except evidence.EvidenceError:
            return PASS, "GOV-T26: tampered Evidence History detected."
        except Exception as exc:
            return FAIL, f"GOV-T26: unexpected exception: {exc}"

    return FAIL, "GOV-T26: tampered Evidence History was accepted."


def test_gov_t27_task_contract_rejects_unknown_risk():
    """GOV-T27: Unknown risk flags fail contract validation."""
    contract = _load_module(
        "aos_task_contract_test",
        ".agent/01-core/task_contract.py",
    )
    task = {
        "task_id": "t27",
        "classification": "medium",
        "capabilities": ["testing"],
        "risk": {"invented_risk": True},
        "approval": {"status": "approved", "provenance": "policy"},
        "verification": [],
    }

    try:
        contract.validate_task_contract(task)
    except contract.TaskContractError:
        return PASS, "GOV-T27: unknown risk flag rejected."
    except Exception as exc:
        return FAIL, f"GOV-T27: unexpected exception: {exc}"

    return FAIL, "GOV-T27: unknown risk flag was accepted."


def test_gov_t28_current_execution_gate_ready():
    """GOV-T28: Current T025 resolves to READY/HUMAN_APPROVED."""
    gate = _load_module(
        "aos_execution_gate_current",
        ".agent/01-core/execution_gate.py",
    )
    try:
        result = gate.evaluate_current()
    except Exception as exc:
        return FAIL, f"GOV-T28: current execution gate failed: {exc}"

    if result.get("status") != "READY":
        return FAIL, f"GOV-T28: current task is not READY: {result}"
    if result.get("execution_mode") != "HUMAN_APPROVED":
        return FAIL, f"GOV-T28: expected HUMAN_APPROVED: {result}"
    if not result.get("verification"):
        return FAIL, "GOV-T28: no named verification checks returned."

    return PASS, "GOV-T28: T025 is READY with HUMAN_APPROVED execution mode."


def test_gov_t29_registered_adr_execution_gate_auto_executes():
    """GOV-T29: Execution Gate returns AUTO_EXECUTE for verified ADR scope."""
    gate = _load_module(
        "aos_execution_gate_auto",
        ".agent/01-core/execution_gate.py",
    )
    project = _json(".agent/profiles/project.json")
    policy = _json(".agent/01-core/approval-policy.json")
    registry = _json(".agent/01-core/approval-registry.json")
    context_map = _json(".agent/01-core/context-map.json")
    task = {
        "task_id": "t29",
        "classification": "sensitive",
        "capabilities": ["architecture", "testing"],
        "risk": {},
        "approval": {
            "status": "approved",
            "provenance": "approved_adr",
            "reference": "ADR-008",
        },
        "verification": ["governance_compile"],
    }

    try:
        result = gate.evaluate_execution(
            task, project, policy, registry, context_map
        )
    except Exception as exc:
        return FAIL, f"GOV-T29: execution gate failed: {exc}"

    if result.get("status") != "READY":
        return FAIL, f"GOV-T29: task not READY: {result}"
    if result.get("execution_mode") != "AUTO_EXECUTE":
        return FAIL, f"GOV-T29: expected AUTO_EXECUTE: {result}"

    return PASS, "GOV-T29: verified ADR task is READY/AUTO_EXECUTE."


def test_gov_t30_approval_registry_sources_resolve():
    """GOV-T30: Every approval registry entry resolves to durable source evidence."""
    engine = _load_module(
        "aos_approval_engine_registry_sources",
        ".agent/01-core/approval_engine.py",
    )
    registry = _json(".agent/01-core/approval-registry.json")
    entries = registry.get("entries", [])
    if not entries:
        return FAIL, "GOV-T30: approval registry has no entries."

    seen = set()
    for entry in entries:
        entry_id = entry.get("id")
        if not isinstance(entry_id, str) or not entry_id.strip():
            return FAIL, "GOV-T30: registry entry missing id."
        if entry_id in seen:
            return FAIL, f"GOV-T30: duplicate registry id: {entry_id}"
        seen.add(entry_id)

        try:
            engine._verify_registry_source(entry)
        except Exception as exc:
            return FAIL, f"GOV-T30: {entry_id} source invalid: {exc}"

    return PASS, (
        f"GOV-T30: {len(entries)} approval registry entries resolve "
        "to durable source evidence."
    )
