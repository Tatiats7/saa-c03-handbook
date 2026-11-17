# brief-27, part E: the 22 question slots and the question plan.

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
slot(bullet="3.3.S1", concept="reader-endpoint-for-read-scaling", difficulty=2, type="single", layer="core",
     exam_english=["ee-least-operational-overhead"], section=sec("The reader endpoint"), trap="aurora-trap-writes-through-reader-endpoint",
     distractor_traps=[], twin="first of strict twin pair A (twin q07)",
     key_facts=["aurora-reader-endpoint-connection-balancing-read-only", "aurora-reader-endpoint-balances-replicas", "aurora-ha-use-cluster-and-reader-endpoints"],
     note=("Shared stem: a company runs an Amazon Aurora PostgreSQL DB cluster with one writer and four Aurora Replicas: two large and two "
           "small. The team adds and removes replicas often. Each web request opens a new database connection. Changed phrase: 'Read-only "
           "queries from the web application must be spread across all the replicas, including replicas that are added later.' Ask: 'Which "
           "solution meets this requirement with the LEAST operational overhead?' Key: (A) Connect the read-only queries to the reader endpoint "
           "of the cluster ([connection-balancing support for read-only connections] (aurora-reader-endpoint-connection-balancing-read-only); "
           "[reader endpoint for read-only connections] (aurora-ha-use-cluster-and-reader-endpoints)). Options identical in q07: (A) as above; "
           "(B) Create a custom endpoint that contains the two large replicas, and connect the read-only queries to it; (C) Point all "
           "connections of the application, writes included, at the reader endpoint, so that every replica shares the work (trap "
           "aurora-trap-writes-through-reader-endpoint in both stems; why links [the only one that can perform write operations] "
           "(aurora-cluster-endpoint-only-one-for-writes)); (D) Store the instance endpoint of each replica in the application settings, and "
           "choose one for each query (violates-qualifier in both stems: you then [hardcode all the hostnames] "
           "(aurora-endpoint-abstracts-connections-no-hardcode)). In q01, (B) is violates-requirement: the small replicas get no queries. "
           "'Each web request opens a new connection' is in the shared stem so that connection balancing spreads the queries (no ambiguity "
           "with aurora-trap-reader-endpoint-balances-queries). Write option texts in neutral words that fit both stems."))
slot(bullet="3.3.K7", concept="aurora-replicas-low-lag-vs-rds-replicas", difficulty=2, type="single", layer="core",
     exam_english=["ee-least-operational-overhead", "ee-scalable"], section=sec("Aurora Replicas read"), trap="aurora-trap-replicas-copy-data",
     distractor_traps=["rds-trap-standby-serves-reads"],
     key_facts=["aurora-adding-replicas-read-same-volume-offload", "aurora-replica-lag-under-100-ms", "aurora-existing-mysql-postgres-code-works"],
     note=("Bullets also 2.1.K15, 3.3.S4. A company runs Amazon RDS for PostgreSQL with three read replicas. At write peaks the replicas "
           "fall up to 40 seconds behind, and dashboards show stale data. The company needs a scalable read tier with replica lag in "
           "milliseconds, behind one read endpoint, without rewriting its SQL. Which solution meets these requirements with the LEAST "
           "operational overhead? Key: migrate to an Aurora PostgreSQL cluster and send dashboard queries to Aurora Replicas through the "
           "reader endpoint ([connect to the same storage volume] (aurora-adding-replicas-read-same-volume-offload); [much less than 100 "
           "milliseconds] (aurora-replica-lag-under-100-ms); [code, tools, and applications] (aurora-existing-mysql-postgres-code-works)). "
           "Distractors: stay on RDS, because Aurora Replicas also copy every change to their own storage, and add two larger read replicas "
           "(trap aurora-trap-replicas-copy-data; why links rds-read-replica-async-read-only and aurora-adding-replicas-read-same-volume-offload); "
           "convert the RDS DB instance to Multi-AZ and send the dashboard queries to the standby (trap rds-trap-standby-serves-reads; why "
           "links [doesn't serve read traffic] (rds-multi-az-instance-standby-no-reads)); put Amazon ElastiCache in front of all dashboard "
           "reads and keep the replicas (violates-qualifier: a second store to run and keep in step; why links "
           "dynamodb-decision-guide-elasticache-caching-layer). Do not offer a Multi-AZ DB cluster: its readable standbys could be argued."))
slot(bullet="2.2.K6", concept="point-in-time-restore-new-cluster", difficulty=1, type="single", layer="core",
     exam_english=["ee-point-in-time"], section=sec("Backups are continuous"), trap="aurora-trap-restore-in-place", distractor_traps=[],
     key_facts=["aurora-pitr-any-second-within-retention-period", "aurora-pitr-creates-new-cluster"],
     note=("Difficulty 1, qualifier none (no violates-qualifier option). Use Aurora PostgreSQL, so that Backtrack is not an answer. A faulty "
           "release deleted rows in an Aurora PostgreSQL cluster at 14:05; the backup retention period is 7 days. The company must get the "
           "data back as it was at 14:04 (a point in time). What should a solutions architect do? Key: restore the cluster to 14:04 as a new "
           "DB cluster, then copy the rows back ([any second during your retention period] (aurora-pitr-any-second-within-retention-period); "
           "[creating a new DB cluster] (aurora-pitr-creates-new-cluster)). Distractors: run a point-in-time restore that rolls the existing "
           "cluster back to 14:04 in place (trap aurora-trap-restore-in-place; why links aurora-restore-always-creates-new-cluster); promote an "
           "Aurora Replica, which still holds the old rows (misconception: replicas read the same volume, aurora-adding-replicas-read-same-volume-offload); "
           "restore the most recent manual snapshot, taken last week (violates-requirement: loses a week of data)."))
