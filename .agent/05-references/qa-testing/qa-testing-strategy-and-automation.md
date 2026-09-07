# SKILL: QA Master Engineer v3.2

**Version:** 3.2  
**Category:** Testing & Quality Assurance  
**Replaces:** v3.1  
**Works with:** Claude · Gemini · Copilot · Cursor · Any AI Tool  
**Distilled from:** Google Testing Blog · Microsoft SDL · ISTQB · OWASP · Playwright Docs · Newman Docs · axe-core · W3C WCAG 2.1 · Kent Beck TDD · Martin Fowler Testing Patterns

---

## CHANGELOG v3.2

| # | Change | Reason |
|---|---------|-------|
| 1 | RULE 00: Detective Mode before any test | 90% of projects do not have documentation |
| 2 | Full Investigation Protocol | The tester discovers the project themselves |
| 3 | Smart Questions System | No assumptions — specific questions only |
| 4 | Playwright → Smoke only | Was too slow without justification |
| 5 | Newman → Main focus | 20x faster + covers logic |
| 6 | Layer 0: Business Logic | The most important and was completely absent |
| 7 | Document outcomes only, not steps | Reduce size while maintaining value |
| 8 | Discovered Checklist instead of static | Every project generates custom checklists |

---

## TABLE OF CONTENTS

