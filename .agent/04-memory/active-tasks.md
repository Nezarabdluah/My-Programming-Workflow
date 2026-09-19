# Active Tasks — AOS v8.0.0-rc.1

## T032 — README Colored Text Visual Standard 🟡
- **State:** Validating
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating

### Acceptance Criteria
- Five README visuals use plain text + arrows/boxes + colored emoji.
- No Mermaid remains in README.
- Capability coverage and source-of-truth boundary remain intact.
- ADR-014 and GOV-T41 enforce the colored-text visual standard.
- Existing GOV-T41 mutation detects showcase regression.
- Full verification remains green; Boot stays ≤150.

### Evidence
Run `35443018159`: 41 PASS, 28/28 mutations, GOV-T41 PASS, Boot 135/150.

### Next
Run Validating-state verification; close T032 only if green.
