# Active Tasks — AOS v8.0-dev

## T029 — v8 Release Readiness & Sanitized Installation 🔴
- **State:** Validating
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating

### Acceptance Criteria
- Entrypoints must use Execution Gate + executable evidence.
- Consumer install must exclude source Memory/Profile/Task/evidence state.
- CI must verify PRs, main, and manual release checks.
- GOV-T38/T39 and mutations must prove release/onboarding contracts.
- Boot must be ≤150 lines before RC; no RC bump before final green evidence.

### Result
- [x] Entrypoints/start/init/CI aligned.
- [x] ADR-013 + sanitized installer.
- [x] GOV-T38/T39 + 26/26 mutation coverage.
- [x] Public docs/INDEX synchronized.
- [x] Boot reduced to 144 lines and GOV-T11 hardened to 150.
- [ ] Validating-state full verification.
- [ ] Done-state verification and release decision.

### Evidence
Completed verification `35440351468`: 39 PASS, 26/26 mutations, Boot 144/150, Evidence Bundle/History PASS.

### Next
Validate the release-readiness state; then close T029 only if all hard gates remain green.
