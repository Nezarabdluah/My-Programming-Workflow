# Active Tasks — AOS v8.0-dev

## T027 — Stabilization & Public Contract Sync 🟡
- **State:** Executing
- **Branch:** `aos-v8-sprint2-stabilization`
- **Approval:** verified pattern `pattern-existing-local-refactor`.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing

### Acceptance Criteria
- README describes current Execution Gate, Context Broker, approvals, evidence, and risk routing.
- Public metrics match current governance/mutation baseline.
- VERSION sync metadata is current.
- Memory reflects merged PR #5 rather than pre-merge state.
- GOV-T36 blocks stale public-contract text.
- Mutation proves GOV-T36 can fail.
- Execution Gate resolves T027 to AUTO_EXECUTE.
- No merge before final green CI.

### Progress
- [x] README rewritten to current v8 runtime.
- [x] GOV-T36 added.
- [x] README drift mutation added.
- [x] VERSION sync date updated.
- [ ] Sync current memory from merged PR #5.
- [ ] Run CI and fix failures.
- [ ] Validating + Done-state CI.

### Next
Sync memory, open PR, and run full verification.
