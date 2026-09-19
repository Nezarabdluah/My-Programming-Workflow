"""AOS Governance — Memory Tests (v8.0.0-rc.1)

GOV-T03: ADR structure validation
GOV-T04: Active mistakes cap (max 20)
GOV-T05: Handoff validity (mandatory memory files present)
GOV-T11: Boot context budget compliance
"""
import re
from pathlib import Path

PASS = "PASS"
FAIL = "FAIL"
SKIP_EXPECTED = "SKIP_EXPECTED"
SKIP_UNSUPPORTED = "SKIP_UNSUPPORTED"

# v8 release boot context limit
BOOT_CONTEXT_HARD_LIMIT = 150

# Canonical boot context only. Entry adapters such as .agent/AGENTS.md are not
# counted because boot-manifest.md is the runtime authority.
BOOT_FILES = [
    ".agent/01-core/boot-manifest.md",
    ".agent/VERSION",
    ".agent/04-memory/project-context.md",
    ".agent/04-memory/learned-mistakes.md",
    ".agent/04-memory/active-tasks.md",
]


def test_gov_t03_adr_structure():
    """GOV-T03: Verify ADRs follow the required format.

    Each ADR must contain: Context, Decision, Consequences.
    Template entries are skipped.
    """
    path = Path(".agent/04-memory/decisions.md")
    if not path.exists():
        return SKIP_EXPECTED, "GOV-T03: decisions.md not found — no ADRs to validate."

    content = path.read_text(encoding="utf-8")
    adrs = re.findall(r"## .*?(ADR-\d+)(?::|\s)", content)

    if not adrs:
        return SKIP_EXPECTED, "GOV-T03: No ADR entries found."

    real_adrs = 0
    incomplete = []
    for adr in adrs:
        # Find the heading line containing this ADR
        adr_pattern = re.compile(r"## .*?" + re.escape(adr) + r".*", re.MULTILINE)
        match = adr_pattern.search(content)
        if not match:
            continue

        start_pos = match.start()

        # Find the next ## heading or end of file
        next_heading = re.search(r"\n## ", content[match.end():])
        if next_heading:
            end_pos = match.end() + next_heading.start()
        else:
            end_pos = len(content)

        section = content[start_pos:end_pos]

        # Skip template entries
        if "[Architectural Decision Title]" in section:
            continue

        real_adrs += 1
        has_context = "Context" in section
        has_decision = "Decision" in section or "decision" in section
        has_consequences = "Consequences" in section or "consequences" in section

        if not (has_context and has_decision and has_consequences):
            incomplete.append(adr)

    if not real_adrs:
        return SKIP_EXPECTED, "GOV-T03: Only template ADRs found."

    if incomplete:
        return FAIL, (
            f"GOV-T03: Incomplete ADR(s): {', '.join(incomplete)} — "
            "missing required sections."
        )

    return PASS, f"GOV-T03: {real_adrs} ADR(s) follow the standard format."


def test_gov_t04_mistakes_cap():
    """GOV-T04: Verify active mistakes do not exceed the 20-mistake cap."""
    path = Path(".agent/04-memory/learned-mistakes.md")
    if not path.exists():
        return SKIP_EXPECTED, "GOV-T04: learned-mistakes.md not found."

    content = path.read_text(encoding="utf-8")

    # Count rows with Type markers (English format)
    type_pattern = r"\[Type [ABC]\]"
    rows = [line for line in content.split("\n")
            if line.strip().startswith("|") and re.search(type_pattern, line)]

    if len(rows) > 20:
        return FAIL, (
            f"GOV-T04: Active-mistake cap exceeded "
            f"(current: {len(rows)} | cap: 20)."
        )

    return PASS, f"GOV-T04: Active mistakes under control (current: {len(rows)})."


def test_gov_t05_handoff_validity():
    """GOV-T05: Verify mandatory memory files exist and are non-empty."""
    required = [
        "project-context.md",
        "learned-mistakes.md",
        "active-tasks.md",
        "decisions.md",
    ]

    memory_dir = Path(".agent/04-memory")
    if not memory_dir.exists():
        return FAIL, "GOV-T05: Memory directory .agent/04-memory/ not found."

    missing = []
    empty = []
    for name in required:
        fp = memory_dir / name
        if not fp.exists():
            missing.append(name)
        elif fp.stat().st_size < 10:
            empty.append(name)

    if missing:
        return FAIL, f"GOV-T05: Missing memory file(s): {', '.join(missing)}"
    if empty:
        return FAIL, f"GOV-T05: Empty memory file(s): {', '.join(empty)}"

    return PASS, "GOV-T05: All mandatory memory files present and non-empty."


def test_gov_t11_boot_context_budget():
    """GOV-T11: Verify canonical Boot Context stays within the v8 release budget."""
    total_lines = 0
    missing = []
    file_stats = []

    for rel_path in BOOT_FILES:
        fp = Path(rel_path)
        if not fp.exists():
            missing.append(rel_path)
            continue
        lines = fp.read_text(encoding="utf-8").count("\n") + 1
        total_lines += lines
        file_stats.append((rel_path, lines))

    if missing:
        return FAIL, "GOV-T11: Boot files missing: " + ", ".join(missing)

    detail = "; ".join(
        f"{name.split('/')[-1]}={count}" for name, count in file_stats
    )

    if total_lines > BOOT_CONTEXT_HARD_LIMIT:
        return FAIL, (
            f"GOV-T11: Canonical boot context {total_lines} lines exceeds "
            f"release ceiling {BOOT_CONTEXT_HARD_LIMIT}. [{detail}]"
        )

    return PASS, (
        f"GOV-T11: Canonical boot context {total_lines} lines is within "
        f"release ceiling {BOOT_CONTEXT_HARD_LIMIT}. [{detail}]"
    )


def test_gov_t37_merge_safe_boot_memory():
    """GOV-T37: Canonical Boot Memory must exclude volatile VCS state."""
    files = [
        Path(".agent/04-memory/project-context.md"),
        Path(".agent/04-memory/active-tasks.md"),
    ]

    violations = []
    field_patterns = [
        re.compile(r"^\s*-\s*\*\*(?:Branch|PR|Main):\*\*", re.MULTILINE),
        re.compile(r"^\s*(?:Branch|PR|Main)\s*:", re.MULTILINE),
    ]
    phrase_patterns = [
        re.compile(r"\bprepare\s+PR\s*#?\d*", re.IGNORECASE),
        re.compile(r"\bmerge\s+PR\s*#?\d*", re.IGNORECASE),
        re.compile(r"\bawaiting\s+(?:final\s+)?(?:done-state\s+)?CI\b", re.IGNORECASE),
        re.compile(r"\brun\s+(?:final\s+)?done-state\s+CI\b", re.IGNORECASE),
    ]

    for path in files:
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        for pattern in field_patterns + phrase_patterns:
            match = pattern.search(content)
            if match:
                violations.append(f"{path.name}: {match.group(0)!r}")

    if violations:
        return FAIL, (
            "GOV-T37: volatile VCS state found in Boot Memory: "
            + "; ".join(violations)
        )

    return PASS, "GOV-T37: Boot Memory is merge-safe and free of volatile VCS state."
