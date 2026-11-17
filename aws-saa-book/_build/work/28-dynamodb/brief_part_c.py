# brief-28, part C: How-it-works subsections 8 to 14, then Numbers, Decision record and FAQ quick-fire.

# 8 ---------------------------------------------------------------------------------------------
sub("Conditional writes and transactions stop one write from overwriting another", 4, 210, ["3.3.S2", "3.3.K8"],
    ["dynamodb-updateitem-conditional-update", "dynamodb-updateitem-atomic-counter", "dynamodb-transactions-all-or-nothing",
     "dynamodb-transactions-serializable-isolation", "dynamodb-transaction-max-items", "dynamodb-transaction-max-data",
     "dynamodb-transactget-100-actions", "dynamodb-transaction-single-account-region", "dynamodb-transactions-not-on-indexes",
     "dynamodb-transactions-capacity-consumed-even-on-failure", "dynamodb-transaction-two-units-prepare-commit",
     "dynamodb-transaction-changes-propagate-gradually", "dynamodb-s3-dynamodb-no-cross-transactions"],
    {
        "problem": ("Two workers read the same item, change it and write it back. Without a check, the second write silently "
                    "erases the first one."),
        "trace": [
            "**Overwrite by default.** `PutItem` and `DeleteItem` are [unconditional] (dynamodb-writes-unconditional-by-default): each one [overwrites an existing item] (dynamodb-writes-unconditional-by-default) that has the same key.",
            "**Add a condition.** [A conditional write succeeds] (dynamodb-conditional-write-succeeds-only-if-condition) only if the item attributes [meet one or more expected conditions] (dynamodb-conditional-write-succeeds-only-if-condition), for example [if there is not already an item] (dynamodb-conditional-write-use-cases) with that key.",
            "**Catch a concurrent change.** With optimistic locking, each item has a [version attribute that increments with every update] (dynamodb-optimistic-locking-detects-conflicts-at-write); a writer with an old version gets a [`ConditionalCheckFailedException`] (dynamodb-optimistic-locking-condition-fails-on-concurrent-change).",
            "**Change several items as one.** A transaction makes [all-or-nothing changes to multiple items] (dynamodb-transactions-acid-multiple-items-tables) with [atomicity, consistency, isolation, and durability (ACID)] (dynamodb-transactions-acid-multiple-items-tables); `TransactWriteItems` groups [up to 100 write actions] (dynamodb-transactwrite-100-actions).",
            "**Stay in one account and Region.** The items must be in the [same AWS account and in the same Region] (dynamodb-transactwriteitems-same-account-same-region), and DynamoDB performs [two underlying reads or writes of every item] (dynamodb-transactions-no-extra-cost-two-operations).",
        ],
        "table": ("Which write keeps data correct (columns: Need | Use | If the check fails): create an item only if it is new | "
                  "`PutItem` with a condition | the write fails; nothing changes; update only the version you read | a condition on "
                  "the version attribute | the write fails, and you read again; change two items together | `TransactWriteItems` "
                  "| [no changes are made at all] (dynamodb-transactwriteitems-vs-batchwriteitem); count page views | an atomic "
                  "counter in `UpdateItem` | not a check: [the updates are not idempotent] (dynamodb-atomic-counter-not-idempotent)."),
        "why": ("Why no locks? Optimistic locking [detects conflicts at write time] (dynamodb-optimistic-locking-detects-conflicts-at-write) "
                "instead of blocking readers, so no reader waits for a writer."),
        "exam_signal": ("\"all-or-nothing\" or \"both updates must succeed or neither\" points to `TransactWriteItems`, which gives a "
                        "[guaranteed all-or-nothing result] (dynamodb-transactwriteitems-all-or-nothing)."),
        "exam_trap": "dynamodb-trap-batch-write-is-atomic",
        "exam_trap_text": ("> **Exam trap:** `BatchWriteItem` is not a transaction. With it, [only some of the actions] "
                           "(dynamodb-transactwriteitems-vs-batchwriteitem) might succeed, and [`BatchWriteItem` does not support "
                           "`UpdateItem` requests] (dynamodb-batchwriteitem-no-updateitem). "
                           "<!-- trap: dynamodb-trap-batch-write-is-atomic -->"),
        "try_it": "dynamodb-t03 (Try it callout, one line: 'Make a conditional write refuse an overwrite' in 3-do.md)",
        "body_extras": ("Only if words remain, one sentence: a retried `TransactWriteItems` stays idempotent if you [include a client "
                        "token] (dynamodb-transactwriteitems-idempotent-client-token), which is valid for [10 minutes] "
                        "(dynamodb-transaction-client-token-10-minutes). Reference only: an atomic counter is wrong where "
                        "[overcounting or undercounting can't be tolerated] (dynamodb-atomic-counter-not-for-exact-counts); "
                        "transaction limits [100 unique items] (dynamodb-transaction-max-items) and [4 MB] "
                        "(dynamodb-transaction-max-data) are in the B-list; [Transactions cannot be performed using indexes] "
                        "(dynamodb-transactions-not-on-indexes); a failed transaction still uses capacity "
                        "(dynamodb-transactions-capacity-consumed-even-on-failure)."),
        "say_it": "The short answer is: a condition or a transaction protects a write. The thing to watch is that a batch write can half succeed.",
        "stop_and_answer": ("A booking service must create a booking item and lower the seats-left number in another item. If one "
                            "change fails, neither may stay. Which call? Answer: `TransactWriteItems`: the actions [either succeeds "
                            "or fails as a unit] (dynamodb-transactwriteitems-succeeds-or-fails-as-unit) (write the link so the "
                            "sentence reads 'the transaction either succeeds or fails as a unit'); add a condition that seats left "
                            "stay above zero."),
    })

