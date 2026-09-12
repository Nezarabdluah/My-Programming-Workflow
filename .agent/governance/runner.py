"""AOS Governance Runner — v8.0-dev

Runs all governance tests and produces structured results.
Supports 5 official result statuses per ADR-006/v8 plan:
  PASS, FAIL, SKIP_EXPECTED, SKIP_UNSUPPORTED, ERROR

Usage:
  python runner.py          # human-readable output
  python runner.py --json   # machine-readable JSON output
"""

import sys
import json
import importlib
import traceback
from pathlib import Path
from datetime import datetime, timezone

# Windows console guard: force UTF-8
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# --- Official result statuses ---
PASS = "PASS"
FAIL = "FAIL"
SKIP_EXPECTED = "SKIP_EXPECTED"       # check not applicable with evidence
SKIP_UNSUPPORTED = "SKIP_UNSUPPORTED" # environment cannot run check
ERROR = "ERROR"                        # checker itself crashed

TEST_MODULES = ["test_state", "test_rules", "test_memory"]

ICONS = {
    PASS: "✅",
    FAIL: "❌",
    SKIP_EXPECTED: "⏭️",
    SKIP_UNSUPPORTED: "⚠️",
    ERROR: "💥",
}


def run_all_tests(json_output=False):
    current_dir = str(Path(__file__).parent)
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)

    results = []
    now = datetime.now(timezone.utc).isoformat()

    if not json_output:
        print("🔍 [AOS v8.0-dev] Running governance tests...")
        print("=" * 60)

    for module_name in TEST_MODULES:
        try:
            module = importlib.import_module(module_name)
            for attr_name in sorted(dir(module)):
                if not attr_name.startswith("test_"):
                    continue
                test_func = getattr(module, attr_name)
                try:
                    result = test_func()
                    # Support both old (bool, msg) and new (status, msg) return
                    if isinstance(result, tuple) and len(result) == 2:
                        status_or_bool, msg = result
                        if isinstance(status_or_bool, bool):
                            status = PASS if status_or_bool else FAIL
                        elif status_or_bool in (PASS, FAIL, SKIP_EXPECTED,
                                                SKIP_UNSUPPORTED, ERROR):
                            status = status_or_bool
                        else:
                            status = ERROR
                            msg = f"Unknown return type: {status_or_bool}"
                    else:
                        status = ERROR
                        msg = f"Bad return format: {result!r}"
                except Exception as e:
                    status = ERROR
                    msg = f"{attr_name} crashed: {e}"

                entry = {
                    "test": attr_name,
                    "module": module_name,
                    "status": status,
                    "message": msg,
                    "timestamp": now,
                }
                results.append(entry)

                if not json_output:
                    icon = ICONS.get(status, "?")
                    print(f"  {icon} [{status:18s}] {attr_name}: {msg}")

        except Exception as e:
            entry = {
                "test": module_name,
                "module": module_name,
                "status": ERROR,
                "message": f"Module import failed: {e}",
                "timestamp": now,
            }
            results.append(entry)
            if not json_output:
                print(f"  💥 [ERROR] {module_name}: {e}")

    # Summary
    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1

    summary = {
        "total": len(results),
        "counts": counts,
        "all_hard_gates_pass": counts.get(FAIL, 0) == 0 and counts.get(ERROR, 0) == 0,
        "timestamp": now,
    }

    if json_output:
        output = {"summary": summary, "results": results}
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        print("=" * 60)
        parts = [f"{ICONS.get(s, '?')} {s}: {c}" for s, c in sorted(counts.items())]
        print(f"📊 Summary: {' | '.join(parts)}")
        if summary["all_hard_gates_pass"]:
            print("\n🎉 All hard gates clear.")
        else:
            print("\n🚨 Hard gate failures detected.")

    sys.exit(0 if summary["all_hard_gates_pass"] else 1)


if __name__ == "__main__":
    json_mode = "--json" in sys.argv
    run_all_tests(json_output=json_mode)
