facts card: 605 facts
s3-access-analyzer-public-or-other-accounts
  claim: IAM Access Analyzer for S3 alerts you when a bucket is configured to allow access to anyone on the internet or to other AWS accounts, including accounts outside your organization.
  scope: S3 buckets.
  link: [IAM Access Analyzer for S3](../facts/s3.md#s3-access-analyzer-public-or-other-accounts)
s3-access-grants-identities
  claim: S3 Access Grants maps identities to S3 datasets by prefix, bucket or object, granting read-only, write-only or read-write access to IAM principals and directly to users or groups from a corporate directory through IAM Identity Center.
  scope: per Access Grants instance.
  link: [a simplified model for defining access permissions](../facts/s3.md#s3-access-grants-identities)
  link: [users or groups from your corporate directory](../facts/s3.md#s3-access-grants-identities)
  link: [read-only, write-only, or read-write access](../facts/s3.md#s3-access-grants-identities)
s3-access-log-destination-must-use-sse-s3
  claim: A bucket that receives server access logs must use SSE-S3; with SSE-KMS default encryption the log objects may be written with a key you cannot access.
  scope: per log destination bucket.
  link: [must use Amazon S3 managed keys (SSE-S3)](../facts/s3.md#s3-access-log-destination-must-use-sse-s3)
  link: [encrypted with a key that you can't access](../facts/s3.md#s3-access-log-destination-must-use-sse-s3)
s3-access-logging-vs-cloudtrail-identity
  claim: A bucket can write server access log records for all requests made against it; customers who need IAM or user identity in their logs use CloudTrail data events instead.
  scope: per bucket.
  link: [can configure AWS CloudTrail Data Events](../facts/s3.md#s3-access-logging-vs-cloudtrail-identity)
  link: [access log records for all requests](../facts/s3.md#s3-access-logging-vs-cloudtrail-identity)
s3-access-point-definition
  claim: An access point is a named network endpoint with its own access policy, attached to a data source such as a general purpose bucket, that simplifies managing access at scale to shared datasets.
  scope: Amazon S3 access points.
  link: [named network endpoints with dedicated access policies](../facts/s3.md#s3-access-point-definition)
  link: [simplify managing data access at scale](../facts/s3.md#s3-access-point-definition)
s3-access-point-needs-bucket-permission-too
  claim: To access objects through an access point, both the access point policy and the underlying bucket must permit the request; AWS recommends delegating access control from the bucket to its access points for buckets that need no direct access.
  scope: per request through an access point.
  link: [both the access point and the underlying bucket](../facts/s3.md#s3-access-point-needs-bucket-permission-too)
  link: [delegate access control for a bucket](../facts/s3.md#s3-access-point-needs-bucket-permission-too)
s3-access-point-network-origin-vpc
  claim: An access point has a network origin of Internet or VPC. With network origin VPC, S3 rejects every request that does not come from the named VPC; the network origin is set at creation and cannot be changed afterwards.
  scope: per access point; fixed; set with VpcConfiguration at creation.
  link: [doesn't originate from that VPC](../facts/s3.md#s3-access-point-network-origin-vpc)
  link: [you can't change its network origin](../facts/s3.md#s3-access-point-network-origin-vpc)
  link: [network origin of Internet](../facts/s3.md#s3-access-point-network-origin-vpc)
s3-access-point-policy-like-bucket-policy
  claim: An access point policy is written like a bucket policy with the access point ARN as the resource. S3 evaluates all relevant policies (user, bucket, access point, VPC endpoint, SCPs and ACLs) when it authorizes a request through an access point.
  scope: per access point.
  link: [like you would a bucket policy](../facts/s3.md#s3-access-point-policy-like-bucket-policy)
  link: [evaluates all the relevant policies](../facts/s3.md#s3-access-point-policy-like-bucket-policy)
s3-access-point-policy-only-through-access-point
  claim: Restrictions in an access point policy apply only to requests made through that access point; attaching an access point does not change how the bucket handles requests made directly to it.
  scope: per access point policy.
  link: [only to requests made through that access point](../facts/s3.md#s3-access-point-policy-only-through-access-point)
s3-access-point-vpc-endpoint-policy-both
  claim: To use a VPC-restricted access point, the VPC endpoint policy must grant access to both the access point and the underlying bucket; requests through the access point succeed only then.
  scope: per VPC endpoint.
  link: [the VPC endpoint policy grants access to both](../facts/s3.md#s3-access-point-vpc-endpoint-policy-both)
s3-access-point-vpc-only
  claim: Each access point has its own access point policy, Block Public Access settings can be configured for each access point attached to a bucket, and any access point can be configured to accept requests only from a virtual private cloud (VPC) to restrict S3 data access to a private network.
  scope: per access point.
  link: [accept requests only from a virtual private cloud](../facts/s3.md#s3-access-point-vpc-only)
  link: [its own access point policy](../facts/s3.md#s3-access-point-vpc-only)
s3-access-point-vs-bucket-policy-vpc-lockdown
  claim: Bucket policies can still limit a bucket to specified VPCs, but access points give an easier, auditable way to lock all or part of a shared dataset to VPC-only traffic; an Organizations SCP can require that every new access point sets its network origin to vpc.
  scope: access control design choice.
  link: [an easier, auditable way to lock down](../facts/s3.md#s3-access-point-vs-bucket-policy-vpc-lockdown)
  link: [any access point created in your organization](../facts/s3.md#s3-access-point-vs-bucket-policy-vpc-lockdown)
s3-access-points-object-operations-only
  claim: Access points can be used only for operations on objects, such as GetObject and PutObject, not for other bucket operations like deleting buckets or creating replication configurations. When attached to a bucket, the access point policy works together with the bucket policy.
  scope: per access point.
  link: [to perform operations on objects](../facts/s3.md#s3-access-points-object-operations-only)
  link: [works in conjunction with the underlying bucket policy](../facts/s3.md#s3-access-points-object-operations-only)
s3-access-points-quota
  claim: An account can create 10,000 S3 Access Points per Region by default, and the quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [10,000](../facts/s3.md#s3-access-points-quota)
  say: ten thousand
s3-access-points-scale-policy-space
  claim: IAM and bucket policies are the simplest approach for a small to medium number of datasets but are bounded by the 20 KB bucket policy and 5 KB IAM policy size limits; access points give far more policy space because each access point has its own policy of up to 20 KB and there can be thousands per Region per account.
  scope: per account; maximum.
  link: [policy size limits of S3 bucket policies (20 KB) and IAM policies (5 KB)](../facts/s3.md#s3-access-points-scale-policy-space)
  link: [significantly more space for policy statements](../facts/s3.md#s3-access-points-scale-policy-space)
  link: [thousands of access points per AWS Region per account, with a policy up to 20 KB in size for each access point](../facts/s3.md#s3-access-points-scale-policy-space)
s3-account-regional-namespace-never-reused
  claim: Only your account can create general purpose buckets in your account regional namespace, and these bucket names can never be re-created by another account.
  scope: account regional namespace.
  link: [can never be re-created by another account](../facts/s3.md#s3-account-regional-namespace-never-reused)
  link: [Only your account can create general purpose buckets](../facts/s3.md#s3-account-regional-namespace-never-reused)
s3-acl-definition-and-default
  claim: An ACL is attached to each bucket and object as a subresource and lists which AWS accounts or groups get which type of access. When a bucket or object is created, S3 makes a default ACL that grants the resource owner full control.
  scope: per bucket and object; default.
  link: [which AWS accounts or groups are granted access](../facts/s3.md#s3-acl-definition-and-default)
  link: [grants the resource owner full control](../facts/s3.md#s3-acl-definition-and-default)
s3-acl-writes-fail-when-bucket-owner-enforced
  claim: With the Bucket owner enforced setting, you must use policies to grant access; requests that set or update an ACL fail with AccessControlListNotSupported, while reading ACLs still works.
  scope: per general purpose bucket; Object Ownership set to Bucket owner enforced.
  link: [AccessControlListNotSupported](../facts/s3.md#s3-acl-writes-fail-when-bucket-owner-enforced)
  link: [you must use policies to grant access](../facts/s3.md#s3-acl-writes-fail-when-bucket-owner-enforced)
s3-acls-not-recommended
  claim: Most modern S3 use cases no longer need ACLs. AWS recommends keeping ACLs disabled except when you need to control access for each object individually.
  scope: general purpose buckets.
  link: [keep ACLs disabled](../facts/s3.md#s3-acls-not-recommended)
  link: [control access for each object individually](../facts/s3.md#s3-acls-not-recommended)
s3-archive-batch-operations-restore-throughput
  claim: S3 Batch Operations can retrieve many archived objects with a single request, which uses the full restore-request rate of your account; restore requests are throttled above the account rate and S3 returns a ThrottlingException.
  scope: per AWS account.
  link: [retrieve many objects with a single request](../facts/s3.md#s3-archive-batch-operations-restore-throughput)
  link: [Amazon S3 returns a ThrottlingException error](../facts/s3.md#s3-archive-batch-operations-restore-throughput)
s3-archive-classes-access-model
  claim: S3 Glacier Instant Retrieval gives millisecond retrieval for rarely accessed long-term data and is available for real-time access. S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive are archived and not available for real-time access; the archive classes require minimum storage durations and retrieval fees.
  scope: S3 Glacier storage classes.
  link: [requires milliseconds retrieval](../facts/s3.md#s3-archive-classes-access-model)
  link: [archived, and not available for real-time access](../facts/s3.md#s3-archive-classes-access-model)
  link: [require minimum storage durations and retrieval fees](../facts/s3.md#s3-archive-classes-access-model)
s3-archive-classes-min-duration-and-retrieval-fees
  claim: The S3 Glacier storage classes (Instant Retrieval, Flexible Retrieval and Deep Archive) are designed for low-cost long-term data storage; they require minimum storage durations and retrieval fees, which makes them most effective for rarely accessed data.
  scope: S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive.
  link: [minimum storage durations and retrieval fees](../facts/s3.md#s3-archive-classes-min-duration-and-retrieval-fees)
  link: [most effective for rarely accessed data](../facts/s3.md#s3-archive-classes-min-duration-and-retrieval-fees)
s3-archive-metadata-overhead
  claim: Each object archived to S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive carries 40 KB of extra metadata: 8 KB billed at S3 Standard rates (name and metadata, so the object still lists in real time) and 32 KB billed at the Glacier class rate (index data needed to restore it).
  scope: per object archived to S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive; fixed.
  link: [40 KB](../facts/s3.md#s3-archive-metadata-overhead)
  link: [8 KB](../facts/s3.md#s3-archive-metadata-overhead)
  link: [32 KB](../facts/s3.md#s3-archive-metadata-overhead)
  say: forty kilobytes | eight kilobytes | thirty-two kilobytes
s3-archive-min-duration
  claim: The minimum storage duration is 90 days for S3 Glacier Flexible Retrieval and 180 days for S3 Glacier Deep Archive; deleting or overwriting an archived object inside that period costs a prorated early deletion fee.
  scope: per object in S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive; minimum.
  link: [90 days](../facts/s3.md#s3-archive-min-duration)
  link: [180 days](../facts/s3.md#s3-archive-min-duration)
  link: [prorated early deletion fee](../facts/s3.md#s3-archive-min-duration)
  say: ninety days | one hundred eighty days | a prorated early deletion fee
s3-archive-objects-stay-in-s3
  claim: Objects in the S3 Glacier storage classes remain in Amazon S3; you cannot access them through the separate Amazon Glacier (vault) service.
  scope: S3 Glacier storage classes.
  link: [your objects remain in Amazon S3](../facts/s3.md#s3-archive-objects-stay-in-s3)
  link: [can't access them directly](../facts/s3.md#s3-archive-objects-stay-in-s3)
s3-archive-one-restore-at-a-time
  claim: S3 processes only one restore request at a time per object.
  scope: per archived object.
  link: [one restore request at a time per object](../facts/s3.md#s3-archive-one-restore-at-a-time)
  say: one restore at a time per object
s3-archive-provisioned-capacity-requester-buys
  claim: Provisioned capacity helps ensure that retrieval capacity for Expedited retrievals from S3 Glacier Flexible Retrieval is available when you need it; without it, Expedited retrievals might not be accepted during periods of high demand. Provisioned capacity units are allocated to an AWS account, so the requester of the Expedited data retrieval, not the bucket owner, should purchase them.
  scope: per AWS account.
  link: [your retrieval capacity for Expedited retrievals](../facts/s3.md#s3-archive-provisioned-capacity-requester-buys)
  link: [Expedited retrievals might not be accepted](../facts/s3.md#s3-archive-provisioned-capacity-requester-buys)
  link: [the requester of the Expedited data retrieval](../facts/s3.md#s3-archive-provisioned-capacity-requester-buys)
s3-archive-provisioned-capacity-unit
  claim: One unit of provisioned capacity guarantees at least 3 Expedited retrievals every 5 minutes from S3 Glacier Flexible Retrieval and up to 300 megabytes per second of retrieval throughput; without it, Expedited retrievals might not be accepted during periods of high demand.
  scope: per provisioned capacity unit; minimum; Expedited retrievals from S3 Glacier Flexible Retrieval.
  link: [3 Expedited retrievals every 5 minutes](../facts/s3.md#s3-archive-provisioned-capacity-unit)
  link: [300 megabytes per second](../facts/s3.md#s3-archive-provisioned-capacity-unit)
  say: three expedited retrievals every five minutes | three hundred megabytes per second
s3-archive-restore-needed-flexible-deep
  claim: Objects in S3 Glacier Instant Retrieval are immediately available with GET, but data in S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive must first be retrieved with the RestoreObject API.
  scope: S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive.
  link: [immediately available using GET](../facts/s3.md#s3-archive-restore-needed-flexible-deep)
  link: [retrieve data using the RestoreObject REST API](../facts/s3.md#s3-archive-restore-needed-flexible-deep)
s3-archive-restore-request-rate
  claim: When you initiate restore requests for objects in S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive or S3 Intelligent-Tiering, a retrieval-requests quota applies to your AWS account: S3 Glacier supports restore requests at a rate of 1,000 transactions per second. Above that rate, otherwise valid requests are throttled or rejected with a ThrottlingException error; S3 Batch Operations can retrieve many objects with a single request.
  scope: per AWS account; maximum; adjustable; RestoreObject requests for S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive or S3 Intelligent-Tiering objects; increased restoration limits through AWS Support.
  link: [1,000 transactions per second](../facts/s3.md#s3-archive-restore-request-rate)
  say: one thousand transactions per second
s3-archive-restore-temporary-copy
  claim: Before you can access an archived object, you must restore a temporary copy of it. The restored copy is available only for the duration that you specify in the restore request; then S3 deletes the temporary copy, the object remains archived, and its storage class still reads as S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive. While the copy exists, you pay for both the archive (at the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive rate) and the temporary copy (at the S3 Standard storage rate). S3 processes only one restore request at a time per object.
  scope: per archived object.
  link: [restore a temporary copy of it](../facts/s3.md#s3-archive-restore-temporary-copy)
  link: [available only for the duration that you specify](../facts/s3.md#s3-archive-restore-temporary-copy)
  link: [the object's storage class remains](../facts/s3.md#s3-archive-restore-temporary-copy)
  link: [only one restore request at a time](../facts/s3.md#s3-archive-restore-temporary-copy)
s3-archive-restore-throughput
  claim: S3 Glacier restores large datasets at up to 1–2 petabytes per day per customer account; any object larger than 5 terabytes restores at up to 300 megabytes per second, so a 50-terabyte S3 Glacier Flexible Retrieval object could take up to 48 hours.
  scope: per customer account; maximum; adjustable; contact AWS Support for higher restoration limits.
  link: [1–2 petabytes per day](../facts/s3.md#s3-archive-restore-throughput)
  link: [300 megabytes per second](../facts/s3.md#s3-archive-restore-throughput)
  say: one to two petabytes per day | three hundred megabytes per second
s3-archive-retrieval-options-three
  claim: A restore chooses one of three retrieval options by speed: Expedited, Standard and Bulk. Standard is the default when no option is given; Bulk is the lowest-cost option; Expedited is a premium option charged at the Expedited rate and is not available for S3 Glacier Deep Archive.
  scope: per restore request; default; Expedited is not available for S3 Glacier Deep Archive.
  link: [Expedited, Standard and Bulk](../facts/s3.md#s3-archive-retrieval-options-three)
  link: [Standard is the default option](../facts/s3.md#s3-archive-retrieval-options-three)
  link: [the lowest-cost retrieval option](../facts/s3.md#s3-archive-retrieval-options-three)
  link: [Expedited retrievals are a premium feature](../facts/s3.md#s3-archive-retrieval-options-three)
s3-archive-retrieval-times-deep
  claim: From S3 Glacier Deep Archive or the Intelligent-Tiering Deep Archive Access tier, Expedited retrieval is not available, Standard completes within 12 hours (9-12 hours with Batch Operations) and Bulk within 48 hours.
  scope: S3 Glacier Deep Archive or S3 Intelligent-Tiering Deep Archive Access.
  link: [Within 12 hours](../facts/s3.md#s3-archive-retrieval-times-deep)
  link: [Within 48 hours](../facts/s3.md#s3-archive-retrieval-times-deep)
  link: [Not available](../facts/s3.md#s3-archive-retrieval-times-deep)
  say: within twelve hours | within forty-eight hours | not available
s3-archive-retrieval-times-flexible
  claim: From S3 Glacier Flexible Retrieval or the S3 Intelligent-Tiering Archive Access tier, typical retrieval times are: Expedited 1–5 minutes for objects under 250 megabytes, Standard 3–5 hours (Minutes–5 hours with Batch Operations) and Bulk 5–12 hours.
  scope: S3 Glacier Flexible Retrieval or S3 Intelligent-Tiering Archive Access; typical times; the Expedited time is for objects under 250 megabytes.
  link: [1–5 minutes](../facts/s3.md#s3-archive-retrieval-times-flexible)
  link: [3–5 hours](../facts/s3.md#s3-archive-retrieval-times-flexible)
  link: [5–12 hours](../facts/s3.md#s3-archive-retrieval-times-flexible)
  say: one to five minutes | three to five hours | five to twelve hours
s3-authorization-both-accounts-must-allow
  claim: To act on an S3 resource, an IAM principal needs permission from both its own parent AWS account and the AWS account that owns the resource; for a bucket operation, the bucket owner must have granted the permission.
  scope: per request.
  link: [permission from both the parent AWS account](../facts/s3.md#s3-authorization-both-accounts-must-allow)
  link: [the bucket owner has granted permission](../facts/s3.md#s3-authorization-both-accounts-must-allow)
s3-authorization-evaluation-order
  claim: S3 evaluates all the relevant access policies, user policies and resource-based policies (bucket policy, bucket ACL and object ACL) in deciding whether to authorize a request. A bucket operation needs permission from the bucket owner; for an object request, S3 evaluates all the policies owned by the bucket owner, and if there is an explicit deny set, S3 does not authorize the request. In the user context, the parent account to which the user belongs is the context authority.
  scope: per request.
  link: [evaluates all the relevant access policies](../facts/s3.md#s3-authorization-evaluation-order)
  link: [If there is an explicit deny set](../facts/s3.md#s3-authorization-evaluation-order)
  link: [user context](../facts/s3.md#s3-authorization-evaluation-order)
s3-availability-sla
  claim: The availability SLA is 99.9% for S3 Standard, S3 Express One Zone, S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive, and 99% for S3 Intelligent-Tiering, S3 Standard-IA, S3 One Zone-IA and S3 Glacier Instant Retrieval.
  scope: per storage class, per billing month; the SLA figure, lower than the designed-for availability.
  link: [99.9%](../facts/s3.md#s3-availability-sla)
  link: [99%](../facts/s3.md#s3-availability-sla)
  say: ninety-nine point nine percent | ninety-nine percent
s3-aws-backup-requires-versioning
  claim: AWS Backup can make continuous backups (for point-in-time restore) and periodic backups (for long-term retention) of S3 data and restore to a point in time you choose. S3 Versioning must be turned on before AWS Backup can back up a bucket.
  scope: per bucket.
  link: [continuous backups and periodic backups](../facts/s3.md#s3-aws-backup-requires-versioning)
  link: [continuous backups are useful for point-in-time restore](../facts/s3.md#s3-aws-backup-requires-versioning)
  link: [must activate S3 Versioning on your bucket](../facts/s3.md#s3-aws-backup-requires-versioning)
s3-az-loss-resilience
  claim: Every storage class except S3 One Zone-IA and S3 Express One Zone is designed to survive the physical loss of an entire Availability Zone.
  scope: per storage class.
  link: [except for S3 One Zone-IA](../facts/s3.md#s3-az-loss-resilience)
  say: all classes except One Zone-IA and Express One Zone
s3-backup-continuous-vs-periodic
  claim: AWS Backup for S3 offers continuous backups for point-in-time restore and periodic backups for long-term retention; alongside it, S3 Versioning and S3 Replication support self-recovery from accidental deletions.
  scope: AWS Backup for Amazon S3.
  link: [Continuous backups are useful for point-in-time restore](../facts/s3.md#s3-backup-continuous-vs-periodic)
  link: [useful to meet your long-term data-retention needs](../facts/s3.md#s3-backup-continuous-vs-periodic)
s3-backup-set-lifecycle-expiration-for-versions
  claim: For a versioned bucket that AWS Backup protects, set a lifecycle expiration rule; otherwise storage cost can grow because every version is retained.
  scope: versioning-enabled buckets backed up by AWS Backup.
  link: [AWS Backup retains all versions](../facts/s3.md#s3-backup-set-lifecycle-expiration-for-versions)
  link: [set a lifecycle expiration rule for versioning-enabled buckets](../facts/s3.md#s3-backup-set-lifecycle-expiration-for-versions)
s3-batch-operations-definition
  claim: S3 Batch Operations runs one operation on a list of objects you specify; a single job can act on billions of objects, and S3 tracks progress, sends notifications and stores a completion report.
  scope: per Batch Operations job.
  link: [perform a single operation on lists](../facts/s3.md#s3-batch-operations-definition)
  link: [a specified operation on billions of objects](../facts/s3.md#s3-batch-operations-definition)
  link: [tracks progress, sends notifications](../facts/s3.md#s3-batch-operations-definition)
s3-batch-operations-manifest
  claim: A Batch Operations job needs a manifest: an S3 object listing the bucket name, object key and optionally the version of each object, in the form of an S3 Inventory report or a CSV file. S3 can also generate the manifest from object filter criteria you set.
  scope: per Batch Operations job.
  link: [contains the object keys](../facts/s3.md#s3-batch-operations-manifest)
  link: [Inventory report or a CSV file](../facts/s3.md#s3-batch-operations-manifest)
  link: [you must supply a manifest](../facts/s3.md#s3-batch-operations-manifest)
s3-batch-operations-supported-operations
  claim: Batch Operations can copy objects, update their server-side encryption, set object tags or ACLs, start restores from S3 Glacier Flexible Retrieval, and invoke a Lambda function for custom actions. The object list comes from a custom list or an S3 Inventory report.
  scope: per Batch Operations job.
  link: [copy objects, update server-side encryption of objects](../facts/s3.md#s3-batch-operations-supported-operations)
  link: [invoke an AWS Lambda function](../facts/s3.md#s3-batch-operations-supported-operations)
  link: [use an Amazon S3 Inventory report](../facts/s3.md#s3-batch-operations-supported-operations)
s3-batch-replication-for-existing-objects
  claim: Live replication (CRR and SRR) automatically replicates newly uploaded objects as they are written to the bucket; S3 Batch Replication replicates existing objects, as fully managed S3 Batch Operations jobs.
  scope: per replication configuration.
  link: [replicates newly uploaded objects as they are written](../facts/s3.md#s3-batch-replication-for-existing-objects)
  link: [allows you to replicate existing objects](../facts/s3.md#s3-batch-replication-for-existing-objects)
s3-best-practice-bucket-not-public
  claim: AWS security best practice: unless you explicitly need anyone on the internet to read or write the bucket, make sure the bucket is not public.
  scope: per bucket; unless you explicitly require public read or write access.
  link: [your S3 bucket is not public](../facts/s3.md#s3-best-practice-bucket-not-public)
s3-best-practice-iam-roles-not-stored-credentials
  claim: AWS recommends not storing AWS credentials in an application or EC2 instance; use an IAM role so the application gets temporary credentials for S3 access.
  scope: applications on EC2 and other AWS services.
  link: [use an IAM role to manage temporary credentials](../facts/s3.md#s3-best-practice-iam-roles-not-stored-credentials)
  link: [not storing AWS credentials directly in the application](../facts/s3.md#s3-best-practice-iam-roles-not-stored-credentials)
s3-best-practice-least-privilege
  claim: AWS recommends granting only the permissions required to perform a task (least privilege) on S3 resources, to reduce the impact of errors or malicious intent.
  scope: IAM and bucket policies for S3.
  link: [grant only the permissions that are required](../facts/s3.md#s3-best-practice-least-privilege)
s3-best-practice-wildcard-principal-means-anyone
  claim: A bucket policy that allows a wildcard identity, "Principal": "*", effectively means anyone; a wildcard action "*" allows any action in the bucket. Both are signs of a public or over-permissive bucket.
  scope: bucket policies.
  link: [which effectively means "anyone"](../facts/s3.md#s3-best-practice-wildcard-principal-means-anyone)
  link: [perform any action in the Amazon S3 bucket](../facts/s3.md#s3-best-practice-wildcard-principal-means-anyone)
s3-billing-early-delete-deep-archive-usage-type
  claim: In the S3 usage report, the usage type EarlyDelete-GDA (in GB-Hours, hourly) is the prorated storage usage for objects deleted from S3 Glacier Deep Archive before the 180-day minimum commitment ended.
  scope: per object, S3 Glacier Deep Archive; minimum; object removed before the minimum storage duration.
  link: [EarlyDelete-GDA](../facts/s3.md#s3-billing-early-delete-deep-archive-usage-type)
  link: [180-day minimum commitment](../facts/s3.md#s3-billing-early-delete-deep-archive-usage-type)
  say: EarlyDelete GDA | one hundred eighty-day minimum commitment
s3-billing-early-delete-flexible-usage-type
  claim: In the S3 usage report, the usage type EarlyDelete-ByteHrs (in GB-Hours, hourly) is the prorated storage usage for objects deleted from S3 Glacier Flexible Retrieval before the 90-day minimum commitment ended.
  scope: per object, S3 Glacier Flexible Retrieval; minimum; object removed before the minimum storage duration.
  link: [EarlyDelete-ByteHrs](../facts/s3.md#s3-billing-early-delete-flexible-usage-type)
  link: [90-day minimum commitment](../facts/s3.md#s3-billing-early-delete-flexible-usage-type)
  say: EarlyDelete ByteHrs | ninety-day minimum commitment
s3-billing-early-delete-glacier-ir-usage-type
  claim: In the S3 usage report, the usage type EarlyDelete-GIR (in GB-Hours, hourly) is the prorated storage usage for objects deleted or transitioned from S3 Glacier Instant Retrieval before the 90-day minimum commitment ended.
  scope: per object, S3 Glacier Instant Retrieval; minimum; object removed before the minimum storage duration.
  link: [EarlyDelete-GIR](../facts/s3.md#s3-billing-early-delete-glacier-ir-usage-type)
  link: [90-day minimum commitment](../facts/s3.md#s3-billing-early-delete-glacier-ir-usage-type)
  say: EarlyDelete GIR | ninety-day minimum commitment
s3-billing-early-delete-standard-ia-usage-type
  claim: In the S3 usage report, the usage type EarlyDelete-SIA (in GB-Hours, hourly) is the prorated storage usage for objects deleted from S3 Standard-IA before the 30-day minimum commitment ended.
  scope: per object, S3 Standard-IA; minimum; object removed before the minimum storage duration.
  link: [EarlyDelete-SIA](../facts/s3.md#s3-billing-early-delete-standard-ia-usage-type)
  link: [30-day minimum commitment](../facts/s3.md#s3-billing-early-delete-standard-ia-usage-type)
  say: EarlyDelete SIA | thirty-day minimum commitment
s3-block-public-access-account-level-recommended
  claim: A Block Public Access setting applied to an account applies to all buckets and access points that the account owns, and account settings apply to all AWS Regions globally (they might not take effect in all Regions at once). AWS recommends turning on all four settings for the account, and recommends applying BlockPublicPolicy at the account level: then S3 blocks public policies even if a user alters the bucket policy to disable this setting.
  scope: per account.
  link: [applies to all buckets and access points](../facts/s3.md#s3-block-public-access-account-level-recommended)
  link: [the settings apply to all AWS Regions globally](../facts/s3.md#s3-block-public-access-account-level-recommended)
  link: [turn on all four settings](../facts/s3.md#s3-block-public-access-account-level-recommended)
s3-block-public-access-centralized-controls
  claim: S3 Block Public Access gives centralized controls that limit public access to S3 resources, and these controls are enforced regardless of how the resources were created; it can also be enforced organization-wide through AWS Organizations.
  scope: per account, per bucket, or per organization.
  link: [enforced regardless of how the resources are created](../facts/s3.md#s3-block-public-access-centralized-controls)
  link: [organization-level enforcement through AWS Organizations](../facts/s3.md#s3-block-public-access-centralized-controls)
s3-block-public-access-default-on
  claim: Block Public Access settings are turned on at the bucket level by default. AWS recommends keeping all four settings enabled unless a specific use case needs one turned off.
  scope: per bucket; default; adjustable.
  link: [turned on at the bucket level](../facts/s3.md#s3-block-public-access-default-on)
  link: [keep all Block Public Access settings enabled](../facts/s3.md#s3-block-public-access-default-on)
s3-block-public-access-four-settings-most-restrictive
  claim: Block Public Access has four independent settings (BlockPublicAcls, IgnorePublicAcls, BlockPublicPolicy, RestrictPublicBuckets) that can be applied to an access point, a bucket or a whole account in any combination. When the settings at different levels differ, S3 applies the most restrictive combination.
  scope: per access point, bucket or account.
  link: [four settings](../facts/s3.md#s3-block-public-access-four-settings-most-restrictive)
  link: [applies the most restrictive combination](../facts/s3.md#s3-block-public-access-four-settings-most-restrictive)
  link: [BlockPublicAcls](../facts/s3.md#s3-block-public-access-four-settings-most-restrictive)
  link: [IgnorePublicAcls](../facts/s3.md#s3-block-public-access-four-settings-most-restrictive)
  link: [RestrictPublicBuckets](../facts/s3.md#s3-block-public-access-four-settings-most-restrictive)
  link: [BlockPublicPolicy](../facts/s3.md#s3-block-public-access-four-settings-most-restrictive)
s3-block-public-access-not-per-object
  claim: Block Public Access settings exist only for organizations, access points, buckets and accounts; S3 does not support them per object. Removing a setting makes a bucket or object with a public policy or ACL public again, because the settings never change the policies or ACLs themselves.
  scope: Block Public Access.
  link: [on a per-object basis](../facts/s3.md#s3-block-public-access-not-per-object)
  link: [don't alter existing policies or ACLs](../facts/s3.md#s3-block-public-access-not-per-object)
s3-block-public-access-overrides-policies
  claim: By default new buckets, access points and objects do not allow public access, but policies and permissions can be edited to allow it; Block Public Access settings override those policies and permissions so that public access stays limited.
  scope: access points, buckets, accounts and organizations; default.
  link: [settings override these policies and permissions](../facts/s3.md#s3-block-public-access-overrides-policies)
  link: [don't allow public access](../facts/s3.md#s3-block-public-access-overrides-policies)
s3-bpa-org-bucket-most-restrictive
  claim: Account-level Block Public Access settings inherit organization-level policies, and S3 applies the most restrictive of the bucket-level and effective account-level settings, so a bucket with Block Public Access turned off is still protected when the organization policy is on.
  scope: bucket, account and organization Block Public Access.
  link: [takes the most restrictive policy](../facts/s3.md#s3-bpa-org-bucket-most-restrictive)
  say: the most restrictive setting wins
s3-bpa-org-level-overrides-account
  claim: Organization-level Block Public Access policies propagate automatically to the selected member accounts and override account-level settings. At the organization level all four settings are applied together as one policy; you cannot select individual settings.
  scope: organization-level Block Public Access policy.
  link: [override account-level settings](../facts/s3.md#s3-bpa-org-level-overrides-account)
  link: [all four settings are applied together](../facts/s3.md#s3-bpa-org-level-overrides-account)
  say: they override account-level settings | all four settings together
s3-bucket-key-cloudtrail-logs-bucket-arn
  claim: With an S3 Bucket Key enabled, KMS CloudTrail events log the bucket ARN instead of the object ARN, and there are fewer KMS CloudTrail events for SSE-KMS objects.
  scope: per bucket using SSE-KMS with a Bucket Key.
  link: [your bucket ARN instead of your object ARN](../facts/s3.md#s3-bucket-key-cloudtrail-logs-bucket-arn)
s3-bucket-key-kms-cost-up-to-99-percent
  claim: An S3 Bucket Key for SSE-KMS can reduce AWS KMS request costs by up to 99 percent by decreasing the request traffic from S3 to KMS.
  scope: per bucket using SSE-KMS; maximum.
  link: [up to 99 percent](../facts/s3.md#s3-bucket-key-kms-cost-up-to-99-percent)
  say: up to ninety-nine percent
s3-bucket-key-reduces-kms-requests
  claim: With SSE-KMS default encryption you can enable S3 Bucket Keys, which reduce request traffic from S3 to AWS KMS and lower the cost of encryption.
  scope: per bucket; default encryption set to SSE-KMS.
  link: [S3 Bucket Keys](../facts/s3.md#s3-bucket-key-reduces-kms-requests)
  link: [reduce the cost of encryption](../facts/s3.md#s3-bucket-key-reduces-kms-requests)
s3-bucket-name-global-namespace-default
  claim: By default, general purpose buckets exist in a global namespace: each bucket name must be unique across all AWS accounts in all Regions within a partition. You can instead create a bucket in your account regional namespace, a subdivision of the global namespace that only your account can create buckets in.
  scope: general purpose buckets, per partition; default; adjustable; the account regional namespace is an opt-in alternative.
  link: [unique across all AWS accounts](../facts/s3.md#s3-bucket-name-global-namespace-default)
  link: [global namespace](../facts/s3.md#s3-bucket-name-global-namespace-default)
  link: [account regional namespace](../facts/s3.md#s3-bucket-name-global-namespace-default)
s3-bucket-name-region-fixed
  claim: After you create a bucket, you cannot change its name or its AWS Region, and bucket ownership cannot be transferred to another account.
  scope: per general purpose bucket; fixed.
  link: [can't change its name or Region](../facts/s3.md#s3-bucket-name-region-fixed)
  say: cannot change the name or the Region
s3-bucket-no-size-limit
  claim: A bucket has no maximum size and no limit on the number of objects it can store; you can keep all objects in one bucket, but a bucket cannot be created inside another bucket.
  scope: per general purpose bucket.
  link: [no max bucket size](../facts/s3.md#s3-bucket-no-size-limit)
  link: [can't create a bucket from within another bucket](../facts/s3.md#s3-bucket-no-size-limit)
  say: no maximum bucket size
s3-bucket-owner-can-deny-and-delete-any-object
  claim: The bucket owner, who pays the bill, can explicitly deny access to any object in the bucket regardless of who owns it, and can delete any object in the bucket.
  scope: per bucket.
  link: [regardless of who owns it](../facts/s3.md#s3-bucket-owner-can-deny-and-delete-any-object)
  link: [can also delete any object in the bucket](../facts/s3.md#s3-bucket-owner-can-deny-and-delete-any-object)
s3-bucket-policy-cannot-stop-lifecycle
  claim: A bucket policy cannot prevent deletions or transitions made by an S3 Lifecycle rule; even a policy that denies all actions to all principals leaves the Lifecycle configuration working.
  scope: per bucket.
  link: [can't use a bucket policy to prevent deletions](../facts/s3.md#s3-bucket-policy-cannot-stop-lifecycle)
  link: [still functions as normal](../facts/s3.md#s3-bucket-policy-cannot-stop-lifecycle)
s3-bucket-policy-cross-account-upload-owner-control
  claim: A bucket policy can grant another account cross-account permission to upload objects while ensuring that the bucket owner has full control of the uploaded objects.
  scope: S3 bucket policies.
  link: [grants cross-account permissions to upload objects](../facts/s3.md#s3-bucket-policy-cross-account-upload-owner-control)
s3-bucket-policy-deny-outside-org
  claim: A Deny statement with the aws:PrincipalOrgID condition blocks every principal outside your AWS Organization; a Deny overrides any Allow no matter how access was granted.
  scope: per bucket policy.
  link: [aws:PrincipalOrgID](../facts/s3.md#s3-bucket-policy-deny-outside-org)
  link: [A Deny statement overrides any Allow](../facts/s3.md#s3-bucket-policy-deny-outside-org)
s3-bucket-policy-max-size
  claim: A bucket policy is limited to 20 KB in size, and identity-based policies have the same 20 KB size limit; complex access permission requirements might exceed this limit.
  scope: per bucket policy; maximum; not adjustable.
  link: [20 KB](../facts/s3.md#s3-bucket-policy-max-size)
  say: twenty kilobytes
s3-bucket-policy-not-other-accounts-objects
  claim: Bucket policy permissions apply to the objects in the bucket that the bucket owner owns; they do not apply to objects owned by other AWS accounts.
  scope: per bucket; ACLs enabled so that other accounts can own objects.
  link: [don't apply to objects that are owned](../facts/s3.md#s3-bucket-policy-not-other-accounts-objects)
  link: [owned by the bucket owner](../facts/s3.md#s3-bucket-policy-not-other-accounts-objects)
s3-bucket-policy-object-tag-condition
  claim: A policy can limit a user to reading only objects that carry a given tag key and value, using the s3:ExistingObjectTag condition key.
  scope: per policy statement.
  link: [s3:ExistingObjectTag](../facts/s3.md#s3-bucket-policy-object-tag-condition)
  link: [limits a user to only reading objects](../facts/s3.md#s3-bucket-policy-object-tag-condition)
s3-bucket-policy-owner-only
  claim: A bucket policy is a resource-based IAM policy that grants access to the bucket and its objects. Only the bucket owner can attach a policy to a bucket, and its permissions apply to the objects in the bucket that the bucket owner owns.
  scope: per bucket.
  link: [resource-based AWS Identity and Access Management (IAM) policy](../facts/s3.md#s3-bucket-policy-owner-only)
  link: [Only the bucket owner can associate a policy](../facts/s3.md#s3-bucket-policy-owner-only)
  link: [owned by the bucket owner](../facts/s3.md#s3-bucket-policy-owner-only)
s3-bucket-policy-require-mfa-condition
  claim: A bucket policy can require MFA with the aws:MultiFactorAuthAge condition key, which gives the age in seconds of temporary credentials created with an MFA device and is absent when the credentials were not created with MFA.
  scope: per bucket policy.
  link: [aws:MultiFactorAuthAge](../facts/s3.md#s3-bucket-policy-require-mfa-condition)
  link: [this key value is null (absent)](../facts/s3.md#s3-bucket-policy-require-mfa-condition)
s3-bucket-policy-require-sse-kms-on-put
  claim: A bucket policy can require every object written to the bucket to be encrypted with SSE-KMS and deny the request otherwise. The s3:x-amz-server-side-encryption condition key names the encryption type, for example AES256 for SSE-S3.
  scope: per bucket policy.
  link: [s3:x-amz-server-side-encryption](../facts/s3.md#s3-bucket-policy-require-sse-kms-on-put)
  link: [every object that is written to the bucket](../facts/s3.md#s3-bucket-policy-require-sse-kms-on-put)
  link: [SSE-S3 (AES256)](../facts/s3.md#s3-bucket-policy-require-sse-kms-on-put)
s3-bucket-policy-secure-transport-https-only
  claim: To allow only encrypted HTTPS (TLS) connections, a bucket policy uses the aws:SecureTransport global condition key; it is true for HTTPS requests and false for HTTP, and the example policy explicitly denies HTTP requests.
  scope: per bucket policy.
  link: [aws:SecureTransport](../facts/s3.md#s3-bucket-policy-secure-transport-https-only)
  link: [the request was sent through HTTPS](../facts/s3.md#s3-bucket-policy-secure-transport-https-only)
  link: [explicitly denies HTTP requests](../facts/s3.md#s3-bucket-policy-secure-transport-https-only)
s3-bucket-policy-source-vpce-condition
  claim: A bucket policy can restrict a bucket to one VPC endpoint with the aws:SourceVpce condition, which takes the VPC endpoint ID, not an ARN; when the endpoint is not used, the policy denies all access. Such a policy also blocks console access, because console requests do not come from the endpoint.
  scope: per bucket policy.
  link: [aws:SourceVpce](../facts/s3.md#s3-bucket-policy-source-vpce-condition)
  link: [only the VPC endpoint ID](../facts/s3.md#s3-bucket-policy-source-vpce-condition)
  link: [disables console access to the specified bucket](../facts/s3.md#s3-bucket-policy-source-vpce-condition)
s3-bucket-policy-tls-version-condition
  claim: The s3:TlsVersion condition key lets IAM, VPC endpoint or bucket policies require a minimum TLS version from clients.
  scope: per policy.
  link: [s3:TlsVersion](../facts/s3.md#s3-bucket-policy-tls-version-condition)
  link: [write policies that require a minimum TLS version](../facts/s3.md#s3-bucket-policy-tls-version-condition)
s3-bucket-policy-wildcards-object-subset
  claim: A bucket policy can use wildcard characters in ARNs and other values to grant permissions to a subset of the objects in the bucket.
  scope: S3 bucket policies.
  link: [wildcard characters on Amazon Resource Names (ARNs)](../facts/s3.md#s3-bucket-policy-wildcards-object-subset)
s3-bucket-quota-change-note
  claim: Unpaginated ListBuckets requests are only supported for accounts at the default general purpose bucket quota of 10,000; an account with an approved quota above 10,000 must send paginated ListBuckets requests.
  scope: per AWS account; default; adjustable; quota raised above 10,000.
  link: [default general purpose bucket quota of 10,000](../facts/s3.md#s3-bucket-quota-change-note)
  say: default quota of ten thousand buckets
s3-bucket-quota-default
  claim: An AWS account can create up to 10,000 general purpose buckets by default; you request a higher quota in the Service Quotas console.
  scope: per AWS account; default; adjustable.
  link: [10,000 general purpose buckets](../facts/s3.md#s3-bucket-quota-default)
  say: ten thousand general purpose buckets
s3-bucket-quota-max-1-million
  claim: By default an account can create up to 10,000 general purpose buckets, and any customer can request a quota increase up to 1 million buckets.
  scope: per AWS account; maximum; adjustable; by quota increase request in Service Quotas.
  link: [1 million buckets](../facts/s3.md#s3-bucket-quota-max-1-million)
  link: [10,000 general purpose buckets](../facts/s3.md#s3-bucket-quota-max-1-million)
  say: one million buckets | ten thousand general purpose buckets
s3-bucket-region-fixed
  claim: A bucket is created in one AWS Region that you choose. After you create a bucket, you cannot change its name or its Region.
  scope: per bucket, all bucket types; fixed.
  link: [cannot change the name of the bucket](../facts/s3.md#s3-bucket-region-fixed)
  link: [the AWS Region where the bucket will reside](../facts/s3.md#s3-bucket-region-fixed)
s3-bucket-tags-max
  claim: A bucket can carry at most 50 tags.
  scope: per bucket; maximum; not adjustable.
  link: [50](../facts/s3.md#s3-bucket-tags-max)
  say: fifty
s3-byte-range-fetch-parallel
  claim: Concurrent connections can fetch different byte ranges of the same object, which gives higher aggregate throughput than one whole-object request and shortens retries when a request is interrupted.
  scope: GET requests on one object.
  link: [fetch different byte ranges](../facts/s3.md#s3-byte-range-fetch-parallel)
  link: [higher aggregate throughput](../facts/s3.md#s3-byte-range-fetch-parallel)
  link: [improve retry times](../facts/s3.md#s3-byte-range-fetch-parallel)
s3-case-bynder-changing-access-patterns
  claim: Bynder's data access patterns frequently change, which makes traditional storage options less cost effective; Bynder says that instead of having to review the access pattern of assets by hand, S3 Intelligent-Tiering does it automatically.
  scope: Bynder case study.
  link: [data access patterns frequently change](../facts/s3.md#s3-case-bynder-changing-access-patterns)
  link: [does it for us automatically](../facts/s3.md#s3-case-bynder-changing-access-patterns)
s3-case-bynder-cost-tags-per-bucket
  claim: Bynder puts tags on each S3 bucket so that it can track costs and adjust as needed, and uses AWS Cost Explorer to visualize, understand and manage its AWS costs and usage.
  scope: Bynder case study.
  link: [allocates tags to each Amazon S3 bucket](../facts/s3.md#s3-case-bynder-cost-tags-per-bucket)
s3-case-bynder-intelligent-tiering-65-percent
  claim: Bynder stores 18 PB of customer data, more than 175 million assets, in S3 Intelligent-Tiering, which has led to a storage cost saving of 65 percent.
  scope: Bynder case study.
  link: [18 PB](../facts/s3.md#s3-case-bynder-intelligent-tiering-65-percent)
  link: [more than 175 million assets](../facts/s3.md#s3-case-bynder-intelligent-tiering-65-percent)
  link: [storage cost savings of 65 percent](../facts/s3.md#s3-case-bynder-intelligent-tiering-65-percent)
s3-case-snap-access-pattern-analysis
  claim: Snap first analyzed the access patterns of its data; the analysis showed that S3 Glacier Instant Retrieval would reduce costs because the class is ideal for data that needs immediate access but is accessed only once per quarter. Snap then migrated with S3 Lifecycle policies.
  scope: Snap Inc. case study.
  link: [only accessed once per quarter](../facts/s3.md#s3-case-snap-access-pattern-analysis)
  link: [using Amazon S3 Lifecycle policies](../facts/s3.md#s3-case-snap-access-pattern-analysis)
s3-case-snap-glacier-ir-migration-savings
  claim: Snap moved more than 2 exabytes of data (roughly 1.5 trillion media files) from Amazon S3 Standard-IA to Amazon S3 Glacier Instant Retrieval, and as a result saved tens of millions of dollars on storage.
  scope: Snap Inc. case study.
  link: [more than 2 exabytes of data](../facts/s3.md#s3-case-snap-glacier-ir-migration-savings)
  link: [1.5 trillion media files](../facts/s3.md#s3-case-snap-glacier-ir-migration-savings)
  link: [saved tens of millions of dollars on storage](../facts/s3.md#s3-case-snap-glacier-ir-migration-savings)
s3-change-account-regional-namespace-2026-03
  claim: On 2026-03-12 Amazon S3 added account regional namespaces for general purpose buckets: you can create buckets in your own reserved namespace, a subdivision of the global namespace that only your account can create buckets in, instead of finding globally unique names.
  scope: general purpose buckets; by default buckets are still created in the shared global namespace.
  link: [2026-03-12](../facts/s3.md#s3-change-account-regional-namespace-2026-03)
  link: [account regional namespace](../facts/s3.md#s3-change-account-regional-namespace-2026-03)
  say: March twelfth, twenty twenty-six | an account regional namespace
s3-change-batch-standard-restore-minutes-2023-08
  claim: Since 2023-08-09 Standard retrievals for restore requests made through S3 Batch Operations can start within minutes. For S3 Glacier Flexible Retrieval and the Intelligent-Tiering Archive Access tier they typically start within minutes and finish within 3-5 hours at up to 1–2 petabytes per day; before, the Standard tier began restoring 3–5 hours from job activation.
  scope: Standard retrievals started by S3 Batch Operations, Glacier Flexible Retrieval and Intelligent-Tiering Archive Access; Batch Operations restore only.
  link: [2023-08-09](../facts/s3.md#s3-change-batch-standard-restore-minutes-2023-08)
  link: [typically start within minutes](../facts/s3.md#s3-change-batch-standard-restore-minutes-2023-08)
  link: [3-5 hours](../facts/s3.md#s3-change-batch-standard-restore-minutes-2023-08)
  say: August ninth, twenty twenty-three | they start within minutes | three to five hours
  changed: 2023-08-09: was 3–5 hours from job activation
s3-change-bpa-acls-default-new-buckets-2023-04
  claim: Since 2023-04-27 Amazon S3 automatically enables S3 Block Public Access and disables ACLs for all new buckets in all AWS Regions.
  scope: new buckets, all Regions; default; settings can be changed after creation.
  link: [2023-04-27](../facts/s3.md#s3-change-bpa-acls-default-new-buckets-2023-04)
  link: [Block Public Access turned on by default](../facts/s3.md#s3-change-bpa-acls-default-new-buckets-2023-04)
  link: [ACLs are disabled by default](../facts/s3.md#s3-change-bpa-acls-default-new-buckets-2023-04)
  say: April twenty-seventh, twenty twenty-three | Block Public Access is on by default | ACLs are off by default
s3-change-bpa-organization-level-2025-11
  claim: On 2025-11-26 S3 Block Public Access added organization-level enforcement through AWS Organizations: a policy attached at the root or at an organizational unit propagates to all accounts in that scope, and new member accounts inherit it automatically.
  scope: per organization, root or OU or selected accounts.
  link: [2025-11-26](../facts/s3.md#s3-change-bpa-organization-level-2025-11)
  link: [organization level (using AWS Organizations)](../facts/s3.md#s3-change-bpa-organization-level-2025-11)
  say: November twenty-sixth, twenty twenty-five | at the organization level
s3-change-bucket-quota-10000-2024-11
  claim: By default an AWS account can now create up to 10,000 general purpose buckets, up from the earlier default of 100 buckets, and any customer can request a quota increase up to 1 million buckets.
  scope: general purpose buckets per AWS account; default; increase requested through Service Quotas.
  link: [10,000](../facts/s3.md#s3-change-bucket-quota-10000-2024-11)
  link: [1 million buckets](../facts/s3.md#s3-change-bucket-quota-10000-2024-11)
  say: ten thousand | one million buckets
  changed: 2024-11-14: was 100
s3-change-conditional-deletes-2025-09
  claim: On 2025-09-16 S3 added conditional deletes in general purpose buckets: a delete sent with the if-match header and an ETag succeeds only if the ETag matches the object, and the s3:if-match condition key in a bucket policy can require the header on DeleteObject and DeleteObjects requests.
  scope: general purpose buckets.
  link: [2025-09-16](../facts/s3.md#s3-change-conditional-deletes-2025-09)
  link: [conditional deletes](../facts/s3.md#s3-change-conditional-deletes-2025-09)
  say: September sixteenth, twenty twenty-five | conditional deletes
s3-change-conditional-writes-2024-08
  claim: Since 2024-08-20 S3 supports conditional writes for PutObject and CompleteMultipartUpload: with the If-None-Match header the write fails if an object with the same key name already exists in the bucket, which prevents overwrites.
  scope: general purpose buckets, PutObject and CompleteMultipartUpload.
  link: [2024-08-20](../facts/s3.md#s3-change-conditional-writes-2024-08)
  link: [If-None-Match](../facts/s3.md#s3-change-conditional-writes-2024-08)
  say: August twentieth, twenty twenty-four | the If-None-Match header
s3-change-conditional-writes-if-match-and-keys-2024-11
  claim: On 2024-11-25 S3 added the If-Match header, which makes a write fail when the ETag you give does not match the object's ETag in S3, and the condition keys s3:if-match and s3:if-none-match, which let bucket policies force clients to use these headers.
  scope: general purpose buckets.
  link: [2024-11-25](../facts/s3.md#s3-change-conditional-writes-if-match-and-keys-2024-11)
  link: [s3:if-none-match](../facts/s3.md#s3-change-conditional-writes-if-match-and-keys-2024-11)
  say: November twenty-fifth, twenty twenty-four | the s3 if-match and if-none-match condition keys
s3-change-crc64nvme-default-checksum-2024-12
  claim: On 2024-12-01 S3 added the CRC-64NVME checksum algorithm and improved checksum integrity features. CRC64NVME is now the default checksum algorithm; for uploads, all AWS-owned clients calculate a checksum and send it with the request, and S3 calculates its own checksum and validates it before storing the object.
  scope: object uploads; default; another supported algorithm can be chosen.
  link: [2024-12-01](../facts/s3.md#s3-change-crc64nvme-default-checksum-2024-12)
  link: [CRC64NVME](../facts/s3.md#s3-change-crc64nvme-default-checksum-2024-12)
  say: December first, twenty twenty-four | C R C sixty-four N V M E
s3-change-default-encryption-sse-s3-2023-01
  claim: Since 2023-01-05 all new object uploads to Amazon S3 are automatically encrypted at no additional cost; SSE-S3 is applied to all new buckets and to any existing bucket that did not already have default encryption configured.
  scope: every new object upload, all buckets; default; existing buckets with SSE-S3 or SSE-KMS configured kept their setting.
  link: [2023-01-05](../facts/s3.md#s3-change-default-encryption-sse-s3-2023-01)
  link: [SSE-S3](../facts/s3.md#s3-change-default-encryption-sse-s3-2023-01)
  say: January fifth, twenty twenty-three | S3 managed keys, S S E S three
s3-change-dsse-kms-2023-06
  claim: On 2023-06-13 Amazon S3 added dual-layer server-side encryption with AWS KMS keys (DSSE-KMS), which applies two layers of encryption to objects when they are uploaded.
  scope: server-side encryption options.
  link: [2023-06-13](../facts/s3.md#s3-change-dsse-kms-2023-06)
  link: [two layers of encryption](../facts/s3.md#s3-change-dsse-kms-2023-06)
  say: June thirteenth, twenty twenty-three | two layers of encryption
s3-change-encryption-type-control-2025-11
  claim: On 2025-11-19 Amazon S3 added a bucket-level default encryption setting that enforces SSE-S3 or SSE-KMS for all write requests to a bucket; with the PutBucketEncryption API you can disable SSE-C on specific buckets.
  scope: per general purpose bucket.
  link: [2025-11-19](../facts/s3.md#s3-change-encryption-type-control-2025-11)
  link: [Using the PutBucketEncryption API](../facts/s3.md#s3-change-encryption-type-control-2025-11)
  say: November nineteenth, twenty twenty-five | with the PutBucketEncryption API
s3-change-event-notification-system-tags-2026-07
  claim: On 2026-07-16 S3 Event Notifications began to include system-generated tags in events delivered to all destinations, including Amazon EventBridge, Amazon SQS, Amazon SNS and AWS Lambda, so one EventBridge rule can filter events from thousands of buckets.
  scope: S3 Event Notifications, general purpose buckets; GA after 2026-07-15: not examinable yet.
  link: [2026-07-16](../facts/s3.md#s3-change-event-notification-system-tags-2026-07)
  link: [system-generated tags](../facts/s3.md#s3-change-event-notification-system-tags-2026-07)
  say: July sixteenth, twenty twenty-six | system-generated tags
s3-change-express-one-zone-launch-2023-11
  claim: On 2023-11-28 AWS launched S3 Express One Zone, a high-performance, single-zone S3 storage class built to deliver consistent, single-digit millisecond data access for the most latency-sensitive applications.
  scope: S3 Express One Zone storage class (directory buckets).
  link: [2023-11-28](../facts/s3.md#s3-change-express-one-zone-launch-2023-11)
  link: [single-digit millisecond data access](../facts/s3.md#s3-change-express-one-zone-launch-2023-11)
  say: November twenty-eighth, twenty twenty-three | single-digit millisecond access
s3-change-express-one-zone-price-cut-2025-04
  claim: On 2025-04-10 S3 Express One Zone reduced its prices for storage by 31%, PUT requests by 55% and GET requests by 85%, and cut its per-gigabyte data upload and retrieval charges by 60%.
  scope: S3 Express One Zone, all Regions where available.
  link: [2025-04-10](../facts/s3.md#s3-change-express-one-zone-price-cut-2025-04)
  link: [GET requests by 85%](../facts/s3.md#s3-change-express-one-zone-price-cut-2025-04)
  say: April tenth, twenty twenty-five | eighty-five percent on GET requests
s3-change-lifecycle-ia-no-30-day-minimum-2026-07
  claim: On 2026-07-16 Amazon S3 removed the 30-day minimum retention in S3 Standard before a Lifecycle transition to S3 Standard-IA or S3 One Zone-IA: Lifecycle rules can now transition objects to these classes as soon as 0 days after creation.
  scope: Lifecycle transitions from S3 Standard to S3 Standard-IA and S3 One Zone-IA; minimum; GA after 2026-07-15: not examinable yet.
  link: [2026-07-16](../facts/s3.md#s3-change-lifecycle-ia-no-30-day-minimum-2026-07)
  link: [as soon as 0 days after creation](../facts/s3.md#s3-change-lifecycle-ia-no-30-day-minimum-2026-07)
  link: [30-day minimum retention in S3 Standard](../facts/s3.md#s3-change-lifecycle-ia-no-30-day-minimum-2026-07)
  say: July sixteenth, twenty twenty-six | from day zero | thirty days in S3 Standard first
  changed: 2026-07-16: was 30-day minimum retention in S3 Standard
s3-change-lifecycle-pauses-failed-replication-2026-04
  claim: Since 2026-04-09 S3 Lifecycle no longer expires or transitions objects that have failed replication, even if they match a lifecycle rule. When both Replication and Lifecycle are enabled, Lifecycle blocks expiration and transition actions on objects with PENDING or FAILED replication status, and FAILED objects keep incurring storage costs until the replication issue is resolved.
  scope: buckets with both S3 Replication and S3 Lifecycle; applies automatically to existing and new configurations.
  link: [2026-04-09](../facts/s3.md#s3-change-lifecycle-pauses-failed-replication-2026-04)
  link: [S3 Lifecycle blocks expiration and transition actions](../facts/s3.md#s3-change-lifecycle-pauses-failed-replication-2026-04)
  say: April ninth, twenty twenty-six | Lifecycle waits until the object replicates
s3-change-lifecycle-small-objects-128-kb-2024-09
  claim: On 2024-09-24 Amazon S3 began applying a default to Lifecycle configurations that prevents objects smaller than 128 KB from being transitioned to any storage class. To let smaller objects transition, you add an object size filter to the transition rule with a custom minimum size (ObjectSizeGreaterThan) or maximum size (ObjectSizeLessThan).
  scope: Lifecycle transition rules; default; override with an object size filter.
  link: [2024-09-24](../facts/s3.md#s3-change-lifecycle-small-objects-128-kb-2024-09)
  link: [smaller than 128 KB](../facts/s3.md#s3-change-lifecycle-small-objects-128-kb-2024-09)
  say: September twenty-fourth, twenty twenty-four | smaller than one hundred twenty-eight kilobytes
s3-change-max-object-size-50-tb-2025-12
  claim: On 2025-12-02 Amazon S3 raised the maximum size of an object from 5 TB to 50 TB. Objects that large must be uploaded with the Multipart Upload API, and because a single GET request is limited to 5 TB, they are downloaded with concurrent GetObject requests. The largest object that a single PUT can upload is still 5 GB.
  scope: per object; maximum; objects above 5 GB need multipart upload.
  link: [2025-12-02](../facts/s3.md#s3-change-max-object-size-50-tb-2025-12)
  link: [50 TB](../facts/s3.md#s3-change-max-object-size-50-tb-2025-12)
  link: [5 GB](../facts/s3.md#s3-change-max-object-size-50-tb-2025-12)
  say: December second, twenty twenty-five | fifty terabytes | five gigabytes
  changed: 2025-12-02: was 5 TB
s3-change-no-charge-unauthorized-requests-2024-08
  claim: Since 2024-08-19 S3 does not charge for unauthorized requests that the customer did not initiate: for AccessDenied (HTTP 403 Forbidden), S3 does not charge the bucket owner when the request comes from outside the bucket owner's AWS account or AWS organization.
  scope: AccessDenied (403) responses to requests from outside the account or organization; requests from inside the account or organization are still billed.
  link: [2024-08-19](../facts/s3.md#s3-change-no-charge-unauthorized-requests-2024-08)
  link: [S3 doesn't charge the bucket owner](../facts/s3.md#s3-change-no-charge-unauthorized-requests-2024-08)
  say: August nineteenth, twenty twenty-four | the bucket owner is not charged
s3-change-object-lambda-closed-2025-11
  claim: Since November 7, 2025 S3 Object Lambda is available only to existing customers that already use it and to select AWS Partner Network partners; new customers cannot sign up.
  scope: S3 Object Lambda; existing customers and select APN partners continue.
  link: [November 7, 2025](../facts/s3.md#s3-change-object-lambda-closed-2025-11)
  link: [no longer be open to new customers](../facts/s3.md#s3-change-object-lambda-closed-2025-11)
  say: November seventh, twenty twenty-five | closed to new customers
s3-change-object-lock-existing-buckets-2023-11
  claim: Since 2023-11-20 Object Lock can be enabled on an existing S3 bucket, not only at bucket creation. After Object Lock is enabled on a bucket, Object Lock cannot be disabled and versioning cannot be suspended for that bucket.
  scope: general purpose buckets; versioning must be enabled.
  link: [2023-11-20](../facts/s3.md#s3-change-object-lock-existing-buckets-2023-11)
  link: [enable Object Lock on existing Amazon S3 bucket](../facts/s3.md#s3-change-object-lock-existing-buckets-2023-11)
  say: November twentieth, twenty twenty-three | Object Lock can be enabled on an existing bucket
s3-change-object-lock-variable-retention-2026-09
  claim: On 2026-09-08 S3 Object Lock added variable retention: you place an event hold with a retention duration on an object, S3 protects the object while the hold is on, and when you release the hold S3 keeps the object for the duration you specified.
  scope: Object Lock retention on object versions; GA after 2026-07-15: not examinable yet.
  link: [2026-09-08](../facts/s3.md#s3-change-object-lock-variable-retention-2026-09)
  link: [variable retention](../facts/s3.md#s3-change-object-lock-variable-retention-2026-09)
  say: September eighth, twenty twenty-six | variable retention with event holds
s3-change-rcp-for-s3-2024-11
  claim: Since 2024-11-13 resource control policies (RCPs) in AWS Organizations can set the maximum available permissions on S3 buckets across the whole organization. An RCP grants no permissions by itself; it limits what identity-based and resource-based policies can allow.
  scope: per organization with all features enabled.
  link: [2024-11-13](../facts/s3.md#s3-change-rcp-for-s3-2024-11)
  link: [maximum available permissions](../facts/s3.md#s3-change-rcp-for-s3-2024-11)
  say: November thirteenth, twenty twenty-four | the maximum available permissions
s3-change-restore-request-rate-1000-tps-2022-11
  claim: Since 2022-11-15 Amazon S3 supports restore requests at up to 1,000 transactions per second, per AWS account, for the S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive storage classes.
  scope: per AWS account, restore requests; maximum.
  link: [2022-11-15](../facts/s3.md#s3-change-restore-request-rate-1000-tps-2022-11)
  link: [1,000 transactions per second](../facts/s3.md#s3-change-restore-request-rate-1000-tps-2022-11)
  say: November fifteenth, twenty twenty-two | one thousand transactions per second
s3-change-s3-files-launch-2026-04
  claim: On 2026-04-07 AWS launched Amazon S3 Files, a shared file system that connects any AWS compute resource directly with data in Amazon S3; S3 file systems can be mounted on Amazon EC2, AWS Lambda, Amazon EKS and Amazon ECS.
  scope: S3 general purpose buckets.
  link: [2026-04-07](../facts/s3.md#s3-change-s3-files-launch-2026-04)
  link: [shared file system](../facts/s3.md#s3-change-s3-files-launch-2026-04)
  say: April seventh, twenty twenty-six | a shared file system on top of S3
s3-change-select-closed-to-new-customers-2024-07
  claim: Since 2024-07-25 Amazon S3 Select is no longer available to new customers, and Amazon S3 Glacier Select is listed among services in maintenance with the same date; existing customers can continue to use S3 Select as usual.
  scope: S3 Select and S3 Glacier Select; existing customers continue.
  link: [2024-07-25](../facts/s3.md#s3-change-select-closed-to-new-customers-2024-07)
  link: [no longer available to new customers](../facts/s3.md#s3-change-select-closed-to-new-customers-2024-07)
  say: July twenty-fifth, twenty twenty-four | closed to new customers
s3-change-sse-c-disabled-default-2026-04
  claim: In April 2026 Amazon S3 deployed a default that disables SSE-C for new write requests on all new general purpose buckets, and on existing buckets in accounts that had no SSE-C encrypted objects. Applications that need SSE-C must enable it with the PutBucketEncryption API after creating the bucket. New buckets in Middle East (Bahrain) and Middle East (UAE) are excepted.
  scope: general purpose buckets; default; existing buckets in accounts with SSE-C objects were not changed; Middle East (Bahrain) and Middle East (UAE) excepted.
  link: [April 2026](../facts/s3.md#s3-change-sse-c-disabled-default-2026-04)
  link: [SSE-C encryption disabled for all new write requests](../facts/s3.md#s3-change-sse-c-disabled-default-2026-04)
  say: April twenty twenty-six | SSE-C is off for new writes
s3-change-update-object-encryption-2026-01
  claim: On 2026-01-29 Amazon S3 added the UpdateObjectEncryption API, which changes the server-side encryption type of encrypted objects without any data movement, for example from SSE-S3 to SSE-KMS; with S3 Batch Operations it can standardize the encryption type of entire buckets while keeping object properties and Lifecycle eligibility.
  scope: encrypted objects in general purpose buckets; objects must already be encrypted.
  link: [2026-01-29](../facts/s3.md#s3-change-update-object-encryption-2026-01)
  link: [without any data movement](../facts/s3.md#s3-change-update-object-encryption-2026-01)
  say: January twenty-ninth, twenty twenty-six | without moving the data
s3-class-deep-archive-compare-row
  claim: S3 Glacier Deep Archive has a 180 days minimum storage duration, a recommended access frequency of annually, average retrieval times of 9 to 48 hours, and it is an archival class.
  scope: S3 Glacier Deep Archive.
  link: [180 days](../facts/s3.md#s3-class-deep-archive-compare-row)
  link: [Annually](../facts/s3.md#s3-class-deep-archive-compare-row)
  link: [9 to 48 hours](../facts/s3.md#s3-class-deep-archive-compare-row)
  say: one hundred eighty days | annually | nine to forty-eight hours
s3-class-deep-archive-lowest-cost-twelve-hours
  claim: S3 Glacier Deep Archive is the lowest cost storage in the cloud, for long-lived archives such as compliance archives, with data retrieval within twelve hours.
  scope: S3 Glacier Deep Archive.
  link: [S3 Glacier Deep Archive](../facts/s3.md#s3-class-deep-archive-lowest-cost-twelve-hours)
  link: [the lowest cost storage in the cloud](../facts/s3.md#s3-class-deep-archive-lowest-cost-twelve-hours)
  link: [data retrieval within twelve hours](../facts/s3.md#s3-class-deep-archive-lowest-cost-twelve-hours)
s3-class-deep-archive-profile
  claim: S3 Glacier Deep Archive is for long-lived archive data accessed less than once a year with retrieval times of hours, designed for 99.999999999% durability and 99.99% availability (after you restore objects) across >= 3 Availability Zones, with a 180 days minimum storage duration and per-GB retrieval fees; objects must be restored before access.
  scope: S3 Glacier Deep Archive storage class.
  link: [99.99% (after you restore objects)](../facts/s3.md#s3-class-deep-archive-profile)
  link: [180 days](../facts/s3.md#s3-class-deep-archive-profile)
  link: [less than once a year](../facts/s3.md#s3-class-deep-archive-profile)
  say: ninety-nine point nine nine percent after restore | one hundred eighty days | less than once a year
s3-class-deep-archive-retrieval-12-48-hours
  claim: S3 Glacier Deep Archive has two retrieval options that range from 12-48 hours.
  scope: S3 Glacier Deep Archive.
  link: [12-48 hours](../facts/s3.md#s3-class-deep-archive-retrieval-12-48-hours)
  link: [two retrieval options](../facts/s3.md#s3-class-deep-archive-retrieval-12-48-hours)
  say: twelve to forty-eight hours
s3-class-express-one-zone-profile
  claim: S3 Express One Zone gives single-digit millisecond data access within a single Availability Zone that you choose, designed for 99.999999999% durability and 99.95% availability in 1 Availability Zone, with no minimum storage duration and no minimum billable object size.
  scope: S3 Express One Zone storage class.
  link: [99.95%](../facts/s3.md#s3-class-express-one-zone-profile)
  link: [1 Availability Zone](../facts/s3.md#s3-class-express-one-zone-profile)
  say: ninety-nine point nine five percent | one Availability Zone
s3-class-flexible-retrieval-free-bulk-5-12-hours
  claim: S3 Glacier Flexible Retrieval is for archive data that does not need immediate access but needs retrieval of large data sets at no cost (backup, disaster recovery): retrieval in minutes, or free bulk retrievals in 5-12 hours.
  scope: S3 Glacier Flexible Retrieval; bulk retrieval option.
  link: [S3 Glacier Flexible Retrieval](../facts/s3.md#s3-class-flexible-retrieval-free-bulk-5-12-hours)
  link: [free bulk retrievals in 5-12 hours](../facts/s3.md#s3-class-flexible-retrieval-free-bulk-5-12-hours)
  say: free bulk retrievals in five to twelve hours
s3-class-flexible-retrieval-not-real-time
  claim: S3 Glacier Flexible Retrieval is for archives where portions of the data might need to be retrieved in minutes; data in this storage class is archived and not available for real-time access.
  scope: S3 Glacier Flexible Retrieval (GLACIER).
  link: [not available for real-time access](../facts/s3.md#s3-class-flexible-retrieval-not-real-time)
  link: [retrieved in minutes](../facts/s3.md#s3-class-flexible-retrieval-not-real-time)
s3-class-flexible-retrieval-three-options
  claim: S3 Glacier Flexible Retrieval has three retrieval options: expedited typically in 1–5 minutes, standard typically in 3–5 hours, and free bulk typically in 5–12 hours.
  scope: S3 Glacier Flexible Retrieval; typical completion times.
  link: [1–5 minutes](../facts/s3.md#s3-class-flexible-retrieval-three-options)
  link: [3–5 hours](../facts/s3.md#s3-class-flexible-retrieval-three-options)
  link: [5–12 hours](../facts/s3.md#s3-class-flexible-retrieval-three-options)
  say: one to five minutes | three to five hours | five to twelve hours
s3-class-glacier-family-same-durability
  claim: Each of the three S3 Glacier storage classes offers the same durability and resiliency as S3 Standard, at lower storage costs.
  scope: S3 Glacier Instant Retrieval, Flexible Retrieval and Deep Archive.
  link: [same durability and resiliency](../facts/s3.md#s3-class-glacier-family-same-durability)
  say: same durability and resiliency
s3-class-glacier-flexible-access-1-2-per-year
  claim: AWS recommends S3 Glacier Flexible Retrieval for archive data that is accessed 1 to 2 times a year and does not need immediate access; it offers free bulk retrievals and suits backup and disaster recovery.
  scope: S3 Glacier Flexible Retrieval.
  link: [one to two times a year](../facts/s3.md#s3-class-glacier-flexible-access-1-2-per-year)
  link: [free bulk retrievals](../facts/s3.md#s3-class-glacier-flexible-access-1-2-per-year)
  say: one to two times a year | free bulk retrievals
s3-class-glacier-flexible-compare-row
  claim: S3 Glacier Flexible Retrieval has a 90 days minimum storage duration, a recommended access frequency of semi-annually, average retrieval times of minutes to 12 hours, and it is an archival class.
  scope: S3 Glacier Flexible Retrieval.
  link: [90 days](../facts/s3.md#s3-class-glacier-flexible-compare-row)
  link: [Semi-annually](../facts/s3.md#s3-class-glacier-flexible-compare-row)
  link: [Minutes to 12 hours](../facts/s3.md#s3-class-glacier-flexible-compare-row)
  say: ninety days | semi-annually | minutes to twelve hours
s3-class-glacier-flexible-profile
  claim: S3 Glacier Flexible Retrieval is for long-lived archive data accessed once a year with retrieval times of minutes to hours, designed for 99.999999999% durability and 99.99% availability (after you restore objects) across >= 3 Availability Zones, with a 90 days minimum storage duration and per-GB retrieval fees; objects must be restored before access.
  scope: S3 Glacier Flexible Retrieval storage class.
  link: [99.99% (after you restore objects)](../facts/s3.md#s3-class-glacier-flexible-profile)
  link: [90 days](../facts/s3.md#s3-class-glacier-flexible-profile)
  link: [once a year](../facts/s3.md#s3-class-glacier-flexible-profile)
  link: [minutes to hours](../facts/s3.md#s3-class-glacier-flexible-profile)
  say: ninety-nine point nine nine percent after restore | ninety days | once a year | minutes to hours
s3-class-glacier-ir-compare-row
  claim: S3 Glacier Instant Retrieval has a 90 days minimum storage duration, a recommended access frequency of quarterly, average retrieval times of milliseconds, and it is not an archival class.
  scope: S3 Glacier Instant Retrieval.
  link: [90 days](../facts/s3.md#s3-class-glacier-ir-compare-row)
  link: [Quarterly](../facts/s3.md#s3-class-glacier-ir-compare-row)
  link: [Milliseconds](../facts/s3.md#s3-class-glacier-ir-compare-row)
  say: ninety days | quarterly | milliseconds
s3-class-glacier-ir-lowest-cost-milliseconds
  claim: For archive data that needs immediate access, S3 Glacier Instant Retrieval is the archive class that gives the lowest cost storage with milliseconds retrieval.
  scope: S3 Glacier storage classes; archive data that needs immediate access.
  link: [S3 Glacier Instant Retrieval](../facts/s3.md#s3-class-glacier-ir-lowest-cost-milliseconds)
  link: [milliseconds retrieval](../facts/s3.md#s3-class-glacier-ir-lowest-cost-milliseconds)
s3-class-glacier-ir-min-size-and-duration
  claim: S3 Glacier Instant Retrieval has a minimum object size of 128 KB and a minimum storage duration of 90 days.
  scope: per object, S3 Glacier Instant Retrieval; minimum.
  link: [128 KB](../facts/s3.md#s3-class-glacier-ir-min-size-and-duration)
  link: [90 days](../facts/s3.md#s3-class-glacier-ir-min-size-and-duration)
  say: one hundred twenty-eight kilobytes | ninety days
s3-class-glacier-ir-profile
  claim: S3 Glacier Instant Retrieval is for long-lived archive data accessed once a quarter with millisecond access, designed for 99.999999999% durability and 99.9% availability across >= 3 Availability Zones, with a 90 days minimum storage duration, a 128 KB minimum billable object size and per-GB retrieval fees.
  scope: S3 Glacier Instant Retrieval storage class.
  link: [99.9%](../facts/s3.md#s3-class-glacier-ir-profile)
  link: [90 days](../facts/s3.md#s3-class-glacier-ir-profile)
  link: [128 KB](../facts/s3.md#s3-class-glacier-ir-profile)
  link: [once a quarter](../facts/s3.md#s3-class-glacier-ir-profile)
  say: ninety-nine point nine percent | ninety days | one hundred twenty-eight kilobytes | once a quarter
s3-class-glacier-ir-real-time-access
  claim: S3 Glacier Instant Retrieval is for long-term data that is rarely accessed and requires milliseconds retrieval; data in this storage class is available for real-time access.
  scope: S3 Glacier Instant Retrieval (GLACIER_IR).
  link: [available for real-time access](../facts/s3.md#s3-class-glacier-ir-real-time-access)
  link: [milliseconds retrieval](../facts/s3.md#s3-class-glacier-ir-real-time-access)
s3-class-glacier-ir-vs-standard-ia
  claim: S3 Glacier Instant Retrieval gives real-time access with the same latency and throughput as S3 Standard-IA; compared with S3 Standard-IA it has lower storage costs but higher data access costs.
  scope: S3 Glacier Instant Retrieval versus S3 Standard-IA.
  link: [same latency and throughput performance](../facts/s3.md#s3-class-glacier-ir-vs-standard-ia)
  link: [lower storage costs but higher data access costs](../facts/s3.md#s3-class-glacier-ir-vs-standard-ia)
  say: same latency and throughput performance | lower storage costs but higher data access costs
s3-class-int-tiering-profile
  claim: S3 Intelligent-Tiering is for data with unknown, changing or unpredictable access patterns, designed for 99.999999999% durability and 99.9% availability across >= 3 Availability Zones, with no minimum storage duration, no minimum billable object size, no retrieval fees and a per-object monitoring and automation fee; objects less than 128KB are not monitored and always stay in the Frequent Access tier.
  scope: S3 Intelligent-Tiering storage class.
  link: [99.9%](../facts/s3.md#s3-class-int-tiering-profile)
  link: [less than 128KB](../facts/s3.md#s3-class-int-tiering-profile)
  say: ninety-nine point nine percent | less than one twenty-eight kilobytes
s3-class-one-zone-ia-profile
  claim: S3 One Zone-IA is for recreatable, infrequently accessed data (once a month) with millisecond access, designed for 99.999999999% durability and 99.5% availability in 1 Availability Zone, with a 30 days minimum storage duration, a 128 KB minimum billable object size and per-GB retrieval fees; it is not resilient to the loss of the Availability Zone.
  scope: S3 One Zone-IA storage class.
  link: [99.5%](../facts/s3.md#s3-class-one-zone-ia-profile)
  link: [1 Availability Zone](../facts/s3.md#s3-class-one-zone-ia-profile)
  link: [30 days](../facts/s3.md#s3-class-one-zone-ia-profile)
  say: ninety-nine point five percent | one Availability Zone | thirty days
s3-class-standard-ia-profile
  claim: S3 Standard-IA is for long-lived, infrequently accessed data (once a month) with millisecond access, designed for 99.999999999% durability and 99.9% availability across >= 3 Availability Zones, with a 30 days minimum storage duration, a 128 KB minimum billable object size and per-GB retrieval fees.
  scope: S3 Standard-IA storage class.
  link: [99.9%](../facts/s3.md#s3-class-standard-ia-profile)
  link: [30 days](../facts/s3.md#s3-class-standard-ia-profile)
  link: [128 KB](../facts/s3.md#s3-class-standard-ia-profile)
  link: [once a month](../facts/s3.md#s3-class-standard-ia-profile)
  say: ninety-nine point nine percent | thirty days | one hundred twenty-eight kilobytes | once a month
s3-class-standard-profile
  claim: S3 Standard is for frequently accessed data (more than once a month) with millisecond access, designed for 99.999999999% durability and 99.99% availability across >= 3 Availability Zones, with no minimum storage duration and no minimum billable object size.
  scope: S3 Standard storage class.
  link: [99.999999999%](../facts/s3.md#s3-class-standard-profile)
  link: [99.99%](../facts/s3.md#s3-class-standard-profile)
  link: [more than once a month](../facts/s3.md#s3-class-standard-profile)
  say: eleven nines | ninety-nine point nine nine percent | more than once a month
s3-client-side-encryption-not-exposed-to-aws
  claim: With client-side encryption the objects are encrypted before they are sent, are not exposed to any third party including AWS, and S3 plays no role in encrypting or decrypting them.
  scope: client-side encryption.
  link: [aren't exposed to any third party, including AWS](../facts/s3.md#s3-client-side-encryption-not-exposed-to-aws)
  link: [does not play a role in encrypting](../facts/s3.md#s3-client-side-encryption-not-exposed-to-aws)
s3-client-side-encryption-you-manage-keys
  claim: With client-side encryption you encrypt data client-side and upload the encrypted data to S3; you manage the encryption process, the encryption keys and related tools.
  scope: client-side encryption.
  link: [you manage the encryption process, the encryption keys](../facts/s3.md#s3-client-side-encryption-you-manage-keys)
s3-cloudfront-oai-bucket-policy
  claim: A bucket policy can grant a CloudFront origin access identity (OAI) permission to get (read) all objects in the bucket, so that users can access the objects through CloudFront but not directly through Amazon S3.
  scope: per bucket policy.
  link: [through CloudFront but not directly through Amazon S3](../facts/s3.md#s3-cloudfront-oai-bucket-policy)
  link: [origin access identity (OAI)](../facts/s3.md#s3-cloudfront-oai-bucket-policy)
s3-cloudwatch-alarm-on-policy-changes
  claim: A CloudWatch alarm can be set to trigger when an S3 API call puts or deletes a bucket policy, a bucket lifecycle or a bucket replication configuration, or puts a bucket ACL.
  scope: CloudTrail events sent to CloudWatch.
  link: [PUT or DELETE a bucket policy](../facts/s3.md#s3-cloudwatch-alarm-on-policy-changes)
s3-concurrent-writers-latest-timestamp-wins
  claim: Amazon S3 does not support object locking for concurrent writers: if two PUT requests are made to the same key at the same time, the request with the latest timestamp wins.
  scope: PUT requests to one key; without conditional write headers.
  link: [the request with the latest timestamp wins](../facts/s3.md#s3-concurrent-writers-latest-timestamp-wins)
  say: the latest timestamp wins
s3-conditional-writes-enforce-bucket-policy
  claim: A bucket policy can enforce conditional writes for object uploads in general purpose buckets by using the condition keys s3:if-match or s3:if-none-match.
  scope: general purpose buckets; multipart uploads must exempt CreateMultipartUpload, UploadPart and UploadPartCopy.
  link: [condition keys `s3:if-match` or `s3:if-none-match`](../facts/s3.md#s3-conditional-writes-enforce-bucket-policy)
  say: the if-match or if-none-match condition keys
s3-console-upload-max
  claim: The S3 console can upload a file of up to 160 GB; a larger file needs the AWS CLI, an SDK or the REST API.
  scope: per file uploaded in the S3 console; maximum; not adjustable.
  link: [160 GB](../facts/s3.md#s3-console-upload-max)
  say: one hundred sixty gigabytes
s3-cors-purpose
  claim: Cross-origin resource sharing (CORS) defines a way for client web applications that are loaded in one domain to interact with resources in a different domain. For example, when JavaScript on a website hosted at the S3 website endpoint makes authenticated GET and PUT requests to the same bucket through its S3 API endpoint, a browser would normally block JavaScript from allowing those requests; a CORS configuration on the bucket can explicitly enable cross-origin requests from the website endpoint.
  scope: per bucket.
  link: [interact with resources in a different domain](../facts/s3.md#s3-cors-purpose)
  link: [block JavaScript from allowing those requests](../facts/s3.md#s3-cors-purpose)
  link: [explicitly enable cross-origin requests](../facts/s3.md#s3-cors-purpose)
s3-cors-rule-match-origin-method-headers
  claim: In a CORS request to a bucket, the Origin header must match AllowedOrigins, the requested method must match AllowedMethods, and the headers of a preflight request must match AllowedHeaders.
  scope: per bucket CORS configuration.
  link: [AllowedOrigins](../facts/s3.md#s3-cors-rule-match-origin-method-headers)
  link: [AllowedMethods](../facts/s3.md#s3-cors-rule-match-origin-method-headers)
  link: [AllowedHeaders](../facts/s3.md#s3-cors-rule-match-origin-method-headers)
s3-cors-rule-matching
  claim: On a browser preflight request, S3 uses the first CORSRule that matches the request's Origin, method and headers against AllowedOrigins, AllowedMethods and AllowedHeaders. ACLs and policies still apply when CORS is enabled.
  scope: per bucket CORS configuration.
  link: [the first CORSRule rule that matches](../facts/s3.md#s3-cors-rule-matching)
  link: [The ACLs and policies continue to apply](../facts/s3.md#s3-cors-rule-matching)
s3-crr-compute-clusters-two-regions
  claim: If compute clusters in two different AWS Regions analyze the same set of objects, Cross-Region Replication can keep object copies in both Regions for operational efficiency.
  scope: S3 Cross-Region Replication.
  link: [Increase operational efficiency](../facts/s3.md#s3-crr-compute-clusters-two-regions)
s3-crr-for-compliance-distance-requirements
  claim: S3 already stores data across several geographically separate Availability Zones; when compliance requires copies at a greater distance, Cross-Region Replication copies objects automatically and asynchronously to a bucket in a distant Region.
  scope: per replication rule.
  link: [store data at even greater distances](../facts/s3.md#s3-crr-for-compliance-distance-requirements)
  link: [automatic, asynchronous copying of objects](../facts/s3.md#s3-crr-for-compliance-distance-requirements)
s3-crr-minimize-latency-copies-near-users
  claim: When customers are in two geographic locations, Cross-Region Replication can minimize latency by keeping object copies in AWS Regions that are geographically closer to the users.
  scope: S3 Cross-Region Replication; customers in two geographic locations.
  link: [minimize latency in accessing objects](../facts/s3.md#s3-crr-minimize-latency-copies-near-users)
s3-crr-requires-versioning-source-and-destination
  claim: Cross-Region Replication requires versioning to be enabled on both the source bucket and the destination bucket.
  scope: source and destination buckets of a replication rule.
  link: [S3 buckets to have versioning enabled](../facts/s3.md#s3-crr-requires-versioning-source-and-destination)
s3-data-protection-mechanisms
  claim: Versioning preserves, retrieves and restores every version of every object so you can recover from unintended user actions and application failures; by default a request returns the most recently written version. Object Lock and S3 Replication are the other data protection features named beside versioning.
  scope: per bucket; default.
  link: [every version of every object](../facts/s3.md#s3-data-protection-mechanisms)
  link: [requests retrieve the most recently written version](../facts/s3.md#s3-data-protection-mechanisms)
  link: [Amazon S3 Object Lock and S3 Replication](../facts/s3.md#s3-data-protection-mechanisms)
  link: [recover from both unintended user actions](../facts/s3.md#s3-data-protection-mechanisms)
s3-deep-archive-lowest-cost-72-hours
  claim: S3 Glacier Deep Archive is the lowest-cost storage option in AWS; it is meant for data kept for multiple years for compliance, for backup or disaster recovery, or for infrequently accessed data that can wait up to 72 hours to be retrieved.
  scope: S3 Glacier Deep Archive; maximum; data accessed less than once a year.
  link: [lowest-cost storage option in AWS](../facts/s3.md#s3-deep-archive-lowest-cost-72-hours)
  link: [up to 72 hours](../facts/s3.md#s3-deep-archive-lowest-cost-72-hours)
  say: lowest-cost storage option in AWS | up to seventy-two hours
s3-default-encryption-cannot-disable
  claim: SSE-S3 is the base level of encryption for every new object uploaded to a bucket, and you can no longer disable encryption for new object uploads.
  scope: new object uploads, every bucket.
  link: [no longer disable encryption](../facts/s3.md#s3-default-encryption-cannot-disable)
  say: you can no longer disable encryption
s3-default-encryption-change-not-retroactive
  claim: Changing a bucket's default encryption to SSE-KMS does not change the encryption of objects already in the bucket. To re-encrypt existing objects, use S3 Batch Operations with the Copy action to write them back to the same bucket.
  scope: per bucket.
  link: [in the bucket is not changed](../facts/s3.md#s3-default-encryption-change-not-retroactive)
  link: [you can use Amazon S3 Batch Operations](../facts/s3.md#s3-default-encryption-change-not-retroactive)
s3-default-encryption-existing-objects-not-encrypted
  claim: Automatic encryption applies only to new uploads: objects already stored unencrypted in an existing bucket are not encrypted automatically, and to encrypt them you can use S3 Batch Operations to create encrypted copies.
  scope: objects stored before default encryption applied.
  link: [won't be automatically encrypted](../facts/s3.md#s3-default-encryption-existing-objects-not-encrypted)
  link: [S3 Batch Operations to create encrypted copies](../facts/s3.md#s3-default-encryption-existing-objects-not-encrypted)
  say: existing objects are not encrypted automatically | Batch Operations copies
s3-default-encryption-sse-s3-override-per-request-or-bucket
  claim: Server-side encryption with Amazon S3 managed keys (SSE-S3) is the default encryption configuration for every S3 bucket. To use a different type of encryption, you can either specify the type of server-side encryption to use in your S3 PUT requests or set the default encryption configuration in the destination bucket.
  scope: per bucket (default) and per object (PUT request); default; adjustable.
  link: [the default encryption configuration for every bucket](../facts/s3.md#s3-default-encryption-sse-s3-override-per-request-or-bucket)
  link: [specify the type of server-side encryption to use](../facts/s3.md#s3-default-encryption-sse-s3-override-per-request-or-bucket)
s3-delete-marker-soft-delete
  claim: In a versioned bucket, deleting the current version without a version ID does not permanently delete the object; S3 adds a delete marker, which becomes the current version with a new version ID.
  scope: per versioning-enabled bucket; the delete request names no version ID.
  link: [issuing a soft delete of the object](../facts/s3.md#s3-delete-marker-soft-delete)
  link: [Amazon S3 doesn't permanently delete the object](../facts/s3.md#s3-delete-marker-soft-delete)
  link: [becomes the current (or newest) version](../facts/s3.md#s3-delete-marker-soft-delete)
s3-delete-specific-version-needs-version-id
  claim: In an unversioned bucket you delete by key only; in a versioning-enabled bucket you can give the version ID to delete one specific version of the object.
  scope: per bucket.
  link: [provide the version ID of the object](../facts/s3.md#s3-delete-specific-version-needs-version-id)
  link: [you provide only the object key name](../facts/s3.md#s3-delete-specific-version-needs-version-id)
s3-directory-bucket-access-settings-fixed
  claim: Directory buckets have all Block Public Access settings on, Object Ownership set to bucket owner enforced and ACLs disabled, and these settings cannot be modified. Users have no permissions on directory buckets by default; access is granted with IAM identities or access points.
  scope: directory buckets; fixed.
  link: [these settings can't be modified](../facts/s3.md#s3-directory-bucket-access-settings-fixed)
  link: [users don't have permissions for directory buckets](../facts/s3.md#s3-directory-bucket-access-settings-fixed)
s3-directory-bucket-hierarchical
  claim: Directory buckets organize data hierarchically into directories, unlike the flat structure of general purpose buckets; they have no prefix limits and individual directories scale horizontally.
  scope: directory buckets.
  link: [organize data hierarchically into directories](../facts/s3.md#s3-directory-bucket-hierarchical)
  link: [there aren't prefix limits for directory buckets](../facts/s3.md#s3-directory-bucket-hierarchical)
s3-directory-bucket-inactive-after-90-days
  claim: A directory bucket in an Availability Zone with no request activity for at least 90 days becomes inactive and is temporarily unreadable and unwritable; it keeps all data and metadata, storage charges continue, and an access request reactivates it, typically within a few minutes, with HTTP 503 errors during the transition.
  scope: directory buckets in Availability Zones; no request activity for at least 90 days; does not apply to Local Zone buckets.
  link: [transition to an inactive state](../facts/s3.md#s3-directory-bucket-inactive-after-90-days)
  link: [retain all storage, object metadata, and bucket metadata](../facts/s3.md#s3-directory-bucket-inactive-after-90-days)
  link: [reads and writes return an HTTP 503 (Service Unavailable) error code](../facts/s3.md#s3-directory-bucket-inactive-after-90-days)
s3-directory-bucket-local-zone-residency
  claim: For data residency, a directory bucket can be created in a single AWS Dedicated Local Zone to keep data inside a specific data perimeter; directory buckets in Local Zones support the S3 One Zone-IA storage class, and Local Zones are supported only for directory buckets.
  scope: directory buckets in Local Zones.
  link: [a single AWS Dedicated Local Zone (DLZ)](../facts/s3.md#s3-directory-bucket-local-zone-residency)
  link: [only supported for directory buckets](../facts/s3.md#s3-directory-bucket-local-zone-residency)
s3-directory-bucket-public-access-disabled
  claim: Directory buckets have all public access disabled by default and this cannot be changed; you can grant access only to the directory bucket itself, not to individual objects in it.
  scope: directory buckets; fixed.
  link: [all public access disabled by default](../facts/s3.md#s3-directory-bucket-public-access-disabled)
  link: [this behavior can't be changed](../facts/s3.md#s3-directory-bucket-public-access-disabled)
  link: [grant access only to your directory buckets](../facts/s3.md#s3-directory-bucket-public-access-disabled)
s3-directory-bucket-quota
  claim: An AWS account can create up to 100 directory buckets per Region, with no limit on the number of objects in a bucket; contact Support to raise the quota.
  scope: per AWS account, per Region; default; adjustable.
  link: [100 directory buckets](../facts/s3.md#s3-directory-bucket-quota)
  say: one hundred directory buckets
s3-directory-bucket-read-tps-quota
  claim: Each directory bucket supports up to 200,000 read TPS (GET/HEAD requests per second) by default; to raise it you contact Support.
  scope: per directory bucket; default; adjustable; increase through AWS Support.
  link: [200,000 read TPS](../facts/s3.md#s3-directory-bucket-read-tps-quota)
  say: two hundred thousand reads per second
s3-directory-bucket-single-az-express
  claim: A directory bucket for low-latency use is created in a single Availability Zone and supports the S3 Express One Zone storage class; data is stored redundantly on multiple devices within that one Availability Zone, and the class is recommended for performance-sensitive applications that benefit from single-digit millisecond PUT and GET latencies.
  scope: directory buckets in Availability Zones.
  link: [a single AWS Availability Zone](../facts/s3.md#s3-directory-bucket-single-az-express)
  link: [redundantly stored on multiple devices](../facts/s3.md#s3-directory-bucket-single-az-express)
  link: [single-digit millisecond PUT and GET latencies](../facts/s3.md#s3-directory-bucket-single-az-express)
s3-directory-bucket-unsupported-features
  claim: Directory buckets do not support, among others, S3 Versioning, S3 Replication, S3 Object Lock, MFA delete, Requester Pays, S3 Event Notifications, Lifecycle transition actions, object tags, server access logs, static website hosting and Transfer Acceleration.
  scope: directory buckets.
  link: [not supported by directory buckets](../facts/s3.md#s3-directory-bucket-unsupported-features)
  link: [S3 Versioning](../facts/s3.md#s3-directory-bucket-unsupported-features)
  link: [S3 Replication](../facts/s3.md#s3-directory-bucket-unsupported-features)
  link: [S3 Object Lock](../facts/s3.md#s3-directory-bucket-unsupported-features)
s3-directory-bucket-write-tps-quota
  claim: Each directory bucket supports up to 100,000 write TPS (PUT/DELETE requests per second) by default; to raise it you contact Support.
  scope: per directory bucket; default; adjustable; increase through AWS Support.
  link: [100,000 write TPS](../facts/s3.md#s3-directory-bucket-write-tps-quota)
  say: one hundred thousand writes per second
s3-dsse-kms-two-layers
  claim: DSSE-KMS applies two layers of encryption to an object without the infrastructure that client-side encryption needs; each layer uses a different implementation of 256-bit AES-GCM, and KMS generates and manages the keys.
  scope: per object encrypted with DSSE-KMS.
  link: [two layers of encryption to your data](../facts/s3.md#s3-dsse-kms-two-layers)
  link: [256-bit Advanced Encryption Standard with Galois Counter Mode (AES-GCM)](../facts/s3.md#s3-dsse-kms-two-layers)
s3-durability-availability-design
  claim: S3 Standard storage is designed for 99.999999999% durability and 99.99% availability of objects over a given year, and the multi-zone classes store objects on multiple devices across a minimum of three Availability Zones in a Region.
  scope: S3 Standard objects, per year; designed-for figures, not the SLA.
  link: [99.999999999%](../facts/s3.md#s3-durability-availability-design)
  link: [99.99%](../facts/s3.md#s3-durability-availability-design)
  link: [minimum of three Availability Zones](../facts/s3.md#s3-durability-availability-design)
  say: eleven nines | ninety-nine point nine nine percent | at least three Availability Zones
s3-durability-three-az-design
  claim: S3 Standard, Intelligent-Tiering, Standard-IA, Glacier Instant Retrieval, Glacier Flexible Retrieval and Glacier Deep Archive store objects redundantly on multiple devices across at least three Availability Zones in a Region; S3 One Zone-IA stores data redundantly within a single Availability Zone.
  scope: per storage class; minimum.
  link: [a minimum of three Availability Zones](../facts/s3.md#s3-durability-three-az-design)
  link: [within a single Availability Zone](../facts/s3.md#s3-durability-three-az-design)
  link: [loss of an entire Amazon S3 Availability Zone](../facts/s3.md#s3-durability-three-az-design)
s3-encryption-in-transit-https-tls
  claim: HTTPS (TLS) protects S3 traffic from eavesdropping and person-in-the-middle manipulation; AWS recommends allowing only encrypted HTTPS connections through a bucket policy condition.
  scope: per bucket; bucket policy with the aws:SecureTransport condition.
  link: [allowing only encrypted connections over HTTPS (TLS)](../facts/s3.md#s3-encryption-in-transit-https-tls)
  link: [eavesdropping on or manipulating network traffic](../facts/s3.md#s3-encryption-in-transit-https-tls)
s3-encryption-in-transit-options
  claim: Data in transit to and from S3 is protected with SSL/TLS, including hybrid post-quantum key exchange, or with client-side encryption.
  scope: data in transit.
  link: [Secure Socket Layer/Transport Layer Security (SSL/TLS)](../facts/s3.md#s3-encryption-in-transit-options)
  link: [client-side encryption](../facts/s3.md#s3-encryption-in-transit-options)
s3-event-destinations-same-region
  claim: An SNS topic, SQS queue or Lambda function used as an S3 event notification destination must be in the same Region as the bucket.
  scope: per event notification destination (SNS topic, SQS queue, Lambda function).
  link: [same AWS Region as your Amazon S3 bucket](../facts/s3.md#s3-event-destinations-same-region)
  link: [same Region as your S3 bucket](../facts/s3.md#s3-event-destinations-same-region)
s3-event-notification-one-destination
  claim: Each event notification configuration can specify only one destination, and S3 sends one event entry per notification message.
  scope: per event notification configuration.
  link: [Only one destination can be specified](../facts/s3.md#s3-event-notification-one-destination)
  link: [one event entry for each notification message](../facts/s3.md#s3-event-notification-one-destination)
s3-event-notification-recursive-loop
  claim: A notification whose handler writes to the same bucket that triggers it can cause an execution loop; AWS advises using two buckets or limiting the trigger to a prefix for incoming objects.
  scope: per bucket with event notifications.
  link: [could cause an execution loop](../facts/s3.md#s3-event-notification-recursive-loop)
  link: [use two buckets](../facts/s3.md#s3-event-notification-recursive-loop)
s3-event-notifications-at-least-once-seconds
  claim: S3 event notifications are designed to be delivered at least once; they typically arrive in seconds but can sometimes take a minute or longer.
  scope: S3 Event Notifications.
  link: [delivered at least once](../facts/s3.md#s3-event-notifications-at-least-once-seconds)
  link: [delivered in seconds](../facts/s3.md#s3-event-notifications-at-least-once-seconds)
s3-event-notifications-max
  claim: A bucket can have at most 100 event notification configurations.
  scope: per bucket; maximum; not adjustable.
  link: [100](../facts/s3.md#s3-event-notifications-max)
  say: one hundred
s3-event-notifications-no-fifo-destinations
  claim: SQS FIFO queues and SNS FIFO topics are not supported as S3 event notification destinations; to deliver S3 events to an SQS FIFO queue, use Amazon EventBridge.
  scope: S3 event notification destinations.
  link: [FIFO (First-In-First-Out) queues aren't supported](../facts/s3.md#s3-event-notifications-no-fifo-destinations)
  link: [you can use Amazon EventBridge](../facts/s3.md#s3-event-notifications-no-fifo-destinations)
  link: [SNS FIFO is not allowed](../facts/s3.md#s3-event-notifications-no-fifo-destinations)
s3-event-notifications-no-order-duplicates
  claim: S3 Event Notifications are not guaranteed to arrive in the order the events occurred, and on rare occasions retries can cause duplicate notifications for the same event.
  scope: S3 Event Notifications.
  link: [aren't guaranteed to arrive in the same order](../facts/s3.md#s3-event-notifications-no-order-duplicates)
  link: [duplicate S3 Event Notifications](../facts/s3.md#s3-event-notifications-no-order-duplicates)
s3-eventbridge-all-events-more-targets
  claim: EventBridge delivery is turned on or off for the whole bucket: when enabled, all S3 events are sent to EventBridge without choosing event types, and EventBridge rules can route them to additional targets.
  scope: per bucket, Amazon EventBridge delivery.
  link: [all events are sent to EventBridge](../facts/s3.md#s3-eventbridge-all-events-more-targets)
  link: [route events to additional targets](../facts/s3.md#s3-eventbridge-all-events-more-targets)
s3-express-one-zone-10x-faster-80-percent
  claim: The S3 User Guide overview says S3 Express One Zone is the lowest latency cloud object storage class available today, with data access speeds up to 10x faster and request costs 80 percent lower than S3 Standard.
  scope: S3 Express One Zone storage class; compared with S3 Standard.
  link: [up to 10x faster](../facts/s3.md#s3-express-one-zone-10x-faster-80-percent)
  link: [80 percent lower](../facts/s3.md#s3-express-one-zone-10x-faster-80-percent)
  say: up to ten times faster | eighty percent lower
s3-express-one-zone-hundreds-of-thousands-rps
  claim: For applications that need consistent high performance, S3 Express One Zone is designed for single-digit millisecond latencies and can support hundreds of thousands of requests per second.
  scope: S3 Express One Zone, directory bucket.
  link: [hundreds of thousands of requests per second](../facts/s3.md#s3-express-one-zone-hundreds-of-thousands-rps)
  say: hundreds of thousands of requests per second
s3-express-one-zone-single-digit-ms-single-az
  claim: S3 Express One Zone is a high-performance, single-Availability-Zone storage class built for consistent single-digit millisecond access for the most latency-sensitive applications.
  scope: S3 Express One Zone (EXPRESS_ONEZONE), directory buckets.
  link: [single-digit millisecond data access](../facts/s3.md#s3-express-one-zone-single-digit-ms-single-az)
  link: [single-zone](../facts/s3.md#s3-express-one-zone-single-digit-ms-single-az)
s3-faq-access-analyzer-s3
  claim: IAM Access Analyzer for S3 alerts you when a bucket is configured to allow access to anyone on the internet or is shared with other AWS accounts.
  scope: S3 buckets.
  link: [anyone on the internet](../facts/s3.md#s3-faq-access-analyzer-s3)
s3-faq-access-control-mechanisms
  claim: Access to S3 can be controlled with IAM policies, bucket policies, access point policies, ACLs, Query String Authentication, VPC endpoint policies, SCPs in AWS Organizations, and S3 Block Public Access.
  scope: Amazon S3 resources.
  link: [bucket policies, access point policies](../facts/s3.md#s3-faq-access-control-mechanisms)
s3-faq-archive-classes-summary
  claim: Choose S3 Glacier Flexible Retrieval for archive data that needs retrieval in minutes or free bulk retrievals in 5-12 hours, and S3 Glacier Deep Archive, the lowest cost storage in the cloud, for retrieval within 12 hours.
  scope: S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive.
  link: [free bulk retrievals in 5—12 hours](../facts/s3.md#s3-faq-archive-classes-summary)
  link: [data retrieval within 12 hours](../facts/s3.md#s3-faq-archive-classes-summary)
s3-faq-auto-encrypt-uploads
  claim: S3 automatically encrypts all object uploads to your bucket, as of January 5, 2023.
  scope: per object upload; default; not adjustable.
  link: [automatically encrypts all object uploads](../facts/s3.md#s3-faq-auto-encrypt-uploads)
s3-faq-availability-design-by-class
  claim: S3 Standard is designed for 99.99% availability; S3 Standard-IA, S3 Intelligent-Tiering and S3 Glacier Instant Retrieval for 99.9%; S3 One Zone-IA for 99.5%; S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive for 99.99% availability with an SLA of 99.9%.
  scope: per storage class, design target.
  link: [99.99% availability](../facts/s3.md#s3-faq-availability-design-by-class)
  link: [99.9% availability](../facts/s3.md#s3-faq-availability-design-by-class)
  link: [99.5% availability](../facts/s3.md#s3-faq-availability-design-by-class)
  link: [SLA of 99.9%](../facts/s3.md#s3-faq-availability-design-by-class)
  say: ninety-nine point nine nine percent availability | ninety-nine point nine percent availability | ninety-nine point five percent availability
s3-faq-batch-replication-existing
  claim: S3 Batch Replication replicates existing bucket contents, including objects that previously failed to replicate and objects replicated from another source.
  scope: per replication configuration.
  link: [S3 Batch Replication](../facts/s3.md#s3-faq-batch-replication-existing)
s3-faq-batch-replication-metrics
  claim: You cannot use metrics like bytes pending, operations pending and replication latency to track S3 Batch Replication progress; you can use the operations failed replication metric to monitor existing objects that do not replicate successfully with S3 Batch Replication.
  scope: S3 Batch Replication jobs.
  link: [cannot use metrics like bytes pending](../facts/s3.md#s3-faq-batch-replication-metrics)
s3-faq-block-public-access-default
  claim: All new buckets have Block Public Access turned on by default.
  scope: per new bucket; default; not adjustable.
  link: [Block Public Access turned on by default](../facts/s3.md#s3-faq-block-public-access-default)
s3-faq-bucket-policy-sourcevpce
  claim: A bucket policy can restrict access to a specific VPC endpoint with the aws:sourceVpce condition.
  scope: per bucket policy.
  link: [aws:sourceVpce](../facts/s3.md#s3-faq-bucket-policy-sourcevpce)
s3-faq-checksum-algorithms
  claim: For upload and download integrity checks you can choose SHA-1, SHA-512, SHA-256, CRC32, CRC32C, CRC64NVME, MD5, XXHash64, XXHash3 or XXHash128.
  scope: per upload or download.
  link: [CRC64NVME](../facts/s3.md#s3-faq-checksum-algorithms)
s3-faq-checksum-sdk-crc-default
  claim: The latest AWS SDKs automatically calculate CRC-based checksums for all uploads, and S3 independently verifies the checksum before accepting the object.
  scope: per upload, latest SDKs; default; not adjustable.
  link: [CRC-based checksums](../facts/s3.md#s3-faq-checksum-sdk-crc-default)
s3-faq-checksum-whole-object
  claim: If the SDK does not pre-calculate a checksum, S3 calculates a CRC-based checksum of the whole object, even for multipart uploads.
  scope: per upload without a precalculated checksum.
  link: [whole object, even for multipart uploads](../facts/s3.md#s3-faq-checksum-whole-object)
s3-faq-client-side-encryption-keys
  claim: With a client-side encryption library you keep the keys and encrypt objects before they are sent to S3, so only encrypted objects travel over the internet.
  scope: client-side encryption.
  link: [you retain control of the keys](../facts/s3.md#s3-faq-client-side-encryption-keys)
s3-faq-consistency-list
  claim: S3 also gives strong consistency for list operations: after a write, a listing of the bucket immediately reflects the change.
  scope: list operations.
  link: [strong consistency for list operations](../facts/s3.md#s3-faq-consistency-list)
s3-faq-consistency-read-latest
  claim: After a successful write of a new object or an overwrite of an existing object, any subsequent read immediately receives the latest version of the object.
  scope: per read after a successful write.
  link: [immediately receives the latest version](../facts/s3.md#s3-faq-consistency-read-latest)
s3-faq-consistency-strong
  claim: S3 delivers strong read-after-write consistency automatically, at no additional cost and without changes to performance or availability.
  scope: Amazon S3.
  link: [strong read-after-write consistency](../facts/s3.md#s3-faq-consistency-strong)
  link: [no additional cost](../facts/s3.md#s3-faq-consistency-strong)
s3-faq-copy-within-region-free
  claim: There is no data transfer charge for a COPY within one S3 Region; a COPY between Regions is charged at the pricing page rates.
  scope: COPY requests.
  link: [COPY request](../facts/s3.md#s3-faq-copy-within-region-free)
s3-faq-cross-account-access-billing
  claim: Normal S3 pricing applies when another AWS account accesses your storage, unless you configure the bucket as Requester Pays, in which case the requester pays for requests and downloads.
  scope: access from another AWS account.
  link: [Requester Pays](../facts/s3.md#s3-faq-cross-account-access-billing)
s3-faq-crr-reasons
  claim: CRR gives lower-latency access from other geographic regions and can meet a compliance requirement to keep copies hundreds of miles apart.
  scope: S3 Cross-Region Replication.
  link: [hundreds of miles apart](../facts/s3.md#s3-faq-crr-reasons)
s3-faq-crr-vs-mrap
  claim: CRR moves data across Regions to create isolated replicas, while Multi-Region Access Points route requests across Regions; together they give a replicated multi-Region dataset behind a single global endpoint.
  scope: CRR and Multi-Region Access Points.
  link: [single global endpoint](../facts/s3.md#s3-faq-crr-vs-mrap)
s3-faq-data-transfer-billed-to-source
  claim: Data transfer costs are billed to the source bucket owner.
  scope: S3 data transfer charges.
  link: [source bucket owner](../facts/s3.md#s3-faq-data-transfer-billed-to-source)
s3-faq-data-transfer-same-region-free
  claim: There is no data transfer charge between Amazon EC2 (or any AWS service) and S3 within the same Region.
  scope: data transfer within one Region.
  link: [no Data Transfer charge](../facts/s3.md#s3-faq-data-transfer-same-region-free)
s3-faq-deep-archive-bill-line-item
  claim: S3 Glacier Deep Archive usage and cost show up as an independent service line item on the monthly AWS bill, separate from Amazon S3 usage and costs; in the AWS Cost Management tool, they are included under Amazon S3 usage and cost in the detailed monthly spend reports.
  scope: monthly AWS bill.
  link: [independent service line item](../facts/s3.md#s3-faq-deep-archive-bill-line-item)
s3-faq-deep-archive-integrations
  claim: S3 Glacier Deep Archive works with object tagging, Lifecycle, Object Lock and Replication, and one bucket can mix Deep Archive with S3 Standard, Standard-IA, One Zone-IA and Flexible Retrieval objects.
  scope: S3 Glacier Deep Archive.
  link: [a single Amazon S3 bucket](../facts/s3.md#s3-faq-deep-archive-integrations)
s3-faq-deep-archive-min-180-days
  claim: S3 Glacier Deep Archive objects have a minimum of 180 days of storage; earlier deletion, overwrite or transition incurs a pro-rated charge for the remaining days.
  scope: per object, S3 Glacier Deep Archive; minimum; not adjustable.
  link: [180 days](../facts/s3.md#s3-faq-deep-archive-min-180-days)
  say: one hundred eighty days
s3-faq-deep-archive-price
  claim: S3 Glacier Deep Archive storage starts from $0.00099 per GB-month (about $1 per TB-month).
  scope: S3 Glacier Deep Archive storage, lowest Region price; minimum.
  link: [$0.00099 per GB-month](../facts/s3.md#s3-faq-deep-archive-price)
  link: [about $1 per TB-month](../facts/s3.md#s3-faq-deep-archive-price)
  say: about one dollar per terabyte-month
s3-faq-deep-archive-retrieval-times
  claim: Deep Archive Standard retrieval (the default) returns data within 12 hours, typically starting within 9 hours with S3 Batch Operations; Bulk retrieval typically completes within 48 hours.
  scope: restores from S3 Glacier Deep Archive.
  link: [12 hours](../facts/s3.md#s3-faq-deep-archive-retrieval-times)
  link: [48 hours](../facts/s3.md#s3-faq-deep-archive-retrieval-times)
  link: [9 hours](../facts/s3.md#s3-faq-deep-archive-retrieval-times)
  say: twelve hours | forty-eight hours | nine hours
s3-faq-deep-archive-tape-migration
  claim: To move tape archives into S3 Glacier Deep Archive, AWS suggests Tape Gateway (a virtual tape library for existing backup applications), AWS Snowball for terabytes to petabytes, or AWS Direct Connect.
  scope: tape archive migration.
  link: [Tape Gateway](../facts/s3.md#s3-faq-deep-archive-tape-migration)
  link: [AWS Snowball](../facts/s3.md#s3-faq-deep-archive-tape-migration)
  link: [AWS Direct Connect](../facts/s3.md#s3-faq-deep-archive-tape-migration)
s3-faq-deep-archive-vs-flexible-cost
  claim: S3 Glacier Deep Archive is up to 75% less expensive than S3 Glacier Flexible Retrieval.
  scope: storage price, S3 Glacier Deep Archive compared with S3 Glacier Flexible Retrieval.
  link: [up to 75% less expensive](../facts/s3.md#s3-faq-deep-archive-vs-flexible-cost)
  say: up to seventy-five percent less expensive
s3-faq-delete-is-immediate
  claim: When you tell S3 to delete data, it is deleted immediately and cannot be recovered by AWS.
  scope: per delete request.
  link: [cannot be recovered by AWS](../facts/s3.md#s3-faq-delete-is-immediate)
s3-faq-delete-protection-features
  claim: S3 Versioning, S3 Replication and S3 Object Lock are optional features that add protection beyond durability; a backup application can also back up bucket data.
  scope: per bucket.
  link: [add additional data protection, beyond the durability](../facts/s3.md#s3-faq-delete-protection-features)
s3-faq-directory-bucket-express-only
  claim: Directory buckets only allow objects in the S3 Express One Zone storage class, which processes data within a single Availability Zone.
  scope: directory buckets.
  link: [directory buckets only allow objects stored](../facts/s3.md#s3-faq-directory-bucket-express-only)
s3-faq-directory-bucket-tps
  claim: Each directory bucket can support up to 2 million transactions per second (TPS), independent of the number of directories in the bucket.
  scope: per directory bucket, maximum the bucket type can support; maximum; not adjustable.
  link: [2 million transactions per second](../facts/s3.md#s3-faq-directory-bucket-tps)
  say: two million transactions per second
s3-faq-disable-bucket-hostname
  claim: You cannot completely disable direct access through the bucket hostname, but a bucket policy can reject requests that are not made through an access point.
  scope: per bucket.
  link: [rejects requests not made using an access point](../facts/s3.md#s3-faq-disable-bucket-hostname)
s3-faq-durability-11-nines
  claim: S3 is designed to provide 99.999999999% (11 nines) data durability.
  scope: S3 design target.
  link: [99.999999999%](../facts/s3.md#s3-faq-durability-11-nines)
  link: [11 nines](../facts/s3.md#s3-faq-durability-11-nines)
  say: eleven nines | eleven nines
s3-faq-durability-integrity-checks
  claim: S3 checks integrity end to end on every upload, confirms the data is stored redundantly before the upload succeeds, and keeps checking data at rest over time.
  scope: per object upload and data at rest.
  link: [end-to-end integrity checking](../facts/s3.md#s3-faq-durability-integrity-checks)
s3-faq-durability-not-delete-protection
  claim: S3 durability does not protect against accidental or malicious deletes; you still need to decide what to keep and which controls protect against wrong deletes.
  scope: Amazon S3 durability.
  link: [does not protect against accidental or malicious deletes](../facts/s3.md#s3-faq-durability-not-delete-protection)
s3-faq-encryption-options
  claim: Beyond SSE-S3, you can encrypt S3 data with SSE-C, SSE-KMS, DSSE-KMS, or a client library such as the Amazon S3 Encryption Client.
  scope: encryption of data at rest in Amazon S3.
  link: [SSE-C, SSE-KMS, DSSE-KMS](../facts/s3.md#s3-faq-encryption-options)
s3-faq-encryption-sse-s3-base
  claim: S3 applies S3-managed server-side encryption (SSE-S3) as the base level of encryption to all object uploads.
  scope: per object upload; default; not adjustable.
  link: [SSE-S3](../facts/s3.md#s3-faq-encryption-sse-s3-base)
s3-faq-events-destinations
  claim: S3 Event Notifications can be published to Amazon EventBridge, Amazon SNS, Amazon SQS, or directly to AWS Lambda.
  scope: S3 Event Notifications.
  link: [Amazon EventBridge, Amazon SNS, Amazon SQS](../facts/s3.md#s3-faq-events-destinations)
  link: [directly to AWS Lambda](../facts/s3.md#s3-faq-events-destinations)
s3-faq-events-lifecycle
  claim: You can set up S3 Event Notifications to notify you when S3 Lifecycle transitions or expires objects.
  scope: S3 Event Notifications.
  link: [when S3 Lifecycle transitions or expires objects](../facts/s3.md#s3-faq-events-lifecycle)
s3-faq-events-no-charge
  claim: There is no additional S3 charge for event notifications; you pay only for SNS, SQS or the Lambda function that handles them.
  scope: S3 Event Notifications.
  link: [no additional charges](../facts/s3.md#s3-faq-events-no-charge)
s3-faq-events-prefix-suffix
  claim: Event notifications can be filtered by object name prefixes and suffixes.
  scope: per event notification configuration.
  link: [prefixes and suffixes](../facts/s3.md#s3-faq-events-prefix-suffix)
s3-faq-flexible-40kb-metadata
  claim: S3 Glacier Flexible Retrieval adds 40 KB of metadata per archived object: 32 KB billed at the Glacier rate and 8 KB billed at the S3 Standard rate.
  scope: per object archived to S3 Glacier Flexible Retrieval.
  link: [40 KB](../facts/s3.md#s3-faq-flexible-40kb-metadata)
  link: [32 KB](../facts/s3.md#s3-faq-flexible-40kb-metadata)
  link: [8 KB](../facts/s3.md#s3-faq-flexible-40kb-metadata)
  say: forty kilobytes | thirty-two kilobytes | eight kilobytes
s3-faq-flexible-bulk-free
  claim: Expedited and Standard retrievals have a per-GB retrieval fee and a per-request fee; Bulk retrievals from S3 Glacier Flexible Retrieval are free.
  scope: retrievals from S3 Glacier Flexible Retrieval.
  link: [per-GB retrieval fee and per-request fee](../facts/s3.md#s3-faq-flexible-bulk-free)
  link: [are free](../facts/s3.md#s3-faq-flexible-bulk-free)
s3-faq-flexible-direct-put-glacier
  claim: You can PUT directly into S3 Glacier Flexible Retrieval by specifying GLACIER in the x-amz-storage-class header, or transition objects from any active-data class with Lifecycle rules.
  scope: S3 Glacier Flexible Retrieval.
  link: [GLACIER](../facts/s3.md#s3-faq-flexible-direct-put-glacier)
s3-faq-flexible-expedited-provisioned
  claim: Without provisioned capacity, Expedited retrievals might not be accepted during periods of high demand.
  scope: Expedited retrievals.
  link: [might not be accepted](../facts/s3.md#s3-faq-flexible-expedited-provisioned)
s3-faq-flexible-min-90-days
  claim: S3 Glacier Flexible Retrieval objects have a minimum of 90 days of storage; earlier deletion, overwrite or transition incurs a pro-rated charge for the remaining days.
  scope: per object, S3 Glacier Flexible Retrieval; minimum; not adjustable.
  link: [90 days](../facts/s3.md#s3-faq-flexible-min-90-days)
  say: ninety days
s3-faq-flexible-restore-notification
  claim: S3 Event Notifications can tell you when an object has been restored from S3 Glacier Flexible Retrieval and its temporary copy is available.
  scope: per restore request.
  link: [restore notifications](../facts/s3.md#s3-faq-flexible-restore-notification)
s3-faq-flexible-restore-temp-copy
  claim: A retrieval from S3 Glacier Flexible Retrieval creates a temporary copy in S3 Standard for the number of days you specify, and leaves the archived data intact.
  scope: per restore request.
  link: [temporary copy](../facts/s3.md#s3-faq-flexible-restore-temp-copy)
s3-faq-flexible-retrieval-times
  claim: From S3 Glacier Flexible Retrieval, for all but the largest objects (250MB+), Expedited retrievals are typically made available within 1-5 minutes; Standard retrievals typically complete in 3-5 hours and typically start in minutes when initiated with S3 Batch Operations; Bulk retrievals typically complete within 5-12 hours and are free of charge.
  scope: restores from S3 Glacier Flexible Retrieval; typical times; the Expedited time excludes the largest objects (250MB+).
  link: [1-5 minutes](../facts/s3.md#s3-faq-flexible-retrieval-times)
  link: [3-5 hours](../facts/s3.md#s3-faq-flexible-retrieval-times)
  link: [5-12 hours](../facts/s3.md#s3-faq-flexible-retrieval-times)
  say: one to five minutes | three to five hours | five to twelve hours
s3-faq-flexible-vs-instant-cost
  claim: S3 Glacier Flexible Retrieval costs up to 10% less than S3 Glacier Instant Retrieval, for archive data accessed 1-2 times per year and retrieved asynchronously.
  scope: storage price, S3 Glacier Flexible Retrieval compared with S3 Glacier Instant Retrieval.
  link: [up to 10% lower cost](../facts/s3.md#s3-faq-flexible-vs-instant-cost)
  link: [1-2 times per year](../facts/s3.md#s3-faq-flexible-vs-instant-cost)
s3-faq-free-dto-leave-aws
  claim: AWS offers eligible customers free data transfer out to the internet when they move all of their data off AWS, in accordance with a process that AWS describes in the S3 FAQ.
  scope: eligible customers moving all data off AWS; eligible customers who follow the process that AWS describes.
  link: [free data transfer out to the internet](../facts/s3.md#s3-faq-free-dto-leave-aws)
s3-faq-general-purpose-bucket-classes
  claim: A single general purpose bucket can hold objects in all storage classes except S3 Express One Zone; general purpose buckets are recommended for most use cases.
  scope: general purpose buckets.
  link: [all storage classes except S3 Express One Zone](../facts/s3.md#s3-faq-general-purpose-bucket-classes)
s3-faq-glacier-classes-multi-az
  claim: All S3 Glacier storage classes keep data on multiple devices across physically separated Availability Zones within a Region.
  scope: S3 Glacier storage classes.
  link: [multi-Availability Zone (AZ) resiliency](../facts/s3.md#s3-faq-glacier-classes-multi-az)
s3-faq-ia-to-standard-copy-charges
  claim: Changing an object from S3 Standard-IA to S3 Standard with a COPY request incurs an S3 Standard COPY request charge and an S3 Standard-IA data retrieval charge.
  scope: COPY from S3 Standard-IA to S3 Standard.
  link: [data retrieval](../facts/s3.md#s3-faq-ia-to-standard-copy-charges)
s3-faq-instant-retrieval-availability
  claim: S3 Glacier Instant Retrieval is designed for 99.9% availability, the same as S3 Standard-IA, with service credits if availability is less than 99% in a billing cycle.
  scope: S3 Glacier Instant Retrieval.
  link: [99.9% availability](../facts/s3.md#s3-faq-instant-retrieval-availability)
  link: [less than 99%](../facts/s3.md#s3-faq-instant-retrieval-availability)
s3-faq-instant-retrieval-min-128kb
  claim: S3 Glacier Instant Retrieval has a minimum object storage charge of 128KB.
  scope: per object, S3 Glacier Instant Retrieval; minimum; not adjustable.
  link: [128KB](../facts/s3.md#s3-faq-instant-retrieval-min-128kb)
  say: one hundred twenty-eight kilobytes
s3-faq-instant-retrieval-min-90-days
  claim: S3 Glacier Instant Retrieval objects have a minimum of 90 days of storage; an object deleted, overwritten or transitioned before 90 days incurs a pro-rated charge for the remaining days.
  scope: per object, S3 Glacier Instant Retrieval; minimum; not adjustable.
  link: [90 days](../facts/s3.md#s3-faq-instant-retrieval-min-90-days)
  say: ninety days
s3-faq-instant-retrieval-no-restore
  claim: S3 Glacier Instant Retrieval gives milliseconds access with the same throughput as S3 Standard and S3 Standard-IA; unlike Flexible Retrieval and Deep Archive, no Restore request is needed.
  scope: S3 Glacier Instant Retrieval.
  link: [do not need to issue a Restore request](../facts/s3.md#s3-faq-instant-retrieval-no-restore)
s3-faq-instant-retrieval-once-a-quarter
  claim: S3 Glacier Instant Retrieval is ideal for data accessed about once a quarter that still needs milliseconds retrieval, with a lower storage price and slightly higher access costs than S3 Standard-IA.
  scope: S3 Glacier Instant Retrieval.
  link: [once a quarter](../facts/s3.md#s3-faq-instant-retrieval-once-a-quarter)
s3-faq-intelligent-tiering-default-class
  claim: For changing, unpredictable or unknown access patterns, AWS says S3 Intelligent-Tiering should be the default storage class.
  scope: S3 Intelligent-Tiering.
  link: [should be the default storage class](../facts/s3.md#s3-faq-intelligent-tiering-default-class)
s3-faq-it-archive-restore-times
  claim: Objects in the Archive Access tier return to the Frequent Access tier in 3-5 hours, and within 12 hours from the Deep Archive Access tier, after a Restore request.
  scope: S3 Intelligent-Tiering archive tiers.
  link: [3-5 hours](../facts/s3.md#s3-faq-it-archive-restore-times)
  link: [12 hours](../facts/s3.md#s3-faq-it-archive-restore-times)
  say: three to five hours | twelve hours
s3-faq-it-archive-tiers-90-180
  claim: With the optional archive tiers enabled, objects not accessed for a minimum of 90 days move to the Archive Access tier (up to 71% saving) and after 180 days to the Deep Archive Access tier (up to 95%).
  scope: S3 Intelligent-Tiering optional archive tiers.
  link: [minimum of 90 days](../facts/s3.md#s3-faq-it-archive-tiers-90-180)
  link: [180 days](../facts/s3.md#s3-faq-it-archive-tiers-90-180)
  link: [71%](../facts/s3.md#s3-faq-it-archive-tiers-90-180)
  link: [95%](../facts/s3.md#s3-faq-it-archive-tiers-90-180)
  say: one hundred eighty days | seventy-one percent | ninety-five percent
s3-faq-it-availability-durability
  claim: Intelligent-Tiering is designed for 99.9% availability and 99.999999999% durability, with the same latency and throughput as S3 Standard.
  scope: S3 Intelligent-Tiering, design target.
  link: [99.9% availability](../facts/s3.md#s3-faq-it-availability-durability)
  link: [99.999999999% durability](../facts/s3.md#s3-faq-it-availability-durability)
s3-faq-it-lifecycle-out
  claim: You can lifecycle objects from the S3 Intelligent-Tiering Frequent Access, Infrequent Access and Archive Instant Access tiers to S3 One Zone-IA, S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive.
  scope: objects in the S3 Intelligent-Tiering Frequent Access, Infrequent Access and Archive Instant Access tiers.
  link: [S3 One-Zone Infrequent Access, S3 Glacier Flexible Retrieval](../facts/s3.md#s3-faq-it-lifecycle-out)
s3-faq-it-monitoring-fee
  claim: Intelligent-Tiering charges a small monthly monitoring and automation fee per object, in addition to storage, requests and data transfer.
  scope: per object in S3 Intelligent-Tiering.
  link: [monitoring and automation per object](../facts/s3.md#s3-faq-it-monitoring-fee)
s3-faq-it-moves-back
  claim: An object in the Infrequent Access or Archive Instant Access tier that is accessed later is moved back to the Frequent Access tier automatically.
  scope: per object in S3 Intelligent-Tiering.
  link: [automatically moved back to the Frequent Access tier](../facts/s3.md#s3-faq-it-moves-back)
s3-faq-it-no-min-duration
  claim: S3 Intelligent-Tiering has no minimum storage duration.
  scope: S3 Intelligent-Tiering.
  link: [no minimum storage duration](../facts/s3.md#s3-faq-it-no-min-duration)
s3-faq-it-no-retrieval-fees
  claim: There are no retrieval charges in S3 Intelligent-Tiering, and no tiering or lifecycle charges when objects move between its access tiers.
  scope: S3 Intelligent-Tiering.
  link: [no retrieval charges](../facts/s3.md#s3-faq-it-no-retrieval-fees)
s3-faq-it-small-objects-128kb
  claim: Intelligent-Tiering has no minimum billable object size, but objects smaller than 128KB are not eligible for auto-tiering: they are always charged at Frequent Access rates with no monitoring and automation charge.
  scope: per object, S3 Intelligent-Tiering auto-tiering threshold; fixed; not adjustable.
  link: [128KB](../facts/s3.md#s3-faq-it-small-objects-128kb)
  link: [no minimum billable object size](../facts/s3.md#s3-faq-it-small-objects-128kb)
  say: one hundred twenty-eight kilobytes
s3-faq-it-tiers-30-90-days
  claim: Intelligent-Tiering moves objects not accessed for 30 consecutive days to the Infrequent Access tier (up to 40% saving) and after 90 days of no access to the Archive Instant Access tier (up to 68%).
  scope: per object in S3 Intelligent-Tiering.
  link: [30 consecutive days](../facts/s3.md#s3-faq-it-tiers-30-90-days)
  link: [90 days](../facts/s3.md#s3-faq-it-tiers-30-90-days)
  link: [40%](../facts/s3.md#s3-faq-it-tiers-30-90-days)
  link: [68%](../facts/s3.md#s3-faq-it-tiers-30-90-days)
  say: thirty consecutive days | ninety days | forty percent | sixty-eight percent
s3-faq-lifecycle-example-30-365
  claim: A Lifecycle rule can, for example, archive all objects under the prefix logs/ to S3 Glacier Flexible Retrieval 30 days after creation and expire them after 365 days.
  scope: example Lifecycle rule.
  link: [30 days](../facts/s3.md#s3-faq-lifecycle-example-30-365)
  link: [365 days](../facts/s3.md#s3-faq-lifecycle-example-30-365)
  say: thirty days | three hundred sixty-five days
s3-faq-lifecycle-existing-and-new
  claim: Lifecycle policies apply to both existing and new objects in the bucket.
  scope: per Lifecycle policy.
  link: [both existing and new S3 objects](../facts/s3.md#s3-faq-lifecycle-existing-and-new)
s3-faq-lifecycle-incomplete-multipart
  claim: A Lifecycle rule that expires incomplete multipart uploads removes the uncommitted parts and their storage after a set number of days, so you stop paying for parts that were never completed.
  scope: per Lifecycle policy.
  link: [incomplete multipart uploads](../facts/s3.md#s3-faq-lifecycle-incomplete-multipart)
s3-faq-lifecycle-prefix-or-bucket
  claim: A Lifecycle policy can be specified at the prefix level or at the bucket level.
  scope: per Lifecycle policy.
  link: [prefix or at the bucket level](../facts/s3.md#s3-faq-lifecycle-prefix-or-bucket)
s3-faq-lifecycle-transition-request-charge
  claim: There is no cost to set up Lifecycle policies; a transition request is charged per object when the object becomes eligible for transition.
  scope: per object transitioned.
  link: [charged per object](../facts/s3.md#s3-faq-lifecycle-transition-request-charge)
s3-faq-lifecycle-what
  claim: S3 Lifecycle can transition objects by age from S3 Standard to Standard-IA, One Zone-IA or the Glacier classes, expire objects by age, and expire incomplete multipart uploads by upload age.
  scope: per Lifecycle policy.
  link: [multipart upload expiration](../facts/s3.md#s3-faq-lifecycle-what)
s3-faq-macie-sensitive-data
  claim: Amazon Macie uses machine learning to recognize sensitive data in S3, such as personally identifiable information (PII) or intellectual property, and shows where it is stored.
  scope: Amazon Macie.
  link: [personally identifiable information (PII)](../facts/s3.md#s3-faq-macie-sensitive-data)
s3-faq-mfa-delete
  claim: With Versioning and MFA Delete enabled on a bucket, permanently deleting a version of an object needs two forms of authentication: your AWS account credentials and a valid six-digit code and serial number from an authentication device in your physical possession.
  scope: per versioning-enabled bucket with MFA Delete.
  link: [MFA Delete](../facts/s3.md#s3-faq-mfa-delete)
  link: [two forms of authentication](../facts/s3.md#s3-faq-mfa-delete)
  link: [a valid six-digit code and serial number](../facts/s3.md#s3-faq-mfa-delete)
s3-faq-min-3-az-default
  claim: By default S3 stores data redundantly across a minimum of 3 Availability Zones.
  scope: per object, Regional storage classes; minimum; not adjustable.
  link: [minimum of 3 Availability Zones](../facts/s3.md#s3-faq-min-3-az-default)
  say: a minimum of three Availability Zones
s3-faq-mrap-failover-controls
  claim: Multi-Region Access Points run active-active or active-passive; in active-passive, failover controls shift S3 request traffic to the alternate Region and account within minutes.
  scope: per Multi-Region Access Point.
  link: [active-passive](../facts/s3.md#s3-faq-mrap-failover-controls)
  link: [within minutes](../facts/s3.md#s3-faq-mrap-failover-controls)
s3-faq-mrap-global-accelerator
  claim: Multi-Region Access Points, based on AWS Global Accelerator, route requests over the AWS network to the lowest-latency replicated copy and improve performance by up to 60%.
  scope: per Multi-Region Access Point.
  link: [up to 60%](../facts/s3.md#s3-faq-mrap-global-accelerator)
  link: [Based on AWS Global Accelerator](../facts/s3.md#s3-faq-mrap-global-accelerator)
  say: up to sixty percent
s3-faq-mrap-requester-pays
  claim: The underlying buckets of a Multi-Region Access Point can be Requester Pays buckets; the requester then pays the request and data transfer cost of both the bucket and the access point.
  scope: per Multi-Region Access Point.
  link: [Requester Pays buckets](../facts/s3.md#s3-faq-mrap-requester-pays)
s3-faq-multipart-over-100mb
  claim: For objects larger than 100 MB, AWS says customers should consider multipart upload.
  scope: per object upload.
  link: [100 MB](../facts/s3.md#s3-faq-multipart-over-100mb)
  say: one hundred megabytes
s3-faq-no-minimum-charge
  claim: With S3 you pay only for what you use; there is no minimum charge.
  scope: Amazon S3 billing.
  link: [no minimum charge](../facts/s3.md#s3-faq-no-minimum-charge)
s3-faq-object-lock-across-classes
  claim: Object Lock protection stays in place regardless of the storage class and through Lifecycle transitions between classes.
  scope: per locked object version.
  link: [regardless of which storage class](../facts/s3.md#s3-faq-object-lock-across-classes)
s3-faq-object-lock-cannot-disable
  claim: Once Object Lock is enabled on a bucket, you cannot disable Object Lock or Versioning for that bucket.
  scope: per bucket.
  link: [cannot disable S3 Object Lock or S3 Versioning](../facts/s3.md#s3-faq-object-lock-cannot-disable)
s3-faq-object-lock-legal-hold
  claim: A Legal Hold keeps an object version from being modified or deleted indefinitely until it is explicitly removed.
  scope: per object version.
  link: [Legal Hold](../facts/s3.md#s3-faq-object-lock-legal-hold)
s3-faq-object-lock-modes
  claim: In Governance Mode, accounts with specific IAM permissions can remove WORM protection; in Compliance Mode, no user can remove it, including the root account.
  scope: per object version.
  link: [Governance Mode](../facts/s3.md#s3-faq-object-lock-modes)
  link: [Compliance Mode](../facts/s3.md#s3-faq-object-lock-modes)
  link: [including the root account](../facts/s3.md#s3-faq-object-lock-modes)
s3-faq-object-lock-not-d3p
  claim: For these financial-services record rules, AWS is not a designated third party (D3P); you must select a D3P yourself and name it in the notification to your regulator.
  scope: financial services record-keeping rules.
  link: [not a designated third party (D3P)](../facts/s3.md#s3-faq-object-lock-not-d3p)
s3-faq-object-lock-regulations
  claim: Object Lock supports broker-dealers who must keep records in a non-erasable, non-rewritable format under SEC Rule 17a-4(f), FINRA Rule 4511 or CFTC Regulation 1.31.
  scope: S3 Object Lock.
  link: [SEC Rule 17a-4(f), FINRA Rule 4511, or CFTC Regulation 1.31](../facts/s3.md#s3-faq-object-lock-regulations)
s3-faq-object-lock-replication-all-features
  claim: All replication features, including SRR, CRR, replication metrics, Replication Time Control and Batch Replication, are supported when replicating from Object Lock buckets.
  scope: replication from Object Lock buckets.
  link: [supported while replicating from S3 Object Lock buckets](../facts/s3.md#s3-faq-object-lock-replication-all-features)
s3-faq-object-lock-replication-destination
  claim: To replicate objects from an Object Lock bucket, the destination bucket must also have Object Lock enabled.
  scope: replication from Object Lock buckets.
  link: [must also have S3 Object Lock enabled](../facts/s3.md#s3-faq-object-lock-replication-destination)
s3-faq-object-lock-replication-permissions
  claim: Replicating from an Object Lock bucket needs the permissions s3:GetObjectRetention and s3:GetObjectLegalHold on the source bucket in the replication role; an s3:Get* permission also satisfies this.
  scope: replication IAM role.
  link: [s3:GetObjectRetention and s3:GetObjectLegalHold](../facts/s3.md#s3-faq-object-lock-replication-permissions)
s3-faq-object-lock-retention-types
  claim: Object Lock has two retention types: fixed, where you set the Retain Until Date, and variable, where you turn on an event hold and S3 sets the Retain Until Date when you release the hold.
  scope: per object version.
  link: [Retain Until Date](../facts/s3.md#s3-faq-object-lock-retention-types)
  link: [event hold](../facts/s3.md#s3-faq-object-lock-retention-types)
s3-faq-object-lock-what
  claim: S3 Object Lock prevents an object version from being deleted or overwritten for a period you define or indefinitely, to enforce retention or meet regulatory compliance.
  scope: per object version.
  link: [deleted or overwritten](../facts/s3.md#s3-faq-object-lock-what)
s3-faq-object-size-range
  claim: An individual S3 object can range in size from a minimum of 0 bytes to a maximum of 50 TB.
  scope: per object; maximum; not adjustable.
  link: [50 TB](../facts/s3.md#s3-faq-object-size-range)
  link: [0 bytes](../facts/s3.md#s3-faq-object-size-range)
  say: fifty terabytes | zero bytes
s3-faq-object-tags-replicated
  claim: Object tags can be replicated with Cross-Region Replication; configurations enabled earlier need new permissions before tags replicate.
  scope: S3 Cross-Region Replication.
  link: [Object tags can be replicated](../facts/s3.md#s3-faq-object-tags-replicated)
s3-faq-one-zone-az-loss
  claim: If all or part of an Availability Zone is lost or damaged, data in a One Zone storage class may be lost.
  scope: data in a One Zone storage class.
  link: [may be lost](../facts/s3.md#s3-faq-one-zone-az-loss)
  link: [a One Zone storage class may be lost](../facts/s3.md#s3-faq-one-zone-az-loss)
s3-faq-one-zone-ia-20-percent
  claim: S3 One Zone-IA stores data redundantly within a single Availability Zone at 20% less cost than S3 Standard-IA.
  scope: storage price, S3 One Zone-IA compared with S3 Standard-IA.
  link: [20% less cost](../facts/s3.md#s3-faq-one-zone-ia-20-percent)
  say: twenty percent less cost
s3-faq-one-zone-ia-not-resilient
  claim: S3 One Zone-IA data is not resilient to the loss of availability or the physical loss of an Availability Zone; S3 Standard, S3 Intelligent-Tiering, S3 Standard-IA and the S3 Glacier classes are designed to withstand it.
  scope: S3 One Zone-IA.
  link: [not resilient to the loss of availability](../facts/s3.md#s3-faq-one-zone-ia-not-resilient)
s3-faq-one-zone-ia-sla-99
  claim: S3 One Zone-IA offers a 99% available SLA and is designed for eleven 9’s of durability within its Availability Zone.
  scope: S3 One Zone-IA.
  link: [99% available SLA](../facts/s3.md#s3-faq-one-zone-ia-sla-99)
  say: ninety-nine percent available SLA
s3-faq-one-zone-ia-use-cases
  claim: S3 One Zone-IA suits infrequently accessed backup copies, disaster recovery copies or other easily re-creatable data.
  scope: S3 One Zone-IA.
  link: [easily re-creatable data](../facts/s3.md#s3-faq-one-zone-ia-use-cases)
s3-faq-privatelink-on-prem
  claim: AWS PrivateLink for S3 lets on-premises applications reach S3 over Direct Connect or VPN through interface endpoints, without public IPs, firewall changes or an internet gateway.
  scope: interface VPC endpoints for S3.
  link: [AWS Direct Connect or AWS VPN](../facts/s3.md#s3-faq-privatelink-on-prem)
s3-faq-replication-async
  claim: S3 Replication copies objects automatically and asynchronously across buckets, which can be owned by the same AWS account or by different accounts.
  scope: per replication configuration.
  link: [automatic, asynchronous copying](../facts/s3.md#s3-faq-replication-async)
s3-faq-replication-china
  claim: S3 Replication is not available between AWS China Regions and Regions outside China; replication is possible only within the China Regions.
  scope: AWS China Regions.
  link: [not available between AWS China Regions](../facts/s3.md#s3-faq-replication-china)
s3-faq-replication-cross-account-ownership
  claim: For CRR and SRR you can replicate into a different AWS account and use Ownership Overwrite to give the destination account ownership of the replicated data, keeping source and destination ownership distinct.
  scope: cross-account CRR and SRR.
  link: [Ownership Overwrite](../facts/s3.md#s3-faq-replication-cross-account-ownership)
s3-faq-replication-cross-account-who-pays
  claim: In cross-account replication the source account pays for all data transfer and the destination account pays for the replication PUT requests.
  scope: cross-account replication.
  link: [destination account pays for the replication PUT requests](../facts/s3.md#s3-faq-replication-cross-account-who-pays)
  link: [the source account pays for all data transfer](../facts/s3.md#s3-faq-replication-cross-account-who-pays)
s3-faq-replication-encryption-types
  claim: S3 Replication supports all encryption types that S3 offers. For server-side encryption, the S3 FAQ names SSE-S3, SSE-KMS and SSE-C among the options S3 offers.
  scope: S3 Replication.
  link: [all encryption types](../facts/s3.md#s3-faq-replication-encryption-types)
s3-faq-replication-lifecycle-not-replicated
  claim: Lifecycle actions are not replicated; to apply the same lifecycle to both buckets, enable the same lifecycle configuration on both.
  scope: source and destination buckets.
  link: [Lifecycle actions are not replicated](../facts/s3.md#s3-faq-replication-lifecycle-not-replicated)
s3-faq-replication-metrics
  claim: Replication gives four CloudWatch metrics (operations pending, bytes pending, replication latency, operations failed replication), and s3:Replication event notifications report which objects failed and why.
  scope: per replication rule.
  link: [operations pending, bytes pending, replication latency](../facts/s3.md#s3-faq-replication-metrics)
  link: [s3:Replication](../facts/s3.md#s3-faq-replication-metrics)
s3-faq-replication-metrics-default-rtc
  claim: Replication metrics and events can be enabled per rule and are enabled by default for rules with Replication Time Control.
  scope: per replication rule; default; not adjustable.
  link: [enabled by default for S3 Replication Time Control](../facts/s3.md#s3-faq-replication-metrics-default-rtc)
s3-faq-replication-multiple-destinations
  claim: Replication can send data to multiple destination buckets in the same or different Regions, each with its own storage class, encryption and RTC settings.
  scope: per source bucket.
  link: [multiple destination buckets](../facts/s3.md#s3-faq-replication-multiple-destinations)
s3-faq-replication-other-storage-class
  claim: Replication rules can write the copies into another storage class, in the same or a different Region.
  scope: per replication rule.
  link: [into another storage class](../facts/s3.md#s3-faq-replication-other-storage-class)
s3-faq-replication-pricing
  claim: Replication is billed as destination storage, the primary copy, replication PUT requests and any infrequent-access retrieval charges; CRR also pays inter-Region data transfer out, while SRR has no data transfer charge.
  scope: S3 Replication charges.
  link: [inter-region Data Transfer OUT](../facts/s3.md#s3-faq-replication-pricing)
  link: [no data transfer charges](../facts/s3.md#s3-faq-replication-pricing)
s3-faq-replication-retry-batch
  claim: Objects that fail to replicate at first can be re-replicated with S3 Batch Replication.
  scope: objects that failed to replicate.
  link: [re-replicate objects that fail to replicate initially](../facts/s3.md#s3-faq-replication-retry-batch)
s3-faq-replication-scope
  claim: Replication (CRR and SRR) is configured at the bucket level, a shared prefix level, or the object level using object tags.
  scope: per replication configuration.
  link: [object level using S3 object tags](../facts/s3.md#s3-faq-replication-scope)
s3-faq-replication-versioning-required
  claim: Versioning must be enabled on both the source and destination buckets to enable replication.
  scope: source and destination buckets.
  link: [both the source and destination buckets](../facts/s3.md#s3-faq-replication-versioning-required)
s3-faq-requester-pays-owner-storage
  claim: In general bucket owners pay for all S3 storage of their bucket; Requester Pays is for sharing data without paying for other people's access.
  scope: per Requester Pays bucket.
  link: [bucket owners pay for all Amazon S3 storage](../facts/s3.md#s3-faq-requester-pays-owner-storage)
s3-faq-rtc-events-over-15-min
  claim: With RTC enabled you receive an event notification when an object takes more than 15 minutes to replicate, and another when that object then replicates successfully.
  scope: per replication rule with S3 Replication Time Control.
  link: [more than 15 minutes](../facts/s3.md#s3-faq-rtc-events-over-15-min)
  say: more than fifteen minutes
s3-faq-rtc-sla-credit
  claim: If fewer than 99.9% of objects replicate within 15 minutes for a Region pair in a billing month, the RTC SLA gives a service credit on every object that took longer than 15 minutes.
  scope: per replication Region pair, per billing month.
  link: [service credit on any object](../facts/s3.md#s3-faq-rtc-sla-credit)
s3-faq-secure-by-default
  claim: S3 is secure by default: on creation, only you have access to the buckets you create.
  scope: per new bucket; default; not adjustable.
  link: [secure by default](../facts/s3.md#s3-faq-secure-by-default)
s3-faq-single-put-max
  claim: The largest object that can be uploaded in a single PUT is 5 GB.
  scope: per PUT request; maximum; not adjustable.
  link: [5 GB](../facts/s3.md#s3-faq-single-put-max)
  say: five gigabytes
s3-faq-sla-service-credit
  claim: The S3 SLA provides a service credit if the monthly uptime percentage falls below the service commitment in any billing cycle.
  scope: per billing cycle.
  link: [service credit](../facts/s3.md#s3-faq-sla-service-credit)
s3-faq-srr-reasons
  claim: SRR keeps a copy of your data in a separate AWS account in the same Region for data sovereignty and compliance, aggregates logs from several buckets, or mirrors test and development environments.
  scope: S3 Same-Region Replication.
  link: [separate AWS account in the same region](../facts/s3.md#s3-faq-srr-reasons)
s3-faq-sse-c-keys
  claim: With SSE-C, S3 performs the encryption and decryption while you retain control of the encryption keys and manage the keys you send to S3.
  scope: per object encrypted with SSE-C.
  link: [you retain control of the encryption keys](../facts/s3.md#s3-faq-sse-c-keys)
  link: [while you retain control of the encryption keys](../facts/s3.md#s3-faq-sse-c-keys)
s3-faq-standard-ia-min-128kb
  claim: S3 Standard-IA has a minimum object storage charge of 128KB; smaller objects are charged as if they were 128KB.
  scope: per object, S3 Standard-IA; minimum; not adjustable.
  link: [128KB](../facts/s3.md#s3-faq-standard-ia-min-128kb)
  say: one hundred twenty-eight kilobytes
s3-faq-standard-ia-min-30-days
  claim: Data deleted from S3 Standard-IA within 30 days is charged for the full 30 days.
  scope: per object, S3 Standard-IA; minimum; not adjustable.
  link: [30 days](../facts/s3.md#s3-faq-standard-ia-min-30-days)
  say: thirty days
s3-faq-standard-ia-retrieval-charge
  claim: S3 Standard-IA combines a low per-GB storage price with a per-GB retrieval charge, and keeps the durability, throughput and low latency of S3 Standard.
  scope: S3 Standard-IA.
  link: [per-GB retrieval charge](../facts/s3.md#s3-faq-standard-ia-retrieval-charge)
s3-faq-standard-ia-tier-down
  claim: Lifecycle policies can tier objects from S3 Standard-IA to S3 One Zone-IA, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive.
  scope: Lifecycle transitions from S3 Standard-IA.
  link: [from S3 Standard-IA to S3 One Zone-IA](../facts/s3.md#s3-faq-standard-ia-tier-down)
s3-faq-standard-vs-ia-access-frequency
  claim: S3 Standard is the best choice when you access data more than once a month; S3 Standard-IA suits data kept for at least a month and accessed once every month or two.
  scope: S3 Standard and S3 Standard-IA.
  link: [more than once a month](../facts/s3.md#s3-faq-standard-vs-ia-access-frequency)
  link: [once every month or two](../facts/s3.md#s3-faq-standard-vs-ia-access-frequency)
s3-faq-storage-class-cost-structure
  claim: Each S3 storage class charges a fee to store data and fees to access it; choose by access pattern and retention time for the lowest total cost over the data's lifetime.
  scope: all storage classes.
  link: [access patterns and retention time](../facts/s3.md#s3-faq-storage-class-cost-structure)
s3-faq-storage-unlimited
  claim: The total volume of data and the number of objects you can store in S3 are unlimited.
  scope: Amazon S3.
  link: [unlimited](../facts/s3.md#s3-faq-storage-unlimited)
s3-faq-ta-edge-locations
  claim: S3 Transfer Acceleration uses CloudFront’s globally distributed edge locations; data arriving at an edge location is routed to the bucket over an optimized network path.
  scope: per accelerated transfer.
  link: [optimized network path](../facts/s3.md#s3-faq-ta-edge-locations)
s3-faq-ta-multipart
  claim: Transfer Acceleration supports all bucket-level features, including multipart uploads.
  scope: buckets with Transfer Acceleration.
  link: [multipart uploads](../facts/s3.md#s3-faq-ta-multipart)
s3-faq-ta-not-faster-no-charge
  claim: If AWS determines that Transfer Acceleration is not likely to be faster than a regular transfer, it does not charge for acceleration on that transfer and may bypass the acceleration system.
  scope: per accelerated transfer.
  link: [we will not charge](../facts/s3.md#s3-faq-ta-not-faster-no-charge)
s3-faq-ta-vs-direct-connect
  claim: Direct Connect suits a private networking requirement; Transfer Acceleration is best for data sent from distributed client locations over the public internet or where network conditions are variable.
  scope: upload path choice.
  link: [distributed client locations over the public internet](../facts/s3.md#s3-faq-ta-vs-direct-connect)
s3-faq-ta-vs-mrap
  claim: S3 Transfer Acceleration can help accelerate long-distance transfers of larger objects to and from a single S3 bucket; S3 Multi-Region Access Points give similar accelerated transfers over the AWS global network, but across many S3 buckets in multiple AWS Regions.
  scope: Transfer Acceleration compared with Multi-Region Access Points.
  link: [a single Amazon S3 bucket](../facts/s3.md#s3-faq-ta-vs-mrap)
s3-faq-table-bucket-iceberg
  claim: A table bucket is purpose-built for storing tables in the Apache Iceberg format.
  scope: table buckets.
  link: [Apache Iceberg](../facts/s3.md#s3-faq-table-bucket-iceberg)
s3-faq-tape-gateway-deep-archive
  claim: Tape Gateway supports archiving new virtual tapes directly to S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive, and helps move tape-based backups to AWS without any changes to existing backup workflows.
  scope: Tape Gateway.
  link: [archiving your new virtual tapes directly](../facts/s3.md#s3-faq-tape-gateway-deep-archive)
s3-faq-traffic-spikes
  claim: S3 is designed to handle traffic for any internet application; its scale spreads the load so that no individual application is affected by traffic spikes.
  scope: Amazon S3.
  link: [no individual application is affected by traffic spikes](../facts/s3.md#s3-faq-traffic-spikes)
s3-faq-two-way-replication-rules
  claim: Bidirectional replication is a pair of rules: one from the source bucket to the bucket holding the replicas, and a second rule from that bucket back to the source; the buckets can be in the same or different Regions.
  scope: pair of buckets.
  link: [second replication rule](../facts/s3.md#s3-faq-two-way-replication-rules)
s3-faq-vector-bucket
  claim: A vector bucket is purpose-built for storing and querying vectors through dedicated vector APIs, not the S3 object APIs.
  scope: vector buckets.
  link: [dedicated vector APIs](../facts/s3.md#s3-faq-vector-bucket)
s3-faq-versioning-rollback-window
  claim: Lifecycle rules plus Versioning can give a rollback window, for example by archiving previous versions to S3 Glacier Flexible Retrieval and deleting them after 100 days.
  scope: per versioning-enabled bucket.
  link: [100-day window](../facts/s3.md#s3-faq-versioning-rollback-window)
  say: a hundred-day window
s3-faq-vpce-both-same-vpc
  claim: You can use both interface and gateway endpoints for S3 in the same VPC; only requests to the endpoint-specific DNS names go through the interface endpoint and all other requests keep using the gateway endpoint.
  scope: per VPC.
  link: [VPC endpoint specific names](../facts/s3.md#s3-faq-vpce-both-same-vpc)
s3-faq-vpce-choose
  claim: AWS recommends interface endpoints to reach S3 from on premises or from a VPC in another Region, and gateway endpoints for same-Region VPC access because gateway endpoints are not billed.
  scope: VPC endpoints for S3.
  link: [gateway VPC endpoints as they are not billed](../facts/s3.md#s3-faq-vpce-choose)
s3-faq-vpce-two-types
  claim: There are two types of VPC endpoints for S3: gateway endpoints, a target in your route table, and interface endpoints, which use private IPs and can be reached from your VPC, on premises, or another Region.
  scope: VPC endpoints for S3.
  link: [gateway VPC endpoints and interface VPC endpoints](../facts/s3.md#s3-faq-vpce-two-types)
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
s3-flat-namespace-no-folders
  claim: The S3 data model is flat: a bucket stores objects and there is no hierarchy of subbuckets or subfolders. Folders are inferred from key name prefixes and delimiters.
  scope: general purpose buckets.
  link: [flat structure](../facts/s3.md#s3-flat-namespace-no-folders)
  link: [no hierarchy of subbuckets or subfolders](../facts/s3.md#s3-flat-namespace-no-folders)
  link: [key name prefixes and delimiters](../facts/s3.md#s3-flat-namespace-no-folders)
s3-flexible-large-objects-48-hours
  claim: From S3 Glacier Flexible Retrieval, for any retrieval option, objects larger than 5 TB typically finish restoring within 48 hours, with up to 300 megabytes per second (MBps) of retrieval throughput.
  scope: per object, S3 Glacier Flexible Retrieval; any retrieval option, objects larger than 5 TB.
  link: [larger than 5 TB](../facts/s3.md#s3-flexible-large-objects-48-hours)
  link: [within 48 hours](../facts/s3.md#s3-flexible-large-objects-48-hours)
  link: [300 megabytes per second](../facts/s3.md#s3-flexible-large-objects-48-hours)
  say: larger than five terabytes | within forty-eight hours | three hundred megabytes per second
s3-general-purpose-bucket-all-classes
  claim: A general purpose bucket is the original bucket type, recommended for most use cases; it can hold any number of objects across all storage classes except S3 Express One Zone, and stores objects redundantly across multiple Availability Zones.
  scope: general purpose buckets.
  link: [except for S3 Express One Zone](../facts/s3.md#s3-general-purpose-bucket-all-classes)
  link: [recommended for most use cases and access patterns](../facts/s3.md#s3-general-purpose-bucket-all-classes)
  link: [redundantly store objects across multiple Availability Zones](../facts/s3.md#s3-general-purpose-bucket-all-classes)
s3-glacier-archive-max-size
  claim: One S3 Glacier archive can be at most 40,000 Gigabytes.
  scope: per archive; maximum; not adjustable.
  link: [40,000 Gigabytes](../facts/s3-glacier.md#s3-glacier-archive-max-size)
  say: forty thousand gigabytes
s3-glacier-change-vault-service-closed-2025-10
  claim: Amazon Glacier, the original standalone vault-based service, is no longer accepting new customers; the AWS list of services in maintenance shows Amazon S3 Glacier Direct with an announcement date of 2025-10-07. Existing data stays secure and accessible indefinitely, and for archival storage AWS recommends the S3 Glacier storage classes.
  scope: Amazon Glacier vaults and the 2012 REST API; existing customers continue.
  link: [2025-10-07](../facts/s3-glacier.md#s3-glacier-change-vault-service-closed-2025-10)
  link: [is no longer accepting new customers](../facts/s3-glacier.md#s3-glacier-change-vault-service-closed-2025-10)
  link: [Amazon Glacier storage classes in Amazon S3](../facts/s3-glacier.md#s3-glacier-change-vault-service-closed-2025-10)
  say: October seventh, twenty twenty-five | closed to new customers | the S3 Glacier storage classes
s3-glacier-provisioned-capacity-units-max
  claim: An account can purchase at most 2 S3 Glacier provisioned capacity units in each supported Region.
  scope: per account, in each supported Region; maximum; not adjustable.
  link: [2](../facts/s3-glacier.md#s3-glacier-provisioned-capacity-units-max)
  say: two
s3-glacier-random-restore-quota
  claim: S3 Glacier allows 35 random restore requests per PiB stored per day.
  scope: per PiB stored, per day; maximum; not adjustable.
  link: [35](../facts/s3-glacier.md#s3-glacier-random-restore-quota)
  say: thirty-five
s3-glacier-vault-lock-24-hour-validation
  claim: Locking a vault takes two steps; after the lock is initiated, you have 24 hours to validate the Vault Lock policy and complete the lock before the lock ID expires.
  scope: per Vault Lock initiation (lock ID); fixed; not adjustable.
  link: [24 hours](../facts/s3-glacier.md#s3-glacier-vault-lock-24-hour-validation)
s3-glacier-vault-lock-policy-immutable
  claim: Glacier Vault Lock enforces compliance controls such as write once read many (WORM) on an Amazon Glacier vault with a Vault Lock policy; once the policy is locked it can no longer be changed or deleted.
  scope: per Amazon Glacier vault.
  link: [lock the policy from future edits](../facts/s3-glacier.md#s3-glacier-vault-lock-policy-immutable)
  link: [can no longer be changed or deleted](../facts/s3-glacier.md#s3-glacier-vault-lock-policy-immutable)
s3-glacier-vault-lock-vs-access-policy
  claim: A Vault Lock policy differs from a vault access policy: both control access to the vault, but only the Vault Lock policy can be locked against future changes, for regulatory controls; the access policy is for controls that change often.
  scope: per Amazon Glacier vault.
  link: [can be locked to prevent future changes](../facts/s3-glacier.md#s3-glacier-vault-lock-vs-access-policy)
  link: [subject to frequent modification](../facts/s3-glacier.md#s3-glacier-vault-lock-vs-access-policy)
s3-glacier-vaults-per-account
  claim: An account can have at most 1,000 S3 Glacier vaults per Region; the quota is not adjustable.
  scope: per account, per Region; maximum; not adjustable.
  link: [1,000](../facts/s3-glacier.md#s3-glacier-vaults-per-account)
  say: one thousand
s3-global-bucket-name-freed-on-delete
  claim: A global general purpose bucket name is unavailable to anyone else in the partition while the bucket exists; when the bucket is deleted, the name becomes available again for anyone to re-create.
  scope: shared global namespace, per partition.
  link: [becomes available again in the global namespace](../facts/s3.md#s3-global-bucket-name-freed-on-delete)
  link: [unavailable for anyone else to create](../facts/s3.md#s3-global-bucket-name-freed-on-delete)
s3-guardduty-s3-protection-cloudtrail-events
  claim: With the S3 protection feature, Amazon GuardDuty analyzes AWS CloudTrail management and data events for S3 resources and monitors them for malicious and suspicious activity.
  scope: Amazon GuardDuty S3 protection; S3 protection configured in GuardDuty.
  link: [S3 protection feature in GuardDuty](../facts/s3.md#s3-guardduty-s3-protection-cloudtrail-events)
s3-hot-objects-503-over-5000
  claim: Sustained high request rates (typically over 5,000 requests per second to a small number of objects) can return HTTP 503 slowdown responses; each AWS SDK retries automatically with exponential backoff.
  scope: a small number of objects; typically sustained rates.
  link: [over 5,000 requests per second](../facts/s3.md#s3-hot-objects-503-over-5000)
  say: over five thousand requests per second
s3-ia-classes-millisecond-access-retrieval-fee
  claim: S3 Standard-IA and S3 One Zone-IA are for long-lived, infrequently accessed data; objects stay available for millisecond access like S3 Standard, but S3 charges a retrieval fee for them.
  scope: S3 Standard-IA and S3 One Zone-IA.
  link: [available for millisecond access](../facts/s3.md#s3-ia-classes-millisecond-access-retrieval-fee)
  link: [charges a retrieval fee for these objects](../facts/s3.md#s3-ia-classes-millisecond-access-retrieval-fee)
s3-ia-min-billable-size
  claim: S3 Standard-IA and S3 One Zone-IA bill a minimum of 128 KB per object: an object smaller than 128 KB is charged as 128 KB, so these classes suit objects larger than 128 KB kept for at least 30 days.
  scope: per object in S3 Standard-IA or S3 One Zone-IA; minimum.
  link: [128 KB](../facts/s3.md#s3-ia-min-billable-size)
  say: one hundred twenty-eight kilobytes
s3-ia-min-duration-charge
  claim: S3 Standard-IA and S3 One Zone-IA have a 30-day minimum storage duration: an object deleted, overwritten or transitioned before 30 days is charged the normal storage charge plus a pro-rated charge for the rest of the 30 days.
  scope: per object in S3 Standard-IA or S3 One Zone-IA; minimum; object deleted, overwritten or transitioned before 30 days.
  link: [30 days](../facts/s3.md#s3-ia-min-duration-charge)
  link: [pro-rated charge for the remainder of the 30-day minimum](../facts/s3.md#s3-ia-min-duration-charge)
  say: thirty days | a pro-rated charge for the rest of the thirty days
s3-int-tiering-archive-retrieval-times
  claim: A Standard retrieval from the Intelligent-Tiering Archive Access tier takes 3–5 hours and from the Deep Archive Access tier occurs within 12 hours; the tiers perform like S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive, and the Archive Instant Access tier keeps millisecond access.
  scope: per object in the S3 Intelligent-Tiering archive tiers; Standard retrieval.
  link: [3–5 hours](../facts/s3.md#s3-int-tiering-archive-retrieval-times)
  link: [within 12 hours](../facts/s3.md#s3-int-tiering-archive-retrieval-times)
  say: three to five hours | within twelve hours
s3-int-tiering-automatic-tiers
  claim: For a low monthly object monitoring and automation charge, S3 Intelligent-Tiering moves an object to the Infrequent Access tier after 30 consecutive days without access and to the Archive Instant Access tier after 90 days of no access, without performance impact. Objects smaller than 128 KB are not monitored, are not eligible for automatic tiering and always stay in the Frequent Access tier.
  scope: per object in S3 Intelligent-Tiering; fixed; objects of 128 KB or more.
  link: [30 consecutive days](../facts/s3.md#s3-int-tiering-automatic-tiers)
  link: [90 days](../facts/s3.md#s3-int-tiering-automatic-tiers)
  say: thirty consecutive days | ninety days
s3-int-tiering-move-back
  claim: When an object in the Infrequent Access or Archive Instant Access tier of S3 Intelligent-Tiering is accessed again, it is moved back to the Frequent Access tier automatically; other actions do not count as access that moves it back.
  scope: per object in S3 Intelligent-Tiering.
  link: [automatically moved back to the Frequent Access tier](../facts/s3.md#s3-int-tiering-move-back)
  link: [don't constitute access](../facts/s3.md#s3-int-tiering-move-back)
  say: moved back to the Frequent Access tier
s3-int-tiering-no-retrieval-fees
  claim: S3 Intelligent-Tiering has no retrieval fees and no minimum storage duration, and is designed for 99.9% availability and 99.999999999% durability.
  scope: S3 Intelligent-Tiering storage class; a monthly per-object monitoring and automation charge applies instead.
  link: [no retrieval fees](../facts/s3.md#s3-int-tiering-no-retrieval-fees)
  link: [99.9%](../facts/s3.md#s3-int-tiering-no-retrieval-fees)
  say: no retrieval fees | ninety-nine point nine percent
s3-int-tiering-optional-archive-tiers
  claim: The optional Archive Access tier archives objects not accessed for a minimum of 90 consecutive days and the optional Deep Archive Access tier after a minimum of 180 consecutive days; for both, the number of days can be set up to a maximum of 730 days, and objects in them must be restored with RestoreObject before they can be read.
  scope: per S3 Intelligent-Tiering configuration; minimum; the number of days of no access is configurable, up to a maximum of 730 days.
  link: [minimum of 90 consecutive days](../facts/s3.md#s3-int-tiering-optional-archive-tiers)
  link: [minimum of 180 consecutive days](../facts/s3.md#s3-int-tiering-optional-archive-tiers)
  link: [maximum of 730 days](../facts/s3.md#s3-int-tiering-optional-archive-tiers)
  say: at least ninety consecutive days | at least one hundred eighty consecutive days | up to seven hundred thirty days
s3-int-tiering-restore-rate
  claim: Restores from the S3 Intelligent-Tiering Archive Access and Deep Archive Access tiers are limited to 1,000 transactions per second (TPS) of restore requests per account per Region.
  scope: per account, per Region; maximum; adjustable; restores from the Archive Access and Deep Archive Access tiers; increased restoration limits through AWS Support.
  link: [1,000 transactions per second (TPS)](../facts/s3.md#s3-int-tiering-restore-rate)
  say: one thousand transactions per second
s3-int-tiering-savings
  claim: The S3 Intelligent-Tiering page says the class moves objects not accessed for 30 consecutive days to the Infrequent Access tier for savings of 40%, after 90 days of no access to the Archive Instant Access tier with savings of 68%, and, when turned on, objects not accessed for 180 days to the Deep Archive Access tier with up to 95% in storage cost savings.
  scope: S3 Intelligent-Tiering access tiers; marketing figures from the storage class page.
  link: [40%](../facts/s3.md#s3-int-tiering-savings)
  link: [68%](../facts/s3.md#s3-int-tiering-savings)
  link: [up to 95%](../facts/s3.md#s3-int-tiering-savings)
  say: forty percent | sixty-eight percent | up to ninety-five percent
s3-int-tiering-small-objects
  claim: An object smaller than 128 KB in S3 Intelligent-Tiering is not monitored and not eligible for automatic tiering: it always stays in the Frequent Access tier, is billed at Frequent Access rates and does not incur the monitoring and automation charge.
  scope: per object in S3 Intelligent-Tiering; minimum; object smaller than 128 KB.
  link: [128 KB](../facts/s3.md#s3-int-tiering-small-objects)
  link: [always stored in the Frequent Access tier](../facts/s3.md#s3-int-tiering-small-objects)
  say: one hundred twenty-eight kilobytes | always kept in the Frequent Access tier
s3-intelligent-tiering-archive-tiers-need-restore
  claim: Intelligent-Tiering has three automatic low-latency tiers (Frequent Access, Infrequent Access, Archive Instant Access) and two optional archive tiers (Archive Access, Deep Archive Access) that you activate only for data read asynchronously; objects in the optional archive tiers must be restored with RestoreObject before access.
  scope: S3 Intelligent-Tiering; Archive Access and Deep Archive Access are activated per bucket configuration.
  link: [two optional archive access tiers](../facts/s3.md#s3-intelligent-tiering-archive-tiers-need-restore)
  link: [first restore the object by using RestoreObject](../facts/s3.md#s3-intelligent-tiering-archive-tiers-need-restore)
  link: [only if your objects can be accessed asynchronously](../facts/s3.md#s3-intelligent-tiering-archive-tiers-need-restore)
s3-intelligent-tiering-automatic-tiers
  claim: Intelligent-Tiering automatically stores objects in three access tiers: one for frequent access, a lower-cost one for infrequent access and a very low-cost one for rarely accessed data; it monitors access patterns for a low monthly per-object monitoring and automation charge.
  scope: S3 Intelligent-Tiering.
  link: [automatically stores objects in three access tiers](../facts/s3.md#s3-intelligent-tiering-automatic-tiers)
  link: [a low monthly object monitoring and automation charge](../facts/s3.md#s3-intelligent-tiering-automatic-tiers)
s3-intelligent-tiering-ideal-for-unknown-access
  claim: S3 Intelligent-Tiering is the class for data with unknown, changing or unpredictable access patterns, independent of object size or retention period, and can be the default class for almost any workload.
  scope: S3 Intelligent-Tiering.
  link: [unknown, changing, or unpredictable access patterns](../facts/s3.md#s3-intelligent-tiering-ideal-for-unknown-access)
  link: [the default storage class for virtually any workload](../facts/s3.md#s3-intelligent-tiering-ideal-for-unknown-access)
s3-intelligent-tiering-purpose
  claim: S3 Intelligent-Tiering moves objects between access tiers automatically as access patterns change, with no retrieval fees; it is the class to choose for data with unknown or changing access patterns.
  scope: S3 Intelligent-Tiering.
  link: [data that has unknown or changing access patterns](../facts/s3.md#s3-intelligent-tiering-purpose)
  link: [there are no retrieval fees for S3 Intelligent-Tiering](../facts/s3.md#s3-intelligent-tiering-purpose)
  link: [most cost-effective access tier](../facts/s3.md#s3-intelligent-tiering-purpose)
s3-intelligent-tiering-small-objects-frequent-tier
  claim: An object smaller than 128 KB in S3 Intelligent-Tiering is not monitored and not eligible for auto-tiering; it always stays in the Frequent Access tier.
  scope: per object, S3 Intelligent-Tiering; minimum; object size below 128 KB.
  link: [less than 128 KB](../facts/s3.md#s3-intelligent-tiering-small-objects-frequent-tier)
  link: [always stored in the Frequent Access tier](../facts/s3.md#s3-intelligent-tiering-small-objects-frequent-tier)
  say: less than one hundred twenty-eight kilobytes
s3-lifecycle-abort-incomplete-multipart
  claim: A lifecycle rule with the AbortIncompleteMultipartUpload action stops multipart uploads that are not completed within a set number of days after they started, and deletes their parts. AWS recommends this rule as a best practice to minimize storage costs; it applies to existing and future multipart uploads and never deletes objects.
  scope: per bucket lifecycle rule; the number of days after initiation is set in the rule.
  link: [AbortIncompleteMultipartUpload](../facts/s3.md#s3-lifecycle-abort-incomplete-multipart)
  link: [stops the multipart upload and deletes the parts](../facts/s3.md#s3-lifecycle-abort-incomplete-multipart)
  link: [no objects are deleted by this lifecycle action](../facts/s3.md#s3-lifecycle-abort-incomplete-multipart)
s3-lifecycle-archive-transition-async-billing-at-rule-date
  claim: Lifecycle transitions to Glacier Flexible Retrieval and Deep Archive run asynchronously, so the physical move can lag the rule date, but you are charged at the destination class rate from the date the rule is satisfied. The one exception is a transition to Intelligent-Tiering, where billing changes after the physical transition completes.
  scope: per transitioned object.
  link: [might be a delay between the transition date](../facts/s3.md#s3-lifecycle-archive-transition-async-billing-at-rule-date)
  link: [from the date the lifecycle rule is satisfied](../facts/s3.md#s3-lifecycle-archive-transition-async-billing-at-rule-date)
  link: [billing changes occur after the physical transition completes](../facts/s3.md#s3-lifecycle-archive-transition-async-billing-at-rule-date)
s3-lifecycle-billing-changes-at-eligibility
  claim: If S3 moves or expires an object later than it became eligible, billing changes apply as soon as the object becomes eligible; the exception is a transition to S3 Intelligent-Tiering, which is billed at the new class only after the transition.
  scope: per object, Lifecycle actions.
  link: [as soon as the object becomes eligible](../facts/s3.md#s3-lifecycle-billing-changes-at-eligibility)
  link: [billing changes don't occur until](../facts/s3.md#s3-lifecycle-billing-changes-at-eligibility)
s3-lifecycle-conflict-cost-optimized
  claim: When Lifecycle rules overlap, S3 Lifecycle optimizes for cost: of two overlapping expirations the shorter one is honored, and of two overlapping transitions the lower-cost storage class is chosen.
  scope: overlapping Lifecycle rules.
  link: [the shorter expiration policy is honored](../facts/s3.md#s3-lifecycle-conflict-cost-optimized)
  link: [the lower-cost storage class](../facts/s3.md#s3-lifecycle-conflict-cost-optimized)
  link: [optimizes for cost](../facts/s3.md#s3-lifecycle-conflict-cost-optimized)
s3-lifecycle-conflict-deletion-wins
  claim: When an object is eligible for several Lifecycle actions on the same day, permanent deletion takes precedence over transition, and an S3 Glacier Flexible Retrieval transition wins over an S3 Standard-IA or One Zone-IA transition.
  scope: per object, actions on the same day.
  link: [Permanent deletion takes precedence over transition](../facts/s3.md#s3-lifecycle-conflict-deletion-wins)
  link: [chooses the S3 Glacier Flexible Retrieval transition](../facts/s3.md#s3-lifecycle-conflict-deletion-wins)
s3-lifecycle-conflict-intelligent-tiering-favored
  claim: An exception to the cheapest-path rule: S3 Lifecycle favors S3 Intelligent-Tiering over any storage class except S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive.
  scope: overlapping Lifecycle rules.
  link: [S3 Intelligent-Tiering is favored by S3 Lifecycle](../facts/s3.md#s3-lifecycle-conflict-intelligent-tiering-favored)
s3-lifecycle-date-action-repeats
  claim: A date-based Lifecycle action is not applied only once: S3 keeps applying it after the date has passed, for as long as the rule status is Enabled.
  scope: per date-based Lifecycle rule.
  link: [not a one-time action](../facts/s3.md#s3-lifecycle-date-action-repeats)
  link: [as long as the rule status is](../facts/s3.md#s3-lifecycle-date-action-repeats)
s3-lifecycle-days-rounded-to-midnight-utc
  claim: For a days-based Lifecycle action, S3 adds the days in the rule to the object creation time and rounds the result up to the next day at midnight UTC.
  scope: per days-based Lifecycle rule.
  link: [the next day at midnight UTC](../facts/s3.md#s3-lifecycle-days-rounded-to-midnight-utc)
s3-lifecycle-early-transition-charge
  claim: Transitioning an object out of a storage class before that class's minimum storage duration is billed for the remainder of the duration.
  scope: per object transitioned by Lifecycle; the source class has a minimum storage duration.
  link: [charged for the remainder of that duration](../facts/s3.md#s3-lifecycle-early-transition-charge)
  say: charged for the rest of the minimum duration
s3-lifecycle-encrypted-objects-stay-encrypted
  claim: Encrypted objects remain encrypted throughout a storage class transition.
  scope: per transitioned object.
  link: [encrypted objects remain encrypted](../facts/s3.md#s3-lifecycle-encrypted-objects-stay-encrypted)
s3-lifecycle-expiration-depends-on-versioning
  claim: S3 makes all expired objects unavailable; whether they are permanently removed depends on the versioning state of the bucket.
  scope: per expired object.
  link: [makes all expired objects unavailable](../facts/s3.md#s3-lifecycle-expiration-depends-on-versioning)
  link: [depends on the versioning state of the bucket](../facts/s3.md#s3-lifecycle-expiration-depends-on-versioning)
s3-lifecycle-expiration-keeps-incomplete-mpu
  claim: Expiration actions do not remove incomplete multipart uploads; that needs the AbortIncompleteMultipartUpload Lifecycle action.
  scope: per Lifecycle expiration rule.
  link: [don't remove incomplete multipart uploads](../facts/s3.md#s3-lifecycle-expiration-keeps-incomplete-mpu)
  link: [AbortIncompleteMultipartUpload](../facts/s3.md#s3-lifecycle-expiration-keeps-incomplete-mpu)
s3-lifecycle-expiration-versioned-delete-marker
  claim: In a versioning-enabled bucket, when a Lifecycle expiration acts on an object whose current version is not a delete marker, S3 adds a delete marker with a unique version ID: the delete marker becomes the current version and the previous current version becomes noncurrent. Object expiration applies only to an object's current version.
  scope: per versioning-enabled bucket.
  link: [adds a delete marker](../facts/s3.md#s3-lifecycle-expiration-versioned-delete-marker)
  link: [applies only to an object's current version](../facts/s3.md#s3-lifecycle-expiration-versioned-delete-marker)
s3-lifecycle-expire-glacier-min-charge
  claim: If a Lifecycle expiration rule expires objects that have been in S3 Glacier Flexible Retrieval for less than 90 days, you are charged for 90 days; for S3 Glacier Deep Archive under 180 days, you are charged for 180 days.
  scope: per object, S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive; minimum; expired by a Lifecycle rule before the minimum duration.
  link: [charged for 90 days](../facts/s3.md#s3-lifecycle-expire-glacier-min-charge)
  link: [charged for 180 days](../facts/s3.md#s3-lifecycle-expire-glacier-min-charge)
  say: charged for ninety days | charged for one hundred eighty days
s3-lifecycle-expire-ia-30-day-charge
  claim: If a Lifecycle expiration rule expires objects that have been in S3 Standard-IA or S3 One Zone-IA for less than 30 days, you are charged for 30 days.
  scope: per object, S3 Standard-IA and S3 One Zone-IA; minimum; expired by a Lifecycle rule before 30 days.
  link: [charged for 30 days](../facts/s3.md#s3-lifecycle-expire-ia-30-day-charge)
  say: charged for thirty days
s3-lifecycle-expired-object-not-charged
  claim: There may be a delay between an object's expiration date and its removal, but you are not charged for the expiration or for storage time after the object has expired.
  scope: per object; after Lifecycle expiration.
  link: [not charged for expiration](../facts/s3.md#s3-lifecycle-expired-object-not-charged)
  say: not charged for expiration
s3-lifecycle-extra-actions-mpu-delete-markers
  claim: Besides transition and expiration, Lifecycle actions can stop incomplete multipart uploads and remove expired object delete markers.
  scope: per Lifecycle configuration.
  link: [stop incomplete multipart uploads](../facts/s3.md#s3-lifecycle-extra-actions-mpu-delete-markers)
  link: [remove expired object delete markers](../facts/s3.md#s3-lifecycle-extra-actions-mpu-delete-markers)
s3-lifecycle-filter-prefix-tags-and
  claim: A Lifecycle rule can filter objects by key prefix, object tags or both; combined filters use a logical AND, and one filter can have only one prefix and zero or more tags.
  scope: per Lifecycle rule.
  link: [key prefix, object tags, or a combination](../facts/s3.md#s3-lifecycle-filter-prefix-tags-and)
  link: [only one prefix, and zero or more tags](../facts/s3.md#s3-lifecycle-filter-prefix-tags-and)
s3-lifecycle-glacier-overhead-40-kb-per-object
  claim: Each object archived to S3 Glacier Flexible Retrieval or Deep Archive carries 8 KB of metadata billed at S3 Standard rates plus 32 KB of index metadata billed at the Glacier class rate, so archiving many small objects adds overhead; AWS suggests aggregating small objects first.
  scope: per object archived to S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive; fixed.
  link: [8 KB of storage for the name of the object and other metadata](../facts/s3.md#s3-lifecycle-glacier-overhead-40-kb-per-object)
  link: [32 KB of storage for index and related metadata](../facts/s3.md#s3-lifecycle-glacier-overhead-40-kb-per-object)
  link: [aggregating many small objects into a smaller number](../facts/s3.md#s3-lifecycle-glacier-overhead-40-kb-per-object)
  say: eight kilobytes | thirty-two kilobytes
s3-lifecycle-no-single-rule-before-minimum-duration
  claim: One lifecycle rule cannot transition an object out of a storage class before that class's minimum storage duration has passed; for example, after a transition to S3 Glacier Instant Retrieval (90-day minimum) at day 4, the Deep Archive step must be at day 94 or later. Two separate rules can do it, but you pay the minimum-duration charge.
  scope: per Lifecycle rule; minimum; storage classes with a minimum storage duration.
  link: [can't create a single Lifecycle rule](../facts/s3.md#s3-lifecycle-no-single-rule-before-minimum-duration)
  link: [at least 94 days](../facts/s3.md#s3-lifecycle-no-single-rule-before-minimum-duration)
  say: at least ninety-four days
s3-lifecycle-no-transition-out-of-archive
  claim: A Lifecycle rule cannot move an object from S3 Glacier Deep Archive to any other class, and from S3 Glacier Flexible Retrieval only to Deep Archive. To change an archived object's class otherwise, restore a temporary copy first and then copy the object with the new storage class.
  scope: per archived object.
  link: [can go only one way](../facts/s3.md#s3-lifecycle-no-transition-out-of-archive)
  link: [transitioned to the S3 Glacier Deep Archive](../facts/s3.md#s3-lifecycle-no-transition-out-of-archive)
  link: [make a temporary copy of the object first](../facts/s3.md#s3-lifecycle-no-transition-out-of-archive)
s3-lifecycle-noncurrent-version-expiration
  claim: The NoncurrentVersionExpiration action permanently deletes noncurrent object versions, which cannot be recovered; it can be based on the number of days since the versions became noncurrent.
  scope: per versioning-enabled bucket.
  link: [permanently delete noncurrent versions of objects](../facts/s3.md#s3-lifecycle-noncurrent-version-expiration)
  link: [These deleted objects can't be recovered](../facts/s3.md#s3-lifecycle-noncurrent-version-expiration)
s3-lifecycle-noncurrent-versions-retain-1-100
  claim: With NoncurrentVersionExpiration you can, besides a number of days, set a maximum number of noncurrent versions to retain, between 1 and 100; this needs a Filter element in the rule.
  scope: per Lifecycle rule, versioned bucket; maximum; not adjustable; the rule must have a Filter element.
  link: [between 1 and 100](../facts/s3.md#s3-lifecycle-noncurrent-versions-retain-1-100)
  say: between one and one hundred
s3-lifecycle-one-action-per-day
  claim: An object is eligible for only one S3 Lifecycle action per day; when multiple rules match, S3 applies the least costly action.
  scope: per object, per day; maximum; multiple matching rules.
  link: [only one S3 Lifecycle action per day](../facts/s3.md#s3-lifecycle-one-action-per-day)
  link: [applies the least costly action](../facts/s3.md#s3-lifecycle-one-action-per-day)
  say: only one S3 Lifecycle action per day | applies the least costly action
s3-lifecycle-remove-expired-delete-markers
  claim: The Lifecycle Expiration action can also remove expired object delete markers (delete markers with no remaining object versions).
  scope: per versioning-enabled bucket.
  link: [remove any expired object delete markers](../facts/s3.md#s3-lifecycle-remove-expired-delete-markers)
s3-lifecycle-rule-change-propagation-15-min
  claim: Lifecycle rule changes can take up to 15 minutes to propagate; tag updates take effect faster, so removing the triggering tag is how you stop a pending tag-based expiration.
  scope: per Lifecycle configuration; maximum.
  link: [up to 15 minutes to propagate](../facts/s3.md#s3-lifecycle-rule-change-propagation-15-min)
  say: up to fifteen minutes to propagate
s3-lifecycle-rule-status-filter
  claim: Each Lifecycle rule has a rule ID and a status (enabled or disabled); S3 performs no action of a disabled rule.
  scope: per Lifecycle rule.
  link: [doesn't perform any actions specified in the rule](../facts/s3.md#s3-lifecycle-rule-status-filter)
s3-lifecycle-rules-max
  claim: A Lifecycle configuration can hold at most 1,000 rules.
  scope: per Lifecycle configuration; maximum; not adjustable.
  link: [1,000](../facts/s3.md#s3-lifecycle-rules-max)
  say: one thousand
s3-lifecycle-small-object-default
  claim: Since September 2024 a Lifecycle configuration by default does not transition objects smaller than 128 KB to any storage class, because each transition is a billed request; an object size filter in the rule allows them. Before September 2024 such objects could by default transition only to S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive, and configurations created before September 2024 keep that previous behavior unless you modify them.
  scope: per Lifecycle configuration; default; adjustable; an ObjectSizeGreaterThan or ObjectSizeLessThan filter changes it; configurations created before September 2024 keep the previous behavior until modified.
  link: [128 KB](../facts/s3.md#s3-lifecycle-small-object-default)
  link: [prevents objects smaller than 128 KB from being transitioned](../facts/s3.md#s3-lifecycle-small-object-default)
  link: [add an object size filter](../facts/s3.md#s3-lifecycle-small-object-default)
  link: [charged a transition request for each object](../facts/s3.md#s3-lifecycle-small-object-default)
  say: one hundred twenty-eight kilobytes | objects under one twenty-eight kilobytes are not transitioned
  changed: 2024-09: was allowed objects smaller than 128 KB to be transitioned only to the S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive storage classes
s3-lifecycle-transition-and-expiration-actions
  claim: An S3 Lifecycle configuration is a set of rules that define actions S3 applies to a group of objects; it can transition objects to less expensive storage classes, archive them or delete them.
  scope: per Lifecycle configuration.
  link: [a set of rules that define actions](../facts/s3.md#s3-lifecycle-transition-and-expiration-actions)
  link: [transition objects to less expensive storage classes](../facts/s3.md#s3-lifecycle-transition-and-expiration-actions)
s3-lifecycle-transition-to-intelligent-tiering-for-unknown-patterns
  claim: A lifecycle rule can transition objects into S3 Intelligent-Tiering; AWS suggests this when you do not know the access pattern or it changes over time.
  scope: S3 Lifecycle configuration; unknown or changing access patterns.
  link: [transition the objects to the S3 Intelligent-Tiering](../facts/s3.md#s3-lifecycle-transition-to-intelligent-tiering-for-unknown-patterns)
s3-lifecycle-transition-waterfall
  claim: Lifecycle transitions follow a waterfall: S3 Standard can move to Standard-IA, Intelligent-Tiering, One Zone-IA, Glacier Instant Retrieval, Glacier Flexible Retrieval or Glacier Deep Archive; One Zone-IA only to Glacier Flexible Retrieval or Deep Archive; Glacier Flexible Retrieval only to Deep Archive.
  scope: per Lifecycle transition rule.
  link: [a waterfall model for transitioning between storage classes](../facts/s3.md#s3-lifecycle-transition-waterfall)
  link: [S3 Standard storage class to the S3 Standard-IA](../facts/s3.md#s3-lifecycle-transition-waterfall)
s3-lifecycle-transitions-table
  claim: The S3 storage classes comparison table marks Lifecycle transitions as Yes for S3 Standard, S3 Intelligent-Tiering, S3 Standard-IA, S3 One Zone-IA, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive, and as No for S3 Express One Zone.
  scope: storage classes in the S3 storage classes comparison table.
  link: [Lifecycle transitions](../facts/s3.md#s3-lifecycle-transitions-table)
  say: Lifecycle transitions
s3-listbuckets-paginated-above-10000
  claim: Accounts with an approved general purpose bucket quota above 10,000 must send paginated ListBuckets requests; unpaginated ListBuckets requests are rejected for them.
  scope: per AWS account; approved general purpose bucket quota above 10,000.
  link: [greater than 10,000](../facts/s3.md#s3-listbuckets-paginated-above-10000)
  say: greater than ten thousand
s3-macie-sensitive-data-finding
  claim: Amazon Macie discovers sensitive data in S3 with machine learning and pattern matching; when it detects sensitive data in an S3 object, it generates a security finding.
  scope: Amazon Macie on S3.
  link: [machine learning and pattern matching](../facts/s3.md#s3-macie-sensitive-data-finding)
s3-mfa-delete-not-with-lifecycle
  claim: MFA delete cannot be used with Lifecycle configurations.
  scope: per bucket with MFA delete.
  link: [You cannot use MFA delete with lifecycle configurations](../facts/s3.md#s3-mfa-delete-not-with-lifecycle)
s3-mfa-delete-protected-operations
  claim: With MFA delete enabled, the bucket owner must include two forms of authentication to permanently delete an object version or to change the versioning state of the bucket.
  scope: per bucket with MFA delete.
  link: [delete a version or change the versioning state](../facts/s3.md#s3-mfa-delete-protected-operations)
  link: [two forms of authentication](../facts/s3.md#s3-mfa-delete-protected-operations)
s3-mfa-delete-root-only-cli-api
  claim: Only the bucket owner (the root account) can enable MFA delete, and it cannot be enabled in the AWS Management Console: you must use the AWS CLI or the API.
  scope: per bucket.
  link: [only the bucket owner (root account)](../facts/s3.md#s3-mfa-delete-root-only-cli-api)
  link: [You must use the AWS Command Line Interface](../facts/s3.md#s3-mfa-delete-root-only-cli-api)
s3-min-duration-charge-table
  claim: Minimum storage duration charges are N/A for S3 Standard and S3 Intelligent-Tiering, 1 hour for S3 Express One Zone, 30 days for S3 Standard-IA and S3 One Zone-IA, 90 days for S3 Glacier Instant Retrieval and S3 Glacier Flexible Retrieval, and 180 days for S3 Glacier Deep Archive.
  scope: per object, per storage class; minimum.
  link: [1 hour](../facts/s3.md#s3-min-duration-charge-table)
  link: [30 days](../facts/s3.md#s3-min-duration-charge-table)
  link: [90 days](../facts/s3.md#s3-min-duration-charge-table)
  link: [180 days](../facts/s3.md#s3-min-duration-charge-table)
  say: one hour | thirty days | ninety days | one hundred eighty days
s3-mountpoint-file-client-limits
  claim: Mountpoint for Amazon S3 is an open source file client that mounts an S3 bucket on a compute instance as a local file system. It does not support modifying existing files or deleting existing directories, and it is not suitable for applications that need collaboration and coordination across multiple compute instances or users.
  scope: Mountpoint for Amazon S3.
  link: [open source file client](../facts/s3.md#s3-mountpoint-file-client-limits)
  link: [does not support modifying existing files](../facts/s3.md#s3-mountpoint-file-client-limits)
  say: an open source file client | no edits of existing files
s3-mpu-max-parts
  claim: A multipart upload has at most 10,000 parts.
  scope: per multipart upload; maximum; not adjustable.
  link: [10,000 parts](../facts/s3.md#s3-mpu-max-parts)
  say: ten thousand parts
s3-mpu-no-expiry
  claim: A started multipart upload has no expiry: you must explicitly complete or stop it, and its parts can be uploaded independently, in any order, and in parallel.
  scope: per multipart upload.
  link: [no expiry](../facts/s3.md#s3-mpu-no-expiry)
  say: no expiry
s3-mpu-object-size-range
  claim: Multipart upload works for objects from 5 MB to 50 TB in size.
  scope: per object uploaded with multipart upload; maximum; not adjustable.
  link: [5 MB to 50 TB](../facts/s3.md#s3-mpu-object-size-range)
  say: five megabytes to fifty terabytes
s3-mpu-part-numbers
  claim: Multipart upload part numbers run from 1 to 10,000 (inclusive).
  scope: per multipart upload; fixed; not adjustable.
  link: [1 to 10,000](../facts/s3.md#s3-mpu-part-numbers)
  say: one to ten thousand
s3-mpu-part-size
  claim: Each part of a multipart upload is 5 MiB to 5 GiB; there is no minimum size for the last part.
  scope: per part of a multipart upload; maximum; not adjustable; the last part has no minimum size.
  link: [5 MiB to 5 GiB](../facts/s3.md#s3-mpu-part-size)
  link: [5 MiB](../facts/s3.md#s3-mpu-part-size)
  link: [5 GiB](../facts/s3.md#s3-mpu-part-size)
  say: five mebibytes to five gibibytes | five mebibytes | five gibibytes
s3-mpu-recommended-threshold
  claim: AWS calls multipart upload a best practice for objects of 100 MB or larger, instead of a single-operation upload.
  scope: per object; recommendation, not a limit.
  link: [100 MB](../facts/s3.md#s3-mpu-recommended-threshold)
  say: one hundred megabytes
s3-mrap-per-account-quota
  claim: An account can have 100 Multi-Region Access Points; this quota is not adjustable.
  scope: per account; maximum; not adjustable.
  link: [100](../facts/s3.md#s3-mrap-per-account-quota)
  say: one hundred
s3-mrap-regions-max
  claim: A Multi-Region Access Point can span at most 20 Regions.
  scope: per Multi-Region Access Point; maximum; not adjustable.
  link: [20](../facts/s3.md#s3-mrap-regions-max)
  say: twenty
s3-multi-region-access-point-lowest-latency-copy
  claim: S3 Multi-Region Access Points, built on AWS Global Accelerator, route each request over the AWS network to the lowest-latency copy of data that is replicated across several Regions, and can speed access by up to 60%.
  scope: per Multi-Region Access Point; maximum; data sets replicated across multiple AWS Regions.
  link: [the lowest latency copy of your data](../facts/s3.md#s3-multi-region-access-point-lowest-latency-copy)
  link: [up to 60%](../facts/s3.md#s3-multi-region-access-point-lowest-latency-copy)
  say: up to sixty percent
s3-multi-region-access-point-routing-cost
  claim: A Multi-Region Access Point adds a data routing cost per GB processed on top of the normal S3 request, storage, data transfer and replication charges.
  scope: per GB routed through the Multi-Region Access Point; requests routed within AWS; internet acceleration is an extra charge.
  link: [data routing cost for each gigabyte (GB) processed](../facts/s3.md#s3-multi-region-access-point-routing-cost)
s3-multipart-anonymous-cannot-initiate
  claim: Starting a multipart upload returns an upload ID that every later part upload, list, complete or stop request must carry; anonymous users cannot initiate multipart uploads.
  scope: per multipart upload.
  link: [anonymous users cannot initiate multipart uploads](../facts/s3.md#s3-multipart-anonymous-cannot-initiate)
  link: [this upload ID is required](../facts/s3.md#s3-multipart-anonymous-cannot-initiate)
s3-multipart-upload-incomplete-parts-billed
  claim: After you start a multipart upload and upload parts, you pay for storage of those parts until you complete or stop the upload; only then does S3 free the parts and stop billing.
  scope: per multipart upload.
  link: [must either complete or stop the multipart upload](../facts/s3.md#s3-multipart-upload-incomplete-parts-billed)
s3-multipart-upload-parallel-parts-throughput
  claim: With multipart upload you upload parts in parallel to improve throughput, and a failed part is retransmitted without affecting the other parts.
  scope: per multipart upload.
  link: [upload parts in parallel to improve throughput](../facts/s3.md#s3-multipart-upload-parallel-parts-throughput)
  link: [retransmit that part without affecting other parts](../facts/s3.md#s3-multipart-upload-parallel-parts-throughput)
s3-multipart-upload-parts-parallel
  claim: Multipart upload uploads one object as a set of parts that can be sent independently and in any order; a failed part is retransmitted without affecting the others, and S3 assembles the object when all parts are uploaded. AWS calls it a best practice for objects of 100 MB or larger.
  scope: per object upload.
  link: [as a set of parts](../facts/s3.md#s3-multipart-upload-parts-parallel)
  link: [retransmit that part without affecting other parts](../facts/s3.md#s3-multipart-upload-parts-parallel)
  link: [100 MB or larger](../facts/s3.md#s3-multipart-upload-parts-parallel)
s3-object-definition-identifier-metadata
  claim: Object storage stores and manages data in an unstructured format called objects; each object is tagged with a unique identifier and contains metadata that describes the underlying content.
  scope: object storage.
  link: [tagged with a unique identifier](../facts/s3.md#s3-object-definition-identifier-metadata)
s3-object-key-unique-in-bucket
  claim: Each object has a key (or key name), which is the unique identifier for the object within its bucket.
  scope: per bucket.
  link: [unique identifier for the object within the bucket](../facts/s3.md#s3-object-key-unique-in-bucket)
  link: [key name](../facts/s3.md#s3-object-key-unique-in-bucket)
s3-object-lambda-alternatives
  claim: Alternatives to S3 Object Lambda include the AWS Solution Dynamic Image Transformation for Amazon CloudFront, invoking AWS Lambda by other means (through CloudFront, API Gateway or function URLs), or processing data in the client application; all of them keep S3 as the storage, so no data migration is needed.
  scope: replacing S3 Object Lambda.
  link: [invoking AWS Lambda by other means](../facts/s3.md#s3-object-lambda-alternatives)
  say: call Lambda through CloudFront, API Gateway or a function URL
s3-object-lock-bucket-default-retention
  claim: A bucket default retention sets a duration in days or years for every object version placed in the bucket afterwards; S3 computes the Retain Until Date by adding that duration to the version's creation time. An explicit retention set on an object version overrides the bucket default.
  scope: per bucket; default; applies to object versions placed in the bucket.
  link: [how long to protect every object version](../facts/s3.md#s3-object-lock-bucket-default-retention)
  link: [adding the specified duration](../facts/s3.md#s3-object-lock-bucket-default-retention)
  link: [individual Object Lock settings override any bucket property](../facts/s3.md#s3-object-lock-bucket-default-retention)
s3-object-lock-compliance-mode
  claim: In compliance mode, a protected object version cannot be overwritten or deleted by any user, including the root user; its retention mode cannot be changed and its retention period cannot be shortened. The only way to delete such an object before its retention date is to delete the AWS account.
  scope: per object version in compliance mode.
  link: [can't be overwritten or deleted by any user](../facts/s3.md#s3-object-lock-compliance-mode)
  link: [its retention period can't be shortened](../facts/s3.md#s3-object-lock-compliance-mode)
  link: [delete the associated AWS account](../facts/s3.md#s3-object-lock-compliance-mode)
s3-object-lock-delete-behavior
  claim: On a locked object, a permanent DELETE that names a version ID returns Access Denied (403 Forbidden), while a simple DELETE without a version ID returns 200 OK and adds a delete marker that becomes the current version. Delete markers are not WORM-protected.
  scope: per protected object version.
  link: [Access Denied (403 Forbidden)](../facts/s3.md#s3-object-lock-delete-behavior)
  link: [inserts a delete marker in the bucket](../facts/s3.md#s3-object-lock-delete-behavior)
  link: [delete markers are not WORM-protected](../facts/s3.md#s3-object-lock-delete-behavior)
s3-object-lock-enable-existing-bucket
  claim: You can enable Object Lock for an existing S3 bucket with the console, the AWS CLI, the AWS SDKs or the REST API; Object Lock works only with versioned buckets.
  scope: general purpose buckets; versioning enabled.
  link: [enable Object Lock for an existing S3 bucket](../facts/s3.md#s3-object-lock-enable-existing-bucket)
  link: [Object Lock works only with versioned buckets](../facts/s3.md#s3-object-lock-enable-existing-bucket)
  say: Object Lock can be added to an existing bucket | the bucket must be versioned
s3-object-lock-governance-mode
  claim: In governance mode, users cannot overwrite or delete a locked object version or change its lock settings unless they have special permission. To override governance retention a user needs s3:BypassGovernanceRetention and must send the x-amz-bypass-governance-retention:true header.
  scope: per object version in governance mode; the user holds s3:BypassGovernanceRetention.
  link: [unless they have special permissions](../facts/s3.md#s3-object-lock-governance-mode)
  link: [s3:BypassGovernanceRetention](../facts/s3.md#s3-object-lock-governance-mode)
  link: [x-amz-bypass-governance-retention:true](../facts/s3.md#s3-object-lock-governance-mode)
s3-object-lock-legal-hold-independent
  claim: A legal hold is independent of the retention period: if the retention period expires, the legal hold keeps protecting the object until an authorized user removes it, and if the hold is removed, the retention period still protects the version until it expires. Any user with the s3:PutObjectLegalHold permission can place or remove a legal hold.
  scope: per object version.
  link: [the legal hold continues to protect the object](../facts/s3.md#s3-object-lock-legal-hold-independent)
  link: [s3:PutObjectLegalHold](../facts/s3.md#s3-object-lock-legal-hold-independent)
s3-object-lock-lifecycle-cannot-expire-locked
  claim: Lifecycle rules keep working on protected objects, including placing delete markers, but a Lifecycle expiration cannot delete a locked object version. Object Lock is kept in every storage class and across Lifecycle transitions.
  scope: per locked object version.
  link: [locked version of an object cannot be deleted](../facts/s3.md#s3-object-lock-lifecycle-cannot-expire-locked)
  link: [maintained regardless of which storage class](../facts/s3.md#s3-object-lock-lifecycle-cannot-expire-locked)
s3-object-lock-mode-choice
  claim: AWS says to use governance mode when most users must not delete objects but some privileged users may alter retention or delete, and compliance mode when no user, including the root user, may ever delete objects during the retention period.
  scope: Object Lock mode choice.
  link: [some users with special permissions](../facts/s3.md#s3-object-lock-mode-choice)
  link: [never want any user, including the root user](../facts/s3.md#s3-object-lock-mode-choice)
s3-object-lock-not-key-loss
  claim: Object Lock does not protect against losing or deleting encryption keys: if objects are encrypted with SSE-KMS and the KMS key is deleted, the objects may become unreadable.
  scope: per bucket.
  link: [does not protect against losing access](../facts/s3.md#s3-object-lock-not-key-loss)
  link: [your objects may become unreadable](../facts/s3.md#s3-object-lock-not-key-loss)
s3-object-lock-replication-destination
  claim: Object Lock works with S3 Replication: locked objects and their retention metadata are copied, and if the source bucket has Object Lock enabled, the destination buckets must also have Object Lock enabled.
  scope: per replication rule; source bucket has Object Lock enabled.
  link: [must also have Object Lock enabled](../facts/s3.md#s3-object-lock-replication-destination)
  link: [copying of locked objects and their retention metadata](../facts/s3.md#s3-object-lock-replication-destination)
s3-object-lock-requires-versioning
  claim: Object Lock works only in buckets with S3 Versioning enabled, and a retention period or legal hold protects only the object version named in the request. Locks do not stop new versions or delete markers from being added on top of the object.
  scope: per bucket.
  link: [buckets that have S3 Versioning enabled](../facts/s3.md#s3-object-lock-requires-versioning)
  link: [protects only the version that's specified](../facts/s3.md#s3-object-lock-requires-versioning)
  link: [don't prevent new versions of the object](../facts/s3.md#s3-object-lock-requires-versioning)
s3-object-lock-retention-extend-only
  claim: A retention period can be extended by submitting a new Object Lock request with a later Retain Until Date; S3 replaces the period with the longer one. Setting a retention period needs the s3:PutObjectRetention permission.
  scope: per object version.
  link: [you can extend the retention period](../facts/s3.md#s3-object-lock-retention-extend-only)
  link: [s3:PutObjectRetention](../facts/s3.md#s3-object-lock-retention-extend-only)
s3-object-lock-retention-limits-bucket-policy
  claim: A bucket policy can restrict the minimum and maximum allowed Object Lock retention periods with the s3:object-lock-remaining-retention-days condition key.
  scope: bucket policy on an Object Lock bucket.
  link: [s3:object-lock-remaining-retention-days](../facts/s3.md#s3-object-lock-retention-limits-bucket-policy)
s3-object-lock-retention-per-object-or-bucket-default
  claim: An Object Lock retention period can be set uniquely for individual objects, and a default retention period can also be set on the bucket.
  scope: S3 Object Lock retention periods; bucket has Object Lock enabled.
  link: [a unique retention period for individual objects](../facts/s3.md#s3-object-lock-retention-per-object-or-bucket-default)
  link: [a default retention period on an S3 bucket](../facts/s3.md#s3-object-lock-retention-per-object-or-bucket-default)
s3-object-lock-retention-vs-legal-hold
  claim: Object Lock has two retention tools: a retention period locks an object version for a fixed period, and a legal hold gives the same protection with no expiration date and stays until you remove it. An object version can have a retention period, a legal hold, or both.
  scope: per object version.
  link: [a retention period, a legal hold, or both](../facts/s3.md#s3-object-lock-retention-vs-legal-hold)
  link: [it has no expiration date](../facts/s3.md#s3-object-lock-retention-vs-legal-hold)
  link: [a fixed period of time](../facts/s3.md#s3-object-lock-retention-vs-legal-hold)
s3-object-lock-worm-definition
  claim: S3 Object Lock can help prevent objects from being deleted or overwritten for a fixed or variable amount of time, or indefinitely, using a write-once-read-many (WORM) model; it can help meet regulatory requirements that require WORM storage.
  scope: per object version.
  link: [a fixed or variable amount of time](../facts/s3.md#s3-object-lock-worm-definition)
  link: [write-once-read-many (WORM) model](../facts/s3.md#s3-object-lock-worm-definition)
  link: [WORM storage](../facts/s3.md#s3-object-lock-worm-definition)
s3-object-lock-worm-prevents-deletion
  claim: S3 Object Lock stores objects in a write-once-read-many (WORM) model and helps prevent accidental or inappropriate deletion, for example of CloudTrail logs.
  scope: per bucket with Object Lock enabled.
  link: ["Write Once Read Many" (WORM) model](../facts/s3.md#s3-object-lock-worm-prevents-deletion)
  link: [help prevent accidental or inappropriate deletion of data](../facts/s3.md#s3-object-lock-worm-prevents-deletion)
s3-object-max-size
  claim: A single S3 object can be up to 50 TB in size. Until December 2, 2025 the maximum was 5 TB.
  scope: per object; maximum; not adjustable.
  link: [50 TB](../facts/s3.md#s3-object-max-size)
  link: [5 TB](../facts/s3.md#s3-object-max-size)
  say: fifty terabytes | five terabytes
  changed: 2025-12-02: was 5 TB
s3-object-max-size-exact
  claim: The exact maximum object size is 53.7 TB (48.8 TiB), set by the multipart limits of 10,000 parts of 5 GiB each; AWS documentation commonly rounds this to 50 TB.
  scope: per object; maximum; not adjustable; 10,000 parts of 5 GiB.
  link: [53.7 TB](../facts/s3.md#s3-object-max-size-exact)
  link: [48.8 TiB](../facts/s3.md#s3-object-max-size-exact)
  say: fifty-three point seven terabytes | forty-eight point eight tebibytes
s3-object-ownership-default-bucket-owner-enforced
  claim: S3 Object Ownership is a bucket-level setting. By default it is set to Bucket owner enforced and all ACLs are disabled; the bucket owner then owns every object in the bucket and manages access only with policies.
  scope: per general purpose bucket; default; adjustable.
  link: [Bucket owner enforced](../facts/s3.md#s3-object-ownership-default-bucket-owner-enforced)
  link: [all ACLs are disabled](../facts/s3.md#s3-object-ownership-default-bucket-owner-enforced)
  link: [the bucket owner owns all the objects](../facts/s3.md#s3-object-ownership-default-bucket-owner-enforced)
s3-object-ownership-disable-acls-existing-bucket
  claim: ACLs can be disabled on new and existing buckets. On an existing bucket with objects, after ACLs are disabled the bucket and object ACLs no longer take part in access evaluation and access is decided by policies; ACLs can be re-enabled later and the earlier ACLs come back.
  scope: per general purpose bucket.
  link: [no longer part of an access evaluation](../facts/s3.md#s3-object-ownership-disable-acls-existing-bucket)
  link: [your preexisting bucket and object ACLs are restored](../facts/s3.md#s3-object-ownership-disable-acls-existing-bucket)
s3-object-ownership-put-with-other-acl-fails
  claim: With ACLs disabled, a bucket accepts only PUT requests that specify no ACL or the bucket-owner-full-control ACL; a PUT with any other ACL fails with a 400 error and the code AccessControlListNotSupported.
  scope: per general purpose bucket; Object Ownership set to Bucket owner enforced.
  link: [PUT requests that do not specify an ACL](../facts/s3.md#s3-object-ownership-put-with-other-acl-fails)
  link: [fail and return a 400 error with the error code AccessControlListNotSupported](../facts/s3.md#s3-object-ownership-put-with-other-acl-fails)
s3-object-ownership-three-settings
  claim: Object Ownership has three settings: Bucket owner enforced (ACLs disabled, bucket owner owns every object), Bucket owner preferred (bucket owner owns new objects written with the bucket-owner-full-control canned ACL), and Object writer (the uploading account owns the object and can grant access with ACLs).
  scope: per general purpose bucket.
  link: [Bucket owner enforced (default)](../facts/s3.md#s3-object-ownership-three-settings)
  link: [Bucket owner preferred](../facts/s3.md#s3-object-ownership-three-settings)
  link: [Object writer](../facts/s3.md#s3-object-ownership-three-settings)
  link: [bucket-owner-full-control](../facts/s3.md#s3-object-ownership-three-settings)
s3-object-parts
  claim: Objects consist of object data and metadata. The metadata is a set of name-value pairs, including default system metadata such as the last-modified date, standard HTTP metadata such as Content-Type, and custom metadata you set when the object is stored.
  scope: Amazon S3 objects.
  link: [object data and metadata](../facts/s3.md#s3-object-parts)
  link: [a set of name-value pairs](../facts/s3.md#s3-object-parts)
s3-object-storage-api-read-heavy
  claim: Object storage (Amazon S3) is accessed through an API over the internet and suits read-heavy workloads such as streaming applications and services.
  scope: object storage, compared with block and file storage.
  link: [an application programming interface (API) over the internet](../facts/s3.md#s3-object-storage-api-read-heavy)
  link: [read-heavy workloads](../facts/s3.md#s3-object-storage-api-read-heavy)
s3-object-storage-definition
  claim: Amazon S3 is an object storage service that stores data as objects within buckets. An object is a file plus any metadata that describes the file, and a bucket is a container for objects.
  scope: Amazon S3.
  link: [object storage service](../facts/s3.md#s3-object-storage-definition)
  link: [a file and any metadata](../facts/s3.md#s3-object-storage-definition)
  link: [a bucket is a container for objects](../facts/s3.md#s3-object-storage-definition)
  say: an object storage service
s3-object-tags-max
  claim: An object can carry at most 10 tags.
  scope: per object; maximum; not adjustable.
  link: [10](../facts/s3.md#s3-object-tags-max)
  say: ten
s3-object-tags-uses
  claim: Object tags are key-value pairs on objects that can be added, changed or removed at any time. They can drive IAM policies, Lifecycle rules (transitions and expiration) and storage metrics.
  scope: per object.
  link: [key-value pairs applied to S3 objects](../facts/s3.md#s3-object-tags-uses)
  link: [set up Amazon S3 Lifecycle policies](../facts/s3.md#s3-object-tags-uses)
s3-object-writer-owns-object-when-acls-enabled
  claim: With the Object Ownership setting Object writer, the AWS account that uploads an object owns the object, has full control over it and can grant other users access to it through ACLs: when another account uploads an object to your general purpose bucket, that account (the object writer) owns the object. Object Ownership can be set so that ACLs are disabled and you, as the bucket owner, automatically own every object in the bucket.
  scope: per general purpose bucket; Object Ownership set to Object writer.
  link: [that account (the object writer) owns the object](../facts/s3.md#s3-object-writer-owns-object-when-acls-enabled)
  link: [automatically own every object](../facts/s3.md#s3-object-writer-owns-object-when-acls-enabled)
s3-objects-stay-in-region
  claim: Objects stored in an AWS Region never leave that Region unless you explicitly transfer or replicate them to another Region.
  scope: per Region; unless you explicitly transfer or replicate the objects.
  link: [never leave the Region unless you explicitly transfer](../facts/s3.md#s3-objects-stay-in-region)
  link: [never leave the Region](../facts/s3.md#s3-objects-stay-in-region)
s3-one-zone-ia-az-loss
  claim: S3 One Zone-IA stores data in only one Availability Zone, is as durable as S3 Standard-IA but less available, and is not resilient to the physical loss of that Availability Zone; use it for data you can re-create, such as CRR replicas.
  scope: S3 One Zone-IA storage class.
  link: [not resilient to the physical loss](../facts/s3.md#s3-one-zone-ia-az-loss)
  link: [re-create the data if the Availability Zone fails](../facts/s3.md#s3-one-zone-ia-az-loss)
  link: [for object replicas when configuring S3 Cross-Region Replication](../facts/s3.md#s3-one-zone-ia-az-loss)
  say: not resilient to the loss of its Availability Zone | data you can re-create
s3-one-zone-ia-single-az-20-percent-cheaper
  claim: S3 One Zone-IA stores data in a single Availability Zone, unlike the other classes that use a minimum of three, and costs 20% less than S3 Standard-IA.
  scope: S3 One Zone-IA, storage price compared with S3 Standard-IA.
  link: [20% less than S3 Standard-IA](../facts/s3.md#s3-one-zone-ia-single-az-20-percent-cheaper)
  link: [stores data in a single AZ](../facts/s3.md#s3-one-zone-ia-single-az-20-percent-cheaper)
  say: twenty percent less than S3 Standard-IA
s3-performance-retries-consistent-latency
  claim: Aggressive timeouts and retries help drive consistent S3 latency: if the first request is slow, a retried request is likely to take a different path and quickly succeed.
  scope: latency-sensitive applications on S3.
  link: [Aggressive timeouts and retries](../facts/s3.md#s3-performance-retries-consistent-latency)
s3-performance-same-region-ec2
  claim: AWS recommends accessing a bucket from Amazon EC2 instances in the same AWS Region when possible, which reduces network latency and data transfer costs.
  scope: EC2 access to S3; when possible.
  link: [in the same AWS Region](../facts/s3.md#s3-performance-same-region-ec2)
  link: [reduce network latency and data transfer costs](../facts/s3.md#s3-performance-same-region-ec2)
s3-performance-scale-connections-horizontally
  claim: AWS says the best S3 performance comes from issuing multiple concurrent requests spread over separate connections, to maximize the bandwidth available from S3; S3 has no limit on the number of connections made to a bucket.
  scope: per bucket, Amazon S3 performance guidelines.
  link: [multiple concurrent requests](../facts/s3.md#s3-performance-scale-connections-horizontally)
  link: [Amazon S3 doesn't have any limits](../facts/s3.md#s3-performance-scale-connections-horizontally)
s3-permission-delegation-no-second-cross-account-hop
  claim: An account that owns an S3 resource can grant permissions to another AWS account, which can then delegate them (or a subset) to its own users; but an account that received permissions from another account cannot delegate them cross-account to a further AWS account.
  scope: S3 permission delegation.
  link: [can't delegate permission cross-account to another AWS account](../facts/s3.md#s3-permission-delegation-no-second-cross-account-hop)
s3-policy-implicit-deny-explicit-deny
  claim: In an S3 policy, access that is not explicitly allowed is implicitly denied, and an explicit Deny blocks access even if another policy grants it.
  scope: per request.
  link: [access is implicitly denied](../facts/s3.md#s3-policy-implicit-deny-explicit-deny)
  link: [even if a different policy grants access](../facts/s3.md#s3-policy-implicit-deny-explicit-deny)
s3-policy-resource-arn-forms
  claim: A policy names the bucket ARN arn:aws:s3:::bucket_name for bucket-level operations, and arn:aws:s3:::bucket_name/* (or bucket_name/prefix/*) for object-level operations. The s3:ListBucket permission allows the ListObjectsV2 operation.
  scope: per policy statement.
  link: [for all objects in the bucket](../facts/s3.md#s3-policy-resource-arn-forms)
  link: [the Amazon S3 ListObjectsV2 operation](../facts/s3.md#s3-policy-resource-arn-forms)
s3-prefix-not-directory
  claim: A prefix is a string at the start of the object key name; prefixes organize data like directories but are not directories.
  scope: general purpose buckets.
  link: [prefixes are not directories](../facts/s3.md#s3-prefix-not-directory)
  link: [a string of characters at the beginning](../facts/s3.md#s3-prefix-not-directory)
s3-prefix-parallel-reads-55000
  claim: AWS's example: spreading reads over 10 prefixes in one bucket can scale read performance to 55,000 read requests per second.
  scope: per bucket, example; reads parallelized across 10 prefixes.
  link: [10 prefixes](../facts/s3.md#s3-prefix-parallel-reads-55000)
  link: [55,000 read requests per second](../facts/s3.md#s3-prefix-parallel-reads-55000)
  say: ten prefixes | fifty-five thousand read requests per second
s3-prefix-request-rate-baseline
  claim: An application can achieve at least 3,500 PUT/COPY/POST/DELETE requests or 5,500 GET/HEAD requests per second per partitioned S3 prefix.
  scope: per partitioned prefix, per bucket; minimum; not adjustable; a baseline AWS says you can achieve at least; S3 scales above it automatically and gradually.
  link: [3,500 PUT/COPY/POST/DELETE](../facts/s3.md#s3-prefix-request-rate-baseline)
  link: [5,500 GET/HEAD requests per second](../facts/s3.md#s3-prefix-request-rate-baseline)
  say: three thousand five hundred PUT, COPY, POST or DELETE | five thousand five hundred GET or HEAD requests per second
s3-prefixes-no-limit
  claim: There is no limit to the number of prefixes in an S3 bucket, so spreading keys over more prefixes raises the total request rate.
  scope: per bucket.
  link: [no limits to the number of prefixes](../facts/s3.md#s3-prefixes-no-limit)
  say: no limits to the number of prefixes
s3-presign-cli-sdk-expiration
  claim: A presigned URL created with the AWS CLI or an SDK can be valid for up to 7 days from the time of creation (Signature Version 4).
  scope: per presigned URL created with the AWS CLI or SDKs; maximum; not adjustable; AWS Signature Version 4; long-lived IAM user credentials.
  link: [7 days](../facts/s3.md#s3-presign-cli-sdk-expiration)
  say: seven days
s3-presign-console-expiration
  claim: A presigned URL created in the S3 console can be valid for between 1 minute and 12 hours from the time of creation.
  scope: per presigned URL created in the S3 console; maximum; not adjustable.
  link: [12 hours](../facts/s3.md#s3-presign-console-expiration)
  link: [1 minute](../facts/s3.md#s3-presign-console-expiration)
  say: twelve hours | one minute
s3-presign-console-object-max
  claim: The S3 console can generate a presigned URL for sharing an object of up to 5 TB.
  scope: per object shared with a console-made presigned URL; maximum; not adjustable.
  link: [5 TB](../facts/s3.md#s3-presign-console-object-max)
  say: five terabytes
s3-presign-ec2-role-duration
  claim: A presigned URL signed with the role credentials of an EC2 instance is valid only for the duration of those role credentials, typically 6 hours.
  scope: per presigned URL; signed with the IAM role credentials of an EC2 instance.
  link: [typically 6 hours](../facts/s3.md#s3-presign-ec2-role-duration)
  say: typically six hours
s3-presigned-url-creator-needs-permission
  claim: Anyone with valid security credentials can create a presigned URL, but the URL only works if its creator has permission to perform the operation the URL is for. A presigned URL is limited by the permissions of the user who created it.
  scope: per presigned URL.
  link: [anyone with valid security credentials](../facts/s3.md#s3-presigned-url-creator-needs-permission)
  link: [limited by the permissions of the user](../facts/s3.md#s3-presigned-url-creator-needs-permission)
  link: [presigned URLs are bearer tokens](../facts/s3.md#s3-presigned-url-creator-needs-permission)
s3-presigned-url-expires-with-temporary-credentials
  claim: A presigned URL made with temporary credentials expires when those credentials expire, even if the URL was given a later expiration time. With an assumed IAM role, the URL expires when the role session ends.
  scope: presigned URLs made with temporary security credentials; temporary credentials (IAM role, EC2 instance role, STS).
  link: [the URL expires when the credential expires](../facts/s3.md#s3-presigned-url-expires-with-temporary-credentials)
  link: [expires when the role session ends](../facts/s3.md#s3-presigned-url-expires-with-temporary-credentials)
  link: [whichever occurs first](../facts/s3.md#s3-presigned-url-expires-with-temporary-credentials)
s3-presigned-url-network-restriction-source-ip-vpce
  claim: To restrict where presigned URLs can be used, write IAM or bucket policies with a network condition: aws:SourceIp for the public S3 endpoint, or aws:SourceVpc / aws:SourceVpce for a VPC endpoint; these restrictions apply to all S3 access, not only presigned URLs.
  scope: IAM principal, bucket, or access point policies.
  link: [aws:SourceIp](../facts/s3.md#s3-presigned-url-network-restriction-source-ip-vpce)
  link: [aws:SourceVpc or aws:SourceVpce](../facts/s3.md#s3-presigned-url-network-restriction-source-ip-vpce)
  link: [also apply outside of the presigned URL scenario](../facts/s3.md#s3-presigned-url-network-restriction-source-ip-vpce)
s3-presigned-url-reusable-until-expiry
  claim: A presigned URL can be used many times until its expiration date and time. S3 checks the expiration at the time of the HTTP request, so a download that started before expiry continues past it.
  scope: per presigned URL.
  link: [multiple times, up to the expiration date](../facts/s3.md#s3-presigned-url-reusable-until-expiry)
  link: [at the time of the HTTP request](../facts/s3.md#s3-presigned-url-reusable-until-expiry)
s3-presigned-url-time-limited-creator-credentials
  claim: A presigned URL grants time-limited access to an object without changing the bucket policy. The URL uses the credentials of the IAM principal who generated it.
  scope: per presigned URL.
  link: [time-limited access to objects in Amazon S3](../facts/s3.md#s3-presigned-url-time-limited-creator-credentials)
  link: [principal who generated the URL](../facts/s3.md#s3-presigned-url-time-limited-creator-credentials)
  link: [time-limited access](../facts/s3.md#s3-presigned-url-time-limited-creator-credentials)
s3-presigned-url-upload-no-credentials-needed
  claim: A presigned URL can let someone upload a specific object to your bucket without having AWS credentials or permissions of their own. If an object with the same key already exists, S3 replaces it with the uploaded object, and after the upload the bucket owner owns the object.
  scope: per presigned URL.
  link: [an upload without requiring another party](../facts/s3.md#s3-presigned-url-upload-no-credentials-needed)
  link: [replaces the existing object with the uploaded object](../facts/s3.md#s3-presigned-url-upload-no-credentials-needed)
  link: [the bucket owner will own the object](../facts/s3.md#s3-presigned-url-upload-no-credentials-needed)
s3-pricing-cost-components
  claim: S3 has no minimum charge; its cost components are storage, requests and data retrieval, data transfer and transfer acceleration, data management and insights features, replication, and transform and query features.
  scope: Amazon S3, all Regions.
  link: [storage pricing, request and data retrieval pricing](../facts/s3.md#s3-pricing-cost-components)
  link: [no minimum charge](../facts/s3.md#s3-pricing-cost-components)
s3-pricing-data-transfer-in-free
  claim: Data transferred into Amazon S3 from the internet is free.
  scope: data transfer into S3; from the internet.
  link: [Data transferred in from the internet](../facts/s3.md#s3-pricing-data-transfer-in-free)
s3-pricing-data-transfer-out-first-100-gb-free
  claim: The first 100GB per month of data transferred out to the internet is free, aggregated across all AWS services and Regions (except China and GovCloud).
  scope: per month, aggregated across all AWS services and Regions; except China and GovCloud.
  link: [first 100GB per month](../facts/s3.md#s3-pricing-data-transfer-out-first-100-gb-free)
  say: the first one hundred gigabytes per month
s3-pricing-data-transfer-same-region-free
  claim: Data transferred from an S3 bucket to any AWS service in the same Region is free, including to a different account in that Region; so is transfer between S3 buckets in the same Region.
  scope: data transfer out of S3; destination in the same AWS Region.
  link: [any AWS service(s) within the same AWS Region](../facts/s3.md#s3-pricing-data-transfer-same-region-free)
  link: [between S3 buckets in the same AWS Region](../facts/s3.md#s3-pricing-data-transfer-same-region-free)
s3-pricing-data-transfer-to-cloudfront-free
  claim: You pay for all bandwidth into and out of Amazon S3 except for some transfers; data transferred out to Amazon CloudFront is one of these exceptions.
  scope: data transfer out of S3; destination is Amazon CloudFront.
  link: [Data transferred out to Amazon CloudFront](../facts/s3.md#s3-pricing-data-transfer-to-cloudfront-free)
s3-pricing-ingest-charge-per-request-on-transition
  claim: There are per-request ingest charges when you use PUT, COPY or lifecycle rules to move data into any S3 storage class; AWS advises you to consider the ingest or transition cost before moving objects into any storage class.
  scope: per request, any storage class; PUT, COPY or lifecycle transition into a storage class.
  link: [per-request ingest charges](../facts/s3.md#s3-pricing-ingest-charge-per-request-on-transition)
  link: [Consider the ingest or transition cost](../facts/s3.md#s3-pricing-ingest-charge-per-request-on-transition)
s3-pricing-intelligent-tiering-monitoring-charge-no-retrieval
  claim: S3 Intelligent-Tiering adds a monthly monitoring and automation charge per object, and has no retrieval charges and no tiering charges when objects move between access tiers.
  scope: S3 Intelligent-Tiering, per object.
  link: [monthly monitoring and automation charge per object](../facts/s3.md#s3-pricing-intelligent-tiering-monitoring-charge-no-retrieval)
  link: [no retrieval charges, and no additional tiering charges](../facts/s3.md#s3-pricing-intelligent-tiering-monitoring-charge-no-retrieval)
s3-pricing-list-requests-charged-delete-free
  claim: LIST requests on any storage class are charged at the S3 Standard PUT, COPY and POST rate; DELETE and CANCEL requests are free.
  scope: per request, all storage classes.
  link: [DELETE and CANCEL requests are free](../facts/s3.md#s3-pricing-list-requests-charged-delete-free)
  link: [LIST requests for any storage class are charged](../facts/s3.md#s3-pricing-list-requests-charged-delete-free)
s3-pricing-restore-pays-archive-plus-temporary-standard-copy
  claim: When you restore an archive from S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive, you pay for both the archive (at its Glacier class rate) and the temporary restored copy, which is charged at the S3 Standard storage rate for a duration of time you choose.
  scope: per restored object, S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive; during the restore window.
  link: [paying for both the archive](../facts/s3.md#s3-pricing-restore-pays-archive-plus-temporary-standard-copy)
  link: [charged at the S3 Standard storage rate](../facts/s3.md#s3-pricing-restore-pays-archive-plus-temporary-standard-copy)
s3-pricing-retrieval-charges-which-classes
  claim: A retrieval charge applies on GET for S3 Standard-IA, S3 One Zone-IA and S3 Glacier Instant Retrieval; for S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive the retrieval is paid as part of the restore request.
  scope: by storage class.
  link: [pay for retrievals when you GET an object](../facts/s3.md#s3-pricing-retrieval-charges-which-classes)
  link: [as a part of the restore request](../facts/s3.md#s3-pricing-retrieval-charges-which-classes)
s3-pricing-storage-rate-size-duration-class
  claim: The storage charge depends on the size of the objects, how long they were stored during the month, and their storage class.
  scope: per object, per month.
  link: [how long you stored the objects](../facts/s3.md#s3-pricing-storage-rate-size-duration-class)
s3-private-by-default
  claim: Buckets and the objects in them are private by default and can be accessed only if you explicitly grant access. Access is managed with bucket policies, IAM policies, ACLs, and S3 Access Points.
  scope: buckets and objects; default; adjustable.
  link: [can be accessed only if you explicitly grant](../facts/s3.md#s3-private-by-default)
  link: [bucket policies, AWS Identity and Access Management](../facts/s3.md#s3-private-by-default)
s3-public-policy-definition
  claim: S3 considers a bucket or object ACL public if it grants any permissions to members of the predefined AllUsers or AuthenticatedUsers groups. When evaluating a bucket policy, S3 begins by assuming that the policy is public, then evaluates the policy to determine whether it qualifies as non-public.
  scope: Block Public Access evaluation.
  link: [the predefined AllUsers or AuthenticatedUsers groups](../facts/s3.md#s3-public-policy-definition)
  link: [begins by assuming that the policy is public](../facts/s3.md#s3-public-policy-definition)
s3-quota-increase-not-immediate
  claim: Only some S3 quotas can be increased, and increases are not granted immediately; one may take a couple of days to become effective.
  scope: per AWS account.
  link: [may take a couple of days](../facts/s3.md#s3-quota-increase-not-immediate)
  say: may take a couple of days
s3-replication-archived-objects-not-replicated
  claim: Objects in S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive or the Intelligent-Tiering Archive Access or Deep Archive Access tiers are not replicated until you restore them and copy them to a different storage class.
  scope: per replication rule.
  link: [until you restore them and copy them](../facts/s3.md#s3-replication-archived-objects-not-replicated)
s3-replication-bucket-config-not-replicated
  claim: Changes to bucket-level settings such as the Lifecycle configuration or a notification configuration on the source bucket are not applied to the destination bucket, so source and destination buckets can have different configurations.
  scope: source and destination buckets.
  link: [not applied to the destination bucket](../facts/s3.md#s3-replication-bucket-config-not-replicated)
s3-replication-cross-account-requirements
  claim: For cross-account replication, the destination bucket owner must grant the source bucket owner permission to replicate with a bucket policy, and the destination buckets cannot be Requester Pays buckets.
  scope: per cross-account replication configuration; source and destination buckets owned by different AWS accounts.
  link: [grant the owner of the source bucket permissions](../facts/s3.md#s3-replication-cross-account-requirements)
  link: [cannot be configured as Requester Pays buckets](../facts/s3.md#s3-replication-cross-account-requirements)
s3-replication-delete-markers-optional
  claim: You can replicate delete markers from source to destination if delete marker replication is enabled in the replication configuration; S3 then behaves as if the object was deleted in both buckets. S3 Replication does not support delete marker replication for object tag-based replication rules.
  scope: per replication rule; delete marker replication enabled in the rule.
  link: [delete marker replication enabled](../facts/s3.md#s3-replication-delete-markers-optional)
  link: [the object was deleted in both buckets](../facts/s3.md#s3-replication-delete-markers-optional)
  link: [does not support delete marker replication](../facts/s3.md#s3-replication-delete-markers-optional)
s3-replication-destinations-quota
  claim: A source bucket can replicate to 28 destination buckets across all its replication rules by default; the quota is adjustable.
  scope: per source bucket; default; adjustable.
  link: [28](../facts/s3.md#s3-replication-destinations-quota)
  say: twenty-eight
s3-replication-direct-to-colder-class
  claim: Replication can put replicas directly into S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive or another storage class in the destination bucket; or it can keep the same class and let a lifecycle configuration on the destination move replicas to a colder class as they age.
  scope: S3 Replication destination buckets.
  link: [directly put objects into S3 Glacier Flexible Retrieval](../facts/s3.md#s3-replication-direct-to-colder-class)
s3-replication-kms-request-quota
  claim: When you replicate objects encrypted with SSE-KMS, AWS KMS requests per second quotas apply, both to requests that you make directly and to requests that S3 replication makes on your behalf.
  scope: KMS requests made directly and by S3 replication on your behalf; objects encrypted with SSE-KMS.
  link: [AWS KMS requests per second quotas apply](../facts/s3.md#s3-replication-kms-request-quota)
  say: AWS KMS requests per second quotas apply
s3-replication-lifecycle-honors-original-creation-time
  claim: Replication time depends on object size and can take hours for large objects. Lifecycle rules on the destination bucket use the object's original creation time, not the time the replica arrived.
  scope: per replicated object.
  link: [honor the original creation time of the object](../facts/s3.md#s3-replication-lifecycle-honors-original-creation-time)
  link: [it can take several hours](../facts/s3.md#s3-replication-lifecycle-honors-original-creation-time)
s3-replication-metadata-one-way-by-default
  claim: By default S3 replicates metadata such as tags, ACLs and Object Lock settings from the source object to its replicas only. With replica modification sync enabled on both buckets, metadata changes made on a replica are copied back to the source, making replication two-way.
  scope: per replication rule; default; adjustable; replica modification sync must be enabled on both source and destination buckets.
  link: [from the source objects to the replicas only](../facts/s3.md#s3-replication-metadata-one-way-by-default)
  link: [replica modification sync](../facts/s3.md#s3-replication-metadata-one-way-by-default)
  link: [making the replication bidirectional (two-way replication)](../facts/s3.md#s3-replication-metadata-one-way-by-default)
  link: [on both the source and destination buckets](../facts/s3.md#s3-replication-metadata-one-way-by-default)
s3-replication-object-lock-both-buckets
  claim: If the source bucket has S3 Object Lock enabled, every destination bucket of its replication must also have Object Lock enabled.
  scope: replication from a bucket with Object Lock.
  link: [must also have S3 Object Lock enabled](../facts/s3.md#s3-replication-object-lock-both-buckets)
s3-replication-owner-override-restrict-replicas
  claim: With the owner override option, replication changes replica ownership to the AWS account that owns the destination bucket, whoever owns the source object; this can be used to restrict access to the replicas.
  scope: S3 Replication.
  link: [owner override](../facts/s3.md#s3-replication-owner-override-restrict-replicas)
s3-replication-pricing-dimensions
  claim: Cross-Region Replication adds inter-Region data transfer out from S3 to each destination Region; S3 Replication Time Control adds an RTC data transfer charge and replication metrics billed like CloudWatch custom metrics.
  scope: Cross-Region Replication and S3 Replication Time Control.
  link: [inter-region Data Transfer OUT from S3](../facts/s3.md#s3-replication-pricing-dimensions)
  link: [a Replication Time Control Data Transfer charge](../facts/s3.md#s3-replication-pricing-dimensions)
s3-replication-replica-keeps-source-encryption
  claim: Replicas of SSE-S3, SSE-KMS or DSSE-KMS objects use the same encryption type as the source objects, not the destination bucket default; unencrypted source objects are encrypted with the destination bucket default encryption.
  scope: per replica.
  link: [same type of encryption as the source objects](../facts/s3.md#s3-replication-replica-keeps-source-encryption)
  link: [default encryption settings of the destination bucket](../facts/s3.md#s3-replication-replica-keeps-source-encryption)
s3-replication-replicas-not-rereplicated
  claim: By default S3 does not replicate objects that are themselves replicas created by another replication rule (A to B, then B to C does not copy the replicas from A to C); Batch Replication can replicate them.
  scope: chained replication rules.
  link: [are not replicated to bucket C](../facts/s3.md#s3-replication-replicas-not-rereplicated)
  link: [use Batch Replication](../facts/s3.md#s3-replication-replicas-not-rereplicated)
s3-replication-request-overhead-per-object
  claim: For each replicated object, S3 replication makes up to 5 GET/HEAD requests and 1 PUT request to the source bucket and 1 PUT request to each destination bucket, and these count toward the request-rate guidelines; you pay for only 1 PUT request per object replicated.
  scope: per replicated object; maximum.
  link: [up to 5 GET/HEAD requests](../facts/s3.md#s3-replication-request-overhead-per-object)
  link: [1 PUT request per object replicated](../facts/s3.md#s3-replication-request-overhead-per-object)
  say: up to five GET or HEAD requests | one PUT request per object replicated
s3-replication-requires-versioning-both
  claim: S3 Replication requires versioning enabled on both the source and the destination bucket, and S3 must have permissions to replicate objects from the source bucket to the destination bucket or buckets on your behalf.
  scope: per replication configuration.
  link: [source and destination buckets must have versioning enabled](../facts/s3.md#s3-replication-requires-versioning-both)
  link: [must have permissions to replicate objects](../facts/s3.md#s3-replication-requires-versioning-both)
s3-replication-requires-versioning-both-buckets
  claim: S3 Replication requires versioning to be enabled on both the source and the destination bucket; if you disable versioning on the destination, replication fails, and you cannot disable it on the source while a replication configuration exists.
  scope: source and destination buckets of a replication configuration.
  link: [source and destination buckets must have versioning enabled](../facts/s3.md#s3-replication-requires-versioning-both-buckets)
  link: [on the destination bucket, replication fails](../facts/s3.md#s3-replication-requires-versioning-both-buckets)
  link: [must remove the replication configuration](../facts/s3.md#s3-replication-requires-versioning-both-buckets)
s3-replication-role-kms-decrypt-encrypt
  claim: To replicate KMS-encrypted objects, the replication IAM role needs kms:Decrypt on the key that protects the source object and kms:Encrypt on the key that will protect the replica; if the keys belong to another account, that key owner must grant these permissions.
  scope: replication IAM role.
  link: [`kms:Decrypt`](../facts/s3.md#s3-replication-role-kms-decrypt-encrypt)
  link: [`kms:Encrypt`](../facts/s3.md#s3-replication-role-kms-decrypt-encrypt)
s3-replication-rules-max
  claim: A replication configuration can hold at most 1,000 rules.
  scope: per replication configuration; maximum; not adjustable.
  link: [1,000](../facts/s3.md#s3-replication-rules-max)
  say: one thousand
s3-replication-sse-c-supported
  claim: S3 Replication supports objects encrypted with SSE-C, with no additional SSE-C permissions beyond those replication already needs and no additional charge.
  scope: S3 Replication.
  link: [supports objects that are encrypted with SSE-C](../facts/s3.md#s3-replication-sse-c-supported)
  link: [no additional charges](../facts/s3.md#s3-replication-sse-c-supported)
s3-replication-sse-kms-opt-in
  claim: By default S3 does not replicate objects encrypted with SSE-KMS or DSSE-KMS; the replication configuration must opt in to them and name the customer managed KMS key to encrypt the replicas.
  scope: per replication rule; default; not adjustable.
  link: [doesn't replicate objects that are encrypted with SSE-KMS](../facts/s3.md#s3-replication-sse-kms-opt-in)
  link: [Explicitly opt in](../facts/s3.md#s3-replication-sse-kms-opt-in)
s3-replication-tag-rules-need-tag-at-put
  claim: With tag-based replication rules and live replication, a new object must carry the matching tag in the PutObject request; objects tagged afterwards are not replicated and need S3 Batch Replication.
  scope: tag-based replication rules.
  link: [those objects also won't be replicated](../facts/s3.md#s3-replication-tag-rules-need-tag-at-put)
  link: [you must use S3 Batch Replication](../facts/s3.md#s3-replication-tag-rules-need-tag-at-put)
s3-replication-time-control-15-minutes
  claim: S3 Replication Time Control is designed to replicate most objects in seconds and 99.99% of objects within 15 minutes, backed by an SLA that 99.9% of objects replicate within 15 minutes per Region pair in a billing month. It is enabled per replication rule.
  scope: per replication rule, per Region pair; S3 RTC enabled on the rule.
  link: [99.99% of objects within 15 minutes](../facts/s3.md#s3-replication-time-control-15-minutes)
  link: [99.9% of objects will be replicated in 15 minutes](../facts/s3.md#s3-replication-time-control-15-minutes)
  link: [enabled as an option for each replication rule](../facts/s3.md#s3-replication-time-control-15-minutes)
s3-replication-two-way-before-mrap-failover
  claim: To fail over to a bucket in another Region and keep all metadata and objects in sync, set up two-way (bi-directional) replication rules before configuring Multi-Region Access Point failover controls, so data written to the failover bucket is replicated back to the source bucket.
  scope: S3 Replication with Multi-Region Access Points; failover with Multi-Region Access Point failover controls.
  link: [two-way replication](../facts/s3.md#s3-replication-two-way-before-mrap-failover)
s3-replication-version-deletes-not-replicated
  claim: A DELETE that names a version ID deletes that version only in the source bucket; S3 does not replicate the deletion to the destination buckets, which protects data from malicious deletions.
  scope: per replication configuration.
  link: [doesn't replicate the deletion in the destination buckets](../facts/s3.md#s3-replication-version-deletes-not-replicated)
  link: [protects data from malicious deletions](../facts/s3.md#s3-replication-version-deletes-not-replicated)
s3-request-scaling-gradual-503
  claim: S3 scaling to a higher request rate is gradual, not instantaneous; while S3 scales, clients may see some 503 (Slow Down) errors, which go away when scaling is complete.
  scope: per prefix; during scaling to a new higher request rate.
  link: [503 (Slow Down) errors](../facts/s3.md#s3-request-scaling-gradual-503)
  say: five-oh-three Slow Down errors
s3-requester-pays-header-required
  claim: A requester must include the x-amz-request-payer header (or the RequestPayer parameter) to show they accept the charges. Without it, S3 returns a 403 error and charges the bucket owner for the request.
  scope: per request to a Requester Pays bucket; bucket owners do not need to add the header.
  link: [x-amz-request-payer](../facts/s3.md#s3-requester-pays-header-required)
  link: [Amazon S3 returns a 403 error and charges the bucket owner for the request](../facts/s3.md#s3-requester-pays-header-required)
s3-requester-pays-no-anonymous
  claim: A Requester Pays bucket does not allow anonymous access; every request must be authenticated so that S3 can identify and charge the requester.
  scope: per Requester Pays bucket.
  link: [anonymous access to that bucket is not allowed](../facts/s3.md#s3-requester-pays-no-anonymous)
  link: [must authenticate all requests](../facts/s3.md#s3-requester-pays-no-anonymous)
s3-requester-pays-share-without-paying-access
  claim: Configure a bucket as Requester Pays when you want to share data but not pay the charges that other people's access to it creates; the requester then pays the request and data transfer cost.
  scope: per bucket.
  link: [share data but not incur charges](../facts/s3.md#s3-requester-pays-share-without-paying-access)
s3-requester-pays-who-pays
  claim: With a Requester Pays bucket, the requester instead of the bucket owner pays for the request and the data download. The bucket owner always pays for storing the data.
  scope: per general purpose bucket; Requester Pays enabled on the bucket.
  link: [the requester instead of the bucket owner pays](../facts/s3.md#s3-requester-pays-who-pays)
  link: [the bucket owner always pays the cost](../facts/s3.md#s3-requester-pays-who-pays)
  link: [Requester Pays](../facts/s3.md#s3-requester-pays-who-pays)
s3-restore-batch-one-archive-type-per-job
  claim: A Batch Operations restore job works either on Glacier Flexible Retrieval and Deep Archive objects or on Intelligent-Tiering archive tier objects, never both in the same job.
  scope: per Batch Operations restore job.
  link: [can't operate on both types of archived objects](../facts/s3.md#s3-restore-batch-one-archive-type-per-job)
s3-restore-completed-event
  claim: You can be notified when an object restore completes with the s3:ObjectRestore:Completed event of S3 Event Notifications.
  scope: per restore request.
  link: [`s3:ObjectRestore:Completed`](../facts/s3.md#s3-restore-completed-event)
s3-restore-intelligent-tiering-no-expiry
  claim: Objects restored from S3 Glacier Flexible Retrieval or Deep Archive are kept only for the number of days you specify, while objects restored from the Intelligent-Tiering Archive Access or Deep Archive Access tiers have no expiration date and move back to the Frequent Access tier.
  scope: restored objects.
  link: [for the number of days that you specify](../facts/s3.md#s3-restore-intelligent-tiering-no-expiry)
  link: [don't have expiration dates](../facts/s3.md#s3-restore-intelligent-tiering-no-expiry)
s3-restore-temporary-copy-storage-class-unchanged
  claim: Archived objects are not readable in real time: you start a restore request and wait for a temporary copy that lives for the number of days you specify; the object's storage class stays Glacier Flexible Retrieval or Deep Archive.
  scope: per restore request.
  link: [a temporary copy of the object is available](../facts/s3.md#s3-restore-temporary-copy-storage-class-unchanged)
  link: [the object's storage class remains](../facts/s3.md#s3-restore-temporary-copy-storage-class-unchanged)
s3-retrieval-bulk-lowest-cost-48-hours-deep-archive
  claim: Bulk is the lowest-cost retrieval option: typically within 5–12 hours from S3 Glacier Flexible Retrieval and within 48 hours from S3 Glacier Deep Archive; Bulk retrievals are free for Glacier Flexible Retrieval and Intelligent-Tiering objects.
  scope: per restore request, Bulk retrieval tier; typical times.
  link: [Bulk](../facts/s3.md#s3-retrieval-bulk-lowest-cost-48-hours-deep-archive)
  link: [within 48 hours](../facts/s3.md#s3-retrieval-bulk-lowest-cost-48-hours-deep-archive)
  link: [within 5–12 hours](../facts/s3.md#s3-retrieval-bulk-lowest-cost-48-hours-deep-archive)
  link: [Bulk retrievals are free](../facts/s3.md#s3-retrieval-bulk-lowest-cost-48-hours-deep-archive)
  say: within forty-eight hours | within five to twelve hours
s3-retrieval-expedited-1-5-minutes-not-deep-archive
  claim: Expedited retrieval, for occasional urgent requests, typically makes objects under 250 megabytes available within 1–5 minutes from S3 Glacier Flexible Retrieval; it is a premium option and is not available for S3 Glacier Deep Archive.
  scope: per restore request, Expedited retrieval tier, S3 Glacier Flexible Retrieval and Intelligent-Tiering Archive Access; typical times; Provisioned Capacity can be purchased.
  link: [within 1–5 minutes](../facts/s3.md#s3-retrieval-expedited-1-5-minutes-not-deep-archive)
  link: [under 250 megabytes](../facts/s3.md#s3-retrieval-expedited-1-5-minutes-not-deep-archive)
  link: [Not available](../facts/s3.md#s3-retrieval-expedited-1-5-minutes-not-deep-archive)
  say: within one to five minutes | under two hundred fifty megabytes
s3-retrieval-standard-default-12-hours-deep-archive
  claim: Standard is the default retrieval option when a restore request names none; it typically finishes within 3–5 hours for S3 Glacier Flexible Retrieval and within 12 hours for S3 Glacier Deep Archive.
  scope: per restore request, Standard retrieval tier; default; adjustable; typical times; Batch Operations restores start sooner.
  link: [Standard is the default option](../facts/s3.md#s3-retrieval-standard-default-12-hours-deep-archive)
  link: [within 3–5 hours](../facts/s3.md#s3-retrieval-standard-default-12-hours-deep-archive)
  link: [within 12 hours](../facts/s3.md#s3-retrieval-standard-default-12-hours-deep-archive)
  say: within three to five hours | within twelve hours
s3-retry-large-requests-slowest-5-percent
  claim: For large variably sized requests (for example, more than 128 MB), AWS advises tracking throughput and retrying the slowest 5 percent of the requests.
  scope: per application; large variably sized requests.
  link: [slowest 5 percent](../facts/s3.md#s3-retry-large-requests-slowest-5-percent)
  link: [more than 128 MB](../facts/s3.md#s3-retry-large-requests-slowest-5-percent)
  say: slowest five percent | more than one hundred twenty-eight megabytes
s3-retry-small-requests-2-seconds
  claim: For smaller requests (for example, less than 512 KB), AWS's guideline is to retry a GET or PUT after 2 seconds, then a second retry after an additional 4 seconds.
  scope: per request; latency-sensitive applications, small requests.
  link: [after 2 seconds](../facts/s3.md#s3-retry-small-requests-2-seconds)
  link: [additional 4 seconds](../facts/s3.md#s3-retry-small-requests-2-seconds)
  link: [less than 512 KB](../facts/s3.md#s3-retry-small-requests-2-seconds)
  say: after two seconds | additional four seconds | less than five hundred twelve kilobytes
s3-rtc-guide-99-9-percent-15-minutes
  claim: The S3 User Guide says S3 Replication Time Control replicates most uploaded objects in seconds, and 99.9 percent of those objects within 15 minutes.
  scope: per replication rule with S3 RTC enabled; S3 RTC enabled.
  link: [99.9 percent](../facts/s3.md#s3-rtc-guide-99-9-percent-15-minutes)
  link: [within 15 minutes](../facts/s3.md#s3-rtc-guide-99-9-percent-15-minutes)
  say: ninety-nine point nine percent | within fifteen minutes
s3-rtc-metrics-events-within-15-minutes
  claim: Replication metrics and replication events become available within 15 minutes of enabling S3 RTC; enabling S3 RTC also enables S3 Replication metrics on the rule.
  scope: per replication rule; maximum; S3 RTC enabled.
  link: [within 15 minutes of enabling S3 RTC](../facts/s3.md#s3-rtc-metrics-events-within-15-minutes)
  say: within fifteen minutes of enabling S3 RTC
s3-rtc-sla-exclusions
  claim: The S3 RTC SLA does not apply during periods when the S3 request-rate performance guidelines are exceeded, or when the replication data transfer rate exceeds the default 1 gigabit per second (Gbps) quota.
  scope: per account, per source Region; default; the transfer rate quota can be raised.
  link: [1 gigabit per second (Gbps)](../facts/s3.md#s3-rtc-sla-exclusions)
  say: one gigabit per second
s3-rtc-threshold-only-15-minutes
  claim: In an S3 RTC replication rule, the EventThreshold minutes and the ReplicationTime minutes can only be set to 15.
  scope: per replication rule; fixed; S3 RTC enabled.
  link: [15](../facts/s3.md#s3-rtc-threshold-only-15-minutes)
  say: fifteen
s3-rtc-transfer-rate-quota
  claim: Replication Time Control transfers at most 1 Gigabits per second from a source Region per account by default; the quota is adjustable.
  scope: per account, per source Region; default; adjustable.
  link: [1 Gigabits per second](../facts/s3.md#s3-rtc-transfer-rate-quota)
  say: one gigabit per second
s3-same-account-bucket-or-user-policy
  claim: When the bucket owner and the parent account of the user are the same account, the bucket owner can grant access with either a bucket policy or a user policy.
  scope: same-account access to S3; bucket owner and the user's parent account are the same.
  link: [either a bucket policy or a user policy](../facts/s3.md#s3-same-account-bucket-or-user-policy)
s3-server-access-logging-vs-cloudtrail-data-events
  claim: Server access logging gives detailed records of the requests made to a bucket, for security and access audits. CloudTrail data events record object-level API activity such as GetObject, DeleteObject and PutObject for individual buckets.
  scope: per bucket.
  link: [detailed records of the requests](../facts/s3.md#s3-server-access-logging-vs-cloudtrail-data-events)
  link: [record object-level API activity for individual buckets](../facts/s3.md#s3-server-access-logging-vs-cloudtrail-data-events)
  link: [GetObject, DeleteObject, and PutObject](../facts/s3.md#s3-server-access-logging-vs-cloudtrail-data-events)
s3-server-side-vs-client-side-encryption
  claim: With server-side encryption S3 encrypts objects before writing them to disk and decrypts them on download. With client-side encryption you encrypt data before upload and manage the encryption process, keys and tools yourself.
  scope: per object.
  link: [encrypts your objects before saving them on disks](../facts/s3.md#s3-server-side-vs-client-side-encryption)
  link: [encrypt your data client-side](../facts/s3.md#s3-server-side-vs-client-side-encryption)
  link: [you manage the encryption process, encryption keys](../facts/s3.md#s3-server-side-vs-client-side-encryption)
s3-single-key-updates-atomic
  claim: Updates to a single key are atomic: a concurrent read during an overwrite returns either the old data or the new data, never partial or corrupt data.
  scope: per object key.
  link: [updates to a single key are atomic](../facts/s3.md#s3-single-key-updates-atomic)
  link: [never partial or corrupt data](../facts/s3.md#s3-single-key-updates-atomic)
s3-single-put-max
  claim: With a single PUT operation through the AWS SDKs, REST API or AWS CLI, you can upload a single object up to 5 GB in size.
  scope: per single PUT operation; maximum; not adjustable; single operation through the SDKs, REST API or AWS CLI.
  link: [5 GB](../facts/s3.md#s3-single-put-max)
  say: five gigabytes
s3-small-object-latency-100-200ms
  claim: Latency-sensitive applications can achieve consistent small-object latencies (and first-byte-out latencies for larger objects) of roughly 100–200 milliseconds on S3.
  scope: per request, small objects; first-byte-out latency for larger objects.
  link: [roughly 100–200 milliseconds](../facts/s3.md#s3-small-object-latency-100-200ms)
  say: roughly one hundred to two hundred milliseconds
s3-srr-no-data-transfer-charge-crr-varies-by-region
  claim: Same-Region Replication has no data transfer charge; Cross-Region Replication pays inter-Region data transfer, and the rate depends on the Region pair you choose.
  scope: per GB replicated.
  link: [no data transfer charges associated with Same-Region Replication](../facts/s3.md#s3-srr-no-data-transfer-charge-crr-varies-by-region)
  link: [inter-Region data transfer charges vary](../facts/s3.md#s3-srr-no-data-transfer-charge-crr-varies-by-region)
s3-sse-c-disabled-by-default-2026-04
  claim: Starting April 2026, SSE-C is disabled by default for all new general purpose buckets and for existing buckets in accounts with no SSE-C encrypted objects; to use it you set BlockedEncryptionTypes to NONE with PutBucketEncryption.
  scope: new general purpose buckets, and existing buckets in accounts with no SSE-C encrypted objects; default; adjustable; while blocked, writes that specify SSE-C fail with HTTP 403 AccessDenied.
  link: [Starting April 2026](../facts/s3.md#s3-sse-c-disabled-by-default-2026-04)
  link: [SSE-C is disabled by default](../facts/s3.md#s3-sse-c-disabled-by-default-2026-04)
s3-sse-c-impractical-for-sharing
  claim: SSE-C needs the encryption key in every read or write request, which makes sharing access with other users, roles or AWS services impractical; AWS managed services cannot natively decrypt SSE-C objects. SSE-S3 or SSE-KMS give equal protection with more flexibility.
  scope: SSE-C objects.
  link: [provide the encryption key with every request](../facts/s3.md#s3-sse-c-impractical-for-sharing)
  link: [cannot be natively decrypted by AWS managed services](../facts/s3.md#s3-sse-c-impractical-for-sharing)
s3-sse-c-key-never-stored-https-required
  claim: With SSE-C, S3 never stores the encryption key, so you must supply it every time the data is downloaded, and requests with SSE-C headers must use HTTPS.
  scope: SSE-C requests.
  link: [S3 never stores the encryption key](../facts/s3.md#s3-sse-c-key-never-stored-https-required)
  link: [You must use HTTPS](../facts/s3.md#s3-sse-c-key-never-stored-https-required)
s3-sse-kms-benefits-over-sse-s3
  claim: SSE-KMS lets AWS KMS manage the keys and adds separate permissions for using the KMS key, plus an audit trail that shows who used the key for which object and when, including failed attempts.
  scope: per object encrypted with SSE-KMS.
  link: [there are separate permissions](../facts/s3.md#s3-sse-kms-benefits-over-sse-s3)
  link: [who used your key to access which object](../facts/s3.md#s3-sse-kms-benefits-over-sse-s3)
s3-sse-kms-cross-account-needs-customer-managed-key
  claim: When no KMS key is named in the request or bucket default, the AWS managed key aws/s3 is used; it works for principals in the same account as the key. For cross-account access to SSE-KMS objects you need a customer managed key whose key policy allows the other account.
  scope: per object encrypted with SSE-KMS; default.
  link: [the AWS managed key (aws/s3) is used](../facts/s3.md#s3-sse-kms-cross-account-needs-customer-managed-key)
  link: [use a customer managed key](../facts/s3.md#s3-sse-kms-cross-account-needs-customer-managed-key)
s3-sse-kms-key-same-region-as-bucket
  claim: With SSE-KMS on an S3 bucket, the AWS KMS keys must be in the same Region as the bucket.
  scope: per bucket using SSE-KMS.
  link: [in the same Region as the bucket](../facts/s3.md#s3-sse-kms-key-same-region-as-bucket)
s3-sse-kms-multi-region-keys-single-region
  claim: S3 accepts multi-Region KMS keys but treats them as single-Region keys and does not use their multi-Region features.
  scope: SSE-KMS with multi-Region keys.
  link: [as though they were single-Region keys](../facts/s3.md#s3-sse-kms-multi-region-keys-single-region)
s3-sse-kms-when-more-key-control
  claim: Choose SSE-KMS or DSSE-KMS over the SSE-S3 default when you need more control over the keys, such as managing key rotation and access policy grants.
  scope: per bucket.
  link: [if you need more control over your keys](../facts/s3.md#s3-sse-kms-when-more-key-control)
s3-sse-s3-default-every-bucket
  claim: Every S3 bucket has encryption configured by default and every new object is encrypted at rest with SSE-S3 unless another type is chosen. To use another type, name it in the PUT request (SSE-KMS, DSSE-KMS or SSE-C) or change the bucket default to SSE-KMS or DSSE-KMS.
  scope: per bucket; default; adjustable.
  link: [the default encryption configuration for every bucket](../facts/s3.md#s3-sse-s3-default-every-bucket)
  link: [are automatically encrypted at rest](../facts/s3.md#s3-sse-s3-default-every-bucket)
  link: [you can use SSE-KMS or DSSE-KMS](../facts/s3.md#s3-sse-s3-default-every-bucket)
  link: [SSE-S3](../facts/s3.md#s3-sse-s3-default-every-bucket)
s3-standard-ia-primary-copy
  claim: AWS recommends S3 Standard-IA for the primary or only copy of data that cannot be re-created; its objects are resilient to the loss of an Availability Zone.
  scope: S3 Standard-IA storage class.
  link: [primary or only copy of data](../facts/s3.md#s3-standard-ia-primary-copy)
  say: the only copy of data you cannot re-create
s3-standard-ia-vs-one-zone-ia-use
  claim: Use S3 Standard-IA for the primary or only copy of data that cannot be re-created. Use S3 One Zone-IA when you can re-create the data if the Availability Zone fails, for example for replicas made by Cross-Region Replication; it stores data in only one Availability Zone and is not resilient to the loss of that zone.
  scope: storage class choice.
  link: [primary or only copy of data](../facts/s3.md#s3-standard-ia-vs-one-zone-ia-use)
  link: [re-create the data if the Availability Zone fails](../facts/s3.md#s3-standard-ia-vs-one-zone-ia-use)
  link: [not resilient to the physical loss](../facts/s3.md#s3-standard-ia-vs-one-zone-ia-use)
s3-storage-class-analysis-observation
  claim: Storage Class Analysis watches object-level access patterns in one bucket, prefix or tag set for the previous 30 to 90 days and recommends when to move data to another storage class; you then configure a Lifecycle rule to do the transition.
  scope: per bucket, prefix or tag.
  link: [monitor access patterns across objects](../facts/s3.md#s3-storage-class-analysis-observation)
  link: [the previous 30-90 days](../facts/s3.md#s3-storage-class-analysis-observation)
  link: [configure an S3 Lifecycle policy](../facts/s3.md#s3-storage-class-analysis-observation)
s3-storage-class-default-standard
  claim: Every object has a storage class. If you do not specify one when uploading, S3 assigns S3 Standard, the default storage class.
  scope: per object; default; adjustable.
  link: [S3 Standard](../facts/s3.md#s3-storage-class-default-standard)
  link: [Amazon S3 assigns the S3 Standard storage class](../facts/s3.md#s3-storage-class-default-standard)
s3-storage-class-set-per-object
  claim: A storage class is set per object: one general purpose bucket can hold objects in every storage class except S3 Express One Zone.
  scope: general purpose buckets.
  link: [at the object level](../facts/s3.md#s3-storage-class-set-per-object)
  link: [all storage classes except S3 Express One Zone](../facts/s3.md#s3-storage-class-set-per-object)
s3-storage-lens-find-buckets-without-abort-mpu-rule
  claim: S3 Storage Lens can identify buckets that have no S3 Lifecycle rule to abort incomplete multipart uploads that are more than 7 days old, and buckets that do not use data-protection practices such as S3 Replication or S3 Versioning.
  scope: S3 Storage Lens.
  link: [incomplete multipart uploads that are more than 7 days old](../facts/s3.md#s3-storage-lens-find-buckets-without-abort-mpu-rule)
  link: [such as using S3 Replication or S3 Versioning](../facts/s3.md#s3-storage-lens-find-buckets-without-abort-mpu-rule)
s3-storage-lens-free-metric-categories
  claim: Free Storage Lens metrics include summary, cost optimization, data protection, access management, performance and event metrics.
  scope: S3 Storage Lens free tier.
  link: [summary, cost optimization, data protection](../facts/s3.md#s3-storage-lens-free-metric-categories)
s3-storage-lens-free-vs-advanced
  claim: S3 Storage Lens has free tier metrics and advanced tier metrics at additional charge; the advanced tier adds advanced metric categories, prefix aggregation, contextual recommendations, expanded prefixes metrics reports and CloudWatch publishing.
  scope: S3 Storage Lens.
  link: [free tier metrics and advanced tier metrics](../facts/s3.md#s3-storage-lens-free-vs-advanced)
  link: [Amazon CloudWatch publishing](../facts/s3.md#s3-storage-lens-free-vs-advanced)
  link: [contextual recommendations](../facts/s3.md#s3-storage-lens-free-vs-advanced)
s3-storage-lens-organization-view
  claim: S3 Storage Lens gives organization-wide visibility into storage usage and activity with daily recommendations to cut cost and improve data protection; S3 Inventory instead lists the objects of one bucket or prefix with their metadata for object-level analysis.
  scope: per organization or account.
  link: [organization-wide visibility into object storage usage](../facts/s3.md#s3-storage-lens-organization-view)
  link: [a list of your objects](../facts/s3.md#s3-storage-lens-organization-view)
  link: [daily organization level recommendations](../facts/s3.md#s3-storage-lens-organization-view)
s3-strong-read-after-write-consistency
  claim: S3 gives strong read-after-write consistency for PUT and DELETE requests of objects in all AWS Regions, for new objects, overwrites and deletes alike.
  scope: all AWS Regions.
  link: [strong read-after-write consistency](../facts/s3.md#s3-strong-read-after-write-consistency)
  link: [PUT and DELETE requests of objects](../facts/s3.md#s3-strong-read-after-write-consistency)
  link: [in all AWS Regions](../facts/s3.md#s3-strong-read-after-write-consistency)
s3-table-and-vector-buckets
  claim: S3 has four bucket types: general purpose, directory, table and vector buckets. Table buckets store tabular data as Apache Iceberg tables for analytics engines such as Athena, Redshift and Spark; vector buckets store and query vector embeddings with dedicated APIs.
  scope: Amazon S3 bucket types.
  link: [four types of buckets](../facts/s3.md#s3-table-and-vector-buckets)
  link: [storing tabular data in the Apache Iceberg format](../facts/s3.md#s3-table-and-vector-buckets)
  link: [purpose-built to store and query vectors](../facts/s3.md#s3-table-and-vector-buckets)
s3-transfer-acceleration-endpoint-and-naming
  claim: To use Transfer Acceleration you must send requests to the bucket-name.s3-accelerate.amazonaws.com endpoint; the regular endpoints keep standard transfer. The bucket name must be DNS-compliant and must not contain periods.
  scope: per general purpose bucket.
  link: [s3-accelerate.amazonaws.com](../facts/s3.md#s3-transfer-acceleration-endpoint-and-naming)
  link: [must not contain periods](../facts/s3.md#s3-transfer-acceleration-endpoint-and-naming)
s3-transfer-acceleration-how-it-works
  claim: Transfer Acceleration is a bucket-level feature for fast transfers over long distances between a client and a general purpose bucket. It uses CloudFront edge locations: data arrives at an edge location and is routed to S3 over an optimized network path.
  scope: per general purpose bucket.
  link: [secure transfers of files over long distances](../facts/s3.md#s3-transfer-acceleration-how-it-works)
  link: [globally distributed edge locations in Amazon CloudFront](../facts/s3.md#s3-transfer-acceleration-how-it-works)
  link: [over an optimized network path](../facts/s3.md#s3-transfer-acceleration-how-it-works)
s3-transfer-acceleration-no-charge-when-not-faster
  claim: On each accelerated upload AWS checks whether Transfer Acceleration is likely to be faster than a regular transfer to the same Region; if not, that use is not charged and may bypass the acceleration system.
  scope: per upload; AWS determines the transfer is not likely to be faster than a regular transfer.
  link: [we will not charge for that use](../facts/s3.md#s3-transfer-acceleration-no-charge-when-not-faster)
s3-transfer-acceleration-no-data-at-edge
  claim: Transfer Acceleration keeps the same security as regular S3 transfers, works over standard TCP without firewall changes, and never stores data at the edge locations.
  scope: per accelerated transfer.
  link: [No data is ever saved](../facts/s3.md#s3-transfer-acceleration-no-data-at-edge)
  link: [the same security as regular transfers](../facts/s3.md#s3-transfer-acceleration-no-data-at-edge)
s3-transfer-acceleration-pricing-added-to-data-transfer
  claim: S3 Transfer Acceleration speeds up internet transfers between a client and one bucket; its price depends on the edge location used and is added on top of normal data transfer pricing.
  scope: per GB accelerated, per edge location.
  link: [based on the AWS edge location used](../facts/s3.md#s3-transfer-acceleration-pricing-added-to-data-transfer)
  link: [in addition to Data Transfer pricing](../facts/s3.md#s3-transfer-acceleration-pricing-added-to-data-transfer)
s3-transfer-acceleration-vs-cloudfront-small-objects
  claim: Transfer Acceleration is the better choice when higher throughput is wanted. For objects smaller than 1 GB or a data set under 1 GB, AWS says to consider CloudFront PUT/POST instead.
  scope: upload path choice; object or data set size under 1 GB.
  link: [if a higher throughput is desired](../facts/s3.md#s3-transfer-acceleration-vs-cloudfront-small-objects)
  link: [smaller than 1 GB](../facts/s3.md#s3-transfer-acceleration-vs-cloudfront-small-objects)
s3-transfer-acceleration-when-to-use
  claim: Use Transfer Acceleration when customers upload to one central bucket from all over the world, when you move gigabytes to terabytes across continents regularly, or when you cannot use all your available bandwidth when uploading to S3.
  scope: per general purpose bucket.
  link: [upload to a centralized general purpose bucket](../facts/s3.md#s3-transfer-acceleration-when-to-use)
  link: [on a regular basis across continents](../facts/s3.md#s3-transfer-acceleration-when-to-use)
  link: [can't use all of your available bandwidth](../facts/s3.md#s3-transfer-acceleration-when-to-use)
s3-trusted-advisor-open-access-warnings
  claim: AWS recommends regularly checking the security advisories in Trusted Advisor, in particular warnings about S3 buckets with open access permissions.
  scope: AWS account.
  link: [security advisories posted in Trusted Advisor](../facts/s3.md#s3-trusted-advisor-open-access-warnings)
s3-update-object-encryption-job-max-objects
  claim: A single Batch Operations UpdateObjectEncryption job can support a manifest with up to 20 billion objects, and the operation can also change the customer managed KMS key used to encrypt the data.
  scope: per Batch Operations UpdateObjectEncryption job; maximum; not adjustable.
  link: [up to 20 billion objects](../facts/s3.md#s3-update-object-encryption-job-max-objects)
  say: up to twenty billion objects
s3-update-object-encryption-unsupported-objects
  claim: UpdateObjectEncryption does not support objects that are unencrypted or encrypted with DSSE-KMS or SSE-C, and you cannot specify SSE-S3 as the new type. It fails on any object that has an Object Lock retention mode or legal hold.
  scope: UpdateObjectEncryption operation.
  link: [doesn't support objects that are unencrypted](../facts/s3.md#s3-update-object-encryption-unsupported-objects)
  link: [fails on any object](../facts/s3.md#s3-update-object-encryption-unsupported-objects)
  say: not for unencrypted, DSSE-KMS or SSE-C objects | fails on locked objects
s3-upload-overwrite-creates-new-version
  claim: Uploading an object with a key that already exists in a versioning-enabled bucket creates another version instead of replacing the existing object. A bucket can hold an unlimited number of objects, and you need write permission on the bucket to upload.
  scope: per versioning-enabled bucket.
  link: [creates another version of the object](../facts/s3.md#s3-upload-overwrite-creates-new-version)
  link: [an unlimited number of objects in a bucket](../facts/s3.md#s3-upload-overwrite-creates-new-version)
s3-version-id-null-before-versioning
  claim: When you enable S3 Versioning in a bucket, S3 generates a unique version ID for each object added to the bucket; objects that already existed in the bucket when versioning was enabled have a version ID of null.
  scope: per versioning-enabled bucket.
  link: [version ID of null](../facts/s3.md#s3-version-id-null-before-versioning)
  link: [a unique version ID for each object](../facts/s3.md#s3-version-id-null-before-versioning)
s3-versioning-delete-with-version-id-permanent
  claim: Only the bucket owner or an authorized IAM user can permanently delete a version: a DELETE that names the versionId permanently deletes that version and S3 adds no delete marker.
  scope: per versioning-enabled bucket.
  link: [that object version is permanently deleted](../facts/s3.md#s3-versioning-delete-with-version-id-permanent)
  link: [doesn't insert a delete marker](../facts/s3.md#s3-versioning-delete-with-version-id-permanent)
s3-versioning-every-version-billed
  claim: Normal S3 rates apply to every version of an object that is stored or requested, so an overwritten object's older version keeps costing storage until it is deleted.
  scope: per versioning-enabled bucket.
  link: [apply for every version of an object](../facts/s3.md#s3-versioning-every-version-billed)
s3-versioning-get-delete-marker-404
  claim: After a delete in a versioned bucket, the delete marker is the current version; a plain GET returns a 404 Not Found error, but a GET that names an older version ID still returns that version.
  scope: per versioning-enabled bucket.
  link: [404 Not Found](../facts/s3.md#s3-versioning-get-delete-marker-404)
  link: [The delete marker becomes the current version](../facts/s3.md#s3-versioning-get-delete-marker-404)
s3-versioning-never-back-to-unversioned
  claim: Versioning is enabled and suspended at the bucket level. After a bucket is version-enabled it can never return to an unversioned state; it can only be suspended.
  scope: per bucket.
  link: [can never return to an unversioned state](../facts/s3.md#s3-versioning-never-back-to-unversioned)
  link: [you can *suspend* versioning on that bucket](../facts/s3.md#s3-versioning-never-back-to-unversioned)
s3-versioning-new-version-only-on-put
  claim: New object versions are created only when a new object is PUT (CopyObject also works through a PUT); changing the tags on an object does not create a new version.
  scope: per versioning-enabled bucket.
  link: [don't create a new version](../facts/s3.md#s3-versioning-new-version-only-on-put)
  link: [changing the tags on an object](../facts/s3.md#s3-versioning-new-version-only-on-put)
s3-versioning-off-by-default
  claim: S3 Versioning is disabled on buckets by default and must be explicitly enabled.
  scope: per general purpose bucket; default; not adjustable.
  link: [S3 Versioning is disabled on buckets](../facts/s3.md#s3-versioning-off-by-default)
  link: [you must explicitly enable it](../facts/s3.md#s3-versioning-off-by-default)
s3-versioning-preserves-on-overwrite-and-delete
  claim: Once versioning is enabled, S3 keeps the existing object whenever you PUT, POST, COPY or DELETE it. After a DELETE, simple un-versioned requests no longer return the object, but every version is still preserved and can be retrieved or restored, and only the bucket owner can permanently delete a version.
  scope: per versioning-enabled bucket.
  link: [preserves existing objects anytime you perform a PUT](../facts/s3.md#s3-versioning-preserves-on-overwrite-and-delete)
  link: [can be retrieved or restored](../facts/s3.md#s3-versioning-preserves-on-overwrite-and-delete)
  link: [Only the owner of an Amazon S3 bucket](../facts/s3.md#s3-versioning-preserves-on-overwrite-and-delete)
  link: [the most recently written version](../facts/s3.md#s3-versioning-preserves-on-overwrite-and-delete)
s3-versioning-rollback-window-with-lifecycle
  claim: You can use S3 Lifecycle rules together with S3 Versioning to implement a rollback window; for example, you can delete noncurrent versions of an object after five days when there are at least two newer versions, and you can change the number of days or the number of newer versions.
  scope: per versioning-enabled bucket.
  link: [implement a rollback window](../facts/s3.md#s3-versioning-rollback-window-with-lifecycle)
  link: [at least two newer versions of the object](../facts/s3.md#s3-versioning-rollback-window-with-lifecycle)
s3-versioning-suspend-keeps-existing-versions
  claim: Suspending versioning stops new versions from accruing; existing objects and versions in the bucket do not change, only how S3 handles future requests.
  scope: per bucket.
  link: [existing objects in your bucket do not change](../facts/s3.md#s3-versioning-suspend-keeps-existing-versions)
  link: [stop accruing new versions](../facts/s3.md#s3-versioning-suspend-keeps-existing-versions)
s3-versioning-three-states-all-objects
  claim: The versioning state of a bucket (unversioned, versioning-enabled or versioning-suspended) applies to all objects in the bucket, never to only some of them.
  scope: per bucket.
  link: [applies to all (never some) of the objects](../facts/s3.md#s3-versioning-three-states-all-objects)
s3-vpc-endpoint-keeps-traffic-off-internet
  claim: A VPC endpoint for S3 is a logical entity inside a VPC that connects only to S3, so traffic does not cross the open internet; bucket policies can restrict access to a given VPC or endpoint, and a VPC without an internet gateway limits data exfiltration.
  scope: per VPC endpoint and per bucket policy.
  link: [help prevent traffic from traversing the open internet](../facts/s3.md#s3-vpc-endpoint-keeps-traffic-off-internet)
  link: [control which VPCs or VPC endpoints have access](../facts/s3.md#s3-vpc-endpoint-keeps-traffic-off-internet)
  link: [help prevent data exfiltration](../facts/s3.md#s3-vpc-endpoint-keeps-traffic-off-internet)
s3-vpc-endpoint-private-connection
  claim: A VPC endpoint for S3 is a logical entity inside a VPC that allows connectivity only to S3 and needs no internet, VPN, NAT instance or Direct Connect path; it changes only how requests are routed, and public S3 endpoints keep working.
  scope: per VPC endpoint.
  link: [doesn't require access over the internet](../facts/s3.md#s3-vpc-endpoint-private-connection)
  link: [VPC endpoints change only how requests are routed](../facts/s3.md#s3-vpc-endpoint-private-connection)
  link: [allows connectivity only to Amazon S3](../facts/s3.md#s3-vpc-endpoint-private-connection)
s3-vs-block-storage-direct-attached
  claim: Block storage offers high-performance storage that is direct-attached to a compute instance with low-latency access, which suits applications that require fast and consistent I/O operations.
  scope: block storage, compared with object and file storage.
  link: [direct-attached to a compute instance](../facts/s3.md#s3-vs-block-storage-direct-attached)
  link: [fast and consistent I/O operations](../facts/s3.md#s3-vs-block-storage-direct-attached)
s3-vs-file-storage-shared-mount
  claim: File-based storage is natively mountable from virtually any operating system using industry-standard protocols like NFS and SMB, and provides simple storage for workloads that need access to shared data across multiple compute instances.
  scope: file-based storage, compared with object and block storage.
  link: [industry-standard protocols like NFS and SMB](../facts/s3.md#s3-vs-file-storage-shared-mount)
  link: [shared data across multiple compute instances](../facts/s3.md#s3-vs-file-storage-shared-mount)
s3-war-avoid-public-buckets-use-cloudfront
  claim: Well-Architected guidance: review bucket policies regularly, avoid publicly readable or writable buckets unless absolutely necessary, detect public buckets with AWS Config, and serve content from S3 through Amazon CloudFront.
  scope: S3 bucket policies.
  link: [Avoid using publicly readable or writeable buckets](../facts/s3.md#s3-war-avoid-public-buckets-use-cloudfront)
  link: [Amazon CloudFront to serve content from Amazon S3](../facts/s3.md#s3-war-avoid-public-buckets-use-cloudfront)
s3-war-customer-managed-keys-for-sensitive-data
  claim: Well-Architected guidance: AWS-managed and service-controlled KMS keys are used on your behalf by AWS; for sensitive data that needs fine-grained control of the key, use customer managed keys, which you fully control including rotation and key policies.
  scope: AWS KMS keys used for S3 server-side encryption.
  link: [requires fine-grained access to the underlying encryption key](../facts/s3.md#s3-war-customer-managed-keys-for-sensitive-data)
  link: [full control over CMKs, including rotation](../facts/s3.md#s3-war-customer-managed-keys-for-sensitive-data)
s3-war-encrypts-new-objects-by-default
  claim: The Well-Architected security pillar notes that Amazon S3 now encrypts all new objects by default, with no impact on performance.
  scope: all new S3 objects; default.
  link: [now encrypt all new objects by default](../facts/s3.md#s3-war-encrypts-new-objects-by-default)
  link: [no impact on performance](../facts/s3.md#s3-war-encrypts-new-objects-by-default)
s3-war-iam-access-analyzer-external-access
  claim: IAM Access Analyzer can analyze S3 buckets and raise a finding when a bucket policy grants access to an external entity.
  scope: per account or organization.
  link: [grants access to an external entity](../facts/s3.md#s3-war-iam-access-analyzer-external-access)
s3-war-keys-mapped-to-data-classification
  claim: Well-Architected guidance: map encryption keys to data classifications, for example one KMS key for production data and another for development or test data, instead of one key for everything.
  scope: AWS KMS keys.
  link: [Map encryption keys to data classifications](../facts/s3.md#s3-war-keys-mapped-to-data-classification)
  link: [one AWS KMS key for encrypting production data](../facts/s3.md#s3-war-keys-mapped-to-data-classification)
s3-war-object-lock-even-root-user
  claim: Well-Architected guidance: S3 Object Lock gives mandatory access control that prevents objects from being deleted or overwritten, even by the root user, until the lock expires; Amazon Glacier Vault Lock does the same for Glacier vault archives.
  scope: locked object versions; until the lock expires.
  link: [even by the root user](../facts/s3.md#s3-war-object-lock-even-root-user)
  link: [Amazon Glacier Vault Lock](../facts/s3.md#s3-war-object-lock-even-root-user)
s3-war-s3-inventory-audits-replication-encryption
  claim: S3 Inventory audits and reports the replication and encryption status of objects, for business, compliance and regulatory needs.
  scope: per bucket.
  link: [the replication and encryption status of your objects](../facts/s3.md#s3-war-s3-inventory-audits-replication-encryption)
s3-war-separate-accounts-per-classification
  claim: Well-Architected guidance: separate data of different classification levels into distinct AWS accounts managed with AWS Organizations, to isolate it and lower the risk of exposure.
  scope: data classification levels.
  link: [distinct AWS accounts for each level](../facts/s3.md#s3-war-separate-accounts-per-classification)
s3-website-content-must-be-public
  claim: For a public website, you must make all your content publicly readable so that customers can access it at the S3 website endpoint; the website endpoint supports only publicly readable content, while the REST API endpoint supports both public and private content.
  scope: S3 website endpoint.
  link: [make all your content publicly readable](../facts/s3.md#s3-website-content-must-be-public)
s3-website-endpoint-no-https
  claim: S3 website endpoints do not support HTTPS or access points; AWS names Amazon CloudFront in front of the bucket as a way to serve the static website over HTTPS.
  scope: S3 website endpoints.
  link: [do not support HTTPS or access points](../facts/s3.md#s3-website-endpoint-no-https)
  link: [Use Amazon CloudFront](../facts/s3.md#s3-website-endpoint-no-https)
s3-website-endpoint-regional
  claim: A bucket configured as a static website is served at the Region-specific website endpoint of the bucket, which is different from the REST API endpoint.
  scope: S3 website endpoints.
  link: [AWS Region-specific website endpoint of the bucket](../facts/s3.md#s3-website-endpoint-regional)
  link: [Website endpoints are different](../facts/s3.md#s3-website-endpoint-regional)
s3-website-requester-pays-403
  claim: Requester Pays buckets do not allow access through a website endpoint; any such request receives a 403 Access Denied response.
  scope: S3 website endpoints.
  link: [403 Access Denied](../facts/s3.md#s3-website-requester-pays-403)
  link: [do not allow access through a website endpoint](../facts/s3.md#s3-website-requester-pays-403)
s3-website-sse-kms-needs-cloudfront-oac
  claim: A static website bucket encrypted with SSE-KMS must be served through a CloudFront distribution, because SSE-KMS does not support anonymous users; the distribution must use origin access control (OAC), since OAI does not support SSE-KMS.
  scope: static website buckets using SSE-KMS.
  link: [SSE-KMS doesn't support anonymous users](../facts/s3.md#s3-website-sse-kms-needs-cloudfront-oac)
  link: [you must use OAC instead](../facts/s3.md#s3-website-sse-kms-needs-cloudfront-oac)
