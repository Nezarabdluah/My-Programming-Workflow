# 📱 Mobile QA Orchestrator — Coordinator

> Skill for ensuring the quality of React Native / Expo applications.
> Path: `.agent/03-workflows/mobile-qa/`
> Pattern: coordinator + split steps (like security-gate)

---

## ⚠️ Mandatory Resource Injection (before starting QA) — MUST, gate blocked without it
0. Read `05-references/books/00-master-index.md` Stage 5 → load every MUST resource listed there
1. Read `01-core/wiring-registry.md` → find Testing / QA capability rows
2. Load `05-references/books/constitutions/security-constitution.md` — XSS, input validation
3. Load `05-references/books/constitutions/perf-constitution.md` — network payload, blind guessing ban
4. Load `02-rules/testing-and-quality.md` → cite REF-TEST-* contracts as `// [REF-TEST-X]`
5. Grep `05-references/qa-testing/qa-testing-strategy-and-automation.md` for relevant `[QA-*]` anchors
6. Cite constitutions as `// [CONST-XXX-N]` and produce a 1-line Resource Utilization Summary before Done

---

## Invocation

When a mobile app QA check is requested, read this file first, then execute the steps.

User inputs:
- **Test scenario** — mandatory
- **Mode** (optional): `quick` | `risk` | `release`
- **Platform** (optional): `ios` | `android` | `both`
- **Extra details** (optional): account, build, environment

---

## Automatic Mode Selection

If the user did not specify a mode:
- **`quick`** ← ordinary scenarios (view, navigate, search)
- **`risk`** ← any scenario touching: auth, payments, permissions, personal data, deletion

---

## Steps

```
┌──────────────────────────┬───────┬──────┬─────────┐
│ Step                     │ quick │ risk │ release │
├──────────────────────────┼───────┼──────┼─────────┤
│ 1. Environment discovery │  ✅   │  ✅  │   ✅    │
│ 2. Build verification    │  ✅   │  ✅  │   ✅    │
│ 3. Scenario execution    │  ✅   │  ✅  │   ✅    │
│ 4. Report                │  ✅   │  ✅  │   ✅    │
└──────────────────────────┴───────┴──────┴─────────┘
```

> Advanced checks (risk-exploration, security-privacy, performance-network)
> will be added as separate steps later. Currently they run within Step 3 as far as available tools allow.

1. `step-1-environment-discovery.md` — framework, tools, and emulator discovery
2. `step-2-build-verification.md` — build and run verification
3. `step-3-scenario-execution.md` — scenario execution and conditional checks
4. `step-7-evidence-report.md` — final report

---

## Decision Gate — applied before every step

```yaml
# Before moving to any step — verify:
gate:
  previous_step_status: passed | failed | blocked  # what is the previous step's state?
  blockers_exist: true | false                      # is anything blocking progress?
  tools_required: []                                # what tools are required?
  tools_available: []                               # what is actually available?
  decision: proceed | skip | block                  # the decision

# Decisions:
#   proceed → next step
#   skip    → record SKIPPED with the reason and move on
#   block   → record BLOCKED and stop the run entirely
```

---

## Issue Classifications — 8 categories

| Classification | Meaning |
|----------------|---------|
| `PRODUCT_DEFECT` | defect in product logic or UI |
| `AUTOMATION_DEFECT` | defect in the test script or a flaky selector |
| `ENVIRONMENT_DEFECT` | environment problem (emulator, build, local network) |
| `TEST_DATA_DEFECT` | missing test data or unprepared account |
| `PERFORMANCE_DEFECT` | slowness, freeze, or resource consumption |
| `SECURITY_DEFECT` | data exposure or insecure storage |
| `UX_DEFECT` | works, but the experience is poor |
| `REQUIREMENT_GAP` | unspecified behavior — needs a product decision |

## Severity Levels — 4 levels

| Severity | Criterion |
|----------|-----------|
| `P0` | crash, data loss, security vulnerability, blocked critical path |
| `P1` | a main workflow fails |
| `P2` | important but a workaround exists |
| `P3` | cosmetic, minor UX, low risk |

---

## Coverage States

| State | Meaning |
|-------|---------|
| `EXECUTED` | the check actually ran via a tool or manually |
| `SKIPPED` | intentional skip — the mode does not require it |
| `NOT_AVAILABLE` | the check is required but the tool/capability is unavailable |
| `BLOCKED` | the check is required but a problem prevents running it |

---

## Optional Tools

| Tool | Purpose | How to detect |
|------|---------|---------------|
| **Maestro** | automated E2E flows | `maestro --version` + presence of `.maestro/` |
| **Detox** | automated E2E tests | `.detoxrc.*` or `detox` in package.json |
| **Appium** | advanced cross-device automation | `wdio.conf.*` |
| **Jest** | unit tests | `jest.config.*` or `jest` in package.json |
| **adb** | Android emulator control | `adb version` |
| **xcrun simctl** | iOS simulator control | `xcrun simctl list` (macOS only) |
| **EAS CLI** | cloud Expo builds | `eas --version` |

> If a tool is unavailable ← record `NOT_AVAILABLE` — never guess its results.

---

## Handoff Contract — embedded

```yaml
run:
  scenario: ""
  mode: quick|risk|release
  platform: ""
  build: ""
  status: running|passed|failed|blocked|partial

environment: {}    # filled in step 1
build: {}          # filled in step 2
scenario: {}       # filled in step 3
issues: []         # accumulated from all steps
evidence: []       # accumulated from all steps
coverage: {}       # filled in step 4 (the report)
next_action: ""
```

---

## Safety Rules

- ❌ Never modify app code, dependencies, or settings — except on explicit request
- ❌ Never expose real credentials, tokens, or personal data
- ❌ Never wipe databases or shared environments without explicit permission
- ⚠️ Retry twice only — and only for transient errors
- ⚠️ Never conflate environment failure with product defect
- ⚠️ Never claim a check result without an actual tool — record `NOT_AVAILABLE`

---

## Memory Note

> Do not update `project-context.md` after every QA run.
> Update it only when the skill's own structure changes or new steps are added.
> Check results are recorded in the report only (step 4).

---

Start step 1 now.
