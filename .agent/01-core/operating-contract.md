# Operating Contract — Supplemental Policy (AOS v8.0-dev)

> **Runtime authority:** `01-core/boot-manifest.md`
> This file is a supplemental policy reference. It is not loaded at boot unless the active task needs it.
> ADR-006 and ADR-007 govern the v8 migration away from fixed full-stack assumptions and mandatory reference injection.

## 1. Conflict Resolution

When rules conflict, prefer:
1. Security and data integrity
2. Accurate project context and approved decisions
3. Correctness and executable evidence
4. Simplicity and reversibility
5. Performance and cost
6. Framework/language conventions

An unresolved conflict that materially changes architecture, security, data, or external contracts requires Navigator review.

## 2. Architecture Neutrality

AOS Core must not assume a project is a full-stack web application, Clean Architecture system, DDD system, microservice, or any other specific architecture.

Core rule:
> Verify every **affected** project area before declaring the task complete.

Project-specific layers and architectural conventions come from:
- the existing codebase,
- the Project Profile,
- an activated Technology Profile,
- approved ADRs.

A seven-layer full-stack coverage model is therefore optional guidance for projects that explicitly activate the full-stack-web profile; it is not a universal Core requirement.

## 3. Context & Knowledge

Knowledge is loaded on demand.

- Do not load reference files during Boot.
- Do not load a complete bundle by default.
- Use `wiring-registry.md` to discover resources for active capabilities.
- Load the smallest resource set needed to make or verify the current decision.
- Technology-specific rules belong in Technology Profiles.
- Heavy references remain grep/search-first.
- REF/CONST citations in production source are optional. Put compliance evidence in the task evidence/report unless a source comment genuinely helps maintainers.

Until Context Broker exists, the agent performs this selection manually and records what it used.

## 4. Task Process

- 🟢 Simple: execute with proportional verification.
- 🟡 Medium: specification/plan appropriate to the change, then verification.
- 🔴 Sensitive: explicit risk/architecture/security review and approval where required.

The canonical state machine and approval rules live in `boot-manifest.md`.

## 5. Evidence

Claims do not prove completion.

Use executable or inspectable evidence whenever available:
- build/test/lint exit status,
- CI checks,
- diffs,
- security scans,
- migration checks,
- file/line references,
- structured task evidence.

A model assertion alone is never equivalent to a passing check.

## 6. Memory & Learning

Project state, approved decisions, and learned mistakes remain durable across sessions.

When a developer correction reveals:
- an existing rule was ignored → fix execution/checking,
- project-specific knowledge → record it in project memory,
- a missing reusable rule → propose a rule/profile/governance improvement.

Repeated failures should become prevention: a rule, profile constraint, regression test, or governance check.

## 7. Proportionality

AOS must not create ceremony without risk reduction.

Use the lightest process that still protects:
- correctness,
- security,
- data integrity,
- architectural consistency,
- reversibility,
- user-visible behavior.

Do not require ADRs, threat models, full-stack coverage, or large reference bundles for changes that do not justify them.
