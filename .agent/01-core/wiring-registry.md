---
id: core-wiring-registry
description: Central declarative wiring manifest — maps each active capability to its rule file, REF contracts, and grep-only reference anchors. The single source of truth for dependency injection.
alwaysApply: false
globs: []
requires: []
---

# Wiring Registry — Central Dependency Injection Container (AOS v7.0)

> **How this works**: every capability row below declares its dependencies **by ID** (declarative wiring).
> Resolution is **lazy** — load a resource only at the moment its capability becomes active.
> Direction is **one-way** — consumers know their dependencies; resources never know their consumers (REF-ARCH-DEP applied to the knowledge system itself).

## Resolution procedure (Mandatory Injection)
1. Find your capability row below.
2. Load the **constitution** (L4-C) — actionable rules from 16 engineering books.
3. Load the **rule file** (L3) — one file at a time, never two.
4. Grep the **reference anchor** (L4) inside the named file — **never read the full file**.
5. Cite applied contracts in code comments, e.g. `// [REF-DB-N1]: prevent N+1 query`.
6. For full stage-by-stage resource mapping, see **`books/00-master-index.md`** (Resource Injection Matrix).

## Capability → Dependency Map

| Capability (when active) | Rule file (L3) | REF contracts | Constitution (L4-C) | Reference anchors (L4) |
|--------------------------|----------------|---------------|---------------------|------------------------|
| Architecture / DDD / modules | `02-rules/architecture-and-design.md` | `REF-ARCH-*` | `arch-constitution.md` + `ddd-constitution.md` | books: grep `Aggregate`, `SOLID` |
| Database / queries / performance | `02-rules/database-performance.md` | `REF-DB-*` | `perf-constitution.md` | devops: `[OPS-DBPERF]` |
| Security / auth / authorization | `02-rules/security-checklist.md` | `REF-SEC-*` | `security-constitution.md` | devops: `[OPS-SECTEST]`, `[OPS-OWASP10]` |
| Testing / quality gate | `02-rules/testing-and-quality.md` | `REF-TEST-*` | `security-constitution.md` (audit) + `perf-constitution.md` | qa: `[QA-PYRAMID]`, `[QA-UNIT]` |
| Observability / logging | `02-rules/testing-and-quality.md` §2 | `REF-OBS-*` | — | devops: `[OPS-OBSERVABILITY]` |
| Resilience / concurrency | `02-rules/testing-and-quality.md` §3 | `REF-RES-*` | `resilience-constitution.md` | — |
| API / network / latency | `02-rules/network-and-api.md` | `REF-NET-*` | `integration-constitution.md` | devops: `[OPS-K6]` |
| Context budget / sessions | `01-core/token-budget.md` | `REF-AI-*` | — | — |
| Feature completeness (🟡/🔴) | `02-rules/vertical-slice-governance.md` | — | — | — |
| Production readiness | `03-workflows/production-readiness.md` | — | `resilience-constitution.md` | devops: `[OPS-PRR]`, `[OPS-SCORECARD]` |
| Deployment / rollback | `stage-7-deployment.md` | — | `resilience-constitution.md` | devops: `[OPS-ROLLBACK]` |
| Post-launch metrics | `stage-8-post-launch.md` | — | `perf-constitution.md` | devops: `[OPS-DORA]` |
| QA automation | `03-workflows/qa-strategy.md` | — | — | qa: `[QA-DETECTIVE]`, `[QA-E2E-SMOKE]` |

> **Constitution path prefix**: `05-references/books/constitutions/`
> **Prompts**: `backend-prompts.md`, `frontend-prompts.md`, `debugging-prompts.md` in `05-references/prompts/`
> **Templates**: `06-templates/` (entity-patterns, coding-standards, pre-commit-template, github-security-gate, pull_request_template) — universal, stack-agnostic

## Knowledge Bundles (AppBundling)

> Each bundle groups ALL related resources (constitution + rules + templates + prompts + book references)
> for a specific capability. Load the ENTIRE bundle when the capability is active.

