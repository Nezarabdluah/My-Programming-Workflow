# 🧠 Learned Mistakes & Lessons (Learned Mistakes - AOS v7.0)

> **Contract**: read mandatorily at session start.
> **Cap**: 20 active mistakes (newest on top — Lost-in-the-Middle resistance).
> **Pruning & escalation**: a mistake repeated 3 times escalates into a fixed rule in `02-rules/` or an automated test.

| # | Date | Type | Mistake & developer alert | Lesson & engineering fix to prevent recurrence | Repetition (max 3) |
|---|------|------|---------------------------|------------------------------------------------|--------------------|
| # | Date | Type | Mistake & developer alert | Lesson & engineering fix to prevent recurrence | Repetition (max 3) |
|---|------|------|---------------------------|------------------------------------------------|--------------------| 
| 01 | 2026-09-06 | [Type B] | CRITICAL: Delegated translation of the 2988-line books file to a subagent. The subagent wrote a 344-line summary instead of a full translation, permanently deleting lessons 2-114 (~2644 lines). No backup existed. | **FIX**: (1) NEVER delegate destructive write operations on irreplaceable files to subagents. (2) For large file rewrites: ALWAYS create a backup copy FIRST (even without git). (3) For files > 500 lines: translate in-place using replace_file_content on sections, never overwrite the entire file. (4) Verify output line count ≈ input line count BEFORE confirming success. | 1/3 |
<!-- newest always on top — add new mistakes here -->
