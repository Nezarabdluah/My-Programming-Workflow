---
id: rules-database
description: Query design, mandatory pagination, N+1 prevention, SARGability, indexing, document-DB indexing, and resource disposal. Load for any DB, query, or performance work.
alwaysApply: false
globs: ["**/*.sql", "**/Migrations/**", "**/*Repository*", "**/Entities/**"]
requires: [REF-DB-SARG, REF-DB-COVER, REF-DB-PAG, REF-DB-N1, REF-DB-IMPLICIT, REF-DB-NOSQL, REF-DB-DISPOSE]
---

# Database Performance

> Load this file when the task concerns databases, queries, or performance.

---

## 1. Efficient Query Design

### Pagination — mandatory:
- ❌ **Never** load a full table into memory
- ✅ Use server-side pagination (LIMIT/OFFSET or cursor-based)
- ✅ Every data list = mandatory pagination

### N+1 query prevention:
- ❌ **Never** query inside a loop
- ✅ Use Eager Loading, Batch Queries, or direct Projection

### Read optimization:
- ✅ For read-only queries ← disable change tracking
- ✅ Never fetch unneeded columns — use Projection/Select

---

## 2. Indexing & Query Tuning

### SARGability rules (Search Argument Able):
- ❌ Never apply functions to columns in WHERE
  - Wrong: `WHERE YEAR(created_date) = 2023` ← Full Scan!
- ✅ Use range comparisons:
  - Right: `WHERE created_date >= '2023-01-01' AND created_date < '2024-01-01'` ← Index Seek

### Covering Indexes:
- ✅ If the query performs repeated Key Lookups ← add the required columns to INCLUDE

### Plan cache pollution prevention:
- ✅ Use parameterized queries. Never paste user input into raw SQL.

### Implicit conversion prevention:
- ❌ Never pass a data type different from the column type (e.g. NVARCHAR into a VARCHAR column)

---

## 3. Document Databases

### Strict indexing:
- ❌ Never query unindexed fields
- ✅ Design Compound Indexes by the **ESR** rule: Equality first, Sort second, Range last
- ✅ Verify with Explain that the query uses an Index Scan, not a Collection Scan

### Minimizing transferred data:
- ❌ Never fetch the whole document when you need a few fields
- ✅ Always use Projection

### Bulk writes:
- ✅ Use Bulk Write/Insert instead of individual loops

---

## 4. Resource Management

- ✅ DB connections, files, sessions ← close them immediately after use
- ✅ Use your language's resource-management pattern:
  - `using` in C# | `with` in Python | `try-with-resources` in Java | `defer` in Go
- ❌ Never leave connections open — not even on error paths
