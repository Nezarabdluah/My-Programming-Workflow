# Create Backend Module

> Layered-backend workflow. Use only when the existing project/profile has comparable business/use-case/persistence/API areas; otherwise adapt to the project's established architecture.

---

## Prerequisites
- ✅ Task classified (Simple/Medium/Sensitive)
- ✅ The relevant rules file is loaded

## Context Expansion (ADR-007)

Before implementation:
1. Inspect the project's existing backend architecture and conventions.
2. Use `wiring-registry.md` to discover only resources relevant to the task.
3. Load architecture/DDD guidance only if the project actually uses those patterns.
4. Load DB/security/API rules only when those capabilities are affected.
5. Use templates/prompts as optional accelerators, not mandatory architecture.
6. Record material compliance in evidence/review notes; source REF/CONST comments are optional.

---

## Step 1: Requirements Analysis
1. Identify the use case/business capability and affected data/contracts.
2. Identify the project components/boundaries involved.
3. Identify required operations and behavior.
4. Identify business rules/invariants when the project has a domain model.
5. **State your assumptions** to the developer before starting.

---

## Step 2: Implement the Project's Business/Domain Area
1. Create the entity with its properties
2. Add invariants — no invalid state
3. Create Value Objects if needed
4. Use repository abstractions only when they match the project's architecture
5. Verify dependencies against the project's established boundaries

---

## Step 3: Implement the Use-Case/Application Area
1. Create DTOs: input (Create/Update) + output (Response)
2. Create the Application Service
3. Add input validation
4. Add authorization checks
5. Verify the implementation follows the project's dependency conventions

---

## Step 4: Implement Persistence/Infrastructure (when applicable)
1. Follow the project's established persistence abstraction.
2. Change schema/migrations only when required.
3. Add/query indexes based on actual access patterns when relevant.
4. Verify query behavior/performance issues relevant to the change.

---

## Step 5: Implement the External/API Boundary (when applicable)
1. Follow the project's existing endpoint/handler pattern.
2. Add appropriate authorization, validation, and error behavior.
3. Update API documentation when the project uses it.
4. Verify the external contract and affected security boundaries.

---

## Step 6: Tests
1. Write Unit Tests for domain logic
2. Write Integration Tests for the API
3. Run all tests ← zero failures

---

## Step 7: Verification & Delivery
1. Build the project ← zero errors
2. Run the tests ← all pass
3. Review `02-rules/testing-and-quality.md` → the checklist
4. Update `04-memory/project-context.md`
