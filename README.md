<p align="center">
  <img src="https://img.shields.io/badge/AOS-v7.0.0-blue?style=for-the-badge&labelColor=1a1a2e" alt="AOS Version"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&labelColor=1a1a2e" alt="License"/>
  <img src="https://img.shields.io/badge/works%20with-Claude%20%7C%20Cursor%20%7C%20Copilot%20%7C%20Windsurf-orange?style=for-the-badge&labelColor=1a1a2e" alt="AI Tools"/>
</p>

<h1 align="center">AOS — Agent Operating System</h1>

<p align="center">
  <strong>Turn any AI coding assistant into a governed engineering team.</strong><br/>
  <em>Every task classified. Every delivery verified. Context persists across sessions.</em>
</p>

<p align="center">
  <a href="#-you-dont-need-to-understand-aos-to-use-it">Quick Start</a> •
  <a href="#-see-it-in-action">See It in Action</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-compatibility">Compatibility</a> •
  <a href="#-faq">FAQ</a>
</p>

---

## What is AOS?

AOS (Agent Operating System) is a **stack-agnostic framework** that transforms any AI coding assistant into a **governed engineering team**. It solves one fundamental problem:

> *AI models know good practice but never apply it consistently.*

AOS enforces mandatory resource injection, cumulative memory across sessions, and deterministic governance — so every task follows the same professional workflow, regardless of which AI tool you use.

---

## You Don't Need to Understand AOS to Use It

If you only want to use AOS, here's everything you need:

```
1. Copy .agent/ into your project
2. Start your AI assistant with the session prompt
3. Give it a task
4. Let the workflow handle routing and governance
```

Everything else — constitutions, wiring registry, REF directives, master pipeline — is **optional documentation** for when you want to customize or extend the system.

---

## Requirements

**Required:**
- Git
- An AI coding assistant that can read local files (Claude Code, Cursor, Windsurf, Copilot, etc.)
- Python 3.x (for governance runner)

**Optional:**
- CI/CD pipeline (GitHub Actions, Azure DevOps)
- Git hooks (pre-commit, pre-push)

---

## Quick Start

### 1. Clone the master

```bash
git clone https://github.com/Nezarabdluah/My-Programming-Workflow.git
```

### 2. Copy .agent/ into your project

```bash
cp -r My-Programming-Workflow/.agent/ your-project/.agent/
```

### 3. Start your AI with the session prompt

Paste this as your first message to the AI:

```text
You operate on AOS v7.0 — Knowledge-first & Memory-first Platform.
Main AOS source (READ-ONLY): /path/to/your-project/.agent

STEP 0 — BOOT:
1. Read .agent/INDEX.md
2. Read .agent/01-core/operating-contract.md
3. Read .agent/04-memory/project-context.md
4. Print boot report and ask for the first task.
```

### 4. Give it a task

```text
Fix the wallet transaction sorting bug.
The API ignores the requested sorting field.
```

> ✅ The agent classifies the task, loads relevant rules, implements the fix, runs governance checks, and saves memory for the next session.

---

## See It in Action

### Example: Fixing a Bug

Here's exactly what happens when you give AOS a real task:

```
You:    "Fix the wallet transaction sorting bug.
         The API ignores the requested sorting field."

AOS:    [Mode: 🟡 Medium]
        [Path: B — Known type → debug-common-errors.md]

        1. CLASSIFY → 🟡 Medium (multi-file, business logic)
        2. ROUTE → Bug workflow (debug-common-errors.md)
        3. INJECT RESOURCES:
           - Load: 02-rules/database-performance.md
           - Load: 02-rules/testing-and-quality.md
           - Grep: REF-DB-N1, REF-DB-PAG
           - Load: debugging-prompts.md
        4. INSPECT → Find root cause in OrderService.cs:47
        5. IDENTIFY → Missing ORDER BY in query
        6. FIX → Add proper sorting with SARGable query
        7. TEST → Run unit tests → all green
        8. GOVERN → python .agent/governance/runner.py → ✅ PASSED
        9. REPORT → Vertical-slice coverage table
        10. MEMORY → Update active-tasks.md + project-context.md

AOS:    ✅ Done. Fixed in OrderService.cs:47
        // [REF-DB-PAG]: Server-side pagination applied
        // [REF-DB-SARG]: SARGable query enforced
        Tests: 12/12 passing
        Governance: [Enforcement: runner.py 🔶]
```

