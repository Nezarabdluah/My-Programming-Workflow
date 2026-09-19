# Project Context — AOS v8.0-dev

- **Phase:** Sprint 2 — Stabilization
- **Task:** T027 — Executing
- **Branch:** `aos-v8-sprint2-stabilization`
- **Main:** risk-aware routing merged via PR #5 / `b21db66de4dd2c1ee28ca4ae38737734a2d3b52e`

## Architecture
- ADR-008: deterministic Context Broker.
- ADR-010: verified provenance + Execution Gate + Evidence History.
- ADR-011: risk/affected-area capability derivation.

## Current
Public README and metadata were stale relative to the runtime. T027 synchronizes the public contract and adds governance against future drift.

## Next
Run Execution Gate + CI, then validate and merge only if green.
