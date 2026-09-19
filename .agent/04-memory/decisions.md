# Architectural & Design Decision Log — AOS v8.0.0-rc.1

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

## 🏛️ ADR-006: Vertical Slice Governance moves from Core to optional Technology Profile
* **Date**: 2026-09-12
* **Status**: Approved
* **Context & problem**:
  ADR-001 adopted a 7-layer Vertical Slice charter as a "fixed Project-Agnostic rule" baked into `operating-contract.md § 5`. However, the seven layers (Database, Domain, Application, API, Frontend, UI/UX, Tests) assume a full-stack web application architecture. This does not apply to CLI tools, data pipelines, embedded systems, libraries, mobile-only apps, or infrastructure modules. Embedding these layers in Core violates the v8 principle: "The core must not contain assumptions about project structure."
* **Approved decision**:
  Remove the Vertical Slice 7-layer mandate from `01-core/operating-contract.md`. The concept of "verify all affected layers" remains as a general Core principle (without naming specific layers). The 7-layer checklist moves to an optional Technology Profile (`profiles/full-stack-web.yaml` or similar) that projects can opt into. The mandatory report rule (coverage table + decisions + deviations + human-review) stays in Core as a general evidence requirement, but uses project-defined layers from the Project Manifest instead of a hardcoded list.
* **Rejected alternatives and why**:
  1. Keep the 7 layers but add "not applicable" for each ← rejected: still forces every project through a web-app mental model; adds noise for non-web projects
  2. Remove all layer-checking ← rejected: layer coverage is valuable; only the hardcoded list is the problem
* **Technical consequences**:
  * **Performance**: reduces Boot Context by ~20 lines; eliminates irrelevant checklist items for non-web projects
  * **Maintainability**: Core becomes truly project-agnostic; layer definitions live where they belong (project or profile)
  * **Security**: no impact; security verification remains a Core concern independent of layer structure

---

## 🏛️ ADR-007: 05-references become optional indexed resources outside Boot Context
* **Date**: 2026-09-12
* **Status**: Approved
* **Context & problem**:
  The `05-references/` directory contains 14 files totaling 6,062 lines, including 6 constitutions (79 rules from 16 engineering books), a 34-rule REF catalog, QA/DevOps references, and prompt templates. Currently, `session-prompt.md` mandates loading constitutions and rule files before writing any code (Steps 2-4), which inflates Task Expansion Context significantly. Some content is technology-neutral (general engineering principles) while other content is technology-specific (SARGable queries, EF Core patterns).
* **Approved decision**:
  (1) Technology-neutral references (general engineering principles, security fundamentals, testing strategy) remain as optional indexed resources loadable on demand via Context Broker.
  (2) Technology-specific references (database-specific query patterns, framework-specific conventions) move to Technology Profiles.
  (3) No reference file is loaded during Boot — all references are loaded only during Task Expansion, triggered by Context Broker based on task relevance.
  (4) The mandatory 5-step resource injection protocol in `session-prompt.md` is replaced by demand-driven loading: Context Broker determines what to load based on task classification and Project Profile.
  (5) Citation format (`// [REF-xxx]`, `// [CONST-xxx]`) becomes optional — evidence of rule compliance goes in Evidence Bundle, not in production code.
* **Rejected alternatives and why**:
  1. Delete all references ← rejected: the engineering knowledge is valuable; only the loading strategy is wrong
  2. Keep mandatory injection but reduce file sizes ← rejected: the problem is unconditional loading, not file size alone
* **Technical consequences**:
  * **Performance**: eliminates ~2,000-6,000 tokens of mandatory pre-code loading; Task Expansion loads only relevant resources
  * **Maintainability**: references evolve independently of Core; adding a new reference doesn't change Core behavior
  * **Security**: security references remain available but loaded by policy trigger, not by hardcoded prompt instruction

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


---

## ADR-008: Deterministic Context Broker with machine-readable task and project contracts
* **Date**: 2026-09-19
* **Status**: Approved (Sprint 2 direction accepted by the Navigator)
* **Context & problem**:
  ADR-007 made context loading selective, but the current runtime still relies on the agent manually interpreting Markdown wiring. That keeps resource selection partly heuristic, difficult to test, and vulnerable to loading too much or silently missing relevant context.
* **Approved decision**:
  Introduce a deterministic Context Broker. A structured Task Contract supplies classification and explicit capabilities; a Project Profile supplies project type, activated Technology Profiles, and executable verification commands; a machine-readable Context Map is the single executable capability→resource mapping. The broker returns the minimum ordered resource set and never infers architecture from file count alone. Human/model reasoning may decide capabilities, but resource resolution after that decision is deterministic and testable.
