---
name: create-company
description: Build an AI company in Claude Code. Interviews the owner about the company, its documents and the roles they want, then creates a company folder with shared rules, a docs index, one agent per role with an expert playbook, a hub that routes the owner's messages to the right roles, sessions reachable from the phone, and evals. Run with /create-company, or /create-company add-role | playbook <role> | sessions | evals <role>.
disable-model-invocation: true
compatibility: Claude Code in a terminal on macOS, Linux or WSL, v2.1.224 or later; Remote Control needs a claude.ai subscription.
---

# /create-company

Builds a company of role agents that work for one owner: each role is an expert with a playbook, reads the owner's
own documents at the time of use, keeps only its own conversation notes, and answers the owner directly, through a
hub, or when another role consults it. Read `${CLAUDE_SKILL_DIR}/references/principles.md` once before the first
build. Every template, script and guide named below lives under `${CLAUDE_SKILL_DIR}`.

`$ARGUMENTS` picks the mode: empty = build a company; `add-role` = add one role to an existing company;
`playbook <role>` = write or rewrite a role's playbook; `sessions` = start or restart the sessions; `evals <role>` =
test a role's playbook.

## Rules for this skill

- Ask, never assume: the owner chooses the roles, the docs, the folder and every name. Use AskUserQuestion with the
  recommended default first; ask one question at a time when the answer needs thought, a short batch otherwise.
- Write nothing about the owner's company into an agent file, a skill or a notebook: facts and plans stay in the
  owner's docs and strategy files, referenced from `docs-index.md`.
- Preview before writing: show the plan, then the filled `CLAUDE.md` and one agent file, and get a yes. Never
  overwrite an existing folder.
- Never start sessions, run evals or spawn research agents without the owner's yes: each costs usage on their plan.
  Say the expected number of runs before asking.

## Build a company (no arguments)

### 1. Check the tools

`claude --version` (suggest `claude update` when it is old), `git`, `python3`. On macOS `textutil` reads .docx; on
Linux suggest `pandoc`; `pdftotext` or the Read tool for PDFs.

### 2. Interview

1. **The company:** its name; one paragraph on what it does; the owner's name as the roles should address them; the
   language(s) answers should be in.
2. **The folder:** where to create it (default `~/<company-slug>-company`); it becomes its own git repo.
3. **The sources** (`templates/docs-index.md`):
   - Living docs: the files that hold company facts (at least one). Check each path exists and pick its read command.
   - The strategy files: plans, briefs and the owner's earlier answers, with dates (optional). The roles read them
     as knowledge, not rules.
   - Evidence: research folders (optional).
   - Excluded: old copies or folders the roles must never read (optional).
4. **The roles** (`references/role-design.md`): show the menu, recommend three to five to start, and let the owner
   pick or name their own, each marked keep, bench (written, not started) or cut. For each role ask the mandate in
   one line, the deliverables, the boundaries and the answer format (offer the defaults). Suggest merging overlaps.
5. **The model** for every role (default the strongest the owner's plan allows; a cheaper one costs less per answer)
   and any style rules for drafts (for example "no long dashes", "we, not I").
6. **How to run them:** background sessions with Remote Control (each role on its own, reachable from the phone; the
   default) or one session (the hub runs the roles as subagents; simpler, nothing in the background). Then: the hub
   (default yes; offer groups such as `@all` and `@board`); expert playbooks now (one research agent per role; slow
   and heavy) or later; eval cases per role.

### 3. Preview

List every file and folder to be created and every command that will run; show the filled `CLAUDE.md` and one agent
file. Wait for a yes.

### 4. Build

1. Create the folder and `git init`.
2. `CLAUDE.md` from `templates/company-CLAUDE.md`: fill every `{{...}}`; `{{ROLE_LIST}}` names each role with its
   field in a few words (the hub routes by it); `{{EXCLUDED_SOURCES}}` names the excluded folders ("Never use
   <folder>: it holds old versions."); `{{STYLE_RULES}}` adds the owner's style rules as rule 7.
3. `docs-index.md` from `templates/docs-index.md`: one row per source with its exact read command. Run each command
   once to prove it reads.
4. `.claude/settings.json` from `templates/settings.json`: the allow list holds each read command in the index (as
   `Bash(<command prefix>:*)`), `python3 -c` when a role does math, `WebSearch` and `WebFetch`; the read directories
   are the folders holding the sources.
5. One `.claude/agents/<role>.md` per role (benched roles too) from `templates/role-agent.md`, filled from the
   interview. Keep `SendMessage` in `tools:`, never add `Agent`, and leave out "Your playbook" until it exists.
6. `.claude/agent-memory/<role>/MEMORY.md` per role: a title, one line on what it holds (the role's own dated notes
   from its conversations, never company facts or plans), an empty "Notes" list.
7. The hub: `.claude/agents/hub.md` from `templates/hub-agent.md` (background sessions) or
   `templates/hub-subagents.md` (one session).
8. `.claude/skills/ask/SKILL.md` from `templates/ask-skill.md`, and `usage-log.md` from `templates/usage-log.md`.
9. Copy `scripts/` into the company folder as `scripts/`, so it can restart sessions and run evals on its own.
10. If evals were chosen: `evals/<role>/cases.md` and `cases.json` per role (`templates/eval-cases.md`), from real
    tasks the owner gives; offer drafts from the mandate and let the owner correct them.
11. If playbooks were chosen now: one research agent per role, at most five in parallel, with the brief in
    `references/playbook-authoring.md`; review each result, then add "Your playbook" to that role's agent file.
12. `git add -A && git commit -m "The company: rules, docs index, roles"`.

### 5. Hand over

`references/sessions-and-hub.md` holds the details behind these steps.

1. Ask the owner to open `claude` in the folder once and accept the trust prompt: until then the folder's settings are
   ignored.
2. Background sessions: `scripts/start_sessions.sh <folder> <kept roles> hub`; give the links, ask the owner to pin
   each session right away in `claude agents` (select it and press Control+T; it moves under "Pinned"), and to check
   the wiring by typing in the hub "@<one role> reply with the single word ok".
   One session: `cd <folder> && claude --agent hub -n hub` (add `--remote-control hub` for the phone).
3. Explain in a few lines: `/ask <role> <question>`; the hub (mention roles, or none and it picks them), "discuss"
   and "summarize"; a standing session per role; when the docs or the strategy files change, update them, never the
   roles; after editing a role, restart its session; the two-week usage log.

## add-role

Run interview step 4 for the new role only, then build steps 5, 6 and 12, add the role to the roster in `CLAUDE.md`
and to the hub's mention list, and offer to start its session. Restarting the hub picks up the new name and clears
the hub's conversation: say so first.

## playbook <role>

Write or rewrite the playbook with a research agent (`references/playbook-authoring.md`), review it, add "Your
playbook" to the agent file, commit, and offer to restart the role's session.

## sessions

`scripts/start_sessions.sh <folder> [role ...]` (details in `references/sessions-and-hub.md`). Before restarting a
session that may be in use, say that its conversation will be cleared and wait for a yes.

## evals <role>

Follow `references/evals.md`: cases, runs (`scripts/run_evals.py`; one run per case to iterate, three before
deciding), blind pairs (`scripts/blind_pairs.py`), a fresh judge per role (`templates/judge-prompt.md`), the
unblinded totals, and the decision per role: preload the playbook, keep it on demand, or cut it.

## When something breaks

`references/troubleshooting.md`.
