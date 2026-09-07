# Master Pipeline — Stage 6: Production Readiness Review (PRR)

> This is stage 6 of 8. Next: `stage-7-deployment.md`
> Required for: 🔴 | Skipped for: 🟢 🟡

---

## Decision Gate

```yaml
gate:
  stage_number: 6
  stage_name: "Production Readiness Review"
  classification_required: [🔴]
  previous_stage_status: passed       # stage 5 must pass
  requires:
    - all tests passing (stage 5)
    - architecture approved (stage 2)
    - threat model approved (stage 3)
  resources_loaded:
    - "⚠️ MANDATORY: read 05-references/books/00-master-index.md → Stage 6 row"
    - constitutions: resilience-constitution (Circuit Breaker, Outbox, Concurrency)
    - 03-workflows/production-readiness.md
    - wiring-registry → OPS-PRR, OPS-SCORECARD, OPS-SIGNALS
  decision: proceed | skip

# Skip condition: classification ∈ {🟢, 🟡}
#   → ⛔ GATE SKIPPED — classification does not require PRR
```

---

## Task: production readiness assessment

### 6.1 — PRR Scorecard

```
□ Load 03-workflows/production-readiness.md and follow the scorecard
□ Grep [OPS-PRR] and [OPS-SCORECARD] in devops reference for criteria
□ Assess each dimension:

  | Dimension          | Score | Evidence |
  |--------------------|-------|----------|
  | Reliability        |       |          |
  | Scalability        |       |          |
  | Observability      |       |          |
  | Security           |       |          |
  | Disaster Recovery  |       |          |
  | Documentation      |       |          |
  | Operational Runbook|       |          |
```

### 6.2 — SLO Definition

```
□ Define Service Level Objectives (grep [OPS-SLO]):
  - Availability target (e.g., 99.9%)
  - Latency targets (p50, p95, p99)
  - Error budget
  - Measurement method
```

### 6.3 — Observability Verification

```
□ Verify observability stack (grep [OPS-OBSERVABILITY], [OPS-ALERTS]):
  - Structured logging in place (REF-OBS-LOG)
  - Distributed tracing configured (REF-OBS-TRACE)
  - Alerting rules defined
  - Dashboard / monitoring available
```

### 6.4 — PRR Gate Decision

```
□ All scorecard dimensions ≥ minimum threshold:
  → ✅ GATE PASSED

□ Any critical dimension below threshold:
  → ⛔ GATE FAILED — resolve before deployment

□ Non-critical gaps with mitigation plan:
  → ✅ GATE PASSED with conditions (list the conditions)
```

---

## Resource Injection (from wiring-registry)

| Resource | When |
|----------|------|
| `03-workflows/production-readiness.md` | Always at stage entry |
| DevOps: grep `[OPS-PRR]`, `[OPS-SCORECARD]` | Scorecard assessment |
| DevOps: grep `[OPS-SLO]`, `[OPS-SIGNALS]` | SLO definition |
| DevOps: grep `[OPS-OBSERVABILITY]`, `[OPS-ALERTS]` | Observability check |
| `02-rules/testing-and-quality.md` §2 | REF-OBS-LOG, REF-OBS-TRACE |

---

## Gate Output

```yaml
gate_result:
  stage: 6
  status: ✅ GATE PASSED | ⛔ GATE FAILED | ⛔ NEEDS CLARIFICATION
  prr_scorecard: { passed: 0, failed: 0, conditional: 0 }
  slo_defined: true | false
  observability_verified: true | false
  conditions: []                      # conditions for conditional pass
  next_stage: 7
  blockers: []
```

> After gate passes → update `project-context.md` with PRR status.
