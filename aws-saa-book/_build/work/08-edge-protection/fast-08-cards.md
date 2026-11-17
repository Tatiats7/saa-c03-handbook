facts card: 32 facts
waf-definition-web-application-firewall
  claim: AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to your protected web application resources.
  scope: per protected resource.
  link: [a web application firewall](../facts/waf.md#waf-definition-web-application-firewall)
  link: [monitor the HTTP and HTTPS requests](../facts/waf.md#waf-definition-web-application-firewall)
shield-standard-automatic-no-charge
  claim: All AWS customers get the automatic protection of Shield Standard at no additional charge; it defends against the most common, frequently occurring network and transport layer DDoS attacks.
  scope: every AWS account; default; not adjustable.
  link: [at no additional charge](../facts/shield.md#shield-standard-automatic-no-charge)
  link: [All AWS customers benefit from the automatic protection](../facts/shield.md#shield-standard-automatic-no-charge)
  link: [network and transport layer DDoS attacks](../facts/shield.md#shield-standard-automatic-no-charge)
network-firewall-definition
  claim: AWS Network Firewall is a stateful, managed network firewall and intrusion detection and prevention service for your VPC.
  scope: per VPC.
  link: [a stateful, managed, network firewall](../facts/network-firewall.md#network-firewall-definition)
  link: [intrusion detection and prevention service](../facts/network-firewall.md#network-firewall-definition)
firewall-manager-definition-central-rules
  claim: AWS Firewall Manager is a security management service that lets you centrally configure and manage firewall rules across your accounts and applications in AWS Organizations.
  scope: per organization in AWS Organizations.
  link: [a security management service](../facts/firewall-manager.md#firewall-manager-definition-central-rules)
  link: [centrally configure and manage firewall rules](../facts/firewall-manager.md#firewall-manager-definition-central-rules)
waf-forwards-requests-then-block-or-allow
  claim: The underlying service forwards the requests it receives to AWS WAF for inspection against your rules; once a request meets a condition defined in your rules, AWS WAF instructs the underlying service to either block or allow the request based on the action you define.
  scope: per protected resource.
  link: [forwards those requests to AWS WAF for inspection](../facts/waf.md#waf-forwards-requests-then-block-or-allow)
  link: [to either block or allow the request](../facts/waf.md#waf-forwards-requests-then-block-or-allow)
network-firewall-route-tables-enable-protection
  claim: The firewall protects subnets in your VPC by filtering traffic between them and locations outside the VPC, and to enable its protection you modify the VPC route tables to send traffic through the Network Firewall firewall endpoints.
  scope: per VPC.
  link: [you modify your Amazon VPC route tables](../facts/network-firewall.md#network-firewall-route-tables-enable-protection)
  link: [through the Network Firewall firewall endpoints](../facts/network-firewall.md#network-firewall-route-tables-enable-protection)
waf-vs-shield-layer
  claim: AWS WAF protects at the application layer (L7); AWS Shield protects at the network, transport and application layers (L3/L4/L7).
  scope: AWS WAF compared with AWS Shield.
  link: [Application layer (L7)](../facts/waf.md#waf-vs-shield-layer)
  link: [Network, transport, and application layers (L3/L4/L7)](../facts/waf.md#waf-vs-shield-layer)
waf-vs-shield-inspection-level
  claim: AWS WAF inspects traffic at the request level, while AWS Shield inspects at the packet level.
  scope: AWS WAF compared with AWS Shield.
  link: [Request-level](../facts/waf.md#waf-vs-shield-inspection-level)
  link: [Packet-level](../facts/waf.md#waf-vs-shield-inspection-level)
waf-vs-shield-deployment
  claim: AWS WAF must be explicitly set up, while AWS Shield Standard protection is included for all customer accounts.
  scope: AWS WAF compared with AWS Shield.
  link: [Must be explicitly set up](../facts/waf.md#waf-vs-shield-deployment)
  link: [Shield Standard protection included for all customer accounts](../facts/waf.md#waf-vs-shield-deployment)
network-firewall-complements-sg-waf-marketplace
  claim: Network Firewall complements existing AWS network and application security services by giving control and visibility of Layer 3-7 traffic for the whole VPC, and you may use it alongside security groups, AWS WAF rules or AWS Marketplace appliances.
  scope: AWS Network Firewall.
  link: [control and visibility to Layer 3-7 network traffic for your entire VPC](../facts/network-firewall.md#network-firewall-complements-sg-waf-marketplace)
  link: [along your existing security controls](../facts/network-firewall.md#network-firewall-complements-sg-waf-marketplace)
network-firewall-faq-inspects-routed-traffic
  claim: AWS Network Firewall inspects all traffic that is routed to its endpoint; routing is the mechanism for path insertion and filtering.
  scope: per firewall endpoint.
  link: [all traffic that is routed to the endpoint](../facts/network-firewall.md#network-firewall-faq-inspects-routed-traffic)
shield-advanced-monthly-fee
  claim: AWS Shield Advanced costs a monthly fee of $3,000 per month per organization, plus Shield Advanced data transfer usage fees for the resources it protects.
  scope: per organization (payer account); AWS Channel Resellers pay a separate monthly fee for each member account (pricing page note).
  link: [$3,000 per month](../facts/shield.md#shield-advanced-monthly-fee)
  say: three thousand dollars per month
shield-advanced-one-year-commitment
  claim: AWS Shield Advanced requires a 1-year subscription commitment and a monthly fee, plus a usage fee based on data transfer out from CloudFront, ELB, EC2 and Global Accelerator; subscriptions auto-renew annually.
  scope: per Shield Advanced subscription; all Shield Advanced benefits, including DDoS cost protection, are subject to fulfilling the 1-year commitment.
  link: [1-year subscription commitment](../facts/shield.md#shield-advanced-one-year-commitment)
  link: [auto-renew annually](../facts/shield.md#shield-advanced-one-year-commitment)
  say: one-year subscription commitment
shield-advanced-not-automatic-per-resource
  claim: Shield Advanced protections are enabled only for resources that you explicitly specify in Shield Advanced or protect through a Firewall Manager Shield Advanced policy; Shield Advanced does not automatically protect your resources.
  scope: per resource.
  link: [explicitly specified in Shield Advanced](../facts/shield.md#shield-advanced-not-automatic-per-resource)
  link: [Shield Advanced doesn't automatically protect your resources.](../facts/shield.md#shield-advanced-not-automatic-per-resource)
shield-faq-advanced-layers-srt-cost-protection
  claim: AWS Shield Advanced includes DDoS protection for layers 3, 4 and 7, 24/7 support from the Shield Response Team (SRT), and cost protection against event spikes.
  scope: Shield Advanced subscription.
  link: [layers 3, 4, and 7](../facts/shield.md#shield-faq-advanced-layers-srt-cost-protection)
  link: [24/7 support from the Shield Response Team](../facts/shield.md#shield-faq-advanced-layers-srt-cost-protection)
waf-faq-sqli-xss-protection
  claim: AWS WAF helps protect a website from common attack techniques like SQL injection and cross-site scripting (XSS).
  scope: AWS WAF.
  link: [SQL injection and Cross-Site Scripting (XSS)](../facts/waf.md#waf-faq-sqli-xss-protection)
shield-faq-standard-layer-3-4-all-customers
  claim: AWS Shield Standard protects all AWS customers against common, frequently occurring infrastructure (layer 3 and 4) events such as SYN/UDP floods and reflection events.
  scope: AWS Shield Standard.
  link: [layer 3 and 4](../facts/shield.md#shield-faq-standard-layer-3-4-all-customers)
  link: [for all AWS customers](../facts/shield.md#shield-faq-standard-layer-3-4-all-customers)
waf-faq-rate-based-web-layer-ddos
  claim: AWS WAF rate-based rules are designed to protect against use cases such as web-layer DDoS attacks, brute force login attempts and bad bots.
  scope: rate-based rules.
  link: [web-layer DDoS attacks](../facts/waf.md#waf-faq-rate-based-web-layer-ddos)
  link: [brute force login attempts](../facts/waf.md#waf-faq-rate-based-web-layer-ddos)
network-firewall-domain-sni-host-header
  claim: For HTTPS traffic, Network Firewall uses the Server Name Indication (SNI) in the TLS handshake to find the domain name, and for HTTP it uses the Host header; it does not do out-of-band DNS lookups and uses the SNI or Host header, not IP addresses, for domain list rules.
  scope: domain list rule groups.
  link: [Server Name Indication (SNI) extension](../facts/network-firewall.md#network-firewall-domain-sni-host-header)
  link: [uses the HTTP host header](../facts/network-firewall.md#network-firewall-domain-sni-host-header)
  link: [doesn't pause connections to do out-of-band DNS lookups](../facts/network-firewall.md#network-firewall-domain-sni-host-header)
firewall-manager-auto-applies-to-new-accounts
  claim: If you add a new account to the organization, Firewall Manager automatically applies the policy to the resources in that account that are within the policy scope.
  scope: per Firewall Manager policy; resources within policy scope.
  link: [Firewall Manager automatically applies the policy](../facts/firewall-manager.md#firewall-manager-auto-applies-to-new-accounts)
network-firewall-when-to-use
  claim: AWS positions Network Firewall for control and visibility of VPC-to-VPC traffic, URL, IP and domain-based outbound filtering to stop data leaks and block known malware hosts, securing Direct Connect and VPN traffic through Transit Gateway, and filtering inbound internet traffic.
  scope: AWS Network Firewall.
  link: [control and visibility of VPC-to-VPC traffic](../facts/network-firewall.md#network-firewall-when-to-use)
  link: [URL, IP address, and domain-based outbound traffic filtering](../facts/network-firewall.md#network-firewall-when-to-use)
network-firewall-not-for-ddos
  claim: Network Firewall is designed to protect and control access to and from your VPC, not to mitigate volumetric attacks like DDoS; for DDoS protection AWS recommends the AWS Best Practices for DDoS Resiliency and AWS Shield Advanced.
  scope: AWS Network Firewall.
  link: [but not to mitigate volumetric attacks](../facts/network-firewall.md#network-firewall-not-for-ddos)
  link: [explore AWS Shield Advanced](../facts/network-firewall.md#network-firewall-not-for-ddos)
waf-protected-resource-types
  claim: A web ACL (protection pack) can protect Amazon CloudFront, Amazon API Gateway, Application Load Balancer, AWS AppSync, Amazon Cognito, AWS App Runner, AWS Amplify, Amazon CloudWatch, Amazon Bedrock AgentCore Gateway and AWS Verified Access resources; for API Gateway the protected resource type is the REST API.
  scope: per web ACL (protection pack).
  link: [Amazon CloudFront, Amazon API Gateway, Application Load Balancer](../facts/waf.md#waf-protected-resource-types)
  link: [AWS AppSync, Amazon Cognito, AWS App Runner](../facts/waf.md#waf-protected-resource-types)
  link: [Amazon API Gateway REST API](../facts/waf.md#waf-protected-resource-types)
shield-advanced-resource-types
  claim: Shield Advanced protects CloudFront distributions, Route 53 hosted zones, Global Accelerator standard accelerators, EC2 Elastic IP addresses (and the EC2 instances and Network Load Balancers associated with them), Application Load Balancers and Classic Load Balancers.
  scope: Shield Advanced protections.
  link: [Amazon EC2 instances, through association to Amazon EC2 Elastic IP addresses.](../facts/shield.md#shield-advanced-resource-types)
  link: [Network Load Balancers, through associations to Amazon EC2 Elastic IP addresses.](../facts/shield.md#shield-advanced-resource-types)
  link: [AWS Global Accelerator standard accelerators.](../facts/shield.md#shield-advanced-resource-types)
shield-no-http-content-inspection
  claim: AWS Shield inspects traffic primarily at the network and transport layers and does not inspect the contents of application layer (HTTP/S) traffic; it looks for DDoS patterns such as unusually high traffic volumes or protocol misuse.
  scope: AWS Shield.
  link: [does not inspect the contents](../facts/shield.md#shield-no-http-content-inspection)
  link: [unusually high traffic volumes or protocol misuse](../facts/shield.md#shield-no-http-content-inspection)
waf-vs-shield-primary-purpose
  claim: AWS WAF protects against exploits on web applications (such as SQL injection or XSS), while AWS Shield protects against DDoS attacks (such as SYN or UDP floods).
  scope: AWS WAF compared with AWS Shield.
  link: [Protects against exploits on web applications](../facts/waf.md#waf-vs-shield-primary-purpose)
  link: [Protects against DDoS attacks](../facts/waf.md#waf-vs-shield-primary-purpose)
shield-advanced-paid-expanded-protection
  claim: Shield Advanced is a subscription that provides expanded DDoS attack protection for the resources you add protection to, and it incurs additional charges.
  scope: per protected resource; account subscribed and protection added to the resource.
  link: [provides expanded DDoS attack protection](../facts/shield.md#shield-advanced-paid-expanded-protection)
  link: [Shield Advanced incurs additional charges.](../facts/shield.md#shield-advanced-paid-expanded-protection)
waf-rate-limit-minimum
  claim: The lowest rate limit that a rate-based rule accepts is 10; before August 30, 2024 the minimum request rate was 100.
  scope: per rate-based rule; minimum; not adjustable; the rate limit counts requests in the rule's evaluation window.
  link: [10](../facts/waf.md#waf-rate-limit-minimum)
  link: [100](../facts/waf.md#waf-rate-limit-minimum)
  say: ten requests | one hundred requests
  changed: 2024-08-30: was 100
waf-rate-window-options
  claim: The evaluation window of a rate-based rule can be 1 minute, 2 minutes, 5 minutes or 10 minutes, and 5 minutes is the default; before February 28, 2024 the only option was 5 minutes.
  scope: per rate-based rule; default; adjustable; the window sets how far back AWS WAF counts, not how often it checks.
  link: [5 minutes](../facts/waf.md#waf-rate-window-options)
  link: [10 minutes](../facts/waf.md#waf-rate-window-options)
  link: [1 minute](../facts/waf.md#waf-rate-window-options)
  say: five minutes | ten minutes | one minute
  changed: 2024-02-28: was 5 minutes
waf-ip-set-max-addresses
  claim: One IP set can hold at most 10,000 IP addresses or IP address ranges in CIDR notation; this quota is fixed.
  scope: per IP set; maximum; not adjustable.
  link: [10,000](../facts/waf.md#waf-ip-set-max-addresses)
  say: ten thousand addresses or ranges
vpc-quota-rules-per-network-acl
  claim: The default quota is 20 rules per network ACL, which is the maximum for inbound rules and for outbound rules; it can be raised to at most 40 inbound rules and 40 outbound rules (80 in total), but network performance might be impacted.
  scope: per network ACL; default; adjustable; maximum 40 inbound and 40 outbound; performance might be impacted.
  link: [20 rules per network ACL](../facts/vpc.md#vpc-quota-rules-per-network-acl)
  link: [40 inbound rules and 40 outbound rules](../facts/vpc.md#vpc-quota-rules-per-network-acl)
  say: twenty rules per network ACL | up to forty inbound and forty outbound
waf-atp-inspects-login-attempts
  claim: The ATP managed rule group labels and manages requests that might be part of account takeover attempts by inspecting login attempts that clients send to the application's login endpoint, and it checks email and password combinations against a stolen credential database.
  scope: AWSManagedRulesATPRuleSet.
  link: [inspecting login attempts](../facts/waf.md#waf-atp-inspects-login-attempts)
  link: [against its stolen credential database](../facts/waf.md#waf-atp-inspects-login-attempts)
