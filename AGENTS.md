# AGENTS.md — Agent Entry Point (AOS v7.0)

> Thin bridge. The single source of truth lives in `.agent/AGENTS.md` — read it and follow it exactly
> (session boot, SDD workflow, wiring registry, handoff protocol, forbidden list).

1. Index: `.agent/INDEX.md`. Contract: `.agent/01-core/operating-contract.md`. Session: `.agent/01-core/session-prompt.md`.
2. Memory: `.agent/04-memory/` (project-context, active-tasks, learned-mistakes, decisions).
3. Budget ≤ 400 lines/session · one `02-rules/` file at a time · grep-only `05-references/`.
4. Classify every task (🟢 Simple / 🟡 Medium / 🔴 Sensitive); 🟡/🔴 need approved spec + plan before code.
5. Cite `// [REF-XX-N]` and `// [CONST-XX-N]`; produce a Resource Utilization Summary before Done.
6. Governance: `python .agent/governance/runner.py` before Done. Never write outside the local project.
