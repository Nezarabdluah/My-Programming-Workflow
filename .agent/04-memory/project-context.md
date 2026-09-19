# Project Context — AOS v8.0-dev

- **Phase:** Sprint 2 Context Broker Foundation
- **Task:** T023 — Validating
- **Branch:** `aos-v8-sprint2-context`
- **Main:** convergence merged via PR #1

## Architecture
- Boot manifest is canonical.
- ADR-006: web seven-layer model is profile-scoped.
- ADR-007: resources load selectively.
- ADR-008: Task Contract + Project/Technology Profiles + executable Context Map drive deterministic broker resolution.

## Current
Broker, profiles, T12–T16, mutations, and PR #2 are implemented. Latest validation failed only GOV-T11 because boot memory grew to 207 lines.

## Next
Keep boot below 200, rerun CI, then close T023 only if green.
