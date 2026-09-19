"""End-to-end smoke test for the one-command consumer bootstrap."""

import importlib.util
import json
import tempfile
from pathlib import Path


def load_bootstrap():
    path = Path(".agent/bootstrap.py")
    spec = importlib.util.spec_from_file_location("aos_bootstrap_smoke", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    bootstrap = load_bootstrap()

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "consumer-web-app"
        root.mkdir(parents=True)

        (root / "package.json").write_text(
            json.dumps({
                "scripts": {
                    "build": "vite build",
                    "test": "vitest run",
                    "lint": "eslint ."
                }
            }),
            encoding="utf-8",
        )
        (root / "tsconfig.json").write_text("{}", encoding="utf-8")

        result = bootstrap.bootstrap(root, verify=True)

        if result.get("status") != "READY":
            raise SystemExit(f"bootstrap did not finish READY: {result}")
        verification = result.get("verification") or {}
        if verification.get("status") != "PASS":
            raise SystemExit(f"consumer verification failed: {verification}")

        print("BOOTSTRAP SMOKE PASS")
        print(f"project_type={result['project_type']}")
        print(f"languages={','.join(result['languages'])}")
        print(f"commands={','.join(result['commands'])}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
