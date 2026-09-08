# 06-templates/ — Stack-Specific Plugin System

> **AOS is stack-agnostic**. This folder contains optional, stack-specific plugins that load conditionally.
> The AOS core (`01-core/`, `02-rules/`, `03-workflows/`, `04-memory/`, `05-references/`) works with ANY tech stack.

---

## How It Works

```
  AOS Core (stack-agnostic)
  ├── 01-core/          ← universal workflow rules
  ├── 02-rules/         ← language-agnostic engineering rules
  ├── 03-workflows/     ← stack-agnostic pipelines
  ├── 04-memory/        ← universal memory system
  ├── 05-references/    ← generic references and constitutions
  └── 06-templates/     ← OPTIONAL stack-specific plugins
      ├── dotnet-abp/   ← .NET/ABP plugin (optional)
      ├── lang-python/  ← Python plugin (community-contributed)
      ├── lang-node/    ← Node.js plugin (community-contributed)
      └── lang-go/      ← Go plugin (community-contributed)
```

---

## Available Plugins

| Plugin | Stack | Status | Description |
|--------|-------|--------|-------------|
| `dotnet-abp/` | .NET 8 + ABP Framework | ✅ Available | Entity patterns, standards, persona, prompts, PR template, pre-commit, CI gate |
| `lang-python/` | Python | 🔜 Coming Soon | — |
| `lang-node/` | Node.js / TypeScript | 🔜 Coming Soon | — |
| `lang-go/` | Go | 🔜 Coming Soon | — |

---

## How Plugins Are Loaded

The AOS agent uses **conditional injection** via the wiring-registry and master-index:

```
  IF stack-specific plugin installed in 06-templates/{stack}/
  THEN:
    1. Load the plugin's prompts alongside generic prompts (no conflict)
    2. Follow the plugin's entity patterns and standards
    3. Apply the plugin's PR template and pre-commit config
  ELSE:
    - Use only generic prompts from 05-references/prompts/
    - Follow universal engineering rules from 02-rules/
```

---

## Create Your Own Stack Plugin

### Step 1: Copy the template
```bash
cp -r 06-templates/dotnet-abp/ 06-templates/lang-your-stack/
```

### Step 2: Replace content
Keep the same file structure but replace with your stack's patterns:

| File | What to put in it |
|------|-------------------|
| `entity-pattern.md` | Your stack's entity/model patterns |
| `standards.md` | Your stack's coding standards and conventions |
| `persona.md` | System persona for code generation in your stack |
| `prompts.md` | Ready-to-use prompts for your stack |
| `pull_request_template.md` | PR template for your stack |
| `pre-commit-config.yaml` | Git hooks for your stack (linters, formatters) |
| `github-security-gate.yml` | CI/CD security workflow for your stack |

### Step 3: Register your plugin
Add your plugin to the table in this file so others can discover it.

---

## Why Stack-Agnostic?

AOS is a **workflow framework**, not a tech stack. It defines:
- **How** you work (phases, gates, verification, review)
- **What** quality standards apply (SOLID, DDD, security, testing)
- **When** to load resources (conditional injection)

The **what** you build (React, Django, Rails, Go) is YOUR choice. AOS adapts to your stack via plugins.

---

## FAQ

**Q: Do I need a plugin to use AOS?**
A: No. AOS works out of the box with any stack. Plugins are optional enhancements.

**Q: Can I use multiple plugins?**
A: Yes. Each plugin loads independently. You can have `dotnet-abp/` and `lang-python/` in the same project.

**Q: Will plugins conflict with each other?**
A: No. Plugins are isolated. Each plugin's files are loaded only when its stack is detected.

**Q: How do I know which plugin is active?**
A: The agent's boot report shows which stack is detected and which plugins are loaded.
