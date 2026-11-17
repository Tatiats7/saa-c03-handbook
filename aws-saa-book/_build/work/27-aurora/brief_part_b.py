# brief-27, part B: How-it-works subsections 1 to 7.


def sub(heading, minutes, words, bullets, facts, plan, route=None):
    d = {"file": "2-deep.md", "section": anchor(heading), "heading": heading, "bullets": bullets, "facts": facts,
         "status": "write", "minutes": minutes, "words_all_in": words}
    if route:
        d["route"] = route
    d["plan"] = plan
    BRIEF["sections"].append(d)


# 1 ---------------------------------------------------------------------------------------------
sub("An Aurora cluster runs DB instances on one shared cluster volume", 3, 205, ["3.3.S2", "3.3.K8", "3.3.S4"],
    ["aurora-is-managed-relational-engine", "aurora-faq-what-is-aurora", "aurora-part-of-rds", "aurora-cluster-has-instances-and-volume",
     "aurora-separates-compute-and-storage", "aurora-one-primary-per-cluster", "aurora-primary-handles-ddl-dml",
     "aurora-write-operations-managed-by-primary", "aurora-replicas-read-only-auto-replication", "aurora-single-instance-still-a-cluster",
     "aurora-management-operates-on-clusters", "aurora-existing-mysql-postgres-code-works", "aurora-faq-no-special-drivers",
     "aurora-faq-open-source-compatibility", "aurora-uses-rds-console-cli-api", "aurora-rds-responsible-hosting",
     "aurora-customer-responsible-query-tuning", "aurora-dg-use-when-relational-modernize", "aurora-instance-class-determines-compute-memory",
     "aurora-instance-class-type-and-size", "aurora-t-classes-dev-test-only", "aurora-memory-optimized-r-class-example",
     "aurora-add-instance-no-data-copy", "aurora-remove-instance-keeps-data", "aurora-delete-instances-keep-cluster-and-data",
     "aurora-delete-cluster-removes-volume-and-data", "aurora-cluster-volume-contents-all-data-and-metadata",
     "aurora-faq-compute-scaling-manual", "aurora-faq-compute-scaling-serverless", "aurora-faq-compute-scaling-limitless",
     "aurora-faq-limitless-when-to-use", "aurora-dg-limitless-beyond-single-instance", "aurora-limitless-horizontal-write-scaling",
     "aurora-throughput-up-to-6x-stock-mysql-and-postgresql", "aurora-dg-dsql-active-active-multi-region", "aurora-change-dsql-generally-available"],
    {
        "problem": ("A classic database ties its data to the disk of one server. A second server, or a bigger one, first needs its own copy "
                    "of all the data. Aurora keeps the data apart from the servers."),
        "trace": [
            "**One engine you know.** Aurora is a [fully managed relational database engine] (aurora-is-managed-relational-engine) that is [compatible with MySQL and PostgreSQL] (aurora-is-managed-relational-engine), and it is [part of the managed database service] (aurora-part-of-rds) Amazon RDS.",
            "**Compute apart from storage.** A cluster has [one or more DB instances] (aurora-cluster-has-instances-and-volume) and [a cluster volume that manages the data] (aurora-cluster-has-instances-and-volume).",
            "**One writer.** Each cluster has [one primary DB instance] (aurora-one-primary-per-cluster); the [primary instance handles all data definition language] (aurora-primary-handles-ddl-dml) and data manipulation statements.",
            "**More instances are readers.** The other DB instances are read-only and are [known as Aurora Replicas] (aurora-replicas-read-only-auto-replication).",
            "**Add an instance without copying.** You can [add a DB instance quickly] (aurora-add-instance-no-data-copy), because Aurora [doesn't make a new copy] (aurora-add-instance-no-data-copy) of the table data.",
        ],
        "table": ("What lives where (columns: Part | Holds | You change it by): DB instance | CPU and memory; the class "
                  "[determines the computation and memory capacity] (aurora-instance-class-determines-compute-memory) | choosing another "
                  "instance class; Cluster volume | [user data, schema objects, and internal metadata] (aurora-cluster-volume-contents-all-data-and-metadata) "
                  "| nothing: it follows the data (subsection 3); Cluster | both, managed as one: Aurora works on [entire clusters of database servers] "
                  "(aurora-management-operates-on-clusters) | adding or removing DB instances. One link per fact per cell; cells at most 15 words."),
        "why": ("Why keep compute and storage apart? An instance can join or leave without moving data, and you can delete DB instances "
                "while [preserving the cluster itself] (aurora-delete-instances-keep-cluster-and-data). Even a cluster with [only a single DB "
                "instance] (aurora-single-instance-still-a-cluster) is [still a cluster] (aurora-single-instance-still-a-cluster), because its "
                "storage already spans Availability Zones."),
        "exam_signal": ("\"a relational database compatible with MySQL or PostgreSQL, with high performance and availability\" points to "
                        "Aurora, a [fully managed relational database service] (aurora-faq-what-is-aurora); \"migrate or modernize an "
                        "on-premises relational workload\" also points to Aurora ([migrating or modernizing an on-premises relational workload] "
                        "(aurora-dg-use-when-relational-modernize))."),
        "exam_trap": None,
        "body_extras": ("Only if words remain, one sentence: existing [code, tools, and applications] (aurora-existing-mysql-postgres-code-works) "
                        "work with Aurora, with [standard MySQL and PostgreSQL database drivers] (aurora-faq-no-special-drivers). Reference only, "
                        "no sentence: the throughput claim of up to 6x (aurora-throughput-up-to-6x-stock-mysql-and-postgresql: volatile marketing "
                        "figure; the decision guide still says five times); T classes for dev and test only (aurora-t-classes-dev-test-only); "
                        "query tuning stays with you (aurora-customer-responsible-query-tuning; chapter 26 teaches the split); Aurora PostgreSQL "
                        "Limitless Database for write throughput [beyond the limits of a single Aurora instance] (aurora-dg-limitless-beyond-single-instance): "
                        "name it at most once, never as a question key; Amazon Aurora DSQL is a separate service outside the exam's in-scope list "
                        "(aurora-dg-dsql-active-active-multi-region): no sentence."),
        "say_it": "The short answer is: Aurora puts several DB instances on one shared volume. The thing to watch is that one instance writes.",
        "stop_and_answer": ("A team adds a third DB instance to an Aurora cluster that holds 2 TB of data. Does Aurora copy the 2 TB to the "
                            "new instance before it can serve queries? Answer: no; Aurora [doesn't make a new copy] (aurora-add-instance-no-data-copy) "
                            "of the table data, and the new instance connects to the shared volume, so you can [add a DB instance quickly] "
                            "(aurora-add-instance-no-data-copy). 2 TB is an example value."),
    })

