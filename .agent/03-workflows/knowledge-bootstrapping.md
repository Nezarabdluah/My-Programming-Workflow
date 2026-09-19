# 🚀 Knowledge Bootstrapping — Knowledge Exploitation for Existing Projects & Automation Activation

> **AOS v8:** run this workflow when Stage 0 or the Navigator requests codebase discovery for an existing project. Do not run automatically on every session.

---

## 🔍 Step 1: Code Inspection & Exploration (Detective Mode)
The agent performs a quick inspection and exploration of the existing project, grounding knowledge:
1. **Architecture discovery**: inspect root files and subfolders. Identify the architecture in use (Clean Architecture, MVC, Monolith, Microservices).
2. **Write the code map**: identify the main components, files, and layers, and record them immediately in `.agent/04-memory/codebase-map.md`.
3. **Record project knowledge**: write discovered patterns, setup libraries, and data-access approaches into `.agent/04-memory/project-knowledge.md`.

---

## 🧪 Step 2: Activate & Configure Automatic Test Execution
Engineering excellence relies on evidence, not expectations. Automated tests must be activated:
1. **Find test libraries**:
   * Node.js project ← look for Jest, Vitest, or Playwright in `package.json`.
   * Python ← look for pytest or unittest.
   * .NET ← look for xUnit or NUnit.
2. **Record run commands**:
   Record the automatic run command (e.g. `npm run test`, `pytest`, or `dotnet test`) in `.agent/04-memory/project-knowledge.md` under "Automated tests".
3. **Continuous execution**:
   The agent commits to running these tests locally, automatically, and verifying full success before delivering any 🟡 medium or 🔴 sensitive task.

---

## Step 3: Automation Discovery
1. Detect existing CI, hooks, security scanning, and deployment automation.
2. Record what already exists before proposing additions.
3. Do not modify hooks/CI automatically; adding or changing repository automation requires an explicit task/plan.
4. Prefer `python .agent/governance/verify.py` for AOS verification when available.
