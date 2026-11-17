"""register-17: after-run checks: counts, open conflicts of the chapter, display rule, shared quotes."""
import json, re, sys, collections
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
sys.path.insert(0, ROOT + "/tools")
from saalib.common import normalize_text  # noqa: E402
from saalib import lint  # noqa: E402
facts = []
for s in ["ec2-auto-scaling", "aws-auto-scaling"]:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        if line.strip():
            facts.append(json.loads(line))
print(collections.Counter(f["status"] for f in facts))
live = {f["id"]: f for f in facts if f["status"] not in ("rejected", "superseded")}
print("live", len(live), "hard", sum(1 for f in live.values() if f["hard"]),
      "rel", dict(collections.Counter(f.get("exam_relevance") for f in live.values())),
      "no scope", sum(1 for f in live.values() if not (f.get("qualifiers") or {}).get("scope")),
      "no bullets", [i for i, f in live.items() if not f.get("bullets")])
opn = []
for line in open(ROOT + "/_build/facts/conflicts.jsonl"):
    c = json.loads(line)
    if c["status"] == "open" and any(x in live for x in c["facts"]):
        opn.append(c)
print("open conflicts of the chapter:", len(opn))
for c in opn:
    print("  ", c["id"], c["facts"])
NUM = re.compile(r"(?<![A-Za-z])\d")
bad = 0
for i, f in live.items():
    qs = [normalize_text(e.get("quote") or "") for e in f["evidence"]]
    for v in f["values"]:
        d = v["display"]
        if not NUM.search(d) and (len(d.split()) > 8 or not any(lint.holds_display(q, normalize_text(d)) for q in qs)):
            bad += 1
            print("  display rule:", i, v["key"], d)
print("display rule breaks:", bad)
qmap = collections.defaultdict(set)
for f in live.values():
    for e in f["evidence"]:
        qmap[(e["source_id"], e["quote"])].add(f["id"])
print("quotes shared by two or more live facts:", sum(1 for v in qmap.values() if len(v) > 1))
for k, v in qmap.items():
    if len(v) > 1:
        print("  ", sorted(v), "|", k[1][:90])