# 9 ---------------------------------------------------------------------------------------------
sub("Time to Live deletes expired items without using write capacity", 3, 205, ["4.3.K4", "4.3.S3"],
    ["dynamodb-faq-ttl-defines-per-item-timestamp", "dynamodb-faq-ttl-use-case", "dynamodb-ttl-per-item-expiration-timestamp",
     "dynamodb-ttl-expired-items-deleted-at-any-time", "dynamodb-ttl-expired-item-still-updatable", "dynamodb-ttl-five-years-past-ignored",
     "dynamodb-ttl-no-minimum-duration", "dynamodb-ttl-toggle-once-per-hour", "dynamodb-ttl-stream-identification-only-in-source-region",
     "dynamodb-ttl-streams-lambda-no-getrecords-charge", "dynamodb-table-class-default-standard", "dynamodb-table-class-default-standard-no-performance-effect",
     "dynamodb-table-class-standard-ia-same-performance", "dynamodb-table-class-standard-lower-throughput-cost",
     "dynamodb-table-class-standard-vs-ia-50-percent-storage", "dynamodb-table-class-not-permanent", "dynamodb-table-class-update-background",
     "dynamodb-table-class-switch-no-code-change", "dynamodb-table-class-indexes-share-table-class", "dynamodb-table-class-change-limit",
     "dynamodb-table-class-standard-ia-feature-compatible", "dynamodb-faq-standard-ia-features", "dynamodb-faq-standard-ia-dax-compatible",
     "dynamodb-time-series-one-table-per-period", "dynamodb-time-series-old-tables-standard-ia", "dynamodb-time-series-older-tables-scale-down",
     "dynamodb-table-class-ia-60-lower-25-higher", "dynamodb-table-class-ia-threshold-50-percent"],
    {
        "problem": ("Old session and job items fill a table and raise the storage bill. A nightly delete job costs write capacity, "
                    "and someone must run it."),
        "trace": [
            "**Turn it on and name an attribute.** You [first enable it on a table] (dynamodb-ttl-enable-then-define-attribute) and then [define a specific attribute] (dynamodb-ttl-enable-then-define-attribute) for the expiry time.",
            "**Store a number in epoch seconds.** The value must be a Number in [Unix epoch time format at the seconds granularity] (dynamodb-ttl-attribute-number-epoch-seconds); a TTL attribute that is [not a Number type] (dynamodb-ttl-non-number-attribute-ignored) is [ignored by the TTL process] (dynamodb-ttl-non-number-attribute-ignored).",
            "**Delete later, at no write cost.** DynamoDB deletes expired items [within a few days of their expiration time] (dynamodb-ttl-deletes-within-days-no-wcu), [without consuming any write throughput] (dynamodb-faq-ttl-no-write-throughput).",
            "**Filter until then.** Expired items [continue to show in read and write operations] (dynamodb-ttl-expired-items-visible-until-deleted) and [still count towards storage and read costs] (dynamodb-ttl-expired-items-count-for-storage-reads); they [can be filtered from read and write operations] (dynamodb-ttl-filter-expired-items-on-read).",
            "**Send deletes to the stream.** TTL deletes [go into DynamoDB Streams] (dynamodb-ttl-deletes-appear-in-streams-as-service) as [service deletions instead of user deletes] (dynamodb-ttl-deletes-appear-in-streams-as-service), so a function can archive them.",
        ],
        "table": ("Keep or delete old data (columns: Need | Use): delete items after a time | time to live (TTL); keep rarely read "
                  "data at a lower storage price | the Standard-IA table class, made for tables where [storage is the dominant "
                  "cost] (dynamodb-table-class-standard-ia-lower-storage-cost); keep data until you delete it | nothing: by "
                  "default data will [remain in the table indefinitely] (dynamodb-faq-data-retention-indefinite); archive expired "
                  "items to Amazon S3 | TTL plus a stream and a Lambda function."),
        "why": ("Why days and not seconds? TTL runs as a background process: AWS presents it as a [cost-effective method for "
                "deleting items] (dynamodb-ttl-cost-effective-delete), not as a timer."),
        "exam_signal": ("\"delete session data automatically after a period, at no extra cost\" points to TTL, which [automatically "
                        "deletes expired items] (dynamodb-faq-ttl-deletes-expired-items)."),
        "exam_trap": None,
        "spot_the_bug": ("**Spot the bug.** A team enables TTL on the attribute `expires`. The code writes it as text, for example "
                         "\"2026-10-14T12:00:00Z\". A month later, no item has been deleted. What is wrong? Reveal: the TTL "
                         "attribute must be a Number in [Unix epoch time format at the seconds granularity] "
                         "(dynamodb-ttl-attribute-number-epoch-seconds); an attribute that is [not a Number type] "
                         "(dynamodb-ttl-non-number-attribute-ignored) is [ignored by the TTL process] "
                         "(dynamodb-ttl-non-number-attribute-ignored). Store the expiry as epoch seconds."),
        "body_extras": ("Only if words remain, one sentence: Standard-IA has [~60% lower] (dynamodb-table-class-ia-60-lower-25-higher) "
                        "storage cost and [~25% higher] (dynamodb-table-class-ia-60-lower-25-higher) read and write cost, and a table "
                        "can switch [twice in a 30-day period] (dynamodb-faq-table-class-switch-twice-30-days). The 60/25 fact is "
                        "volatile: prose only. Reference only: the time series pattern (dynamodb-time-series-old-tables-standard-ia); "
                        "TTL toggle once per hour (dynamodb-ttl-toggle-once-per-hour); TTL more than five years in the past "
                        "(dynamodb-ttl-five-years-past-ignored)."),
        "say_it": "The short answer is: TTL deletes old items for free in the background. The thing to watch is that expired items can still appear for a while.",
        "stop_and_answer": ("A game keeps daily scores for one year. After a week the scores are rarely read, and storage is most "
                            "of the table bill. TTL, a table class, or both? Answer: both: the Standard-IA class, because [Standard-IA "
                            "tables have lower storage costs] (dynamodb-faq-table-class-cost-tradeoff), and TTL to delete each score "
                            "when its year ends, [without consuming any write throughput] (dynamodb-faq-ttl-no-write-throughput)."),
    })

