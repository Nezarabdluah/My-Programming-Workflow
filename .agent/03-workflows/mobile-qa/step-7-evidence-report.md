# Mobile QA — Step 4: Evidence Report

> This is step 4 of 4 (the last). Previous: `step-3-scenario-execution.md`
> Always executed in every mode.
> (numbered step-7 in the filesystem for compatibility with future steps)

---

## Decision Gate

```yaml
gate:
  previous_step: step-3 (scenario-execution)
  previous_status: any (passed|failed|blocked|partial)
  requires: nothing — the report is always produced
  decision: proceed — gather all results and issue the report
```

---

## Task: produce the final report

### Template:

```markdown
# 📱 Mobile QA Report

**Date**: [today's date]
**Scenario**: [one-sentence description]
**Mode**: quick | risk | release
**Platform**: iOS | Android | both
**Framework**: React Native CLI | Expo Managed | Expo Bare
**Execution type**: full (device + code) | static-only (code) | manual

---

## Result: ✅ PASSED | ❌ FAILED | 🚫 BLOCKED | 🟡 PARTIAL

[one sentence summarizing the result]

---

## Discovered Environment

| Item | Value |
|------|-------|
| Framework | [framework] |
| Version | [rn_version] |
| Package manager | [package_manager] |
| E2E tool | [detox/maestro/NOT_AVAILABLE] |
| Emulator/device | [description or NOT_AVAILABLE] |

---

## Verified Steps

| # | Action | Expected | Actual | Type | Status |
|---|--------|----------|--------|------|--------|
| 1 | [action] | [expected] | [actual] | static/runtime | ✅/❌ |

---

## Discovered Issues

| # | Title | Classification | Severity | Evidence | Likely cause |
|---|-------|----------------|----------|----------|--------------|
| ISS-001 | [description] | [one of 8 classifications] | P0-P3 | [link/description] | [cause] |

### Classifications (8 categories):
| Classification | Meaning |
|----------------|---------|
| `PRODUCT_DEFECT` | defect in product logic or UI |
| `AUTOMATION_DEFECT` | defect in the test script/selector |
| `ENVIRONMENT_DEFECT` | environment problem (emulator, build, network) |
| `TEST_DATA_DEFECT` | missing test data |
| `PERFORMANCE_DEFECT` | slowness or freezing |
| `SECURITY_DEFECT` | data exposure or insecure storage |
| `UX_DEFECT` | works, but the experience is poor |
| `REQUIREMENT_GAP` | behavior unspecified in requirements |

---

## Coverage

| Check | State | Notes |
|-------|-------|-------|
| Core scenario (runtime) | EXECUTED / NOT_AVAILABLE | [note] |
| Static code check | EXECUTED / SKIPPED | [note] |
| Invalid input | EXECUTED / SKIPPED / NOT_AVAILABLE | [note] |
| Back button | EXECUTED / SKIPPED / NOT_AVAILABLE | [note] |
| Double-tap | EXECUTED / SKIPPED / NOT_AVAILABLE | [note] |
| Security check (static) | EXECUTED / SKIPPED | [note] |
| Security check (runtime) | EXECUTED / SKIPPED / NOT_AVAILABLE | [note] |
| Permissions audit | EXECUTED / SKIPPED | [note] |
| Offline | EXECUTED / SKIPPED / NOT_AVAILABLE | [note] |
| Performance (cold start) | EXECUTED / SKIPPED / NOT_AVAILABLE | [note] |
| CI tests | EXECUTED / SKIPPED / NOT_AVAILABLE | [note] |
| TypeScript | EXECUTED / SKIPPED / NOT_AVAILABLE | [note] |
| Lint | EXECUTED / SKIPPED / NOT_AVAILABLE | [note] |

### Coverage states:
- `EXECUTED` — the check actually ran via a tool or manually
- `SKIPPED` — intentional skip (the mode does not require it)
- `NOT_AVAILABLE` — the check is required but the tool/capability is unavailable
- `BLOCKED` — the check is required but a problem prevents running it

---

## Evidence

| # | Type | Description | Step |
|---|------|-------------|------|
| 1 | screenshot/log/video/test_output | [description] | [#] |

---

## Next Action

> [one clear, actionable recommendation]
> Example: "Fix ISS-001 (P0 crash), then re-test the login flow"

---

## Health Score (release mode only)

> Method source: `.agent/05-references/qa-testing/` — Health Score Formula
> Adapted for mobile: weights reflect platform priorities.
> ⚠️ computed only in release mode. In quick/risk → record "N/A — not release mode".

| Dimension | Weight | Score (0-10) | Method |
|-----------|--------|--------------|--------|
| Core scenario | 30% | (passed steps / total × 10) | runtime + static |
| Static security check | 20% | (0 issues = 10, -2 per issue) | static code scan |
| Universal Triggers | 20% | (passed checks / total × 10) | runtime |
| CI tests | 15% | (passed tests / total × 10) | jest/detox/maestro |
| Performance & network | 15% | (cold start + offline acceptable = 10) | runtime |

```
90-100 🟢 excellent — ready to release
70-89  🟡 good     — release with monitoring
50-69  🟠 fair     — fix before the next feature
0-49   🔴 poor     — do not release
```

> ⚠️ If any dimension = NOT_AVAILABLE → do not score it.
> Compute the percentage from the available dimensions only. Record how many dimensions were scored.

---

## Report Rules

```
Strict rules — no exceptions:

  ❌ never record PASSED without actual verification of the final outcome
  ❌ never leave "Actual" empty — write exactly what happened
  ❌ never conflate ENVIRONMENT_DEFECT with PRODUCT_DEFECT
  ❌ never record EXECUTED for a check you had no tool to run — record NOT_AVAILABLE
  ❌ never record SKIPPED for a required check whose tool was unavailable — that is NOT_AVAILABLE

  ✅ every issue: classification (8 categories) + severity (P0-P3) + evidence
  ✅ every coverage item: a clear state with a note
  ✅ distinguish what is static and what is runtime
  ✅ the next action: specific and actionable

