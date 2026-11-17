"""register-27: build amend patch files from reg-decisions.json, reg-displays.json and reg-scopes.json.
Writes only under _build/work/27-aurora/ (reg-patches/, reg-build-report.json, reg-proposals.txt).
Usage: python3 -I reg_build.py [--write]"""
import json, re, sys, copy, os

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
sys.path.insert(0, ROOT + "/tools")
from saalib.common import normalize_text  # noqa: E402

W = ROOT + "/_build/work/27-aurora/"
OUT = W + "reg-patches/"
WRITE = "--write" in sys.argv
SVCS = ("aurora", "aurora-serverless")

allf = {}
for fn in os.listdir(ROOT + "/data/facts"):
    if fn.endswith(".jsonl"):
        for line in open(ROOT + "/data/facts/" + fn):
            if line.strip():
                f = json.loads(line)
                allf[f["id"]] = f
facts = {k: v for k, v in allf.items() if v["service"] in SVCS}

D = json.load(open(W + "reg-decisions.json"))
DISP = json.load(open(W + "reg-displays.json")) if os.path.exists(W + "reg-displays.json") else {}
SC = json.load(open(W + "reg-scopes.json")) if os.path.exists(W + "reg-scopes.json") else {"rules": [], "override": {}}

problems = []
gone = {o for o, n, _ in D["supersede"]} | {r[0] for r in D["reject"]}
for o, n, _ in D["supersede"]:
    if o not in facts:
        problems.append("supersede: unknown old " + o)
    elif facts[o]["status"] in ("rejected", "superseded"):
        problems.append("supersede: already retired " + o)
    if n not in allf:
        problems.append("supersede: unknown target " + n)
    elif allf[n]["status"] in ("rejected", "superseded") or n in gone:
        problems.append("supersede: target retired " + n)
for r, _ in D["reject"]:
    if r not in facts:
        problems.append("reject: unknown " + r)

live = {k: v for k, v in facts.items() if v["status"] not in ("rejected", "superseded") and k not in gone}
patch = {}


def P(i):
    if i not in live:
        problems.append("edit on retired or foreign fact " + i)
        return {}
    return patch.setdefault(i, {})


def cur(i, k):
    return copy.deepcopy(patch.get(i, {}).get(k, facts[i].get(k)))


def norm(s):
    return normalize_text(s or "").lower()


RANK = {"core": 3, "extended": 2, "reference": 1}

# 1. merge bullets and relevance of superseded facts into kept facts of this chapter
for o, n, _ in D["supersede"]:
    if n not in live:
        continue
    b = cur(n, "bullets") or []
    nb = list(b)
    for x in facts[o].get("bullets") or []:
        if x not in nb:
            nb.append(x)
    if nb != b:
        P(n)["bullets"] = nb
    ro, rn = facts[o].get("exam_relevance"), cur(n, "exam_relevance")
    if RANK.get(ro, 0) > RANK.get(rn, 0):
        P(n)["exam_relevance"] = ro

# 2. relevance overrides
for i, r in D.get("relevance", {}).items():
    if cur(i, "exam_relevance") != r:
        P(i)["exam_relevance"] = r

# 2b. extra displays
for i, lst in D.get("add_values", {}).items():
    vals = cur(i, "values")
    for k, d in lst:
        if any(v["key"] == k for v in vals):
            problems.append(f"{i}: key exists {k}")
            continue
        vals.append({"key": k, "display": d})
    P(i)["values"] = vals

# 3. displays
STOP = set("the a an of to in for and or with that by as on at from is are be your its their this these those it".split())
KEEP = re.compile(r"\b(can't|cannot|don't|doesn't|isn't|aren't|won't|not|no|only|must|always|never|without|any|all)\b", re.I)


def windows(words, quotes):
    out = []
    n = len(words)
    for L in range(min(8, n), 1, -1):
        for s in range(0, n - L + 1):
            w = words[s:s + L]
            if w[0].lower() in STOP or w[-1].lower().strip(",.") in STOP:
                continue
            ph = " ".join(w).strip(",")
            if any(norm(ph) in q for q in quotes):
                out.append(ph)
        if out:
            break
    return out


