# Master Pipeline — Stage 1: Requirements & Specs

> This is stage 1 of 8. Next: `stage-2-architecture.md`
> Required for: 🟡 🔴 | Skipped for: 🟢

---

## Decision Gate

```yaml
gate:
  stage_number: 1
  stage_name: "Requirements & Specs"
  classification_required: [🟡, 🔴]
  previous_stage_status: passed       # stage 0 must pass
  requires:
    - completed intake (stage 0)
    - developer-provided feature description or user request
  context_candidates:
    - 03-workflows/requirements-analysis.md
    - ddd-constitution.md (only if domain language/bounded contexts materially apply)
    - 02-rules/vertical-slice-governance.md (only if an activated full-stack profile uses it)
  decision: proceed | skip

# Skip condition: classification = 🟢
#   → ⛔ GATE SKIPPED — classification 🟢 does not require formal specs
```

---

## Task: draft requirements and obtain approval — SDD workflow

### 1.1 — Requirements Analysis

```
□ Load and follow 03-workflows/requirements-analysis.md
□ Draft the feature specification:
  - Feature name and description
  - User stories with acceptance criteria (Given/When/Then or EARS notation)
  - Non-functional requirements (performance, security, accessibility)
  - Out-of-scope items (explicit exclusions)
□ Save to specs/[feature-name].md
```

### 1.2 — Task Decomposition

```
□ Break the feature into independently testable MVP increments
□ Prefer independently valuable/testable vertical increments when appropriate to the project architecture
□ Identify the actual affected project areas; do not invent layers solely to satisfy a generic checklist
□ Save the implementation plan to specs/[feature-name].plan.md
□ Save the task list to specs/[feature-name].tasks.md
```

### 1.3 — Developer Approval Gate

```
⏸️ HARD STOP — present specs and plan to the developer for approval.

□ Print the spec summary and task breakdown
□ Wait for explicit approval before proceeding

  Developer approves → ✅ GATE PASSED
  Developer requests changes → revise and re-present
  Developer rejects → ⛔ GATE FAILED — record reason, return to Draft
```

---

## Context Expansion (selective)

| Resource | When |
|----------|------|
| `03-workflows/requirements-analysis.md` | Stage workflow |
| `02-rules/vertical-slice-governance.md` | Only when the project/profile activates full-stack vertical-slice guidance |

---

## Gate Output

```yaml
gate_result:
  stage: 1
  status: ✅ GATE PASSED | ⛔ GATE FAILED | ⛔ NEEDS CLARIFICATION
  specs_path: "specs/[feature-name].md"
  plan_path: "specs/[feature-name].plan.md"
  tasks_path: "specs/[feature-name].tasks.md"
  developer_approved: true | false
  next_stage: 2 | 4                  # 2 if 🔴, 4 if 🟡
  blockers: []
```

> After gate passes → update `active-tasks.md` with approved spec references.
