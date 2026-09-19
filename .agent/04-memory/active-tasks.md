# Active Tasks & SDD State — AOS v8.0-dev

> Current work only. Historical completed tasks belong in `04-memory/archive/`.

## T022 — AOS v8 Convergence Sprint 🔴

- **State:** Executing
- **Branch:** `aos-v8-convergence`
- **Purpose:** make runtime policy, workflows, governance, and memory match approved ADR-006/ADR-007 before Sprint 2 features.
- **Approval:** developer approved starting implementation after the audit and convergence plan.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing

### Acceptance Criteria
- `boot-manifest.md` is the canonical runtime entry point.
- Fixed seven-layer full-stack governance is removed from Core and is profile-scoped.
- Reference/resource loading follows ADR-007 selective context expansion.
- Legacy v7 entry/session workflows cannot override v8 runtime policy.
- Governance checks validate v8 behavior instead of legacy artifacts.
- Boot memory contains current state only; historical tasks are archived.
- No change is merged to `main` before review and verification.

### Current Progress
- [x] Created isolated convergence branch.
- [x] Demoted legacy `session-prompt.md` to a compatibility shim.
- [x] Routed legacy session start to `boot-manifest.md`.
- [x] Applied ADR-006 to Core vertical-slice policy and pipeline stages.
- [x] Applied ADR-007 selective context expansion to Core, registry, resource index, pipeline, QA, and UX workflow.
- [x] Migrated init/end-session workflows to v8 semantics.
- [ ] Harden governance T09/T10 and Boot budget semantics.
- [ ] Reconcile INDEX and remaining v7 headers/legacy authorities.
- [ ] Add AOS self-development mode.
- [ ] Run/collect full regression evidence before PR/merge.

### Next Step
Harden governance and verify that checks fail on real convergence violations instead of passing on textual markers.
