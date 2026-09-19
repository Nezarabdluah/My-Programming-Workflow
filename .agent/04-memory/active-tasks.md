# Active Tasks & SDD State — AOS v8.0-dev

> Current work only. Historical completed tasks belong in `04-memory/archive/`.

## T022 — AOS v8 Convergence Sprint 🔴
- **State:** Validating
- **Branch:** `aos-v8-convergence`
- **Purpose:** align runtime policy, workflows, governance, and memory with ADR-006/ADR-007 before Sprint 2.
- **Approval:** developer approved implementation after audit and convergence planning.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating

### Acceptance Criteria
- `boot-manifest.md` is the canonical runtime entry point.
- Full-stack seven-layer governance is profile-scoped, not Core.
- Context expansion follows ADR-007 selective loading.
- Governance validates v8 behavior rather than legacy artifacts.
- Current memory excludes historical completed tasks.
- No merge to `main` before review and full verification.

### Progress
- [x] Canonical entry + legacy compatibility shims.
- [x] ADR-006/007 applied across Core, resource registry/index, pipeline, QA/UX, init/closeout.
- [x] Historical active-task log archived.
- [x] T09/T10/Boot-budget governance hardened; full `verify.py` added.
- [x] AOS self-development mode added.
- [x] Reconciled INDEX, classification, token budget, collaboration policy, and remaining v7 authority drift.
- [x] Full GitHub Actions verification passed on current branch head (governance + mutations).
- [x] Draft PR #1 opened for validation only; not merged.
- [ ] Final validation pass after this memory-state update.
- [ ] Mark Done only after final CI remains green and diff review has no blockers.

### Validation Evidence
- GitHub Actions workflow: `AOS Verify`
- Latest validated run before state transition: `35436735290` → success
- Governance: 11/11 PASS
- Mutation tests: 8/8 detected, 0 missed
- Drift scan: no active v7/mandatory-bundle/fixed-seven-layer markers found

### Next Step
Run final CI after the Validating-state memory update, then close T022 only if it remains green.
