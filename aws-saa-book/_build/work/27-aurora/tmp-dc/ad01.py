import json
D = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/27-aurora/tmp-dc/"


def fact(id, kind, claim, q, vals, scope, cond, bullets, note, hard=False, rel="core"):
    return {"id": id, "service": "aurora", "home_chapter": "27", "kind": kind, "claim": claim, "question": q,
            "values": [{"key": k, "display": d, "spoken": s} if s else {"key": k, "display": d} for (k, d, s) in vals],
            "qualifiers": {"scope": scope, "default_or_max": "", "adjustable": False, "condition": cond},
            "source_tier": 1, "hard": hard, "tier0": False, "volatility": "stable", "changed": None,
            "exam_relevance": rel, "bullets": bullets, "note": note}


out = {
 "adopt-dg-dynamodb.json": fact("aurora-dg-dynamodb-key-value-single-digit-ms", "capability",
    "The AWS database decision guide describes DynamoDB as a key-value database optimized to provide a serverless, NoSQL, fully managed database with single-digit millisecond performance at any scale.",
    "How does the AWS database decision guide describe what DynamoDB is optimized for?",
    [("perf", "single-digit millisecond performance at any scale", "single-digit millisecond performance at any scale")],
    "DynamoDB in the AWS database decision guide", "neighbour service; chapter 28 owns DynamoDB", ["4.3.K9", "3.3.K8"],
    "d27-112, d27-113. Table row: Data model Key-value.", hard=True),
 "adopt-dg-rds.json": fact("aurora-dg-rds-six-engines-fully-managed", "capability",
    "The AWS database decision guide says to use Amazon RDS when you need a fully managed relational database with your choice of six popular engines: PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, and Db2.",
    "How many engines does the AWS database decision guide list for Amazon RDS, and which are they?",
    [("engines", "your choice of six popular engines", "a choice of six popular engines")],
    "RDS in the AWS database decision guide", "neighbour service; chapter 26 owns RDS", ["3.3.S4", "3.3.K8"],
    "d27-042, d27-113. RDS keeps the Oracle, SQL Server, MariaDB and Db2 engines that Aurora does not offer.", hard=True),
 "adopt-dg-dsql.json": fact("aurora-dg-dsql-active-active-multi-region", "capability",
    "The AWS database decision guide says to use Amazon Aurora DSQL when the application needs distributed SQL with active-active multi-Region replication, strong consistency, and no servers to manage.",
    "When does the AWS database decision guide point to Aurora DSQL instead of an Aurora cluster?",
    [("dsql", "distributed SQL with active-active multi-Region replication", "distributed SQL with active-active multi-Region replication")],
    "Aurora DSQL in the AWS database decision guide", "out of scope for the exam; mention only to rule it out", ["3.3.K8"],
    "d27-121, d27-113. DSQL is a separate service, not an Aurora cluster feature; it is not in the in-scope service list of the exam guide.", rel="reference"),
 "adopt-dg-limitless.json": fact("aurora-dg-limitless-beyond-single-instance", "capability",
    "The AWS database decision guide says to use Aurora PostgreSQL Limitless Database when the relational workload needs write throughput or storage beyond the limits of a single Aurora instance, while keeping a single-database experience.",
    "When does the AWS database decision guide point to Aurora PostgreSQL Limitless Database?",
    [("limitless", "beyond the limits of a single Aurora instance", "beyond the limits of a single Aurora instance")],
    "Aurora PostgreSQL Limitless Database in the AWS database decision guide", "Aurora PostgreSQL only", ["3.3.K8", "3.3.S4"],
    "d27-113.", rel="extended"),
}
rows = {"adopt-dg-dynamodb.json": 6, "adopt-dg-rds.json": 4, "adopt-dg-dsql.json": 1, "adopt-dg-limitless.json": 3}
for fn, f in out.items():
    json.dump(f, open(D + fn, "w"), indent=1)
    print(fn, rows[fn])
