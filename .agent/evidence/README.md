# Evidence Bundle

`current.json` is generated evidence for the active Task Contract.

Rules:
- Never hand-author PASS/FAIL; status derives from the actual process exit code.
- Run only named checks declared in `profiles/project.json`.
- Commands execute without a shell.
- Re-running a named check replaces stale current evidence for that check.
- Archive completed evidence with `evidence_recorder.py --archive-current`.
- History archives contain the bundle plus SHA-256 integrity metadata.
- Verify archives with `--verify-archive <path>`.
- `current.json` and `history/` are generated and gitignored.
- CI publishes history as an external artifact when audit retention is useful.
