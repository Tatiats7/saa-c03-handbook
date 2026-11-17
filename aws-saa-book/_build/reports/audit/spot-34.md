# Spot check spot-34: chapter 34 (Kinesis Data Streams, Data Firehose and MSK)

Date: 2026-10-14 (ledger clock 2026-10-15). Checker: Opus spot check after the first entail vote round, before adjudication.
Pool: 642 facts with home_chapter 34 and status mech-pass in kinesis-data-streams, data-firehose and msk. Seed 20261013 + 34 = 20261047; 30 picked with `random.Random(seed).sample` over the sorted ids. Sample file: `spot-34.sample.json`.

## Result

- Checked: 30
- Not positive (my verdict partial or unsure): 9, all partial
- Voter misses (first-round entail vote `support`, my verdict not positive): 2
- Partials the first-round voter had already caught: 7
- Amended: 9 (all with `--by spot-34`; each now mech-pass at a new rev with no votes, for a fresh vote at adjudication)

## Sample and verdicts

| # | Fact | First-round entail | Spot verdict |
|---|------|--------------------|--------------|
| 1 | data-firehose-s3-batches-records-add-separator | support | support |
| 2 | msk-api-interface-endpoint-privatelink | support | support |
| 3 | msk-replicator-fully-managed-cross-region-and-same-region | support | support |
| 4 | data-firehose-cross-account-and-cross-region-http-delivery | partial | partial |
| 5 | kinesis-data-streams-retention-minimum-24-hours | support | support |
| 6 | kinesis-data-streams-faq-retention-long-term-up-to-365-days | partial | partial |
| 7 | kinesis-data-streams-faq-put-temporary-retry-sustained-add-shards | partial | partial |
| 8 | kinesis-data-streams-faq-warm-throughput-update-api | partial | partial |
| 9 | data-firehose-direct-put-throughput-quota | partial | partial |
| 10 | data-firehose-change-snowflake-ga-2024-04 | support | support |
| 11 | data-firehose-http-endpoint-in-vpc-not-supported | support | support |
| 12 | data-firehose-getrecords-once-per-second-per-shard | support | support |
| 13 | data-firehose-dynamic-partitioning-500-active-partitions | support | **partial (voter miss)** |
| 14 | kinesis-data-streams-kcl-child-shards-after-parent | support | support |
| 15 | kinesis-data-streams-faq-provisioned-pricing-hourly-shard-plus-records | support | support |
| 16 | kinesis-data-streams-security-use-iam-roles-not-stored-credentials | support | support |
| 17 | kinesis-data-streams-faq-sse-is-stream-specific | support | support |
| 18 | msk-pricing-serverless-dimensions | partial | partial |
| 19 | msk-tiered-storage-minimum-retention-3-days | support | support |
| 20 | data-firehose-change-cloudwatch-logs-decompression-2023-12 | support | support |
| 21 | msk-change-express-brokers-added-2024-11 | support | support |
| 22 | msk-tiered-storage-compatible-with-existing-kafka-apis | support | support |
| 23 | kinesis-data-streams-change-service-managed-partition-keys-2026-09 | support | support |
| 24 | kinesis-data-streams-retention-decrease-hides-old-records-immediately | support | support |
| 25 | data-firehose-format-conversion-other-formats-via-lambda | support | support |
| 26 | kinesis-data-streams-case-iccw-kds-firehose-lambda-s3 | partial | partial |
| 27 | kinesis-data-streams-provisioned-for-predictable-traffic | support | support |
| 28 | kinesis-data-streams-faq-secure-by-default-owners-only | support | **partial (voter miss)** |
| 29 | kinesis-data-streams-faq-s3-general-purpose-delivery | support | support |
| 30 | msk-runs-open-source-kafka-no-code-changes | support | support |

## Non-positive verdicts, with reasons and repairs

1. **data-firehose-dynamic-partitioning-500-active-partitions** (voter miss). The qualifiers say the 500 limit is a default that can be raised up to 2500 with the Limits form, but that stands only in the next sentence, outside the quote. Amended (rev 2): quote extended verbatim with the Limits-form sentence; claim states the increase up to 2500; added display "up to 2500 active partitions".
2. **kinesis-data-streams-faq-secure-by-default-owners-only** (voter miss). "Only the account and data stream owners have access" is a universal statement whose exception (IAM policies selectively grant permissions to users and groups) stands two sentences later in the same answer. Amended (rev 2): quote extended through the IAM sentence; claim adds it; qualifiers mark the owner-only access as the default.
3. **data-firehose-cross-account-and-cross-region-http-delivery** (voter caught). "For these scenarios" sits in the cross-Region paragraph; the claim extended the data transfer charge to the cross-account case. Amended (rev 3): claim limits the charge to cross-Region and outside-AWS delivery; quotes split to stay within 80 words.
4. **kinesis-data-streams-faq-retention-long-term-up-to-365-days** (voter caught). Qualifiers said adjustable true and per data stream; the quote gives a fixed 365-day maximum. Amended (rev 2): adjustable false, scope names the FAQ question, condition "greater than seven days".
5. **kinesis-data-streams-faq-put-temporary-retry-sustained-add-shards** (voter caught). The quote starts "If this is due to"; the provisioned-mode scope and the ProvisionedThroughputExceeded rejection stand in the preceding sentences. Amended (rev 2): added the preceding sentences as a second quote; claim and qualifiers scoped to provisioned mode.
6. **kinesis-data-streams-faq-warm-throughput-update-api** (voter caught). The scope (on-demand stream, On-demand Advantage heading) stood only in the previous sentence and heading; the claim said any existing data stream. Amended (rev 2): quote extended with the previous sentence; claim and scope name on-demand streams in On-demand Advantage mode.
7. **data-firehose-direct-put-throughput-quota** (voter caught). The quotes gave the values but not "default", the request path, the proportional scaling or the Kinesis Data Streams source exception that the qualifiers state; the automatic throughput increase on throttling stood nearby. Amended (rev 3): added four verbatim quotes from the same page (automatic increase, request an increase, proportional scaling, KDS source exception); claim states them.
8. **msk-pricing-serverless-dimensions** (voter caught). The qualifier condition on data transfer charges stood only in the next sentence. Amended (rev 3): added that sentence as a quote and to the claim.
9. **kinesis-data-streams-case-iccw-kds-firehose-lambda-s3** (voter caught). The full name and the soil and water quality purpose stood only in the surrounding text; "including" was narrowed to "on". Amended (rev 2): added the purpose sentence, the extended solution sentence and the "About ICCW" sentence; claim says "based on AWS services including".

## Notes

- Positive but noted, not amended: msk-tiered-storage-minimum-retention-3-days has the qualifier scope "per topic", which the page does not state; the claim and value are fully carried by the quote and the page title gives the Standard-broker scope.
- Flag rule (voter misses only): 2 of 30, below the flag threshold of 3.
- Patch files: `_build/work/34-streaming/spot-34/*.json`.
