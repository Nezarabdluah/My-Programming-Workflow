# THE 16 BOOKS REFERENCE CATALOG (ENGINEERING CONSTITUTION DIRECTIVES)

This catalog contains the synthesized directives extracted from the 16 core software engineering, architecture, database, security, and networking books. 

When modifying code, the agent MUST explicitly cite compliance with the relevant `[REF-...]` tag in its thinking or explanations.

---

## 1. 🏛️ ARCHITECTURE, OOP & DOMAIN DESIGN (Clean Architecture, DDD, GoF Patterns)

### `[REF-ARCH-DEP]`: Inward Dependency Flow
- **Source**: *Clean Architecture* (Robert C. Martin)
- **Directive**: Source code dependencies must point only inward toward high-level policies. Inner circles (Domain, Application) must not know anything about outer circles (UI, Web, Databases, Frameworks).

### `[REF-ARCH-ISOL]`: Domain Isolation (Pure Domain Models)
- **Source**: *Domain-Driven Design* (Eric Evans)
- **Directive**: Domain entities must be Plain Objects (POCOs/POJOs/dataclasses). They are forbidden from importing ORM frameworks (like Entity Framework, SQLAlchemy) or Web controllers. Database-specific or framework-specific annotations must not leak into core Domain classes.

### `[REF-ARCH-AGGR]`: Aggregate Boundaries & Invariant Protection
- **Source**: *Domain-Driven Design* (Eric Evans)
- **Directive**: Define clear Aggregate Roots. External objects must only hold references to the Aggregate Root by ID (e.g. `CategoryId`), never to internal child entities. The Aggregate Root is solely responsible for validating all business rules (invariants) and is the sole entry point for modifications.

### `[REF-ARCH-VO]`: Immutable Value Objects
- **Source**: *Domain-Driven Design* (Eric Evans) / *The Object-Oriented Thought Process*
- **Directive**: Entities that have no identity but are defined by their values (e.g., Address, Money) must be Value Objects. Value Objects must be 100% immutable. Create a new instance instead of modifying fields of an existing instance.

### `[REF-ARCH-REPO]`: Repository Abstraction
- **Source**: *Domain-Driven Design* (Eric Evans)
- **Directive**: Use the Repository pattern to simulate an in-memory collection of Aggregate Roots. Never inject database contexts directly into Application Services or Domain logic. The Domain dictates what it needs using interfaces, and the Infrastructure implements it.

### `[REF-ARCH-SOLID]`: SOLID Principles Compliance
- **Source**: *Clean Architecture* (Robert C. Martin) / *Software Engineering* (Ian Sommerville)
- **Directive**: Enforce SRP (one reason to change), OCP (extend via new classes, close existing for edits), LSP (subtypes substitutable without throwing `NotImplementedException`), ISP (small cohesive interfaces), and DIP (inject interfaces, not concretions).