1. [RULE 00 — Detective Mode](#rule00)
2. [Hard Rules](#hard-rules)
3. [Installation](#installation)
4. [Investigation Protocol](#investigation)
5. [Smart Questions System](#questions)
6. [Test Pyramid v3.2](#pyramid)
7. [Layer 0 — Business Logic](#layer0)
8. [Layer 1 — Playwright Smoke Only](#playwright)
9. [Layer 2 — Newman (Main Focus)](#newman)
10. [Layer 3 — Unit Tests](#unit)
11. [Discovered Checklist System](#checklist)
12. [Documentation Protocol](#documentation)
13. [Post-Session Analytics](#analytics)
14. [Regression Registry](#registry)
15. [CI/CD](#cicd)
16. [Activation Prompts](#prompts)
17. [Mandatory Outputs](#outputs)
18. [Folder Structure](#structure)

---

## [QA-DETECTIVE] 1. RULE 00 — DETECTIVE MODE {#rule00}

> This is the most important rule in the entire skill — never to be bypassed

```
"If you do not find documentation — do not assume.
 Dig into the code, database, and the running system.
 Gather facts. Record gaps. Ask precisely.
 
 Blind testing is more dangerous than no testing."
```

### When to apply?
```
Always — in every project — even if full documentation exists
Because code is the only truth that does not lie
```

---

## [QA-HARDRULES] 2. HARD RULES {#hard-rules}

```
RULE 00: Detective Mode first — no test before understanding the project
RULE 01: Run the installer on first activation in any project
RULE 02: Read qa-config.json before any test run
RULE 03: Read REGRESSION-REGISTRY.md — know what exists
RULE 04: New feature = investigation + tests + full regression
RULE 05: Playwright for smoke only — do not overload with slowMo in regression
RULE 06: Capture final outcome only — not every step
RULE 07: Video on failure only — no continuous recording
RULE 08: P0 Auth works first — always
RULE 09: Failure → instant screenshot → 1 retry → stop and report
RULE 10: No CSS selectors — role or data-testid only
RULE 11: Newman: The 5 folders per endpoint — mandatory
RULE 12: Layer 0 before Newman — logic before API
RULE 13: Update REGRESSION-REGISTRY.md after every session
RULE 14: a11y on every new page — not optional
RULE 15: Security baseline on every form and every auth endpoint
RULE 16: Calculate Health Score after every session
RULE 17: Clean Test Data after every E2E session
RULE 18: Inspect Server Logs after every test run
RULE 19: Do not start testing before answering critical questions
RULE 20: Discovered Checklist — discover then test, not the other way around
RULE 21: Unknown Feature → apply Feature DNA 8 dimensions — never improvise
```

---

## 3. INSTALLATION {#installation}

```bash
#!/bin/bash
# QA Master v3.2 — Project Self-Installer

PROJECT_ROOT=$(pwd)
PROJECT_NAME=$(basename "$PROJECT_ROOT")
AGENT_DIR="$PROJECT_ROOT/.agent"
DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M:%S)

echo "🔧 QA Master v3.2 — Installing in: $PROJECT_NAME"

mkdir -p "$AGENT_DIR/skills"
mkdir -p "$PROJECT_ROOT/evidence/testing/_reports/playwright"
mkdir -p "$PROJECT_ROOT/evidence/testing/_reports/api"
mkdir -p "$PROJECT_ROOT/evidence/testing/_reports/coverage"
mkdir -p "$PROJECT_ROOT/evidence/testing/screenshots/failures"
mkdir -p "$PROJECT_ROOT/evidence/testing/screenshots/system-proof"
mkdir -p "$PROJECT_ROOT/evidence/testing/flows"
mkdir -p "$PROJECT_ROOT/evidence/investigation"
mkdir -p "$PROJECT_ROOT/evidence/architecture-decisions"
mkdir -p "$PROJECT_ROOT/tests/e2e/helpers"
mkdir -p "$PROJECT_ROOT/tests/api/envs"
mkdir -p "$PROJECT_ROOT/tests/logic"

cat > "$AGENT_DIR/qa-config.json" << 'EOF'
{
  "project": "",
  "skillVersion": "3.2",
  "environment": {
    "local":   { "ui": "http://localhost:4200", "api": "http://localhost:5000" },
    "staging": { "ui": "", "api": "" }
  },
  "credentials": {
    "roles": []
  },
  "execution": {
    "dev": { "headless": false, "slowMo": 150, "workers": 1, "video": "on-failure" },
    "ci":  { "headless": true,  "slowMo": 0,   "workers": 4, "video": "on-failure" }
  },
  "performanceBudgets": {
    "pageLoad":    3000,
    "apiResponse": 1000,
    "search":      500,
    "formSubmit":  1500
  },
  "documentation": {
    "screenshots": {
      "mode": "outcomes-only",
      "captureOn": ["final-pass", "any-fail", "system-proof"]
    },
    "video": { "mode": "on-failure-only" },
    "criticalFlows": []
  },
  "a11yLevel": "wcag21aa",
  "browsers": ["chromium", "firefox"]
}
EOF

cat > "$PROJECT_ROOT/evidence/testing/REGRESSION-REGISTRY.md" << EOF
# REGRESSION REGISTRY — $PROJECT_NAME
Skill Version: 3.2 | Initialized: $DATE | Health: N/A

## FEATURES
| ID | Feature | Logic | API | E2E | a11y | Sec | Screenshots | Last Run | Health |
|----|---------|-------|-----|-----|------|-----|-------------|----------|--------|

## BUGS
| ID | Feature | Severity | Layer | Status | Found | Fixed | Root Cause |
|----|---------|----------|-------|--------|-------|-------|------------|

## TREND
| Date | Features | Pass% | Bugs | Health |
|------|----------|-------|------|--------|
| $DATE | 0 | N/A | 0 | N/A |
EOF

cat > "$PROJECT_ROOT/evidence/investigation/INVESTIGATION-TEMPLATE.md" << 'EOF'
# Investigation Report — [PROJECT NAME]
Date: | Investigator: | Status: 🔍 In Progress

## 1. What I Discovered from the Code

### Roles & Permissions
| Role | Permissions | Constraints |
|------|-------------|-------------|

### Discovered Features
| Feature | Description | Operations | States | Rules |
|---------|-------------|------------|--------|-------|

### Business Rules Extracted from Validators
| Rule | Condition | Result upon breach |
|------|-----------|--------------------|

### Discovered State Machines
| Entity | States | Allowed Transitions |
|--------|--------|---------------------|

## 2. What I Discovered from the Database

### Main Tables
| Table | Purpose | Relationships | Important Constraints |
|-------|---------|---------------|-----------------------|

### Enums / Lookup Tables
| Enum | Values | Meaning |
|------|--------|---------|

## 3. What I Discovered from the Running System

### Pages and Routes
| Route | What it displays | Operations | Export? | Filter? |
|-------|------------------|------------|---------|---------|

### Monitored API Calls (Network Tab)
| Endpoint | Method | When called | Parameters |
|----------|--------|-------------|------------|

### Pre-existing Errors (Console / Network)
| Error | On which page | Impact |
|-------|---------------|--------|

## 4. Gaps in Understanding — Required Questions

| # | Question | Why it's important | Priority | Answer |
|---|----------|--------------------|----------|--------|

## 5. Feature DNA Analysis
(To be filled for each discovered feature — before building the Test Plan)

| Feature | DATA | TIME | USERS | EXTERNAL | STATE | MEDIA | COMPUTATION | INTERFACE |
|---------|------|------|-------|----------|-------|-------|-------------|-----------|
| [feature] | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |

### Details of Active Dimensions (✅ only)
| Dimension | Details | Generated Tests |
|-----------|---------|-----------------|

## 6. Discovered Test Plan
(To be filled after answering questions + Feature DNA)

### Features × Test Types
| Feature | Logic Tests | API Tests | E2E Smoke | a11y | Security |
|---------|-------------|-----------|-----------|------|----------|

## 6. Decision to Start
[ ] All critical questions answered
[ ] Investigation Report complete
[ ] Test Plan approved
[ ] Ready to begin testing ✅
EOF

echo "✅ QA Master v3.2 installed in: $PROJECT_NAME"
echo "→ Next step: Execute Investigation Protocol"
```

---

## [QA-INVESTIGATION] 4. INVESTIGATION PROTOCOL {#investigation}

> Execute this completely before writing any test

### STEP 1 — Reading Code (Backend)

```
Mandatory Order:

□ Domain Entities
  - What are the main entities?
  - What are their relationships?
  - What are the properties and their types?
  - What are the value objects and enums?

□ Application Services / Use Cases
  - What operations are available? (Create/Update/Delete/Approve...)
  - What are the required DTOs for each operation?
  - What are the validations on each input?

□ Domain Events
  - What happens behind the scenes?
  - What are the side effects? (emails / notifications / updates)

□ Permissions / Authorization
  - What permission constants are defined?
  - Who owns which permission?
  - Is there resource-based authorization?

□ Database Migrations / Schema
  - What are the actual constraints? (unique / not null / check)
  - What are the indexes? (indicates frequently searched fields)
  - What are the default values?
```

### STEP 2 — Reading Code (Frontend)

```
□ Routing Module
  - All existing routes
  - The guards on each route
  - The lazy loaded modules

□ Components
  - What is displayed in each component?
  - What are the @Input and @Output?
  - What services are used?

□ Services / HTTP Calls
  - All called API endpoints
  - Error handling mechanism
  - Caching if it exists

□ Models / Interfaces
  - Expected data format
  - Optional fields
  - Enums used in the UI
```

### STEP 3 — Exploring the Running System

```
□ Open each page — Record:
  - What does it display?
  - What operations are available?
  - Does it have filter? sort? export? print?
  - What are the visible edge cases?

□ Open Network Tab — For each page:
  - What API calls happen?
  - What are the query parameters?
  - What is the shape of the responses?

□ Open Console — Record:
  - Every pre-existing error
  - Every warning
  - Every failed request

□ Try Failure States:
  - Slow connection (Network throttling)
  - API error simulation
  - Empty data
```

### STEP 4 — Drawing the Relationship Map

```markdown
## Relationship Map — [PROJECT]

### Data Flow
[Entity A] ──creates──> [Entity B] ──triggers──> [Notification]
[Feature X] ──depends on──> [Feature Y]

### Critical Paths (Highest Risk)
1. [The path affecting money / approvals / deletions]
2. [The path passing through the most entities]
3. [The most frequently used path]

### Shared State (Data shared between features)
- [entity]: used in [feature A, B, C]
- changing it affects: [...]
```

---

## [QA-QUESTIONS] 5. SMART QUESTIONS SYSTEM {#questions}

> Every question must be specific and based on what you discovered

### Smart Question Template

```markdown
## Question #[N]
**Discovered in code:** [What you actually found]
**Gap in understanding:** [What you couldn't find an answer to]
**Question:** [Very specific question]
**Why it's important for testing:** [Impact on test plan]
**Priority:** Critical / Important / Enhancement
```

### Examples of Smart Questions

```markdown
## Question #1
Discovered: Application.Status has 4 values: Draft/Submitted/Approved/Rejected
Gap: Couldn't find logic for Re-open after Rejected
Question: Can a rejected Application be re-opened? And who has the permission?
Why it's important: State machine tests will fail if we assume incorrectly
Priority: Critical

## Question #2
Discovered: ExportService contains ExportToExcel but no PDF method
Gap: I don't know if PDF is planned or postponed
Question: Is PDF export required for this feature? If yes — does it have a special layout?
Why it's important: So I don't waste time testing a non-existent feature
Priority: Important

## Question #3
Discovered: Scholarship.MaxApplicants = nullable
Gap: I don't know the expected behavior if it's null
Question: If MaxApplicants is empty — does it mean "no limit" or "closed"?
Why it's important: Boundary tests will differ entirely based on the answer
Priority: Critical
```

### Critical Questions Rule

```
Testing will not start until these questions are answered:
  ✓ Anything related to State Transitions
  ✓ Anything related to money or approvals
  ✓ Anything related to Permissions and deletion privileges
  
These can be postponed:
  ~ UX and user experience questions
  ~ Rare edge cases questions
  ~ Future enhancements questions
```

---

## [QA-PYRAMID] 6. TEST PYRAMID v3.2 {#pyramid}

```
                    /\
                   /E2E\          ← 5%   Playwright (Smoke + Auth only)
                  /──────\
                 / Newman  \      ← 45%  API + Business Scenarios
                /────────────\
               / Unit + Logic \   ← 50%  xUnit/Jest + Domain Logic
              /________________\

Logic:
  Layer 0 (Logic)  → Fastest — milliseconds — catches faulty logic
  Layer 2 (Newman) → Fast — seconds — catches API and integration issues
  Layer 1 (E2E)    → Slow — minutes — catches what others miss in the UI
```

---

## [QA-L0-LOGIC] 7. LAYER 0 — BUSINESS LOGIC TESTING {#layer0}

> The most important layer — completely absent in v3.1

### 7.1 — State Machine Tests

```csharp
// For every entity with states — test every possible and impossible transition
// Discover the states from the code first — do not assume

[Theory]
// ✅ Allowed transitions
[InlineData("Draft",      "Submitted",   true)]
[InlineData("Submitted",  "UnderReview", true)]
[InlineData("UnderReview","Approved",    true)]
[InlineData("UnderReview","Rejected",    true)]
// ❌ Forbidden transitions — discovered from Business Rules
[InlineData("Submitted",  "Draft",       false)]
[InlineData("Approved",   "Rejected",    false)]
[InlineData("Rejected",   "Approved",    false)]
public void Entity_StateTransition_EnforcesRules(
    string from, string to, bool shouldSucceed)
{
    // arrange
    var entity = CreateEntityWithStatus(from);
    // act
    var act = () => entity.TransitionTo(ParseStatus(to));
    // assert
    if (shouldSucceed)
        act.Should().NotThrow();
    else
        act.Should().Throw<BusinessException>();
}
```

### 7.2 — Invariant Tests (Unbreakable Rules)

```csharp
// For every rule discovered from code or questions — test it

// Example: Approved amount cannot exceed total budget
[Fact]
public void ApprovedAmount_CannotExceedTotalBudget()
{
    var entity = new Entity { TotalBudget = 5000 };
    var act = () => entity.Approve(amount: 7000);
    act.Should().Throw<BusinessException>()
       .WithMessage("*exceed*budget*");
}

// Example: No submission after deadline
[Fact]
public void Submission_IsRejected_AfterDeadline()
{
    var entity = new Entity { Deadline = DateTime.Now.AddDays(-1) };
    var act = () => entity.Submit();
    act.Should().Throw<BusinessException>()
       .WithMessage("*deadline*");
}

// Example: Capacity cannot be exceeded
[Fact]
public void Capacity_CannotBeExceeded()
{
    var entity = new Entity { MaxCapacity = 10 };
    for (int i = 0; i < 10; i++) entity.AddMember();
    var act = () => entity.AddMember(); // The 11th
    act.Should().Throw<BusinessException>()
       .WithMessage("*capacity*full*");
}
```

### 7.3 — Decision Table Tests

```markdown
## Before writing — draw the decision table from discovered data:

| Condition 1 | Condition 2 | Condition 3 | Result        |
|-------------|-------------|-------------|---------------|
| GPA ≥ 3.5   | Level = B   | Full-time   | ✅ Eligible   |
| GPA ≥ 3.5   | Level = B   | Part-time   | ❌ Ineligible |
| GPA < 3.5   | Level = B   | Full-time   | ❌ Ineligible |
| GPA ≥ 3.5   | Level = M   | Full-time   | ❌ Ineligible |
```

```csharp
// Each row in the table = 1 test
[Theory]
[InlineData(3.5, "Bachelor", true,  true)]
[InlineData(3.5, "Bachelor", false, false)]
[InlineData(2.9, "Bachelor", true,  false)]
[InlineData(3.5, "Master",   true,  false)]
public void EligibilityRule_MatchesDecisionTable(
    double gpa, string level, bool fullTime, bool expected)
{
    var result = _service.CheckEligibility(new Request
    {
        GPA = gpa, Level = level, IsFullTime = fullTime
    });
    result.IsEligible.Should().Be(expected);
}
```

### 7.4 — Data Contradiction Tests

```csharp
// Discover possible contradictions from the relationship map

// Example: Student enrolled in conflicting scholarships
[Fact]
public void Student_CannotHold_ConflictingScholarships()
{
    var student = new Student();
    student.AssignScholarship(fullTimeRequired);   // ✅
    var act = () => student.AssignScholarship(partTimeRequired); // ❌
    act.Should().Throw<BusinessException>()
       .WithMessage("*conflict*");
}

// Example: Start date after end date
[Fact]
public void Event_StartDate_CannotBeAfterEndDate()
{
    var act = () => new Event
    {
        StartDate = DateTime.Today.AddDays(5),
        EndDate   = DateTime.Today.AddDays(1) // Before start
    };
    act.Should().Throw<ArgumentException>();
}
```

### 7.5 — Full Story Tests

```csharp
// Test the entire journey — not just isolated steps
// Discover stories from User Stories or Relationship Map

[Fact]
public async Task Story_CompleteJourney_FromSubmitToCompletion()
{
    // Chapter 1: Application
    var application = await _appService.CreateAsync(validRequest);
    application.Status.Should().Be("Draft");

    // Chapter 2: Submission
    await _appService.SubmitAsync(application.Id);
    application = await _appService.GetAsync(application.Id);
    application.Status.Should().Be("Submitted");

    // Chapter 3: Review — check side effects
    await _reviewService.StartReviewAsync(application.Id);
    var notification = await _notificationRepo.GetLatestAsync(application.UserId);
    notification.Should().NotBeNull(); // Notification sent

    // Chapter 4: Approval — check constraints
    await _approvalService.ApproveAsync(application.Id, amount: 3000);
    var budget = await _budgetService.GetRemainingAsync();
    budget.Should().BeGreaterOrEqualTo(0); // Unbreakable fixed rule

    // Chapter 5: Final verification
    application = await _appService.GetAsync(application.Id);
    application.Status.Should().Be("Approved");
    application.ApprovedAmount.Should().Be(3000);
}
```

---

## [QA-E2E-SMOKE] 8. LAYER 1 — PLAYWRIGHT SMOKE ONLY {#playwright}

> Playwright for smoke only — do not burden it with what Newman can do

### When to use Playwright?

```
✅ Use it only for:
  - Auth flows (login / logout / session)
  - Critical UI that Newman is blind to
  - Visual UX (layout / responsive / RTL)
  - Interactions relying on the DOM

❌ Do not use it for:
  - Validation rules (Newman is enough)
  - Business logic (Layer 0 is enough)
  - API responses (Newman is enough)
```

### Configuration

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

const isCI = process.env.CI === 'true';

export default defineConfig({
  testDir:  './tests/e2e',
  timeout:  30_000,
  retries:  1,
  workers:  isCI ? 4 : 1,
  reporter: [
    ['html', { outputFolder: 'evidence/testing/_reports/playwright' }],
    ['json', { outputFile:   'evidence/testing/_reports/results.json' }],
    ['list']
  ],
  use: {
    headless:   isCI,
    slowMo:     isCI ? 0 : 150,       // ← Faster than v3.1 (was 300)
    video:     'on-failure',           // ← Video on failure only
    screenshot: 'off',                 // ← We control screenshots manually
    trace:     'retain-on-failure',
    baseURL:    process.env.BASE_URL ?? 'http://localhost:4200',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox',  use: { ...devices['Desktop Firefox'] } },
    { name: 'mobile',   use: { ...devices['iPhone 13'] } },
  ],
});
```

### Smoke Test Structure

```typescript
// tests/e2e/smoke.spec.ts
// This file only covers critical paths that Newman doesn't see

test.describe('P0 — Auth (Critical)', () => {
  test('Login valid → dashboard loads', async ({ page }) => { });
  test('Login invalid → specific error shown', async ({ page }) => { });
  test('Protected route without token → redirect', async ({ page }) => { });
  test('Role-based UI visibility', async ({ page }) => { });
  test('Logout → session cleared', async ({ page }) => { });
});

test.describe('P1 — Critical UI Flows', () => {
  // Only flows with special UI behavior
  // Do not re-test what Newman has tested
  test('Main happy path — user can complete primary task', async ({ page }) => { });
  test('Empty state shown when no data', async ({ page }) => { });
  test('Error state shown on API failure', async ({ page }) => { });
});

test.describe('P2 — Layout & Responsiveness', () => {
  test('Mobile layout — no broken elements', async ({ page }) => { });
  test('RTL layout correct for Arabic', async ({ page }) => { });
  test('Keyboard navigation works', async ({ page }) => { });
});
```

### Screenshot Protocol (Modified)

```typescript
// helpers/screenshot.helper.ts
// We photograph the outcome only — not every step

export type ScreenshotType = 'system-proof' | 'failure' | 'final-result';

export async function captureOutcome(
  page: Page,
  type: ScreenshotType,
  context: { feature: string; scenario: string; note: string }
): Promise<string> {

  const timestamp = new Date().toISOString().replace(/[-:.TZ]/g, '').slice(0, 15);
  const filename  = `${context.feature}-${context.scenario}-${type}-${timestamp}.png`;

  const dir = type === 'failure'
    ? 'evidence/testing/screenshots/failures'
    : type === 'system-proof'
    ? 'evidence/testing/screenshots/system-proof'
    : `evidence/testing/screenshots/${context.feature}`;

  fs.mkdirSync(dir, { recursive: true });

  await page.screenshot({
    path:     `${dir}/${filename}`,
    fullPage: type === 'failure' // full page only on failure
  });

  return `${dir}/${filename}`;
}

// In the test:
// ✅ Correct
await captureOutcome(page, 'final-result', {
  feature: 'blog', scenario: 'create-post', note: 'Post appeared in list'
});

// ❌ Wrong — we do not capture every step
await page.fill('[name=title]', 'My Post');
await page.screenshot({ path: 'step-2.png' }); // Forbidden
```

---

## [QA-API-NEWMAN] 9. LAYER 2 — NEWMAN (Main Focus) {#newman}

> This is the heart of testing in v3.2 — it must be comprehensive

### Setup

```bash
npm install -g newman newman-reporter-htmlextra

# Run a single feature
newman run tests/api/[feature].collection.json \
  --environment tests/api/envs/local.json \
  --reporters cli,htmlextra,json \
  --reporter-htmlextra-export evidence/testing/_reports/api/[feature]-report.html \
  --reporter-json-export evidence/testing/_reports/api/[feature]-results.json \
  --bail

# Run full regression
newman run tests/api/regression.collection.json \
  --environment tests/api/envs/local.json \
  --reporters cli,htmlextra \
  --reporter-htmlextra-export evidence/testing/_reports/api/regression-report.html
```

### Full Collection Structure — Template

```json
{
  "info": {
    "name": "[Feature] — Complete Test Suite",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [

    {
      "name": "📁 Folder 1 — Happy Path",
      "item": [
        {
          "name": "Create — Valid Data",
          "event": [
            {
              "listen": "test",
              "script": {
                "exec": [
                  "pm.test('Status 200/201', () => pm.response.to.have.status(201));",
                  "pm.test('Response time < 1000ms', () => pm.expect(pm.response.responseTime).to.be.below(1000));",
                  "pm.test('Returns id', () => pm.expect(pm.response.json()).to.have.property('id'));",
                  "pm.test('Schema matches contract', () => pm.response.to.have.jsonSchema(pm.globals.get('schema')));",
                  "pm.environment.set('createdId', pm.response.json().id);"
                ]
              }
            }
          ]
        },
        {
          "name": "Read — Get by ID",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 200', () => pm.response.to.have.status(200));",
            "pm.test('Data matches what was created', () => {",
            "  const body = pm.response.json();",
            "  pm.expect(body.id).to.eql(pm.environment.get('createdId'));",
            "});"
          ]}}]
        },
        {
          "name": "List — Pagination",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 200', () => pm.response.to.have.status(200));",
            "pm.test('Has items array', () => pm.expect(pm.response.json().items).to.be.an('array'));",
            "pm.test('Has totalCount', () => pm.expect(pm.response.json().totalCount).to.be.a('number'));",
            "pm.test('Respects pageSize', () => pm.expect(pm.response.json().items.length).to.be.at.most(10));"
          ]}}]
        }
      ]
    },

    {
      "name": "📁 Folder 2 — Validation & Errors",
      "item": [
        {
          "name": "Empty required fields → 400",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 400', () => pm.response.to.have.status(400));",
            "pm.test('Error message is specific (not generic)', () => {",
            "  const body = pm.response.json();",
            "  pm.expect(body.message || body.error).to.not.include('Something went wrong');",
            "  pm.expect(body.message || body.error).to.have.length.above(10);",
            "});"
          ]}}]
        },
        {
          "name": "Beyond max length → 400",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 400', () => pm.response.to.have.status(400));",
            "pm.test('Mentions field name in error', () => {",
            "  pm.expect(JSON.stringify(pm.response.json())).to.include('title');",
            "});"
          ]}}]
        },
        {
          "name": "Invalid data type → 400",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 400', () => pm.response.to.have.status(400));"
          ]}}]
        }
      ]
    },

    {
      "name": "📁 Folder 3 — Auth & Authorization",
      "item": [
        {
          "name": "No token → 401",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 401', () => pm.response.to.have.status(401));"
          ]}}]
        },
        {
          "name": "Invalid token → 401",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 401', () => pm.response.to.have.status(401));"
          ]}}]
        },
        {
          "name": "Wrong role (user tries admin endpoint) → 403",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 403', () => pm.response.to.have.status(403));"
          ]}}]
        },
        {
          "name": "User accesses another user's resource → 403/404",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Cannot access other user resource', () => {",
            "  pm.expect(pm.response.code).to.be.oneOf([403, 404]);",
            "});"
          ]}}]
        }
      ]
    },

    {
      "name": "📁 Folder 4 — Boundary & Edge Values",
      "item": [
        {
          "name": "Minimum valid value",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 201 — minimum accepted', () => pm.response.to.have.status(201));"
          ]}}]
        },
        {
          "name": "Maximum valid value",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 201 — maximum accepted', () => pm.response.to.have.status(201));"
          ]}}]
        },
        {
          "name": "Maximum + 1 → rejected",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Status 400 — beyond maximum rejected', () => pm.response.to.have.status(400));"
          ]}}]
        },
        {
          "name": "XSS payload in text fields",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('XSS not executed — escaped or rejected', () => {",
            "  pm.expect(pm.response.text()).to.not.include('<script>alert');",
            "});"
          ]}}]
        },
        {
          "name": "SQL injection in inputs",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('SQLi: no 500 error', () => pm.expect(pm.response.code).to.not.equal(500));",
            "pm.test('SQLi: no stack trace leaked', () => {",
            "  pm.expect(pm.response.text()).to.not.include('SqlException');",
            "  pm.expect(pm.response.text()).to.not.include('at System.');",
            "});"
          ]}}]
        },
        {
          "name": "Arabic text input",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Arabic text accepted and returned correctly', () => {",
            "  const body = pm.response.json();",
            "  pm.expect(JSON.stringify(body)).to.include('\\u0627\\u0644');",
            "});"
          ]}}]
        },
        {
          "name": "Null optional fields",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Null optional fields accepted', () => pm.response.to.have.status(201));"
          ]}}]
        },
        {
          "name": "Pagination — beyond last page",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Beyond last page: empty items, not error', () => {",
            "  pm.expect(pm.response.code).to.equal(200);",
            "  pm.expect(pm.response.json().items).to.be.an('array').that.is.empty;",
            "});"
          ]}}]
        }
      ]
    },

    {
      "name": "📁 Folder 5 — Chained Flow (Full Story)",
      "item": [
        {
          "name": "Step 1: Create",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Created successfully', () => pm.response.to.have.status(201));",
            "pm.environment.set('chainId', pm.response.json().id);"
          ]}}]
        },
        {
          "name": "Step 2: Read — Verify created data",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Data persisted correctly', () => {",
            "  const body = pm.response.json();",
            "  pm.expect(body.id).to.eql(pm.environment.get('chainId'));",
            "});"
          ]}}]
        },
        {
          "name": "Step 3: Update",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Updated successfully', () => pm.response.to.have.status(200));"
          ]}}]
        },
        {
          "name": "Step 4: Read — Verify update applied",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Update reflected in GET', () => {",
            "  pm.expect(pm.response.json().title).to.include('Updated');",
            "});"
          ]}}]
        },
        {
          "name": "Step 5: Delete",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Deleted successfully', () => pm.response.to.have.status(204));"
          ]}}]
        },
        {
          "name": "Step 6: Read after delete → 404",
          "event": [{ "listen": "test", "script": { "exec": [
            "pm.test('Deleted resource returns 404', () => pm.response.to.have.status(404));"
          ]}}]
        }
      ]
    },

    {
      "name": "📁 Folder 6 — Business Logic Scenarios",
      "description": "This folder is filled after Investigation — customized for each project",
      "item": [
        {
          "name": "[DISCOVERED RULE 1] — [Rule Description]",
          "event": [{ "listen": "test", "script": { "exec": [
            "// Write tests based on what you discovered from Investigation"
          ]}}]
        }
      ]
    }

  ]
}
```

### Schema Validation Helper

```javascript
// In pre-request script or in globals
pm.globals.set('validateSchema', function(data, schema) {
  const errors = [];

  // Check required fields
  if (schema.required) {
    schema.required.forEach(field => {
      if (data[field] === undefined || data[field] === null) {
        errors.push(`Missing required field: ${field}`);
      }
    });
  }

  // Check types
  if (schema.properties) {
    Object.entries(schema.properties).forEach(([key, def]) => {
      if (data[key] !== undefined) {
        const actualType = typeof data[key];
        if (def.type === 'array' && !Array.isArray(data[key])) {
          errors.push(`${key}: expected array, got ${actualType}`);
        } else if (def.type !== 'array' && actualType !== def.type) {
          errors.push(`${key}: expected ${def.type}, got ${actualType}`);
        }
      }
    });
  }

  return errors;
});
```

---

## [QA-UNIT] 10. LAYER 3 — UNIT TESTS {#unit}

### Coverage Thresholds

```json
{
  "coverageThreshold": {
    "global": {
      "branches":  65,
      "functions": 75,
      "lines":     75
    }
  }
}
```

### Checklist for each AppService

```
  ✅ Happy path → expected output
  ✅ Every Business Rule has a separate test
  ✅ Guard clauses (null / empty / invalid) → correct exception
  ✅ Boundary values
  ✅ Permission checks (mock ICurrentUser)
  ✅ Domain events published after operations
  ✅ Idempotency — same operation twice → same result
