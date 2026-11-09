---
name: criar-skills
description: >-
  Creates, reviews, and fixes Antigravity Agent Skills (SKILL.md with
  references/ and scripts/). Use when the user asks to build, improve, debug, or
  standardize a skill, or wants reusable agent behavior ("criar skill", "nova
  skill", "melhorar skill").
---

# Skill Authoring (Antigravity)

## Decide first: rule or skill?

- Invariant that applies every turn ("use zod", "never import internal/") ->
  **rule** in `AGENTS.md` or `GEMINI.md`.
- Multi-step procedure used sometimes -> **skill**.
- One deterministic operation -> **script** called by a skill.

Rules cost tokens every turn. Skills cost one description line until activated.

## Locations

| Scope | Path |
| --- | --- |
| Global (all projects) | `~/.gemini/config/skills/<name>/SKILL.md` |
| Workspace (committed) | `<repo>/.agents/skills/<name>/SKILL.md` |

Antigravity also reads `.agent/skills/` for compatibility. One skill per folder.

## Required anatomy

```text
<name>/
  SKILL.md          # required: frontmatter + procedure
  references/       # optional: material read only on demand
  scripts/          # optional: deterministic helpers
  resources/        # optional: templates, schemas, fixtures
```

Frontmatter supports `name` and `description` only. `name` is optional and
defaults to the folder name; use lowercase-hyphenated.

## Write the description

It is the only part loaded on every turn, and it is the trigger. Formula:

```text
<What it produces, in third person>. Use when <trigger 1>, <trigger 2>, or when
the user says "<phrase the user would actually type>".
```

Rules:

- Third person, imperative-free ("Produces X", not "I will produce X").
- <= 60 words. Every extra word is paid on every turn.
- Include the words the user types, in the user's language (pt-BR + English).
- State the boundary: what it is *not* for, when that prevents false triggers.
- No marketing adjectives ("powerful", "comprehensive", "robust").

Good: `Generates database migrations with the project's expand-and-contract
pattern. Use when adding or changing a column, index, or constraint.`

Bad: `A powerful, comprehensive skill that helps with all database tasks.`

More pairs: [references/description-examples.md](references/description-examples.md).

## Write the body

- Start with the decision the agent must make, not with background.
- One instruction per bullet. Testable verbs: "Run", "Read", "Do not", "Stop".
- Include a decision tree when there are 3+ branches.
- Include the verification step and its expected output.
- Delete anything the model already knows. No tutorials, no copied docs.
- Cross-reference rules instead of restating them.
- No hidden state: the skill must work after a context reset.

## Size discipline

| Part | Limit | Why |
| --- | --- | --- |
| description | 60 words | paid every turn |
| SKILL.md | 120 lines / ~800 tokens | paid on activation |
| references/* | no limit | paid only when linked and read |
| scripts/* | short, `--help`, exit codes | run, don't read |

If SKILL.md grows past 120 lines, move examples, long tables, and edge cases
into `references/` and link them from the body.

## Scripts

- `--help` prints usage and exits 0.
- No interactive prompts; read flags or stdin.
- Exit non-zero on failure, with one line on stderr.
- Idempotent: safe to run twice.
- Tell the agent to run `--help` before reading the source.

## Procedure to create a skill

1. `scripts/new_skill.sh <name> [--workspace <repo>]`
2. Fill the description using the formula above.
3. Write the body against the checklist below.
4. `scripts/check_skill.py <skill-dir>` -> fix every ERROR.
5. Test: start a fresh session, use a prompt that should trigger it, and one that
   should not. Adjust the description, not the body, for trigger problems.

## Review checklist

Fail any item -> fix before shipping.

1. Does the description trigger on the intended prompts and stay quiet on
   adjacent ones?
2. Can the agent execute every step with the tools it actually has?
3. Is each instruction verifiable (a command, a file, an output)?
4. Does any step merely restate general coding knowledge?
5. Does it work without chat history?
6. Is the token cost of the body justified by the reliability it adds?
7. Does it contradict the global rules or another skill?

## Anti-patterns

- Encyclopedia skill: one skill covering five jobs.
- Vague description: "helps with code".
- Copy-pasted framework docs that will drift.
- Steps that need a human to interpret the result.
- Magic constants with no source.
- 500-line SKILL.md that could be 80 lines + one reference.
- Duplicating a rule that is already always-on.
