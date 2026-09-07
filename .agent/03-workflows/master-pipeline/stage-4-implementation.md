# Master Pipeline — Stage 4: Implementation

> This is stage 4 of 8. Next: `stage-5-testing.md`
> Required for: 🟢 🟡 🔴 (all classifications)

---

## Decision Gate

```yaml
gate:
  stage_number: 4
  stage_name: "Implementation"
  classification_required: [🟢, 🟡, 🔴]
  previous_stage_status: passed       # previous required stage must pass
  requires:
    - 🟢: completed intake (stage 0)
    - 🟡: approved specs (stage 1)
    - 🔴: approved architecture + threat model (stages 2-3)
  resources_loaded:
    - "⚠️ MANDATORY: read 05-references/books/00-master-index.md → Stage 4 row"
    - constitutions: arch-constitution + ddd-constitution + perf-constitution + security-constitution
    - 02-rules/architecture-and-design.md (if architecture task)
    - 02-rules/database-performance.md (if DB task)
    - 02-rules/network-and-api.md (if API task)
    - prompts: backend-prompts.md (if .NET) | frontend-prompts.md (if Angular)
    - templates: entity-pattern.md + standards.md (if ABP project)
    - wiring-registry → relevant REF contracts
  decision: proceed
```

---

## Task: code implementation in MVP increments

### 4.1 — Vertical Slice Execution

```
□ For each task from the approved plan:
  1. Load the relevant rule file from wiring-registry (one at a time)
  2. Implement as a vertical slice covering all applicable layers:
     Database → Domain → Application → API → Frontend → UI/UX → Tests
  3. Cite applied REF contracts in code comments:
     e.g. // [REF-DB-N1]: prevent N+1 query
          // [REF-ARCH-DEP]: one-way dependency flow

□ Follow 02-rules/vertical-slice-governance.md for the mandatory coverage report
```

### 4.2 — Incremental Delivery

```
□ After each increment:
  - Run available local tests (unit, lint, type-check)
  - Fix failures before moving to the next increment
  - Do NOT batch all implementation then test at the end

□ If tests are unavailable:
  - Record NOT_AVAILABLE — never claim passing without evidence
  - Proceed to stage 5 for formal testing
```

### 4.3 — Code Quality Checks

```
□ Before exiting stage 4:
  - Verify no TODO/FIXME items left unresolved (or explicitly deferred with reason)
  - Verify all files follow project conventions (04-memory/project-knowledge.md)
  - Run formatter/linter if available

□ Apply learned mistakes from 04-memory/learned-mistakes.md
```

### 4.4 — Self-Assessment (no hard stop — informational)

```
□ Produce a brief implementation summary:
  - Files created/modified (with line references)
  - REF contracts applied
  - Known limitations or deferred items
  - Ready for testing gate: yes | no (with blockers)
```

---

## Resource Injection (from wiring-registry)

| Resource | When |
|----------|------|
| `02-rules/architecture-and-design.md` | Module creation / CRUD / architecture |
| `02-rules/database-performance.md` | Database queries / migrations |
| `02-rules/security-checklist.md` | Auth / security-sensitive code |
| `02-rules/network-and-api.md` | API endpoints / network calls |
| Grep relevant `REF-*` contracts | Per capability from wiring-registry |

---

## Gate Output

```yaml
gate_result:
  stage: 4
  status: ✅ GATE PASSED | ⛔ GATE FAILED | ⛔ NEEDS CLARIFICATION
  increments_completed: 0
  increments_total: 0
  files_created: []
  files_modified: []
  ref_contracts_applied: []
  local_tests_passed: true | false | not_available
  next_stage: 5
  blockers: []
```

> After gate passes → update `active-tasks.md` with completed increments.
