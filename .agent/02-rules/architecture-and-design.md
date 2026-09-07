---
id: rules-architecture
description: Clean Architecture dependency rule, DDD tactical patterns, and the SOLID review checklist. Load for any work on project structure, domain modeling, or module design.
alwaysApply: false
globs: ["**/Domain/**", "**/Entities/**", "**/Aggregates/**"]
requires: [REF-ARCH-DEP, REF-ARCH-ISOL, REF-ARCH-AGGR, REF-ARCH-VO, REF-ARCH-REPO, REF-ARCH-SOLID, REF-ARCH-FACADE]
---

# Architecture & Design

> Load this file when the task concerns project structure or architectural design.

---

## 1. Clean Architecture

### The inward dependency rule:
- `Presentation / UI / APIs` depend on `Application`
- `Infrastructure / Data Access` depend on `Domain`
- `Domain` = the core. **Zero external dependencies** on databases, frameworks, or I/O libraries

### Entity isolation:
- ❌ Domain models never import: ORM, HTTP, file systems, networking
- ✅ Domain models = plain objects with no infrastructure-specific annotations

### Boundary inversion:
- ✅ If the Domain needs data ← it declares an interface
- ✅ The Infrastructure layer implements the interface — hiding SQL/NoSQL details

---

## 2. Domain-Driven Design (DDD)

### Aggregate Roots:
- Group related entities into an **Aggregate**
- Designate exactly one entity as the **Aggregate Root**
- ❌ External modification of child entities directly is forbidden
- ✅ All access goes through the Root only

### Invariant protection:
- ✅ The Root owns every business rule inside its boundary
- ❌ No state change that violates any invariant

### Value Objects:
- Properties defined purely by their values (address, money, color) = Value Objects
- ✅ **100% immutable** — to change one, create a new instance

### Domain Events:
- ✅ Raise domain events (e.g. `OrderPlacedEvent`) on state change
- ✅ Use events for cross-aggregate side effects (email, inventory) asynchronously

---

## 3. SOLID — Review Checklist

| Principle | Rule | Violation smell |
|-----------|------|-----------------|
| **S** — Single Responsibility | one reason to change per unit | unit does business logic + DB writes |
| **O** — Open/Closed | extend with new code, don't edit old | long `if/else` or `switch` on types |
| **L** — Liskov Substitution | subtypes replace base types without breakage | method throws `NotImplemented` |
| **I** — Interface Segregation | small focused interfaces | interface with 10+ methods, client uses 2 |
| **D** — Dependency Inversion | depend on abstractions, not concretions | high-level unit imports a DB unit directly |

---

## 4. General Rules

- **Library first**: before writing custom code ← check for a proven library
  - Priority: Built-in → Standard Lib → Mature OSS → Custom
- **YAGNI**: don't build what you don't need now. Easily-deletable code beats "flexible" code.
- **Composition over Inheritance**: prefer composition except in clear cases.
- **Law of Demeter**: an object talks only to its immediate neighbors. No long dot-chains.
