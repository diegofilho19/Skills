---
name: economia-de-tokens
description: >-
  Cuts input tokens when exploring or editing a codebase: search before
  reading, read narrow ranges, batch tool calls, avoid re-reads, and stop when
  the task is done. Use for coding tasks in large repos, long sessions, or when
  the user mentions context, token cost, or a slow agent.
---

# Context Budget

Input tokens dominate cost in agent sessions. Spend them on the smallest slice
of the repo that answers the question.

## Budgets per task

| Task | Tool calls | Lines read |
| --- | --- | --- |
| Locate one symbol or file | <= 3 | <= 100 |
| Small fix (1-2 files) | <= 8 | <= 400 |
| Feature (3-6 files) | <= 20 | <= 1500 |
| Refactor across the repo | plan first, then per-file budgets | n/a |

If you exceed the budget, stop and say what is missing. Do not keep reading
hoping for clarity; narrow the question.

## Loop

1. **Search** with output limits:
   `rg -n --max-count 20 -g '!node_modules' -g '!dist' '<pattern>'`
   Use `-l` when you only need file names.
2. **Read the region**, not the file: offset around the match, 20-40 lines.
3. **Edit** with a targeted replacement. Do not rewrite the file.
4. **Verify** with the narrowest command that can fail: one test, `tsc --noEmit`
   on the project, a single lint rule.
5. **Stop** when the acceptance criteria are met.

## Do not

- Read a whole file "to get context" when a symbol search would do.
- Re-read a file you just edited; you already know the change.
- Print tool output verbatim. Extract the 3 lines that matter.
- Spawn a subagent for a one-file change.
- Load skills, references, or docs that are not needed for this step.
- Rebuild or run the full suite to check a typo.
- Repeat a failing command without changing the input.
- Keep a growing todo list in the reply; track it in your head or a scratch file.

## Batching

Independent reads, searches, and greps go in the same turn. Serialize only when
the next call's input depends on the previous output. Each round trip re-sends
context.

## Output filtering

- `| head -50`, `--max-count`, `--stat`, `-l`, `-q`.
- Test failures: take the first failure block and the summary, not the full log.
- Builds: take the first error and the exit code.
- JSON: `jq '.[0:3]'` or a targeted selector.

## Handoff when context runs out

Write a short state note (10 lines max) and continue from it:

```text
Goal:
Done:
Next:
Blocked by:
Files touched:
Commands that work:
```

Keep it in the repo or `/tmp`, not in the chat history.

## Stop rule

Done means the requested behavior works and the check passes. It does not mean
"the code looks nicer". No drive-by refactors, renames, comment cleanups, or
extra docs unless asked.
