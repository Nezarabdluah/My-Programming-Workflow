<p align="center">
  <img src="https://img.shields.io/badge/AOS-v7.0.0-blue?style=for-the-badge&labelColor=1a1a2e" alt="AOS Version"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&labelColor=1a1a2e" alt="License"/>
  <img src="https://img.shields.io/badge/works%20with-Claude%20%7C%20Cursor%20%7C%20Copilot%20%7C%20Windsurf-orange?style=for-the-badge&labelColor=1a1a2e" alt="AI Tools"/>
  <img src="https://img.shields.io/badge/stack-agnostic-Universal-grey?style=for-the-badge&labelColor=1a1a2e" alt="Stack Agnostic"/>
</p>

<h1 align="center">AOS — Agent Operating System</h1>

<p align="center">
  <strong>Turn any AI coding assistant into a governed engineering team.</strong><br/>
  <em>Every task classified. Every delivery verified. Context persists across sessions.</em>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-see-it-in-action">See It in Action</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-project-structure">Structure</a> •
  <a href="#-faq">FAQ</a>
</p>

---

## What is AOS?

AOS (Agent Operating System) is a **fully stack-agnostic framework** that transforms any AI coding assistant into a **governed engineering team**. It solves one fundamental problem:

> *AI models know good practice but never apply it consistently.*

AOS enforces mandatory resource injection, cumulative memory across sessions, and deterministic governance — so every task follows the same professional workflow, regardless of which AI tool or programming language you use.

---

## You Don't Need to Understand AOS to Use It

```
  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │   1. Copy .agent/ into your project                        │
  │   2. Start your AI with the session prompt                 │
  │   3. Give it a task                                        │
  │   4. Let the workflow handle everything                    │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

Everything else — constitutions, wiring registry, REF directives, master pipeline — is **optional documentation** for when you want to customize or extend the system.

---

## Requirements

```
  ┌─────────────────────────────┬─────────────────────────────┐
  │  REQUIRED                   │  OPTIONAL                   │
  ├─────────────────────────────┼─────────────────────────────┤
  │  Git                        │  CI/CD pipeline             │
  │  AI assistant (file-reading)│  Git hooks                  │
  │  Python 3.x (governance)    │  Spec-Kit                   │
  └─────────────────────────────┴─────────────────────────────┘
```

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
4. Read .agent/04-memory/learned-mistakes.md
5. Read .agent/04-memory/active-tasks.md
6. Read .agent/VERSION
7. Read .agent/01-core/token-budget.md
8. Read .agent/01-core/collaboration-rules.md
9. Print boot report and ask for the first task.
```

### 4. Give it a task

```text
Fix the wallet transaction sorting bug.
The API ignores the requested sorting field.
```

> ✅ The agent classifies the task, loads relevant rules, implements the fix, runs governance checks, and saves memory for the next session.

---

## See It in Action

### What You Do vs What AOS Does

```
  ┌─────────────────────────────────────────────────────────────┐
  │                    YOUR INTERACTION                         │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │   You:  "Fix wallet sorting bug"                           │
  │              │                                              │
  │              ▼                                              │
  │   AOS:   [Mode: 🟡 Medium]                                 │
  │          [Path: B → debug-common-errors.md]                 │
  │              │                                              │
  │              ▼                                              │
  │   AOS:   1. Load rules (database + testing)                │
  │          2. Grep: REF-DB-N1, REF-DB-PAG                    │
  │          3. Inspect code → find root cause                  │
  │          4. Fix: OrderService.cs:47                         │
  │          5. Run tests → 12/12 passing                       │
  │          6. Governance → ✅ PASSED                          │
  │              │                                              │
  │              ▼                                              │
  │   AOS:   ✅ Done. // [REF-DB-PAG] applied                  │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

### Bug Fix Example (Step by Step)

```
  ┌──────┬──────────────────────────────────┬──────────┐
  │ Step │ What Happens                     │ Who      │
  ├──────┼──────────────────────────────────┼──────────┤
  │  1   │ You give the task                │ You      │
  │  2   │ AOS classifies: 🟡 Medium        │ AOS      │
  │  3   │ AOS routes: Bug workflow          │ AOS      │
  │  4   │ AOS loads rules + references      │ AOS      │
  │  5   │ AOS analyzes code                 │ AOS      │
  │  6   │ AOS proposes fix                  │ AOS      │
  │  7   │ AOS implements fix                │ AOS      │
  │  8   │ AOS runs tests                    │ AOS      │
  │  9   │ AOS runs governance               │ AOS      │
  │ 10   │ AOS saves memory                  │ AOS      │
  │ 11   │ You review the result             │ You      │
  └──────┴──────────────────────────────────┴──────────┘
```

### Feature Example (With Approval Gate)

```
  ┌──────┬──────────────────────────────────┬──────────┐
  │ Step │ What Happens                     │ Who      │
  ├──────┼──────────────────────────────────┼──────────┤
  │  1   │ You: "Add email notifications"   │ You      │
  │  2   │ AOS: Classify → 🔴 Sensitive     │ AOS      │
  │  3   │ AOS: Draft spec + user stories   │ AOS      │
  │  4   │ AOS: Ask you 3 questions         │ AOS      │
  │  5   │ AOS: Present plan                │ AOS      │
  │  6   │ ⏸️  AOS STOPS — waits for you    │ You      │
  │  7   │ AOS: Implement vertically        │ AOS      │
  │  8   │ AOS: Run tests + governance      │ AOS      │
  │  9   │ AOS: Delivery report             │ AOS      │
  └──────┴──────────────────────────────────┴──────────┘
```

> **Key insight**: AOS never writes code for 🟡/🔴 tasks without your approval first.

---

## How a Task Flows

```
  ┌──────────┐     ┌──────────┐     ┌──────────┐
  │  1.BOOT  │────▶│2.CLASSIFY│────▶│ 3.ROUTE  │
  └──────────┘     └──────────┘     └──────────┘
                                          │
                    ┌─────────────────────┼─────────────────────┐
                    │                     │                     │
                    ▼                     ▼                     ▼
              ┌──────────┐         ┌──────────┐         ┌──────────┐
              │ A:Feature│         │ B:Known  │         │C:Trivial │
              │  (SDD)   │         │  Type    │         │ (do now) │
              └──────────┘         └──────────┘         └──────────┘
                    │                     │                     │
                    └─────────────────────┼─────────────────────┘
                                          │
                                          ▼
                                   ┌────────────┐
                                   │ 4. INJECT  │
                                   │   Rules    │
                                   │   Refs     │
                                   │   Prompts  │
                                   └────────────┘
                                          │
                                          ▼
                                   ┌────────────┐
                                   │5.IMPLEMENT │
                                   └────────────┘
                                          │
                                          ▼
                                   ┌────────────┐
                                   │  6.GOVERN  │
                                   │ runner.py  │
                                   └────────────┘
                                          │
                                          ▼
                                   ┌────────────┐
                                   │  7.CLOSE   │
                                   │  Memory    │
                                   │  Saved     │
                                   └────────────┘
```

### Task Classification

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  MODE      SIGNALS                         PROCESS             │
  ├─────────────────────────────────────────────────────────────────┤
  │  🟢 Simple   typo, color, comment (≤2 files)  Execute + summary│
  │  🟡 Medium   business logic, multi-file        SDD → approve   │
  │  🔴 Sensitive DB, auth, architecture (>5)      ADR + OWASP    │
  └─────────────────────────────────────────────────────────────────┘
```

### Quick Decision Matrix

```
  ┌─────────────────────────────────────────────┬──────────────────┐
  │ Question                                    │ Yes →            │
  ├─────────────────────────────────────────────┼──────────────────┤
  │ Does it touch security, auth, or perms?     │ 🔴 Sensitive     │
  │ Does it modify the database schema?         │ 🔴 Sensitive     │
  │ Does it affect more than 5 files?           │ 🔴 Sensitive     │
  │ Does it add new business logic or an API?   │ 🟡 Medium        │
  │ Is it purely visual or documentation-only?  │ 🟢 Simple        │
  └─────────────────────────────────────────────┴──────────────────┘
```

### Task Paths

