<p align="center">
  <h1 align="center">🤖 AOS — Agent Operating System</h1>
  <p align="center">
    <strong>v8.0-dev</strong> · نظام حوكمة وتشغيل وكلاء البرمجة<br>
    مستقل عن اللغة · مستقل عن الإطار · مستقل عن المحرر
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-8.0--dev-blue" alt="version">
  <img src="https://img.shields.io/badge/governance-11%2F11%20PASS-brightgreen" alt="governance">
  <img src="https://img.shields.io/badge/books-16%20distilled-purple" alt="books">
  <img src="https://img.shields.io/badge/constitutions-6%20(79%20rules)-orange" alt="constitutions">
  <img src="https://img.shields.io/badge/pipeline-9%20stages-red" alt="pipeline">
  <img src="https://img.shields.io/badge/mutations-6%2F6%20detected-brightgreen" alt="mutations">
</p>

---

## 🎯 What is AOS?

AOS turns any AI coding agent into a **governed, memory-aware, knowledge-powered** engineering partner.

It's not just rules — it's a **complete knowledge system** built from 16 engineering books, distilled into actionable constitutions, wired together through a dependency injection registry, and enforced by automated governance.

```
  ┌──────────────────────────────────────────────────────────────┐
  │                         AOS v8.0                             │
  │                                                              │
  │   📚 16 Books ──► 📜 6 Constitutions ──► 📏 34 REF Rules   │
  │                          │                      │            │
  │                          ▼                      ▼            │
  │                   📦 7 Knowledge Bundles                     │
  │                          │                                   │
  │                          ▼                                   │
  │                   🔌 Wiring Registry                         │
  │                    (connects everything)                     │
  │                          │                                   │
  │              ┌───────────┼───────────┐                       │
  │              ▼           ▼           ▼                       │
  │         🏭 Pipeline  🤖 Agent   ✅ Governance               │
  │         (9 stages)   (guided)   (11 checks)                 │
  │              │           │           │                       │
  │              └───────────┼───────────┘                       │
  │                          ▼                                   │
  │                    💾 Memory                                 │
  │               (persists across sessions)                     │
  └──────────────────────────────────────────────────────────────┘
```

---

## ⚡ Quick Start

### Method 1: Automatic (just open your project)
If you use any of these tools, AOS loads automatically — **no setup needed**:

| Tool | Auto-reads | Status |
|------|-----------|--------|
| **Cursor** | `.cursorrules` | ✅ Works automatically |
| **Claude Code** | `CLAUDE.md` | ✅ Works automatically |
| **GitHub Copilot** | `.github/copilot-instructions.md` | ✅ Works automatically |
| **Antigravity** | `AGENTS.md` | ✅ Works automatically |
| **Any other AI** | See Method 2 below | 📋 One command |

### Method 2: One command (any AI tool)
```bash
python .agent/start.py --copy
```
This copies the full boot prompt to your clipboard. Paste it into any AI chat — done.

### Method 3: Manual
Just tell your AI:
> Read `AGENTS.md` at the project root and follow its instructions.

### Setup (first time only)
```bash
git clone https://github.com/Nezarabdluah/My-Programming-Workflow.git
cp -r My-Programming-Workflow/.agent  /path/to/your/project/
cp My-Programming-Workflow/AGENTS.md  /path/to/your/project/
cp My-Programming-Workflow/CLAUDE.md  /path/to/your/project/
cp My-Programming-Workflow/.cursorrules /path/to/your/project/
cp -r My-Programming-Workflow/.github /path/to/your/project/
```

### Useful Commands
```bash
python .agent/start.py          # Print boot prompt to screen
python .agent/start.py --copy   # Copy boot prompt to clipboard
python .agent/start.py --check  # Run governance checks
```

---

## 📁 Project Structure

