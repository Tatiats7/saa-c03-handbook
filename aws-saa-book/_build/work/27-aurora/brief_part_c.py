# brief-27, part C: How-it-works subsections 8 to 14, then Numbers, Decision record and FAQ quick-fire.

# 8 ---------------------------------------------------------------------------------------------
sub("Aurora Serverless v2 changes capacity with load inside a range you set", 4, 220, ["3.3.K8", "4.3.S3", "3.3.S2"],
    ["aurora-serverless-on-demand-autoscaling-configuration", "aurora-serverless-faq-definition", "aurora-serverless-acu-about-2-gib-memory",
     "aurora-serverless-specify-min-max-capacity-range", "aurora-serverless-capacity-range-0-256-acu-half-acu-steps",
     "aurora-serverless-scaling-increments-as-small-as-half-acu", "aurora-serverless-scales-in-half-acu-steps",
     "aurora-serverless-scales-up-on-cpu-memory-network-load", "aurora-serverless-scaling-with-open-connections-no-quiet-point",
     "aurora-serverless-scales-without-disrupting-client-transactions", "aurora-serverless-scaling-does-not-disrupt-operations",
     "aurora-serverless-scaling-rate-depends-on-current-capacity", "aurora-serverless-billing-unit-acu-hours", "aurora-serverless-faq-billed-per-second-acu",
     "aurora-serverless-charged-only-for-resources-consumed", "aurora-serverless-db-serverless-instance-class-type",
     "aurora-serverless-db-instance-class-always-db-serverless", "aurora-serverless-needs-scaling-configuration-before-instances",
     "aurora-serverless-capacity-range-set-with-first-instance-applies-to-all", "aurora-serverless-mixed-configuration-cluster",
     "aurora-serverless-faq-mixed-cluster-with-provisioned", "aurora-serverless-convert-provisioned-and-serverless",
     "aurora-serverless-convert-writer-via-failover", "aurora-serverless-convert-writer-to-provisioned-via-failover",
     "aurora-serverless-works-like-provisioned-for-failover", "aurora-serverless-faq-supports-all-provisioned-features",
     "aurora-serverless-compute-and-storage-separate", "aurora-serverless-tier-0-1-readers-follow-writer",
     "aurora-serverless-tier-2-to-15-readers-scale-independently", "aurora-serverless-reader-follow-writer-or-independent",
     "aurora-serverless-readers-scale-independently-of-writer", "aurora-serverless-standby-scales-with-writer-multi-az",
     "aurora-serverless-auto-pause-min-capacity-zero", "aurora-serverless-auto-pause-after-no-connections", "aurora-serverless-min-capacity-above-zero-no-pause",
     "aurora-serverless-open-connections-block-pause", "aurora-serverless-rds-proxy-blocks-auto-pause", "aurora-serverless-connect-to-paused-instance-resumes",
     "aurora-serverless-auto-pause-no-compute-charge-while-paused", "aurora-serverless-auto-pause-billing-storage-still-charged",
     "aurora-serverless-auto-pause-resume-about-15-seconds", "aurora-serverless-auto-pause-deeper-sleep-after-24-hours",
     "aurora-serverless-auto-pause-timeout-range", "aurora-serverless-retry-logic-for-paused-instances",
     "aurora-serverless-auto-pause-for-systems-without-strict-slo", "aurora-serverless-auto-pause-tolerate-slight-connection-delay",
     "aurora-serverless-scheduled-jobs-do-not-resume-paused-instance", "aurora-serverless-choose-variable-spiky-workloads",
     "aurora-serverless-choose-multitenant-dev-test", "aurora-serverless-dev-test-low-minimum-instead-of-burstable",
     "aurora-serverless-provisioned-suited-to-steady-workloads", "aurora-serverless-provisioned-constant-capacity-predict-ahead",
     "aurora-serverless-overprovision-raises-cost", "aurora-serverless-provisioned-brief-outages-acceptable",
     "aurora-serverless-identical-min-max-never-scales", "aurora-serverless-max-capacity-at-least-min", "aurora-serverless-max-cluster-capacity-n-times-max-acu",
     "aurora-serverless-platform-versions-not-serverless-v1", "aurora-serverless-change-v1-upgrade-to-v2-recommended",
     "aurora-serverless-change-scale-to-zero", "aurora-serverless-v2-adds-data-api-auto-pause-256-acu", "aurora-serverless-product-save-up-to-90-percent",
     "aurora-faq-data-api-http-no-drivers-no-pools-no-vpc", "aurora-faq-data-api-when-to-use", "aurora-faq-data-api-pools-connections",
     "aurora-serverless-storage-io-follow-cluster-configuration"],
    {
        "problem": ("A provisioned DB instance has a fixed size. When load is hard to predict, you pay for capacity that waits idle, or "
                    "you run short at the peak."),
        "trace": [
            "**Choose the instance class db.serverless.** It is a [special DB instance class type] (aurora-serverless-db-serverless-instance-class-type) inside an ordinary Aurora cluster.",
            "**Set a range in ACUs.** Each Aurora capacity unit (ACU) has [approximately 2 gibibytes (GiB) of memory] (aurora-serverless-acu-about-2-gib-memory) with matching CPU and networking; you [specify the minimum and maximum capacity range] (aurora-serverless-specify-min-max-capacity-range).",
            "**Aurora follows the load.** It [continuously tracks] (aurora-serverless-scales-up-on-cpu-memory-network-load) [CPU, memory, and network] (aurora-serverless-scales-up-on-cpu-memory-network-load) and scales in [increments as small as 0.5 ACUs] (aurora-serverless-scaling-increments-as-small-as-half-acu).",
            "**No quiet moment needed.** Scaling happens while connections are open: Aurora [doesn't wait for a quiet point] (aurora-serverless-scaling-with-open-connections-no-quiet-point).",
            "**You pay for what runs.** Charges are [measured in terms of ACU-hours] (aurora-serverless-billing-unit-acu-hours), at [a flat rate per second of ACU usage] (aurora-serverless-faq-billed-per-second-acu).",
        ],
        "table": ("Does the instance pause when idle? (columns: Setting | Result): minimum capacity zero ACUs, no connections | it can [pause "
                  "after a period with no user connections] (aurora-serverless-auto-pause-after-no-connections); minimum capacity [higher than "
                  "zero ACUs] (aurora-serverless-min-capacity-above-zero-no-pause) | it does not pause; minimum zero, but RDS Proxy in front | "
                  "it [won't automatically pause] (aurora-serverless-rds-proxy-blocks-auto-pause); a paused instance gets a connection | it "
                  "[automatically resumes and accepts the connection] (aurora-serverless-connect-to-paused-instance-resumes). Write 'zero ACUs' "
                  "in words in the cells (no digit outside a link)."),
        "why": ("Why not a bigger provisioned instance? With fixed capacity you can face [higher costs if you overprovision] "
                "(aurora-serverless-overprovision-raises-cost); AWS says Aurora Serverless v2 is intended for [variable or \"spiky\" workloads] "
                "(aurora-serverless-choose-variable-spiky-workloads)."),
        "exam_signal": ("\"unpredictable\", \"spiky\" or \"used a few hours a day\" points to Aurora Serverless v2 ([variable or \"spiky\" "
                        "workloads] (aurora-serverless-choose-variable-spiky-workloads)); \"steady load around the clock\" points to provisioned "
                        "instances, which are [suitable for steady workloads] (aurora-serverless-provisioned-suited-to-steady-workloads). If the "
                        "Why already links the spiky display, link [development and test systems] (aurora-serverless-choose-multitenant-dev-test) "
                        "here for the first clause instead."),
        "exam_trap": "aurora-trap-serverless-pauses-whenever-idle",
        "exam_trap_text": ("> **Exam trap:** Idle does not mean free. The instances can pause only when you set the minimum capacity [for the "
                           "cluster to zero ACUs] (aurora-serverless-auto-pause-min-capacity-zero), and even then storage is charged: only the "
                           "[instance charge is zero] (aurora-serverless-auto-pause-billing-storage-still-charged). "
                           "<!-- trap: aurora-trap-serverless-pauses-whenever-idle -->"),
        "body_extras": ("Only if words remain, one sentence: one cluster can mix [both Aurora serverless and provisioned capacity] "
                        "(aurora-serverless-mixed-configuration-cluster). Reference only: the range 0 to 256 ACUs "
                        "(aurora-serverless-capacity-range-0-256-acu-half-acu-steps: volatile, B-list); scaling to zero is new since 2024 "
                        "(aurora-serverless-change-scale-to-zero: Changed recently entry); resume in [approximately 15 seconds] "
                        "(aurora-serverless-auto-pause-resume-about-15-seconds: B-list); readers in tiers 0 and 1 follow the writer "
                        "(aurora-serverless-tier-0-1-readers-follow-writer); convert a provisioned writer by failover "
                        "(aurora-serverless-convert-writer-via-failover); it [works like provisioned for failover] "
                        "(aurora-serverless-works-like-provisioned-for-failover); the Data API is an [HTTP-based API] "
                        "(aurora-faq-data-api-http-no-drivers-no-pools-no-vpc) for new Lambda-based applications (FAQ only); the 90% savings "
                        "claim (aurora-serverless-product-save-up-to-90-percent) is marketing: no sentence. Aurora Serverless v1 appears at most "
                        "once (see naming)."),
        "say_it": "The short answer is: Aurora Serverless v2 grows and shrinks the instance with the load. The thing to watch is the minimum capacity you set.",
        "stop_and_answer": ("A team sets the minimum and the maximum capacity of an Aurora Serverless v2 cluster to the same value, 16 ACUs, to "
                            "make costs predictable. At the next sales peak, queries slow down. Will Aurora add capacity? Answer: no; with "
                            "[identical] (aurora-serverless-identical-min-max-never-scales) minimum and maximum, [the capacity never scales up or "
                            "down] (aurora-serverless-identical-min-max-never-scales). 16 ACUs is an example value."),
    }, route="pass")

