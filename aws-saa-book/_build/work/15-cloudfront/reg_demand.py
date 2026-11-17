"""register-15: write demand statuses and fact ids from the miners' notes into brief.v0.json."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
W = ROOT / "aws-saa-book/_build/work/15-cloudfront"
rows = {}
for f in ["cloudfront", "global-accelerator"]:
    for l in open(ROOT / f"aws-saa-book/data/facts/{f}.jsonl"):
        r = json.loads(l); rows[r["id"]] = r

def live(fid, seen=()):
    r = rows.get(fid)
    if r is None or fid in seen:
        return None
    if r["status"] == "superseded":
        return live(r.get("superseded_by"), seen + (fid,))
    if r["status"] == "rejected":
        return None
    return fid

notes = {}
for n in ["mine-behavior", "mine-faq", "mine-numbers", "mine-decisions+changes"]:
    for it in json.loads((W / f"{n}.json").read_text())["items"]:
        notes[it["id"]] = it
over = {
    "d120": {"status": "partial", "add": ["global-accelerator-dec-guide-edge-category-route53-elb"],
             "note": "register-15: the guide separates the services by category and purpose (new fact global-accelerator-dec-guide-edge-category-route53-elb); no sentence compares Route 53 or ELB with CloudFront head to head"},
    "d133": {"status": "partial", "add": ["cloudfront-change-waf-blocked-requests-free-2024-10"],
             "note": "register-15: WAF-blocked requests free since 2024-10-25 added from the What's New feed snapshot (cloudfront-change-waf-blocked-requests-free-2024-10); the 2024-07 'managed cache policies for web applications' post is not fetchable (robots.txt), only the 2024-05-24 history row is quoted"},
    "d173": {"status": "filled", "add": ["global-accelerator-change-dual-stack-2022-07", "global-accelerator-change-ipv6-ec2-endpoints-2023-08",
                                          "global-accelerator-change-dual-stack-nlb-2023-11", "global-accelerator-dual-stack-ipv6-support"],
             "note": "register-15: the FAQ IPv6 sentence (ALB only) was rejected as out of date; current IP versions come from the dual-stack facts and the document history"},
    "d063": {"note": "register-15: OAC lists opt-in Regions launched after December 2022; OAI lacks them. Both kept with their own scope (cloudfront-oac-supports-all-regions-dynamic-requests, cloudfront-oai-legacy-not-for-all-scenarios)"},
    "d003": {"note": "register-15: teach 50 GB cacheable per GET response (cloudfront-quota-max-cacheable-file-size); the FAQ 30 GB fact is reference only"},
    "d008": {"note": "register-15: teach the quotas-page rates; the FAQ in-progress figures (3,000 objects, 15 wildcard paths) are reference only"},
}
brief = json.loads((W / "brief.v0.json").read_text())
counts, missing = {}, []
for d in brief["demand"]:
    n = notes.get(d["id"])
    if n is None:
        missing.append(d["id"]); continue
    o = over.get(d["id"], {})
    ids = []
    for fid in list(n.get("facts", [])) + o.get("add", []):
        x = live(fid)
        if x and x not in ids:
            ids.append(x)
    status = o.get("status", n["status"])
    if status in ("filled", "contradicted", "partial") and not ids:
        status = "not-found"
    d["status"] = status
    d["facts"] = ids
    d["registered_by"] = "register-15"
    note = " ".join(x for x in [n.get("note", ""), o.get("note", "")] if x).strip()
    if note:
        d["note"] = note
    counts[status] = counts.get(status, 0) + 1
(W / "brief.v0.json").write_text(json.dumps(brief, indent=1, ensure_ascii=False) + "\n")
print(counts, "missing notes:", missing)
