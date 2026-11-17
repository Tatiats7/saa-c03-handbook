facts card: 2 facts
global-infrastructure-single-az-failure-takes-all-instances
  claim: If all of your EC2 instances are in a single Availability Zone and that Availability Zone is affected by a failure, none of your EC2 instances are available.
  scope: EC2 instances hosted in one Availability Zone; the Availability Zone is affected by a failure.
  link: [none of your EC2 instances would be available](../facts/global-infrastructure.md#global-infrastructure-single-az-failure-takes-all-instances)
  say: none of your instances would be available
global-infrastructure-production-at-least-two-azs
  claim: The reliability pillar says to deploy and operate all production workloads in at least two Availability Zones in a Region; a production workload that exists only in a single Availability Zone is a named anti-pattern.
  scope: production workloads; minimum.
  link: [at least two Availability Zones (AZs) in a Region](../facts/global-infrastructure.md#global-infrastructure-production-at-least-two-azs)
  link: [Your production workload exists only in a single Availability Zone](../facts/global-infrastructure.md#global-infrastructure-production-at-least-two-azs)
  say: at least two Availability Zones for every production workload
