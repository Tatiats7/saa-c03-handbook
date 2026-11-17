# brief-28, part E: the 22 question slots and the question plan.

SEC = {s["heading"]: "2-deep.md#" + s["section"] for s in BRIEF["sections"] if s["file"] == "2-deep.md"}


def sec(prefix):
    for h, v in SEC.items():
        if h.startswith(prefix):
            return v
    raise KeyError(prefix)


Q = BRIEF["question_slots"] = []


def slot(**k):
    k["id"] = "q%02d" % (len(Q) + 1)
    Q.append(k)


# ---------------------------------------------------------------- core (q01 to q11)
slot(bullet="4.3.S3", concept="on-demand-for-unpredictable-traffic", difficulty=2, type="single", layer="core",
     exam_english=["ee-most-cost-effective", "ee-unpredictable", "ee-spiky"], section=sec("On-demand mode"),
     trap="dynamodb-trap-auto-scaling-prevents-throttling", distractor_traps=[], twin="first of strict twin pair A (twin q07)",
     key_facts=["dynamodb-ondemand-better-for-fluctuating-traffic", "dynamodb-faq-on-demand-for-unpredictable",
                "dynamodb-throttling-with-autoscaling-possible", "dynamodb-ondemand-billed-per-request-zero-traffic-free"],
     note=("Shared stem: a company stores order data in a DynamoDB table in provisioned capacity mode with auto scaling. The "
           "company wants to keep reads and writes from being throttled and to lower the table's cost. Changed phrase: 'Traffic is "
           "unpredictable: it stays near zero for hours, then rises to many times the usual level within minutes.' Ask: 'Which "
           "solution meets these requirements MOST cost-effectively?' Key: (A) Switch the table to on-demand capacity mode "
           "([On-demand capacity mode is the better choice] (dynamodb-ondemand-better-for-fluctuating-traffic); [billed per read or "
           "write request] (dynamodb-ondemand-billed-per-request-zero-traffic-free)). Options identical in q07: (A) as above; (B) "
           "Keep provisioned capacity with auto scaling, and buy reserved capacity for the base load; (C) Put a DynamoDB Accelerator "
           "(DAX) cluster in front of the table; (D) Set the provisioned capacity to the highest peak ever measured and keep it "
           "there. In q01, (B) carries the trap dynamodb-trap-auto-scaling-prevents-throttling (why links [does not respond "
           "instantly] (dynamodb-throttling-with-autoscaling-possible)); (C) is misconception: DAX caches reads and [DAX benefits "
           "might be limited] (dax-write-heavy-limited-benefit) for writes; (D) violates-qualifier (pays for the peak all day: "
           "[hourly read and write capacity you have provisioned] (dynamodb-provisioned-billing-basis)). Write option texts in "
           "neutral words that fit both stems. Do not use the volatile 2024-11-01 price change in any why."))
slot(bullet="3.3.K3", concept="hot-partition-key-design", difficulty=2, type="single", layer="core",
     exam_english=["ee-best", "ee-scalable"], section=sec("A hash of the partition key"),
     trap="dynamodb-trap-spare-capacity-no-throttle", distractor_traps=["how-the-exam-asks-trap-keyword-bait"],
     worked="worked think-aloud, no wrong path",
     key_facts=["dynamodb-partition-max-throughput", "dynamodb-hot-partitions-throttle-while-others-underutilized",
                "dynamodb-few-partition-keys-spread-writes", "dynamodb-write-sharding-random-suffix"],
     note=("A company stores votes in a DynamoDB table in provisioned mode. The partition key is the contest ID, and during a final "
           "almost every vote is for one contest. CloudWatch shows that consumed write capacity is far below the table's provisioned "
           "write capacity, but many writes are throttled. Which solution will BEST resolve the throttling? Key: spread the writes "
           "for the hot contest over several partition key values by adding a random suffix (write sharding), and sum the shards "
           "when reading ([add a random number] (dynamodb-write-sharding-random-suffix); spread the writes [across more distinct "
           "partition key values] (dynamodb-few-partition-keys-spread-writes)). Distractors: raise the table's provisioned write capacity (trap "
           "dynamodb-trap-spare-capacity-no-throttle; why links [1,000 write units per second] (dynamodb-partition-max-throughput)); "
           "switch the table to on-demand capacity mode (misconception: on-demand does not raise the per-partition ceiling; why "
           "links [throttling while other operations may remain underutilized] (dynamodb-hot-partitions-throttle-while-others-underutilized) "
           "and states that the partition ceiling applies to every partition; the claims reviewer checks this wording); add a DAX "
           "cluster (violates-requirement: DAX helps reads, [DAX benefits might be limited] (dax-write-heavy-limited-benefit) for "
           "writes). Worked think-aloud: find the constraint (one hot key, spare table capacity), predict, eliminate, choose."))