### Example: Adding a Feature

```
You:    "Add email notifications for order confirmations."

AOS:    [Mode: 🔴 Sensitive]
        [Path: A — Feature → SDD workflow]

        1. SPECIFY → Draft user stories with acceptance criteria
        2. CLARIFY → Ask you 3 questions about requirements
        3. APPROVE → ⏸️ STOP — waiting for your approval
        4. PLAN → Break into MVP increments
        5. IMPLEMENT → Build vertically (DB → Domain → API → Frontend → Tests)
        6. VALIDATE → Run all tests + governance
        7. CLOSE → Delivery report + memory saved

AOS:    📋 Spec saved to specs/order-notifications.md
        ⏸️ Please review and approve the plan before I start coding.
```

---

## How a Task Flows

Every task follows the same 7-step rhythm:

```mermaid
graph LR
    A["1. Boot"] --> B["2. Classify"]
    B --> C["3. Route"]
    C --> D["4. Inject"]
    D --> E["5. Implement"]
    E --> F["6. Govern"]
    F --> G["7. Close"]
```

### Task Classification

| Mode | Signals | Process |
|------|---------|---------|
| 🟢 **Simple** | typo, color, comment (≤2 files) | Execute immediately + summary |
| 🟡 **Medium** | business logic, multi-file | SDD spec → approval → tests green |
| 🔴 **Sensitive** | DB, auth, architecture (>5 files) | ADR + OWASP + human gate |

### Task Paths

| Path | When | What Happens |
|------|------|--------------|
| **A** — Feature | new functionality | SDD spec → approval → plan → implement |
| **B** — Known type | backend, frontend, bug, security | Follow matching workflow |
| **C** — Trivial | typo, color, comment | Done immediately |
| **D** — Full delivery | production-grade | Pipeline stages 0–8 |

---

## Architecture

Six layers, one direction, zero ambiguity:

```mermaid
graph TB
    L0["L0: Constitution<br/>AGENTS.md + operating-contract"]
    L5["L5: Governance<br/>runner.py — executable truth"]
    L1["L1: Memory Core<br/>04-memory/ — cumulative context"]
    L2["L2: Pipeline<br/>03-workflows/ — stages 0–8"]
    L3["L3: Rules<br/>02-rules/ — 6 specialized files"]
    L4["L4: References<br/>05-references/ — grep-only"]

    L0 --> L5
    L5 --> L1
    L1 --> L2
    L2 --> L3
    L3 --> L4
```

| Layer | Contains | Authority |
|-------|----------|-----------|
| **L0** Constitution | `AGENTS.md` + operating contract | Highest — wins every conflict |
| **L5** Governance | `runner.py` — executable checks | Overrides any model claim |
| **L1** Memory | `04-memory/` — cumulative context | Single source of truth |
| **L2** Pipeline | `03-workflows/` — stages 0–8 | Consumable, loaded per task |
| **L3** Rules | `02-rules/` — 6 files | One file at a time, never two |
| **L4** References | `05-references/` — books, REF, QA | Grep-only, never full-read |

> Dependency flow is **strictly one-way**: Workflows → Memory → References → Rules.

---

## Compatibility

AOS works with any AI coding assistant that can read local files.

