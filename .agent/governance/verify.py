"""AOS full verification — governance + mutation checks.

Usage:
  python .agent/governance/verify.py
"""

import subprocess
import sys
from pathlib import Path


def run(script_name):
    script = Path(__file__).with_name(script_name)
    completed = subprocess.run([sys.executable, str(script)], check=False)
    return completed.returncode


def main():
    print("=== AOS Governance ===")
    governance_code = run("runner.py")

    print("\n=== AOS Mutation Verification ===")
    mutation_code = run("test_mutations.py")

    if governance_code != 0 or mutation_code != 0:
        print(
            "\nFULL VERIFICATION FAILED "
            f"(governance={governance_code}, mutations={mutation_code})"
        )
        return 1

    print("\nFULL VERIFICATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