* **Rejected alternatives and why**:
  1. Natural-language-only broker ← rejected: difficult to test and reproduces the same heuristic loading problem.
  2. Duplicate the existing Markdown wiring into several profile files ← rejected: creates multiple truth sources and drift.
  3. Require external YAML libraries ← rejected for Core: AOS governance should run on stock Python; JSON is used for executable contracts.
* **Technical consequences**:
  * **Performance**: predictable minimal context expansion and zero external parser dependency.
  * **Maintainability**: capability routing becomes machine-testable; Markdown registry becomes documentation over the executable map.
  * **Security**: sensitive capabilities can deterministically require security resources and stronger verification without depending on prompt memory.


---

## ADR-009: Policy-based approval engine and executable Evidence Bundle
* **Date**: 2026-09-19
* **Status**: Approved (Sprint 2 continuation authorized by the Navigator)
* **Context & problem**:
  AOS currently has a strict approval gate for non-trivial work, but the runtime does not distinguish between genuinely new/high-risk decisions and work already covered by approved policy/ADR/patterns. This causes unnecessary interruptions. Separately, verification evidence is spread across reports/logs and can be asserted textually instead of being captured as structured execution results.
* **Approved decision**:
  (1) Add a deterministic Approval Engine driven by Task Contract classification, explicit risk flags, and approval provenance.
  (2) Hard-stop risks (destructive/irreversible operations, new architecture/security boundary, production changes, breaking external contracts, data migration) require human approval unless an explicit approved ADR/policy reference permits the exact action.
  (3) Low-risk Simple work is policy-approved automatically; Medium work inside established patterns may proceed when risk flags are clear; Sensitive work requires accepted provenance (human/approved ADR/approved pattern) and never silently self-approves a hard-stop risk.
  (4) Add an executable Evidence Bundle recorder that runs declared verification commands and records command, exit code, timestamp, source, and PASS/FAIL. PASS is derived from exit code and cannot be authored manually.
* **Rejected alternatives and why**:
  1. Ask the developer before every 🟡/🔴 task ← rejected: excessive interruption and poor autonomy.
  2. Let the model decide approval in free text ← rejected: not deterministic or auditable.
  3. Store verification only as prose in memory/PRs ← rejected: claims are not executable evidence.
* **Technical consequences**:
  * **Performance**: fewer unnecessary approval pauses; small execution overhead for structured verification.
  * **Maintainability**: approval logic and evidence semantics become testable/versioned.
  * **Security**: hard-stop risks cannot auto-approve merely because the model says a pattern exists.


---

## ADR-010: Verified approval provenance, explicit execution mode, and tamper-evident evidence history
* **Date**: 2026-09-19
* **Status**: Approved (Sprint 2 continuation authorized by the Navigator)
* **Context & problem**:
  ADR-009 introduced structured approval provenance and executable evidence, but `approved_adr` / `approved_pattern` references are still trusted as plain text, execution intent is only implicit in APPROVED/BLOCKED, and `evidence/current.json` retains only the latest task evidence.
* **Approved decision**:
  (1) Add a machine-readable approval registry. Non-human provenance such as `approved_adr` and `approved_pattern` must resolve to an approved registry entry and match declared scope before the task can auto-execute.
  (2) Approval evaluation returns an explicit execution mode: `AUTO_EXECUTE`, `HUMAN_APPROVED`, or `HUMAN_REQUIRED`.
  (3) Hard-stop risks always require explicit human approval; registry entries cannot bypass this boundary.
  (4) Add evidence history archiving with SHA-256 content hashes. Current evidence remains generated and ephemeral; archived bundles are immutable-by-convention records suitable for CI artifacts/audit review.
  (5) Add executable Task Contract validation so malformed risk/provenance fields fail before approval/context resolution.
* **Rejected alternatives and why**:
  1. Trust any string in `approval.reference` ← rejected: spoofable provenance.
  2. Store all evidence history directly in Git by default ← rejected: repository bloat and noisy churn.
  3. Keep binary APPROVED/BLOCKED only ← rejected: does not tell the agent whether it may proceed autonomously or must wait for a human.
* **Technical consequences**:
  * **Performance**: negligible local validation/hash cost.
  * **Maintainability**: approval provenance and execution mode become deterministic and auditable.
  * **Security**: hard-stop boundaries cannot be bypassed by forged ADR/pattern text; archived evidence can be integrity-checked.


---

