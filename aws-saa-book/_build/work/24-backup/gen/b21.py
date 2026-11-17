import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
WP = "docs/whitepapers/latest/disaster-recovery-workloads-on-aws/"
OPT, BCP, TST = WP + "disaster-recovery-options-in-the-cloud", WP + "business-continuity-plan-bcp", WP + "testing-disaster-recovery"
R = "docs/wellarchitected/latest/reliability-pillar/"
B1, B2, B3, B4, R1, R2 = R + "rel_backing_up_data_identified_backups_data", R + "rel_backing_up_data_secured_backups_data", R + "rel_backing_up_data_automated_backups_data", R + "rel_backing_up_data_periodic_recovery_testing_data", R + "rel_planning_for_recovery_objective_defined_recovery", R + "rel_planning_for_recovery_disaster_recovery"
WA = dict(service="well-architected")
f = []
f.append(F("well-architected-dr-four-strategies-low-cost-to-multi-region", "behavior",
 "AWS groups disaster recovery strategies into four approaches, ranging from the low cost and low complexity of making backups to more complex strategies using multiple active Regions.",
 "How many DR approaches does AWS describe and what is the range from cheapest to most complex?",
 ["four approaches", "low cost and low complexity of making backups"],
 [E(OPT, "Disaster recovery strategies available to you within AWS can be broadly categorized into four approaches, ranging from the low cost and low complexity of making backups to more complex strategies using multiple active Regions.")],
 scope="AWS disaster recovery strategies", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-backup-restore-may-suffice-single-data-center", "behavior",
 "For a disaster that is the disruption or loss of one physical data center for a well-architected, highly available workload, a backup and restore approach may be all you need; if a disaster means loss of a Region or regulation requires it, consider Pilot Light, Warm Standby or Multi-Site Active/Active.",
 "When is backup and restore enough, and when do you need pilot light, warm standby or multi-site?",
 ["you may only require a backup and restore approach", "Pilot Light, Warm Standby, or Multi-Site Active/Active"],
 [E(OPT, "For a disaster event based on disruption or loss of one physical data center for a well-architected, highly available workload, you may only require a backup and restore approach to disaster recovery. If your definition of a disaster goes beyond the disruption or loss of a physical data center to that of a Region or if you are subject to regulatory requirements that require it, then you should consider Pilot Light, Warm Standby, or Multi-Site Active/Active.")],
 scope="choosing a DR strategy", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-backup-restore-suitable-for-data-loss-corruption", "behavior",
 "Backup and restore is a suitable approach for mitigating data loss or corruption, and it can also mitigate a regional disaster by replicating data to other Regions or the lack of redundancy of single-AZ workloads.",
 "What does the backup and restore DR strategy protect against?",
 ["suitable approach for mitigating against data loss or corruption", "replicating data to other AWS Regions"],
 [E(OPT, "Backup and restore is a suitable approach for mitigating against data loss or corruption. This approach can also be used to mitigate against a regional disaster by replicating data to other AWS Regions, or to mitigate lack of redundancy for workloads deployed to a single Availability Zone.")],
 scope="backup and restore strategy", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-backup-restore-redeploy-infrastructure-with-iac", "behavior",
 "With backup and restore you must redeploy the infrastructure, configuration and application code in the recovery Region, and you should always use infrastructure as code so redeployment is quick and error-free; without it, restoring can take longer and possibly exceed your RTO.",
 "What does backup and restore need besides the data, and why use infrastructure as code?",
 ["you must redeploy the infrastructure, configuration, and application code", "always deploy using infrastructure as code (IaC)"],
 [E(OPT, "In addition to data, you must redeploy the infrastructure, configuration, and application code in the recovery Region. To enable infrastructure to be redeployed quickly without errors, you should always deploy using infrastructure as code (IaC) using services such as AWS CloudFormation or the AWS Cloud Development Kit (AWS CDK). Without IaC, it may be complex to restore workloads in the recovery Region, which will lead to increased recovery times and possibly exceed your RTO.")],
 scope="backup and restore strategy", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-backup-frequency-sets-recovery-point-rpo", "behavior",
 "How often you run backups determines the recovery point you can achieve, which should align to your RPO, and the backup should let you restore to the point in time it was taken.",
 "What decides the recovery point you can achieve with backups?",
 ["How often you run your backup will determine your achievable recovery point", "should align to meet your RPO"],
 [E(OPT, "Your workload data will require a backup strategy that runs periodically or is continuous. How often you run your backup will determine your achievable recovery point (which should align to meet your RPO). The backup should also offer a way to restore it to the point in time in which it was taken.")],
 scope="backup frequency and RPO", tier0=True, bullets=["2.2.K4", "1.3.S5"], **WA))
