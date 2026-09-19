# Active Tasks — AOS v8.0-dev

## T024 — Evidence Bundle & Approval Policy 🔴
- **State:** Executing
- **Branch:** `aos-v8-sprint2-evidence-approval`
- **Approval:** Navigator approved continuing Sprint 2.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing

### Acceptance Criteria
- Hard-stop risks cannot self-approve through model text/pattern claims.
- Low-risk Simple work can proceed by policy without unnecessary interruption.
- Sensitive/Medium approvals use explicit provenance in Task Contract.
- Evidence checks run only named Project Profile commands.
- Evidence PASS/FAIL derives only from process exit code.
- CI generates and validates `evidence/current.json`.
- Governance/mutations prove approval and evidence failure modes.
- No merge to `main` before final green CI.

### Progress
- [x] ADR-009 approved.
- [x] Approval policy + engine implemented.
- [x] Evidence recorder + evidence semantics implemented.
- [x] T024 risk/provenance contract added.
- [x] GOV-T17–T22 added and runner integrated.
- [x] Approval/evidence mutations added.
- [x] CI switched to executable Evidence Bundle.
- [ ] Run CI and fix failures.
- [ ] Review diff, Validating-state CI, then Done-state CI.

### Next
Open/use PR, run GitHub Actions, and fix any governance/evidence failures.
