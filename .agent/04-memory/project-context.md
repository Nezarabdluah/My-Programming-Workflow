# Project Context — AOS v8.0-dev

## Current State
- **Phase:** Sprint 2 — Context Broker Foundation
- **Task:** T023 — Executing
- **Branch:** `aos-v8-sprint2-context`
- **Main:** v8 convergence merged successfully
- **Merged PR:** #1 via squash commit `5e6de0409814d1ae3234a60b3b44876aec889115`

## Active Architecture
- `boot-manifest.md` is canonical runtime authority.
- ADR-006: fixed seven-layer web model is profile-scoped.
- ADR-007: references/resources load selectively.
- ADR-008: deterministic Context Broker resolves explicit task capabilities against Project/Technology Profiles and executable context map.

## Sprint 2 Work
- Added Context Broker executable and machine-readable context map.
- Added project + technology profiles.
- Added current task contract.
- Added governance tests for minimal resource selection and profile gating.
- Boot/init/index now route non-trivial context expansion through the broker.

## Next
Add mutation tests, run GitHub Actions in a Draft PR, then review before expanding Sprint 2 into Evidence Bundle/Approval Policy.
