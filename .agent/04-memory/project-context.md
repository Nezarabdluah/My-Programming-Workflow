# Project Context — AOS v8.0-dev

- **Phase:** Sprint 2 — Merge-Safe Memory
- **Task:** T028 — Done

## Architecture
ADR-008 Context Broker · ADR-010 Execution Gate/Evidence History · ADR-011 risk routing · ADR-012 merge-safe durable memory.

## Current
Merge-safe memory is implemented and validated. Completed verification `35439819747` passed 37 governance checks and 24/24 mutations.

## Next
Use durable memory only for stable engineering facts and immutable completed evidence; query VCS transport state live.