```
your-project/
├── AGENTS.md                          ← 🚪 Entry point
└── .agent/
    ├── 01-core/
    │   ├── boot-manifest.md           ← 🧠 Loaded every session (~106 lines)
    │   ├── wiring-registry.md         ← 🔌 Connects everything to everything
    │   └── task-classification.md     ← 🏷️ Detailed classification rules
    │
    ├── 02-rules/                      ← 📏 Engineering rules (one at a time)
    │   ├── architecture-and-design.md ←    SOLID, DDD, Clean Architecture
    │   ├── database-performance.md    ←    N+1, SARGable, indexing
    │   ├── security-checklist.md      ←    OWASP, auth, XSS, BOLA
    │   ├── testing-and-quality.md     ←    Test pyramid, coverage
    │   ├── network-and-api.md         ←    API design, latency, resilience
    │   └── vertical-slice-governance.md ←  Full-stack slice verification
    │
    ├── 03-workflows/                  ← 🔄 Step-by-step procedures
    │   ├── master-pipeline/           ←    🏭 9-stage full project lifecycle
    │   │   ├── 00-coordinator.md      ←       Orchestrates all stages
    │   │   ├── stage-0-intake.md      ←       Classify & scope
    │   │   ├── stage-1-requirements.md←       Specs & user stories
    │   │   ├── stage-2-architecture.md←       ADR & design
    │   │   ├── stage-3-threat-model.md←       STRIDE security analysis
    │   │   ├── stage-4-implementation.md←     Code with full bundles
    │   │   ├── stage-5-testing.md     ←       Quality gate
    │   │   ├── stage-6-production-readiness.md ← PRR scorecard
    │   │   ├── stage-7-deployment.md  ←       Rollout & rollback
    │   │   └── stage-8-post-launch.md ←       Monitoring & DORA
    │   ├── mobile-qa/                 ←    📱 Mobile testing (5 steps)
    │   ├── security-gate/             ←    🔐 Security review (7 steps)
    │   └── *.md                       ←    Other workflows
    │
    ├── 04-memory/                     ← 💾 Persistent across sessions
    │   ├── project-context.md         ←    Where we stopped
    │   ├── active-tasks.md            ←    Current work
    │   ├── learned-mistakes.md        ←    Don't repeat (max 20)
    │   └── decisions.md               ←    Architecture decisions (ADRs)
    │
    ├── 05-references/                 ← 📚 Knowledge base (grep only!)
    │   ├── engineering-rules-catalog-REF.md  ← 34 REF rules
    │   ├── books/
    │   │   ├── 00-master-index.md     ←    Resource Injection Matrix
    │   │   ├── engineering-books-16-distilled.txt ← 16 books distilled
    │   │   └── constitutions/         ←    6 constitutions (79 rules)
    │   ├── prompts/                   ←    Backend/Frontend/Debug prompts
    │   ├── devops-ops/                ←    DevOps & production reference
    │   └── qa-testing/                ←    QA strategy reference
    │
    └── governance/                    ← ✅ Automated enforcement
        ├── runner.py                  ←    11 checks + JSON output
        ├── test_state.py              ←    State machine validation
        ├── test_rules.py              ←    Rule & ADR verification
        ├── test_memory.py             ←    Memory & boot budget
        └── test_mutations.py          ←    Anti-rubber-stamp proofs
```

---

## 📚 Knowledge System — How Everything Connects

This is the heart of AOS. It's not random files — it's a **pipeline from books to code**:

```
  ┌─────────────────────────────────────────────────────────────┐
  │                    KNOWLEDGE PIPELINE                        │
  │                                                              │
  │  📖 16 Engineering Books                                    │
  │  (Clean Code, DDD, DDIA, OWASP, Accelerate, etc.)          │
  │       │                                                      │
  │       ▼ distilled into                                       │
  │  📜 6 Constitutions (79 actionable rules)                   │
  │  ┌──────────────┬──────────────┬──────────────┐             │
  │  │ Architecture │  Security    │  Performance │             │
  │  │  (15 rules)  │  (17 rules)  │  (11 rules)  │             │
  │  ├──────────────┼──────────────┼──────────────┤             │
  │  │     DDD      │  Resilience  │ Integration  │             │
  │  │  (11 rules)  │  (15 rules)  │  (10 rules)  │             │
  │  └──────────────┴──────────────┴──────────────┘             │
  │       │                                                      │
  │       ▼ organized into                                       │
  │  📦 7 Knowledge Bundles                                     │
  │  (each = constitution + rules + templates + prompts + refs) │
  │       │                                                      │
  │       ▼ wired through                                        │
  │  🔌 Wiring Registry (capability → full dependency map)      │
  │       │                                                      │
  │       ▼ injected at                                          │
  │  🏭 The right pipeline stage, at the right time             │
  └─────────────────────────────────────────────────────────────┘
```

### The 7 Knowledge Bundles

Each bundle groups **ALL** related resources for a capability:

