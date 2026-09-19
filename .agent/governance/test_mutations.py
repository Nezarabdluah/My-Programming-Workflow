"""AOS Governance — Mutation Tests (v8.0-dev)

Proves that governance checks actually FAIL when violations are introduced.
A check that never fails is a rubber-stamp — mutation tests prevent that.

Usage:
  python test_mutations.py
"""
import sys
import shutil
import tempfile
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Add governance dir to path
gov_dir = str(Path(__file__).parent)
if gov_dir not in sys.path:
    sys.path.insert(0, gov_dir)


def _backup_and_write(path, content):
    """Backup original file and write mutation content."""
    backup = path.with_suffix(path.suffix + ".mutation_backup")
    if path.exists():
        shutil.copy2(path, backup)
    path.write_text(content, encoding="utf-8")
    return backup


def _restore(path, backup):
    """Restore original file from backup."""
    if backup.exists():
        shutil.copy2(backup, path)
        backup.unlink()
    elif path.exists():
        path.unlink()


def run_mutation(name, setup_fn, check_fn, expect_fail=True):
    """Run a single mutation test."""
    backups = []
    try:
        backups = setup_fn()
        result = check_fn()

        if isinstance(result, tuple):
            status = result[0]
            msg = result[1]
        else:
            status = "ERROR"
            msg = f"Bad return: {result}"

        if expect_fail:
            # We expect the check to FAIL
            if status == "FAIL":
                print(f"  ✅ MUTATION {name}: Check correctly detected the violation.")
                return True
            else:
                print(f"  ❌ MUTATION {name}: Check DID NOT detect violation! Got: [{status}] {msg}")
                return False
        else:
            if status == "PASS":
                print(f"  ✅ MUTATION {name}: Check correctly passed after fix.")
                return True
            else:
                print(f"  ❌ MUTATION {name}: Expected PASS but got: [{status}] {msg}")
                return False
    except Exception as e:
        print(f"  💥 MUTATION {name}: Crashed: {e}")
        return False
    finally:
        for path, backup in backups:
            _restore(path, backup)


def mut_t04_exceed_mistakes_cap():
    """Mutate learned-mistakes.md to have 25 mistakes (exceeds cap of 20)."""
    from test_memory import test_gov_t04_mistakes_cap
    path = Path(".agent/04-memory/learned-mistakes.md")

    def setup():
        rows = "\n".join(
            f"| {i:02d} | 2026-01-01 | [Type B] | Test mistake {i} | Fix {i} | 1/3 |"
            for i in range(1, 26)
        )
        content = f"# Learned Mistakes\n\n| # | Date | Type | Mistake | Fix | Rep |\n|---|------|------|---------|-----|-----|\n{rows}\n"
        backup = _backup_and_write(path, content)
        return [(path, backup)]

    return run_mutation("T04-EXCEED-CAP", setup, test_gov_t04_mistakes_cap)


def mut_t05_missing_memory_file():
    """Mutate by temporarily renaming a required memory file."""
    from test_memory import test_gov_t05_handoff_validity
    path = Path(".agent/04-memory/decisions.md")
    hidden = path.with_suffix(".md.mutation_hidden")

    def setup():
        if path.exists():
            shutil.move(str(path), str(hidden))
        return [(path, hidden)]

    return run_mutation("T05-MISSING-FILE", setup, test_gov_t05_handoff_validity)


def mut_t09_done_without_state_history():
    """Mutate: completed sensitive task without ordered state history."""
    from test_state import test_gov_t09_workflow_integrity
    path = Path(".agent/04-memory/active-tasks.md")

    def setup():
        content = """# Active Tasks

## T999 — Mutation Test 🔴
- **State:** **Done**
- Acceptance criteria: mutation-only test
- [x] Implementation complete
"""
        backup = _backup_and_write(path, content)
        return [(path, backup)]

    return run_mutation(
        "T09-DONE-WITHOUT-HISTORY",
        setup,
        test_gov_t09_workflow_integrity,
    )


def mut_t10_missing_referenced_adr():
    """Mutate: policy references ADR-006 but decisions only contains ADR-099."""
    from test_rules import test_gov_t10_decision_consistency
    path = Path(".agent/04-memory/decisions.md")

    def setup():
        content = """# Decisions

## ADR-099: Complete but unrelated
* **Context & problem**: Mutation test context.
* **Approved decision**: Keep only ADR-099.
* **Technical consequences**: Mutation test consequences.
"""
        backup = _backup_and_write(path, content)
        return [(path, backup)]

    return run_mutation(
        "T10-MISSING-REFERENCED-ADR",
        setup,
        test_gov_t10_decision_consistency,
    )


