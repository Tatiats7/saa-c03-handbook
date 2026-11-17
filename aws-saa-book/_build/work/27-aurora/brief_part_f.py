# brief-27, part F: terms, tasks, speak, cards, diagrams, fact requests, notes.

BRIEF["terms"] = ["read-replica", "fail-over", "scale-out", "serverless", "durability", "recovery-point-objective",
                  "recovery-time-objective", "asynchronous"]
BRIEF["term_requests"] = [
    "Aurora DB cluster (one or more DB instances and a cluster volume)", "cluster volume", "primary instance (writer)", "Aurora Replica",
    "cluster endpoint (writer endpoint)", "reader endpoint", "custom endpoint", "instance endpoint", "promotion tier (failover priority)",
    "Aurora Auto Scaling", "Aurora capacity unit (ACU)", "Aurora Serverless v2 (db.serverless)", "auto-pause (automatic pause and resume)",
    "mixed-configuration cluster", "Aurora Global Database (primary cluster, secondary cluster)", "global writer endpoint", "write forwarding",
    "switchover (Aurora Global Database)", "managed failover (Aurora Global Database)", "headless secondary cluster",
    "point-in-time recovery (latest restorable time)", "Backtrack", "Aurora clone (copy-on-write)", "Aurora Standard", "Aurora I/O-Optimized",
    "Aurora read replica (migration from RDS; cross-Region binlog replica)", "binary log (binlog) replication", "IAM database authentication",
]
BRIEF["terms_note"] = ("terms lists only bank terms (B11). 'asynchronous' is taught for Aurora Replicas and Global Database replication; its bank "
                       "collocations are about Lambda, so the words table does not use it. Respell only bank respellings (STYLE 4).")

