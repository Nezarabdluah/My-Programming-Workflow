# Master Pipeline — Stage 7: Deployment & Rollout

> This is stage 7 of 8. Next: `stage-8-post-launch.md`
> Required for: 🔴 | Skipped for: 🟢 🟡

---

## Decision Gate

```yaml
gate:
  stage_number: 7
  stage_name: "Deployment & Rollout"
  classification_required: [🔴]
  previous_stage_status: passed       # stage 6 must pass
  requires:
    - PRR passed or conditionally passed (stage 6)
    - deployment target identified (staging / production)
  resources_loaded:
    - "⚠️ MANDATORY: read 05-references/books/00-master-index.md → Stage 7 row"
    - constitutions: resilience-constitution (rollback design, graceful degradation)
    - wiring-registry → OPS-ROLLBACK
  decision: proceed | skip

# Skip condition: classification ∈ {🟢, 🟡}
#   → ⛔ GATE SKIPPED — classification does not require formal deployment planning
```

---

## Task: deployment planning and execution

### 7.1 — Deployment Strategy

```
□ Define the deployment approach:
  - Blue/Green deployment
  - Canary release (percentage-based rollout)
  - Rolling update
  - Feature flags (dark launch)

□ Document the chosen strategy with rationale
□ Record as an ADR if this is the first deployment of this type
```

### 7.2 — Rollback Plan

```
□ Define the rollback procedure (grep [OPS-ROLLBACK]):
  - Rollback trigger conditions (error rate, latency spike, manual)
  - Rollback steps (automated / manual)
  - Data migration rollback (if applicable)
  - Estimated rollback time
  - Responsible team/person

□ ⚠️ A deployment without a documented rollback plan → ⛔ GATE FAILED
```

### 7.3 — Pre-Deployment Checklist

```
□ Verify before deploying:
  - [ ] All tests passing (stage 5 evidence)
  - [ ] PRR passed (stage 6 evidence)
  - [ ] Database migrations tested and reversible
  - [ ] Environment variables / secrets configured
  - [ ] Monitoring and alerting active
  - [ ] Rollback plan documented and tested
  - [ ] Change communication sent (if required)
```

### 7.4 — Deployment Execution

```
□ Execute deployment to the target environment:
  - Record the deployment timestamp
  - Monitor initial health checks
  - Verify smoke tests pass in production

□ Post-deployment verification:
  - Service responding correctly
  - No error spike in logs/monitoring
  - Key user flows working (manual or automated smoke)
```

### 7.5 — Deployment Gate Decision

```
□ Deployment successful + smoke tests pass:
  → ✅ GATE PASSED

□ Deployment failed or smoke tests fail:
  → Execute rollback plan immediately
  → ⛔ GATE FAILED — record root cause, return to stage 4 or 5
```

---

## Resource Injection (from wiring-registry)

| Resource | When |
|----------|------|
| DevOps: grep `[OPS-ROLLBACK]` | Rollback plan design |
| DevOps: grep `[OPS-SIGNALS]` | Post-deployment health monitoring |
| `02-rules/network-and-api.md` | If API versioning is involved |

---

## Gate Output

```yaml
gate_result:
  stage: 7
  status: ✅ GATE PASSED | ⛔ GATE FAILED
  deployment_strategy: ""
  rollback_plan_documented: true | false
  deployment_timestamp: ""
  smoke_tests: passed | failed | not_available
  rollback_executed: true | false
  next_stage: 8
  blockers: []
```

> After gate passes → update `project-context.md` with deployment status.
