import sys
sys.path.insert(0, "aws-saa-book/_build/work/23-efs-fsx")
from mk import f, emit

W = "efs/whatisefs"; H = "efs/how-it-works"; FE = "efs/features"
F = []
F.append(f("efs-protocol-nfsv4-versions", "capability",
  "Amazon EFS supports the Network File System version 4 protocol, in the versions NFSv4.1 and NFSv4.0.",
  "Which protocol and versions do clients use to mount Amazon EFS?",
  [(W, "Amazon EFS supports the Network File System version 4 (NFSv4.1 and NFSv4.0) protocol, so the applications and tools that you use today work seamlessly with Amazon EFS.")],
  ["NFSv4.1 and NFSv4.0", "Network File System version 4"], "Amazon EFS", "3.1.K2", tier0=True))
F.append(f("efs-serverless-elastic-no-provisioning", "behavior",
  "Amazon EFS is serverless and fully elastic: you do not provision or manage storage capacity, and a file system grows and shrinks automatically as you add and remove files.",
  "Does an EFS file system need provisioned capacity, and does it grow and shrink on its own?",
  [(W, "Amazon Elastic File System (Amazon EFS) provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance."),
   (W, "Amazon EFS is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files.")],
  ["serverless, fully elastic file storage", "growing and shrinking automatically", "without provisioning or managing storage capacity"],
  "Amazon EFS file system", ["3.1.S2", "4.1.S4"], tier0=True))
F.append(f("efs-windows-ec2-not-supported", "restriction",
  "Using Amazon EFS with Microsoft Windows-based Amazon EC2 instances is not supported.",
  "Can Windows-based EC2 instances mount an Amazon EFS file system?",
  [(W, "Using Amazon EFS with Microsoft Windows–based Amazon EC2 instances is not supported.")],
  ["is not supported", "Microsoft Windows–based Amazon EC2 instances"], "Amazon EFS clients", "3.1.K3", tier0=True))
F.append(f("efs-clients-current-linux-nfsv41-and-mount-helper", "capability",
  "AWS recommends a current generation Linux NFSv4.1 client, such as those in the latest Amazon Linux, Amazon Linux 2, Red Hat, Ubuntu, and macOS Big Sur AMIs, together with the EFS mount helper.",
  "Which operating systems and client does AWS recommend for mounting EFS?",
  [(H, "We recommend using a current generation Linux NFSv4.1 client, such as those found in the latest Amazon Linux, Amazon Linux 2, Red Hat, Ubuntu, and macOS Big Sur AMIs, in conjunction with the EFS mount helper.")],
  ["current generation Linux NFSv4.1 client", "macOS Big Sur AMIs", "in conjunction with the EFS mount helper"],
  "Amazon EFS clients", "3.1.K3", rel="extended"))
F.append(f("efs-compute-services-ec2-ecs-eks-lambda-fargate", "capability",
  "Amazon EFS is accessible from most types of AWS compute instances, including Amazon EC2, Amazon ECS, Amazon EKS, AWS Lambda, and AWS Fargate.",
  "Which AWS compute services can use Amazon EFS?",
  [(W, "Amazon EFS is accessible across most types of Amazon Web Services compute instances, including Amazon EC2, Amazon ECS, Amazon EKS, AWS Lambda, and AWS Fargate.")],
  ["Amazon EC2, Amazon ECS, Amazon EKS, AWS Lambda, and AWS Fargate", "most types of Amazon Web Services compute instances"],
  "Amazon EFS clients", "3.1.K2", tier0=True))
F.append(f("efs-sagemaker-training-jobs-access", "capability",
  "You can access training data in EFS from Amazon SageMaker training jobs by referencing an EFS file system in your CreateTrainingJob request.",
  "Can Amazon SageMaker use data in an EFS file system?",
  [("www/efs/faq", "Yes. You can access training data in EFS from Amazon SageMaker training jobs by referencing an EFS file system in your CreateTrainingJob request .")],
  ["access training data in EFS", "Amazon SageMaker training jobs"],
  "Amazon EFS with SageMaker", "3.1.K2", rel="extended"))
