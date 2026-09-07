# Mobile QA — Step 3: Scenario Execution

> This is step 3 of 4. Previous: `step-2-build-verification.md` | Next: `step-7-evidence-report.md`

---

## Decision Gate

```yaml
gate:
  previous_step: step-2 (build-verification)
  previous_status: must be passed or partial
  requires:
    - dependencies_installed = true
    - build_success = true | partial
  capabilities:
    device_available: true|false   # from steps 1+2
    e2e_tool: detox|maestro|none   # from step 1
  decision:
    device + e2e_tool:    → full execution (automation + runtime verification)
    device + no e2e_tool: → manual/interactive execution
    no device + code:     → static analysis only
    no device + no code:  → BLOCKED
```

> ⚠️ Critical separation: **static checking (code)** is different from **runtime checking (device)**.
> Never conflate them. Record clearly which type was executed.

---

## Task: turn the scenario into explicit steps and execute them

### 3.1 — Scenario analysis

```
□ Break the user's request into:
  - Goal: what must be true at the end
  - Preconditions: what must be ready
  - Steps: the sequence of actions
  - Expected outcome: what is verified

□ Record the steps:
  | # | Action | Expected | Type | Status |
  |---|--------|----------|------|--------|
  | 1 | [action] | [outcome] | static|runtime | ⏳ |
```

### 3.1b — Feature DNA for mobile (risk + release modes)

> Method source: `.agent/05-references/qa-testing/` — Feature DNA (8 dimensions)
> Adapted for mobile: the INTERFACE and EXTERNAL dimensions expand to include platform traits.

```
□ For each feature in the scenario — ask the eight dimensions:
  Every ✅ generates additional checks. Every ❌ is dropped.

  | Dimension | Question (mobile-adapted) | If ✅ — check |
  |-----------|---------------------------|---------------|
  | DATA | does it read/write data? | 0 records / corrupt data / sensitive / stored locally |
  | TIME | does it involve timing or real-time? | before/after deadline / push notification timing |
  | USERS | how many users interact? | isolation / conflict / different roles |
  | EXTERNAL | does it call an API or service? | success / failure / slow / offline |
  | STATE | does it have states? | allowed + forbidden transitions / persistence across sessions |
  | MEDIA | does it handle camera/images/files? | permissions / size / extension / corrupt file |
  | COMPUTATION | does it compute anything? | precision / overflow / division by zero |
  | INTERFACE | mobile-specific interaction? | gestures / orientation / keyboard / deep links |

□ Record the result:
  active dimensions: [list of ✅ dimensions]
  generated checks: [count]
  ⚠️ never generate checks for ❌ dimensions
```

### 3.2 — Static checking (always available)

> This checks the source code by reading it — needs no device or emulator.

```
□ Code-path analysis (Detective Mode — from the QA reference):
  > "Never test without understanding. The code is the only truth."
  - Identify the files involved in the scenario (screens, components, services)
  - Trace the data flow (API calls, state management)
  - Verify error handling exists
  - Identify the navigation flow (stack, tab, drawer)
  - Identify state management (Redux, Zustand, Context, MobX)

□ Static security check (risk + release modes):
  > source: `.agent/02-rules/security-checklist.md`

  Insecure storage:
  - search for: AsyncStorage.setItem storing tokens/passwords
  - search for: MMKV without encryption for sensitive data
  - ✅ safe: expo-secure-store / react-native-keychain / EncryptedStorage

  Data exposure:
  - search for: console.log printing tokens, passwords, or personal data
  - search for: hardcoded API keys or secrets (they will NOT be hidden in the JS bundle)

  Network:
  - search for: http:// (without s) in network requests
  - iOS: inspect Info.plist → NSAllowsArbitraryLoads (must be false)
  - Android: inspect network_security_config → cleartextTrafficPermitted

  IDOR (from security-checklist — double-boundary validation):
  - search API calls: is a user ID passed from the client instead of being extracted from the token?
  - search for: fetch(`/api/users/${userId}`) where userId comes from state, not the server
  - ⚠️ this is a code grep — not a runtime check

  - record every result clearly: "static code scan — not runtime verification"

□ Permissions check (release mode):
  - iOS: read Info.plist → every NSxxxUsageDescription — justified and clearly written?
  - Android: read AndroidManifest.xml → <uses-permission> — justified?
  - Expo: read app.json → plugins/permissions — all necessary?
  - record: "static permissions audit — from manifest/config files"
```

