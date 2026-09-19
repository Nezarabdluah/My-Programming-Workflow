# Project Context — AOS v8.0-dev

- **Phase:** Sprint 2 Context Broker Foundation
- **Task:** T023 — Done
- **Branch:** `aos-v8-sprint2-context`
- **Main:** convergence merged via PR #1

## Architecture
- Boot manifest is canonical.
- ADR-006: web seven-layer model is profile-scoped.
- ADR-007: resources load selectively.
- ADR-008: Task Contract + Project/Technology Profiles + executable Context Map drive deterministic broker resolution.

## Current
Broker, profiles, T12–T16, mutations, and PR #2 are implemented. Run `35437378236` passed full verification after memory compaction.

## Next
Run Done-state CI, then prepare PR #2 for squash merge if green.