```

### Checklist for each Angular Component

```
  ✅ Renders without error
  ✅ @Input bindings visible in the template
  ✅ @Output events are emitted
  ✅ Service calls mocked
  ✅ Loading state is displayed
  ✅ Error state is displayed
  ✅ Empty state is displayed
```

---

## [QA-CHECKLISTS] 11. DISCOVERED CHECKLIST SYSTEM {#checklist}

> No static checklist — every project generates custom checklists from Investigation

### How does it work?

```
1. Execute Investigation Protocol
2. For each discovered feature → ask the following question:

   "What can happen to this feature?"
   
3. The answer automatically generates the checklist
```

### Feature DNA Analysis — Works with any feature even unknown ones

> This system comes **before** the Universal Triggers
> It ensures coverage of any feature — even if never mentioned in this file

```markdown
## Feature DNA — 8 dimensions for any feature

After Investigation, for each discovered feature ask the 8 dimensions:
Every ✅ generates a custom checklist — every ❌ is removed from the plan

| Dimension | Core Question | If ✅ — Test |
|-----------|---------------|--------------|
| 1. DATA | Does it read or write data? | 0 records / 1 / many / corrupted / sensitive |
| 2. TIME | Does it involve timing or real-time? | Before/during/after deadline — interruption — delay |
| 3. USERS | How many users interact with it? | One: isolation — Multiple: conflict + race condition |
| 4. EXTERNAL | Does it connect to an external service? | Success / failure / slowness / complete outage |
| 5. STATE | Does it have states? | Every allowed transition + every forbidden transition |
| 6. MEDIA | Does it handle files or media? | Size / extension / corrupted file / large file |
| 7. COMPUTATION | Does it involve calculations or AI? | Precision / overflow / negative values / illogical results |
| 8. INTERFACE | Does it have special UI interaction? | Every gesture / shortcut / animation / live update |
```

```markdown
## Feature DNA — Filling Template in Investigation

