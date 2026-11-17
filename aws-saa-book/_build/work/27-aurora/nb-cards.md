facts card: 50 facts
rds-decision-guide-aurora-row
  claim: The decision guide recommends Amazon Aurora when you migrate or modernize an on-premises relational workload or when the workload has less predictable query patterns; it supports MySQL- and PostgreSQL-compatible engines.
  scope: AWS database decision guide (Choosing an AWS database service).
  link: [less predictable query patterns](../facts/rds.md#rds-decision-guide-aurora-row)
rds-decision-guide-rds-row
  claim: The AWS database decision guide says to use Amazon RDS when you need a fully managed relational database with a choice of six engines (PostgreSQL, MySQL, MariaDB, SQL Server, Oracle and Db2); it is optimized for structured data with full SQL support, automated backups, software patching and Multi-AZ deployments.
  scope: AWS database decision guide (Choosing an AWS database service).
  link: [fully managed relational database](../facts/rds.md#rds-decision-guide-rds-row)
  link: [six popular engines](../facts/rds.md#rds-decision-guide-rds-row)
  say: six popular engines
rds-decision-guide-dynamodb-row
  claim: The decision guide places Amazon DynamoDB as a key-value database for workloads such as session stores or shopping carts, optimized as a serverless NoSQL database with single-digit millisecond performance at any scale.
  scope: AWS database decision guide (Choosing an AWS database service).
  link: [session stores or shopping carts](../facts/rds.md#rds-decision-guide-dynamodb-row)
  link: [single-digit millisecond performance at any scale](../facts/rds.md#rds-decision-guide-dynamodb-row)
rds-decision-guide-relational-joins
  claim: Relational databases store structured data in tables, rows and columns and support complex queries through joins.
  scope: AWS database decision guide (Choosing an AWS database service).
  link: [complex queries through joins](../facts/rds.md#rds-decision-guide-relational-joins)
rds-decision-guide-cache-microseconds
  claim: For extremely high read performance with microsecond response times, the decision guide suggests in-memory caching such as Amazon ElastiCache alongside the database, or a durable in-memory database such as Amazon MemoryDB.
  scope: AWS database decision guide (Choosing an AWS database service).
  link: [measured in microseconds](../facts/rds.md#rds-decision-guide-cache-microseconds)
rds-multi-az-one-vs-two-standbys
  claim: A Multi-AZ DB instance deployment has one standby that provides failover support but serves no read traffic; a Multi-AZ DB cluster deployment has two standbys that provide failover support and can also serve read traffic.
  scope: Multi-AZ DB instance and Multi-AZ DB cluster deployments.
  link: [one standby or two standby DB instances](../facts/rds.md#rds-multi-az-one-vs-two-standbys)
  link: [can also serve read traffic](../facts/rds.md#rds-multi-az-one-vs-two-standbys)
  link: [doesn't serve read traffic](../facts/rds.md#rds-multi-az-one-vs-two-standbys)
rds-multi-az-instance-standby-no-reads
  claim: In a Multi-AZ DB instance deployment, RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone, and the standby does not serve read traffic.
  scope: Multi-AZ DB instance deployment.
  link: [synchronous standby replica in a different Availability Zone](../facts/rds.md#rds-multi-az-instance-standby-no-reads)
  link: [doesn't serve read traffic](../facts/rds.md#rds-multi-az-instance-standby-no-reads)
rds-read-replica-async-read-only
  claim: Amazon RDS copies updates from the primary DB instance to a read replica asynchronously; clients have read/write access to the primary and read-only access to the replica.
  scope: RDS DB instance read replicas.
  link: [read-only access to the replica](../facts/rds.md#rds-read-replica-async-read-only)
  link: [copies them asynchronously to the read replica](../facts/rds.md#rds-read-replica-async-read-only)
rds-change-read-replicas-15-2022-10
  claim: On October 20, 2022 Amazon RDS for MariaDB, MySQL and PostgreSQL DB instances gained support for up to 15 read replicas.
  scope: RDS DB instance read replicas.
  link: [October 20, 2022](../facts/rds.md#rds-change-read-replicas-15-2022-10)
  link: [up to 15 read replicas](../facts/rds.md#rds-change-read-replicas-15-2022-10)
  say: October twentieth, twenty twenty-two | up to fifteen read replicas
rds-compare-failover-vs-promote
  claim: A non-Aurora Multi-AZ deployment fails over automatically to the standby when a problem is detected, while a non-Aurora read replica can be manually promoted to a standalone database instance.
  scope: non-Aurora RDS: Multi-AZ deployments, multi-Region deployments and read replicas.
  link: [Automatic failover to standby](../facts/rds.md#rds-compare-failover-vs-promote)
  link: [Can be manually promoted](../facts/rds.md#rds-compare-failover-vs-promote)
rds-multi-az-instance-failover-time
  claim: Failover of a Multi-AZ DB instance typically takes 60–120 seconds; large transactions or a lengthy recovery process can increase failover time.
  scope: per Multi-AZ DB instance deployment; fixed; not adjustable; typical value; large transactions or lengthy recovery can make it longer.
  link: [60–120 seconds](../facts/rds.md#rds-multi-az-instance-failover-time)
  say: sixty to one hundred twenty seconds
rds-multi-az-cluster-not-aurora
  claim: RDS Multi-AZ DB clusters are not the same as Aurora DB clusters.
  scope: Multi-AZ DB cluster deployments.
  link: [aren't the same as Aurora DB clusters](../facts/rds.md#rds-multi-az-cluster-not-aurora)
rds-multi-az-cluster-failover-time
  claim: Failover of a Multi-AZ DB cluster typically takes under 35 seconds and completes when both reader DB instances have applied the outstanding transactions from the failed writer.
  scope: per Multi-AZ DB cluster; fixed; not adjustable; typical value; depends on database activity.
  link: [under 35 seconds](../facts/rds.md#rds-multi-az-cluster-failover-time)
  say: under thirty-five seconds
rds-multi-az-cluster-three-azs-all-read
  claim: A Multi-AZ DB cluster deployment has a writer DB instance and two reader DB instances in three separate Availability Zones of one Region, and all three can serve read traffic.
  scope: Multi-AZ DB cluster deployment, one Region.
  link: [three separate Availability Zones](../facts/rds.md#rds-multi-az-cluster-three-azs-all-read)
  link: [All three DB instances can serve read traffic](../facts/rds.md#rds-multi-az-cluster-three-azs-all-read)
  link: [two reader DB instances](../facts/rds.md#rds-multi-az-cluster-three-azs-all-read)
rds-read-replica-promote-reboot-minutes
  claim: When you promote a read replica, RDS stops replication and reboots the replica before making it available; the promotion can take several minutes or longer depending on the replica's size.
  scope: RDS DB instance read replicas.
  link: [RDS stops replication and reboots the read replica](../facts/rds.md#rds-read-replica-promote-reboot-minutes)
  link: [several minutes or longer](../facts/rds.md#rds-read-replica-promote-reboot-minutes)
rds-cross-region-replica-use-cases
  claim: A read replica in a different AWS Region is used to improve disaster recovery, to scale reads into a Region closer to users, and to make migration between Regions easier.
  scope: cross-Region read replicas.
  link: [Improve your disaster recovery capabilities.](../facts/rds.md#rds-cross-region-replica-use-cases)
  link: [closer to your users](../facts/rds.md#rds-cross-region-replica-use-cases)
  link: [easier to migrate](../facts/rds.md#rds-cross-region-replica-use-cases)
rds-multi-region-async-replica-survives-region
  claim: You can create RDS DB instances in multiple Regions; an instance that replicates asynchronously to a DB instance in another Region keeps a copy available if one Region becomes unavailable.
  scope: cross-Region read replicas.
  link: [replicates asynchronously to a standby DB instance](../facts/rds.md#rds-multi-region-async-replica-survives-region)
  link: [If one Region becomes unavailable](../facts/rds.md#rds-multi-region-async-replica-survives-region)
rds-faq-read-replica-cross-region-lag
  claim: For a cross-Region read replica, the delay before written data is available on the replica depends on the network latency between the two Regions.
  scope: cross-Region read replicas.
  link: [network latency between the two regions](../facts/rds.md#rds-faq-read-replica-cross-region-lag)
rds-cross-region-replica-higher-lag
  claim: A read replica in a different Region than its source can be expected to have more replication lag, because of the longer network channels between Regional data centers.
  scope: cross-Region read replicas.
  link: [higher level of lag time](../facts/rds.md#rds-cross-region-replica-higher-lag)
  link: [longer network channels between regional data centers](../facts/rds.md#rds-cross-region-replica-higher-lag)
rds-storage-ebs-striping
  claim: Amazon RDS stores database and logs on EBS volumes and, depending on the storage size, stripes across multiple EBS volumes to improve IOPS performance.
  scope: RDS DB instance storage and performance.
  link: [Amazon RDS uses EBS volumes](../facts/rds.md#rds-storage-ebs-striping)
  link: [stripes across multiple EBS volumes](../facts/rds.md#rds-storage-ebs-striping)
rds-engines-supported
  claim: Amazon RDS (not counting Aurora) offers these database engines: IBM Db2, MariaDB, Microsoft SQL Server, MySQL, Oracle Database, and PostgreSQL.
  scope: Amazon RDS user guide (engines other than Aurora).
  link: [IBM Db2, MariaDB, Microsoft SQL Server](../facts/rds.md#rds-engines-supported)
  link: [MySQL, Oracle Database, and PostgreSQL](../facts/rds.md#rds-engines-supported)
  link: [engines that you are already familiar with](../facts/rds.md#rds-engines-supported)
rds-pricing-dimension-io-requests-magnetic-aurora
  claim: Storage I/O requests per month are a billing dimension only for Amazon RDS magnetic storage and Amazon Aurora.
  scope: Amazon RDS billing.
  link: [magnetic storage and Amazon Aurora only](../facts/rds.md#rds-pricing-dimension-io-requests-magnetic-aurora)
rds-faq-read-replica-asynchronous
  claim: Read replicas of RDS for MySQL, MariaDB, PostgreSQL, Oracle and SQL Server use the engines' native asynchronous replication, not synchronous replication.
  scope: read replicas of RDS for MySQL, MariaDB, PostgreSQL, Oracle and SQL Server.
  link: [native asynchronous replication](../facts/rds.md#rds-faq-read-replica-asynchronous)
rds-faq-read-replica-own-endpoint
  claim: You connect to a read replica like a standard DB instance, using its own endpoint; with several read replicas, your application decides how to spread the read traffic.
  scope: RDS DB instance read replicas.
  link: [it is up to your application](../facts/rds.md#rds-faq-read-replica-own-endpoint)
  link: [retrieve the endpoint(s) for your read replica(s)](../facts/rds.md#rds-faq-read-replica-own-endpoint)
rds-replica-size-as-much-as-source
  claim: For effective replication AWS recommends read replicas with as much or more compute and storage as their source; otherwise replication lag likely increases or the replica can run out of space.
  scope: RDS DB instance read replicas.
  link: [as much or more compute and storage resources](../facts/rds.md#rds-replica-size-as-much-as-source)
  link: [replication lag is likely to increase](../facts/rds.md#rds-replica-size-as-much-as-source)
rds-snapshots-incremental
  claim: The first snapshot of a DB instance holds the full database; later snapshots of the same database are incremental and save only the data changed since the most recent snapshot.
  scope: DB snapshots.
  link: [Subsequent snapshots of the same database are incremental](../facts/rds.md#rds-snapshots-incremental)
rds-compare-replication-sync-async
  claim: Multi-AZ deployments use synchronous replication; multi-Region deployments and read replicas use asynchronous replication.
  scope: non-Aurora RDS: Multi-AZ deployments, multi-Region deployments and read replicas.
  link: [synchronous replication](../facts/rds.md#rds-compare-replication-sync-async)
  link: [Asynchronous replication](../facts/rds.md#rds-compare-replication-sync-async)
rds-replica-lag-cause-write-load
  claim: In a Multi-AZ DB cluster, replica lag generally occurs when the write workload is too high for the reader DB instances to apply the transactions efficiently.
  scope: RDS Multi-AZ DB clusters (writer and reader DB instances).
  link: [write workload is too high](../facts/rds.md#rds-replica-lag-cause-write-load)
rds-read-replica-definition
  claim: A read replica is a read-only copy of a DB instance; routing queries to it reduces the load on the primary and lets read-heavy workloads scale out beyond one DB instance.
  scope: RDS DB instance read replicas.
  link: [read-only copy of a DB instance](../facts/rds.md#rds-read-replica-definition)
  link: [read-heavy database workloads](../facts/rds.md#rds-read-replica-definition)
rds-faq-multiaz-replication-synchronous
  claim: Multi-AZ replication is synchronous: all database writes are concurrent on the primary and standby, which protects the latest database updates because they should be available on the standby if failover is required.
  scope: Multi-AZ DB instance deployments.
  link: [concurrent on the primary and standby](../facts/rds.md#rds-faq-multiaz-replication-synchronous)
dynamodb-vs-aurora-global-database-single-writer
  claim: An Aurora global database has one primary Region where data is written and up to 10 read-only secondary Regions; only the primary cluster performs writes. DynamoDB global tables are multi-active: every replica accepts reads and writes.
  scope: Aurora Global Database versus DynamoDB global tables; Aurora write forwarding lets secondary clusters send writes to the primary.
  link: [one primary AWS Region](../facts/dynamodb.md#dynamodb-vs-aurora-global-database-single-writer)
  link: [up to 10 read-only secondary AWS Regions](../facts/dynamodb.md#dynamodb-vs-aurora-global-database-single-writer)
  link: [Only the primary cluster performs write operations](../facts/dynamodb.md#dynamodb-vs-aurora-global-database-single-writer)
  say: one writable primary Region | up to ten read-only secondary Regions | only the primary cluster writes
dynamodb-global-table-any-replica-serves-reads-writes
  claim: Any global table replica can serve reads and writes.
  scope: per global table.
  link: [Any global table replica](../facts/dynamodb.md#dynamodb-global-table-any-replica-serves-reads-writes)
  link: [serve reads and writes](../facts/dynamodb.md#dynamodb-global-table-any-replica-serves-reads-writes)
dynamodb-faq-global-tables-multi-active
  claim: DynamoDB global tables is a fully managed, serverless, multi-Region, and multi-active database.
  scope: DynamoDB global tables.
  link: [multi-Region, and multi-active database](../facts/dynamodb.md#dynamodb-faq-global-tables-multi-active)
dynamodb-gt-multi-active-no-failover-needed
  claim: DynamoDB global tables are a fully managed, serverless, multi-Region and multi-active database: if processing is interrupted in one Region, there is no need for a database failover because applications can read and write to any replica table.
  scope: DynamoDB global tables.
  link: [multi-Region, and multi-active](../facts/dynamodb.md#dynamodb-gt-multi-active-no-failover-needed)
  link: [there is no need for a database failover](../facts/dynamodb.md#dynamodb-gt-multi-active-no-failover-needed)
  say: multi-Region and multi-active | no database failover is needed
dynamodb-decision-guide-aurora-relational-joins
  claim: The AWS database decision guide describes Amazon Aurora as a relational database for migrating or modernizing an on-premises relational workload, or when query patterns are less predictable, and says relational databases support complex queries through joins.
  scope: AWS database decision guide, Choose section.
  link: [less predictable query patterns](../facts/dynamodb.md#dynamodb-decision-guide-aurora-relational-joins)
  link: [complex queries through joins](../facts/dynamodb.md#dynamodb-decision-guide-aurora-relational-joins)
  say: less predictable query patterns | complex queries through joins
dynamodb-decision-guide-key-value-session-store
  claim: The AWS database decision guide lists DynamoDB as a key-value database for workloads such as session stores or shopping carts, optimized to be a serverless, NoSQL, fully managed database with single-digit millisecond performance at any scale.
  scope: AWS database decision guide, Choose section.
  link: [session stores or shopping carts](../facts/dynamodb.md#dynamodb-decision-guide-key-value-session-store)
  link: [single-digit millisecond performance at any scale](../facts/dynamodb.md#dynamodb-decision-guide-key-value-session-store)
  link: [Key-value](../facts/dynamodb.md#dynamodb-decision-guide-key-value-session-store)
  say: session stores and shopping carts | single-digit millisecond performance at any scale | key-value
dynamodb-decision-guide-elasticache-caching-layer
  claim: The AWS database decision guide describes Amazon ElastiCache as an in-memory service for a caching layer that improves read performance, optimized for microsecond reads and sub-millisecond writes as an ephemeral cache for frequently accessed data.
  scope: AWS database decision guide, Choose section.
  link: [caching layer to improve read performance](../facts/dynamodb.md#dynamodb-decision-guide-elasticache-caching-layer)
  link: [ephemeral cache for frequently accessed data](../facts/dynamodb.md#dynamodb-decision-guide-elasticache-caching-layer)
  say: a caching layer to improve read performance | an ephemeral cache for frequently accessed data
dynamodb-decision-guide-rds-full-sql
  claim: The AWS database decision guide describes Amazon RDS as a fully managed relational database with a choice of six engines, optimized for structured data with full SQL support, automated backups, software patching and Multi-AZ deployments.
  scope: AWS database decision guide, Choose section.
  link: [full SQL support](../facts/dynamodb.md#dynamodb-decision-guide-rds-full-sql)
  link: [PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, and Db2](../facts/dynamodb.md#dynamodb-decision-guide-rds-full-sql)
  say: full SQL support | PostgreSQL, MySQL, MariaDB, SQL Server, Oracle and Db2
dynamodb-no-joins-heart-of-nosql-modeling
  claim: Eliminating the need for JOINs is at the heart of NoSQL data modeling; AWS says this is why DynamoDB can deliver consistent performance at any scale, while RDBMS performance is not constant at scale because of the runtime complexity of SQL queries and JOINs.
  scope: DynamoDB versus relational design.
  link: [at the heart of NoSQL data modeling](../facts/dynamodb.md#dynamodb-no-joins-heart-of-nosql-modeling)
  say: no joins is at the heart of NoSQL modeling
dynamodb-dg-oltp-relational-vs-non-relational
  claim: The decision guide focuses on databases for online transaction processing (OLTP) and says there are two high-level categories: relational and non-relational. Non-relational options cover key-value, document, caching, in-memory, graph, time series and wide-column data models.
  scope: AWS database decision guide.
  link: [relational and non-relational](../facts/dynamodb.md#dynamodb-dg-oltp-relational-vs-non-relational)
  link: [key-value, document, caching, in-memory, graph](../facts/dynamodb.md#dynamodb-dg-oltp-relational-vs-non-relational)
  say: relational and non-relational | key-value, document, in-memory, graph, time series and wide-column
dynamodb-wa-oltp-dynamodb-vs-rds-joins
  claim: For high-throughput read as-is transactional processing the performance pillar suggests a NoSQL database such as DynamoDB. For high-throughput and complex read patterns such as joins with consistency, it says to use Amazon RDS.
  scope: Well-Architected PERF03-BP01.
  link: [consider a NoSQL database such as DynamoDB](../facts/dynamodb.md#dynamodb-wa-oltp-dynamodb-vs-rds-joins)
  link: [complex read patterns (like join)](../facts/dynamodb.md#dynamodb-wa-oltp-dynamodb-vs-rds-joins)
  say: a NoSQL database such as DynamoDB | Amazon RDS for join-heavy reads
dynamodb-faq-global-tables-zero-rpo-mrsc
  claim: With multi-Region strong consistency, applications can be built with zero RPO and the highest levels of resiliency.
  scope: DynamoDB global tables with multi-Region strong consistency; multi-Region strong consistency is used.
  link: [zero RPO](../facts/dynamodb.md#dynamodb-faq-global-tables-zero-rpo-mrsc)
  say: zero RPO
dynamodb-transaction-not-across-gt-regions
  claim: Transactions are not supported across Regions in global tables; ACID guarantees apply only within the Region where the write is made originally.
  scope: global tables; ACID guarantees only within the Region where the write is made originally.
  link: [not supported across Regions](../facts/dynamodb.md#dynamodb-transaction-not-across-gt-regions)
rds-proxy-failover-66-percent
  claim: RDS Proxy bypasses DNS caches to reduce failover times by up to 66% for Amazon RDS Multi-AZ DB instances, and routes traffic to the new database instance while preserving application connections.
  scope: Amazon RDS Multi-AZ DB instances; maximum.
  link: [up to 66%](../facts/rds-proxy.md#rds-proxy-failover-66-percent)
  say: up to sixty-six percent
rds-proxy-failover-same-ip-no-dns
  claim: During failovers RDS Proxy keeps accepting connections at the same IP address and directs them to the new primary, so clients are not affected by DNS propagation delays on failover.
  scope: RDS DB instances in a Multi-AZ configuration.
  link: [at the same IP address](../facts/rds-proxy.md#rds-proxy-failover-same-ip-no-dns)
  link: [directs connections to the new primary](../facts/rds-proxy.md#rds-proxy-failover-same-ip-no-dns)
rds-proxy-definition-pool-share
  claim: Amazon RDS Proxy lets applications pool and share database connections to improve their ability to scale, and makes them more resilient to database failures by connecting to a standby while preserving application connections.
  scope: Amazon RDS Proxy.
  link: [pool and share database connections](../facts/rds-proxy.md#rds-proxy-definition-pool-share)
  link: [preserving application connections](../facts/rds-proxy.md#rds-proxy-definition-pool-share)
rds-proxy-lambda-connection-pooling
  claim: AWS Lambda functions are good candidates for RDS Proxy because they make frequent short database connections that benefit from its connection pooling, and they can use IAM authentication instead of database credentials in the function code.
  scope: Amazon RDS Proxy.
  link: [connection pooling offered by RDS Proxy](../facts/rds-proxy.md#rds-proxy-lambda-connection-pooling)
  link: [frequent short database connections](../facts/rds-proxy.md#rds-proxy-lambda-connection-pooling)
rds-proxy-read-only-endpoint-clusters
  claim: By default, the RDS Proxy endpoint for a Multi-AZ DB cluster has read/write capability and sends all requests to the writer instance of the cluster; if the proxy is associated with a Multi-AZ DB cluster, you can create additional read/write or read-only endpoints for that proxy.
  scope: RDS Proxy with Multi-AZ DB clusters; the proxy is associated with a Multi-AZ DB cluster.
  link: [additional read/write or read-only endpoints](../facts/rds-proxy.md#rds-proxy-read-only-endpoint-clusters)
  link: [sends all requests to the writer instance](../facts/rds-proxy.md#rds-proxy-read-only-endpoint-clusters)
lambda-vpc-db-connections-rds-proxy
  claim: Because Lambda scales by creating many concurrent execution environments that each keep their own database connection, high concurrency can exhaust database connection limits; for relational databases the guide says to use Amazon RDS Proxy to pool and manage connections.
  scope: Lambda functions that access a relational database.
  link: [exhaust database connection limits](../facts/lambda.md#lambda-vpc-db-connections-rds-proxy)
  link: [to pool and manage connections](../facts/lambda.md#lambda-vpc-db-connections-rds-proxy)
lambda-rds-proxy-recommended-production
  claim: Lambda can connect to Amazon RDS directly or through RDS Proxy; direct connections suit simple scenarios and proxies are recommended for production, because a proxy manages a pool of shared connections so the function can reach high concurrency without exhausting database connections.
  scope: Lambda with Amazon RDS.
  link: [proxies are recommended for production](../facts/lambda.md#lambda-rds-proxy-recommended-production)
