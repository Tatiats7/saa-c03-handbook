"""register-11: merge the miners' demand notes (read-only); writes reg-demand.txt.

For each demand item of brief.v0.json: the status and facts each miner reported, the fact ids
that do not exist or are not live, and a proposed status.
"""
import json
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/11-vpc-connectivity/"
facts = {}
for s in ["vpc-peering", "transit-gateway", "vpc-endpoints", "privatelink", "vpc", "s3", "dynamodb", "elb", "direct-connect", "site-to-site-vpn", "client-vpn", "well-architected", "route53", "network-firewall", "ram"]:
    try:
        for line in open(ROOT + "/data/facts/%s.jsonl" % s):
            line = line.strip()
            if line:
                f = json.loads(line)
                facts[f["id"]] = f
    except IOError:
        pass
brief = json.load(open(W + "brief.v0.json"))
notes = {}
for n in ["mine-faq.json", "mine-numbers+changes.json", "mine-behavior+decisions.json"]:
    d = json.load(open(W + n))
    for k, v in (d.get("demand") or {}).items():
        notes.setdefault(k, []).append((n.split(".")[0][5:], v))
out = open(W + "reg-demand.txt", "w")
summary = {}
for item in brief["demand"]:
    did = item["id"]
    ids = []
    sts = []
    out.write("== %s [%s] %s\n" % (did, item["bullet"], item["question"][:300]))
    for lens, v in notes.get(did, []):
        if isinstance(v, dict):
            st = v.get("status")
            fl = list(v.get("facts") or []) + list(v.get("reused") or [])
            note = v.get("note") or ""
        elif isinstance(v, list):
            st = "found" if v else "not found"
            fl = v
            note = ""
        else:
            st = str(v)
            fl = []
            note = ""
        sts.append(st)
        ids += [x for x in fl if x not in ids]
        out.write("  %s: %s %s %s\n" % (lens, st, ",".join(fl), ("NOTE: " + note[:300]) if note else ""))
    bad = [x for x in ids if x not in facts or facts[x]["status"] in ("rejected", "superseded")]
    if bad:
        out.write("  MISSING/DEAD: %s\n" % ",".join("%s(%s)" % (x, facts[x]["status"] if x in facts else "absent") for x in bad))
    live = [x for x in ids if x not in bad]
    prop = "found" if live else "not-found"
    if any(s and "partial" in s for s in sts):
        prop = "partial"
    if not notes.get(did):
        prop = "NO NOTE"
    summary[prop] = summary.get(prop, 0) + 1
    out.write("  => %s (%d live facts)\n" % (prop, len(live)))
out.close()
print(summary)
