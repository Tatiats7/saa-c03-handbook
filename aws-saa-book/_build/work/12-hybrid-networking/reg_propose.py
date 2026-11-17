"""register-12: propose a short display (<= 8 words, a contiguous window of the old display, so it stays
verbatim in the quote) for every number-free display over 8 words. Read-only; writes reg-proposals.json and
reg-proposals.txt. The registrar reviews the proposals and overrides them in reg-decisions.json.
"""
import json, re, sys
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
live = {i: f for i, f in facts.items() if f["status"] not in ("rejected", "superseded")}
STOP_START = {"and", "or", "that", "which", "to", "of", "for", "with", "by", "in", "on", "at", "as", "if", "so", "but", "than"}
STOP_END = {"the", "a", "an", "of", "to", "and", "or", "for", "with", "your", "that", "by", "in", "on", "at", "is", "are", "be", "can", "you", "will", "as", "from", "its", "their", "this", "these", "when", "if", "not"}
KEY = {"not", "cannot", "can't", "only", "must", "no", "never", "always", "free", "default", "automatically", "doesn't", "don't", "won't"}
SVC_WORDS = {"site", "vpn", "direct", "connect", "client", "faq", "limit", "quota", "default", "change", "behavior", "restriction", "capability", "pricing", "billing"}
NAME = re.compile(r"\b(S3|EC2|IPv4|IPv6|IKEv1|IKEv2|SAML 2\.0|Route 53)\b")


def score(win, idt):
    w = [x.lower().strip(",.;:()\"'") for x in win]
    s = 0.0
    for x in w:
        if x in idt:
            s += 2
        if x in KEY:
            s += 2.5
    if w[0] in STOP_START:
        s -= 3
    if w[-1] in STOP_END:
        s -= 3
    s += 0.3 * len(w)
    return s


props = {}
for i, f in sorted(live.items()):
    if f.get("home_chapter") != "12":
        continue
    idt = set(t for t in i.split("-") if len(t) > 2) - SVC_WORDS
    for v in f.get("values", []):
        d = v["display"]
        if re.search(r"\d", NAME.sub("", d)):
            continue
        words = d.split()
        if len(words) <= 8:
            continue
        best = None
        for n in range(4, 9):
            for k in range(0, len(words) - n + 1):
                win = words[k:k + n]
                sc = score(win, idt)
                if best is None or sc > best[0]:
                    best = (sc, " ".join(win))
        new = best[1].rstrip(",;:")
        props.setdefault(i, {})[d] = new
json.dump(props, open(W + "reg-proposals.json", "w"), indent=1, ensure_ascii=False)
out = open(W + "reg-proposals.txt", "w")
for i in sorted(props):
    f = live[i]
    out.write("%s  [%s] C: %s\n" % (i, f["kind"], f["claim"][:200]))
    for d, n in props[i].items():
        out.write("    - %s\n    + %s\n" % (d, n))
out.close()
print("facts", len(props), "displays", sum(len(x) for x in props.values()))