slot(bullet="3.3.K8", concept="serverless-v2-for-spiky-load", difficulty=2, type="single", layer="core",
     exam_english=["ee-most-cost-effective", "ee-unpredictable", "ee-spiky"], section=sec("Aurora Serverless v2"),
     trap="aurora-trap-auto-scaling-scales-writer", distractor_traps=[], twin="first of strict twin pair C (twin q10)",
     key_facts=["aurora-serverless-choose-variable-spiky-workloads", "aurora-serverless-specify-min-max-capacity-range", "aurora-serverless-overprovision-raises-cost"],
     note=("Bullets also 4.3.S3. Shared stem: a company is moving a new order-processing application to an Amazon Aurora MySQL DB cluster; "
           "reads and writes both grow with the orders. Changed phrase: 'The load is unpredictable: it stays low for hours, then spikes to "
           "many times the usual level within minutes.' Ask: 'Which capacity option is the MOST cost-effective?' Key: (A) Use Aurora "
           "Serverless v2 DB instances with a capacity range from a low minimum to a high maximum ([variable or \"spiky\" workloads] "
           "(aurora-serverless-choose-variable-spiky-workloads); [specify the minimum and maximum capacity range] "
           "(aurora-serverless-specify-min-max-capacity-range)). Options identical in q10: (A) as above; (B) Use provisioned DB instances sized "
           "for the usual load, and buy Reserved Instances for a 3-year term; (C) Use provisioned DB instances sized for the peak load, and "
           "pay On-Demand rates (violates-qualifier in q04: [higher costs if you overprovision] (aurora-serverless-overprovision-raises-cost)); "
           "(D) Keep one provisioned writer and use Aurora Auto Scaling to add Aurora Replicas when the load grows (trap "
           "aurora-trap-auto-scaling-scales-writer in q04, because writes spike too; why links aurora-autoscaling-writer-not-scaled). In q04, "
           "(B) is violates-requirement (cannot absorb the spikes). Never let the key rest on scaling to zero or on the 256 ACU maximum: both "
           "are volatile (changed 2024 and 2024-10)."))
slot(bullet="3.3.S4", concept="relational-joins-aurora-vs-dynamodb", difficulty=1, type="single", layer="core",
     exam_english=["ee-transactional"], section=sec("An Aurora cluster runs"), trap=None, distractor_traps=[],
     key_facts=["aurora-is-managed-relational-engine", "rds-decision-guide-relational-joins", "aurora-dg-use-when-relational-modernize"],
     note=("Difficulty 1, qualifier none. Bullets also 4.3.K9. A company builds a transactional order system. The data has customers, "
           "orders and products with many relationships, reports join several tables, and the team writes SQL for PostgreSQL today. Which "
           "AWS database service fits this workload? Key: Amazon Aurora PostgreSQL ([compatible with MySQL and PostgreSQL] "
           "(aurora-is-managed-relational-engine); [complex queries through joins] (rds-decision-guide-relational-joins)). Distractors: Amazon "
           "DynamoDB with one table for each entity (misconception: [at the heart of NoSQL data modeling] (dynamodb-no-joins-heart-of-nosql-modeling) "
           "is removing joins); Amazon ElastiCache as the only data store (misconception: an [ephemeral cache for frequently accessed data] "
           "(dynamodb-decision-guide-elasticache-caching-layer)); Amazon S3 with Amazon Athena for the order system (keyword-bait: 'reports'). "
           "Do not offer Amazon RDS for PostgreSQL: two defensible answers. Options of difficulty 1 can be short (2 to 45 words)."))
slot(bullet="2.2.K6", concept="replica-in-another-az-for-failover", difficulty=2, type="single", layer="core",
     exam_english=["ee-least-operational-overhead", "ee-across-availability-zones"], section=sec("When the writer fails"),
     trap="aurora-trap-single-instance-is-ha", distractor_traps=["aws-map-trap-one-az-is-highly-available"],
     key_facts=["aurora-auto-failover-to-replica", "aurora-failover-time-with-replica-guide", "aurora-convert-to-multi-az-by-adding-reader-other-az"],
     note=("Bullets also 3.3.K1, 2.2.S2. A company runs a production Aurora MySQL cluster with one DB instance; the cluster volume keeps "
           "copies across multiple Availability Zones. The database must recover from a failure of the DB instance or its Availability Zone "
           "automatically, in less than a minute. Which solution meets these requirements with the LEAST operational overhead? Key: add an "
           "Aurora Replica in a different Availability Zone and keep the application on the cluster endpoint ([adding a new reader DB "
           "instance] (aurora-convert-to-multi-az-by-adding-reader-other-az); [automatically fails over to an Aurora Replica] "
           "(aurora-auto-failover-to-replica); [less than 60 seconds] (aurora-failover-time-with-replica-guide)). Distractors: no change, "
           "because the six-copy storage already makes the cluster highly available (trap aurora-trap-single-instance-is-ha; why links "
           "[less than 10 minutes] (aurora-failover-time-without-replica)); add an Aurora Replica in the same Availability Zone as the writer "
           "(trap aws-map-trap-one-az-is-highly-available; why links aurora-single-az-cluster-create-instances-manually); create an Aurora "
           "global database with a secondary Region and fail over to it (violates-qualifier: a Region-level tool for a zone problem, more to "
           "run). 'less than a minute' in words keeps the key off the exact value."))