slot(bullet="3.3.S2", concept="strongly-consistent-read-after-write", difficulty=1, type="single", layer="core",
     exam_english=["ee-must"], section=sec("Read and write units"),
     trap="dynamodb-trap-default-read-is-latest", distractor_traps=["dynamodb-trap-gsi-strong-read", "dynamodb-trap-dax-speeds-every-read"],
     key_facts=["dynamodb-eventually-consistent-default", "dynamodb-eventually-consistent-may-lag", "dynamodb-consistentread-parameter"],
     note=("Difficulty 1, qualifier none (no violates-qualifier option). An application writes an order item to a DynamoDB table and "
           "reads it back at once with GetItem. Sometimes the read returns the old version. The read must always return the result "
           "of every earlier successful write. What should a solutions architect do? Key: set ConsistentRead to true on the GetItem call "
           "([optional `ConsistentRead` parameter] (dynamodb-consistentread-parameter); [most up-to-date data] "
           "(dynamodb-consistentread-parameter)). Distractors: read the order from a global secondary index with a strongly "
           "consistent query (trap dynamodb-trap-gsi-strong-read; why links [support eventual consistency only] "
           "(dynamodb-index-read-consistency-gsi-vs-lsi)); add DAX so that reads come from memory (trap "
           "dynamodb-trap-dax-speeds-every-read; why links [DAX passes strongly consistent read requests to DynamoDB] "
           "(dax-passes-through-strong-reads-and-transactions) and [eventually consistent data] "
           "(dax-eventually-consistent-microsecond-latency)); enable DynamoDB Streams on the table (misconception: a stream feeds "
           "other consumers; reads from streams are eventually consistent: [reads from GSIs and streams are eventually consistent] "
           "(dynamodb-gsi-and-streams-reads-eventual))."))
slot(bullet="3.3.K3", concept="gsi-for-new-access-pattern-existing-table", difficulty=2, type="single", layer="core",
     exam_english=["ee-least-operational-overhead", "ee-currently", "ee-eventually"], section=sec("Secondary indexes"),
     trap="dynamodb-trap-lsi-added-later", distractor_traps=["dynamodb-trap-filter-saves-capacity"],
     twin="first of strict twin pair B (twin q10)",
     key_facts=["dynamodb-index-online-operations-gsi-vs-lsi", "dynamodb-gsi-key-schema-can-differ", "dynamodb-gsi-add-to-existing-table"],
     note=("Shared stem: a company's DynamoDB table orders has the partition key CustomerId and the sort key OrderDate. A new screen "
           "must list one customer's orders sorted by OrderTotal. Changed phrase: 'The table currently holds two years of orders, "
           "and eventually consistent reads are acceptable for the new screen.' Ask: 'Which solution meets these requirements with "
           "the LEAST operational overhead?' Key: (A) Add a global secondary index with the partition key CustomerId and the sort "
           "key OrderTotal, and query it ([add a new global secondary index] (dynamodb-index-online-operations-gsi-vs-lsi); [the "
           "table continues to be available] (dynamodb-gsi-add-to-existing-table)). Options identical in q10: (A) as above; (B) "
           "Define a local secondary index with the sort key OrderTotal; (C) Scan the table with a filter expression on CustomerId, "
           "and sort the results in the application; (D) Copy each order into a second table keyed by CustomerId and OrderTotal "
           "with a Lambda function on the table's stream. In q04, (B) carries dynamodb-trap-lsi-added-later (why links [cannot add "
           "a local secondary index] (dynamodb-index-online-operations-gsi-vs-lsi)); (C) carries dynamodb-trap-filter-saves-capacity "
           "and is violates-qualifier; (D) violates-qualifier (code to run). Neutral option wording for both stems."))
slot(bullet="3.3.K4", concept="reduce-read-capacity-of-report-job", difficulty=2, type="multi", layer="core",
     exam_english=["ee-most-cost-effective", "ee-select-two", "ee-mission-critical"], section=sec("A Query reads"),
     trap="dynamodb-trap-filter-saves-capacity", distractor_traps=[],
     key_facts=["dynamodb-sparse-index-faster-cheaper-than-scan", "dynamodb-gsi-only-items-with-key-attributes",
                "dynamodb-eventually-consistent-half-cost", "dynamodb-scan-filter-same-read-capacity"],
     note=("Select TWO, five options. A nightly report job Scans a large provisioned DynamoDB table with strongly consistent reads and "
           "a filter expression that keeps only orders whose status is OPEN; a few hundred of millions of orders are open. The scan "
           "consumes most of the read capacity, and the mission-critical order API is throttled during the job. Which TWO actions "
           "will reduce the read capacity the job consumes MOST cost-effectively? (Select TWO.) Keys: add an attribute that only "
           "open orders carry, index it in a sparse global secondary index, and Query the index ([only tracks data items] "
           "(dynamodb-gsi-only-items-with-key-attributes); [faster and less expensive to query that index] "
           "(dynamodb-sparse-index-faster-cheaper-than-scan)); use eventually consistent reads, at [half the cost of strongly "
           "consistent reads] (dynamodb-eventually-consistent-half-cost). Distractors: make the filter expression more selective "
           "(trap dynamodb-trap-filter-saves-capacity; why links [consumes the same amount of read capacity] "
           "(dynamodb-scan-filter-same-read-capacity)); return fewer attributes with a projection expression (misconception: "
           "capacity counts [the number of items and the size] (dynamodb-read-capacity-by-items-read-not-returned), not the data "
           "returned); run a parallel scan with more workers (violates-requirement: it can [consume all of your table's "
           "provisioned read capacity] (dynamodb-parallel-scan-heavy-demand)). 'a few hundred' is an example value; avoid a "
           "number with a unit in the stem."))
slot(bullet="3.3.K2", concept="dax-for-microsecond-repeated-reads", difficulty=2, type="single", layer="core",
     exam_english=["ee-least-development-effort", "ee-without-changing-the-application"], section=sec("DAX answers"),
     trap=None, distractor_traps=["aurora-trap-cache-as-database"],
     key_facts=["dax-api-compatible-minimal-changes", "dax-eventually-consistent-microsecond-latency", "dax-ideal-fastest-reads-hot-keys"],
     note=("A gaming company reads the same small set of player profile items from a DynamoDB table thousands of times a second with "
           "eventually consistent reads. Read latency must drop from milliseconds to microseconds, and the company wants to do this "
           "without changing the application's data access logic. Which solution meets these requirements with the LEAST "
           "development effort? Key: add a DAX cluster and use the DAX client ([API-compatible with DynamoDB] "
           "(dax-api-compatible-minimal-changes); [with microsecond latency] (dax-eventually-consistent-microsecond-latency)). "
           "Distractors: add an ElastiCache cluster and write cache-aside code (violates-qualifier: code changes; chapter 29); "
           "raise the table's read capacity (misconception: more capacity does not change latency from milliseconds to "
           "microseconds; DynamoDB alone gives [single-digit millisecond performance] (dax-modest-needs-use-dynamodb-alone)); move "
           "the profiles into ElastiCache and remove the table (trap aurora-trap-cache-as-database: ElastiCache is an [ephemeral "
           "cache for frequently accessed data] (dynamodb-decision-guide-elasticache-caching-layer))."))
