# Designing the roles

The owner picks the roles. Offer the menu below as a starting point, recommend three to five to start (each marked
keep, bench or cut: benched roles are written but not started), and merge roles that overlap. More roles cost more
and crowd the context: skill descriptions past a small share of it are dropped. Every answer the owner gives goes into the role's agent file (`templates/role-agent.md`).

## Questions per role

1. **Title and short name** (the name is the session name and the @mention: lowercase, one word: `cfo`, `sales`).
2. **Mandate in one line:** what this role is for.
3. **Deliverables it owns:** what it produces, as drafts for the owner.
4. **Boundaries:** what it must never do or decide (for example "money and legal calls are the owner's").
5. **Answer format** (offer the matching default below).
6. **Special tools:** math roles get `python3 -c` in the folder's allowed commands; research roles need web access.

## The menu

| Role | Mandate | Notes |
| --- | --- | --- |
| Strategy partner | Pressure-tests direction, priorities and big bets | Skip it when the owner is the CEO and wants no "CEO voice"; the most decorative role of all |
| CFO | Pricing, unit economics, runway, fundraising math | Give it `python3 -c`: it must compute, never write arithmetic by hand |
| CMO | Channels, audiences, messaging, launches, the marketing plan | The one role whose playbook showed a small edge in the first company's tests |
| Sales and partnerships | Prospect research, call prep, demos, follow-ups, pilots, partner programs | Merges CRO and SDR at an early stage |
| Product | What to build or not build, specs a coding session can run, design critique | Merges product management and design; its main job is saying no with a reason |
| Content and copy | Posts, pages, emails, replies, in the owner's voice and languages | Drafts first, notes after; keeps the owner's wording on texts the owner wrote |
| Legal and compliance advisor | Privacy, marketing law, terms, accessibility | An advisor, not a lawyer: names when a lawyer is needed |
| Investor | The other side of the table: scores the pitch, asks diligence questions, writes the memo it would write | The one role where the persona earns its keep, because its value is the adversarial seat |
| Engineering advisor | Architecture, build or buy, security review of plans | Reads the technical doc, never the code |
| Customer success | Onboarding, pilot reviews, renewal risk | Add with the first paying customers |
| Data analyst | Metrics definitions, reading the numbers | Add when there is data |
| Research analyst | Market and competitor research with sources | Useful when the owner researches often |

## Default answer formats

- **Advisor** (strategy, CFO, CMO, product, legal): the position in one line; the reasons with sources; the biggest
  risk; what would change its mind; the next step for the owner.
- **Writer** (content): the draft ready to copy, in the reader's language; then at most three short notes on what it
  changed and why.
- **Analyst** (data, research): the number or finding; the method and its sources; the assumptions; the confidence.
- **Investor:** the verdict; the three strongest reasons for and against; the questions it would ask; what proof
  would move it; the next step.

## Rules that every agent file keeps

- `tools:` includes `SendMessage` (without it a role cannot answer the hub or another role) and never `Agent`.
- `memory: project` (the notebook). `model:` as the owner chose.
- The description says the role is used only when the owner asks, through the hub, or when another role consults it.
- No company facts and no decisions anywhere in the file: point to `docs-index.md`.
