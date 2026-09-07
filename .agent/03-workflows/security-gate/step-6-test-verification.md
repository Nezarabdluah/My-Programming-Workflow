# Security Gate — Step 6: Test Verification

> This is step 6 of 7. Previous: `step-5-code-review.md` | Next: `step-7-gate-report.md`

---

## Task: verify tests cover the security changes

### 1. Authorization tests:
- [ ] Test denying access without login (401)
- [ ] Test denying access with insufficient permissions (403)
- [ ] Test IDOR denial (a user attempting to access another user's resource)

### 2. Input tests:
- [ ] Test rejecting empty/invalid inputs (400)
- [ ] Test rejecting malicious inputs (SQL injection, XSS payloads)

### 3. Test execution:
- [ ] All tests pass ✅
- [ ] No skipped tests without a recorded reason

---

Done? Open the next step: `step-7-gate-report.md`
