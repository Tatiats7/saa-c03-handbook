#!/usr/bin/env python3
"""Write a progress report of the SAA-C03 Handbook build to stdout (Markdown). Run from the repository root:

  python3 aws-saa-book/_build/ledger/workflows/status_report.py > STATUS.md

Reads only the ledger, the data files and the corpus log; changes nothing. Stdlib only."""
import glob, json, subprocess, sys, time
from collections import Counter
from urllib.parse import urlparse

TOOL = [sys.executable, "aws-saa-book/tools/saa.py"]
W = {"plan": 5, "mine": 12, "register": 5, "verify-facts": 13, "brief": 5, "prose": 14, "questions": 8, "tasks": 3, "cards": 2,
     "speak": 2, "diagrams": 1, "edit": 7, "verify-questions": 8, "review": 7, "fix": 6, "finalize": 2}


def sh(args):
    return subprocess.run(TOOL + args, capture_output=True, text=True).stdout


def main():
    from pathlib import Path
    tmp = Path("aws-saa-book/_build/tmp/status-report.txt").resolve()
    tmp.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(TOOL + ["status", "--out", str(tmp)], capture_output=True, text=True)
    lines = tmp.read_text().strip().split("\n")
    rows = [l.split() for l in lines[1:] if l.strip() and l[:2].isdigit()]
    out = ["# SAA-C03 Handbook: build status", "", f"Generated {time.strftime('%Y-%m-%d %H:%M %Z')} from the ledger by `status_report.py`.", ""]
    total, ready, facts_done, need_facts = 0, 0, 0, 0
    table = ["| Ch | Slug | Template | State | Next stage | Facts verified | Questions |", "|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: r[0]):
        cid, slug, tpl, wave, state = r[:5]
        nxt = next((x.split("=", 1)[1] for x in r if x.startswith("next=")), "")
        facts = next((x.split("=", 1)[1] for x in r if x.startswith("facts=")), "")
        q = next((x.split("=", 1)[1] for x in r if x.startswith("q=")), "")
        if state == "ready":
            done = 100
        else:
            try:
                s = json.loads(sh(["stage", "show", cid])); s = s.get("stages", s)
            except json.JSONDecodeError:
                s = {}
            done = sum(W[k] for k, v in s.items() if k in W and isinstance(v, dict) and v.get("status") == "pass")
        total += done
        ready += state == "ready"
        if tpl not in ("synthesis", "mock"):
            need_facts += 1
            facts_done += state in ("ready", "facts-verified", "drafted", "reviewed")
        table.append(f"| {cid} | {slug} | {tpl} | {state} | {nxt or '-'} | {facts} | {q} |")
    n = len(rows) or 1
    out += ["## Progress", "", "| Measure | Value |", "|---|---|",
            f"| Overall, weighted by the 16 ledger stages | {total / n:.1f}% |",
            f"| Chapters ready (final gate passed) | {ready} of {n} |",
            f"| Fact bases verified (chapters that mine their own facts) | {facts_done} of {need_facts} |", ""]
    vf = 0
    for f in glob.glob("aws-saa-book/data/facts/*.jsonl"):
        for line in open(f):
            if '"status": "verified"' in line or '"status":"verified"' in line:
                vf += 1
    words = 0
    for f in glob.glob("aws-saa-book/[0-9][0-9]-*/1-fast.md") + glob.glob("aws-saa-book/[0-9][0-9]-*/2-deep.md"):
        words += len(open(f).read().split())
    out += ["| Book totals | Value |", "|---|---|", f"| Verified facts | {vf:,} |", f"| Hand-written words (fast and deep files) | {words:,} |", ""]
    out += ["## Chapters", ""] + table + [""]
    hosts, guides, urls = Counter(), Counter(), set()
    try:
        for line in open("aws-saa-book/_build/corpus/fetch.log.jsonl"):
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            u = d.get("url", "")
            if not u or u in urls or d.get("status") not in (200, 304):
                continue
            urls.add(u)
            p = urlparse(u)
            hosts[p.netloc] += 1
            if p.netloc == "docs.aws.amazon.com":
                guides[p.path.strip("/").split("/")[0]] += 1
    except FileNotFoundError:
        pass
    snaps = len(glob.glob("aws-saa-book/_build/corpus/snap/**/*", recursive=True))
    out += ["## Downloaded AWS pages (the corpus)", "",
            f"{len(urls):,} unique pages fetched with status 200, saved under `aws-saa-book/_build/corpus/` ({snaps:,} snapshot files). "
            "Every verified fact quotes one of these snapshots and checks its SHA-256, so the corpus travels with the repository and is never re-fetched.", "",
            "| Host | Pages |", "|---|---|"] + [f"| {h} | {c:,} |" for h, c in hosts.most_common()] + ["",
            f"Documentation guides covered: {len(guides)}. Largest: " + ", ".join(f"{g} ({c})" for g, c in guides.most_common(15)) + ".", "",
            "Not downloaded yet: the pages for the chapters whose state is `planned` above. Their plan agents fetch them (only pages not already in the corpus).", ""]
    print("\n".join(out))


if __name__ == "__main__":
    main()