BRIEF["tasks"] = [
    {"id": "aurora-t01", "type": "look", "title": "Read your Aurora quota and find the db.serverless instance class",
     "section": "1-fast.md#look-first",
     "kills": "\"Aurora Serverless v2 is a separate database product with its own kind of cluster.\"",
     "trap": None, "pass_route": False, "status": "write",
     "plan": ("In AWS CloudShell, read-only, 3 minutes, $0. (1) aws rds describe-account-attributes --query "
              "\"AccountQuotas[?AccountQuotaName=='DBClusters']\" --output table: expect the quota of DB clusters, [40 Aurora DB clusters] "
              "(aurora-quota-db-clusters-per-region) by default, adjustable. (2) aws rds describe-db-engine-versions --engine aurora-postgresql "
              "--default-only --query \"DBEngineVersions[].{Version:EngineVersion,Family:DBParameterGroupFamily}\" --output table: expect one "
              "default Aurora PostgreSQL version and its parameter group family. (3) aws rds describe-orderable-db-instance-options --engine "
              "aurora-postgresql --db-instance-class db.serverless --query \"OrderableDBInstanceOptions[0].{Class:DBInstanceClass,Version:EngineVersion}\" "
              "--output table: expect db.serverless listed like any instance class: Aurora Serverless v2 is a [special DB instance class type] "
              "(aurora-serverless-db-serverless-instance-class-type) in an ordinary cluster. Creates nothing. The writer confirms each operation and "
              "the query fields with tasks check-cli --reference; no pipe character inside a --query (T104)."),
     "facts": ["aurora-quota-db-clusters-per-region", "aurora-serverless-db-serverless-instance-class-type", "aurora-is-managed-relational-engine"]},
    {"id": "aurora-t02", "type": "try", "title": "Set a recovery point limit for an Aurora PostgreSQL global database",
     "section": "2-deep.md#" + anchor("A secondary Region takes over by failover after an outage, by switchover when healthy"),
     "kills": "\"Nobody can set an upper bound on the data that an Aurora global database loses in a failover.\"",
     "trap": "aurora-trap-global-failover-no-data-loss", "pass_route": True, "status": "write",
     "plan": ("In AWS CloudShell, about 8 minutes, $0: a DB cluster parameter group has no charge and no DB cluster is created (state the cost "
              "line as $0; T109 needs no cost fact for $0). Steps: capture the parameter group family of the default Aurora PostgreSQL version "
              "(aws rds describe-db-engine-versions --engine aurora-postgresql --default-only --query DBEngineVersions[0].DBParameterGroupFamily, "
              "capture FAMILY); aws rds create-db-cluster-parameter-group --db-cluster-parameter-group-name "
              "saa-aurora-t02 --db-parameter-group-family $FAMILY --description \"saa global RPO\" --tags Key=book,Value=saa "
              "Key=task,Value=aurora-t02. Break it: predict 'Can you set a recovery point limit of 10 seconds?'; aws rds "
              "modify-db-cluster-parameter-group --db-cluster-parameter-group-name saa-aurora-t02 --parameters "
              "\"ParameterName=rds.global_db_rpo,ParameterValue=10,ApplyMethod=immediate\": expect an InvalidParameterValue error; explain: valid "
              "values start at [20 seconds] (aurora-global-rpo-parameter-range). Fix: the same modify with ParameterValue=20, expect success; "
              "aws rds describe-db-cluster-parameters --db-cluster-parameter-group-name saa-aurora-t02 --source user --query "
              "\"Parameters[].{Name:ParameterName,Value:ParameterValue}\" --output table: expect rds.global_db_rpo with value 20. Say in a step "
              "text what the parameter does: with it you [manage the recovery point objective (RPO)] "
              "(aurora-global-db-postgres-rpo-managed-by-parameter), and if all secondaries fall behind, [Aurora pauses transactions on the "
              "primary cluster] (aurora-global-db-rpo-blocks-commits-when-all-secondaries-behind). Cleanup: aws rds "
              "delete-db-cluster-parameter-group --db-cluster-parameter-group-name saa-aurora-t02. Verify: aws rds "
              "describe-db-cluster-parameter-groups --db-cluster-parameter-group-name saa-aurora-t02 with expect 'DBParameterGroupNotFound' "
              "(T108 by-name exception of R6). Label 'checked against docs, not run in a real account'. The writer confirms with tasks "
              "check-cli --reference that create-db-cluster-parameter-group takes --tags in the Key=,Value= shape, that rds.global_db_rpo is a "
              "modifiable parameter of the default aurora-postgresql family, and the exact error code of the break step; if the parameter is not "
              "in the family's list, the writer reports the task for a re-plan instead of guessing."),
     "facts": ["aurora-global-rpo-parameter-range", "aurora-global-db-postgres-rpo-managed-by-parameter",
               "aurora-global-db-rpo-blocks-commits-when-all-secondaries-behind", "aurora-global-db-rpo-parameter-dynamic",
               "aurora-global-db-two-region-keep-default-rpo-secondary"]},
    {"id": "aurora-t03", "type": "try", "title": "Require TLS in an Aurora MySQL cluster parameter group",
     "section": "2-deep.md#" + anchor("Encryption at rest is set at creation and covers the whole cluster"),
     "kills": "\"Aurora MySQL and Aurora PostgreSQL use the same parameter to require TLS.\"",
     "trap": None, "pass_route": False, "status": "write",
     "plan": ("In AWS CloudShell, about 8 minutes, $0 (no DB cluster is created). Steps: capture the parameter group family of the default "
              "Aurora MySQL version (aws rds describe-db-engine-versions --engine aurora-mysql --default-only --query "
              "DBEngineVersions[0].DBParameterGroupFamily, capture FAMILY); aws rds create-db-cluster-parameter-group "
              "--db-cluster-parameter-group-name saa-aurora-t03 --db-parameter-group-family $FAMILY --description \"saa require TLS\" --tags "
              "Key=book,Value=saa Key=task,Value=aurora-t03. Break it: predict 'Can you set rds.force_ssl in an Aurora MySQL group?'; aws rds "
              "modify-db-cluster-parameter-group --db-cluster-parameter-group-name saa-aurora-t03 --parameters "
              "\"ParameterName=rds.force_ssl,ParameterValue=1,ApplyMethod=immediate\": expect an error (the parameter does not exist in this "
              "family); explain: Aurora PostgreSQL uses the `rds.force_ssl` parameter ([use `rds.force_ssl` parameter] "
              "(aurora-postgres-rds-force-ssl-parameter)), Aurora MySQL the [`require_secure_transport` DB cluster parameter] "
              "(aurora-mysql-require-secure-transport-parameter). Fix: the same modify with "
              "\"ParameterName=require_secure_transport,ParameterValue=ON,ApplyMethod=immediate\", expect success; describe-db-cluster-parameters "
              "--source user: expect require_secure_transport ON. Step text: the change needs no reboot ([don't need to reboot your DB cluster] "
              "(aurora-mysql-require-secure-transport-no-reboot)). Cleanup: aws rds delete-db-cluster-parameter-group "
              "--db-cluster-parameter-group-name saa-aurora-t03. Verify: describe-db-cluster-parameter-groups with the name, expect "
              "'DBParameterGroupNotFound' (T108 by-name exception). Label 'checked against docs, not run in a real account'. The writer confirms "
              "the error code of the break step with tasks check-cli --reference; the default value of require_secure_transport depends on the "
              "version (aurora-mysql-require-secure-transport-default-by-version): the task does not claim it."),
     "facts": ["aurora-mysql-require-secure-transport-parameter", "aurora-postgres-rds-force-ssl-parameter", "aurora-mysql-require-secure-transport-no-reboot",
               "aurora-mysql-require-secure-transport-default-by-version", "aurora-ssl-tls-connections-both-engines"]},
]

