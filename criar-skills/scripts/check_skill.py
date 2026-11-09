#!/usr/bin/env python3
"""Validate an Antigravity skill folder (SKILL.md frontmatter, size, links)."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MAX_DESC_WORDS = 60
MAX_BODY_LINES = 120
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)#]+\.md)(?:#[^)]*)?\)")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    data: dict[str, str] = {}
    key = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[0] not in " \t" and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value in ("", ">-", ">", "|", "|-"):
                data[key] = ""
            else:
                data[key] = value.strip("'\"")
        elif key and line[0] in " \t":
            data[key] = (data[key] + " " + line.strip()).strip()
    return data, body


def unquote(value: str) -> str:
    return value.strip().strip("'\"")


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Check a skill folder for Antigravity compatibility."
    )
    ap.add_argument("skill_dir", type=Path, help="path to the skill folder")
    ap.add_argument(
        "--strict",
        action="store_true",
        help="treat warnings as errors (for CI)",
    )
    args = ap.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    skill_dir: Path = args.skill_dir.resolve()
    skill = skill_dir / "SKILL.md"

    if not skill.is_file():
        print(f"ERROR: {skill} not found", file=sys.stderr)
        return 1

    text = skill.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    if not fm:
        errors.append("SKILL.md must start with a YAML frontmatter block")

    name = unquote(fm.get("name", ""))
    if name:
        if not NAME_RE.match(name):
            errors.append(f"name '{name}' must be lowercase-hyphenated")
        if name != skill_dir.name:
            warnings.append(
                f"name '{name}' differs from folder '{skill_dir.name}' "
                "(folder name is the fallback)"
            )
    else:
        warnings.append("no explicit 'name'; the folder name will be used")

    desc = unquote(fm.get("description", ""))
    if not desc:
        errors.append("description is required; it is the trigger")
    else:
        words = len(desc.split())
        if words > MAX_DESC_WORDS:
            errors.append(
                f"description has {words} words; keep it <= {MAX_DESC_WORDS}"
            )
        lower = desc.lower()
        if not re.search(r"\buse (when|for|before|after|during|on)\b", lower):
            warnings.append("description has no 'Use when ...' / 'Use for ...' clause")
        if not re.search(r"[a-z]{4}", lower):
            errors.append("description looks empty or non-textual")

    body_lines = body.splitlines()
    if len(body_lines) > MAX_BODY_LINES:
        warnings.append(
            f"body has {len(body_lines)} lines (> {MAX_BODY_LINES}); "
            "move detail to references/"
        )

    for target in LINK_RE.findall(body):
        path = (skill_dir / target).resolve()
        if not path.is_file():
            errors.append(f"broken link: {target}")

    scripts = sorted((skill_dir / "scripts").glob("*")) if (skill_dir / "scripts").is_dir() else []
    for script in scripts:
        if script.is_file() and not script.suffix:
            warnings.append(f"script without extension: {script.name} (use .sh/.py)")

    for label, items in (("ERROR", errors), ("WARN", warnings)):
        for item in items:
            print(f"{label}: {item}")

    if errors or (args.strict and warnings):
        return 1
    print(f"ok: {skill_dir.name} ({len(body_lines)} body lines, {len(desc.split())} desc words)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
