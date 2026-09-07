# My Programming Workflow — Agent Operating System (AOS) v7.0

> **A stack-agnostic operating system for AI-assisted software engineering.**
> Copy the `.agent/` folder into any project, paste one session prompt, and every task —
> feature, bugfix, security review, or QA — runs through classified, governed,
> memory-preserving workflows instead of free-form prompting.

**Version:** 7.0.0 "Wired Pipeline" · **Source repo:** https://github.com/Nezarabdluah/My-Programming-Workflow

---

## Table of Contents

1. [What This Is](#1-what-this-is)
2. [Why It Is Different](#2-why-it-is-different)
3. [Architecture at a Glance](#3-architecture-at-a-glance)
4. [Repository Map](#4-repository-map)
5. [Core Concepts](#5-core-concepts)
6. [Quick Start — New Project](#6-quick-start--new-project)
7. [Quick Start — Existing Project](#7-quick-start--existing-project)
8. [The Session Prompt (copy-paste)](#8-the-session-prompt-copy-paste)
9. [Daily Workflow — Step by Step](#9-daily-workflow--step-by-step)
10. [Workflow Catalog](#10-workflow-catalog)
11. [Reference Library](#11-reference-library)
12. [Governance Gate (deterministic checks)](#12-governance-gate-deterministic-checks)
13. [Switching AI Tools Mid-Project](#13-switching-ai-tools-mid-project)
14. [Keeping Projects in Sync](#14-keeping-projects-in-sync)
15. [FAQ](#15-faq)

---

## 1. What This Is

AOS is a **Markdown-driven operating layer** that sits between you and any coding AI
(Claude, Antigravity, Cursor, Windsurf, Copilot, or anything else). It provides:

- **Task classification** — every request is triaged as 🟢 Simple, 🟡 Medium, or 🔴 Sensitive, and the process scales with risk.
- **Spec-Driven Development (SDD)** — medium and sensitive tasks must pass `Draft → Clarify → Approved → Planning → Ready → Executing → Validating → Done`, with a hard human approval gate before code is written.
- **Mandatory resource injection** — the model is forced to load the right constitutions, rules, and references for the current stage and cite them in code (`// [REF-DB-N1]`, `// [CONST-SEC-3]`).
- **Cumulative memory** — project state, decisions (ADRs), and learned mistakes survive across sessions and across tools.
- **Deterministic governance** — a Python test-suite (`governance/runner.py`) verifies memory, rules, and state independently of what the model claims.

It is **stack-agnostic**: the same system governs .NET/ABP, Node, Python, mobile, or any other stack.
Ready-made templates exist for .NET 8 + ABP + Angular + SQL Server under `06-templates/dotnet-abp/`.

---

## 2. Why It Is Different

| Problem with plain prompting | How AOS fixes it |
|------------------------------|------------------|
| The model "knows" good practice but never applies it | **Mandatory Injection Protocol** — every workflow starts with a `MUST, gate blocked` resource-loading block; a stage cannot be marked Done without a Resource Utilization Summary |
| Knowledge scattered across chats | **Wiring Registry** (`01-core/wiring-registry.md`) — one central DI container mapping each capability to its rule file, REF contracts, constitution, and grep anchors |
| 16 books of engineering wisdom, zero enforcement | **6 constitution files** (79 actionable rules) + a **34-directive REF catalog** + a **114-lesson distilled archive** (all English, greppable by lesson number), all cited by ID in code |
| Context lost when switching tools or sessions | **Memory module** (`04-memory/`) + **handoff protocol** — the next tool resumes exactly where you stopped |
| "Done" means "code compiles" | **Vertical-slice governance** — Done requires explicit coverage of 7 layers (DB → Domain → Application → API → Frontend → UI/UX → Tests) or a written justification |
| Rules contradict each other | **Layer priority** L0 → L5 and a **conflict-resolution order** (Security > Memory > Correctness > Simplicity > Performance > Conventions) |

---

## 3. Architecture at a Glance

```
L0  Constitution ─────── AGENTS.md + 01-core/operating-contract.md        ← highest authority
L5  Governance ───────── governance/runner.py (executable truth, overrides any model claim)
L1  Memory Core ──────── 04-memory/ (cumulative context, single source of truth)
L2  Pipeline ─────────── 03-workflows/ + master-pipeline/ (consumable stages 0–8)
L3  Rules ────────────── 02-rules/ (6 specialized files, load ONE at a time)
L4  References ───────── 05-references/ (grep-only, never read in full)  ← lowest authority
```

**Dependency flow is strictly one-way:** Workflows → Memory → References → Rules.
Workflows never embed hard quality rules; rules never know their consumers.

---

## 4. Repository Map

```
.agent/
├── AGENTS.md                  ← master directive: boot order, SDD, wiring, handoff, forbidden list
├── INDEX.md                   ← smart index: start here to reach any file
├── VERSION                    ← aos_version + last_sync + source_path
├── 01-core/                   ← mandatory at session start
│   ├── operating-contract.md  ← conflict priority, SDD, vertical-slice charter, mistake learning
│   ├── session-prompt.md      ← unified boot: Step 0 matching → Session Mode → Paths A/B/C/D
│   ├── task-classification.md ← 🟢/🟡/🔴 indicators + Zero-Trust escalation rule
│   ├── token-budget.md        ← ≤ 400 lines/session selective-loading policy
│   ├── collaboration-rules.md ← Driver/Navigator pair-programming protocol
│   └── wiring-registry.md     ← ⭐ central DI container: capability → rule → REF → constitution
├── 02-rules/                  ← specialized rules (load ONE at a time)
│   ├── architecture-and-design.md | database-performance.md | security-checklist.md
│   ├── testing-and-quality.md     | network-and-api.md      | vertical-slice-governance.md
├── 03-workflows/              ← Markdown-driven task guides, each with a MUST injection block
│   ├── init-project.md / start-session.md / end-session.md / requirements-analysis.md
│   ├── create-backend-module.md / create-frontend-module.md
│   ├── debug-common-errors.md / improve-user-experience.md
│   ├── knowledge-bootstrapping.md / qa-strategy.md / production-readiness.md
│   ├── master-pipeline/       ← ⭐ Path D: stages 0–8 (Intake → … → Post-Launch) with decision gates
│   ├── mobile-qa/             ← coordinator + steps for React Native / Expo QA
│   └── security-gate/         ← coordinator + 7 steps (threat model → gate report)
├── 04-memory/                 ← per-PROJECT cumulative memory (initialized fresh per project)
│   ├── project-context.md / active-tasks.md / decisions.md (ADRs) / learned-mistakes.md
│   └── project-knowledge.md / codebase-map.md / mistakes-archive.md
├── 05-references/             ← grep-only library (query with grep, never full-read)
│   ├── engineering-rules-catalog-REF.md  ← 34 [REF-*] directives in 8 categories
│   ├── books/00-master-index.md          ← ⭐ Resource Injection Matrix: 20/20 resources → every stage (MUST/SHOULD/IF)
│   ├── books/engineering-books-16-distilled.txt ← 114 lessons, all English, grep by "Lesson N"
│   ├── books/constitutions/              ← 6 files, 79 actionable rules (arch, ddd, security, perf, resilience, integration)
│   ├── prompts/                          ← backend-prompts, frontend-prompts, debugging-prompts (+ ABP row in matrix)
│   ├── qa-testing/ (11 [QA-*]) / devops-ops/ (18 [OPS-*]) ← anchors, grep-only
├── 06-templates/dotnet-abp/   ← entity-pattern, standards, persona, prompts, PR template, pre-commit, security gate
├── 06-templates/claude-skills/ ← official anthropics/skills clone, reference-only (tracked as submodule; see FAQ)
├── governance/                ← runner.py + 3 test files, 10 checks, fully English (GOV-T01…T11)
└── adr/                       ← ADR template
AGENTS.md (root bridge for ~30 tools) / .gitignore / .cursorrules / .windsurfrules  ← IDE shims pointing assistants at .agent/
```

---

## 5. Core Concepts

### 5.1 Task classification

| Class | Signal words | Process |
|-------|--------------|---------|
| 🟢 Simple | "fix the color", "add a comment", typo | YAGNI — execute immediately, text summary |
| 🟡 Medium | business-logic change, multi-file edits | Clean-Code policy + full SDD + tests green locally |
| 🔴 Sensitive | database, security, architecture | ADR mandatory + OWASP/SARGable checks + human approval gate |

Zero-Trust rule: when in doubt, escalate one level. Never downgrade 🟡/🔴 to skip process.

### 5.2 Task routing — Paths A / B / C / D

- **Path A** — new feature / large change → SDD spec (`requirements-analysis.md`).
- **Path B** — task matches a file in `03-workflows/` → read it and follow its steps exactly.
- **Path C** — trivial edit → do it, summarize.
- **Path D** — full pipeline (stages 0–8 in `master-pipeline/`) for production-grade delivery.

### 5.3 Mandatory injection & citation

Before writing code, the agent MUST:

1. Read `05-references/books/00-master-index.md` for the current stage.
2. Resolve capabilities via `01-core/wiring-registry.md`.
3. Load every `MUST` constitution; check every `IF` condition.
4. Cite in code: `// [REF-DB-N1]: prevent N+1 query`, `// [CONST-SEC-3]`.
5. Produce a **Resource Utilization Summary** before marking the stage Done.

The matrix covers **20/20 resources** — nothing is an island. Delivery also declares an enforcement level: `[Enforcement: CI ✅]` > `[hooks ⚠️]` > `[runner.py 🔶]` > `[manual 🔶]` (model claim alone `[claim ❌]` is rejected). Full pipeline work scales by the DoD ladder: 🟢 mini / 🟡 stages 1,4,5 / 🔴 all 0–8.

### 5.4 Session budgets

- **Reading budget:** ≤ 400 lines per session — load `02-rules/` one file at a time, grep (never full-read) `05-references/`.
- **Mistakes:** max 20 active in `learned-mistakes.md` (newest on top); a mistake repeated 3× escalates into a permanent rule or test.

---

## 6. Quick Start — New Project

**Prerequisites:** a clone of this repo somewhere stable on your machine (it is the source), plus any AI coding assistant.

1. **Copy the system into your project.** Follow `.agent/03-workflows/init-project.md`:
   copy `01-core/`, `02-rules/`, `03-workflows/`, `05-references/`, `governance/`, `adr/`, `06-templates/`, `INDEX.md`, `AGENTS.md`, `VERSION` into your project's `.agent/` folder.
2. **Initialize memory.** Create `.agent/04-memory/` with the seven files from `init-project.md` Step 3
   (`project-context.md`, `learned-mistakes.md`, `decisions.md`, `active-tasks.md`, `project-knowledge.md`, `codebase-map.md`, `mistakes-archive.md`).
3. **Stamp the version.** Write `.agent/VERSION` with `aos_version: 7.0.0`, today's date, and `source_path: [YOUR-LOCAL-AOS-PATH]` (never a real local path in shared files).
4. **Paste the session prompt** ([Section 8](#8-the-session-prompt-copy-paste)) as your first message to the AI.
5. The agent prints a **boot report** (proof of read) and asks for the first task. If the project already contains code, it runs **knowledge bootstrapping** first (codebase map, conventions, test activation).

> ⚠️ Source Protection Rule: this repo is the **read-only master**. The agent may read from it but must never write to it — all writes happen in the project's local `.agent/04-memory/`.

---

## 7. Quick Start — Existing Project

Same as above, except after the boot report the agent:

1. Executes `.agent/03-workflows/knowledge-bootstrapping.md` — maps your codebase into `04-memory/codebase-map.md`, records conventions in `project-knowledge.md`.
2. Checks test automation and DevOps hooks, proposes quick wins.
3. If `.agent/` already exists locally, it **diffs it against the master** and copies over only the missing files until the structure is 100% complete.

---

## 8. The Session Prompt (copy-paste)

Paste the block below as the **first message** of any new project or session.
Replace `[YOUR-LOCAL-AOS-PATH]` with the folder where you cloned this repo
(e.g. `C:\AOS\My-Programming-Workflow\.agent`).

```text
You operate on an integrated system: AOS v7.0 + Spec-Kit (SDD) — Knowledge-first & Memory-first Platform.
Communicate in clear, professional English. Think aloud in a structured, rigorous way before every decision.
Main AOS source (READ-ONLY): [YOUR-LOCAL-AOS-PATH]

SOURCE PROTECTION: never modify or write to the Main AOS Path. All writes happen in the current project's local .agent/04-memory/ only.

STEP 0 — BOOT & MATCH (silent, then report):
1. If the current project has no .agent/ folder → initialize it by fully executing [MAIN-AOS-PATH]/03-workflows/init-project.md (copy system + init 04-memory/ + stamp VERSION).
2. If .agent/ exists → diff 01-core/, 02-rules/, 03-workflows/, 04-memory/, 05-references/, governance/ against the main source; copy any missing file so the structure is 100% complete.
3. If the project already contains code → also execute .agent/03-workflows/knowledge-bootstrapping.md.

SESSION MODE (budget ≤ 400 lines). Read in order:
1. .agent/INDEX.md  2. .agent/01-core/operating-contract.md  3. .agent/04-memory/project-context.md
4. .agent/04-memory/learned-mistakes.md  5. .agent/04-memory/active-tasks.md  6. .agent/VERSION

Then print this boot report:
  Session started | System: AOS v7.0 (Knowledge & Memory-first)
  Project: [name] | Stack: [detected: package.json / requirements.txt / csproj|sln / General]
  Memory — project-context: "[last task verbatim or 'new project']"
  Memory — learned-mistakes: [N] active, latest: "[quote or 'none']"
  Memory — active-tasks: [N] pending, top: "[quote or 'none']"
  VERSION: [in sync ✅ / needs sync ⚠️]
  Ready — what is our next task?

TASK ROUTING:
- Path A (new feature / big change: "add", "rebuild", "create system", "change architecture") → classify 🟢/🟡/🔴, apply the Policy Engine (🔴 = ADR + OWASP/SARGable + human gate; 🟡 = Clean Code + local tests green), then SDD: Draft → Clarify → Approved → Planning → Ready → Executing → Validating → Done. STOP at the Approval Gate before writing code.
- Path B (matches .agent/03-workflows/: backend module, frontend module, bug, UX, mobile-qa, security-gate, requirements, QA, production-readiness) → read that file and follow it exactly, including its MUST injection block.
- Path C (trivial: text, color, comment) → 🟢 do it, summarize.
- Path D (full delivery) → run 03-workflows/master-pipeline/ stages 0–8 with decision gates.

SMART WIRING (before code): resolve via .agent/01-core/wiring-registry.md + .agent/05-references/books/00-master-index.md (20/20 resources mapped); load the ONE matching 02-rules/ file; grep (never full-read) 05-references/ including the 114-lesson books archive by lesson number/keyword when deep rationale is needed; ABP project → also inject 06-templates/dotnet-abp/prompts.md alongside backend-prompts; cite as // [REF-XX-N] and // [CONST-XX-N]; end each stage with a Resource Utilization Summary.

HANDOFF (on "switch tool" / "save session"): update active-tasks.md + project-context.md + decisions.md, then print a handoff summary (project, current feature, exact stopping point, next step).
CLOSEOUT (on "end session"): execute .agent/03-workflows/end-session.md, update all memory files, print the session summary.

FORBIDDEN: writing to the main AOS source · loading two rule files at once · full-reading 05-references/ · skipping classification · coding 🟡/🔴 without approved spec+plan · ending a 🟡/🔴 reply without updating memory · accepting assumptions — test-tool success is the only proof of code quality.
```

---

## 9. Daily Workflow — Step by Step

1. **Open a session** — paste the prompt above; confirm the boot report.
2. **State the task** — e.g. "Add order refunds to the billing module."
3. **Confirm classification** — the agent proposes 🟢/🟡/🔴; correct it if wrong (corrections are classified A/B/C and learned).
4. **Review the spec & plan** (🟡/🔴) — user stories + acceptance criteria (`Given/When/Then` or EARS), then MVP increments. **Approve explicitly** — nothing is coded before this.
5. **Watch injection happen** — the agent loads the matrix row, wiring row, constitution(s), the one rule file, and prompt packs, citing IDs.
6. **Review the vertical-slice report** — every delivery ends with: slice-coverage table (`[Layer] ← [done / n/a because…]` with `file:line`), architectural decisions (decision ← rejected alternative ← principle), judgment calls, and items flagged for human review.
7. **Validate** — project tests green + `governance/runner.py` where applicable, declaring the enforcement level (`[Enforcement: CI/hooks/runner/manual]`).
8. **Close or hand off** — "end session" or "switch tool"; memory files updated, summary printed.

---

## 10. Workflow Catalog

| Task | File |
|------|------|
| Link a new project | `03-workflows/init-project.md` |
| Start / end a session | `03-workflows/start-session.md`, `end-session.md` |
| Requirements & SDD specs (EARS + Given/When/Then) | `03-workflows/requirements-analysis.md` |
| Backend module (Domain → App → Infra → API → Tests) | `03-workflows/create-backend-module.md` |
| Frontend module (components, state, independence) | `03-workflows/create-frontend-module.md` |
| Bug diagnosis (evidence-first, root-cause search) | `03-workflows/debug-common-errors.md` |
| UX review (interaction, visual, accessibility) | `03-workflows/improve-user-experience.md` |
| Existing-codebase onboarding | `03-workflows/knowledge-bootstrapping.md` |
| Test strategy & quality gates | `03-workflows/qa-strategy.md` |
| Production readiness (10-dimension scorecard) | `03-workflows/production-readiness.md` |
| Full delivery pipeline, stages 0–8 | `03-workflows/master-pipeline/` |
| Mobile QA (React Native / Expo) | `03-workflows/mobile-qa/` |
| Security gate (7 steps incl. secret scan, gate report) | `03-workflows/security-gate/` |

---

## 11. Reference Library

- **REF catalog** — `05-references/engineering-rules-catalog-REF.md`: 34 directives across ARCH, DB, SEC, NET, TEST, OBS, RES, AI.
- **Constitutions** — `05-references/books/constitutions/`: architecture, DDD, security, performance, resilience, integration (79 rules total).
- **Books archive** — `05-references/books/engineering-books-16-distilled.txt`: 114 lessons, fully English, grep by `Lesson N` or keyword (reconstructed gap-fill marked `PART III`, see `books/00-index.md`).
- **Injection matrix** — `05-references/books/00-master-index.md`: the single table mapping **20/20 resources** to every pipeline stage with `MUST` (gate blocked) / `SHOULD` / `IF`.
- **Prompt packs** — `05-references/prompts/`: backend, frontend, debugging; plus ABP-specific snippets in `06-templates/dotnet-abp/prompts.md`.
- **QA & DevOps** — `05-references/qa-testing/` (`[QA-*]`), `05-references/devops-ops/` (`[OPS-*]`).
- **ABP templates** — `06-templates/dotnet-abp/`: entity pattern, standards, persona, PR template, pre-commit config, CI security gate.

---

## 12. Governance Gate (deterministic checks)

The model can claim anything — `governance/runner.py` is executable ground truth:

```bash
python .agent/governance/runner.py
```

It runs `test_memory.py`, `test_rules.py`, and `test_state.py` — 10 checks, fully English (memory integrity, rule linkage, SDD state validity, ADR structure, handoff validity, dead references, …).
`03-workflows/end-session.md` enforces this gate **before** any task may be marked Done (GOV-T11: only actual evidence — exit codes, tool output — counts as proof).
`03-workflows/end-session.md` enforces this gate **before** any task may be marked Done.

---

## 13. Switching AI Tools Mid-Project

Memory is tool-independent by design:

1. Tell the current agent: **"switch tool"** (or "save session").
2. It updates `active-tasks.md`, `project-context.md`, `decisions.md` and prints a formatted handoff summary.
3. In the new tool, paste the [session prompt](#8-the-session-prompt-copy-paste) **plus** the handoff summary.
4. The new agent resumes at the exact stopping point — no re-explaining.

---

## 14. Keeping Projects in Sync

- Each project's `.agent/VERSION` records `aos_version`, `last_sync`, and `source_path`.
- To upgrade a project: pull this repo, re-run the Step-0 diff from the session prompt, copy missing/updated files, bump `last_sync`.
- Never edit the master directly for project needs — project-specific learning belongs in the project's `04-memory/learned-mistakes.md`; generally useful rules belong in `02-rules/` via a deliberate, reviewed change.

---

## 15. FAQ

**Which AI tools does this work with?**
Any assistant that can read local files and follow instructions — Claude, Cursor, Windsurf, Copilot, Antigravity, and similar. Tool-specific shims (`.cursorrules`, `.windsurfrules`) point at `.agent/`.

**Does it force a tech stack?**
No. The core is stack-agnostic. Only `06-templates/` is .NET/ABP-specific, and it loads conditionally (`IF ABP project`).

**What does a "task" cost in context?**
Boot reads are capped at 400 lines; rules load one file at a time; references are grep-queried, never fully read. The matrix tells the model exactly what each stage needs — nothing more.

**Where do I put secrets or machine-specific paths?**
Never in the repo. The session prompt's `[YOUR-LOCAL-AOS-PATH]` is per-machine and stays in your chat, not in committed files.

**Is everything really 100% English?**
Yes — audited zero-Arabic across the repo (system files, governance suite, 114-lesson archive, memory files). Chat language is yours to choose: the session prompt says English, but replace that line with any language (e.g. Arabic) without touching the system.

**How are the bundled Claude skills (`06-templates/claude-skills/`) managed?**
They are a pristine clone of the official `anthropics/skills` repo (17 skills: pdf/docx/pptx/xlsx, webapp-testing, mcp-builder, skill-creator, devops-toolkit, and more) kept as **reference-only** — AOS workflows never load or index their internals. Track them as a submodule so the published repo stays lean:
`git submodule add https://github.com/anthropics/skills.git 06-templates/claude-skills`
then remove the ignore line in `.gitignore`. Consumers clone with `git clone --recurse-submodules <repo-url>`.

**Can I contribute?**
Yes — open an issue or PR at https://github.com/Nezarabdluah/My-Programming-Workflow. Changes to `01-core/` and `02-rules/` need extra-careful review since every project inherits them.