# 9 ---------------------------------------------------------------------------------------------
sub("Aurora Global Database copies the cluster volume to read-only Regions", 4, 225, ["2.2.S2", "3.3.K1", "4.3.K8", "3.3.K7"],
    ["aurora-faq-global-db-definition", "aurora-global-database-multi-region-ha", "aurora-global-db-multiple-clusters-multiple-regions",
     "aurora-global-db-spans-at-least-two-regions", "aurora-global-db-primary-region-one-writer", "aurora-global-db-only-primary-writes",
     "aurora-global-db-secondary-region-readers-only", "aurora-global-db-replication-uses-storage-not-engine",
     "aurora-global-db-product-page-storage-based-replication-dedicated", "aurora-global-replication-latency-under-1-second",
     "aurora-faq-global-db-physical-lag-under-one-second", "aurora-cmp-global-db-storage-layer-replication-less-than-1-second",
     "aurora-global-database-async-replication-secondary", "aurora-global-db-replication-little-primary-performance-impact",
     "aurora-global-db-no-binlog-management", "aurora-global-secondary-regions-max-10", "aurora-global-secondary-each-in-different-region",
     "aurora-global-db-no-two-clusters-same-region", "aurora-global-secondary-cluster-max-16-reader-instances",
     "aurora-global-primary-max-readers-15-minus-secondary-regions", "aurora-global-db-scale-reads-connect-to-nearby-reader-endpoint",
     "aurora-cmp-global-db-low-latency-reads-worldwide", "aurora-global-db-scale-secondary-readers-serverless",
     "aurora-global-headless-secondary-no-compute-charge", "aurora-global-headless-needs-instance-before-promotion",
     "aurora-global-mixed-provisioned-and-serverless-between-regions", "aurora-faq-global-db-mixed-io-configurations",
     "aurora-global-requires-memory-optimized-instance-class", "aurora-global-instance-class-memory-optimized",
     "aurora-global-db-only-specific-versions-regions", "aurora-faq-global-db-both-engines", "aurora-cmp-global-db-write-forwarding-secondary-to-primary",
     "aurora-global-db-write-forwarding-auto-forwards-to-primary", "aurora-write-forwarding-secondary-forward-sql-writes",
     "aurora-write-forwarding-off-by-default-secondary", "aurora-write-forwarding-primary-source-of-truth",
     "aurora-write-forwarding-aurora-handles-cross-region-networking", "aurora-global-db-occasional-writes-use-secondary-reader-with-write-forwarding",
     "aurora-global-db-write-forwarding-unsupported-operations", "aurora-postgres-write-forwarding-consistency-modes-default-session",
     "aurora-postgres-write-forwarding-session-mode-waits-for-own-writes", "aurora-postgres-write-forwarding-higher-consistency-more-waiting",
     "aurora-postgres-local-write-forwarding-read-after-write", "aurora-postgres-no-cross-region-aurora-replicas",
     "aurora-mysql-cross-region-read-replica-cluster", "aurora-mysql-binlog-cross-region-replica-up-to-five",
     "aurora-mysql-cross-region-up-to-five-replica-clusters", "aurora-cmp-binlog-cross-region-replica-more-lag", "aurora-faq-binlog-cross-region-lag-unbounded",
     "aurora-cmp-global-db-minimal-lag-vs-xregion-replica", "aurora-faq-cross-region-physical-or-logical", "aurora-mysql-cross-region-data-transfer-charges",
     "aurora-mysql-cross-region-replica-must-be-encrypted-if-source", "aurora-mysql-promote-replica-to-standalone", "aurora-faq-promote-binlog-replica-few-minutes",
     "aurora-pricing-global-db-replicated-write-io-between-regions", "aurora-pricing-global-db-replicated-writes-equal-primary-writes",
     "aurora-pricing-global-db-replicated-write-io-both-configurations", "aurora-pricing-global-db-other-billed-dimensions",
     "aurora-faq-io-optimized-cross-region-replication-io-still-charged", "aurora-resources-not-auto-replicated-across-regions",
     "aurora-no-cross-region-automated-backup-replication", "aurora-global-db-secrets-manager-not-supported",
     "aurora-serverless-global-database-read-copies-dr", "aurora-serverless-global-secondary-can-use-serverless",
     "aurora-serverless-global-secondary-no-auto-pause", "dynamodb-vs-aurora-global-database-single-writer",
     "dynamodb-global-table-any-replica-serves-reads-writes"],
    {
        "problem": ("A whole Region can fail, and users far from it wait for every read. A copy in another Region must stay current "
                    "without slowing the writer, because [AWS Regions are isolated from each other] (aurora-resources-not-auto-replicated-across-regions)."),
        "trace": [
            "**One primary Region writes.** [Only the primary cluster performs write operations] (aurora-global-db-only-primary-writes).",
            "**Storage ships the changes.** Replication uses the [cluster storage volume and not the database engine] (aurora-global-db-replication-uses-storage-not-engine), with latency [typically under a second] (aurora-global-replication-latency-under-1-second).",
            "**Secondary Regions read.** A secondary Region runs a cluster [made up entirely of Aurora Replicas] (aurora-global-db-secondary-region-readers-only); applications there [connect to the reader endpoint] (aurora-global-db-scale-reads-connect-to-nearby-reader-endpoint) in their own Region.",
            "**Several Regions.** A global database can have [up to 10 secondary AWS Regions] (aurora-global-secondary-regions-max-10); the value changed in 2025 (Changed recently), so no question turns on it.",
        ],
        "table": ("Ways to copy Aurora data to another Region (columns: Question | Aurora Global Database | Aurora MySQL binlog replica | "
                  "Snapshot copy): How it copies | [storage-based replication] (aurora-global-db-product-page-storage-based-replication-dedicated) | "
                  "[MySQL binary log (binlog) replication] (aurora-mysql-binlog-cross-region-replica-up-to-five) | you [manually copy Aurora "
                  "snapshots] (aurora-no-cross-region-automated-backup-replication); Typical lag | [typically under a second] "
                  "(aurora-global-replication-latency-under-1-second) | [there is more lag time] (aurora-cmp-binlog-cross-region-replica-more-lag) "
                  "| the time since the last copy; Engines | [both Aurora MySQL and Aurora PostgreSQL] (aurora-faq-global-db-both-engines) | "
                  "Aurora MySQL only | both. Four columns; cells at most 15 words."),
        "why": ("Why replicate in storage? The writer does no extra work: the replication has [little performance impact on the primary DB "
                "cluster] (aurora-global-db-replication-little-primary-performance-impact), and you [don't need to configure or manage] "
                "(aurora-global-db-no-binlog-management) binlog replication."),
        "exam_signal": ("\"recover from a Regional outage with an RPO of seconds\" or \"low-latency reads for users around the world\" on a "
                        "relational database points to Aurora Global Database, built for [low latency global reads and disaster recovery] "
                        "(aurora-global-database-multi-region-ha); \"every Region must accept writes\" points to DynamoDB global tables, where "
                        "[Any global table replica] (dynamodb-global-table-any-replica-serves-reads-writes) can [serve reads and writes] "
                        "(dynamodb-global-table-any-replica-serves-reads-writes)."),
        "exam_trap": "aurora-trap-postgres-cross-region-replica",
        "exam_trap_text": ("> **Exam trap:** Aurora PostgreSQL has no cross-Region read replica like the Aurora MySQL binlog replica. Aurora "
                           "PostgreSQL [doesn't support cross-Region Aurora Replicas] (aurora-postgres-no-cross-region-aurora-replicas); use "
                           "Aurora Global Database. <!-- trap: aurora-trap-postgres-cross-region-replica -->"),
        "go_deeper": ("Go deeper: write forwarding (at most 70 words). Secondary clusters can [forward SQL statements that perform write "
                      "operations] (aurora-write-forwarding-secondary-forward-sql-writes) to the primary; [write forwarding isn't enabled] "
                      "(aurora-write-forwarding-off-by-default-secondary) when you add a secondary. The data is [always changed first on the "
                      "primary cluster] (aurora-write-forwarding-primary-source-of-truth). It suits [occasional DML statements] "
                      "(aurora-global-db-occasional-writes-use-secondary-reader-with-write-forwarding), and it [doesn't support certain MySQL or "
                      "PostgreSQL operations] (aurora-global-db-write-forwarding-unsupported-operations), such as DDL."),
        "body_extras": ("Reference only: between Regions you [pay for replicated write I/O operations] "
                        "(aurora-pricing-global-db-replicated-write-io-between-regions); a secondary without DB "
                        "instances is [not charged for compute, only for storage] (aurora-global-headless-secondary-no-compute-charge) and needs an "
                        "instance before promotion (aurora-global-headless-needs-instance-before-promotion); a secondary can hold [up to 16 "
                        "read-only DB instances] (aurora-global-secondary-cluster-max-16-reader-instances: B-list); memory-optimized classes "
                        "(aurora-global-requires-memory-optimized-instance-class); Aurora Serverless v2 in secondaries "
                        "(aurora-serverless-global-secondary-can-use-serverless); the FAQ's choice [either physical or logical replication] "
                        "(aurora-faq-cross-region-physical-or-logical) is an FAQ item; the Secrets Manager restriction "
                        "(aurora-global-db-secrets-manager-not-supported) is volatile: no sentence."),
        "say_it": "The short answer is: Global Database copies the storage to other Regions in about a second. The thing to watch is writes: one Region takes them.",
        "stop_and_answer": ("A company runs Aurora PostgreSQL in us-east-1 and opens an office in Europe. Reports there are slow, and every "
                            "write can stay in us-east-1. What gives the European office fast reads? Answer: an Aurora global database with a "
                            "secondary cluster in a European Region; the office applications [connect to the reader endpoint] "
                            "(aurora-global-db-scale-reads-connect-to-nearby-reader-endpoint) of that cluster."),
    }, route="pass")

