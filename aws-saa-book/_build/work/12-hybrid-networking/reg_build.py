"""register-12: build amend patch files from reg-decisions.json (adapted from register-19).

Writes only under _build/work/12-hybrid-networking/reg-patches/ and reg-patch-ids.json. Reads data/facts/<service>.jsonl.
Checks every display of every live fact of chapter 12 after the patches: a display without a digit is held by a
normalised quote and has at most 8 words (RULINGS 2026-10-11); a display with a digit is held by a quote or the claim.
"""
import json, re, sys, copy, os
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
sys.path.insert(0, ROOT + "/tools")
from saalib.common import normalize_text  # noqa: E402

W = ROOT + "/_build/work/12-hybrid-networking/"
OUT = W + "reg-patches/"
os.makedirs(OUT, exist_ok=True)
SVCS = ["site-to-site-vpn", "direct-connect", "client-vpn"]
REL = {"core": 3, "extended": 2, "reference": 1, None: 0}

facts = {}
for s in SVCS:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f

D = json.load(open(W + "reg-decisions.json"))
problems = []
gone = {o for o, n, _ in D["supersede"]} | {r[0] for r in D["reject"]}
patch = {}


def P(i):
    if i not in facts:
        problems.append("unknown fact " + i)
        return None
    if i in gone:
        problems.append("edit on a fact that leaves: " + i)
    return patch.setdefault(i, {})


def cur(i, field):
    p = patch.get(i, {})
    return copy.deepcopy(p[field]) if field in p else copy.deepcopy(facts[i].get(field))


def window(display, new):
    """Return the original-text word window of display that normalises to new, or None."""
    words = display.split()
    target = normalize_text(new)
    for a in range(len(words)):
        for b in range(a + 1, len(words) + 1):
            w = " ".join(words[a:b]).rstrip(",;:.")
            if normalize_text(w) == target:
                return w
    return None


for i, news in D["short"].items():
    if not news:
        continue
    p = P(i)
    if p is None:
        continue
    vals = cur(i, "values")
    used = set()
    for new in news:
        hits = [(k, window(v["display"], new)) for k, v in enumerate(vals)]
        hits = [(k, w) for k, w in hits if w is not None and k not in used]
        if len(hits) != 1:
            problems.append("%s: short %r matches %d displays" % (i, new, len(hits)))
            continue
        k, w = hits[0]
        used.add(k)
        if vals[k]["display"] != w:
            vals[k]["display"] = w
            vals[k].pop("spoken", None)
    p["values"] = vals

for i, m in D.get("replace", {}).items():
    p = P(i)
    if p is None:
        continue
    vals = cur(i, "values")
    for old, new in m.items():
        hit = [v for v in vals if normalize_text(v["display"]).startswith(normalize_text(old))]
        if len(hit) != 1:
            problems.append("%s: replace %r matches %d displays" % (i, old, len(hit)))
            continue
        hit[0]["display"] = new
        hit[0].pop("spoken", None)
    p["values"] = vals

for i, lst in D.get("drop", {}).items():
    p = P(i)
    if p is None:
        continue
    vals = cur(i, "values")
    for old in lst:
        hit = [v for v in vals if normalize_text(v["display"]).startswith(normalize_text(old))]
        if len(hit) != 1:
            problems.append("%s: drop %r matches %d displays" % (i, old, len(hit)))
            continue
        vals.remove(hit[0])
    p["values"] = vals

for i, lst in D.get("add_values", {}).items():
    p = P(i)
    if p is None:
        continue
    vals = cur(i, "values")
    for k, d in lst:
        if any(v["key"] == k for v in vals):
            problems.append("%s: key exists %s" % (i, k))
            continue
        vals.append({"key": k, "display": d})
    p["values"] = vals

for i, m in D["patch"].items():
    p = P(i)
    if p is None:
        continue
    for k in ("claim", "note", "exam_relevance", "volatility", "hard", "kind", "question"):
        if k in m:
            p[k] = m[k]
    if "qualifiers" in m:
        q = cur(i, "qualifiers") or {}
        q.update(m["qualifiers"])
        p["qualifiers"] = q
    if "evidence_keep" in m or "evidence_add" in m:
        ev = cur(i, "evidence")
        keep = m.get("evidence_keep", list(range(len(ev))))
        new_ev = [{k: ev[j][k] for k in ("source_id", "url", "quote", "table_header", "heading") if ev[j].get(k)} for j in keep]
        for e in m.get("evidence_add", []):
            new_ev.append(dict(e))
        p["evidence"] = new_ev

# a kept fact takes the bullets, the higher relevance, hard true and the note of what it absorbs
for o, n, why in D["supersede"]:
    if n not in facts or o not in facts:
        problems.append("supersede pair unknown: %s -> %s" % (o, n))
        continue
    if n in gone:
        problems.append("supersede target leaves: %s" % n)
    fo = facts[o]
    b = cur(n, "bullets") or []
    nb = list(b)
    for x in fo.get("bullets") or []:
        if x not in nb:
            nb.append(x)
    if nb != b:
        P(n)["bullets"] = nb
    if REL[fo.get("exam_relevance")] > REL[cur(n, "exam_relevance")]:
        P(n)["exam_relevance"] = fo.get("exam_relevance")
    if fo.get("hard") and not cur(n, "hard"):
        P(n)["hard"] = True
        if not cur(n, "question"):
            P(n)["question"] = fo.get("question")
    on = (fo.get("note") or "").strip()
    nn = cur(n, "note") or ""
    tag = "Absorbed %s" % o
    if tag not in nn:
        P(n)["note"] = (nn + (" " if nn else "") + tag + (" (" + on + ")" if on else "") + ".").strip()


def check(i, vals, ev, claim, tag):
    nq = [normalize_text(e["quote"]) for e in ev]
    seen = set()
    for v in vals:
        d = v["display"]
        dn = normalize_text(d)
        if dn in seen:
            problems.append("%s %s: duplicate display %r" % (tag, i, d))
        seen.add(dn)
        if not re.search(r"\d", d):
            if not any(dn in q for q in nq):
                problems.append("%s %s: number-free display not in a quote %r" % (tag, i, d))
            if len(d.split()) > 8:
                problems.append("%s %s: display over 8 words %r" % (tag, i, d))
        else:
            if not any(dn in q for q in nq) and dn not in normalize_text(claim):
                problems.append("%s %s: display in neither quote nor claim %r" % (tag, i, d))
    if not vals:
        problems.append("%s %s: no display left" % (tag, i))


for i, f in sorted(facts.items()):
    if f["status"] in ("rejected", "superseded") or i in gone or f.get("home_chapter") != "12":
        continue
    p = patch.get(i, {})
    check(i, p.get("values", f["values"]), p.get("evidence", f["evidence"]), p.get("claim", f["claim"]),
          "PATCHED" if i in patch else "UNTOUCHED")

for name in os.listdir(OUT):
    os.remove(OUT + name)
for i, p in sorted(patch.items()):
    json.dump(p, open(OUT + i + ".json", "w"), indent=1, ensure_ascii=False)
json.dump(sorted(patch), open(W + "reg-patch-ids.json", "w"), indent=1)
print("patches", len(patch), "supersede", len(D["supersede"]), "reject", len(D["reject"]))
print("problems", len(problems))
for x in problems:
    print(" ", x)
