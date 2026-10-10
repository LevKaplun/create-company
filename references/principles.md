# Why the company is built this way

Read this before changing the design. Each rule below came from research (September 2026 sources and the current
Claude Code docs, listed at the end) or from a failure we hit while building and using the first company.

## What makes a role useful

1. **A persona line is not expertise.** "You are the CFO" only sets focus and tone. Expertise comes from a playbook
   (procedures, named frameworks, checklists, templates, a quality bar) and from real documents.
2. **Fewer, fuller roles.** One agent with the right skills beat setups with subagents in Anthropic's own
   comparisons (a vendor claim), and in a paired experiment flat teams wrote better reports than teams under a manager
   agent that could send work back, while the managed teams used 51.5% more tokens. Each role owns its whole
   deliverable; no AI managers over AI workers. Start with three to six roles.
3. **A role is a professional in its field with the full picture.** Its expertise is its agent file and playbook;
   what it knows about the company, the product and the strategy comes from the owner's sources, read at the time
   of use: the living docs (facts), the strategy files (plans, briefs, the owner's earlier answers) and the
   research. Nothing about the company is written into a role, a playbook or a notebook: it goes stale and carries
   whoever wrote it, so when something changes, the doc changes, never the role. The strategy files are knowledge,
   not rules: a role leads with its own judgment and, where it differs from the current plan or from what the owner
   said before, says so and why. On facts the newest information wins, and what the owner just said is the newest.
   What stays a rule: the owner's writing rules for drafts in the owner's name, and the limits of authority and law
   (for example: the owner decides, sends and pays; drafts only; no cold outreach without the owner's say;
   customers' projects off limits).
4. **Binding plans make clerks.** The first company framed the owner's plan files as decision records that bind the
   roles; in real use every role opened by reciting them ("your decision of <date> makes X the gate") and turned
   new ideas down as against a locked decision. The files are knowledge, and each role says when it disagrees.
5. **The docs are the single source.** One canonical copy of each doc; old copies and old folders are named as
   excluded so no role reads them.

## How roles work together

6. **Groups converge.** LLM groups follow the majority and converge earlier than human groups, whoever speaks first
   shapes the answer, and on opinion questions debate rarely moves a position. So first answers are independent (the
   hub never passes one role's answer to another unless asked), discussion rounds are explicit and short, and a
   summary keeps the disagreements.
7. **Long conversations drift.** In a long role-play benchmark even the strongest system first broke character after
   about ten turns, and under sustained pushback models give in more the longer the conversation runs. So a role's
   memory lives in its notebook (its own dated notes only), and a long session is restarted fresh.
8. **Consults have limits.** Inside the company a role may consult another when the task truly needs it: up to three
   exchanges, never a chain to a third role, and the replies go to the owner word for word.
9. **Focus.** Lead with the answer, answer only what was asked, no padding, raise an unasked point only if it would
   change the decision, at most 150 words to another role.
10. **From outside, only when the owner asks.** Other Claude sessions (coding, research) never use the roles on
    their own initiative; the roles are the owner's advisors, not helpers for other work.

## How to know it works

11. **Evaluate before trusting, then judge by real use.** In the first company, the plain role (agent file, shared
    rules, docs and strategy files) already scored 88 to 92 percent on real tasks; the long playbooks added nothing
    measurable for two of three roles and a mild lean for the third (one run per case, ten to twelve cases per role,
    graded blind: a small sample). So playbooks load on demand by default, and the roles are judged by two weeks of
    real use: did an answer change a decision or save time?
12. **We found no study showing an AI board improving a founder's decisions.** Treat the company as an experiment.
    Its value is recurring work done faster (drafts, analysis, math, research) and an occasional independent check
    before a big, hard-to-reverse decision; not a weekly meeting ritual.
13. **Mind the cost.** Every role run reads its docs (tens of thousands of tokens). A full eval is dozens of heavy
    runs; a role session that sits idle costs nothing.

## Sources

Most are preprints from September 2026: read them as signals, not settled results.

- **1.** A role in the system prompt "focuses Claude's behavior and tone": Anthropic,
  [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).
  Skills "turn a general-purpose agent into a specialist": Anthropic,
  [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). Personas written from
  model memory misstated a documented position on 1 to 4 of 20 answers, while an agent with no persona never did:
  [mimeo, arXiv 2609.00453](https://arxiv.org/abs/2609.00453).
- **2.** "A single agent with skills consistently has outperformed both the one-prompt-for-everything design and the
  subagent design on quality": Anthropic,
  [A guide to the anatomy of effective commerce agents](https://claude.com/blog/the-anatomy-of-effective-commerce-agents)
  (comparison data not published). Flat teams wrote better reports, and the managed ones used 51.5% more tokens; a
  manager "earns its cost when it can verify something and becomes a liability when it can only opine":
  [Loop-Back Authority in LLM Agent Teams, arXiv 2609.14767](https://arxiv.org/abs/2609.14767).
- **6.** LLM groups "follow majorities more often, surface less unique information, and converge earlier" than human
  groups: [arXiv 2609.13261](https://arxiv.org/abs/2609.13261). First-speaker bias in sequential debate:
  [arXiv 2609.38964](https://arxiv.org/abs/2609.38964). Positions unchanged in over 90% of comparisons on opinion
  questions: [arXiv 2609.08016](https://arxiv.org/abs/2609.08016).
- **7.** The strongest system's first persona failure came after 10.4 turns on average, in spoken dialogue:
  [RoleBreak, arXiv 2609.16614](https://arxiv.org/abs/2609.16614). "Collapse rates increase with conversation length
  for every model" under sustained pushback: [SPINE, arXiv 2609.09090](https://arxiv.org/abs/2609.09090).