slot(bullet="4.3.S3", concept="on-demand-for-unpredictable-traffic", difficulty=2, type="single", layer="core",
     exam_english=["ee-most-cost-effective", "ee-steady-state", "ee-predictable"], section=sec("Provisioned mode"),
     trap=None, distractor_traps=["dynamodb-trap-auto-scaling-prevents-throttling"], twin="second of strict twin pair A (twin_of q01)",
     key_facts=["dynamodb-provisioned-ideal-steady-predictable-usage", "dynamodb-ondemand-cheaper-below-35-percent-utilization",
                "dynamodb-reserved-capacity-terms-and-discount", "dynamodb-faq-provisioned-for-predictable"],
     note=("Strict twin of q01: same stem, same options, same qualifier (MOST cost-effectively). Changed phrase: 'Traffic is steady "
           "and predictable around the clock, the provisioned capacity is almost fully used all day, and the load will stay at this "
           "level for at least the next 3 years.' Key: (B) Keep provisioned capacity with auto scaling, and buy reserved capacity "
           "for the base load ([more steady and predictable usage pattern] (dynamodb-provisioned-ideal-steady-predictable-usage); "
           "[77% off standard rates for a three-year term] (dynamodb-reserved-capacity-terms-and-discount) only where offered: say "
           "'reserved capacity' without a percentage in the stem and options). In q07, (A) on-demand is violates-qualifier: at high, "
           "steady utilization on-demand is not the cheaper mode; why links [below 35%] "
           "(dynamodb-ondemand-cheaper-below-35-percent-utilization) as the rule of thumb (do not cite the volatile price-cut "
           "fact); (C) DAX misconception as in q01; (D) violates-qualifier (no discount, capacity at the peak). Twin line of each "
           "quotes the other's changed phrase. At least 3 questions stand between q01 and q07."))
slot(bullet="4.3.K5", concept="capacity-unit-calculation", difficulty=1, type="single", layer="core",
     exam_english=["ee-needs-to"], section=sec("Read and write units"),
     trap=None, distractor_traps=["dynamodb-trap-default-read-is-latest"],
     key_facts=["dynamodb-read-capacity-formula", "dynamodb-read-rounding-4kb", "dynamodb-write-capacity-formula", "dynamodb-rcu-definition",
                "dynamodb-wcu-definition"],
     note=("Difficulty 1, qualifier none. A table in provisioned mode stores items of 6 KB. The application needs to make 100 "
           "strongly consistent reads per second and 50 writes per second. How many read capacity units and write capacity units "
           "does the table need? Key: 200 RCUs and 300 WCUs (6 KB rounds up to 8 KB for reads: two units per strongly consistent "
           "read, [divide the item size of the operation by 4 KB] (dynamodb-read-capacity-formula) and [next 4 KB multiple] "
           "(dynamodb-read-rounding-4kb); writes: [divide the item size of the operation by 1 KB] (dynamodb-write-capacity-formula), "
           "six units per write). Distractors: 100 RCUs and 300 WCUs (counts eventually consistent reads; trap "
           "dynamodb-trap-default-read-is-latest is the nearest belief, or leave the distractor with misconception only if the "
           "writer finds the tag does not fit); 200 RCUs and 50 WCUs (one unit per write regardless of size); 150 RCUs and 300 "
           "WCUs (rounds 6 KB to 6 KB for reads). Explanations write the arithmetic in words where a number with a unit has no "
           "display (L304 applies to the explanation: link the formula facts in each sentence that holds a size)."))
slot(bullet="2.2.S5", concept="pitr-restore-to-new-table", difficulty=1, type="single", layer="core",
     exam_english=["ee-point-in-time"], section=sec("Every restore"),
     trap="dynamodb-trap-restore-in-place", distractor_traps=["rds-trap-restore-overwrites-instance"],
     key_facts=["dynamodb-pitr-restores-to-new-table", "dynamodb-pitr-protects-accidental-writes-deletes",
                "dynamodb-restore-cannot-overwrite-existing-table"],
     note=("Difficulty 1, qualifier none. A faulty release deleted many items from a DynamoDB table at 14:05. Point-in-time recovery "
           "is enabled. The company must get the table data back as it was at 14:04. What should a solutions architect do? Key: "
           "restore the table to 14:04 into a new table, then copy the deleted items back or point the application at the new table "
           "([always restores to a new table] (dynamodb-pitr-restores-to-new-table)). Distractors: restore the table to 14:04 over "
           "the existing table (trap dynamodb-trap-restore-in-place; why links [can't overwrite an existing table] "
           "(dynamodb-restore-cannot-overwrite-existing-table)); restore last week's on-demand backup (violates-requirement: loses a "
           "week of data); read the deleted items from the table's DynamoDB stream (misconception: records have a [lifetime of 24 "
           "hours] (dynamodb-stream-records-24-hours) and a stream may not be enabled; keep the option text free of numbers)."))
