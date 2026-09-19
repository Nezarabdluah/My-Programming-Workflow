# Agent Operating System (AOS v8.0.0-rc.1)

Read `.agent/01-core/boot-manifest.md` first. It is the canonical runtime contract.

## Boot
Load only the Boot Manifest plus the memory files listed in its Boot Sequence. Do not preload INDEX, workflows, rules, profiles, or references.

## Non-trivial tasks
1. Maintain `.agent/task-contracts/current.json`.
2. Run `python .agent/01-core/execution_gate.py`.
3. Stop if mode is `HUMAN_REQUIRED`.
4. For `HUMAN_APPROVED` or `AUTO_EXECUTE`, use only returned broker resources and named verification checks.

## Governance & Evidence
Before Done, run named checks through `.agent/01-core/evidence_recorder.py`.
Use `governance_verify` for full governance + mutation verification.
PASS/FAIL must come from executable evidence.

## Source protection
Consumer mode must not modify upstream AOS. AOS self-development must use a non-main branch and green final verification before merge.

## Memory
Keep Boot Memory durable and merge-safe. Query branch/PR/mergeability/queued-CI state live instead of persisting it.
