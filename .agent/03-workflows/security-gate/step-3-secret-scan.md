# Security Gate — Step 3: Secret Scan

> This is step 3 of 7. Previous: `step-2-dependency-check.md` | Next: `step-4-access-review.md`

---

## Task: verify no secrets are exposed in the code

### 1. Search for secret patterns:
```
Search the code for:
- API keys: any string starting with sk-, pk-, AKIA, ghp_, xox
- Passwords: any variable named password, secret, token, key
- Connection strings: any string containing Server=, Host=, mongodb://
- Private keys: -----BEGIN RSA PRIVATE KEY-----
```

### 2. Verify the files:
- [ ] `.env` is in `.gitignore`
- [ ] No `.pem`, `.key`, `.p12` files in the repository
- [ ] `appsettings.json` / `config.py` contains no real secrets
- [ ] No secrets in Docker Compose or CI/CD files

### 3. Decision:
- ❌ Exposed secret ← **remove it immediately + rotate the key**
- ✅ Clean ← continue

---

Done? Open the next step: `step-4-access-review.md`
