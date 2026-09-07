# Create Frontend Module

> General workflow for building a frontend UI module with any stack.

---

## ⚠️ Mandatory Resource Injection (before writing any code) — MUST, gate blocked without it
0. Read `05-references/books/00-master-index.md` Stage 4 → load every MUST resource listed there
1. Read `01-core/wiring-registry.md` → find Architecture / API rows
2. Load constitutions from `05-references/books/constitutions/`:
   - `arch-constitution.md` — No Logic in UI, DTO Mandate
   - `ddd-constitution.md` — UI State Ignorance, Frontend Parity
   - `security-constitution.md` — Angular Security Bypass Ban, XSS prevention
   - `integration-constitution.md` — BFF Pattern, Payload Minimization
3. IF Angular project → inject `05-references/prompts/frontend-prompts.md`
4. Cite constitutions in code as `// [CONST-XXX-N]` and produce a 1-line Resource Utilization Summary before Done

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
4. Identify the required State Management

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
4. ✅ Pagination for every data list

---

## Step 5: Input Validation
1. Add validation to every form
2. ✅ Show clear error messages to the user
3. ❌ Never send unvalidated data to the server

---

## Step 6: User Experience
1. ✅ Responsive design — works at every size
2. ✅ Confirmation before destructive operations (delete, state change)
3. ✅ Clear success/error messages
4. ✅ Never disable buttons without a visible reason

---

## Step 7: Verification & Delivery
1. Build the project ← zero errors
2. Test in more than one browser
3. Update `04-memory/project-context.md`
