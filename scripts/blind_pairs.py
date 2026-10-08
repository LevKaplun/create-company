#!/usr/bin/env python3
"""Copy a role's eval outputs into blind pairs (X and Y in random order) and keep the key apart.

    python3 scripts/blind_pairs.py <company folder> <role> <results folder name> <blind folder>
    python3 scripts/blind_pairs.py <company folder> <role> <results folder name> <blind folder> --unblind <grades.json>

The blind folder must be OUTSIDE the company folder, so the judge cannot find the results or the key. The judge
writes `<role>-grades.json` as {"case-01": {"X": {"passed": n, "applicable": n}, "Y": {...}, "verdict": "X|Y|tie|both_bad"}}.
With --unblind, the script maps X and Y back to A (with the playbook) and B (without) and prints the totals.
"""
import json
import pathlib
import random
import shutil
import sys


def make(company, role, results, blind):
    src = pathlib.Path(company) / "evals" / role / results
    dst = pathlib.Path(blind) / role
    dst.mkdir(parents=True, exist_ok=True)
    rng = random.SystemRandom()
    key = {}
    for a in sorted(src.glob("*-A.md")):
        case = a.name[:-5]
        flip = rng.random() < 0.5
        key[case] = {"X": "B" if flip else "A", "Y": "A" if flip else "B"}
        for label, arm in key[case].items():
            shutil.copy(src / f"{case}-{arm}.md", dst / f"{case}-{label}.md")
    (pathlib.Path(blind) / f"{role}-key.json").write_text(json.dumps(key, indent=1))
    print(f"{len(key)} pairs in {dst}; key in {pathlib.Path(blind) / (role + '-key.json')} (do not show it to the judge)")


def unblind(blind, role, grades_path):
    key = json.loads((pathlib.Path(blind) / f"{role}-key.json").read_text())
    grades = json.loads(pathlib.Path(grades_path).read_text())
    totals = {"A": [0, 0], "B": [0, 0]}
    verdicts = {"A": 0, "B": 0, "tie": 0, "both_bad": 0}
    for case, g in grades.items():
        for label in ("X", "Y"):
            arm = key[case][label]
            totals[arm][0] += g[label]["passed"]
            totals[arm][1] += g[label]["applicable"]
        v = g["verdict"]
        verdicts[key[case][v] if v in ("X", "Y") else v] += 1
    for arm, (p, a) in totals.items():
        label = "with the playbook" if arm == "A" else "without it"
        print(f"{arm} ({label}): {p}/{a} checks = {100 * p / a:.1f}%")
    print("judge preferred:", verdicts)


if __name__ == "__main__":
    if len(sys.argv) >= 7 and sys.argv[5] == "--unblind":
        unblind(sys.argv[4], sys.argv[2], sys.argv[6])
    elif len(sys.argv) == 5:
        make(*sys.argv[1:5])
    else:
        sys.exit(__doc__)
