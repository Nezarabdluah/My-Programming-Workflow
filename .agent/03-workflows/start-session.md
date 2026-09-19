# Start Session — Legacy Compatibility Workflow (AOS v8.0.0-rc.1)

> **Status:** Deprecated compatibility workflow.
> **Canonical runtime entry point:** `.agent/01-core/boot-manifest.md`
> Kept only for older integrations that still invoke `03-workflows/start-session.md`.

## Compatibility behavior

If this file is invoked:

1. Stop processing this legacy workflow.
2. Read `.agent/01-core/boot-manifest.md`.
3. Execute the boot sequence defined there exactly.
4. Load only the memory files and conditional resources required by that contract.
5. Do not restore the v7 400-line boot sequence or route through `session-prompt.md`.

The boot manifest owns session startup, proof-of-read, task classification, routing, context budget, governance, and handoff behavior.
