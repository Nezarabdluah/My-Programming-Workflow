#!/bin/sh
set -eu

# Thin remote launcher. All target inspection and writes stay in .agent/bootstrap.py.
AOS_REPO_URL="${AOS_REPO_URL:-https://github.com/Nezarabdluah/My-Programming-Workflow.git}"
AOS_REF="${AOS_REF:-main}"
AOS_TARGET="${AOS_TARGET:-$(pwd -P)}"

if ! command -v git >/dev/null 2>&1; then
  echo "AOS BOOTSTRAP BLOCKED: git is required." >&2
  exit 2
fi

if command -v python3 >/dev/null 2>&1; then
  AOS_PYTHON=python3
elif command -v python >/dev/null 2>&1; then
  AOS_PYTHON=python
else
  echo "AOS BOOTSTRAP BLOCKED: Python 3 is required." >&2
  exit 2
fi

AOS_TEMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/aos-bootstrap.XXXXXX")
cleanup() {
  rm -rf "$AOS_TEMP_DIR"
}
trap cleanup EXIT HUP INT TERM

git -C "$AOS_TEMP_DIR" init -q
git -C "$AOS_TEMP_DIR" remote add origin "$AOS_REPO_URL"
git -C "$AOS_TEMP_DIR" fetch -q --depth 1 origin "$AOS_REF"
git -C "$AOS_TEMP_DIR" checkout -q --detach FETCH_HEAD

"$AOS_PYTHON" "$AOS_TEMP_DIR/.agent/bootstrap.py" "$AOS_TARGET"
