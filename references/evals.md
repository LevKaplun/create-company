# Testing the roles

Two stages: an eval that tells whether each playbook helps, then two weeks of real use.

## 1. The eval: with and without the playbook

1. **Cases.** 10 to 15 real tasks per role, from questions the owner asked or will ask, with names replaced by
   placeholders. Prompts go in `evals/<role>/cases.json` (`[{"id": "case-01", "prompt": "..."}]`), yes or no checks
   in `evals/<role>/cases.md` (`templates/eval-cases.md`). Keep the last third as a held-out set. Never write a
   company fact or a decision into a check: point to the doc or record.
2. **Runs.** Commit the notebooks first, then `python3 scripts/run_evals.py <company folder> <role>[,<role>] --workers 4`.
   Each case runs headless in fresh sessions: arm A with the playbook preloaded, arm B without it. One run per case
   is enough while iterating; add `--runs 3` before deciding anything. A run takes
   one to ten minutes; three roles with ten cases each are 60 runs, about an hour, and heavy usage on the plan.
3. **Blind grading.** `python3 scripts/blind_pairs.py <company> <role> results-<date> <blind folder outside the company>`
   copies each pair as X and Y in random order and keeps the key apart. A fresh judge (a new agent, with
   `templates/judge-prompt.md`) grades every check and picks the answer the owner would act on with fewer
   corrections. Then `blind_pairs.py ... --unblind <grades.json>` maps X and Y back and prints the totals.
4. **Reading it.** With one run per case the noise is about 15 points (less with three), so a few points' difference is no difference;
   the judge's preferences matter more than the pass rates. Fix the checks the judge flags as wrong. Decide per role:
   preload the playbook (it clearly helps), keep it on demand (no measurable difference), or cut it.

### What the runner handles for you

- The prompt goes on stdin: `--disallowedTools` takes several values and swallows a trailing prompt.
- `--strict-mcp-config` keeps the owner's connectors out of the runs.
- The agent memory field writes notes even when Write is disallowed, so the runner resets the notebooks with git at
  the end and removes the temporary agents.

## 2. Real use

Every question through the hub or `/ask` adds a row to `usage-log.md`. After two weeks the owner fills in the result
column: changed a decision, saved time, or neither. Keep the roles that earn it; cut or merge the rest.
