# Production Readiness Review (PRR) — Scorecard & Checklist

> Standalone workflow for assessing production readiness before deployment.
> Referenced by: master-pipeline stage 6 (Production Readiness Review)
> Related references: `05-references/devops-ops/` (grep-only)

---

## Purpose

This workflow provides a structured production readiness assessment using a scorecard model. It ensures that no critical operational dimension is overlooked before a production deployment.

---

## 1. PRR Scorecard

Assess each dimension on a 3-level scale:

| Level | Meaning |
|-------|---------|
| 🟢 Ready | Meets all requirements — no action needed |
| 🟡 Conditional | Gaps exist but are mitigated or accepted with a plan |
| 🔴 Not Ready | Critical gaps — must be resolved before deployment |

### Scorecard Dimensions

```
┌────────────────────────┬────────┬──────────────────────────────────┐
│ Dimension              │ Score  │ Evidence / Notes                 │
├────────────────────────┼────────┼──────────────────────────────────┤
│ 1. Reliability         │        │                                  │
│ 2. Scalability         │        │                                  │
│ 3. Observability       │        │                                  │
│ 4. Security            │        │                                  │
│ 5. Disaster Recovery   │        │                                  │
│ 6. Documentation       │        │                                  │
│ 7. Operational Runbook │        │                                  │
│ 8. Dependency Health   │        │                                  │
│ 9. Data Management     │        │                                  │
│ 10. Compliance         │        │                                  │
└────────────────────────┴────────┴──────────────────────────────────┘
```

---

## 2. Dimension Details

### 2.1 Reliability (grep [OPS-PRR])
```
□ Error handling covers all critical paths
□ Retry/circuit-breaker patterns for external calls (REF-RES-CIRCUIT)
□ Graceful degradation under partial failures
□ Health check endpoints available
□ No single points of failure identified
```

### 2.2 Scalability
```
□ Load tested (if applicable — grep [OPS-K6])
□ Database queries optimized (REF-DB-SARG, REF-DB-N1)
□ Pagination implemented for list endpoints (REF-DB-PAG)
□ Resource limits configured (memory, CPU, connections)
□ Horizontal scaling path identified
```

### 2.3 Observability (grep [OPS-OBSERVABILITY])
```
□ Structured logging (REF-OBS-LOG) — no PII in logs
□ Distributed tracing (REF-OBS-TRACE) — correlation IDs propagated
□ Metrics / dashboards configured
□ Alerting rules defined (grep [OPS-ALERTS])
□ Log retention policy set
```

### 2.4 Security (grep [OPS-SECTEST])
```
□ Authentication verified (REF-SEC-JWT)
□ Authorization — no IDOR vulnerabilities (REF-SEC-IDOR)
□ Input validation on all boundaries (REF-SEC-VALID)
□ Secrets management — no hardcoded credentials
□ Dependency vulnerability scan clean
□ OWASP Top 10 reviewed (grep [OPS-OWASP10])
```

### 2.5 Disaster Recovery (grep [OPS-ROLLBACK])
```
□ Backup strategy documented and tested
□ Rollback plan documented and rehearsed
□ Database migration rollback tested
□ Recovery Time Objective (RTO) defined
□ Recovery Point Objective (RPO) defined
```

### 2.6 Documentation
```
□ API documentation current (OpenAPI / Swagger)
□ Architecture decision records (ADRs) up to date
□ README with setup instructions
□ Change log / release notes prepared
```

### 2.7 Operational Runbook
```
□ Common incident response procedures documented
□ Escalation paths defined
□ On-call rotation identified (if applicable)
□ Known issues and workarounds listed
```

### 2.8 Dependency Health
```
□ All dependencies on supported versions
□ No known CVEs in dependency tree
□ License compliance verified
□ External service SLAs reviewed
```

### 2.9 Data Management
```
□ Database migrations tested (forward and backward)
□ Data retention policy defined
□ PII handling compliant with requirements
□ Backup/restore tested
```

### 2.10 Compliance
```
□ Regulatory requirements identified and met
□ Audit trail in place (if required)
□ Data processing agreements current
□ Privacy impact assessment (if applicable)
```

---

## 3. PRR Decision Logic

```
All dimensions 🟢:
  → ✅ PRR PASSED — ready for production

Any dimension 🟡 (none 🔴):
  → ✅ PRR PASSED with conditions
  → Document: condition + owner + deadline for resolution

Any dimension 🔴:
  → ⛔ PRR FAILED — resolve before deployment
  → Document: blocker + remediation plan
```

---

## 4. DevOps Reference Anchors (grep-only)

Use these anchors to query `05-references/devops-ops/devops-enterprise-and-production-readiness.md`:

| Anchor | Topic |
|--------|-------|
| `[OPS-INTAKE]` | Initial project intake |
| `[OPS-SIGNALS]` | Health signals and monitoring |
| `[OPS-20TEST]` | 20% test rule |
| `[OPS-SLO]` | SLO definition |
| `[OPS-SECTEST]` | Security testing |
| `[OPS-DBPERF]` | Database performance |
| `[OPS-SCORECARD]` | Production scorecard |
| `[OPS-DORA]` | DORA metrics |
| `[OPS-PRR]` | Production readiness review |
| `[OPS-ROLLBACK]` | Rollback procedures |
| `[OPS-OBSERVABILITY]` | Observability stack |
| `[OPS-K6]` | Load testing with K6 |