### `[REF-ARCH-FACADE]`: Facade Pattern for Use Cases
- **Source**: *Design Patterns: Elements of Reusable Object-Oriented Software* (GoF)
- **Directive**: Treat Application Services (or FastAPI routers/C# AppServices) as Facades. They coordinate tasks (fetch DTOs, call Domain Managers, save database), but must not contain core business logic, calculations, or policies.

---

## 2. 🛢️ DATABASE PERFORMANCE & QUERY TUNING (SQL Server, PostgreSQL, MongoDB)

### `[REF-DB-SARG]`: SARGable Queries & Index Seek Enforcement
- **Source**: *SQL Server Execution Plans* (Grant Fritchey) / *SQL Server Query Performance Tuning*
- **Directive**: Write queries so they are Search Argument Able (SARGable) to trigger **Index Seeks** rather than full Table/Index Scans.
  - ❌ NEVER apply functions or operations to columns in filters: `WHERE YEAR(CreatedDate) = 2023`.
  - ✅ Use range comparisons instead: `WHERE CreatedDate >= '2023-01-01' AND CreatedDate < '2024-01-01'`.

### `[REF-DB-COVER]`: Covering Indexes & Key Lookup Prevention
- **Source**: *Expert Performance Indexing in Azure SQL and SQL Server* (Edward Pollack)
- **Directive**: Design indexes to cover query outputs. Avoid expensive **Key Lookups** / **RID Lookups** in relational execution plans by ensuring that columns present in the `SELECT` clause but missing from the index key are added to the index's `INCLUDE` clause.

### `[REF-DB-PAG]`: Server-Side Pagination
- **Source**: *SQL Server Query Performance Tuning*
- **Directive**: Always perform pagination at the database server level (`Skip`/`Take` or `LIMIT`/`OFFSET`). Never load an entire dataset into memory to filter or paginate in the application code.

### `[REF-DB-N1]`: N+1 Query Prevention
- **Source**: *SQL Server Execution Plans* (Grant Fritchey)
- **Directive**: Prevent N+1 queries. Never execute a query inside a loop. Use Eager Loading (`Include` / `joinedload` / `selectinload`) or select only required properties via projection (`.Select()`) to fetch data in a single round-trip.

### `[REF-DB-IMPLICIT]`: Implicit Conversion Prevention
- **Source**: *SQL Server Execution Plans* (Grant Fritchey)
- **Directive**: Prevent implicit conversions that cause index scans. Ensure the data types of variables passed to the database match the database column types exactly (e.g., do not pass `NVARCHAR` parameters to `VARCHAR` columns).

### `[REF-DB-NOSQL]`: Compound Indexing (MongoDB)
- **Source**: *NoSQL Databases Best Practices*
- **Directive**: For MongoDB, construct compound indexes following the Equality, Sort, Range (ESR) rule. Ensure all query fields are covered, and verify execution stats show `IXSCAN` and zero `COLLSCAN`.

### `[REF-DB-DISPOSE]`: Resource Disposal Protocol
- **Source**: *Clean Architecture* (Robert C. Martin)
- **Directive**: Always dispose of database connections, transactional sessions, streams, and file handles using language-native managers (`with` in Python, `using` in C#).

---

## 3. 🔐 APPLICATION SECURITY & WEB HACKING DEFENSE (OWASP, WAHH)

### `[REF-SEC-JWT]`: Secure Cookie Session Management
- **Source**: *The Web Application Hacker's Handbook*
- **Directive**: Never store JWTs or session IDs in `localStorage` or `sessionStorage` due to XSS vulnerability. Always store tokens in **`HttpOnly`**, **`Secure`**, and **`SameSite=Strict`** cookies.

### `[REF-SEC-IDOR]`: Insecure Direct Object Reference Defense
- **Source**: *OWASP Testing Guide*
- **Directive**: Enforce ownership checking for every resource retrieval/modification. Verify that the requested resource ID belongs to the authenticated user ID parsed from the secure session:
  - `SELECT * FROM Orders WHERE Id = :id AND OwnerUserId = :session_user_id`

### `[REF-SEC-VALID]`: Double-Boundary Validation
- **Source**: *The Web Application Hacker's Handbook*
- **Directive**: Implement validation at both the API/request boundary (DTO schemas, Pydantic models) to reject malformed requests early, AND inside the Domain entities to protect domain integrity.

### `[REF-SEC-XSS]`: XSS Output Encoding & Safe Render
- **Source**: *OWASP Testing Guide*
- **Directive**: Prevent XSS by using framework-native safe text bindings (`textContent`, `{{}}`). Never use unsafe APIs with raw user input (`innerHTML`, `dangerouslySetInnerHTML`, `bypassSecurityTrustHtml`, or `eval()`).

### `[REF-SEC-INJECT]`: Injection Sanitization & Whitelisting
- **Source**: *The Web Application Hacker's Handbook*
- **Directive**: Prevent SQL/NoSQL/Command injection. Use query parameterization. If dynamic sorting columns, operators, or tables are required, validate them against a strict static whitelist in code; reject anything else.

---

## 4. 🧪 TESTING, OBSERVABILITY & RESILIENCE (Software Engineering)

### `[REF-TEST-BEHAV]`: Behavior-Driven Testing
- **Source**: *Software Engineering* (Ian Sommerville)
- **Directive**: Write tests that verify behavior and outputs for a given input, not implementation details. A pure refactoring (changing the code structure without modifying behavior) must not break tests.

### `[REF-TEST-MOCK]`: Mocking Isolation
- **Source**: *Software Engineering* (Ian Sommerville)
- **Directive**: Mock only external, non-deterministic dependencies (I/O, database, third-party REST APIs). Do not mock your own domain entities, calculations, or internal helper classes.

### `[REF-OBS-LOG]`: Structured Logging
- **Source**: *Software Engineering* (Ian Sommerville)
- **Directive**: Logs must be structured (JSON format), containing critical diagnostic fields: `Timestamp`, `CorrelationId` / `TraceId`, `LogLevel`, and `ExceptionDetails` when applicable.

### `[REF-OBS-TRACE]`: Distributed Tracing
- **Source**: *Software Engineering* (Ian Sommerville)
- **Directive**: Propagate `TraceId` / `CorrelationId` headers in all cross-service calls, API requests, and message brokers to enable complete transaction tracing.

### `[REF-RES-CIRCUIT]`: Circuit Breaker & Resilience
- **Source**: *Software Engineering* (Ian Sommerville)
- **Directive**: Protect all external integration points against transient failures by configuring:
  1. Timeouts (to prevent blocking threads).
  2. Exponential Backoff with Jitter (to retry cleanly).
  3. Circuit Breakers (to stop requests when failure thresholds are exceeded).

---

## 5. 🤖 AI PAIR PROGRAMMING & PROMPT ENGINEERING (Optimizing Prompt Engineering)

### `[REF-AI-CONTRACT]`: Token-Budget Context Pruning
- **Source**: *Optimizing Prompt Engineering for Generative AI* (Erik Herman)
- **Directive**: To keep code accuracy high and prevent context degradation, if active context usage reaches **70% of the model limit**, alert the user to summarize the session into `current-context.md` and start a new chat. Output only git-like diffs for file edits to preserve output tokens.

---

## 6. 🌐 NETWORK OBSERVABILITY & LATENCY OPTIMIZATION (Wireshark Network Analysis)

### `[REF-NET-EVIDENCE]`: Evidence-Based Troubleshooting
- **Source**: *Wireshark Network Analysis* (Laura Chappell)
- **Directive**: Prohibit blind guessing. When diagnosing performance issues or timeouts, you must request and analyze payload sizes, HTTP response times, or TCP packet traces first before suggesting code modifications.

### `[REF-NET-PAYLOAD]`: Network Payload Optimization
- **Source**: *Wireshark Network Analysis* (Laura Chappell)
- **Directive**: Always optimize payload size. Relational or NoSQL models must be mapped to flat, minimal DTOs to avoid sending unused fields over the wire.

### `[REF-NET-BATCH]`: Chunky vs Chatty (Request Batching)
- **Source**: *Wireshark Network Analysis* (Laura Chappell)
- **Directive**: Prohibit executing API requests inside loops. Use Backend-For-Frontend (BFF) or aggregated API endpoints to fetch data in a single chunky payload instead of multiple chatty requests.

### `[REF-NET-LATENCY]`: Latency Differentiation
- **Source**: *Wireshark Network Analysis* (Laura Chappell)
- **Directive**: Differentiate between Server Response Time (backend/database processing delay) and Network Latency (transmission delay) using time-to-first-byte (TTFB) analysis and timestamps.

### `[REF-NET-COMPRESS]`: Compression Enforcement
- **Source**: *Wireshark Network Analysis* (Laura Chappell)
- **Directive**: Ensure compression (e.g. GZIP, Brotli) is enabled for all JSON payloads and web resources to minimize bandwidth usage.