### [Feature Name] — DNA Analysis
| Dimension | Present? | Discovered Details | Generated Tests |
|-----------|----------|--------------------|-----------------|
| DATA | ✅ | Reads and writes — sensitive data | Save / conflict / leak |
| TIME | ✅ | deadline + real-time updates | Before/after deadline / interruption |
| USERS | ✅ | 3 different roles | Each role + permission intersection |
| EXTERNAL | ❌ | None | — |
| STATE | ✅ | Draft→Submitted→Approved | Complete State Machine |
| MEDIA | ❌ | None | — |
| COMPUTATION | ✅ | Calculating remaining amount | Precision + overflow + negative |
| INTERFACE | ✅ | drag & drop + live cursor | Every gesture + interruption |

→ Active dimensions: DATA, TIME, USERS, STATE, COMPUTATION, INTERFACE
→ Tests automatically generated from these 6 dimensions only
```

```markdown
## Practical Example — A feature not mentioned in the file
## "Real-time Collaborative Editing"

DNA Analysis:
  DATA        ✅ → Test: Two users save the same line → Who wins?
  TIME        ✅ → Test: 5 seconds delay in sync → Does data conflict?
  USERS       ✅ → Test: 50 users at the same time → Is performance acceptable?
  EXTERNAL    ❌ → Removed
  STATE       ✅ → Test: connected / disconnected / reconnecting
  MEDIA       ❌ → Removed
  COMPUTATION ✅ → Test: merge conflict algorithm — Result logical?
  INTERFACE   ✅ → Test: User 2's cursor appears to User 1 immediately?

