# End Session — Memory & Evidence Closeout (AOS v8.0-dev)

> Use when ending work or handing the project to another agent/tool.
> Runtime authority remains `01-core/boot-manifest.md`.

## 1. Update durable memory

Update only what actually changed:
- `project-context.md` — current state, stopping point, next step
- `active-tasks.md` — active/pending work and accurate states
- `decisions.md` — approved architectural decisions
- `learned-mistakes.md` — developer-corrected/new lessons
- `project-knowledge.md` / `codebase-map.md` — only when new durable knowledge was discovered

Do not turn active memory into a historical changelog; archive completed history separately when needed.

### Durable vs volatile state

Boot Memory must remain valid across branch/PR transitions.

Do **not** persist as durable memory:
- current branch name,
- pull-request state/number as the current state,
- mergeability,
- queued/in-progress CI state,
- instructions such as "merge PR next" or "run final CI next".

Query those facts live from version control when needed.

Durable memory may keep immutable evidence such as completed CI run IDs, commit SHAs, ADR IDs, and completed task states.

## 2. Verification gate

Evidence, not model claims, determines closeout quality.

Preferred evidence order:
1. CI checks
2. repository hooks
3. `python .agent/governance/runner.py`
4. manual verification only when automation is unavailable

Record:
- timestamp
- checks actually run
- exit/result status
- blockers or unsupported checks

A failed hard gate blocks a clean closeout. SKIP is not PASS.

## 3. Handoff summary

For tool-to-tool handoff, provide:
- project/task
- exact stopping point
- current task state
- next action
- material decisions/risks
- verification evidence available

## 4. Final report

Report only:
- completed work
- remaining work
- new decisions/mistakes
- verification status
- memory update status

Do not claim full compliance when required checks were not executed.
