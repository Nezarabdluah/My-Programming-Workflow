# 🔄 Master Pipeline — Coordinator

> Full project lifecycle: from initial intake to post-launch monitoring.
> Path: `.agent/03-workflows/master-pipeline/`
> Pattern: coordinator + split stages (like mobile-qa / security-gate)

---

## Invocation

When a **full project pipeline** is requested (Path D: "full project / from scratch to production"), read this file first, then execute stages in order.

User inputs:
- **Project name** — mandatory
- **Classification** — mandatory: 🟢 Simple / 🟡 Medium / 🔴 Sensitive
- **Stack** (optional): auto-detected from codebase if omitted
- **Extra details** (optional): constraints, deadlines, compliance requirements

---

## DoD Ladder — Definition of Done by Classification

```
┌────────────────────────────────────┬───────┬──────┬──────────┐
│ Stage                              │  🟢   │  🟡  │    🔴    │
├────────────────────────────────────┼───────┼──────┼──────────┤
│ 0. Intake & Classification        │  ✅   │  ✅  │   ✅     │
│ 1. Requirements & Specs           │  —    │  ✅  │   ✅     │
│ 2. Architecture & Design          │  —    │  —   │   ✅     │
│ 3. Threat Model & Security Design │  —    │  —   │   ✅     │
│ 4. Implementation                 │  ✅   │  ✅  │   ✅     │
│ 5. Testing & Quality Gate         │  ✅   │  ✅  │   ✅     │
│ 6. Production Readiness Review    │  —    │  —   │   ✅     │
│ 7. Deployment & Rollout           │  —    │  —   │   ✅     │
│ 8. Post-Launch Monitoring         │  —    │  —   │   ✅     │
└────────────────────────────────────┴───────┴──────┴──────────┘

🟢 Simple   = stages 0, 4, 5 only (mini-build)
🟡 Medium   = stages 0, 1, 4, 5 (with specs)
🔴 Sensitive = ALL stages 0–8 (full pipeline)
```

Stages marked `—` are **skipped** with `⛔ GATE SKIPPED — classification does not require this stage`.

---

## Stages

0. `stage-0-intake.md` — Project intake, classification, and codebase discovery
1. `stage-1-requirements.md` — Requirements analysis, user stories, acceptance criteria (SDD: Draft → Clarify → Approved)
2. `stage-2-architecture.md` — Architecture & design decisions (ADR), dependency map
3. `stage-3-threat-model.md` — STRIDE threat model, security design review
4. `stage-4-implementation.md` — Code implementation (MVP increments, vertical slices)
5. `stage-5-testing.md` — Testing & quality gate (unit, integration, E2E)
6. `stage-6-production-readiness.md` — PRR scorecard, SLO definition, runbook
7. `stage-7-deployment.md` — Deployment strategy, rollback plan, release
8. `stage-8-post-launch.md` — Post-launch monitoring, DORA metrics, retrospective

---

## Decision Gate — applied before every stage

```yaml
# Before moving to any stage — verify:
gate:
  stage_number: N
  stage_name: ""
  classification: 🟢 | 🟡 | 🔴
  stage_required: true | false              # per DoD ladder above
  previous_stage_status: passed | failed | skipped | blocked
  blockers_exist: true | false
  resources_loaded: []                      # from wiring-registry
  decision: proceed | skip | block

# Decisions:
#   proceed → load stage file and execute
#   skip    → record ⛔ GATE SKIPPED with reason, move to next stage
#   block   → record ⛔ GATE FAILED, stop the pipeline entirely
```

---

## Hard Stop-Gate Tags

Use these tags explicitly at every gate decision point:

| Tag | Meaning |
|-----|---------|
| `✅ GATE PASSED` | All gate conditions met — proceed to next stage |
| `⛔ GATE FAILED` | Critical blocker — pipeline halted until resolved |
| `⛔ GATE SKIPPED` | Stage not required by classification — skip with reason |
| `⛔ NEEDS CLARIFICATION` | Ambiguity or missing input — stop and ask the developer |

---

## Mandatory Resource Injection Protocol

> **"Availability is not enough — ENFORCEMENT is what separates professional systems from amateur ones."**

Before entering ANY stage, the model MUST:

1. **Read `05-references/books/00-master-index.md`** — find the current stage's row.
2. **Load every MUST resource** listed for that stage (constitutions, rules, prompts, templates).
3. **Check every IF condition** and load matched resources.
4. **Cite loaded resources** in a Resource Injection Block at the top of the stage output:

```yaml
# RESOURCE INJECTION — Stage N: [Name]
constitutions_loaded:
  - arch-constitution.md      # [cite specific rules applied]
  - security-constitution.md  # [cite specific rules applied]
rules_loaded:
  - architecture-and-design.md  # REF-ARCH-DEP, REF-ARCH-ISOL
refs_grepped:
  - devops: [OPS-SECTEST]       # matched: line 450
prompts_injected:
  - backend-prompts.md          # active for .NET generation
templates_used:
  - entity-pattern.md           # for new entity creation
coverage: "5/5 MUST loaded | 1/2 IF triggered"
```

5. **Produce a Resource Utilization Summary** before marking stage as Done (see master-index template).

## Handoff Contract — embedded

```yaml
pipeline:
  project: ""
  classification: 🟢 | 🟡 | 🔴
  stack: ""
  status: running | passed | failed | blocked | partial
  current_stage: 0
  started_at: ""

stages:
  0_intake: { status: pending, gate: null }
  1_requirements: { status: pending, gate: null }
  2_architecture: { status: pending, gate: null }
  3_threat_model: { status: pending, gate: null }
  4_implementation: { status: pending, gate: null }
  5_testing: { status: pending, gate: null }
  6_production_readiness: { status: pending, gate: null }
  7_deployment: { status: pending, gate: null }
  8_post_launch: { status: pending, gate: null }

issues: []           # accumulated from all stages
decisions: []        # ADRs recorded during stages 2-3
evidence: []         # test reports, scan results
next_action: ""
```

---

## Safety Rules

- ❌ Never skip a required stage without explicit developer override
- ❌ Never mark a gate as PASSED without verifiable evidence
- ❌ Never proceed past a FAILED gate — resolve or escalate first
- ⚠️ A `⛔ NEEDS CLARIFICATION` pauses the pipeline until the developer responds
- ⚠️ Classification can only be escalated (🟢→🟡→🔴), never downgraded, without a recorded ADR
- ⚠️ Memory updates are mandatory after every stage completion (active-tasks + project-context)

---

## Memory Note

> Update `project-context.md` and `active-tasks.md` after every stage gate.
> Do not update after sub-steps within a stage — only at gate boundaries.
> Pipeline status is tracked in the handoff contract above and in `active-tasks.md`.

---

Start stage 0 now.