# 2 ---------------------------------------------------------------------------------------------
sub("Every write is stored as six copies across three Availability Zones", 4, 215, ["3.3.K1", "2.2.S2"],
    ["aurora-synchronous-replication-to-six-storage-nodes", "aurora-storage-six-copies-three-azs", "aurora-cluster-volume-three-azs-one-region",
     "aurora-cluster-volume-spans-azs-copy-each", "aurora-storage-three-azs-from-subnet-group", "aurora-every-instance-in-one-of-three-azs",
     "aurora-storage-copies-regardless-of-instance-azs", "aurora-storage-loss-tolerance-write-read", "aurora-faq-tolerates-two-copies-lost-write",
     "aurora-faq-tolerates-three-copies-lost-read", "aurora-storage-segment-size-10-gib", "aurora-faq-segments-six-copies",
     "aurora-storage-auto-repair-segment", "aurora-auto-repair-avoids-pitr", "aurora-three-azs-copies-minimize-disk-loss",
     "aurora-reliable-durable-fault-tolerant", "aurora-faq-crash-restart-under-60s", "aurora-recovery-from-restart-near-instant",
     "aurora-recovery-asynchronous-parallel-threads", "aurora-page-cache-survives-database-restart", "aurora-faq-pay-for-one-copy",
     "aurora-faq-replication-not-charged", "aurora-data-transfer-between-azs-for-replication-free", "aurora-replication-independent-of-instance-count",
     "aurora-db-subnet-group-two-azs", "aurora-vpc-needs-two-subnets-two-azs", "aurora-region-has-multiple-isolated-azs",
     "aurora-no-local-zones", "aurora-cmp-ha-az-failure-no-data-loss-brief-interruption", "aurora-failover-time-without-replica",
     "aurora-sla-two-commitments-multi-az-single-az", "aurora-sla-multi-az-99-99", "aurora-sla-single-az-99-9"],
    {
        "problem": "A disk can fail, and so can a whole Availability Zone. The data must survive both, and writes must keep working.",
        "trace": [
            "**The writer sends each change to storage.** Aurora [synchronously replicates the data across Availability Zones] (aurora-synchronous-replication-to-six-storage-nodes) to [six storage nodes] (aurora-synchronous-replication-to-six-storage-nodes).",
            "**Three zones, two copies in each.** The volume holds [six copies] (aurora-storage-six-copies-three-azs) of your data across [three AZs] (aurora-storage-six-copies-three-azs), all in a [single AWS Region] (aurora-cluster-volume-three-azs-one-region).",
            "**Small pieces, fast repair.** Aurora splits the volume into [10 GiB segments] (aurora-storage-segment-size-10-gib); when a segment fails, [Aurora immediately repairs the segment] (aurora-storage-auto-repair-segment) from the other copies.",
            "**Lost copies are absorbed.** Writes continue after the loss of [up to two copies] (aurora-storage-loss-tolerance-write-read); reads continue after the loss of [up to three copies] (aurora-storage-loss-tolerance-write-read).",
        ],
        "table": ("What keeps working (columns: Event | What happens): one disk segment fails | Aurora repairs it from the other copies "
                  "(aurora-storage-auto-repair-segment, already linked in the trace: no second link needed); two copies are lost | reads and "
                  "writes continue; three copies are lost | reads continue ([up to three copies] (aurora-storage-loss-tolerance-write-read)); "
                  "the writer DB instance fails | storage is fine; the compute side recovers by failover (subsection 6). Write no row that "
                  "states what happens after three lost copies for writes: no fact says it."),
        "why": ("Why six copies of one write? With copies in three zones, the chance of data loss from a disk failure is [greatly minimized] "
                "(aurora-three-azs-copies-minimize-disk-loss), and [you only pay for one copy] (aurora-faq-pay-for-one-copy)."),
        "exam_signal": ("\"the data must survive the loss of an Availability Zone without managing replication\" points to the Aurora cluster "
                        "volume: a cluster can tolerate the failure of an Availability Zone [without any loss of data] "
                        "(aurora-cmp-ha-az-failure-no-data-loss-brief-interruption)."),
        "exam_trap": "aurora-trap-single-instance-is-ha",
        "exam_trap_text": ("> **Exam trap:** Six copies protect the data, not the DB instance. A cluster with no Aurora Replica recreates its "
                           "writer, which typically takes [less than 10 minutes] (aurora-failover-time-without-replica). <!-- trap: aurora-trap-single-instance-is-ha -->"),
        "go_deeper": ("Go deeper: fast restarts (at most 70 words). After a crash, Aurora does not replay the redo log, which cuts restart "
                      "time to [less than 60 seconds] (aurora-faq-crash-restart-under-60s) in most cases. It [recovers asynchronously on "
                      "parallel threads] (aurora-recovery-asynchronous-parallel-threads), and the page cache is [managed in a separate process "
                      "from the database] (aurora-page-cache-survives-database-restart). Self-repair also [reduces the need to perform a "
                      "point-in-time restore] (aurora-auto-repair-avoids-pitr) after a disk failure."),
        "body_extras": ("Reference only, no sentence unless words remain: Aurora picks the three zones from the DB subnet group "
                        "([three separate AZs selected automatically by Aurora] (aurora-storage-three-azs-from-subnet-group)); every DB instance "
                        "must be in one of them (aurora-every-instance-in-one-of-three-azs); the copies exist [regardless of whether the instances] "
                        "(aurora-storage-copies-regardless-of-instance-azs) span zones; a subnet group needs [at least two Availability Zones] "
                        "(aurora-db-subnet-group-two-azs); replication is free ([for DB cluster replication is free] "
                        "(aurora-data-transfer-between-azs-for-replication-free)); Aurora [doesn't support Local Zones] (aurora-no-local-zones); "
                        "SLA credit thresholds 99.99% Multi-AZ and 99.9% Single-AZ (aurora-sla-multi-az-99-99, aurora-sla-single-az-99-9) are "
                        "service-credit terms, not an availability promise: no sentence."),
        "say_it": "The short answer is: Aurora saves each write six times in three zones. The thing to watch is compute: one instance is still one instance.",
        "stop_and_answer": ("A cluster's storage uses AZ 1, AZ 2 and AZ 3, and its only DB instance runs in AZ 1. During the morning peak, "
                            "two storage nodes in AZ 2 fail. Do writes stop? Answer: no; writes continue after the loss of [up to two copies] "
                            "(aurora-storage-loss-tolerance-write-read), and [Aurora immediately repairs the segment] "
                            "(aurora-storage-auto-repair-segment). AZ 1 to AZ 3 are labels."),
    })

