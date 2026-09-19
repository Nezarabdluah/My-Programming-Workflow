# Active Tasks — AOS v8.0-dev

## T028 — Merge-Safe Durable Memory 🔴
- **State:** Done
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating → Done

### Acceptance Criteria
- Boot Memory excludes volatile branch/PR/mergeability/queued-CI state.
- Immutable completed evidence remains allowed.
- Boot/end-session define durable vs volatile state.
- GOV-T37 + mutation enforce merge-safe memory.
- Public metrics include T37 and mutation coverage.
- Execution Gate and final verification remain green.

### Result
- [x] ADR-012, Boot/end-session policy, GOV-T37, mutation, README, and T028 contract completed.
- [x] Executing and Validating verification passed.
- [x] T028 closed; final Done-state verification pending as completion evidence.

### Evidence
Completed verification `35439819747`: 37 PASS, 24/24 mutations, Evidence Bundle PASS.

### Next
Verify the completed task state; subsequent work should use merge-safe memory semantics.
