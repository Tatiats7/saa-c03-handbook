import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
WP = "docs/whitepapers/latest/disaster-recovery-workloads-on-aws/"
BCP, TST = WP + "business-continuity-plan-bcp", WP + "testing-disaster-recovery"
R = "docs/wellarchitected/latest/reliability-pillar/"
B1, B2, B3, B4, R1, R2 = R + "rel_backing_up_data_identified_backups_data", R + "rel_backing_up_data_secured_backups_data", R + "rel_backing_up_data_automated_backups_data", R + "rel_backing_up_data_periodic_recovery_testing_data", R + "rel_planning_for_recovery_objective_defined_recovery", R + "rel_planning_for_recovery_disaster_recovery"
WA = dict(service="well-architected")
f = []
f.append(F("well-architected-rel09-bp01-identify-and-back-up-or-reproduce-data", "behavior",
 "REL09-BP01 says to understand and use the backup capabilities of the data services and resources in the workload, and to back up all data that needs it or be able to reproduce the data from sources.",
 "What does REL09-BP01 ask you to do about backups?",
 ["Understand and use the backup capabilities of the data services", "Most services provide capabilities to back up workload data"],
 [E(B1, "Understand and use the backup capabilities of the data services and resources used by the workload. Most services provide capabilities to back up workload data.")],
 scope="Well-Architected REL09-BP01", tier0=True, bullets=["2.2.S5"], **WA))
f.append(F("well-architected-rel09-bp01-reproducible-data-may-not-need-backup", "behavior",
 "Data that can be reproduced from other sources, such as through ElastiCache replica nodes or RDS read replicas, might not need a backup if those sources meet your RPO and RTO.",
 "When might you not need a backup of some data?",
 ["reproducing the data from other sources", "you might not require a backup"],
 [E(B1, "You might be able to meet data recovery needs by reproducing the data from other sources. For example, Amazon ElastiCache replica nodes or Amazon RDS read replicas could be used to reproduce data if the primary is lost. In cases where sources like this can be used to meet your Recovery Point Objective (RPO) and Recovery Time Objective (RTO), you might not require a backup.")],
 scope="Well-Architected REL09-BP01", bullets=["2.2.S5"], **WA))
f.append(F("well-architected-rel09-bp01-backup-frequency-depends-on-rpo", "behavior",
 "Creating backups of data sources is a periodic process and the frequency should depend on the RPO.",
 "What should decide how often data is backed up?",
 ["the frequency should depend on the RPO", "periodic process"],
 [E(B1, "Creating backups of data sources is a periodic process and the frequency should depend on the RPO.")],
 scope="Well-Architected REL09-BP01", tier0=True, bullets=["2.2.S5", "2.2.K4"], **WA))
f.append(F("well-architected-rel09-bp01-classify-data-by-criticality", "behavior",
 "Different data sets have different levels of criticality and therefore different resiliency requirements, so classify data sources by criticality; some data may need an RPO near zero while less critical data can tolerate a higher RPO.",
 "Why classify data sources by criticality before choosing backups?",
 ["different levels of criticality", "require a RPO near zero"],
 [E(B1, "Different data sets will have different levels of criticality for a workload, and therefore different requirements for resiliency. For example, some data might be critical and require a RPO near zero, while other data might be less critical and can tolerate a higher RPO and some data loss.")],
 scope="Well-Architected REL09-BP01", bullets=["2.2.S5"], **WA))
f.append(F("well-architected-rel09-bp01-recovery-time-must-fit-rto", "behavior",
 "When selecting a backup strategy, consider the time it takes to recover data; it depends on the type of backup or the complexity of the data reproduction mechanism and should fall within the workload's RTO.",
 "What must recovery time from a backup fit within?",
 ["consider the time it takes to recover data", "should fall within the RTO"],
 [E(B1, "When selecting a backup strategy, consider the time it takes to recover data. The time needed to recover data depends on the type of backup (in the case of a backup strategy), or the complexity of the data reproduction mechanism. This time should fall within the RTO for the workload.")],
 scope="Well-Architected REL09-BP01", bullets=["2.2.S5", "2.2.K4"], **WA))
