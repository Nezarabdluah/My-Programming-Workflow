# 🔄 Start Session — Session Start Protocol (AOS v7.0)

> **⚠️ LEGACY FILE**: This file is superseded by `01-core/session-prompt.md` which contains the full boot protocol inline. Kept for backward compatibility only. Do not load directly — use session-prompt.md instead.

> **Contract**: executed mandatorily at the start of every work session to guarantee context continuity and safe version sync.

---

## 🔍 Step 0: Sync Check
1. Read the project's `.agent/VERSION` file.
2. Compare the `aos_version` and `source_path` against the main source.
3. If the versions differ, alert the developer:
   > "⚠️ An AOS governance update exists (source version: [X] | current project version: [Y]). Do you want to update the locally-untouched files?"
4. Follow the developer's decision — **never auto-update without approval**.

---

## 🧠 Step 1: Memory Read & Context Load
Read the mandatory files in this order (reading budget ≤ 400 lines):
1. `.agent/INDEX.md` ← the index for file routing.
2. `.agent/01-core/operating-contract.md` ← the governance contract and agent behavior.
3. `.agent/04-memory/project-context.md` ← the last project state and active stopping points.
4. `.agent/04-memory/learned-mistakes.md` ← read and immediately avoid the learned mistakes.
5. `.agent/04-memory/active-tasks.md` ← read active tasks and the current SDD state.

---

## 🔄 Step 2: Handoff Detection & Reception
Check task state in `04-memory/active-tasks.md` and `04-memory/project-context.md`:
* **Are there active tasks in `Executing` or `Planning` state handed over from another tool?**
  * **Yes**: present them to the developer immediately and say:
    > "I found a pending session handed over from the previous tool: [feature / running task] in state [current state]. I will resume from the documented stopping point: [stopping point]. Shall we continue from here, or do you have a new task?"
  * **No**: wait for the developer to direct you to the next task.

---

## 📝 Step 3: Readiness Report & Proof of Read
Print the formatted report to the developer (as documented in `session-prompt.md`) as proof of complete, successful memory reading and the start of work.
