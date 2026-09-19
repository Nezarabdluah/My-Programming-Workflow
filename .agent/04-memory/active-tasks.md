# Active Tasks — AOS v8.0-dev

## T029 — v8 Release Readiness & Sanitized Installation 🔴
- **State:** Executing
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing

### Acceptance Criteria
- Entrypoints must use Execution Gate + executable evidence.
- Consumer install must exclude source Memory/Profile/Task/evidence state.
- CI must verify PRs, main, and manual release checks.
- GOV-T38/T39 and mutations must prove release/onboarding contracts.
- Boot must be ≤150 lines before RC; no RC bump before final green evidence.

### Progress
- [x] Entrypoints/start/init/CI aligned.
- [x] ADR-013 + sanitized installer.
- [x] GOV-T38/T39 + mutations.
- [x] README/INDEX onboarding synchronized.
- [x] First release-readiness verification: 39/39 + 26/26.
- [x] Boot contract compressed; final budget enforcement in progress.
- [ ] Enforce ≤150 and rerun full verification.
- [ ] Decide RC readiness from final evidence.

### Next
Enforce the final Boot budget, then complete release-readiness validation.
