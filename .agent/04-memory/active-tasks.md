# Active Tasks & SDD State — AOS v8.0-dev

> Current work only. History is archived under `04-memory/archive/`.

## T023 — Sprint 2 Context Broker Foundation 🔴
- **State:** Executing
- **Branch:** `aos-v8-sprint2-context`
- **Purpose:** replace manual selective-loading fallback with deterministic Context Broker + Project/Technology Profiles.
- **Approval:** Navigator explicitly asked to continue Sprint 2 after v8 convergence merged.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing

### Acceptance Criteria
- Context selection after capability declaration is deterministic and machine-testable.
- Project Profile records project type, active Technology Profiles, and real verification commands.
- Profile-gated resources do not load unless the profile is active.
- Unknown capabilities fail explicitly instead of silently guessing.
- Boot routes 🟡/🔴 work through Task Contract + Context Broker.
- Governance and mutation tests prove broker minimality/profile gating.
- Sprint 2 work stays isolated from `main` until review and green CI.

### Progress
- [x] ADR-008 approved.
- [x] Added executable `context-map.json`.
- [x] Added `context_broker.py`.
- [x] Added Project Profile + Technology Profiles.
- [x] Added structured `task-contracts/current.json`.
- [x] Added GOV-T12/T13/T14 context tests and runner integration.
- [x] Boot/init/INDEX/wiring linked to executable broker.
- [ ] Add broker mutation tests.
- [ ] Run full CI on Draft PR.
- [ ] Review diff and move to Validating only if green.

### Next Step
Add mutation coverage for broker failure modes, then open Draft PR for GitHub Actions verification.
