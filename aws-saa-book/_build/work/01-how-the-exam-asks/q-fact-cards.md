facts card: 36 facts
global-infrastructure-single-az-failure-takes-all-instances
  claim: If all of your EC2 instances are in a single Availability Zone and that Availability Zone is affected by a failure, none of your EC2 instances are available.
  scope: EC2 instances hosted in one Availability Zone; the Availability Zone is affected by a failure.
  link: [none of your EC2 instances would be available](../facts/global-infrastructure.md#global-infrastructure-single-az-failure-takes-all-instances)
  say: none of your instances would be available
vpc-prod-at-least-two-azs
  claim: For a production environment AWS recommends selecting at least two Availability Zones and deploying resources evenly in each active Availability Zone.
  link: [at least two Availability Zones](../facts/vpc.md#vpc-prod-at-least-two-azs)
  link: [deploy your AWS resources evenly in each active Availability Zone](../facts/vpc.md#vpc-prod-at-least-two-azs)
global-infrastructure-production-at-least-two-azs
  claim: The reliability pillar says to deploy and operate all production workloads in at least two Availability Zones in a Region; a production workload that exists only in a single Availability Zone is a named anti-pattern.
  scope: production workloads; minimum.
  link: [at least two Availability Zones (AZs) in a Region](../facts/global-infrastructure.md#global-infrastructure-production-at-least-two-azs)
  link: [Your production workload exists only in a single Availability Zone](../facts/global-infrastructure.md#global-infrastructure-production-at-least-two-azs)
  say: at least two Availability Zones for every production workload
vpc-natgw-shared-across-azs-loses-internet
  claim: If resources in several Availability Zones share one NAT gateway and that gateway's Availability Zone goes down, resources in the other Availability Zones lose internet access; create a NAT gateway in each Availability Zone and route each zone to its own gateway.
  scope: zonal NAT gateways used by resources in several Availability Zones; zonal NAT gateways (a regional NAT gateway expands into each Availability Zone that has resources: vpc-regional-natgw-vs-zonal).
  link: [resources in the other Availability Zones lose internet access](../facts/vpc.md#vpc-natgw-shared-across-azs-loses-internet)
  link: [create a NAT gateway in each Availability Zone, and configure your routing to ensure that resources use the NAT gateway in the same Availability Zone](../facts/vpc.md#vpc-natgw-shared-across-azs-loses-internet)
vpc-natgw-vs-instance-cost
  claim: A NAT gateway is charged by the number of gateways, the duration of use and the data sent through them; a NAT instance is charged by the number of instances, the duration of use and the instance type and size.
  scope: per NAT gateway or NAT instance.
  link: [Charged depending on the number of NAT gateways you use, duration of usage, and amount of data that you send through the NAT gateways](../facts/vpc.md#vpc-natgw-vs-instance-cost)
  link: [Charged depending on the number of NAT instances that you use, duration of usage, and instance type and size](../facts/vpc.md#vpc-natgw-vs-instance-cost)
vpc-natgw-one-az-redundant-in-zone
  claim: Each NAT gateway is created in one specific Availability Zone and is implemented with redundancy inside that zone.
  scope: per zonal NAT gateway; zonal NAT gateways (a regional NAT gateway expands across Availability Zones: vpc-regional-natgw-vs-zonal).
  link: [Each NAT gateway is created in a specific Availability Zone and implemented with redundancy in that zone](../facts/vpc.md#vpc-natgw-one-az-redundant-in-zone)
well-architected-tradeoff-examples-dev-versus-mission-critical
  claim: AWS gives examples of trade-offs: in development environments you might reduce cost and sustainability impact at the expense of reliability; for mission-critical solutions you might optimize reliability at increased cost and sustainability impact.
  link: [reduce cost at the expense of reliability in development environments](../facts/well-architected.md#well-architected-tradeoff-examples-dev-versus-mission-critical)
  link: [optimize reliability with increased costs and sustainability impact](../facts/well-architected.md#well-architected-tradeoff-examples-dev-versus-mission-critical)
vpc-natgw-route-from-private-subnet
  claim: To give instances in a private subnet internet access, you create a NAT gateway (or NAT instance) in a public subnet and add a route in the private subnet's route table that sends 0.0.0.0/0 to the NAT device.
  scope: per private subnet route table; zonal NAT gateway or NAT instance (a regional NAT gateway does not need a public subnet: vpc-regional-natgw-no-public-subnet).
  link: [create a NAT gateway or launch a NAT instance in a public subnet](../facts/vpc.md#vpc-natgw-route-from-private-subnet)
  link: [routes IPv4 internet traffic (`0.0.0.0/0`) to the NAT device](../facts/vpc.md#vpc-natgw-route-from-private-subnet)
  say: the NAT gateway sits in a public subnet | the private subnet's default route points at the NAT gateway
iam-idc-recommended-front-door-for-workforce
  claim: AWS calls IAM Identity Center its recommended front door into AWS and the primary tool to manage the AWS access of workforce users.
  link: [recommended front door into AWS](../facts/iam.md#iam-idc-recommended-front-door-for-workforce)
  link: [primary tool to manage the AWS access of your workforce users](../facts/iam.md#iam-idc-recommended-front-door-for-workforce)
iam-idc-creates-role-per-permission-set
  claim: IAM Identity Center creates and manages IAM roles in the individual AWS accounts for each permission set that you grant to users.
  scope: per AWS account assigned a permission set.
  link: [creates and manages IAM roles in individual AWS accounts for each permission set](../facts/iam.md#iam-idc-creates-role-per-permission-set)
well-architected-rely-on-centralized-identity-provider-for-workforce
  claim: Security pillar best practice SEC02-BP04: for workforce identities, rely on a centralized identity provider, so that access is created, assigned, revoked and audited from a single location.
  scope: workforce identities (employees and contractors).
  link: [rely on an identity provider that allows you to manage identities in a centralized place](../facts/well-architected.md#well-architected-rely-on-centralized-identity-provider-for-workforce)
  link: [creating, assigning, managing, revoking, and auditing access from a single location](../facts/well-architected.md#well-architected-rely-on-centralized-identity-provider-for-workforce)
iam-users-have-long-term-credentials-roles-do-not
  claim: An IAM user has long-term credentials (a password and access keys); a role has no standard long-term credentials and gives temporary security credentials for each role session. AWS recommends relying on temporary credentials instead of creating IAM users where possible.
  scope: IAM users and IAM roles.
  link: [does not have standard long-term credentials, such as a password or access keys](../facts/iam.md#iam-users-have-long-term-credentials-roles-do-not)
  link: [IAM users have long-term credentials such as passwords and access keys](../facts/iam.md#iam-users-have-long-term-credentials-roles-do-not)
  link: [identities with long-term credentials](../facts/iam.md#iam-users-have-long-term-credentials-roles-do-not)
vpc-gateway-endpoint-no-hourly-or-processing-charge
  claim: Gateway VPC endpoints have no data processing or hourly charges, so routing S3 traffic through a gateway endpoint instead of the NAT gateway avoids the NAT gateway data processing charge.
  scope: per gateway endpoint.
  link: [There are no data processing or hourly charges for using Gateway Type VPC endpoints](../facts/vpc.md#vpc-gateway-endpoint-no-hourly-or-processing-charge)
  link: [avoid the NAT Gateway Data Processing charge](../facts/vpc.md#vpc-gateway-endpoint-no-hourly-or-processing-charge)
vpc-interface-endpoint-billed-hour-per-az-and-gb
  claim: An interface VPC endpoint is billed for each hour it is provisioned in each Availability Zone and per GB of data processed.
  link: [billed for each hour that your interface VPC endpoint is provisioned in each Availability Zone](../facts/vpc.md#vpc-interface-endpoint-billed-hour-per-az-and-gb)
  link: [You are also billed per GB of data processed](../facts/vpc.md#vpc-interface-endpoint-billed-hour-per-az-and-gb)
  say: per hour per Availability Zone | and per GB processed
vpc-natgw-data-processing-any-destination
  claim: NAT gateway data processing charges apply to each gigabyte processed through the gateway regardless of the traffic's source or destination, and standard data transfer charges apply on top.
  scope: per NAT gateway.
  link: [regardless of the traffic's source or destination](../facts/vpc.md#vpc-natgw-data-processing-any-destination)
  link: [You also incur standard AWS data transfer charges for all data transferred via the NAT gateway](../facts/vpc.md#vpc-natgw-data-processing-any-destination)
vpc-gateway-endpoint-s3-dynamodb-no-privatelink
  claim: Gateway VPC endpoints give connectivity to Amazon S3 and DynamoDB without an internet gateway or NAT device, and, unlike other VPC endpoint types, they do not use AWS PrivateLink.
  link: [Gateway VPC endpoints provide reliable connectivity to Amazon S3 and DynamoDB without requiring an internet gateway or a NAT device for your VPC](../facts/vpc.md#vpc-gateway-endpoint-s3-dynamodb-no-privatelink)
  link: [Gateway endpoints do not use AWS PrivateLink, unlike other types of VPC endpoints](../facts/vpc.md#vpc-gateway-endpoint-s3-dynamodb-no-privatelink)
  say: gateway endpoints reach S3 and DynamoDB without an internet gateway or NAT
vpc-faq-s3-access-options
  claim: Instances in a VPC can reach Amazon S3 through a VPC endpoint for S3, which keeps all traffic inside Amazon's network and lets you apply extra access policies, or through an internet gateway, or over Direct Connect or VPN via the data center.
  scope: per VPC.
  link: [VPC Endpoint for S3, which makes sure all traffic remains within Amazon's network](../facts/vpc.md#vpc-faq-s3-access-options)
  link: [use an Internet gateway to enable Internet access from your VPC and instances in the VPC can communicate with Amazon S3](../facts/vpc.md#vpc-faq-s3-access-options)
  say: a VPC endpoint for S3 keeps the traffic on the AWS network
vpc-natgw-vs-instance-maintenance
  claim: A NAT gateway is managed by AWS with no maintenance on your side; a NAT instance is managed by you, including software updates and operating system patches.
  link: [Managed by AWS](../facts/vpc.md#vpc-natgw-vs-instance-maintenance)
  link: [Managed by you, for example, by installing software updates or operating system patches on the instance](../facts/vpc.md#vpc-natgw-vs-instance-maintenance)
vpc-natgw-preferred-over-nat-instance
  claim: AWS recommends a NAT gateway over a NAT instance because it provides better availability, higher bandwidth and needs less administrative effort.
  link: [NAT gateways provide better availability, higher bandwidth, and requires less administrative effort](../facts/vpc.md#vpc-natgw-preferred-over-nat-instance)
vpc-natgw-vs-instance-availability
  claim: A NAT gateway is highly available with redundancy inside its Availability Zone, and you create one per Availability Zone for a zone-independent design; a NAT instance needs a script to manage failover between instances.
  link: [Highly available](../facts/vpc.md#vpc-natgw-vs-instance-availability)
  link: [Use a script to manage failover between instances](../facts/vpc.md#vpc-natgw-vs-instance-availability)
  link: [Create a NAT gateway in each Availability Zone to ensure zone-independent architecture](../facts/vpc.md#vpc-natgw-vs-instance-availability)
vpc-natgw-each-active-az-in-production
  claim: In production AWS recommends deploying a NAT gateway in each active Availability Zone.
  scope: per active Availability Zone of a production VPC; zonal NAT gateways.
  link: [deploy a NAT gateway in each active AZ](../facts/vpc.md#vpc-natgw-each-active-az-in-production)
iam-compute-services-receive-role-credentials-no-keys-needed
  claim: On an AWS compute service such as EC2 or Lambda, AWS delivers the temporary credentials of an IAM role to the compute resource; SDK applications find and use them, so there is no need to distribute long-lived IAM user credentials to workloads on AWS.
  link: [AWS delivers the temporary credentials of an IAM role to that compute resource](../facts/iam.md#iam-compute-services-receive-role-credentials-no-keys-needed)
  link: [no need to distribute long lived credentials for an IAM user](../facts/iam.md#iam-compute-services-receive-role-credentials-no-keys-needed)
iam-ec2-role-credentials-rotate-automatically
  claim: Role credentials delivered to an EC2 instance are temporary and updated automatically, so you do not manage credentials on the instance; a change to a role shared by many instances propagates to all of them, and a role can be attached to an instance that is already running.
  scope: roles for EC2.
  link: [temporary and updated automatically](../facts/iam.md#iam-ec2-role-credentials-rotate-automatically)
  link: [propagates to all of them](../facts/iam.md#iam-ec2-role-credentials-rotate-automatically)
  link: [attached to an instance that is already running](../facts/iam.md#iam-ec2-role-credentials-rotate-automatically)
iam-best-practice-least-privilege-definition
  claim: Least-privilege permissions means granting only the permissions required to perform a task, by defining the actions allowed on specific resources under specific conditions.
  scope: IAM policies.
  link: [defining the actions that can be taken on specific resources under specific conditions](../facts/iam.md#iam-best-practice-least-privilege-definition)
iam-long-term-keys-valid-until-revoked-temporary-expire
  claim: Long-term access keys of IAM users and the root user stay valid until you revoke them by hand; temporary credentials from roles and STS expire after a short period, which limits the damage of an accidental exposure.
  scope: access keys and temporary security credentials.
  link: [remain valid until you manually revoke them](../facts/iam.md#iam-long-term-keys-valid-until-revoked-temporary-expire)
  link: [expire after a short period of time](../facts/iam.md#iam-long-term-keys-valid-until-revoked-temporary-expire)
  link: [reduce your risk in case credentials are accidentally exposed](../facts/iam.md#iam-long-term-keys-valid-until-revoked-temporary-expire)
vpc-gateway-endpoint-no-onprem-cross-region-tgw
  claim: An S3 gateway endpoint does not allow access from on-premises networks, from peered VPCs in other AWS Regions, or through a transit gateway; for those cases you use an interface endpoint, at additional cost.
  link: [gateway endpoints do not allow access from on-premises networks, from peered VPCs in other AWS Regions, or through a transit gateway](../facts/vpc.md#vpc-gateway-endpoint-no-onprem-cross-region-tgw)
  link: [you must use an interface endpoint, which is available for an additional cost](../facts/vpc.md#vpc-gateway-endpoint-no-onprem-cross-region-tgw)
  say: not from on premises, other Regions or a transit gateway | use an interface endpoint instead
vpc-faq-interface-endpoints-privatelink
  claim: Interface endpoints give private connectivity to services powered by PrivateLink, whether AWS services, your own services or SaaS solutions, and support connectivity over Direct Connect.
  scope: per interface endpoint.
  link: [services powered by PrivateLink, being AWS services, your own services or SaaS solutions](../facts/vpc.md#vpc-faq-interface-endpoints-privatelink)
  link: [supports connectivity over Direct Connect](../facts/vpc.md#vpc-faq-interface-endpoints-privatelink)
  say: AWS services, your own services or SaaS over PrivateLink
vpc-wa-sec06-no-ssh-rdp-use-session-manager
  claim: Well-Architected says security group ingress rules for EC2 instances should not allow port 22/tcp (SSH) or 3389/tcp (RDP), and to use AWS Systems Manager Session Manager for interactive access when needed, with session logging to CloudWatch Logs or Amazon S3.
  link: [do not permit access on port 22/tcp (SSH) or port 3389/tcp (RDP)](../facts/vpc.md#vpc-wa-sec06-no-ssh-rdp-use-session-manager)
  link: [Use AWS Systems Manager Session Manager to provide interactive access to instances when necessary](../facts/vpc.md#vpc-wa-sec06-no-ssh-rdp-use-session-manager)
vpc-sg-allow-rules-only
  claim: A security group holds allow rules only; it cannot hold deny rules. A network ACL can hold both allow and deny rules.
  scope: per security group.
  link: [You can specify allow rules, but not deny rules](../facts/vpc.md#vpc-sg-allow-rules-only)
  link: [Network ACLs can be used to set both Allow and Deny rules](../facts/vpc.md#vpc-sg-allow-rules-only)
vpc-sg-chain-web-allows-lb-sg
  claim: In the guide's web and database example, the web server security group allows inbound HTTPS on TCP 443 only from the load balancer's security group.
  link: [Allows inbound HTTPS access from the load balancer](../facts/vpc.md#vpc-sg-chain-web-allows-lb-sg)
  link: [ID of the security group for the load balancer](../facts/vpc.md#vpc-sg-chain-web-allows-lb-sg)
vpc-nacl-rule-order-first-match
  claim: Each network ACL rule allows or denies traffic and has a number from 1 to 32766; rules are evaluated in order starting with the lowest number, and the first rule that matches is applied without evaluating any further rules.
  scope: per network ACL rule.
  link: [a number from 1 to 32766](../facts/vpc.md#vpc-nacl-rule-order-first-match)
  link: [starting with the lowest numbered rule](../facts/vpc.md#vpc-nacl-rule-order-first-match)
  link: [we do not evaluate any additional rules](../facts/vpc.md#vpc-nacl-rule-order-first-match)
  say: rule numbers one to thirty-two thousand seven hundred sixty-six | lowest number first | the first match wins
iam-scp-applies-to-member-root-user
  claim: An SCP restricts permissions for IAM users and roles in member accounts, including the member account's root user; SCPs don't affect users or roles in the management account, and service-linked roles can't be restricted by SCPs.
  scope: member accounts of an organization.
  link: [including the member account's root user](../facts/iam.md#iam-scp-applies-to-member-root-user)
  link: [restricts permissions for IAM users and roles in member accounts](../facts/iam.md#iam-scp-applies-to-member-root-user)
iam-root-user-no-identity-policies-or-boundary
  claim: You cannot attach identity-based policies to the root user, and you cannot set a permissions boundary for the root user.
  scope: AWS account root user.
  link: [cannot attach identity-based policies to the root user](../facts/iam.md#iam-root-user-no-identity-policies-or-boundary)
  link: [cannot set a permissions boundary for the root user](../facts/iam.md#iam-root-user-no-identity-policies-or-boundary)
iam-scp-never-grants-permissions
  claim: An SCP never grants permissions; it sets a permission guardrail on the maximum permissions of IAM users and roles, and the administrator must still attach identity-based or resource-based policies to grant access.
  scope: every SCP; maximum.
  link: [An SCP never grants permissions](../facts/iam.md#iam-scp-never-grants-permissions)
  link: [a permission guardrail on the maximum permissions of IAM users and roles](../facts/iam.md#iam-scp-never-grants-permissions)
  link: [the administrator must still attach identity-based or resource-based policies](../facts/iam.md#iam-scp-never-grants-permissions)
global-infrastructure-multi-region-when-multi-az-suffices-is-anti-pattern
  claim: Implementing a multi-Region architecture when a multi-AZ architecture would satisfy the business requirements is a named anti-pattern; the desired outcome is production workloads distributed among multiple Availability Zones or Regions for fault tolerance and high availability.
  scope: location strategy.
  link: [You implement a multi-Region architecture when a multi-AZ architecture would satisfy business requirements](../facts/global-infrastructure.md#global-infrastructure-multi-region-when-multi-az-suffices-is-anti-pattern)
  link: [distributed among multiple Availability Zones (AZs) or Regions to achieve fault tolerance and high availability](../facts/global-infrastructure.md#global-infrastructure-multi-region-when-multi-az-suffices-is-anti-pattern)
  say: going multi-Region when multi-AZ is enough is an anti-pattern
well-architected-multi-az-is-ha-and-dr-multi-region-active-passive
  claim: Deploying across multiple Availability Zones in a Region is part of a high availability strategy and also part of a DR strategy; DR strategies may also use multiple Regions, for example active/passive failover from the active Region to the DR Region.
  link: [Deploying your workload across multiple Availability Zones in an AWS Region is part of a high availability strategy](../facts/well-architected.md#well-architected-multi-az-is-ha-and-dr-multi-region-active-passive)
  link: [DR strategies may also make use of multiple AWS Regions](../facts/well-architected.md#well-architected-multi-az-is-ha-and-dr-multi-region-active-passive)
