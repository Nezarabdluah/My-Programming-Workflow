# 📝 Project Context (AOS v7.0)

> **Session 4** — 2026-09-07 | Agent: Muse Spark (OpenCode)

## Current State
- **AOS version**: v7.0.0 "Wired Pipeline"
- **Phase**: PUBLISHED — pushed to https://github.com/Nezarabdluah/My-Programming-Workflow (main: 652e89c + 540eec5)
- **All operational files**: English (per ADR-005)
- **Goal achieved**: Every path (A/B/C/D) forces mandatory resource injection

## What Just Happened (Session 3)
T013 integration completed — the "islands problem" is solved:
1. Created 6 constitution files (79 actionable rules extracted from 16 engineering books)
2. Created Resource Injection Matrix (00-master-index.md) mapping ALL resources to ALL stages
3. Updated wiring-registry: "Lazy Resolution" → "Mandatory Injection" with constitution column
4. Updated pipeline coordinator: Mandatory Resource Injection Protocol with YAML citation template
5. Updated session-prompt: 5-step loading (Registry → Constitutions → Rules → Prompts → Citations)
6. Updated INDEX.md with new entries
7. All 7 verification checks passed green

## Architecture Summary (post-T013)
```
L0 (AGENTS.md) — Constitution
L5 (governance/) — Deterministic enforcement
L1 (04-memory/) — Cumulative context
L2 (03-workflows/ + master-pipeline/) — Pipeline stages 0-8
    ↓ Each stage loads from:
L3 (02-rules/) — 6 specialized rule files
L4 (05-references/) — Constitutions + REF catalog + DevOps + QA + Books + Prompts
    + 06-templates/ — universal stack-agnostic templates (entity-patterns, coding-standards, pre-commit, CI gate, PR template)
```

## Critical Alerts
- ⚠️ Books file (engineering-books-16-distilled.txt): 1412 lines on disk (was 2988). Constitutions extracted as mitigation. Full recovery requires user to re-provide content.
- ⚠️ NEVER delegate destructive writes to subagents (learned-mistake #01)

## Next Steps
1. T012: User provides remaining books content → translate to English
2. Budget verification: count permanent load after all changes
3. Dry-run: test the pipeline on a sample project to verify resource injection works