# 3 ---------------------------------------------------------------------------------------------
sub("The cluster volume grows by itself and you pay for used space", 3, 195, ["3.3.S2", "4.3.S3"],
    ["aurora-cluster-volume-grows-automatically", "aurora-pricing-storage-io-not-provisioned-in-advance", "aurora-charged-only-for-space-used",
     "aurora-volume-shrinks-when-data-removed", "aurora-storage-features-depend-on-version", "aurora-storage-grows-10-gib-to-256-tib-in-10-gib-increments",
     "aurora-cluster-volume-max-256-tib-overview", "aurora-change-storage-max-256-tib", "aurora-faq-storage-scales-to-256-tib",
     "aurora-table-size-limits-mysql-64-tib-postgresql-32-tib", "aurora-storage-separate-local-temp-files", "aurora-cluster-volume-ssd-single-virtual",
     "aurora-pricing-storage-billed-gb-month-both-configurations", "aurora-faq-limitless-beyond-256-tib", "rds-storage-ebs-striping"],
    {
        "problem": "On a database server with its own disk, you choose the disk size in advance. You pay for empty space, and a full disk stops the database.",
        "trace": [
            "**Nothing to size.** With Aurora you do not [provision either storage or I/O operations in advance] (aurora-pricing-storage-io-not-provisioned-in-advance).",
            "**It grows with the data.** The cluster volume grows by itself as the [amount of data in your database increases] (aurora-cluster-volume-grows-automatically), from a [minimum of 10 GiB] (aurora-storage-grows-10-gib-to-256-tib-in-10-gib-increments).",
            "**You pay for what is used.** You are [only charged for the space that you use] (aurora-charged-only-for-space-used); storage is [billed in per GB-month increments] (aurora-pricing-storage-billed-gb-month-both-configurations).",
            "**Dropped data frees space.** When you drop or truncate a table, [the space allocated for that data is freed] (aurora-volume-shrinks-when-data-removed); this [automatic resizing when data is removed] (aurora-storage-features-depend-on-version) depends on the engine version.",
        ],
        "table": ("What the cluster volume does (columns: Event | Result): data grows | the volume grows; nobody resizes it; a table is "
                  "dropped | space is freed (version-dependent); the volume reaches its maximum | the volume has a [maximum size of 256 "
                  "tebibytes (TiB)] (aurora-cluster-volume-max-256-tib-overview), which varies by engine version; "
                  "sorting large data sets | Aurora uses [separate local storage for nonpersistent, temporary files] "
                  "(aurora-storage-separate-local-temp-files), not the volume. The 256 TiB value is volatile (changed in 2025): it can stand in "
                  "this table, never in a question key."),
        "why": ("Why can Aurora bill only used space? The data sits on one [single, virtual volume] (aurora-cluster-volume-ssd-single-virtual) "
                "shared by every instance, so no instance owns a fixed disk. Compare RDS, where [Amazon RDS uses EBS volumes] "
                "(rds-storage-ebs-striping) that you allocate."),
        "exam_signal": ("\"storage grows unpredictably\" or \"no capacity planning for database storage\" points to the Aurora cluster volume, "
                        "which grows as the [amount of data in your database increases] (aurora-cluster-volume-grows-automatically)."),
        "exam_trap": None,
        "body_extras": ("Reference only: maximum table size 64 TiB for Aurora MySQL and 32 TiB for Aurora PostgreSQL "
                        "(aurora-table-size-limits-mysql-64-tib-postgresql-32-tib; B-list candidate, not planned); the 128 TiB to 256 TiB change "
                        "is the alternate Changed recently entry (aurora-change-storage-max-256-tib); Limitless Database for data [beyond 256 TiB] "
                        "(aurora-faq-limitless-beyond-256-tib): no sentence."),
        "say_it": "The short answer is: Aurora storage grows with your data, and you pay for what you use. The thing to watch is the maximum, which depends on the version.",
        "stop_and_answer": ("A team plans to allocate 5 TB of storage for a new Aurora cluster that holds 300 GB today, to leave room for "
                            "two years of growth. What do you tell them? Answer: there is nothing to allocate; you do not [provision either "
                            "storage or I/O operations in advance] (aurora-pricing-storage-io-not-provisioned-in-advance), and you are [only "
                            "charged for the space that you use] (aurora-charged-only-for-space-used). The sizes are example values."),
    })

