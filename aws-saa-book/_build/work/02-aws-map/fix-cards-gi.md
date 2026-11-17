facts card: 21 facts
global-infrastructure-route53-failover-use-health-checks-not-record-changes
  claim: A statically stable Route 53 design fails over between Regions using health check status; changing record values with ChangeResourceRecordSets, changing weights or creating new records at failover time depends on the Route 53 control plane.
  link: [use the status of health checks to perform failovers between Regions](../facts/global-infrastructure.md#global-infrastructure-route53-failover-use-health-checks-not-record-changes)
  link: [These approaches depend on the Route 53 control plane](../facts/global-infrastructure.md#global-infrastructure-route53-failover-use-health-checks-not-record-changes)
global-infrastructure-three-service-types-zonal-regional-global
  claim: AWS groups its services into three categories by fault isolation boundary: zonal, Regional and global.
  link: [zonal, Regional, and global](../facts/global-infrastructure.md#global-infrastructure-three-service-types-zonal-regional-global)
  link: [three different categories of services](../facts/global-infrastructure.md#global-infrastructure-three-service-types-zonal-regional-global)
  say: zonal, Regional and global
global-infrastructure-us-west-1-newer-accounts-two-azs
  claim: Newer accounts can access two Availability Zones in US West (N. California), although the Regions table lists the Region with 3 AZs.
  scope: US West (N. California), newer accounts; newer accounts.
  link: [two Availability Zones](../facts/global-infrastructure.md#global-infrastructure-us-west-1-newer-accounts-two-azs)
global-infrastructure-az-no-shared-fate
  claim: Availability Zones are designed not to be hit at the same time by one shared-fate event such as utility power loss, water disruption, fiber isolation, earthquakes, fires, tornadoes or floods, and their generators and cooling are not shared.
  scope: Availability Zones within one Region.
  link: [designed not to be simultaneously impacted by a shared fate scenario](../facts/global-infrastructure.md#global-infrastructure-az-no-shared-fate)
  link: [utility power, water disruption, fiber isolation, earthquakes, fires, tornadoes, or floods](../facts/global-infrastructure.md#global-infrastructure-az-no-shared-fate)
  say: zones are designed not to fail together from one shared event
global-infrastructure-az-name-mapping-independent-per-account
  claim: For accounts created before November 2025, in the oldest Regions, AWS maps Availability Zone names to physical zones independently per account, so us-east-1a in your account might not be the same physical location as us-east-1a in another account; accounts created from November 2025 get the same mapping.
  scope: Availability Zone names in the oldest Regions; accounts created before November 2025.
  link: [we independently map Availability Zones to codes for each AWS account](../facts/global-infrastructure.md#global-infrastructure-az-name-mapping-independent-per-account)
  link: [might not be the same physical location as it is in another account](../facts/global-infrastructure.md#global-infrastructure-az-name-mapping-independent-per-account)
  link: [Accounts created starting November 2025, get the same Availability Zones mapped to codes](../facts/global-infrastructure.md#global-infrastructure-az-name-mapping-independent-per-account)
  say: zone names are mapped to physical zones separately per account
  changed: 2025-11: was we independently map Availability Zones to codes for each AWS account
global-infrastructure-customer-content-stays-in-chosen-region
  claim: AWS services process and store customer content in the Region or Regions where the customer uses the services; the named global services (IAM, Organizations, CloudFront, Route53, Global Accelerator, Direct Connect, Firewall Manager, WAF, Shield) may store and process data globally.
  scope: customer content; except the listed global services.
  link: [process and store customer content in the AWS region(s) where the services are used by the customer](../facts/global-infrastructure.md#global-infrastructure-customer-content-stays-in-chosen-region)
  link: [may store and process data globally](../facts/global-infrastructure.md#global-infrastructure-customer-content-stays-in-chosen-region)
  link: [store customer content in the AWS region(s)](../facts/global-infrastructure.md#global-infrastructure-customer-content-stays-in-chosen-region)
  say: customer content stays in the Region where you use the service | customer content stays in the Region you use
global-infrastructure-three-cost-drivers
  claim: AWS names three fundamental cost drivers: compute, storage, and outbound data transfer.
  scope: AWS pricing in general.
  link: [compute, storage, and outbound data transfer](../facts/global-infrastructure.md#global-infrastructure-three-cost-drivers)
  link: [three fundamental drivers of cost](../facts/global-infrastructure.md#global-infrastructure-three-cost-drivers)
global-infrastructure-faq-wavelength-ultralow-latency-for-5g-devices
  claim: AWS Wavelength is designed to deliver ultralow-latency applications to 5G devices by extending AWS infrastructure, services, APIs and tools into telecommunications providers' 5G networks.
  link: [ultralow-latency applications to 5G devices](../facts/global-infrastructure.md#global-infrastructure-faq-wavelength-ultralow-latency-for-5g-devices)
  say: Wavelength is for ultra low latency applications on five G devices
global-infrastructure-faq-outposts-for-workloads-that-must-stay-on-premises
  claim: AWS Outposts is designed for workloads that need to remain on premises because of latency requirements, where the customer wants that workload to run seamlessly with the rest of their workloads on AWS; it is fully managed and uses AWS-designed compute and storage racks on premises.
  link: [workloads that need to remain on premises due to latency requirements](../facts/global-infrastructure.md#global-infrastructure-faq-outposts-for-workloads-that-must-stay-on-premises)
  link: [Outposts is fully managed](../facts/global-infrastructure.md#global-infrastructure-faq-outposts-for-workloads-that-must-stay-on-premises)
  say: Outposts is for workloads that must stay on premises
global-infrastructure-edge-locations-connected-to-regions-by-backbone
  claim: Edge locations connect to the Regions through the AWS network backbone, a fully redundant, multiple 100GbE parallel fiber that circles the globe.
  link: [connected to the AWS Regions through the AWS network backbone](../facts/global-infrastructure.md#global-infrastructure-edge-locations-connected-to-regions-by-backbone)
  link: [multiple 100GbE parallel fiber](../facts/global-infrastructure.md#global-infrastructure-edge-locations-connected-to-regions-by-backbone)
global-infrastructure-pop-hosts-cloudfront-route53-global-accelerator
  claim: AWS points of presence host Amazon CloudFront (a CDN), Amazon Route 53 (public DNS) and AWS Global Accelerator (edge networking optimization), in addition to the Regions and Availability Zones.
  scope: AWS edge network.
  link: [Amazon CloudFront](../facts/global-infrastructure.md#global-infrastructure-pop-hosts-cloudfront-route53-global-accelerator)
  link: [Amazon Route 53](../facts/global-infrastructure.md#global-infrastructure-pop-hosts-cloudfront-route53-global-accelerator)
  link: [AWS Global Accelerator](../facts/global-infrastructure.md#global-infrastructure-pop-hosts-cloudfront-route53-global-accelerator)
global-infrastructure-faq-local-zones-vs-availability-zones-core-vs-full-services
  claim: Local Zones are designed to bring the core services needed for the latency-sensitive part of a workload closer to end users, while Availability Zones provide access to the full array of AWS services.
  link: [the core services needed for the latency-sensitive portions of your workload](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-vs-availability-zones-core-vs-full-services)
  link: [Availability Zones provide access to the full array of AWS services](../facts/global-infrastructure.md#global-infrastructure-faq-local-zones-vs-availability-zones-core-vs-full-services)
  say: a Local Zone is designed to bring the core services for the latency-sensitive part of a workload closer to users
global-infrastructure-pre-provision-capacity-instead-of-control-plane-recovery
  claim: Pre-provisioning extra capacity, rather than relying on the EC2 control plane to launch new instances after an Availability Zone fails, is how you achieve static stability; removing control plane dependencies from the recovery path gives more resilient workloads.
  link: [having that extra capacity pre-provisioned helps achieve static stability](../facts/global-infrastructure.md#global-infrastructure-pre-provision-capacity-instead-of-control-plane-recovery)
  link: [eliminating dependencies on control planes](../facts/global-infrastructure.md#global-infrastructure-pre-provision-capacity-instead-of-control-plane-recovery)
  say: pre-provision capacity in the other zones instead of launching during the failure
global-infrastructure-static-stability-example-three-per-az-fifty-percent
  claim: In the whitepaper example, to stay statically stable against a single Availability Zone failure you deploy three instances in each Availability Zone, nine in total, which means running 50% additional instances.
  link: [three instances in each Availability Zone, for a total of nine](../facts/global-infrastructure.md#global-infrastructure-static-stability-example-three-per-az-fifty-percent)
  link: [50% additional instances](../facts/global-infrastructure.md#global-infrastructure-static-stability-example-three-per-az-fifty-percent)
global-infrastructure-cloudfront-content-served-during-control-plane-impairment
  claim: During a CloudFront control plane impairment the CRUDL operations, including invalidations, may not work, but content continues to be cached and served and origin failovers continue to work.
  link: [your content will continue to be cached and served](../facts/global-infrastructure.md#global-infrastructure-cloudfront-content-served-during-control-plane-impairment)
  link: [origin failovers will continue to work](../facts/global-infrastructure.md#global-infrastructure-cloudfront-content-served-during-control-plane-impairment)
global-infrastructure-az-latency-single-digit-ms
  claim: Availability Zones in the same Region are close enough for high-throughput, low-latency networking with single-digit millisecond latency, so data can be replicated synchronously between them.
  scope: Availability Zones of one Region.
  link: [single-digit millisecond](../facts/global-infrastructure.md#global-infrastructure-az-latency-single-digit-ms)
  link: [replicate data synchronously between Availability Zones](../facts/global-infrastructure.md#global-infrastructure-az-latency-single-digit-ms)
  say: single-digit millisecond latency between Availability Zones
global-infrastructure-az-id-same-physical-location-every-account
  claim: An AZ ID (for example use1-az2) names the same physical location in every AWS account, so a subnet shared with another account appears there in the zone with the same AZ ID.
  scope: AZ IDs.
  link: [the same physical location in every AWS account](../facts/global-infrastructure.md#global-infrastructure-az-id-same-physical-location-every-account)
  link: [a Region-specific prefix, followed by -az, followed by a number](../facts/global-infrastructure.md#global-infrastructure-az-id-same-physical-location-every-account)
  link: [this subnet is available to that account in the Availability Zone whose AZ ID is also `use1-az2`](../facts/global-infrastructure.md#global-infrastructure-az-id-same-physical-location-every-account)
  say: an AZ ID is the same physical zone in every account
global-infrastructure-zonal-resource-deploy-in-multiple-azs
  claim: A zonal resource is specific to the Availability Zone in which you create it, and the best practice is to deploy your application in multiple Availability Zones so that it remains available even if one Availability Zone fails.
  scope: zonal resources.
  link: [specific to the Availability Zone in which you create it](../facts/global-infrastructure.md#global-infrastructure-zonal-resource-deploy-in-multiple-azs)
  link: [deploy your application in multiple Availability Zones, so that your application remains available even if one Availability Zone fails](../facts/global-infrastructure.md#global-infrastructure-zonal-resource-deploy-in-multiple-azs)
  say: a zonal resource lives in one Availability Zone | deploy in multiple Availability Zones so the application stays available if one zone fails
global-infrastructure-regional-service-definition
  claim: A Regional service is one that AWS has built on top of multiple Availability Zones and presents to you as a single Regional endpoint, so you do not have to work out how to use zonal services well.
  link: [built on top of multiple Availability Zones](../facts/global-infrastructure.md#global-infrastructure-regional-service-definition)
  link: [a single Regional endpoint](../facts/global-infrastructure.md#global-infrastructure-regional-service-definition)
  say: a Regional service is spread over several Availability Zones behind one Regional endpoint
global-infrastructure-static-stability-definition
  claim: Static stability means that a system keeps operating in its current state, as normal, without needing to make changes while a dependency fails or is unavailable.
  link: [continue to operate as normal without the need to make changes during the failure or unavailability of dependencies](../facts/global-infrastructure.md#global-infrastructure-static-stability-definition)
  link: [static stability](../facts/global-infrastructure.md#global-infrastructure-static-stability-definition)
  say: static stability: keep working without changes when a dependency fails
global-infrastructure-auto-scaling-relies-on-ec2-control-plane
  claim: Launching new EC2 instances through Auto Scaling takes time and relies on the EC2 control plane, so the remaining capacity could be overwhelmed while replacements start.
  link: [deploying new instances through auto scaling relies on the EC2 control plane](../facts/global-infrastructure.md#global-infrastructure-auto-scaling-relies-on-ec2-control-plane)
  link: [launching new EC2 instances takes time](../facts/global-infrastructure.md#global-infrastructure-auto-scaling-relies-on-ec2-control-plane)
