import sys
sys.path.insert(0, "aws-saa-book/_build/work/23-efs-fsx")
from mk import f, emit

FAQ = "www/efs/faq"; AP = "efs/efs-access-points"; IAM = "efs/iam-access-control-nfs-efs"; BPA = "efs/access-control-block-public-access"
NA = "efs/network-access"; AF = "efs/accessing-fs"
F = []
F.append(f("efs-access-point-enforces-posix-user-and-root-directory", "behavior",
  "An EFS access point can enforce a user identity, including POSIX groups, for all requests made through it, and can enforce a different root directory so clients can access only that directory and its subdirectories.",
  "What does an EFS access point enforce?",
  [(AP, "Access points can enforce a user identity, including the user's POSIX groups, for all file system requests that are made through the access point. Access points can also enforce a different root directory for the file system so that clients can only access data in the specified directory or its subdirectories.")],
  ["enforce a user identity", "enforce a different root directory", "specified directory or its subdirectories"], "EFS access point", "3.1.K2", tier0=True))
F.append(f("efs-access-point-needs-mount-target-first", "restriction",
  "You must create at least one mount target in your VPC before using access points, because mount targets provide network connectivity while access points provide access control.",
  "Does an access point replace the mount target?",
  [(AP, "You must create at least one mount target in your VPC before using access points. Mount targets provide the network connectivity to your EFS file system while access points provide the access control and application-specific entry points.")],
  ["create at least one mount target", "provide the network connectivity", "provide the access control"], "EFS access point", "3.1.K2", rel="extended"))
F.append(f("efs-access-point-iam-policy-enforces-specific-access-point", "capability",
  "You can use IAM policies to enforce that specific applications use a specific access point.",
  "How do you force an application to use a particular EFS access point?",
  [(AP, "You can use AWS Identity and Access Management (IAM) policies to enforce that specific applications use a specific access point.")],
  ["specific applications use a specific access point", "IAM) policies"], "EFS access point", "3.1.K2"))
F.append(f("efs-access-point-mount-with-mount-helper-tls", "behavior",
  "You use the EFS mount helper when mounting a file system through an access point, and the mount command includes the file system ID, the access point ID and the tls mount option.",
  "How do you mount an EFS file system through an access point?",
  [(AP, "You use the EFS mount helper when mounting a file system using an access point. In the mount command, include file system ID, the access point ID, and the `tls` mount option, as shown in the following example.")],
  ["use the EFS mount helper", "the access point ID"], "EFS access point", "3.1.K2", rel="extended"))
F.append(f("efs-access-point-faq-configure-os-user-group-root-directory", "capability",
  "When you create an EFS access point you can configure an operating system user and group, and a root directory, for all connections that use it.",
  "What can you configure when you create an EFS access point?",
  [(FAQ, "When you create an Amazon EFS Access Point, you can configure an operating system user and group, and a root directory for all connections that use it.")],
  ["operating system user and group", "a root directory for all connections"], "EFS access point", "3.1.K2"))
F.append(f("efs-access-point-faq-root-directory-auto-created-first-connect", "behavior",
  "If you specify the root directory's owner, EFS creates the access point root directory with the permissions you provide the first time a client connects.",
  "When does EFS create the root directory of an access point?",
  [(FAQ, "If you specify the root directory’s owner, EFS will automatically create it with the permissions you provide the first time a client connects to the access point.")],
  ["automatically create it", "the first time a client connects"], "EFS access point", "3.1.K2", rel="reference"))
F.append(f("efs-iam-identity-and-resource-policies-control-client-access", "capability",
  "You can use both IAM identity policies and resource policies to control client access to EFS, including read-only, write and root access.",
  "How do IAM policies control which clients can mount and write to EFS?",
  [(IAM, "You can use both IAM identity policies and resource policies to control client access to Amazon EFS resources in a way that is scalable and optimized for cloud environments. Using IAM, you can permit clients to perform specific actions on a file system, including read-only, write, and root access.")],
  ["IAM identity policies and resource policies", "read-only, write, and root access"], "EFS IAM authorization for NFS clients", "3.1.K2", tier0=True))
