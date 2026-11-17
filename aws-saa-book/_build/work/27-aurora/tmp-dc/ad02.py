import json
D = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/27-aurora/tmp-dc/"


def fact(id, kind, claim, q, vals, scope, cond, bullets, note, ci, hard=True, rel="core", vol="frequently-changing", cond_dm=""):
    return {"id": id, "service": "aurora", "home_chapter": "27", "kind": kind, "claim": claim, "question": q,
            "values": [{"key": k, "display": d, "spoken": s} if s else {"key": k, "display": d} for (k, d, s) in vals],
            "qualifiers": {"scope": scope, "default_or_max": cond_dm, "adjustable": False, "condition": cond},
            "source_tier": 1, "hard": hard, "tier0": False, "volatility": vol, "changed": None,
            "exam_relevance": rel, "bullets": bullets, "change_items": ci, "note": note}


H = "docs/AmazonRDS/latest/AuroraUserGuide/WhatsNew#"
out = {
 "adopt-h-mysql-v2-eos.json": (25, fact("aurora-change-mysql-v2-end-of-standard-support", "change",
    "Aurora MySQL version 2 reached the end of standard support on October 31, 2024.",
    "When did Aurora MySQL version 2 reach the end of standard support?",
    [("eos", "reached the end of standard support on October 31, 2024", "reached the end of standard support on October 31, 2024")],
    "Aurora MySQL version 2", "after this date RDS Extended Support applies to enrolled clusters", ["4.3.S3"],
    "d27-098. Pair with the Extended Support facts.", [H + "42"], rel="extended")),
 "adopt-h-pitr-awsbackup.json": (67, fact("aurora-change-pitr-with-aws-backup", "change",
    "You can manage Aurora automated (continuous) backups in AWS Backup and restore to specified times from them; the document history lists this on September 7, 2023.",
    "What did the September 2023 change let you do with Aurora continuous backups and AWS Backup?",
    [("pitr", "restore to specified times from them", "restore to specified times from them")],
    "Aurora automated (continuous) backups managed in AWS Backup", "", ["2.2.K6", "4.3.S3"],
    "d27-073. Chapter 24 owns AWS Backup. The Aurora PITR page confirms: if the cluster has an AWS Backup plan, that plan is used for point-in-time recovery.", [H + "84"])),
 "adopt-h-io-optimized.json": (81, fact("aurora-change-io-optimized-introduced", "change",
    "Aurora added a second DB cluster storage configuration, Aurora I/O-Optimized, on May 11, 2023: you pay only for the usage and storage of your DB clusters, with no additional charges for read and write I/O operations.",
    "What did Aurora add in May 2023 and how are I/O operations charged with it?",
    [("io-opt", "no additional charges for read and write I/O operations", "no additional charges for read and write I/O operations")],
    "Aurora DB cluster storage configuration", "the other configuration is Aurora Standard", ["4.3.S3"],
    "d27-092. Older exam material knows only the pay-per-I/O model, now called Aurora Standard.", [H + "98", "whats-new-v2#about-aws-whats-new-2023-05-amazon-aurora-i-o-optimized"])),
 "adopt-h-retain-backups.json": (74, fact("aurora-change-retain-automated-backups-deleted-cluster", "change",
    "You can retain automated backups for deleted Aurora clusters and restore them to a specified point in time; the document history lists this on August 4, 2023.",
    "Can you keep Aurora automated backups after you delete a cluster?",
    [("retain", "retain automated backups for deleted Aurora clusters", "retain automated backups for deleted clusters")],
    "Aurora DB clusters", "you choose to retain the backups when you delete the cluster", ["2.2.K6", "4.3.S3"],
    "Changed recently. Older sources, including the Aurora FAQ, still say automated backups are not kept after an instance is deleted.", [H + "91", "whats-new-v2#about-aws-whats-new-2023-08-amazon-aurora-automatic-backup-deleted-clusters"], rel="extended")),
 "adopt-h-backtrack-v3.json": (102, fact("aurora-change-backtrack-aurora-mysql-3", "change",
    "Aurora MySQL 3 versions gained Backtrack on January 4, 2023: you move your database to a prior point in time without restoring from a backup, and it completes within seconds, even for large databases.",
    "Which Aurora MySQL versions gained Backtrack in January 2023, and how long does a backtrack take?",
    [("backtrack", "it completes within seconds, even for large databases", "it completes within seconds")],
    "Aurora MySQL 3.* DB clusters", "Backtrack is an Aurora MySQL feature", ["2.2.K6"],
    "Older sources say Backtrack works only on Aurora MySQL 2. Backtrack is not available for Aurora PostgreSQL.", [H + "119", "whats-new-v2#about-aws-whats-new-2023-01-backtrack-support-aurora-mysql-3-0-compatible-mysql-8-0-available"], rel="extended")),
 "adopt-h-extsupport-feb24.json": (49, fact("aurora-change-extended-support-auto-enable", "change",
    "Amazon RDS automatically enables Amazon RDS Extended Support when Aurora MySQL and Aurora PostgreSQL major engine versions in your DB clusters and global clusters reach the Aurora end of standard support date; the document history lists this on February 15, 2024.",
    "What happens to an Aurora major engine version when it reaches the end of standard support?",
    [("auto", "automatically enables Amazon RDS Extended Support", "RDS automatically enables Extended Support")],
    "Aurora MySQL and Aurora PostgreSQL major engine versions", "you can opt out to avoid charges", ["4.3.S3"],
    "d27-098. Cost trap: this enrollment is billed.", [H + "66", "whats-new-v2#about-aws-whats-new-2023-09-amazon-aurora-rds-extended-support-mysql-postgresql-databases"])),
 "adopt-h-extsupport-mar24.json": (44, fact("aurora-change-extended-support-auto-enroll-on-create", "change",
    "Creating or restoring an Aurora MySQL version 2 or 3, or Aurora PostgreSQL version 11 database automatically enrolls that database in Amazon RDS Extended Support, and you can opt out to avoid charges; the document history lists this on March 21, 2024.",
    "What happens when you create or restore an Aurora MySQL version 2 database after its end of standard support?",
    [("enroll", "automatically enrolls that database into Amazon RDS Extended Support", "automatically enrolls the database in Extended Support")],
    "Aurora MySQL version 2 or 3 and Aurora PostgreSQL version 11 databases", "you can opt out", ["4.3.S3"],
    "d27-098.", [H + "61"], rel="extended")),
}
for fn, (row, f) in out.items():
    json.dump(f, open(D + fn, "w"), indent=1)
    print(fn, row)