F.append(f("efs-regional-multi-az-continuous-availability", "behavior",
  "A Regional EFS file system stores data redundantly across multiple Availability Zones in one AWS Region, which keeps the data continuously available even when one or more Availability Zones are unavailable.",
  "How does a Regional EFS file system store data, and what happens when an Availability Zone is unavailable?",
  [(FE, "Storing data across multiple Availability Zones provides continuous availability to the data, even when one or more Availability Zones in an AWS Region are unavailable.")],
  ["continuous availability to the data", "even when one or more Availability Zones"],
  "Regional file system", "2.2.K11", tier0=True))
F.append(f("efs-regional-recommended-type", "behavior",
  "Regional is the recommended EFS file system type; it stores data redundantly across multiple geographically separated Availability Zones within the same AWS Region.",
  "Which EFS file system type is recommended, and where does it store data?",
  [(FE, "Regional file systems (recommended) store data redundantly across multiple geographically separated Availability Zones within the same AWS Region.")],
  ["Regional file systems (recommended)", "multiple geographically separated Availability Zones"],
  "Regional file system", "2.2.K11"))
F.append(f("efs-onezone-single-az-storage", "behavior",
  "A One Zone EFS file system stores data within a single Availability Zone.",
  "Where does a One Zone EFS file system store its data?",
  [(FE, "One Zone file systems store data within a single Availability Zone. Storing data in a single Availability Zone provides continuous availability to the data."),],
  ["store data within a single Availability Zone", "continuous availability to the data"],
  "One Zone file system", "2.2.K11"))
F.append(f("efs-onezone-az-loss-data-may-be-lost", "restriction",
  "If all or part of the Availability Zone is lost or damaged, for example by fire or water damage, data in a One Zone file system may be lost.",
  "What extra failure mode does a One Zone EFS file system add compared with a Regional one?",
  [(FE, "In the unlikely case of the loss or damage to all or part of an AWS Availability Zone, data in a One Zone storage class may be lost. For example, events like fire and water damage could result in data loss.")],
  ["One Zone storage class may be lost", "fire and water damage"],
  "One Zone file system", "2.2.K11", tier0=True))
F.append(f("efs-onezone-automatic-backup-aws-backup", "behavior",
  "Amazon EFS automatically backs up One Zone file systems with AWS Backup, and you can restore a backup to any operational Availability Zone in the Region or to a different Region.",
  "What protects a One Zone EFS file system against loss of its Availability Zone, and where can a backup be restored?",
  [(FE, "For added data protection, Amazon EFS automatically backs up One Zone file systems with AWS Backup. You can restore file system backups to any operational Availability Zone within an AWS Region, or you can restore them to a different AWS Region.")],
  ["backs up One Zone file systems", "different AWS Region"],
  "One Zone file system", "2.2.K11", tier0=True))
F.append(f("efs-onezone-only-certain-azs", "restriction",
  "One Zone file systems are available only in certain Availability Zones.",
  "Can a One Zone EFS file system be created in any Availability Zone?",
  [(FE, "One Zone file systems are available to only certain Availability Zones.")],
  ["available to only certain Availability Zones", "One Zone file systems are available"],
  "One Zone file system", "2.2.K11", rel="extended"))
F.append(f("efs-mount-target-definition-ip-nfs-endpoint", "behavior",
  "A mount target provides an IP address for an NFSv4 endpoint at which you can mount an EFS file system; to access a file system in a VPC you create one or more mount targets in that VPC.",
  "What is an EFS mount target?",
  [(H, "To access your EFS file system in a VPC, you create one or more mount targets in the VPC. A *mount target* provides an IP address for an NFSv4 endpoint at which you can mount an EFS file system.")],
  ["provides an IP address for an NFSv4 endpoint", "one or more mount targets in the VPC"],
  "EFS mount target", "3.1.K2", tier0=True))
F.append(f("efs-dns-name-resolves-to-same-az-mount-target", "behavior",
  "You mount an EFS file system by its DNS name, which resolves to the IP address of the mount target in the same Availability Zone as your EC2 instance.",
  "Which mount target does the EFS DNS name resolve to?",
  [(H, "You mount your file system using its Domain Name Service (DNS) name, which resolves to the IP address of the EFS mount target in the same Availability Zone as your EC2 instance.")],
  ["resolves to the IP address of the EFS", "Domain Name Service (DNS) name"],
  "EFS mount target", "3.1.K2"))