slot(bullet="3.3.S1", concept="custom-endpoint-for-analytics", difficulty=2, type="single", layer="core",
     exam_english=["ee-least-operational-overhead"], section=sec("The reader endpoint"), trap="aurora-trap-writes-through-reader-endpoint",
     distractor_traps=[], twin_of="q01", twin="second of strict twin pair A (twin of q01)",
     key_facts=["aurora-custom-endpoint-set-of-chosen-instances", "aurora-custom-endpoint-use-different-instance-classes-reporting"],
     note=("Same stem and same four options as q01. Changed phrase: 'Monthly analytics queries must run only on the two large replicas, so "
           "that they do not slow down the replicas that serve the web application.' Key: (B) the custom endpoint with the two large replicas "
           "([a set of DB instances that you choose] (aurora-custom-endpoint-set-of-chosen-instances); [instances that use a particular AWS "
           "instance class] (aurora-custom-endpoint-use-different-instance-classes-reporting)). In q07, (A) is violates-requirement: the "
           "reader endpoint [balances connections to available Aurora Replicas] (aurora-reader-endpoint-balances-connections-not-queries), the "
           "small ones included; (C) keeps trap aurora-trap-writes-through-reader-endpoint; (D) is violates-qualifier (it works, with "
           "hardcoded names). At least 3 questions stand between q01 and q07."))
slot(bullet="2.2.S2", concept="global-database-for-region-dr", difficulty=2, type="single", layer="core",
     exam_english=["ee-least-operational-overhead", "ee-cross-region"], section=sec("Aurora Global Database copies"),
     trap="aurora-trap-postgres-cross-region-replica", distractor_traps=["how-the-exam-asks-trap-multi-az-covers-region"],
     key_facts=["aurora-faq-global-db-definition", "aurora-global-replication-latency-under-1-second", "aurora-global-rpo-typically-seconds-guide"],
     note=("Bullets also 3.3.K1. A company runs an Aurora PostgreSQL DB cluster in one AWS Region. A new contract requires cross-Region "
           "recovery: if the Region fails, the database must run in a second Region with an RPO of seconds and an RTO of minutes. Which "
           "solution meets these requirements with the LEAST operational overhead? Key: an Aurora global database with a secondary cluster in "
           "the second Region ([span multiple AWS Regions] (aurora-faq-global-db-definition); [typically under a second] "
           "(aurora-global-replication-latency-under-1-second); [typically measured in seconds] (aurora-global-rpo-typically-seconds-guide)). "
           "Distractors: create a cross-Region Aurora Replica of the PostgreSQL cluster (trap aurora-trap-postgres-cross-region-replica; "
           "impossible-feature; why links [doesn't support cross-Region Aurora Replicas] (aurora-postgres-no-cross-region-aurora-replicas)); "
           "add Aurora Replicas in two more Availability Zones (trap how-the-exam-asks-trap-multi-az-covers-region; why: zones are in one "
           "Region, [single AWS Region] (aurora-cluster-volume-three-azs-one-region)); copy a cluster snapshot to the second Region every hour "
           "with a scheduled script (violates-requirement and violates-qualifier: RPO of up to an hour; [manually copy Aurora snapshots] "
           "(aurora-no-cross-region-automated-backup-replication)). Do not cite the volatile aurora-global-secondary-regions-max-10."))
slot(bullet="3.3.S2", concept="encrypt-existing-cluster", difficulty=1, type="single", layer="core",
     exam_english=["ee-at-rest"], section=sec("Encryption at rest"), trap="aurora-trap-encrypt-existing-in-place", distractor_traps=[],
     key_facts=["aurora-encryption-cannot-convert-unencrypted-in-place", "aurora-restore-unencrypted-snapshot-specify-kms-key"],
     note=("Difficulty 1, qualifier none. An auditor finds that an Aurora PostgreSQL DB cluster, created years ago, is not encrypted at rest. "
           "The data must be encrypted with an AWS KMS key. What should a solutions architect do? Key: take a snapshot, restore it to a new DB "
           "cluster and specify a KMS key, then move the application ([restore an unencrypted snapshot] "
           "(aurora-encryption-cannot-convert-unencrypted-in-place); [specify a KMS key when you restore] "
           "(aurora-restore-unencrypted-snapshot-specify-kms-key)). Distractors: modify the cluster and turn on encryption (trap "
           "aurora-trap-encrypt-existing-in-place; why links [can't convert an unencrypted DB cluster] "
           "(aurora-encryption-cannot-convert-unencrypted-in-place)); add an encrypted Aurora Replica and fail over to it (impossible-feature; "
           "why links [can't create an encrypted Aurora Replica] (aurora-replica-encryption-must-match-cluster)); set rds.force_ssl in the "
           "cluster parameter group (different-problem: in transit; aurora-postgres-rds-force-ssl-parameter). Do not offer Blue/Green "
           "Deployments (aurora-sec-blue-green-encrypt-existing-cluster can also encrypt: two answers). 'created years ago' keeps the 2026 "
           "default encryption of new clusters out of the question."))
