<p align="center">
  <h1 align="center">🤖 AOS — Agent Operating System</h1>
  <p align="center">
    <strong>v8.0-dev</strong> · Governed execution for AI coding agents<br>
    Language-Agnostic · Framework-Agnostic · Editor-Agnostic
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-8.0--dev-blue" alt="version">
  <img src="https://img.shields.io/badge/governance-37%20checks-brightgreen" alt="governance">
  <img src="https://img.shields.io/badge/mutations-24%2F24%20detected-brightgreen" alt="mutations">
  <img src="https://img.shields.io/badge/pipeline-9%20stages-red" alt="pipeline">
  <img src="https://img.shields.io/badge/books-16%20distilled-purple" alt="books">
</p>

---

## Start in 30 Seconds

Copy `.agent` into your project, then tell your AI tool:

```text
Read .agent/01-core/boot-manifest.md and follow it exactly.
It is the canonical runtime contract.

For non-trivial work:
1. Update .agent/task-contracts/current.json.
2. Run: python .agent/01-core/execution_gate.py
3. If HUMAN_REQUIRED, stop for approval.
4. If HUMAN_APPROVED or AUTO_EXECUTE, use only broker-selected context.
5. Before Done, run named checks through .agent/01-core/evidence_recorder.py.
Never fabricate evidence.
```

Automatic entry adapters are also included for tools that support repository instructions:
`AGENTS.md`, `CLAUDE.md`, `.cursorrules`, and GitHub Copilot instructions.

---

## What AOS Is

AOS is a small operating system around an AI coding agent. It makes task execution:

- **stateful** — durable memory and SDD state survive sessions,
- **risk-aware** — classification, explicit risk flags, affected areas,
- **approval-aware** — deterministic approval provenance and hard-stop policy,
- **context-efficient** — Context Broker selects only relevant resources,
- **project-aware** — Project Profile + Technology Profiles,
- **evidence-driven** — PASS/FAIL comes from executed checks,
- **self-verifying** — governance + mutation tests prove checks can fail.

The runtime is intentionally deterministic where determinism matters.

---

## Runtime Flow

```text
Task
  ↓
Task Contract
  - classification
  - capabilities
  - affected areas
  - risk flags
  - approval provenance
  - named verification checks
  ↓
Execution Gate
  ├─ HUMAN_REQUIRED → stop
  ├─ HUMAN_APPROVED → proceed
  └─ AUTO_EXECUTE → proceed
  ↓
Context Broker
  - explicit capabilities
  - risk-derived capabilities
  - affected-area-derived capabilities
  - Technology Profile gates
  ↓
Minimal selected resources
  ↓
Implementation
  ↓
Evidence Recorder
  - executes named Project Profile commands
  - derives PASS/FAIL from exit code
  ↓
Evidence Bundle + Evidence History
  ↓
Governance + Mutation Tests
```

---

## Canonical Core

| File | Purpose |
|---|---|
| `.agent/01-core/boot-manifest.md` | Canonical runtime contract |
| `.agent/01-core/task_contract.py` | Structured Task Contract validation |
| `.agent/01-core/execution_gate.py` | Unified pre-execution decision |
| `.agent/01-core/approval_engine.py` | Approval provenance and hard-stop policy |
| `.agent/01-core/approval-policy.json` | Executable approval policy |
| `.agent/01-core/approval-registry.json` | Verified ADR/pattern approval sources |
| `.agent/01-core/context_broker.py` | Deterministic context resolver |
| `.agent/01-core/context-map.json` | Executable capability → resource map |
| `.agent/01-core/evidence_recorder.py` | Executable Evidence Bundle/History recorder |
| `.agent/01-core/wiring-registry.md` | Human-readable capability/resource catalog |

`context-map.json` is the executable resource source of truth. The Markdown wiring registry is documentation for humans and agents.

---

## Task Contract

The current non-trivial task lives in:

`.agent/task-contracts/current.json`

It records:

