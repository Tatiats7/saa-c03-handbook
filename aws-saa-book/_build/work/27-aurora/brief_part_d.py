# brief-27, part D: traps, compare tables, signals, words, numbers, changed recently, FAQ, story, decision record, real world, devices.

BRIEF["traps"] = [
    {"id": "aurora-trap-replicas-copy-data",
     "belief": "Each Aurora Replica keeps its own copy of the data, as an RDS read replica does, so every extra replica adds replication lag and storage cost.",
     "truth": "Aurora Replicas connect to the same cluster volume as the writer; replica lag is usually much less than 100 milliseconds, and you pay for one copy of the storage.",
     "facts": ["aurora-adding-replicas-read-same-volume-offload", "aurora-replica-lag-under-100-ms", "aurora-faq-pay-for-one-copy"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "aurora-trap-writes-through-reader-endpoint",
     "belief": "An application can send its writes to the reader endpoint, so that the Aurora Replicas share the write load too.",
     "truth": "The cluster endpoint is the only endpoint that performs write operations; a session on the reader endpoint runs read-only statements on an Aurora Replica.",
     "facts": ["aurora-cluster-endpoint-only-one-for-writes", "aurora-reader-endpoint-balances-each-connection-read-only-session"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "aurora-trap-global-all-regions-write",
     "belief": "Every Region of an Aurora global database accepts writes, as every replica of a DynamoDB global table does.",
     "truth": "Only the primary cluster performs write operations; a secondary Region runs Aurora Replicas only, and write forwarding sends its writes to the primary.",
     "facts": ["aurora-global-db-only-primary-writes", "aurora-global-db-secondary-region-readers-only", "aurora-global-db-write-forwarding-auto-forwards-to-primary"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "aurora-trap-switchover-for-region-outage",
     "belief": "When the primary Region of an Aurora global database has an outage, you run a switchover to move the primary role.",
     "truth": "Switchovers are for global databases whose clusters are all healthy; to recover from an unplanned outage, you use the failover mechanism.",
     "facts": ["aurora-global-db-switchover-healthy-only-unplanned-use-failover", "aurora-global-db-failover-use-for-unplanned-outage"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "aurora-trap-encrypt-existing-in-place",
     "belief": "You can turn on encryption for an existing unencrypted Aurora cluster by modifying it.",
     "truth": "You cannot convert an unencrypted DB cluster to an encrypted one; restore an unencrypted snapshot to a new cluster and specify a KMS key.",
     "facts": ["aurora-encryption-cannot-convert-unencrypted-in-place", "aurora-restore-unencrypted-snapshot-specify-kms-key"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "aurora-trap-single-instance-is-ha",
     "belief": "Because the cluster volume keeps six copies in three Availability Zones, a cluster with one DB instance is highly available and fails over in seconds.",
     "truth": "The copies protect the data, not the compute: without an Aurora Replica, Aurora recreates the primary instance, which typically takes less than 10 minutes, and after an AZ outage you create new instances yourself.",
     "facts": ["aurora-failover-time-without-replica", "aurora-single-az-cluster-create-instances-manually", "aurora-storage-six-copies-three-azs"],
     "placed_in": "2-deep.md#every-write-is-stored-as-six-copies-across-three-availability-zones (Exam trap callout)"},
    {"id": "aurora-trap-reader-endpoint-balances-queries",
     "belief": "The reader endpoint spreads every query evenly across the Aurora Replicas, also when the application keeps one long-lived connection pool.",
     "truth": "The reader endpoint balances connections, not individual queries; to balance each query, the application opens a new connection for each query.",
     "facts": ["aurora-reader-endpoint-balances-connections-not-queries", "aurora-reader-endpoint-new-connection-per-query-to-balance"],
     "placed_in": "2-deep.md#the-reader-endpoint-spreads-connections-not-single-queries-across-replicas (Exam trap callout)"},
    {"id": "aurora-trap-auto-scaling-scales-writer",
     "belief": "Aurora Auto Scaling adds capacity for writes when the writer is busy.",
     "truth": "Aurora Auto Scaling adds and removes Aurora Replicas and helps only the reader instances; the writer keeps its instance class.",
     "facts": ["aurora-autoscaling-writer-not-scaled", "aurora-cmp-aurora-auto-scaling-adjusts-replicas"],
     "placed_in": "2-deep.md#aurora-auto-scaling-adds-and-removes-aurora-replicas-for-read-load (Exam trap callout)"},
    {"id": "aurora-trap-serverless-pauses-whenever-idle",
     "belief": "An idle Aurora Serverless v2 database costs nothing, whatever its settings.",
     "truth": "Instances pause only when the minimum capacity is zero ACUs and no connection is open (RDS Proxy keeps one open); a minimum above zero never pauses, and storage is charged even while paused.",
     "facts": ["aurora-serverless-auto-pause-min-capacity-zero", "aurora-serverless-min-capacity-above-zero-no-pause",
               "aurora-serverless-rds-proxy-blocks-auto-pause", "aurora-serverless-auto-pause-billing-storage-still-charged"],
     "placed_in": "2-deep.md#aurora-serverless-v2-changes-capacity-with-load-inside-a-range-you-set (Exam trap callout)"},
    {"id": "aurora-trap-postgres-cross-region-replica",
     "belief": "An Aurora PostgreSQL cluster can get a cross-Region read replica cluster, as Aurora MySQL can with binlog replication.",
     "truth": "Aurora PostgreSQL does not support cross-Region Aurora Replicas; Aurora Global Database takes its reads and its recovery to other Regions.",
     "facts": ["aurora-postgres-no-cross-region-aurora-replicas", "aurora-mysql-cross-region-read-replica-cluster"],
     "placed_in": "2-deep.md#aurora-global-database-copies-the-cluster-volume-to-read-only-regions (Exam trap callout)"},
    {"id": "aurora-trap-global-failover-no-data-loss",
     "belief": "A failover of an Aurora global database after a Region outage loses no data, because replication takes about a second.",
     "truth": "Replication to the secondaries is asynchronous, so a failover can lose writes that were not replicated (RPO typically seconds); only a switchover of healthy clusters has an RPO of 0.",
     "facts": ["aurora-global-db-failover-can-lose-writes-consistent-state", "aurora-global-failover-rpo-nonzero-seconds", "aurora-global-switchover-rpo-zero"],
     "placed_in": "2-deep.md#a-secondary-region-takes-over-by-failover-after-an-outage-by-switchover-when-healthy (Exam trap callout)"},
    {"id": "aurora-trap-restore-in-place",
     "belief": "A point-in-time restore rolls the running Aurora cluster back, so the application keeps its endpoint.",
     "truth": "A point-in-time or snapshot restore creates a new DB cluster with new endpoints; only Backtrack rewinds a cluster in place, and only on Aurora MySQL clusters created with Backtrack enabled.",
     "facts": ["aurora-pitr-creates-new-cluster", "aurora-restore-always-creates-new-cluster", "aurora-backtrack-only-if-enabled-at-creation",
               "aurora-backtrack-in-minutes-no-new-cluster"],
     "placed_in": "2-deep.md#backups-are-continuous-and-every-restore-creates-a-new-cluster (Exam trap callout)"},
    {"id": "aurora-trap-io-optimized-always-cheaper",
     "belief": "Aurora I/O-Optimized always costs less, because it has no I/O charges.",
     "truth": "I/O-Optimized is the best choice when I/O is 25% or more of the Aurora spend; below that share, Aurora Standard costs less.",
     "facts": ["aurora-io-optimized-best-when-io-25-percent-or-more", "aurora-standard-best-when-io-under-25-percent"],
     "placed_in": "2-deep.md#aurora-standard-charges-for-each-io-and-io-optimized-includes-it (Exam trap callout)"},
]
BRIEF["traps_from_other_chapters"] = {
    "rule": ("Question writers can tag a distractor with a trap id of another chapter when the distractor states exactly that belief "
             "(lint.traps() knows them). Q205 needs a trap id on at least half of all wrong options of the chapter; reuse is allowed. "
             "Candidates that fit Aurora stems:"),
    "ids": ["rds-trap-standby-serves-reads", "rds-trap-read-replica-for-failover", "rds-trap-multi-az-is-a-backup",
            "how-the-exam-asks-trap-multi-az-covers-region", "aws-map-trap-one-az-is-highly-available", "aws-map-trap-sync-replication-across-regions",
            "aws-map-trap-region-auto-replicates", "kms-trap-key-is-global", "lambda-trap-connection-per-invocation"],
    "check": "Before tagging, confirm each id with lint.traps() (the planning list of chapter 26 named them; chapters 01, 02, 06 and 18 own them).",
}

BRIEF["compare_tables"] = [
    {"title": "Aurora, RDS or DynamoDB", "section": "1-fast.md#choose-it-or-not", "h3_section_id": "aurora-rds-or-dynamodb",
     "neighbours": ["Amazon Aurora", "Amazon RDS", "Amazon DynamoDB"],
     "rows": ("Columns: Question | Amazon Aurora | Amazon RDS | Amazon DynamoDB. Data model: relational, [compatible with MySQL and PostgreSQL] "
              "(aurora-is-managed-relational-engine) | relational, [six popular engines] (rds-decision-guide-rds-row) | [Key-value] "
              "(dynamodb-decision-guide-key-value-session-store) and document. Storage: one volume, [six copies] "
              "(aurora-storage-six-copies-three-azs) shared by all instances | [Amazon RDS uses EBS volumes] (rds-storage-ebs-striping) for each "
              "instance | managed by AWS (no link). Joins (cut first if over budget): both relational engines support [complex queries through "
              "joins] (rds-decision-guide-relational-joins): write the cell once across the two columns or 'yes' in the RDS column | removing "
              "joins is [at the heart of NoSQL data modeling] (dynamodb-no-joins-heart-of-nosql-modeling). Three rows."),
     "deciding_question": "Does the data need SQL and joins, and must many replicas read it with almost no lag?"},
    {"title": "Aurora Replica, RDS read replica or Multi-AZ standby", "section": "1-fast.md#choose-it-or-not",
     "h3_section_id": "aurora-replica-rds-read-replica-or-multi-az-standby",
     "neighbours": ["Aurora Replica", "RDS read replica", "RDS Multi-AZ DB instance standby"],
     "rows": ("Columns: Question | Aurora Replica | RDS read replica | Multi-AZ standby. Where the data comes from: it reads the writer's "
              "volume: replicas [connect to the same storage volume] (aurora-adding-replicas-read-same-volume-offload) | RDS [copies them "
              "asynchronously to the read replica] (rds-read-replica-async-read-only) | a [synchronous standby replica in a different "
              "Availability Zone] (rds-multi-az-instance-standby-no-reads). Serves reads: yes | yes | no. Write 'no' only in a cell that links "
              "[doesn't serve read traffic] (rds-multi-az-one-vs-two-standbys). Takes over automatically: yes, Aurora [automatically fails over "
              "to an Aurora Replica] (aurora-auto-failover-to-replica) | no: it [Can be manually promoted] (rds-compare-failover-vs-promote) | "
              "yes: [Automatic failover to standby] (rds-compare-failover-vs-promote). Three rows; a failover-time row is optional and only with "
              "the links [less than 60 seconds] (aurora-failover-time-with-replica-guide), [several minutes or longer] "
              "(rds-read-replica-promote-reboot-minutes), [60–120 seconds] (rds-multi-az-instance-failover-time)."),
     "deciding_question": "Must the copy serve reads, take over by itself, or both?"},
    {"title": "Provisioned instances or Aurora Serverless v2", "section": "1-fast.md#choose-it-or-not",
     "h3_section_id": "provisioned-instances-or-aurora-serverless-v2",
     "neighbours": ["provisioned DB instances", "Aurora Serverless v2"],
     "rows": ("Columns: Question | Provisioned | Aurora Serverless v2 (3 columns). Fits: [suitable for steady workloads] "
              "(aurora-serverless-provisioned-suited-to-steady-workloads) | [variable or \"spiky\" workloads] "
              "(aurora-serverless-choose-variable-spiky-workloads). Unit of capacity: the instance class [determines the computation and memory "
              "capacity] (aurora-instance-class-determines-compute-memory) | ACUs of [approximately 2 gibibytes (GiB) of memory] "
              "(aurora-serverless-acu-about-2-gib-memory) each. Bill (cut first if over budget): [relatively easy to forecast] "
              "(aurora-serverless-provisioned-constant-capacity-predict-ahead) | [measured in terms of ACU-hours] "
              "(aurora-serverless-billing-unit-acu-hours). Three rows."),
     "deciding_question": "Can you predict the load well enough to choose an instance size in advance?"},
    {"title": "Aurora Global Database or DynamoDB global tables", "section": "1-fast.md#choose-it-or-not",
     "h3_section_id": "aurora-global-database-or-dynamodb-global-tables",
     "neighbours": ["Aurora Global Database", "DynamoDB global tables"],
     "rows": ("Columns: Question | Aurora Global Database | DynamoDB global tables (3 columns). Who writes: [Only the primary cluster performs "
              "write operations] (aurora-global-db-only-primary-writes) | [Any global table replica] "
              "(dynamodb-global-table-any-replica-serves-reads-writes) can [serve reads and writes] (dynamodb-global-table-any-replica-serves-reads-writes). "
              "After a Region outage: you [perform a cross-Region failover] (aurora-global-db-failover-cross-region-to-secondary) | [there is no "
              "need for a database failover] (dynamodb-gt-multi-active-no-failover-needed). Data model: relational SQL | key-value (no links; "
              "table 1 has them). Three rows."),
     "deciding_question": "Must every Region accept writes, or is one writer Region enough?"},
]

BRIEF["signals"] = [
    {"stem": "read-heavy; replicas fall behind at peak; scale reads with low lag",
     "think": "Aurora Replicas behind the reader endpoint", "fact": "aurora-adding-replicas-read-same-volume-offload",
     "because": "replicas [connect to the same storage volume] (aurora-adding-replicas-read-same-volume-offload)",
     "but_not_if": "the data is key-value with no joins and needs [single-digit millisecond performance at any scale] (dynamodb-decision-guide-key-value-session-store): Amazon DynamoDB"},
    {"stem": "unpredictable or spiky load; database used a few hours a day",
     "think": "Aurora Serverless v2", "fact": "aurora-serverless-choose-variable-spiky-workloads",
     "because": "it is intended for [variable or \"spiky\" workloads] (aurora-serverless-choose-variable-spiky-workloads)",
     "but_not_if": "the load is steady for years: provisioned instances with Reserved Instances, [appropriate for steady-state database workloads] (aurora-pricing-reserved-instances-steady-state)"},
    {"stem": "Region outage; RPO of seconds; relational database",
     "think": "Aurora Global Database", "fact": "aurora-global-replication-latency-under-1-second",
     "because": "storage replication runs with latency [typically under a second] (aurora-global-replication-latency-under-1-second)",
     "but_not_if": "an RPO of hours is enough at the lowest cost: copy snapshots to the second Region; you [manually copy Aurora snapshots] (aurora-no-cross-region-automated-backup-replication)"},
    {"stem": "low-latency reads for users around the world",
     "think": "Aurora Global Database, reads from each Region's reader endpoint", "fact": "aurora-cmp-global-db-low-latency-reads-worldwide",
     "because": "it serves [low-latency read operations for applications] (aurora-cmp-global-db-low-latency-reads-worldwide) in each Region",
     "but_not_if": "users in every Region also write often and locally: DynamoDB global tables, where any replica can [serve reads and writes] (dynamodb-global-table-any-replica-serves-reads-writes)"},
    {"stem": "fail over automatically within a minute if the writer fails",
     "think": "an Aurora Replica in another Availability Zone", "fact": "aurora-auto-failover-to-replica",
     "because": "Aurora [automatically fails over to an Aurora Replica] (aurora-auto-failover-to-replica) in [less than 60 seconds] (aurora-failover-time-with-replica-guide)",
     "but_not_if": "the cluster keeps one instance to save cost: then the writer is recreated, typically in [less than 10 minutes] (aurora-failover-time-without-replica)"},
    {"stem": "test with a copy of production data; ready in minutes; no impact on production",
     "think": "Aurora cloning", "fact": "aurora-clone-shares-data-pages-separate-volume",
     "because": "a clone [shares the same data pages as the original] (aurora-clone-shares-data-pages-separate-volume) at first",
     "but_not_if": "the copy must be in another Region: copy a snapshot; you [can't create a clone] (aurora-clone-same-region-only) in a different Region"},
    {"stem": "undo a bad change in minutes; keep the same cluster (Aurora MySQL)",
     "think": "Backtrack", "fact": "aurora-backtrack-in-minutes-no-new-cluster",
     "because": "it [rewinds the DB cluster in minutes] (aurora-backtrack-in-minutes-no-new-cluster)",
     "but_not_if": "the cluster runs Aurora PostgreSQL: a point-in-time restore to a new cluster; [Backtrack is not available for Aurora PostgreSQL] (aurora-backtrack-not-for-postgresql)"},
    {"stem": "I/O-intensive; unpredictable I/O costs",
     "think": "Aurora I/O-Optimized", "fact": "aurora-io-optimized-no-io-charges",
     "because": "it has [no additional charges for read and write I/O] (aurora-io-optimized-no-io-charges)",
     "but_not_if": "I/O is [less than 25%] (aurora-standard-best-when-io-under-25-percent) of the Aurora spend: Aurora Standard"},
]

BRIEF["words_table"] = [
    {"term": "read replica", "respelling": "REP-lih-kuh", "collocation": "promote a read replica (bold: promote)", "do_not_confuse": "Aurora Replica (same volume) and standby"},
    {"term": "fail over", "respelling": "FAYL OH-ver", "collocation": "an automatic failover (bold: automatic)", "do_not_confuse": "switchover (a planned move of a global database)"},
    {"term": "scale out", "respelling": None, "collocation": "scale out on a metric (bold: metric)", "do_not_confuse": "scale up (a larger instance class)"},
    {"term": "serverless", "respelling": None, "collocation": "a serverless option (bold: option)", "do_not_confuse": "Aurora Serverless v1 (deprecated)"},
    {"term": "durability", "respelling": "dyoor-uh-BIL-ih-tee", "collocation": "durable storage (bold: storage)", "do_not_confuse": "availability"},
    {"term": "recovery point objective", "respelling": None, "collocation": "meet an RPO (bold: meet)", "do_not_confuse": "recovery time objective"},
    {"term": "recovery time objective", "respelling": None, "collocation": "an RTO of hours (bold: hours)", "do_not_confuse": "recovery point objective"},
    {"term": "reader endpoint", "respelling": None, "collocation": "connect to the reader endpoint (bold: connect)",
     "do_not_confuse": "cluster endpoint (writes)", "note": "not in data/terms.json yet: needs-term marker (term_requests)"},
]

BRIEF["numbers"] = {
    "a_list": [
        {"display": "up to 15 Aurora Replicas in addition to the primary DB instance", "fact": "aurora-replicas-up-to-15-in-addition-to-primary", "card": "aurora-c001",
         "note": "the quota [15 read replicas] (aurora-quota-read-replicas-per-primary) cannot be raised for Aurora"},
        {"display": "six copies", "fact": "aurora-storage-six-copies-three-azs", "card": "aurora-c002",
         "note": "of the data, across [three AZs] (aurora-storage-six-copies-three-azs); you pay for one copy"},
        {"display": "less than 60 seconds", "fact": "aurora-failover-time-with-replica-guide", "card": "aurora-c003",
         "note": "typical failover with an Aurora Replica, often [less than 30 seconds] (aurora-failover-time-with-replica-guide)"},
        {"display": "less than 10 minutes", "fact": "aurora-failover-time-without-replica", "card": "aurora-c004",
         "note": "typical recovery with no Aurora Replica: Aurora recreates the primary"},
        {"display": "much less than 100 milliseconds", "fact": "aurora-replica-lag-under-100-ms", "card": "aurora-c005",
         "note": "usual Aurora Replica lag in the same Region; it grows with the write rate"},
        {"display": "typically under a second", "fact": "aurora-global-replication-latency-under-1-second", "card": "aurora-c006",
         "note": "Aurora Global Database replication latency to secondary Regions"},
        {"display": "less than 1 minute", "fact": "aurora-global-promote-secondary-under-1-minute", "card": "aurora-c007",
         "note": "AWS's figure for promoting a secondary Region (product page and FAQ); the user guide says RTO [in the order of minutes] (aurora-global-rto-order-of-minutes-guide). Never let the difference decide an answer."},
        {"display": "1–35 days", "fact": "aurora-backup-retention-period-range-1-35-days", "card": "aurora-c008",
         "note": "backup retention period; automated backups cannot be turned off"},
    ],
    "b_list": [
        {"display": "25% or more", "fact": "aurora-io-optimized-best-when-io-25-percent-or-more", "note": "I/O share of Aurora spend at which I/O-Optimized is the best choice"},
        {"display": "once every 30 days", "fact": "aurora-io-switch-standard-to-io-optimized-once-every-30-days", "note": "how often a cluster can move from Standard to I/O-Optimized"},
        {"display": "72 hours", "fact": "aurora-backtrack-window-limit-72-hours", "note": "limit of the Backtrack window (Aurora MySQL only)"},
        {"display": "0 for the highest priority to 15 for the lowest priority", "fact": "aurora-promotion-priority-range", "note": "promotion tiers of Aurora Replicas"},
        {"display": "up to 16 read-only DB instances", "fact": "aurora-global-secondary-cluster-max-16-reader-instances", "note": "in a secondary cluster of a global database"},
        {"display": "approximately 2 gibibytes (GiB) of memory", "fact": "aurora-serverless-acu-about-2-gib-memory", "note": "one ACU, with matching CPU and networking"},
        {"display": "maximum of 256 ACUs", "fact": "aurora-serverless-capacity-range-0-256-acu-half-acu-steps", "note": "top of the Aurora Serverless v2 range on current versions (volatile: B-list only, never a question key)"},
        {"display": "approximately 15 seconds", "fact": "aurora-serverless-auto-pause-resume-about-15-seconds", "note": "typical resume of a paused instance"},
        {"display": "within 5 minutes of the current time", "fact": "aurora-backup-latest-restorable-time-within-5-minutes", "note": "typical latest restorable time"},
        {"display": "one day", "fact": "aurora-backup-retention-default-1-day", "note": "default backup retention period"},
        {"display": "up to seven days", "fact": "aurora-stop-cluster-up-to-seven-days", "note": "longest stop of a cluster; then Aurora starts it"},
        {"display": "10 GiB segments", "fact": "aurora-storage-segment-size-10-gib", "note": "size of the pieces that Aurora repairs"},
    ],
    "not_used": [
        "No prices: the chapter has no verified fact of kind price. Tasks cost $0.",
        "256 TiB (volume maximum) and 10 secondary Regions are volatile, changed in 2025: Changed recently only (and the subsection 3 table), never an A-list row or a question key.",
        "Custom endpoints per cluster: two facts with different scopes (guide: up to five, not adjustable; quotas page: 5, adjustable): write no number.",
        "Account quotas (40 clusters, 40 instances, 100 manual snapshots): reference only; the Look task shows the cluster quota.",
        "SLA credit thresholds (99.99% Multi-AZ, 99.9% Single-AZ) and the Limitless Database 99.99%: service-credit terms or a feature outside the exam: no row.",
        "Reserved Instance discounts (up to 45% and 66%), Database Savings Plans (up to 35%, volatile), I/O-Optimized savings (up to 40%): chapter 41 owns discounts; no row.",
    ],
}

BRIEF["changed_recently"] = {
    "fast": [
        {"date": "2023-08-21", "what": "Aurora Global Database: the planned move is now called switchover; managed failover handles outages",
         "fact": "aurora-change-global-failover-managed-unplanned",
         "old_display": "managed planned failover", "now_display": "in typically a minute",
         "exam_probably_expects": "older questions say 'managed planned failover' for a planned move of the primary Region; read it as switchover. Prefer an option that is right under both names.",
         "status": "examinable",
         "note": "Old: '[managed planned failover] (aurora-change-global-failover-managed-unplanned)'. Now: 'switchover for a planned move; managed failover converts a secondary Region into the new primary [in typically a minute] (aurora-change-global-failover-managed-unplanned) after an outage'. changed.date 2023-08-21 = the date in the first line."},
        {"date": "2024-11-20", "what": "Aurora Serverless v2 can scale to zero ACUs and pause",
         "fact": "aurora-serverless-change-scale-to-zero",
         "old_display": "0.5 ACUs", "now_display": "0 ACUs",
         "exam_probably_expects": "older questions say the minimum is 0.5 ACU and that Aurora Serverless v2 cannot pause. Prefer an option that is right under both values.",
         "status": "examinable",
         "note": "Old: '[0.5 ACUs] (aurora-serverless-change-scale-to-zero) minimum'. Now: 'a minimum of [0 ACUs] (aurora-serverless-change-scale-to-zero); the instance pauses when idle'. Volatile fact: never a question key."},
        {"date": "2025-05-21", "what": "More secondary Regions in an Aurora global database",
         "fact": "aurora-global-secondary-regions-max-10",
         "old_display": "up to 5 secondary Regions", "now_display": "up to 10 secondary AWS Regions",
         "exam_probably_expects": "older questions may say five secondary Regions. Do not let the count decide an answer.",
         "status": "examinable",
         "note": "Volatile fact: never a question key."},
    ],
    "alternate": [
        {"date": "2025-07-03", "what": "Larger Aurora cluster volumes", "fact": "aurora-change-storage-max-256-tib",
         "old_display": "128 TiB", "now_display": "256 TiB",
         "exam_probably_expects": "older questions say 128 TiB; the maximum now depends on the engine version. Do not let the size decide an answer.",
         "status": "examinable", "rule": "write it only if the three entries above stay under 90 words"},
    ],
    "pending": [
        {"date": "2026-02-18", "what": "New Aurora clusters are encrypted by default", "fact": "aurora-change-default-encryption-new-clusters",
         "old_display": "not available. (new feature: write the fixed text)", "now_display": "encrypted by default with an AWS owned key",
         "exam_probably_expects": "older questions assume that a new cluster is unencrypted unless you choose encryption; existing clusters keep their setting.",
         "status": "examinable (2026-02-18 is before the cut-off 2026-07-15)",
         "pending": "fr-0092 (fact_requests, filed by brief-27): the fact has no changed record, so L107 cannot check the date. Write the entry only when the request is filled; if it is closed as unfillable, mention the default only as the body_extras sentence of subsection 14."},
    ],
    "considered_not_used": [
        {"fact": "aurora-serverless-change-instant-scaling-16-acu", "why": "posted 2026-09-30, after the cut-off (not examinable yet), and the fact has no changed record, so a B-list entry cannot pass L107; reference only"},
        {"fact": "aurora-change-mysql-delayed-replication", "why": "posted 2026-09-03, not examinable yet, no changed record; Aurora MySQL binlog detail"},
        {"fact": "aurora-serverless-change-v1-deprecation-date-extended", "why": "the changed record is about the extension of a date; the book teaches Aurora Serverless v2 as current truth and names v1 once as deprecated"},
        {"fact": "aurora-change-io-optimized-introduced", "why": "no changed record; I/O-Optimized is current truth in subsection 12"},
        {"fact": "aurora-change-global-writer-endpoint", "why": "no changed record; the global writer endpoint is current truth in subsection 10"},
        {"fact": "aurora-change-blue-green-deployments-introduced", "why": "Blue/Green Deployments belong to chapter 26; reference only"},
        {"fact": "aurora-change-limitless-database-ga", "why": "Limitless Database is outside the exam's focus; reference only"},
        {"fact": "aurora-change-dsql-generally-available", "why": "Aurora DSQL is not in the in-scope service list"},
        {"fact": "aurora-change-performance-insights-end-of-life", "why": "monitoring belongs to chapter 37"},
        {"fact": "aurora-change-database-savings-plans-announced", "why": "chapter 41 owns Database Savings Plans"},
        {"fact": "aurora-serverless-change-platform-version-4-performance", "why": "no changed record and no answer depends on it"},
    ],
}

BRIEF["faq"] = [
    {"n": 1, "q": "Can you turn off automated backups on Aurora?", "fact": "aurora-faq-automated-backups-always-on",
     "answer": "No; automated continuous backups are [always enabled] (aurora-faq-automated-backups-always-on)",
     "url": "https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq-availability-and-durability.html",
     "quote": "Yes, automated continuous backups are always enabled on Amazon Aurora DB Instances with no database performance impact."},
    {"n": 2, "q": "Can a low promotion tier keep a replica from ever becoming the writer?", "fact": "aurora-faq-low-priority-replica-still-promoted-if-needed",
     "answer": "No; if the higher tiers are unhealthy, Amazon RDS [will promote the lower priority replica] (aurora-faq-low-priority-replica-still-promoted-if-needed)",
     "url": "https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq-availability-and-durability.html",
     "quote": "However, if the higher priority replicas on the cluster are unhealthy or unavailable, Amazon RDS will promote the lower priority replica."},
    {"n": 3, "q": "Can Aurora Replicas in the same Region lag seconds behind?", "fact": "aurora-faq-replica-lag-tens-of-ms-same-region",
     "answer": "Rarely; AWS typically observes [tens of milliseconds] (aurora-faq-replica-lag-tens-of-ms-same-region)",
     "url": "https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq-availability-and-durability.html",
     "quote": "Since replicas share the same data volume as the primary instance in the same AWS Region, there is virtually no replication lag."},
    {"n": 4, "q": "Can you set up cross-Region replicas for Aurora?", "fact": "aurora-faq-cross-region-physical-or-logical",
     "answer": "Yes, with [either physical or logical replication] (aurora-faq-cross-region-physical-or-logical); physical replication is Aurora Global Database",
     "url": "https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq-availability-and-durability.html",
     "quote": "Yes, you can set up cross-Region replicas using either physical or logical replication."},
    {"n": 5, "q": "Can an application keep its connection settings when the primary Region fails?", "fact": "aurora-faq-global-db-no-code-change-writer-endpoint",
     "answer": "Yes; the Global Database writer endpoint lets you [avoid the need to make application code changes] (aurora-faq-global-db-no-code-change-writer-endpoint)",
     "url": "https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq-availability-and-durability.html",
     "quote": "You can also use the Aurora Global Database writer endpoint to avoid the need to make application code changes."},
    {"n": 6, "q": "Can you restore a snapshot into the cluster that is running?", "fact": "aurora-faq-snapshot-restore-new-instance",
     "answer": "No; a restore [requires the creation of a new DB Instance] (aurora-faq-snapshot-restore-new-instance)",
     "url": "https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq-availability-and-durability.html",
     "quote": "Note that restoring data from  snapshots requires the creation of a new DB Instance.",
     "quote_note": "the page has two spaces between 'from' and 'snapshots': copy the quote exactly"},
    {"n": 7, "q": "Do you pay extra for the replication between Availability Zones?", "fact": "aurora-faq-replication-not-charged",
     "answer": "No; [Aurora replication is bundled into the price] (aurora-faq-replication-not-charged)",
     "url": "https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq-billing.html",
     "quote": "No, Aurora replication is bundled into the price."},
    {"n": 8, "q": "Can one cluster mix provisioned and Aurora Serverless v2 instances?", "fact": "aurora-serverless-faq-mixed-cluster-with-provisioned",
     "answer": "Yes; a mixed-configuration cluster can hold [any combination of provisioned and serverless instances] (aurora-serverless-faq-mixed-cluster-with-provisioned)",
     "url": "https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq-scalability.html",
     "quote": "Yes, you can add Aurora serverless instances to your existing Aurora DB cluster , creating a mixed-configuration cluster with any combination of provisioned and serverless instances.",
     "quote_note": "the page has a space before the comma after 'cluster': copy the quote exactly"},
    {"n": 9, "q": "Does Aurora encryption also cover backups and replicas?", "fact": "aurora-faq-encryption-covers-backups-replicas",
     "answer": "Yes; it covers the storage and the [automated backups, snapshots, and replicas] (aurora-faq-encryption-covers-backups-replicas) of the cluster",
     "url": "https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq-security.html",
     "quote": "When encryption is enabled, data stored at rest in the underlying storage is encrypted, along with automated backups, snapshots, and replicas in the same cluster."},
    {"n": 10, "q": "Do you need special drivers to connect to Aurora?", "fact": "aurora-faq-no-special-drivers",
     "answer": "No; Aurora works with [standard MySQL and PostgreSQL database drivers] (aurora-faq-no-special-drivers)",
     "url": "https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq.html",
     "quote": "Aurora works with standard MySQL and PostgreSQL database drivers."},
]
BRIEF["faq_alternates"] = ["aurora-faq-pay-for-one-copy", "aurora-faq-io-optimized-works-with-reserved-instances", "aurora-faq-tolerates-two-copies-lost-write",
                           "aurora-serverless-faq-snapshot-restore-both-directions", "aurora-faq-shared-snapshot-same-region-only",
                           "aurora-faq-promotion-highest-priority-first"]
BRIEF["faq_note"] = (
    "Each quote block holds one whole sentence of the evidence quote of the item's fact, copied exactly (F2, L306); the 'quote' field of each "
    "item is that sentence, checked against the stored evidence. All quotes are on the Aurora FAQ pages of the extended-content guide "
    "(https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/). The link line under each quote names the page, for example "
    "'— [Aurora FAQ: availability and durability](<url>)'. If the section runs over 430 words, replace item 8 (the longest quote) with "
    "aurora-faq-io-optimized-works-with-reserved-instances (quote: 'Yes, Aurora I/O-Optimized works with existing Aurora Reserved Instances.'). "
    "Do not use aurora-faq-pay-for-one-copy unless needed: its only sentence also holds the volatile 256 TiB figure.")

BRIEF["story"] = {
    "stage": 3, "month": 20,
    "trigger": "With the bank, the database grows from 400 GB to 1.2 TB. At peak the read replica is 40 seconds behind, and dashboards show old data.",
    "problem": ("Callvale's PostgreSQL database holds 1.2 TB, and 90% of queries are reads. At peak, the one read replica is up to 40 seconds "
                "behind the primary. Callvale needs several replicas behind one endpoint, fast failover, and a path to a second Region. The "
                "application must stay PostgreSQL-compatible."),
    "uses_numbers": ["database_size_gb", "database_read_percent", "replica_behind_seconds", "aurora_replicas", "dev_staging_hours_per_week"],
    "state_at_month_20": ("Stage 3, story order 30 (month 20, after chapter 19 in the same month). Before this chapter: RDS for PostgreSQL with a "
                          "Multi-AZ DB instance (one standby) since month 8 (26); one read replica for dashboard queries and RDS Proxy since stage 2 "
                          "(26 later line); DynamoDB jobs table (28); ElastiCache for sessions and results (29); seven accounts (04); customer "
                          "managed keys (06, alias/callvale-db); rotated database credentials (07); Fargate services (19, month 20, same month, "
                          "earlier in story order); three Availability Zones in prod. Not yet: AWS Backup (24, month 22), a second Region "
                          "(40, stage 4)."),
    "rules": ("Question stems never name Callvale. The story never teaches a fact. No dollar amounts in story text. Ben's question is the "
              "speak item aurora-s01. W903: in the Startup example callouts and the Decision record, write digits only for numbers of "
              "uses_numbers: 1.2 TB (database_size_gb 1200 at stage 3, written '1.2 TB' as the JSON meaning says; if W903 warns on 1.2, report "
              "it, do not change the story), 400 GB (stage 2 value of the same key), 90 (percent of reads), 40 (seconds behind), 2 (Aurora "
              "Replicas; prefer the word 'two'), 50 (hours a week of dev and staging). Write AZ 1 to AZ 3 as labels only in diagrams."),
}

BRIEF["decision_record"] = {
    "status": "write",
    "context": ("The trigger of data/startup.json chapter 27, at most 80 words, stage 3: Callvale now serves the bank. Its PostgreSQL database "
                "has grown from 400 GB to 1.2 TB, and 90% of queries are reads. At peak, the one RDS read replica is 40 seconds behind, and "
                "dashboards show old data. The application must stay PostgreSQL-compatible, and the bank's contract will need a second Region."),
    "requirement": ("Several low-lag replicas must serve reads behind one endpoint, the database must fail over fast, and a second Region must "
                    "be possible later, in the MOST scalable way (qualifier of the JSON: most scalable)."),
    "requirement_qualifier": "most scalable",
    "options": ["a larger RDS instance with more read replicas", "Amazon Aurora PostgreSQL (chosen)", "a cache for all dashboard reads"],
    "decision": ("An Aurora PostgreSQL cluster with one writer and two Aurora Replicas in three Availability Zones (data/startup.json choice). "
                 "Dev and staging, used 50 hours a week, run Aurora Serverless v2 (data/startup.json note)."),
    "reasons_with_facts": [
        "Option 1 keeps the lag: RDS [copies them asynchronously to the read replica] (rds-read-replica-async-read-only) for each replica, each on its own storage ([Amazon RDS uses EBS volumes] (rds-storage-ebs-striping)), and with several replicas [it is up to your application] (rds-faq-read-replica-own-endpoint) to spread the reads.",
        "Option 3 adds a second store: ElastiCache is an [ephemeral cache for frequently accessed data] (dynamodb-decision-guide-elasticache-caching-layer), so the database still needs replicas, and results in the cache can be older than the database (story reason, no fact).",
        "Option 2: Aurora Replicas [connect to the same storage volume] (aurora-adding-replicas-read-same-volume-offload) with lag usually [much less than 100 milliseconds] (aurora-replica-lag-under-100-ms); one reader endpoint spreads read connections; Aurora fails over to a replica in [less than 60 seconds] (aurora-failover-time-with-replica-guide); the same [code, tools, and applications] (aurora-existing-mysql-postgres-code-works) keep working; and Aurora Global Database can [span multiple AWS Regions] (aurora-faq-global-db-definition) later, the path for PostgreSQL, which [doesn't support cross-Region Aurora Replicas] (aurora-postgres-no-cross-region-aurora-replicas).",
    ],
    "tradeoff": ("A migration with a short cutover, and a new cost model to learn (data/startup.json tradeoff, word for word). Optional links: "
                 "the move by Aurora read replica can take [several hours per terabyte of data] (aurora-postgres-migrate-replica-hours-per-terabyte); "
                 "with Aurora Standard [you pay per-request for I/O] (aurora-faq-standard-pay-per-io-vs-io-optimized-included)."),
    "later": "One sentence at most: at stage 4, a secondary cluster in US West (Oregon) joins as an Aurora Global Database (chapter 40). No new option in the record.",
    "spot_the_bug": None,
    "diagrams": ["aurora-before", "aurora-after"],
}

BRIEF["realworld"] = {
    "status": "optional", "company": "DraftKings",
    "facts": ["aurora-case-draftkings-replication-lag-seconds-to-milliseconds", "aurora-case-draftkings-peak-traffic-minimal-delay",
              "aurora-case-draftkings-durable-three-azs-pay-one-copy"],
    "point": ("DraftKings, a sports and gaming company, moved to Aurora for its peak traffic; an architect says that instead of 30 seconds of "
              "replication lag they might see [10–30 milliseconds using Aurora] (aurora-case-draftkings-replication-lag-seconds-to-milliseconds). "
              "One AWS quote block of one whole sentence (22 words): \"With Aurora, DraftKings can effectively manage the intense read and "
              "write operations that are typical during peak traffic times, with minimal delay.\" "
              "(https://aws.amazon.com/solutions/case-studies/draftkings-aurora-case-study/). It shows: shared-storage replicas keep replica "
              "lag low at peak, the same problem as Callvale's 40-second replica. At most 100 words. Never part of Callvale's story. D13 asks "
              "for a year in bold: the saved quotes state none, so bold the company alone and report it. Alternative: BMW Group with Aurora "
              "Serverless v2, which can [scale to accommodate peaks on demand] (aurora-serverless-case-bmw-serverless-v2-automated-capacity-peaks)."),
    "rule": "Write it only if 2-deep.md stays at or under 4,390 words without it. It is not in the sections list, so leaving it out is no L905 error.",
}

BRIEF["devices"] = {
    "exam_trap_callouts_2_deep": {
        "every-write-is-stored-as-six-copies-across-three-availability-zones": "aurora-trap-single-instance-is-ha",
        "the-reader-endpoint-spreads-connections-not-single-queries-across-replicas": "aurora-trap-reader-endpoint-balances-queries",
        "aurora-auto-scaling-adds-and-removes-aurora-replicas-for-read-load": "aurora-trap-auto-scaling-scales-writer",
        "aurora-serverless-v2-changes-capacity-with-load-inside-a-range-you-set": "aurora-trap-serverless-pauses-whenever-idle",
        "aurora-global-database-copies-the-cluster-volume-to-read-only-regions": "aurora-trap-postgres-cross-region-replica",
        "a-secondary-region-takes-over-by-failover-after-an-outage-by-switchover-when-healthy": "aurora-trap-global-failover-no-data-loss",
        "backups-are-continuous-and-every-restore-creates-a-new-cluster": "aurora-trap-restore-in-place",
        "aurora-standard-charges-for-each-io-and-io-optimized-includes-it": "aurora-trap-io-optimized-always-cheaper",
    },
    "exam_trap_form": "> **Exam trap:** <wrong belief in plain words>. <truth with its fact link>. <!-- trap: <id> -->  Each one adds a new case; never restate the table above it. The plans give ready texts (exam_trap_text).",
    "fast_traps_list": ["aurora-trap-replicas-copy-data", "aurora-trap-writes-through-reader-endpoint", "aurora-trap-global-all-regions-write",
                        "aurora-trap-switchover-for-region-outage", "aurora-trap-encrypt-existing-in-place"],
    "fast_traps_links": ("Each fast trap item links one fact in its Truth part: replicas-copy-data [connect to the same storage volume] "
                         "(aurora-adding-replicas-read-same-volume-offload); writes-through-reader-endpoint [the only one that can perform write "
                         "operations] (aurora-cluster-endpoint-only-one-for-writes); global-all-regions-write [Only the primary cluster performs "
                         "write operations] (aurora-global-db-only-primary-writes); switchover-for-region-outage [recover from an unplanned outage] "
                         "(aurora-global-db-failover-use-for-unplanned-outage); encrypt-existing-in-place [can't convert an unencrypted DB "
                         "cluster] (aurora-encryption-cannot-convert-unencrypted-in-place)."),
    "go_deeper": [
        "every-write-is-stored-as-six-copies-across-three-availability-zones: fast restarts",
        "the-reader-endpoint-spreads-connections-not-single-queries-across-replicas: custom endpoints",
        "when-the-writer-fails-aurora-promotes-a-replica-behind-the-same-endpoint: which replica wins, and faster reconnects",
        "aurora-global-database-copies-the-cluster-volume-to-read-only-regions: write forwarding",
        "backups-are-continuous-and-every-restore-creates-a-new-cluster: Backtrack and clones",
    ],
    "spot_the_bug": [
        "when-the-writer-fails-aurora-promotes-a-replica-behind-the-same-endpoint: all three DB instances in one Availability Zone",
        "data-moves-into-aurora-by-snapshot-by-aurora-read-replica-or-by-aws-dms: promoting the Aurora read replica while the source still takes writes",
    ],
    "try_it": [
        "a-secondary-region-takes-over-by-failover-after-an-outage-by-switchover-when-healthy: aurora-t02",
        "encryption-at-rest-is-set-at-creation-and-covers-the-whole-cluster: aurora-t03",
    ],
    "startup_example_2_deep": ["aurora-replicas-read-the-shared-volume-so-replica-lag-stays-low: the 40-second replica and the two Aurora Replicas"],
    "predict_the_picture": "In one breath: 'When an application writes to an Aurora cluster with two Aurora Replicas, where does the data go, and where do the replicas read it from?' before the hero aurora-hero (LEARNING device 6).",
    "route_pass_subsections": [
        "aurora-replicas-read-the-shared-volume-so-replica-lag-stays-low",
        "when-the-writer-fails-aurora-promotes-a-replica-behind-the-same-endpoint",
        "aurora-serverless-v2-changes-capacity-with-load-inside-a-range-you-set",
        "aurora-global-database-copies-the-cluster-volume-to-read-only-regions",
    ],
    "route_pass_note": "Four of the maximum four (section_flag.h3_pass_route_subsections). The reader marked Aurora Serverless as 'right but not sure' in her diagnostic, so subsection 8 is on the pass route.",
    "xref_markers": [
        "02 AWS map (Regions and Availability Zones)",
        "06 KMS (customer managed keys, AWS owned keys)",
        "10 VPC (private subnets, security groups)",
        "18 Lambda (connections from many functions; RDS Proxy)",
        "24 AWS Backup (backup plans for Aurora)",
        "26 RDS (Multi-AZ, read replicas, RDS Proxy, Blue/Green Deployments)",
        "28 DynamoDB (key-value design, global tables)",
        "29 ElastiCache (caching layer)",
        "37 Monitoring (CloudWatch metrics, Database Activity Streams)",
        "39 Migration (AWS DMS and AWS SCT)",
        "40 HA and DR (pilot light, warm standby, RPO and RTO tests)",
        "41 Cost optimization (Reserved Instances, Database Savings Plans)",
    ],
}
