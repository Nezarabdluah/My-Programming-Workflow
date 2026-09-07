# Mobile QA — Step 1: Environment Discovery

> This is step 1 of 4. Next: `step-2-build-verification.md`

---

## Decision Gate

```yaml
gate:
  previous_step: none              # this is the first step
  requires:
    - an existing React Native or Expo project (package.json)
  tools_required: none             # file reading only
  decision: proceed
```

> If `package.json` is missing or contains neither `react-native` nor `expo` ← `BLOCKED` immediately.

---

## Task: discover the project environment automatically — file reading only

### 1.1 — Framework identification

```
□ Read package.json → dependencies + devDependencies:

  "expo" present + no native android/ios folders
    → framework: expo-managed

  "expo" + "react-native" + android/ or ios/ folders
    → framework: expo-bare

  "react-native" without "expo"
    → framework: react-native-cli

  Neither "react-native" nor "expo"
    → BLOCKED — this is not a React Native/Expo project

□ Record versions:
  - react-native: (from package.json)
  - expo SDK: (from package.json → "expo" version)
```

### 1.2 — Package manager

```
□ Identify from the existing lockfile:
  yarn.lock           → yarn
  pnpm-lock.yaml      → pnpm
  package-lock.json   → npm
  bun.lockb           → bun
  no lockfile         → npm (default) + record a warning
```

### 1.3 — Available scripts

```
□ Read scripts from package.json — record:
  start:   (run command)
  build:   (build command)
  test:    (test command)
  lint:    (lint command)
  any custom scripts (e2e, detox, maestro...)
```

### 1.4 — Platform & identifier

```
□ Identify supported platforms:
  ios/ present       → iOS supported
  android/ present   → Android supported
  Expo managed       → tool-dependent (Expo Go / EAS)

□ App identifier:
  iOS:     ios/*/Info.plist → CFBundleIdentifier
  Android: android/app/build.gradle → applicationId
  Expo:    app.json → slug, ios.bundleIdentifier, android.package

  If not found → record "unspecified" and continue
```

### 1.5 — Discover available testing tools

> ⚠️ Discovery only — do not execute any tool here. Record what is available and what is not.

```
□ Unit test frameworks:
  jest.config.* or "jest" in package.json    → unit: jest
  vitest in package.json                     → unit: vitest
  nothing                                    → unit: NOT_AVAILABLE

□ E2E test frameworks:
  .detoxrc.* or "detox" in package.json      → e2e: detox
  .maestro/ or maestro/ folder               → e2e: maestro
  wdio.conf.*                                → e2e: appium
  nothing                                    → e2e: NOT_AVAILABLE

□ Device/emulator tools (verify actual availability):
  adb version           → adb: available | NOT_AVAILABLE
  xcrun simctl list     → simctl: available | NOT_AVAILABLE (macOS only)
  eas --version         → eas: available | NOT_AVAILABLE
  maestro --version     → maestro_cli: available | NOT_AVAILABLE

□ For every unavailable tool:
  - record NOT_AVAILABLE — never assume it exists
  - never try to install it — just record
```

### 1.6 — Emulators & devices

```
□ Only if tools are available from 1.5:

  adb available:
    → run: adb devices
    → run: emulator -list-avds (if present)
    → record connected devices / available emulators

  simctl available:
    → run: xcrun simctl list devices available
    → record available simulators

  neither adb nor simctl:
    → record: emulators: NOT_AVAILABLE
    → this is not necessarily a blocker — testing may run on a physical device
    → ask the user: "Do you have a connected device or another way to run the app?"
```

---

## Outputs

```yaml
environment:
  framework: expo-managed | expo-bare | react-native-cli
  rn_version: ""
  expo_sdk: ""
  package_manager: npm | yarn | pnpm | bun
  platform: ios | android | both
  app_identifier: ""
  scripts:
    start: ""
    build: ""
    test: ""
    lint: ""
  tools:
    unit: jest | vitest | NOT_AVAILABLE
    e2e: detox | maestro | appium | NOT_AVAILABLE
    adb: available | NOT_AVAILABLE
    simctl: available | NOT_AVAILABLE
    eas: available | NOT_AVAILABLE
    maestro_cli: available | NOT_AVAILABLE
  emulators:
    android: []      # or NOT_AVAILABLE
    ios: []          # or NOT_AVAILABLE
  blockers: []
```

---

## Decision Gate for the Next Step

```yaml
gate:
  # Step 2 needs:
  requires:
    - framework identified (not empty)
    - package_manager identified
    - at least one supported platform
  nice_to_have:
    - an emulator or device available
    - an E2E test framework available
  decision:
    all_requires_met: proceed → step-2
    framework_unknown: block
    no_platform: block
```
