# Init Project — AOS v8.0-dev

> One-time workflow for linking a software project to AOS.
> Runtime authority after initialization: `.agent/01-core/boot-manifest.md`.

## 1. Discover the project

Inspect the repository to identify:
- stack and package/build manifests,
- test infrastructure,
- repository state,
- existing architecture/patterns.

Do not force a predefined architecture.

## 2. Install the AOS runtime

Copy the current AOS runtime structure into the project's `.agent/` directory, including:
- `01-core/`
- `02-rules/`
- `03-workflows/`
- `05-references/`
- `06-templates/`
- `governance/`
- `adr/`
- `INDEX.md`
- `AGENTS.md`
- `VERSION`

Do not treat legacy compatibility files as canonical runtime policy.

## 3. Initialize project memory

Create `.agent/04-memory/` with:
- `project-context.md`
- `learned-mistakes.md`
- `decisions.md`
- `active-tasks.md`
- `project-knowledge.md`
- `codebase-map.md`
- `mistakes-archive.md`

Initialize only truthful current state. Do not pre-mark work as Approved or Done.

## 4. Record project knowledge

For an existing project:
- map key folders/components,
- detect test/build/lint/E2E commands,
- record established conventions,
- record architecture only from evidence in the codebase.

Technology Profiles and Project Profile support are Sprint 2 work; do not fabricate them if they are absent.

## 5. Write VERSION

Use the current source version:

```yaml
aos_version: 8.0.0-dev
last_sync: [today]
source_path: [YOUR-LOCAL-AOS-PATH]
```

## 6. Verify initialization

Run available AOS governance checks and verify required runtime files exist.

Then hand off to `01-core/boot-manifest.md` for normal operation.
