# Running the company: sessions, the hub, the phone

## Two ways to run them

- **Background sessions** (default): every role and the hub run on their own, keep their own conversations, and
  show up on the phone. Needs a claude.ai subscription for Remote Control.
- **One session** (simpler): the hub runs the roles as named subagents inside a single session
  (`templates/hub-subagents.md`). Nothing runs in the background; the roles' conversations live only as long as
  that session.

## Three ways to talk to the roles

1. **`/ask <role> <question>`** in any session opened in the company folder: a fresh role answers one question.
2. **A standing session per role:** `claude --agent cfo -n cfo` in the folder, or as a background session with Remote
   Control so it lives without a terminal and shows up in the Claude app on the phone.
3. **The hub:** the owner's chief of staff, one session for the whole team. The owner mentions roles
   (`@cfo @cmo ...`, groups such as `@all`), or mentions none and the hub picks the one to three roles the message is
   about and says who. It relays each answer word for word and, after two or more, ends with a bottom line of at most
   four lines: where they agree, where they differ, what is left to choose. "discuss" starts a focused round where
   each role sees the others' answers; "summarize" gives a fuller summary of agreement and disagreement, nothing
   added.

## Starting the background sessions

`scripts/start_sessions.sh <company folder>` starts every role and the hub with
`claude --bg --agent <role> --name <role> --remote-control <role> "<first message>"`, waits until they are idle and
prints each Remote Control link. In the app the sessions keep their names.

- **Pin them right away** in `claude agents`: select each session and press Control+T; it moves under a "Pinned"
  header. An unpinned idle session stops after about an hour, and a hub waiting on a stopped role waits. A pin keeps
  a running session up but does not start a stopped one: `claude respawn <id>` does, keeping its conversation
  (opening the session or replying to it also brings it back).
- **A shutdown or restart of the computer stops every session** (sleep does not). Afterwards
  `claude respawn --all` brings them back with their conversations.
- **Editing a role does not reach a running session.** A session keeps the system prompt it started with. After
  changing an agent file, `CLAUDE.md` or a playbook, restart that session.
- **A restart of a fresh session wipes its conversation**, and the link changes. Tell the owner before restarting a
  session that is in use. `claude respawn <id>` keeps the conversation but not a new prompt.

## Settings the folder needs (`templates/settings.json`)

- Messages between the roles and the hub: `crossSessionInbound` only takes effect from user settings or `--settings`,
  never from a project's settings, so `start_sessions.sh` passes `--settings '{"crossSessionInbound":"accept"}'` on
  every launch. Without it, sessions in different permission modes hold each other's messages.
- `worktree.bgIsolation: "none"`: background sessions edit the folder in place. Without it they are pushed into a
  separate worktree, and notebook notes and the usage log never land in the folder.
- `permissions.allow`: the read commands for the doc formats, `python3 -c` for math roles, web search and fetch.
- `permissions.additionalDirectories`: the folders holding the docs, the strategy files and the evidence.
- **Trust the folder once:** open `claude` in it interactively and accept the trust prompt. Until then the folder's
  own settings are ignored.

## Checking the wiring

After starting, ask the owner to type in the hub: "@<one role> reply with the single word ok". The hub sends it, the
role answers the hub, and the hub shows the reply. If nothing comes back, see `troubleshooting.md`.

## Cost

Every message to a role is a turn on the owner's plan, like a typed prompt; an idle session costs nothing. The first
answer of a session reads the docs it needs (often tens of thousands of tokens); later answers in the same session
reuse what it read while the cache lasts (about an hour on a subscription).