Automatically generated tests — without mentioning "Collaborative Editing" in the file ever:
  □ Two users edit the same word → one result, no conflict
  □ Interruption while typing → Data saved upon reconnection
  □ New user joins → Sees current state completely
  □ 50 users → response time < budget
  □ Others' cursors appear/disappear correctly
```

---

### Universal Triggers — Questions for each feature

> These are applied **after** Feature DNA — for common features expand on details

```markdown
## For each discovered Feature — ask these questions:

### If you find a LIST:
  □ Does it work with 0 records? (empty state)
  □ Does it work with 1 record?
  □ Does it work with 10,000 records? (performance)
  □ Does it have a sort? → Test ascending + descending + persists with pagination
  □ Does it have a filter? → See filter section
  □ Does it have a search? → See search section
  □ Does it have pagination? → Page 1 + last + beyond last
  □ Does it have an export? → See export section

### If you find a FORM:
  □ Are all required fields rejected if empty?
  □ Do errors appear together, not one by one?
  □ Does data persist after an API error?
  □ Does it prevent double submit?
  □ Does it warn when leaving page without saving?
  □ Is Tab order logical?
  □ Does Enter submit the form? (And is this desired?)
  □ Does it work with copy-paste?
  □ Does date picker reject illogical dates?
  □ Does file upload reject large sizes?
  □ Does file upload reject wrong extensions?

