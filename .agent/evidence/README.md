# Evidence Bundle

`current.json` is generated evidence for the active Task Contract.

Rules:
- Do not hand-author PASS/FAIL.
- Run named checks through `01-core/evidence_recorder.py`.
- Status is derived from process exit code.
- Commands come only from `profiles/project.json`.
- Keep transient command output out of the bundle; store durable metadata only.
- Before starting a new task, archive evidence when it is useful for audit/history or let the new task replace the current bundle.
