# Active Tasks — AOS v8.0-dev

## T027 — Stabilization & Public Contract Sync 🟡
- **State:** Validating
- **Branch:** `aos-v8-sprint2-stabilization`
- **Approval:** verified pattern `pattern-existing-local-refactor`.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating

### Acceptance Criteria
- README matches the current Execution Gate/Context Broker/approval/evidence runtime.
- Public governance/mutation metrics are current.
- VERSION and post-PR5 memory are current.
- GOV-T36 blocks stale public-contract text.
- Mutation proves GOV-T36 can fail.
- T027 resolves READY/AUTO_EXECUTE via verified pattern.
- No merge before final green CI.

### Progress
- [x] README synchronized to v8 runtime.
- [x] GOV-T36 + drift mutation.
- [x] VERSION + post-PR5 memory synchronized.
- [x] T17/T28 made provenance-aware.
- [x] Executing-state CI: 36/36 + 23/23.
- [ ] Validating-state CI.
- [ ] Done-state CI for T09.

### Evidence
Run `35439510825`: 36 PASS, 23/23 mutations, Evidence Bundle PASS, Boot 193/200.

### Next
Run Validating-state CI, then close T027 only if green.
