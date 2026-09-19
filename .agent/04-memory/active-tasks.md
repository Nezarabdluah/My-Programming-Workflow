# Active Tasks — AOS v8.0.0-rc.1

## T035 — Zero-Setup One-Command Bootstrap 🔴
- **State:** Validating
- **Approval:** explicit Navigator approval to make onboarding truly one-command.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating

### Acceptance Criteria
- README starts with one copy-paste command per supported shell, run from the consumer project.
- Remote launchers use a temporary source checkout and delegate all target writes to `bootstrap.py`.
- Foreign agent infrastructure still blocks before any target write.
- Existing AOS safe-upgrade preservation remains unchanged.
- Launcher smoke coverage runs in CI for Bash and PowerShell.
- Internal phases remain documentation, not user setup steps.
- Boot remains ≤150.

### Plan
- [x] Add root Bash and PowerShell launchers with temporary cleanup.
- [x] Make current-directory bootstrap the primary README UX.
- [x] Add deterministic governance/mutation/smoke coverage.
- [ ] Run full verification and CI before Done.

### Next
Validate both launcher paths in CI before Done.
