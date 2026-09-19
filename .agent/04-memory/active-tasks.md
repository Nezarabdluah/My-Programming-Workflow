# Active Tasks — AOS v8.0-dev

## T028 — Merge-Safe Durable Memory 🔴
- **State:** Executing
- **Approval:** explicit Navigator approval for the architecture change.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing

### Acceptance Criteria
- Boot Memory excludes volatile branch/PR/mergeability/queued-CI state.
- Immutable completed evidence remains allowed.
- End-session and boot handoff rules define durable vs volatile state.
- GOV-T37 detects volatile VCS state in Boot Memory.
- Mutation proves GOV-T37 can fail.
- README/public metrics reflect T37 and mutation coverage.
- Execution Gate approves T028 under explicit human provenance.
- Final verification remains green before completion.

### Progress
- [x] ADR-012 approved.
- [x] Boot + end-session memory rules updated.
- [x] GOV-T37 + mutation added.
- [x] README updated to 37 checks / 24 mutations.
- [x] T028 Task Contract added.
- [x] Boot Memory rewritten without volatile VCS state.
- [ ] Run full CI and fix failures.
- [ ] Validating-state verification.
- [ ] Done-state verification.

### Next
Validate merge-safe memory semantics and governance evidence.