# 10 --------------------------------------------------------------------------------------------
sub("A secondary Region takes over by failover after an outage, by switchover when healthy", 4, 225, ["2.2.K6", "2.2.S2"],
    ["aurora-global-db-failover-use-for-unplanned-outage", "aurora-global-db-failover-after-primary-region-outage",
     "aurora-global-db-failover-cross-region-to-secondary", "aurora-global-db-managed-failover-recommended-for-dr",
     "aurora-global-db-managed-failover-no-wait-async", "aurora-global-db-failover-can-lose-writes-consistent-state",
     "aurora-global-failover-rpo-nonzero-seconds", "aurora-global-rpo-typically-seconds-guide", "aurora-global-rto-order-of-minutes-guide",
     "aurora-global-promote-secondary-under-1-minute", "aurora-global-rpo-1-second-rto-under-1-minute", "aurora-cmp-wp-global-db-promote-under-one-minute",
     "aurora-global-managed-failover-primary-role-few-minutes", "aurora-global-db-managed-failover-readds-old-primary",
     "aurora-global-failover-rebuild-secondaries-minutes-to-hours", "aurora-global-db-failover-choose-least-lag-secondary",
     "aurora-global-db-manual-failover-choose-least-lag", "aurora-global-db-manual-failover-when-managed-unavailable",
     "aurora-global-db-detach-secondary-standalone-readwrite", "aurora-global-db-write-fencing-best-effort-split-brain",
     "aurora-global-db-unplanned-outage-replication-stops", "aurora-global-db-failover-new-volume-snapshot-old-primary",
     "aurora-global-db-switchover-controlled-scenarios", "aurora-global-db-switchover-healthy-only-unplanned-use-failover",
     "aurora-global-db-switchover-planned-no-data-loss", "aurora-global-switchover-rpo-zero", "aurora-global-db-switchover-waits-for-sync",
     "aurora-global-db-switchover-keeps-topology", "aurora-global-db-switchover-short-unavailability", "aurora-global-switchover-time-typically-under-30-seconds",
     "aurora-global-db-failback-via-switchover", "aurora-global-db-switchover-use-case-fail-back", "aurora-global-db-same-engine-version-for-managed-switchover",
     "aurora-global-db-writer-endpoint-auto-updated", "aurora-global-writer-endpoint-follows-switchover-failover",
     "aurora-global-db-writer-endpoint-no-app-change-after-switchover", "aurora-global-db-writer-endpoint-no-connection-string-change",
     "aurora-global-db-global-writer-single-readwrite-endpoint", "aurora-global-writer-endpoint-same-purpose-as-cluster-endpoint",
     "aurora-global-db-writes-to-primary-via-writer-endpoint", "aurora-global-db-cluster-endpoint-must-change-if-not-global-writer",
     "aurora-global-db-failover-use-global-writer-endpoint-low-ttl", "aurora-faq-global-db-no-code-change-writer-endpoint",
     "aurora-change-global-writer-endpoint", "aurora-change-global-failover-managed-unplanned", "aurora-global-database-async-replication-secondary",
     "aurora-global-db-postgres-rpo-managed-by-parameter", "aurora-global-db-postgres-rpo-parameter-affects-primary",
     "aurora-global-db-rpo-blocks-commits-when-all-secondaries-behind", "aurora-global-rpo-parameter-range", "aurora-global-db-rpo-parameter-dynamic",
     "aurora-global-db-two-region-keep-default-rpo-secondary", "aurora-cmp-wp-global-db-monitor-rpo-lag", "aurora-global-db-rpo-definition-data-loss-in-time",
     "aurora-global-db-rto-definition-measures-downtime", "aurora-global-db-lower-rto-rpo-than-traditional-replication", "aurora-global-db-arc-region-switch",
     "aurora-global-db-secondary-readers-restart-with-primary-writer", "aurora-global-db-secondary-read-replicas-stay-available-lag-grows",
     "aurora-global-db-rds-proxy-redirect-writes-after-role-switch", "aurora-global-db-write-forwarding-reconnect-after-failover",
     "aurora-cmp-wp-pilot-light-continuous-replication-best-for-rpo", "aurora-cmp-wp-warm-standby-faster-than-pilot-light",
     "aurora-cmp-wp-write-global-fit", "aurora-cmp-wp-active-active-async-replication-near-zero-rpo", "aurora-cmp-wp-multi-site-recovery-near-zero",
     "aurora-cmp-wp-pilot-light-core-infrastructure-always-available", "aurora-cmp-wp-global-db-dedicated-infrastructure-latency"],
    {
        "problem": ("Two events move the primary role to another Region: a planned move while everything is healthy, and an outage of the "
                    "primary Region. Each needs its own operation."),
        "trace": [
            "**Outage: fail over.** Use failover to [recover from an unplanned outage] (aurora-global-db-failover-use-for-unplanned-outage); AWS says the managed failover [method is recommended for disaster recovery] (aurora-global-db-managed-failover-recommended-for-dr).",
            "**Failover does not wait.** Managed failover [doesn't wait for data to synchronize] (aurora-global-db-managed-failover-no-wait-async), so the RPO is typically a [non-zero value measured in seconds] (aurora-global-failover-rpo-nonzero-seconds); the chosen secondary typically takes the primary role [within a few minutes] (aurora-global-managed-failover-primary-role-few-minutes).",
            "**Planned move: switch over.** A switchover lets you [relocate the primary cluster] (aurora-global-db-switchover-planned-no-data-loss) [with no data loss] (aurora-global-db-switchover-planned-no-data-loss), because Aurora first [waits for the target secondary Region clusters] (aurora-global-db-switchover-waits-for-sync) to catch up.",
            "**One name for writes.** The global writer endpoint [always points to the current writer DB instance] (aurora-global-db-global-writer-single-readwrite-endpoint), so you [don't need to change the connection settings] (aurora-global-db-writer-endpoint-no-app-change-after-switchover) after a switchover.",
        ],
        "table": ("Failover or switchover (columns: Question | Failover | Switchover): When to use it | to [recover from an unplanned outage] "
                  "(aurora-global-db-failover-use-for-unplanned-outage) | for [controlled scenarios, such as operational maintenance] "
                  "(aurora-global-db-switchover-controlled-scenarios); State of the clusters | the primary Region has failed | all [in a healthy "
                  "state] (aurora-global-db-switchover-healthy-only-unplanned-use-failover); Data loss | possible: unreplicated writes are lost | "
                  "[RPO is 0 (no data loss)] (aurora-global-switchover-rpo-zero); The old primary | Aurora [automatically adds back the old "
                  "primary Region] (aurora-global-db-managed-failover-readds-old-primary) | the topology is kept ([maintains your global "
                  "database's existing replication topology] (aurora-global-db-switchover-keeps-topology))."),
        "why": ("Why can a failover lose data? Aurora [asynchronously replicates all data and updates] (aurora-global-database-async-replication-secondary) "
                "to the secondaries, so the newest writes can still be on their way when the primary Region fails."),
        "exam_signal": ("\"the primary Region is unavailable; restore write access in the secondary Region\" points to a managed cross-Region "
                        "failover ([method is recommended for disaster recovery] (aurora-global-db-managed-failover-recommended-for-dr)); "
                        "\"planned maintenance; move the primary to another Region with no data loss\" points to a switchover ([with no data "
                        "loss] (aurora-global-db-switchover-planned-no-data-loss)). If the trace already uses both displays, link "
                        "[controlled scenarios, such as operational maintenance] (aurora-global-db-switchover-controlled-scenarios) for the "
                        "second clause."),
        "exam_trap": "aurora-trap-global-failover-no-data-loss",
        "exam_trap_text": ("> **Exam trap:** A Global Database failover is not lossless. [Both failover methods can result] "
                           "(aurora-global-db-failover-can-lose-writes-consistent-state) in a [loss of write transaction data that wasn't "
                           "replicated] (aurora-global-db-failover-can-lose-writes-consistent-state); only a switchover of healthy clusters has "
                           "[RPO is 0 (no data loss)] (aurora-global-switchover-rpo-zero). <!-- trap: aurora-trap-global-failover-no-data-loss -->"),
        "try_it": ("aurora-t02, after the table: one sentence ('Set an upper bound on the data loss of an Aurora PostgreSQL global database in a "
                   "cluster parameter group, and watch AWS refuse a value that is too low.'), then 'See [3-do.md](3-do.md). <!-- task: aurora-t02 -->'."),
        "body_extras": ("Only if words remain, one sentence: for Aurora PostgreSQL you can [manage the recovery point objective (RPO)] "
                        "(aurora-global-db-postgres-rpo-managed-by-parameter) with a cluster parameter; when every secondary falls behind, "
                        "[Aurora pauses transactions on the primary cluster] (aurora-global-db-rpo-blocks-commits-when-all-secondaries-behind). "
                        "Reference only: "
                        "AWS marketing and the FAQ say promotion in [less than 1 minute] (aurora-global-promote-secondary-under-1-minute) while "
                        "the guide says RTO [in the order of minutes] (aurora-global-rto-order-of-minutes-guide): never in one sentence; fail "
                        "back with a switchover (aurora-global-db-failback-via-switchover); a switchover takes [typically under 30 seconds] "
                        "(aurora-global-switchover-time-typically-under-30-seconds: volatile, no sentence); manual failover by detaching a "
                        "secondary (aurora-global-db-detach-secondary-standalone-readwrite); write fencing is best effort "
                        "(aurora-global-db-write-fencing-best-effort-split-brain); DR strategies of the whitepaper belong to chapter 40."),
        "say_it": "The short answer is: fail over after an outage, switch over when all is healthy. The thing to watch is data loss: a failover can lose seconds.",
        "stop_and_answer": ("A bank requires an RPO of 15 minutes and an RTO of 1 hour if the primary Region is lost. On paper, does Aurora "
                            "Global Database meet both? Answer: yes on paper: a failover loses a [non-zero value measured in seconds] "
                            "(aurora-global-failover-rpo-nonzero-seconds) of writes, and the secondary takes the primary role [within a few "
                            "minutes] (aurora-global-managed-failover-primary-role-few-minutes); only a recovery test proves it. The 15 minutes and "
                            "1 hour are example values in the prompt."),
    })

