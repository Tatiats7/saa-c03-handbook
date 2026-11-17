import sys
sys.path.insert(0, "aws-saa-book/_build/work/23-efs-fsx")
from mk import f, emit

FAQ = "www/efs/faq"; R = "efs/efs-replication"; CR = "efs/create-replication"; FO = "efs/replication-fail-over"; XA = "efs/cross-account-replication"
EN = "efs/encryption-at-rest"; AP = "efs/efs-access-points"; IAM = "efs/iam-access-control-nfs-efs"; BPA = "efs/access-control-block-public-access"
F = []
F.append(f("efs-replication-automatic-transparent-data-and-metadata", "behavior",
  "When you enable replication, Amazon EFS automatically and transparently replicates the data and metadata of the source file system to a destination file system.",
  "What does EFS replication copy to the destination file system?",
  [(R, "When you enable replication on an EFS file system, Amazon EFS automatically and transparently replicates the data and metadata on the source file system to a destination file system.")],
  ["automatically and transparently replicates", "data and metadata on the source file system"], "EFS replication", "2.2.K11", tier0=True))
F.append(f("efs-replication-destination-new-or-existing-region-of-choice", "capability",
  "EFS Replication copies your file system data into a new or existing file system in the Region of your choice, transferring only incremental changes.",
  "Where does EFS Replication copy a file system, and how are changes sent?",
  [(FAQ, "Amazon EFS Replication copies your file system data into a new or existing file system in the Region of your choice. It keeps the two file systems synchronized by automatically transferring only incremental changes without requiring additional infrastructure or a custom process.")],
  ["new or existing file system", "only incremental changes"], "EFS replication", "2.2.K11", tier0=True))
F.append(f("efs-replication-rpo-rto-minutes", "sla",
  "EFS replication is continual and designed to provide a recovery point objective (RPO) and a recovery time objective (RTO) of minutes.",
  "What recovery point and recovery time objectives does EFS replication target?",
  [("efs/features", "Replication is continual and designed to provide a recovery point objective (RPO) and a recovery time objective (RTO) of minutes.")],
  ["objective (RTO) of minutes", "Replication is continual"], "EFS replication", "2.2.K11", tier0=True))
F.append(f("efs-replication-rpo-15-minutes-most-file-systems", "sla",
  "After the initial replication finishes, Amazon EFS maintains a recovery point objective (RPO) of 15 minutes for most file systems.",
  "What RPO does EFS replication maintain after the initial sync?",
  [(R, "After the initial replication is finished, Amazon EFS maintains a Recovery Point Objective (RPO) of 15 minutes for most file systems.")],
  ["RPO) of 15 minutes", "for most file systems"], "EFS replication, after initial sync", "2.2.K11", dm="", tier0=True))
F.append(f("efs-replication-rpo-longer-large-busy-sources", "restriction",
  "If the source file system has files that change very frequently and has either more than 100 million files or files larger than 100 GB, replication may take longer than 15 minutes.",
  "When can EFS replication take longer than 15 minutes?",
  [(R, "However, if the source file system has files that change very frequently and has either more than 100 million files or files that are larger than 100 GB, replication may take longer than 15 minutes.")],
  ["more than 100 million files", "larger than 100 GB", "longer than 15 minutes"], "EFS replication", "2.2.K11", rel="extended"))
F.append(f("efs-replication-initial-sync-before-replica-accessible", "behavior",
  "Replicated data is accessible in the destination file system only after the initial sync completes, and how long that takes depends on the size of the source and the number of files.",
  "When is replicated data available in the destination EFS file system?",
  [(R, "Replicated data is accessible in the destination file system only after the initial sync completes. The amount of time that the initial sync takes to finish depends on factors such as the size of the source file system and the number of files in it.")],
  ["only after the initial sync completes", "size of the source file system"], "EFS replication", "2.2.K11", rel="extended"))
F.append(f("efs-replication-not-point-in-time-consistent", "restriction",
  "EFS replication is not point-in-time consistent: changes are transferred based on the last synced time, and changes made after that time may not be replicated.",
  "Is an EFS replica point-in-time consistent?",
  [(R, "Changes made to the source file system are not transferred to the destination file system in a point-in-time consistent manner."),
   (FAQ, "No. EFS Replication doesn't provide point-in-time consistent replication.")],
  ["point-in-time consistent manner", "doesn't provide point-in-time consistent replication"],
  "EFS replication", "2.2.K11", tier0=True))
F.append(f("efs-replication-destination-read-only-while-replicating", "behavior",
  "The destination file system of EFS replication is read-only while replication is enabled, and applications can use it in read-only mode for low-latency cross-Region access.",
  "Can you write to the replica of an EFS file system while replication is on?",
  [(CR, "Amazon EFS automatically creates a new file system and copies the data and metadata on the source file system to a new read-only destination file system in the AWS Region that you choose."),
   (FAQ, "While EFS Replication is enabled, your applications can use the replica file system in read-only mode for low network latency cross-Region access.")],
  ["new read-only destination file system", "use the replica file system in read-only mode"], "EFS replication", "2.2.K11", tier0=True))
