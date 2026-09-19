# Active Tasks — AOS v8.0-dev

## T025 — Verified Provenance & Autonomous Execution 🔴
- **State:** Validating
- **Branch:** `aos-v8-sprint2-autonomy`
- **Approval:** Navigator approved Sprint 2 continuation.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating

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
- [x] CI green: 30/30 governance + 18/18 mutations.
- [x] Evidence Bundle/History + artifact flow verified.
- [ ] Final Validating-state CI.
- [ ] Done-state CI for T09.

### Evidence
Run `35438279608`: full verification + Evidence History success.

### Next
Run Validating-state CI; close T025 only if green.