F.append(f("efs-iam-nfs-client-authorization-requires-mount-helper", "restriction",
  "You must use the EFS mount helper to mount an EFS file system in order to use IAM authorization to control client access.",
  "Which mount method is required for IAM authorization on EFS?",
  [(IAM, "You must use the EFS mount helper to mount your EFS file systems in order to use IAM authorization to control client access.")],
  ["must use the EFS mount helper", "IAM authorization to control client access"], "EFS IAM authorization for NFS clients", "3.1.K2", tier0=True))
F.append(f("efs-default-file-system-policy-full-access-anonymous", "default",
  "The default EFS file system policy does not use IAM to authenticate and grants full access to any anonymous client that can connect to the file system through a mount target.",
  "What access does the default EFS file system policy give?",
  [(IAM, "The default EFS file system policy does not use IAM to authenticate, and grants full access to any anonymous client that can connect to the file system using a mount target.")],
  ["does not use IAM to authenticate", "grants full access to any anonymous client"], "EFS file system policy", "3.1.K2", dm="default", adj=True, tier0=True))
F.append(f("efs-iam-authorization-logged-to-cloudtrail", "behavior",
  "When you use IAM authorization for NFS clients, client connections and IAM authorization decisions are logged to AWS CloudTrail.",
  "Where are EFS client connections and IAM authorization decisions logged?",
  [(IAM, "When you use IAM authorization for NFS clients, client connections and IAM authorization decisions are logged to AWS CloudTrail.")],
  ["logged to AWS CloudTrail", "IAM authorization decisions"], "EFS IAM authorization for NFS clients", "3.1.K2", rel="extended"))
F.append(f("efs-network-and-iam-control-nfs-client-access", "behavior",
  "NFS client access to Amazon EFS is controlled by both IAM policies and network security policies such as security groups.",
  "What controls which NFS clients can reach an EFS file system?",
  [("efs/whatisefs", "NFS client access to Amazon EFS is controlled by both AWS Identity and Access Management (IAM) policies and network security policies, such as security groups.")],
  ["controlled by both AWS Identity and Access Management", "network security policies, such as security groups"], "Amazon EFS access control", "3.1.K2", tier0=True))
F.append(f("efs-faq-control-instances-with-security-groups-and-iam", "behavior",
  "You control which EC2 instances can access an EFS file system with VPC security group rules and IAM policies; security groups control network traffic and an IAM policy on the file system controls which clients can mount it and with what permissions.",
  "How do you control which EC2 instances can access your EFS file system?",
  [(FAQ, "You control which EC2 instances can access your file system using VPC security group rules and IAM policies. Use VPC security groups to control the network traffic to and from your file system. Attach an IAM policy to your file system to control which clients can mount your file system and with what permissions, and use EFS Access Points to manage application access.")],
  ["VPC security group rules and IAM policies", "Attach an IAM policy to your file system"], "Amazon EFS access control", "3.1.K2", tier0=True))
F.append(f("efs-nfs-client-needs-network-connection-to-port-2049", "restriction",
  "An NFSv4.1 client can only mount an EFS file system if it can make a network connection to the NFS port (TCP port 2049) of one of the file system's mount targets.",
  "Which port must a client reach to mount an EFS file system?",
  [(NA, "An NFS version 4.1 (NFSv4.1) client can only mount a file system if it can make a network connection to the NFS port (TCP port 2049) of one of the file system's mount targets.")],
  ["NFS port (TCP port 2049)", "can only mount a file system"], "EFS mount target network access", "3.1.K2", tier0=True))