# 10 --------------------------------------------------------------------------------------------
sub("DynamoDB Streams records each item change in order for 24 hours", 4, 215, ["3.3.S2"],
    ["dynamodb-faq-cdc-two-streaming-models", "dynamodb-faq-streams-24-hour-log", "dynamodb-faq-streams-auto-scale-capacity",
     "dynamodb-faq-stream-record-contents", "dynamodb-faq-streams-vs-kinesis-choice", "dynamodb-faq-kinesis-no-ordering-dedup",
     "dynamodb-streams-no-record-for-no-change", "dynamodb-streams-separate-endpoint-same-region", "dynamodb-streams-shard-readers",
     "dynamodb-streams-disabled-stream-readable-24h", "dynamodb-streams-encrypted-at-rest", "dynamodb-streams-view-old-image",
     "dynamodb-streams-vs-kds-processing-options", "dynamodb-streams-consumers-flink-eventbridge-lambda", "dynamodb-kds-longer-retention-enhanced-fan-out",
     "dynamodb-pricing-streams-lambda-getrecords-not-charged", "dynamodb-pricing-cdc-unit-per-1kb-write", "dynamodb-transaction-changes-propagate-gradually",
     "lambda-ddb-streams-poll-4-per-second", "lambda-esm-batches-records", "lambda-faq-streams-retry-until-expiry",
     "eventbridge-faq-pipes-sources-sqs-kinesis-dynamodb-kafka-mq"],
    {
        "problem": ("Other systems must react when an item changes. Reading the table again and again to find changes is slow and "
                    "costs reads."),
        "trace": [
            "**Turn on a stream.** DynamoDB Streams is an [optional feature that captures data modification events] (dynamodb-streams-optional-feature); it [operates asynchronously] (dynamodb-streams-no-performance-impact-on-enable), with [no performance impact on a table] (dynamodb-streams-no-performance-impact-on-enable).",
            "**Choose what each record holds.** The stream view type is [`KEYS_ONLY`] (dynamodb-streams-view-keys-only), [`NEW_IMAGE`] (dynamodb-streams-view-new-image), [`OLD_IMAGE`] (dynamodb-streams-view-old-image) or [`NEW_AND_OLD_IMAGES`] (dynamodb-streams-view-new-and-old-images); to change it, you [disable the current stream] (dynamodb-streams-view-type-not-editable) and create a new one.",
            "**Keep each item's order.** Each record appears [exactly once in the stream] (dynamodb-streams-record-exactly-once), with [ordering at the level of an individual item] (dynamodb-streams-order-per-item-not-partition), [not across an entire partition] (dynamodb-streams-order-per-item-not-partition).",
            "**Let Lambda read it.** DynamoDB is [integrated with AWS Lambda] (dynamodb-streams-lambda-triggers): triggers [automatically respond to events in DynamoDB Streams] (dynamodb-streams-lambda-triggers) through an [Event source mapping] (lambda-trigger-dynamodb-esm), and on an error [Lambda retries the batch] (dynamodb-streams-lambda-retries-until-success-or-expiry).",
            "**Lose records after a day.** Stream records have a [lifetime of 24 hours] (dynamodb-stream-records-24-hours) and are then [automatically removed from the stream] (dynamodb-stream-records-24-hours).",
        ],
        "table": ("DynamoDB Streams or Kinesis Data Streams for DynamoDB (columns: Question | DynamoDB Streams | Kinesis Data Streams "
                  "for DynamoDB): consumers per shard | [2 simultaneous] (dynamodb-streams-vs-kds-consumers-per-shard) | [5 "
                  "simultaneous] (dynamodb-streams-vs-kds-consumers-per-shard), or [20 simultaneous consumers per shard] "
                  "(dynamodb-streams-vs-kds-consumers-per-shard) with enhanced fan-out; duplicates | [No duplicate records appear "
                  "in the stream] (dynamodb-streams-vs-kds-duplicates) | [Duplicate records might occasionally appear in the "
                  "stream] (dynamodb-streams-vs-kds-duplicates); order | [same sequence as the actual modifications] "
                  "(dynamodb-streams-vs-kds-ordering) | from a [timestamp attribute on each stream record] "
                  "(dynamodb-streams-vs-kds-ordering). Retention stays out of this table: the Exam trap carries it."),
        "why": ("Why a log of changes? Other systems react without reading the table, because DynamoDB Streams records a "
                "[time-ordered sequence of every item-level change] (dynamodb-streams-time-ordered-changes) in [near-real time] "
                "(dynamodb-streams-time-ordered-changes)."),
        "exam_signal": ("\"run a function when an item changes\" points to DynamoDB Streams with a Lambda trigger, the [native "
                        "integration with AWS Lambda] (dynamodb-faq-streams-lambda-triggers)."),
        "exam_trap": "dynamodb-trap-stream-keeps-changes",
        "exam_trap_text": ("> **Exam trap:** A stream is not an archive. Its records have a [lifetime of 24 hours] "
                           "(dynamodb-stream-records-24-hours); to keep and replay changes for longer, Kinesis Data Streams for "
                           "DynamoDB keeps them [up to 365 days] (dynamodb-faq-kinesis-365-day-retention). "
                           "<!-- trap: dynamodb-trap-stream-keeps-changes -->"),
        "body_extras": ("Only if words remain, one sentence: Lambda trigger reads of the stream cost nothing: you are [not charged for "
                        "GetRecords API calls] (dynamodb-pricing-streams-lambda-getrecords-not-charged) made [through DynamoDB "
                        "triggers on AWS Lambda] (dynamodb-pricing-streams-lambda-getrecords-not-charged) (volatile pricing fact: "
                        "prose only). Reference only: Kinesis Data Streams for DynamoDB [might appear in a different order] and "
                        "[might also appear more than once] (dynamodb-kds-order-and-duplicates); EventBridge Pipes can read a stream "
                        "(eventbridge-faq-pipes-sources-sqs-kinesis-dynamodb-kafka-mq); no record when nothing changed "
                        "(dynamodb-streams-no-record-for-no-change)."),
        "say_it": "The short answer is: a stream lists each item change in order, for a day. The thing to watch is how many readers share it.",
        "stop_and_answer": ("Each new order must reach a billing function, a search-index function and an analytics team's reader. "
                            "Is one DynamoDB stream enough? Answer: not with three readers: you can subscribe [up to two Lambda "
                            "functions] (dynamodb-streams-lambda-two-functions-per-stream) to one stream, and more [read throttling "
                            "might occur] (dynamodb-streams-lambda-two-functions-per-stream); Kinesis Data Streams for DynamoDB "
                            "supports [5 simultaneous] (dynamodb-streams-vs-kds-consumers-per-shard) consumers per shard."),
    })

