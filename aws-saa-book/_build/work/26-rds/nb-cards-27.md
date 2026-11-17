facts card: 823 facts
aurora-add-instance-no-data-copy
  claim: You can add a DB instance to an Aurora cluster quickly because Aurora does not make a new copy of the table data; the new instance connects to the shared volume that already contains the data.
  scope: Aurora cluster volume (shared storage).
  link: [add a DB instance quickly](../facts/aurora.md#aurora-add-instance-no-data-copy)
  link: [doesn't make a new copy](../facts/aurora.md#aurora-add-instance-no-data-copy)
aurora-add-replicas-console-cli-api
  claim: You can add Aurora Replicas to a DB cluster using the AWS Management Console, the AWS CLI, or the RDS API.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [the AWS CLI, or the RDS API](../facts/aurora.md#aurora-add-replicas-console-cli-api)
  link: [add Aurora Replicas to a DB cluster](../facts/aurora.md#aurora-add-replicas-console-cli-api)
aurora-adding-replicas-read-same-volume-offload
  claim: Aurora Replicas connect to the same storage volume as the primary DB instance, but support read operations only, and you use them to offload read workloads from the primary DB instance.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [connect to the same storage volume](../facts/aurora.md#aurora-adding-replicas-read-same-volume-offload)
  link: [support read operations only](../facts/aurora.md#aurora-adding-replicas-read-same-volume-offload)
aurora-all-instances-see-single-logical-volume
  claim: The primary instance and the Aurora Replicas in an Aurora DB cluster all see the data in the cluster volume as a single logical volume.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [see the data in the cluster volume](../facts/aurora.md#aurora-all-instances-see-single-logical-volume)
  link: [single logical volume](../facts/aurora.md#aurora-all-instances-see-single-logical-volume)
aurora-auto-failover-to-replica
  claim: Aurora automatically fails over to an Aurora Replica if the primary DB instance becomes unavailable.
  scope: Aurora DB cluster failover within one Region.
  link: [automatically fails over to an Aurora Replica](../facts/aurora.md#aurora-auto-failover-to-replica)
  link: [primary DB instance becomes unavailable](../facts/aurora.md#aurora-auto-failover-to-replica)
aurora-auto-repair-avoids-pitr
  claim: Because of storage auto-repair, Aurora avoids data loss and reduces the need to perform a point-in-time restore to recover from a disk failure.
  scope: Aurora cluster volume (shared storage).
  link: [avoids data loss](../facts/aurora.md#aurora-auto-repair-avoids-pitr)
  link: [reduces the need to perform a point-in-time restore](../facts/aurora.md#aurora-auto-repair-avoids-pitr)
aurora-auto-scaling-both-engines-removes-unused
  claim: Aurora Auto Scaling is available for both Aurora MySQL and Aurora PostgreSQL.
  scope: Aurora Auto Scaling for Aurora Replicas.
  link: [available for both Aurora MySQL and Aurora PostgreSQL](../facts/aurora.md#aurora-auto-scaling-both-engines-removes-unused)
  link: [Aurora Auto Scaling is available](../facts/aurora.md#aurora-auto-scaling-both-engines-removes-unused)
aurora-auto-scaling-cooldown-default
  claim: If you do not set the scale-in or scale-out cooldown period, the default for each is 300 seconds.
  scope: per scaling policy, scale-in and scale-out cooldown each; default; adjustable.
  link: [default for each is 300 seconds](../facts/aurora.md#aurora-auto-scaling-cooldown-default)
  link: [300 seconds](../facts/aurora.md#aurora-auto-scaling-cooldown-default)
aurora-auto-scaling-needs-writer-first
  claim: Before you can use Aurora Auto Scaling with an Aurora DB cluster, you must first create an Aurora DB cluster with a primary (writer) DB instance.
  scope: Aurora Auto Scaling for Aurora Replicas.
  link: [a primary (writer) DB instance](../facts/aurora.md#aurora-auto-scaling-needs-writer-first)
  link: [Before you can use Aurora Auto Scaling](../facts/aurora.md#aurora-auto-scaling-needs-writer-first)
aurora-auto-scaling-new-replica-last-promotion-priority
  claim: The promotion tier for replicas added by Aurora Auto Scaling is set to the last priority, which is 15 by default, so a replica with a better priority is promoted first during a failover.
  scope: per Aurora Replica added by Aurora Auto Scaling; default; not adjustable.
  link: [last priority, which is 15 by default](../facts/aurora.md#aurora-auto-scaling-new-replica-last-promotion-priority)
  link: [promotion tier for new Aurora Replicas](../facts/aurora.md#aurora-auto-scaling-new-replica-last-promotion-priority)
aurora-auto-scaling-new-replica-same-class-as-primary
  claim: When Aurora Auto Scaling adds a new Aurora Replica, the new replica has the same DB instance class as the primary instance.
  scope: Aurora Auto Scaling for Aurora Replicas.
  link: [same DB instance class](../facts/aurora.md#aurora-auto-scaling-new-replica-same-class-as-primary)
  link: [adds a new Aurora Replica](../facts/aurora.md#aurora-auto-scaling-new-replica-same-class-as-primary)
aurora-auto-scaling-one-policy-per-target-metric
  claim: For each Aurora DB cluster, you can create only one Auto Scaling policy for each target metric.
  scope: per Aurora DB cluster, per target metric; maximum; not adjustable.
  link: [only one Auto Scaling policy](../facts/aurora.md#aurora-auto-scaling-one-policy-per-target-metric)
  link: [each target metric](../facts/aurora.md#aurora-auto-scaling-one-policy-per-target-metric)
aurora-auto-scaling-policy-min-max-replicas
  claim: The scaling policy defines the minimum and maximum number of Aurora Replicas that Aurora Auto Scaling can manage.
  scope: Aurora Auto Scaling for Aurora Replicas.
  link: [minimum and maximum number of Aurora Replicas](../facts/aurora.md#aurora-auto-scaling-policy-min-max-replicas)
  link: [scaling policy defines](../facts/aurora.md#aurora-auto-scaling-policy-min-max-replicas)
aurora-auto-scaling-scale-out-always-enabled
  claim: Scale-out activities are always enabled so that the scaling policy can create Aurora Replicas as needed, while scale-in activities can be enabled or disabled for a policy.
  scope: Aurora Auto Scaling for Aurora Replicas.
  link: [Scale-out activities are always enabled](../facts/aurora.md#aurora-auto-scaling-scale-out-always-enabled)
  link: [create Aurora Replicas as needed](../facts/aurora.md#aurora-auto-scaling-scale-out-always-enabled)
aurora-auto-scaling-target-tracking-cloudwatch
  claim: Aurora Auto Scaling target tracking creates and manages CloudWatch alarms that trigger the scaling policy and calculates the scaling adjustment from the metric and target value.
  scope: Aurora Auto Scaling for Aurora Replicas.
  link: [creates and manages CloudWatch alarms](../facts/aurora.md#aurora-auto-scaling-target-tracking-cloudwatch)
  link: [metric and target value](../facts/aurora.md#aurora-auto-scaling-target-tracking-cloudwatch)
aurora-auto-scaling-use-reader-endpoint
  claim: To benefit from Aurora Auto Scaling, applications must support connections to new Aurora Replicas, and AWS recommends using the Aurora reader endpoint to do so.
  scope: Aurora Auto Scaling for Aurora Replicas.
  link: [recommend using the Aurora reader endpoint](../facts/aurora.md#aurora-auto-scaling-use-reader-endpoint)
  link: [support connections to new Aurora Replicas](../facts/aurora.md#aurora-auto-scaling-use-reader-endpoint)
aurora-automated-backup-copy-to-keep-longer
  claim: To keep an automated backup for a longer period, copy it to create a manual snapshot, which is retained until you delete it.
  scope: Aurora automated backups.
  link: [copy it to create a manual snapshot](../facts/aurora.md#aurora-automated-backup-copy-to-keep-longer)
  link: [retained until you delete it](../facts/aurora.md#aurora-automated-backup-copy-to-keep-longer)
aurora-automated-backups-stored-in-s3
  claim: Aurora automated backups are stored in Amazon S3.
  scope: Aurora automated backups.
  link: [stored in Amazon S3](../facts/aurora.md#aurora-automated-backups-stored-in-s3)
  link: [Aurora automated backups](../facts/aurora.md#aurora-automated-backups-stored-in-s3)
aurora-autoscaling-global-secondary-unsupported
  claim: Aurora global databases currently do not support Aurora Auto Scaling for secondary DB clusters.
  scope: per Aurora global database secondary DB cluster.
  link: [don't support Aurora Auto Scaling](../facts/aurora.md#aurora-autoscaling-global-secondary-unsupported)
aurora-autoscaling-needs-all-instances-available
  claim: Aurora Auto Scaling only scales a DB cluster if all cluster instances are in the available state.
  scope: per Aurora DB cluster.
  link: [all cluster instances are in the available state](../facts/aurora.md#aurora-autoscaling-needs-all-instances-available)
aurora-autoscaling-predefined-metric-reader-connections
  claim: Aurora Auto Scaling supports the predefined metric RDSReaderAverageDatabaseConnections, the average DatabaseConnections across all Aurora Replicas in the Aurora DB cluster.
  scope: per Aurora DB cluster scaling policy.
  link: [RDSReaderAverageDatabaseConnections](../facts/aurora.md#aurora-autoscaling-predefined-metric-reader-connections)
aurora-autoscaling-predefined-metric-reader-cpu
  claim: Aurora Auto Scaling supports the predefined metric RDSReaderAverageCPUUtilization, the average CPUUtilization across all Aurora Replicas in the Aurora DB cluster.
  scope: per Aurora DB cluster scaling policy.
  link: [RDSReaderAverageCPUUtilization](../facts/aurora.md#aurora-autoscaling-predefined-metric-reader-cpu)
aurora-autoscaling-removes-only-own-replicas
  claim: Aurora Auto Scaling only removes Aurora Replicas that it created.
  scope: per Aurora DB cluster.
  link: [only removes Aurora Replicas that it created](../facts/aurora.md#aurora-autoscaling-removes-only-own-replicas)
aurora-autoscaling-replica-count-range
  claim: Aurora Auto Scaling maximum and minimum number of Aurora Replicas must each be set to 0 to 15, and the maximum must be equal to or greater than the minimum.
  scope: per Aurora DB cluster scaling policy; maximum; adjustable; the minimum has the same 0–15 range and must be equal to or less than the maximum.
  link: [0–15](../facts/aurora.md#aurora-autoscaling-replica-count-range)
  say: zero to fifteen
aurora-autoscaling-writer-not-scaled
  claim: Aurora Auto Scaling does not apply to the workload on the writer DB instance. It helps with the workload only on the reader instances.
  scope: per Aurora DB cluster.
  link: [only on the reader instances](../facts/aurora.md#aurora-autoscaling-writer-not-scaled)
aurora-aws-backup-manages-clusters
  claim: You can use AWS Backup to manage backups of Amazon Aurora DB clusters.
  scope: Aurora automated backups.
  link: [use AWS Backup to manage backups](../facts/aurora.md#aurora-aws-backup-manages-clusters)
  link: [Amazon Aurora DB clusters](../facts/aurora.md#aurora-aws-backup-manages-clusters)
aurora-az-chosen-automatically-if-not-specified
  claim: When you create a DB instance in your cluster without specifying an AZ, Aurora automatically chooses an appropriate AZ for that instance.
  scope: per DB instance created in an Aurora cluster; default; not adjustable.
  link: [automatically chooses an appropriate AZ](../facts/aurora.md#aurora-az-chosen-automatically-if-not-specified)
  link: [if you don't specify an AZ](../facts/aurora.md#aurora-az-chosen-automatically-if-not-specified)
aurora-az-outage-readers-in-other-azs-promoted
  claim: If an AZ outage makes the primary unavailable and a provisioned or Aurora serverless cluster has reader instances in other AZs, Aurora promotes one of those readers to be the new primary instance.
  scope: Aurora DB cluster failover within one Region.
  link: [reader instances in other AZs](../facts/aurora.md#aurora-az-outage-readers-in-other-azs-promoted)
  link: [promote one of those reader instances](../facts/aurora.md#aurora-az-outage-readers-in-other-azs-promoted)
aurora-backtrack-brief-instance-disruption
  claim: Backtracking causes a brief DB instance disruption.
  scope: Aurora MySQL Backtrack.
  link: [causes a brief DB instance disruption](../facts/aurora.md#aurora-backtrack-brief-instance-disruption)
  link: [brief DB instance disruption](../facts/aurora.md#aurora-backtrack-brief-instance-disruption)
aurora-backtrack-in-minutes-no-new-cluster
  claim: Backtracking a DB cluster does not require a new DB cluster and rewinds the DB cluster in minutes, whereas restoring to a point in time launches a new DB cluster and can take hours.
  scope: Aurora MySQL Backtrack.
  link: [doesn't require a new DB cluster](../facts/aurora.md#aurora-backtrack-in-minutes-no-new-cluster)
  link: [rewinds the DB cluster in minutes](../facts/aurora.md#aurora-backtrack-in-minutes-no-new-cluster)
aurora-backtrack-no-cross-region-replicas
  claim: You cannot create cross-Region read replicas from a backtrack-enabled Aurora cluster, but you can still enable binary log (binlog) replication on the cluster.
  scope: per Aurora MySQL DB cluster with Backtrack enabled.
  link: [can't create cross-Region read replicas](../facts/aurora.md#aurora-backtrack-no-cross-region-replicas)
aurora-backtrack-not-for-postgresql
  claim: Backtrack is not available for Aurora PostgreSQL. It is an Aurora MySQL feature.
  scope: per Aurora DB engine.
  link: [Backtrack is not available for Aurora PostgreSQL](../facts/aurora.md#aurora-backtrack-not-for-postgresql)
aurora-backtrack-only-if-enabled-at-creation
  claim: Backtracking is only available for DB clusters that were created with the Backtrack feature enabled, and you cannot modify a DB cluster to enable it.
  scope: per Aurora MySQL DB cluster.
  link: [created with the Backtrack feature enabled](../facts/aurora.md#aurora-backtrack-only-if-enabled-at-creation)
aurora-backtrack-pay-hourly-for-change-records
  claim: Aurora retains change records for the target backtrack window, and you pay an hourly rate for storing them.
  scope: Aurora MySQL Backtrack.
  link: [you pay an hourly rate for storing them](../facts/aurora.md#aurora-backtrack-pay-hourly-for-change-records)
  link: [retains change records for the target backtrack window](../facts/aurora.md#aurora-backtrack-pay-hourly-for-change-records)
aurora-backtrack-rewind-without-restore
  claim: With Amazon Aurora MySQL-Compatible Edition, you can backtrack a DB cluster to a specific time, without restoring data from a backup.
  scope: Aurora MySQL Backtrack.
  link: [backtrack a DB cluster to a specific time](../facts/aurora.md#aurora-backtrack-rewind-without-restore)
  link: [without restoring data from a backup](../facts/aurora.md#aurora-backtrack-rewind-without-restore)
aurora-backtrack-rewinds-not-replacement-for-backups
  claim: Backtracking is not a replacement for backing up the DB cluster so that you can restore it to a point in time.
  scope: Aurora MySQL Backtrack.
  link: [not a replacement for backing up](../facts/aurora.md#aurora-backtrack-rewinds-not-replacement-for-backups)
  link: [restore it to a point in time](../facts/aurora.md#aurora-backtrack-rewinds-not-replacement-for-backups)
aurora-backtrack-whole-cluster-not-single-table
  claim: Backtracking affects the entire DB cluster, so you cannot selectively backtrack a single table or a single data update.
  scope: Aurora MySQL Backtrack.
  link: [Backtracking affects the entire DB cluster](../facts/aurora.md#aurora-backtrack-whole-cluster-not-single-table)
  link: [can't selectively backtrack a single table](../facts/aurora.md#aurora-backtrack-whole-cluster-not-single-table)
aurora-backtrack-window-limit-72-hours
  claim: The limit for a backtrack window of an Aurora MySQL DB cluster is 72 hours.
  scope: per Aurora MySQL DB cluster with Backtrack enabled; maximum; not adjustable.
  link: [72 hours](../facts/aurora.md#aurora-backtrack-window-limit-72-hours)
  say: seventy-two hours
aurora-backup-awsbackup-snapshots-not-counted-in-quota
  claim: Snapshots managed by AWS Backup are considered manual DB cluster snapshots, but they do not count toward the DB cluster snapshot quota for Aurora.
  scope: per Aurora DB cluster snapshot quota.
  link: [don't count toward the DB cluster snapshot quota](../facts/aurora.md#aurora-backup-awsbackup-snapshots-not-counted-in-quota)
aurora-backup-cannot-disable-automated
  claim: You cannot disable automated backups on Aurora.
  scope: per Aurora DB cluster.
  link: [can't disable automated backups on Aurora](../facts/aurora.md#aurora-backup-cannot-disable-automated)
aurora-backup-continuous-incremental-no-impact
  claim: Aurora automated backups are continuous and incremental, so you can restore to any point within the backup retention period, and no performance impact or interruption of database service occurs as backup data is written.
  scope: per Aurora DB cluster.
  link: [continuous and incremental](../facts/aurora.md#aurora-backup-continuous-incremental-no-impact)
aurora-backup-default-window-30-minutes
  claim: If you do not specify a preferred backup window when you create the DB cluster, Aurora assigns a default 30-minute backup window, selected at random from an 8-hour block of time for each AWS Region.
  scope: per Aurora DB cluster, per AWS Region; default; adjustable.
  link: [default 30-minute backup window](../facts/aurora.md#aurora-backup-default-window-30-minutes)
  link: [8-hour block of time](../facts/aurora.md#aurora-backup-default-window-30-minutes)
  say: a thirty-minute window | an eight-hour block
aurora-backup-free-up-to-100-percent-of-cluster-size
  claim: You are not charged for the backup storage of up to 100% of the size of your database cluster, and there is no charge for database snapshots created within the backup retention period.
  scope: per Aurora DB cluster; maximum.
  link: [up to 100% of the size of your database cluster](../facts/aurora.md#aurora-backup-free-up-to-100-percent-of-cluster-size)
  say: up to one hundred percent of the cluster size
aurora-backup-latest-restorable-time-within-5-minutes
  claim: The latest restorable time of an Aurora DB cluster is the most recent point to which you can restore it. It is typically within 5 minutes of the current time for an active DB cluster.
  scope: per Aurora DB cluster; typical value; for a retained automated backup it is within 5 minutes of the cluster deletion time.
  link: [within 5 minutes of the current time](../facts/aurora.md#aurora-backup-latest-restorable-time-within-5-minutes)
  say: within five minutes of now
aurora-backup-no-charge-1-day-retention
  claim: There is no charge for an Aurora automated backup whose retention period is just 1 day.
  scope: per Aurora DB cluster.
  link: [no charge for an automated backup whose retention period is just 1 day](../facts/aurora.md#aurora-backup-no-charge-1-day-retention)
aurora-backup-retention-default-1-day
  claim: For Amazon Aurora DB clusters, the default backup retention period is one day regardless of how the DB cluster is created.
  scope: per Aurora DB cluster; default; adjustable.
  link: [one day](../facts/aurora.md#aurora-backup-retention-default-1-day)
  say: one day
aurora-backup-retention-period-range-1-35-days
  claim: You can specify an Aurora backup retention period from 1 to 35 days when you create, modify or restore a DB cluster.
  scope: per Aurora DB cluster; maximum; adjustable.
  link: [1–35 days](../facts/aurora.md#aurora-backup-retention-period-range-1-35-days)
  say: one to thirty-five days
aurora-backup-storage-free-equals-cluster-volume-size
  claim: Aurora provides a free amount of backup usage equal to the latest cluster volume size, which is subtracted from the calculated automated backup usage.
  scope: per Aurora DB cluster.
  link: [equal to the latest cluster volume size](../facts/aurora.md#aurora-backup-storage-free-equals-cluster-volume-size)
aurora-backup-storage-free-up-to-total-storage
  claim: There is no additional charge for backup storage of up to 100% of your total Aurora database storage for each Aurora DB cluster.
  scope: per Aurora DB cluster; maximum.
  link: [up to 100% of your total Aurora database storage](../facts/aurora.md#aurora-backup-storage-free-up-to-total-storage)
  link: [no additional charge for backup storage](../facts/aurora.md#aurora-backup-storage-free-up-to-total-storage)
aurora-backup-window-continues-past-window
  claim: If an Aurora backup requires more time than allotted to the backup window, the backup continues after the window ends, until it finishes.
  scope: Aurora automated backups.
  link: [backup continues after the window ends](../facts/aurora.md#aurora-backup-window-continues-past-window)
  link: [more time than allotted](../facts/aurora.md#aurora-backup-window-continues-past-window)
aurora-backup-window-not-overlap-maintenance
  claim: The Aurora backup window cannot overlap with the weekly maintenance window for the DB cluster.
  scope: per Aurora DB cluster.
  link: [can't overlap with the weekly maintenance window](../facts/aurora.md#aurora-backup-window-not-overlap-maintenance)
aurora-backups-automatic-continuous-incremental
  claim: Aurora backs up the cluster volume automatically and retains restore data for the length of the backup retention period.
  scope: Aurora automated backups.
  link: [backs up your cluster volume automatically](../facts/aurora.md#aurora-backups-automatic-continuous-incremental)
  link: [length of the backup retention period](../facts/aurora.md#aurora-backups-automatic-continuous-incremental)
aurora-backups-no-performance-impact
  claim: No performance impact or interruption of database service occurs as Aurora backup data is being written.
  scope: Aurora automated backups.
  link: [No performance impact or interruption of database service](../facts/aurora.md#aurora-backups-no-performance-impact)
  link: [as backup data is being written](../facts/aurora.md#aurora-backups-no-performance-impact)
aurora-best-practice-dns-ttl-under-30-seconds
  claim: If a client application caches the Domain Name Service (DNS) data of DB instances, set a time-to-live (TTL) value of less than 30 seconds.
  scope: Aurora performance best practices.
  link: [set a time-to-live (TTL) value of less than 30 seconds](../facts/aurora.md#aurora-best-practice-dns-ttl-under-30-seconds)
  link: [caching the Domain Name Service (DNS) data](../facts/aurora.md#aurora-best-practice-dns-ttl-under-30-seconds)
aurora-best-practice-ram-working-set-in-memory
  claim: To optimize performance, allocate enough RAM so that your working set resides almost completely in memory.
  scope: Aurora performance best practices.
  link: [allocate enough RAM](../facts/aurora.md#aurora-best-practice-ram-working-set-in-memory)
  link: [working set resides almost completely in memory](../facts/aurora.md#aurora-best-practice-ram-working-set-in-memory)
aurora-best-practice-test-failover
  claim: Test failover for your DB cluster to understand how long the process takes for your use case.
  scope: Aurora DB cluster failover within one Region.
  link: [Test failover for your DB cluster](../facts/aurora.md#aurora-best-practice-test-failover)
  link: [how long the process takes](../facts/aurora.md#aurora-best-practice-test-failover)
aurora-billing-backup-storage-grows-with-retention-and-snapshots
  claim: Increasing the backup retention period or taking additional database snapshots increases the backup storage consumed by the database.
  scope: Aurora DB instance billing and reserved DB instances.
  link: [Increasing your backup retention period](../facts/aurora.md#aurora-billing-backup-storage-grows-with-retention-and-snapshots)
  link: [increases the backup storage consumed by your database](../facts/aurora.md#aurora-billing-backup-storage-grows-with-retention-and-snapshots)
aurora-binary-log-not-needed-for-replication-pitr
  claim: Aurora does not need the binary logs to replicate data within a DB cluster or to perform point-in-time restore (PITR).
  scope: Aurora automated backups.
  link: [does not need the binary logs](../facts/aurora.md#aurora-binary-log-not-needed-for-replication-pitr)
  link: [point-in-time restore (PITR)](../facts/aurora.md#aurora-binary-log-not-needed-for-replication-pitr)
aurora-blue-green-changes-without-affecting-production
  claim: You can make changes to the Aurora DB cluster in the green environment, such as upgrading the engine version or changing parameters, without affecting production workloads.
  scope: Aurora Blue/Green Deployments.
  link: [without affecting production workloads](../facts/aurora.md#aurora-blue-green-changes-without-affecting-production)
  link: [upgrade the major or minor DB engine version](../facts/aurora.md#aurora-blue-green-changes-without-affecting-production)
aurora-blue-green-green-stays-in-sync
  claim: In a blue/green deployment, the blue environment is the current production environment, and the green environment is the staging environment that stays in sync with it.
  scope: Aurora Blue/Green Deployments.
  link: [green environment is the staging environment](../facts/aurora.md#aurora-blue-green-green-stays-in-sync)
  link: [stays in sync with the current production environment](../facts/aurora.md#aurora-blue-green-green-stays-in-sync)
aurora-blue-green-rds-proxy-smart-drivers-reduce-downtime
  claim: Amazon Aurora Blue/Green Deployments support Amazon RDS Proxy and smart drivers, which reduce writer node upgrade downtime during switchover by redirecting connections without waiting for DNS propagation.
  scope: Aurora Blue/Green Deployments.
  link: [support Amazon RDS Proxy and smart drivers](../facts/aurora.md#aurora-blue-green-rds-proxy-smart-drivers-reduce-downtime)
  link: [without waiting for DNS propagation](../facts/aurora.md#aurora-blue-green-rds-proxy-smart-drivers-reduce-downtime)
aurora-blue-green-staging-copy-test-changes
  claim: By using Amazon Aurora Blue/Green Deployments, you can make and test database changes before implementing them in a production environment.
  scope: Aurora Blue/Green Deployments.
  link: [make and test database changes](../facts/aurora.md#aurora-blue-green-staging-copy-test-changes)
  link: [Amazon Aurora Blue/Green Deployments](../facts/aurora.md#aurora-blue-green-staging-copy-test-changes)
aurora-blue-green-supported-engines-and-global-database
  claim: Blue/Green Deployments are supported for Aurora MySQL, Aurora PostgreSQL, and Aurora Global Database.
  scope: Aurora Blue/Green Deployments.
  link: [Aurora MySQL, Aurora PostgreSQL, and Aurora Global Database](../facts/aurora.md#aurora-blue-green-supported-engines-and-global-database)
  link: [Blue/Green Deployments are supported](../facts/aurora.md#aurora-blue-green-supported-engines-and-global-database)
aurora-blue-green-switchover-under-a-minute-no-data-loss
  claim: The switchover of an Aurora blue/green deployment typically takes under a minute with no data loss and no need for application changes.
  scope: Aurora Blue/Green Deployments.
  link: [typically takes under a minute](../facts/aurora.md#aurora-blue-green-switchover-under-a-minute-no-data-loss)
  link: [no data loss](../facts/aurora.md#aurora-blue-green-switchover-under-a-minute-no-data-loss)
aurora-cannot-stop-single-instance
  claim: You cannot stop an individual Aurora DB instance; you stop the whole DB cluster.
  scope: stopping and starting an Aurora DB cluster.
  link: [can't stop an individual Aurora DB instance](../facts/aurora.md#aurora-cannot-stop-single-instance)
  link: [individual Aurora DB instance](../facts/aurora.md#aurora-cannot-stop-single-instance)
aurora-case-draftkings-durable-three-azs-pay-one-copy
  claim: The AWS case study about DraftKings says that Aurora offers storage resiliency by making data durable across three Availability Zones, and that the company only needs to pay for one copy.
  scope: customer case study on the AWS site; case-study text published by AWS, not a service guarantee.
  link: [durable across three Availability Zones](../facts/aurora.md#aurora-case-draftkings-durable-three-azs-pay-one-copy)
aurora-case-draftkings-peak-traffic-minimal-delay
  claim: The AWS case study says that with Aurora, DraftKings can manage the intense read and write operations typical of peak traffic times with minimal delay.
  scope: customer case study on the AWS site; a customer statement published by AWS, not a service guarantee.
  link: [with minimal delay](../facts/aurora.md#aurora-case-draftkings-peak-traffic-minimal-delay)
aurora-case-draftkings-replication-lag-seconds-to-milliseconds
  claim: In the AWS case study a DraftKings architect says that instead of 30 seconds of replication lag during high volume periods, they might see 10-30 milliseconds using Aurora.
  scope: customer case study on the AWS site; a customer statement published by AWS, not a service guarantee.
  link: [10–30 milliseconds using Aurora](../facts/aurora.md#aurora-case-draftkings-replication-lag-seconds-to-milliseconds)
aurora-case-supercell-reduced-downtime
  claim: The AWS case study says that by adopting Amazon Aurora, a MySQL-compatible database service, Supercell has significantly reduced downtime.
  scope: customer case study on the AWS site; a customer statement published by AWS, not a service guarantee.
  link: [significantly reduced downtime](../facts/aurora.md#aurora-case-supercell-reduced-downtime)
aurora-change-backtrack-aurora-mysql-3
  claim: Aurora MySQL 3 versions gained Backtrack on January 4, 2023: you move your database to a prior point in time without restoring from a backup, and it completes within seconds, even for large databases.
  scope: Aurora MySQL 3.* DB clusters; Backtrack is an Aurora MySQL feature.
  link: [it completes within seconds, even for large databases](../facts/aurora.md#aurora-change-backtrack-aurora-mysql-3)
  say: it completes within seconds
aurora-change-blue-green-deployments-introduced
  claim: RDS Blue/Green Deployments let you make changes to an Aurora DB cluster in a staging environment, test them without affecting the production DB cluster, and promote the staging environment to production with minimal downtime; the document history lists this on November 27, 2022.
  scope: Aurora DB clusters, Blue/Green Deployments.
  link: [with minimal downtime](../facts/aurora.md#aurora-change-blue-green-deployments-introduced)
aurora-change-data-api-mysql-serverless-provisioned
  claim: RDS Data API became available for Aurora MySQL clusters that use Aurora serverless or provisioned instances; the document history lists this on September 26, 2024.
  scope: RDS Data API with Aurora MySQL.
  link: [Aurora serverless or provisioned instances](../facts/aurora.md#aurora-change-data-api-mysql-serverless-provisioned)
aurora-change-data-api-postgresql-serverless-provisioned
  claim: RDS Data API became available for Aurora PostgreSQL serverless and provisioned DB clusters on December 21, 2023; it gives access to Aurora clusters through a secure HTTP endpoint, so SQL statements run without database drivers or managed connections.
  scope: RDS Data API with Aurora PostgreSQL.
  link: [a secure HTTP endpoint](../facts/aurora.md#aurora-change-data-api-postgresql-serverless-provisioned)
aurora-change-database-savings-plans-announced
  claim: AWS announced Database Savings Plans, a pricing model that saves up to 35% in exchange for a commitment to a consistent amount of usage over a one-year term with no upfront payment.
  scope: Database Savings Plans; maximum; announced 2025-12-02.
  link: [save up to 35%](../facts/aurora.md#aurora-change-database-savings-plans-announced)
  say: save up to thirty-five percent
aurora-change-database-savings-plans-apply-to-serverless-and-provisioned
  claim: Database Savings Plans automatically apply to eligible serverless and provisioned instance usage regardless of supported engine, instance family, size, deployment option or AWS Region.
  scope: Database Savings Plans; announced 2025-12-02.
  link: [eligible serverless and provisioned instance usage](../facts/aurora.md#aurora-change-database-savings-plans-apply-to-serverless-and-provisioned)
aurora-change-default-encryption-cannot-disable
  claim: You cannot disable encryption on new Aurora clusters, but you can choose a customer managed key or an AWS managed KMS key instead of server-side encryption when you create the cluster.
  scope: new Aurora DB clusters; applies to new clusters where no encryption configuration is provided.
  link: [You cannot disable encryption on new clusters](../facts/aurora.md#aurora-change-default-encryption-cannot-disable)
aurora-change-default-encryption-clones-replicas-stay-unencrypted
  claim: Clones, snapshot copies, and Aurora replicas created from an unencrypted source are not automatically encrypted, because the default applies only to the new cluster itself.
  scope: clones, snapshot copies and replicas of an unencrypted source; source created before February 18, 2026 without encryption.
  link: [are not automatically encrypted](../facts/aurora.md#aurora-change-default-encryption-clones-replicas-stay-unencrypted)
aurora-change-default-encryption-existing-clusters-unaffected
  claim: Existing Aurora clusters are not changed by default server-side encryption, and they keep their current encryption configuration with customer managed or AWS managed KMS keys.
  scope: existing Aurora DB clusters.
  link: [Existing clusters remain unaffected](../facts/aurora.md#aurora-change-default-encryption-existing-clusters-unaffected)
aurora-change-default-encryption-new-clusters
  claim: All new Aurora DB clusters created on or after February 18, 2026 are encrypted by default with an AWS owned key. Older clusters that did not opt in to encryption stay as they were.
  scope: new Aurora DB clusters; default; the What's New post is dated February 16, 2026; the guide gives February 18, 2026.
  link: [encrypted by default with an AWS owned key](../facts/aurora.md#aurora-change-default-encryption-new-clusters)
  say: encrypted by default with an AWS owned key
aurora-change-dsql-generally-available
  claim: AWS announced the general availability of Amazon Aurora DSQL, a serverless, distributed SQL database with active-active high availability and multi-Region strong consistency.
  scope: Amazon Aurora DSQL; general availability announced 2025-05-27.
  link: [serverless, distributed SQL database](../facts/aurora.md#aurora-change-dsql-generally-available)
  say: a serverless, distributed SQL database
aurora-change-extended-support-auto-enable
  claim: Amazon RDS automatically enables Amazon RDS Extended Support when Aurora MySQL and Aurora PostgreSQL major engine versions in your DB clusters and global clusters reach the Aurora end of standard support date; the document history lists this on February 15, 2024.
  scope: Aurora MySQL and Aurora PostgreSQL major engine versions.
  link: [automatically enables Amazon RDS Extended Support](../facts/aurora.md#aurora-change-extended-support-auto-enable)
  say: RDS automatically enables Extended Support
aurora-change-extended-support-auto-enroll-on-create
  claim: Creating or restoring an Aurora MySQL version 2 or 3, or Aurora PostgreSQL version 11 database automatically enrolls that database in Amazon RDS Extended Support, and you can opt out to avoid charges; the document history lists this on March 21, 2024.
  scope: Aurora MySQL version 2 or 3 and Aurora PostgreSQL version 11 databases; you can opt out.
  link: [automatically enrolls that database](../facts/aurora.md#aurora-change-extended-support-auto-enroll-on-create)
  say: automatically enrolls the database in Extended Support
aurora-change-free-tier-express-configuration
  claim: Aurora PostgreSQL became available on the AWS Free Tier: with a Free Plan account you can create an Aurora PostgreSQL serverless cluster with express configuration, which lets you create and query a database in seconds.
  scope: Aurora PostgreSQL serverless on the AWS Free Tier; announced 2026-03-25; available in the Regions where Aurora PostgreSQL serverless is supported.
  link: [using express configuration](../facts/aurora.md#aurora-change-free-tier-express-configuration)
aurora-change-global-db-managed-minor-upgrade-postgresql-only
  claim: Managed minor version upgrades for Aurora Global Database are currently supported only for Aurora PostgreSQL-compatible engines.
  scope: Aurora Global Database; announced 2026-02-10.
  link: [only supported for Aurora PostgreSQL-compatible engines](../facts/aurora.md#aurora-change-global-db-managed-minor-upgrade-postgresql-only)
aurora-change-global-db-managed-minor-version-upgrades
  claim: Aurora Global Database supports managed minor version upgrades: you start the upgrade in the console, SDK or CLI and all global clusters, across Regions, are upgraded to the selected minor version.
  scope: Aurora Global Database; announced 2026-02-10; currently supported only for Aurora PostgreSQL-compatible engines.
  link: [managed minor version upgrades](../facts/aurora.md#aurora-change-global-db-managed-minor-version-upgrades)
  say: managed minor version upgrades
aurora-change-global-failover-managed-unplanned
  claim: On 2023-08-21 Aurora added managed Global Database Failover: you can convert a secondary Region into the new primary Region in typically a minute and keep the Global Database configuration. The planned-event operation, earlier called managed planned failover, is now called switchover.
  scope: Aurora Global Database, cross-Region failover; unplanned events such as a Regional outage; uses managed failover, not switchover.
  link: [in typically a minute](../facts/aurora.md#aurora-change-global-failover-managed-unplanned)
  link: [managed planned failover](../facts/aurora.md#aurora-change-global-failover-managed-unplanned)
  say: in typically a minute | managed planned failover
  changed: 2023-08-21: was managed planned failover
aurora-change-global-writer-endpoint
  claim: The Aurora Global Database writer endpoint automatically updates to point to the current writer instance in the global cluster, so it always points to the primary DB cluster, even after a switchover or failover to a different AWS Region.
  scope: Aurora Global Database; announced 2024-10-22.
  link: [point to the current writer instance](../facts/aurora.md#aurora-change-global-writer-endpoint)
  say: updates itself to the current writer
aurora-change-io-optimized-introduced
  claim: On May 11, 2023, Aurora added a new DB cluster storage configuration: with Aurora I/O-Optimized you pay only for the usage and storage of your DB clusters, with no additional charges for read and write I/O operations.
  scope: Aurora DB cluster storage configuration.
  link: [no additional charges for read and write I/O](../facts/aurora.md#aurora-change-io-optimized-introduced)
  say: no additional charges for read and write I/O operations
aurora-change-limitless-database-ga
  claim: Aurora PostgreSQL Limitless Database offers capabilities such as distributed query planning and transaction management, so you do not need to create custom solutions or manage multiple databases to scale.
  scope: Aurora PostgreSQL Limitless Database.
  link: [distributed query planning and transaction management](../facts/aurora.md#aurora-change-limitless-database-ga)
  say: distributed query planning and transaction management
aurora-change-mysql-delayed-replication
  claim: Aurora MySQL delayed replication lets you configure a binlog replica to lag behind its source by a set period of time, as a safeguard against human error and logical data corruption.
  scope: Aurora MySQL binlog replicas; posted 2026-09-03, after 2026-07-15: not examinable yet.
  link: [lag behind its source by a set period](../facts/aurora.md#aurora-change-mysql-delayed-replication)
aurora-change-mysql-multi-source-delayed-replication-version
  claim: Multi-source replication and delayed replication are supported on Aurora MySQL version 8.4.8 and higher, in all AWS Regions where Aurora MySQL is available.
  scope: Aurora MySQL; minimum; posted 2026-09-03, after 2026-07-15: not examinable yet.
  link: [Aurora MySQL version 8.4.8 and higher](../facts/aurora.md#aurora-change-mysql-multi-source-delayed-replication-version)
aurora-change-mysql-v2-end-of-standard-support
  claim: Aurora MySQL version 2 reached the end of standard support on October 31, 2024.
  scope: Aurora MySQL version 2.
  link: [reached the end of standard support on October 31, 2024](../facts/aurora.md#aurora-change-mysql-v2-end-of-standard-support)
  say: reached the end of standard support on October 31, 2024
aurora-change-performance-insights-end-of-life
  claim: AWS first announced November 30, 2025 as the end-of-life date for Performance Insights; the CloudWatch guide now says the end-of-life date for Performance Insights was July 31, 2026, and that AWS has migrated Performance Insights users to Database Insights.
  scope: Performance Insights; the first announcement (Aurora document history, May 30, 2025) gave November 30, 2025.
  link: [July 31, 2026](../facts/aurora.md#aurora-change-performance-insights-end-of-life)
  link: [migrated Performance Insights users to Database Insights](../facts/aurora.md#aurora-change-performance-insights-end-of-life)
aurora-change-pitr-with-aws-backup
  claim: You can manage Aurora automated (continuous) backups in AWS Backup and restore to specified times from them; the document history lists this on September 7, 2023.
  scope: Aurora automated (continuous) backups managed in AWS Backup.
  link: [restore to specified times from them](../facts/aurora.md#aurora-change-pitr-with-aws-backup)
  say: restore to specified times from them
aurora-change-retain-automated-backups-deleted-cluster
  claim: You can retain automated backups for deleted Aurora clusters and restore them to a specified point in time; the document history lists this on August 4, 2023.
  scope: Aurora DB clusters; you choose to retain the backups when you delete the cluster.
  link: [retain automated backups for deleted Aurora clusters](../facts/aurora.md#aurora-change-retain-automated-backups-deleted-cluster)
  say: retain automated backups for deleted clusters
aurora-change-storage-max-256-tib
  claim: On 2025-07-03 the maximum Aurora cluster storage volume doubled from 128 TiB to 256 TiB for Aurora PostgreSQL-Compatible Edition. The Aurora features page now gives 256 TiB as the maximum size of the database volume, and the Aurora size-limits list says the maximum varies by engine version.
  scope: per Aurora cluster volume; maximum; Aurora cluster volume maximum size varies by engine version.
  link: [256 TiB](../facts/aurora.md#aurora-change-storage-max-256-tib)
  link: [128 TiB](../facts/aurora.md#aurora-change-storage-max-256-tib)
  say: two hundred fifty-six tebibytes | one hundred twenty-eight tebibytes
  changed: 2025-07-03: was 128 TiB
aurora-change-zero-etl-redshift-mysql-ga
  claim: Zero-ETL integrations with Amazon Redshift became generally available for Aurora MySQL on November 7, 2023.
  scope: Aurora MySQL zero-ETL integration with Amazon Redshift.
  link: [now generally available for Aurora MySQL](../facts/aurora.md#aurora-change-zero-etl-redshift-mysql-ga)
aurora-change-zero-etl-redshift-postgresql-ga
  claim: Zero-ETL integrations with Amazon Redshift became generally available for an Aurora PostgreSQL source DB cluster on October 15, 2024; they make transactional data available in Amazon Redshift within seconds of it being written.
  scope: Aurora PostgreSQL zero-ETL integration with Amazon Redshift.
  link: [within seconds of it being written](../facts/aurora.md#aurora-change-zero-etl-redshift-postgresql-ga)
aurora-charged-only-for-space-used
  claim: You are charged only for the space that you use in an Aurora cluster volume, even though the volume can grow up to 256 tebibytes (TiB) for specific engine versions.
  scope: per Aurora cluster volume; maximum; 256 TiB applies to specific engine versions.
  link: [only charged for the space that you use](../facts/aurora.md#aurora-charged-only-for-space-used)
  link: [256 tebibytes (TiB)](../facts/aurora.md#aurora-charged-only-for-space-used)
aurora-clone-copy-on-write-max-15
  claim: You can create up to 15 clones with the copy-on-write protocol; after 15 clones, the next clone that you create is a full copy.
  scope: Aurora cloning, clones created with the copy-on-write protocol; maximum; not adjustable.
  link: [up to 15 clones with copy-on-write protocol](../facts/aurora.md#aurora-clone-copy-on-write-max-15)
  say: fifteen clones
aurora-clone-copy-on-write-storage-on-change
  claim: Additional storage is allocated for a clone only when the source Aurora DB cluster or the clone changes data on the Aurora storage volume.
  scope: Aurora cloning.
  link: [allocated only when changes are made to data](../facts/aurora.md#aurora-clone-copy-on-write-storage-on-change)
aurora-clone-cross-account-default-key-unsupported
  claim: You cannot create a cross-account clone of an Aurora cluster that is encrypted with the default RDS key.
  scope: per Aurora DB cluster.
  link: [can't create a cross-account clone](../facts/aurora.md#aurora-clone-cross-account-default-key-unsupported)
aurora-clone-cross-account-max-15
  claim: You can create a maximum of 15 cross-account clones from any single Aurora DB cluster, and each must be owned by a different AWS account.
  scope: per source Aurora DB cluster; maximum; not adjustable.
  link: [maximum of 15 cross-account clones](../facts/aurora.md#aurora-clone-cross-account-max-15)
  say: fifteen cross-account clones
aurora-clone-cross-vpc-same-availability-zones
  claim: You can create a clone in a different VPC than the source Aurora DB cluster, but the subnets of the VPCs must map to the same Availability Zones.
  scope: per Aurora DB cluster clone.
  link: [different virtual private cloud (VPC)](../facts/aurora.md#aurora-clone-cross-vpc-same-availability-zones)
aurora-clone-instances-configurable-differently
  claim: After creating an Aurora clone, you can configure its DB instances differently from the source Aurora DB cluster.
  scope: Aurora cloning.
  link: [configure the Aurora DB instances differently](../facts/aurora.md#aurora-clone-instances-configurable-differently)
  link: [After creating an Aurora clone](../facts/aurora.md#aurora-clone-instances-configurable-differently)
aurora-clone-multiple-from-same-or-clone
  claim: You can create more than one clone from the same Aurora DB cluster, and multiple clones from another clone.
  scope: Aurora cloning.
  link: [more than one clone](../facts/aurora.md#aurora-clone-multiple-from-same-or-clone)
  link: [multiple clones from another clone](../facts/aurora.md#aurora-clone-multiple-from-same-or-clone)
aurora-clone-needs-source-with-instance
  claim: You cannot create a clone from an Aurora DB cluster that has no DB instances; you can only clone clusters that have at least one DB instance.
  scope: per source Aurora DB cluster.
  link: [at least one DB instance](../facts/aurora.md#aurora-clone-needs-source-with-instance)
aurora-clone-same-region-only
  claim: You cannot create a clone in a different AWS Region from the source Aurora DB cluster.
  scope: per Aurora DB cluster clone.
  link: [can't create a clone](../facts/aurora.md#aurora-clone-same-region-only)
aurora-clone-shares-data-pages-separate-volume
  claim: By using Aurora cloning, you can create a new cluster that initially shares the same data pages as the original, but is a separate and independent volume.
  scope: Aurora cloning.
  link: [shares the same data pages as the original](../facts/aurora.md#aurora-clone-shares-data-pages-separate-volume)
  link: [separate and independent volume](../facts/aurora.md#aurora-clone-shares-data-pages-separate-volume)
aurora-clone-test-with-production-data
  claim: Aurora cloning is especially useful for quickly setting up test environments using production data, without risking data corruption.
  scope: Aurora cloning.
  link: [test environments using your production data](../facts/aurora.md#aurora-clone-test-with-production-data)
  link: [without risking data corruption](../facts/aurora.md#aurora-clone-test-with-production-data)
aurora-cluster-endpoint-also-reads
  claim: You can also use the cluster endpoint for read operations, such as queries.
  scope: Aurora cluster (writer) endpoint.
  link: [use the cluster endpoint for read operations](../facts/aurora.md#aurora-cluster-endpoint-also-reads)
  link: [read operations, such as queries](../facts/aurora.md#aurora-cluster-endpoint-also-reads)
aurora-cluster-endpoint-builtin-cannot-modify
  claim: Each Aurora cluster has a single built-in cluster endpoint whose name and attributes are managed by Aurora, and you cannot create, delete, or modify it.
  scope: Aurora cluster (writer) endpoint.
  link: [single built-in cluster endpoint](../facts/aurora.md#aurora-cluster-endpoint-builtin-cannot-modify)
  link: [can't create, delete, or modify](../facts/aurora.md#aurora-cluster-endpoint-builtin-cannot-modify)
aurora-cluster-endpoint-connects-to-current-primary
  claim: A cluster endpoint (or writer endpoint) for an Aurora DB cluster connects to the current primary DB instance for that DB cluster.
  scope: Aurora cluster (writer) endpoint.
  link: [connects to the current primary DB instance](../facts/aurora.md#aurora-cluster-endpoint-connects-to-current-primary)
  link: [cluster endpoint (or writer endpoint)](../facts/aurora.md#aurora-cluster-endpoint-connects-to-current-primary)
aurora-cluster-endpoint-fails-over-minimal-interruption
  claim: During a failover, the DB cluster continues to serve connection requests to the cluster endpoint from the new primary DB instance, with minimal interruption of service.
  scope: Aurora cluster (writer) endpoint.
  link: [continues to serve connection requests](../facts/aurora.md#aurora-cluster-endpoint-fails-over-minimal-interruption)
  link: [minimal interruption of service](../facts/aurora.md#aurora-cluster-endpoint-fails-over-minimal-interruption)
aurora-cluster-endpoint-ip-changes-after-failover-flush-dns
  claim: The physical IP address pointed to by the cluster endpoint changes when the failover mechanism promotes a new DB instance to be the read/write primary instance.
  scope: Aurora cluster (writer) endpoint.
  link: [pointed to by the cluster endpoint changes](../facts/aurora.md#aurora-cluster-endpoint-ip-changes-after-failover-flush-dns)
  link: [promotes a new DB instance](../facts/aurora.md#aurora-cluster-endpoint-ip-changes-after-failover-flush-dns)
aurora-cluster-endpoint-only-one-for-writes
  claim: The cluster endpoint is the only Aurora endpoint that can perform write operations such as DDL statements.
  scope: Aurora cluster (writer) endpoint.
  link: [the only one that can perform write operations](../facts/aurora.md#aurora-cluster-endpoint-only-one-for-writes)
  link: [write operations such as DDL statements](../facts/aurora.md#aurora-cluster-endpoint-only-one-for-writes)
aurora-cluster-endpoint-stays-same-after-failover
  claim: To use a connection string that stays the same even when a failover promotes a new primary instance, you connect to the cluster endpoint.
  scope: Aurora cluster (writer) endpoint.
  link: [connect to the cluster endpoint](../facts/aurora.md#aurora-cluster-endpoint-stays-same-after-failover)
  link: [stays the same even when a failover promotes](../facts/aurora.md#aurora-cluster-endpoint-stays-same-after-failover)
aurora-cluster-has-instances-and-volume
  claim: An Aurora DB cluster consists of one or more DB instances and a cluster volume that manages the data for those DB instances.
  scope: Aurora cluster volume (shared storage).
  link: [one or more DB instances](../facts/aurora.md#aurora-cluster-has-instances-and-volume)
  link: [a cluster volume that manages the data](../facts/aurora.md#aurora-cluster-has-instances-and-volume)
aurora-cluster-volume-contents-all-data-and-metadata
  claim: The Aurora cluster volume contains all user data, schema objects, and internal metadata such as the system tables and the binary log.
  scope: Aurora cluster volume (shared storage).
  link: [user data, schema objects, and internal metadata](../facts/aurora.md#aurora-cluster-volume-contents-all-data-and-metadata)
  link: [system tables and the binary log](../facts/aurora.md#aurora-cluster-volume-contents-all-data-and-metadata)
aurora-cluster-volume-grows-automatically
  claim: Aurora cluster volumes automatically grow as the amount of data in the database increases.
  scope: Aurora cluster volume (shared storage).
  link: [automatically grow as the amount of data](../facts/aurora.md#aurora-cluster-volume-grows-automatically)
  link: [amount of data in your database increases](../facts/aurora.md#aurora-cluster-volume-grows-automatically)
aurora-cluster-volume-max-256-tib-overview
  claim: An Aurora cluster volume can grow to a maximum size of 256 tebibytes (TiB); the Aurora size-limits list says the maximum size varies by engine version.
  scope: per Aurora DB cluster volume; maximum; not adjustable; Aurora cluster volume maximum size varies by engine version.
  link: [maximum size of 256 tebibytes (TiB)](../facts/aurora.md#aurora-cluster-volume-max-256-tib-overview)
  say: two hundred fifty-six tebibytes
aurora-cluster-volume-spans-azs-copy-each
  claim: An Aurora cluster volume is a virtual database storage volume that spans multiple Availability Zones, and each Availability Zone has a copy of the DB cluster data.
  scope: Aurora cluster volume (shared storage).
  link: [spans multiple Availability Zones](../facts/aurora.md#aurora-cluster-volume-spans-azs-copy-each)
  link: [each Availability Zone having a copy](../facts/aurora.md#aurora-cluster-volume-spans-azs-copy-each)
aurora-cluster-volume-ssd-single-virtual
  claim: Aurora data is stored in the cluster volume, which is a single, virtual volume that uses solid state drives (SSDs).
  scope: Aurora cluster volume (shared storage).
  link: [single, virtual volume](../facts/aurora.md#aurora-cluster-volume-ssd-single-virtual)
  link: [solid state drives (SSDs)](../facts/aurora.md#aurora-cluster-volume-ssd-single-virtual)
aurora-cluster-volume-three-azs-one-region
  claim: A cluster volume consists of copies of the data across three Availability Zones in a single AWS Region.
  scope: Aurora cluster volume (shared storage).
  link: [copies of the data across three Availability Zones](../facts/aurora.md#aurora-cluster-volume-three-azs-one-region)
  link: [single AWS Region](../facts/aurora.md#aurora-cluster-volume-three-azs-one-region)
aurora-cmp-aurora-auto-scaling-adjusts-replicas
  claim: Aurora Auto Scaling dynamically adjusts the number of Aurora Replicas (reader DB instances) in an Aurora DB cluster. It is available for Aurora MySQL and Aurora PostgreSQL.
  scope: Aurora DB cluster; readers only; the writer is not scaled.
  link: [dynamically adjusts the number of Aurora Replicas](../facts/aurora.md#aurora-cmp-aurora-auto-scaling-adjusts-replicas)
aurora-cmp-binlog-cross-region-replica-more-lag
  claim: An Aurora MySQL cross-Region read replica has more lag than a same-Region replica because of the longer network channels between AWS Regions.
  scope: Aurora MySQL cross-Region read replica (binlog).
  link: [there is more lag time](../facts/aurora.md#aurora-cmp-binlog-cross-region-replica-more-lag)
aurora-cmp-global-db-fast-recovery-from-region-outage
  claim: The multi-Region configuration of an Aurora global database provides fast recovery from the rare outage that might affect an entire AWS Region.
  scope: Aurora Global Database.
  link: [fast recovery from the rare outage](../facts/aurora.md#aurora-cmp-global-db-fast-recovery-from-region-outage)
aurora-cmp-global-db-low-latency-reads-worldwide
  claim: A full copy of the data in multiple geographic locations lets an Aurora global database serve low-latency read operations to applications that connect from widely separated locations around the world.
  scope: Aurora Global Database.
  link: [low-latency read operations for applications](../facts/aurora.md#aurora-cmp-global-db-low-latency-reads-worldwide)
aurora-cmp-global-db-minimal-lag-vs-xregion-replica
  claim: AWS gives Aurora Global Database as the alternative to Aurora MySQL cross-Region read replicas when you want to scale reads with minimal lag.
  scope: Aurora MySQL cross-Region replication.
  link: [scale read operations with minimal lag time](../facts/aurora.md#aurora-cmp-global-db-minimal-lag-vs-xregion-replica)
aurora-cmp-global-db-storage-layer-replication-less-than-1-second
  claim: In an Aurora global database the Aurora storage layer, not the database engine, replicates changes from the primary to all secondaries, so lag is minimal and typically less than 1 second. This also means you do not configure or manage binlog replication.
  scope: Aurora global database, primary to secondaries; the sentence is on the Aurora MySQL cross-Region replica page.
  link: [typically, less than 1 second](../facts/aurora.md#aurora-cmp-global-db-storage-layer-replication-less-than-1-second)
  say: typically less than one second
aurora-cmp-global-db-write-forwarding-secondary-to-primary
  claim: With the write forwarding feature you can configure an Aurora global database so that secondary clusters send write requests to the primary.
  scope: Aurora Global Database.
  link: [secondary clusters send write requests to the primary](../facts/aurora.md#aurora-cmp-global-db-write-forwarding-secondary-to-primary)
aurora-cmp-ha-az-failure-no-data-loss-brief-interruption
  claim: An Aurora DB cluster is fault tolerant by design: it can tolerate the failure of an Availability Zone without any loss of data and with only a brief interruption of service.
  scope: Aurora DB cluster within one Region.
  link: [without any loss of data](../facts/aurora.md#aurora-cmp-ha-az-failure-no-data-loss-brief-interruption)
  link: [only a brief interruption of service](../facts/aurora.md#aurora-cmp-ha-az-failure-no-data-loss-brief-interruption)
aurora-cmp-rds-promote-replica-minutes-reboot
  claim: For DB instances other than Aurora, promoting a read replica to take over read/write work takes a few minutes, and a reboot is part of the process.
  scope: RDS read replica promotion (non-Aurora); DR whitepaper wording; non-Aurora RDS engines.
  link: [takes a few minutes to complete](../facts/aurora.md#aurora-cmp-rds-promote-replica-minutes-reboot)
aurora-cmp-reader-endpoint-and-auto-scaling
  claim: Aurora provides a reader endpoint for automatic connection routing and load balancing across read replicas, and supports auto scaling that adds and removes replicas based on your performance metrics settings.
  scope: Aurora read replicas.
  link: [a reader endpoint for automatic connection routing](../facts/aurora.md#aurora-cmp-reader-endpoint-and-auto-scaling)
aurora-cmp-replica-lag-often-single-digit-milliseconds
  claim: The Aurora features page says that because replicas do not perform writes, more processing power serves reads and replica lag is reduced, often down to single-digit milliseconds.
  scope: Aurora read replicas in one Region.
  link: [often down to single-digit milliseconds](../facts/aurora.md#aurora-cmp-replica-lag-often-single-digit-milliseconds)
  say: often single-digit milliseconds
aurora-cmp-replicas-share-storage-no-replica-writes
  claim: Aurora read replicas share the same underlying storage as the primary instance, which lowers cost and avoids the need to perform writes at the replica nodes.
  scope: Aurora read replicas.
  link: [share the same underlying storage](../facts/aurora.md#aurora-cmp-replicas-share-storage-no-replica-writes)
aurora-cmp-wp-active-active-async-replication-near-zero-rpo
  claim: The DR whitepaper says asynchronous data replication in the multi-site active/active strategy enables near-zero RPO, and it names Aurora global database as an example service.
  scope: DR whitepaper, multi-site active/active.
  link: [near-zero RPO](../facts/aurora.md#aurora-cmp-wp-active-active-async-replication-near-zero-rpo)
aurora-cmp-wp-global-db-dedicated-infrastructure-latency
  claim: The DR whitepaper says an Aurora global database uses dedicated infrastructure that leaves the databases fully available to the application and replicates to the secondary Region with typical latency of under a second.
  scope: Aurora global database replication.
  link: [typical latency of under a second](../facts/aurora.md#aurora-cmp-wp-global-db-dedicated-infrastructure-latency)
  say: typical latency of under a second
aurora-cmp-wp-global-db-monitor-rpo-lag
  claim: You can configure Aurora to monitor the RPO lag time of all secondary clusters, so that at least one secondary cluster stays within your target RPO window.
  scope: Aurora global database.
  link: [stays within your target RPO window](../facts/aurora.md#aurora-cmp-wp-global-db-monitor-rpo-lag)
aurora-cmp-wp-global-db-promote-under-one-minute
  claim: The DR whitepaper says that if the primary Region suffers a performance degradation or outage, you can promote one of the secondary Regions of an Aurora global database to take read/write responsibilities in less than one minute, even in a complete regional outage.
  scope: Aurora global database promotion.
  link: [in less than one minute](../facts/aurora.md#aurora-cmp-wp-global-db-promote-under-one-minute)
  say: in less than one minute
aurora-cmp-wp-multi-site-recovery-near-zero
  claim: The DR whitepaper says multi-site active/active is the most complex and costly DR approach, but it can reduce recovery time to near zero for most disasters; data corruption may still need backups, which usually means a non-zero recovery point.
  scope: DR whitepaper, multi-site active/active.
  link: [recovery time to near zero](../facts/aurora.md#aurora-cmp-wp-multi-site-recovery-near-zero)
aurora-cmp-wp-pilot-light-continuous-replication-best-for-rpo
  claim: For the pilot light DR strategy, the DR whitepaper says continuous data replication to live databases and data stores in the DR Region is the best approach for low RPO, in addition to point-in-time backups. Aurora global databases are on its list of services that provide this replication.
  scope: DR whitepaper, pilot light.
  link: [the best approach for low RPO](../facts/aurora.md#aurora-cmp-wp-pilot-light-continuous-replication-best-for-rpo)
aurora-cmp-wp-pilot-light-core-infrastructure-always-available
  claim: In the pilot light strategy the core infrastructure is always available, and unlike backup and restore you can quickly provision a full scale production environment by switching on and scaling out the application servers.
  scope: DR whitepaper, pilot light; data stores such as databases are always on; application servers are switched off.
  link: [your core infrastructure is always available](../facts/aurora.md#aurora-cmp-wp-pilot-light-core-infrastructure-always-available)
aurora-cmp-wp-warm-standby-faster-than-pilot-light
  claim: In the warm standby strategy a scaled down but fully functional copy of the production environment runs in another Region, which extends the pilot light idea and decreases the time to recovery because the workload is always on.
  scope: DR whitepaper, warm standby.
  link: [decreases the time to recovery](../facts/aurora.md#aurora-cmp-wp-warm-standby-faster-than-pilot-light)
aurora-cmp-wp-write-global-fit
  claim: The DR whitepaper calls Aurora global database a good fit for the write global strategy, because it supports synchronization with read-replicas across Regions and you can promote one of the secondary Regions to take read/write responsibilities in less than one minute.
  scope: DR whitepaper, multi-site active/active.
  link: [supports synchronization with read-replicas across Regions](../facts/aurora.md#aurora-cmp-wp-write-global-fit)
  link: [in less than one minute](../facts/aurora.md#aurora-cmp-wp-write-global-fit)
aurora-convert-to-multi-az-by-adding-reader-other-az
  claim: You can convert an existing Aurora DB cluster into a Multi-AZ DB cluster by adding a new reader DB instance and specifying a different AZ.
  scope: Aurora DB cluster failover within one Region.
  link: [adding a new reader DB instance](../facts/aurora.md#aurora-convert-to-multi-az-by-adding-reader-other-az)
  link: [specifying a different AZ](../facts/aurora.md#aurora-convert-to-multi-az-by-adding-reader-other-az)
aurora-copy-cross-region-cross-account-share-first
  claim: To copy a snapshot cross-Region and cross-account in a single action, you must first share the snapshot with the target AWS account, and if it is encrypted, also share the AWS KMS key.
  scope: Aurora DB cluster snapshots.
  link: [must first share the snapshot](../facts/aurora.md#aurora-copy-cross-region-cross-account-share-first)
  link: [share the AWS KMS key](../facts/aurora.md#aurora-copy-cross-region-cross-account-share-first)
aurora-copy-encrypted-snapshot-cross-region-destination-key
  claim: To copy an encrypted snapshot from one AWS Region to another, you must specify the KMS key in the destination AWS Region, because KMS keys are specific to the Region where they are created.
  scope: Aurora DB cluster snapshots.
  link: [KMS key in the destination AWS Region](../facts/aurora.md#aurora-copy-encrypted-snapshot-cross-region-destination-key)
  link: [KMS keys are specific to the AWS Region](../facts/aurora.md#aurora-copy-encrypted-snapshot-cross-region-destination-key)
aurora-copy-encrypted-snapshot-stays-encrypted
  claim: If you copy an encrypted snapshot, the copy must also be encrypted.
  scope: Aurora DB cluster snapshots.
  link: [must also be encrypted](../facts/aurora.md#aurora-copy-encrypted-snapshot-stays-encrypted)
  link: [copy an encrypted snapshot](../facts/aurora.md#aurora-copy-encrypted-snapshot-stays-encrypted)
aurora-custom-endpoint-avoids-cname-updates-and-supports-tls
  claim: With custom endpoints you can avoid updating CNAME records when your cluster grows or shrinks, and you can use encrypted TLS/SSL connections.
  scope: Aurora custom endpoints.
  link: [avoid updating CNAME records](../facts/aurora.md#aurora-custom-endpoint-avoids-cname-updates-and-supports-tls)
  link: [encrypted Transport Layer Security/Secure Sockets Layer (TLS/SSL) connections](../facts/aurora.md#aurora-custom-endpoint-avoids-cname-updates-and-supports-tls)
aurora-custom-endpoint-balances-beyond-read-only-vs-writer
  claim: A custom endpoint provides balanced database connections based on criteria other than the read-only or read/write capability of the DB instances.
  scope: Aurora custom endpoints.
  link: [criteria other than the read-only or read/write capability](../facts/aurora.md#aurora-custom-endpoint-balances-beyond-read-only-vs-writer)
  link: [balanced database connections](../facts/aurora.md#aurora-custom-endpoint-balances-beyond-read-only-vs-writer)
aurora-custom-endpoint-console-type-any
  claim: You cannot select the custom endpoint type in the console, and all custom endpoints created through the console have type ANY; you can set the type with the AWS CLI or Amazon RDS API.
  scope: Aurora custom endpoints.
  link: [have a type of `ANY`](../facts/aurora.md#aurora-custom-endpoint-console-type-any)
  link: [can't select the custom endpoint type](../facts/aurora.md#aurora-custom-endpoint-console-type-any)
aurora-custom-endpoint-existing-connections-stay-on-membership-change
  claim: When you add a DB instance to a custom endpoint or remove it from one, any existing connections to that DB instance remain active.
  scope: Aurora custom endpoints.
  link: [existing connections to that DB instance remain active](../facts/aurora.md#aurora-custom-endpoint-existing-connections-stay-on-membership-change)
  link: [add a DB instance to a custom endpoint](../facts/aurora.md#aurora-custom-endpoint-existing-connections-stay-on-membership-change)
aurora-custom-endpoint-name-max-63-characters
  claim: The maximum length for an Aurora custom endpoint name is 63 characters.
  scope: per custom endpoint name; maximum; not adjustable.
  link: [63 characters](../facts/aurora.md#aurora-custom-endpoint-name-max-63-characters)
  say: sixty-three characters
aurora-custom-endpoint-none-until-created-up-to-five
  claim: An Aurora DB cluster has no custom endpoints until you create one, and you can create up to five custom endpoints for each provisioned Aurora cluster or Aurora serverless cluster.
  scope: per provisioned Aurora cluster or Aurora serverless cluster; maximum; not adjustable.
  link: [up to five custom endpoints](../facts/aurora.md#aurora-custom-endpoint-none-until-created-up-to-five)
  link: [no custom endpoints until you create one](../facts/aurora.md#aurora-custom-endpoint-none-until-created-up-to-five)
aurora-custom-endpoint-not-in-snapshot-recreate-after-restore
  claim: Custom endpoints are not included in a snapshot, so you create them again after restoring a cluster.
  scope: Aurora custom endpoints.
  link: [Custom endpoints are not included in the snapshot](../facts/aurora.md#aurora-custom-endpoint-not-in-snapshot-recreate-after-restore)
  link: [create them again after restoring](../facts/aurora.md#aurora-custom-endpoint-not-in-snapshot-recreate-after-restore)
aurora-custom-endpoint-passive-dns-random-balancing
  claim: Custom endpoints distribute connections across instances passively, using DNS to return the IP address of one of the instances randomly.
  scope: Aurora custom endpoints.
  link: [distribute connections across instances passively](../facts/aurora.md#aurora-custom-endpoint-passive-dns-random-balancing)
  link: [one of the instances randomly](../facts/aurora.md#aurora-custom-endpoint-passive-dns-random-balancing)
aurora-custom-endpoint-reader-type-membership-follows-failover
  claim: With the AWS CLI or Amazon RDS API you can specify the endpoint type, and for a READER custom endpoint the membership is automatically adjusted during failovers and promotions.
  scope: Aurora custom endpoints.
  link: [automatically adjusted during failovers and promotions](../facts/aurora.md#aurora-custom-endpoint-reader-type-membership-follows-failover)
  link: [endpoint type is set to `READER`](../facts/aurora.md#aurora-custom-endpoint-reader-type-membership-follows-failover)
aurora-custom-endpoint-set-of-chosen-instances
  claim: A custom endpoint for an Aurora cluster represents a set of DB instances that you choose, and Aurora balances connections among the instances in the group.
  scope: Aurora custom endpoints.
  link: [a set of DB instances that you choose](../facts/aurora.md#aurora-custom-endpoint-set-of-chosen-instances)
  link: [custom endpoint](../facts/aurora.md#aurora-custom-endpoint-set-of-chosen-instances)
aurora-custom-endpoint-skip-reader-endpoint-when-using
  claim: When you use custom endpoints, you typically do not use the reader endpoint for that cluster.
  scope: Aurora custom endpoints.
  link: [typically don't use the reader endpoint](../facts/aurora.md#aurora-custom-endpoint-skip-reader-endpoint-when-using)
  link: [When you use custom endpoints](../facts/aurora.md#aurora-custom-endpoint-skip-reader-endpoint-when-using)
aurora-custom-endpoint-static-or-exclusion-list
  claim: A custom endpoint can have a list of DB instances to include (a static list) or to exclude (an exclusion list), and each custom endpoint can contain only one of these list types.
  scope: Aurora custom endpoints.
  link: [include in, or exclude from, a custom endpoint](../facts/aurora.md#aurora-custom-endpoint-static-or-exclusion-list)
  link: [only one of these list types](../facts/aurora.md#aurora-custom-endpoint-static-or-exclusion-list)
aurora-custom-endpoint-types-reader-any
  claim: Both reader and writer DB instances can be part of a custom endpoint of type ANY, and only reader DB instances can be part of a READER custom endpoint.
  scope: Aurora custom endpoints.
  link: [Both reader and writer DB instances](../facts/aurora.md#aurora-custom-endpoint-types-reader-any)
  link: [Only reader DB instances](../facts/aurora.md#aurora-custom-endpoint-types-reader-any)
aurora-custom-endpoint-unavailable-replica-stays-associated
  claim: If an Aurora Replica becomes unavailable, it remains associated with any custom endpoints, but you cannot connect to it through those endpoints until it becomes available again.
  scope: Aurora custom endpoints.
  link: [remains associated with any custom endpoints](../facts/aurora.md#aurora-custom-endpoint-unavailable-replica-stays-associated)
  link: [becomes unavailable](../facts/aurora.md#aurora-custom-endpoint-unavailable-replica-stays-associated)
aurora-custom-endpoint-use-different-instance-classes-reporting
  claim: You can define a custom endpoint to connect to instances that use a particular instance class or DB parameter group, for example to send internal users to low-capacity instances for reports and production traffic to high-capacity instances.
  scope: Aurora custom endpoints.
  link: [particular DB parameter group](../facts/aurora.md#aurora-custom-endpoint-use-different-instance-classes-reporting)
  link: [instances that use a particular AWS instance class](../facts/aurora.md#aurora-custom-endpoint-use-different-instance-classes-reporting)
aurora-custom-endpoints-preferred-over-instance-endpoint-for-special-instances
  claim: When some DB instances are configured differently from others, AWS recommends custom endpoints instead of the instance endpoint.
  scope: Aurora custom endpoints.
  link: [use custom endpoints instead of the instance endpoint](../facts/aurora.md#aurora-custom-endpoints-preferred-over-instance-endpoint-for-special-instances)
  link: [custom endpoints](../facts/aurora.md#aurora-custom-endpoints-preferred-over-instance-endpoint-for-special-instances)
aurora-customer-responsible-query-tuning
  claim: Under the shared responsibility model, the customer is responsible for query tuning, which is the process of adjusting SQL queries to improve performance.
  scope: Amazon Aurora overview.
  link: [responsible for query tuning](../facts/aurora.md#aurora-customer-responsible-query-tuning)
  link: [adjusting SQL queries to improve performance](../facts/aurora.md#aurora-customer-responsible-query-tuning)
aurora-das-dbas-no-access-to-streams
  claim: Database administrators do not have access to the collection, transmission, storage, and processing of database activity streams.
  scope: Database Activity Streams for Aurora.
  link: [DBAs don't have access](../facts/aurora.md#aurora-das-dbas-no-access-to-streams)
  link: [control administrator access to data streams](../facts/aurora.md#aurora-das-dbas-no-access-to-streams)
aurora-das-free-but-kinesis-charges
  claim: Use of the database activity streams feature in Amazon Aurora is free, but Amazon Kinesis charges for a data stream.
  scope: Database Activity Streams for Aurora.
  link: [feature in Amazon Aurora is free](../facts/aurora.md#aurora-das-free-but-kinesis-charges)
  link: [Amazon Kinesis charges for a data stream](../facts/aurora.md#aurora-das-free-but-kinesis-charges)
aurora-das-global-db-start-each-cluster
  claim: If you use an Aurora global database, you start a database activity stream on each DB cluster separately, and each cluster delivers audit data to its own Kinesis stream within its own AWS Region.
  scope: Database Activity Streams for Aurora.
  link: [on each DB cluster separately](../facts/aurora.md#aurora-das-global-db-start-each-cluster)
  link: [own Kinesis stream within its own AWS Region](../facts/aurora.md#aurora-das-global-db-start-each-cluster)
aurora-das-near-real-time-monitoring
  claim: By using Database Activity Streams, you can monitor near real-time streams of database activity in Aurora.
  scope: Database Activity Streams for Aurora.
  link: [monitor near real-time streams of database activity](../facts/aurora.md#aurora-das-near-real-time-monitoring)
  link: [Database Activity Streams](../facts/aurora.md#aurora-das-near-real-time-monitoring)
aurora-das-pushes-to-kinesis
  claim: An Aurora DB cluster with Database Activity Streams pushes activities to an Amazon Kinesis data stream in near real time, and the Kinesis stream is created automatically.
  scope: Database Activity Streams for Aurora.
  link: [pushes activities to an Amazon Kinesis data stream](../facts/aurora.md#aurora-das-pushes-to-kinesis)
  link: [in near real time](../facts/aurora.md#aurora-das-pushes-to-kinesis)
aurora-das-requires-kinesis-and-kms
  claim: AWS KMS is required for database activity streams because they are always encrypted, and Amazon Kinesis is also required.
  scope: Database Activity Streams for Aurora.
  link: [AWS Key Management Service (AWS KMS) is required](../facts/aurora.md#aurora-das-requires-kinesis-and-kms)
  link: [they are always encrypted](../facts/aurora.md#aurora-das-requires-kinesis-and-kms)
aurora-das-started-at-cluster-level
  claim: In Amazon Aurora, you start a database activity stream at the cluster level, and all DB instances in the cluster have database activity streams enabled.
  scope: Database Activity Streams for Aurora.
  link: [at the cluster level](../facts/aurora.md#aurora-das-started-at-cluster-level)
aurora-das-synchronous-mode-postgres-only
  claim: Synchronous mode for database activity streams is available for Aurora PostgreSQL, and you cannot use synchronous mode with Aurora MySQL.
  scope: Database Activity Streams for Aurora.
  link: [Synchronous mode is available for Aurora PostgreSQL](../facts/aurora.md#aurora-das-synchronous-mode-postgres-only)
  link: [can't use synchronous mode with Aurora MySQL](../facts/aurora.md#aurora-das-synchronous-mode-postgres-only)
aurora-data-transfer-between-azs-for-replication-free
  claim: Data transferred between Availability Zones for DB cluster replication is free in Aurora.
  scope: per Aurora DB cluster.
  link: [for DB cluster replication is free](../facts/aurora.md#aurora-data-transfer-between-azs-for-replication-free)
aurora-db-subnet-group-collection-of-subnets
  claim: A DB subnet group is a collection of subnets, typically private, that you create in a VPC and then designate for your DB clusters.
  scope: Aurora DB clusters in a VPC.
  link: [collection of subnets (typically private)](../facts/aurora.md#aurora-db-subnet-group-collection-of-subnets)
  link: [designate for your DB clusters](../facts/aurora.md#aurora-db-subnet-group-collection-of-subnets)
aurora-db-subnet-group-two-azs
  claim: Each DB subnet group must have at least one subnet in at least two Availability Zones in the AWS Region.
  scope: Aurora DB clusters in a VPC.
  link: [at least two Availability Zones](../facts/aurora.md#aurora-db-subnet-group-two-azs)
  link: [Each DB subnet group must have](../facts/aurora.md#aurora-db-subnet-group-two-azs)
aurora-default-vpc-new-clusters-created-there
  claim: Accounts have a default VPC, and all new DB clusters are created in the default VPC unless you specify otherwise.
  scope: per account; default; not adjustable.
  link: [created in the default VPC](../facts/aurora.md#aurora-default-vpc-new-clusters-created-there)
  link: [Accounts have a default VPC](../facts/aurora.md#aurora-default-vpc-new-clusters-created-there)
aurora-delete-cluster-removes-volume-and-data
  claim: Deleting an Aurora cluster removes the cluster volume containing all your data, but you can save a snapshot of your data before deleting.
  scope: deleting Aurora DB instances and clusters.
  link: [removes the cluster volume containing all your data](../facts/aurora.md#aurora-delete-cluster-removes-volume-and-data)
  link: [Deleting the cluster](../facts/aurora.md#aurora-delete-cluster-removes-volume-and-data)
aurora-delete-instances-keep-cluster-and-data
  claim: You can delete DB instances from an Aurora cluster while preserving the cluster itself and the data that it contains.
  scope: deleting Aurora DB instances and clusters.
  link: [preserving the cluster itself](../facts/aurora.md#aurora-delete-instances-keep-cluster-and-data)
  link: [the data that it contains](../facts/aurora.md#aurora-delete-instances-keep-cluster-and-data)
aurora-deletion-protection-blocks-cluster-delete
  claim: You cannot delete clusters that have deletion protection enabled, though you can delete DB instances within the cluster.
  scope: deleting Aurora DB instances and clusters.
  link: [can't delete clusters that have deletion protection enabled](../facts/aurora.md#aurora-deletion-protection-blocks-cluster-delete)
  link: [deletion protection enabled](../facts/aurora.md#aurora-deletion-protection-blocks-cluster-delete)
aurora-deletion-protection-default-console-vs-cli
  claim: Deletion protection is enabled by default when you create a production DB cluster in the AWS Management Console, but disabled by default when you create a cluster with the AWS CLI or API.
  scope: per Aurora DB cluster, depends on how the cluster is created; default; adjustable.
  link: [enabled by default when you create a production](../facts/aurora.md#aurora-deletion-protection-default-console-vs-cli)
  link: [disabled by default if you create a cluster](../facts/aurora.md#aurora-deletion-protection-default-console-vs-cli)
aurora-deletion-protection-toggle-no-outage
  claim: Enabling or disabling deletion protection does not cause an outage.
  scope: deleting Aurora DB instances and clusters.
  link: [doesn't cause an outage](../facts/aurora.md#aurora-deletion-protection-toggle-no-outage)
  link: [Enabling or disabling deletion protection](../facts/aurora.md#aurora-deletion-protection-toggle-no-outage)
aurora-detects-problems-activates-failover-automatically
  claim: Aurora detects database problems and activates the failover mechanism automatically when necessary.
  scope: Aurora DB cluster failover within one Region.
  link: [detects database problems](../facts/aurora.md#aurora-detects-problems-activates-failover-automatically)
  link: [activates the failover mechanism automatically](../facts/aurora.md#aurora-detects-problems-activates-failover-automatically)
aurora-dg-dsql-active-active-multi-region
  claim: The AWS database decision guide says to use Amazon Aurora DSQL when the application needs distributed SQL with active-active multi-Region replication, strong consistency, and no servers to manage.
  scope: Aurora DSQL in the AWS database decision guide; out of scope for the exam; mention only to rule it out.
  link: [distributed SQL with active-active multi-Region replication](../facts/aurora.md#aurora-dg-dsql-active-active-multi-region)
  say: distributed SQL with active-active multi-Region replication
aurora-dg-limitless-beyond-single-instance
  claim: The AWS database decision guide says to use Aurora PostgreSQL Limitless Database when the relational workload needs write throughput or storage beyond the limits of a single Aurora instance, while keeping a single-database experience.
  scope: Aurora PostgreSQL Limitless Database in the AWS database decision guide; Aurora PostgreSQL only.
  link: [beyond the limits of a single Aurora instance](../facts/aurora.md#aurora-dg-limitless-beyond-single-instance)
  say: beyond the limits of a single Aurora instance
aurora-dg-use-when-relational-modernize
  claim: The AWS database decision guide says to choose Amazon Aurora when you are migrating or modernizing an on-premises relational workload, or when the workload has less predictable query patterns, and that Aurora supports MySQL- and PostgreSQL-compatible engines.
  scope: Aurora in the AWS database decision guide; guidance, not a limit.
  link: [migrating or modernizing an on-premises relational workload](../facts/aurora.md#aurora-dg-use-when-relational-modernize)
  say: migrating or modernizing an on-premises relational workload
aurora-disabled-kms-key-cluster-inaccessible-recoverable
  claim: When you disable the KMS key of an encrypted Aurora DB cluster, Aurora can lose access to it, and the cluster goes into the inaccessible-encryption-credentials-recoverable state, where the instance is stopped for seven days.
  scope: Aurora encryption at rest with AWS KMS.
  link: [lose access to the KMS key](../facts/aurora.md#aurora-disabled-kms-key-cluster-inaccessible-recoverable)
  link: [remains in this state for seven days](../facts/aurora.md#aurora-disabled-kms-key-cluster-inaccessible-recoverable)
aurora-distribute-instances-multiple-azs-recommended
  claim: AWS recommends distributing the primary instance and reader instances of an Aurora DB cluster over multiple AZs to improve availability.
  scope: Aurora DB cluster failover within one Region.
  link: [distribute the primary instance and reader instances](../facts/aurora.md#aurora-distribute-instances-multiple-azs-recommended)
  link: [over multiple AZs](../facts/aurora.md#aurora-distribute-instances-multiple-azs-recommended)
aurora-encrypted-cluster-all-instances-logs-backups-snapshots
  claim: For an Aurora encrypted DB cluster, all DB instances, logs, backups, and snapshots are encrypted.
  scope: Aurora encryption at rest with AWS KMS.
  link: [logs, backups, and snapshots are encrypted](../facts/aurora.md#aurora-encrypted-cluster-all-instances-logs-backups-snapshots)
  link: [Amazon Aurora encrypted DB cluster](../facts/aurora.md#aurora-encrypted-cluster-all-instances-logs-backups-snapshots)
aurora-encrypted-cluster-snapshot-same-kms-key
  claim: A snapshot of an encrypted DB cluster must be encrypted using the same KMS key as the DB cluster.
  scope: Aurora encryption at rest with AWS KMS.
  link: [same KMS key as the DB cluster](../facts/aurora.md#aurora-encrypted-cluster-snapshot-same-kms-key)
  link: [snapshot of an encrypted DB cluster](../facts/aurora.md#aurora-encrypted-cluster-snapshot-same-kms-key)
aurora-encrypted-snapshot-cannot-be-public
  claim: Making an encrypted Aurora snapshot public is not supported.
  scope: sharing encrypted Aurora DB cluster snapshots.
  link: [making such snapshots public isn't supported](../facts/aurora.md#aurora-encrypted-snapshot-cannot-be-public)
  link: [encrypted snapshots](../facts/aurora.md#aurora-encrypted-snapshot-cannot-be-public)
aurora-encryption-cannot-convert-unencrypted-in-place
  claim: You cannot convert an unencrypted DB cluster to an encrypted one, but you can restore an unencrypted snapshot to an encrypted Aurora DB cluster by specifying a KMS key.
  scope: Aurora encryption at rest with AWS KMS.
  link: [can't convert an unencrypted DB cluster](../facts/aurora.md#aurora-encryption-cannot-convert-unencrypted-in-place)
  link: [restore an unencrypted snapshot](../facts/aurora.md#aurora-encryption-cannot-convert-unencrypted-in-place)
aurora-encryption-cannot-turn-off
  claim: You cannot turn off encryption on an encrypted Aurora DB cluster.
  scope: Aurora encryption at rest with AWS KMS.
  link: [can't turn off encryption](../facts/aurora.md#aurora-encryption-cannot-turn-off)
  link: [encrypted DB cluster](../facts/aurora.md#aurora-encryption-cannot-turn-off)
aurora-encryption-kms-key-cannot-change
  claim: Once you have created an encrypted DB cluster, you cannot change the KMS key used by that DB cluster.
  scope: Aurora encryption at rest with AWS KMS.
  link: [can't change the KMS key](../facts/aurora.md#aurora-encryption-kms-key-cannot-change)
  link: [created an encrypted DB cluster](../facts/aurora.md#aurora-encryption-kms-key-cannot-change)
aurora-encryption-same-kms-key-all-instances
  claim: Each DB instance in an Aurora DB cluster shares the same storage, encrypted with the same KMS key.
  scope: Aurora encryption at rest with AWS KMS.
  link: [encrypted with the same KMS key](../facts/aurora.md#aurora-encryption-same-kms-key-all-instances)
  link: [Each DB instance in the DB cluster](../facts/aurora.md#aurora-encryption-same-kms-key-all-instances)
aurora-encryption-transparent-no-client-changes
  claim: You do not need to modify your database client applications to use Aurora encryption.
  scope: Aurora encryption at rest with AWS KMS.
  link: [don't need to modify your database client applications](../facts/aurora.md#aurora-encryption-transparent-no-client-changes)
  link: [use encryption](../facts/aurora.md#aurora-encryption-transparent-no-client-changes)
aurora-encryption-uses-aws-kms-key
  claim: Amazon Aurora uses an AWS Key Management Service (AWS KMS) key to encrypt its encrypted resources.
  scope: Aurora encryption at rest with AWS KMS.
  link: [uses an AWS Key Management Service key](../facts/aurora.md#aurora-encryption-uses-aws-kms-key)
  link: [AWS Key Management Service key](../facts/aurora.md#aurora-encryption-uses-aws-kms-key)
aurora-endpoint-abstracts-connections-no-hardcode
  claim: Because Aurora uses endpoints to abstract connections, you do not have to hardcode all the hostnames or write your own logic for balancing and rerouting connections when some DB instances are not available.
  scope: Aurora cluster (writer) endpoint.
  link: [hardcode all the hostnames](../facts/aurora.md#aurora-endpoint-abstracts-connections-no-hardcode)
  link: [balancing and rerouting connections](../facts/aurora.md#aurora-endpoint-abstracts-connections-no-hardcode)
aurora-every-instance-in-one-of-three-azs
  claim: Every DB instance in an Aurora cluster must be in one of the three AZs that host the cluster's storage copies.
  scope: Aurora cluster volume (shared storage).
  link: [must be in one of these three AZs](../facts/aurora.md#aurora-every-instance-in-one-of-three-azs)
  link: [Every DB instance in the cluster](../facts/aurora.md#aurora-every-instance-in-one-of-three-azs)
aurora-existing-mysql-postgres-code-works
  claim: The code, tools, and applications that work with existing MySQL and PostgreSQL databases can be used with Aurora.
  scope: Amazon Aurora overview.
  link: [code, tools, and applications](../facts/aurora.md#aurora-existing-mysql-postgres-code-works)
  link: [can be used with Aurora](../facts/aurora.md#aurora-existing-mysql-postgres-code-works)
aurora-export-snapshot-all-data-by-default
  claim: By default, all data in the snapshot is exported, but you can choose to export specific sets of databases, schemas, or tables.
  scope: per snapshot export; default; not adjustable.
  link: [all data in the snapshot is exported](../facts/aurora.md#aurora-export-snapshot-all-data-by-default)
  link: [specific sets of databases, schemas, or tables](../facts/aurora.md#aurora-export-snapshot-all-data-by-default)
aurora-export-snapshot-analyze-with-athena-redshift-spectrum
  claim: After the data is exported, you can analyze it directly with tools like Amazon Athena or Amazon Redshift Spectrum.
  scope: Aurora snapshot export to Amazon S3.
  link: [Amazon Athena or Amazon Redshift Spectrum](../facts/aurora.md#aurora-export-snapshot-analyze-with-athena-redshift-spectrum)
  link: [analyze the exported data directly](../facts/aurora.md#aurora-export-snapshot-analyze-with-athena-redshift-spectrum)
aurora-export-snapshot-parquet-format
  claim: Exported Aurora snapshot data is stored in an Apache Parquet format that is compressed and consistent.
  scope: Aurora snapshot export to Amazon S3.
  link: [Apache Parquet format](../facts/aurora.md#aurora-export-snapshot-parquet-format)
  link: [compressed and consistent](../facts/aurora.md#aurora-export-snapshot-parquet-format)
aurora-export-snapshot-to-s3-background
  claim: You can export DB cluster snapshot data to an Amazon S3 bucket, and the export process runs in the background and does not affect the performance of the active DB cluster.
  scope: Aurora snapshot export to Amazon S3.
  link: [export DB cluster snapshot data to an Amazon S3 bucket](../facts/aurora.md#aurora-export-snapshot-to-s3-background)
  link: [doesn't affect the performance](../facts/aurora.md#aurora-export-snapshot-to-s3-background)
aurora-export-snapshot-to-s3-for-long-term
  claim: For very long-term backups, AWS recommends exporting snapshot data to Amazon S3.
  scope: Aurora snapshot export to Amazon S3.
  link: [exporting snapshot data to Amazon S3](../facts/aurora.md#aurora-export-snapshot-to-s3-for-long-term)
  link: [very long-term backups](../facts/aurora.md#aurora-export-snapshot-to-s3-for-long-term)
aurora-failover-new-primary-by-promoting-or-creating
  claim: If the primary DB instance fails, Aurora automatically fails over to a new primary DB instance by either promoting an existing Aurora Replica or creating a new primary DB instance.
  scope: Aurora DB cluster failover within one Region.
  link: [promoting an existing Aurora Replica](../facts/aurora.md#aurora-failover-new-primary-by-promoting-or-creating)
  link: [creating a new primary DB instance](../facts/aurora.md#aurora-failover-new-primary-by-promoting-or-creating)
aurora-failover-read-write-fail-with-exception
  claim: During an Aurora failover to a replica there is a brief interruption during which read and write operations fail with an exception.
  scope: Aurora DB cluster failover within one Region.
  link: [read and write operations fail with an exception](../facts/aurora.md#aurora-failover-read-write-fail-with-exception)
  link: [brief interruption](../facts/aurora.md#aurora-failover-read-write-fail-with-exception)
aurora-failover-time-with-replica-guide
  claim: When the cluster has Aurora Replicas and the primary fails, service is typically restored in less than 60 seconds, and often in less than 30 seconds.
  scope: per Aurora DB cluster with at least one Aurora Replica; typical value; a replica is promoted to primary.
  link: [less than 60 seconds](../facts/aurora.md#aurora-failover-time-with-replica-guide)
  link: [less than 30 seconds](../facts/aurora.md#aurora-failover-time-with-replica-guide)
  say: under a minute | under thirty seconds
aurora-failover-time-without-replica
  claim: When the cluster has no Aurora Replicas, Aurora recreates the primary instance in the same AZ, and service is restored when the new primary instance is created, which typically takes less than 10 minutes.
  scope: per Aurora DB cluster with a single DB instance; typical value; the primary instance is recreated in the same AZ.
  link: [less than 10 minutes](../facts/aurora.md#aurora-failover-time-without-replica)
  say: under ten minutes
aurora-faq-add-1-to-15-replicas-three-azs
  claim: To increase availability you can create 1 to 15 replicas in any of three AZs, and Aurora automatically includes them in failover primary selection.
  scope: per cluster; maximum; in any of three AZs.
  link: [1 to 15 replicas](../facts/aurora.md#aurora-faq-add-1-to-15-replicas-three-azs)
aurora-faq-automated-backups-always-on
  claim: Automated continuous backups are always enabled on Aurora DB instances, with no database performance impact.
  scope: per Aurora DB instance.
  link: [always enabled](../facts/aurora.md#aurora-faq-automated-backups-always-on)
aurora-faq-babelfish-sql-server
  claim: Babelfish for Aurora PostgreSQL lets applications written for SQL Server work without code changes.
  scope: SQL Server migrations to Aurora PostgreSQL.
  link: [Babelfish for Aurora PostgreSQL](../facts/aurora.md#aurora-faq-babelfish-sql-server)
aurora-faq-binlog-cross-region-lag-unbounded
  claim: Binlog-based logical replication lag across Regions can grow indefinitely depending on the change/apply rate and network delays, although under typical conditions under a minute of lag is common.
  scope: per cross-Region binlog replica; typical lag is under a minute.
  link: [can grow indefinitely](../facts/aurora.md#aurora-faq-binlog-cross-region-lag-unbounded)
aurora-faq-binlog-external-mysql
  claim: You can set up binlog replication between an Aurora MySQL instance and an external MySQL database, which can run on Amazon RDS, self-managed on AWS, or outside AWS.
  scope: Aurora MySQL binary log (binlog) replication.
  link: [an external MySQL database](../facts/aurora.md#aurora-faq-binlog-external-mysql)
aurora-faq-blue-green-costs-about-double
  claim: While a blue/green deployment exists you pay approximately 2x the cost of running workloads on db.instances, because green instances cost the same as blue instances.
  scope: per blue/green deployment lifespan.
  link: [approximately 2x the cost](../facts/aurora.md#aurora-faq-blue-green-costs-about-double)
aurora-faq-blue-green-no-cross-region-replicas-or-rollback
  claim: Blue/green deployments do not currently support cross-Region read replicas or rollback.
  scope: RDS blue/green deployments; stated as not currently supported.
  link: [cross-Region read replicas or rollback](../facts/aurora.md#aurora-faq-blue-green-no-cross-region-replicas-or-rollback)
aurora-faq-blue-green-supports-global-database
  claim: Amazon RDS blue/green deployments support Aurora Global Database.
  scope: Aurora Blue/Green Deployments.
  link: [support Aurora Global Database](../facts/aurora.md#aurora-faq-blue-green-supports-global-database)
aurora-faq-blue-green-switchover-blocks-writes
  claim: During a blue/green switchover, writes are blocked on both environments until the green environment catches up, which ensures zero data loss.
  scope: per switchover.
  link: [writes are blocked on both environments](../facts/aurora.md#aurora-faq-blue-green-switchover-blocks-writes)
aurora-faq-blue-green-use-cases
  claim: Blue/green deployments are ideal for major or minor version upgrades, operating system updates, schema changes and parameter changes; the blue environment is current production and the green environment is staging that becomes the new production after switchover.
  scope: Aurora Blue/Green Deployments.
  link: [blue environment is your current production](../facts/aurora.md#aurora-faq-blue-green-use-cases)
aurora-faq-cannot-encrypt-existing-instance
  claim: Encrypting an existing unencrypted Aurora instance is not currently supported; to encrypt an existing database, create a new encrypted DB instance and migrate your data into it.
  scope: per existing unencrypted instance; FAQ states it as not currently supported.
  link: [not currently supported](../facts/aurora.md#aurora-faq-cannot-encrypt-existing-instance)
aurora-faq-cluster-endpoint-promotes-replica
  claim: When Aurora detects a problem with the primary instance it triggers a failover, and if you use the cluster endpoint a replica is promoted to primary.
  scope: per failover; application uses the cluster endpoint.
  link: [automatically detect a problem with your primary instance](../facts/aurora.md#aurora-faq-cluster-endpoint-promotes-replica)
aurora-faq-compute-scaling-limitless
  claim: Aurora PostgreSQL Limitless Database automatically scales compute horizontally for high-scale applications that need more write throughput or storage than a single instance provides.
  scope: ways to scale Aurora compute.
  link: [Automatically scales compute horizontally](../facts/aurora.md#aurora-faq-compute-scaling-limitless)
aurora-faq-compute-scaling-manual
  claim: With manual scaling you select the desired DB instance type, and the change applies during your maintenance window or immediately with the Apply Immediately flag.
  scope: per DB instance type change.
  link: [Apply Immediately flag](../facts/aurora.md#aurora-faq-compute-scaling-manual)
aurora-faq-compute-scaling-serverless
  claim: One of three ways to scale Aurora compute is Aurora serverless, an on-demand, autoscaling configuration that adjusts database compute based on application demand within a capacity range you specify.
  scope: ways to scale Aurora compute.
  link: [on-demand, autoscaling configuration](../facts/aurora.md#aurora-faq-compute-scaling-serverless)
aurora-faq-crash-restart-under-60s
  claim: After a crash Aurora does not replay the redo log from the last checkpoint, which reduces database restart times to less than 60 seconds in most cases.
  scope: per database restart; in most cases.
  link: [less than 60 seconds](../facts/aurora.md#aurora-faq-crash-restart-under-60s)
aurora-faq-cross-region-cluster-15-replicas-tens-of-ms
  claim: You can add up to 15 replicas on each cross-Region Aurora cluster; they share the same underlying storage as the cross-Region replica and typically lag behind the primary by tens of milliseconds.
  scope: per cross-Region Aurora cluster; maximum; lag is typical.
  link: [up to 15 replicas](../facts/aurora.md#aurora-faq-cross-region-cluster-15-replicas-tens-of-ms)
  link: [tens of milliseconds](../facts/aurora.md#aurora-faq-cross-region-cluster-15-replicas-tens-of-ms)
aurora-faq-cross-region-dr-manual-process
  claim: In this FAQ answer, disaster recovery across Regions is described as a manual process in which you promote a secondary Region to take read/write workloads.
  scope: cross-Region disaster recovery; stated in the failover answer; another FAQ answer names a managed Global Database failover operation.
  link: [a manual process](../facts/aurora.md#aurora-faq-cross-region-dr-manual-process)
aurora-faq-cross-region-physical-or-logical
  claim: You can set up Aurora cross-Region replicas using either physical replication (Aurora Global Database) or logical replication.
  scope: Aurora cross-Region replication and Aurora Global Database (FAQ); the FAQ recommends Global Database for low-latency global reads and disaster recovery.
  link: [either physical or logical replication](../facts/aurora.md#aurora-faq-cross-region-physical-or-logical)
aurora-faq-cross-region-recommend-global-db
  claim: For low-latency global reads and disaster recovery, the FAQ recommends using Aurora Global Database.
  scope: Aurora cross-Region replication and Aurora Global Database (FAQ).
  link: [we recommend using Amazon Aurora Global Database](../facts/aurora.md#aurora-faq-cross-region-recommend-global-db)
aurora-faq-data-api-free-tier-1-million
  claim: The Data API includes a free tier of 1 million requests per month, aggregated across all Regions, for the first year.
  scope: per month, aggregated across all Regions; first year only.
  link: [1 million requests per month](../facts/aurora.md#aurora-faq-data-api-free-tier-1-million)
aurora-faq-data-api-http-no-drivers-no-pools-no-vpc
  claim: The Data API is an HTTP-based API that eliminates the need to deploy database drivers, manage connection pools, or configure VPC networking.
  scope: RDS Data API for Aurora.
  link: [HTTP-based API](../facts/aurora.md#aurora-faq-data-api-http-no-drivers-no-pools-no-vpc)
aurora-faq-data-api-iam-and-secrets-manager
  claim: Administrators give a user permission to use the Data API by attaching an IAM policy, and a Data API call can pass the DB cluster credentials by using a secret in AWS Secrets Manager.
  scope: RDS Data API for Aurora.
  link: [Identity and Access Management (IAM) policy](../facts/aurora.md#aurora-faq-data-api-iam-and-secrets-manager)
  link: [a secret in AWS Secrets Manager](../facts/aurora.md#aurora-faq-data-api-iam-and-secrets-manager)
aurora-faq-data-api-pools-connections
  claim: The Data API automatically pools and shares database connections for better scalability and supports Aurora Global Database writer instances.
  scope: RDS Data API for Aurora.
  link: [automatically pools and shares database connections](../facts/aurora.md#aurora-faq-data-api-pools-connections)
aurora-faq-data-api-use-drivers-when
  claim: Use database drivers instead of the Data API when an existing application is highly coupled with database drivers, when there are long-running queries, or when you need features such as temporary tables or session variables.
  scope: RDS Data API for Aurora.
  link: [when there are long-running queries](../facts/aurora.md#aurora-faq-data-api-use-drivers-when)
aurora-faq-data-api-when-to-use
  claim: Use the Data API for new modern applications, particularly those built with AWS Lambda that access Aurora in a request/response model.
  scope: RDS Data API for Aurora.
  link: [particularly those built with AWS Lambda](../facts/aurora.md#aurora-faq-data-api-when-to-use)
aurora-faq-database-port-access
  claim: Aurora databases must be accessed through the database port entered on database creation.
  scope: per database.
  link: [the database port entered on database creation](../facts/aurora.md#aurora-faq-database-port-access)
aurora-faq-database-savings-plan-35-percent
  claim: A Database Savings Plan for Aurora usage can reduce costs by up to 35% when you commit to a consistent amount of usage over a 1-year term.
  scope: per Savings Plan commitment; maximum; consistent usage commitment.
  link: [up to 35%](../facts/aurora.md#aurora-faq-database-savings-plan-35-percent)
  link: [1-year term](../facts/aurora.md#aurora-faq-database-savings-plan-35-percent)
aurora-faq-delete-keeps-manual-snapshots
  claim: After you delete an Aurora DB instance, Aurora retains the final user-created DB snapshot and all other manually created DB snapshots.
  scope: per deleted DB instance; a final snapshot exists only if you choose to create one.
  link: [retains this final user-created DB Snapshot](../facts/aurora.md#aurora-faq-delete-keeps-manual-snapshots)
aurora-faq-encryption-at-rest-kms
  claim: You can encrypt Aurora databases at rest using keys you manage through AWS Key Management Service (AWS KMS).
  scope: Aurora encryption at rest with AWS KMS.
  link: [AWS Key Management Service (AWS KMS)](../facts/aurora.md#aurora-faq-encryption-at-rest-kms)
aurora-faq-encryption-covers-backups-replicas
  claim: When encryption is enabled, data at rest in the underlying storage is encrypted, along with automated backups, snapshots and replicas in the same cluster.
  scope: per cluster; encryption is enabled.
  link: [automated backups, snapshots, and replicas](../facts/aurora.md#aurora-faq-encryption-covers-backups-replicas)
aurora-faq-encryption-in-transit-ssl
  claim: Aurora uses SSL (AES-256) to secure connections between the database instance and your application.
  scope: connections between the DB instance and the application.
  link: [SSL (AES-256)](../facts/aurora.md#aurora-faq-encryption-in-transit-ssl)
aurora-faq-failover-cname-within-30s
  claim: With replicas, Aurora flips the canonical name record (CNAME) to point at the healthy replica, which is promoted to new primary, and failover typically completes within 30 seconds.
  scope: per failover, cluster with replicas; typical, not a guarantee.
  link: [within 30 seconds](../facts/aurora.md#aurora-faq-failover-cname-within-30s)
aurora-faq-free-tier-aurora-postgresql-serverless
  claim: Aurora PostgreSQL provides 4 ACUs and 1 GiB of storage per cluster on the Free plan.
  scope: per cluster, Free plan; Aurora PostgreSQL.
  link: [4 ACUs](../facts/aurora.md#aurora-faq-free-tier-aurora-postgresql-serverless)
  link: [1 GiB of storage per cluster](../facts/aurora.md#aurora-faq-free-tier-aurora-postgresql-serverless)
aurora-faq-global-db-10-secondary-regions
  claim: An Aurora Global Database can have up to 10 secondary Regions.
  scope: per Aurora Global Database; maximum; the same FAQ page still shows an older five-Region figure in the cross-Region replicas answer.
  link: [up to 10 secondary Regions](../facts/aurora.md#aurora-faq-global-db-10-secondary-regions)
aurora-faq-global-db-activity-streams-supported
  claim: You can use database activity streams with Aurora Global Database.
  scope: Aurora cross-Region replication and Aurora Global Database (FAQ); to analyze activity, the FAQ suggests advanced auditing, general logs and slow query logs instead.
  link: [Yes](../facts/aurora.md#aurora-faq-global-db-activity-streams-supported)
aurora-faq-global-db-both-engines
  claim: Aurora Global Database is available for both Aurora MySQL and Aurora PostgreSQL.
  scope: Aurora cross-Region replication and Aurora Global Database (FAQ).
  link: [both Aurora MySQL and Aurora PostgreSQL](../facts/aurora.md#aurora-faq-global-db-both-engines)
aurora-faq-global-db-definition
  claim: Aurora Global Database allows a single Aurora database to span multiple AWS Regions, and it provides disaster recovery from region-wide outages.
  scope: Aurora cross-Region replication and Aurora Global Database (FAQ).
  link: [span multiple AWS Regions](../facts/aurora.md#aurora-faq-global-db-definition)
aurora-faq-global-db-mixed-io-configurations
  claim: In an Aurora Global Database you can configure the primary Region as Aurora I/O-Optimized and the secondary Regions as Aurora Standard, or the reverse.
  scope: between primary and secondary Regions.
  link: [Aurora Standard or the reverse](../facts/aurora.md#aurora-faq-global-db-mixed-io-configurations)
aurora-faq-global-db-no-code-change-writer-endpoint
  claim: If the primary Region becomes unavailable you do not need to update application code: you can use the managed cross-Region Global Database failover operation, and the Global Database writer endpoint avoids the need for application code changes.
  scope: per Global Database failover; uses the Global Database writer endpoint.
  link: [avoid the need to make application code changes](../facts/aurora.md#aurora-faq-global-db-no-code-change-writer-endpoint)
aurora-faq-global-db-physical-lag-under-one-second
  claim: Cross-Region replicas that use Aurora Global Database physical replication have a typical lag of under a second.
  scope: per secondary Region; typical.
  link: [under a second](../facts/aurora.md#aurora-faq-global-db-physical-lag-under-one-second)
aurora-faq-guardduty-rds-protection
  claim: GuardDuty RDS Protection profiles and monitors login activity using tailored ML models to detect suspicious logins to Aurora databases.
  scope: Amazon Aurora (FAQ).
  link: [GuardDuty RDS Protection](../facts/aurora.md#aurora-faq-guardduty-rds-protection)
aurora-faq-hipaa-eligible
  claim: Both the MySQL- and PostgreSQL-compatible editions of Aurora are HIPAA eligible.
  scope: Amazon Aurora (FAQ).
  link: [HIPAA eligible](../facts/aurora.md#aurora-faq-hipaa-eligible)
aurora-faq-io-optimized-backup-prices-unchanged
  claim: Aurora I/O-Optimized does not change the price of backtrack, snapshot, export or continuous backup.
  scope: Aurora billing (FAQ).
  link: [no changes to the price of backtrack](../facts/aurora.md#aurora-faq-io-optimized-backup-prices-unchanged)
aurora-faq-io-optimized-cross-region-replication-io-still-charged
  claim: With Aurora I/O-Optimized, the charges for I/O operations required to replicate data across Regions continue to apply.
  scope: cross-Region replication.
  link: [continue to apply](../facts/aurora.md#aurora-faq-io-optimized-cross-region-replication-io-still-charged)
aurora-faq-io-optimized-fits-io-intensive-workloads
  claim: Aurora I/O-Optimized delivers improved price performance for I/O-intensive applications that need high write throughput or run analytical queries processing large amounts of data.
  scope: Aurora billing (FAQ).
  link: [improved price performance for I/O-intensive applications](../facts/aurora.md#aurora-faq-io-optimized-fits-io-intensive-workloads)
aurora-faq-io-optimized-works-with-reserved-instances
  claim: Aurora I/O-Optimized works with existing Aurora Reserved Instances, and Aurora automatically accounts for the price difference between Aurora Standard and Aurora I/O-Optimized.
  scope: Aurora billing (FAQ).
  link: [works with existing Aurora Reserved Instances](../facts/aurora.md#aurora-faq-io-optimized-works-with-reserved-instances)
aurora-faq-limitless-availability-99-99
  claim: Aurora PostgreSQL Limitless Database supports up to 99.99% availability with configurable compute redundancy, which you enable by setting compute redundancy greater than zero.
  scope: Aurora PostgreSQL Limitless Database; maximum; compute redundancy set greater than zero.
  link: [up to 99.99% availability](../facts/aurora.md#aurora-faq-limitless-availability-99-99)
aurora-faq-limitless-beyond-256-tib
  claim: For workloads that need to scale beyond 256 TiB, Aurora PostgreSQL Limitless Database provides automated horizontal scaling.
  scope: Aurora PostgreSQL Limitless Database.
  link: [beyond 256 TiB](../facts/aurora.md#aurora-faq-limitless-beyond-256-tib)
aurora-faq-limitless-requires-io-optimized-pg-16-4
  claim: Aurora PostgreSQL Limitless Database is available for the Aurora I/O-Optimized cluster configuration starting with PostgreSQL 16.4 compatibility.
  scope: Aurora PostgreSQL Limitless Database; minimum; Aurora I/O-Optimized cluster configuration.
  link: [PostgreSQL 16.4 compatibility](../facts/aurora.md#aurora-faq-limitless-requires-io-optimized-pg-16-4)
aurora-faq-limitless-three-table-types
  claim: Aurora PostgreSQL Limitless Database supports three table types: sharded, reference and standard.
  scope: Aurora PostgreSQL Limitless Database.
  link: [sharded, reference, and standard](../facts/aurora.md#aurora-faq-limitless-three-table-types)
aurora-faq-limitless-when-to-use
  claim: Use Aurora PostgreSQL Limitless Database for applications that need to scale horizontally and require more write throughput or data storage capacity than a single Aurora database instance supports.
  scope: Aurora PostgreSQL Limitless Database.
  link: [scale horizontally](../facts/aurora.md#aurora-faq-limitless-when-to-use)
aurora-faq-low-priority-replica-still-promoted-if-needed
  claim: You can assign lower priority tiers to replicas you do not want promoted, but if the higher priority replicas are unhealthy or unavailable, Amazon RDS promotes the lower priority replica.
  scope: per failover; higher priority replicas are unhealthy or unavailable.
  link: [will promote the lower priority replica](../facts/aurora.md#aurora-faq-low-priority-replica-still-promoted-if-needed)
aurora-faq-migration-dms-continuous-replication
  claim: For large-scale MySQL migrations with minimal downtime, AWS DMS supports continuous replication while the source database remains operational.
  scope: migration into Aurora.
  link: [AWS Database Migration Service (AWS DMS)](../facts/aurora.md#aurora-faq-migration-dms-continuous-replication)
aurora-faq-monitoring-database-insights-vs-devops-guru
  claim: CloudWatch Database Insights monitors Aurora resources in real time with customizable dashboards, pre-built alarms and fleet-level monitoring, while DevOps Guru uses ML to analyze metrics over time, detect anomalies and offer insights and recommendations.
  scope: Amazon Aurora (FAQ).
  link: [monitors Aurora resources in real time](../facts/aurora.md#aurora-faq-monitoring-database-insights-vs-devops-guru)
  link: [uses ML to analyze metrics over time](../facts/aurora.md#aurora-faq-monitoring-database-insights-vs-devops-guru)
aurora-faq-mysql-migration-mysqldump
  claim: The most straightforward way to migrate between MySQL and Aurora is the standard MySQL utilities mysqldump to export and mysqlimport to import, and the same tools work in reverse for migration back to MySQL.
  scope: migration into Aurora.
  link: [mysqldump to export data from MySQL](../facts/aurora.md#aurora-faq-mysql-migration-mysqldump)
aurora-faq-mysql-migration-snapshot-from-rds
  claim: You can use the Amazon RDS DB snapshot migration feature to migrate an Amazon RDS for MySQL DB snapshot directly to Aurora through the Amazon RDS console.
  scope: RDS for MySQL.
  link: [Amazon RDS DB snapshot migration feature](../facts/aurora.md#aurora-faq-mysql-migration-snapshot-from-rds)
aurora-faq-mysql-up-to-6x-throughput
  claim: Aurora delivers up to 6x the throughput of stock MySQL by tightly integrating the database engine with an SSD-based virtualized storage layer built for database workloads.
  scope: Aurora MySQL compared with stock MySQL; maximum.
  link: [up to 6x the throughput of stock MySQL](../facts/aurora.md#aurora-faq-mysql-up-to-6x-throughput)
aurora-faq-no-automatic-snapshot-sharing
  claim: Automatic sharing of Aurora DB snapshots is not supported; to share a snapshot you must manually create a copy and then share the copy.
  scope: per snapshot.
  link: [Automatic sharing of DB snapshots is not supported](../facts/aurora.md#aurora-faq-no-automatic-snapshot-sharing)
aurora-faq-no-special-drivers
  claim: Aurora does not require special drivers: it works with standard MySQL and PostgreSQL database drivers, with no modifications required.
  scope: Amazon Aurora (FAQ).
  link: [standard MySQL and PostgreSQL database drivers](../facts/aurora.md#aurora-faq-no-special-drivers)
aurora-faq-open-source-compatibility
  claim: Aurora PostgreSQL and Aurora MySQL offer full open source compatibility, so existing code, applications, drivers and tools can be used with little or no modification.
  scope: Aurora PostgreSQL and Aurora MySQL.
  link: [little or no modification](../facts/aurora.md#aurora-faq-open-source-compatibility)
aurora-faq-optimized-reads-8x-latency-30-percent
  claim: Optimized reads for Aurora PostgreSQL delivers up to 8x improved query latency and up to 30% cost savings compared to instances without it.
  scope: Aurora PostgreSQL instances with optimized reads; maximum; compared with instances without it.
  link: [up to 8x improved query latency](../facts/aurora.md#aurora-faq-optimized-reads-8x-latency-30-percent)
  link: [up to 30% cost savings](../facts/aurora.md#aurora-faq-optimized-reads-8x-latency-30-percent)
aurora-faq-optimized-reads-instances-not-serverless
  claim: The Aurora FAQ says Optimized Reads is not available on Aurora serverless, and names Intel-based R6id and Graviton-based R6gd and R8gd instances as instances where it is available; a later What's New post also names M8gd instances with Optimized Reads for Aurora PostgreSQL.
  scope: Aurora PostgreSQL Optimized Reads.
  link: [not available on Aurora serverless](../facts/aurora.md#aurora-faq-optimized-reads-instances-not-serverless)
  link: [R6id and Graviton-based R6gd and R8gd instances](../facts/aurora.md#aurora-faq-optimized-reads-instances-not-serverless)
aurora-faq-optimized-reads-no-extra-charge
  claim: Optimized reads for Aurora PostgreSQL has no additional charge beyond the price of Intel-based R6id and Graviton-based R6gd and R8gd instances.
  scope: Aurora PostgreSQL Optimized Reads.
  link: [no additional charges for optimized reads](../facts/aurora.md#aurora-faq-optimized-reads-no-extra-charge)
aurora-faq-parallel-query-not-data-warehouse
  claim: Parallel Query is ideal for operational analytics on fresh data in large tables, but it is not a data warehouse replacement; for exabyte-scale analytics consider Amazon Redshift.
  scope: Aurora MySQL parallel query.
  link: [not a data warehouse replacement](../facts/aurora.md#aurora-faq-parallel-query-not-data-warehouse)
aurora-faq-parallel-query-pushdown
  claim: Parallel Query for Aurora MySQL pushes down and distributes the computational load of a single query across thousands of CPUs in Aurora's storage layer, speeding up analytical queries by up to two orders of magnitude.
  scope: Aurora MySQL analytical queries; maximum.
  link: [up to two orders of magnitude](../facts/aurora.md#aurora-faq-parallel-query-pushdown)
aurora-faq-pay-for-one-copy
  claim: Aurora replicates data across three Availability Zones but you only pay for one copy.
  scope: per database storage.
  link: [you only pay for one copy](../facts/aurora.md#aurora-faq-pay-for-one-copy)
aurora-faq-pitr-latest-five-minutes
  claim: The latest restorable time for an Aurora point-in-time restore can be up to five minutes in the past.
  scope: per point-in-time restore operation; maximum; restores to a new instance.
  link: [up to five minutes in the past](../facts/aurora.md#aurora-faq-pitr-latest-five-minutes)
aurora-faq-postgresql-migration-snapshot-from-rds
  claim: You can use the RDS DB snapshot migration feature to migrate an Amazon RDS for PostgreSQL DB snapshot directly to Aurora through the Amazon RDS console.
  scope: RDS for PostgreSQL.
  link: [RDS DB snapshot migration feature](../facts/aurora.md#aurora-faq-postgresql-migration-snapshot-from-rds)
aurora-faq-postgresql-up-to-6x-throughput
  claim: Aurora delivers up to 6x the throughput of stock PostgreSQL by tightly integrating the database engine with an SSD-based virtualized storage layer built for database workloads.
  scope: Aurora PostgreSQL compared with stock PostgreSQL; maximum.
  link: [up to 6x the throughput of stock PostgreSQL](../facts/aurora.md#aurora-faq-postgresql-up-to-6x-throughput)
aurora-faq-priority-change-no-failover
  claim: You can modify Aurora promotion priority tiers at any time without triggering a failover.
  scope: per instance priority tier.
  link: [without triggering a failover](../facts/aurora.md#aurora-faq-priority-change-no-failover)
aurora-faq-promote-binlog-replica-few-minutes
  claim: For logical (binlog) replication, promoting a cross-Region replica typically takes a few minutes depending on your workload.
  scope: per promotion; typical; depends on workload.
  link: [a few minutes](../facts/aurora.md#aurora-faq-promote-binlog-replica-few-minutes)
aurora-faq-promotion-highest-priority-first
  claim: You can assign a promotion priority tier to each instance of a cluster, and when the primary fails Amazon RDS promotes the replica with the highest priority.
  scope: per instance in a cluster.
  link: [promotion priority tier](../facts/aurora.md#aurora-faq-promotion-highest-priority-first)
aurora-faq-promotion-tie-largest-wins
  claim: If two or more Aurora replicas share the same promotion priority, Amazon RDS promotes the largest one.
  scope: per failover; two or more replicas with the same priority.
  link: [promotes the largest one](../facts/aurora.md#aurora-faq-promotion-tie-largest-wins)
aurora-faq-rds-proxy-failover-66-percent
  claim: For faster failovers, Amazon RDS Proxy connects to the failover instance while preserving application connections, reducing failover times by up to 66%.
  scope: per failover; maximum; application connects through RDS Proxy.
  link: [up to 66%](../facts/aurora.md#aurora-faq-rds-proxy-failover-66-percent)
aurora-faq-read-io-one-per-page
  claim: Every database page read operation counts as one I/O in Aurora.
  scope: per page read.
  link: [counts as one I/O](../facts/aurora.md#aurora-faq-read-io-one-per-page)
aurora-faq-read-io-page-size
  claim: Pages not in memory incur read I/O charges, at 16 KB per page in Aurora MySQL and 8 KB in Aurora PostgreSQL.
  scope: per page not in memory; fixed; pages served from memory or cache are not charged.
  link: [16 KB per page in Aurora MySQL](../facts/aurora.md#aurora-faq-read-io-page-size)
  link: [8 KB in Aurora PostgreSQL](../facts/aurora.md#aurora-faq-read-io-page-size)
aurora-faq-replica-lag-tens-of-ms-same-region
  claim: Because Aurora replicas share the same data volume as the primary instance in the same AWS Region, there is virtually no replication lag; lag times are typically in the tens of milliseconds.
  scope: per replica, same Region; typical.
  link: [tens of milliseconds](../facts/aurora.md#aurora-faq-replica-lag-tens-of-ms-same-region)
aurora-faq-replicas-promoted-without-data-loss
  claim: Any Aurora replica can be promoted to primary without any data loss, which enhances fault tolerance.
  scope: per replica promotion.
  link: [without any data loss](../facts/aurora.md#aurora-faq-replicas-promoted-without-data-loss)
aurora-faq-replication-not-charged
  claim: There is no separate charge for Aurora replication because it is bundled into the price; you are charged on the storage your database consumes at the database layer, not the virtualized storage layer.
  scope: Aurora billing (FAQ).
  link: [Aurora replication is bundled into the price](../facts/aurora.md#aurora-faq-replication-not-charged)
aurora-faq-runs-in-vpc-full-control
  claim: Creating Aurora DB instances in a VPC gives you complete control over who can access your Aurora databases, including defining virtual network topologies that closely resemble traditional on-premises networks.
  scope: Aurora DB clusters in a VPC.
  link: [complete control over who can access](../facts/aurora.md#aurora-faq-runs-in-vpc-full-control)
  link: [closely resemble traditional on-premises networks](../facts/aurora.md#aurora-faq-runs-in-vpc-full-control)
aurora-faq-segments-six-copies
  claim: Aurora divides the database volume into 10 GiB segments, and each segment is replicated six ways across three Availability Zones.
  scope: per database volume segment; fixed.
  link: [10 GiB](../facts/aurora.md#aurora-faq-segments-six-copies)
  link: [six ways](../facts/aurora.md#aurora-faq-segments-six-copies)
  link: [three Availability Zones](../facts/aurora.md#aurora-faq-segments-six-copies)
aurora-faq-shared-snapshot-same-region-only
  claim: Shared Aurora snapshots are accessible only within the same AWS Region, and encrypted Aurora snapshots can also be shared.
  scope: per shared snapshot.
  link: [accessible only within the same AWS Region](../facts/aurora.md#aurora-faq-shared-snapshot-same-region-only)
aurora-faq-single-instance-new-instance-same-az
  claim: For a single instance with no replicas, Aurora attempts to create a new DB instance in the same AZ as the original instance on a best-effort basis.
  scope: cluster without replicas; may not succeed if an issue broadly affects the AZ.
  link: [on a best-effort basis](../facts/aurora.md#aurora-faq-single-instance-new-instance-same-az)
aurora-faq-snapshot-restore-new-instance
  claim: Restoring data from an Aurora snapshot requires the creation of a new DB instance.
  scope: per snapshot restore.
  link: [requires the creation of a new DB Instance](../facts/aurora.md#aurora-faq-snapshot-restore-new-instance)
aurora-faq-standard-pay-per-io-vs-io-optimized-included
  claim: With Aurora Standard you pay per request for I/O, while with Aurora I/O-Optimized read and write I/O operations are included at no additional charge.
  scope: per cluster configuration.
  link: [you pay per-request for I/O](../facts/aurora.md#aurora-faq-standard-pay-per-io-vs-io-optimized-included)
  link: [included at no additional charge](../facts/aurora.md#aurora-faq-standard-pay-per-io-vs-io-optimized-included)
aurora-faq-storage-scales-to-256-tib
  claim: Aurora's storage system automatically scales up to 256 TiB per database instance and replicates the data across three Availability Zones.
  scope: per database instance; maximum.
  link: [256 TiB](../facts/aurora.md#aurora-faq-storage-scales-to-256-tib)
  link: [three Availability Zones](../facts/aurora.md#aurora-faq-storage-scales-to-256-tib)
aurora-faq-tolerates-three-copies-lost-read
  claim: Aurora is designed to handle the loss of up to three copies of data without affecting read availability.
  scope: per database volume; maximum; transparent handling.
  link: [up to three copies](../facts/aurora.md#aurora-faq-tolerates-three-copies-lost-read)
aurora-faq-tolerates-two-copies-lost-write
  claim: Aurora is designed to handle the loss of up to two copies of data without affecting database write availability.
  scope: per database volume; maximum; transparent handling.
  link: [up to two copies](../facts/aurora.md#aurora-faq-tolerates-two-copies-lost-write)
aurora-faq-up-to-15-read-replicas
  claim: With Aurora PostgreSQL and MySQL you get up to 15 low-latency read replicas, point-in-time recovery, and continuous backup to Amazon S3.
  scope: per cluster, Aurora PostgreSQL and Aurora MySQL; maximum.
  link: [up to 15 low-latency read replicas](../facts/aurora.md#aurora-faq-up-to-15-read-replicas)
aurora-faq-vpc-supported
  claim: Aurora DB instances can be created in a VPC, which gives you control over who can access your Aurora databases.
  scope: Aurora DB clusters in a VPC.
  link: [can be created in a VPC](../facts/aurora.md#aurora-faq-vpc-supported)
aurora-faq-what-is-aurora
  claim: Amazon Aurora is a fully managed relational database service designed for high performance and availability at global scale for PostgreSQL, MySQL, and DSQL.
  scope: Amazon Aurora (FAQ).
  link: [fully managed relational database service](../facts/aurora.md#aurora-faq-what-is-aurora)
aurora-faq-write-io-4-kb-units
  claim: Aurora write I/Os are counted in 4 KB units, and only redo log records (Aurora MySQL) or write-ahead log records (Aurora PostgreSQL) are written.
  scope: per write I/O; fixed.
  link: [4 KB units](../facts/aurora.md#aurora-faq-write-io-4-kb-units)
aurora-faq-zero-etl-no-charge-for-processing
  claim: Ongoing processing of data changes by Aurora zero-ETL integration is offered at no additional charge, but you pay for existing resources used to create and process the change data.
  scope: Aurora zero-ETL integrations.
  link: [offered at no additional charge](../facts/aurora.md#aurora-faq-zero-etl-no-charge-for-processing)
aurora-faq-zero-etl-redshift-when
  claim: Use the Aurora zero-ETL integration with Amazon Redshift when you need near real-time access to transactional data for analytics.
  scope: Aurora zero-ETL integrations.
  link: [near real-time access to transactional data for analytics](../facts/aurora.md#aurora-faq-zero-etl-redshift-when)
aurora-faq-zero-etl-targets-no-charge
  claim: Aurora zero-ETL integrations have two targets, Amazon Redshift and Amazon SageMaker Lakehouse, and ongoing processing of data changes is offered at no additional charge.
  scope: Aurora zero-ETL integrations.
  link: [Amazon Redshift](../facts/aurora.md#aurora-faq-zero-etl-targets-no-charge)
  link: [no additional charge](../facts/aurora.md#aurora-faq-zero-etl-targets-no-charge)
aurora-final-snapshot-does-not-expire-retained-backups-do
  claim: Unlike a retained automated backup, a final snapshot does not expire, so AWS strongly suggests taking a final snapshot even if you retain automated backups.
  scope: retained automated backups and the final snapshot of a deleted Aurora DB cluster.
  link: [a final snapshot doesn't expire](../facts/aurora.md#aurora-final-snapshot-does-not-expire-retained-backups-do)
  link: [Unlike a retained automated backup](../facts/aurora.md#aurora-final-snapshot-does-not-expire-retained-backups-do)
aurora-free-plan-postgresql-serverless-4-acu-1-gib
  claim: The AWS Free Plan gives access to Aurora PostgreSQL serverless instances with up to 4 ACUs and 1 GiB of storage per cluster, and you can upgrade to the Paid plan at any time to scale up to 256 ACUs and 256 TiB of storage.
  scope: per Aurora PostgreSQL serverless cluster on the Free Plan; maximum.
  link: [up to 4 ACUs](../facts/aurora.md#aurora-free-plan-postgresql-serverless-4-acu-1-gib)
  link: [1 GiB of storage per cluster](../facts/aurora.md#aurora-free-plan-postgresql-serverless-4-acu-1-gib)
  say: up to four ACUs | one gibibyte of storage
aurora-free-tier-limit-clusters-and-instances
  claim: The Aurora PostgreSQL Free Tier allows a maximum of 2 clusters and 2 instances per account.
  scope: per AWS account, Aurora PostgreSQL on the AWS Free Tier; maximum; not adjustable.
  link: [Maximum 2 clusters and 2 instances per account](../facts/aurora.md#aurora-free-tier-limit-clusters-and-instances)
aurora-free-tier-no-global-database-no-zero-etl
  claim: Aurora Global Database and zero-ETL integrations are not supported on the Aurora PostgreSQL Free Tier.
  scope: Aurora PostgreSQL on the AWS Free Tier.
  link: [Zero-ETL integrations are not supported](../facts/aurora.md#aurora-free-tier-no-global-database-no-zero-etl)
aurora-free-tier-postgresql-express-config-only
  claim: On the AWS Free Tier, only Aurora PostgreSQL clusters created with express configuration are supported; full configuration is not available.
  scope: Aurora PostgreSQL on the AWS Free Tier.
  link: [created with express configuration](../facts/aurora.md#aurora-free-tier-postgresql-express-config-only)
aurora-frequent-connections-use-rds-proxy
  claim: If applications frequently open and close connections, or keep a large number of long-lived connections open, AWS recommends using Amazon RDS Proxy.
  scope: Aurora performance best practices.
  link: [we recommend that you use Amazon RDS Proxy](../facts/aurora.md#aurora-frequent-connections-use-rds-proxy)
  link: [frequently open and close connections](../facts/aurora.md#aurora-frequent-connections-use-rds-proxy)
aurora-global-database-async-replication-secondary
  claim: Aurora asynchronously replicates all data and updates from the primary AWS Region to each of the secondary Regions of a global database.
  scope: Aurora Global Database.
  link: [asynchronously replicates all data and updates](../facts/aurora.md#aurora-global-database-async-replication-secondary)
  link: [to each of the secondary Regions](../facts/aurora.md#aurora-global-database-async-replication-secondary)
aurora-global-database-multi-region-ha
  claim: Each Aurora global database spans multiple AWS Regions, enabling low latency global reads and disaster recovery from outages across an AWS Region.
  scope: Aurora Global Database.
  link: [spans multiple AWS Regions](../facts/aurora.md#aurora-global-database-multi-region-ha)
  link: [low latency global reads and disaster recovery](../facts/aurora.md#aurora-global-database-multi-region-ha)
aurora-global-db-arc-region-switch
  claim: ARC Region Switch, which integrates with Aurora Global Database, orchestrates failover steps across AWS accounts and Regions, provides real-time recovery dashboards, and generates compliance reports.
  scope: Aurora Global Database.
  link: [orchestrates failover steps across AWS accounts and Regions](../facts/aurora.md#aurora-global-db-arc-region-switch)
  link: [real-time recovery dashboards](../facts/aurora.md#aurora-global-db-arc-region-switch)
aurora-global-db-auto-synchronizes-primary-to-secondary
  claim: In Aurora Global Database, Aurora automatically synchronizes all changes made in the primary DB cluster to one or more secondary clusters.
  scope: Aurora Global Database.
  link: [automatically synchronizes all changes](../facts/aurora.md#aurora-global-db-auto-synchronizes-primary-to-secondary)
  link: [one or more secondary clusters](../facts/aurora.md#aurora-global-db-auto-synchronizes-primary-to-secondary)
aurora-global-db-cannot-rename-member-cluster
  claim: You cannot rename a Regional Aurora DB cluster while it is a member of an Aurora global database.
  scope: Aurora Global Database.
  link: [can't rename a Regional Aurora DB cluster](../facts/aurora.md#aurora-global-db-cannot-rename-member-cluster)
  link: [member of an Aurora global database](../facts/aurora.md#aurora-global-db-cannot-rename-member-cluster)
aurora-global-db-cluster-endpoint-must-change-if-not-global-writer
  claim: If application connections use the cluster endpoint of the old primary cluster instead of the global writer endpoint, change the connection settings to use the cluster endpoint of the new primary cluster.
  scope: Aurora Global Database writer endpoint.
  link: [cluster endpoint of the new primary cluster](../facts/aurora.md#aurora-global-db-cluster-endpoint-must-change-if-not-global-writer)
  link: [instead of the global writer endpoint](../facts/aurora.md#aurora-global-db-cluster-endpoint-must-change-if-not-global-writer)
aurora-global-db-detach-secondary-standalone-readwrite
  claim: Removing a secondary DB cluster from an Aurora global database immediately stops replication from the primary to that secondary and promotes it to a standalone provisioned Aurora DB cluster with full read/write capabilities.
  scope: Aurora Global Database.
  link: [immediately stops the replication](../facts/aurora.md#aurora-global-db-detach-secondary-standalone-readwrite)
  link: [standalone provisioned Aurora DB cluster](../facts/aurora.md#aurora-global-db-detach-secondary-standalone-readwrite)
aurora-global-db-failback-via-switchover
  claim: After the original topology is restored, you can fail back to the original primary Region by performing a switchover operation.
  scope: Aurora Global Database switchover (planned).
  link: [fail back your global database](../facts/aurora.md#aurora-global-db-failback-via-switchover)
  link: [performing a switchover operation](../facts/aurora.md#aurora-global-db-failback-via-switchover)
aurora-global-db-failover-after-primary-region-outage
  claim: To recover an Aurora Global Database after an outage in the primary Region, use the failover mechanism.
  scope: Aurora Global Database failover (unplanned outage).
  link: [after an outage in the primary Region](../facts/aurora.md#aurora-global-db-failover-after-primary-region-outage)
  link: [use the failover mechanism](../facts/aurora.md#aurora-global-db-failover-after-primary-region-outage)
aurora-global-db-failover-can-lose-writes-consistent-state
  claim: Both failover methods can result in a loss of write transaction data that was not replicated to the chosen secondary before the failover event occurred.
  scope: Aurora Global Database failover (unplanned outage).
  link: [loss of write transaction data that wasn't replicated](../facts/aurora.md#aurora-global-db-failover-can-lose-writes-consistent-state)
  link: [Both failover methods can result](../facts/aurora.md#aurora-global-db-failover-can-lose-writes-consistent-state)
aurora-global-db-failover-choose-least-lag-secondary
  claim: Choosing the secondary Region with the least replication lag can minimize data loss during a failover from a failed primary Region.
  scope: Aurora Global Database failover (unplanned outage).
  link: [secondary Region with the least replication lag](../facts/aurora.md#aurora-global-db-failover-choose-least-lag-secondary)
  link: [minimize data loss](../facts/aurora.md#aurora-global-db-failover-choose-least-lag-secondary)
aurora-global-db-failover-cross-region-to-secondary
  claim: With the failover approach, you perform a cross-Region failover to one of the secondary DB clusters in your Aurora global database.
  scope: Aurora Global Database failover (unplanned outage).
  link: [cross-Region failover](../facts/aurora.md#aurora-global-db-failover-cross-region-to-secondary)
  link: [perform a cross-Region failover](../facts/aurora.md#aurora-global-db-failover-cross-region-to-secondary)
aurora-global-db-failover-new-volume-snapshot-old-primary
  claim: To ensure consistent data, Aurora creates a new storage volume for the old primary Region after it recovers, and first attempts to take a snapshot of the old storage volume at the point of failure.
  scope: Aurora Global Database failover (unplanned outage).
  link: [creates a new storage volume](../facts/aurora.md#aurora-global-db-failover-new-volume-snapshot-old-primary)
  link: [snapshot of the old storage volume](../facts/aurora.md#aurora-global-db-failover-new-volume-snapshot-old-primary)
aurora-global-db-failover-use-for-unplanned-outage
  claim: Use the Aurora Global Database failover approach to recover from an unplanned outage.
  scope: Aurora Global Database failover (unplanned outage).
  link: [recover from an unplanned outage](../facts/aurora.md#aurora-global-db-failover-use-for-unplanned-outage)
  link: [Failover](../facts/aurora.md#aurora-global-db-failover-use-for-unplanned-outage)
aurora-global-db-failover-use-global-writer-endpoint-low-ttl
  claim: Before a failover, make sure that applications that connect to the primary DB cluster use the global writer endpoint. If you use the global writer endpoint and your application or networking layers cache DNS values, reduce the DNS cache TTL to a low value such as 5 seconds.
  scope: Aurora Global Database failover (unplanned outage); the TTL step applies when the application or networking layers cache DNS values.
  link: [using the global writer endpoint](../facts/aurora.md#aurora-global-db-failover-use-global-writer-endpoint-low-ttl)
  link: [low value such as 5 seconds](../facts/aurora.md#aurora-global-db-failover-use-global-writer-endpoint-low-ttl)
aurora-global-db-global-writer-single-readwrite-endpoint
  claim: The global writer is the single read/write endpoint that always points to the current writer DB instance for the global database cluster.
  scope: Aurora Global Database writer endpoint.
  link: [always points to the current writer DB instance](../facts/aurora.md#aurora-global-db-global-writer-single-readwrite-endpoint)
  link: [single read/write endpoint](../facts/aurora.md#aurora-global-db-global-writer-single-readwrite-endpoint)
aurora-global-db-interop-same-privileges-in-every-region
  claim: Using a global database with other AWS services such as Amazon S3 and AWS Lambda requires that all Aurora DB clusters in the global database have the same privileges, external functions, and so on in the respective AWS Regions.
  scope: Aurora Global Database.
  link: [same privileges, external functions, and so on](../facts/aurora.md#aurora-global-db-interop-same-privileges-in-every-region)
  link: [all Aurora DB clusters in your global database](../facts/aurora.md#aurora-global-db-interop-same-privileges-in-every-region)
aurora-global-db-lower-rto-rpo-than-traditional-replication
  claim: The secondary clusters of an Aurora Global Database let you make it available in a new primary AWS Region more quickly (lower RTO) and with less data loss (lower RPO) than traditional replication solutions.
  scope: Aurora Global Database.
  link: [more quickly (lower RTO)](../facts/aurora.md#aurora-global-db-lower-rto-rpo-than-traditional-replication)
  link: [less data loss (lower RPO)](../facts/aurora.md#aurora-global-db-lower-rto-rpo-than-traditional-replication)
aurora-global-db-managed-failover-no-wait-async
  claim: Managed failover does not wait for data to synchronize between the chosen secondary Region and the current primary Region, and because replication is asynchronous, not all transactions may have reached the secondary before it is promoted.
  scope: Aurora Global Database failover (unplanned outage).
  link: [doesn't wait for data to synchronize](../facts/aurora.md#aurora-global-db-managed-failover-no-wait-async)
  link: [chosen secondary Region and the current primary Region](../facts/aurora.md#aurora-global-db-managed-failover-no-wait-async)
aurora-global-db-managed-failover-readds-old-primary
  claim: With managed failover, Aurora automatically adds the old primary Region back to the global database as a secondary Region when it becomes available again.
  scope: Aurora Global Database failover (unplanned outage).
  link: [automatically adds back the old primary Region](../facts/aurora.md#aurora-global-db-managed-failover-readds-old-primary)
aurora-global-db-managed-failover-recommended-for-dr
  claim: Managed failover is the method recommended for disaster recovery of an Aurora global database.
  scope: Aurora Global Database failover (unplanned outage).
  link: [method is recommended for disaster recovery](../facts/aurora.md#aurora-global-db-managed-failover-recommended-for-dr)
  link: [Managed failover](../facts/aurora.md#aurora-global-db-managed-failover-recommended-for-dr)
aurora-global-db-manual-failover-choose-least-lag
  claim: In a manual failover, if the global database has two or more secondary AWS Regions, choose the secondary cluster that has the least replication lag.
  scope: Aurora Global Database failover (unplanned outage).
  link: [the least replication lag](../facts/aurora.md#aurora-global-db-manual-failover-choose-least-lag)
  link: [two or more secondary AWS Regions](../facts/aurora.md#aurora-global-db-manual-failover-choose-least-lag)
aurora-global-db-manual-failover-when-managed-unavailable
  claim: A manual failover is an alternative to managed failover, for example when the primary and secondary DB clusters are not running compatible engine versions.
  scope: Aurora Global Database failover (unplanned outage).
  link: [aren't running compatible engine versions](../facts/aurora.md#aurora-global-db-manual-failover-when-managed-unavailable)
  link: [use the managed failover process](../facts/aurora.md#aurora-global-db-manual-failover-when-managed-unavailable)
aurora-global-db-multiple-clusters-multiple-regions
  claim: With Amazon Aurora Global Database, you set up multiple Aurora DB clusters that span multiple AWS Regions.
  scope: Aurora Global Database.
  link: [span multiple AWS Regions](../facts/aurora.md#aurora-global-db-multiple-clusters-multiple-regions)
  link: [Amazon Aurora Global Database](../facts/aurora.md#aurora-global-db-multiple-clusters-multiple-regions)
aurora-global-db-no-auto-minor-upgrade
  claim: Automatic minor version upgrade does not apply to Aurora MySQL and Aurora PostgreSQL clusters that are part of a global database.
  scope: Aurora Global Database.
  link: [doesn't apply to Aurora MySQL and Aurora PostgreSQL](../facts/aurora.md#aurora-global-db-no-auto-minor-upgrade)
  link: [part of a global database](../facts/aurora.md#aurora-global-db-no-auto-minor-upgrade)
aurora-global-db-no-binlog-management
  claim: With an Aurora global database you do not need to configure or manage Aurora MySQL binlog (binary logging) replication.
  scope: Aurora Global Database.
  link: [don't need to configure or manage](../facts/aurora.md#aurora-global-db-no-binlog-management)
  link: [binlog (binary logging) replication](../facts/aurora.md#aurora-global-db-no-binlog-management)
aurora-global-db-no-individual-stop-start
  claim: You cannot stop or start the Aurora DB clusters in a global database individually.
  scope: Aurora Global Database.
  link: [can't stop or start the Aurora DB clusters](../facts/aurora.md#aurora-global-db-no-individual-stop-start)
  link: [global database individually](../facts/aurora.md#aurora-global-db-no-individual-stop-start)
aurora-global-db-no-two-clusters-same-region
  claim: No two Aurora DB clusters in an Aurora global database can be in the same AWS Region.
  scope: Aurora Global Database.
  link: [no two Aurora DB clusters](../facts/aurora.md#aurora-global-db-no-two-clusters-same-region)
  link: [same AWS Region](../facts/aurora.md#aurora-global-db-no-two-clusters-same-region)
aurora-global-db-occasional-writes-use-secondary-reader-with-write-forwarding
  claim: For occasional DML statements such as maintenance and data cleanup, connect to the reader endpoint of a secondary cluster that has write forwarding enabled.
  scope: write forwarding in an Aurora global database.
  link: [has write forwarding enabled](../facts/aurora.md#aurora-global-db-occasional-writes-use-secondary-reader-with-write-forwarding)
  link: [occasional DML statements](../facts/aurora.md#aurora-global-db-occasional-writes-use-secondary-reader-with-write-forwarding)
aurora-global-db-only-primary-writes
  claim: In an Aurora global database, only the primary cluster performs write operations.
  scope: Aurora Global Database.
  link: [Only the primary cluster performs write operations](../facts/aurora.md#aurora-global-db-only-primary-writes)
  link: [primary cluster](../facts/aurora.md#aurora-global-db-only-primary-writes)
aurora-global-db-only-specific-versions-regions
  claim: Only specific versions of the Aurora MySQL and Aurora PostgreSQL database engines in certain AWS Regions support Aurora Global Database.
  scope: Aurora Global Database.
  link: [Only specific versions](../facts/aurora.md#aurora-global-db-only-specific-versions-regions)
  link: [in certain AWS Regions](../facts/aurora.md#aurora-global-db-only-specific-versions-regions)
aurora-global-db-plan-faster-recovery-regional-disasters
  claim: By using Aurora Global Database, you can plan for faster recovery from rare, unplanned Regional disasters or complete service-level outages.
  scope: Aurora Global Database.
  link: [faster recovery from rare, unplanned Regional disasters](../facts/aurora.md#aurora-global-db-plan-faster-recovery-regional-disasters)
  link: [complete service-level outages](../facts/aurora.md#aurora-global-db-plan-faster-recovery-regional-disasters)
aurora-global-db-postgres-rds-replica-primary-no-secondary
  claim: If the primary DB cluster of a global database is based on a replica of an Amazon RDS PostgreSQL instance, you cannot create a secondary cluster.
  scope: Aurora Global Database.
  link: [a replica of an Amazon RDS PostgreSQL instance](../facts/aurora.md#aurora-global-db-postgres-rds-replica-primary-no-secondary)
  link: [can't create a secondary cluster](../facts/aurora.md#aurora-global-db-postgres-rds-replica-primary-no-secondary)
aurora-global-db-postgres-rpo-managed-by-parameter
  claim: With an Aurora PostgreSQL-based global database, you can manage the recovery point objective (RPO) by using the rds.global_db_rpo parameter.
  scope: Aurora PostgreSQL-based global database, managed RPO (rds.global_db_rpo).
  link: [manage the recovery point objective (RPO)](../facts/aurora.md#aurora-global-db-postgres-rpo-managed-by-parameter)
  link: [`rds.global_db_rpo` parameter](../facts/aurora.md#aurora-global-db-postgres-rpo-managed-by-parameter)
aurora-global-db-postgres-rpo-parameter-affects-primary
  claim: With an Aurora PostgreSQL-based global database, the rds.global_db_rpo parameter sets and tracks the upper bound on RPO, but doing so might affect transaction processing on the primary cluster's writer node.
  scope: Aurora PostgreSQL-based global database, managed RPO (rds.global_db_rpo).
  link: [`rds.global_db_rpo` parameter](../facts/aurora.md#aurora-global-db-postgres-rpo-parameter-affects-primary)
  link: [might affect transaction processing](../facts/aurora.md#aurora-global-db-postgres-rpo-parameter-affects-primary)
aurora-global-db-primary-region-one-writer
  claim: The primary AWS Region of an Aurora global database supports an Aurora DB cluster that has one writer Aurora DB instance.
  scope: Aurora Global Database.
  link: [one writer Aurora DB instance](../facts/aurora.md#aurora-global-db-primary-region-one-writer)
  link: [The primary AWS Region supports](../facts/aurora.md#aurora-global-db-primary-region-one-writer)
aurora-global-db-product-page-promote-secondary-for-readwrite
  claim: If the primary Region suffers a performance degradation or outage, you can promote one of the secondary Regions to take read/write responsibilities.
  scope: Aurora Global Database.
  link: [take read/write responsibilities](../facts/aurora.md#aurora-global-db-product-page-promote-secondary-for-readwrite)
  link: [primary Region suffers a performance degradation or outage](../facts/aurora.md#aurora-global-db-product-page-promote-secondary-for-readwrite)
aurora-global-db-product-page-spans-regions-no-performance-impact
  claim: Amazon Aurora Global Database is designed for globally distributed applications, allowing a single Amazon Aurora database to span multiple AWS Regions.
  scope: Aurora Global Database.
  link: [designed for globally distributed applications](../facts/aurora.md#aurora-global-db-product-page-spans-regions-no-performance-impact)
  link: [span multiple AWS Regions](../facts/aurora.md#aurora-global-db-product-page-spans-regions-no-performance-impact)
aurora-global-db-product-page-storage-based-replication-dedicated
  claim: Aurora Global Database uses storage-based replication with typical latency of less than 1 second, using dedicated infrastructure that leaves the database fully available to serve application workloads.
  scope: Aurora Global Database.
  link: [storage-based replication](../facts/aurora.md#aurora-global-db-product-page-storage-based-replication-dedicated)
  link: [dedicated infrastructure that leaves your database fully available](../facts/aurora.md#aurora-global-db-product-page-storage-based-replication-dedicated)
aurora-global-db-rds-proxy-any-cluster
  claim: You can use RDS Proxy with any DB cluster in an Aurora global database.
  scope: RDS Proxy with Aurora Global Database.
  link: [any DB cluster in an Aurora global database](../facts/aurora.md#aurora-global-db-rds-proxy-any-cluster)
aurora-global-db-rds-proxy-redirect-writes-after-role-switch
  claim: After a global database switchover or failover, you must redirect the application's write operations to the read/write endpoint of the proxy that is associated with the new primary cluster.
  scope: RDS Proxy with Aurora Global Database; after a switchover or failover.
  link: [redirect your application's write operations](../facts/aurora.md#aurora-global-db-rds-proxy-redirect-writes-after-role-switch)
aurora-global-db-replication-little-primary-performance-impact
  claim: The replication performed by Aurora Global Database has little performance impact on the primary DB cluster.
  scope: Aurora Global Database.
  link: [little performance impact on the primary DB cluster](../facts/aurora.md#aurora-global-db-replication-little-primary-performance-impact)
  link: [replication performed by Aurora Global Database](../facts/aurora.md#aurora-global-db-replication-little-primary-performance-impact)
aurora-global-db-replication-uses-storage-not-engine
  claim: Aurora Global Database uses the cluster storage volume, not the database engine, for fast, low-overhead replication.
  scope: Aurora Global Database.
  link: [cluster storage volume and not the database engine](../facts/aurora.md#aurora-global-db-replication-uses-storage-not-engine)
  link: [fast, low-overhead replication](../facts/aurora.md#aurora-global-db-replication-uses-storage-not-engine)
aurora-global-db-rpo-blocks-commits-when-all-secondaries-behind
  claim: If all secondary clusters are behind the target RPO, Aurora pauses transactions on the primary cluster until at least one secondary cluster catches up.
  scope: Aurora PostgreSQL-based global database, managed RPO (rds.global_db_rpo).
  link: [Aurora pauses transactions on the primary cluster](../facts/aurora.md#aurora-global-db-rpo-blocks-commits-when-all-secondaries-behind)
  link: [secondary clusters catches up](../facts/aurora.md#aurora-global-db-rpo-blocks-commits-when-all-secondaries-behind)
aurora-global-db-rpo-definition-data-loss-in-time
  claim: Recovery point objective (RPO) is the amount of data that can be lost, measured in time, after a disaster or service outage.
  scope: disaster recovery terms as the Aurora Global Database guide defines them.
  link: [amount of data that can be lost](../facts/aurora.md#aurora-global-db-rpo-definition-data-loss-in-time)
  link: [after a disaster or service outage](../facts/aurora.md#aurora-global-db-rpo-definition-data-loss-in-time)
aurora-global-db-rpo-parameter-dynamic
  claim: The rds.global_db_rpo parameter is dynamic, so you can reset it quickly if you do not want write transactions to stall until the lag decreases.
  scope: Aurora PostgreSQL-based global database, managed RPO (rds.global_db_rpo).
  link: [`rds.global_db_rpo` parameter is dynamic](../facts/aurora.md#aurora-global-db-rpo-parameter-dynamic)
  link: [The `rds.global_db_rpo` parameter is dynamic](../facts/aurora.md#aurora-global-db-rpo-parameter-dynamic)
aurora-global-db-rto-definition-measures-downtime
  claim: Recovery time objective (RTO) is the time it takes a system to return to a working state after a disaster or service outage.
  scope: disaster recovery terms as the Aurora Global Database guide defines them.
  link: [return to a working state](../facts/aurora.md#aurora-global-db-rto-definition-measures-downtime)
  link: [after a disaster or service outage](../facts/aurora.md#aurora-global-db-rto-definition-measures-downtime)
aurora-global-db-same-engine-version-for-managed-switchover
  claim: You can perform managed cross-Region switchovers or failovers with Aurora Global Database only if the primary and secondary DB clusters have the same major and minor engine versions.
  scope: Aurora Global Database.
  link: [same major and minor engine versions](../facts/aurora.md#aurora-global-db-same-engine-version-for-managed-switchover)
  link: [managed cross-Region switchovers or failovers](../facts/aurora.md#aurora-global-db-same-engine-version-for-managed-switchover)
aurora-global-db-scale-reads-connect-to-nearby-reader-endpoint
  claim: To scale read-only requests in the same or nearby AWS Region as your application, connect to the reader endpoint of the primary or secondary Aurora clusters of a global database.
  scope: Aurora Global Database.
  link: [connect to the reader endpoint](../facts/aurora.md#aurora-global-db-scale-reads-connect-to-nearby-reader-endpoint)
  link: [same or nearby AWS Region as your application](../facts/aurora.md#aurora-global-db-scale-reads-connect-to-nearby-reader-endpoint)
aurora-global-db-scale-secondary-readers-serverless
  claim: You can scale up each secondary cluster of an Aurora global database independently by adding Aurora reader instances to serve read-only workloads, and you can use Aurora serverless for the reader instances.
  scope: Aurora Global Database.
  link: [scale up each secondary cluster independently](../facts/aurora.md#aurora-global-db-scale-secondary-readers-serverless)
  link: [adding one or more Aurora reader instances](../facts/aurora.md#aurora-global-db-scale-secondary-readers-serverless)
aurora-global-db-secondary-read-replicas-stay-available-lag-grows
  claim: On supported engine versions, secondary Region read replicas remain available for application requests during unplanned events, although the replication lag may continue to increase until the event is resolved.
  scope: Aurora Global Database.
  link: [read replicas remain available for your application requests](../facts/aurora.md#aurora-global-db-secondary-read-replicas-stay-available-lag-grows)
  link: [replication lag may continue to increase](../facts/aurora.md#aurora-global-db-secondary-read-replicas-stay-available-lag-grows)
aurora-global-db-secondary-readers-restart-with-primary-writer
  claim: If the primary Region's writer DB instance restarts or fails over, reader DB instances in secondary Regions also restart, and the secondary cluster is unavailable until all its readers are back in sync.
  scope: Aurora Global Database.
  link: [reader DB instances in secondary Regions also restart](../facts/aurora.md#aurora-global-db-secondary-readers-restart-with-primary-writer)
  link: [undergoes a restart or failover](../facts/aurora.md#aurora-global-db-secondary-readers-restart-with-primary-writer)
aurora-global-db-secondary-region-readers-only
  claim: A secondary AWS Region of an Aurora global database runs a read-only Aurora DB cluster made up entirely of Aurora Replicas.
  scope: Aurora Global Database.
  link: [made up entirely of Aurora Replicas](../facts/aurora.md#aurora-global-db-secondary-region-readers-only)
  link: [A secondary AWS Region runs](../facts/aurora.md#aurora-global-db-secondary-region-readers-only)
aurora-global-db-secondary-same-engine-version-recommended
  claim: AWS recommends creating secondary DB clusters for a global database with the same version of the Aurora DB engine as the primary.
  scope: Aurora Global Database.
  link: [same version of the Aurora DB engine](../facts/aurora.md#aurora-global-db-secondary-same-engine-version-recommended)
  link: [create secondary DB clusters](../facts/aurora.md#aurora-global-db-secondary-same-engine-version-recommended)
aurora-global-db-secrets-manager-not-supported
  claim: Secrets Manager does not support Aurora Global Database, so you must first turn off Secrets Manager integration for the DB instance when you add a Region to a global database.
  scope: Aurora Global Database.
  link: [Secrets Manager doesn't support Aurora Global Database](../facts/aurora.md#aurora-global-db-secrets-manager-not-supported)
  link: [turn off Secrets Manager integration](../facts/aurora.md#aurora-global-db-secrets-manager-not-supported)
aurora-global-db-set-up-write-privileges-ahead-of-promotion
  claim: Because a read-only secondary cluster can be promoted to primary, AWS recommends setting up write privileges ahead of time on all Aurora DB clusters for any services you plan to use with the global database.
  scope: Aurora Global Database.
  link: [set up write privileges ahead of time](../facts/aurora.md#aurora-global-db-set-up-write-privileges-ahead-of-promotion)
  link: [can be promoted to the role of primary](../facts/aurora.md#aurora-global-db-set-up-write-privileges-ahead-of-promotion)
aurora-global-db-spans-at-least-two-regions
  claim: An Aurora global database spans at least two AWS Regions.
  scope: Aurora Global Database.
  link: [spans at least two AWS Regions](../facts/aurora.md#aurora-global-db-spans-at-least-two-regions)
  link: [at least two AWS Regions](../facts/aurora.md#aurora-global-db-spans-at-least-two-regions)
aurora-global-db-switchover-controlled-scenarios
  claim: Use switchover for controlled scenarios, such as operational maintenance and other planned operational procedures where all the Aurora clusters and other services they interact with are in a healthy state.
  scope: Aurora Global Database switchover (planned).
  link: [controlled scenarios, such as operational maintenance](../facts/aurora.md#aurora-global-db-switchover-controlled-scenarios)
  link: [planned operational procedures](../facts/aurora.md#aurora-global-db-switchover-controlled-scenarios)
aurora-global-db-switchover-healthy-only-unplanned-use-failover
  claim: Switchovers are designed for an Aurora global database where all the Aurora clusters and other services they interact with are in a healthy state.
  scope: Aurora Global Database switchover (planned).
  link: [in a healthy state](../facts/aurora.md#aurora-global-db-switchover-healthy-only-unplanned-use-failover)
  link: [Switchovers are designed to be used](../facts/aurora.md#aurora-global-db-switchover-healthy-only-unplanned-use-failover)
aurora-global-db-switchover-keeps-topology
  claim: The switchover mechanism maintains the global database's existing replication topology, with the same number of Aurora clusters in the same Regions.
  scope: Aurora Global Database switchover (planned).
  link: [maintains your global database's existing replication topology](../facts/aurora.md#aurora-global-db-switchover-keeps-topology)
  link: [same number of Aurora clusters](../facts/aurora.md#aurora-global-db-switchover-keeps-topology)
aurora-global-db-switchover-planned-no-data-loss
  claim: Switchover lets you relocate the primary cluster of a healthy Aurora Global Database to one of its secondary Regions with no data loss.
  scope: Aurora Global Database switchover (planned).
  link: [relocate the primary cluster](../facts/aurora.md#aurora-global-db-switchover-planned-no-data-loss)
  link: [with no data loss](../facts/aurora.md#aurora-global-db-switchover-planned-no-data-loss)
aurora-global-db-switchover-short-unavailability
  claim: During a Global Database switchover, the database is unavailable for a short time while the primary and selected secondary clusters assume their new roles.
  scope: Aurora Global Database switchover (planned).
  link: [unavailable for a short time](../facts/aurora.md#aurora-global-db-switchover-short-unavailability)
  link: [assume their new roles](../facts/aurora.md#aurora-global-db-switchover-short-unavailability)
aurora-global-db-switchover-use-case-fail-back
  claim: One use of switchover is as a zero-data-loss method to fail back to the original primary Region after a failover.
  scope: Aurora Global Database switchover (planned).
  link: [zero-data-loss method to fail back](../facts/aurora.md#aurora-global-db-switchover-use-case-fail-back)
  link: [original primary Region after a failover](../facts/aurora.md#aurora-global-db-switchover-use-case-fail-back)
aurora-global-db-switchover-waits-for-sync
  claim: Before Aurora starts a switchover, it waits for the target secondary Region clusters to be fully synchronized with the primary Region cluster.
  scope: Aurora Global Database switchover (planned).
  link: [waits for the target secondary Region clusters](../facts/aurora.md#aurora-global-db-switchover-waits-for-sync)
  link: [fully synchronized with the primary Region cluster](../facts/aurora.md#aurora-global-db-switchover-waits-for-sync)
aurora-global-db-two-region-keep-default-rpo-secondary
  claim: In a global database with only two AWS Regions, AWS recommends keeping the rds.global_db_rpo parameter's default value in the secondary Region's parameter group.
  scope: Aurora PostgreSQL-based global database, managed RPO (rds.global_db_rpo).
  link: [keeping the `rds.global_db_rpo` parameter's default value](../facts/aurora.md#aurora-global-db-two-region-keep-default-rpo-secondary)
  link: [only two AWS Regions](../facts/aurora.md#aurora-global-db-two-region-keep-default-rpo-secondary)
aurora-global-db-unplanned-outage-replication-stops
  claim: During an unexpected outage in the primary Region of an Aurora global database, the primary cluster and its writer node are not available, and replication between the primary and secondary DB clusters stops.
  scope: Aurora Global Database failover (unplanned outage).
  link: [its writer node aren't available](../facts/aurora.md#aurora-global-db-unplanned-outage-replication-stops)
  link: [secondary DB clusters stops](../facts/aurora.md#aurora-global-db-unplanned-outage-replication-stops)
aurora-global-db-write-fencing-best-effort-split-brain
  claim: Because fencing writes is a best-effort attempt, writes might be momentarily accepted in the old primary Region, causing split-brain issues.
  scope: Aurora Global Database failover (unplanned outage).
  link: [fencing writes is a best-effort attempt](../facts/aurora.md#aurora-global-db-write-fencing-best-effort-split-brain)
  link: [causing split-brain issues](../facts/aurora.md#aurora-global-db-write-fencing-best-effort-split-brain)
aurora-global-db-write-forwarding-auto-forwards-to-primary
  claim: With write forwarding, Aurora automatically forwards write statements from a secondary cluster to the writer in the primary Region of the Aurora Global Database.
  scope: write forwarding in an Aurora global database.
  link: [automatically forwards the write statements to the writer](../facts/aurora.md#aurora-global-db-write-forwarding-auto-forwards-to-primary)
  link: [primary Region of your Aurora Global Database](../facts/aurora.md#aurora-global-db-write-forwarding-auto-forwards-to-primary)
aurora-global-db-write-forwarding-reconnect-after-failover
  claim: With write forwarding, after a cross-Region failover or switchover you must update your application code or configuration to connect to the newly promoted primary Region's reader endpoint.
  scope: write forwarding in an Aurora global database.
  link: [update your application code or configuration](../facts/aurora.md#aurora-global-db-write-forwarding-reconnect-after-failover)
  link: [newly promoted primary Region's reader endpoint](../facts/aurora.md#aurora-global-db-write-forwarding-reconnect-after-failover)
aurora-global-db-write-forwarding-unsupported-operations
  claim: Write forwarding does not support certain MySQL or PostgreSQL operations, such as data definition language (DDL) changes or SELECT FOR UPDATE statements.
  scope: write forwarding in an Aurora global database.
  link: [doesn't support certain MySQL or PostgreSQL operations](../facts/aurora.md#aurora-global-db-write-forwarding-unsupported-operations)
  link: [data definition language (DDL) changes](../facts/aurora.md#aurora-global-db-write-forwarding-unsupported-operations)
aurora-global-db-writer-endpoint-auto-updated
  claim: Each Aurora Global Database comes with a writer endpoint that Aurora automatically updates to route requests to the current writer instance of the primary DB cluster.
  scope: Aurora Global Database writer endpoint.
  link: [writer endpoint that is automatically updated by Aurora](../facts/aurora.md#aurora-global-db-writer-endpoint-auto-updated)
  link: [current writer instance of the primary DB cluster](../facts/aurora.md#aurora-global-db-writer-endpoint-auto-updated)
aurora-global-db-writer-endpoint-cross-region-read-write
  claim: You can use the global writer endpoint to send cross-Region read/write requests to the writer.
  scope: Aurora Global Database writer endpoint.
  link: [send cross-Region read/write requests to your writer](../facts/aurora.md#aurora-global-db-writer-endpoint-cross-region-read-write)
  link: [use the global endpoint](../facts/aurora.md#aurora-global-db-writer-endpoint-cross-region-read-write)
aurora-global-db-writer-endpoint-for-dml-ddl-strong-consistency
  claim: Connect to the Aurora Global Database writer endpoint if you need to run DML and DDL statements, or if you need strong consistency between reads and writes.
  scope: Aurora Global Database writer endpoint.
  link: [strong consistency between reads and writes](../facts/aurora.md#aurora-global-db-writer-endpoint-for-dml-ddl-strong-consistency)
  link: [Connect to the Aurora Global Database writer endpoint](../facts/aurora.md#aurora-global-db-writer-endpoint-for-dml-ddl-strong-consistency)
aurora-global-db-writer-endpoint-name-changes-on-rename
  claim: If you rename an Aurora Global Database, the writer endpoint name changes, and any code that uses it must be updated with the new name.
  scope: Aurora Global Database writer endpoint.
  link: [the writer endpoint name changes](../facts/aurora.md#aurora-global-db-writer-endpoint-name-changes-on-rename)
  link: [must be updated with the new name](../facts/aurora.md#aurora-global-db-writer-endpoint-name-changes-on-rename)
aurora-global-db-writer-endpoint-no-app-change-after-switchover
  claim: If you use the Aurora Global Database writer endpoint, you do not need to change the connection settings in your application after a switchover.
  scope: Aurora Global Database writer endpoint.
  link: [don't need to change the connection settings](../facts/aurora.md#aurora-global-db-writer-endpoint-no-app-change-after-switchover)
  link: [Aurora Global Database writer endpoint](../facts/aurora.md#aurora-global-db-writer-endpoint-no-app-change-after-switchover)
aurora-global-db-writer-endpoint-no-connection-string-change
  claim: With the writer endpoint, you do not have to modify your connection string after you change the location of the primary Region using managed Aurora Global Database switchover and failover.
  scope: Aurora Global Database writer endpoint.
  link: [don't have to modify your connection string](../facts/aurora.md#aurora-global-db-writer-endpoint-no-connection-string-change)
  link: [change the location of the primary Region](../facts/aurora.md#aurora-global-db-writer-endpoint-no-connection-string-change)
aurora-global-db-writes-to-primary-via-writer-endpoint
  claim: You issue write operations to the primary DB cluster in the primary AWS Region, and the most convenient way is to use the global database writer endpoint, which always points to the primary DB cluster, even after a switchover or failover to a different Region.
  scope: Aurora Global Database writer endpoint.
  link: [always points to the primary DB cluster](../facts/aurora.md#aurora-global-db-writes-to-primary-via-writer-endpoint)
  link: [write operations to the primary DB cluster](../facts/aurora.md#aurora-global-db-writes-to-primary-via-writer-endpoint)
aurora-global-failover-rebuild-secondaries-minutes-to-hours
  claim: After a managed failover, rebuilding the other secondary Region clusters can take a few minutes to several hours, depending on the size of the storage volume and the distance between the Regions.
  scope: per Aurora global database managed failover.
  link: [a few minutes to several hours](../facts/aurora.md#aurora-global-failover-rebuild-secondaries-minutes-to-hours)
  say: from minutes to hours
aurora-global-failover-rpo-nonzero-seconds
  claim: The RPO of an Aurora Global Database failover from an unplanned outage is typically a non-zero value measured in seconds, depending on the replication lag at the time of the failure.
  scope: per Aurora global database failover.
  link: [non-zero value measured in seconds](../facts/aurora.md#aurora-global-failover-rpo-nonzero-seconds)
  say: a few seconds of possible data loss
aurora-global-headless-needs-instance-before-promotion
  claim: Before you can perform a switchover or failover to a headless secondary Aurora DB cluster, you must add a DB instance to it.
  scope: per headless secondary DB cluster of an Aurora global database.
  link: [you must add a DB instance to it](../facts/aurora.md#aurora-global-headless-needs-instance-before-promotion)
aurora-global-headless-secondary-no-compute-charge
  claim: A headless secondary Aurora DB cluster is one without a DB instance, and it can lower expenses for an Aurora global database: compute and storage are decoupled, so without the DB instance you are not charged for compute, only for storage.
  scope: per secondary DB cluster of an Aurora global database.
  link: [not charged for compute, only for storage](../facts/aurora.md#aurora-global-headless-secondary-no-compute-charge)
aurora-global-instance-class-memory-optimized
  claim: AWS recommends that an Aurora global database use a db.r5 or higher instance class.
  scope: per Aurora global database DB cluster.
  link: [db.r5 or higher instance class](../facts/aurora.md#aurora-global-instance-class-memory-optimized)
aurora-global-managed-failover-primary-role-few-minutes
  claim: After a managed failover in an Aurora global database, the chosen secondary cluster typically assumes the primary role within a few minutes.
  scope: per Aurora global database managed failover.
  link: [within a few minutes](../facts/aurora.md#aurora-global-managed-failover-primary-role-few-minutes)
  say: within a few minutes
aurora-global-mixed-provisioned-and-serverless-between-regions
  claim: An Aurora global database can use a mixed configuration of provisioned or serverless instance class types between the primary and secondary Regions.
  scope: per Aurora global database.
  link: [provisioned or serverless instance class types](../facts/aurora.md#aurora-global-mixed-provisioned-and-serverless-between-regions)
aurora-global-primary-max-readers-15-minus-secondary-regions
  claim: The maximum number of read-only instances allowed in the primary AWS Region of an Aurora global database, given the actual number of secondary Regions, is 15 minus s, where s is the total number of secondary AWS Regions.
  scope: per Aurora global database, primary AWS Region; maximum; not adjustable; s is the total number of secondary AWS Regions.
  link: [15 - s](../facts/aurora.md#aurora-global-primary-max-readers-15-minus-secondary-regions)
aurora-global-promote-secondary-under-1-minute
  claim: In the event of a Regional degradation or outage, one of the secondary Regions of an Aurora global database can be promoted to read and write capabilities in less than 1 minute.
  scope: per Aurora global database, promotion of a secondary Region; AWS marketing and FAQ wording; the user guide says RTO can be in the order of minutes.
  link: [less than 1 minute](../facts/aurora.md#aurora-global-promote-secondary-under-1-minute)
  say: under a minute
aurora-global-replication-latency-under-1-second
  claim: Aurora Global Database replicates data to the secondary Regions over dedicated infrastructure with latency typically under a second.
  scope: per Aurora global database, primary to secondary Regions; typical value; replication is asynchronous.
  link: [typically under a second](../facts/aurora.md#aurora-global-replication-latency-under-1-second)
  say: typically under one second
aurora-global-requires-memory-optimized-instance-class
  claim: An Aurora global database requires DB instance classes that are optimized for memory-intensive applications.
  scope: per Aurora global database DB cluster.
  link: [optimized for memory-intensive applications](../facts/aurora.md#aurora-global-requires-memory-optimized-instance-class)
aurora-global-rpo-1-second-rto-under-1-minute
  claim: AWS describes an effective recovery point objective (RPO) of 1 second and a recovery time objective (RTO) of less than 1 minute for an Aurora cluster that recovers from a Regional outage by promoting a secondary Region.
  scope: per Aurora global database, promotion of a secondary Region; product page wording.
  link: [RPO) of 1 second](../facts/aurora.md#aurora-global-rpo-1-second-rto-under-1-minute)
  link: [RTO) of less than 1 minute](../facts/aurora.md#aurora-global-rpo-1-second-rto-under-1-minute)
  say: one second | under a minute
aurora-global-rpo-parameter-range
  claim: For an Aurora PostgreSQL global database, valid values of the rds.global_db_rpo parameter range from 20 seconds to 2,147,483,647 seconds.
  scope: per Aurora PostgreSQL-based global database; minimum; adjustable.
  link: [20 seconds](../facts/aurora.md#aurora-global-rpo-parameter-range)
  say: twenty seconds
aurora-global-rpo-typically-seconds-guide
  claim: The Aurora User Guide says that for an Aurora global database, the recovery point objective (RPO) is typically measured in seconds.
  scope: per Aurora global database.
  link: [typically measured in seconds](../facts/aurora.md#aurora-global-rpo-typically-seconds-guide)
  say: typically measured in seconds
aurora-global-rto-order-of-minutes-guide
  claim: The Aurora User Guide says that for Aurora Global Database, the recovery time objective (RTO) can be in the order of minutes.
  scope: per Aurora global database.
  link: [in the order of minutes](../facts/aurora.md#aurora-global-rto-order-of-minutes-guide)
  say: in the order of minutes
aurora-global-secondary-cluster-max-16-reader-instances
  claim: The secondary cluster of an Aurora global database is read-only, so it can support up to 16 read-only DB instances rather than the usual limit of 15 for a single Aurora cluster.
  scope: per secondary DB cluster of an Aurora global database; maximum; not adjustable.
  link: [up to 16 read-only DB instances](../facts/aurora.md#aurora-global-secondary-cluster-max-16-reader-instances)
  link: [usual limit of 15](../facts/aurora.md#aurora-global-secondary-cluster-max-16-reader-instances)
  say: sixteen read-only instances | fifteen
aurora-global-secondary-each-in-different-region
  claim: You can create up to 10 secondary read-only Aurora DB clusters in an Aurora global database, and each must be in a different Region.
  scope: per Aurora global database; maximum.
  link: [each must be in a different Region](../facts/aurora.md#aurora-global-secondary-each-in-different-region)
aurora-global-secondary-regions-max-10
  claim: An Aurora global database can have up to 10 secondary AWS Regions. The limit was 5 secondary Regions before the May 2025 increase.
  scope: per Aurora global database; maximum; not adjustable; each secondary DB cluster must be in a different Region.
  link: [up to 10 secondary AWS Regions](../facts/aurora.md#aurora-global-secondary-regions-max-10)
  link: [up to 5 secondary Regions](../facts/aurora.md#aurora-global-secondary-regions-max-10)
  say: ten secondary Regions | five secondary Regions
  changed: 2025-05-21: was up to 5 secondary Regions
aurora-global-serverless-primary-min-capacity-8-acu
  claim: For a global database with Aurora Serverless, the minimum recommended capacity for the DB cluster in the primary AWS Region is 8 ACUs.
  scope: per primary DB cluster of an Aurora global database using Aurora Serverless; minimum; not adjustable; a recommendation, not an enforced minimum.
  link: [8 ACUs](../facts/aurora.md#aurora-global-serverless-primary-min-capacity-8-acu)
  say: eight ACUs
aurora-global-switchover-rpo-zero
  claim: A switchover of an Aurora global database synchronizes the secondary DB clusters with the primary before making any other changes, so the RPO is 0 (no data loss).
  scope: per Aurora global database switchover; for planned operations where all clusters are healthy.
  link: [RPO is 0 (no data loss)](../facts/aurora.md#aurora-global-switchover-rpo-zero)
  say: zero data loss
aurora-global-switchover-time-typically-under-30-seconds
  claim: Aurora Global Database cross-Region switchover reduces the recovery time for read/write operations to typically under 30 seconds on upgraded cluster versions.
  scope: per Aurora global database, cross-Region switchover; the cluster must be upgraded to a supported engine version.
  link: [typically under 30 seconds](../facts/aurora.md#aurora-global-switchover-time-typically-under-30-seconds)
  say: typically under thirty seconds
aurora-global-writer-endpoint-follows-switchover-failover
  claim: When a secondary cluster becomes the new primary cluster due to a switchover or failover, Aurora automatically switches the global database writer endpoint to point to the cluster endpoint of the new primary cluster, in the other AWS Region.
  scope: Aurora Global Database writer endpoint.
  link: [automatically switches this endpoint](../facts/aurora.md#aurora-global-writer-endpoint-follows-switchover-failover)
  link: [cluster endpoint of the new primary cluster](../facts/aurora.md#aurora-global-writer-endpoint-follows-switchover-failover)
aurora-global-writer-endpoint-same-purpose-as-cluster-endpoint
  claim: Aurora Global Database has a special kind of endpoint, the global database writer endpoint, that serves the same purpose as the cluster endpoint of a standalone Aurora cluster.
  scope: Aurora Global Database writer endpoint.
  link: [special kind of endpoint](../facts/aurora.md#aurora-global-writer-endpoint-same-purpose-as-cluster-endpoint)
  link: [same purpose as the cluster endpoint](../facts/aurora.md#aurora-global-writer-endpoint-same-purpose-as-cluster-endpoint)
aurora-ha-use-cluster-and-reader-endpoints
  claim: For clusters where high availability is important, use the cluster endpoint for read/write or general-purpose connections and the reader endpoint for read-only connections.
  scope: Aurora cluster (writer) endpoint.
  link: [cluster endpoint for read/write](../facts/aurora.md#aurora-ha-use-cluster-and-reader-endpoints)
  link: [reader endpoint for read-only connections](../facts/aurora.md#aurora-ha-use-cluster-and-reader-endpoints)
aurora-iam-db-auth-central-access-management
  claim: With IAM database authentication you can use IAM to centrally manage access to your database resources, instead of managing access individually on each DB cluster.
  scope: IAM database authentication for Aurora.
  link: [centrally manage access to your database resources](../facts/aurora.md#aurora-iam-db-auth-central-access-management)
  link: [instead of managing access individually](../facts/aurora.md#aurora-iam-db-auth-central-access-management)
aurora-iam-db-auth-engines
  claim: IAM database authentication works with Aurora MySQL and Aurora PostgreSQL.
  scope: IAM database authentication for Aurora.
  link: [works with Aurora MySQL, and Aurora PostgreSQL](../facts/aurora.md#aurora-iam-db-auth-engines)
  link: [IAM database authentication](../facts/aurora.md#aurora-iam-db-auth-engines)
aurora-iam-db-auth-token-instead-of-password
  claim: With IAM database authentication, you do not need to use a password when you connect to a DB cluster; you use an authentication token instead.
  scope: IAM database authentication for Aurora.
  link: [don't need to use a password](../facts/aurora.md#aurora-iam-db-auth-token-instead-of-password)
  link: [use an authentication token](../facts/aurora.md#aurora-iam-db-auth-token-instead-of-password)
aurora-iam-db-auth-token-only-for-authentication
  claim: The IAM authentication token is used only for authentication and does not affect the session after it is established.
  scope: IAM database authentication for Aurora.
  link: [only used for authentication](../facts/aurora.md#aurora-iam-db-auth-token-only-for-authentication)
  link: [doesn't affect the session after it is established](../facts/aurora.md#aurora-iam-db-auth-token-only-for-authentication)
aurora-iam-db-auth-token-sigv4-15-minutes
  claim: IAM database authentication tokens are generated using AWS Signature Version 4, and each token has a lifetime of 15 minutes.
  scope: per authentication token; fixed; not adjustable.
  link: [lifetime of 15 minutes](../facts/aurora.md#aurora-iam-db-auth-token-sigv4-15-minutes)
  link: [AWS Signature Version 4](../facts/aurora.md#aurora-iam-db-auth-token-sigv4-15-minutes)
aurora-iam-db-auth-traffic-ssl-tls
  claim: With IAM database authentication, network traffic to and from the database is encrypted using SSL or TLS.
  scope: IAM database authentication for Aurora.
  link: [traffic to and from the database is encrypted](../facts/aurora.md#aurora-iam-db-auth-traffic-ssl-tls)
  link: [Transport Layer Security (TLS)](../facts/aurora.md#aurora-iam-db-auth-traffic-ssl-tls)
aurora-instance-class-determines-compute-memory
  claim: The DB instance class determines the computation and memory capacity of an Amazon Aurora DB instance.
  scope: Aurora DB instance classes.
  link: [determines the computation and memory capacity](../facts/aurora.md#aurora-instance-class-determines-compute-memory)
  link: [DB instance class](../facts/aurora.md#aurora-instance-class-determines-compute-memory)
aurora-instance-class-type-and-size
  claim: A DB instance class consists of both the DB instance class type and the size.
  scope: Aurora DB instance classes.
  link: [DB instance class type and the size](../facts/aurora.md#aurora-instance-class-type-and-size)
  link: [DB instance class type](../facts/aurora.md#aurora-instance-class-type-and-size)
aurora-instance-endpoint-console-only
  claim: The instance endpoint location for each instance can be found only in the AWS Management Console, on the instance detail page.
  scope: Aurora instance endpoints.
  link: [in the AWS Management Console only](../facts/aurora.md#aurora-instance-endpoint-console-only)
  link: [instance detail page for your instance](../facts/aurora.md#aurora-instance-endpoint-console-only)
aurora-instance-endpoint-specific-db-instance
  claim: An instance endpoint connects to a specific DB instance within an Aurora cluster, and each DB instance has its own unique instance endpoint.
  scope: Aurora instance endpoints.
  link: [connects to a specific DB instance](../facts/aurora.md#aurora-instance-endpoint-specific-db-instance)
  link: [its own unique instance endpoint](../facts/aurora.md#aurora-instance-endpoint-specific-db-instance)
aurora-instance-endpoint-use-diagnose-one-instance
  claim: In day-to-day Aurora operations, the main use of instance endpoints is to diagnose capacity or performance issues that affect one specific instance in an Aurora cluster.
  scope: Aurora instance endpoints.
  link: [diagnose capacity or performance issues](../facts/aurora.md#aurora-instance-endpoint-use-diagnose-one-instance)
  link: [one specific instance](../facts/aurora.md#aurora-instance-endpoint-use-diagnose-one-instance)
aurora-io-counted-same-writer-reader
  claim: I/O operations in Aurora DB clusters are counted the same way, whether they run on a writer or a reader DB instance.
  scope: I/O operations in an Aurora DB cluster.
  link: [counted the same way](../facts/aurora.md#aurora-io-counted-same-writer-reader)
  link: [writer or reader DB instance](../facts/aurora.md#aurora-io-counted-same-writer-reader)
aurora-io-optimized-best-when-io-25-percent-or-more
  claim: Aurora I/O-Optimized is the best choice when your I/O spending is 25% or more of your total Aurora database spending.
  scope: per Aurora DB cluster; the Aurora FAQ and the pricing page say 'exceeds 25%'; the User Guide says '25% or more'.
  link: [25% or more](../facts/aurora.md#aurora-io-optimized-best-when-io-25-percent-or-more)
  say: a quarter or more
aurora-io-optimized-no-io-charges
  claim: With Aurora I/O-Optimized you pay only for the usage and storage of your DB clusters, with no additional charges for read and write I/O operations.
  scope: Aurora I/O-Optimized cluster storage configuration.
  link: [no additional charges for read and write I/O](../facts/aurora.md#aurora-io-optimized-no-io-charges)
  link: [pay only for the usage and storage](../facts/aurora.md#aurora-io-optimized-no-io-charges)
aurora-io-optimized-save-up-to-40-percent-above-25-percent-io
  claim: With Aurora I/O-Optimized, if your I/O spend exceeds 25% of your total Aurora database spend, you can save up to 40% on costs.
  scope: per Aurora DB cluster.
  link: [exceeds 25%](../facts/aurora.md#aurora-io-optimized-save-up-to-40-percent-above-25-percent-io)
  link: [up to 40%](../facts/aurora.md#aurora-io-optimized-save-up-to-40-percent-above-25-percent-io)
  say: more than a quarter | up to forty percent
aurora-io-switch-io-optimized-to-standard-any-time
  claim: You can switch an Aurora cluster from Aurora I/O-Optimized to Aurora Standard at any time.
  scope: per Aurora DB cluster.
  link: [at any time](../facts/aurora.md#aurora-io-switch-io-optimized-to-standard-any-time)
  say: at any time
aurora-io-switch-no-downtime-non-nvme-and-serverless
  claim: Switching between Aurora Standard and Aurora I/O-Optimized for non-NVMe-based DB instances causes no downtime. Aurora Serverless instances are non-NVMe-based, so no reboot is required when switching from Standard to I/O-Optimized.
  scope: per Aurora DB cluster.
  link: [there is no downtime](../facts/aurora.md#aurora-io-switch-no-downtime-non-nvme-and-serverless)
aurora-io-switch-standard-to-io-optimized-once-every-30-days
  claim: You can switch an Aurora cluster from Aurora Standard to Aurora I/O-Optimized once every 30 days.
  scope: per Aurora DB cluster; minimum; not adjustable.
  link: [once every 30 days](../facts/aurora.md#aurora-io-switch-standard-to-io-optimized-once-every-30-days)
  say: once every thirty days
aurora-is-managed-relational-engine
  claim: Amazon Aurora is a fully managed relational database engine that is compatible with MySQL and PostgreSQL.
  scope: Amazon Aurora overview.
  link: [fully managed relational database engine](../facts/aurora.md#aurora-is-managed-relational-engine)
  link: [compatible with MySQL and PostgreSQL](../facts/aurora.md#aurora-is-managed-relational-engine)
aurora-limitless-horizontal-write-scaling
  claim: Amazon Aurora PostgreSQL Limitless Database provides automated horizontal scaling to process millions of write transactions per second and manages petabytes of data while operating inside a single database.
  scope: Aurora PostgreSQL Limitless Database.
  link: [millions of write transactions per second](../facts/aurora.md#aurora-limitless-horizontal-write-scaling)
  link: [manages petabytes of data](../facts/aurora.md#aurora-limitless-horizontal-write-scaling)
aurora-limitless-routers-present-single-database-image
  claim: In Limitless Database, routers manage the distributed nature of the database and present a single database image to database clients.
  scope: Aurora PostgreSQL Limitless Database.
  link: [present a single database image to database clients](../facts/aurora.md#aurora-limitless-routers-present-single-database-image)
  link: [manage the distributed nature of the database](../facts/aurora.md#aurora-limitless-routers-present-single-database-image)
aurora-limitless-shard-group-contains-nodes-cluster-endpoint
  claim: All of the nodes of a Limitless Database are contained in the DB shard group, and you use the DB cluster endpoint to access Limitless Database.
  scope: Aurora PostgreSQL Limitless Database.
  link: [contained in the DB shard group](../facts/aurora.md#aurora-limitless-shard-group-contains-nodes-cluster-endpoint)
  link: [use the DB cluster endpoint](../facts/aurora.md#aurora-limitless-shard-group-contains-nodes-cluster-endpoint)
aurora-limitless-shards-store-subset-of-data
  claim: In Limitless Database, shards are Aurora PostgreSQL DB instances that each store a subset of the data, allowing simultaneous processing to achieve higher write throughput.
  scope: Aurora PostgreSQL Limitless Database.
  link: [store a subset of the data](../facts/aurora.md#aurora-limitless-shards-store-subset-of-data)
  link: [simultaneous processing to achieve higher write throughput](../facts/aurora.md#aurora-limitless-shards-store-subset-of-data)
aurora-limitless-two-layer-routers-shards
  claim: Limitless Database achieves scale with a two-layer architecture of multiple database nodes, which are either routers or shards.
  scope: Aurora PostgreSQL Limitless Database.
  link: [two-layer architecture consisting of multiple database nodes](../facts/aurora.md#aurora-limitless-two-layer-routers-shards)
  link: [Nodes are either routers or shards](../facts/aurora.md#aurora-limitless-two-layer-routers-shards)
aurora-management-operates-on-clusters
  claim: Aurora management operations typically involve entire clusters of database servers that are synchronized through replication, instead of individual database instances.
  scope: Amazon Aurora overview.
  link: [entire clusters of database servers](../facts/aurora.md#aurora-management-operates-on-clusters)
  link: [instead of individual database instances](../facts/aurora.md#aurora-management-operates-on-clusters)
aurora-manual-failover-console-cli-api
  claim: You can use the AWS Management Console, AWS CLI, or RDS API to perform a manual failover.
  scope: Aurora DB cluster failover within one Region.
  link: [AWS Management Console, AWS CLI, or RDS API](../facts/aurora.md#aurora-manual-failover-console-cli-api)
  link: [perform a manual failover](../facts/aurora.md#aurora-manual-failover-console-cli-api)
aurora-manual-failover-possible
  claim: You can perform a manual failover of an Aurora DB cluster, for example to replace a provisioned writer DB instance with an Aurora serverless writer instance.
  scope: Aurora DB cluster failover within one Region.
  link: [perform a manual failover](../facts/aurora.md#aurora-manual-failover-possible)
  link: [an Aurora serverless writer instance](../facts/aurora.md#aurora-manual-failover-possible)
aurora-manual-failover-target-db-instance-identifier
  claim: When you fail over a DB cluster with the AWS CLI failover-db-cluster command, the --target-db-instance-identifier parameter is the name of the DB instance to promote to the primary DB instance.
  scope: Aurora DB cluster failover within one Region.
  link: [The name of the DB instance to promote](../facts/aurora.md#aurora-manual-failover-target-db-instance-identifier)
  link: [--target-db-instance-identifier](../facts/aurora.md#aurora-manual-failover-target-db-instance-identifier)
aurora-manual-snapshots-not-subject-to-retention
  claim: Unlike automated backups, manual snapshots are not subject to the backup retention period.
  scope: Aurora automated backups.
  link: [manual snapshots aren't subject to the backup retention](../facts/aurora.md#aurora-manual-snapshots-not-subject-to-retention)
  link: [Unlike automated backups](../facts/aurora.md#aurora-manual-snapshots-not-subject-to-retention)
aurora-max-connections-set-by-parameter-group
  claim: The maximum number of connections allowed to an Aurora DB instance is determined by the max_connections parameter in the instance-level parameter group for the DB instance.
  scope: Aurora performance best practices.
  link: [determined by the `max_connections` parameter](../facts/aurora.md#aurora-max-connections-set-by-parameter-group)
  link: [instance-level parameter group](../facts/aurora.md#aurora-max-connections-set-by-parameter-group)
aurora-memory-optimized-r-class-example
  claim: db.r6g is an example of a memory-optimized DB instance class type powered by AWS Graviton2 processors.
  scope: Aurora DB instance classes.
  link: [db.r6g is a memory-optimized DB instance class type](../facts/aurora.md#aurora-memory-optimized-r-class-example)
  link: [powered by AWS Graviton2 processors](../facts/aurora.md#aurora-memory-optimized-r-class-example)
aurora-migrate-from-rds-snapshot-or-replication
  claim: You can bring data from Amazon RDS for MySQL and Amazon RDS for PostgreSQL into Aurora by creating and restoring snapshots, or by setting up one-way replication.
  scope: migration into Aurora.
  link: [creating and restoring snapshots](../facts/aurora.md#aurora-migrate-from-rds-snapshot-or-replication)
  link: [setting up one-way replication](../facts/aurora.md#aurora-migrate-from-rds-snapshot-or-replication)
aurora-migrate-heterogeneous-consider-sct
  claim: If you migrate to Aurora from a database system with a different underlying engine, AWS suggests the AWS Schema Conversion Tool (AWS SCT) to simplify the process.
  scope: heterogeneous migration into Aurora; source engine differs from the Aurora engine.
  link: [AWS Schema Conversion Tool (AWS SCT)](../facts/aurora.md#aurora-migrate-heterogeneous-consider-sct)
  link: [different underlying engine than Aurora's](../facts/aurora.md#aurora-migrate-heterogeneous-consider-sct)
aurora-migrate-options-depend-on-engine-and-source
  claim: You have several options for migrating data from an existing database to an Amazon Aurora DB cluster, depending on database engine compatibility.
  scope: migration into Aurora.
  link: [several options for migrating data](../facts/aurora.md#aurora-migrate-options-depend-on-engine-and-source)
  link: [depending on database engine compatibility](../facts/aurora.md#aurora-migrate-options-depend-on-engine-and-source)
aurora-modify-priority-no-failover-trigger
  claim: You can modify the priority of an Aurora Replica at any time, and modifying the priority does not trigger a failover.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [modify the priority of an Aurora Replica](../facts/aurora.md#aurora-modify-priority-no-failover-trigger)
  link: [doesn't trigger a failover](../facts/aurora.md#aurora-modify-priority-no-failover-trigger)
aurora-mysql-binlog-cross-region-replica-up-to-five
  claim: You can create an Aurora read replica of an Aurora MySQL DB cluster in a different AWS Region by using MySQL binary log (binlog) replication, and each cluster can have up to five read replicas created this way, each in a different Region.
  scope: per Aurora MySQL DB cluster, cross-Region read replicas created with binlog replication; maximum; not adjustable; each replica in a different Region.
  link: [up to five read replicas](../facts/aurora.md#aurora-mysql-binlog-cross-region-replica-up-to-five)
  link: [MySQL binary log (binlog) replication](../facts/aurora.md#aurora-mysql-binlog-cross-region-replica-up-to-five)
aurora-mysql-binlog-not-for-serverless-v1
  claim: Binlog replication is not available for Aurora Serverless v1 clusters.
  scope: Aurora MySQL binary log (binlog) replication.
  link: [binlog replication isn't available for Aurora Serverless v1 clusters](../facts/aurora.md#aurora-mysql-binlog-not-for-serverless-v1)
  link: [Aurora Serverless v1 clusters](../facts/aurora.md#aurora-mysql-binlog-not-for-serverless-v1)
aurora-mysql-binlog-only-innodb-tables
  claim: When you replicate between Aurora MySQL and MySQL, use only InnoDB tables.
  scope: Aurora MySQL binary log (binlog) replication.
  link: [use only InnoDB tables](../facts/aurora.md#aurora-mysql-binlog-only-innodb-tables)
  link: [replicate between Aurora MySQL and MySQL](../facts/aurora.md#aurora-mysql-binlog-only-innodb-tables)
aurora-mysql-binlog-replication-external-mysql-inside-or-outside-aws
  claim: You can set up binlog-based replication between an Aurora MySQL database and an external MySQL database running inside or outside of AWS.
  scope: Aurora MySQL binary log (binlog) replication.
  link: [an external MySQL database](../facts/aurora.md#aurora-mysql-binlog-replication-external-mysql-inside-or-outside-aws)
  link: [inside or outside of AWS](../facts/aurora.md#aurora-mysql-binlog-replication-external-mysql-inside-or-outside-aws)
aurora-mysql-binlog-replication-with-mysql
  claim: Because Aurora MySQL is compatible with MySQL, you can set up replication between a MySQL database and an Aurora MySQL DB cluster using MySQL binary log (binlog) replication.
  scope: Aurora MySQL binary log (binlog) replication.
  link: [set up replication between a MySQL database](../facts/aurora.md#aurora-mysql-binlog-replication-with-mysql)
  link: [MySQL binary log replication](../facts/aurora.md#aurora-mysql-binlog-replication-with-mysql)
aurora-mysql-binlog-same-region-two-clusters
  claim: Two Aurora MySQL DB clusters in the same Region can be replicated by using MySQL binary log (binlog) replication.
  scope: Aurora MySQL binary log (binlog) replication.
  link: [in the same Region](../facts/aurora.md#aurora-mysql-binlog-same-region-two-clusters)
  link: [MySQL binary log (binlog) replication](../facts/aurora.md#aurora-mysql-binlog-same-region-two-clusters)
aurora-mysql-binlog-source-or-replica
  claim: With binlog replication, your Aurora MySQL DB cluster can be the replication source or the replica.
  scope: Aurora MySQL binary log (binlog) replication.
  link: [replication source or the replica](../facts/aurora.md#aurora-mysql-binlog-source-or-replica)
aurora-mysql-cross-region-data-transfer-charges
  claim: Data transferred for Aurora MySQL cross-Region replication incurs Amazon RDS data transfer charges.
  scope: Aurora MySQL cross-Region read replicas (binlog replication).
  link: [incurs Amazon RDS data transfer charges](../facts/aurora.md#aurora-mysql-cross-region-data-transfer-charges)
  link: [Data transferred for cross-Region replication](../facts/aurora.md#aurora-mysql-cross-region-data-transfer-charges)
aurora-mysql-cross-region-read-replica-cluster
  claim: You can create an Amazon Aurora MySQL DB cluster as a read replica in a different AWS Region than the source DB cluster.
  scope: Aurora MySQL cross-Region read replicas (binlog replication).
  link: [in a different AWS Region](../facts/aurora.md#aurora-mysql-cross-region-read-replica-cluster)
  link: [Aurora MySQL DB cluster as a read replica](../facts/aurora.md#aurora-mysql-cross-region-read-replica-cluster)
aurora-mysql-cross-region-replica-must-be-encrypted-if-source
  claim: The cross-Region read replica must be encrypted if the source DB cluster is encrypted.
  scope: Aurora MySQL cross-Region read replicas (binlog replication).
  link: [must be encrypted if the source DB cluster](../facts/aurora.md#aurora-mysql-cross-region-replica-must-be-encrypted-if-source)
  link: [read replica must be encrypted](../facts/aurora.md#aurora-mysql-cross-region-replica-must-be-encrypted-if-source)
aurora-mysql-cross-region-up-to-five-replica-clusters
  claim: For each source Aurora MySQL DB cluster, you can have up to five cross-Region DB clusters that are read replicas.
  scope: per source Aurora MySQL DB cluster; maximum; not adjustable.
  link: [up to five cross-Region DB clusters](../facts/aurora.md#aurora-mysql-cross-region-up-to-five-replica-clusters)
aurora-mysql-dr-read-replica-of-mysql
  claim: To use Aurora for disaster recovery of a MySQL DB instance, create an Amazon Aurora DB cluster and make it a read replica of the MySQL DB instance.
  scope: Aurora MySQL DB cluster as a read replica of a MySQL DB instance.
  link: [a read replica of your MySQL DB instance](../facts/aurora.md#aurora-mysql-dr-read-replica-of-mysql)
  link: [disaster recovery of your MySQL DB instance](../facts/aurora.md#aurora-mysql-dr-read-replica-of-mysql)
aurora-mysql-failover-restarts-only-writer-and-target
  claim: In Aurora MySQL, Aurora restarts only the writer DB instance and the reader instance to which it fails over, so other readers stay available through the reader endpoint.
  scope: Aurora MySQL DB clusters.
  link: [restarts only the writer DB instance](../facts/aurora.md#aurora-mysql-failover-restarts-only-writer-and-target)
  link: [reader instance to which it fails over](../facts/aurora.md#aurora-mysql-failover-restarts-only-writer-and-target)
aurora-mysql-migrate-by-setting-up-replication
  claim: Because Aurora MySQL is compatible with MySQL, you can migrate data from a MySQL database by setting up replication between the MySQL database and an Aurora MySQL DB cluster.
  scope: migration into Aurora.
  link: [by setting up replication](../facts/aurora.md#aurora-mysql-migrate-by-setting-up-replication)
  link: [Amazon Aurora MySQL is compatible with MySQL](../facts/aurora.md#aurora-mysql-migrate-by-setting-up-replication)
aurora-mysql-migrate-from-rds-snapshot-under-an-hour
  claim: You can create a new Aurora database from an RDS for MySQL DB snapshot, and migration operations based on DB snapshots typically complete in under an hour.
  scope: migration into Aurora.
  link: [typically complete in under an hour](../facts/aurora.md#aurora-mysql-migrate-from-rds-snapshot-under-an-hour)
  link: [from an RDS for MySQL DB snapshot](../facts/aurora.md#aurora-mysql-migrate-from-rds-snapshot-under-an-hour)
aurora-mysql-migrate-replica-lag-zero-then-stop-replication
  claim: To migrate from RDS for MySQL with an Aurora read replica, wait until the replica lag is 0, direct client applications to the Aurora read replica, and then stop replication to make it a standalone Aurora MySQL DB cluster.
  scope: migration into Aurora.
  link: [replica lag between the RDS for MySQL DB instance and the Aurora read replica is 0](../facts/aurora.md#aurora-mysql-migrate-replica-lag-zero-then-stop-replication)
  link: [stop replication to make the Aurora read replica](../facts/aurora.md#aurora-mysql-migrate-replica-lag-zero-then-stop-replication)
aurora-mysql-migrate-replica-takes-hours-per-tib
  claim: Migration to Aurora MySQL with an Aurora read replica takes a while, roughly several hours per tebibyte (TiB) of data.
  scope: migration into Aurora.
  link: [roughly several hours per tebibyte (TiB) of data](../facts/aurora.md#aurora-mysql-migrate-replica-takes-hours-per-tib)
  link: [migration to take a while](../facts/aurora.md#aurora-mysql-migrate-replica-takes-hours-per-tib)
aurora-mysql-no-aurora-replica-if-source-has-cross-region-replica
  claim: You cannot create an Aurora read replica if your RDS for MySQL DB instance is already the source for a cross-Region read replica.
  scope: migration into Aurora.
  link: [can't create an Aurora read replica](../facts/aurora.md#aurora-mysql-no-aurora-replica-if-source-has-cross-region-replica)
  link: [already the source for a cross-Region read replica](../facts/aurora.md#aurora-mysql-no-aurora-replica-if-source-has-cross-region-replica)
aurora-mysql-only-one-aurora-read-replica-per-rds-mysql
  claim: You can have only one Aurora read replica for an RDS for MySQL DB instance.
  scope: migration into Aurora.
  link: [only one Aurora read replica](../facts/aurora.md#aurora-mysql-only-one-aurora-read-replica-per-rds-mysql)
  link: [RDS for MySQL DB instance](../facts/aurora.md#aurora-mysql-only-one-aurora-read-replica-per-rds-mysql)
aurora-mysql-promote-replica-data-recovery-scheme
  claim: Typically, you promote an Aurora MySQL read replica to a standalone DB cluster as a data recovery scheme if the source DB cluster fails.
  scope: Aurora MySQL cross-Region read replicas (binlog replication).
  link: [data recovery scheme](../facts/aurora.md#aurora-mysql-promote-replica-data-recovery-scheme)
aurora-mysql-promote-replica-reboots-instances
  claim: When you promote an Aurora MySQL read replica, its DB instances are rebooted before they become available.
  scope: Aurora MySQL cross-Region read replicas (binlog replication).
  link: [rebooted before they become available](../facts/aurora.md#aurora-mysql-promote-replica-reboots-instances)
aurora-mysql-promote-replica-to-standalone
  claim: You can promote an Aurora MySQL read replica to a standalone DB cluster.
  scope: Aurora MySQL cross-Region read replicas (binlog replication).
  link: [promote an Aurora MySQL read replica](../facts/aurora.md#aurora-mysql-promote-replica-to-standalone)
  link: [standalone DB cluster](../facts/aurora.md#aurora-mysql-promote-replica-to-standalone)
aurora-mysql-promote-stops-replication
  claim: When you promote an Aurora MySQL read replica, replication is stopped and the DB instances are rebooted.
  scope: Aurora MySQL cross-Region read replicas (binlog replication).
  link: [replication is stopped](../facts/aurora.md#aurora-mysql-promote-stops-replication)
  link: [When you promote a read replica](../facts/aurora.md#aurora-mysql-promote-stops-replication)
aurora-mysql-promoted-cluster-not-replication-target
  claim: Because a promoted DB cluster is no longer a read replica, you cannot use it as a replication target.
  scope: Aurora MySQL cross-Region read replicas (binlog replication).
  link: [no longer a read replica](../facts/aurora.md#aurora-mysql-promoted-cluster-not-replication-target)
  link: [can't use it as a replication target](../facts/aurora.md#aurora-mysql-promoted-cluster-not-replication-target)
aurora-mysql-read-replica-of-rds-mysql-binlog-async
  claim: Aurora uses the MySQL DB engines' binary log replication functionality to create a special type of DB cluster called an Aurora read replica for a source RDS for MySQL DB instance.
  scope: migration into Aurora.
  link: [binary log replication functionality](../facts/aurora.md#aurora-mysql-read-replica-of-rds-mysql-binlog-async)
  link: [called an Aurora read replica](../facts/aurora.md#aurora-mysql-read-replica-of-rds-mysql-binlog-async)
aurora-mysql-replica-use-cluster-endpoint-address
  claim: When you set up replication between a MySQL DB instance and an Aurora cluster, use the Aurora DB cluster endpoint address so that after a failover the promoted replica continues to use it.
  scope: Aurora MySQL DB cluster as a read replica of a MySQL DB instance.
  link: [Use the Amazon Aurora DB cluster endpoint address](../facts/aurora.md#aurora-mysql-replica-use-cluster-endpoint-address)
  link: [continues to use the DB cluster endpoint address](../facts/aurora.md#aurora-mysql-replica-use-cluster-endpoint-address)
aurora-mysql-replicas-same-underlying-data
  claim: All Aurora MySQL replicas work from the same underlying data.
  scope: Aurora MySQL DB clusters.
  link: [work from the same underlying data](../facts/aurora.md#aurora-mysql-replicas-same-underlying-data)
  link: [All the replicas](../facts/aurora.md#aurora-mysql-replicas-same-underlying-data)
aurora-mysql-require-secure-transport-default-by-version
  claim: By default, the require_secure_transport parameter is set to ON in Aurora MySQL version 8.4, while it is set to OFF in Aurora MySQL versions 2 and 3.
  scope: per Aurora MySQL DB cluster, by engine version; default; adjustable.
  link: [set to `ON` in Aurora MySQL version 8.4](../facts/aurora.md#aurora-mysql-require-secure-transport-default-by-version)
  link: [set to `OFF` in Aurora MySQL versions 2 and 3](../facts/aurora.md#aurora-mysql-require-secure-transport-default-by-version)
aurora-mysql-require-secure-transport-no-reboot
  claim: You do not need to reboot your DB cluster for a change to the require_secure_transport parameter to take effect.
  scope: Aurora MySQL DB clusters, encryption in transit.
  link: [don't need to reboot your DB cluster](../facts/aurora.md#aurora-mysql-require-secure-transport-no-reboot)
  link: [change to take effect](../facts/aurora.md#aurora-mysql-require-secure-transport-no-reboot)
aurora-mysql-require-secure-transport-parameter
  claim: You can require that all user connections to your Aurora MySQL DB cluster use TLS by using the require_secure_transport DB cluster parameter.
  scope: Aurora MySQL DB clusters, encryption in transit.
  link: [require that all user connections](../facts/aurora.md#aurora-mysql-require-secure-transport-parameter)
  link: [`require_secure_transport` DB cluster parameter](../facts/aurora.md#aurora-mysql-require-secure-transport-parameter)
aurora-mysql-resource-exhaustion-causes-restart-failover
  claim: If a workload exhausts the resources of an Aurora MySQL DB instance, the instance might slow down, restart, or even fail over to another DB instance.
  scope: Aurora MySQL DB clusters.
  link: [might slow down, restart, or even fail over](../facts/aurora.md#aurora-mysql-resource-exhaustion-causes-restart-failover)
  link: [exhausts the resources you're using](../facts/aurora.md#aurora-mysql-resource-exhaustion-causes-restart-failover)
aurora-mysql-scale-reads-for-mysql-with-aurora-replica
  claim: To use Aurora to scale reads for a MySQL DB instance, create an Amazon Aurora MySQL DB cluster and make it a read replica of the MySQL DB instance.
  scope: Aurora MySQL DB cluster as a read replica of a MySQL DB instance.
  link: [a read replica of your MySQL DB instance](../facts/aurora.md#aurora-mysql-scale-reads-for-mysql-with-aurora-replica)
  link: [scale reads for your MySQL DB instance](../facts/aurora.md#aurora-mysql-scale-reads-for-mysql-with-aurora-replica)
aurora-mysql-spreads-read-connections
  claim: Aurora automatically spreads read-only connections across multiple database instances, helping an Aurora cluster support query-intensive workloads.
  scope: Aurora MySQL DB clusters.
  link: [automatically spreads your read-only connections](../facts/aurora.md#aurora-mysql-spreads-read-connections)
  link: [query-intensive workloads](../facts/aurora.md#aurora-mysql-spreads-read-connections)
aurora-mysql-standard-import-export-tools-work
  claim: Standard MySQL import and export tools (mysqldump, mysqlimport) work with Aurora.
  scope: migration into Aurora.
  link: [Standard MySQL import and export tools](../facts/aurora.md#aurora-mysql-standard-import-export-tools-work)
  link: [(mysqldump, mysqlimport) work with Aurora](../facts/aurora.md#aurora-mysql-standard-import-export-tools-work)
aurora-mysql-write-forwarding-rds-proxy-no-session-value
  claim: The RDS Proxy feature does not support the SESSION value for the aurora_replica_read_consistency variable.
  scope: Aurora MySQL write forwarding in a global database.
  link: [doesn't support the `SESSION` value](../facts/aurora.md#aurora-mysql-write-forwarding-rds-proxy-no-session-value)
  link: [`aurora_replica_read_consistency` variable](../facts/aurora.md#aurora-mysql-write-forwarding-rds-proxy-no-session-value)
aurora-mysql-write-forwarding-set-read-consistency-per-session
  claim: Always set the aurora_replica_read_consistency parameter for any session for which you want to forward writes, because otherwise Aurora MySQL does not enable write forwarding for that session.
  scope: Aurora MySQL write forwarding in a global database.
  link: [set the `aurora_replica_read_consistency` parameter for any session](../facts/aurora.md#aurora-mysql-write-forwarding-set-read-consistency-per-session)
  link: [forward writes](../facts/aurora.md#aurora-mysql-write-forwarding-set-read-consistency-per-session)
aurora-mysql-write-forwarding-version-support
  claim: Write forwarding is supported with Aurora MySQL 2.08.1 and higher versions, in every Region where Aurora MySQL-based global databases are available.
  scope: Aurora MySQL write forwarding in a global database.
  link: [supported with Aurora MySQL 2.08.1 and higher versions](../facts/aurora.md#aurora-mysql-write-forwarding-version-support)
aurora-no-cross-region-automated-backup-replication
  claim: Cross-Region automated backup replication is not supported for Aurora DB clusters, so for disaster recovery across Regions you must manually copy Aurora snapshots to the destination Region.
  scope: Aurora automated backups.
  link: [Cross-Region automated backup replication isn't supported](../facts/aurora.md#aurora-no-cross-region-automated-backup-replication)
  link: [manually copy Aurora snapshots](../facts/aurora.md#aurora-no-cross-region-automated-backup-replication)
aurora-no-incremental-snapshots-full-copies
  claim: Aurora does not support incremental snapshots, and Aurora DB cluster snapshot copies are always stored as full copies.
  scope: Aurora DB cluster snapshots.
  link: [Aurora doesn't support incremental snapshots](../facts/aurora.md#aurora-no-incremental-snapshots-full-copies)
  link: [always stored as full copies](../facts/aurora.md#aurora-no-incremental-snapshots-full-copies)
aurora-no-local-zones
  claim: Aurora does not support Local Zones.
  scope: AWS Regions and Availability Zones for Aurora.
  link: [doesn't support Local Zones](../facts/aurora.md#aurora-no-local-zones)
  link: [Aurora doesn't support Local Zones](../facts/aurora.md#aurora-no-local-zones)
aurora-no-replica-primary-recreated-same-az
  claim: If the DB cluster has no Aurora Replicas, the primary instance is recreated in the same AZ during a failure event, and read and write operations fail with an exception until it is created.
  scope: Aurora DB cluster failover within one Region.
  link: [recreated in the same AZ](../facts/aurora.md#aurora-no-replica-primary-recreated-same-az)
  link: [doesn't contain any Aurora Replicas](../facts/aurora.md#aurora-no-replica-primary-recreated-same-az)
aurora-nvme-io-switch-needs-engine-restart
  claim: For NVMe-based DB instances, switching between Aurora I/O-Optimized and Aurora Standard requires a database engine restart, which may cause a brief period of downtime.
  scope: Aurora DB cluster storage configuration (Standard or I/O-Optimized).
  link: [requires a database engine restart](../facts/aurora.md#aurora-nvme-io-switch-needs-engine-restart)
  link: [brief period of downtime](../facts/aurora.md#aurora-nvme-io-switch-needs-engine-restart)
aurora-on-demand-billing-one-second-increments-ten-minute-minimum
  claim: Aurora On-Demand partial instance-hours are billed in 1-second increments with a 10-minute minimum charge following a billable status change such as creating, starting, or modifying the database instance.
  scope: per Aurora DB instance; minimum.
  link: [10-minute minimum charge](../facts/aurora.md#aurora-on-demand-billing-one-second-increments-ten-minute-minimum)
  link: [1-second increments](../facts/aurora.md#aurora-on-demand-billing-one-second-increments-ten-minute-minimum)
  say: ten-minute minimum | one-second increments
aurora-one-primary-per-cluster
  claim: Each Aurora DB cluster has one primary DB instance.
  scope: Aurora DB cluster: primary instance and Aurora Replicas.
  link: [one primary DB instance](../facts/aurora.md#aurora-one-primary-per-cluster)
  link: [Each Aurora DB cluster](../facts/aurora.md#aurora-one-primary-per-cluster)
aurora-optimized-reads-nvme-instance-types
  claim: Aurora Optimized Reads is available by default when you create a DB cluster that uses Graviton-based R6gd, R8gd, and Intel-based R6id instances with NVMe storage.
  scope: Aurora PostgreSQL Optimized Reads.
  link: [R6gd, R8gd, and Intel-based R6id instances](../facts/aurora.md#aurora-optimized-reads-nvme-instance-types)
  link: [non-volatile memory express (NVMe) storage](../facts/aurora.md#aurora-optimized-reads-nvme-instance-types)
aurora-optimized-reads-standard-cluster-temp-objects-only
  claim: On an Aurora Standard cluster, Optimized Reads makes use of only temporary objects, whereas on an Aurora I/O-Optimized cluster it uses both tiered cache and temporary objects.
  scope: Aurora PostgreSQL Optimized Reads.
  link: [makes use of only temporary objects](../facts/aurora.md#aurora-optimized-reads-standard-cluster-temp-objects-only)
  link: [Aurora Standard cluster](../facts/aurora.md#aurora-optimized-reads-standard-cluster-temp-objects-only)
aurora-optimized-reads-tiered-cache-and-temp-objects
  claim: Aurora Optimized Reads supports two capabilities: tiered cache and temporary objects.
  scope: Aurora PostgreSQL Optimized Reads.
  link: [tiered cache and temporary objects](../facts/aurora.md#aurora-optimized-reads-tiered-cache-and-temp-objects)
  link: [two capabilities](../facts/aurora.md#aurora-optimized-reads-tiered-cache-and-temp-objects)
aurora-page-cache-survives-database-restart
  claim: In Aurora, each DB instance's page cache is managed in a separate process from the database, so the page cache can survive independently of the database.
  scope: Aurora crash recovery and reliability.
  link: [managed in a separate process from the database](../facts/aurora.md#aurora-page-cache-survives-database-restart)
  link: [survive independently of the database](../facts/aurora.md#aurora-page-cache-survives-database-restart)
aurora-parallel-query-best-for-large-analytic-queries
  claim: Parallel query works best with Aurora MySQL DB clusters that have tables with millions of rows and analytic queries that take minutes or hours to complete.
  scope: Aurora MySQL parallel query.
  link: [tables with millions of rows](../facts/aurora.md#aurora-parallel-query-best-for-large-analytic-queries)
  link: [take minutes or hours to complete](../facts/aurora.md#aurora-parallel-query-best-for-large-analytic-queries)
aurora-parallel-query-engine-decides-no-sql-changes
  claim: When the parallel query feature is turned on, the Aurora MySQL engine automatically determines when queries can benefit, without SQL changes such as hints or table attributes.
  scope: Aurora MySQL parallel query.
  link: [automatically determines when queries can benefit](../facts/aurora.md#aurora-parallel-query-engine-decides-no-sql-changes)
  link: [without requiring SQL changes](../facts/aurora.md#aurora-parallel-query-engine-decides-no-sql-changes)
aurora-parallel-query-pushes-work-to-storage
  claim: Aurora MySQL parallel query is an optimization that parallelizes some of the I/O and computation involved in processing data-intensive queries.
  scope: Aurora MySQL parallel query.
  link: [parallelizes some of the I/O and computation](../facts/aurora.md#aurora-parallel-query-pushes-work-to-storage)
  link: [data-intensive queries](../facts/aurora.md#aurora-parallel-query-pushes-work-to-storage)
aurora-parallel-query-unrelated-to-postgresql-parallel-query
  claim: The PostgreSQL database engine's feature called parallel query is unrelated to Aurora parallel query.
  scope: Aurora MySQL parallel query.
  link: [unrelated to Aurora parallel query](../facts/aurora.md#aurora-parallel-query-unrelated-to-postgresql-parallel-query)
  link: [That feature](../facts/aurora.md#aurora-parallel-query-unrelated-to-postgresql-parallel-query)
aurora-parallel-query-without-it-head-node-processes
  claim: Without parallel query, each query brings all the scanned data to a single node within the Aurora MySQL cluster (the head node) and performs all the query processing there.
  scope: Aurora MySQL parallel query.
  link: [all the scanned data to a single node](../facts/aurora.md#aurora-parallel-query-without-it-head-node-processes)
  link: [performs all the query processing there](../facts/aurora.md#aurora-parallel-query-without-it-head-node-processes)
aurora-part-of-rds
  claim: Aurora is part of the managed database service Amazon Relational Database Service (Amazon RDS).
  scope: Amazon Aurora overview.
  link: [part of the managed database service](../facts/aurora.md#aurora-part-of-rds)
  link: [Amazon Relational Database Service](../facts/aurora.md#aurora-part-of-rds)
aurora-performance-guide-replica-lag-considerably-under-100-ms
  claim: You can achieve read scaling by creating up to 15 Aurora Replicas in a DB cluster. Each Aurora Replica returns the same data from the cluster volume with minimal replica lag, usually considerably less than 100 milliseconds after the primary instance has written an update.
  scope: per Aurora DB cluster; maximum.
  link: [considerably less than 100 milliseconds](../facts/aurora.md#aurora-performance-guide-replica-lag-considerably-under-100-ms)
  say: well under a hundred milliseconds
aurora-pitr-any-point-within-retention
  claim: You can restore an Aurora DB cluster to any point in time within the backup retention period.
  scope: Aurora point-in-time recovery.
  link: [any point in time](../facts/aurora.md#aurora-pitr-any-point-within-retention)
  link: [backup retention period](../facts/aurora.md#aurora-pitr-any-point-within-retention)
aurora-pitr-any-second-within-retention-period
  claim: Aurora point-in-time recovery lets you restore your database to any second during the retention period, up to the last 5 minutes.
  scope: per Aurora DB cluster.
  link: [any second during your retention period](../facts/aurora.md#aurora-pitr-any-second-within-retention-period)
  say: any second in the retention period
aurora-pitr-aws-backup-plan-used-for-point-in-time-recovery
  claim: If an Aurora DB cluster is associated with a backup plan in AWS Backup, that backup plan is used for point-in-time recovery.
  scope: Aurora DB cluster point-in-time recovery; since September 2023 Aurora automated (continuous) backups can be managed in AWS Backup.
  link: [that backup plan is used for point-in-time recovery](../facts/aurora.md#aurora-pitr-aws-backup-plan-used-for-point-in-time-recovery)
aurora-pitr-creates-new-cluster
  claim: Restoring an Aurora DB cluster to a specific point in time creates a new DB cluster.
  scope: per Aurora DB cluster.
  link: [creating a new DB cluster](../facts/aurora.md#aurora-pitr-creates-new-cluster)
aurora-pitr-logs-uploaded-continuously-to-s3
  claim: Amazon Aurora uploads log records for DB clusters to Amazon S3 continuously.
  scope: Aurora point-in-time recovery.
  link: [uploads log records for DB clusters to Amazon S3 continuously](../facts/aurora.md#aurora-pitr-logs-uploaded-continuously-to-s3)
  link: [Amazon S3 continuously](../facts/aurora.md#aurora-pitr-logs-uploaded-continuously-to-s3)
aurora-pitr-restored-same-retention-as-source
  claim: The backup retention period of a cluster restored to a point in time is the same as that of the source DB cluster.
  scope: Aurora point-in-time recovery.
  link: [same as that of the source DB cluster](../facts/aurora.md#aurora-pitr-restored-same-retention-as-source)
  link: [backup retention period of the restored DB cluster](../facts/aurora.md#aurora-pitr-restored-same-retention-as-source)
aurora-postgres-ccm-cold-cache-after-failover
  claim: After a typical failover, the new writer starts with an empty buffer cache (a cold cache), which degrades performance because the instance must read from the slower disk.
  scope: Aurora PostgreSQL cluster cache management.
  link: [A cold cache degrades performance](../facts/aurora.md#aurora-postgres-ccm-cold-cache-after-failover)
  link: [read from the slower disk](../facts/aurora.md#aurora-postgres-ccm-cold-cache-after-failover)
aurora-postgres-ccm-keeps-cache-synchronized-warm
  claim: Cluster cache management keeps the data in the designated reader's cache synchronized with the data in the writer DB instance's cache, so the reader has a warm cache when it is promoted.
  scope: Aurora PostgreSQL cluster cache management.
  link: [kept synchronized with the data](../facts/aurora.md#aurora-postgres-ccm-keeps-cache-synchronized-warm)
  link: [designated reader's cache](../facts/aurora.md#aurora-postgres-ccm-keeps-cache-synchronized-warm)
aurora-postgres-ccm-not-for-global-secondary
  claim: Cluster cache management is not supported for Aurora PostgreSQL secondary DB clusters that are part of Aurora global databases.
  scope: Aurora PostgreSQL cluster cache management.
  link: [isn't supported for Aurora PostgreSQL secondary DB cluster](../facts/aurora.md#aurora-postgres-ccm-not-for-global-secondary)
  link: [part of Aurora global databases](../facts/aurora.md#aurora-postgres-ccm-not-for-global-secondary)
aurora-postgres-ccm-same-instance-class-as-writer
  claim: Cluster cache management requires that the designated reader instance have the same instance class type and size as the writer.
  scope: Aurora PostgreSQL cluster cache management.
  link: [same instance class type and size](../facts/aurora.md#aurora-postgres-ccm-same-instance-class-as-writer)
  link: [as the writer](../facts/aurora.md#aurora-postgres-ccm-same-instance-class-as-writer)
aurora-postgres-ccm-set-reader-failover-target
  claim: With cluster cache management for Aurora PostgreSQL, you set a specific reader DB instance as the failover target.
  scope: Aurora PostgreSQL cluster cache management.
  link: [as the failover target](../facts/aurora.md#aurora-postgres-ccm-set-reader-failover-target)
  link: [cluster cache management](../facts/aurora.md#aurora-postgres-ccm-set-reader-failover-target)
aurora-postgres-cluster-cache-mgmt-preserves-cache
  claim: For Aurora PostgreSQL, cluster cache management can preserve the page cache of a designated reader instance that becomes the writer instance after failover.
  scope: Aurora PostgreSQL cluster cache management.
  link: [cluster cache management](../facts/aurora.md#aurora-postgres-cluster-cache-mgmt-preserves-cache)
  link: [designated reader instance that becomes the writer instance](../facts/aurora.md#aurora-postgres-cluster-cache-mgmt-preserves-cache)
aurora-postgres-fast-failover-aws-jdbc-driver
  claim: Use the AWS JDBC Driver to take full advantage of the failover capabilities of Aurora PostgreSQL.
  scope: Aurora PostgreSQL client failover best practices.
  link: [Use the AWS JDBC Driver](../facts/aurora.md#aurora-postgres-fast-failover-aws-jdbc-driver)
  link: [failover capabilities of Aurora PostgreSQL](../facts/aurora.md#aurora-postgres-fast-failover-aws-jdbc-driver)
aurora-postgres-fast-failover-dns-caching-timeouts
  claim: For fast failover, set timeouts for Java DNS caching aggressively, which helps the Aurora read-only endpoint cycle through read-only nodes on later connection attempts.
  scope: Aurora PostgreSQL client failover best practices.
  link: [Set timeouts for Java Domain Name System (DNS)](../facts/aurora.md#aurora-postgres-fast-failover-dns-caching-timeouts)
  link: [properly cycle through read-only nodes](../facts/aurora.md#aurora-postgres-fast-failover-dns-caching-timeouts)
aurora-postgres-fast-failover-use-read-write-endpoints
  claim: For fast failover with Aurora PostgreSQL, use the read and write Aurora endpoints that are provided to connect to the cluster.
  scope: Aurora PostgreSQL client failover best practices.
  link: [Use the read and write Aurora endpoints](../facts/aurora.md#aurora-postgres-fast-failover-use-read-write-endpoints)
  link: [provided to connect to the cluster](../facts/aurora.md#aurora-postgres-fast-failover-use-read-write-endpoints)
aurora-postgres-import-from-s3
  claim: You can migrate data by importing it from Amazon S3 into a table belonging to an Aurora PostgreSQL DB cluster.
  scope: migration from RDS for PostgreSQL or other sources to Aurora PostgreSQL.
  link: [importing it from Amazon S3 into a table](../facts/aurora.md#aurora-postgres-import-from-s3)
  link: [Aurora PostgreSQL DB cluster](../facts/aurora.md#aurora-postgres-import-from-s3)
aurora-postgres-local-write-forwarding-read-after-write
  claim: You can use local write forwarding for applications that have occasional writes and require read-after-write consistency, which is the ability to read the latest write in a transaction.
  scope: Aurora PostgreSQL write forwarding.
  link: [occasional writes and require read-after-write consistency](../facts/aurora.md#aurora-postgres-local-write-forwarding-read-after-write)
  link: [local write forwarding](../facts/aurora.md#aurora-postgres-local-write-forwarding-read-after-write)
aurora-postgres-logical-replication-all-versions
  claim: Logical replication is supported by all currently available Aurora PostgreSQL versions.
  scope: Aurora PostgreSQL replication options.
  link: [supported by all currently available Aurora PostgreSQL versions](../facts/aurora.md#aurora-postgres-logical-replication-all-versions)
  link: [Logical replication is supported](../facts/aurora.md#aurora-postgres-logical-replication-all-versions)
aurora-postgres-logical-replication-individual-tables
  claim: With PostgreSQL's logical replication feature, an Aurora PostgreSQL DB cluster can replicate and synchronize individual tables rather than the entire database instance.
  scope: Aurora PostgreSQL replication options.
  link: [replicate and synchronize individual tables](../facts/aurora.md#aurora-postgres-logical-replication-individual-tables)
  link: [rather than the entire database instance](../facts/aurora.md#aurora-postgres-logical-replication-individual-tables)
aurora-postgres-logical-replication-same-region
  claim: Two Aurora PostgreSQL DB clusters in the same Region can be replicated by using PostgreSQL's logical replication feature.
  scope: Aurora PostgreSQL replication options.
  link: [PostgreSQL's logical replication feature](../facts/aurora.md#aurora-postgres-logical-replication-same-region)
  link: [in the same Region](../facts/aurora.md#aurora-postgres-logical-replication-same-region)
aurora-postgres-max-connections-ideal-setting-plus-three
  claim: The ideal max_connections setting for Aurora PostgreSQL supports all the client connections the application needs, without an excess of unused connections, plus at least 3 more connections to support AWS automation.
  scope: Aurora PostgreSQL max_connections setting.
  link: [supports all the client connections your application needs](../facts/aurora.md#aurora-postgres-max-connections-ideal-setting-plus-three)
  link: [at least 3 more connections to support AWS automation](../facts/aurora.md#aurora-postgres-max-connections-ideal-setting-plus-three)
aurora-postgres-max-connections-too-low-no-slots
  claim: If the max_connections value is too low, the Aurora PostgreSQL DB instance might not have sufficient connections available when clients attempt to connect.
  scope: Aurora PostgreSQL max_connections setting.
  link: [might not have sufficient connections available](../facts/aurora.md#aurora-postgres-max-connections-too-low-no-slots)
  link: [max_connections` value is too low](../facts/aurora.md#aurora-postgres-max-connections-too-low-no-slots)
aurora-postgres-migrate-replica-hours-per-terabyte
  claim: Migrating from RDS for PostgreSQL to Aurora PostgreSQL with an Aurora read replica can take several hours per terabyte of data.
  scope: migration from RDS for PostgreSQL or other sources to Aurora PostgreSQL.
  link: [several hours per terabyte of data](../facts/aurora.md#aurora-postgres-migrate-replica-hours-per-terabyte)
  link: [for the migration to complete](../facts/aurora.md#aurora-postgres-migrate-replica-hours-per-terabyte)
aurora-postgres-migrate-replica-lag-zero-stop-replication
  claim: When the replica lag between the RDS for PostgreSQL DB instance and the Aurora PostgreSQL read replica is zero, you can stop replication and make the Aurora read replica a standalone Aurora PostgreSQL DB cluster for reading and writing.
  scope: migration from RDS for PostgreSQL or other sources to Aurora PostgreSQL.
  link: [Aurora PostgreSQL read replica is zero](../facts/aurora.md#aurora-postgres-migrate-replica-lag-zero-stop-replication)
  link: [you can stop replication](../facts/aurora.md#aurora-postgres-migrate-replica-lag-zero-stop-replication)
aurora-postgres-migrate-snapshot-from-rds
  claim: You can migrate data directly from an RDS for PostgreSQL DB snapshot to an Aurora PostgreSQL DB cluster.
  scope: migration from RDS for PostgreSQL or other sources to Aurora PostgreSQL.
  link: [from an RDS for PostgreSQL DB snapshot](../facts/aurora.md#aurora-postgres-migrate-snapshot-from-rds)
  link: [Aurora PostgreSQL DB cluster](../facts/aurora.md#aurora-postgres-migrate-snapshot-from-rds)
aurora-postgres-no-cross-region-aurora-replicas
  claim: Aurora PostgreSQL does not support cross-Region Aurora Replicas, but Aurora Global Database can scale read capabilities to more than one AWS Region.
  scope: Aurora PostgreSQL replication options.
  link: [doesn't support cross-Region Aurora Replicas](../facts/aurora.md#aurora-postgres-no-cross-region-aurora-replicas)
  link: [cross-Region Aurora Replicas](../facts/aurora.md#aurora-postgres-no-cross-region-aurora-replicas)
aurora-postgres-non-postgres-source-use-dms
  claim: You can use AWS Database Migration Service (AWS DMS) to migrate data from a database that is not PostgreSQL-compatible to Aurora PostgreSQL.
  scope: migration from RDS for PostgreSQL or other sources to Aurora PostgreSQL.
  link: [AWS Database Migration Service (AWS DMS)](../facts/aurora.md#aurora-postgres-non-postgres-source-use-dms)
  link: [not PostgreSQL-compatible](../facts/aurora.md#aurora-postgres-non-postgres-source-use-dms)
aurora-postgres-promote-stop-write-workload-on-source
  claim: Before promoting the Aurora PostgreSQL replica, stop all database write workload on the source RDS for PostgreSQL DB instance.
  scope: migration from RDS for PostgreSQL or other sources to Aurora PostgreSQL.
  link: [Stop all database write workload on the source](../facts/aurora.md#aurora-postgres-promote-stop-write-workload-on-source)
  link: [RDS for PostgreSQL DB instance](../facts/aurora.md#aurora-postgres-promote-stop-write-workload-on-source)
aurora-postgres-promotion-unlinks-source
  claim: After promotion of the Aurora read replica is complete, the source RDS for PostgreSQL DB instance and the Aurora PostgreSQL DB cluster are unlinked.
  scope: migration from RDS for PostgreSQL or other sources to Aurora PostgreSQL.
  link: [are unlinked](../facts/aurora.md#aurora-postgres-promotion-unlinks-source)
  link: [After promotion is complete](../facts/aurora.md#aurora-postgres-promotion-unlinks-source)
aurora-postgres-rds-force-ssl-parameter
  claim: To require SSL/TLS connections to an Aurora PostgreSQL DB cluster, use the rds.force_ssl parameter.
  scope: Aurora PostgreSQL DB clusters, encryption in transit.
  link: [use `rds.force_ssl` parameter](../facts/aurora.md#aurora-postgres-rds-force-ssl-parameter)
  link: [require SSL/TLS connections](../facts/aurora.md#aurora-postgres-rds-force-ssl-parameter)
aurora-postgres-read-replica-migration-same-region-account
  claim: The Aurora read replica migration option for RDS for PostgreSQL is available only within the same AWS Region and account, and only if the Region offers a compatible version of Aurora PostgreSQL.
  scope: migration from RDS for PostgreSQL or other sources to Aurora PostgreSQL.
  link: [within the same AWS Region and account](../facts/aurora.md#aurora-postgres-read-replica-migration-same-region-account)
  link: [compatible version of Aurora PostgreSQL](../facts/aurora.md#aurora-postgres-read-replica-migration-same-region-account)
aurora-postgres-replica-independent-endpoint
  claim: An Aurora Replica is an independent endpoint in an Aurora DB cluster, best used for scaling read operations and increasing availability.
  scope: Aurora PostgreSQL Aurora Replicas.
  link: [scaling read operations and increasing availability](../facts/aurora.md#aurora-postgres-replica-independent-endpoint)
  link: [independent endpoint in an Aurora DB cluster](../facts/aurora.md#aurora-postgres-replica-independent-endpoint)
aurora-postgres-unused-connections-degrade-performance
  claim: If the max_connections value exceeds the number of connections that are actually needed, the unused connections can cause performance to degrade.
  scope: Aurora PostgreSQL max_connections setting.
  link: [unused connections can cause performance to degrade](../facts/aurora.md#aurora-postgres-unused-connections-degrade-performance)
aurora-postgres-write-forwarding-consistency-modes-default-session
  claim: For the apg_write_forward.consistency_mode parameter you can specify SESSION, EVENTUAL, GLOBAL, or OFF, and by default the value is SESSION.
  scope: per session, apg_write_forward.consistency_mode; default; adjustable.
  link: [`SESSION`, `EVENTUAL`, `GLOBAL`, or `OFF`](../facts/aurora.md#aurora-postgres-write-forwarding-consistency-modes-default-session)
  link: [By default, the value is set to `SESSION`](../facts/aurora.md#aurora-postgres-write-forwarding-consistency-modes-default-session)
aurora-postgres-write-forwarding-eventual-mode-may-be-stale
  claim: In EVENTUAL mode, results of write operations in the same session are not visible until the write is performed on the primary Region and replicated to the current Region, so queries might see slightly stale data.
  scope: Aurora PostgreSQL write forwarding.
  link: [aren't visible until the write operation is performed](../facts/aurora.md#aurora-postgres-write-forwarding-eventual-mode-may-be-stale)
  link: [replicated to the current Region](../facts/aurora.md#aurora-postgres-write-forwarding-eventual-mode-may-be-stale)
aurora-postgres-write-forwarding-global-mode-sees-all-committed
  claim: In GLOBAL mode, a query proceeds when the secondary cluster is up-to-date with all committed data from the primary cluster, as of the time that the query began.
  scope: Aurora PostgreSQL write forwarding.
  link: [up-to-date with all committed data](../facts/aurora.md#aurora-postgres-write-forwarding-global-mode-sees-all-committed)
  link: [as of the time that the query began](../facts/aurora.md#aurora-postgres-write-forwarding-global-mode-sees-all-committed)
aurora-postgres-write-forwarding-higher-consistency-more-waiting
  claim: As you increase the write forwarding consistency level, your application spends more time waiting for changes to be propagated between AWS Regions.
  scope: Aurora PostgreSQL write forwarding.
  link: [spends more time waiting](../facts/aurora.md#aurora-postgres-write-forwarding-higher-consistency-more-waiting)
  link: [increase the consistency level](../facts/aurora.md#aurora-postgres-write-forwarding-higher-consistency-more-waiting)
aurora-postgres-write-forwarding-read-only-transaction-not-forwarded
  claim: If the transaction access mode is set to read only, write forwarding is not used.
  scope: Aurora PostgreSQL write forwarding.
  link: [write forwarding isn't used](../facts/aurora.md#aurora-postgres-write-forwarding-read-only-transaction-not-forwarded)
  link: [transaction access mode is set to read only](../facts/aurora.md#aurora-postgres-write-forwarding-read-only-transaction-not-forwarded)
aurora-postgres-write-forwarding-session-mode-waits-for-own-writes
  claim: In SESSION mode, if necessary, the query waits for the results of forwarded write operations to be replicated to the current Region, but it does not wait for results of writes performed in other Regions or other sessions.
  scope: Aurora PostgreSQL write forwarding.
  link: [waits for the results of forwarded write operations](../facts/aurora.md#aurora-postgres-write-forwarding-session-mode-waits-for-own-writes)
  link: [doesn't wait for updated results](../facts/aurora.md#aurora-postgres-write-forwarding-session-mode-waits-for-own-writes)
aurora-postgres-write-forwarding-toggle-no-downtime
  claim: Enabling or disabling write forwarding does not cause downtime or a reboot.
  scope: Aurora PostgreSQL write forwarding.
  link: [doesn't cause downtime or a reboot](../facts/aurora.md#aurora-postgres-write-forwarding-toggle-no-downtime)
  link: [Enabling or disabling write forwarding](../facts/aurora.md#aurora-postgres-write-forwarding-toggle-no-downtime)
aurora-postgres-write-forwarding-version-support
  claim: In Aurora PostgreSQL version 16 and higher major versions, global write forwarding is supported in all minor versions.
  scope: Aurora PostgreSQL write forwarding.
  link: [supported in all minor versions](../facts/aurora.md#aurora-postgres-write-forwarding-version-support)
  link: [Aurora PostgreSQL version 16 and higher major versions](../facts/aurora.md#aurora-postgres-write-forwarding-version-support)
aurora-pricing-aurora-usage-eligible-database-savings-plans
  claim: Aurora usage may be eligible for Database Savings Plans, which give savings in exchange for a commitment to a specific amount of usage measured per hour over a 1-year term.
  scope: Database Savings Plans for Aurora.
  link: [over a 1-year term](../facts/aurora.md#aurora-pricing-aurora-usage-eligible-database-savings-plans)
aurora-pricing-backup-storage-definition
  claim: Aurora backup storage is the storage associated with automated database backups and customer-initiated database cluster snapshots.
  scope: Aurora backup storage.
  link: [customer-initiated database cluster snapshots](../facts/aurora.md#aurora-pricing-backup-storage-definition)
aurora-pricing-backup-storage-deleted-cluster-metered
  claim: For backups and snapshots beyond the free amount, including those from deleted clusters, Aurora backup usage is metered per GB-month.
  scope: Aurora backup storage beyond the free amount.
  link: [including those from deleted clusters](../facts/aurora.md#aurora-pricing-backup-storage-deleted-cluster-metered)
aurora-pricing-data-transfer-cross-az-ec2-charged
  claim: For data transferred between an Amazon EC2 instance and an Aurora DB instance in different Availability Zones of the same Region, Amazon EC2 Regional Data Transfer charges apply.
  scope: Aurora and EC2 in different Availability Zones.
  link: [Amazon EC2 Regional Data Transfer charges apply](../facts/aurora.md#aurora-pricing-data-transfer-cross-az-ec2-charged)
aurora-pricing-data-transfer-same-az-ec2-free
  claim: Data transferred between Aurora and Amazon EC2 instances in the same Availability Zone is free.
  scope: Aurora and EC2 in one Availability Zone.
  link: [in the same Availability Zone is free](../facts/aurora.md#aurora-pricing-data-transfer-same-az-ec2-free)
aurora-pricing-database-savings-plans-apply-to-serverless
  claim: Database Savings Plans apply automatically to the latest provisioned instance generations regardless of engine, instance family, size, Availability Zone or Region, and they also apply to serverless usage.
  scope: Database Savings Plans.
  link: [also apply to serverless usage](../facts/aurora.md#aurora-pricing-database-savings-plans-apply-to-serverless)
aurora-pricing-database-savings-plans-cover-aurora
  claim: Database Savings Plans reduce costs by up to 35% on Aurora and on RDS, DynamoDB, ElastiCache, DocumentDB, Timestream, Neptune, Keyspaces, DMS and Amazon OpenSearch Service.
  scope: Database Savings Plans.
  link: [reducing costs by up to 35% on Aurora](../facts/aurora.md#aurora-pricing-database-savings-plans-cover-aurora)
aurora-pricing-extended-support-end-enrollment-any-time
  claim: You can end enrollment in RDS Extended Support at any time.
  scope: RDS Extended Support enrollment; by changing the EngineLifecycleSupport parameter or by upgrading to an engine still under standard support.
  link: [end enrollment in RDS Extended Support](../facts/aurora.md#aurora-pricing-extended-support-end-enrollment-any-time)
aurora-pricing-extended-support-mysql-year-before-charges
  claim: Aurora MySQL-compatible customers have at least a year to migrate to a standard support version after community end of life before RDS Extended Support charges begin.
  scope: RDS Extended Support, Aurora MySQL; the pricing page says charges also depend on AWS Region and calendar date.
  link: [at least a year to migrate](../facts/aurora.md#aurora-pricing-extended-support-mysql-year-before-charges)
aurora-pricing-extended-support-new-old-version-databases-charged
  claim: You can create new databases with major engine versions that have reached the Aurora end of standard support date; Aurora automatically enrolls these new databases in RDS Extended Support and charges you for it, unless you disabled RDS Extended Support during creation or restoration.
  scope: new Aurora databases on a major engine version past the Aurora end of standard support date; enrollment happens if you didn't disable RDS Extended Support during creation or restoration.
  link: [charges you for this offering](../facts/aurora.md#aurora-pricing-extended-support-new-old-version-databases-charged)
aurora-pricing-extended-support-per-acu-hour
  claim: For Aurora serverless, RDS Extended Support is priced per Aurora Capacity Unit (ACU) per hour consumed by your database.
  scope: RDS Extended Support, Aurora serverless.
  link: [priced per Aurora Capacity Unit (ACU) per hour](../facts/aurora.md#aurora-pricing-extended-support-per-acu-hour)
aurora-pricing-extended-support-per-vcpu-hour
  claim: For provisioned instances on Amazon Aurora, RDS Extended Support is priced per vCPU per hour.
  scope: RDS Extended Support, provisioned Aurora instances.
  link: [priced per vCPU per hour](../facts/aurora.md#aurora-pricing-extended-support-per-vcpu-hour)
aurora-pricing-extended-support-purpose
  claim: Amazon RDS Extended Support lets you keep using Aurora MySQL-compatible and PostgreSQL-compatible major versions after the community end-of-life.
  scope: RDS Extended Support for Aurora.
  link: [Aurora MySQL-Compatible and PostgreSQL-Compatible Edition major versions](../facts/aurora.md#aurora-pricing-extended-support-purpose)
aurora-pricing-extended-support-up-to-three-years
  claim: During RDS Extended Support, AWS provides fixes for critical security issues and bugs through patch releases, which gives you up to three years to upgrade to a new major version.
  scope: RDS Extended Support for Aurora.
  link: [up to three years](../facts/aurora.md#aurora-pricing-extended-support-up-to-three-years)
  say: up to three years
aurora-pricing-global-db-other-billed-dimensions
  claim: Apart from replicated write I/Os, an Aurora global database is billed for instances, storage and I/O usage in the primary and secondary Regions, plus cross-Region data transfer, backup storage and other billable Aurora features.
  scope: Aurora Global Database.
  link: [cross-Region data transfer, backup storage](../facts/aurora.md#aurora-pricing-global-db-other-billed-dimensions)
aurora-pricing-global-db-replicated-write-io-between-regions
  claim: With Aurora Global Database you pay for replicated write I/O operations between the primary Region and each secondary Region.
  scope: Aurora Global Database.
  link: [pay for replicated write I/O operations](../facts/aurora.md#aurora-pricing-global-db-replicated-write-io-between-regions)
aurora-pricing-global-db-replicated-write-io-both-configurations
  claim: You pay for replicated write I/O operations with both the Aurora Standard and the Aurora I/O-Optimized configuration.
  scope: Aurora Global Database.
  link: [both Aurora Standard and Aurora I/O-Optimized configuration options](../facts/aurora.md#aurora-pricing-global-db-replicated-write-io-both-configurations)
aurora-pricing-global-db-replicated-writes-equal-primary-writes
  claim: The number of replicated write I/O operations to each secondary Region is the same as the number of in-Region write I/O operations performed by the primary Region.
  scope: Aurora Global Database, per secondary Region.
  link: [the number of in-Region write I/O operations](../facts/aurora.md#aurora-pricing-global-db-replicated-writes-equal-primary-writes)
aurora-pricing-limitless-billing-unit-acu-hours-shard-group
  claim: Aurora PostgreSQL Limitless Database provides on-demand capacity where the billing unit is Aurora capacity unit (ACU) hours in a DB shard group.
  scope: Aurora PostgreSQL Limitless Database.
  link: [(ACU) hours in a DB shard group](../facts/aurora.md#aurora-pricing-limitless-billing-unit-acu-hours-shard-group)
aurora-pricing-reserved-instances-apply-across-configurations
  claim: A Reserved Instance discounted rate is applied automatically to usage of any size in the same instance family, across the Aurora Standard and Aurora I/O-Optimized configurations.
  scope: Aurora provisioned Reserved Instances.
  link: [any size in the same instance family](../facts/aurora.md#aurora-pricing-reserved-instances-apply-across-configurations)
aurora-pricing-reserved-instances-exclude-storage
  claim: Aurora Reserved Instance prices do not cover storage costs.
  scope: Aurora provisioned Reserved Instances.
  link: [Reserved Instance prices do not cover storage costs](../facts/aurora.md#aurora-pricing-reserved-instances-exclude-storage)
aurora-pricing-reserved-instances-io-only-with-io-optimized
  claim: Read and write I/O costs are covered by Aurora Reserved Instances only when the cluster is configured as Aurora I/O-Optimized.
  scope: Aurora provisioned Reserved Instances.
  link: [only covered when your database cluster is configured](../facts/aurora.md#aurora-pricing-reserved-instances-io-only-with-io-optimized)
aurora-pricing-reserved-instances-steady-state
  claim: AWS says Reserved Instances are appropriate for steady-state database workloads and offer significant savings over On-Demand Instances.
  scope: Aurora provisioned Reserved Instances.
  link: [appropriate for steady-state database workloads](../facts/aurora.md#aurora-pricing-reserved-instances-steady-state)
aurora-pricing-snapshot-export-entire-cluster-charged
  claim: You are charged for exporting the entire Aurora DB cluster, whether you export all of the data or only part of it.
  scope: Aurora snapshot export.
  link: [whether you export all or partial data](../facts/aurora.md#aurora-pricing-snapshot-export-entire-cluster-charged)
aurora-pricing-snapshot-export-per-gigabyte
  claim: For all Aurora snapshots and cluster exports, usage is metered per gigabyte of snapshot data.
  scope: Aurora snapshot and cluster export.
  link: [metered per gigabyte of snapshot data](../facts/aurora.md#aurora-pricing-snapshot-export-per-gigabyte)
aurora-pricing-storage-billed-gb-month-both-configurations
  claim: Aurora storage is billed in per GB-month increments for both the Aurora Standard and the Aurora I/O-Optimized configurations.
  scope: Aurora storage.
  link: [billed in per GB-month increments](../facts/aurora.md#aurora-pricing-storage-billed-gb-month-both-configurations)
aurora-pricing-storage-io-not-provisioned-in-advance
  claim: With Aurora you do not provision storage or I/O operations in advance, and both scale automatically with the demands of the application.
  scope: Aurora storage and I/O.
  link: [provision either storage or I/O operations in advance](../facts/aurora.md#aurora-pricing-storage-io-not-provisioned-in-advance)
aurora-primary-created-in-subnet-group-subnet
  claim: When you create an Aurora DB cluster, Aurora creates the primary instance in one of the subnets in the VPC's DB subnet group.
  scope: Aurora DB clusters in a VPC.
  link: [in one of the subnets](../facts/aurora.md#aurora-primary-created-in-subnet-group-subnet)
  link: [VPC's DB subnet group](../facts/aurora.md#aurora-primary-created-in-subnet-group-subnet)
aurora-primary-handles-ddl-dml
  claim: The primary instance handles all data definition language (DDL) and data manipulation language (DML) statements.
  scope: Aurora DB cluster: primary instance and Aurora Replicas.
  link: [primary instance handles all data definition language](../facts/aurora.md#aurora-primary-handles-ddl-dml)
  link: [handles all data definition language (DDL)](../facts/aurora.md#aurora-primary-handles-ddl-dml)
aurora-private-ip-public-access-option
  claim: A DB cluster launched in a VPC has a private IP address for traffic inside the VPC, and that private IP address is not publicly accessible.
  scope: Aurora DB clusters in a VPC.
  link: [private IP address for traffic inside the VPC](../facts/aurora.md#aurora-private-ip-public-access-option)
  link: [isn't publicly accessible](../facts/aurora.md#aurora-private-ip-public-access-option)
aurora-promoting-replica-faster-than-new-primary
  claim: Promoting an Aurora Replica to the primary instance is much faster than creating a new primary instance.
  scope: Aurora DB cluster failover within one Region.
  link: [much faster than creating a new primary instance](../facts/aurora.md#aurora-promoting-replica-faster-than-new-primary)
  link: [Promoting an Aurora Replica](../facts/aurora.md#aurora-promoting-replica-faster-than-new-primary)
aurora-promotion-priority-highest-promoted-first
  claim: If the primary instance fails, Amazon RDS promotes the Aurora Replica with the highest priority to the new primary instance; priorities range from 0 for the highest priority to 15 for the lowest priority.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [promotes the Aurora Replica with the highest priority](../facts/aurora.md#aurora-promotion-priority-highest-promoted-first)
  link: [0 for the highest priority to 15 for the lowest priority](../facts/aurora.md#aurora-promotion-priority-highest-promoted-first)
aurora-promotion-priority-range
  claim: Aurora Replica promotion priorities range from 0 for the highest priority to 15 for the lowest priority.
  scope: per Aurora Replica.
  link: [0 for the highest priority to 15 for the lowest priority](../facts/aurora.md#aurora-promotion-priority-range)
  say: zero is the highest priority, fifteen is the lowest
aurora-promotion-tie-break-arbitrary
  claim: If two or more Aurora Replicas share the same priority and size, Amazon RDS promotes an arbitrary replica in the same promotion tier.
  scope: per Aurora DB cluster failover.
  link: [an arbitrary replica](../facts/aurora.md#aurora-promotion-tie-break-arbitrary)
aurora-promotion-tie-break-largest
  claim: If two or more Aurora Replicas share the same priority, Amazon RDS promotes the replica that is largest in size.
  scope: per Aurora DB cluster failover.
  link: [the replica that is largest in size](../facts/aurora.md#aurora-promotion-tie-break-largest)
aurora-promotion-tiers-ignored-after-five-failures
  claim: After five unsuccessful failover attempts, Aurora no longer considers promotion tiers when it picks a failover target.
  scope: per Aurora DB cluster failover.
  link: [five unsuccessful failover attempts](../facts/aurora.md#aurora-promotion-tiers-ignored-after-five-failures)
  say: five failed attempts
aurora-public-access-controlled-by-security-group
  claim: Access to an Aurora DB cluster is ultimately controlled by the security group it uses, and public access is not permitted if the security group has no inbound rules that permit it.
  scope: Aurora DB clusters in a VPC.
  link: [ultimately controlled by the security group it uses](../facts/aurora.md#aurora-public-access-controlled-by-security-group)
  link: [security group](../facts/aurora.md#aurora-public-access-controlled-by-security-group)
aurora-public-access-needs-all-public-subnets
  claim: For an Aurora DB cluster to be publicly accessible, all of the subnets in its DB subnet group must be public.
  scope: Aurora DB clusters in a VPC.
  link: [in its DB subnet group must be public](../facts/aurora.md#aurora-public-access-needs-all-public-subnets)
  link: [publicly accessible](../facts/aurora.md#aurora-public-access-needs-all-public-subnets)
aurora-quota-custom-endpoints-per-cluster
  claim: An account can create up to 5 custom endpoints per Aurora DB cluster in each supported Region by default. The quota can be adjusted through Service Quotas.
  scope: per Aurora DB cluster, per AWS Region, per account; default; adjustable.
  link: [5 custom endpoints](../facts/aurora.md#aurora-quota-custom-endpoints-per-cluster)
  say: five custom endpoints
aurora-quota-db-clusters-per-region
  claim: The default is 40 Aurora DB clusters allowed in an account in each supported Region, and the quota is adjustable.
  scope: per account, per AWS Region; default; adjustable.
  link: [40 Aurora DB clusters](../facts/aurora.md#aurora-quota-db-clusters-per-region)
  say: forty DB clusters
aurora-quota-db-instances-per-region
  claim: The default is 40 DB instances allowed in an account in each supported Region, except 20 in ap-south-1, and the quota is adjustable.
  scope: per account, per AWS Region; default; adjustable; ap-south-1 has a default of 20; each of the other supported Regions has 40.
  link: [40 DB instances](../facts/aurora.md#aurora-quota-db-instances-per-region)
  link: [ap-south-1: 20](../facts/aurora.md#aurora-quota-db-instances-per-region)
  say: forty DB instances
aurora-quota-iam-roles-per-cluster
  claim: The default is 5 IAM roles associated with a DB cluster in each supported Region, and the quota is adjustable.
  scope: per DB cluster, per AWS Region; default; adjustable.
  link: [5 IAM roles](../facts/aurora.md#aurora-quota-iam-roles-per-cluster)
  say: five IAM roles
aurora-quota-manual-cluster-snapshots
  claim: The default is 100 manual DB cluster snapshots in each supported Region, and the quota is adjustable.
  scope: per account, per AWS Region; default; adjustable.
  link: [100 manual DB cluster snapshots](../facts/aurora.md#aurora-quota-manual-cluster-snapshots)
  say: one hundred manual cluster snapshots
aurora-quota-rds-proxies-per-region
  claim: The default is 20 RDS proxies allowed in an account in each supported Region, and the quota is adjustable.
  scope: per account, per AWS Region; default; adjustable.
  link: [20 RDS proxies](../facts/aurora.md#aurora-quota-rds-proxies-per-region)
  say: twenty proxies
aurora-quota-read-replicas-per-primary
  claim: The default is 15 read replicas per primary DB instance in each supported Region, and AWS states that this quota cannot be adjusted for Amazon Aurora.
  scope: per primary DB instance, per AWS Region; maximum; not adjustable; for Amazon Aurora the quota cannot be adjusted, although the Adjustable column of the table says Yes.
  link: [15 read replicas](../facts/aurora.md#aurora-quota-read-replicas-per-primary)
  say: fifteen read replicas
aurora-quota-subnets-per-subnet-group
  claim: A DB subnet group can hold at most 20 subnets, and the quota cannot be adjusted.
  scope: per DB subnet group, per AWS Region; maximum; not adjustable.
  link: [20 subnets](../facts/aurora.md#aurora-quota-subnets-per-subnet-group)
  say: twenty subnets
aurora-rds-mysql-read-replica-for-migration
  claim: You can make an Aurora read replica of an RDS for MySQL DB instance, and you typically use this approach for migration to Aurora MySQL rather than for ongoing replication.
  scope: migration into Aurora.
  link: [migration to Aurora MySQL](../facts/aurora.md#aurora-rds-mysql-read-replica-for-migration)
  link: [rather than for ongoing replication](../facts/aurora.md#aurora-rds-mysql-read-replica-for-migration)
aurora-rds-postgres-read-replica-for-migration
  claim: You can make an Aurora read replica of an RDS for PostgreSQL DB instance, and you typically use this approach for migration to Aurora PostgreSQL rather than for ongoing replication.
  scope: migration into Aurora.
  link: [migration to Aurora PostgreSQL](../facts/aurora.md#aurora-rds-postgres-read-replica-for-migration)
  link: [rather than for ongoing replication](../facts/aurora.md#aurora-rds-postgres-read-replica-for-migration)
aurora-rds-proxy-connection-pool-reuse
  claim: RDS Proxy establishes a database connection pool and reuses connections in this pool, which avoids the memory and CPU overhead of opening a new database connection each time.
  scope: RDS Proxy with Aurora.
  link: [establishes a database connection pool and reuses connections](../facts/aurora.md#aurora-rds-proxy-connection-pool-reuse)
  link: [avoids the memory and CPU overhead](../facts/aurora.md#aurora-rds-proxy-connection-pool-reuse)
aurora-rds-proxy-failover-reduction-66-percent
  claim: RDS Proxy bypasses DNS caches to reduce failover times by up to 66% for Aurora Multi-AZ databases.
  scope: Aurora Multi-AZ databases using RDS Proxy; maximum.
  link: [up to 66%](../facts/aurora.md#aurora-rds-proxy-failover-reduction-66-percent)
  say: up to sixty-six percent
aurora-rds-proxy-reader-endpoint-reconnects-faster
  claim: Applications can reconnect more quickly to RDS Proxy read-only endpoints than to the Aurora reader endpoint if reader instances become unavailable.
  scope: RDS Proxy with Aurora.
  link: [reconnect more quickly to the proxy endpoints](../facts/aurora.md#aurora-rds-proxy-reader-endpoint-reconnects-faster)
  link: [than the Aurora reader endpoint](../facts/aurora.md#aurora-rds-proxy-reader-endpoint-reconnects-faster)
aurora-rds-responsible-hosting
  claim: Under the shared responsibility model, Amazon RDS is responsible for hosting the software components and infrastructure of DB instances and DB clusters.
  scope: Amazon Aurora overview.
  link: [hosting the software components and infrastructure](../facts/aurora.md#aurora-rds-responsible-hosting)
  link: [DB instances and DB clusters](../facts/aurora.md#aurora-rds-responsible-hosting)
aurora-reader-endpoint-balances-connections-not-queries
  claim: The reader endpoint balances connections to available Aurora Replicas, not individual queries.
  scope: Aurora reader endpoint.
  link: [balances connections to available Aurora Replicas](../facts/aurora.md#aurora-reader-endpoint-balances-connections-not-queries)
  link: [doesn't balance individual queries](../facts/aurora.md#aurora-reader-endpoint-balances-connections-not-queries)
aurora-reader-endpoint-balances-each-connection-read-only-session
  claim: If the cluster contains one or more Aurora Replicas, the reader endpoint balances each connection request among the Aurora Replicas, and in that session you can only run read-only statements such as SELECT.
  scope: Aurora reader endpoint.
  link: [balances each connection request among the Aurora Replicas](../facts/aurora.md#aurora-reader-endpoint-balances-each-connection-read-only-session)
  link: [only perform read-only statements](../facts/aurora.md#aurora-reader-endpoint-balances-each-connection-read-only-session)
aurora-reader-endpoint-balances-replicas
  claim: To run queries, you connect to the reader endpoint, and Aurora automatically balances connections among all the Aurora Replicas.
  scope: Aurora reader endpoint.
  link: [connect to the reader endpoint](../facts/aurora.md#aurora-reader-endpoint-balances-replicas)
  link: [connection-balancing among all the Aurora Replicas](../facts/aurora.md#aurora-reader-endpoint-balances-replicas)
aurora-reader-endpoint-builtin-cannot-modify
  claim: Each Aurora cluster has a single built-in reader endpoint whose name and attributes are managed by Aurora, and you cannot create, delete, or modify it.
  scope: Aurora reader endpoint.
  link: [single built-in reader endpoint](../facts/aurora.md#aurora-reader-endpoint-builtin-cannot-modify)
  link: [can't create, delete, or modify](../facts/aurora.md#aurora-reader-endpoint-builtin-cannot-modify)
aurora-reader-endpoint-connection-balancing-read-only
  claim: A reader endpoint for an Aurora DB cluster provides connection-balancing support for read-only connections to the DB cluster.
  scope: Aurora reader endpoint.
  link: [connection-balancing support for read-only connections](../facts/aurora.md#aurora-reader-endpoint-connection-balancing-read-only)
  link: [reader endpoint](../facts/aurora.md#aurora-reader-endpoint-connection-balancing-read-only)
aurora-reader-endpoint-may-point-to-new-primary-briefly
  claim: During a failover, the reader endpoint might direct connections to the new primary DB instance for a short time after an Aurora Replica is promoted.
  scope: Aurora reader endpoint.
  link: [direct connections to the new primary DB instance](../facts/aurora.md#aurora-reader-endpoint-may-point-to-new-primary-briefly)
  link: [for a short time](../facts/aurora.md#aurora-reader-endpoint-may-point-to-new-primary-briefly)
aurora-reader-endpoint-new-connection-per-query-to-balance
  claim: To balance each query across the read workload, open a new connection to the reader endpoint for each query.
  scope: Aurora reader endpoint.
  link: [connection to the reader endpoint for each query](../facts/aurora.md#aurora-reader-endpoint-new-connection-per-query-to-balance)
  link: [balance each query](../facts/aurora.md#aurora-reader-endpoint-new-connection-per-query-to-balance)
aurora-reader-endpoint-no-replica-goes-to-primary-writes-allowed
  claim: If the cluster contains only a primary instance and no Aurora Replicas, the reader endpoint connects to the primary instance, and you can perform write operations through it.
  scope: Aurora reader endpoint.
  link: [reader endpoint connects to the primary instance](../facts/aurora.md#aurora-reader-endpoint-no-replica-goes-to-primary-writes-allowed)
  link: [no Aurora Replicas](../facts/aurora.md#aurora-reader-endpoint-no-replica-goes-to-primary-writes-allowed)
aurora-reader-endpoint-reduces-primary-overhead-scales-selects
  claim: By processing read statements on the read-only Aurora Replicas, the reader endpoint reduces the overhead on the primary instance.
  scope: Aurora reader endpoint.
  link: [reduces the overhead on the primary instance](../facts/aurora.md#aurora-reader-endpoint-reduces-primary-overhead-scales-selects)
  link: [read-only Aurora Replicas](../facts/aurora.md#aurora-reader-endpoint-reduces-primary-overhead-scales-selects)
aurora-reader-takes-over-as-primary-failover
  claim: When a problem affects the primary instance, one of the reader instances takes over as the primary instance, a mechanism known as failover.
  scope: Aurora DB cluster failover within one Region.
  link: [takes over as the primary instance](../facts/aurora.md#aurora-reader-takes-over-as-primary-failover)
aurora-recommend-replica-in-two-azs
  claim: To increase availability, AWS recommends creating at least one or more Aurora Replicas in two or more different Availability Zones.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [at least one or more Aurora Replicas](../facts/aurora.md#aurora-recommend-replica-in-two-azs)
  link: [two or more different Availability Zones](../facts/aurora.md#aurora-recommend-replica-in-two-azs)
aurora-recovery-asynchronous-parallel-threads
  claim: Aurora recovers asynchronously on parallel threads, so the database is open and available immediately after an unplanned restart.
  scope: Aurora crash recovery and reliability.
  link: [recovers asynchronously on parallel threads](../facts/aurora.md#aurora-recovery-asynchronous-parallel-threads)
  link: [open and available immediately](../facts/aurora.md#aurora-recovery-asynchronous-parallel-threads)
aurora-recovery-from-restart-near-instant
  claim: Aurora is designed to recover from an unplanned restart almost instantaneously and continue to serve application data without the binary log.
  scope: Aurora crash recovery and reliability.
  link: [recover from an unplanned restart almost instantaneously](../facts/aurora.md#aurora-recovery-from-restart-near-instant)
  link: [without the binary log](../facts/aurora.md#aurora-recovery-from-restart-near-instant)
aurora-region-has-multiple-isolated-azs
  claim: Each AWS Region has multiple, isolated locations known as Availability Zones.
  scope: AWS Regions and Availability Zones for Aurora.
  link: [multiple, isolated locations known as Availability Zones](../facts/aurora.md#aurora-region-has-multiple-isolated-azs)
  link: [Each AWS Region](../facts/aurora.md#aurora-region-has-multiple-isolated-azs)
aurora-regions-independent-activity-current-region
  claim: Each AWS Region is completely independent, and any Amazon RDS activity you initiate, such as creating database instances, runs only in your current default AWS Region.
  scope: AWS Regions and Availability Zones for Aurora.
  link: [each AWS Region is completely independent](../facts/aurora.md#aurora-regions-independent-activity-current-region)
  link: [runs only in your current default AWS Region](../facts/aurora.md#aurora-regions-independent-activity-current-region)
aurora-reliable-durable-fault-tolerant
  claim: Aurora is designed to be reliable, durable, and fault tolerant.
  scope: Aurora crash recovery and reliability.
  link: [reliable, durable, and fault tolerant](../facts/aurora.md#aurora-reliable-durable-fault-tolerant)
  link: [designed to be reliable](../facts/aurora.md#aurora-reliable-durable-fault-tolerant)
aurora-remove-instance-keeps-data
  claim: You can remove a DB instance from an Aurora cluster without removing any of the underlying data, and Aurora removes the data only when you delete the entire cluster.
  scope: deleting Aurora DB instances and clusters.
  link: [without removing any of the underlying data](../facts/aurora.md#aurora-remove-instance-keeps-data)
  link: [delete the entire cluster](../facts/aurora.md#aurora-remove-instance-keeps-data)
aurora-replica-encryption-must-match-cluster
  claim: You cannot create an encrypted Aurora Replica for an unencrypted Aurora DB cluster, and you cannot create an unencrypted Aurora Replica for an encrypted Aurora DB cluster.
  scope: Aurora encryption at rest with AWS KMS.
  link: [can't create an encrypted Aurora Replica](../facts/aurora.md#aurora-replica-encryption-must-match-cluster)
  link: [can't create an unencrypted Aurora Replica](../facts/aurora.md#aurora-replica-encryption-must-match-cluster)
aurora-replica-failover-priority-specify
  claim: You can specify the failover priority for Aurora Replicas.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [specify the failover priority](../facts/aurora.md#aurora-replica-failover-priority-specify)
  link: [failover priority for Aurora Replicas](../facts/aurora.md#aurora-replica-failover-priority-specify)
aurora-replica-lag-under-100-ms
  claim: Aurora Replica lag is usually much less than 100 milliseconds after the primary instance has written an update, and replica lag varies depending on the rate of database change.
  scope: per Aurora DB cluster (Aurora Replicas in the same Region); typical value; replica lag varies depending on the rate of database change.
  link: [much less than 100 milliseconds](../facts/aurora.md#aurora-replica-lag-under-100-ms)
  say: well under a hundred milliseconds
aurora-replica-lag-varies-with-write-rate
  claim: Aurora replica lag varies depending on the rate of database change, so a large amount of write operations can increase it.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [varies depending on the rate of database change](../facts/aurora.md#aurora-replica-lag-varies-with-write-rate)
  link: [increase in replica lag](../facts/aurora.md#aurora-replica-lag-varies-with-write-rate)
aurora-replica-promoted-if-writer-unavailable
  claim: If the writer instance in a cluster becomes unavailable, Aurora automatically promotes one of the reader instances to be the new writer.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [automatically promotes one of the reader instances](../facts/aurora.md#aurora-replica-promoted-if-writer-unavailable)
  link: [new writer](../facts/aurora.md#aurora-replica-promoted-if-writer-unavailable)
aurora-replica-recommend-same-class-different-az
  claim: For high availability, AWS recommends creating one or more Aurora Replicas of the same DB instance class as the primary instance, in different Availability Zones.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [same DB instance class as the primary instance](../facts/aurora.md#aurora-replica-recommend-same-class-different-az)
  link: [in different Availability Zones](../facts/aurora.md#aurora-replica-recommend-same-class-different-az)
aurora-replicas-asynchronous-replication-no-primary-impact
  claim: Aurora Replicas use asynchronous replication to support high availability without affecting primary instance performance.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [use asynchronous replication](../facts/aurora.md#aurora-replicas-asynchronous-replication-no-primary-impact)
  link: [without affecting primary instance performance](../facts/aurora.md#aurora-replicas-asynchronous-replication-no-primary-impact)
aurora-replicas-can-be-only-replication
  claim: You can use Aurora Replicas within an Aurora cluster as your only form of replication to keep your data highly available, or combine them with other types of replication.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [as your only form of replication](../facts/aurora.md#aurora-replicas-can-be-only-replication)
  link: [keep your data highly available](../facts/aurora.md#aurora-replicas-can-be-only-replication)
aurora-replicas-dedicated-reads-shared-volume-little-copy-work
  claim: Because the cluster volume is shared among all DB instances in the DB cluster, minimal additional work is required to replicate a copy of the data for each Aurora Replica.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [cluster volume is shared among all DB instances](../facts/aurora.md#aurora-replicas-dedicated-reads-shared-volume-little-copy-work)
  link: [minimal additional work is required](../facts/aurora.md#aurora-replicas-dedicated-reads-shared-volume-little-copy-work)
aurora-replicas-max-per-cluster
  claim: After you create the primary (writer) instance, you can create up to 15 read-only Aurora Replicas in an Aurora DB cluster.
  scope: per Aurora DB cluster; maximum; not adjustable; the read replicas per primary quota cannot be adjusted for Amazon Aurora.
  link: [up to 15 read-only Aurora Replicas](../facts/aurora.md#aurora-replicas-max-per-cluster)
  say: fifteen Aurora Replicas
aurora-replicas-need-not-match-primary-instance-class
  claim: Aurora Replicas do not have to be of the same DB instance class as the primary instance, although AWS recommends the same class for high-availability replicas.
  scope: per Aurora Replica.
  link: [don't have to be of the same](../facts/aurora.md#aurora-replicas-need-not-match-primary-instance-class)
aurora-replicas-offload-reads
  claim: Aurora Replicas can offload read workloads from the primary DB instance.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [offload read workloads](../facts/aurora.md#aurora-replicas-offload-reads)
  link: [from the primary DB instance](../facts/aurora.md#aurora-replicas-offload-reads)
aurora-replicas-read-only-auto-replication
  claim: When you add a second or later DB instance to an Aurora provisioned DB cluster, those other DB instances are read-only and are known as Aurora Replicas.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [read-only and are known as Aurora Replicas](../facts/aurora.md#aurora-replicas-read-only-auto-replication)
  link: [known as Aurora Replicas](../facts/aurora.md#aurora-replicas-read-only-auto-replication)
aurora-replicas-return-same-data-minimal-lag
  claim: All Aurora Replicas return the same data for query results with minimal replica lag.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [return the same data for query results](../facts/aurora.md#aurora-replicas-return-same-data-minimal-lag)
  link: [minimal replica lag](../facts/aurora.md#aurora-replicas-return-same-data-minimal-lag)
aurora-replicas-separate-azs-for-ha
  claim: To maintain high availability, locate Aurora Replicas in separate Availability Zones.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [locating Aurora Replicas in separate Availability Zones](../facts/aurora.md#aurora-replicas-separate-azs-for-ha)
  link: [Maintain high availability](../facts/aurora.md#aurora-replicas-separate-azs-for-ha)
aurora-replicas-spread-across-azs-of-cluster
  claim: Aurora Replicas can be distributed across the Availability Zones that a DB cluster spans within an AWS Region.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [distributed across the Availability Zones](../facts/aurora.md#aurora-replicas-spread-across-azs-of-cluster)
  link: [within an AWS Region](../facts/aurora.md#aurora-replicas-spread-across-azs-of-cluster)
aurora-replicas-two-purposes-read-scale-availability
  claim: Aurora Replicas have two main purposes: scaling read operations by issuing queries to them, and increasing availability.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [two main purposes](../facts/aurora.md#aurora-replicas-two-purposes-read-scale-availability)
  link: [scale the read operations for your application](../facts/aurora.md#aurora-replicas-two-purposes-read-scale-availability)
aurora-replicas-up-to-15-in-addition-to-primary
  claim: Each Aurora DB cluster can have up to 15 Aurora Replicas in addition to the primary DB instance.
  scope: per Aurora DB cluster; maximum; not adjustable; the read replicas per primary quota cannot be adjusted for Amazon Aurora.
  link: [up to 15 Aurora Replicas in addition to the primary DB instance](../facts/aurora.md#aurora-replicas-up-to-15-in-addition-to-primary)
  say: fifteen Aurora Replicas besides the primary
aurora-replication-independent-of-instance-count
  claim: The amount of replication of Aurora data is independent of the number of DB instances in the cluster.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [independent of the number of DB instances](../facts/aurora.md#aurora-replication-independent-of-instance-count)
  link: [The amount of replication](../facts/aurora.md#aurora-replication-independent-of-instance-count)
aurora-reserved-instance-all-upfront-full-payment
  claim: With the All Upfront option, full payment is made at the start of the term, with no other costs incurred for the remainder of the term regardless of the number of hours used.
  scope: Aurora DB instance billing and reserved DB instances.
  link: [Full payment is made at the start](../facts/aurora.md#aurora-reserved-instance-all-upfront-full-payment)
  link: [no other costs incurred](../facts/aurora.md#aurora-reserved-instance-all-upfront-full-payment)
aurora-reserved-instance-billing-discount-not-physical
  claim: Reserved DB instances are not physical instances, but a billing discount applied to the use of certain on-demand DB instances in your account.
  scope: Aurora DB instance billing and reserved DB instances.
  link: [not physical instances, but rather a billing discount](../facts/aurora.md#aurora-reserved-instance-billing-discount-not-physical)
aurora-reserved-instance-both-storage-configurations
  claim: Aurora reserved DB instances can be used with both Aurora I/O-Optimized and Aurora Standard clusters, and Aurora automatically accounts for the price difference between these configurations.
  scope: Aurora DB instance billing and reserved DB instances.
  link: [with both DB cluster configurations](../facts/aurora.md#aurora-reserved-instance-both-storage-configurations)
  link: [automatically accounts for the price difference](../facts/aurora.md#aurora-reserved-instance-both-storage-configurations)
aurora-reserved-instance-consolidated-billing-shared
  claim: If you are using consolidated billing, all accounts in the organization can receive the hourly cost benefit of reserved DB instances purchased by any other account.
  scope: Aurora DB instance billing and reserved DB instances.
  link: [all accounts in the organization](../facts/aurora.md#aurora-reserved-instance-consolidated-billing-shared)
  link: [purchased by any other account](../facts/aurora.md#aurora-reserved-instance-consolidated-billing-shared)
aurora-reserved-instance-discount-up-to-45-and-66-percent
  claim: Aurora 1-year Reserved Instances provide discounts up to 45% and 3-year Reserved Instances provide discounts of up to 66% over On-Demand Instances.
  scope: per Aurora provisioned instance; maximum.
  link: [up to 45%](../facts/aurora.md#aurora-reserved-instance-discount-up-to-45-and-66-percent)
  link: [up to 66%](../facts/aurora.md#aurora-reserved-instance-discount-up-to-45-and-66-percent)
  say: up to forty-five percent | up to sixty-six percent
aurora-reserved-instance-io-optimized-30-percent-more-units
  claim: Aurora I/O-Optimized consumes 30% more normalized units per hour than Aurora Standard for reserved DB instances.
  scope: per reserved DB instance, normalized units per hour; fixed.
  link: [30% more normalized units per hour](../facts/aurora.md#aurora-reserved-instance-io-optimized-30-percent-more-units)
  link: [Aurora I/O-Optimized consumes](../facts/aurora.md#aurora-reserved-instance-io-optimized-30-percent-more-units)
aurora-reserved-instance-no-upfront-one-year-only
  claim: The No Upfront reserved DB instance option is available only as a one-year reservation.
  scope: Aurora DB instance billing and reserved DB instances.
  link: [only available as a one-year reservation](../facts/aurora.md#aurora-reserved-instance-no-upfront-one-year-only)
  link: [No Upfront](../facts/aurora.md#aurora-reserved-instance-no-upfront-one-year-only)
aurora-reserved-instance-one-or-three-year-term
  claim: Using reserved DB instances, you can reserve an Aurora DB instance for a one- or three-year term.
  scope: Aurora DB instance billing and reserved DB instances.
  link: [one- or three-year term](../facts/aurora.md#aurora-reserved-instance-one-or-three-year-term)
aurora-reserved-instance-size-flexible-within-class-type
  claim: Size-flexible reserved DB instances are automatically applied across all DB instance class sizes, but can only scale in their instance class type.
  scope: Aurora DB instance billing and reserved DB instances.
  link: [can only scale in their instance class type](../facts/aurora.md#aurora-reserved-instance-size-flexible-within-class-type)
  link: [applied across all DB instance class sizes](../facts/aurora.md#aurora-reserved-instance-size-flexible-within-class-type)
aurora-reserved-instance-tied-to-type-and-region
  claim: Discounts for reserved DB instances are tied to instance type and AWS Region.
  scope: Aurora DB instance billing and reserved DB instances.
  link: [tied to instance type and AWS Region](../facts/aurora.md#aurora-reserved-instance-tied-to-type-and-region)
  link: [Discounts for reserved DB instances](../facts/aurora.md#aurora-reserved-instance-tied-to-type-and-region)
aurora-resources-not-auto-replicated-across-regions
  claim: AWS Regions are isolated from each other, and AWS does not automatically replicate resources across Regions.
  scope: AWS Regions and Availability Zones for Aurora.
  link: [we don't automatically replicate resources across AWS Regions](../facts/aurora.md#aurora-resources-not-auto-replicated-across-regions)
  link: [AWS Regions are isolated from each other](../facts/aurora.md#aurora-resources-not-auto-replicated-across-regions)
aurora-restart-faster-than-failover
  claim: Restarting is faster and involves less overhead than failover, so the fastest path to recovery is often to restart or to fail over to the same DB instance.
  scope: Aurora DB cluster failover within one Region.
  link: [Restarting is faster](../facts/aurora.md#aurora-restart-faster-than-failover)
  link: [less overhead than failover](../facts/aurora.md#aurora-restart-faster-than-failover)
aurora-restore-always-creates-new-cluster
  claim: You cannot restore from a DB cluster snapshot to an existing DB cluster; a new DB cluster is created when you restore.
  scope: restoring an Aurora DB cluster from a snapshot.
  link: [a new DB cluster is created](../facts/aurora.md#aurora-restore-always-creates-new-cluster)
  link: [can't restore from a DB cluster snapshot](../facts/aurora.md#aurora-restore-always-creates-new-cluster)
aurora-restore-cli-api-must-create-primary-instance
  claim: If you use the AWS CLI to restore a DB cluster, you must explicitly create the primary instance for your DB cluster; the console creates the primary DB instance automatically.
  scope: restoring an Aurora DB cluster from a snapshot.
  link: [you must explicitly create the primary instance](../facts/aurora.md#aurora-restore-cli-api-must-create-primary-instance)
  link: [restore a DB cluster](../facts/aurora.md#aurora-restore-cli-api-must-create-primary-instance)
aurora-restore-inherits-retention-period
  claim: When you do not explicitly set the backup retention period during a restore, the restored cluster inherits it from the source snapshot or cluster.
  scope: per restored Aurora DB cluster; default; not adjustable.
  link: [restored cluster inherits the backup retention period](../facts/aurora.md#aurora-restore-inherits-retention-period)
  link: [from the source snapshot or cluster](../facts/aurora.md#aurora-restore-inherits-retention-period)
aurora-restore-snapshot-whole-cluster
  claim: A DB cluster snapshot is a storage volume snapshot that backs up the entire DB cluster and not just individual databases.
  scope: restoring an Aurora DB cluster from a snapshot.
  link: [backing up the entire DB cluster](../facts/aurora.md#aurora-restore-snapshot-whole-cluster)
  link: [not just individual databases](../facts/aurora.md#aurora-restore-snapshot-whole-cluster)
aurora-restore-unencrypted-snapshot-specify-kms-key
  claim: To restore an unencrypted snapshot to an encrypted Aurora DB cluster, specify a KMS key when you restore from the unencrypted snapshot.
  scope: restoring an Aurora DB cluster from a snapshot.
  link: [specify a KMS key when you restore](../facts/aurora.md#aurora-restore-unencrypted-snapshot-specify-kms-key)
  link: [unencrypted snapshot](../facts/aurora.md#aurora-restore-unencrypted-snapshot-specify-kms-key)
aurora-restore-without-primary-endpoints-creating
  claim: If you do not create the primary DB instance after a restore, the DB cluster endpoints remain in the creating status.
  scope: restoring an Aurora DB cluster from a snapshot.
  link: [DB cluster endpoints remain in the `creating` status](../facts/aurora.md#aurora-restore-without-primary-endpoints-creating)
  link: [don't create the primary DB instance](../facts/aurora.md#aurora-restore-without-primary-endpoints-creating)
aurora-retain-automated-backups-after-delete
  claim: When you delete a provisioned or Aurora serverless DB cluster, you can retain automated backups, which lets you restore to a point in time within the backup retention period even after the cluster is deleted.
  scope: Aurora automated backups.
  link: [you can retain automated backups](../facts/aurora.md#aurora-retain-automated-backups-after-delete)
  link: [even after the cluster is deleted](../facts/aurora.md#aurora-retain-automated-backups-after-delete)
aurora-revoke-kms-access-does-not-affect-running-db
  claim: Revoking the calling principal's access to the KMS key does not affect a running Aurora database, but disabling the key impacts all DB clusters encrypted with that key.
  scope: Aurora encryption at rest with AWS KMS.
  link: [does not affect a running database](../facts/aurora.md#aurora-revoke-kms-access-does-not-affect-running-db)
aurora-sec-blue-green-encrypt-existing-cluster
  claim: A blue/green deployment can create a green environment encrypted with a different KMS key, which lets you encrypt an unencrypted Aurora DB cluster or change the KMS key of an encrypted one.
  scope: Aurora DB cluster encryption; a blue/green deployment; the other route is a snapshot restore with encryption turned on.
  link: [encrypt an unencrypted DB cluster](../facts/aurora.md#aurora-sec-blue-green-encrypt-existing-cluster)
aurora-sec-iam-controls-management-actions
  claim: AWS IAM controls who can perform Amazon RDS management actions on Aurora DB clusters and DB instances.
  scope: Aurora security, management actions; first of three levels of Aurora security.
  link: [you use AWS Identity and Access Management (IAM)](../facts/aurora.md#aurora-sec-iam-controls-management-actions)
aurora-security-group-default-deny
  claim: When you first create a DB cluster, its firewall prevents any database access except through rules specified by an associated security group.
  scope: per newly created DB cluster; default; not adjustable.
  link: [firewall prevents any database access](../facts/aurora.md#aurora-security-group-default-deny)
  link: [rules specified by an associated security group](../facts/aurora.md#aurora-security-group-default-deny)
aurora-security-iam-db-auth-user-or-role-token
  claim: By using IAM database authentication, you can use the same credentials to control access to your AWS resources and your databases.
  scope: IAM database authentication for Aurora.
  link: [same credentials to control access](../facts/aurora.md#aurora-security-iam-db-auth-user-or-role-token)
  link: [IAM database authentication](../facts/aurora.md#aurora-security-iam-db-auth-user-or-role-token)
aurora-security-kerberos-with-directory-service
  claim: For Kerberos authentication, an Aurora DB cluster works with AWS Directory Service for Microsoft Active Directory.
  scope: Kerberos authentication for Aurora.
  link: [AWS Directory Service for Microsoft Active Directory](../facts/aurora.md#aurora-security-kerberos-with-directory-service)
  link: [enable Kerberos authentication](../facts/aurora.md#aurora-security-kerberos-with-directory-service)
aurora-security-vpc-required-security-group
  claim: Aurora DB clusters must be created in a virtual private cloud (VPC) based on the Amazon VPC service, and a VPC security group controls which devices and EC2 instances can open connections to the endpoint and port of the DB instance.
  scope: Aurora DB clusters in a VPC.
  link: [must be created in a virtual private cloud](../facts/aurora.md#aurora-security-vpc-required-security-group)
  link: [VPC security group](../facts/aurora.md#aurora-security-vpc-required-security-group)
aurora-separates-compute-and-storage
  claim: An Aurora DB cluster separates compute capacity from storage.
  scope: Aurora cluster volume (shared storage).
  link: [separation of compute capacity and storage](../facts/aurora.md#aurora-separates-compute-and-storage)
  link: [compute capacity and storage](../facts/aurora.md#aurora-separates-compute-and-storage)
aurora-serverless-acu-about-2-gib-memory
  claim: Each Aurora capacity unit (ACU) is a combination of approximately 2 gibibytes (GiB) of memory, corresponding CPU, and networking.
  scope: per ACU of Aurora Serverless; fixed; not adjustable.
  link: [approximately 2 gibibytes (GiB) of memory](../facts/aurora-serverless.md#aurora-serverless-acu-about-2-gib-memory)
  say: about two gibibytes of memory
aurora-serverless-auto-pause-after-no-connections
  claim: Aurora serverless DB instances can automatically pause after a period with no user connections, and automatically resume when a connection request arrives.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [pause after a period with no user connections](../facts/aurora-serverless.md#aurora-serverless-auto-pause-after-no-connections)
  link: [automatically resume when a connection request arrives](../facts/aurora-serverless.md#aurora-serverless-auto-pause-after-no-connections)
aurora-serverless-auto-pause-billing-storage-still-charged
  claim: While an Aurora Serverless instance is auto-paused, its instance charge is zero, but AWS still charges for Aurora storage and other aspects of the cluster that are not tied to that DB instance.
  scope: per auto-paused Aurora Serverless instance.
  link: [instance charge is zero](../facts/aurora-serverless.md#aurora-serverless-auto-pause-billing-storage-still-charged)
aurora-serverless-auto-pause-deeper-sleep-after-24-hours
  claim: If an Aurora Serverless instance remains paused more than 24 hours, Aurora can put it into a deeper sleep, and the resume time can be 30 seconds or longer.
  scope: per auto-paused Aurora Serverless instance paused more than 24 hours.
  link: [30 seconds or longer](../facts/aurora-serverless.md#aurora-serverless-auto-pause-deeper-sleep-after-24-hours)
  say: thirty seconds or longer
aurora-serverless-auto-pause-faster-resume-than-stop-start
  claim: Auto-pause for Aurora serverless resumes faster than starting a stopped cluster and automates the process of determining when to pause and resume each DB instance.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [a faster resume than starting a stopped cluster](../facts/aurora-serverless.md#aurora-serverless-auto-pause-faster-resume-than-stop-start)
aurora-serverless-auto-pause-for-systems-without-strict-slo
  claim: The Aurora serverless automatic pause and resume feature helps manage costs for systems that do not have a stringent service level objective (SLO).
  scope: Aurora serverless auto-pause; for example development and test clusters, or internal applications where a brief pause is acceptable.
  link: [don't have a stringent service level objective](../facts/aurora-serverless.md#aurora-serverless-auto-pause-for-systems-without-strict-slo)
aurora-serverless-auto-pause-min-capacity-zero
  claim: To enable auto-pause for all the Aurora serverless DB instances in a cluster, you set the minimum capacity value for the cluster to zero ACUs.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [for the cluster to zero ACUs](../facts/aurora-serverless.md#aurora-serverless-auto-pause-min-capacity-zero)
  link: [enable the auto-pause behavior](../facts/aurora-serverless.md#aurora-serverless-auto-pause-min-capacity-zero)
aurora-serverless-auto-pause-no-compute-charge-while-paused
  claim: You are not charged for Aurora serverless instance capacity while an instance is in the paused state.
  scope: paused Aurora serverless instance; storage is still charged.
  link: [aren't charged for instance capacity](../facts/aurora-serverless.md#aurora-serverless-auto-pause-no-compute-charge-while-paused)
aurora-serverless-auto-pause-resume-about-15-seconds
  claim: A paused Aurora Serverless instance typically resumes in approximately 15 seconds, so AWS recommends that client timeout settings be longer than 15 seconds.
  scope: per auto-paused Aurora Serverless instance; typical value.
  link: [approximately 15 seconds](../facts/aurora-serverless.md#aurora-serverless-auto-pause-resume-about-15-seconds)
  say: about fifteen seconds
aurora-serverless-auto-pause-timeout-range
  claim: The auto-pause interval of Aurora Serverless can be set from a minimum of 300 seconds (five minutes), which is also the default, up to a maximum of 86,400 seconds (one day).
  scope: per Aurora Serverless cluster with a minimum capacity of 0 ACUs; default; adjustable; the minimum, 300 seconds, is also the default.
  link: [300 seconds (five minutes)](../facts/aurora-serverless.md#aurora-serverless-auto-pause-timeout-range)
  link: [86,400 seconds (one day)](../facts/aurora-serverless.md#aurora-serverless-auto-pause-timeout-range)
  say: five minutes | one day
aurora-serverless-auto-pause-tolerate-slight-connection-delay
  claim: If a workload has periods of inactivity and can tolerate slight delays in connecting while the instance resumes, AWS suggests using auto-pause with Aurora serverless instances to reduce costs.
  scope: Aurora serverless auto-pause.
  link: [tolerate slight delays in connecting](../facts/aurora-serverless.md#aurora-serverless-auto-pause-tolerate-slight-connection-delay)
aurora-serverless-auto-pause-writer-and-tier-0-1-pause-together
  claim: The writer instance and all reader instances with failover priority 0 and 1 always pause and resume at the same time.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [failover priority 0 and 1 always pause and resume at the same time](../facts/aurora-serverless.md#aurora-serverless-auto-pause-writer-and-tier-0-1-pause-together)
  link: [writer instances and all reader instances](../facts/aurora-serverless.md#aurora-serverless-auto-pause-writer-and-tier-0-1-pause-together)
aurora-serverless-billing-unit-acu-hours
  claim: The charges for Aurora serverless capacity are measured in terms of ACU-hours.
  scope: Aurora serverless.
  link: [measured in terms of ACU-hours](../facts/aurora-serverless.md#aurora-serverless-billing-unit-acu-hours)
  say: measured in ACU-hours
aurora-serverless-binlog-or-logical-replication-blocks-pause
  claim: In an Aurora PostgreSQL cluster that has logical replication enabled, or an Aurora MySQL cluster that has binlog replication enabled, the writer instance and any reader instances in failover promotion tiers zero and one do not automatically pause.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [logical replication enabled](../facts/aurora-serverless.md#aurora-serverless-binlog-or-logical-replication-blocks-pause)
  link: [binlog replication enabled](../facts/aurora-serverless.md#aurora-serverless-binlog-or-logical-replication-blocks-pause)
aurora-serverless-capacity-range-0-256-acu-half-acu-steps
  claim: Aurora Serverless capacity ranges from a minimum of 0 Aurora capacity units (ACU) to a maximum of 256 ACUs, in increments of 0.5 ACU. The allowed minimum value depends on the Aurora version.
  scope: per Aurora cluster with Aurora Serverless DB instances; maximum; adjustable; the allowed minimum value depends on the Aurora version; 0 ACU needs a version that supports auto-pause.
  link: [maximum of 256 ACUs](../facts/aurora-serverless.md#aurora-serverless-capacity-range-0-256-acu-half-acu-steps)
  link: [minimum of 0 Aurora capacity units (ACU)](../facts/aurora-serverless.md#aurora-serverless-capacity-range-0-256-acu-half-acu-steps)
  link: [increments of 0.5 ACU](../facts/aurora-serverless.md#aurora-serverless-capacity-range-0-256-acu-half-acu-steps)
  say: two hundred fifty-six ACUs | zero ACUs | half-ACU steps
aurora-serverless-capacity-range-0-256-needs-mysql-3-08-postgresql-16-3
  claim: The 0–256 ACUs capacity range, which allows scaling to 0 ACUs, needs Aurora MySQL 3.08.0 and higher, or Aurora PostgreSQL 13.15 and higher, 14.12 and higher, 15.7 and higher, or 16.3 and higher.
  scope: per Aurora Serverless cluster, by engine version.
  link: [0–256 ACUs](../facts/aurora-serverless.md#aurora-serverless-capacity-range-0-256-needs-mysql-3-08-postgresql-16-3)
aurora-serverless-capacity-range-0-5-128-needs-mysql-3-02-postgresql-16-1
  claim: The 0.5–128 ACUs capacity range needs Aurora MySQL 3.02.0 and higher, or Aurora PostgreSQL 13.6 and higher, 14.3 and higher, 15.2 and higher, or 16.1 and higher.
  scope: per Aurora Serverless cluster, by engine version.
  link: [0.5–128 ACUs](../facts/aurora-serverless.md#aurora-serverless-capacity-range-0-5-128-needs-mysql-3-02-postgresql-16-1)
aurora-serverless-capacity-range-0-5-256-needs-mysql-3-06-postgresql-16-1
  claim: The 0.5–256 ACUs capacity range needs Aurora MySQL 3.06.0 and higher, or Aurora PostgreSQL 13.13 and higher, 14.10 and higher, 15.5 and higher, or 16.1 and higher.
  scope: per Aurora Serverless cluster, by engine version.
  link: [0.5–256 ACUs](../facts/aurora-serverless.md#aurora-serverless-capacity-range-0-5-256-needs-mysql-3-06-postgresql-16-1)
aurora-serverless-capacity-range-set-with-first-instance-applies-to-all
  claim: You set the Aurora serverless capacity range, which applies to all the DB instances in the DB cluster, at the same time that you add the first Aurora serverless DB instance to the cluster.
  scope: Aurora serverless capacity range and scaling.
  link: [applies to all the DB instances](../facts/aurora-serverless.md#aurora-serverless-capacity-range-set-with-first-instance-applies-to-all)
  link: [add the first Aurora serverless DB instance](../facts/aurora-serverless.md#aurora-serverless-capacity-range-set-with-first-instance-applies-to-all)
aurora-serverless-capacity-scales-within-range-mix-with-provisioned
  claim: Aurora serverless capacity increases and decreases, within a range that you specify, depending on the load on your database, and you can configure a combination of Aurora serverless and on-demand or reserved provisioned instances.
  scope: Aurora serverless capacity range and scaling.
  link: [within a range that you specify](../facts/aurora-serverless.md#aurora-serverless-capacity-scales-within-range-mix-with-provisioned)
  link: [depending on the load on your database](../facts/aurora-serverless.md#aurora-serverless-capacity-scales-within-range-mix-with-provisioned)
aurora-serverless-case-bmw-before-serverless-ran-at-maximum
  claim: The AWS case study says that to account for usage spikes, BMW previously had to run workloads at maximum settings throughout the day, which incurred significant costs.
  scope: customer case study on the AWS site; a customer statement published by AWS, not a service guarantee.
  link: [run workloads at maximum settings throughout the day](../facts/aurora-serverless.md#aurora-serverless-case-bmw-before-serverless-ran-at-maximum)
aurora-serverless-case-bmw-outcomes-uptime-scalability-costs
  claim: The AWS case study says BMW achieved 99.99 percent uptime, increased scalability, reduced costs, and freed up developers' time to focus on innovation.
  scope: customer case study on the AWS site; a customer statement published by AWS, not a service guarantee.
  link: [achieved 99.99 percent uptime](../facts/aurora-serverless.md#aurora-serverless-case-bmw-outcomes-uptime-scalability-costs)
aurora-serverless-case-bmw-serverless-v2-automated-capacity-peaks
  claim: The AWS case study says that using Aurora Serverless v2, BMW has automated management of its database capacity and can scale to accommodate peaks on demand.
  scope: customer case study on the AWS site; a customer statement published by AWS, not a service guarantee.
  link: [scale to accommodate peaks on demand](../facts/aurora-serverless.md#aurora-serverless-case-bmw-serverless-v2-automated-capacity-peaks)
aurora-serverless-change-instant-scaling-16-acu
  claim: Aurora serverless now scales in even larger steps, adding up to 16 ACUs to its current capacity within a second and continuing to scale up to 256 ACUs as the workload grows.
  scope: Aurora serverless scale-up; maximum; posted 2026-09-30, after 2026-07-15: not examinable yet; enabled by default on platform version 3 or 4.
  link: [adding up to 16 ACUs to its current capacity within a second](../facts/aurora-serverless.md#aurora-serverless-change-instant-scaling-16-acu)
  say: up to sixteen ACUs within a second
aurora-serverless-change-max-256-acus
  claim: On October 3, 2024 Aurora serverless DB clusters could be created with a maximum capacity of 256 Aurora capacity units (ACUs).
  scope: per Aurora serverless DB instance (capacity range); maximum; needs a supported engine version; the guide's capacity table lists 0.5-128 ACUs for older engine versions.
  link: [maximum capacity of 256 Aurora capacity units (ACUs)](../facts/aurora-serverless.md#aurora-serverless-change-max-256-acus)
aurora-serverless-change-platform-version-4-performance
  claim: Aurora serverless platform version 4 gives up to 30% improved performance compared with platform version 3, and AWS says the improvements come at no additional cost.
  scope: Aurora serverless platform version 4; maximum; announced 2026-04-21; available in the Regions the guide lists.
  link: [Up to 30% improved performance compared to platform version 3](../facts/aurora-serverless.md#aurora-serverless-change-platform-version-4-performance)
  say: up to thirty percent better performance
aurora-serverless-change-scale-to-zero
  claim: Since 2024-11-20 Aurora serverless can scale down to 0 ACUs instead of stopping at 0.5 ACUs. To use it you set the minimum capacity to 0 ACUs, and the instance pauses after a period of inactivity.
  scope: per Aurora serverless DB instance; minimum; needs a supported engine version (guide: Aurora PostgreSQL 16.3, 15.7, 14.12, 13.15 or higher; Aurora MySQL 3.08.0 or higher).
  link: [0 ACUs](../facts/aurora-serverless.md#aurora-serverless-change-scale-to-zero)
  link: [0.5 ACUs](../facts/aurora-serverless.md#aurora-serverless-change-scale-to-zero)
  say: zero ACUs | half an ACU
  changed: 2024-11-20: was 0.5 ACUs
aurora-serverless-change-v1-auto-upgrade-to-v2
  claim: From April 7, 2025, AWS upgrades Aurora Serverless v1 clusters that were not upgraded to Aurora Serverless v2 during a scheduled cluster maintenance window.
  scope: Aurora Serverless v1 clusters; the announcement says an engine version not available for v2 is upgraded to a version v2 supports.
  link: [automatically upgrade your Aurora Serverless v1 cluster to Aurora Serverless v2](../facts/aurora-serverless.md#aurora-serverless-change-v1-auto-upgrade-to-v2)
aurora-serverless-change-v1-deprecation-date-extended
  claim: AWS extended the end-of-support date of Aurora Serverless v1 from December 31, 2024, to March 31, 2025. The announcement applies only to Serverless v1, and Serverless v2 continues to be supported.
  scope: Aurora Serverless v1; the re:Post announcement by AWS.
  link: [March 31, 2025](../facts/aurora-serverless.md#aurora-serverless-change-v1-deprecation-date-extended)
  link: [December 31, 2024](../facts/aurora-serverless.md#aurora-serverless-change-v1-deprecation-date-extended)
  say: March thirty-first, twenty twenty-five | December thirty-first, twenty twenty-four
  changed: 2025-03-31: was December 31, 2024
aurora-serverless-change-v1-no-extended-support
  claim: RDS Extended Support is not available for Aurora Serverless v1.
  scope: Aurora Serverless v1.
  link: [will not be available for Aurora Serverless v1](../facts/aurora-serverless.md#aurora-serverless-change-v1-no-extended-support)
aurora-serverless-change-v1-no-new-clusters-from-2025-01-08
  claim: From January 8, 2025, you can no longer create new Aurora Serverless v1 clusters with the AWS Console or the CLI.
  scope: Aurora Serverless v1.
  link: [you will no longer be able to create new Aurora Serverless v1 clusters](../facts/aurora-serverless.md#aurora-serverless-change-v1-no-new-clusters-from-2025-01-08)
aurora-serverless-change-v1-to-v2-add-v2-reader-and-failover
  claim: The last step of the AWS procedure to upgrade Aurora Serverless v1 to v2 is to add an Aurora Serverless v2 reader to the upgraded provisioned cluster and fail over to it.
  scope: Aurora Serverless v1 to v2 upgrade.
  link: [Add an Aurora Serverless v2 reader to the upgraded provisioned cluster and failover to it](../facts/aurora-serverless.md#aurora-serverless-change-v1-to-v2-add-v2-reader-and-failover)
aurora-serverless-change-v1-to-v2-first-step-provisioned
  claim: The first step of the AWS procedure to upgrade Aurora Serverless v1 to v2 is to convert the Serverless v1 database cluster to a provisioned cluster.
  scope: Aurora Serverless v1 to v2 upgrade; the second step is an engine upgrade if needed.
  link: [Convert your Aurora Serverless v1 database cluster to a provisioned cluster](../facts/aurora-serverless.md#aurora-serverless-change-v1-to-v2-first-step-provisioned)
aurora-serverless-change-v1-upgrade-to-v2-recommended
  claim: In an announcement on AWS re:Post, AWS recommended upgrading databases running Aurora Serverless v1 to Aurora Serverless v2 before March 31, 2025; the Aurora User Guide now calls Aurora Serverless v1 a deprecated product.
  scope: Aurora Serverless v1.
  link: [upgrading your databases running Aurora Serverless v1 to Aurora Serverless v2](../facts/aurora-serverless.md#aurora-serverless-change-v1-upgrade-to-v2-recommended)
  link: [a deprecated product](../facts/aurora-serverless.md#aurora-serverless-change-v1-upgrade-to-v2-recommended)
aurora-serverless-charged-only-for-resources-consumed
  claim: With Aurora serverless you are charged only for the resources that your DB clusters consume.
  scope: Aurora serverless DB clusters.
  link: [charged only for the resources](../facts/aurora-serverless.md#aurora-serverless-charged-only-for-resources-consumed)
aurora-serverless-choose-multitenant-dev-test
  claim: AWS says the automation of Aurora serverless is especially valuable for multitenant databases, distributed databases, development and test systems, and other environments with highly variable and unpredictable workloads.
  scope: Aurora serverless.
  link: [development and test systems](../facts/aurora-serverless.md#aurora-serverless-choose-multitenant-dev-test)
aurora-serverless-choose-variable-spiky-workloads
  claim: AWS says Aurora serverless is intended for variable or spiky workloads, where it is hard to plan when to change database capacity.
  scope: Aurora serverless.
  link: [variable or "spiky" workloads](../facts/aurora-serverless.md#aurora-serverless-choose-variable-spiky-workloads)
aurora-serverless-cluster-cache-management-not-available
  claim: For Aurora Serverless DB instances, the apg_ccm_enabled configuration parameter of Aurora PostgreSQL cluster cache management does not apply.
  scope: per Aurora Serverless DB instance.
  link: [doesn't apply to Aurora serverless DB instances](../facts/aurora-serverless.md#aurora-serverless-cluster-cache-management-not-available)
aurora-serverless-compute-and-storage-separate
  claim: With Aurora serverless, as with provisioned clusters, storage capacity and compute capacity are separate, so a cluster can hold many terabytes of data while its CPU and memory scale down.
  scope: Aurora serverless; scaling refers to compute capacity.
  link: [storage capacity and compute capacity are separate](../facts/aurora-serverless.md#aurora-serverless-compute-and-storage-separate)
aurora-serverless-connect-to-paused-instance-resumes
  claim: When you connect to a paused Aurora serverless instance, it automatically resumes and accepts the connection.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [automatically resumes and accepts the connection](../facts/aurora-serverless.md#aurora-serverless-connect-to-paused-instance-resumes)
  link: [connect to a paused Aurora serverless instance](../facts/aurora-serverless.md#aurora-serverless-connect-to-paused-instance-resumes)
aurora-serverless-convert-provisioned-and-serverless
  claim: You can modify existing Aurora DB instances from provisioned to Aurora serverless, or from Aurora serverless to provisioned, without creating a new cluster or DB instance.
  scope: Aurora DB instances.
  link: [from provisioned to Aurora serverless](../facts/aurora-serverless.md#aurora-serverless-convert-provisioned-and-serverless)
aurora-serverless-convert-writer-to-provisioned-via-failover
  claim: To convert an Aurora serverless writer to provisioned, switch one of the reader DB instances from Aurora serverless to provisioned, and then perform a failover to make that provisioned DB instance the writer.
  scope: Aurora serverless DB instances in an Aurora DB cluster.
  link: [Switch one of the reader DB instances](../facts/aurora-serverless.md#aurora-serverless-convert-writer-to-provisioned-via-failover)
  link: [perform a failover](../facts/aurora-serverless.md#aurora-serverless-convert-writer-to-provisioned-via-failover)
aurora-serverless-convert-writer-via-failover
  claim: To try Aurora serverless on a provisioned cluster, add Aurora serverless readers and use the Aurora failover mechanism to promote one to writer, which lets you switch over with minimal downtime and without changing the endpoint that client applications use.
  scope: Aurora serverless DB instances in an Aurora DB cluster.
  link: [use the Aurora failover mechanism](../facts/aurora-serverless.md#aurora-serverless-convert-writer-via-failover)
  link: [without changing the endpoint](../facts/aurora-serverless.md#aurora-serverless-convert-writer-via-failover)
aurora-serverless-db-instance-class-always-db-serverless
  claim: The --db-instance-class parameter for Aurora serverless is always db.serverless.
  scope: Aurora serverless DB instances in an Aurora DB cluster.
  link: [always `db.serverless`](../facts/aurora-serverless.md#aurora-serverless-db-instance-class-always-db-serverless)
  link: [`--db-instance-class` parameter for Aurora serverless](../facts/aurora-serverless.md#aurora-serverless-db-instance-class-always-db-serverless)
aurora-serverless-db-serverless-instance-class-type
  claim: db.serverless is a special DB instance class type used by Aurora serverless.
  scope: Aurora serverless DB instances.
  link: [db.serverless](../facts/aurora-serverless.md#aurora-serverless-db-serverless-instance-class-type)
  link: [special DB instance class type](../facts/aurora-serverless.md#aurora-serverless-db-serverless-instance-class-type)
aurora-serverless-dev-test-low-minimum-instead-of-burstable
  claim: For development and testing, Aurora serverless lets you create DB instances with a low minimum capacity instead of burstable db.t DB instance classes, and the instances scale down when the database is not in use.
  scope: Aurora serverless development and test environments.
  link: [a low minimum capacity](../facts/aurora-serverless.md#aurora-serverless-dev-test-low-minimum-instead-of-burstable)
aurora-serverless-faq-auto-pause-both-engines
  claim: Automatic pause and resume is available for both Aurora PostgreSQL and Aurora MySQL, and is especially useful for development, test and SaaS multi-tenant environments with long inactive periods.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [both Aurora PostgreSQL and Aurora MySQL](../facts/aurora-serverless.md#aurora-serverless-faq-auto-pause-both-engines)
aurora-serverless-faq-auto-resume-on-connection
  claim: When a new connection arrives at a paused Aurora serverless instance, the instance automatically resumes, typically faster than starting a stopped cluster.
  scope: per instance; a new connection arrives.
  link: [the instance automatically resumes](../facts/aurora-serverless.md#aurora-serverless-faq-auto-resume-on-connection)
aurora-serverless-faq-billed-per-second-acu
  claim: Aurora serverless capacity is measured in Aurora Capacity Units (ACUs), and you pay a flat rate per second of ACU usage.
  scope: per second of ACU usage; the rate depends on Aurora Standard or Aurora I/O-Optimized.
  link: [a flat rate per second of ACU usage](../facts/aurora-serverless.md#aurora-serverless-faq-billed-per-second-acu)
aurora-serverless-faq-definition
  claim: Aurora serverless is an on-demand, autoscaling configuration for Aurora that adjusts compute capacity within a range you set in Aurora Capacity Units (ACUs), in fine-grained increments.
  scope: Aurora serverless.
  link: [on-demand, autoscaling configuration](../facts/aurora-serverless.md#aurora-serverless-faq-definition)
aurora-serverless-faq-express-config-internet-gateway
  claim: With express configuration you can create and connect to an Aurora PostgreSQL database in seconds, pre-configured with an Aurora serverless cluster, and you also get a new internet gateway that supports the Postgres wire protocol for secure connections from tools and IDEs outside AWS without a VPN.
  scope: Aurora PostgreSQL express configuration; newer FAQ text; the scalability answer says you can't give a public IP address to Aurora serverless.
  link: [a new internet gateway](../facts/aurora-serverless.md#aurora-serverless-faq-express-config-internet-gateway)
aurora-serverless-faq-express-config-no-vpc
  claim: For streamlined setup you can create an Aurora serverless instance without a VPC using express configuration.
  scope: express configuration.
  link: [create an Aurora serverless instance without a VPC](../facts/aurora-serverless.md#aurora-serverless-faq-express-config-no-vpc)
aurora-serverless-faq-mixed-cluster-with-provisioned
  claim: You can add Aurora serverless instances to an existing Aurora DB cluster, creating a mixed-configuration cluster with any combination of provisioned and serverless instances.
  scope: per Aurora DB cluster.
  link: [any combination of provisioned and serverless instances](../facts/aurora-serverless.md#aurora-serverless-faq-mixed-cluster-with-provisioned)
aurora-serverless-faq-same-vpc-no-public-ip
  claim: The Aurora FAQ says you access Aurora serverless from a client application running in the same VPC and that you can't give a public IP address to Aurora serverless. Clusters created with express configuration are different: they are automatically set up with an internet access gateway, which provides public access to the database with IAM authentication.
  scope: Aurora serverless DB clusters; except clusters created with express configuration, which get an internet access gateway with IAM authentication.
  link: [can't give a public IP address](../facts/aurora-serverless.md#aurora-serverless-faq-same-vpc-no-public-ip)
aurora-serverless-faq-scales-to-zero-pauses
  claim: Aurora serverless scales down to zero ACUs when the database has no active connections, automatically pausing the instance to eliminate compute costs during idle periods.
  scope: per instance; no active connections.
  link: [scales down to zero ACUs](../facts/aurora-serverless.md#aurora-serverless-faq-scales-to-zero-pauses)
aurora-serverless-faq-set-capacity-explicitly
  claim: If capacity cannot scale fast enough for a sudden workload change, you can set the Aurora serverless capacity explicitly through the console, CLI or API.
  scope: Aurora serverless.
  link: [set it explicitly](../facts/aurora-serverless.md#aurora-serverless-faq-set-capacity-explicitly)
aurora-serverless-faq-snapshot-restore-both-directions
  claim: You can restore snapshots between provisioned and serverless Aurora clusters in either direction.
  scope: per snapshot restore.
  link: [in either direction](../facts/aurora-serverless.md#aurora-serverless-faq-snapshot-restore-both-directions)
aurora-serverless-faq-supports-all-provisioned-features
  claim: Aurora serverless supports all features of provisioned Aurora, including read replicas, Multi-AZ configuration, Aurora Global Database, RDS Proxy and CloudWatch Database Insights.
  scope: Aurora serverless DB instances in an Aurora DB cluster.
  link: [supports all features of provisioned Aurora](../facts/aurora-serverless.md#aurora-serverless-faq-supports-all-provisioned-features)
aurora-serverless-global-database-read-copies-dr
  claim: You can use Aurora serverless in combination with Aurora global databases to create additional read-only copies of your cluster in other AWS Regions for disaster recovery purposes.
  scope: Aurora serverless DB instances in an Aurora global database or VPC.
  link: [Aurora serverless in combination with Aurora global databases](../facts/aurora-serverless.md#aurora-serverless-global-database-read-copies-dr)
  link: [disaster recovery purposes](../facts/aurora-serverless.md#aurora-serverless-global-database-read-copies-dr)
aurora-serverless-global-primary-writer-no-auto-pause
  claim: If a cluster is the primary cluster in an Aurora global database, Aurora does not automatically pause the Aurora serverless writer instance.
  scope: Aurora serverless DB instances in an Aurora global database or VPC.
  link: [primary cluster in an Aurora global database](../facts/aurora-serverless.md#aurora-serverless-global-primary-writer-no-auto-pause)
  link: [doesn't automatically pause the Aurora serverless writer instance](../facts/aurora-serverless.md#aurora-serverless-global-primary-writer-no-auto-pause)
aurora-serverless-global-secondary-can-use-serverless
  claim: In an Aurora global database you might not need as much capacity in the secondary clusters as in the primary, so you can use Aurora serverless DB instances there and let capacity scale up if a secondary Region is promoted.
  scope: Aurora global database secondary clusters.
  link: [Aurora serverless DB instances in the secondary clusters](../facts/aurora-serverless.md#aurora-serverless-global-secondary-can-use-serverless)
aurora-serverless-global-secondary-no-auto-pause
  claim: Aurora serverless instances in the secondary clusters of an Aurora Global Database do not automatically pause.
  scope: Aurora serverless DB instances in an Aurora global database or VPC.
  link: [don't automatically pause](../facts/aurora-serverless.md#aurora-serverless-global-secondary-no-auto-pause)
  link: [Aurora serverless instances in the secondary clusters](../facts/aurora-serverless.md#aurora-serverless-global-secondary-no-auto-pause)
aurora-serverless-identical-min-max-never-scales
  claim: If the minimum and maximum capacity of an Aurora serverless cluster are identical, the capacity never scales up or down.
  scope: Aurora serverless capacity range and scaling.
  link: [the capacity never scales up or down](../facts/aurora-serverless.md#aurora-serverless-identical-min-max-never-scales)
  link: [identical](../facts/aurora-serverless.md#aurora-serverless-identical-min-max-never-scales)
aurora-serverless-invalid-credentials-still-resume
  claim: A connection attempt that does not include valid credentials still causes a paused Aurora serverless DB instance to resume.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [still causes the DB instance to resume](../facts/aurora-serverless.md#aurora-serverless-invalid-credentials-still-resume)
  link: [doesn't include valid credentials](../facts/aurora-serverless.md#aurora-serverless-invalid-credentials-still-resume)
aurora-serverless-low-min-capacity-independent-readers-replication-lag
  claim: If an Aurora serverless cluster has readers whose promotion tier is not 0 or 1, the readers do not scale along with the writer.
  scope: Aurora serverless capacity range and scaling.
  link: [readers don't scale along with the writer](../facts/aurora-serverless.md#aurora-serverless-low-min-capacity-independent-readers-replication-lag)
  link: [promotion tier of the readers isn't 0 or 1](../facts/aurora-serverless.md#aurora-serverless-low-min-capacity-independent-readers-replication-lag)
aurora-serverless-max-capacity-at-least-min
  claim: The maximum capacity of an Aurora serverless cluster must be at least as high as the minimum capacity.
  scope: Aurora serverless capacity range and scaling.
  link: [at least as high as the minimum](../facts/aurora-serverless.md#aurora-serverless-max-capacity-at-least-min)
aurora-serverless-max-cluster-capacity-n-times-max-acu
  claim: When an Aurora serverless cluster has n Aurora serverless DB instances, the theoretical maximum capacity the cluster can consume at any moment is n times the maximum ACU setting for the cluster.
  scope: Aurora serverless capacity range and scaling.
  link: [n times the maximum ACU setting](../facts/aurora-serverless.md#aurora-serverless-max-cluster-capacity-n-times-max-acu)
  link: [theoretical maximum Aurora serverless capacity](../facts/aurora-serverless.md#aurora-serverless-max-cluster-capacity-n-times-max-acu)
aurora-serverless-min-capacity-above-zero-no-pause
  claim: If the minimum capacity value for the DB cluster is higher than zero ACUs, the Aurora serverless instances in the cluster do not automatically pause.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [higher than zero ACUs](../facts/aurora-serverless.md#aurora-serverless-min-capacity-above-zero-no-pause)
  link: [don't automatically pause](../facts/aurora-serverless.md#aurora-serverless-min-capacity-above-zero-no-pause)
aurora-serverless-minimum-capacity-0-needs-auto-pause-versions
  claim: The smallest Aurora Serverless capacity that you can define is 0 ACUs, for Aurora Serverless versions that support the auto-pause feature.
  scope: per Aurora cluster with Aurora Serverless DB instances; minimum; in older versions without auto-pause the lowest minimum is 0.5 ACUs.
  link: [smallest Aurora serverless capacity that you can define is 0 ACUs](../facts/aurora-serverless.md#aurora-serverless-minimum-capacity-0-needs-auto-pause-versions)
  say: zero ACUs with auto-pause
aurora-serverless-mixed-configuration-cluster
  claim: You can set up a cluster that contains both Aurora serverless and provisioned capacity, called a mixed-configuration cluster.
  scope: Aurora serverless DB instances in an Aurora DB cluster.
  link: [both Aurora serverless and provisioned capacity](../facts/aurora-serverless.md#aurora-serverless-mixed-configuration-cluster)
  link: [mixed-configuration cluster](../facts/aurora-serverless.md#aurora-serverless-mixed-configuration-cluster)
aurora-serverless-multi-az-cluster-compute-in-more-than-one-az
  claim: A Multi-AZ Aurora DB cluster has compute capacity available at all times in more than one Availability Zone.
  scope: Aurora serverless DB instances in an Aurora DB cluster.
  link: [in more than one Availability Zone](../facts/aurora-serverless.md#aurora-serverless-multi-az-cluster-compute-in-more-than-one-az)
  link: [Multi-AZ Aurora DB cluster](../facts/aurora-serverless.md#aurora-serverless-multi-az-cluster-compute-in-more-than-one-az)
aurora-serverless-multi-az-distribute-instances
  claim: You can distribute the Aurora serverless DB instances of a cluster across multiple Availability Zones.
  scope: Aurora serverless DB instances in an Aurora DB cluster.
  link: [across multiple Availability Zones](../facts/aurora-serverless.md#aurora-serverless-multi-az-distribute-instances)
  link: [Multi-AZ](../facts/aurora-serverless.md#aurora-serverless-multi-az-distribute-instances)
aurora-serverless-needs-scaling-configuration-before-instances
  claim: An Aurora cluster must have a ServerlessV2ScalingConfiguration attribute, which specifies the capacity range, before you can add any DB instances that use the db.serverless DB instance class.
  scope: Aurora serverless DB instances in an Aurora DB cluster.
  link: [`ServerlessV2ScalingConfiguration` attribute](../facts/aurora-serverless.md#aurora-serverless-needs-scaling-configuration-before-instances)
  link: [`db.serverless` DB instance class](../facts/aurora-serverless.md#aurora-serverless-needs-scaling-configuration-before-instances)
aurora-serverless-not-supported-with-aurora-auto-scaling
  claim: Aurora Auto Scaling, which adds new readers based on CPU usage, is not supported with Aurora Serverless; instead you can create Aurora Serverless reader instances in advance and leave them scaled down to low capacity.
  scope: per Aurora cluster with Aurora Serverless DB instances.
  link: [Aurora Auto Scaling isn't supported](../facts/aurora-serverless.md#aurora-serverless-not-supported-with-aurora-auto-scaling)
aurora-serverless-older-versions-cannot-reach-zero
  claim: In older Aurora MySQL and Aurora PostgreSQL versions, idle Aurora serverless writers and readers can scale down to the minimum ACU value that you specified, but not all the way to zero ACUs.
  scope: Aurora serverless capacity range and scaling.
  link: [but not all the way to zero ACUs](../facts/aurora-serverless.md#aurora-serverless-older-versions-cannot-reach-zero)
  link: [older Aurora MySQL and Aurora PostgreSQL versions](../facts/aurora-serverless.md#aurora-serverless-older-versions-cannot-reach-zero)
aurora-serverless-on-demand-autoscaling-configuration
  claim: Aurora serverless is an on-demand, autoscaling configuration for Amazon Aurora.
  scope: Aurora serverless.
  link: [on-demand, autoscaling configuration for Amazon Aurora](../facts/aurora-serverless.md#aurora-serverless-on-demand-autoscaling-configuration)
  link: [Aurora serverless](../facts/aurora-serverless.md#aurora-serverless-on-demand-autoscaling-configuration)
aurora-serverless-open-connections-block-pause
  claim: If any user-initiated connections are open to an Aurora serverless instance, the instance does not pause.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [user-initiated connections are open](../facts/aurora-serverless.md#aurora-serverless-open-connections-block-pause)
  link: [the instance won't pause](../facts/aurora-serverless.md#aurora-serverless-open-connections-block-pause)
aurora-serverless-overprovision-raises-cost
  claim: Configuring capacity correctly in advance is not always possible with the provisioned model, and overprovisioning can result in higher costs because you hold capacity that you do not use.
  scope: Aurora provisioned clusters for variable workloads.
  link: [higher costs if you overprovision](../facts/aurora-serverless.md#aurora-serverless-overprovision-raises-cost)
aurora-serverless-paused-instances-not-resumed-by-connect-while-cluster-stopped
  claim: While an Aurora cluster is stopped, any paused Aurora serverless instances do not automatically resume based on attempts to connect.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [don't automatically resume based on attempts to connect](../facts/aurora-serverless.md#aurora-serverless-paused-instances-not-resumed-by-connect-while-cluster-stopped)
  link: [While an Aurora cluster is stopped](../facts/aurora-serverless.md#aurora-serverless-paused-instances-not-resumed-by-connect-while-cluster-stopped)
aurora-serverless-platform-version-new-clusters-latest
  claim: All new Aurora serverless clusters, database restores, and new clones launch with the latest platform version available in your AWS Region.
  scope: Aurora serverless platform versions.
  link: [launch with the latest platform version available](../facts/aurora-serverless.md#aurora-serverless-platform-version-new-clusters-latest)
aurora-serverless-platform-version-upgrade-options
  claim: Existing Aurora serverless clusters on an older platform version can be upgraded directly to the latest platform version by applying pending maintenance, stopping and restarting the cluster, or using blue/green deployments.
  scope: Aurora serverless platform versions.
  link: [applying the pending maintenance](../facts/aurora-serverless.md#aurora-serverless-platform-version-upgrade-options)
aurora-serverless-platform-versions-not-serverless-v1
  claim: Aurora serverless platform versions should not be confused with Aurora Serverless v1, which the guide calls a deprecated product with a different architecture.
  scope: Aurora serverless platform versions.
  link: [a deprecated product with a different architecture](../facts/aurora-serverless.md#aurora-serverless-platform-versions-not-serverless-v1)
aurora-serverless-product-save-up-to-90-percent
  claim: The Aurora serverless product page says you pay only for the capacity your application consumes and can save up to 90% of database cost compared with provisioning capacity for peak load.
  scope: Aurora serverless compared with provisioning capacity for peak load; maximum; marketing statement on the product page; actual savings depend on the workload.
  link: [save up to 90% of your database cost](../facts/aurora-serverless.md#aurora-serverless-product-save-up-to-90-percent)
  say: up to ninety percent
aurora-serverless-provisioned-brief-outages-acceptable
  claim: The Aurora provisioned model works well when you can adjust capacity in advance of expected consumption patterns and it is acceptable to have brief outages while you change the instance class of the writer and readers.
  scope: Aurora provisioned clusters.
  link: [acceptable to have brief outages](../facts/aurora-serverless.md#aurora-serverless-provisioned-brief-outages-acceptable)
aurora-serverless-provisioned-constant-capacity-predict-ahead
  claim: With provisioned Aurora capacity, charges are relatively easy to forecast because capacity is constant, but you have to predict in advance how much capacity you need.
  scope: Aurora provisioned clusters.
  link: [relatively easy to forecast](../facts/aurora-serverless.md#aurora-serverless-provisioned-constant-capacity-predict-ahead)
aurora-serverless-provisioned-suited-to-steady-workloads
  claim: AWS says Aurora provisioned clusters are suitable for steady workloads; with provisioned clusters, you choose a DB instance class that has a predefined amount of memory, CPU power, I/O bandwidth, and so on.
  scope: Aurora provisioned clusters.
  link: [suitable for steady workloads](../facts/aurora-serverless.md#aurora-serverless-provisioned-suited-to-steady-workloads)
aurora-serverless-rds-proxy-blocks-auto-pause
  claim: Because an associated RDS Proxy maintains an open connection to each DB instance in the cluster, Aurora serverless instances in such a cluster do not automatically pause.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [won't automatically pause](../facts/aurora-serverless.md#aurora-serverless-rds-proxy-blocks-auto-pause)
  link: [proxy maintains an open connection](../facts/aurora-serverless.md#aurora-serverless-rds-proxy-blocks-auto-pause)
aurora-serverless-rds-proxy-supported
  claim: You can use Amazon RDS Proxy with Aurora serverless to allow your applications to pool and share database connections to improve their ability to scale.
  scope: Aurora serverless DB instances in an Aurora DB cluster.
  link: [use Amazon RDS Proxy](../facts/aurora-serverless.md#aurora-serverless-rds-proxy-supported)
  link: [improve their ability to scale](../facts/aurora-serverless.md#aurora-serverless-rds-proxy-supported)
aurora-serverless-reader-follow-writer-or-independent
  claim: You can choose to make an Aurora serverless reader follow the capacity of the associated writer, or scale independently, by specifying its promotion tier.
  scope: Aurora serverless capacity range and scaling.
  link: [follow the capacity of the associated writer](../facts/aurora-serverless.md#aurora-serverless-reader-follow-writer-or-independent)
  link: [specifying the promotion tier for that reader](../facts/aurora-serverless.md#aurora-serverless-reader-follow-writer-or-independent)
aurora-serverless-readers-alternative-to-aurora-auto-scaling
  claim: Instead of Aurora Auto Scaling, you can create Aurora serverless reader DB instances in advance and leave them scaled down to low capacity, which is a faster and less disruptive way to scale a cluster's read capacity.
  scope: Aurora serverless capacity range and scaling.
  link: [create Aurora serverless reader DB instances in advance](../facts/aurora-serverless.md#aurora-serverless-readers-alternative-to-aurora-auto-scaling)
  link: [leave them scaled down to low capacity](../facts/aurora-serverless.md#aurora-serverless-readers-alternative-to-aurora-auto-scaling)
aurora-serverless-readers-scale-independently-of-writer
  claim: By specifying promotion tiers for Aurora serverless DB instances, you can configure a cluster so that reader DB instances scale independently of the writer to handle extra load, then scale back down.
  scope: Aurora serverless readers; mixed-use OLTP application with periodic query spikes.
  link: [specifying promotion tiers](../facts/aurora-serverless.md#aurora-serverless-readers-scale-independently-of-writer)
aurora-serverless-readers-tier-2-15-pause-independently
  claim: You can enable some reader instances to pause even while the writer instance and other readers in the cluster remain active, by assigning them a failover priority in the range 2-15.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [enable some reader instances to pause](../facts/aurora-serverless.md#aurora-serverless-readers-tier-2-15-pause-independently)
  link: [failover priority in the range 2-15](../facts/aurora-serverless.md#aurora-serverless-readers-tier-2-15-pause-independently)
aurora-serverless-replication-at-storage-layer-reader-capacity
  claim: In Aurora, replication occurs at the storage layer, so reader capacity does not directly affect replication.
  scope: Aurora serverless capacity range and scaling.
  link: [replication occurs at the storage layer](../facts/aurora-serverless.md#aurora-serverless-replication-at-storage-layer-reader-capacity)
  link: [reader capacity doesn't directly affect replication](../facts/aurora-serverless.md#aurora-serverless-replication-at-storage-layer-reader-capacity)
aurora-serverless-resuming-reader-resumes-writer
  claim: Resuming any reader always causes the writer to resume, and resuming the writer always causes any readers with failover priority 0 and 1 to resume.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [always causes the writer to resume](../facts/aurora-serverless.md#aurora-serverless-resuming-reader-resumes-writer)
  link: [readers with failover priority 0 and 1 to resume](../facts/aurora-serverless.md#aurora-serverless-resuming-reader-resumes-writer)
aurora-serverless-retry-logic-for-paused-instances
  claim: AWS recommends implementing retry logic for connections to Aurora clusters that have some Aurora serverless instances with auto-pause enabled.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [implementing retry logic for connections](../facts/aurora-serverless.md#aurora-serverless-retry-logic-for-paused-instances)
  link: [auto-pause enabled](../facts/aurora-serverless.md#aurora-serverless-retry-logic-for-paused-instances)
aurora-serverless-scale-to-zero-auto-pause-resume
  claim: In recent Aurora MySQL and Aurora PostgreSQL versions, Aurora serverless writers and readers can scale all the way down to zero ACUs, a capability called automatic pause and resume, or auto-pause.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [scale all the way down to zero ACUs](../facts/aurora-serverless.md#aurora-serverless-scale-to-zero-auto-pause-resume)
  link: [automatic pause and resume, or auto-pause](../facts/aurora-serverless.md#aurora-serverless-scale-to-zero-auto-pause-resume)
aurora-serverless-scales-in-half-acu-steps
  claim: Aurora serverless can add half an ACU when only a little more capacity is needed, unlike a provisioned cluster, where scaling up means adding a whole new DB instance.
  scope: Aurora serverless.
  link: [add half an ACU](../facts/aurora-serverless.md#aurora-serverless-scales-in-half-acu-steps)
  say: add half an ACU
aurora-serverless-scales-up-on-cpu-memory-network-load
  claim: Aurora continuously tracks utilization of resources such as CPU, memory, and network for each Aurora serverless writer or reader, and scales up when capacity is constrained by any of these.
  scope: Aurora serverless capacity range and scaling.
  link: [CPU, memory, and network](../facts/aurora-serverless.md#aurora-serverless-scales-up-on-cpu-memory-network-load)
  link: [continuously tracks](../facts/aurora-serverless.md#aurora-serverless-scales-up-on-cpu-memory-network-load)
aurora-serverless-scales-without-disrupting-client-transactions
  claim: Aurora serverless scales compute and memory capacity as needed, with no disruption to client transactions or the overall workload.
  scope: Aurora serverless capacity range and scaling.
  link: [no disruption to client transactions](../facts/aurora-serverless.md#aurora-serverless-scales-without-disrupting-client-transactions)
  link: [scales compute and memory capacity as needed](../facts/aurora-serverless.md#aurora-serverless-scales-without-disrupting-client-transactions)
aurora-serverless-scaling-does-not-disrupt-operations
  claim: Scaling does not disrupt any database operations that are underway.
  scope: Aurora serverless capacity range and scaling.
  link: [Scaling doesn't disrupt any database operations](../facts/aurora-serverless.md#aurora-serverless-scaling-does-not-disrupt-operations)
  link: [operations that are underway](../facts/aurora-serverless.md#aurora-serverless-scaling-does-not-disrupt-operations)
aurora-serverless-scaling-increments-as-small-as-half-acu
  claim: Aurora Serverless scaling happens in increments as small as 0.5 ACUs. The larger the current capacity, the larger the scaling increment.
  scope: per Aurora Serverless writer or reader; minimum.
  link: [increments as small as 0.5 ACUs](../facts/aurora-serverless.md#aurora-serverless-scaling-increments-as-small-as-half-acu)
  say: steps as small as half an ACU
aurora-serverless-scaling-rate-depends-on-current-capacity
  claim: The scaling rate for an Aurora serverless DB instance depends on its current capacity, and the higher the current capacity, the faster it can scale up.
  scope: Aurora serverless capacity range and scaling.
  link: [depends on its current capacity](../facts/aurora-serverless.md#aurora-serverless-scaling-rate-depends-on-current-capacity)
  link: [the faster it can scale up](../facts/aurora-serverless.md#aurora-serverless-scaling-rate-depends-on-current-capacity)
aurora-serverless-scaling-with-open-connections-no-quiet-point
  claim: Aurora serverless scaling can happen while connections are open and transactions are in process, and Aurora serverless does not wait for a quiet point to begin scaling.
  scope: Aurora serverless capacity range and scaling.
  link: [doesn't wait for a quiet point](../facts/aurora-serverless.md#aurora-serverless-scaling-with-open-connections-no-quiet-point)
  link: [while database connections are open](../facts/aurora-serverless.md#aurora-serverless-scaling-with-open-connections-no-quiet-point)
aurora-serverless-scheduled-jobs-do-not-resume-paused-instance
  claim: Aurora does not automatically resume a paused instance for engine-specific scheduled jobs, such as those in the PostgreSQL pg_cron extension or the MySQL event scheduler.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [doesn't automatically resume a paused instance](../facts/aurora-serverless.md#aurora-serverless-scheduled-jobs-do-not-resume-paused-instance)
  link: [PostgreSQL `pg_cron` extension](../facts/aurora-serverless.md#aurora-serverless-scheduled-jobs-do-not-resume-paused-instance)
aurora-serverless-specify-min-max-capacity-range
  claim: With Aurora serverless you specify the minimum and maximum capacity range, and Aurora scales each Aurora serverless writer or reader in the cluster within that range.
  scope: Aurora serverless capacity range and scaling.
  link: [specify the minimum and maximum capacity range](../facts/aurora-serverless.md#aurora-serverless-specify-min-max-capacity-range)
  link: [within that capacity range](../facts/aurora-serverless.md#aurora-serverless-specify-min-max-capacity-range)
aurora-serverless-standby-scales-with-writer-multi-az
  claim: With Aurora serverless, you can choose for the standby compute capacity to scale up and down along with the capacity of the writer, so the second AZ is ready to take over the current workload.
  scope: Aurora serverless DB instances in a Multi-AZ Aurora DB cluster.
  link: [standby compute capacity to scale up and down](../facts/aurora-serverless.md#aurora-serverless-standby-scales-with-writer-multi-az)
  link: [can scale down when the database is idle](../facts/aurora-serverless.md#aurora-serverless-standby-scales-with-writer-multi-az)
aurora-serverless-stop-start-all-versions
  claim: The stop/start cluster feature is available for all Aurora serverless versions.
  scope: Aurora serverless DB instances in an Aurora DB cluster.
  link: [available for all Aurora serverless versions](../facts/aurora-serverless.md#aurora-serverless-stop-start-all-versions)
  link: [stop and start the entire cluster](../facts/aurora-serverless.md#aurora-serverless-stop-start-all-versions)
aurora-serverless-storage-io-follow-cluster-configuration
  claim: You can configure all instances in an Aurora cluster, including Aurora serverless instances, to use the Aurora Standard or the Aurora I/O-Optimized configuration, based on the price-performance and price-predictability needs of the application.
  scope: Aurora serverless clusters.
  link: [Aurora Standard or Aurora I/O-Optimized configuration](../facts/aurora-serverless.md#aurora-serverless-storage-io-follow-cluster-configuration)
aurora-serverless-tier-0-1-readers-follow-writer
  claim: For Aurora serverless readers in promotion tiers 0 and 1, the minimum capacity is defined by the current writer capacity and the maximum capacity is the maximum ACU value specified for the cluster.
  scope: Aurora serverless capacity range and scaling.
  link: [defined by the current writer capacity](../facts/aurora-serverless.md#aurora-serverless-tier-0-1-readers-follow-writer)
  link: [promotion tiers 0 and 1](../facts/aurora-serverless.md#aurora-serverless-tier-0-1-readers-follow-writer)
aurora-serverless-tier-2-to-15-readers-scale-independently
  claim: Aurora serverless readers in promotion tiers 2–15 scale independently from the writer.
  scope: Aurora serverless capacity range and scaling.
  link: [scale independently from the writer](../facts/aurora-serverless.md#aurora-serverless-tier-2-to-15-readers-scale-independently)
  link: [promotion tiers 2–15](../facts/aurora-serverless.md#aurora-serverless-tier-2-to-15-readers-scale-independently)
aurora-serverless-v2-adds-data-api-auto-pause-256-acu
  claim: AWS says Aurora Serverless v2 continues to be supported and offers additional features beyond v1: Data API support, automatic pause and resume, and a maximum database capacity of up to 256 ACUs.
  scope: Aurora Serverless v2; maximum; statement of the v1 end-of-support announcement.
  link: [automatic pause/resume capabilities](../facts/aurora-serverless.md#aurora-serverless-v2-adds-data-api-auto-pause-256-acu)
  link: [up to 256 ACUs](../facts/aurora-serverless.md#aurora-serverless-v2-adds-data-api-auto-pause-256-acu)
  say: automatic pause and resume | up to two hundred fifty-six ACUs
aurora-serverless-wait-20-minutes-before-pausing-after-admin
  claim: After an Aurora Serverless instance wakes up for an administrative operation such as an upgrade or applying maintenance, Aurora waits at least 20 minutes before pausing that instance again.
  scope: per auto-paused Aurora Serverless instance; minimum; not adjustable.
  link: [at least 20 minutes](../facts/aurora-serverless.md#aurora-serverless-wait-20-minutes-before-pausing-after-admin)
  say: at least twenty minutes
aurora-serverless-works-like-provisioned-for-failover
  claim: Aurora serverless works like provisioned for failover and other high availability features.
  scope: Aurora serverless DB instances in an Aurora DB cluster.
  link: [works like provisioned for failover](../facts/aurora-serverless.md#aurora-serverless-works-like-provisioned-for-failover)
  link: [other high availability features](../facts/aurora-serverless.md#aurora-serverless-works-like-provisioned-for-failover)
aurora-serverless-zero-etl-blocks-auto-pause
  claim: In a cluster with an associated zero-ETL integration to Redshift, the writer instance and any reader instances in failover promotion tiers zero and one do not automatically pause.
  scope: Aurora serverless auto-pause (minimum capacity 0 ACUs).
  link: [zero-ETL integration to Redshift](../facts/aurora-serverless.md#aurora-serverless-zero-etl-blocks-auto-pause)
  link: [don't automatically pause](../facts/aurora-serverless.md#aurora-serverless-zero-etl-blocks-auto-pause)
aurora-share-manual-snapshot-enables-copy
  claim: Sharing a manual DB cluster snapshot, whether encrypted or unencrypted, enables authorized AWS accounts to copy the snapshot.
  scope: Aurora DB cluster snapshots.
  link: [enables authorized AWS accounts to copy the snapshot](../facts/aurora.md#aurora-share-manual-snapshot-enables-copy)
  link: [Sharing a manual DB cluster snapshot](../facts/aurora.md#aurora-share-manual-snapshot-enables-copy)
aurora-single-az-cluster-create-instances-manually
  claim: If a provisioned or Aurora serverless cluster has only a single DB instance, or if the primary and all readers are in the same AZ, you must manually create one or more new DB instances in another AZ after an AZ outage.
  scope: Aurora DB cluster with all instances in one AZ, after an AZ outage.
  link: [manually create one or more new DB instances](../facts/aurora.md#aurora-single-az-cluster-create-instances-manually)
  link: [only contains a single DB instance](../facts/aurora.md#aurora-single-az-cluster-create-instances-manually)
aurora-single-instance-still-a-cluster
  claim: An Aurora configuration with only a single DB instance is still a cluster, because the underlying storage volume involves multiple storage nodes distributed across multiple Availability Zones.
  scope: Amazon Aurora overview.
  link: [still a cluster](../facts/aurora.md#aurora-single-instance-still-a-cluster)
  link: [only a single DB instance](../facts/aurora.md#aurora-single-instance-still-a-cluster)
aurora-sla-multi-az-99-99
  claim: Under the Aurora Multi-AZ SLA, a Multi-AZ cluster whose Monthly Uptime Percentage is less than 99.99% but at least 99.0% earns a 10% service credit.
  scope: Amazon Aurora Multi-AZ SLA, per Multi-AZ cluster, monthly billing cycle; cluster with instances in at least two Availability Zones.
  link: [99.99%](../facts/aurora.md#aurora-sla-multi-az-99-99)
aurora-sla-single-az-99-9
  claim: Under the Aurora Single-AZ SLA, a Single-AZ cluster whose uptime percentage is less than 99.9% but at least 99.0% earns a 10% service credit.
  scope: Amazon Aurora Single-AZ SLA, per Single-AZ cluster, monthly billing cycle; all instances of the cluster in one Availability Zone.
  link: [99.9%](../facts/aurora.md#aurora-sla-single-az-99-9)
aurora-sla-two-commitments-multi-az-single-az
  claim: AWS makes two SLA commitments for Amazon Aurora: a Multi-AZ SLA for each cluster deployed across two or more AZs, and a Single-AZ SLA for each cluster deployed to one AZ.
  scope: Amazon Aurora Service Level Agreement, per Aurora cluster.
  link: [two SLA commitments for Amazon Aurora](../facts/aurora.md#aurora-sla-two-commitments-multi-az-single-az)
aurora-snapshot-cluster-must-be-available
  claim: Your DB cluster must be in the available state to take a DB cluster snapshot.
  scope: Aurora DB cluster snapshots.
  link: [must be in the `available` state](../facts/aurora.md#aurora-snapshot-cluster-must-be-available)
  link: [take a DB cluster snapshot](../facts/aurora.md#aurora-snapshot-cluster-must-be-available)
aurora-snapshot-copy-region-and-shared
  claim: You can copy an Aurora DB cluster snapshot within the same AWS Region or across AWS Regions, and you can copy shared snapshots.
  scope: Aurora DB cluster snapshots.
  link: [copy a snapshot across AWS Regions](../facts/aurora.md#aurora-snapshot-copy-region-and-shared)
  link: [copy shared snapshots](../facts/aurora.md#aurora-snapshot-copy-region-and-shared)
aurora-snapshot-default-kms-key-cannot-be-shared
  claim: Snapshots that have been encrypted with the default AWS KMS key cannot be shared.
  scope: Aurora DB cluster snapshots.
  link: [default AWS KMS key can't be shared](../facts/aurora.md#aurora-snapshot-default-kms-key-cannot-be-shared)
  link: [default AWS KMS key](../facts/aurora.md#aurora-snapshot-default-kms-key-cannot-be-shared)
aurora-snapshot-share-up-to-20-accounts
  claim: You can share an Aurora snapshot with up to 20 AWS account IDs or make it public.
  scope: per Aurora snapshot; maximum; not adjustable.
  link: [up to 20 AWS account IDs](../facts/aurora.md#aurora-snapshot-share-up-to-20-accounts)
  say: twenty account IDs
aurora-snapshot-storage-charged-after-cluster-deleted
  claim: After the Aurora cluster associated with a snapshot is deleted, storing that snapshot incurs the standard backup storage charges for Aurora.
  scope: Aurora DB cluster snapshots.
  link: [incurs the standard backup storage charges for Aurora](../facts/aurora.md#aurora-snapshot-storage-charged-after-cluster-deleted)
  link: [cluster associated with a snapshot is deleted](../facts/aurora.md#aurora-snapshot-storage-charged-after-cluster-deleted)
aurora-snapshots-always-full-backups
  claim: Aurora DB cluster snapshots are always full backups that capture the size of the cluster volume when you create them, and Aurora treats them as manual snapshots whether taken manually or through an AWS Backup plan.
  scope: per Aurora DB cluster snapshot.
  link: [always full backups](../facts/aurora.md#aurora-snapshots-always-full-backups)
aurora-snapshots-do-not-expire
  claim: To retain data beyond the backup retention period you can take a snapshot of the cluster volume, and Aurora DB cluster snapshots do not expire.
  scope: per Aurora DB cluster snapshot.
  link: [snapshots don't expire](../facts/aurora.md#aurora-snapshots-do-not-expire)
aurora-snapshots-free-within-retention-period
  claim: Aurora provides unlimited free storage for snapshots within the automated backup retention period. After a manual snapshot is outside this period, it incurs charges per GB-month.
  scope: per Aurora DB cluster.
  link: [unlimited free storage for snapshots](../facts/aurora.md#aurora-snapshots-free-within-retention-period)
aurora-ssl-tls-connections-both-engines
  claim: You can use SSL or TLS from your application to encrypt a connection to a DB cluster running Aurora MySQL or Aurora PostgreSQL.
  scope: encryption in transit (SSL/TLS) to Aurora DB clusters.
  link: [encrypt a connection to a DB cluster](../facts/aurora.md#aurora-ssl-tls-connections-both-engines)
  link: [Transport Layer Security (TLS)](../facts/aurora.md#aurora-ssl-tls-connections-both-engines)
aurora-standard-best-when-io-under-25-percent
  claim: Aurora Standard is the best choice when your I/O spending is less than 25% of your total Aurora database spending, and you pay a standard rate per 1 million requests for I/O operations.
  scope: per Aurora DB cluster.
  link: [less than 25%](../facts/aurora.md#aurora-standard-best-when-io-under-25-percent)
  link: [per 1 million requests](../facts/aurora.md#aurora-standard-best-when-io-under-25-percent)
  say: under a quarter | per million requests
aurora-standard-pays-per-million-io
  claim: With Aurora Standard you pay for usage and storage plus a standard rate per 1 million requests for I/O operations.
  scope: Aurora Standard cluster storage configuration.
  link: [standard rate per 1 million requests for I/O operations](../facts/aurora.md#aurora-standard-pays-per-million-io)
  link: [also pay a standard rate](../facts/aurora.md#aurora-standard-pays-per-million-io)
aurora-stop-cluster-up-to-seven-days
  claim: You can stop an Aurora DB cluster for up to seven days. If you do not start it manually after seven days, it is started automatically so that it does not fall behind required maintenance updates.
  scope: per Aurora DB cluster; maximum; not adjustable.
  link: [up to seven days](../facts/aurora.md#aurora-stop-cluster-up-to-seven-days)
  say: up to seven days
aurora-stop-not-with-cross-region-replica-or-blue-green
  claim: You cannot stop and start an Aurora cluster that has a cross-Region read replica, or one that is part of a blue/green deployment.
  scope: stopping and starting an Aurora DB cluster.
  link: [can't stop and start a cluster](../facts/aurora.md#aurora-stop-not-with-cross-region-replica-or-blue-green)
  link: [part of a blue/green deployment](../facts/aurora.md#aurora-stop-not-with-cross-region-replica-or-blue-green)
aurora-stop-start-manage-dev-test-costs
  claim: Stopping and starting Aurora DB clusters helps you manage costs for development and test environments.
  scope: stopping and starting an Aurora DB cluster.
  link: [manage costs for development and test environments](../facts/aurora.md#aurora-stop-start-manage-dev-test-costs)
  link: [Stopping and starting Aurora DB clusters](../facts/aurora.md#aurora-stop-start-manage-dev-test-costs)
aurora-stopped-cluster-charges-storage-not-instance-hours
  claim: While an Aurora DB cluster is stopped, you are charged only for cluster storage, manual snapshots, and automated backup storage within your retention window, and not for any DB instance hours.
  scope: stopping and starting an Aurora DB cluster.
  link: [charged only for cluster storage](../facts/aurora.md#aurora-stopped-cluster-charges-storage-not-instance-hours)
  link: [aren't charged for any DB instance hours](../facts/aurora.md#aurora-stopped-cluster-charges-storage-not-instance-hours)
aurora-stopped-cluster-no-config-changes-no-backups
  claim: You cannot modify the configuration of an Aurora DB cluster, or any of its DB instances, while the cluster is stopped.
  scope: stopping and starting an Aurora DB cluster.
  link: [can't modify the configuration](../facts/aurora.md#aurora-stopped-cluster-no-config-changes-no-backups)
  link: [while the cluster is stopped](../facts/aurora.md#aurora-stopped-cluster-no-config-changes-no-backups)
aurora-storage-auto-repair-segment
  claim: When a segment of a disk volume fails, Aurora immediately repairs the segment, using data in the other volumes that make up the cluster volume.
  scope: Aurora cluster volume (shared storage).
  link: [Aurora immediately repairs the segment](../facts/aurora.md#aurora-storage-auto-repair-segment)
  link: [When a segment of a disk volume fails](../facts/aurora.md#aurora-storage-auto-repair-segment)
aurora-storage-copies-regardless-of-instance-azs
  claim: Aurora stores the copies of the cluster data across multiple Availability Zones in a single Region, whether or not the DB instances in the cluster span multiple Availability Zones.
  scope: per Aurora DB cluster volume.
  link: [regardless of whether the instances](../facts/aurora.md#aurora-storage-copies-regardless-of-instance-azs)
aurora-storage-features-depend-on-version
  claim: Some Aurora storage features, such as the maximum size of a cluster volume and automatic resizing when data is removed, depend on the Aurora version of the cluster.
  scope: Aurora cluster volume (shared storage).
  link: [maximum size of a cluster volume](../facts/aurora.md#aurora-storage-features-depend-on-version)
  link: [automatic resizing when data is removed](../facts/aurora.md#aurora-storage-features-depend-on-version)
aurora-storage-grows-10-gib-to-256-tib-in-10-gib-increments
  claim: Aurora storage starts at a minimum of 10 GiB and automatically grows up to 256 TiB in 10 GiB increments. The previous maximum for Aurora PostgreSQL was 128 TiB.
  scope: per Aurora DB cluster volume; maximum; not adjustable; 256 TiB applies to newer engine versions; earlier versions have a 128 TiB maximum (see the quotas and constraints page).
  link: [up to 256 TiB](../facts/aurora.md#aurora-storage-grows-10-gib-to-256-tib-in-10-gib-increments)
  link: [minimum of 10 GiB](../facts/aurora.md#aurora-storage-grows-10-gib-to-256-tib-in-10-gib-increments)
  link: [128 TiB](../facts/aurora.md#aurora-storage-grows-10-gib-to-256-tib-in-10-gib-increments)
  say: two hundred fifty-six tebibytes | ten gibibytes | one hundred twenty-eight tebibytes
  changed: 2025-07-03: was 128 TiB
aurora-storage-loss-tolerance-write-read
  claim: Aurora storage transparently handles the loss of up to two copies of data without affecting write availability, and the loss of up to three copies without affecting read availability.
  scope: per Aurora DB cluster volume; fixed.
  link: [up to two copies](../facts/aurora.md#aurora-storage-loss-tolerance-write-read)
  link: [up to three copies](../facts/aurora.md#aurora-storage-loss-tolerance-write-read)
  say: two copies | three copies
aurora-storage-segment-size-10-gib
  claim: Aurora automatically divides the database volume into 10 GiB segments spread across many disks.
  scope: per Aurora DB cluster volume; fixed.
  link: [10 GiB segments](../facts/aurora.md#aurora-storage-segment-size-10-gib)
  say: ten gibibyte segments
aurora-storage-separate-local-temp-files
  claim: Aurora uses separate local storage, not the cluster volume, for nonpersistent temporary files such as those used to sort large data sets and build indexes.
  scope: Aurora cluster volume (shared storage).
  link: [separate local storage for nonpersistent, temporary files](../facts/aurora.md#aurora-storage-separate-local-temp-files)
  link: [nonpersistent, temporary files](../facts/aurora.md#aurora-storage-separate-local-temp-files)
aurora-storage-six-copies-three-azs
  claim: The storage of each Aurora DB cluster consists of six copies of all your data, spread across three AZs.
  scope: per Aurora DB cluster volume; fixed.
  link: [six copies](../facts/aurora.md#aurora-storage-six-copies-three-azs)
  link: [three AZs](../facts/aurora.md#aurora-storage-six-copies-three-azs)
  say: six copies | three Availability Zones
aurora-storage-three-azs-from-subnet-group
  claim: Each Aurora DB cluster hosts copies of its storage in three separate AZs that Aurora selects automatically from the AZs in your DB subnet group.
  scope: Aurora cluster volume (shared storage).
  link: [three separate AZs selected automatically by Aurora](../facts/aurora.md#aurora-storage-three-azs-from-subnet-group)
  link: [AZs in your DB subnet group](../facts/aurora.md#aurora-storage-three-azs-from-subnet-group)
aurora-synchronous-replication-to-six-storage-nodes
  claim: When data is written to the primary DB instance, Aurora synchronously replicates the data across Availability Zones to six storage nodes associated with the cluster volume.
  scope: Aurora cluster volume (shared storage).
  link: [synchronously replicates the data across Availability Zones](../facts/aurora.md#aurora-synchronous-replication-to-six-storage-nodes)
  link: [six storage nodes](../facts/aurora.md#aurora-synchronous-replication-to-six-storage-nodes)
aurora-t-classes-dev-test-only
  claim: AWS recommends using the burstable T DB instance classes only for development, test, or other nonproduction servers.
  scope: Aurora DB instance classes.
  link: [T DB instance classes only for development, test](../facts/aurora.md#aurora-t-classes-dev-test-only)
  link: [other nonproduction servers](../facts/aurora.md#aurora-t-classes-dev-test-only)
aurora-table-size-limits-mysql-64-tib-postgresql-32-tib
  claim: For an Aurora MySQL DB cluster the maximum table size is 64 tebibytes (TiB), and for an Aurora PostgreSQL DB cluster it is 32 tebibytes (TiB).
  scope: per table, by engine; maximum; not adjustable.
  link: [64 tebibytes (TiB)](../facts/aurora.md#aurora-table-size-limits-mysql-64-tib-postgresql-32-tib)
  link: [32 tebibytes (TiB)](../facts/aurora.md#aurora-table-size-limits-mysql-64-tib-postgresql-32-tib)
  say: sixty-four tebibytes | thirty-two tebibytes
aurora-three-azs-copies-minimize-disk-loss
  claim: Because Aurora maintains multiple copies of the data in three Availability Zones, the chance of losing data as a result of a disk failure is greatly minimized.
  scope: Aurora cluster volume (shared storage).
  link: [copies of your data in three Availability Zones](../facts/aurora.md#aurora-three-azs-copies-minimize-disk-loss)
  link: [greatly minimized](../facts/aurora.md#aurora-three-azs-copies-minimize-disk-loss)
aurora-throughput-up-to-6x-stock-mysql-and-postgresql
  claim: Aurora delivers up to 6x the throughput of stock PostgreSQL and up to 6x the throughput of stock MySQL on similar hardware.
  scope: Aurora MySQL and Aurora PostgreSQL compared with stock engines on similar hardware; maximum; benchmark claim; the AWS database decision guide still says up to five times the throughput of standard MySQL.
  link: [up to 6x the throughput of stock MySQL](../facts/aurora.md#aurora-throughput-up-to-6x-stock-mysql-and-postgresql)
  link: [up to 6x the throughput of stock PostgreSQL](../facts/aurora.md#aurora-throughput-up-to-6x-stock-mysql-and-postgresql)
  say: up to six times the throughput of MySQL | up to six times the throughput of PostgreSQL
aurora-uses-rds-console-cli-api
  claim: Aurora uses the Amazon RDS console, AWS CLI commands, and API operations for routine tasks such as provisioning, patching, backup, recovery, failure detection, and repair.
  scope: Amazon Aurora overview.
  link: [Amazon RDS AWS Management Console interface](../facts/aurora.md#aurora-uses-rds-console-cli-api)
  link: [provisioning, patching, backup, recovery, failure detection, and repair](../facts/aurora.md#aurora-uses-rds-console-cli-api)
aurora-volume-shrinks-when-data-removed
  claim: When Aurora data is removed, for example by dropping or truncating a table, the space allocated for that data is freed, which helps minimize storage charges.
  scope: Aurora cluster volume (shared storage).
  link: [the space allocated for that data is freed](../facts/aurora.md#aurora-volume-shrinks-when-data-removed)
  link: [dropping or truncating a table](../facts/aurora.md#aurora-volume-shrinks-when-data-removed)
aurora-vpc-needs-two-subnets-two-azs
  claim: A VPC for an Aurora DB cluster must have at least two subnets, in two different Availability Zones in the AWS Region where you deploy the cluster.
  scope: Aurora DB clusters in a VPC.
  link: [must have at least two subnets](../facts/aurora.md#aurora-vpc-needs-two-subnets-two-azs)
  link: [two different Availability Zones](../facts/aurora.md#aurora-vpc-needs-two-subnets-two-azs)
aurora-vpc-no-additional-cost
  claim: There is no additional cost to run an Aurora DB cluster in a VPC.
  scope: Aurora DB clusters in a VPC.
  link: [no additional cost](../facts/aurora.md#aurora-vpc-no-additional-cost)
aurora-write-forwarding-aurora-handles-cross-region-networking
  claim: With write forwarding, Aurora handles the cross-Region networking setup, so you do not implement your own mechanism to send writes from a secondary Region to the primary.
  scope: write forwarding in an Aurora global database.
  link: [Aurora handles the cross-Region networking setup](../facts/aurora.md#aurora-write-forwarding-aurora-handles-cross-region-networking)
  link: [saves you from implementing your own mechanism](../facts/aurora.md#aurora-write-forwarding-aurora-handles-cross-region-networking)
aurora-write-forwarding-off-by-default-secondary
  claim: By default, write forwarding is not enabled when you add a secondary cluster to an Aurora global database.
  scope: per secondary cluster of an Aurora global database; default; adjustable.
  link: [write forwarding isn't enabled](../facts/aurora.md#aurora-write-forwarding-off-by-default-secondary)
  link: [add a secondary cluster](../facts/aurora.md#aurora-write-forwarding-off-by-default-secondary)
aurora-write-forwarding-primary-source-of-truth
  claim: With write forwarding, the data is always changed first on the primary cluster and then replicated to the secondary clusters, so the primary cluster is the source of truth.
  scope: write forwarding in an Aurora global database.
  link: [always changed first on the primary cluster](../facts/aurora.md#aurora-write-forwarding-primary-source-of-truth)
  link: [then replicated to the secondary clusters](../facts/aurora.md#aurora-write-forwarding-primary-source-of-truth)
aurora-write-forwarding-secondary-forward-sql-writes
  claim: With write forwarding enabled, secondary clusters in an Aurora global database forward SQL statements that perform write operations to the primary cluster.
  scope: write forwarding in an Aurora global database.
  link: [forward SQL statements that perform write operations](../facts/aurora.md#aurora-write-forwarding-secondary-forward-sql-writes)
  link: [With write forwarding enabled](../facts/aurora.md#aurora-write-forwarding-secondary-forward-sql-writes)
aurora-write-operations-managed-by-primary
  claim: Write operations in an Aurora cluster are managed by the primary instance.
  scope: Aurora Replicas in one Aurora DB cluster.
  link: [managed by the primary instance](../facts/aurora.md#aurora-write-operations-managed-by-primary)
  link: [Write operations](../facts/aurora.md#aurora-write-operations-managed-by-primary)
aurora-writer-reader-endpoints-follow-failover-instance-endpoints-not
  claim: Unlike instance endpoints, the writer and reader endpoints automatically change which DB instance they connect to if a DB instance in the cluster becomes unavailable.
  scope: Aurora cluster (writer) endpoint.
  link: [automatically change which DB instance they connect](../facts/aurora.md#aurora-writer-reader-endpoints-follow-failover-instance-endpoints-not)
  link: [Unlike the instance endpoints](../facts/aurora.md#aurora-writer-reader-endpoints-follow-failover-instance-endpoints-not)
aurora-zero-etl-monitors-pipeline-health
  claim: A zero-ETL integration monitors the health of the data pipeline and recovers from issues when possible.
  scope: Aurora zero-ETL integrations.
  link: [monitors the health of the data pipeline](../facts/aurora.md#aurora-zero-etl-monitors-pipeline-health)
  link: [recovers from issues when possible](../facts/aurora.md#aurora-zero-etl-monitors-pipeline-health)
aurora-zero-etl-multiple-sources-one-target
  claim: You can create zero-ETL integrations from multiple Aurora DB clusters into a single target data warehouse or lakehouse.
  scope: Aurora zero-ETL integrations.
  link: [into a single target data warehouse or lakehouse](../facts/aurora.md#aurora-zero-etl-multiple-sources-one-target)
  link: [derive insights across multiple applications](../facts/aurora.md#aurora-zero-etl-multiple-sources-one-target)
aurora-zero-etl-near-real-time-analytics
  claim: An Aurora zero-ETL integration with Amazon Redshift and Amazon SageMaker AI enables near real-time analytics and machine learning using data from Aurora.
  scope: Aurora zero-ETL integrations.
  link: [near real-time analytics and machine learning](../facts/aurora.md#aurora-zero-etl-near-real-time-analytics)
  link: [Amazon Redshift and Amazon SageMaker AI](../facts/aurora.md#aurora-zero-etl-near-real-time-analytics)
aurora-zero-etl-source-and-target
  claim: To create a zero-ETL integration, you specify an Aurora DB cluster as the source and a supported data warehouse or lakehouse as the target.
  scope: Aurora zero-ETL integrations.
  link: [an Aurora DB cluster as the source](../facts/aurora.md#aurora-zero-etl-source-and-target)
  link: [supported data warehouse or lakehouse as the target](../facts/aurora.md#aurora-zero-etl-source-and-target)