### If you find a FILTER:
  □ Does a single filter work?
  □ Do two filters work together?
  □ Do all filters work together?
  □ Does "clear all" clear everything?
  □ Does the URL change? (shareable link)
  □ Does the filter persist after refresh?
  □ Does the filter reset pagination to page 1?
  □ Does a filter with no results give an empty state?

### If you find a SEARCH:
  □ Does it work with partial text?
  □ Is it case-insensitive?
  □ Does it work in Arabic?
  □ Unfound text → clear message?
  □ Do special chars not break the system?
  □ Does it work with debounce? (Not a request per char)

### If you find EXPORT (PDF / Excel / CSV):
  □ Does it work with 0 records? (Empty file or message?)
  □ Does it work with 10,000 records? (No hanging)
  □ Does it export only filtered or all?
  □ Is the file name logical?
  □ If PDF:
      □ Is Arabic Right-to-Left?
      □ Do tables not break?
      □ Do charts appear?
      □ Are pages numbered?
  □ If Excel:
      □ Are all columns present?
      □ Are headers correct?
      □ Are numbers actual numbers, not text?

### If you find a WORKFLOW / APPROVAL:
  □ Is every state transition correct? (State Machine)
  □ Are forbidden transitions rejected?
  □ Is a notification sent at each stage?
  □ Does the assignee receive the notification?
  □ Can a stage be skipped? (Should not)
  □ Can it be reverted? (Depends on business rule)
  □ Does it have a deadline? → What happens if it expires?

### If you find PERMISSIONS:
  □ Does each role only see what is allowed?
  □ Is the Admin UI hidden from the User?
  □ Is the Admin URL rejected without permission?
  □ Can another user's data be accessed? (IDOR)
  □ Does changing a role update permissions immediately?

### If you find NOTIFICATIONS:
  □ Does Toast appear in 500ms?
  □ Does Toast disappear automatically?
  □ Can it be closed manually?
  □ Do 3 Toasts together not overlap?
  □ Is the error message visually distinct from success?
  □ Do Confirmation dialogs explain consequences?

### If you find CHARTS / DASHBOARD:
  □ Is the data correct? (Check the API)
  □ Does it work with 0 data points?
  □ Does it work with 10,000 data points?
  □ Are legends clear?
  □ Does it update upon changing the filter?

### For each page — UI/UX Universal:
  □ Does the page title change? (browser tab)
  □ Is the breadcrumb correct?
  □ Is the loading state professional? (skeleton / spinner)
  □ Is the console free of errors?
  □ Does it work on mobile? (375px)
  □ Does it work with browser zoom 150%?
  □ Is a11y: no violations?
```

### Feature DNA Analysis — For each feature not present in the above list

> If you discover a feature that doesn't belong to any known trigger — apply this analysis
> Works with anything — even features not yet invented

```markdown
## The 8 dimensions — ask each dimension for every discovered feature

Dimension 1: DATA
  □ Does it read data?
      → Test: 0 records / 1 / many / corrupted data / null
  □ Does it write data?
      → Test: Correct save / update / conflict during concurrent save
  □ Is the data sensitive?
      → Test: Doesn't appear in URL / doesn't leak in logs / encrypted in DB

Dimension 2: TIME
  □ Does it have a timer or deadline?
      → Test: Before time / during / after / expired
  □ Does it have real-time / WebSocket?
      → Test: Sync between users / connection drop / reconnection
  □ Does it have scheduling or cron?
      → Test: Execution on time / failure & retry / wrong repetition

Dimension 3: USERS
  □ Is it only one user?
      → Test: Isolation / doesn't see others' data
  □ Are there multiple concurrent users?
      → Test: Race condition / who wins on conflict / locking
  □ Do different roles interact?
      → Test: Each role individually + intersection points between them

Dimension 4: EXTERNAL
  □ Does it connect to an external API or service?
      → Test: Success / timeout / 500 / complete outage / slow response
  □ Does it receive external data? (webhook / callback)
      → Test: Correct data / malformed / suspicious / duplicate
  □ Does it send externally? (email / SMS / push)
      → Test: Correct send / failure / no repetition

Dimension 5: STATE
  □ Does it have states or workflow?
      → Draw State Machine → test every allowed and forbidden transition
  □ Is state saved across sessions?
      → Test: refresh / logout-login / another device
  □ Is state shared between users?
      → Test: Change appears to everyone immediately / or after refresh

Dimension 6: MEDIA
  □ Does it have file or image uploads?
      → Test: Max size / rejected extensions / corrupted file / special name
  □ Does it display images or video?
      → Test: Broken image → fallback / video won't load / slow load
  □ Does it process files? (PDF generation / Excel / compress)
      → Test: 0 records / 10,000 records / Arabic data / layout

Dimension 7: COMPUTATION
  □ Does it involve calculations or formulas?
      → Test: Decimal precision / negative values / overflow / divide by zero
  □ Does it have AI or ML?
      → Test: Logical result / weird input / empty input / bias in results
  □ Does it transform or aggregate data?
      → Test: Accuracy of result / data loss / performance with large amounts

