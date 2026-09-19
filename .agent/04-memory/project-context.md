# Project Context — AOS v8.0-dev

- **Phase:** Sprint 2 — Merge-Safe Memory
- **Task:** T028 — Executing

## Architecture
- ADR-008: deterministic Context Broker.
- ADR-010: verified provenance + Execution Gate + Evidence History.
- ADR-011: risk/affected-area capability routing.
- ADR-012: durable Boot Memory excludes volatile VCS transport state.

## Current
Boot/end-session rules, GOV-T37, mutation coverage, README metrics, and T028 contract implement merge-safe durable memory.

## Next
Run full verification, fix any failures, then validate the memory lifecycle before completion.