slot(bullet="3.3.K3", concept="gsi-for-new-access-pattern-existing-table", difficulty=2, type="single", layer="core",
     exam_english=["ee-least-operational-overhead", "ee-currently"], section=sec("Secondary indexes"),
     trap="dynamodb-trap-gsi-strong-read", distractor_traps=["dynamodb-trap-filter-saves-capacity"],
     twin="second of strict twin pair B (twin_of q04)",
     key_facts=["dynamodb-lsi-created-with-table", "dynamodb-lsi-strongly-consistent-allowed", "dynamodb-index-read-consistency-gsi-vs-lsi"],
     note=("Strict twin of q04: same stem, options and qualifier. Changed phrase: 'The table is being created now and holds no data "
           "yet, and the new screen must use strongly consistent reads.' Key: (B) Define a local secondary index with the sort key "
           "OrderTotal ([created when the table is created] (dynamodb-lsi-created-with-table); [either eventually consistent or "
           "strongly consistent reads] (dynamodb-lsi-strongly-consistent-allowed)). In q10, (A) carries dynamodb-trap-gsi-strong-read "
           "(why links [support eventual consistency only] (dynamodb-index-read-consistency-gsi-vs-lsi)); (C) and (D) as in q04. The "
           "word 'currently' in q04 becomes the changed phrase's 'now' here: list ee-currently only in q04 if the word is gone."))
slot(bullet="3.3.S4", concept="dynamodb-for-key-value-sessions", difficulty=2, type="single", layer="core",
     exam_english=["ee-least-operational-overhead", "ee-serverless", "ee-small-team"], section="1-fast.md#choose-it-or-not",
     trap=None, distractor_traps=["how-the-exam-asks-trap-keyword-bait", "lambda-trap-connection-per-invocation", "aurora-trap-cache-as-database"],
     key_facts=["dynamodb-decision-guide-key-value-session-store", "dynamodb-serverless-no-servers", "dynamodb-intro-little-operational-overhead",
                "lambda-ddb-http-api-no-connections"],
     note=("Bullets also 3.3.K8, 4.3.K9. A startup with a small team stores user session data for a mobile app. Each request reads or "
           "writes one session by its session ID; there are no joins, and traffic swings from almost nothing at night to millions "
           "of requests at peak. Lambda functions handle the requests. Which database meets these requirements with the LEAST "
           "operational overhead? Key: Amazon DynamoDB in on-demand mode ([session stores or shopping carts] "
           "(dynamodb-decision-guide-key-value-session-store); [don't need to provision any servers] "
           "(dynamodb-serverless-no-servers); [DynamoDB uses an HTTP API] (lambda-ddb-http-api-no-connections)). Distractors: Amazon "
           "RDS for PostgreSQL with Multi-AZ (violates-qualifier: instances, connections; tag lambda-trap-connection-per-invocation "
           "only if the option says each function opens its own connection); a self-managed NoSQL database on EC2 (violates-qualifier: "
           "AWS says DynamoDB [can reduce operational overhead] (dynamodb-wa-managed-nosql-reduces-overhead) against self-hosting); "
           "Amazon ElastiCache as the only session store (trap aurora-trap-cache-as-database). 'serverless' may appear in the stem "
           "(ee-serverless); the keyword-bait tag fits an option that repeats it wrongly."))

# ---------------------------------------------------------------- extended (q12 to q22)
slot(bullet="2.2.S2", concept="multi-region-recovery-choice", difficulty=2, type="single", layer="extended",
     exam_english=["ee-most-cost-effective", "ee-cross-region", "ee-as-soon-as-possible"], section=sec("In a global table"),
     trap=None, distractor_traps=[],
     twin="first of strict twin pair C (twin q16)",
     key_facts=["dynamodb-dr-global-tables-mrec-rto-zero", "dynamodb-global-table-any-replica-serves-reads-writes",
                "dynamodb-faq-global-table-one-replica-per-region", "dax-same-region-as-tables"],
     note=("Shared stem: a company runs a DynamoDB table in us-east-1 for its order service. The company is planning for the failure "
           "of the whole Region. Changed phrase: 'If us-east-1 becomes unavailable, users must keep reading and writing orders in "
           "us-west-2 within seconds, with no restore step.' Ask: 'Which solution meets these requirements MOST cost-effectively?' "
           "Key: (A) Make the table a global table with a replica table in us-west-2 ([RPO of a few seconds] and [RTO of zero] "
           "(dynamodb-dr-global-tables-mrec-rto-zero); [Any global table replica] can [serve reads and writes] "
           "(dynamodb-global-table-any-replica-serves-reads-writes)). Options identical in q16: (A) as above; (B) Use AWS Backup to "
           "back up the table every hour and copy each backup to us-west-2; (C) Add a second replica table in another Availability "
           "Zone of us-east-1; (D) Create a DAX cluster in us-west-2 that caches the table. In q12, (B) violates-requirement (a "
           "restore takes minutes to hours); (C) is impossible-feature: [one replica table per AWS Region] "
           "(dynamodb-faq-global-table-one-replica-per-region), and the data is already in [three Availability Zones] "
           "(dynamodb-faq-sync-replication-three-azs); (D) impossible-feature: DAX works only with [tables that are in the same "
           "Region] (dax-same-region-as-tables). The explanation may add that no database failover is needed ([no primary Region] "
           "(dynamodb-faq-global-tables-no-failover-needed)). No slot trap: no option of the shared set states a trap belief, and "
           "the options must stay identical in q16."))
