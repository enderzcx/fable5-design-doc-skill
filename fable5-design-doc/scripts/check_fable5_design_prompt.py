#!/usr/bin/env python3
import re
import sys
from pathlib import Path


REQUIRED_PATTERNS = {
    "short launch prompt": r"^##\s+Short Launch Prompt\s*$",
    "full prompt": r"^##\s+Full Prompt\s*$",
    "design target": r"^##\s+Design Target\s*$",
    "confirmed boundaries": r"^##\s+Confirmed Boundaries\s*$",
    "fable5 decision authority": r"^##\s+Fable5 Decision Authority\s*$",
    "source material": r"^##\s+Source Material\s*$",
    "final design document requirements": r"^##\s+Final Design Document Requirements\s*$",
    "validation requirements": r"^##\s+Validation Requirements\s*$",
    "strict non-goals": r"^##\s+Strict Non-Goals\s*$",
    "output rules": r"^##\s+Output Rules\s*$",
}

PLACEHOLDER_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_fable5_design_prompt.py <prompt-doc.md>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"missing file: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    missing = [
        name
        for name, pattern in REQUIRED_PATTERNS.items()
        if not re.search(pattern, text, flags=re.MULTILINE)
    ]
    placeholders = sorted(set(PLACEHOLDER_RE.findall(text)))

    if missing:
        print("missing required sections:")
        for name in missing:
            print(f"- {name}")

    if placeholders:
        print("unresolved placeholders:")
        for placeholder in placeholders:
            print(f"- {placeholder}")

    if missing or placeholders:
        return 1

    print(f"ok: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