```json
{
  "task_id": "T000",
  "classification": "medium",
  "capabilities": ["testing"],
  "affected_areas": ["src/feature"],
  "risk": {
    "security_boundary": false,
    "data_migration": false
  },
  "approval": {
    "status": "approved",
    "provenance": "approved_pattern",
    "reference": "pattern-id"
  },
  "verification": ["build", "test"]
}
```

Unknown risks, invalid provenance, missing verification names, and invalid affected areas are rejected by executable validation.

---

## Approval & Autonomous Execution

The Execution Gate returns one of three modes:

| Mode | Meaning |
|---|---|
| `AUTO_EXECUTE` | Policy/verified ADR/pattern covers the task |
| `HUMAN_APPROVED` | Explicit Navigator approval covers the task |
| `HUMAN_REQUIRED` | Stop before implementation |

Hard-stop risks include destructive/irreversible changes, new architecture, security boundaries, production changes, breaking external contracts, and data migrations.

A text string such as `"approved_adr"` is not trusted by itself. ADR/pattern provenance must resolve through `approval-registry.json` to durable source evidence and valid scope.

---

## Context Broker

The broker combines three sources:

1. **Explicit capabilities** from the Task Contract.
2. **Risk-derived capabilities** from `context-map.json`.
3. **Affected-area-derived capabilities** from the Project Profile.

Examples:

```text
security_boundary=true
  → Security + Testing

data_migration=true
  → Database + Testing

production_change=true
  → Production Readiness + Deployment + Testing

.github/workflows/**
  → Deployment + Testing   (project-specific rule)
```

Capabilities are de-duplicated while preserving provenance such as:
`explicit`, `risk:security_boundary`, or `area:.github/workflows`.

Technology-specific resources load only when their Technology Profile is active.

---

## Project & Technology Profiles

`.agent/profiles/project.json` defines the current project:

- project type,
- languages,
- active Technology Profiles,
- architecture source of truth,
- named verification commands,
- affected-area → capability rules.

Technology Profiles live under:

`.agent/profiles/technology/`

The full-stack seven-layer model is optional profile guidance, not a Core assumption.

---

## Evidence Bundle & History

Verification commands are named in the Project Profile and executed through:

```bash
python .agent/01-core/evidence_recorder.py --check governance_compile
python .agent/01-core/evidence_recorder.py --check governance_verify
```

Rules:

- commands must be declared in the Project Profile,
- execution is shell-free,
- PASS/FAIL is derived from the process exit code,
- current evidence is written to `.agent/evidence/current.json`,
- completed evidence can be archived with SHA-256 integrity,
- tampering with archived evidence is detected,
- CI can upload Evidence History as an artifact.

A prose claim such as “tests passed” is not executable evidence.

---

## Knowledge System

AOS still includes:

- 16 distilled engineering books,
- 6 constitutions,
- REF/OPS/QA reference catalogs,
- specialized engineering rules,
- prompts and templates.

But knowledge loading is now **on demand**.

```text
Task Contract
  ↓
Context Broker
  ↓
selected rule/reference/workflow entries only
```

Heavy references are search/grep-first. Complete bundles are not loaded by default.

---

## Master Pipeline

For full lifecycle work AOS provides nine stages:

```text
0 Intake
1 Requirements
2 Architecture
3 Threat Model
4 Implementation
5 Testing
6 Production Readiness
7 Deployment
8 Post-Launch
```

The required depth depends on task risk/classification. Stage resources are selected contextually; the pipeline does not force every project into a fixed full-stack architecture.

---

## Memory & SDD

Canonical states for non-trivial work:

```text
Draft → Clarify → Approved → Planning → Ready → Executing → Validating → Done
```

Durable memory:

| File | Purpose |
|---|---|
| `project-context.md` | Current project/session state |
| `active-tasks.md` | Current task + SDD state |
| `learned-mistakes.md` | Active learned mistakes |
| `decisions.md` | ADR log |
| `project-knowledge.md` | Durable discovered project patterns |
| `codebase-map.md` | Discovered project structure |

