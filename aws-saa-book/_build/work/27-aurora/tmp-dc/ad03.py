import json
D = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/27-aurora/tmp-dc/"
def fact(id, claim, q, vals, scope, cond, note, ci):
    return {"id": id, "service": "aurora", "home_chapter": "27", "kind": "change", "claim": claim, "question": q,
            "values": [{"key": k, "display": d} for (k, d) in vals],
            "qualifiers": {"scope": scope, "default_or_max": "", "adjustable": False, "condition": cond},
            "source_tier": 1, "hard": True, "tier0": False, "volatility": "frequently-changing", "changed": None,
            "exam_relevance": "extended", "bullets": ["3.3.K8", "3.3.S2"], "change_items": ci, "note": note}
out = {
 "adopt-h-zeroetl-pg.json": fact("aurora-change-zero-etl-redshift-postgresql-ga",
   "Zero-ETL integrations with Amazon Redshift became generally available for an Aurora PostgreSQL source DB cluster on October 15, 2024; they make transactional data available in Amazon Redshift within seconds of it being written.",
   "When did Aurora PostgreSQL zero-ETL integration with Amazon Redshift become generally available?",
   [("seconds", "within seconds of it being written to an Aurora PostgreSQL source DB cluster")],
   "Aurora PostgreSQL zero-ETL integration with Amazon Redshift", "", "Replaces a self-built ETL pipeline for near real-time analytics.",
   ["docs/AmazonRDS/latest/AuroraUserGuide/WhatsNew#46", "whats-new-v2#launchmarketingintake-1045"]),
 "adopt-h-zeroetl-mysql.json": fact("aurora-change-zero-etl-redshift-mysql-ga",
   "Zero-ETL integrations with Amazon Redshift became generally available for Aurora MySQL on November 7, 2023.",
   "When did Aurora MySQL zero-ETL integration with Amazon Redshift become generally available?",
   [("ga", "now generally available for Aurora MySQL")],
   "Aurora MySQL zero-ETL integration with Amazon Redshift", "", "Aurora PostgreSQL followed in October 2024.",
   ["docs/AmazonRDS/latest/AuroraUserGuide/WhatsNew#78", "whats-new-v2#about-aws-whats-new-2023-11-aws-general-availability-amazon-aurora-mysql-zero-etl-integration-redshift"]),
}
rows = {"adopt-h-zeroetl-pg.json": 29, "adopt-h-zeroetl-mysql.json": 61}
for fn, f in out.items():
    json.dump(f, open(D + fn, "w"), indent=1); print(fn, rows[fn])
