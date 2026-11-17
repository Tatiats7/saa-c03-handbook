---
id: "27"
slug: aurora
title: Amazon Aurora
file: fast
tier: deep
domains: [2, 3, 4]
tasks: ["3.3", "4.3", "2.1", "2.2"]
services: [aurora, aurora-serverless]
minutes: {fast: 20, pass: 70, full: 160}
status: ready
updated: 2026-10-14
---

# Amazon Aurora

## Predict (1 min)
<!-- section: role=predict; route=fast; minutes=1 -->

**Predict 1.** An Aurora cluster has only one DB instance, and its storage keeps copies in three Availability Zones. If that DB instance fails, is the database back within seconds? <!-- gist-trap -->

**Predict 2.** Your company runs an Aurora global database in two Regions. Can an application in the second Region write to the database there?

**Predict 3.** An Aurora Serverless v2 database has no users at night. Do you still pay for its compute at night?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

In AWS CloudShell, without creating anything, find db.serverless among the instance classes. Then read the default Aurora PostgreSQL version and your DB cluster quota.

<!-- task:start id=aurora-t01 -->

Look

**It kills the belief.** "Aurora Serverless v2 is a separate database product with its own kind of cluster."

> **Cost:** $0.

**Permissions.** `rds:DescribeAccountAttributes`, `rds:DescribeDBEngineVersions`, `rds:DescribeOrderableDBInstanceOptions`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. Read your quota for DB clusters in this Region: how many you use, and the maximum.

   ```bash
   aws rds describe-account-attributes --query "AccountQuotas[?AccountQuotaName=='DBClusters'].[AccountQuotaName,Used,Max]" --output table
   ```

   Expect: One row: DBClusters, then Used and Max. Max is your quota of DB clusters in this Region. The default quota is 40 Aurora DB clusters, and you can ask AWS to raise it.

2. Read the default Aurora PostgreSQL version and its parameter group family. Aurora is a managed relational database engine, compatible with MySQL and PostgreSQL. This task uses PostgreSQL.

   ```bash
   aws rds describe-db-engine-versions --engine aurora-postgresql --default-only --query "DBEngineVersions[].[EngineVersion,DBParameterGroupFamily]" --output table
   ```

   Expect: One row: a version number, and a family name that starts with aurora-postgresql. The Try tasks of this chapter use the family again.

3. Store the same default version as APG_VERSION, for the next command.

   ```bash
   APG_VERSION=$(aws rds describe-db-engine-versions --engine aurora-postgresql --default-only --query DBEngineVersions[0].EngineVersion --output text)
   ```

   Expect: No output. APG_VERSION now holds the version number from the table above.

4. List the DB instance classes that this version offers in this Region. Look for db.serverless, the instance class of Aurora Serverless v2.

   ```bash
   aws rds describe-orderable-db-instance-options --engine aurora-postgresql --engine-version $APG_VERSION --query "OrderableDBInstanceOptions[].DBInstanceClass" --output text
   ```

   Expect: A long list of DB instance class names that start with db. One of them is db.serverless, in the same list as the classes of provisioned DB instances. Aurora Serverless v2 is an instance class, not a separate kind of cluster: one Aurora DB cluster can hold any combination of provisioned and serverless DB instances. If db.serverless is missing, this Region does not offer Aurora Serverless v2 for this version.

**Label.** checked against docs, not run in a real account. Checked 2026-10-14.

