# Active Tasks — AOS v8.0-dev

## T023 — Sprint 2 Context Broker Foundation 🔴
- **State:** Validating
- **Branch:** `aos-v8-sprint2-context`
- **Approval:** Navigator approved continuing Sprint 2.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating

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
- [ ] Final Validating-state CI.
- [ ] Done-state CI with complete T09 history.

### Last Evidence
Run `35437348178`: 15/16 PASS + 12/12 mutations; only GOV-T11 failed at 207 boot lines.

### Next
Keep boot <200, rerun CI, then close T023 if green.
