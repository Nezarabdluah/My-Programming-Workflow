# 📋 Requirements Analysis — SDD Spec Drafting Workflow

> **Contract**: used at the start of 🟡 medium and 🔴 sensitive features to draft precise specifications before writing any code.

---

## 🚦 Requirements State Machine & Policy Transitions
This workflow moves through 3 mandatory states:
`Draft (feature draft) ──► Clarify (mutual clarification) ──► Approved (technical sign-off)`

### ⚡ Policy Engine Evaluation:
Before moving to the `Approved` state, run the policy engine and apply the mandatory checks:
* **🔴 Sensitive**: enforce the approved `ADR-001` specification policy, write an architectural decision record, and activate security gates.
* **🟡 Medium**: enforce the `Clean Code Audit` policy and prepare automated tests.

---

## 📝 Step 1: Drafting (Draft State)
Prepare the initial spec file in `specs/[feature-name].md` with this structure:

### 1. Overview
* **Problem**: [what is the functional problem?]
* **Proposed solution**: [how does this code solve it?]
* **Target user**: [the benefiting party or user]

### 2. Independently Testable, Prioritized User Stories
Break requirements into prioritized user stories (P1, P2...) where each story is **independently implementable and testable as an MVP**:

* **User Story 1 (Priority: P1) - [Title]**:
  - As a [user type], I want [action] so that [value].
  - **P1 priority rationale**: [why is this the feature's core?]
  - **Independent verification step**: [how do we test it alone to confirm value delivery?]
  - **Acceptance criteria (Acceptance Scenarios)** — use **either** Given/When/Then **or** EARS notation:
    - Given/When/Then: `Given [initial state] → When [action] → Then [expected outcome]`
    - EARS: `WHEN [trigger] THE SYSTEM SHALL [behavior]`
    - EARS variants:
      - Ubiquitous: `THE SYSTEM SHALL [behavior]` (always true)
      - Event-driven: `WHEN [event] THE SYSTEM SHALL [response]`
      - State-driven: `WHILE [state] THE SYSTEM SHALL [behavior]`
      - Optional: `WHERE [feature is included] THE SYSTEM SHALL [behavior]`
      - Unwanted: `IF [unwanted condition] THEN THE SYSTEM SHALL [countermeasure]`

* **User Story 2 (Priority: P2) - [Title]**:
  - As a [user], I want [action] so that [goal].
  - **Acceptance criteria**:
    1. **Given** -> **When** -> **Then** *(or EARS notation above)*

---

## 🔍 Step 2: Clarification & Gap Closing (Clarify State)
1. **Ambiguity scan**: analyze the spec draft for vague requirements and uncovered edge cases.
2. **Ask questions**: compile a list of specific, targeted questions for the developer (Navigator).
3. **Update the spec**: once the developer answers, merge the answers into the written spec file.

---

## 🤝 Step 3: Approval & Crossing (Approved State)
1. The developer reviews the final spec file.
2. Upon the developer's approval, move the state in `04-memory/active-tasks.md` to `Approved`.
3. Update the decision log `04-memory/decisions.md` with any agreed technical decisions.
4. Move immediately to the architectural planning and task-breakdown path.
