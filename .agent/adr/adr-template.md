# ADR [Number]: [Short Title of Decision]

> [!CAUTION]
> **Over-Engineering Guard**: Do NOT write an ADR for routine feature development, simple class refactoring, or everyday tasks. 
> ADRs are STRICTLY reserved for foundational, high-impact architectural shifts (e.g., changing DB engines, choosing between REST and gRPC, adopting event sourcing, or refactoring security frameworks).

*   **Status**: [Proposed | Approved | Deprecated | Superseded by ADR-XXXX]
*   **Date**: YYYY-MM-DD
*   **Author**: [Your Name / Agent Name]
*   **Deciders**: [List of decision-makers]

---

## 1. Context & Problem Statement
Describe the technical context, requirement, or problem you are trying to solve. What are the constraints, user stories, or issues driving this decision?

---

## 2. Decision Driver Rules (Citations)
List the specific rule IDs from `.agent/directives/reference-catalog.md` or engineering principles driving this architectural decision.
*   `[REF-...]`: [Description of rule relevance]
*   `[REF-...]`: [Description of rule relevance]

---

## 3. Alternatives Considered
Detail the other designs or technical choices considered, along with their pros and cons.

### Option A: [Option Title]
*   **Description**: Briefly explain this option.
*   **Pros**:
    *   Benefit 1
    *   Benefit 2
*   **Cons**:
    *   Drawback 1
    *   Drawback 2

### Option B: [Option Title]
*   **Description**: Briefly explain this option.
*   **Pros**:
    *   Benefit 1
*   **Cons**:
    *   Drawback 1

---

## 4. Chosen Decision
Explain the selected solution, why it was chosen over the alternatives, and how it resolves the problem statement while adhering to the referenced directives.

---

## 5. Consequences & Implications
Detail the trade-offs and impact of this choice on the codebase and future development.
*   **What is simplified**: [Explain what is easier]
*   **What is made more complex / Technical Debt**: [Explain any trade-offs, limitations, or downstream changes required]
*   **Observability & Security impact**: [Mention logs, metrics, or permission gates impacted]
*   **Migration Plan**: [If overriding existing code, how will it be migrated?]
