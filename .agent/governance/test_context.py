"""AOS Governance — Context Broker Tests (v8 Sprint 2)."""

import importlib.util
import json
from pathlib import Path

PASS = "PASS"
FAIL = "FAIL"


def _load_broker():
    path = Path(".agent/01-core/context_broker.py")
    if not path.exists():
        raise RuntimeError("context_broker.py missing")
    spec = importlib.util.spec_from_file_location("aos_context_broker", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def test_gov_t12_context_broker_minimality():
    """GOV-T12: Security task must not load unrelated DB/API rule files."""
    broker = _load_broker()
    context_map = _json(".agent/01-core/context-map.json")
    project = _json(".agent/profiles/project.json")

    task = {
        "task_id": "mutation-free-t12",
        "classification": "sensitive",
        "capabilities": ["security"],
    }
    result = broker.resolve_context(task, project, context_map)
    paths = {resource["path"] for resource in result["resources"]}

    required = ".agent/02-rules/security-checklist.md"
    forbidden = {
        ".agent/02-rules/database-performance.md",
        ".agent/02-rules/network-and-api.md",
        ".agent/02-rules/architecture-and-design.md",
    }

    if required not in paths:
        return FAIL, "GOV-T12: security capability did not load security rule."
    leaked = sorted(paths.intersection(forbidden))
    if leaked:
        return FAIL, f"GOV-T12: unrelated resources leaked into context: {leaked}"

    return PASS, f"GOV-T12: minimal security context resolved ({len(paths)} paths)."


def test_gov_t13_profile_gate():
    """GOV-T13: Profile-gated resources load only when profile is active."""
    broker = _load_broker()
    context_map = _json(".agent/01-core/context-map.json")
    project = _json(".agent/profiles/project.json")

    task = {
        "task_id": "profile-gate-t13",
        "classification": "medium",
        "capabilities": ["full-stack-vertical"],
    }

    result = broker.resolve_context(task, project, context_map)
    paths = {resource["path"] for resource in result["resources"]}
    vertical = ".agent/02-rules/vertical-slice-governance.md"

    if vertical in paths:
        return FAIL, "GOV-T13: full-stack resource loaded without full-stack-web profile."
    if not result["skipped"]:
        return FAIL, "GOV-T13: broker did not record profile-gated skip."

    project_with_profile = dict(project)
    project_with_profile["technology_profiles"] = list(
        project.get("technology_profiles", [])
    ) + ["full-stack-web"]
    activated = broker.resolve_context(task, project_with_profile, context_map)
    active_paths = {resource["path"] for resource in activated["resources"]}

    if vertical not in active_paths:
        return FAIL, "GOV-T13: full-stack resource missing after profile activation."

    return PASS, "GOV-T13: profile-gated resource activation works correctly."


def test_gov_t14_current_contract_resolves():
    """GOV-T14: Current task contract resolves without unknown capabilities."""
    broker = _load_broker()
    task = _json(".agent/task-contracts/current.json")
    project = _json(".agent/profiles/project.json")
    context_map = _json(".agent/01-core/context-map.json")

    try:
        result = broker.resolve_context(task, project, context_map)
    except Exception as exc:
        return FAIL, f"GOV-T14: current task contract failed to resolve: {exc}"

    if not result["resources"]:
        return FAIL, "GOV-T14: current task resolved to empty context."

    return PASS, (
        f"GOV-T14: {task['task_id']} resolved "
        f"{len(result['resources'])} resource entries."
    )


def test_gov_t15_context_map_integrity():
    """GOV-T15: Executable context map stays valid and cataloged."""
    context_map = _json(".agent/01-core/context-map.json")
    wiring = Path(".agent/01-core/wiring-registry.md").read_text(encoding="utf-8")

    capabilities = context_map.get("capabilities", {})
    if not capabilities:
        return FAIL, "GOV-T15: context map contains no capabilities."

    missing_labels = []
    missing_paths = []
    for capability, definition in capabilities.items():
        label = definition.get("catalog_label")
        if not label or label not in wiring:
            missing_labels.append(capability)

        for resource in definition.get("resources", []):
            path = resource.get("path")
            if not path or not Path(path).exists():
                missing_paths.append(f"{capability}:{path}")

    if missing_labels:
        return FAIL, (
            "GOV-T15: capability missing from human wiring catalog: "
            + ", ".join(sorted(missing_labels))
        )

    if missing_paths:
        return FAIL, (
            "GOV-T15: context map points to missing resources: "
            + ", ".join(sorted(missing_paths))
        )

    return PASS, (
        f"GOV-T15: {len(capabilities)} executable capabilities are "
        "cataloged and all resource paths exist."
    )


def test_gov_t16_project_profile_integrity():
    """GOV-T16: Project Profile references real Technology Profiles and commands."""
    project = _json(".agent/profiles/project.json")
    profiles = project.get("technology_profiles", [])
    if not isinstance(profiles, list):
        return FAIL, "GOV-T16: technology_profiles must be a list."

    missing_profiles = []
    for profile_id in profiles:
        path = Path(f".agent/profiles/technology/{profile_id}.json")
        if not path.exists():
            missing_profiles.append(profile_id)

    if missing_profiles:
        return FAIL, (
            "GOV-T16: missing Technology Profile file(s): "
            + ", ".join(sorted(missing_profiles))
        )

    commands = project.get("commands", {})
    if not isinstance(commands, dict) or not commands:
        return FAIL, "GOV-T16: project commands are missing."

    empty_commands = [
        name for name, command in commands.items()
        if not isinstance(command, str) or not command.strip()
    ]
    if empty_commands:
        return FAIL, (
            "GOV-T16: empty project command(s): "
            + ", ".join(sorted(empty_commands))
        )

    return PASS, (
        f"GOV-T16: {len(profiles)} Technology Profile(s) resolve and "
        f"{len(commands)} project command(s) are defined."
    )


def test_gov_t31_security_risk_derives_security_context():
    """GOV-T31: security_boundary risk derives Security + Testing context."""
    broker = _load_broker()
    context_map = _json(".agent/01-core/context-map.json")
    project = _json(".agent/profiles/project.json")
    task = {
        "task_id": "t31",
        "classification": "sensitive",
        "capabilities": [],
        "affected_areas": [],
        "risk": {"security_boundary": True},
    }

    result = broker.resolve_context(task, project, context_map)
    effective = set(result["effective_capabilities"])
    paths = {resource["path"] for resource in result["resources"]}

    if not {"security", "testing"}.issubset(effective):
        return FAIL, f"GOV-T31: missing derived capabilities: {effective}"
    if ".agent/02-rules/security-checklist.md" not in paths:
        return FAIL, "GOV-T31: security rule missing from derived context."
    sources = result["capability_sources"].get("security", [])
    if "risk:security_boundary" not in sources:
        return FAIL, f"GOV-T31: risk provenance missing: {sources}"

    return PASS, "GOV-T31: security risk deterministically derives Security/Testing."


def test_gov_t32_data_migration_derives_database_context():
    """GOV-T32: data_migration risk derives Database + Testing context."""
    broker = _load_broker()
    context_map = _json(".agent/01-core/context-map.json")
    project = _json(".agent/profiles/project.json")
    task = {
        "task_id": "t32",
        "classification": "sensitive",
        "capabilities": [],
        "affected_areas": [],
        "risk": {"data_migration": True},
    }

    result = broker.resolve_context(task, project, context_map)
    effective = set(result["effective_capabilities"])
    paths = {resource["path"] for resource in result["resources"]}

    if not {"database", "testing"}.issubset(effective):
        return FAIL, f"GOV-T32: missing DB/testing capabilities: {effective}"
    if ".agent/02-rules/database-performance.md" not in paths:
        return FAIL, "GOV-T32: database rule missing from migration context."

    return PASS, "GOV-T32: data migration derives Database/Testing context."


def test_gov_t33_workflow_area_derives_deployment_context():
    """GOV-T33: .github/workflows affected area derives Deployment + Testing."""
    broker = _load_broker()
    context_map = _json(".agent/01-core/context-map.json")
    project = _json(".agent/profiles/project.json")
    task = {
        "task_id": "t33",
        "classification": "medium",
        "capabilities": [],
        "affected_areas": [".github/workflows/aos-verify.yml"],
        "risk": {},
    }

    result = broker.resolve_context(task, project, context_map)
    effective = set(result["effective_capabilities"])
    paths = {resource["path"] for resource in result["resources"]}

    if not {"deployment", "testing"}.issubset(effective):
        return FAIL, f"GOV-T33: workflow area missing capabilities: {effective}"
    deployment = ".agent/03-workflows/master-pipeline/stage-7-deployment.md"
    if deployment not in paths:
        return FAIL, "GOV-T33: deployment workflow missing from derived context."
    sources = result["capability_sources"].get("deployment", [])
    if "area:.github/workflows" not in sources:
        return FAIL, f"GOV-T33: area provenance missing: {sources}"

    return PASS, "GOV-T33: CI workflow area derives Deployment/Testing context."


def test_gov_t34_capability_sources_deduplicate():
    """GOV-T34: One capability may have multiple provenance sources without duplication."""
    broker = _load_broker()
    context_map = _json(".agent/01-core/context-map.json")
    project = _json(".agent/profiles/project.json")
    task = {
        "task_id": "t34",
        "classification": "sensitive",
        "capabilities": ["testing"],
        "affected_areas": [".github/workflows/aos-verify.yml"],
        "risk": {"production_change": True},
    }

    result = broker.resolve_context(task, project, context_map)
    effective = result["effective_capabilities"]
    if effective.count("testing") != 1:
        return FAIL, f"GOV-T34: testing duplicated in effective list: {effective}"

    sources = set(result["capability_sources"].get("testing", []))
    required = {
        "explicit",
        "risk:production_change",
        "area:.github/workflows",
    }
    if not required.issubset(sources):
        return FAIL, f"GOV-T34: missing provenance source(s): {sources}"

    return PASS, "GOV-T34: capability de-duplication preserves all provenance."


def test_gov_t35_risk_and_area_maps_reference_known_capabilities():
    """GOV-T35: Risk/area derivation maps can reference only executable capabilities."""
    context_map = _json(".agent/01-core/context-map.json")
    project = _json(".agent/profiles/project.json")
    known = set(context_map.get("capabilities", {}))

    bad_risks = []
    for risk, capabilities in context_map.get("risk_capability_map", {}).items():
        if not isinstance(capabilities, list):
            bad_risks.append(f"{risk}:not-list")
            continue
        for capability in capabilities:
            if capability not in known:
                bad_risks.append(f"{risk}:{capability}")

    bad_areas = []
    seen_prefixes = set()
    for rule in project.get("area_capability_rules", []):
        prefix = rule.get("prefix")
        if prefix in seen_prefixes:
            bad_areas.append(f"duplicate:{prefix}")
        seen_prefixes.add(prefix)
        for capability in rule.get("capabilities", []):
            if capability not in known:
                bad_areas.append(f"{prefix}:{capability}")

    if bad_risks or bad_areas:
        return FAIL, (
            "GOV-T35: invalid derivation mapping(s): "
            + ", ".join(bad_risks + bad_areas)
        )

    return PASS, "GOV-T35: risk/area maps reference only known capabilities."
