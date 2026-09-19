# Active Tasks & SDD State — AOS v8.0-dev

> Current work only. Historical completed tasks belong in `04-memory/archive/`.

## T022 — AOS v8 Convergence Sprint 🔴
- **State:** Executing
- **Branch:** `aos-v8-convergence`
- **Purpose:** align runtime policy, workflows, governance, and memory with ADR-006/ADR-007 before Sprint 2.
- **Approval:** developer approved implementation after audit and convergence planning.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing

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
- [ ] Reconcile INDEX and remaining v7 authority drift.
- [ ] Run full governance + mutation regression and review diff.
- [ ] Open PR only after verification evidence is available.

### Next Step
Reconcile remaining legacy authority/index references, then run full verification.