# 11 --------------------------------------------------------------------------------------------
sub("Backups are continuous, and every restore creates a new cluster", 4, 220, ["2.2.K6", "3.3.S2"],
    ["aurora-backups-automatic-continuous-incremental", "aurora-backup-continuous-incremental-no-impact", "aurora-backups-no-performance-impact",
     "aurora-backup-cannot-disable-automated", "aurora-faq-automated-backups-always-on", "aurora-backup-retention-period-range-1-35-days",
     "aurora-backup-retention-default-1-day", "aurora-pitr-any-point-within-retention", "aurora-pitr-any-second-within-retention-period",
     "aurora-backup-latest-restorable-time-within-5-minutes", "aurora-faq-pitr-latest-five-minutes", "aurora-pitr-logs-uploaded-continuously-to-s3",
     "aurora-automated-backups-stored-in-s3", "aurora-pitr-creates-new-cluster", "aurora-restore-always-creates-new-cluster",
     "aurora-faq-snapshot-restore-new-instance", "aurora-restore-cli-api-must-create-primary-instance", "aurora-restore-without-primary-endpoints-creating",
     "aurora-restore-inherits-retention-period", "aurora-pitr-restored-same-retention-as-source", "aurora-restore-snapshot-whole-cluster",
     "aurora-snapshots-do-not-expire", "aurora-manual-snapshots-not-subject-to-retention", "aurora-automated-backup-copy-to-keep-longer",
     "aurora-snapshots-always-full-backups", "aurora-no-incremental-snapshots-full-copies", "aurora-snapshot-cluster-must-be-available",
     "aurora-export-snapshot-to-s3-for-long-term", "aurora-export-snapshot-to-s3-background", "aurora-export-snapshot-parquet-format",
     "aurora-export-snapshot-analyze-with-athena-redshift-spectrum", "aurora-export-snapshot-all-data-by-default", "aurora-snapshot-copy-region-and-shared",
     "aurora-copy-encrypted-snapshot-cross-region-destination-key", "aurora-copy-encrypted-snapshot-stays-encrypted",
     "aurora-copy-cross-region-cross-account-share-first", "aurora-no-cross-region-automated-backup-replication", "aurora-share-manual-snapshot-enables-copy",
     "aurora-snapshot-share-up-to-20-accounts", "aurora-faq-shared-snapshot-same-region-only", "aurora-faq-no-automatic-snapshot-sharing",
     "aurora-snapshot-default-kms-key-cannot-be-shared", "aurora-encrypted-snapshot-cannot-be-public", "aurora-retain-automated-backups-after-delete",
     "aurora-change-retain-automated-backups-deleted-cluster", "aurora-final-snapshot-does-not-expire-retained-backups-do",
     "aurora-faq-delete-keeps-manual-snapshots", "aurora-delete-cluster-removes-volume-and-data", "aurora-deletion-protection-blocks-cluster-delete",
     "aurora-deletion-protection-default-console-vs-cli", "aurora-deletion-protection-toggle-no-outage", "aurora-aws-backup-manages-clusters",
     "aurora-change-pitr-with-aws-backup", "aurora-pitr-aws-backup-plan-used-for-point-in-time-recovery", "aurora-backup-awsbackup-snapshots-not-counted-in-quota",
     "aurora-backtrack-rewind-without-restore", "aurora-backtrack-in-minutes-no-new-cluster", "aurora-backtrack-only-if-enabled-at-creation",
     "aurora-backtrack-not-for-postgresql", "aurora-backtrack-window-limit-72-hours", "aurora-backtrack-whole-cluster-not-single-table",
     "aurora-backtrack-rewinds-not-replacement-for-backups", "aurora-backtrack-brief-instance-disruption", "aurora-backtrack-pay-hourly-for-change-records",
     "aurora-backtrack-no-cross-region-replicas", "aurora-clone-shares-data-pages-separate-volume", "aurora-clone-copy-on-write-storage-on-change",
     "aurora-clone-test-with-production-data", "aurora-clone-copy-on-write-max-15", "aurora-clone-same-region-only", "aurora-clone-multiple-from-same-or-clone",
     "aurora-clone-instances-configurable-differently", "aurora-clone-needs-source-with-instance", "aurora-clone-cross-vpc-same-availability-zones",
     "aurora-clone-cross-account-max-15", "aurora-clone-cross-account-default-key-unsupported", "aurora-binary-log-not-needed-for-replication-pitr",
     "aurora-backup-default-window-30-minutes", "aurora-backup-window-continues-past-window", "aurora-backup-window-not-overlap-maintenance",
     "aurora-backup-free-up-to-100-percent-of-cluster-size", "aurora-backup-storage-free-up-to-total-storage", "aurora-backup-no-charge-1-day-retention",
     "aurora-snapshots-free-within-retention-period", "aurora-billing-backup-storage-grows-with-retention-and-snapshots",
     "aurora-snapshot-storage-charged-after-cluster-deleted", "aurora-pricing-backup-storage-definition", "aurora-pricing-backup-storage-deleted-cluster-metered",
     "aurora-backup-storage-free-equals-cluster-volume-size", "aurora-quota-manual-cluster-snapshots"],
    {
        "problem": ("A faulty release deletes rows at 14:05. The team needs the data as it was at 14:04, and it must also keep month-end "
                    "copies for years."),
        "trace": [
            "**Backups run all the time.** Aurora [backs up your cluster volume automatically] (aurora-backups-automatic-continuous-incremental); the backups are [continuous and incremental] (aurora-backup-continuous-incremental-no-impact), and you [can't disable automated backups on Aurora] (aurora-backup-cannot-disable-automated).",
            "**You choose how long.** The retention period is [1–35 days] (aurora-backup-retention-period-range-1-35-days).",
            "**Restore to a second.** Point-in-time recovery reaches [any second during your retention period] (aurora-pitr-any-second-within-retention-period); the latest restorable time is typically [within 5 minutes of the current time] (aurora-backup-latest-restorable-time-within-5-minutes).",
            "**A restore is a new cluster.** A point-in-time restore means [creating a new DB cluster] (aurora-pitr-creates-new-cluster); from a snapshot, too, [a new DB cluster is created] (aurora-restore-always-creates-new-cluster).",
        ],
        "table": ("Four ways back in time (columns: Need | Tool | Result): data from three days ago | point-in-time restore | a new cluster "
                  "(linked in the trace); a copy kept for years | a manual snapshot: [snapshots don't expire] (aurora-snapshots-do-not-expire) | a "
                  "new cluster when you restore it; a test copy of production today | a clone that [shares the same data pages as the original] "
                  "(aurora-clone-shares-data-pages-separate-volume) | a separate volume; rewind Aurora MySQL by minutes | Backtrack, which "
                  "[rewinds the DB cluster in minutes] (aurora-backtrack-in-minutes-no-new-cluster) | the same cluster."),
        "why": ("Why is a restore a new cluster? The running cluster stays untouched while you check the restored data; then you copy rows "
                "back or move the application. To keep data longer than the retention period, [copy it to create a manual snapshot] "
                "(aurora-automated-backup-copy-to-keep-longer)."),
        "exam_signal": ("\"restore the database to its state of 10 minutes ago\" points to point-in-time recovery to a new cluster ([any second "
                        "during your retention period] (aurora-pitr-any-second-within-retention-period)); \"retain backups for 7 years\" points "
                        "to manual snapshots, because [snapshots don't expire] (aurora-snapshots-do-not-expire), or to an export to Amazon S3 "
                        "for [very long-term backups] (aurora-export-snapshot-to-s3-for-long-term). If the table uses the snapshot display, "
                        "keep only the export link here."),
        "exam_trap": "aurora-trap-restore-in-place",
        "exam_trap_text": ("> **Exam trap:** A point-in-time restore does not roll back the running cluster: it means [creating a new DB "
                           "cluster] (aurora-pitr-creates-new-cluster). Backtrack rewinds in place, but only on Aurora MySQL clusters [created "
                           "with the Backtrack feature enabled] (aurora-backtrack-only-if-enabled-at-creation). <!-- trap: aurora-trap-restore-in-place -->"),
        "go_deeper": ("Go deeper: Backtrack and clones (at most 70 words). [Backtrack is not available for Aurora PostgreSQL] "
                      "(aurora-backtrack-not-for-postgresql); its window has a limit of [72 hours] (aurora-backtrack-window-limit-72-hours), "
                      "and [Backtracking affects the entire DB cluster] (aurora-backtrack-whole-cluster-not-single-table). It is [not a "
                      "replacement for backing up] (aurora-backtrack-rewinds-not-replacement-for-backups). A clone stores only changes: "
                      "storage is [allocated only when changes are made to data] (aurora-clone-copy-on-write-storage-on-change)."),
        "body_extras": ("Reference only: the default retention is [one day] (aurora-backup-retention-default-1-day: B-list); you can retain "
                        "automated backups when you delete a cluster (aurora-retain-automated-backups-after-delete), but [a final snapshot "
                        "doesn't expire] (aurora-final-snapshot-does-not-expire-retained-backups-do); deletion protection is on by default only "
                        "in the console (aurora-deletion-protection-default-console-vs-cli); AWS Backup can manage Aurora backups "
                        "(aurora-aws-backup-manages-clusters; chapter 24); cross-Region copies are manual snapshot copies (subsection 9 table); "
                        "sharing: up to 20 accounts, same Region, not with the default KMS key (aurora-snapshot-share-up-to-20-accounts, "
                        "aurora-faq-shared-snapshot-same-region-only, aurora-snapshot-default-kms-key-cannot-be-shared); exports are Parquet "
                        "(aurora-export-snapshot-parquet-format); backup storage up to the cluster size is free "
                        "(aurora-backup-storage-free-up-to-total-storage)."),
        "say_it": "The short answer is: Aurora backs up all the time, and a restore gives you a new cluster. The thing to watch is the retention period you set.",
        "stop_and_answer": ("A company must keep a restorable copy of its month-end data for 7 years. It sets the backup retention period to the "
                            "highest value. Is that enough? Answer: no; the retention period is [1–35 days] "
                            "(aurora-backup-retention-period-range-1-35-days). Take a manual snapshot at each month-end, because [snapshots don't "
                            "expire] (aurora-snapshots-do-not-expire). 7 years is an example value."),
    })

