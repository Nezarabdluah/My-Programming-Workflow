# Task Classification — AOS v8.0.0-rc.1

Classify every task before implementation:
`[Mode: 🟢 Simple | 🟡 Medium | 🔴 Sensitive]`

Classification is **risk-first**, not file-count-first. File count is only a weak signal.

## 🟢 Simple
Use when the change is local, reversible, and low-risk.

Typical examples:
- documentation/typo/localization text,
- visual styling with no behavior/security/data impact,
- small configuration cleanup,
- isolated bug fix with low blast radius.

Required:
- inspect the affected area,
- proportional verification,
- concise completion evidence.

A Simple task may still need a test/build/lint/visual check when behavior or tooling can regress.

## 🟡 Medium
Use when the task changes localized behavior or business logic without crossing a sensitive boundary.

Typical examples:
- localized business-rule change,
- API behavior within an established contract,
- multi-file refactor within an approved architecture,
- new non-sensitive workflow in an existing pattern.

Required:
- acceptance criteria or plan appropriate to the change,
- verification of affected behavior,
- no new architectural decision without escalation.

## 🔴 Sensitive
Use when failure could materially affect security, data integrity, architecture, production, or external contracts.

Automatic strong signals:
- authentication/authorization/security boundary,
- schema/data migration or destructive data operation,
- architecture/module boundary change,
- secrets/permissions/tenancy/isolation,
- production deployment/rollback,
- payment or other high-integrity transaction,
- irreversible or high-blast-radius change.

Required:
- explicit risk review,
- relevant ADR/approval when a new decision is introduced,
- stronger verification and evidence.

## Risk Dimensions
Consider:
- security impact,
- data impact,
- architecture impact,
- external contract impact,
- blast radius,
- reversibility,
- production impact,
- migration/destructive risk.

Escalate when any dimension materially increases.
Do not silently downgrade during execution.

## File Count
File count alone never determines classification.
Many low-risk files can remain 🟢/🟡; one authorization or schema file can be 🔴.
