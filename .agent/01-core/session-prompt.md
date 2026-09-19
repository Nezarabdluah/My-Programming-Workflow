# Legacy Session Prompt Compatibility Shim

> **Status:** Deprecated compatibility file for pre-v8 integrations.
> **Runtime authority:** `.agent/01-core/boot-manifest.md`
> **AOS version:** v8.0.0-rc.1

This file is intentionally not an operational contract.

Older integrations may still look for `01-core/session-prompt.md`. When they do, they MUST immediately hand off to the canonical v8 boot contract:

1. Read `.agent/01-core/boot-manifest.md`.
2. Follow its boot sequence, classification, routing, context-budget, governance, and handoff rules.
3. Do not load the legacy v7 boot sequence or mandatory full knowledge bundles from historical versions.
4. Treat ADR-006 and ADR-007 in `.agent/04-memory/decisions.md` as the approved migration direction until convergence is complete.

No new policy may be added to this compatibility shim. Runtime policy belongs in the canonical boot contract or in a deliberately scoped rule/profile/workflow.