f.append(F("well-architected-rel09-bp01-anti-pattern-no-rpo-or-frequency-misses-rpo", "behavior",
 "A common REL09-BP01 anti-pattern is having no defined RPO, or a backup frequency that cannot meet the RPO.",
 "Which RPO-related anti-pattern does REL09-BP01 name?",
 ["No defined RPO, or backup frequency cannot meet RPO", "anti-pattern"],
 [E(B1, "No defined RPO, or backup frequency cannot meet RPO.")],
 scope="Well-Architected REL09-BP01", rel="extended", bullets=["2.2.S5"], **WA))
f.append(F("well-architected-rel09-bp02-control-access-and-encrypt-backups", "behavior",
 "REL09-BP02 says to control and detect access to backups using authentication and authorization, to use encryption to prevent and detect compromise of backup data integrity, and to encrypt backups to protect the confidentiality and integrity of your data.",
 "What does REL09-BP02 require for backup security?",
 ["Control and detect access to backups using authentication and authorization", "Encrypt backups to protect the confidentiality and integrity of your data"],
 [E(B2, "Control and detect access to backups using authentication and authorization. Prevent and detect if data integrity of backups is compromised using encryption."),
  E(B2, "Encrypt backups to protect the confidentiality and integrity of your data.")],
 scope="Well-Architected REL09-BP02", tier0=True, bullets=["2.2.S5", "1.3.S1"], **WA))
f.append(F("well-architected-rel09-bp02-anti-patterns-immutability-security-domain", "behavior",
 "REL09-BP02 lists as anti-patterns not encrypting backups, not implementing immutability against deletion or tampering, using the same security domain for production and backup systems, and giving the same access to backups and restoration automation as to the data.",
 "Which backup security anti-patterns does REL09-BP02 name?",
 ["Not implementing immutability for protection against deletion or tampering", "Using the same security domain for production and backup systems"],
 [E(B2, "Not encrypting your backups."),
  E(B2, "Not implementing immutability for protection against deletion or tampering."),
  E(B2, "Using the same security domain for production and backup systems."),
  E(B2, "Having the same access to the backups and restoration automation as you do to the data.")],
 scope="Well-Architected REL09-BP02", tier0=True, bullets=["2.2.S5", "1.3.S1"], **WA))
f.append(F("well-architected-rel09-bp02-immutability-vault-lock-or-s3-object-lock", "behavior",
 "For cyber resilience, implement immutability with AWS Backup Vault Lock or S3 Object Lock to prevent backup data from being altered or deleted during its retention period, which protects against ransomware and malicious deletion.",
 "Which AWS features give immutable backups?",
 ["AWS Backup Vault Lock or Amazon S3 Object Lock", "protecting against ransomware and malicious deletion"],
 [E(B2, "Implement immutability using AWS Backup Vault Lock or Amazon S3 Object Lock to prevent backup data from being altered or deleted during its retention period, protecting against ransomware and malicious deletion.")],
 scope="Well-Architected REL09-BP02", tier0=True, bullets=["2.2.S5", "1.3.S1"], **WA))
f.append(F("well-architected-rel09-bp02-logical-isolation-lag-vault", "behavior",
 "For cyber resilience, establish logical isolation between production and backup environments with an AWS Backup logically air-gapped vault for critical systems, so that both environments are not compromised at once.",
 "Which AWS Backup feature separates backups from the production environment?",
 ["AWS Backup logically air-gapped vault for critical systems", "prevent compromise of both environments simultaneously"],
 [E(B2, "Establish logical isolation between production and backup environments with AWS Backup logically air-gapped vault for critical systems, creating separation that helps prevent compromise of both environments simultaneously.")],
 scope="Well-Architected REL09-BP02", tier0=True, bullets=["2.2.S5"], **WA))
f.append(F("well-architected-rel09-bp02-restore-testing-and-multi-party-approval", "behavior",
 "REL09-BP02 recommends validating backup integrity regularly with AWS Backup restore testing, and implementing AWS Backup multi-party approval for critical recovery operations so that multiple designated approvers must authorize them.",
 "Which AWS Backup features does REL09-BP02 recommend for validation and approval?",
 ["AWS Backup restore testing", "requiring authorization from multiple designated approvers"],
 [E(B2, "Validate backup integrity regularly using AWS Backup restore testing to verify that backups are not corrupted and can be successfully restored following a cyber incident."),
  E(B2, "Implement multi-party approval for critical recovery operations using AWS Backup multi-party approval to prevent unauthorized or malicious recovery attempts by requiring authorization from multiple designated approvers.")],
 scope="Well-Architected REL09-BP02", bullets=["2.2.S5", "1.3.K2"], **WA))