# 4 ---------------------------------------------------------------------------------------------
sub("Aurora Replicas read the shared volume, so replica lag stays low", 4, 225, ["3.3.K7", "2.1.K15", "3.3.S1", "4.3.K8"],
    ["aurora-adding-replicas-read-same-volume-offload", "aurora-replicas-dedicated-reads-shared-volume-little-copy-work",
     "aurora-all-instances-see-single-logical-volume", "aurora-cmp-replicas-share-storage-no-replica-writes",
     "aurora-replicas-asynchronous-replication-no-primary-impact", "aurora-replica-lag-under-100-ms",
     "aurora-performance-guide-replica-lag-considerably-under-100-ms", "aurora-faq-replica-lag-tens-of-ms-same-region",
     "aurora-cmp-replica-lag-often-single-digit-milliseconds", "aurora-replica-lag-varies-with-write-rate", "aurora-replicas-return-same-data-minimal-lag",
     "aurora-replicas-up-to-15-in-addition-to-primary", "aurora-replicas-max-per-cluster", "aurora-faq-up-to-15-read-replicas",
     "aurora-quota-read-replicas-per-primary", "aurora-replicas-two-purposes-read-scale-availability", "aurora-replicas-offload-reads",
     "aurora-replicas-need-not-match-primary-instance-class", "aurora-add-replicas-console-cli-api", "aurora-replicas-spread-across-azs-of-cluster",
     "aurora-replication-independent-of-instance-count", "aurora-replicas-can-be-only-replication", "aurora-mysql-replicas-same-underlying-data",
     "rds-read-replica-async-read-only", "rds-storage-ebs-striping", "rds-compare-failover-vs-promote", "rds-replica-size-as-much-as-source",
     "rds-change-read-replicas-15-2022-10"],
    {
        "problem": ("An RDS read replica receives every change and writes it again to its own storage. Under heavy writes, that copy "
                    "falls behind, and reads show old data."),
        "trace": [
            "**The writer writes once.** The change lands in the shared cluster volume (subsection 2); no link needed for this step.",
            "**Replicas read the same volume.** Aurora Replicas [connect to the same storage volume] (aurora-adding-replicas-read-same-volume-offload) as the primary DB instance but [support read operations only] (aurora-adding-replicas-read-same-volume-offload).",
            "**Little to copy.** Because the volume is shared, [minimal additional work is required] (aurora-replicas-dedicated-reads-shared-volume-little-copy-work) to give each replica the data.",
            "**Lag stays short.** Replica lag is usually [much less than 100 milliseconds] (aurora-replica-lag-under-100-ms); it [varies depending on the rate of database change] (aurora-replica-lag-varies-with-write-rate).",
            "**Up to fifteen readers.** A cluster can have [up to 15 Aurora Replicas in addition to the primary DB instance] (aurora-replicas-up-to-15-in-addition-to-primary).",
        ],
        "table": ("RDS read replica or Aurora Replica (columns: Question | RDS read replica | Aurora Replica): How the data arrives | RDS "
                  "[copies them asynchronously to the read replica] (rds-read-replica-async-read-only) | it reads the volume the writer wrote: "
                  "replicas [share the same underlying storage] (aurora-cmp-replicas-share-storage-no-replica-writes); Storage | its own: "
                  "[Amazon RDS uses EBS volumes] (rds-storage-ebs-striping) | none of its own; Typical lag | depends on the write load | "
                  "[much less than 100 milliseconds] (aurora-replica-lag-under-100-ms); Failover target | [Can be manually promoted] "
                  "(rds-compare-failover-vs-promote) | promoted automatically (subsection 6). Then the diagram aurora-replica-compare "
                  "(caption and alt fixed in diagrams below; no numbered steps)."),
        "diagram": "aurora-replica-compare, after the table (caption and alt fixed in diagrams below; no numbered steps).",
        "why": ("Why does a shared volume cut lag? Replicas [share the same underlying storage] (aurora-cmp-replicas-share-storage-no-replica-writes) "
                "with the writer, so a replica writes no copy of the change; it reads the pages that the writer already stored. If the table "
                "already uses this display, link [work from the same underlying data] (aurora-mysql-replicas-same-underlying-data) only for "
                "Aurora MySQL, or write the reason without a second link."),
        "exam_signal": ("\"read replicas fall behind at peak\" or \"scale reads with minimal replica lag\" on MySQL or PostgreSQL points to "
                        "Aurora Replicas, whose lag is usually [much less than 100 milliseconds] (aurora-replica-lag-under-100-ms); \"reads must "
                        "show every write at once\" still points to the writer, because lag [varies depending on the rate of database change] "
                        "(aurora-replica-lag-varies-with-write-rate). If the trace already uses both displays, link the second clause to "
                        "[minimal replica lag] (aurora-replicas-return-same-data-minimal-lag)."),
        "exam_trap": None,
        "startup_example": ("> **Startup example:** Callvale's one read replica was up to 40 seconds behind at peak. Callvale now sends "
                            "dashboard queries to two Aurora Replicas through the reader endpoint. (26 words; 40 is in uses_numbers; 'two' is a word.)"),
        "body_extras": ("Reference only: a replica can use another instance class ([don't have to be of the same] "
                        "(aurora-replicas-need-not-match-primary-instance-class)), but HA replicas should match (subsection 6); replicas have "
                        "[two main purposes] (aurora-replicas-two-purposes-read-scale-availability); the FAQ says [tens of milliseconds] "
                        "(aurora-faq-replica-lag-tens-of-ms-same-region) and the features page says single-digit milliseconds "
                        "(aurora-cmp-replica-lag-often-single-digit-milliseconds): never put two lag figures in one sentence; the quota of 15 "
                        "[15 read replicas] (aurora-quota-read-replicas-per-primary) cannot be raised for Aurora."),
        "say_it": "The short answer is: Aurora Replicas read the writer's own volume, so they stay close behind. The thing to watch is lag: low, not zero.",
        "stop_and_answer": ("A team runs RDS for PostgreSQL with three read replicas. At peak, replica lag reaches 30 seconds, and the team "
                            "plans to add a fourth replica of the same size. Will that cut the lag? Answer: no; RDS [copies them asynchronously "
                            "to the read replica] (rds-read-replica-async-read-only) for each replica, so a fourth replica adds a fourth copy to "
                            "keep up; Aurora Replicas [connect to the same storage volume] (aurora-adding-replicas-read-same-volume-offload) "
                            "instead. 30 seconds is an example value."),
    }, route="pass")

