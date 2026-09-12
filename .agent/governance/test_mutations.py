"""AOS Governance — Mutation Tests (v8.0-dev)

Proves that governance checks actually FAIL when violations are introduced.
A check that never fails is a rubber-stamp — mutation tests prevent that.

Usage:
  python test_mutations.py
"""
import sys
import shutil
import tempfile
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Add governance dir to path
gov_dir = str(Path(__file__).parent)
if gov_dir not in sys.path:
    sys.path.insert(0, gov_dir)


def _backup_and_write(path, content):
    """Backup original file and write mutation content."""
    backup = path.with_suffix(path.suffix + ".mutation_backup")
    if path.exists():
        shutil.copy2(path, backup)
    path.write_text(content, encoding="utf-8")
    return backup


def _restore(path, backup):
    """Restore original file from backup."""
    if backup.exists():
        shutil.copy2(backup, path)
        backup.unlink()
    elif path.exists():
        path.unlink()


def run_mutation(name, setup_fn, check_fn, expect_fail=True):
    """Run a single mutation test."""
    backups = []
    try:
        backups = setup_fn()
        result = check_fn()

        if isinstance(result, tuple):
            status = result[0]
            msg = result[1]
        else:
            status = "ERROR"
            msg = f"Bad return: {result}"

        if expect_fail:
            # We expect the check to FAIL
            if status == "FAIL":
                print(f"  ✅ MUTATION {name}: Check correctly detected the violation.")
                return True
            else:
                print(f"  ❌ MUTATION {name}: Check DID NOT detect violation! Got: [{status}] {msg}")
                return False
        else:
            if status == "PASS":
                print(f"  ✅ MUTATION {name}: Check correctly passed after fix.")
                return True
            else:
                print(f"  ❌ MUTATION {name}: Expected PASS but got: [{status}] {msg}")
                return False
    except Exception as e:
        print(f"  💥 MUTATION {name}: Crashed: {e}")
        return False
    finally:
        for path, backup in backups:
            _restore(path, backup)


def mut_t04_exceed_mistakes_cap():
    """Mutate learned-mistakes.md to have 25 mistakes (exceeds cap of 20)."""
    from test_memory import test_gov_t04_mistakes_cap
    path = Path(".agent/04-memory/learned-mistakes.md")

    def setup():
        rows = "\n".join(
            f"| {i:02d} | 2026-01-01 | [Type B] | Test mistake {i} | Fix {i} | 1/3 |"
            for i in range(1, 26)
        )
        content = f"# Learned Mistakes\n\n| # | Date | Type | Mistake | Fix | Rep |\n|---|------|------|---------|-----|-----|\n{rows}\n"
        backup = _backup_and_write(path, content)
        return [(path, backup)]

    return run_mutation("T04-EXCEED-CAP", setup, test_gov_t04_mistakes_cap)


def mut_t05_missing_memory_file():
    """Mutate by temporarily renaming a required memory file."""
    from test_memory import test_gov_t05_handoff_validity
    path = Path(".agent/04-memory/decisions.md")
    hidden = path.with_suffix(".md.mutation_hidden")

    def setup():
        if path.exists():
            shutil.move(str(path), str(hidden))
        return [(path, hidden)]

    return run_mutation("T05-MISSING-FILE", setup, test_gov_t05_handoff_validity)


def mut_t10_incomplete_adr():
    """Mutate decisions.md to have an ADR missing required sections."""
    from test_rules import test_gov_t10_decision_consistency
    path = Path(".agent/04-memory/decisions.md")

    def setup():
        content = """# Decisions

## 🏛️ ADR-099: Incomplete Test Decision
* **Date**: 2026-01-01
* **Status**: Approved
* **Context & problem**:
  This ADR is intentionally missing Decision and Consequences sections.
"""
        backup = _backup_and_write(path, content)
        return [(path, backup)]

    return run_mutation("T10-INCOMPLETE-ADR", setup, test_gov_t10_decision_consistency)


def mut_t10_no_adr_with_rules():
    """Mutate: rules exist but no ADR recorded."""
    from test_rules import test_gov_t10_decision_consistency
    path = Path(".agent/04-memory/decisions.md")

    def setup():
        content = "# Decisions\n\nNo decisions recorded yet.\n"
        backup = _backup_and_write(path, content)
        return [(path, backup)]

    return run_mutation("T10-NO-ADR-WITH-RULES", setup, test_gov_t10_decision_consistency)


def mut_t03_bad_adr_format():
    """Mutate: ADR exists but missing Consequences section."""
    from test_memory import test_gov_t03_adr_structure
    path = Path(".agent/04-memory/decisions.md")

    def setup():
        content = """# Decisions

## 🏛️ ADR-099: Bad Format Decision
* **Date**: 2026-01-01
* **Status**: Approved
* **Context & problem**:
  Some context here.
* **Approved decision**:
  Some decision here.
"""
        backup = _backup_and_write(path, content)
        return [(path, backup)]

    return run_mutation("T03-BAD-ADR-FORMAT", setup, test_gov_t03_adr_structure)


def mut_t11_boot_too_large():
    """Mutate: inflate boot-manifest.md beyond hard limit."""
    from test_memory import test_gov_t11_boot_context_budget
    path = Path(".agent/01-core/boot-manifest.md")

    def setup():
        filler = "\n".join(f"# Filler line {i}" for i in range(400))
        content = f"# Inflated Boot Manifest\n\n{filler}\n"
        backup = _backup_and_write(path, content)
        return [(path, backup)]

    return run_mutation("T11-BOOT-TOO-LARGE", setup, test_gov_t11_boot_context_budget)


if __name__ == "__main__":
    print("🧬 [AOS v8.0-dev] Running Mutation Tests...")
    print("=" * 60)
    print("Each test introduces a deliberate violation and verifies")
    print("the governance check correctly detects it.\n")

    mutations = [
        mut_t04_exceed_mistakes_cap,
        mut_t05_missing_memory_file,
        mut_t10_incomplete_adr,
        mut_t10_no_adr_with_rules,
        mut_t03_bad_adr_format,
        mut_t11_boot_too_large,
    ]

    passed = 0
    failed = 0
    for mut_fn in mutations:
        if mut_fn():
            passed += 1
        else:
            failed += 1

    print(f"\n{'=' * 60}")
    print(f"📊 Mutations: {passed} detected / {failed} missed / {len(mutations)} total")

    if failed > 0:
        print("🚨 Some mutations were NOT detected — governance has gaps!")
        sys.exit(1)
    else:
        print("🎉 All mutations correctly detected — no rubber-stamps!")
        sys.exit(0)