slot(bullet="4.3.S3", concept="reserved-instances-for-steady-load", difficulty=2, type="single", layer="core",
     exam_english=["ee-most-cost-effective", "ee-steady-state", "ee-predictable"], section=sec("Aurora Serverless v2"),
     trap=None, distractor_traps=[], twin_of="q04", twin="second of strict twin pair C (twin of q04)",
     key_facts=["aurora-pricing-reserved-instances-steady-state", "aurora-serverless-provisioned-suited-to-steady-workloads", "aurora-reserved-instance-one-or-three-year-term"],
     note=("Same stem and same four options as q04. Changed phrase: 'The load is steady and predictable around the clock, and it will stay at "
           "this level for at least the next 3 years.' Key: (B) provisioned DB instances sized for the usual load with Reserved Instances for "
           "a 3-year term ([appropriate for steady-state database workloads] (aurora-pricing-reserved-instances-steady-state); [suitable for "
           "steady workloads] (aurora-serverless-provisioned-suited-to-steady-workloads); [one- or three-year term] "
           "(aurora-reserved-instance-one-or-three-year-term)). In q10, (A) is a misconception: Aurora Serverless v2 is meant for [variable "
           "or \"spiky\" workloads] (aurora-serverless-choose-variable-spiky-workloads), and a steady load keeps connections open, so "
           "[the instance won't pause] (aurora-serverless-open-connections-block-pause); (C) is violates-qualifier "
           "(On-Demand, no commitment discount); (D) is different-problem (adds readers; the load does not change). No price numbers: the "
           "reasons rest on the stated fit of each model. In q04, tag (D) with aurora-trap-auto-scaling-scales-writer only if its text says "
           "that the replicas take the write load; otherwise it is a misconception with the same why."))
slot(bullet="4.3.K7", concept="heterogeneous-migration-sct-dms", difficulty=2, type="multi", select=2, layer="core",
     exam_english=["ee-which-combination", "ee-select-two", "ee-legacy", "ee-migrate"], section=sec("Data moves into Aurora"),
     trap=None, distractor_traps=[],
     key_facts=["aurora-migrate-heterogeneous-consider-sct", "aurora-postgres-non-postgres-source-use-dms"],
     note=("Select TWO, five options. A company plans to migrate a legacy on-premises Oracle database, with stored procedures in PL/SQL, to "
           "Aurora PostgreSQL. Which combination of steps meets this requirement with the LEAST operational overhead? (Select TWO.) Keys: "
           "(1) convert the schema and code with the AWS Schema Conversion Tool ([AWS Schema Conversion Tool (AWS SCT)] "
           "(aurora-migrate-heterogeneous-consider-sct)); (2) move the data with AWS Database Migration Service ([AWS Database Migration Service "
           "(AWS DMS)] (aurora-postgres-non-postgres-source-use-dms)). Distractors: create an Aurora read replica of the Oracle database "
           "(misconception: Aurora read replicas come from RDS for MySQL and PostgreSQL, [creating and restoring snapshots] or one-way "
           "replication: aurora-migrate-from-rds-snapshot-or-replication); use Babelfish for Aurora PostgreSQL to run the Oracle code "
           "unchanged (sibling-confusion: Babelfish is for SQL Server, aurora-faq-babelfish-sql-server); export the data with mysqldump and "
           "import it into Aurora (keyword-bait; violates-qualifier). Chapter 39 owns the DMS and SCT mechanics; keep the explanation at "
           "'which tool for which half'. No claim about downtime: no fact gives one for this path."))

# ---------------------------------------------------------------- extended (q12 to q22)
slot(bullet="2.2.K6", concept="global-failover-for-region-outage", difficulty=2, type="single", layer="extended",
     exam_english=["ee-least-operational-overhead", "ee-as-soon-as-possible"], section=sec("A secondary Region takes over"),
     trap="aurora-trap-switchover-for-region-outage", distractor_traps=[], twin="first of strict twin pair B (twin q16)",
     key_facts=["aurora-global-db-failover-use-for-unplanned-outage", "aurora-global-db-managed-failover-recommended-for-dr",
                "aurora-global-writer-endpoint-follows-switchover-failover"],
     note=("Shared stem: a company runs an Amazon Aurora global database for Aurora PostgreSQL. The primary cluster is in us-east-1 and one "
           "secondary cluster is in us-west-2. Applications connect through the global writer endpoint. Changed phrase: 'An outage makes the "
           "primary cluster in us-east-1 unavailable, and the company must restore write access in us-west-2 as soon as possible.' Ask: "
           "'Which solution meets these requirements with the LEAST operational overhead?' Key: (A) Run a managed cross-Region failover to the "
           "secondary cluster in us-west-2 ([recover from an unplanned outage] (aurora-global-db-failover-use-for-unplanned-outage); [method is "
           "recommended for disaster recovery] (aurora-global-db-managed-failover-recommended-for-dr); the writer endpoint follows: "
           "[automatically switches this endpoint] (aurora-global-writer-endpoint-follows-switchover-failover)). Options identical in q16: "
           "(A) as above; (B) Run a switchover to the secondary cluster in us-west-2; (C) Remove the secondary cluster from the global database, "
           "and point the applications at its cluster endpoint; (D) Restore the latest cluster snapshot in us-west-2, and point the "
           "applications at the new cluster. In q12: (B) trap aurora-trap-switchover-for-region-outage (why links [in a healthy state] "
           "(aurora-global-db-switchover-healthy-only-unplanned-use-failover)); (C) violates-qualifier (works as a manual step, "
           "[immediately stops the replication] (aurora-global-db-detach-secondary-standalone-readwrite), and the applications must change "
           "endpoints); (D) violates-requirement (slow; snapshots reach another Region only by copy, aurora-no-cross-region-automated-backup-replication)."))
