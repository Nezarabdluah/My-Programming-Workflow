import sys
import importlib
from pathlib import Path

# Windows console guard: force UTF-8 so emoji output never crashes cp1256/cp1252 terminals
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Specialized governance test modules
TEST_MODULES = [
    "test_state",
    "test_rules",
    "test_memory"
]

def run_all_tests():
    print("🔍 [AOS v7.0] Running automated governance tests...")
    print("=" * 60)

    success_count = 0
    failure_count = 0
    failures = []

    # Pin the import path to the current folder
    current_dir = str(Path(__file__).parent)
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)

    for module_name in TEST_MODULES:
        try:
            module = importlib.import_module(module_name)
            # Discover and run every test_ function
            for attr_name in dir(module):
                if attr_name.startswith("test_"):
                    test_func = getattr(module, attr_name)
                    print(f"🏃 Running test: {attr_name}...")
                    success, msg = test_func()
                    if success:
                        print(f"✅ {msg}")
                        success_count += 1
                    else:
                        print(f"❌ {msg}")
                        failure_count += 1
                        failures.append((attr_name, msg))
        except Exception as e:
            print(f"💥 Error while running test module {module_name}: {e}")
            failure_count += 1
            failures.append((module_name, str(e)))

    print("=" * 60)
    print(f"📊 Summary: {success_count} passed | {failure_count} failed")

    if failure_count > 0:
        print("\n🚨 Failure details:")
        for name, msg in failures:
            print(f" - {name}: {msg}")
        sys.exit(1)
    else:
        print("\n🎉 All governance tests passed 100%.")
        sys.exit(0)

if __name__ == "__main__":
    run_all_tests()