f.append(F("well-architected-dr-aws-backup-central-location-and-cross-region-copy", "capability",
 "AWS Backup provides a centralized location to configure, schedule and monitor backup capabilities for services such as EBS, EC2, RDS, DynamoDB, EFS, Storage Gateway and FSx, and supports copying backups across Regions, such as to a disaster recovery Region.",
 "What does AWS Backup give a backup-and-restore DR strategy?",
 ["a centralized location to configure, schedule, and monitor AWS backup capabilities", "copying backups across Regions, such as to a disaster recovery Region"],
 [E(OPT, "AWS Backup provides a centralized location to configure, schedule, and monitor AWS backup capabilities for the following services and resources:"),
  E(OPT, "AWS Backup supports copying backups across Regions, such as to a disaster recovery Region.")],
 scope="backup and restore strategy", tier0=True, bullets=["2.2.K4", "4.1.K5"], **WA))
f.append(F("well-architected-dr-cross-account-backup-protects-insider-account-compromise", "capability",
 "The AWS Backup cross-account backup capability helps protect from disaster events that include insider threats or account compromise.",
 "Which disaster events does a cross-account backup copy protect against?",
 ["insider threats or account compromise", "cross-account backup capability"],
 [E(OPT, "Or, you can use AWS Backup to copy backups across accounts and to other AWS Regions. The cross-account backup capability helps protect from disaster events that include insider threats or account compromise.")],
 scope="AWS Backup cross-account copy", tier0=True, bullets=["2.2.K4", "1.3.S5", "2.2.S5"], **WA))
f.append(F("well-architected-dr-continuous-replication-shortest-backup-time-not-protect-corruption", "behavior",
 "Continuous replication of data gives the shortest time (near zero) to back up your data, but may not protect against data corruption or malicious attack, such as unauthorized deletion, as well as point-in-time backups do.",
 "Is continuous replication a substitute for point-in-time backups?",
 ["shortest time (near zero) to back up your data", "may not protect against disaster events such as data corruption or malicious attack"],
 [E(OPT, "Continuous replication of data has the advantage of being the shortest time (near zero) to back up your data, but may not protect against disaster events such as data corruption or malicious attack (such as unauthorized data deletion) as well as point-in-time backups.")],
 scope="replication versus point-in-time backup", tier0=True, bullets=["2.2.S5", "2.2.K4"], **WA))
f.append(F("well-architected-dr-replication-needs-versioning-or-pitr-against-corruption", "behavior",
 "Continuous data replication protects against some types of disaster, but may not protect against data corruption or destruction unless the strategy also includes versioning of stored data or point-in-time recovery.",
 "What must replication be combined with to protect against data corruption?",
 ["may not protect you against data corruption or destruction", "versioning of stored data or options for point-in-time recovery"],
 [E(OPT, "Continuous data replication protects you against some types of disaster, but it may not protect you against data corruption or destruction unless your strategy also includes versioning of stored data or options for point-in-time recovery.")],
 scope="pilot light and replication", tier0=True, bullets=["2.2.S5", "2.2.K4"], **WA))
f.append(F("well-architected-dr-s3-versioning-protects-deletion-modification-human-error", "behavior",
 "S3 object versioning protects data from deletion or modification by retaining the original version before the action, and it can mitigate human-error disasters.",
 "How does S3 versioning help in disaster recovery?",
 ["retaining the original version before the action", "human-error type disasters"],
 [E(OPT, "Object versioning protects your data in S3 from the consequences of deletion or modification actions by retaining the original version before the action. Object versioning can be a useful mitigation for human-error type disasters.")],
 scope="S3 versioning", bullets=["2.2.S5", "2.2.K4"], **WA))