# 11 --------------------------------------------------------------------------------------------
sub("DAX answers repeated eventually consistent reads from memory in microseconds", 4, 215, ["3.3.K2", "3.3.S2"],
    ["dax-faq-fully-managed-caching-microseconds", "dax-faq-microsecond-cache-10x", "dax-faq-extra-cost-option-in-memory-cache",
     "dax-no-cache-invalidation-or-population-needed", "dax-negative-caching", "dax-lru-evicts-before-expiry", "dax-query-cache-ttl-zero-not-cached",
     "dax-no-auto-refresh-after-direct-write", "dax-clients-may-read-different-values-by-node", "dax-node-replication-eventually-consistent",
     "dax-replica-failover-to-new-primary", "dax-primary-node-and-read-replicas", "dax-cluster-node-count", "dax-cluster-up-to-11-nodes",
     "dax-scale-by-adding-nodes", "dax-larger-node-type-needs-new-cluster", "dax-single-az-nodes-unavailable-on-az-failure",
     "dax-same-region-as-tables", "dax-security-group-port-8111", "dax-traffic-stays-in-vpc", "dax-cluster-needs-iam-service-role",
     "dax-service-role-policy-defines-dynamodb-actions", "dax-users-inherit-cluster-policy", "dax-iam-policy-needs-dax-actions",
     "dax-separate-clusters-for-isolation", "dax-no-table-management-operations", "dax-supports-transactions-same-isolation",
     "dax-transactgetitems-not-cached", "dax-transactwriteitems-extra-read-capacity", "dax-write-around-reduces-write-latency",
     "dax-write-through-extra-network-hop", "dax-bulk-writes-reduce-read-cache-effectiveness", "dax-cost-reduction-high-hit-rate",
     "dax-sizing-typical-hit-rate-85-95", "dax-sizing-consumed-rcu-only-cache-misses", "dax-low-cache-hit-cold-data-not-worth-it",
     "dax-not-ideal-no-microsecond-need-or-repeated-reads", "dax-encryption-at-rest-aes-256", "dax-encryption-at-rest-no-customer-keys",
     "dax-encryption-in-transit-not-on-existing-cluster", "dax-pricing-pay-for-provisioned-capacity", "dax-single-item-reads-beyond-3000-rcu",
     "elasticache-builders-library-inline-cache-dax-read-through"],
    {
        "problem": ("Single-digit milliseconds is not fast enough for some screens, and a few hot items can get most of the reads. A "
                    "cache in front of the table answers those reads from memory."),
        "trace": [
            "**Send every call to DAX.** The DAX client [directs all of your application's DynamoDB API requests] (dax-client-routes-requests-to-cluster) to the cluster, and DAX is [API-compatible with DynamoDB] (dax-api-compatible-minimal-changes).",
            "**Answer a hit from memory.** DAX keeps an [item cache] (dax-item-cache-getitem-batchgetitem) for GetItem and a [query cache] (dax-query-cache-query-scan) for Query and Scan, and returns [eventually consistent data] (dax-eventually-consistent-microsecond-latency) [with microsecond latency] (dax-eventually-consistent-microsecond-latency).",
            "**Fill the cache on a miss.** On a miss, [DAX sends the request to DynamoDB] (dax-cache-miss-reads-dynamodb-and-fills-cache), and then [DAX stores them in the item cache] (dax-cache-miss-reads-dynamodb-and-fills-cache).",
            "**Write through.** DAX is a [write-through caching service] (dax-is-write-through-cache): data is [first written to the DynamoDB table] (dax-write-through-both-table-and-dax), then to the cache.",
            "**Skip the cache for strong reads.** [DAX passes strongly consistent read requests to DynamoDB] (dax-passes-through-strong-reads-and-transactions), and [it does not cache the results] (dax-passes-through-strong-reads-and-transactions).",
        ],
        "table": ("When DAX helps (columns: Workload | DAX?): many repeated reads of the same items | yes: it suits apps that [read a "
                  "small number of items more frequently] (dax-ideal-fastest-reads-hot-keys); reads that must be strongly "
                  "consistent | no gain: apps that [require strongly consistent reads] (dax-not-ideal-strong-reads-write-heavy-few-repeats) "
                  "are not ideal; write-heavy | little: [DAX benefits might be limited] (dax-write-heavy-limited-benefit); "
                  "modest latency needs | not needed: DynamoDB alone gives [single-digit millisecond performance] "
                  "(dax-modest-needs-use-dynamodb-alone)."),
        "why": ("Why a cluster in your VPC? DAX is designed to [run within an Amazon Virtual Private Cloud] (dax-runs-inside-vpc), "
                "and [Three nodes are required] (dax-production-three-nodes-three-azs) for a fault-tolerant cluster."),
        "exam_signal": ("\"microsecond reads from DynamoDB with minimal code changes\" points to DAX, which needs [only minimal "
                        "functional changes] (dax-api-compatible-minimal-changes); \"cache several databases, or use lists and sorted "
                        "sets\" points to ElastiCache: [ElastiCache (Redis OSS) supports advanced data structures] "
                        "(dax-vs-elasticache-complex-queries)."),
        "exam_trap": None,
        "diagram": "dynamodb-dax-read (after the trace; caption and steps in diagrams)",
        "body_extras": ("Only if words remain, one sentence: cached items stay until their TTL, by default [5 minutes] "
                        "(dax-default-ttl-5-minutes-both-caches), so a write that bypasses DAX leaves the cache and the table to "
                        "[hold inconsistent values for the same key] (dax-bypass-causes-inconsistent-values) until then. Never link "
                        "dax-can-subvert-dynamodb-iam-policies: its display holds bold markup. Reference only: cluster size limits "
                        "(dax-cluster-up-to-11-nodes, B-list), port 8111 (dax-security-group-port-8111), same-Region tables "
                        "(dax-same-region-as-tables), encryption at rest without customer keys (dax-encryption-at-rest-no-customer-keys)."),
        "say_it": "The short answer is: DAX answers repeated reads from memory. The thing to watch is strong reads, which go straight to the table.",
        "stop_and_answer": ("A leaderboard reads the same 100 items thousands of times a second with eventually consistent reads; "
                            "writes are rare. Latency must drop to microseconds with almost no code change. Does DAX fit? Answer: "
                            "yes; DAX is [API-compatible with DynamoDB] (dax-api-compatible-minimal-changes), and it delivers [up to "
                            "a 10 times performance improvement] (dax-faq-microsecond-cache-10x) for repeated reads. 100 is an "
                            "example value in the prompt."),
    })

