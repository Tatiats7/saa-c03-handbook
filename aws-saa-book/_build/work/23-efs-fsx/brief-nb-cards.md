facts card: 21 facts
s3-change-s3-files-launch-2026-04
  claim: On 2026-04-07 AWS launched Amazon S3 Files, a shared file system that connects any AWS compute resource directly with data in Amazon S3; S3 file systems can be mounted on Amazon EC2, AWS Lambda, Amazon EKS and Amazon ECS.
  scope: S3 general purpose buckets.
  link: [2026-04-07](../facts/s3.md#s3-change-s3-files-launch-2026-04)
  link: [shared file system](../facts/s3.md#s3-change-s3-files-launch-2026-04)
  say: April seventh, twenty twenty-six | a shared file system on top of S3
s3-files-built-on-efs-data-stays-in-s3
  claim: S3 Files is built using Amazon EFS and gives file system access to S3 data; the authoritative data always remains in S3, and background synchronization keeps the file system and the bucket consistent in both directions.
  scope: S3 Files.
  link: [Built using Amazon EFS](../facts/s3.md#s3-files-built-on-efs-data-stays-in-s3)
  link: [Your authoritative data always remains in S3](../facts/s3.md#s3-files-built-on-efs-data-stays-in-s3)
  say: built on Amazon EFS | the data stays in S3
s3-files-vs-efs-vs-fsx
  claim: AWS positions S3 Files for data that is already in S3 and must be used by file-based applications, AI agents or teams with standard file operations; Amazon EFS for a fully managed shared file system as primary storage where data originates in and is mainly accessed through the file system; and Amazon FSx for existing applications that run on network-attached file storage.
  scope: choosing file access for AWS compute.
  link: [you already have data in S3](../facts/s3.md#s3-files-vs-efs-vs-fsx)
  link: [primary storage](../facts/s3.md#s3-files-vs-efs-vs-fsx)
  link: [run on network-attached file storage](../facts/s3.md#s3-files-vs-efs-vs-fsx)
  say: S3 Files when the data already lives in S3 | EFS as primary shared file storage | FSx for existing NAS applications
ebs-decision-guide-block-storage-single-instance
  claim: The AWS storage decision guide maps block storage (Amazon EBS and EC2 instance store) to applications that need low-latency, high-performance durable storage attached to single EC2 instances or containers, such as databases.
  scope: AWS storage decision guide, block storage.
  link: [attached to single Amazon EC2 instances or containers](../facts/ebs.md#ebs-decision-guide-block-storage-single-instance)
  link: [low-latency, high-performance durable storage](../facts/ebs.md#ebs-decision-guide-block-storage-single-instance)
ebs-decision-guide-file-storage-shared-access
  claim: The AWS storage decision guide maps file system storage (such as Amazon EFS and Amazon FSx) to applications and workloads that need shared read and write access across multiple Amazon EC2 instances or containers, or from multiple on-premises servers.
  scope: AWS storage decision guide, file storage.
  link: [shared read and write access across multiple Amazon EC2 instances](../facts/ebs.md#ebs-decision-guide-file-storage-shared-access)
ebs-vs-efs-az-scope-and-sharing
  claim: Each EBS volume is replicated within its own Availability Zone, while Amazon EFS is a regional service that stores data within and across multiple Availability Zones and gives shared access to thousands of EC2 instances.
  scope: EBS volume versus Amazon EFS file system; EBS Multi-Attach aside.
  link: [automatically replicated within its Availability Zone](../facts/ebs.md#ebs-vs-efs-az-scope-and-sharing)
  link: [within and across multiple Availability Zones](../facts/ebs.md#ebs-vs-efs-az-scope-and-sharing)
ebs-multi-attach-provisioned-iops-same-az
  claim: EBS Multi-Attach lets you attach a single Provisioned IOPS SSD (io1 or io2) volume to several instances in the same Availability Zone, and each attached instance has full read and write permission.
  scope: Multi-Attach enabled io1 and io2 volumes.
  link: [attach a single Provisioned IOPS SSD](../facts/ebs.md#ebs-multi-attach-provisioned-iops-same-az)
  link: [in the same Availability Zone](../facts/ebs.md#ebs-multi-attach-provisioned-iops-same-az)
  link: [full read and write permission](../facts/ebs.md#ebs-multi-attach-provisioned-iops-same-az)
ebs-multi-attach-needs-clustered-file-system
  claim: Standard file systems such as XFS and EXT4 are not designed for simultaneous access by several instances; with Multi-Attach you should use a clustered file system.
  scope: Multi-Attach enabled volumes.
  link: [use a clustered file system](../facts/ebs.md#ebs-multi-attach-needs-clustered-file-system)
  link: [not designed to be accessed simultaneously](../facts/ebs.md#ebs-multi-attach-needs-clustered-file-system)
ebs-multi-attach-provisioned-iops-only
  claim: Multi-Attach is supported only on Provisioned IOPS SSD (io1 and io2) volumes.
  scope: per EBS volume type.
  link: [supported exclusively on](../facts/ebs.md#ebs-multi-attach-provisioned-iops-only)
  link: [Provisioned IOPS SSD (`io1` and `io2`) volumes](../facts/ebs.md#ebs-multi-attach-provisioned-iops-only)
  say: supported exclusively on io1 and io2 | Provisioned IOPS SSD io1 and io2 volumes
ebs-volume-same-az-as-instance
  claim: You can attach several EBS volumes to one instance, but the volume and the instance must be in the same Availability Zone.
  scope: EBS volume attachment.
  link: [must be in the same Availability Zone](../facts/ebs.md#ebs-volume-same-az-as-instance)
  link: [attach multiple EBS volumes to a single instance](../facts/ebs.md#ebs-volume-same-az-as-instance)
instance-store-ideal-for-temporary-data
  claim: Instance store is ideal for temporary information that changes frequently, such as buffers, caches and scratch data, and for temporary data that you replicate across a fleet of instances.
  scope: instance store.
  link: [temporary storage of information that changes frequently](../facts/instance-store.md#instance-store-ideal-for-temporary-data)
  link: [buffers, caches, scratch data](../facts/instance-store.md#instance-store-ideal-for-temporary-data)
  link: [replicate across a fleet of instances](../facts/instance-store.md#instance-store-ideal-for-temporary-data)
  say: temporary data that changes often | buffers, caches and scratch data | or data copied across many instances
directory-service-fsx-windows-needs-managed-ad-or-self-managed
  claim: An FSx for Windows File Server file system is joined to an Active Directory domain, either AWS Managed Microsoft AD or a self-managed Microsoft Active Directory; Amazon FSx does not support AD Connector or Simple AD.
  scope: FSx for Windows File Server Active Directory integration.
  link: [Amazon FSx does not support](../facts/directory-service.md#directory-service-fsx-windows-needs-managed-ad-or-self-managed)
  link: [Using a self-managed Microsoft Active Directory](../facts/directory-service.md#directory-service-fsx-windows-needs-managed-ad-or-self-managed)
directory-service-two-way-trust-for-aws-apps-one-way-for-ec2-rds-fsx
  claim: A two-way trust is required for AWS enterprise apps such as IAM Identity Center, WorkSpaces, Amazon Quick, WorkMail and the AWS Management Console, because AWS Managed Microsoft AD must query users and groups in the self-managed AD; Amazon EC2, Amazon RDS and Amazon FSx work with either a one-way or a two-way trust.
  scope: trusts between AWS Managed Microsoft AD and a self-managed AD.
  link: [two-way trust is required](../facts/directory-service.md#directory-service-two-way-trust-for-aws-apps-one-way-for-ec2-rds-fsx)
  link: [either a one-way or two-way trust](../facts/directory-service.md#directory-service-two-way-trust-for-aws-apps-one-way-for-ec2-rds-fsx)
ecs-efs-fargate-platform-14-linux-only
  claim: For tasks hosted on Fargate, Amazon EFS file systems are supported on platform version 1.4.0 or later (Linux).
  scope: Amazon EFS on Fargate tasks; minimum; Linux.
  link: [platform version 1.4.0 or later (Linux)](../facts/ecs.md#ecs-efs-fargate-platform-14-linux-only)
  link: [tasks that are hosted on Fargate](../facts/ecs.md#ecs-efs-fargate-platform-14-linux-only)
ecs-efs-volumes-shared-persistent-across-instances
  claim: Amazon EFS file systems can be used with Amazon ECS to export file system data across your fleet of container instances so that tasks have access to the same persistent storage no matter the instance on which they land.
  scope: Amazon ECS with Amazon EFS.
  link: [access to the same persistent storage](../facts/ecs.md#ecs-efs-volumes-shared-persistent-across-instances)
  link: [no matter the instance on which they land](../facts/ecs.md#ecs-efs-volumes-shared-persistent-across-instances)
lambda-change-s3-files-mount-2026
  claim: On 2026-04-21 Lambda added support for Amazon S3 Files, so functions can mount Amazon S3 buckets as file systems and perform standard file operations without downloading data for processing; S3 Files is built using Amazon EFS.
  scope: Lambda functions.
  link: [mount Amazon S3 buckets as file systems](../facts/lambda.md#lambda-change-s3-files-mount-2026)
  link: [2026-04-21](../facts/lambda.md#lambda-change-s3-files-mount-2026)
  say: April twenty-first, twenty twenty-six
lambda-efs-mount-target-every-az
  claim: For Lambda, create the EFS file system with a mount target in every Availability Zone the function connects to, use at least two Availability Zones for performance and resilience, and allow NFS traffic (port 2049) in the security groups of the function and the mount targets.
  scope: Amazon EFS file system used by Lambda.
  link: [a mount target in every Availability Zone](../facts/lambda.md#lambda-efs-mount-target-every-az)
  link: [use at least two Availability Zones](../facts/lambda.md#lambda-efs-mount-target-every-az)
  link: [NFS traffic (port 2049)](../facts/lambda.md#lambda-efs-mount-target-every-az)
  say: a mount target in every Availability Zone
lambda-efs-role-permissions
  claim: If the EFS file system has a user-configured IAM policy, the function's execution role needs the matching elasticfilesystem permissions (included in the AmazonElasticFileSystemClientReadWriteAccess managed policy) and the permissions required to connect to the file system's VPC.
  scope: execution role of a function that uses Amazon EFS; the file system has a user-configured IAM policy.
  link: [AmazonElasticFileSystemClientReadWriteAccess](../facts/lambda.md#lambda-efs-role-permissions)
  link: [connect to the file system's VPC](../facts/lambda.md#lambda-efs-role-permissions)
  say: the EFS client read-write managed policy
lambda-efs-shared-mount-in-vpc
  claim: A function can mount an Amazon EFS file system to a local directory, so the function code can access and modify shared resources safely and at high concurrency; the function connects to the file system over the local network in a VPC.
  scope: Lambda function with an Amazon EFS file system; the function connects to a VPC.
  link: [mount an Amazon Elastic File System](../facts/lambda.md#lambda-efs-shared-mount-in-vpc)
  link: [access and modify shared resources safely](../facts/lambda.md#lambda-efs-shared-mount-in-vpc)
  link: [over the local network in a VPC](../facts/lambda.md#lambda-efs-shared-mount-in-vpc)
  say: mount an EFS file system
fargate-faq-efs-for-persistent-storage
  claim: Amazon EFS can provide persistent storage to workloads running on AWS Fargate.
  scope: AWS Fargate workloads.
  link: [Amazon Elastic File System (EFS)](../facts/fargate.md#fargate-faq-efs-for-persistent-storage)
fargate-storage-types-ebs-efs-bind
  claim: For ECS tasks hosted on Fargate, Amazon EBS volumes, Amazon EFS volumes for persistent storage, and bind mounts for ephemeral storage are supported.
  scope: ECS tasks on Fargate.
  link: [cost-effective, durable, high-performance block storage](../facts/fargate.md#fargate-storage-types-ebs-efs-bind)
  link: [Amazon EFS volumes for persistent storage](../facts/fargate.md#fargate-storage-types-ebs-efs-bind)
  link: [Bind mounts for ephemeral storage](../facts/fargate.md#fargate-storage-types-ebs-efs-bind)
