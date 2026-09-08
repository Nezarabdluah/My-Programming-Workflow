# Coding Standards — Stack-Agnostic Guide

> Universal coding standards derived from Clean Architecture, DDD, and production best practices.

---

## Core Principles

### SOLID (Always Enforced)
1. **Single Responsibility**: One class/module = one reason to change
2. **Open/Closed**: Open for extension, closed for modification
3. **Liskov Substitution**: Subtypes must be substitutable for base types
4. **Interface Segregation**: Many specific interfaces > one general interface
5. **Dependency Inversion**: Depend on abstractions, not concretions

### DDD (Domain-Driven Design)
- **Ubiquitous Language**: Class and method names match business terms exactly
- **Bounded Contexts**: Each module = one bounded context. No cross-context entity sharing
- **Aggregate Root**: Data modification ONLY through Aggregate Root methods
- **Reference by ID**: Aggregates reference each other by ID, not object reference
- **Value Objects**: Immutable objects representing concepts (Money, Address, Email)

---

## Entity Rules (Any Stack)

### Encapsulation
- ✅ Private/controlled setters on all properties
- ✅ Factory methods or `Create` static methods for construction
- ✅ Business methods on the entity, not on services
- ❌ Never use `ObjectMapper.Map(input, entity)` for updates — call entity methods instead
- ❌ Never allow direct property mutation from outside the entity

### Example Pattern (Pseudocode)
```
class Entity:
    private _name: string
    private _isActive: bool

    static Create(name: string) -> Entity:
        Validate(name)
        return Entity(_name: name, _isActive: true)

    Update(name: string):
        Validate(name)
        this._name = name

    Deactivate():
        this._isActive = false
```

---

## Async Everywhere

- ✅ All I/O operations (DB, API, file) MUST be asynchronous
- ❌ Never block on async methods synchronously
- ❌ Never use `.Result` or `.Wait()` (C#), `asyncio.run()` inside async (Python), `execSync` (JS)

---

## Caching Strategy

| What to Cache | TTL | Pattern |
|---------------|-----|---------|
| Lookup data (countries, roles) | 5-15 min | Cache-aside |
| Public GET endpoints | 1-5 min | Response cache |
| User-specific data | Short or none | Avoid caching |
| Mutations | Never cache | Invalidate on write |

---

## Error Handling

- ✅ Use typed exceptions / error codes — never generic "Error"
- ✅ Log at the boundary, not deep in the domain
- ✅ Return structured error responses (HTTP 4xx/5xx with error codes)
- ❌ Never swallow exceptions silently
- ❌ Never return `null` or `false` for business rule violations — throw/raise specific errors

---

## System Internals (Good to Know)

### WAL & CDC
- DB writes to Write-Ahead Log first (sequential I/O), then moves data to tables
- For data movement: use CDC (Change Data Capture) instead of periodic polling

### API Gateway Patterns
- **Rate Limiting**: Token Bucket algorithm → HTTP 429
- **Load Balancing**: Round Robin or Least Connections

---

## Testing Standards

| Test Type | What to Test | Speed | Count |
|-----------|-------------|-------|-------|
| Unit | Domain logic, Value Objects, pure functions | Fast | Most |
| Integration | API endpoints, DB queries, external services | Medium | Some |
| E2E | Full user workflows | Slow | Few critical paths |

### Test Rules
- ✅ Test behavior, not implementation
- ✅ One assertion per test (or one logical assertion)
- ✅ Use descriptive test names: "should reject order when inventory is zero"
- ❌ Never test private methods directly
- ❌ Never depend on test execution order

---

## Code Review Checklist

```
  □ SOLID principles followed?
  □ Dependency Rule respected (dependencies point inward)?
  □ Entity encapsulation maintained?
  □ All inputs validated at boundary AND in domain?
  □ Async used for all I/O operations?
  □ Error handling is typed and structured?
  □ No hardcoded secrets or credentials?
  □ Tests cover the happy path AND edge cases?
  □ No N+1 queries or missing indexes?
  □ Code follows the project's naming conventions?
```