## ADR-011: Risk- and affected-area-aware capability derivation
* **Date**: 2026-09-19
* **Status**: Approved (Sprint 2 continuation authorized by the Navigator)
* **Context & problem**:
  The Context Broker currently trusts the Task Contract's explicit `capabilities` list. If an agent correctly marks `security_boundary`, `data_migration`, `production_change`, or an affected path such as CI/deployment files but forgets the corresponding capability, relevant rules can be omitted.
* **Approved decision**:
  (1) Keep explicit capabilities as the primary declaration.
  (2) Add a Core `risk_capability_map` in `context-map.json` that deterministically augments capabilities from true risk flags.
  (3) Add project-specific `area_capability_rules` in Project Profile so repository paths can activate relevant capabilities without hardcoding project structure into Core.
  (4) Context Broker returns declared capabilities, effective capabilities, and provenance for every derived capability.
  (5) Derived capabilities are additive only; the broker never silently removes an explicit capability.
* **Rejected alternatives and why**:
  1. Natural-language inference from task title/body ← rejected: non-deterministic and difficult to test.
  2. Hardcode repository paths in Core ← rejected: violates project-agnostic architecture.
  3. Let risk only affect approval, not context ← rejected: approval safety does not guarantee the agent loaded the right engineering guidance.
* **Technical consequences**:
  * **Performance**: small deterministic expansion only when risk/area evidence activates a capability.
  * **Maintainability**: project-specific path knowledge stays in Project Profile; Core keeps generic risk semantics.
  * **Security**: sensitive risk flags automatically activate their relevant context even when explicit capability declaration is incomplete.


---

## ADR-012: Merge-safe durable memory excludes volatile VCS state
* **Date**: 2026-09-19
* **Status**: Approved (Sprint 2 continuation authorized by the Navigator)
* **Context & problem**:
  Boot Memory repeatedly stored branch names, pull-request status, and next-step instructions such as "merge PR" or "run Done-state CI". Those statements were true on the feature branch but became stale immediately after squash merge, forcing a new repair task after nearly every merge.
* **Approved decision**:
  (1) Durable Boot Memory must record project/task facts that remain true across branch and PR transitions.
  (2) Current branch, PR state, mergeability, queued/in-progress CI state, and "merge this PR next" are volatile VCS state and must be queried live from the repository instead of persisted in `project-context.md` or `active-tasks.md`.
  (3) Immutable evidence identifiers such as commit SHAs, completed CI run IDs, ADR IDs, and completed task states may be stored.
  (4) Completed task memory should end with an engineering next step, or no next step, rather than repository-transport instructions.
  (5) Governance must detect volatile VCS state in canonical Boot Memory.
* **Rejected alternatives and why**:
  1. Run a post-merge memory repair commit after every PR ← rejected: creates endless follow-up churn and another merge cycle.
  2. Store PR/branch facts with "may be stale" labels ← rejected: Boot Memory should be reliable by default.
  3. Remove all execution evidence from memory ← rejected: immutable completed evidence remains useful for handoff and audit.
* **Technical consequences**:
  * **Performance**: smaller Boot Memory and fewer repair commits.
  * **Maintainability**: memory remains valid across squash/rebase/branch transitions.
  * **Security**: reduces incorrect operational decisions caused by stale repository state.


---

## ADR-013: Sanitized two-phase installation for consumer projects
* **Date**: 2026-09-19
* **Status**: Approved (release-readiness requirement)
* **Context & problem**:
  Copying the repository's entire `.agent` directory into a consumer project also copies source-specific state such as `profiles/project.json`, `task-contracts/current.json`, Boot Memory, and generated evidence. That can make a new project start with AOS's own identity, task, approval, and history.
* **Approved decision**:
  (1) Split onboarding into Install and Initialize.
  (2) Install copies only reusable runtime assets: Core, rules, workflows, references, templates, governance, ADR templates, Technology Profiles, INDEX, AGENTS, VERSION, and evidence documentation.
  (3) Install must not copy source-specific Project Profile, current Task Contract, Boot Memory, or generated Evidence History.
  (4) Initialize discovers the target repository and creates target-specific Memory, Project Profile, Task Contract, and verification commands before full governance is expected to pass.
  (5) Provide an executable installer so users do not need to manually remember the exclusion list.
* **Rejected alternatives and why**:
  1. Continue recommending `cp -r .agent` and ask the agent to clean it afterward ← rejected: stale source state is already present during boot and can bias decisions.
  2. Keep source-specific files but label them examples ← rejected: executable runtime reads them as current state.
  3. Publish a second manually maintained runtime tree ← rejected: duplicates the source of truth and increases drift.
