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


def _is_aos_source_repo():
    path = Path(".agent/profiles/project.json")
    if not path.exists():
        return False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return (
        data.get("project_id") == "my-programming-workflow"
        and data.get("project_type") == "engineering-workflow-framework"
    )


def _json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def test_gov_t17_current_approval_resolves():
    """GOV-T17: Current task approval mode must match verified provenance."""
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

    provenance = result.get("provenance")
    expected_mode = (
        "HUMAN_APPROVED" if provenance == "human" else "AUTO_EXECUTE"
    )
    if result.get("execution_mode") != expected_mode:
        return FAIL, (
            f"GOV-T17: provenance {provenance!r} expected "
            f"{expected_mode}, got {result.get('execution_mode')!r}: {result}"
        )

    return PASS, (
        "GOV-T17: current task approval mode matches verified provenance "
        f"({provenance} → {expected_mode})."
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
        "affected_areas": ["src"],
        "risk": {"destructive": True},
        "approval": {
            "status": "approved",
            "provenance": "approved_pattern",
            "reference": "hard-stop-test-pattern",
        },
        "verification": [],
    }
    registry = {
        "entries": [{
            "id": "hard-stop-test-pattern",
            "type": "approved_pattern",
            "status": "approved",
            "scope": "runtime",
            "capabilities": ["architecture"],
            "risk_allowlist": ["destructive"],
            "source": ".agent/adr/system-decisions.md",
            "source_marker": "ADR-008",
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
    """GOV-T28: Current task resolves READY with provenance-consistent mode."""
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

    provenance = result.get("approval", {}).get("provenance")
    expected_mode = (
        "HUMAN_APPROVED" if provenance == "human" else "AUTO_EXECUTE"
    )
    if result.get("execution_mode") != expected_mode:
        return FAIL, (
            f"GOV-T28: provenance {provenance!r} expected "
            f"{expected_mode}, got {result.get('execution_mode')!r}: {result}"
        )
    if not result.get("verification"):
        return FAIL, "GOV-T28: no named verification checks returned."

    return PASS, (
        f"GOV-T28: {result.get('task_id')} is READY/{expected_mode} "
        f"via {provenance}."
    )


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

    commands = project.get("commands", {})
    preferred = [
        "aos_compile",
        "governance_compile",
        "aos_verify",
        "governance_verify",
    ]
    verification_check = next(
        (name for name in preferred if name in commands),
        next(iter(commands), None),
    )
    if not verification_check:
        return FAIL, "GOV-T29: project has no named verification command."

    task = {
        "task_id": "t29",
        "classification": "sensitive",
        "capabilities": ["architecture", "testing"],
        "affected_areas": [".agent"],
        "risk": {},
        "approval": {
            "status": "approved",
            "provenance": "approved_adr",
            "reference": "ADR-008",
        },
        "verification": [verification_check],
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

    return PASS, (
        "GOV-T29: verified ADR task is READY/AUTO_EXECUTE "
        f"using check {verification_check}."
    )


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
    source_repo = engine._is_aos_source_repo()
    checked = 0
    for entry in entries:
        if entry.get("scope", "runtime") == "aos-source" and not source_repo:
            continue

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
        checked += 1

    return PASS, (
        f"GOV-T30: {checked} applicable approval registry entries resolve "
        "to durable source evidence."
    )


def test_gov_t39_sanitized_installer_excludes_source_state():
    """GOV-T39: Consumer installer must not copy source-specific project state."""
    if not _is_aos_source_repo():
        return "SKIP_EXPECTED", "GOV-T39: AOS-source-only installer self-test."

    installer = _load_module(
        "aos_sanitized_installer",
        ".agent/install.py",
    )

    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "consumer-project"
        target.mkdir(parents=True, exist_ok=True)

        try:
            result = installer.install(target)
        except Exception as exc:
            return FAIL, f"GOV-T39: installer failed: {exc}"

        required = [
            target / ".agent/01-core/boot-manifest.md",
            target / ".agent/governance/verify.py",
            target / ".agent/profiles/technology",
            target / ".agent/evidence/README.md",
            target / "AGENTS.md",
        ]
        missing = [str(path.relative_to(target)) for path in required if not path.exists()]
        if missing:
            return FAIL, (
                "GOV-T39: reusable runtime missing after install: "
                + ", ".join(missing)
            )

        forbidden = [
            target / ".agent/04-memory",
            target / ".agent/profiles/project.json",
            target / ".agent/task-contracts/current.json",
            target / ".agent/evidence/current.json",
            target / ".agent/evidence/history",
        ]
        leaked = [str(path.relative_to(target)) for path in forbidden if path.exists()]
        if leaked:
            return FAIL, (
                "GOV-T39: source-specific state leaked into consumer install: "
                + ", ".join(leaked)
            )

        if result.get("runtime_installed") is not True:
            return FAIL, "GOV-T39: installer did not report runtime_installed=true."

    return PASS, "GOV-T39: sanitized installer copies runtime and excludes source state."


def test_gov_t42_foreign_agent_conflict_is_write_free():
    """GOV-T42: Foreign agent infrastructure blocks before any AOS write."""
    if not _is_aos_source_repo():
        return "SKIP_EXPECTED", "GOV-T42: AOS-source-only installer safety test."

    installer = _load_module("aos_installer_conflict", ".agent/install.py")

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "foreign-project"
        (root / ".agent").mkdir(parents=True)
        sentinel = root / ".agent" / "foreign-system.txt"
        sentinel.write_text("foreign-agent-state", encoding="utf-8")

        try:
            installer.install(root)
        except installer.InstallError:
            pass
        except Exception as exc:
            return FAIL, f"GOV-T42: unexpected conflict exception: {exc}"
        else:
            return FAIL, "GOV-T42: foreign .agent was not blocked."

        if sentinel.read_text(encoding="utf-8") != "foreign-agent-state":
            return FAIL, "GOV-T42: foreign agent state was modified."
        if (root / ".agent" / "VERSION").exists():
            return FAIL, "GOV-T42: AOS wrote files despite preflight conflict."

    return PASS, "GOV-T42: foreign agent conflict blocks with zero AOS writes."


def test_gov_t43_safe_upgrade_preserves_project_state():
    """GOV-T43: Recognized AOS upgrades preserve project state and back up adapters."""
    if not _is_aos_source_repo():
        return "SKIP_EXPECTED", "GOV-T43: AOS-source-only upgrade safety test."

    installer = _load_module("aos_installer_upgrade", ".agent/install.py")

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "existing-aos"
        root.mkdir(parents=True)

        first = installer.install(root)
        if first.get("mode") != "fresh":
            return FAIL, f"GOV-T43: first install was not fresh: {first}"

        state = {
            root / ".agent/04-memory/project-context.md": "KEEP-MEMORY",
            root / ".agent/profiles/project.json": '{"keep":"profile"}\n',
            root / ".agent/task-contracts/current.json": '{"keep":"task"}\n',
            root / ".agent/evidence/history/keep.json": '{"keep":"evidence"}\n',
        }
        for path, value in state.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(value, encoding="utf-8")

        adapter = root / "AGENTS.md"
        adapter.write_text(
            adapter.read_text(encoding="utf-8") + "\nCUSTOM-AOS-ADAPTER-LINE\n",
            encoding="utf-8",
        )

        second = installer.install(root)
        if second.get("mode") != "upgrade":
            return FAIL, f"GOV-T43: existing AOS was not classified upgrade: {second}"

        for path, value in state.items():
            if not path.exists() or path.read_text(encoding="utf-8") != value:
                return FAIL, f"GOV-T43: preserved state changed: {path}"

        backup = root / ".agent/backups/last-upgrade/AGENTS.md"
        if not backup.exists():
            return FAIL, "GOV-T43: managed adapter backup missing."
        if "CUSTOM-AOS-ADAPTER-LINE" not in backup.read_text(encoding="utf-8"):
            return FAIL, "GOV-T43: adapter backup did not preserve prior content."

    return PASS, "GOV-T43: safe upgrade preserves state and backs up managed adapters."


def test_gov_t44_bootstrap_initializes_detected_consumer():
    """GOV-T44: One-command bootstrap initializes a detected consumer project."""
    if not _is_aos_source_repo():
        return "SKIP_EXPECTED", "GOV-T44: AOS-source-only bootstrap self-test."

    bootstrap = _load_module("aos_bootstrap_consumer", ".agent/bootstrap.py")

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "web-app"
        root.mkdir(parents=True)
        (root / "package.json").write_text(
            json.dumps({
                "scripts": {
                    "build": "vite build",
                    "test": "vitest run",
                    "lint": "eslint .",
                }
            }),
            encoding="utf-8",
        )
        (root / "tsconfig.json").write_text("{}", encoding="utf-8")

        result = bootstrap.bootstrap(root, verify=False)

        if result.get("status") != "READY":
            return FAIL, f"GOV-T44: detected project was not READY: {result}"
        if result.get("project_type") != "node":
            return FAIL, f"GOV-T44: expected node project: {result}"
        if set(result.get("languages", [])) != {"javascript", "typescript"}:
            return FAIL, f"GOV-T44: language detection mismatch: {result}"

        profile = json.loads(
            (root / ".agent/profiles/project.json").read_text(encoding="utf-8")
        )
        for command in ["aos_compile", "aos_verify", "project_build", "project_test", "project_lint"]:
            if command not in profile.get("commands", {}):
                return FAIL, f"GOV-T44: missing detected command: {command}"

        task = json.loads(
            (root / ".agent/task-contracts/current.json").read_text(encoding="utf-8")
        )
        if task.get("capabilities") != ["testing"]:
            return FAIL, "GOV-T44: bootstrap task lacks portable testing context."

        for name in [
            "project-context.md",
            "active-tasks.md",
            "learned-mistakes.md",
            "decisions.md",
        ]:
            if not (root / ".agent/04-memory" / name).exists():
                return FAIL, f"GOV-T44: missing initialized memory file: {name}"

    return PASS, "GOV-T44: one-command bootstrap creates detected consumer state."


def test_gov_t45_source_only_approval_rejected_in_consumer():
    """GOV-T45: AOS-source approval patterns cannot authorize consumer work."""
    engine = _load_module(
        "aos_approval_scope_consumer",
        ".agent/01-core/approval_engine.py",
    )
    policy = _json(".agent/01-core/approval-policy.json")
    registry = {
        "entries": [{
            "id": "source-only-test-pattern",
            "type": "approved_pattern",
            "status": "approved",
            "scope": "aos-source",
            "capabilities": ["architecture", "testing"],
            "risk_allowlist": [],
            "source": ".agent/adr/system-decisions.md",
            "source_marker": "ADR-008",
        }]
    }
    task = {
        "task_id": "t45",
        "classification": "medium",
        "capabilities": ["architecture", "testing"],
        "affected_areas": ["src"],
        "risk": {},
        "approval": {
            "status": "approved",
            "provenance": "approved_pattern",
            "reference": "source-only-test-pattern",
        },
        "verification": ["aos_verify"],
    }

    original = engine._is_aos_source_repo
    engine._is_aos_source_repo = lambda: False
    try:
        engine.evaluate_approval(task, policy, registry)
    except engine.ApprovalError:
        return PASS, "GOV-T45: source-only approval pattern rejected in consumer mode."
    except Exception as exc:
        return FAIL, f"GOV-T45: unexpected exception: {exc}"
    finally:
        engine._is_aos_source_repo = original

    return FAIL, "GOV-T45: source-only approval pattern authorized consumer work."
