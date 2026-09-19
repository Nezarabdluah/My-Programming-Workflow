# Active Tasks — AOS v8.0.0-rc.1

## T030 — v8.0.0-rc.1 Release Candidate Cut 🔴
- **State:** Validating
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating

### Acceptance Criteria
- VERSION/runtime/public markers must match v8.0.0-rc.1.
- GOV-T40 + mutation must enforce version consistency.
- Public baseline must be 40 checks / 27 mutations.
- Boot must remain ≤150 lines.
- RC must pass Execution Gate, Evidence Bundle/History, governance, and mutations.
- No tag/release before completed-state and main push verification are green.

### Progress
- [x] RC1 markers and GOV-T40 synchronized.
- [x] Executing-state verification: 40/40 + 27/27.
- [ ] Validating-state verification.
- [ ] Done-state verification.
- [ ] Merge, verify main push, then tag/release.

### Evidence
Run `35441275931`: 40 PASS, 27/27 mutations, Boot 144/150, Evidence Bundle/History PASS.

### Next
Validate RC1 state; close T030 only if all hard gates remain green.
