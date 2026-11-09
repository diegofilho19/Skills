# Claim checklist

Use this when the answer will be acted on, reviewed, or shipped. For casual
chat, the four labels in `SKILL.md` are enough.

## 1. Pre-flight (30 seconds)

- [ ] What did I actually read or run this session? List the paths and outputs.
- [ ] Which names in my answer did **not** appear in that list?
- [ ] For each of those: verify now, or label `NAO VERIFICADO`.
- [ ] Does any number, version, or date come from memory? Verify or drop it.
- [ ] Did I open every URL and file I cite?

## 2. Symbol checklist

| Thing | Verify with | Common hallucination |
| --- | --- | --- |
| Function/method | `rg -n "def name\|function name\|name ="` | right name, wrong module |
| Import path | `rg -n "from .* import"` / read `__init__` | invented submodule |
| CLI flag | `cmd --help` | `--no-cache` vs `--no-cache-dir` |
| Config key | schema file, docs, or runtime error | plausible nesting |
| Env var | `rg -n "process.env\|os.environ"` | invented `APP_*` prefix |
| Package version | lockfile / `npm view` / `pip show` | API that exists only in newer version |
| Endpoint | route file or OpenAPI spec | right path, wrong method |
| Error cause | full stack trace, not the last line | guessing from the message |

## 3. Failure modes to name explicitly

- **Version drift**: the API changed between the version installed and the one in
  your memory. Check the lockfile, not the docs homepage.
- **Renamed symbol**: the concept exists, the name does not. Search for the
  concept, then use the real name.
- **Two similar libraries**: verify the import actually present in the project.
- **Config that is read but not applied**: check the loader, not just the key.
- **Tests that pass for the wrong reason**: read the assertion, not the summary.
- **Silent default**: "it works" may rely on a default the user will change.

## 4. Recovery script

If you already stated something wrong:

```text
Correção: eu disse X. O correto é Y (`path:line`). A causa do erro foi Z.
```

One line, no apology spiral, then continue with the corrected answer.

## 5. When to refuse

Refuse to guess, and say why, when the claim affects:

- production data or migrations;
- authentication, permissions, or secrets;
- money, billing, or quotas;
- legal, medical, or safety outcomes;
- a destructive command (`rm`, `DROP`, `force push`, `--hard reset`).

Offer the exact read-only command that would settle it.