def mut_t10_incomplete_adr():
    """Mutate decisions.md to have an ADR missing required sections."""
    from test_rules import test_gov_t10_decision_consistency
    path = Path(".agent/04-memory/decisions.md")

    def setup():
        content = """# Decisions

## 🏛️ ADR-099: Incomplete Test Decision
* **Date**: 2026-01-01
* **Status**: Approved
* **Context & problem**:
  This ADR is intentionally missing Decision and Consequences sections.
"""
        backup = _backup_and_write(path, content)
        return [(path, backup)]

    return run_mutation("T10-INCOMPLETE-ADR", setup, test_gov_t10_decision_consistency)


def mut_t10_no_adr_with_rules():
    """Mutate: rules exist but no ADR recorded."""
    from test_rules import test_gov_t10_decision_consistency
    path = Path(".agent/04-memory/decisions.md")

    def setup():
        content = "# Decisions\n\nNo decisions recorded yet.\n"
        backup = _backup_and_write(path, content)
        return [(path, backup)]

    return run_mutation("T10-NO-ADR-WITH-RULES", setup, test_gov_t10_decision_consistency)


def mut_t03_bad_adr_format():
    """Mutate: ADR exists but missing Consequences section."""
    from test_memory import test_gov_t03_adr_structure
    path = Path(".agent/04-memory/decisions.md")

    def setup():
        content = """# Decisions

## 🏛️ ADR-099: Bad Format Decision
* **Date**: 2026-01-01
* **Status**: Approved
* **Context & problem**:
  Some context here.
* **Approved decision**:
  Some decision here.
"""
        backup = _backup_and_write(path, content)
        return [(path, backup)]

    return run_mutation("T03-BAD-ADR-FORMAT", setup, test_gov_t03_adr_structure)


def mut_t14_unknown_capability():
    """Mutate current task to reference an unknown capability."""
    import json
    from test_context import test_gov_t14_current_contract_resolves
    path = Path(".agent/task-contracts/current.json")

    def setup():
        original = json.loads(path.read_text(encoding="utf-8"))
        original["capabilities"] = ["definitely-unknown-capability"]
        backup = _backup_and_write(
            path,
            json.dumps(original, indent=2) + "\n",
        )
        return [(path, backup)]

    return run_mutation(
        "T14-UNKNOWN-CAPABILITY",
        setup,
        test_gov_t14_current_contract_resolves,
    )


def mut_t13_profile_gate_removed():
    """Mutate context map so full-stack resource loses its profile gate."""
    import json
    from test_context import test_gov_t13_profile_gate
    path = Path(".agent/01-core/context-map.json")

    def setup():
        data = json.loads(path.read_text(encoding="utf-8"))
        data["capabilities"]["full-stack-vertical"].pop(
            "requires_profile", None
        )
        backup = _backup_and_write(
            path,
            json.dumps(data, indent=2) + "\n",
        )
        return [(path, backup)]

    return run_mutation(
        "T13-PROFILE-GATE-REMOVED",
        setup,
        test_gov_t13_profile_gate,
    )


def mut_t15_missing_context_resource():
    """Mutate context map to reference a missing resource path."""
    import json
    from test_context import test_gov_t15_context_map_integrity
    path = Path(".agent/01-core/context-map.json")

    def setup():
        data = json.loads(path.read_text(encoding="utf-8"))
        data["capabilities"]["security"]["resources"][0]["path"] = (
            ".agent/02-rules/definitely-missing.md"
        )
        backup = _backup_and_write(
            path,
            json.dumps(data, indent=2) + "\n",
        )
        return [(path, backup)]

    return run_mutation(
        "T15-MISSING-CONTEXT-RESOURCE",
        setup,
        test_gov_t15_context_map_integrity,
    )


def mut_t16_missing_technology_profile():
    """Mutate Project Profile to reference a missing Technology Profile."""
    import json
    from test_context import test_gov_t16_project_profile_integrity
    path = Path(".agent/profiles/project.json")

    def setup():
        data = json.loads(path.read_text(encoding="utf-8"))
        data["technology_profiles"] = ["definitely-missing-profile"]
        backup = _backup_and_write(
            path,
            json.dumps(data, indent=2) + "\n",
        )
        return [(path, backup)]

    return run_mutation(
        "T16-MISSING-TECHNOLOGY-PROFILE",
        setup,
        test_gov_t16_project_profile_integrity,
    )