```
  Path A ─── New Feature ──────── SDD spec → approve → plan → build
  Path B ─── Known Type ───────── Follow matching workflow file
  Path C ─── Trivial ──────────── Do it now, summarize
  Path D ─── Full Delivery ────── Pipeline stages 0–8
```

---

## Policy Engine

AOS applies different policies based on task classification:

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  🔴 SENSITIVE (DB / Security / Architecture)                   │
  ├─────────────────────────────────────────────────────────────────┤
  │  • ADR in decisions.md is MANDATORY                            │
  │  • OWASP security policy activated                             │
  │  • SARGable query checks activated                             │
  │  • Human Approval Gate REQUIRED before code                    │
  │  • Full compliance: rules + build + tests + security + report  │
  └─────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────┐
  │  🟡 MEDIUM (Business Logic / Multi-file)                       │
  ├─────────────────────────────────────────────────────────────────┤
  │  • Clean Code policy (functions ≤ 20 lines, units ≤ 200)      │
  │  • Automatic local test runs                                   │
  │  • Contract + build + tests required                           │
  └─────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────┐
  │  🟢 SIMPLE (Trivial / Cosmetic)                                │
  ├─────────────────────────────────────────────────────────────────┤
  │  • YAGNI policy activated                                      │
  │  • Execute immediately                                         │
  │  • Text summary only                                          │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Spec-Driven Development (SDD)

For 🟡 Medium and 🔴 Sensitive tasks, AOS follows this state machine:

```
  ┌───────┐    ┌─────────┐    ┌──────────┐    ┌─────────┐
  │ DRAFT │───▶│ CLARIFY │───▶│ APPROVED │───▶│ PLANNING│
  └───────┘    └─────────┘    └──────────┘    └─────────┘
                                     │
                                     ▼
                              ┌──────────┐    ┌───────────┐
                              │  READY   │───▶│ EXECUTING │
                              └──────────┘    └───────────┘
                                                   │
                                                   ▼
                                            ┌────────────┐    ┌──────┐
                                            │ VALIDATING │───▶│ DONE │
                                            └────────────┘    └──────┘
```

> **The ⏸️ is sacred**: no code is written before you approve the spec and plan.

---

## Conflict Resolution Priority

When rules conflict, AOS resolves by priority:

```
  ┌──────┬─────────────────────────────────────────────────────────┐
  │ Rank │ Priority                                                │
  ├──────┼─────────────────────────────────────────────────────────┤
  │  1   │ Security & data integrity (Zero Trust)                  │
  │  2   │ Cumulative memory & knowledge integrity                 │
  │  3   │ Correctness & tests (build succeeds, tests green)      │
  │  4   │ Simplicity & reversibility (YAGNI)                      │
  │  5   │ Performance & token budget                              │
  │  6   │ Language/framework conventions                          │
  └──────┴─────────────────────────────────────────────────────────┘

  If an unlisted conflict arises → STOP and ask the developer.
```

---

## Architecture

Six layers, one direction, zero ambiguity:

```
  ┌─────────────────────────────────────────────────────────┐
  │  L0  Constitution      AGENTS.md + operating contract   │  ← HIGHEST
  ├─────────────────────────────────────────────────────────┤
  │  L5  Governance        runner.py — executable truth     │
  ├─────────────────────────────────────────────────────────┤
  │  L1  Memory Core       04-memory/ — cumulative context │
  ├─────────────────────────────────────────────────────────┤
  │  L2  Pipeline          03-workflows/ — stages 0–8      │
  ├─────────────────────────────────────────────────────────┤
  │  L3  Rules             02-rules/ — 6 specialized files │
  ├─────────────────────────────────────────────────────────┤
  │  L4  References        05-references/ — grep-only       │  ← LOWEST
  └─────────────────────────────────────────────────────────┘

  Dependency flow: L0 → L5 → L1 → L2 → L3 → L4 (one-way, never reversed)
```

| Layer | Contains | Authority |
|-------|----------|-----------|
| **L0** Constitution | `AGENTS.md` + operating contract | Highest — wins every conflict |
| **L5** Governance | `runner.py` — executable checks | Overrides any model claim |
| **L1** Memory | `04-memory/` — cumulative context | Single source of truth |
| **L2** Pipeline | `03-workflows/` — stages 0–8 | Consumable, loaded per task |
| **L3** Rules | `02-rules/` — 6 files | One file at a time, never two |
| **L4** References | `05-references/` — books, REF, QA | Grep-only, never full-read |

---

## Wiring Registry

The central DI container maps capabilities to dependencies:

```
  ┌──────────────────────────┬──────────────────────┬──────────────────┐
  │ Capability               │ Rule File            │ REF Contracts    │
  ├──────────────────────────┼──────────────────────┼──────────────────┤
  │ Architecture / DDD       │ architecture-and-    │ REF-ARCH-*       │
  │                          │ design.md            │                  │
  ├──────────────────────────┼──────────────────────┼──────────────────┤
  │ Database / queries       │ database-            │ REF-DB-*         │
  │                          │ performance.md       │                  │
  ├──────────────────────────┼──────────────────────┼──────────────────┤
  │ Security / auth          │ security-            │ REF-SEC-*        │
  │                          │ checklist.md         │                  │
  ├──────────────────────────┼──────────────────────┼──────────────────┤
  │ Testing / quality        │ testing-and-         │ REF-TEST-*       │
  │                          │ quality.md           │                  │
  ├──────────────────────────┼──────────────────────┼──────────────────┤
  │ API / network            │ network-and-         │ REF-NET-*        │
  │                          │ api.md               │                  │
  ├──────────────────────────┼──────────────────────┼──────────────────┤
  │ Feature completeness     │ vertical-slice-      │ —                │
  │ (🟡/🔴)                  │ governance.md        │                  │
  └──────────────────────────┴──────────────────────┴──────────────────┘
```

**Resolution procedure:**
```
  1. Find your capability row
  2. Load the constitution (L4-C)
  3. Load the rule file (L3) — ONE at a time
  4. Grep the reference anchor (L4) — never read full file
  5. Cite in code: // [REF-DB-N1], // [CONST-SEC-3]
```

### Knowledge Bundles

AOS groups ALL related resources into **bundles** for each capability. When a capability is active, load the **entire bundle** (constitution + rules + templates + prompts + book references):

```
  ┌──────────────────────────┬──────────────────────────────────────────┐
  │ Bundle                   │ Contains                                 │
  ├──────────────────────────┼──────────────────────────────────────────┤
  │ DB Performance           │ perf-constitution + database-perf.md     │
  │                          │ + backend-prompts + entity-patterns      │
  ├──────────────────────────┼──────────────────────────────────────────┤
  │ Security                 │ security-constitution + security-        │
  │                          │ checklist + github-security-gate + PR    │
  ├──────────────────────────┼──────────────────────────────────────────┤
  │ Architecture & DDD       │ arch-constitution + ddd-constitution     │
  │                          │ + architecture-rules + coding-standards  │
  ├──────────────────────────┼──────────────────────────────────────────┤
  │ Resilience               │ resilience-constitution + testing §3     │
  ├──────────────────────────┼──────────────────────────────────────────┤
  │ API & Integration        │ integration-constitution + network-api   │
  │                          │ + backend-prompts                        │
  ├──────────────────────────┼──────────────────────────────────────────┤
  │ Testing & Quality        │ security-audit + perf-audit +            │
  │                          │ testing-rules + qa-strategy + runner     │
  ├──────────────────────────┼──────────────────────────────────────────┤
  │ Production Readiness     │ resilience-constitution + PRR + devops   │
  └──────────────────────────┴──────────────────────────────────────────┘

  See: 01-core/wiring-registry.md → Knowledge Bundles section
```

**How bundles work in practice:**

```
  Task: "Fix N+1 query in OrdersRepository"

  1. Classify → 🟡 Medium (business logic, multi-file)
  2. Identify capability → DB Performance
  3. Load FULL bundle:
     ├── perf-constitution.md           (11 rules)
     ├── database-performance.md        (7 REF-DB rules)
     ├── engineering-rules-catalog-REF  (grep REF-DB-*)
     ├── backend-prompts.md             (DB sections)
     ├── entity-patterns.md             (query patterns)
     └── engineering-books-16-distilled (grep "Lesson 5")
  4. Apply rules → cite // [REF-DB-N1] in code
  5. Run governance → ✅ PASSED
```