# 5 ---------------------------------------------------------------------------------------------
sub("The reader endpoint spreads connections, not single queries, across replicas", 4, 215, ["3.3.S1", "2.1.K15"],
    ["aurora-cluster-endpoint-connects-to-current-primary", "aurora-cluster-endpoint-only-one-for-writes", "aurora-cluster-endpoint-also-reads",
     "aurora-cluster-endpoint-builtin-cannot-modify", "aurora-reader-endpoint-connection-balancing-read-only", "aurora-reader-endpoint-balances-replicas",
     "aurora-reader-endpoint-balances-connections-not-queries", "aurora-reader-endpoint-balances-each-connection-read-only-session",
     "aurora-reader-endpoint-new-connection-per-query-to-balance", "aurora-reader-endpoint-no-replica-goes-to-primary-writes-allowed",
     "aurora-reader-endpoint-reduces-primary-overhead-scales-selects", "aurora-reader-endpoint-builtin-cannot-modify",
     "aurora-ha-use-cluster-and-reader-endpoints", "aurora-endpoint-abstracts-connections-no-hardcode", "aurora-instance-endpoint-specific-db-instance",
     "aurora-instance-endpoint-use-diagnose-one-instance", "aurora-instance-endpoint-console-only", "aurora-custom-endpoint-set-of-chosen-instances",
     "aurora-custom-endpoint-use-different-instance-classes-reporting", "aurora-custom-endpoint-skip-reader-endpoint-when-using",
     "aurora-custom-endpoint-types-reader-any", "aurora-custom-endpoint-reader-type-membership-follows-failover",
     "aurora-custom-endpoint-static-or-exclusion-list", "aurora-custom-endpoint-none-until-created-up-to-five",
     "aurora-custom-endpoints-preferred-over-instance-endpoint-for-special-instances", "aurora-custom-endpoint-passive-dns-random-balancing",
     "aurora-custom-endpoint-not-in-snapshot-recreate-after-restore", "aurora-custom-endpoint-console-type-any",
     "aurora-custom-endpoint-existing-connections-stay-on-membership-change", "aurora-custom-endpoint-unavailable-replica-stays-associated",
     "aurora-custom-endpoint-avoids-cname-updates-and-supports-tls", "aurora-custom-endpoint-balances-beyond-read-only-vs-writer",
     "aurora-custom-endpoint-name-max-63-characters", "aurora-quota-custom-endpoints-per-cluster", "aurora-mysql-spreads-read-connections",
     "aurora-cmp-reader-endpoint-and-auto-scaling"],
    {
        "problem": ("An application should not keep a list of DB instance names. Instances come and go, and the writer can change. Aurora "
                    "gives the cluster a few stable names instead."),
        "trace": [
            "**Writes go to the cluster endpoint.** It [connects to the current primary DB instance] (aurora-cluster-endpoint-connects-to-current-primary) and is [the only one that can perform write operations] (aurora-cluster-endpoint-only-one-for-writes).",
            "**Reads go to the reader endpoint.** It gives [connection-balancing support for read-only connections] (aurora-reader-endpoint-connection-balancing-read-only).",
            "**It balances each connection once.** The reader endpoint [balances connections to available Aurora Replicas] (aurora-reader-endpoint-balances-connections-not-queries) and [doesn't balance individual queries] (aurora-reader-endpoint-balances-connections-not-queries).",
            "**No replica, no readers.** In a cluster with [no Aurora Replicas] (aurora-reader-endpoint-no-replica-goes-to-primary-writes-allowed), the [reader endpoint connects to the primary instance] (aurora-reader-endpoint-no-replica-goes-to-primary-writes-allowed).",
        ],
        "table": ("Four kinds of endpoint (columns: Endpoint | Connects to | Use it for): cluster | the current writer | the [cluster endpoint "
                  "for read/write] (aurora-ha-use-cluster-and-reader-endpoints) work; reader | the Aurora Replicas | the [reader endpoint for "
                  "read-only connections] (aurora-ha-use-cluster-and-reader-endpoints); custom | [a set of DB instances that you choose] "
                  "(aurora-custom-endpoint-set-of-chosen-instances) | a group, such as large replicas for reports; instance | one DB instance: "
                  "it [connects to a specific DB instance] (aurora-instance-endpoint-specific-db-instance) | to [diagnose capacity or "
                  "performance issues] (aurora-instance-endpoint-use-diagnose-one-instance)."),
        "why": ("Why balance connections and not queries? The choice of replica happens when a connection opens. To spread single queries, "
                "open a new [connection to the reader endpoint for each query] (aurora-reader-endpoint-new-connection-per-query-to-balance)."),
        "exam_signal": ("\"send read-only queries to the replicas, also to replicas added later, without changing the application\" points to "
                        "the reader endpoint ([connection-balancing support for read-only connections] "
                        "(aurora-reader-endpoint-connection-balancing-read-only)); \"reports must run only on the two largest replicas\" points to "
                        "a custom endpoint ([a set of DB instances that you choose] (aurora-custom-endpoint-set-of-chosen-instances))."),
        "exam_trap": "aurora-trap-reader-endpoint-balances-queries",
        "exam_trap_text": ("> **Exam trap:** A connection pool on the reader endpoint does not spread each query. The endpoint [doesn't balance "
                           "individual queries] (aurora-reader-endpoint-balances-connections-not-queries), so a long-lived connection keeps "
                           "using the replica it first reached. <!-- trap: aurora-trap-reader-endpoint-balances-queries -->"),
        "go_deeper": ("Go deeper: custom endpoints (at most 70 words). A cluster has [no custom endpoints until you create one] "
                      "(aurora-custom-endpoint-none-until-created-up-to-five). Members of a `READER` custom endpoint are [automatically adjusted "
                      "during failovers and promotions] (aurora-custom-endpoint-reader-type-membership-follows-failover); an `ANY` endpoint can "
                      "hold [Both reader and writer DB instances] (aurora-custom-endpoint-types-reader-any). With custom endpoints you "
                      "[typically don't use the reader endpoint] (aurora-custom-endpoint-skip-reader-endpoint-when-using). If words remain: "
                      "[Custom endpoints are not included in the snapshot] (aurora-custom-endpoint-not-in-snapshot-recreate-after-restore), so you "
                      "[create them again after restoring] (aurora-custom-endpoint-not-in-snapshot-recreate-after-restore)."),
        "body_extras": ("Reference only: the number of custom endpoints per cluster has two facts with different scopes "
                        "(aurora-custom-endpoint-none-until-created-up-to-five says up to five and not adjustable in the guide; "
                        "aurora-quota-custom-endpoints-per-cluster says 5 by default, adjustable through Service Quotas): write no number; the "
                        "cluster and reader endpoints are built in and [can't create, delete, or modify] (aurora-cluster-endpoint-builtin-cannot-modify); "
                        "the instance endpoint's location is in the console only (aurora-instance-endpoint-console-only)."),
        "say_it": "The short answer is: write through the cluster endpoint and read through the reader endpoint. The thing to watch is that the reader endpoint balances connections.",
        "stop_and_answer": ("A reporting job opens one connection to the reader endpoint at 08:00 and runs 5,000 queries on it until 18:00. The "
                            "cluster has three Aurora Replicas. How many replicas serve those queries? Answer: one; the reader endpoint "
                            "[balances connections to available Aurora Replicas] (aurora-reader-endpoint-balances-connections-not-queries), not "
                            "queries. To spread them, open a new [connection to the reader endpoint for each query] "
                            "(aurora-reader-endpoint-new-connection-per-query-to-balance). The times and counts are example values."),
    })

