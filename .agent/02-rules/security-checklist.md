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
- Prefer server-managed secure sessions or HttpOnly cookies for browser applications when the architecture supports them.
- Do not put long-lived/high-value bearer tokens in browser storage without an explicit threat-model decision and compensating controls.
- Cookie attributes (Secure/SameSite) must match the deployment and cross-site flow requirements.

### Refresh token rotation:
- ✅ Issue a new Refresh Token with every renewal request
- ✅ If a rotated old token is reused ← revoke the entire token family immediately (likely breach)

### Algorithm protection:
- ✅ Explicitly pin the accepted algorithm in verification settings
- ❌ Reject `alg: "none"` or any key chosen dynamically from the token header

---

## 2. Access Control & IDOR

### Default-deny policy:
- Protected resources should use default-deny authorization where the framework/application supports it.
- Public/anonymous endpoints must be explicit and reviewed.

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
- Apply rate limiting/abuse controls where exposure, cost, or threat model justifies them; do not add arbitrary throttling to every endpoint without context.
- Require HTTPS for production and untrusted networks. Local development/test environments may use HTTP when isolated and explicitly configured.
- ❌ Never store secrets (API keys, passwords) in source code