# 12 --------------------------------------------------------------------------------------------
sub("Aurora Standard charges for each I/O, and I/O-Optimized includes it", 3, 205, ["4.3.S3"],
    ["aurora-standard-pays-per-million-io", "aurora-faq-standard-pay-per-io-vs-io-optimized-included", "aurora-io-optimized-no-io-charges",
     "aurora-io-optimized-best-when-io-25-percent-or-more", "aurora-standard-best-when-io-under-25-percent",
     "aurora-io-optimized-save-up-to-40-percent-above-25-percent-io", "aurora-faq-io-optimized-fits-io-intensive-workloads",
     "aurora-io-switch-standard-to-io-optimized-once-every-30-days", "aurora-io-switch-io-optimized-to-standard-any-time",
     "aurora-io-switch-no-downtime-non-nvme-and-serverless", "aurora-nvme-io-switch-needs-engine-restart", "aurora-faq-read-io-one-per-page",
     "aurora-faq-read-io-page-size", "aurora-faq-write-io-4-kb-units", "aurora-io-counted-same-writer-reader", "aurora-change-io-optimized-introduced",
     "aurora-faq-io-optimized-works-with-reserved-instances", "aurora-reserved-instance-both-storage-configurations",
     "aurora-pricing-reserved-instances-io-only-with-io-optimized", "aurora-reserved-instance-io-optimized-30-percent-more-units",
     "aurora-faq-io-optimized-backup-prices-unchanged", "aurora-faq-io-optimized-cross-region-replication-io-still-charged",
     "aurora-serverless-storage-io-follow-cluster-configuration", "aurora-pricing-reserved-instances-steady-state", "aurora-reserved-instance-one-or-three-year-term",
     "aurora-reserved-instance-discount-up-to-45-and-66-percent", "aurora-reserved-instance-no-upfront-one-year-only",
     "aurora-reserved-instance-size-flexible-within-class-type", "aurora-reserved-instance-billing-discount-not-physical",
     "aurora-reserved-instance-tied-to-type-and-region", "aurora-reserved-instance-consolidated-billing-shared", "aurora-reserved-instance-all-upfront-full-payment",
     "aurora-pricing-reserved-instances-exclude-storage", "aurora-pricing-reserved-instances-apply-across-configurations",
     "aurora-on-demand-billing-one-second-increments-ten-minute-minimum", "aurora-stop-cluster-up-to-seven-days",
     "aurora-stopped-cluster-charges-storage-not-instance-hours", "aurora-stop-start-manage-dev-test-costs", "aurora-cannot-stop-single-instance",
     "aurora-stop-not-with-cross-region-replica-or-blue-green", "aurora-stopped-cluster-no-config-changes-no-backups",
     "aurora-faq-database-savings-plan-35-percent", "aurora-pricing-database-savings-plans-cover-aurora", "aurora-pricing-aurora-usage-eligible-database-savings-plans",
     "aurora-pricing-database-savings-plans-apply-to-serverless", "aurora-pricing-data-transfer-same-az-ec2-free",
     "aurora-pricing-data-transfer-cross-az-ec2-charged", "aurora-pricing-extended-support-purpose", "aurora-pricing-extended-support-up-to-three-years",
     "aurora-change-extended-support-auto-enable", "rds-pricing-dimension-io-requests-magnetic-aurora"],
    {
        "problem": ("Aurora bills DB instances and storage and, in one configuration, every I/O request. An I/O-heavy workload can see a "
                    "large I/O bill that changes every month."),
        "trace": [
            "**Standard: pay per request.** With Aurora Standard you pay a [standard rate per 1 million requests for I/O operations] (aurora-standard-pays-per-million-io) on top of instances and storage.",
            "**I/O-Optimized: I/O included.** With Aurora I/O-Optimized you [pay only for the usage and storage] (aurora-io-optimized-no-io-charges), with [no additional charges for read and write I/O] (aurora-io-optimized-no-io-charges).",
            "**Choose by the I/O share.** I/O-Optimized is the best choice when I/O is [25% or more] (aurora-io-optimized-best-when-io-25-percent-or-more) of your Aurora spending; Standard is best below that ([less than 25%] (aurora-standard-best-when-io-under-25-percent)).",
            "**Switching has limits.** You can move to I/O-Optimized [once every 30 days] (aurora-io-switch-standard-to-io-optimized-once-every-30-days), and back to Standard [at any time] (aurora-io-switch-io-optimized-to-standard-any-time).",
        ],
        "table": ("Standard or I/O-Optimized (columns: Question | Aurora Standard | Aurora I/O-Optimized): I/O charges | [you pay per-request "
                  "for I/O] (aurora-faq-standard-pay-per-io-vs-io-optimized-included) | [included at no additional charge] "
                  "(aurora-faq-standard-pay-per-io-vs-io-optimized-included); Reserved Instances cover I/O | no | yes: I/O costs are "
                  "[only covered when your database cluster is configured] (aurora-pricing-reserved-instances-io-only-with-io-optimized) as "
                  "I/O-Optimized; Readers and writers | I/O is [counted the same way] (aurora-io-counted-same-writer-reader) on every DB "
                  "instance | no I/O bill at all."),
        "why": ("Why two models? For light I/O, paying per request is cheapest; for heavy I/O, AWS cites [improved price performance for "
                "I/O-intensive applications] (aurora-faq-io-optimized-fits-io-intensive-workloads) and a predictable bill."),
        "exam_signal": ("\"I/O-intensive\" or \"unpredictable I/O costs\" points to Aurora I/O-Optimized ([no additional charges for read and "
                        "write I/O] (aurora-io-optimized-no-io-charges)); \"low I/O, cost-sensitive\" points to Aurora Standard. Link the second "
                        "clause only if the trace has not used [less than 25%] (aurora-standard-best-when-io-under-25-percent)."),
        "exam_trap": "aurora-trap-io-optimized-always-cheaper",
        "exam_trap_text": ("> **Exam trap:** I/O-Optimized does not always cost less. It is the best choice at [25% or more] "
                           "(aurora-io-optimized-best-when-io-25-percent-or-more) of spending on I/O; below that share, Aurora Standard is the "
                           "cheaper choice. <!-- trap: aurora-trap-io-optimized-always-cheaper -->"),
        "body_extras": ("Only if words remain, one sentence: a steady cluster saves with Reserved Instances, which are [appropriate for "
                        "steady-state database workloads] (aurora-pricing-reserved-instances-steady-state). Reference only: stop a cluster for [up to seven days] "
                        "(aurora-stop-cluster-up-to-seven-days: B-list) and pay storage but no instance hours "
                        "(aurora-stopped-cluster-charges-storage-not-instance-hours); On-Demand billing per second with a [10-minute minimum "
                        "charge] (aurora-on-demand-billing-one-second-increments-ten-minute-minimum); up to 40% savings above the 25% share "
                        "(aurora-io-optimized-save-up-to-40-percent-above-25-percent-io); Database Savings Plans (volatile; chapter 41); RDS "
                        "Extended Support (volatile; reference only); EC2 to Aurora data transfer is free in one AZ "
                        "(aurora-pricing-data-transfer-same-az-ec2-free)."),
        "say_it": "The short answer is: Standard bills each I/O request, and I/O-Optimized has no I/O charges. The thing to watch is the I/O share of your bill.",
        "stop_and_answer": ("A cluster's Aurora bill is 40% I/O charges, and the team moved it to I/O-Optimized 10 days ago. Now they want to "
                            "move back to Standard for a week and then return to I/O-Optimized. Can they? Answer: they can move back to "
                            "Standard [at any time] (aurora-io-switch-io-optimized-to-standard-any-time), but the return to I/O-Optimized must "
                            "wait: the move is allowed [once every 30 days] (aurora-io-switch-standard-to-io-optimized-once-every-30-days). The "
                            "percentages and days are example values."),
    })

