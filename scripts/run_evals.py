#!/usr/bin/env python3
"""Run a role's eval cases headless, with its playbook (arm A) and without it (arm B).

    python3 scripts/run_evals.py <company folder> <role>[,<role>...] [--workers 4] [--cases 1-10] [--runs 3]

Each role needs `evals/<role>/cases.json`: a list of {"id": "case-01", "prompt": "..."}.

Arm A runs the role with its playbook preloaded; arm B runs a temporary copy of the agent with no playbook section,
no `skills:` line and the Skill tool disallowed. Both get the same docs, records, notebook and model. Outputs go to
`evals/<role>/results-<date>/<case>-A.md` and `-B.md` (with `-r2`, `-r3` before the arm when --runs is above 1).
One run per case is enough to iterate; use three before deciding anything. Afterwards the temporary agents are removed and the notebooks
are reset with git, because the agent memory field writes notes even when Write is disallowed.

Grade the outputs blind with `scripts/blind_pairs.py` and a fresh judge (references/evals.md).
"""
import argparse
import concurrent.futures as cf
import datetime
import json
import pathlib
import re
import subprocess
import sys
import time


def parse_range(text, count):
    if not text:
        return set(range(1, count + 1))
    lo, _, hi = text.partition("-")
    return set(range(int(lo), int(hi or lo) + 1))


def make_arms(company, role):
    agents = company / ".claude" / "agents"
    src = (agents / f"{role}.md").read_text(encoding="utf-8")
    head, _, body = src.partition("\n---\n")
    head_lines = [l for l in head.split("\n") if not l.startswith("skills:")]
    # Arm A: the playbook preloaded.
    arm_a = "\n".join(head_lines + [f"skills: [{role}-playbook]"]) + "\n---\n" + body
    arm_a = arm_a.replace(f"name: {role}\n", f"name: {role}-eval-a\n", 1)
    # Arm B: no playbook at all.
    body_b = re.sub(r"\n## Your playbook\n.*?(?=\n## |\Z)", "\n", body, flags=re.S)
    arm_b = "\n".join(head_lines) + "\n---\n" + body_b
    arm_b = arm_b.replace(f"name: {role}\n", f"name: {role}-eval-b\n", 1)
    (agents / f"{role}-eval-a.md").write_text(arm_a, encoding="utf-8")
    (agents / f"{role}-eval-b.md").write_text(arm_b, encoding="utf-8")


def drop_arms(company, role):
    for arm in ("a", "b"):
        (company / ".claude" / "agents" / f"{role}-eval-{arm}.md").unlink(missing_ok=True)
        mem = company / ".claude" / "agent-memory" / f"{role}-eval-{arm}"
        if mem.exists():
            subprocess.run(["rm", "-rf", str(mem)], check=False)


def settings(company):
    data = json.loads((company / ".claude" / "settings.json").read_text())
    perms = data.get("permissions", {})
    allowed = ["Read", "Grep", "Glob", "WebSearch", "WebFetch"] + perms.get("allow", [])
    return ",".join(dict.fromkeys(allowed)), perms.get("additionalDirectories", [])


def run_one(company, role, case_id, prompt, arm, out_dir, allowed, dirs, run=1):
    agent = f"{role}-eval-{arm.lower()}"
    disallowed = "Write,Edit,Agent,SendMessage" + (",Skill" if arm == "B" else "")
    cmd = ["claude", "-p", "--agent", agent, "--output-format", "text", "--strict-mcp-config",
           "--allowedTools", allowed, "--disallowedTools", disallowed]
    if dirs:
        cmd += ["--add-dir", *dirs]
    started = time.time()
    try:
        # The prompt goes on stdin: --disallowedTools takes several values and would swallow a trailing prompt.
        res = subprocess.run(cmd, input=prompt, capture_output=True, text=True, cwd=company, timeout=1200)
        body = res.stdout if res.returncode == 0 else res.stdout + "\n\n[stderr]\n" + res.stderr[-2000:]
        code = res.returncode
    except subprocess.TimeoutExpired:
        body, code = "[timed out after 1200 s]", -1
    took = int(time.time() - started)
    stem = case_id if run == 1 else f"{case_id}-r{run}"
    (out_dir / f"{stem}-{arm}.md").write_text(body, encoding="utf-8")
    with open(out_dir / "run-log.txt", "a") as log:
        log.write(f"{stem} {arm} exit={code} {took}s\n")
    return f"{role} {stem} {arm} exit={code} {took}s"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("company")
    ap.add_argument("roles")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--cases", default="")
    ap.add_argument("--runs", type=int, default=1)
    args = ap.parse_args()
    company = pathlib.Path(args.company).resolve()
    dirty = subprocess.run(["git", "-C", str(company), "status", "--porcelain", "--", ".claude/agent-memory"],
                           capture_output=True, text=True).stdout.strip()
    if dirty:
        sys.exit("Commit the notebooks first: the runner resets .claude/agent-memory with git when it finishes.")
    allowed, dirs = settings(company)
    day = datetime.date.today().isoformat()
    jobs = []
    for role in args.roles.split(","):
        cases = json.loads((company / "evals" / role / "cases.json").read_text(encoding="utf-8"))
        keep = parse_range(args.cases, len(cases))
        out_dir = company / "evals" / role / f"results-{day}"
        out_dir.mkdir(parents=True, exist_ok=True)
        make_arms(company, role)
        for n, case in enumerate(cases, start=1):
            if n in keep:
                for run in range(1, args.runs + 1):
                    for arm in ("A", "B"):
                        jobs.append((company, role, case["id"], case["prompt"], arm, out_dir, allowed, dirs, run))
    print(f"{len(jobs)} runs", flush=True)
    try:
        with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
            for line in pool.map(lambda j: run_one(*j), jobs):
                print(line, flush=True)
    finally:
        for role in args.roles.split(","):
            drop_arms(company, role)
        subprocess.run(["git", "-C", str(company), "checkout", "--", ".claude/agent-memory"], check=False)
        subprocess.run(["git", "-C", str(company), "clean", "-fdq", ".claude/agent-memory"], check=False)


if __name__ == "__main__":
    main()
