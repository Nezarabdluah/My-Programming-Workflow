---
id: core-token-budget
description: Token budget policy and selective loading rules. Load when planning session reading or when context usage approaches limits.
alwaysApply: false
globs: []
requires: [REF-AI-CONTRACT]
---

# Token Budget — Token Policy & Selective Loading

---

## Total ceiling: ≤ 400 lines of reading per session

### Always loaded (permanent, keep lean):
| File | Size class |
|------|-----------|
| `AGENTS.md` | Light |
| `01-core/operating-contract.md` | Medium |
| `04-memory/project-context.md` | Light (grows with use — keep it pruned) |
| `04-memory/learned-mistakes.md` | Light (max 20 active mistakes) |
| `VERSION` | Tiny |

> Size classes: **Tiny** ≤ 10 lines · **Light** ≤ 60 · **Medium** ≤ 120 · **Heavy** = grep-only. Exact line counts drift — treat classes, not numbers, as the contract.

### Loaded per task (ONE file at a time from each):
| Type | Size class |
|------|-----------|
| One rules file from `02-rules/` | Light–Medium |
| One workflow file from `03-workflows/` (or one step file of a sub-workflow) | Light–Medium |

### Never auto-loaded:
- `05-references/*` ← grep only (resolve anchors via `01-core/wiring-registry.md`)
- `06-templates/*` ← only during project initialization
- `04-memory/mistakes-archive.md` ← archive only
- `04-memory/project-knowledge.md`, `codebase-map.md` ← on demand
- `04-memory/decisions.md`, `active-tasks.md` ← on demand / conditional per AGENTS.md

---

## Token efficiency rules
1. **No repo dumping**: never read the whole project. Grep first, then read the identified file.
2. **Targeted reading**: use line ranges. Never read a full file when a function-level check suffices.
3. **Differential updates**: output only the changes (diff-style). Never rewrite whole files without need.
4. **70% warning**: when context reaches 70% of the model limit ← warn the developer and propose summarizing progress into memory.
5. **References guard**: never read `05-references/books/` in full — grep only [REF-AI-CONTRACT].
