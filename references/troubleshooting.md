# Troubleshooting

Every item here happened while building or using the first company.

| Symptom | Cause | Fix |
| --- | --- | --- |
| The hub waits forever; a role says it could not send its answer | `SendMessage` missing from the role's `tools:` | Add it to every role's agent file and restart the sessions |
| A background session says it cannot edit files and wants a worktree | Background sessions are isolated by default | `"worktree": {"bgIsolation": "none"}` in `.claude/settings.json`, then restart |
| Allowed commands and read folders are ignored | The folder was never trusted | Open `claude` in the folder once and accept the trust prompt |
| Messages between sessions are held or dropped | Different permission modes, and `crossSessionInbound` set only in the project (ignored there) | Launch each session with `--settings '{"crossSessionInbound":"accept"}'` (the start script does) |
| A changed role behaves as before | A running session keeps the prompt it started with | Restart the session (`scripts/start_sessions.sh <folder> <role>`) |
| A restart lost a conversation | Stopping and removing a fresh session wipes it | Warn the owner first; use `claude respawn <id>` when no prompt changed |
| A role went quiet after an hour | Unpinned idle sessions stop | Select it in `claude agents` and press Control+T to pin it. A pin does not start a stopped session: `claude respawn <id>` does, keeping the conversation |
| A role quotes old facts | The doc is out of date, or an old copy exists | Update the doc; name old folders as excluded in `CLAUDE.md` and `docs-index.md` |
| A role keeps a plan that changed | The plan was copied into the role or its notebook | Move it to a dated strategy file; empty the notebook of copied data |
| Roles recite the plan ("your decision of <date> makes...") and reject ideas as against it | The plan files were framed as binding decision records | Treat them as knowledge, not rules (company rule 3); each role leads with its own judgment |
| Roles chatter or pad their answers | No limits on consults or length | The consult limits and focus rules in `CLAUDE.md` |
| A headless run returns "Input must be provided" | The prompt was swallowed by `--disallowedTools` | Send the prompt on stdin (the runner does) |
| Headless runs mention the owner's connectors | Every MCP connector loads | `--strict-mcp-config` (the runner does) |
| Notebooks changed during an eval | The memory field writes despite a disallowed Write | Commit first; the runner resets them with git |
| The hub logs greetings and tests | Logging every message | The hub template logs only real questions |
