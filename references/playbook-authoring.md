# Writing a role's expert playbook

A playbook is a skill in `.claude/skills/<role>-playbook/`: `SKILL.md` plus `references/*.md`. It holds expertise,
never company facts. Build each one with a research agent (the brief below), then review it yourself.

## What goes in

- **Rules first.** After compaction only the first few thousand tokens of an invoked skill survive, so the rules that
  must always hold come first, then a routing table (which kind of request goes to which workflow), then the
  workflows.
- **Procedures and named frameworks** a top practitioner uses in that job today, each adapted, not pasted.
- **Checklists, output templates and a quality bar**, plus the common mistakes with a bad and a good example.
- **Where facts live:** a map from each kind of fact to the doc and section heading, never the fact itself. The
  strategy files go in the map as knowledge the role weighs, never as rules the playbook enforces.
- **Sources** in `references/sources.md`: each with its date, licence and what was taken. Prefer recent material and
  current library state; say plainly when nothing recent exists instead of filling the gap with older sources.

## What never goes in

Company facts (products, prices, customers, team, numbers), the owner's plans and earlier answers, market figures
that change (valuations, prices, rankings: the playbook says how to find them on the day), and anything from an
excluded folder.

## On demand or preloaded

By default the agent file points to the playbook and the role opens it when a task needs a framework, template or
checklist. Preload it (`skills: [<role>-playbook]` in the agent file) only when an eval shows it helps.

## The brief for the research agent

Give each agent: the company's `CLAUDE.md` and `docs-index.md` to read first; the role's agent file; the rules above;
the exact files to write (`SKILL.md` with the description "Playbook for <company>'s <role> role agent.", the
`references/`); the evidence rule (recent sources, current library state, cited); and the limits (write only inside
the playbook folder, no installs, no commits, no helper agents). Run at most five in parallel. Then review: no company
facts or plans (search for prices, names, numbers), no plan turned into a rule, every source cited, rules first,
nothing from an excluded folder.