def mut_t18_remove_destructive_hard_stop():
    """Mutate approval policy so destructive risk can bypass human approval."""
    import json
    from test_execution import test_gov_t18_hard_stop_requires_human
    path = Path(".agent/01-core/approval-policy.json")

    def setup():
        data = json.loads(path.read_text(encoding="utf-8"))
        data["hard_stop_risks"] = [
            item for item in data.get("hard_stop_risks", [])
            if item != "destructive"
        ]
        backup = _backup_and_write(
            path,
            json.dumps(data, indent=2) + "\n",
        )
        return [(path, backup)]

    return run_mutation(
        "T18-REMOVE-DESTRUCTIVE-HARD-STOP",
        setup,
        test_gov_t18_hard_stop_requires_human,
    )


def mut_t20_evidence_always_passes():
    """Mutate evidence status derivation so every exit code becomes PASS."""
    from test_execution import test_gov_t20_evidence_status_is_derived
    path = Path(".agent/01-core/evidence_recorder.py")

    def setup():
        original = path.read_text(encoding="utf-8")
        mutated = original.replace(
            'return "PASS" if exit_code == 0 else "FAIL"',
            'return "PASS"',
        )
        backup = _backup_and_write(path, mutated)
        return [(path, backup)]

    return run_mutation(
        "T20-EVIDENCE-ALWAYS-PASSES",
        setup,
        test_gov_t20_evidence_status_is_derived,
    )


def mut_t23_revoke_registered_adr():
    """Mutate approval registry so ADR-008 is no longer approved."""
    import json
    from test_execution import test_gov_t23_registered_adr_auto_execute
    path = Path(".agent/01-core/approval-registry.json")

    def setup():
        data = json.loads(path.read_text(encoding="utf-8"))
        for entry in data.get("entries", []):
            if entry.get("id") == "ADR-008":
                entry["status"] = "revoked"
        backup = _backup_and_write(
            path,
            json.dumps(data, indent=2) + "\n",
        )
        return [(path, backup)]

    return run_mutation(
        "T23-REVOKE-REGISTERED-ADR",
        setup,
        test_gov_t23_registered_adr_auto_execute,
    )


def mut_t26_disable_archive_integrity_check():
    """Mutate evidence verification so tampered archives are accepted."""
    from test_execution import test_gov_t26_evidence_history_detects_tampering
    path = Path(".agent/01-core/evidence_recorder.py")

    def setup():
        original = path.read_text(encoding="utf-8")
        start = original.index("def verify_archive(path: Path) -> bool:")
        end = original.index("\ndef run_named_check(", start)
        mutated = (
            original[:start]
            + "def verify_archive(path: Path) -> bool:\n    return True\n\n"
            + original[end + 1:]
        )
        backup = _backup_and_write(path, mutated)
        return [(path, backup)]

    return run_mutation(
        "T26-DISABLE-ARCHIVE-INTEGRITY",
        setup,
        test_gov_t26_evidence_history_detects_tampering,
    )


def mut_t27_allow_unknown_risk():
    """Mutate Task Contract schema to accept an invented risk flag."""
    from test_execution import test_gov_t27_task_contract_rejects_unknown_risk
    path = Path(".agent/01-core/task_contract.py")

    def setup():
        original = path.read_text(encoding="utf-8")
        mutated = original.replace(
            '    "data_migration",\n}',
            '    "data_migration",\n    "invented_risk",\n}',
        )
        backup = _backup_and_write(path, mutated)
        return [(path, backup)]

    return run_mutation(
        "T27-ALLOW-UNKNOWN-RISK",
        setup,
        test_gov_t27_task_contract_rejects_unknown_risk,
    )


def mut_t30_forge_registry_source_marker():
    """Mutate ADR registry source marker so durable provenance no longer resolves."""
    import json
    from test_execution import test_gov_t30_approval_registry_sources_resolve
    path = Path(".agent/01-core/approval-registry.json")

    def setup():
        data = json.loads(path.read_text(encoding="utf-8"))
        for entry in data.get("entries", []):
            if entry.get("id") == "ADR-008":
                entry["source_marker"] = "ADR-DOES-NOT-EXIST"
        backup = _backup_and_write(
            path,
            json.dumps(data, indent=2) + "\n",
        )
        return [(path, backup)]

    return run_mutation(
        "T30-FORGE-REGISTRY-SOURCE-MARKER",
        setup,
        test_gov_t30_approval_registry_sources_resolve,
    )