# 12 --------------------------------------------------------------------------------------------
sub("Every restore, from a backup or a point in time, creates a new table", 4, 215, ["2.2.S5", "4.3.K4"],
    ["dynamodb-backup-asynchronous-available-within-minutes", "dynamodb-ondemand-backup-no-performance-impact",
     "dynamodb-backup-cross-region-restore-native", "dynamodb-pitr-cross-region-restore", "dynamodb-pitr-no-capacity-no-impact",
     "dynamodb-pitr-latest-restorable-five-minutes", "dynamodb-pitr-restore-or-rollback-in-place", "dynamodb-pitr-shorter-period-same-price",
     "dynamodb-restore-no-provisioned-throughput", "dynamodb-restore-exclude-indexes-faster", "dynamodb-restore-concurrency-limits",
     "dynamodb-aws-backup-native-integration", "dynamodb-aws-backup-copy-cross-region-account", "dynamodb-aws-backup-restore-needs-copy-first",
     "dynamodb-aws-backup-files-not-deletable-in-dynamodb-console", "dynamodb-export-always-encrypted", "dynamodb-export-cross-account-cross-region",
     "dynamodb-export-formats", "dynamodb-export-no-completion-sla", "dynamodb-incremental-export-window", "dynamodb-import-new-table-only",
     "dynamodb-import-no-write-capacity", "dynamodb-import-source-formats", "dynamodb-import-gsi-supported-lsi-not",
     "dynamodb-faq-extra-cost-option-on-demand-backup", "dynamodb-faq-global-tables-pitr-per-replica",
     "dynamodb-pitr-global-table-replica-restore-independent", "dynamodb-pricing-pitr-delete-system-backup-free",
     "well-architected-resiliency-managed-services-customer-owns-backup-versioning-replication"],
    {
        "problem": ("A bad release deletes items, or someone deletes a table. The data must come back as it was at a known moment, "
                    "without risk to what still works."),
        "trace": [
            "**Take on-demand backups.** Each on-demand backup means the [entire table data is backed up] (dynamodb-backup-full-table-every-time), [without consuming any provisioned throughput on the table] (dynamodb-backup-no-provisioned-throughput) and with [zero impact on table performance or availability] (dynamodb-backup-restore-zero-performance-impact).",
            "**Turn on point-in-time recovery.** PITR gives [automatic continuous backups] (dynamodb-pitr-automatic-continuous-backups) that protect a table [from accidental write or delete operations] (dynamodb-pitr-protects-accidental-writes-deletes); you can restore to a moment from [five minutes before the current time] (dynamodb-pitr-restore-window-five-minutes-to-period) back to the start of the recovery period.",
            "**Restore into a new table.** Point-in-time recovery [always restores to a new table] (dynamodb-pitr-restores-to-new-table), and a backup restores the [entire table data to a new table] (dynamodb-backup-restore-only-to-new-table).",
            "**Set the missing settings again.** [Tags aren't preserved in restored tables] (dynamodb-restore-tags-not-preserved); add them, and check the other table settings, before the application uses the table.",
            "**Copy to other accounts and Regions.** AWS Backup can [copy backups to multiple AWS accounts] (dynamodb-aws-backup-copy-multiple-accounts-regions) [as part of a scheduled backup plan] (dynamodb-aws-backup-copy-multiple-accounts-regions), and Vault Lock keeps them [write-once-read-many (WORM)] (dynamodb-aws-backup-vault-lock-worm).",
        ],
        "table": ("Recovery options (columns: Option | RPO | RTO): PITR | [minimal RPO (seconds)] (dynamodb-dr-pitr-rpo-seconds) | "
                  "[reasonable RTO (minutes to hours)] (dynamodb-dr-pitr-rpo-seconds); daily on-demand backup | [RPO of 24 hours] "
                  "(dynamodb-dr-daily-on-demand-backup-rpo-24h) | minutes to hours; AWS Backup with an hourly cross-Region copy | "
                  "[RPO of 1 hour] (dynamodb-dr-aws-backup-rpo-1-hour) | minutes to hours; export to Amazon S3 | [RPO of a few "
                  "minutes] (dynamodb-dr-s3-export-rpo-minutes) | minutes to hours. 'minutes to hours' without a link in the last "
                  "three rows is plain text with no number: allowed. Spell out RPO and RTO at first use (bank terms)."),
        "why": ("Why always a new table? A restore never touches the live table: you check the restored data first, then point the "
                "application at it or copy items back. The resiliency of your data stays your job ([managing resiliency of your "
                "data including backup, versioning, and replication strategies] "
                "(well-architected-resiliency-managed-services-customer-owns-backup-versioning-replication))."),
        "exam_signal": ("\"restore the table to the state just before an accidental delete\" points to point-in-time recovery, "
                        "whose latest restore point is typically [five minutes before the current time] "
                        "(dynamodb-pitr-latest-restorable-five-minutes)."),
        "exam_trap": "dynamodb-trap-restore-in-place",
        "exam_trap_text": ("> **Exam trap:** A restore does not roll the live table back. You [can't overwrite an existing table] "
                           "(dynamodb-restore-cannot-overwrite-existing-table) during a restore, so the application must switch to "
                           "the new table or copy the items back. <!-- trap: dynamodb-trap-restore-in-place -->"),
        "go_deeper": ("Go deeper: deleted tables, exports and the recovery period (at most 70 words). Deleting a table that has PITR "
                      "leaves a [system backup] (dynamodb-pitr-deleted-table-system-backup) that DynamoDB [retains it for 35 days] "
                      "(dynamodb-pitr-deleted-table-system-backup). Turning PITR off and on will [reset the start time] "
                      "(dynamodb-pitr-reenable-resets-start-time). Export to Amazon S3 needs PITR ([enable PITR on your table] "
                      "(dynamodb-export-requires-pitr)) and exports [both full and incremental data] "
                      "(dynamodb-export-full-and-incremental). The recovery period can be set [between 1 and 35 days] "
                      "(dynamodb-change-pitr-configurable-period-2025-01)."),
        "body_extras": ("Reference only, no sentence: cross-Region PITR restore (dynamodb-pitr-cross-region-restore); AWS Backup "
                        "restores to another Region need a copy first (dynamodb-aws-backup-restore-needs-copy-first); import from S3 "
                        "creates a new table and uses no write capacity (dynamodb-import-new-table-only, "
                        "dynamodb-import-no-write-capacity); PITR on each global table replica (dynamodb-faq-global-tables-pitr-per-replica)."),
        "say_it": "The short answer is: every restore builds a new table. The thing to watch is that your application must switch to it.",
        "stop_and_answer": ("A bank requires backups that an administrator cannot delete, with copies in a second account. What do "
                            "you use? Answer: AWS Backup: it can [copy backups to multiple AWS accounts] "
                            "(dynamodb-aws-backup-copy-multiple-accounts-regions), and Vault Lock [protects backups from inadvertent "
                            "or malicious delete operations] (dynamodb-aws-backup-vault-lock-worm)."),
    })

