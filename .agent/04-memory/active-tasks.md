# Active Tasks — AOS v8.0-dev

## T025 — Verified Provenance & Autonomous Execution 🔴
- **State:** Done
- **Branch:** `aos-v8-sprint2-autonomy`
- **Approval:** Navigator approved Sprint 2 continuation.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating → Done

### Acceptance Criteria
- ADR/pattern provenance must resolve to approved scoped registry entries.
- Hard-stop risks always require explicit human approval.
- Execution mode is explicit: AUTO_EXECUTE / HUMAN_APPROVED / HUMAN_REQUIRED.
- Task Contract rejects unknown risk/provenance fields.
- Evidence History archives are SHA-256 integrity-checked.
- CI evaluates Execution Gate and uploads verified evidence history.
- Mutations prove provenance/hash/schema protections fail correctly.
- No merge before final green CI.

### Progress
- [x] ADR-010 + approval registry.
- [x] Task Contract validator.
- [x] Approval Engine verifies provenance scope and returns execution mode.
- [x] Unified Execution Gate added.
- [x] Evidence History archive/hash verification added.
- [x] GOV-T23–T29 + mutations added.
- [x] Boot + CI routed through execution gate/history.
- [x] CI green: 30/30 governance + 19/19 mutations.
- [x] Evidence Bundle/History + artifact flow verified.
- [x] Final Validating-state CI passed.
- [x] Done-state CI passed; GOV-T09 verified full history.

### Evidence
Run `35438378213`: Done-state PASS + 19/19 + Evidence History.

### Next
Run final head CI, then squash-merge PR #4 only if green.