def mut_t31_reject_registry_adr_status():
    """Mutate ADR-008 source status to Rejected; registry provenance must fail."""
    from test_execution import test_gov_t30_approval_registry_sources_resolve
    path = Path(".agent/04-memory/decisions.md")

    def setup():
        content = path.read_text(encoding="utf-8")
        start = content.find("## ADR-008:")
        if start < 0:
            raise RuntimeError("ADR-008 heading not found")
        end = content.find("\n## ", start + 1)
        if end < 0:
            end = len(content)
        section = content[start:end]
        if "* **Status**: Approved" not in section:
            raise RuntimeError("ADR-008 approved status not found")
        section = section.replace(
            "* **Status**: Approved",
            "* **Status**: Rejected",
            1,
        )
        mutated = content[:start] + section + content[end:]
        backup = _backup_and_write(path, mutated)
        return [(path, backup)]

    return run_mutation(
        "T31-REJECT-REGISTRY-ADR-STATUS",
        setup,
        test_gov_t30_approval_registry_sources_resolve,
    )


def mut_t31_remove_security_risk_mapping():
    """Mutate risk map so security_boundary no longer derives Security."""
    import json
    from test_context import test_gov_t31_security_risk_derives_security_context
    path = Path(".agent/01-core/context-map.json")

    def setup():
        data = json.loads(path.read_text(encoding="utf-8"))
        data.get("risk_capability_map", {}).pop("security_boundary", None)
        backup = _backup_and_write(
            path,
            json.dumps(data, indent=2) + "\n",
        )
        return [(path, backup)]

    return run_mutation(
        "T31-REMOVE-SECURITY-RISK-MAPPING",
        setup,
        test_gov_t31_security_risk_derives_security_context,
    )


def mut_t33_remove_workflow_area_mapping():
    """Mutate Project Profile so CI workflow paths no longer derive Deployment."""
    import json
    from test_context import test_gov_t33_workflow_area_derives_deployment_context
    path = Path(".agent/profiles/project.json")

    def setup():
        data = json.loads(path.read_text(encoding="utf-8"))
        data["area_capability_rules"] = [
            rule for rule in data.get("area_capability_rules", [])
            if rule.get("prefix") != ".github/workflows"
        ]
        backup = _backup_and_write(
            path,
            json.dumps(data, indent=2) + "\n",
        )
        return [(path, backup)]

    return run_mutation(
        "T33-REMOVE-WORKFLOW-AREA-MAPPING",
        setup,
        test_gov_t33_workflow_area_derives_deployment_context,
    )


def mut_t35_unknown_derived_capability():
    """Mutate risk map to reference a capability absent from Context Map."""
    import json
    from test_context import test_gov_t35_risk_and_area_maps_reference_known_capabilities
    path = Path(".agent/01-core/context-map.json")

    def setup():
        data = json.loads(path.read_text(encoding="utf-8"))
        data["risk_capability_map"]["security_boundary"] = [
            "definitely-unknown-capability"
        ]
        backup = _backup_and_write(
            path,
            json.dumps(data, indent=2) + "\n",
        )
        return [(path, backup)]

    return run_mutation(
        "T35-UNKNOWN-DERIVED-CAPABILITY",
        setup,
        test_gov_t35_risk_and_area_maps_reference_known_capabilities,
    )


def mut_t36_restore_stale_readme_contract():
    """Mutate README with a stale mandatory-bundle marker."""
    from test_rules import test_gov_t36_public_contract_sync
    path = Path("README.md")

    def setup():
        original = path.read_text(encoding="utf-8")
        mutated = original + "\n\nNothing is optional. Load ALL of it.\n"
        backup = _backup_and_write(path, mutated)
        return [(path, backup)]

    return run_mutation(
        "T36-RESTORE-STALE-README-CONTRACT",
        setup,
        test_gov_t36_public_contract_sync,
    )


def mut_t37_add_volatile_branch_state():
    """Mutate project context with volatile branch/PR transport state."""
    from test_memory import test_gov_t37_merge_safe_boot_memory
    path = Path(".agent/04-memory/project-context.md")

    def setup():
        original = path.read_text(encoding="utf-8")
        mutated = original + "\n- **Branch:** `temporary-feature`\n## Next\nMerge PR #999 next.\n"
        backup = _backup_and_write(path, mutated)
        return [(path, backup)]

    return run_mutation(
        "T37-ADD-VOLATILE-BRANCH-STATE",
        setup,
        test_gov_t37_merge_safe_boot_memory,
    )