<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** Amazon Aurora is a [fully managed relational database engine](../facts/aurora.md#aurora-is-managed-relational-engine) for MySQL and PostgreSQL. DB instances share one volume that keeps [six copies](../facts/aurora.md#aurora-storage-six-copies-three-azs) of the data.

**The problem it solves.** RDS read replicas each copy all the data. In Aurora, the writer and its Aurora Replicas share one volume, so you can [add a DB instance quickly](../facts/aurora.md#aurora-add-instance-no-data-copy).

**Predict the picture.** Where do writes go, and where do Aurora Replicas read?

<details>
<summary>Show the picture</summary>

![A sequence with four participants: an application, the writer DB instance, the cluster volume in three Availability Zones, and an Aurora Replica. The application writes through the cluster endpoint, the writer stores the change in the volume, the replica reads the same volume for queries that come through the reader endpoint, and after a failure the replica becomes the writer.](../diagrams/svg/aurora-hero.svg)

**Figure.** Writes go through the writer into one volume with six copies, and the Aurora Replicas read that same volume.

1. The application sends writes to the cluster endpoint, which [connects to the current primary DB instance](../facts/aurora.md#aurora-cluster-endpoint-connects-to-current-primary).
2. Aurora [synchronously replicates the data across Availability Zones](../facts/aurora.md#aurora-synchronous-replication-to-six-storage-nodes) to [six storage nodes](../facts/aurora.md#aurora-synchronous-replication-to-six-storage-nodes).
3. Read-only connections use the reader endpoint, which spreads them among the Aurora Replicas.
4. Aurora Replicas [connect to the same storage volume](../facts/aurora.md#aurora-adding-replicas-read-same-volume-offload) as the writer, so no data is copied to them.
5. If the writer fails, Aurora [automatically fails over to an Aurora Replica](../facts/aurora.md#aurora-auto-failover-to-replica), and the cluster endpoint follows it.

</details>

> **Startup example:** Callvale's PostgreSQL database holds 1.2 TB, and 90% of queries are reads. At peak, the one read replica is 40 seconds behind. Callvale needs several replicas behind one endpoint, fast failover, and a path to a second Region.

## Words that go together (1 min)
<!-- section: role=words; route=fast; minutes=1 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| read replica (REP-lih-kuh) | **promote** a read replica | A copy of a database that serves read queries | Aurora Replica: reads the shared volume |
| fail over (FAYL OH-ver) | an **automatic** failover | Move the writer role to a replica | switchover: a planned move of a global database |
| scale out | scale out on a **metric** | Add more instances, here Aurora Replicas | scale up: a larger instance class |
| serverless | a serverless **option** | AWS manages the capacity inside a range you set | Aurora Serverless v1, an older product |
| recovery point objective | **meet** an RPO | RPO: the recent data, in time, the business accepts to lose | recovery time objective |
| recovery time objective | an RTO of **hours** | RTO: the longest downtime the business accepts | recovery point objective |
| Multi-AZ (MUL-tee ay-ZEE) | a Multi-AZ **deployment** | Copies of a resource in more than one Availability Zone, for availability | read replica: for read scaling; Aurora readers do both |

## Choose it or not (4 min)
<!-- section: role=choose; route=fast; minutes=4 -->

### Aurora RDS or DynamoDB

<!-- table: compare -->
| Question | Amazon Aurora | Amazon RDS | Amazon DynamoDB |
|---|---|---|---|
| Data model? | Relational, [compatible with MySQL and PostgreSQL](../facts/aurora.md#aurora-is-managed-relational-engine) | Relational, [six popular engines](../facts/rds.md#rds-decision-guide-rds-row) | [Key-value](../facts/dynamodb.md#dynamodb-decision-guide-key-value-session-store) database |
| Storage? | One volume with [six copies](../facts/aurora.md#aurora-storage-six-copies-three-azs), shared by all instances | [Amazon RDS uses EBS volumes](../facts/rds.md#rds-storage-ebs-striping) for each DB instance | Managed by AWS |
| Joins? | Yes: relational engines support [complex queries through joins](../facts/rds.md#rds-decision-guide-relational-joins) | Yes, the same | Removing joins is [at the heart of NoSQL data modeling](../facts/dynamodb.md#dynamodb-no-joins-heart-of-nosql-modeling) |

**Deciding question:** Does the data need SQL and joins, and must many replicas read it with almost no delay?

> **Exam trap:** Many think that DynamoDB fits joined relational data. Removing joins is [at the heart of NoSQL data modeling](../facts/dynamodb.md#dynamodb-no-joins-heart-of-nosql-modeling). Others keep all records in Amazon ElastiCache alone, an [ephemeral cache for frequently accessed data](../facts/dynamodb.md#dynamodb-decision-guide-elasticache-caching-layer). <!-- trap: aurora-trap-dynamodb-for-joins --> <!-- trap: aurora-trap-cache-as-database -->

### Aurora Replica RDS read replica or Multi-AZ standby

<!-- table: compare -->
| Question | Aurora Replica | RDS read replica | Multi-AZ DB instance standby |
|---|---|---|---|
| Where does its data come from? | The writer's own volume: replicas [connect to the same storage volume](../facts/aurora.md#aurora-adding-replicas-read-same-volume-offload) | Updates from the primary: RDS [copies them asynchronously to the read replica](../facts/rds.md#rds-read-replica-async-read-only) | A [synchronous standby replica in a different Availability Zone](../facts/rds.md#rds-multi-az-instance-standby-no-reads) |
| Serves reads? | Yes | Yes | No: [a Multi-AZ standby cannot serve read requests](../facts/rds.md#rds-faq-multiaz-standby-no-reads) |
| Takes over by itself? | Yes: Aurora [automatically fails over to an Aurora Replica](../facts/aurora.md#aurora-auto-failover-to-replica) | No: it [can be manually promoted](../facts/rds.md#rds-compare-failover-vs-promote) | Yes: [automatic failover to standby](../facts/rds.md#rds-compare-failover-vs-promote) |

**Deciding question:** Must the copy serve reads, take over by itself, or both?

> **Exam trap:** Many think that a low-priority promotion tier (a high tier number) stops a replica from ever becoming the writer. If the higher-priority replicas are unhealthy, Amazon RDS [will promote the lower priority replica](../facts/aurora.md#aurora-faq-low-priority-replica-still-promoted-if-needed). <!-- trap: aurora-trap-tier-blocks-promotion -->

### Provisioned instances or Aurora Serverless v2

<!-- table: compare -->
| Question | Provisioned instances | Aurora Serverless v2 |
|---|---|---|
| Which load fits? | Provisioned clusters are [suitable for steady workloads](../facts/aurora-serverless.md#aurora-serverless-provisioned-suited-to-steady-workloads) | [Variable or "spiky" workloads](../facts/aurora-serverless.md#aurora-serverless-choose-variable-spiky-workloads) |
| Unit of capacity? | The DB instance class [determines the computation and memory capacity](../facts/aurora.md#aurora-instance-class-determines-compute-memory) | Aurora capacity units (ACUs) of [approximately 2 gibibytes (GiB) of memory](../facts/aurora-serverless.md#aurora-serverless-acu-about-2-gib-memory) each |
| How is it billed? | Constant capacity that you size in advance | Charges are [measured in terms of ACU-hours](../facts/aurora-serverless.md#aurora-serverless-billing-unit-acu-hours) |

**Deciding question:** Can you predict the load well enough to choose an instance size in advance?

### Aurora Global Database or DynamoDB global tables

<!-- table: compare -->
| Question | Aurora Global Database | DynamoDB global tables |
|---|---|---|
| Which Regions accept writes? | One: [only the primary cluster performs write operations](../facts/aurora.md#aurora-global-db-only-primary-writes) | Every Region: [any global table replica](../facts/dynamodb.md#dynamodb-global-table-any-replica-serves-reads-writes) can [serve reads and writes](../facts/dynamodb.md#dynamodb-global-table-any-replica-serves-reads-writes) |
| After a Region outage? | You [perform a cross-Region failover](../facts/aurora.md#aurora-global-db-failover-cross-region-to-secondary) to a secondary cluster | [There is no need for a database failover](../facts/dynamodb.md#dynamodb-gt-multi-active-no-failover-needed) |
| Data model? | Relational, with SQL | Key-value |

**Deciding question:** Must every Region write as an equal writer, or is one writer Region enough?

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "read-heavy; replicas fall behind at peak" | Aurora Replicas behind the reader endpoint | replicas [connect to the same storage volume](../facts/aurora.md#aurora-adding-replicas-read-same-volume-offload) | key-value data without joins: Amazon DynamoDB |
| "unpredictable or spiky load" | Aurora Serverless v2 | it is meant for [variable or "spiky" workloads](../facts/aurora-serverless.md#aurora-serverless-choose-variable-spiky-workloads) | the load is steady for years: provisioned instances with Reserved Instances |
| "Region outage; RPO of seconds" | Aurora Global Database | replication latency is [typically under a second](../facts/aurora.md#aurora-global-replication-latency-under-1-second) | an RPO of hours at low cost: copy snapshots to the second Region |
| "low-latency reads around the world" | Aurora Global Database | it serves [low-latency read operations for applications](../facts/aurora.md#aurora-cmp-global-db-low-latency-reads-worldwide) | every Region must write as an equal writer: DynamoDB global tables |
| "fail over automatically within a minute" | an Aurora Replica in another Availability Zone | failover typically takes [less than 60 seconds](../facts/aurora.md#aurora-failover-time-with-replica-guide) | one instance only: recreation typically takes [less than 10 minutes](../facts/aurora.md#aurora-failover-time-without-replica) |
| "test on a copy of production data" | Aurora cloning | a clone [shares the same data pages as the original](../facts/aurora.md#aurora-clone-shares-data-pages-separate-volume) at first | the copy is for another Region: copy a snapshot |
| "undo a bad change; keep the same cluster" | Backtrack (Aurora MySQL) | it [rewinds the DB cluster in minutes](../facts/aurora.md#aurora-backtrack-in-minutes-no-new-cluster) | Aurora PostgreSQL, or created without Backtrack: a point-in-time restore to a new cluster |
| "I/O-intensive; unpredictable I/O costs" | Aurora I/O-Optimized | [no additional charges for read and write I/O](../facts/aurora.md#aurora-io-optimized-no-io-charges) | I/O is [less than 25%](../facts/aurora.md#aurora-standard-best-when-io-under-25-percent) of the spend: Aurora Standard |

### Traps

- **Wrong belief:** Each Aurora Replica keeps its own copy of the data. **Truth:** Aurora Replicas [connect to the same storage volume](../facts/aurora.md#aurora-adding-replicas-read-same-volume-offload) as the writer. <!-- trap: aurora-trap-replicas-copy-data -->
- **Wrong belief:** Writes can go to the reader endpoint, so the replicas share the write load. **Truth:** The cluster endpoint is [the only one that can perform write operations](../facts/aurora.md#aurora-cluster-endpoint-only-one-for-writes). <!-- trap: aurora-trap-writes-through-reader-endpoint -->
- **Wrong belief:** Every Region of an Aurora global database accepts writes. **Truth:** [Only the primary cluster performs write operations](../facts/aurora.md#aurora-global-db-only-primary-writes). <!-- trap: aurora-trap-global-all-regions-write -->
- **Wrong belief:** After an outage of the primary Region, you run a switchover. **Truth:** A switchover is for clusters [in a healthy state](../facts/aurora.md#aurora-global-db-switchover-healthy-only-unplanned-use-failover). A failover is how you [recover from an unplanned outage](../facts/aurora.md#aurora-global-db-failover-use-for-unplanned-outage). <!-- trap: aurora-trap-switchover-for-region-outage -->
- **Wrong belief:** You can encrypt an existing cluster by modifying it. **Truth:** Encryption needs a new cluster: [restore an unencrypted snapshot](../facts/aurora.md#aurora-encryption-cannot-convert-unencrypted-in-place) and [specify a KMS key when you restore](../facts/aurora.md#aurora-restore-unencrypted-snapshot-specify-kms-key). <!-- trap: aurora-trap-encrypt-existing-in-place -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2023-08-21) The planned Region move has a new name.<br>
> **Old:** [managed planned failover](../facts/aurora.md#aurora-change-global-failover-managed-unplanned).<br>
> **Now:** switchover. A new managed failover handles an outage, [in typically a minute](../facts/aurora.md#aurora-change-global-failover-managed-unplanned) in the announcement.<br>
> **The exam probably expects:** either name. Prefer an option that is right under both names.<br>
> **Status:** examinable.

> **Changed recently:** (2024-11-20) Aurora Serverless v2 can scale to zero.<br>
> **Old:** lowest capacity [0.5 ACUs](../facts/aurora-serverless.md#aurora-serverless-change-scale-to-zero).<br>
> **Now:** a minimum of [0 ACUs](../facts/aurora-serverless.md#aurora-serverless-change-scale-to-zero), so an idle instance can pause.<br>
> **The exam probably expects:** no pause. Prefer an option that is right under both values.<br>
> **Status:** examinable.

> **Changed recently:** (2025-03-31) Aurora Serverless v1 reached its end of support.<br>
> **Old:** end of support on [December 31, 2024](../facts/aurora-serverless.md#aurora-serverless-change-v1-deprecation-date-extended).<br>
> **Now:** v1 support ended on [March 31, 2025](../facts/aurora-serverless.md#aurora-serverless-change-v1-deprecation-date-extended). Use Aurora Serverless v2.<br>
> **The exam probably expects:** "Aurora Serverless" for either version. Choose by the feature the stem needs.<br>
> **Status:** examinable.

> **Changed recently:** (2026-02-18) New clusters come encrypted at rest.<br>
> **Old:** a cluster where you [did not opt in for encryption](../facts/aurora.md#aurora-change-default-encryption-new-clusters) stayed unencrypted.<br>
> **Now:** new clusters are [encrypted by default with an AWS owned key](../facts/aurora.md#aurora-change-default-encryption-new-clusters).<br>
> **The exam probably expects:** encryption as a step you choose.<br>
> **Status:** examinable.

## Check (2 min)
<!-- section: role=check; route=fast; minutes=2 -->

**Check 1.** A writer and its Aurora Replica both run in one Availability Zone. That zone fails. Is the database back within a minute?

<details>
<summary>Answer</summary>

No. You [manually create one or more new DB instances](../facts/aurora.md#aurora-single-az-cluster-create-instances-manually) in another zone.

**Predict 1:** No. Aurora recreates the instance, typically in [less than 10 minutes](../facts/aurora.md#aurora-failover-time-without-replica).

</details>

**Check 2.** An application sends an INSERT to the secondary cluster of an Aurora global database. What must be on?

<details>
<summary>Answer</summary>

Write forwarding: secondaries [with write forwarding enabled](../facts/aurora.md#aurora-write-forwarding-secondary-forward-sql-writes) [forward SQL statements that perform write operations](../facts/aurora.md#aurora-write-forwarding-secondary-forward-sql-writes) to the primary.

**Predict 2:** Not by itself: [only the primary cluster performs write operations](../facts/aurora.md#aurora-global-db-only-primary-writes). Write forwarding sends it to the primary.

</details>

**Check 3.** An Aurora Serverless v2 cluster with minimum capacity 0.5 ACUs is idle at night. Does it pause?

<details>
<summary>Answer</summary>

No. With a minimum [higher than zero ACUs](../facts/aurora-serverless.md#aurora-serverless-min-capacity-above-zero-no-pause), the instances do not pause.

**Predict 3:** Yes, unless you set the minimum capacity [for the cluster to zero ACUs](../facts/aurora-serverless.md#aurora-serverless-auto-pause-min-capacity-zero).

</details>

## Recap from memory (2 min)
<!-- section: role=recap; route=fast; minutes=2 -->

**Recap 1.** In the second compare table, where does each replica get its data?

<details>
<summary>Answer</summary>

Aurora Replica: the writer's volume. RDS read replica: RDS [copies them asynchronously to the read replica](../facts/rds.md#rds-read-replica-async-read-only).

</details>

**Recap 2.** In the signals table, what fits "unpredictable or spiky load", and what is its "But not if"?

<details>
<summary>Answer</summary>

Aurora Serverless v2; not if the load is steady for years: provisioned instances with Reserved Instances.

</details>

**Recap 3.** Which Region of an Aurora global database accepts writes?

<details>
<summary>Answer</summary>

The primary Region: [only the primary cluster performs write operations](../facts/aurora.md#aurora-global-db-only-primary-writes).

</details>
