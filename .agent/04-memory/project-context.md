# Project Context — AOS v8.0-dev

## Current State
- **Phase:** v8 Convergence Sprint
- **Active task:** T022
- **Branch:** `aos-v8-convergence`
- **Main branch:** unchanged
- **Verification:** Validating; GitHub Actions full verification is green on the latest pre-state-update head

## Convergence Decisions Being Applied
- ADR-006: fixed seven-layer vertical-slice governance moves out of Core into optional project/profile guidance.
- ADR-007: references/resources load on demand; complete bundles and production REF/CONST comments are not mandatory.

## Completed in This Sprint
- Canonicalized `boot-manifest.md` as runtime entry.
- Demoted v7 session/start compatibility paths.
- Aligned Core operating contract and vertical-slice guidance with ADR-006/007.
- Converted wiring/master resource mapping to selective context discovery.
- Updated Master Pipeline stages, QA, UX, init, and closeout semantics.

## Validation Status
- Governance: 11/11 PASS
- Mutation verification: 8/8 detected, 0 missed
- GitHub Actions run `35436735290`: success
- Draft PR #1 remains unmerged

## Next
- Re-run full verification after the current memory transition to `Validating`.
- If green and no diff blockers remain, mark T022 Done and prepare merge strategy.
