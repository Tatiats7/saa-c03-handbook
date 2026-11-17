"""register-17: build amend patches from reg-decisions.json (writes only under _build/work/17-auto-scaling/reg-patches).

Usage: python3 reg_build.py [--write]
Prints problems (displays that break the 8-word or verbatim rule, unknown ids) and the scope fills.
"""
import json, re, sys, copy, os
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
sys.path.insert(0, ROOT + "/tools")
from saalib.common import normalize_text  # noqa: E402
from saalib import lint  # noqa: E402

W = ROOT + "/_build/work/17-auto-scaling/"
OUT = W + "reg-patches/"
WRITE = "--write" in sys.argv

facts = {}
for s in ["ec2-auto-scaling", "aws-auto-scaling"]:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f
live = {i: f for i, f in facts.items() if f["status"] not in ("rejected", "superseded")}
D = json.load(open(W + "reg-decisions.json"))
problems = []
REL = {"core": 3, "extended": 2, "reference": 1}

sup = {o: n for o, n, _ in D["supersede"]}
rej = {i for i, _ in D["reject"]}
for cf in D.get("resolve", []):
    if not cf[2]:
        rej.add(cf[3])
gone = set(sup) | rej
for o, n in sup.items():
    if o not in live or n not in live:
        problems.append("supersede unknown: %s -> %s" % (o, n))
    if n in gone:
        problems.append("supersede target retired: %s -> %s" % (o, n))

patch = {}


def P(i):
    if i not in live:
        problems.append("unknown/retired fact " + i)
        return {}
    if i in gone:
        problems.append("edit on retired fact " + i)
    return patch.setdefault(i, {})


def cur(i, k):
    p = patch.get(i, {})
    return copy.deepcopy(p[k]) if k in p else copy.deepcopy(live[i].get(k))


# evidence drops (by source id or index)
for i, drops in D.get("drop_evidence", {}).items():
    ev = cur(i, "evidence")
    keep = []
    for n, e in enumerate(ev):
        if n in drops or e["source_id"] in drops:
            continue
        keep.append({k: e.get(k) for k in ("source_id", "url", "quote", "table_header", "heading") if k in e})
    if len(keep) == len(ev):
        problems.append("%s: drop_evidence removed nothing" % i)
    P(i)["evidence"] = keep

# displays
for i, m in D.get("display", {}).items():
    vals = cur(i, "values")
    keys = [v["key"] for v in vals]
    for k, d in m.items():
        if d is None:
            if k not in keys:
                problems.append("%s: no key %s to drop" % (i, k))
            vals = [v for v in vals if v["key"] != k]
        elif k in keys:
            for v in vals:
                if v["key"] == k:
                    v["display"] = d
                    if "spoken" in v and v["spoken"] and len(v["spoken"].split()) > 8:
                        v.pop("spoken")
        else:
            vals.append({"key": k, "display": d})
    P(i)["values"] = vals

for f in ("claim", "kind", "note"):
    for i, v in D.get(f, {}).items():
        P(i)[f] = v
for i, v in D.get("hard", {}).items():
    P(i)["hard"] = v
for i, v in D.get("rel", {}).items():
    P(i)["exam_relevance"] = v
for i, v in D.get("bullets_add", {}).items():
    b = cur(i, "bullets") or []
    P(i)["bullets"] = b + [x for x in v if x not in b]

# merge bullets and relevance from superseded facts into the kept fact
for o, n in sup.items():
    if o not in live or n not in live:
        continue
    b = cur(n, "bullets") or []
    add = [x for x in (live[o].get("bullets") or []) if x not in b]
    if add:
        P(n)["bullets"] = b + add
    r_old, r_new = live[o].get("exam_relevance"), cur(n, "exam_relevance")
    if REL.get(r_old, 0) > REL.get(r_new, 0):
        P(n)["exam_relevance"] = r_old
    if live[o].get("hard") and not cur(n, "hard"):
        P(n)["hard"] = True

