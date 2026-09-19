# Project Context — AOS v8.0-dev

- **Phase:** Sprint 2 — Evidence & Approval
- **Task:** T024 — Validating
- **Branch:** `aos-v8-sprint2-evidence-approval`
- **Main:** Context Broker foundation merged via PR #2

## Architecture
- ADR-008: deterministic Context Broker + profiles.
- ADR-009: deterministic Approval Engine + executable Evidence Bundle.

## Current
Approval/evidence implementation is complete and shell-free. Run `35437681233` passed 22/22 governance, 14/14 mutations, and Evidence Bundle validation.

## Next
Run Validating-state CI; if green, mark Done and prepare PR #3 for squash merge.