f.append(F("well-architected-rel09-bp02-rds-backups-encrypted-if-db-encrypted-ddb-always", "behavior",
 "For Amazon RDS, if you encrypt your databases then your backups are encrypted too, and DynamoDB backups are always encrypted.",
 "Are RDS and DynamoDB backups encrypted?",
 ["if you have chosen to encrypt your databases, then your backups are encrypted also", "DynamoDB backups are always encrypted"],
 [E(B2, "For Amazon RDS, if you have chosen to encrypt your databases, then your backups are encrypted also. DynamoDB backups are always encrypted.")],
 scope="Well-Architected REL09-BP02", bullets=["1.3.S1", "2.2.S5"], **WA))
f.append(F("well-architected-rel09-bp02-encrypted-source-gives-encrypted-backup", "behavior",
 "Use encryption on each of your data stores: if your source data is encrypted, the backup will also be encrypted.",
 "Is a backup of an encrypted data store also encrypted?",
 ["If your source data is encrypted, then the backup will also be encrypted", "Use encryption on each of your data stores"],
 [E(B2, "Use encryption on each of your data stores. If your source data is encrypted, then the backup will also be encrypted.")],
 scope="Well-Architected REL09-BP02", bullets=["1.3.S1", "2.2.S5"], **WA))
f.append(F("well-architected-rel09-bp03-automate-backups-by-rpo-schedule", "behavior",
 "REL09-BP03 says to configure backups to run automatically on a schedule informed by the RPO or by changes in the dataset: critical datasets with low data loss requirements are backed up frequently, less critical data less often.",
 "How should backup frequency be set when automating backups?",
 ["taken automatically based on a periodic schedule informed by the Recovery Point Objective (RPO)", "backed up automatically on a frequent basis"],
 [E(B3, "Configure backups to be taken automatically based on a periodic schedule informed by the Recovery Point Objective (RPO), or by changes in the dataset. Critical datasets with low data loss requirements need to be backed up automatically on a frequent basis, whereas less critical data where some loss is acceptable can be backed up less frequently.")],
 scope="Well-Architected REL09-BP03", tier0=True, bullets=["2.2.S5", "2.2.K4"], **WA))
f.append(F("well-architected-rel09-bp03-aws-backup-rds-five-minutes-s3-fifteen-minutes", "behavior",
 "AWS Backup can back up Amazon RDS instances almost continuously every five minutes and Amazon S3 objects almost continuously every fifteen minutes for point-in-time recovery.",
 "How close to continuous can AWS Backup get for RDS and S3?",
 ["almost continuously every five minutes", "almost continuously every fifteen minutes"],
 [E(B3, "AWS Backup can be used to create automated data backups of various AWS data sources. Amazon RDS instances can be backed up almost continuously every five minutes and Amazon S3 objects can be backed up almost continuously every fifteen minutes, providing for point-in-time recovery (PITR) to a specific point in time within the backup history.")],
 scope="AWS Backup continuous backups", tier0=True, bullets=["2.2.S5", "1.3.S5"], **WA))
f.append(F("well-architected-rel09-bp03-aws-backup-hourly-for-ebs-dynamodb-fsx", "behavior",
 "For other data sources such as EBS volumes, DynamoDB tables or FSx file systems, AWS Backup can run automated backups as frequently as every hour.",
 "How often can AWS Backup back up EBS volumes, DynamoDB tables and FSx file systems?",
 ["as frequently as every hour", "Amazon EBS volumes, Amazon DynamoDB tables, or Amazon FSx file systems"],
 [E(B3, "For other AWS data sources, such as Amazon EBS volumes, Amazon DynamoDB tables, or Amazon FSx file systems, AWS Backup can run automated backup as frequently as every hour.")],
 scope="AWS Backup snapshot backups", bullets=["2.2.S5", "1.3.S5"], **WA))
