# Master Pipeline — Stage 0: Intake & Classification

> This is stage 0 of 8. Next: `stage-1-requirements.md`
> Required for: 🟢 🟡 🔴 (all classifications)

---

## Decision Gate

```yaml
gate:
  stage_number: 0
  stage_name: "Intake & Classification"
  previous_stage: none              # this is the first stage
  requires:
    - a project directory or description from the developer
  resources_loaded: []              # no specialized resources needed
  decision: proceed
```

> If no project information is provided ← `⛔ NEEDS CLARIFICATION` immediately.

---

## Task: project intake and classification — discovery only, no code changes

### 0.1 — Project Discovery

```
□ Identify the project type:
  - Existing codebase → scan for stack markers (package.json, *.csproj, requirements.txt, go.mod, etc.)
  - New project → ask the developer for stack choice and constraints

□ Record in the handoff contract:
  - project name
  - detected/chosen stack
  - repository state (new / existing / monorepo)
```

### 0.2 — Task Classification

```
□ Classify the incoming task using 01-core/task-classification.md:

  🟢 Simple — single file, cosmetic, < 1 hour
  🟡 Medium — multi-file, requires specs, testable feature
  🔴 Sensitive — auth, payments, data deletion, architecture change,
                 multi-service, production deployment

□ Apply Zero-Trust Escalation Rule:
  If ANY doubt about classification → escalate one level (never downgrade)
```

### 0.3 — DoD Ladder Assignment

```
□ Based on classification, declare the required stages:

  🟢 → stages 0, 4, 5
  🟡 → stages 0, 1, 4, 5
  🔴 → stages 0–8 (all)

□ Record the ladder in the handoff contract
```

### 0.4 — Knowledge Bootstrapping (existing projects only)

```
□ If the project has existing code:
  - Execute 03-workflows/knowledge-bootstrapping.md
  - Map discovered patterns to 04-memory/project-knowledge.md
  - Identify existing test infrastructure

□ If the project is new:
  - Skip — record ⛔ GATE SKIPPED — new project, no existing code
```

---

## Gate Output

```yaml
gate_result:
  stage: 0
  status: ✅ GATE PASSED | ⛔ GATE FAILED | ⛔ NEEDS CLARIFICATION
  classification: 🟢 | 🟡 | 🔴
  required_stages: [0, 4, 5] | [0, 1, 4, 5] | [0, 1, 2, 3, 4, 5, 6, 7, 8]
  stack: ""
  next_stage: 1 | 4                  # depends on classification
  blockers: []
```

> After gate passes → update `active-tasks.md` with classification and next stage.
