# .NET/ABP Plugin — Optional Stack-Specific Templates

> **Status**: Optional plugin — NOT required by AOS core
> **适用场景**: .NET 8 + ABP Framework + SQL Server + Angular projects only
> **AOS is stack-agnostic**: this plugin is ONE example of how stack-specific templates work

---

## What This Plugin Provides

| File | Purpose |
|------|---------|
| `entity-pattern.md` | Ready-to-copy .NET/ABP entity patterns (properties, DbSets, encapsulation rules) |
| `standards.md` | .NET/ABP coding standards (DDD in ABP, API Gateway YARP, abphelper post-generation fixes) |
| `persona.md` | System persona for .NET code generation (Senior Software Architect + Security Engineer) |
| `prompts.md` | Ready-to-use .NET/ABP prompts (backend generation, abphelper fix, Angular + ABP) |
| `pull_request_template.md` | PR template for .NET/ABP projects |
| `pre-commit-config.yaml` | Git hooks: gitleaks + dotnet format |
| `github-security-gate.yml` | GitHub Actions CI/CD security workflow for .NET |

---

## When to Use This Plugin

```
  ✅ USE this plugin when:
     - Your project uses .NET 8 + ABP Framework
     - You want ABP-specific entity patterns and standards
     - You need abphelper post-generation fixes

  ❌ DO NOT use this plugin when:
     - Your project uses Python, Node.js, Go, Ruby, etc.
     - Your project uses a different .NET framework (not ABP)
     - You want generic backend patterns (use 05-references/prompts/backend-prompts.md instead)
```

---

## How to Activate This Plugin

1. Copy this entire `dotnet-abp/` folder to your project's `.agent/06-templates/dotnet-abp/`
2. The AOS agent will automatically detect it and inject the relevant templates when working on .NET/ABP code
3. No configuration needed — the wiring-registry and master-index handle conditional loading via `IF stack plugin`

---

## How to Create Your Own Stack Plugin

1. Copy this `dotnet-abp/` folder as a template
2. Rename it to your stack (e.g., `lang-python/`, `lang-node/`, `lang-go/`)
3. Replace the content with your stack's patterns, standards, and prompts
4. Keep the same file structure (entity-pattern.md, standards.md, prompts.md, etc.)
5. Add your plugin to `06-templates/README.md` so others can discover it

---

## AOS Core Remains Stack-Agnostic

This plugin does NOT make AOS stack-specific. The core AOS files:
- `01-core/` — universal workflow rules
- `02-rules/` — language-agnostic engineering rules
- `03-workflows/` — stack-agnostic pipelines
- `04-memory/` — universal memory system
- `05-references/` — generic references and constitutions

Only `06-templates/{stack}/` is stack-specific, and it loads conditionally via `IF stack plugin`.