BRIEF["speak"] = [
    {"id": "aurora-s01", "kind": "explain", "persona": "Ben, CTO of Callvale",
     "prompt": "It is still PostgreSQL. What do I get from Aurora that RDS did not give me?",
     "section": "2-deep.md#" + anchor("Aurora Replicas read the shared volume, so replica lag stays low"), "pass_route": True,
     "facts": ["aurora-adding-replicas-read-same-volume-offload", "aurora-replica-lag-under-100-ms", "aurora-replicas-up-to-15-in-addition-to-primary",
               "aurora-reader-endpoint-connection-balancing-read-only", "aurora-failover-time-with-replica-guide", "aurora-storage-six-copies-three-azs",
               "aurora-faq-global-db-definition", "aurora-existing-mysql-postgres-code-works", "aurora-faq-standard-pay-per-io-vs-io-optimized-included"],
     "note": ("Ben talks in short technical sentences and distrusts what he must run at night. Short answer: the same PostgreSQL, but on a "
              "storage layer that all instances share, so replicas stay milliseconds behind instead of forty seconds. How it works: the writer "
              "stores each change once, in six copies across three zones; Aurora Replicas read that same storage; one reader endpoint spreads "
              "the dashboard connections; if the writer fails, a replica takes over in under a minute behind the same endpoint. Watch: the bill "
              "changes shape: storage you use, and I/O per request on Aurora Standard; the move needs a short cutover. In your case: 'Which "
              "dashboards break first when the replica is behind?' Must not say: 'Aurora Replicas copy the data like RDS replicas'; 'replica "
              "lag is zero'; 'Aurora is a different engine, so you rewrite the SQL'. Numbers as words from the say forms: well under a hundred "
              "milliseconds; fifteen Aurora Replicas besides the primary; under a minute; six copies, three Availability Zones.")},
    {"id": "aurora-s02", "kind": "compare", "persona": "a startup founder in office hours",
     "prompt": "Aurora Serverless v2 or a provisioned instance: which one should our new SaaS database use?",
     "section": "2-deep.md#" + anchor("Aurora Serverless v2 changes capacity with load inside a range you set"), "pass_route": False,
     "facts": ["aurora-serverless-choose-variable-spiky-workloads", "aurora-serverless-provisioned-suited-to-steady-workloads",
               "aurora-serverless-acu-about-2-gib-memory", "aurora-serverless-specify-min-max-capacity-range",
               "aurora-serverless-scaling-with-open-connections-no-quiet-point", "aurora-serverless-faq-mixed-cluster-with-provisioned",
               "aurora-pricing-reserved-instances-steady-state", "aurora-serverless-auto-pause-min-capacity-zero"],
     "note": ("First sentence starts 'Both': both run the same Aurora engine on the same storage; the difference is how capacity is sized. "
              "Short answer: Serverless v2 while the load is new and uneven; provisioned, with Reserved Instances, once it is steady. How it "
              "works: Serverless v2 grows and shrinks the instance in small steps inside a range you set, even with connections open; a "
              "provisioned instance has a fixed size that you choose. Watch: the minimum you set decides the idle cost; one cluster can mix both, "
              "so you can switch later. In your case: 'Do you know your peak yet, and how often does it come?' Must not say: 'serverless is "
              "always cheaper'; 'serverless means no instance'; 'you must rebuild the cluster to change'. Numbers as words: about two gibibytes "
              "of memory per ACU.")},
    {"id": "aurora-s03", "kind": "compare", "persona": "a startup CTO you advise",
     "prompt": "Aurora Global Database or DynamoDB global tables: which one gives us a second Region?",
     "section": "2-deep.md#" + anchor("Aurora Global Database copies the cluster volume to read-only Regions"), "pass_route": False,
     "facts": ["aurora-global-db-only-primary-writes", "aurora-global-replication-latency-under-1-second", "aurora-global-db-failover-use-for-unplanned-outage",
               "aurora-global-rpo-typically-seconds-guide", "dynamodb-global-table-any-replica-serves-reads-writes",
               "dynamodb-gt-multi-active-no-failover-needed", "dynamodb-no-joins-heart-of-nosql-modeling"],
     "note": ("First sentence starts 'Both': both keep a copy of your data in another Region; the difference is who can write. Short answer: "
              "Aurora Global Database if the data is relational; DynamoDB global tables if every Region must write. How it works: Aurora has one "
              "writer Region and read-only secondaries, replicated in about a second, and you fail over after an outage; in a global table every "
              "Region reads and writes, and no database failover is needed. Watch: an Aurora failover can lose a few seconds of writes; DynamoDB "
              "needs a key-value design without joins. In your case: 'Do your users in the second Region need to write, or mostly read?' Must "
              "not say: 'every Aurora Region accepts writes'; 'Aurora failover loses nothing'; 'DynamoDB supports joins'. Numbers as words: "
              "typically under one second; a few seconds of possible data loss.")},
    {"id": "aurora-s04", "kind": "decide", "persona": "Ana, CEO of Callvale",
     "prompt": "Ben wants to pay for I/O-Optimized on our main database. Is it worth it?",
     "section": "2-deep.md#" + anchor("Aurora Standard charges for each I/O, and I/O-Optimized includes it"), "pass_route": False,
     "facts": ["aurora-io-optimized-best-when-io-25-percent-or-more", "aurora-standard-best-when-io-under-25-percent", "aurora-io-optimized-no-io-charges",
               "aurora-standard-pays-per-million-io", "aurora-io-switch-standard-to-io-optimized-once-every-30-days",
               "aurora-io-switch-io-optimized-to-standard-any-time", "aurora-faq-io-optimized-works-with-reserved-instances"],
     "note": ("Ana uses no AWS terms: explain I/O the first time as 'each time the database reads or writes a piece of data on disk'. Short "
              "answer: it depends on one number on the bill: the share of I/O charges. How it works: on the standard plan we pay for each I/O "
              "request; on I/O-Optimized I/O has no charge; AWS calls it the best choice at a quarter or more of the database spend. Watch: we "
              "can go back to the standard plan at any time, but move to I/O-Optimized only once every thirty days, so decide from a full month "
              "of bills. In your case: 'Can finance pull last month's database bill split by item?' Must not say: 'I/O-Optimized is always "
              "cheaper'; 'I/O-Optimized makes the database faster'; 'we can switch back and forth every week'. Numbers as words: a quarter or "
              "more; once every thirty days.")},
]