f.append(F("well-architected-rel09-bp03-backup-plan-rules-frequency-informed-by-rpo", "behavior",
 "In AWS Backup, create backup plan rules that define the resources to back up and the frequency of backups, and base that frequency on the RPO you established.",
 "How do you tie an AWS Backup plan to the RPO?",
 ["create rules which define the resources to backup", "This frequency should be informed by the RPO"],
 [E(B3, "Using backup plans in AWS Backup, create rules which define the resources to backup, and the frequency at which these backups should be created. This frequency should be informed by the RPO established in Step 2.")],
 scope="Well-Architected REL09-BP03", bullets=["4.3.S1", "2.2.K4"], **WA))
f.append(F("well-architected-rel09-bp04-recover-periodically-to-verify-rto-rpo", "behavior",
 "REL09-BP04 says to validate that your backup process meets your RTO and RPO by performing a recovery test, and to periodically restore backups to a new location and run tests to verify the integrity of the data.",
 "Why periodically restore backups?",
 ["performing a recovery test", "Periodically restore backups to a new location"],
 [E(B4, "Validate that your backup process implementation meets your Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) by performing a recovery test."),
  E(B4, "Periodically restore backups to a new location and run tests to verify the integrity of the data.")],
 scope="Well-Architected REL09-BP04", tier0=True, bullets=["2.2.S5", "1.3.K2"], **WA))
f.append(F("well-architected-rel09-bp04-anti-patterns-assuming-backup-exists-or-restorable", "behavior",
 "REL09-BP04 names as anti-patterns assuming that a backup exists, assuming that a backup is fully operational and data can be recovered from it, and assuming that restore time falls within the RTO.",
 "Which assumptions about backups does REL09-BP04 warn against?",
 ["Assuming that a backup exists", "Assuming that the time to restore or recover data from a backup falls within the RTO"],
 [E(B4, "Assuming that a backup exists."),
  E(B4, "Assuming that the backup of a system is fully operational and that data can be recovered from it."),
  E(B4, "Assuming that the time to restore or recover data from a backup falls within the RTO for the workload.")],
 scope="Well-Architected REL09-BP04", rel="extended", bullets=["2.2.S5"], **WA))
f.append(F("well-architected-rel13-bp01-define-rto-and-rpo-for-each-workload", "behavior",
 "REL13-BP01 says to define a Recovery Time Objective (RTO) and a Recovery Point Objective (RPO) for each workload to guide how you respond and recover from failures.",
 "What does REL13-BP01 ask you to define for each workload?",
 ["define a Recovery Time Objective (RTO) and Recovery Point Objective (RPO) for each workload", "guide how you respond and recover from failures"],
 [E(R1, "In order to guide how you respond and recover from failures, define a Recovery Time Objective (RTO) and Recovery Point Objective (RPO) for each workload.")],
 scope="Well-Architected REL13-BP01", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-rel13-bp01-too-strict-objectives-cost-more", "behavior",
 "Selecting recovery objectives that are more stringent than the actual business objectives forces recovery implementations that are costlier and more complicated than the workload needs.",
 "What is the cost of recovery objectives that are stricter than the business needs?",
 ["more stringent than actual business objectives", "costlier and more complicated than what the workload needs"],
 [E(R1, "You select recovery objectives that are more stringent than actual business objectives. This forces recovery implementations that are costlier and more complicated than what the workload needs.")],
 scope="Well-Architected REL13-BP01", tier0=True, bullets=["2.2.K4", "4.3.S1"], **WA))
