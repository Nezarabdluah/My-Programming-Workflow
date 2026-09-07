# 🛡️ Security Gate — Coordinator

> Execute the seven steps in order. Never skip a step.

## ⚠️ Mandatory Resource Injection (before starting gate) — MUST, gate blocked without it
0. Read `05-references/books/00-master-index.md` Stage 3 → load every MUST resource listed there
1. Read `01-core/wiring-registry.md` → find Security capability row
2. Load `05-references/books/constitutions/security-constitution.md` — 17 rules (Zero Trust, XSS, BOLA, TOCTOU, Memory Safety)
3. Load `02-rules/security-checklist.md` → cite REF-SEC-* contracts as `// [REF-SEC-X]`
4. Grep `05-references/devops-ops/devops-enterprise-and-production-readiness.md` for `[OPS-SECTEST]`, `[OPS-OWASP10]`
5. IF GitHub → apply `06-templates/dotnet-abp/github-security-gate.yml`
6. Cite constitutions as `// [CONST-SEC-N]` and produce a 1-line Resource Utilization Summary before Done

1. `step-1-threat-model.md` — threat modeling (human / manual)
2. `step-2-dependency-check.md` — dependency check (automated via CI/CD)
3. `step-3-secret-scan.md` — secret scan (automated via pre-commit and CI/CD)
4. `step-4-access-review.md` — access review (human / manual)
5. `step-5-code-review.md` — code & formatting review (partially automated via CI/CD)
6. `step-6-test-verification.md` — test & coverage verification (automated via CI/CD)
7. `step-7-gate-report.md` — final report (auto-posted in PR comments and recorded in memory)

*Note*: the security gates were integrated with effective automation tools for .NET projects to block merging on failure.

Start step 1 now.
