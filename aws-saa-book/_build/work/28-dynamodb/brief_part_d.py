# brief-28, part D: traps, compare tables, signals, words, numbers, changed recently, FAQ, story, decision record, real world, devices.

BRIEF["traps"] = [
    # five fast traps (1-fast.md Signals and traps, H3 Traps)
    {"id": "dynamodb-trap-spare-capacity-no-throttle",
     "belief": "If the table as a whole has unused capacity, no request is throttled.",
     "truth": "Each partition has its own ceiling of 3,000 read units and 1,000 write units per second, so traffic on one hot key or item is throttled while the rest of the table is idle.",
     "facts": ["dynamodb-partition-max-throughput", "dynamodb-hot-partitions-throttle-while-others-underutilized"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "dynamodb-trap-default-read-is-latest",
     "belief": "A read right after a write always returns the new value.",
     "truth": "Eventually consistent is the default for every read, and it might not reflect a write that just finished; set ConsistentRead to true on the table or an LSI to get the latest data.",
     "facts": ["dynamodb-eventually-consistent-default", "dynamodb-eventually-consistent-may-lag", "dynamodb-consistentread-parameter"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "dynamodb-trap-ttl-deletes-on-time",
     "belief": "Time to Live deletes an item at the second it expires, so expired items never appear in reads.",
     "truth": "DynamoDB deletes expired items within a few days of their expiration time; until then they still show in reads, so filter them out.",
     "facts": ["dynamodb-ttl-deletes-within-days-no-wcu", "dynamodb-ttl-expired-items-visible-until-deleted", "dynamodb-ttl-filter-expired-items-on-read"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "dynamodb-trap-dax-speeds-every-read",
     "belief": "DAX speeds up every read, strongly consistent reads included.",
     "truth": "DAX passes strongly consistent reads to DynamoDB and does not cache the results; it serves eventually consistent data.",
     "facts": ["dax-passes-through-strong-reads-and-transactions", "dax-eventually-consistent-microsecond-latency"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    {"id": "dynamodb-trap-global-table-primary-region",
     "belief": "A global table has a primary Region, and a Region outage needs a database failover to a secondary.",
     "truth": "A global table has no primary Region; any replica table serves reads and writes, so no database failover is required.",
     "facts": ["dynamodb-faq-global-tables-no-failover-needed", "dynamodb-global-table-any-replica-serves-reads-writes"],
     "placed_in": "1-fast.md#signals-and-traps (fast trap list)"},
    # eight Exam trap callouts in 2-deep.md
    {"id": "dynamodb-trap-gsi-strong-read",
     "belief": "A global secondary index can serve strongly consistent reads, like the table.",
     "truth": "Strongly consistent reads are supported only on tables and local secondary indexes; queries on a global secondary index are eventually consistent only.",
     "facts": ["dynamodb-strong-reads-only-tables-and-lsi", "dynamodb-index-read-consistency-gsi-vs-lsi"],
     "placed_in": "2-deep.md#read-and-write-units-depend-on-item-size-and-read-consistency (Exam trap callout)"},
    {"id": "dynamodb-trap-on-demand-absorbs-any-spike",
     "belief": "An on-demand table absorbs any traffic spike instantly, however large.",
     "truth": "On-demand instantly accommodates up to double the previous peak; traffic above double the previous peak within 30 minutes can be throttled, so pre-warm the table for a larger launch.",
     "facts": ["dynamodb-on-demand-previous-peak-double", "dynamodb-on-demand-throttle-if-double-within-30-min", "dynamodb-warm-throughput-prewarm-for-peak-events"],
     "placed_in": "2-deep.md#on-demand-mode-bills-each-request-and-needs-no-capacity-plan (Exam trap callout)"},
    {"id": "dynamodb-trap-auto-scaling-prevents-throttling",
     "belief": "Auto scaling on a provisioned table prevents throttling, even in a sudden spike.",
     "truth": "Auto scaling reacts after the target is breached for two consecutive minutes and takes several minutes to update capacity; throttling can occur regardless of auto scaling.",
     "facts": ["dynamodb-autoscaling-two-consecutive-minutes", "dynamodb-autoscaling-update-takes-minutes-throttle", "dynamodb-throttling-with-autoscaling-possible"],
     "placed_in": "2-deep.md#provisioned-mode-bills-the-capacity-you-set-and-auto-scaling-follows-within-minutes (Exam trap callout)"},
    {"id": "dynamodb-trap-filter-saves-capacity",
     "belief": "A filter expression on a Scan or Query lowers the read capacity that the request consumes.",
     "truth": "A filter is applied after the items are read, so the request consumes the same read capacity with or without it.",
     "facts": ["dynamodb-scan-filter-same-read-capacity", "dynamodb-query-filter-same-read-capacity"],
     "placed_in": "2-deep.md#a-query-reads-one-partition-key-but-a-scan-reads-every-item (Exam trap callout)"},
    {"id": "dynamodb-trap-lsi-added-later",
     "belief": "You can add a local secondary index to a table that already holds data.",
     "truth": "Local secondary indexes are created only when the table is created; to add an index later, create a global secondary index.",
     "facts": ["dynamodb-index-online-operations-gsi-vs-lsi", "dynamodb-lsi-created-with-table"],
     "placed_in": "2-deep.md#secondary-indexes-give-the-same-items-a-second-key-to-query (Exam trap callout)"},
    {"id": "dynamodb-trap-batch-write-is-atomic",
     "belief": "BatchWriteItem writes all of its items or none of them.",
     "truth": "With BatchWriteItem only some of the actions might succeed; TransactWriteItems is all-or-nothing.",
     "facts": ["dynamodb-transactwriteitems-vs-batchwriteitem", "dynamodb-transactwriteitems-all-or-nothing"],
     "placed_in": "2-deep.md#conditional-writes-and-transactions-stop-one-write-from-overwriting-another (Exam trap callout)"},
    {"id": "dynamodb-trap-stream-keeps-changes",
     "belief": "A DynamoDB stream keeps item changes for as long as consumers need them, like an archive.",
     "truth": "Stream records have a lifetime of 24 hours; Kinesis Data Streams for DynamoDB keeps records up to 1 year for replay.",
     "facts": ["dynamodb-stream-records-24-hours", "dynamodb-streams-vs-kds-retention"],
     "placed_in": "2-deep.md#dynamodb-streams-records-each-item-change-in-order-for-24-hours (Exam trap callout)"},
    {"id": "dynamodb-trap-restore-in-place",
     "belief": "A point-in-time restore or a backup restore rolls the existing table back in place.",
     "truth": "Every restore creates a new table, and a restore cannot overwrite an existing table; the application switches to the new table or items are copied back.",
     "facts": ["dynamodb-pitr-restores-to-new-table", "dynamodb-restore-cannot-overwrite-existing-table", "dynamodb-backup-restore-only-to-new-table"],
     "placed_in": "2-deep.md#every-restore-from-a-backup-or-a-point-in-time-creates-a-new-table (Exam trap callout)"},
]
BRIEF["traps_from_other_chapters"] = {
    "rule": ("Question writers can tag a distractor with a trap id of another chapter when the distractor states exactly that belief "
             "(lint.traps() knows them; build_brief.py confirmed each id below on 2026-10-14). Q205 needs a trap id on at least half "
             "of all wrong options of the chapter; reuse is allowed."),
    "ids": {
        "aurora-trap-dynamodb-for-joins": "DynamoDB as the answer for complex joins and ad hoc SQL (27)",
        "aurora-trap-cache-as-database": "a cache as the only store of durable data (27)",
        "aurora-trap-global-all-regions-write": "every Region of an Aurora global database accepts writes (27)",
        "lambda-trap-connection-per-invocation": "a new database connection per invocation is fine at scale (18)",
        "vpc-trap-s3-needs-nat": "private subnets need a NAT gateway to reach S3 (and, by the same belief, DynamoDB) (10)",
        "vpc-trap-endpoint-types-alike": "gateway and interface endpoints are interchangeable (10)",
        "how-the-exam-asks-trap-eventually-means-maybe": "'eventually consistent' means the data may never arrive (01)",
        "how-the-exam-asks-trap-keyword-bait": "an option that repeats a stem keyword ('serverless') must be right (01)",
        "how-the-exam-asks-trap-cheapest-wins": "the cheapest option wins even when it misses a requirement (01)",
        "kms-trap-aws-managed-key-controllable": "you can manage or rotate an AWS managed key yourself (06)",
        "rds-trap-restore-overwrites-instance": "a restore overwrites the running database (26)",
    },
}

BRIEF["compare_tables"] = [
    {"title": "DynamoDB, Aurora or RDS", "section": "1-fast.md#choose-it-or-not", "h3_section_id": "dynamodb-aurora-or-rds",
     "neighbours": ["Amazon DynamoDB", "Amazon Aurora", "Amazon RDS"],
     "rows": ("Columns: Question | DynamoDB | Aurora | RDS. Data model: [Key-value] (dynamodb-decision-guide-key-value-session-store) "
              "and document | relational, with [complex queries through joins] (dynamodb-decision-guide-aurora-relational-joins) | "
              "relational, with [full SQL support] (dynamodb-decision-guide-rds-full-sql). Joins: none: DynamoDB [doesn't support a "
              "JOIN operator] (dynamodb-no-join-operator) | yes | yes. What you pay for (cut first if over budget): each request in "
              "on-demand mode, [billed per read or write request] (dynamodb-ondemand-billed-per-request-zero-traffic-free) | the DB "
              "instances you run (plain words, no link) | the DB instances you run. Three rows."),
     "deciding_question": "Are the access patterns known key lookups at any scale, or does the data need joins and ad hoc SQL?"},
    {"title": "On-demand or provisioned capacity", "section": "1-fast.md#choose-it-or-not", "h3_section_id": "on-demand-or-provisioned-capacity",
     "neighbours": ["on-demand capacity mode", "provisioned capacity mode"],
     "rows": ("Columns: Question | On-demand | Provisioned (3 columns). Fits: traffic it can [handle fluctuating traffic] "
              "(dynamodb-ondemand-better-for-fluctuating-traffic) for: unpredictable and spiky; write the cell as 'unknown or spiky "
              "traffic: it can [handle fluctuating traffic]' | [steady workloads with predictable growth] "
              "(dynamodb-provisioned-fits-steady-forecastable). You pay for: each request: [billed per read or write request] "
              "(dynamodb-ondemand-billed-per-request-zero-traffic-free) | the [hourly read and write capacity you have provisioned] "
              "(dynamodb-provisioned-billing-basis). Long-term discount: none: reserved capacity is not available [or on-demand "
              "capacity mode] (dynamodb-reserved-capacity-not-for-ia-on-demand) | reserved capacity, [up to 54% off standard rates "
              "for a one-year term] (dynamodb-reserved-capacity-terms-and-discount). Three rows; Recap 1 asks for row 2."),
     "deciding_question": "Can you forecast the reads and writes per second well enough to pay for them in advance?"},
    {"title": "Global or local secondary index", "section": "1-fast.md#choose-it-or-not", "h3_section_id": "global-or-local-secondary-index",
     "neighbours": ["global secondary index", "local secondary index"],
     "rows": ("Columns: Question | Global secondary index | Local secondary index (3 columns). Key: any new key: its [index key "
              "schema can be different] (dynamodb-gsi-key-schema-can-differ) | the [same partition key as the base table] "
              "(dynamodb-lsi-same-partition-key), another sort key. When you can add it: any time: you can [add a new global "
              "secondary index] (dynamodb-index-online-operations-gsi-vs-lsi) | only at creation: it is [created when the table is "
              "created] (dynamodb-lsi-created-with-table). Strongly consistent reads: no: queries [support eventual consistency only] "
              "(dynamodb-index-read-consistency-gsi-vs-lsi) | yes: [either eventual consistency or strong consistency] "
              "(dynamodb-index-read-consistency-gsi-vs-lsi). Three rows."),
     "deciding_question": "Does the new query need a different partition key, or the same key with another sort order and strong reads?"},
    {"title": "DAX or ElastiCache", "section": "1-fast.md#choose-it-or-not", "h3_section_id": "dax-or-elasticache",
     "neighbours": ["Amazon DynamoDB Accelerator (DAX)", "Amazon ElastiCache"],
     "rows": ("Columns: Question | DAX | ElastiCache (3 columns). What it caches: DynamoDB reads only; DAX is [API-compatible with "
              "DynamoDB] (dax-api-compatible-minimal-changes) | many sources: a [front-end caching layer] "
              "(elasticache-faq-front-end-cache-for-rds-aurora-documentdb-dynamodb) for RDS, Aurora and DynamoDB. Code change: [only "
              "minimal functional changes] (dax-api-compatible-minimal-changes) | your code reads and fills the cache (plain words; "
              "chapter 29 teaches lazy loading). Data structures (cut first if over budget): items and query results | lists, sets "
              "and hashes: [ElastiCache (Redis OSS) supports advanced data structures] (dax-vs-elasticache-complex-queries). Three "
              "rows."),
     "deciding_question": "Is the cache only for DynamoDB reads, or also for other data and richer data structures?"},
]

BRIEF["signals"] = [
    {"stem": "unpredictable traffic; a new application; pay only per request",
     "think": "on-demand capacity mode", "fact": "dynamodb-ondemand-better-for-fluctuating-traffic",
     "because": "[On-demand capacity mode is the better choice] (dynamodb-ondemand-better-for-fluctuating-traffic) for spiky traffic",
     "but_not_if": "the traffic is steady and forecast for years: provisioned capacity with reserved capacity, for [consistent or predictable traffic] (dynamodb-faq-provisioned-for-predictable)"},
    {"stem": "microsecond reads; the same items read again and again",
     "think": "DAX", "fact": "dax-eventually-consistent-microsecond-latency",
     "because": "it serves [eventually consistent data] (dax-eventually-consistent-microsecond-latency) [with microsecond latency] (dax-eventually-consistent-microsecond-latency)",
     "but_not_if": "reads must be strongly consistent: [DAX passes strongly consistent read requests to DynamoDB] (dax-passes-through-strong-reads-and-transactions)"},
    {"stem": "delete old items automatically; expire sessions; no extra cost",
     "think": "time to live (TTL)", "fact": "dynamodb-faq-ttl-no-write-throughput",
     "because": "it deletes items [without consuming any write throughput] (dynamodb-faq-ttl-no-write-throughput)",
     "but_not_if": "an item must vanish at an exact second: deletion comes [within a few days of their expiration time] (dynamodb-ttl-deletes-within-days-no-wcu); filter on read too"},
    {"stem": "multi-Region, active-active; users write in their own Region",
     "think": "DynamoDB global tables", "fact": "dynamodb-global-table-any-replica-serves-reads-writes",
     "because": "[Any global table replica] (dynamodb-global-table-any-replica-serves-reads-writes) can [serve reads and writes] (dynamodb-global-table-any-replica-serves-reads-writes)",
     "but_not_if": "the data is relational with joins: Aurora Global Database, where [Only the primary cluster performs write operations] (dynamodb-vs-aurora-global-database-single-writer)"},
    {"stem": "run code when an item changes",
     "think": "DynamoDB Streams with a Lambda trigger", "fact": "dynamodb-faq-streams-lambda-triggers",
     "because": "the stream has a [native integration with AWS Lambda] (dynamodb-faq-streams-lambda-triggers)",
     "but_not_if": "changes must be kept or replayed for days: Kinesis Data Streams for DynamoDB, [Up to 1 year] (dynamodb-streams-vs-kds-retention)"},
    {"stem": "query by an attribute that is not the key",
     "think": "a global secondary index", "fact": "dynamodb-gsi-key-schema-can-differ",
     "because": "its [index key schema can be different] (dynamodb-gsi-key-schema-can-differ)",
     "but_not_if": "a new table needs strongly consistent reads on another sort key: an LSI, [created when the table is created] (dynamodb-lsi-created-with-table)"},
    {"stem": "restore to just before an accidental delete",
     "think": "point-in-time recovery (PITR)", "fact": "dynamodb-pitr-protects-accidental-writes-deletes",
     "because": "it protects tables [from accidental write or delete operations] (dynamodb-pitr-protects-accidental-writes-deletes)",
     "but_not_if": "copies must be kept in another account or Region: AWS Backup can [copy backups to multiple AWS accounts] (dynamodb-aws-backup-copy-multiple-accounts-regions)"},
    {"stem": "private subnets reach DynamoDB without a NAT gateway",
     "think": "a gateway endpoint", "fact": "dynamodb-faq-gateway-endpoint-no-igw-nat",
     "because": "it works [without requiring an internet gateway or NAT device] (dynamodb-faq-gateway-endpoint-no-igw-nat)",
     "but_not_if": "requests come from on premises or a peered VPC in another Region: [you must use AWS PrivateLink] (dynamodb-faq-gateway-endpoint-limits-use-privatelink)"},
]

BRIEF["words_table"] = [
    {"term": "partition key", "respelling": None, "collocation": "choose a partition key (bold: choose)", "do_not_confuse": "sort key",
     "bank": "term_request partition-key"},
    {"term": "sort key", "respelling": None, "collocation": "a sort key condition (bold: condition)", "do_not_confuse": "secondary index",
     "bank": "term_request sort-key"},
    {"term": "eventually consistent", "respelling": "ih-VEN-choo-uh-lee", "collocation": "an eventually consistent read (bold: read)",
     "do_not_confuse": "strongly consistent read", "bank": "eventually-consistent (in the bank)"},
    {"term": "read capacity unit", "respelling": None, "collocation": "provision read capacity units (bold: provision)",
     "do_not_confuse": "read request unit (on-demand)", "bank": "term_request read-capacity-unit"},
    {"term": "on-demand capacity mode", "respelling": None, "collocation": "switch a table to on-demand capacity mode (bold: switch)",
     "do_not_confuse": "On-Demand Instance (Amazon EC2)", "bank": "term_request on-demand-capacity-mode"},
    {"term": "global secondary index", "respelling": None, "collocation": "add a global secondary index (bold: add)",
     "do_not_confuse": "local secondary index", "bank": "term_request global-secondary-index"},
    {"term": "global table", "respelling": None, "collocation": "add a replica to a global table (bold: add)",
     "do_not_confuse": "Aurora Global Database", "bank": "term_request global-table"},
    {"term": "time to live", "respelling": None, "collocation": "enable TTL on a table (bold: enable)",
     "do_not_confuse": "deleting with a scheduled job", "bank": "time-to-live (in the bank; term_request adds this DynamoDB collocation and meaning)"},
]

BRIEF["numbers"] = {
    "a_list": [
        {"display": "400 KB", "fact": "dynamodb-item-size-max", "card": "dynamodb-c001",
         "what": "Maximum size of one item, attribute names included", "why": "a larger object goes to Amazon S3 with a pointer in the item"},
        {"display": "3,000 read units per second", "display2": "1,000 write units per second", "fact": "dynamodb-partition-max-throughput",
         "card": "dynamodb-c002", "what": "Ceiling of one partition (link both displays in cell 1)", "why": "explains a hot key that is throttled while the table has spare capacity"},
        {"display": "next 4 KB multiple", "fact": "dynamodb-read-rounding-4kb", "card": "dynamodb-c003",
         "what": "Read size rounding", "why": "decides the read units of an item"},
        {"display": "next 1 KB multiple", "fact": "dynamodb-write-rounding-1kb", "card": "dynamodb-c004",
         "what": "Write size rounding", "why": "decides the write units of an item"},
        {"display": "1 MB per call", "fact": "dynamodb-query-result-1mb", "card": "dynamodb-c005",
         "what": "Most data one Query or Scan call returns", "why": "larger results need paging with LastEvaluatedKey"},
        {"display": "lifetime of 24 hours", "fact": "dynamodb-stream-records-24-hours", "card": "dynamodb-c006",
         "what": "Life of a DynamoDB Streams record", "why": "longer replay needs Kinesis Data Streams for DynamoDB"},
        {"display": "up to 5 local secondary indexes", "fact": "dynamodb-index-limits-20-gsi-5-lsi", "card": "dynamodb-c007",
         "what": "LSIs per table, all defined at creation", "why": "more alternate keys need GSIs"},
        {"display": "10 GB", "fact": "dynamodb-lsi-collection-one-partition", "card": "dynamodb-c008",
         "what": "Largest item collection in a table with an LSI", "why": "a collection that grows past it needs a GSI design"},
    ],
    "b_list": [
        {"display": "up to 20 global secondary indexes", "fact": "dynamodb-index-limits-20-gsi-5-lsi", "what": "GSIs per table (default quota, adjustable)"},
        {"display": "100 unique items", "fact": "dynamodb-transaction-max-items", "what": "Items in one transaction; the data limit is [4 MB] (dynamodb-transaction-max-data)"},
        {"display": "five minutes before the current time", "fact": "dynamodb-pitr-latest-restorable-five-minutes", "what": "Typical latest restore point of PITR"},
        {"display": "between 1 and 35 days", "fact": "dynamodb-change-pitr-configurable-period-2025-01", "what": "PITR recovery period you can set (volatile: B-list only)"},
        {"display": "exceed double your previous peak within 30 minutes", "fact": "dynamodb-on-demand-throttle-if-double-within-30-min", "what": "When an on-demand table can throttle"},
        {"display": "up to four times in a 24-hour rolling window", "fact": "dynamodb-capacity-mode-switch-four-per-24h", "what": "Switches from provisioned to on-demand (volatile, changed 2025-08-12)"},
        {"display": "70%", "fact": "dynamodb-autoscaling-target-recommended", "what": "Recommended auto scaling target utilization"},
        {"display": "two consecutive minutes", "fact": "dynamodb-autoscaling-two-consecutive-minutes", "what": "Breach that starts a scaling action"},
        {"display": "up to five minutes (300 seconds)", "fact": "dynamodb-burst-capacity-retention", "what": "Unused capacity kept as burst capacity"},
        {"display": "99.999%", "fact": "dynamodb-gt-sla-99999-vs-single-region-9999", "what": "Availability SLA of global tables; one Region: [99.99%] (dynamodb-gt-sla-99999-vs-single-region-9999)"},
        {"display": "5 minutes", "fact": "dax-default-ttl-5-minutes-both-caches", "what": "Default TTL of the DAX item cache and query cache"},
        {"display": "Three nodes are required", "fact": "dax-production-three-nodes-three-azs", "what": "Smallest fault-tolerant DAX cluster"},
    ],
    "not_used": [
        "Prices: the pricing examples ($0.25 per GB storage, $0.20 PITR, $0.15 restore, $0.6250 per million replicated writes, DAX $0.12 per hour) are volatile example prices: no row; tasks may use them in cost lines only.",
        "Account quotas (2,500 tables, 80,000 RCU and WCU per account, 40,000 per table): the Look task shows them; no row.",
        "Reserved capacity discounts (54%, 77%) and Database Savings Plans (18%, 35%): subsection 5 names the 54% once; chapter 41 owns discounts.",
        "MRSC numbers (exactly three Regions, 15 Regions) and GSI multi-attribute keys (up to four attributes): volatile; table, Go deeper and Changed recently only.",
        "DAX node counts (11 nodes, 50 nodes per Region, 500 tables): reference only.",
        "Customer case figures (90 percent, 99.999 percent, 1,000 times): the real-world box only.",
    ],
}

BRIEF["changed_recently"] = {
    "fast": [
        {"date": "2024-11-01", "what": "On-demand prices fell; replicated writes of global tables now cost the same as single-Region writes",
         "fact": "dynamodb-change-ondemand-price-cut-2024-11",
         "old_display": "cost effective for spiky workloads", "now_display": "achieve a lower price with on-demand mode",
         "exam_probably_expects": "older questions pick on-demand for spiky or unknown traffic and provisioned for steady traffic; that rule still gives the right answer, so prefer an option that is right under both prices.",
         "status": "examinable",
         "note": "Old: 'on-demand was described as [cost effective for spiky workloads]'. Now: 'most provisioned workloads [achieve a lower price with on-demand mode]'. Volatile fact: never a question key; the capacity-mode questions rest on stable facts."},
        {"date": "2025-08-12", "what": "Switching a table from provisioned to on-demand mode",
         "fact": "dynamodb-change-capacity-mode-switch-limit-2025-08",
         "old_display": "once every 24 hours", "now_display": "four times every 24 hours",
         "exam_probably_expects": "older questions say once a day. Do not let the count decide an answer.",
         "status": "examinable", "note": "Volatile fact: never a question key."},
        {"date": "2025-11-19", "what": "Keys of a global secondary index can combine several attributes",
         "fact": "dynamodb-change-gsi-multi-attribute-keys-2025-11",
         "old_display": "limited to one attribute each", "now_display": "up to four attributes each",
         "exam_probably_expects": "older answers join attributes into one string key; that design still works. Do not let the count decide an answer.",
         "status": "examinable",
         "note": "Replaced by the MRSC entry when its fact request is filled (pending)."},
    ],
    "pending": [
        {"date": "2025-06-30", "what": "Global tables can use multi-Region strong consistency (MRSC)",
         "fact": "dynamodb-change-mrsc-global-tables-ga-2025-06",
         "old_display": "not available. (new mode: write the fixed text)", "now_display": "June 30, 2025 (date) and [Recovery Point Objective (RPO) of zero] for the value",
         "exam_probably_expects": "older questions assume that global tables are always eventually consistent across Regions; that is still the default (MREC).",
         "status": "examinable (2025-06-30 is before the cut-off 2026-07-15)",
         "pending": ("fact request fr-0101, filed by brief-28 (fact_requests): the fact has no changed record, so L107 cannot check the date. "
                     "Write the entry only when the request is filled; it then replaces the GSI-keys entry. If it is closed as "
                     "unfillable, MRSC appears only in the subsection 13 table.")},
    ],
    "considered_not_used": [
        {"fact": "dynamodb-change-tables-per-account-256-to-2500", "why": "the change is dated 2022-03-09, before mid-2022 (RULINGS rule 7): no entry; the Look task shows the current quota"},
        {"fact": "dynamodb-change-fullaccess-v2-managed-policy-2025-04", "why": "an IAM managed-policy rename; no exam answer depends on it"},
        {"fact": "dynamodb-change-pitr-configurable-period-2025-01", "why": "no changed record; the default stays 35 days; the B-list row and the subsection 12 Go deeper carry it"},
        {"fact": "dynamodb-change-warm-throughput-2024-11", "why": "no changed record; warm throughput is current truth in subsection 4"},
        {"fact": "dynamodb-change-ondemand-max-throughput-2024-05", "why": "no changed record; current truth in the subsection 4 table"},
        {"fact": "dynamodb-change-resource-based-policies-2024-03", "why": "no changed record; subsection 14 extras"},
        {"fact": "dynamodb-change-privatelink-interface-endpoints-2024-03", "why": "no changed record; interface endpoints are current truth in subsection 14"},
        {"fact": "dynamodb-change-abac-tables-2024-11", "why": "no changed record; ABAC is reference only"},
        {"fact": "dynamodb-change-abac-streams-2026-08", "why": "after the cut-off (not examinable yet) and no changed record, so a B-list entry cannot pass L107"},
        {"fact": "dynamodb-change-filtered-export-to-s3-2026-10", "why": "after the cut-off and no changed record"},
        {"fact": "dynamodb-change-mrsc-more-regions-2026-09", "why": "after the cut-off and no changed record"},
        {"fact": "dynamodb-change-resource-control-policies-2026-02", "why": "organization policy; chapter 04 owns RCPs"},
        {"fact": "dynamodb-change-throttling-diagnostics-2025-08", "why": "monitoring detail; no answer depends on it"},
        {"fact": "dynamodb-change-ipv6-support-2025-10", "why": "no answer depends on it"},
        {"fact": "dax-change-privatelink-2025-10", "why": "DAX management API detail"},
        {"fact": "dax-change-r7i-instances-2025-04", "why": "instance type detail"},
    ],
}

FAQ_URL = "https://aws.amazon.com/dynamodb/faqs/"
BRIEF["faq"] = [
    {"n": 1, "q": "Can one global table have two replica tables in the same Region?", "fact": "dynamodb-faq-global-table-one-replica-per-region",
     "answer": "No; a global table has [one replica table per AWS Region] (dynamodb-faq-global-table-one-replica-per-region)", "url": FAQ_URL,
     "quote": "A single Amazon DynamoDB global table can only have one replica table per AWS Region."},
    {"n": 2, "q": "Does a global table need a database failover when a Region fails?", "fact": "dynamodb-faq-global-tables-no-failover-needed",
     "answer": "No; it has [no primary Region] (dynamodb-faq-global-tables-no-failover-needed), so you send traffic to another Region", "url": FAQ_URL,
     "quote": "A global table has no primary Region, and thus no database failover is required when directing read and write traffic to a different Region."},
    {"n": 3, "q": "Can you store large images inside DynamoDB items?", "fact": "dynamodb-faq-blob-use-s3-pointers",
     "answer": "You can store binary data, but the better pattern is to [store pointers to Amazon S3 objects] (dynamodb-faq-blob-use-s3-pointers)", "url": FAQ_URL,
     "quote": "Yes, DynamoDB can store BLOB; however, it is not generally suited to storing documents or images. A better architectural pattern is to store pointers to Amazon S3 objects in a DynamoDB table."},
    {"n": 4, "q": "Does a time to live (TTL) delete use write capacity?", "fact": "dynamodb-faq-ttl-no-write-throughput",
     "answer": "No; DynamoDB deletes the item [without consuming any write throughput] (dynamodb-faq-ttl-no-write-throughput)", "url": FAQ_URL,
     "quote": "With TTL, you can define a per-item timestamp to determine when an item is no longer needed, and DynamoDB automatically deletes the item from your table without consuming any write throughput."},
    {"n": 5, "q": "Does DynamoDB delete old data by itself?", "fact": "dynamodb-faq-data-retention-indefinite",
     "answer": "No; data will [remain in the table indefinitely] (dynamodb-faq-data-retention-indefinite) unless you or TTL delete it", "url": FAQ_URL,
     "quote": "There is no set expiration or deletion time for data stored in an Amazon DynamoDB table by default."},
    {"n": 6, "q": "Can you query on attributes that are not part of the primary key?", "fact": "dynamodb-faq-query-nonkey-via-gsi-lsi",
     "answer": "Yes, through [global secondary indexes and local secondary indexes] (dynamodb-faq-query-nonkey-via-gsi-lsi)", "url": FAQ_URL,
     "quote": "DynamoDB also provides flexible querying by letting you query on nonprimary key attributes using global secondary indexes and local secondary indexes."},
    {"n": 7, "q": "Does Kinesis Data Streams for DynamoDB keep record order and remove duplicates?", "fact": "dynamodb-faq-kinesis-no-ordering-dedup",
     "answer": "No; it [does not provide record ordering nor deduplication guarantees] (dynamodb-faq-kinesis-no-ordering-dedup); DynamoDB Streams does", "url": FAQ_URL,
     "quote": "Unlike DynamoDB Streams, Kinesis Data Streams for DynamoDB does not provide record ordering nor deduplication guarantees."},
    {"n": 8, "q": "Can a VPC reach DynamoDB without an internet gateway or a NAT device?", "fact": "dynamodb-faq-gateway-endpoint-no-igw-nat",
     "answer": "Yes, through a gateway endpoint, [without requiring an internet gateway or NAT device] (dynamodb-faq-gateway-endpoint-no-igw-nat)", "url": FAQ_URL,
     "quote": "With a gateway endpoint, you can access DynamoDB from your VPC, without requiring an internet gateway or NAT device for your VPC."},
    {"n": 9, "q": "Can on-premises servers use a DynamoDB gateway endpoint?", "fact": "dynamodb-faq-gateway-endpoint-limits-use-privatelink",
     "answer": "No; for on-premises access [you must use AWS PrivateLink] (dynamodb-faq-gateway-endpoint-limits-use-privatelink)", "url": FAQ_URL,
     "quote": "However, gateway endpoints do not allow access from on-premises networks, from peered VPCs in other AWS Regions, or through a transit gateway."},
    {"n": 10, "q": "Can you switch a table between the Standard and Standard-IA table classes?", "fact": "dynamodb-faq-table-class-switch-twice-30-days",
     "answer": "Yes, [twice in a 30-day period] (dynamodb-faq-table-class-switch-twice-30-days), without downtime", "url": FAQ_URL,
     "quote": "You can switch between these table classes twice in a 30-day period without downtime, allowing you to optimize your costs based on your table's usage patterns."},
]
BRIEF["faq_alternates"] = ["dynamodb-faq-max-item-size-400-kb", "dynamodb-faq-global-tables-pitr-per-replica", "dynamodb-faq-streams-24-hour-log",
                           "dynamodb-faq-block-public-access-always-on", "dynamodb-faq-resource-policy-covers-indexes",
                           "dynamodb-faq-all-data-encrypted-transit-rest"]
BRIEF["faq_note"] = (
    "Each quote block holds whole sentences of the evidence quote of the item's fact, copied exactly (F2, L306); the 'quote' field of "
    "each item is that text, checked by build_brief.py against the stored evidence. All quotes are on the Amazon DynamoDB FAQs page "
    "(https://aws.amazon.com/dynamodb/faqs/); the link line under each quote is '— [Amazon DynamoDB FAQs](https://aws.amazon.com/dynamodb/faqs/)'. "
    "If the section runs over 430 words, replace item 3 (the longest quote) with dynamodb-faq-max-item-size-400-kb (quote: 'The "
    "maximum size of an item that can be stored in a DynamoDB table is 400 KB.'). Item 5's short answer may name TTL only as 'or "
    "TTL deletes it', because the quote is only its first sentence. Item 9's quote begins with 'However,': keep it, it is part of "
    "the sentence.")

BRIEF["story"] = {
    "stage": 2, "month": 13,
    "trigger": "On launch day, each call's status row in PostgreSQL is updated 12 times. Row locks and 900 connections stop the database.",
    "problem": ("Each call has one job record that the pipeline updates about 12 times. Writes are spiky, from 2 calls a minute at "
                "night to 40 at peak. The pipeline reads and writes by call ID and lists one customer's jobs by time. The pipeline "
                "needs no joins."),
    "uses_numbers": ["job_updates_per_call", "peak_uploads_per_minute", "night_uploads_per_minute", "job_record_ttl_days", "launch_day_incident"],
    "state_at_month_13": ("Stage 2, story order 15 (month 13, after chapter 32 in the same month and before 23 and 29). Before this "
                          "chapter: pipeline state P2 (S3 event, uploads queue, start-job function, convert queue, conversion "
                          "workers, a chain of functions for Amazon Transcribe and Amazon Comprehend, save-results, the "
                          "transcript-ready topic) with job status in PostgreSQL through Amazon RDS Proxy (31, 18, 26); the state "
                          "machine call-pipeline (32, same month, earlier in story order). After: P3, job state in the DynamoDB table "
                          "jobs. Not yet: ElastiCache (29, later in month 13), Amazon EFS (23), a second Region (40, stage 4), "
                          "AWS Backup (24, month 22)."),
    "rules": ("Question stems never name Callvale. The story never teaches a fact. No dollar amounts in story text. Ben's question "
              "is the speak item dynamodb-s01. W903: in the Startup example callouts and the Decision record, write digits only for "
              "numbers of uses_numbers: 12 (updates per call), 2 and 40 (calls a minute at night and at peak, stage 2), 90 (days "
              "until a job record is deleted), 900 (database connections on launch day), 47 (minutes of the launch-day failure). "
              "Write AZ labels only in diagrams; this chapter's story diagrams need none."),
}

BRIEF["decision_record"] = {
    "status": "write",
    "context": ("The trigger and the problem of data/startup.json chapter 28, at most 80 words, stage 2: 'On launch day, each call's "
                "status row in PostgreSQL was updated 12 times. Row locks and 900 connections stopped the database. Writes swing "
                "from 2 calls a minute at night to 40 at peak. The pipeline reads and writes one job by call ID and lists one "
                "customer's jobs by time. It needs no joins.' (about 55 words)."),
    "requirement": ("Job state must take spiky writes and simple key lookups, and old jobs must disappear, with the LEAST "
                    "operational overhead (qualifier of the JSON: least operational overhead)."),
    "requirement_qualifier": "least operational overhead",
    "options": ["a larger PostgreSQL instance for the job rows", "Amazon DynamoDB with on-demand capacity (chosen)", "Amazon ElastiCache for job state"],
    "decision": ("A DynamoDB table, jobs, with on-demand capacity and one global secondary index (data/startup.json choice). The "
                 "global secondary index by-customer lists one customer's jobs by time, and time to live deletes each job record 90 "
                 "days after the call (data/startup.json adds and note)."),
    "reasons_with_facts": [
        "Option 1 keeps the bottleneck: functions open connections to a relational server, while [DynamoDB uses an HTTP API] (lambda-ddb-http-api-no-connections) and needs none; a larger instance still holds every row lock in one place.",
        "Option 3 risks the data: ElastiCache is an [ephemeral cache for frequently accessed data] (dynamodb-decision-guide-elasticache-caching-layer), and relying on cached data [as if it is durably stored] (dynamodb-wa-cache-not-durable-store) is an anti-pattern; job state must survive.",
        "Option 2: on-demand mode can [handle fluctuating traffic] (dynamodb-ondemand-better-for-fluctuating-traffic) with no capacity to set; reads and writes by call ID are key lookups; the GSI gives the second access pattern because its [index key schema can be different] (dynamodb-gsi-key-schema-can-differ); TTL deletes old jobs [without consuming any write throughput] (dynamodb-faq-ttl-no-write-throughput).",
    ],
    "tradeoff": ("Access patterns must be known first. A new query can need a new index, and there are no SQL joins (data/startup.json "
                 "tradeoff, word for word). Optional link on the last clause: DynamoDB [doesn't support a JOIN operator] "
                 "(dynamodb-no-join-operator)."),
    "later": ("One sentence at most: at stage 4, a replica table in US West (Oregon) makes jobs a global table (chapter 40), and the "
              "table moves to provisioned capacity with auto scaling after the cost review (chapter 41). No new option in the record."),
    "spot_the_bug": None,
    "diagrams": ["dynamodb-before", "dynamodb-after"],
}

BRIEF["realworld"] = {
    "status": "optional", "company": "Genesys", "year": 2024,
    "facts": ["dynamodb-case-genesys-on-demand-unpredictable-workloads", "dynamodb-case-genesys-99-999-availability-global-tables",
              "dynamodb-case-genesys-dynamodb-standard-no-maintenance-windows"],
    "point": ("**Genesys, 2024.** in bold (the year comes from the fact dynamodb-case-genesys-99-999-availability-global-tables: '12 "
              "months ending July 31, 2024'). Genesys, a contact-center software company, runs Genesys Cloud on DynamoDB and reports "
              "[99.999 percent availability for the 12 months ending July 31, 2024] (dynamodb-case-genesys-99-999-availability-global-tables), "
              "with [DynamoDB global tables to automatically replicate data] (dynamodb-case-genesys-99-999-availability-global-tables). "
              "One AWS quote block of one whole sentence (17 words): \"Additionally, Genesys Cloud can handle unpredictable workloads "
              "efficiently using the on-demand capacity mode in Amazon DynamoDB.\" "
              "(https://aws.amazon.com/solutions/case-studies/genesys-dynamodb-case-study/). It shows: on-demand capacity for "
              "unpredictable load and global tables for multi-Region availability. Then a two-sentence Say it. At most 100 words. "
              "Never part of Callvale's story; the reported availability is the customer's result, not a DynamoDB SLA."),
    "rule": "Write it only if 2-deep.md stays at or under 4,390 words without it. It is not in the sections list, so leaving it out is no L905 error.",
}

BRIEF["devices"] = {
    "exam_trap_callouts_2_deep": {
        "read-and-write-units-depend-on-item-size-and-read-consistency": "dynamodb-trap-gsi-strong-read",
        "on-demand-mode-bills-each-request-and-needs-no-capacity-plan": "dynamodb-trap-on-demand-absorbs-any-spike",
        "provisioned-mode-bills-the-capacity-you-set-and-auto-scaling-follows-within-minutes": "dynamodb-trap-auto-scaling-prevents-throttling",
        "a-query-reads-one-partition-key-but-a-scan-reads-every-item": "dynamodb-trap-filter-saves-capacity",
        "secondary-indexes-give-the-same-items-a-second-key-to-query": "dynamodb-trap-lsi-added-later",
        "conditional-writes-and-transactions-stop-one-write-from-overwriting-another": "dynamodb-trap-batch-write-is-atomic",
        "dynamodb-streams-records-each-item-change-in-order-for-24-hours": "dynamodb-trap-stream-keeps-changes",
        "every-restore-from-a-backup-or-a-point-in-time-creates-a-new-table": "dynamodb-trap-restore-in-place",
    },
    "exam_trap_form": "> **Exam trap:** <wrong belief in plain words>. <truth with its fact link>. <!-- trap: <id> -->  Each one adds a new case; never restate the table above it. The plans give ready texts (exam_trap_text).",
    "fast_traps_list": ["dynamodb-trap-spare-capacity-no-throttle", "dynamodb-trap-default-read-is-latest", "dynamodb-trap-ttl-deletes-on-time",
                        "dynamodb-trap-dax-speeds-every-read", "dynamodb-trap-global-table-primary-region"],
    "fast_traps_links": ("Each fast trap item links one fact in its Truth part: spare-capacity-no-throttle [1,000 write units per "
                         "second] (dynamodb-partition-max-throughput) for one partition; default-read-is-latest [Eventually consistent "
                         "is the default] (dynamodb-eventually-consistent-default); ttl-deletes-on-time [within a few days of their "
                         "expiration time] (dynamodb-ttl-deletes-within-days-no-wcu); dax-speeds-every-read [DAX passes strongly "
                         "consistent read requests to DynamoDB] (dax-passes-through-strong-reads-and-transactions); "
                         "global-table-primary-region [no primary Region] (dynamodb-faq-global-tables-no-failover-needed)."),
    "go_deeper": [
        "a-hash-of-the-partition-key-picks-the-partition-so-hot-keys-throttle: adaptive and burst capacity",
        "provisioned-mode-bills-the-capacity-you-set-and-auto-scaling-follows-within-minutes: reserved capacity and the 35% rule",
        "a-query-reads-one-partition-key-but-a-scan-reads-every-item: big scans without hurting the application",
        "secondary-indexes-give-the-same-items-a-second-key-to-query: sparse indexes and back-pressure",
        "every-restore-from-a-backup-or-a-point-in-time-creates-a-new-table: deleted tables, exports and the recovery period",
        "in-a-global-table-every-replica-accepts-reads-and-writes: what does not cross Regions",
    ],
    "spot_the_bug": [
        "time-to-live-deletes-expired-items-without-using-write-capacity: the TTL attribute written as text",
        "iam-controls-access-and-every-table-is-encrypted-at-rest: DynamoDB traffic through a NAT gateway",
    ],
    "try_it": [
        "a-query-reads-one-partition-key-but-a-scan-reads-every-item: dynamodb-t02",
        "conditional-writes-and-transactions-stop-one-write-from-overwriting-another: dynamodb-t03",
    ],
    "startup_example_2_deep": ["on-demand-mode-bills-each-request-and-needs-no-capacity-plan: the night and peak write rates and on-demand mode"],
    "predict_the_picture": "In one breath: 'When an application writes one item, where does DynamoDB store it, and when does it say the write is safe?' before the hero dynamodb-hero (LEARNING device 6).",
    "route_pass_subsections": [
        "a-hash-of-the-partition-key-picks-the-partition-so-hot-keys-throttle",
        "on-demand-mode-bills-each-request-and-needs-no-capacity-plan",
        "secondary-indexes-give-the-same-items-a-second-key-to-query",
        "in-a-global-table-every-replica-accepts-reads-and-writes",
    ],
    "route_pass_note": ("Four of the maximum four (section_flag.h3_pass_route_subsections). The reader marked DynamoDB global tables "
                        "as 'right but not sure' in her diagnostic, so subsection 13 is on the pass route."),
    "xref_markers": [
        "02 AWS map (Regions and Availability Zones)",
        "06 KMS (AWS owned, AWS managed and customer managed keys)",
        "10 VPC (gateway endpoints, NAT gateways)",
        "11 VPC connectivity (interface endpoints, AWS PrivateLink)",
        "18 Lambda (event source mappings for streams; connections from many functions)",
        "24 AWS Backup (backup plans, Vault Lock, cross-account copies)",
        "26 RDS and 27 Aurora (relational choice; Aurora Global Database)",
        "29 ElastiCache (caching strategies, lazy loading)",
        "31 Messaging (Kinesis Data Streams)",
        "40 HA and DR (RPO and RTO per strategy)",
        "41 Cost optimization (reserved capacity, Savings Plans)",
    ],
}