f.append(F("well-architected-rel13-bp02-strategies-increasing-cost-complexity-decreasing-rto-rpo", "behavior",
 "The multi-Region DR strategies are listed in increasing order of cost and complexity, and decreasing order of RTO and RPO.",
 "How do the DR strategies order by cost and by RTO and RPO?",
 ["increasing order of cost and complexity", "decreasing order of RTO and RPO"],
 [E(R2, "They are listed in increasing order of cost and complexity, and decreasing order of RTO and RPO.")],
 scope="Well-Architected REL13-BP02", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-rel13-bp02-backup-restore-rpo-hours-rto-24-hours", "behavior",
 "In REL13-BP02, backup and restore has an RPO in hours and an RTO in 24 hours or less: you back up your data and applications into the recovery Region.",
 "What RPO and RTO does the backup and restore strategy target?",
 ["RPO in hours, RTO in 24 hours or less", "Back up your data and applications into the recovery Region"],
 [E(R2, "Backup and restore (RPO in hours, RTO in 24 hours or less): Back up your data and applications into the recovery Region.")],
 scope="Well-Architected REL13-BP02", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-rel13-bp02-pilot-light-rpo-minutes-rto-tens-of-minutes", "behavior",
 "In REL13-BP02, pilot light has an RPO in minutes and an RTO in tens of minutes: you provision a copy of your core workload infrastructure in the recovery Region.",
 "What RPO and RTO does the pilot light strategy target?",
 ["RPO in minutes, RTO in tens of minutes", "Provision a copy of your core workload infrastructure"],
 [E(R2, "Pilot light (RPO in minutes, RTO in tens of minutes): Provision a copy of your core workload infrastructure in the recovery Region.")],
 scope="Well-Architected REL13-BP02", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-rel13-bp02-warm-standby-rpo-seconds-rto-minutes", "behavior",
 "In REL13-BP02, warm standby has an RPO in seconds and an RTO in minutes: you maintain a scaled-down but fully functional version of your workload always running in the recovery Region.",
 "What RPO and RTO does the warm standby strategy target?",
 ["RPO in seconds, RTO in minutes", "scaled-down but fully functional version of your workload always running"],
 [E(R2, "Warm standby (RPO in seconds, RTO in minutes): Maintain a scaled-down but fully functional version of your workload always running in the recovery Region.")],
 scope="Well-Architected REL13-BP02", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-rel13-bp02-multi-region-active-active-rpo-near-zero", "behavior",
 "In REL13-BP02, multi-Region (multi-site) active-active has an RPO near zero and an RTO potentially zero: the workload is deployed to, and actively serves traffic from, multiple AWS Regions.",
 "What RPO and RTO does multi-site active-active target?",
 ["RPO near zero, RTO potentially zero", "actively serving traffic from, multiple AWS Regions"],
 [E(R2, "Multi-Region (multi-site) active-active (RPO near zero, RTO potentially zero): Your workload is deployed to, and actively serving traffic from, multiple AWS Regions.")],
 scope="Well-Architected REL13-BP02", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-rel13-bp02-replication-not-protect-corruption-without-pitr", "behavior",
 "Data replication is useful for synchronization and protects against some types of disaster, but it will not protect against data corruption or destruction unless the solution also includes point-in-time recovery.",
 "Does data replication protect against data corruption?",
 ["it will not protect you against data corruption or destruction", "options for point-in-time recovery"],
 [E(R2, "Data replication is useful for data synchronization and will protect you against some types of disaster, but it will not protect you against data corruption or destruction unless your solution also includes options for point-in-time recovery.")],
 scope="Well-Architected REL13-BP02", tier0=True, bullets=["2.2.S5", "2.2.K4"], **WA))
f.append(F("well-architected-rel13-bp02-backup-restore-least-complex-higher-rto-rpo", "behavior",
 "Backup and restore is the least complex DR strategy to implement, but it needs more time and effort to restore the workload, leading to higher RTO and RPO.",
 "What is the trade-off of backup and restore compared with other DR strategies?",
 ["least complex strategy to implement", "leading to higher RTO and RPO"],
 [E(R2, "Backup and restore is the least complex strategy to implement, but will require more time and effort to restore the workload, leading to higher RTO and RPO.")],
 scope="Well-Architected REL13-BP02", tier0=True, bullets=["2.2.K4"], **WA))
f.append(F("well-architected-rel13-bp02-choose-strategy-tradeoff-avoid-too-stringent", "behavior",
 "Choosing a DR strategy is a trade-off between reducing downtime and data loss (RTO and RPO) and the cost and complexity of the strategy, and you should avoid a strategy more stringent than needed, as that incurs unnecessary cost.",
 "How should you balance RTO, RPO and cost when choosing a DR strategy?",
 ["trade-off between reducing downtime and data loss", "more stringent than it needs to be"],
 [E(R2, "Choosing a DR strategy is a trade-off between reducing downtime and data loss (RTO and RPO) and the cost and complexity of implementing the strategy. You should avoid implementing a strategy that is more stringent than it needs to be, as this incurs unnecessary costs.")],
 scope="Well-Architected REL13-BP02", tier0=True, bullets=["2.2.K4", "4.3.S1"], **WA))
