# Project Context — AOS v8.0-dev

## Current State
- **Phase:** v8 Convergence Sprint
- **Task:** T022 — Done
- **Branch:** `aos-v8-convergence`
- **Main:** unchanged
- **PR:** #1 draft, unmerged

## Applied Decisions
- ADR-006: fixed seven-layer vertical-slice governance removed from Core.
- ADR-007: context/resources load selectively; full bundles and source REF/CONST comments are not mandatory.

## Current Result
- Core, workflows, rules, INDEX, memory, governance, and CI aligned to v8.
- GitHub Actions run `35436797418` passed full verification after memory compaction.
- T022 is closed pending one final Done-state CI check so GOV-T09 validates the full state history.

## Next
If Done-state CI remains green, prepare the draft PR for merge review/squash strategy.
