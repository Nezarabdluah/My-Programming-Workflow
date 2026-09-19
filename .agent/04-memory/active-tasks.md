# Active Tasks — AOS v8.0.0-rc.1

## T033 — README Three-Step Quick Start 🟡
- **State:** Validating
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating

### Acceptance Criteria
- README begins with a simple 3-step startup path.
- Installation model is explicit: one AOS source copy, per-project `.agent`, no background service.
- Windows and generic install examples are shown.
- Initialization and normal task usage are understandable without browsing internal files.
- GOV-T41 protects the Quick Start markers.
- Full verification remains green; Boot stays ≤150.

### Evidence
Run `35443861839`: 41 PASS, 28/28 mutations, GOV-T41 PASS, Boot 135/150.

### Next
Run Validating-state verification; close T033 only if green.