proposals = []
for i, f in sorted(live.items()):
    quotes = [norm(e.get("quote")) for e in f["evidence"]]
    vals = cur(i, "values")
    changed = False
    newvals = []
    for v in vals:
        d = v["display"]
        key = f"{i}#{v['key']}"
        if key in DISP:
            nd = DISP[key]
            if nd is None:
                changed = True
                continue
            if nd != d:
                v = dict(v, display=nd)
                changed = True
        elif not re.search(r"\d", d) and (len(d.split()) > 8 or not any(norm(d) in q for q in quotes)):
            cands = windows(d.split(), quotes)
            keepc = [c for c in cands if KEEP.search(c)] if KEEP.search(d) else cands
            pick = (keepc or cands or [None])[0]
            proposals.append((key, d, pick, cands[:4]))
            if pick:
                v = dict(v, display=pick)
                changed = True
            else:
                problems.append(f"{key}: no verbatim window for display {d!r}")
        newvals.append(v)
    # unique displays
    seen, uniq = set(), []
    for v in newvals:
        if norm(v["display"]) in seen:
            changed = True
            continue
        seen.add(norm(v["display"]))
        uniq.append(v)
    if changed:
        P(i)["values"] = uniq
    for v in uniq:
        d = v["display"]
        if not re.search(r"\d", d):
            if len(d.split()) > 8:
                problems.append(f"{i}: display over 8 words: {d}")
            if not any(norm(d) in q for q in quotes):
                problems.append(f"{i}: display not verbatim in a quote: {d}")
    if not uniq:
        problems.append(f"{i}: no display left")

# 4. scopes
scopes, noscope = {}, []
for i, f in sorted(live.items()):
    q = cur(i, "qualifiers") or {}
    if (q.get("scope") or "").strip():
        continue
    s = SC["override"].get(i)
    if s is None:
        for rx, val in SC["rules"]:
            if re.search(rx, i):
                s = val
                break
    if s is None:
        noscope.append(i)
        continue
    q2 = dict(q)
    q2.setdefault("default_or_max", "")
    q2.setdefault("adjustable", False)
    q2.setdefault("condition", "")
    q2["scope"] = s
    P(i)["qualifiers"] = q2
    scopes[i] = s

# 5. hard: number, number word or restriction wording in the claim
HARDRX = re.compile(r"(?<![A-Za-z.])\d+(?![A-Za-z0-9])|\b(two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|sixteen|twenty)\b|"
                    r"\b(cannot|can't|must|only|always|never|by default|at most|up to|not supported|does not support|"
                    r"do not support|is not available|are not available|no additional|free|not charged)\b", re.I)
hard_set = []
for i, f in sorted(live.items()):
    if not cur(i, "hard") and HARDRX.search(f["claim"]):
        P(i)["hard"] = True
        hard_set.append(i)
        if not (f.get("question") or "").strip():
            problems.append(f"{i}: hard without question")

patch = {k: v for k, v in patch.items() if v}
with open(W + "reg-proposals.txt", "w") as fh:
    fh.write("# auto display proposals: key | old | picked | other candidates\n")
    for key, d, pick, c in proposals:
        fh.write(f"{key}\n   old: {d}\n   new: {pick}\n   alt: {c[1:]}\n")
    fh.write("\n# live facts without a scope rule\n")
    for i in noscope:
        fh.write(i + "\n")
    fh.write("\n# hard set true\n")
    for i in hard_set:
        fh.write(f"{i} :: {live[i]['claim']}\n")
if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for i, p in patch.items():
        json.dump(p, open(OUT + i + ".json", "w"), ensure_ascii=False, indent=1)
json.dump({"patches": sorted(patch), "scopes": scopes, "hard_set": hard_set, "noscope": noscope, "problems": problems},
          open(W + "reg-build-report.json", "w"), ensure_ascii=False, indent=1)
print("live", len(live), "patches", len(patch), "proposals", len(proposals), "scopes", len(scopes), "noscope", len(noscope),
      "hard_set", len(hard_set), "problems", len(problems))
for x in problems[:60]:
    print("PROBLEM", x)