| Bundle | Constitution | Rules | What it enforces |
|--------|-------------|-------|-----------------|
| 🏗️ **Architecture & DDD** | arch + ddd (26 rules) | REF-ARCH-* | Layer isolation, Aggregates, SOLID |
| 🗄️ **DB Performance** | perf (11 rules) | REF-DB-* | SARGable, N+1 prevention, indexing |
| 🔒 **Security** | security (17 rules) | REF-SEC-* | OWASP, Zero Trust, XSS, BOLA |
| 🧪 **Testing & Quality** | security + perf (audit) | REF-TEST-* | Test pyramid, coverage, quality gates |
| 🔄 **Resilience** | resilience (15 rules) | REF-RES-* | Circuit breaker, concurrency, outbox |
| 🌐 **API & Integration** | integration (10 rules) | REF-NET-* | API design, latency, boundaries |
| 🚀 **Production Readiness** | resilience | REF-OPS-* | PRR scorecard, DORA metrics |

### How Bundles Get Loaded

```
  Task arrives: "Add user authentication"
       │
       ▼
  🏷️ Classify: 🔴 Sensitive (touches auth/security)
       │
       ▼
  🔌 Wiring Registry lookup:
     capability = "Security / auth"
       │
       ▼
  📦 Load Security Bundle:
     ├── security-constitution.md (17 rules)
     ├── security-checklist.md (REF-SEC rules)
     ├── engineering-rules-catalog-REF.md (grep REF-SEC-*)
     ├── github-security-gate.yml
     └── devops reference (grep OPS-SECTEST)
       │
       ▼
  🤖 Agent writes code with ALL 17 security rules enforced
```

### 🔌 Knowledge Wiring — The 7 Mandatory Steps

Before writing ANY code, the agent MUST follow these steps:

```
  ┌─────────────────────────────────────────────────────────────┐
  │              KNOWLEDGE WIRING PROTOCOL                      │
  │                                                              │
  │  Step 1  📖 Read wiring-registry.md                         │
  │               → find your capability row                     │
  │                        │                                     │
  │  Step 2  📜 Load Constitution(s)                            │
  │               arch-constitution.md  (15 rules)               │
  │               ddd-constitution.md   (11 rules)               │
  │               security-constitution.md (17 rules)            │
  │               perf-constitution.md  (11 rules)               │
  │               resilience-constitution.md (15 rules)          │
  │               integration-constitution.md (10 rules)         │
  │                        │                                     │
  │  Step 3  📏 Load Rule File                                  │
  │               ONE from 02-rules/ per wiring row              │
  │                        │                                     │
  │  Step 4  🔍 Grep REF Contracts                              │
  │               engineering-rules-catalog-REF.md               │
  │               grep REF-ARCH-*, REF-DB-*, REF-SEC-*, etc.    │
  │                        │                                     │
  │  Step 5  📚 Grep Books (if listed in wiring row)            │
  │               engineering-books-16-distilled.txt             │
  │               by lesson number or keyword                    │
  │                        │                                     │
  │  Step 6  💬 Load Prompts (if relevant)                      │
  │               backend-prompts.md                             │
  │               frontend-prompts.md                            │
  │               debugging-prompts.md                           │
  │                        │                                     │
  │  Step 7  📋 Consult Master Index (for pipeline stages)      │
  │               books/00-master-index.md                       │
  │               = stage-by-stage resource injection map        │
  │                        │                                     │
  │               ▼▼▼                                            │
  │  ✅ NOW write code — with every rule enforced               │
  └─────────────────────────────────────────────────────────────┘
```

> **Nothing is optional.** Every resource in the wiring row MUST be loaded.
> A bundle = constitution + rules + templates + prompts + book refs. Load ALL of it.

---

## 🏭 Master Pipeline — From Idea to Production

For full projects (Path D), AOS guides the agent through 9 stages:

```
  ┌─────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
  │ Stage 0 │─►│ Stage 1  │─►│ Stage 2  │─►│ Stage 3  │
  │ INTAKE  │  │   SPECS  │  │  DESIGN  │  │ SECURITY │
  │ Classify│  │ Require- │  │ ADR +    │  │ STRIDE   │
  │ & scope │  │ ments    │  │ Arch     │  │ Threat   │
  └─────────┘  └──────────┘  └──────────┘  └──────────┘
       │                                        │
       │   ┌──────────┐  ┌──────────┐  ┌──────────┐
       │   │ Stage 6  │◄─│ Stage 5  │◄─│ Stage 4  │
       │   │   PRR    │  │ TESTING  │  │  BUILD   │
       │   │Scorecard │  │ Quality  │  │All Bundles│
       │   └──────────┘  └──────────┘  └──────────┘
       │        │
       │   ┌──────────┐  ┌──────────┐
       └──►│ Stage 7  │─►│ Stage 8  │
           │ DEPLOY   │  │POSTLAUNCH│
           │ Rollout  │  │ DORA +   │
           │& Rollback│  │ Monitor  │
           └──────────┘  └──────────┘
```

