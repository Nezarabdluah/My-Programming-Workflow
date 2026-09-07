# Improve User Experience

> Workflow for improving UIs and interaction smoothness.

---

## ⚠️ Mandatory Resource Injection (before any UI changes) — MUST, gate blocked without it
0. Read `05-references/books/00-master-index.md` Stage 4 → load every MUST resource listed there
1. Read `01-core/wiring-registry.md` → find Architecture / API rows
2. Load constitutions:
   - `arch-constitution.md` — No Logic in UI
   - `ddd-constitution.md` — UI State Ignorance (backend provides boolean flags)
   - `security-constitution.md` — XSS prevention, bypassSecurityTrust ban
   - `integration-constitution.md` — Payload Minimization, BFF pattern
3. IF Angular → inject `05-references/prompts/frontend-prompts.md`
4. Cite constitutions in code as `// [CONST-XXX-N]` and produce a 1-line Resource Utilization Summary before Done

---

## Step 1: Assess the Current State
1. What screens/pages are targeted?
2. What current problems do users face?
3. What are the most-used actions?

---

## Step 2: Interaction Improvements

### Action buttons:
- ✅ Disable the button during processing (with a loading indicator)
- ✅ Confirm before destructive operations (delete, state change)
- ✅ Clear success message after every operation
- ❌ Never disable a button without showing why

### Forms:
- ✅ Real-time validation while typing
- ✅ Error messages next to the offending field (not only at page top)
- ✅ Auto-save drafts in long forms
- ✅ Auto-focus on the first field

### Lists & tables:
- ✅ Pagination or infinite scroll for every list
- ✅ Clear search and filtering
- ✅ Clear empty state with a suggested action
- ✅ Sensible default ordering (usually newest first)

---

## Step 3: Visual Improvements

### Loading states:
- ✅ Skeleton loaders instead of blank screens
- ✅ Progress bars for long operations
- ❌ No context-free surprise spinners

### Responsive:
- ✅ Works on phone, tablet, and desktop
- ✅ Content priorities adapt to screen size
- ✅ Lists collapse into dropdown menus on small screens

### Accessibility:
- ✅ Sufficient color contrast (WCAG AA at minimum)
- ✅ Every image has alt text
- ✅ Keyboard navigation works

---

## Step 4: Verification
1. Test at different screen sizes
2. Test failure scenarios (slow network, empty data)
3. Update `04-memory/project-context.md`
