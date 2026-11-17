"""Helper for brief-19: show facts, list evidence URLs, check brief.json fact ids.

Usage:
  python3 aws-saa-book/_build/work/19-containers/brief19_tool.py urls SERVICE...
  python3 aws-saa-book/_build/work/19-containers/brief19_tool.py show ID...
  python3 aws-saa-book/_build/work/19-containers/brief19_tool.py check
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FACTS = ROOT / "data" / "facts"
WORK = ROOT / "_build" / "work" / "19-containers"


def load():
    out = {}
    for f in sorted(FACTS.glob("*.jsonl")):
        for line in f.read_text().splitlines():
            if line.strip():
                x = json.loads(line)
                out[x["id"]] = x
    return out


def ev_urls(x):
    ev = x.get("evidence")
    evs = ev if isinstance(ev, list) else [ev] if ev else []
    return [e.get("url") for e in evs if isinstance(e, dict)]


def main():
    cmd = sys.argv[1]
    facts = load()
    if cmd == "urls":
        for svc in sys.argv[2:]:
            urls = {}
            for x in facts.values():
                if x.get("service") == svc and x.get("status") == "verified":
                    for u in ev_urls(x):
                        urls.setdefault(u, []).append(x["id"])
            for u, ids in urls.items():
                print(svc, u, len(ids), ids[:4])
    elif cmd == "show":
        for i in sys.argv[2:]:
            x = facts.get(i)
            if not x:
                print(i, "MISSING")
                continue
            ev = x.get("evidence")
            evs = ev if isinstance(ev, list) else [ev]
            print(i, x.get("status"), x.get("kind"), x.get("hard"))
            for e in evs:
                print("   url:", e.get("url"), "| heading:", e.get("heading"))
                print("   quote:", e.get("quote"))
            print("   displays:", [v.get("display") for v in x.get("values") or []])
            print("   changed:", x.get("changed"))
    elif cmd == "check":
        brief = json.loads((WORK / "brief.json").read_text())
        text = json.dumps(brief, ensure_ascii=False)
        known = set(facts)
        cands = set(re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)+", text))
        prefixes = ("ecs-", "eks-", "ecr-", "fargate-", "lambda-", "ec2-", "elb-", "vpc-", "iam-")
        used = sorted(c for c in cands if c in known)
        bad = [c for c in used if facts[c].get("status") != "verified"]
        print("fact ids named:", len(used))
        print("not verified:", bad)
        # ids that look like facts but are unknown
        trap_ids = {t["id"] for t in brief.get("traps", [])}
        sec_ids = {s["section"] for s in brief.get("sections", [])}
        odd = sorted(c for c in cands if c.startswith(prefixes) and c not in known and c not in trap_ids
                     and c not in sec_ids and "-trap-" not in c and not re.match(r"^(ecs|eks)-anywhere$", c))
        print("unknown fact-like ids:", odd)
        # display check for [text] (fact-id) pairs
        pairs = re.findall(r"\[([^\]]+)\] \(([a-z0-9-]+)\)", text)
        miss = []
        for disp, fid in pairs:
            x = facts.get(fid)
            if not x:
                continue
            ds = [str(v.get("display", "")).lower() for v in x.get("values") or []]
            if not any(d and d in disp.lower() for d in ds):
                miss.append((disp, fid, ds))
        loose = re.findall(r"\[([^\]]+)\]([^\[\]]{0,200}?)\(([a-z0-9]+(?:-[a-z0-9]+)+)\)", text)
        for disp, _gap, fid in loose:
            x = facts.get(fid)
            if not x or (disp, fid) in [(m[0], m[1]) for m in miss]:
                continue
            ds = [str(v.get("display", "")).lower() for v in x.get("values") or []]
            if not any(d and d in disp.lower() for d in ds):
                miss.append((disp, fid, ds))
        print("bracket texts without a display:", len(miss))
        for m in miss:
            print("   ", m)
        print("sections:", len(brief.get("sections", [])), "traps:", len(brief.get("traps", [])),
              "slots:", len(brief.get("question_slots", [])))


if __name__ == "__main__":
    main()