### Which Stages Run? Depends on Classification:

| Classification | Stages | What you get |
|---------------|--------|-------------|
| 🟢 Simple | 0 → 4 → 5 | Quick build + test |
| 🟡 Medium | 0 → 1 → 4 → 5 | Specs + build + test |
| 🔴 Sensitive | 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 | **Full pipeline** |

> Each stage has a **Resource Injection Matrix** (`books/00-master-index.md`) that tells the agent exactly which bundles, rules, and references to load.

---

## 🔌 Wiring Registry — The Connection Map

The wiring registry is the **single source of truth** that maps capabilities to resources:

```
  ┌────────────────────┐     ┌──────────────────┐     ┌──────────────┐
  │   CAPABILITY       │────►│   RULE FILE      │────►│ CONSTITUTION │
  │   (what you're     │     │   (02-rules/)    │     │ (from books) │
  │    working on)     │     └──────────────────┘     └──────────────┘
  └────────────────────┘              │                       │
                                      ▼                       ▼
                              ┌──────────────────┐    ┌──────────────┐
                              │  REF CONTRACTS   │    │ BOOK ANCHORS │
                              │  (grep catalog)  │    │ (grep books) │
                              └──────────────────┘    └──────────────┘
```

| When you're doing... | Load rule | Load constitution | Grep |
|---------------------|-----------|------------------|------|
| Architecture / DDD | architecture-and-design.md | arch + ddd | REF-ARCH-* |
| Database / queries | database-performance.md | perf | REF-DB-* |
| Security / auth | security-checklist.md | security | REF-SEC-* |
| Testing / quality | testing-and-quality.md | security + perf (audit) | REF-TEST-* |
| API / network | network-and-api.md | integration | REF-NET-* |
| Resilience | testing-and-quality.md §3 | resilience | REF-RES-* |
| Production readiness | production-readiness.md | resilience | REF-OPS-* |

---

## 🔐 Specialized Workflows

### 📱 Mobile QA (5 Steps)
```
  Step 1          Step 2         Step 3          Step 7
  ┌──────────┐   ┌──────────┐  ┌──────────┐   ┌──────────┐
  │Environment│──►│  Build   │─►│ Scenario │──►│ Evidence │
  │ Discovery │   │ Verify   │  │Execution │   │  Report  │
  └──────────┘   └──────────┘  └──────────┘   └──────────┘
  Detect device    Build OK?    Run test       Screenshot +
  & platform       Sign OK?     scenarios      log evidence
```

### 🔒 Security Gate (7 Steps)
```
  Step 1         Step 2        Step 3       Step 4
  ┌─────────┐   ┌─────────┐  ┌─────────┐  ┌─────────┐
  │ Threat  │──►│  Deps   │─►│ Secret  │─►│ Access  │
  │ Model   │   │  Check  │  │  Scan   │  │ Review  │
  └─────────┘   └─────────┘  └─────────┘  └─────────┘
       Step 5        Step 6        Step 7
  ┌─────────┐   ┌─────────┐  ┌─────────┐
  │  Code   │──►│  Test   │─►│  Gate   │
  │ Review  │   │ Verify  │  │ Report  │
  └─────────┘   └─────────┘  └─────────┘
```

### Other Workflows
| Workflow | File | Purpose |
|----------|------|---------|
| 🆕 Init Project | `init-project.md` | Initialize AOS in a new project |
| 🔧 Backend Module | `create-backend-module.md` | Create a new backend service |
| 🎨 Frontend Module | `create-frontend-module.md` | Create a new UI component |
| 🐛 Debug Errors | `debug-common-errors.md` | Systematic error resolution |
| 📝 Requirements | `requirements-analysis.md` | EARS/Given-When-Then specs |
| 🎯 UX Improvement | `improve-user-experience.md` | UI/UX enhancement |
| 🚀 Production Ready | `production-readiness.md` | 10-dimension PRR scorecard |
| 🧪 QA Strategy | `qa-strategy.md` | Test strategy framework |
| 📚 Knowledge Bootstrap | `knowledge-bootstrapping.md` | Load knowledge bundles into a new project |
| ▶️ Start Session | `start-session.md` | Session boot checklist |
| ⏹️ End Session | `end-session.md` | Save memory + handoff summary |