slot(bullet="2.1.K15", concept="auto-scaling-readers-target-tracking", difficulty=2, type="single", layer="extended",
     exam_english=["ee-least-operational-overhead"], section=sec("Aurora Auto Scaling adds"), trap="aurora-trap-auto-scaling-scales-writer",
     distractor_traps=[],
     key_facts=["aurora-cmp-aurora-auto-scaling-adjusts-replicas", "aurora-autoscaling-predefined-metric-reader-cpu", "aurora-auto-scaling-use-reader-endpoint"],
     note=("Bullets also 3.3.S1. Read traffic on a provisioned Aurora MySQL cluster rises sharply each weekday morning and falls at night. "
           "At peak the Aurora Replicas reach 90 percent CPU while the writer stays at 30 percent. The application reads through the reader "
           "endpoint. Which solution adjusts read capacity automatically with the LEAST operational overhead? Key: an Aurora Auto Scaling "
           "target tracking policy on the average CPU of the replicas ([dynamically adjusts the number of Aurora Replicas] "
           "(aurora-cmp-aurora-auto-scaling-adjusts-replicas); [RDSReaderAverageCPUUtilization] (aurora-autoscaling-predefined-metric-reader-cpu)). "
           "Distractors: change the writer to a larger instance class each morning (trap aurora-trap-auto-scaling-scales-writer where the "
           "option says Aurora Auto Scaling resizes the writer; otherwise misconception: the writer is not the bottleneck, "
           "aurora-autoscaling-writer-not-scaled); a scheduled Lambda function that adds and deletes replicas (violates-qualifier); an Aurora "
           "global database secondary for the extra reads (different-problem). Write the trap option as 'Turn on Aurora Auto Scaling for the "
           "writer DB instance so that its instance class grows at peak' to state the belief exactly."))
slot(bullet="2.2.S2", concept="az-and-region-resilience-combination", difficulty=3, type="multi", select=2, layer="extended",
     exam_english=["ee-which-combination", "ee-select-two", "ee-highly-available"], section=sec("When the writer fails"),
     trap="aurora-trap-single-instance-is-ha", distractor_traps=["aurora-trap-postgres-cross-region-replica"],
     worked="think-aloud, wrong_path true",
     key_facts=["aurora-convert-to-multi-az-by-adding-reader-other-az", "aurora-auto-failover-to-replica", "aurora-faq-global-db-definition",
                "aurora-global-rpo-typically-seconds-guide"],
     note=("Select TWO, five options. A company runs an Aurora PostgreSQL cluster with one DB instance. It must stay highly available with "
           "automatic failover if an Availability Zone fails, and it must be able to recover in a second Region with an RPO measured in "
           "seconds if the primary Region fails. Which combination of steps meets these requirements with the LEAST operational overhead? "
           "(Select TWO.) Keys: (1) add an Aurora Replica in a different Availability Zone ([adding a new reader DB instance] "
           "(aurora-convert-to-multi-az-by-adding-reader-other-az); [automatically fails over to an Aurora Replica] "
           "(aurora-auto-failover-to-replica)); (2) add the cluster to an Aurora global database with a secondary cluster in the second Region "
           "([span multiple AWS Regions] (aurora-faq-global-db-definition); [typically measured in seconds] (aurora-global-rpo-typically-seconds-guide)). "
           "Distractors: rely on the six copies of the cluster volume for the Availability Zone failure (trap aurora-trap-single-instance-is-ha); "
           "create a cross-Region Aurora Replica (trap aurora-trap-postgres-cross-region-replica; impossible-feature, "
           "aurora-postgres-no-cross-region-aurora-replicas); copy a snapshot to the second Region every 15 minutes with a script "
           "(violates-qualifier and violates-requirement). Think-aloud with wrong_path true: step 3 predicts 'the storage already spans three "
           "zones, so only the Region needs work'; step 5 starts 'My first idea breaks because the storage survives, but with one DB "
           "instance Aurora must recreate the writer'."))
slot(bullet="4.3.S3", concept="standard-vs-io-optimized-by-io-share", difficulty=2, type="single", layer="extended",
     exam_english=["ee-most-cost-effective", "ee-steady-state"], section=sec("Aurora Standard charges"), trap="aurora-trap-io-optimized-always-cheaper",
     distractor_traps=[],
     key_facts=["aurora-standard-best-when-io-under-25-percent", "aurora-pricing-reserved-instances-steady-state", "aurora-reserved-instance-both-storage-configurations"],
     note=("An Aurora PostgreSQL cluster on Aurora Standard runs a steady-state load around the clock. The bill shows that I/O charges are "
           "about 10 percent of the cluster's Aurora spend. A team member proposes Aurora I/O-Optimized because it has no I/O charges. Which "
           "change is the MOST cost-effective? Key: keep Aurora Standard and buy Reserved Instances for the DB instances ([less than 25%] "
           "(aurora-standard-best-when-io-under-25-percent); [appropriate for steady-state database workloads] "
           "(aurora-pricing-reserved-instances-steady-state); Reserved Instances work [with both DB cluster configurations] "
           "(aurora-reserved-instance-both-storage-configurations)). Distractors: switch to I/O-Optimized, because a cluster without I/O charges "
           "always costs less (trap aurora-trap-io-optimized-always-cheaper; why links [25% or more] "
           "(aurora-io-optimized-best-when-io-25-percent-or-more)); move the reads to Aurora Replicas to lower the I/O bill (misconception: I/O "
           "is [counted the same way] (aurora-io-counted-same-writer-reader) on readers); move the instances to Aurora Serverless v2 to remove "
           "the I/O charges (misconception: serverless instances follow the cluster's [Aurora Standard or Aurora I/O-Optimized configuration] "
           "(aurora-serverless-storage-io-follow-cluster-configuration)). The 10 percent is a stem value; the key rests on the 25% threshold."))
