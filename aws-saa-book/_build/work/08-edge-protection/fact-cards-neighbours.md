facts card: 11 facts
well-architected-sec05-anti-pattern-perimeter-only
  claim: Well-Architected lists as anti-patterns controlling traffic only at the boundary of network layers, and applying controls to ingress or egress traffic but not both.
  scope: SEC05-BP02 Control traffic flow within your network layers.
  link: [You take a perimeter-based approach to network security](../facts/well-architected.md#well-architected-sec05-anti-pattern-perimeter-only)
  link: [but not both](../facts/well-architected.md#well-architected-sec05-anti-pattern-perimeter-only)
well-architected-sec05-control-north-south-then-east-west
  claim: Well-Architected SEC05-BP02 says to segment within network layers so only necessary flows are allowed, first controlling north-south traffic between the internet or external systems and the workload, then east-west traffic between components.
  scope: SEC05-BP02 Control traffic flow within your network layers.
  link: [*north-south* traffic](../facts/well-architected.md#well-architected-sec05-control-north-south-then-east-west)
  link: [*east-west* traffic](../facts/well-architected.md#well-architected-sec05-control-north-south-then-east-west)
well-architected-sec05-finer-control-services
  claim: Security groups and route tables give traffic control at Layer 4 (IP address and port ranges), and you can gain further control with additional services such as AWS PrivateLink, DNS Firewall, AWS Network Firewall and AWS WAF.
  scope: SEC05-BP02 implementation guidance.
  link: [traffic control at a Layer 4 level (IP address and port ranges)](../facts/well-architected.md#well-architected-sec05-finer-control-services)
  link: [you can gain further control using additional services](../facts/well-architected.md#well-architected-sec05-finer-control-services)
well-architected-sec05-layers-reduce-inspection-scope
  claim: Well-Architected SEC05-BP01 says establishing network layers is the first step in restricting unnecessary pathways through the network, and discrete layers reduce the scope of analysis for inspection systems such as intrusion detection or malware prevention.
  scope: SEC05-BP01 Create network layers.
  link: [the first step in restricting unnecessary pathways](../facts/well-architected.md#well-architected-sec05-layers-reduce-inspection-scope)
  link: [reduce the scope of analysis for inspection systems](../facts/well-architected.md#well-architected-sec05-layers-reduce-inspection-scope)
vpc-sg-allow-rules-only
  claim: A security group holds allow rules only; it cannot hold deny rules. A network ACL can hold both allow and deny rules.
  scope: per security group.
  link: [You can specify allow rules, but not deny rules](../facts/vpc.md#vpc-sg-allow-rules-only)
  link: [Network ACLs can be used to set both Allow and Deny rules](../facts/vpc.md#vpc-sg-allow-rules-only)
vpc-def-network-acl
  claim: A network ACL allows or denies specific inbound or outbound traffic at the subnet level.
  scope: per network ACL.
  link: [allows or denies specific inbound or outbound traffic at the subnet level](../facts/vpc.md#vpc-def-network-acl)
  say: an allow-and-deny filter on the subnet
vpc-network-firewall-stateful-managed
  claim: AWS Network Firewall filters network traffic at the perimeter of a VPC; it is a stateful, managed network firewall and intrusion detection and prevention service.
  link: [filter network traffic at the perimeter of your VPC](../facts/vpc.md#vpc-network-firewall-stateful-managed)
  link: [a stateful, managed, network firewall and intrusion detection and prevention service](../facts/vpc.md#vpc-network-firewall-stateful-managed)
  say: a stateful managed firewall with intrusion prevention
vpc-quota-rules-per-network-acl
  claim: The default quota is 20 rules per network ACL, which is the maximum for inbound rules and for outbound rules; it can be raised to at most 40 inbound rules and 40 outbound rules (80 in total), but network performance might be impacted.
  scope: per network ACL; default; adjustable; maximum 40 inbound and 40 outbound; performance might be impacted.
  link: [20 rules per network ACL](../facts/vpc.md#vpc-quota-rules-per-network-acl)
  link: [40 inbound rules and 40 outbound rules](../facts/vpc.md#vpc-quota-rules-per-network-acl)
  say: twenty rules per network ACL | up to forty inbound and forty outbound
vpc-nacl-deny-rule-lower-number
  claim: To deny some ports inside a wide allowed port range, give the deny rule a lower number than the rule that allows the wider range.
  link: [give the deny rule a lower number than the rule that allows the wider range of port traffic](../facts/vpc.md#vpc-nacl-deny-rule-lower-number)
  say: the deny rule needs the lower number
vpc-sg-vs-nacl-rule-type
  claim: A security group supports allow rules only; a network ACL supports allow and deny rules.
  link: [Allow rules only](../facts/vpc.md#vpc-sg-vs-nacl-rule-type)
  link: [Allow and deny rules](../facts/vpc.md#vpc-sg-vs-nacl-rule-type)
vpc-sg-vs-nacl-level
  claim: A security group operates at the instance level; a network ACL operates at the subnet level.
  link: [Instance level](../facts/vpc.md#vpc-sg-vs-nacl-level)
  link: [Subnet level](../facts/vpc.md#vpc-sg-vs-nacl-level)
