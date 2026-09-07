# Security Gate — Step 2: Dependency Check

> This is step 2 of 7. Previous: `step-1-threat-model.md` | Next: `step-3-secret-scan.md`

---

## Task: check external dependencies

### 1. List every direct dependency:
| Library | Version | Last update | Known vulnerabilities? |
|---------|---------|-------------|------------------------|
| [name] | [X.Y.Z] | [date] | yes/no |

### 2. Check for vulnerabilities:
- ✅ Run the vulnerability scanner appropriate to your stack:
  - `npm audit` / `yarn audit` — Node.js
  - `dotnet list package --vulnerable` — .NET
  - `pip audit` / `safety check` — Python
  - `cargo audit` — Rust
  - or any equivalent SBOM tool

### 3. Decision:
- ❌ Critical or High vulnerability ← **must be fixed before continuing**
- ⚠️ Medium vulnerability ← record it with a remediation plan
- ✅ Low or None ← continue

---

Done? Open the next step: `step-3-secret-scan.md`
