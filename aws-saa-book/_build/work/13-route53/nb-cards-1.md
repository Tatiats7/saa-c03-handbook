facts card: 10 facts
elb-custom-domain-route53-alias
  claim: To use a DNS name that is easier to remember, you associate a custom domain name with the DNS name of the Application Load Balancer, for example with an Amazon Route 53 alias record that points to the load balancer.
  scope: Application Load Balancer DNS name.
  link: [create a custom domain name](../facts/elb.md#elb-custom-domain-route53-alias)
  link: [create an alias record](../facts/elb.md#elb-custom-domain-route53-alias)
elb-route53-map-domain-to-load-balancer
  claim: AWS assigns a URL to each load balancer, and you can map your own easy-to-remember domain name to the load balancer.
  scope: Amazon Route 53 with Elastic Load Balancing.
  link: [AWS assigns URLs to your resources](../facts/elb.md#elb-route53-map-domain-to-load-balancer)
  link: [map your domain name to a load balancer](../facts/elb.md#elb-route53-map-domain-to-load-balancer)
elb-nlb-faq-route53-dns-failover
  claim: Route 53 health checks and DNS failover improve the availability of applications behind Network Load Balancers: with a multi-AZ load balancer, Route 53 fails away from an Availability Zone with no healthy instances or unhealthy load balancer nodes, and you can designate alternate load balancers for failover across Regions.
  scope: Network Load Balancer.
  link: [Route 53 health checking and DNS failover](../facts/elb.md#elb-nlb-faq-route53-dns-failover)
  link: [designate alternate load balancers for failover across regions](../facts/elb.md#elb-nlb-faq-route53-dns-failover)
  link: [fail away to alternate load balancer nodes](../facts/elb.md#elb-nlb-faq-route53-dns-failover)
elb-dns-ttl-60-seconds-remap
  claim: As traffic changes, Elastic Load Balancing scales the load balancer and updates its DNS entry, which has a TTL of 60 seconds so that the IP addresses can be remapped quickly.
  scope: load balancer DNS entry.
  link: [time-to-live (TTL) of 60 seconds](../facts/elb.md#elb-dns-ttl-60-seconds-remap)
  link: [scales your load balancer](../facts/elb.md#elb-dns-ttl-60-seconds-remap)
  link: [IP addresses can be remapped quickly](../facts/elb.md#elb-dns-ttl-60-seconds-remap)
elb-dns-returns-node-ips
  claim: Clients resolve the load balancer's domain name through DNS; Amazon controls the DNS entry and the Amazon DNS servers return the IP addresses of the load balancer nodes.
  scope: load balancer DNS name.
  link: [The DNS entry is controlled by Amazon](../facts/elb.md#elb-dns-returns-node-ips)
  link: [IP addresses of the load balancer nodes](../facts/elb.md#elb-dns-returns-node-ips)
elb-compare-static-elastic-ip-nlb-only
  claim: In the AWS feature table, only the Network Load Balancer has a static or Elastic IP address; the Application, Gateway and Classic Load Balancers do not.
  scope: Elastic Load Balancing.
  link: [IP address - Static, Elastic](../facts/elb.md#elb-compare-static-elastic-ip-nlb-only)
  link: [Network Load Balancer](../facts/elb.md#elb-compare-static-elastic-ip-nlb-only)
elb-unhealthy-target-stop-resume
  claim: When the load balancer detects an unhealthy target it stops routing traffic to it, and it resumes routing when the target is healthy again.
  scope: registered target.
  link: [it stops routing traffic to that target](../facts/elb.md#elb-unhealthy-target-stop-resume)
  link: [resumes routing traffic to that target](../facts/elb.md#elb-unhealthy-target-stop-resume)
ec2-auto-scaling-elb-checks-reroute-and-replace
  claim: When ELB health checks are enabled on the group and an instance fails them, Elastic Load Balancing stops sending it traffic while EC2 Auto Scaling replaces the instance.
  scope: per Auto Scaling group with a load balancer.
  link: [Elastic Load Balancing stops sending traffic to it](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-checks-reroute-and-replace)
  link: [Amazon EC2 Auto Scaling replaces the unhealthy instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-checks-reroute-and-replace)
ec2-eip-mask-instance-failure-remap
  claim: An Elastic IP address is a static IPv4 address; by rapidly remapping it to another instance in your account, you can mask the failure of an instance or software.
  scope: Elastic IP addresses; the replacement instance is in the same account and Region.
  link: [a static IPv4 address](../facts/ec2.md#ec2-eip-mask-instance-failure-remap)
  link: [rapidly remapping the address to another instance](../facts/ec2.md#ec2-eip-mask-instance-failure-remap)
  say: a static public IPv4 address | move the address to a healthy instance
elb-alb-global-accelerator-static-ips
  claim: An accelerator for a load balancer directs traffic over the AWS global network to static IP addresses that serve as fixed endpoints in the Region nearest the client, and AWS Global Accelerator is protected by Shield Standard.
  scope: load balancer with AWS Global Accelerator.
  link: [static IP addresses that serve as fixed endpoints](../facts/elb.md#elb-alb-global-accelerator-static-ips)
  link: [protected by Shield Standard](../facts/elb.md#elb-alb-global-accelerator-static-ips)
