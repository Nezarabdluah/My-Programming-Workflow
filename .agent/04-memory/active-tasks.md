# Active Tasks — AOS v8.0.0-rc.1

## T034 — One-Command Consumer Bootstrap 🔴
- **State:** Done
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating → Done

### Acceptance Criteria
- One command safely installs/upgrades, discovers, initializes, and verifies a consumer project.
- Foreign agent infrastructure blocks before any AOS write.
- Existing AOS upgrades preserve project state and back up managed adapters.
- Consumer governance/provenance remains portable and source-scoped.
- Real consumer bootstrap smoke passes in CI.
- README exposes bootstrap as the default onboarding path.
- Boot remains ≤150.

### Result
- [x] Collision-safe installer + safe upgrade/backups.
- [x] Portable runtime ADR/provenance + consumer/source governance split.
- [x] One-command bootstrap + T42–T45 + 32/32 mutations.
- [x] CI consumer bootstrap smoke.
- [x] Executing + Validating verification passed.

### Evidence
Run `35445890991`: 45 PASS, 32/32 mutations, bootstrap smoke PASS, Boot 139/150.

### Next
Use `bootstrap.py` as the default consumer onboarding command.
