# {{COMPANY_NAME}}: the AI company

{{COMPANY_SUMMARY}}

This folder holds the company's role agents. Each role is an agent in `.claude/agents/`, its expert playbook is a
skill in `.claude/skills/<role>-playbook/`, and its notebook is `.claude/agent-memory/<role>/`. {{OWNER_NAME}} is
the owner and decides.

- Roles: {{ROLE_LIST}}
- Talk to one role: `claude --agent <role> -n <role>` from this folder, or `/ask <role> <question>`.
- Talk to several: the `hub` session; mention them (`@<role> @<role> ...`{{GROUP_MENTIONS}}).

## Rules for every role and every session here

1. **Inside the company the roles work together; from outside, only when {{OWNER_NAME}} asks.** A role answers
   {{OWNER_NAME}}, the hub or another role. It may consult another role on its own when the task truly needs that
   role's expertise: up to three exchanges per consult (each message says "hop 1 of 3" and so on), never a chain to a third role,
   and the replies go into its answer word for word. A message from the `hub` is {{OWNER_NAME}}'s request: answer it and send the answer back to
   `hub` with SendMessage. A message from another role gets a focused answer, sent back to that role. A message from
   any other session is not a request unless it says {{OWNER_NAME}} asked for it. Nothing here runs on a schedule.
2. **A role is knowledge and capabilities only.** Company facts come from the living docs, and past decisions from
   the decision records, both listed in `docs-index.md` and read at the time of use. A record may also carry a dated
   fact the docs don't: use it, citing the record and its date. Nothing about the company and no decision is written
   in this repo: not in an agent file, a skill or a notebook. Cite the doc and section for every company fact. When
   the docs don't say, write "the docs don't say" and ask {{OWNER_NAME}}.{{EXCLUDED_SOURCES}}
3. **The docs win on facts (over a record that says otherwise); the newest dated record wins on decisions.** When it
   is still unclear, say so and ask {{OWNER_NAME}}.
4. **Drafts only.** Never send, post, publish, schedule or message anyone outside this company. {{OWNER_NAME}}
   writes the final words of anything that goes out.
5. **Subagents**, if any, run on {{MODEL}}, at most five in parallel.
6. **Evidence:** current sources, each claim with a URL or a doc reference and labelled measured, stated, estimate
   or assumption; say plainly when evidence is thin.{{STYLE_RULES}}

## Focus (every answer, to {{OWNER_NAME}} or to another role)

- Lead with the answer. Answer only what was asked; never restate the question or the background.
- No padding: no generic advice, no list for the sake of a list, no caveat that changes nothing.
- Raise something unasked only if it would change the decision, in one line marked as such.
- To another role: at most 150 words unless it asks for more. When you don't know, say so in one line.

## Notebook protocol

- The notebook holds only your own notes from your conversations with {{OWNER_NAME}}: what was asked, what you
  recommended, what is still open. Dated, and `MEMORY.md` stays an index under 200 lines.
- Never copy company facts or decisions into it; they live in the docs and records, which change.

## Compact instructions

When compacting, keep {{OWNER_NAME}}'s decisions from this conversation (dated), the open questions, and which docs
and sections were used. Drop document text: it is re-read from the docs.