# 13 --------------------------------------------------------------------------------------------
sub("In a global table, every replica accepts reads and writes", 5, 225, ["2.2.S2", "3.3.K1", "2.2.S5"],
    ["dynamodb-global-tables-definition", "dynamodb-faq-global-tables-all-replicas-read-write", "dynamodb-faq-global-vs-regular-table",
     "dynamodb-faq-reasons-for-global-tables", "dynamodb-faq-global-tables-same-apis", "dynamodb-global-tables-same-apis-no-app-changes",
     "dynamodb-global-tables-no-primary-table", "dynamodb-global-tables-available-wherever-dynamodb", "dynamodb-global-tables-same-durability-as-single-region",
     "dynamodb-faq-replica-table-same-items-and-key", "dynamodb-global-table-replicas-share-name-key-data", "dynamodb-global-tables-v2019-recommended",
     "dynamodb-global-tables-upgrade-keeps-serving", "dynamodb-global-tables-same-kms-key-type", "dynamodb-global-tables-encrypt-at-rest-kms",
     "dynamodb-gt-capacity-mode-synchronized-across-replicas", "dynamodb-global-tables-on-demand-write-capacity-synced",
     "dynamodb-gt-provisioned-replication-uses-write-capacity", "dynamodb-gt-replicated-write-price-same", "dynamodb-gt-rwru-per-replica",
     "dynamodb-gt-no-cross-region-transfer-fee", "dynamodb-gt-write-quota-match-regions", "dynamodb-gt-backfill-quota",
     "dynamodb-mrec-add-replica-no-performance-impact", "dynamodb-mrec-streams-enabled-cannot-disable", "dynamodb-mrec-ttl-delete-replicated",
     "dynamodb-mrec-ttl-replicated-delete-charged", "dynamodb-global-tables-replicationlatency-increase-redirect",
     "dynamodb-global-tables-apply-custom-logic-to-redirect", "dynamodb-gt-write-modes-three-active-active", "dynamodb-faq-global-tables-99999",
     "dynamodb-sla-standard-vs-global-tables", "dynamodb-multi-account-global-tables-replica-per-account", "dynamodb-change-multi-account-global-tables",
     "dynamodb-gt-multi-account-mrec-only", "dynamodb-global-tables-mrsc-same-account-only", "dynamodb-mrsc-witness-no-reads-writes",
     "dynamodb-mrsc-replicated-write-conflict", "dynamodb-mrsc-existing-items-not-supported", "dynamodb-mrsc-no-replicationlatency-metric",
     "dynamodb-gt-write-to-one-region-for-transactions", "dynamodb-gt-write-mixed-home-region", "dynamodb-global-tables-product-page-one-to-two-seconds",
     "rds-wa-cross-region-replication-primary-writes"],
    {
        "problem": ("Users on two continents want low latency, and the service must survive the loss of a whole Region. A table in "
                    "one Region cannot give either."),
        "trace": [
            "**Add a replica table per Region.** A global table has [two or more replica tables] (dynamodb-global-table-one-replica-per-region) in different Regions, with [only one replica per AWS Region] (dynamodb-global-table-one-replica-per-region).",
            "**Write anywhere.** [Any global table replica] (dynamodb-global-table-any-replica-serves-reads-writes) can [serve reads and writes] (dynamodb-global-table-any-replica-serves-reads-writes), and DynamoDB [automatically replicates the write to all other replicas] (dynamodb-global-table-write-replicated-automatically).",
            "**Replicate eventually by default.** If you choose nothing, the table [defaults to multi-Region eventual consistency (MREC)] (dynamodb-global-tables-default-mrec); writes arrive [typically within a second or less] (dynamodb-gt-mrec-default-last-writer-wins), and a conflict ends with [last writer wins] (dynamodb-gt-mrec-default-last-writer-wins).",
            "**Fail over without the database.** A global table has [no primary Region] (dynamodb-faq-global-tables-no-failover-needed); when a Region is impaired, you [shift application traffic to a different Region] (dynamodb-global-tables-shift-traffic-on-regional-impairment).",
            "**Know the recovery numbers.** MREC gives an [RPO of a few seconds] (dynamodb-dr-global-tables-mrec-rto-zero) and an [RTO of zero] (dynamodb-dr-global-tables-mrec-rto-zero); the SLA is [99.999%] (dynamodb-gt-sla-99999-vs-single-region-9999) instead of [99.99%] (dynamodb-gt-sla-99999-vs-single-region-9999) for one Region.",
        ],
        "table": ("MREC or MRSC (columns: Question | MREC | MRSC): Regions | two or more | [exactly three Regions] "
                  "(dynamodb-gt-mrsc-exactly-three-regions); data loss after a Region failure | [RPO of a few seconds] "
                  "(dynamodb-dr-global-tables-mrec-rto-zero) | [zero RPO] (dynamodb-dr-global-tables-mrsc-rpo-zero); a strongly "
                  "consistent read after a write in another Region | can return [stale data returned from strongly consistent read "
                  "operations] (dynamodb-mrec-strong-reads-may-be-stale) | returns the latest version. The MRSC facts "
                  "dynamodb-gt-mrsc-* are volatile (MRSC is new since 2025-06-30): table and prose only, never a question key. Write "
                  "MRSC's last cell 'the latest version' as plain text or link [always return the latest version of an item] "
                  "(dynamodb-gt-mrsc-synchronous-latest-reads)."),
        "why": ("Why last writer wins? Both models use [multi-Region writes, asynchronous replication, last-writer-wins conflict "
                "resolution] (dynamodb-global-tables-both-models-same-features) in MREC tables, so two Regions can change one item at "
                "once, and one simple rule keeps every replica table equal. If this link text is too long for the sentence, link "
                "[last writer wins] (dynamodb-gt-mrec-default-last-writer-wins) instead."),
        "exam_signal": ("\"active-active in several Regions with local writes\" points to global tables, a [multi-Region, and "
                        "multi-active database] (dynamodb-faq-global-tables-multi-active); \"one writer Region, relational\" points "
                        "to Aurora Global Database, where [Only the primary cluster performs write operations] "
                        "(dynamodb-vs-aurora-global-database-single-writer)."),
        "exam_trap": None,
        "go_deeper": ("Go deeper: what does not cross Regions (at most 70 words). Transactions are [not supported across Regions] "
                      "(dynamodb-transaction-not-across-gt-regions); in MREC, transactional writes are [not replicated as a unit "
                      "across Regions] (dynamodb-mrec-transactions-not-replicated-as-unit). In MRSC, [Time to Live (TTL) is not "
                      "supported] (dynamodb-gt-mrsc-no-ttl-lsi-transactions) (volatile: Go deeper only). You [cannot change a "
                      "global table's consistency mode] (dynamodb-global-tables-consistency-mode-fixed) after you create it."),
        "body_extras": ("Reference only, no sentence unless words remain: no cross-Region data transfer fee for replication "
                        "(dynamodb-gt-no-cross-region-transfer-fee); replicated writes are billed in each replica Region "
                        "(dynamodb-gt-rwru-per-replica); provisioned replicas need write capacity for replication "
                        "(dynamodb-gt-provisioned-replication-uses-write-capacity); multi-account global tables (MREC only; volatile "
                        "change fact): no sentence; the product page's 'one to two seconds' disagrees with the guide's 'a second or "
                        "less': write one figure only, the guide's, linked above."),
        "say_it": "The short answer is: every Region can read and write the same table. The thing to watch is conflicts, where the last write wins.",
        "stop_and_answer": ("A global table has replica tables in us-east-1 and eu-west-1. us-east-1 is impaired. What must the "
                            "team change in the database to keep writing? Answer: nothing in the database: there is [no primary "
                            "Region] (dynamodb-faq-global-tables-no-failover-needed); route users to eu-west-1, and data not yet "
                            "replicated [will be replicated when the replica becomes healthy] "
                            "(dynamodb-mrec-unreplicated-data-resumes-after-recovery)."),
    }, route="pass")

