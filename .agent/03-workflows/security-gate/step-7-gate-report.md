# Security Gate — Step 7: Gate Report

> This is step 7 of 7 (the last). Previous: `step-6-test-verification.md`

---

## Task: produce the security gate report

### Template:
```markdown
# 🛡️ Security Gate Report

**Date**: [today's date]
**Task**: [task description]
**Classification**: 🔴 Sensitive

## Check Results

| Step | Result | Notes |
|------|--------|-------|
| 1. Threat modeling | ✅/❌ | [notes] |
| 2. Dependency check | ✅/❌ | [notes] |
| 3. Secret scan | ✅/❌ | [notes] |
| 4. Access review | ✅/❌ | [notes] |
| 5. Code review | ✅/❌ | [notes] |
| 6. Test verification | ✅/❌ | [notes] |

## Final Verdict
- ✅ **PASS**: all steps passed — the task is ready for delivery
- ❌ **FAIL**: step [X] failed — must be fixed before delivery

## Discovered Issues (if any)
| # | Issue | Severity | Fix |
|---|-------|----------|-----|
| 1 | [description] | Critical/High/Medium | [what was done] |
```

---

## After the Report:
1. If PASS ← deliver the task
2. If FAIL ← fix the issues ← re-run only the failed steps
3. Update `04-memory/project-context.md`