F.append(f("efs-replication-destination-faq-region-or-az-of-choice", "capability",
  "You can use EFS Replication to replicate your file system to a Region or Availability Zone of your choice, without managing additional infrastructure or custom processes.",
  "Can an EFS file system replicate to a One Zone destination or another Region?",
  [(FAQ, "Use EFS Replication to replicate your file system to a Region or Availability Zone (AZ) of your choice without having to manage additional infrastructure or custom processes.")],
  ["Region or Availability Zone (AZ) of your choice", "without having to manage additional infrastructure"], "EFS replication", "2.2.K11", rel="extended"))
F.append(f("efs-replication-failover-delete-configuration-replica-writeable", "behavior",
  "To fail over to the replica file system you delete its replication configuration; after the configuration is deleted the replica becomes writeable and you can use it in your application workflow.",
  "How do you fail over to an EFS replica?",
  [(FO, "In the event of a disaster or when performing game day exercises, you can fail over to your replica file system by deleting its replication configuration. After the replication configuration is deleted, the replica becomes writeable and you can start using it in your application workflow.")],
  ["by deleting its replication configuration", "the replica becomes writeable"], "EFS replication failover", "2.2.K11", tier0=True))
F.append(f("efs-replication-failback-discard-or-preserve-changes", "behavior",
  "During failback you can choose to discard the changes made to the replica during failover, or preserve them by copying them back to the primary file system.",
  "What choices do you have when failing back to the primary EFS file system?",
  [(FO, "During the failback process, you can choose to discard the changes made to your replica file system or preserve them by copying them back to your primary.")],
  ["discard the changes made to your replica", "preserve them by copying them back"], "EFS replication failback", "2.2.K11"))
F.append(f("efs-replication-delete-config-takes-minutes-destination-writeable", "behavior",
  "Deleting a replication configuration and changing the destination file system to be writeable can take several minutes, and you can delete the configuration from either the source or the destination file system.",
  "How long does it take to make an EFS replica writeable?",
  [("efs/delete-replications", "Deleting a replication configuration and changing the destination file system to be writeable can take several minutes to complete."),
   ("efs/delete-replications", "You can delete an existing replication configuration from either the source or the destination file system by using the Amazon EFS console, the AWS CLI, or the API.")],
  ["can take several minutes to complete", "either the source or the destination"], "EFS replication", "2.2.K11", rel="extended"))
F.append(f("efs-replication-file-system-in-one-configuration-only", "restriction",
  "A file system can be part of only one replication configuration, and a destination file system cannot be the source of another replication configuration.",
  "Can an EFS replica be replicated onward to a third file system?",
  [(CR, "A file system can be part of only one replication configuration. You cannot use a destination file system as the source file system in another replication configuration.")],
  ["part of only one replication configuration", "cannot use a destination file system"], "EFS replication", "2.2.K11", rel="extended"))
F.append(f("efs-replication-cannot-delete-file-system-in-configuration", "restriction",
  "You cannot delete a file system that is part of a replication configuration; you must delete the replication configuration first.",
  "Can you delete an EFS file system that is in a replication configuration?",
  [("efs/delete-replications", "You cannot delete a file system that is part of a replication configuration. You must delete the replication configuration before deleting the file system.")],
  ["cannot delete a file system that is part", "delete the replication configuration before deleting"], "EFS replication", "2.2.K11", rel="extended"))
F.append(f("efs-replication-available-all-efs-regions", "capability",
  "Replication is available in all AWS Regions in which Amazon EFS is available.",
  "In which Regions is EFS replication available?",
  [(R, "Replication is available in all AWS Regions in which Amazon EFS is available.")],
  ["available in all AWS Regions", "in which Amazon EFS is available"], "EFS replication", "2.2.K11", rel="extended"))
F.append(f("efs-replication-no-abac-tags", "restriction",
  "EFS replication does not support using tags for attribute-based access control (ABAC).",
  "Does EFS replication support attribute-based access control with tags?",
  [(R, "Replication does not support using tags for attribute-based access control (ABAC).")],
  ["does not support using tags", "attribute-based access control (ABAC)"], "EFS replication", "2.2.K11", rel="reference"))
F.append(f("efs-replication-destination-metered-12-mib-hidden-data", "pricing-dimension",
  "To facilitate replication, EFS creates hidden directories and metadata on the destination file system, which equal approximately 12 MiB of metered data that you are billed for.",
  "How much extra metered data does EFS replication add to the destination file system?",
  [(R, "To facilitate replication, Amazon EFS creates hidden directories and metadata on the destination file system. These equate to approximately 12 mebibytes (MiB) of metered data for which you are billed.")],
  ["approximately 12 mebibytes (MiB) of metered data", "hidden directories and metadata"], "EFS replication destination", "2.2.K11", rel="reference"))
