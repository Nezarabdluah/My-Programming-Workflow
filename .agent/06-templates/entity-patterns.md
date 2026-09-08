# Entity / Model Patterns — Stack-Agnostic Guide

> Universal patterns for designing entities, models, and frontend components in any stack.

---

## Quick Entity Schema (YAML Notation)

```yaml
EntityName:
  id: UUID/Guid
  name: string (max 300)
  nameAr: string (max 300)
  isActive: boolean
  createdAt: datetime
  updatedAt: datetime
  Relations:
    - BelongsTo: ParentEntity
    - HasMany: ChildEntity
```

---

## Layered Architecture Flow

```text
Presentation Layer (API / Frontend)
    ↓
Application Layer (Use Cases, Commands, Queries)
    ↓
Domain Layer (Entities, Value Objects, Domain Events, Repository Interfaces)
    ↑
Infrastructure Layer (DbContext/ORM, External APIs, Repository Implementations)
```

**Dependency Rule**: Dependencies MUST always point inwards. Outer layers depend on inner layers, never the reverse.

---

## Entity Design Rules (Any Stack)

### 1. Encapsulation
- Properties MUST have controlled access (private setters, readonly fields, or immutability)
- Never expose mutable internal state directly
- Use factory methods or constructors for creation

### 2. Validation
- Validate at the boundary (DTOs/API input) AND in the domain (business rules)
- Never trust frontend input — treat all inputs as potentially malicious
- Use your framework's validation mechanism (FluentValidation, Zod, Pydantic, etc.)

### 3. Identity
- Use UUID/Guid for primary keys in distributed systems
- Use sequential IDs only when performance requires it and distribution is not a concern

### 4. Audit Trail
- Track createdAt, updatedAt, createdBy, updatedBy
- Consider soft delete (isDeleted flag) vs hard delete based on compliance needs

---

## Frontend Component Patterns (Any Framework)

### List Component
```
Properties:
  - items: Array<Entity>
  - filterText: string
  - sorting: string
  - pagination: { skip, take, total }

Methods:
  - ngOnInit / mounted: load items
  - getItems(): fetch with pagination + filter + sort
  - create(): open form modal
  - edit(item): open form modal with data
  - delete(item): confirm + delete
  - pageChanged(event): update pagination
```

### Form Component
```
Properties:
  - id: string | null
  - item: Entity
  - saving: boolean

Methods:
  - ngOnInit / mounted: if id exists, load item
  - save(): create or update
  - close(): close modal/dialog
```

### Frontend Best Practices
- Always use `trackBy` / `key` in list rendering
- Use change detection strategy (OnPush, React.memo, etc.)
- Server-side filtering for large datasets — never filter large arrays in the browser
- Handle loading, error, and empty states explicitly

---

## Localization Pattern

```json
{
  "Create": "Create",
  "Edit": "Edit",
  "Delete": "Delete",
  "Save": "Save",
  "Cancel": "Cancel",
  "Confirm": "Are you sure?"
}
```
> Keys stay in English. Values adapt to your app's locale (Arabic, French, etc.).

---

## Domain Events vs Integration Events

| Type | Scope | Use Case |
|------|-------|----------|
| **Domain Event** | Within a single Bounded Context | "OrderCreated" → update inventory in same module |
| **Integration Event** | Across Bounded Contexts / Microservices | "OrderCompleted" → send email, update analytics |

---

## Value Objects

- MUST be immutable
- Use language-native immutability features:
  - TypeScript/JavaScript: `readonly` properties or `Object.freeze`
  - C#: `record struct` or `readonly struct`
  - Python: `dataclass(frozen=True)` or `NamedTuple`
  - Go: struct with no exported mutable fields
  - Rust: struct with no `&mut` references

---

## Repository Pattern

- Define repository INTERFACE in the Domain layer
- Implement repository in the Infrastructure layer
- Never inject database context/ORM directly into Application Services
- One repository per Aggregate Root — never per child entity