* **Technical consequences**:
  * **Performance**: negligible copy overhead.
  * **Maintainability**: one source runtime with deterministic exclusions.
  * **Security**: prevents accidental reuse of source approvals, project identity, and evidence in unrelated repositories.


---

## ADR-014: README is the complete user-facing capability map, not a second runtime authority
* **Date**: 2026-09-19
* **Status**: Approved (Navigator requested a complete README experience)
* **Context & problem**:
  AOS has a rich runtime across Core, workflows, rules, profiles, references, governance, DevOps, security, QA, UX, memory, and evidence. A technically correct README can still force a new user to browse many files just to understand what the project contains, how the pieces connect, and how to start. That weakens discoverability and makes the project look smaller than it is.
* **Approved decision**:
  (1) README is the canonical **user-facing overview**: a new user should understand the project's purpose, capabilities, lifecycle, major subsystems, installation, first-run flow, evidence model, governance strength, and where to go deeper without browsing the repository first.
  (2) README must include lightweight colored text capability/lifecycle maps using plain text, arrows, box-drawing characters, icons, and colored-square emoji; Mermaid and image-only diagrams are not the default. The capability matrix must cover Architecture, Security, Testing/QA, DevOps/Deployment, Reliability/Observability, Database/Performance, API/Network, UX/Frontend, Mobile QA, Memory/Learning, Governance, Evidence, and Knowledge.
  (3) README must clearly distinguish overview documentation from executable authority: `boot-manifest.md`, Task Contract, Execution Gate, Context Map, Profiles, and Project Profile remain runtime sources of truth.
  (4) README should link concepts to their authoritative files instead of duplicating detailed rules that can drift.
  (5) Governance must fail if the README loses its required overview sections, visual maps, quick-start path, source-of-truth boundary, or major capability coverage.
* **Rejected alternatives and why**:
  1. Keep README minimal and make users browse `.agent` ← rejected: poor onboarding/discoverability.
  2. Copy all runtime rules into README ← rejected: creates a second executable truth source and drift.
  3. Rely on screenshots only ← rejected: harder to maintain, search, diff, and keep accessible.
  4. Use Mermaid as the default README visual language ← rejected after Navigator review: colored text diagrams are faster to scan, lighter, copyable, and match the desired project presentation.
* **Technical consequences**:
  * **Usability**: users can understand AOS from one page before opening internal files.
  * **Maintainability**: deep rules remain in authoritative runtime files.
  * **Governance**: public capability coverage becomes testable rather than editorial.


---

## ADR-015: One-command bootstrap with collision-safe consumer onboarding
* **Date**: 2026-09-19
* **Status**: Approved
* **Context & problem**:
  The previous consumer flow required a sanitized install command, then a separate agent-driven initialization step. It also treated existing agent infrastructure too simplistically: projects may already contain `.agent`, `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, or Copilot instructions from another system. Blind merge/overwrite is unsafe.
* **Approved decision**:
  (1) Make `.agent/bootstrap.py <target>` the default consumer onboarding command.
  (2) Bootstrap performs write-free preflight, safe install/upgrade, conservative project discovery, target-specific state initialization, and portable AOS verification.
  (3) Foreign or unknown agent infrastructure blocks before any AOS write; AOS never guesses, deletes, renames, or merges it automatically.
  (4) Recognized AOS upgrades preserve Memory, Project Profile, Task Contract, and Evidence History; managed root adapters are backed up before refresh.
  (5) Runtime ADRs required by AOS live in bundled `.agent/adr/system-decisions.md`; project ADRs remain in project Memory.
  (6) AOS-source-only governance/mutations are skipped in consumer projects while portable runtime governance still runs.
  (7) Project discovery is evidence-based; uncertain stacks return `NEEDS_REVIEW` instead of fabricated commands/profile data.
* **Rejected alternatives and why**:
  1. Keep install + manual initialization as the primary UX ← rejected: avoidable friction and setup mistakes.
  2. Auto-merge any existing `.agent` or agent instruction files ← rejected: can silently corrupt another agent system.
  3. Always overwrite existing AOS project state during upgrade ← rejected: destroys durable project memory and evidence.
  4. Assume a stack from folder names alone ← rejected: weak evidence and unsafe automation.
* **Technical consequences**:
  * **Usability**: one command produces a ready or explicitly review-required project.
  * **Safety**: collision detection happens before writes; upgrades preserve durable state.
  * **Portability**: consumer verification no longer depends on AOS-source README/release files.
  * **Maintainability**: bootstrap behavior is covered by governance, mutations, and an end-to-end consumer smoke test.
