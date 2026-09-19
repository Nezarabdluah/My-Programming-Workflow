# Project Context — AOS v8.0-dev

- **Phase:** v8 Release Readiness
- **Task:** T029 — Executing

## Architecture
ADR-008 Context Broker · ADR-010 Execution Gate/Evidence History · ADR-011 risk routing · ADR-012 merge-safe memory · ADR-013 sanitized two-phase installation.

## Current
Release entrypoints and consumer onboarding are being synchronized to the executable v8 runtime. Sanitized installation separates reusable runtime from target-specific state.

## Next
Run full release-readiness verification, then address Boot budget and any remaining RC blockers.