F.append(f("efs-cross-account-replication-supported", "capability",
  "You can replicate EFS file systems across AWS accounts.",
  "Can an EFS file system replicate to a different AWS account?",
  [(XA, "You can replicate EFS file systems across AWS accounts.")],
  ["replicate EFS file systems across AWS accounts", "across AWS accounts"], "EFS replication", "2.2.K11", tier0=True))
F.append(f("efs-cross-account-replication-requires-iam-role-not-service-linked", "restriction",
  "For cross-account replication you must provide an IAM role when you create the replication configuration; using the service-linked role is not permitted.",
  "Which role does cross-account EFS replication use?",
  [(R, "If you are performing cross-account replication, then you must provide an IAM role when you create the replication configuration. Using the service-linked role is not permitted.")],
  ["must provide an IAM role", "service-linked role is not permitted"], "EFS cross-account replication", "2.2.K11"))
F.append(f("efs-cross-account-replication-destination-must-exist-first", "restriction",
  "For cross-account replication you must create both the source and destination file systems first, because Amazon EFS cannot create the destination file system for you during replication.",
  "Can EFS create the destination file system during cross-account replication?",
  [(XA, "You must create both the source file system and the destination file system in the replication configuration before you can create the IAM role for the source account. Amazon EFS cannot create the destination file system for you during replication.")],
  ["create both the source file system", "cannot create the destination file system for you"], "EFS cross-account replication", "2.2.K11", rel="extended"))
F.append(f("efs-cross-account-replication-needs-file-system-policies", "restriction",
  "Cross-account replication needs an IAM role that gives Amazon EFS permission to replicate in the destination account, plus policies on the file systems that you share across accounts.",
  "What setup does cross-account EFS replication need?",
  [(XA, "Instead of using service-linked roles to perform cross-account replication, you must create an IAM role that gives Amazon EFS permission to perform replication in the destination account. You also need to create policies on the file systems that you want to share across accounts.")],
  ["create an IAM role that gives Amazon", "create policies on the file systems"], "EFS cross-account replication", "2.2.K11", rel="extended"))
F.append(f("efs-encryption-at-rest-console-default-cli-explicit", "default",
  "Encryption at rest is enabled by default when you create a file system in the EFS console, but when you use the AWS CLI, API or SDKs you must enable encryption explicitly.",
  "Is EFS encryption at rest on by default?",
  [(EN, "When you create a file system using the Amazon EFS console, encryption at rest is enabled by default. When using the AWS CLI, API, or SDKs to create a file system, you must explicity enable encryption.")],
  ["encryption at rest is enabled by default", "you must explicity enable encryption"], "EFS encryption at rest", "3.1.K2", dm="default", adj=True, tier0=True))
F.append(f("efs-encryption-setting-cannot-change-after-creation", "restriction",
  "After you create an EFS file system you cannot change its encryption setting, so you cannot make an unencrypted file system encrypted.",
  "Can you encrypt an existing unencrypted EFS file system?",
  [(EN, "After you create an EFS file system, you cannot change its encryption setting. This means that you cannot modify an unencrypted file system to make it encrypted.")],
  ["cannot change its encryption setting", "cannot modify an unencrypted file system"], "EFS encryption at rest", "3.1.K2", tier0=True))
F.append(f("efs-encryption-at-rest-aes-256-data-and-metadata", "behavior",
  "Amazon EFS uses the industry-standard AES-256 encryption algorithm to encrypt data and metadata at rest.",
  "Which algorithm does EFS use for encryption at rest?",
  [(EN, "Amazon EFS uses industry-standard AES-256 encryption algorithm to encrypt data and metadata at rest.")],
  ["industry-standard AES-256 encryption algorithm", "data and metadata at rest"], "EFS encryption at rest", "3.1.K2"))
F.append(f("efs-encryption-transparent-no-application-change", "behavior",
  "In an encrypted EFS file system, data and metadata are encrypted before being written to storage and automatically decrypted when read, transparently to your applications.",
  "Do applications need changes to use an encrypted EFS file system?",
  [(EN, "In an encrypted file system, data and metadata are encrypted by default before being written to storage and are automatically decrypted when read."),
   (EN, "These processes are handled transparently by Amazon EFS, so you don't need to modify your applications.")],
  ["automatically decrypted when read", "don't need to modify your applications"], "EFS encryption at rest", "3.1.K2", rel="extended"))
F.append(f("efs-encryption-scp-condition-key-enforcement", "capability",
  "You can define service control policies in AWS Organizations to enforce Amazon EFS encryption for all accounts in your organization.",
  "How can an organization force all new EFS file systems to be encrypted?",
  [(EN, "You can also define service control policies (SCPs) inside AWS Organizations to enforce Amazon EFS encryption for all AWS accounts in your organization.")],
  ["service control policies (SCPs) inside AWS Organizations", "enforce Amazon EFS encryption"], "EFS encryption at rest", "3.1.K2", rel="extended"))
emit("facts-behavior-04.json", F)
