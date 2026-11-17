"""register-23: read-only analysis of chapter 23 facts. Writes reg-*.txt files in this folder."""
import json, re, sys, collections, glob, os
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
sys.path.insert(0, ROOT + "/tools")
from saalib.common import normalize_text  # noqa: E402
W = ROOT + "/_build/work/23-efs-fsx/"

facts = {}
for p in glob.glob(ROOT + "/data/facts/*.jsonl"):
    for line in open(p):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f
ch = {i: f for i, f in facts.items() if f.get("home_chapter") == "23"}
live = {i: f for i, f in ch.items() if f["status"] not in ("rejected", "superseded")}
print("chapter facts", len(ch), "live", len(live))
print("by service", collections.Counter(f["service"] for f in live.values()))
print("by status", collections.Counter(f["status"] for f in ch.values()))
print("by kind", collections.Counter(f["kind"] for f in live.values()))
print("hard", collections.Counter(bool(f.get("hard")) for f in live.values()))
print("relevance", collections.Counter(f.get("exam_relevance") for f in live.values()))

NAME = re.compile(r"\b(S3|EC2|x86_64|arm64|IPv4|IPv6|NFSv4|NFSv4\.0|NFSv4\.1|NFSv3|SMB|Lustre|ONTAP|OpenZFS|2049|SSD|HDD)\b")
NUMW = re.compile(r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|half|percent)\b", re.I)
flags = collections.defaultdict(list)
for i, f in sorted(live.items()):
    nq = [normalize_text(e.get("quote") or "") for e in f["evidence"]]
    for v in f["values"]:
        d = v["display"]
        dn = normalize_text(d)
        sd = re.sub(r"\b[A-Za-z]+[0-9][A-Za-z0-9.]*\b", "", d)
        numeric = bool(re.search(r"\d", sd)) or bool(NUMW.search(sd))
        if not numeric and not any(dn in q for q in nq):
            flags["display-paraphrase"].append((i, d))
        if not numeric and len(d.split()) > 8:
            flags["display-long"].append((i, d))
    q = f.get("qualifiers") or {}
    if not str(q.get("scope") or "").strip():
        flags["no-scope"].append((i, f["kind"]))
    if f["kind"] in ("limit", "quota", "default") and not q.get("default_or_max"):
        flags["no-default_or_max"].append((i, f["kind"]))
    if f.get("hard") and not f.get("question"):
        flags["hard-no-question"].append((i, ""))
    if not f.get("exam_relevance"):
        flags["no-relevance"].append((i, ""))
    pre = i.split("-")[0]
    if pre != f["service"]:
        flags["id-prefix-vs-service"].append((i, f["service"]))
    if not f.get("bullets"):
        flags["no-bullets"].append((i, f["kind"]))
    if f["kind"] == "change":
        dates = re.findall(r"20\d\d-\d\d-\d\d", " ".join(v["display"] for v in f["values"]))
        if dates and max(dates) > "2026-07-15":
            flags["change-after-cutoff"].append((i, "%s rel=%s" % (max(dates), f.get("exam_relevance"))))
    if f["kind"] == "case-study" and f.get("exam_relevance") != "reference":
        flags["case-study-relevance"].append((i, f.get("exam_relevance")))

with open(W + "reg-flags.txt", "w") as o:
    for k, lst in flags.items():
        o.write("## %s (%d)\n" % (k, len(lst)))
        for i, d in lst:
            o.write("  %s | %s\n" % (i, d))
for k, lst in flags.items():
    print("flag", k, len(lst))

# duplicates: same source and overlapping match span, or same normalised quote
spans = collections.defaultdict(list)
for i, f in live.items():
    for e in f["evidence"]:
        m = e.get("match") or [0, 0]
        spans[e["source_id"]].append((m[0], m[1], i))
groups = []
seen_pairs = set()
for sid, lst in spans.items():
    lst.sort()
    for a in range(len(lst)):
        for b in range(a + 1, len(lst)):
            if lst[b][0] >= lst[a][1]:
                break
            if lst[a][2] == lst[b][2]:
                continue
            ov = min(lst[a][1], lst[b][1]) - lst[b][0]
            short = min(lst[a][1] - lst[a][0], lst[b][1] - lst[b][0]) or 1
            pair = tuple(sorted((lst[a][2], lst[b][2])))
            if pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            groups.append((sid, pair, round(ov / short, 2)))
with open(W + "reg-overlaps.txt", "w") as o:
    for sid, (x, y), r in sorted(groups):
        fx, fy = live[x], live[y]
        o.write("%s %.2f\n  A %s [%s] %s | %s\n  B %s [%s] %s | %s\n" % (
            sid, r, x, fx["kind"], fx["claim"], [v["display"] for v in fx["values"]],
            y, fy["kind"], fy["claim"], [v["display"] for v in fy["values"]]))
print("overlap pairs", len(groups), "ratio>=0.8", sum(1 for g in groups if g[2] >= 0.8))

# open conflicts touching chapter facts
conf = [json.loads(l) for l in open(ROOT + "/_build/facts/conflicts.jsonl") if l.strip()]
oc = [c for c in conf if c["status"] == "open" and any(x in ch for x in c["facts"])]
with open(W + "reg-conflicts.txt", "w") as o:
    for c in oc:
        o.write(c["id"] + "\n")
        for x in c["facts"]:
            f = facts.get(x)
            if not f:
                o.write("  ? %s missing\n" % x)
                continue
            o.write("  %s [%s %s] %s | %s | scope=%s\n" % (x, f["status"], f["kind"], f["claim"],
                    [v["display"] for v in f["values"]], (f.get("qualifiers") or {}).get("scope")))
print("open conflicts for ch23", len(oc), "all open", sum(1 for c in conf if c["status"] == "open"))

# compact dump
with open(W + "reg-compact.txt", "w") as o:
    for i, f in sorted(live.items()):
        q = f.get("qualifiers") or {}
        o.write("%s | %s | h=%s | %s | %s | scope=%s | %s\n" % (
            i, f["kind"], int(bool(f.get("hard"))), f.get("exam_relevance"),
            " ;; ".join(v["display"] for v in f["values"]), q.get("scope"), f["claim"]))
