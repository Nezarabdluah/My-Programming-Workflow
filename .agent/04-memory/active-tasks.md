# Active Tasks — AOS v8.0.0-rc.1

## T034 — One-Command Consumer Bootstrap 🔴
- **State:** Validating
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating

### Acceptance Criteria
- One command performs safe preflight, install/upgrade, discovery, initialization, and portable verification.
- Foreign agent infrastructure must block before writes.
- Existing AOS upgrades must preserve project state and back up managed adapters.
- Consumer governance/provenance must be portable and source-scoped correctly.
- Real consumer bootstrap smoke must pass in CI.
- README must present bootstrap as default onboarding.
- Boot must remain ≤150.

### Evidence
Run `35445855519`: 45 PASS, 32/32 mutations, consumer bootstrap smoke PASS, Evidence Bundle/History PASS.

### Next
Run Validating-state verification; close T034 only if source + consumer paths remain green.
