facts card: 19 facts
well-architected-single-tenant-managed-services-patching-split
  claim: For managed services on single-tenant architectures such as ElastiCache, RDS and OpenSearch Service, AWS identifies vulnerabilities, develops and releases patches and notifies customers, and the customer selects maintenance windows, applies service updates or schedules restarts within the communicated timeframes.
  link: [Identify vulnerabilities, develop and validate patches, release patches within the service's patching SLA](../facts/well-architected.md#well-architected-single-tenant-managed-services-patching-split)
  link: [selecting maintenance windows, applying service updates, or scheduling required restarts](../facts/well-architected.md#well-architected-single-tenant-managed-services-patching-split)
  say: for RDS, AWS builds the patch; you choose the maintenance window
well-architected-customer-responsible-for-guest-os-apps-security-groups
  claim: The customer is responsible for the guest operating system (including updates and security patches), the application software, and the configuration of the AWS-provided security group firewall.
  link: [guest operating system (including updates and security patches)](../facts/well-architected.md#well-architected-customer-responsible-for-guest-os-apps-security-groups)
  link: [configuration of the AWS provided security group firewall](../facts/well-architected.md#well-architected-customer-responsible-for-guest-os-apps-security-groups)
  say: you patch the guest OS, your apps, and you configure the security groups
well-architected-abstracted-services-aws-runs-os-customer-manages-data
  claim: For abstracted services such as Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system and the platforms; the customer manages the data (including encryption options), classifies assets and uses IAM to set permissions.
  link: [AWS operates the infrastructure layer, the operating system, and platforms](../facts/well-architected.md#well-architected-abstracted-services-aws-runs-os-customer-manages-data)
  link: [managing their data (including encryption options), classifying their assets, and using IAM tools to apply the appropriate permissions](../facts/well-architected.md#well-architected-abstracted-services-aws-runs-os-customer-manages-data)
  say: for S3 and DynamoDB, AWS runs the platform; you own your data, its encryption and its permissions
well-architected-pillar-cost-optimization-definition
  claim: Cost optimization is the ability to run systems to deliver business value at the lowest price point.
  scope: AWS Well-Architected Framework pillars.
  link: [lowest price point](../facts/well-architected.md#well-architected-pillar-cost-optimization-definition)
well-architected-pillar-sustainability-definition
  claim: Sustainability is the ability to continually improve sustainability impacts by reducing energy consumption and increasing efficiency across all components of a workload, maximizing the benefits of provisioned resources and minimizing the total resources required.
  scope: AWS Well-Architected Framework pillars.
  link: [reducing energy consumption and increasing efficiency](../facts/well-architected.md#well-architected-pillar-sustainability-definition)
well-architected-security-and-operational-excellence-not-traded-off
  claim: You make trade-offs between pillars based on business context, but security and operational excellence are generally not traded off against the other pillars.
  link: [Security and operational excellence are generally not traded-off against the other pillars](../facts/well-architected.md#well-architected-security-and-operational-excellence-not-traded-off)
  link: [you make trade-offs between pillars based on your business context](../facts/well-architected.md#well-architected-security-and-operational-excellence-not-traded-off)
  say: you can trade cost against reliability, but not security or operations
well-architected-region-pricing-differs-choose-by-cost
  claim: Resource pricing may differ in each Region because of local land, fiber, electricity and tax costs; COST07-BP02 says to deploy in higher-cost Regions only to meet latency, data residency and data sovereignty requirements.
  link: [Resource pricing may be different in each Region](../facts/well-architected.md#well-architected-region-pricing-differs-choose-by-cost)
  link: [only deploy in Regions with higher costs to meet latency, data residency and data sovereignty requirements](../facts/well-architected.md#well-architected-region-pricing-differs-choose-by-cost)
  say: prices differ by Region; pay more only when latency or residency demands it
well-architected-sustainability-pillar-focus-energy
  claim: The sustainability pillar focuses on environmental impacts, especially energy consumption and efficiency.
  link: [focuses on environmental impacts, especially energy consumption and efficiency](../facts/well-architected.md#well-architected-sustainability-pillar-focus-energy)
management-console-private-access-limits-console-to-known-accounts-from-vpc
  claim: AWS Management Console Private Access limits console use to a specified set of known AWS accounts when the traffic originates from within your VPC, and routes console traffic through AWS PrivateLink VPC endpoints instead of the public internet.
  scope: AWS Management Console Private Access.
  link: [specified set of known AWS accounts](../facts/management-console.md#management-console-private-access-limits-console-to-known-accounts-from-vpc)
  link: [VPC endpoints](../facts/management-console.md#management-console-private-access-limits-console-to-known-accounts-from-vpc)
management-console-cloudshell-faq-home-directory-kept-120-days
  claim: CloudShell keeps the files in your home directory for up to 120 days after your last CloudShell session, counted separately per Region; opening CloudShell in that Region with the same IAM principal resets the timer, and you are notified in the health dashboard before deletion.
  scope: CloudShell home directory files, per Region; maximum; not adjustable; counted from the last CloudShell session in that Region.
  link: [120 days](../facts/management-console.md#management-console-cloudshell-faq-home-directory-kept-120-days)
  link: [Accessing CloudShell in the expiring Region through the same IAM principal will reset the timer](../facts/management-console.md#management-console-cloudshell-faq-home-directory-kept-120-days)
  say: one hundred twenty days per Region
management-console-cloudshell-vpc-environments-no-persistent-storage
  claim: CloudShell VPC environments have no persistent storage: the home directory is deleted when the VPC environment times out or is deleted or restarted.
  scope: CloudShell VPC environments.
  link: [CloudShell VPC environments do not have persistent storage](../facts/management-console.md#management-console-cloudshell-vpc-environments-no-persistent-storage)
  link: [The $HOME directory is deleted when your VPC environment times out](../facts/management-console.md#management-console-cloudshell-vpc-environments-no-persistent-storage)
management-console-cloudshell-storage-deleted-after-120-days-unused
  claim: If you stop using CloudShell in a Region, its persistent storage is deleted automatically after 120 days unless you launch CloudShell in that Region again.
  scope: per Region, per user home directory; fixed; not adjustable; no CloudShell session in that Region.
  link: [120 days](../facts/management-console.md#management-console-cloudshell-storage-deleted-after-120-days-unused)
aws-cli-long-term-iam-user-credentials-not-recommended
  claim: IAM user long-term credentials, which have no expiration, are not recommended for the CLI; storing credentials outside the CLI is also not recommended because it is only as secure as that location.
  link: [(Not recommended) Use long-term credentials, which have no expiration](../facts/aws-cli.md#aws-cli-long-term-iam-user-credentials-not-recommended)
  link: [This method is only as secure as the external location the credentials are stored](../facts/aws-cli.md#aws-cli-long-term-iam-user-credentials-not-recommended)
  say: long-term access keys never expire, so AWS does not recommend them
iam-shared-responsibility-customer-applies-permissions-with-iam
  claim: Under the shared responsibility model, for abstracted services such as S3 and DynamoDB AWS runs the infrastructure, operating system and platform, while the customer is responsible for managing and classifying their data, choosing encryption options and using IAM tools to apply the right permissions.
  scope: abstracted services such as Amazon S3 and Amazon DynamoDB.
  link: [using IAM tools to apply the appropriate permissions](../facts/iam.md#iam-shared-responsibility-customer-applies-permissions-with-iam)
  link: [managing their data (including encryption options), classifying their assets](../facts/iam.md#iam-shared-responsibility-customer-applies-permissions-with-iam)
  link: [AWS operates the infrastructure layer, the operating system, and platforms](../facts/iam.md#iam-shared-responsibility-customer-applies-permissions-with-iam)
iam-resources-global-same-role-any-region
  claim: IAM resources are global, so the same IAM role can be used in any Region.
  scope: IAM resources.
  link: [IAM resources are global](../facts/iam.md#iam-resources-global-same-role-any-region)
  link: [the same role can be used in any Region](../facts/iam.md#iam-resources-global-same-role-any-region)
  say: IAM resources are global | one role works in every Region
global-infrastructure-local-zone-extension-of-region-own-internet
  claim: A Local Zone is an extension of an AWS Region close to your users; it has its own connections to the internet and supports Direct Connect, so resources there can serve low-latency applications.
  link: [an extension of an AWS Region in geographic proximity to your users](../facts/global-infrastructure.md#global-infrastructure-local-zone-extension-of-region-own-internet)
  link: [their own connections to the internet and support Direct Connect](../facts/global-infrastructure.md#global-infrastructure-local-zone-extension-of-region-own-internet)
global-infrastructure-edge-location-services
  claim: Amazon CloudFront, Amazon Route 53, AWS Firewall Manager, AWS Shield and AWS WAF are provided through AWS edge locations.
  scope: AWS edge locations.
  link: [Amazon CloudFront, Amazon Route 53, AWS Firewall Manager, AWS Shield, and AWS WAF services are provided through AWS Edge Locations](../facts/global-infrastructure.md#global-infrastructure-edge-location-services)
  say: CloudFront, Route 53, Firewall Manager, Shield and WAF are provided through the edge locations
management-console-global-view-map-view-since-2026-08
  claim: AWS Global View in the AWS Management Console now offers an interactive map view that plots all AWS Regions and AWS Local Zones, and customers can toggle between it and the existing list view; previously, customers had to scan through a list of AWS locations in Global View.
  scope: AWS Global View in the AWS Management Console.
  link: [interactive map view](../facts/management-console.md#management-console-global-view-map-view-since-2026-08)
  link: [a list of AWS locations](../facts/management-console.md#management-console-global-view-map-view-since-2026-08)
  changed: 2026-08-12: was a list of AWS locations
well-architected-rpo-definition
  claim: RPO (Recovery Point Objective) is the maximum acceptable amount of time since the last data recovery point; the organization defines it, and it sets the acceptable data loss between the last recovery point and the interruption.
  scope: disaster recovery objectives.
  link: [maximum acceptable amount of time since the last data recovery point](../facts/well-architected.md#well-architected-rpo-definition)
  link: [RPO](../facts/well-architected.md#well-architected-rpo-definition)