slot(bullet="4.3.K4", concept="standard-ia-for-rarely-read-history", difficulty=3, type="single", layer="extended",
     exam_english=["ee-most-cost-effective", "ee-infrequently-accessed", "ee-retain"], section=sec("Time to Live"),
     trap=None, distractor_traps=["how-the-exam-asks-trap-cheapest-wins"],
     key_facts=["dynamodb-table-class-standard-ia-lower-storage-cost", "dynamodb-table-class-standard-vs-ia-50-percent-storage",
                "dynamodb-table-class-standard-ia-same-performance", "dynamodb-table-class-switch-no-code-change"],
     note=("Bullets also 4.3.S3. A company keeps 5 years of order history in a DynamoDB table and must retain all of it, queryable "
           "through the same API. Items older than one month are infrequently accessed. Storage is about 70% of the table's monthly "
           "bill. Which solution will reduce the cost MOST cost-effectively without changing the application? Key: change the "
           "table class to DynamoDB Standard-IA ([storage is the dominant cost] (dynamodb-table-class-standard-ia-lower-storage-cost); "
           "[approximately 50% or more of the overall monthly cost] (dynamodb-table-class-standard-vs-ia-50-percent-storage); "
           "[does not require changing your application code] (dynamodb-table-class-switch-no-code-change); [same performance, "
           "durability, and availability] (dynamodb-table-class-standard-ia-same-performance)). Distractors: enable TTL to delete "
           "items older than one month (violates-requirement: data must be retained; tag how-the-exam-asks-trap-cheapest-wins); "
           "switch to on-demand capacity mode (misconception: changes the request bill, not storage); export old items to Amazon S3 "
           "Glacier and delete them from the table (violates-requirement: no longer queryable through the same API). 5 years, one "
           "month and 70% are stem values; the why links the 50% display."))
slot(bullet="3.3.S2", concept="streams-lambda-on-item-change", difficulty=2, type="single", layer="extended",
     exam_english=["ee-near-real-time", "ee-least-operational-overhead"], section=sec("DynamoDB Streams"),
     trap="dynamodb-trap-stream-keeps-changes", distractor_traps=[],
     key_facts=["dynamodb-streams-lambda-triggers", "dynamodb-faq-streams-lambda-triggers", "dynamodb-streams-time-ordered-changes"],
     note=("A company stores support tickets in a DynamoDB table. When a ticket's status changes to CLOSED, a survey email must be sent "
           "in near real-time. Which solution meets this requirement with the LEAST operational overhead? Key: enable DynamoDB "
           "Streams on the table with the NEW_AND_OLD_IMAGES view and add a Lambda function as a trigger that sends the email when "
           "the status changed ([automatically respond to events in DynamoDB Streams] (dynamodb-streams-lambda-triggers); "
           "[`NEW_AND_OLD_IMAGES`] (dynamodb-streams-view-new-and-old-images)). Distractors: a Lambda function on an EventBridge "
           "schedule that scans the table every minute for closed tickets (violates-qualifier and violates-requirement: delay, "
           "reads); keep the stream records for a weekly batch job that reads them each Sunday (trap "
           "dynamodb-trap-stream-keeps-changes; why links [lifetime of 24 hours] (dynamodb-stream-records-24-hours)); an EC2 "
           "application that reads the stream with the Kinesis Client Library (violates-qualifier: servers to run)."))
slot(bullet="3.3.K8", concept="transaction-with-idempotent-retry", difficulty=3, type="single", layer="extended",
     exam_english=["ee-ensure", "ee-transactional"], section=sec("Conditional writes"),
     trap="dynamodb-trap-batch-write-is-atomic", distractor_traps=[],
     key_facts=["dynamodb-transactwriteitems-all-or-nothing", "dynamodb-transactwriteitems-idempotent-client-token",
                "dynamodb-transactwriteitems-vs-batchwriteitem", "dynamodb-transaction-client-token-10-minutes"],
     note=("Bullets also 3.3.S2. A payments service moves points between two users. The debit of one item and the credit of another "
           "item must both happen or neither. The client sometimes times out and sends the same request again; the transfer must "
           "not be applied twice. Which solution will ensure this with the LEAST development effort? Key: one TransactWriteItems "
           "call with both updates, conditions on the balance, and a client request token ([guaranteed all-or-nothing result] "
           "(dynamodb-transactwriteitems-all-or-nothing); [include a client token] (dynamodb-transactwriteitems-idempotent-client-token)). "
           "Distractors: one BatchWriteItem call with both items (trap dynamodb-trap-batch-write-is-atomic; why links [only some of "
           "the actions] (dynamodb-transactwriteitems-vs-batchwriteitem)); two UpdateItem calls with atomic counters (misconception: "
           "[the updates are not idempotent] (dynamodb-atomic-counter-not-idempotent), and no all-or-nothing); two conditional "
           "UpdateItem calls and code that reverses the first if the second fails (violates-qualifier: custom rollback code)."))
slot(bullet="2.2.S2", concept="multi-region-recovery-choice", difficulty=2, type="single", layer="extended",
     exam_english=["ee-most-cost-effective", "ee-cross-region", "ee-acceptable"], section=sec("Every restore"),
     trap=None, distractor_traps=[], twin="second of strict twin pair C (twin_of q12)",
     key_facts=["dynamodb-dr-aws-backup-rpo-1-hour", "dynamodb-aws-backup-copy-multiple-accounts-regions", "dynamodb-gt-rwru-per-replica"],
     note=("Bullets also 2.2.S5. Strict twin of q12: same stem, options and qualifier. Changed phrase: 'After an outage of us-east-1, "
           "the company must be able to restore the orders in us-west-2; losing up to 1 hour of data and a recovery of several hours "
           "are acceptable.' Key: (B) Use AWS Backup to back up the table every hour and copy each backup to us-west-2 ([RPO of 1 "
           "hour] (dynamodb-dr-aws-backup-rpo-1-hour); [copy backups to multiple AWS accounts] "
           "(dynamodb-aws-backup-copy-multiple-accounts-regions) and Regions). In q16, (A) is violates-qualifier: a replica table "
           "means a second table and [one rWRU per replica table] (dynamodb-gt-rwru-per-replica) for every write, which the stem "
           "does not need; (C) and (D) impossible as in q12. Twin lines quote each other's changed phrase. At least 3 questions "
           "stand between q12 and q16."))