---

## 🔄 How It Works — Session Lifecycle

```
┌──────────────────────────────────────────────────────────────┐
│                     SESSION LIFECYCLE                         │
│                                                              │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐ │
│  │  🟢 BOOT │──►│ 🎯 TASK  │──►│ 🔌 WIRE  │──►│ ⚙️ WORK  │ │
│  └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘ │
│       │              │              │               │        │
│  Read boot      Classify it    Load the right   Write code   │
│  manifest +     🟢 🟡 or 🔴   Knowledge Bundle  with rules  │
│  memory files                  from wiring                   │
│                                registry                      │
│                                                              │
│  ┌──────────┐   ┌──────────┐                                │
│  │ 💾 SAVE  │◄──│ ✅ CHECK │                                │
│  └────┬─────┘   └────┬─────┘                                │
│       │              │                                       │
│  Update memory  Run governance                               │
│  for next       (11 checks)                                  │
│  session                                                     │
└──────────────────────────────────────────────────────────────┘
```

### 🏷️ Task Classification

| Color | Type | What happens |
|-------|------|--------------|
| 🟢 | **Simple** | Cosmetic edit → just do it |
| 🟡 | **Medium** | Multi-file logic → spec + plan + approval first |
| 🔴 | **Sensitive** | Security/architecture → ADR + full pipeline |

> ⬆️ **Escalation only** — never downgrade 🟡→🟢 during execution

### 🔀 Task Routing (Path A / B / C / D)

After classification, the task follows one of four paths:

```
  ┌──────────────────────────────────────────────────────────┐
  │                  TASK ROUTING                             │
  │                                                          │
  │  Path A ─ New feature (🟡/🔴)                           │
  │           SDD: Draft → Clarify → Approved → Code         │
  │           + Load Knowledge Bundle from wiring-registry    │
  │                                                          │
  │  Path B ─ Matches a workflow                              │
  │           Read the matching workflow from 03-workflows/   │
  │           Follow its steps exactly                        │
  │                                                          │
  │  Path C ─ Simple edit (🟢)                               │
  │           Do it directly → summarize                      │
  │                                                          │
  │  Path D ─ Full project lifecycle (🔴)                    │
  │           master-pipeline: 9 stages (Intake → Post-Launch)│
  │           🟢 stages 0,4,5 │ 🟡 stages 0,1,4,5           │
  │           🔴 ALL stages 0–8                               │
  └──────────────────────────────────────────────────────────┘
```

### 🧠 Memory System

```
  SESSION 1                SESSION 2                SESSION 3
  ┌────────┐              ┌────────┐              ┌────────┐
  │ Work.. │──── Save ───►│ Resume │──── Save ───►│ Resume │
  └────────┘   memory     └────────┘   memory     └────────┘

  4 files that persist across sessions:
  📍 project-context.md  — where we stopped
  📋 active-tasks.md     — pending work
  ⚠️ learned-mistakes.md — don't repeat (max 20, escalate at 3)
  📐 decisions.md        — architecture decisions (ADRs)
```

---

## ✅ Governance — Automated Quality Enforcement

```bash
python .agent/governance/runner.py          # human-readable
python .agent/governance/runner.py --json   # machine-readable
python .agent/governance/test_mutations.py  # prove checks work
```

### The 11 Checks

```
┌──────────────────────────────────────────────────────────┐
│                   GOVERNANCE DASHBOARD                    │
├──────┬───────────────────────────────────┬───────────────┤
│ Test │ What it checks                    │ Status        │
├──────┼───────────────────────────────────┼───────────────┤
│ T01  │ Task state matches state machine  │ ✅ PASS       │
│ T02  │ Acceptance criteria for 🟡/🔴     │ ✅ PASS       │
│ T03  │ ADR format (Context+Decision+Con) │ ✅ PASS       │
│ T04  │ Mistakes under cap (≤20)          │ ✅ PASS       │
│ T05  │ Memory files exist & non-empty    │ ✅ PASS       │
│ T06  │ Rules linked from workflow        │ ✅ PASS       │
│ T07  │ REF citations match catalog       │ ✅ PASS       │
│ T08  │ No stale/dead references          │ ✅ PASS       │
│ T09  │ No illegal state jumps            │ ✅ PASS       │
│ T10  │ ADRs complete & match contract    │ ✅ PASS       │
│ T11  │ Boot context within budget        │ ✅ PASS       │
├──────┴───────────────────────────────────┴───────────────┤
│ 5 Statuses: PASS · FAIL · SKIP_EXPECTED · SKIP_UNSUP · ERROR │
│ SKIP is never PASS. FAIL blocks delivery.                │
└──────────────────────────────────────────────────────────┘
```

