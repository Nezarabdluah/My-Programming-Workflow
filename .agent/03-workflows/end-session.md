# 🚪 End Session — Session End & Memory Save Protocol (AOS v7.0)

> **Contract**: executed when the developer asks to end the session or to move work to another AI tool.

---

## 💾 Step 1: Comprehensive Local Memory Update
Update every memory file in `.agent/04-memory/` to match exactly what was accomplished:
1. `project-context.md` ← document: the last completed task, the pending task, and any critical technical notes.
2. `active-tasks.md` ← set SDD states precisely for features, and mark completed tasks `[x]` and pending tasks `[ ]`.
3. `decisions.md` ← record any approved architectural decisions (ADRs).
4. `learned-mistakes.md` ← add any new mistakes the developer corrected you on.
5. `project-knowledge.md` & `codebase-map.md` ← document any new patterns or folder structures created.

---

## 🔒 Step 1.5: Governance Enforcement Gate (pre-Done)

> **GOV-T11**: the agent must never claim compliance — only **actual evidence** (exit codes, timestamped report files, tool output) counts as proof.

### Graduated Enforcement Levels

Declare the enforcement level for this session using the tag below:

| Level | Tag | Meaning |
|-------|-----|---------|
| CI pipeline ran | `[Enforcement: CI ✅]` | Automated CI/CD ran and passed — highest confidence |
| Git hooks fired | `[Enforcement: hooks ⚠️]` | Pre-commit/pre-push hooks ran — good confidence |
| runner.py executed | `[Enforcement: runner.py 🔶]` | Governance runner ran locally — acceptable confidence |
| Manual checklist | `[Enforcement: manual 🔶]` | No automation — lowest acceptable confidence |
| Model claim only | `[Enforcement: claim ❌]` | **REJECTED** — never accepted as proof |

### Execution Steps

```
□ If governance/runner.py is available and the project has Python:
  1. Run: python .agent/governance/runner.py
  2. Record the exit code and output
  3. If exit code ≠ 0 → ⛔ GATE FAILED — fix issues before closing session
  4. If exit code = 0 → ✅ GATE PASSED — proceed to Step 2

□ If runner.py is not available or Python is not installed:
  1. Run the manual governance checklist:
     - [ ] All memory files updated (project-context, active-tasks, decisions, learned-mistakes)
     - [ ] No version conflicts (VERSION matches all file headers)
     - [ ] No orphaned legacy paths
     - [ ] Active tasks accurately reflect current state
  2. Tag as [Enforcement: manual 🔶]
  3. Proceed to Step 2

□ Report format (GOV-T11 — actual evidence required):
  - Timestamp: [ISO 8601]
  - Tool: runner.py | manual checklist
  - Exit code: [0 | N]
  - Output: [paste actual tool output, not a summary]
  - Enforcement level: [tag from table above]
```

## 🔄 Step 2: Handoff Summary
If the session ends for the purpose of moving to another tool, draft and print a formatted handoff summary to copy:

```text
🔄 Handoff Summary for AOS v7.0
📋 Project: [project name] | Stack: [type]
📍 Last stopping point: [describe precisely where work stopped and the last file opened]
📌 Next step: [what the next agent must start with immediately]
⚠️ Critical alerts: [any architectural decisions or learned mistakes that must be respected]
💾 Memory fully updated locally and ready for import ✅.
```

---

## 📝 Step 3: Final Session Report
Print the approved final report to close the session properly:
   📋 Session summary:
   ✅ Completed tasks: [list]
   ⏳ Pending tasks: [list — saved in active-tasks.md]
   📝 New mistakes recorded: [count]
   💾 Memory: all files updated and saved locally ✅
   👋 Session closed successfully.
