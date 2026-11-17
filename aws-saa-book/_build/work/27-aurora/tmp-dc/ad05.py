import json
D = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/27-aurora/tmp-dc/"
def fact(id, claim, q, vals, scope, cond, note, ci):
    return {"id": id, "service": "aurora", "home_chapter": "27", "kind": "change", "claim": claim, "question": q,
            "values": [{"key": k, "display": d} for (k, d) in vals],
            "qualifiers": {"scope": scope, "default_or_max": "", "adjustable": False, "condition": cond},
            "source_tier": 1, "hard": True, "tier0": False, "volatility": "frequently-changing", "changed": None,
            "exam_relevance": "extended", "bullets": ["3.3.S2"], "change_items": ci, "note": note}
out = {
 "adopt-h-bg-intro.json": fact("aurora-change-blue-green-deployments-introduced",
   "RDS Blue/Green Deployments let you make changes to an Aurora DB cluster in a staging environment, test them without affecting the production DB cluster, and promote the staging environment to production with minimal downtime; the document history lists this on November 27, 2022.",
   "What do RDS Blue/Green Deployments let you do for an Aurora DB cluster?",
   [("bg", "promote the staging environment to be the new production environment, with minimal downtime")],
   "Aurora DB clusters, Blue/Green Deployments", "Aurora PostgreSQL support was added on October 26, 2023", "Chapter 26 owns RDS blue/green basics; this is the Aurora history entry.",
   ["docs/AmazonRDS/latest/AuroraUserGuide/WhatsNew#129", "whats-new-v2#about-aws-whats-new-2023-10-amazon-rds-blue-green-deployments-aurora-rds-postgresql"]),
}
rows = {"adopt-h-bg-intro.json": 112}
for fn, f in out.items():
    json.dump(f, open(D + fn, "w"), indent=1); print(fn, rows[fn])
