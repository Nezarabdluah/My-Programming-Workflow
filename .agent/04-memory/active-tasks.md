# ⏳ Active Tasks & SDD States (AOS v7.0)

> **Current state**: T013 "Islands to Pipeline" integration COMPLETE — full resource injection system deployed.
> **Active branch**: N/A — the upgrade runs on the `.agent` system itself

---

## 🎯 Main Task: AOS v7.0 "Wired Pipeline" Upgrade (🔴 Sensitive — ADR-003)

### Completed Phases (1-6) — DO NOT re-inspect:
- [x] T001-T010: path fixes, version unification, INDEX, anchors, frontmatter, wiring-registry, master-pipeline (10 files), qa-strategy, production-readiness, session-prompt Path D, governance pre-Done gate, EARS notation, layer priority, English conversion (~45 operational files)

### T011: Heavy References Translation (PARTIAL ✅)
- [x] DevOps reference: 2196 lines, fully English, 18 OPS anchors
- [x] QA reference: 1775 lines, fully English, 11 QA anchors
- [/] Books file: 1412 lines on disk (damaged by subagent, partially recovered) — constitutions extracted as replacement strategy

### T013: "Islands to Pipeline" Integration (DONE ✅ + REVIEWED ✅)
**Goal**: make the model USE every AOS resource professionally through mandatory stages.
- [x] Created 6 constitution files (79 actionable rules from 16 engineering books)
- [x] Created `00-master-index.md` — Resource Injection Matrix (157 lines)
- [x] Updated `wiring-registry.md` — Constitution (L4-C) column + Mandatory Injection
- [x] Updated `00-coordinator.md` — Mandatory Resource Injection Protocol
- [x] Updated `session-prompt.md` — 5-step resource loading
- [x] Updated `INDEX.md` — constitutions + master index entries
- [x] **REVIEW FIX**: Fixed 4 wrong filenames in master-index (security-review→security-checklist, testing-strategy→testing-and-quality, error-handling-and-resilience→testing-and-quality §3, pr-template→pull_request_template)
- [x] **REVIEW FIX**: Added MANDATORY injection refs to all 8 stage files (1-8)
- [x] **REVIEW FIX**: Integrated orphaned files: persona.md + github-security-gate.yml into master-index
- [x] **REVIEW FIX**: Updated books/00-index.md to point to new constitution structure
- [x] Final verification: 9/9 checks green (all paths valid, zero orphans, zero Arabic)

### REMAINING (updated 2026-09-07):
- [x] T021: README refresh + GitHub push (🟢 DONE): 9 README updates (114 lessons, 20/20, EN governance, enforcement tags, FAQ); secret scan clean; git init/add/commit (652e89c) + fixed .gitignore path bugdropping claude-skills gitlink (540eec5); pushed main → https://github.com/Nezarabdluah/My-Programming-Workflow.
- [x] T020: Lessons reconstruction (🔴 DONE 2026-09-07): R1-R10 complete — lessons 1-114 contiguous (91 reconstructed: CleanArch 34-40, DDD 41-48, GoF 49-60, OWASP2025 61-68, SQL 69-76, SE+Net 77-86, Pragmatic+Refactoring 87-97, Legacy+DevOps+AI 98-114 incl. capstone); books 1412→2337 lines, 0 Arabic project-wide; fixed 1 stray CJK char; claude-skills → submodule path+docs. Governance 8/2 (T01/T02 pre-existing).
- [x] T018: Strict review (🟡 DONE): 0 Arabic files repo-wide; py_compile ALL OK; 47/47 referenced paths exist; books 1412 + 0 bare Arabic-Version headers; matrix/Step4 wiring intact; placeholders clean; governance 8/2 (T01/T02 pre-existing — task-state format findings, NOT fixed to avoid fabricating state); __pycache__ cleaned.
- [x] T019: Matrix 20/20 (🟢 DONE): added Wiring Registry (Stage 0) + Governance Runner (Stage 5) rows — Resource Injection Matrix now literally maps every resource.
- [x] T017: Zero-Arabic + governance-EN (🟡 DONE 2026-09-07): runner+3 tests fully English (8/2 verified, T04 counts correctly); project-wide audit = 0 files with Arabic (was 812 lines); books 798→0, 1412 lines preserved, EN lesson headers 0→73; backups: T016-chunks + T017-books-full-md5 in Temp. Supersedes T014.
- [x] T016: Residual-islands closure (🟡 DONE): Books Archive rows in matrix Stage 2+4; chunk1-3 deleted after verified backup; ABP line in Step 4; shims + root AGENTS.md bridge; root .gitignore; paths → placeholder; runner v7.0 + UTF-8 guard.
- [x] T015: Gap-closure hardening (🟡 Medium — Approved + DONE): hardened 4 workflows + 2 coordinators with 00-master-index MUST refs + CONST/REF citation format + summary line; added ABP Prompts row to master-index Stage 4; added Mandatory Resource Injection clause to operating-contract §1. Verified: 6/6 files reference master-index, 7/7 MUST gates, governance 8/2 (T01/T02 pre-existing fails unrelated).
- [ ] T012: Books file full content recovery (user has original — needs to re-paste or export)
- [x] T014: Translate remaining Arabic in books file to English (DONE via T017 — superseded).
- [ ] Permanent load budget re-verification (after all changes)

## Key verified facts:
- Constitution path prefix: `05-references/books/constitutions/`
- Master Index: `05-references/books/00-master-index.md`
- 6 constitutions = 79 actionable rules from 16 engineering books
- Injection modes: MUST (gate blocked) | SHOULD (recommended) | IF (conditional)
- Citation format: `// [CONST-SEC-3]` for constitutions, `// [REF-DB-N1]` for rules
