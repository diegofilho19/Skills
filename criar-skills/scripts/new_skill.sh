#!/usr/bin/env bash
# Create a new Antigravity skill from the standard skeleton.
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: new_skill.sh <name> [--workspace <repo>] [--force]

  <name>               lowercase-hyphenated skill name (e.g. db-migrations)
  --workspace <repo>   create in <repo>/.agents/skills/ instead of globally
  --force              overwrite an existing SKILL.md
  -h, --help           show this help

Global location: ~/.gemini/config/skills/<name>/SKILL.md
EOF
}

name=""
repo=""
force=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help) usage; exit 0 ;;
    --workspace)
      [[ $# -ge 2 ]] || { echo "error: --workspace needs a path" >&2; exit 2; }
      repo="$2"; shift 2 ;;
    --force) force=1; shift ;;
    -*) echo "error: unknown flag $1" >&2; usage >&2; exit 2 ;;
    *)
      [[ -z "$name" ]] || { echo "error: only one name allowed" >&2; exit 2; }
      name="$1"; shift ;;
  esac
done

[[ -n "$name" ]] || { usage >&2; exit 2; }

if [[ ! "$name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "error: '$name' must be lowercase-hyphenated (a-z, 0-9, single dashes)" >&2
  exit 2
fi

if [[ -n "$repo" ]]; then
  [[ -d "$repo" ]] || { echo "error: repo not found: $repo" >&2; exit 2; }
  base="$repo/.agents/skills"
else
  base="$HOME/.gemini/config/skills"
fi

dir="$base/$name"
skill="$dir/SKILL.md"

if [[ -e "$skill" && $force -ne 1 ]]; then
  echo "error: $skill already exists (use --force to overwrite)" >&2
  exit 1
fi

mkdir -p "$dir/references" "$dir/scripts"

if [[ ! -e "$skill" || $force -eq 1 ]]; then
  cat > "$skill" <<EOF
---
name: $name
description: >-
  <What it produces, third person>. Use when <trigger>, <trigger>, or when the
  user says "<literal phrase>".
---

# $name

<One sentence: the decision or output this skill guarantees.>

## When this applies

- <Situation>

Not for: <adjacent case>.

## Procedure

1. <Action with a concrete tool or command>.
2. <Action>.

## Verification

Run \`<command>\`. Success looks like:

\`\`\`text
<expected output>
\`\`\`
EOF
fi

echo "created: $skill"
echo "next:"
echo "  1. write the description (<= 60 words, include the user's literal words)"
echo "  2. write the body (<= 120 lines; move detail to references/)"
echo "  3. python3 \"$(dirname "$0")/check_skill.py\" \"$dir\""