f.append(F("well-architected-dr-s3-replication-delete-marker-source-only-by-default", "default",
 "When S3 replication backs up data to a DR Region, then by default when an object is deleted in the source bucket Amazon S3 adds a delete marker in the source bucket only, which protects data in the DR Region from malicious deletions in the source Region.",
 "Does deleting an object in the source bucket also delete it in the S3 replication destination by default?",
 ["adds a delete marker in the source bucket only", "protects data in the DR Region from malicious deletions"],
 [E(OPT, "If you are using S3 replication to back up data to your DR region, then, by default, when an object is deleted in the source bucket, Amazon S3 adds a delete marker in the source bucket only. This approach protects data in the DR Region from malicious deletions in the source Region.")],
 scope="S3 replication to a DR Region", dm="default", tier0=True, bullets=["2.2.S5", "2.2.K4"], **WA))
f.append(F("well-architected-dr-restore-is-control-plane-test-restore-periodically", "behavior",
 "Implementing a scheduled periodic data restore is a good idea because restoring from backup is a control plane operation; if that operation were unavailable during a disaster you would still have operable data stores created from a recent backup.",
 "Why schedule periodic restores into the DR Region?",
 ["data restore from backup is a control plane operation", "operable data stores created from a recent backup"],
 [E(OPT, "Implementing a scheduled periodic data restore is a good idea as data restore from backup is a control plane operation. If this operation was not available during a disaster, you would still have operable data stores created from a recent backup.")],
 scope="backup and restore strategy", rel="extended", bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-backup-strategy-must-include-testing", "behavior",
 "Your backup strategy must include testing your backups.",
 "Does a backup strategy need to include testing?",
 ["must include testing your backups", "Your backup strategy"],
 [E(OPT, "Your backup strategy must include testing your backups. See the Testing Disaster Recovery section for more information.")],
 scope="backup strategy", bullets=["2.2.S5", "2.2.K4"], **WA))