def mut_t38_restore_stale_start_check():
    """Mutate start.py so --check falls back to runner.py again."""
    from test_rules import test_gov_t38_release_contract_entrypoints
    path = Path(".agent/start.py")

    def setup():
        original = path.read_text(encoding="utf-8")
        mutated = original.replace(
            'str(agent_dir / "governance" / "verify.py")',
            'str(agent_dir / "governance" / "runner.py")',
        )
        backup = _backup_and_write(path, mutated)
        return [(path, backup)]

    return run_mutation(
        "T38-RESTORE-STALE-START-CHECK",
        setup,
        test_gov_t38_release_contract_entrypoints,
    )


def mut_t39_leak_project_profile():
    """Mutate installer so source Project Profile leaks into consumer project."""
    from test_execution import test_gov_t39_sanitized_installer_excludes_source_state
    path = Path(".agent/install.py")

    def setup():
        original = path.read_text(encoding="utf-8")
        marker = "    if TECHNOLOGY_PROFILES.exists():\n"
        injected = (
            '    _copy_file(\n'
            '        SOURCE_AGENT / "profiles" / "project.json",\n'
            '        target_agent / "profiles" / "project.json",\n'
            '    )\n\n'
        )
        if marker not in original:
            raise RuntimeError("installer insertion marker not found")
        mutated = original.replace(marker, injected + marker, 1)
        backup = _backup_and_write(path, mutated)
        return [(path, backup)]

    return run_mutation(
        "T39-LEAK-PROJECT-PROFILE",
        setup,
        test_gov_t39_sanitized_installer_excludes_source_state,
    )


def mut_t11_boot_too_large():
    """Mutate: inflate boot-manifest.md beyond hard limit."""
    from test_memory import test_gov_t11_boot_context_budget
    path = Path(".agent/01-core/boot-manifest.md")

    def setup():
        filler = "\n".join(f"# Filler line {i}" for i in range(400))
        content = f"# Inflated Boot Manifest\n\n{filler}\n"
        backup = _backup_and_write(path, content)
        return [(path, backup)]

    return run_mutation("T11-BOOT-TOO-LARGE", setup, test_gov_t11_boot_context_budget)


if __name__ == "__main__":
    print("🧬 [AOS v8.0-dev] Running Mutation Tests...")
    print("=" * 60)
    print("Each test introduces a deliberate violation and verifies")
    print("the governance check correctly detects it.\n")

    mutations = [
        mut_t04_exceed_mistakes_cap,
        mut_t05_missing_memory_file,
        mut_t09_done_without_state_history,
        mut_t10_missing_referenced_adr,
        mut_t10_incomplete_adr,
        mut_t10_no_adr_with_rules,
        mut_t03_bad_adr_format,
        mut_t13_profile_gate_removed,
        mut_t14_unknown_capability,
        mut_t15_missing_context_resource,
        mut_t16_missing_technology_profile,
        mut_t18_remove_destructive_hard_stop,
        mut_t20_evidence_always_passes,
        mut_t23_revoke_registered_adr,
        mut_t26_disable_archive_integrity_check,
        mut_t27_allow_unknown_risk,
        mut_t30_forge_registry_source_marker,
        mut_t31_reject_registry_adr_status,
        mut_t31_remove_security_risk_mapping,
        mut_t33_remove_workflow_area_mapping,
        mut_t35_unknown_derived_capability,
        mut_t36_restore_stale_readme_contract,
        mut_t37_add_volatile_branch_state,
        mut_t38_restore_stale_start_check,
        mut_t39_leak_project_profile,
        mut_t11_boot_too_large,
    ]

    passed = 0
    failed = 0
    for mut_fn in mutations:
        if mut_fn():
            passed += 1
        else:
            failed += 1

    print(f"\n{'=' * 60}")
    print(f"📊 Mutations: {passed} detected / {failed} missed / {len(mutations)} total")

    if failed > 0:
        print("🚨 Some mutations were NOT detected — governance has gaps!")
        sys.exit(1)
    else:
        print("🎉 All mutations correctly detected — no rubber-stamps!")
        sys.exit(0)
