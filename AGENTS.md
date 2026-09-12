# AGENTS.md — Agent Entry Point (AOS v8.0-dev)

> Read `.agent/01-core/boot-manifest.md` and follow it exactly.
> It is the single boot file. All other resources load on demand.

1. Boot: `.agent/01-core/boot-manifest.md` — contract, classification, budget, governance.
2. Memory: `.agent/04-memory/` (project-context, active-tasks, learned-mistakes, decisions).
3. Classify every task (🟢/🟡/🔴); 🟡/🔴 need approved spec + plan before code.
4. Rules: load ONE from `02-rules/` per task. References: grep `05-references/` only.
5. Run governance: `python .agent/governance/runner.py` before Done. Never write outside the local project.
