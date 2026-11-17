"""register-12: read-only analysis of the chapter 12 facts (adapted from register-19).

Flags: number-free displays over 8 words or not held by a quote; empty scope;
pairs that share a quote sentence or have a high claim-token similarity.
Writes reg-analysis.txt in this folder.
"""
import json, re, sys, itertools, collections
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
sys.path.insert(0, ROOT + "/tools")
from saalib.common import normalize_text  # noqa: E402

W = ROOT + "/_build/work/12-hybrid-networking/"
SVCS = ["site-to-site-vpn", "direct-connect", "client-vpn"]
facts = {}
for s in SVCS:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f
live = {i: f for i, f in facts.items() if f["status"] not in ("rejected", "superseded") and f.get("home_chapter") == "12"}
other_home = [i for i, f in facts.items() if f["status"] not in ("rejected", "superseded") and f.get("home_chapter") != "12"]

NAME = re.compile(r"\b(S3|EC2|IPv4|IPv6|IKEv1|IKEv2|SAML 2\.0|Route 53|AES\d*|SHA\d*)\b")
NUMW = re.compile(r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\b", re.I)
out = open(W + "reg-analysis.txt", "w")
out.write("LIVE %d; live facts of these services with another home chapter: %s\n" % (len(live), other_home))
long_disp = []
for i, f in sorted(live.items()):
    nq = [normalize_text(e["quote"]) for e in f["evidence"]]
    for v in f.get("values", []):
        d = v["display"]
        stripped = NAME.sub("", d)
        numeric = bool(re.search(r"\d", stripped)) or bool(NUMW.search(stripped))
        dn = normalize_text(d)
        inq = any(dn in q for q in nq)
        if not numeric and len(d.split()) > 8:
            long_disp.append((i, d, inq))
        elif not numeric and not inq:
            long_disp.append((i, d, inq))
out.write("LONG OR NOT-IN-QUOTE NUMBER-FREE DISPLAYS: %d\n" % len(long_disp))
for i, d, inq in long_disp:
    out.write("  %s :: %s%s\n" % (i, d, "" if inq else "   [NOT IN QUOTE]"))

out.write("\nEMPTY SCOPE:\n")
for i, f in sorted(live.items()):
    if not (f.get("qualifiers") or {}).get("scope"):
        out.write("  %s %s\n" % (i, f["kind"]))

out.write("\nNO VALUES:\n")
for i, f in sorted(live.items()):
    if not f.get("values"):
        out.write("  %s\n" % i)

out.write("\nRELEVANCE COUNTS: %s\n" % dict(collections.Counter(f.get("exam_relevance") for f in live.values())))
out.write("HARD COUNTS: %s\n" % dict(collections.Counter(f.get("hard") for f in live.values())))
out.write("KIND COUNTS: %s\n" % dict(collections.Counter(f.get("kind") for f in live.values())))

out.write("\nSHARED QUOTE SENTENCES:\n")
sent = collections.defaultdict(set)
for i, f in live.items():
    for e in f["evidence"]:
        for s in re.split(r"(?<=[.!?])\s+", normalize_text(e["quote"])):
            if len(s.split()) >= 6:
                sent[(e["source_id"], s)].add(i)
pairs = collections.Counter()
for k, ids in sent.items():
    if len(ids) > 1:
        for a, b in itertools.combinations(sorted(ids), 2):
            pairs[(a, b)] += 1
for (a, b), n in sorted(pairs.items()):
    out.write("  %s <> %s (%d)\n" % (a, b, n))


def toks(c):
    return set(t for t in re.findall(r"[a-z]+", c.lower()) if len(t) > 2)


out.write("\nSIMILAR CLAIMS (same service, jaccard>=0.45, not above):\n")
bysvc = collections.defaultdict(list)
for i, f in live.items():
    bysvc[f["service"]].append(i)
for s, ids in bysvc.items():
    for a, b in itertools.combinations(sorted(ids), 2):
        if (a, b) in pairs:
            continue
        ta, tb = toks(live[a]["claim"]), toks(live[b]["claim"])
        j = len(ta & tb) / max(1, len(ta | tb))
        if j >= 0.45:
            out.write("  %.2f %s <> %s\n" % (j, a, b))
out.close()
print("live", len(live), "long", len(long_disp), "pairs", len(pairs))
