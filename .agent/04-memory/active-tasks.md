# Active Tasks — AOS v8.0-dev

## T029 — v8 Release Readiness & Sanitized Installation 🔴
- **State:** Done
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating → Done

### Acceptance Criteria
- Entrypoints/CI must match Execution Gate + executable evidence.
- Consumer install must exclude source project state.
- GOV-T38/T39 + mutations must enforce release/onboarding contracts.
- Boot must remain ≤150 lines before RC.

### Result
- [x] Entrypoints, start/init flow, CI triggers, README, and INDEX aligned.
- [x] ADR-013 + sanitized installer behaviorally verified.
- [x] GOV-T38/T39 with 26/26 mutation coverage.
- [x] Boot hard gate set to 150 and validated below ceiling.
- [x] T029 completed; final Done-state verification is the completion evidence.

### Evidence
Completed validation `35440422576`: 39 PASS, 26/26 mutations, Boot 146/150, Evidence Bundle/History PASS.

### Next
Use this baseline for the v8 release-candidate cut after completed-state verification.
