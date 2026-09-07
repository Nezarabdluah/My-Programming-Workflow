# Master Pipeline — Stage 5: Testing & Quality Gate

> This is stage 5 of 8. Next: `stage-6-production-readiness.md`
> Required for: 🟢 🟡 🔴 (all classifications)

---

## Decision Gate

```yaml
gate:
  stage_number: 5
  stage_name: "Testing & Quality Gate"
  classification_required: [🟢, 🟡, 🔴]
  previous_stage_status: passed       # stage 4 must pass
  requires:
    - completed implementation (stage 4)
    - test infrastructure identified (or declared unavailable)
  resources_loaded:
    - "⚠️ MANDATORY: read 05-references/books/00-master-index.md → Stage 5 row"
    - constitutions: security-constitution (AUDIT self-check) + perf-constitution (N+1, SARGable)
    - 02-rules/testing-and-quality.md
    - 03-workflows/qa-strategy.md
    - wiring-registry → REF-TEST contracts
  decision: proceed
```

---

## Task: verify implementation against quality standards

### 5.1 — Test Pyramid Execution

```
□ Execute tests bottom-up per the test pyramid (QA: grep [QA-PYRAMID]):

  Layer 1 — Unit Tests (REF-TEST-BEHAV):
    - Test behavior, not implementation details
    - Mock only external dependencies (REF-TEST-MOCK)
    - Run: [project test command]
    - Result: ✅ PASSED / ⛔ FAILED (with failure details)

  Layer 2 — Integration Tests:
    - Test component interactions and data flow
    - Verify database queries (REF-DB-N1, REF-DB-SARG)
    - Run: [project integration test command]
    - Result: ✅ PASSED / ⛔ FAILED / NOT_AVAILABLE

  Layer 3 — E2E / Smoke Tests (QA: grep [QA-E2E-SMOKE]):
    - Test critical user paths end-to-end
    - Run: [project E2E command]
    - Result: ✅ PASSED / ⛔ FAILED / NOT_AVAILABLE
```

### 5.2 — Static Analysis & Linting

```
□ Run available static analysis tools:
  - Linter: [tool] → result
  - Type checker: [tool] → result
  - Security scanner: [tool] → result (if available)
  - Result: ✅ PASSED / ⛔ FAILED / NOT_AVAILABLE
```

### 5.3 — Vertical Slice Coverage Report

```
□ Produce the mandatory coverage report (02-rules/vertical-slice-governance.md):

  | Layer        | Status                                    |
  |--------------|-------------------------------------------|
  | Database     | done / not applicable because... / deferred because... |
  | Domain       | done / not applicable because... / deferred because... |
  | Application  | done / not applicable because... / deferred because... |
  | API          | done / not applicable because... / deferred because... |
  | Frontend     | done / not applicable because... / deferred because... |
  | UI/UX        | done / not applicable because... / deferred because... |
  | Tests        | done / not applicable because... / deferred because... |

□ Include: file_path:line for every "done" entry
□ Any missing layer without justification → ⛔ GATE FAILED
```

### 5.4 — Quality Gate Decision

```
□ All tests pass (or NOT_AVAILABLE with justification):
  → ✅ GATE PASSED

□ Any test failure without a fix:
  → ⛔ GATE FAILED — return to stage 4 for fixes

□ Coverage report incomplete:
  → ⛔ GATE FAILED — complete the report before proceeding
```

---

## Resource Injection (from wiring-registry)

| Resource | When |
|----------|------|
| `02-rules/testing-and-quality.md` | Always at stage entry |
| Grep `REF-TEST-BEHAV, MOCK` | During test writing |
| QA: grep `[QA-PYRAMID]`, `[QA-L0-LOGIC]`, `[QA-UNIT]` | For test strategy |
| QA: grep `[QA-E2E-SMOKE]`, `[QA-API-NEWMAN]` | For E2E and API tests |
| QA: grep `[QA-CHECKLISTS]` | For pre-delivery checklist |

---

## Gate Output

```yaml
gate_result:
  stage: 5
  status: ✅ GATE PASSED | ⛔ GATE FAILED
  unit_tests: { passed: 0, failed: 0, skipped: 0 }
  integration_tests: { passed: 0, failed: 0, status: available | not_available }
  e2e_tests: { passed: 0, failed: 0, status: available | not_available }
  static_analysis: passed | failed | not_available
  coverage_report: complete | incomplete
  next_stage: 6 | done              # 6 if 🔴, done if 🟢/🟡
  blockers: []
```

> After gate passes → for 🟢/🟡 the pipeline is DONE. For 🔴 continue to stage 6.