# 14 --------------------------------------------------------------------------------------------
sub("IAM controls access, and every table is encrypted at rest", 3, 205, ["3.3.S2", "2.2.S2"],
    ["dynamodb-faq-fgac-items-attributes", "dynamodb-attributes-condition-key-top-level", "dynamodb-faq-iam-attach-targets",
     "dynamodb-faq-resource-policies-tables-streams", "dynamodb-faq-resource-policy-covers-indexes", "dynamodb-resource-policy-max-20kb",
     "dynamodb-faq-block-public-access-always-on", "dynamodb-faq-abac-tags-ga", "dynamodb-cloudtrail-control-and-data-plane-events",
     "dynamodb-faq-audit-cloudtrail-item-level", "dynamodb-encryption-aes-256-kms", "dynamodb-faq-rest-kms-aes-256",
     "dynamodb-encryption-covers-indexes-streams-backups", "dynamodb-encryption-transparent", "dynamodb-encryption-key-type-switch-any-time",
     "dynamodb-encryption-key-switch-limit", "dynamodb-customer-managed-key-same-key-for-table-indexes-streams",
     "dynamodb-faq-key-aws-owned-default-free", "dynamodb-faq-key-aws-managed-audit", "dynamodb-faq-key-customer-managed-most-control",
     "dynamodb-aws-owned-key-no-fee", "dynamodb-faq-all-data-encrypted-transit-rest", "dynamodb-faq-transit-https", "dynamodb-https-default-ssl-tls",
     "dynamodb-faq-two-vpc-endpoint-types", "dynamodb-faq-privatelink-interface-endpoints", "dynamodb-faq-privatelink-stays-on-amazon-network",
     "dynamodb-faq-gateway-vs-privatelink-cost-note", "dynamodb-vpc-endpoint-private-ip-access", "dynamodb-faq-hipaa-baa",
     "vpc-endpoints-gateway-region-only", "vpc-gateway-endpoint-s3-dynamodb-no-privatelink", "vpc-endpoints-wa-cost08-gateway-free-interface-hourly",
     "well-architected-abstracted-services-aws-runs-os-customer-manages-data"],
    {
        "problem": ("A table often holds personal data. Only the right workloads may read it, the data must be encrypted, and "
                    "traffic from private subnets should stay off the internet."),
        "trace": [
            "**Use IAM, not passwords.** DynamoDB has [no user names or passwords] (dynamodb-no-passwords-iam-access); IAM policies decide every request.",
            "**Narrow to items and attributes.** A policy can [restrict access to individual items in a table] (dynamodb-fgac-restrict-items-and-attributes) and [access to the attributes in those items] (dynamodb-fgac-restrict-items-and-attributes), for example with the condition key [`LeadingKeys`] (dynamodb-leadingkeys-condition-key-partition-key), which stands for [the partition key] (dynamodb-leadingkeys-condition-key-partition-key).",
            "**Encrypt by default.** [By default, DynamoDB encrypts] (dynamodb-encrypt-at-rest-default) all data at rest; you choose an [AWS owned key (default encryption type)] (dynamodb-encryption-key-types), an [AWS managed key] (dynamodb-encryption-key-types) or a [Customer managed key] (dynamodb-encryption-key-types).",
            "**Keep control of your key.** With a customer managed key, disabling the key [prevents all users and the DynamoDB service] (dynamodb-customer-managed-key-disabled-blocks-access) from reading or writing the table.",
            "**Take the private path.** A gateway endpoint lets a VPC reach DynamoDB [without requiring an internet gateway or NAT device] (dynamodb-faq-gateway-endpoint-no-igw-nat); from on premises, [you must use AWS PrivateLink] (dynamodb-faq-gateway-endpoint-limits-use-privatelink).",
        ],
        "table": ("Which key type (columns: Key | Cost | What you can do): AWS owned key | [offered at no additional charge] "
                  "(dynamodb-aws-owned-key-no-additional-charge) | nothing: you [cannot view, manage, or use AWS owned keys] "
                  "(dynamodb-aws-owned-key-not-viewable); AWS managed key | [AWS KMS charges apply] "
                  "(dynamodb-aws-owned-key-no-additional-charge) | [audit their use in AWS CloudTrail logs] "
                  "(dynamodb-aws-managed-key-audit-cloudtrail); customer managed key | KMS charges (plain words, already linked in "
                  "row 2) | [Customer managed keys] (dynamodb-faq-key-customer-managed-most-control) give the most control: you "
                  "create, rotate and disable them."),
        "why": ("Why IAM and not database users? DynamoDB is an API service: [DynamoDB utilizes IAM] (dynamodb-no-passwords-iam-access), "
                "so the role that runs your code also carries its table permissions."),
        "exam_signal": ("\"each user may read only the items with the user's own ID\" points to fine-grained access control with "
                        "the [`LeadingKeys`] (dynamodb-leadingkeys-condition-key-partition-key) condition key."),
        "exam_trap": None,
        "spot_the_bug": ("**Spot the bug.** Lambda functions in private subnets write to DynamoDB through a NAT gateway, and the NAT "
                         "bill grows each month. What is wrong? Reveal: the functions can reach DynamoDB through a gateway endpoint, "
                         "[without requiring an internet gateway or NAT device] (dynamodb-faq-gateway-endpoint-no-igw-nat); there is "
                         "[no additional charge for using gateway endpoints] (vpc-endpoints-wp-gateway-endpoint-no-additional-charge)."),
        "body_extras": ("Only if words remain, one sentence: DynamoDB [supports resource-based policies for tables and streams] "
                        "(dynamodb-faq-resource-policies-tables-streams), and Block Public Access is [always enabled with DynamoDB] "
                        "(dynamodb-faq-block-public-access-always-on). Reference only: traffic uses HTTPS (dynamodb-https-default-ssl-tls); "
                        "encryption covers indexes, streams and backups (dynamodb-encryption-covers-indexes-streams-backups); the "
                        "volatile resource-policy and ABAC change facts: no sentence; chapter 10 and chapter 11 own the endpoint "
                        "details (xref)."),
        "say_it": "The short answer is: IAM controls access, and encryption is on by default. The thing to watch is the network path from private subnets.",
        "stop_and_answer": ("The security team disables the customer managed key of a table during an incident and forgets it. What "
                            "happens to the application, and what happens after a week? Answer: reads and writes fail at once, "
                            "because the disabled key [prevents all users and the DynamoDB service] "
                            "(dynamodb-customer-managed-key-disabled-blocks-access); if the key stays inaccessible [longer than seven "
                            "days] (dynamodb-customer-managed-key-inaccessible-archived), [the table is archived] "
                            "(dynamodb-customer-managed-key-inaccessible-archived)."),
    })

