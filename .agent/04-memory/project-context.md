# Project Context — AOS v8.0-dev
## Current
- **Phase:** Sprint 2 — Context Broker Foundation
- **Task:** T023 — Validating
- **Branch:** `aos-v8-sprint2-context`
- **Main:** convergence merged via PR #1 / `5e6de0409814d1ae3234a60b3b44876aec889115`

## Architecture
- `boot-manifest.md` is canonical runtime authority.
- ADR-006: fixed seven-layer web model is profile-scoped.
- ADR-007: resources load selectively.
- ADR-008: Task Contract + Project/Technology Profiles + executable Context Map drive deterministic Context Broker resolution.

## Sprint 2
- Broker, context map, project/technology profiles, and current task contract added.
- GOV-T12/T13/T14 cover minimality, profile gating, and current contract resolution.
- Boot/init/INDEX/wiring now route non-trivial context through the broker.

## Validation
- Context Broker + profiles + task contract + T12–T16 are green.
- Latest GitHub Actions: `35437322891` success.

## Next
Run final CI in Validating state; then close T023 and prepare PR #2 for merge review.