| Tool | Auto-discovery | Session Prompt | Notes |
|------|----------------|----------------|-------|
| **Claude Code** | ✅ via `AGENTS.md` | ✅ paste manually | Best support — CLAUDE.md equivalent |
| **Cursor** | ✅ via `.cursorrules` | ✅ paste manually | Shims point to `.agent/` |
| **Windsurf** | ✅ via `.windsurfrules` | ✅ paste manually | Shims point to `.agent/` |
| **GitHub Copilot** | ⚠️ partial | ✅ paste manually | Uses custom instructions |
| **Any file-reading AI** | ✅ via `AGENTS.md` | ✅ paste manually | ~30 tools auto-discover |

> **How it works**: `.cursorrules` and `.windsurfrules` are pointer files that tell the AI to read `.agent/AGENTS.md`. Root `AGENTS.md` is auto-discovered by ~30 tools.

---

## Repository Structure

```
.agent/
├── AGENTS.md                  # Master directive contract
├── INDEX.md                   # Smart index — reach any file
├── VERSION                    # Version + sync info
├── 01-core/                   # Core (mandatory at session start)
│   ├── operating-contract.md  #   Operational contract
│   ├── session-prompt.md      #   Unified session prompt
│   ├── task-classification.md #   🟢/🟡/🔴 indicators
│   ├── token-budget.md        #   ≤400 lines/session policy
│   └── wiring-registry.md     #   Central DI container
├── 02-rules/                  # Specialized rules (ONE at a time)
│   ├── architecture-and-design.md
│   ├── database-performance.md
│   ├── security-checklist.md
│   ├── testing-and-quality.md
│   ├── network-and-api.md
│   └── vertical-slice-governance.md
├── 03-workflows/              # Workflows (Markdown-driven)
│   ├── master-pipeline/       #   Stages 0–8
│   ├── security-gate/         #   Security gate (7 steps)
│   └── mobile-qa/             #   Mobile QA
├── 04-memory/                 # Cumulative contextual memory
│   ├── project-context.md
│   ├── active-tasks.md
│   ├── decisions.md
│   └── learned-mistakes.md
├── 05-references/             # References (grep-only)
│   ├── engineering-rules-catalog-REF.md
│   ├── books/
│   │   ├── 00-master-index.md #   Resource Injection Matrix
│   │   └── constitutions/     #   6 constitutions (79 rules)
│   └── prompts/
├── 06-templates/              # Project templates
│   └── dotnet-abp/            #   ABP/.NET specific
├── governance/                # Deterministic enforcement
│   ├── runner.py
│   └── test_*.py
└── adr/                       # Architecture Decision Records
```

---

## Reference Library

| Resource | Description |
|----------|-------------|
| **REF Catalog** | 34 directives: ARCH×7, DB×7, SEC×5, NET×5, TEST×2, OBS×2, RES×1, AI×1 |
| **Constitutions** | 79 actionable rules from 16 engineering books |
| **Books Archive** | 114 lessons — grep `Lesson N` for deep rationale |
| **Prompt Packs** | backend / frontend / debugging |
| **QA / DevOps** | 11 `[QA-*]` anchors · 18 `[OPS-*]` anchors |

---

## Governance Gate

```bash
python .agent/governance/runner.py
```

**10 deterministic checks** — executable ground truth, not model claims.

| Enforcement Level | Tag | Confidence |
|-------------------|-----|------------|
| CI pipeline ran | `[Enforcement: CI ✅]` | Highest |
| Git hooks fired | `[Enforcement: hooks ⚠️]` | Good |
| runner.py executed | `[Enforcement: runner.py 🔶]` | Acceptable |
| Manual checklist | `[Enforcement: manual 🔶]` | Lowest acceptable |
| Model claim only | `[Enforcement: claim ❌]` | **REJECTED** |

---

## Session Prompt

<details>
<summary><b>Click to expand the full session prompt</b></summary>

