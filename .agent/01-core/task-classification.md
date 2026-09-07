# Task Classification

At the start of every task, you **must** classify it and print:
`[Mode: 🟢 Simple | 🟡 Medium | 🔴 Sensitive]`

---

## 🟢 Simple Mode (Level 1)
**Indicators**: CSS/HTML edits, UI layouts, `.md` files, simple single-file bug fixes.
**Keywords**: "style", "rename", "typo", "doc", "UI alignment", "bug fix".
**Scope**: ≤ 2 files, zero system impact.
**Required**: the operational contract only. No tests, no reports.

---

## 🟡 Medium Mode (Level 2)
**Indicators**: business logic, adding API endpoints, refactoring multiple files.
**Keywords**: "endpoint", "controller", "refactor", "service", "utility".
**Scope**: 3-5 files, localized impact on one component.
**Required**: contract + build + tests. No reports, no ADR.

---

## 🔴 Sensitive Mode (Level 3)
**Indicators**: database changes, authentication, security, core architecture.
**Keywords**: "authentication", "security", "database schema", "indexing", "architecture", "payment", "authorization", "JWT".
**Scope**: > 5 files, or any change touching the core DB or auth.
**Required**: full compliance — rules + build + tests + security gate + report.

---

## ⚠️ Zero-Trust Rule
If you are ever unsure about the classification — **always treat the task as Sensitive**.

## Quick Decision Matrix
| Question | Yes → |
|----------|-------|
| Does it touch security, auth, or permissions? | 🔴 Sensitive |
| Does it modify the database schema? | 🔴 Sensitive |
| Does it affect more than 5 files? | 🔴 Sensitive |
| Does it add new business logic or an API? | 🟡 Medium |
| Is it purely visual or documentation-only? | 🟢 Simple |
