---
id: "28"
slug: dynamodb
title: Amazon DynamoDB
file: fast
tier: deep
domains: [2, 3, 4]
tasks: ["3.3", "4.3", "2.2"]
services: [dynamodb, dax]
minutes: {fast: 20, pass: 74, full: 164}
status: ready
updated: 2026-10-14
---

# Amazon DynamoDB

## Predict (1 min)
<!-- section: role=predict; route=fast; minutes=1 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** A provisioned table uses only a fifth of its write capacity. Can writes to one popular item still be throttled? <!-- gist-trap -->

**Predict 2.** An application writes an item and reads it back immediately with a default GetItem call. Is the new value guaranteed?

**Predict 3.** A global table has replica tables in two Regions. Can an application write to the replica table in the second Region?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

In AWS CloudShell, read the throughput quotas of your account and of each new table, in two Regions. Quotas apply on a [per-Region basis](../facts/dynamodb.md#dynamodb-quotas-per-region) unless AWS says otherwise.

<!-- task:start id=dynamodb-t01 -->

Look

**It kills the belief.** "A DynamoDB table has no throughput limit."

> **Cost:** $0.

**Permissions.** `dynamodb:DescribeLimits`, `servicequotas:ListAWSDefaultServiceQuotas`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. Read the provisioned throughput quotas of your account in this Region: one pair for the whole account, and one pair for each new table.

   ```bash
   aws dynamodb describe-limits --output table
   ```

   Expect: Four numbers: AccountMaxReadCapacityUnits, AccountMaxWriteCapacityUnits, TableMaxReadCapacityUnits and TableMaxWriteCapacityUnits. With the default quotas, the two account values are 80,000 and the two table values are 40,000. You can ask AWS to raise each of them.

2. Run the same command for a second Region, <OTHER_REGION>. Choose a Region that you do not work in, for example eu-west-1.

   ```bash
   aws dynamodb describe-limits --region <OTHER_REGION> --output table
   ```

   Expect: The four numbers of that Region. Each Region shows its own set, because DynamoDB quotas apply per Region.

3. List the default DynamoDB quotas of this Region. Find the rows whose names hold the words throughput limit.

   ```bash
   aws service-quotas list-aws-default-service-quotas --service-code dynamodb --query "Quotas[].[QuotaName,Value,Adjustable]" --output table
   ```

   Expect: A table of quota names, default values, and True or False. True marks a quota that you can ask AWS to increase. In on-demand mode, the account has no account-level throughput quota, but each table has one: the default is 40,000 read request units and 40,000 write request units.

**Label.** checked against docs, not run in a real account. Checked 2026-10-14.

<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** Amazon DynamoDB is a **serverless** database for [key-value and document](../facts/dynamodb.md#dynamodb-key-value-and-document) data, with [single-digit millisecond performance at any scale](../facts/dynamodb.md#dynamodb-decision-guide-key-value-session-store).

**The problem it solves.** In a relational database, each client holds a connection, and updates to one row wait for its lock. [DynamoDB uses an HTTP API](../facts/lambda.md#lambda-ddb-http-api-no-connections) with no open connection, and a key hash spreads items over partitions.

**Predict the picture.** When an application writes one item, where does DynamoDB store it, and when does it say the write is safe?

<details>
<summary>Show the picture</summary>

![A sequence with four participants: an application, DynamoDB, one partition, and its copies in three Availability Zones. The application sends a write with the item's key. DynamoDB hashes the partition key and picks the partition. The partition stores the item in three zones. DynamoDB returns success. A later read is eventually consistent unless it asks for a strong read.](../diagrams/svg/dynamodb-hero.svg)

**Figure.** A write lands in the partition that the key's hash picks, and DynamoDB replicates it across three Availability Zones.

1. The application sends a write that holds the item's primary key.
2. DynamoDB feeds the partition key value into an [internal hash function](../facts/dynamodb.md#dynamodb-partition-key-hash-decides-partition), which [determines the partition](../facts/dynamodb.md#dynamodb-partition-key-hash-decides-partition).
3. DynamoDB synchronously replicates the item across [three Availability Zones](../facts/dynamodb.md#dynamodb-faq-sync-replication-three-azs).
4. When the write returns HTTP 200 (OK), it has been [durably persisted](../facts/dynamodb.md#dynamodb-successful-write-http-200-durable).
5. [Eventually consistent is the default](../facts/dynamodb.md#dynamodb-eventually-consistent-default) for a later read; a strongly consistent read returns the [most up-to-date data](../facts/dynamodb.md#dynamodb-consistentread-parameter).

</details>

> **Startup example:** Each call has one job record that the pipeline updates about 12 times. Writes are spiky, from 2 calls a minute at night to 40 at peak. The pipeline reads and writes by call ID and lists one customer's jobs by time. The pipeline needs no joins.

## Words that go together (1 min)
<!-- section: role=words; route=fast; minutes=1 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| partition key | **choose** a partition key | Its hash picks the item's partition | sort key |
| sort key | a sort key **condition** | Orders items with one partition key value | secondary index |
| eventually consistent (ih-VEN-choo-uh-lee) | an eventually consistent **read** | A read that can miss a recent write | strongly consistent read |
| read capacity unit | **provision** read capacity units | Read throughput unit in provisioned mode | read request unit (on-demand mode) |
| on-demand capacity mode | **switch** a table to on-demand capacity mode | Bills each request; no capacity plan | On-Demand Instance (Amazon EC2) |
| global secondary index | **add** a global secondary index | A second key to query the same items | local secondary index |
| global table | **add** a replica to a global table | Replica tables in several Regions, each accepting writes | Aurora Global Database |
| time to live | **enable** TTL on a table | A per-item expiry time; DynamoDB deletes the item later | deleting with a scheduled job |

## Choose it or not (4 min)
<!-- section: role=choose; route=fast; minutes=4 -->

### DynamoDB Aurora or RDS

<!-- table: compare -->
| Question | DynamoDB | Aurora or RDS |
|---|---|---|
| Which data model? | [Key-value](../facts/dynamodb.md#dynamodb-decision-guide-key-value-session-store) and document | Relational, with [complex queries through joins](../facts/dynamodb.md#dynamodb-decision-guide-aurora-relational-joins) and [full SQL support](../facts/dynamodb.md#dynamodb-decision-guide-rds-full-sql) |
| Joins? | No JOIN operator, [unlike relational databases](../facts/dynamodb.md#dynamodb-no-join-operator) | Yes |
| What do you pay for? | Each request in on-demand mode: [billed per read or write request](../facts/dynamodb.md#dynamodb-ondemand-billed-per-request-zero-traffic-free) | Database instances or serverless capacity, plus storage |

**Deciding question:** Are the access patterns known key lookups at any scale, or does the data need joins and ad hoc SQL?

### On-demand or provisioned capacity

<!-- table: compare -->
| Question | On-demand | Provisioned |
|---|---|---|
| Which traffic fits? | Unknown or spiky traffic: it can [handle fluctuating traffic](../facts/dynamodb.md#dynamodb-ondemand-better-for-fluctuating-traffic) | [Steady workloads with predictable growth](../facts/dynamodb.md#dynamodb-provisioned-fits-steady-forecastable) |
| What do you pay for? | Each request: [billed per read or write request](../facts/dynamodb.md#dynamodb-ondemand-billed-per-request-zero-traffic-free) | The [hourly read and write capacity you have provisioned](../facts/dynamodb.md#dynamodb-provisioned-billing-basis) |
| Long-term discount? | No reserved capacity: it is not for Standard-IA tables [or on-demand capacity mode](../facts/dynamodb.md#dynamodb-reserved-capacity-not-for-ia-on-demand) | Reserved capacity, [up to 54% off standard rates for a one-year term](../facts/dynamodb.md#dynamodb-reserved-capacity-terms-and-discount) |

**Deciding question:** Can you forecast the reads and writes per second well enough to pay for them in advance?

### Global or local secondary index

<!-- table: compare -->
| Question | Global secondary index | Local secondary index |
|---|---|---|
| Which key? | Any new key: its [index key schema can be different](../facts/dynamodb.md#dynamodb-gsi-key-schema-can-differ) | The [same partition key as the base table](../facts/dynamodb.md#dynamodb-lsi-same-partition-key), another sort key |
| When can you add it? | Later too: you can [add a new global secondary index](../facts/dynamodb.md#dynamodb-index-online-operations-gsi-vs-lsi) | Only at creation: it is [created when the table is created](../facts/dynamodb.md#dynamodb-lsi-created-with-table) |
| Strongly consistent reads? | No: queries [support eventual consistency only](../facts/dynamodb.md#dynamodb-index-read-consistency-gsi-vs-lsi) | Yes: [either eventual consistency or strong consistency](../facts/dynamodb.md#dynamodb-index-read-consistency-gsi-vs-lsi) |

**Deciding question:** Does the new query need a different partition key, or the same key with another sort order and strong reads?

### DAX or ElastiCache

<!-- table: compare -->
| Question | Amazon DynamoDB Accelerator (DAX) | Amazon ElastiCache |
|---|---|---|
| What does it cache? | DynamoDB reads; DAX is [API-compatible with DynamoDB](../facts/dax.md#dax-api-compatible-minimal-changes) | Many sources: a [front-end caching layer](../facts/elasticache.md#elasticache-faq-front-end-cache-for-rds-aurora-documentdb-dynamodb) for RDS, Aurora and DynamoDB |
| How much code changes? | [Only minimal functional changes](../facts/dax.md#dax-api-compatible-minimal-changes) | Your code reads and fills the cache |
| What happens to a write? | It is [first written to the DynamoDB table](../facts/dax.md#dax-write-through-both-table-and-dax), then to DAX | Your code decides |
| Queries beyond key-value access? | No | Yes: [ElastiCache (Redis OSS) supports advanced data structures](../facts/dax.md#dax-vs-elasticache-complex-queries) |

**Deciding question:** Is the cache only for DynamoDB reads, or also for other data and queries beyond key-value access?

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "unpredictable traffic; a new application; pay only per request" | on-demand capacity mode | [on-demand capacity mode is the better choice](../facts/dynamodb.md#dynamodb-ondemand-better-for-fluctuating-traffic) | steady load for years: provisioned plus reserved capacity, for [consistent or predictable traffic](../facts/dynamodb.md#dynamodb-faq-provisioned-for-predictable) |
| "microsecond reads; the same items read again and again" | DAX | it serves [eventually consistent data](../facts/dax.md#dax-eventually-consistent-microsecond-latency) [with microsecond latency](../facts/dax.md#dax-eventually-consistent-microsecond-latency) | strong reads: read the table; [DAX passes strongly consistent read requests to DynamoDB](../facts/dax.md#dax-passes-through-strong-reads-and-transactions) |
| "delete old items automatically; expire sessions; no extra cost" | time to live (TTL) | it deletes items [without consuming any write throughput](../facts/dynamodb.md#dynamodb-faq-ttl-no-write-throughput) | exact expiry: filter on read; deletion [within a few days of their expiration time](../facts/dynamodb.md#dynamodb-ttl-deletes-within-days-no-wcu) |
| "multi-Region, active-active; users write in their own Region" | DynamoDB global tables | [any global table replica](../facts/dynamodb.md#dynamodb-global-table-any-replica-serves-reads-writes) can [serve reads and writes](../facts/dynamodb.md#dynamodb-global-table-any-replica-serves-reads-writes) | relational data with joins: Aurora Global Database; [only the primary cluster performs write operations](../facts/dynamodb.md#dynamodb-vs-aurora-global-database-single-writer) |
| "run code when an item changes" | DynamoDB Streams with a Lambda trigger | the stream has a [native integration with AWS Lambda](../facts/dynamodb.md#dynamodb-faq-streams-lambda-triggers) | replay for days: Kinesis Data Streams for DynamoDB, [up to 1 year](../facts/dynamodb.md#dynamodb-streams-vs-kds-retention) |
| "private subnets, no NAT gateway" | a gateway endpoint | [without requiring an internet gateway or NAT device](../facts/dynamodb.md#dynamodb-faq-gateway-endpoint-no-igw-nat) | on premises: [you must use AWS PrivateLink](../facts/dynamodb.md#dynamodb-faq-gateway-endpoint-limits-use-privatelink) |
| "storage is most of the bill" | the Standard-IA table class | [Standard-IA tables have lower storage costs](../facts/dynamodb.md#dynamodb-faq-table-class-cost-tradeoff) | heavy reads and writes: Standard has [lower costs for reads and writes](../facts/dynamodb.md#dynamodb-faq-table-class-cost-tradeoff) |
| "query by an attribute that is not the key" | a global secondary index | its [index key schema can be different](../facts/dynamodb.md#dynamodb-gsi-key-schema-can-differ) | strong reads, same partition key: a local secondary index, [created when the table is created](../facts/dynamodb.md#dynamodb-lsi-created-with-table) |

### Traps

- **Wrong belief:** If the table has unused capacity, no request is throttled. **Truth:** Each partition delivers at most [1,000 write units per second](../facts/dynamodb.md#dynamodb-partition-max-throughput), so one hot key meets **throttling** and other partitions stay idle. <!-- trap: dynamodb-trap-spare-capacity-no-throttle -->
- **Wrong belief:** A read right after a write returns the new value. **Truth:** [Eventually consistent is the default](../facts/dynamodb.md#dynamodb-eventually-consistent-default) for every read. Set `ConsistentRead` to true to get the latest data. <!-- trap: dynamodb-trap-default-read-is-latest -->
- **Wrong belief:** Time to live deletes an item at the second it expires. **Truth:** DynamoDB deletes expired items [within a few days of their expiration time](../facts/dynamodb.md#dynamodb-ttl-deletes-within-days-no-wcu). Unless you filter them, expired items [continue to show in read and write operations](../facts/dynamodb.md#dynamodb-ttl-expired-items-visible-until-deleted). <!-- trap: dynamodb-trap-ttl-deletes-on-time -->
- **Wrong belief:** DAX speeds up every read, strongly consistent reads included. **Truth:** [DAX passes strongly consistent read requests to DynamoDB](../facts/dax.md#dax-passes-through-strong-reads-and-transactions), and [it does not cache the results](../facts/dax.md#dax-passes-through-strong-reads-and-transactions). <!-- trap: dynamodb-trap-dax-speeds-every-read -->
- **Wrong belief:** A global table has a primary Region, and a Region outage needs a database failover. **Truth:** A global table has [no primary Region](../facts/dynamodb.md#dynamodb-faq-global-tables-no-failover-needed), so the application sends its writes to a replica table in a healthy Region. <!-- trap: dynamodb-trap-global-table-primary-region -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2024-11-01) On-demand prices fell.<br>
> **Old:** on-demand was [cost effective for spiky workloads](../facts/dynamodb.md#dynamodb-change-ondemand-price-cut-2024-11).<br>
> **Now:** most provisioned workloads [achieve a lower price with on-demand mode](../facts/dynamodb.md#dynamodb-change-ondemand-price-cut-2024-11).<br>
> **The exam probably expects:** on-demand for spiky, provisioned for steady traffic. Choose an answer that is right under old and new prices.<br>
> **Status:** examinable.

> **Changed recently:** (2025-08-12) Switches from provisioned to on-demand mode.<br>
> **Old:** [once every 24 hours](../facts/dynamodb.md#dynamodb-change-capacity-mode-switch-limit-2025-08).<br>
> **Now:** [four times every 24 hours](../facts/dynamodb.md#dynamodb-change-capacity-mode-switch-limit-2025-08).<br>
> **The exam probably expects:** the old value. Do not let the count decide an answer.<br>
> **Status:** examinable.

> **Changed recently:** (2025-11-19) Attributes per global secondary index key.<br>
> **Old:** [limited to one attribute each](../facts/dynamodb.md#dynamodb-change-gsi-multi-attribute-keys-2025-11).<br>
> **Now:** [up to four attributes each](../facts/dynamodb.md#dynamodb-change-gsi-multi-attribute-keys-2025-11).<br>
> **The exam probably expects:** one attribute per key. Do not let the count decide an answer.<br>
> **Status:** examinable.

> **Changed recently:** (2024-03-19) Interface endpoints for DynamoDB.<br>
> **Old:** a gateway endpoint, for traffic from a VPC.<br>
> **Now:** also [interface VPC endpoints and private IP addresses](../facts/dynamodb.md#dynamodb-faq-privatelink-interface-endpoints) ([March 19, 2024](../facts/dynamodb.md#dynamodb-change-privatelink-interface-endpoints-2024-03)).<br>
> **The exam probably expects:** gateway endpoint in a VPC; interface endpoint from on premises.<br>
> **Status:** examinable.

## Check (2 min)
<!-- section: role=check; route=fast; minutes=2 -->

**Check 1.** A table's partition key is `country`, and most users live in one country. The table has spare write capacity. Can those writes be throttled?

<details>
<summary>Answer</summary>

Yes. A key with a [small number of partition key values](../facts/dynamodb.md#dynamodb-few-partition-keys-spread-writes) creates ["hot" partitions that result in throttling](../facts/dynamodb.md#dynamodb-hot-partitions-cause-throttling).

**Predict 1:** Yes. One partition delivers at most [1,000 write units per second](../facts/dynamodb.md#dynamodb-partition-max-throughput).

</details>

**Check 2.** A function writes an order, and the next function reads it through a global secondary index. Can that read be strongly consistent?

<details>
<summary>Answer</summary>

No. Queries on a global secondary index [support eventual consistency only](../facts/dynamodb.md#dynamodb-index-read-consistency-gsi-vs-lsi).

**Predict 2:** No. [Eventually consistent is the default](../facts/dynamodb.md#dynamodb-eventually-consistent-default).

</details>

**Check 3.** Users in us-east-1 and eu-west-1 change the same item almost at the same time. The global table has default settings. Which change remains?

<details>
<summary>Answer</summary>

The later one: by default, [last writer wins](../facts/dynamodb.md#dynamodb-gt-mrec-default-last-writer-wins).

**Predict 3:** Yes. [Any global table replica](../facts/dynamodb.md#dynamodb-global-table-any-replica-serves-reads-writes) can [serve reads and writes](../facts/dynamodb.md#dynamodb-global-table-any-replica-serves-reads-writes).

</details>

## Recap from memory (2 min)
<!-- section: role=recap; route=fast; minutes=2 -->

**Recap 1.** What does each capacity mode bill for?

<details>
<summary>Answer</summary>

On-demand: each request, [billed per read or write request](../facts/dynamodb.md#dynamodb-ondemand-billed-per-request-zero-traffic-free). Provisioned: the [hourly read and write capacity you have provisioned](../facts/dynamodb.md#dynamodb-provisioned-billing-basis).

</details>

**Recap 2.** In the signals table, what fits "run code when an item changes", and its "But not if"?

<details>
<summary>Answer</summary>

DynamoDB Streams with a Lambda trigger. Not if replay is needed: Kinesis Data Streams for DynamoDB, [up to 1 year](../facts/dynamodb.md#dynamodb-streams-vs-kds-retention).

</details>

**Recap 3.** When does time to live delete an expired item?

<details>
<summary>Answer</summary>

[Within a few days of their expiration time](../facts/dynamodb.md#dynamodb-ttl-deletes-within-days-no-wcu).

</details>
