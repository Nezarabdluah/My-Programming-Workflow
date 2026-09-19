# Active Tasks — AOS v8.0-dev

## T026 — Risk & Affected-Area Context Routing 🔴
- **State:** Executing
- **Branch:** `aos-v8-sprint2-risk-routing`
- **Approval:** Navigator approved Sprint 2 continuation.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing

### Acceptance Criteria
- True risk flags deterministically add required capabilities.
- Project affected-area rules add project-specific capabilities.
- Explicit capabilities are preserved; derived duplicates are de-duplicated.
- Broker reports declared/effective capabilities and provenance sources.
- Risk/area mappings may reference only executable capabilities.
- Current T026 derives Testing although it declares only Architecture.
- Mutations prove missing/invalid derivation mappings are detected.
- No merge before final green CI.

### Progress
- [x] ADR-011 approved.
- [x] Core risk→capability map added.
- [x] Project area→capability rules added.
- [x] Broker derives and explains effective capabilities.
- [x] Task Contract validates affected areas.
- [x] GOV-T31–T35 + routing mutations added.
- [ ] Run CI and fix failures.
- [ ] Validating-state + Done-state CI.

### Next
Run PR CI; verify T026 derives Testing and all routing gates stay green.
