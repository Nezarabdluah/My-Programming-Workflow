# 📇 INDEX.md — Smart Index for AOS v7.0

> Search here first. Every file is listed with its description — complete structural coverage.

## 🔑 Entry Point & Sync
| File | Description |
|------|-------------|
| `AGENTS.md` | Master directive contract: session boot, SDD workflow, REF rules, handoff protocol |
| `VERSION` | Version number, last sync date, and source path |

## 🏛️ 01-core/ — Core (mandatory at session start)
| File | Description |
|------|-------------|
| `operating-contract.md` | Operational contract: conflict priority, dependency rules, policy engine, SDD, vertical-slice charter, mistake learning |
| `session-prompt.md` | Unified session prompt: boot & matching, proof-of-read, task routing (Paths A/B/C), REF wiring, handoff, closeout |
| `task-classification.md` | 🟢/🟡/🔴 classification indicators, keywords, scope, and the Zero-Trust escalation rule |
| `token-budget.md` | Token budget and selective loading policy (≤ 400 lines/session) |
| `collaboration-rules.md` | Pair-programming protocol: Driver/Navigator roles, step & proof, stop gates, response structure |
| `wiring-registry.md` | ⭐ Central DI container: capability → rule file → REF contracts → grep-only reference anchors |

## 📐 02-rules/ — Specialized Rules (conditionally loaded, ONE at a time)
| File | Description |
|------|-------------|
| `architecture-and-design.md` | Clean Architecture dependency rule, DDD (Aggregates, Value Objects, Events), SOLID review checklist |
| `database-performance.md` | Query design, pagination, N+1 prevention, SARGability, indexing, document DBs, resource disposal |
| `security-checklist.md` | JWT/session security, IDOR defense, injection & XSS prevention, boundary validation |
| `testing-and-quality.md` | Test strategy (behavior over implementation), structured logging, tracing, resilience, pre-delivery checklist |
| `network-and-api.md` | Payload optimization, chunky-vs-chatty, evidence-based diagnosis, API design best practices |
| `vertical-slice-governance.md` | **Full-Stack Vertical Slice Charter — 7 layers + mandatory coverage report (fixed, Project-Agnostic)** |

## 🔄 03-workflows/ — Workflows (Markdown-driven)
| File | Description |
|------|-------------|
| `init-project.md` | One-time workflow: linking a new project to AOS (structure copy, 04-memory init, VERSION) |
| `start-session.md` | Session start protocol: context continuity and version sync |
| `end-session.md` | Session end protocol: memory save, **governance enforcement gate (pre-Done)**, and handoff summary export |
| `requirements-analysis.md` | Requirements analysis and SDD spec drafting (Draft → Clarify → Approved) with user stories — supports **Given/When/Then and EARS** notation |
| `create-backend-module.md` | Full backend module guide (Domain → Application → Infrastructure → API → Tests) |
| `create-frontend-module.md` | Frontend component/screen guide and independence rules |
| `debug-common-errors.md` | Evidence-first error diagnosis with root-cause search and common error patterns |
| `improve-user-experience.md` | UI/UX review and improvement workflow (interaction, visual, accessibility) |
| `knowledge-bootstrapping.md` | Knowledge exploitation for existing projects: codebase map, test automation, DevOps hooks |
| `qa-strategy.md` | **QA strategy**: test pyramid, strategy selection by classification, test plan template, quality gate criteria |
| `production-readiness.md` | **PRR scorecard**: 10-dimension production readiness assessment with graduated scoring |

### Sub-workflows (coordinator + step files — load ONE step at a time):
| Directory | Description |
|-----------|-------------|
| `master-pipeline/` | **⭐ Master Pipeline (Path D)**: coordinator + stages 0-8 (Intake → Requirements → Architecture → Threat Model → Implementation → Testing → PRR → Deployment → Post-Launch) with YAML decision gates, hard stop-gate tags, DoD ladder by classification (🟢 mini / 🟡 1,4,5 / 🔴 all 0-8) |
| `mobile-qa/` | Mobile QA: coordinator + steps 1-3, 7 (environment discovery, build verification, scenario execution, evidence report) |
| `security-gate/` | Security gate: coordinator + steps 1-7 (threat model, dependency check, secret scan, access review, code review, test verification, gate report) |

## 🧠 04-memory/ — Cumulative Contextual Memory
| File | Description |
|------|-------------|
| `project-context.md` | Last project state, session state, critical alerts |
| `learned-mistakes.md` | Active mistakes log (max 20, newest on top) |
| `active-tasks.md` | Active/pending tasks with SDD states |
| `decisions.md` | Architectural decision log (ADRs) |
| `project-knowledge.md` | Discovered code patterns and project conventions |
| `codebase-map.md` | Discovered file/structure map |
| `mistakes-archive.md` | Historical/archived mistakes |

## 📚 05-references/ — References (Grep-Only, never read in full)
| File/Directory | Description |
|----------------|-------------|
| `engineering-rules-catalog-REF.md` | The 34 `[REF-*]` directives in 8 categories (ARCH×7, DB×7, SEC×5, NET×5, TEST×2, OBS×2, RES×1, AI×1) |
| `books/00-master-index.md` | **⭐ Resource Injection Matrix** — maps ALL AOS resources to ALL pipeline stages with MUST/SHOULD/IF injection modes |
| `books/constitutions/` | **6 actionable constitution files** extracted from 16 engineering books (arch, ddd, security, perf, resilience, integration) |
| `books/engineering-books-16-distilled.txt` | 16 distilled books (archive — educational content, grep by lesson number or keyword) |
| `prompts/` | Ready-made optimized prompts: `backend-prompts.md`, `frontend-prompts.md`, `debugging-prompts.md` |
| `qa-testing/qa-testing-strategy-and-automation.md` | QA strategy + automation (11 `[QA-*]` anchors) |
| `devops-ops/devops-enterprise-and-production-readiness.md` | DevOps + security + performance + monitoring (18 `[OPS-*]` anchors) |

## 📦 06-templates/ — Project Templates (loaded only during project init)
| Directory | Description |
|-----------|-------------|
| `dotnet-abp/` | Optional .NET/ABP plugin: entity-pattern, standards, persona, prompts, PR template, pre-commit config, GitHub security gate |
| `claude-skills/` | Full git copy of a skills library — **reference only; never load, never index its internals** |

## 🏛️ adr/ — Architecture Decision Records
| File | Description |
|------|-------------|
| `adr-template.md` | ADR template (context, decision, rejected alternatives, consequences) |

## ⚙️ governance/ — Deterministic Enforcement (Python)
| File | Description |
|------|-------------|
| `runner.py` | Governance runner — the ground-truth executable check |
| `test_memory.py`, `test_rules.py`, `test_state.py` | Governance test suite |
