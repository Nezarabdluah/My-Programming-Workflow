# Active Tasks — AOS v8.0.0-rc.1

## T030 — v8.0.0-rc.1 Release Candidate Cut 🔴
- **State:** Executing
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing

### Acceptance Criteria
- VERSION and active runtime/public markers must be v8.0.0-rc.1.
- GOV-T40 must detect version drift; mutation must prove it fails.
- Public metrics must show 40 governance checks / 27 mutations.
- Boot must remain ≤150 lines.
- Release candidate must pass Execution Gate, Evidence Bundle/History, governance, and mutations.
- No tag/release until completed-state verification and main push verification are green.

### Progress
- [x] VERSION set to 8.0.0-rc.1.
- [x] Active runtime/public version markers migrated.
- [x] GOV-T40 + version-drift mutation added.
- [x] README metrics updated to 40 / 27.
- [ ] Run full RC verification.
- [ ] Validating + Done-state verification.
- [ ] Merge RC cut and verify main push before tag/release.

### Next
Run the full RC verification and fix any version-consistency blocker.
