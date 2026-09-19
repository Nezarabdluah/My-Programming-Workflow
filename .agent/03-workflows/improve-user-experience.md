# Improve User Experience

> Workflow for improving UIs and interaction smoothness.

---

## Context Expansion (ADR-007)

Before UI changes, load only the guidance that materially applies:
1. Inspect the existing UI patterns and project conventions first.
2. Use `wiring-registry.md` to discover relevant security/API/architecture resources when needed.
3. Load frontend prompts only when they add value for the detected framework.
4. Grep targeted references for actual risks such as XSS, payload shape, accessibility, or API behavior.
5. Do not require REF/CONST comments in production UI code; record material compliance in evidence/review notes.

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
