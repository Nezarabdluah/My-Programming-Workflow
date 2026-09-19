# Project Context — AOS v8.0-dev

## Current State
- **Phase:** v8 Convergence Sprint
- **Task:** T022 — Validating
- **Branch:** `aos-v8-convergence`
- **Main:** unchanged
- **PR:** #1 draft, unmerged

## Applied Decisions
- ADR-006: fixed seven-layer vertical-slice governance removed from Core.
- ADR-007: context/resources load selectively; full bundles and source REF/CONST comments are not mandatory.

## Current Result
- Core, workflows, rules, INDEX, memory, governance, and CI aligned to v8.
- Governance previously reached 11/11 PASS and mutations 8/8.
- Latest validation exposed only boot-budget regression from duplicated memory evidence.

## Next
Compact boot memory below 200 lines, rerun GitHub Actions, and mark T022 Done only if fully green.
