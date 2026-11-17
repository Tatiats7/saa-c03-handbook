"""register-11: writes the demand statuses of brief.v0.json from the miners' notes and the registrar's work.

Statuses: filled, partial, not-found. Superseded fact ids are replaced by the fact that superseded them.
"""
import json
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/11-vpc-connectivity/"
facts = {}
import os
for fn in os.listdir(ROOT + "/data/facts"):
    if not fn.endswith(".jsonl"):
        continue
    for line in open(ROOT + "/data/facts/" + fn):
        line = line.strip()
        if line:
            f = json.loads(line)
            facts[f["id"]] = f

def live(i):
    seen = set()
    while i in facts and facts[i]["status"] == "superseded" and facts[i].get("superseded_by") and i not in seen:
        seen.add(i)
        i = facts[i]["superseded_by"]
    if i in facts and facts[i]["status"] not in ("rejected", "superseded"):
        return i
    return None

brief = json.load(open(W + "brief.v0.json"))
notes = {}
for n in ["mine-faq.json", "mine-numbers+changes.json", "mine-behavior+decisions.json"]:
    d = json.load(open(W + n))
    for k, v in (d.get("demand") or {}).items():
        notes.setdefault(k, []).append(v)

EXTRA = {
    "d11-015": (["vpc-peering-billing-usage-type-2025"], "register-11: the existing change fact carries the 'no changes to the pricing' sentence."),
    "d11-049": (["transit-gateway-faq-connect-sdwan", "transit-gateway-faq-connect-no-static-routes"], "register-11: FAQ facts named."),
    "d11-050": (["vpc-centralized-egress-reduces-natgw-cost", "vpc-centralized-egress-tgw-processing-tradeoff", "transit-gateway-wp-centralize-shared-services"], "register-11: chapter 10 facts reused."),
    "d11-057": (["vpc-gateway-endpoint-no-hourly-or-processing-charge", "vpc-endpoints-wp-gateway-endpoint-no-additional-charge"], "register-11: the chapter 10 fact quotes the gateway-endpoints sentence."),
    "d11-025": (["transit-gateway-route-evaluation-most-specific-first"], "register-11: added the longest-prefix rule as a heading-scoped list line (Route evaluation order)."),
    "d11-054": (["privatelink-interface-endpoint-sends-tcp-or-udp", "vpc-endpoints-faq-five-types"], "register-11: the interface type is covered by the concepts line fact; tunnel endpoints (2026-09-18) are not examinable yet and stay out."),
    "d11-018": (["vpc-peering-rejected-request-visibility", "vpc-peering-expired-request-visible-2-days", "vpc-peering-deleted-connection-visibility"], "register-11: the visibility windows exist as numbers-lens facts."),
}
PARTIAL_NOTE = {
    "d11-071": "register-11: one more search (corpus, 'available in all Availability Zones' and the PrivateLink guide's Availability Zone sentences) found no general statement for AWS-service interface endpoints; only service pages (for example Amazon Comprehend) say so. Teach the endpoint-service rule and the one-subnet-per-AZ rule.",
    "d11-091": "register-11: one more search ('transit VPC' in saved pages) found no current page that says Transit Gateway replaces a transit VPC; only the 2019 What's New feed text. Teach the transit VPC challenges as stated.",
}
FORCE_FILLED = {"d11-018", "d11-025", "d11-054"}

summary = {}
for item in brief["demand"]:
    did = item["id"]
    ids, sts, mnotes = [], [], []
    for v in notes.get(did, []):
        if isinstance(v, dict):
            sts.append(v.get("status") or "")
            for x in list(v.get("facts") or []) + list(v.get("reused") or []):
                if x not in ids:
                    ids.append(x)
            if v.get("note"):
                mnotes.append(v["note"])
        elif isinstance(v, list):
            ids += [x for x in v if x not in ids]
    extra_note = None
    if did in EXTRA:
        add, extra_note = EXTRA[did]
        ids += [x for x in add if x not in ids]
    out = []
    for x in ids:
        y = live(x)
        if y and y not in out:
            out.append(y)
    if not out:
        st = "not-found"
    elif did in FORCE_FILLED:
        st = "filled"
    elif any("partial" in s for s in sts) or did in PARTIAL_NOTE:
        st = "partial"
    else:
        st = "filled"
    item["status"] = st
    item["facts"] = out
    nl = list(mnotes)
    if extra_note:
        nl.append(extra_note)
    if did in PARTIAL_NOTE:
        nl.append(PARTIAL_NOTE[did])
    if nl:
        item["note"] = " | ".join(nl)
    summary[st] = summary.get(st, 0) + 1
brief["registered_by"] = "register-11"
brief["registered_at"] = "2026-10-14"
json.dump(brief, open(W + "brief.v0.json", "w"), indent=1, ensure_ascii=False)
print(summary)
