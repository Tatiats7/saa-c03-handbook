"""register-26: read-only dump and analysis of chapter 26 facts (writes only the two files named on the command line)."""
import json, re, sys, collections

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
sys.path.insert(0, ROOT + "/tools")
from saalib.common import normalize_text  # noqa: E402

DUMP, OUT = sys.argv[1], sys.argv[2]

facts = {}
for p in [ROOT + "/data/facts/rds.jsonl", ROOT + "/data/facts/rds-proxy.jsonl"]:
    for line in open(p):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f
live = {i: f for i, f in facts.items() if f["status"] not in ("rejected", "superseded")}

d = []
for i in sorted(live):
    f = live[i]
    q = f.get("qualifiers") or {}
    d.append("=== %s | %s | %s | hard=%s | %s | %s | by=%s | bul=%s" % (i, f["service"], f["kind"], f.get("hard"), f.get("exam_relevance"), f.get("volatility"), f.get("author"), ",".join(f.get("bullets") or [])))
    d.append("C: " + f["claim"])
    d.append("Q: " + (f.get("question") or ""))
    d.append("V: " + " || ".join("%s=%s" % (v.get("key"), v.get("display")) for v in f.get("values", [])))
    d.append("S: scope=%r dom=%r adj=%r cond=%r" % (q.get("scope"), q.get("default_or_max"), q.get("adjustable"), q.get("condition")))
    for e in f["evidence"]:
        d.append("E: [%s] %s%s" % (e["source_id"], ("H{%s} " % e["table_header"]) if e.get("table_header") else (("HD{%s} " % e["heading"]) if e.get("heading") else ""), e["quote"]))
    if f.get("changed"):
        d.append("CH: %s" % json.dumps(f["changed"]))
    if f.get("change_items"):
        d.append("CI: %s" % json.dumps(f["change_items"]))
open(DUMP, "w").write("\n".join(d) + "\n")


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())).strip()


def toks(s):
    return set(w for w in re.findall(r"[a-z]+", (s or "").lower()) if len(w) > 2)


STOP = set("the and for you can are that with this your from not use when have has its into all any amazon rds instance instances".split())
out = []
w = out.append
w("STATUS %s" % dict(collections.Counter(f["status"] for f in facts.values())))
w("LIVE %d  hard %d" % (len(live), sum(1 for f in live.values() if f.get("hard"))))
w("services %s" % dict(collections.Counter(f["service"] for f in live.values())))
w("kinds %s" % dict(collections.Counter(f["kind"] for f in live.values())))
w("relevance %s" % dict(collections.Counter(f.get("exam_relevance") for f in live.values())))
w("authors %s" % dict(collections.Counter(f.get("author") for f in live.values())))

w("\n## NAMESPACE (id prefix vs service)")
for i, f in sorted(live.items()):
    if i.startswith("rds-proxy-") and f["service"] != "rds-proxy":
        w("%s service=%s" % (i, f["service"]))
    if f["service"] == "rds-proxy" and not i.startswith("rds-proxy-"):
        w("%s service=%s" % (i, f["service"]))

w("\n## DISPLAY ISSUES (number-free: > 8 words or not verbatim in a quote)")
nbad = 0
for i, f in sorted(live.items()):
    quotes = [normalize_text(e.get("quote") or "").lower() for e in f["evidence"]]
    for v in f.get("values", []):
        dd = v.get("display", "")
        if re.search(r"\d", dd):
            continue
        nw = len(dd.split())
        nd = normalize_text(dd).lower()
        inq = any(nd and nd in q for q in quotes)
        if nw > 8 or not inq:
            nbad += 1
            w("%s | key=%s | words=%d | inquote=%s | %s" % (i, v.get("key"), nw, inq, dd))
w("display issues: %d" % nbad)

w("\n## EMPTY SCOPE")
for i, f in sorted(live.items()):
    q = f.get("qualifiers") or {}
    if not q.get("scope"):
        w("%s %s" % (i, f["kind"]))

w("\n## HARD FALSE but claim has digit or absolute word")
ABS = ["only", "always", "never", "cannot", "can't", "must", "by default", "up to", "at most", "not supported", "can not", "isn't supported", "aren't supported", "doesn't support", "don't support"]
for i, f in sorted(live.items()):
    c = " " + f["claim"].lower() + " "
    if not f.get("hard") and (re.search(r"\d", c) or any(" %s " % a in c for a in ABS)):
        w("%s kind=%s : %s" % (i, f["kind"], f["claim"][:170]))
w("\n## HARD TRUE without question")
for i, f in sorted(live.items()):
    if f.get("hard") and not f.get("question"):
        w(i)

w("\n## SAME QUOTE")
byq = collections.defaultdict(list)
for i, f in live.items():
    for e in f["evidence"]:
        byq[(e["source_id"], norm(e["quote"]))].append(i)
for k, ids in sorted(byq.items(), key=lambda x: sorted(set(x[1]))):
    if len(set(ids)) > 1:
        w("%s :: %s" % (sorted(set(ids)), k[1][:140]))

w("\n## OVERLAPPING QUOTE SPANS (same source)")
spans = collections.defaultdict(list)
for i, f in live.items():
    for e in f["evidence"]:
        m = e.get("match")
        if isinstance(m, dict):
            m = [m.get("start"), m.get("end")]
        if m and isinstance(m, (list, tuple)) and len(m) >= 2 and all(isinstance(x, int) for x in m[:2]):
            spans[e["source_id"]].append((m[0], m[1], i))
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

w("\n## SIMILAR CLAIMS (jaccard >= 0.4)")
ids = sorted(live)
T = {i: toks(live[i]["claim"]) - STOP for i in ids}
for a in range(len(ids)):
    for b in range(a + 1, len(ids)):
        x, y = T[ids[a]], T[ids[b]]
        if not x or not y:
            continue
        j = len(x & y) / len(x | y)
        if j >= 0.4 and tuple(sorted((ids[a], ids[b]))) not in pairs:
            w("%.2f %s  <>  %s" % (j, ids[a], ids[b]))
open(OUT, "w").write("\n".join(out) + "\n")
print("dump", len(d), "analysis", len(out))
