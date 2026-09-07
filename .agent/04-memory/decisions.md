# 📐 Architectural & Design Decision Log (ADR Log - AOS v7.0)

> **Contract**: updated whenever a critical architectural decision is made or amended. Records decisions, alternatives, and consequences.

---

## 🏛️ ADR-001: Adopting the Full-Stack Vertical Slice Governance Charter as a fixed Project-Agnostic rule
* **Date**: 2026-08-30
* **Status**: Approved
* **Context & problem**:
  Reports were being filed as "done" covering a single layer (e.g. API only) without justifying the fate of the remaining layers, creating gaps between Backend/Frontend/DB/Tests and breaking the vertical-slice principle of DDD/Clean Architecture.
* **Approved decision**:
  Adopt a charter of 7 mandatory layers (Database → Domain → Application → API → Frontend → UI/UX → Tests) with a four-part report (coverage table + architectural decisions + judgment calls + items needing human review). Documented in `02-rules/vertical-slice-governance.md` and merged into `01-core/operating-contract.md § 5`.
* **Rejected alternatives and why**:
  1. Horizontal slicing (layer by layer) ← rejected: delays integration-gap discovery and violates Vertical Slice
  2. Free-form reports without a fixed template ← rejected: allows silently skipping layers
  3. Making the charter optional per project ← rejected: the requirement is a fixed Project-Agnostic rule
* **Technical consequences**:
  * **Performance**: no direct negative impact; increases reporting time but reduces rework
  * **Maintainability**: a unified report format eases review and automation
  * **Security**: forces explicit Authorization and Error Handling coverage in every slice

---

## 🏛️ ADR-003: Adopting the AOS v7.0 "Wired Pipeline" architecture — declarative knowledge injection + deterministic enforcement
* **Date**: 2026-09-06
* **Status**: Approved (developer approved the final plan and foundation execution on 2026-09-06)
* **Context & problem**:
  The heavy references (books 2987 lines / devops 2195 / qa 1774) went unused because directed grep had no anchors, and the system relied on persuading the model — unreliable (arXiv:2310.01798: self-correction without external signal degrades performance). Also: an active version conflict (VERSION=7.0.0 vs 12 files on v6.0), leftover legacy paths, and a fully orphaned governance engine (`governance/runner.py` + 3 tests never linked to end-session).
* **Approved decision**:
  A 6-layer architecture with declared priority (L0 constitution / L1 memory core / L2 lazy pipeline stages / L3 rules / L4 grep-only references with stable anchors / L5 executable governance) and one-way dependency flow L2→L3→L4; declarative frontmatter (id/description/alwaysApply/globs/requires) on every loadable file; a central container `01-core/wiring-registry.md` covering all 8 REF categories (34 rules); a 9-stage master-pipeline (0-Intake → 8-Post-Launch) as coordinator + per-stage files with hard stop-gate tags and a DoD ladder by classification (🟢 mini / 🟡 1,4,5 / 🔴 full); graduated enforcement: CI > hooks > runner.py > checklist with explicitly declared confidence level.
* **Rejected alternatives and why**:
  1. A bidirectional Knowledge Graph linking everything to everything ← rejected: maintenance nightmare + context rot + violates YAGNI; one-way DI adopted (the consumer knows its dependency; the resource never knows its consumers)
  2. A separate Manifest/JSON as the wiring container ← rejected: YAML frontmatter is the de-facto standard of leading tools and reads naturally to models
  3. Relying on textual persuasion alone ("make sure you complied") ← rejected: refuted by DeepMind research; the alternative is executable evidence (exit codes / timestamped reports)
  4. A single merged file for all 9 stages ← rejected: inflates context (Context Rot); per-stage files loaded one at a time adopted (the successful mobile-qa pattern)
* **Technical consequences**:
  * **Performance**: permanent load L0+L1 ≤ ~150 lines; average lines seen per decision ~260 (under the 400 ceiling); heavy references injected only at their stage (Lazy Resolution)
  * **Maintainability**: a single wiring truth-point (wiring-registry); "point, don't copy" prevents number conflicts; claude-skills (git clone) documented as a never-indexed resource
  * **Security**: a STRIDE Threat-Model stage is mandatory in the 🔴 path before Build; a PRR/Scorecard gate before production

---

## 🏛️ ADR-004: Books anchor strategy — lesson-title grep anchors instead of inserted headers
* **Date**: 2026-09-06
* **Status**: Approved
* **Context & problem**:
  The plan assumed `engineering-books-16-distilled.txt` had zero greppable structure and required inserting `## [BOOK-*]` headers. Inspection showed the file is a raw NotebookLM chat export whose knowledge is organized as 114 numbered bilingual lessons (e.g. lesson 34 on CQRS & Event Sourcing) each ending with an "Agent Constitution" block — already greppable by number or English keyword.
* **Approved decision**:
  Do not modify the books file. The wiring registry anchors it via verbatim lesson titles/numbers and English keywords, documented in `books/00-index.md` and `01-core/wiring-registry.md`.
* **Rejected alternatives and why**:
  1. Bulk scripted insertion of ~100 anchor lines ← rejected under careful mode (no backup): regex over Arabic text in the system's most valuable file for marginal gain over title-grep
  2. Restructuring the file into proper markdown ← rejected: content rewrite, out of scope, risks semantic loss
* **Technical consequences**:
  * **Performance**: zero risk to the books file; registry-based resolution works with plain grep today
  * **Maintainability**: anchor truth lives in one place (wiring-registry); if the file is ever restructured, only the registry changes

---

## 🏛️ ADR-005: English as the operational language of AOS (Arabic for developer chat)
* **Date**: 2026-09-06
* **Status**: Approved (developer directive)
* **Context & problem**:
  The developer directed that all AOS files be in English for portability across tools and models, while continuing to chat with the developer in Arabic.
* **Approved decision**:
  All operational files (root, 01-core, 02-rules, 03-workflows + sub-workflows, 04-memory structure, reference indexes, prompts, dotnet-abp templates incl. YAML gates) are written in English. Every session prompt keeps the binding instruction "communicate with the developer in Modern Standard Arabic". The 3 heavy references stay Arabic for now (deferred P2 — T011) because their anchors are language-neutral IDs and translation risks semantic loss; intentional Arabic remains only as grep examples (lesson titles) and app-localization data.
* **Rejected alternatives and why**:
  1. Translating the heavy references now ← rejected: ~7,000 lines, high token cost, semantic-loss risk, marginal gain (anchors already English)
  2. Dropping the Arabic-chat instruction ← rejected: the developer's working language is Arabic
* **Technical consequences**:
  * **Performance**: English operational layer improves cross-model reliability; anchors and frontmatter are natively English
  * **Maintainability**: one operational language; Arabic preserved where it is data (localization) or grep targets (lesson titles)
  * **Security**: no impact

---

## 🏛️ ADR-002: [Architectural Decision Title]
* **Date**: [Date]
* **Status**: [Draft / Proposed / Approved / Rejected / Deprecated]
* **Context & problem**:
  [Describe the technical or architectural problem currently facing the project and why a decision is needed]
* **Approved decision**:
  [Describe the adopted engineering solution in detail]
* **Rejected alternatives and why**:
  1. [Alternative 1] ← [rejection reason, e.g.: increases p99 response time]
  2. [Alternative 2] ← [rejection reason, e.g.: violates Single Responsibility]
* **Technical consequences**:
  * **Performance**: [e.g.: slightly higher memory use but faster seeks]
  * **Maintainability**: [e.g.: full isolation of the data-access layer]
  * **Security**: [e.g.: double input hardening]
