"""AOS v8 sanitized installer for consumer projects.

Copies reusable runtime assets while deliberately excluding source-project
memory, Project Profile, current Task Contract, and generated evidence.

Usage:
  python .agent/install.py /path/to/target-project
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SOURCE_ROOT = Path(__file__).resolve().parent.parent
SOURCE_AGENT = SOURCE_ROOT / ".agent"

RUNTIME_DIRS = [
    "01-core",
    "02-rules",
    "03-workflows",
    "05-references",
    "06-templates",
    "governance",
    "adr",
]

RUNTIME_FILES = [
    "INDEX.md",
    "AGENTS.md",
    "VERSION",
]

ROOT_ADAPTERS = [
    "AGENTS.md",
    "CLAUDE.md",
    ".cursorrules",
]

TECHNOLOGY_PROFILES = SOURCE_AGENT / "profiles" / "technology"
EVIDENCE_README = SOURCE_AGENT / "evidence" / "README.md"


class InstallError(ValueError):
    pass


def _copy_dir(source: Path, target: Path) -> None:
    if not source.exists():
        raise InstallError(f"Missing runtime directory: {source}")
    shutil.copytree(source, target, dirs_exist_ok=True)


def _copy_file(source: Path, target: Path) -> None:
    if not source.exists():
        raise InstallError(f"Missing runtime file: {source}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def install(target_root: Path) -> dict:
    target_root = target_root.resolve()
    if target_root == SOURCE_ROOT.resolve():
        raise InstallError("Refusing to install consumer runtime over the AOS source repository.")

    target_agent = target_root / ".agent"
    target_agent.mkdir(parents=True, exist_ok=True)

    for name in RUNTIME_DIRS:
        _copy_dir(SOURCE_AGENT / name, target_agent / name)

    for name in RUNTIME_FILES:
        _copy_file(SOURCE_AGENT / name, target_agent / name)

    if TECHNOLOGY_PROFILES.exists():
        _copy_dir(
            TECHNOLOGY_PROFILES,
            target_agent / "profiles" / "technology",
        )

    if EVIDENCE_README.exists():
        _copy_file(
            EVIDENCE_README,
            target_agent / "evidence" / "README.md",
        )

    for name in ROOT_ADAPTERS:
        source = SOURCE_ROOT / name
        if source.exists():
            _copy_file(source, target_root / name)

    copilot = SOURCE_ROOT / ".github" / "copilot-instructions.md"
    if copilot.exists():
        _copy_file(
            copilot,
            target_root / ".github" / "copilot-instructions.md",
        )

    excluded = [
        ".agent/04-memory/",
        ".agent/profiles/project.json",
        ".agent/task-contracts/current.json",
        ".agent/evidence/current.json",
        ".agent/evidence/history/",
    ]

    return {
        "target": str(target_root),
        "runtime_installed": True,
        "excluded_source_state": excluded,
        "next": "Run .agent/03-workflows/init-project.md in the target repository.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Install sanitized AOS runtime")
    parser.add_argument("target", help="Target project root")
    args = parser.parse_args()

    target = Path(args.target)
    target.mkdir(parents=True, exist_ok=True)

    try:
        result = install(target)
    except InstallError as exc:
        print(f"INSTALL FAILED: {exc}")
        return 1

    print("AOS runtime installed.")
    print(f"Target: {result['target']}")
    print("Source-specific state excluded:")
    for item in result["excluded_source_state"]:
        print(f"  - {item}")
    print(result["next"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
