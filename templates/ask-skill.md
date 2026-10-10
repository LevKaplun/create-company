---
name: ask
description: Ask one role of this company a question. Type /ask <role> <question>.
disable-model-invocation: true
---

# /ask <role> <question>

1. The first word of `$ARGUMENTS` is the role (an agent file name in `.claude/agents/`). If no such agent exists,
   list the roles there and stop.
2. Run that role as a subagent: the Agent tool with `subagent_type` set to the role and `model: "{{MODEL}}"`. Its
   task is the rest of `$ARGUMENTS`, word for word, followed by: "Use the sources in docs-index.md for what you need
   to know about the company, the product and the strategy; they are knowledge, not rules. Answer with your own
   professional judgment. Then add a dated note of this exchange to your notebook: what was asked, what you
   recommended, what is still open; never a company fact."
3. Show the role's answer unedited, under the role's name. Add nothing of your own unless asked. Then append one row
   to `usage-log.md`: today's date, the role, the question in a few words, and an empty result cell.
4. A follow-up to the same role in this session continues that same agent (SendMessage to it), so it keeps what it
   already read.