C = BRIEF["cards"] = []


def card(t, deck, section, facts, trap, front, back):
    C.append({"id": "aurora-c%03d" % (len(C) + 1), "type": t, "deck": deck, "section": section, "facts": facts, "trap": trap,
              "front": front, "back": back})


S_ = lambda p: sec(p)  # noqa: E731
card("number", "core", S_("Aurora Replicas read"), ["aurora-replicas-up-to-15-in-addition-to-primary"], None,
     "In Aurora, how many Aurora Replicas can one DB cluster have?", "Up to 15 Aurora Replicas in addition to the primary DB instance.")
card("number", "core", S_("Every write is stored"), ["aurora-storage-six-copies-three-azs"], "aurora-trap-single-instance-is-ha",
     "In Aurora, how many copies of the data does the cluster volume keep?", "Six copies, across three Availability Zones.")
card("number", "core", S_("When the writer fails"), ["aurora-failover-time-with-replica-guide"], None,
     "In Aurora, how long does a failover to an Aurora Replica typically take?", "Less than 60 seconds, often less than 30 seconds.")
card("number", "core", S_("When the writer fails"), ["aurora-failover-time-without-replica"], "aurora-trap-single-instance-is-ha",
     "In Aurora, a cluster has no Aurora Replica. How long does recovery typically take?", "Less than 10 minutes: Aurora recreates the primary.")
card("number", "core", S_("Aurora Replicas read"), ["aurora-replica-lag-under-100-ms"], "aurora-trap-replicas-copy-data",
     "In Aurora, how far behind the writer is an Aurora Replica usually?", "Much less than 100 milliseconds.")
card("number", "core", S_("Aurora Global Database copies"), ["aurora-global-replication-latency-under-1-second"], None,
     "In Aurora Global Database, what is the typical replication latency to a secondary Region?", "Typically under a second.")
card("number", "core", S_("A secondary Region takes over"), ["aurora-global-promote-secondary-under-1-minute"], None,
     "In Aurora Global Database, how fast does AWS say a secondary Region can be promoted?", "In less than 1 minute.")
card("number", "core", S_("Backups are continuous"), ["aurora-backup-retention-period-range-1-35-days"], None,
     "In Aurora, what is the range of the backup retention period?", "1–35 days.")
card("differ", "core", S_("Aurora Replicas read"), ["aurora-adding-replicas-read-same-volume-offload"], "aurora-trap-replicas-copy-data",
     "Aurora Replica or RDS read replica: which one reads the writer's own storage volume?", "The Aurora Replica.")
card("differ", "core", S_("The reader endpoint"), ["aurora-cluster-endpoint-only-one-for-writes"], "aurora-trap-writes-through-reader-endpoint",
     "In Aurora, cluster endpoint or reader endpoint: which one accepts writes?", "The cluster endpoint.")
card("decide", "core", S_("Aurora Serverless v2"), ["aurora-serverless-choose-variable-spiky-workloads"], None,
     "In Aurora, the load is spiky and hard to predict. Which capacity option fits?", "Aurora Serverless v2: capacity follows the load inside your range.")
card("decide", "core", S_("Aurora Global Database copies"), ["aurora-faq-global-db-definition", "aurora-global-replication-latency-under-1-second"], None,
     "A relational database must recover in another Region with an RPO of seconds. What do you use?", "Aurora Global Database.")
card("cannot", "core", S_("Aurora Global Database copies"), ["aurora-global-db-only-primary-writes"], "aurora-trap-global-all-regions-write",
     "In an Aurora global database, can a secondary cluster accept writes on its own?", "No. Only the primary cluster writes; write forwarding sends writes there.")
card("cannot", "core", S_("Encryption at rest"), ["aurora-encryption-cannot-convert-unencrypted-in-place"], "aurora-trap-encrypt-existing-in-place",
     "In Aurora, can you turn on encryption for an existing unencrypted cluster?", "No. Restore a snapshot to a new cluster with a KMS key.")
card("differ", "extended", S_("A secondary Region takes over"), ["aurora-global-db-failover-use-for-unplanned-outage"], "aurora-trap-switchover-for-region-outage",
     "In Aurora Global Database, failover or switchover: which one is for a Region outage?", "Failover. Switchover needs healthy clusters.")
card("cannot", "extended", S_("A secondary Region takes over"), ["aurora-global-db-failover-can-lose-writes-consistent-state"], "aurora-trap-global-failover-no-data-loss",
     "In Aurora Global Database, is a failover after a Region outage free of data loss?", "No. Writes that were not yet replicated can be lost.")
card("cannot", "extended", S_("Aurora Auto Scaling adds"), ["aurora-autoscaling-writer-not-scaled"], "aurora-trap-auto-scaling-scales-writer",
     "In Aurora, can Aurora Auto Scaling add capacity for writes?", "No. It scales only the reader instances.")
card("cannot", "extended", S_("The reader endpoint"), ["aurora-reader-endpoint-balances-connections-not-queries"], "aurora-trap-reader-endpoint-balances-queries",
     "In Aurora, does the reader endpoint balance each query?", "No. It balances connections, not individual queries.")