# 6 ---------------------------------------------------------------------------------------------
sub("When the writer fails, Aurora promotes a replica behind the same endpoint", 4, 225, ["2.2.K6", "2.2.S2", "3.3.K1"],
    ["aurora-detects-problems-activates-failover-automatically", "aurora-auto-failover-to-replica", "aurora-reader-takes-over-as-primary-failover",
     "aurora-replica-promoted-if-writer-unavailable", "aurora-failover-new-primary-by-promoting-or-creating", "aurora-promoting-replica-faster-than-new-primary",
     "aurora-failover-time-with-replica-guide", "aurora-faq-failover-cname-within-30s", "aurora-failover-time-without-replica",
     "aurora-no-replica-primary-recreated-same-az", "aurora-faq-single-instance-new-instance-same-az", "aurora-az-outage-readers-in-other-azs-promoted",
     "aurora-single-az-cluster-create-instances-manually", "aurora-cluster-endpoint-stays-same-after-failover",
     "aurora-cluster-endpoint-fails-over-minimal-interruption", "aurora-cluster-endpoint-ip-changes-after-failover-flush-dns",
     "aurora-failover-read-write-fail-with-exception", "aurora-reader-endpoint-may-point-to-new-primary-briefly",
     "aurora-writer-reader-endpoints-follow-failover-instance-endpoints-not", "aurora-instance-endpoint-specific-db-instance",
     "aurora-recommend-replica-in-two-azs", "aurora-replica-recommend-same-class-different-az", "aurora-replicas-separate-azs-for-ha",
     "aurora-distribute-instances-multiple-azs-recommended", "aurora-convert-to-multi-az-by-adding-reader-other-az",
     "aurora-promotion-priority-highest-promoted-first", "aurora-promotion-priority-range", "aurora-promotion-tie-break-largest",
     "aurora-promotion-tie-break-arbitrary", "aurora-faq-low-priority-replica-still-promoted-if-needed", "aurora-modify-priority-no-failover-trigger",
     "aurora-faq-priority-change-no-failover", "aurora-promotion-tiers-ignored-after-five-failures", "aurora-replica-failover-priority-specify",
     "aurora-faq-add-1-to-15-replicas-three-azs", "aurora-faq-promotion-highest-priority-first", "aurora-faq-promotion-tie-largest-wins",
     "aurora-manual-failover-console-cli-api", "aurora-manual-failover-possible", "aurora-manual-failover-target-db-instance-identifier",
     "aurora-best-practice-test-failover", "aurora-restart-faster-than-failover", "aurora-best-practice-dns-ttl-under-30-seconds",
     "aurora-faq-rds-proxy-failover-66-percent", "aurora-rds-proxy-failover-reduction-66-percent", "aurora-rds-proxy-reader-endpoint-reconnects-faster",
     "aurora-postgres-cluster-cache-mgmt-preserves-cache", "aurora-postgres-ccm-cold-cache-after-failover", "aurora-postgres-ccm-set-reader-failover-target",
     "aurora-postgres-ccm-same-instance-class-as-writer", "aurora-postgres-ccm-keeps-cache-synchronized-warm", "aurora-postgres-fast-failover-aws-jdbc-driver",
     "aurora-postgres-fast-failover-dns-caching-timeouts", "aurora-postgres-fast-failover-use-read-write-endpoints",
     "aurora-mysql-failover-restarts-only-writer-and-target", "aurora-faq-cluster-endpoint-promotes-replica", "aurora-faq-replicas-promoted-without-data-loss",
     "aurora-cmp-ha-az-failure-no-data-loss-brief-interruption"],
    {
        "problem": ("The writer DB instance can fail, and so can its Availability Zone. Writes must move to another DB instance by "
                    "themselves, and the application must find it."),
        "trace": [
            "**Aurora detects it.** Aurora [detects database problems] (aurora-detects-problems-activates-failover-automatically) and [activates the failover mechanism automatically] (aurora-detects-problems-activates-failover-automatically).",
            "**A replica becomes the writer.** Aurora [automatically fails over to an Aurora Replica] (aurora-auto-failover-to-replica); the priority tier decides which one (Go deeper).",
            "**The endpoint follows.** The cluster endpoint [stays the same even when a failover promotes] (aurora-cluster-endpoint-stays-same-after-failover) a new writer.",
            "**A short break.** During the switch, [read and write operations fail with an exception] (aurora-failover-read-write-fail-with-exception); service is typically back in [less than 60 seconds] (aurora-failover-time-with-replica-guide), often in [less than 30 seconds] (aurora-failover-time-with-replica-guide).",
        ],
        "table": ("When the writer fails (columns: Cluster | What Aurora does | Typical time): a writer and a replica in another AZ | "
                  "[promoting an existing Aurora Replica] (aurora-failover-new-primary-by-promoting-or-creating) | [less than 60 seconds] "
                  "(aurora-failover-time-with-replica-guide); one DB instance only | the primary is [recreated in the same AZ] "
                  "(aurora-no-replica-primary-recreated-same-az) | [less than 10 minutes] (aurora-failover-time-without-replica); all instances "
                  "in one AZ, and that AZ fails | you [manually create one or more new DB instances] (aurora-single-az-cluster-create-instances-manually) "
                  "in another AZ | until you act."),
        "why": ("Why keep a replica of the same size in another zone? [Promoting an Aurora Replica] (aurora-promoting-replica-faster-than-new-primary) "
                "is [much faster than creating a new primary instance] (aurora-promoting-replica-faster-than-new-primary), so AWS advises "
                "replicas of the [same DB instance class as the primary instance] (aurora-replica-recommend-same-class-different-az) placed "
                "[in different Availability Zones] (aurora-replica-recommend-same-class-different-az)."),
        "exam_signal": ("\"fail over automatically within a minute if the writer or its Availability Zone fails\" points to an Aurora Replica in "
                        "another AZ: Aurora [automatically fails over to an Aurora Replica] (aurora-auto-failover-to-replica); \"the connection "
                        "string must not change after a failover\" points to the cluster endpoint ([connect to the cluster endpoint] "
                        "(aurora-cluster-endpoint-stays-same-after-failover))."),
        "exam_trap": None,
        "spot_the_bug": ("**Spot the bug.** A production Aurora cluster has one writer and two Aurora Replicas. To keep traffic between them "
                         "fast, the team placed all three DB instances in AZ 1. 'The storage is in three zones anyway,' they say. What is wrong? "
                         "Reveal (about 55 words): the data survives an AZ 1 outage, but no DB instance does; no replica in another zone can be "
                         "promoted, so you must [manually create one or more new DB instances] (aurora-single-az-cluster-create-instances-manually). "
                         "Place replicas [in different Availability Zones] (aurora-replica-recommend-same-class-different-az). AZ 1 is a label."),
        "go_deeper": ("Go deeper: which replica wins, and faster reconnects (at most 70 words). Priorities run from [0 for the highest priority "
                      "to 15 for the lowest priority] (aurora-promotion-priority-range); on a tie, RDS promotes [the replica that is largest in "
                      "size] (aurora-promotion-tie-break-largest). A low tier is not a lock: RDS [will promote the lower priority replica] "
                      "(aurora-faq-low-priority-replica-still-promoted-if-needed) when the others are unhealthy. RDS Proxy cuts failover time by "
                      "[up to 66%] (aurora-rds-proxy-failover-reduction-66-percent). Cut the proxy sentence first if over 70 words."),
        "body_extras": ("Reference only: the FAQ says failover typically completes [within 30 seconds] (aurora-faq-failover-cname-within-30s): never "
                        "two failover-time links in one sentence; test failovers ([Test failover for your DB cluster] (aurora-best-practice-test-failover)); "
                        "a client DNS cache under 30 seconds (aurora-best-practice-dns-ttl-under-30-seconds; B-list candidate); Aurora PostgreSQL "
                        "cluster cache management keeps a warm cache on a chosen reader (aurora-postgres-cluster-cache-mgmt-preserves-cache); the "
                        "reader endpoint can point at the new writer [for a short time] (aurora-reader-endpoint-may-point-to-new-primary-briefly); "
                        "convert a single-AZ cluster by [adding a new reader DB instance] (aurora-convert-to-multi-az-by-adding-reader-other-az)."),
        "say_it": "The short answer is: Aurora promotes a replica, and the cluster endpoint follows it. The thing to watch is where your replicas run.",
        "stop_and_answer": ("A cluster has its writer in AZ 1 and one Aurora Replica in AZ 2. The application connects with the instance endpoint "
                            "of the writer. After a failover, writes keep failing although the replica is now the writer. Why? Answer: an instance "
                            "endpoint [connects to a specific DB instance] (aurora-instance-endpoint-specific-db-instance); only the writer and "
                            "reader endpoints [automatically change which DB instance they connect] "
                            "(aurora-writer-reader-endpoints-follow-failover-instance-endpoints-not) to. Use the cluster endpoint."),
    }, route="pass")

