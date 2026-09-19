# AGENTS.md — Agent Entry Point (AOS v8.0.0-rc.1)

> Read `.agent/01-core/boot-manifest.md` and follow it exactly.
> It is the canonical runtime contract; all other resources load on demand.

1. Load the Boot Manifest and canonical memory listed by its Boot Sequence.
2. Classify the task and, for non-trivial work, maintain `.agent/task-contracts/current.json`.
3. Run `python .agent/01-core/execution_gate.py` before implementation.
4. If READY, use only broker-selected resources returned by the Execution Gate.
5. Before Done, run named verification through `.agent/01-core/evidence_recorder.py`; full verification is `governance_verify`.
6. Never fabricate evidence or write outside the local project.
