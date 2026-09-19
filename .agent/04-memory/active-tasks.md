# Active Tasks — AOS v8.0.0-rc.1

## T031 — README Showcase & Complete Capability Map 🔴
- **State:** Validating
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating

### Acceptance Criteria
- README must explain purpose, capabilities, lifecycle, and first-run flow from one page.
- Capability coverage must include Architecture, Security, QA, DevOps, Reliability, Performance, API, UX, Mobile, Memory, Governance, Evidence, and Knowledge.
- Mermaid diagrams must explain runtime/lifecycle/evidence visually.
- README must distinguish user-facing overview from executable authority.
- GOV-T41 + mutation must protect the showcase.
- Final verification must remain green.

### Result
- [x] ADR-014 approved.
- [x] README rebuilt as complete capability showcase.
- [x] 5 Mermaid diagrams + end-to-end onboarding added.
- [x] GOV-T41 + mutation added.
- [x] Executing-state verification: 41/41 + 28/28, Boot 138/150.
- [ ] Validating-state verification.
- [ ] Done-state verification.

### Evidence
Run `35441879771`: 41 PASS, 28/28 mutations, 5 Mermaid diagrams, Boot 138/150.

### Next
Validate the README showcase, then close T031 only if all gates stay green.
