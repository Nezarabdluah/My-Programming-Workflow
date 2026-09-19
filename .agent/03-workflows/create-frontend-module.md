# Create Frontend Module

> Frontend UI workflow. Adapt steps to the detected framework, design system, application type, and existing project conventions.

---

## Context Expansion (ADR-007)

Before implementation:
1. Inspect the existing frontend framework, design system, state patterns, and project conventions.
2. Use `wiring-registry.md` to discover only relevant resources.
3. Load security/API guidance for actual risks such as XSS, authorization-driven UI state, or payload design.
4. Load framework prompts only when they materially help.
5. Do not require production-code REF/CONST comments; record material evidence in review notes.

---

## Step 1: Requirements Analysis
1. What pages/screens are required?
2. What data does each screen display?
3. What actions are available to the user?
4. Are there input forms?
5. **State your assumptions** to the developer.

---

## Step 2: Component Structure
1. Design the Component Tree
2. Identify reusable components
3. Identify each component's data sources (API endpoints)
4. Identify whether local/shared/server state management is actually required

---

## Step 3: Build Components
1. Build components bottom-up (smallest first)
2. One component = one responsibility
3. ✅ Use clear intent-revealing names
4. ❌ No business logic in components — put it in services

---

## Step 4: Data Binding
1. Bind each component to the right API
2. Add loading states
3. Add user-facing error handling
4. Use pagination/virtualization/infinite loading when dataset size or project conventions justify it

---

## Step 5: Input Validation
1. Add validation to every form
2. ✅ Show clear error messages to the user
3. ❌ Never send unvalidated data to the server

---

## Step 6: User Experience
1. Verify the target responsive breakpoints/devices defined by the product
2. ✅ Confirmation before destructive operations (delete, state change)
3. ✅ Clear success/error messages
4. ✅ Never disable buttons without a visible reason

---

## Step 7: Verification & Delivery
1. Build the project ← zero errors
2. Test the browser/device matrix required by the project when applicable
3. Update `04-memory/project-context.md`