Dimension 8: INTERFACE
  □ Does it have non-traditional interaction? (drag-drop / canvas / map / swipe)
      → Test: Every gesture / keyboard alternative / mobile vs desktop
  □ Does it have live updates in the UI?
      → Test: Auto update / no flicker / performance with many updates
  □ Does it have special navigation or routing?
      → Test: Direct URL / browser back / deep link / query params
```

### How to use Feature DNA

```markdown
## Application Steps — 3 minutes per feature

1. Write the feature name
2. Ask each of the 8 dimensions: "Does this apply to this feature?"
3. For each dimension with ✅ → add corresponding tests to Test Plan
4. For each dimension with ❌ → ignore it completely

## Practical Example: "Real-time Chat"

| Dimension | Applies? | Generated Tests |
|-----------|----------|-----------------|
| DATA | ✅ | Messages saved / not lost on drop |
| TIME | ✅ | real-time delivery / correct timestamp |
| USERS | ✅ | User typing → appears to other / blocking |
| EXTERNAL | ❌ | — |
| STATE | ✅ | read/unread / online/offline |
| MEDIA | ✅ | Sending images / files / max size |
| COMPUTATION | ❌ | — |
| INTERFACE | ✅ | Auto scroll down / Enter submits |

## Practical Example: "AI Scholarship Recommender"

| Dimension | Applies? | Generated Tests |
|-----------|----------|-----------------|
| DATA | ✅ | Missing data → does it work? |
| TIME | ❌ | — |
| USERS | ✅ | Same student → same recommendation always? |
| EXTERNAL | ✅ | AI service fails → fallback? |
| STATE | ❌ | — |
| MEDIA | ❌ | — |
| COMPUTATION | ✅ | Logical result / weird input / bias |
| INTERFACE | ✅ | Explaining reason for recommendation / how it updates |
```

### The New Rule

```
RULE 21 — Feature DNA before any Trigger:
"If you don't find the feature in Universal Triggers
 → apply the 8 dimensions → generate custom tests
 → do not improvise and do not ignore"
```

---

## [QA-DOC] 12. DOCUMENTATION PROTOCOL {#documentation}

> "Document Outcomes, Not Steps"

### What we document

```
✅ We document:
  System Proof   → One full picture of the UI working correctly
  Failure State  → Picture + video of error for analysis
  Bug Fix        → Before and after
  Critical Flow  → Video for the full journey

❌ We do not document:
  Every step in the test
  Intermediate states
  The same thing twice
```

### System Proof Screenshot

```typescript
// Upon feature completion → one picture proving it works
async function captureSystemProof(page: Page, feature: string, note: string) {
  await page.waitForLoadState('networkidle');
  await captureOutcome(page, 'system-proof', {
    feature, scenario: 'working-state', note
  });
}

// Example usage — only once for the feature
test('@proof Blog.List.WorkingState', async ({ page }) => {
  await loginAs(page, 'admin');
  await page.goto('/blog/posts');
  await page.waitForLoadState('networkidle');
  await captureSystemProof(page, 'blog', 'Blog list with real data — production ready');
});
```

### Bug Fix Documentation

```markdown
<!-- evidence/testing/screenshots/failures/BUG-[ID]/diff-notes.md -->

# BUG-[ID] Fix Documentation
**Feature:** [Feature name]
**Severity:** Critical / High / Medium / Low
**Found:** [Discovery date]
**Fixed:** [Fix date]

## The Problem
[Precise description of the problem]

## Root Cause
[The root cause from the code]

## Before Fix
![before](before-[timestamp].png)
[What used to appear]

## After Fix
![after](after-[timestamp].png)
[What appears now]

## Applied Solution
[What changed in the code]

## How we prevent recurrence
[The test added to prevent regression]
```

### Critical Flow Video

```typescript
// One video for the full journey — only once upon completion
test('@flow Auth.CompleteJourney', async ({ page }) => {
  // This test is run with video: 'on' once for documentation
  // Then saved in evidence/testing/flows/auth-journey.webm
});
```

---

## 13. POST-SESSION ANALYTICS {#analytics}

### Health Score Formula (Modified)

```
Dimension               Weight   Score (0-10)
──────────────────────────────────────────────
Business Logic Tests      25%     (Layer 0 pass rate × 10)
API Tests (Newman)        25%     (passed/total × 10)
E2E Smoke                 15%     (passed/total × 10)
Observability Coverage    15%     (error states covered × 10)
a11y Compliance           10%     (0 violations=10, -1 per violation)
Security Baseline         10%     (0 issues=10, -2 per issue)
──────────────────────────────────────────────
TOTAL                    100%     /100

90-100 🟢 Excellent  — production ready
70-89  🟡 Good       — ship with monitoring
50-69  🟠 Fair       — fix before next feature
0-49   🔴 Poor       — do not ship
```

### Session Report Template

```markdown
## [DATE] — [FEATURE] — Health: [XX]/100

### Scores
| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|---------|
| Business Logic | 25% | X/10 | X |
| API (Newman) | 25% | X/10 | X |
| E2E Smoke | 15% | X/10 | X |
| Observability | 15% | X/10 | X |
| a11y | 10% | X/10 | X |
| Security | 10% | X/10 | X |
| **TOTAL** | | | **/100** |

### Investigation Summary
| What I discovered | Source | Impact on testing |
|-------------------|--------|-------------------|

### Questions Asked & Answered
| Question | Answer | Impact |
|----------|--------|--------|

### Discovered Checklist Coverage
| Feature | Discovered triggers | Tested | Missing |
|---------|---------------------|--------|---------|

### Bugs Found
| ID | Feature | Severity | Layer | Root Cause |
|----|---------|----------|-------|------------|

### Performance
| Endpoint/Page | Time | Budget | Status |
|---------------|------|--------|--------|

### Documentation
| Type | File | Purpose |
|------|------|---------|

### Server Log Errors During Run
[Any errors in the backend logs]

### Things left unanswered
[Questions not answered — require next session]

### Verdict
[ ] ✅ SHIP
[ ] ⚠️ SHIP WITH MONITORING  
[ ] ❌ HOLD
```

---

## 14. REGRESSION REGISTRY {#registry}

```markdown
# REGRESSION REGISTRY — [PROJECT]
Skill: v3.2 | Updated: [date] | Health: [score]/100

## INVESTIGATION STATUS
| Feature | Investigation | Open Questions | Test Plan |
|---------|---------------|----------------|-----------|
| Auth | ✅ Complete | 0 | ✅ Ready |
| Blog | 🔍 In Progress | 3 | ⏳ Pending |

## FEATURES
| ID | Feature | Logic | API | E2E | a11y | Sec | Health | Last Run |
|----|---------|-------|-----|-----|------|-----|--------|----------|
| F001 | Auth | ✅ | ✅ | ✅ | ✅ | ✅ | 94/100 | [date] |

## BUGS
| ID | Feature | Severity | Layer | Status | Found | Fixed | Root Cause |
|----|---------|----------|-------|--------|-------|-------|------------|

## DISCOVERED CHECKLISTS STATUS
| Feature | Triggers Found | Covered | Coverage% |
|---------|----------------|---------|-----------|
```

---

## 15. CI/CD {#cicd}

```yaml
# .github/workflows/qa.yml
name: QA Pipeline v3.2