Evidence rules:
  - Screenshots: on failure + the final result only
  - Logs: on console errors or crashes
  - Video: for issues hard to describe in text
  - ❌ no unnecessary evidence
```

---

## After the Report

```
1. ✅ PASSED   → the report is the final output
2. ❌ FAILED   → order the fixes: P0 first
3. 🚫 BLOCKED  → explain what blocks testing and what the user must provide
4. 🟡 PARTIAL  → explain what passed, what was untested, and why

⚠️ Do not update project-context.md — QA results stay in the report only.
```

---

## Linked AOS Sources

> This skill draws on existing AOS knowledge. Refer to it when needed:

| Source | What it provides | When to consult |
|--------|------------------|-----------------|
| [qa-testing-strategy-and-automation.md](file:///c:/Users/farha/Downloads/New%20folder/ANLASH-dde0788aa999cb717ea6a0fa477b26ca26d2d0eb/.agent/05-references/qa-testing/qa-testing-strategy-and-automation.md) | Feature DNA + Universal Triggers + Health Score + Documentation Protocol | analyzing a complex feature or building a test plan |
| [testing-and-quality.md](file:///c:/Users/farha/Downloads/New%20folder/ANLASH-dde0788aa999cb717ea6a0fa477b26ca26d2d0eb/.agent/02-rules/testing-and-quality.md) | AAA rules + Resilience + Pre-delivery checklist | assessing test quality or offline behavior |
| [security-checklist.md](file:///c:/Users/farha/Downloads/New%20folder/ANLASH-dde0788aa999cb717ea6a0fa477b26ca26d2d0eb/.agent/02-rules/security-checklist.md) | JWT + IDOR + XSS + Boundary Validation | the static security check |
| [network-and-api.md](file:///c:/Users/farha/Downloads/New%20folder/ANLASH-dde0788aa999cb717ea6a0fa477b26ca26d2d0eb/.agent/02-rules/network-and-api.md) | evidence-based diagnosis — never guess | performance assessment |
