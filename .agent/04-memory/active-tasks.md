# Active Tasks — AOS v8.0-dev

## T029 — v8 Release Readiness & Sanitized Installation 🔴
- **State:** Executing
- **Approval:** explicit Navigator approval.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing

### Acceptance Criteria
- All public/automatic entrypoints route through Execution Gate + executable evidence.
- `start.py --check` runs full governance + mutations.
- CI verifies pull requests, `main`, and manual release checks.
- Consumer install excludes source Memory, Project Profile, current Task Contract, and generated evidence.
- Initialization creates target-specific state before full governance is expected to pass.
- GOV-T38 protects release entrypoint/runtime alignment.
- GOV-T39 behaviorally verifies sanitized installation.
- Mutations prove T38/T39 can fail.
- Public metrics and INDEX match the release-readiness runtime.
- No RC version bump until final readiness verification is green.

### Progress
- [x] Entry adapters, start.py, init workflow, and CI triggers aligned.
- [x] ADR-013 + sanitized installer implemented.
- [x] GOV-T38/T39 + mutations added.
- [x] README and INDEX onboarding synchronized.
- [ ] Run full verification and fix blockers.
- [ ] Audit Boot budget toward final 150-line target.
- [ ] Decide RC readiness only after green final evidence.

### Next
Run release-readiness verification and resolve any remaining blockers.
