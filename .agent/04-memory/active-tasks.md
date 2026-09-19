# Active Tasks — AOS v8.0.0-rc.1

## T030 — v8.0.0-rc.1 Release Candidate Cut 🔴
- **State:** Done
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating → Done

### Acceptance Criteria
- VERSION/runtime/public markers must match v8.0.0-rc.1.
- GOV-T40 + mutation must enforce version consistency.
- Public baseline must be 40 checks / 27 mutations.
- Boot must remain ≤150 lines.
- RC must pass Execution Gate, Evidence Bundle/History, governance, and mutations.
- No tag/release before main push verification is green.

### Result
- [x] RC1 markers and GOV-T40 synchronized.
- [x] Executing + Validating verification passed.
- [x] T030 closed; completed-state verification remains as release evidence.

### Evidence
Run `35441304411`: 40 PASS, 27/27 mutations, Boot 145/150, Evidence Bundle/History PASS.

### Next
Verify completed state, merge RC cut, verify main push, then create the RC tag/release.
