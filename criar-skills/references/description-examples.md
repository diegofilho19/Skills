# Description examples

The description is the trigger and the per-turn cost. Judge it by two questions:
does it fire on the right prompt, and does it stay quiet on the wrong one?

## Pairs

### 1

Bad: `Helps with tests.`

Good: `Writes and fixes pytest tests for this repo, including fixtures and
parametrization. Use when adding coverage, fixing a failing test, or when the
user says "escrever teste", "teste quebrado".`

Why: names the framework, the action, and the exact triggers.

### 2

Bad: `A comprehensive skill for API development, debugging, documentation, and
deployment.`

Good: `Reviews HTTP handlers for auth, input validation, and error mapping. Use
when reviewing a route, controller, or endpoint before merge.`

Why: one job, one boundary.

### 3

Bad: `Use for React.`

Good: `Builds React components with the project's server-component and Tailwind
conventions. Use when creating, splitting, or refactoring a component under
src/app. Not for styling-only changes.`

Why: scopes both the trigger and the exclusion.

### 4

Bad: `Token saving.`

Good: `Produces terse, answer-first replies with no preamble or recap. Use when
the user asks to be direct, brief, or to save tokens ("sem enrolação",
"objetivo", "curto").`

Why: includes the literal phrases a user types, in their language.

### 5

Bad: `Database expert.`

Good: `Writes reversible SQL migrations for PostgreSQL with expand-and-contract
and CONCURRENTLY indexes. Use when altering columns, indexes, or constraints in
existing tables.`

Why: replaces a role with a procedure and constraints.

### 6

Bad: `Improves code quality.`

Good: `Removes dead code and duplicated helpers after a refactor, then runs the
project linter. Use when the user asks to clean up a file or module.`

Why: "quality" is unmeasurable; "removes X then runs Y" is testable.

### 7

Bad: `Skill for git.`

Good: `Prepares commits: groups staged changes, writes a conventional-commit
message, and checks for secrets. Use when the user asks to commit or review a
diff before committing.`

Why: a bounded workflow, not a topic.

### 8

Bad: `Advanced debugging with AI.`

Good: `Traces a runtime error from the failing test to the first bad frame, then
proposes the smallest fix. Use when given a stack trace, a red test, or "não sei
por que quebrou".`

Why: input -> output, with the user's own phrasing.

### 9

Bad: `Frontend performance.`

Good: `Finds render and bundle regressions in this Next.js app using the build
output and React Profiler. Use when a page is slow or the bundle grows.`

Why: names the measurement, not the aspiration.

### 10

Bad: `Security.`

Good: `Audits a diff for injection, auth bypass, and secret leakage, and blocks
the merge on findings. Use before merging changes that touch auth, SQL, or env
files.`

Why: scope, method, and consequence.

## Test

For each description, write two prompts:

1. One that must trigger it.
2. One that is adjacent and must not.

If the second triggers, add a boundary sentence. If the first does not, add the
literal words the prompt uses.
