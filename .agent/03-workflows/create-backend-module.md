# Create Backend Module

> General workflow for building a complete backend module with any stack.

---

## Prerequisites
- ✅ Task classified (Simple/Medium/Sensitive)
- ✅ The relevant rules file is loaded

## ⚠️ Mandatory Resource Injection (before writing any code) — MUST, gate blocked without it
0. Read `05-references/books/00-master-index.md` Stage 4 → load every MUST resource listed there
1. Read `01-core/wiring-registry.md` → find Architecture / DDD / Database rows
2. Load constitutions from `05-references/books/constitutions/`:
   - `arch-constitution.md` — Dependency Rule, Layer Isolation, DTO Mandate
   - `ddd-constitution.md` — Aggregate Root, Repository rules, Ubiquitous Language
   - `perf-constitution.md` — SARGable queries, N+1 prevention
   - `security-constitution.md` — Mass Assignment, Validation layering
3. Load rules: `02-rules/architecture-and-design.md` → cite `REF-ARCH-*` contracts in code as `// [REF-ARCH-X]`
4. IF stack-specific plugin installed (e.g., `06-templates/dotnet-abp/`) → inject `05-references/prompts/backend-prompts.md` (generic backend generation) + `06-templates/{stack}/prompts.md` (stack-specific snippets) + follow `06-templates/{stack}/entity-pattern.md`
5. Cite constitutions in code as `// [CONST-XXX-N]` and produce a 1-line Resource Utilization Summary before Done

---

## Step 1: Requirements Analysis
1. Identify the main Entity: what is its name? Its properties?
2. Identify relationships: does it relate to other entities?
3. Identify required operations: CRUD? Custom operations?
4. Identify Business Rules: what are the invariants?
5. **State your assumptions** to the developer before starting.

---

## Step 2: Build the Domain Layer
1. Create the entity with its properties
2. Add invariants — no invalid state
3. Create Value Objects if needed
4. Declare the Repository interface
5. ✅ Verify: the Domain has zero external dependencies

---

## Step 3: Build the Application Layer
1. Create DTOs: input (Create/Update) + output (Response)
2. Create the Application Service
3. Add input validation
4. Add authorization checks
5. ✅ Verify: the service uses the interface, not the implementation

---

## Step 4: Build the Infrastructure Layer
1. Implement the repository interface
2. Set up the database (Schema/Migration)
3. Add appropriate indexes
4. ✅ Verify: pagination + indexes + no N+1

---

## Step 5: Build the Presentation Layer (API)
1. Create the Controller/Router with endpoints
2. Add error handling
3. Add documentation (Swagger/OpenAPI)
4. ✅ Verify: flat DTOs + rate limiting + validation

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