slot(bullet="4.3.K9", concept="relational-joins-not-dynamodb", difficulty=2, type="single", layer="extended",
     exam_english=["ee-least-operational-overhead", "ee-transactional"], section="1-fast.md#choose-it-or-not",
     trap="aurora-trap-dynamodb-for-joins", distractor_traps=["how-the-exam-asks-trap-keyword-bait"],
     key_facts=["dynamodb-no-join-operator", "dynamodb-decision-guide-aurora-relational-joins", "dynamodb-wa-oltp-dynamodb-vs-rds-joins",
                "dynamodb-nosql-queries-efficient-in-limited-ways"],
     note=("Bullets also 3.3.S4. A company is building a reporting service. Analysts run new ad hoc queries every week that join "
           "orders, customers and products, and the access patterns are not known in advance. The team wants a managed database. "
           "Which database meets these requirements with the LEAST operational overhead? Key: Amazon Aurora with SQL: relational "
           "databases support [complex queries through joins] (dynamodb-decision-guide-aurora-relational-joins) and suit [less "
           "predictable query patterns] (dynamodb-decision-guide-aurora-relational-joins). Leave Amazon RDS out of the options, so "
           "that it is not a second right answer. Distractors: DynamoDB with a global secondary index for each report (trap "
           "aurora-trap-dynamodb-for-joins; why links [doesn't support a JOIN operator] (dynamodb-no-join-operator) and [queried "
           "efficiently in a limited number of ways] (dynamodb-nosql-queries-efficient-in-limited-ways)); DynamoDB with DAX "
           "(keyword-bait: speed is not the requirement); ElastiCache as the data store (misconception: [ephemeral cache for "
           "frequently accessed data] (dynamodb-decision-guide-elasticache-caching-layer))."))
slot(bullet="3.3.K2", concept="dax-with-mixed-consistency-reads", difficulty=3, type="single", layer="extended",
     exam_english=["ee-must", "ee-acceptable", "ee-most-operationally-efficient"], section=sec("DAX answers"),
     trap="dynamodb-trap-dax-speeds-every-read", distractor_traps=["dynamodb-trap-gsi-strong-read"],
     key_facts=["dax-passes-through-strong-reads-and-transactions", "dax-eventually-consistent-microsecond-latency",
                "dax-client-routes-requests-to-cluster", "dynamodb-strong-reads-only-tables-and-lsi"],
     note=("An online store reads product items from a DynamoDB table. Product pages read the same items thousands of times a second; "
           "data a few seconds old is acceptable there, and the pages need microsecond reads. The checkout must read the current "
           "price of each item with a strongly consistent read. Which solution meets these requirements in the MOST operationally "
           "efficient way? Key: add a DAX cluster and use the DAX client for all reads: product pages use eventually consistent "
           "reads, which DAX serves from memory, and the checkout uses strongly consistent reads, which DAX passes to the table "
           "([eventually consistent data] [with microsecond latency] (dax-eventually-consistent-microsecond-latency); [DAX passes "
           "strongly consistent read requests to DynamoDB] (dax-passes-through-strong-reads-and-transactions)). Distractors: make "
           "every read strongly consistent through DAX so that the checkout is fast too (trap dynamodb-trap-dax-speeds-every-read; "
           "why links [it does not cache the results] (dax-passes-through-strong-reads-and-transactions)); have the checkout read "
           "a global secondary index with strong consistency (trap dynamodb-trap-gsi-strong-read; why links [only supported on "
           "tables and local secondary indexes] (dynamodb-strong-reads-only-tables-and-lsi)); cache the product items in each web "
           "server's memory and refresh them every few seconds (violates-qualifier: code and stale copies per server; misconception "
           "tag none). 'a few seconds' is a stem phrase without a number."))
slot(bullet="4.3.K4", concept="ttl-expiry-and-filter-on-read", difficulty=3, type="multi", layer="extended",
     exam_english=["ee-select-two", "ee-must", "ee-most-operationally-efficient"], section=sec("Time to Live"),
     trap="dynamodb-trap-ttl-deletes-on-time", distractor_traps=["how-the-exam-asks-trap-eventually-means-maybe"],
     key_facts=["dynamodb-ttl-attribute-number-epoch-seconds", "dynamodb-ttl-deletes-within-days-no-wcu",
                "dynamodb-ttl-expired-items-visible-until-deleted", "dynamodb-ttl-filter-expired-items-on-read"],
     note=("Select TWO, five options. A web application stores sessions in a DynamoDB table. A session must expire one hour after its "
           "last use, expired sessions must never be accepted, and old session items must be removed without extra write cost. "
           "Which TWO actions meet these requirements in the MOST operationally efficient way? (Select TWO.) Keys: enable TTL on an "
           "attribute that stores the expiry time as a Number in epoch seconds ([Unix epoch time format at the seconds granularity] "
           "(dynamodb-ttl-attribute-number-epoch-seconds); [without consuming any write throughput] "
           "(dynamodb-faq-ttl-no-write-throughput)); in every read, reject items whose expiry time is in the past, with a filter "
           "or a check in code ([can be filtered from read and write operations] (dynamodb-ttl-filter-expired-items-on-read)). "
           "Distractors: rely on TTL alone, because TTL deletes items as soon as they expire (trap dynamodb-trap-ttl-deletes-on-time; "
           "why links [within a few days of their expiration time] (dynamodb-ttl-deletes-within-days-no-wcu)); store the expiry as "
           "an ISO 8601 text string (misconception: [ignored by the TTL process] (dynamodb-ttl-non-number-attribute-ignored)); a "
           "Lambda function every minute that scans and deletes expired sessions (violates-requirement: write cost, overhead). "
           "Worked: no. 'one hour' is a stem value."))