card("cannot", "extended", S_("Aurora Serverless v2"), ["aurora-serverless-min-capacity-above-zero-no-pause"], "aurora-trap-serverless-pauses-whenever-idle",
     "In Aurora Serverless v2, does an instance pause if the minimum capacity is above zero ACUs?", "No. It pauses only with a minimum of zero ACUs.")
card("cannot", "extended", S_("Aurora Global Database copies"), ["aurora-postgres-no-cross-region-aurora-replicas"], "aurora-trap-postgres-cross-region-replica",
     "Can an Aurora PostgreSQL cluster have a cross-Region Aurora Replica?", "No. Use Aurora Global Database.")
card("cannot", "extended", S_("Backups are continuous"), ["aurora-pitr-creates-new-cluster"], "aurora-trap-restore-in-place",
     "In Aurora, does a point-in-time restore roll back the running cluster?", "No. It creates a new DB cluster.")
card("decide", "extended", S_("Aurora Standard charges"), ["aurora-io-optimized-best-when-io-25-percent-or-more"], "aurora-trap-io-optimized-always-cheaper",
     "In Aurora, I/O is a large share of the database bill. Which storage configuration fits?", "Aurora I/O-Optimized, from 25% or more of the spend.")
card("cannot", "extended", S_("Backups are continuous"), ["aurora-backup-cannot-disable-automated"], None,
     "In Aurora, can you turn off automated backups?", "No. They are always on.")
card("decide", "extended", S_("The reader endpoint"), ["aurora-custom-endpoint-set-of-chosen-instances"], None,
     "In Aurora, reports must run only on two large replicas. What do the reports connect to?", "A custom endpoint with those two replicas.")
card("cannot", "extended", S_("Backups are continuous"), ["aurora-backtrack-not-for-postgresql"], None,
     "Can you backtrack an Aurora PostgreSQL cluster?", "No. Backtrack is an Aurora MySQL feature.")
card("decide", "extended", S_("Backups are continuous"), ["aurora-clone-test-with-production-data", "aurora-clone-copy-on-write-storage-on-change"], None,
     "In Aurora, you need a test copy of production data within minutes. What do you use?", "An Aurora clone: it stores only changed pages.")
card("decide", "extended", S_("Data moves into Aurora"), ["aurora-migrate-heterogeneous-consider-sct"], None,
     "Moving Oracle to Aurora PostgreSQL: which tool converts the schema?", "AWS Schema Conversion Tool (AWS SCT).")
card("decide", "extended", S_("Data moves into Aurora"), ["aurora-rds-postgres-read-replica-for-migration"], None,
     "RDS for PostgreSQL to Aurora, same account and Region, short cutover: which path?", "An Aurora read replica, promoted at zero lag.")
card("differ", "extended", S_("Aurora Global Database copies"), ["dynamodb-global-table-any-replica-serves-reads-writes", "aurora-global-db-only-primary-writes"], "aurora-trap-global-all-regions-write",
     "Aurora Global Database or DynamoDB global tables: which one accepts writes in every Region?", "DynamoDB global tables.")
card("decide", "extended", S_("Aurora Serverless v2"), ["aurora-serverless-auto-pause-min-capacity-zero", "aurora-serverless-auto-pause-no-compute-charge-while-paused"], "aurora-trap-serverless-pauses-whenever-idle",
     "In Aurora Serverless v2, a dev database is idle most of the week. How do you stop paying for its compute?", "Set the minimum capacity to zero ACUs, so it pauses.")
card("cannot", "extended", S_("An Aurora cluster runs"), ["aurora-add-instance-no-data-copy"], "aurora-trap-replicas-copy-data",
     "In Aurora, does a new DB instance get its own copy of the data?", "No. It connects to the shared cluster volume.")
card("decide", "extended", S_("Backups are continuous"), ["aurora-snapshots-do-not-expire"], None,
     "In Aurora, a restorable copy must be kept for many years. What do you use?", "Manual DB cluster snapshots: they do not expire.")

BRIEF["card_plan"] = {
    "core": 14, "extended": 18, "number_cards_equal_a_list_rows": 8,
    "rule": ("Fronts and backs above are drafts for the card writer: one fact per card, an answer of at most 12 words, a display of a fact for "
             "any number with a unit (up to 15 Aurora Replicas in addition to the primary DB instance, six copies, less than 60 seconds, less "
             "than 30 seconds, less than 10 minutes, much less than 100 milliseconds, typically under a second, less than 1 minute, 1–35 days, "
             "25% or more are the displays; write the back so that the display stands in it; trim the c001 back if it passes 12 words: 'Up to "
             "15 Aurora Replicas in addition to the primary DB instance.' is 12 words), and the context named at the start of the front. No "
             "front holds a number with a unit that is not a display of a card fact ('many years', not '7 years'). No absolute word without a "
             "fact of the card that supports it. aurora-c029 rests on the volatile scale-to-zero change: keep it in the extended deck and never "
             "turn it into a question key."),
}