```text
You operate on an integrated system: AOS v7.0 + Spec-Kit (SDD) — Knowledge-first & Memory-first Platform.
Communicate in clear, professional English. Think aloud in a structured, rigorous way before every decision.
Main AOS source (READ-ONLY): [YOUR-LOCAL-AOS-PATH]

SOURCE PROTECTION: never modify or write to the Main AOS Path. All writes happen in the current project's local .agent/04-memory/ only.

STEP 0 — BOOT & MATCH (silent, then report):
1. If the current project has no .agent/ folder → initialize it by fully executing [YOUR-LOCAL-AOS-PATH]/03-workflows/init-project.md
2. If .agent/ exists → diff 01-core/, 02-rules/, 03-workflows/, 04-memory/, 05-references/, governance/ against the main source; copy any missing file
3. If the project already contains code → also execute .agent/03-workflows/knowledge-bootstrapping.md

SESSION MODE (budget ≤ 400 lines). Read in order:
1. .agent/INDEX.md  2. .agent/01-core/operating-contract.md  3. .agent/04-memory/project-context.md
4. .agent/04-memory/learned-mistakes.md  5. .agent/04-memory/active-tasks.md  6. .agent/VERSION

Then print this boot report:
  Session started | System: AOS v7.0 (Knowledge & Memory-first)
  Project: [name] | Stack: [detected]
  Memory — project-context: "[last task verbatim or 'new project']"
  Memory — learned-mistakes: [N] active, latest: "[quote or 'none']"
  Memory — active-tasks: [N] pending, top: "[quote or 'none']"
  VERSION: [in sync ✅ / needs sync ⚠️]
  Ready — what is our next task?

TASK ROUTING:
- Path A (new feature) → SDD: Draft → Clarify → Approved → Planning → Ready → Executing → Validating → Done
- Path B (known type) → follow matching workflow file
- Path C (trivial) → do it, summarize
- Path D (full delivery) → master-pipeline stages 0–8

SMART WIRING (before code): resolve via wiring-registry.md + 00-master-index.md; load ONE 02-rules/ file; grep 05-references/; cite // [REF-XX-N] and // [CONST-XX-N]

HANDOFF: update memory files, print handoff summary
CLOSEOUT: execute end-session.md, update all memory, print summary

FORBIDDEN: writing to main AOS source · loading two rule files at once · full-reading 05-references/ · skipping classification · coding 🟡/🔴 without approved spec+plan · ending without updating memory
```

</details>

---

## Switching AI Tools

1. Say **"switch tool"** — memory updates, handoff summary prints
2. In the new tool, paste the session prompt + handoff summary
3. Work resumes at the exact stopping point

---

## FAQ

**Which AI tools work?**
Any assistant reading local files: Claude, Cursor, Windsurf, Copilot, and more. Shims point them at `.agent/`; root `AGENTS.md` is auto-discovered by ~30 tools.

**Which stack?**
None forced. Only `06-templates/` is .NET/ABP-specific and loads conditionally.

**Cost per task?**
Boot ≤400 lines; one rule file at a time; references are grepped, never dumped.

**How do constitutions work?**
6 constitution files (79 rules) extracted from 16 engineering books. Loaded at pipeline stages via the Resource Injection Matrix and cited as `// [CONST-XXX-N]`.

**What is the Vertical Slice Governance?**
Every feature must cover 7 layers: Database, Domain, Application, API, Frontend, UI/UX, Tests. A report without coverage = rejected.

**What if I just want to use it without understanding the internals?**
Copy `.agent/`, paste the session prompt, give it tasks. The system handles routing and governance automatically. Everything else is optional.

---

## Contributing

Issues and PRs welcome at [Nezarabdluah/My-Programming-Workflow](https://github.com/Nezarabdluah/My-Programming-Workflow).

`01-core/` and `02-rules/` need extra-careful review — every project inherits them. Shorter files get followed more reliably: prune ruthlessly.

---

## License

MIT License — see [LICENSE](LICENSE) for details.