slot(bullet="3.3.K4", concept="prewarm-on-demand-for-launch", difficulty=3, type="single", layer="extended",
     exam_english=["ee-stringent", "ee-spiky", "ee-least-operational-overhead"], section=sec("On-demand mode"),
     trap="dynamodb-trap-on-demand-absorbs-any-spike", distractor_traps=["dynamodb-trap-auto-scaling-prevents-throttling"],
     key_facts=["dynamodb-on-demand-previous-peak-double", "dynamodb-on-demand-throttle-if-double-within-30-min",
                "dynamodb-warm-throughput-prewarm-for-peak-events", "dynamodb-warm-throughput-definition"],
     note=("A company will launch a ticket sale. Its new DynamoDB table in on-demand mode has served only light test traffic. At the "
           "launch minute, the company expects many times more requests than the table has ever served, and it has stringent "
           "requirements: no request may be throttled. Which solution meets these requirements with the LEAST operational overhead? "
           "Key: before the launch, raise the table's warm throughput to the expected peak (pre-warm) ([pre-warming] and [baseline "
           "that your tables can instantly support] (dynamodb-warm-throughput-prewarm-for-peak-events)). Distractors: keep on-demand "
           "mode as it is, because it absorbs any spike (trap dynamodb-trap-on-demand-absorbs-any-spike; why links [instantly "
           "accommodates up to double the previous peak] (dynamodb-on-demand-previous-peak-double)); switch to provisioned mode with "
           "auto scaling at a 70% target (trap dynamodb-trap-auto-scaling-prevents-throttling); put DAX in front of the table "
           "(misconception: writes go through to the table: [first written to the DynamoDB table] (dax-write-through-both-table-and-dax)). "
           "Warm throughput became available on 2024-11-13 (dynamodb-change-warm-throughput-2024-11, volatile change fact): the key "
           "facts above are stable and the feature is examinable; never link the change fact in a why."))
slot(bullet="3.3.S2", concept="private-access-vpc-and-on-premises", difficulty=3, type="multi", layer="extended",
     exam_english=["ee-select-two", "ee-privately", "ee-most-cost-effective", "ee-on-premises"], section=sec("IAM controls access"),
     trap=None,
     distractor_traps=["vpc-trap-s3-needs-nat", "vpc-trap-endpoint-types-alike"],
     worked="worked think-aloud with a wrong path",
     key_facts=["dynamodb-faq-gateway-endpoint-no-igw-nat", "dynamodb-faq-gateway-endpoint-limits-use-privatelink",
                "dynamodb-faq-privatelink-interface-endpoints", "vpc-endpoints-wp-gateway-endpoint-no-additional-charge"],
     note=("Select TWO, five options. Applications in private subnets of a VPC and servers in the company's data center, connected "
           "through AWS Direct Connect, read and write a DynamoDB table. The traffic must not use the public internet, and the cost "
           "must be as low as possible. Which TWO actions meet these requirements MOST cost-effectively? (Select TWO.) Keys: a "
           "gateway endpoint for DynamoDB in the VPC route tables for the applications ([without requiring an internet gateway or "
           "NAT device] (dynamodb-faq-gateway-endpoint-no-igw-nat); [no additional charge for using gateway endpoints] "
           "(vpc-endpoints-wp-gateway-endpoint-no-additional-charge)); an interface endpoint for DynamoDB (AWS PrivateLink) for the "
           "data center servers ([you must use AWS PrivateLink] (dynamodb-faq-gateway-endpoint-limits-use-privatelink); [interface "
           "VPC endpoints and private IP addresses] (dynamodb-faq-privatelink-interface-endpoints)). Distractors: a NAT gateway in "
           "each Availability Zone (tag vpc-trap-s3-needs-nat only if its belief text covers DynamoDB; otherwise misconception); "
           "route the data center servers through the gateway endpoint (tag vpc-trap-endpoint-types-alike; why links the "
           "FAQ restriction); an internet gateway with public IP addresses (violates-requirement). Worked with a wrong path: step 3 "
           "predicts 'interface endpoints for everything', step 5 'My first idea breaks because' the applications in the VPC can use "
           "the gateway endpoint at no charge."))
slot(bullet="3.3.K1", concept="global-tables-active-active-writes", difficulty=2, type="single", layer="extended",
     exam_english=["ee-users-around-the-world", "ee-lowest-latency", "ee-highly-available"], section=sec("In a global table"),
     trap="dynamodb-trap-global-table-primary-region", distractor_traps=["aurora-trap-global-all-regions-write"],
     key_facts=["dynamodb-global-table-any-replica-serves-reads-writes", "dynamodb-faq-global-tables-no-failover-needed",
                "dynamodb-faq-global-tables-same-apis", "dynamodb-vs-aurora-global-database-single-writer"],
     note=("Bullets also 2.2.S2. A company's users around the world write to a profile service that stores items in a DynamoDB table "
           "in us-east-1. Users in Europe and Asia see high write latency. Writes must be local in each Region, and the service must "
           "stay highly available if one Region fails. Which solution gives the LOWEST write latency for every user? Key: a global "
           "table with replica tables in the users' Regions, each application writing to its local replica ([Any global table "
           "replica] can [serve reads and writes] (dynamodb-global-table-any-replica-serves-reads-writes); [same APIs as single "
           "Region DynamoDB tables] (dynamodb-faq-global-tables-same-apis)). Distractors: a global table whose us-east-1 replica "
           "takes all writes and fails over to another Region in an outage (trap dynamodb-trap-global-table-primary-region; why "
           "links [no primary Region] (dynamodb-faq-global-tables-no-failover-needed)); Aurora Global Database with clusters in each "
           "Region (trap aurora-trap-global-all-regions-write; why links [Only the primary cluster performs write operations] "
           "(dynamodb-vs-aurora-global-database-single-writer)); DAX clusters in Europe and Asia (impossible-feature: [tables that "
           "are in the same Region] (dax-same-region-as-tables)). Do not use MRSC facts (volatile)."))