Completed historical task detail should be archived instead of bloating Boot Context.

Durable Boot Memory is **merge-safe**: current branch, PR status, mergeability, and queued/in-progress CI state are queried live from version control instead of being persisted. Immutable evidence such as completed CI run IDs, commit SHAs, ADR IDs, and completed task states may be retained.

---

## Governance

Run full verification with:

```bash
python .agent/governance/verify.py
```

Current governance covers T01–T37, including:

- task state and acceptance criteria,
- ADR/memory integrity,
- boot context budget,
- Context Broker minimality/profile gating,
- Project Profile integrity,
- Approval Engine behavior,
- Evidence Bundle semantics,
- approval provenance/source verification,
- Execution Gate behavior,
- Evidence History tamper detection,
- risk/affected-area capability derivation,
- public README/runtime contract synchronization,
- merge-safe durable Boot Memory.

Mutation tests deliberately corrupt the system and verify governance catches the violation.

Current verified baseline from Sprint 2:

- **37 governance checks** (Done state may include expected skips),
- **24/24 mutation violations detected**,
- **Boot Context 194/200 lines** on the final risk-routing validation,
- Evidence Bundle and Evidence History verified in CI.

---

## Project Structure

```text
.agent/
├── 01-core/
│   ├── boot-manifest.md
│   ├── task_contract.py
│   ├── execution_gate.py
│   ├── approval_engine.py
│   ├── approval-policy.json
│   ├── approval-registry.json
│   ├── context_broker.py
│   ├── context-map.json
│   └── evidence_recorder.py
├── 02-rules/
├── 03-workflows/
│   └── master-pipeline/
├── 04-memory/
├── 05-references/
├── 06-templates/
├── profiles/
│   ├── project.json
│   └── technology/
├── task-contracts/
│   └── current.json
├── evidence/
│   ├── README.md
│   └── history/
└── governance/
    ├── runner.py
    ├── verify.py
    ├── test_state.py
    ├── test_rules.py
    ├── test_memory.py
    ├── test_context.py
    ├── test_execution.py
    └── test_mutations.py
```

---

## Context Budget

Current convergence ceiling:

- Boot Context: **≤200 lines**
- Final v8 target: **≤150 lines**

Task expansion budgets are proportional to task complexity. Context budget is a guardrail, not a reason to omit required security/correctness evidence.

---

## Core Principles

1. Security and data integrity.
2. Accurate context and approved decisions.
3. Correctness and executable evidence.
4. Simplicity and reversibility.
5. Performance and cost.
6. Stack conventions.

Additional rules:

- evidence over claims,
- no hidden classification downgrade,
- no direct AOS self-development writes to `main`,
- no unconditional full-reference loading,
- no fixed full-stack assumptions without profile activation,
- no unverified ADR/pattern string as approval provenance.

---

## Architecture Decisions

Current v8 direction is defined by:

- ADR-006 — Vertical Slice → optional Technology Profile.
- ADR-007 — references/resources → on-demand.
- ADR-008 — deterministic Context Broker.
- ADR-009 — Approval Engine + executable Evidence Bundle.
- ADR-010 — verified provenance + autonomous Execution Gate + Evidence History.
- ADR-011 — risk/affected-area capability routing.

Older ADRs remain in the log as historical decisions and may be superseded by later ADRs.

---

## Contributing

Before submitting a change:

```bash
python .agent/01-core/execution_gate.py
python .agent/01-core/evidence_recorder.py --check governance_compile
python .agent/01-core/evidence_recorder.py --check governance_verify
```

Use a branch/PR for AOS self-development. Merge only after final CI and Done-state verification are green.

---

## License

MIT License — see [LICENSE](LICENSE).

---

<p align="center">
  <strong>AOS v8.0-dev</strong> · Deterministic context · Verified approvals · Executable evidence · Mutation-tested governance
</p>
