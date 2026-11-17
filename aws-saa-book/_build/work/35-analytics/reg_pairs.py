"""register-35: looser similarity scan across miner labels (read-only); prints pairs with both claims."""
import json, re, sys

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
SERVICES = ["athena", "glue", "lake-formation", "emr", "opensearch", "quick", "data-exchange"]
TH = float(sys.argv[1]) if len(sys.argv) > 1 else 0.35
OUT = sys.argv[2]
facts = {}
for s in SERVICES:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        if line.strip():
            f = json.loads(line)
            if f["status"] not in ("rejected", "superseded") and str(f.get("home_chapter")) == "35":
                facts[f["id"]] = f
STOP = set("the and for you can are that with this your from not use when have has its into all any amazon aws athena glue emr opensearch quick lake formation data exchange service sight".split())


def toks(s):
    return set(w for w in re.findall(r"[a-z]+", (s or "").lower()) if len(w) > 2) - STOP


ids = sorted(facts)
T = {i: toks(facts[i]["claim"]) for i in ids}
out = []
for a in range(len(ids)):
    for b in range(a + 1, len(ids)):
        fa, fb = facts[ids[a]], facts[ids[b]]
        if fa["service"] != fb["service"] or fa["kind"] in ("quota", "change") or fb["kind"] in ("quota", "change"):
            continue
        if fa.get("author") == fb.get("author"):
            continue
        x, y = T[ids[a]], T[ids[b]]
        if not x or not y:
            continue
        j = len(x & y) / len(x | y)
        if j >= TH:
            out.append("%.2f %s <> %s\n  A: %s\n  B: %s" % (j, ids[a], ids[b], fa["claim"][:220], fb["claim"][:220]))
open(OUT, "w").write("\n".join(out) + "\n")
print(len(out))
