# Active Tasks — AOS v8.0-dev

## T024 — Evidence Bundle & Approval Policy 🔴
- **State:** Done
- **Branch:** `aos-v8-sprint2-evidence-approval`
- **Approval:** Navigator approved Sprint 2 continuation.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating → Done

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
- [x] Final Validating-state CI passed.
- [x] T024 closed; awaiting Done-state CI for T09.

### Evidence
Run `35437710721`: full Validating-state verification success.

### Next
Run Done-state CI; if green, prepare PR #3 for squash merge.
