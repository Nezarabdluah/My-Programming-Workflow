# Backend Prompts — General Backend Prompts

> Ready-to-use prompts for any backend stack.

---

## 1. Full CRUD creation
```
Create full CRUD for entity [Name] with the following properties: [property list]

Required:
- Domain layer: Entity + Invariants + Repository Interface
- Application layer: DTOs + Application Service + Input Validation
- Infrastructure layer: Repository Implementation + Migration
- API layer: Controller + Endpoints + Error Handling
- Tests: Unit Tests for the domain + Integration Tests for the API

Comply with: Clean Architecture + SOLID + mandatory pagination
```

## 2. Query performance tuning
```
This query is slow: [the query]

Analyze:
1. Does it contain an N+1 query?
2. Does it need a new index?
3. Is the filtering SARGable?
4. Does it fetch unneeded columns?

Provide the fix with the root-cause explanation.
```

## 3. Security review
```
Review this code from a security perspective:
[code]

Check for: SQL Injection, XSS, IDOR, exposed secrets, exposed stack traces
```

## 4. Adding error handling
```
Add comprehensive error handling to this code: [code]

Required:
- Generic messages for users (no technical details)
- Detailed logging with correlation_id
- Proper HTTP status codes (400, 401, 403, 404, 500)
- Retry + Circuit Breaker for outbound calls
```

## 5. Writing tests
```
Write tests for this code: [code]

- Unit Tests: domain behavior + edge cases
- Integration Tests: the API endpoints
- AAA structure: Arrange, Act, Assert
- Name tests with clear descriptions
```