# 13 --------------------------------------------------------------------------------------------
sub("Data moves into Aurora by snapshot, by Aurora read replica or by AWS DMS", 3, 215, ["4.3.K7", "4.3.K8", "3.3.K7"],
    ["aurora-migrate-options-depend-on-engine-and-source", "aurora-migrate-from-rds-snapshot-or-replication", "aurora-faq-mysql-migration-snapshot-from-rds",
     "aurora-faq-postgresql-migration-snapshot-from-rds", "aurora-mysql-migrate-from-rds-snapshot-under-an-hour", "aurora-postgres-migrate-snapshot-from-rds",
     "aurora-rds-mysql-read-replica-for-migration", "aurora-rds-postgres-read-replica-for-migration", "aurora-mysql-read-replica-of-rds-mysql-binlog-async",
     "aurora-mysql-migrate-replica-lag-zero-then-stop-replication", "aurora-postgres-migrate-replica-lag-zero-stop-replication",
     "aurora-postgres-promote-stop-write-workload-on-source", "aurora-postgres-promotion-unlinks-source", "aurora-postgres-read-replica-migration-same-region-account",
     "aurora-mysql-migrate-replica-takes-hours-per-tib", "aurora-postgres-migrate-replica-hours-per-terabyte", "aurora-mysql-only-one-aurora-read-replica-per-rds-mysql",
     "aurora-mysql-no-aurora-replica-if-source-has-cross-region-replica", "aurora-mysql-migrate-by-setting-up-replication", "aurora-mysql-binlog-replication-with-mysql",
     "aurora-mysql-binlog-replication-external-mysql-inside-or-outside-aws", "aurora-faq-binlog-external-mysql", "aurora-mysql-binlog-source-or-replica",
     "aurora-mysql-binlog-only-innodb-tables", "aurora-faq-mysql-migration-mysqldump", "aurora-mysql-standard-import-export-tools-work",
     "aurora-postgres-import-from-s3", "aurora-migrate-heterogeneous-consider-sct", "aurora-postgres-non-postgres-source-use-dms",
     "aurora-faq-migration-dms-continuous-replication", "aurora-faq-babelfish-sql-server", "aurora-mysql-scale-reads-for-mysql-with-aurora-replica",
     "aurora-mysql-dr-read-replica-of-mysql", "aurora-mysql-replica-use-cluster-endpoint-address", "aurora-postgres-logical-replication-individual-tables",
     "aurora-postgres-logical-replication-same-region", "aurora-mysql-binlog-same-region-two-clusters", "aurora-dg-use-when-relational-modernize"],
    {
        "problem": ("A database already runs on Amazon RDS, on premises, or on another engine. The move must copy the data and switch the "
                    "application with as little downtime as the business accepts."),
        "trace": [
            "**Same engine from RDS: a snapshot.** You can migrate [from an RDS for PostgreSQL DB snapshot] (aurora-postgres-migrate-snapshot-from-rds) to an Aurora PostgreSQL cluster; for MySQL, snapshot migrations [typically complete in under an hour] (aurora-mysql-migrate-from-rds-snapshot-under-an-hour).",
            "**Same engine, short cutover: an Aurora read replica.** Aurora can build an Aurora read replica of the RDS DB instance for [migration to Aurora PostgreSQL] (aurora-rds-postgres-read-replica-for-migration), only [within the same AWS Region and account] (aurora-postgres-read-replica-migration-same-region-account); it can take [several hours per terabyte of data] (aurora-postgres-migrate-replica-hours-per-terabyte).",
            "**Cut over at zero lag.** [Stop all database write workload on the source] (aurora-postgres-promote-stop-write-workload-on-source); when the lag is zero, [you can stop replication] (aurora-postgres-migrate-replica-lag-zero-stop-replication) and the replica becomes a standalone cluster.",
            "**Another engine: convert, then copy.** From Oracle or SQL Server, AWS suggests the [AWS Schema Conversion Tool (AWS SCT)] (aurora-migrate-heterogeneous-consider-sct) for the schema and [AWS Database Migration Service (AWS DMS)] (aurora-postgres-non-postgres-source-use-dms) for the data.",
        ],
        "table": ("Which path (columns: Source | Path): RDS for MySQL or PostgreSQL, a maintenance window is fine | snapshot migration "
                  "([creating and restoring snapshots] (aurora-migrate-from-rds-snapshot-or-replication)); RDS for MySQL or PostgreSQL, short "
                  "cutover | Aurora read replica, then promote ([setting up one-way replication] (aurora-migrate-from-rds-snapshot-or-replication)); "
                  "MySQL outside RDS | binlog replication from [an external MySQL database] (aurora-mysql-binlog-replication-external-mysql-inside-or-outside-aws); "
                  "Oracle or SQL Server | AWS SCT, then AWS DMS (chapter 39 owns both tools). Two columns; no downtime figures: no fact gives them."),
        "why": ("Why an Aurora read replica for the move? The source keeps serving while the copy catches up, so the switch waits only for "
                "the last changes; AWS uses this replica for migration [rather than for ongoing replication] "
                "(aurora-rds-postgres-read-replica-for-migration)."),
        "exam_signal": ("\"migrate RDS for PostgreSQL to Aurora with minimal downtime\" points to an Aurora read replica, then promotion "
                        "([migration to Aurora PostgreSQL] (aurora-rds-postgres-read-replica-for-migration)); \"migrate Oracle to Aurora "
                        "PostgreSQL\" points to AWS SCT and AWS DMS ([AWS Schema Conversion Tool (AWS SCT)] (aurora-migrate-heterogeneous-consider-sct)). "
                        "If the trace uses both displays, link [different underlying engine than Aurora's] (aurora-migrate-heterogeneous-consider-sct) "
                        "in the second clause."),
        "exam_trap": None,
        "spot_the_bug": ("**Spot the bug.** A team moves RDS for PostgreSQL to Aurora with an Aurora read replica. To save time, it promotes the "
                         "replica at 09:00 while the application still writes to the RDS DB instance, and points the application at Aurora at "
                         "09:30. What is wrong? Reveal (about 50 words): the writes from 09:00 to 09:30 stay on RDS, because after promotion the "
                         "two databases [are unlinked] (aurora-postgres-promotion-unlinks-source). [Stop all database write workload on the "
                         "source] (aurora-postgres-promote-stop-write-workload-on-source) first, and promote when the lag of the [Aurora "
                         "PostgreSQL read replica is zero] (aurora-postgres-migrate-replica-lag-zero-stop-replication)."),
        "body_extras": ("Reference only: one Aurora read replica per RDS for MySQL DB instance (aurora-mysql-only-one-aurora-read-replica-per-rds-mysql); "
                        "standard tools work ([Standard MySQL import and export tools] (aurora-mysql-standard-import-export-tools-work)); Aurora "
                        "PostgreSQL can import from Amazon S3 (aurora-postgres-import-from-s3); Babelfish for SQL Server applications "
                        "(aurora-faq-babelfish-sql-server: FAQ only); logical replication of single tables (aurora-postgres-logical-replication-individual-tables)."),
        "say_it": "The short answer is: from RDS, promote an Aurora read replica. The thing to watch is stopping writes before the cutover.",
        "stop_and_answer": ("A company wants to move a 2 TB RDS for PostgreSQL database into Aurora PostgreSQL in a different AWS account, with "
                            "a short cutover. Can it use an Aurora read replica? Answer: no; that option works only [within the same AWS Region "
                            "and account] (aurora-postgres-read-replica-migration-same-region-account). It needs another path, for example a "
                            "snapshot. 2 TB is an example value."),
    })

