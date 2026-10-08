#!/usr/bin/env bash
# Start (or restart) the company's role sessions and the hub as background sessions with Remote Control.
#
#   scripts/start_sessions.sh <company folder> [role ...]
#
# With no roles named, it starts every agent in .claude/agents/ (the hub included). A session that is already running
# under the same name is stopped and removed first, which WIPES its conversation: say so to the owner before
# restarting a session that is in use. Prints each session's state and its Remote Control link.
set -euo pipefail

company="${1:?usage: start_sessions.sh <company folder> [role ...]}"
shift || true
cd "$company"

if [ "$#" -gt 0 ]; then
  roles=("$@")
else
  roles=()
  for f in .claude/agents/*.md; do roles+=("$(basename "$f" .md)"); done
fi

session_id() {
  claude agents --json 2>/dev/null | python3 -c "
import json, sys
name, cwd = sys.argv[1], sys.argv[2]
for s in json.load(sys.stdin):
    if s.get('name') == name and s.get('cwd') == cwd:
        print(s['id']); break" "$1" "$PWD"
}

for role in "${roles[@]}"; do
  id="$(session_id "$role")"
  if [ -n "$id" ]; then
    claude stop "$id" >/dev/null 2>&1 || true
    claude rm "$id" >/dev/null 2>&1 || true
  fi
  if [ "$role" = "hub" ]; then
    first="Reply in one line that the team channel is ready."
  else
    first="Reply in one line that you are ready, then wait for the first question. Do not read any file yet."
  fi
  # crossSessionInbound only takes effect from user settings or --settings, not from the project's settings.
  claude --bg --agent "$role" --name "$role" --remote-control "$role" \
    --settings '{"crossSessionInbound":"accept"}' "$first" >/dev/null 2>&1
  echo "started $role"
done

# Wait until every started session is idle (at most two minutes), then print the links.
for _ in $(seq 1 24); do
  busy=0
  for role in "${roles[@]}"; do
    state="$(claude agents --json 2>/dev/null | python3 -c "
import json, sys
name, cwd = sys.argv[1], sys.argv[2]
print(next((s.get('status', '') for s in json.load(sys.stdin) if s.get('name') == name and s.get('cwd') == cwd), ''))" "$role" "$PWD")"
    [ "$state" = "idle" ] || busy=1
  done
  [ "$busy" -eq 0 ] && break
  sleep 5
done

for role in "${roles[@]}"; do
  link="$(claude logs "$role" 2>/dev/null | grep -o 'https://claude.ai/code/session_[A-Za-z0-9]*' | tail -1 || true)"
  echo "$role | ${link:-no Remote Control link yet: run 'claude logs $role'}"
done
echo "Pin the sessions you want always on in 'claude agents'; an unpinned idle session stops after about an hour."
