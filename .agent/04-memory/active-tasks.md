# Active Tasks — AOS v8.0-dev

## T023 — Sprint 2 Context Broker Foundation 🔴
- **State:** Done
- **Branch:** `aos-v8-sprint2-context`
- **Approval:** Navigator approved continuing Sprint 2.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating → Done

### Acceptance Criteria
- Deterministic Task Contract → Context Broker → Context Map resolution.
- Project/Technology Profiles drive profile-gated context.
- Unknown capabilities/resource drift fail explicitly.
- Governance proves minimality, profile gates, map integrity, and profile integrity.
- No merge to `main` before final green CI.

### Progress
- [x] ADR-008, broker, context map, profiles, task contract.
- [x] Boot/init/INDEX/wiring integrated.
- [x] GOV-T12–T16 added.
- [x] Broker/profile/map mutations added.
- [x] PR #2 CI reached 15/15 before validation-memory update.
- [x] Final Validating-state CI passed.
- [x] T023 closed; awaiting Done-state CI for T09.

### Last Evidence
Run `35437378236`: full verification success after memory compaction.

### Next
Run Done-state CI; if green, prepare PR #2 for squash merge.