F.append(f("efs-one-mount-target-per-az-shared-by-instances", "behavior",
  "You can create one mount target in each Availability Zone in a Region; if the VPC has several subnets in that zone you create it in one of them, and all EC2 instances in that zone share it.",
  "How many mount targets can a Regional EFS file system have in one Availability Zone, and who uses it?",
  [(H, "You can create one mount target in each Availability Zone in an AWS Region. If there are multiple subnets in an Availability Zone in your VPC, you create a mount target in one of the subnets. Then all EC2 instances in that Availability Zone share that mount target.")],
  ["one mount target in each Availability Zone", "mount target in one of the subnets", "share that mount target"],
  "EFS mount target, per Availability Zone", "3.1.K2", tier0=True))
F.append(f("efs-regional-mount-target-per-az-same-az-access", "default",
  "For a Regional file system a mount target is created in each Availability Zone, and AWS recommends that you access the file system through the mount target in the same Availability Zone for performance and cost reasons.",
  "Why does a Regional EFS file system need a mount target in each Availability Zone?",
  [(H, "Because the file system is Regional, a mount target was created in each Availability Zone. We recommend that you access the file system from a mount target within the same Availability Zone for performance and cost reasons.")],
  ["a mount target was created in each", "within the same Availability Zone", "for performance and cost reasons"],
  "Regional file system", "3.1.K2", dm="default", rel="core"))
F.append(f("efs-mount-targets-only-one-vpc-at-a-time", "restriction",
  "An EFS file system can have mount targets in only one VPC at a time.",
  "In how many VPCs can one EFS file system have mount targets at the same time?",
  [(H, "An EFS file system can have mount targets in only one VPC at a time.")],
  ["only one VPC at a time", "can have mount targets"],
  "EFS file system", "3.1.K2", rel="extended"))
F.append(f("efs-onezone-single-mount-target-same-az", "restriction",
  "A One Zone file system supports only a single mount target, located in the same Availability Zone as the file system; you cannot add additional mount targets.",
  "How many mount targets can a One Zone EFS file system have?",
  [("efs/mounting-one-zone", "EFS One Zone file systems support only a single mount target which is located in the same Availability Zone as the file system. You cannot add additional mount targets.")],
  ["support only a single mount target", "You cannot add additional mount targets"],
  "One Zone file system", ["3.1.K2", "2.2.K11"], tier0=True))
F.append(f("efs-onezone-other-az-instance-pays-data-access-charges", "behavior",
  "An EC2 instance in a different Availability Zone from a One Zone file system's mount target pays EC2 data access charges for using that mount target.",
  "What is the cost effect of mounting a One Zone EFS file system from an instance in another Availability Zone?",
  [(H, "In this example, the EC2 instance in the us-west-2c Availability Zone will pay EC2 data access charges for accessing a mount target in a different Availability Zone.")],
  ["pay EC2 data access charges", "in a different Availability Zone"],
  "One Zone file system, cross-AZ access", "2.2.K11"))
F.append(f("efs-onezone-same-az-avoids-transfer-charges-better-performance", "behavior",
  "Accessing a One Zone file system from an EC2 instance in the same Availability Zone as the file system's mount target avoids data transfer charges between Availability Zones and gives better performance.",
  "How do you avoid cross-AZ data transfer charges with a One Zone EFS file system?",
  [("efs/mounting-one-zone", "You can avoid data transfer charges between Availability Zones and achieve better performance by accessing an EFS file system using an Amazon EC2 compute instance that is located in the same Availability Zone as that of the file system's mount target.")],
  ["avoid data transfer charges between Availability Zones", "achieve better performance", "located in the same Availability Zone"],
  "One Zone file system", "2.2.K11"))
F.append(f("efs-onezone-other-az-mount-needs-az-name-or-mount-target-dns", "restriction",
  "To mount a One Zone file system on an EC2 instance in a different Availability Zone, you have to specify the file system's Availability Zone name or the DNS name of its mount target in the mount helper command.",
  "What must the mount command specify when a One Zone EFS file system is mounted from another Availability Zone?",
  [("efs/mounting-one-zone", "If you are mounting a One Zone file system on an Amazon EC2 instance that is located in a different Availability Zone, you have to specify the file system's Availability Zone name or the DNS name of the file system's mount target in the mount helper mount command.")],
  ["specify the file system's Availability Zone name", "DNS name of the file system's mount target"],
  "One Zone file system", "2.2.K11", rel="extended"))
