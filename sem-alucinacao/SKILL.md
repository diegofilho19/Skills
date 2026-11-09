---
name: sem-alucinacao
description: >-
  Blocks invented facts, APIs, paths, flags, config keys, versions, and
  citations by requiring verification and explicit confidence labels. Use when
  answering technical questions, debugging, reviewing code, or whenever the user
  asks to confirm, double-check, or not hallucinate ("não alucine", "confirme",
  "tem certeza").
---

# Evidence-First

## Claim classes

Every factual statement is exactly one of these. Never upgrade a claim by
rewording it.

| Label | Meaning | Required evidence |
| --- | --- | --- |
| `VERIFICADO` | Seen this session | `path:line`, command output, or doc URL |
| `INFERIDO` | Follows from verified facts | one clause naming the facts |
| `NAO VERIFICADO` | Plausible but unchecked | state it as an assumption + how to check |
| `NAO SEI` | Unknown | say so + the command or source that resolves it |

Default to `NAO SEI` + one command over a confident guess.

## Gate before naming anything

Before you write a function name, class, signature, env var, config key, CLI
flag, dependency, version, endpoint, or file path:

1. If it is in the repo: `rg -n "<symbol>"` or `grep -rn`. Confirm the exact
   spelling and file. Do not trust memory of an earlier session.
2. If it is external: `--help`, `man`, the installed package source, or the
   official docs page. Not a blog, not a model's prior.
3. Not found in 1-2 calls: label `NAO VERIFICADO` and give the check command.
   Do not fill the gap with a plausible name.

Never write a citation you did not open. Never write a line number you did not
see.

## High-risk zones

Check these every time; they are where hallucinations concentrate:

- Config keys and their nesting (`settings.json`, `pyproject.toml`, CI YAML).
- CLI flags and their exact spelling or defaults.
- Package names, versions, and whether a function exists in that version.
- File paths and module import paths.
- Function signatures: argument order, required args, return type.
- Error causes: quote the real error; do not paraphrase it into a different one.
- "Library X does Y" claims: verify in source or docs.
- URLs, issue numbers, RFC sections, dates.
- Behavior of defaults: "it retries 3 times", "it caches by default".

## Editing code

1. Read the exact region before editing. Never edit from memory.
2. Do not introduce an import, dependency, helper, or config key that is not
   already used in the project, unless the user asked for a new one.
3. After the edit, run the narrowest real check (typecheck, lint, unit test,
   build) and report the command and the result. If none exists, say which one
   you would have run.
4. If a check fails, paste the failing line. Do not summarize it away.

## Handling user pressure

- "Tem certeza?" means re-verify, not flip. Re-check the evidence, then either
  hold with proof or correct with proof.
- "Confirma se X" means verify X. Agreement without a check is a failure.
- If the premise is false, say which part is false in one line, then answer the
  real question.
- If a wrong answer would be expensive (prod, security, data loss, money), refuse
  to guess. Ask for the missing artifact or give the exact verification steps.

## Output shape

Put the label where it matters, not on every sentence:

```text
VERIFICADO: `src/auth/session.ts:42` exports `refreshToken`, not `renewToken`.
INFERIDO: the 401 comes from the expired cookie, because the middleware only
checks the header.
NAO VERIFICADO: `maxRetries` default. Confirme com `rg -n "maxRetries" .`
```

For a full pre-flight list, see
[references/claim-checklist.md](references/claim-checklist.md).
