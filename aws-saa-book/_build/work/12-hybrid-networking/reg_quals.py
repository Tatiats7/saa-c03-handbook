"""register-12: read-only check of qualifier consistency for limit, quota and default facts.

Flags: claim says the value cannot be increased but default_or_max is not max/fixed or adjustable is true;
claim says you can request an increase but adjustable is false or default_or_max is not default.
"""
import json, re
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
SVCS = ["site-to-site-vpn", "direct-connect", "client-vpn"]
for s in SVCS:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        if not line.strip():
            continue
        f = json.loads(line)
        if f["status"] in ("rejected", "superseded") or f["kind"] not in ("limit", "quota", "default"):
            continue
        q = f.get("qualifiers") or {}
        c = f["claim"].lower()
        ev = " ".join(e["quote"].lower() + " " + (e.get("table_header") or "").lower() for e in f["evidence"])
        no_inc = "cannot be increased" in c or "can't be increased" in c or "not adjustable" in c
        can_inc = "request an increase" in c or "contact your solutions architect" in c
        flag = []
        if no_inc and (q.get("adjustable") or q.get("default_or_max") not in ("max", "fixed", "min")):
            flag.append("no-increase but dom=%s adj=%s" % (q.get("default_or_max"), q.get("adjustable")))
        if can_inc and (not q.get("adjustable") or q.get("default_or_max") != "default"):
            flag.append("increase but dom=%s adj=%s" % (q.get("default_or_max"), q.get("adjustable")))
        if not no_inc and not can_inc and f["kind"] == "quota":
            flag.append("quota without adjustability words; dom=%s adj=%s" % (q.get("default_or_max"), q.get("adjustable")))
        if flag:
            print(f["id"], "|", "; ".join(flag))
            print("    C:", f["claim"][:220])