# 14 --------------------------------------------------------------------------------------------
sub("Encryption at rest is set at creation and covers the whole cluster", 3, 220, ["3.3.S2"],
    ["aurora-encryption-uses-aws-kms-key", "aurora-faq-encryption-at-rest-kms", "aurora-encrypted-cluster-all-instances-logs-backups-snapshots",
     "aurora-faq-encryption-covers-backups-replicas", "aurora-encryption-same-kms-key-all-instances", "aurora-encrypted-cluster-snapshot-same-kms-key",
     "aurora-encryption-cannot-convert-unencrypted-in-place", "aurora-restore-unencrypted-snapshot-specify-kms-key", "aurora-sec-blue-green-encrypt-existing-cluster",
     "aurora-faq-cannot-encrypt-existing-instance", "aurora-encryption-cannot-turn-off", "aurora-encryption-kms-key-cannot-change",
     "aurora-replica-encryption-must-match-cluster", "aurora-encryption-transparent-no-client-changes", "aurora-disabled-kms-key-cluster-inaccessible-recoverable",
     "aurora-revoke-kms-access-does-not-affect-running-db", "aurora-change-default-encryption-new-clusters", "aurora-change-default-encryption-cannot-disable",
     "aurora-change-default-encryption-existing-clusters-unaffected", "aurora-change-default-encryption-clones-replicas-stay-unencrypted",
     "aurora-ssl-tls-connections-both-engines", "aurora-faq-encryption-in-transit-ssl", "aurora-postgres-rds-force-ssl-parameter",
     "aurora-mysql-require-secure-transport-parameter", "aurora-mysql-require-secure-transport-no-reboot", "aurora-mysql-require-secure-transport-default-by-version",
     "aurora-iam-db-auth-engines", "aurora-iam-db-auth-token-instead-of-password", "aurora-iam-db-auth-token-sigv4-15-minutes",
     "aurora-iam-db-auth-token-only-for-authentication", "aurora-iam-db-auth-traffic-ssl-tls", "aurora-iam-db-auth-central-access-management",
     "aurora-security-iam-db-auth-user-or-role-token", "aurora-sec-iam-controls-management-actions", "aurora-security-vpc-required-security-group",
     "aurora-security-group-default-deny", "aurora-public-access-controlled-by-security-group", "aurora-public-access-needs-all-public-subnets",
     "aurora-private-ip-public-access-option", "aurora-db-subnet-group-collection-of-subnets", "aurora-faq-runs-in-vpc-full-control",
     "aurora-faq-vpc-supported", "aurora-vpc-no-additional-cost", "aurora-default-vpc-new-clusters-created-there", "aurora-faq-database-port-access",
     "aurora-security-kerberos-with-directory-service", "aurora-das-near-real-time-monitoring", "aurora-das-pushes-to-kinesis",
     "aurora-das-requires-kinesis-and-kms", "aurora-das-started-at-cluster-level", "aurora-das-dbas-no-access-to-streams", "aurora-faq-guardduty-rds-protection",
     "aurora-faq-hipaa-eligible", "aurora-mysql-cross-region-replica-must-be-encrypted-if-source", "aurora-copy-encrypted-snapshot-cross-region-destination-key"],
    {
        "problem": ("A security review asks two questions: is the data encrypted on disk, in every backup and replica, and is it "
                    "encrypted on the network?"),
        "trace": [
            "**One key for the cluster.** Aurora [uses an AWS Key Management Service key] (aurora-encryption-uses-aws-kms-key); every DB instance shares storage [encrypted with the same KMS key] (aurora-encryption-same-kms-key-all-instances).",
            "**Every copy follows.** In an encrypted cluster, the instances and the [logs, backups, and snapshots are encrypted] (aurora-encrypted-cluster-all-instances-logs-backups-snapshots).",
            "**Existing clusters: restore, not modify.** You [can't convert an unencrypted DB cluster] (aurora-encryption-cannot-convert-unencrypted-in-place) to an encrypted one, but you can [restore an unencrypted snapshot] (aurora-encryption-cannot-convert-unencrypted-in-place) to an encrypted cluster if you [specify a KMS key when you restore] (aurora-restore-unencrypted-snapshot-specify-kms-key).",
            "**On the network: TLS.** Clients can [encrypt a connection to a DB cluster] (aurora-ssl-tls-connections-both-engines) with TLS; Aurora PostgreSQL requires it through the `rds.force_ssl` parameter ([use `rds.force_ssl` parameter] (aurora-postgres-rds-force-ssl-parameter)), Aurora MySQL through the [`require_secure_transport` DB cluster parameter] (aurora-mysql-require-secure-transport-parameter).",
        ],
        "table": ("Which control answers which question (columns: Question | Control): Who can reach the database port | a VPC security group: "
                  "at first, the [firewall prevents any database access] (aurora-security-group-default-deny); Who can create or delete clusters "
                  "| IAM policies ([you use AWS Identity and Access Management (IAM)] (aurora-sec-iam-controls-management-actions)); Sign in "
                  "without a password | IAM database authentication: [use an authentication token] (aurora-iam-db-auth-token-instead-of-password) "
                  "with a [lifetime of 15 minutes] (aurora-iam-db-auth-token-sigv4-15-minutes); Data on disk | a KMS key chosen when you create "
                  "the cluster. Then the Try it callout."),
        "why": ("Why is it cheap to turn on? Encryption is transparent: you [don't need to modify your database client applications] "
                "(aurora-encryption-transparent-no-client-changes)."),
        "exam_signal": ("\"encrypt an existing unencrypted Aurora cluster\" points to a snapshot restored with a KMS key ([specify a KMS key when "
                        "you restore] (aurora-restore-unencrypted-snapshot-specify-kms-key)); \"all connections must use TLS\" points to the "
                        "engine's cluster parameter. Write the second clause without a second link if the trace already linked both parameter facts."),
        "exam_trap": None,
        "try_it": ("aurora-t03, after the table: one sentence ('Require TLS in an Aurora MySQL cluster parameter group, and see that the PostgreSQL "
                   "setting does not exist there.'), then 'See [3-do.md](3-do.md). <!-- task: aurora-t03 -->'."),
        "body_extras": ("Only if words remain, one sentence: new clusters are now [encrypted by default with an AWS owned key] "
                        "(aurora-change-default-encryption-new-clusters; volatile; it becomes a Changed recently entry only when the fact request "
                        "is filled). Reference only: you [can't turn off encryption] (aurora-encryption-cannot-turn-off) and [can't change the KMS "
                        "key] (aurora-encryption-kms-key-cannot-change); a blue/green deployment can also encrypt a cluster "
                        "(aurora-sec-blue-green-encrypt-existing-cluster); a disabled key makes the cluster inaccessible "
                        "(aurora-disabled-kms-key-cluster-inaccessible-recoverable); clusters must be in a VPC "
                        "(aurora-security-vpc-required-security-group); public access needs every subnet of the group to be public "
                        "(aurora-public-access-needs-all-public-subnets); Database Activity Streams send activity to Kinesis "
                        "(aurora-das-pushes-to-kinesis; chapter 37); Kerberos with Directory Service (aurora-security-kerberos-with-directory-service)."),
        "say_it": "The short answer is: turn on encryption when you create the cluster, and require TLS in its parameter group. The thing to watch is old clusters: restore to encrypt.",
        "stop_and_answer": ("An unencrypted Aurora MySQL cluster must become encrypted. The team plans to add an encrypted Aurora Replica and then "
                            "fail over to it. Will that work? Answer: no; all DB instances share one volume, and you [can't create an encrypted "
                            "Aurora Replica] (aurora-replica-encryption-must-match-cluster) for an unencrypted cluster. Restore a snapshot and "
                            "[specify a KMS key when you restore] (aurora-restore-unencrypted-snapshot-specify-kms-key)."),
    })

