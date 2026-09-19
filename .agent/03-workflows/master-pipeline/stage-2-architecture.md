# Master Pipeline — Stage 2: Architecture & Design

> This is stage 2 of 8. Next: `stage-3-threat-model.md`
> Required for: 🔴 | Skipped for: 🟢 🟡

---

## Decision Gate

```yaml
gate:
  stage_number: 2
  stage_name: "Architecture & Design"
  classification_required: [🔴]
  previous_stage_status: passed       # stage 1 must pass
  requires:
    - approved specs from stage 1
  context_candidates:
    - 02-rules/architecture-and-design.md (when the task uses these architectural patterns)
    - arch/ddd/integration constitutions only when materially relevant
    - targeted REF-ARCH anchors when evidence is needed
  decision: proceed | skip

# Skip condition: classification ∈ {🟢, 🟡}
#   → ⛔ GATE SKIPPED — classification does not require formal architecture review
```

---

## Task: architecture design and ADR recording

### 2.1 — Dependency Map

```
□ Map the components and boundaries actually used by this project/feature.
□ Verify dependencies against the project's established architecture and approved ADRs.
□ Check for circular or forbidden dependencies where the chosen architecture defines such constraints.
□ Use REF-ARCH guidance only when its architectural model applies to this project.
```

### 2.2 — Domain Modeling (if DDD applies)

```
□ Identify and document:
  - Aggregates and Aggregate Roots (REF-ARCH-AGGR)
  - Value Objects (REF-ARCH-VO)
  - Domain Events
  - Repository contracts (REF-ARCH-REPO)
□ Apply SOLID principles (REF-ARCH-SOLID)
```

### 2.3 — Architecture Decision Record (ADR)

```
□ For every significant design decision:
  - Record an ADR in 04-memory/decisions.md using the template from adr/adr-template.md
  - Document: context, decision, rejected alternatives (with reasons), consequences
  - Include performance, maintainability, and security impact

□ Minimum required ADRs for 🔴:
  - Data model / persistence strategy
  - API design / communication patterns
  - Any third-party service integration
```

### 2.4 — Developer Review Gate

```
⏸️ HARD STOP — present architecture to the developer for review.

□ Present the dependency map and ADRs
□ Wait for explicit approval

  Developer approves → ✅ GATE PASSED
  Developer requests changes → revise architecture and ADRs
  Developer rejects → ⛔ GATE FAILED — record reason
```

---

## Context Expansion (selective)

| Resource | When |
|----------|------|
| `02-rules/architecture-and-design.md` | When Clean Architecture / DDD / module-design guidance applies |
| Grep `REF-ARCH-DEP, ISOL, AGGR, VO, REPO, SOLID, FACADE` | During dependency and domain modeling |
| Books: grep `Clean Architecture`, `Aggregate`, `SOLID` | When justifying design decisions |

---

## Gate Output

```yaml
gate_result:
  stage: 2
  status: ✅ GATE PASSED | ⛔ GATE FAILED | ⛔ NEEDS CLARIFICATION
  adrs_recorded: []                   # list of ADR IDs
  dependency_map_verified: true | false
  developer_approved: true | false
  next_stage: 3
  blockers: []
```

> After gate passes → update `decisions.md` with all new ADRs.
