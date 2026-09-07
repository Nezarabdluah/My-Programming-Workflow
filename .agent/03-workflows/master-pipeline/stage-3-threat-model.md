# Master Pipeline — Stage 3: Threat Model & Security Design

> This is stage 3 of 8. Next: `stage-4-implementation.md`
> Required for: 🔴 | Skipped for: 🟢 🟡

---

## Decision Gate

```yaml
gate:
  stage_number: 3
  stage_name: "Threat Model & Security Design"
  classification_required: [🔴]
  previous_stage_status: passed       # stage 2 must pass
  requires:
    - approved architecture from stage 2
    - feature specs from stage 1
  resources_loaded:
    - "⚠️ MANDATORY: read 05-references/books/00-master-index.md → Stage 3 row"
    - constitutions: security-constitution (Zero Trust, XSS, BOLA, TOCTOU)
    - 02-rules/security-checklist.md
    - wiring-registry → REF-SEC contracts
  decision: proceed | skip

# Skip condition: classification ∈ {🟢, 🟡}
#   → ⛔ GATE SKIPPED — classification does not require formal threat modeling
```

---

## Task: STRIDE threat model and security design review

### 3.1 — STRIDE Analysis

```
□ For each component in the architecture:
  - Spoofing: can an attacker impersonate a user or service?
  - Tampering: can data be modified in transit or at rest?
  - Repudiation: can actions be denied without audit trail?
  - Information Disclosure: can sensitive data leak?
  - Denial of Service: can the service be overwhelmed?
  - Elevation of Privilege: can a user gain unauthorized access?

□ Document findings in a threat matrix:
  | Component | Threat | Category | Severity | Mitigation |
```

### 3.2 — Security Controls Design

```
□ For each identified threat, design mitigations:
  - Authentication: JWT handling (REF-SEC-JWT)
  - Authorization: IDOR prevention (REF-SEC-IDOR)
  - Input validation: boundary checks (REF-SEC-VALID)
  - Output encoding: XSS prevention (REF-SEC-XSS)
  - Query safety: injection prevention (REF-SEC-INJECT)

□ Grep [OPS-SECTEST], [OPS-SHIFTLEFT], [OPS-OWASP10] for additional controls
```

### 3.3 — Security Gate Review

```
□ Optionally invoke the full security-gate workflow:
  03-workflows/security-gate/00-coordinator.md
  (7 steps: threat model → dependency check → secret scan →
   access review → code review → test verification → gate report)

□ If invoked, the security-gate report becomes evidence for this stage
```

### 3.4 — Developer Review Gate

```
⏸️ HARD STOP — present the threat model to the developer.

□ Summarize: threats found, severity, planned mitigations
□ Wait for explicit approval

  Developer approves → ✅ GATE PASSED
  Developer requests changes → revise mitigations
  Developer rejects → ⛔ GATE FAILED — record reason
```

---

## Resource Injection (from wiring-registry)

| Resource | When |
|----------|------|
| `02-rules/security-checklist.md` | Always at stage entry |
| Grep `REF-SEC-JWT, IDOR, VALID, XSS, INJECT` | During controls design |
| DevOps: grep `[OPS-SECTEST]`, `[OPS-SHIFTLEFT]`, `[OPS-OWASP10]` | For compliance checks |

---

## Gate Output

```yaml
gate_result:
  stage: 3
  status: ✅ GATE PASSED | ⛔ GATE FAILED | ⛔ NEEDS CLARIFICATION
  threats_identified: 0
  critical_threats: 0
  mitigations_designed: 0
  security_gate_invoked: true | false
  developer_approved: true | false
  next_stage: 4
  blockers: []
```

> After gate passes → record security decisions as ADRs in `decisions.md`.