### 3.3 — Runtime checking (only if a device/emulator is available)

> ⚠️ Never execute this section if `device_available = false`. Record `NOT_AVAILABLE`.

```
□ Selector rules:
  1. ✅ testID / accessibilityLabel — most stable
  2. ✅ visible text (text content) — acceptable if unique
  3. ⚠️ accessibility role + name — acceptable fallback
  4. ❌ coordinates (x, y) — forbidden except as a last resort, documented

□ Verification after every action:
  - Did the expected screen appear?
  - Is the required element present?
  - Is the data correct?
  - Are there no console errors?

□ Waiting:
  - waitFor instead of sleep — always
  - limit: 10s normal, 30s for network
  - timeout = failure (never extend the timeout)

□ If an E2E tool is available (Maestro/Detox):
  - use it to run the steps automatically
  - record: "automated via [tool name]"

□ If no E2E tool:
  - execute manually/interactively on the emulator
  - record: "manual/interactive execution"
```

### 3.4 — Mode-conditional checks

```
□ quick mode:
  → the core scenario only — no extra checks

□ risk mode (in addition to quick):
  The following checks run only if the tool/capability is available:

  Invalid input (needs: device):
    □ empty, too long, special characters, Arabic, emoji
    → device_available? → execute | record NOT_AVAILABLE

  Back button (needs: device):
    □ during a form (does it warn about data loss?)
    □ after a successful operation
    □ from a modal/bottom sheet
    → device_available? → execute | record NOT_AVAILABLE

  Double-tap (needs: device):
    □ submit button (does it create two records?)
    □ navigation button (does it open two screens?)
    → device_available? → execute | record NOT_AVAILABLE
```

### 3.4b — Mobile Universal Triggers (risk + release modes)

> Method source: `.agent/05-references/qa-testing/` — Universal Triggers
> Adapted for mobile: filtered to common React Native patterns.
> Apply only the patterns present in the tested feature — never check what does not exist.

```
□ If a FORM exists in the feature (needs: device):
  □ required fields empty → error message?
  □ do errors appear all at once or one by one?
  □ does data persist after an API error?
  □ does the keyboard hide fields? (KeyboardAvoidingView)
  □ auto-scroll to the invalid field?
  □ does copy-paste work?
  → device_available? → execute | record NOT_AVAILABLE

□ If a LIST exists in the feature (needs: device):
  □ 0 items → clear empty state?
  □ smooth scrolling with 50+ items? (FlatList, not ScrollView)
  □ pull-to-refresh works?
  □ pagination / infinite scroll?
  → device_available? → execute | record NOT_AVAILABLE

□ If SEARCH/FILTER exists (needs: device):
  □ partial search works?
  □ Arabic search works?
  □ debounce (not a request per keystroke)?
  □ clearing the filter restores all results?
  □ no results → clear message?
  → device_available? → execute | record NOT_AVAILABLE

□ If PERMISSIONS exist (camera, location, notifications):
  □ permission denied → handled gracefully?
  □ explanation shown before requesting?
  □ redirect to settings if previously denied?
  → device_available? → execute | record NOT_AVAILABLE

□ If NOTIFICATIONS exist (push/in-app):
  □ notification appears at the right time?
  □ tapping it opens the correct screen? (deep link)
  □ app in background → does the notification arrive?
  → device_available? → execute | record NOT_AVAILABLE

⚠️ Never check a trigger absent from the feature — record SKIPPED.
```

