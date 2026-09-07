# Debug Common Errors

> General workflow for diagnosing and fixing software errors.

---

## Golden Rule: Evidence First
- ❌ Never guess the cause
- ✅ Collect evidence first, then diagnose

## ⚠️ Mandatory Resource Injection (before debugging) — MUST, gate blocked without it
0. Read `05-references/books/00-master-index.md` Stage 5 → load every MUST resource listed there
1. Inject `05-references/prompts/debugging-prompts.md`
2. Read `01-core/wiring-registry.md` → match the error type to capability row
3. Load matching constitutions:
   - DB/query error → `perf-constitution.md` (SARGable, N+1)
   - Auth/permission error → `security-constitution.md` (BOLA, IDOR)
   - Concurrency/timeout → `resilience-constitution.md` (TOCTOU, Deadlocks)
   - Architecture/DI error → `arch-constitution.md` (Dependency Rule)
4. Cite rules in fix as `// [REF-XXX]` / `// [CONST-XXX-N]` and produce a 1-line Resource Utilization Summary before Done

---

## Step 1: Reproduce the Error
1. What is the exact error message? (copy it in full)
2. When does it occur? (which action triggers it?)
3. Does it always reproduce or intermittently?
4. Did it work before? What changed?

---

## Step 2: Collect Evidence
- ✅ Read the full error message and stack trace
- ✅ Check logs (search by correlation_id if available)
- ✅ Check the Network tab (HTTP status, response size, TTFB)
- ✅ Check browser console errors
- ✅ Check DB logs if the error is data-related

---

## Step 3: Isolate the Problem
Identify the layer where the error occurs:

| Symptom | Likely layer |
|---------|--------------|
| 4xx HTTP error | API/Controller — check validation and routing |
| 5xx HTTP error | Server — check the service and DB |
| White screen / JS error | Frontend — check the console |
| Slowness without error | DB or Network — check the query plan and payload size |
| Incorrect data | Business Logic — check the domain |
| Connection timeout | Infrastructure — check connections and health |

---

## Step 4: Fix the Error
1. Identify the root cause — never just the symptoms
2. Write the fix
3. ✅ Add a test preventing recurrence
4. ✅ Build and run the tests

---

## Step 5: Document & Learn
1. Is this a recurring mistake? ← record it in `learned-mistakes.md`
2. Does it expose a gap in the rules? ← propose updating `02-rules/`
3. Update `04-memory/project-context.md`

---

## Common Error Patterns (Stack-Agnostic)

| Pattern | Usual cause | Fix |
|---------|-------------|-----|
| N+1 Queries | query inside a loop | Eager Loading / Batch |
| Memory Leak | unclosed resources | using/with/defer + Dispose |
| Race Condition | concurrent access without protection | Locks / Transactions |
| Null Reference | missing null checks | Null checks / Optional types |
| CORS Error | missing server config | add the proper CORS headers |
| 401 Unauthorized | expired or missing token | check the auth flow |
| Circular Dependency | circular import between units | restructure using interfaces |
