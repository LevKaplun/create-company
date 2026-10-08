# {{ROLE_TITLE}} eval: real tasks, with and without the playbook

The prompts live in `cases.json` (the runner reads them); the checks live here (the judge reads them). Write each
case from a real task the owner asked or will ask, with names replaced by placeholders. Keep the last third of the
cases as a held-out set: run them only once the playbook stops changing.

## Checks for every case

- G1. Leads with the answer; nothing restated; no padding.
- G2. Every company fact cites a doc or record and its section, or says the docs don't say.
- G3. No claim the docs don't support.
- G4. Follows the answer format in the agent file.
- G5. Drafts only: proposes nothing that sends, posts or publishes.
{{STYLE_CHECKS}}

## Cases

### 1. {{CASE_TITLE}}

- Prompt: in `cases.json` as `case-01`.
- 1.1 {{A check a top practitioner's answer would pass and a generic answer would fail.}}
- 1.2 {{A check that the decision records were read and cited, without stating the decision here.}}
- 1.3 {{A check on the deliverable's shape or completeness.}}

<!-- Write checks as yes or no questions about the answer. A check must be passable: if two careful answers both
fail it for the same reason, the check is wrong, not the answers. Never write a company fact or a decision into a
check; point to the doc or record instead, so the check follows whatever it says on the day. -->
