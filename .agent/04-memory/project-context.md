# Project Context — AOS v8.0-dev

- **Phase:** Sprint 2 — Merge-Safe Memory
- **Task:** T028 — Validating

## Architecture
- ADR-008: deterministic Context Broker.
- ADR-010: verified provenance + Execution Gate + Evidence History.
- ADR-011: risk/affected-area capability routing.
- ADR-012: durable Boot Memory excludes volatile VCS transport state.

## Current
Merge-safe memory rules, GOV-T37, mutation coverage, and public documentation are implemented. Completed verification `35439761791` passed 37 governance checks and 24/24 mutations.

## Next
Validate completion semantics and final evidence before closing T028.
