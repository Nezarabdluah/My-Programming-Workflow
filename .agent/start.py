"""AOS Quick Start — prints the full boot prompt ready to paste into any AI chat.

Usage:
  python .agent/start.py          → prints boot prompt to screen
  python .agent/start.py --copy   → copies to clipboard (Windows)
  python .agent/start.py --check  → runs governance checks
"""
import sys
import subprocess
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

def main():
    root = Path(__file__).parent.parent
    agent_dir = root / ".agent"

    if "--check" in sys.argv:
        subprocess.run([sys.executable, str(agent_dir / "governance" / "runner.py")], cwd=str(root))
        return

    # Boot files to include
    boot_files = [
        agent_dir / "01-core" / "boot-manifest.md",
        agent_dir / "04-memory" / "project-context.md",
        agent_dir / "04-memory" / "learned-mistakes.md",
        agent_dir / "04-memory" / "active-tasks.md",
        agent_dir / "VERSION",
    ]

    prompt_parts = []
    prompt_parts.append("# AOS — Agent Operating System (Auto-loaded Boot Prompt)\n")
    prompt_parts.append("> Follow these instructions exactly. They are your operating contract.\n")

    for f in boot_files:
        if f.exists():
            content = f.read_text(encoding="utf-8").strip()
            rel = f.relative_to(root)
            prompt_parts.append(f"\n---\n## File: {rel}\n\n{content}\n")
        else:
            prompt_parts.append(f"\n> ⚠️ Missing: {f.relative_to(root)}\n")

    prompt_parts.append("\n---\n## Quick Reference\n")
    prompt_parts.append("- Wiring Registry: `.agent/01-core/wiring-registry.md`")
    prompt_parts.append("- Master Pipeline: `.agent/03-workflows/master-pipeline/00-coordinator.md`")
    prompt_parts.append("- Governance: `python .agent/governance/runner.py`")
    prompt_parts.append("- Knowledge Index: `.agent/05-references/books/00-master-index.md`\n")

    full_prompt = "\n".join(prompt_parts)

    if "--copy" in sys.argv:
        try:
            process = subprocess.Popen(["clip"], stdin=subprocess.PIPE)
            process.communicate(full_prompt.encode("utf-16le"))
            print(f"✅ Boot prompt copied to clipboard! ({len(full_prompt)} chars)")
            print("   Paste it into your AI chat to start working with AOS.")
        except Exception as e:
            print(f"❌ Clipboard failed: {e}")
            print(full_prompt)
    else:
        print(full_prompt)
        print(f"\n{'='*60}")
        print(f"📋 {len(full_prompt)} chars | Tip: use --copy to copy to clipboard")
        print(f"🔍 Use --check to run governance checks")


if __name__ == "__main__":
    main()
