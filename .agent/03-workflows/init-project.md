# 🚀 Init Project — New Project Initialization (AOS v7.0)

> **Contract**: used once only when linking a new project to AOS.
> **Main source**: `[YOUR-LOCAL-AOS-PATH]`

---

## 🔍 Step 1: Technology Discovery
Inspect the project root and discovered files:
* `package.json` ← Node.js / React / Next.js
* `requirements.txt` or `pyproject.toml` ← Python
* `csproj` or `sln` ← .NET / C#
* Otherwise ← General Stack

---

## 📂 Step 2: Copy the Main AOS v7.0 Structure
Copy the following folders and files from the absolute main source into the new project's `.agent/` folder:
1. `01-core/` in full (operating-contract.md, session-prompt.md, and supporting files).
2. `02-rules/` in full (the six specialized rule files).
3. `03-workflows/` in full (init-project.md, start-session.md, end-session.md, requirements-analysis.md, etc.).
4. `05-references/` in full (engineering-rules-catalog-REF.md + books/ + qa-testing/ + devops-ops/ + prompts/).
5. `governance/` in full (runner.py + tests) + `adr/` + `06-templates/` when available.
6. Root files: `INDEX.md` + `AGENTS.md` + `VERSION`.

---

## 💾 Step 3: Create the Cumulative Memory Module (04-memory/)
Create the `.agent/04-memory/` folder locally in the new project and initialize it with these default files:
* `project-context.md` ← write into it: "Init date: [today's date] | Project state: initial setup".
* `learned-mistakes.md` ← empty table with the approved column headers.
* `decisions.md` ← empty template of the approved ADR format.
* `active-tasks.md` ← initialized with state `Approved` and the initial linking/setup tasks.
* `project-knowledge.md` ← empty, for discovered patterns.
* `codebase-map.md` ← records the currently discovered file structure.
* `mistakes-archive.md` ← empty, for historical mistakes.

---

## 🔄 Step 4: Write the VERSION File
Create `.agent/VERSION` in the new project with this content:
```yaml
aos_version: 7.0.0
last_sync: [today's date]
source_path: [YOUR-LOCAL-AOS-PATH]
```

---

## 📝 Step 5: Project Init Report
Print the formatted initialization report to notify the developer of readiness:

   ✅ Project initialized successfully for AOS v7.0
   📋 Detected stack: [stack name]
   🧠 Contextual memory: 04-memory/ folder created and all 7 files initialized successfully.
   🔄 Version: 7.0.0 (in sync with the main source)
   🎯 Ready to start — please assign the first task!
