"""Helper for brief-11: read the demand list, show facts, check brief.json.

Usage:
  python3 aws-saa-book/_build/work/11-vpc-connectivity/brief11_tool.py demand [all|open] OUT
  python3 aws-saa-book/_build/work/11-vpc-connectivity/brief11_tool.py show OUT ID...
  python3 aws-saa-book/_build/work/11-vpc-connectivity/brief11_tool.py grep OUT STATUS REGEX...
  python3 aws-saa-book/_build/work/11-vpc-connectivity/brief11_tool.py check OUT
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FACTS = ROOT / "data" / "facts"
WORK = ROOT / "_build" / "work" / "11-vpc-connectivity"


def load():
    out = {}
    for f in sorted(FACTS.glob("*.jsonl")):
        for line in f.read_text().splitlines():
            if line.strip():
                x = json.loads(line)
                out[x["id"]] = x
    return out


def evs(x):
    ev = x.get("evidence")
    return ev if isinstance(ev, list) else [ev] if ev else []


def fmt(x):
    lines = [f"{x['id']} | {x.get('status')} | {x.get('kind')} | hard={x.get('hard')} | home={x.get('home_chapter')}"]
    lines.append(f"   claim: {x.get('claim')}")
    for e in evs(x):
        if isinstance(e, dict):
            lines.append(f"   url: {e.get('url')} | heading: {e.get('heading')}")
            lines.append(f"   quote: {e.get('quote')}")
    lines.append(f"   displays: {[v.get('display') for v in x.get('values') or []]}")
    if x.get("changed"):
        lines.append(f"   changed: {x.get('changed')}")
    return "\n".join(lines)


def main():
    cmd = sys.argv[1]
    if cmd == "demand":
        mode, out = sys.argv[2], sys.argv[3]
        v0 = json.loads((WORK / "brief.v0.json").read_text())
        rows = []
        for d in v0["demand"]:
            if mode == "open" and d.get("status") == "filled":
                continue
            rows.append(f"{d['id']} [{d.get('status')}] {d.get('bullet')} {d.get('service')} {d.get('kind')}\n   Q: {d.get('question')}\n   facts: {d.get('facts')}\n   note: {d.get('note') or d.get('status_note') or ''}")
        extra = {k: v for k, v in v0.items() if k not in ("demand",)}
        Path(out).write_text(json.dumps(extra, indent=1, ensure_ascii=False) + "\n\n" + "\n".join(rows))
        print(len(rows), "rows")
    elif cmd == "show":
        out = sys.argv[2]
        facts = load()
        res = []
        for i in sys.argv[3:]:
            res.append(fmt(facts[i]) if i in facts else f"{i} MISSING")
        Path(out).write_text("\n".join(res))
        print(len(res), "facts")
    elif cmd in ("grep", "grepc"):
        out, status = sys.argv[2], sys.argv[3]
        pats = [re.compile(p, re.I) for p in sys.argv[4:]]
        facts = load()
        res = []
        for x in facts.values():
            if status != "any" and x.get("status") != status:
                continue
            blob = x["id"] + " " + (x.get("claim") or "")
            if all(p.search(blob) for p in pats):
                if cmd == "grepc":
                    res.append(f"{x['id']} [{x.get('home_chapter')}] {x.get('claim')} || {[v.get('display') for v in x.get('values') or []]}")
                else:
                    res.append(fmt(x))
        Path(out).write_text("\n".join(res))
        print(len(res), "facts")
    elif cmd == "check":
        out = sys.argv[2]
        facts = load()
        brief = json.loads((WORK / "brief.json").read_text())
        text = json.dumps(brief, ensure_ascii=False)
        cands = set(re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)+", text))
        used = sorted(c for c in cands if c in facts)
        bad = [c for c in used if facts[c].get("status") != "verified"]
        res = [f"fact ids named: {len(used)}", f"not verified: {bad}"]
        trap_ids = {t["id"] for t in brief.get("traps", [])}
        sec_ids = {s["section"] for s in brief.get("sections", [])}
        prefixes = ("vpc-", "transit-gateway-", "privatelink-", "vpc-endpoints-", "vpc-peering-", "elb-", "route53-", "dx-", "vpn-", "s3-", "dynamodb-", "ram-", "network-firewall-", "hybrid-")
        odd = sorted(c for c in cands if c.startswith(prefixes) and c not in facts and c not in trap_ids
                     and c not in sec_ids and "-trap-" not in c and not c.startswith("vpc-connectivity-"))
        res.append(f"unknown fact-like ids: {odd}")
        loose = re.findall(r"\[([^\]]+)\]([^\[\]]{0,200}?)\(([a-z0-9]+(?:-[a-z0-9]+)+)\)", text)
        miss = []
        for disp, _gap, fid in loose:
            x = facts.get(fid)
            if not x:
                continue
            ds = [str(v.get("display", "")).lower() for v in x.get("values") or []]
            if not any(d and d in disp.lower() for d in ds):
                miss.append((disp, fid, ds))
        res.append(f"bracket texts without a display: {len(miss)}")
        res += [f"    {m}" for m in miss]
        # every bullet in sections and slots
        res.append(f"sections: {len(brief.get('sections', []))} traps: {len(brief.get('traps', []))} slots: {len(brief.get('question_slots', []))}")
        Path(out).write_text("\n".join(res))
        print("\n".join(res[:3]))
        print(res[-1])


if __name__ == "__main__":
    main()
