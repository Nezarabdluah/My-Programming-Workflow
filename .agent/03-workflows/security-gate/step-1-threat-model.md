# Security Gate — Step 1: Threat Model

> This is step 1 of 7. Next: `step-2-dependency-check.md`

---

## Task: identify potential threats

### 1. Classify the exposed assets:
- What sensitive data exists? (passwords, personal data, financial)
- What systems are exposed? (public APIs, user interfaces)

### 2. Use STRIDE to classify threats:
| Threat | Question | Applies? |
|--------|----------|----------|
| **S**poofing | can one impersonate another user? | |
| **T**ampering | can data be modified without permission? | |
| **R**epudiation | can a performed action be denied? | |
| **I**nformation Disclosure | can confidential data be exposed? | |
| **D**enial of Service | can the service be disrupted? | |
| **E**levation of Privilege | can permissions be escalated? | |

### 3. Assign severity:
| Threat | Likelihood | Impact | Severity | Mitigation |
|--------|-----------|--------|----------|------------|
| [description] | high/medium/low | high/medium/low | [product] | [action] |

---

Done? Open the next step: `step-2-dependency-check.md`
