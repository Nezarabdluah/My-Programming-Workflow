# Security Gate — Step 4: Access Review

> This is step 4 of 7. Previous: `step-3-secret-scan.md` | Next: `step-5-code-review.md`

---

## Task: verify the authorization system

### 1. Default-Deny check:
- [ ] Every endpoint is protected by explicit authorization checks
- [ ] No endpoint is unintentionally open
- [ ] Admin pages are protected by elevated permissions

### 2. IDOR check:
- [ ] Every query verifies resource ownership:
  ```
  ✅ db.find(id == resourceId AND owner_id == currentUser.id)
  ❌ db.find(id == resourceId)  // IDOR!
  ```
- [ ] No endpoint accepts user_id from the request (the client)

### 3. Session context check:
- [ ] User identity is read from the server-side session only
- [ ] Roles and permissions are never read from query params or body
- [ ] Every sensitive state change requires re-verification

### 4. Decision:
- ❌ An IDOR vulnerability or open endpoint ← **must be fixed immediately**
- ✅ Everything protected ← continue

---

Done? Open the next step: `step-5-code-review.md`
