# create-company

A Claude Code skill that builds you an AI company: a team of role agents (a CFO, a CMO, a product lead, whoever you
choose) that read your own documents, answer you directly or together in one "hub" chat, and can run as sessions you
reach from your phone.

## What you get

- **The roles you pick.** Each one is an agent with a clear mandate, boundaries and answer format, plus an optional
  expert playbook (frameworks, checklists, templates) researched for its job.
- **Your documents as the only source.** Roles never carry facts about your company; they read your docs and your
  strategy files (plans, briefs, your earlier answers) when they answer. The plans are knowledge, not rules: each
  role is a professional in its field, leads with its own judgment and tells you where it differs from the plan.
  When something changes, you update the doc, not the role.
- **A hub, your chief of staff.** Write `@cfo @cmo should we raise prices?` and each answers on its own, or write
  without a mention and the hub sends it to the one to three roles it is about and says who. Two or more answers
  end with a short bottom line: where they agree, where they differ, what is left for you to choose. Say "discuss"
  for a short round where they react to each other, "summarize" for a fuller summary.
- **Memory.** Each role keeps its own notes from your conversations.
- **Your phone.** Every role and the hub can run as a background session with Remote Control, so they appear in the
  Claude app. Prefer something simpler? Choose "one session" and the hub runs the roles inside a single window.
- **Evals.** A way to test whether each role's playbook really helps, graded blind.

## Install

Clone it into your personal skills folder:

```
git clone https://github.com/LevKaplun/create-company ~/.claude/skills/create-company
```

Then, in Claude Code, type `/create-company`. You run it once to build your company; the company folder it creates
holds everything after that, including the scripts to restart sessions and run tests. To update the skill later:
`git -C ~/.claude/skills/create-company pull`.

## Requirements

- Claude Code in a terminal on macOS, Linux or WSL, a recent version (`claude update`); for the
  roles to message each other: 2.1.224 or later.
- A paid plan; Remote Control (the phone) needs a claude.ai subscription.
- `git` and `python3`. Word files are read with `textutil` on macOS or `pandoc` on Linux.

## What is inside

Markdown guides and templates, plus three small scripts the skill copies into your company folder:
`start_sessions.sh` (starts or restarts the role sessions), `run_evals.py` and `blind_pairs.py` (the playbook tests).
No hooks, no servers, nothing that runs in your other sessions. Read them before you run them, as you should with
anything you install.

Two guides are worth reading even if you never run the skill:
[`references/principles.md`](references/principles.md), why the company is built this way, with sources, and
[`references/troubleshooting.md`](references/troubleshooting.md), the Claude Code behaviors we ran into (background
sessions, messages between sessions, headless runs) and the fix for each.

## Use

- `/create-company`: the interview and the build.
- `/create-company add-role`, `/create-company playbook <role>`, `/create-company sessions`,
  `/create-company evals <role>`: later changes.
- Inside your company folder: `/ask <role> <question>`, the hub, or `claude --agent <role> -n <role>`.

## Be honest with yourself

The roles are useful for recurring work (drafts, analysis, math, research) and for an independent check before a
big decision. In the first company built this way, a plain role with good rules and real documents already did most
of the work, and the long playbooks made a small difference for only one of three roles. Agreement between roles
running on the same model is weak evidence. Treat it as an experiment, keep the usage log it creates for two weeks,
and keep only the roles that changed a decision or saved you time. Every answer uses your plan's usage; idle sessions cost nothing.
