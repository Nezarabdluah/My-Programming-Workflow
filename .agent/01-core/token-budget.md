---
id: core-token-budget
description: Supplemental context-budget and selective-loading guidance for AOS v8.
alwaysApply: false
globs: []
requires: [REF-AI-CONTRACT]
---

# Token Budget — AOS v8.0-dev

> Canonical boot limits live in `01-core/boot-manifest.md` and are enforced by GOV-T11.

## Canonical Boot

Boot only:
- `01-core/boot-manifest.md`
- `04-memory/project-context.md`
- `04-memory/learned-mistakes.md`
- `04-memory/active-tasks.md`
- `VERSION`

During v8 convergence the canonical boot ceiling is 200 lines; final target is 150.

Do not preload:
- INDEX,
- operating-contract,
- workflows,
- rules,
- profiles,
- references.

## Task Expansion

Load only what the current task needs:
- one directly relevant rule file at a time,
- one workflow/stage at a time,
- project memory on demand,
- heavy references by search/grep only.

Suggested expansion budgets from the boot contract:
- 🟢 up to ~2K tokens when needed,
- 🟡 up to ~6K,
- 🔴 up to ~10K when justified.

These are budgets, not targets.

## Efficiency Rules
1. Search before broad reading.
2. Prefer relevant line ranges/functions over whole-file reads.
3. Do not dump the repository into context.
4. Do not load a complete knowledge bundle by default.
5. Summarize durable progress into memory before a tool/session handoff.
6. When context pressure becomes material, preserve state and reduce loaded context rather than continuing blindly.
7. Never sacrifice correctness/security merely to hit a token target.
