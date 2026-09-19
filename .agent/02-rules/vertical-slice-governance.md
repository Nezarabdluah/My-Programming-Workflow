---
id: rules-vertical-slice
description: Optional full-stack web coverage guidance. Activate only when the project/profile declares these layers relevant.
alwaysApply: false
globs: []
requires: []
---

# Full-Stack Web Vertical Slice Guidance

> **AOS v8 status:** optional/project-profile guidance per ADR-006.
> This file is **not** a fixed project-agnostic Core rule.

## 1. Activation

Use this guidance only when:
- the Project Profile declares a full-stack web architecture, or
- the existing codebase clearly uses these layers and the task spans them, or
- the Navigator explicitly activates this coverage model.

Do not force missing layers into projects that do not use them.

## 2. Coverage Principle

Before declaring a feature complete, identify every project area materially affected by the change and verify each one.

For a typical full-stack web project, candidate areas may include:

| Area | Typical evidence |
|------|------------------|
| Data persistence | schema/migration/query/index evidence when affected |
| Domain/business rules | entities/value objects/domain services/rules when affected |
| Application/use-case layer | orchestration, DTO/contracts, validation when affected |
| API/integration boundary | endpoint, authorization, error contract when affected |
| Frontend/state | component/state/data flow when affected |
| UI/UX/accessibility | interaction/design/accessibility when affected |
| Tests | tests or other proportional verification for changed behavior |

These are **candidate areas, not mandatory layers**.

## 3. Planning

Plan vertically when that produces independently valuable/testable increments.

Do not create database, domain, API, frontend, or UI artifacts merely to satisfy a checklist.

For each affected area record one of:
- `done` with evidence,
- `not applicable` with a short reason,
- `deferred` with a follow-up task/decision.

## 4. Completion Report

When this profile is active, use a dynamic coverage table:

```markdown
| Affected area | Status | Evidence / Reason |
|---------------|--------|-------------------|
| [project-defined area] | done / not applicable / deferred | [path, check, or reason] |
```

Also record material architectural decisions, deviations from established project patterns, and items that require human review.

## 5. Evidence Rules

- Evidence must reflect the actual project architecture.
- Production-source REF/CONST comments are optional.
- Do not invent a layer or artifact solely for compliance.
- Tests/verification are proportional to risk and behavior changed.
- Security, authorization, destructive data changes, and irreversible migrations require stronger review regardless of layer count.

## 6. Migration Note

This file supersedes the v7 fixed seven-layer charter. ADR-006 is the architectural decision authorizing the change. Future Technology Profiles may reference this file or absorb its guidance.
