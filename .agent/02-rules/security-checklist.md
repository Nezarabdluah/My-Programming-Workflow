---
id: rules-security
description: JWT/session storage rules, IDOR defense, injection & XSS prevention, double-boundary validation. Load for any security, auth, or authorization work.
alwaysApply: false
globs: ["**/Auth/**", "**/Security/**", "**/*Controller*", "**/Middleware/**"]
requires: [REF-SEC-JWT, REF-SEC-IDOR, REF-SEC-VALID, REF-SEC-XSS, REF-SEC-INJECT]
---

# Security Checklist

> Load this file when the task concerns security, authentication, or authorization.

---

## 1. JWT & Session Security

### Token storage:
- ❌ **Never** store JWTs in localStorage or sessionStorage (XSS-exposed)
- ✅ Store them in `HttpOnly` + `Secure` + `SameSite=Strict` cookies

### Refresh token rotation:
- ✅ Issue a new Refresh Token with every renewal request
- ✅ If a rotated old token is reused ← revoke the entire token family immediately (likely breach)

### Algorithm protection:
- ✅ Explicitly pin the accepted algorithm in verification settings
- ❌ Reject `alg: "none"` or any key chosen dynamically from the token header

---

## 2. Access Control & IDOR

### Default-deny policy:
- ✅ All routes and endpoints deny access by default
- ✅ Grant access explicitly via attributes or middleware

### IDOR prevention (Insecure Direct Object Reference):
- ❌ Never assume the logged-in user owns a resource just because they supplied an ID
- ✅ **Always** verify ownership in the query:
  ```
  db.orders.find(id == orderId AND owner_id == currentUser.id)
  ```

### Centralized session context:
- ❌ Never read user roles or identity from query params or body
- ✅ Read them exclusively from the verified security context (server-side session/token)

---

## 3. Injection & XSS

### SQL Injection:
- ✅ Use parameterized queries or an ORM
- ❌ **Never** paste user input into SQL or system commands
- ✅ For dynamic identifiers (table names, sorting) ← validate against a strict whitelist

### XSS Prevention:
- ❌ Never use unsafe APIs with user data:
  - `innerHTML`, `eval()`, `dangerouslySetInnerHTML`, `bypassSecurityTrustHtml`
- ✅ Use safe text binding that auto-encodes HTML

---

## 4. Boundary Validation — Double Boundary

- ✅ **Boundary 1**: validate input at the edge (DTO validation, schema validators)
  ← reject malformed requests early
- ✅ **Boundary 2**: re-validate inside domain entities (business rules/invariants)
  ← guarantee invalid state is never saved even if it crosses the edge

---

## 5. General Rules

- ✅ Never expose stack traces or technical details to end users
- ✅ Log security errors to an internal log with a CorrelationId
- ✅ Add rate limiting to every public API
- ✅ Use HTTPS only — no HTTP in any environment
- ❌ Never store secrets (API keys, passwords) in source code
