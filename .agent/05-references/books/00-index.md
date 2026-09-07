# 📚 Books Reference — 16 Engineering Books

> ⚠ Never read the full distilled file — use constitutions and grep only.

## Architecture (post-T013)

The books knowledge has been restructured into:

### 1. Constitutions (actionable rules — LOAD these)
| File | Rules | Topics |
|------|-------|--------|
| `constitutions/arch-constitution.md` | 15 | Clean Architecture, SDP/SAP, Systems of Systems |
| `constitutions/ddd-constitution.md` | 11 | Ubiquitous Language, Aggregates, State Pattern |
| `constitutions/security-constitution.md` | 17 | Zero Trust, XSS, BOLA, TOCTOU, Memory Safety |
| `constitutions/perf-constitution.md` | 11 | SARGable, N+1, Projections, Network Payload |
| `constitutions/resilience-constitution.md` | 15 | Concurrency, Fault Tolerance, Deadlocks, Command/Undo |
| `constitutions/integration-constitution.md` | 10 | ACL, BFF, Event-Driven Decoupling |

### 2. Resource Injection Matrix (stage mapping)
→ `00-master-index.md` — maps constitutions + all AOS resources to pipeline stages 0-8

### 3. Archive (educational content — grep only)
→ `engineering-books-16-distilled.txt` — original 16-book distillation, grep by lesson number or English keyword

### 4. Part III — Reconstructed lessons (T020, gap-fill)
→ Lessons 11–15, 21–25, 34–114 were lost in the original export; they are re-distilled inside the same file from public knowledge of the 16 books (marked `PART III — RECONSTRUCTED`), NOT the lost originals. Grep them exactly like Parts I–II.

## Source Books
1. Clean Architecture (Robert C. Martin)
2. Domain-Driven Design (Eric Evans)
3. Design Patterns (Gang of Four)
4. OWASP Testing Guide
5. The Web Application Hacker's Handbook (WAHH)
6. SQL Server Execution Plans (Grant Fritchey)
7. Expert Performance Indexing (Jason Strate)
8. Software Engineering (Ian Sommerville)
9. Wireshark 101 (Laura Chappell)
10. Object-Oriented Analysis and Design with Applications (Grady Booch)
11. UML Distilled (Martin Fowler)
12. Patterns of Enterprise Application Architecture (Martin Fowler)
13. The Pragmatic Programmer (Hunt & Thomas)
14. Refactoring (Martin Fowler)
15. Working Effectively with Legacy Code (Michael Feathers)
16. Prompt Engineering for AI (various)

## How to grep the archive:
```
grep -n "SARGable" engineering-books-16-distilled.txt
grep -n "Aggregate" engineering-books-16-distilled.txt
grep -n "OWASP" engineering-books-16-distilled.txt
```