# Numbers, Decision record, FAQ -------------------------------------------------------------------
BRIEF["sections"].append({
    "file": "2-deep.md", "section": "numbers-that-decide-answers", "heading": "Numbers that decide answers", "bullets": [],
    "facts": ["aurora-replicas-up-to-15-in-addition-to-primary", "aurora-storage-six-copies-three-azs", "aurora-failover-time-with-replica-guide",
              "aurora-failover-time-without-replica", "aurora-replica-lag-under-100-ms", "aurora-global-replication-latency-under-1-second",
              "aurora-global-promote-secondary-under-1-minute", "aurora-backup-retention-period-range-1-35-days",
              "aurora-io-optimized-best-when-io-25-percent-or-more", "aurora-io-switch-standard-to-io-optimized-once-every-30-days",
              "aurora-backtrack-window-limit-72-hours", "aurora-promotion-priority-range", "aurora-global-secondary-cluster-max-16-reader-instances",
              "aurora-serverless-acu-about-2-gib-memory", "aurora-serverless-capacity-range-0-256-acu-half-acu-steps",
              "aurora-serverless-auto-pause-resume-about-15-seconds", "aurora-backup-latest-restorable-time-within-5-minutes",
              "aurora-backup-retention-default-1-day", "aurora-stop-cluster-up-to-seven-days", "aurora-storage-segment-size-10-gib"],
    "status": "write", "minutes": 3,
    "plan": ("The A-list and B-list tables of numbers (see numbers), in the form of CONVENTIONS D10, at most 290 words. No entry under the B-list: "
             "no not-examinable change is taught in this chapter (the two not-examinable changes of 2026 have no changed record; see "
             "changed_recently.considered_not_used)."),
})
BRIEF["sections"].append({
    "file": "2-deep.md", "section": "decision-record", "heading": "Decision record", "bullets": ["3.3.S4", "2.1.K15", "2.2.K6"],
    "facts": ["rds-read-replica-async-read-only", "rds-storage-ebs-striping", "rds-faq-read-replica-own-endpoint",
              "dynamodb-decision-guide-elasticache-caching-layer", "aurora-adding-replicas-read-same-volume-offload", "aurora-replica-lag-under-100-ms",
              "aurora-replicas-up-to-15-in-addition-to-primary", "aurora-reader-endpoint-connection-balancing-read-only",
              "aurora-failover-time-with-replica-guide", "aurora-existing-mysql-postgres-code-works", "aurora-faq-global-db-definition",
              "aurora-postgres-no-cross-region-aurora-replicas", "aurora-postgres-migrate-replica-hours-per-terabyte",
              "aurora-faq-standard-pay-per-io-vs-io-optimized-included", "aurora-serverless-choose-multitenant-dev-test"],
    "status": "write", "minutes": 3,
    "plan": "Five bold fields of CONVENTIONS D11 (see decision_record), the before and after diagrams embedded as noted there. At most 270 words.",
})
BRIEF["sections"].append({
    "file": "2-deep.md", "section": "faq-quick-fire", "heading": "FAQ quick-fire", "bullets": [],
    "facts": ["aurora-faq-automated-backups-always-on", "aurora-faq-low-priority-replica-still-promoted-if-needed", "aurora-faq-replica-lag-tens-of-ms-same-region",
              "aurora-faq-cross-region-physical-or-logical", "aurora-faq-global-db-no-code-change-writer-endpoint", "aurora-faq-snapshot-restore-new-instance",
              "aurora-faq-replication-not-charged", "aurora-serverless-faq-mixed-cluster-with-provisioned", "aurora-faq-encryption-covers-backups-replicas",
              "aurora-faq-no-special-drivers"],
    "status": "write", "minutes": 5,
    "plan": ("Ten FAQ items in the form of CONVENTIONS D12 (see faq): a can-or-cannot question, the short answer with a fact link, then the "
             "verbatim AWS quote block from the item's FAQ page (the evidence page of its fact), holding the one whole sentence of the "
             "evidence quote that carries the answer. At most 430 words."),
})
