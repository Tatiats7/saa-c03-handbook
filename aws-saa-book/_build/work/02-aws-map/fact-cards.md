facts card: 310 facts
aws-cli-account-based-endpoints-v2-2025-03
  claim: Account-based endpoints that use your AWS account ID have been supported in the AWS CLI version 2 since March 20, 2025.
  scope: AWS CLI version 2.
  link: [March 20, 2025](../facts/aws-cli.md#aws-cli-account-based-endpoints-v2-2025-03)
aws-cli-credential-precedence-command-line-env-then-files
  claim: CLI settings take precedence in a fixed order: command line options first, then environment variables, then assumed roles, IAM Identity Center, the credentials file, a custom process, the config file, container credentials and finally EC2 instance profile credentials.
  link: [Command line options](../facts/aws-cli.md#aws-cli-credential-precedence-command-line-env-then-files)
  link: [Environment variables](../facts/aws-cli.md#aws-cli-credential-precedence-command-line-env-then-files)
  link: [Credentials file](../facts/aws-cli.md#aws-cli-credential-precedence-command-line-env-then-files)
  link: [Amazon EC2 instance profile credentials](../facts/aws-cli.md#aws-cli-credential-precedence-command-line-env-then-files)
aws-cli-credentials-and-config-files-in-dot-aws
  claim: The AWS CLI stores the credentials you enter with aws configure in a file named credentials, and the less sensitive settings in a file named config, both in the .aws folder in your home directory.
  scope: AWS CLI configuration.
  link: [.aws folder in your home directory](../facts/aws-cli.md#aws-cli-credentials-and-config-files-in-dot-aws)
aws-cli-credentials-file-wins-over-config-file
  claim: If a profile with the same name has credentials in both the credentials file and the config file, the keys in the credentials file take precedence.
  scope: AWS CLI configuration.
  link: [the keys in the credentials file take precedence](../facts/aws-cli.md#aws-cli-credentials-file-wins-over-config-file)
aws-cli-default-profile-named-default
  claim: By default the AWS CLI uses the settings of the profile named default; to use other settings you create and reference additional named profiles.
  scope: AWS CLI configuration; default; adjustable.
  link: [profile named `default`](../facts/aws-cli.md#aws-cli-default-profile-named-default)
aws-cli-definition-open-source-command-line-tool
  claim: The AWS CLI is an open source tool for interacting with AWS services through commands in your shell; with minimal configuration it runs commands equivalent to the functionality of the console.
  link: [an open source tool that enables you to interact with AWS services using commands in your command-line shell](../facts/aws-cli.md#aws-cli-definition-open-source-command-line-tool)
  link: [functionality equivalent to that provided by the browser-based AWS Management Console](../facts/aws-cli.md#aws-cli-definition-open-source-command-line-tool)
  say: the CLI does from a terminal what the console does in a browser
aws-cli-ec2-instance-metadata-role-credentials
  claim: When the CLI runs on an EC2 instance with an IAM role attached, it automatically and securely retrieves temporary credentials from the instance metadata.
  link: [the AWS CLI automatically and securely retrieves the credentials from the instance metadata](../facts/aws-cli.md#aws-cli-ec2-instance-metadata-role-credentials)
  link: [metadata that the AWS CLI can directly query for temporary credentials](../facts/aws-cli.md#aws-cli-ec2-instance-metadata-role-credentials)
  say: on EC2, attach a role; the CLI reads temporary credentials from instance metadata
aws-cli-iaas-functions-available-within-180-days
  claim: All IaaS administration, management and access functions of the console are available in the AWS API and CLI, and new IaaS features and services get full console functionality through the API and CLI at launch or within 180 days.
  link: [available in the AWS API and AWS CLI](../facts/aws-cli.md#aws-cli-iaas-functions-available-within-180-days)
  link: [at launch or within 180 days of launch](../facts/aws-cli.md#aws-cli-iaas-functions-available-within-180-days)
aws-cli-long-term-iam-user-credentials-not-recommended
  claim: IAM user long-term credentials, which have no expiration, are not recommended for the CLI; storing credentials outside the CLI is also not recommended because it is only as secure as that location.
  link: [(Not recommended) Use long-term credentials, which have no expiration](../facts/aws-cli.md#aws-cli-long-term-iam-user-credentials-not-recommended)
  link: [This method is only as secure as the external location the credentials are stored](../facts/aws-cli.md#aws-cli-long-term-iam-user-credentials-not-recommended)
  say: long-term access keys never expire, so AWS does not recommend them
aws-cli-one-tool-multiple-services-scripts
  claim: With one tool to download and configure, the AWS CLI controls multiple AWS services from the command line and automates them through scripts.
  link: [control multiple AWS services from the command line and automate them through scripts](../facts/aws-cli.md#aws-cli-one-tool-multiple-services-scripts)
  link: [just one tool to download and configure](../facts/aws-cli.md#aws-cli-one-tool-multiple-services-scripts)
aws-cli-output-option-overrides-env-and-config
  claim: The --output option on a command sets the output format for that one command only and overrides any environment variable or config file value; the AWS_DEFAULT_OUTPUT environment variable in turn overrides the config file.
  scope: AWS CLI output format.
  link: [overrides any currently set environment variable or the value in the `config` file](../facts/aws-cli.md#aws-cli-output-option-overrides-env-and-config)
aws-cli-profile-prefix-only-in-config-file
  claim: In the config file a named profile section is written [profile name], but in the credentials file the word profile is left out.
  scope: AWS CLI configuration.
  link: [do not include it in the `credentials` file](../facts/aws-cli.md#aws-cli-profile-prefix-only-in-config-file)
aws-cli-recommended-short-term-console-credentials
  claim: If you use root, IAM users, or federation with IAM for AWS account access, AWS recommends short-term credentials obtained by logging in to the CLI with your console credentials; IAM Identity Center workforce users also use short-term credentials, and security best practice is AWS Organizations with IAM Identity Center.
  scope: the console-credentials recommendation applies if you use root, IAM users, or federation with IAM for AWS account access.
  link: [Use short-term credentials by logging into the AWS CLI with your console credentials](../facts/aws-cli.md#aws-cli-recommended-short-term-console-credentials)
  link: [Security best practice is to use AWS Organizations with IAM Identity Center](../facts/aws-cli.md#aws-cli-recommended-short-term-console-credentials)
  say: log in to the CLI with your console credentials to get short-term credentials
aws-cli-temporary-portal-credentials-max-twelve-hours
  claim: Temporary credentials copied from the AWS access portal are valid for as long as the chosen IAM role's session settings allow, with a maximum duration of twelve hours, and must be copied again when they expire.
  scope: temporary credentials copied from the AWS access portal into the credentials file; maximum; not adjustable.
  link: [The maximum duration is twelve hours](../facts/aws-cli.md#aws-cli-temporary-portal-credentials-max-twelve-hours)
  link: [twelve hours](../facts/aws-cli.md#aws-cli-temporary-portal-credentials-max-twelve-hours)
aws-cli-version-2-current-major-version
  claim: AWS CLI version 2 is the most recent major version and supports all the latest features; some version 2 features are not backported to version 1, and version 2 has breaking changes from version 1.
  link: [The AWS CLI version 2 is the most recent major version of the AWS CLI](../facts/aws-cli.md#aws-cli-version-2-current-major-version)
  link: [Some features introduced in version 2 are not backported to version 1](../facts/aws-cli.md#aws-cli-version-2-current-major-version)
aws-cli-yaml-stream-output-for-large-data
  claim: The yaml-stream output format streams the output as YAML, which allows faster handling of large data types.
  scope: AWS CLI output format.
  link: [faster handling of large data types](../facts/aws-cli.md#aws-cli-yaml-stream-output-for-large-data)
global-infrastructure-account-type-cannot-reach-other-partition-regions
  claim: You cannot describe or access the Regions of one account type from another: a standard AWS account cannot reach the AWS GovCloud (US) Regions or the China Regions.
  scope: account types (AWS, AWS GovCloud (US), Amazon AWS (China)).
  link: [You can't describe or access the Regions of one type of account from another](../facts/global-infrastructure.md#global-infrastructure-account-type-cannot-reach-other-partition-regions)
  link: [you can't access the AWS GovCloud (US) Regions or the China Regions from an AWS account](../facts/global-infrastructure.md#global-infrastructure-account-type-cannot-reach-other-partition-regions)
  say: a standard account cannot reach GovCloud or China Regions
global-infrastructure-async-cross-region-replication-may-lose-data
  claim: When you use an AWS datastore that is replicated asynchronously across Regions, a failover between Regions can lose data or leave data inconsistent.
  link: [the possibility of data loss or inconsistency when you fail over](../facts/global-infrastructure.md#global-infrastructure-async-cross-region-replication-may-lose-data)
  link: [asynchronously replicated datastore](../facts/global-infrastructure.md#global-infrastructure-async-cross-region-replication-may-lose-data)
global-infrastructure-auto-scaling-relies-on-ec2-control-plane
  claim: Launching new EC2 instances through Auto Scaling takes time and relies on the EC2 control plane, so the remaining capacity could be overwhelmed while replacements start.
  link: [deploying new instances through auto scaling relies on the EC2 control plane](../facts/global-infrastructure.md#global-infrastructure-auto-scaling-relies-on-ec2-control-plane)
  link: [launching new EC2 instances takes time](../facts/global-infrastructure.md#global-infrastructure-auto-scaling-relies-on-ec2-control-plane)
global-infrastructure-az-code-is-region-code-plus-letter
  claim: The code of an Availability Zone is its Region code followed by a letter, for example us-east-2a, us-east-2b and us-east-2c in the us-east-2 Region.
  scope: Availability Zone codes.
  link: [its Region code followed by a letter identifier](../facts/global-infrastructure.md#global-infrastructure-az-code-is-region-code-plus-letter)
  say: the Region code followed by a letter
global-infrastructure-az-definition-discrete-data-centers
  claim: An Availability Zone is one or more discrete data centers, each with redundant power, networking and connectivity, housed in separate facilities, so that a fire, tornado or flood affects only a single Availability Zone.
  scope: Availability Zones.
  link: [one or more discrete data centers, each with redundant power, networking, and connectivity, and housed in separate facilities](../facts/global-infrastructure.md#global-infrastructure-az-definition-discrete-data-centers)
  link: [only a single Availability Zone would be affected](../facts/global-infrastructure.md#global-infrastructure-az-definition-discrete-data-centers)
  say: an Availability Zone is one or more separate data centers with their own redundant power, networking and connectivity
global-infrastructure-az-deployments-separated-in-time
  claim: When AWS deploys updates to its own services, the deployments to the Availability Zones of one Region are separated in time, so that a bad deployment does not fail every zone at once.
  scope: AWS service deployments.
  link: [deployments to Availability Zones in the same Region are separated in time](../facts/global-infrastructure.md#global-infrastructure-az-deployments-separated-in-time)
  say: AWS rolls its updates out to one zone at a time
global-infrastructure-az-distance-within-100-km
  claim: The Availability Zones of a Region are many kilometers apart from each other, but all are within 100 km (60 miles) of each other.
  scope: Availability Zones of one Region; maximum.
  link: [within 100 km (60 miles) of each other](../facts/global-infrastructure.md#global-infrastructure-az-distance-within-100-km)
  link: [within 100 km](../facts/global-infrastructure.md#global-infrastructure-az-distance-within-100-km)
  say: within one hundred kilometers, about sixty miles, of each other
global-infrastructure-az-id-same-physical-location-every-account
  claim: An AZ ID (for example use1-az2) names the same physical location in every AWS account, so a subnet shared with another account appears there in the zone with the same AZ ID.
  scope: AZ IDs.
  link: [the same physical location in every AWS account](../facts/global-infrastructure.md#global-infrastructure-az-id-same-physical-location-every-account)
  link: [a Region-specific prefix, followed by -az, followed by a number](../facts/global-infrastructure.md#global-infrastructure-az-id-same-physical-location-every-account)
  link: [this subnet is available to that account in the Availability Zone whose AZ ID is also `use1-az2`](../facts/global-infrastructure.md#global-infrastructure-az-id-same-physical-location-every-account)
  say: an AZ ID is the same physical zone in every account
global-infrastructure-az-independence-azi
  claim: AWS calls the strong isolation of Availability Zones from each other Availability Zone Independence (AZI).
  scope: Availability Zones.
  link: [Availability Zone Independence (AZI)](../facts/global-infrastructure.md#global-infrastructure-az-independence-azi)
  say: Availability Zone Independence, A Z I
global-infrastructure-az-interconnect-metro-fiber
  claim: The Availability Zones of a Region are connected through low-latency, high-bandwidth, highly redundant networking over dedicated metro fiber.
  scope: Availability Zones of one Region.
  link: [low-latency, high-bandwidth, highly-redundant networking, over dedicated metro fiber](../facts/global-infrastructure.md#global-infrastructure-az-interconnect-metro-fiber)
  link: [dedicated metro fiber](../facts/global-infrastructure.md#global-infrastructure-az-interconnect-metro-fiber)
  say: low-latency, high-bandwidth, highly redundant networking over dedicated metro fiber
global-infrastructure-az-latency-single-digit-ms
  claim: Availability Zones in the same Region are close enough for high-throughput, low-latency networking with single-digit millisecond latency, so data can be replicated synchronously between them.
  scope: Availability Zones of one Region.
  link: [single-digit millisecond](../facts/global-infrastructure.md#global-infrastructure-az-latency-single-digit-ms)
  link: [replicate data synchronously between Availability Zones](../facts/global-infrastructure.md#global-infrastructure-az-latency-single-digit-ms)
  say: single-digit millisecond latency between Availability Zones
global-infrastructure-az-name-mapping-independent-per-account
  claim: For accounts created before November 2025, in the oldest Regions, AWS maps Availability Zone names to physical zones independently per account, so us-east-1a in your account might not be the same physical location as us-east-1a in another account; accounts created from November 2025 get the same mapping.
  scope: Availability Zone names in the oldest Regions; accounts created before November 2025.
  link: [we independently map Availability Zones to codes for each AWS account](../facts/global-infrastructure.md#global-infrastructure-az-name-mapping-independent-per-account)
  link: [might not be the same physical location as it is in another account](../facts/global-infrastructure.md#global-infrastructure-az-name-mapping-independent-per-account)
  link: [Accounts created starting November 2025, get the same Availability Zones mapped to codes](../facts/global-infrastructure.md#global-infrastructure-az-name-mapping-independent-per-account)
  say: zone names are mapped to physical zones separately per account
  changed: 2025-11: was we independently map Availability Zones to codes for each AWS account
global-infrastructure-az-no-shared-fate
  claim: Availability Zones are designed not to be hit at the same time by one shared-fate event such as utility power loss, water disruption, fiber isolation, earthquakes, fires, tornadoes or floods, and their generators and cooling are not shared.
  scope: Availability Zones within one Region.
  link: [designed not to be simultaneously impacted by a shared fate scenario](../facts/global-infrastructure.md#global-infrastructure-az-no-shared-fate)
  link: [utility power, water disruption, fiber isolation, earthquakes, fires, tornadoes, or floods](../facts/global-infrastructure.md#global-infrastructure-az-no-shared-fate)
  say: zones are designed not to fail together from one shared event
global-infrastructure-cloud-computing-definition
  claim: Cloud computing is the on-demand delivery of compute power, database, storage, applications and other IT resources through a cloud services platform over the internet with pay-as-you-go pricing.
  link: [on-demand delivery of compute power, database, storage, applications, and other IT resources](../facts/global-infrastructure.md#global-infrastructure-cloud-computing-definition)
  link: [pay-as-you-go pricing](../facts/global-infrastructure.md#global-infrastructure-cloud-computing-definition)
global-infrastructure-cloudfront-content-served-during-control-plane-impairment
  claim: During a CloudFront control plane impairment the CRUDL operations, including invalidations, may not work, but content continues to be cached and served and origin failovers continue to work.
  link: [your content will continue to be cached and served](../facts/global-infrastructure.md#global-infrastructure-cloudfront-content-served-during-control-plane-impairment)
  link: [origin failovers will continue to work](../facts/global-infrastructure.md#global-infrastructure-cloudfront-content-served-during-control-plane-impairment)
global-infrastructure-constrained-az-count-differs
  claim: AWS can restrict new zonal resources in a constrained Availability Zone and can remove it from the list for new accounts, so your account can see a different number of Availability Zones in a Region than another account does.
  scope: per account, per Region; constrained Availability Zones only.
  link: [a different number of available Availability Zones in a Region than another account does](../facts/global-infrastructure.md#global-infrastructure-constrained-az-count-differs)
  say: a constrained Availability Zone can be hidden from new accounts, so the count differs per account
global-infrastructure-control-plane-definition-crudl
  claim: A control plane provides the administrative APIs that create, read or describe, update, delete and list (CRUDL) resources; launching an EC2 instance, creating an S3 bucket and describing an SQS queue are control plane actions.
  link: [create, read/describe, update, delete, and list (CRUDL) resources](../facts/global-infrastructure.md#global-infrastructure-control-plane-definition-crudl)
  link: [launching a new Amazon Elastic Compute Cloud (Amazon EC2) instance](../facts/global-infrastructure.md#global-infrastructure-control-plane-definition-crudl)
  say: the control plane is the set of APIs that create, change and delete resources
global-infrastructure-cross-region-features-same-partition-only
  claim: Cross-Region features such as Amazon S3 Cross-Region Replication or AWS Transit Gateway inter-Region peering are supported only between Regions in the same partition, and IAM credentials from one partition cannot be used with resources in another partition.
  scope: cross-Region features and IAM credentials across partitions.
  link: [only supported between Regions in the same partition](../facts/global-infrastructure.md#global-infrastructure-cross-region-features-same-partition-only)
  link: [cannot use IAM credentials from one partition to interact with resources in a different partition](../facts/global-infrastructure.md#global-infrastructure-cross-region-features-same-partition-only)
global-infrastructure-customer-content-stays-in-chosen-region
  claim: AWS services process and store customer content in the Region or Regions where the customer uses the services; the named global services (IAM, Organizations, CloudFront, Route53, Global Accelerator, Direct Connect, Firewall Manager, WAF, Shield) may store and process data globally.
  scope: customer content; except the listed global services.
  link: [process and store customer content in the AWS region(s) where the services are used by the customer](../facts/global-infrastructure.md#global-infrastructure-customer-content-stays-in-chosen-region)
  link: [may store and process data globally](../facts/global-infrastructure.md#global-infrastructure-customer-content-stays-in-chosen-region)
  say: customer content stays in the Region where you use the service
global-infrastructure-data-plane-definition-primary-function
  claim: The data plane provides the primary function of a service: the running EC2 instance, reads and writes to an EBS volume, gets and puts to an S3 bucket, and Route 53 answering DNS queries and running health checks.
  link: [provides the primary function of the service](../facts/global-infrastructure.md#global-infrastructure-data-plane-definition-primary-function)
  link: [Route 53 answering DNS queries and performing health checks](../facts/global-infrastructure.md#global-infrastructure-data-plane-definition-primary-function)
  say: the data plane is the service doing its real job
global-infrastructure-data-plane-fails-less-often-than-control-plane
  claim: Data planes are deliberately simpler than control planes, so failures are statistically less likely in the data plane than in the control plane.
  link: [statistically less likely to occur in the data plane versus the control plane](../facts/global-infrastructure.md#global-infrastructure-data-plane-fails-less-often-than-control-plane)
  link: [fewer moving parts compared to control planes](../facts/global-infrastructure.md#global-infrastructure-data-plane-fails-less-often-than-control-plane)
global-infrastructure-do-not-rely-on-global-control-planes-in-recovery
  claim: AWS recommends not relying on the control planes of partitional or edge network global services in a recovery path and relying on their data plane operations instead.
  link: [Do not rely on the control planes of partitional services in your recovery path](../facts/global-infrastructure.md#global-infrastructure-do-not-rely-on-global-control-planes-in-recovery)
  link: [rely on the data plane operations of these services](../facts/global-infrastructure.md#global-infrastructure-do-not-rely-on-global-control-planes-in-recovery)
  say: recover with data plane actions, not with control plane calls
global-infrastructure-each-pop-isolated
  claim: Each point of presence is isolated from the others, so a failure that affects one PoP or one metropolitan area does not affect the rest of the global edge network.
  link: [Each PoP is isolated from the others](../facts/global-infrastructure.md#global-infrastructure-each-pop-isolated)
  link: [a failure affecting a single PoP or metropolitan area does not impact the rest of the global network](../facts/global-infrastructure.md#global-infrastructure-each-pop-isolated)
global-infrastructure-ec2-instance-runs-without-control-plane
  claim: A launched EC2 instance does not depend on any control plane API to keep running or to start again after a reboot; the same holds for VPCs, S3 buckets and objects, and EBS volumes.
  link: [does not depend on any control plane APIs in order to stay running](../facts/global-infrastructure.md#global-infrastructure-ec2-instance-runs-without-control-plane)
  link: [VPCs, Amazon S3 buckets and objects, and Amazon EBS volumes](../facts/global-infrastructure.md#global-infrastructure-ec2-instance-runs-without-control-plane)
global-infrastructure-edge-location-services
  claim: Amazon CloudFront, Amazon Route 53, AWS Firewall Manager, AWS Shield and AWS WAF are provided through AWS edge locations.
  scope: AWS edge locations.
  link: [Amazon CloudFront, Amazon Route 53, AWS Firewall Manager, AWS Shield, and AWS WAF services are provided through AWS Edge Locations](../facts/global-infrastructure.md#global-infrastructure-edge-location-services)
  say: CloudFront, Route 53, Firewall Manager, Shield and WAF are provided through the edge locations
global-infrastructure-edge-locations-connected-to-regions-by-backbone
  claim: Edge locations connect to the Regions through the AWS network backbone, a fully redundant, multiple 100GbE parallel fiber that circles the globe.
  link: [connected to the AWS Regions through the AWS network backbone](../facts/global-infrastructure.md#global-infrastructure-edge-locations-connected-to-regions-by-backbone)
  link: [multiple 100GbE parallel fiber](../facts/global-infrastructure.md#global-infrastructure-edge-locations-connected-to-regions-by-backbone)
global-infrastructure-edge-network-global-services-route53-example
  claim: Edge network global services keep their control plane in the aws partition and run their data planes in the points of presence; Route 53, for example, has its control plane in us-east-1 and a data plane spread across hundreds of PoPs and every Region.
  link: [host their data planes in the global points of presence (PoP) infrastructure](../facts/global-infrastructure.md#global-infrastructure-edge-network-global-services-route53-example)
  link: [Route 53 operates its control plane in the us-east-1 Region, but its data plane is distributed across hundreds of PoPs globally](../facts/global-infrastructure.md#global-infrastructure-edge-network-global-services-route53-example)
global-infrastructure-existing-resources-survive-control-plane-impairment
  claim: Once a resource is provisioned, data plane access to it has no dependency on the control plane, so even when creating, modifying or deleting resources is impaired, existing resources remain available.
  link: [existing resources remain available](../facts/global-infrastructure.md#global-infrastructure-existing-resources-survive-control-plane-impairment)
  link: [has no dependency on the control plane](../facts/global-infrastructure.md#global-infrastructure-existing-resources-survive-control-plane-impairment)
global-infrastructure-faq-dedicated-local-zones-exclusive-use
  claim: Dedicated Local Zones are Local Zones built for the exclusive use of one customer or community; they offer the same benefits as Local Zones, and AWS also works with the customer to provide the security and compliance features that customer needs on its own private zones.
  link: [built for the exclusive use by a customer or community](../facts/global-infrastructure.md#global-infrastructure-faq-dedicated-local-zones-exclusive-use)
  say: a Dedicated Local Zone is built for one customer or community only
global-infrastructure-faq-local-zone-parent-availability-zone-control-plane
  claim: Each Local Zone is associated with one specific Availability Zone in its parent Region, and that parent Availability Zone handles certain control plane operations for the Local Zone, such as API calls.
  link: [associated with a specific Availability Zone in its parent Region](../facts/global-infrastructure.md#global-infrastructure-faq-local-zone-parent-availability-zone-control-plane)
  link: [handles certain control plane operations for the Local Zone, such as API calls](../facts/global-infrastructure.md#global-infrastructure-faq-local-zone-parent-availability-zone-control-plane)
  say: every Local Zone has a parent Availability Zone in its parent Region
global-infrastructure-faq-local-zones-and-azs-both-support-high-availability
  claim: Both Local Zones and Availability Zones can be used to build applications for high availability.
  link: [Both Local Zones and Availability Zones allow you to build applications for high availability](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-and-azs-both-support-high-availability)
global-infrastructure-faq-local-zones-connected-to-parent-region-private-network
  claim: A Local Zone is connected to its parent Region over the redundant, very high-bandwidth AWS private network, so applications in the Local Zone get fast, secure, seamless access to the rest of AWS services.
  link: [connected to the parent Region using the Amazon redundant and very high-bandwidth private network](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-connected-to-parent-region-private-network)
global-infrastructure-faq-local-zones-connectivity-direct-connect-and-internet
  claim: You can connect to Local Zones over AWS Direct Connect and over the internet.
  link: [over AWS Direct Connect and over the Internet](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-connectivity-direct-connect-and-internet)
global-infrastructure-faq-local-zones-data-residency-local-storage-services
  claim: As with Regions, you keep control over where data placed in a Local Zone is stored and how it is secured; by using local storage services such as Amazon EBS and Amazon FSx you can keep data inside specific Local Zones to meet data residency requirements.
  link: [you maintain control over the data you place in Local Zones](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-data-residency-local-storage-services)
  link: [you can ensure your data stays in specific Local Zones](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-data-residency-local-storage-services)
  say: you control where data in a Local Zone is stored
global-infrastructure-faq-local-zones-ec2-pricing-models
  claim: There are three ways to pay for Amazon EC2 instances in Local Zones: On-Demand, Savings Plans and Spot Instances.
  link: [On-Demand, Savings Plans, and Spot Instances](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-ec2-pricing-models)
  say: On-Demand, Savings Plans and Spot
global-infrastructure-faq-local-zones-extend-vpc-with-subnet
  claim: You extend a VPC from the parent Region into a Local Zone by creating a new subnet and assigning it to the Local Zone; the VPC then treats that subnet like a subnet in any other Availability Zone.
  link: [creating a new subnet and assigning it to the Local Zone](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-extend-vpc-with-subnet)
  say: you create a subnet in the Local Zone and the VPC extends there
global-infrastructure-faq-local-zones-kms-from-parent-region
  claim: You can use AWS KMS from a Local Zone; services that support KMS in Local Zones encrypt data with customer managed keys, AWS managed keys or an external key store from the parent Region.
  link: [you can use AWS Key Management Service (KMS) from a Local Zone](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-kms-from-parent-region)
  say: yes, KMS works from a Local Zone
global-infrastructure-faq-local-zones-must-be-enabled-per-account-first
  claim: Local Zones are reached through the API endpoint and Management Console of their parent Region, and you must first enable a Local Zone for your AWS account before you can deploy resources to it; once enabled it appears alongside the other Availability Zones.
  scope: Local Zones, per AWS account.
  link: [you must first enable the Local Zones for your AWS account before you can deploy resources to them](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-must-be-enabled-per-account-first)
  link: [accessible from API Endpoint and the AWS Management Console of their parent Region](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-must-be-enabled-per-account-first)
  say: you must enable a Local Zone for your account before you can use it
global-infrastructure-faq-local-zones-own-internet-connection-and-direct-connect
  claim: Local Zones have their own connection to the internet and support AWS Direct Connect, so resources in a Local Zone can serve local end users with very low-latency communications.
  link: [their own connection to the internet and support AWS Direct Connect](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-own-internet-connection-and-direct-connect)
global-infrastructure-faq-local-zones-regional-services-reached-privately-via-vpc
  claim: In a Local Zone, services such as Amazon EC2, EBS and VPC are locally available and can serve nearby end users with extremely low latency, while other AWS services such as Amazon S3 and Amazon Aurora are accessible privately through the VPC over the AWS private network.
  link: [accessible privately through VPC over AWS private network](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-regional-services-reached-privately-via-vpc)
  link: [locally available and can be used to serve end users in geographic proximity with extremely low latency](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-regional-services-reached-privately-via-vpc)
global-infrastructure-faq-local-zones-select-services-closer-to-users
  claim: Local Zones let you use select AWS services, such as compute and storage, closer to end users, giving them very low-latency access to applications that run locally.
  link: [very low-latency access to applications running locally](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-select-services-closer-to-users)
  link: [select AWS services, like compute and storage services, closer to more end users](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-select-services-closer-to-users)
  say: Local Zones put select services closer to end users for very low latency
global-infrastructure-faq-local-zones-services-available-locally
  claim: Services available locally in Local Zones include Amazon EC2, VPC, EBS, FSx, Elastic Load Balancing, EMR, ElastiCache and RDS; orchestration services such as EC2 Auto Scaling, EKS, ECS, Systems Manager, CloudWatch, CloudTrail and CloudFormation can work with them.
  link: [Amazon EC2, Amazon VPC, Amazon EBS, Amazon FSx, Elastic Load Balancing (ELB), Amazon EMR, Amazon ElastiCache, and Amazon Relational Database Service (Amazon RDS) are available locally in Local Zones](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-services-available-locally)
  say: EC2, VPC, EBS, FSx, load balancing, EMR, ElastiCache and RDS run locally in Local Zones
global-infrastructure-faq-local-zones-single-digit-millisecond-latency-workloads
  claim: Local Zones are AWS infrastructure designed to run workloads that require single-digit millisecond latency, such as video rendering, graphics-intensive and virtual desktop applications, without the customer owning or operating a data center.
  link: [single-digit millisecond latency](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-single-digit-millisecond-latency-workloads)
  link: [without the need to own and operate their own data center infrastructure](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-single-digit-millisecond-latency-workloads)
  say: single digit millisecond latency
global-infrastructure-faq-local-zones-vs-availability-zones-core-vs-full-services
  claim: Local Zones are designed to bring the core services needed for the latency-sensitive part of a workload closer to end users, while Availability Zones provide access to the full array of AWS services.
  link: [the core services needed for the latency-sensitive portions of your workload](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-vs-availability-zones-core-vs-full-services)
  link: [Availability Zones provide access to the full array of AWS services](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-vs-availability-zones-core-vs-full-services)
  say: a Local Zone is designed to bring the core services for the latency-sensitive part of a workload closer to users
global-infrastructure-faq-local-zones-when-to-use-latency-hybrid-residency
  claim: AWS says to use Local Zones to deploy workloads closer to end users for low-latency requirements, to meet low-latency requirements between workloads in a hybrid deployment, and to store data in a specific geographic location for data residency requirements.
  link: [deploy workloads closer to your end users for low-latency requirements](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-when-to-use-latency-hybrid-residency)
  link: [meet low latency requirements between workloads in a hybrid deployment](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-when-to-use-latency-hybrid-residency)
  link: [store data in a specific geographic location to meet data residency requirements](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-when-to-use-latency-hybrid-residency)
  say: use a Local Zone to put a workload close to end users for low latency
global-infrastructure-faq-outposts-for-workloads-that-must-stay-on-premises
  claim: AWS Outposts is designed for workloads that need to remain on premises because of latency requirements, where the customer wants that workload to run seamlessly with the rest of their workloads on AWS; it is fully managed and uses AWS-designed compute and storage racks on premises.
  link: [workloads that need to remain on premises due to latency requirements](../facts/global-infrastructure.md#global-infrastructure-faq-outposts-for-workloads-that-must-stay-on-premises)
  link: [Outposts is fully managed](../facts/global-infrastructure.md#global-infrastructure-faq-outposts-for-workloads-that-must-stay-on-premises)
  say: Outposts is for workloads that must stay on premises
global-infrastructure-faq-wavelength-ultralow-latency-for-5g-devices
  claim: AWS Wavelength is designed to deliver ultralow-latency applications to 5G devices by extending AWS infrastructure, services, APIs and tools into telecommunications providers' 5G networks.
  link: [ultralow-latency applications to 5G devices](../facts/global-infrastructure.md#global-infrastructure-faq-wavelength-ultralow-latency-for-5g-devices)
  say: Wavelength is for ultra low latency applications on five G devices
global-infrastructure-fault-isolation-boundary-definition
  claim: Fault isolation limits the impact of a component or system failure to a defined boundary; components outside the boundary are unaffected, and running a workload across multiple fault isolation boundaries makes it more resilient.
  scope: fault isolation.
  link: [limits the impact of a component or system failure to a defined boundary](../facts/global-infrastructure.md#global-infrastructure-fault-isolation-boundary-definition)
  link: [components outside of the boundary are unaffected by the failure](../facts/global-infrastructure.md#global-infrastructure-fault-isolation-boundary-definition)
  say: fault isolation keeps a failure inside a defined boundary
global-infrastructure-fiber-backbone-20-million-km
  claim: The AWS global network backbone has nearly 20 million kilometers of terrestrial and subsea fiber optic cabling, which AWS says gives faster data transfers, lower latency and increased performance.
  scope: AWS global network, as retrieved on the snapshot date.
  link: [nearly 20 million kilometers](../facts/global-infrastructure.md#global-infrastructure-fiber-backbone-20-million-km)
  link: [faster data transfers, lower latency, and increased performance](../facts/global-infrastructure.md#global-infrastructure-fiber-backbone-20-million-km)
  say: nearly twenty million kilometers of fiber
global-infrastructure-general-endpoint-routes-to-us-east-1
  claim: EC2, EC2 Auto Scaling and EMR also accept a general endpoint without a Region; a request to a general endpoint is routed to US East (N. Virginia), us-east-1, the default Region for API calls.
  scope: general endpoints of Amazon EC2, EC2 Auto Scaling and Amazon EMR; default; not adjustable.
  link: [AWS routes the API request to US East (N. Virginia) (us-east-1), which is the default Region for API calls](../facts/global-infrastructure.md#global-infrastructure-general-endpoint-routes-to-us-east-1)
  link: [us-east-1](../facts/global-infrastructure.md#global-infrastructure-general-endpoint-routes-to-us-east-1)
global-infrastructure-global-service-control-plane-single-region-data-plane-global
  claim: A global service has resources that are not Region-specific; for most global services the control plane is hosted in a single Region while the data plane is distributed globally.
  link: [their control plane is hosted in a single AWS Region, while their data plane is globally distributed](../facts/global-infrastructure.md#global-infrastructure-global-service-control-plane-single-region-data-plane-global)
  link: [commonly referred to as global](../facts/global-infrastructure.md#global-infrastructure-global-service-control-plane-single-region-data-plane-global)
  say: a global service has one control plane Region and a worldwide data plane
global-infrastructure-hybrid-deployment-definition
  claim: A hybrid deployment connects infrastructure and applications between cloud-based resources and existing resources that are not in the cloud, most commonly the cloud and existing on-premises infrastructure.
  link: [connect infrastructure and applications between cloud-based resources and existing resources that are not located in the cloud](../facts/global-infrastructure.md#global-infrastructure-hybrid-deployment-definition)
  link: [between the cloud and existing on-premises infrastructure](../facts/global-infrastructure.md#global-infrastructure-hybrid-deployment-definition)
global-infrastructure-iam-control-plane-us-east-1
  claim: In the aws partition the IAM control plane is in the us-east-1 Region, with isolated data planes in each Region of the partition.
  link: [us-east-1](../facts/global-infrastructure.md#global-infrastructure-iam-control-plane-us-east-1)
  link: [isolated data planes in each Region of the partition](../facts/global-infrastructure.md#global-infrastructure-iam-control-plane-us-east-1)
global-infrastructure-inbound-transfer-no-charge-in-most-cases
  claim: In most cases there is no charge for inbound data transfer or for data transfer between AWS services within the same Region, with some exceptions.
  scope: AWS pricing in general; some exceptions; verify the service's data transfer rates.
  link: [no charge for inbound data transfer](../facts/global-infrastructure.md#global-infrastructure-inbound-transfer-no-charge-in-most-cases)
global-infrastructure-inter-az-traffic-encrypted
  claim: All traffic between Availability Zones is encrypted.
  scope: traffic between Availability Zones.
  link: [All traffic between AZs is encrypted](../facts/global-infrastructure.md#global-infrastructure-inter-az-traffic-encrypted)
  say: all traffic between Availability Zones is encrypted
global-infrastructure-local-zone-extension-of-region-own-internet
  claim: A Local Zone is an extension of an AWS Region close to your users; it has its own connections to the internet and supports Direct Connect, so resources there can serve low-latency applications.
  link: [an extension of an AWS Region in geographic proximity to your users](../facts/global-infrastructure.md#global-infrastructure-local-zone-extension-of-region-own-internet)
  link: [their own connections to the internet and support Direct Connect](../facts/global-infrastructure.md#global-infrastructure-local-zone-extension-of-region-own-internet)
global-infrastructure-local-zone-must-be-enabled-then-subnet
  claim: To use a Local Zone you must first enable it, then create a subnet in the Local Zone, then launch resources in that subnet.
  link: [you must first enable it](../facts/global-infrastructure.md#global-infrastructure-local-zone-must-be-enabled-then-subnet)
  link: [create a subnet in the Local Zone](../facts/global-infrastructure.md#global-infrastructure-local-zone-must-be-enabled-then-subnet)
global-infrastructure-local-zone-no-vpc-endpoints-no-site-to-site-vpn
  claim: You cannot create VPC endpoints inside Local Zone subnets, and AWS Site-to-Site VPN is not available in Local Zones (use a software VPN instead).
  scope: Local Zone subnets.
  link: [You cannot create VPC endpoints inside Local Zone subnets](../facts/global-infrastructure.md#global-infrastructure-local-zone-no-vpc-endpoints-no-site-to-site-vpn)
  link: [The AWS Site-to-Site VPN is not available in Local Zones](../facts/global-infrastructure.md#global-infrastructure-local-zone-no-vpc-endpoints-no-site-to-site-vpn)
global-infrastructure-local-zone-parent-region-private-network
  claim: Local Zones have local internet ingress and egress to reduce latency and are connected to their parent Region through Amazon's redundant, high-bandwidth private network, giving them access to the full range of services.
  link: [connected to their parent Region through Amazon’s redundant and high-bandwidth private network](../facts/global-infrastructure.md#global-infrastructure-local-zone-parent-region-private-network)
  link: [local internet ingress and egress to reduce latency](../facts/global-infrastructure.md#global-infrastructure-local-zone-parent-region-private-network)
global-infrastructure-local-zone-subnets-same-routing-rules
  claim: Local Zone subnets follow the same routing rules as Availability Zone subnets, including route tables, security groups and network ACLs, and outbound internet traffic leaves from the Local Zone itself.
  link: [the same routing rules as Availability Zone subnets](../facts/global-infrastructure.md#global-infrastructure-local-zone-subnets-same-routing-rules)
  link: [Outbound internet traffic leaves a Local Zone from the Local Zone](../facts/global-infrastructure.md#global-infrastructure-local-zone-subnets-same-routing-rules)
global-infrastructure-local-zone-use-cases
  claim: AWS names three reasons to use Local Zones: run low-latency applications at the edge, simplify hybrid cloud migrations, and meet stringent data residency requirements such as state and local rules in healthcare, financial services, iGaming and government.
  link: [Run low-latency applications at the edge](../facts/global-infrastructure.md#global-infrastructure-local-zone-use-cases)
  link: [Simplify hybrid cloud migrations](../facts/global-infrastructure.md#global-infrastructure-local-zone-use-cases)
  link: [Meet stringent data residency requirements](../facts/global-infrastructure.md#global-infrastructure-local-zone-use-cases)
  say: Local Zones are for low latency at the edge, hybrid migration and data residency
global-infrastructure-local-zones-definition-close-to-population-centers
  claim: AWS Local Zones place compute, storage, database and other select AWS resources close to large population and industry centers so that users get low-latency access to applications.
  link: [close to large population and industry centers](../facts/global-infrastructure.md#global-infrastructure-local-zones-definition-close-to-population-centers)
  link: [low-latency access to your applications](../facts/global-infrastructure.md#global-infrastructure-local-zones-definition-close-to-population-centers)
  say: a Local Zone puts AWS compute and storage in a big city near the users
global-infrastructure-local-zones-pricing-no-enable-charge-different-prices
  claim: Enabling a Local Zone costs nothing; you pay only for the resources you deploy there, and resources in Local Zones have different prices from the parent Region.
  scope: AWS Local Zones.
  link: [no additional charge for enabling Local Zones](../facts/global-infrastructure.md#global-infrastructure-local-zones-pricing-no-enable-charge-different-prices)
  link: [different prices than they do in parent AWS Regions](../facts/global-infrastructure.md#global-infrastructure-local-zones-pricing-no-enable-charge-different-prices)
global-infrastructure-most-customers-single-region-suffices
  claim: AWS believes that most customers can reach their resilience goals in a single Region by using Regional services or Multi-AZ architectures built on zonal services.
  link: [most customers can achieve their resilience goals in a single Region](../facts/global-infrastructure.md#global-infrastructure-most-customers-single-region-suffices)
  link: [Regional services or Multi-AZ architectures](../facts/global-infrastructure.md#global-infrastructure-most-customers-single-region-suffices)
  say: for most workloads one Region with several Availability Zones is enough
global-infrastructure-multi-region-avoids-correlated-failures
  claim: The physical and logical separation between AWS Regions avoids correlated failures between them, so a multi-Region architecture can make a workload resilient to the impairment of a Regional service.
  link: [avoids correlated failures between them](../facts/global-infrastructure.md#global-infrastructure-multi-region-avoids-correlated-failures)
  link: [resilient to the impairment of a Regional service](../facts/global-infrastructure.md#global-infrastructure-multi-region-avoids-correlated-failures)
global-infrastructure-multi-region-duplicate-everything-no-cross-region-dependency
  claim: In a multi-Region design you must duplicate the workload's components, including VPCs, compute and data services, in each Region; a component in one Region that depends on a different Region increases the risk of failure and weakens the reliability posture.
  scope: multi-Region deployment.
  link: [you must duplicate your workload's components in each Region](../facts/global-infrastructure.md#global-infrastructure-multi-region-duplicate-everything-no-cross-region-dependency)
  link: [dependencies between Regions where a component in one Region relies on services or components in a different Region](../facts/global-infrastructure.md#global-infrastructure-multi-region-duplicate-everything-no-cross-region-dependency)
  say: every component is duplicated in each Region
global-infrastructure-multi-region-only-for-extreme-resilience
  claim: AWS says that workloads that require extreme resilience (such as critical infrastructure, health-related applications, or services with stringent customer or mandated availability requirements) may require more availability than a single AWS Region can provide; such workloads should be deployed and operated across at least two AWS Regions, assuming data residency requirements allow it.
  scope: multi-Region deployment; data residency requirements allow it.
  link: [workloads that require extreme resilience](../facts/global-infrastructure.md#global-infrastructure-multi-region-only-for-extreme-resilience)
  link: [deploy and operate your workload across at least two AWS Regions](../facts/global-infrastructure.md#global-infrastructure-multi-region-only-for-extreme-resilience)
  link: [assuming that your data residency requirements allow it](../facts/global-infrastructure.md#global-infrastructure-multi-region-only-for-extreme-resilience)
  say: when the workload requires extreme resilience
global-infrastructure-multi-region-when-multi-az-suffices-is-anti-pattern
  claim: Implementing a multi-Region architecture when a multi-AZ architecture would satisfy the business requirements is a named anti-pattern; the desired outcome is production workloads distributed among multiple Availability Zones or Regions for fault tolerance and high availability.
  scope: location strategy.
  link: [You implement a multi-Region architecture when a multi-AZ architecture would satisfy business requirements](../facts/global-infrastructure.md#global-infrastructure-multi-region-when-multi-az-suffices-is-anti-pattern)
  link: [distributed among multiple Availability Zones (AZs) or Regions to achieve fault tolerance and high availability](../facts/global-infrastructure.md#global-infrastructure-multi-region-when-multi-az-suffices-is-anti-pattern)
  say: going multi-Region when multi-AZ is enough is an anti-pattern
global-infrastructure-new-account-quota-may-be-lower
  claim: The actual quota value of an account may be less than the AWS default if the account was recently created or is used minimally.
  scope: per account.
  link: [less than the AWS default quota value](../facts/global-infrastructure.md#global-infrastructure-new-account-quota-may-be-lower)
global-infrastructure-no-automatic-cross-region-replication
  claim: AWS does not replicate your resources across Regions for you; resources and data you create in one Region exist in no other Region unless you use a replication or copy feature of a service, or replicate them yourself.
  scope: resources and data across Regions; some resource types can be replicated across Regions when you set it up.
  link: [we don't automatically replicate them for you](../facts/global-infrastructure.md#global-infrastructure-no-automatic-cross-region-replication)
  link: [unless you explicitly use a replication or copy feature offered by an AWS service or replicate the resource yourself](../facts/global-infrastructure.md#global-infrastructure-no-automatic-cross-region-replication)
  say: AWS does not replicate your resources across Regions for you
global-infrastructure-no-synchronous-cross-region-replication
  claim: AWS does not provide a synchronous cross-Region replication feature.
  scope: replication between Regions.
  link: [does not provide a synchronous Cross-Region replication feature](../facts/global-infrastructure.md#global-infrastructure-no-synchronous-cross-region-replication)
  link: [synchronous Cross-Region replication feature](../facts/global-infrastructure.md#global-infrastructure-no-synchronous-cross-region-replication)
  say: replication between Regions is asynchronous
global-infrastructure-north-america-counts
  claim: As retrieved on the snapshot date, North America has 31 Availability Zones within 9 geographic Regions, with 31 edge network locations and 3 edge cache locations.
  scope: North America, as retrieved on the snapshot date.
  link: [31 Availability Zones within 9 Geographic Regions](../facts/global-infrastructure.md#global-infrastructure-north-america-counts)
  link: [31 Edge Network Locations and 3 Edge Cache Locations](../facts/global-infrastructure.md#global-infrastructure-north-america-counts)
global-infrastructure-opt-in-regions-after-march-2019
  claim: A Region introduced after March 20, 2019 must be enabled in the account before you can use it; the earlier Regions are enabled by default, so you can create resources in them immediately.
  scope: per account, per Region; default; adjustable; Regions introduced after March 20, 2019 are disabled until enabled.
  link: [you must enable the Region before you can access it](../facts/global-infrastructure.md#global-infrastructure-opt-in-regions-after-march-2019)
  link: [a Region introduced after March 20, 2019](../facts/global-infrastructure.md#global-infrastructure-opt-in-regions-after-march-2019)
  link: [The earlier Regions are enabled by default](../facts/global-infrastructure.md#global-infrastructure-opt-in-regions-after-march-2019)
  say: newer Regions must be enabled before you can use them
global-infrastructure-outbound-transfer-tiered-per-gb
  claim: Outbound data transfer is aggregated across services and charged at the outbound data transfer rate, and the more data you transfer the less you pay per GB.
  scope: AWS pricing in general.
  link: [the less you pay per GB](../facts/global-infrastructure.md#global-infrastructure-outbound-transfer-tiered-per-gb)
  link: [AWS Data Transfer Out](../facts/global-infrastructure.md#global-infrastructure-outbound-transfer-tiered-per-gb)
global-infrastructure-outpost-extension-of-az-managed-as-part-of-region
  claim: An Outpost is a pool of AWS compute and storage capacity at a customer site that AWS operates, monitors and manages as part of a Region; each Outpost is an extension of an Availability Zone and its Region.
  link: [Each Outpost is an extension of an Availability Zone and its associated Region](../facts/global-infrastructure.md#global-infrastructure-outpost-extension-of-az-managed-as-part-of-region)
  link: [AWS operates, monitors, and manages this capacity as part of an AWS Region](../facts/global-infrastructure.md#global-infrastructure-outpost-extension-of-az-managed-as-part-of-region)
global-infrastructure-outpost-form-factors-servers-and-racks
  claim: Outposts come in several form factors, from 1U and 2U Outposts servers to 42U Outposts racks and multi-rack deployments.
  link: [from 1U and 2U Outposts servers to 42U Outposts racks](../facts/global-infrastructure.md#global-infrastructure-outpost-form-factors-servers-and-racks)
  link: [multiple rack deployments](../facts/global-infrastructure.md#global-infrastructure-outpost-form-factors-servers-and-racks)
global-infrastructure-outposts-definition-extends-aws-to-premises
  claim: AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs and tools to customer premises, for lower latency and local data processing using the same programming interfaces as in Regions.
  link: [extends AWS infrastructure, services, APIs, and tools to customer premises](../facts/global-infrastructure.md#global-infrastructure-outposts-definition-extends-aws-to-premises)
  link: [lower latency and local data processing needs](../facts/global-infrastructure.md#global-infrastructure-outposts-definition-extends-aws-to-premises)
  say: Outposts is AWS hardware and services in your own building, managed by AWS
global-infrastructure-partition-names-aws-aws-cn-aws-us-gov
  claim: Commercial Regions are in the aws partition, the China Regions are in the aws-cn partition, and the AWS GovCloud (US) Regions are in the aws-us-gov partition.
  link: [aws](../facts/global-infrastructure.md#global-infrastructure-partition-names-aws-aws-cn-aws-us-gov)
  link: [aws-cn](../facts/global-infrastructure.md#global-infrastructure-partition-names-aws-aws-cn-aws-us-gov)
  link: [aws-us-gov](../facts/global-infrastructure.md#global-infrastructure-partition-names-aws-aws-cn-aws-us-gov)
global-infrastructure-partition-one-per-region-hard-boundary
  claim: Every Region is in exactly one partition, each partition has one or more Regions, and partitions have independent instances of IAM and form a hard boundary between Regions in different partitions.
  link: [Every Region is in exactly one partition](../facts/global-infrastructure.md#global-infrastructure-partition-one-per-region-hard-boundary)
  link: [independent instances of AWS Identity and Access Management (IAM)](../facts/global-infrastructure.md#global-infrastructure-partition-one-per-region-hard-boundary)
  link: [a hard boundary between Regions in different partitions](../facts/global-infrastructure.md#global-infrastructure-partition-one-per-region-hard-boundary)
  say: a partition is a group of Regions with its own IAM and a hard boundary
global-infrastructure-partitional-services-definition-iam-example
  claim: Partitional global services exist once per partition with their control plane in a single Region; some, like AWS Network Manager, are control-plane only, while others, like IAM, have their own data plane distributed across every Region of the partition, and failures in one partition do not affect other partitions.
  link: [Partitional services provide their control plane in a single AWS Region](../facts/global-infrastructure.md#global-infrastructure-partitional-services-definition-iam-example)
  link: [Failures in a partitional service do not impact other partitions](../facts/global-infrastructure.md#global-infrastructure-partitional-services-definition-iam-example)
global-infrastructure-pay-as-you-go-no-termination-fees
  claim: AWS prices the vast majority of its services pay-as-you-go: you pay only for the services you use, for as long as you use them, without long-term contracts, and when you stop there are no additional costs or termination fees.
  scope: AWS pricing in general.
  link: [pay-as-you-go](../facts/global-infrastructure.md#global-infrastructure-pay-as-you-go-no-termination-fees)
  link: [no additional costs or termination fees](../facts/global-infrastructure.md#global-infrastructure-pay-as-you-go-no-termination-fees)
global-infrastructure-pop-hosts-cloudfront-route53-global-accelerator
  claim: AWS points of presence host Amazon CloudFront (a CDN), Amazon Route 53 (public DNS) and AWS Global Accelerator (edge networking optimization), in addition to the Regions and Availability Zones.
  scope: AWS edge network.
  link: [Amazon CloudFront](../facts/global-infrastructure.md#global-infrastructure-pop-hosts-cloudfront-route53-global-accelerator)
  link: [Amazon Route 53](../facts/global-infrastructure.md#global-infrastructure-pop-hosts-cloudfront-route53-global-accelerator)
  link: [AWS Global Accelerator](../facts/global-infrastructure.md#global-infrastructure-pop-hosts-cloudfront-route53-global-accelerator)
global-infrastructure-pre-provision-capacity-instead-of-control-plane-recovery
  claim: Pre-provisioning extra capacity, rather than relying on the EC2 control plane to launch new instances after an Availability Zone fails, is how you achieve static stability; removing control plane dependencies from the recovery path gives more resilient workloads.
  link: [having that extra capacity pre-provisioned helps achieve static stability](../facts/global-infrastructure.md#global-infrastructure-pre-provision-capacity-instead-of-control-plane-recovery)
  link: [eliminating dependencies on control planes](../facts/global-infrastructure.md#global-infrastructure-pre-provision-capacity-instead-of-control-plane-recovery)
  say: pre-provision capacity in the other zones instead of launching during the failure
global-infrastructure-production-at-least-two-azs
  claim: The reliability pillar says to deploy and operate all production workloads in at least two Availability Zones in a Region; a production workload that exists only in a single Availability Zone is a named anti-pattern.
  scope: production workloads; minimum.
  link: [at least two Availability Zones (AZs) in a Region](../facts/global-infrastructure.md#global-infrastructure-production-at-least-two-azs)
  link: [Your production workload exists only in a single Availability Zone](../facts/global-infrastructure.md#global-infrastructure-production-at-least-two-azs)
  say: at least two Availability Zones for every production workload
global-infrastructure-region-billing-code-use1
  claim: AWS billing and usage reports often abbreviate Region codes with short codes such as USE1 for us-east-1 (US East (N. Virginia)); for example, the line_item_usage_type value APE1-USE1-AWS-In-Bytes shows the short codes of the Asia Pacific (Hong Kong) and US East (N. Virginia) Regions.
  scope: AWS billing and usage reports.
  link: [USE1](../facts/global-infrastructure.md#global-infrastructure-region-billing-code-use1)
  link: [APE1-USE1-AWS-In-Bytes](../facts/global-infrastructure.md#global-infrastructure-region-billing-code-use1)
global-infrastructure-region-choice-services-and-latency
  claim: When choosing a Region, select one that has the services and features you need, and lower network latency by choosing a Region close to the majority of your users; being closer to customers and meeting legal requirements are the stated reasons to create resources in a given location.
  scope: Region selection.
  link: [select a Region that has the AWS services and features that you need](../facts/global-infrastructure.md#global-infrastructure-region-choice-services-and-latency)
  link: [lower network latency when you select a Region that is close to the majority of your users](../facts/global-infrastructure.md#global-infrastructure-region-choice-services-and-latency)
  link: [closer to your European customers or to meet legal requirements](../facts/global-infrastructure.md#global-infrastructure-region-choice-services-and-latency)
  say: pick a Region that has the services you need | pick a Region close to most of your users to lower latency
global-infrastructure-region-count-aws-account-34
  claim: An AWS account gets access to 34 Regions as retrieved from the Regions guide on the snapshot date; this count leaves out the AWS GovCloud (US) and China Regions, which need their own account types.
  scope: Regions provided by an AWS account (not GovCloud, not China); count as retrieved on the snapshot date; new Regions open every year.
  link: [34 Regions](../facts/global-infrastructure.md#global-infrastructure-region-count-aws-account-34)
  say: thirty-four Regions for an AWS account, GovCloud and China not counted
global-infrastructure-region-is-separate-geographic-area
  claim: A Region is a physical location in the world: a separate geographic area in which AWS has multiple Availability Zones.
  scope: AWS Regions.
  link: [a separate geographic area where AWS has multiple Availability Zones](../facts/global-infrastructure.md#global-infrastructure-region-is-separate-geographic-area)
  link: [a physical location in the world](../facts/global-infrastructure.md#global-infrastructure-region-is-separate-geographic-area)
  say: a Region is a separate geographic area with multiple Availability Zones
global-infrastructure-region-isolated-for-fault-tolerance
  claim: Each AWS Region is designed to be isolated from the other Regions, and this isolation is what gives the greatest possible fault tolerance and stability.
  scope: AWS Regions.
  link: [designed to be isolated from the other Regions](../facts/global-infrastructure.md#global-infrastructure-region-isolated-for-fault-tolerance)
  link: [the greatest possible fault tolerance and stability](../facts/global-infrastructure.md#global-infrastructure-region-isolated-for-fault-tolerance)
  say: each Region is designed to be isolated from the others
global-infrastructure-region-launched-ap-east-2
  claim: AWS launched the Asia Pacific (Taipei) Region, ap-east-2, on June 6, 2025.
  scope: AWS Regions.
  link: [ap-east-2](../facts/global-infrastructure.md#global-infrastructure-region-launched-ap-east-2)
  link: [June 6, 2025](../facts/global-infrastructure.md#global-infrastructure-region-launched-ap-east-2)
global-infrastructure-region-launched-ap-south-2
  claim: AWS launched the Asia Pacific (Hyderabad) Region, ap-south-2, on November 22, 2022.
  scope: AWS Regions.
  link: [ap-south-2](../facts/global-infrastructure.md#global-infrastructure-region-launched-ap-south-2)
  link: [November 22, 2022](../facts/global-infrastructure.md#global-infrastructure-region-launched-ap-south-2)
global-infrastructure-region-launched-ap-southeast-4
  claim: AWS launched the Asia Pacific (Melbourne) Region, ap-southeast-4, on January 23, 2023.
  scope: AWS Regions.
  link: [ap-southeast-4](../facts/global-infrastructure.md#global-infrastructure-region-launched-ap-southeast-4)
  link: [January 23, 2023](../facts/global-infrastructure.md#global-infrastructure-region-launched-ap-southeast-4)
global-infrastructure-region-launched-ap-southeast-5
  claim: AWS launched the Asia Pacific (Malaysia) Region, ap-southeast-5, on August 21, 2024.
  scope: AWS Regions.
  link: [ap-southeast-5](../facts/global-infrastructure.md#global-infrastructure-region-launched-ap-southeast-5)
  link: [August 21, 2024](../facts/global-infrastructure.md#global-infrastructure-region-launched-ap-southeast-5)
global-infrastructure-region-launched-ap-southeast-6
  claim: AWS launched the Asia Pacific (New Zealand) Region, ap-southeast-6, on September 2, 2025.
  scope: AWS Regions.
  link: [ap-southeast-6](../facts/global-infrastructure.md#global-infrastructure-region-launched-ap-southeast-6)
  link: [September 2, 2025](../facts/global-infrastructure.md#global-infrastructure-region-launched-ap-southeast-6)
global-infrastructure-region-launched-ap-southeast-7
  claim: AWS launched the Asia Pacific (Thailand) Region, ap-southeast-7, on January 7, 2025.
  scope: AWS Regions.
  link: [ap-southeast-7](../facts/global-infrastructure.md#global-infrastructure-region-launched-ap-southeast-7)
  link: [January 7, 2025](../facts/global-infrastructure.md#global-infrastructure-region-launched-ap-southeast-7)
global-infrastructure-region-launched-ca-west-1
  claim: AWS launched the Canada West (Calgary) Region, ca-west-1, on December 20, 2023.
  scope: AWS Regions.
  link: [ca-west-1](../facts/global-infrastructure.md#global-infrastructure-region-launched-ca-west-1)
  link: [December 20, 2023](../facts/global-infrastructure.md#global-infrastructure-region-launched-ca-west-1)
global-infrastructure-region-launched-eu-central-2
  claim: AWS launched the Europe (Zurich) Region, eu-central-2, on November 8, 2022.
  scope: AWS Regions.
  link: [eu-central-2](../facts/global-infrastructure.md#global-infrastructure-region-launched-eu-central-2)
  link: [November 8, 2022](../facts/global-infrastructure.md#global-infrastructure-region-launched-eu-central-2)
global-infrastructure-region-launched-eu-south-2
  claim: AWS launched the Europe (Spain) Region, eu-south-2, on November 15, 2022.
  scope: AWS Regions.
  link: [eu-south-2](../facts/global-infrastructure.md#global-infrastructure-region-launched-eu-south-2)
  link: [November 15, 2022](../facts/global-infrastructure.md#global-infrastructure-region-launched-eu-south-2)
global-infrastructure-region-launched-il-central-1
  claim: AWS launched the Israel (Tel Aviv) Region, il-central-1, on August 1, 2023.
  scope: AWS Regions.
  link: [il-central-1](../facts/global-infrastructure.md#global-infrastructure-region-launched-il-central-1)
  link: [August 1, 2023](../facts/global-infrastructure.md#global-infrastructure-region-launched-il-central-1)
global-infrastructure-region-launched-me-central-1
  claim: AWS launched the Middle East (UAE) Region, me-central-1, on August 29, 2022.
  scope: AWS Regions.
  link: [me-central-1](../facts/global-infrastructure.md#global-infrastructure-region-launched-me-central-1)
  link: [August 29, 2022](../facts/global-infrastructure.md#global-infrastructure-region-launched-me-central-1)
global-infrastructure-region-launched-mx-central-1
  claim: AWS launched the Mexico (Central) Region, mx-central-1, on January 14, 2025.
  scope: AWS Regions.
  link: [mx-central-1](../facts/global-infrastructure.md#global-infrastructure-region-launched-mx-central-1)
  link: [January 14, 2025](../facts/global-infrastructure.md#global-infrastructure-region-launched-mx-central-1)
global-infrastructure-region-min-three-azs
  claim: Every AWS Region has at least three Availability Zones.
  scope: per Region; minimum; not adjustable.
  link: [at least three Availability Zones](../facts/global-infrastructure.md#global-infrastructure-region-min-three-azs)
  link: [at least three](../facts/global-infrastructure.md#global-infrastructure-region-min-three-azs)
  say: at least three Availability Zones in every Region
global-infrastructure-region-pricing-differs-local-market
  claim: Resource pricing differs between Regions because each Region operates within local market conditions, for example the cost of land, fiber, electricity and taxes.
  scope: per Region.
  link: [different in each Region](../facts/global-infrastructure.md#global-infrastructure-region-pricing-differs-local-market)
global-infrastructure-regional-endpoint-syntax
  claim: Most AWS services offer a Regional endpoint of the form protocol://service-code.region-code.amazonaws.com, for example https://dynamodb.us-west-2.amazonaws.com for DynamoDB in US West (Oregon).
  link: [https://dynamodb.us-west-2.amazonaws.com](../facts/global-infrastructure.md#global-infrastructure-regional-endpoint-syntax)
  link: [Most Amazon Web Services offer a Regional endpoint](../facts/global-infrastructure.md#global-infrastructure-regional-endpoint-syntax)
global-infrastructure-regional-resource-visible-only-in-its-region
  claim: A regional resource is specific to the Region in which you create it; to view your resources you must specify a Region, and you then see only the resources tied to that Region.
  scope: regional resources.
  link: [specific to the Region in which you create it](../facts/global-infrastructure.md#global-infrastructure-regional-resource-visible-only-in-its-region)
  link: [you see only the resources that are tied to that Region](../facts/global-infrastructure.md#global-infrastructure-regional-resource-visible-only-in-its-region)
  say: a regional resource belongs to the Region you created it in
global-infrastructure-regional-service-definition
  claim: A Regional service is one that AWS has built on top of multiple Availability Zones and presents to you as a single Regional endpoint, so you do not have to work out how to use zonal services well.
  link: [built on top of multiple Availability Zones](../facts/global-infrastructure.md#global-infrastructure-regional-service-definition)
  link: [a single Regional endpoint](../facts/global-infrastructure.md#global-infrastructure-regional-service-definition)
  say: a Regional service is spread over several Availability Zones behind one Regional endpoint
global-infrastructure-regional-services-fail-independently
  claim: Regions have even greater physical separation and isolation than Availability Zones; with few exceptions, AWS services operate fully independently per Region (Regional services), and a failure of a Regional service is designed not to affect that service in another Region.
  scope: Regional services; with few exceptions.
  link: [operate fully independently between different Regions](../facts/global-infrastructure.md#global-infrastructure-regional-services-fail-independently)
  link: [A failure of an AWS Regional service is designed not to impact the service in a different Region](../facts/global-infrastructure.md#global-infrastructure-regional-services-fail-independently)
  say: Regional services run independently in each Region | a failure in one Region is designed not to touch another Region
global-infrastructure-route53-control-plane-us-east-1-data-plane-pops
  claim: The Route 53 control plane (all public APIs for hosted zones, records, health checks and more) is hosted in us-east-1; its data plane is the authoritative DNS service running in over 200 PoP locations and in each Region.
  link: [hosted in us-east-1](../facts/global-infrastructure.md#global-infrastructure-route53-control-plane-us-east-1-data-plane-pops)
  link: [runs across over 200 PoP locations as well as in each AWS Region](../facts/global-infrastructure.md#global-infrastructure-route53-control-plane-us-east-1-data-plane-pops)
global-infrastructure-route53-dns-and-health-checks-continue-during-control-plane-impairment
  claim: During a Route 53 control plane impairment the CRUDL operations may not work, but DNS resolution, health checks and routing updates driven by health checks continue to work.
  link: [DNS resolution and health checks, and updates to routing resulting from changes in health checks, will continue to work](../facts/global-infrastructure.md#global-infrastructure-route53-dns-and-health-checks-continue-during-control-plane-impairment)
  link: [CRUDL-type operations for Route 53 may not work](../facts/global-infrastructure.md#global-infrastructure-route53-dns-and-health-checks-continue-during-control-plane-impairment)
  say: Route 53 keeps answering DNS and running health checks even if its APIs are down
global-infrastructure-route53-failover-use-health-checks-not-record-changes
  claim: A statically stable Route 53 design fails over between Regions using health check status; changing record values with ChangeResourceRecordSets, changing weights or creating new records at failover time depends on the Route 53 control plane.
  link: [use the status of health checks to perform failovers between Regions](../facts/global-infrastructure.md#global-infrastructure-route53-failover-use-health-checks-not-record-changes)
  link: [These approaches depend on the Route 53 control plane](../facts/global-infrastructure.md#global-infrastructure-route53-failover-use-health-checks-not-record-changes)
global-infrastructure-s3-regional-recovers-from-az-failure
  claim: Amazon S3 spreads requests and data across multiple Availability Zones and is designed to recover automatically from the failure of an Availability Zone; you only interact with its Regional endpoint.
  link: [designed to automatically recover from the failure of an Availability Zone](../facts/global-infrastructure.md#global-infrastructure-s3-regional-recovers-from-az-failure)
  link: [you only interact with the Regional endpoint](../facts/global-infrastructure.md#global-infrastructure-s3-regional-recovers-from-az-failure)
global-infrastructure-service-quota-default-per-region
  claim: Every AWS account has default quotas, formerly called limits, for each AWS service, and unless AWS notes otherwise each quota is Region-specific.
  scope: per account, per Region; default; adjustable.
  link: [Region-specific](../facts/global-infrastructure.md#global-infrastructure-service-quota-default-per-region)
  link: [formerly referred to as limits](../facts/global-infrastructure.md#global-infrastructure-service-quota-default-per-region)
global-infrastructure-service-quota-increase-takes-days
  claim: A quota increase is not granted immediately: Support might approve, deny or partially approve it, and it might take a couple of days to take effect.
  scope: service quota increase requests.
  link: [a couple of days](../facts/global-infrastructure.md#global-infrastructure-service-quota-increase-takes-days)
  link: [not granted immediately](../facts/global-infrastructure.md#global-infrastructure-service-quota-increase-takes-days)
global-infrastructure-service-quota-not-all-increasable
  claim: You can request increases for some quotas, but not all quotas can be increased.
  scope: service quotas.
  link: [not all quotas can be increased](../facts/global-infrastructure.md#global-infrastructure-service-quota-not-all-increasable)
global-infrastructure-services-depending-on-route53-control-plane
  claim: When you provision an Elastic Load Balancer, the service creates public DNS records and health checks in Route 53, which relies on the Route 53 control plane in us-east-1; AWS recommends not relying on creating such Route 53 resources in the recovery path and pre-provisioning resources like ELBs instead.
  link: [Pre-provision these resources, like ELBs, to prevent a dependency on the Route 53 control plane in your recovery path](../facts/global-infrastructure.md#global-infrastructure-services-depending-on-route53-control-plane)
  link: [This relies on the Route 53 control plane in us-east-1](../facts/global-infrastructure.md#global-infrastructure-services-depending-on-route53-control-plane)
global-infrastructure-single-az-failure-takes-all-instances
  claim: If all of your EC2 instances are in a single Availability Zone and that Availability Zone is affected by a failure, none of your EC2 instances are available.
  scope: EC2 instances hosted in one Availability Zone; the Availability Zone is affected by a failure.
  link: [none of your EC2 instances would be available](../facts/global-infrastructure.md#global-infrastructure-single-az-failure-takes-all-instances)
  say: none of your instances would be available
global-infrastructure-single-region-services-appendix-c
  claim: Some services or features are available only in a single Region (the whitepaper's Appendix C), for example Billing and Cost Management with Cost Explorer, Cost and Usage Reports, Budgets and Savings Plans; the static stability guidance for global services applies to them.
  link: [only available in a single Region](../facts/global-infrastructure.md#global-infrastructure-single-region-services-appendix-c)
  link: [Billing and Cost Management (AWS Cost Explorer, AWS Cost and Usage Reports, AWS Budgets, Savings Plans)](../facts/global-infrastructure.md#global-infrastructure-single-region-services-appendix-c)
global-infrastructure-six-advantages-of-cloud-computing
  claim: The six advantages of cloud computing are: trade fixed expense for variable expense; benefit from massive economies of scale; stop guessing capacity; increase speed and agility; stop spending money running and maintaining data centers; go global in minutes.
  link: [Trade fixed expense for variable expense](../facts/global-infrastructure.md#global-infrastructure-six-advantages-of-cloud-computing)
  link: [Benefit from massive economies of scale](../facts/global-infrastructure.md#global-infrastructure-six-advantages-of-cloud-computing)
  link: [Stop guessing capacity](../facts/global-infrastructure.md#global-infrastructure-six-advantages-of-cloud-computing)
  link: [Increase speed and agility](../facts/global-infrastructure.md#global-infrastructure-six-advantages-of-cloud-computing)
  link: [Stop spending money running and maintaining data centers](../facts/global-infrastructure.md#global-infrastructure-six-advantages-of-cloud-computing)
  link: [Go global in minutes](../facts/global-infrastructure.md#global-infrastructure-six-advantages-of-cloud-computing)
global-infrastructure-static-stability-definition
  claim: Static stability means that a system keeps operating in its current state, as normal, without needing to make changes while a dependency fails or is unavailable.
  link: [continue to operate as normal without the need to make changes during the failure or unavailability of dependencies](../facts/global-infrastructure.md#global-infrastructure-static-stability-definition)
  link: [static stability](../facts/global-infrastructure.md#global-infrastructure-static-stability-definition)
  say: static stability: keep working without changes when a dependency fails
global-infrastructure-static-stability-example-three-per-az-fifty-percent
  claim: In the whitepaper example, to stay statically stable against a single Availability Zone failure you deploy three instances in each Availability Zone, nine in total, which means running 50% additional instances.
  link: [three instances in each Availability Zone, for a total of nine](../facts/global-infrastructure.md#global-infrastructure-static-stability-example-three-per-az-fifty-percent)
  link: [50% additional instances](../facts/global-infrastructure.md#global-infrastructure-static-stability-example-three-per-az-fifty-percent)
global-infrastructure-three-cost-drivers
  claim: AWS names three fundamental cost drivers: compute, storage, and outbound data transfer.
  scope: AWS pricing in general.
  link: [compute, storage, and outbound data transfer](../facts/global-infrastructure.md#global-infrastructure-three-cost-drivers)
  link: [three fundamental drivers of cost](../facts/global-infrastructure.md#global-infrastructure-three-cost-drivers)
global-infrastructure-three-service-types-zonal-regional-global
  claim: AWS groups its services into three categories by fault isolation boundary: zonal, Regional and global.
  link: [zonal, Regional, and global](../facts/global-infrastructure.md#global-infrastructure-three-service-types-zonal-regional-global)
  link: [three different categories of services](../facts/global-infrastructure.md#global-infrastructure-three-service-types-zonal-regional-global)
  say: zonal, Regional and global
global-infrastructure-us-east-1-six-azs
  claim: US East (N. Virginia), us-east-1, has 6 Availability Zones and does not require opt-in, as retrieved from the Regions table on the snapshot date.
  scope: US East (N. Virginia).
  link: [6](../facts/global-infrastructure.md#global-infrastructure-us-east-1-six-azs)
  link: [us-east-1](../facts/global-infrastructure.md#global-infrastructure-us-east-1-six-azs)
global-infrastructure-us-west-1-newer-accounts-two-azs
  claim: Newer accounts can access two Availability Zones in US West (N. California), although the Regions table lists the Region with 3 AZs.
  scope: US West (N. California), newer accounts; newer accounts.
  link: [two Availability Zones](../facts/global-infrastructure.md#global-infrastructure-us-west-1-newer-accounts-two-azs)
global-infrastructure-wavelength-carrier-gateway-no-inbound-from-internet
  claim: A carrier gateway allows inbound traffic from the carrier network and outbound traffic to the carrier network and the internet, but there is no inbound connection from the internet to a Wavelength Zone through the carrier gateway.
  scope: Wavelength Zone carrier gateway.
  link: [There is no inbound connection configuration from the internet to a Wavelength Zone through the carrier gateway](../facts/global-infrastructure.md#global-infrastructure-wavelength-carrier-gateway-no-inbound-from-internet)
  link: [allows inbound traffic from a carrier network in a specific location](../facts/global-infrastructure.md#global-infrastructure-wavelength-carrier-gateway-no-inbound-from-internet)
global-infrastructure-wavelength-zone-definition
  claim: Wavelength Zones let developers build applications that deliver ultra-low latencies to 5G devices and end users; Wavelength deploys standard AWS compute and storage services to the edge of telecommunication carriers' 5G networks.
  scope: Wavelength Zones.
  link: [deploys standard AWS compute and storage services to the edge of telecommunication carriers' 5G networks](../facts/global-infrastructure.md#global-infrastructure-wavelength-zone-definition)
  say: Wavelength puts AWS compute and storage inside the carrier's five G network
global-infrastructure-wavelength-zone-opt-in-then-create
  claim: To deploy resources to a Wavelength Zone you first opt in to the Wavelength Zone and then create resources in it; the subnet is created in a VPC of the Region.
  link: [first opt in to the Wavelength Zone, and then create resources in the Wavelength Zone](../facts/global-infrastructure.md#global-infrastructure-wavelength-zone-opt-in-then-create)
  link: [create a subnet in a Wavelength Zone that is associated with the VPC](../facts/global-infrastructure.md#global-infrastructure-wavelength-zone-opt-in-then-create)
global-infrastructure-zonal-resource-deploy-in-multiple-azs
  claim: A zonal resource is specific to the Availability Zone in which you create it, and the best practice is to deploy your application in multiple Availability Zones so that it remains available even if one Availability Zone fails.
  scope: zonal resources.
  link: [specific to the Availability Zone in which you create it](../facts/global-infrastructure.md#global-infrastructure-zonal-resource-deploy-in-multiple-azs)
  link: [deploy your application in multiple Availability Zones, so that your application remains available even if one Availability Zone fails](../facts/global-infrastructure.md#global-infrastructure-zonal-resource-deploy-in-multiple-azs)
  say: a zonal resource lives in one Availability Zone | deploy in multiple Availability Zones so the application stays available if one zone fails
global-infrastructure-zonal-service-definition
  claim: A zonal service lets you specify which Availability Zone its resources are deployed into; it operates independently in each Availability Zone of a Region and fails independently in each Availability Zone.
  link: [specify which Availability Zone the resources are deployed into](../facts/global-infrastructure.md#global-infrastructure-zonal-service-definition)
  link: [fail independently in each Availability Zone](../facts/global-infrastructure.md#global-infrastructure-zonal-service-definition)
  say: a zonal service runs and fails independently in each Availability Zone
global-infrastructure-zonal-service-no-cross-az-dependency
  claim: In a zonal service the components in one Availability Zone do not take dependencies on components in other Availability Zones, because a zonal service has zonal data planes.
  link: [don't take dependencies on components in other Availability Zones](../facts/global-infrastructure.md#global-infrastructure-zonal-service-no-cross-az-dependency)
  link: [zonal data planes](../facts/global-infrastructure.md#global-infrastructure-zonal-service-no-cross-az-dependency)
management-console-cloudshell-browser-based-pre-authenticated
  claim: AWS CloudShell is a browser-based, pre-authenticated shell launched directly from the console; you run AWS CLI commands in Bash, PowerShell or Z shell without downloading or installing command line tools.
  link: [a browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console](../facts/management-console.md#management-console-cloudshell-browser-based-pre-authenticated)
  link: [without downloading or installing command line tools](../facts/management-console.md#management-console-cloudshell-browser-based-pre-authenticated)
  say: CloudShell is a terminal in the browser, already signed in as you
management-console-cloudshell-command-size-65412-characters
  claim: A CloudShell command cannot exceed 65412 characters; to run a longer command, AWS says to create a script and run it from the command line interface.
  scope: per command; maximum; not adjustable.
  link: [65412 characters](../facts/management-console.md#management-console-cloudshell-command-size-65412-characters)
management-console-cloudshell-concurrent-shells-10-per-region
  claim: You can run up to 10 CloudShell shells at the same time in each AWS Region for your account; you can request a quota increase for each Region in the Service Quotas console.
  scope: per Region, per account; default; adjustable.
  link: [up to 10 shells](../facts/management-console.md#management-console-cloudshell-concurrent-shells-10-per-region)
management-console-cloudshell-console-credentials-no-configuration
  claim: CloudShell users are pre-authenticated, so you do not configure credentials to use AWS CLI version 2, which is pre-installed in the CloudShell compute environment.
  link: [you don't need to configure credentials when interacting with AWS services using AWS CLI version 2](../facts/management-console.md#management-console-cloudshell-console-credentials-no-configuration)
  link: [The AWS CLI is pre-installed on the shell's compute environment](../facts/management-console.md#management-console-cloudshell-console-credentials-no-configuration)
  say: no access keys: CloudShell uses your console sign-in
management-console-cloudshell-faq-access-from-console-icon-new-tab
  claim: CloudShell is available from the AWS Management Console and requires no software installation, manual updates or patch management.
  link: [CloudShell is available from the AWS Management Console](../facts/management-console.md#management-console-cloudshell-faq-access-from-console-icon-new-tab)
  link: [requires no software installation, manual updates, or patch management](../facts/management-console.md#management-console-cloudshell-faq-access-from-console-icon-new-tab)
  say: from the console, nothing to install
management-console-cloudshell-faq-browser-shell-pre-authenticated
  claim: AWS CloudShell is a browser-based shell for managing, exploring and interacting with your AWS resources, and it is pre-authenticated with your console credentials.
  link: [a browser-based shell](../facts/management-console.md#management-console-cloudshell-faq-browser-shell-pre-authenticated)
  link: [pre-authenticated with your console credentials](../facts/management-console.md#management-console-cloudshell-faq-browser-shell-pre-authenticated)
  say: a browser based shell that is already signed in with your console credentials
management-console-cloudshell-faq-cannot-attach-more-storage-use-s3
  claim: You cannot directly attach more storage to CloudShell; to store more than 1 GB, create and use an S3 bucket from CloudShell.
  scope: CloudShell home directory storage.
  link: [you cannot directly attach more storage to CloudShell](../facts/management-console.md#management-console-cloudshell-faq-cannot-attach-more-storage-use-s3)
  say: no; use an S3 bucket for more than one gigabyte
management-console-cloudshell-faq-default-public-egress-no-ingress
  claim: By default, CloudShell has public internet egress but no ingress capability.
  scope: CloudShell environment network access; default; not adjustable.
  link: [public internet egress, but does not have ingress capability](../facts/management-console.md#management-console-cloudshell-faq-default-public-egress-no-ingress)
  say: outbound internet yes, inbound no
management-console-cloudshell-faq-download-files-up-to-1-gb
  claim: You can upload files to the CloudShell home directory through the browser, and download files of up to 1 GB from CloudShell to your local machine.
  scope: per file downloaded from CloudShell to the local machine; maximum; not adjustable.
  link: [up to 1 GB in size](../facts/management-console.md#management-console-cloudshell-faq-download-files-up-to-1-gb)
  say: downloads of up to one gigabyte
management-console-cloudshell-faq-home-directory-kept-120-days
  claim: CloudShell keeps the files in your home directory for up to 120 days after your last CloudShell session, counted separately per Region; opening CloudShell in that Region with the same IAM principal resets the timer, and you are notified in the health dashboard before deletion.
  scope: CloudShell home directory files, per Region; maximum; not adjustable; counted from the last CloudShell session in that Region.
  link: [120 days](../facts/management-console.md#management-console-cloudshell-faq-home-directory-kept-120-days)
  link: [Accessing CloudShell in the expiring Region through the same IAM principal will reset the timer](../facts/management-console.md#management-console-cloudshell-faq-home-directory-kept-120-days)
  say: one hundred twenty days per Region
management-console-cloudshell-faq-home-directory-persists-1-gb-per-region
  claim: Only changes inside the CloudShell home directory persist across sessions, per Region: you can store up to 1 GB of files in your home directory in each supported Region, and storage is not synchronized across Regions.
  scope: CloudShell home directory, per user, per AWS Region; maximum; not adjustable.
  link: [1 GB](../facts/management-console.md#management-console-cloudshell-faq-home-directory-persists-1-gb-per-region)
  link: [Only changes made inside your home directory will persist across CloudShell sessions per AWS Region](../facts/management-console.md#management-console-cloudshell-faq-home-directory-persists-1-gb-per-region)
  link: [Storage is not synchronized across AWS Regions](../facts/management-console.md#management-console-cloudshell-faq-home-directory-persists-1-gb-per-region)
  say: one gigabyte per Region
management-console-cloudshell-faq-interactive-not-long-running
  claim: CloudShell is intended for interactive work rather than long-running processes; for a long process AWS says to use another compute service.
  link: [intended for interactive workloads rather than long running processes](../facts/management-console.md#management-console-cloudshell-faq-interactive-not-long-running)
  say: interactive only, not long running jobs
management-console-cloudshell-faq-no-additional-charge
  claim: There is no additional charge for CloudShell; you pay for the other AWS resources you use with it, and data transfer is billed at standard AWS data transfer rates.
  link: [no additional charge for CloudShell](../facts/management-console.md#management-console-cloudshell-faq-no-additional-charge)
  link: [Data transfer is billed at standard AWS data transfer rates](../facts/management-console.md#management-console-cloudshell-faq-no-additional-charge)
  say: CloudShell itself is free; you pay for what you create with it
management-console-cloudshell-faq-no-api-console-only
  claim: CloudShell has no API: it is meant to be used from the AWS Management Console and does not currently support programmatic interaction.
  scope: AWS CloudShell, as stated on the FAQ snapshot date.
  link: [does not currently support programmatic interaction](../facts/management-console.md#management-console-cloudshell-faq-no-api-console-only)
  say: no API; console use only
management-console-cloudshell-faq-no-windows-or-macos-instances
  claim: CloudShell does not currently support Windows or macOS instances; PowerShell is pre-installed and can be used on Linux.
  scope: AWS CloudShell compute environment, as stated on the FAQ snapshot date.
  link: [does not currently support Windows or macOS instances](../facts/management-console.md#management-console-cloudshell-faq-no-windows-or-macos-instances)
  say: Linux only; PowerShell runs on that Linux
management-console-cloudshell-faq-one-vm-per-region-10-sessions
  claim: CloudShell gives one virtual machine per Region per user, with up to 10 sessions active at the same time on that virtual machine, and shells from several Regions can be open at once.
  scope: per user, per Region (sessions per virtual machine); maximum; not adjustable.
  link: [one virtual machine per Region, per user](../facts/management-console.md#management-console-cloudshell-faq-one-vm-per-region-10-sessions)
  link: [up to 10 sessions](../facts/management-console.md#management-console-cloudshell-faq-one-vm-per-region-10-sessions)
  say: one virtual machine per Region per user | up to ten sessions
management-console-cloudshell-faq-only-administrator-or-poweruser-by-default
  claim: By default only users with the Administrator or PowerUser role can start a CloudShell session; an IAM policy can restrict the ability to launch CloudShell, and all other users must be granted permission by an administrator.
  scope: CloudShell session start, per IAM principal; default; not adjustable; an IAM policy can grant or deny access.
  link: [only users that have the Administrator or PowerUser role can start a CloudShell session by default](../facts/management-console.md#management-console-cloudshell-faq-only-administrator-or-poweruser-by-default)
  link: [using an AWS Identity and Access Management (IAM) policy you can restrict the ability to launch CloudShell](../facts/management-console.md#management-console-cloudshell-faq-only-administrator-or-poweruser-by-default)
  say: by default only Administrator or PowerUser can start it
management-console-cloudshell-faq-same-privileges-as-console-login
  claim: In CloudShell you have only the privileges granted by your console login credentials, the same as installing and using the AWS CLI on your own machine with those credentials, and CloudShell usage is logged to CloudTrail with API calls annotated as coming from a user's CloudShell session.
  link: [no more, no less](../facts/management-console.md#management-console-cloudshell-faq-same-privileges-as-console-login)
  link: [CloudShell usage information is logged to AWS CloudTrail](../facts/management-console.md#management-console-cloudshell-faq-same-privileges-as-console-login)
  say: exactly the privileges of your console login, no more, no less
management-console-cloudshell-faq-software-persists-only-inside-home-directory
  claim: Software you install completely inside the CloudShell home directory persists across sessions; software installed outside the home directory does not persist.
  link: [Software installed completely within your home directory will persist across sessions](../facts/management-console.md#management-console-cloudshell-faq-software-persists-only-inside-home-directory)
  link: [Software installed outside of your home directory does not persist across sessions](../facts/management-console.md#management-console-cloudshell-faq-software-persists-only-inside-home-directory)
  say: only what is inside the home directory survives
management-console-cloudshell-faq-stops-after-keyboard-inactivity
  claim: CloudShell stops automatically after a period of keyboard inactivity; background processes do not count as activity and may be terminated without notice, and all sessions disconnect when the console session ends.
  link: [automatically stop after a period of keyboard input inactivity](../facts/management-console.md#management-console-cloudshell-faq-stops-after-keyboard-inactivity)
  link: [Processes running in the background do not constitute activity](../facts/management-console.md#management-console-cloudshell-faq-stops-after-keyboard-inactivity)
  link: [automatically disconnect all sessions when your console session ends](../facts/management-console.md#management-console-cloudshell-faq-stops-after-keyboard-inactivity)
  say: it stops after keyboard inactivity
management-console-cloudshell-faq-tools-preinstalled-no-local-install
  claim: Common development and operations tools, including the AWS CLI, are pre-installed in CloudShell, so there is no need to install or configure software on your local machine.
  link: [no need to install or configure software on your local machine](../facts/management-console.md#management-console-cloudshell-faq-tools-preinstalled-no-local-install)
  link: [contains common AWS command line interfaces, including AWS CLI](../facts/management-console.md#management-console-cloudshell-faq-tools-preinstalled-no-local-install)
  say: the CLI and common tools are already installed
management-console-cloudshell-faq-vpc-resources-accessible
  claim: CloudShell can access resources that are in your private VPC.
  link: [access resources that are in your private VPC](../facts/management-console.md#management-console-cloudshell-faq-vpc-resources-accessible)
  say: yes, CloudShell can reach resources in a private VPC
management-console-cloudshell-faq-vs-ec2-instance-connect
  claim: EC2 Instance Connect opens a browser terminal to an existing EC2 instance in your account, while CloudShell needs no resources in your account and is meant for running AWS CLI commands and general scripting.
  link: [CloudShell does not require any resources in your account](../facts/management-console.md#management-console-cloudshell-faq-vs-ec2-instance-connect)
  link: [CloudShell is most useful for running AWS CLI commands and general purpose scripting](../facts/management-console.md#management-console-cloudshell-faq-vs-ec2-instance-connect)
  say: Instance Connect needs an instance; CloudShell needs nothing in your account
management-console-cloudshell-no-additional-charge
  claim: AWS CloudShell has no additional charge; you pay for the other AWS resources you run with it, and standard data transfer rates apply.
  scope: AWS CloudShell.
  link: [available at no additional charge](../facts/management-console.md#management-console-cloudshell-no-additional-charge)
  link: [you pay for other AWS resources that you run with AWS CloudShell](../facts/management-console.md#management-console-cloudshell-no-additional-charge)
management-console-cloudshell-no-inbound-ports-no-public-ip
  claim: CloudShell can reach the public internet outbound, but you cannot access inbound ports and no public IP address is available.
  scope: CloudShell environment network.
  link: [No public IP address is available](../facts/management-console.md#management-console-cloudshell-no-inbound-ports-no-public-ip)
management-console-cloudshell-persistent-home-directory-per-region
  claim: CloudShell persistent storage is in your home directory, is private to you, and persists between sessions in each Region, unlike the ephemeral environment resources recycled after each session.
  link: [data in your home directory persists between sessions](../facts/management-console.md#management-console-cloudshell-persistent-home-directory-per-region)
  link: [Persistent storage is located in your home directory ($HOME) and is private to you](../facts/management-console.md#management-console-cloudshell-persistent-home-directory-per-region)
management-console-cloudshell-persistent-storage-1-gb-per-region
  claim: AWS CloudShell gives 1 GB of persistent storage per Region at no cost, in the home directory, which persists between sessions.
  scope: per Region, per user home directory; maximum; not adjustable.
  link: [1 GB](../facts/management-console.md#management-console-cloudshell-persistent-storage-1-gb-per-region)
management-console-cloudshell-region-follows-console-region
  claim: The CloudShell Region is in sync with the console Region selection; if CloudShell is not available in the selected Region it operates in the nearest Region.
  link: [The selection of the Console Region is in sync with the CloudShell Region](../facts/management-console.md#management-console-cloudshell-region-follows-console-region)
  link: [CloudShell will operate in the nearest Region](../facts/management-console.md#management-console-cloudshell-region-follows-console-region)
management-console-cloudshell-safe-paste-enabled-by-default
  claim: Safe Paste is enabled by default in CloudShell; it makes you verify that multiline text you paste does not contain malicious scripts.
  scope: AWS CloudShell, per environment; default; not adjustable.
  link: [Safe Paste is enabled by default](../facts/management-console.md#management-console-cloudshell-safe-paste-enabled-by-default)
  link: [verify that the multiline text that you want to paste into the shell doesn't contain malicious scripts](../facts/management-console.md#management-console-cloudshell-safe-paste-enabled-by-default)
management-console-cloudshell-session-ends-after-12-hours
  claim: A CloudShell session that runs continuously for approximately 12 hours ends automatically, even if the user keeps interacting with it.
  scope: per shell session; maximum; not adjustable.
  link: [approximately 12 hours](../facts/management-console.md#management-console-cloudshell-session-ends-after-12-hours)
management-console-cloudshell-session-ends-after-20-30-minutes-inactive
  claim: A CloudShell session ends after 20–30 minutes without keyboard or pointer interaction (10 minutes in AWS GovCloud (US) Regions); running processes do not count as interaction.
  scope: per shell session; fixed; not adjustable.
  link: [20–30 minutes](../facts/management-console.md#management-console-cloudshell-session-ends-after-20-30-minutes-inactive)
  link: [10 minutes](../facts/management-console.md#management-console-cloudshell-session-ends-after-20-30-minutes-inactive)
management-console-cloudshell-storage-deleted-after-120-days-unused
  claim: If you stop using CloudShell in a Region, its persistent storage is deleted automatically after 120 days unless you launch CloudShell in that Region again.
  scope: per Region, per user home directory; fixed; not adjustable; no CloudShell session in that Region.
  link: [120 days](../facts/management-console.md#management-console-cloudshell-storage-deleted-after-120-days-unused)
management-console-cloudshell-vpc-environments-no-persistent-storage
  claim: CloudShell VPC environments have no persistent storage: the home directory is deleted when the VPC environment times out or is deleted or restarted.
  scope: CloudShell VPC environments.
  link: [CloudShell VPC environments do not have persistent storage](../facts/management-console.md#management-console-cloudshell-vpc-environments-no-persistent-storage)
  link: [The $HOME directory is deleted when your VPC environment times out](../facts/management-console.md#management-console-cloudshell-vpc-environments-no-persistent-storage)
management-console-cloudshell-vpc-environments-two-per-principal
  claim: You can create up to two CloudShell VPC environments per IAM principal.
  scope: per IAM principal; maximum; not adjustable.
  link: [up to two VPC environments](../facts/management-console.md#management-console-cloudshell-vpc-environments-two-per-principal)
management-console-console-unified-navigation-features
  claim: The AWS Management Console is the web application that gives centralized access to every individual service console; its Unified Navigation lets you search for services, view notifications, open CloudShell, reach account and billing information and change general settings.
  link: [centralized access to all individual AWS service consoles](../facts/management-console.md#management-console-console-unified-navigation-features)
  link: [search for services, view notifications, access AWS CloudShell, access account and billing information, and customize your general console settings](../facts/management-console.md#management-console-console-unified-navigation-features)
  say: the console is the web application that gives you one place to reach every service console
management-console-default-region-last-visited-unless-set
  claim: If you do not set a default Region in Unified Settings, the console uses the last Region you visited; with IAM Identity Center sign-in the last-visited Region does not persist across sessions, so AWS says to set a specific default Region.
  scope: AWS Management Console default Region, per user (Unified Settings); default; not adjustable.
  link: [the console uses the last Region that you visited](../facts/management-console.md#management-console-default-region-last-visited-unless-set)
  link: [The last-visited Region doesn't persist across IAM Identity Center sessions](../facts/management-console.md#management-console-default-region-last-visited-unless-set)
management-console-default-region-set-in-unified-settings
  claim: The default Region is set from the Unified Settings page: gear icon, See all user settings, Edit next to Localization and default Region, choose a Region, Save settings.
  link: [Unified Settings](../facts/management-console.md#management-console-default-region-set-in-unified-settings)
  link: [Localization and default Region](../facts/management-console.md#management-console-default-region-set-in-unified-settings)
management-console-faq-find-service-services-menu-or-unified-search
  claim: To find a service in the Management Console you can open the Services menu in the top navigation bar to see all services grouped by category, or search for services with Unified Search; Console Home also offers Favorites and Recently visited widgets.
  link: [select the Services menu in the top level navigation bar](../facts/management-console.md#management-console-faq-find-service-services-menu-or-unified-search)
  link: [search for services using Unified Search](../facts/management-console.md#management-console-faq-find-service-services-menu-or-unified-search)
  say: the Services menu or Unified Search
management-console-faq-mobile-app-biometric-sign-in
  claim: Biometric authentication can be set up on supported iOS and Android devices running Console Mobile Application v2.0+.
  scope: supported iOS and Android devices running Console Mobile Application v2.0+.
  link: [biometrics authentication on supported iOS and Android devices running Console Mobile Application v2.0+](../facts/management-console.md#management-console-faq-mobile-app-biometric-sign-in)
  say: yes, on supported devices that run version 2.0 or later of the app
management-console-faq-mobile-app-can-assume-iam-roles
  claim: The Console Mobile App can assume IAM roles.
  link: [Yes, on iOS and Android V2.0+](../facts/management-console.md#management-console-faq-mobile-app-can-assume-iam-roles)
  say: yes, the mobile app can assume IAM roles
management-console-faq-mobile-app-cloudwatch-automatic-dashboards-not-supported
  claim: The Console Mobile App shows the CloudWatch custom dashboards your identity may access, but CloudWatch automatic dashboards are not yet supported in the app.
  scope: Console Mobile App, as stated on the FAQ snapshot date.
  link: [CloudWatch automatic dashboards are not yet supported in the AWS Console Mobile App](../facts/management-console.md#management-console-faq-mobile-app-cloudwatch-automatic-dashboards-not-supported)
  say: custom dashboards yes, automatic dashboards not yet
management-console-faq-mobile-app-create-resources-only-via-cloudshell
  claim: In the Console Mobile App the only way to create resources is through AWS CloudShell with the AWS CLI; the app's graphical interface lets you view and sometimes modify resources, but not create them.
  scope: Console Mobile App.
  link: [the only way to create resources from the mobile app is to do so through the AWS CloudShell service using the AWS Command Line Interface (AWS CLI)](../facts/management-console.md#management-console-faq-mobile-app-create-resources-only-via-cloudshell)
  link: [you cannot create resources through the graphical user interface](../facts/management-console.md#management-console-faq-mobile-app-create-resources-only-via-cloudshell)
  say: only through CloudShell and the CLI, not through the app's graphical interface
management-console-faq-mobile-app-fido-hardware-and-software-authenticators
  claim: The Console Mobile App supports all FIDO certified hardware authenticators, such as YubiKey, for MFA, and software authenticators such as Google Authenticator, Microsoft Authenticator and LastPass Authenticator.
  link: [all FIDO certified hardware authenticators](../facts/management-console.md#management-console-faq-mobile-app-fido-hardware-and-software-authenticators)
  say: any FIDO certified hardware key and common software authenticators
management-console-faq-mobile-app-mfa-supported
  claim: The Console Mobile App supports MFA, and AWS recommends a hardware MFA device or a virtual MFA on a separate mobile device for the greatest level of account protection.
  link: [a hardware MFA device or a virtual MFA on a separate mobile device](../facts/management-console.md#management-console-faq-mobile-app-mfa-supported)
  say: yes, MFA is supported; use a hardware device or a virtual MFA on a separate phone
management-console-faq-mobile-app-root-cannot-be-deactivated
  claim: If a mobile device is lost, an IAM user's credentials can be deactivated to prevent unauthorized access, but a root account cannot be deactivated.
  scope: Console Mobile App sign-in credentials.
  link: [Root accounts cannot be deactivated](../facts/management-console.md#management-console-faq-mobile-app-root-cannot-be-deactivated)
  link: [an IAM user can be deactivated to prevent unauthorized access](../facts/management-console.md#management-console-faq-mobile-app-root-cannot-be-deactivated)
  say: a root account cannot be deactivated
management-console-faq-mobile-app-s3-presigned-url-download
  claim: The Console Mobile App can generate a pre-signed URL for an S3 object; a pre-signed URL grants time-limited permission to download the object.
  link: [generate a pre-signed URL for an S3 object](../facts/management-console.md#management-console-faq-mobile-app-s3-presigned-url-download)
  link: [A pre-signed URL grants time-limited permission to download the object](../facts/management-console.md#management-console-faq-mobile-app-s3-presigned-url-download)
  say: it makes a pre-signed URL for the object
management-console-faq-mobile-app-sign-in-methods
  claim: The Console Mobile Application supports several sign-in methods: root credentials, IAM user credentials, and federated login through IAM Identity Center (formerly AWS Single Sign-On), Microsoft Active Directory and third-party identity providers; AWS recommends IAM user credentials or a federated role.
  link: [owner/root credentials, IAM user credentials, and federated login](../facts/management-console.md#management-console-faq-mobile-app-sign-in-methods)
  link: [We recommend using either IAM user credentials or a federated role to log in to the Console Mobile Application](../facts/management-console.md#management-console-faq-mobile-app-sign-in-methods)
  say: root, IAM user or federated sign in
management-console-faq-mobile-app-usage-charges-need-cloudwatch-permission
  claim: You can view current usage charges in the Console Mobile App after enabling billing alerts in Billing Preferences, and your identity must have permission to view CloudWatch to see them.
  link: [you can view your current usage charges in the Console Mobile Application](../facts/management-console.md#management-console-faq-mobile-app-usage-charges-need-cloudwatch-permission)
  link: [your identity must have permission to view CloudWatch](../facts/management-console.md#management-console-faq-mobile-app-usage-charges-need-cloudwatch-permission)
  say: yes, with CloudWatch permission and billing alerts enabled
management-console-faq-solutions-section-wizards
  claim: The Solutions section on Console Home holds simplified, automated workflows and wizards that use and introduce different AWS services, and that create the resources needed to build the intended solution.
  link: [simplified and automated workflows and wizards](../facts/management-console.md#management-console-faq-solutions-section-wizards)
  say: guided workflows and wizards
management-console-global-view-map-view-since-2026-08
  claim: AWS Global View in the AWS Management Console now offers an interactive map view that plots all AWS Regions and AWS Local Zones, and customers can toggle between it and the existing list view; previously, customers had to scan through a list of AWS locations in Global View.
  scope: AWS Global View in the AWS Management Console.
  link: [interactive map view](../facts/management-console.md#management-console-global-view-map-view-since-2026-08)
  changed: 2026-08-12: was a list of AWS locations
management-console-local-zones-in-region-selector
  claim: The console's Region selector has a Local Zones tab that lists all opted-in Local Zones; choosing a Local Zone opens its parent Region's console page.
  scope: AWS Management Console Region selector.
  link: [parent Region](../facts/management-console.md#management-console-local-zones-in-region-selector)
management-console-missing-resources-check-region
  claim: If resources you created do not appear in the console, the console may be showing a different Region; some resources, such as EC2 instances, are specific to the Region where they were created.
  link: [the console might be displaying resources from a different Region](../facts/management-console.md#management-console-missing-resources-check-region)
  link: [Some resources (such as Amazon EC2 instances) are specific to the Region where they were created](../facts/management-console.md#management-console-missing-resources-check-region)
management-console-multi-session-announced
  claim: AWS announced multi-session support for the console: customers can sign in to up to 5 sessions in a single browser, in any combination of root, IAM or federated roles in different accounts or the same account.
  scope: AWS Management Console; maximum.
  link: [up to 5 sessions](../facts/management-console.md#management-console-multi-session-announced)
management-console-multi-session-opt-in-per-browser
  claim: Multi-session support is an opt-in, and the opt-in is browser specific.
  scope: AWS Management Console multi-session.
  link: [browser specific](../facts/management-console.md#management-console-multi-session-opt-in-per-browser)
management-console-multi-session-up-to-five-identities
  claim: You can sign in to up to five different identities at the same time in a single web browser in the AWS Management Console, in any combination of root, IAM or federated roles in the same or different accounts.
  scope: per web browser; maximum; not adjustable; multi-session support turned on.
  link: [up to five different identities](../facts/management-console.md#management-console-multi-session-up-to-five-identities)
  link: [up to five](../facts/management-console.md#management-console-multi-session-up-to-five-identities)
management-console-pricing-calculator-free-estimates
  claim: AWS Pricing Calculator is a free web-based service for creating cost estimates of AWS use cases before building them; it estimates fees and charges excluding taxes and is for information only.
  link: [a web-based service that you can use to create cost estimates to suit your AWS use cases](../facts/management-console.md#management-console-pricing-calculator-free-estimates)
  link: [AWS Pricing Calculator is free for use](../facts/management-console.md#management-console-pricing-calculator-free-estimates)
management-console-private-access-100-percent-traffic-via-vpc-endpoints
  claim: Under Private Access the console can operate in VPCs without public internet access; Private Access controls 100% of the browser traffic through VPC endpoints.
  scope: AWS Management Console Private Access.
  link: [100% of the browser traffic](../facts/management-console.md#management-console-private-access-100-percent-traffic-via-vpc-endpoints)
management-console-private-access-all-traffic-through-vpc-endpoints-since-2026-06
  claim: Since 2026-06-15, console traffic under Private Access can flow through VPC endpoints for the supported service consoles, eliminating the need for internet access; before, Private Access still required internet connectivity.
  scope: AWS Management Console Private Access.
  link: [eliminating the need for any internet access](../facts/management-console.md#management-console-private-access-all-traffic-through-vpc-endpoints-since-2026-06)
  changed: 2026-06-15: was still required internet connectivity
management-console-private-access-limits-console-to-known-accounts-from-vpc
  claim: AWS Management Console Private Access limits console use to a specified set of known AWS accounts when the traffic originates from within your VPC, and routes console traffic through AWS PrivateLink VPC endpoints instead of the public internet.
  scope: AWS Management Console Private Access.
  link: [specified set of known AWS accounts](../facts/management-console.md#management-console-private-access-limits-console-to-known-accounts-from-vpc)
  link: [VPC endpoints](../facts/management-console.md#management-console-private-access-limits-console-to-known-accounts-from-vpc)
management-console-private-access-pay-only-for-privatelink-endpoints
  claim: Private Access has no price of its own: you pay only for the AWS PrivateLink VPC endpoint usage and data processing it uses.
  scope: AWS Management Console Private Access.
  link: [AWS PrivateLink VPC endpoint usage and data processing](../facts/management-console.md#management-console-private-access-pay-only-for-privatelink-endpoints)
management-console-root-user-complete-access
  claim: The root user is the account owner with complete access to all AWS services and resources; you are the root user if you created the account and sign in with the root user email and password.
  link: [the account owner with complete access to all AWS services and resources](../facts/management-console.md#management-console-root-user-complete-access)
  link: [sign in using your root user email and password](../facts/management-console.md#management-console-root-user-complete-access)
  say: the root user owns the account and can do everything
management-console-services-list-by-region-updated-daily
  claim: The AWS Services by Region page lists which services are available in each Region and is updated daily.
  link: [The AWS Services List is updated daily](../facts/management-console.md#management-console-services-list-by-region-updated-daily)
  link: [AWS Services by Region](../facts/management-console.md#management-console-services-list-by-region-updated-daily)
management-console-some-services-need-no-region-selection
  claim: For many services you choose a Region that specifies where resources are managed, but you do not need to choose a Region for the console itself or for some services such as IAM.
  link: [You don't need to choose a Region for the AWS Management Console or for some services, such as AWS Identity and Access Management](../facts/management-console.md#management-console-some-services-need-no-region-selection)
  link: [Regions are sets of AWS resources located in the same geographical area](../facts/management-console.md#management-console-some-services-need-no-region-selection)
  say: IAM is global; you never pick a Region for it
well-architected-abstracted-services-aws-runs-os-customer-manages-data
  claim: For abstracted services such as Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system and the platforms; the customer manages the data (including encryption options), classifies assets and uses IAM to set permissions.
  link: [AWS operates the infrastructure layer, the operating system, and platforms](../facts/well-architected.md#well-architected-abstracted-services-aws-runs-os-customer-manages-data)
  link: [managing their data (including encryption options), classifying their assets, and using IAM tools to apply the appropriate permissions](../facts/well-architected.md#well-architected-abstracted-services-aws-runs-os-customer-manages-data)
  say: for S3 and DynamoDB, AWS runs the platform; you own your data, its encryption and its permissions
well-architected-availability-99-9-percent-max-downtime
  claim: An availability goal of 99.9% allows at most 8 hours 45 minutes of unavailability per year; AWS pairs this tier with internal tools like knowledge management and project tracking.
  scope: per year.
  link: [99.9%](../facts/well-architected.md#well-architected-availability-99-9-percent-max-downtime)
  link: [8 hours 45 minutes](../facts/well-architected.md#well-architected-availability-99-9-percent-max-downtime)
well-architected-availability-99-95-percent-max-downtime
  claim: An availability goal of 99.95% allows at most 4 hours 22 minutes of unavailability per year; AWS pairs this tier with online commerce and point of sale.
  scope: per year.
  link: [99.95%](../facts/well-architected.md#well-architected-availability-99-95-percent-max-downtime)
  link: [4 hours 22 minutes](../facts/well-architected.md#well-architected-availability-99-95-percent-max-downtime)
well-architected-availability-99-99-percent-max-downtime
  claim: An availability goal of 99.99% allows at most 52 minutes of unavailability per year; AWS pairs this tier with video delivery and broadcast workloads.
  scope: per year.
  link: [99.99%](../facts/well-architected.md#well-architected-availability-99-99-percent-max-downtime)
  link: [52 minutes](../facts/well-architected.md#well-architected-availability-99-99-percent-max-downtime)
well-architected-availability-99-999-percent-max-downtime
  claim: An availability goal of 99.999% allows at most 5 minutes of unavailability per year; AWS pairs this tier with ATM transactions and telecommunications workloads.
  scope: per year.
  link: [99.999%](../facts/well-architected.md#well-architected-availability-99-999-percent-max-downtime)
  link: [5 minutes](../facts/well-architected.md#well-architected-availability-99-999-percent-max-downtime)
well-architected-availability-99-percent-max-downtime
  claim: An availability goal of 99% allows at most 3 days 15 hours of unavailability per year; AWS pairs this tier with batch processing, data extraction, transfer and load jobs.
  scope: per year.
  link: [99%](../facts/well-architected.md#well-architected-availability-99-percent-max-downtime)
  link: [3 days 15 hours](../facts/well-architected.md#well-architected-availability-99-percent-max-downtime)
well-architected-availability-definition
  claim: Availability is the percentage of time that a workload is available for use, where available for use means it performs its agreed function successfully when required.
  scope: reliability pillar.
  link: [percentage of time that a workload is available for use](../facts/well-architected.md#well-architected-availability-definition)
well-architected-availability-excluding-planned-downtime-not-advised
  claim: AWS advises against excluding scheduled downtime such as planned maintenance from the availability calculation, because users will likely want to use the service during those times.
  scope: availability calculation.
  link: [this is not advised](../facts/well-architected.md#well-architected-availability-excluding-planned-downtime-not-advised)
well-architected-availability-hard-dependency-product-rule
  claim: With hard dependencies the invoking system's availability is the product of the dependencies' availabilities: a 99.99% system with hard dependencies on two 99.99% systems can theoretically reach 99.97%.
  link: [the invoking system’s availability is the product of the dependent systems’ availabilities](../facts/well-architected.md#well-architected-availability-hard-dependency-product-rule)
  link: [99.97% availability](../facts/well-architected.md#well-architected-availability-hard-dependency-product-rule)
well-architected-availability-redundant-components-sum-the-nines
  claim: With independent redundant components, availability is 100% minus the product of the component failure rates: two independent components at 99.9% give 99.9999%, and when all values are only nines you can add the counts of nines.
  link: [100% minus the product of the component failure rates](../facts/well-architected.md#well-architected-availability-redundant-components-sum-the-nines)
  link: [two redundant, independent components with three nines availability results in six nines](../facts/well-architected.md#well-architected-availability-redundant-components-sum-the-nines)
well-architected-awareness-training-is-a-shared-control
  claim: Awareness and training is a shared control: AWS trains AWS employees, and a customer must train their own employees.
  link: [AWS trains AWS employees, but a customer must train their own employees](../facts/well-architected.md#well-architected-awareness-training-is-a-shared-control)
  link: [Awareness & Training](../facts/well-architected.md#well-architected-awareness-training-is-a-shared-control)
well-architected-aws-controls-host-os-virtualization-and-facilities
  claim: AWS operates, manages and controls the components from the host operating system and virtualization layer down to the physical security of the facilities where the service runs.
  link: [from the host operating system and virtualization layer down to the physical security of the facilities](../facts/well-architected.md#well-architected-aws-controls-host-os-virtualization-and-facilities)
  link: [host operating system and virtualization layer](../facts/well-architected.md#well-architected-aws-controls-host-os-virtualization-and-facilities)
  say: AWS owns everything from the host operating system down to the building
well-architected-aws-infrastructure-aligned-with-security-standards
  claim: The infrastructure AWS provides is designed and managed in alignment with security best practices and a variety of IT security standards, and AWS documents its IT control environment in whitepapers, reports, certifications, accreditations and third-party attestations.
  link: [designed and managed in alignment with best security practices and a variety of IT security standards](../facts/well-architected.md#well-architected-aws-infrastructure-aligned-with-security-standards)
  link: [whitepapers, reports, certifications, accreditations, and other third-party attestations](../facts/well-architected.md#well-architected-aws-infrastructure-aligned-with-security-standards)
well-architected-aws-responsible-for-infrastructure-security-of-the-cloud
  claim: AWS is responsible for protecting the infrastructure that runs all AWS Cloud services: the hardware, software, networking and facilities.
  link: [protecting the infrastructure that runs all of the services offered in the AWS Cloud](../facts/well-architected.md#well-architected-aws-responsible-for-infrastructure-security-of-the-cloud)
  link: [the hardware, software, networking, and facilities that run AWS Cloud services](../facts/well-architected.md#well-architected-aws-responsible-for-infrastructure-security-of-the-cloud)
well-architected-bulkhead-cell-based-architecture-definition
  claim: A bulkhead (cell-based) architecture restricts the effect of a failure to a limited number of components: the workload runs as multiple isolated cells, each independent, sharing no state, and handling a subset of requests.
  link: [restrict the effect of failure within a workload to a limited number of components](../facts/well-architected.md#well-architected-bulkhead-cell-based-architecture-definition)
  link: [Each cell is independent, does not share state with other cells, and handles a subset of the overall workload requests](../facts/well-architected.md#well-architected-bulkhead-cell-based-architecture-definition)
well-architected-case-burns-mcdonnell-30-percent-cost-reduction
  claim: By using Conformity, an AWS Well-Architected Partner Solution, and adopting the AWS Well-Architected Framework, Burns & McDonnell reduced costs by 30 percent year over year; a quote from the firm in the case study says it saved about 30 percent of its overall AWS bill in the first week by taking action, and reduced waste by identifying overprovisioned instances.
  link: [reduced costs by 30 percent year over year](../facts/well-architected.md#well-architected-case-burns-mcdonnell-30-percent-cost-reduction)
  link: [We saved about 30 percent of our overall AWS bill in the first week by taking action](../facts/well-architected.md#well-architected-case-burns-mcdonnell-30-percent-cost-reduction)
well-architected-case-burns-mcdonnell-50-percent-faster-resolution
  claim: By using the partner tool Conformity and adopting the Well-Architected Framework, Burns & McDonnell cut mean time to resolution for cloud misconfigurations by 50 percent.
  link: [a 50 percent reduction in mean time to resolution](../facts/well-architected.md#well-architected-case-burns-mcdonnell-50-percent-faster-resolution)
well-architected-case-vanguard-well-architected-tool-resilience
  claim: Vanguard used the AWS Well-Architected Tool, with Lambda, Step Functions and EventBridge, to communicate best practices internally and build more resilient applications; its domain architect says the team started from the Well-Architected Framework as a baseline.
  link: [better communicate best practices internally and build more resilient applications](../facts/well-architected.md#well-architected-case-vanguard-well-architected-tool-resilience)
  link: [We started with a baseline of the AWS Well-Architected Framework](../facts/well-architected.md#well-architected-case-vanguard-well-architected-tool-resilience)
well-architected-cell-example-10-cells-90-percent-unaffected
  claim: In AWS's cell example, a workload with 10 cells serving 100 requests keeps 90% of requests unaffected when one cell fails.
  link: [If a workload uses 10 cells to service 100 requests, when a failure occurs, 90% of the overall requests would be unaffected](../facts/well-architected.md#well-architected-cell-example-10-cells-90-percent-unaffected)
  link: [10 cells](../facts/well-architected.md#well-architected-cell-example-10-cells-90-percent-unaffected)
well-architected-cheaper-region-for-non-critical-when-no-restrictions
  claim: If you have no obligations in data privacy, security and business requirements, use Regions with lower prices for your workloads; AWS's example: if your default Region is Asia Pacific (Sydney), deploying non-critical development and test EC2 instances in US East (N. Virginia) (us-east-1) will cost you less.
  link: [Use Regions that provide lower prices for AWS services to deploy your workloads if you have no obligations in data privacy, security and business requirements](../facts/well-architected.md#well-architected-cheaper-region-for-non-critical-when-no-restrictions)
  link: [deploying non-critical (development and test) Amazon EC2 instances in US East (N. Virginia) (us-east-1) will cost you less](../facts/well-architected.md#well-architected-cheaper-region-for-non-critical-when-no-restrictions)
well-architected-compliance-is-shared-responsibility
  claim: Compliance is a shared responsibility between AWS and the customer, and customers can build on the security controls AWS applies to its infrastructure.
  link: [Compliance is a shared responsibility between AWS and the customer](../facts/well-architected.md#well-architected-compliance-is-shared-responsibility)
  link: [building on top of the security controls AWS uses on its infrastructure](../facts/well-architected.md#well-architected-compliance-is-shared-responsibility)
well-architected-configuration-management-is-a-shared-control
  claim: Configuration management is a shared control: AWS maintains the configuration of its infrastructure devices, and the customer configures their own guest operating systems, databases and applications.
  link: [AWS maintains the configuration of its infrastructure devices](../facts/well-architected.md#well-architected-configuration-management-is-a-shared-control)
  link: [configuring their own guest operating systems, databases, and applications](../facts/well-architected.md#well-architected-configuration-management-is-a-shared-control)
well-architected-consumption-model-dev-test-75-percent-example
  claim: AWS's consumption-model example: development and test environments typically run only eight hours a day during the work week, so stopping them when not in use can save up to 75% (40 hours versus 168 hours).
  link: [a potential cost savings of 75% (40 hours versus 168 hours)](../facts/well-architected.md#well-architected-consumption-model-dev-test-75-percent-example)
  link: [only used for eight hours a day during the work week](../facts/well-architected.md#well-architected-consumption-model-dev-test-75-percent-example)
well-architected-cost-optimization-design-principles
  claim: The five cost optimization design principles are: implement Cloud Financial Management; adopt a consumption model; measure overall efficiency; stop spending money on undifferentiated heavy lifting; analyze and attribute expenditure.
  link: [Implement Cloud Financial Management](../facts/well-architected.md#well-architected-cost-optimization-design-principles)
  link: [Adopt a consumption model](../facts/well-architected.md#well-architected-cost-optimization-design-principles)
  link: [Measure overall efficiency](../facts/well-architected.md#well-architected-cost-optimization-design-principles)
  link: [Stop spending money on undifferentiated heavy lifting](../facts/well-architected.md#well-architected-cost-optimization-design-principles)
  link: [Analyze and attribute expenditure](../facts/well-architected.md#well-architected-cost-optimization-design-principles)
well-architected-customer-responsibility-varies-by-service-region-law
  claim: Customer responsibility varies with the AWS services and Regions chosen, how those services are integrated into the IT environment, and the laws and regulations that apply to the organization and workload.
  link: [the AWS services and Regions they choose](../facts/well-architected.md#well-architected-customer-responsibility-varies-by-service-region-law)
  link: [the laws and regulations applicable to their organization and workload](../facts/well-architected.md#well-architected-customer-responsibility-varies-by-service-region-law)
well-architected-customer-responsible-for-guest-os-apps-security-groups
  claim: The customer is responsible for the guest operating system (including updates and security patches), the application software, and the configuration of the AWS-provided security group firewall.
  link: [guest operating system (including updates and security patches)](../facts/well-architected.md#well-architected-customer-responsible-for-guest-os-apps-security-groups)
  link: [configuration of the AWS provided security group firewall](../facts/well-architected.md#well-architected-customer-responsible-for-guest-os-apps-security-groups)
  say: you patch the guest OS, your apps, and you configure the security groups
well-architected-customer-specific-controls-definition
  claim: Customer-specific controls are solely the customer's responsibility and depend on the application deployed; AWS's example is service and communications protection or zone security, such as routing data within specific security environments.
  link: [solely the responsibility of the customer based on the application they are deploying](../facts/well-architected.md#well-architected-customer-specific-controls-definition)
  link: [Service and Communications Protection or Zone Security](../facts/well-architected.md#well-architected-customer-specific-controls-definition)
well-architected-data-transfer-cost-keep-data-close
  claim: Consider data transfer costs when selecting Regions: keep data close to customers and resources and choose Regions where data flows with minimal transfer.
  link: [Consider data transfer costs when selecting Regions](../facts/well-architected.md#well-architected-data-transfer-cost-keep-data-close)
  link: [Keep your data close to your customer and close to the resources](../facts/well-architected.md#well-architected-data-transfer-cost-keep-data-close)
well-architected-dr-differs-from-availability
  claim: Disaster recovery focuses on one-time recovery objectives for natural disasters, large-scale technical failures or human threats, while availability measures mean resiliency over a period of time against component failures, load spikes or software bugs.
  scope: disaster recovery objectives.
  link: [one-time recovery objectives](../facts/well-architected.md#well-architected-dr-differs-from-availability)
  link: [mean resiliency over a period of time](../facts/well-architected.md#well-architected-dr-differs-from-availability)
well-architected-ec2-is-iaas-customer-does-all-security-configuration
  claim: Amazon EC2 is categorized as Infrastructure as a Service (IaaS), so the customer must perform all of the necessary security configuration and management tasks for it.
  link: [categorized as Infrastructure as a Service (IaaS)](../facts/well-architected.md#well-architected-ec2-is-iaas-customer-does-all-security-configuration)
  link: [requires the customer to perform all of the necessary security configuration and management tasks](../facts/well-architected.md#well-architected-ec2-is-iaas-customer-does-all-security-configuration)
well-architected-faq-apis-extend-into-governance-workflows
  claim: The Well-Architected APIs let you extend Well-Architected functionality, best practices, measurements and learnings into your existing architecture governance processes, applications and workflows.
  link: [use the Well-Architected APIs](../facts/well-architected.md#well-architected-faq-apis-extend-into-governance-workflows)
  say: there are Well-Architected APIs
well-architected-faq-custom-lens-definition
  claim: A custom lens lets you review a workload with your own questions, in the same way you review workloads against the Framework and AWS-provided lenses; a custom lens can include pillars, questions, answer choices, helpful resources and improvement plans.
  link: [review your workload using customized questions](../facts/well-architected.md#well-architected-faq-custom-lens-definition)
  link: [pillars, questions, answer choices, helpful resources, and improvement plans](../facts/well-architected.md#well-architected-faq-custom-lens-definition)
  say: a custom lens is your own set of review questions
well-architected-faq-framework-consistent-approach-improve-over-time
  claim: The AWS Well-Architected Framework lets you review architectures with a consistent approach and gives guidance to improve designs over time.
  link: [review your architectures using a consistent approach](../facts/well-architected.md#well-architected-faq-framework-consistent-approach-improve-over-time)
  link: [guidance to improve designs over time](../facts/well-architected.md#well-architected-faq-framework-consistent-approach-improve-over-time)
  say: the Framework is a consistent way to review architectures and improve them over time
well-architected-faq-partner-trained-on-framework-for-review-help
  claim: For help with workload reviews and improvement initiatives, AWS points you to a partner who has been trained on the Well-Architected Framework.
  link: [a partner who has been trained on the AWS Well-Architected Framework](../facts/well-architected.md#well-architected-faq-partner-trained-on-framework-for-review-help)
  say: a trained Well-Architected partner
well-architected-faq-review-answer-questions-per-pillar-get-improvement-plan
  claim: In a Well-Architected review you define the workload, answer questions across each pillar, and the Tool evaluates the answers and produces an improvement plan with a prioritized list of issues for the workload.
  link: [answer questions across each of the architectural pillars](../facts/well-architected.md#well-architected-faq-review-answer-questions-per-pillar-get-improvement-plan)
  link: [an improvement plan with a prioritized list of issues for the workload](../facts/well-architected.md#well-architected-faq-review-answer-questions-per-pillar-get-improvement-plan)
  say: you answer questions for each pillar
well-architected-faq-review-at-major-milestones
  claim: AWS recommends performing a Well-Architected workload review at major milestones in the development cycle.
  link: [at major milestones in your development cycle](../facts/well-architected.md#well-architected-faq-review-at-major-milestones)
  say: review at major milestones of the development cycle
well-architected-faq-share-workloads-and-custom-lenses
  claim: You can share workloads and custom lenses that you own with other AWS accounts, with IAM users in the same Region, and with AWS Organizations.
  link: [Share workloads and custom lenses that you own with other AWS accounts](../facts/well-architected.md#well-architected-faq-share-workloads-and-custom-lenses)
  say: you can share workloads and custom lenses with other accounts and with Organizations
well-architected-faq-six-pillars-named
  claim: The Framework's design principles and best practices are organized into six conceptual areas, the pillars: operational excellence, security, reliability, performance efficiency, cost optimization and sustainability.
  link: [six pillars](../facts/well-architected.md#well-architected-faq-six-pillars-named)
  link: [operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability](../facts/well-architected.md#well-architected-faq-six-pillars-named)
  say: six pillars | operational excellence, security, reliability, performance efficiency, cost optimization and sustainability
well-architected-faq-tool-accessed-from-management-console
  claim: You access the AWS Well-Architected Tool by signing in to the AWS Management Console with your AWS account.
  link: [signing in to the AWS Management Console with your AWS account](../facts/well-architected.md#well-architected-faq-tool-accessed-from-management-console)
  say: it is in the Management Console
well-architected-faq-tool-delivers-issues-and-step-by-step-guidance
  claim: The Well-Architected Tool delivers a list of potential issues found in your workloads and gives step-by-step guidance to make improvements; you can also view the issues found across your whole portfolio of workloads.
  link: [a list of potential issues found in your workloads](../facts/well-architected.md#well-architected-faq-tool-delivers-issues-and-step-by-step-guidance)
  link: [step-by-step guidance to make improvements](../facts/well-architected.md#well-architected-faq-tool-delivers-issues-and-step-by-step-guidance)
  say: a list of potential issues and step by step guidance
well-architected-faq-tool-no-additional-charge
  claim: There is no additional charge for the AWS Well-Architected Tool; you pay only for the underlying AWS resources.
  link: [no additional charge](../facts/well-architected.md#well-architected-faq-tool-no-additional-charge)
  link: [You pay only for your underlying AWS resources](../facts/well-architected.md#well-architected-faq-tool-no-additional-charge)
  say: no additional charge
well-architected-faq-tool-reviews-workloads-against-best-practices
  claim: The AWS Well-Architected Tool lets you review your workloads against current AWS best practices and get advice on how to architect them for the cloud; it uses the AWS Well-Architected Framework.
  link: [review your workloads against current AWS best practices](../facts/well-architected.md#well-architected-faq-tool-reviews-workloads-against-best-practices)
  link: [This tool uses the AWS Well-Architected Framework](../facts/well-architected.md#well-architected-faq-tool-reviews-workloads-against-best-practices)
  say: the Tool reviews a workload against AWS best practices
well-architected-faq-workload-definition
  claim: A workload is the collection of resources and code that make up a cloud application.
  link: [the collection of resources and code that make up a cloud application](../facts/well-architected.md#well-architected-faq-workload-definition)
  say: a workload is the resources and code that make up one cloud application
well-architected-five-nines-is-99-999-percent
  claim: "Five nines" is short-hand for 99.999% availability.
  scope: availability short-hand.
  link: [99.999%](../facts/well-architected.md#well-architected-five-nines-is-99-999-percent)
  link: [five nines](../facts/well-architected.md#well-architected-five-nines-is-99-999-percent)
well-architected-framework-definition-best-practices-and-questions
  claim: The AWS Well-Architected Framework is a consistent set of best practices for evaluating architectures and a set of questions for judging how well an architecture aligns with AWS best practices.
  link: [a consistent set of best practices for customers and partners to evaluate architectures](../facts/well-architected.md#well-architected-framework-definition-best-practices-and-questions)
  link: [a set of questions you can use to evaluate how well an architecture is aligned to AWS best practices](../facts/well-architected.md#well-architected-framework-definition-best-practices-and-questions)
  say: a set of best practices and questions to check an architecture against AWS guidance
well-architected-general-design-principles
  claim: The general design principles are: stop guessing your capacity needs; test systems at production scale; automate with architectural experimentation in mind; consider evolutionary architectures; drive architectures using data; improve through game days.
  link: [Stop guessing your capacity needs](../facts/well-architected.md#well-architected-general-design-principles)
  link: [Test systems at production scale](../facts/well-architected.md#well-architected-general-design-principles)
  link: [Automate with architectural experimentation in mind](../facts/well-architected.md#well-architected-general-design-principles)
  link: [Consider evolutionary architectures](../facts/well-architected.md#well-architected-general-design-principles)
  link: [Drive architectures using data](../facts/well-architected.md#well-architected-general-design-principles)
  link: [Improve through game days](../facts/well-architected.md#well-architected-general-design-principles)
well-architected-generative-ai-lens-released
  claim: AWS released the Well-Architected Generative AI Lens, a guidance document for generative AI workloads that covers all six Well-Architected pillars.
  scope: Well-Architected lenses.
  link: [Well-Architected Generative AI Lens](../facts/well-architected.md#well-architected-generative-ai-lens-released)
well-architected-inherited-controls-definition
  claim: Inherited controls are controls that a customer fully inherits from AWS; AWS's example is physical and environmental controls.
  link: [Controls which a customer fully inherits from AWS](../facts/well-architected.md#well-architected-inherited-controls-definition)
  link: [inherited controls](../facts/well-architected.md#well-architected-inherited-controls-definition)
well-architected-least-privilege-and-no-long-term-credentials
  claim: A strong identity foundation means least privilege, separation of duties with appropriate authorization for each interaction, centralized identity management, and aiming to eliminate reliance on long-term static credentials.
  link: [Implement the principle of least privilege and enforce separation of duties](../facts/well-architected.md#well-architected-least-privilege-and-no-long-term-credentials)
  link: [aim to eliminate reliance on long-term static credentials](../facts/well-architected.md#well-architected-least-privilege-and-no-long-term-credentials)
  say: least privilege, central identity, and no long-term keys
well-architected-least-privilege-anti-patterns
  claim: Common least-privilege anti-patterns named by the Security pillar include granting users administrator permissions by default and using the root user for daily activities.
  link: [By default, you grant users administrator permissions](../facts/well-architected.md#well-architected-least-privilege-anti-patterns)
well-architected-least-privilege-desired-outcome
  claim: The Security pillar's desired outcome for least privilege: users have only the minimum permissions for their job, developers are isolated from production with separate accounts, and production access is limited to the duration of a task and revoked afterwards.
  link: [Users have only the minimum permissions required for their specific job functions](../facts/well-architected.md#well-architected-least-privilege-desired-outcome)
  link: [You use separate AWS accounts to isolate developers from production environments](../facts/well-architected.md#well-architected-least-privilege-desired-outcome)
well-architected-major-update-2023-04
  claim: On April 10, 2023 the Well-Architected Framework had a major update: best practices gained prescriptive guidance, new best practices were added, and new questions were added to the Security and Cost Optimization pillars.
  scope: AWS Well-Architected Framework.
  link: [April 10, 2023](../facts/well-architected.md#well-architected-major-update-2023-04)
well-architected-major-update-2023-10
  claim: On October 3, 2023 the Well-Architected Framework had a major update described by AWS only as major pillar updates.
  scope: AWS Well-Architected Framework.
  link: [October 3, 2023](../facts/well-architected.md#well-architected-major-update-2023-10)
well-architected-major-update-2024-06
  claim: On June 27, 2024 the Well-Architected Framework had a major update with large-scale best practice updates throughout the pillars; Security and Cost both received new best practices.
  scope: AWS Well-Architected Framework.
  link: [June 27, 2024](../facts/well-architected.md#well-architected-major-update-2024-06)
well-architected-major-update-2024-11
  claim: On November 6, 2024 the Well-Architected Framework had a major update: the Reliability pillar received a large-scale refresh, Security and Operational excellence guidance was updated with new service and generative AI suggestions, and Sustainability gained a new best practice.
  scope: AWS Well-Architected Framework.
  link: [November 6, 2024](../facts/well-architected.md#well-architected-major-update-2024-11)
well-architected-multi-az-is-ha-and-dr-multi-region-active-passive
  claim: Deploying across multiple Availability Zones in a Region is part of a high availability strategy and also part of a DR strategy; DR strategies may also use multiple Regions, for example active/passive failover from the active Region to the DR Region.
  link: [Deploying your workload across multiple Availability Zones in an AWS Region is part of a high availability strategy](../facts/well-architected.md#well-architected-multi-az-is-ha-and-dr-multi-region-active-passive)
  link: [DR strategies may also make use of multiple AWS Regions](../facts/well-architected.md#well-architected-multi-az-is-ha-and-dr-multi-region-active-passive)
well-architected-multi-tenant-managed-services-aws-patches-without-customer-action
  claim: For managed services on multi-tenant architectures such as ElastiCache Serverless, DynamoDB and S3, AWS applies patches without requiring customer action.
  link: [Apply patches without requiring customer action](../facts/well-architected.md#well-architected-multi-tenant-managed-services-aws-patches-without-customer-action)
  link: [multi-tenant architectures (such as Amazon ElastiCache Serverless, Amazon DynamoDB, and Amazon S3)](../facts/well-architected.md#well-architected-multi-tenant-managed-services-aws-patches-without-customer-action)
well-architected-operational-excellence-design-principles
  claim: The operational excellence design principles are: organize teams around business outcomes; implement observability for actionable insights; safely automate where possible; make frequent, small, reversible changes; refine operations procedures frequently; anticipate failure; learn from all operational events and metrics; use managed services.
  link: [Organize teams around business outcomes](../facts/well-architected.md#well-architected-operational-excellence-design-principles)
  link: [Implement observability for actionable insights](../facts/well-architected.md#well-architected-operational-excellence-design-principles)
  link: [Safely automate where possible](../facts/well-architected.md#well-architected-operational-excellence-design-principles)
  link: [Make frequent, small, reversible changes](../facts/well-architected.md#well-architected-operational-excellence-design-principles)
  link: [Refine operations procedures frequently](../facts/well-architected.md#well-architected-operational-excellence-design-principles)
  link: [Anticipate failure](../facts/well-architected.md#well-architected-operational-excellence-design-principles)
  link: [Learn from all operational events and metrics](../facts/well-architected.md#well-architected-operational-excellence-design-principles)
  link: [Use managed services](../facts/well-architected.md#well-architected-operational-excellence-design-principles)
well-architected-patch-management-is-a-shared-control
  claim: Patch management is a shared control: AWS patches and fixes flaws within the infrastructure, and customers patch their guest OS and applications.
  link: [AWS is responsible for patching and fixing flaws within the infrastructure](../facts/well-architected.md#well-architected-patch-management-is-a-shared-control)
  link: [customers are responsible for patching their guest OS and applications](../facts/well-architected.md#well-architected-patch-management-is-a-shared-control)
  say: AWS patches the infrastructure; you patch your guest OS and applications
well-architected-performance-efficiency-design-principles
  claim: The five performance efficiency design principles are: democratize advanced technologies; go global in minutes; use serverless architectures; experiment more often; consider mechanical sympathy.
  link: [Democratize advanced technologies](../facts/well-architected.md#well-architected-performance-efficiency-design-principles)
  link: [Go global in minutes](../facts/well-architected.md#well-architected-performance-efficiency-design-principles)
  link: [Use serverless architectures](../facts/well-architected.md#well-architected-performance-efficiency-design-principles)
  link: [Experiment more often](../facts/well-architected.md#well-architected-performance-efficiency-design-principles)
  link: [Consider mechanical sympathy](../facts/well-architected.md#well-architected-performance-efficiency-design-principles)
well-architected-pillar-cost-optimization-definition
  claim: Cost optimization is the ability to run systems to deliver business value at the lowest price point.
  scope: AWS Well-Architected Framework pillars.
  link: [lowest price point](../facts/well-architected.md#well-architected-pillar-cost-optimization-definition)
well-architected-pillar-operational-excellence-definition
  claim: Operational excellence is the ability to support development and run workloads effectively, gain insight into their operations, and continuously improve supporting processes and procedures to deliver business value.
  scope: AWS Well-Architected Framework pillars.
  link: [gain insight into their operations](../facts/well-architected.md#well-architected-pillar-operational-excellence-definition)
well-architected-pillar-performance-efficiency-definition
  claim: Performance efficiency is the ability to use computing resources efficiently to meet system requirements and to keep that efficiency as demand changes and technologies evolve.
  scope: AWS Well-Architected Framework pillars.
  link: [use computing resources efficiently](../facts/well-architected.md#well-architected-pillar-performance-efficiency-definition)
well-architected-pillar-reliability-definition
  claim: The reliability pillar is the ability of a workload to perform its intended function correctly and consistently when it is expected to, including the ability to operate and test the workload through its total lifecycle.
  scope: AWS Well-Architected Framework pillars.
  link: [perform its intended function correctly and consistently](../facts/well-architected.md#well-architected-pillar-reliability-definition)
well-architected-pillar-security-definition
  claim: The security pillar describes how to take advantage of cloud technologies to protect data, systems and assets in a way that can improve your security posture.
  scope: AWS Well-Architected Framework pillars.
  link: [protect data, systems, and assets](../facts/well-architected.md#well-architected-pillar-security-definition)
well-architected-pillar-sustainability-definition
  claim: Sustainability is the ability to continually improve sustainability impacts by reducing energy consumption and increasing efficiency across all components of a workload, maximizing the benefits of provisioned resources and minimizing the total resources required.
  scope: AWS Well-Architected Framework pillars.
  link: [reducing energy consumption and increasing efficiency](../facts/well-architected.md#well-architected-pillar-sustainability-definition)
well-architected-region-choice-affects-carbon-footprint
  claim: The choice of Region significantly affects a workload's performance, cost and carbon footprint, so Regions should be chosen on business requirements and sustainability goals together.
  link: [significantly affects its KPIs, including performance, cost, and carbon footprint](../facts/well-architected.md#well-architected-region-choice-affects-carbon-footprint)
  link: [based on both business requirements and sustainability goals](../facts/well-architected.md#well-architected-region-choice-affects-carbon-footprint)
well-architected-region-choice-closer-to-users-latency-sovereignty
  claim: A best practice is to place computing resources closer to users for lower latency and strong data sovereignty, choosing the location by business, data privacy, performance and security requirements, and using multiple locations for global end users.
  link: [place computing resources closer to users to provide lower latency and strong data sovereignty](../facts/well-architected.md#well-architected-region-choice-closer-to-users-latency-sovereignty)
  link: [For applications with global end users, use multiple locations](../facts/well-architected.md#well-architected-region-choice-closer-to-users-latency-sovereignty)
well-architected-region-pricing-differs-choose-by-cost
  claim: Resource pricing may differ in each Region because of local land, fiber, electricity and tax costs; COST07-BP02 says to deploy in higher-cost Regions only to meet latency, data residency and data sovereignty requirements.
  link: [Resource pricing may be different in each Region](../facts/well-architected.md#well-architected-region-pricing-differs-choose-by-cost)
  link: [only deploy in Regions with higher costs to meet latency, data residency and data sovereignty requirements](../facts/well-architected.md#well-architected-region-pricing-differs-choose-by-cost)
  say: prices differ by Region; pay more only when latency or residency demands it
well-architected-reliability-design-principles
  claim: The five reliability design principles are: automatically recover from failure; test recovery procedures; scale horizontally to increase aggregate workload availability; stop guessing capacity; manage change through automation.
  link: [Automatically recover from failure](../facts/well-architected.md#well-architected-reliability-design-principles)
  link: [Test recovery procedures](../facts/well-architected.md#well-architected-reliability-design-principles)
  link: [Scale horizontally to increase aggregate workload availability](../facts/well-architected.md#well-architected-reliability-design-principles)
  link: [Stop guessing capacity](../facts/well-architected.md#well-architected-reliability-design-principles)
  link: [Manage change through automation](../facts/well-architected.md#well-architected-reliability-design-principles)
well-architected-rely-on-centralized-identity-provider-for-workforce
  claim: Security pillar best practice SEC02-BP04: for workforce identities, rely on a centralized identity provider, so that access is created, assigned, revoked and audited from a single location.
  scope: workforce identities (employees and contractors).
  link: [rely on an identity provider that allows you to manage identities in a centralized place](../facts/well-architected.md#well-architected-rely-on-centralized-identity-provider-for-workforce)
  link: [creating, assigning, managing, revoking, and auditing access from a single location](../facts/well-architected.md#well-architected-rely-on-centralized-identity-provider-for-workforce)
well-architected-resiliency-definition
  claim: Resiliency is the ability of a workload to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions such as misconfigurations or transient network issues.
  link: [recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions](../facts/well-architected.md#well-architected-resiliency-definition)
well-architected-resiliency-ec2-customer-deploys-across-azs
  claim: For EC2 the customer performs all resiliency configuration: deploying instances across multiple locations such as Availability Zones, implementing self-healing with services like Auto Scaling, and following resilient architecture practices for the applications on the instances.
  link: [deploying Amazon EC2 instances across multiple locations (such as AWS Availability Zones)](../facts/well-architected.md#well-architected-resiliency-ec2-customer-deploys-across-azs)
  link: [implementing self-healing using services like Auto Scaling](../facts/well-architected.md#well-architected-resiliency-ec2-customer-deploys-across-azs)
well-architected-resiliency-is-shared-of-versus-in
  claim: Resiliency is also shared: AWS is responsible for the resiliency of the infrastructure that runs all AWS Cloud services, and the customer's responsibility is determined by the services they select.
  link: [Resiliency is a shared responsibility between AWS and you](../facts/well-architected.md#well-architected-resiliency-is-shared-of-versus-in)
  link: [AWS is responsible for resiliency of the infrastructure that runs all of the services offered in the AWS Cloud](../facts/well-architected.md#well-architected-resiliency-is-shared-of-versus-in)
  say: AWS makes the infrastructure resilient; you make your workload resilient
well-architected-resiliency-managed-services-customer-owns-backup-versioning-replication
  claim: For managed services such as S3 and DynamoDB, AWS operates the infrastructure, operating system and platform, and the customer is responsible for the resiliency of their data: backup, versioning and replication strategies.
  link: [managing resiliency of your data including backup, versioning, and replication strategies](../facts/well-architected.md#well-architected-resiliency-managed-services-customer-owns-backup-versioning-replication)
  link: [AWS operates the infrastructure layer, the operating system, and platforms](../facts/well-architected.md#well-architected-resiliency-managed-services-customer-owns-backup-versioning-replication)
  say: even on S3, backups, versioning and replication are your decisions
well-architected-responsible-ai-lens-and-updated-ml-genai-lenses
  claim: AWS released one new Responsible AI lens and two updated lenses, Machine Learning and Generative AI, for AI workloads.
  scope: Well-Architected lenses.
  link: [Responsible AI](../facts/well-architected.md#well-architected-responsible-ai-lens-and-updated-ml-genai-lenses)
well-architected-review-at-milestones-before-go-live-and-continually
  claim: Reviews should happen at key milestones, early in design to avoid one-way doors and before go-live, and AWS recommends that the team that builds the architecture reviews it continually rather than holding a formal review meeting.
  link: [early on in the design phase to avoid one-way doors that are difficult to change, and then before the go-live date](../facts/well-architected.md#well-architected-review-at-milestones-before-go-live-and-continually)
  link: [continually review their architecture, rather than holding a formal review meeting](../facts/well-architected.md#well-architected-review-at-milestones-before-go-live-and-continually)
well-architected-review-audit-reports-to-determine-inherited-controls
  claim: AWS tells customers to review its third-party audit attestation documents to determine which controls they inherit and which controls remain for them to implement.
  link: [Review third-party audit attestation documents to determine inherited controls](../facts/well-architected.md#well-architected-review-audit-reports-to-determine-inherited-controls)
  link: [what required controls may be remaining for you to implement](../facts/well-architected.md#well-architected-review-audit-reports-to-determine-inherited-controls)
well-architected-review-is-conversation-not-audit
  claim: A Well-Architected review is a constructive, blame-free conversation about architectural decisions, lightweight (hours, not days), and not an audit mechanism.
  link: [a constructive conversation about architectural decisions, and is not an audit mechanism](../facts/well-architected.md#well-architected-review-is-conversation-not-audit)
  link: [a lightweight process (hours not days)](../facts/well-architected.md#well-architected-review-is-conversation-not-audit)
  say: a review is a conversation, not an audit
well-architected-review-outcome-prioritized-issues
  claim: The purpose of a review is to identify critical issues or areas to improve; the outcome is a list of issues that you prioritize by business context and a set of actions that improve the customer's experience of the workload.
  link: [identify any critical issues that might need addressing or areas that could be improved](../facts/well-architected.md#well-architected-review-outcome-prioritized-issues)
  link: [a list of issues that you can prioritize based on your business context](../facts/well-architected.md#well-architected-review-outcome-prioritized-issues)
well-architected-review-risks-hri-and-mri-definitions
  claim: A Well-Architected review sorts its findings into two categories: a high risk issue (HRI) is an architectural or operational choice that may cause significant negative impact to a business, and a medium risk issue (MRI) is a choice that may also impact the business negatively, but to a lesser extent than an HRI.
  scope: Well-Architected Framework Review (WAFR) findings.
  link: [Architectural and operational choices that may cause significant negative impact to a business](../facts/well-architected.md#well-architected-review-risks-hri-and-mri-definitions)
  link: [to a lesser extent than HRIs](../facts/well-architected.md#well-architected-review-risks-hri-and-mri-definitions)
  say: an HRI is a choice that may cause significant negative impact to the business | an MRI may also hurt the business, but to a lesser extent
well-architected-rpo-definition
  claim: RPO (Recovery Point Objective) is the maximum acceptable amount of time since the last data recovery point; the organization defines it, and it sets the acceptable data loss between the last recovery point and the interruption.
  scope: disaster recovery objectives.
  link: [maximum acceptable amount of time since the last data recovery point](../facts/well-architected.md#well-architected-rpo-definition)
  link: [RPO](../facts/well-architected.md#well-architected-rpo-definition)
well-architected-rto-definition
  claim: RTO (Recovery Time Objective) is the maximum acceptable delay between the interruption of service and the restoration of service; the organization defines it, and it sets the acceptable window of unavailability.
  scope: disaster recovery objectives.
  link: [maximum acceptable delay between the interruption of service and restoration of service](../facts/well-architected.md#well-architected-rto-definition)
  link: [RTO](../facts/well-architected.md#well-architected-rto-definition)
well-architected-rto-is-target-for-single-event-mttr-is-mean
  claim: RTO is a target, or maximum value allowed, for a single availability-impacting event, while MTTR is a mean taken over several events in a period of time.
  scope: disaster recovery objectives.
  link: [RTO is a target, or maximum value allowed](../facts/well-architected.md#well-architected-rto-is-target-for-single-event-mttr-is-mean)
  link: [MTTR is a mean value](../facts/well-architected.md#well-architected-rto-is-target-for-single-event-mttr-is-mean)
well-architected-secure-root-deactivate-programmatic-access
  claim: The Security pillar says that deactivating programmatic access to the root user, setting controls for it and avoiding its routine use reduce the risk that root credentials are exposed and the environment compromised.
  link: [Deactivating programmatic access to the root user](../facts/well-architected.md#well-architected-secure-root-deactivate-programmatic-access)
well-architected-security-and-operational-excellence-not-traded-off
  claim: You make trade-offs between pillars based on business context, but security and operational excellence are generally not traded off against the other pillars.
  link: [Security and operational excellence are generally not traded-off against the other pillars](../facts/well-architected.md#well-architected-security-and-operational-excellence-not-traded-off)
  link: [you make trade-offs between pillars based on your business context](../facts/well-architected.md#well-architected-security-and-operational-excellence-not-traded-off)
  say: you can trade cost against reliability, but not security or operations
well-architected-security-at-all-layers-defense-in-depth
  claim: Apply security at all layers means a defense in depth approach with multiple security controls, applied to all layers, for example the edge of the network, VPC, load balancing, every instance and compute service, operating system, application and code.
  link: [a defense in depth approach with multiple security controls](../facts/well-architected.md#well-architected-security-at-all-layers-defense-in-depth)
  link: [edge of network, VPC, load balancing, every instance and compute service, operating system, application, and code](../facts/well-architected.md#well-architected-security-at-all-layers-defense-in-depth)
well-architected-security-design-principles
  claim: The Well-Architected Framework lists these security design principles: implement a strong identity foundation; maintain traceability; apply security at all layers; automate security best practices; protect data in transit and at rest; keep people away from data; prepare for security events.
  link: [Implement a strong identity foundation](../facts/well-architected.md#well-architected-security-design-principles)
  link: [Maintain traceability](../facts/well-architected.md#well-architected-security-design-principles)
  link: [Apply security at all layers](../facts/well-architected.md#well-architected-security-design-principles)
  link: [Automate security best practices](../facts/well-architected.md#well-architected-security-design-principles)
  link: [Protect data in transit and at rest](../facts/well-architected.md#well-architected-security-design-principles)
  link: [Keep people away from data](../facts/well-architected.md#well-architected-security-design-principles)
  link: [Prepare for security events](../facts/well-architected.md#well-architected-security-design-principles)
well-architected-security-in-the-cloud-you-retain-control
  claim: While AWS manages security of the cloud, you are responsible for security in the cloud and retain control of the security you choose to implement for your content, platform, applications, systems and networks, as you would in your own data center.
  link: [While AWS manages security of the cloud, you are responsible for security in the cloud](../facts/well-architected.md#well-architected-security-in-the-cloud-you-retain-control)
  link: [you retain control of the security you choose to implement](../facts/well-architected.md#well-architected-security-in-the-cloud-you-retain-control)
well-architected-shared-controls-definition
  claim: Shared controls apply to both the infrastructure layer and the customer layers in separate contexts: AWS provides the requirements for the infrastructure and the customer must provide their own control implementation within their use of AWS services.
  link: [AWS provides the requirements for the infrastructure and the customer must provide their own control implementation](../facts/well-architected.md#well-architected-shared-controls-definition)
  link: [apply to both the infrastructure layer and customer layers](../facts/well-architected.md#well-architected-shared-controls-definition)
well-architected-shared-responsibility-of-versus-in-the-cloud
  claim: Security and compliance are shared between AWS and the customer; the split is commonly called security 'of' the cloud (AWS) versus security 'in' the cloud (customer).
  link: [Security “of” the Cloud versus Security “in” the Cloud](../facts/well-architected.md#well-architected-shared-responsibility-of-versus-in-the-cloud)
  link: [Security and Compliance is a shared responsibility between AWS and the customer](../facts/well-architected.md#well-architected-shared-responsibility-of-versus-in-the-cloud)
  say: AWS secures the cloud itself; you secure what you put in it
well-architected-single-tenant-managed-services-patching-split
  claim: For managed services on single-tenant architectures such as ElastiCache, RDS and OpenSearch Service, AWS identifies vulnerabilities, develops and releases patches and notifies customers, and the customer selects maintenance windows, applies service updates or schedules restarts within the communicated timeframes.
  link: [Identify vulnerabilities, develop and validate patches, release patches within the service's patching SLA](../facts/well-architected.md#well-architected-single-tenant-managed-services-patching-split)
  link: [selecting maintenance windows, applying service updates, or scheduling required restarts](../facts/well-architected.md#well-architected-single-tenant-managed-services-patching-split)
  say: for RDS, AWS builds the patch; you choose the maintenance window
well-architected-six-pillars
  claim: The AWS Well-Architected Framework is based on six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.
  scope: AWS Well-Architected Framework.
  link: [six pillars](../facts/well-architected.md#well-architected-six-pillars)
  link: [operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability](../facts/well-architected.md#well-architected-six-pillars)
well-architected-sustainability-design-principles
  claim: The six sustainability design principles are: understand your impact; establish sustainability goals; maximize utilization; anticipate and adopt new, more efficient hardware and software offerings; use managed services; reduce the downstream impact of your cloud workloads.
  link: [Understand your impact](../facts/well-architected.md#well-architected-sustainability-design-principles)
  link: [Establish sustainability goals](../facts/well-architected.md#well-architected-sustainability-design-principles)
  link: [Maximize utilization](../facts/well-architected.md#well-architected-sustainability-design-principles)
  link: [Anticipate and adopt new, more efficient hardware and software offerings](../facts/well-architected.md#well-architected-sustainability-design-principles)
  link: [Use managed services](../facts/well-architected.md#well-architected-sustainability-design-principles)
  link: [Reduce the downstream impact of your cloud workloads](../facts/well-architected.md#well-architected-sustainability-design-principles)
well-architected-sustainability-pillar-added-2021-11
  claim: The Sustainability pillar was added to the Well-Architected Framework on November 20, 2021; material written before that date describes fewer pillars.
  scope: AWS Well-Architected Framework.
  link: [November 20, 2021](../facts/well-architected.md#well-architected-sustainability-pillar-added-2021-11)
well-architected-sustainability-pillar-focus-energy
  claim: The sustainability pillar focuses on environmental impacts, especially energy consumption and efficiency.
  link: [focuses on environmental impacts, especially energy consumption and efficiency](../facts/well-architected.md#well-architected-sustainability-pillar-focus-energy)
well-architected-terms-component-workload-architecture
  claim: In the framework a component is the code, configuration and AWS resources that together deliver against a requirement; a workload is a set of components that together deliver business value; architecture is how components work together in a workload.
  link: [the code, configuration, and AWS Resources that together deliver against a requirement](../facts/well-architected.md#well-architected-terms-component-workload-architecture)
  link: [a set of components that together deliver business value](../facts/well-architected.md#well-architected-terms-component-workload-architecture)
  link: [how components work together in a workload](../facts/well-architected.md#well-architected-terms-component-workload-architecture)
well-architected-terms-milestones-portfolio-level-of-effort
  claim: Milestones mark key changes in an architecture through the product lifecycle; the technology portfolio is the collection of workloads a business needs to operate; level of effort categorizes the time, effort and complexity of a task as high (weeks to months), medium (days to weeks) or low (hours to days).
  link: [key changes in your architecture as it evolves throughout the product lifecycle](../facts/well-architected.md#well-architected-terms-milestones-portfolio-level-of-effort)
  link: [the collection of workloads that are required for the business to operate](../facts/well-architected.md#well-architected-terms-milestones-portfolio-level-of-effort)
  link: [the amount of time, effort, and complexity a task requires for implementation](../facts/well-architected.md#well-architected-terms-milestones-portfolio-level-of-effort)
well-architected-tradeoff-examples-dev-versus-mission-critical
  claim: AWS gives examples of trade-offs: in development environments you might reduce cost and sustainability impact at the expense of reliability; for mission-critical solutions you might optimize reliability at increased cost and sustainability impact.
  link: [reduce cost at the expense of reliability in development environments](../facts/well-architected.md#well-architected-tradeoff-examples-dev-versus-mission-critical)
  link: [optimize reliability with increased costs and sustainability impact](../facts/well-architected.md#well-architected-tradeoff-examples-dev-versus-mission-critical)
well-architected-wa-tool-reviews-workloads-at-no-charge
  claim: The AWS Well-Architected Tool is a cloud service that reviews and measures your architecture against the framework at no charge and gives recommendations for making workloads more reliable, secure, efficient and cost-effective.
  scope: AWS Well-Architected Tool.
  link: [a service for reviewing your workloads at no charge](../facts/well-architected.md#well-architected-wa-tool-reviews-workloads-at-no-charge)
  link: [provides recommendations for making your workloads more reliable, secure, efficient, and cost-effective](../facts/well-architected.md#well-architected-wa-tool-reviews-workloads-at-no-charge)
  say: the Well-Architected Tool is free and lives in the console
well-architected-workforce-federation-two-levels-per-account-or-organization
  claim: The Security pillar names two levels at which a centralized identity provider can federate workforce users into AWS: direct federation to each AWS account, or federation to multiple accounts in the AWS organization, where IAM Identity Center can centrally manage workforce access to AWS accounts and applications.
  link: [direct federation to each AWS account or federating to multiple accounts in your AWS organization](../facts/well-architected.md#well-architected-workforce-federation-two-levels-per-account-or-organization)
  link: [use AWS IAM Identity Center to centrally manage access for your workforce users to AWS accounts and applications](../facts/well-architected.md#well-architected-workforce-federation-two-levels-per-account-or-organization)
