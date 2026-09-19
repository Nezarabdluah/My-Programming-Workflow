# Active Tasks — AOS v8.0.0-rc.1

## T034 — One-Command Consumer Bootstrap 🔴
- **State:** Executing
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing

### Acceptance Criteria
- One command performs preflight → install/upgrade → discovery → initialization → portable verification.
- Foreign agent infrastructure blocks before any AOS write.
- Recognized AOS upgrade preserves project Memory/Profile/Task/Evidence and backs up managed adapters.
- Consumer governance must not depend on AOS-source README/release state.
- Runtime approval provenance must be portable and source-only patterns must not authorize consumer tasks.
- Fresh consumer bootstrap must be behaviorally tested and CI-smoked.
- README makes bootstrap the default path; manual install/init remains fallback only.
- Full verification remains green; Boot stays ≤150.

### Progress
- [x] Safe installer preflight + upgrade preservation/backups.
- [x] Portable runtime ADR registry + approval scope enforcement.
- [x] Consumer/source governance and mutation separation.
- [x] One-command `bootstrap.py` implemented.
- [x] Behavioral tests T42–T45 + mutations.
- [x] CI consumer bootstrap smoke test added.
- [x] README switched to one-command UX.
- [ ] Align INDEX/init workflow and run full verification.
- [ ] Fix smoke/governance failures.
- [ ] Validating + Done-state verification.

### Next
Run full verification and consumer smoke; fix any portability blocker.
