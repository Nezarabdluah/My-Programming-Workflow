# QA Strategy — Testing Approach & Automation Guide

> Standalone workflow for defining and executing a QA strategy.
> Referenced by: master-pipeline stage 5 (Testing & Quality Gate)
> Related references: `05-references/qa-testing/` (grep-only)

---

## Purpose

This workflow guides the agent in establishing a testing strategy appropriate to the project's classification, stack, and maturity level. It bridges the gap between the abstract test pyramid and concrete, executable test plans.

---

## 1. Test Strategy Selection

Based on project classification, select the testing depth:

```
┌─────────────────────────────────┬───────┬──────┬──────────┐
│ Testing Activity                │  🟢   │  🟡  │    🔴    │
├─────────────────────────────────┼───────┼──────┼──────────┤
│ Unit tests (critical paths)     │  ✅   │  ✅  │   ✅     │
│ Unit tests (comprehensive)     │  —    │  ✅  │   ✅     │
│ Integration tests              │  —    │  ✅  │   ✅     │
│ E2E / smoke tests              │  —    │  —   │   ✅     │
│ Performance / load tests       │  —    │  —   │   ✅     │
│ Security / penetration tests   │  —    │  —   │   ✅     │
│ Accessibility tests            │  —    │  —   │   ✅     │
└─────────────────────────────────┴───────┴──────┴──────────┘
```

---

## 2. Test Pyramid (grep [QA-PYRAMID] for details)

```
          ┌─────────┐
          │  E2E /  │  ← few, slow, high confidence
          │  Smoke  │
         ┌┴─────────┴┐
         │Integration │  ← moderate, test boundaries
        ┌┴────────────┴┐
        │  Unit Tests   │  ← many, fast, isolated
        └───────────────┘
```

### Principles:
- **Test behavior, not implementation** (REF-TEST-BEHAV)
- **Mock only external boundaries** (REF-TEST-MOCK)
- **Each test must be independent and repeatable**
- **Test names describe the expected behavior in plain language**

---

## 3. Test Infrastructure Discovery

```
□ Scan the project for existing test infrastructure:
  - Test runner: Jest, pytest, xUnit, NUnit, MSTest, etc.
  - Test directory structure: __tests__/, tests/, *.test.*, *.spec.*
  - Coverage tools: Istanbul, coverage.py, Coverlet
  - CI integration: GitHub Actions, Azure DevOps, etc.
  - E2E framework: Playwright, Cypress, Maestro, Detox

□ Record findings in 04-memory/project-knowledge.md
□ If no test infrastructure exists:
  - Recommend a stack-appropriate setup
  - ⛔ NEEDS CLARIFICATION — ask the developer before adding test dependencies
```

---

## 4. Test Plan Template

For each feature or increment, produce:

```markdown
### Test Plan: [Feature Name]

**Scope**: [what is being tested]
**Classification**: 🟢 | 🟡 | 🔴
**Test runner**: [tool]

#### Unit Tests
| Test ID | Description | Input | Expected Output | Status |
|---------|-------------|-------|-----------------|--------|

#### Integration Tests (🟡 🔴 only)
| Test ID | Description | Components | Expected Behavior | Status |

#### E2E Tests (🔴 only)
| Test ID | User Flow | Steps | Expected Result | Status |
```

---

## 5. QA Reference Anchors (grep-only)

Use these anchors to query `05-references/qa-testing/qa-testing-strategy-and-automation.md`:

| Anchor | Topic |
|--------|-------|
| `[QA-DETECTIVE]` | Investigation methodology |
| `[QA-HARDRULES]` | Non-negotiable testing rules |
| `[QA-INVESTIGATION]` | Root-cause analysis techniques |
| `[QA-QUESTIONS]` | Questions to ask before testing |
| `[QA-PYRAMID]` | Test pyramid strategy |
| `[QA-L0-LOGIC]` | Logic-layer testing |
| `[QA-E2E-SMOKE]` | E2E and smoke testing |
| `[QA-API-NEWMAN]` | API testing with Newman |
| `[QA-UNIT]` | Unit testing best practices |
| `[QA-CHECKLISTS]` | Pre-delivery checklists |
| `[QA-DOC]` | Test documentation |

---

## 6. Quality Gate Criteria

A quality gate passes when:

| Criterion | 🟢 | 🟡 | 🔴 |
|-----------|-----|-----|-----|
| Critical-path unit tests pass | ✅ | ✅ | ✅ |
| All unit tests pass | — | ✅ | ✅ |
| Integration tests pass | — | ✅ | ✅ |
| E2E smoke tests pass | — | — | ✅ |
| No P0/P1 open issues | ✅ | ✅ | ✅ |
| Coverage report complete | — | ✅ | ✅ |
| Vertical-slice coverage table | — | ✅ | ✅ |
