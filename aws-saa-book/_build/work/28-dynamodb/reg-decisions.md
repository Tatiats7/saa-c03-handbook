# register-28 decisions (2026-10-13)

Format: OLD -> KEPT (supersede), or REJECT id (reason).

## Duplicates
- dax-item-cache-ttl-default-5-minutes -> dax-default-ttl-5-minutes-both-caches (both caches covers item cache)
- dax-fully-managed-highly-available-cache -> dax-faq-fully-managed-caching-microseconds (same sentence; FAQ kept for quick-fire)
- dax-performance-10x-microseconds -> dax-faq-microsecond-cache-10x (same sentence on product page and FAQ)
- dynamodb-adaptive-capacity-automatic -> dynamodb-adaptive-capacity-automatic-no-cost (same sentence)
- dynamodb-adaptive-capacity-no-extra-cost -> dynamodb-adaptive-capacity-automatic-no-cost (same sentence)
- dynamodb-autoscaling-console-default -> dynamodb-autoscaling-console-enabled-by-default (same sentence)
- dynamodb-autoscaling-trigger-two-minutes -> dynamodb-autoscaling-two-consecutive-minutes (same sentence)
- dynamodb-aws-backup-schedule-copy-lifecycle -> dynamodb-aws-backup-native-integration (same quotes; its Vault Lock claim had no quote)
- dynamodb-burst-capacity-five-minutes -> dynamodb-burst-capacity-retention (identical)
- dynamodb-capacity-mode-switch-limit -> dynamodb-capacity-mode-switch-four-per-24h (same sentence, two pages)
- kept both: dax-cluster-node-count and dax-cluster-up-to-11-nodes (two pages, two phrasings of one limit; both exam-useful)
- dynamodb-index-comparison-queries-and-partitions -> dynamodb-index-queries-span-table-gsi-vs-single-partition-lsi (same table row)
- dynamodb-index-comparison-read-consistency -> dynamodb-index-read-consistency-gsi-vs-lsi (same table row)
- dynamodb-lsi-max-per-table -> dynamodb-index-limits-20-gsi-5-lsi (same limit, the kept sentence names both index types)
- dynamodb-gsi-default-per-table -> dynamodb-index-limits-20-gsi-5-lsi (same limit)
- dynamodb-large-items-store-s3-pointer -> dynamodb-large-items-store-in-s3 (same quote; extra claim parts had no quote)
- dynamodb-lsi-partition-key-same-as-table -> dynamodb-lsi-same-partition-key
- dynamodb-nested-attributes-32-levels -> dynamodb-nested-attribute-depth (identical sentence)
- dynamodb-unlimited-items-per-table -> dynamodb-table-size-no-practical-limit
- dynamodb-mrsc-exactly-three-regions -> dynamodb-gt-mrsc-exactly-three-regions
- dynamodb-mrsc-witness-option -> dynamodb-gt-mrsc-exactly-three-regions
- dynamodb-mrsc-ttl-not-supported -> dynamodb-gt-mrsc-no-ttl-lsi-transactions
- dynamodb-mrsc-lsi-not-supported -> dynamodb-gt-mrsc-no-ttl-lsi-transactions
- dynamodb-mrsc-transactions-not-supported -> dynamodb-gt-mrsc-no-ttl-lsi-transactions
- dynamodb-mrsc-rpo-zero -> dynamodb-gt-mrsc-rpo-zero-mrec-rpo-seconds
- dynamodb-mrec-rpo-equals-replication-delay -> dynamodb-gt-mrsc-rpo-zero-mrec-rpo-seconds
- dynamodb-mrsc-higher-latency-than-mrec -> dynamodb-gt-mrsc-rpo-zero-mrec-rpo-seconds
- dynamodb-mrsc-synchronous-to-another-region -> dynamodb-gt-mrsc-synchronous-latest-reads (identical quote)
- dynamodb-mrsc-synchronous-replication -> dynamodb-gt-mrsc-synchronous-latest-reads
- dynamodb-mrec-async-replication-within-a-second -> dynamodb-gt-mrec-default-last-writer-wins
- dynamodb-mrec-last-writer-wins -> dynamodb-gt-mrec-default-last-writer-wins
- dynamodb-mrec-default-replication-within-second -> dynamodb-gt-mrec-default-last-writer-wins
- dynamodb-global-tables-replication-consumes-write-capacity -> dynamodb-gt-provisioned-replication-uses-write-capacity
- dynamodb-global-tables-no-database-failover-needed -> dynamodb-gt-multi-active-no-failover-needed (same product-page sentence)
- dynamodb-ondemand-new-table-throughput -> dynamodb-new-ondemand-table-4000-writes-12000-reads
- dynamodb-ondemand-default-recommended -> dynamodb-on-demand-default-recommended
- dynamodb-ondemand-default-recommended-mode -> dynamodb-on-demand-default-recommended
- dynamodb-ondemand-double-previous-peak -> dynamodb-on-demand-previous-peak-double
- dynamodb-ondemand-throttle-30-minutes -> dynamodb-on-demand-throttle-if-double-within-30-min
- dynamodb-on-demand-zero-traffic-no-charge -> dynamodb-ondemand-billed-per-request-zero-traffic-free
- dynamodb-ondemand-zero-traffic-no-charge -> dynamodb-ondemand-billed-per-request-zero-traffic-free
- dynamodb-on-demand-billed-per-request -> dynamodb-ondemand-billed-per-request-zero-traffic-free
- dynamodb-pitr-recovery-period-default-35 -> dynamodb-pitr-35-days-default-1-to-35-configurable
- dynamodb-pitr-recovery-period-1-to-35 -> dynamodb-pitr-35-days-default-1-to-35-configurable
- dynamodb-pitr-35-days-per-second-granularity -> dynamodb-pitr-35-days-default-1-to-35-configurable
- dynamodb-pitr-no-performance-effect -> dynamodb-pitr-no-capacity-no-impact
- dynamodb-pitr-price-not-reduced-by-shorter-period -> dynamodb-pitr-shorter-period-same-price (identical quote)
- dynamodb-pricing-free-tier-200m-requests -> dynamodb-faq-free-tier-200m-requests (same sentence, FAQ kept)
- dynamodb-pricing-free-tier-first-25-gb-storage -> dynamodb-pricing-standard-free-25gb-storage
- dynamodb-provisioned-billed-on-provisioned-not-consumed -> dynamodb-provisioned-billing-basis
- dynamodb-provisioned-charged-for-provisioned-not-consumed -> dynamodb-provisioned-billing-basis
- dynamodb-provisioned-for-steady-predictable-workloads -> dynamodb-provisioned-fits-steady-forecastable (identical quote)
- dynamodb-reserved-capacity-provisioned-standard-only -> dynamodb-reserved-capacity-not-for-ia-on-demand (its replicated-WCU claim had no quote)
- dynamodb-reserved-capacity-savings -> dynamodb-reserved-capacity-terms-and-discount (quote is inside the kept fact's quote)
- dynamodb-streams-disabled-readable-24-hours -> dynamodb-streams-disabled-stream-readable-24h
- dynamodb-streams-log-24-hours -> dynamodb-stream-records-24-hours
- dynamodb-streams-record-appears-exactly-once -> dynamodb-streams-record-exactly-once
- dynamodb-streams-same-sequence-per-item -> dynamodb-streams-record-exactly-once
- dynamodb-streams-vs-kds-consumers -> dynamodb-streams-vs-kds-consumers-per-shard (same table row)
- dynamodb-streams-lambda-synchronous-invoke -> dynamodb-streams-consumers-flink-eventbridge-lambda
- dynamodb-table-class-standard-default-recommended -> dynamodb-table-class-default-standard (identical)
- dynamodb-table-class-standard-ia-50-percent-rule -> dynamodb-table-class-ia-threshold-50-percent (identical)
- dynamodb-standard-ia-lower-storage-higher-throughput-cost -> dynamodb-table-class-ia-60-lower-25-higher (same sentence; escaped tilde)
- dynamodb-table-class-standard-ia-storage-dominant -> dynamodb-table-class-standard-ia-lower-storage-cost
- dynamodb-transactwrite-aggregate-4mb -> dynamodb-transaction-max-data
- dynamodb-ttl-deletes-without-write-throughput -> dynamodb-ttl-deletes-within-days-no-wcu (identical)
- dynamodb-ttl-typically-few-days-any-time -> dynamodb-ttl-expired-items-deleted-at-any-time (identical)
- dynamodb-ttl-expired-items-deleted-free-delay -> dynamodb-ttl-deletes-within-days-no-wcu (bundle of kept sentences)
- dynamodb-ttl-epoch-seconds-format -> dynamodb-ttl-attribute-number-epoch-seconds
- dynamodb-warm-throughput-no-decrease -> dynamodb-warm-throughput-cannot-decrease (identical)
- dynamodb-warm-throughput-cannot-decrease-charged -> dynamodb-warm-throughput-cannot-decrease
- dynamodb-warm-throughput-default-no-cost -> dynamodb-warm-throughput-default-free-prewarm-charged (identical)
- dynamodb-warm-throughput-definition-prewarm -> dynamodb-warm-throughput-definition (product-launch claim had no quote)
- dynamodb-nosql-limited-query-ways-not-for-adhoc -> dynamodb-nosql-queries-efficient-in-limited-ways (ad hoc claim had no quote)
- dynamodb-sort-key-range-queries -> dynamodb-query-sort-key-range-operators (identical)
- dynamodb-query-needs-partition-key-value -> dynamodb-query-partition-key-equality-sort-key-optional
- dynamodb-wa-replicated-across-azs-durable -> dynamodb-data-on-ssd-multi-az
- dynamodb-faq-replica-names-single-vs-multi-account -> dynamodb-faq-multi-account-table-names
- dynamodb-gt-availability-99-999 -> dynamodb-gt-sla-99999-vs-single-region-9999 (product page; guide and SLA kept)
- dynamodb-global-tables-product-page-availability -> dynamodb-gt-sla-99999-vs-single-region-9999

## Scope, not conflict
- dynamodb-database-savings-plans-cover-dynamodb (up to 35%, plan-wide across database services) and dynamodb-faq-database-savings-plans-18-percent (up to 18% for DynamoDB usage, 1-year term): both kept, scope made explicit.
- dynamodb-global-table-replicas-share-name-key-data: same name holds for single-account global tables; multi-account replicas may use other names (dynamodb-faq-multi-account-table-names). Condition added.
- dynamodb-faq-global-tables-prerequisites: FAQ list (Streams, same name, same key, same write capacity) kept with condition single-account.

## hard
- Set hard true on the FAQ-lens capability and behavior facts that had hard false (can/supports claims), for consistency with the guide-lens facts. Case-study facts without numbers stay hard false.

## Displays
- Every number-free display over 8 words, or with Markdown emphasis, replaced by a verbatim phrase of at most 8 words of the same quote.
