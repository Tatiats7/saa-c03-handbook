"""register-23: claim-similarity pairs of live chapter 23 facts that the span scan did not catch (read-only)."""
import json, re, glob, itertools
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/23-efs-fsx/"
facts = {}
for p in glob.glob(ROOT + "/data/facts/*.jsonl"):
    for line in open(p):
        if line.strip():
            f = json.loads(line)
            if f.get("home_chapter") == "23" and f["status"] not in ("rejected", "superseded"):
                facts[f["id"]] = f
STOP = set("the a an and or of to in for on with is are be by that this it its your you can as from at not which when".split())


def toks(s):
    return {t for t in re.findall(r"[a-z0-9.]+", s.lower()) if t not in STOP}


span_pairs = set()
cur = []
for line in open(W + "reg-overlaps.txt"):
    m = re.match(r"\s+[AB] (\S+)", line)
    if m:
        cur.append(m.group(1))
        if len(cur) == 2:
            span_pairs.add(frozenset(cur))
            cur = []
for line in open(ROOT + "/_build/facts/conflicts.jsonl"):
    if line.strip():
        c = json.loads(line)
        span_pairs.add(frozenset(c["facts"]))
toks_by = {i: toks(f["claim"]) for i, f in facts.items()}
out = []
ids = sorted(facts)
for a, b in itertools.combinations(ids, 2):
    ta, tb = toks_by[a], toks_by[b]
    if not ta or not tb:
        continue
    j = len(ta & tb) / len(ta | tb)
    if j >= 0.5 and frozenset((a, b)) not in span_pairs:
        sa = facts[a]["evidence"][0]["source_id"]
        sb = facts[b]["evidence"][0]["source_id"]
        out.append((round(j, 2), a, b, sa, sb))
out.sort(reverse=True)
with open(W + "reg-similar.txt", "w") as o:
    for j, a, b, sa, sb in out:
        fa, fb = facts[a], facts[b]
        o.write("%.2f %s\n  A %s [%s] %s | %s\n  B %s [%s] %s | %s\n" % (
            j, "same-src" if sa == sb else sa + " vs " + sb,
            a, fa["kind"], fa["claim"], [v["display"] for v in fa["values"]],
            b, fb["kind"], fb["claim"], [v["display"] for v in fb["values"]]))
print(len(out))
