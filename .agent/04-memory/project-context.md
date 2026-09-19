# Project Context — AOS v8.0-dev

## Current State
- **Phase:** v8 Convergence Sprint
- **Active task:** T022
- **Branch:** `aos-v8-convergence`
- **Main branch:** unchanged
- **Verification:** implementation in progress; full governance/mutation regression not yet executed

## Convergence Decisions Being Applied
- ADR-006: fixed seven-layer vertical-slice governance moves out of Core into optional project/profile guidance.
- ADR-007: references/resources load on demand; complete bundles and production REF/CONST comments are not mandatory.

## Completed in This Sprint
- Canonicalized `boot-manifest.md` as runtime entry.
- Demoted v7 session/start compatibility paths.
- Aligned Core operating contract and vertical-slice guidance with ADR-006/007.
- Converted wiring/master resource mapping to selective context discovery.
- Updated Master Pipeline stages, QA, UX, init, and closeout semantics.

## Next
- Harden governance truthfulness (T09/T10/boot budget).
- Remove remaining v7 authority drift.
- Add self-development mode.
- Run full regression evidence before proposing merge.