### Bundle: DB Performance
```
├── 05-references/books/constitutions/perf-constitution.md     (11 rules)
├── 02-rules/database-performance.md                           (7 REF-DB rules)
├── 05-references/engineering-rules-catalog-REF.md             (grep REF-DB-*)
├── 05-references/prompts/backend-prompts.md                   (DB sections)
├── 06-templates/entity-patterns.md                            (query patterns)
└── 05-references/books/engineering-books-16-distilled.txt     (grep "Lesson 5", "Lesson 10")
```

### Bundle: Security
```
├── 05-references/books/constitutions/security-constitution.md (17 rules)
├── 02-rules/security-checklist.md                             (5 REF-SEC rules)
├── 05-references/engineering-rules-catalog-REF.md             (grep REF-SEC-*)
├── 06-templates/github-security-gate.yml                      (CI/CD security)
├── 06-templates/pull_request_template.md                      (PR security gate)
└── 05-references/devops-ops/devops-enterprise-and-production-readiness.md (grep [OPS-SECTEST])
```

### Bundle: Architecture & DDD
```
├── 05-references/books/constitutions/arch-constitution.md     (15 rules)
├── 05-references/books/constitutions/ddd-constitution.md      (11 rules)
├── 02-rules/architecture-and-design.md                        (7 REF-ARCH rules)
├── 05-references/engineering-rules-catalog-REF.md             (grep REF-ARCH-*, REF-MOD-*)
├── 06-templates/entity-patterns.md                            (entity design)
├── 06-templates/coding-standards.md                           (SOLID, DDD, encapsulation)
└── 05-references/books/engineering-books-16-distilled.txt     (grep "Lesson 1", "Lesson 7")
```

### Bundle: Resilience & Concurrency
```
├── 05-references/books/constitutions/resilience-constitution.md (15 rules)
├── 02-rules/testing-and-quality.md §3                         (REF-RES-*)
├── 05-references/engineering-rules-catalog-REF.md             (grep REF-RES-*)
└── 05-references/books/engineering-books-16-distilled.txt     (grep "Lesson 8", "Lesson 11")
```

### Bundle: API & Integration
```
├── 05-references/books/constitutions/integration-constitution.md (10 rules)
├── 02-rules/network-and-api.md                                (5 REF-NET rules)
├── 05-references/engineering-rules-catalog-REF.md             (grep REF-NET-*)
├── 05-references/prompts/backend-prompts.md                   (API sections)
└── 05-references/devops-ops/devops-enterprise-and-production-readiness.md (grep [OPS-K6])
```

### Bundle: Testing & Quality
```
├── 05-references/books/constitutions/security-constitution.md (audit section)
├── 05-references/books/constitutions/perf-constitution.md     (performance audit)
├── 02-rules/testing-and-quality.md                            (REF-TEST-*)
├── 05-references/engineering-rules-catalog-REF.md             (grep REF-TEST-*)
├── 05-references/qa-testing/qa-testing-strategy-and-automation.md (grep QA-*)
├── 03-workflows/qa-strategy.md                                (test strategy)
└── governance/runner.py                                       (GOV-T11)
```

### Bundle: Production Readiness
```
├── 05-references/books/constitutions/resilience-constitution.md
├── 03-workflows/production-readiness.md                       (10-dimension PRR)
├── 05-references/devops-ops/devops-enterprise-and-production-readiness.md (grep OPS-*)
└── 05-references/engineering-rules-catalog-REF.md             (grep REF-OPS-*)
```

## Resource Injection Matrix (Master Index)
For the **full stage-by-stage mandatory resource map** (what to load at each pipeline stage), see:
→ **`05-references/books/00-master-index.md`**

Injection modes: **MUST** = gate blocked | **SHOULD** = recommended | **IF** = conditional on stack/context

## Registry discipline
- This file is the **only** place where capability→dependency wiring is defined ("point, don't copy").
- Adding a REF category, constitution, or anchor requires updating this registry.
- Constitution files = extracted actionable rules from 16 engineering books (see `books/constitutions/`).