slot(bullet="2.2.K6", concept="global-switchover-planned-move", difficulty=2, type="single", layer="extended",
     exam_english=["ee-least-operational-overhead"], section=sec("A secondary Region takes over"), trap="aurora-trap-global-failover-no-data-loss",
     distractor_traps=[], twin_of="q12", twin="second of strict twin pair B (twin of q12)",
     key_facts=["aurora-global-db-switchover-planned-no-data-loss", "aurora-global-db-switchover-controlled-scenarios", "aurora-global-switchover-rpo-zero"],
     note=("Same stem and same four options as q12. Changed phrase: 'For a planned maintenance event, the company must move the primary role "
           "to us-west-2 while both Regions are healthy, with no data loss.' Key: (B) the switchover ([relocate the primary cluster] "
           "(aurora-global-db-switchover-planned-no-data-loss); [controlled scenarios, such as operational maintenance] "
           "(aurora-global-db-switchover-controlled-scenarios); [RPO is 0 (no data loss)] (aurora-global-switchover-rpo-zero)). In q16, (A) "
           "carries trap aurora-trap-global-failover-no-data-loss (why links [doesn't wait for data to synchronize] "
           "(aurora-global-db-managed-failover-no-wait-async)); (C) is violates-requirement (replication stops; the old primary stays apart); "
           "(D) is violates-requirement (data after the snapshot is lost). Do not cite the volatile "
           "aurora-global-switchover-time-typically-under-30-seconds. At least 3 questions stand between q12 and q16."))
slot(bullet="3.3.K1", concept="global-reads-write-forwarding", difficulty=3, type="single", layer="extended",
     exam_english=["ee-least-operational-overhead", "ee-users-around-the-world"], section=sec("Aurora Global Database copies"),
     trap="aurora-trap-global-all-regions-write", distractor_traps=[], worked="think-aloud, wrong_path false",
     key_facts=["aurora-cmp-global-db-low-latency-reads-worldwide", "aurora-global-db-occasional-writes-use-secondary-reader-with-write-forwarding",
                "aurora-write-forwarding-secondary-forward-sql-writes"],
     note=("Bullets also 2.2.S2. A company's users are around the world, mostly in North America and Europe. Its order database is Aurora "
           "MySQL in us-east-1. European users see slow page loads, which are mostly reads. Europe also sends a few writes, such as profile "
           "changes, and every write must reach the same database. Which solution gives European users low-latency reads with the LEAST "
           "operational overhead? Key: an Aurora global database with a secondary cluster in a European Region; the European application "
           "reads from that cluster's reader endpoint and sends its occasional writes through write forwarding ([low-latency read operations "
           "for applications] (aurora-cmp-global-db-low-latency-reads-worldwide); [occasional DML statements] "
           "(aurora-global-db-occasional-writes-use-secondary-reader-with-write-forwarding); [forward SQL statements that perform write "
           "operations] (aurora-write-forwarding-secondary-forward-sql-writes)). Distractors: make the European secondary cluster a second "
           "writer that accepts its own writes (trap aurora-trap-global-all-regions-write; why links [Only the primary cluster performs write "
           "operations] (aurora-global-db-only-primary-writes)); a separate Aurora cluster in Europe kept in step by a custom sync job "
           "(violates-qualifier); move the data to DynamoDB global tables (violates-qualifier: a rewrite of a relational application). "
           "Six think-aloud steps, no wrong path. Do not cite the volatile write-forwarding version facts."))
slot(bullet="4.3.K8", concept="aurora-read-replica-migration-short-cutover", difficulty=2, type="single", layer="extended",
     exam_english=["ee-minimal-downtime", "ee-migrate", "ee-least-operational-overhead"], section=sec("Data moves into Aurora"),
     trap=None, distractor_traps=[],
     key_facts=["aurora-rds-postgres-read-replica-for-migration", "aurora-postgres-migrate-replica-lag-zero-stop-replication",
                "aurora-postgres-read-replica-migration-same-region-account"],
     note=("Bullets also 4.3.K7. A company runs a 3 TB Amazon RDS for PostgreSQL DB instance and wants to migrate it to Aurora PostgreSQL in the "
           "same AWS account and Region with minimal downtime. Which approach meets these requirements with the LEAST operational overhead? "
           "Key: create an Aurora read replica of the RDS DB instance, wait until the lag is zero, stop the writes, and promote it ([migration to "
           "Aurora PostgreSQL] (aurora-rds-postgres-read-replica-for-migration); [you can stop replication] "
           "(aurora-postgres-migrate-replica-lag-zero-stop-replication); [within the same AWS Region and account] "
           "(aurora-postgres-read-replica-migration-same-region-account)). Distractors: take a snapshot, stop the application, and restore the "
           "snapshot into Aurora (violates-requirement: the application is down for the whole restore; aurora-postgres-migrate-snapshot-from-rds); "
           "convert the schema with AWS SCT and move the data with AWS DMS (violates-qualifier: a schema conversion that the same engine does "
           "not need; aurora-migrate-heterogeneous-consider-sct); export with pg_dump and import with pg_restore (violates-qualifier and "
           "violates-requirement). No downtime figure in the explanation: no fact gives one."))