# 7 ---------------------------------------------------------------------------------------------
sub("Aurora Auto Scaling adds and removes Aurora Replicas for read load", 3, 200, ["2.1.K15", "3.3.S1"],
    ["aurora-cmp-aurora-auto-scaling-adjusts-replicas", "aurora-auto-scaling-both-engines-removes-unused", "aurora-auto-scaling-target-tracking-cloudwatch",
     "aurora-autoscaling-predefined-metric-reader-cpu", "aurora-autoscaling-predefined-metric-reader-connections", "aurora-auto-scaling-policy-min-max-replicas",
     "aurora-autoscaling-replica-count-range", "aurora-auto-scaling-cooldown-default", "aurora-auto-scaling-scale-out-always-enabled",
     "aurora-autoscaling-removes-only-own-replicas", "aurora-autoscaling-writer-not-scaled", "aurora-auto-scaling-needs-writer-first",
     "aurora-autoscaling-needs-all-instances-available", "aurora-auto-scaling-new-replica-same-class-as-primary",
     "aurora-auto-scaling-new-replica-last-promotion-priority", "aurora-auto-scaling-use-reader-endpoint", "aurora-auto-scaling-one-policy-per-target-metric",
     "aurora-autoscaling-global-secondary-unsupported", "aurora-serverless-not-supported-with-aurora-auto-scaling",
     "aurora-serverless-readers-alternative-to-aurora-auto-scaling", "aurora-cmp-reader-endpoint-and-auto-scaling", "aurora-one-primary-per-cluster",
     "aurora-faq-compute-scaling-manual"],
    {
        "problem": "Read traffic rises every morning and falls at night. A fixed number of replicas is too small at the peak and wasted at night.",
        "trace": [
            "**Set a range.** The scaling policy sets the [minimum and maximum number of Aurora Replicas] (aurora-auto-scaling-policy-min-max-replicas), each between [0–15] (aurora-autoscaling-replica-count-range).",
            "**Track one metric.** Target tracking [creates and manages CloudWatch alarms] (aurora-auto-scaling-target-tracking-cloudwatch) for a metric such as average replica CPU, [RDSReaderAverageCPUUtilization] (aurora-autoscaling-predefined-metric-reader-cpu).",
            "**Add and remove replicas.** Aurora Auto Scaling [dynamically adjusts the number of Aurora Replicas] (aurora-cmp-aurora-auto-scaling-adjusts-replicas); a new replica has the [same DB instance class] (aurora-auto-scaling-new-replica-same-class-as-primary) as the primary.",
            "**Applications find them.** Applications must [support connections to new Aurora Replicas] (aurora-auto-scaling-use-reader-endpoint); AWS advises the reader endpoint for that.",
        ],
        "table": ("What Aurora Auto Scaling changes (columns: Workload | Does it scale?): reads on the replicas | yes: it helps [only on the "
                  "reader instances] (aurora-autoscaling-writer-not-scaled); writes on the writer | no (same fact, linked once in row 1); "
                  "replicas that you added by hand | it [only removes Aurora Replicas that it created] (aurora-autoscaling-removes-only-own-replicas); "
                  "Aurora Serverless v2 readers | no: [Aurora Auto Scaling isn't supported] (aurora-serverless-not-supported-with-aurora-auto-scaling)."),
        "why": ("Why only readers? A cluster has [one primary DB instance] (aurora-one-primary-per-cluster), so more instances can only add read "
                "capacity. A busy writer needs a larger instance class instead (the [Apply Immediately flag] (aurora-faq-compute-scaling-manual) "
                "changes it now; otherwise the change waits for the maintenance window)."),
        "exam_signal": ("\"read traffic varies during the day\" with provisioned instances points to Aurora Auto Scaling ([dynamically adjusts the "
                        "number of Aurora Replicas] (aurora-cmp-aurora-auto-scaling-adjusts-replicas)); \"the writer's CPU is high from writes\" "
                        "does not, because it scales [only on the reader instances] (aurora-autoscaling-writer-not-scaled)."),
        "exam_trap": "aurora-trap-auto-scaling-scales-writer",
        "exam_trap_text": ("> **Exam trap:** Aurora Auto Scaling does not add write capacity. It helps [only on the reader instances] "
                           "(aurora-autoscaling-writer-not-scaled); for a busy writer, choose a larger instance class or Aurora Serverless v2 "
                           "(subsection 8). <!-- trap: aurora-trap-auto-scaling-scales-writer -->"),
        "body_extras": ("Reference only: cooldowns default to [300 seconds] (aurora-auto-scaling-cooldown-default); a new replica gets the [last "
                        "priority, which is 15 by default] (aurora-auto-scaling-new-replica-last-promotion-priority); it scales only when [all "
                        "cluster instances are in the available state] (aurora-autoscaling-needs-all-instances-available); not for Global Database "
                        "secondaries (aurora-autoscaling-global-secondary-unsupported); with Aurora Serverless v2, create readers in advance and "
                        "[leave them scaled down to low capacity] (aurora-serverless-readers-alternative-to-aurora-auto-scaling)."),
        "say_it": "The short answer is: Aurora Auto Scaling adds replicas when reads grow and removes them later. The thing to watch is the writer: it keeps its size.",
        "stop_and_answer": ("A team created two Aurora Replicas by hand. At the morning peak, Aurora Auto Scaling added three more. At night the "
                            "load drops. Can Aurora Auto Scaling remove the team's two replicas? Answer: no; it [only removes Aurora Replicas that "
                            "it created] (aurora-autoscaling-removes-only-own-replicas). The counts are example values."),
    })
