facts card: 617 facts
rds-apply-immediately-downtime-risk
  claim: If any pending modification needs the DB instance to be temporarily unavailable, choosing Apply Immediately can cause unexpected downtime.
  scope: DB instance modifications.
  link: [can cause unexpected downtime](../facts/rds.md#rds-apply-immediately-downtime-risk)
rds-apply-immediately-vs-window
  claim: Modifications not applied immediately go into the pending modifications queue and are applied in the next maintenance window; choosing Apply Immediately applies the new change and everything already in the queue.
  scope: DB instance modifications.
  link: [pending modifications queue](../facts/rds.md#rds-apply-immediately-vs-window)
  link: [pending changes in the queue](../facts/rds.md#rds-apply-immediately-vs-window)
rds-auto-minor-upgrade-forced-security
  claim: Automatic minor version upgrades run in the maintenance window; for critical security issues or end of support, RDS applies a minor version upgrade even if Auto minor version upgrade is off.
  scope: minor version upgrades.
  link: [even if you haven't enabled](../facts/rds.md#rds-auto-minor-upgrade-forced-security)
  link: [critical security issues](../facts/rds.md#rds-auto-minor-upgrade-forced-security)
rds-automated-backup-needs-available-state
  claim: Automated backups happen only while the DB instance is in the available state; they do not occur in another state such as storage_full.
  scope: automated backups.
  link: [must be in the `available` state](../facts/rds.md#rds-automated-backup-needs-available-state)
  link: [for example, `storage_full`](../facts/rds.md#rds-automated-backup-needs-available-state)
rds-automated-backup-pitr-in-retention
  claim: With automated backups you can recover the DB instance to any point in time during the backup retention period.
  scope: automated backups.
  link: [any point in time](../facts/rds.md#rds-automated-backup-pitr-in-retention)
  link: [during the backup retention period](../facts/rds.md#rds-automated-backup-pitr-in-retention)
rds-automated-backup-whole-instance-window
  claim: RDS takes automated backups during the backup window as a storage volume snapshot of the whole DB instance, not of individual databases, and saves them according to the backup retention period that you specify.
  scope: automated backups.
  link: [backing up the entire DB instance](../facts/rds.md#rds-automated-backup-whole-instance-window)
  link: [during the backup window](../facts/rds.md#rds-automated-backup-whole-instance-window)
rds-aws-backup-centralize
  claim: AWS Backup is a fully managed service that centralizes and automates backup of data across AWS services and on premises, including RDS databases.
  scope: RDS automated backups and snapshots.
  link: [centralize and automate the backup of data](../facts/rds.md#rds-aws-backup-centralize)
rds-aws-backup-manual-snapshots-no-quota
  claim: You can manage RDS backups in AWS Backup; backups managed by AWS Backup count as manual DB snapshots but do not count toward the RDS DB snapshot quota.
  scope: RDS automated backups and snapshots.
  link: [considered manual DB snapshots](../facts/rds.md#rds-aws-backup-manual-snapshots-no-quota)
  link: [don't count toward the DB snapshot quota](../facts/rds.md#rds-aws-backup-manual-snapshots-no-quota)
rds-backup-aws-backup-not-in-snapshot-quota
  claim: Backups managed by AWS Backup are considered manual DB snapshots but don't count toward the manual snapshot quota.
  scope: per account, per Region; default; not adjustable.
  link: [don't count toward the manual snapshot quota](../facts/rds.md#rds-backup-aws-backup-not-in-snapshot-quota)
  say: they don't count toward the manual snapshot quota
rds-backup-daily-during-window
  claim: Automated backups occur daily during the preferred backup window, and a backup that needs more time continues after the window ends until it finishes.
  scope: per DB instance or Multi-AZ DB cluster; the backup window can't overlap the weekly maintenance window.
  link: [Automated backups occur daily](../facts/rds.md#rds-backup-daily-during-window)
  say: once a day in the backup window
rds-backup-geo-redundant-across-azs
  claim: Primary DB storage is in a single Availability Zone, while backup data including transaction logs is replicated across multiple Availability Zones for durability.
  scope: RDS automated backups and snapshots.
  link: [replicated across multiple Availability Zones](../facts/rds.md#rds-backup-geo-redundant-across-azs)
  link: [located within a single Availability Zone](../facts/rds.md#rds-backup-geo-redundant-across-azs)
rds-backup-io-suspension-multi-az
  claim: For MariaDB, MySQL, Oracle and PostgreSQL in a Multi-AZ deployment, I/O isn't suspended on the primary during backup because the backup is taken from the standby; for SQL Server I/O is suspended briefly because the backup is taken from the primary.
  scope: per DB instance; Single-AZ instances can see a brief I/O suspension, typically under a few seconds.
  link: [the backup is taken from the standby](../facts/rds.md#rds-backup-io-suspension-multi-az)
  say: Multi-AZ backups come from the standby
rds-backup-manual-snapshot-limit-automated-exempt
  claim: Manual DB instance snapshots have an adjustable default quota of 100 per Region (you can have up to 100 manual snapshots per Region); this limit doesn't apply to automated backups, and manual snapshots are not deleted when the DB instance is deleted.
  scope: per account, per Region; default; adjustable; automated backups don't count toward this limit.
  link: [up to 100 manual snapshots per Region](../facts/rds.md#rds-backup-manual-snapshot-limit-automated-exempt)
  link: [Manual snapshots are not deleted](../facts/rds.md#rds-backup-manual-snapshot-limit-automated-exempt)
  say: up to one hundred manual snapshots per Region | manual snapshots stay after the instance is deleted
rds-backup-retention-default
  claim: If you don't set a backup retention period, the default is one day for a DB instance created with the RDS API or AWS CLI and seven days for one created in the console.
  scope: per new DB instance; default; adjustable; the default depends on the tool used to create the instance.
  link: [one day](../facts/rds.md#rds-backup-retention-default)
  link: [seven days](../facts/rds.md#rds-backup-retention-default)
  say: one day | seven days
rds-backup-retention-multi-az-cluster
  claim: For a Multi-AZ DB cluster, you can set the backup retention period to between 1 and 35 days.
  scope: per Multi-AZ DB cluster; maximum; not adjustable.
  link: [between 1 and 35 days](../facts/rds.md#rds-backup-retention-multi-az-cluster)
  say: one to thirty-five days
rds-backup-retention-range
  claim: The backup retention period of a DB instance can be set between 0 and 35 days, and setting it to 0 disables automated backups.
  scope: per DB instance; maximum; not adjustable; Multi-AZ DB clusters allow 1 to 35 days.
  link: [between 0 and 35 days](../facts/rds.md#rds-backup-retention-range)
  link: [Setting the backup retention period to 0 disables automated backups](../facts/rds.md#rds-backup-retention-range)
  say: zero to thirty-five days | zero turns automated backups off
rds-backup-retention-zero-change-outage
  claim: Changing the backup retention period of a DB instance from 0 to a nonzero value, or from a nonzero value to 0, causes an outage.
  scope: per DB instance; only when crossing between 0 and a nonzero value.
  link: [An outage occurs](../facts/rds.md#rds-backup-retention-zero-change-outage)
  say: an outage occurs
rds-backup-storage-per-region-s3
  claim: RDS backup storage is counted per Region as the automated backups plus manual DB snapshots in that Region; copying a snapshot to another Region adds to that Region's backup storage; backups are stored in Amazon S3.
  scope: per AWS Region.
  link: [Backups are stored in Amazon S3.](../facts/rds.md#rds-backup-storage-per-region-s3)
  link: [for each AWS Region](../facts/rds.md#rds-backup-storage-per-region-s3)
rds-backup-window-default
  claim: If you don't specify a preferred backup window, Amazon RDS assigns a default 30-minute backup window selected at random from an 8-hour block of time for each AWS Region.
  scope: per DB instance or Multi-AZ DB cluster; default; adjustable; the 8-hour block depends on the Region.
  link: [30-minute backup window](../facts/rds.md#rds-backup-window-default)
  link: [an 8-hour block of time](../facts/rds.md#rds-backup-window-default)
  say: a thirty-minute backup window | an eight-hour block of time
rds-billing-begins-available-ends-terminate
  claim: Billing for a DB instance starts as soon as it is available and continues until the instance terminates, on deletion or instance failure; to stop paying instance hours you must stop or delete it.
  scope: DB instance hours.
  link: [as soon as the DB instance is available](../facts/rds.md#rds-billing-begins-available-ends-terminate)
  link: [you must stop or delete it](../facts/rds.md#rds-billing-begins-available-ends-terminate)
rds-billing-per-second-minimum
  claim: Partial DB instance hours are billed in one-second increments with a 10-minute minimum after a billable status change such as creating, starting or modifying.
  scope: per DB instance; minimum; after a billable status change.
  link: [one-second increments](../facts/rds.md#rds-billing-per-second-minimum)
  link: [a 10-minute minimum](../facts/rds.md#rds-billing-per-second-minimum)
  say: per second | with a ten-minute minimum
rds-blue-green-cost-about-2x
  claim: While a blue/green deployment exists you pay for the green instances at the same price as the blue ones, so you pay approximately 2x the cost of the workload for its lifespan.
  scope: RDS Blue/Green Deployments.
  link: [approximately 2x the cost](../facts/rds.md#rds-blue-green-cost-about-2x)
  say: approximately two times the cost
rds-blue-green-engines-only
  claim: Amazon RDS Blue/Green Deployments are supported only for RDS for MariaDB, RDS for MySQL and RDS for PostgreSQL (not RDS for Oracle, SQL Server or Db2).
  scope: RDS Blue/Green Deployments.
  link: [RDS for MySQL, and RDS for PostgreSQL only](../facts/rds.md#rds-blue-green-engines-only)
rds-blue-green-no-rollback
  claim: The RDS FAQ says you cannot use Blue/Green Deployments to roll back changes.
  scope: RDS Blue/Green Deployments.
  link: [cannot use Amazon RDS Blue/Green Deployments to rollback](../facts/rds.md#rds-blue-green-no-rollback)
rds-blue-green-no-secrets-manager-passwords
  claim: Blue/green deployments don't support managing master user passwords with AWS Secrets Manager.
  scope: RDS Blue/Green Deployments.
  link: [don't support managing master user passwords](../facts/rds.md#rds-blue-green-no-secrets-manager-passwords)
rds-blue-green-pitr-not-carried
  claim: After a blue/green switchover, point-in-time recovery history does not carry over to the new production DB instance; its earliest restorable time starts when the green environment was created.
  scope: RDS Blue/Green Deployments.
  link: [history doesn't carry over](../facts/rds.md#rds-blue-green-pitr-not-carried)
rds-blue-green-same-account
  claim: The blue and green environments of a blue/green deployment must be in the same AWS account.
  scope: RDS Blue/Green Deployments.
  link: [must be in the same AWS account](../facts/rds.md#rds-blue-green-same-account)
rds-blue-green-staging-in-sync
  claim: A blue/green deployment creates a staging environment (green) that copies the current production environment (blue) and stays in sync with it, so you can make and test database changes before implementing them in production.
  scope: RDS Blue/Green Deployments.
  link: [stays in sync with the current production environment](../facts/rds.md#rds-blue-green-staging-in-sync)
rds-blue-green-supports-proxy
  claim: The user guide says RDS Blue/Green Deployments support Amazon RDS Proxy and smart drivers, which reduce writer node upgrade downtime during switchover by redirecting connections to the new production environment without waiting for DNS propagation.
  scope: RDS Blue/Green Deployments.
  link: [support Amazon RDS Proxy and smart drivers](../facts/rds.md#rds-blue-green-supports-proxy)
rds-blue-green-switchover-guardrails
  claim: When you start a switchover, RDS runs basic readiness checks called switchover guardrails that prevent the switchover if the environments aren't ready, to avoid longer than expected downtime and loss of data between the blue and green environments.
  scope: RDS Blue/Green Deployments.
  link: [switchover guardrails](../facts/rds.md#rds-blue-green-switchover-guardrails)
rds-blue-green-switchover-under-a-minute
  claim: An RDS blue/green switchover typically takes under a minute, with no data loss and no need for application changes.
  scope: RDS Blue/Green Deployments.
  link: [typically takes under a minute](../facts/rds.md#rds-blue-green-switchover-under-a-minute)
  link: [no data loss](../facts/rds.md#rds-blue-green-switchover-under-a-minute)
rds-blue-green-uses
  claim: Typical blue/green changes are upgrading the major or minor DB engine version, upgrading the underlying file system configuration and changing database parameters in the staging environment.
  scope: RDS Blue/Green Deployments.
  link: [upgrade the major or minor DB engine version](../facts/rds.md#rds-blue-green-uses)
rds-bp-backup-window-low-write-iops
  claim: AWS's operational guideline is to enable automatic backups and set the backup window to occur during the daily low in write IOPS, because that is when a backup is least disruptive to database usage.
  scope: RDS basic operational guidelines.
  link: [daily low in write IOPS](../facts/rds.md#rds-bp-backup-window-low-write-iops)
rds-bp-dns-ttl-under-30-seconds
  claim: If a client application caches the DNS data of DB instances, AWS advises a TTL of less than 30 seconds, because the IP address of a DB instance can change after a failover.
  scope: client DNS cache of DB instance endpoints; maximum.
  link: [less than 30 seconds](../facts/rds.md#rds-bp-dns-ttl-under-30-seconds)
  say: less than thirty seconds
rds-bp-more-io-capacity
  claim: If the workload needs more I/O than provisioned, recovery after a failover or database failure will be slow; to increase I/O capacity, migrate to a DB instance class with high I/O capacity, convert from General Purpose SSD to Provisioned IOPS SSD storage, or, if you already use Provisioned IOPS storage, provision additional throughput capacity.
  scope: RDS basic operational guidelines.
  link: [recovery after a failover or database failure](../facts/rds.md#rds-bp-more-io-capacity)
rds-bp-sla-requires-guidelines
  claim: The Amazon RDS Service Level Agreement requires that you follow the basic operational guidelines that AWS lists for working with Amazon RDS.
  scope: RDS basic operational guidelines.
  link: [Service Level Agreement requires](../facts/rds.md#rds-bp-sla-requires-guidelines)
rds-bp-test-failover
  claim: AWS advises testing failover to learn how long it takes for your use case and to make sure the application reconnects automatically to the new DB instance.
  scope: RDS basic operational guidelines.
  link: [Test failover for your DB instance](../facts/rds.md#rds-bp-test-failover)
rds-bp-working-set-in-memory
  claim: An RDS performance best practice is to allocate enough RAM so that the working set (the data and indexes frequently in use) resides almost completely in memory; to check, the ReadIOPS metric should be small and stable while the DB instance is under load.
  scope: RDS basic operational guidelines.
  link: [resides almost completely in memory](../facts/rds.md#rds-bp-working-set-in-memory)
rds-case-crossuite-postgresql
  claim: In an AWS case study, the Crossuite team used Amazon RDS for PostgreSQL for the backend, taking advantage of its scalability and reliability.
  scope: AWS customer case study.
  link: [AWS Relational Database Service (RDS) PostgreSQL](../facts/rds.md#rds-case-crossuite-postgresql)
rds-case-crossuite-uptime
  claim: In an AWS case study, Crossuite reports that it achieved 99.9 percent uptime while reducing latency for its customers.
  scope: AWS customer case study.
  link: [99.9 percent uptime](../facts/rds.md#rds-case-crossuite-uptime)
  say: ninety-nine point nine percent uptime
rds-case-prove-cost-five-times
  claim: Prove reports that it reduced database management cost by five times after migrating to Amazon RDS.
  scope: AWS customer case study.
  link: [reduced database management cost by five times](../facts/rds.md#rds-case-prove-cost-five-times)
rds-case-prove-oracle-to-rds
  claim: Prove, an identity verification company, moved from managing its own Oracle database on premises to Amazon RDS, and its engineers cut in half the time they spend managing applications.
  scope: AWS customer case study.
  link: [cut in half how much time](../facts/rds.md#rds-case-prove-oracle-to-rds)
rds-change-additional-storage-volumes-2025-11
  claim: On November 14, 2025 RDS for Oracle and RDS for SQL Server gained up to three additional storage volumes (gp3 or io2 each), for up to 256 TiB of total storage per DB instance.
  scope: RDS DB instance storage and performance.
  link: [November 14, 2025](../facts/rds.md#rds-change-additional-storage-volumes-2025-11)
  link: [up to 256 TiB per DB instance](../facts/rds.md#rds-change-additional-storage-volumes-2025-11)
  link: [up to three additional storage volumes](../facts/rds.md#rds-change-additional-storage-volumes-2025-11)
  say: November fourteenth, twenty twenty-five | up to two hundred fifty-six tebibytes per DB instance
rds-change-blue-green-2022-11
  claim: On November 27, 2022 Amazon RDS added Blue/Green Deployments: you change a staging environment, test it without affecting production, then promote it to production with minimal downtime.
  scope: RDS Blue/Green Deployments.
  link: [November 27, 2022](../facts/rds.md#rds-change-blue-green-2022-11)
  link: [with minimal downtime](../facts/rds.md#rds-change-blue-green-2022-11)
  say: November twenty-seventh, twenty twenty-two
rds-change-blue-green-storage-2024-11
  claim: From November 20, 2024 you can adjust storage settings in the green environment of an RDS blue/green deployment.
  scope: RDS Blue/Green Deployments.
  link: [November 20, 2024](../facts/rds.md#rds-change-blue-green-storage-2024-11)
  link: [adjust storage settings in the green environment](../facts/rds.md#rds-change-blue-green-storage-2024-11)
  say: November twentieth, twenty twenty-four
rds-change-blue-green-switchover-five-seconds-2026-01
  claim: From January 20, 2026, RDS Blue/Green Deployments switchover for single-Region configurations typically has five seconds or lower of writer downtime when applications connect directly to the database endpoint, and two seconds or lower with the AWS Advanced JDBC Driver.
  scope: RDS Blue/Green Deployments.
  link: [January 20, 2026](../facts/rds.md#rds-change-blue-green-switchover-five-seconds-2026-01)
  link: [typically five seconds or lower downtime](../facts/rds.md#rds-change-blue-green-switchover-five-seconds-2026-01)
  link: [typically see two seconds or lower](../facts/rds.md#rds-change-blue-green-switchover-five-seconds-2026-01)
  say: January twentieth, twenty twenty-six | typically five seconds or lower downtime | typically two seconds or lower
rds-change-cross-region-cross-account-snapshot-copy-2025-09
  claim: Since September 23, 2025 Amazon RDS can copy a snapshot across Regions and accounts in one step; before, customers did it in a two step process (first to another Region, then to another account, or the reverse).
  scope: DB snapshot copy across Regions and accounts.
  link: [September 23, 2025](../facts/rds.md#rds-change-cross-region-cross-account-snapshot-copy-2025-09)
  link: [without performing it sequentially as two separate copies](../facts/rds.md#rds-change-cross-region-cross-account-snapshot-copy-2025-09)
  link: [two step process](../facts/rds.md#rds-change-cross-region-cross-account-snapshot-copy-2025-09)
  say: September twenty-third, twenty twenty-five | two step process
  changed: 2025-09-23: was two step process
rds-change-custom-oracle-end-of-support
  claim: AWS will end support for Amazon RDS Custom for Oracle on March 31, 2027 (notice in the RDS document history dated March 31, 2026).
  scope: Amazon RDS Custom.
  link: [March 31, 2027](../facts/rds.md#rds-change-custom-oracle-end-of-support)
  link: [March 31, 2026](../facts/rds.md#rds-change-custom-oracle-end-of-support)
  say: March thirty-first, twenty twenty-seven | March thirty-first, twenty twenty-six
rds-change-database-insights-2025-02
  claim: On February 20, 2025 Amazon RDS gained support for monitoring with CloudWatch Database Insights.
  scope: CloudWatch Database Insights and Performance Insights.
  link: [February 20, 2025](../facts/rds.md#rds-change-database-insights-2025-02)
  link: [use Database Insights to monitor](../facts/rds.md#rds-change-database-insights-2025-02)
  say: February twentieth, twenty twenty-five
rds-change-database-savings-plans-2025-12
  claim: On December 2, 2025 AWS announced Database Savings Plans, which save up to 35% for a commitment to a consistent amount of usage (in $/hour) over a one-year term with no upfront payment; Amazon RDS is one of the supported services.
  scope: Database Savings Plans.
  link: [December 2, 2025](../facts/rds.md#rds-change-database-savings-plans-2025-12)
  link: [save up to 35%](../facts/rds.md#rds-change-database-savings-plans-2025-12)
  link: [one-year term with no upfront payment](../facts/rds.md#rds-change-database-savings-plans-2025-12)
  say: December second, twenty twenty-five | save up to thirty-five percent
rds-change-dedicated-log-volume-2023-10
  claim: On October 17, 2023 Amazon RDS added dedicated log volumes (DLV) for RDS for MariaDB, MySQL and PostgreSQL, for databases with large allocated storage, high IOPS needs or latency-sensitive workloads.
  scope: RDS DB instance storage and performance.
  link: [October 17, 2023](../facts/rds.md#rds-change-dedicated-log-volume-2023-10)
  link: [dedicated log volume (DLV)](../facts/rds.md#rds-change-dedicated-log-volume-2023-10)
  say: October seventeenth, twenty twenty-three
rds-change-ena-express-multi-az-2026-05
  claim: On May 26, 2026 RDS Multi-AZ instances began to use ENA Express for replication traffic between Availability Zones, with up to 25 Gbps single-flow bandwidth for cross-AZ replication.
  scope: Cross-AZ ENA Express for Multi-AZ DB instances.
  link: [May 26, 2026](../facts/rds.md#rds-change-ena-express-multi-az-2026-05)
  link: [up to 25 Gbps single-flow bandwidth](../facts/rds.md#rds-change-ena-express-multi-az-2026-05)
  say: May twenty-sixth, twenty twenty-six | up to twenty-five gigabits per second of single-flow bandwidth
rds-change-ena-express-no-charge
  claim: ENA Express for Amazon RDS Multi-AZ replication has no additional charge and is offered for RDS for MariaDB, MySQL, PostgreSQL, Db2 and Oracle (announced May 26, 2026).
  scope: Cross-AZ ENA Express for Multi-AZ DB instances.
  link: [May 26, 2026](../facts/rds.md#rds-change-ena-express-no-charge)
  link: [at no additional charge](../facts/rds.md#rds-change-ena-express-no-charge)
  say: May twenty-sixth, twenty twenty-six
rds-change-extended-support-auto-enable-2024-02
  claim: From February 15, 2024 Amazon RDS automatically enables RDS Extended Support when RDS for MySQL and RDS for PostgreSQL major engine versions reach the RDS end of standard support date.
  scope: RDS Extended Support.
  link: [February 15, 2024](../facts/rds.md#rds-change-extended-support-auto-enable-2024-02)
  link: [automatically enables Amazon RDS Extended Support](../facts/rds.md#rds-change-extended-support-auto-enable-2024-02)
  say: February fifteenth, twenty twenty-four
rds-change-extended-support-create-restore-2024-03
  claim: From March 21, 2024, creating or restoring an RDS for MySQL 5.7 or RDS for PostgreSQL 11 database enrolls it automatically in RDS Extended Support; you can opt out to avoid charges after the end of standard support.
  scope: RDS Extended Support.
  link: [March 21, 2024](../facts/rds.md#rds-change-extended-support-create-restore-2024-03)
  link: [opt out of RDS Extended Support](../facts/rds.md#rds-change-extended-support-create-restore-2024-03)
  say: March twenty-first, twenty twenty-four
rds-change-gp3-storage-2022-11
  claim: On November 4, 2022 Amazon RDS added General Purpose SSD (gp3) storage, which lets you set storage performance independently of storage capacity.
  scope: RDS DB instance storage and performance.
  link: [November 4, 2022](../facts/rds.md#rds-change-gp3-storage-2022-11)
  link: [independently of storage capacity](../facts/rds.md#rds-change-gp3-storage-2022-11)
  say: November fourth, twenty twenty-two
rds-change-io2-block-express-2024-03
  claim: On March 6, 2024 Amazon RDS added the io2 Block Express storage type for DB instances.
  scope: RDS DB instance storage and performance.
  link: [March 6, 2024](../facts/rds.md#rds-change-io2-block-express-2024-03)
  link: [io2 Block Express storage type](../facts/rds.md#rds-change-io2-block-express-2024-03)
  say: March sixth, twenty twenty-four
rds-change-magnetic-restore-ends-2026-07
  claim: Amazon RDS completed the deprecation of magnetic storage: starting July 1, 2026 you can no longer restore a snapshot to magnetic storage and must choose another storage type such as gp3 or io2 Block Express (history row dated June 25, 2026).
  scope: RDS DB instance storage and performance.
  link: [July 1, 2026](../facts/rds.md#rds-change-magnetic-restore-ends-2026-07)
  link: [June 25, 2026](../facts/rds.md#rds-change-magnetic-restore-ends-2026-07)
  link: [such as gp3 or io2 Block Express](../facts/rds.md#rds-change-magnetic-restore-ends-2026-07)
  say: July first, twenty twenty-six | June twenty-fifth, twenty twenty-six
rds-change-optimized-reads-mysql-2022-11
  claim: On November 27, 2022 Amazon RDS added Optimized Reads for faster query processing on RDS for MySQL DB instances.
  scope: RDS Optimized Reads and Optimized Writes.
  link: [November 27, 2022](../facts/rds.md#rds-change-optimized-reads-mysql-2022-11)
  link: [faster query processing](../facts/rds.md#rds-change-optimized-reads-mysql-2022-11)
  say: November twenty-seventh, twenty twenty-two
rds-change-optimized-writes-mysql-2022-11
  claim: On November 27, 2022 Amazon RDS added Optimized Writes to improve the performance of write transactions for RDS for MySQL DB instances.
  scope: RDS Optimized Reads and Optimized Writes.
  link: [November 27, 2022](../facts/rds.md#rds-change-optimized-writes-mysql-2022-11)
  link: [improve the performance of write transactions](../facts/rds.md#rds-change-optimized-writes-mysql-2022-11)
  say: November twenty-seventh, twenty twenty-two
rds-change-postgresql-delayed-replicas-2025-08
  claim: On August 22, 2025 RDS for PostgreSQL added delayed read replicas: you set a minimum time a replica lags behind the source, as a buffer against human errors such as accidental table drops.
  scope: delayed read replicas.
  link: [August 22, 2025](../facts/rds.md#rds-change-postgresql-delayed-replicas-2025-08)
  link: [accidental table drops](../facts/rds.md#rds-change-postgresql-delayed-replicas-2025-08)
  say: August twenty-second, twenty twenty-five
rds-change-proxy-multi-az-clusters-2023-11
  claim: On November 9, 2023 RDS Proxy gained support for connecting to Multi-AZ DB clusters.
  scope: Amazon RDS Proxy.
  link: [November 9, 2023](../facts/rds.md#rds-change-proxy-multi-az-clusters-2023-11)
  link: [connecting to Multi-AZ DB clusters](../facts/rds.md#rds-change-proxy-multi-az-clusters-2023-11)
  say: November ninth, twenty twenty-three
rds-change-read-replicas-15-2022-10
  claim: On October 20, 2022 Amazon RDS for MariaDB, MySQL and PostgreSQL DB instances gained support for up to 15 read replicas.
  scope: RDS DB instance read replicas.
  link: [October 20, 2022](../facts/rds.md#rds-change-read-replicas-15-2022-10)
  link: [up to 15 read replicas](../facts/rds.md#rds-change-read-replicas-15-2022-10)
  say: October twentieth, twenty twenty-two | up to fifteen read replicas
rds-change-secrets-manager-master-password-2022-12
  claim: On December 22, 2022 Amazon RDS gained the ability to manage the master user password of a DB instance or Multi-AZ DB cluster in AWS Secrets Manager.
  scope: RDS-managed master user password in AWS Secrets Manager.
  link: [December 22, 2022](../facts/rds.md#rds-change-secrets-manager-master-password-2022-12)
  link: [manage the master user password](../facts/rds.md#rds-change-secrets-manager-master-password-2022-12)
  say: December twenty-second, twenty twenty-two
rds-change-storage-modifications-four-2026-07
  claim: On July 15, 2026 Amazon RDS began to allow up to four storage modifications per DB instance in a rolling 24-hour window; a new modification can start as soon as storage optimization of the previous one completes, instead of waiting for the six-hour cool-off period.
  scope: storage modifications of a DB instance.
  link: [July 15, 2026](../facts/rds.md#rds-change-storage-modifications-four-2026-07)
  link: [up to four storage modifications](../facts/rds.md#rds-change-storage-modifications-four-2026-07)
  link: [rolling 24-hour window](../facts/rds.md#rds-change-storage-modifications-four-2026-07)
  link: [six-hour cool-off period](../facts/rds.md#rds-change-storage-modifications-four-2026-07)
  say: July fifteenth, twenty twenty-six | up to four storage modifications | rolling twenty-four-hour window | six-hour cool-off period
  changed: 2026-07-15: was six-hour cool-off period
rds-change-zero-etl-postgresql-oracle-2025-07
  claim: On July 23, 2025 zero-ETL integrations became available with RDS for PostgreSQL and RDS for Oracle as the source.
  scope: RDS zero-ETL integrations.
  link: [July 23, 2025](../facts/rds.md#rds-change-zero-etl-postgresql-oracle-2025-07)
  link: [RDS for PostgreSQL and RDS for Oracle](../facts/rds.md#rds-change-zero-etl-postgresql-oracle-2025-07)
  say: July twenty-third, twenty twenty-five
rds-change-zero-etl-redshift-ga-2024-09
  claim: Zero-ETL integrations from RDS for MySQL to Amazon Redshift became generally available on September 12, 2024; they make transactional data available in Redshift within seconds of being written.
  scope: RDS zero-ETL integrations.
  link: [September 12, 2024](../facts/rds.md#rds-change-zero-etl-redshift-ga-2024-09)
  link: [within seconds of it being written](../facts/rds.md#rds-change-zero-etl-redshift-ga-2024-09)
  say: September twelfth, twenty twenty-four
rds-class-burstable-baseline-unlimited
  claim: Burstable db.t3 classes provide a baseline performance level with the ability to burst to full CPU usage and are configured for Unlimited mode; db.t4g instances are also configured for Unlimited mode and can burst beyond the baseline over a 24-hour window for an additional charge.
  scope: burstable-performance DB instance classes.
  link: [baseline performance level](../facts/rds.md#rds-class-burstable-baseline-unlimited)
  link: [configured for Unlimited mode](../facts/rds.md#rds-class-burstable-baseline-unlimited)
  link: [for an additional charge](../facts/rds.md#rds-class-burstable-baseline-unlimited)
rds-class-general-purpose-balanced
  claim: The db.m7g general-purpose DB instance classes, powered by AWS Graviton3 processors, deliver balanced compute, memory, and networking for a broad range of general-purpose workloads.
  scope: db.m7g DB instance classes.
  link: [balanced compute, memory, and networking](../facts/rds.md#rds-class-general-purpose-balanced)
rds-class-memory-optimized-memory-intensive
  claim: The memory-optimized db.z1d instance classes are optimized for memory-intensive applications, with high compute capacity and a high memory footprint; the db.x1 classes offer one of the lowest price per GiB of RAM among the DB instance classes.
  scope: DB instance classes.
  link: [optimized for memory-intensive applications](../facts/rds.md#rds-class-memory-optimized-memory-intensive)
  link: [lowest price per GiB of RAM](../facts/rds.md#rds-class-memory-optimized-memory-intensive)
rds-class-types-use-cases
  claim: Amazon RDS offers general-purpose, memory-optimized (including the Z family), compute-optimized and burstable-performance DB instance classes.
  scope: DB instance classes.
  link: [memory-optimized Z family](../facts/rds.md#rds-class-types-use-cases)
  link: [burstable-performance DB instance class types](../facts/rds.md#rds-class-types-use-cases)
  link: [compute-optimized instance class types](../facts/rds.md#rds-class-types-use-cases)
rds-cloudwatch-metrics-every-minute-free
  claim: Amazon RDS automatically sends metrics to CloudWatch every minute for each active database, with no additional charge for these RDS metrics.
  scope: each active database.
  link: [every minute](../facts/rds.md#rds-cloudwatch-metrics-every-minute-free)
  link: [You don't get additional charges](../facts/rds.md#rds-cloudwatch-metrics-every-minute-free)
rds-cloudwatch-monitor-capacity-limits
  claim: AWS's basic operational guidelines say to use metrics to monitor memory, CPU, replica lag and storage usage, with CloudWatch notifications when usage patterns change or the deployment approaches capacity limits.
  scope: RDS basic operational guidelines.
  link: [memory, CPU, replica lag, and storage usage](../facts/rds.md#rds-cloudwatch-monitor-capacity-limits)
  link: [approaches capacity limits](../facts/rds.md#rds-cloudwatch-monitor-capacity-limits)
rds-compare-active-instances
  claim: In a non-Aurora Multi-AZ deployment only the primary instance is active, while all read replicas are accessible and can be used for read scaling.
  scope: non-Aurora RDS: Multi-AZ deployments, multi-Region deployments and read replicas.
  link: [only the primary instance is active](../facts/rds.md#rds-compare-active-instances)
  link: [can be used for read scaling](../facts/rds.md#rds-compare-active-instances)
rds-compare-backups
  claim: In a non-Aurora Multi-AZ deployment automated backups are taken from the standby; read replicas have no backups configured by default.
  scope: non-Aurora RDS: Multi-AZ deployments, multi-Region deployments and read replicas.
  link: [automated backups are taken from standby](../facts/rds.md#rds-compare-backups)
  link: [No backups configured by default](../facts/rds.md#rds-compare-backups)
rds-compare-engine-upgrades
  claim: For non-Aurora RDS, engine version upgrades in a Multi-AZ deployment happen on the primary, while a read replica's engine version upgrade is independent from its source instance.
  scope: non-Aurora RDS: Multi-AZ deployments, multi-Region deployments and read replicas.
  link: [independent from source instance](../facts/rds.md#rds-compare-engine-upgrades)
rds-compare-failover-vs-promote
  claim: A non-Aurora Multi-AZ deployment fails over automatically to the standby when a problem is detected, while a non-Aurora read replica can be manually promoted to a standalone database instance.
  scope: non-Aurora RDS: Multi-AZ deployments, multi-Region deployments and read replicas.
  link: [Automatic failover to standby](../facts/rds.md#rds-compare-failover-vs-promote)
  link: [Can be manually promoted](../facts/rds.md#rds-compare-failover-vs-promote)
rds-compare-maz-az-outage
  claim: In an AZ failure, a Single-AZ deployment risks data loss and hours of failover time; Multi-AZ with one standby fails over automatically to the up-to-date standby; with two readable standbys one of the remaining standbys takes over the writes.
  scope: RDS deployment options: Single-AZ, Multi-AZ with one standby, Multi-AZ with two readable standbys.
  link: [risk data loss and hours of failover time](../facts/rds.md#rds-compare-maz-az-outage)
  link: [automatically failover to the up-to-date standby](../facts/rds.md#rds-compare-maz-az-outage)
rds-compare-maz-commit-latency
  claim: Multi-AZ with two readable standbys gives up to 2x faster transaction commits than Multi-AZ with one standby.
  scope: RDS deployment options: Single-AZ, Multi-AZ with one standby, Multi-AZ with two readable standbys.
  link: [Up to 2x faster transaction commits](../facts/rds.md#rds-compare-maz-commit-latency)
  say: up to two times faster transaction commits
rds-compare-maz-engines
  claim: The Multi-AZ deployment with two readable standbys is offered only for RDS for PostgreSQL and RDS for MySQL, while Single-AZ and Multi-AZ with one standby are offered for all six RDS engines.
  scope: RDS deployment options: Single-AZ, Multi-AZ with one standby, Multi-AZ with two readable standbys.
  link: [Amazon RDS for PostgreSQL Amazon RDS for MySQL](../facts/rds.md#rds-compare-maz-engines)
rds-compare-maz-failover-time
  claim: Failover time: Single-AZ has no automatic failover (a point-in-time restore can take several hours, and updates after the latest restorable time, typically the last 5 minutes, are lost); Multi-AZ with one standby has a new primary in as quickly as 60 seconds; Multi-AZ with two readable standbys typically in under 35 seconds, depending on replica lag.
  scope: RDS deployment options: Single-AZ, Multi-AZ with one standby, Multi-AZ with two readable standbys.
  link: [as quickly as 60 seconds](../facts/rds.md#rds-compare-maz-failover-time)
  link: [typically under 35 seconds](../facts/rds.md#rds-compare-maz-failover-time)
  link: [can take several hours](../facts/rds.md#rds-compare-maz-failover-time)
  say: as quickly as sixty seconds | typically under thirty-five seconds
rds-compare-maz-minor-upgrade-downtime
  claim: With Automatic Minor Version Upgrades, Single-AZ and Multi-AZ with one standby take their minor upgrade downtime in the 30-minute maintenance window; Multi-AZ with two readable standbys has typically under 1 second with RDS Proxy or an open source proxy, and typically under 35 seconds alone.
  scope: RDS deployment options: Single-AZ, Multi-AZ with one standby, Multi-AZ with two readable standbys.
  link: [Typically under 1 second](../facts/rds.md#rds-compare-maz-minor-upgrade-downtime)
  link: [Typically under 35 seconds](../facts/rds.md#rds-compare-maz-minor-upgrade-downtime)
  say: typically under one second | typically under thirty-five seconds
rds-compare-maz-read-capacity
  claim: Single-AZ and Multi-AZ with one standby add no read capacity (the one standby is only a passive failover target); in Multi-AZ with two readable standbys, both standbys are failover targets and also serve read traffic.
  scope: RDS deployment options: Single-AZ, Multi-AZ with one standby, Multi-AZ with two readable standbys.
  link: [only a passive failover target](../facts/rds.md#rds-compare-maz-read-capacity)
  link: [serve read traffic](../facts/rds.md#rds-compare-maz-read-capacity)
rds-compare-placement
  claim: Multi-AZ deployments always span at least two Availability Zones in one Region; a read replica can be in the same Availability Zone, in another Availability Zone, or in another Region.
  scope: non-Aurora RDS: Multi-AZ deployments, multi-Region deployments and read replicas.
  link: [Always span at least two Availability Zones](../facts/rds.md#rds-compare-placement)
  link: [Cross-AZ, or Cross-Region](../facts/rds.md#rds-compare-placement)
rds-compare-purpose-ha-dr-scale
  claim: AWS states the main purpose of each option: Multi-AZ deployments are for high availability, multi-Region deployments are for disaster recovery and local performance, and read replicas are for scalability.
  scope: non-Aurora RDS: Multi-AZ deployments, multi-Region deployments and read replicas.
  link: [Main purpose is high availability](../facts/rds.md#rds-compare-purpose-ha-dr-scale)
  link: [Main purpose is scalability](../facts/rds.md#rds-compare-purpose-ha-dr-scale)
  link: [disaster recovery and local performance](../facts/rds.md#rds-compare-purpose-ha-dr-scale)
rds-compare-replication-sync-async
  claim: Multi-AZ deployments use synchronous replication; multi-Region deployments and read replicas use asynchronous replication.
  scope: non-Aurora RDS: Multi-AZ deployments, multi-Region deployments and read replicas.
  link: [synchronous replication](../facts/rds.md#rds-compare-replication-sync-async)
  link: [Asynchronous replication](../facts/rds.md#rds-compare-replication-sync-async)
rds-console-dms-cdc-keeps-target-available
  claim: In the RDS console migration, full load and full load plus CDC require downtime of the target, while change data capture (CDC) only keeps the target available and migrates ongoing changes.
  scope: RDS console migration with AWS DMS.
  link: [keep your target database available through the migration](../facts/rds.md#rds-console-dms-cdc-keeps-target-available)
  link: [This option requires downtime.](../facts/rds.md#rds-console-dms-cdc-keeps-target-available)
rds-console-dms-migration
  claim: The RDS console can migrate a MySQL, MariaDB or PostgreSQL database from EC2, on premises or another cloud into an equivalent RDS database using AWS DMS; the source and target must have the same engine and compatible versions.
  scope: RDS for MySQL, MariaDB and PostgreSQL targets.
  link: [AWS Database Migration Service (AWS DMS)](../facts/rds.md#rds-console-dms-migration)
  link: [same database engine and compatible engine versions](../facts/rds.md#rds-console-dms-migration)
rds-cross-region-backup-charges
  claim: Cross-Region automated backups pay DB snapshot copy charges for the data transfer and standard storage charges in the destination Region.
  scope: cross-Region automated backups.
  link: [DB snapshot copy charges apply](../facts/rds.md#rds-cross-region-backup-charges)
  link: [standard charges apply to storage](../facts/rds.md#rds-cross-region-backup-charges)
rds-cross-region-backup-not-multi-az-cluster
  claim: Automated backup replication to another Region is not supported for Multi-AZ DB clusters, but it is supported for Multi-AZ DB instance deployments.
  scope: cross-Region automated backups.
  link: [isn't supported for Multi-AZ DB clusters](../facts/rds.md#rds-cross-region-backup-not-multi-az-cluster)
  link: [supported for Multi-AZ DB instance deployments](../facts/rds.md#rds-cross-region-backup-not-multi-az-cluster)
rds-cross-region-backup-pitr-destination
  claim: You can restore a DB instance to a specific point in time from a replicated backup; in the console you choose the destination Region (where backups are replicated to), and you restore the DB instance in the destination Region.
  scope: cross-Region automated backups.
  link: [to a specific point in time](../facts/rds.md#rds-cross-region-backup-pitr-destination)
  link: [from a replicated backup](../facts/rds.md#rds-cross-region-backup-pitr-destination)
rds-cross-region-backup-replication
  claim: For disaster recovery, you can configure a DB instance to replicate its snapshots and transaction logs to a destination Region; RDS starts the cross-Region copy as soon as each is ready.
  scope: DB instances.
  link: [replicate snapshots and transaction logs](../facts/rds.md#rds-cross-region-backup-replication)
  link: [as soon as they are ready](../facts/rds.md#rds-cross-region-backup-replication)
rds-cross-region-replica-all-engines
  claim: You can create a cross-Region read replica from a source Db2, MariaDB, Microsoft SQL Server, MySQL, Oracle or PostgreSQL DB instance.
  scope: cross-Region read replicas; Region and version availability vary.
  link: [in a different AWS Region](../facts/rds.md#rds-cross-region-replica-all-engines)
  link: [Db2, MariaDB, Microsoft SQL Server, MySQL, Oracle, or PostgreSQL](../facts/rds.md#rds-cross-region-replica-all-engines)
rds-cross-region-replica-chain-cuts-transfer
  claim: For MySQL and MariaDB you can reduce cross-Region data transfer costs by creating one replica from the source in the other Region and creating the other replicas there from that first replica.
  scope: RDS for MySQL and RDS for MariaDB.
  link: [reduce your data transfer costs](../facts/rds.md#rds-cross-region-replica-chain-cuts-transfer)
  link: [reducing the number of cross-Region read replicas](../facts/rds.md#rds-cross-region-replica-chain-cuts-transfer)
rds-cross-region-replica-data-transfer-charged
  claim: Data transferred for cross-Region replication incurs RDS data transfer charges: the initial snapshot transfer and every data modification sent from the source Region to the replica Region.
  scope: cross-Region read replicas.
  link: [incurs Amazon RDS data transfer charges](../facts/rds.md#rds-cross-region-replica-data-transfer-charged)
  link: [data transferred out of the source AWS Region](../facts/rds.md#rds-cross-region-replica-data-transfer-charged)
rds-cross-region-replica-default-security-group
  claim: A cross-Region read replica uses the default security group, and in most cases the default DB parameter group and option group of its engine.
  scope: cross-Region read replicas; default; adjustable; Db2 needs a custom parameter group; MySQL and Oracle accept one through the CLI.
  link: [The read replica uses the default security group.](../facts/rds.md#rds-cross-region-replica-default-security-group)
  link: [default DB parameter group and DB option group](../facts/rds.md#rds-cross-region-replica-default-security-group)
rds-cross-region-replica-encrypted-source-dest-key
  claim: To create an encrypted cross-Region read replica, the source DB instance must be encrypted and you choose a KMS key in the destination Region.
  scope: cross-Region read replicas.
  link: [the source DB instance must be encrypted](../facts/rds.md#rds-cross-region-replica-encrypted-source-dest-key)
  link: [KMS key in the destination AWS Region](../facts/rds.md#rds-cross-region-replica-encrypted-source-dest-key)
rds-cross-region-replica-govcloud
  claim: You can replicate between the GovCloud (US-East) and GovCloud (US-West) Regions, but not into or out of GovCloud (US).
  scope: cross-Region read replicas.
  link: [not into or out of GovCloud (US)](../facts/rds.md#rds-cross-region-replica-govcloud)
rds-cross-region-replica-higher-lag
  claim: A read replica in a different Region than its source can be expected to have more replication lag, because of the longer network channels between Regional data centers.
  scope: cross-Region read replicas.
  link: [higher level of lag time](../facts/rds.md#rds-cross-region-replica-higher-lag)
  link: [longer network channels between regional data centers](../facts/rds.md#rds-cross-region-replica-higher-lag)
rds-cross-region-replica-source-deleted
  claim: When the source of a cross-Region read replica is deleted, the replica is promoted for Db2, MariaDB, SQL Server, MySQL and Oracle; for PostgreSQL its replication status becomes terminated and it is not promoted.
  scope: cross-Region read replicas, per engine.
  link: [the read replica is promoted](../facts/rds.md#rds-cross-region-replica-source-deleted)
  link: [The read replica isn't promoted.](../facts/rds.md#rds-cross-region-replica-source-deleted)
rds-cross-region-replica-use-cases
  claim: A read replica in a different AWS Region is used to improve disaster recovery, to scale reads into a Region closer to users, and to make migration between Regions easier.
  scope: cross-Region read replicas.
  link: [Improve your disaster recovery capabilities.](../facts/rds.md#rds-cross-region-replica-use-cases)
  link: [closer to your users](../facts/rds.md#rds-cross-region-replica-use-cases)
  link: [easier to migrate](../facts/rds.md#rds-cross-region-replica-use-cases)
rds-custom-oracle-end-of-support-access
  claim: AWS ends support for Amazon RDS Custom for Oracle on March 31, 2027; after that date you can no longer access the RDS Custom for Oracle console or its resources.
  scope: Amazon RDS Custom.
  link: [March 31, 2027](../facts/rds.md#rds-custom-oracle-end-of-support-access)
  link: [no longer be able to access](../facts/rds.md#rds-custom-oracle-end-of-support-access)
  say: March thirty-first, twenty twenty-seven
rds-custom-os-access
  claim: Amazon RDS Custom automates database administration but lets you access and customize the database environment and operating system, for legacy, custom and packaged applications; standard Amazon RDS does not let you access the underlying host.
  scope: RDS Custom (Oracle and SQL Server).
  link: [customize your database environment and operating system](../facts/rds.md#rds-custom-os-access)
  link: [doesn't let you access the underlying host](../facts/rds.md#rds-custom-os-access)
rds-custom-vs-rds-vs-ec2
  claim: AWS recommends Amazon RDS when the database and OS should be fully managed by AWS, RDS Custom when you need administrative rights to the database and underlying OS, and self-managed databases on Amazon EC2 when you want full management responsibility.
  scope: Amazon RDS Custom.
  link: [Amazon RDS Custom is the better choice](../facts/rds.md#rds-custom-vs-rds-vs-ec2)
  link: [self-managing your commercial databases on Amazon EC2](../facts/rds.md#rds-custom-vs-rds-vs-ec2)
rds-customer-owns-query-tuning
  claim: Under the RDS shared responsibility model, AWS hosts the software components and infrastructure of DB instances; you are responsible for query tuning.
  scope: RDS shared responsibility.
  link: [You are responsible for query tuning](../facts/rds.md#rds-customer-owns-query-tuning)
  link: [hosting the software components and infrastructure](../facts/rds.md#rds-customer-owns-query-tuning)
rds-database-insights-advanced-fleet-views
  claim: Only the Advanced mode of Database Insights lets you define and save fleet-wide monitoring views; Standard mode does not support them.
  scope: CloudWatch Database Insights and Performance Insights.
  link: [Not supported](../facts/rds.md#rds-database-insights-advanced-fleet-views)
  link: [Supported](../facts/rds.md#rds-database-insights-advanced-fleet-views)
rds-database-insights-advanced-retention-465-days
  claim: When you turn on the Advanced mode of Database Insights while creating a DB instance or Multi-AZ DB cluster, the retention period must be 15 months in the console, and at least 465 days with the create-db-instance or create-db-cluster AWS CLI command.
  scope: per DB instance or Multi-AZ DB cluster, when created with Advanced mode; minimum; when the DB instance or Multi-AZ DB cluster is created with the Advanced mode of Database Insights.
  link: [at least 465 days](../facts/rds.md#rds-database-insights-advanced-retention-465-days)
  say: at least four hundred sixty-five days
rds-database-insights-inherits-performance-insights
  claim: CloudWatch Database Insights inherits all the capabilities of Performance Insights and adds fleet-level monitoring, application performance monitoring integration, and correlation of database metrics with logs and events.
  scope: CloudWatch Database Insights and Performance Insights.
  link: [inherits all the capabilities of Performance Insights](../facts/rds.md#rds-database-insights-inherits-performance-insights)
  link: [fleet-level monitoring](../facts/rds.md#rds-database-insights-inherits-performance-insights)
rds-database-insights-retention-by-mode
  claim: Database Insights Standard mode includes up to 7 days of detailed database and per-query metrics retention at no additional cost; for retention beyond 7 days you can configure 1 to 24 months, at the same price as Performance Insights; Advanced mode supports 1–24 months of retention at no additional cost.
  scope: per database, detailed database and per-query metrics; default.
  link: [up to 7 days](../facts/rds.md#rds-database-insights-retention-by-mode)
  link: [1–24 months, at no additional cost](../facts/rds.md#rds-database-insights-retention-by-mode)
  say: up to seven days | one to twenty-four months at no additional cost
rds-database-insights-standard-default
  claim: By default, RDS turns on the Standard mode of CloudWatch Database Insights for Amazon RDS databases.
  scope: per RDS database; default; not adjustable.
  link: [Standard mode of Database Insights](../facts/rds.md#rds-database-insights-standard-default)
rds-db-instance-identifier-rules
  claim: A DB instance identifier must contain 1–63 alphanumeric characters or hyphens, start with a letter, and be unique for all DB instances per AWS account, per AWS Region.
  scope: per DB instance identifier; maximum; can't end with a hyphen or contain two consecutive hyphens.
  link: [1–63 alphanumeric characters or hyphens](../facts/rds.md#rds-db-instance-identifier-rules)
  say: one to sixty-three letters, digits or hyphens
rds-decision-guide-aurora-row
  claim: The decision guide recommends Amazon Aurora when you migrate or modernize an on-premises relational workload or when the workload has less predictable query patterns; it supports MySQL- and PostgreSQL-compatible engines.
  scope: AWS database decision guide (Choosing an AWS database service).
  link: [less predictable query patterns](../facts/rds.md#rds-decision-guide-aurora-row)
rds-decision-guide-cache-microseconds
  claim: For extremely high read performance with microsecond response times, the decision guide suggests in-memory caching such as Amazon ElastiCache alongside the database, or a durable in-memory database such as Amazon MemoryDB.
  scope: AWS database decision guide (Choosing an AWS database service).
  link: [measured in microseconds](../facts/rds.md#rds-decision-guide-cache-microseconds)
rds-decision-guide-dynamodb-row
  claim: The decision guide places Amazon DynamoDB as a key-value database for workloads such as session stores or shopping carts, optimized as a serverless NoSQL database with single-digit millisecond performance at any scale.
  scope: AWS database decision guide (Choosing an AWS database service).
  link: [session stores or shopping carts](../facts/rds.md#rds-decision-guide-dynamodb-row)
  link: [single-digit millisecond performance at any scale](../facts/rds.md#rds-decision-guide-dynamodb-row)
rds-decision-guide-rds-row
  claim: The AWS database decision guide says to use Amazon RDS when you need a fully managed relational database with a choice of six engines (PostgreSQL, MySQL, MariaDB, SQL Server, Oracle and Db2); it is optimized for structured data with full SQL support, automated backups, software patching and Multi-AZ deployments.
  scope: AWS database decision guide (Choosing an AWS database service).
  link: [fully managed relational database](../facts/rds.md#rds-decision-guide-rds-row)
  link: [six popular engines](../facts/rds.md#rds-decision-guide-rds-row)
  say: six popular engines
rds-decision-guide-rehost-ec2-tasks
  claim: If you rehost a database on Amazon EC2, you still own the operational tasks such as upgrades, patches, backups, capacity planning, performance and availability targets.
  scope: AWS database decision guide (Choosing an AWS database service).
  link: [upgrades, patches, backups, capacity planning](../facts/rds.md#rds-decision-guide-rehost-ec2-tasks)
rds-decision-guide-relational-joins
  claim: Relational databases store structured data in tables, rows and columns and support complex queries through joins.
  scope: AWS database decision guide (Choosing an AWS database service).
  link: [complex queries through joins](../facts/rds.md#rds-decision-guide-relational-joins)
rds-decision-guide-replatform
  claim: In a re-platform strategy you migrate an on-premises relational database to a fully managed Amazon RDS instance; re-platforming makes no changes to the application but uses a fully managed service in the cloud.
  scope: AWS database decision guide (Choosing an AWS database service).
  link: [fully managed Amazon RDS instance](../facts/rds.md#rds-decision-guide-replatform)
rds-default-choice-relational
  claim: AWS recommends Amazon RDS as the default choice for most relational database deployments, because on-premises and Amazon EC2 alternatives make you spend more time managing software and hardware.
  scope: relational database deployments on AWS.
  link: [default choice for most relational database deployments](../facts/rds.md#rds-default-choice-relational)
rds-default-vpc
  claim: All new DB instances are created in the account's default VPC unless you specify otherwise.
  scope: new DB instances; default; adjustable.
  link: [created in the default VPC](../facts/rds.md#rds-default-vpc)
rds-delayed-replica-pause-promote
  claim: With a delayed RDS for PostgreSQL read replica you can pause replication before a bad change is applied, resume up to a specific log position, and promote the replica; AWS says this recovers faster than a point-in-time restore, which can take hours for large databases (announced August 22, 2025).
  scope: delayed read replicas.
  link: [August 22, 2025](../facts/rds.md#rds-delayed-replica-pause-promote)
  link: [can take hours for large databases](../facts/rds.md#rds-delayed-replica-pause-promote)
  say: August twenty-second, twenty twenty-five
rds-delete-final-snapshot-option
  claim: When you delete a DB instance you can take a final snapshot and use it to restore the deleted instance later; without a final snapshot, to restore the deleted instance you either retain automated backups or use an earlier manual snapshot.
  scope: deleting a DB instance and its backups.
  link: [If you take a final snapshot](../facts/rds.md#rds-delete-final-snapshot-option)
  link: [no final snapshot exists](../facts/rds.md#rds-delete-final-snapshot-option)
rds-delete-instance-automated-backups-deleted
  claim: When you delete a DB instance without choosing Retain automated backups, all its automated backups are deleted with it; final and manual DB snapshots are independent and are not deleted.
  scope: deleting a DB instance and its backups; Retain automated backups not chosen.
  link: [all automated backups are deleted](../facts/rds.md#rds-delete-instance-automated-backups-deleted)
  link: [Manual snapshots are not deleted](../facts/rds.md#rds-delete-instance-automated-backups-deleted)
rds-delete-replicated-backups-kept
  claim: If you do not retain automated backups when deleting a DB instance, RDS deletes the automated backups in the same Region, but keeps automated backups that were replicated to another Region.
  scope: cross-Region automated backups.
  link: [replicated to another AWS Region, RDS keeps them](../facts/rds.md#rds-delete-replicated-backups-kept)
rds-deletion-protection-console-default
  claim: Deletion protection is turned on by default for a DB instance created with the console and must be turned off before the instance can be deleted; turning it off does not cause an outage.
  scope: DB instances created with the console; default; adjustable.
  link: [deletion protection is turned on](../facts/rds.md#rds-deletion-protection-console-default)
  link: [This operation doesn't cause an outage.](../facts/rds.md#rds-deletion-protection-console-default)
rds-ec2-database-user-error-risk
  claim: Running a database on Amazon EC2 makes you more prone to user errors: updating the operating system or database software by hand can cause application downtime.
  scope: self-managed database on Amazon EC2.
  link: [more prone to user errors](../facts/rds.md#rds-ec2-database-user-error-risk)
rds-ena-express-benefits
  claim: With Cross-AZ ENA Express, Multi-AZ deployments get lower replication latency and less variability, and better failover reliability for write-intensive workloads.
  scope: Cross-AZ ENA Express for Multi-AZ DB instances.
  link: [improves failover reliability](../facts/rds.md#rds-ena-express-benefits)
rds-ena-express-default-new-instances
  claim: Cross-AZ ENA Express is enabled by default on all newly created Multi-AZ DB instances that use eligible instance classes; to enable it on an existing Multi-AZ DB instance, stop and start the instance, modify it to use an eligible instance class, or use Scale Compute on an eligible instance class.
  scope: newly created Multi-AZ DB instances with eligible instance classes; default; not adjustable.
  link: [enabled by default](../facts/rds.md#rds-ena-express-default-new-instances)
rds-ena-express-multi-az-replication
  claim: Amazon RDS supports Cross-Availability Zone ENA Express for eligible DB instance classes in Multi-AZ deployments; it increases single-flow network bandwidth for faster block-level replication between the primary and standby DB instances.
  scope: Cross-AZ ENA Express for Multi-AZ DB instances.
  link: [faster block-level data replication](../facts/rds.md#rds-ena-express-multi-az-replication)
rds-ena-express-not-sql-server
  claim: Cross-AZ ENA Express is not supported for Amazon RDS for SQL Server.
  scope: Cross-AZ ENA Express for Multi-AZ DB instances.
  link: [not supported for Amazon RDS for SQL Server](../facts/rds.md#rds-ena-express-not-sql-server)
rds-encrypt-existing-via-snapshot-copy
  claim: To add encryption to an unencrypted DB instance, take a snapshot, copy it while specifying a KMS key so the copy is encrypted, and restore an encrypted DB instance from the encrypted copy.
  scope: RDS encryption at rest.
  link: [encrypt a copy of an unencrypted snapshot](../facts/rds.md#rds-encrypt-existing-via-snapshot-copy)
  link: [restore an encrypted DB instance](../facts/rds.md#rds-encrypt-existing-via-snapshot-copy)
rds-encryption-aes256-transparent
  claim: Encrypted RDS DB instances use AES-256; RDS handles access authentication and decryption transparently with minimal performance impact, so client applications need no changes.
  scope: encrypted DB instances.
  link: [AES-256 encryption algorithm](../facts/rds.md#rds-encryption-aes256-transparent)
  link: [don't need to modify your database client applications](../facts/rds.md#rds-encryption-aes256-transparent)
rds-encryption-all-engines-storage
  claim: Amazon RDS encryption is available for all database engines and storage types, and for most DB instance classes.
  scope: RDS encryption at rest; a few old instance classes (db.m1, db.m2, db.t2.micro) do not support it.
  link: [available for all database engines and storage types](../facts/rds.md#rds-encryption-all-engines-storage)
  link: [most DB instance classes](../facts/rds.md#rds-encryption-all-engines-storage)
rds-encryption-at-rest-scope
  claim: RDS encryption at rest covers the DB instance's underlying storage, its logs, automated backups, read replicas and snapshots.
  scope: encrypted DB instances.
  link: [logs, automated backups, read replicas, and snapshots](../facts/rds.md#rds-encryption-at-rest-scope)
  link: [the underlying storage for DB instances](../facts/rds.md#rds-encryption-at-rest-scope)
rds-encryption-blue-green-change-key
  claim: A blue/green deployment can create a green environment encrypted with a different KMS key, which can encrypt an unencrypted DB instance or change the key of an encrypted one.
  scope: RDS encryption at rest.
  link: [use a blue/green deployment](../facts/rds.md#rds-encryption-blue-green-change-key)
  link: [encrypt an unencrypted DB instance](../facts/rds.md#rds-encryption-blue-green-change-key)
rds-encryption-cannot-turn-off
  claim: You cannot turn off encryption on an encrypted DB instance; to get unencrypted data you export it and import it into an unencrypted DB instance.
  scope: encrypted DB instances.
  link: [You can't turn off encryption](../facts/rds.md#rds-encryption-cannot-turn-off)
  link: [export data from an encrypted DB instance](../facts/rds.md#rds-encryption-cannot-turn-off)
rds-encryption-default-aws-managed-key
  claim: When you create an encrypted DB instance without specifying a customer managed key, RDS uses the AWS managed key for Amazon RDS; each Region of an account has a different AWS managed key for RDS.
  scope: encrypted DB instances; default; adjustable; no customer managed key specified.
  link: [Amazon RDS uses the AWS managed key](../facts/rds.md#rds-encryption-default-aws-managed-key)
  link: [for each AWS Region](../facts/rds.md#rds-encryption-default-aws-managed-key)
rds-encryption-disabled-key-inaccessible
  claim: If you disable the KMS key of an encrypted DB instance, RDS loses access to the key; where backups are enabled and the instance can stop, it goes into a recoverable state 2 hours after detection and stays stopped for seven days, and you recover it by enabling the KMS key and restarting the instance; if it isn't recovered within seven days, it goes into a terminal state and you can only restore it from a DB snapshot or backup.
  scope: encrypted DB instances that can stop; backups enabled.
  link: [seven days](../facts/rds.md#rds-encryption-disabled-key-inaccessible)
  link: [loses access to the KMS key](../facts/rds.md#rds-encryption-disabled-key-inaccessible)
rds-encryption-kms-key-fixed
  claim: Once an encrypted DB instance is created, you can't change the KMS key it uses; to change the key, create a manual snapshot of the instance and enable encryption with the new key while copying the snapshot.
  scope: encrypted DB instances.
  link: [you can't change the KMS key](../facts/rds.md#rds-encryption-kms-key-fixed)
  link: [enable encryption while copying the snapshot](../facts/rds.md#rds-encryption-kms-key-fixed)
rds-encryption-kms-regional-replica
  claim: KMS keys are specific to the Region where they are created, so a read replica in a different Region needs a KMS key in the destination Region.
  scope: encrypted cross-Region read replicas.
  link: [specify a KMS key in the destination Region](../facts/rds.md#rds-encryption-kms-regional-replica)
  link: [KMS keys are specific to the AWS Region](../facts/rds.md#rds-encryption-kms-regional-replica)
rds-encryption-no-encrypted-snapshot-of-unencrypted
  claim: You cannot create an encrypted snapshot directly from an unencrypted DB instance, and a snapshot of an encrypted DB instance must use the same KMS key as the instance.
  scope: RDS encryption at rest.
  link: [can't create an encrypted snapshot](../facts/rds.md#rds-encryption-no-encrypted-snapshot-of-unencrypted)
  link: [using the same KMS key](../facts/rds.md#rds-encryption-no-encrypted-snapshot-of-unencrypted)
rds-encryption-no-restore-unencrypted-to-encrypted
  claim: You can't restore an unencrypted backup or snapshot to an encrypted DB instance.
  scope: RDS encryption at rest.
  link: [You can't restore an unencrypted backup or snapshot](../facts/rds.md#rds-encryption-no-restore-unencrypted-to-encrypted)
rds-encryption-only-at-create
  claim: You can encrypt an RDS DB instance only when you create it, not afterwards; you can effectively add encryption by restoring from an encrypted copy of a snapshot.
  scope: RDS encryption at rest.
  link: [only encrypt an Amazon RDS DB instance](../facts/rds.md#rds-encryption-only-at-create)
  link: [not after the DB instance is created](../facts/rds.md#rds-encryption-only-at-create)
  link: [encrypt a copy of an unencrypted snapshot](../facts/rds.md#rds-encryption-only-at-create)
rds-encryption-replica-matches-source
  claim: A read replica must match its source's encryption: no encrypted replica of an unencrypted instance and no unencrypted replica of an encrypted instance; in the same Region an encrypted replica uses the same KMS key as the source.
  scope: read replicas; same-key rule applies when source and replica are in the same AWS Region.
  link: [unencrypted read replica of an encrypted DB instance](../facts/rds.md#rds-encryption-replica-matches-source)
  link: [same KMS key as the source DB instance](../facts/rds.md#rds-encryption-replica-matches-source)
rds-encryption-replica-traffic-encrypted
  claim: For both encrypted and unencrypted DB instances, data in transit between the source and its read replicas is encrypted, even across AWS Regions.
  scope: read replica replication traffic.
  link: [even when replicating across AWS Regions](../facts/rds.md#rds-encryption-replica-traffic-encrypted)
rds-encryption-tde-oracle-sqlserver
  claim: RDS also supports Transparent Data Encryption (TDE) for Oracle and SQL Server; TDE can be combined with RDS encryption at rest (with a possible slight performance cost), and each method has its own keys.
  scope: RDS for Oracle and RDS for SQL Server.
  link: [Transparent Data Encryption (TDE)](../facts/rds.md#rds-encryption-tde-oracle-sqlserver)
  link: [manage different keys for each encryption method](../facts/rds.md#rds-encryption-tde-oracle-sqlserver)
rds-engine-upgrade-downtime-blue-green
  claim: Database engine upgrades require downtime, which a blue/green deployment can minimize.
  scope: RDS maintenance and engine upgrades.
  link: [Database engine upgrades require downtime.](../facts/rds.md#rds-engine-upgrade-downtime-blue-green)
  link: [using a blue/green deployment](../facts/rds.md#rds-engine-upgrade-downtime-blue-green)
rds-engines-supported
  claim: Amazon RDS (not counting Aurora) offers these database engines: IBM Db2, MariaDB, Microsoft SQL Server, MySQL, Oracle Database, and PostgreSQL.
  scope: Amazon RDS user guide (engines other than Aurora).
  link: [IBM Db2, MariaDB, Microsoft SQL Server](../facts/rds.md#rds-engines-supported)
  link: [MySQL, Oracle Database, and PostgreSQL](../facts/rds.md#rds-engines-supported)
  link: [engines that you are already familiar with](../facts/rds.md#rds-engines-supported)
rds-enhanced-monitoring-agent-processes
  claim: Enhanced Monitoring shows OS metrics in real time from an agent on the DB instance, useful to see how processes or threads use the CPU, while CloudWatch gathers CPU metrics from the hypervisor; Enhanced Monitoring metrics go to CloudWatch Logs.
  scope: RDS Enhanced Monitoring.
  link: [how different processes or threads use the CPU](../facts/rds.md#rds-enhanced-monitoring-agent-processes)
  link: [from an agent on the DB instance](../facts/rds.md#rds-enhanced-monitoring-agent-processes)
  link: [from the hypervisor](../facts/rds.md#rds-enhanced-monitoring-agent-processes)
rds-enhanced-monitoring-os-metrics
  claim: Performance Insights assesses the load on the database; Enhanced Monitoring looks at operating system metrics in real time.
  scope: RDS Enhanced Monitoring.
  link: [metrics in real time for the operating system](../facts/rds.md#rds-enhanced-monitoring-os-metrics)
  link: [assesses the load on your database](../facts/rds.md#rds-enhanced-monitoring-os-metrics)
rds-event-subscription-sns
  claim: RDS groups events into categories that you can subscribe to so that you are notified when an event in that category occurs, and it uses the ARN of an Amazon SNS topic to identify each subscription.
  scope: RDS event notifications.
  link: [groups events into categories](../facts/rds.md#rds-event-subscription-sns)
  link: [ARN of an Amazon SNS topic](../facts/rds.md#rds-event-subscription-sns)
rds-events-eventbridge-rules
  claim: With Amazon EventBridge you can write rules that match RDS events and send them to targets such as an AWS Lambda function or an Amazon SNS topic for automated actions.
  scope: RDS events in Amazon EventBridge.
  link: [an AWS Lambda function](../facts/rds.md#rds-events-eventbridge-rules)
  link: [which automated actions to take](../facts/rds.md#rds-events-eventbridge-rules)
rds-export-snapshot-all-types-same-region-bucket
  claim: All types of DB snapshots can be exported (manual, automated system, and AWS Backup snapshots), and the S3 bucket must be in the same Region as the snapshot.
  scope: snapshot export to Amazon S3.
  link: [You can export all types of DB snapshots](../facts/rds.md#rds-export-snapshot-all-types-same-region-bucket)
  link: [same AWS Region as the snapshot](../facts/rds.md#rds-export-snapshot-all-types-same-region-bucket)
rds-export-snapshot-athena-redshift-spectrum
  claim: Exported snapshot data can be analyzed directly with Amazon Athena or Amazon Redshift Spectrum.
  scope: snapshot export to Amazon S3.
  link: [Amazon Athena or Amazon Redshift Spectrum](../facts/rds.md#rds-export-snapshot-athena-redshift-spectrum)
rds-export-snapshot-not-restorable
  claim: Exported snapshot data in S3 cannot be restored to a new DB instance or imported into an existing DB instance.
  scope: snapshot export to Amazon S3.
  link: [You can't restore exported snapshot data from S3](../facts/rds.md#rds-export-snapshot-not-restorable)
rds-export-snapshot-s3-parquet
  claim: You can export DB snapshot data to an Amazon S3 bucket in compressed Apache Parquet format; the export runs in the background without affecting the active database's performance.
  scope: snapshot export to Amazon S3.
  link: [Apache Parquet format](../facts/rds.md#rds-export-snapshot-s3-parquet)
  link: [doesn't affect the performance of your active database](../facts/rds.md#rds-export-snapshot-s3-parquet)
rds-extended-support-auto-enroll
  claim: Unless you disabled RDS Extended Support when you created or restored the DB instance or DB cluster, Amazon RDS enrolls it automatically in Extended Support after the RDS end of standard support date.
  scope: per DB instance or DB cluster; default; not adjustable.
  link: [automatically enroll them in RDS Extended Support](../facts/rds.md#rds-extended-support-auto-enroll)
rds-extended-support-charge-stops
  claim: The additional charge for RDS Extended Support automatically stops when you upgrade to an engine version that's covered under standard support or delete the database that's running a major version past the RDS end of standard support date.
  scope: RDS Extended Support.
  link: [automatically stops](../facts/rds.md#rds-extended-support-charge-stops)
rds-extended-support-charges-standby
  claim: RDS Extended Support charges also apply to standby instances in Multi-AZ deployments.
  scope: RDS Extended Support.
  link: [apply to standby instances in Multi-AZ deployments](../facts/rds.md#rds-extended-support-charges-standby)
rds-extended-support-charges-start-day-after
  claim: Extended Support charges start the day after the RDS end of standard support date for every engine enrolled in Extended Support.
  scope: RDS Extended Support.
  link: [beginning the day after](../facts/rds.md#rds-extended-support-charges-start-day-after)
rds-extended-support-more-time
  claim: RDS Extended Support is a paid offering that gives you more time to upgrade to a supported major engine version.
  scope: RDS Extended Support.
  link: [This paid offering gives you more time](../facts/rds.md#rds-extended-support-more-time)
rds-extended-support-mysql57-charges-march-2024
  claim: Example from the guide: the RDS end of standard support for RDS for MySQL 5.7 was February 29, 2024; databases still on 5.7 were enrolled automatically in Extended Support that day, and charges started on March 1, 2024.
  scope: RDS Extended Support.
  link: [February 29, 2024](../facts/rds.md#rds-extended-support-mysql57-charges-march-2024)
  link: [March 1, 2024](../facts/rds.md#rds-extended-support-mysql57-charges-march-2024)
  say: February twenty-ninth, twenty twenty-four | March first, twenty twenty-four
rds-extended-support-opt-out
  claim: You can avoid Extended Support charges by changing the EngineLifecycleSupport parameter with the AWS CLI or RDS API; if the DB instance or cluster is already past its standard support end date, it then upgrades automatically to the next supported major version.
  scope: RDS Extended Support.
  link: [modifying the `EngineLifecycleSupport` parameter](../facts/rds.md#rds-extended-support-opt-out)
  link: [automatically upgrades to the next supported major version](../facts/rds.md#rds-extended-support-opt-out)
rds-extended-support-priced-per-vcpu-hour
  claim: For provisioned instances on Aurora, RDS for MySQL and RDS for PostgreSQL, RDS Extended Support is priced per vCPU per hour, and the price also depends on the calendar date.
  scope: RDS Extended Support.
  link: [priced per vCPU per hour](../facts/rds.md#rds-extended-support-priced-per-vcpu-hour)
rds-extended-support-up-to-3-years
  claim: RDS Extended Support is available for up to 3 years past the RDS end of standard support date of a major engine version; after that, if you have not upgraded, Amazon RDS upgrades the major engine version automatically. RDS for MySQL 5.7 is an exception: its end of standard support date was February 29, 2024, and major version 5.7 reaches its end of Extended Support on June 30, 2029.
  scope: per major engine version, after the RDS end of standard support date; maximum; not adjustable; RDS for MySQL 5.7 runs longer: end of Extended Support June 30, 2029.
  link: [up to 3 years](../facts/rds.md#rds-extended-support-up-to-3-years)
  link: [automatically upgrade your major engine version](../facts/rds.md#rds-extended-support-up-to-3-years)
  say: up to three years
rds-extended-support-what
  claim: RDS Extended Support lets you keep running a database on a major engine version after the RDS end of standard support date, for an additional cost.
  scope: RDS Extended Support.
  link: [for an additional cost](../facts/rds.md#rds-extended-support-what)
rds-external-source-binlog-replication
  claim: You can set up replication between an RDS for MySQL or MariaDB DB instance and a MySQL or MariaDB instance outside Amazon RDS by using binary log file replication.
  scope: RDS for MySQL and RDS for MariaDB DB instances.
  link: [external to Amazon RDS](../facts/rds.md#rds-external-source-binlog-replication)
  link: [binary log file replication](../facts/rds.md#rds-external-source-binlog-replication)
rds-failover-without-proxy-outage
  claim: Without RDS Proxy, a failover involves a brief outage during which writes are not possible and existing connections are disrupted, so the application must reopen them.
  scope: RDS DB instances in a Multi-AZ configuration; no RDS Proxy.
  link: [a failover involves a brief outage](../facts/rds.md#rds-failover-without-proxy-outage)
  link: [your application must reopen them](../facts/rds.md#rds-failover-without-proxy-outage)
rds-faq-apply-immediately-pending-changes
  claim: Instance class and storage changes are applied in the maintenance window unless you use the apply-immediately flag, which also applies any other pending system changes.
  scope: DB instance modifications.
  link: [any other pending system changes](../facts/rds.md#rds-faq-apply-immediately-pending-changes)
rds-faq-auto-minor-version-upgrade
  claim: When a new minor engine version has significant bug fixes, RDS schedules automatic upgrades for DB instances whose Auto Minor Version Upgrade setting is Yes.
  scope: RDS maintenance and engine upgrades.
  link: [Auto Minor Version Upgrade](../facts/rds.md#rds-faq-auto-minor-version-upgrade)
rds-faq-automated-backups-enable-pitr
  claim: Automated backups enable point-in-time recovery: RDS takes a full daily snapshot in the backup window and captures transaction logs as updates are made.
  scope: RDS automated backups and snapshots.
  link: [point-in-time recovery](../facts/rds.md#rds-faq-automated-backups-enable-pitr)
  link: [full daily snapshot](../facts/rds.md#rds-faq-automated-backups-enable-pitr)
rds-faq-automated-backups-on-by-default
  claim: By default, RDS turns on automated backups for a DB instance with a 7-day retention period; you do not need to enable them.
  scope: per DB instance; default; adjustable.
  link: [7-day retention period](../facts/rds.md#rds-faq-automated-backups-on-by-default)
rds-faq-aws-config-records-rds
  claim: AWS Config can continuously record configuration changes to RDS DB instances, DB subnet groups, DB snapshots, DB security groups and event subscriptions, and AWS Config rules can check them.
  scope: configuration monitoring of RDS resources.
  link: [AWS Config](../facts/rds.md#rds-faq-aws-config-records-rds)
rds-faq-backup-incremental
  claim: Backup size is directly proportional to the amount of data on the DB instance; after the first backup, backups are incremental and store only changed data.
  scope: RDS automated backups and snapshots.
  link: [Subsequent backups are incremental](../facts/rds.md#rds-faq-backup-incremental)
rds-faq-backup-patching-managed
  claim: Amazon RDS can automatically back up your database and keep the database software up to date.
  scope: Amazon RDS managed operations.
  link: [automatically back up your database](../facts/rds.md#rds-faq-backup-patching-managed)
rds-faq-backup-window-io-suspension
  claim: During the backup window, storage I/O may be briefly suspended (typically under a few seconds), but there is no I/O suspension for Multi-AZ deployments because the backup is taken from the standby.
  scope: RDS automated backups and snapshots.
  link: [no I/O suspension for Multi-AZ DB deployments](../facts/rds.md#rds-faq-backup-window-io-suspension)
  link: [storage I/O may be briefly suspended](../facts/rds.md#rds-faq-backup-window-io-suspension)
rds-faq-backups-stored-in-s3
  claim: RDS DB snapshots and automated backups are stored in Amazon S3.
  scope: RDS automated backups and snapshots.
  link: [stored in S3](../facts/rds.md#rds-faq-backups-stored-in-s3)
rds-faq-billing-instance-hours-stop-or-delete
  claim: DB instance hours are billed for each hour the DB instance runs in an available state; to stop paying instance hours you must stop or delete it.
  scope: Amazon RDS billing.
  link: [stop or delete it](../facts/rds.md#rds-faq-billing-instance-hours-stop-or-delete)
rds-faq-billing-per-second-10-minute-minimum
  claim: Partial DB instance hours are billed in one-second increments, with a 10 minute minimum charge after a billable status change such as creating, starting or modifying the DB instance class.
  scope: Amazon RDS billing.
  link: [one-second increments](../facts/rds.md#rds-faq-billing-per-second-10-minute-minimum)
  link: [10 minute minimum charge](../facts/rds.md#rds-faq-billing-per-second-10-minute-minimum)
rds-faq-billing-piops-regardless-of-use
  claim: With Provisioned IOPS (SSD) storage you pay per month for the provisioned IOPS rate, regardless of the IOPS you consume.
  scope: Amazon RDS billing.
  link: [regardless of IOPS consumed](../facts/rds.md#rds-faq-billing-piops-regardless-of-use)
rds-faq-billing-stopped-instance
  claim: A stopped DB instance is still charged for provisioned storage (including Provisioned IOPS) and backup storage, but not for DB instance hours.
  scope: Amazon RDS billing.
  link: [but not for DB instance hours](../facts/rds.md#rds-faq-billing-stopped-instance)
  link: [provisioned storage (including Provisioned IOPS)](../facts/rds.md#rds-faq-billing-stopped-instance)
rds-faq-blue-green-engines
  claim: The FAQ lists Blue/Green Deployments for Aurora MySQL, Aurora PostgreSQL, RDS for MySQL, RDS for MariaDB and RDS for PostgreSQL.
  scope: RDS Blue/Green Deployments.
  link: [Amazon RDS for PostgreSQL](../facts/rds.md#rds-faq-blue-green-engines)
rds-faq-blue-green-environments
  claim: In Blue/Green Deployments the blue environment is the current production environment and the green environment is the staging environment that becomes production after switchover.
  scope: RDS Blue/Green Deployments.
  link: [blue environment is your current production environment](../facts/rds.md#rds-faq-blue-green-environments)
rds-faq-blue-green-max-downtime-30-seconds
  claim: You can set the maximum tolerable switchover downtime as low as 30 seconds; a switchover times out if an ongoing transaction exceeds it.
  scope: per Blue/Green switchover, maximum tolerable downtime setting; minimum; adjustable.
  link: [30 seconds](../facts/rds.md#rds-faq-blue-green-max-downtime-30-seconds)
rds-faq-blue-green-old-environment-kept
  claim: After switchover, Blue/Green Deployments do not delete the old production environment, and it keeps incurring standard charges until you delete it.
  scope: RDS Blue/Green Deployments.
  link: [do not delete your old production environment](../facts/rds.md#rds-faq-blue-green-old-environment-kept)
rds-faq-blue-green-switchover-blocks-writes
  claim: A Blue/Green switchover blocks writes to both the blue and green environments until the switchover is complete; green catches up with production, then green is promoted by redirecting traffic to it, and Blue/Green Deployments are designed to enable writes on green after the switchover, ensuring zero data loss.
  scope: RDS Blue/Green Deployments.
  link: [block writes](../facts/rds.md#rds-faq-blue-green-switchover-blocks-writes)
  link: [zero data loss](../facts/rds.md#rds-faq-blue-green-switchover-blocks-writes)
rds-faq-blue-green-use-cases
  claim: Blue/Green Deployments suit major or minor engine version upgrades, operating system updates, schema changes that do not break logical replication, and parameter changes, with short, predictable downtime.
  scope: RDS Blue/Green Deployments.
  link: [major or minor version database engine upgrades](../facts/rds.md#rds-faq-blue-green-use-cases)
  link: [short, predictable downtime](../facts/rds.md#rds-faq-blue-green-use-cases)
rds-faq-cloudtrail-api-history
  claim: AWS CloudTrail records the Amazon RDS API calls in your account, which supports security analysis, resource change tracking and compliance auditing.
  scope: RDS API call history.
  link: [AWS CloudTrail](../facts/rds.md#rds-faq-cloudtrail-api-history)
rds-faq-compute-scale-brief-outage
  claim: Changing the DB instance class makes the database temporarily unavailable, typically for a few minutes, during the maintenance window unless the change is applied immediately.
  scope: DB instance class changes.
  link: [temporarily unavailable](../facts/rds.md#rds-faq-compute-scale-brief-outage)
  link: [only a few minutes](../facts/rds.md#rds-faq-compute-scale-brief-outage)
rds-faq-database-savings-plans-35-percent
  claim: Amazon RDS usage can be covered by Database Savings Plans, which reduce costs by up to 35% for a commitment to a consistent amount of usage over a 1-year term.
  scope: Amazon RDS usage covered by a Database Savings Plan, 1-year term; maximum.
  link: [up to 35%](../facts/rds.md#rds-faq-database-savings-plans-35-percent)
  link: [1-year term](../facts/rds.md#rds-faq-database-savings-plans-35-percent)
rds-faq-delete-instance-final-snapshot
  claim: When you delete a DB instance you can create a final DB snapshot, which RDS keeps with your other manual snapshots so you can restore the instance later.
  scope: deleting a DB instance and its backups.
  link: [final DB snapshot](../facts/rds.md#rds-faq-delete-instance-final-snapshot)
rds-faq-ec2-connection-automation
  claim: When you choose to connect to an EC2 compute resource while creating a database, RDS automates the networking setup, such as security groups, subnets and ingress and egress rules.
  scope: RDS console database creation.
  link: [Connect to an EC2 compute resource](../facts/rds.md#rds-faq-ec2-connection-automation)
rds-faq-encrypt-existing-via-snapshot-copy
  claim: To encrypt an unencrypted DB instance, create a DB snapshot, copy it with a KMS encryption key, and restore an encrypted DB instance from the encrypted copy.
  scope: RDS encryption at rest.
  link: [creating a copy of that snapshot](../facts/rds.md#rds-faq-encrypt-existing-via-snapshot-copy)
rds-faq-encryption-at-rest-all-engines-kms
  claim: Amazon RDS supports encryption at rest for all database engines, using keys managed in AWS KMS.
  scope: RDS encryption at rest.
  link: [encryption at rest for all database engines](../facts/rds.md#rds-faq-encryption-at-rest-all-engines-kms)
rds-faq-encryption-covers-backups-replicas-snapshots
  claim: On an encrypted DB instance, the data at rest in the underlying storage is encrypted, and so are its automated backups, read replicas and snapshots.
  scope: RDS encryption at rest.
  link: [automated backups, read replicas, and snapshots](../facts/rds.md#rds-faq-encryption-covers-backups-replicas-snapshots)
rds-faq-engines
  claim: Amazon RDS gives you RDS for PostgreSQL, RDS for MySQL, RDS for MariaDB, RDS for SQL Server, RDS for Oracle, or RDS for Db2.
  scope: Amazon RDS engines.
  link: [RDS for Oracle, or RDS for Db2](../facts/rds.md#rds-faq-engines)
rds-faq-enhanced-monitoring-1-second
  claim: Enhanced Monitoring is turned on per instance, with a granularity you choose down to 1 second.
  scope: per DB instance, Enhanced Monitoring granularity; minimum; adjustable.
  link: [1 second](../facts/rds.md#rds-faq-enhanced-monitoring-1-second)
rds-faq-enhanced-monitoring-all-engines
  claim: Enhanced Monitoring supports all Amazon RDS database engines.
  scope: RDS Enhanced Monitoring.
  link: [all Amazon RDS database engines](../facts/rds.md#rds-faq-enhanced-monitoring-all-engines)
rds-faq-enhanced-monitoring-cloudwatch-logs-30-days
  claim: Enhanced Monitoring metrics are delivered to CloudWatch Logs, where the default retention period is 30 days.
  scope: Enhanced Monitoring log retention in CloudWatch Logs; default; adjustable.
  link: [30 days](../facts/rds.md#rds-faq-enhanced-monitoring-cloudwatch-logs-30-days)
rds-faq-enhanced-monitoring-os-metrics
  claim: Enhanced Monitoring collects operating system metrics and process information for a DB instance at the granularity you set.
  scope: RDS Enhanced Monitoring.
  link: [vital operating system metrics and process information](../facts/rds.md#rds-faq-enhanced-monitoring-os-metrics)
rds-faq-existing-code-works
  claim: Amazon RDS gives you the capabilities of a familiar RDS for PostgreSQL, MySQL, MariaDB, SQL Server, Oracle or Db2 database, so the code, applications and tools you already use with your existing databases should work seamlessly with Amazon RDS.
  scope: Amazon RDS engines.
  link: [should work seamlessly with Amazon RDS](../facts/rds.md#rds-faq-existing-code-works)
rds-faq-free-backup-storage-equals-provisioned
  claim: Free backup storage is provided up to the account's total provisioned database storage in the Region; only backup storage above that is charged.
  scope: per account, per Region.
  link: [total provisioned database storage](../facts/rds.md#rds-faq-free-backup-storage-equals-provisioned)
  link: [account-specific and region-specific](../facts/rds.md#rds-faq-free-backup-storage-equals-provisioned)
rds-faq-general-purpose-ssd-3-iops-per-gb
  claim: The FAQ describes General Purpose (SSD) storage as suitable for a broad range of database workloads with moderate I/O requirements, with a baseline of 3 IOPS/GB and the ability to burst up to 3,000 IOPS.
  scope: General Purpose (SSD) storage as the RDS FAQ describes it.
  link: [3 IOPS/GB](../facts/rds.md#rds-faq-general-purpose-ssd-3-iops-per-gb)
  link: [3,000 IOPS](../facts/rds.md#rds-faq-general-purpose-ssd-3-iops-per-gb)
rds-faq-hipaa-eligible
  claim: All Amazon RDS database engines are HIPAA-eligible, so they can store protected health information under a Business Associate Agreement (BAA) with AWS.
  scope: all RDS database engines.
  link: [HIPAA-eligible](../facts/rds.md#rds-faq-hipaa-eligible)
rds-faq-iam-policies-tags
  claim: IAM policies can reference RDS resources such as DB instances, DB snapshots, read replicas, DB parameter groups and DB subnet groups, and tags can be used in IAM policies to list the actions that can be taken on resources with the same tags.
  scope: access control to RDS resources.
  link: [AWS IAM policies](../facts/rds.md#rds-faq-iam-policies-tags)
rds-faq-lambda-connection-recommends-proxy
  claim: The RDS console can set up the network connection between a Lambda function and an RDS or Aurora database, and AWS recommends using RDS Proxy for that connection.
  scope: RDS console Lambda connection setup.
  link: [We recommend that you use RDS Proxy](../facts/rds.md#rds-faq-lambda-connection-recommends-proxy)
  link: [Set up Lambda connection](../facts/rds.md#rds-faq-lambda-connection-recommends-proxy)
rds-faq-maintenance-offline-events
  claim: The maintenance events that take a DB instance offline are compute scaling (generally a few minutes), database engine version upgrades and required software patching.
  scope: RDS maintenance and engine upgrades.
  link: [database engine version upgrades](../facts/rds.md#rds-faq-maintenance-offline-events)
  link: [required software patching](../facts/rds.md#rds-faq-maintenance-offline-events)
rds-faq-maintenance-window-default-30-minute
  claim: If you do not choose a preferred weekly maintenance window when you create a DB instance, RDS assigns a 30-minute default window.
  scope: per DB instance, preferred weekly maintenance window; default; adjustable.
  link: [30-minute](../facts/rds.md#rds-faq-maintenance-window-default-30-minute)
rds-faq-maintenance-window-purpose
  claim: The maintenance window controls when DB instance modifications, engine version upgrades and software patching happen; a scheduled maintenance event starts during that window.
  scope: RDS maintenance and engine upgrades.
  link: [initiated during the maintenance window you identify](../facts/rds.md#rds-faq-maintenance-window-purpose)
rds-faq-major-deprecation-6-month
  claim: After RDS announces that a major engine version is deprecated, you get a minimum six (6) month period to start an upgrade yourself.
  scope: RDS maintenance and engine upgrades.
  link: [minimum six (6) month period](../facts/rds.md#rds-faq-major-deprecation-6-month)
rds-faq-major-upgrade-not-automatic
  claim: Major version upgrades do not happen automatically and must be started by you, except when the major version is deprecated.
  scope: RDS maintenance and engine upgrades.
  link: [will not occur automatically](../facts/rds.md#rds-faq-major-upgrade-not-automatic)
rds-faq-minor-deprecation-3-month
  claim: After RDS announces that a minor engine version is deprecated, there is a three (3) month period before automatic upgrades begin.
  scope: RDS maintenance and engine upgrades.
  link: [three (3) month period](../facts/rds.md#rds-faq-minor-deprecation-3-month)
rds-faq-multi-az-for-write-availability
  claim: To increase write availability and protect recent updates against failure, AWS recommends a Multi-AZ deployment rather than read replicas, because read replica writes happen after the source and replication lag can vary significantly.
  scope: Multi-AZ DB instance deployments.
  link: [run your DB instance as a Multi-AZ deployment](../facts/rds.md#rds-faq-multi-az-for-write-availability)
  link: [this replication “lag” can vary significantly](../facts/rds.md#rds-faq-multi-az-for-write-availability)
rds-faq-multiaz-automatic-failover
  claim: During some planned maintenance, or on DB instance or Availability Zone failure, RDS fails over to the standby automatically, and because the DB instance name record stays the same, the application resumes without manual intervention.
  scope: Multi-AZ DB instance deployments.
  link: [automatically failover to the standby](../facts/rds.md#rds-faq-multiaz-automatic-failover)
  link: [name record for your DB instance](../facts/rds.md#rds-faq-multiaz-automatic-failover)
rds-faq-multiaz-backup-storage-same
  claim: Backup storage usage is the same for a standard and a Multi-AZ deployment; in Multi-AZ, backups are taken from the standby.
  scope: Multi-AZ DB instance deployments.
  link: [taken from your standby](../facts/rds.md#rds-faq-multiaz-backup-storage-same)
rds-faq-multiaz-convert-no-downtime
  claim: Converting a DB instance from Single-AZ to Multi-AZ should cause no downtime, though latency can rise while the standby catches up.
  scope: Multi-AZ DB instance deployments.
  link: [there should be no downtime incurred](../facts/rds.md#rds-faq-multiaz-convert-no-downtime)
rds-faq-multiaz-elevated-latency
  claim: A Multi-AZ deployment may show higher latency than a Single-AZ deployment because of synchronous replication.
  scope: Multi-AZ DB instance deployments.
  link: [elevated latencies](../facts/rds.md#rds-faq-multiaz-elevated-latency)
rds-faq-multiaz-failover-event-notification
  claim: RDS emits a DB instance event when an automatic failover happens, and RDS Event Notifications can notify you of specific DB events.
  scope: Multi-AZ DB instance deployments.
  link: [emit a DB instance event](../facts/rds.md#rds-faq-multiaz-failover-event-notification)
  link: [Amazon RDS Event Notifications](../facts/rds.md#rds-faq-multiaz-failover-event-notification)
rds-faq-multiaz-failover-one-to-two-minutes
  claim: A Multi-AZ DB instance failover typically completes within one to two minutes, from detection of the failure to resumed transactions on the standby.
  scope: Multi-AZ DB instance deployments.
  link: [one to two minutes](../facts/rds.md#rds-faq-multiaz-failover-one-to-two-minutes)
rds-faq-multiaz-failover-triggers
  claim: RDS fails over automatically on loss of availability in the primary Availability Zone, loss of network connectivity to the primary, compute unit failure on the primary, or storage failure on the primary.
  scope: Multi-AZ DB instance deployments.
  link: [Loss of network connectivity to primary](../facts/rds.md#rds-faq-multiaz-failover-triggers)
  link: [Storage failure on primary](../facts/rds.md#rds-faq-multiaz-failover-triggers)
rds-faq-multiaz-no-replication-transfer-charge
  claim: You are not charged for data transfer used to replicate data between the Multi-AZ primary and standby.
  scope: Multi-AZ DB instance deployments.
  link: [You are not charged for the data transfer](../facts/rds.md#rds-faq-multiaz-no-replication-transfer-charge)
rds-faq-multiaz-reboot-with-failover
  claim: You can force a failover by choosing to fail over when you reboot the DB instance.
  scope: Multi-AZ DB instance deployments.
  link: [initiate a failover when rebooting your instance](../facts/rds.md#rds-faq-multiaz-reboot-with-failover)
rds-faq-multiaz-reduces-maintenance-impact
  claim: Running a DB instance as a Multi-AZ deployment can further reduce the impact of a maintenance event.
  scope: Multi-AZ DB instance deployments.
  link: [further reduce the impact of a maintenance event](../facts/rds.md#rds-faq-multiaz-reduces-maintenance-impact)
rds-faq-multiaz-replication-synchronous
  claim: Multi-AZ replication is synchronous: all database writes are concurrent on the primary and standby, which protects the latest database updates because they should be available on the standby if failover is required.
  scope: Multi-AZ DB instance deployments.
  link: [concurrent on the primary and standby](../facts/rds.md#rds-faq-multiaz-replication-synchronous)
rds-faq-multiaz-standby-no-reads
  claim: In a Multi-AZ DB instance deployment, the standby cannot serve read requests; Multi-AZ is for availability and durability, not read scaling.
  scope: Multi-AZ DB instance deployments; Multi-AZ DB instance deployment (one standby).
  link: [a Multi-AZ standby cannot serve read requests](../facts/rds.md#rds-faq-multiaz-standby-no-reads)
rds-faq-multiaz-synchronous-standby
  claim: In a Multi-AZ DB instance deployment, RDS provisions and maintains a synchronous standby replica in a different Availability Zone.
  scope: Multi-AZ DB instance deployments.
  link: [synchronous “standby” replica in a different Availability Zone](../facts/rds.md#rds-faq-multiaz-synchronous-standby)
rds-faq-multiaz-two-readable-standbys-proxy
  claim: RDS Proxy supports Multi-AZ with two readable standbys, which gives failovers of typically under 35 seconds, added read capacity, and minor version upgrade downtime of typically under 1 second.
  scope: Multi-AZ DB cluster deployments (two readable standbys) with RDS Proxy.
  link: [typically under 35 second failovers](../facts/rds.md#rds-faq-multiaz-two-readable-standbys-proxy)
  link: [two readable standbys](../facts/rds.md#rds-faq-multiaz-two-readable-standbys-proxy)
rds-faq-onprem-access-security-groups
  claim: Access to an RDS database over the internet must be turned on intentionally through security groups, and can be limited to specific IPs, IP ranges or subnets of your data center.
  scope: network access to RDS databases.
  link: [by configuring Security Groups](../facts/rds.md#rds-faq-onprem-access-security-groups)
rds-faq-optimized-reads-nvme-2x
  claim: For MySQL and MariaDB workloads that use temporary objects, RDS Optimized Reads places the temporary objects on NVMe-based instance storage instead of the EBS volume, speeding up complex query processing by up to 2X.
  scope: RDS for MySQL and RDS for MariaDB.
  link: [NVMe-based instance storage](../facts/rds.md#rds-faq-optimized-reads-nvme-2x)
  link: [up to 2X](../facts/rds.md#rds-faq-optimized-reads-nvme-2x)
rds-faq-optimized-writes-2x
  claim: RDS Optimized Writes gives RDS for MySQL up to 2x improved write transaction throughput, at no additional cost.
  scope: RDS for MySQL.
  link: [up to 2x improved write transaction throughput](../facts/rds.md#rds-faq-optimized-writes-2x)
rds-faq-oracle-1-database
  claim: An RDS for Oracle DB instance holds 1 database, with no software limit on the number of schemas per database.
  scope: per DB instance, RDS for Oracle; maximum; not adjustable.
  link: [1 database per instance](../facts/rds.md#rds-faq-oracle-1-database)
rds-faq-oracle-sqlserver-additional-volumes-256-tib
  claim: RDS for Oracle and RDS for SQL Server can add up to three additional storage volumes of up to 64 TiB each, for a maximum of 256 TiB of storage.
  scope: per DB instance, RDS for Oracle and RDS for SQL Server, primary plus additional storage volumes; maximum; not adjustable.
  link: [256 TiB](../facts/rds.md#rds-faq-oracle-sqlserver-additional-volumes-256-tib)
  link: [64 TiB](../facts/rds.md#rds-faq-oracle-sqlserver-additional-volumes-256-tib)
rds-faq-parameter-group-container
  claim: A DB parameter group is a container for engine configuration values that can be applied to one or more DB instances.
  scope: DB parameter groups and option groups.
  link: [container](../facts/rds.md#rds-faq-parameter-group-container)
rds-faq-parameter-group-default
  claim: If you create a DB instance without specifying a DB parameter group, a default DB parameter group is used.
  scope: per DB instance created without a DB parameter group; default; adjustable.
  link: [a default DB Parameter Group is used](../facts/rds.md#rds-faq-parameter-group-default)
rds-faq-parameter-group-updates-all
  claim: All DB instances that use a DB parameter group get every parameter update made to that group.
  scope: DB parameter groups and option groups.
  link: [get all the parameter updates](../facts/rds.md#rds-faq-parameter-group-updates-all)
rds-faq-performance-insights-what
  claim: Amazon RDS Performance Insights is a performance tuning and monitoring feature for assessing the load on a database and deciding when and where to act.
  scope: CloudWatch Database Insights and Performance Insights.
  link: [assess the load on their database](../facts/rds.md#rds-faq-performance-insights-what)
rds-faq-piops-for-oltp
  claim: Provisioned IOPS (SSD) storage is optimized for I/O-intensive, transactional (OLTP) database workloads.
  scope: RDS DB instance storage and performance.
  link: [I/O-intensive, transactional (OLTP) database workloads](../facts/rds.md#rds-faq-piops-for-oltp)
rds-faq-piops-rate-for-lifetime
  claim: With Provisioned IOPS (SSD) storage you specify an IOPS rate when you create the DB instance, and RDS provisions that rate for the lifetime of the DB instance.
  scope: RDS DB instance storage and performance.
  link: [provisions that IOPS rate](../facts/rds.md#rds-faq-piops-rate-for-lifetime)
rds-faq-pitr-any-second-latest-restorable
  claim: A point-in-time restore can target any second in the retention period up to the Latest Restorable Time, which is typically within the last five minutes.
  scope: RDS automated backups and snapshots.
  link: [any second during your retention period](../facts/rds.md#rds-faq-pitr-any-second-latest-restorable)
  link: [last five minutes](../facts/rds.md#rds-faq-pitr-any-second-latest-restorable)
rds-faq-private-subnet-backend
  claim: In a VPC you can create a public-facing subnet with Internet access for web servers and place the backend RDS DB instances in a private-facing subnet with no Internet access.
  scope: RDS DB instances in a VPC.
  link: [private-facing subnet with no Internet access](../facts/rds.md#rds-faq-private-subnet-backend)
rds-faq-quota-db-instances-40
  claim: By default, an account can have up to 40 DB instances in total.
  scope: per account, all RDS DB instances in total; default; adjustable.
  link: [40 DB instances](../facts/rds.md#rds-faq-quota-db-instances-40)
  link: [40 Amazon RDS DB instances](../facts/rds.md#rds-faq-quota-db-instances-40)
rds-faq-quota-license-included-10
  claim: Of the default 40 DB instances, up to 10 can be RDS for Oracle or RDS for SQL Server DB instances under the License Included model.
  scope: per account, RDS for Oracle or RDS for SQL Server DB instances under the License Included model; default; not adjustable.
  link: [up to 10](../facts/rds.md#rds-faq-quota-license-included-10)
rds-faq-rds-vs-ec2-ami
  claim: Amazon RDS runs a fully managed relational database and offloads database administration; a relational database AMI on Amazon EC2 means you manage your own relational database.
  scope: Amazon RDS compared with a database AMI on Amazon EC2.
  link: [offloading database administration](../facts/rds.md#rds-faq-rds-vs-ec2-ami)
  link: [manage your own relational database](../facts/rds.md#rds-faq-rds-vs-ec2-ami)
rds-faq-read-replica-asynchronous
  claim: Read replicas of RDS for MySQL, MariaDB, PostgreSQL, Oracle and SQL Server use the engines' native asynchronous replication, not synchronous replication.
  scope: read replicas of RDS for MySQL, MariaDB, PostgreSQL, Oracle and SQL Server.
  link: [native asynchronous replication](../facts/rds.md#rds-faq-read-replica-asynchronous)
rds-faq-read-replica-billing
  claim: A read replica is billed as a standard DB instance at the same rates, and data transfer for replication between the source and a read replica in the same Region is not charged.
  scope: RDS DB instance read replicas.
  link: [billed as a standard DB Instance](../facts/rds.md#rds-faq-read-replica-billing)
  link: [within the same AWS Region](../facts/rds.md#rds-faq-read-replica-billing)
rds-faq-read-replica-can-be-multiaz
  claim: RDS for MySQL, MariaDB, PostgreSQL and Oracle let you make a read replica itself Multi-AZ, for disaster recovery and less downtime from engine upgrades.
  scope: RDS DB instance read replicas.
  link: [enable Multi-AZ configuration on read replicas](../facts/rds.md#rds-faq-read-replica-can-be-multiaz)
rds-faq-read-replica-cross-region-lag
  claim: For a cross-Region read replica, the delay before written data is available on the replica depends on the network latency between the two Regions.
  scope: cross-Region read replicas.
  link: [network latency between the two regions](../facts/rds.md#rds-faq-read-replica-cross-region-lag)
rds-faq-read-replica-disaster-recovery
  claim: A read replica can be used for disaster recovery of the source DB instance, in the same Region or in another Region.
  scope: RDS DB instance read replicas.
  link: [disaster recovery of the source DB instance](../facts/rds.md#rds-faq-read-replica-disaster-recovery)
rds-faq-read-replica-from-multiaz-source
  claim: A read replica can use a Multi-AZ DB instance as its source, combining write availability and durability with read scalability.
  scope: RDS DB instance read replicas.
  link: [use the two in conjunction](../facts/rds.md#rds-faq-read-replica-from-multiaz-source)
rds-faq-read-replica-lag-metric
  claim: The number of seconds a read replica is behind its primary is published as the CloudWatch metric Replica Lag.
  scope: RDS DB instance read replicas.
  link: [Replica Lag](../facts/rds.md#rds-faq-read-replica-lag-metric)
rds-faq-read-replica-mysql-ddl
  claim: RDS for MySQL can be configured to allow DDL statements on a read replica by setting the read_only parameter to 0; RDS for PostgreSQL does not support DDL on a read replica.
  scope: RDS for MySQL and RDS for PostgreSQL read replicas.
  link: [permit DDL SQL statements against a read replica](../facts/rds.md#rds-faq-read-replica-mysql-ddl)
  link: [setting the “read_only” parameter to “0.”](../facts/rds.md#rds-faq-read-replica-mysql-ddl)
rds-faq-read-replica-needs-backups
  claim: Automatic backups must be turned on (retention period other than 0) on the source DB instance before you add read replicas, and must stay on for read replicas to work.
  scope: RDS DB instance read replicas.
  link: [Backups must remain enabled](../facts/rds.md#rds-faq-read-replica-needs-backups)
rds-faq-read-replica-oracle-sqlserver-no-cascade
  claim: RDS for Oracle and RDS for SQL Server do not support read replicas of read replicas.
  scope: RDS for Oracle and RDS for SQL Server read replicas.
  link: [not currently supported](../facts/rds.md#rds-faq-read-replica-oracle-sqlserver-no-cascade)
rds-faq-read-replica-own-endpoint
  claim: You connect to a read replica like a standard DB instance, using its own endpoint; with several read replicas, your application decides how to spread the read traffic.
  scope: RDS DB instance read replicas.
  link: [it is up to your application](../facts/rds.md#rds-faq-read-replica-own-endpoint)
  link: [retrieve the endpoint(s) for your read replica(s)](../facts/rds.md#rds-faq-read-replica-own-endpoint)
rds-faq-read-replica-reporting
  claim: Business reporting queries can run against a read replica instead of the primary production DB instance.
  scope: RDS DB instance read replicas.
  link: [Business reporting or data warehousing scenarios](../facts/rds.md#rds-faq-read-replica-reporting)
rds-faq-read-replica-source-deleted-mysql
  claim: An RDS for MySQL or MariaDB read replica stays active and keeps serving reads after its source DB instance is deleted.
  scope: RDS for MySQL and RDS for MariaDB read replicas.
  link: [stay active and continue accepting read traffic](../facts/rds.md#rds-faq-read-replica-source-deleted-mysql)
rds-faq-read-replica-source-deleted-postgresql
  claim: If you delete an RDS for PostgreSQL DB instance that has read replicas, all its read replicas are promoted to standalone DB instances that accept reads and writes.
  scope: RDS for PostgreSQL read replicas.
  link: [promoted to standalone DB Instances](../facts/rds.md#rds-faq-read-replica-source-deleted-postgresql)
rds-faq-read-replica-three-tiers
  claim: Amazon Aurora, RDS for MySQL and RDS for MariaDB can have three tiers of read replicas (a replica of a replica of a replica).
  scope: Aurora, RDS for MySQL and RDS for MariaDB read replicas.
  link: [three tiers of read replicas](../facts/rds.md#rds-faq-read-replica-three-tiers)
rds-faq-read-replica-use-cases
  claim: A common reason for a read replica is to scale beyond the compute or I/O capacity of a single DB instance for read-heavy workloads.
  scope: RDS DB instance read replicas.
  link: [read-heavy database workloads](../facts/rds.md#rds-faq-read-replica-use-cases)
rds-faq-required-patching-security-durability
  claim: RDS schedules required software patching automatically only for patches that are security and durability related.
  scope: RDS maintenance and engine upgrades.
  link: [security and durability related](../facts/rds.md#rds-faq-required-patching-security-durability)
rds-faq-restore-creates-new-instance
  claim: A restore to a point in time or from a DB snapshot creates a new DB instance with a new endpoint.
  scope: restoring a DB instance from a snapshot or a point in time.
  link: [created with a new endpoint](../facts/rds.md#rds-faq-restore-creates-new-instance)
rds-faq-retention-0-disables-backups
  claim: Setting the backup retention period to 0 turns off automated backups, which AWS does not recommend.
  scope: RDS automated backups and snapshots.
  link: [setting the retention period to 0](../facts/rds.md#rds-faq-retention-0-disables-backups)
rds-faq-retention-default-7-max-35-days
  claim: The automated backup retention period is 7 days by default and can be set to up to 35 days.
  scope: per DB instance, automated backup retention period; default; adjustable.
  link: [7 days](../facts/rds.md#rds-faq-retention-default-7-max-35-days)
  link: [35 days](../facts/rds.md#rds-faq-retention-default-7-max-35-days)
rds-faq-retention-not-0-for-replica-source
  claim: The backup retention period cannot be set to 0 if the DB instance is a source for read replicas.
  scope: RDS automated backups and snapshots.
  link: [cannot be set to 0](../facts/rds.md#rds-faq-retention-not-0-for-replica-source)
rds-faq-ri-cannot-cancel
  claim: You cannot cancel an RDS reserved DB instance, and the one-time payment (if any) is not refundable.
  scope: RDS reserved DB instances.
  link: [you cannot cancel your reserved DB instance](../facts/rds.md#rds-faq-ri-cannot-cancel)
rds-faq-ri-multiaz-covers-two-single-az
  claim: With an engine and license model that support size flexibility, a Multi-AZ reserved instance covers usage for two Single-AZ DB instances.
  scope: RDS reserved DB instances; engine and license model that support reserved instance size flexibility.
  link: [two Single-AZ DB instances](../facts/rds.md#rds-faq-ri-multiaz-covers-two-single-az)
rds-faq-ri-multiaz-option
  claim: Reserved instances are available for Multi-AZ deployments: you select the Multi-AZ option when you buy the reservation.
  scope: RDS reserved DB instances.
  link: [select the Multi-AZ option](../facts/rds.md#rds-faq-ri-multiaz-option)
rds-faq-ri-not-capacity-reservation
  claim: RDS reserved instances are bought for a Region, not an Availability Zone, so they are not capacity reservations.
  scope: RDS reserved DB instances.
  link: [they are not capacity reservations](../facts/rds.md#rds-faq-ri-not-capacity-reservation)
rds-faq-ri-payment-options
  claim: Reserved instances have three payment options: No Upfront, Partial Upfront and All Upfront.
  scope: RDS reserved DB instances.
  link: [No Upfront, Partial Upfront, All Upfront](../facts/rds.md#rds-faq-ri-payment-options)
rds-faq-ri-read-replica
  claim: A DB instance reservation can apply to a read replica when the DB instance class and Region are the same.
  scope: RDS reserved DB instances.
  link: [applied to a read replica](../facts/rds.md#rds-faq-ri-read-replica)
rds-faq-ri-region-fixed
  claim: A reserved instance is tied to one Region for its whole term and cannot be moved, but it can be used in any Availability Zone of that Region.
  scope: RDS reserved DB instances.
  link: [fixed for the lifetime of the reservation](../facts/rds.md#rds-faq-ri-region-fixed)
rds-faq-ri-size-flexibility
  claim: For engines eligible for size flexibility (MySQL, MariaDB, PostgreSQL, Amazon Aurora, Oracle Bring Your Own License), a reservation applies to a running DB instance of any size in the same instance family, engine and Region.
  scope: RDS reserved DB instances.
  link: [any size within the same instance family](../facts/rds.md#rds-faq-ri-size-flexibility)
rds-faq-ri-terms-one-or-three-year
  claim: RDS reserved instances reserve a DB instance for a one or three year term in exchange for a significant discount compared to On-Demand pricing.
  scope: RDS reserved DB instances.
  link: [one or three year term](../facts/rds.md#rds-faq-ri-terms-one-or-three-year)
rds-faq-scale-beyond-largest-partitioning
  claim: When an application needs more compute than the largest DB instance class or more storage than the maximum allocation, you can partition the data across multiple DB instances.
  scope: scaling beyond one DB instance.
  link: [implement partitioning](../facts/rds.md#rds-faq-scale-beyond-largest-partitioning)
rds-faq-snapshots-user-initiated-kept-until-deleted
  claim: DB snapshots are user-initiated, can be taken as often as you wish, and are kept until you explicitly delete them.
  scope: manual DB snapshots.
  link: [kept until you explicitly delete them](../facts/rds.md#rds-faq-snapshots-user-initiated-kept-until-deleted)
  link: [user-initiated](../facts/rds.md#rds-faq-snapshots-user-initiated-kept-until-deleted)
rds-faq-sqlserver-100-databases
  claim: An RDS for SQL Server DB instance holds up to 100 databases.
  scope: per DB instance, RDS for SQL Server; maximum; not adjustable.
  link: [100 databases](../facts/rds.md#rds-faq-sqlserver-100-databases)
rds-faq-ssl-tls-adds-latency
  claim: SSL/TLS encryption is compute-intensive and increases the latency of the database connection.
  scope: encryption in transit (SSL/TLS) to RDS databases.
  link: [increase the latency of your database connection](../facts/rds.md#rds-faq-ssl-tls-adds-latency)
rds-faq-ssl-tls-all-engines
  claim: SSL/TLS encryption of connections is supported for all Amazon RDS engines, and RDS generates an SSL/TLS certificate for each DB instance.
  scope: encryption in transit (SSL/TLS) to RDS databases.
  link: [supported for all Amazon RDS engines](../facts/rds.md#rds-faq-ssl-tls-all-engines)
rds-faq-storage-scale-stays-available
  claim: Allocated storage can be increased while the DB instance stays available.
  scope: storage increases of a DB instance.
  link: [while maintaining DB Instance availability](../facts/rds.md#rds-faq-storage-scale-stays-available)
rds-faq-subnet-group-every-az
  claim: A DB subnet group should have at least one subnet in every Availability Zone of the Region.
  scope: DB subnet groups.
  link: [at least one subnet for every Availability Zone](../facts/rds.md#rds-faq-subnet-group-every-az)
rds-faq-tde-oracle-sqlserver
  claim: RDS for Oracle and RDS for SQL Server support the Transparent Data Encryption (TDE) of those engines.
  scope: RDS for Oracle and RDS for SQL Server.
  link: [Transparent Data Encryption (TDE)](../facts/rds.md#rds-faq-tde-oracle-sqlserver)
rds-faq-test-upgrade-on-restored-copy
  claim: To test a new engine version, create a DB snapshot, restore it to a new DB instance, and upgrade that new instance first.
  scope: RDS maintenance and engine upgrades.
  link: [restoring from the DB snapshot](../facts/rds.md#rds-faq-test-upgrade-on-restored-copy)
rds-faq-upgrade-downtime-even-multiaz
  claim: Upgrading a DB engine version requires downtime, even for Multi-AZ instances.
  scope: RDS maintenance and engine upgrades.
  link: [even for Multi-AZ instances](../facts/rds.md#rds-faq-upgrade-downtime-even-multiaz)
rds-faq-upgrade-next-window-by-default
  claim: By default, a manual engine version upgrade is applied during the next maintenance window; you can choose Apply Immediately to upgrade at once.
  scope: manual engine version upgrade of a DB instance; default; adjustable.
  link: [next maintenance window](../facts/rds.md#rds-faq-upgrade-next-window-by-default)
  link: [Apply Immediately](../facts/rds.md#rds-faq-upgrade-next-window-by-default)
rds-faq-use-dns-name-ip-changes
  claim: Connect to a DB instance by its DNS name, because the underlying IP address can change, for example during failover.
  scope: connecting to a DB instance.
  link: [use the DNS Name to connect](../facts/rds.md#rds-faq-use-dns-name-ip-changes)
rds-firewall-blocks-until-sg-rules
  claim: When you first create a DB instance, its firewall blocks all database access except through rules in its associated security group.
  scope: new DB instances.
  link: [its firewall prevents any database access](../facts/rds.md#rds-firewall-blocks-until-sg-rules)
rds-free-tier-credits-after-2025-07-15
  claim: The RDS FAQ says accounts that sign up for the AWS Free Tier after July 15, 2025 choose a Free Plan or a Paid Plan, and either plan offers $100 in credits plus up to an additional $100 in credits for activating foundational AWS services; accounts that signed up before that date can keep using RDS for free for up to 12 months on select Single-AZ instances with up to 750 hours per month.
  scope: AWS Free Tier for Amazon RDS; depends on sign-up date; how long the plan and credits last is set by the AWS Free Tier terms, not taught here.
  link: [$100 in credits](../facts/rds.md#rds-free-tier-credits-after-2025-07-15)
  link: [750 hours per month](../facts/rds.md#rds-free-tier-credits-after-2025-07-15)
  link: [July 15, 2025](../facts/rds.md#rds-free-tier-credits-after-2025-07-15)
  changed: 2025-07-15: was 750 hours per month
rds-iam-auth-extra-memory
  claim: IAM DB authentication needs between 300 and 1000 MiB of extra memory on the database for reliable connectivity.
  scope: per DB instance using IAM DB authentication; minimum; not adjustable; on burstable classes, reduce memory used by other parameters by the same amount.
  link: [between 300 and 1000 MiB](../facts/rds.md#rds-iam-auth-extra-memory)
  say: three hundred to one thousand mebibytes
rds-iam-auth-token-lifetime
  claim: An IAM database authentication token is generated with AWS Signature Version 4 and has a lifetime of 15 minutes; it is used only for authentication and doesn't affect the session after it is established.
  scope: per authentication token; fixed; not adjustable; an established session is not affected when the token expires.
  link: [15 minutes](../facts/rds.md#rds-iam-auth-token-lifetime)
  say: fifteen minutes
rds-iam-manages-resources-not-login
  claim: IAM policies decide who can manage RDS resources (create, describe, modify, delete DB instances), while the DB engine's own security features control who can log in to the databases.
  scope: access to RDS resources and databases; IAM database authentication is a separate option for some engines.
  link: [who is allowed to manage Amazon RDS resources](../facts/rds.md#rds-iam-manages-resources-not-login)
  link: [Use the security features of your DB engine](../facts/rds.md#rds-iam-manages-resources-not-login)
rds-instance-class-changeable
  claim: You can change the DB instance class of a DB instance when your requirements change, for example to scale up to a larger size of the same class type.
  scope: DB instance classes.
  link: [you can change your DB instance class](../facts/rds.md#rds-instance-class-changeable)
  link: [scale up](../facts/rds.md#rds-instance-class-changeable)
rds-keep-automated-backup-longer-copy
  claim: RDS deletes automated backups at the end of their retention period, when automated backups are disabled, and when the DB instance is deleted; to keep one longer, copy it to a manual snapshot, which is kept until you delete it.
  scope: RDS automated backups and snapshots.
  link: [copy it to create a manual snapshot](../facts/rds.md#rds-keep-automated-backup-longer-copy)
  link: [retained until you delete it](../facts/rds.md#rds-keep-automated-backup-longer-copy)
rds-kms-aws-managed-key-aws-rds
  claim: By default the RDS AWS managed key (aws/rds) is used for encryption, and you cannot manage, rotate or delete it; for full control over a KMS key you must create a customer managed key.
  scope: RDS encryption at rest; default; adjustable.
  link: [aws/rds](../facts/rds.md#rds-kms-aws-managed-key-aws-rds)
  link: [can't manage, rotate, or delete](../facts/rds.md#rds-kms-aws-managed-key-aws-rds)
  link: [you must create a *customer managed key*](../facts/rds.md#rds-kms-aws-managed-key-aws-rds)
rds-kms-envelope-encryption-cloudtrail
  claim: Amazon RDS integrates with AWS KMS and uses envelope encryption; every action taken with an AWS managed or customer managed key can be audited in AWS CloudTrail.
  scope: RDS encryption at rest.
  link: [Amazon RDS uses envelope encryption.](../facts/rds.md#rds-kms-envelope-encryption-cloudtrail)
  link: [audit logs of every action](../facts/rds.md#rds-kms-envelope-encryption-cloudtrail)
rds-lambda-console-connect-proxy
  claim: The RDS console can set up the connection between a Lambda function and a DB instance, directly or through RDS Proxy; the Lambda function must be in the same VPC as the DB instance.
  scope: console automatic connectivity.
  link: [same VPC as the DB instance](../facts/rds.md#rds-lambda-console-connect-proxy)
  link: [through RDS Proxy](../facts/rds.md#rds-lambda-console-connect-proxy)
rds-long-term-backup-export-s3
  claim: For very long-term backups of MariaDB, MySQL and PostgreSQL data, AWS recommends exporting snapshot data to Amazon S3, because a snapshot cannot be restored to a major engine version that is no longer supported.
  scope: RDS for MariaDB, MySQL and PostgreSQL.
  link: [exporting snapshot data to Amazon S3](../facts/rds.md#rds-long-term-backup-export-s3)
  link: [very long-term backups](../facts/rds.md#rds-long-term-backup-export-s3)
rds-maintenance-mandatory-upgrade-outside-window
  claim: Changing the maintenance window does not prevent mandatory upgrades: after the mandatory apply date, RDS can apply a forced upgrade outside the preferred maintenance window.
  scope: forced upgrades; after the mandatory apply date.
  link: [outside of your preferred maintenance window](../facts/rds.md#rds-maintenance-mandatory-upgrade-outside-window)
  link: [after the mandatory apply date has passed](../facts/rds.md#rds-maintenance-mandatory-upgrade-outside-window)
rds-maintenance-multi-az-standby-first
  claim: For a Multi-AZ deployment, RDS applies operating system updates by maintaining the standby, promoting it to primary, and then maintaining the old primary, which becomes the new standby; this reduces the impact of maintenance.
  scope: Multi-AZ deployments, operating system updates.
  link: [Perform maintenance on the standby.](../facts/rds.md#rds-maintenance-multi-az-standby-first)
  link: [Promote the standby to primary.](../facts/rds.md#rds-maintenance-multi-az-standby-first)
rds-maintenance-window-default
  claim: If you don't specify a maintenance window, RDS assigns a weekly 30-minute maintenance window selected at random from an 8-hour block of time per Region, on a randomly selected day of the week.
  scope: per DB instance; default; adjustable; larger maintenance events may take more than 30 minutes.
  link: [30-minute maintenance window](../facts/rds.md#rds-maintenance-window-default)
  link: [an 8-hour block of time per region](../facts/rds.md#rds-maintenance-window-default)
  say: a thirty-minute weekly window | an eight-hour block per Region
rds-maintenance-window-no-overlap-backup
  claim: The maintenance window and the backup window of a DB instance cannot overlap.
  scope: per DB instance.
  link: [cannot overlap](../facts/rds.md#rds-maintenance-window-no-overlap-backup)
rds-maintenance-window-offline-patching
  claim: Some maintenance, such as required OS or database patching, takes the DB instance offline for a short time; required patching is scheduled automatically only for security and reliability patches, typically once every few months.
  scope: required patching.
  link: [offline for a short time](../facts/rds.md#rds-maintenance-window-offline-patching)
  link: [typically once every few months](../facts/rds.md#rds-maintenance-window-offline-patching)
rds-maintenance-window-weekly
  claim: Every DB instance has a weekly maintenance window, a time interval in which system changes such as modifications and software patching are applied.
  scope: RDS maintenance and engine upgrades.
  link: [weekly time interval](../facts/rds.md#rds-maintenance-window-weekly)
rds-major-vs-minor-upgrade
  claim: A major engine version upgrade can bring changes that are not compatible with existing applications and must be started manually; a minor version upgrade is backward-compatible and can be applied manually or with Auto minor version upgrade.
  scope: DB engine version upgrades.
  link: [not compatible with existing applications](../facts/rds.md#rds-major-vs-minor-upgrade)
  link: [backward-compatible](../facts/rds.md#rds-major-vs-minor-upgrade)
  link: [**Auto minor version upgrade**](../facts/rds.md#rds-major-vs-minor-upgrade)
rds-managed-tasks
  claim: Amazon RDS manages backups, software patching, automatic failure detection and recovery.
  scope: Amazon RDS managed operations.
  link: [manages backups, software patching](../facts/rds.md#rds-managed-tasks)
  link: [automatic failure detection, and recovery](../facts/rds.md#rds-managed-tasks)
rds-manual-snapshots-dont-expire
  claim: Unlike automated backups, manual snapshots are not subject to the backup retention period and do not expire.
  scope: manual DB snapshots.
  link: [Snapshots don't expire.](../facts/rds.md#rds-manual-snapshots-dont-expire)
  link: [aren't subject to the backup retention period](../facts/rds.md#rds-manual-snapshots-dont-expire)
rds-master-password-length
  claim: The master password length depends on the engine: Db2 8–255, Oracle 8–30, MariaDB and MySQL 8–41, SQL Server and PostgreSQL 8–128 printable ASCII characters.
  scope: per DB instance master user; maximum; excluding /, ", a space and @.
  link: [MariaDB and MySQL: 8–41](../facts/rds.md#rds-master-password-length)
  link: [SQL Server and PostgreSQL: 8–128](../facts/rds.md#rds-master-password-length)
  say: eight to forty-one characters for MySQL and MariaDB | eight to one hundred twenty-eight characters for PostgreSQL and SQL Server
rds-master-username-rules
  claim: The master username can contain 1–16 alphanumeric characters and underscores, must start with a letter, and can't be changed after the DB instance is created.
  scope: per DB instance master user; maximum; can't be a word reserved by the database engine.
  link: [1–16 alphanumeric characters and underscores](../facts/rds.md#rds-master-username-rules)
  say: one to sixteen letters, digits or underscores
rds-max-connections-from-instance-class
  claim: If you do not set the connection limit (such as max_connections) in the parameter group, Amazon RDS calculates it automatically from the DB instance class, so it can change when you scale the instance.
  scope: max_connections parameter; default; adjustable; not set explicitly in the parameter group.
  link: [based on the database instance class](../facts/rds.md#rds-max-connections-from-instance-class)
  link: [can change when you scale your database instances](../facts/rds.md#rds-max-connections-from-instance-class)
rds-max-connections-t3-micro
  claim: The default maximum number of connections for a MySQL DB instance on a db.t3.micro DB instance class is approximately 60, because max_connections is derived from instance memory.
  scope: per DB instance (MySQL, db.t3.micro); default; adjustable; set in the parameter group; depends on instance class memory.
  link: [approximately 60](../facts/rds.md#rds-max-connections-t3-micro)
  say: about sixty
rds-multi-az-automatic-failover-infrastructure
  claim: When a planned or unplanned outage of a Multi-AZ DB instance results from an infrastructure defect, Amazon RDS automatically switches to the standby replica in another Availability Zone.
  scope: Multi-AZ DB instance deployment; the outage results from an infrastructure defect.
  link: [automatically switches to a standby replica](../facts/rds.md#rds-multi-az-automatic-failover-infrastructure)
  link: [planned or unplanned outage](../facts/rds.md#rds-multi-az-automatic-failover-infrastructure)
rds-multi-az-billing-write-io-doubles
  claim: A Multi-AZ DB instance deployment is billed at Multi-AZ pricing; write I/O usage doubles because data is synchronously replicated to the standby, read I/O stays the same, and replication data transfer between primary and standby is not charged.
  scope: Multi-AZ DB instance deployments.
  link: [Multi-AZ pricing](../facts/rds.md#rds-multi-az-billing-write-io-doubles)
  link: [Write I/O usage associated with database updates](../facts/rds.md#rds-multi-az-billing-write-io-doubles)
  link: [not charged for the data transfer](../facts/rds.md#rds-multi-az-billing-write-io-doubles)
  link: [Read I/O usage will remain the same](../facts/rds.md#rds-multi-az-billing-write-io-doubles)
rds-multi-az-cluster-benefits
  claim: Compared with Multi-AZ DB instance deployments, Multi-AZ DB clusters provide high availability, more capacity for read workloads and lower write latency.
  scope: Multi-AZ DB cluster compared with Multi-AZ DB instance.
  link: [increased capacity for read workloads](../facts/rds.md#rds-multi-az-cluster-benefits)
  link: [lower write latency](../facts/rds.md#rds-multi-az-cluster-benefits)
rds-multi-az-cluster-endpoint-survives-failover
  claim: If the writer of a Multi-AZ DB cluster fails, the cluster fails over automatically to a new writer and keeps serving connection requests to the cluster endpoint with minimal interruption.
  scope: Multi-AZ DB cluster deployment.
  link: [automatically fails over to a new writer](../facts/rds.md#rds-multi-az-cluster-endpoint-survives-failover)
  link: [minimal interruption of service](../facts/rds.md#rds-multi-az-cluster-endpoint-survives-failover)
rds-multi-az-cluster-engines-mysql-postgresql
  claim: Multi-AZ DB clusters are available with RDS for MySQL and RDS for PostgreSQL (in the listed Regions and engine versions); they aren't available with RDS for Db2, MariaDB, Oracle or SQL Server.
  scope: Multi-AZ DB cluster deployment, per engine.
  link: [aren't available with the following engines](../facts/rds.md#rds-multi-az-cluster-engines-mysql-postgresql)
rds-multi-az-cluster-failover-resolves-lag
  claim: In a Multi-AZ DB cluster, a failover must first resolve replica lag before it promotes a new writer, so replica lag affects failover time.
  scope: Multi-AZ DB cluster deployment.
  link: [must first resolve the replica lag](../facts/rds.md#rds-multi-az-cluster-failover-resolves-lag)
rds-multi-az-cluster-failover-time
  claim: Failover of a Multi-AZ DB cluster typically takes under 35 seconds and completes when both reader DB instances have applied the outstanding transactions from the failed writer.
  scope: per Multi-AZ DB cluster; fixed; not adjustable; typical value; depends on database activity.
  link: [under 35 seconds](../facts/rds.md#rds-multi-az-cluster-failover-time)
  say: under thirty-five seconds
rds-multi-az-cluster-instance-read-replicas
  claim: You can create DB instance read replicas from a Multi-AZ DB cluster to scale reads beyond the cluster, but you cannot currently create a Multi-AZ DB cluster read replica from an existing Multi-AZ DB cluster.
  scope: Multi-AZ DB clusters.
  link: [one or more DB instance read replicas](../facts/rds.md#rds-multi-az-cluster-instance-read-replicas)
  link: [can't create a Multi-AZ DB cluster read replica](../facts/rds.md#rds-multi-az-cluster-instance-read-replicas)
rds-multi-az-cluster-native-replication-failover-target
  claim: In a Multi-AZ DB cluster, reader DB instances are automatic failover targets and also serve read traffic; on a writer outage RDS fails over to the reader with the most recent change record.
  scope: Multi-AZ DB cluster deployment.
  link: [act as automatic failover targets](../facts/rds.md#rds-multi-az-cluster-native-replication-failover-target)
  link: [has the most recent change record](../facts/rds.md#rds-multi-az-cluster-native-replication-failover-target)
rds-multi-az-cluster-no-storage-autoscaling
  claim: Multi-AZ DB clusters do not support storage autoscaling by setting the maximum allocated storage; as an alternative you scale storage manually.
  scope: Multi-AZ DB cluster deployment.
  link: [you can scale storage manually](../facts/rds.md#rds-multi-az-cluster-no-storage-autoscaling)
rds-multi-az-cluster-not-aurora
  claim: RDS Multi-AZ DB clusters are not the same as Aurora DB clusters.
  scope: Multi-AZ DB cluster deployments.
  link: [aren't the same as Aurora DB clusters](../facts/rds.md#rds-multi-az-cluster-not-aurora)
rds-multi-az-cluster-read-replica-from-instance
  claim: A Multi-AZ DB cluster read replica is a cluster created from a source DB instance and receives its updates asynchronously; it can be used to migrate to a Multi-AZ DB cluster with minimal downtime.
  scope: Multi-AZ DB cluster read replicas.
  link: [create from a source DB instance](../facts/rds.md#rds-multi-az-cluster-read-replica-from-instance)
  link: [asynchronously copied to the Multi-AZ DB cluster](../facts/rds.md#rds-multi-az-cluster-read-replica-from-instance)
rds-multi-az-cluster-semisynchronous
  claim: Multi-AZ DB clusters use semisynchronous replication: a change commits once at least one reader DB instance acknowledges it, not all replicas.
  scope: Multi-AZ DB cluster deployment.
  link: [semisynchronous replication](../facts/rds.md#rds-multi-az-cluster-semisynchronous)
  link: [acknowledgment from at least one reader DB instance](../facts/rds.md#rds-multi-az-cluster-semisynchronous)
rds-multi-az-cluster-three-azs-all-read
  claim: A Multi-AZ DB cluster deployment has a writer DB instance and two reader DB instances in three separate Availability Zones of one Region, and all three can serve read traffic.
  scope: Multi-AZ DB cluster deployment, one Region.
  link: [three separate Availability Zones](../facts/rds.md#rds-multi-az-cluster-three-azs-all-read)
  link: [All three DB instances can serve read traffic](../facts/rds.md#rds-multi-az-cluster-three-azs-all-read)
  link: [two reader DB instances](../facts/rds.md#rds-multi-az-cluster-three-azs-all-read)
rds-multi-az-cluster-upgrade-downtime
  claim: A minor version upgrade of a Multi-AZ DB cluster typically has 35 seconds of downtime, which RDS Proxy can reduce to one second or less.
  scope: per Multi-AZ DB cluster; fixed; not adjustable; typical values; an open source proxy can also be used.
  link: [typically 35 seconds](../facts/rds.md#rds-multi-az-cluster-upgrade-downtime)
  link: [one second or less](../facts/rds.md#rds-multi-az-cluster-upgrade-downtime)
  say: about thirty-five seconds | one second or less with RDS Proxy
rds-multi-az-cluster-writer-reader-endpoints
  claim: A Multi-AZ DB cluster has a writer endpoint that connects to the writer DB instance for reads and writes, and a reader endpoint that connects to either reader DB instance for read-only operations.
  scope: Multi-AZ DB cluster deployment.
  link: [writer endpoint](../facts/rds.md#rds-multi-az-cluster-writer-reader-endpoints)
  link: [reader endpoint](../facts/rds.md#rds-multi-az-cluster-writer-reader-endpoints)
  link: [support only read operations](../facts/rds.md#rds-multi-az-cluster-writer-reader-endpoints)
rds-multi-az-cname-flip-retry
  claim: During failover RDS flips the CNAME record of the DB instance to the standby, which is promoted to primary; AWS encourages connection retry logic in the application.
  scope: Multi-AZ DB instance deployments.
  link: [flips the canonical name record (CNAME)](../facts/rds.md#rds-multi-az-cname-flip-retry)
  link: [implement database connection retry at the application layer](../facts/rds.md#rds-multi-az-cname-flip-retry)
rds-multi-az-conversion-best-practice-replica
  claim: As a best practice AWS advises against converting a production DB instance to Multi-AZ in place; instead create a read replica, enable backups on it, convert it to Multi-AZ, load its volumes and promote it to primary.
  scope: production DB instances.
  link: [avoid converting a production DB instance](../facts/rds.md#rds-multi-az-conversion-best-practice-replica)
  link: [then promote it to the primary DB instance](../facts/rds.md#rds-multi-az-conversion-best-practice-replica)
rds-multi-az-conversion-complete-event
  claim: When the modification to Multi-AZ is complete, Amazon RDS emits the event RDS-EVENT-0025.
  scope: Multi-AZ DB instance deployments.
  link: [RDS-EVENT-0025](../facts/rds.md#rds-multi-az-conversion-complete-event)
rds-multi-az-conversion-no-downtime-perf-impact
  claim: Converting a Single-AZ DB instance to Multi-AZ avoids downtime but might impact performance, particularly for write-sensitive workloads, because synchronous replication can increase I/O latency.
  scope: Single-AZ to Multi-AZ DB instance conversion.
  link: [avoids downtime but might impact performance](../facts/rds.md#rds-multi-az-conversion-no-downtime-perf-impact)
  link: [write-sensitive workloads](../facts/rds.md#rds-multi-az-conversion-no-downtime-perf-impact)
rds-multi-az-conversion-snapshot-steps
  claim: When a Single-AZ DB instance is modified to Multi-AZ, RDS takes a snapshot of the primary's EBS volumes, creates the standby's volumes from that snapshot, and turns on synchronous block-level replication.
  scope: Single-AZ to Multi-AZ DB instance conversion.
  link: [Takes a snapshot of the primary DB instance's](../facts/rds.md#rds-multi-az-conversion-snapshot-steps)
  link: [synchronous block-level replication](../facts/rds.md#rds-multi-az-conversion-snapshot-steps)
rds-multi-az-convert-by-modifying
  claim: You can convert an existing DB instance to a Multi-AZ DB instance deployment by modifying the DB instance and specifying the Multi-AZ option.
  scope: Multi-AZ DB instance deployments.
  link: [by modifying the DB instance](../facts/rds.md#rds-multi-az-convert-by-modifying)
  link: [specifying the Multi-AZ option](../facts/rds.md#rds-multi-az-convert-by-modifying)
rds-multi-az-durability-no-restore-needed
  claim: If a primary storage volume fails in a Multi-AZ deployment, RDS fails over to the standby with all updates intact, whereas a Single-AZ deployment needs a user-initiated restore and loses updates after the latest restorable time.
  scope: Multi-AZ DB instance deployments.
  link: [all of your database updates are intact](../facts/rds.md#rds-multi-az-durability-no-restore-needed)
  link: [a user-initiated restore operation would be required](../facts/rds.md#rds-multi-az-durability-no-restore-needed)
rds-multi-az-engine-upgrade-both-down
  claim: An engine version upgrade of a Multi-AZ DB instance modifies the primary and the standby at the same time, so both are unavailable and there is downtime until the upgrade completes.
  scope: Multi-AZ DB instance deployments, engine version upgrades; RDS for SQL Server uses rolling upgrades.
  link: [modifies both primary and secondary DB instances](../facts/rds.md#rds-multi-az-engine-upgrade-both-down)
  link: [causes downtime until the upgrade is complete](../facts/rds.md#rds-multi-az-engine-upgrade-both-down)
rds-multi-az-failover-dns-change-reconnect
  claim: At failover RDS changes the DNS record of the DB instance to point to the standby, so existing connections to the DB instance must be re-established.
  scope: Multi-AZ DB instance deployment.
  link: [changes the Domain Name System (DNS) record](../facts/rds.md#rds-multi-az-failover-dns-change-reconnect)
  link: [re-establish any existing connections](../facts/rds.md#rds-multi-az-failover-dns-change-reconnect)
rds-multi-az-failover-event-subscription
  claim: To know that a Multi-AZ DB instance has failed over, you can set up DB event subscriptions that notify you by email or SMS when a failover starts.
  scope: Multi-AZ DB instance deployments.
  link: [DB event subscriptions](../facts/rds.md#rds-multi-az-failover-event-subscription)
  link: [notify you by email or SMS](../facts/rds.md#rds-multi-az-failover-event-subscription)
rds-multi-az-failover-host-unhealthy
  claim: A Multi-AZ DB instance fails over when the deployment detects an impaired (unhealthy) primary host.
  scope: Multi-AZ DB instance deployment.
  link: [detected an impaired primary DB instance](../facts/rds.md#rds-multi-az-failover-host-unhealthy)
rds-multi-az-failover-network-loss
  claim: A Multi-AZ DB instance fails over when RDS monitoring detects that the primary is unreachable because of a loss of network connectivity.
  scope: Multi-AZ DB instance deployment.
  link: [loss of network connectivity](../facts/rds.md#rds-multi-az-failover-network-loss)
  link: [network reachability failure](../facts/rds.md#rds-multi-az-failover-network-loss)
rds-multi-az-failover-no-admin-intervention
  claim: Amazon RDS handles Multi-AZ failovers automatically, without administrative intervention, and the failover reason can be seen in the event log.
  scope: Multi-AZ DB instance deployment.
  link: [without administrative intervention](../facts/rds.md#rds-multi-az-failover-no-admin-intervention)
  link: [view these failover reasons in the event log](../facts/rds.md#rds-multi-az-failover-no-admin-intervention)
rds-multi-az-failover-on-modification
  claim: A modification of a Multi-AZ DB instance by the customer can trigger a failover.
  scope: Multi-AZ DB instance deployment.
  link: [modification triggered a failover](../facts/rds.md#rds-multi-az-failover-on-modification)
  link: [modified by customer](../facts/rds.md#rds-multi-az-failover-on-modification)
rds-multi-az-failover-on-os-patching
  claim: A Multi-AZ DB instance fails over to the standby when the operating system under the database is patched in an offline operation during the maintenance window.
  scope: Multi-AZ DB instance deployment.
  link: [being patched in an offline operation](../facts/rds.md#rds-multi-az-failover-on-os-patching)
  link: [triggered during the maintenance window](../facts/rds.md#rds-multi-az-failover-on-os-patching)
rds-multi-az-failover-reboot-with-failover
  claim: A Multi-AZ DB instance fails over when the user reboots it and chooses Reboot with failover.
  scope: Multi-AZ DB instance deployment.
  link: [Reboot with failover](../facts/rds.md#rds-multi-az-failover-reboot-with-failover)
  link: [The user requested a failover](../facts/rds.md#rds-multi-az-failover-reboot-with-failover)
rds-multi-az-failover-storage-failure
  claim: A Multi-AZ DB instance fails over when the storage volume under the primary host fails.
  scope: Multi-AZ DB instance deployment.
  link: [detected a storage issue](../facts/rds.md#rds-multi-az-failover-storage-failure)
rds-multi-az-instance-failover-time
  claim: Failover of a Multi-AZ DB instance typically takes 60–120 seconds; large transactions or a lengthy recovery process can increase failover time.
  scope: per Multi-AZ DB instance deployment; fixed; not adjustable; typical value; large transactions or lengthy recovery can make it longer.
  link: [60–120 seconds](../facts/rds.md#rds-multi-az-instance-failover-time)
  say: sixty to one hundred twenty seconds
rds-multi-az-instance-higher-write-latency
  claim: Because of synchronous replication, a Multi-AZ DB instance deployment can have higher write and commit latency than a Single-AZ deployment.
  scope: Multi-AZ DB instance deployment.
  link: [increased write and commit latency](../facts/rds.md#rds-multi-az-instance-higher-write-latency)
  link: [because of the synchronous data replication](../facts/rds.md#rds-multi-az-instance-higher-write-latency)
rds-multi-az-instance-not-read-scaling
  claim: The Multi-AZ DB instance high availability option is not a read scaling solution: the standby replica cannot serve read traffic; for read-only traffic use a Multi-AZ DB cluster or a read replica.
  scope: Multi-AZ DB instance deployment.
  link: [isn't a scaling solution for read-only scenarios](../facts/rds.md#rds-multi-az-instance-not-read-scaling)
  link: [You can't use a standby replica](../facts/rds.md#rds-multi-az-instance-not-read-scaling)
  link: [use a Multi-AZ DB cluster](../facts/rds.md#rds-multi-az-instance-not-read-scaling)
rds-multi-az-instance-protects-az-disruption
  claim: A Multi-AZ DB instance deployment can improve availability during planned maintenance and help protect databases against DB instance failure and Availability Zone disruption.
  scope: Multi-AZ DB instance deployment.
  link: [DB instance failure and Availability Zone disruption](../facts/rds.md#rds-multi-az-instance-protects-az-disruption)
  link: [during planned system maintenance](../facts/rds.md#rds-multi-az-instance-protects-az-disruption)
rds-multi-az-instance-standby-no-reads
  claim: In a Multi-AZ DB instance deployment, RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone, and the standby does not serve read traffic.
  scope: Multi-AZ DB instance deployment.
  link: [synchronous standby replica in a different Availability Zone](../facts/rds.md#rds-multi-az-instance-standby-no-reads)
  link: [doesn't serve read traffic](../facts/rds.md#rds-multi-az-instance-standby-no-reads)
rds-multi-az-instance-synchronous-replication
  claim: In a Multi-AZ DB instance deployment the primary is synchronously replicated across Availability Zones to a standby replica, for data redundancy and to minimize latency spikes during system backups.
  scope: Multi-AZ DB instance deployment.
  link: [synchronously replicated across Availability Zones](../facts/rds.md#rds-multi-az-instance-synchronous-replication)
  link: [minimize latency spikes during system backups](../facts/rds.md#rds-multi-az-instance-synchronous-replication)
rds-multi-az-jvm-dns-ttl-60
  claim: Because DNS entries of AWS resources can change, AWS recommends configuring the JVM with a DNS TTL of no more than 60 seconds so the application picks up the new IP address after a failover.
  scope: Java virtual machine DNS cache (networkaddress.cache.ttl); maximum.
  link: [no more than 60 seconds](../facts/rds.md#rds-multi-az-jvm-dns-ttl-60)
rds-multi-az-manual-failover-reboot
  claim: You can force a Multi-AZ failover manually by rebooting the Multi-AZ DB instance (Reboot with failover).
  scope: Multi-AZ DB instance deployment.
  link: [force a failover manually](../facts/rds.md#rds-multi-az-manual-failover-reboot)
  link: [when you reboot a Multi-AZ DB instance](../facts/rds.md#rds-multi-az-manual-failover-reboot)
rds-multi-az-no-failover-db-operations
  claim: RDS Multi-AZ deployments do not fail over automatically in response to database operations such as long-running queries, deadlocks or database corruption errors.
  scope: Multi-AZ DB instance deployments.
  link: [do not failover automatically](../facts/rds.md#rds-multi-az-no-failover-db-operations)
  link: [long running queries, deadlocks, or database corruption errors](../facts/rds.md#rds-multi-az-no-failover-db-operations)
rds-multi-az-one-vs-two-standbys
  claim: A Multi-AZ DB instance deployment has one standby that provides failover support but serves no read traffic; a Multi-AZ DB cluster deployment has two standbys that provide failover support and can also serve read traffic.
  scope: Multi-AZ DB instance and Multi-AZ DB cluster deployments.
  link: [one standby or two standby DB instances](../facts/rds.md#rds-multi-az-one-vs-two-standbys)
  link: [can also serve read traffic](../facts/rds.md#rds-multi-az-one-vs-two-standbys)
  link: [doesn't serve read traffic](../facts/rds.md#rds-multi-az-one-vs-two-standbys)
rds-multi-az-os-patch-failover-under-minute
  claim: When operating system patches must be applied, a Multi-AZ DB instance needs a short failover to patch the primary, which typically lasts less than a minute.
  scope: Multi-AZ DB instance deployments.
  link: [typically lasts less than a minute](../facts/rds.md#rds-multi-az-os-patch-failover-under-minute)
rds-multi-az-recommend-piops-production
  claim: For production workloads on Multi-AZ, AWS recommends Provisioned IOPS for fast, consistent performance.
  scope: Multi-AZ DB instance deployments.
  link: [we recommend that you use Provisioned IOPS](../facts/rds.md#rds-multi-az-recommend-piops-production)
  link: [fast, consistent performance](../facts/rds.md#rds-multi-az-recommend-piops-production)
rds-multi-az-scaling-standby-first
  claim: For Multi-AZ deployments, DB instance scaling and OS patching are applied first on the standby before an automatic failover, so the availability impact is limited to the failover time.
  scope: Multi-AZ DB instance deployments.
  link: [applied first on the standby](../facts/rds.md#rds-multi-az-scaling-standby-first)
  link: [limited only to the time required](../facts/rds.md#rds-multi-az-scaling-standby-first)
rds-multi-az-sql-server-mirroring-ags
  claim: Multi-AZ for MariaDB, MySQL, Oracle and PostgreSQL uses the Amazon failover technology; Microsoft SQL Server DB instances use SQL Server Database Mirroring or Always On Availability Groups.
  scope: Multi-AZ DB instance deployment, per engine.
  link: [SQL Server Database Mirroring (DBM)](../facts/rds.md#rds-multi-az-sql-server-mirroring-ags)
  link: [Always On Availability Groups (AGs)](../facts/rds.md#rds-multi-az-sql-server-mirroring-ags)
  link: [use the Amazon failover technology](../facts/rds.md#rds-multi-az-sql-server-mirroring-ags)
rds-multi-az-standby-same-region
  claim: RDS automatically provisions a Multi-AZ standby in a different Availability Zone of the same Region as the primary; you cannot select the standby's Availability Zone or alter the number of standbys (one dedicated standby per DB instance primary).
  scope: Multi-AZ DB instance deployments; fixed.
  link: [a different Availability Zone of the same Region](../facts/rds.md#rds-multi-az-standby-same-region)
  link: [one dedicated standby per DB instance primary](../facts/rds.md#rds-multi-az-standby-same-region)
rds-multi-region-async-replica-survives-region
  claim: You can create RDS DB instances in multiple Regions; an instance that replicates asynchronously to a DB instance in another Region keeps a copy available if one Region becomes unavailable.
  scope: cross-Region read replicas.
  link: [replicates asynchronously to a standby DB instance](../facts/rds.md#rds-multi-region-async-replica-survives-region)
  link: [If one Region becomes unavailable](../facts/rds.md#rds-multi-region-async-replica-survives-region)
rds-mysql-delayed-replication-dr
  claim: RDS for MySQL supports delayed replication as a disaster recovery strategy: you set the minimum time, in seconds, that replication from the source to the read replica is delayed.
  scope: RDS for MySQL delayed replication.
  link: [strategy for disaster recovery](../facts/rds.md#rds-mysql-delayed-replication-dr)
rds-on-outposts-hybrid
  claim: You can run Amazon RDS on premises using Amazon RDS on Outposts.
  scope: Amazon RDS on Outposts.
  link: [Amazon RDS on Outposts](../facts/rds.md#rds-on-outposts-hybrid)
rds-optimized-reads-instance-store
  claim: An RDS for MySQL DB instance or Multi-AZ DB cluster that uses RDS Optimized Reads can achieve up to 2x faster query processing; Optimized Reads is turned on by default when the DB instance class has an instance store, such as db.m5d or db.m6gd.
  scope: RDS for MySQL; maximum.
  link: [up to 2x faster query processing](../facts/rds.md#rds-optimized-reads-instance-store)
  link: [turned on by default](../facts/rds.md#rds-optimized-reads-instance-store)
  say: up to two times faster query processing
rds-optimized-writes-mysql
  claim: RDS Optimized Writes for MySQL writes data only once when flushing to durable storage, without the doublewrite buffer, and can give up to two times higher write transaction throughput; it runs on instance classes that use the AWS Nitro System.
  scope: RDS for MySQL; maximum; DB instance classes on the AWS Nitro System.
  link: [up to two times higher write transaction throughput](../facts/rds.md#rds-optimized-writes-mysql)
  link: [without the need for the doublewrite buffer](../facts/rds.md#rds-optimized-writes-mysql)
rds-option-group-default-empty
  claim: RDS gives each new DB instance an empty default option group that cannot be modified or deleted; to apply an option you create or copy an option group, add options and associate it with the instance.
  scope: option groups; default; not adjustable.
  link: [empty default option group](../facts/rds.md#rds-option-group-default-empty)
  link: [can't modify or delete this default option group](../facts/rds.md#rds-option-group-default-empty)
rds-option-groups-features
  claim: RDS uses option groups to enable and configure additional engine features (options) for a DB instance; PostgreSQL does not use option groups and uses extensions and modules instead.
  scope: DB parameter groups and option groups.
  link: [Amazon RDS uses option groups](../facts/rds.md#rds-option-groups-features)
  link: [PostgreSQL does not use options and option groups.](../facts/rds.md#rds-option-groups-features)
rds-oracle-li-byol
  claim: RDS for Oracle has two licensing options, License Included and Bring Your Own License; License Included (AWS holds the license) is supported only for Standard Edition 2, and BYOL for Enterprise Edition and Standard Edition 2.
  scope: RDS for Oracle.
  link: [License Included (LI)](../facts/rds.md#rds-oracle-li-byol)
  link: [Bring Your Own License (BYOL)](../facts/rds.md#rds-oracle-li-byol)
  link: [only supported on Amazon RDS for Oracle Database Standard Edition 2 (SE2)](../facts/rds.md#rds-oracle-li-byol)
rds-oracle-read-replicas-recommend-five
  claim: RDS for Oracle allows up to 15 read replicas per source DB instance in each Region, but AWS recommends limiting replicas to 5 to minimize replication lag.
  scope: per source DB instance, per Region (Oracle); maximum; not adjustable; the recommendation is to minimize replication lag.
  link: [up to 15 read replicas](../facts/rds.md#rds-oracle-read-replicas-recommend-five)
  link: [limiting replicas to 5](../facts/rds.md#rds-oracle-read-replicas-recommend-five)
  say: up to fifteen read replicas | no more than five
rds-other-vpc-access-peering
  claim: When the DB instance is in a different VPC from the EC2 instance that accesses it, you can use VPC peering to reach it.
  scope: access from an EC2 instance in another VPC.
  link: [you can use VPC peering](../facts/rds.md#rds-other-vpc-access-peering)
rds-parameter-group-default-not-modifiable
  claim: A DB instance created without a DB parameter group uses a default one, and the settings of a default parameter group cannot be modified; to change parameters you create a custom parameter group and associate it with the instance.
  scope: DB parameter groups.
  link: [can't modify the parameter settings](../facts/rds.md#rds-parameter-group-default-not-modifiable)
  link: [Create a new parameter group.](../facts/rds.md#rds-parameter-group-default-not-modifiable)
rds-parameter-group-shared-changes
  claim: Updating parameters in a DB parameter group changes them for every DB instance associated with that group.
  scope: DB parameter groups and option groups.
  link: [the changes apply to all DB instances](../facts/rds.md#rds-parameter-group-shared-changes)
rds-parameter-pending-reboot-not-automatic
  claim: A pending-reboot parameter group status does not cause an automatic reboot in the next maintenance window; you must reboot the DB instance manually to apply the changes.
  scope: DB parameter groups.
  link: [doesn't result in an automatic reboot](../facts/rds.md#rds-parameter-pending-reboot-not-automatic)
  link: [manually reboot the DB instance](../facts/rds.md#rds-parameter-pending-reboot-not-automatic)
rds-parameter-static-dynamic
  claim: A changed static parameter takes effect only after you manually reboot the DB instance; a changed dynamic parameter takes effect immediately by default, without a reboot.
  scope: DB instance parameters.
  link: [after you manually reboot the associated DB instances](../facts/rds.md#rds-parameter-static-dynamic)
  link: [takes effect immediately, without requiring a reboot](../facts/rds.md#rds-parameter-static-dynamic)
rds-performance-insights-eol-migrated-database-insights
  claim: The CloudWatch guide says the end-of-life date for Performance Insights was July 31, 2026 and that AWS migrated Performance Insights users to Database Insights; Standard mode keeps flexible 1-24 month retention at the Performance Insights price, and Advanced mode includes 1-24 month retention at no extra cost.
  scope: CloudWatch Database Insights and Performance Insights.
  link: [July 31, 2026](../facts/rds.md#rds-performance-insights-eol-migrated-database-insights)
  link: [migrated Performance Insights users to Database Insights](../facts/rds.md#rds-performance-insights-eol-migrated-database-insights)
  say: July thirty-first, twenty twenty-six
rds-pitr-log-upload-five-minutes
  claim: RDS uploads the transaction logs of DB instances to Amazon S3 every five minutes, which bounds how recent the latest restorable time can be.
  scope: per DB instance with automated backups; fixed; not adjustable.
  link: [every five minutes](../facts/rds.md#rds-pitr-log-upload-five-minutes)
  say: every five minutes
rds-pitr-new-instance-within-retention
  claim: Point-in-time recovery restores to any point in time within the backup retention period and creates a new DB instance without modifying the source DB instance.
  scope: per DB instance with automated backups.
  link: [within your backup retention period](../facts/rds.md#rds-pitr-new-instance-within-retention)
  link: [creating a new DB instance](../facts/rds.md#rds-pitr-new-instance-within-retention)
  say: any point within the backup retention period | it creates a new DB instance
rds-postgresql-delayed-replication-purpose
  claim: RDS for PostgreSQL delayed replication intentionally delays applying data changes from the primary to one or more read replicas, to protect against data corruption, accidental data loss or erroneous transactions.
  scope: RDS for PostgreSQL delayed replication.
  link: [intentionally delay the replication of data changes](../facts/rds.md#rds-postgresql-delayed-replication-purpose)
rds-pricing-cross-az-ec2-transfer-charged
  claim: Data transfer between an Amazon EC2 instance and an RDS DB instance in different Availability Zones of the same Region is charged (standard EC2 Regional data transfer for the EC2 instance); there is no additional charge on the RDS side.
  scope: Amazon RDS billing.
  link: [data transfer charges will apply](../facts/rds.md#rds-pricing-cross-az-ec2-transfer-charged)
rds-pricing-cross-region-automated-backups
  claim: Cross-Region automated backups are charged for the data transferred to copy the snapshot and transaction logs across Regions, plus snapshot storage in the destination Region; storing the transaction logs has no additional charge.
  scope: Amazon RDS billing.
  link: [no additional charge for storage](../facts/rds.md#rds-pricing-cross-region-automated-backups)
rds-pricing-cross-region-snapshot-copy
  claim: A DB snapshot copy to another Region is charged for the data transferred, and the copy is then charged as snapshot storage in the destination Region.
  scope: Amazon RDS billing.
  link: [charged for the data transferred](../facts/rds.md#rds-pricing-cross-region-snapshot-copy)
rds-pricing-dimension-backup-storage
  claim: Backup storage is the storage for automated backups and customer-initiated DB snapshots; a longer backup retention period or more snapshots increases it.
  scope: Amazon RDS billing.
  link: [Increasing your backup retention period](../facts/rds.md#rds-pricing-dimension-backup-storage)
rds-pricing-dimension-data-transfer
  claim: Amazon RDS bills internet data transfer in and out of the DB instance.
  scope: Amazon RDS billing.
  link: [Internet data transfer in and out](../facts/rds.md#rds-pricing-dimension-data-transfer)
rds-pricing-dimension-instance-hours
  claim: Amazon RDS bills DB instance hours based on the type of DB instance you use (for example db.t3.micro or db.m4.large).
  scope: Amazon RDS billing.
  link: [DB instance hours](../facts/rds.md#rds-pricing-dimension-instance-hours)
rds-pricing-dimension-io-requests-magnetic-aurora
  claim: Storage I/O requests per month are a billing dimension only for Amazon RDS magnetic storage and Amazon Aurora.
  scope: Amazon RDS billing.
  link: [magnetic storage and Amazon Aurora only](../facts/rds.md#rds-pricing-dimension-io-requests-magnetic-aurora)
rds-pricing-dimension-storage-gb-month
  claim: Amazon RDS bills storage per GB per month for the storage capacity you provision to the DB instance, prorated if you scale it within the month.
  scope: Amazon RDS billing.
  link: [Storage (per GB per month)](../facts/rds.md#rds-pricing-dimension-storage-gb-month)
rds-pricing-multi-az-about-twice
  claim: Multi-AZ deployments cost more than Single-AZ deployments and can cost approximately twice as much, because of the additional standby instance and its resources.
  scope: Amazon RDS billing.
  link: [approximately twice as much](../facts/rds.md#rds-pricing-multi-az-about-twice)
rds-pricing-on-demand-use-cases
  claim: With On-Demand Instances you pay for compute capacity per hour the DB instance runs, with no long-term commitment; AWS recommends them for short-term, spiky or unpredictable workloads that cannot be interrupted.
  scope: Amazon RDS billing.
  link: [short-term, spiky, or unpredictable workloads](../facts/rds.md#rds-pricing-on-demand-use-cases)
rds-pricing-public-ipv4
  claim: An RDS resource in a VPC with a public IPv4 address incurs the standard public IPv4 address charges.
  scope: Amazon RDS billing.
  link: [standard public IPv4 address charges](../facts/rds.md#rds-pricing-public-ipv4)
rds-pricing-ri-up-to-69-percent
  claim: The RDS pricing page says Reserved Instances can save up to 69% over on-demand rates for steady-state use, with a one- or three-year term.
  scope: Amazon RDS billing.
  link: [save up to 69%](../facts/rds.md#rds-pricing-ri-up-to-69-percent)
  link: [one- or three-year term](../facts/rds.md#rds-pricing-ri-up-to-69-percent)
  say: save up to sixty-nine percent
rds-private-access-vpn-direct-connect
  claim: A DB instance that is in a VPC but isn't publicly accessible can be reached from a private network through an AWS Site-to-Site VPN connection or a Direct Connect connection.
  scope: DB instances in a VPC that are not publicly accessible.
  link: [AWS Site-to-Site VPN connection](../facts/rds.md#rds-private-access-vpn-direct-connect)
  link: [isn't publicly accessible](../facts/rds.md#rds-private-access-vpn-direct-connect)
rds-private-subnet-web-tier-pattern
  claim: A common pattern places web servers in a public subnet and the DB instances in a private subnet so that only the web servers can reach the databases.
  scope: DB instances in a VPC.
  link: [deployed in the private subnet](../facts/rds.md#rds-private-subnet-web-tier-pattern)
  link: [only the web servers have access](../facts/rds.md#rds-private-subnet-web-tier-pattern)
rds-proxy-additional-endpoints
  claim: You can add up to 20 additional proxy endpoints for each proxy, provisioned across the Availability Zones chosen at creation.
  scope: per proxy; maximum; not adjustable.
  link: [up to 20 additional proxy endpoints](../facts/rds-proxy.md#rds-proxy-additional-endpoints)
  say: up to twenty additional endpoints
rds-proxy-blue-green-switchover
  claim: During a Blue/Green Deployments switchover, RDS Proxy redirects connections to the green environment once it becomes production, without DNS propagation delays.
  scope: Amazon RDS Proxy.
  link: [eliminating DNS propagation delays](../facts/rds-proxy.md#rds-proxy-blue-green-switchover)
rds-proxy-borrow-timeout-default
  claim: By default, RDS Proxy waits 120 seconds for a connection in the pool to become available before it returns a timeout error, which also covers a failover in progress.
  scope: per proxy (connection borrow timeout); default; adjustable; applies when the pool is at its maximum or no database instance is available, such as during failover.
  link: [120 seconds](../facts/rds-proxy.md#rds-proxy-borrow-timeout-default)
  say: one hundred twenty seconds
rds-proxy-candidate-no-builtin-pool
  claim: Applications that open and close many database connections and have no built-in connection pooling, and applications that keep many connections open for long periods, are good candidates for RDS Proxy.
  scope: Amazon RDS Proxy.
  link: [don't have built-in connection pooling mechanisms](../facts/rds-proxy.md#rds-proxy-candidate-no-builtin-pool)
  link: [keep a large number of connections open](../facts/rds-proxy.md#rds-proxy-candidate-no-builtin-pool)
rds-proxy-candidate-small-instances
  claim: For DB instances on smaller instance classes such as T2 or T3, a proxy can help avoid out-of-memory conditions and reduce the CPU overhead of establishing connections.
  scope: Amazon RDS Proxy.
  link: [avoid out-of-memory conditions](../facts/rds-proxy.md#rds-proxy-candidate-small-instances)
  link: [such as T2 or T3](../facts/rds-proxy.md#rds-proxy-candidate-small-instances)
rds-proxy-candidate-too-many-connections
  claim: A DB instance that hits 'too many connections' errors is a good candidate for RDS Proxy: applications open many client connections while the proxy keeps a smaller number of long-lived connections to the database.
  scope: Amazon RDS Proxy.
  link: ["too many connections" errors](../facts/rds-proxy.md#rds-proxy-candidate-too-many-connections)
  link: [smaller number of long-lived connections](../facts/rds-proxy.md#rds-proxy-candidate-too-many-connections)
rds-proxy-client-connection-max-life
  claim: RDS Proxy enforces a maximum life of client connections of 24 hours, and this value is not configurable.
  scope: per client connection; maximum; not adjustable.
  link: [24 hours](../facts/rds-proxy.md#rds-proxy-client-connection-max-life)
  say: twenty-four hours
rds-proxy-default-endpoint-two-azs
  claim: Each proxy has a default endpoint provisioned across only two Availability Zones chosen from the proxy's configured subnets.
  scope: default proxy endpoint; fixed; if subnets in more than two AZs are configured, any two are selected.
  link: [only two Availability Zones](../facts/rds-proxy.md#rds-proxy-default-endpoint-two-azs)
rds-proxy-definition-pool-share
  claim: Amazon RDS Proxy lets applications pool and share database connections to improve their ability to scale, and makes them more resilient to database failures by connecting to a standby while preserving application connections.
  scope: Amazon RDS Proxy.
  link: [pool and share database connections](../facts/rds-proxy.md#rds-proxy-definition-pool-share)
  link: [preserving application connections](../facts/rds-proxy.md#rds-proxy-definition-pool-share)
rds-proxy-end-to-end-iam
  claim: RDS Proxy offers standard IAM authentication (IAM to the proxy, Secrets Manager credentials to the database) and end-to-end IAM authentication (IAM from the application to the database through the proxy, with no credentials in Secrets Manager).
  scope: Amazon RDS Proxy.
  link: [End-to-end IAM authentication](../facts/rds-proxy.md#rds-proxy-end-to-end-iam)
  link: [avoids database credential management in Secrets Manager](../facts/rds-proxy.md#rds-proxy-end-to-end-iam)
rds-proxy-endpoint-cross-vpc
  claim: When you create a proxy endpoint you can associate it with a different VPC than the proxy's VPC, so applications in another VPC can connect to the proxy.
  scope: additional proxy endpoints.
  link: [a different virtual private cloud (VPC)](../facts/rds-proxy.md#rds-proxy-endpoint-cross-vpc)
  link: [connect to the proxy from another VPC](../facts/rds-proxy.md#rds-proxy-endpoint-cross-vpc)
rds-proxy-endpoint-privatelink-charges
  claim: Adding a proxy endpoint provisions an AWS PrivateLink interface endpoint, and additional endpoints add charges; the default endpoint cannot be modified.
  scope: proxy endpoints.
  link: [provisions an AWS PrivateLink interface endpoint](../facts/rds-proxy.md#rds-proxy-endpoint-privatelink-charges)
  link: [The RDS proxy default endpoint cannot be modified.](../facts/rds-proxy.md#rds-proxy-endpoint-privatelink-charges)
rds-proxy-engines-not-db2-oracle
  claim: RDS Proxy is available with RDS for MariaDB, MySQL, PostgreSQL and SQL Server (in the listed Regions and engine versions), and isn't available for RDS for Db2 or RDS for Oracle.
  scope: RDS engines (Aurora covered in chapter 27); Region and version availability vary.
  link: [RDS Proxy isn't available for the following engines:](../facts/rds-proxy.md#rds-proxy-engines-not-db2-oracle)
rds-proxy-failover-66-percent
  claim: RDS Proxy bypasses DNS caches to reduce failover times by up to 66% for Amazon RDS Multi-AZ DB instances, and routes traffic to the new database instance while preserving application connections.
  scope: Amazon RDS Multi-AZ DB instances; maximum.
  link: [up to 66%](../facts/rds-proxy.md#rds-proxy-failover-66-percent)
  say: up to sixty-six percent
rds-proxy-failover-idle-connections-kept
  claim: Through RDS Proxy most connections stay alive during a failover; only connections in the middle of a transaction or SQL statement are canceled, and while the writer is unavailable the proxy queues incoming requests.
  scope: Amazon RDS Proxy.
  link: [most connections stay alive during failovers](../facts/rds-proxy.md#rds-proxy-failover-idle-connections-kept)
  link: [RDS Proxy queues up incoming requests](../facts/rds-proxy.md#rds-proxy-failover-idle-connections-kept)
rds-proxy-failover-same-ip-no-dns
  claim: During failovers RDS Proxy keeps accepting connections at the same IP address and directs them to the new primary, so clients are not affected by DNS propagation delays on failover.
  scope: RDS DB instances in a Multi-AZ configuration.
  link: [at the same IP address](../facts/rds-proxy.md#rds-proxy-failover-same-ip-no-dns)
  link: [directs connections to the new primary](../facts/rds-proxy.md#rds-proxy-failover-same-ip-no-dns)
rds-proxy-faq-adds-5-ms-connect-directly
  claim: RDS Proxy can add an average of 5 milliseconds of network latency; an application that cannot tolerate that, or does not need connection management, may connect directly to the database endpoint.
  scope: Amazon RDS Proxy.
  link: [5 milliseconds](../facts/rds-proxy.md#rds-proxy-faq-adds-5-ms-connect-directly)
rds-proxy-faq-bypasses-dns-caches
  claim: RDS Proxy bypasses DNS caches to reduce failover times by up to 66% for RDS and Aurora Multi-AZ databases.
  scope: Amazon RDS Proxy.
  link: [bypasses Domain Name System (DNS) caches](../facts/rds-proxy.md#rds-proxy-faq-bypasses-dns-caches)
  link: [up to 66%](../facts/rds-proxy.md#rds-proxy-faq-bypasses-dns-caches)
rds-proxy-faq-engines
  claim: RDS Proxy is available for Aurora MySQL, Aurora PostgreSQL, RDS for MariaDB, RDS for MySQL, RDS for PostgreSQL and RDS for SQL Server.
  scope: Amazon RDS Proxy.
  link: [Amazon RDS for SQL Server](../facts/rds-proxy.md#rds-proxy-faq-engines)
rds-proxy-faq-failover-retries-possible
  claim: During database failovers behind RDS Proxy, the application may see increased latency and ongoing transactions may have to be retried.
  scope: Amazon RDS Proxy.
  link: [ongoing transactions may have to be retried](../facts/rds-proxy.md#rds-proxy-faq-failover-retries-possible)
rds-proxy-faq-iam-end-to-end
  claim: RDS Proxy can use IAM authentication for client-to-proxy connections only, with Secrets Manager for proxy-to-database, or IAM for both legs, which removes the need to store database passwords in Secrets Manager.
  scope: Amazon RDS Proxy.
  link: [both client-to-proxy and proxy-to-database connections](../facts/rds-proxy.md#rds-proxy-faq-iam-end-to-end)
rds-proxy-faq-lambda-iam-execution-role
  claim: With RDS Proxy, a Lambda function no longer handles database credentials in code: it can authenticate to RDS Proxy and the database with its IAM execution role.
  scope: Amazon RDS Proxy.
  link: [IAM execution role](../facts/rds-proxy.md#rds-proxy-faq-lambda-iam-execution-role)
rds-proxy-faq-no-code-changes
  claim: RDS Proxy needs no additional infrastructure to provision or manage and can be enabled for most applications with no code changes.
  scope: Amazon RDS Proxy.
  link: [no code changes](../facts/rds-proxy.md#rds-proxy-faq-no-code-changes)
rds-proxy-faq-scales-automatically
  claim: RDS Proxy is fully managed and scales its capacity automatically with application demand.
  scope: Amazon RDS Proxy.
  link: [scales its capacity automatically](../facts/rds-proxy.md#rds-proxy-faq-scales-automatically)
rds-proxy-faq-secrets-manager-credentials
  claim: RDS Proxy lets you manage database credentials centrally in AWS Secrets Manager.
  scope: Amazon RDS Proxy.
  link: [AWS Secrets Manager](../facts/rds-proxy.md#rds-proxy-faq-secrets-manager-credentials)
rds-proxy-faq-use-case-idle-connections
  claim: Instead of overprovisioning a database for mostly idle connections, RDS Proxy can hold the idle connections and open database connections only as needed.
  scope: Amazon RDS Proxy.
  link: [hold idling connections](../facts/rds-proxy.md#rds-proxy-faq-use-case-idle-connections)
rds-proxy-faq-use-case-open-close
  claim: Applications that open and close database connections often, such as serverless, PHP or Ruby on Rails apps, benefit from the connection pool that RDS Proxy keeps.
  scope: Amazon RDS Proxy.
  link: [Serverless, PHP, or Ruby on Rails](../facts/rds-proxy.md#rds-proxy-faq-use-case-open-close)
rds-proxy-faq-use-case-unpredictable
  claim: For unpredictable workloads, RDS Proxy lets many application connections share a database connection and regulates the number of database connections opened.
  scope: Amazon RDS Proxy.
  link: [share a database connection](../facts/rds-proxy.md#rds-proxy-faq-use-case-unpredictable)
rds-proxy-faq-vpc-subnets
  claim: When you enable RDS Proxy, you specify the VPC and subnets from which the proxy can be accessed.
  scope: Amazon RDS Proxy.
  link: [specify the VPC and subnets](../facts/rds-proxy.md#rds-proxy-faq-vpc-subnets)
rds-proxy-faq-what
  claim: Amazon RDS Proxy is a fully managed, highly available database proxy that makes applications more scalable, more resilient to database failures and more secure.
  scope: Amazon RDS Proxy.
  link: [fully managed, highly available database proxy](../facts/rds-proxy.md#rds-proxy-faq-what)
rds-proxy-faq-why-pooling-failover-iam
  claim: RDS Proxy pools and shares database connections, reduces failover times by up to 66% while preserving application connections, and can enforce IAM authentication with credentials stored in Secrets Manager.
  scope: Amazon RDS Proxy.
  link: [pooling and sharing database connections](../facts/rds-proxy.md#rds-proxy-faq-why-pooling-failover-iam)
  link: [up to 66%](../facts/rds-proxy.md#rds-proxy-faq-why-pooling-failover-iam)
rds-proxy-ha-serverless-infrastructure
  claim: RDS Proxy infrastructure is highly available across multiple Availability Zones, its compute, memory and storage are independent of the DB instance, and its compute is serverless, scaling automatically with the workload.
  scope: Amazon RDS Proxy.
  link: [highly available and deployed over multiple Availability Zones](../facts/rds-proxy.md#rds-proxy-ha-serverless-infrastructure)
  link: [independent of your RDS DB instance](../facts/rds-proxy.md#rds-proxy-ha-serverless-infrastructure)
  link: [The RDS Proxy compute resources are serverless](../facts/rds-proxy.md#rds-proxy-ha-serverless-infrastructure)
rds-proxy-iam-and-secrets-auth
  claim: With RDS Proxy you can enforce IAM authentication for clients connecting to the proxy, and the proxy connects to the database with either IAM database authentication or credentials stored in AWS Secrets Manager.
  scope: Amazon RDS Proxy.
  link: [enforce AWS Identity and Access Management (IAM) authentication](../facts/rds-proxy.md#rds-proxy-iam-and-secrets-auth)
  link: [credentials stored in AWS Secrets Manager](../facts/rds-proxy.md#rds-proxy-iam-and-secrets-auth)
rds-proxy-idle-client-timeout-default
  claim: By default, RDS Proxy closes a client connection that has been idle for 1,800 seconds (30 minutes); the setting is adjustable.
  scope: per proxy (IdleClientTimeout); default; adjustable; the database connection stays open and returns to the pool.
  link: [1,800 seconds (30 minutes)](../facts/rds-proxy.md#rds-proxy-idle-client-timeout-default)
  say: thirty minutes
rds-proxy-lambda-connection-pooling
  claim: AWS Lambda functions are good candidates for RDS Proxy because they make frequent short database connections that benefit from its connection pooling, and they can use IAM authentication instead of database credentials in the function code.
  scope: Amazon RDS Proxy.
  link: [connection pooling offered by RDS Proxy](../facts/rds-proxy.md#rds-proxy-lambda-connection-pooling)
  link: [frequent short database connections](../facts/rds-proxy.md#rds-proxy-lambda-connection-pooling)
rds-proxy-lambda-console-connect
  claim: When you connect a Lambda function to a DB instance in the RDS console, you can route the connection through RDS Proxy; RDS then configures the VPC security groups for the function, the DB instance and the proxy.
  scope: Amazon RDS Proxy.
  link: [configures the VPC security group for the proxy](../facts/rds-proxy.md#rds-proxy-lambda-console-connect)
rds-proxy-max-connections-percent
  claim: MaxConnectionsPercent limits the connections RDS Proxy can open to the database as a percentage of the database's maximum connections, so the pool size follows the database configuration when you resize the instance.
  scope: RDS Proxy target group setting.
  link: [limits the number of connections](../facts/rds-proxy.md#rds-proxy-max-connections-percent)
  link: [as a percentage of the maximum](../facts/rds-proxy.md#rds-proxy-max-connections-percent)
rds-proxy-max-connections-percent-example
  claim: MaxConnectionsPercent caps proxy connections as a percentage of the database's max_connections: with max_connections 1000 and MaxConnectionsPercent 95, the limit is 950 connections.
  scope: per proxy target group; maximum; AWS recommends at least 30% headroom above recent maximum usage.
  link: [950 connections](../facts/rds-proxy.md#rds-proxy-max-connections-percent-example)
  say: nine hundred fifty connections
rds-proxy-multi-az-cluster-minor-upgrade-downtime
  claim: RDS Proxy can be used with Multi-AZ DB clusters and can reduce the downtime of a minor version upgrade of a Multi-AZ DB cluster to one second or less.
  scope: minor version upgrade of a Multi-AZ DB cluster; maximum; with RDS Proxy.
  link: [one second or less](../facts/rds-proxy.md#rds-proxy-multi-az-cluster-minor-upgrade-downtime)
rds-proxy-multi-user-fragments-pool
  claim: Back-end connections are reused only for clients with the same database user name, so many unique database accounts (for example one per tenant) fragment the pool into micro-pools and reduce RDS Proxy's efficiency.
  scope: Amazon RDS Proxy.
  link: [user-specific micro-pools](../facts/rds-proxy.md#rds-proxy-multi-user-fragments-pool)
  link: [multi-user environments](../facts/rds-proxy.md#rds-proxy-multi-user-fragments-pool)
rds-proxy-multiplexing-default
  claim: By default RDS Proxy can reuse a connection after each transaction in a session (multiplexing); taking a connection from the pool to reuse it is called borrowing.
  scope: RDS Proxy connections; default; not adjustable.
  link: [This transaction-level reuse is called *multiplexing*.](../facts/rds-proxy.md#rds-proxy-multiplexing-default)
  link: [*borrowing* the connection](../facts/rds-proxy.md#rds-proxy-multiplexing-default)
rds-proxy-multiplexing-fewer-db-connections
  claim: With multiplexing, many simultaneous client connections to the proxy share a smaller number of connections to the DB instance, which reduces memory overhead and the chance of 'too many connections' errors.
  scope: Amazon RDS Proxy.
  link: [keeps a smaller number of connections open](../facts/rds-proxy.md#rds-proxy-multiplexing-fewer-db-connections)
  link: [reduces the chance of "too many connections" errors](../facts/rds-proxy.md#rds-proxy-multiplexing-fewer-db-connections)
rds-proxy-no-code-changes
  claim: RDS Proxy is fully compatible with the engine versions it supports, and most applications can use it with no code changes.
  scope: Amazon RDS Proxy; the application connects to the proxy endpoint.
  link: [with no code changes](../facts/rds-proxy.md#rds-proxy-no-code-changes)
rds-proxy-not-rds-custom-sqlserver
  claim: You cannot use RDS Proxy with RDS Custom for SQL Server, or with a VPC whose tenancy is set to dedicated.
  scope: Amazon RDS Proxy.
  link: [with RDS Custom for SQL Server](../facts/rds-proxy.md#rds-proxy-not-rds-custom-sqlserver)
  link: [tenancy set to `dedicated`](../facts/rds-proxy.md#rds-proxy-not-rds-custom-sqlserver)
rds-proxy-pinned-until-session-ends
  claim: When a connection is pinned, each later transaction uses the same database connection until the session ends, and no other client connection can reuse that database connection meanwhile.
  scope: Amazon RDS Proxy.
  link: [until the session ends](../facts/rds-proxy.md#rds-proxy-pinned-until-session-ends)
rds-proxy-pinning-definition
  claim: When RDS Proxy cannot be sure that reusing a connection outside the current session is safe, it keeps the session on the same connection until the session ends; this is called pinning.
  scope: Amazon RDS Proxy.
  link: [This fallback behavior is called *pinning*.](../facts/rds-proxy.md#rds-proxy-pinning-definition)
  link: [keeps the session on the same connection](../facts/rds-proxy.md#rds-proxy-pinning-definition)
rds-proxy-pinning-minimize-init-query
  claim: To minimize pinning, set variables consistently across connections, move identical SET statements into the proxy's initialization query, and watch the CloudWatch metric DatabaseConnectionsCurrentlySessionPinned; for PostgreSQL, setting a variable leads to session pinning.
  scope: Amazon RDS Proxy.
  link: [DatabaseConnectionsCurrentlySessionPinned](../facts/rds-proxy.md#rds-proxy-pinning-minimize-init-query)
  link: [setting a variable leads to session pinning](../facts/rds-proxy.md#rds-proxy-pinning-minimize-init-query)
rds-proxy-pinning-one-to-one
  claim: Pinning creates an exclusive one-to-one association between a client-proxy connection and a proxy-database connection, so avoiding it matters whenever RDS Proxy is used mainly for scalability and efficiency.
  scope: Amazon RDS Proxy.
  link: [exclusive 1:1 association](../facts/rds-proxy.md#rds-proxy-pinning-one-to-one)
rds-proxy-pinning-reduces-reuse
  claim: RDS Proxy pins a client connection to one database connection when it detects a session state change that is not appropriate for other sessions, such as changing a session variable; pinning reduces the effectiveness of connection reuse.
  scope: Amazon RDS Proxy.
  link: [Pinning reduces the effectiveness of connection reuse.](../facts/rds-proxy.md#rds-proxy-pinning-reduces-reuse)
  link: [session state change](../facts/rds-proxy.md#rds-proxy-pinning-reduces-reuse)
rds-proxy-pinning-statement-size
  claim: Any statement with a text size greater than 16 KB causes RDS Proxy to pin the session to the current connection.
  scope: per client session; maximum; not adjustable.
  link: [greater than 16 KB](../facts/rds-proxy.md#rds-proxy-pinning-statement-size)
  say: larger than sixteen kilobytes
rds-proxy-pricing-endpoints
  claim: The default endpoint of an RDS Proxy has no additional charge; each extra proxy endpoint provisions an AWS PrivateLink interface endpoint, which has its own charges.
  scope: Amazon RDS Proxy.
  link: [no additional charges associated with the default endpoint](../facts/rds-proxy.md#rds-proxy-pricing-endpoints)
rds-proxy-pricing-per-vcpu
  claim: For provisioned instances, RDS Proxy is priced per vCPU per hour of the underlying database; partial hours are billed in 1-second increments, with a 10-minute minimum charge following a billable status change such as creating, starting, or modifying.
  scope: per proxy; Aurora Serverless is priced per ACU per hour instead; the default proxy endpoint has no extra charge, additional endpoints incur PrivateLink charges.
  link: [priced per vCPU per hour](../facts/rds-proxy.md#rds-proxy-pricing-per-vcpu)
  link: [a 10-minute minimum charge](../facts/rds-proxy.md#rds-proxy-pricing-per-vcpu)
  say: per vCPU of the database per hour | ten-minute minimum
rds-proxy-quota-proxies
  claim: The default quota for RDS proxies is 20 per account in each Region, and it is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [20](../facts/rds-proxy.md#rds-proxy-quota-proxies)
  say: twenty
rds-proxy-read-only-endpoint-clusters
  claim: By default, the RDS Proxy endpoint for a Multi-AZ DB cluster has read/write capability and sends all requests to the writer instance of the cluster; if the proxy is associated with a Multi-AZ DB cluster, you can create additional read/write or read-only endpoints for that proxy.
  scope: RDS Proxy with Multi-AZ DB clusters; the proxy is associated with a Multi-AZ DB cluster.
  link: [additional read/write or read-only endpoints](../facts/rds-proxy.md#rds-proxy-read-only-endpoint-clusters)
  link: [sends all requests to the writer instance](../facts/rds-proxy.md#rds-proxy-read-only-endpoint-clusters)
rds-proxy-same-vpc-not-public
  claim: RDS Proxy must be in the same VPC as the database and cannot be publicly accessible, even if the database is.
  scope: Amazon RDS Proxy.
  link: [The proxy can't be publicly accessible](../facts/rds-proxy.md#rds-proxy-same-vpc-not-public)
  link: [same virtual private cloud (VPC) as the database](../facts/rds-proxy.md#rds-proxy-same-vpc-not-public)
  link: [be publicly accessible](../facts/rds-proxy.md#rds-proxy-same-vpc-not-public)
rds-proxy-secrets-per-proxy
  claim: Each proxy can have up to 200 associated Secrets Manager secrets, which limits it to up to 200 different user accounts when using secrets.
  scope: per proxy; maximum; not adjustable; when authenticating with secrets.
  link: [up to 200 associated Secrets Manager secrets](../facts/rds-proxy.md#rds-proxy-secrets-per-proxy)
  say: up to two hundred secrets
rds-proxy-single-target-many-proxies
  claim: Each proxy can be associated with a single target DB instance, but several proxies can be associated with the same DB instance.
  scope: per proxy.
  link: [associated with a single target DB instance](../facts/rds-proxy.md#rds-proxy-single-target-many-proxies)
  link: [associate multiple proxies with the same DB instance](../facts/rds-proxy.md#rds-proxy-single-target-many-proxies)
rds-proxy-surges-queue-throttle
  claim: RDS Proxy queues or throttles application connections that cannot be served at once from the pool, so latency may rise but the application keeps scaling; requests beyond your limits are rejected (load shedding).
  scope: Amazon RDS Proxy.
  link: [queues or throttles application connections](../facts/rds-proxy.md#rds-proxy-surges-queue-throttle)
  link: [it sheds load](../facts/rds-proxy.md#rds-proxy-surges-queue-throttle)
rds-proxy-tls-acm-no-cert-download
  claim: RDS Proxy uses certificates from AWS Certificate Manager (ACM), so applications that connect through it don't need to download Amazon RDS certificates; you can connect to the proxy using a higher version of TLS than you use in the underlying database.
  scope: Amazon RDS Proxy.
  link: [AWS Certificate Manager (ACM)](../facts/rds-proxy.md#rds-proxy-tls-acm-no-cert-download)
  link: [don't need to download Amazon RDS certificates](../facts/rds-proxy.md#rds-proxy-tls-acm-no-cert-download)
rds-proxy-vpc-two-subnets-two-azs
  claim: RDS Proxy needs a VPC shared with the DB instance that has at least two subnets in different Availability Zones; client applications such as EC2, Lambda or ECS can be in the proxy's VPC or in another VPC.
  scope: RDS Proxy VPC; minimum.
  link: [a minimum of two subnets](../facts/rds-proxy.md#rds-proxy-vpc-two-subnets-two-azs)
  link: [in different Availability Zones](../facts/rds-proxy.md#rds-proxy-vpc-two-subnets-two-azs)
rds-proxy-writer-only-not-replica
  claim: For RDS DB instances in replication configurations, a proxy can be associated only with the writer DB instance, not with a read replica.
  scope: RDS DB instances (not Aurora).
  link: [only with the writer DB instance](../facts/rds-proxy.md#rds-proxy-writer-only-not-replica)
rds-public-access-option
  claim: A DB instance in a VPC always has a private IP address; the Public access option decides whether it also gets a public IP address, and public access still needs security group inbound rules and an internet gateway on the DB subnet group's subnets.
  scope: DB instances in a VPC.
  link: [**Public access** option](../facts/rds.md#rds-public-access-option)
  link: [must have an internet gateway](../facts/rds.md#rds-public-access-option)
rds-quota-concurrent-cross-region-replica-requests
  claim: By default an account can have 20 concurrent cross-Region read replica requests and 20 concurrent snapshot copy requests in each Region.
  scope: per account, per Region; default; adjustable; concurrent requests, not the total number of replicas or copies.
  link: [20 for each Region](../facts/rds.md#rds-quota-concurrent-cross-region-replica-requests)
  say: twenty per Region
rds-quota-cross-region-automated-backups
  claim: The default quota for cross-Region automated backups is 20 for an AWS account.
  scope: per account; default; adjustable.
  link: [20 for an AWS account](../facts/rds.md#rds-quota-cross-region-automated-backups)
  say: twenty per account
rds-quota-db-instances
  claim: The default quota for DB instances is 40 per account in each Region (20 in ap-south-1), and the quota is adjustable.
  scope: per account, per Region; default; adjustable; ap-south-1 has a default of 20.
  link: [40](../facts/rds.md#rds-quota-db-instances)
  link: [ap-south-1: 20](../facts/rds.md#rds-quota-db-instances)
  say: forty | twenty in ap-south-1
rds-quota-db-subnet-groups
  claim: The default quota for DB subnet groups is 50 per account in each Region (20 in ap-south-1), and it is adjustable.
  scope: per account, per Region; default; adjustable; ap-south-1 has a default of 20.
  link: [50](../facts/rds.md#rds-quota-db-subnet-groups)
  say: fifty
rds-quota-event-subscriptions
  claim: The default quota for RDS event subscriptions is 20 per account in each Region, and it is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [20](../facts/rds.md#rds-quota-event-subscriptions)
  say: twenty
rds-quota-iam-roles-per-db-instance
  claim: The default quota for IAM roles associated with one DB instance is 5, and it is adjustable.
  scope: per DB instance; default; adjustable.
  link: [5](../facts/rds.md#rds-quota-iam-roles-per-db-instance)
  say: five
rds-quota-license-included-instances
  claim: Within the default total of 40 DB instances, license-included SQL Server is limited to 10 DB instances for each edition (Enterprise, Standard, Web and Express).
  scope: per account, per Region; default; adjustable; license-included model; the page also lists 10 for license-included Oracle and 40 for MySQL, MariaDB and PostgreSQL.
  link: [10 for each SQL Server edition](../facts/rds.md#rds-quota-license-included-instances)
  say: ten for each SQL Server edition
rds-quota-manual-db-instance-snapshots
  claim: The default quota for manual DB instance snapshots is 100 per account in each Region, and it is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [100](../facts/rds.md#rds-quota-manual-db-instance-snapshots)
  say: one hundred
rds-quota-option-groups
  claim: The default quota for option groups is 20 per account in each Region, and it is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [20](../facts/rds.md#rds-quota-option-groups)
  say: twenty
rds-quota-parameter-groups
  claim: The default quota for DB parameter groups is 50 per account in each Region (20 in ap-south-1), and it is adjustable.
  scope: per account, per Region; default; adjustable; ap-south-1 has a default of 20.
  link: [50](../facts/rds.md#rds-quota-parameter-groups)
  say: fifty
rds-quota-read-replicas-per-primary
  claim: The default quota for read replicas per primary DB instance is 15 in each Region; it is adjustable for Amazon RDS but cannot be adjusted for Amazon Aurora.
  scope: per primary DB instance, per Region; default; adjustable; the table says the quota cannot be adjusted for Amazon Aurora.
  link: [15](../facts/rds.md#rds-quota-read-replicas-per-primary)
  say: fifteen
rds-quota-reserved-db-instances
  claim: The default quota for reserved DB instances is 40 per account in each Region (20 in ap-south-1), and it is adjustable.
  scope: per account, per Region; default; adjustable; ap-south-1 has a default of 20.
  link: [40](../facts/rds.md#rds-quota-reserved-db-instances)
  say: forty
rds-quota-subnets-per-db-subnet-group
  claim: A DB subnet group can hold at most 20 subnets, and this quota is not adjustable.
  scope: per DB subnet group; maximum; not adjustable.
  link: [20](../facts/rds.md#rds-quota-subnets-per-db-subnet-group)
  say: twenty
rds-quota-total-storage
  claim: The default quota for total storage of all RDS DB instances added together is 100,000 GB per account in each Region; it is adjustable and does not apply to Amazon Aurora.
  scope: per account, per Region, all DB instances added together; default; adjustable; measured in GB on EBS volumes; does not apply to Amazon Aurora.
  link: [100,000](../facts/rds.md#rds-quota-total-storage)
  say: one hundred thousand gigabytes
rds-read-replica-all-databases
  claim: Applications connect to a read replica like to any DB instance, and RDS replicates all databases from the source DB instance.
  scope: RDS DB instance read replicas.
  link: [replicates all databases from the source](../facts/rds.md#rds-read-replica-all-databases)
rds-read-replica-async-read-only
  claim: Amazon RDS copies updates from the primary DB instance to a read replica asynchronously; clients have read/write access to the primary and read-only access to the replica.
  scope: RDS DB instance read replicas.
  link: [read-only access to the replica](../facts/rds.md#rds-read-replica-async-read-only)
  link: [copies them asynchronously to the read replica](../facts/rds.md#rds-read-replica-async-read-only)
rds-read-replica-billing
  claim: Read replicas are billed as standard DB instances at the same rates as their DB instance class; replication data transfer between source and replica within the same Region is not charged.
  scope: read replicas; data transfer is free only within the same AWS Region.
  link: [billed as standard DB instances](../facts/rds.md#rds-read-replica-billing)
  link: [aren't charged for the data transfer](../facts/rds.md#rds-read-replica-billing)
rds-read-replica-can-be-multi-az
  claim: You can create a read replica with its own standby in another Availability Zone (a Multi-AZ read replica), independently of whether the source is Multi-AZ.
  scope: RDS DB instance read replicas.
  link: [create a standby of your replica](../facts/rds.md#rds-read-replica-can-be-multi-az)
  link: [independent of whether the source database](../facts/rds.md#rds-read-replica-can-be-multi-az)
rds-read-replica-cascading-engines
  claim: For RDS for MariaDB, RDS for MySQL and certain versions of RDS for PostgreSQL you can create a read replica from an existing read replica; for RDS for Db2, Oracle and SQL Server you cannot.
  scope: per engine; PostgreSQL: certain versions only.
  link: [from an existing read replica](../facts/rds.md#rds-read-replica-cascading-engines)
  link: [For RDS for Db2, RDS for Oracle, and RDS for SQL Server](../facts/rds.md#rds-read-replica-cascading-engines)
rds-read-replica-create-io-suspension
  claim: Creating a read replica causes a very brief I/O suspension (typically about one second) on the source when the snapshot begins; a Multi-AZ source avoids it because the snapshot is taken from the secondary.
  scope: source DB instance when a read replica is created; avoided when the source is a Multi-AZ deployment.
  link: [about one second](../facts/rds.md#rds-read-replica-create-io-suspension)
  link: [snapshot is taken from the secondary DB instance](../facts/rds.md#rds-read-replica-create-io-suspension)
rds-read-replica-created-from-snapshot
  claim: When you create a read replica, RDS takes a snapshot of the source instance, creates a read-only instance from it, and then updates it with the engine's asynchronous replication whenever the primary changes.
  scope: RDS DB instance read replicas.
  link: [takes a snapshot of the source instance](../facts/rds.md#rds-read-replica-created-from-snapshot)
  link: [asynchronous replication method](../facts/rds.md#rds-read-replica-created-from-snapshot)
rds-read-replica-cross-region-secure-channel
  claim: For a read replica in a different AWS Region, RDS sets up a secure communications channel between the primary and the replica, including the needed security group entries.
  scope: cross-Region read replicas.
  link: [secure communications channel](../facts/rds.md#rds-read-replica-cross-region-secure-channel)
  link: [different AWS Region](../facts/rds.md#rds-read-replica-cross-region-secure-channel)
rds-read-replica-definition
  claim: A read replica is a read-only copy of a DB instance; routing queries to it reduces the load on the primary and lets read-heavy workloads scale out beyond one DB instance.
  scope: RDS DB instance read replicas.
  link: [read-only copy of a DB instance](../facts/rds.md#rds-read-replica-definition)
  link: [read-heavy database workloads](../facts/rds.md#rds-read-replica-definition)
rds-read-replica-encrypted-needs-encrypted-source
  claim: To create an encrypted read replica, the source DB instance must be encrypted.
  scope: RDS DB instance read replicas.
  link: [The source DB instance must be encrypted](../facts/rds.md#rds-read-replica-encrypted-needs-encrypted-source)
rds-read-replica-no-autoscaling
  claim: You must create RDS read replicas manually; RDS does not support autoscaling of read replicas (adding or removing replicas as read demand changes).
  scope: RDS DB instance read replicas.
  link: [You must manually create read replicas](../facts/rds.md#rds-read-replica-no-autoscaling)
  link: [doesn't support autoscaling of read replicas](../facts/rds.md#rds-read-replica-no-autoscaling)
rds-read-replica-no-circular-replication
  claim: Amazon RDS does not support circular replication: a DB instance cannot be configured as a replication source for an existing DB instance; a read replica can only be created new from an existing DB instance.
  scope: RDS DB instance read replicas.
  link: [doesn't support circular replication](../facts/rds.md#rds-read-replica-no-circular-replication)
rds-read-replica-no-direct-cross-account
  claim: There is no direct way to create a read replica in another AWS account using the console or AWS CLI.
  scope: console and AWS CLI.
  link: [read replica in another AWS account](../facts/rds.md#rds-read-replica-no-direct-cross-account)
rds-read-replica-promote-ddl-mysql-mariadb
  claim: For MySQL and MariaDB, slow DDL operations such as building indexes can be done on a read replica that is in sync, which is then promoted and used by the applications.
  scope: RDS for MySQL and RDS for MariaDB.
  link: [on a MySQL or MariaDB read replica](../facts/rds.md#rds-read-replica-promote-ddl-mysql-mariadb)
  link: [promote the read replica](../facts/rds.md#rds-read-replica-promote-ddl-mysql-mariadb)
rds-read-replica-promote-not-replication-target
  claim: A promoted read replica is a standalone DB instance: it keeps its option group and parameter group, can have its own read replicas and point-in-time restores, and can no longer be a replication target.
  scope: promoted read replica.
  link: [it is no longer a read replica](../facts/rds.md#rds-read-replica-promote-not-replication-target)
  link: [retains the option group and the parameter group](../facts/rds.md#rds-read-replica-promote-not-replication-target)
rds-read-replica-promote-reboot-minutes
  claim: When you promote a read replica, RDS stops replication and reboots the replica before making it available; the promotion can take several minutes or longer depending on the replica's size.
  scope: RDS DB instance read replicas.
  link: [RDS stops replication and reboots the read replica](../facts/rds.md#rds-read-replica-promote-reboot-minutes)
  link: [several minutes or longer](../facts/rds.md#rds-read-replica-promote-reboot-minutes)
rds-read-replica-promote-recovery-steps
  claim: Read replica promotion can be a data recovery scheme if the primary fails, complementing synchronous replication and automatic failover; it carries the limitations of asynchronous replication.
  scope: RDS DB instance read replicas.
  link: [data recovery scheme](../facts/rds.md#rds-read-replica-promote-recovery-steps)
  link: [limitations of asynchronous replication](../facts/rds.md#rds-read-replica-promote-recovery-steps)
rds-read-replica-promote-sharding
  claim: For sharding, you can create read replicas for each shard and promote them when you convert them into standalone shards.
  scope: RDS DB instance read replicas.
  link: [convert them into standalone shards](../facts/rds.md#rds-read-replica-promote-sharding)
  link: [corresponding to each of your shards](../facts/rds.md#rds-read-replica-promote-sharding)
rds-read-replica-promote-standalone
  claim: You can promote a read replica into a standalone DB instance; promoting one replica has no effect on the other replicas of the same source.
  scope: RDS DB instance read replicas.
  link: [has no effect on the other replicas](../facts/rds.md#rds-read-replica-promote-standalone)
  link: [into a standalone DB instance](../facts/rds.md#rds-read-replica-promote-standalone)
rds-read-replica-read-only-connections
  claim: A read replica allows only read-only connections; the exceptions are RDS for Db2 and RDS for Oracle, whose standby and mounted replicas accept no user connections and are mainly for cross-Region disaster recovery.
  scope: DB instance read replicas.
  link: [allows only read-only connections](../facts/rds.md#rds-read-replica-read-only-connections)
  link: [don't accept user connections](../facts/rds.md#rds-read-replica-read-only-connections)
rds-read-replica-requires-automated-backups
  claim: Before you create a read replica you must enable automatic backups on the source DB instance by setting a backup retention period other than 0; this also applies to a read replica that is the source for another read replica.
  scope: source DB instance of a read replica.
  link: [a value other than 0](../facts/rds.md#rds-read-replica-requires-automated-backups)
  link: [enable automatic backups on the source DB instance](../facts/rds.md#rds-read-replica-requires-automated-backups)
rds-read-replica-same-vpc-recommended
  claim: Within a Region, AWS strongly recommends creating read replicas in the same VPC as the source DB instance, because a different VPC can cause CIDR overlap that makes the replica unstable.
  scope: read replicas within one AWS Region.
  link: [in the same virtual private cloud (VPC)](../facts/rds.md#rds-read-replica-same-vpc-recommended)
  link: [CIDR overlap makes the replica unstable](../facts/rds.md#rds-read-replica-same-vpc-recommended)
rds-read-replica-size-same-or-larger
  claim: AWS recommends using the same or a larger DB instance class and storage type for a read replica as for its source DB instance.
  scope: RDS DB instance read replicas.
  link: [same or larger DB instance class](../facts/rds.md#rds-read-replica-size-same-or-larger)
rds-read-replica-source-delete-promotes
  claim: If you delete a source DB instance without deleting its read replicas in the same Region, each replica is promoted to a standalone DB instance.
  scope: read replicas in the same AWS Region as the source.
  link: [promoted to a standalone DB instance](../facts/rds.md#rds-read-replica-source-delete-promotes)
rds-read-replica-storage-type-default
  claim: By default a read replica is created with the same storage type as the source DB instance, but you can create it with a different storage type within the options AWS lists.
  scope: read replica storage type; default; adjustable.
  link: [same storage type as the source DB instance](../facts/rds.md#rds-read-replica-storage-type-default)
  link: [different storage type](../facts/rds.md#rds-read-replica-storage-type-default)
rds-read-replica-use-disaster-recovery
  claim: A read replica can be promoted to a standalone instance as a disaster recovery solution if the primary DB instance fails.
  scope: RDS DB instance read replicas.
  link: [promote a read replica to a standalone instance](../facts/rds.md#rds-read-replica-use-disaster-recovery)
  link: [Implementing disaster recovery](../facts/rds.md#rds-read-replica-use-disaster-recovery)
rds-read-replica-use-reporting
  claim: A use case for read replicas is to run business reporting or data warehousing queries against the replica instead of the production DB instance.
  scope: RDS DB instance read replicas.
  link: [Business reporting or data warehousing scenarios](../facts/rds.md#rds-read-replica-use-reporting)
rds-read-replica-use-source-unavailable
  claim: Read replicas can serve read traffic while the source DB instance is unavailable (for example during backup I/O suspension or maintenance), but the replica's data might be stale.
  scope: RDS DB instance read replicas.
  link: [might be stale](../facts/rds.md#rds-read-replica-use-source-unavailable)
  link: [while the source DB instance is unavailable](../facts/rds.md#rds-read-replica-use-source-unavailable)
rds-read-replica-with-multi-az-source
  claim: A DB instance can have a read replica and a Multi-AZ standby at the same time; replication to the standby is synchronous, and unlike a read replica the standby cannot serve read traffic.
  scope: RDS DB instance read replicas.
  link: [Replication with the standby replica is synchronous](../facts/rds.md#rds-read-replica-with-multi-az-source)
  link: [a standby replica can't serve read traffic](../facts/rds.md#rds-read-replica-with-multi-az-source)
rds-replica-billing-active-until-delete
  claim: Billing for a read replica begins when it has been created (status active) and continues at standard DB instance hour rates until you delete it.
  scope: read replicas.
  link: [replica has been successfully created](../facts/rds.md#rds-replica-billing-active-until-delete)
  link: [until you issue a command to delete it](../facts/rds.md#rds-replica-billing-active-until-delete)
rds-replica-lag-cause-write-load
  claim: In a Multi-AZ DB cluster, replica lag generally occurs when the write workload is too high for the reader DB instances to apply the transactions efficiently.
  scope: RDS Multi-AZ DB clusters (writer and reader DB instances).
  link: [write workload is too high](../facts/rds.md#rds-replica-lag-cause-write-load)
rds-replica-lag-causes-faq
  claim: A read replica can fall behind when write I/O on the source exceeds the replica's apply rate (more likely if the replica has less compute), when complex or long-running transactions hold up replication, or because of network partitions or latency.
  scope: RDS DB instance read replicas.
  link: [Complex or long-running transactions](../facts/rds.md#rds-replica-lag-causes-faq)
  link: [Network partitions or latency](../facts/rds.md#rds-replica-lag-causes-faq)
rds-replica-lag-metric-definition
  claim: In a Multi-AZ DB cluster, replica lag is the difference in time between the latest transaction on the writer DB instance and the latest applied transaction on a reader DB instance; the CloudWatch metric ReplicaLag represents this time difference.
  scope: RDS Multi-AZ DB clusters (writer and reader DB instances).
  link: [ReplicaLag](../facts/rds.md#rds-replica-lag-metric-definition)
  link: [difference in time between the latest transaction](../facts/rds.md#rds-replica-lag-metric-definition)
rds-replica-mysql-logical-writable
  claim: RDS for MariaDB and MySQL read replicas use logical replication, and you can enable a MariaDB or MySQL read replica to be writable.
  scope: RDS for MariaDB and RDS for MySQL read replicas.
  link: [Logical replication.](../facts/rds.md#rds-replica-mysql-logical-writable)
  link: [read replica to be writable](../facts/rds.md#rds-replica-mysql-logical-writable)
rds-replica-postgresql-not-writable
  claim: An RDS for PostgreSQL read replica is a physical copy and cannot be made writable; PostgreSQL has a single process handling replication.
  scope: RDS for PostgreSQL read replicas.
  link: [to be made writable](../facts/rds.md#rds-replica-postgresql-not-writable)
  link: [PostgreSQL has a single process handling replication.](../facts/rds.md#rds-replica-postgresql-not-writable)
rds-replica-size-as-much-as-source
  claim: For effective replication AWS recommends read replicas with as much or more compute and storage as their source; otherwise replication lag likely increases or the replica can run out of space.
  scope: RDS DB instance read replicas.
  link: [as much or more compute and storage resources](../facts/rds.md#rds-replica-size-as-much-as-source)
  link: [replication lag is likely to increase](../facts/rds.md#rds-replica-size-as-much-as-source)
rds-replica-sqlserver-no-backups
  claim: Automatic backups and manual snapshots aren't supported on RDS for SQL Server read replicas, while they are supported on RDS for MariaDB and RDS for MySQL read replicas.
  scope: read replicas, per engine.
  link: [aren't supported on RDS for SQL Server](../facts/rds.md#rds-replica-sqlserver-no-backups)
rds-replica-status-error-terminated
  claim: For RDS for MariaDB, MySQL and PostgreSQL read replicas, if replication is stopped for more than 30 consecutive days, either manually or due to a replication error, Amazon RDS terminates replication between the primary DB instance and all read replicas.
  scope: RDS for MariaDB, MySQL and PostgreSQL read replicas; fixed; replication stopped manually or by an error.
  link: [more than 30 consecutive days](../facts/rds.md#rds-replica-status-error-terminated)
  link: [Amazon RDS terminates replication](../facts/rds.md#rds-replica-status-error-terminated)
rds-replicas-resume-after-multi-az-failover
  claim: When a Multi-AZ source fails over, its available read replicas resume replication automatically from the newly promoted primary once failover completes.
  scope: read replicas of a Multi-AZ DB instance deployment.
  link: [automatically resume replication once failover has completed](../facts/rds.md#rds-replicas-resume-after-multi-az-failover)
rds-required-patching-security-reliability
  claim: RDS automatically schedules required patching only for patches related to security and instance reliability; such patching is infrequent, typically once every few months.
  scope: RDS maintenance and engine upgrades.
  link: [typically once every few months](../facts/rds.md#rds-required-patching-security-reliability)
rds-resilience-pitr-retention
  claim: Amazon RDS saves automated backups according to the retention period you set, and you can recover the database to any point in time during that retention period.
  scope: RDS automated backups and snapshots.
  link: [any point in time](../facts/rds.md#rds-resilience-pitr-retention)
rds-resilience-replica-promote-dr
  claim: Read replicas use the MariaDB, MySQL, Oracle and PostgreSQL engines' built-in asynchronous replication; you can route reads to them to reduce load on the source, and promote a read replica to a standalone instance as a disaster recovery solution if the source fails.
  scope: RDS DB instance read replicas.
  link: [promote a read replica to a standalone instance](../facts/rds.md#rds-resilience-replica-promote-dr)
rds-resilience-snapshot-restore-dr
  claim: You can create a DB instance by restoring a DB snapshot as a disaster recovery solution if the source DB instance fails.
  scope: DB snapshots.
  link: [restoring from this DB snapshot](../facts/rds.md#rds-resilience-snapshot-restore-dr)
rds-restore-cannot-reduce-storage
  claim: You cannot reduce the amount of storage when you restore a DB instance.
  scope: restore from DB snapshot.
  link: [You can't reduce the amount of storage](../facts/rds.md#rds-restore-cannot-reduce-storage)
rds-restore-creates-new-instance
  claim: Restoring a DB snapshot always creates a new DB instance; you cannot restore a snapshot onto an existing DB instance.
  scope: restoring a DB instance from a snapshot or a point in time.
  link: [can't restore from a DB snapshot](../facts/rds.md#rds-restore-creates-new-instance)
  link: [you create a new DB instance](../facts/rds.md#rds-restore-creates-new-instance)
rds-restore-default-parameter-group
  claim: A restored DB instance gets the default DB parameter group unless you choose a different one, and the default group has no custom parameter settings.
  scope: restored DB instances; default; adjustable.
  link: [The default DB parameter group is associated](../facts/rds.md#rds-restore-default-parameter-group)
  link: [unless you choose a different one](../facts/rds.md#rds-restore-default-parameter-group)
rds-restore-default-vpc-security-group
  claim: A restored DB instance gets the default VPC, DB subnet group and VPC security group unless you choose different ones.
  scope: restored DB instances; default; adjustable.
  link: [and VPC security group are associated](../facts/rds.md#rds-restore-default-vpc-security-group)
  link: [unless you choose different ones](../facts/rds.md#rds-restore-default-vpc-security-group)
rds-restore-different-storage-type
  claim: You can restore a DB instance with a different storage type than the source snapshot, though the restore is slower because the data must be migrated.
  scope: restoring a DB instance from a snapshot or a point in time.
  link: [use a different storage type](../facts/rds.md#rds-restore-different-storage-type)
  link: [the restore process is slower](../facts/rds.md#rds-restore-different-storage-type)
rds-restore-lazy-loading
  claim: A restored DB instance can be used as soon as it is available while it keeps loading data from Amazon S3 in the background (lazy loading); data not yet loaded is downloaded on first access.
  scope: restoring a DB instance from a snapshot or a point in time.
  link: [lazy loading](../facts/rds.md#rds-restore-lazy-loading)
  link: [continues to load data in the background](../facts/rds.md#rds-restore-lazy-loading)
rds-restore-shared-encrypted-copy-first
  claim: You cannot restore a DB instance directly from a DB snapshot that is both shared and encrypted; copy the snapshot and restore from the copy.
  scope: restoring a DB instance from a snapshot or a point in time.
  link: [both shared and encrypted](../facts/rds.md#rds-restore-shared-encrypted-copy-first)
  link: [make a copy of the DB snapshot](../facts/rds.md#rds-restore-shared-encrypted-copy-first)
rds-restore-standard-or-multi-az
  claim: A DB instance created by point-in-time restore or snapshot restore can be standard or Multi-AZ, regardless of the deployment the backup came from.
  scope: restoring a DB instance from a snapshot or a point in time.
  link: [can be either standard or Multi-AZ](../facts/rds.md#rds-restore-standard-or-multi-az)
rds-retained-automated-backups-expire
  claim: Retained automated backups of a deleted DB instance are kept for the retention period set at deletion and then expire completely, so AWS strongly suggests also taking a final snapshot, which does not expire.
  scope: retained automated backups of deleted DB instances.
  link: [retained automated backups eventually expire](../facts/rds.md#rds-retained-automated-backups-expire)
  link: [The final snapshot doesn't expire.](../facts/rds.md#rds-retained-automated-backups-expire)
rds-retained-automated-backups-instances-only
  claim: Automated backups can be retained after deletion only for DB instances, not for Multi-AZ DB clusters.
  scope: deleting a DB instance and its backups.
  link: [not Multi-AZ DB clusters](../facts/rds.md#rds-retained-automated-backups-instances-only)
rds-retained-backups-billed-until-deleted
  claim: Retained automated backups and manual snapshots incur billing charges until they are deleted.
  scope: deleting a DB instance and its backups.
  link: [incur billing charges until they're deleted](../facts/rds.md#rds-retained-backups-billed-until-deleted)
rds-retained-backups-no-parameter-groups
  claim: Retained automated backups do not contain information about parameter groups or option groups.
  scope: retained automated backups.
  link: [don't contain information about parameters or option groups](../facts/rds.md#rds-retained-backups-no-parameter-groups)
rds-ri-multi-az-and-single-az
  claim: Reserved DB instance benefits apply to both Multi-AZ and Single-AZ configurations, so you can move between them within the same DB instance class type.
  scope: per reserved DB instance; the example on the page: one large Single-AZ instance (four normalized units per hour) equals two medium instances in Multi-AZ (2+2 = 4).
  link: [apply to both Multi-AZ and Single-AZ configurations](../facts/rds.md#rds-ri-multi-az-and-single-az)
  say: it covers both Multi-AZ and Single-AZ
rds-ri-no-upfront-one-year-only
  claim: The No Upfront payment option for a reserved DB instance is only available as a one-year reservation.
  scope: per reserved DB instance (No Upfront).
  link: [only available as a one-year reservation](../facts/rds.md#rds-ri-no-upfront-one-year-only)
  say: one year only
rds-ri-payment-options
  claim: Amazon RDS reserved instances have three payment options: No Upfront, Partial Upfront and All Upfront.
  scope: per reserved DB instance purchase.
  link: [No Upfront, Partial Upfront, All Upfront](../facts/rds.md#rds-ri-payment-options)
  say: no upfront, partial upfront and all upfront
rds-ri-size-flexibility-exclusions
  claim: Size-flexible reserved DB instances apply only within the same instance class type, Region and engine, and size flexibility does not apply to RDS for SQL Server and RDS for Oracle License Included.
  scope: per reserved DB instance.
  link: [Size flexibility does not apply](../facts/rds.md#rds-ri-size-flexibility-exclusions)
  link: [can only scale in their instance class type](../facts/rds.md#rds-ri-size-flexibility-exclusions)
  say: not for SQL Server or license-included Oracle | only within one instance class type
rds-ri-terms-no-cancel
  claim: A reserved DB instance is a one-year or three-year commitment that can't be cancelled; it is a billing discount, not a physical instance.
  scope: per reserved DB instance; you can delete the covered DB instance and launch a compatible one to keep the discount.
  link: [a one-year or three-year commitment](../facts/rds.md#rds-ri-terms-no-cancel)
  link: [You can't cancel a reserved DB instance](../facts/rds.md#rds-ri-terms-no-cancel)
  say: one or three years | it can't be cancelled
rds-savings-plans-flexibility
  claim: Database Savings Plans apply automatically to the latest provisioned instance generations regardless of engine, instance family, size, Availability Zone or Region, and also to serverless usage.
  scope: Database Savings Plans.
  link: [regardless of engine, instance family, size](../facts/rds.md#rds-savings-plans-flexibility)
rds-savings-plans-not-combined-with-ri
  claim: For the same workload you cannot combine Database Savings Plans with Amazon RDS Reserved Instances; you can use a Reserved Instance for one workload and a Database Savings Plan for another.
  scope: Database Savings Plans.
  link: [you cannot combine Database Savings Plans](../facts/rds.md#rds-savings-plans-not-combined-with-ri)
rds-savings-plans-sqlserver-license-excluded
  claim: For Amazon RDS for SQL Server, Database Savings Plans apply only to the instance price; Windows Server and SQL Server licensing is billed separately at on-demand rates.
  scope: Database Savings Plans.
  link: [apply only to instance price](../facts/rds.md#rds-savings-plans-sqlserver-license-excluded)
rds-sec-bp-iam-for-api
  claim: AWS advises using IAM to control access to Amazon RDS API operations, especially those that create, modify or delete RDS resources such as DB instances, security groups and parameter groups.
  scope: RDS security best practices.
  link: [control access to Amazon RDS API operations](../facts/rds.md#rds-sec-bp-iam-for-api)
rds-sec-bp-master-password-change
  claim: Change the RDS master user password with the AWS Management Console, AWS CLI or RDS API; changing it with another tool such as a SQL client might revoke privileges for the user.
  scope: RDS security best practices.
  link: [privileges being revoked for the user unintentionally](../facts/rds.md#rds-sec-bp-master-password-change)
rds-sec-bp-secrets-manager-rotation
  claim: The RDS security best practices advise configuring AWS Secrets Manager to rotate the secrets for Amazon RDS automatically.
  scope: RDS security best practices.
  link: [automatically rotate the secrets](../facts/rds.md#rds-sec-bp-secrets-manager-rotation)
rds-secrets-manager-deleted-with-instance
  claim: If you delete a DB instance that manages a secret in Secrets Manager, the secret and its metadata are deleted too.
  scope: RDS-managed master user password in AWS Secrets Manager.
  link: [the secret and its associated metadata](../facts/rds.md#rds-secrets-manager-deleted-with-instance)
rds-secrets-manager-master-password
  claim: When RDS manages the master user password in Secrets Manager, RDS generates the password, stores it in Secrets Manager, and rotates the secret every seven days by default (the schedule can be changed).
  scope: master user password managed by RDS in Secrets Manager; default.
  link: [every seven days](../facts/rds.md#rds-secrets-manager-master-password)
  link: [RDS generates the password](../facts/rds.md#rds-secrets-manager-master-password)
rds-secrets-manager-no-app-changes
  claim: With Secrets Manager managing the master password, RDS rotates database credentials regularly without requiring application changes.
  scope: RDS-managed master user password in AWS Secrets Manager.
  link: [without requiring application changes](../facts/rds.md#rds-secrets-manager-no-app-changes)
rds-secrets-manager-not-blue-green-custom
  claim: RDS management of master passwords in Secrets Manager is not supported for Blue/Green Deployments, RDS Custom, Oracle Data Guard switchover, or creating a read replica from a source that manages credentials this way (except RDS for SQL Server and Db2).
  scope: RDS-managed master user password in AWS Secrets Manager.
  link: [all DB engines except RDS for SQL Server](../facts/rds.md#rds-secrets-manager-not-blue-green-custom)
  link: [Creating a read replica](../facts/rds.md#rds-secrets-manager-not-blue-green-custom)
rds-security-group-default-no-access
  claim: VPC security groups control traffic in and out of a DB instance, and by default network access to a DB instance is turned off until security group rules allow it.
  scope: DB instance network access; default; adjustable.
  link: [network access is turned off](../facts/rds.md#rds-security-group-default-no-access)
  link: [VPC security groups control the access](../facts/rds.md#rds-security-group-default-no-access)
rds-security-group-source-sg
  claim: A VPC security group rule for a DB instance can specify another VPC security group as the source, which allows incoming traffic from all instances (typically application servers) that use the source VPC security group.
  scope: VPC security groups for DB instances.
  link: [specifying a VPC security group as the source](../facts/rds.md#rds-security-group-source-sg)
  link: [typically application servers](../facts/rds.md#rds-security-group-source-sg)
rds-security-managed-processes
  claim: You configure security only for your own use cases, not for processes Amazon RDS manages such as creating backups and replicating to read replicas.
  scope: security configuration for RDS.
  link: [You don't have to configure security access](../facts/rds.md#rds-security-managed-processes)
rds-separate-azs-protect-location-failure
  claim: Each Availability Zone is engineered to be isolated from failures in other AZs, so launching DB instances in separate Availability Zones protects applications from the failure of a single location.
  scope: DB instances in several Availability Zones.
  link: [isolated from failures in other Availability Zones](../facts/rds.md#rds-separate-azs-protect-location-failure)
  link: [the failure of a single location](../facts/rds.md#rds-separate-azs-protect-location-failure)
rds-share-automated-copy-first
  claim: To share an automated DB snapshot, you first copy it to a manual DB snapshot and share the copy; this also applies to AWS Backup-generated resources.
  scope: DB snapshots.
  link: [copying the automated snapshot](../facts/rds.md#rds-share-automated-copy-first)
rds-share-default-kms-key-not-shareable
  claim: You can't share a snapshot encrypted with the default KMS key (the AWS managed key) of the sharing account; to share it, create a customer managed key in the same Region and give the other account access to it, copy the snapshot to a new snapshot using the customer managed key, and share the copy.
  scope: encrypted manual DB snapshots.
  link: [encrypted using the default KMS key](../facts/rds.md#rds-share-default-kms-key-not-shareable)
  link: [using the customer managed key](../facts/rds.md#rds-share-default-kms-key-not-shareable)
rds-share-public-unencrypted-only
  claim: Only an unencrypted manual snapshot can be shared as Public; a Public snapshot lets all AWS accounts restore a DB instance from it, and encrypted snapshots cannot be shared as public.
  scope: manual DB snapshots.
  link: [encrypted snapshots can't be shared as public](../facts/rds.md#rds-share-public-unencrypted-only)
  link: [all AWS accounts can restore a DB instance](../facts/rds.md#rds-share-public-unencrypted-only)
rds-share-snapshot-copy-or-restore
  claim: Sharing a manual DB snapshot lets authorized accounts copy it whether encrypted or not; sharing an unencrypted manual snapshot also lets them restore a DB instance from it directly.
  scope: manual DB snapshots.
  link: [enables authorized AWS accounts to copy the snapshot](../facts/rds.md#rds-share-snapshot-copy-or-restore)
  link: [directly restore a DB instance from the snapshot](../facts/rds.md#rds-share-snapshot-copy-or-restore)
rds-share-tde-snapshots-not-shareable
  claim: Oracle or Microsoft SQL Server snapshots encrypted with Transparent Data Encryption (TDE) cannot be shared.
  scope: RDS for Oracle and RDS for SQL Server.
  link: [encrypted using Transparent Data Encryption (TDE)](../facts/rds.md#rds-share-tde-snapshots-not-shareable)
rds-snapshot-copy-cross-region-account-single-step
  claim: A snapshot can be copied within a Region, across Regions, and from shared snapshots, and can be copied to another Region or account in a single step.
  scope: DB snapshots; the snapshot (and its KMS key, if encrypted) must first be shared with the target account.
  link: [in a single step](../facts/rds.md#rds-snapshot-copy-cross-region-account-single-step)
  link: [copy a snapshot across AWS Regions](../facts/rds.md#rds-snapshot-copy-cross-region-account-single-step)
rds-snapshot-copy-cross-region-kms-destination
  claim: To copy an encrypted snapshot to another Region you must specify a KMS key valid in the destination Region (a Region-specific key or a multi-Region key), because KMS keys cannot be used outside the Region where they were created.
  scope: cross-Region copy of encrypted snapshots.
  link: [KMS key valid in the destination AWS Region](../facts/rds.md#rds-snapshot-copy-cross-region-kms-destination)
  link: [a multi-Region key](../facts/rds.md#rds-snapshot-copy-cross-region-kms-destination)
rds-snapshot-copy-cross-region-transfer-charges
  claim: Copying a DB snapshot to another Region creates a manual snapshot retained in that Region, and copying it out of the source Region incurs RDS data transfer charges.
  scope: cross-Region snapshot copy.
  link: [create a manual DB snapshot that is retained](../facts/rds.md#rds-snapshot-copy-cross-region-transfer-charges)
  link: [incurs Amazon RDS data transfer charges](../facts/rds.md#rds-snapshot-copy-cross-region-transfer-charges)
rds-snapshot-copy-encrypted-stays-encrypted
  claim: The copy of an encrypted snapshot must also be encrypted; within a Region you can keep the same KMS key or choose another.
  scope: DB snapshots.
  link: [must also be encrypted](../facts/rds.md#rds-snapshot-copy-encrypted-stays-encrypted)
  link: [Or you can specify a different KMS key.](../facts/rds.md#rds-snapshot-copy-encrypted-stays-encrypted)
rds-snapshot-copy-is-manual
  claim: You can copy automated backups or manual DB snapshots, and the copy is always a manual snapshot.
  scope: DB snapshots.
  link: [the copy is a manual snapshot](../facts/rds.md#rds-snapshot-copy-is-manual)
rds-snapshot-copy-not-multi-az-cluster
  claim: You cannot copy a snapshot of a Multi-AZ DB cluster, and you cannot share one.
  scope: Multi-AZ DB cluster snapshots.
  link: [You can't copy a snapshot](../facts/rds.md#rds-snapshot-copy-not-multi-az-cluster)
  link: [You can't share a snapshot](../facts/rds.md#rds-snapshot-copy-not-multi-az-cluster)
rds-snapshot-single-az-io-suspension
  claim: A DB snapshot of a Single-AZ DB instance causes a brief I/O suspension of a few seconds to a few minutes; for Multi-AZ MariaDB, MySQL, Oracle and PostgreSQL the backup is taken from the standby so the primary's I/O is not suspended, while SQL Server Multi-AZ still suspends I/O briefly.
  scope: DB snapshots and backups, per deployment and engine.
  link: [brief I/O suspension](../facts/rds.md#rds-snapshot-single-az-io-suspension)
  link: [the backup is taken from the standby](../facts/rds.md#rds-snapshot-single-az-io-suspension)
  link: [For SQL Server, I/O activity is suspended briefly](../facts/rds.md#rds-snapshot-single-az-io-suspension)
rds-snapshots-copy-both-share-manual
  claim: You can copy both automated and manual DB snapshots, but you can share only manual DB snapshots.
  scope: DB snapshots.
  link: [share manual DB snapshots](../facts/rds.md#rds-snapshots-copy-both-share-manual)
  link: [copy both automatic and manual DB snapshots](../facts/rds.md#rds-snapshots-copy-both-share-manual)
rds-snapshots-incremental
  claim: The first snapshot of a DB instance holds the full database; later snapshots of the same database are incremental and save only the data changed since the most recent snapshot.
  scope: DB snapshots.
  link: [Subsequent snapshots of the same database are incremental](../facts/rds.md#rds-snapshots-incremental)
rds-sqlserver-express-free-dev
  claim: For development and testing, SQL Server Express Edition is a free edition available with License Included, and Developer Edition is licensed for non-production use only with BYOM.
  scope: RDS for SQL Server.
  link: [**Express Edition** A free edition](../facts/rds.md#rds-sqlserver-express-free-dev)
  link: [licensed for non-production use only](../facts/rds.md#rds-sqlserver-express-free-dev)
rds-sqlserver-li-byom
  claim: RDS for SQL Server supports License Included, where RDS pricing includes the SQL Server license, and Bring Your Own Media, where RDS charges no SQL Server license fee and you use existing licenses with License Mobility through Software Assurance.
  scope: RDS for SQL Server.
  link: [License Included and Bring Your Own Media](../facts/rds.md#rds-sqlserver-li-byom)
  link: [pricing includes the SQL Server software license](../facts/rds.md#rds-sqlserver-li-byom)
rds-sqlserver-read-replicas-limits
  claim: RDS for SQL Server allows up to 15 read replicas from one source DB instance, but replication might lag when the source has more than 5 read replicas.
  scope: per source DB instance (SQL Server); maximum; not adjustable; Enterprise Edition only, on DB instance classes with four or more vCPUs.
  link: [up to 15 read replicas](../facts/rds.md#rds-sqlserver-read-replicas-limits)
  link: [more than 5 read replicas](../facts/rds.md#rds-sqlserver-read-replicas-limits)
  say: up to fifteen read replicas | lag can appear above five replicas
rds-sqlserver-read-replicas-requirements
  claim: RDS for SQL Server read replicas are only available on the Enterprise Edition engine and on DB instance classes with four or more vCPUs.
  scope: per DB instance (SQL Server); minimum.
  link: [only available on the SQL Server Enterprise Edition](../facts/rds.md#rds-sqlserver-read-replicas-requirements)
  link: [four or more vCPUs](../facts/rds.md#rds-sqlserver-read-replicas-requirements)
  say: Enterprise Edition only | four or more vCPUs
rds-stop-billing
  claim: While a DB instance is stopped, you are charged for provisioned storage (including Provisioned IOPS) and backup storage, but not for DB instance hours.
  scope: per stopped DB instance; a publicly accessible instance is also charged for its public IPv4 address.
  link: [charged for provisioned storage (including Provisioned IOPS)](../facts/rds.md#rds-stop-billing)
  link: [you're not charged for DB instance hours](../facts/rds.md#rds-stop-billing)
  say: you still pay for storage and provisioned IOPS | no instance-hour charges
rds-stop-max-seven-days
  claim: A DB instance can be stopped for a maximum of 7 consecutive days; if you don't start it after seven consecutive days, RDS starts it automatically.
  scope: per DB instance; maximum; not adjustable; RDS then starts the instance so it doesn't fall behind required maintenance.
  link: [7 consecutive days](../facts/rds.md#rds-stop-max-seven-days)
  say: seven consecutive days
rds-stop-not-with-read-replica
  claim: You can't stop a DB instance that has a read replica or that is a read replica, and RDS for SQL Server doesn't support stopping a DB instance in a Multi-AZ deployment.
  scope: per DB instance.
  link: [You can't stop a DB instance](../facts/rds.md#rds-stop-not-with-read-replica)
  link: [doesn't support stopping a DB instance](../facts/rds.md#rds-stop-not-with-read-replica)
  say: instances with read replicas, and read replicas | SQL Server in a Multi-AZ deployment
rds-storage-additional-volumes-three
  claim: With RDS for Oracle and RDS for SQL Server you can attach up to three additional storage volumes to a DB instance, each gp3 or io2.
  scope: per DB instance (Oracle, SQL Server); maximum; not adjustable; storage autoscaling isn't supported for additional storage volumes.
  link: [up to three additional storage volumes](../facts/rds.md#rds-storage-additional-volumes-three)
  say: up to three additional storage volumes
rds-storage-autoscaling-cannot-decrease
  claim: Storage autoscaling can't decrease the allocated storage, and you can't reduce the storage of a DB instance after it has been allocated.
  scope: per DB instance; to shrink, use a blue/green deployment or a new DB instance with less storage.
  link: [Autoscaling can't decrease the allocated storage](../facts/rds.md#rds-storage-autoscaling-cannot-decrease)
  say: autoscaling never shrinks storage
rds-storage-autoscaling-default-threshold
  claim: The default maximum storage threshold for storage autoscaling is 1,000 GiB, so with the default an instance doesn't autoscale above 1,000 GiB.
  scope: per autoscaling-enabled DB instance; default; adjustable; you can set a higher threshold up to the maximum allocated storage of the engine and instance class.
  link: [1,000 GiB](../facts/rds.md#rds-storage-autoscaling-default-threshold)
  say: one thousand gibibytes
rds-storage-autoscaling-large-loads
  claim: Storage autoscaling cannot completely prevent storage-full situations during large data loads, because further storage modifications must wait for storage optimization and are limited in number per day.
  scope: storage autoscaling; large data loads.
  link: [can't completely prevent storage-full situations](../facts/rds.md#rds-storage-autoscaling-large-loads)
rds-storage-autoscaling-max-threshold
  claim: The maximum storage threshold is the limit you set for autoscaling a DB instance, and autoscaling does not occur if the increment would exceed it.
  scope: storage autoscaling.
  link: [maximum storage threshold](../facts/rds.md#rds-storage-autoscaling-max-threshold)
rds-storage-autoscaling-no-downtime
  claim: Enabling storage autoscaling doesn't require a database reboot and doesn't cause any downtime.
  scope: per DB instance.
  link: [doesn't cause any downtime](../facts/rds.md#rds-storage-autoscaling-no-downtime)
  say: no downtime and no reboot
rds-storage-autoscaling-not-magnetic
  claim: Storage autoscaling cannot be used with magnetic storage, and autoscaling operations are not logged by AWS CloudTrail.
  scope: storage autoscaling.
  link: [Autoscaling can't be used with magnetic storage.](../facts/rds.md#rds-storage-autoscaling-not-magnetic)
  link: [aren't logged by AWS CloudTrail](../facts/rds.md#rds-storage-autoscaling-not-magnetic)
rds-storage-autoscaling-threshold-min-10-percent
  claim: The maximum storage threshold for storage autoscaling must be at least 10% more than the current allocated storage; AWS recommends at least 26% more to avoid an event notification.
  scope: per autoscaling-enabled DB instance; minimum.
  link: [at least 10% more](../facts/rds.md#rds-storage-autoscaling-threshold-min-10-percent)
  link: [at least 26% more](../facts/rds.md#rds-storage-autoscaling-threshold-min-10-percent)
  say: at least ten percent more | at least twenty-six percent more
rds-storage-autoscaling-trigger-five-minutes
  claim: Storage autoscaling acts only when the low-storage condition lasts at least five minutes.
  scope: per autoscaling-enabled DB instance; minimum; not adjustable; one of three trigger conditions.
  link: [at least five minutes](../facts/rds.md#rds-storage-autoscaling-trigger-five-minutes)
  say: at least five minutes
rds-storage-autoscaling-trigger-free-space
  claim: Storage autoscaling starts a storage increase when free available space is less than or equal to 10 percent of the allocated storage (together with the other trigger conditions).
  scope: per autoscaling-enabled DB instance; fixed; not adjustable; the low-storage condition must also last at least five minutes, and the previous modification must have finished optimizing.
  link: [10 percent of the allocated storage](../facts/rds.md#rds-storage-autoscaling-trigger-free-space)
  say: ten percent of the allocated storage
rds-storage-autoscaling-unpredictable
  claim: Storage autoscaling is meant for unpredictable workloads: when RDS detects that the DB instance is running out of free space, it scales up the storage automatically, avoiding manual scaling.
  scope: storage autoscaling.
  link: [If your workload is unpredictable](../facts/rds.md#rds-storage-autoscaling-unpredictable)
  link: [it automatically scales up your storage](../facts/rds.md#rds-storage-autoscaling-unpredictable)
rds-storage-choice-oltp-moderate
  claim: AWS maps high-performance OLTP workloads to Provisioned IOPS (SSD) storage and database workloads with moderate I/O requirements to General Purpose (SSD) storage; Provisioned IOPS provisions a chosen IOPS rate for the life of the instance.
  scope: RDS DB instance storage and performance.
  link: [High-performance OLTP workloads](../facts/rds.md#rds-storage-choice-oltp-moderate)
  link: [moderate I/O requirements](../facts/rds.md#rds-storage-choice-oltp-moderate)
  link: [fast, predictable, and consistent I/O performance](../facts/rds.md#rds-storage-choice-oltp-moderate)
rds-storage-dlv-fixed-size
  claim: A dedicated log volume (DLV) is supported only for Provisioned IOPS storage (io1 and io2 Block Express) and is created with a fixed size of 1,024 GiB and 3,000 Provisioned IOPS.
  scope: per dedicated log volume; fixed; not adjustable; DLVs aren't supported for gp2 and gp3.
  link: [1,024 GiB](../facts/rds.md#rds-storage-dlv-fixed-size)
  link: [3,000 Provisioned IOPS](../facts/rds.md#rds-storage-dlv-fixed-size)
  say: one thousand twenty-four gibibytes | three thousand provisioned IOPS
rds-storage-ebs-striping
  claim: Amazon RDS stores database and logs on EBS volumes and, depending on the storage size, stripes across multiple EBS volumes to improve IOPS performance.
  scope: RDS DB instance storage and performance.
  link: [Amazon RDS uses EBS volumes](../facts/rds.md#rds-storage-ebs-striping)
  link: [stripes across multiple EBS volumes](../facts/rds.md#rds-storage-ebs-striping)
rds-storage-gp-for-dev-test
  claim: General Purpose SSD storage is cost-effective for a broad range of workloads and is best suited for development and testing environments.
  scope: RDS DB instance storage and performance.
  link: [best suited for development and testing environments](../facts/rds.md#rds-storage-gp-for-dev-test)
  link: [cost-effective storage type](../facts/rds.md#rds-storage-gp-for-dev-test)
rds-storage-gp2-baseline-per-gib
  claim: gp2 storage has a baseline I/O performance of 3 IOPS for each GiB, with a minimum of 100 IOPS, so larger volumes perform better.
  scope: per gp2 volume; fixed; not adjustable; gp2 is the previous generation; IOPS can't be provisioned directly on gp2.
  link: [3 IOPS for each GiB](../facts/rds.md#rds-storage-gp2-baseline-per-gib)
  link: [a minimum of 100 IOPS](../facts/rds.md#rds-storage-gp2-baseline-per-gib)
  say: three IOPS per gibibyte | at least one hundred IOPS
rds-storage-gp2-burst
  claim: Individual gp2 volumes below 1,000 GiB can burst to 3,000 IOPS for extended periods, limited by the volume's I/O credit balance.
  scope: per gp2 volume below 1,000 GiB; maximum; not adjustable; burst performance depends on the I/O credit balance.
  link: [3,000 IOPS](../facts/rds.md#rds-storage-gp2-burst)
  link: [below 1,000 GiB](../facts/rds.md#rds-storage-gp2-burst)
  say: three thousand IOPS | volumes below one thousand gibibytes
rds-storage-gp2-range-small
  claim: For MariaDB, MySQL and PostgreSQL gp2 volumes of 5–399 GiB, baseline IOPS range from 100-1197 IOPS with 128-250 MiB/s of throughput and bursts to 3,000 IOPS.
  scope: per DB instance (gp2; MariaDB, MySQL, PostgreSQL); fixed; not adjustable; gp2 is the previous generation.
  link: [100-1197 IOPS](../facts/rds.md#rds-storage-gp2-range-small)
  link: [3,000](../facts/rds.md#rds-storage-gp2-range-small)
  say: one hundred to eleven hundred ninety-seven IOPS | three thousand IOPS burst
rds-storage-gp3-baseline
  claim: On gp3 storage volumes, Amazon RDS provides a baseline storage performance of 3000 IOPS and 125 MiB/s.
  scope: per gp3 storage volume (below the striping threshold); default; adjustable; for striped volumes the baseline is 12,000 IOPS and 500 MiB/s.
  link: [3000 IOPS](../facts/rds.md#rds-storage-gp3-baseline)
  link: [125 MiB/s](../facts/rds.md#rds-storage-gp3-baseline)
  say: three thousand IOPS | one hundred twenty-five mebibytes per second
rds-storage-gp3-iops-ratio-max
  claim: On gp3, the maximum ratio of IOPS to allocated storage is 500 and the maximum ratio of storage throughput to IOPS is 0.25, for all supported DB engines.
  scope: per DB instance (gp3); maximum; not adjustable; on RDS for SQL Server the minimum IOPS-to-storage ratio is 0.5.
  link: [500](../facts/rds.md#rds-storage-gp3-iops-ratio-max)
  link: [0.25](../facts/rds.md#rds-storage-gp3-iops-ratio-max)
  say: five hundred | zero point two five
rds-storage-gp3-range-large
  claim: For Db2, MariaDB, MySQL and PostgreSQL gp3 volumes of 400–65,536 GiB, the baseline is 12,000 IOPS/500 MiB/s, and you can provision 12,000–64,000 IOPS and 500–4,000 MiB/s of throughput.
  scope: per DB instance (gp3; Db2, MariaDB, MySQL, PostgreSQL); maximum; not adjustable; at or above the 400 GiB threshold.
  link: [400–65,536 GiB](../facts/rds.md#rds-storage-gp3-range-large)
  link: [12,000 IOPS/500 MiB/s](../facts/rds.md#rds-storage-gp3-range-large)
  link: [12,000–64,000 IOPS](../facts/rds.md#rds-storage-gp3-range-large)
  link: [500–4,000 MiB/s](../facts/rds.md#rds-storage-gp3-range-large)
  say: four hundred gibibytes and more | twelve thousand IOPS and five hundred mebibytes per second | twelve thousand to sixty-four thousand IOPS | five hundred to four thousand mebibytes per second
rds-storage-gp3-range-small
  claim: For Db2, MariaDB, MySQL and PostgreSQL gp3 volumes of 20–399 GiB, the baseline is 3,000 IOPS/125 MiB/s and additional IOPS or throughput can't be provisioned (not applicable).
  scope: per DB instance (gp3; Db2, MariaDB, MySQL, PostgreSQL); fixed; not adjustable; below the 400 GiB striping threshold.
  link: [20–399 GiB](../facts/rds.md#rds-storage-gp3-range-small)
  link: [3,000 IOPS/125 MiB/s](../facts/rds.md#rds-storage-gp3-range-small)
  say: twenty to three hundred ninety-nine gibibytes | three thousand IOPS and one hundred twenty-five mebibytes per second
rds-storage-gp3-range-sqlserver
  claim: For RDS for SQL Server gp3 volumes of 20–65,536 GiB, the baseline is 3,000 IOPS/125 MiB/s, and you can provision 3,000–80,000 IOPS and 125–2,000 MiB/s at any storage size.
  scope: per DB instance (gp3; SQL Server); maximum; not adjustable; SQL Server has no striping threshold.
  link: [3,000–80,000 IOPS](../facts/rds.md#rds-storage-gp3-range-sqlserver)
  link: [125–2,000 MiB/s](../facts/rds.md#rds-storage-gp3-range-sqlserver)
  say: three thousand to eighty thousand IOPS | one hundred twenty-five to two thousand mebibytes per second
rds-storage-gp3-striped-baseline
  claim: For striped gp3 volumes (four volumes instead of one, above a storage-size threshold; not on RDS for SQL Server), Amazon RDS provides a baseline of 12,000 IOPS and 500 MiB/s.
  scope: per DB instance with striped gp3 storage; default; adjustable; every engine except RDS for SQL Server, which doesn't support volume striping.
  link: [12,000 IOPS](../facts/rds.md#rds-storage-gp3-striped-baseline)
  link: [500 MiB/s](../facts/rds.md#rds-storage-gp3-striped-baseline)
  say: twelve thousand IOPS | five hundred mebibytes per second
rds-storage-increase-min-10-percent
  claim: A manual increase of a storage volume must be at least 10%, and allocated space can't be deallocated.
  scope: per storage volume; minimum.
  link: [a minimum of 10%](../facts/rds.md#rds-storage-increase-min-10-percent)
  link: [You can't deallocate space](../facts/rds.md#rds-storage-increase-min-10-percent)
  say: at least ten percent | you can't deallocate space
rds-storage-io1-iops-ratio
  claim: For io1 storage, the ratio of IOPS to allocated storage (in GiB) must be from 1–50 on RDS for SQL Server and 0.5–50 on the other RDS DB engines.
  scope: per DB instance (io1); maximum; not adjustable; io1 is the previous generation; AWS recommends io2 Block Express where available.
  link: [1–50](../facts/rds.md#rds-storage-io1-iops-ratio)
  link: [0.5–50](../facts/rds.md#rds-storage-io1-iops-ratio)
  say: one to fifty | half to fifty
rds-storage-io2-iops-ratio
  claim: For io2 Block Express, the ratio of IOPS to allocated storage (in GiB) must be from 0.5–1,000; for DB instances not based on the AWS Nitro System it must be from 0.5–500.
  scope: per DB instance (io2 Block Express); maximum; not adjustable; with storage autoscaling the same ratio applies to the maximum storage threshold.
  link: [0.5–1,000](../facts/rds.md#rds-storage-io2-iops-ratio)
  link: [0.5–500](../facts/rds.md#rds-storage-io2-iops-ratio)
  say: from half to one thousand IOPS per gibibyte | from half to five hundred IOPS per gibibyte
rds-storage-io2-max-iops
  claim: AWS recommends io2 Block Express storage for I/O-intensive, latency-sensitive workloads, with up to 256,000 I/O operations per second.
  scope: per DB instance storage (io2 Block Express); maximum; not adjustable; the DB instance class can impose a lower limit.
  link: [up to 256,000 I/O operations per second](../facts/rds.md#rds-storage-io2-max-iops)
  say: up to two hundred fifty-six thousand IOPS
rds-storage-io2-max-iops-volume-size
  claim: On io2 Block Express, maximum IOPS can be provisioned with volumes of 256 GiB and larger (1,000 IOPS × 256 GiB = 256,000 IOPS).
  scope: per DB instance (io2 Block Express, Nitro-based); minimum; not adjustable; for instances not based on the AWS Nitro System, maximum IOPS are reached at 512 GiB.
  link: [256 GiB and larger](../facts/rds.md#rds-storage-io2-max-iops-volume-size)
  say: two hundred fifty-six gibibytes and larger
rds-storage-io2-range-mysql-postgresql
  claim: For Db2, MariaDB, MySQL and PostgreSQL, io2 Block Express storage ranges from 100–65,536 GiB with 1,000–256,000 IOPS, and the table lists a maximum throughput of 16,000 MiB/s.
  scope: per storage volume (io2 Block Express; Db2, MariaDB, MySQL, PostgreSQL); maximum; not adjustable; the DB instance class can impose lower limits; the comparison table on the same page says throughput scales up to 4,000 MB/s.
  link: [100–65,536 GiB](../facts/rds.md#rds-storage-io2-range-mysql-postgresql)
  link: [1,000–256,000 IOPS](../facts/rds.md#rds-storage-io2-range-mysql-postgresql)
  link: [16,000 MiB/s](../facts/rds.md#rds-storage-io2-range-mysql-postgresql)
  say: one hundred to sixty-five thousand five hundred thirty-six gibibytes | one thousand to two hundred fifty-six thousand IOPS | sixteen thousand mebibytes per second
rds-storage-latency-by-type
  claim: io2 Block Express gives sub-millisecond latency 99.9% of the time, io1 single-digit millisecond latency 99.9% of the time, and gp3 and gp2 single-digit millisecond latency 99% of the time.
  scope: per storage volume type; fixed; not adjustable.
  link: [Sub-millisecond, provided consistently 99.9% of the time](../facts/rds.md#rds-storage-latency-by-type)
  link: [Single-digit millisecond, provided consistently 99% of the time](../facts/rds.md#rds-storage-latency-by-type)
  say: sub-millisecond, ninety-nine point nine percent of the time | single-digit millisecond, ninety-nine percent of the time
rds-storage-magnetic-restore-ends
  claim: Magnetic storage is deprecated and no longer offered for new DB instances, and starting July 1, 2026, you can no longer restore a snapshot to magnetic storage.
  scope: all RDS DB instances; existing magnetic volumes were migrated to gp3.
  link: [July 1, 2026](../facts/rds.md#rds-storage-magnetic-restore-ends)
  link: [no longer offered for new DB instances](../facts/rds.md#rds-storage-magnetic-restore-ends)
  say: July first, twenty twenty-six | no longer offered for new DB instances
rds-storage-max-256-tib-oracle-sqlserver
  claim: RDS for Oracle and RDS for SQL Server DB instances can have up to 256 TiB of storage by adding additional storage volumes; each additional volume holds up to 64 TiB.
  scope: per DB instance (Oracle, SQL Server); maximum; not adjustable; only with additional storage volumes.
  link: [256 TiB](../facts/rds.md#rds-storage-max-256-tib-oracle-sqlserver)
  link: [up to 64 TiB of storage](../facts/rds.md#rds-storage-max-256-tib-oracle-sqlserver)
  say: two hundred fifty-six tebibytes | up to sixty-four tebibytes per additional volume
rds-storage-max-64-tib
  claim: Db2, MySQL, MariaDB and PostgreSQL DB instances can have up to 64 TiB of storage, and every DB instance has a primary storage volume with a maximum capacity of 64 TiB.
  scope: per DB instance (Db2, MySQL, MariaDB, PostgreSQL); per primary storage volume for every engine; maximum; not adjustable; most DB instance classes; some smaller or previous-generation classes have lower maximums.
  link: [64 TiB](../facts/rds.md#rds-storage-max-64-tib)
  say: sixty-four tebibytes
rds-storage-max-iops-by-type
  claim: Maximum IOPS per storage type: io2 Block Express 256,000; io1 256,000 (64,000 on RDS for SQL Server); gp3 and gp2 64,000 (16,000 on RDS for SQL Server); IOPS can't be provisioned directly on gp2.
  scope: per storage volume type; maximum; not adjustable; the DB instance class can impose a lower limit.
  link: [256,000](../facts/rds.md#rds-storage-max-iops-by-type)
  link: [64,000 (16,000 on RDS for SQL Server)](../facts/rds.md#rds-storage-max-iops-by-type)
  say: two hundred fifty-six thousand | sixty-four thousand, sixteen thousand on SQL Server
rds-storage-modifications-four-per-24-hours
  claim: Storage modifications are limited to a maximum of four within any 24-hour period, and a further modification can't start until storage optimization of the previous one completes.
  scope: per DB instance; maximum; not adjustable; applies to storage autoscaling too: it acts only when fewer than four storage modifications occurred in the past 24 hours.
  link: [a maximum of four modifications within any 24-hour period](../facts/rds.md#rds-storage-modifications-four-per-24-hours)
  say: at most four storage modifications in any twenty-four hours
rds-storage-piops-charged-provisioned
  claim: With Provisioned IOPS storage, you are charged for the provisioned resources whether or not you use them in a given month.
  scope: per DB instance with Provisioned IOPS storage.
  link: [whether or not you use them](../facts/rds.md#rds-storage-piops-charged-provisioned)
  say: whether or not you use them
rds-storage-piops-for-production
  claim: Provisioned IOPS storage is designed for I/O-intensive database workloads that need low I/O latency and consistent I/O throughput, and is best suited for production environments.
  scope: RDS DB instance storage and performance.
  link: [low I/O latency and consistent I/O throughput](../facts/rds.md#rds-storage-piops-for-production)
  link: [best suited for production environments](../facts/rds.md#rds-storage-piops-for-production)
  link: [I/O-intensive workloads](../facts/rds.md#rds-storage-piops-for-production)
rds-storage-striping-four-volumes
  claim: For MariaDB, MySQL and PostgreSQL, Amazon RDS automatically stripes SSD storage of 400–65,536 GiB across 4 volumes.
  scope: per DB instance (General Purpose or Provisioned IOPS SSD; MariaDB, MySQL, PostgreSQL); fixed; not adjustable; Oracle stripes from 200 GiB; SQL Server always uses 1 volume.
  link: [400–65,536 GiB](../facts/rds.md#rds-storage-striping-four-volumes)
  link: [4](../facts/rds.md#rds-storage-striping-four-volumes)
  say: four hundred gibibytes and more | four volumes
rds-subnet-group-two-azs
  claim: An RDS DB subnet group requires a subnet in at least two Availability Zones, which also makes it easy to switch to a Multi-AZ deployment later.
  scope: DB subnet group; minimum.
  link: [a subnet in at least two Availability Zones](../facts/rds.md#rds-subnet-group-two-azs)
rds-tls-all-engines
  claim: Applications can use SSL/TLS to encrypt connections to RDS databases running Db2, MariaDB, Microsoft SQL Server, MySQL, Oracle or PostgreSQL, optionally verifying the server certificate.
  scope: encryption in transit (SSL/TLS) to RDS databases.
  link: [Transport Layer Security (TLS)](../facts/rds.md#rds-tls-all-engines)
  link: [server identity verification](../facts/rds.md#rds-tls-all-engines)
rds-tls-force-mysql
  claim: For RDS for MySQL, the require_secure_transport parameter forces SSL/TLS for all user connections; it is OFF by default and can be set to ON in the DB parameter group without a reboot.
  scope: RDS for MySQL; default; adjustable.
  link: [`require_secure_transport`](../facts/rds.md#rds-tls-force-mysql)
  link: [You don't need to reboot your DB instance](../facts/rds.md#rds-tls-force-mysql)
rds-tls-force-postgresql
  claim: For RDS for PostgreSQL, the rds.force_ssl parameter requires SSL connections; its default is 1 (on) for version 15 and later and 0 (off) for 14 and older, and changing it needs a custom DB parameter group.
  scope: RDS for PostgreSQL; default; adjustable; default depends on major version.
  link: [`rds.force_ssl`](../facts/rds.md#rds-tls-force-postgresql)
  link: [version 15 and later](../facts/rds.md#rds-tls-force-postgresql)
  link: [create a custom DB parameter group](../facts/rds.md#rds-tls-force-postgresql)
rds-tls-server-certificate-auto-rotation
  claim: With the rds-ca-rsa2048-g1, rds-ca-rsa4096-g1 or rds-ca-ecc384-g1 certificate authority, RDS manages the DB server certificate and rotates it automatically before it expires.
  scope: databases using the current RDS certificate authorities.
  link: [RDS rotates the DB server certificate automatically](../facts/rds.md#rds-tls-server-certificate-auto-rotation)
rds-vpc-no-additional-cost
  claim: There is no additional cost to run a DB instance in a VPC.
  scope: DB instances in a VPC.
  link: [no additional cost](../facts/rds.md#rds-vpc-no-additional-cost)
rds-vs-ec2-application-optimization
  claim: Application optimization stays with the customer in all three models: on premises, on Amazon EC2 and on Amazon RDS.
  scope: Amazon RDS compared with a database on Amazon EC2 or on premises.
  link: [Application optimization](../facts/rds.md#rds-vs-ec2-application-optimization)
rds-vs-ec2-database-backups
  claim: Database backups are the customer's job on premises and on Amazon EC2, and AWS's job on Amazon RDS.
  scope: Amazon RDS compared with a database on Amazon EC2 or on premises.
  link: [Database backups](../facts/rds.md#rds-vs-ec2-database-backups)
rds-vs-ec2-database-software-patching
  claim: Database software patching is done by the customer on premises and on Amazon EC2, and by AWS on Amazon RDS.
  scope: Amazon RDS compared with a database on Amazon EC2 or on premises.
  link: [Database software patching](../facts/rds.md#rds-vs-ec2-database-software-patching)
rds-vs-ec2-high-availability
  claim: High availability is managed by the customer for a database on Amazon EC2 and by AWS for Amazon RDS.
  scope: Amazon RDS compared with a database on Amazon EC2 or on premises.
  link: [High availability](../facts/rds.md#rds-vs-ec2-high-availability)
rds-vs-ec2-os-patching
  claim: Operating system patching is done by the customer for a database on Amazon EC2 and by AWS for Amazon RDS.
  scope: Amazon RDS compared with a database on Amazon EC2 or on premises.
  link: [Operating system (OS) patching](../facts/rds.md#rds-vs-ec2-os-patching)
rds-wa-cross-region-primary-replica
  claim: For multi-Region designs, Well-Architected notes that with Amazon RDS (unlike DynamoDB global tables) you designate a primary read/write Region and read-only replica Regions.
  scope: AWS Well-Architected Framework guidance.
  link: [designate a primary (read/write) Region](../facts/rds.md#rds-wa-cross-region-primary-replica)
rds-wa-cross-region-replication-primary-writes
  claim: The Well-Architected reliability pillar lists Amazon RDS among managed data services with cross-Region replication; unlike DynamoDB global tables, such services need a primary Region for writes while other Regions hold read-only replicas.
  scope: multi-Region workloads.
  link: [designate a primary Region for writes](../facts/rds.md#rds-wa-cross-region-replication-primary-writes)
  link: [other Regions contain read-only replicas](../facts/rds.md#rds-wa-cross-region-replication-primary-writes)
rds-wa-managed-data-enable-cross-az
  claim: Well-Architected REL10-BP01 advises, for managed data services such as Amazon RDS, to study the service's replication and resilience capabilities and enable cross-AZ replication and failover if necessary.
  scope: AWS Well-Architected Framework guidance.
  link: [Enable cross-AZ replication and failover if necessary](../facts/rds.md#rds-wa-managed-data-enable-cross-az)
rds-wa-purpose-built-anti-pattern
  claim: The Well-Architected performance pillar lists as an anti-pattern sticking to one data store because the team already knows one particular type of database solution.
  scope: AWS Well-Architected Framework guidance.
  link: [You stick to one data store](../facts/rds.md#rds-wa-purpose-built-anti-pattern)
rds-wa-relational-acid
  claim: Well-Architected describes relational databases (Aurora, RDS, Redshift) as designed for ACID transactions, referential integrity and strong data consistency, used by many traditional applications, ERP, CRM and ecommerce.
  scope: AWS Well-Architected Framework guidance.
  link: [referential integrity and strong data consistency](../facts/rds.md#rds-wa-relational-acid)
rds-wa-relational-storage-upper-bounds
  claim: Well-Architected notes that relational databases have upper bounds on provisioned storage and often must be horizontally partitioned (sharded) when they reach these limits, while serverless databases such as DynamoDB scale dynamically.
  scope: AWS Well-Architected Framework guidance.
  link: [upper bounds on provisioned storage](../facts/rds.md#rds-wa-relational-storage-upper-bounds)
rds-zero-etl-what
  claim: An RDS zero-ETL integration is a fully managed way to make transactional data from an RDS database available in Amazon Redshift or an Amazon SageMaker AI lakehouse in near real time, for analytics and machine learning.
  scope: RDS zero-ETL integrations.
  link: [near real-time analytics and machine learning](../facts/rds.md#rds-zero-etl-what)
