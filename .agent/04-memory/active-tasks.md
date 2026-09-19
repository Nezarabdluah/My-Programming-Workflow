# Active Tasks & SDD State — AOS v8.0-dev

> Current work only. History is archived under `04-memory/archive/`.

## T022 — AOS v8 Convergence Sprint 🔴
- **State:** Validating
- **Branch:** `aos-v8-convergence`
- **Purpose:** align runtime, workflows, governance, and memory with ADR-006/ADR-007 before Sprint 2.
- **Approval:** developer approved implementation after audit/planning.

### State History
Draft → Clarify → Approved → Planning → Ready → Executing → Validating

### Acceptance Criteria
- Canonical runtime entry = `boot-manifest.md`.
- Seven-layer full-stack policy is profile-scoped, not Core.
- Context loading follows ADR-007 selective expansion.
- Governance validates v8 behavior and catches deliberate mutations.
- Current boot memory excludes historical completed tasks.
- No merge to `main` before final green verification.

### Progress
- [x] Core/pipeline/rules/memory converged to v8 semantics.
- [x] Legacy task history archived.
- [x] Governance hardened; `verify.py` + GitHub Actions added.
- [x] Draft PR #1 opened, unmerged.
- [x] Diff review completed; remaining v7 authority drift removed.
- [ ] Final CI after memory compaction.
- [ ] Mark Done only if final CI is green.

### Last Evidence
GitHub Actions run `35436769705`: 10/11 governance PASS, 8/8 mutations; only GOV-T11 failed because boot memory grew to 212 lines.

### Next Step
Compact boot memory below 200, rerun CI, then close T022 if green.
