---
id: "26"
slug: rds
title: Amazon RDS
file: fast
tier: deep
domains: [1, 2, 3, 4]
tasks: ["2.1", "2.2", "3.3", "4.3", "4.1", "1.3"]
services: [rds, rds-proxy]
minutes: {fast: 20, pass: 46, full: 79}
status: ready
updated: 2026-10-14
---

# Amazon RDS

## Predict (1 min)
<!-- section: role=predict; route=fast; minutes=1 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** A **Multi-AZ** (MUL-tee ay-ZEE) deployment keeps a second copy of your database in another **Availability Zone** (AZ). Can your reporting queries read from that second copy? <!-- gist-trap -->

**Predict 2.** An engineer deletes a table by mistake at 10:00. Can Amazon RDS give you the database as it was at 09:55?

**Predict 3.** Hundreds of short-lived functions each open a database connection at the same moment. What runs out first on the database: CPU, storage or connections?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

In AWS CloudShell, read three things without creating anything. Read your DB instance quota, the default PostgreSQL version, and whether a small instance class can run Multi-AZ and read replicas.

<!-- task:start id=rds-t01 -->

Look

**It kills the belief.** "Amazon RDS is a database that you install and configure yourself on a server."

> **Cost:** $0.

**Permissions.** `rds:DescribeAccountAttributes`, `rds:DescribeDBEngineVersions`, `rds:DescribeOrderableDBInstanceOptions`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. Read your quota for DB instances in this Region: how many you use, and the maximum.

   ```bash
   aws rds describe-account-attributes --query "AccountQuotas[?AccountQuotaName=='DBInstances'].[AccountQuotaName,Used,Max]" --output table
   ```

   Expect: One row: DBInstances, then Used and Max. Max is your quota. The default quota is 40 in most Regions and 20 in ap-south-1, and you can ask AWS to raise it.

2. Read the default PostgreSQL version and its parameter group family. PostgreSQL is one of six RDS engines, next to IBM Db2, MariaDB, Microsoft SQL Server, MySQL and Oracle Database.

   ```bash
   aws rds describe-db-engine-versions --engine postgres --default-only --query "DBEngineVersions[].[EngineVersion,DBParameterGroupFamily]" --output table
   ```

   Expect: One row: a version number, and a family name that starts with postgres. The parameter group task of this chapter uses the family name again.

3. Store the same default version as PG_VERSION, for the next command.

   ```bash
   PG_VERSION=$(aws rds describe-db-engine-versions --engine postgres --default-only --query DBEngineVersions[0].EngineVersion --output text)
   ```

   Expect: No output. PG_VERSION now holds the version number from the table above.

4. Ask what a small instance class, db.t4g.micro, offers with this version. Look for Multi-AZ and read replicas.

   ```bash
   aws rds describe-orderable-db-instance-options --engine postgres --engine-version $PG_VERSION --db-instance-class db.t4g.micro --query "OrderableDBInstanceOptions[].[StorageType,MultiAZCapable,ReadReplicaCapable]" --output table
   ```

   Expect: One row or more, one for each storage type, with True or False for Multi-AZ and for read replicas. True means that you turn the feature on as a setting of the DB instance. You install no database software: Amazon RDS manages backups, software patching, failure detection and recovery. If the table is empty, run the command again with db.t3.micro.

**Label.** checked against docs, not run in a real account. Checked 2026-10-14.