```
□ release mode (in addition to risk):

  Offline state (needs: device + adb/simctl):
    > source: `.agent/02-rules/testing-and-quality.md` — Resilience
    □ airplane mode → clear error shown?
    □ previously stored data remains available? (graceful degradation)
    □ reconnection → does it resume work automatically?
    □ is there a proper timeout (never waits forever)?
    → adb/simctl available? → execute | record NOT_AVAILABLE

  App startup performance (needs: device):
    □ cold start < 2s excellent / 2-4s acceptable / > 4s a problem
    □ smooth splash screen (no white flash)?
    → device_available? → measure | record NOT_AVAILABLE

  Screen rotation (needs: device):
    □ does the UI adapt without losing form data?
    □ does the scroll position persist?
    → device_available? → execute | record NOT_AVAILABLE

  CI tests (needs: a test tool):
    □ jest --ci / detox test / maestro test
    → tool available? → run | record NOT_AVAILABLE

  TypeScript/Lint check (always available — needs no device):
    □ npx tsc --noEmit
    □ npx eslint . (if configured)
    → always execute
```

### 3.5 — Failure Handling

```
□ When a step fails:
  1. Capture a screenshot immediately (if a device is available)
  2. Record the exact error
  3. Classify: transient or permanent?

  Transient (timeout, slow loading):
    → retry 1 → retry 2 → final failure

  Permanent (missing element, crash, logic error):
    → no retry — immediate failure
    → decide: can the rest of the scenario continue?

□ Failure classification — 8 categories:
  missing/wrong UI        → PRODUCT_DEFECT or UX_DEFECT
  wrong data              → PRODUCT_DEFECT
  crash / red screen      → PRODUCT_DEFECT (P0)
  emulator/environment    → ENVIRONMENT_DEFECT
  missing test data       → TEST_DATA_DEFECT
  flaky selector          → AUTOMATION_DEFECT
  clear slowness          → PERFORMANCE_DEFECT
  unspecified behavior    → REQUIREMENT_GAP
```

### 3.6 — Final Outcome Verification

```
□ Runtime verification (if a device is available):
  - does the final state match the expectation on screen?
  - is the data actually saved/updated?
  - are there no unexpected side effects?

□ Static verification (always):
  - does the code flow match the required scenario?
  - is error handling present in the critical path?

⚠️ Strict rules:
  - never record PASSED without actual verification
  - if verification is runtime-only and no device is available → PARTIAL (not PASSED)
  - state exactly what was verified (static/runtime)
```

---

## Outputs

```yaml
scenario:
  description: ""
  preconditions: []
  execution_type: full|static-only|manual
  steps:
    - id: 1
      action: ""
      expected: ""
      actual: ""
      check_type: static|runtime|both
      status: passed|failed|skipped|NOT_AVAILABLE
      evidence: ""
      retry_count: 0
  conditional_checks:
    invalid_input: passed|failed|SKIPPED|NOT_AVAILABLE
    back_navigation: passed|failed|SKIPPED|NOT_AVAILABLE
    duplicate_tap: passed|failed|SKIPPED|NOT_AVAILABLE
    offline: passed|failed|SKIPPED|NOT_AVAILABLE
    cold_start_ms: 0|NOT_AVAILABLE
    ci_tests: passed|failed|SKIPPED|NOT_AVAILABLE
    typescript: passed|failed|NOT_AVAILABLE
    lint: passed|failed|NOT_AVAILABLE
    static_security: passed|failed|SKIPPED
    permissions_audit: passed|failed|SKIPPED
  final_result:
    expected: ""
    actual: ""
    verified_by: static|runtime|both|none
  status: passed|failed|blocked|partial
```

---

## Decision Gate for the Next Step

```yaml
gate:
  # Step 4 (the report) always runs
  decision: proceed → step-7-evidence-report
  carry_forward:
    - every discovered issue
    - every collected piece of evidence
    - NOT_AVAILABLE states (recorded in coverage)
```
