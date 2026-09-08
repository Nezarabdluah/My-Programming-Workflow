# 06-templates/ — Universal Templates (Stack-Agnostic)

> **AOS is fully stack-agnostic**. All templates here work with ANY programming language or framework.
> Customize the pre-commit and CI/CD templates for your specific stack.

---

## Available Templates

| File | Purpose | Customization Needed? |
|------|---------|----------------------|
| `entity-patterns.md` | Universal entity/model patterns, layered architecture, frontend components | No — works as-is |
| `coding-standards.md` | SOLID, DDD, encapsulation, async, caching, error handling, testing | No — works as-is |
| `pre-commit-template.yaml` | Secret scan + hygiene checks + formatting hooks | Yes — uncomment your stack's formatter |
| `github-security-gate.yml` | CI/CD security workflow (secret scan, deps, format, build, test) | Yes — customize build/test commands |
| `pull_request_template.md` | PR template with security gate attestation | No — works as-is |

---

## How to Customize for Your Stack

### Pre-commit (pre-commit-template.yaml)
Uncomment the formatting hook for your stack:
- **Python**: `black` or `ruff`
- **JavaScript/TypeScript**: `prettier` + `eslint`
- **Go**: `gofmt` + `golangci-lint`
- **Rust**: `cargo fmt` + `cargo clippy`
- **.NET**: `dotnet format`

### CI/CD (github-security-gate.yml)
Replace the placeholder steps with your stack's commands:
- **Dependency check**: `pip-audit`, `npm audit`, `govulncheck`, `cargo audit`
- **Formatting**: `ruff check`, `prettier --check`, `gofmt -l`, `cargo fmt --check`
- **Build**: `npm run build`, `go build ./...`, `cargo build --release`
- **Test**: `pytest --cov`, `npm test -- --coverage`, `go test -coverprofile=coverage.out ./...`

---

## Philosophy

AOS defines **how** you work (phases, gates, verification). The **what** you build (Python, Go, Rust, etc.) is YOUR choice. These templates provide the universal scaffolding — you fill in the stack-specific details.

---

## Creating Stack-Specific Extensions

If you need stack-specific templates (e.g., for a particular framework):

1. Create a new file in `06-templates/` named after your stack (e.g., `django-patterns.md`)
2. Follow the same structure as the existing templates
3. Keep it stack-agnostic where possible — only include patterns specific to your framework
4. Update this README to list your new template