F.append(f("efs-security-groups-on-mount-target-and-instance", "behavior",
  "When using EFS you specify VPC security groups for your EC2 instances and security groups for the EFS mount targets associated with the file system.",
  "Where are security groups applied for EFS?",
  [(NA, "When using Amazon EFS, you specify VPC security groups for your EC2 instances and security groups for the EFS mount targets associated with the file system.")],
  ["security groups for the EFS mount targets", "VPC security groups for your EC2 instances"], "EFS mount target network access", "3.1.K2"))
F.append(f("efs-allows-connections-from-any-source-port", "behavior",
  "To support a broad set of NFS clients, Amazon EFS allows connections from any source port.",
  "Does EFS restrict the client source port?",
  [(NA, "To support a broad set of NFS clients, Amazon EFS allows connections from any source port.")],
  ["allows connections from any source port", "broad set of NFS clients"], "EFS mount target network access", "3.1.K2", rel="reference"))
F.append(f("efs-block-public-access-default-no-public-access", "default",
  "By default, new EFS file systems do not allow public access, but you can modify file system policies to allow public access.",
  "Do new EFS file systems allow public access?",
  [(BPA, "By default, new EFS file systems don't allow public access. However, you can modify file system policies to allow public access.")],
  ["new EFS file systems don't allow public access", "modify file system policies to allow public access"], "EFS block public access", "3.1.K2", dm="default", adj=True, tier0=True))
F.append(f("efs-block-public-access-prevents-public-resource-policies", "behavior",
  "Enabling Block Public Access protects EFS resources by preventing public access from being granted through the resource policies that are directly attached to the file system.",
  "What does EFS Block Public Access prevent?",
  [(BPA, "Enabling Block Public Access access helps protect your resources by preventing public access from being granted through the resource policies that are directly attached to the file system.")],
  ["preventing public access from being granted", "resource policies that are directly attached"], "EFS block public access", "3.1.K2"))
F.append(f("efs-public-policy-evaluation-assumes-public-until-fixed-values", "behavior",
  "To decide whether a file system policy is public, Amazon EFS assumes the policy is public and then evaluates whether it qualifies as non-public.",
  "How does EFS decide that a file system policy is public?",
  [(BPA, "When evaluating whether a file system allows public access, Amazon EFS assumes that the file system policy is public. It then evaluates the file system policy to determine if it qualifies as non-public.")],
  ["assumes that the file system policy is public", "qualifies as non-public"], "EFS block public access", "3.1.K2", rel="extended"))
F.append(f("efs-mount-target-ip-address-cannot-change", "restriction",
  "You cannot change the IP address of an existing mount target; to change it you delete the mount target and create a new one with the new address.",
  "Can you change the IP address of an EFS mount target?",
  [(AF, "You can't change the IP address of an existing mount target. To change an IP address, you need to delete the mount target and create a new one with the new address.")],
  ["can't change the IP address", "delete the mount target and create"], "EFS mount target", "3.1.K2", rel="extended"))
F.append(f("efs-mount-target-vpc-change-requires-deleting-targets", "restriction",
  "To modify the VPC for mount targets you must first delete the existing mount targets.",
  "What must you do to move an EFS file system's mount targets to another VPC?",
  [(AF, "If you want to modify the VPC for mount targets, then you need to first delete the existing mount targets.")],
  ["first delete the existing mount targets", "modify the VPC for mount targets"], "EFS mount target", "3.1.K2", rel="extended"))
F.append(f("efs-mount-target-created-at-or-after-file-system-creation", "capability",
  "You can create a mount target when you create the file system or after, and later you can add mount targets, delete them, and change their security groups.",
  "When can you create or change EFS mount targets?",
  [(AF, "You can create the mount target when you create the file system or after you create the file system."),
   (AF, "After a mount target is created for a file system, you can create additional mount targets, delete mount targets, and modify the security groups for mount targets.")],
  ["create additional mount targets", "modify the security groups for mount targets"], "EFS mount target", "3.1.K2", rel="reference"))
emit("facts-behavior-05.json", F)
