facts card: 452 facts
firewall-manager-accounts-manage-own-rules
  claim: In the web ACLs that Firewall Manager manages, individual accounts can manage their own rules and rule groups in addition to the rule groups defined in the Firewall Manager policy.
  scope: Firewall Manager-managed web ACLs.
  link: [can manage their own rules and rule groups](../facts/firewall-manager.md#firewall-manager-accounts-manage-own-rules)
firewall-manager-audit-or-auto-remediate
  claim: For every Firewall Manager policy you can choose to only view the accounts and resources that are out of compliance without taking corrective action, or to automatically remediate noncompliant resources.
  scope: per Firewall Manager policy.
  link: [without taking corrective action](../facts/firewall-manager.md#firewall-manager-audit-or-auto-remediate)
  link: [automatically remediate noncompliant resources](../facts/firewall-manager.md#firewall-manager-audit-or-auto-remediate)
firewall-manager-auto-applies-to-new-accounts
  claim: If you add a new account to the organization, Firewall Manager automatically applies the policy to the resources in that account that are within the policy scope.
  scope: per Firewall Manager policy; resources within policy scope.
  link: [Firewall Manager automatically applies the policy](../facts/firewall-manager.md#firewall-manager-auto-applies-to-new-accounts)
firewall-manager-best-for-whole-org
  claim: Firewall Manager is particularly useful when you want to protect your entire organization rather than a few specific accounts and resources, or when you frequently add new resources to protect; it also provides centralized monitoring of DDoS attacks across the organization.
  scope: per organization.
  link: [protect your entire organization](../facts/firewall-manager.md#firewall-manager-best-for-whole-org)
  link: [if you frequently add new resources](../facts/firewall-manager.md#firewall-manager-best-for-whole-org)
firewall-manager-change-nacl-policies-2024
  claim: On April 25, 2024, Firewall Manager added network ACL policies, which manage Amazon VPC network ACLs across an organization by enforcing first and last rules in the network ACLs in scope.
  scope: per organization.
  link: [April 25, 2024](../facts/firewall-manager.md#firewall-manager-change-nacl-policies-2024)
  link: [enforces the presence and ordering](../facts/firewall-manager.md#firewall-manager-change-nacl-policies-2024)
  say: April twenty-fifth, twenty twenty-four
firewall-manager-change-quota-increases-2023
  claim: On May 5, 2023, Firewall Manager raised policies per organization from 20 to 50 and primary security groups per policy from one to three, and made the WCU maximum a hard quota.
  scope: per organization.
  link: [May 5, 2023](../facts/firewall-manager.md#firewall-manager-change-quota-increases-2023)
  link: [from 20 to 50](../facts/firewall-manager.md#firewall-manager-change-quota-increases-2023)
  say: May fifth, twenty twenty-three | from twenty to fifty
  changed: 2023-05-05: was 20
firewall-manager-change-retrofit-web-acls-2024
  claim: On October 22, 2024, Firewall Manager AWS WAF policies began to retrofit existing account-owned web ACLs and to create new web ACLs only where needed.
  scope: Firewall Manager AWS WAF policies.
  link: [October 22, 2024](../facts/firewall-manager.md#firewall-manager-change-retrofit-web-acls-2024)
  say: October twenty-second, twenty twenty-four
firewall-manager-charges-underlying-services
  claim: Firewall Manager protection policies are priced with a monthly fee per Region, except AWS Shield protection policies, whose price is included in the Shield Advanced subscription; the AWS WAF web ACLs and rules and the AWS Config rules that Firewall Manager creates are charged based on current pricing.
  scope: Firewall Manager protection policies; AWS Shield protection policies need a Shield Advanced subscription.
  link: [priced with a monthly fee per region](../facts/firewall-manager.md#firewall-manager-charges-underlying-services)
  link: [charged based on current pricing](../facts/firewall-manager.md#firewall-manager-charges-underlying-services)
firewall-manager-compliance-definition
  claim: You can view the compliance status of the accounts and resources in scope of any Firewall Manager policy; an account or resource is compliant if the policy settings are reflected in its settings.
  scope: per Firewall Manager policy.
  link: [the settings in the policy are reflected](../facts/firewall-manager.md#firewall-manager-compliance-definition)
firewall-manager-config-continuous-recording
  claim: For Firewall Manager to monitor policy compliance, AWS Config must continuously record configuration changes for protected resources; the recording frequency must be Continuous, which is the default.
  scope: AWS Config in member accounts; default.
  link: [the recording frequency must be set to **Continuous**](../facts/firewall-manager.md#firewall-manager-config-continuous-recording)
firewall-manager-config-rules-per-account
  claim: Firewall Manager creates two AWS Config rules per policy, per account, and those Config rules are charged at AWS Config pricing.
  scope: per policy, per account.
  link: [two AWS Config rules per policy, per account](../facts/firewall-manager.md#firewall-manager-config-rules-per-account)
firewall-manager-default-admin-full-scope
  claim: The default Firewall Manager administrator has full administrative scope: it can apply policies to all accounts and OUs in the organization, act in all Regions, manage all policy types, and manage third-party firewalls.
  scope: Firewall Manager default administrator.
  link: [The default administrator has full administrative scope.](../facts/firewall-manager.md#firewall-manager-default-admin-full-scope)
  link: [can manage third-party firewalls](../facts/firewall-manager.md#firewall-manager-default-admin-full-scope)
firewall-manager-definition-central-rules
  claim: AWS Firewall Manager is a security management service that lets you centrally configure and manage firewall rules across your accounts and applications in AWS Organizations.
  scope: per organization in AWS Organizations.
  link: [a security management service](../facts/firewall-manager.md#firewall-manager-definition-central-rules)
  link: [centrally configure and manage firewall rules](../facts/firewall-manager.md#firewall-manager-definition-central-rules)
firewall-manager-dns-firewall-policy-associations
  claim: DNS Firewall filters and regulates outbound DNS traffic for VPCs; a Firewall Manager DNS Firewall policy associates each DNS Firewall rule group in the policy with each in-scope VPC in every in-scope account.
  scope: Firewall Manager DNS Firewall policies.
  link: [regulation of outbound DNS traffic for your VPCs](../facts/firewall-manager.md#firewall-manager-dns-firewall-policy-associations)
  link: [an association between each DNS Firewall rule group](../facts/firewall-manager.md#firewall-manager-dns-firewall-policy-associations)
firewall-manager-faq-auto-or-manual-remediation
  claim: A Firewall Manager policy can use automatic remediation, which monitors for drift and applies rules on non-compliant resources, or manual remediation, which creates the policy and rules in each account but does not enforce them on the resources.
  scope: per Firewall Manager policy.
  link: [does not enforce the rules on the resources](../facts/firewall-manager.md#firewall-manager-faq-auto-or-manual-remediation)
firewall-manager-faq-nacls-for-subnets
  claim: AWS Firewall Manager can configure new VPC network access control lists (ACLs) for your VPC subnets.
  scope: Firewall Manager network ACL policies.
  link: [network access control lists (ACLs)](../facts/firewall-manager.md#firewall-manager-faq-nacls-for-subnets)
firewall-manager-faq-network-firewall-and-dns-firewall
  claim: AWS Firewall Manager can deploy AWS Network Firewalls across accounts and VPCs in your organization and associate Amazon Route 53 Resolver DNS Firewall rules across VPCs.
  scope: Firewall Manager Network Firewall and DNS Firewall policies.
  link: [deploy AWS Network Firewalls across accounts and VPCs](../facts/firewall-manager.md#firewall-manager-faq-network-firewall-and-dns-firewall)
firewall-manager-faq-no-resource-limit
  claim: There is not a limit on the number of resources managed by Firewall Manager at this time.
  scope: per Firewall Manager administrator; maximum; not adjustable.
  link: [not a limit on the number of resources](../facts/firewall-manager.md#firewall-manager-faq-no-resource-limit)
firewall-manager-faq-prereq-administrator-account
  claim: Firewall Manager must be associated with the management account of your AWS organization or with a member account that has the appropriate permissions; that account is the Firewall Manager administrator account.
  scope: per organization.
  link: [the Firewall Manager administrator account](../facts/firewall-manager.md#firewall-manager-faq-prereq-administrator-account)
firewall-manager-faq-security-groups-resources
  claim: AWS Firewall Manager can configure new VPC security groups and audit existing security groups for Amazon EC2, Application Load Balancer and ENI resource types.
  scope: Firewall Manager security group policies.
  link: [audit any existing security groups](../facts/firewall-manager.md#firewall-manager-faq-security-groups-resources)
firewall-manager-faq-shield-advanced-resources
  claim: AWS Firewall Manager can create AWS Shield Advanced protections for Application Load Balancers, ELB Classic Load Balancers, Elastic IP addresses and CloudFront distributions.
  scope: Firewall Manager Shield Advanced policies.
  link: [ELB Classic Load Balancers, Elastic IP Addresses](../facts/firewall-manager.md#firewall-manager-faq-shield-advanced-resources)
firewall-manager-faq-sns-and-security-hub
  claim: Firewall Manager can send real-time SNS notifications when new non-compliant resources are discovered, and each account in scope is notified of non-compliant events on AWS Security Hub.
  scope: per Firewall Manager policy.
  link: [real-time notifications](../facts/firewall-manager.md#firewall-manager-faq-sns-and-security-hub)
  link: [non-compliant events on AWS Security Hub](../facts/firewall-manager.md#firewall-manager-faq-sns-and-security-hub)
firewall-manager-faq-waf-rules-on-alb-apigw-cloudfront
  claim: AWS Firewall Manager can roll out AWS WAF rules across Application Load Balancers, API Gateways and Amazon CloudFront distributions.
  scope: Firewall Manager AWS WAF policies.
  link: [Easily roll out AWS WAF rules across](../facts/firewall-manager.md#firewall-manager-faq-waf-rules-on-alb-apigw-cloudfront)
firewall-manager-findings-to-security-hub
  claim: Firewall Manager creates findings for resources that are out of compliance and for attacks that it detects, and sends them to AWS Security Hub CSPM automatically when you use both services.
  scope: per Firewall Manager administrator; Security Hub CSPM in use.
  link: [it sends them to AWS Security Hub CSPM](../facts/firewall-manager.md#firewall-manager-findings-to-security-hub)
  link: [for resources that are out of compliance](../facts/firewall-manager.md#firewall-manager-findings-to-security-hub)
firewall-manager-included-with-shield-advanced
  claim: For AWS Shield Advanced customers, Firewall Manager protection policies are included at no additional charge, but the AWS Config rules that Firewall Manager creates are still charged.
  scope: per Shield Advanced customer.
  link: [included at no additional charge](../facts/firewall-manager.md#firewall-manager-included-with-shield-advanced)
firewall-manager-management-account-creates-admin
  claim: Only the organization's management account can create Firewall Manager default administrator accounts; Firewall Manager sets the default administrator as an AWS Organizations delegated administrator for Firewall Manager.
  scope: per organization.
  link: [Only the organization's management account can create](../facts/firewall-manager.md#firewall-manager-management-account-creates-admin)
  link: [an AWS Organizations delegated administrator for Firewall Manager](../facts/firewall-manager.md#firewall-manager-management-account-creates-admin)
firewall-manager-manual-remediation-mode
  claim: A Firewall Manager policy can run with manual remediation, which creates the policy and associated rules in each account but does not enforce them on resources; you can later edit the policy to remediate automatically.
  scope: per Firewall Manager policy.
  link: [does not enforce the rules on the resources](../facts/firewall-manager.md#firewall-manager-manual-remediation-mode)
  link: [edit the policy to automatically remediate](../facts/firewall-manager.md#firewall-manager-manual-remediation-mode)
firewall-manager-max-administrators
  claim: An organization can have at most 10 Firewall Manager administrators: one default administrator and up to nine more; this quota can't be changed.
  scope: per organization; maximum; not adjustable.
  link: [10](../facts/firewall-manager.md#firewall-manager-max-administrators)
  say: ten administrators
firewall-manager-multiple-admins-scoped
  claim: Firewall Manager can have one or multiple administrators; with multiple administrators you apply administrative scope conditions to each, such as the accounts or OUs, Regions and policy types it can manage.
  scope: per organization.
  link: [you can have one or multiple administrators](../facts/firewall-manager.md#firewall-manager-multiple-admins-scoped)
  link: [apply administrative scope conditions to each administrator](../facts/firewall-manager.md#firewall-manager-multiple-admins-scoped)
firewall-manager-nacl-first-last-rules
  claim: By default, a Firewall Manager network ACL policy can have 5 inbound rules and 5 outbound rules used as first or last rules, for example 2 first and 3 last.
  scope: per network ACL policy, per direction; default; adjustable.
  link: [5](../facts/firewall-manager.md#firewall-manager-nacl-first-last-rules)
  say: five rules in each direction
firewall-manager-needs-org-all-features
  claim: To use Firewall Manager, your account must be a member of the AWS Organizations organization where you use the policies, and the organization must be enabled for all features (consolidated billing only is not enough).
  scope: per organization.
  link: [your organization must be enabled for all features](../facts/firewall-manager.md#firewall-manager-needs-org-all-features)
  link: [must be a member of the organization](../facts/firewall-manager.md#firewall-manager-needs-org-all-features)
firewall-manager-nfw-policy-management-models
  claim: Firewall Manager Network Firewall policies manage Network Firewall firewalls for VPCs across the organization with three firewall management models: distributed (a firewall and endpoints for each account and VPC that's within policy scope), centralized (Firewall Manager creates a single Network Firewall firewall in a single Amazon VPC), or import of existing firewalls.
  scope: Firewall Manager Network Firewall policies.
  link: [Firewall Manager creates and manages your firewalls](../facts/firewall-manager.md#firewall-manager-nfw-policy-management-models)
firewall-manager-nfw-rule-groups-must-exist
  claim: For a Firewall Manager Network Firewall policy, the Network Firewall rule groups must already exist in the Firewall Manager administrator account, and resource sharing with AWS Organizations must be enabled because the policy shares the rule groups across accounts.
  scope: Firewall Manager Network Firewall policies.
  link: [already exist in the Firewall Manager administrator account](../facts/firewall-manager.md#firewall-manager-nfw-rule-groups-must-exist)
  link: [shares Network Firewall rule groups across the accounts](../facts/firewall-manager.md#firewall-manager-nfw-rule-groups-must-exist)
firewall-manager-out-of-scope-keeps-protection
  claim: By default, if an account or resource goes out of policy scope, Firewall Manager does not automatically remove protections or delete Firewall Manager-managed resources, unless you select the option to automatically remove protections from resources that leave the policy scope.
  scope: per Firewall Manager policy; default; adjustable; the remove option is not available for Shield Advanced or AWS WAF Classic policies.
  link: [doesn't automatically remove protections](../facts/firewall-manager.md#firewall-manager-out-of-scope-keeps-protection)
  link: [protections from resources that leave the policy scope](../facts/firewall-manager.md#firewall-manager-out-of-scope-keeps-protection)
firewall-manager-policies-region-specific
  claim: Firewall Manager security policies are Region specific: each policy can include only resources in its AWS Region, so you create a policy for each Region where you operate.
  scope: per Firewall Manager policy.
  link: [security policies are region specific](../facts/firewall-manager.md#firewall-manager-policies-region-specific)
  link: [a new policy for each region](../facts/firewall-manager.md#firewall-manager-policies-region-specific)
firewall-manager-policy-fee
  claim: AWS Firewall Manager charges a monthly fee per protection policy per Region; the pricing example charges $100 per month for one policy.
  scope: per policy per Region; example for an organization not subscribed to Shield Advanced; some Regions charge more than $100 per policy; AWS Config rules and protected-service charges are extra.
  link: [$100 per month](../facts/firewall-manager.md#firewall-manager-policy-fee)
  say: one hundred dollars per month
firewall-manager-policy-types
  claim: A Firewall Manager policy is specific to one policy type (AWS WAF, Shield Advanced, security group, network ACL, Network Firewall, DNS Firewall or third-party firewall); to enforce several types you create several policies, and you can create more than one policy per type.
  scope: per Firewall Manager policy.
  link: [specific to the individual policy type](../facts/firewall-manager.md#firewall-manager-policy-types)
  link: [you can create multiple policies](../facts/firewall-manager.md#firewall-manager-policy-types)
firewall-manager-prereqs-faq-list
  claim: Firewall Manager has three mandatory prerequisites (AWS Organizations with all features, a Firewall Manager administrator account, and AWS Config enabled on member accounts) and one optional prerequisite (AWS Resource Access Manager sharing, for Network Firewall and DNS Firewall policies).
  scope: per organization.
  link: [three mandatory pre-requisites and one optional pre-requisite](../facts/firewall-manager.md#firewall-manager-prereqs-faq-list)
firewall-manager-primary-security-groups
  claim: A Firewall Manager security group policy can have up to 3 primary security groups by default; before May 5, 2023 the maximum was one.
  scope: per security group policy; default; adjustable.
  link: [3](../facts/firewall-manager.md#firewall-manager-primary-security-groups)
  link: [one](../facts/firewall-manager.md#firewall-manager-primary-security-groups)
  say: three security groups
  changed: 2023-05-05: was one
firewall-manager-protection-types
  claim: Firewall Manager simplifies administration across multiple accounts and resources for AWS WAF, AWS Shield Advanced, Amazon VPC security groups and network ACLs, AWS Network Firewall, and Amazon Route 53 Resolver DNS Firewall.
  scope: per organization.
  link: [Amazon VPC security groups and network ACLs](../facts/firewall-manager.md#firewall-manager-protection-types)
  link: [Amazon Route 53 Resolver DNS Firewall](../facts/firewall-manager.md#firewall-manager-protection-types)
firewall-manager-quota-accounts-in-scope
  claim: A Firewall Manager policy can have up to 2,500 accounts in scope by default when you do not explicitly include or exclude accounts, and up to 200 when you do.
  scope: per Firewall Manager policy; default; adjustable.
  link: [2,500](../facts/firewall-manager.md#firewall-manager-quota-accounts-in-scope)
  link: [200](../facts/firewall-manager.md#firewall-manager-quota-accounts-in-scope)
  say: twenty-five hundred accounts | two hundred accounts
firewall-manager-quota-ous-in-scope
  claim: A Firewall Manager policy can have up to 20 organizational units in scope by default.
  scope: per Firewall Manager policy; default; adjustable.
  link: [20](../facts/firewall-manager.md#firewall-manager-quota-ous-in-scope)
  say: twenty OUs
firewall-manager-quota-policies
  claim: An organization can have up to 50 Firewall Manager policies per Region by default (Global and US East (N. Virginia) count together); before May 5, 2023 the number was 20.
  scope: per organization per Region; default; adjustable.
  link: [50](../facts/firewall-manager.md#firewall-manager-quota-policies)
  link: [20](../facts/firewall-manager.md#firewall-manager-quota-policies)
  say: fifty policies | twenty policies
  changed: 2023-05-05: was 20
firewall-manager-ram-for-nfw-dns-policies
  claim: To manage Firewall Manager Network Firewall and DNS Firewall policies, you must enable sharing with AWS Organizations in AWS Resource Access Manager (AWS RAM).
  scope: Network Firewall and DNS Firewall policies.
  link: [must enable sharing with AWS Organizations](../facts/firewall-manager.md#firewall-manager-ram-for-nfw-dns-policies)
firewall-manager-requires-aws-config
  claim: To use Firewall Manager you must enable AWS Config, for each member account (including the administrator account) and each Region that has resources to protect; AWS Config charges apply.
  scope: per member account per Region.
  link: [you must enable AWS Config](../facts/firewall-manager.md#firewall-manager-requires-aws-config)
firewall-manager-rule-groups-per-waf-policy
  claim: A Firewall Manager AWS WAF policy can include up to 50 rule groups by default.
  scope: per AWS WAF policy; default; adjustable.
  link: [50](../facts/firewall-manager.md#firewall-manager-rule-groups-per-waf-policy)
  say: fifty rule groups
firewall-manager-scope-accounts-ous
  claim: You can apply a Firewall Manager policy to all accounts in the organization, to only a list of included accounts and OUs, or to all except a list of excluded accounts and OUs.
  scope: per Firewall Manager policy.
  link: [a specific list of included account numbers](../facts/firewall-manager.md#firewall-manager-scope-accounts-ous)
  link: [except a specific list of excluded account numbers](../facts/firewall-manager.md#firewall-manager-scope-accounts-ous)
firewall-manager-scope-resource-tags
  claim: Resource tags can also define Firewall Manager policy scope: you can include or exclude resources that have all of the tags in a list, or apply the policy only to resources that have any of the specified tags.
  scope: per Firewall Manager policy.
  link: [Resource tags can also be used](../facts/firewall-manager.md#firewall-manager-scope-resource-tags)
firewall-manager-sg-audit-start-without-remediation
  claim: For content or usage audit security group policies, AWS recommends starting with automatic remediation disabled, reviewing the policy details, and then enabling automatic remediation.
  scope: content and usage audit security group policies.
  link: [start with automatic remediation disabled](../facts/firewall-manager.md#firewall-manager-sg-audit-start-without-remediation)
firewall-manager-sg-policy-three-uses
  claim: Firewall Manager security group policies can apply common security groups to specified accounts and resources, audit security group rules to find and fix noncompliant rules, and audit security group usage to clean up unused and redundant security groups.
  scope: Firewall Manager security group policies.
  link: [common security groups to specified accounts and resources](../facts/firewall-manager.md#firewall-manager-sg-policy-three-uses)
  link: [Audit security group rules](../facts/firewall-manager.md#firewall-manager-sg-policy-three-uses)
  link: [clean up unused and redundant security groups](../facts/firewall-manager.md#firewall-manager-sg-policy-three-uses)
firewall-manager-shield-policy-empty-web-acl
  claim: When you apply a Firewall Manager Shield policy with auto remediation, Firewall Manager associates an empty AWS WAF web ACL, used for Shield monitoring, with each in-scope resource that has no web ACL; if you later associate another web ACL, Firewall Manager removes the empty one.
  scope: Firewall Manager Shield Advanced policies; auto remediation enabled.
  link: [associates an empty AWS WAF web ACL](../facts/firewall-manager.md#firewall-manager-shield-policy-empty-web-acl)
  link: [used for Shield monitoring purposes](../facts/firewall-manager.md#firewall-manager-shield-policy-empty-web-acl)
firewall-manager-subscribes-org-to-shield-advanced
  claim: Firewall Manager lets you subscribe all member accounts of an organization to AWS Shield Advanced, and automatically subscribes new in-scope accounts that join the organization.
  scope: per organization.
  link: [all member accounts in an AWS Organizations organization](../facts/firewall-manager.md#firewall-manager-subscribes-org-to-shield-advanced)
  link: [automatically subscribes new in-scope accounts](../facts/firewall-manager.md#firewall-manager-subscribes-org-to-shield-advanced)
firewall-manager-waf-policy-first-last-rule-groups
  claim: The Firewall Manager AWS WAF policy type takes sets of rule groups to run first and last in the web ACL, and in the accounts where the web ACL is applied, the account owner can add rules and rule groups that run in between.
  scope: Firewall Manager AWS WAF policies.
  link: [rule groups to run first and last](../facts/firewall-manager.md#firewall-manager-waf-policy-first-last-rule-groups)
  link: [rules and rule groups to run in between](../facts/firewall-manager.md#firewall-manager-waf-policy-first-last-rule-groups)
firewall-manager-waf-policy-global-for-cloudfront
  claim: When you create a Firewall Manager AWS WAF policy, you choose Global as the Region to protect CloudFront distributions; to protect resources in multiple Regions (other than CloudFront distributions), you must create a separate policy for each Region.
  scope: Firewall Manager AWS WAF policies.
  link: [To protect Amazon CloudFront distributions, choose **Global**.](../facts/firewall-manager.md#firewall-manager-waf-policy-global-for-cloudfront)
  link: [separate Firewall Manager policies for each Region](../facts/firewall-manager.md#firewall-manager-waf-policy-global-for-cloudfront)
firewall-manager-waf-policy-retrofit-existing
  claim: A Firewall Manager AWS WAF policy can create and manage new web ACLs for in-scope resources, replacing web ACLs already in use, or keep the web ACLs already associated with in-scope resources and retrofit them for use by the policy.
  scope: Firewall Manager AWS WAF policies.
  link: [replacing any web ACLs](../facts/firewall-manager.md#firewall-manager-waf-policy-retrofit-existing)
  link: [retrofit them for use by the policy](../facts/firewall-manager.md#firewall-manager-waf-policy-retrofit-existing)
firewall-manager-waf-policy-wcu
  claim: The rule groups in a Firewall Manager AWS WAF policy can use at most 5,000 WCUs in total; this quota can't be changed.
  scope: per AWS WAF policy; maximum; not adjustable.
  link: [5,000](../facts/firewall-manager.md#firewall-manager-waf-policy-wcu)
  say: five thousand W C Us
network-firewall-active-threat-defense
  claim: The active threat defense managed rule group gives advanced network threat protection with rules that AWS continuously updates from Amazon threat intelligence (including MadPot); after you add it to a policy, AWS updates its rules automatically.
  scope: AttackInfrastructure managed rule group.
  link: [updates these rules based on Amazon threat intelligence](../facts/network-firewall.md#network-firewall-active-threat-defense)
  link: [uses Amazon threat intelligence from MadPot](../facts/network-firewall.md#network-firewall-active-threat-defense)
network-firewall-active-threat-defense-capacity
  claim: Active threat defense managed rule groups use a fixed rule capacity of 15,000, while the default total limit stays at 30,000 stateful rules per firewall policy in a Region.
  scope: per firewall policy; fixed; not adjustable.
  link: [15,000](../facts/network-firewall.md#network-firewall-active-threat-defense-capacity)
  link: [30,000](../facts/network-firewall.md#network-firewall-active-threat-defense-capacity)
  say: fifteen thousand | thirty thousand
network-firewall-bandwidth-per-az
  claim: A firewall's endpoints in any single Availability Zone can carry at most 100 Gbps in total, shared by the firewall's own endpoints and its VPC endpoint associations; Network Firewall drops any traffic over the limit.
  scope: per firewall, per Availability Zone; maximum; not adjustable; the firewall scales automatically up to this limit; performance may be impacted if a single endpoint is oversubscribed (FAQ).
  link: [100 Gbps](../facts/network-firewall.md#network-firewall-bandwidth-per-az)
  say: one hundred gigabits per second
network-firewall-case-rapid7-ram-400-endpoints
  claim: Rapid7 built a global Network Firewall rule set and used AWS Resource Access Manager to deploy those rules across more than 400 firewall endpoints in a matter of seconds.
  scope: Rapid7 (case study).
  link: [used AWS RAM to efficiently deploy those rules](../facts/network-firewall.md#network-firewall-case-rapid7-ram-400-endpoints)
  link: [more than 400 firewall endpoints](../facts/network-firewall.md#network-firewall-case-rapid7-ram-400-endpoints)
network-firewall-case-rapid7-with-guardduty
  claim: Rapid7 gained instant visibility into its network traffic with AWS Network Firewall and uses it together with Amazon GuardDuty to better alert its development teams to network traffic issues.
  scope: Rapid7 (case study).
  link: [gained instant visibility into its network traffic](../facts/network-firewall.md#network-firewall-case-rapid7-with-guardduty)
  link: [Using the two services together](../facts/network-firewall.md#network-firewall-case-rapid7-with-guardduty)
network-firewall-change-active-threat-defense-2025
  claim: On June 17, 2025, Network Firewall added support for active threat defense AWS managed rule groups.
  scope: managed rule groups.
  link: [June 17, 2025](../facts/network-firewall.md#network-firewall-change-active-threat-defense-2025)
  say: June seventeenth, twenty twenty-five
network-firewall-change-geoip-2024
  claim: On August 28, 2024, Network Firewall stateful rules gained the Suricata geoip keyword, to filter on the country codes associated with IP addresses.
  scope: stateful rules.
  link: [August 28, 2024](../facts/network-firewall.md#network-firewall-change-geoip-2024)
  say: August twenty-eighth, twenty twenty-four
network-firewall-change-ipv6-subnets-2023
  claim: On January 17, 2023, Network Firewall subnets could be configured to use IPv4, IPv6 or dualstack IP addresses.
  scope: firewall subnets.
  link: [January 17, 2023](../facts/network-firewall.md#network-firewall-change-ipv6-subnets-2023)
  say: January seventeenth, twenty twenty-three
network-firewall-change-outbound-tls-all-regions-2023
  claim: On December 19, 2023, Network Firewall began to support inspection of outbound SSL/TLS traffic in all Regions where it is available.
  scope: all Network Firewall Regions.
  link: [December 19, 2023](../facts/network-firewall.md#network-firewall-change-outbound-tls-all-regions-2023)
  say: December nineteenth, twenty twenty-three
network-firewall-change-price-reduction-2026
  claim: On February 6, 2026, NAT gateway discounts were extended to NAT gateways service-chained with secondary firewall endpoints, and the extra Advanced Inspection data processing charge, which ranged from $0.001/GB to $0.009/GB in 13 Regions, was removed.
  scope: all Regions where Network Firewall is offered.
  link: [February 6, 2026](../facts/network-firewall.md#network-firewall-change-price-reduction-2026)
  link: [$0.001/GB to $0.009/GB](../facts/network-firewall.md#network-firewall-change-price-reduction-2026)
  say: February sixth, twenty twenty-six | a tenth of a cent to almost a cent per gigabyte
  changed: 2026-02-06: was $0.001/GB to $0.009/GB
network-firewall-change-privatelink-2024
  claim: On September 12, 2024, Network Firewall added interface endpoints through AWS PrivateLink, giving a private connection between a VPC and the Network Firewall service without internet access.
  scope: per VPC.
  link: [September 12, 2024](../facts/network-firewall.md#network-firewall-change-privatelink-2024)
  say: September twelfth, twenty twenty-four
network-firewall-change-proxy-mode-preview-2026
  claim: On August 3, 2026, Network Firewall added a no-source-preservation (proxy) mode in public preview, only in US East (Ohio), in which the firewall acts as an explicit forward proxy behind an attached NAT gateway.
  scope: US East (Ohio) only.
  link: [August 3, 2026](../facts/network-firewall.md#network-firewall-change-proxy-mode-preview-2026)
  link: [public preview](../facts/network-firewall.md#network-firewall-change-proxy-mode-preview-2026)
  say: August third, twenty twenty-six
network-firewall-change-reject-action-2023
  claim: On January 9, 2023, Network Firewall added the stateful rule action reject, in addition to pass, drop and alert.
  scope: stateful rules.
  link: [January 9, 2023](../facts/network-firewall.md#network-firewall-change-reject-action-2023)
  link: [reject](../facts/network-firewall.md#network-firewall-change-reject-action-2023)
  say: January ninth, twenty twenty-three
network-firewall-change-stateful-rules-adjustable-2024
  claim: On May 22, 2024, the Network Firewall quota for stateful rules per firewall policy became adjustable.
  scope: per firewall policy.
  link: [May 22, 2024](../facts/network-firewall.md#network-firewall-change-stateful-rules-adjustable-2024)
  say: May twenty-second, twenty twenty-four
network-firewall-change-tgw-attached-2025
  claim: AWS Network Firewall supports native integration with AWS Transit Gateway: a firewall owner can attach a Network Firewall directly to a transit gateway as a transit gateway attachment, with no additional charges beyond standard Network Firewall and Transit Gateway pricing; the What's New post of Jun 16, 2025 announced it in 5 AWS Regions.
  scope: per transit gateway attachment; Region availability at launch was 5 AWS Regions; no saved page gives today's Region list.
  link: [Jun 16, 2025](../facts/network-firewall.md#network-firewall-change-tgw-attached-2025)
  link: [directly to a transit gateway](../facts/network-firewall.md#network-firewall-change-tgw-attached-2025)
  say: June sixteenth, twenty twenty-five
network-firewall-change-tls-inspection-2023
  claim: On March 30, 2023, Network Firewall added TLS inspection configurations, which decrypt and re-encrypt SSL/TLS traffic going through the firewall.
  scope: per firewall policy.
  link: [March 30, 2023](../facts/network-firewall.md#network-firewall-change-tls-inspection-2023)
  say: March thirtieth, twenty twenty-three
network-firewall-change-url-category-filtering-2026
  claim: On January 16, 2026, Network Firewall stateful rules gained the aws_url_category and aws_domain_category keywords, to filter traffic by web content category.
  scope: stateful rules.
  link: [January 16, 2026](../facts/network-firewall.md#network-firewall-change-url-category-filtering-2026)
  say: January sixteenth, twenty twenty-six
network-firewall-change-vpce-associations-2025
  claim: On May 28, 2025, Network Firewall added VPC endpoint associations, which deploy one firewall across multiple VPCs and allow multiple firewall endpoints in one Availability Zone, with a fixed quota of 50 per firewall per Availability Zone.
  scope: per firewall, per Availability Zone.
  link: [May 28, 2025](../facts/network-firewall.md#network-firewall-change-vpce-associations-2025)
  link: [50](../facts/network-firewall.md#network-firewall-change-vpce-associations-2025)
  say: May twenty-eighth, twenty twenty-five | fifty per Availability Zone
network-firewall-combine-transit-gateway
  claim: You can combine Network Firewall with services and components used with your VPC, such as an internet gateway, a NAT gateway, a VPN or a transit gateway; you need a VPC to use Network Firewall.
  scope: per VPC.
  link: [a VPN, or a transit gateway](../facts/network-firewall.md#network-firewall-combine-transit-gateway)
  link: [You need a VPC to use Network Firewall.](../facts/network-firewall.md#network-firewall-combine-transit-gateway)
network-firewall-complements-sg-waf-marketplace
  claim: Network Firewall complements existing AWS network and application security services by giving control and visibility of Layer 3-7 traffic for the whole VPC, and you may use it alongside security groups, AWS WAF rules or AWS Marketplace appliances.
  scope: AWS Network Firewall.
  link: [control and visibility to Layer 3-7 network traffic for your entire VPC](../facts/network-firewall.md#network-firewall-complements-sg-waf-marketplace)
  link: [along your existing security controls](../facts/network-firewall.md#network-firewall-complements-sg-waf-marketplace)
network-firewall-deep-packet-inspection-payload
  claim: Depending on the Suricata compatible rules you provide, the stateful engine might perform deep packet inspection, which works on the payload data within packets rather than on header information.
  scope: stateful rules engine.
  link: [works on the payload data within your packets](../facts/network-firewall.md#network-firewall-deep-packet-inspection-payload)
network-firewall-default-source-preservation
  claim: By default, Network Firewall operates in source-preservation mode: it receives traffic from the VPC endpoint, inspects it with the stateful engine and sends it back through the endpoint, preserving the original source and destination IP addresses; traffic is steered to the firewall through VPC route tables.
  scope: per firewall; default; not adjustable; no-source-preservation mode is in preview only.
  link: [operates in **source-preservation mode**](../facts/network-firewall.md#network-firewall-default-source-preservation)
  link: [source and destination IP addresses are preserved](../facts/network-firewall.md#network-firewall-default-source-preservation)
  link: [steered to the firewall through VPC route tables](../facts/network-firewall.md#network-firewall-default-source-preservation)
network-firewall-default-stateless-action-fragments
  claim: If a packet matches no stateless rule, Network Firewall performs the firewall policy's default stateless action for full packets or UDP fragments; it applies the fragment action only to UDP packet fragments and silently drops fragments of other protocols.
  scope: per firewall policy.
  link: [performs the firewall policy's default stateless rule action](../facts/network-firewall.md#network-firewall-default-stateless-action-fragments)
  link: [silently drops packet fragments for other protocols](../facts/network-firewall.md#network-firewall-default-stateless-action-fragments)
network-firewall-definition
  claim: AWS Network Firewall is a stateful, managed network firewall and intrusion detection and prevention service for your VPC.
  scope: per VPC.
  link: [a stateful, managed, network firewall](../facts/network-firewall.md#network-firewall-definition)
  link: [intrusion detection and prevention service](../facts/network-firewall.md#network-firewall-definition)
network-firewall-domain-allow-denies-others
  claim: With the Allow action in a domain list rule group, the firewall denies traffic of the specified protocol type that does not match the domains; this denial applies only when the firewall policy uses default action order, not strict order.
  scope: domain list rule groups; default action order.
  link: [when the firewall policy uses default action order](../facts/network-firewall.md#network-firewall-domain-allow-denies-others)
  link: [Under strict order, this denial does not apply.](../facts/network-firewall.md#network-firewall-domain-allow-denies-others)
network-firewall-domain-allow-deny-lists
  claim: Network Firewall supports domain name stateful inspection: you can create allow lists and deny lists of domain names that the stateful rules engine looks for in network traffic.
  scope: domain list rule groups.
  link: [allow lists and deny lists with domain names](../facts/network-firewall.md#network-firewall-domain-allow-deny-lists)
network-firewall-domain-capacity-per-policy
  claim: A firewall policy can consume at most 10,000,000 domain name specifications across all AWS Marketplace managed domain rule groups it uses.
  scope: per firewall policy; maximum; not adjustable.
  link: [10,000,000](../facts/network-firewall.md#network-firewall-domain-capacity-per-policy)
  say: ten million domain specifications
network-firewall-domain-home-net-other-vpcs
  claim: By default, domain list inspection uses a HOME_NET set to the CIDR range of the VPC where Network Firewall is deployed, so only traffic from that range is filtered; to filter traffic from other VPCs (for example through a transit gateway), you must set HOME_NET to include their CIDR ranges.
  scope: domain list rule groups; default; adjustable; centralized inspection VPC.
  link: [Only traffic from that range is passed through](../facts/network-firewall.md#network-firewall-domain-home-net-other-vpcs)
  link: [you must manually set the `HOME_NET` variable](../facts/network-firewall.md#network-firewall-domain-home-net-other-vpcs)
network-firewall-domain-sni-host-header
  claim: For HTTPS traffic, Network Firewall uses the Server Name Indication (SNI) in the TLS handshake to find the domain name, and for HTTP it uses the Host header; it does not do out-of-band DNS lookups and uses the SNI or Host header, not IP addresses, for domain list rules.
  scope: domain list rule groups.
  link: [Server Name Indication (SNI) extension](../facts/network-firewall.md#network-firewall-domain-sni-host-header)
  link: [uses the HTTP host header](../facts/network-firewall.md#network-firewall-domain-sni-host-header)
  link: [doesn't pause connections to do out-of-band DNS lookups](../facts/network-firewall.md#network-firewall-domain-sni-host-header)
network-firewall-endpoint-not-own-subnet
  claim: A firewall endpoint can protect any subnet in your VPC except the one in which it is located, so firewall subnets should be reserved for Network Firewall only, with no other applications in them.
  scope: per firewall endpoint.
  link: [except for the one in which it's located](../facts/network-firewall.md#network-firewall-endpoint-not-own-subnet)
  link: [for the exclusive use of Network Firewall](../facts/network-firewall.md#network-firewall-endpoint-not-own-subnet)
network-firewall-endpoints-per-az
  claim: You install firewall endpoints per Availability Zone: for each Availability Zone where you want to use the firewall, you choose a subnet to host the primary firewall endpoint, and you can add VPC endpoint associations for more endpoints.
  scope: per Availability Zone.
  link: [on a per-Availability Zone basis](../facts/network-firewall.md#network-firewall-endpoints-per-az)
  link: [a subnet to host the primary firewall endpoint](../facts/network-firewall.md#network-firewall-endpoints-per-az)
network-firewall-faq-acm-cipher-suites
  claim: AWS Network Firewall supports all cipher suites that AWS Certificate Manager (ACM) supports.
  scope: TLS inspection.
  link: [all cipher suites supported by AWS Certificate Manager](../facts/network-firewall.md#network-firewall-faq-acm-cipher-suites)
network-firewall-faq-centralized-or-distributed
  claim: AWS Network Firewall supports two primary deployment types: distributed, inside each VPC, and centralized, as a VPC attachment to AWS Transit Gateway.
  scope: Network Firewall deployment models.
  link: [centralized and distributed](../facts/network-firewall.md#network-firewall-faq-centralized-or-distributed)
network-firewall-faq-dedicated-subnet-28
  claim: The AWS Network Firewall endpoint must be deployed in a dedicated subnet within your VPC, with a minimum size of /28.
  scope: per firewall endpoint subnet; minimum.
  link: [a dedicated subnet](../facts/network-firewall.md#network-firewall-faq-dedicated-subnet-28)
  link: [a minimum size of /28](../facts/network-firewall.md#network-firewall-faq-dedicated-subnet-28)
network-firewall-faq-import-open-source-rules
  claim: You can import AWS Network Firewall rules you have already written in common open source rule formats, or compatible rules from AWS partners.
  scope: stateful rule groups.
  link: [common open source rule formats](../facts/network-firewall.md#network-firewall-faq-import-open-source-rules)
network-firewall-faq-inspects-encrypted-traffic
  claim: AWS Network Firewall supports deep packet inspection for encrypted traffic.
  scope: TLS inspection.
  link: [deep packet inspection for encrypted traffic](../facts/network-firewall.md#network-firewall-faq-inspects-encrypted-traffic)
network-firewall-faq-inspects-routed-traffic
  claim: AWS Network Firewall inspects all traffic that is routed to its endpoint; routing is the mechanism for path insertion and filtering.
  scope: per firewall endpoint.
  link: [all traffic that is routed to the endpoint](../facts/network-firewall.md#network-firewall-faq-inspects-routed-traffic)
network-firewall-faq-ips-and-web-filtering
  claim: AWS Network Firewall offers an intrusion prevention system (IPS) with signature-based detection of vulnerability exploits, and web filtering that can stop traffic to known-bad URLs and monitor fully qualified domain names.
  scope: AWS Network Firewall.
  link: [signature-based detection](../facts/network-firewall.md#network-firewall-faq-ips-and-web-filtering)
  link: [stop traffic to known-bad URLs](../facts/network-firewall.md#network-firewall-faq-ips-and-web-filtering)
network-firewall-faq-managed-vpc-protection
  claim: AWS Network Firewall is a managed service for deploying network protections for your Amazon VPCs; it scales automatically with your network traffic so you do not deploy or manage infrastructure.
  scope: per VPC.
  link: [scales automatically with your network traffic](../facts/network-firewall.md#network-firewall-faq-managed-vpc-protection)
network-firewall-faq-outbound-control-types
  claim: AWS Network Firewall supports these types of outbound traffic control: HTTPS (SNI)/HTTP protocol URL filtering, access control lists (ACLs), DNS query, and protocol detection.
  scope: outbound traffic.
  link: [HTTPS (SNI)/HTTP protocol URL filtering](../facts/network-firewall.md#network-firewall-faq-outbound-control-types)
network-firewall-faq-owner-billed-for-endpoints
  claim: Only the firewall owner is billed for all associated primary and secondary endpoints, including cross-account endpoint associations.
  scope: firewall owner account.
  link: [Only the firewall owner is billed](../facts/network-firewall.md#network-firewall-faq-owner-billed-for-endpoints)
network-firewall-faq-pricing-dimensions
  claim: AWS Network Firewall pricing is based on the number of firewalls deployed and the amount of traffic inspected.
  scope: AWS Network Firewall pricing.
  link: [the amount of traffic inspected](../facts/network-firewall.md#network-firewall-faq-pricing-dimensions)
network-firewall-faq-regional-use-fms-multi-account
  claim: AWS Network Firewall is a regional service; for maintaining policy and governance across multiple accounts you may use AWS Firewall Manager.
  scope: per Region.
  link: [is a regional service](../facts/network-firewall.md#network-firewall-faq-regional-use-fms-multi-account)
network-firewall-faq-rule-match-types
  claim: AWS Network Firewall supports thousands of rules, which can be based on domain, port, protocol, IP addresses and pattern matching.
  scope: per firewall policy.
  link: [domain, port, protocol, IP addresses, and pattern matching](../facts/network-firewall.md#network-firewall-faq-rule-match-types)
network-firewall-faq-sla-99-99
  claim: AWS Network Firewall offers a Service Level Agreement with an uptime commitment of 99.99%.
  scope: per AWS Network Firewall SLA; fixed.
  link: [99.99%](../facts/network-firewall.md#network-firewall-faq-sla-99-99)
network-firewall-faq-stateless-vs-stateful
  claim: AWS Network Firewall stateless rules are network ACLs based on source and destination IP addresses, ports or protocols; stateful rules use the same fields but maintain and secure connections or sessions throughout their life.
  scope: stateless and stateful rules.
  link: [maintain and secure connections or sessions](../facts/network-firewall.md#network-firewall-faq-stateless-vs-stateful)
network-firewall-faq-tgw-native-or-manual
  claim: You can use AWS Network Firewall with a Transit Gateway either through the native integration capability or by deploying the firewall in a VPC and attaching that VPC to the transit gateway manually.
  scope: transit gateway deployments.
  link: [the native integration capability](../facts/network-firewall.md#network-firewall-faq-tgw-native-or-manual)
network-firewall-faq-tls-versions
  claim: For TLS inspection, AWS Network Firewall supports TLS versions 1.1, 1.2 and 1.3, except encrypted client hello (ECH) and encrypted SNI (ESNI).
  scope: TLS inspection.
  link: [TLS version 1.1, 1.2, and 1.3](../facts/network-firewall.md#network-firewall-faq-tls-versions)
network-firewall-filters-vpc-perimeter
  claim: With Network Firewall you can filter traffic at the perimeter of your VPC, including traffic to and from an internet gateway, a NAT gateway, or over VPN or Direct Connect.
  scope: per VPC.
  link: [filter traffic at the perimeter of your VPC](../facts/network-firewall.md#network-firewall-filters-vpc-perimeter)
  link: [NAT gateway, or over VPN or Direct Connect](../facts/network-firewall.md#network-firewall-filters-vpc-perimeter)
network-firewall-geoip-filter
  claim: Geographic IP filtering in Network Firewall matches country codes for the IP addresses of network traffic, for source, destination or both, and works with Suricata compatible rule strings and standard stateful rule groups; it supports IPv4 and IPv6.
  scope: stateful rule groups.
  link: [matches country codes for the IP addresses](../facts/network-firewall.md#network-firewall-geoip-filter)
  link: [provides support for IPv6 and IPv4](../facts/network-firewall.md#network-firewall-geoip-filter)
network-firewall-inactive-owner-fail-closed
  claim: When a firewall owner's account becomes inactive, the firewall enters a FAIL_CLOSED state and drops all traffic through its primary endpoints and VPC endpoint associations.
  scope: per firewall; firewall owner's account inactive.
  link: [The firewall enters a `FAIL_CLOSED` state](../facts/network-firewall.md#network-firewall-inactive-owner-fail-closed)
  link: [dropping all traffic through both primary endpoints](../facts/network-firewall.md#network-firewall-inactive-owner-fail-closed)
network-firewall-ip-set-references
  claim: A Suricata compatible stateful rule group can have at most 5 IP set references.
  scope: per stateful rule group; maximum; not adjustable.
  link: [5](../facts/network-firewall.md#network-firewall-ip-set-references)
  say: five IP set references
network-firewall-kms-key-stops-traffic
  claim: If the AWS KMS key used by the firewall owner is revoked, disabled or deleted, the firewall cannot process traffic until the key is restored to an active state.
  scope: the AWS KMS key used by the firewall owner.
  link: [AWS KMS key is revoked, disabled, or deleted](../facts/network-firewall.md#network-firewall-kms-key-stops-traffic)
network-firewall-log-destinations
  claim: AWS Network Firewall logs can be natively stored in Amazon S3, Amazon Data Firehose (formerly Amazon Kinesis Data Firehose) and Amazon CloudWatch, and you can use the same or a different logging destination for each log type.
  scope: per firewall.
  link: [the same or different logging destination](../facts/network-firewall.md#network-firewall-log-destinations)
network-firewall-log-types
  claim: Network Firewall can record flow logs, alert logs (traffic matching stateful rules with an alert-sending action: DROP, ALERT and REJECT) and TLS logs (TLS inspection events) from its stateful engine; logging is available only for traffic forwarded to the stateful engine.
  scope: per firewall; logging configured.
  link: [Flow logs are standard network traffic flow logs.](../facts/network-firewall.md#network-firewall-log-types)
  link: [only available for traffic that you forward](../facts/network-firewall.md#network-firewall-log-types)
network-firewall-managed-rule-groups-mostly-free
  claim: Network Firewall managed rule groups are predefined rules that AWS writes and maintains; most AWS managed rule groups are available at no additional cost, and they come as active threat defense, domain and IP, and threat signature rule groups.
  scope: Network Firewall managed rule groups.
  link: [available for at no additional cost](../facts/network-firewall.md#network-firewall-managed-rule-groups-mostly-free)
  link: [predefined, ready-to-use rules that AWS writes and maintains](../facts/network-firewall.md#network-firewall-managed-rule-groups-mostly-free)
network-firewall-nat-gateway-charges-waived
  claim: If a NAT gateway is placed next to Network Firewall in a service chain in the same account, the standard NAT gateway per-hour and data processing charges are waived, one-to-one with Network Firewall usage.
  scope: per NAT gateway in the same Region and networking path; the NAT gateway and the firewall must be in the same Region and the same networking path.
  link: [charges are waived](../facts/network-firewall.md#network-firewall-nat-gateway-charges-waived)
network-firewall-no-asymmetric-routing
  claim: Network Firewall does not support asymmetric routing: request traffic and its response must be routed to the same Network Firewall endpoint in both directions for the firewall to process traffic properly.
  scope: per traffic flow.
  link: [Network Firewall doesn’t support asymmetric routing.](../facts/network-firewall.md#network-firewall-no-asymmetric-routing)
  link: [the Network Firewall endpoint in both directions](../facts/network-firewall.md#network-firewall-no-asymmetric-routing)
network-firewall-no-share-tls-policy
  claim: TLS inspection is not supported for Network Firewall firewalls with VPC endpoint associations: a firewall policy that has TLS inspection enabled cannot be added to a firewall that has VPC endpoint associations, and a VPC endpoint association cannot be created from a firewall whose firewall policy has TLS inspection enabled.
  scope: TLS inspection with VPC endpoint associations.
  link: [not supported for firewalls with VPC endpoint associations](../facts/network-firewall.md#network-firewall-no-share-tls-policy)
network-firewall-not-for-ddos
  claim: Network Firewall is designed to protect and control access to and from your VPC, not to mitigate volumetric attacks like DDoS; for DDoS protection AWS recommends the AWS Best Practices for DDoS Resiliency and AWS Shield Advanced.
  scope: AWS Network Firewall.
  link: [but not to mitigate volumetric attacks](../facts/network-firewall.md#network-firewall-not-for-ddos)
  link: [explore AWS Shield Advanced](../facts/network-firewall.md#network-firewall-not-for-ddos)
network-firewall-one-policy-per-firewall
  claim: Each firewall requires exactly 1 firewall policy, and one firewall policy can be used by up to 1,000 firewalls.
  scope: per firewall; fixed; not adjustable.
  link: [1](../facts/network-firewall.md#network-firewall-one-policy-per-firewall)
  link: [1,000](../facts/network-firewall.md#network-firewall-one-policy-per-firewall)
  say: one policy | one thousand firewalls
network-firewall-own-and-managed-rule-groups
  claim: A Network Firewall rule group is a reusable set of criteria for inspecting and handling traffic; you can use your own rule groups and rule groups managed for you by AWS, and rule groups are either stateless or stateful.
  scope: Network Firewall rule groups.
  link: [managed for you by AWS](../facts/network-firewall.md#network-firewall-own-and-managed-rule-groups)
  link: [either *stateless* or *stateful*](../facts/network-firewall.md#network-firewall-own-and-managed-rule-groups)
network-firewall-price-data-processing
  claim: Network Firewall also charges for traffic processed by the firewall endpoint, per GB per Region and Availability Zone, regardless of the traffic's source or destination; in US East (N. Virginia) it is $0.065 for 1 GB of data processed.
  scope: per GB processed, per Availability Zone; example rate for US East (N. Virginia); charged regardless of the traffic's source or destination.
  link: [$0.065](../facts/network-firewall.md#network-firewall-price-data-processing)
  say: six and a half cents
network-firewall-price-endpoint-hour
  claim: Network Firewall charges an hourly rate for each firewall endpoint per Region and Availability Zone; in the US East (N. Virginia) example it is $0.395 for each hour the endpoint is provisioned.
  scope: per firewall endpoint, per Availability Zone; example rate for US East (N. Virginia); each Availability Zone with an endpoint is charged.
  link: [$0.395](../facts/network-firewall.md#network-firewall-price-endpoint-hour)
  say: about forty cents
network-firewall-quota-firewall-policies
  claim: An account can have up to 20 Network Firewall firewall policies per Region by default.
  scope: per account per Region; default; adjustable.
  link: [20](../facts/network-firewall.md#network-firewall-quota-firewall-policies)
  say: twenty firewall policies
network-firewall-quota-firewalls
  claim: An account can have up to 5 Network Firewall firewalls per Region by default; you can request an increase.
  scope: per account per Region; default; adjustable.
  link: [5](../facts/network-firewall.md#network-firewall-quota-firewalls)
  say: five firewalls
network-firewall-quota-rule-groups-per-account
  claim: An account can have up to 50 stateful rule groups and up to 50 stateless rule groups per Region by default.
  scope: per account per Region, per rule group type; default; adjustable.
  link: [50](../facts/network-firewall.md#network-firewall-quota-rule-groups-per-account)
  say: fifty rule groups of each type
network-firewall-quota-stateful-rules-per-policy
  claim: A firewall policy can use up to 30,000 stateful rules in total across all the rule groups it references, by default; since May 22, 2024 this quota is adjustable.
  scope: per firewall policy, per account per Region; default; adjustable.
  link: [30,000](../facts/network-firewall.md#network-firewall-quota-stateful-rules-per-policy)
  say: thirty thousand stateful rules
network-firewall-quota-vpce-associations-per-account
  claim: An account can have up to 300 VPC endpoint associations per Region by default.
  scope: per account per Region; default; adjustable.
  link: [300](../facts/network-firewall.md#network-firewall-quota-vpce-associations-per-account)
  say: three hundred associations
network-firewall-reject-tcp-reset
  claim: The Reject action drops matching traffic and sends a TCP reset packet back to the sender; Reject is available only for TCP traffic.
  scope: stateful rules.
  link: [A TCP reset packet](../facts/network-firewall.md#network-firewall-reject-tcp-reset)
  link: [`Reject` is available only for TCP traffic.](../facts/network-firewall.md#network-firewall-reject-tcp-reset)
network-firewall-route-igw-both-directions
  claim: To filter all traffic between an internet gateway and customer subnets, you redirect incoming traffic from the internet gateway and outgoing traffic from the customer subnets through the firewall endpoint.
  scope: per VPC.
  link: [incoming traffic from the internet gateway](../facts/network-firewall.md#network-firewall-route-igw-both-directions)
  link: [outgoing traffic from the customer subnets](../facts/network-firewall.md#network-firewall-route-igw-both-directions)
network-firewall-route-tables-enable-protection
  claim: The firewall protects subnets in your VPC by filtering traffic between them and locations outside the VPC, and to enable its protection you modify the VPC route tables to send traffic through the Network Firewall firewall endpoints.
  scope: per VPC.
  link: [you modify your Amazon VPC route tables](../facts/network-firewall.md#network-firewall-route-tables-enable-protection)
  link: [through the Network Firewall firewall endpoints](../facts/network-firewall.md#network-firewall-route-tables-enable-protection)
network-firewall-rule-groups-per-policy
  claim: A firewall policy can reference at most 20 stateful rule groups and at most 20 stateless rule groups; these quotas can't be changed.
  scope: per firewall policy, per rule group type; maximum; not adjustable.
  link: [20](../facts/network-firewall.md#network-firewall-rule-groups-per-policy)
  say: twenty rule groups of each type
network-firewall-rule-order-set-at-create
  claim: You can configure the stateful RuleOrder setting of a firewall policy only when you first create the policy; it cannot be edited later.
  scope: per firewall policy.
  link: [only configure RuleOrder settings when you first create](../facts/network-firewall.md#network-firewall-rule-order-set-at-create)
  link: [RuleOrder can't be edited later.](../facts/network-firewall.md#network-firewall-rule-order-set-at-create)
network-firewall-secondary-endpoint-rate
  claim: When one firewall is associated with multiple VPCs, the primary endpoint pays the standard hourly rate and each secondary endpoint pays a separate, reduced hourly rate per Region and Availability Zone; only the firewall owner is billed.
  scope: per secondary endpoint, per Availability Zone.
  link: [separate, reduced hourly rate](../facts/network-firewall.md#network-firewall-secondary-endpoint-rate)
network-firewall-share-via-ram
  claim: You can share Network Firewall firewalls, firewall policies, rule groups and container associations with other AWS accounts; a shared firewall lets other accounts use its protections in their VPCs through VPC endpoint associations, and shared policies or rule groups can be used in their own firewalls.
  scope: Network Firewall resources; resource owned by the sharing account.
  link: [share Network Firewall firewalls, firewall policies, rule groups](../facts/network-firewall.md#network-firewall-share-via-ram)
  link: [through VPC endpoint associations](../facts/network-firewall.md#network-firewall-share-via-ram)
network-firewall-stateful-actions
  claim: Network Firewall supports the Suricata rule actions pass, drop, reject and alert for stateful rules; by default the engine processes rules in the order pass, drop, reject, then alert, and within each action you can set a priority.
  scope: stateful rules; default; default action order.
  link: [pass, drop, reject, and alert](../facts/network-firewall.md#network-firewall-stateful-actions)
  link: [and then finally alert action](../facts/network-firewall.md#network-firewall-stateful-actions)
network-firewall-stateful-alerts-need-logging
  claim: A stateful rule can pass a packet with or without an alert, or drop it and send an alert; alerts require logging to be configured for the firewall.
  scope: stateful rules.
  link: [with or without an alert](../facts/network-firewall.md#network-firewall-stateful-alerts-need-logging)
  link: [Alerts require logging to be configured](../facts/network-firewall.md#network-firewall-stateful-alerts-need-logging)
network-firewall-stateful-like-sg-default-pass
  claim: Network Firewall stateful rules are similar in behavior and use to VPC security groups, but by default the stateful rules engine allows traffic to pass, while the security group default is to deny traffic.
  scope: stateful rules engine; default; adjustable; default action order; strict order has its own default actions.
  link: [similar in behavior and use](../facts/network-firewall.md#network-firewall-stateful-like-sg-default-pass)
  link: [the stateful rules engine allows traffic to pass](../facts/network-firewall.md#network-firewall-stateful-like-sg-default-pass)
network-firewall-stateful-logging-extra-cost
  claim: Stateful rules can send alerts to the firewall's logs if logging is configured; to see the alerts you must enable logging for the firewall, and logging incurs additional costs.
  scope: per firewall.
  link: [you must enable logging for the firewalls](../facts/network-firewall.md#network-firewall-stateful-logging-extra-cost)
  link: [Logging incurs additional costs.](../facts/network-firewall.md#network-firewall-stateful-logging-extra-cost)
network-firewall-stateful-rule-group-categories
  claim: Network Firewall uses a Suricata rules engine to process all stateful rules; stateful rule groups come as standard stateful rules, domain lists, or Suricata compatible rule strings, and you can write any stateful rule in Suricata compatible format.
  scope: stateful rule groups.
  link: [your stateful rules in Suricata compatible format](../facts/network-firewall.md#network-firewall-stateful-rule-group-categories)
  link: [you can use an easy entry form](../facts/network-firewall.md#network-firewall-stateful-rule-group-categories)
network-firewall-stateless-actions
  claim: Each stateless rule must specify one of three actions: Pass, Drop, or Forward to stateful rules (discontinue stateless inspection and send the packet to the stateful engine); you can also add a named custom action that publishes CloudWatch metrics.
  scope: stateless rules and default stateless actions.
  link: [required to specify one of the following options](../facts/network-firewall.md#network-firewall-stateless-actions)
  link: [forward it to your stateful rules](../facts/network-firewall.md#network-firewall-stateless-actions)
network-firewall-stateless-like-nacl
  claim: The stateless rules engine inspects each packet in isolation, without regard to traffic direction or connection state, processes rules in priority order and stops at the first match; Network Firewall stateless rules are similar in behavior and use to VPC network ACLs.
  scope: stateless rules engine.
  link: [Amazon VPC network access control lists (ACLs)](../facts/network-firewall.md#network-firewall-stateless-like-nacl)
network-firewall-stateless-then-stateful
  claim: Network Firewall evaluates a packet against the stateless rule groups first; the stateless engine might drop the packet, pass it to its destination, or forward it to the stateful rules engine, which inspects packets in the context of their traffic flow and drops or passes them.
  scope: per firewall policy.
  link: [the policy's stateless rule groups first](../facts/network-firewall.md#network-firewall-stateless-then-stateful)
  link: [forward it to the stateful rules engine](../facts/network-firewall.md#network-firewall-stateless-then-stateful)
network-firewall-strict-default-actions
  claim: Stateful default actions apply when you use strict ordering; with strict order you can choose default actions such as Drop all or Drop established, and Drop established is the option to choose when you use your own domain list rule groups under strict order.
  scope: strict-order firewall policies.
  link: [These settings apply when you use strict ordering](../facts/network-firewall.md#network-firewall-strict-default-actions)
  link: [for your own domain list rule groups](../facts/network-firewall.md#network-firewall-strict-default-actions)
network-firewall-strict-order-recommended
  claim: Suricata can evaluate stateful rule groups with the default (action order) method or with strict ordering; AWS recommends strict order because it lets you specify the exact evaluation order, in which rule groups run by priority from the lowest number and rules run in the order defined.
  scope: per firewall policy.
  link: [We recommend that you use strict order](../facts/network-firewall.md#network-firewall-strict-order-recommended)
  link: [specify the exact order](../facts/network-firewall.md#network-firewall-strict-order-recommended)
  link: [starting from the lowest number](../facts/network-firewall.md#network-firewall-strict-order-recommended)
network-firewall-subnet-per-az-required
  claim: When you associate a firewall with a VPC, you must provide a subnet for each Availability Zone where you want a firewall endpoint; a common configuration is an endpoint in each zone that has customer subnets to protect.
  scope: per firewall.
  link: [must provide a subnet for each Availability Zone](../facts/network-firewall.md#network-firewall-subnet-per-az-required)
  link: [a firewall endpoint in each zone](../facts/network-firewall.md#network-firewall-subnet-per-az-required)
network-firewall-supported-by-firewall-manager
  claim: Network Firewall is supported by AWS Firewall Manager, which you can use to centrally configure and manage firewalls across accounts in AWS Organizations from a single account.
  scope: AWS Organizations.
  link: [Network Firewall is supported by AWS Firewall Manager.](../facts/network-firewall.md#network-firewall-supported-by-firewall-manager)
  link: [using a single account in Firewall Manager](../facts/network-firewall.md#network-firewall-supported-by-firewall-manager)
network-firewall-suricata-ips
  claim: Network Firewall uses the open source intrusion prevention system Suricata for stateful inspection and supports Suricata compatible rules.
  scope: stateful rules engine.
  link: [supports Suricata compatible rules](../facts/network-firewall.md#network-firewall-suricata-ips)
network-firewall-tgw-appliance-mode
  claim: In a centralized deployment with a transit gateway, you use Transit Gateway appliance mode on the inspection VPC so that request and response flows stay on the same Network Firewall endpoint.
  scope: centralized deployment model.
  link: [use the Transit Gateway appliance mode](../facts/network-firewall.md#network-firewall-tgw-appliance-mode)
network-firewall-tgw-appliance-mode-always
  claim: Appliance mode is always enabled on transit gateway-attached firewalls, and their traffic is routed through transit gateway route tables, not VPC route tables.
  scope: transit gateway-attached firewalls.
  link: [Appliance mode is always enabled](../facts/network-firewall.md#network-firewall-tgw-appliance-mode-always)
  link: [transit gateway route tables, not VPC route tables](../facts/network-firewall.md#network-firewall-tgw-appliance-mode-always)
network-firewall-tls-config-per-policy
  claim: A firewall policy can have at most 1 TLS inspection configuration, and a TLS inspection configuration at most 1 CA certificate for outbound inspection and at most 10 server certificates for inbound inspection.
  scope: per firewall policy; per TLS inspection configuration; maximum; not adjustable.
  link: [1](../facts/network-firewall.md#network-firewall-tls-config-per-policy)
  link: [10](../facts/network-firewall.md#network-firewall-tls-config-per-policy)
  say: one TLS inspection configuration | ten server certificates
network-firewall-tls-drops-non-tls-in-scope
  claim: Network Firewall drops non-TLS traffic that matches the TLS inspection scope, and drops TLS traffic whose client hello has no server name or whose SNI does not match the downstream server certificate.
  scope: TLS inspection configurations.
  link: [drops non-TLS traffic that matches the conditions](../facts/network-firewall.md#network-firewall-tls-drops-non-tls-in-scope)
  link: [doesn't include a server name](../facts/network-firewall.md#network-firewall-tls-drops-non-tls-in-scope)
network-firewall-tls-inspection-decrypt-reencrypt
  claim: Network Firewall uses TLS inspection configurations to decrypt inbound and outbound SSL/TLS traffic, inspect it with the firewall policy's stateful rules, and re-encrypt it before sending it on; you can inspect inbound, outbound or both.
  scope: per firewall policy; TLS inspection configuration attached.
  link: [decrypt your firewall's inbound and outbound SSL/TLS traffic](../facts/network-firewall.md#network-firewall-tls-inspection-decrypt-reencrypt)
  link: [re-encrypts it before sending it to its destination](../facts/network-firewall.md#network-firewall-tls-inspection-decrypt-reencrypt)
network-firewall-tls-inspection-hourly
  claim: Using TLS inspection adds an hourly Advanced Inspection rate per Region and Availability Zone, with no extra data processing charge beyond standard Network Firewall traffic processing.
  scope: per Region and Availability Zone; TLS inspection feature in use.
  link: [additional hourly rate](../facts/network-firewall.md#network-firewall-tls-inspection-hourly)
network-firewall-tls-interrupts-existing-flows
  claim: When you add a TLS inspection configuration to an existing firewall, Network Firewall interrupts traffic flows that match the scope; ongoing matching TLS traffic is dropped and new connections begin decryption and inspection.
  scope: per firewall; TLS inspection added to an existing firewall.
  link: [Network Firewall interrupts traffic flows](../facts/network-firewall.md#network-firewall-tls-interrupts-existing-flows)
  link: [the firewall drops the traffic](../facts/network-firewall.md#network-firewall-tls-interrupts-existing-flows)
network-firewall-tls-needs-acm-new-policy
  claim: To use TLS inspection, you must import or provision certificates to AWS Certificate Manager, create a TLS inspection configuration, add it to a new firewall policy, and associate that policy with the firewall.
  scope: per firewall.
  link: [import or provision certificates to AWS Certificate Manager](../facts/network-firewall.md#network-firewall-tls-needs-acm-new-policy)
  link: [add that configuration to a new firewall policy](../facts/network-firewall.md#network-firewall-tls-needs-acm-new-policy)
network-firewall-tls-pricing-advanced-inspection
  claim: TLS inspection pricing is based on the amount of traffic Network Firewall inspects (billed as advanced inspection) and the number of deployed firewall endpoints.
  scope: TLS inspection configurations.
  link: [which appears on your bill as advanced inspection](../facts/network-firewall.md#network-firewall-tls-pricing-advanced-inspection)
  link: [the number of deployed firewall endpoints](../facts/network-firewall.md#network-firewall-tls-pricing-advanced-inspection)
network-firewall-tls-protocols-ipv4-ipv6
  claim: TLS inspection is available for the request and the response of HTTPS traffic and other TCP-based application protocols that use TLS, such as SMTPS and POP3s, and supports both IPv4 and IPv6 traffic.
  scope: TLS inspection configurations.
  link: [the request and the response for HTTPS traffic](../facts/network-firewall.md#network-firewall-tls-protocols-ipv4-ipv6)
  link: [supports both IPv4 and IPv6 traffic](../facts/network-firewall.md#network-firewall-tls-protocols-ipv4-ipv6)
network-firewall-two-az-same-zone-routing
  claim: In the multi-zone internet gateway architecture, each Availability Zone has a firewall subnet and a customer subnet; incoming traffic routes to the firewall in the same Availability Zone as the destination customer subnet, and all outgoing traffic routes through the firewalls.
  scope: multi-AZ VPC with internet gateway.
  link: [the firewall in the same Availability Zone](../facts/network-firewall.md#network-firewall-two-az-same-zone-routing)
  link: [All outgoing traffic routes through the firewalls.](../facts/network-firewall.md#network-firewall-two-az-same-zone-routing)
network-firewall-url-category-https-needs-tls-inspection
  claim: The aws_url_category keyword requires TLS inspection to evaluate URLs in HTTPS traffic; without TLS inspection, HTTPS traffic is treated as encrypted TLS traffic and cannot be evaluated, and only domain-level filtering is possible for encrypted traffic (the aws_domain_category keyword evaluates only domain information from TLS SNI or HTTP host headers).
  scope: URL and domain category filtering; HTTPS traffic.
  link: [HTTPS traffic is treated as encrypted TLS traffic](../facts/network-firewall.md#network-firewall-url-category-https-needs-tls-inspection)
network-firewall-url-domain-category-filtering
  claim: URL and Domain Category filtering lets Network Firewall filter traffic by predefined content categories, with the keywords aws_url_category (complete URLs and domains in HTTP/HTTPS traffic) and aws_domain_category (domain only, from the TLS SNI or HTTP Host header).
  scope: stateful rule groups.
  link: [filter network traffic based on predefined content categories](../facts/network-firewall.md#network-firewall-url-domain-category-filtering)
network-firewall-uses-domains-dpi
  claim: You can use Network Firewall to pass traffic only from known AWS service domains or IP endpoints, use custom lists of known bad domains, perform deep packet inspection on traffic entering or leaving the VPC, and filter protocols like HTTPS independent of the port used.
  scope: per firewall.
  link: [Use custom lists of known bad domains](../facts/network-firewall.md#network-firewall-uses-domains-dpi)
  link: [deep packet inspection on traffic entering or leaving](../facts/network-firewall.md#network-firewall-uses-domains-dpi)
  link: [independent of the port used](../facts/network-firewall.md#network-firewall-uses-domains-dpi)
network-firewall-uses-gwlb-internally
  claim: AWS Network Firewall already uses AWS Gateway Load Balancer to give the firewall endpoint elastic scalability and needs no separate GWLB integration; the firewall endpoint ENI has the type gateway_load_balancer_endpoint.
  scope: Network Firewall endpoints.
  link: [already uses AWS Gateway Load Balancer](../facts/network-firewall.md#network-firewall-uses-gwlb-internally)
  link: [does not require separate integration](../facts/network-firewall.md#network-firewall-uses-gwlb-internally)
network-firewall-vpce-associations-only-primary-azs
  claim: You can create VPC endpoint associations for any VPC, but only in Availability Zones where the firewall already has a primary endpoint.
  scope: per firewall.
  link: [where the firewall already has a primary endpoint](../facts/network-firewall.md#network-firewall-vpce-associations-only-primary-azs)
network-firewall-vpce-associations-per-az
  claim: One firewall can have at most 50 VPC endpoint associations in each Availability Zone; this quota can't be changed.
  scope: per firewall, per Availability Zone; maximum; not adjustable.
  link: [50](../facts/network-firewall.md#network-firewall-vpce-associations-per-az)
  say: fifty associations
network-firewall-when-to-use
  claim: AWS positions Network Firewall for control and visibility of VPC-to-VPC traffic, URL, IP and domain-based outbound filtering to stop data leaks and block known malware hosts, securing Direct Connect and VPN traffic through Transit Gateway, and filtering inbound internet traffic.
  scope: AWS Network Firewall.
  link: [control and visibility of VPC-to-VPC traffic](../facts/network-firewall.md#network-firewall-when-to-use)
  link: [URL, IP address, and domain-based outbound traffic filtering](../facts/network-firewall.md#network-firewall-when-to-use)
shield-advanced-billed-to-payer-one-fee
  claim: With Shield Advanced you pay one monthly subscription fee for all accounts created under a consolidated billing account, plus usage fees based on GB of data transferred out; for Organizations members, AWS bills the subscription to the organization's payer account.
  scope: per consolidated billing family; the organization owns all accounts and resources.
  link: [one monthly subscription fee for all accounts](../facts/shield.md#shield-advanced-billed-to-payer-one-fee)
  link: [based on GB of data transferred out](../facts/shield.md#shield-advanced-billed-to-payer-one-fee)
  link: [against the payer account for the organization](../facts/shield.md#shield-advanced-billed-to-payer-one-fee)
shield-advanced-covers-standard-waf-costs
  claim: A Shield Advanced subscription covers the costs of standard AWS WAF capabilities (per web ACL, per rule and the base per-million-request price) for resources you protect with Shield Advanced, but not AWS WAF use for unprotected resources or non-standard AWS WAF costs such as Bot Control and the CAPTCHA action.
  scope: Shield Advanced protected resources.
  link: [the costs of using standard AWS WAF capabilities](../facts/shield.md#shield-advanced-covers-standard-waf-costs)
  link: [does not cover the use of AWS WAF](../facts/shield.md#shield-advanced-covers-standard-waf-costs)
  link: [any additional non-standard AWS WAF costs](../facts/shield.md#shield-advanced-covers-standard-waf-costs)
shield-advanced-dto-fee-examples
  claim: In the AWS Shield pricing examples, Shield Advanced data transfer out usage fees are $0.050 per GB for an Application Load Balancer and $0.025 per GB for a CloudFront distribution.
  scope: per GB of data transfer out from protected resources; example rates from the pricing page; if CloudFront sits in front of the ELB and receives all its traffic, you only need to protect CloudFront.
  link: [$0.050 per GB](../facts/shield.md#shield-advanced-dto-fee-examples)
  link: [$0.025 per GB](../facts/shield.md#shield-advanced-dto-fee-examples)
  say: five cents per gigabyte | two and a half cents per gigabyte
shield-advanced-event-history-13-months
  claim: With Shield Advanced you can see the history of all DDoS incidents on your resources for the trailing 13 months.
  scope: per account.
  link: [13 months](../facts/shield.md#shield-advanced-event-history-13-months)
  say: thirteen months
shield-advanced-includes-anti-ddos-amr
  claim: A Shield Advanced subscription includes access to the Layer 7 Anti-DDoS Amazon managed rule group.
  scope: Shield Advanced subscribers; request volume limits apply (numbers lens).
  link: [includes access to the Layer 7 Anti-DDoS Amazon Managed Rule group](../facts/shield.md#shield-advanced-includes-anti-ddos-amr)
shield-advanced-monthly-fee
  claim: AWS Shield Advanced costs a monthly fee of $3,000 per month per organization, plus Shield Advanced data transfer usage fees for the resources it protects.
  scope: per organization (payer account); AWS Channel Resellers pay a separate monthly fee for each member account (pricing page note).
  link: [$3,000 per month](../facts/shield.md#shield-advanced-monthly-fee)
  say: three thousand dollars per month
shield-advanced-not-automatic-per-resource
  claim: Shield Advanced protections are enabled only for resources that you explicitly specify in Shield Advanced or protect through a Firewall Manager Shield Advanced policy; Shield Advanced does not automatically protect your resources.
  scope: per resource.
  link: [explicitly specified in Shield Advanced](../facts/shield.md#shield-advanced-not-automatic-per-resource)
  link: [Shield Advanced doesn't automatically protect your resources.](../facts/shield.md#shield-advanced-not-automatic-per-resource)
shield-advanced-one-year-commitment
  claim: AWS Shield Advanced requires a 1-year subscription commitment and a monthly fee, plus a usage fee based on data transfer out from CloudFront, ELB, EC2 and Global Accelerator; subscriptions auto-renew annually.
  scope: per Shield Advanced subscription; all Shield Advanced benefits, including DDoS cost protection, are subject to fulfilling the 1-year commitment.
  link: [1-year subscription commitment](../facts/shield.md#shield-advanced-one-year-commitment)
  link: [auto-renew annually](../facts/shield.md#shield-advanced-one-year-commitment)
  say: one-year subscription commitment
shield-advanced-paid-expanded-protection
  claim: Shield Advanced is a subscription that provides expanded DDoS attack protection for the resources you add protection to, and it incurs additional charges.
  scope: per protected resource; account subscribed and protection added to the resource.
  link: [provides expanded DDoS attack protection](../facts/shield.md#shield-advanced-paid-expanded-protection)
  link: [Shield Advanced incurs additional charges.](../facts/shield.md#shield-advanced-paid-expanded-protection)
shield-advanced-resource-types
  claim: Shield Advanced protects CloudFront distributions, Route 53 hosted zones, Global Accelerator standard accelerators, EC2 Elastic IP addresses (and the EC2 instances and Network Load Balancers associated with them), Application Load Balancers and Classic Load Balancers.
  scope: Shield Advanced protections.
  link: [Amazon EC2 instances, through association to Amazon EC2 Elastic IP addresses.](../facts/shield.md#shield-advanced-resource-types)
  link: [Network Load Balancers, through associations to Amazon EC2 Elastic IP addresses.](../facts/shield.md#shield-advanced-resource-types)
  link: [AWS Global Accelerator standard accelerators.](../facts/shield.md#shield-advanced-resource-types)
shield-advanced-visibility-metrics
  claim: Shield Advanced gives access to advanced, real-time metrics and reports on events and attacks on protected resources, through the Shield Advanced API and console and through Amazon CloudWatch metrics.
  scope: Shield Advanced protected resources.
  link: [through Amazon CloudWatch metrics](../facts/shield.md#shield-advanced-visibility-metrics)
shield-advanced-waf-included
  claim: A Shield Advanced subscription includes standard AWS WAF fees for Shield-protected resources (monthly fees for web ACLs and rules, and request fees for web ACLs with the default (1,500) WCU limits), for up to 50 billion AWS WAF requests per month.
  scope: per subscribed payer ID, per calendar month; requests that Shield Advanced detects as DDoS do not count towards the 50 billion; requests beyond it are billed.
  link: [50 billion](../facts/shield.md#shield-advanced-waf-included)
  link: [1,500](../facts/shield.md#shield-advanced-waf-included)
  say: fifty billion requests | fifteen hundred W C Us
shield-advanced-waf-not-covered
  claim: Shield Advanced does not cover AWS WAF for resources that it does not protect, nor non-standard WAF costs such as Bot Control, the CAPTCHA action, web ACLs above 1,500 WCUs, and body inspection beyond the default size.
  scope: per Shield Advanced subscription.
  link: [1,500 WCUs](../facts/shield.md#shield-advanced-waf-not-covered)
  say: fifteen hundred W C Us
shield-advanced-when-to-subscribe
  claim: AWS suggests Shield Advanced for applications that need guaranteed availability, rapid access to DDoS mitigation experts, AWS awareness and notification of attacks, or predictable cloud costs during a DDoS attack.
  scope: per application.
  link: [Guaranteed availability for the users of the application.](../facts/shield.md#shield-advanced-when-to-subscribe)
  link: [Rapid access to DDoS mitigation experts](../facts/shield.md#shield-advanced-when-to-subscribe)
  link: [Predictability in your cloud costs](../facts/shield.md#shield-advanced-when-to-subscribe)
shield-advanced-which-resources-to-protect
  claim: For each subscribed account, AWS suggests adding Shield Advanced protection to resources that serve external users on the internet, that are exposed to the internet and part of a critical application, or that are protected by an AWS WAF web ACL.
  scope: per subscribed account.
  link: [The resource serves external users on the internet.](../facts/shield.md#shield-advanced-which-resources-to-protect)
  link: [protected by an AWS WAF web ACL](../facts/shield.md#shield-advanced-which-resources-to-protect)
shield-anti-ddos-amr-supersedes-l7am
  claim: The AWS WAF Anti-DDoS Managed Rule Group supersedes the Shield Advanced Layer 7 Auto Mitigation (L7AM) feature and detects and mitigates attacks within seconds rather than minutes; existing Shield Advanced customers can continue to use the legacy solution, and new Shield Advanced customers who require it contact AWS Support.
  scope: HTTP request flood protection; existing Shield Advanced customers can keep using the legacy feature; new customers ask AWS Support.
  link: [It supersedes the Layer 7 Auto Mitigation (L7AM) feature.](../facts/shield.md#shield-anti-ddos-amr-supersedes-l7am)
  link: [within seconds rather than minutes](../facts/shield.md#shield-anti-ddos-amr-supersedes-l7am)
shield-architecture-decides-resiliency
  claim: Shield provides DDoS detection and mitigation for all applications running on AWS, but your application architecture decisions influence your level of DDoS resiliency, the application's ability to keep operating within expected parameters during an attack.
  scope: per application.
  link: [will influence your level of DDoS resiliency](../facts/shield.md#shield-architecture-decides-resiliency)
  link: [ability to continue operating within expected parameters](../facts/shield.md#shield-architecture-decides-resiliency)
shield-attack-classes-layers
  claim: Shield detects network volumetric attacks that try to saturate the capacity of the targeted network or resource, and network protocol attacks such as a TCP SYN flood, which can exhaust connection state on servers, load balancers or firewalls.
  scope: AWS Shield.
  link: [network protocol attack is a TCP SYN flood](../facts/shield.md#shield-attack-classes-layers)
  link: [saturate the capacity of the targeted network](../facts/shield.md#shield-attack-classes-layers)
shield-auto-l7-managed-rule-group
  claim: In Shield Advanced automatic application layer DDoS mitigation (the legacy Layer 7 Auto Mitigation, superseded by the Anti-DDoS Managed Rule Group), when automatic mitigation is enabled for a resource, Shield Advanced maintains a rule group in the resource's associated web ACL with a rate-based rule for known DDoS sources, compares current traffic patterns against historic traffic baselines, and responds to detected attacks by deploying additional, custom AWS WAF rules in the rule group.
  scope: per Shield Advanced protected resource; automatic mitigation enabled; legacy feature: new Shield Advanced customers need AWS Support to access it.
  link: [rule group in the resource's associated web ACL](../facts/shield.md#shield-auto-l7-managed-rule-group)
  link: [compares current traffic patterns against historic traffic baselines](../facts/shield.md#shield-auto-l7-managed-rule-group)
shield-auto-l7-mitigation-count-or-block
  claim: You can configure Shield Advanced to respond automatically to application layer (layer 7) attacks against protected resources by counting or blocking the web requests that are part of the attack; this adds to the protection of an AWS WAF web ACL with your own rate-based rule. This automatic mitigation is the legacy Layer 7 Auto Mitigation (L7AM): the Anti-DDoS Managed Rule Group supersedes it, existing Shield Advanced customers can continue to use it, and new Shield Advanced customers who require it contact AWS Support.
  scope: per Shield Advanced protected resource; AWS WAF web ACL associated with the resource; legacy feature for new Shield Advanced customers.
  link: [respond automatically to mitigate application layer (layer 7) attacks](../facts/shield.md#shield-auto-l7-mitigation-count-or-block)
  link: [by counting or blocking web requests](../facts/shield.md#shield-auto-l7-mitigation-count-or-block)
shield-auto-l7-needs-wafv2
  claim: Automatic application layer DDoS mitigation works only with web ACLs created with the latest version of AWS WAF (v2).
  scope: Shield Advanced automatic application layer mitigation.
  link: [the latest version of AWS WAF (v2)](../facts/shield.md#shield-auto-l7-needs-wafv2)
shield-auto-mitigation-wcu
  claim: Turning on Shield Advanced automatic application layer DDoS mitigation adds a rule group to the web ACL that uses 150 web ACL capacity units (WCUs), which count against the web ACL's WCU usage.
  scope: per web ACL.
  link: [150](../facts/shield.md#shield-auto-mitigation-wcu)
  say: one hundred fifty W C Us
shield-change-network-security-manager-ga-2026
  claim: On September 24, 2026, AWS announced general availability of AWS Network Security Manager in US East (N. Virginia); it supports AWS WAF and AWS Shield Advanced, with Network Firewall support to follow.
  scope: US East (N. Virginia).
  link: [September 24, 2026](../facts/shield.md#shield-change-network-security-manager-ga-2026)
  say: September twenty-fourth, twenty twenty-six
shield-cloudfront-protection-prompts-waf-rate-rules
  claim: When you protect CloudFront distributions with Shield Advanced, it prompts you to associate AWS WAF web ACLs and create rate-based rules for them, and offers automatic application layer DDoS mitigation or proactive engagement, which use Route 53 health checks associated with the resource.
  scope: Shield Advanced protections for CloudFront distributions.
  link: [AWS WAF web ACLs and create rate-based rules](../facts/shield.md#shield-cloudfront-protection-prompts-waf-rate-rules)
  link: [use Route 53 health checks](../facts/shield.md#shield-cloudfront-protection-prompts-waf-rate-rules)
shield-cloudfront-route53-inline-mitigation
  claim: Applications that serve content with CloudFront and Route 53 are protected by an integrated, fully inline DDoS mitigation system that mitigates infrastructure layer attacks in real time.
  scope: CloudFront distributions and Route 53 hosted zones.
  link: [an integrated, fully inline DDoS mitigation system](../facts/shield.md#shield-cloudfront-route53-inline-mitigation)
  link: [mitigates infrastructure layer attacks in real time](../facts/shield.md#shield-cloudfront-route53-inline-mitigation)
shield-cost-protection-credit
  claim: If a DDoS attack increases utilization of a Shield Advanced protected resource, you can request a Shield Advanced service credit for charges related to the increased utilization, to the extent it is not mitigated by Shield Advanced; credits apply only to Shield Advanced usage.
  scope: Shield Advanced protected resources; protection added before the attack.
  link: [request a Shield Advanced service credit](../facts/shield.md#shield-cost-protection-credit)
  link: [only to Shield Advanced usage](../facts/shield.md#shield-cost-protection-credit)
shield-credit-charge-types
  claim: Shield Advanced credits are available only for listed types of charges, which include instance costs for protected EC2 instances that an auto-scaling policy created in response to the attack.
  scope: Shield Advanced service credits.
  link: [an auto-scaling policy in response to the attack](../facts/shield.md#shield-credit-charge-types)
shield-credit-prereqs-before-attack
  claim: To be eligible for a credit you must have added Shield Advanced protection to the resource before the attack began (resources added during an attack are not eligible), and for CloudFront and ALB resources you must have had an AWS WAF web ACL with a rate-based rule in Block mode.
  scope: Shield Advanced service credits.
  link: [added during an attack are not eligible](../facts/shield.md#shield-credit-prereqs-before-attack)
  link: [in the web ACL in Block mode](../facts/shield.md#shield-credit-prereqs-before-attack)
shield-credit-request-15-days
  claim: To be eligible for a Shield Advanced cost protection credit, you must submit the credit request within the 15 day period right after the billing month in which the attack occurred.
  scope: per attack billing month.
  link: [15 day](../facts/shield.md#shield-credit-request-15-days)
  say: fifteen days
shield-dns-query-flood-route53
  claim: In a DNS query flood, an attacker uses many DNS queries to exhaust the resources of a DNS server; Shield Advanced can help protect Amazon Route 53 DNS servers against DNS query flood attacks.
  scope: DDoS attack types.
  link: [multiple DNS queries to exhaust the resources](../facts/shield.md#shield-dns-query-flood-route53)
  link: [protection against DNS query flood attacks](../facts/shield.md#shield-dns-query-flood-route53)
shield-edge-services-global-capacity
  claim: Amazon CloudFront, AWS Global Accelerator and Amazon Route 53 give access to internet and DDoS mitigation capacity across the AWS global edge network, which helps mitigate larger volumetric attacks that can reach terabits in scale.
  scope: DDoS resilient architectures.
  link: [mitigating larger volumetric attacks](../facts/shield.md#shield-edge-services-global-capacity)
shield-faq-advanced-api-activation
  claim: AWS Shield Advanced can be activated through APIs, and AWS resources can be added to or removed from Shield Advanced protection through APIs.
  scope: Shield Advanced subscription and protections.
  link: [can be activated via APIs](../facts/shield.md#shield-faq-advanced-api-activation)
shield-faq-advanced-choose-resources
  claim: AWS Shield Advanced lets you choose which resources to protect, and you are charged Shield Advanced Data Transfer only on those protected resources.
  scope: per protected resource.
  link: [choose the resources that you'd like to protect](../facts/shield.md#shield-faq-advanced-choose-resources)
shield-faq-advanced-cloudwatch-notification
  claim: With AWS Shield Advanced you get notification of DDoS events through CloudWatch metrics, typically within a few minutes of event detection.
  scope: Shield Advanced protected resources.
  link: [through CloudWatch metrics](../facts/shield.md#shield-faq-advanced-cloudwatch-notification)
  link: [within a few minutes of event detection](../facts/shield.md#shield-faq-advanced-cloudwatch-notification)
shield-faq-advanced-data-transfer-fees
  claim: In addition to the monthly fee, AWS Shield Advanced charges Data Transfer usage fees for AWS resources enabled for advanced protection, and Shield Advanced charges are in addition to the standard fees of Amazon EC2, Elastic Load Balancing, Amazon CloudFront, AWS Global Accelerator and Amazon Route 53.
  scope: Shield Advanced protected resources.
  link: [Data Transfer usage fees](../facts/shield.md#shield-faq-advanced-data-transfer-fees)
shield-faq-advanced-l7-ddos-50-billion-included
  claim: AWS Shield Advanced customers can enable the AWS WAF application layer DDoS protection feature at no additional cost for up to 50 billion AWS WAF requests per month.
  scope: per Shield Advanced customer, per month; maximum; not adjustable.
  link: [up to 50 billion AWS WAF requests per month](../facts/shield.md#shield-faq-advanced-l7-ddos-50-billion-included)
shield-faq-advanced-layers-srt-cost-protection
  claim: AWS Shield Advanced includes DDoS protection for layers 3, 4 and 7, 24/7 support from the Shield Response Team (SRT), and cost protection against event spikes.
  scope: Shield Advanced subscription.
  link: [layers 3, 4, and 7](../facts/shield.md#shield-faq-advanced-layers-srt-cost-protection)
  link: [24/7 support from the Shield Response Team](../facts/shield.md#shield-faq-advanced-layers-srt-cost-protection)
shield-faq-advanced-multi-account-fee-once
  claim: You subscribe multiple AWS accounts to AWS Shield Advanced by enabling it on each account, and you pay the monthly fee once if the accounts are under a single consolidated billing and you own all the accounts and their resources.
  scope: accounts under one consolidated billing family.
  link: [individually enabling it on each account](../facts/shield.md#shield-faq-advanced-multi-account-fee-once)
  link: [You will pay the monthly fee once](../facts/shield.md#shield-faq-advanced-multi-account-fee-once)
shield-faq-ddos-load-test-not-authorized
  claim: A DDoS load test is not authorized on AWS under the penetration testing policy; a live DDoS test needs approval requested through AWS Support and an approved DDoS test vendor.
  scope: DDoS testing on AWS.
  link: [which is not authorized on AWS](../facts/shield.md#shield-faq-ddos-load-test-not-authorized)
shield-faq-global-threat-dashboard
  claim: AWS Shield Advanced customers get the Global threat environment dashboard, an anonymized and sampled view of all DDoS events seen on AWS within the last 2 weeks.
  scope: Shield Advanced customers.
  link: [the last 2 weeks](../facts/shield.md#shield-faq-global-threat-dashboard)
shield-faq-protect-outside-lock-down-backend
  claim: To protect resources outside AWS with Shield Advanced, customers put CloudFront or Route 53 in front, protect those with Shield Advanced, and must lock down their backend resources to accept traffic only from these AWS endpoints.
  scope: resources outside AWS behind CloudFront or Route 53.
  link: [lock down their backend resources](../facts/shield.md#shield-faq-protect-outside-lock-down-backend)
shield-faq-srt-needs-business-or-enterprise
  claim: The AWS Shield FAQ says you need a Business or Enterprise support plan to escalate to or engage the AWS Shield Response Team (SRT); the AWS Support FAQ says Business Support stops accepting new subscriptions on December 2, 2025, with all old plans shutting down on January 1, 2027, and the current plans are Business Support+, Enterprise and Unified Operations.
  scope: the Shield FAQ answer on SRT escalation; AWS Support plans are in transition to Business Support+, Enterprise and Unified Operations until January 1, 2027.
  link: [a Business or Enterprise support plan](../facts/shield.md#shield-faq-srt-needs-business-or-enterprise)
shield-faq-standard-buy-waf-for-l7-ddos
  claim: For application layer (L7) DDoS protection, AWS Shield Standard customers need to purchase the corresponding AWS Managed Rule group from AWS WAF.
  scope: Shield Standard customers.
  link: [purchase the corresponding AWS Managed Rule group](../facts/shield.md#shield-faq-standard-buy-waf-for-l7-ddos)
shield-faq-standard-layer-3-4-all-customers
  claim: AWS Shield Standard protects all AWS customers against common, frequently occurring infrastructure (layer 3 and 4) events such as SYN/UDP floods and reflection events.
  scope: AWS Shield Standard.
  link: [layer 3 and 4](../facts/shield.md#shield-faq-standard-layer-3-4-all-customers)
  link: [for all AWS customers](../facts/shield.md#shield-faq-standard-layer-3-4-all-customers)
shield-faq-standard-no-additional-cost
  claim: There are no additional costs for AWS Shield Standard; it is built into the AWS services you already use.
  scope: AWS Shield Standard.
  link: [no additional costs for AWS Shield Standard](../facts/shield.md#shield-faq-standard-no-additional-cost)
shield-faq-standard-no-resource-limit
  claim: There is no limit on the number of resources subject to AWS Shield Standard protection.
  scope: per account; maximum; not adjustable.
  link: [no limit on the number of resources](../facts/shield.md#shield-faq-standard-no-resource-limit)
shield-faq-standard-use-waf-for-layer-7
  claim: Customers can use AWS WAF, alongside AWS Shield Standard, to protect against application layer attacks like HTTP POST or GET floods.
  scope: AWS Shield Standard.
  link: [HTTP POST or GET floods](../facts/shield.md#shield-faq-standard-use-waf-for-layer-7)
shield-health-based-detection-route53
  claim: You can use Amazon Route 53 health checks with Shield Advanced for health-based detection, which helps prevent false positives and gives faster detection and mitigation when a protected resource is unhealthy; it is available for any resource type except Route 53 hosted zones.
  scope: Shield Advanced protections.
  link: [helps prevent false positives](../facts/shield.md#shield-health-based-detection-route53)
  link: [provides faster detection and mitigation](../facts/shield.md#shield-health-based-detection-route53)
  link: [any resource type except Route 53 hosted zones](../facts/shield.md#shield-health-based-detection-route53)
shield-http-flood-cache-busting
  claim: In an HTTP flood, including GET and POST floods, an attacker sends many HTTP requests that look like a real user; cache-busting attacks vary the query string to prevent use of edge-cached content and force the origin web server to serve it.
  scope: layer 7 DDoS attack types.
  link: [appear to be from a real user](../facts/shield.md#shield-http-flood-cache-busting)
  link: [prevent use of edge-located cached content](../facts/shield.md#shield-http-flood-cache-busting)
shield-l7-best-mitigated-scale-plus-waf
  claim: Web application layer DDoS attacks are best mitigated using a combination of application scale and a web application firewall (WAF); Shield Advanced uses AWS WAF web request inspection logs to detect anomalies that can be mitigated either automatically or via engagement with the SRT.
  scope: DDoS resilient architectures.
  link: [uses web request inspection logs from AWS WAF](../facts/shield.md#shield-l7-best-mitigated-scale-plus-waf)
shield-layers-3-4-and-7
  claim: Shield Standard and Shield Advanced protect AWS resources against DDoS attacks at the network and transport layers (layers 3 and 4) and the application layer (layer 7).
  scope: AWS Shield Standard and Shield Advanced.
  link: [network and transport layers (layer 3 and 4)](../facts/shield.md#shield-layers-3-4-and-7)
  link: [the application layer (layer 7)](../facts/shield.md#shield-layers-3-4-and-7)
shield-no-http-content-inspection
  claim: AWS Shield inspects traffic primarily at the network and transport layers and does not inspect the contents of application layer (HTTP/S) traffic; it looks for DDoS patterns such as unusually high traffic volumes or protocol misuse.
  scope: AWS Shield.
  link: [does not inspect the contents](../facts/shield.md#shield-no-http-content-inspection)
  link: [unusually high traffic volumes or protocol misuse](../facts/shield.md#shield-no-http-content-inspection)
shield-nsd-preview-no-charge
  claim: AWS Shield network security director is in public preview, and AWS currently does not charge for its use; you still pay for underlying services such as AWS WAF.
  scope: preview.
  link: [does not charge for use](../facts/shield.md#shield-nsd-preview-no-charge)
shield-perimeter-edge-vs-vpc
  claim: If users first enter an application in an AWS Region, the application perimeter is the VPC; if Amazon Route 53 directs them to CloudFront or Global Accelerator first, the perimeter begins at the edge of the AWS network.
  scope: per application.
  link: [perimeter is your Amazon Virtual Private Cloud (VPC)](../facts/shield.md#shield-perimeter-edge-vs-vpc)
  link: [begins at the edge of the AWS network](../facts/shield.md#shield-perimeter-edge-vs-vpc)
shield-proactive-engagement-needs-health-check
  claim: Shield Advanced proactive engagement is available only for resource protections that have an associated Amazon Route 53 health check, and it requires a Business Support or Enterprise Support plan.
  scope: Shield Advanced protections.
  link: [have an associated Amazon Route 53 health check](../facts/shield.md#shield-proactive-engagement-needs-health-check)
  link: [Business Support plan](../facts/shield.md#shield-proactive-engagement-needs-health-check)
shield-proactive-engagement-srt-contacts-you
  claim: With proactive engagement, the SRT contacts you directly when the availability or performance of your application is affected by a possible attack, and it can begin troubleshooting before it reaches you.
  scope: Shield Advanced protections with health checks; event detected by Shield Advanced.
  link: [the SRT contacts you directly](../facts/shield.md#shield-proactive-engagement-srt-contacts-you)
  link: [begin troubleshooting even before they've established contact](../facts/shield.md#shield-proactive-engagement-srt-contacts-you)
shield-proactive-not-for-anti-ddos-amr
  claim: Proactive engagement is not available for events detected by the Anti-DDoS managed rule group; only an event detected by Shield Advanced can trigger it.
  scope: SRT proactive engagement.
  link: [Only an event that's detected by Shield Advanced](../facts/shield.md#shield-proactive-not-for-anti-ddos-amr)
shield-protect-sites-outside-aws-via-cloudfront
  claim: AWS Shield can protect websites not hosted in AWS, because it is integrated with Amazon CloudFront, which supports custom origins outside of AWS.
  scope: resources behind CloudFront; the site is served through CloudFront.
  link: [supports custom origins outside of AWS](../facts/shield.md#shield-protect-sites-outside-aws-via-cloudfront)
shield-protection-groups
  claim: Shield Advanced protection groups are logical collections of protected resources whose protections you manage as a group; newly protected resources that satisfy the group criteria are included automatically, and a resource can belong to several groups.
  scope: Shield Advanced protections.
  link: [create logical collections of your protected resources](../facts/shield.md#shield-protection-groups)
  link: [are automatically included in your protection group](../facts/shield.md#shield-protection-groups)
  link: [can belong to multiple protection groups](../facts/shield.md#shield-protection-groups)
shield-protection-groups-no-auto-mitigation
  claim: Automatic application layer DDoS mitigation does not interact with protection groups: Shield Advanced applies automatic mitigations for individual resources, not based on protection group findings.
  scope: Shield Advanced protection groups.
  link: [does not interact with protection groups](../facts/shield.md#shield-protection-groups-no-auto-mitigation)
  link: [applies automatic attack mitigations for individual resources](../facts/shield.md#shield-protection-groups-no-auto-mitigation)
shield-protection-groups-reduce-false-positives
  claim: Protection groups can reduce false positives in situations such as a blue/green swap, where resources alternate between near zero load and full load; monitoring individual resources there can cause false positives, while monitoring the group does not.
  scope: Shield Advanced protection groups.
  link: [false positives in situations such as blue/green swap](../facts/shield.md#shield-protection-groups-reduce-false-positives)
shield-protects-perimeter
  claim: AWS Shield is a managed threat protection service that protects the perimeter of your application, the first point of entry for application traffic coming from outside the AWS network.
  scope: AWS Shield.
  link: [a managed threat protection service](../facts/shield.md#shield-protects-perimeter)
  link: [protects the perimeter of your application](../facts/shield.md#shield-protects-perimeter)
shield-quota-protected-resources
  claim: By default, Shield Advanced can protect up to 1,000 resources of each supported resource type per account, and the quota applies per Region.
  scope: per resource type, per account, per Region; default; adjustable.
  link: [1,000](../facts/shield.md#shield-quota-protected-resources)
  say: one thousand resources
shield-quota-protection-groups
  claim: By default, an account can have up to 100 Shield Advanced protection groups, and the quota applies per Region.
  scope: per account, per Region; default; adjustable.
  link: [100](../facts/shield.md#shield-quota-protection-groups)
  say: one hundred protection groups
shield-quota-resources-per-protection-group
  claim: A protection group can include up to 1,000 individually selected protected resources by default.
  scope: per protection group (arbitrary pattern); default; adjustable.
  link: [1,000](../facts/shield.md#shield-quota-resources-per-protection-group)
  say: one thousand resources
shield-resilient-web-insert-route53-cloudfront-waf
  claim: You can improve the DDoS resiliency of a web application behind load balancers by inserting Amazon Route 53 hosted zones, CloudFront distributions and AWS WAF web ACLs between it and its users; these hide the application origin, serve requests closer to users, and detect and mitigate application layer request floods.
  scope: web applications behind ELB or a proxy layer.
  link: [inserting Amazon Route 53 hosted zones, Amazon CloudFront distributions, and AWS WAF web ACLs](../facts/shield.md#shield-resilient-web-insert-route53-cloudfront-waf)
  link: [obfuscate the application origin](../facts/shield.md#shield-resilient-web-insert-route53-cloudfront-waf)
  link: [detect and mitigate application layer request floods](../facts/shield.md#shield-resilient-web-insert-route53-cloudfront-waf)
shield-srt-can-change-web-acl-with-approval
  claim: For resources with an AWS WAF web ACL, the SRT can analyze your AWS WAF logs to identify attack characteristics and, with your approval during an engagement, apply changes to your web ACL to block the attacks.
  scope: Shield Advanced subscribers; SRT access granted.
  link: [With your approval during engagement](../facts/shield.md#shield-srt-can-change-web-acl-with-approval)
shield-srt-custom-network-mitigations
  claim: The SRT are security engineers who specialize in DDoS event response, and Shield Advanced customers can work with the SRT to create and manage custom mitigations for their resources.
  scope: Shield Advanced subscribers.
  link: [security engineers who specialize in DDoS event response](../facts/shield.md#shield-srt-custom-network-mitigations)
  link: [create and manage custom mitigations](../facts/shield.md#shield-srt-custom-network-mitigations)
shield-srt-needs-business-or-enterprise-support
  claim: To use the services of the Shield Response Team (SRT), you must be a Shield Advanced customer subscribed to the Business Support plan or the Enterprise Support plan.
  scope: Shield Advanced subscribers.
  link: [Business Support plan](../facts/shield.md#shield-srt-needs-business-or-enterprise-support)
  link: [you can contact the SRT at any time](../facts/shield.md#shield-srt-needs-business-or-enterprise-support)
shield-standard-automatic-no-charge
  claim: All AWS customers get the automatic protection of Shield Standard at no additional charge; it defends against the most common, frequently occurring network and transport layer DDoS attacks.
  scope: every AWS account; default; not adjustable.
  link: [at no additional charge](../facts/shield.md#shield-standard-automatic-no-charge)
  link: [All AWS customers benefit from the automatic protection](../facts/shield.md#shield-standard-automatic-no-charge)
  link: [network and transport layer DDoS attacks](../facts/shield.md#shield-standard-automatic-no-charge)
shield-standard-best-on-edge-resources
  claim: Shield Standard gives particular benefit to Amazon Route 53 hosted zones, CloudFront distributions and Global Accelerator standard accelerators, which receive comprehensive availability protection against all known network and transport layer attacks.
  scope: Route 53 hosted zones, CloudFront distributions, Global Accelerator standard accelerators.
  link: [you get particular benefit with Amazon Route 53 hosted zones](../facts/shield.md#shield-standard-best-on-edge-resources)
  link: [against all known network and transport layer attacks](../facts/shield.md#shield-standard-best-on-edge-resources)
shield-standard-every-region-edge
  claim: AWS Shield Standard is available on all AWS services in every AWS Region and AWS edge location worldwide.
  scope: AWS Shield Standard.
  link: [every AWS Region and AWS edge location worldwide](../facts/shield.md#shield-standard-every-region-edge)
shield-standard-no-cost-automatic
  claim: AWS Shield Standard is automatically enabled when you use services like Elastic Load Balancing (ELB), Application Load Balancer, Amazon CloudFront and Amazon Route 53, at no additional cost.
  scope: all AWS customers.
  link: [at no additional cost](../facts/shield.md#shield-standard-no-cost-automatic)
  link: [automatically enabled](../facts/shield.md#shield-standard-no-cost-automatic)
shield-standard-non-configurable
  claim: With AWS Shield Standard, protection is automatic and non-configurable; Shield Advanced allows some customization, such as advanced metrics and alerts and health checks.
  scope: AWS Shield Standard.
  link: [protection is automatic and non-configurable](../facts/shield.md#shield-standard-non-configurable)
shield-udp-reflection-attack
  claim: In a UDP reflection attack, an attacker spoofs the source of a request and uses UDP to get a large response from a server, so the extra traffic hits the spoofed, attacked IP address.
  scope: DDoS attack types.
  link: [spoof the source of a request](../facts/shield.md#shield-udp-reflection-attack)
  link: [elicit a large response from the server](../facts/shield.md#shield-udp-reflection-attack)
shield-use-with-waf-multi-layer
  claim: AWS Shield defends against large-scale, network-level attacks, and with Shield Advanced you can associate an AWS WAF web ACL with a resource for application layer protection; AWS recommends using both services in tandem for a multi-layered defense.
  scope: web application security.
  link: [Use both services in tandem](../facts/shield.md#shield-use-with-waf-multi-layer)
  link: [for a multi-layered defense strategy](../facts/shield.md#shield-use-with-waf-multi-layer)
waf-acfp-inspects-sign-up
  claim: The ACFP managed rule group labels and manages requests that might be part of malicious account creation attempts by inspecting account creation attempts sent to the application's account sign-up endpoint.
  scope: AWSManagedRulesACFPRuleSet.
  link: [account sign-up endpoint](../facts/waf.md#waf-acfp-inspects-sign-up)
  link: [malicious account creation attempts](../facts/waf.md#waf-acfp-inspects-sign-up)
waf-admin-protection-group
  claim: The Admin protection managed rule group contains rules that let you block external access to exposed administrative pages.
  scope: AWSManagedRulesAdminProtectionRuleSet.
  link: [block external access to exposed administrative pages](../facts/waf.md#waf-admin-protection-group)
waf-alb-behind-cloudfront-token-cookie
  claim: When a web ACL protects an Application Load Balancer that is the origin of a CloudFront distribution, you must configure CloudFront to forward the aws-waf-token cookie, because by default CloudFront removes cookies before forwarding a request to the origin.
  scope: web ACL on an ALB that is a CloudFront origin; rules that use tokens (CAPTCHA, Challenge, intelligent threat mitigation).
  link: [CloudFront removes cookies from the web request](../facts/waf.md#waf-alb-behind-cloudfront-token-cookie)
  link: [keep the token cookie with the web request](../facts/waf.md#waf-alb-behind-cloudfront-token-cookie)
waf-allow-insert-custom-headers
  claim: With the Allow action, in rules that you define, AWS WAF can insert custom headers into the request before forwarding it to the protected resource.
  scope: per Allow rule action.
  link: [insert custom headers into the request](../facts/waf.md#waf-allow-insert-custom-headers)
waf-allowed-request-sent-whole
  claim: When AWS WAF allows a request to proceed, the entire request is sent to the protected resource, including contents outside the limits that AWS WAF could inspect.
  scope: per allowed request.
  link: [the entire web request is sent](../facts/waf.md#waf-allowed-request-sent-whole)
waf-amplify-needs-global-web-acl
  claim: A web ACL that you associate with an AWS Amplify app must be created in the Global (CloudFront) Region; Regional web ACLs are not compatible with Amplify.
  scope: AWS Amplify apps.
  link: [in the Global CloudFront Region](../facts/waf.md#waf-amplify-needs-global-web-acl)
  link: [they are not compatible with Amplify](../facts/waf.md#waf-amplify-needs-global-web-acl)
waf-anonymous-ip-list-group
  claim: The Anonymous IP list managed rule group blocks requests from services that hide viewer identity, including VPNs, proxies, Tor nodes and web hosting providers.
  scope: AWSManagedRulesAnonymousIpList.
  link: [permit the obfuscation of viewer identity](../facts/waf.md#waf-anonymous-ip-list-group)
  link: [VPNs, proxies, Tor nodes, and web hosting providers](../facts/waf.md#waf-anonymous-ip-list-group)
waf-anti-ddos-rule-group-extra-fees
  claim: You are charged additional fees when you use the Anti-DDoS managed rule group.
  scope: AWSManagedRulesAntiDDoSRuleSet.
  link: [You are charged additional fees](../facts/waf.md#waf-anti-ddos-rule-group-extra-fees)
waf-anti-ddos-two-tiers
  claim: AWS WAF offers two tiers of DDoS protection: resource-level DDoS protection (a standard tier that works within Application Load Balancers through on-host filtering of known malicious sources) and the Anti-DDoS managed rule group AWSManagedRulesAntiDDoSRuleSet (an advanced tier).
  scope: AWS WAF.
  link: [works within Application Load Balancers](../facts/waf.md#waf-anti-ddos-two-tiers)
  link: [The advanced tier of DDoS protections](../facts/waf.md#waf-anti-ddos-two-tiers)
waf-api-associate-web-acl-rate
  claim: Calls to AssociateWebACL are limited to one request every 2 seconds per account per Region, and this quota can't be changed.
  scope: per account per Region; maximum; not adjustable.
  link: [One request every 2 seconds](../facts/waf.md#waf-api-associate-web-acl-rate)
  say: one request every two seconds
waf-asn-match-network-organizations
  claim: An ASN match statement inspects traffic by the Autonomous System Number of the request's IP address, so you can allow or block traffic from specific network organizations without managing individual IP addresses.
  scope: per rule statement.
  link: [based on the Autonomous System Number (ASN)](../facts/waf.md#waf-asn-match-network-organizations)
  link: [without having to manage individual IP addresses](../facts/waf.md#waf-asn-match-network-organizations)
waf-asn-not-replace-authentication
  claim: ASN matching supplements, but does not replace, standard authentication and authorization controls.
  scope: ASN match statements.
  link: [supplements, but doesn't replace](../facts/waf.md#waf-asn-not-replace-authentication)
waf-associated-resources-forward-requests
  claim: You associate a web ACL with one or more web application resources, and the associated resources forward incoming requests to AWS WAF for inspection by the web ACL.
  scope: per web ACL.
  link: [forward incoming requests to AWS WAF](../facts/waf.md#waf-associated-resources-forward-requests)
  link: [one or more web application resources](../facts/waf.md#waf-associated-resources-forward-requests)
waf-atp-inspects-login-attempts
  claim: The ATP managed rule group labels and manages requests that might be part of account takeover attempts by inspecting login attempts that clients send to the application's login endpoint, and it checks email and password combinations against a stolen credential database.
  scope: AWSManagedRulesATPRuleSet.
  link: [inspecting login attempts](../facts/waf.md#waf-atp-inspects-login-attempts)
  link: [against its stolen credential database](../facts/waf.md#waf-atp-inspects-login-attempts)
waf-atp-not-for-cognito
  claim: The ATP feature is not available for Amazon Cognito user pools.
  scope: Amazon Cognito user pools.
  link: [not available for Amazon Cognito user pools](../facts/waf.md#waf-atp-not-for-cognito)
waf-atp-response-inspection-cloudfront
  claim: For CloudFront distributions, the ATP rule group also inspects the application's responses to login attempts and can temporarily block client sessions or IP addresses with too many login failures.
  scope: AWSManagedRulesATPRuleSet; CloudFront distributions only.
  link: [temporarily block client sessions or IP addresses](../facts/waf.md#waf-atp-response-inspection-cloudfront)
waf-block-default-403
  claim: When AWS WAF blocks a request, by default the protected AWS resource responds with an HTTP 403 (Forbidden) status code; in rules you define, you can customize the response.
  scope: per Block action; default; adjustable; custom response configured in rules that you define.
  link: [HTTP `403 (Forbidden)` status code](../facts/waf.md#waf-block-default-403)
  link: [you can customize the response](../facts/waf.md#waf-block-default-403)
waf-body-extra-charge-above-16kb
  claim: When you raise the body inspection limit, you pay extra only for requests whose bodies are larger than the default 16 KB: $0.30 per million requests for each additional 16KB analyzed.
  scope: per web ACL, for CloudFront, API Gateway, Cognito, App Runner and Verified Access; list price on the AWS WAF pricing page; prices may vary across AWS Regions.
  link: [$0.30 per million requests](../facts/waf.md#waf-body-extra-charge-above-16kb)
  link: [16 KB](../facts/waf.md#waf-body-extra-charge-above-16kb)
  say: thirty cents per million requests | sixteen kilobytes
waf-body-forwarded-only-within-limit
  claim: When a request body is larger than the body inspection size limit, the host service forwards only the contents within the limit to AWS WAF for inspection.
  scope: per protected resource; request body larger than the body inspection size limit.
  link: [forwards the contents that are within the limit](../facts/waf.md#waf-body-forwarded-only-within-limit)
waf-body-limit-alb-appsync-8kb
  claim: For Application Load Balancer and AWS AppSync, the AWS WAF body inspection size limit is fixed at 8 KB (8,192 bytes).
  scope: per web ACL association, for ALB and AppSync; fixed; not adjustable; AWS WAF inspects only the body contents within the limit; oversize handling applies to the rest.
  link: [8 KB](../facts/waf.md#waf-body-limit-alb-appsync-8kb)
  say: eight kilobytes
waf-body-limit-default-16kb-max-64kb
  claim: For CloudFront, API Gateway, Amazon Cognito, App Runner and Verified Access, the AWS WAF body inspection limit is 16 KB by default and can be raised in 16 KB increments up to 64 KB.
  scope: per web ACL association, for CloudFront, API Gateway, Cognito, App Runner and Verified Access; default; adjustable; set in the web ACL's resource association configuration; the options are 16, 32, 48 and 64 KB.
  link: [16 KB](../facts/waf.md#waf-body-limit-default-16kb-max-64kb)
  link: [64 KB](../facts/waf.md#waf-body-limit-default-16kb-max-64kb)
  say: sixteen kilobytes | sixty-four kilobytes
waf-bot-control-common-level
  claim: The common protection level of Bot Control adds labels to self-identifying bots, verifies generally desirable bots and detects high confidence bot signatures.
  scope: Bot Control common protection level.
  link: [adds labels to self-identifying bots](../facts/waf.md#waf-bot-control-common-level)
  link: [verifies generally desirable bots](../facts/waf.md#waf-bot-control-common-level)
waf-bot-control-targeted-level
  claim: The targeted protection level of Bot Control adds detection for sophisticated bots that do not self identify, using techniques such as browser interrogation, fingerprinting and behavior heuristics.
  scope: Bot Control targeted protection level.
  link: [sophisticated bots that don't self identify](../facts/waf.md#waf-bot-control-targeted-level)
  link: [browser interrogation, fingerprinting, and behavior heuristics](../facts/waf.md#waf-bot-control-targeted-level)
waf-bot-control-via-firewall-manager
  claim: You can use Firewall Manager AWS WAF policies to deploy the Bot Control managed rule group across applications in multiple accounts of your organization in AWS Organizations.
  scope: AWS Organizations.
  link: [AWS Firewall Manager AWS WAF policies](../facts/waf.md#waf-bot-control-via-firewall-manager)
  link: [multiple accounts that are part of your organization](../facts/waf.md#waf-bot-control-via-firewall-manager)
waf-bot-control-what
  claim: With Bot Control you can monitor, block or rate limit bots such as scrapers, scanners, crawlers, status monitors and search engines.
  scope: Bot Control managed rule group.
  link: [monitor, block, or rate limit bots](../facts/waf.md#waf-bot-control-what)
  link: [scrapers, scanners, crawlers, status monitors, and search engines](../facts/waf.md#waf-bot-control-what)
waf-bot-ddos-groups-recognize-cdns
  claim: The Bot Control and Anti-DDoS managed rule groups automatically recognize traffic from the IP ranges of CloudFront, Akamai, Cloudflare and Fastly and use the upstream client IP; other IP-based statements still need a forwarded IP configuration to evaluate the upstream client IP.
  scope: Bot Control and Anti-DDoS managed rule groups; requests through CloudFront, Akamai, Cloudflare or Fastly.
  link: [recognize traffic that originates from the IP ranges](../facts/waf.md#waf-bot-ddos-groups-recognize-cdns)
  link: [still need to specify a forwarded IP configuration](../facts/waf.md#waf-bot-ddos-groups-recognize-cdns)
waf-captcha-challenge-extra-fees
  claim: You are charged additional fees when you use the CAPTCHA or Challenge rule action in a rule or as a rule action override in a rule group.
  scope: per web ACL.
  link: [You are charged additional fees](../facts/waf.md#waf-captcha-challenge-extra-fees)
waf-captcha-challenge-https-only
  claim: CAPTCHA puzzles and silent challenges can run only when browsers access HTTPS endpoints, and browser clients must run in secure contexts to get tokens.
  scope: per CAPTCHA or Challenge action.
  link: [only run when browsers are accessing HTTPS endpoints](../facts/waf.md#waf-captcha-challenge-https-only)
  link: [must be running in secure contexts](../facts/waf.md#waf-captcha-challenge-https-only)
waf-captcha-invalid-token-puzzle-or-challenge
  claim: For a request without a valid token, AWS WAF responds to the client with a custom response code: for CAPTCHA, a CAPTCHA puzzle in a JavaScript interstitial (when the browser can handle it); for Challenge, a JavaScript interstitial with a silent challenge.
  scope: per CAPTCHA or Challenge action; token missing, invalid or expired.
  link: [with a custom response code](../facts/waf.md#waf-captcha-invalid-token-puzzle-or-challenge)
  link: [sends a CAPTCHA puzzle in a JavaScript interstitial](../facts/waf.md#waf-captcha-invalid-token-puzzle-or-challenge)
  link: [a JavaScript interstitial with a silent challenge](../facts/waf.md#waf-captcha-invalid-token-puzzle-or-challenge)
waf-captcha-valid-token-acts-like-count
  claim: When a request carries a valid, unexpired token, the CAPTCHA and Challenge actions are non-terminating: AWS WAF continues to inspect the request with the remaining rules in the web ACL, as with Count.
  scope: per CAPTCHA or Challenge action; token valid and within the immunity time.
  link: [AWS WAF continues to inspect the web request](../facts/waf.md#waf-captcha-valid-token-acts-like-count)
  link: [Similar to the Count configuration](../facts/waf.md#waf-captcha-valid-token-acts-like-count)
waf-captcha-when-block-too-strict
  claim: In web ACL rules, CAPTCHA is commonly used when a Block action would stop too many legitimate requests but letting all traffic through would allow too many unwanted requests, such as from bots.
  scope: per rule.
  link: [would stop too many legitimate requests](../facts/waf.md#waf-captcha-when-block-too-strict)
  link: [such as from bots](../facts/waf.md#waf-captcha-when-block-too-strict)
waf-case-moovit-75-percent-fewer-manual-ddos
  claim: After moving to AWS WAF with Bot Control, Amazon CloudFront and AWS Shield Advanced, Moovit saw a 75 percent decline in DDoS events that require manual intervention per quarter.
  scope: Moovit (case study).
  link: [75 percent decline in DDoS events that require manual intervention per quarter](../facts/waf.md#waf-case-moovit-75-percent-fewer-manual-ddos)
waf-case-moovit-cloudfront-first-waf-defends
  claim: In Moovit's architecture, all requests reach Amazon CloudFront first, while AWS WAF and its load balancers defend against unwanted traffic, and AWS Shield Advanced rules learned normal API use to detect anomalies and block DDoS threats.
  scope: Moovit (case study).
  link: [all requests reach Amazon CloudFront first](../facts/waf.md#waf-case-moovit-cloudfront-first-waf-defends)
  link: [learned the normal patterns of API use](../facts/waf.md#waf-case-moovit-cloudfront-first-waf-defends)
waf-case-moovit-dto-cut-50-percent
  claim: By serving through Amazon CloudFront, Moovit reduced its data transfer out (DTO) costs by 50 percent.
  scope: Moovit (case study).
  link: [reduced DTO costs by 50 percent](../facts/waf.md#waf-case-moovit-dto-cut-50-percent)
waf-case-olx-bot-control-cognito
  claim: OLX uses AWS WAF Bot Control to gain visibility and control over common and pervasive bot traffic to its customer identity solution, mitigating malicious bot events while reducing infrastructure costs.
  scope: OLX (case study).
  link: [Using AWS WAF Bot Control](../facts/waf.md#waf-case-olx-bot-control-cognito)
  link: [while reducing infrastructure costs](../facts/waf.md#waf-case-olx-bot-control-cognito)
waf-challenge-silent-no-user-impact
  claim: The Challenge action runs a silent verification in the background without involving the end user, which makes it a good option for checking suspect clients without hurting the user experience with a CAPTCHA puzzle.
  scope: per rule.
  link: [runs in the background](../facts/waf.md#waf-challenge-silent-no-user-impact)
  link: [without negatively impacting the end user experience](../facts/waf.md#waf-challenge-silent-no-user-impact)
waf-change-alb-anti-ddos-2025
  claim: On June 11, 2025, AWS WAF added resource-level DDoS protection: Anti-DDoS functionality that detects and prevents DDoS attacks in Application Load Balancers.
  scope: Application Load Balancer.
  link: [June 11, 2025](../facts/waf.md#waf-change-alb-anti-ddos-2025)
  say: June eleventh, twenty twenty-five
waf-change-alb-association-quota-2025
  claim: On October 22, 2025, AWS WAF added a quota for Application Load Balancer associations per web ACL, with a default of 100 per web ACL.
  scope: per web ACL, per account per Region; default.
  link: [October 22, 2025](../facts/waf.md#waf-change-alb-association-quota-2025)
  link: [100](../facts/waf.md#waf-change-alb-association-quota-2025)
  say: October twenty-second, twenty twenty-five | one hundred
waf-change-anti-ddos-rule-group-2025
  claim: On June 11, 2025, AWS WAF added the Anti-DDoS managed rule group AWSManagedRulesAntiDDoSRuleSet, which detects, labels and challenges requests suspected to be part of DDoS attacks.
  scope: AWS Managed Rules.
  link: [June 11, 2025](../facts/waf.md#waf-change-anti-ddos-rule-group-2025)
  link: [AWSManagedRulesAntiDDoSRuleSet](../facts/waf.md#waf-change-anti-ddos-rule-group-2025)
  say: June eleventh, twenty twenty-five
waf-change-app-runner-support-2023
  claim: On February 23, 2023, AWS WAF began to support associating a web ACL with an AWS App Runner service; this works only in the latest AWS WAF, not in AWS WAF Classic.
  scope: AWS WAF protected resources.
  link: [February 23, 2023](../facts/waf.md#waf-change-app-runner-support-2023)
  say: February twenty-third, twenty twenty-three
waf-change-atp-cloudfront-2022
  claim: On August 24, 2022, AWS WAF Fraud Control account takeover prevention (ATP) became usable with Amazon CloudFront distributions.
  scope: AWS WAF Fraud Control.
  link: [August 24, 2022](../facts/waf.md#waf-change-atp-cloudfront-2022)
  say: August twenty-fourth, twenty twenty-two
waf-change-challenge-action-2022
  claim: On October 27, 2022, AWS WAF added the Challenge rule action, which verifies that requests are being sent by browsers.
  scope: AWS WAF rule actions.
  link: [October 27, 2022](../facts/waf.md#waf-change-challenge-action-2022)
  link: [verify that requests are being sent by browsers](../facts/waf.md#waf-change-challenge-action-2022)
  say: October twenty-seventh, twenty twenty-two
waf-change-cloudfront-body-64kb-2023
  claim: On April 11, 2023, the maximum AWS WAF body inspection size for CloudFront distributions increased from 8 KB to 64 KB; the default for CloudFront is 16 KB.
  scope: per web ACL, for CloudFront.
  link: [April 11, 2023](../facts/waf.md#waf-change-cloudfront-body-64kb-2023)
  link: [64 KB](../facts/waf.md#waf-change-cloudfront-body-64kb-2023)
  link: [8 KB](../facts/waf.md#waf-change-cloudfront-body-64kb-2023)
  say: April eleventh, twenty twenty-three | sixty-four kilobytes | eight kilobytes
  changed: 2023-04-11: was 8 KB
waf-change-cognito-support-2022
  claim: On August 11, 2022, AWS WAF began to support associating a web ACL with an Amazon Cognito user pool; this works only in the latest AWS WAF, not in AWS WAF Classic.
  scope: AWS WAF protected resources.
  link: [August 11, 2022](../facts/waf.md#waf-change-cognito-support-2022)
  say: August eleventh, twenty twenty-two
waf-change-flat-rate-plan-tiers-2025
  claim: CloudFront flat-rate plans, launched on November 18, 2025, come in Free ($0/month), Pro ($15/month), Business ($200/month) and Premium tiers for new and existing CloudFront distributions.
  scope: per CloudFront distribution.
  link: [$0/month](../facts/waf.md#waf-change-flat-rate-plan-tiers-2025)
  link: [$15/month](../facts/waf.md#waf-change-flat-rate-plan-tiers-2025)
  link: [$200/month](../facts/waf.md#waf-change-flat-rate-plan-tiers-2025)
  say: zero dollars a month | fifteen dollars a month | two hundred dollars a month
waf-change-flat-rate-plans-2025
  claim: On November 18, 2025, CloudFront distributions associated with AWS WAF became eligible for flat-rate pricing plans, which have preset service quotas and give no unexpected usage charges for that distribution.
  scope: per CloudFront distribution.
  link: [November 18, 2025](../facts/waf.md#waf-change-flat-rate-plans-2025)
  link: [won't receive unexpected usage charges](../facts/waf.md#waf-change-flat-rate-plans-2025)
  say: November eighteenth, twenty twenty-five
waf-change-free-vended-logs-2025
  claim: On September 8, 2025, AWS WAF began to include 500 MB of CloudWatch Logs vended logs ingestion for every 1 million WAF requests processed, at no additional cost.
  scope: per 1 million WAF requests.
  link: [September 8, 2025](../facts/waf.md#waf-change-free-vended-logs-2025)
  link: [500 MB](../facts/waf.md#waf-change-free-vended-logs-2025)
  say: September eighth, twenty twenty-five | five hundred megabytes
waf-change-org-list-resources-quota-2024
  claim: On July 26, 2024, AWS WAF began to limit calls to ListResourcesForWebACL by all accounts in an organization in any single Region.
  scope: per organization per Region.
  link: [July 26, 2024](../facts/waf.md#waf-change-org-list-resources-quota-2024)
  say: July twenty-sixth, twenty twenty-four
waf-change-propagation-seconds-to-minutes
  claim: Changes to a web ACL or other AWS WAF resources take a small amount of time to propagate, from a few seconds to a number of minutes; for example, after you add a rule group to a web ACL, the new rule group rules might be in effect in one area where the web ACL is used and not in another.
  scope: per web ACL change.
  link: [a few seconds to a number of minutes](../facts/waf.md#waf-change-propagation-seconds-to-minutes)
  link: [take a small amount of time to propagate](../facts/waf.md#waf-change-propagation-seconds-to-minutes)
waf-change-protection-pack-console-2025
  claim: On June 17, 2025, the AWS WAF console added a new experience that manages web ACLs through protection packs (web ACLs); a protection pack is not functionally different from a web ACL.
  scope: AWS WAF console.
  link: [June 17, 2025](../facts/waf.md#waf-change-protection-pack-console-2025)
  link: [protection pack (web ACL)](../facts/waf.md#waf-change-protection-pack-console-2025)
  link: [not functionally different from a web ACL](../facts/waf.md#waf-change-protection-pack-console-2025)
  say: June seventeenth, twenty twenty-five
waf-change-rate-limit-10-2024
  claim: On August 30, 2024, the minimum request rate for a rate-based rule became 10; before this, it was 100.
  scope: per rate-based rule.
  link: [August 30, 2024](../facts/waf.md#waf-change-rate-limit-10-2024)
  link: [10](../facts/waf.md#waf-change-rate-limit-10-2024)
  link: [100](../facts/waf.md#waf-change-rate-limit-10-2024)
  say: August thirtieth, twenty twenty-four | ten | one hundred
  changed: 2024-08-30: was 100
waf-change-rate-window-2024
  claim: On February 28, 2024, rate-based rules gained a configurable evaluation window of 1, 2, 5 or 10 minutes; the default is 5, which was the only option before.
  scope: per rate-based rule.
  link: [February 28, 2024](../facts/waf.md#waf-change-rate-window-2024)
  link: [5](../facts/waf.md#waf-change-rate-window-2024)
  say: February twenty-eighth, twenty twenty-four | five minutes
  changed: 2024-02-28: was 5
waf-change-regional-association-quotas-2026
  claim: On May 1, 2026, AWS WAF added quotas for API Gateway REST API, Cognito user pool, AppSync GraphQL API, App Runner service, Verified Access instance and Amplify associations per web ACL, with a default of 100 for each.
  scope: per web ACL.
  link: [May 1, 2026](../facts/waf.md#waf-change-regional-association-quotas-2026)
  link: [100 for each](../facts/waf.md#waf-change-regional-association-quotas-2026)
  say: May first, twenty twenty-six | one hundred for each
waf-change-regional-body-limits-2024
  claim: On March 7, 2024, AWS WAF started to support larger body inspection size limits for some regional resources.
  scope: some regional resources.
  link: [March 7, 2024](../facts/waf.md#waf-change-regional-body-limits-2024)
  say: March seventh, twenty twenty-four
waf-change-verified-access-support-2023
  claim: On April 28, 2023, AWS WAF began to support associating a web ACL with an AWS Verified Access instance; this works only in the latest AWS WAF, not in AWS WAF Classic.
  scope: AWS WAF protected resources.
  link: [April 28, 2023](../facts/waf.md#waf-change-verified-access-support-2023)
  say: April twenty-eighth, twenty twenty-three
waf-change-web-acl-wcu-5000-2023
  claim: On April 11, 2023, AWS WAF began allowing up to 5,000 WCUs per web ACL without a request to support, and this new limit cannot be increased.
  scope: per web ACL.
  link: [April 11, 2023](../facts/waf.md#waf-change-web-acl-wcu-5000-2023)
  link: [5,000](../facts/waf.md#waf-change-web-acl-wcu-5000-2023)
  say: April eleventh, twenty twenty-three | five thousand
waf-classic-end-of-support
  claim: AWS WAF Classic is a service in sunset: it was announced on October 7, 2025, and its end of support date is October 7, 2026.
  scope: AWS WAF Classic.
  link: [October 7, 2026](../facts/waf.md#waf-classic-end-of-support)
  link: [October 7, 2025](../facts/waf.md#waf-classic-end-of-support)
  say: October seventh, twenty twenty-six | October seventh, twenty twenty-five
waf-classic-migrate-to-latest
  claim: AWS WAF (the current version) was released in November 2019; resources created in AWS WAF Classic must either stay in AWS WAF Classic or be migrated to the latest version.
  scope: AWS WAF Classic resources.
  link: [November 2019](../facts/waf.md#waf-classic-migrate-to-latest)
  link: [migrate them to this latest version](../facts/waf.md#waf-classic-migrate-to-latest)
  say: November twenty nineteen
waf-cloudfront-flat-rate-includes-waf
  claim: CloudFront flat-rate pricing plans combine the CloudFront CDN with several AWS services and features, including AWS WAF and DDoS protection, into a monthly price with no overage charges, regardless of traffic spikes or attacks.
  scope: CloudFront flat-rate pricing plans.
  link: [into a monthly price with no overage charges](../facts/waf.md#waf-cloudfront-flat-rate-includes-waf)
  link: [regardless of traffic spikes or attacks](../facts/waf.md#waf-cloudfront-flat-rate-includes-waf)
waf-cloudfront-flat-rate-keeps-web-acl
  claim: When a CloudFront distribution uses a flat-rate pricing plan, a valid AWS WAF web ACL must remain associated with it; you cannot remove the association unless you switch back to pay-as-you-go pricing.
  scope: CloudFront distributions on flat-rate pricing plans.
  link: [must remain associated with your CloudFront distribution](../facts/waf.md#waf-cloudfront-flat-rate-keeps-web-acl)
  link: [unless you switch back to pay-as-you-go pricing](../facts/waf.md#waf-cloudfront-flat-rate-keeps-web-acl)
waf-cloudfront-rules-run-at-edge
  claim: When you use AWS WAF on CloudFront, your rules run in all AWS edge locations close to end users, and blocked requests are stopped before they reach your web servers.
  scope: web ACLs on CloudFront distributions.
  link: [your rules run in all AWS Edge Locations](../facts/waf.md#waf-cloudfront-rules-run-at-edge)
  link: [stopped before they reach your web servers](../facts/waf.md#waf-cloudfront-rules-run-at-edge)
waf-cloudfront-standard-distribution-one-web-acl
  claim: For CloudFront standard distributions, AWS WAF adds protection with a single web ACL for each distribution, and you can enable it by associating an existing web ACL or with one-click protection in the CloudFront console.
  scope: CloudFront standard distributions.
  link: [single protection pack (web ACL) for each distribution](../facts/waf.md#waf-cloudfront-standard-distribution-one-web-acl)
  link: [by using one-click protection in the CloudFront console](../facts/waf.md#waf-cloudfront-standard-distribution-one-web-acl)
waf-cloudfront-web-acl-not-other-types
  claim: A web ACL that you have associated with a CloudFront distribution cannot be associated with any other AWS resource type, though it can be associated with more CloudFront distributions.
  scope: global web ACLs.
  link: [with any other AWS resource type](../facts/waf.md#waf-cloudfront-web-acl-not-other-types)
  link: [one or more CloudFront distributions](../facts/waf.md#waf-cloudfront-web-acl-not-other-types)
waf-cloudfront-web-acl-us-east-1
  claim: AWS WAF is available globally for CloudFront distributions, but you must use US East (N. Virginia) to create the web ACL and any resources it uses, such as rule groups, IP sets and regex pattern sets.
  scope: web ACLs for CloudFront distributions.
  link: [available globally for CloudFront distributions](../facts/waf.md#waf-cloudfront-web-acl-us-east-1)
  link: [use the Region US East (N. Virginia)](../facts/waf.md#waf-cloudfront-web-acl-us-east-1)
waf-cognito-no-atp-acfp
  claim: You cannot associate an Amazon Cognito user pool with a web ACL that uses the Fraud Control account creation fraud prevention (ACFP) or account takeover prevention (ATP) managed rule group.
  scope: Amazon Cognito user pools; web ACL uses AWSManagedRulesACFPRuleSet or AWSManagedRulesATPRuleSet.
  link: [You can't associate an Amazon Cognito user pool](../facts/waf.md#waf-cognito-no-atp-acfp)
waf-console-near-real-time-cloudwatch
  claim: The AWS WAF console dashboards give near real-time summaries of the Amazon CloudWatch metrics that AWS WAF collects when it evaluates web traffic.
  scope: per web ACL.
  link: [near real-time summaries of the Amazon CloudWatch metrics](../facts/waf.md#waf-console-near-real-time-cloudwatch)
waf-core-rule-set-owasp
  claim: The core rule set (CRS) managed rule group contains rules that are generally applicable to web applications, and AWS suggests considering it for any AWS WAF use case.
  scope: AWSManagedRulesCommonRuleSet.
  link: [generally applicable to web applications](../facts/waf.md#waf-core-rule-set-owasp)
  link: [for any AWS WAF use case](../facts/waf.md#waf-core-rule-set-owasp)
waf-count-action-test-new-rules
  claim: You can use the Count action for general monitoring and to test new web request handling rules, confirming the new settings before you switch the rules to allow or block matching requests.
  scope: per rule.
  link: [for general monitoring](../facts/waf.md#waf-count-action-test-new-rules)
  link: [to test your new web request handling rules](../facts/waf.md#waf-count-action-test-new-rules)
waf-count-non-terminating-continues
  claim: Count is a non-terminating action: AWS WAF counts the request and continues processing the remaining rules in the web ACL; in your own rules, Count can insert custom headers and add labels that other rules can match.
  scope: per rule.
  link: [This is a non-terminating action.](../facts/waf.md#waf-count-non-terminating-continues)
  link: [AWS WAF continues processing the remaining rules](../facts/waf.md#waf-count-non-terminating-continues)
  link: [add labels that other rules can match against](../facts/waf.md#waf-count-non-terminating-continues)
waf-custom-response-body-max
  claim: A single custom response body can be at most 4 KB, and all response body content in one web ACL or rule group at most 50 KB.
  scope: per custom response; per web ACL or rule group; maximum; not adjustable.
  link: [4 KB](../facts/waf.md#waf-custom-response-body-max)
  link: [50 KB](../facts/waf.md#waf-custom-response-body-max)
  say: four kilobytes | fifty kilobytes
waf-custom-response-overrides-resource
  claim: Custom responses that you specify for the AWS WAF Block action take precedence over any response specifications defined in the protected resource.
  scope: Block actions.
  link: [take precedence over any response specifications](../facts/waf.md#waf-custom-response-overrides-resource)
waf-custom-response-status-headers-body
  claim: For a Block action you can define a custom response with a status code, headers and a response body, and you can redirect the client by using a 3xx status code with a Location header.
  scope: Block rule actions and Block default actions.
  link: [the status code, headers, and response body](../facts/waf.md#waf-custom-response-status-headers-body)
  link: [Redirecting the client to a different URL.](../facts/waf.md#waf-custom-response-status-headers-body)
waf-default-action-allow-or-block
  claim: The web ACL default action must decide the final disposition of the request, so it is a terminating action: Allow or Block.
  scope: per web ACL.
  link: [so it's a terminating action](../facts/waf.md#waf-default-action-allow-or-block)
  link: [must determine the final disposition](../facts/waf.md#waf-default-action-allow-or-block)
waf-default-action-required-applies-no-terminating
  claim: You must set a default action on every web ACL; AWS WAF applies it to any request that passes all rule evaluations without a terminating action being applied.
  scope: per web ACL.
  link: [set the protection pack (web ACL) default action](../facts/waf.md#waf-default-action-required-applies-no-terminating)
  link: [without having a terminating action applied to it](../facts/waf.md#waf-default-action-required-applies-no-terminating)
waf-default-allow-add-block-rules
  claim: To allow most requests and block only some, you set the web ACL default action to Allow and add rules that identify the requests you want to block.
  scope: per web ACL.
  link: [default action to Allow](../facts/waf.md#waf-default-allow-add-block-rules)
  link: [add rules that identify web requests](../facts/waf.md#waf-default-allow-add-block-rules)
waf-definition-web-application-firewall
  claim: AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to your protected web application resources.
  scope: per protected resource.
  link: [a web application firewall](../facts/waf.md#waf-definition-web-application-firewall)
  link: [monitor the HTTP and HTTPS requests](../facts/waf.md#waf-definition-web-application-firewall)
waf-faq-acfp-sign-up-page
  claim: Account Creation Fraud Prevention (ACFP) is a paid managed rule group that detects and mitigates fake account creation attacks against your sign-up or registration page.
  scope: AWSManagedRulesACFPRuleSet.
  link: [a paid managed rule group](../facts/waf.md#waf-faq-acfp-sign-up-page)
  link: [your sign-up or registration page](../facts/waf.md#waf-faq-acfp-sign-up-page)
waf-faq-api-gateway-rest-apis
  claim: As part of Amazon API Gateway, AWS WAF can help secure and protect REST APIs.
  scope: Amazon API Gateway REST APIs.
  link: [your REST APIs](../facts/waf.md#waf-faq-api-gateway-rest-apis)
waf-faq-appsync-graphql-apis
  claim: As part of AWS AppSync, AWS WAF can help secure and protect GraphQL APIs.
  scope: AWS AppSync GraphQL APIs.
  link: [your GraphQL APIs](../facts/waf.md#waf-faq-appsync-graphql-apis)
waf-faq-atp-login-page
  claim: Account Takeover Prevention (ATP) is a managed rule group that monitors traffic to your application login page to detect unauthorized access to user accounts using compromised credentials.
  scope: AWSManagedRulesATPRuleSet.
  link: [detect unauthorized access to user accounts](../facts/waf.md#waf-faq-atp-login-page)
  link: [compromised credentials](../facts/waf.md#waf-faq-atp-login-page)
waf-faq-atp-vs-acfp
  claim: Account takeover attacks target an application sign-in page to gain access to an existing account, whereas account creation fraud targets the sign-up page to commit fraud through fake accounts.
  scope: AWS WAF Fraud Control rule groups (ATP and ACFP).
  link: [targets the application’s sign-up page](../facts/waf.md#waf-faq-atp-vs-acfp)
waf-faq-aws-vs-marketplace-managed-rules
  claim: AWS Managed Rules for AWS WAF are managed by AWS, whereas Managed Rules from AWS Marketplace are managed by third-party security sellers.
  scope: managed rule groups.
  link: [managed by third-party security sellers](../facts/waf.md#waf-faq-aws-vs-marketplace-managed-rules)
waf-faq-block-or-rate-limit-by-ip-header-agent
  claim: You can create AWS WAF rules that block or rate-limit traffic from specific user-agents, from specific IP addresses, or that contain particular request headers.
  scope: per rule.
  link: [block or rate-limit traffic from specific user-agents](../facts/waf.md#waf-faq-block-or-rate-limit-by-ip-header-agent)
waf-faq-challenge-spa-mobile-sdk-mandatory
  claim: The Challenge action does not work well with single page applications (SPA) and native mobile apps, so for these applications SDK integration is mandatory for ACFP.
  scope: ACFP for single page applications and native mobile apps.
  link: [SDK integration is mandatory](../facts/waf.md#waf-faq-challenge-spa-mobile-sdk-mandatory)
waf-faq-charged-once-per-request
  claim: You are charged only once for the standard AWS WAF request rate, whether a request is processed by AWS WAF, by the application layer (L7) DDoS protection rule group, or by both.
  scope: requests processed by AWS WAF and the L7 DDoS protection rule group.
  link: [only be charged once](../facts/waf.md#waf-faq-charged-once-per-request)
waf-faq-charges-in-addition-to-fronting-service
  claim: With pay-as-you-go pricing, AWS WAF charges are in addition to Amazon CloudFront, Application Load Balancer, Amazon API Gateway and AWS AppSync pricing; CloudFront flat-rate pricing plans instead combine CloudFront with multiple AWS services and features, including AWS WAF, into one monthly price.
  scope: AWS WAF pricing; pay-as-you-go pricing; not a CloudFront distribution on a flat-rate pricing plan.
  link: [AWS WAF charges are in addition to](../facts/waf.md#waf-faq-charges-in-addition-to-fronting-service)
waf-faq-cloudtrail-api-history
  claim: To receive a history of all AWS WAF API calls made on your account, you turn on AWS CloudTrail.
  scope: per account.
  link: [you simply turn on AWS CloudTrail](../facts/waf.md#waf-faq-cloudtrail-api-history)
waf-faq-count-action-test-managed-rule
  claim: You can configure a count action for a Managed Rule, which counts the web requests matched by its rules, to estimate how many requests would be blocked if you enable it.
  scope: per managed rule group in a web ACL.
  link: [counts the number of web requests](../facts/waf.md#waf-faq-count-action-test-managed-rule)
waf-faq-custom-error-page-via-cloudfront
  claim: You can configure CloudFront to present a custom error page when AWS WAF blocks requests.
  scope: web ACLs on CloudFront distributions.
  link: [a custom error page when requests are blocked](../facts/waf.md#waf-faq-custom-error-page-via-cloudfront)
waf-faq-inspects-http-and-https
  claim: AWS WAF can inspect web requests transmitted over HTTP or HTTPS.
  scope: per protected resource.
  link: [transmitted over HTTP or HTTPS](../facts/waf.md#waf-faq-inspects-http-and-https)
waf-faq-l7-ddos-adds-50-wcus
  claim: The application layer DDoS protection AWS Managed Rule group adds 50 WCUs to the WCU count in AWS WAF.
  scope: per web ACL that uses the rule group; fixed; not adjustable.
  link: [50 WCUs](../facts/waf.md#waf-faq-l7-ddos-adds-50-wcus)
waf-faq-l7-ddos-managed-rule-group
  claim: AWS WAF application layer (L7) DDoS protection is an AWS Managed Rule group designed to automatically defend applications against DDoS events within seconds.
  scope: AWS WAF application layer (L7) DDoS protection rule group.
  link: [an AWS Managed Rule group](../facts/waf.md#waf-faq-l7-ddos-managed-rule-group)
  link: [within seconds](../facts/waf.md#waf-faq-l7-ddos-managed-rule-group)
waf-faq-l7-ddos-protected-resources
  claim: The AWS WAF Anti-DDoS managed rule group (AWSManagedRulesAntiDDoSRuleSet), the advanced tier of AWS WAF DDoS protection, extends protection to CloudFront distributions, Application Load Balancers and other AWS services supported by AWS WAF.
  scope: AWS WAF Anti-DDoS managed rule group.
  link: [extends to CloudFront distributions, Application Load Balancers](../facts/waf.md#waf-faq-l7-ddos-protected-resources)
waf-faq-l7-ddos-standalone-no-shield-advanced
  claim: AWS WAF application layer (L7) DDoS protection can be purchased standalone and does not require an AWS Shield Advanced subscription.
  scope: AWS WAF application layer (L7) DDoS protection rule group.
  link: [can be purchased standalone](../facts/waf.md#waf-faq-l7-ddos-standalone-no-shield-advanced)
  link: [does not require an AWS Shield Advanced subscription](../facts/waf.md#waf-faq-l7-ddos-standalone-no-shield-advanced)
waf-faq-managed-rules-with-custom-rules
  claim: You can use Managed Rules along with your custom AWS WAF rules in the same web ACL.
  scope: per web ACL.
  link: [along with your custom AWS WAF rules](../facts/waf.md#waf-faq-managed-rules-with-custom-rules)
waf-faq-metrics-and-sampled-requests
  claim: AWS WAF offers two ways to see how a website is being protected: one-minute metrics in CloudWatch and Sampled Web Requests in the AWS WAF API or management console.
  scope: per web ACL.
  link: [one-minute metrics are available in CloudWatch](../facts/waf.md#waf-faq-metrics-and-sampled-requests)
waf-faq-no-monthly-request-limit
  claim: AWS WAF customers are not subject to any limits on the number of requests made in a calendar month; however, AWS Shield Advanced customers are limited to 50 billion AWS Shield protected AWS WAF requests in a calendar month.
  scope: per customer, per calendar month; maximum; not adjustable; Shield Advanced customers: 50 billion Shield-protected AWS WAF requests per calendar month.
  link: [not subject to any limits](../facts/waf.md#waf-faq-no-monthly-request-limit)
waf-faq-rate-based-exempt-ip-ranges
  claim: You can exempt high-traffic source IP ranges from being blocked by a rate-based rule by having a separate IP match condition that allows the request within the rate-based rule.
  scope: per rate-based rule.
  link: [a separate IP match condition](../facts/waf.md#waf-faq-rate-based-exempt-ip-ranges)
waf-faq-rate-based-rule-other-conditions
  claim: A rate-based rule can also contain any other AWS WAF condition that is available for a regular rule.
  scope: per rate-based rule.
  link: [any other AWS WAF Condition](../facts/waf.md#waf-faq-rate-based-rule-other-conditions)
waf-faq-rate-based-rule-price
  claim: A rate-based rule costs the same as a regular AWS WAF rule, which is $1 per rule per WebACL per month.
  scope: per rule, per web ACL, per month; fixed.
  link: [$1 per rule per WebACL per month](../facts/waf.md#waf-faq-rate-based-rule-price)
waf-faq-rate-based-vs-regular-rule
  claim: A rate-based rule is like a regular AWS WAF rule, with one addition: the ability to configure a rate-based threshold.
  scope: per rate-based rule.
  link: [the ability to configure a rate-based threshold](../facts/waf.md#waf-faq-rate-based-vs-regular-rule)
waf-faq-rate-based-web-layer-ddos
  claim: AWS WAF rate-based rules are designed to protect against use cases such as web-layer DDoS attacks, brute force login attempts and bad bots.
  scope: rate-based rules.
  link: [web-layer DDoS attacks](../facts/waf.md#waf-faq-rate-based-web-layer-ddos)
  link: [brute force login attempts](../facts/waf.md#waf-faq-rate-based-web-layer-ddos)
waf-faq-rule-propagation-about-a-minute
  claim: After an initial setup, adding or changing AWS WAF rules typically takes around a minute to propagate worldwide.
  scope: per rule change.
  link: [typically takes around a minute to propagate worldwide](../facts/waf.md#waf-faq-rule-propagation-about-a-minute)
waf-faq-sampled-requests-3-hours
  claim: AWS WAF Sampled Web Requests are stored for up to 3 hours.
  scope: Sampled Web Requests; maximum; not adjustable.
  link: [up to 3 hours](../facts/waf.md#waf-faq-sampled-requests-3-hours)
waf-faq-sqli-xss-protection
  claim: AWS WAF helps protect a website from common attack techniques like SQL injection and cross-site scripting (XSS).
  scope: AWS WAF.
  link: [SQL injection and Cross-Site Scripting (XSS)](../facts/waf.md#waf-faq-sqli-xss-protection)
waf-faq-supported-services
  claim: The AWS WAF FAQ lists Amazon CloudFront, the Application Load Balancer (ALB), Amazon API Gateway and AWS AppSync as the services AWS WAF can be deployed on.
  scope: the AWS WAF FAQ answer (the Developer Guide list in waf-protected-resource-types is longer).
  link: [Amazon API Gateway, and AWS AppSync](../facts/waf.md#waf-faq-supported-services)
waf-faq-supports-ipv6
  claim: AWS WAF can inspect HTTP/S requests coming from both IPv6 and IPv4 addresses.
  scope: per web request.
  link: [both IPv6 and IPv4 addresses](../facts/waf.md#waf-faq-supports-ipv6)
waf-forwarded-header-can-be-spoofed
  claim: A forwarded IP header can be modified by proxies along the way, and attackers might alter its contents to try to bypass AWS WAF inspections.
  scope: forwarded IP configuration.
  link: [Attackers might alter the contents of the header](../facts/waf.md#waf-forwarded-header-can-be-spoofed)
  link: [bypass AWS WAF inspections](../facts/waf.md#waf-forwarded-header-can-be-spoofed)
waf-forwarded-ip-default-origin-ip
  claim: By default, AWS WAF uses the IP address of the web request origin; behind proxies or load balancers this is the last proxy's address, and the client address is usually forwarded in another header, typically X-Forwarded-For.
  scope: rule statements that use the IP address; default; adjustable; forwarded IP configuration changes it.
  link: [the IP address from the web request origin](../facts/waf.md#waf-forwarded-ip-default-origin-ip)
  link: [the address of the last proxy](../facts/waf.md#waf-forwarded-ip-default-origin-ip)
  link: [typically `X-Forwarded-For` (XFF)](../facts/waf.md#waf-forwarded-ip-default-origin-ip)
waf-forwarded-ip-statements
  claim: You can tell AWS WAF to use a forwarded IP address, from X-Forwarded-For or another HTTP header, for the IP set match, geo match, ASN match and rate-based rule statements.
  scope: IP set, geo, ASN and rate-based statements.
  link: [use a forwarded IP address](../facts/waf.md#waf-forwarded-ip-statements)
waf-forwards-requests-then-block-or-allow
  claim: The underlying service forwards the requests it receives to AWS WAF for inspection against your rules; once a request meets a condition defined in your rules, AWS WAF instructs the underlying service to either block or allow the request based on the action you define.
  scope: per protected resource.
  link: [forwards those requests to AWS WAF for inspection](../facts/waf.md#waf-forwards-requests-then-block-or-allow)
  link: [to either block or allow the request](../facts/waf.md#waf-forwards-requests-then-block-or-allow)
waf-geo-match-countries-max
  claim: One geo match statement can list at most 50 country codes.
  scope: per geo match statement; maximum; not adjustable.
  link: [50](../facts/waf.md#waf-geo-match-countries-max)
  say: fifty country codes
waf-geo-match-country-and-region
  claim: A geo match statement manages web requests by country and region of origin; it adds country and region labels to every request it evaluates, whether or not the statement matches, and matches against the country of origin.
  scope: per rule statement.
  link: [based on country and region of origin](../facts/waf.md#waf-geo-match-country-and-region)
waf-geo-region-needs-label-match
  claim: A geo match rule alone cannot match against region codes (below country level); to manage requests by region of origin you use a geo match rule followed by a label match rule.
  scope: per web ACL.
  link: [You can't use a geo match rule alone](../facts/waf.md#waf-geo-region-needs-label-match)
waf-geo-uses-ip-maxmind
  claim: AWS WAF determines the location of requests using MaxMind GeoIP databases.
  scope: geo match statements.
  link: [using MaxMind GeoIP databases](../facts/waf.md#waf-geo-uses-ip-maxmind)
waf-global-cloudfront-equals-us-east-1
  claim: Choosing the Region option "Global (CloudFront)" in an interface is identical to choosing US East (N. Virginia), us-east-1.
  scope: AWS WAF console and APIs.
  link: [identical to choosing Region US East (N. Virginia)](../facts/waf.md#waf-global-cloudfront-equals-us-east-1)
waf-ip-reputation-list-group
  claim: The Amazon IP reputation list managed rule group is based on Amazon internal threat intelligence and is useful to block IP addresses typically associated with bots or other threats.
  scope: AWSManagedRulesAmazonIpReputationList.
  link: [based on Amazon internal threat intelligence](../facts/waf.md#waf-ip-reputation-list-group)
  link: [typically associated with bots or other threats](../facts/waf.md#waf-ip-reputation-list-group)
waf-ip-set-cidr-ipv4-ipv6-not-slash-0
  claim: In an IP set you enter IP addresses or ranges in CIDR notation; AWS WAF supports all IPv4 and IPv6 CIDR ranges except /0.
  scope: per IP set.
  link: [in CIDR notation](../facts/waf.md#waf-ip-set-cidr-ipv4-ipv6-not-slash-0)
  link: [supports all IPv4 and IPv6 CIDR ranges except for `/0`](../facts/waf.md#waf-ip-set-cidr-ipv4-ipv6-not-slash-0)
waf-ip-set-collection-of-addresses
  claim: An IP set is a collection of IP addresses and IP address ranges that you use together in a rule statement; you create the IPSet resource first and then reference it from an IP set rule statement in a web ACL or rule group.
  scope: per IP set.
  link: [collection of IP addresses and IP address ranges](../facts/waf.md#waf-ip-set-collection-of-addresses)
  link: [you reference the set](../facts/waf.md#waf-ip-set-collection-of-addresses)
waf-ip-set-global-for-cloudfront
  claim: Regional IP sets can be used only in web ACLs that protect regional resources; to use an IP set in a web ACL that protects CloudFront distributions, you must create it in Global (CloudFront).
  scope: per IP set.
  link: [You can use regional IP sets only](../facts/waf.md#waf-ip-set-global-for-cloudfront)
  link: [you must use Global (CloudFront)](../facts/waf.md#waf-ip-set-global-for-cloudfront)
waf-ip-set-max-addresses
  claim: One IP set can hold at most 10,000 IP addresses or IP address ranges in CIDR notation; this quota is fixed.
  scope: per IP set; maximum; not adjustable.
  link: [10,000](../facts/waf.md#waf-ip-set-max-addresses)
  say: ten thousand addresses or ranges
waf-known-bad-inputs-group
  claim: The Known bad inputs managed rule group blocks request patterns that are known to be invalid and are associated with exploitation or discovery of vulnerabilities.
  scope: AWSManagedRulesKnownBadInputsRuleSet.
  link: [known to be invalid](../facts/waf.md#waf-known-bad-inputs-group)
  link: [associated with exploitation or discovery of vulnerabilities](../facts/waf.md#waf-known-bad-inputs-group)
waf-log-destination-name-prefix
  claim: When you enable logging for a web ACL, you must choose a logging destination whose name begins with aws-waf-logs-, and you are charged for logging in addition to AWS WAF charges.
  scope: per web ACL logging configuration.
  link: [whose name begins with `aws-waf-logs-`](../facts/waf.md#waf-log-destination-name-prefix)
  link: [You are charged for logging](../facts/waf.md#waf-log-destination-name-prefix)
waf-logging-destinations-three
  claim: You can send web ACL logs to an Amazon CloudWatch Logs log group, an Amazon S3 bucket, or an Amazon Data Firehose delivery stream; the logs include when AWS WAF received the request, request details and the rules it matched.
  scope: per web ACL; logging enabled on the web ACL.
  link: [an Amazon CloudWatch Logs log group](../facts/waf.md#waf-logging-destinations-three)
  link: [an Amazon Simple Storage Service (Amazon S3) bucket](../facts/waf.md#waf-logging-destinations-three)
  link: [an Amazon Data Firehose delivery stream](../facts/waf.md#waf-logging-destinations-three)
waf-managed-paid-groups-bot-atp-acfp
  claim: The AWS Managed Rules groups for Bot Control, Fraud Control account takeover prevention (ATP) and account creation fraud prevention (ACFP) are available for additional fees beyond the basic AWS WAF charges, and you are also charged additional fees when you use the Anti-DDoS managed rule group (AWSManagedRulesAntiDDoSRuleSet).
  scope: AWS Managed Rules rule groups.
  link: [are available for additional fees](../facts/waf.md#waf-managed-paid-groups-bot-atp-acfp)
  link: [charged additional fees](../facts/waf.md#waf-managed-paid-groups-bot-atp-acfp)
waf-managed-rule-groups-definition
  claim: Managed rule groups are collections of predefined, ready-to-use rules that AWS and AWS Marketplace sellers write and maintain for you; basic AWS WAF pricing applies to the use of any managed rule group.
  scope: managed rule groups.
  link: [collections of predefined, ready-to-use rules](../facts/waf.md#waf-managed-rule-groups-definition)
  link: [AWS and AWS Marketplace sellers write and maintain](../facts/waf.md#waf-managed-rule-groups-definition)
waf-managed-rules-auto-updated
  claim: Many AWS and AWS Marketplace sellers automatically update managed rule groups and provide new versions when new vulnerabilities and threats emerge.
  scope: managed rule groups.
  link: [automatically update managed rule groups](../facts/waf.md#waf-managed-rules-auto-updated)
waf-managed-rules-cannot-view-details
  claim: You cannot view all the details of the individual rules inside a managed rule group, to protect the providers' intellectual property and to keep attackers from designing threats that circumvent published rules.
  scope: managed rule groups.
  link: [you can't view all of the details](../facts/waf.md#waf-managed-rules-cannot-view-details)
waf-managed-rules-not-replace-responsibility
  claim: AWS Managed Rules groups add another layer of security for applications but are not intended as a replacement for your own security responsibilities under the shared responsibility model.
  scope: AWS Managed Rules.
  link: [add another layer of security](../facts/waf.md#waf-managed-rules-not-replace-responsibility)
  link: [aren't intended as a replacement](../facts/waf.md#waf-managed-rules-not-replace-responsibility)
waf-managed-rules-usually-block
  claim: Managed rule group rules usually use the Block action, but not all do; for example, some Bot Control rules use the CAPTCHA and Challenge actions.
  scope: managed rule groups.
  link: [the Block action, but not all do](../facts/waf.md#waf-managed-rules-usually-block)
waf-marketplace-fms-each-account-subscribes
  claim: To use an AWS Marketplace rule group in a Firewall Manager AWS WAF policy, each account in the organization must subscribe to it.
  scope: Firewall Manager AWS WAF policies.
  link: [each account in your organization must subscribe](../facts/waf.md#waf-marketplace-fms-each-account-subscribes)
waf-marketplace-pricing-monthly-plus-requests
  claim: A subscribed AWS Marketplace rule group is charged a monthly fee (prorated hourly) plus ongoing request fees based on volume, and the subscription fee is charged only when you add the group to a web ACL and begin using it.
  scope: AWS Marketplace rule groups.
  link: [a monthly fee (prorated hourly)](../facts/waf.md#waf-marketplace-pricing-monthly-plus-requests)
  link: [ongoing request fees based on volume](../facts/waf.md#waf-marketplace-pricing-monthly-plus-requests)
waf-marketplace-rule-groups-subscription
  claim: AWS Marketplace rule groups are available by subscription through AWS Marketplace, and each is owned and managed by the AWS Marketplace seller.
  scope: AWS Marketplace rule groups.
  link: [available by subscription through AWS Marketplace](../facts/waf.md#waf-marketplace-rule-groups-subscription)
  link: [owned and managed by the AWS Marketplace seller](../facts/waf.md#waf-marketplace-rule-groups-subscription)
waf-max-reference-statements
  claim: A web ACL can hold at most 50 reference statements (to rule groups, IP sets or regex pattern sets), and a rule group at most 50 (to IP sets or regex pattern sets).
  scope: per web ACL; per rule group; maximum; not adjustable.
  link: [50](../facts/waf.md#waf-max-reference-statements)
  say: fifty reference statements
waf-max-wcu-per-rule-group
  claim: A rule group can have a capacity of at most 5,000 WCUs; this quota is fixed.
  scope: per rule group; maximum; not adjustable.
  link: [5,000 WCUs](../facts/waf.md#waf-max-wcu-per-rule-group)
  say: five thousand W C Us
waf-max-wcu-per-web-acl
  claim: A web ACL (protection pack) can use at most 5,000 WCUs (web ACL capacity units); this quota is fixed and cannot be changed.
  scope: per web ACL; maximum; not adjustable.
  link: [5,000 WCUs](../facts/waf.md#waf-max-wcu-per-web-acl)
  say: five thousand W C Us
waf-missing-header-no-match
  claim: In a rule statement that uses a forwarded IP configuration, if the header is missing, AWS WAF evaluates any statement that uses that header as No match (a NOT statement converts the No match result to Match); missing headers do not trigger the forwarded IP fallback behavior, only invalid header values do.
  scope: statements that use a forwarded IP configuration; header absent from the request.
  link: [evaluates any statement that uses that header](../facts/waf.md#waf-missing-header-no-match)
  link: [Missing headers don't trigger fallback behavior](../facts/waf.md#waf-missing-header-no-match)
waf-no-alb-on-outposts
  claim: You can associate a web ACL only with an Application Load Balancer within AWS Regions; you cannot associate one with an Application Load Balancer on AWS Outposts.
  scope: Application Load Balancers.
  link: [an Application Load Balancer within AWS Regions](../facts/waf.md#waf-no-alb-on-outposts)
  link: [Application Load Balancer that is on AWS Outposts](../facts/waf.md#waf-no-alb-on-outposts)
waf-no-body-inspection-for-grpc
  claim: AWS WAF does not support request body inspection rules for gRPC traffic; gRPC requests ignore those rules, while all other AWS WAF rules still apply.
  scope: web ACLs for CloudFront distributions or Application Load Balancers; gRPC traffic.
  link: [does not support request body inspection rules](../facts/waf.md#waf-no-body-inspection-for-grpc)
  link: [All other AWS WAF rules will still apply.](../facts/waf.md#waf-no-body-inspection-for-grpc)
waf-one-web-acl-per-resource
  claim: You can associate each AWS resource with only one web ACL (protection pack); one web ACL can be associated with many resources (one-to-many).
  scope: per AWS resource.
  link: [with only one protection pack (web ACL)](../facts/waf.md#waf-one-web-acl-per-resource)
  link: [one-to-many](../facts/waf.md#waf-one-web-acl-per-resource)
waf-oversize-default-continue
  claim: In the AWS WAF console you must choose an oversize handling option; outside the console, the default option is Continue.
  scope: per rule statement; default; adjustable.
  link: [required to choose one of these handling options](../facts/waf.md#waf-oversize-default-continue)
  link: [Outside the console, the default option is Continue.](../facts/waf.md#waf-oversize-default-continue)
waf-oversize-handling-options
  claim: Oversize handling in a rule statement has three options: Continue inspects the contents within the size limits, Match applies the rule action without evaluating the inspection criteria, and No match continues with the rest of the rules as for any non-matching rule.
  scope: rule statements that inspect body, JSON body, headers or cookies.
  link: [contents that are within the size limits](../facts/waf.md#waf-oversize-handling-options)
  link: [applies the rule action to the request](../facts/waf.md#waf-oversize-handling-options)
  link: [like it would do for any non-matching rule](../facts/waf.md#waf-oversize-handling-options)
waf-oversize-host-limits-forwarding
  claim: AWS WAF does not support inspecting very large contents of the request body, headers or cookies, because the host service has count and size limits on what it forwards to AWS WAF.
  scope: body, headers and cookies components.
  link: [doesn't support inspecting very large contents](../facts/waf.md#waf-oversize-host-limits-forwarding)
  link: [has count and size limits](../facts/waf.md#waf-oversize-host-limits-forwarding)
waf-oversize-limits-apply-managed-groups
  claim: Component size and count limits apply to all rules in a web ACL, including rules in managed rule groups and in rule groups shared with you by another account.
  scope: per web ACL.
  link: [apply to all rules that you use](../facts/waf.md#waf-oversize-limits-apply-managed-groups)
waf-oversize-match-block-blocks
  claim: If a rule with the Block action uses the Match oversize option, it blocks any request whose inspected component is oversize.
  scope: per rule; oversize handling Match and rule action Block.
  link: [block a request whose inspected component is oversize](../facts/waf.md#waf-oversize-match-block-blocks)
waf-price-bot-control-free-requests
  claim: Common Bot Control includes the first 10 million requests per month for free, and Targeted Bot Control includes the first 1 million requests per month for free.
  scope: per month.
  link: [10 million requests](../facts/waf.md#waf-price-bot-control-free-requests)
  link: [1 million requests](../facts/waf.md#waf-price-bot-control-free-requests)
  say: ten million requests | one million requests
waf-price-extra-wcu-blocks
  claim: A web ACL is charged an additional $0.20 per million requests for each 500 WCUs that it uses beyond the default allocation of 1500.
  scope: per web ACL; list price on the AWS WAF pricing page; the page says pricing may vary across AWS Regions.
  link: [$0.20 per million requests](../facts/waf.md#waf-price-extra-wcu-blocks)
  link: [each 500 WCUs](../facts/waf.md#waf-price-extra-wcu-blocks)
  say: twenty cents per million requests | each five hundred W C Us
waf-price-fraud-control-subscription
  claim: AWS WAF Fraud Control adds a subscription fee of $10 per month per WebACL, in addition to a request fee for the requests it analyzes.
  scope: per web ACL.
  link: [$10 per month per WebACL](../facts/waf.md#waf-price-fraud-control-subscription)
  say: ten dollars per month per web ACL
waf-price-requests
  claim: AWS WAF charges for the web requests that a web ACL processes; the pricing examples use $0.60 per million requests.
  scope: per web ACL; base request price for a web ACL within 1,500 WCUs and the default body inspection limit; prices may vary across AWS Regions.
  link: [$0.60 per million requests](../facts/waf.md#waf-price-requests)
  say: sixty cents per million requests
waf-price-rule
  claim: Each rule that you add to a web ACL costs $1.00 per month, and each rule group or managed rule group that you add also costs $1.00 per month (prorated hourly).
  scope: per rule, per rule group; list prices from the AWS WAF pricing page; rules inside a rule group that you create are also charged; prices may vary across AWS Regions.
  link: [$1.00 per month](../facts/waf.md#waf-price-rule)
  say: one dollar per month
waf-price-web-acl
  claim: AWS WAF charges for each web ACL that you create; in the pricing example, one web ACL costs $5.00 for the month.
  scope: per web ACL; list prices from the AWS WAF pricing page examples; monthly fees are prorated hourly and pricing may vary across AWS Regions.
  link: [$5.00](../facts/waf.md#waf-price-web-acl)
  say: five dollars
waf-pricing-dimensions
  claim: With pay-as-you-go pricing, AWS WAF charges are based on the number of web ACLs you create, the number of rules per web ACL and the number of web requests received, with no upfront commitments, and they are in addition to Amazon CloudFront, Amazon Cognito, Application Load Balancer, Amazon API Gateway, AWS AppSync or AWS Shield Advanced pricing; a CloudFront distribution on a flat-rate pricing plan instead pays one monthly price.
  scope: AWS WAF; pay-as-you-go pricing; not a CloudFront distribution on a flat-rate pricing plan.
  link: [number of web access control lists (web ACLs)](../facts/waf.md#waf-pricing-dimensions)
  link: [the number of web requests that you receive](../facts/waf.md#waf-pricing-dimensions)
  link: [There are no upfront commitments.](../facts/waf.md#waf-pricing-dimensions)
waf-protect-sites-outside-aws-via-cloudfront
  claim: AWS WAF can protect websites not hosted in AWS, because it is integrated with Amazon CloudFront, which supports custom origins outside of AWS.
  scope: web ACLs on CloudFront distributions; the site is served through a CloudFront distribution.
  link: [supports custom origins outside of AWS](../facts/waf.md#waf-protect-sites-outside-aws-via-cloudfront)
  link: [integrated with Amazon CloudFront](../facts/waf.md#waf-protect-sites-outside-aws-via-cloudfront)
waf-protected-resource-types
  claim: A web ACL (protection pack) can protect Amazon CloudFront, Amazon API Gateway, Application Load Balancer, AWS AppSync, Amazon Cognito, AWS App Runner, AWS Amplify, Amazon CloudWatch, Amazon Bedrock AgentCore Gateway and AWS Verified Access resources; for API Gateway the protected resource type is the REST API.
  scope: per web ACL (protection pack).
  link: [Amazon CloudFront, Amazon API Gateway, Application Load Balancer](../facts/waf.md#waf-protected-resource-types)
  link: [AWS AppSync, Amazon Cognito, AWS App Runner](../facts/waf.md#waf-protected-resource-types)
  link: [Amazon API Gateway REST API](../facts/waf.md#waf-protected-resource-types)
waf-protection-pack-is-web-acl
  claim: Protection packs are the new console location for web ACLs; they simplify web ACL management in the console but do not change the underlying web ACL functionality, and the standard console and the API still work directly with web ACLs.
  scope: AWS WAF console.
  link: [they don't change the underlying web ACL functionality](../facts/waf.md#waf-protection-pack-is-web-acl)
  link: [the new location for web ACLs](../facts/waf.md#waf-protection-pack-is-web-acl)
waf-quota-alb-associations-per-web-acl
  claim: One web ACL (protection pack) can be associated with up to 100 Application Load Balancers by default.
  scope: per web ACL, per account per Region; default; adjustable.
  link: [100](../facts/waf.md#waf-quota-alb-associations-per-web-acl)
  say: one hundred load balancers
waf-quota-ip-sets-per-region
  claim: An AWS account can have up to 100 IP sets in each Region by default.
  scope: per account per Region; default; adjustable.
  link: [100 IP sets](../facts/waf.md#waf-quota-ip-sets-per-region)
  say: one hundred IP sets
waf-quota-list-resources-org-calls
  claim: All accounts in an organization together can call ListResourcesForWebACL at most 12 requests per second in a single Region for us-east-1, us-west-2 and eu-west-1, and 6 requests per second in other Regions; these quotas can't be changed.
  scope: per organization per Region; maximum; not adjustable.
  link: [12 requests per second](../facts/waf.md#waf-quota-list-resources-org-calls)
  link: [6 requests per second](../facts/waf.md#waf-quota-list-resources-org-calls)
  say: twelve requests per second | six requests per second
waf-quota-regex-pattern-sets-per-region
  claim: An AWS account can have up to 10 regex pattern sets in each Region by default.
  scope: per account per Region; default; adjustable.
  link: [10 regex pattern sets](../facts/waf.md#waf-quota-regex-pattern-sets-per-region)
  say: ten regex pattern sets
waf-quota-regional-associations-per-web-acl
  claim: One web ACL has a default quota of 100 associations for each of these resource types: API Gateway REST APIs, Amazon Cognito user pools, AWS AppSync GraphQL APIs, AWS App Runner services, AWS Verified Access instances and AWS Amplify.
  scope: per web ACL, per resource type; default; adjustable.
  link: [100](../facts/waf.md#waf-quota-regional-associations-per-web-acl)
  say: one hundred of each type
waf-quota-requests-per-second-per-web-acl
  claim: The default quota for requests per second per web ACL (protection pack) is 100,000 per account per Region.
  scope: per web ACL, per account per Region; default; adjustable; for CloudFront, the WAF quotas page says the maximum RPS for AWS WAF on CloudFront is set by CloudFront.
  link: [100,000](../facts/waf.md#waf-quota-requests-per-second-per-web-acl)
  say: one hundred thousand requests per second
waf-quota-rule-groups-per-region
  claim: An AWS account can have up to 100 rule groups in AWS WAF in each Region by default.
  scope: per account per Region; default; adjustable.
  link: [100 rule groups](../facts/waf.md#waf-quota-rule-groups-per-region)
  say: one hundred rule groups
waf-quota-web-acls-per-region
  claim: An AWS account can have up to 100 web ACLs (protection packs) in each Region by default; this is a default quota, so you can request an increase.
  scope: per account per Region; default; adjustable.
  link: [100 web ACLs](../facts/waf.md#waf-quota-web-acls-per-region)
  say: one hundred web ACLs
waf-rate-based-bot-control-targeted-alternative
  claim: You can also rate limit web requests with the targeted protection level of the Bot Control managed rule group, which incurs additional fees.
  scope: per web ACL.
  link: [the targeted protection level of the Bot Control](../facts/waf.md#waf-rate-based-bot-control-targeted-alternative)
  link: [incurs additional fees](../facts/waf.md#waf-rate-based-bot-control-targeted-alternative)
waf-rate-based-count-all-needs-scope-down
  claim: The Count all aggregation option counts and rate limits all requests that match the rule's scope-down statement, and it requires a scope-down statement.
  scope: per rate-based rule; aggregation option Count all.
  link: [This option requires a scope-down statement.](../facts/waf.md#waf-rate-based-count-all-needs-scope-down)
waf-rate-based-counts-and-limits
  claim: A rate-based rule counts incoming requests and rate limits them when they come too fast; it aggregates requests by your criteria and counts and rate limits each aggregate grouping based on its evaluation window, request limit and action settings.
  scope: per rate-based rule instance.
  link: [coming at too fast a rate](../facts/waf.md#waf-rate-based-counts-and-limits)
  link: [evaluation window, request limit, and action settings](../facts/waf.md#waf-rate-based-counts-and-limits)
waf-rate-based-default-key-ip
  claim: By default, a rate-based rule aggregates and rate limits requests by the request IP address; you can configure other aggregation keys and combinations, such as a forwarded IP address, the HTTP method or a query argument.
  scope: per rate-based rule; default; adjustable.
  link: [based on the request IP address](../facts/waf.md#waf-rate-based-default-key-ip)
  link: [various other aggregation keys and key combinations](../facts/waf.md#waf-rate-based-default-key-ip)
waf-rate-based-detection-delay
  claim: Requests can arrive at too high a rate for up to several minutes before AWS WAF detects and rate limits them, and a lower rate can last a while before AWS WAF stops rate limiting; usually this delay is below 30 seconds.
  scope: per rate-based rule; maximum; usual case below 30 seconds.
  link: [for up to several minutes](../facts/waf.md#waf-rate-based-detection-delay)
  link: [this delay is below 30 seconds](../facts/waf.md#waf-rate-based-detection-delay)
waf-rate-based-instance-tracked-separately
  claim: AWS WAF tracks each instance of a rate-based rule separately: the same rule settings in two web ACLs, or one rule group used in several places, give separate instances with their own counts.
  scope: per rate-based rule instance.
  link: [separately for each instance of a rate-based rule](../facts/waf.md#waf-rate-based-instance-tracked-separately)
  link: [gets its own tracking and management](../facts/waf.md#waf-rate-based-instance-tracked-separately)
waf-rate-based-ip-blocked-until-rate-falls
  claim: When an IP address breaches a rate-based rule's configured limit, its new requests are blocked until its request rate falls below the threshold.
  scope: per rate-based rule; rule action Block, IP aggregation.
  link: [the request rate falls below the configured threshold](../facts/waf.md#waf-rate-based-ip-blocked-until-rate-falls)
waf-rate-based-key-components-must-be-present
  claim: Every request component named in a rate-based rule's aggregation key must be present in a request for the rule to evaluate or rate limit that request.
  scope: per rate-based rule.
  link: [must be present in a web request](../facts/waf.md#waf-rate-based-key-components-must-be-present)
waf-rate-based-not-precise
  claim: AWS WAF rate limiting is designed to control high request rates and protect availability; it is not intended for precise request-rate limiting and does not guarantee an exact limit match.
  scope: rate-based rules.
  link: [It's not intended for precise request-rate limiting.](../facts/waf.md#waf-rate-based-not-precise)
  link: [does not guarantee an exact limit match](../facts/waf.md#waf-rate-based-not-precise)
waf-rate-based-rules-per-rule-group
  claim: A rule group can contain at most 4 rate-based rules; this quota is fixed.
  scope: per rule group; maximum; not adjustable.
  link: [4 rate-based rules](../facts/waf.md#waf-rate-based-rules-per-rule-group)
  say: four rate-based rules
waf-rate-based-rules-per-web-acl
  claim: A web ACL (protection pack) can contain at most 10 rate-based rules; this quota is fixed.
  scope: per web ACL; maximum; not adjustable.
  link: [10 rate-based rules](../facts/waf.md#waf-rate-based-rules-per-web-acl)
  say: ten rate-based rules
waf-rate-based-scope-down
  claim: To limit requests to a login page without affecting the rest of the site, you can create a rate-based rule with a scope-down statement that matches requests to the login page and the request aggregation set to Count all.
  scope: per rate-based rule.
  link: [a rate-based rule with a scope-down statement](../facts/waf.md#waf-rate-based-scope-down)
  link: [traffic to the rest of your site](../facts/waf.md#waf-rate-based-scope-down)
waf-rate-based-scope-down-optional-or-required
  claim: The scope-down statement of a rate-based rule can be optional or required, depending on the rule's other configuration settings.
  scope: per rate-based rule; required with the Count all aggregation option.
  link: [can be optional or required](../facts/waf.md#waf-rate-based-scope-down-optional-or-required)
waf-rate-based-settings-change-resets-counts
  claim: Changing any rate limit setting of a rate-based rule in use resets its rate limiting counts, which can pause its rate limiting for up to a minute.
  scope: per rate-based rule; maximum; a rate limit setting is changed.
  link: [the change resets the rule's rate limiting counts](../facts/waf.md#waf-rate-based-settings-change-resets-counts)
  link: [for up to a minute](../facts/waf.md#waf-rate-based-settings-change-resets-counts)
waf-rate-limit-minimum
  claim: The lowest rate limit that a rate-based rule accepts is 10; before August 30, 2024 the minimum request rate was 100.
  scope: per rate-based rule; minimum; not adjustable; the rate limit counts requests in the rule's evaluation window.
  link: [10](../facts/waf.md#waf-rate-limit-minimum)
  link: [100](../facts/waf.md#waf-rate-limit-minimum)
  say: ten requests | one hundred requests
  changed: 2024-08-30: was 100
waf-rate-limited-ips-per-rule
  claim: One rate-based rule can rate limit at most 10,000 unique IP addresses at a time; this quota is fixed.
  scope: per rate-based rule; maximum; not adjustable.
  link: [10,000](../facts/waf.md#waf-rate-limited-ips-per-rule)
  say: ten thousand IP addresses
waf-rate-window-options
  claim: The evaluation window of a rate-based rule can be 1 minute, 2 minutes, 5 minutes or 10 minutes, and 5 minutes is the default; before February 28, 2024 the only option was 5 minutes.
  scope: per rate-based rule; default; adjustable; the window sets how far back AWS WAF counts, not how often it checks.
  link: [5 minutes](../facts/waf.md#waf-rate-window-options)
  link: [10 minutes](../facts/waf.md#waf-rate-window-options)
  link: [1 minute](../facts/waf.md#waf-rate-window-options)
  say: five minutes | ten minutes | one minute
  changed: 2024-02-28: was 5 minutes
waf-regex-patterns-per-set
  claim: A regex pattern set can hold at most 10 unique regex patterns.
  scope: per regex pattern set; maximum; not adjustable.
  link: [10](../facts/waf.md#waf-regex-patterns-per-set)
  say: ten patterns
waf-regional-data-stays-in-region
  claim: When AWS WAF monitors and manages web requests for a protected regional resource, it keeps all data in the same Region as the protected resource.
  scope: protected regional resources.
  link: [keeps all data in the same Region](../facts/waf.md#waf-regional-data-stays-in-region)
waf-regional-rules-run-in-region-internal
  claim: When you use AWS WAF on regional services such as Application Load Balancer, Amazon API Gateway and AWS AppSync, your rules run in the Region and can protect internet-facing resources as well as internal resources.
  scope: web ACLs on regional resources.
  link: [your rules run in region](../facts/waf.md#waf-regional-rules-run-in-region-internal)
  link: [internet-facing resources as well as internal resources](../facts/waf.md#waf-regional-rules-run-in-region-internal)
waf-resource-level-ddos-alb-no-rule-group-charges
  claim: Resource-level DDoS protection adds immediate defense to Application Load Balancers without the charges of deploying AWS WAF managed rule groups, using AWS threat intelligence and traffic pattern analysis.
  scope: Application Load Balancers; web ACL associated with the ALB.
  link: [adds immediate defense to Application Load Balancers](../facts/waf.md#waf-resource-level-ddos-alb-no-rule-group-charges)
  link: [without incurring charges of deploying](../facts/waf.md#waf-resource-level-ddos-alb-no-rule-group-charges)
waf-resource-level-ddos-default-active-under-ddos
  claim: Active under DDoS is the default protective mode of resource-level DDoS protection and is recommended for most use cases; Always on is an optional mode that is always active once enabled.
  scope: resource-level DDoS protection for Application Load Balancers; default; adjustable.
  link: [is the default protective mode](../facts/waf.md#waf-resource-level-ddos-default-active-under-ddos)
  link: [an optional mode that is always active](../facts/waf.md#waf-resource-level-ddos-default-active-under-ddos)
waf-resource-level-ddos-needs-web-acl
  claim: You must associate a web ACL with an Application Load Balancer to enable resource-level DDoS protection; a web ACL with no configuration incurs no AWS WAF request charges, but then AWS WAF gives no sampled requests or CloudWatch metrics for that load balancer.
  scope: Application Load Balancers.
  link: [You must associate a web ACL](../facts/waf.md#waf-resource-level-ddos-needs-web-acl)
  link: [not incur charges from AWS WAF requests](../facts/waf.md#waf-resource-level-ddos-needs-web-acl)
waf-response-content-403-or-custom
  claim: Based on conditions you specify, such as source IP addresses or query string values, the protected resource responds with the requested content, with an HTTP 403 (Forbidden) status code, or with a custom response.
  scope: per protected resource.
  link: [an HTTP 403 status code (Forbidden)](../facts/waf.md#waf-response-content-403-or-custom)
  link: [or with a custom response](../facts/waf.md#waf-response-content-403-or-custom)
waf-rule-action-override-any-action
  claim: You can override the actions of the rules inside a rule group to any valid rule action, and matching requests are then handled exactly as if the rule's action were the override setting.
  scope: per rule group in a web ACL.
  link: [to any valid rule action](../facts/waf.md#waf-rule-action-override-any-action)
  link: [handled exactly as if the configured rule's action](../facts/waf.md#waf-rule-action-override-any-action)
waf-rule-group-override-not-alter-group
  claim: When you add a rule group to a web ACL you can override the actions it takes on matching requests; the override does not alter the rule group itself, only how AWS WAF uses it in that web ACL.
  scope: per rule group in a web ACL.
  link: [you can override the actions it takes](../facts/waf.md#waf-rule-group-override-not-alter-group)
  link: [doesn't alter the rule group itself](../facts/waf.md#waf-rule-group-override-not-alter-group)
waf-rule-not-a-resource
  claim: A rule is not an AWS WAF resource: it exists only in the context of a web ACL (protection pack) or a rule group, whereas a web ACL and a rule group are AWS WAF resources.
  scope: AWS WAF components.
  link: [A rule is not an AWS WAF resource.](../facts/waf.md#waf-rule-not-a-resource)
  link: [only exists in the context of](../facts/waf.md#waf-rule-not-a-resource)
waf-rule-priority-unique
  claim: Each rule in a web ACL must have a unique priority setting within that web ACL, and each rule in a rule group a unique priority within that rule group.
  scope: per web ACL or rule group.
  link: [a unique priority setting](../facts/waf.md#waf-rule-priority-unique)
  link: [within that rule group](../facts/waf.md#waf-rule-priority-unique)
waf-rules-evaluated-lowest-priority-first
  claim: AWS WAF evaluates the rules of a web ACL or rule group from the lowest numeric priority setting upward until it finds a match that terminates the evaluation or runs out of rules.
  scope: per web ACL or rule group.
  link: [from the lowest numeric priority setting on up](../facts/waf.md#waf-rules-evaluated-lowest-priority-first)
  link: [finds a match that terminates the evaluation](../facts/waf.md#waf-rules-evaluated-lowest-priority-first)
waf-security-lake-no-waf-charge
  claim: You can configure Amazon Security Lake to collect web ACL data, and AWS WAF does not charge for using this option (Security Lake pricing applies).
  scope: per web ACL.
  link: [AWS WAF doesn't charge you](../facts/waf.md#waf-security-lake-no-waf-charge)
waf-shield-decision-guide-roles
  claim: AWS Shield provides protection against DDoS attacks, and AWS WAF helps protect web applications from common web exploitation attacks.
  scope: AWS network and application protection services.
  link: [protection against Distributed Denial of Service (DDoS) attacks](../facts/waf.md#waf-shield-decision-guide-roles)
  link: [protect web applications from common web exploitation attacks](../facts/waf.md#waf-shield-decision-guide-roles)
waf-size-constraint-bytes-not-contents
  claim: A size constraint statement compares the number of bytes AWS WAF receives for a request component with a number you provide; it inspects only the size of the component, not its contents.
  scope: per rule statement.
  link: [compares the number of bytes](../facts/waf.md#waf-size-constraint-bytes-not-contents)
  link: [doesn't inspect the contents of the component](../facts/waf.md#waf-size-constraint-bytes-not-contents)
waf-sql-database-group
  claim: The SQL database managed rule group blocks request patterns associated with exploitation of SQL databases, like SQL injection attacks; evaluate it if your application interfaces with an SQL database.
  scope: AWSManagedRulesSQLiRuleSet.
  link: [like SQL injection attacks](../facts/waf.md#waf-sql-database-group)
  link: [if your application interfaces with an SQL database](../facts/waf.md#waf-sql-database-group)
waf-sqli-high-more-detection-more-false-positives
  claim: The HIGH sensitivity setting of the SQL injection statement detects more SQL injection attacks and is the recommended setting, but it generates more false positives.
  scope: per SQL injection rule statement.
  link: [detects more SQL injection attacks](../facts/waf.md#waf-sqli-high-more-detection-more-false-positives)
  link: [is the recommended setting](../facts/waf.md#waf-sqli-high-more-detection-more-false-positives)
  link: [generates more false positives](../facts/waf.md#waf-sqli-high-more-detection-more-false-positives)
waf-sqli-sensitivity-default-low
  claim: The SQL injection statement has a sensitivity level setting with the options LOW and HIGH; the default setting is LOW.
  scope: per SQL injection rule statement; default; adjustable.
  link: [The options are LOW and HIGH.](../facts/waf.md#waf-sqli-sensitivity-default-low)
  link: [The default setting is LOW.](../facts/waf.md#waf-sqli-sensitivity-default-low)
waf-sqli-statement-inspects-malicious-sql
  claim: An SQL injection rule statement inspects a web request component for malicious SQL code, which attackers insert to modify a database or extract data from it.
  scope: per rule statement.
  link: [inspects for malicious SQL code](../facts/waf.md#waf-sqli-statement-inspects-malicious-sql)
  link: [modify your database or extract data from it](../facts/waf.md#waf-sqli-statement-inspects-malicious-sql)
waf-standard-actions-no-extra-charge
  claim: AWS WAF supports the standard rule actions Allow, Block and Count at no additional charge, while CAPTCHA attempts and Challenge responses are charged per attempt or response.
  scope: AWS WAF rule actions.
  link: [Allow, Block, Count at no additional charge](../facts/waf.md#waf-standard-actions-no-extra-charge)
  link: [charged per each CAPTCHA attempt and Challenge response](../facts/waf.md#waf-standard-actions-no-extra-charge)
waf-string-match-max-characters
  claim: A string match statement can hold at most 200 characters, and each regex pattern at most 200 characters.
  scope: per string match statement; per regex pattern; maximum; not adjustable.
  link: [200](../facts/waf.md#waf-string-match-max-characters)
  say: two hundred characters
waf-terminating-vs-non-terminating
  claim: Rule actions are terminating or non-terminating; a terminating action stops the web ACL evaluation of the request and either lets it continue to the protected application or blocks it.
  scope: per rule.
  link: [stops the protection pack (web ACL) evaluation](../facts/waf.md#waf-terminating-vs-non-terminating)
  link: [terminating or non-terminating](../facts/waf.md#waf-terminating-vs-non-terminating)
waf-test-in-count-mode-before-production
  claim: Before deploying a web ACL for production traffic, AWS advises testing and tuning it in a staging or test environment, then testing and tuning the rules in count mode with production traffic before enabling them.
  scope: per web ACL rollout.
  link: [test and tune your rules in count mode](../facts/waf.md#waf-test-in-count-mode-before-production)
  link: [in a staging or testing environment](../facts/waf.md#waf-test-in-count-mode-before-production)
waf-test-managed-groups-follow-provider
  claim: AWS recommends that you test and tune any change to a web ACL before applying it to your website or web application traffic, including rule groups managed by someone else (AWS Managed Rules, AWS Marketplace and shared rule groups).
  scope: per web ACL.
  link: [test and tune any changes](../facts/waf.md#waf-test-managed-groups-follow-provider)
  link: [rule groups that are managed by someone else](../facts/waf.md#waf-test-managed-groups-follow-provider)
waf-text-transformations-max
  claim: One rule statement can apply at most 10 text transformations.
  scope: per rule statement; maximum; not adjustable.
  link: [10](../facts/waf.md#waf-text-transformations-max)
  say: ten text transformations
waf-vended-logs-included
  claim: AWS WAF includes 500 MB of CloudWatch Logs and vended logs ingestion for every 1 million WAF requests at no additional cost; usage beyond that is billed at WAF-specific vended logs pricing.
  scope: per 1 million WAF requests.
  link: [500 MB](../facts/waf.md#waf-vended-logs-included)
  link: [1 million WAF requests](../facts/waf.md#waf-vended-logs-included)
  say: five hundred megabytes | one million WAF requests
waf-vs-shield-deployment
  claim: AWS WAF must be explicitly set up, while AWS Shield Standard protection is included for all customer accounts.
  scope: AWS WAF compared with AWS Shield.
  link: [Must be explicitly set up](../facts/waf.md#waf-vs-shield-deployment)
  link: [Shield Standard protection included for all customer accounts](../facts/waf.md#waf-vs-shield-deployment)
waf-vs-shield-inspection-level
  claim: AWS WAF inspects traffic at the request level, while AWS Shield inspects at the packet level.
  scope: AWS WAF compared with AWS Shield.
  link: [Request-level](../facts/waf.md#waf-vs-shield-inspection-level)
  link: [Packet-level](../facts/waf.md#waf-vs-shield-inspection-level)
waf-vs-shield-layer
  claim: AWS WAF protects at the application layer (L7); AWS Shield protects at the network, transport and application layers (L3/L4/L7).
  scope: AWS WAF compared with AWS Shield.
  link: [Application layer (L7)](../facts/waf.md#waf-vs-shield-layer)
  link: [Network, transport, and application layers (L3/L4/L7)](../facts/waf.md#waf-vs-shield-layer)
waf-vs-shield-primary-purpose
  claim: AWS WAF protects against exploits on web applications (such as SQL injection or XSS), while AWS Shield protects against DDoS attacks (such as SYN or UDP floods).
  scope: AWS WAF compared with AWS Shield.
  link: [Protects against exploits on web applications](../facts/waf.md#waf-vs-shield-primary-purpose)
  link: [Protects against DDoS attacks](../facts/waf.md#waf-vs-shield-primary-purpose)
waf-wcu-included-1500
  claim: The basic web ACL price includes up to 1,500 WCUs; using more than 1,500 WCUs adds fees under a tiered pricing model.
  scope: per web ACL.
  link: [1,500 WCUs](../facts/waf.md#waf-wcu-included-1500)
  say: fifteen hundred W C Us
waf-web-acl-region-of-resource
  claim: A web ACL (protection pack) and any AWS WAF resources it uses must be in the Region where the associated resource is located; for CloudFront distributions this Region is US East (N. Virginia).
  scope: per web ACL.
  link: [the Region where the associated resource is located](../facts/waf.md#waf-web-acl-region-of-resource)
  link: [US East (N. Virginia)](../facts/waf.md#waf-web-acl-region-of-resource)
waf-xss-statement-inspects-malicious-scripts
  claim: An XSS attack statement inspects a web request component for malicious scripts; in an XSS attack, the attacker uses vulnerabilities in a benign website to inject malicious client-site scripts into other legitimate web browsers.
  scope: per rule statement.
  link: [inspects for malicious scripts](../facts/waf.md#waf-xss-statement-inspects-malicious-scripts)
  link: [inject malicious client-site scripts](../facts/waf.md#waf-xss-statement-inspects-malicious-scripts)