on:
  push:         { branches: [main, develop] }
  pull_request: { branches: [main] }

jobs:

  logic-tests:
    name: "Layer 0 — Business Logic"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run domain logic tests
        run: dotnet test tests/logic/ --logger trx
      - uses: actions/upload-artifact@v4
        with: { name: logic-results, path: TestResults/ }

  api-tests:
    name: "Layer 2 — Newman API"
    runs-on: ubuntu-latest
    needs: logic-tests
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g newman newman-reporter-htmlextra
      - run: |
          newman run tests/api/regression.collection.json \
            --environment tests/api/envs/ci.json \
            --reporters cli,htmlextra \
            --reporter-htmlextra-export evidence/testing/_reports/api/ci-report.html \
            --bail
      - uses: actions/upload-artifact@v4
        if: always()
        with: { name: api-report, path: evidence/testing/_reports/api/ }

  smoke-tests:
    name: "Layer 1 — Playwright Smoke"
    runs-on: ubuntu-latest
    needs: api-tests
    env:
      CI: 'true'
      BASE_URL: ${{ secrets.STAGING_URL }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npx playwright install --with-deps chromium firefox
      - run: npx playwright test tests/e2e/smoke.spec.ts --project=chromium
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: smoke-report
          path: |
            playwright-report/
            evidence/testing/screenshots/failures/
            evidence/testing/flows/
```

---

## 16. ACTIVATION PROMPTS {#prompts}

```
/qa-install      → First time in project (run the installer)
/qa-investigate  → Full Investigation Protocol for project or feature
/qa-questions    → Show open questions + request answers
/qa-plan         → Build Test Plan from Investigation results
/qa-smoke        → Playwright smoke only (P0 + critical UI)
/qa-api          → Full Newman for a specific feature
/qa-logic        → Layer 0 Business Logic tests
/qa-regression   → All layers (Logic + Newman + Smoke)
/qa-a11y         → Accessibility audit
/qa-security     → Security baseline
/qa-proof        → System Proof screenshots for feature
/qa-bug          → Document bug + before/after screenshots
/qa-report       → Generate Session Report + update Registry
```

---

## 17. MANDATORY OUTPUTS — Every Session {#outputs}

```
OUTPUT 1: Console Summary (with Health Score)
OUTPUT 2: evidence/investigation/[feature]-investigation.md
OUTPUT 3: tests/logic/[feature].tests.cs or .spec.ts (Layer 0)
OUTPUT 4: tests/api/[feature].collection.json (Newman — 6 folders)
OUTPUT 5: tests/e2e/smoke.spec.ts (updated)
OUTPUT 6: evidence/testing/screenshots/ (system-proof + failures only)
OUTPUT 7: REGRESSION-REGISTRY.md + ANALYTICS.md (updated)
```

### Console Summary Format

```
╔══════════════════════════════════════════════════════╗
║         QA MASTER v3.2 — SESSION REPORT              ║
╠══════════════════════════════════════════════════════╣
║ Project    : [name]                                  ║
║ Feature    : [feature]                               ║
║ Date       : [date]    Time: [time]                  ║
╠══════════════════════════════════════════════════════╣
║ 🔍 Investigation : ✅ Complete  │ Questions: 0 open  ║
╠══════════════════════════════════════════════════════╣
║ 🧠 Logic Tests   : XX passed / XX failed             ║
║ 🌐 API (Newman)  : XX passed / XX failed             ║
║ 🎭 E2E Smoke     : XX passed / XX failed             ║
║ ♿ a11y Issues   : X violations                      ║
║ 🛡️  Security      : X issues found                   ║
╠══════════════════════════════════════════════════════╣
║ 📸 System Proof  : X screenshots                     ║
║ 🎬 Failure Video : X recordings                      ║
╠══════════════════════════════════════════════════════╣
║ 🏥 HEALTH SCORE  : [XX]/100  [🟢 Excellent]          ║
╠══════════════════════════════════════════════════════╣
║ 🐛 BUGS FOUND    : X                                  ║
║    🔴 Critical: X  🟠 High: X  🟡 Medium: X          ║
╠══════════════════════════════════════════════════════╣
║ ❓ OPEN QUESTIONS: X (Must answer before next session)║
╠══════════════════════════════════════════════════════╣
║ VERDICT: ✅ SHIP / ⚠️ SHIP WITH MONITORING / ❌ HOLD ║
╚══════════════════════════════════════════════════════╝
```

---

## 18. FOLDER STRUCTURE {#structure}

```
[project-root]/
├── .agent/
│   ├── qa-config.json                     ← Edit immediately after install
│   ├── qa-install-log.md
│   └── skills/
│       └── qa-master.md                   ← Copy of this file
│
├── tests/
│   ├── logic/                             ← Layer 0 (NEW)
│   │   ├── [feature].state-machine.cs
│   │   ├── [feature].invariants.cs
│   │   ├── [feature].decision-table.cs
│   │   └── [feature].stories.cs
│   ├── e2e/
│   │   ├── smoke.spec.ts                  ← The only file (auth + critical UI)
│   │   └── helpers/
│   │       ├── screenshot.helper.ts
│   │       ├── auth.helper.ts
│   │       └── data.factory.ts
│   └── api/
│       ├── [feature].collection.json      ← 6 folders per feature
│       ├── regression.collection.json
│       └── envs/
│           ├── local.json
│           ├── staging.json
│           └── ci.json
│
├── evidence/
│   ├── investigation/                     ← (NEW)
│   │   ├── INVESTIGATION-TEMPLATE.md
│   │   └── [feature]-investigation.md
│   ├── testing/
│   │   ├── REGRESSION-REGISTRY.md        ← Never delete this
│   │   ├── ANALYTICS.md
│   │   ├── _reports/
│   │   │   ├── api/
│   │   │   └── playwright/
│   │   └── screenshots/
│   │       ├── system-proof/              ← One picture per interface
│   │       │   └── [feature]-working-[ts].png
│   │       ├── failures/                  ← On failure only
│   │       │   └── BUG-[ID]/
│   │       │       ├── before-[ts].png
│   │       │       ├── after-[ts].png
│   │       │       └── diff-notes.md
│   │       └── flows/                     ← Journey video
│   │           └── [story]-journey.webm
│   └── architecture-decisions/
│
└── .github/
    └── workflows/
        └── qa.yml
```

---

## CHANGELOG

| Version | Date | Key Changes |
|---------|------|-------------|
| v1.0 | — | Initial Playwright skill |
| v2.0 | — | + Newman, Registry, Observability, Performance |
| v3.0 | — | + Self-Install, a11y, Security, RTL, Health Score, CI/CD |
| v3.1 | — | + Screenshot System, P8/P9, DB Verification, Memory Leak |
| v3.2 | 2025 | + Detective Mode, Investigation Protocol, Smart Questions, Layer 0 Business Logic, Newman as backbone, Playwright for Smoke only, Documentation Outcomes-Only, Discovered Checklists, **Feature DNA (8 dimensions for any unknown feature)** |