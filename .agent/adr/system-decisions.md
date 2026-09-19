# AOS Runtime System Decisions

> Bundled runtime decisions required by executable AOS policy. Project-specific ADRs belong in `.agent/04-memory/decisions.md`.

## ADR-006: Vertical Slice is profile-scoped
**Context:** A universal seven-layer web slice made Core architecture-specific.
**Decision:** Keep Vertical Slice guidance optional and activate it only through project/technology profile evidence.
**Consequences:** Core remains architecture-neutral while full-stack projects can opt into the guidance.

## ADR-007: References and knowledge load on demand
**Context:** Preloading all references inflated context and duplicated policy.
**Decision:** Load only task-relevant rules/references selected by executable routing.
**Consequences:** Lower context cost, less drift, and clearer evidence of what informed a task.

## ADR-008: Deterministic Context Broker
**Context:** Manual resource selection was not reliably auditable.
**Decision:** Resolve task capabilities against Project/Technology Profiles and the executable Context Map.
**Consequences:** Context selection is deterministic, profile-gated, and machine-testable.
