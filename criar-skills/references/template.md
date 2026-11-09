# SKILL.md template

Copy, fill, delete what does not apply. Keep the result under 120 lines.

````markdown
---
name: <lowercase-hyphenated>
description: >-
  <What it produces, third person>. Use when <trigger>, <trigger>, or when the
  user says "<literal phrase>".
---

# <Title>

<One sentence: the decision or output this skill guarantees.>

## When this applies

- <Situation>
- <Situation>

Not for: <adjacent case that belongs to another skill or rule>.

## Procedure

1. <Action with a concrete tool or command>.
2. <Action>.
3. <Action>.

## Decision tree

- If <condition A> -> <step>.
- If <condition B> -> <step>.
- Otherwise -> <fallback>.

## Rules

- MUST <constraint>.
- NEVER <failure mode you have seen>.
- Keep <artifact> under <limit>.

## Verification

Run `<command>`. Success looks like:

```text
<expected output>
```

## References

- [<topic>](references/<file>.md): read only when <condition>.
````

## Notes

- `name` is optional; the folder name is the fallback.
- Frontmatter accepts only `name` and `description`.
- Relative links resolve from the skill folder. Use them freely: linked files
  cost nothing until the agent opens them.
- Put the verification command in the body, not only in a reference.