### Mutation Tests (Anti-Rubber-Stamp)
Every check is proven to actually FAIL when a violation is introduced:
```
✅ T04-EXCEED-CAP:      Detects >20 mistakes
✅ T05-MISSING-FILE:     Detects missing memory
✅ T10-INCOMPLETE-ADR:   Detects bad ADR format
✅ T10-NO-ADR-WITH-RULES: Detects missing ADR
✅ T03-BAD-ADR-FORMAT:   Detects incomplete ADR
✅ T11-BOOT-TOO-LARGE:   Detects boot overflow
```

---

## 📏 Context Budget

AOS minimizes context to keep the agent fast and focused:

```
  ┌──────────────────────────────────────────────┐
  │            CONTEXT BUDGET                     │
  │                                               │
  │  🟦🟦🟦░░░░░░░░░░░░░░░░░░░░  Boot (≤150)   │
  │  🟩🟩░░░░░░░░░░░░░░░░░░░░░░  🟢 +2K tokens │
  │  🟨🟨🟨🟨🟨░░░░░░░░░░░░░░░░  🟡 +6K tokens │
  │  🟥🟥🟥🟥🟥🟥🟥🟥░░░░░░░░░░  🔴 +10K tokens│
  │                                               │
  │  Key: load ONLY what the task needs            │
  │  Never dump the whole repo or full references  │
  └──────────────────────────────────────────────┘
```

---

## 🛡️ Core Principles

```
┌─────────────────────────────────────────────────┐
│              PRIORITY ORDER                      │
│         (when rules conflict)                    │
│                                                  │
│  1. 🔒 Security & data integrity                │
│  2. 🧠 Memory & context accuracy                │
│  3. ✅ Correctness & tests                      │
│  4. 🔄 Simplicity & reversibility               │
│  5. ⚡ Performance & cost                       │
│  6. 📏 Language/framework conventions            │
│                                                  │
│  Unlisted conflict → STOP and ask developer      │
└─────────────────────────────────────────────────┘
```

---

## 📐 Architecture Decisions (ADRs)

| ADR | Decision | Status |
|-----|----------|--------|
| ADR-001 | Vertical Slice Governance charter | ✅ Approved |
| ADR-003 | AOS v7.0 Wired Pipeline architecture | ✅ Approved |
| ADR-004 | Books anchor strategy (grep, don't modify) | ✅ Approved |
| ADR-005 | English operational, Arabic chat | ✅ Approved |
| ADR-006 | Vertical Slice → optional Technology Profile | ✅ Approved |
| ADR-007 | References → on-demand outside Boot | ✅ Approved |

---

## 🚫 Forbidden Actions

| ❌ Action | Why |
|-----------|-----|
| Write outside project | Safety boundary |
| Load 2+ rules simultaneously | Context overflow |
| Read references in full | Grep only — context budget |
| Skip task classification | Governance requirement |
| Code before spec (🟡/🔴) | Approval gate |
| Skip memory update (🟡/🔴) | Session continuity |
| Fabricate tool output | Evidence integrity |
| Downgrade classification | Escalation only |

---

## 📊 Current Metrics

| Metric | Value |
|--------|-------|
| AOS Version | v8.0-dev |
| Boot Context | 272 lines (goal: 150) |
| Governance Checks | 11/11 PASS ✅ |
| Mutation Tests | 6/6 detected ✅ |
| Architecture Decisions | 7 ADRs |
| Engineering Books | 16 distilled |
| Constitutions | 6 (79 rules) |
| Knowledge Bundles | 7 |
| Pipeline Stages | 9 |
| Rule Files | 6 |
| Workflows | 34 |
| REF Contracts | 34 |

---

## 🤝 Contributing

1. Fork the repo
2. Make changes in `.agent/`
3. Run: `python .agent/governance/runner.py`
4. Run: `python .agent/governance/test_mutations.py`
5. All green? Submit a PR!

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">
  <strong>AOS v8.0-dev</strong> · 16 books · 79 rules · 9 stages · 11 checks · 0 rubber-stamps<br>
  Built for agents, governed by humans 🤝
</p>