# Numbers, Decision record, FAQ ------------------------------------------------------------------
BRIEF["sections"].append({
    "file": "2-deep.md", "section": "numbers-that-decide-answers", "heading": "Numbers that decide answers", "bullets": ["4.3.K5", "3.3.K4"],
    "facts": [], "status": "write", "minutes": 3,
    "plan": ("The fixed H3 'A-list' with one numbers table of 8 rows (numbers.a_list; columns Number | What it is | Why it decides an "
             "answer) and the fixed H3 'B-list' with one table of 12 rows (numbers.b_list; columns Number | What it is). Column 1 is "
             "always the fact link with the display given. At most 290 words. Every A-list row has its number card (cards)."),
})
BRIEF["sections"].append({
    "file": "2-deep.md", "section": "decision-record", "heading": "Decision record", "bullets": ["4.3.S3", "3.3.S4", "4.3.K4"],
    "facts": [], "status": "write", "minutes": 3,
    "plan": ("Five bold fields in the order of CONVENTIONS D11 (see decision_record), with the before diagram dynamodb-before after "
             "Context and the after diagram dynamodb-after after Decision. At most 270 words with the diagram alt texts and steps."),
})
BRIEF["sections"].append({
    "file": "2-deep.md", "section": "faq-quick-fire", "heading": "FAQ quick-fire", "bullets": [], "facts": [], "status": "write", "minutes": 4,
    "plan": ("Ten items **FAQ 1.** to **FAQ 10.** in the form of CONVENTIONS D12 (see faq): a can-or-cannot question, a reveal with "
             "the short answer and its fact link, and an AWS quote block with the quote given, copied exactly, and the link line "
             "'— [Amazon DynamoDB FAQs](https://aws.amazon.com/dynamodb/faqs/)'. At most 430 words."),
})