---

## Token Budget

AOS limits reading to prevent context overflow:

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  TOTAL CEILING: ≤ 400 lines per session                        │
  ├─────────────────────────────────────────────────────────────────┤
  │                                                                 │
  │  ALWAYS LOADED (permanent):                                     │
  │  ┌─────────────────────────────────────┬───────────────┐       │
  │  │ File                                │ Size Class    │       │
  │  ├─────────────────────────────────────┼───────────────┤       │
  │  │ AGENTS.md                           │ Light         │       │
  │  │ 01-core/operating-contract.md       │ Medium        │       │
  │  │ 04-memory/project-context.md        │ Light         │       │
  │  │ 04-memory/learned-mistakes.md       │ Light (max 20)│       │
  │  │ VERSION                             │ Tiny          │       │
  │  └─────────────────────────────────────┴───────────────┘       │
  │                                                                 │
  │  LOADED PER TASK (ONE at a time):                               │
  │  ┌─────────────────────────────────────┬───────────────┐       │
  │  │ One rules file from 02-rules/       │ Light–Medium  │       │
  │  │ One workflow file from 03-workflows/ │ Light–Medium  │       │
  │  └─────────────────────────────────────┴───────────────┘       │
  │                                                                 │
  │  NEVER AUTO-LOADED:                                             │
  │  • 05-references/* (grep only)                                  │
  │  • 06-templates/* (init only)                                   │
  │  • 04-memory/mistakes-archive.md (archive only)                │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Mistake Learning System

When the developer corrects you, classify the mistake:

```
  ┌──────────┬──────────────────────────────────────────────────────┐
  │ Type     │ Description                                          │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ Type A   │ Rule exists in 02-rules/ but you didn't follow it   │
  │          │ → Review why, add to checklist. Do NOT record.       │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ Type B   │ New project-specific knowledge                       │
  │          │ → Record in learned-mistakes.md immediately.         │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ Type C   │ Missing general rule                                 │
  │          │ → Propose adding to 02-rules/.                       │
  └──────────┴──────────────────────────────────────────────────────┘

  Rules:
  • Max 20 active mistakes (newest on top)
  • Repeated 3 times → escalates to fixed rule in 02-rules/
```

---

## Vertical Slice Governance

Every feature must cover 7 layers:

```
  ┌──────┬─────────────────────────────────────────────────────────┐
  │  #   │ Layer                                                   │
  ├──────┼─────────────────────────────────────────────────────────┤
  │  1   │ Database — Schema/Migration                             │
  │  2   │ Domain Layer — Aggregate/Entity/Value Object            │
  │  3   │ Application Layer — Service + DTOs + Validation         │
  │  4   │ API Contract — Endpoint + Authorization + Errors        │
  │  5   │ Frontend — Component + State Management                 │
  │  6   │ UI/UX & Animation — Design-system consistency           │
  │  7   │ Tests — Unit + Integration per layer                    │
  └──────┴─────────────────────────────────────────────────────────┘

  MANDATORY REPORT FORMAT:
  1. Slice coverage table: [Layer] ← [done / not applicable because...]
  2. Architectural decisions: [decision] ← [rejected alternative]
  3. Judgment calls: any deviation without a rule → state explicitly
  4. Needs human review: nominate items yourself
```

> A report without the coverage table = **automatically rejected**.

---

## Workflows

### Available Workflows

```
  ┌─────────────────────────────────┬──────────────────────────────────┐
  │ Workflow                        │ Purpose                          │
  ├─────────────────────────────────┼──────────────────────────────────┤
  │ init-project.md                 │ One-time project setup           │
  │ start-session.md                │ Session start protocol           │
  │ end-session.md                  │ Session end + memory save        │
  │ requirements-analysis.md        │ SDD spec drafting                │
  │ create-backend-module.md        │ Full backend module guide        │
  │ create-frontend-module.md       │ Frontend component guide         │
  │ improve-user-experience.md      │ UI/UX improvement workflow       │
  │ debug-common-errors.md          │ Bug fixing workflow              │
  │ knowledge-bootstrapping.md      │ Existing project setup           │
  │ qa-strategy.md                  │ QA strategy + test pyramid       │
  │ production-readiness.md         │ PRR scorecard (10 dimensions)    │
  └─────────────────────────────────┴──────────────────────────────────┘
```

### Master Pipeline (Path D)

For full project delivery, 9 stages with decision gates:

```
  ┌───────┬─────────────────────────────┬───────┬──────┬──────────┐
  │ Stage │ Name                        │  🟢   │  🟡  │    🔴    │
  ├───────┼─────────────────────────────┼───────┼──────┼──────────┤
  │   0   │ Intake & Classification     │  ✅   │  ✅  │   ✅     │
  │   1   │ Requirements & Specs        │  —    │  ✅  │   ✅     │
  │   2   │ Architecture & Design       │  —    │  —   │   ✅     │
  │   3   │ Threat Model & Security     │  —    │  —   │   ✅     │
  │   4   │ Implementation              │  ✅   │  ✅  │   ✅     │
  │   5   │ Testing & Quality Gate      │  ✅   │  ✅  │   ✅     │
  │   6   │ Production Readiness        │  —    │  —   │   ✅     │
  │   7   │ Deployment & Rollout        │  —    │  —   │   ✅     │
  │   8   │ Post-Launch Monitoring      │  —    │  —   │   ✅     │
  └───────┴─────────────────────────────┴───────┴──────┴──────────┘

  🟢 Simple   = stages 0, 4, 5 only (mini-build)
  🟡 Medium   = stages 0, 1, 4, 5 (with specs)
  🔴 Sensitive = ALL stages 0–8 (full pipeline)
```

### Security Gate (7 Steps)

```
  ┌──────┬─────────────────────────────────────────────────────────┐
  │ Step │ Name                                                    │
  ├──────┼─────────────────────────────────────────────────────────┤
  │  1   │ Threat Model (STRIDE)                                   │
  │  2   │ Dependency Check (npm audit, dotnet list)               │
  │  3   │ Secret Scan (gitleaks, API keys, passwords)             │
  │  4   │ Access Review (IDOR, default-deny, session context)     │
  │  5   │ Code Review (injection, XSS, error handling)            │
  │  6   │ Test Verification (auth tests, validation tests)        │
  │  7   │ Gate Report (PASS/FAIL with severity table)             │
  └──────┴─────────────────────────────────────────────────────────┘
```

### Mobile QA (4 Steps)

```
  ┌──────┬─────────────────────────────────────────────────────────┐
  │ Step │ Name                                                    │
  ├──────┼─────────────────────────────────────────────────────────┤
  │  1   │ Environment Discovery (framework, tools, emulators)     │
  │  2   │ Build Verification (install, build, run)                │
  │  3   │ Scenario Execution (static + runtime + triggers)        │
  │  7   │ Evidence Report (issues, coverage, health score)        │
  └──────┴─────────────────────────────────────────────────────────┘

  Modes: quick / risk / release
  Classifications: PRODUCT_DEFECT, ENVIRONMENT_DEFECT, etc.
  Severity: P0 (critical) → P3 (low)
```

---

## Constitutions

6 constitution files with 79 actionable rules extracted from 16 engineering books:

```
  ┌─────────────────────────────┬──────┬─────────────────────────────┐
  │ Constitution                │ Rules │ Focus                       │
  ├─────────────────────────────┼──────┼─────────────────────────────┤
  │ arch-constitution.md        │  15  │ Dependency Rule, SDP/SAP,   │
  │                             │      │ Fan-out, Complexity         │
  ├─────────────────────────────┼──────┼─────────────────────────────┤
  │ ddd-constitution.md         │  11  │ Ubiquitous Language,        │
  │                             │      │ Aggregates, Value Objects   │
  ├─────────────────────────────┼──────┼─────────────────────────────┤
  │ security-constitution.md    │  17  │ Zero Trust, Mass Assignment,│
  │                             │      │ TOCTOU, Validation          │
  ├─────────────────────────────┼──────┼─────────────────────────────┤
  │ perf-constitution.md        │  11  │ SARGable, No Lazy Loading,  │
  │                             │      │ Projection, NoTracking      │
  ├─────────────────────────────┼──────┼─────────────────────────────┤
  │ resilience-constitution.md  │  15  │ Optimistic Concurrency,     │
  │                             │      │ Outbox, Deadlock Prevention │
  ├─────────────────────────────┼──────┼─────────────────────────────┤
  │ integration-constitution.md │  10  │ ACL, BFF, Event Isolation,  │
  │                             │      │ Async by Default            │
  └─────────────────────────────┴──────┴─────────────────────────────┘
```

---

## Reference Library

```
  ┌──────────────────┬──────────────────────────────────────────────┐
  │ Resource         │ Description                                  │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ REF Catalog      │ 34 directives: ARCH×7 DB×7 SEC×5 NET×5     │
  │                  │ TEST×2 OBS×2 RES×1 AI×1                     │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Constitutions    │ 79 rules from 16 engineering books           │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Books Archive    │ 2337 lines, 114 lessons — grep "Lesson N"  │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Prompt Packs     │ backend / frontend / debugging               │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ QA Reference     │ 1775 lines, 11 [QA-*] anchors              │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ DevOps Reference │ 2195 lines, 18 [OPS-*] anchors             │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Templates        │ entity-patterns, coding-standards,           │
  │                  │ pre-commit, PR template, CI/CD gate         │
  └──────────────────┴──────────────────────────────────────────────┘
```

---

## Stack-Specific Templates (Optional)

```
  ┌─────────────────────────────┬─────────────────────────────────────┐
  │ Template                    │ Purpose                             │
  ├─────────────────────────────┼─────────────────────────────────────┤
  │ entity-patterns.md          │ Universal entity/model patterns     │
  │ coding-standards.md         │ SOLID, DDD, encapsulation, async    │
  │ pre-commit-template.yaml    │ Secret scan + hygiene + formatting  │
  │ github-security-gate.yml    │ CI/CD security workflow template    │
  │ pull_request_template.md    │ PR template with security gate      │
  └─────────────────────────────┴─────────────────────────────────────┘

  All templates are STACK-AGNOSTIC.
  Customize pre-commit and CI/CD for your specific stack.
```

---

## Governance Gate

```bash
python .agent/governance/runner.py
```

**10 deterministic checks** — executable ground truth, not model claims.

```
  ┌─────────────────────────┬────────────────────────┬──────────────┐
  │ Enforcement Level       │ Tag                    │ Confidence   │
  ├─────────────────────────┼────────────────────────┼──────────────┤
  │ CI pipeline ran         │ [Enforcement: CI ✅]   │ Highest      │
  │ Git hooks fired         │ [Enforcement: hooks ⚠️]│ Good         │
  │ runner.py executed      │ [Enforcement: 🔶]      │ Acceptable   │
  │ Manual checklist        │ [Enforcement: 🔶]      │ Lowest       │
  │ Model claim only        │ [Enforcement: ❌]      │ REJECTED     │
  └─────────────────────────┴────────────────────────┴──────────────┘
```

### Governance Tests

```
  ┌──────────┬─────────────────────────────────────────────────────┐
  │ Test     │ What it checks                                      │
  ├──────────┼─────────────────────────────────────────────────────┤
  │ GOV-T01  │ Feature state matches approved state machine        │
  │ GOV-T02  │ Given/When/Then acceptance criteria exist           │
  │ GOV-T03  │ ADR structure in decisions.md                       │
  │ GOV-T04  │ 20-mistake cap on active mistakes                   │
  │ GOV-T05  │ All 4 mandatory memory files exist                  │
  │ GOV-T06  │ Session prompt links to rules/ loading              │
  │ GOV-T07  │ [REF-xxx] citations match reference catalog        │
  │ GOV-T08  │ No stale/corrupt reference codes                    │
  │ GOV-T09  │ No illegal state jumps                              │
  │ GOV-T10  │ ADR accompanies engineering-rule changes            │
  └──────────┴─────────────────────────────────────────────────────┘
```

---

## Collaboration Rules

Pair programming protocol:

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  ROLES                                                         │
  ├─────────────────────────────────────────────────────────────────┤
  │  You (Driver)     : implement, write code, verify              │
  │  Developer (Nav)  : direct, review, make final decisions       │
  └─────────────────────────────────────────────────────────────────┘

  Golden Rule: Architectural decisions are NEVER delegated to the agent.
```

### Professional Execution Loop

```
  Context → Plan → Limited Execution → Hard Verification → Review
```

### Anti-Hallucination Rules

```
  ❌ "I expect this to work"           → FORBIDDEN
  ❌ Quoted terminal output (hallucinated) → FORBIDDEN
  ✅ Actual tool run with real output     → REQUIRED
```

---

## ADR Template

Architecture Decision Records with over-engineering guard:

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  ADR SECTIONS                                                  │
  ├─────────────────────────────────────────────────────────────────┤
  │  1. Status / Date / Author                                     │
  │  2. Context & Problem Statement                                │
  │  3. Decision Driver Rules (REF citations)                      │
  │  4. Alternatives Considered (pros/cons)                         │
  │  5. Chosen Decision                                            │
  │  6. Consequences & Implications                                │
  └─────────────────────────────────────────────────────────────────┘

  Over-engineering guard: ADRs reserved for HIGH-IMPACT decisions only.
```

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
1. .agent/INDEX.md
2. .agent/01-core/operating-contract.md
3. .agent/04-memory/project-context.md
4. .agent/04-memory/learned-mistakes.md
5. .agent/04-memory/active-tasks.md
6. .agent/VERSION
7. .agent/01-core/token-budget.md
8. .agent/01-core/collaboration-rules.md

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

SMART WIRING (before code): resolve via wiring-registry.md + 00-master-index.md; load ONE Knowledge Bundle for the active capability; grep 05-references/; cite // [REF-XX-N] and // [CONST-XX-N]

HANDOFF: update memory files, print handoff summary
CLOSEOUT: execute end-session.md, update all memory, print summary

FORBIDDEN: writing to main AOS source · loading two rule files at once · full-reading 05-references/ · skipping classification · coding 🟡/🔴 without approved spec+plan · ending without updating memory
```

</details>

---

## Switching AI Tools

```
  1. Say "switch tool"     → memory updates, handoff summary prints
  2. In the new tool       → paste session prompt + handoff summary
  3. Work resumes          → at the exact stopping point
```

---

## Project Structure

```
.agent/
├── AGENTS.md                      # Master directive contract
├── INDEX.md                       # Smart index — reach any file
├── VERSION                        # Version + sync info
│
├── 01-core/                       # Core (mandatory at session start)
│   ├── operating-contract.md      #   Operational contract (6 sections)
│   ├── session-prompt.md          #   Unified session prompt
│   ├── task-classification.md     #   🟢/🟡/🔴 indicators + decision matrix
│   ├── token-budget.md            #   ≤400 lines/session policy
│   ├── collaboration-rules.md     #   Pair programming protocol
│   └── wiring-registry.md         #   Central DI container + Knowledge Bundles
│
├── 02-rules/                      # Specialized rules (ONE at a time)
│   ├── architecture-and-design.md #   Clean Arch + DDD + SOLID
│   ├── database-performance.md    #   SARGability, N+1, pagination
│   ├── security-checklist.md      #   JWT, IDOR, XSS, injection
│   ├── testing-and-quality.md     #   Testing, observability, resilience
│   ├── network-and-api.md         #   API design, payload optimization
│   └── vertical-slice-governance.md # 7 layers mandatory
│
├── 03-workflows/                  # Workflows (Markdown-driven)
│   ├── master-pipeline/           #   Stages 0–8 (coordinator + 9 files)
│   │   ├── 00-coordinator.md
│   │   ├── stage-0-intake.md
│   │   ├── stage-1-requirements.md
│   │   ├── stage-2-architecture.md
│   │   ├── stage-3-threat-model.md
│   │   ├── stage-4-implementation.md
│   │   ├── stage-5-testing.md
│   │   ├── stage-6-production-readiness.md
│   │   ├── stage-7-deployment.md
│   │   └── stage-8-post-launch.md
│   ├── security-gate/             #   Security gate (coordinator + 7 steps)
│   │   ├── 00-coordinator.md
│   │   ├── step-1-threat-model.md
│   │   ├── step-2-dependency-check.md
│   │   ├── step-3-secret-scan.md
│   │   ├── step-4-access-review.md
│   │   ├── step-5-code-review.md
│   │   ├── step-6-test-verification.md
│   │   └── step-7-gate-report.md
│   ├── mobile-qa/                 #   Mobile QA (coordinator + 4 steps)
│   │   ├── 00-coordinator.md
│   │   ├── step-1-environment-discovery.md
│   │   ├── step-2-build-verification.md
│   │   ├── step-3-scenario-execution.md
│   │   └── step-7-evidence-report.md
│   ├── init-project.md            #   Project initialization
│   ├── start-session.md           #   Session start protocol
│   ├── end-session.md             #   Session end protocol
│   ├── requirements-analysis.md   #   SDD spec drafting
│   ├── create-backend-module.md   #   Full backend module guide
│   ├── create-frontend-module.md  #   Frontend component guide
│   ├── improve-user-experience.md #   UI/UX improvement
│   ├── debug-common-errors.md     #   Bug fixing workflow
│   ├── knowledge-bootstrapping.md #   Existing project setup
│   ├── qa-strategy.md             #   QA strategy + test pyramid
│   └── production-readiness.md    #   PRR scorecard (10 dimensions)
│
├── 04-memory/                     # Cumulative contextual memory
│   ├── project-context.md         #   Last project state
│   ├── active-tasks.md            #   Active tasks with SDD states
│   ├── decisions.md               #   ADR log
│   ├── learned-mistakes.md        #   Mistake learning (Type A/B/C)
│   ├── project-knowledge.md       #   Discovered patterns (on demand)
│   ├── codebase-map.md            #   File structure map (on demand)
│   └── mistakes-archive.md        #   Historical mistakes (archive)
│
├── 05-references/                 # References (grep-only)
│   ├── engineering-rules-catalog-REF.md  # 34 REF directives
│   ├── books/
│   │   ├── 00-master-index.md     #   Resource Injection Matrix
│   │   ├── constitutions/         #   6 constitutions (79 rules)
│   │   │   ├── arch-constitution.md
│   │   │   ├── ddd-constitution.md
│   │   │   ├── security-constitution.md
│   │   │   ├── perf-constitution.md
│   │   │   ├── resilience-constitution.md
│   │   │   └── integration-constitution.md
│   │   └── engineering-books-16-distilled.txt  # 2337 lines
│   ├── prompts/
│   │   ├── backend-prompts.md
│   │   ├── frontend-prompts.md
│   │   └── debugging-prompts.md
│   ├── qa-testing/
│   │   └── qa-testing-strategy-and-automation.md  # 1775 lines
│   └── devops-ops/
│       └── devops-enterprise-and-production-readiness.md  # 2195 lines
│
├── 06-templates/                  # Stack-agnostic templates
│   ├── README.md                  #   Template entry point
│   ├── entity-patterns.md         #   Universal entity/model patterns
│   ├── coding-standards.md        #   SOLID, DDD, encapsulation rules
│   ├── pre-commit-template.yaml   #   Pre-commit hooks template
│   ├── github-security-gate.yml   #   CI/CD security template
│   ├── pull_request_template.md   #   PR template with security gate
│   └── claude-skills/             #   Claude-specific skills (optional)
│
├── governance/                    # Deterministic enforcement
│   ├── runner.py                  #   Governance runner (10 checks)
│   ├── test_memory.py             #   GOV-T03, T04, T05
│   ├── test_rules.py              #   GOV-T06, T07, T08, T10
│   └── test_state.py              #   GOV-T01, T02, T09
│
└── adr/                           # Architecture Decision Records
    └── adr-template.md            #   ADR template with guard
```

---

## Compatibility

AOS works with any AI coding assistant that can read local files.

```
  ┌──────────────────┬──────────────┬────────────────┬──────────────────┐
  │ Tool             │ Auto-discover│ Session Prompt │ Notes            │
  ├──────────────────┼──────────────┼────────────────┼──────────────────┤
  │ Claude Code      │ ✅ AGENTS.md │ ✅ paste       │ Best support     │
  │ Cursor           │ ✅ .cursorrules│ ✅ paste     │ Shims → .agent/  │
  │ Windsurf         │ ✅ .windsurfrules│ ✅ paste   │ Shims → .agent/  │
  │ GitHub Copilot   │ ⚠️ partial   │ ✅ paste       │ Custom instruct. │
  │ Any file-reading │ ✅ AGENTS.md │ ✅ paste       │ ~30 tools        │
  └──────────────────┴──────────────┴────────────────┴──────────────────┘
```

---

## FAQ

<details>
<summary><b>Which AI tools work?</b></summary>

Any assistant reading local files: Claude, Cursor, Windsurf, Copilot, and more. Shims point them at `.agent/`; root `AGENTS.md` is auto-discovered by ~30 tools.
</details>

<details>
<summary><b>Which stack?</b></summary>

None forced. AOS is fully stack-agnostic. All templates in `06-templates/` are universal and customizable for any language or framework.
</details>

<details>
<summary><b>Cost per task?</b></summary>

Boot ≤400 lines; one rule file at a time; references are grepped, never dumped.
</details>

<details>
<summary><b>How do constitutions work?</b></summary>

6 constitution files (79 rules) extracted from 16 engineering books. Loaded at pipeline stages via the Resource Injection Matrix and cited as `// [CONST-XXX-N]`.
</details>

<details>
<summary><b>What is the Vertical Slice Governance?</b></summary>

Every feature must cover 7 layers: Database, Domain, Application, API, Frontend, UI/UX, Tests. A report without coverage = rejected.
</details>

<details>
<summary><b>What if I just want to use it without understanding the internals?</b></summary>

Copy `.agent/`, paste the session prompt, give it tasks. The system handles routing and governance automatically. Everything else is optional.
</details>

<details>
<summary><b>How does the memory system work across sessions?</b></summary>

AOS saves context to `04-memory/` files at the end of every session. The next session reads these files first, so the AI remembers what happened before — including mistakes, decisions, and task progress.
</details>

<details>
<summary><b>What happens if I ignore a governance check?</b></summary>

The task cannot be marked Done. `runner.py` returns FAIL with the specific test that failed. You must fix the issue before proceeding.
</details>

<details>
<summary><b>Can I use AOS without Python?</b></summary>

Yes. Python is only needed for `runner.py` governance checks. You can run the workflow manually and skip governance if needed (not recommended for production).
</details>

<details>
<summary><b>How do I add my own rules?</b></summary>

Create a new file in `02-rules/` following the existing format. Add REF directives to `engineering-rules-catalog-REF.md`. Update `wiring-registry.md` with the new capability row.
</details>

---

## Deep Dive: Boot Sequence

When you paste the session prompt, AOS reads **8 files in order**. Here's what each one does:

```
  ┌──────┬─────────────────────────────────────────────────────────────────┐
  │ Step │ File                         │ What it provides                │
  ├──────┼──────────────────────────────┼─────────────────────────────────┤
  │  1   │ INDEX.md                     │ Smart index — reach any file    │
  │      │                              │ without knowing the structure   │
  ├──────┼──────────────────────────────┼─────────────────────────────────┤
  │  2   │ operating-contract.md        │ The 6-section contract that     │
  │      │                              │ governs ALL agent behavior      │
  ├──────┼──────────────────────────────┼─────────────────────────────────┤
  │  3   │ project-context.md           │ Last known project state —      │
  │      │                              │ what was being worked on        │
  ├──────┼──────────────────────────────┼─────────────────────────────────┤
  │  4   │ learned-mistakes.md          │ Mistakes the AI made before —   │
  │      │                              │ never repeat the same error     │
  ├──────┼──────────────────────────────┼─────────────────────────────────┤
  │  5   │ active-tasks.md              │ Tasks in progress with SDD      │
  │      │                              │ state (DRAFT/CLARIFY/APPROVED)  │
  ├──────┼──────────────────────────────┼─────────────────────────────────┤
  │  6   │ VERSION                      │ Version number + last sync date │
  │      │                              │ — detects if .agent/ is stale   │
  ├──────┼──────────────────────────────┼─────────────────────────────────┤
  │  7   │ token-budget.md              │ ≤400 lines/session policy —     │
  │      │                              │ prevents context overflow       │
  ├──────┼──────────────────────────────┼─────────────────────────────────┤
  │  8   │ collaboration-rules.md       │ Pair programming protocol —     │
  │      │                              │ who decides what, when to stop  │
  └──────┴──────────────────────────────┴─────────────────────────────────┘
```

**Why this order matters:**
- INDEX.md first = the AI can navigate to any file
- operating-contract.md second = rules are loaded before any action
- Memory files = the AI knows what happened before
- VERSION = the AI can detect if .agent/ needs updating
- Token budget + collaboration rules = constraints are loaded last

**What the boot report tells you:**
```
  Session started | System: AOS v7.0 (Knowledge & Memory-first)
  Project: my-app | Stack: detected: TypeScript/React
  Memory — project-context: "fixed wallet sorting bug, 12 tests passing"
  Memory — learned-mistakes: 3 active, latest: "don't use SELECT * in queries"
  Memory — active-tasks: 1 pending, top: "add email notifications"
  VERSION: in sync ✅
```

---

## Deep Dive: Task Classification

AOS classifies every task into one of three modes. Here's how it decides:

```
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  🟢 SIMPLE                                                              │
  ├─────────────────────────────────────────────────────────────────────────┤
  │  Signals:                                                               │
  │    • Typo fix, color change, comment update                            │
  │    • Affects ≤ 2 files                                                 │
  │    • No business logic, no security, no database                       │
  │                                                                         │
  │  Process:                                                               │
  │    • Execute immediately                                               │
  │    • Summarize what was done                                           │
  │    • No approval needed                                                │
  │    • No governance check required                                      │
  │                                                                         │
  │  Examples:                                                              │
  │    "Fix the typo in README.md"                                         │
  │    "Change button color from blue to green"                            │
  │    "Update the copyright year"                                         │
  └─────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────────┐
  │  🟡 MEDIUM                                                              │
  ├─────────────────────────────────────────────────────────────────────────┤
  │  Signals:                                                               │
  │    • New business logic or API endpoint                                │
  │    • Affects 3–5 files                                                │
  │    • No security/auth changes                                         │
  │    • No database schema changes                                        │
  │                                                                         │
  │  Process:                                                               │
  │    • Follow SDD: Draft → Clarify → Approved → Planning → Executing     │
  │    • ⏸️ STOP for approval before writing code                          │
  │    • Load relevant Knowledge Bundle                                    │
  │    • Run governance check                                              │
  │                                                                         │
  │  Examples:                                                              │
  │    "Add pagination to the products API"                                │
  │    "Create a new user profile page"                                    │
  │    "Implement search functionality"                                    │
  └─────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────────┐
  │  🔴 SENSITIVE                                                           │
  ├─────────────────────────────────────────────────────────────────────────┤
  │  Signals:                                                               │
  │    • Security, auth, or permission changes                             │
  │    • Database schema modifications                                     │
  │    • Architecture changes (new module, microservice)                   │
  │    • Affects > 5 files                                                │
  │    • Financial, health, or safety-critical data                        │
  │                                                                         │
  │  Process:                                                               │
  │    • Full SDD + ADR in decisions.md is MANDATORY                       │
  │    • OWASP security policy activated                                   │
  │    • ⏸️ STOP for approval before writing code                          │
  │    • Load ALL relevant Knowledge Bundles                               │
  │    • Run full governance + security gate                               │
  │                                                                         │
  │  Examples:                                                              │
  │    "Add JWT authentication to the API"                                 │
  │    "Migrate user table to new schema"                                  │
  │    "Refactor into microservices"                                       │
  │    "Add role-based access control"                                     │
  └─────────────────────────────────────────────────────────────────────────┘
```

**Decision flow:**
```
  Does it touch security/auth/permissions?
    → YES = 🔴 Sensitive
    → NO ↓

  Does it modify database schema?
    → YES = 🔴 Sensitive
    → NO ↓

  Does it affect > 5 files?
    → YES = 🔴 Sensitive
    → NO ↓

  Does it add new business logic or API?
    → YES = 🟡 Medium
    → NO ↓

  Is it purely visual or documentation?
    → YES = 🟢 Simple
    → NO = 🟡 Medium (default)
```

---

## Deep Dive: Spec-Driven Development (SDD)

For 🟡 and 🔴 tasks, AOS follows a strict state machine. Here's what happens at each state:

```
  ┌───────┐
  │ DRAFT │  The AI writes a specification document:
  └───────┘  • User stories with Given/When/Then
              • Acceptance criteria
              • Affected files list
              • Risk assessment
                │
                ▼
  ┌─────────┐
  │ CLARIFY │  The AI asks you questions:
  └─────────┘  • "Should this support batch operations?"
                • "What's the expected response time?"
                • "Should we keep backward compatibility?"
                │
                ▼
  ┌──────────┐
  │ APPROVED │  You review and approve the spec:
  └──────────┘  • ✅ Approved → proceed to planning
                • ❌ Rejected → back to DRAFT
                • 🔄 Revise → back to CLARIFY
                │
                ▼
  ┌─────────┐
  │PLANNING │  The AI creates a technical plan:
  └─────────┘  • File-by-file implementation plan
                • Test strategy
                • Migration steps
                • Rollback plan
                │
                ▼
  ┌───────┐
  │ READY │  Plan is approved. Ready to implement.
  └───────┘  ⏸️ Final checkpoint before code.
                │
                ▼
  ┌───────────┐
  │ EXECUTING │  The AI writes code:
  └───────────┘  • Implements file by file
                  • Cites // [REF-XXX-N] for every rule
                  • Runs tests after each change
                  • Stops if any test fails
                  │
                  ▼
  ┌────────────┐
  │ VALIDATING │  Verification:
  └────────────┘  • All tests pass
                  • Governance checks pass
                  • Security scan clean
                  • Vertical slice coverage complete
                  │
                  ▼
  ┌──────┐
  │ DONE │  Memory saved. Handoff summary printed.
  └──────┘  Ready for next task.
```

**The ⏸️ is sacred:**
- No code is written before APPROVED state
- No implementation before READY state
- This prevents wasted effort on wrong solutions

---

## Deep Dive: Security Gate

The Security Gate runs 7 checks before any 🔴 Sensitive task can be marked Done:

```
  ┌──────┬──────────────────────────────────────────────────────────────────┐
  │ Step │ What it checks                    │ How it works                │
  ├──────┼───────────────────────────────────┼─────────────────────────────┤
  │  1   │ Threat Model (STRIDE)              │ Identifies Spoofing,       │
  │      │                                   │ Tampering, Repudiation,    │
  │      │                                   │ Info Disclosure, DoS,      │
  │      │                                   │ Elevation of Privilege     │
  ├──────┼───────────────────────────────────┼─────────────────────────────┤
  │  2   │ Dependency Check                   │ Runs npm audit / dotnet    │
  │      │                                   │ list vuln / pip audit      │
  │      │                                   │ — no known CVEs allowed    │
  ├──────┼───────────────────────────────────┼─────────────────────────────┤
  │  3   │ Secret Scan                        │ Scans for API keys,        │
  │      │                                   │ passwords, tokens in code  │
  │      │                                   │ — blocks commit if found   │
  ├──────┼───────────────────────────────────┼─────────────────────────────┤
  │  4   │ Access Review                      │ Checks IDOR, default-deny, │
  │      │                                   │ session context validation │
  ├──────┼───────────────────────────────────┼─────────────────────────────┤
  │  5   │ Code Review                        │ Checks for injection,      │
  │      │                                   │ XSS, error handling gaps   │
  ├──────┼───────────────────────────────────┼─────────────────────────────┤
  │  6   │ Test Verification                  │ Confirms auth tests exist, │
  │      │                                   │ validation tests pass      │
  ├──────┼───────────────────────────────────┼─────────────────────────────┤
  │  7   │ Gate Report                        │ PASS/FAIL with severity    │
  │      │                                   │ table + remediation steps  │
  └──────┴───────────────────────────────────┴─────────────────────────────┘
```

**Severity levels:**
```
  P0 (Critical) → blocks deployment, must fix now
  P1 (High)     → must fix before merge
  P2 (Medium)   → should fix in this sprint
  P3 (Low)      → track for future
```

---

## Deep Dive: Mobile QA

Mobile QA has 3 modes for different scenarios:

```
  ┌──────────┬─────────────────────────────────────────────────────────────┐
  │ Mode     │ When to use                                                 │
  ├──────────┼─────────────────────────────────────────────────────────────┤
  │ quick    │ Daily dev — fast smoke test (5 min)                        │
  │          │ Checks: build success, basic UI loads, no crashes          │
  ├──────────┼─────────────────────────────────────────────────────────────┤
  │ risk     │ Pre-PR — thorough check (15 min)                           │
  │          │ Checks: all scenarios, edge cases, memory leaks            │
  ├──────────┼─────────────────────────────────────────────────────────────┤
  │ release  │ Pre-production — full regression (30+ min)                 │
  │          │ Checks: everything + performance + accessibility           │
  └──────────┴─────────────────────────────────────────────────────────────┘
```

**Issue classification:**
```
  PRODUCT_DEFECT      → bug in your code (fix it)
  ENVIRONMENT_DEFECT  → issue with dev tools/emulator (not your code)
  CONFIG_DEFECT       → wrong configuration (fix config)
  PLATFORM_DEFECT     → OS/browser bug (document, can't fix)
```

---

## Deep Dive: Governance System

The governance runner (`runner.py`) runs **10 deterministic checks**. Here's what each one does:

```
  ┌──────────┬─────────────────────────────────────────────────────────────┐
  │ Test     │ What it checks                          │ Why it matters   │
  ├──────────┼─────────────────────────────────────────┼──────────────────┤
  │ GOV-T01  │ Feature state matches approved state    │ Prevents skipping│
  │          │ machine (no DRAFT → DONE jumps)         │ approval gates  │
  ├──────────┼─────────────────────────────────────────┼──────────────────┤
  │ GOV-T02  │ Given/When/Then acceptance criteria     │ Specs must be   │
  │          │ exist for 🟡/🔴 tasks                   │ testable        │
  ├──────────┼─────────────────────────────────────────┼──────────────────┤
  │ GOV-T03  │ ADR structure in decisions.md           │ Decisions must  │
  │          │ (status, context, decision,后果)        │ be documented   │
  ├──────────┼─────────────────────────────────────────┼──────────────────┤
  │ GOV-T04  │ 20-mistake cap on active mistakes       │ Prevents bloat  │
  │          │                                         │ in memory       │
  ├──────────┼─────────────────────────────────────────┼──────────────────┤
  │ GOV-T05  │ All 4 mandatory memory files exist      │ Memory must be  │
  │          │ (project-context, active-tasks,         │ persistent      │
  │          │  learned-mistakes, decisions)           │                 │
  ├──────────┼─────────────────────────────────────────┼──────────────────┤
  │ GOV-T06  │ Session prompt links to rules/ loading  │ Rules must be   │
  │          │                                         │ accessible      │
  ├──────────┼─────────────────────────────────────────┼──────────────────┤
  │ GOV-T07  │ [REF-xxx] citations match reference     │ No fake rules   │
  │          │ catalog                                 │ — cite real ones│
  ├──────────┼─────────────────────────────────────────┼──────────────────┤
  │ GOV-T08  │ No stale/corrupt reference codes        │ Old/broken refs │
  │          │                                         │ must be cleaned │
  ├──────────┼─────────────────────────────────────────┼──────────────────┤
  │ GOV-T09  │ No illegal state jumps                  │ SDD states must │
  │          │ (e.g., DRAFT → DONE directly)           │ be followed     │
  ├──────────┼─────────────────────────────────────────┼──────────────────┤
  │ GOV-T10  │ ADR accompanies engineering-rule        │ Rule changes    │
  │          │ changes                                 │ need approval   │
  └──────────┴─────────────────────────────────────────┴──────────────────┘
```

**Enforcement levels:**
```
  [Enforcement: CI ✅]    → ran in CI pipeline (highest confidence)
  [Enforcement: hooks ⚠️] → git hooks fired (good confidence)
  [Enforcement: 🔶]       → runner.py executed (acceptable)
  [Enforcement: ❌]       → model claim only (REJECTED)
```

---

## Deep Dive: Memory System

AOS remembers everything across sessions through 7 memory files:

```
  ┌──────────────────────┬───────────────────────────────────────────────┐
  │ File                 │ What it stores                                │
  ├──────────────────────┼───────────────────────────────────────────────┤
  │ project-context.md   │ Last task, modified files, completion notes  │
  │                      │ "Fixed wallet sorting, OrderService.cs:47"   │
  ├──────────────────────┼───────────────────────────────────────────────┤
  │ active-tasks.md      │ Tasks in progress with SDD state             │
  │                      │ "Add email notifications — state: APPROVED"  │
  ├──────────────────────┼───────────────────────────────────────────────┤
  │ learned-mistakes.md  │ Mistakes the AI made (max 20)               │
  │                      │ "Don't use SELECT * — use projections"       │
  ├──────────────────────┼───────────────────────────────────────────────┤
  │ decisions.md         │ Architecture Decision Records                │
  │                      │ "Chose PostgreSQL over MongoDB because..."   │
  ├──────────────────────┼───────────────────────────────────────────────┤
  │ project-knowledge.md │ Discovered patterns (on demand)             │
  │                      │ "Codebase uses Repository pattern"           │
  ├──────────────────────┼───────────────────────────────────────────────┤
  │ codebase-map.md      │ File structure map (on demand)              │
  │                      │ "src/services/OrderService.cs — 200 lines"  │
  ├──────────────────────┼───────────────────────────────────────────────┤
  │ mistakes-archive.md  │ Historical mistakes (archive only)          │
  │                      │ Old mistakes moved here after 20 cap        │
  └──────────────────────┴───────────────────────────────────────────────┘
```

**How learning works:**
```
  Session 1: AI makes mistake → "used SELECT * in query"
             → Recorded in learned-mistakes.md

  Session 2: AI reads learned-mistakes.md
             → Sees "don't use SELECT *"
             → Applies projection instead

  Session 3: Same mistake happens again
             → Count increments (2/3)
             → Still in learned-mistakes.md

  Session 4: Same mistake happens 3rd time
             → ESCALATES to fixed rule in 02-rules/
             → Removed from learned-mistakes.md
             → Permanent rule everyone follows
```

---

## Deep Dive: Reference System

AOS has a layered reference system. Here's how it works:

```
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  Layer 4 (Lowest): References                                          │
  ├─────────────────────────────────────────────────────────────────────────┤
  │                                                                         │
  │  Files in 05-references/ are NEVER read in full.                       │
  │  They are GREPped for specific anchors:                                │
  │                                                                         │
  │  grep "REF-DB-N1" engineering-rules-catalog-REF.md                    │
  │  grep "QA-PYRAMID" qa-testing-strategy-and-automation.md              │
  │  grep "OPS-DEPLOY" devops-enterprise-and-production-readiness.md      │
  │  grep "Lesson 5" engineering-books-16-distilled.txt                   │
  │                                                                         │
  │  This keeps context usage minimal while accessing deep knowledge.     │
  │                                                                         │
  └─────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────────┐
  │  Layer 3: Rules                                                         │
  ├─────────────────────────────────────────────────────────────────────────┤
  │                                                                         │
  │  Only ONE rule file loaded at a time. Never two.                      │
  │  Each rule file contains REF directives:                               │
  │                                                                         │
  │  REF-DB-N1: Prevent N+1 queries — use Include/ThenInclude             │
  │  REF-DB-PAG: Use cursor-based pagination, not OFFSET                  │
  │  REF-SEC-3: Mass Assignment Protection — explicit DTO binding         │
  │                                                                         │
  │  You cite these in code: // [REF-DB-N1]: applied                      │
  │                                                                         │
  └─────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────────┐
  │  Layer 4-C: Constitutions                                               │
  ├─────────────────────────────────────────────────────────────────────────┤
  │                                                                         │
  │  79 actionable rules extracted from 16 engineering books.             │
  │  Each constitution is a focused domain:                                │
  │                                                                         │
  │  arch-constitution.md     → 15 rules (Dependency Rule, SDP/SAP)       │
  │  ddd-constitution.md      → 11 rules (Aggregates, Value Objects)      │
  │  security-constitution.md → 17 rules (Zero Trust, TOCTOU)             │
  │  perf-constitution.md     → 11 rules (SARGable, No Lazy Loading)      │
  │  resilience-constitution.md → 15 rules (Outbox, Deadlock Prevention)  │
  │  integration-constitution.md → 10 rules (ACL, BFF, Async by Default) │
  │                                                                         │
  │  You cite these: // [CONST-SEC-3]: Mass Assignment Protection         │
  │                                                                         │
  └─────────────────────────────────────────────────────────────────────────┘
```

**Citation rules:**
```
  ✅ // [REF-DB-N1]: prevent N+1 query
  ✅ // [CONST-SEC-3]: Mass Assignment Protection
  ✅ // [PROMPT-BE]: backend prompt applied
  ❌ // TODO: fix this later
  ❌ // hardcoded for now
```

---

## Deep Dive: Conflict Resolution

When rules conflict, AOS resolves by priority:

```
  Example 1: Security vs Performance
  ─────────────────────────────────────
  Security says: "Encrypt all database fields"
  Performance says: "Minimize encryption overhead"

  Resolution: Security wins (Rank 1 > Rank 5)
  → Encrypt, but use hardware-accelerated encryption

  Example 2: Simplicity vs Correctness
  ─────────────────────────────────────
  Simplicity says: "Use a simple array"
  Correctness says: "Use a thread-safe collection"

  Resolution: Correctness wins (Rank 3 > Rank 4)
  → Use thread-safe collection, even if more complex

  Example 3: Performance vs Conventions
  ─────────────────────────────────────
  Performance says: "Use raw SQL for this query"
  Conventions says: "Use ORM for all queries"

  Resolution: Performance wins (Rank 5 > Rank 6)
  → Use raw SQL, but document why

  Example 4: Unknown conflict
  ─────────────────────────────────────
  Two rules conflict and neither is clearly higher rank.

  Resolution: STOP and ask the developer.
  → Never guess on ambiguous conflicts
```

---

## Deep Dive: Vertical Slice Governance

Every feature must cover 7 layers. Here's what each layer means:

```
  ┌──────┬──────────────────────────────────────────────────────────────────┐
  │  #   │ Layer                   │ What to deliver                       │
  ├──────┼──────────────────────────┼──────────────────────────────────────┤
  │  1   │ Database                │ Schema migration, index changes,     │
  │      │                         │ seed data if needed                  │
  ├──────┼──────────────────────────┼──────────────────────────────────────┤
  │  2   │ Domain Layer            │ Aggregate root, entities, value      │
  │      │                         │ objects, domain events               │
  ├──────┼──────────────────────────┼──────────────────────────────────────┤
  │  3   │ Application Layer       │ Service class, DTOs, validation,     │
  │      │                         │ business rules                       │
  ├──────┼──────────────────────────┼──────────────────────────────────────┤
  │  4   │ API Contract            │ Endpoint, request/response DTOs,     │
  │      │                         │ authorization, error responses       │
  ├──────┼──────────────────────────┼──────────────────────────────────────┤
  │  5   │ Frontend                │ Component, state management, API     │
  │      │                         │ integration, error handling          │
  ├──────┼──────────────────────────┼──────────────────────────────────────┤
  │  6   │ UI/UX & Animation       │ Design-system consistency,           │
  │      │                         │ loading states, transitions          │
  ├──────┼──────────────────────────┼──────────────────────────────────────┤
  │  7   │ Tests                   │ Unit tests per layer, integration    │
  │      │                         │ tests, edge case coverage            │
  └──────┴──────────────────────────┴──────────────────────────────────────┘
```

**Mandatory report format:**
```
  Slice Coverage:
  ┌──────┬──────────────────────────────────────────────────────────┐
  │  1   │ Database       ✅ migration added                        │
  │  2   │ Domain         ✅ OrderAggregate + OrderItem entity      │
  │  3   │ Application    ✅ OrderService + CreateOrderDTO          │
  │  4   │ API Contract   ✅ POST /api/orders                       │
  │  5   │ Frontend       ✅ OrderForm component                    │
  │  6   │ UI/UX          ✅ loading spinner + success toast        │
  │  7   │ Tests          ✅ 8 unit + 2 integration                 │
  └──────┴──────────────────────────────────────────────────────────┘

  Architectural decisions:
  • Used Repository pattern (rejected: direct DbContext access)

  Judgment calls:
  • Skipped animation (not applicable for API-only feature)

  Needs human review:
  • OrderItem value object design — please confirm
```

---

## Deep Dive: How to Extend AOS

### Add a new rule

```
  1. Create 02-rules/my-new-rule.md
  2. Add REF directives to 05-references/engineering-rules-catalog-REF.md
  3. Update wiring-registry.md with new capability row
  4. Update 05-references/books/00-master-index.md with new stage mapping
```

### Add a new workflow

```
  1. Create 03-workflows/my-workflow.md
  2. Follow existing format (headers, steps, output format)
  3. Reference applicable rules and constitutions
  4. Update INDEX.md with new workflow entry
```

### Add a new knowledge bundle

```
  1. Edit 01-core/wiring-registry.md
  2. Add new bundle section under "Knowledge Bundles"
  3. List ALL files in the bundle (constitution + rules + templates + refs)
  4. Update 05-references/books/00-master-index.md with bundle reference
```

### Add a new template

```
  1. Create 06-templates/my-template.md
  2. Follow existing format (stack-agnostic)
  3. Update 06-templates/README.md with new template entry
  4. Reference it in relevant Knowledge Bundles
```

---

## Deep Dive: Troubleshooting

### Common issues and solutions

```
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ Problem                        │ Solution                               │
  ├─────────────────────────────────┼───────────────────────────────────────┤
  │ AI doesn't load rules          │ Check session prompt is correct       │
  │                                │ Verify .agent/02-rules/ exists        │
  ├─────────────────────────────────┼───────────────────────────────────────┤
  │ AI ignores memory              │ Check 04-memory/ files exist          │
  │                                │ Verify boot reads all 8 files        │
  ├─────────────────────────────────┼───────────────────────────────────────┤
  │ Governance check fails         │ Read the specific GOV-T## test       │
  │                                │ Fix the issue it reports             │
  ├─────────────────────────────────┼───────────────────────────────────────┤
  │ AI writes code for 🟡/🔴      │ Approval gate was skipped            │
  │ without approval               │ Re-read session-prompt.md Step 3     │
  ├─────────────────────────────────┼───────────────────────────────────────┤
  │ Two rule files loaded at once  │ Violates "ONE at a time" rule        │
  │                                │ Unload one, keep only the relevant   │
  ├─────────────────────────────────┼───────────────────────────────────────┤
  │ Context overflow (>400 lines)  │ Too many files loaded                │
  │                                │ Unload non-essential files           │
  ├─────────────────────────────────┼───────────────────────────────────────┤
  │ VERSION out of sync            │ Copy fresh .agent/ from source       │
  │                                │ Or run init-project.md workflow      │
  ├─────────────────────────────────┼───────────────────────────────────────┤
  │ REF citation not found         │ Check engineering-rules-catalog-REF  │
  │                                │ Verify the REF-XXX-N code exists     │
  └─────────────────────────────────────────────────────────────────────────┘
```

---

## Contributing

Issues and PRs welcome at [Nezarabdluah/My-Programming-Workflow](https://github.com/Nezarabdluah/My-Programming-Workflow).

`01-core/` and `02-rules/` need extra-careful review — every project inherits them. Shorter files get followed more reliably: prune ruthlessly.

---

## License

MIT License — see [LICENSE](LICENSE) for details.
