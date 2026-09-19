# Active Tasks — AOS v8.0-dev

## T024 — Evidence Bundle & Approval Policy 🔴
- **State:** Validating
- **Branch:** `aos-v8-sprint2-evidence-approval`
- **Approval:** Navigator approved Sprint 2 continuation.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating

### Acceptance Criteria
- Hard-stop risk cannot bypass explicit human approval.
- Simple low-risk work can policy-approve without interruption.
- Medium/Sensitive provenance is structured and auditable.
- Evidence executes only named Project Profile commands.
- Evidence PASS/FAIL derives from exit code.
- CI generates and validates Evidence Bundle.
- Governance/mutations cover approval/evidence failures.
- No merge before final green CI.

### Progress
- [x] ADR-009 + approval engine/policy.
- [x] Evidence recorder + generated bundle semantics.
- [x] T024 risk/provenance contract.
- [x] GOV-T17–T22 + mutations.
- [x] CI records compile + full verification evidence.
- [x] Evidence commands hardened to shell-free execution.
- [ ] Final Validating-state CI.
- [ ] Done-state CI for T09.

### Evidence
Run `35437681233`: 22/22 PASS, 14/14 mutations, Evidence Bundle PASS.

### Next
Run Validating-state CI, then close T024 only if green.