slot(bullet="3.3.S2", concept="reader-endpoint-and-proxy-for-connection-storms", difficulty=3, type="multi", select=2, layer="extended",
     exam_english=["ee-which-combination", "ee-select-two", "ee-short-lived"], section=sec("The reader endpoint"),
     trap="aurora-trap-reader-endpoint-balances-queries", distractor_traps=["aurora-trap-writes-through-reader-endpoint"],
     key_facts=["aurora-frequent-connections-use-rds-proxy", "aurora-reader-endpoint-reduces-primary-overhead-scales-selects", "lambda-vpc-db-connections-rds-proxy"],
     note=("Select TWO, five options. A company's application runs on AWS Lambda functions that use an Aurora PostgreSQL cluster with one "
           "writer and three Aurora Replicas. During peaks, thousands of short-lived invocations open new connections, the writer runs out of "
           "connections, and most of the queries are reads. Which combination of steps meets these requirements with the LEAST operational "
           "overhead? (Select TWO.) Keys: "
           "(1) put Amazon RDS Proxy between the functions and the cluster ([frequently open and close connections] "
           "(aurora-frequent-connections-use-rds-proxy); [exhaust database connection limits] (lambda-vpc-db-connections-rds-proxy)); (2) send "
           "the read-only queries to the reader endpoint ([reduces the overhead on the primary instance] "
           "(aurora-reader-endpoint-reduces-primary-overhead-scales-selects)). Distractors: send all connections, writes included, to the "
           "reader endpoint (trap aurora-trap-writes-through-reader-endpoint); keep one long-lived pool on the reader endpoint, because it "
           "spreads each query across the replicas (trap aurora-trap-reader-endpoint-balances-queries); build a connection-pooling service on "
           "Amazon EC2 instances in front of the cluster (violates-qualifier: it works, with servers to run). Alternative third distractor: "
           "raise max_connections far above what the application needs (misconception: [unused connections can cause performance to degrade] "
           "(aurora-postgres-unused-connections-degrade-performance)). Do not link the display that says 'we recommend'."))
slot(bullet="2.2.K6", concept="backtrack-rewind-in-place", difficulty=3, type="single", layer="extended",
     exam_english=[], section=sec("Backups are continuous"), trap="aurora-trap-restore-in-place", distractor_traps=[],
     key_facts=["aurora-backtrack-in-minutes-no-new-cluster", "aurora-backtrack-rewind-without-restore"],
     note=("An Aurora MySQL cluster was created with Backtrack turned on and a target backtrack window of 24 hours. A faulty batch job "
           "changed many rows 20 minutes ago. The company must return the whole database to the moment before the job and keep the same "
           "cluster endpoint. Which solution is the FASTEST? Key: backtrack the cluster to the time before the job ([rewinds the DB cluster in "
           "minutes] (aurora-backtrack-in-minutes-no-new-cluster); [doesn't require a new DB cluster] (aurora-backtrack-in-minutes-no-new-cluster); "
           "[without restoring data from a backup] (aurora-backtrack-rewind-without-restore)). Distractors: a point-in-time restore of the "
           "existing cluster in place (trap aurora-trap-restore-in-place; why links aurora-pitr-creates-new-cluster); a point-in-time restore "
           "to a new cluster and a switch of the application (violates-qualifier and violates-requirement: new endpoint; restores [can take "
           "hours]: no such display; write 'is slower' and link [creating a new DB cluster] (aurora-pitr-creates-new-cluster)); create a clone "
           "of the cluster (misconception: a clone copies the current data, [shares the same data pages as the original] "
           "(aurora-clone-shares-data-pages-separate-volume)). Do not cite the volatile aurora-change-backtrack-aurora-mysql-3."))
slot(bullet="3.3.S1", concept="promotion-tiers-failover-order", difficulty=3, type="single", layer="extended",
     exam_english=["ee-least-operational-overhead"], section=sec("When the writer fails"), trap=None, distractor_traps=[],
     key_facts=["aurora-promotion-priority-range", "aurora-promotion-priority-highest-promoted-first", "aurora-promotion-tie-break-arbitrary"],
     note=("Bullets also 2.2.K6. An Aurora PostgreSQL cluster has a writer, two large Aurora Replicas of the same class in AZ 2 and AZ 3, and "
           "one small replica that runs reports. On failover, the large replica in AZ 2 must be the first choice, the large replica in AZ 3 the "
           "second, and the small replica the last. Which configuration meets these requirements with the LEAST operational overhead? Key: "
           "set promotion tier 0 on the AZ 2 replica, tier 1 on the AZ 3 replica and tier 15 on the small replica ([0 for the highest priority to "
           "15 for the lowest priority] (aurora-promotion-priority-range); [promotes the Aurora Replica with the highest priority] "
           "(aurora-promotion-priority-highest-promoted-first)). Distractors: keep the same tier on all replicas, because Aurora promotes the "
           "largest one (misconception: the two large replicas tie, and RDS then promotes [an arbitrary replica] "
           "(aurora-promotion-tie-break-arbitrary)); create a custom endpoint for the two large replicas (misconception: endpoints do not "
           "choose the failover target); give the small replica a tier that blocks its promotion (misconception: RDS [will promote the lower "
           "priority replica] (aurora-faq-low-priority-replica-still-promoted-if-needed) when needed). Tie trap: stem must name the order of "
           "the two large replicas, or 'keep the same tier' becomes a second right answer."))
slot(bullet="4.3.K9", concept="dynamodb-for-key-value-sessions", difficulty=2, type="single", layer="extended",
     exam_english=["ee-least-operational-overhead", "ee-spiky"], section="1-fast.md#choose-it-or-not", trap=None, distractor_traps=[],
     key_facts=["dynamodb-decision-guide-key-value-session-store", "rds-decision-guide-dynamodb-row"],
     note=("Bullets also 3.3.S4, 3.3.K8. A company stores user session data. Every request reads or writes one session by its session ID; "
           "there are no joins, and traffic is spiky, with peaks of millions of requests. The team proposes Aurora Serverless v2. Which "
           "database meets these requirements with the LEAST operational overhead? Key: Amazon DynamoDB ([session stores or shopping carts] "
           "(dynamodb-decision-guide-key-value-session-store); [single-digit millisecond performance at any scale] "
           "(dynamodb-decision-guide-key-value-session-store)). Distractors: Aurora Serverless v2 (keyword-bait 'serverless' and violates-qualifier: "
           "a relational cluster to size and connect for key-value lookups); a provisioned Aurora cluster with Aurora Replicas behind the reader "
           "endpoint (violates-qualifier); Amazon ElastiCache as the only store (misconception: an [ephemeral cache for frequently accessed data] "
           "(dynamodb-decision-guide-elasticache-caching-layer)). The Aurora-side reason: Aurora is for relational workloads "
           "([migrating or modernizing an on-premises relational workload] (aurora-dg-use-when-relational-modernize))."))

