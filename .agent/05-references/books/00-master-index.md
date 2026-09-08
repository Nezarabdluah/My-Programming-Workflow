# AOS Resource Injection Matrix
<!-- This is the SINGLE SOURCE OF TRUTH mapping ALL AOS resources to ALL pipeline stages -->
<!-- Every stage MUST consult this file to know what to load, grep, and cite -->
<!-- Status: MUST = gate blocked without it | SHOULD = recommended | IF = conditional -->

---

## How to Use This File

When executing any pipeline stage, the model MUST:
1. Read this file's section for the current stage
2. Load every MUST resource and cite it in code/docs
3. Check every IF condition and load if matched
4. Produce a Resource Utilization Summary before marking the stage as Done

---

## Stage 0: Intake & Classification

| Resource | Path | Action | Injection |
|----------|------|--------|-----------|
| Operating Contract | `01-core/operating-contract.md` | Read §0 (task classification) | MUST |
| Session Prompt | `01-core/session-prompt.md` | Read to select Path A/B/C/D | MUST |
| Wiring Registry | `01-core/wiring-registry.md` | Resolve capability → rule → REF → constitution | MUST |

---

## Stage 1: Requirements & Specs (SDD)

| Resource | Path | Action | Injection |
|----------|------|--------|-----------|
| Requirements Workflow | `03-workflows/requirements-analysis.md` | Follow EARS/Given-When-Then | MUST |
| DDD Constitution | `05-references/books/constitutions/ddd-constitution.md` | Apply Ubiquitous Language + Bounded Contexts | MUST |
| Architecture Rules | `02-rules/architecture-and-design.md` | Grep applicable REF-ARCH rules | SHOULD |
| Engineering Rules Catalog | `05-references/engineering-rules-catalog-REF.md` | Grep REF-ARCH-* | SHOULD |

---

## Stage 2: Architecture & Design (ADR)

| Resource | Path | Action | Injection |
|----------|------|--------|-----------|
| Architecture Constitution | `05-references/books/constitutions/arch-constitution.md` | Full load — Dependency Rule, SDP/SAP | MUST |
| DDD Constitution | `05-references/books/constitutions/ddd-constitution.md` | Full load — Aggregates, Bounded Contexts | MUST |
| Architecture Rules | `02-rules/architecture-and-design.md` | Full load — cite REF contracts | MUST |
| Engineering Rules Catalog | `05-references/engineering-rules-catalog-REF.md` | Grep REF-ARCH-*, REF-MOD-* | MUST |
| Books Archive | `05-references/books/engineering-books-16-distilled.txt` | Grep by lesson number/keyword for deep design rationale (fallback; constitutions are the primary contract) | IF deep-design |
| Integration Constitution | `05-references/books/constitutions/integration-constitution.md` | Load if multi-module/microservice | IF multi-system |
| Stack Entity Pattern | `06-templates/{stack}/entity-pattern.md` | Load if designing entities and stack plugin is installed | IF stack plugin |
| Stack Standards | `06-templates/{stack}/standards.md` | Load if stack plugin is installed | IF stack plugin |

---

## Stage 3: Threat Model (STRIDE)

| Resource | Path | Action | Injection |
|----------|------|--------|-----------|
| Security Constitution | `05-references/books/constitutions/security-constitution.md` | Full load — Zero Trust, XSS, BOLA, TOCTOU | MUST |
| Security Rules | `02-rules/security-checklist.md` | Full load — cite REF-SEC contracts | MUST |
| Engineering Rules Catalog | `05-references/engineering-rules-catalog-REF.md` | Grep REF-SEC-* | MUST |
| DevOps Reference | `05-references/devops-ops/devops-enterprise-and-production-readiness.md` | Grep OPS-SEC, OPS-AUTH anchors | SHOULD |

---

## Stage 4: Implementation

| Resource | Path | Action | Injection |
|----------|------|--------|-----------|
| Architecture Constitution | `05-references/books/constitutions/arch-constitution.md` | Enforce layer isolation, DTO mandate | MUST |
| DDD Constitution | `05-references/books/constitutions/ddd-constitution.md` | Enforce Aggregate Root, Repository rules | MUST |
| Performance Constitution | `05-references/books/constitutions/perf-constitution.md` | Enforce SARGable, Projection, No Lazy Loading | MUST |
| Security Constitution | `05-references/books/constitutions/security-constitution.md` | Enforce validation layering, Mass Assignment | MUST |
| Backend Prompts | `05-references/prompts/backend-prompts.md` | Inject for backend code generation (generic backend patterns) | MUST |
| Stack Prompts | `06-templates/{stack}/prompts.md` | Inject ready-to-use stack-specific snippets alongside Backend Prompts — no conflict, load both | IF stack plugin |
| Frontend Prompts | `05-references/prompts/frontend-prompts.md` | Inject for Angular code generation | IF frontend |
| Database Rules | `02-rules/database-performance.md` | Cite REF-DB contracts | MUST |
| Error Handling Rules | `02-rules/testing-and-quality.md` §3 | Cite REF-ERR contracts | MUST |
| Engineering Rules Catalog | `05-references/engineering-rules-catalog-REF.md` | Grep REF-DB-*, REF-ERR-*, REF-API-* | MUST |
| Books Archive | `05-references/books/engineering-books-16-distilled.txt` | Grep by lesson number/keyword for implementation rationale (fallback; constitutions are the primary contract) | IF deep-design |
| Resilience Constitution | `05-references/books/constitutions/resilience-constitution.md` | Load if financial/inventory/concurrent ops | IF critical data |
| Stack Entity Pattern | `06-templates/{stack}/entity-pattern.md` | Follow for entity creation | IF stack plugin |
| Stack Standards | `06-templates/{stack}/standards.md` | Follow naming/structure conventions | IF stack plugin |
| Stack Persona | `06-templates/{stack}/persona.md` | Inject as system prompt for stack-specific code generation | IF stack plugin |
| Pre-commit Config | `06-templates/{stack}/pre-commit-config.yaml` | Apply for git hooks | IF stack plugin |

