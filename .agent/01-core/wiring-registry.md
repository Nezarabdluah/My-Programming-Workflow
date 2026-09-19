---
id: core-wiring-registry
description: Central declarative wiring manifest — maps each active capability to its rule file, REF contracts, and grep-only reference anchors. The single source of truth for dependency injection.
alwaysApply: false
globs: []
requires: []
---

# Wiring Registry — Capability & Resource Registry (AOS v8.0.0-rc.1)

> **How this works**: every capability row below declares its dependencies **by ID** (declarative wiring).
> Resolution is **lazy** — load a resource only at the moment its capability becomes active.
> Direction is **one-way** — consumers know their dependencies; resources never know their consumers (REF-ARCH-DEP applied to the knowledge system itself).

## Resolution procedure (ADR-007 / ADR-008)

The executable source of truth is `01-core/context-map.json`; this Markdown file documents the capability model for humans. The broker combines explicit Task Contract capabilities with generic risk-derived capabilities from the Context Map and project-specific affected-area rules from `profiles/project.json`.

Manual fallback only when the executable broker is unavailable:
1. Identify the capability or capabilities materially affected by the task.
2. Use the matching row below to discover available resources.
3. Load at most ONE directly relevant rule file at a time.
4. Grep only the specific reference anchor needed for the current decision.
5. Load constitutions/templates/prompts/book lessons only when they materially change or verify the decision.
6. Record relevant compliance in task evidence/reports. Production-source REF/CONST comments are optional.
7. For lifecycle stages, use `books/00-master-index.md` as an index, not an unconditional loading mandate.

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
| Affected-area completeness | project/profile-defined evidence | — | — | — |
| Full-stack vertical-slice coverage (when activated) | `02-rules/vertical-slice-governance.md` | — | — | — |
| Production readiness | `03-workflows/production-readiness.md` | — | `resilience-constitution.md` | devops: `[OPS-PRR]`, `[OPS-SCORECARD]` |
| Deployment / rollback | `stage-7-deployment.md` | — | `resilience-constitution.md` | devops: `[OPS-ROLLBACK]` |
| Post-launch metrics | `stage-8-post-launch.md` | — | `perf-constitution.md` | devops: `[OPS-DORA]` |
| QA automation | `03-workflows/qa-strategy.md` | — | — | qa: `[QA-DETECTIVE]`, `[QA-E2E-SMOKE]` |

> **Constitution path prefix**: `05-references/books/constitutions/`
> **Prompts**: `backend-prompts.md`, `frontend-prompts.md`, `debugging-prompts.md` in `05-references/prompts/`
> **Templates**: `06-templates/` contains optional starting points. Validate each template against the project stack/profile before use.

## Capability Resource Sets (formerly Knowledge Bundles)

> Each set lists resources that may help with a capability. Do **not** load the entire set by default.
> Select the minimum relevant subset based on the task, project architecture, and evidence needed.

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

## Lifecycle Resource Index (Master Index)
For the **stage-by-stage resource index** (what may be relevant at each pipeline stage), see:
→ **`05-references/books/00-master-index.md`**

ADR-007/ADR-008 govern runtime selection: load only broker-selected resources. Legacy injection labels in reference documentation are descriptive migration metadata only.

## Registry discipline
- `01-core/context-map.json` is the executable capability→resource source of truth; this file is its human-readable catalog.
- Adding a REF category, constitution, or anchor requires updating this registry.
- Constitution files = extracted actionable rules from 16 engineering books (see `books/constitutions/`).