BRIEF["question_plan"] = {
    "write": 22,
    "difficulty": {"1": 3, "2": 14, "3": 5},
    "difficulty_note": "3/22 = 14% (target 20% +- 10), 14/22 = 64% (55% +- 10), 5/22 = 23% (25% +- 10). When the weakest four are cut, cut at least one difficulty-2 question per cut of a 1 or 3, so that the shipped mix stays inside the tolerance.",
    "layer": {"core": 11, "extended": 11},
    "multi": 3,
    "multi_slots": ["q11 (core, difficulty 2)", "q14 (extended, difficulty 3, worked, wrong path)", "q19 (extended, difficulty 3)"],
    "twin_pairs": [
        "q01 / q07 (strict, core, difficulty 2, LEAST operational overhead: 'Read-only queries from the web application must be spread across all the replicas, including replicas that are added later.' / 'Monthly analytics queries must run only on the two large replicas, so that they do not slow down the replicas that serve the web application.'; same four options; key A / key B)",
        "q04 / q10 (strict, core, difficulty 2, MOST cost-effective: 'The load is unpredictable: it stays low for hours, then spikes to many times the usual level within minutes.' / 'The load is steady and predictable around the clock, and it will stay at this level for at least the next 3 years.'; same four options; key A / key B)",
        "q12 / q16 (strict, extended, difficulty 2, LEAST operational overhead: 'An outage makes the primary cluster in us-east-1 unavailable, and the company must restore write access in us-west-2 as soon as possible.' / 'For a planned maintenance event, the company must move the primary role to us-west-2 while both Regions are healthy, with no data loss.'; same four options; key A / key B)",
    ],
    "twin_pairs_note": "Three strict pairs are written so that one rejection still ships two whole pairs (orchestrator note). Each pair turns on a stable fact; none on a volatile one.",
    "worked": ["q14 (wrong path)", "q17 (no wrong path)"],
    "slots_on_a_trap": 16,
    "every_trap_cited": ("12 of the 13 trap ids are the slot trap or a planned distractor trap of at least one slot: replicas-copy-data q02; "
                         "writes-through-reader-endpoint q01 q07 (and q19 distractor); global-all-regions-write q17; switchover-for-region-outage "
                         "q12; encrypt-existing-in-place q09; single-instance-is-ha q06 q14; reader-endpoint-balances-queries q19; "
                         "auto-scaling-scales-writer q04 q13; postgres-cross-region-replica q08 (and q14 distractor); global-failover-no-data-loss "
                         "q16; restore-in-place q03 q20; io-optimized-always-cheaper q15. serverless-pauses-whenever-idle is taught by the Exam trap "
                         "of subsection 8, Check 3 and card aurora-c019; no slot carries it, because an option that states it would rest on the "
                         "volatile scale-to-zero change (2024-11-20). A question writer may still tag a distractor with it if the text states the "
                         "belief and the key does not depend on zero ACUs."),
    "bullets_covered": ("all 13 bullets of the registry entry are the primary bullet of at least one slot: 3.3.K1 q17; 3.3.K7 q02; 3.3.K8 q04; "
                        "3.3.S1 q01 q07 q21; 3.3.S2 q09 q19; 3.3.S4 q05; 4.3.K7 q11; 4.3.K8 q18; 4.3.K9 q22; 4.3.S3 q10 q15; 2.1.K15 q13; "
                        "2.2.K6 q03 q06 q12 q16 q20; 2.2.S2 q08 q14"),
    "q205_rule": ("Q205 is a chapter rule: at least half of all wrong options of the chapter carry a trap id (this brief's 13, or "
                  "traps_from_other_chapters). A distractor gets a trap id only when its text states exactly that trap's belief; otherwise it "
                  "carries a misconception and a distractor_type. Aim for two tagged wrong options in most questions."),
    "rule": ("Question ids are aurora-q001 to aurora-q022 in slot order (q01 = aurora-q001). Protect the three twin pairs, the three "
             "multiple-response questions and both worked questions when the weakest four are cut. At most 2 questions per concept; a unique "
             "(concept, trap) pair per question (twins exempt). Stems never name Callvale; they may reuse its situation and numbers. Keep at "
             "most one impossible-feature distractor per question, and give it a fact. Never let a volatile fact decide a key (list below). "
             "Never state a price. Within a twin pair, the qualifier, the options and every sentence but the changed phrase are identical."),
    "qualifier_rule": ("Difficulty 1 questions (q03, q05, q09) have qualifier none and no violates-qualifier option; every other question has "
                       "one qualifier word of SPEC questions.qualifier_words (MOST, LEAST, BEST, LOWEST, HIGHEST, FASTEST) and at least one "
                       "violates-qualifier option. 3 of 22 without a qualifier stays under the 25% cap of Q204."),
    "key_facts_note": "key_facts of each slot are the stable facts that decide its key; build_brief.py checked that none is volatile.",
}
