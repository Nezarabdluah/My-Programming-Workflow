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
  context_candidates:
    - 03-workflows/qa-strategy.md
    - 02-rules/testing-and-quality.md when testing guidance is needed
    - security/performance references only when those risks are actually affected
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

### 5.3 — Affected-Area Coverage Evidence

```
□ Identify the project areas actually affected by this change.
□ For each affected area, record:
  - done → evidence (check result, path, or diff)
  - deferred → follow-up task/decision
  - not applicable → only when an area was considered but genuinely does not apply

□ Do not require fixed Database/Domain/API/Frontend/UI layers unless the project/profile declares them.
□ If full-stack vertical-slice guidance is activated, its dynamic coverage table may be used.
```

### 5.4 — Quality Gate Decision

```
□ All tests pass (or NOT_AVAILABLE with justification):
  → ✅ GATE PASSED

□ Any test failure without a fix:
  → ⛔ GATE FAILED — return to stage 4 for fixes

□ Materially affected area has no verification/evidence:
  → ⛔ GATE FAILED — complete verification before proceeding
```

---

## Context Expansion (selective)

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
  affected_area_evidence: complete | incomplete
  next_stage: 6 | done              # 6 if 🔴, done if 🟢/🟡
  blockers: []
```

> After gate passes → for 🟢/🟡 the pipeline is DONE. For 🔴 continue to stage 6.