F.append(f("efs-onezone-ecs-eks-lambda-same-az-subnets", "restriction",
  "With a One Zone file system, Amazon ECS tasks and Lambda functions must be launched into subnets in the same Availability Zone as the file system.",
  "Where must ECS tasks or Lambda functions run to use a One Zone EFS file system?",
  [("efs/mounting-one-zone", "To use EFS One Zone file systems with Amazon ECS you should choose only subnets that are in the same Availability Zone as your file system when launching your task."),
   ("efs/mounting-one-zone", "When you use Lambda with One Zone file systems, configure your function to only launch invocations into subnets that are in the same Availability Zone as your file system.")],
  ["subnets that are in the same Availability Zone", "only launch invocations into subnets"],
  "One Zone file system with ECS and Lambda", "2.2.K11", rel="extended"))
F.append(f("efs-concurrent-access-multiple-clients-multiple-azs", "capability",
  "You can access an EFS file system concurrently from multiple NFS clients, and EC2 and other compute instances in multiple Availability Zones of the same Region can share it; EFS supports one to thousands of EC2 instances connecting at once.",
  "How many compute instances can read and write one EFS file system at the same time?",
  [(H, "You can access your EFS file system concurrently from multiple NFS clients, so applications that scale beyond a single connection can access a file system. Amazon EC2 and other AWS compute instances running in multiple Availability Zones within the same AWS Region can access the file system, so that many users can access and share a common data source."),
   ("www/efs/faq", "Amazon EFS supports one to thousands of Amazon Elastic Compute Cloud (EC2) instances connecting to a file system concurrently.")],
  ["concurrently from multiple NFS clients", "one to thousands of Amazon Elastic Compute Cloud (EC2) instances"],
  "EFS file system", "4.1.K4", tier0=True))
F.append(f("efs-onpremises-mount-via-direct-connect-or-vpn", "capability",
  "You can mount EFS file systems on on-premises data center servers when they are connected to your VPC with AWS Direct Connect or Site-to-Site VPN.",
  "Can on-premises servers mount Amazon EFS, and over which connections?",
  [(H, "You can mount your EFS file systems on your on-premises data center servers when connected to your Amazon VPC with AWS Direct Connect or Site-to-Site VPN.")],
  ["AWS Direct Connect or Site-to-Site VPN", "on your on-premises data center servers"],
  "Amazon EFS, on-premises access", "3.1.K2", tier0=True))
F.append(f("efs-onpremises-server-must-be-linux", "restriction",
  "An on-premises server that mounts EFS must have a Linux-based operating system.",
  "Which operating system must an on-premises server use to mount EFS?",
  [(H, "Your on-premises server must have a Linux-based operating system.")],
  ["must have a Linux-based operating system", "on-premises server"],
  "Amazon EFS, on-premises access", "3.1.K3"))
F.append(f("efs-onpremises-security-group-allow-nfs-port-2049", "behavior",
  "To reach EFS from an on-premises server you add a rule to the mount target security group that allows inbound traffic to the NFS port (2049) from that server.",
  "Which security group rule lets an on-premises server mount EFS?",
  [(H, "To access Amazon EFS from an on-premises server, add a rule to your mount target security group to allow inbound traffic to the NFS port (2049) from your on-premises server.")],
  ["NFS port (2049)", "allow inbound traffic", "mount target security group"],
  "EFS mount target security group", "3.1.K2", tier0=True))
F.append(f("efs-onpremises-no-extra-cost-pay-direct-connect", "pricing-dimension",
  "There is no additional cost for on-premises access to EFS file systems; you are charged for the Direct Connect connection to your VPC.",
  "Is there an extra EFS charge for on-premises access?",
  [(H, "There is no additional cost for on-premises access to your Amazon EFS file systems. You are charged for the Direct Connect connection to your Amazon VPC.")],
  ["no additional cost for on-premises access", "charged for the Direct Connect connection"],
  "Amazon EFS, on-premises access", "3.1.K2", rel="extended"))
F.append(f("efs-onpremises-use-mount-target-ip-instead-of-dns", "behavior",
  "AWS recommends mounting an EFS file system on an on-premises server by using a mount target IP address instead of a DNS name.",
  "How does AWS recommend an on-premises server address the EFS mount target?",
  [(H, "For the sake of simplicity, we recommend mounting an Amazon EFS file system on an on-premises server using a mount target IP address instead of a DNS name.")],
  ["mount target IP address instead of", "using a mount target IP address"],
  "Amazon EFS, on-premises access", "3.1.K2", rel="extended"))
emit("facts-behavior-01.json", F)