# scope fills
RULES = [
    ("aws-auto-scaling-aas-", "per Application Auto Scaling scalable target"),
    ("aws-auto-scaling-wa-", "AWS Well-Architected guidance"),
    ("aws-auto-scaling-pricing", "per account"),
    ("aws-auto-scaling-change-scaling-plan", "AWS Auto Scaling scaling plans"),
    ("aws-auto-scaling-", "per AWS Auto Scaling scaling plan"),
    ("-case-", "customer case study"),
    ("-wa-", "AWS Well-Architected guidance"),
    ("whitepaper", "AWS web hosting whitepaper (historical reference)"),
    ("decision-guide", "AWS compute decision guide"),
    ("vertical", "per EC2 instance"),
    ("lifecycle-hook", "per lifecycle hook"),
    ("hook", "per lifecycle hook"),
    ("lifecycle-policy", "per Auto Scaling group with an instance lifecycle policy"),
    ("retained", "per Auto Scaling group with an instance lifecycle policy"),
    ("warm-pool", "per warm pool"),
    ("instance-refresh", "per instance refresh"),
    ("root-volume", "per instance refresh with the replace root volume strategy"),
    ("maintenance-policy", "per Auto Scaling group with an instance maintenance policy"),
    ("max-instance-lifetime", "per Auto Scaling group with a maximum instance lifetime"),
    ("predictive", "per predictive scaling policy"),
    ("target-tracking", "per target tracking scaling policy"),
    ("high-resolution", "per target tracking scaling policy"),
    ("metric-math", "per target tracking scaling policy"),
    ("step-", "per step scaling policy"),
    ("simple", "per simple scaling policy"),
    ("cooldown", "per Auto Scaling group (scaling cooldown)"),
    ("warmup", "per Auto Scaling group (instance warmup)"),
    ("scheduled", "per scheduled action"),
    ("sqs", "per Auto Scaling group that processes an Amazon SQS queue"),
    ("standby", "per instance in Standby"),
    ("scale-in-protection", "per instance with scale-in protection"),
    ("termination", "per Auto Scaling group during scale in"),
    ("terminat", "per Auto Scaling group during scale in"),
    ("grace-period", "per Auto Scaling group (health checks)"),
    ("health", "per Auto Scaling group (health checks)"),
    ("unhealthy", "per Auto Scaling group (health checks)"),
    ("launch-config", "per launch configuration"),
    ("launchinstances", "per LaunchInstances API call"),
    ("synchronous", "per LaunchInstances API call"),
    ("launch-template", "per launch template used by an Auto Scaling group"),
    ("ssm-parameter", "per launch template used by an Auto Scaling group"),
    ("imdsv2", "per launch template used by an Auto Scaling group"),
    ("capacity-reservation", "per Auto Scaling group that uses Capacity Reservations"),
    ("capacity-blocks", "per Auto Scaling group that uses Capacity Reservations"),
    ("odcr", "per Auto Scaling group that uses Capacity Reservations"),
    ("capacity-rebalancing", "per Auto Scaling group with Spot Instances"),
    ("spot", "per Auto Scaling group with Spot Instances"),
    ("weights", "per mixed instances group"),
    ("mixed", "per mixed instances group"),
    ("purchase", "per mixed instances group"),
    ("on-demand", "per mixed instances group"),
    ("zonal-shift", "per Auto Scaling group with zonal shift"),
    ("az-", "per Auto Scaling group across Availability Zones"),
    ("rebalanc", "per Auto Scaling group across Availability Zones"),
    ("launch-in-az", "per Auto Scaling group across Availability Zones"),
    ("launch-retries", "per Auto Scaling group across Availability Zones"),
    ("resilience", "per Auto Scaling group across Availability Zones"),
    ("alb-", "per Application Load Balancer"),
    ("lb-", "per Auto Scaling group with a load balancer"),
    ("elb", "per Auto Scaling group with a load balancer"),
    ("register", "per Auto Scaling group with a load balancer"),
    ("slr", "per account (service-linked role)"),
    ("key", "per account (KMS keys)"),
    ("instance-profile", "per launch template used by an Auto Scaling group"),
    ("secrets", "per launch template used by an Auto Scaling group"),
    ("interface-endpoint", "per VPC"),
    ("control-plane", "per Region"),
    ("process", "per Auto Scaling group (scaling processes)"),
    ("suspend", "per Auto Scaling group (scaling processes)"),
    ("attach", "per Auto Scaling group"),
    ("detach", "per Auto Scaling group"),
    ("faq-", "per Auto Scaling group"),
    ("", "per Auto Scaling group"),
]
scopes = {}
for i in sorted(live):
    if i in gone:
        continue
    q = cur(i, "qualifiers") or {}
    if q.get("scope"):
        continue
    sc = D.get("scope", {}).get(i)
    if sc is None:
        for key, val in RULES:
            if key in i:
                sc = val
                break
    q["scope"] = sc
    for k in ("default_or_max", "condition"):
        q.setdefault(k, "")
    q.setdefault("adjustable", False)
    P(i)["qualifiers"] = q
    scopes[i] = sc

# checks on every live, kept fact (after the patch)
NUM = re.compile(r"(?<![A-Za-z])\d")
for i in sorted(live):
    if i in gone:
        continue
    vals = cur(i, "values")
    ev = cur(i, "evidence")
    qs = [normalize_text(e.get("quote") or "") for e in ev]
    claim = normalize_text(cur(i, "claim"))
    seen = set()
    for v in vals:
        d = v["display"]
        nd = normalize_text(d)
        if d in seen:
            problems.append("%s: duplicate display %r" % (i, d))
        seen.add(d)
        if not NUM.search(d):
            if len(d.split()) > 8:
                problems.append("%s [%s]: LONG %d %r" % (i, v["key"], len(d.split()), d))
            if not any(lint.holds_display(q, nd) for q in qs):
                problems.append("%s [%s]: NOT IN QUOTE %r" % (i, v["key"], d))
        else:
            if not any(lint.holds_display(q, nd) for q in qs + [claim]):
                problems.append("%s [%s]: numeric display not held %r" % (i, v["key"], d))

print("problems:", len(problems))
for p in problems:
    print("  ", p)
print("patches:", len(patch), "scope fills:", len(scopes))
if "--scopes" in sys.argv:
    for i, s in scopes.items():
        print("  SCOPE %s => %s | %s" % (i, s, live[i]["claim"][:110]))
if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        os.remove(OUT + f)
    order = []
    for i, p in sorted(patch.items()):
        if not p or i in gone:
            continue
        json.dump(p, open(OUT + i + ".json", "w"), indent=1, ensure_ascii=False)
        order.append(i)
    json.dump({"amend": order, "supersede": D["supersede"], "reject": D["reject"], "resolve": D.get("resolve", [])},
              open(W + "reg-plan.json", "w"), indent=1)
    print("wrote", len(order), "patch files")
