"""register-21: read-only analysis of chapter 21 facts (no writes outside --out)."""
import json, re, sys, glob, os, collections

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
OUT = sys.argv[1]

facts = {}
for p in glob.glob(ROOT + "/data/facts/*.jsonl"):
    for line in open(p):
        line = line.strip()
        if not line:
            continue
        f = json.loads(line)
        facts[f["id"]] = f  # last line wins

ch = {i: f for i, f in facts.items() if f.get("home_chapter") == "21" or f.get("service") in ("s3", "s3-glacier")}
live = {i: f for i, f in ch.items() if f["status"] not in ("rejected", "superseded")}

def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())).strip()

def toks(s):
    return set(w for w in re.findall(r"[a-z]+", (s or "").lower()) if len(w) > 2)

STOP = set("the and for you can are that with this your from not use when have has its into all any".split())

out = []
w = out.append
st = collections.Counter(f["status"] for f in ch.values())
w("STATUS %s" % dict(st))
w("LIVE %d  hard %d" % (len(live), sum(1 for f in live.values() if f.get("hard"))))
w("services %s" % dict(collections.Counter(f["service"] for f in live.values())))
w("home %s" % dict(collections.Counter(f.get("home_chapter") for f in live.values())))
w("kinds %s" % dict(collections.Counter(f["kind"] for f in live.values())))
w("authors %s" % dict(collections.Counter(f.get("author") for f in live.values())))
w("relevance %s" % dict(collections.Counter(f.get("exam_relevance") for f in live.values())))

# displays
w("\n## DISPLAY ISSUES (number-free > 8 words, or not verbatim in a quote)")
nbad = 0
for i, f in sorted(live.items()):
    quotes = [norm(e.get("quote")) for e in f["evidence"]] + [norm(e.get("table_header")) for e in f["evidence"]]
    for v in f.get("values", []):
        d = v.get("display", "")
        has_digit = bool(re.search(r"\d", d))
        nw = len(d.split())
        inq = any(norm(d) and norm(d) in q for q in quotes)
        if (not has_digit and (nw > 8 or not inq)):
            nbad += 1
            w("%s | key=%s | words=%d | inquote=%s | %s" % (i, v.get("key"), nw, inq, d))
w("display issues: %d" % nbad)

# qualifiers
w("\n## EMPTY SCOPE")
for i, f in sorted(live.items()):
    q = f.get("qualifiers") or {}
    if not q.get("scope"):
        w("%s %s" % (i, f["kind"]))

# hard consistency
w("\n## HARD CHECK (absolute words / numbers but hard false)")
ABS = ["only", "always", "never", "cannot", "can't", "must", "by default", "up to", "at most", "not supported"]
for i, f in sorted(live.items()):
    c = " " + f["claim"].lower() + " "
    if not f.get("hard") and (re.search(r"\d", c) or any(" %s " % a in c for a in ABS)):
        w("%s kind=%s : %s" % (i, f["kind"], f["claim"][:160]))

# duplicates: same quote or high jaccard
w("\n## SAME QUOTE")
byq = collections.defaultdict(list)
for i, f in live.items():
    for e in f["evidence"]:
        byq[(e["source_id"], norm(e["quote"]))].append(i)
for k, ids in byq.items():
    if len(set(ids)) > 1:
        w("%s :: %s" % (sorted(set(ids)), k[1][:120]))

w("\n## OVERLAPPING QUOTE SPANS (same source)")
spans = collections.defaultdict(list)
for i, f in live.items():
    for e in f["evidence"]:
        if e.get("match"):
            spans[e["source_id"]].append((e["match"][0], e["match"][1], i))
pairs = set()
for sid, L in spans.items():
    L.sort()
    for a in range(len(L)):
        for b in range(a + 1, len(L)):
            if L[b][0] >= L[a][1]:
                break
            if L[a][2] != L[b][2]:
                pairs.add(tuple(sorted((L[a][2], L[b][2]))))
for p in sorted(pairs):
    w("%s  <>  %s" % p)

w("\n## SIMILAR CLAIMS (jaccard >= 0.45)")
ids = sorted(live)
T = {i: toks(live[i]["claim"]) - STOP for i in ids}
for a in range(len(ids)):
    for b in range(a + 1, len(ids)):
        x, y = T[ids[a]], T[ids[b]]
        if not x or not y:
            continue
        j = len(x & y) / len(x | y)
        if j >= 0.45 and tuple(sorted((ids[a], ids[b]))) not in pairs:
            w("%.2f %s  <>  %s" % (j, ids[a], ids[b]))

open(OUT, "w").write("\n".join(out) + "\n")
print("written", OUT, len(out))
