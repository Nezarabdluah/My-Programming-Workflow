---
id: rules-vertical-slice
description: Full-Stack Vertical Slice Charter — the 7 mandatory layers and the binding coverage-report format. Load for every 🟡/🔴 feature task; overrides other rules on completeness assessment.
alwaysApply: false
globs: []
requires: []
---

# Full-Stack Vertical Slice Governance

> **Status**: fixed binding rule — applies to every project and every Feature/Use-Case regardless of stack.
> **Priority**: higher than the other 02-rules when assessing task completeness. Any "done" report without explicit coverage of the seven layers = rejected.
> **Reference**: `AGENTS.md § Sequential SDD Workflow` + `operating-contract.md § 4`

---

## 1. Core Rule — Vertical Slice Definition

Every Feature / Use-Case = a **full vertical slice**, not a single layer.

Before calling any task `Done`, every one of the following seven layers must be covered — or its non-applicability explicitly justified:

| # | Layer | What "covered" means | When "not applicable" |
|---|-------|----------------------|------------------------|
| 1 | **Database — Schema/Migration** | Migration + Indexes + Constraints + Seeds if needed | Feature never touches data persistence at all (e.g. static UI text with no storage) — with a line-level justification |
| 2 | **Domain Layer — Aggregate/Entity/Value Object + Domain Rules** | Aggregate Root + Entities + immutable Value Objects + protected Invariants + Domain Events if needed | No business logic at all (rare) — with justification |
| 3 | **Application Layer — Application Service + DTOs + Validation** | Service + DTOs + Validation + Mapping + Orchestration with no Infrastructure leakage | — |
| 4 | **API Contract — Endpoint + Authorization + Error Handling** | Documented endpoint + Authorization/Policy + unified error codes + rate limiting if needed | Internal feature never exposed via API (e.g. internal cron) — with justification |
| 5 | **Frontend — Component + State Management** | Component(s) + State (Redux/Zustand/Context/Query) + Data fetching + Error/Loading states | Pure backend feature with no UI — with justification |
| 6 | **UI/UX & Animation — Design-system consistency** | Complies with the existing design system; no new style without a justifying ADR + consistent animations/transitions + A11y | — |
| 7 | **Tests — Unit + Integration per actually-touched layer** | Unit for Domain/Application + Integration for API/DB + Frontend component/e2e per covered layers | Never — a "done" layer left untested is forbidden |

> **Forbidden**: filing a "done" report while silently skipping a layer without an explicit `not applicable because...` or `deferred because...` justification.

---

## 2. Application Mechanics in SDD

* **Draft/Clarify**: determine whether each layer applies, and record the initial assumption in `active-tasks.md`.
* **Planning**: split the plan into vertical increments (each increment crosses the applicable layers), never horizontal slicing (DB first, then Domain, then API).
* **Ready Gate**: do not enter `Executing` without an approved initial coverage table.
* **Executing**: build vertically — Migration → Domain → Application → API → Frontend → UI/UX → Tests within the same slice.
* **Validating/Done**: do not close the task without the **mandatory coverage report** (Section 3 below). The reviewer rejects the PR if the report is missing.

---

## 3. Mandatory Report/Summary Format

Every completion report (PR description, session summary, handoff) must contain, verbatim, in this order:

### 3.1 Slice coverage table

```markdown
| Layer | Status | Evidence/Path |
|-------|--------|---------------|
| 1. Database | done / not applicable because... / deferred because... | `path/to/migration:line` |
| 2. Domain Layer | ... | `path/to/aggregate:line` |
| 3. Application Layer | ... | `path/to/service:line` |
| 4. API Contract | ... | `path/to/controller:line` |
| 5. Frontend | ... | `path/to/component:line` |
| 6. UI/UX & Animation | ... | `path/to/style:line` |
| 7. Tests | ... | `path/to/test:line` |
```

* `done` = with a file:line link.
* `not applicable because...` = at least one justifying sentence.
* `deferred because...` = with a follow-up task ID in `active-tasks.md`.

### 3.2 Architectural decisions taken

For each decision:
`[decision] ← [rejected alternative and why] ← [principle: DDD/SOLID/ABP/REF-xxx]`

Example:
`Single Aggregate Root for Order ← rejected a Service injecting DbContext directly because it breaks D ← DDD Aggregate + DIP`

### 3.3 Judgment calls & deviations from established patterns

Any decision taken without a pre-documented rule in `02-rules/` or `05-references/engineering-rules-catalog-REF.md`:
* State it explicitly with `file_path:line_number`
* Even at 100% confidence — do not hide it
* Classify it: `project-specific judgment ← record in learned-mistakes.md (Type B)` or `missing general rule ← propose in 02-rules/ (Type C)`

### 3.4 Needs human/architectural review before sign-off

Nominate at least one item yourself from:
* Aggregate boundaries
* Cross-cutting concerns (logging, caching, transactions)
* Authorization logic / IDOR / OWASP
* Breaking migration / data-loss risk

> Do not grade everything the same — flag what is critical.

---

## 4. Compliance & Verification Rules

* **REF**: cite in code: `// [REF-ARCH-xxx]` for architecture, `// [REF-DB-xxx]` for performance, `// [REF-SEC-xxx]` for security.
* **Clean Code**: every layer respects `testing-and-quality.md` (function ≤ 20 lines, unit ≤ 200 lines).
* **YAGNI**: never build a layer "just in case" — if not applicable, justify; don't pile up dead code.
* **AOS Sync**: this charter is read at the start of every session via `01-core/operating-contract.md § 5` and auto-loaded for any 🟡 or 🔴 task.

---

## 5. Violation Penalty

* A report without the coverage table = **automatically rejected** and returned to the `Validating` stage.
* A silenced layer = considered `not done` until proven otherwise.
* Never move to a new task before your report is complete and truthful — even if it takes extra time.

---

## 6. Change Tracking

* Initial version: 2026-08-30 — charter adopted as a fixed Project-Agnostic rule.
* Any later change requires an ADR in `04-memory/decisions.md` and Navigator approval.
