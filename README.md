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

## Master Pipeline (Path D)

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

---

## QA Strategy

```
  ┌─────────────────────────────────┬───────┬──────┬──────────┐
  │ Testing Activity                │  🟢   │  🟡  │    🔴    │
  ├─────────────────────────────────┼───────┼──────┼──────────┤
  │ Unit tests (critical paths)     │  ✅   │  ✅  │   ✅     │
  │ Unit tests (comprehensive)      │  —    │  ✅  │   ✅     │
  │ Integration tests               │  —    │  ✅  │   ✅     │
  │ E2E / smoke tests               │  —    │  —   │   ✅     │
  │ Performance / load tests        │  —    │  —   │   ✅     │
  │ Security / penetration tests    │  —    │  —   │   ✅     │
  └─────────────────────────────────┴───────┴──────┴──────────┘
```

---

## Production Readiness (PRR)

10-dimension scorecard before deployment:

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  PRR SCORECARD                                                 │
  ├──────────────────────────────┬──────────────────────────────────┤
  │ 1. Reliability               │ Error handling, circuit breaker  │
  │ 2. Scalability               │ Load tested, pagination          │
  │ 3. Observability             │ Logging, tracing, metrics        │
  │ 4. Security                  │ Auth, IDOR, validation, secrets  │
  │ 5. Disaster Recovery         │ Backup, rollback, RTO/RPO        │
  │ 6. Documentation             │ API docs, ADRs, README           │
  │ 7. Operational Runbook       │ Incident response, escalation    │
  │ 8. Dependency Health         │ CVEs, licenses, SLAs             │
  │ 9. Data Management           │ Migrations, retention, PII       │
  │10. Compliance                │ Regulatory, audit trail          │
  └──────────────────────────────┴──────────────────────────────────┘

  All 🟢 → ✅ PRR PASSED
  Any 🟡 (none 🔴) → ✅ PRR PASSED with conditions
  Any 🔴 → ⛔ PRR FAILED
```

---

## Reference Library

```
  ┌──────────────────┬──────────────────────────────────────────────┐
  │ Resource         │ Description                                  │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ REF Catalog      │ 34 directives: ARCH×7 DB×7 SEC×5 NET×5     │
  │ Constitutions    │ 79 rules from 16 engineering books           │
  │ Books Archive    │ 114 lessons — grep "Lesson N"               │
  │ Prompt Packs     │ backend / frontend / debugging               │
  │ QA / DevOps      │ 11 [QA-*] anchors · 18 [OPS-*] anchors     │
  └──────────────────┴──────────────────────────────────────────────┘
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

```
  1. Say "switch tool"     → memory updates, handoff summary prints
  2. In the new tool       → paste session prompt + handoff summary
  3. Work resumes          → at the exact stopping point
```

---

## Repository Structure

```
  .agent/
  ├── AGENTS.md                  # Master directive contract
  ├── INDEX.md                   # Smart index — reach any file
  ├── VERSION                    # Version + sync info
  │
  ├── 01-core/                   # Core (mandatory at session start)
  │   ├── operating-contract.md  #   Operational contract
  │   ├── session-prompt.md      #   Unified session prompt
  │   ├── task-classification.md #   🟢/🟡/🔴 indicators
  │   ├── token-budget.md        #   ≤400 lines/session policy
  │   ├── collaboration-rules.md #   Pair programming protocol
  │   └── wiring-registry.md     #   Central DI container
  │
  ├── 02-rules/                  # Specialized rules (ONE at a time)
  │   ├── architecture-and-design.md
  │   ├── database-performance.md
  │   ├── security-checklist.md
  │   ├── testing-and-quality.md
  │   ├── network-and-api.md
  │   └── vertical-slice-governance.md
  │
  ├── 03-workflows/              # Workflows (Markdown-driven)
  │   ├── master-pipeline/       #   Stages 0–8
  │   ├── security-gate/         #   Security gate (7 steps)
  │   ├── mobile-qa/             #   Mobile QA
  │   ├── init-project.md        #   Project initialization
  │   ├── start-session.md       #   Session start protocol
  │   ├── end-session.md         #   Session end protocol
  │   ├── requirements-analysis.md # SDD spec drafting
  │   ├── debug-common-errors.md #   Bug fixing workflow
  │   ├── knowledge-bootstrapping.md # Existing project setup
  │   ├── qa-strategy.md         #   QA strategy
  │   ├── production-readiness.md #  PRR scorecard
  │   ├── create-backend-module.md
  │   ├── create-frontend-module.md
  │   └── improve-user-experience.md
  │
  ├── 04-memory/                 # Cumulative contextual memory
  │   ├── project-context.md
  │   ├── active-tasks.md
  │   ├── decisions.md           #   ADR log (5 decisions)
  │   ├── learned-mistakes.md    #   Mistake learning (Type A/B/C)
  │   ├── project-knowledge.md
  │   ├── codebase-map.md
  │   └── mistakes-archive.md
  │
  ├── 05-references/             # References (grep-only)
  │   ├── engineering-rules-catalog-REF.md
  │   ├── books/
  │   │   ├── 00-master-index.md #   Resource Injection Matrix
  │   │   ├── 00-index.md
  │   │   ├── constitutions/     #   6 constitutions (79 rules)
  │   │   └── engineering-books-16-distilled.txt
  │   ├── prompts/
  │   ├── qa-testing/
  │   └── devops-ops/
  │
  ├── 06-templates/              # Project templates
  │   ├── dotnet-abp/            #   ABP/.NET specific
  │   └── claude-skills/         #   Reference only
  │
  ├── governance/                # Deterministic enforcement
  │   ├── runner.py
  │   ├── test_memory.py
  │   ├── test_rules.py
  │   └── test_state.py
  │
  └── adr/                       # Architecture Decision Records
      └── adr-template.md
```

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