---

## Stage 5: Testing & Quality Gate

| Resource | Path | Action | Injection |
|----------|------|--------|-----------|
| QA Strategy | `03-workflows/qa-strategy.md` | Follow test strategy framework | MUST |
| QA Reference | `05-references/qa-testing/qa-testing-strategy-and-automation.md` | Grep QA-* anchors for test patterns | MUST |
| Security Constitution | `05-references/books/constitutions/security-constitution.md` | Run SECURITY AUDIT self-check | MUST |
| Performance Constitution | `05-references/books/constitutions/perf-constitution.md` | Verify N+1, SARGable compliance | MUST |
| Testing Rules | `02-rules/testing-and-quality.md` | Cite REF-TEST contracts | MUST |
| Engineering Rules Catalog | `05-references/engineering-rules-catalog-REF.md` | Grep REF-TEST-* | MUST |
| Debugging Prompts | `05-references/prompts/debugging-prompts.md` | Inject when fixing test failures | IF debugging |
| Governance Runner | `governance/runner.py` | Execute deterministic gate before Done (GOV-T11) | MUST |

---

## Stage 6: Production Readiness (PRR)

| Resource | Path | Action | Injection |
|----------|------|--------|-----------|
| Production Readiness | `03-workflows/production-readiness.md` | Follow 10-dimension PRR scorecard | MUST |
| Resilience Constitution | `05-references/books/constitutions/resilience-constitution.md` | Verify Circuit Breaker, Outbox, Concurrency | MUST |
| DevOps Reference | `05-references/devops-ops/devops-enterprise-and-production-readiness.md` | Grep OPS-* anchors for deployment checklist | MUST |
| Engineering Rules Catalog | `05-references/engineering-rules-catalog-REF.md` | Grep REF-OPS-*, REF-NET-* | MUST |
| Integration Constitution | `05-references/books/constitutions/integration-constitution.md` | Verify boundary protocols | SHOULD |

---

## Stage 7: Deployment & Rollout

| Resource | Path | Action | Injection |
|----------|------|--------|-----------|
| DevOps Reference | `05-references/devops-ops/devops-enterprise-and-production-readiness.md` | Grep OPS-DEPLOY, OPS-ROLLBACK anchors | MUST |
| Resilience Constitution | `05-references/books/constitutions/resilience-constitution.md` | Verify rollback design, graceful degradation | MUST |
| GitHub Security Gate | `06-templates/{stack}/github-security-gate.yml` | Apply CI/CD security workflow | IF GitHub Actions |
| PR Template | `06-templates/{stack}/pull_request_template.md` | Use for pull request | IF stack plugin |

---

## Stage 8: Post-Launch Monitoring

| Resource | Path | Action | Injection |
|----------|------|--------|-----------|
| DevOps Reference | `05-references/devops-ops/devops-enterprise-and-production-readiness.md` | Grep OPS-MONITOR, OPS-ALERT anchors | MUST |
| Performance Constitution | `05-references/books/constitutions/perf-constitution.md` | Verify query performance in production | SHOULD |
| Debugging Prompts | `05-references/prompts/debugging-prompts.md` | Inject for production debugging | IF incident |

---

## Resource Utilization Summary Template

At the end of each pipeline run, produce this report:

```markdown
## Resource Utilization Report — [Feature/Project Name]

### Resources Loaded & Cited
| Resource | Stage | Citation (file:line or REF-*) |
|----------|-------|-------------------------------|
| [name]   | [#]   | [where used]                  |

### Constitutions Applied
| Constitution | Rules Enforced | Violations Found |
|-------------|----------------|------------------|
| [name]      | [count]        | [count]          |

### Templates Used
| Template | Purpose | Modified? |
|----------|---------|-----------|

### Prompts Injected
| Prompt | Stage | Adaptation |
|--------|-------|------------|

### Coverage: X/Y MUST resources used | Z IF-conditions triggered
```