BRIEF["question_plan"] = {
    "write": 22,
    "difficulty": {"1": 3, "2": 13, "3": 6},
    "difficulty_note": ("3/22 = 14% (target 20% +- 10), 13/22 = 59% (55% +- 10), 6/22 = 27% (25% +- 10). When the weakest four are "
                        "cut, cut at least one difficulty-2 question for each cut of a 1 or a 3, so that the shipped mix stays inside "
                        "the tolerance."),
    "layer": {"core": 11, "extended": 11},
    "multi": 3,
    "multi_slots": ["q05 (core, difficulty 2)", "q19 (extended, difficulty 3)", "q21 (extended, difficulty 3, worked, wrong path)"],
    "twin_pairs": [
        "q01 / q07 (strict, core, difficulty 2, MOST cost-effectively: 'Traffic is unpredictable: it stays near zero for hours, then rises to many times the usual level within minutes.' / 'Traffic is steady and predictable around the clock, the provisioned capacity is almost fully used all day, and the load will stay at this level for at least the next 3 years.'; same four options; key A / key B)",
        "q04 / q10 (strict, core, difficulty 2, LEAST operational overhead: 'The table currently holds two years of orders, and eventually consistent reads are acceptable for the new screen.' / 'The table is being created now and holds no data yet, and the new screen must use strongly consistent reads.'; same four options; key A / key B)",
        "q12 / q16 (strict, extended, difficulty 2, MOST cost-effectively: 'If us-east-1 becomes unavailable, users must keep reading and writing orders in us-west-2 within seconds, with no restore step.' / 'After an outage of us-east-1, the company must be able to restore the orders in us-west-2; losing up to 1 hour of data and a recovery of several hours are acceptable.'; same four options; key A / key B)",
    ],
    "twin_pairs_note": ("Three strict pairs are written so that one rejection still ships two whole pairs (orchestrator note). Each "
                        "pair turns on a stable fact; none on a volatile one. The twin field of the later question is twin_of."),
    "worked": ["q02 (no wrong path)", "q21 (wrong path)"],
    "slots_on_a_trap": 14,
    "every_trap_cited": ("All 13 trap ids of this brief are the slot trap or a planned distractor trap of at least one slot: "
                         "spare-capacity-no-throttle q02; default-read-is-latest q03 (and q08 distractor); ttl-deletes-on-time q19; "
                         "dax-speeds-every-read q18 (and q03 distractor); global-table-primary-region q22; "
                         "gsi-strong-read q10 (and q03 q18 distractors); on-demand-absorbs-any-spike q20; auto-scaling-prevents-throttling "
                         "q01 (and q07 q20 distractors); filter-saves-capacity q05 (and q04 q10 distractors); lsi-added-later q04; "
                         "batch-write-is-atomic q15; stream-keeps-changes q14; restore-in-place q09."),
    "bullets_covered": ("all 13 bullets of the registry entry are the primary bullet of at least one slot: 3.3.K1 q22; 3.3.K2 q06 q18; "
                        "3.3.K3 q02 q04 q10; 3.3.K4 q05 q20; 3.3.K8 q15; 3.3.S2 q03 q14 q21; 3.3.S4 q11; 4.3.K4 q13 q19; "
                        "4.3.K5 q08; 4.3.K9 q17; 4.3.S3 q01 q07; 2.2.S2 q12 q16; 2.2.S5 q09. Secondary bullets are named in each "
                        "note ('Bullets also ...'); list them in the item's bullets field after the primary one."),
    "q205_rule": ("Q205 is a chapter rule: at least half of all wrong options of the chapter carry a trap id (this brief's 13, or "
                  "traps_from_other_chapters). A distractor gets a trap id only when its text states exactly that trap's belief; "
                  "otherwise it carries a misconception and a distractor_type. Aim for two tagged wrong options in most questions."),
    "rule": ("Question ids are dynamodb-q001 to dynamodb-q022 in slot order (q01 = dynamodb-q001). Protect the three twin pairs, the "
             "three multiple-response questions and both worked questions when the weakest four are cut. At most 2 questions per "
             "concept; a unique (concept, trap) pair per question (twins exempt). Stems never name Callvale; they may reuse its "
             "situation. Keep at most one impossible-feature distractor per question, and give it a fact. Never let a volatile fact "
             "decide a key (list below). Never state a price. Within a twin pair, the qualifier, the options and every sentence but "
             "the changed phrase are identical."),
    "qualifier_rule": ("Difficulty 1 questions (q03, q08, q09) have qualifier none and no violates-qualifier option; every other "
                       "question has one qualifier word of SPEC questions.qualifier_words (MOST, LEAST, BEST, LOWEST, HIGHEST, "
                       "FASTEST) and at least one violates-qualifier option. 3 of 22 without a qualifier stays under the 25% cap of "
                       "Q204."),
    "key_facts_note": "key_facts of each slot are the stable facts that decide its key; build_brief.py checked that none is volatile.",
}
