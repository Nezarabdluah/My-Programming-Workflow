# Init Project — AOS v8.0.0-rc.1

> Manual/fallback initialization workflow.
> **Default onboarding:** from the target project, run the public root `bootstrap.sh` or `bootstrap.ps1` one-command launcher documented in README.
> Use this file only for recovery, manual setup, or reviewing a bootstrap result marked `NEEDS_REVIEW`.

## 1. Discover the project

Inspect the target repository and record only evidence-backed facts:
- stack/package/build manifests,
- test/lint/E2E infrastructure,
- repository structure,
- existing architecture/patterns.

Do not force a predefined architecture or invent commands.

## 2. Safe runtime installation

Preferred/default path is the one-command bootstrap.

If installation must be performed manually, use the source installer:

```bash
python .agent/install.py /path/to/target-project
```

Before any write, preflight must protect:
- existing foreign/unknown `.agent`,
- `AGENTS.md`,
- `CLAUDE.md`,
- `.cursorrules`,
- GitHub Copilot instructions.

Unknown agent infrastructure is a hard stop. Do not auto-delete, rename, merge, or overwrite it.

Reusable runtime includes:
- `01-core/`, `02-rules/`, `03-workflows/`
- `05-references/`, `06-templates/`, `governance/`, `adr/`
- `profiles/technology/`
- `evidence/README.md`
- `INDEX.md`, `AGENTS.md`, `VERSION`, supported root adapters

Fresh installation must not copy source-project state:
- `04-memory/`
- `profiles/project.json`
- `task-contracts/`
- `evidence/current.json`
- `evidence/history/`

Recognized AOS upgrades preserve those project-owned paths and back up managed root adapters before refresh.

## 3. Initialize project-owned state

Create/repair target-specific:
- `.agent/profiles/project.json`
- `.agent/task-contracts/current.json`
- `.agent/04-memory/project-context.md`
- `.agent/04-memory/learned-mistakes.md`
- `.agent/04-memory/decisions.md`
- `.agent/04-memory/active-tasks.md`
- `.agent/04-memory/project-knowledge.md`
- `.agent/04-memory/codebase-map.md`

Runtime ADRs belong to `.agent/adr/system-decisions.md`; project decisions belong to project Memory.

## 4. Record project evidence

Record:
- project type/languages only from repository evidence,
- real build/test/lint/E2E commands,
- activated Technology Profiles only when applicable,
- architecture source of truth from the target codebase.

If evidence is insufficient, mark the profile `needs_review` instead of guessing.

## 5. Validate execution runtime

1. validate Project/Technology Profiles,
2. ensure the current Task Contract has at least one resolvable capability,
3. run `python .agent/01-core/execution_gate.py`,
4. confirm approval/context/check resolution,
5. run `python .agent/governance/verify.py`.

AOS-source-only README/release governance may be `SKIP_EXPECTED` in consumer projects; portable hard gates must still pass.

## 6. VERSION

Use the installed runtime version:

```yaml
aos_version: 8.0.0-rc.1
last_sync: [today]
source_path: [YOUR-LOCAL-AOS-PATH]
```

## 7. Handoff

After initialization/repair, normal operation returns to `.agent/01-core/boot-manifest.md`.

For normal onboarding, this entire workflow is orchestrated automatically by `bootstrap.py`.