BRIEF["diagrams"] = [
    {"id": "aurora-hero", "kind": "sequence",
     "placement": "1-fast.md#in-one-breath (behind 'Predict the picture: when an application writes to an Aurora cluster with two Aurora Replicas, where does the data go, and where do the replicas read it from?')",
     "title": "A write, the shared volume, the replicas and a failover",
     "claim": "Writes go through the writer into one volume with six copies, and the Aurora Replicas read that same volume.",
     "alt": ("A sequence with four participants: an application, the writer DB instance, the cluster volume in three Availability Zones, and an "
             "Aurora Replica. The application writes through the cluster endpoint, the writer stores the change in the volume, the replica "
             "reads the same volume for queries that come through the reader endpoint, and after a failure the replica becomes the writer."),
     "say": [
         "The application sends writes to the cluster endpoint, which connects to the current primary DB instance.",
         "Aurora synchronously replicates the data across Availability Zones to six storage nodes.",
         "Read-only connections use the reader endpoint, which spreads them among the Aurora Replicas.",
         "Aurora Replicas connect to the same storage volume as the writer, so no data is copied to them.",
         "If the writer fails, Aurora automatically fails over to an Aurora Replica, and the cluster endpoint follows it.",
     ],
     "facts_for_steps": ["aurora-cluster-endpoint-connects-to-current-primary", "aurora-synchronous-replication-to-six-storage-nodes",
                         "aurora-reader-endpoint-connection-balancing-read-only", "aurora-adding-replicas-read-same-volume-offload",
                         "aurora-auto-failover-to-replica", "aurora-cluster-endpoint-stays-same-after-failover"],
     "note": ("Size s. Participants: Application (users or instance icon), Writer (aurora-instance icon, label 'Writer'), Cluster volume (aurora "
              "icon, label 'Cluster volume, three AZs'), Aurora Replica (aurora-instance icon, label 'Aurora Replica'). Messages: 1 application "
              "to writer 'write'; 2 writer to volume 'six copies'; 3 application to replica 'read' (through the reader endpoint, aside "
              "allowed); 4 replica to volume, dashed, 'read same pages'; 5 an aside on the replica 'promoted if writer fails'. Labels at most 4 "
              "words, no digits. In the Markdown steps, step 1 links [connects to the current primary DB instance] "
              "(aurora-cluster-endpoint-connects-to-current-primary); step 2 links [synchronously replicates the data across Availability "
              "Zones] (aurora-synchronous-replication-to-six-storage-nodes) and [six storage nodes] (aurora-synchronous-replication-to-six-storage-nodes); "
              "step 3 has no hard claim (no link needed; 'spreads' is plain text) or links [connection-balancing support for read-only "
              "connections] (aurora-reader-endpoint-connection-balancing-read-only) if the step is reworded to hold it; step 4 links [connect to "
              "the same storage volume] (aurora-adding-replicas-read-same-volume-offload); step 5 links [automatically fails over to an Aurora "
              "Replica] (aurora-auto-failover-to-replica). If a step changes to fit its link, change say here and in the spec together (L703). "
              "The caption has no absolute word and no number with a unit ('six copies' is a number word), so it needs no link.")},
    {"id": "aurora-replica-compare", "kind": "compare",
     "placement": "2-deep.md#aurora-replicas-read-the-shared-volume-so-replica-lag-stays-low (after the table)",
     "title": "RDS read replica or Aurora Replica",
     "claim": "An RDS read replica keeps its own copy and receives each change later; an Aurora Replica reads the writer's own volume.",
     "alt": ("Two panels. RDS read replica: the application writes to the primary, which has its own storage; changes go asynchronously to a "
             "read replica with its own storage, and reports read the replica. Aurora: the application writes to the writer, the writer and two "
             "Aurora Replicas all connect to one shared cluster volume, and reports read the replicas through the reader endpoint."),
     "panels": [
         "RDS read replica: nodes 'Application', 'Primary', 'Primary storage', 'Read replica', 'Replica storage' (emph: own copy); edges application to primary 'writes', primary to read replica 'asynchronous copy' (dashed), primary to primary storage, read replica to replica storage",
         "Aurora: nodes 'Application', 'Writer', 'Aurora Replica', 'Aurora Replica', 'Cluster volume' (emph: shared); edges application to writer 'writes', writer to cluster volume, each Aurora Replica to cluster volume 'reads'",
     ],
     "say": [],
     "facts_for_caption": ["rds-read-replica-async-read-only", "aurora-adding-replicas-read-same-volume-offload", "aurora-cmp-replicas-share-storage-no-replica-writes"],
     "note": ("Size m, two panels, at most 6 nodes and 7 edges per panel; the application in the same cell in both panels. No numbers in labels. "
              "The caption holds no absolute word and no number, so it needs no link; keep the caption exactly as the claim.")},
    {"id": "aurora-before", "kind": "arch", "placement": "2-deep.md#decision-record (after Context)",
     "title": "Callvale before: RDS with one slow read replica",
     "claim": "The services write to an RDS primary with a standby, and dashboards read from one read replica that falls behind at peak.",
     "alt": ("Before: the Fargate services send writes to the RDS for PostgreSQL primary in AZ 1, which keeps a standby in AZ 2. Dashboard "
             "queries go to one read replica in AZ 3, which falls behind at peak."),
     "say": [
         "The Fargate services send writes and most queries to the RDS primary.",
         "The primary keeps a standby in a second Availability Zone.",
         "Dashboard queries go to the one read replica.",
         "At peak, the read replica falls behind, and dashboards show old data.",
     ],
     "facts_for_steps": [],
     "note": ("Story picture. Steps are story, not AWS rules: no fact link, no number, no absolute word. Two columns, zones named in labels "
              "(three zone boxes exceed the arch limits; elb-after does the same): A1 'Fargate services' (fargate icon), A2 'RDS primary' "
              "(db-instance icon, label names AZ 1), B2 'Standby' (db-instance-standby, AZ 2), B3 'Read replica' (db-instance, AZ 3, emph), "
              "A3 'Dashboards' or the services' read edge. Leave out RDS Proxy, ElastiCache and DynamoDB (not part of this decision). Keep spec say "
              "and Markdown steps equal (L703).")},
    {"id": "aurora-after", "kind": "arch", "placement": "2-deep.md#decision-record (after Decision)",
     "title": "Callvale after: an Aurora cluster with two Aurora Replicas",
     "claim": "The services write through the cluster endpoint and read through the reader endpoint of one Aurora cluster that shares one volume.",
     "alt": ("After: the Fargate services send writes to the cluster endpoint and dashboard queries to the reader endpoint. The Aurora writer "
             "is in AZ 1 and two Aurora Replicas are in AZ 2 and AZ 3; all three use one cluster volume. Dev and staging use Aurora Serverless v2."),
     "say": [
         "The services send writes to the cluster endpoint, which connects to the current primary DB instance.",
         "Dashboard queries use the reader endpoint, which balances connections to available Aurora Replicas.",
         "The writer and both replicas connect to the same storage volume, which keeps six copies of the data.",
         "If the writer fails, Aurora automatically fails over to an Aurora Replica.",
     ],
     "facts_for_steps": ["aurora-cluster-endpoint-connects-to-current-primary", "aurora-reader-endpoint-balances-connections-not-queries",
                         "aurora-adding-replicas-read-same-volume-offload", "aurora-storage-six-copies-three-azs", "aurora-auto-failover-to-replica"],
     "note": ("At most 12 nodes. Same cells as aurora-before: A1 'Fargate services'; A2 'Aurora writer' (aurora-instance icon, AZ 1) replaces the "
              "RDS primary; B2 'Aurora Replica' (AZ 2); B3 'Aurora Replica' (AZ 3); A3 or B4 'Cluster volume' (aurora icon, emph) with an edge "
              "from each instance; optional small node 'Dev and staging: Aurora Serverless v2' (aurora-serverless icon) in a free cell with no "
              "edge, only if the layout lint allows a node without edges. Step 1 links [connects to the current primary DB instance] "
              "(aurora-cluster-endpoint-connects-to-current-primary); step 2 links [balances connections to available Aurora Replicas] "
              "(aurora-reader-endpoint-balances-connections-not-queries); step 3 links [connect to the same storage volume] "
              "(aurora-adding-replicas-read-same-volume-offload) and [six copies] (aurora-storage-six-copies-three-azs); step 4 links "
              "[automatically fails over to an Aurora Replica] (aurora-auto-failover-to-replica). AZ 1 to AZ 3 are labels, not numbers. No "
              "second Region (stage 4). Keep spec say and Markdown steps equal (L703).")},
]

