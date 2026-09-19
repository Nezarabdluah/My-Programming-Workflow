# AOS Runtime System Decisions

> Bundled runtime decisions required by executable AOS policy. Project-specific ADRs belong in `.agent/04-memory/decisions.md`.

## ADR-006: Vertical Slice is profile-scoped
**Status**: Approved
**Context:** A universal seven-layer web slice made Core architecture-specific.
**Decision:** Keep Vertical Slice guidance optional and activate it only through project/technology profile evidence.
**Consequences:** Core remains architecture-neutral while full-stack projects can opt into the guidance.

## ADR-007: References and knowledge load on demand
**Status**: Approved
**Context:** Preloading all references inflated context and duplicated policy.
**Decision:** Load only task-relevant rules/references selected by executable routing.
**Consequences:** Lower context cost, less drift, and clearer evidence of what informed a task.

## ADR-008: Deterministic Context Broker
**Status**: Approved
**Context:** Manual resource selection was not reliably auditable.
**Decision:** Resolve task capabilities against Project/Technology Profiles and the executable Context Map.
**Consequences:** Context selection is deterministic, profile-gated, and machine-testable.


## ADR-009: Policy-based approvals and executable evidence
**Status**: Approved
**Context:** Free-text approval and prose-only verification are not deterministic enough for governed execution.
**Decision:** Use structured approval provenance plus executable Evidence Bundle semantics with PASS/FAIL derived from process exit code.
**Consequences:** Approval and verification are auditable, machine-testable, and portable across consumer projects.