f.append(F("well-architected-rel13-bp02-multi-az-mitigates-fires-floods-power-outages", "behavior",
 "A DR strategy across multiple Availability Zones within one AWS Region can mitigate disaster events such as fires, floods and major power outages; a multi-Region strategy is for events that stop the workload running in a whole Region.",
 "Which disasters does a multi-AZ DR strategy cover?",
 ["multiple Availability Zones (AZs) within a single AWS Region", "fires, floods, and major power outages"],
 [E(R2, "A DR strategy across multiple Availability Zones (AZs) within a single AWS Region, can provide mitigation against disaster events like fires, floods, and major power outages. If it is a requirement to implement protection against an unlikely event that prevents your workload from being able to run in a given AWS Region, you can use a DR strategy that uses multiple Regions.")],
 scope="Well-Architected REL13-BP02", bullets=["2.2.K4"], **WA))
f.append(F("well-architected-rel13-bp02-elastic-disaster-recovery-cheaper-than-warm-standby", "behavior",
 "When cost is a concern and you want RPO and RTO like warm standby, you could consider cloud native solutions like AWS Elastic Disaster Recovery, which take the pilot light approach and offer improved RPO and RTO targets.",
 "Which service gives warm-standby-like RPO and RTO at pilot light cost?",
 ["AWS Elastic Disaster Recovery", "take the pilot light approach and offer improved RPO and RTO targets"],
 [E(R2, "When cost is a concern, and you wish to achieve a similar RPO and RTO objectives as defined in the warm standby strategy, you could consider cloud native solutions, like AWS Elastic Disaster Recovery, that take the pilot light approach and offer improved RPO and RTO targets.")],
 scope="Well-Architected REL13-BP02", bullets=["2.2.K4", "4.3.S1"], **WA))
f.append(F("well-architected-dr-bcp-cost-higher-than-loss-do-not-implement", "behavior",
 "If the cost of the recovery strategy is higher than the cost of the failure or loss, the recovery option should not be put in place unless there is a secondary driver such as regulatory requirements.",
 "When is a recovery option not worth its cost?",
 ["higher than the cost of the failure or loss", "secondary driver such as regulatory requirements"],
 [E(BCP, "If the cost of the recovery strategy is higher than the cost of the failure or loss, the recovery option should not be put in place unless there is a secondary driver such as regulatory requirements. Consider recovery strategies of varying cost when making this assessment.")],
 scope="disaster recovery strategy selection", tier0=True, bullets=["2.2.K4", "4.3.S1"], **WA))
f.append(F("well-architected-dr-bcp-multi-az-may-meet-risk-needs", "behavior",
 "A multi-AZ architecture within an AWS Region may already meet much of your risk mitigation needs, because Availability Zones are designed with meaningful distance between them so most common disasters only impact one zone.",
 "Does a multi-AZ architecture already cover most common disasters?",
 ["a multi-AZ architecture within an AWS Region may already meet much of your risk mitigation needs", "most common disasters should only impact one zone"],
 [E(BCP, "Remember that Availability Zones within an AWS Region are already designed with meaningful distance between them, and careful planning of location, such that most common disasters should only impact one zone and not the others. Therefore, a multi-AZ architecture within an AWS Region may already meet much of your risk mitigation needs.")],
 scope="disaster recovery planning", bullets=["2.2.K4"], **WA))
f.append(F("well-architected-dr-test-failover-regularly-only-tested-recovery-works", "behavior",
 "Test your disaster recovery implementation and regularly test failover to the DR Region to ensure RTO and RPO are met; the only error recovery that works is the path you test frequently.",
 "Why test failover to the DR Region regularly?",
 ["regularly test failover to your workload's DR Region", "the only error recovery that works is the path you test frequently"],
 [E(TST, "Test disaster recovery implementation to validate the implementation and regularly test failover to your workload’s DR Region to ensure that RTO and RPO are met."),
  E(TST, "Our experience has shown that the only error recovery that works is the path you test frequently.")],
 scope="disaster recovery testing", bullets=["2.2.K4", "2.2.S5"], **WA))
dump("facts-behavior-23.json", f[:19])
dump("facts-behavior-24.json", f[19:])
