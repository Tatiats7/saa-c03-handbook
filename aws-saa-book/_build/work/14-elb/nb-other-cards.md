facts card: 19 facts
waf-protected-resource-types
  claim: A web ACL (protection pack) can protect Amazon CloudFront, Amazon API Gateway, Application Load Balancer, AWS AppSync, Amazon Cognito, AWS App Runner, AWS Amplify, Amazon CloudWatch, Amazon Bedrock AgentCore Gateway and AWS Verified Access resources; for API Gateway the protected resource type is the REST API.
  scope: per web ACL (protection pack).
  link: [Amazon CloudFront, Amazon API Gateway, Application Load Balancer](../facts/waf.md#waf-protected-resource-types)
  link: [AWS AppSync, Amazon Cognito, AWS App Runner](../facts/waf.md#waf-protected-resource-types)
  link: [Amazon API Gateway REST API](../facts/waf.md#waf-protected-resource-types)
ec2-auto-scaling-elb-checks-reroute-and-replace
  claim: When ELB health checks are enabled on the group and an instance fails them, Elastic Load Balancing stops sending it traffic while EC2 Auto Scaling replaces the instance.
  scope: per Auto Scaling group with a load balancer.
  link: [Elastic Load Balancing stops sending traffic to it](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-checks-reroute-and-replace)
  link: [Amazon EC2 Auto Scaling replaces the unhealthy instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-checks-reroute-and-replace)
ec2-auto-scaling-elb-health-checks-ignored-by-default
  claim: By default, Amazon EC2 Auto Scaling ignores the results of Elastic Load Balancing health checks.
  scope: per Auto Scaling group; default; adjustable.
  link: [ignores the results of the Elastic Load Balancing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-health-checks-ignored-by-default)
  say: ignores the load balancer health checks
ec2-auto-scaling-health-elb-check-must-be-turned-on
  claim: The Elastic Load Balancing health check type checks whether the load balancer reports the instance as healthy and able to handle requests; you must turn it on for the group.
  scope: per Auto Scaling group; default; adjustable.
  link: [you must turn it on](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-elb-check-must-be-turned-on)
  link: [Elastic Load Balancing health checks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-elb-check-must-be-turned-on)
ec2-auto-scaling-lb-auto-register-deregister
  claim: With a load balancer attached, instances that the group launches are registered with the load balancer automatically, and instances it terminates are deregistered automatically; you do not register instances one by one.
  scope: per Auto Scaling group with a load balancer.
  link: [automatically registered with the load balancer](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-auto-register-deregister)
  link: [automatically deregistered from the load balancer](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-auto-register-deregister)
ec2-auto-scaling-wa-offload-session-data
  claim: To make an application stateless, Well-Architected says to offload session data to a database, a cache or external files.
  scope: AWS Well-Architected guidance.
  link: [database, cache, or external files](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-offload-session-data)
ec2-eip-mask-instance-failure-remap
  claim: An Elastic IP address is a static IPv4 address; by rapidly remapping it to another instance in your account, you can mask the failure of an instance or software.
  scope: Elastic IP addresses; the replacement instance is in the same account and Region.
  link: [a static IPv4 address](../facts/ec2.md#ec2-eip-mask-instance-failure-remap)
  link: [rapidly remapping the address to another instance](../facts/ec2.md#ec2-eip-mask-instance-failure-remap)
  say: a static public IPv4 address | move the address to a healthy instance
vpc-nacl-ephemeral-natgw-elb-lambda-1024-65535
  claim: A NAT gateway, requests from Elastic Load Balancing, and AWS Lambda functions use ephemeral ports 1024-65535, so network ACL rules for their return traffic must allow that range.
  scope: per NAT gateway, load balancer or Lambda function; fixed; not adjustable.
  link: [ports 1024-65535](../facts/vpc.md#vpc-nacl-ephemeral-natgw-elb-lambda-1024-65535)
  say: ten twenty-four to sixty-five five thirty-five
vpc-nacl-elb-health-check-deny
  claim: If the subnet of the backend instances has a network ACL deny rule for all traffic from 0.0.0.0/0 or from the subnet CIDR, the load balancer cannot carry out health checks on the instances.
  link: [your load balancer can't carry out health checks on the instances](../facts/vpc.md#vpc-nacl-elb-health-check-deny)
  say: health checks fail
vpc-sg-chain-web-allows-lb-sg
  claim: In the guide's web and database example, the web server security group allows inbound HTTPS on TCP 443 only from the load balancer's security group.
  link: [Allows inbound HTTPS access from the load balancer](../facts/vpc.md#vpc-sg-chain-web-allows-lb-sg)
  link: [ID of the security group for the load balancer](../facts/vpc.md#vpc-sg-chain-web-allows-lb-sg)
vpc-wa-rel10-bp01-avoid-single-points-of-failure
  claim: A fundamental AWS design principle is to avoid single points of failure, including the physical infrastructure; a production workload that exists in only one Availability Zone is an anti-pattern.
  link: [avoid single points of failure, including the underlying physical infrastructure](../facts/vpc.md#vpc-wa-rel10-bp01-avoid-single-points-of-failure)
  link: [Your production workload exists only in a single Availability Zone](../facts/vpc.md#vpc-wa-rel10-bp01-avoid-single-points-of-failure)
lambda-trigger-alb-sync
  claim: Elastic Load Balancing (an Application Load Balancer) is an event-driven trigger that invokes a Lambda function synchronously.
  scope: Application Load Balancer as a Lambda trigger.
  link: [Event-driven; synchronous invocation](../facts/lambda.md#lambda-trigger-alb-sync)
  link: [Application Load Balancer](../facts/lambda.md#lambda-trigger-alb-sync)
  say: event-driven, synchronous invocation
cognito-alb-authenticate-cognito-https-only
  claim: An Application Load Balancer can authenticate users before they reach the application, through an OIDC-compliant IdP or through Cognito user pools (social IdPs and corporate SAML, OIDC or OAuth identities); the authenticate-cognito and authenticate-oidc actions are supported only on HTTPS listeners.
  scope: Application Load Balancer listener rules.
  link: [offload the work of authenticating users](../facts/cognito.md#cognito-alb-authenticate-cognito-https-only)
  link: [supported only with HTTPS listeners](../facts/cognito.md#cognito-alb-authenticate-cognito-https-only)
shield-advanced-resource-types
  claim: Shield Advanced protects CloudFront distributions, Route 53 hosted zones, Global Accelerator standard accelerators, EC2 Elastic IP addresses (and the EC2 instances and Network Load Balancers associated with them), Application Load Balancers and Classic Load Balancers.
  scope: Shield Advanced protections.
  link: [Amazon EC2 instances, through association to Amazon EC2 Elastic IP addresses.](../facts/shield.md#shield-advanced-resource-types)
  link: [Network Load Balancers, through associations to Amazon EC2 Elastic IP addresses.](../facts/shield.md#shield-advanced-resource-types)
  link: [AWS Global Accelerator standard accelerators.](../facts/shield.md#shield-advanced-resource-types)
ec2-auto-scaling-alb-minimum-two-azs
  claim: An Application Load Balancer must have at least two Availability Zones enabled.
  scope: per Application Load Balancer; minimum.
  link: [at least two Availability Zones](../facts/ec2-auto-scaling.md#ec2-auto-scaling-alb-minimum-two-azs)
ec2-auto-scaling-faq-elb-requests-before-detection-fail
  claim: When ELB notices that an instance is unhealthy it stops routing requests to it, but before it discovers that the instance is unhealthy, some requests to that instance fail.
  scope: per Auto Scaling group with a load balancer.
  link: [some requests to that instance will fail](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-elb-requests-before-detection-fail)
  link: [stop routing requests to it](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-elb-requests-before-detection-fail)
ec2-eip-charged-in-use-and-idle
  claim: All Elastic IP addresses are charged, whether in use or idle, and AWS charges for all public IPv4 addresses, including those on running instances.
  scope: per Elastic IP address.
  link: [a charge for all Elastic IP addresses](../facts/ec2.md#ec2-eip-charged-in-use-and-idle)
  link: [AWS charges for all public IPv4 addresses](../facts/ec2.md#ec2-eip-charged-in-use-and-idle)
  say: every Elastic IP is charged, used or idle
waf-one-web-acl-per-resource
  claim: You can associate each AWS resource with only one web ACL (protection pack); one web ACL can be associated with many resources (one-to-many).
  scope: per AWS resource.
  link: [with only one protection pack (web ACL)](../facts/waf.md#waf-one-web-acl-per-resource)
  link: [one-to-many](../facts/waf.md#waf-one-web-acl-per-resource)
ec2-auto-scaling-faq-which-health-check-type
  claim: If the group uses Elastic Load Balancing, select the ELB health check; if it does not, select the EC2 health check.
  scope: per Auto Scaling group (health checks).
  link: [select an ELB health check](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-which-health-check-type)
  link: [select the EC2 health check](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-which-health-check-type)
