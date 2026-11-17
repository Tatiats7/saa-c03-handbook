"""Helper for the mine-23-behavior lens: builds a facts-add input file and pre-checks quotes and displays."""
import json, re, sys, os

ROOT = "aws-saa-book/_build/corpus/snap/"
WORK = "aws-saa-book/_build/work/23-efs-fsx/"
HARD_KINDS = {"limit", "quota", "default", "restriction", "price", "sla", "change", "exam-policy"}
ABS = ["only", "always", "never", "cannot", "must", "by default", "up to", "at most", "not supported"]
PFX = {
    "efs": ("docs/efs/latest/ug/", "https://docs.aws.amazon.com/efs/latest/ug/"),
    "win": ("docs/fsx/latest/WindowsGuide/", "https://docs.aws.amazon.com/fsx/latest/WindowsGuide/"),
    "lus": ("docs/fsx/latest/LustreGuide/", "https://docs.aws.amazon.com/fsx/latest/LustreGuide/"),
    "ont": ("docs/fsx/latest/ONTAPGuide/", "https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/"),
    "zfs": ("docs/fsx/latest/OpenZFSGuide/", "https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/"),
}


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


_cache = {}


def snap(sid):
    if sid not in _cache:
        p = ROOT + sid + ".txt"
        _cache[sid] = norm(open(p, encoding="utf-8").read()) if os.path.exists(p) else None
    return _cache[sid]


def src(short):
    if short.startswith("www/"):
        return short, "https://aws.amazon.com/" + short[4:] + "/"
    k, name = short.split("/", 1)
    sid_p, url_p = PFX[k]
    return sid_p + name, url_p + name + ".html"


def f(id, kind, claim, question, ev, displays, scope, bul, rel="core", dm="", cond="", adj=False,
      vol="stable", tier0=False, hard=None, spoken=None):
    evid = []
    for e in ev:
        short, quote = e[0], e[1]
        th = e[2] if len(e) > 2 else None
        sid, url = src(short)
        evid.append({"source_id": sid, "url": url, "quote": quote, "table_header": th})
    vals = []
    for i, d in enumerate(displays):
        vals.append({"key": "v%d" % (i + 1), "display": d})
    if hard is None:
        hard = kind in HARD_KINDS or any(re.search(r"\b" + re.escape(a) + r"\b", claim.lower()) for a in ABS) \
            or bool(re.search(r"\d", claim))
    return {
        "id": id, "service": id.split("-")[0], "home_chapter": "23", "kind": kind, "claim": claim,
        "question": question, "values": vals,
        "qualifiers": {"scope": scope, "default_or_max": dm, "adjustable": adj, "condition": cond},
        "evidence": evid, "source_tier": 1, "hard": hard, "tier0": tier0, "volatility": vol,
        "changed": None, "exam_relevance": rel, "bullets": bul if isinstance(bul, list) else [bul],
    }


def emit(name, facts):
    bad = 0
    ids = set()
    for x in facts:
        if x["id"] in ids:
            print("DUP id", x["id"]); bad += 1
        ids.add(x["id"])
        allq = []
        for e in x["evidence"]:
            t = snap(e["source_id"])
            if t is None:
                print("NO SNAP", x["id"], e["source_id"]); bad += 1; continue
            q = norm(e["quote"])
            allq.append(q)
            if q not in t:
                print("QUOTE NOT FOUND", x["id"], "|", e["quote"][:90]); bad += 1
            if len(e["quote"].split()) > 80:
                print("QUOTE >80 words", x["id"]); bad += 1
        c = norm(x["claim"])
        for v in x["values"]:
            d = norm(v["display"])
            if d not in c and not any(d in q for q in allq):
                print("DISPLAY NOT HELD", x["id"], "|", v["display"]); bad += 1
            if not re.search(r"\d", d) and len(d.split()) > 8:
                print("DISPLAY >8 words", x["id"], "|", v["display"]); bad += 1
        if len(x["values"]) < 2:
            print("one display", x["id"])
    n = len(facts)
    k = 1 if n <= 25 else -(-n // 20)
    size = -(-n // k)
    for i in range(k):
        nm = name if k == 1 else name.replace(".json", "-%s.json" % "abcdef"[i])
        json.dump(facts[i * size:(i + 1) * size], open(WORK + nm, "w"), indent=1, ensure_ascii=False)
        print("wrote", nm, len(facts[i * size:(i + 1) * size]))
    print(name, n, "facts;", bad, "problems")