BRIEF["fact_requests"] = [
    {"id": "fr-0092", "service": "aurora", "where": "1-fast.md#changed-recently",
     "question": ("Set changed.date 2026-02-18 and a changed.was on aurora-change-default-encryption-new-clusters (new Aurora DB clusters are "
                  "encrypted by default with an AWS owned key since February 18, 2026; before, a new cluster was unencrypted unless you chose "
                  "encryption), from a saved AWS page that states the old behaviour or the date of the change; close as unfillable if no saved "
                  "page states it."),
     "effect": ("without it, the default-encryption entry of Changed recently is not written (changed_recently.pending), and the change "
                "appears only as the body_extras sentence of subsection 14. Filed 2026-10-14 by brief-27.")},
]

BRIEF["notes_for_orchestrator"] = [
    "Only verified facts are named: chapter-27 aurora- and aurora-serverless- facts from _build/work/27-aurora/fact-cards.md (823 verified, 2026-10-13), plus verified facts of chapters 18 (lambda-), 26 (rds-, rds-proxy-) and 28 (dynamodb-) from _build/work/27-aurora/nb-cards.md. build_brief.py checked every fact id and every display-and-id pair against data/facts/*.jsonl before stage end; the generator and its six data parts stay in _build/work/27-aurora/ (brief_part_a.py to brief_part_f.py) for later edits of the brief.",
    "File budget: How it works = 14 subsections at 195 to 225 words all-in (sum 3,010 by words_all_in) + 5 Go deeper blocks of at most 70 words + the intro line: about 3,385 of the 3,500 cap. 2-deep.md: about 3,385 + Numbers 290 + Decision record 270 + FAQ 430 = about 4,375 of the 4,500 cap; the real-world box (DraftKings, at most 100 words) fits only if the file stays at or under 4,390 words without it, which needs a few cuts. If How it works runs over, cut body_extras first, then the Go deeper of subsection 2.",
    "Traps: 13 (the U5 cap): 5 in the fast list, 8 as Exam trap callouts in 2-deep.md. 2-deep.md callouts: 8 Exam trap + 2 Try it + 1 Startup example = 11 of 12. Subsections without an Exam trap: 1, 3, 4, 6, 13, 14 (6 and 13 carry the two Spot the bug prompts). 16 of 22 slots are built on a trap; serverless-pauses-whenever-idle is carried by prose, Check 3 and a card, not by a slot (its option would rest on a volatile change).",
    "Twin pairs: three strict pairs (q01/q07 endpoints, q04/q10 capacity model, q12/q16 failover or switchover), so that the chapter still ships two whole pairs after one rejection. Each pair has identical options and qualifiers and turns on a stable fact.",
    "Changed recently: three examinable fast entries with changed records (2023-08-21 switchover rename, 2024-11-20 scale to zero, 2025-05-21 ten secondary Regions) and one alternate (2025-07-03, 256 TiB). The 2026-02-18 default encryption waits for fr-0092 (filed by brief-27; open requests block the counts gate, B09, until closed as filled or unfillable). The two not-examinable changes (2026-09-03 delayed replication, 2026-09-30 instant scaling) have no changed record, so no B-list entry is planned.",
    "Naming: 'Aurora Serverless v2' in the book (exam and story name); the user guide writes 'Aurora serverless'. 'switchover' is one word; the fail-over term bans 'switch over'. See naming.",
    "Volatile facts: about 75 chapter-27 facts are volatile (frequently-changing or changed within 24 months), including every 256 TiB, 256 ACU, scale-to-zero, ten-Region, Database Savings Plans, Free Tier, express configuration and write-forwarding version fact. The full list is in question_plan.volatile_facts_never_in_explanation_or_correct_why (Q112). Prose and cards may link them where a plan names them; every key rests on the stable key_facts of its slot.",
    "Demand gaps kept out of the prose (brief.v0 partial items): no saved page states a three-times PostgreSQL throughput or keeps the decision guide's five-times claim verified (d27-002): no throughput sentence; the engine versions with 256 TiB are bullet lines only (d27-008): 'varies by engine version'; 'eventually consistent' is not stated for Aurora Replicas (d27-024): the book says 'low, not zero'; Backtrack with Global Database and Activity Streams with Serverless are bullet lines only (d27-054, d27-069, d27-084): no sentence; no Route 53 or AWS Backup sentence for Global Database (d27-056); no RPO and RTO table per DR strategy (d27-059: chapter 40 owns it); no single v1-versus-v2 HA sentence (d27-082); no Limitless GA date (d27-108); no downtime figure for the Aurora read replica cutover (d27-115): no downtime number in subsection 13 or q18; the stale-read downside of a cache is not an AWS sentence (d27-140): the decision record states it as a design reason without an AWS claim.",
    "Source disagreements kept out of one sentence: failover with replicas 'less than 60 seconds, often less than 30' (guide) against 'within 30 seconds' (FAQ); Global Database promotion 'less than 1 minute' (product page, FAQ) against 'within a few minutes' and RTO 'in the order of minutes' (guide); custom endpoints per cluster 'up to five, not adjustable' (guide) against '5, adjustable' (quotas page): no number written; replica lag 'much less than 100 milliseconds' (guide), 'tens of milliseconds' (FAQ), 'often single-digit milliseconds' (features page): one figure per sentence.",
    "Displays to avoid in links (F2): displays that say 'we' for AWS (aurora-frequent-connections-use-rds-proxy 'we recommend that you use Amazon RDS Proxy', aurora-faq-cross-region-recommend-global-db, aurora-resources-not-auto-replicated-across-regions 'we don't automatically replicate...'); use the other display of each fact. Displays with backticks (aurora-postgres-rds-force-ssl-parameter, aurora-mysql-require-secure-transport-parameter, aurora-snapshot-cluster-must-be-available) and with quotes (aurora-serverless-choose-variable-spiky-workloads: variable or \"spiky\" workloads) are copied exactly.",
    "STARTUP check: the decision record keeps the three options, the qualifier 'most scalable', the choice (one writer and two Aurora Replicas in three Availability Zones) and the trade-off of data/startup.json word for word; dev and staging on Aurora Serverless v2 come from the JSON note. uses_numbers: database_size_gb (1.2 TB; 400 GB at stage 2), database_read_percent (90), replica_behind_seconds (40), aurora_replicas (2), dev_staging_hours_per_week (50). W903 may warn on '1.2' because the JSON stores 1200: report it, do not change the story. The before and after diagrams use two columns with zones in labels, like elb-after.",
    "Term requests: the Aurora terms in term_requests are not in data/terms.json; writers use needs-term markers until they are added. The terms list names only bank terms (B11).",
    "Spoken numbers: speak items write numbers as words from the fact cards' say forms (well under a hundred milliseconds; fifteen Aurora Replicas besides the primary; under a minute; typically under one second; a quarter or more; once every thirty days; about two gibibytes of memory).",
    "Tasks: all three cost $0 (a DB cluster parameter group has no charge; no DB cluster or instance is created), because the chapter has no verified price fact. aurora-t02 depends on rds.global_db_rpo being modifiable in a custom cluster parameter group of the default aurora-postgresql family; the task writer confirms it with tasks check-cli --reference and reports the task for a re-plan if the reference says otherwise.",
]
