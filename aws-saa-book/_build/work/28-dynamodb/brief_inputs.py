"""Read-only helper of brief-28: summarise the inputs of the brief.
Usage: python3 aws-saa-book/_build/work/28-dynamodb/brief_inputs.py MODE [ARG]
Modes: v0 (demand by status), v0keys, vol, faq, changed, case, kinds, price, quote ID, other PREFIXES, startup, terms, spec, ee
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from saalib import facts as F  # noqa: E402

mode = sys.argv[1] if len(sys.argv) > 1 else "v0"
arg = sys.argv[2] if len(sys.argv) > 2 else ""


def load(svcs):
    rows = []
    for svc in svcs:
        p = ROOT / "data" / "facts" / f"{svc}.jsonl"
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            if line.strip():
                f = json.loads(line)
                if f.get("status") == "verified":
                    rows.append(f)
    return rows


if mode == "v0":
    v0 = json.loads((HERE / "brief.v0.json").read_text())
    from collections import Counter
    print(Counter(d.get("status") for d in v0["demand"]))
    for d in v0["demand"]:
        if d.get("status") not in ("found",):
            print(f"{d['id']} [{d.get('status')}] {d.get('bullet')} | {d['question'][:200]} | {d.get('facts')} | {str(d.get('note', ''))[:200]}")
elif mode == "v0keys":
    v0 = json.loads((HERE / "brief.v0.json").read_text())
    for k, v in v0.items():
        print(k, type(v).__name__, (len(v) if hasattr(v, "__len__") else v))
    print(json.dumps(v0["demand"][0], indent=1))
    for k in v0:
        if k not in ("demand", "fetch_pending", "fetch_batches", "fetch_results"):
            print(k, json.dumps(v0[k])[:1500])
elif mode in ("vol", "faq", "changed", "case", "kinds", "price", "hardkinds"):
    rows = load(["dynamodb", "dax"])
    from collections import Counter
    if mode == "kinds":
        print(Counter(f["kind"] for f in rows), len(rows), sum(1 for f in rows if F.is_volatile(f)))
    for f in rows:
        ev = f["evidence"][0]["url"]
        vol = F.is_volatile(f)
        ch = f.get("changed") or {}
        disp = [v["display"] for v in f.get("values") or []]
        if mode == "vol" and vol:
            print(f"{f['id']} ({f.get('volatility')}{', changed ' + ch.get('date', '') if ch else ''})")
        elif mode == "faq" and "faq" in ev:
            print(f"{f['id']} | {f['kind']} | {'VOL' if vol else ''} | {disp} | Q: {f['evidence'][0]['quote'][:300]}")
        elif mode == "changed" and ch:
            print(f"{f['id']} | changed {ch.get('date')} was {ch.get('was')!r} | {'VOL' if vol else ''} | {disp}")
        elif mode == "case" and f["kind"] == "case-study":
            print(f"{f['id']} | {ev} | {f['evidence'][0]['quote']}")
        elif mode == "price" and f["kind"] == "price":
            print(f"{f['id']} | {disp}")
        elif mode == "hardkinds" and f.get("hard") and f["kind"] in ("behavior", "capability", "restriction", "default") and len(disp) < 2:
            print(f"{f['id']} | {f['kind']} | {disp}")
elif mode == "quote":
    for f in load(["dynamodb", "dax", "aurora", "rds", "lambda", "elasticache", "sqs", "sns", "apigateway", "kinesis", "s3", "eventbridge"]):
        if f["id"] == arg:
            print(json.dumps({"id": f["id"], "kind": f["kind"], "hard": f.get("hard"), "volatile": F.is_volatile(f), "values": f.get("values"),
                              "changed": f.get("changed"), "evidence": [{"url": e["url"], "quote": e["quote"], "heading": e.get("heading")} for e in f["evidence"]]}, indent=1))
elif mode == "other":
    for f in load(arg.split(",")):
        vol = F.is_volatile(f)
        print(f"{f['id']} [{f.get('home_chapter')}]{' VOL' if vol else ''} | {f['claim'][:170]} | {[v['display'] for v in f.get('values') or []]}")
elif mode == "grep":
    # grep SVC1,SVC2 WORD1|WORD2 : verified facts of other services whose claim or id holds a word
    svcs, words = arg.split(","), (sys.argv[3] if len(sys.argv) > 3 else "").lower().split("|")
    for f in load(svcs):
        text = (f["id"] + " " + f["claim"]).lower()
        if any(w in text for w in words):
            print(f"{f['id']} [{f.get('home_chapter')}]{' VOL' if F.is_volatile(f) else ''} | {f['claim'][:200]} | {[v['display'] for v in f.get('values') or []]}")
elif mode == "startup":
    s = json.loads((ROOT / "data" / "startup.json").read_text())
    for k, v in s.items():
        if k != "chapters":
            print(k, json.dumps(v)[:800])
    ch = s.get("chapters")
    if isinstance(ch, dict):
        print(json.dumps(ch.get("28"), indent=1))
    elif isinstance(ch, list):
        for c in ch:
            if str(c.get("chapter")) == "28" or c.get("id") == "28":
                print(json.dumps(c, indent=1))
elif mode == "terms":
    t = json.loads((ROOT / "data" / "terms.json").read_text())
    for x in t["terms"]:
        if not arg or arg.lower() in json.dumps(x).lower():
            print(json.dumps(x)[:400])
elif mode == "ee":
    p = ROOT / "data" / "exam-english.json"
    if not p.exists():
        for c in (ROOT / "data").rglob("*english*"):
            print(c)
    else:
        d = json.loads(p.read_text())
        items = d.get("words", d) if isinstance(d, dict) else d
        for w in items:
            print(w.get("id"), "|", w.get("word"), "|", str(w.get("meaning"))[:80])
elif mode == "spec":
    s = json.loads((ROOT / "_build" / "style" / "SPEC.json").read_text())
    if arg:
        cur = s
        for part in arg.split("."):
            cur = cur[part]
        print(json.dumps(cur, indent=1)[:20000])
    else:
        print(list(s.keys()))
