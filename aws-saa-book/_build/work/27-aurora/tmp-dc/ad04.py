import json
D = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/27-aurora/tmp-dc/"
def fact(id, svc, claim, q, vals, scope, cond, bullets, note, ci, dm="", rel="core"):
    return {"id": id, "service": svc, "home_chapter": "27", "kind": "change", "claim": claim, "question": q,
            "values": [{"key": k, "display": d} for (k, d) in vals],
            "qualifiers": {"scope": scope, "default_or_max": dm, "adjustable": False, "condition": cond},
            "source_tier": 1, "hard": True, "tier0": False, "volatility": "frequently-changing", "changed": None,
            "exam_relevance": rel, "bullets": bullets, "change_items": ci, "note": note}
out = {
 "adopt-h-256acu.json": fact("aurora-serverless-change-max-256-acus", "aurora-serverless",
   "On October 3, 2024 Aurora serverless DB clusters could be created with a maximum capacity of 256 Aurora capacity units (ACUs).",
   "What maximum capacity can an Aurora serverless DB cluster have after October 2024?",
   [("max", "maximum capacity of 256 Aurora capacity units (ACUs)")],
   "per Aurora serverless DB instance (capacity range)", "needs a supported engine version; the guide's capacity table lists 0.5-128 ACUs for older engine versions", ["4.3.S3"],
   "d27-077. Older exam material says 128 ACUs as the maximum. The October 2024 What's New post is blocked by robots.txt, so the old value comes only from the capacity table (0.5-128 for Aurora MySQL 3.02.0 and higher, Aurora PostgreSQL 13.6 and higher and similar).",
   ["docs/AmazonRDS/latest/AuroraUserGuide/WhatsNew#47", "whats-new-v2#p146749259"], dm="max"),
 "adopt-h-pi-eol.json": fact("aurora-change-performance-insights-end-of-life", "aurora",
   "AWS announced that the Performance Insights console experience, flexible retention periods and their associated pricing end on November 30, 2025, and recommends upgrading DB clusters to Database Insights before that date.",
   "What replaces the Performance Insights console experience for Aurora monitoring?",
   [("eol", "end-of-life date for Performance Insights: November 30, 2025")],
   "Performance Insights for Aurora DB clusters", "", ["3.3.S2"],
   "Monitoring answers: CloudWatch Database Insights is the replacement named by the row. Announced May 30, 2025.",
   ["docs/AmazonRDS/latest/AuroraUserGuide/WhatsNew#27"], rel="extended"),
}
rows = {"adopt-h-256acu.json": 30, "adopt-h-pi-eol.json": 10}
for fn, f in out.items():
    json.dump(f, open(D + fn, "w"), indent=1); print(fn, rows[fn])
