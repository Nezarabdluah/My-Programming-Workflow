# Security Gate — Step 5: Code Review

> This is step 5 of 7. Previous: `step-4-access-review.md` | Next: `step-6-test-verification.md`

---

## Task: review modified code from a security perspective

### 1. Injection check:
- [ ] No SQL/NoSQL built by string concatenation
- [ ] No `eval()`, `exec()`, or system commands with user input
- [ ] All inputs are validated and sanitized

### 2. XSS check:
- [ ] No `innerHTML`, `dangerouslySetInnerHTML`, `bypassSecurityTrustHtml`
- [ ] All user data is rendered via safe text binding

### 3. Error-handling check:
- [ ] No stack trace shown to the user
- [ ] Error messages are generic for users + detailed in logs
- [ ] Errors are logged with a correlation_id

### 4. Sensitive-data check:
- [ ] Passwords are never returned in any response
- [ ] Personal data is never written to logs
- [ ] DTOs are pruned — no extra fields

---

Done? Open the next step: `step-6-test-verification.md`