<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** Amazon RDS is a [fully managed relational database](../facts/rds.md#rds-decision-guide-rds-row) for [six popular engines](../facts/rds.md#rds-decision-guide-rds-row). AWS [manages backups, software patching](../facts/rds.md#rds-managed-tasks) and failure recovery.

**The problem it solves.** A database on your own instance needs patches, backups and a plan for failures. Amazon RDS moves that routine work to AWS, and you keep the schema and the queries.

**Predict the picture.** When an application writes to a Multi-AZ database, where does the write go, and where do the backups go?

<details>
<summary>Show the picture</summary>

![A sequence with four participants: an application, a primary DB instance, a standby DB instance in another Availability Zone, and Amazon S3. The application writes to the primary, the primary copies the write to the standby, backups go from the standby to Amazon S3, and after a failure the application reconnects to the standby.](../diagrams/svg/rds-hero.svg)

**Figure.** Each write reaches a standby in another zone, backups go to Amazon S3, and a failover moves the same name to the standby.

1. The application connects by DNS name and sends a write to the primary DB instance.
2. The write is [concurrent on the primary and standby](../facts/rds.md#rds-faq-multiaz-replication-synchronous), which runs in another Availability Zone.
3. RDS [automated backups are taken from standby](../facts/rds.md#rds-compare-backups) and [stored in S3](../facts/rds.md#rds-faq-backups-stored-in-s3).
4. If the primary fails, RDS [changes the Domain Name System (DNS) record](../facts/rds.md#rds-multi-az-failover-dns-change-reconnect) to point to the standby.
5. The application must [re-establish any existing connections](../facts/rds.md#rds-multi-az-failover-dns-change-reconnect), now to the new primary.

</details>

> **Startup example:** Callvale runs PostgreSQL on one EC2 instance. Ben applies patches and checks backups by hand. If the instance or its Availability Zone fails, the application stops until Ben restores a snapshot. Callvale needs automatic failover and automatic backups without changes to the application.

## Words that go together (1 min)
<!-- section: role=words; route=fast; minutes=1 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| Multi-AZ (MUL-tee ay-ZEE) | a Multi-AZ **deployment** | A second copy of the database in another Availability Zone | read replica |
| standby | **fail** over to the standby | The copy that waits to take over when the primary fails | read replica |
| fail over (FAYL OH-ver) | an **automatic** failover | Move the work from a failed primary to the standby | roll back |
| read replica (REP-lih-kuh) | **promote** a read replica | A copy of the database that serves read queries | standby |
| RDS Proxy | **pool** connections through RDS Proxy | A managed proxy that shares database connections among many clients | read replica |
| snapshot | **restore** from a snapshot | A point-in-time copy of a database | read replica |
| retention period | **during** the retention period | How long RDS keeps the automated backups | backup window |
| managed service | a **fully** managed service | A service where AWS does the operating work | serverless |

## Choose it or not (4 min)
<!-- section: role=choose; route=fast; minutes=4 -->

### Multi-AZ DB instance or Multi-AZ DB cluster or read replica

<!-- table: compare -->
| Question | Multi-AZ DB instance | Multi-AZ DB cluster | Read replica |
|---|---|---|---|
| Main purpose? | [Main purpose is high availability](../facts/rds.md#rds-compare-purpose-ha-dr-scale) | High availability with [increased capacity for read workloads](../facts/rds.md#rds-multi-az-cluster-benefits) | [Main purpose is scalability](../facts/rds.md#rds-compare-purpose-ha-dr-scale) |
| Replication? | [Synchronous replication](../facts/rds.md#rds-compare-replication-sync-async) | [Semisynchronous replication](../facts/rds.md#rds-multi-az-cluster-semisynchronous) | [Asynchronous replication](../facts/rds.md#rds-compare-replication-sync-async) |
| Serves reads? | No: [a Multi-AZ standby cannot serve read requests](../facts/rds.md#rds-faq-multiaz-standby-no-reads) | Yes: [all three DB instances can serve read traffic](../facts/rds.md#rds-multi-az-cluster-three-azs-all-read) | Yes: [read-only access to the replica](../facts/rds.md#rds-read-replica-async-read-only) |
| Failover? | Automatic, typically [60–120 seconds](../facts/rds.md#rds-multi-az-instance-failover-time) | Automatic, typically [under 35 seconds](../facts/rds.md#rds-multi-az-cluster-failover-time) | By hand: it [can be manually promoted](../facts/rds.md#rds-compare-failover-vs-promote) |

**Deciding question:** Must the database survive a zone failure, serve more reads, or do both?

### Amazon RDS or RDS Custom or a database on Amazon EC2

<!-- table: compare -->
| Question | Amazon RDS | RDS Custom | Database on Amazon EC2 |
|---|---|---|---|
| Host access? | No: for that, RDS Custom lets you [customize your database environment and operating system](../facts/rds.md#rds-custom-os-access) | Yes: [Amazon RDS Custom is the better choice](../facts/rds.md#rds-custom-vs-rds-vs-ec2) for administrative rights | Full: you [manage your own relational database](../facts/rds.md#rds-faq-rds-vs-ec2-ami) |
| Backups and patching? | AWS [manages backups, software patching](../facts/rds.md#rds-managed-tasks) | AWS automates the administration tasks | You own [upgrades, patches, backups, capacity planning](../facts/rds.md#rds-decision-guide-rehost-ec2-tasks) |
| Fits? | The [default choice for most relational database deployments](../facts/rds.md#rds-default-choice-relational) | Legacy, custom and packaged applications | Teams that want full management responsibility |

**Deciding question:** Who runs the operating system of the database host, AWS or your team?

### Amazon RDS or Amazon Aurora or Amazon DynamoDB

<!-- table: compare -->
| Question | Amazon RDS | Amazon Aurora | Amazon DynamoDB |
|---|---|---|---|
| Data model? | Relational, with [complex queries through joins](../facts/rds.md#rds-decision-guide-relational-joins) | Relational: a [fully managed relational database service](../facts/aurora.md#aurora-faq-what-is-aurora) | [Both key-value and document data models](../facts/dynamodb.md#dynamodb-key-value-and-document) |
| Engines or software? | [Six popular engines](../facts/rds.md#rds-decision-guide-rds-row) | MySQL and PostgreSQL compatible | No need to [patch, manage, install, maintain, or operate any software](../facts/dynamodb.md#dynamodb-serverless-no-servers) |
| Storage? | [Amazon RDS uses EBS volumes](../facts/rds.md#rds-storage-ebs-striping) | [Six copies](../facts/aurora.md#aurora-storage-six-copies-three-azs) of the data across [three AZs](../facts/aurora.md#aurora-storage-six-copies-three-azs) | Managed by AWS |
| Read scaling? | [Up to 15 read replicas](../facts/rds.md#rds-change-read-replicas-15-2022-10) on MariaDB, MySQL and PostgreSQL | Aurora Replicas behind a reader endpoint | [Single-digit millisecond performance](../facts/dynamodb.md#dynamodb-intro-single-digit-ms-any-scale) at any scale |

**Deciding question:** Does the data need SQL and joins, and has it outgrown one RDS DB instance and its replicas?

Chapter 27 teaches Aurora and chapter 28 teaches DynamoDB in depth. <!-- xref: 27 Aurora cluster storage and Aurora Replicas --> <!-- xref: 28 DynamoDB key-value design -->

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "highly available, automatic failover, survive an AZ failure" | Multi-AZ DB instance deployment | it protects against [DB instance failure and Availability Zone disruption](../facts/rds.md#rds-multi-az-instance-protects-az-disruption) | the standbys must also serve reads: a Multi-AZ DB cluster (MySQL or PostgreSQL) |
| "read-heavy, reporting slows production" | read replica | it serves [business reporting or data warehousing scenarios](../facts/rds.md#rds-read-replica-use-reporting) | the goal is write availability: Multi-AZ, with [automatic failover to standby](../facts/rds.md#rds-compare-failover-vs-promote) |
| "disaster recovery in another Region" | cross-Region read replica | it helps [improve your disaster recovery capabilities.](../facts/rds.md#rds-cross-region-replica-use-cases) | a slower restore is acceptable: cross-Region automated backups |
| "too many connections, Lambda functions" | RDS Proxy | it keeps a [smaller number of long-lived connections](../facts/rds-proxy.md#rds-proxy-candidate-too-many-connections) | reads drive the CPU and connections are few: a read replica |
| "unpredictable storage growth" | storage autoscaling | [it automatically scales up your storage](../facts/rds.md#rds-storage-autoscaling-unpredictable) | a large one-time data load: allocate the storage first |
| "recover from an accidental delete" | point-in-time restore | it restores [within your backup retention period](../facts/rds.md#rds-pitr-new-instance-within-retention) by [creating a new DB instance](../facts/rds.md#rds-pitr-new-instance-within-retention) | the copy must stay for years: a manual snapshot |
| "access to the operating system" | Amazon RDS Custom | you [customize your database environment and operating system](../facts/rds.md#rds-custom-os-access) | RDS Custom does not run your engine: Amazon EC2 |
| "encrypt an existing unencrypted database" | snapshot, encrypted copy, restore | you [encrypt a copy of an unencrypted snapshot](../facts/rds.md#rds-encrypt-existing-via-snapshot-copy) | the data in transit needs encryption: [Transport Layer Security (TLS)](../facts/rds.md#rds-tls-all-engines) |

### Traps

- **Wrong belief:** The Multi-AZ standby serves reads. **Truth:** [A Multi-AZ standby cannot serve read requests](../facts/rds.md#rds-faq-multiaz-standby-no-reads). For reads, [use a Multi-AZ DB cluster](../facts/rds.md#rds-multi-az-instance-not-read-scaling) or a read replica. <!-- trap: rds-trap-standby-serves-reads -->
- **Wrong belief:** The standby is a backup that brings back a deleted table. **Truth:** Writes are [concurrent on the primary and standby](../facts/rds.md#rds-faq-multiaz-replication-synchronous), so the delete reaches both. Use [point-in-time recovery](../facts/rds.md#rds-faq-automated-backups-enable-pitr). <!-- trap: rds-trap-multi-az-is-a-backup -->
- **Wrong belief:** You can encrypt an existing DB instance by modifying it. **Truth:** You can [only encrypt an Amazon RDS DB instance](../facts/rds.md#rds-encryption-only-at-create) when you create it. [Encrypt a copy of an unencrypted snapshot](../facts/rds.md#rds-encrypt-existing-via-snapshot-copy), then [restore an encrypted DB instance](../facts/rds.md#rds-encrypt-existing-via-snapshot-copy). Or [use a blue/green deployment](../facts/rds.md#rds-encryption-blue-green-change-key). <!-- trap: rds-trap-encrypt-existing-in-place -->
- **Wrong belief:** Automated backups stay after you delete the DB instance. **Truth:** Unless you retain them, [all automated backups are deleted](../facts/rds.md#rds-delete-instance-automated-backups-deleted). [Manual snapshots are not deleted](../facts/rds.md#rds-delete-instance-automated-backups-deleted), so take a final snapshot. <!-- trap: rds-trap-automated-backups-survive-delete -->
- **Wrong belief:** Amazon RDS lets you log in to the database host. **Truth:** Standard RDS gives no host access; RDS Custom lets you [customize your database environment and operating system](../facts/rds.md#rds-custom-os-access). If RDS Custom does not run your engine, use Amazon EC2. <!-- trap: rds-trap-rds-gives-os-access -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2025-09-23) Snapshot copy to another Region and another account.<br>
> **Old:** a [two step process](../facts/rds.md#rds-change-cross-region-cross-account-snapshot-copy-2025-09).<br>
> **Now:** one copy, [without performing it sequentially as two separate copies](../facts/rds.md#rds-change-cross-region-cross-account-snapshot-copy-2025-09).<br>
> **The exam probably expects:** two copies in older questions. Do not let the number of steps decide an answer.<br>
> **Status:** examinable.

> **Changed recently:** (2026-07-15) More storage changes in one day.<br>
> **Old:** a [six-hour cool-off period](../facts/rds.md#rds-change-storage-modifications-four-2026-07) between storage modifications.<br>
> **Now:** [up to four storage modifications](../facts/rds.md#rds-change-storage-modifications-four-2026-07) in a [rolling 24-hour window](../facts/rds.md#rds-change-storage-modifications-four-2026-07).<br>
> **The exam probably expects:** a wait between two storage changes. Prefer an option that does not depend on the wait.<br>
> **Status:** examinable.

## Check (2 min)
<!-- section: role=check; route=fast; minutes=2 -->

**Check 1.** A team runs RDS for SQL Server. It wants automatic failover and copies that also take read traffic. Can it use a Multi-AZ DB cluster?

<details>
<summary>Answer</summary>

No. Multi-AZ DB clusters run MySQL or PostgreSQL. Use a Multi-AZ DB instance for failover, and add a read replica: [a Multi-AZ standby cannot serve read requests](../facts/rds.md#rds-faq-multiaz-standby-no-reads).

**Predict 1:** No. The standby serves no reads.

</details>

**Check 2.** A table was deleted 40 days ago. Backup retention is at its maximum. Can a point-in-time restore bring the table back?

<details>
<summary>Answer</summary>

No. Retention is [between 0 and 35 days](../facts/rds.md#rds-backup-retention-range).

**Predict 2:** Yes, if automated backups are on. A restore reaches [any second during your retention period](../facts/rds.md#rds-faq-pitr-any-second-latest-restorable).

</details>

**Check 3.** An application on two EC2 instances keeps its own pool of 20 long-lived connections. Does it need RDS Proxy?

<details>
<summary>Answer</summary>

Usually not. The proxy suits [frequent short database connections](../facts/rds-proxy.md#rds-proxy-lambda-connection-pooling), and it adds an average of [5 milliseconds](../facts/rds-proxy.md#rds-proxy-faq-adds-5-ms-connect-directly).

**Predict 3:** Connections. Many functions can [exhaust database connection limits](../facts/lambda.md#lambda-vpc-db-connections-rds-proxy).

</details>

## Recap from memory (2 min)
<!-- section: role=recap; route=fast; minutes=2 -->

**Recap 1.** In the first compare table, how does a Multi-AZ DB instance replicate, and how does a read replica?

<details>
<summary>Answer</summary>

[Synchronous replication](../facts/rds.md#rds-compare-replication-sync-async) for Multi-AZ; [asynchronous replication](../facts/rds.md#rds-compare-replication-sync-async) for the read replica.

</details>

**Recap 2.** What does the signals table give for "too many connections", and what is its "But not if"?

<details>
<summary>Answer</summary>

RDS Proxy. But if reads drive the CPU and connections are few, a read replica.

</details>

**Recap 3.** How do you encrypt an existing unencrypted DB instance?

<details>
<summary>Answer</summary>

Encrypt a snapshot copy, then [restore an encrypted DB instance](../facts/rds.md#rds-encrypt-existing-via-snapshot-copy). Or [use a blue/green deployment](../facts/rds.md#rds-encryption-blue-green-change-key).

</details>
