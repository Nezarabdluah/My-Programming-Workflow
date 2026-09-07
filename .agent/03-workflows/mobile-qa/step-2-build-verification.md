# Mobile QA — Step 2: Build Verification

> This is step 2 of 4. Previous: `step-1-environment-discovery.md` | Next: `step-3-scenario-execution.md`

---

## Decision Gate

```yaml
gate:
  previous_step: step-1 (environment-discovery)
  previous_status: must be passed (framework + platform identified)
  requires:
    - environment.framework ≠ ""
    - environment.package_manager ≠ ""
  tools_required:
    - package_manager CLI (npm|yarn|pnpm|bun)
    - an emulator or connected device (optional — detected)
  decision:
    previous_passed: proceed
    previous_blocked: block — never attempt a build
```

---

## Task: verify build and run before testing

### 2.1 — Install dependencies

```
□ Run the install command:
  npm  → npm install
  yarn → yarn install
  pnpm → pnpm install
  bun  → bun install

□ Result:
  ✅ zero errors                → dependencies_installed: true
  ⚠️ warnings (peer deps...)   → dependencies_installed: true + record the warnings
  ❌ errors blocking install    → ENVIRONMENT_DEFECT → BLOCKED
```

### 2.2 — Native dependencies (conditional)

```
□ Only if framework ≠ expo-managed:

  iOS (if platform = ios|both + simctl available):
    - cd ios && pod install
    - ✅ success → native_ios: synced
    - ❌ failure → record the error — may block iOS only, not everything

  Android (if platform = android|both):
    - verify local.properties exists
    - verify ANDROID_HOME / ANDROID_SDK_ROOT
    - ❌ missing → record a warning (not necessarily a blocker)

□ If framework = expo-managed:
  - no native dependencies — skip this sub-step
```

### 2.3 — Build the app

```
□ According to framework and available tools (from step 1):

  ┌─ expo-managed ──────────────────────────────────┐
  │ npx expo start (verify Metro starts w/o errors) │
  │ or: npx expo run:android / npx expo run:ios     │
  │ or: eas build (if eas is available)             │
  └─────────────────────────────────────────────────┘

  ┌─ react-native-cli ─────────────────────────────┐
  │ Android: npx react-native run-android           │
  │ iOS:     npx react-native run-ios               │
  └─────────────────────────────────────────────────┘

  ┌─ expo-bare ────────────────────────────────────┐
  │ npx expo run:android / npx expo run:ios         │
  └─────────────────────────────────────────────────┘

□ Classify build errors:
  Gradle/Xcode error     → ENVIRONMENT_DEFECT (environment not set up)
  Metro bundler crash    → may be PRODUCT_DEFECT (bad code)
  TS/Babel compile error → PRODUCT_DEFECT (code error)
  SDK version mismatch   → ENVIRONMENT_DEFECT

□ If neither emulator nor device exists:
  - try Metro only (npx expo start / npx react-native start)
  - if Metro starts without errors → build: partial (Metro OK, no device)
  - record: "cannot verify on-device run — NOT_AVAILABLE"
```

### 2.4 — Run verification (conditional)

```
□ Only if an emulator or device is available:

  - Does the first screen appear?
  - Is Metro/Bundler connected?
  - Is there a Red Screen or Yellow Box?
  - Record:
    app_launches: true|false
    initial_screen: "description of what appears"
    red_screen: true|false
    console_errors: [any errors]

□ If no emulator and no device:
  - app_launches: NOT_AVAILABLE
  - record the reason and continue
  - ⚠️ this affects step 3 (scenario execution)
```

---

## Outputs

```yaml
build:
  dependencies_installed: true|false
  native_deps:
    ios: synced|failed|skipped|NOT_AVAILABLE
    android: synced|failed|skipped|NOT_AVAILABLE
  build_success: true|false|partial
  build_errors: []
  build_method: "metro-only|full-build|eas"
  app_launches: true|false|NOT_AVAILABLE
  initial_screen: ""
  red_screen: false
  console_errors: []
  blockers: []
```

---

## Decision Gate for the Next Step

```yaml
gate:
  # Step 3 needs:
  requires:
    - dependencies_installed = true
    - build_success ≠ false (true or partial is acceptable)
  affects_step_3:
    app_launches = NOT_AVAILABLE:
      → step 3 will be limited (static code checks only)
      → record in the report: "runtime testing: NOT_AVAILABLE"
    app_launches = true:
      → step 3 is full (code checks + runtime)
  decision:
    deps_ok + build_ok: proceed → step-3
    deps_failed: block
    build_failed: block (with error details)
    build_partial: proceed → step-3 (with constraints)
```
