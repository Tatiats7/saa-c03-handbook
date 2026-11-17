facts card: 305 facts
control-tower-10-scps-per-ou
  claim: A limit of 10 SCPs per OU applies to the OUs in an AWS Control Tower landing zone; AWS Organizations states that all policy limits are hard limits.
  scope: per OU in the landing zone; maximum; not adjustable.
  link: [ten (10) SCPs per OU](../facts/control-tower.md#control-tower-10-scps-per-ou)
  say: ten SCPs per OU
control-tower-100-concurrent-control-operations
  claim: Optional controls can be activated and deactivated concurrently, through an asynchronous process; up to 100 control-related operations can be in progress at a time, in total, whether called from the console or from an API.
  scope: AWS Control Tower optional control operations, console and API combined; maximum.
  link: [100](../facts/control-tower.md#control-tower-100-concurrent-control-operations)
  say: one hundred
control-tower-10000-accounts-per-landing-zone
  claim: AWS Control Tower supports up to 10,000 accounts in the landing zone's organization, divided among all of its OUs; the AWS Organizations quota page lists this AWS Control Tower limit of 10000 accounts as one that cannot be increased.
  scope: per landing zone organization, across all OUs; maximum; not adjustable.
  link: [10,000 accounts](../facts/control-tower.md#control-tower-10000-accounts-per-landing-zone)
  say: ten thousand accounts
control-tower-5-concurrent-account-operations
  claim: Account Factory can provision, update and enroll accounts concurrently, with up to 5 account-related operations in progress at once; unmanaging accounts must be done one account at a time. The concurrent account operations quota has a default of 5, is adjustable, and has a maximum of 10.
  scope: concurrent account operations in Account Factory; default; adjustable; unmanaging accounts is one account at a time; the quota can be raised to a maximum of 10.
  link: [five (5) account-related operations](../facts/control-tower.md#control-tower-5-concurrent-account-operations)
  link: [Maximum: 10](../facts/control-tower.md#control-tower-5-concurrent-account-operations)
  say: five account operations | a maximum of ten
control-tower-account-factory-on-service-catalog
  claim: Account Factory works as an account vending machine built on provisioned products in AWS Service Catalog.
  scope: AWS Control Tower Account Factory.
  link: [vending machine](../facts/control-tower.md#control-tower-account-factory-on-service-catalog)
  link: [provisioned products in AWS Service Catalog](../facts/control-tower.md#control-tower-account-factory-on-service-catalog)
control-tower-account-factory-template
  claim: Account Factory is a configurable account template that standardizes provisioning of new accounts with pre-approved configurations; it can create and enroll accounts and automatically applies controls and policies to them.
  scope: AWS Control Tower Account Factory.
  link: [a configurable account template](../facts/control-tower.md#control-tower-account-factory-template)
  link: [pre-approved account configurations](../facts/control-tower.md#control-tower-account-factory-template)
  link: [automates the process of applying controls and policies](../facts/control-tower.md#control-tower-account-factory-template)
control-tower-accounts-isolated-containers-blast-radius
  claim: AWS best practices recommend separating resources and workloads into multiple accounts, which act as isolated resource containers that categorize workloads and reduce the blast radius when things go wrong.
  scope: AWS multi-account strategy.
  link: [isolated resource containers](../facts/control-tower.md#control-tower-accounts-isolated-containers-blast-radius)
  link: [blast radius reduction when things go wrong](../facts/control-tower.md#control-tower-accounts-isolated-containers-blast-radius)
control-tower-accounts-outside-not-bound
  claim: New accounts created outside of Control Tower Account Factory are not bound by the registered OU's controls; existing accounts, and any new OUs or accounts that you create outside of Control Tower, are not bound by Control Tower controls unless you separately register the OU or enroll the account.
  scope: accounts and OUs created or kept outside Control Tower governance.
  link: [are not bound by the registered OU's controls](../facts/control-tower.md#control-tower-accounts-outside-not-bound)
  link: [separately register the OU or enroll the account](../facts/control-tower.md#control-tower-accounts-outside-not-bound)
control-tower-auto-enrollment-baseline-from-destination-ou
  claim: With the optional auto-enrollment feature, available for landing zone version 3.1 and above, an account moved into Control Tower automatically receives the baseline resources and control configurations of the destination OU; this applies to existing and newly created accounts.
  scope: per account moved into a registered OU; auto-enrollment turned on; landing zone version 3.1 and above.
  link: [automatically receives baseline resources](../facts/control-tower.md#control-tower-auto-enrollment-baseline-from-destination-ou)
  say: automatically receives baseline resources
control-tower-auto-enrollment-unenroll-by-moving
  claim: With auto-enrollment on, moving an account into a registered OU enrolls it with that OU's baseline and controls, for existing and newly created accounts; moving it to an unregistered OU or the root unenrolls it and Control Tower removes the baseline resources and controls.
  scope: Control Tower auto-enrollment; auto-enrollment enabled; landing zone 3.1 or later.
  link: [The account automatically receives baseline resources and controls](../facts/control-tower.md#control-tower-auto-enrollment-unenroll-by-moving)
  link: [an OU that is not registered](../facts/control-tower.md#control-tower-auto-enrollment-unenroll-by-moving)
  link: [removes all deployed baseline resources and controls automatically](../facts/control-tower.md#control-tower-auto-enrollment-unenroll-by-moving)
control-tower-billed-underlying-services
  claim: When you set up AWS Control Tower, AWS Organizations and IAM Identity Center come at no additional charge, but you pay by usage for services such as Service Catalog, CloudTrail, AWS Config, CloudWatch, SNS, S3 and Amazon VPC.
  scope: per landing zone; based on your usage of these services.
  link: [AWS Service Catalog, AWS CloudTrail, AWS Config](../facts/control-tower.md#control-tower-billed-underlying-services)
  say: Service Catalog, CloudTrail, AWS Config
control-tower-case-norstella-acquisitions-automation
  claim: Norstella provisions accounts with infrastructure as code instead of involving multiple teams, and when it acquires new businesses it uses AWS Control Tower automation to align their infrastructure.
  scope: Norstella case study.
  link: [an infrastructure-as-code approach to provision accounts](../facts/control-tower.md#control-tower-case-norstella-acquisitions-automation)
  link: [When Norstella acquires new businesses](../facts/control-tower.md#control-tower-case-norstella-acquisitions-automation)
control-tower-case-norstella-under-5-months
  claim: Norstella, created from the merger of five pharmaceutical solution providers, used AWS to build a scalable enterprise cloud environment from scratch, and used AWS Control Tower to complete its migration in under 5 months, a process that typically takes over 1 year.
  scope: Norstella case study.
  link: [under 5 months](../facts/control-tower.md#control-tower-case-norstella-under-5-months)
  link: [typically takes over 1 year](../facts/control-tower.md#control-tower-case-norstella-under-5-months)
  link: [used AWS Control Tower to complete its migration](../facts/control-tower.md#control-tower-case-norstella-under-5-months)
  say: under five months | typically takes over one year
control-tower-change-100-concurrent-control-ops-2024-05
  claim: On 2024-05-20 AWS Control Tower increased the concurrent control operations quota to 100.
  scope: per landing zone; maximum.
  link: [2024-05-20](../facts/control-tower.md#control-tower-change-100-concurrent-control-ops-2024-05)
  link: [100](../facts/control-tower.md#control-tower-change-100-concurrent-control-ops-2024-05)
  say: May twentieth, twenty twenty-four | one hundred
control-tower-change-1000-accounts-per-ou-2024-08
  claim: On 2024-08-30 AWS Control Tower increased the limit on accounts per OU, so an OU can hold up to 1000 accounts.
  scope: per OU; maximum.
  link: [2024-08-30](../facts/control-tower.md#control-tower-change-1000-accounts-per-ou-2024-08)
  link: [1000 accounts per OU](../facts/control-tower.md#control-tower-change-1000-accounts-per-ou-2024-08)
  say: August thirtieth, twenty twenty-four | one thousand accounts per OU
control-tower-change-auto-enrollment-2025-10
  claim: On 2025-10-15 AWS Control Tower added automatic account enrollment and moving accounts between OUs.
  scope: per landing zone.
  link: [2025-10-15](../facts/control-tower.md#control-tower-change-auto-enrollment-2025-10)
  link: [Automatic account enrollment](../facts/control-tower.md#control-tower-change-auto-enrollment-2025-10)
  say: October fifteenth, twenty twenty-five | automatic account enrollment
control-tower-change-backup-integration-2024-11
  claim: On 2024-11-25 AWS Control Tower integrated with AWS Backup, so you can set up plans to back up your AWS Control Tower resources.
  scope: per landing zone.
  link: [2024-11-25](../facts/control-tower.md#control-tower-change-backup-integration-2024-11)
  link: [integrates with AWS Backup](../facts/control-tower.md#control-tower-change-backup-integration-2024-11)
  say: November twenty-fifth, twenty twenty-four | integrates with AWS Backup
control-tower-change-declarative-controls-2024-12
  claim: On 2024-12-01 AWS Control Tower added preventive controls implemented with declarative policies, a new type of policy for a new type of preventive control.
  scope: per landing zone.
  link: [2024-12-01](../facts/control-tower.md#control-tower-change-declarative-controls-2024-12)
  link: [preventive controls with declarative policies](../facts/control-tower.md#control-tower-change-declarative-controls-2024-12)
  say: December first, twenty twenty-four | preventive controls with declarative policies
control-tower-change-landing-zone-3-org-trail-2022-07
  claim: On 2022-07-29 AWS Control Tower landing zone version 3.0 changed from account-based AWS CloudTrail trails to organization-based trails, and aggregates AWS Config information in the home Region only.
  scope: per landing zone; landing zone version 3.0.
  link: [2022-07-29](../facts/control-tower.md#control-tower-change-landing-zone-3-org-trail-2022-07)
  link: [account-based AWS CloudTrail trails](../facts/control-tower.md#control-tower-change-landing-zone-3-org-trail-2022-07)
  say: July twenty-ninth, twenty twenty-two | account-based CloudTrail trails
  changed: 2022-07-29: was account-based AWS CloudTrail trails
control-tower-change-landing-zone-4-2025-11
  claim: On 2025-11-17 AWS Control Tower landing zone version 4.0 became available, with optional service integrations and a dedicated controls environment.
  scope: per landing zone.
  link: [2025-11-17](../facts/control-tower.md#control-tower-change-landing-zone-4-2025-11)
  link: [a dedicated controls environment](../facts/control-tower.md#control-tower-change-landing-zone-4-2025-11)
  say: November seventeenth, twenty twenty-five | a dedicated controls environment
control-tower-change-proactive-controls-ga-2023-01
  claim: On 2023-01-24 AWS Control Tower proactive controls moved from preview to general availability.
  scope: per landing zone.
  link: [2023-01-24](../facts/control-tower.md#control-tower-change-proactive-controls-ga-2023-01)
  link: [Proactive controls generally available](../facts/control-tower.md#control-tower-change-proactive-controls-ga-2023-01)
  say: January twenty-fourth, twenty twenty-three | proactive controls generally available
control-tower-change-rcp-controls-2024-11
  claim: On 2024-11-15 AWS Control Tower launched managed controls implemented with resource control policies (RCPs), a new type of preventive control.
  scope: per landing zone.
  link: [2024-11-15](../facts/control-tower.md#control-tower-change-rcp-controls-2024-11)
  link: [implemented with RCPs](../facts/control-tower.md#control-tower-change-rcp-controls-2024-11)
  say: November fifteenth, twenty twenty-four | implemented with RCPs
control-tower-control-applies-to-whole-ou
  claim: A control applies to an entire OU, so every account in the OU is affected and users in any account of the landing zone are always subject to the controls of their account's OU.
  scope: AWS Control Tower controls.
  link: [applies to an entire organizational unit (OU)](../facts/control-tower.md#control-tower-control-applies-to-whole-ou)
  link: [every AWS account within the OU is affected](../facts/control-tower.md#control-tower-control-applies-to-whole-ou)
control-tower-control-types-mechanisms
  claim: Preventive controls are implemented with SCPs, RCPs and declarative policies; detective controls with AWS Config rules; proactive controls with CloudFormation hooks.
  scope: AWS Control Tower controls.
  link: [Resource Control Policies (RCPs), and declarative policies](../facts/control-tower.md#control-tower-control-types-mechanisms)
  link: [detective controls are implemented using AWS Config rules](../facts/control-tower.md#control-tower-control-types-mechanisms)
  link: [implemented using AWS CloudFormation hooks](../facts/control-tower.md#control-tower-control-types-mechanisms)
control-tower-detective-alerts-dashboard-status
  claim: A detective control detects noncompliant resources and alerts through the dashboard; its status is clear, in violation, or not enabled, and it applies only in Regions that Control Tower supports.
  scope: Control Tower detective controls.
  link: [provides alerts through the dashboard](../facts/control-tower.md#control-tower-detective-alerts-dashboard-status)
  link: [clear, in violation, or not enabled](../facts/control-tower.md#control-tower-detective-alerts-dashboard-status)
control-tower-detective-security-hub-standard
  claim: Integrated detective Security Hub CSPM controls are implemented with AWS Config rules and are owned by the Service-Managed Standard: AWS Control Tower in Security Hub CSPM.
  scope: Control Tower detective controls.
  link: [implemented using AWS Config rules](../facts/control-tower.md#control-tower-detective-security-hub-standard)
  link: [Service-Managed Standard: AWS Control Tower](../facts/control-tower.md#control-tower-detective-security-hub-standard)
control-tower-drift-detected-automatically
  claim: Control Tower detects drift automatically; drift for a member account is surfaced in Amazon SNS notifications that are aggregated in the audit account, but these SNS notifications are not available when the auto-enroll capability for accounts is enabled.
  scope: Control Tower drift; the SNS drift notifications are not available when auto-enroll is enabled.
  link: [AWS Control Tower detects drift automatically](../facts/control-tower.md#control-tower-drift-detected-automatically)
  link: [aggregated in the audit account](../facts/control-tower.md#control-tower-drift-detected-automatically)
control-tower-drift-reset-landing-zone
  claim: Most drift can be resolved by administrators, but a few types must be resolved immediately: deleting the Security OU or the required Control Tower IAM roles gives an error that tells you to reset the landing zone, and moving a shared account out of a foundational OU creates Move Account drift that you remediate by updating the landing zone.
  scope: Control Tower drift.
  link: [Most types of drift can be resolved](../facts/control-tower.md#control-tower-drift-reset-landing-zone)
  link: [instructing you to reset the landing zone immediately](../facts/control-tower.md#control-tower-drift-reset-landing-zone)
  link: [you must update the landing zone](../facts/control-tower.md#control-tower-drift-reset-landing-zone)
control-tower-easiest-way-secure-multi-account
  claim: AWS describes Control Tower as the easiest way to set up and govern a secure, compliant, multi-account AWS environment based on best practices.
  scope: AWS Control Tower.
  link: [the easiest way to set up and govern](../facts/control-tower.md#control-tower-easiest-way-secure-multi-account)
  link: [a secure, compliant, multi-account AWS environment](../facts/control-tower.md#control-tower-easiest-way-secure-multi-account)
control-tower-enablecontrol-10-in-progress
  claim: For the EnableControl and DisableControl APIs the limit is 100 concurrent operations, of which 10 can be in progress simultaneously while the rest are queued.
  scope: EnableControl and DisableControl API calls in AWS Control Tower; maximum; remaining operations are queued.
  link: [one hundred (100) concurrent operations](../facts/control-tower.md#control-tower-enablecontrol-10-in-progress)
  link: [Ten operations (10)](../facts/control-tower.md#control-tower-enablecontrol-10-in-progress)
  say: one hundred concurrent operations | ten operations
control-tower-enroll-needs-execution-role-no-config
  claim: To enroll an existing account, it must have the AWSControlTowerExecution role and must not have existing AWS Config resources; an existing account cannot become the audit or log archive account except during initial setup.
  scope: enrolling an existing account into Control Tower.
  link: [that account must have the AWSControlTowerExecution role enabled](../facts/control-tower.md#control-tower-enroll-needs-execution-role-no-config)
  link: [must not have existing AWS Config resources](../facts/control-tower.md#control-tower-enroll-needs-execution-role-no-config)
  link: [except during initial landing zone setup](../facts/control-tower.md#control-tower-enroll-needs-execution-role-no-config)
control-tower-enrollment-applies-baseline-config
  claim: Enrolling an account applies mandatory controls to it through the SCPs of the selected OU, enables AWS Config and configures it to record all resources in the account, and adds the AWS Config rules that apply the Control Tower detective controls.
  scope: account enrollment into Control Tower.
  link: [Applies mandatory controls to the account](../facts/control-tower.md#control-tower-enrollment-applies-baseline-config)
  link: [configures it to record all resources](../facts/control-tower.md#control-tower-enrollment-applies-baseline-config)
control-tower-ephemeral-workloads-raise-config-costs
  claim: Running ephemeral workloads from accounts in AWS Control Tower can increase AWS Config costs, because AWS Config records the configuration changes of creating and deleting these temporary resources.
  scope: per enrolled account; ephemeral workloads such as Spot Instances, EMR jobs and Auto Scaling.
  link: [increase in costs from AWS Config](../facts/control-tower.md#control-tower-ephemeral-workloads-raise-config-costs)
  say: an increase in AWS Config costs
control-tower-existing-org-one-landing-zone
  claim: In an existing organization you can have one landing zone per organization; Control Tower uses the existing management account and sets up a new audit account and logging account in a registered OU.
  scope: Control Tower in an existing organization.
  link: [one landing zone per AWS Organizations organization](../facts/control-tower.md#control-tower-existing-org-one-landing-zone)
  link: [No new management account is needed](../facts/control-tower.md#control-tower-existing-org-one-landing-zone)
  link: [an audit account and a logging account](../facts/control-tower.md#control-tower-existing-org-one-landing-zone)
control-tower-extends-organizations
  claim: Control Tower orchestration extends the capabilities of AWS Organizations and applies controls (guardrails) to keep organizations and accounts from drifting away from best practices.
  scope: AWS Control Tower and AWS Organizations.
  link: [extends the capabilities of AWS Organizations](../facts/control-tower.md#control-tower-extends-organizations)
  link: [AWS Control Tower applies controls](../facts/control-tower.md#control-tower-extends-organizations)
control-tower-faq-api-available-console-for-rest
  claim: AWS Control Tower has an API; operations that the API does not cover are done in the Control Tower console.
  scope: AWS Control Tower API.
  link: [use the AWS Control Tower console](../facts/control-tower.md#control-tower-faq-api-available-console-for-rest)
control-tower-faq-built-on-organizations-scps-rcps
  claim: AWS Control Tower is built on AWS Organizations; it sets up account structures automatically and implements preventive guardrails with SCPs and RCPs.
  scope: AWS Control Tower.
  link: [preventive guardrails using SCPs and RCPs](../facts/control-tower.md#control-tower-faq-built-on-organizations-scps-rcps)
control-tower-faq-cfct-and-aft-customizations
  claim: Customizations for AWS Control Tower (CfCT) and Account Factory for Terraform (AFT) add customizations to Control Tower accounts with CloudFormation templates, SCPs or Terraform.
  scope: accounts governed by AWS Control Tower.
  link: [Customizations for AWS Control Tower (CfCT)](../facts/control-tower.md#control-tower-faq-cfct-and-aft-customizations)
  link: [Account Factory for Terraform (AFT)](../facts/control-tower.md#control-tower-faq-cfct-and-aft-customizations)
control-tower-faq-complementary-to-security-hub
  claim: AWS Control Tower and AWS Security Hub CSPM are complementary, and AWS says to use Control Tower preventive controls together with Security Hub detective controls.
  scope: AWS Control Tower with Security Hub CSPM.
  link: [complementary services](../facts/control-tower.md#control-tower-faq-complementary-to-security-hub)
  link: [preventive controls in combination with](../facts/control-tower.md#control-tower-faq-complementary-to-security-hub)
control-tower-faq-customize-accounts-account-factory
  claim: Control Tower can customize new and existing accounts when you provision their resources from the Control Tower console, and the customized accounts are provisioned in account factory.
  scope: new and existing Control Tower accounts.
  link: [provisioned in account factory](../facts/control-tower.md#control-tower-faq-customize-accounts-account-factory)
control-tower-faq-full-landing-zone-or-controls-only
  claim: Customers can either follow a guided route to a full well-architected environment or directly enable AWS managed controls in their existing organization.
  scope: organizations adopting AWS Control Tower.
  link: [directly enabling AWS managed controls](../facts/control-tower.md#control-tower-faq-full-landing-zone-or-controls-only)
control-tower-faq-identity-center-default-directory
  claim: Control Tower sets up IAM Identity Center with a native default directory; after landing zone setup you can connect a supported directory such as AWS Managed Microsoft AD, or manage access control yourself.
  scope: landing zone identity setup.
  link: [IAM Identity Center with a native default directory](../facts/control-tower.md#control-tower-faq-identity-center-default-directory)
  link: [such as AWS Managed Microsoft AD](../facts/control-tower.md#control-tower-faq-identity-center-default-directory)
control-tower-faq-landing-zone-sets-ous-config-cloudtrail
  claim: The Control Tower landing zone sets up the Organizations structure with recommended OUs, configures AWS Config and CloudTrail, and implements guardrails across accounts.
  scope: AWS Control Tower landing zone.
  link: [recommended organizational units (OUs)](../facts/control-tower.md#control-tower-faq-landing-zone-sets-ous-config-cloudtrail)
  link: [configures core security services like AWS Config](../facts/control-tower.md#control-tower-faq-landing-zone-sets-ous-config-cloudtrail)
control-tower-faq-mandatory-and-optional-controls
  claim: Control Tower applies mandatory and optional high-level rules, called controls, that help enforce your policies.
  scope: AWS Control Tower controls.
  link: [mandatory and optional high-level rules, called controls](../facts/control-tower.md#control-tower-faq-mandatory-and-optional-controls)
control-tower-faq-organizations-framework-control-tower-layer
  claim: AWS describes Organizations as the framework and Control Tower as the automation and governance layer on top of it.
  scope: AWS Organizations and AWS Control Tower.
  link: [Organizations as the framework](../facts/control-tower.md#control-tower-faq-organizations-framework-control-tower-layer)
  link: [automation and governance layer](../facts/control-tower.md#control-tower-faq-organizations-framework-control-tower-layer)
control-tower-faq-pay-for-config-rules-of-detective-controls
  claim: You also pay for the services that deploy controls, such as the AWS Config rules that Control Tower sets up for detective controls.
  scope: Control Tower detective controls.
  link: [AWS Config rules](../facts/control-tower.md#control-tower-faq-pay-for-config-rules-of-detective-controls)
control-tower-faq-region-deny-customizable
  claim: You can customize the Control Tower Region deny control to apply the Regional restrictions that your business needs.
  scope: Control Tower Region deny control.
  link: [Region deny control](../facts/control-tower.md#control-tower-faq-region-deny-customizable)
control-tower-faq-who-should-use
  claim: AWS Control Tower is designed for organizations that manage multiple AWS accounts and need centralized governance and automated policy enforcement.
  scope: AWS Control Tower.
  link: [organizations managing multiple AWS accounts](../facts/control-tower.md#control-tower-faq-who-should-use)
  link: [centralized governance and automated policy enforcement](../facts/control-tower.md#control-tower-faq-who-should-use)
control-tower-guardrail-renamed-control
  claim: Control Tower now uses the term control; the earlier term guardrail means the same thing.
  scope: AWS Control Tower terminology.
  link: [These terms are synonymous for our purposes](../facts/control-tower.md#control-tower-guardrail-renamed-control)
  link: [the previous term, guardrail](../facts/control-tower.md#control-tower-guardrail-renamed-control)
control-tower-guidance-levels
  claim: Control guidance has three categories: mandatory controls protect resources that Control Tower deploys, strongly recommended controls enforce common best practices, and elective controls track or lock down commonly restricted actions; the last two apply at the OU level.
  scope: AWS Control Tower control guidance.
  link: [These controls protect AWS Control Tower-deployed resources](../facts/control-tower.md#control-tower-guidance-levels)
  link: [enforce some common best practices](../facts/control-tower.md#control-tower-guidance-levels)
  link: [track or lock down actions](../facts/control-tower.md#control-tower-guidance-levels)
control-tower-landing-zone-definition
  claim: A landing zone is a well-architected multi-account environment based on security and compliance best practices; it holds all OUs, accounts, users and other resources that you want under compliance regulation.
  scope: AWS Control Tower landing zone.
  link: [a well-architected, multi-account environment](../facts/control-tower.md#control-tower-landing-zone-definition)
  link: [the enterprise-wide container](../facts/control-tower.md#control-tower-landing-zone-definition)
control-tower-landing-zone-setup-actions
  claim: When it sets up a landing zone through the console, Control Tower creates the Security OU and an optional Sandbox OU, creates an IAM Identity Center directory (or lets you self-manage your identity provider), and applies all mandatory preventive and detective controls; starting with landing zone version 4.0, mandatory controls are no longer applied by default.
  scope: landing zone set up through the console; starting with landing zone version 4.0, mandatory controls are no longer applied by default.
  link: [the Security OU and the optional Sandbox OU](../facts/control-tower.md#control-tower-landing-zone-setup-actions)
  link: [Creates a cloud-native directory in IAM Identity Center](../facts/control-tower.md#control-tower-landing-zone-setup-actions)
  link: [allows you to self-manage your identity provider](../facts/control-tower.md#control-tower-landing-zone-setup-actions)
control-tower-log-archive-and-audit-roles
  claim: The log archive account is a repository for API activity and resource configuration logs from all accounts; the audit account is a restricted account that gives security and compliance teams read and write access to all accounts.
  scope: Control Tower shared accounts.
  link: [a repository for logs of API activities](../facts/control-tower.md#control-tower-log-archive-and-audit-roles)
  link: [a restricted account](../facts/control-tower.md#control-tower-log-archive-and-audit-roles)
  link: [your security and compliance teams](../facts/control-tower.md#control-tower-log-archive-and-audit-roles)
control-tower-logs-all-actions-including-management
  claim: Control Tower logs actions automatically through CloudTrail and AWS Config, including actions from the management account and from member accounts.
  scope: Control Tower landing zone.
  link: [All actions are logged](../facts/control-tower.md#control-tower-logs-all-actions-including-management)
  link: [actions from the AWS Control Tower management account](../facts/control-tower.md#control-tower-logs-all-actions-including-management)
control-tower-lz4-mandatory-not-default
  claim: Starting with landing zone version 4.0, mandatory controls are no longer applied by default.
  scope: Control Tower landing zone version 4.0 and later.
  link: [Landing Zone version 4.0](../facts/control-tower.md#control-tower-lz4-mandatory-not-default)
  link: [mandatory controls are no longer applied by default](../facts/control-tower.md#control-tower-lz4-mandatory-not-default)
control-tower-mandatory-cloudtrail-controls-before-lz4
  claim: The mandatory control Disallow Configuration Changes to CloudTrail prevents configuration changes to CloudTrail in the landing zone; from landing zone 4.0 Control Tower no longer deploys it, because it protected account trails of landing zone 2.9 and below.
  scope: Control Tower mandatory controls; landing zone versions below 4.0.
  link: [prevents configuration changes to CloudTrail](../facts/control-tower.md#control-tower-mandatory-cloudtrail-controls-before-lz4)
  link: [will no longer deploy the below controls](../facts/control-tower.md#control-tower-mandatory-cloudtrail-controls-before-lz4)
control-tower-mandatory-controls-cannot-change
  claim: The Control Tower guides say mandatory controls are always applied and can't be changed or deactivated, because they protect Control Tower resources, while elective and strongly recommended controls can be changed at any time; starting with landing zone version 4.0, mandatory controls are no longer applied by default.
  scope: AWS Control Tower mandatory controls; starting with landing zone version 4.0, mandatory controls are no longer applied by default.
  link: [Mandatory controls are always applied](../facts/control-tower.md#control-tower-mandatory-controls-cannot-change)
  link: [they can't be deactivated](../facts/control-tower.md#control-tower-mandatory-controls-cannot-change)
  link: [change the elective or strongly recommended controls](../facts/control-tower.md#control-tower-mandatory-controls-cannot-change)
control-tower-mandatory-log-archive-bucket-controls
  claim: Mandatory preventive controls on the Security OU stop changes to the bucket policy, encryption, logging and lifecycle configuration of the S3 buckets that Control Tower creates in the log archive account, and stop deletion of those buckets.
  scope: Control Tower mandatory controls on the Security OU.
  link: [prevents changes to bucket policy](../facts/control-tower.md#control-tower-mandatory-log-archive-bucket-controls)
  link: [prevents deletion of Amazon S3 buckets](../facts/control-tower.md#control-tower-mandatory-log-archive-bucket-controls)
  link: [in the log archive account](../facts/control-tower.md#control-tower-mandatory-log-archive-bucket-controls)
control-tower-moved-account-keeps-old-controls
  claim: When an account moves from one OU to another, the controls of the previous OU are not removed; controls implemented with SCPs and AWS Config rules must be removed manually.
  scope: Control Tower drift; account moved between OUs.
  link: [controls from the previous OU are not removed](../facts/control-tower.md#control-tower-moved-account-keeps-old-controls)
  link: [always must be removed manually](../facts/control-tower.md#control-tower-moved-account-keeps-old-controls)
control-tower-new-account-vpc-replaced-enrolled-kept
  claim: When Account Factory creates a new account, Control Tower removes the default VPC and creates a new VPC; when an existing account is enrolled, it neither creates a VPC nor removes existing VPCs.
  scope: accounts provisioned or enrolled by Control Tower; default; adjustable; Account Factory can be configured to create no VPC.
  link: [removes the AWS default VPC](../facts/control-tower.md#control-tower-new-account-vpc-replaced-enrolled-kept)
  link: [does not create a new VPC](../facts/control-tower.md#control-tower-new-account-vpc-replaced-enrolled-kept)
control-tower-no-additional-charge
  claim: There is no additional charge for using AWS Control Tower; you pay only for the AWS services it enables and the services you use in the landing zone, for example Service Catalog for Account Factory and CloudTrail for events.
  scope: per landing zone.
  link: [No additional charge](../facts/control-tower.md#control-tower-no-additional-charge)
  say: no additional charge
control-tower-no-workloads-in-management-account
  claim: AWS does not recommend running production workloads from the Control Tower management account; create a separate account for workloads.
  scope: Control Tower management account.
  link: [not recommended to run any type of production](../facts/control-tower.md#control-tower-no-workloads-in-management-account)
  link: [Create a separate AWS Control Tower account](../facts/control-tower.md#control-tower-no-workloads-in-management-account)
control-tower-one-operation-at-a-time
  claim: AWS Control Tower has overall concurrency limitations: in general, one operation at a time is permitted, with two exceptions: optional controls can be activated and deactivated concurrently, and Account Factory can provision, update and enroll accounts concurrently.
  scope: AWS Control Tower operations; maximum; except optional control operations and Account Factory account operations.
  link: [one operation at a time is permitted](../facts/control-tower.md#control-tower-one-operation-at-a-time)
  say: one operation at a time
control-tower-orchestration-for-many-accounts
  claim: AWS says that if you host more than a handful of accounts, an orchestration layer such as Control Tower helps with account deployment and governance, and Control Tower can be the primary way to provision accounts and infrastructure.
  scope: AWS Control Tower.
  link: [more than a handful of accounts](../facts/control-tower.md#control-tower-orchestration-for-many-accounts)
  link: [your primary way to provision accounts and infrastructure](../facts/control-tower.md#control-tower-orchestration-for-many-accounts)
control-tower-ou-over-1000-accounts-cannot-register
  claim: An existing OU with more than 1000 directly nested accounts cannot be registered or re-registered in AWS Control Tower.
  scope: per OU, directly nested accounts; maximum; not adjustable; registering or re-registering an existing OU.
  link: [1000](../facts/control-tower.md#control-tower-ou-over-1000-accounts-cannot-register)
  say: one thousand
control-tower-preventive-apply-unenrolled-detective-enrolled-only
  claim: On a registered OU, preventive controls apply to all member accounts under the OU, enrolled and unenrolled, while detective controls apply to enrolled accounts only.
  scope: OU registered with Control Tower.
  link: [under the OU, enrolled and unenrolled](../facts/control-tower.md#control-tower-preventive-apply-unenrolled-detective-enrolled-only)
  link: [detective controls apply to enrolled accounts only](../facts/control-tower.md#control-tower-preventive-apply-unenrolled-detective-enrolled-only)
control-tower-preventive-detective-proactive-defined
  claim: Preventive controls prevent actions from occurring; detective controls detect events when they occur and log them; proactive controls check resources before they are provisioned and do not provision noncompliant resources.
  scope: AWS Control Tower controls.
  link: [Preventive controls prevent actions from occurring](../facts/control-tower.md#control-tower-preventive-detective-proactive-defined)
  link: [Detective controls detect specific events when they occur](../facts/control-tower.md#control-tower-preventive-detective-proactive-defined)
  link: [before the resources are provisioned](../facts/control-tower.md#control-tower-preventive-detective-proactive-defined)
control-tower-preventive-not-on-management-account
  claim: Control Tower preventive controls are not applied to the management account; the root user and administrators in the management account can perform work that controls would otherwise deny, and their actions are still logged in the log archive account.
  scope: Control Tower management account.
  link: [not applied to the management account](../facts/control-tower.md#control-tower-preventive-not-on-management-account)
  link: [This exception is intentional](../facts/control-tower.md#control-tower-preventive-not-on-management-account)
  link: [continue to be tracked in the logs](../facts/control-tower.md#control-tower-preventive-not-on-management-account)
control-tower-preventive-status-all-regions
  claim: A preventive control disallows actions that lead to policy violations; its status is enforced or not enabled, and preventive controls are supported in all AWS Regions.
  scope: Control Tower preventive controls.
  link: [it disallows actions that lead to policy violations](../facts/control-tower.md#control-tower-preventive-status-all-regions)
  link: [Preventive controls are supported in all AWS Regions](../facts/control-tower.md#control-tower-preventive-status-all-regions)
control-tower-proactive-only-cloudformation
  claim: Proactive controls check resources when they are created or updated through CloudFormation stack operations, so they may not affect requests made directly through the console, APIs, SDKs or other infrastructure-as-code tools.
  scope: Control Tower proactive controls.
  link: [by means of CloudFormation stack operations](../facts/control-tower.md#control-tower-proactive-only-cloudformation)
  link: [may not affect requests that are made directly](../facts/control-tower.md#control-tower-proactive-only-cloudformation)
control-tower-proactive-status-pass-fail-skip
  claim: A proactive control scans resources before provisioning; noncompliant resources are not provisioned, and the control status is PASS, FAIL or SKIP.
  scope: Control Tower proactive controls.
  link: [scans your resources before they are provisioned](../facts/control-tower.md#control-tower-proactive-status-pass-fail-skip)
  link: [PASS, FAIL, or SKIP](../facts/control-tower.md#control-tower-proactive-status-pass-fail-skip)
control-tower-recommended-additional-ous
  claim: Beyond the Security OU, the Control Tower guidance recommends a Sandbox OU, an Infrastructure OU for shared services and networking accounts, and a Workloads OU for production workloads.
  scope: AWS multi-account strategy for a Control Tower landing zone.
  link: [called the Sandbox OU](../facts/control-tower.md#control-tower-recommended-additional-ous)
  link: [the Infrastructure OU](../facts/control-tower.md#control-tower-recommended-additional-ous)
  link: [called the Workloads OU](../facts/control-tower.md#control-tower-recommended-additional-ous)
control-tower-region-deny-blocks-unlisted-regions
  claim: The Region deny control disallows unlisted operations in global and Regional services outside the specified Regions, including Regions where Control Tower is not available and Regions not selected for governance; actions are allowed as usual in governed Regions.
  scope: Control Tower Region deny control.
  link: [disallows access to unlisted operations](../facts/control-tower.md#control-tower-region-deny-blocks-unlisted-regions)
  link: [outside of the specified Regions](../facts/control-tower.md#control-tower-region-deny-blocks-unlisted-regions)
  link: [allowed as usual in Regions with Governed status](../facts/control-tower.md#control-tower-region-deny-blocks-unlisted-regions)
control-tower-region-deny-elective-preventive
  claim: The landing zone Region deny control is an elective control with preventive guidance, and it is the top-level control associated with the Region deny action.
  scope: Control Tower Region deny control.
  link: [This is an elective control with preventive guidance](../facts/control-tower.md#control-tower-region-deny-elective-preventive)
  link: [top-level control associated with the Region deny action](../facts/control-tower.md#control-tower-region-deny-elective-preventive)
control-tower-region-deny-exemptions
  claim: The Region deny control cannot deny access to your home Region, and certain global services such as IAM and AWS Organizations are exempt from it.
  scope: Control Tower Region deny control.
  link: [You cannot deny access to your home Region](../facts/control-tower.md#control-tower-region-deny-exemptions)
  link: [such as IAM and AWS Organizations, are exempt](../facts/control-tower.md#control-tower-region-deny-exemptions)
control-tower-region-deny-existing-resources-inaccessible
  claim: Before enabling the Region deny control, make sure no resources exist in the denied Regions, because you lose access to them, and while it is enabled you cannot deploy resources there.
  scope: Control Tower Region deny control; control enabled.
  link: [you will not have access to your resources](../facts/control-tower.md#control-tower-region-deny-existing-resources-inaccessible)
  link: [not be able to deploy resources](../facts/control-tower.md#control-tower-region-deny-existing-resources-inaccessible)
control-tower-region-deny-landing-zone-not-per-ou
  claim: The landing zone Region deny control cannot be configured for individual OUs; when enabled it applies to all OUs with the AWSControlTowerBaseline enabled.
  scope: AWS-GR_REGION_DENY (landing zone Region deny control).
  link: [This control cannot be configured for individual OUs](../facts/control-tower.md#control-tower-region-deny-landing-zone-not-per-ou)
  link: [applies to all OUs with the AWSControlTowerBaseline enabled](../facts/control-tower.md#control-tower-region-deny-landing-zone-not-per-ou)
control-tower-register-ous-enroll-accounts
  claim: To bring existing parts of an organization under Control Tower, you register existing OUs and enroll existing accounts into a governed OU so that controls apply to them.
  scope: Control Tower in an existing organization.
  link: [Enroll additional existing AWS accounts](../facts/control-tower.md#control-tower-register-ous-enroll-accounts)
  link: [you can Register existing OUs](../facts/control-tower.md#control-tower-register-ous-enroll-accounts)
control-tower-sets-up-governs-multi-account
  claim: AWS Control Tower sets up and governs a multi-account environment that follows prescriptive best practices, orchestrating AWS Organizations, AWS Service Catalog and IAM Identity Center to build a landing zone.
  scope: AWS Control Tower.
  link: [set up and govern an AWS multi-account environment](../facts/control-tower.md#control-tower-sets-up-governs-multi-account)
  link: [orchestrates the capabilities of several other AWS services](../facts/control-tower.md#control-tower-sets-up-governs-multi-account)
  link: [to build a landing zone](../facts/control-tower.md#control-tower-sets-up-governs-multi-account)
control-tower-shared-accounts
  claim: The shared accounts of a landing zone are the management account, the log archive account and the audit account, provisioned during setup.
  scope: AWS Control Tower landing zone.
  link: [the log archive account, and the audit account](../facts/control-tower.md#control-tower-shared-accounts)
  link: [provisioned during setup](../facts/control-tower.md#control-tower-shared-accounts)
control-tower-staging-distinct-from-production
  claim: AWS recommends, at a minimum, a pre-production (Staging) environment that is distinct from Production, with distinct controls and policies; the Production and Staging environments can be created and governed as separate OUs and billed as separate accounts.
  scope: AWS multi-account strategy for a Control Tower landing zone.
  link: [a pre-production (or Staging) environment](../facts/control-tower.md#control-tower-staging-distinct-from-production)
  link: [governed as separate OUs](../facts/control-tower.md#control-tower-staging-distinct-from-production)
control-tower-strongly-recommended-elective-off-by-default
  claim: Strongly recommended controls and elective controls are not enabled by default.
  scope: Control Tower controls; default; adjustable.
  link: [By default, Strongly recommended controls are not enabled](../facts/control-tower.md#control-tower-strongly-recommended-elective-off-by-default)
  link: [By default, Elective controls are not enabled](../facts/control-tower.md#control-tower-strongly-recommended-elective-off-by-default)
control-tower-two-region-deny-controls
  claim: Control Tower offers two Region deny controls: AWS-GR_REGION_DENY applies to the entire landing zone, and CT.MULTISERVICE.PV.1 can apply to specific OUs.
  scope: Control Tower Region deny controls.
  link: [applies to the entire landing zone](../facts/control-tower.md#control-tower-two-region-deny-controls)
  link: [can apply to specific OUs that you specify](../facts/control-tower.md#control-tower-two-region-deny-controls)
control-tower-uses-stacksets
  claim: Control Tower uses CloudFormation StackSets by default to set up resources in your accounts, deploying one stack set instance per account and Region.
  scope: Control Tower landing zone.
  link: [uses CloudFormation StackSets to set up resources](../facts/control-tower.md#control-tower-uses-stacksets)
  link: [one stack set instance per account and Region](../facts/control-tower.md#control-tower-uses-stacksets)
organizations-account-default-cost-allocation
  claim: An account is the default means by which AWS costs are allocated, so separate accounts per business unit or workload group make it easier to report, control, forecast and budget spending; cost allocation tags give finer allocation.
  scope: multi-account strategy.
  link: [default means by which AWS costs are allocated](../facts/organizations.md#organizations-account-default-cost-allocation)
  link: [you can apply cost allocation tags](../facts/organizations.md#organizations-account-default-cost-allocation)
organizations-account-is-security-access-billing-boundary
  claim: The AWS Security Reference Architecture treats an AWS account as a security, access and billing boundary, and AWS recommends multiple accounts as workloads grow.
  scope: AWS accounts in a multi-account environment.
  link: [security, access, and billing boundaries](../facts/organizations.md#organizations-account-is-security-access-billing-boundary)
  link: [set up multiple accounts as your workloads grow](../facts/organizations.md#organizations-account-is-security-access-billing-boundary)
organizations-account-isolation-limits-blast-radius
  claim: Account-level isolation limits the scope of impact: if an application problem, misconfiguration or malicious activity happens in one account, the impact can be contained and kept from affecting workloads in other accounts.
  scope: multi-account strategy.
  link: [the impacts can be contained](../facts/organizations.md#organizations-account-isolation-limits-blast-radius)
  link: [clear security, access, and billing boundaries](../facts/organizations.md#organizations-account-isolation-limits-blast-radius)
organizations-accounts-closable-per-30-days
  claim: Within a 30-day period you can close 20% of the member accounts or 250 accounts, whichever is higher, with a maximum of 1,000; this quota is not adjustable, and after you reach it you can't close more accounts until it resets.
  scope: per organization, per 30-day period; maximum; not adjustable; 20% of member accounts or 250, whichever is higher, at most 1,000.
  link: [20%](../facts/organizations.md#organizations-accounts-closable-per-30-days)
  link: [250](../facts/organizations.md#organizations-accounts-closable-per-30-days)
  link: [1,000](../facts/organizations.md#organizations-accounts-closable-per-30-days)
  say: twenty percent | two hundred fifty | one thousand
organizations-accounts-distribute-quotas
  claim: An AWS account gives natural security, access and billing boundaries, and multiple accounts let you distribute account-level quotas and API request-rate limits; production should be in separate accounts from test and development.
  scope: multi-account environment.
  link: [natural security, access, and billing boundaries](../facts/organizations.md#organizations-accounts-distribute-quotas)
  link: [distribute account level quotas and API request-rate limits](../facts/organizations.md#organizations-accounts-distribute-quotas)
  link: [separate production workloads from test/development workloads](../facts/organizations.md#organizations-accounts-distribute-quotas)
organizations-acquired-accounts-move-intact
  claim: If you acquire a business that already runs on AWS, you can move its accounts intact into your existing organization as a first step to integrating it.
  scope: multi-account strategy.
  link: [move the associated accounts intact](../facts/organizations.md#organizations-acquired-accounts-move-intact)
  link: [an initial step toward integrating acquired services](../facts/organizations.md#organizations-acquired-accounts-move-intact)
organizations-ai-opt-out-policy
  claim: With the AWS Organizations AI services opt-out policy you can opt out of the use of your content for service improvement; when you opt out, the AI service deletes the associated historical content shared with AWS before, limited to stored content that is not required to provide service functions.
  scope: AI services opt-out policies; deletion is limited to stored content not required to provide service functions.
  link: [opt out of use of your content](../facts/organizations.md#organizations-ai-opt-out-policy)
  link: [deletes all of the associated historical content](../facts/organizations.md#organizations-ai-opt-out-policy)
organizations-all-features-cannot-revert
  claim: An organization that started with consolidated billing can later enable all features, but once all features is enabled it cannot go back to consolidated billing.
  scope: per organization; after all features is enabled.
  link: [you can later enable all features](../facts/organizations.md#organizations-all-features-cannot-revert)
  link: [cannot migrate from all features to consolidated billing](../facts/organizations.md#organizations-all-features-cannot-revert)
organizations-all-features-invited-accounts-must-approve
  claim: To enable all features, every invited member account must approve the change by accepting a request; accounts created with AWS Organizations get no request.
  scope: organization moving from consolidated billing to all features.
  link: [Every invited account must approve enabling all features](../facts/organizations.md#organizations-all-features-invited-accounts-must-approve)
  link: [don't get a request](../facts/organizations.md#organizations-all-features-invited-accounts-must-approve)
organizations-all-features-is-default-feature-set
  claim: All features is the default feature set of AWS Organizations, and it includes every capability of consolidated billing plus the administrative capabilities.
  scope: per organization; default; adjustable.
  link: [the default feature set](../facts/organizations.md#organizations-all-features-is-default-feature-set)
  link: [all the capabilities of consolidated billing](../facts/organizations.md#organizations-all-features-is-default-feature-set)
organizations-attach-policies-to-ous-not-accounts
  claim: Attaching policies to OUs rather than to individual accounts simplifies policy management across groups of similar accounts, and this matters more as the number of accounts grows.
  scope: AWS Organizations policy management.
  link: [policies to OUs rather than to individual accounts](../facts/organizations.md#organizations-attach-policies-to-ous-not-accounts)
  link: [the number of accounts in your environment grows](../facts/organizations.md#organizations-attach-policies-to-ous-not-accounts)
organizations-attachment-limits-direct-only-hard
  claim: The per-entity policy attachment limits count only policies attached directly to an OU or account; policies that apply by inheritance do not count against them, and all policy attachment limits are hard limits.
  scope: per root, OU or account; maximum; not adjustable; directly attached policies only.
  link: [All policy limits are hard limits](../facts/organizations.md#organizations-attachment-limits-direct-only-hard)
  say: all policy limits are hard limits
organizations-backup-policy-effective-plan-immutable
  claim: Backup policies centrally apply AWS Backup plans to resources across the organization's accounts; the effective backup plan appears in each account as an immutable plan that can be viewed but not changed.
  scope: backup policies.
  link: [centrally manage and apply backup plans](../facts/organizations.md#organizations-backup-policy-effective-plan-immutable)
  link: [as an immutable plan for that account](../facts/organizations.md#organizations-backup-policy-effective-plan-immutable)
  link: [You can view it, but not change it](../facts/organizations.md#organizations-backup-policy-effective-plan-immutable)
organizations-billing-management-account-charged-monthly
  claim: Each month AWS charges the management account owner, not the member account owners; member accounts can still see their own usage and charges but not those of other accounts.
  scope: consolidated billing.
  link: [AWS charges the management account owner](../facts/organizations.md#organizations-billing-management-account-charged-monthly)
  link: [they can still see their usage and charges](../facts/organizations.md#organizations-billing-management-account-charged-monthly)
  link: [They can't view or obtain data](../facts/organizations.md#organizations-billing-management-account-charged-monthly)
organizations-billing-treats-accounts-as-one-for-tiers
  claim: For billing, AWS treats all accounts in the organization as one account and combines their usage to decide which volume pricing tiers apply.
  scope: services with volume pricing tiers, for example data transfer and Amazon S3.
  link: [as if they were one account](../facts/organizations.md#organizations-billing-treats-accounts-as-one-for-tiers)
  link: [AWS combines the usage from all accounts](../facts/organizations.md#organizations-billing-treats-accounts-as-one-for-tiers)
organizations-case-vwfs-eight-engineers-1600-accounts
  claim: Volkswagen Financial Services has more than 1,600 AWS accounts across 48 markets, and its platform team of eight engineers uses AWS Organizations to establish governance at scale.
  scope: Volkswagen Financial Services case study.
  link: [more than 1,600 accounts](../facts/organizations.md#organizations-case-vwfs-eight-engineers-1600-accounts)
  link: [a team of eight engineers](../facts/organizations.md#organizations-case-vwfs-eight-engineers-1600-accounts)
  link: [using AWS Organizations to establish governance at scale](../facts/organizations.md#organizations-case-vwfs-eight-engineers-1600-accounts)
  say: more than sixteen hundred accounts
organizations-case-vwfs-four-accounts-per-workload-scps
  claim: Volkswagen Financial Services splits each workload into four accounts (development, integration, preproduction and production), keeps central accounts for compliance, monitoring and auditing, and applies SCPs.
  scope: Volkswagen Financial Services case study.
  link: [four AWS accounts](../facts/organizations.md#organizations-case-vwfs-four-accounts-per-workload-scps)
  link: [centralized accounts for compliance, monitoring, and auditing](../facts/organizations.md#organizations-case-vwfs-four-accounts-per-workload-scps)
  link: [service control policies (SCPs)](../facts/organizations.md#organizations-case-vwfs-four-accounts-per-workload-scps)
  say: four AWS accounts
organizations-central-manage-govern-accounts
  claim: AWS Organizations lets you centrally manage and govern many accounts: create accounts, group them, apply policies for governance, and pay for all of them with a single payment method.
  scope: an organization.
  link: [centrally manage and govern your environment](../facts/organizations.md#organizations-central-manage-govern-accounts)
  link: [single payment method for all of your accounts](../facts/organizations.md#organizations-central-manage-govern-accounts)
  link: [apply policies for governance](../facts/organizations.md#organizations-central-manage-govern-accounts)
organizations-change-accounts-10000-2024-08
  claim: On 2024-08-14 AWS Organizations began to support up to 10,000 member accounts in an organization, doubling the previous limit of 5,000 accounts; with a valid business need you can request a 10,000 account quota without service limit checks.
  scope: per organization; maximum; quota increase request with a valid business need.
  link: [10,000 member accounts](../facts/organizations.md#organizations-change-accounts-10000-2024-08)
  link: [5,000 accounts](../facts/organizations.md#organizations-change-accounts-10000-2024-08)
  say: ten thousand member accounts | five thousand accounts
  changed: 2024-08-14: was 5,000 accounts
organizations-change-billing-transfer-2025-11
  claim: Since 2025-11-19 Billing Transfer lets customers in multi-organization environments designate a single management account to centrally manage and pay the bills of multiple AWS organizations.
  scope: across multiple organizations.
  link: [2025-11-19](../facts/organizations.md#organizations-change-billing-transfer-2025-11)
  link: [Billing Transfer](../facts/organizations.md#organizations-change-billing-transfer-2025-11)
  say: November nineteenth, twenty twenty-five | Billing Transfer
organizations-change-chat-applications-policies-2024-09
  claim: On 2024-09-26 AWS Organizations added chat applications policies, which control access to the organization's accounts from chat applications such as Slack and Microsoft Teams.
  scope: per organization, OU or account.
  link: [2024-09-26](../facts/organizations.md#organizations-change-chat-applications-policies-2024-09)
  link: [chat applications policies](../facts/organizations.md#organizations-change-chat-applications-policies-2024-09)
  say: September twenty-sixth, twenty twenty-four | chat applications policies
organizations-change-declarative-policies-2024-12
  claim: On 2024-12-01 AWS Organizations added declarative policies, which centrally declare and enforce desired configurations for an AWS service across an organization; once attached, the configuration is always maintained when the service adds new features or APIs.
  scope: per organization, OU or account.
  link: [2024-12-01](../facts/organizations.md#organizations-change-declarative-policies-2024-12)
  link: [declare and enforce desired configurations](../facts/organizations.md#organizations-change-declarative-policies-2024-12)
  say: December first, twenty twenty-four | declare and enforce desired configurations
organizations-change-departure-controls-default-2026-07
  claim: Since 2026-07-10, when you create a new organization in the AWS Organizations console, Organizations automatically applies SCPs that prevent member accounts from leaving the organization or closing themselves; you can modify or disable these settings at any time.
  scope: new organizations created in the AWS Organizations console; default; available in US East (N. Virginia), AWS GovCloud (US) and China Regions.
  link: [2026-07-10](../facts/organizations.md#organizations-change-departure-controls-default-2026-07)
  link: [prevent member accounts from leaving the organization](../facts/organizations.md#organizations-change-departure-controls-default-2026-07)
  say: July tenth, twenty twenty-six | prevent member accounts from leaving the organization
organizations-change-direct-account-transfers-2025-11
  claim: On 2025-11-19 AWS Organizations added direct account transfers: an account can move to a different organization without first being removed from its current organization, which ends the previous requirement for the account to temporarily operate as a standalone account.
  scope: per account moving between organizations.
  link: [2025-11-19](../facts/organizations.md#organizations-change-direct-account-transfers-2025-11)
  link: [temporarily operate as a standalone account](../facts/organizations.md#organizations-change-direct-account-transfers-2025-11)
  say: November nineteenth, twenty twenty-five | temporarily operate as a standalone account
  changed: 2025-11-19: was temporarily operate as a standalone account
organizations-change-guardduty-policies-2026-09
  claim: On 2026-09-25 AWS Organizations added Amazon GuardDuty policies, which centrally enable and manage GuardDuty configurations, including protection plans, across the accounts of an organization.
  scope: per organization, OU or account.
  link: [2026-09-25](../facts/organizations.md#organizations-change-guardduty-policies-2026-09)
  link: [Amazon GuardDuty policies](../facts/organizations.md#organizations-change-guardduty-policies-2026-09)
  say: September twenty-fifth, twenty twenty-six | Amazon GuardDuty policies
organizations-change-inspector-policies-2025-11
  claim: Since 2025-11-19 Amazon Inspector can be enabled, configured and managed across an organization with an Inspector policy type in AWS Organizations.
  scope: per organization, OU or account.
  link: [2025-11-19](../facts/organizations.md#organizations-change-inspector-policies-2025-11)
  link: [Inspector policy type](../facts/organizations.md#organizations-change-inspector-policies-2025-11)
  say: November nineteenth, twenty twenty-five | Inspector policy type
organizations-change-rcp-quota-2000-2026-07
  claim: On 2026-07-22 AWS Organizations raised the number of resource control policies (RCPs) per organization to 2,000, doubling the previous limit of 1,000; existing organizations get the higher limit automatically.
  scope: per organization; maximum.
  link: [2026-07-22](../facts/organizations.md#organizations-change-rcp-quota-2000-2026-07)
  link: [2,000 resource control policies](../facts/organizations.md#organizations-change-rcp-quota-2000-2026-07)
  link: [1,000](../facts/organizations.md#organizations-change-rcp-quota-2000-2026-07)
  say: July twenty-second, twenty twenty-six | two thousand resource control policies | one thousand
  changed: 2026-07-22: was 1,000
organizations-change-security-hub-policies-2025-06
  claim: On 2025-06-17 AWS Organizations added Security Hub policies, which centrally manage Security Hub configurations across the accounts of an organization.
  scope: per organization, OU or account.
  link: [2025-06-17](../facts/organizations.md#organizations-change-security-hub-policies-2025-06)
  link: [Security Hub policies](../facts/organizations.md#organizations-change-security-hub-policies-2025-06)
  say: June seventeenth, twenty twenty-five | Security Hub policies
organizations-change-upgrade-rollout-policy-2025-11
  claim: Since 2025-11-21 AWS Organizations supports the upgrade rollout policy, which staggers automatic minor version upgrades across Amazon Aurora and Amazon RDS databases so that upgrades start with less critical environments.
  scope: per organization, account or resource tag.
  link: [2025-11-21](../facts/organizations.md#organizations-change-upgrade-rollout-policy-2025-11)
  link: [upgrade rollout policy](../facts/organizations.md#organizations-change-upgrade-rollout-policy-2025-11)
  say: November twenty-first, twenty twenty-five | upgrade rollout policy
organizations-closed-account-reopen-within-90-days
  claim: After you close an AWS account, you can reopen it within 90 days from the day you closed it; this is the post-closure period, after which AWS permanently closes the account.
  scope: per closed AWS account; maximum; not adjustable; during the post-closure period.
  link: [90 days](../facts/organizations.md#organizations-closed-account-reopen-within-90-days)
  say: ninety days
organizations-closed-member-account-permanent-after-90-days
  claim: A closed member account shows a CLOSED label in the AWS Organizations console for up to 90 days after the closure date; after 90 days it is permanently closed and no longer displayed, and removal from the organization can take a few more days.
  scope: per closed member account; fixed.
  link: [90 days](../facts/organizations.md#organizations-closed-member-account-permanent-after-90-days)
  say: ninety days
organizations-closed-or-suspended-account-cannot-migrate
  claim: You cannot migrate a closed or suspended account to another organization.
  scope: per account.
  link: [cannot migrate a closed or suspended account](../facts/organizations.md#organizations-closed-or-suspended-account-cannot-migrate)
  say: cannot migrate a closed or suspended account
organizations-concurrent-account-closures-3
  claim: Only 3 member account closures can be in progress at the same time; as soon as one finishes, you can close another account.
  scope: per organization; maximum; not adjustable; closures in progress at one time.
  link: [3](../facts/organizations.md#organizations-concurrent-account-closures-3)
  say: three
organizations-concurrent-account-creations-5
  claim: You can create at most 5 member accounts concurrently; as soon as one creation finishes, you can start another.
  scope: per organization; maximum; not adjustable; account creations in progress at one time.
  link: [5](../facts/organizations.md#organizations-concurrent-account-creations-5)
  say: five
organizations-consolidated-billing-combined-usage-shares-discounts
  claim: Consolidated billing combines usage across all accounts in the organization, which shares volume pricing discounts, Reserved Instance discounts and Savings Plans, and it is offered at no additional cost.
  scope: organization with consolidated billing.
  link: [combine the usage across all accounts](../facts/organizations.md#organizations-consolidated-billing-combined-usage-shares-discounts)
  link: [shares the volume pricing discounts, Reserved Instance discounts](../facts/organizations.md#organizations-consolidated-billing-combined-usage-shares-discounts)
  link: [offered at no additional cost](../facts/organizations.md#organizations-consolidated-billing-combined-usage-shares-discounts)
organizations-consolidated-billing-no-policies-or-integrations
  claim: With only the consolidated billing feature set, an organization cannot integrate other AWS services across its accounts and cannot use policies to restrict what users and roles in its accounts can do.
  scope: organization with the consolidated billing feature set only.
  link: [you can't enable other AWS services to integrate](../facts/organizations.md#organizations-consolidated-billing-no-policies-or-integrations)
  link: [use policies to restrict what users and roles](../facts/organizations.md#organizations-consolidated-billing-no-policies-or-integrations)
organizations-cost-allocation-tags-management-account
  claim: In an organization, only the management account has access to the cost allocation tags manager in the Billing console.
  scope: cost allocation tags in an organization.
  link: [Only the management account in an organization](../facts/organizations.md#organizations-cost-allocation-tags-management-account)
  link: [cost allocation tags manager](../facts/organizations.md#organizations-cost-allocation-tags-management-account)
organizations-create-invite-only-from-management-account
  claim: Only the management account can create member accounts or invite existing accounts to join the organization; a delegated administrator account cannot.
  scope: creating and inviting member accounts.
  link: [can be done only from the management account](../facts/organizations.md#organizations-create-invite-only-from-management-account)
  link: [not from a delegated administrator account](../facts/organizations.md#organizations-create-invite-only-from-management-account)
organizations-created-account-gets-access-role
  claim: When you create an account in an organization, AWS Organizations creates an IAM role in it that is named OrganizationAccountAccessRole by default, and no other users or roles.
  scope: member account created through AWS Organizations; default; adjustable; a different name can be given at creation.
  link: [OrganizationAccountAccessRole](../facts/organizations.md#organizations-created-account-gets-access-role)
  link: [automatically creates an IAM role](../facts/organizations.md#organizations-created-account-gets-access-role)
  link: [doesn't create any other users or roles](../facts/organizations.md#organizations-created-account-gets-access-role)
organizations-credit-sharing-on-by-default
  claim: By default credit sharing is turned on in an organization, and accounts must have credit sharing activated to give or receive shared credits.
  scope: AWS credits in an organization; default; adjustable.
  link: [by default (Credit sharing turned on)](../facts/organizations.md#organizations-credit-sharing-on-by-default)
  link: [Accounts must have credit sharing activated](../facts/organizations.md#organizations-credit-sharing-on-by-default)
organizations-credit-sharing-payer-controls
  claim: In an organization, only the payer account can turn credit sharing off or on; when credit sharing is off, credits apply only to the account that received them.
  scope: AWS credits in an organization.
  link: [only the payer account can turn credit sharing](../facts/organizations.md#organizations-credit-sharing-payer-controls)
  link: [Credits are applied to only the account](../facts/organizations.md#organizations-credit-sharing-payer-controls)
organizations-decision-guide-control-tower-layered-on-orgs
  claim: The cloud governance decision guide says to use AWS Organizations to consolidate accounts into an organization and AWS Control Tower as an orchestration service layered on top of Organizations to structure the estate and extend governance over OUs.
  scope: AWS cloud governance decision guide.
  link: [consolidate multiple AWS accounts into an organization](../facts/organizations.md#organizations-decision-guide-control-tower-layered-on-orgs)
  link: [layered on top of AWS Organizations](../facts/organizations.md#organizations-decision-guide-control-tower-layered-on-orgs)
organizations-decision-guide-governance-services
  claim: The AWS cloud governance decision guide recommends AWS Organizations to consolidate accounts and apply governance policies, AWS Control Tower to set up and orchestrate multiple services for security and compliance, AWS Config to detect drift from ideal configuration, and Security Hub CSPM to run continuous checks against security standards.
  scope: AWS cloud governance decision guide.
  link: [To consolidate multiple AWS accounts into an organization](../facts/organizations.md#organizations-decision-guide-governance-services)
  link: [To setup and orchestrate multiple AWS services](../facts/organizations.md#organizations-decision-guide-governance-services)
  link: [detect if AWS resources drift from it](../facts/organizations.md#organizations-decision-guide-governance-services)
  link: [To run automated and continuous checks](../facts/organizations.md#organizations-decision-guide-governance-services)
organizations-decision-guide-identity-center-workforce
  claim: The identity decision guide says an organization instance of IAM Identity Center helps manage workforce access to AWS accounts: it assigns permissions to users and provisions them to multiple accounts from a central place.
  scope: AWS identity decision guide.
  link: [manage your workforce access to AWS accounts](../facts/organizations.md#organizations-decision-guide-identity-center-workforce)
  link: [provision the permissions to multiple accounts](../facts/organizations.md#organizations-decision-guide-identity-center-workforce)
organizations-declarative-effective-policy
  claim: The effective declarative policy of an account is the set of rules inherited from the root and OUs plus those attached directly to the account; it is the final set of rules that apply.
  scope: declarative policies.
  link: [the set of rules that are inherited](../facts/organizations.md#organizations-declarative-effective-policy)
  link: [specifies the final set of rules](../facts/organizations.md#organizations-declarative-effective-policy)
organizations-declarative-governs-service-linked-roles-row
  claim: Declarative policies govern service-linked roles; SCPs and RCPs do not.
  scope: SCPs, RCPs and declarative policies.
  link: [Governs service-linked roles?](../facts/organizations.md#organizations-declarative-governs-service-linked-roles-row)
  link: [No | No | Yes](../facts/organizations.md#organizations-declarative-governs-service-linked-roles-row)
organizations-declarative-inheritance-root-ou-account
  claim: A declarative policy attached to the root is inherited by all OUs and accounts; attached to an OU it is inherited by accounts directly under it or under any child OU; attached to an account it affects only that account.
  scope: declarative policy inheritance (not SCPs or RCPs).
  link: [all OUs and accounts in the organization inherit](../facts/organizations.md#organizations-declarative-inheritance-root-ou-account)
  link: [it affects only that account](../facts/organizations.md#organizations-declarative-inheritance-root-ou-account)
organizations-declarative-new-accounts-inherit-detach-rolls-back
  claim: Accounts that join an organization inherit its declarative policies automatically, and when a declarative policy is detached the attribute rolls back to its state before the policy was attached.
  scope: declarative policies.
  link: [will automatically inherit the declarative policy](../facts/organizations.md#organizations-declarative-new-accounts-inherit-detach-rolls-back)
  link: [the attribute state will roll back](../facts/organizations.md#organizations-declarative-new-accounts-inherit-detach-rolls-back)
organizations-declarative-policies-per-entity
  claim: Declarative policies need no minimum attachment, and at most 10 can be attached directly to the root, to each OU and to each account.
  scope: per root, OU or account (direct attachment); maximum; not adjustable; inherited policies do not count.
  link: [10](../facts/organizations.md#organizations-declarative-policies-per-entity)
  say: ten
organizations-declarative-policy-at-root-includes-management
  claim: A declarative policy attached to the root applies to all OUs and accounts including the management account, while an authorization policy such as an SCP attached to the root does not apply to the management account.
  scope: policies attached to the organization root.
  link: [including the management account for the organization](../facts/organizations.md#organizations-declarative-policy-at-root-includes-management)
  link: [It does not apply to the management account](../facts/organizations.md#organizations-declarative-policy-at-root-includes-management)
organizations-declarative-policy-blocks-vpc-public-access
  claim: Declarative policies prevent noncompliant actions; for example, they can block public internet access to Amazon VPC resources or enforce encryption in transit for VPC traffic across the organization.
  scope: declarative policies.
  link: [Use declarative policies to prevent noncompliant actions](../facts/organizations.md#organizations-declarative-policy-blocks-vpc-public-access)
  link: [block public internet access to Amazon VPC resources](../facts/organizations.md#organizations-declarative-policy-blocks-vpc-public-access)
organizations-declarative-policy-control-plane-not-api
  claim: Declarative policies are enforced in the service's control plane: authorization policies regulate access to APIs, while declarative policies are applied directly at the service level.
  scope: declarative policies compared with SCPs and RCPs.
  link: [enforced in the service's control plane](../facts/organizations.md#organizations-declarative-policy-control-plane-not-api)
  link: [authorization policies regulate access to APIs](../facts/organizations.md#organizations-declarative-policy-control-plane-not-api)
organizations-declarative-policy-maintained-for-new-features
  claim: A declarative policy centrally declares and enforces the desired configuration of an AWS service across the organization, and the configuration stays enforced when the service adds new features or APIs.
  scope: declarative policies.
  link: [centrally declare and enforce your desired configuration](../facts/organizations.md#organizations-declarative-policy-maintained-for-new-features)
  link: [the configuration is always maintained](../facts/organizations.md#organizations-declarative-policy-maintained-for-new-features)
organizations-delegated-admin-for-service-permissions
  claim: Registering a member account as delegated administrator for an AWS service gives it some administrative permissions for that service plus read-only Organizations permissions, which reduces use of the management account.
  scope: member account registered as delegated administrator for one AWS service; the service supports delegated administrators and trusted access is enabled.
  link: [reduce the usage of the management account](../facts/organizations.md#organizations-delegated-admin-for-service-permissions)
  link: [some administrative permissions for that service](../facts/organizations.md#organizations-delegated-admin-for-service-permissions)
  link: [permissions for Organizations read-only actions](../facts/organizations.md#organizations-delegated-admin-for-service-permissions)
organizations-delegation-policy-max-size
  claim: The Organizations quota page lists 40,000 characters as the maximum size of the resource-based delegation policy; it calls these values default maximums and says you can request increases for some of them.
  scope: per organization; default; listed among default maximums; increases can be requested for some of these values.
  link: [40,000 characters](../facts/organizations.md#organizations-delegation-policy-max-size)
  say: forty thousand characters
organizations-direct-account-transfer-by-invitation
  claim: To migrate an account to another organization, the new organization sends an invitation and the account accepts it; the account does not need to leave its current organization or operate as a standalone account first. Before 2025-11-19 the account had to temporarily operate as a standalone account.
  scope: per account moving between organizations.
  link: [doesn't need to leave its current organization](../facts/organizations.md#organizations-direct-account-transfer-by-invitation)
  say: does not need to leave its current organization
  changed: 2025-11-19: was temporarily operate as a standalone account
organizations-disable-trusted-access-does-not-block-users
  claim: Disabling trusted access does not stop users and roles with the right permissions from using the service; to block them, remove their IAM permissions or use SCPs, which apply only to member accounts.
  scope: trusted access for an integrated service.
  link: [does not prevent users and roles](../facts/organizations.md#organizations-disable-trusted-access-does-not-block-users)
  link: [You can apply SCPs to only member accounts](../facts/organizations.md#organizations-disable-trusted-access-does-not-block-users)
organizations-ec2-declarative-policy-attributes
  claim: EC2 declarative policies centrally enforce configurations for Amazon EC2, Amazon VPC and Amazon EBS across the organization; their attributes include VPC Block Public Access, Image Block Public Access, Allowed Images Settings, Instance Metadata defaults, Serial Console Access and Snapshot Block Public Access.
  scope: EC2 declarative policies in AWS Organizations.
  link: [Amazon EC2, Amazon VPC, and Amazon EBS](../facts/organizations.md#organizations-ec2-declarative-policy-attributes)
  link: [VPC Block Public Access](../facts/organizations.md#organizations-ec2-declarative-policy-attributes)
  link: [Allowed Images Settings, Instance Metadata defaults](../facts/organizations.md#organizations-ec2-declarative-policy-attributes)
organizations-ec2-policy-custom-error-messages
  claim: EC2 policies support custom error messages, such as a link to an internal wiki, when an API operation fails because of the policy, and CloudTrail can flag API failures caused by EC2 policies.
  scope: EC2 declarative policies.
  link: [EC2 policies allow you to create custom error messages](../facts/organizations.md#organizations-ec2-policy-custom-error-messages)
  link: [CloudTrail can flag API operation failures due to EC2 policies](../facts/organizations.md#organizations-ec2-policy-custom-error-messages)
organizations-ec2-policy-snapshot-bpa
  claim: The Snapshot Block Public Access attribute of an EC2 declarative policy controls whether Amazon EBS snapshots are publicly accessible.
  scope: EC2 declarative policies.
  link: [Snapshot Block Public Access](../facts/organizations.md#organizations-ec2-policy-snapshot-bpa)
  link: [Controls if Amazon EBS snapshots are publicly accessible](../facts/organizations.md#organizations-ec2-policy-snapshot-bpa)
organizations-enable-all-features-request-90-days
  claim: A request to enable all features in an organization expires after 90 days.
  scope: per enable-all-features handshake; maximum; not adjustable.
  link: [90 days](../facts/organizations.md#organizations-enable-all-features-request-90-days)
  say: ninety days
organizations-faq-account-moved-to-ou-inherits-policies
  claim: After you add an account, by invitation or by creation, you can move it to an OU, and the account automatically inherits the policies attached to that OU.
  scope: accounts added to an OU.
  link: [automatically inherits the policies attached to the OU](../facts/organizations.md#organizations-faq-account-moved-to-ou-inherits-policies)
organizations-faq-account-one-ou-at-a-time
  claim: An AWS account can be a member of only one OU at a time.
  scope: per AWS account.
  link: [member of only one OU at a time](../facts/organizations.md#organizations-faq-account-one-ou-at-a-time)
organizations-faq-bill-does-not-reflect-ou-structure
  claim: The bill of an organization does not reflect the OU structure that you defined.
  scope: bill of an organization.
  link: [your bill will not reflect the structure](../facts/organizations.md#organizations-faq-bill-does-not-reflect-ou-structure)
organizations-faq-config-detective-and-proactive-rules-alongside
  claim: Next to SCPs, RCPs and declarative policies, you can keep using AWS Config detective rules to monitor changes and AWS Config proactive rules to prevent non-compliant resources created through CloudFormation.
  scope: AWS Config rules used next to organization policies.
  link: [AWS Config detective rules](../facts/organizations.md#organizations-faq-config-detective-and-proactive-rules-alongside)
  link: [AWS Config proactive rules](../facts/organizations.md#organizations-faq-config-detective-and-proactive-rules-alongside)
organizations-faq-consolidated-billing-single-payer-tiered-pricing
  claim: Consolidated billing gives an organization a single payer account for all its accounts and default tiered-pricing benefits automatically.
  scope: consolidated billing in an organization.
  link: [single-payer account for all accounts](../facts/organizations.md#organizations-faq-consolidated-billing-single-payer-tiered-pricing)
  link: [default tiered-pricing benefits](../facts/organizations.md#organizations-faq-consolidated-billing-single-payer-tiered-pricing)
organizations-faq-cost-allocation-tags-in-consolidated-bill
  claim: To group costs, you can use cost allocation tags in individual accounts, and that allocation is visible in the consolidated bill of the organization.
  scope: cost allocation tags in an organization.
  link: [use cost allocation tags in individual AWS accounts](../facts/organizations.md#organizations-faq-cost-allocation-tags-in-consolidated-bill)
organizations-faq-created-account-can-become-standalone
  claim: An account created in an organization can be removed and made standalone, but because AWS did not collect all standalone-account information at creation, you must first add it, which can include contact information, a valid payment method and a support plan.
  scope: accounts created with AWS Organizations.
  link: [does not collect all of the information](../facts/organizations.md#organizations-faq-created-account-can-become-standalone)
  link: [providing a valid payment method](../facts/organizations.md#organizations-faq-created-account-can-become-standalone)
organizations-faq-created-account-can-move-to-another-org
  claim: An AWS account created with AWS Organizations can be transferred to a new organization through an invitation, and after the new organization accepts, the account inherits that organization's billing, support plans and policies.
  scope: accounts created with AWS Organizations.
  link: [transferred to a new organization through an invitation](../facts/organizations.md#organizations-faq-created-account-can-move-to-another-org)
  link: [inherit the new organization's billing, support plans](../facts/organizations.md#organizations-faq-created-account-can-move-to-another-org)
organizations-faq-declarative-customizable-error-messages
  claim: Compared with SCPs, declarative policies give a simpler way to define a configuration and show end users why their actions failed through customizable error messages.
  scope: declarative policies.
  link: [customizable error messages](../facts/organizations.md#organizations-faq-declarative-customizable-error-messages)
organizations-faq-declarative-no-scp-updates-for-new-apis
  claim: With declarative policies you do not have to update SCPs for new APIs to protect a configuration; once set, a declarative policy maintains the configuration.
  scope: declarative policies.
  link: [you do not have to update your SCPs](../facts/organizations.md#organizations-faq-declarative-no-scp-updates-for-new-apis)
  link: [a declarative policy will maintain the configuration](../facts/organizations.md#organizations-faq-declarative-no-scp-updates-for-new-apis)
organizations-faq-declarative-plus-scp-additional-layer
  claim: Where existing SCPs cover a control that declarative policies support, adding that control to a declarative policy is an additional layer of protection.
  scope: declarative policies next to SCPs.
  link: [additional layer of protection](../facts/organizations.md#organizations-faq-declarative-plus-scp-additional-layer)
organizations-faq-declarative-prevents-noncompliant-actions
  claim: Once enforced, a declarative policy prevents non-compliant actions, and its configuration is kept when AWS adds new APIs and features or when resources, principals or accounts are added to the organization.
  scope: declarative policies.
  link: [these policies prevent non-compliant actions](../facts/organizations.md#organizations-faq-declarative-prevents-noncompliant-actions)
organizations-faq-enable-integration-in-service-console
  claim: To use an AWS service integrated with AWS Organizations, you go to that service in the console and enable the integration there.
  scope: AWS services integrated with AWS Organizations.
  link: [in the AWS Management Console to that service](../facts/organizations.md#organizations-faq-enable-integration-in-service-console)
organizations-faq-entities-global-except-china
  claim: All organization entities are global, not Regional, except for organizations managed in China; this is similar to how IAM works.
  scope: organization entities (root, OUs, accounts, policies).
  link: [All organization entities are globally accessible](../facts/organizations.md#organizations-faq-entities-global-except-china)
organizations-faq-invite-several-accounts-at-once
  claim: You can invite more than one AWS account in one action by giving a comma-separated list of email addresses or AWS account IDs.
  scope: invitations to join an organization.
  link: [comma-separated list of email addresses](../facts/organizations.md#organizations-faq-invite-several-accounts-at-once)
organizations-faq-invited-account-must-accept
  claim: An administrator in the invited AWS account must accept or reject the invitation, through the Organizations console, the AWS CLI or the Organizations API.
  scope: invited AWS accounts.
  link: [must accept or reject the request](../facts/organizations.md#organizations-faq-invited-account-must-accept)
organizations-faq-management-account-owner-pays-all-usage
  claim: The owner of the management account pays for all usage, data and resources used by the accounts in the organization.
  scope: per organization.
  link: [paying for all usage, data, and resources](../facts/organizations.md#organizations-faq-management-account-owner-pays-all-usage)
organizations-faq-more-accounts-via-support-case
  claim: The FAQ says the number of accounts you can manage in an organization can vary, and that you request more accounts by opening a support case in the AWS Support Center.
  scope: accounts per organization.
  link: [open a support case to request an increase](../facts/organizations.md#organizations-faq-more-accounts-via-support-case)
organizations-faq-multiple-accounts-best-practice
  claim: Using multiple AWS accounts is a best practice for scaling, because accounts give a natural billing boundary and isolate resources for security.
  scope: multi-account environment.
  link: [natural billing boundary for costs](../facts/organizations.md#organizations-faq-multiple-accounts-best-practice)
  link: [isolates resources for security](../facts/organizations.md#organizations-faq-multiple-accounts-best-practice)
organizations-faq-no-region-needed-china-separate-org
  claim: You do not specify an AWS Region when you create and manage an organization, but accounts used in China need a separate organization.
  scope: per organization.
  link: [do not need to specify an AWS Region](../facts/organizations.md#organizations-faq-no-region-needed-china-separate-org)
  link: [separate organization for accounts used in China](../facts/organizations.md#organizations-faq-no-region-needed-china-separate-org)
organizations-faq-org-without-scp-consolidated-billing-only
  claim: You can create and manage an organization without enforcing any SCP: you decide which policies to enforce, and an organization can use only consolidated billing.
  scope: per organization.
  link: [decide which policies that you want to enforce](../facts/organizations.md#organizations-faq-org-without-scp-consolidated-billing-only)
  link: [only of the consolidated billing functionality](../facts/organizations.md#organizations-faq-org-without-scp-consolidated-billing-only)
organizations-faq-ou-one-parent-ou-at-a-time
  claim: An OU can be a member of only one OU at a time, so an OU cannot have more than one parent OU.
  scope: per OU.
  link: [member of only one OU at a time](../facts/organizations.md#organizations-faq-ou-one-parent-ou-at-a-time)
organizations-faq-policies-enforced-automatically-on-new-account
  claim: When an account joins an organization, applicable policies such as SCPs are enforced in it automatically; for example an SCP attached to the root applies to the new account directly.
  scope: accounts that join an organization.
  link: [enforced automatically in the newly added account](../facts/organizations.md#organizations-faq-policies-enforced-automatically-on-new-account)
organizations-faq-programmatic-mfa-not-supported
  claim: Setting up MFA programmatically on an AWS account that you create in your organization is currently not supported, according to the FAQ.
  scope: accounts created in an organization.
  link: [This currently is not supported.](../facts/organizations.md#organizations-faq-programmatic-mfa-not-supported)
organizations-faq-rcp-restrict-to-org-identities
  claim: An RCP can restrict access to your resources so that only identities in your organization can access them, or set the conditions under which external identities can access them.
  scope: resource control policies.
  link: [accessed by identities that belong to your organization](../facts/organizations.md#organizations-faq-rcp-restrict-to-org-identities)
organizations-free-tier-applies-to-total-org-usage
  claim: In an organization, AWS applies the free tier to the total usage across all accounts, not to each account individually.
  scope: services that support a free tier, in an organization.
  link: [applies the free tier to the total usage](../facts/organizations.md#organizations-free-tier-applies-to-total-org-usage)
  link: [doesn't apply the free tier to each account](../facts/organizations.md#organizations-free-tier-applies-to-total-org-usage)
organizations-fullawsaccess-attached-by-default
  claim: AWS Organizations attaches the AWS managed SCP FullAWSAccess, which allows all services and actions, to every root, OU and account when it is created.
  scope: every root, OU and account; default; adjustable; SCP policy type enabled; the policy can be replaced.
  link: [FullAWSAccess](../facts/organizations.md#organizations-fullawsaccess-attached-by-default)
  link: [to every root, OU and account](../facts/organizations.md#organizations-fullawsaccess-attached-by-default)
  link: [This policy allows all services and actions](../facts/organizations.md#organizations-fullawsaccess-attached-by-default)
organizations-fullawsaccess-removed-blocks-actions
  claim: If FullAWSAccess is removed and not replaced at some level of the organization, all OUs and accounts under that level are blocked from taking any actions.
  scope: OUs and accounts below the level where FullAWSAccess is removed; no replacement Allow policy.
  link: [blocked from taking any actions](../facts/organizations.md#organizations-fullawsaccess-removed-blocks-actions)
  link: [all AWS actions from member accounts will fail](../facts/organizations.md#organizations-fullawsaccess-removed-blocks-actions)
organizations-global-service-hosted-us-east-1
  claim: AWS Organizations is a global service that is physically hosted in the US East (N. Virginia) Region, us-east-1.
  scope: per organization.
  link: [US East (N. Virginia) Region](../facts/organizations.md#organizations-global-service-hosted-us-east-1)
  say: US East, Northern Virginia
organizations-invitation-attempts-per-24-hours
  claim: In a 24-hour period you can make either 20 invitation attempts or as many as the maximum number of accounts allowed in your organization, whichever is greater; accepted invitations don't count against this quota. The page lists this among default maximums and says you can request increases for some of these values.
  scope: per organization, per 24-hour period; default; or the maximum number of accounts allowed, whichever is greater; listed among default maximums.
  link: [20](../facts/organizations.md#organizations-invitation-attempts-per-24-hours)
  say: twenty
organizations-invitation-expires-15-days
  claim: Each invitation to join an organization must be answered within 15 days, or it expires.
  scope: per invitation; maximum; not adjustable.
  link: [15 days](../facts/organizations.md#organizations-invitation-expires-15-days)
  say: fifteen days
organizations-invitations-and-closed-accounts-count-toward-quota
  claim: An invitation sent to an account counts against the maximum-accounts quota until the invited account declines, the management account cancels it, or it expires; a closed account keeps counting against the quota until it is permanently closed.
  scope: per organization.
  link: [counts against this quota](../facts/organizations.md#organizations-invitations-and-closed-accounts-count-toward-quota)
  say: counts against this quota
organizations-invited-account-access-role-optional
  claim: An invited account does not get the access role automatically; after it accepts the invitation, an administrator can choose to create an IAM role that lets the management account access it.
  scope: existing account invited to the organization; after the account accepts the invitation.
  link: [choose to create an IAM role](../facts/organizations.md#organizations-invited-account-access-role-optional)
  link: [Organizations did not automatically create such a role](../facts/organizations.md#organizations-invited-account-access-role-optional)
organizations-keep-resources-out-of-management-account
  claim: AWS recommends keeping all resources out of the management account, because SCPs do not restrict any users or roles in the management account.
  scope: management account of an organization.
  link: [keep them out of the management account](../facts/organizations.md#organizations-keep-resources-out-of-management-account)
  link: [do not work to restrict any users](../facts/organizations.md#organizations-keep-resources-out-of-management-account)
organizations-log-archive-account-consolidates-logs
  claim: The Log Archive account is a consolidation point for log data gathered from all accounts in the organization, used mainly by security, operations, audit and compliance teams; its log data is considered immutable because it is protected from being changed or deleted.
  scope: Log Archive account in the Security OU.
  link: [a consolidation point for log data](../facts/organizations.md#organizations-log-archive-account-consolidates-logs)
  link: [considered immutable](../facts/organizations.md#organizations-log-archive-account-consolidates-logs)
  link: [protected from being changed or deleted](../facts/organizations.md#organizations-log-archive-account-consolidates-logs)
organizations-management-account-cannot-be-changed
  claim: You cannot change which account in an organization is the management account.
  scope: per organization.
  link: [You cannot change which account](../facts/organizations.md#organizations-management-account-cannot-be-changed)
  link: [is the management account](../facts/organizations.md#organizations-management-account-cannot-be-changed)
organizations-management-account-controls-ri-sp-sharing
  claim: The management account can control Reserved Instance and Savings Plans discount sharing for any account in the organization, including turning sharing on or off for individual accounts.
  scope: Reserved Instances and Savings Plans in an organization.
  link: [The management account of an organization can control](../facts/organizations.md#organizations-management-account-controls-ri-sp-sharing)
  link: [Activate or deactivate sharing for individual accounts](../facts/organizations.md#organizations-management-account-controls-ri-sp-sharing)
organizations-management-account-pays-all-charges
  claim: The management account is the payer account: it pays all charges that the accounts in its organization accrue.
  scope: management account of an organization.
  link: [the role of a payer account](../facts/organizations.md#organizations-management-account-pays-all-charges)
  link: [responsible for paying all charges](../facts/organizations.md#organizations-management-account-pays-all-charges)
organizations-max-accounts-default-10
  claim: By default an organization can have at most 10 accounts; the quota is adjustable through the Service Quotas console, and only the management account can submit the increase request.
  scope: per organization; default; adjustable; newly created accounts and organizations might experience a quota below the default.
  link: [10](../facts/organizations.md#organizations-max-accounts-default-10)
  say: ten
organizations-max-accounts-increase-50000
  claim: Increases of the accounts-per-organization quota can be granted up to 50,000 accounts, based on customer qualifications and requirements.
  scope: per organization; maximum; adjustable; granted based on customer qualifications and requirements.
  link: [50,000 accounts](../facts/organizations.md#organizations-max-accounts-increase-50000)
  say: fifty thousand accounts
organizations-member-account-one-organization-at-a-time
  claim: A member account can belong to only one organization at a time.
  scope: per member account.
  link: [only one organization at a time](../facts/organizations.md#organizations-member-account-one-organization-at-a-time)
  link: [A member account can belong to](../facts/organizations.md#organizations-member-account-one-organization-at-a-time)
organizations-migration-created-account-min-age-four-days
  claim: To migrate an account that was created in an organization, you must wait at least 4 days after the account was created; invited accounts are not subject to this waiting period.
  scope: per account created in an organization; minimum; not adjustable; not for invited accounts.
  link: [four days](../facts/organizations.md#organizations-migration-created-account-min-age-four-days)
  say: four days
organizations-migration-org-min-age-seven-days
  claim: To migrate an account to a new organization, you must wait at least 7 days after that organization was created.
  scope: per destination organization; minimum; not adjustable; account migration between organizations.
  link: [seven days](../facts/organizations.md#organizations-migration-org-min-age-seven-days)
  say: seven days
organizations-nested-ous-inherit-parent-policies
  claim: Nested OUs inherit the policies of their parent OU in addition to any controls attached directly to them.
  scope: nested OUs.
  link: [inherit the policies from the parent OU](../facts/organizations.md#organizations-nested-ous-inherit-parent-policies)
  link: [in addition to any controls assigned directly](../facts/organizations.md#organizations-nested-ous-inherit-parent-policies)
organizations-no-additional-charge
  claim: AWS Organizations is offered at no additional charge; you are charged only for the AWS resources that users and roles in your member accounts use.
  scope: per organization.
  link: [no additional charge](../facts/organizations.md#organizations-no-additional-charge)
  say: no additional charge
organizations-one-root-per-organization
  claim: An organization has only one root.
  scope: per organization; fixed.
  link: [1](../facts/organizations.md#organizations-one-root-per-organization)
  say: one
organizations-org-trail-members-cannot-modify-or-delete
  claim: An organization trail created in the management account logs events for all accounts, applies to all member accounts automatically, and member accounts can see it but cannot modify or delete it; by default they cannot read its log files in S3.
  scope: CloudTrail organization trail.
  link: [Member accounts can see the organization trail](../facts/organizations.md#organizations-org-trail-members-cannot-modify-or-delete)
  link: [can't modify or delete it](../facts/organizations.md#organizations-org-trail-members-cannot-modify-or-delete)
  link: [don't have access to the log files](../facts/organizations.md#organizations-org-trail-members-cannot-modify-or-delete)
organizations-org-trail-only-from-management-account
  claim: You must sign in with the management account or a delegated administrator account of the organization to create an organization trail.
  scope: CloudTrail organization trail.
  link: [the management account or a delegated administrator account](../facts/organizations.md#organizations-org-trail-only-from-management-account)
  link: [to create an organization trail](../facts/organizations.md#organizations-org-trail-only-from-management-account)
organizations-organization-is-tree-of-accounts
  claim: An organization is a collection of AWS accounts arranged in a tree, with a root at the top and organizational units nested under the root.
  scope: an organization.
  link: [a collection of AWS accounts](../facts/organizations.md#organizations-organization-is-tree-of-accounts)
  link: [hierarchical, tree-like structure](../facts/organizations.md#organizations-organization-is-tree-of-accounts)
  link: [a root at the top](../facts/organizations.md#organizations-organization-is-tree-of-accounts)
organizations-ou-is-group-of-accounts
  claim: An organizational unit (OU) is a group of AWS accounts in an organization, and an OU can contain other OUs to form a hierarchy.
  scope: an organization.
  link: [a group of AWS accounts within an organization](../facts/organizations.md#organizations-ou-is-group-of-accounts)
  link: [An OU can also contain other OUs](../facts/organizations.md#organizations-ou-is-group-of-accounts)
organizations-ou-max-nesting-five-levels
  claim: OUs can be nested five levels deep under a root: excluding the root and the AWS accounts created in the lowest OUs, the hierarchy can be five levels deep.
  scope: per organization root; maximum.
  link: [Five levels of OUs deep](../facts/organizations.md#organizations-ou-max-nesting-five-levels)
  say: five levels deep
organizations-ou-policy-inherited-by-accounts
  claim: OUs group accounts to administer them as one unit: a policy-based control attached to an OU is inherited automatically by all accounts in the OU, and accounts can move from one OU to another.
  scope: organizational units.
  link: [to administer as a single unit](../facts/organizations.md#organizations-ou-policy-inherited-by-accounts)
  link: [accounts within the OU automatically inherit the policy](../facts/organizations.md#organizations-ou-policy-inherited-by-accounts)
  link: [move accounts from one OU to another](../facts/organizations.md#organizations-ou-policy-inherited-by-accounts)
organizations-ous-by-controls-not-reporting-structure
  claim: AWS recommends isolating production workload environments and data under top-level workload-oriented OUs, and basing OUs on a common set of controls rather than on the company's reporting structure.
  scope: OU design.
  link: [based on a common set of controls](../facts/organizations.md#organizations-ous-by-controls-not-reporting-structure)
  link: [rather than mirroring your company’s reporting structure](../facts/organizations.md#organizations-ous-by-controls-not-reporting-structure)
organizations-ous-per-organization
  claim: An organization can have up to 2000 OUs.
  scope: per organization; maximum; not adjustable.
  link: [2000](../facts/organizations.md#organizations-ous-per-organization)
  say: two thousand
organizations-policies-need-all-features
  claim: You can use organization policies when all features are enabled in the organization; with only the consolidated billing features you can't use policies to restrict what users and roles in different accounts can do, and SCPs aren't available.
  scope: organization policies.
  link: [when all features are enabled](../facts/organizations.md#organizations-policies-need-all-features)
  link: [You can use policies](../facts/organizations.md#organizations-policies-need-all-features)
organizations-policies-per-organization
  claim: An organization can have up to 10,000 service control policies and up to 2000 resource control policies.
  scope: per organization; maximum; not adjustable.
  link: [10,000](../facts/organizations.md#organizations-policies-per-organization)
  link: [2000](../facts/organizations.md#organizations-policies-per-organization)
  say: ten thousand | two thousand
organizations-policy-categories-authorization-declarative
  claim: Organizations has two broad categories of policy: authorization policies (SCPs and RCPs) manage the security of accounts, and declarative policies configure and manage AWS services and their features across the organization.
  scope: AWS Organizations policy types.
  link: [centrally manage the security of AWS accounts](../facts/organizations.md#organizations-policy-categories-authorization-declarative)
  link: [centrally configure and manage AWS services](../facts/organizations.md#organizations-policy-categories-authorization-declarative)
  link: [service control policies (SCPs)](../facts/organizations.md#organizations-policy-categories-authorization-declarative)
organizations-policy-targets-unlimited
  claim: The number of targets (root, OUs, accounts) that one policy can be attached to is unlimited.
  scope: per policy; maximum; not adjustable.
  link: [Unlimited](../facts/organizations.md#organizations-policy-targets-unlimited)
  say: unlimited
organizations-protect-accounts-from-closure-iam-policy
  claim: To protect member accounts from accidental closure, attach an IAM policy that denies account closure, listing protected accounts by ARN or matching them by tag with aws:ResourceTag.
  scope: member accounts in an organization.
  link: [IAM policy that specifies which accounts are exempt](../facts/organizations.md#organizations-protect-accounts-from-closure-iam-policy)
  link: [Tag individual accounts and use the aws:ResourceTag](../facts/organizations.md#organizations-protect-accounts-from-closure-iam-policy)
organizations-rcp-affects-external-principals-scp-only-internal
  claim: RCPs can affect the effective permissions of principals outside the organization that access your resources, while SCPs can affect only principals inside the organization.
  scope: SCPs and RCPs.
  link: [principals external to your organization](../facts/organizations.md#organizations-rcp-affects-external-principals-scp-only-internal)
  link: [SCPs can only impact the effective permissions](../facts/organizations.md#organizations-rcp-affects-external-principals-scp-only-internal)
  link: [principals within your AWS organization](../facts/organizations.md#organizations-rcp-affects-external-principals-scp-only-internal)
organizations-rcp-allow-only-in-rcpfullawsaccess
  claim: In RCPs the Allow effect is supported only for the RCPFullAWSAccess policy, so custom RCPs use Deny statements.
  scope: resource control policies.
  link: [The effect of Allow is only supported](../facts/organizations.md#organizations-rcp-allow-only-in-rcpfullawsaccess)
  link: [You can make use of Deny statements](../facts/organizations.md#organizations-rcp-allow-only-in-rcpfullawsaccess)
organizations-rcp-applies-to-own-resources-even-external-callers
  claim: An RCP affects only resources owned by accounts in the organization that attached it: it applies to a bucket in a member account even when users from an outside account access it, but not to resources in that outside account.
  scope: resources in member accounts.
  link: [affect only resources](../facts/organizations.md#organizations-rcp-applies-to-own-resources-even-external-callers)
  link: [don't affect resources from accounts outside the organization](../facts/organizations.md#organizations-rcp-applies-to-own-resources-even-external-callers)
organizations-rcp-max-attached-per-entity
  claim: You can attach at most 5 RCPs directly to the root, to each OU and to each account; the RCPFullAWSAccess policy is attached automatically, cannot be detached and counts toward that quota.
  scope: per root, per OU, per account (directly attached); maximum; not adjustable; hard limit; inherited policies do not count.
  link: [5](../facts/organizations.md#organizations-rcp-max-attached-per-entity)
  link: [RCPFullAWSAccess](../facts/organizations.md#organizations-rcp-max-attached-per-entity)
  say: five | R-C-P full A-W-S access
organizations-rcp-not-aws-managed-kms-keys
  claim: RCPs do not apply to AWS managed keys in AWS KMS.
  scope: AWS managed keys for AWS KMS.
  link: [RCPs do not apply to AWS managed keys](../facts/organizations.md#organizations-rcp-not-aws-managed-kms-keys)
  link: [You cannot change or manage their permissions](../facts/organizations.md#organizations-rcp-not-aws-managed-kms-keys)
organizations-rcp-only-with-all-features
  claim: RCPs are available only in an organization that has all features enabled, not with consolidated billing only.
  scope: resource control policies.
  link: [only in an organization that has all features](../facts/organizations.md#organizations-rcp-only-with-all-features)
  link: [RCPs aren't available](../facts/organizations.md#organizations-rcp-only-with-all-features)
organizations-rcp-resource-policy-cannot-override
  claim: If an RCP blocks a permission at any level above an account, a resource in that account does not have the permission, even when its owner attaches a resource-based policy that allows full access.
  scope: resources in member accounts with an applicable RCP.
  link: [does not have that permission](../facts/organizations.md#organizations-rcp-resource-policy-cannot-override)
  link: [allows full access to any user](../facts/organizations.md#organizations-rcp-resource-policy-cannot-override)
organizations-rcpfullawsaccess-cannot-detach
  claim: When RCPs are enabled, the AWS managed policy RCPFullAWSAccess is attached to the root, every OU and every account; it cannot be detached, it lets all requests pass RCP evaluation, and it does not grant access.
  scope: organization root, every OU and every account; fixed; not adjustable; RCP policy type enabled.
  link: [You cannot detach this policy](../facts/organizations.md#organizations-rcpfullawsaccess-cannot-detach)
  link: [This AWS managed policy does not grant access](../facts/organizations.md#organizations-rcpfullawsaccess-cannot-detach)
organizations-recommended-foundational-ous
  claim: The foundational OUs AWS recommends are the Security OU, for accounts that apply security policies and compliance controls across the organization, and the Infrastructure OU, for accounts that host shared core infrastructure and networking.
  scope: AWS recommended OU structure.
  link: [Security OU](../facts/organizations.md#organizations-recommended-foundational-ous)
  link: [Infrastructure OU](../facts/organizations.md#organizations-recommended-foundational-ous)
organizations-recommended-suspended-policy-staging-ous
  claim: Among the procedural OUs AWS recommends are a Suspended OU for accounts suspended or deactivated for security or administrative reasons, and a Policy Staging OU to test new or changed organization policies before applying them to production.
  scope: AWS recommended OU structure.
  link: [Suspended OU](../facts/organizations.md#organizations-recommended-suspended-policy-staging-ous)
  link: [Policy Staging OU](../facts/organizations.md#organizations-recommended-suspended-policy-staging-ous)
organizations-recommended-workloads-sandbox-ous
  claim: AWS recommends a Workloads OU for business workloads, both production and non-production, and a Sandbox OU for experimentation, testing and development with limited access to production resources.
  scope: AWS recommended OU structure.
  link: [Workloads OU](../facts/organizations.md#organizations-recommended-workloads-sandbox-ous)
  link: [Sandbox OU](../facts/organizations.md#organizations-recommended-workloads-sandbox-ous)
organizations-remove-account-needs-standalone-info
  claim: An account can be removed from an organization only if it has what a standalone account needs: a support plan, verified contact information and a current payment method.
  scope: member account being removed from an organization.
  link: [only if the account has the information](../facts/organizations.md#organizations-remove-account-needs-standalone-info)
  link: [provide a current payment method](../facts/organizations.md#organizations-remove-account-needs-standalone-info)
organizations-remove-created-account-wait-four-days
  claim: An account created in the organization can be removed only 4 days or more after it was created; invited accounts have no waiting period.
  scope: account created in the organization; minimum; not for invited accounts.
  link: [at least four days](../facts/organizations.md#organizations-remove-created-account-wait-four-days)
  link: [Invited accounts aren't subject to this waiting period](../facts/organizations.md#organizations-remove-created-account-wait-four-days)
  say: at least four days
organizations-remove-delegated-admin-deregister-first
  claim: An account that is a delegated administrator for any AWS service enabled for the organization cannot be removed until it is deregistered.
  scope: member account being removed from an organization; the account is a delegated administrator.
  link: [must not be a delegated administrator account](../facts/organizations.md#organizations-remove-delegated-admin-deregister-first)
  link: [you must first deregister it](../facts/organizations.md#organizations-remove-delegated-admin-deregister-first)
organizations-removed-account-access-role-not-deleted
  claim: When a member account is removed, the IAM role that gave the management account access is not deleted automatically; to end that access you must delete the role by hand.
  scope: account removed from an organization.
  link: [isn't automatically deleted](../facts/organizations.md#organizations-removed-account-access-role-not-deleted)
  link: [you must manually delete the IAM role](../facts/organizations.md#organizations-removed-account-access-role-not-deleted)
organizations-removed-account-not-subject-to-policies
  claim: After an account leaves an organization, its principals are no longer affected by any organization policy, so SCP restrictions are gone and its users and roles might have more permissions.
  scope: account removed from or leaving an organization.
  link: [restrictions imposed by SCPs are gone](../facts/organizations.md#organizations-removed-account-not-subject-to-policies)
  link: [might have more permissions than they had before](../facts/organizations.md#organizations-removed-account-not-subject-to-policies)
organizations-ri-sp-benefit-owner-account-first
  claim: With organization-wide sharing, a commitment benefits the account that owns it first, and the remaining benefit can then be shared with other accounts in the organization.
  scope: organization-wide RI and Savings Plans sharing.
  link: [Commitments benefit the account owner first](../facts/organizations.md#organizations-ri-sp-benefit-owner-account-first)
  link: [remaining benefits can be shared](../facts/organizations.md#organizations-ri-sp-benefit-owner-account-first)
organizations-root-access-management-new-accounts-no-root-creds
  claim: After root access management is enabled, newly created member accounts have no root user credentials, and accounts created in Organizations have no root user credentials by default.
  scope: member accounts created in AWS Organizations; default; adjustable.
  link: [newly created member accounts are secure-by-default](../facts/organizations.md#organizations-root-access-management-new-accounts-no-root-creds)
  link: [have no root user credentials by default](../facts/organizations.md#organizations-root-access-management-new-accounts-no-root-creds)
organizations-scp-admin-policy-cannot-override
  claim: If any level above an account blocks a permission, implicitly or explicitly, users and roles in that account cannot use it, even when the account administrator attaches AdministratorAccess.
  scope: member accounts under an SCP.
  link: [can't use that permission](../facts/organizations.md#organizations-scp-admin-policy-cannot-override)
  link: [attaches the AdministratorAccess IAM policy](../facts/organizations.md#organizations-scp-admin-policy-cannot-override)
organizations-scp-allow-list-strategy
  claim: You can replace FullAWSAccess with an SCP that allows only a set of services, so that new AWS services are not allowed until the SCPs are updated to allow them explicitly.
  scope: SCP strategy.
  link: [You can replace FullAWSAccess with a policy](../facts/organizations.md#organizations-scp-allow-list-strategy)
  link: [new AWS services are not allowed](../facts/organizations.md#organizations-scp-allow-list-strategy)
organizations-scp-allow-needed-at-every-level
  claim: For a permission to be allowed in an account, an explicit Allow SCP statement must exist at every level from the root through each OU in the path to the account, including the account itself.
  scope: SCP evaluation for one member account.
  link: [at every level from the root](../facts/organizations.md#organizations-scp-allow-needed-at-every-level)
  link: [there must be an explicit Allow statement](../facts/organizations.md#organizations-scp-allow-needed-at-every-level)
organizations-scp-applies-to-delegated-admin-accounts
  claim: SCPs affect only member accounts, which means they also apply to member accounts that are designated as delegated administrators.
  scope: member accounts, including delegated administrator accounts.
  link: [designated as delegated administrators](../facts/organizations.md#organizations-scp-applies-to-delegated-admin-accounts)
  link: [They affect only the member accounts](../facts/organizations.md#organizations-scp-applies-to-delegated-admin-accounts)
organizations-scp-condition-principal-arn-allow
  claim: An SCP Allow statement can use a Condition on aws:PrincipalArn to permit specific principals to access AWS services.
  scope: SCP Condition element.
  link: [use a condition element with an allow statement](../facts/organizations.md#organizations-scp-condition-principal-arn-allow)
  link: [permit specific principals to access AWS services](../facts/organizations.md#organizations-scp-condition-principal-arn-allow)
organizations-scp-controls-which-resources-identities-access
  claim: SCPs control which resources your identities can access, for example to stop your identities from reaching resources outside the organization; RCPs control which identities can access your resources, for example to stop external identities.
  scope: SCPs and RCPs.
  link: [control which resources your identities can access](../facts/organizations.md#organizations-scp-controls-which-resources-identities-access)
  link: [control which identities can access your resources](../facts/organizations.md#organizations-scp-controls-which-resources-identities-access)
organizations-scp-deny-at-any-level-applies-below
  claim: Any SCP from the root down to the account can deny a permission, and a Deny attached at any level applies to all OUs and member accounts beneath it.
  scope: SCP evaluation.
  link: [any SCP from the root through each OU](../facts/organizations.md#organizations-scp-deny-at-any-level-applies-below)
  link: [all the OUs and member accounts underneath it](../facts/organizations.md#organizations-scp-deny-at-any-level-applies-below)
organizations-scp-deny-by-default-model
  claim: SCP evaluation follows a deny-by-default model: any permission that the SCPs do not explicitly allow is denied.
  scope: SCP evaluation.
  link: [a deny-by-default model](../facts/organizations.md#organizations-scp-deny-by-default-model)
  link: [not explicitly allowed in the SCPs are denied](../facts/organizations.md#organizations-scp-deny-by-default-model)
organizations-scp-deny-leave-and-close-recommended
  claim: Member accounts can leave the organization or close themselves, so AWS recommends an SCP at the root that denies organizations:LeaveOrganization and account:CloseAccount.
  scope: member accounts of an organization.
  link: [can leave your organization or close themselves](../facts/organizations.md#organizations-scp-deny-leave-and-close-recommended)
  link: [attach an SCP at the root](../facts/organizations.md#organizations-scp-deny-leave-and-close-recommended)
  link: [organizations:LeaveOrganization and account:CloseAccount](../facts/organizations.md#organizations-scp-deny-leave-and-close-recommended)
organizations-scp-deny-list-strategy
  claim: With a deny-list SCP, every service that is not named in the SCP's Deny statement is allowed; Deny statements at the root or an OU affect all accounts under it.
  scope: SCP strategy; FullAWSAccess remains attached.
  link: [All services that aren't listed](../facts/organizations.md#organizations-scp-deny-list-strategy)
  link: [they affect all the accounts under it](../facts/organizations.md#organizations-scp-deny-list-strategy)
organizations-scp-disable-type-detaches-all
  claim: Disabling the SCP policy type in a root detaches all SCPs from every entity in that root; if SCPs are enabled again, only FullAWSAccess is attached and the old attachments are lost.
  scope: an organization root; SCP policy type disabled.
  link: [all SCPs are automatically detached](../facts/organizations.md#organizations-scp-disable-type-detaches-all)
  link: [are lost and aren't automatically recoverable](../facts/organizations.md#organizations-scp-disable-type-detaches-all)
organizations-scp-examples-coarse-grained-deny-list
  claim: SCPs are meant as coarse-grained guardrails that do not grant access, and the AWS example SCPs use a deny-list strategy that also needs FullAWSAccess or another allowing policy attached.
  scope: AWS example SCPs.
  link: [coarse-grained guardrails](../facts/organizations.md#organizations-scp-examples-coarse-grained-deny-list)
  link: [use a deny list strategy](../facts/organizations.md#organizations-scp-examples-coarse-grained-deny-list)
organizations-scp-max-attached-per-entity
  claim: You can attach at most 10 SCPs directly to the root, to each OU and to each account, and every entity must keep at least 1 SCP attached while SCPs are enabled. Before May 15, 2026 the maximum was 5 SCPs per entity.
  scope: per root, per OU, per account (directly attached; inherited policies do not count); maximum; not adjustable; all policy limits on this table are hard limits.
  link: [10](../facts/organizations.md#organizations-scp-max-attached-per-entity)
  link: [at least one SCP attached](../facts/organizations.md#organizations-scp-max-attached-per-entity)
  say: ten | at least one
  changed: 2026-05-15: was 5
organizations-scp-max-document-size
  claim: A service control policy document can be at most 10,240 characters, while a resource control policy can be at most 5120 characters. Before May 15, 2026 the SCP maximum was 5,120 characters.
  scope: per policy document; maximum; not adjustable; the console removes extra white space before counting; the CLI and SDKs save the policy exactly as provided.
  link: [10,240 characters](../facts/organizations.md#organizations-scp-max-document-size)
  link: [5120 characters](../facts/organizations.md#organizations-scp-max-document-size)
  say: ten thousand two hundred forty characters | five thousand one hundred twenty characters
  changed: 2026-05-15: was 5,120 characters
organizations-scp-no-effect-on-management-account
  claim: SCPs affect only member accounts; they have no effect on users or roles in the management account, and they do not affect service-linked roles.
  scope: per organization.
  link: [affect only member accounts](../facts/organizations.md#organizations-scp-no-effect-on-management-account)
  link: [users or roles in the management account](../facts/organizations.md#organizations-scp-no-effect-on-management-account)
  link: [do not affect any service-linked role](../facts/organizations.md#organizations-scp-no-effect-on-management-account)
organizations-scp-notaction-region-limit-example
  claim: An SCP Deny statement with NotAction and an aws:RequestedRegion condition can limit accounts to approved Regions while exempting the services listed in NotAction.
  scope: SCP with Deny, NotAction and aws:RequestedRegion.
  link: [use a NotAction element to exclude AWS services](../facts/organizations.md#organizations-scp-notaction-region-limit-example)
  link: [restrict access to any operations outside](../facts/organizations.md#organizations-scp-notaction-region-limit-example)
  link: [except for actions in the specified services](../facts/organizations.md#organizations-scp-notaction-region-limit-example)
organizations-scp-principal-centric-rcp-resource-centric
  claim: SCPs are principal-centric controls that limit the maximum permissions of principals in member accounts; RCPs are resource-centric controls that limit the maximum permissions available for resources in member accounts.
  scope: authorization policies in member accounts.
  link: [SCPs are principal-centric controls](../facts/organizations.md#organizations-scp-principal-centric-rcp-resource-centric)
  link: [RCPs are resource-centric controls](../facts/organizations.md#organizations-scp-principal-centric-rcp-resource-centric)
organizations-scp-rcp-independent-data-perimeter
  claim: SCPs and RCPs are independent controls; you can enable either one or both, and using both builds a data perimeter around your identities and your resources.
  scope: SCPs and RCPs.
  link: [SCPs and RCPs are independent controls](../facts/organizations.md#organizations-scp-rcp-independent-data-perimeter)
  link: [data perimeter around your identities and your resources](../facts/organizations.md#organizations-scp-rcp-independent-data-perimeter)
organizations-scp-test-in-ou-not-root
  claim: AWS strongly recommends not attaching an SCP to the root without testing its impact; instead move accounts one at a time, or in small numbers, into a test OU.
  scope: rolling out SCPs.
  link: [don't attach SCPs to the root](../facts/organizations.md#organizations-scp-test-in-ou-not-root)
  link: [OU that you can move your accounts into](../facts/organizations.md#organizations-scp-test-in-ou-not-root)
organizations-scp-user-without-iam-policy-has-no-access
  claim: Users and roles still need IAM permission policies: a user without any IAM permission policy has no access, even when the SCPs allow all services and actions.
  scope: IAM users and roles in member accounts.
  link: [has no access](../facts/organizations.md#organizations-scp-user-without-iam-policy-has-no-access)
  link: [even if the applicable SCPs allow all services](../facts/organizations.md#organizations-scp-user-without-iam-policy-has-no-access)
organizations-security-tooling-account-delegated-admin
  claim: The Security Tooling (Audit) account provides centralized delegated administrator access to AWS security tools and view-only investigative access into all accounts; it aggregates services such as Security Hub CSPM, GuardDuty, Macie, Firewall Manager, Detective, Inspector and IAM Access Analyzer.
  scope: Security Tooling account in the Security OU.
  link: [centralized delegated admin access to AWS security tooling](../facts/organizations.md#organizations-security-tooling-account-delegated-admin)
  link: [an aggregation point](../facts/organizations.md#organizations-security-tooling-account-delegated-admin)
organizations-sensitive-data-dedicated-accounts
  claim: Limiting sensitive data stores to dedicated accounts lets you control access more tightly and restrict permissions at the coarse-grained account level instead of managing fine-grained access in one broad account.
  scope: multi-account strategy.
  link: [limiting sensitive data stores to dedicated accounts](../facts/organizations.md#organizations-sensitive-data-dedicated-accounts)
  link: [at the coarse-grained account level](../facts/organizations.md#organizations-sensitive-data-dedicated-accounts)
organizations-separate-accounts-prod-nonprod-by-default
  claim: Using separate accounts for non-production and production separates, by default, the resources and data of one workload environment from other environments and workloads, so each can have its own security and operational controls.
  scope: multi-account strategy.
  link: [separate accounts for the non-production and production environments](../facts/organizations.md#organizations-separate-accounts-prod-nonprod-by-default)
  link: [by default, the resources and data](../facts/organizations.md#organizations-separate-accounts-prod-nonprod-by-default)
organizations-single-organization-recommended
  claim: AWS recommends one organization for all your accounts, because an organization is a security boundary that keeps policies and configuration consistent across accounts.
  scope: multi-account environment.
  link: [creating a single organization](../facts/organizations.md#organizations-single-organization-recommended)
  link: [An organization is a security boundary](../facts/organizations.md#organizations-single-organization-recommended)
organizations-stacksets-provision-to-accounts
  claim: With Organizations you can create accounts programmatically and centrally provision recommended resources and permissions to them with AWS CloudFormation StackSets, for example per group of development and production accounts.
  scope: AWS Organizations with CloudFormation StackSets.
  link: [programmatically creating new accounts](../facts/organizations.md#organizations-stacksets-provision-to-accounts)
  link: [AWS CloudFormation StackSets](../facts/organizations.md#organizations-stacksets-provision-to-accounts)
organizations-tag-policy-enforced-blocks-noncompliant-tagging
  claim: A tag policy can enforce compliance on specified resource types, which prevents noncompliant tagging requests on those resource types from completing.
  scope: tag policies with enforcement; enforcement set for the resource type.
  link: [noncompliant tagging operations on specified resource types](../facts/organizations.md#organizations-tag-policy-enforced-blocks-noncompliant-tagging)
  link: [are prevented from completing](../facts/organizations.md#organizations-tag-policy-enforced-blocks-noncompliant-tagging)
organizations-tag-policy-standardizes-tags
  claim: Tag policies standardize tags on resources in the organization's accounts; untagged resources and tags not defined in the tag policy are not evaluated for compliance.
  scope: tag policies.
  link: [standardize the tags attached to the AWS resources](../facts/organizations.md#organizations-tag-policy-standardizes-tags)
  link: [Untagged resources or tags that aren't defined](../facts/organizations.md#organizations-tag-policy-standardizes-tags)
  link: [aren't evaluated for compliance with the tag policy](../facts/organizations.md#organizations-tag-policy-standardizes-tags)
organizations-tags-per-root-ou-account
  claim: The Organizations quota page lists 50 as the number of tags that you can attach to a root, an OU or an account; it calls these values default maximums and says you can request increases for some of them.
  scope: per root, OU or account; default; listed among default maximums; increases can be requested for some of these values.
  link: [50](../facts/organizations.md#organizations-tags-per-root-ou-account)
  say: fifty
organizations-trusted-access-service-acts-on-behalf
  claim: Trusted access lets a supported AWS service perform tasks in your organization and its accounts on your behalf by creating service-linked roles; it does not otherwise change the permissions of users or roles.
  scope: AWS services integrated with Organizations.
  link: [perform tasks in your organization and its accounts](../facts/organizations.md#organizations-trusted-access-service-acts-on-behalf)
  link: [create an IAM role called a service-linked role](../facts/organizations.md#organizations-trusted-access-service-acts-on-behalf)
organizations-wa-root-user-most-privileged
  claim: The Well-Architected security pillar says the root user is the most privileged user in an account and in some cases cannot be constrained by security policies; in an organization, secure the management account's root user first, and preventative controls can be placed on member account root users.
  scope: AWS Well-Architected SEC01-BP02.
  link: [the most privileged user in an AWS account](../facts/organizations.md#organizations-wa-root-user-most-privileged)
  link: [cannot be constrained by security policies](../facts/organizations.md#organizations-wa-root-user-most-privileged)
  link: [Prioritize securing your management account’s root user](../facts/organizations.md#organizations-wa-root-user-most-privileged)
organizations-when-scp-when-rcp
  claim: Use an SCP to limit the permissions of IAM principals inside the organization's member accounts; use an RCP to restrict principals outside the organization that request access to resources in member accounts.
  scope: authorization policies.
  link: [an SCP when you need to limit permissions](../facts/organizations.md#organizations-when-scp-when-rcp)
  link: [RCP when you need to restrict IAM principals](../facts/organizations.md#organizations-when-scp-when-rcp)
ram-az-names-differ-use-az-ids
  claim: AWS maps physical Availability Zones randomly to AZ names for each account, so us-east-1a in one account may be a different location in another; an AZ ID such as use1-az1 is the same physical location in every account, and a shared subnet is available in the consumer's AZ with the same AZ ID.
  scope: subnets shared across accounts.
  link: [maps the physical Availability Zones randomly](../facts/ram.md#ram-az-names-differ-use-az-ids)
  link: [the same physical location in every AWS account](../facts/ram.md#ram-az-names-differ-use-az-ids)
  link: [whose AZ ID is also use1-az2](../facts/ram.md#ram-az-names-differ-use-az-ids)
ram-cannot-add-outside-org-or-ous
  claim: You can add only your own organization and its OUs as principals of a resource share, not organizations or OUs from outside; outside principals can be added only as individual accounts or, for supported services, IAM roles and users.
  scope: RAM resource share principals.
  link: [You can add only the organization](../facts/ram.md#ram-cannot-add-outside-org-or-ous)
  link: [can't add OUs or organizations from outside](../facts/ram.md#ram-cannot-add-outside-org-or-ous)
ram-change-customer-managed-permissions-2023-04
  claim: On 2023-04-19 AWS RAM added customer managed permissions in the console, so you can author and maintain fine-grained resource access controls for supported resource types.
  scope: per resource type; supported resource types.
  link: [2023-04-19](../facts/ram.md#ram-change-customer-managed-permissions-2023-04)
  link: [fine-grained resource access controls](../facts/ram.md#ram-change-customer-managed-permissions-2023-04)
  say: April nineteenth, twenty twenty-three | fine-grained resource access controls
ram-change-ebs-volumes-shareable-2026-08
  claim: On 2026-08-20 AWS RAM added support for sharing Amazon EBS volumes with other AWS accounts or your organization.
  scope: per EBS volume.
  link: [2026-08-20](../facts/ram.md#ram-change-ebs-volumes-shareable-2026-08)
  link: [Amazon Elastic Block Store (Amazon EBS) volumes](../facts/ram.md#ram-change-ebs-volumes-shareable-2026-08)
  say: August twentieth, twenty twenty-six | Amazon EBS volumes
ram-change-eventbridge-buses-shareable-2026-09
  claim: On 2026-09-24 AWS RAM added support for sharing Amazon EventBridge custom event buses with other AWS accounts, or with IAM roles and users.
  scope: per custom event bus.
  link: [2026-09-24](../facts/ram.md#ram-change-eventbridge-buses-shareable-2026-09)
  link: [custom event buses](../facts/ram.md#ram-change-eventbridge-buses-shareable-2026-09)
  say: September twenty-fourth, twenty twenty-six | custom event buses
ram-change-pending-invitations-250-2023-06
  claim: On 2023-06-08 AWS RAM increased the maximum number of pending invitations per sharing account from 20 to 250; 250 is the default quota today, and it is adjustable.
  scope: per sharing account; default.
  link: [2023-06-08](../facts/ram.md#ram-change-pending-invitations-250-2023-06)
  link: [250](../facts/ram.md#ram-change-pending-invitations-250-2023-06)
  link: [20](../facts/ram.md#ram-change-pending-invitations-250-2023-06)
  say: June eighth, twenty twenty-three | two hundred fifty | twenty
  changed: 2023-06-08: was 20
ram-change-security-groups-shareable-2024-10
  claim: On 2024-10-30 AWS RAM added support for sharing Amazon VPC security groups; the current list of shareable resources says a security group can be shared with only AWS accounts in its own organization.
  scope: per security group; shareable with only AWS accounts in the same organization.
  link: [2024-10-30](../facts/ram.md#ram-change-security-groups-shareable-2024-10)
  link: [share Amazon VPC Security groups](../facts/ram.md#ram-change-security-groups-shareable-2024-10)
  say: October thirtieth, twenty twenty-four | share Amazon VPC security groups
ram-change-vpc-lattice-shareable-2023-03
  claim: On 2023-03-31 AWS RAM added support for sharing Amazon VPC Lattice services and service networks with other AWS accounts.
  scope: per VPC Lattice service or service network.
  link: [2023-03-31](../facts/ram.md#ram-change-vpc-lattice-shareable-2023-03)
  link: [VPC Lattice service and service network](../facts/ram.md#ram-change-vpc-lattice-shareable-2023-03)
  say: March thirty-first, twenty twenty-three | VPC Lattice services and service networks
ram-consumer-account-policies-apply
  claim: Sharing a resource grants principals in the consuming account access to it, and the policies and permissions that apply to roles and users in the consuming account also apply to the shared resource.
  scope: AWS RAM consuming accounts.
  link: [granting access for principals in the consuming account](../facts/ram.md#ram-consumer-account-policies-apply)
  link: [also apply to the shared resource](../facts/ram.md#ram-consumer-account-policies-apply)
ram-customer-managed-permissions-quota
  claim: By default an account can have at most 1,500 customer managed permissions in AWS RAM in each supported Region, and this quota is adjustable.
  scope: per account, in each supported Region; default; adjustable.
  link: [1,500](../facts/ram.md#ram-customer-managed-permissions-quota)
  say: one thousand five hundred
ram-disable-trusted-access-removes-org-principals
  claim: When trusted access between RAM and AWS Organizations is disabled, principals in the organization are removed from all resource shares and lose access to the shared resources.
  scope: RAM integration with AWS Organizations; trusted access disabled.
  link: [removed from all resource shares](../facts/ram.md#ram-disable-trusted-access-removes-org-principals)
  link: [lose access to those shared resources](../facts/ram.md#ram-disable-trusted-access-removes-org-principals)
ram-enable-sharing-in-ram-console-not-orgs
  claim: Sharing with AWS Organizations must be enabled from the RAM console or CLI so that the RAM service-linked role is created; enabling trusted access from the Organizations console does not create the role, and then you cannot share within the organization.
  scope: RAM integration with AWS Organizations.
  link: [You must enable sharing with AWS Organizations](../facts/ram.md#ram-enable-sharing-in-ram-console-not-orgs)
  link: [you can't share resources within your organization](../facts/ram.md#ram-enable-sharing-in-ram-console-not-orgs)
ram-faq-aws-managed-permission-default-per-type
  claim: AWS managed permissions are created and maintained by AWS, and every resource type has a default AWS managed permission.
  scope: per resource type in a resource share; default; not adjustable.
  link: [created and maintained by AWS](../facts/ram.md#ram-faq-aws-managed-permission-default-per-type)
  link: [has a default AWS managed permission](../facts/ram.md#ram-faq-aws-managed-permission-default-per-type)
ram-faq-control-access-with-iam-policies
  claim: An account controls access to resources shared with it by using IAM policies.
  scope: accounts that receive shared resources.
  link: [You can specify IAM policies](../facts/ram.md#ram-faq-control-access-with-iam-policies)
ram-faq-iam-roles-users-supported-types
  claim: AWS RAM can share with IAM roles and IAM users only for supported resource types.
  scope: RAM principals of type IAM role or IAM user.
  link: [For supported resource types](../facts/ram.md#ram-faq-iam-roles-users-supported-types)
ram-faq-monitor-cloudtrail-and-events
  claim: All AWS RAM API calls are logged in AWS CloudTrail, and events are sent whenever resource shares change.
  scope: AWS RAM API calls and resource shares.
  link: [logged in AWS CloudTrail](../facts/ram.md#ram-faq-monitor-cloudtrail-and-events)
  link: [triggered whenever there are changes to resource shares](../facts/ram.md#ram-faq-monitor-cloudtrail-and-events)
ram-faq-no-additional-cost
  claim: Sharing resources with AWS RAM has no additional cost.
  scope: AWS RAM resource sharing.
  link: [share resources at no additional cost](../facts/ram.md#ram-faq-no-additional-cost)
ram-faq-one-managed-permission-per-resource-type
  claim: A managed permission defines the actions, conditions and principals for a resource type in a resource share, and each resource type is associated with either an AWS managed or a customer managed permission.
  scope: resource types in a resource share.
  link: [AWS managed permission or a customer managed permission](../facts/ram.md#ram-faq-one-managed-permission-per-resource-type)
ram-faq-resource-share-steps
  claim: To share with AWS RAM, you add resources to a resource share, choose a managed permission for each resource type, and specify who gets access.
  scope: creating a resource share.
  link: [choosing a managed permission](../facts/ram.md#ram-faq-resource-share-steps)
ram-faq-share-with-any-account-ous-if-enabled
  claim: AWS RAM can share with any AWS account; sharing with OUs or the whole organization is possible when sharing within the organization is enabled.
  scope: AWS RAM principals.
  link: [You can share resources with any AWS account.](../facts/ram.md#ram-faq-share-with-any-account-ous-if-enabled)
  link: [sharing within your organization is enabled](../facts/ram.md#ram-faq-share-with-any-account-ous-if-enabled)
ram-faq-shared-resources-in-service-console-and-apis
  claim: Resources shared with an account also appear in the console pages and the List and Describe APIs of their resource type, next to the account's own resources.
  scope: accounts that receive shared resources.
  link: [respective List/Describe APIs for those resource types](../facts/ram.md#ram-faq-shared-resources-in-service-console-and-apis)
ram-faq-stop-sharing
  claim: You can stop sharing a resource by removing it from the resource share or by deleting the resource share.
  scope: resource owner of a resource share.
  link: [removing it from the resource share](../facts/ram.md#ram-faq-stop-sharing)
  link: [deleting the resource share](../facts/ram.md#ram-faq-stop-sharing)
ram-managed-permission-generates-resource-policy
  claim: After you create a resource share, RAM uses the managed permission to generate a resource-based policy that it attaches to each shared resource; the effect of a managed permission is always Allow.
  scope: RAM managed permissions.
  link: [generate a resource-based policy](../facts/ram.md#ram-managed-permission-generates-resource-policy)
  link: [the effect is always Allow](../facts/ram.md#ram-managed-permission-generates-resource-policy)
ram-managed-permissions-aws-and-customer
  claim: RAM has two types of managed permissions: AWS managed permissions, with one default permission for every supported resource type, and customer managed permissions that you author to grant only the actions you need (least privilege).
  scope: RAM managed permissions.
  link: [AWS managed permissions and customer managed permissions](../facts/ram.md#ram-managed-permissions-aws-and-customer)
  link: [default managed permission available for every resource type](../facts/ram.md#ram-managed-permissions-aws-and-customer)
  link: [that you author and maintain](../facts/ram.md#ram-managed-permissions-aws-and-customer)
ram-org-sharing-no-invitations
  claim: To share within an organization you first enable sharing with AWS Organizations in RAM; then RAM sends no invitations and principals in the organization get access without exchanging invitations.
  scope: RAM sharing within an organization; sharing with AWS Organizations enabled.
  link: [you must first use the AWS RAM console](../facts/ram.md#ram-org-sharing-no-invitations)
  link: [AWS RAM doesn't send invitations to principals](../facts/ram.md#ram-org-sharing-no-invitations)
ram-outside-org-needs-invitation
  claim: When RAM shares with an account outside the organization, it starts an invitation process and the recipient must accept the invitation before it can access the shared resources.
  scope: RAM sharing outside the organization; resource type allows sharing outside the organization.
  link: [AWS RAM initiates an invitation process](../facts/ram.md#ram-outside-org-needs-invitation)
  link: [The recipient must accept the invitation](../facts/ram.md#ram-outside-org-needs-invitation)
ram-pending-invitations-per-sharing-account
  claim: A sharing account can have at most 250 pending invitations by default, and the quota is adjustable; it applies only to accounts sharing with accounts outside their AWS organization, a receiving account has no quota on pending invitations, and invitations are not used when sharing within an organization that has resource sharing turned on.
  scope: per sharing account; default; adjustable; only for sharing with accounts outside the same organization.
  link: [250](../facts/ram.md#ram-pending-invitations-per-sharing-account)
  say: two hundred fifty
ram-principals-per-resource-share
  claim: A resource share can have 5,000 principal associations (the default quota), and this quota is not adjustable.
  scope: per resource share; default; not adjustable.
  link: [5,000](../facts/ram.md#ram-principals-per-resource-share)
  say: five thousand
ram-reduces-overhead-no-duplicate-resources
  claim: RAM reduces operational overhead because a resource is created once and shared, so you do not provision duplicate resources in every account, and all users of a share are managed by a single set of policies and permissions.
  scope: AWS RAM.
  link: [eliminates the need to provision duplicate resources](../facts/ram.md#ram-reduces-overhead-no-duplicate-resources)
  link: [a single set of policies and permissions](../facts/ram.md#ram-reduces-overhead-no-duplicate-resources)
ram-regional-resources-used-in-their-region
  claim: Most resources shared with RAM are Regional: they exist in the Region where they were created, you must direct operations to that Region to use them, and a resource share is visible only in the Region where it was created.
  scope: Regional resources shared with RAM.
  link: [share with AWS RAM are Regional](../facts/ram.md#ram-regional-resources-used-in-their-region)
  link: [you must direct your operations to that Region](../facts/ram.md#ram-regional-resources-used-in-their-region)
  link: [visible in only the AWS Region](../facts/ram.md#ram-regional-resources-used-in-their-region)
ram-resource-associations-per-region
  claim: By default an account can have at most 25,000 resource associations across all its resource shares in a Region, and this quota is adjustable; a resource included in 10 different resource shares counts 10 against this limit.
  scope: per account, per Region, across all resource shares; default; adjustable; each inclusion of a resource in a share counts once.
  link: [25,000](../facts/ram.md#ram-resource-associations-per-region)
  say: twenty-five thousand
ram-resource-shares-per-region
  claim: By default an account can have at most 25,000 resource shares per AWS Region, and this quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [25,000](../facts/ram.md#ram-resource-shares-per-region)
  say: twenty-five thousand
ram-resources-per-resource-share
  claim: A resource share can have 5,000 resource associations (the default quota), and this quota is not adjustable.
  scope: per resource share; default; not adjustable.
  link: [5,000](../facts/ram.md#ram-resources-per-resource-share)
  say: five thousand
ram-scp-can-prevent-external-sharing
  claim: An SCP can prevent users from creating resource shares that allow sharing with principals outside the sharing user's organization, and another example SCP blocks principals from accepting resource share invitations.
  scope: SCPs applied to AWS RAM; all features and SCPs enabled.
  link: [prevents users from creating resource shares](../facts/ram.md#ram-scp-can-prevent-external-sharing)
  link: [outside of the sharing user's organization](../facts/ram.md#ram-scp-can-prevent-external-sharing)
  link: [accepting an invitation to use a resource share](../facts/ram.md#ram-scp-can-prevent-external-sharing)
ram-share-across-accounts-ous-org-roles
  claim: AWS RAM securely shares your resources across AWS accounts, within your organization or OUs, and with IAM roles and users for supported resource types, so a resource is created once and used by other accounts.
  scope: AWS RAM resource shares; IAM roles and users only for supported resource types.
  link: [securely share your resources across AWS accounts](../facts/ram.md#ram-share-across-accounts-ous-org-roles)
  link: [create a resource once](../facts/ram.md#ram-share-across-accounts-ous-org-roles)
  link: [Identity and Access Management (IAM) roles and users](../facts/ram.md#ram-share-across-accounts-ous-org-roles)
ram-share-aurora-cluster-for-cloning
  claim: RAM can share an Aurora DB cluster with any AWS account so that other accounts can clone the shared, centrally managed DB cluster.
  scope: rds:Cluster resource shares.
  link: [clone a shared, centrally managed DB cluster](../facts/ram.md#ram-share-aurora-cluster-for-cloning)
  link: [Can share with any AWS account](../facts/ram.md#ram-share-aurora-cluster-for-cloning)
ram-share-by-account-id-any-account
  claim: With RAM you can share with all accounts in the organization or only with accounts in specified OUs, and you can also share with specific AWS accounts by account ID whether or not they are in an organization.
  scope: AWS RAM principals; resource type must allow sharing outside the organization.
  link: [share resources with all the other accounts](../facts/ram.md#ram-share-by-account-id-any-account)
  link: [share with specific AWS accounts by account ID](../facts/ram.md#ram-share-by-account-id-any-account)
  link: [whether the account is part of an organization](../facts/ram.md#ram-share-by-account-id-any-account)
ram-share-ipam-pools-any-account
  claim: RAM can share Amazon VPC IPAM pools with any AWS account, with IAM roles or users, or with an organization or OU, so those principals allocate CIDRs from the pool to resources such as VPCs in their own accounts.
  scope: ec2:IpamPool resource shares.
  link: [Can share with any AWS account](../facts/ram.md#ram-share-ipam-pools-any-account)
  link: [allocate CIDRs from the pool](../facts/ram.md#ram-share-ipam-pools-any-account)
ram-share-license-configurations-any-account
  claim: RAM can share AWS License Manager license configurations with any AWS account or the organization, so centrally managed licensing rules are enforced across multiple accounts.
  scope: license-manager:LicenseConfiguration resource shares.
  link: [Can share with any AWS account](../facts/ram.md#ram-share-license-configurations-any-account)
  link: [enforce centrally managed licensing rules](../facts/ram.md#ram-share-license-configurations-any-account)
ram-share-prefix-lists-any-account
  claim: RAM can share managed prefix lists with any AWS account or the organization, so multiple accounts can reference centrally managed prefix lists in their security groups and subnet route tables.
  scope: ec2:PrefixList resource shares.
  link: [Can share with any AWS account](../facts/ram.md#ram-share-prefix-lists-any-account)
  link: [reference prefix lists in their resources](../facts/ram.md#ram-share-prefix-lists-any-account)
ram-share-resolver-rules-any-account
  claim: RAM can share DNS Resolver rules (route53resolver:ResolverRule) with any AWS account, so many accounts forward DNS queries from their VPCs through shared, centrally managed Resolver rules.
  scope: route53resolver:ResolverRule resource shares.
  link: [Can share with any AWS account](../facts/ram.md#ram-share-resolver-rules-any-account)
  link: [forward DNS queries from their virtual private clouds](../facts/ram.md#ram-share-resolver-rules-any-account)
ram-share-security-groups-only-within-organization
  claim: RAM can share security groups only with AWS accounts in the same organization; participants associate the shared security group with their elastic network interfaces.
  scope: ec2:SecurityGroup resource shares.
  link: [only AWS accounts in its own organization](../facts/ram.md#ram-share-security-groups-only-within-organization)
  link: [security group with their Elastic network interfaces](../facts/ram.md#ram-share-security-groups-only-within-organization)
ram-share-subnets-only-within-organization
  claim: RAM can share VPC subnets only with AWS accounts in the same organization, not with IAM roles or users, and default subnets cannot be shared.
  scope: ec2:Subnet resource shares.
  link: [only AWS accounts in its own organization](../facts/ram.md#ram-share-subnets-only-within-organization)
  link: [Default subnets are not shareable](../facts/ram.md#ram-share-subnets-only-within-organization)
ram-share-transit-gateway-any-account
  claim: RAM can share a transit gateway with any AWS account or the organization, so many accounts route traffic between their VPCs and on-premises networks through one centrally managed transit gateway.
  scope: ec2:TransitGateway resource shares.
  link: [Can share with any AWS account](../facts/ram.md#ram-share-transit-gateway-any-account)
  link: [a shared, centrally managed transit gateway](../facts/ram.md#ram-share-transit-gateway-any-account)
ram-sharing-does-not-change-owner-quotas
  claim: Sharing a resource with principals outside the owning account does not change the permissions or quotas that apply to the resource in the account that created it.
  scope: RAM owning account.
  link: [doesn't change the permissions or quotas](../facts/ram.md#ram-sharing-does-not-change-owner-quotas)
  link: [within the account that created it](../facts/ram.md#ram-sharing-does-not-change-owner-quotas)
ram-some-types-only-within-organization
  claim: Some resource types can't be shared with any account that isn't a member of the organization; the Shareable AWS resources page shows which resource types can be shared outside the organization.
  scope: RAM resource types.
  link: [Some resource types can’t be shared](../facts/ram.md#ram-some-types-only-within-organization)
ram-tgw-shared-attachment-accept
  claim: An invited account must accept the transit gateway resource share in RAM before it can use the transit gateway, and if Auto accept shared attachments was not enabled when the transit gateway was created, cross-account (shared) attachments must be accepted manually.
  scope: transit gateway shared through RAM; Auto accept shared attachments not enabled.
  link: [You must accept the resource share](../facts/ram.md#ram-tgw-shared-attachment-accept)
  link: [you must manually accept cross-account (shared) attachment](../facts/ram.md#ram-tgw-shared-attachment-accept)
  link: [Auto accept shared attachments](../facts/ram.md#ram-tgw-shared-attachment-accept)
ram-vpc-only-owner-attaches-transit-gateway
  claim: Only the VPC owner can attach a transit gateway to a shared VPC subnet; participants cannot.
  scope: shared VPC subnets.
  link: [Only the VPC owner can attach](../facts/ram.md#ram-vpc-only-owner-attaches-transit-gateway)
  link: [Participants can't](../facts/ram.md#ram-vpc-only-owner-attaches-transit-gateway)
ram-vpc-participant-resources-count-participant-quota
  claim: Participants can create a limited set of VPC resources in a shared VPC, such as network interfaces and security groups, and those resources count against the participant account's VPC quotas, not the owner's.
  scope: participants in a shared VPC.
  link: [create a limited set of VPC resources](../facts/ram.md#ram-vpc-participant-resources-count-participant-quota)
  link: [VPC quotas in the participant account](../facts/ram.md#ram-vpc-participant-resources-count-participant-quota)
ram-vpc-participants-no-route-tables-nat
  claim: In a shared VPC subnet, participants cannot work with route tables (they can only describe them) and cannot create, delete or describe NAT gateways.
  scope: participants in a shared VPC subnet.
  link: [Participants cannot work with route tables](../facts/ram.md#ram-vpc-participants-no-route-tables-nat)
  link: [Participants cannot create, delete, or describe NAT gateways](../facts/ram.md#ram-vpc-participants-no-route-tables-nat)
ram-vs-resource-policy-org-ou-without-ids
  claim: Compared with sharing through a resource-based policy, RAM can share with an organization or OU without listing every account ID, and shared resources appear in the consumer's service console and APIs; resources shared by a resource-based policy are not visible this way and must be referenced by ARN.
  scope: AWS RAM compared with resource-based policies.
  link: [enumerate every one of the AWS account IDs](../facts/ram.md#ram-vs-resource-policy-org-ou-without-ids)
  link: [resources were directly in the user's account](../facts/ram.md#ram-vs-resource-policy-org-ou-without-ids)
  link: [shared by attaching a resource-based policy aren't visible](../facts/ram.md#ram-vs-resource-policy-org-ou-without-ids)
ram-whole-organization-counts-as-one-principal
  claim: Each shared principal referenced in a resource share adds one to the principal quota, but sharing with an entire organization by referencing its ID counts as only one.
  scope: per resource share; sharing with the organization ID.
  link: [counts as only one against this quota](../facts/ram.md#ram-whole-organization-counts-as-one-principal)
  say: counts as only one