f.append(F("well-architected-dr-test-regularly-so-you-trust-invoking-it", "behavior",
 "It is critical to regularly assess and test your disaster recovery strategy so that you have confidence in invoking it if it becomes necessary.",
 "Why test a disaster recovery strategy regularly?",
 ["regularly assess and test your disaster recovery strategy", "confidence in invoking it"],
 [E(OPT, "It is critical to regularly assess and test your disaster recovery strategy so that you have confidence in invoking it, should it become necessary.")],
 scope="disaster recovery strategy", bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-data-plane-only-failover-higher-availability", "behavior",
 "For maximum resiliency you should use only data plane operations in a failover operation, because data planes typically have higher availability design goals than control planes.",
 "Why should a failover use data plane operations only?",
 ["use only data plane operations as part of your failover operation", "higher availability design goals than the control planes"],
 [E(OPT, "For maximum resiliency, you should use only data plane operations as part of your failover operation. This is because the data planes typically have higher availability design goals than the control planes.")],
 scope="failover design", rel="extended", bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-pilot-light-definition-core-always-on-servers-off", "behavior",
 "With pilot light you replicate your data to another Region and provision a copy of your core workload infrastructure; resources for data replication and backup are always on, while application servers are loaded with code and configuration but switched off until testing or failover.",
 "What is the pilot light DR approach?",
 ["replicate your data from one Region to another", "switched off"],
 [E(OPT, "With the pilot light approach, you replicate your data from one Region to another and provision a copy of your core workload infrastructure. Resources required to support data replication and backup, such as databases and object storage, are always on. Other elements, such as application servers, are loaded with application code and configurations, but are \"switched off\" and are only used during testing or when disaster recovery failover is invoked.")],
 scope="pilot light strategy", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-warm-standby-scaled-down-always-on-lower-recovery-time", "behavior",
 "Warm standby keeps a scaled down but fully functional copy of the production environment in another Region, which extends pilot light and decreases recovery time because the workload is always on in another Region.",
 "What is the warm standby DR approach and how does it compare with pilot light on recovery time?",
 ["scaled down, but fully functional, copy of your production environment", "decreases the time to recovery"],
 [E(OPT, "The warm standby approach involves ensuring that there is a scaled down, but fully functional, copy of your production environment in another Region. This approach extends the pilot light concept and decreases the time to recovery because your workload is always-on in another Region.")],
 scope="warm standby strategy", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-pilot-light-vs-warm-standby-handle-traffic-immediately", "behavior",
 "Pilot light cannot process requests without additional action first, whereas warm standby can handle traffic at reduced capacity immediately.",
 "What is the difference between pilot light and warm standby?",
 ["pilot light cannot process requests without additional action taken first", "warm standby can handle traffic (at reduced capacity levels) immediately"],
 [E(R2, "The distinction is that pilot light cannot process requests without additional action taken first, while warm standby can handle traffic (at reduced capacity levels) immediately.") if False else E(R2, "The distinction is that pilot light cannot process requests without additional action taken first, while warm standby can handle traffic (at reduced capacity levels) immediately.")],
 scope="pilot light versus warm standby", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-multi-site-most-complex-costly-near-zero-recovery-time", "behavior",
 "Multi-site active/active is the most complex and costly DR approach, but it can reduce recovery time to near zero for most disasters; data corruption may still need backups, which usually gives a non-zero recovery point.",
 "How do cost and recovery time compare for multi-site active/active, and what does it not solve?",
 ["most complex and costly approach to disaster recovery", "reduce your recovery time to near zero"],
 [E(OPT, "This approach is the most complex and costly approach to disaster recovery, but it can reduce your recovery time to near zero for most disasters with the correct technology choices and implementation (however data corruption may need to rely on backups, which usually results in a non-zero recovery point).")],
 scope="multi-site active/active strategy", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-warm-standby-cheaper-simpler-than-full-active-active", "behavior",
 "If you do not want to use both Regions to handle user traffic, warm standby is a more economical and operationally less complex approach than a full second environment run active/active.",
 "When is warm standby preferred over multi-site active/active?",
 ["Warm Standby offers a more economical and operationally less complex approach", "do not want to use both Regions to handle user traffic"],
 [E(OPT, "Alternatively, if you do not want to use both Regions to handle user traffic, then Warm Standby offers a more economical and operationally less complex approach.")],
 scope="warm standby versus multi-site", bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-multi-site-backup-still-required-data-disaster-nonzero", "behavior",
 "Even with multi-site active/active, backup and recovery are still required and should be tested regularly, because recovery times for a data disaster such as corruption or deletion will always be greater than zero and the recovery point is always before the disaster was discovered.",
 "Does multi-site active/active remove the need for backups?",
 ["Backup and recovery are still required and should be tested regularly", "will always be greater than zero"],
 [E(OPT, "Testing for a data disaster is also required. Backup and recovery are still required and should be tested regularly. It should also be noted that recovery times for a data disaster involving data corruption, deletion, or obfuscation will always be greater than zero and the recovery point will always be at some point before the disaster was discovered.")],
 scope="multi-site active/active strategy", tier0=True, bullets=["2.2.S5", "2.2.K4"], **WA))
f.append(F("well-architected-dr-pilot-light-minimizes-ongoing-cost", "behavior",
 "A pilot light approach minimizes the ongoing cost of disaster recovery by minimizing the active resources, and simplifies recovery because the core infrastructure requirements are already in place.",
 "Why is pilot light cheap to run?",
 ["minimizes the ongoing cost of disaster recovery", "core infrastructure requirements are all in place"],
 [E(OPT, "A pilot light approach minimizes the ongoing cost of disaster recovery by minimizing the active resources, and simplifies recovery at the time of a disaster because the core infrastructure requirements are all in place.")],
 scope="pilot light strategy", bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-elastic-disaster-recovery-pilot-light-block-level-replication", "capability",
 "AWS Elastic Disaster Recovery continuously replicates server-hosted applications and databases from any source into AWS using block-level replication, and uses the pilot light strategy with switched-off resources in a staging area VPC.",
 "What is AWS Elastic Disaster Recovery and which DR strategy does it use?",
 ["continuously replicates server-hosted applications", "uses the Pilot Light strategy"],
 [E(OPT, "AWS Elastic Disaster Recovery (DRS) continuously replicates server-hosted applications and server- hosted databases from any source into AWS using block-level replication of the underlying server."),
  E(OPT, "Elastic Disaster Recovery uses the Pilot Light strategy, maintaining a copy of data and “switched-off” resources in an Amazon Virtual Private Cloud (Amazon VPC) used as a staging area.")],
 scope="AWS Elastic Disaster Recovery", tier0=True, bullets=["2.2.K4"], **WA))
dump("facts-behavior-21.json", f[:12])
dump("facts-behavior-22.json", f[12:])
