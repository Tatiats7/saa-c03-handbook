import json
D = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/27-aurora/tmp-dc/"
def fact(id, claim, q, vals, scope, cond, ci):
    return {"id": id, "service": "aurora", "home_chapter": "27", "kind": "change", "claim": claim, "question": q,
            "values": [{"key": k, "display": d} for (k, d) in vals],
            "qualifiers": {"scope": scope, "default_or_max": "", "adjustable": False, "condition": cond},
            "source_tier": 1, "hard": True, "tier0": False, "volatility": "frequently-changing", "changed": None,
            "exam_relevance": "extended", "bullets": ["3.3.K8"], "change_items": ci,
            "note": "Changed recently: older sources say the Data API works only with Aurora Serverless v1, which is retired."}
out = {
 "adopt-h-dataapi-pg.json": fact("aurora-change-data-api-postgresql-serverless-provisioned",
   "RDS Data API became available for Aurora PostgreSQL serverless and provisioned DB clusters on December 21, 2023; it gives access to Aurora clusters through a secure HTTP endpoint, so SQL statements run without database drivers or managed connections.",
   "Which Aurora PostgreSQL clusters can use the RDS Data API since December 2023?",
   [("dataapi", "access your Aurora clusters through a secure HTTP endpoint")],
   "RDS Data API with Aurora PostgreSQL", "", ["docs/AmazonRDS/latest/AuroraUserGuide/WhatsNew#70"]),
 "adopt-h-dataapi-mysql.json": fact("aurora-change-data-api-mysql-serverless-provisioned",
   "RDS Data API became available for Aurora MySQL clusters that use Aurora serverless or provisioned instances; the document history lists this on September 26, 2024.",
   "Which Aurora MySQL clusters can use the RDS Data API since September 2024?",
   [("dataapi", "Aurora MySQL clusters that use Aurora serverless or provisioned instances")],
   "RDS Data API with Aurora MySQL", "", ["docs/AmazonRDS/latest/AuroraUserGuide/WhatsNew#50"]),
}
rows = {"adopt-h-dataapi-pg.json": 53, "adopt-h-dataapi-mysql.json": 33}
for fn, f in out.items():
    json.dump(f, open(D + fn, "w"), indent=1); print(fn, rows[fn])
