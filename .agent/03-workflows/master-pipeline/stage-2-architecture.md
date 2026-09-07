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
  resources_loaded:
    - "⚠️ MANDATORY: read 05-references/books/00-master-index.md → Stage 2 row"
    - constitutions: arch-constitution + ddd-constitution + integration-constitution (if multi-module)
    - 02-rules/architecture-and-design.md
    - wiring-registry → REF-ARCH contracts
  decision: proceed | skip

# Skip condition: classification ∈ {🟢, 🟡}
#   → ⛔ GATE SKIPPED — classification does not require formal architecture review
```

---

## Task: architecture design and ADR recording

### 2.1 — Dependency Map

```
□ Map the component dependency graph for the feature:
  - Identify layers: Database → Domain → Application → API → Frontend → UI/UX → Tests
  - Verify one-way dependency flow (no circular references)
  - Grep REF-ARCH-DEP in engineering-rules-catalog-REF.md for compliance
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

## Resource Injection (from wiring-registry)

| Resource | When |
|----------|------|
| `02-rules/architecture-and-design.md` | Always at stage entry |
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
