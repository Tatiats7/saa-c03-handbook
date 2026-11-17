facts card: 384 facts
iam-abac-no-policy-update-for-new-resources
  claim: With ABAC an administrator no longer needs to update existing policies to allow access to new resources, and fewer policies are needed because you don't create different policies for different job functions.
  scope: attribute-based access control in IAM.
  link: [no longer needs to update existing policies to allow access to new resources](../facts/iam.md#iam-abac-no-policy-update-for-new-resources)
  link: [fewer policies are needed](../facts/iam.md#iam-abac-no-policy-update-for-new-resources)
iam-abac-recommended-only-within-own-organization
  claim: The Security pillar recommends using ABAC for access control only when both the principals and the resources belong to your own organization, because an external party can use the same tag names and values.
  scope: ABAC with tags, principals and resources of your own organization.
  link: [only be used for access control when both the principals and resources are owned by your AWS Organization](../facts/iam.md#iam-abac-recommended-only-within-own-organization)
  link: [External parties may use the same tag names and values as your organization](../facts/iam.md#iam-abac-recommended-only-within-own-organization)
iam-abac-tag-match-allows-all-resources
  claim: With ABAC a policy can allow actions on all resources when the resource's tag matches the principal's tag, instead of listing specific resources as RBAC does.
  scope: attribute-based access control in IAM.
  link: [when the resource's tag matches the principal's tag](../facts/iam.md#iam-abac-tag-match-allows-all-resources)
  link: [instead of listing specific resources as RBAC does](../facts/iam.md#iam-abac-tag-match-allows-all-resources)
iam-access-analyzer-continuous-public-cross-account-findings
  claim: IAM Access Analyzer monitors supported resource types continuously and generates a finding for resources that allow public or cross-account access.
  link: [generates a finding for resources that allow public or cross-account access](../facts/iam.md#iam-access-analyzer-continuous-public-cross-account-findings)
iam-access-analyzer-custom-checks-new-access
  claim: IAM Access Analyzer custom policy checks validate policies against your own security standards: they check whether an updated policy grants new access compared to the existing version, and through the CLI and API whether critical actions are allowed.
  scope: IAM Access Analyzer custom policy checks.
  link: [grants new access compared to the existing version](../facts/iam.md#iam-access-analyzer-custom-checks-new-access)
  link: [against your own security standards](../facts/iam.md#iam-access-analyzer-custom-checks-new-access)
iam-access-analyzer-custom-policy-checks-are-paid
  claim: IAM Access Analyzer custom policy checks are a paid feature, and a charge is associated with each check for new access.
  scope: per check.
  link: [Custom policy checks are a paid feature](../facts/iam.md#iam-access-analyzer-custom-policy-checks-are-paid)
  link: [A charge is associated with each check for new access](../facts/iam.md#iam-access-analyzer-custom-policy-checks-are-paid)
iam-access-analyzer-external-finding-per-shared-resource
  claim: IAM Access Analyzer uses logic-based reasoning on resource-based policies to find resources shared with external principals, and it generates a finding for each resource shared outside your account.
  scope: IAM Access Analyzer external access analyzer.
  link: [logic-based reasoning on resource-based policies](../facts/iam.md#iam-access-analyzer-external-finding-per-shared-resource)
  link: [a finding for each resource shared outside your account](../facts/iam.md#iam-access-analyzer-external-finding-per-shared-resource)
iam-access-analyzer-external-is-regional
  claim: For external access, IAM Access Analyzer analyzes only policies of resources in the Region where it is enabled, so you must create an external access analyzer in each Region where you use supported resources.
  scope: IAM Access Analyzer external access analyzer, per Region.
  link: [analyzes only policies of resources in the Region where it is enabled](../facts/iam.md#iam-access-analyzer-external-is-regional)
  link: [create an external access analyzer in each Region](../facts/iam.md#iam-access-analyzer-external-is-regional)
iam-access-analyzer-external-resource-types
  claim: IAM Access Analyzer external access analysis covers S3 buckets and directory buckets, IAM roles, KMS keys, Lambda functions and layers, SQS queues, Secrets Manager secrets, SNS topics, EBS volume snapshots, RDS DB snapshots and DB cluster snapshots, ECR repositories, EFS file systems, and DynamoDB streams and tables.
  scope: IAM Access Analyzer external access analyzer.
  link: [S3 buckets and directory buckets, IAM roles, KMS keys, Lambda functions and layers, SQS queues](../facts/iam.md#iam-access-analyzer-external-resource-types)
  link: [EBS volume snapshots, RDS DB snapshots and DB cluster snapshots](../facts/iam.md#iam-access-analyzer-external-resource-types)
iam-access-analyzer-guides-to-least-privilege-external-internal-unused
  claim: IAM Access Analyzer helps you reach least privilege with features to set, verify, and refine permissions: it analyzes external, internal, and unused access and validates that your IAM policies match your security standards.
  link: [analyzing external, internal, and unused access](../facts/iam.md#iam-access-analyzer-guides-to-least-privilege-external-internal-unused)
  link: [set, verify, and refine permissions](../facts/iam.md#iam-access-analyzer-guides-to-least-privilege-external-internal-unused)
iam-access-analyzer-policy-generation-from-cloudtrail
  claim: IAM Access Analyzer can analyze your CloudTrail logs for the actions and services an IAM user or role used in a date range and generate an IAM policy based on that activity.
  scope: IAM Access Analyzer policy generation.
  link: [analyze your CloudTrail logs](../facts/iam.md#iam-access-analyzer-policy-generation-from-cloudtrail)
  link: [generate an IAM policy based on that activity](../facts/iam.md#iam-access-analyzer-policy-generation-from-cloudtrail)
iam-access-analyzer-policy-generation-time-range
  claim: Access Analyzer policy generation can analyze at most 90 days of CloudTrail data, and this quota cannot be raised.
  scope: per policy generation; maximum; not adjustable; CloudTrail time range.
  link: [90 days](../facts/iam.md#iam-access-analyzer-policy-generation-time-range)
  say: ninety days
iam-access-analyzer-policy-validation
  claim: IAM Access Analyzer policy validation checks policies against IAM policy grammar and AWS best practices and returns security warnings, errors, general warnings and suggestions.
  scope: IAM Access Analyzer policy validation.
  link: [against IAM policy grammar and AWS best practices](../facts/iam.md#iam-access-analyzer-policy-validation)
  link: [security warnings, errors, general warnings and suggestions](../facts/iam.md#iam-access-analyzer-policy-validation)
iam-access-analyzer-policy-validation-100-checks
  claim: IAM Access Analyzer policy validation provides more than 100 policy checks with actionable recommendations, checking policies against the IAM policy grammar and AWS best practices.
  scope: IAM Access Analyzer policy validation.
  link: [more than 100 policy checks](../facts/iam.md#iam-access-analyzer-policy-validation-100-checks)
iam-access-analyzer-quota-access-previews-per-hour
  claim: An analyzer can create at most 1,000 access previews per hour.
  scope: per analyzer, per hour; maximum; not adjustable.
  link: [1,000](../facts/iam.md#iam-access-analyzer-quota-access-previews-per-hour)
  say: one thousand
iam-access-analyzer-quota-account-analyzers
  claim: An account can have 1 account-level IAM Access Analyzer per analyzer type per Region, and this quota cannot be raised.
  scope: per analyzer type, per AWS account, per Region; maximum; not adjustable; account-level analyzers.
  link: [1](../facts/iam.md#iam-access-analyzer-quota-account-analyzers)
  say: one
iam-access-analyzer-quota-archive-rules
  claim: An Access Analyzer can have 100 archive rules by default, up to a maximum of 1,000, with up to 20 values per criterion in each rule.
  scope: per analyzer; default; adjustable; each archive rule can have up to 20 values per criterion.
  link: [100](../facts/iam.md#iam-access-analyzer-quota-archive-rules)
  link: [1,000](../facts/iam.md#iam-access-analyzer-quota-archive-rules)
  say: one hundred | one thousand
iam-access-analyzer-quota-concurrent-policy-generations
  claim: IAM Access Analyzer has a Concurrent policy generations quota of 1; the default quota and the maximum quota are both 1.
  scope: IAM Access Analyzer quotas table, row Concurrent policy generations (the table does not name a per-account or per-Region unit); maximum; not adjustable.
  link: [1](../facts/iam.md#iam-access-analyzer-quota-concurrent-policy-generations)
  say: one
iam-access-analyzer-quota-org-analyzers
  claim: An account can have 5 organization-level external or unused access analyzers per analyzer type per Region by default, and the quota is adjustable.
  scope: per analyzer type, per AWS account, per Region; default; adjustable; organization-level external or unused access analyzers.
  link: [5](../facts/iam.md#iam-access-analyzer-quota-org-analyzers)
  say: five
iam-access-analyzer-quota-org-internal-analyzers
  claim: An organization can have 1 organization-level internal access analyzer per Region, and the maximum is also 1.
  scope: per AWS organization, per Region; maximum; not adjustable.
  link: [1](../facts/iam.md#iam-access-analyzer-quota-org-internal-analyzers)
  say: one
iam-access-analyzer-quota-policy-generation-cloudtrail-size
  claim: Policy generation can analyze up to 25 GB of AWS CloudTrail data.
  scope: per policy generation; maximum; not adjustable.
  link: [25 GB](../facts/iam.md#iam-access-analyzer-quota-policy-generation-cloudtrail-size)
  say: twenty-five gigabytes
iam-access-analyzer-security-warning-overly-permissive
  claim: Access Analyzer policy validation raises a security warning when a policy statement allows access that AWS considers overly permissive.
  link: [It generates security warnings when a statement in your policy allows access we consider overly permissive](../facts/iam.md#iam-access-analyzer-security-warning-overly-permissive)
iam-access-analyzer-three-analyzer-types
  claim: IAM Access Analyzer has three analyzer types: external access analyzers find resources shared with an external entity, internal access analyzers find internal access to selected resources, and unused access analyzers find unused access.
  scope: per organization or account (zone of trust).
  link: [external access analyzers](../facts/iam.md#iam-access-analyzer-three-analyzer-types)
  link: [internal access analyzers](../facts/iam.md#iam-access-analyzer-three-analyzer-types)
  link: [unused access analyzers](../facts/iam.md#iam-access-analyzer-three-analyzer-types)
  say: external access analyzers | internal access analyzers | unused access analyzers
iam-access-analyzer-unused-access-findings
  claim: An unused access analyzer continuously monitors IAM roles and users and generates findings for unused roles, unused access keys and unused passwords; for active roles and users it shows unused services and actions.
  scope: IAM Access Analyzer unused access analyzer.
  link: [unused roles, unused access keys and unused passwords](../facts/iam.md#iam-access-analyzer-unused-access-findings)
  link: [unused services and actions](../facts/iam.md#iam-access-analyzer-unused-access-findings)
iam-access-analyzer-unused-access-paid-per-role-or-user-per-month
  claim: An unused access analyzer in IAM Access Analyzer is a paid feature: you pay per IAM role or IAM user analyzed per month.
  scope: per unused access analyzer; only when an unused access analyzer is enabled.
  link: [pay per IAM role or IAM user analyzed per month](../facts/iam.md#iam-access-analyzer-unused-access-paid-per-role-or-user-per-month)
  link: [paid feature](../facts/iam.md#iam-access-analyzer-unused-access-paid-per-role-or-user-per-month)
iam-access-analyzer-unused-not-per-region
  claim: Unused access findings do not depend on the Region, so one unused access analyzer is enough; you do not need one in every Region where you have resources.
  scope: per unused access analyzer.
  link: [findings for the analyzer do not change based on Region](../facts/iam.md#iam-access-analyzer-unused-not-per-region)
  link: [Creating an analyzer in each Region where you have resources is not required](../facts/iam.md#iam-access-analyzer-unused-not-per-region)
  say: unused access findings do not depend on the Region | one analyzer is enough
iam-access-analyzer-unused-tracking-period
  claim: An unused access analyzer evaluates permissions that have existed for the whole tracking period, which can be set from 1 to 365 days; with 90 days, only permissions at least 90 days old are analyzed and a finding is made when they show no use in that period.
  scope: per unused access analyzer; maximum; not adjustable; only entities that existed for the entire tracking period are evaluated.
  link: [between 1 and 365 days](../facts/iam.md#iam-access-analyzer-unused-tracking-period)
  link: [90 days](../facts/iam.md#iam-access-analyzer-unused-tracking-period)
  say: one to three hundred sixty-five days | ninety days
iam-access-analyzer-validation-finding-types
  claim: Policy validation findings include security warnings, errors, general warnings and suggestions; in the IAM console they are shown for managed policies and inline user or role policies, but not for inline group policies.
  scope: IAM Access Analyzer policy validation in the IAM console.
  link: [security warnings, errors, general warnings, and suggestions](../facts/iam.md#iam-access-analyzer-validation-finding-types)
  link: [IAM Access Analyzer does not generate these findings for inline group policies](../facts/iam.md#iam-access-analyzer-validation-finding-types)
iam-access-analyzer-zone-of-trust
  claim: When you enable IAM Access Analyzer you create an analyzer for your organization or your account; that organization or account is the zone of trust, and access by principals inside it is considered trusted.
  scope: IAM Access Analyzer external access analyzer.
  link: [that organization or account is the zone of trust](../facts/iam.md#iam-access-analyzer-zone-of-trust)
  link: [access by principals inside it is considered trusted](../facts/iam.md#iam-access-analyzer-zone-of-trust)
iam-access-denied-message-names-policy-type
  claim: An access denied message for an explicit deny includes the phrase 'with an explicit deny in a <type> policy' and may give the policy ARN; for an implicit deny it says 'because no <type> policy allows the <action> action'. If several policy types deny a request, only one type is named.
  scope: access denied error messages (services that support the format).
  link: [with an explicit deny in a <type> policy](../facts/iam.md#iam-access-denied-message-names-policy-type)
  link: [because no <type> policy allows the <action> action](../facts/iam.md#iam-access-denied-message-names-policy-type)
iam-access-key-prefix-akia-vs-asia
  claim: Access key IDs that begin with AKIA are long-term credentials for an IAM user or the root user; access key IDs that begin with ASIA are temporary credentials created with AWS STS.
  scope: access key IDs.
  link: [begin with AKIA are long-term credentials](../facts/iam.md#iam-access-key-prefix-akia-vs-asia)
  link: [begin with ASIA are temporary credentials](../facts/iam.md#iam-access-key-prefix-akia-vs-asia)
iam-access-key-secret-shown-once
  claim: The secret access key can be retrieved only when the key is created; a lost secret means deleting the access key and creating a new one.
  scope: per access key.
  link: [retrieved only at the time you create it](../facts/iam.md#iam-access-key-secret-shown-once)
  link: [delete the access key and create a new one](../facts/iam.md#iam-access-key-secret-shown-once)
  say: you can only see the secret when you create the key | delete the key and create a new one
iam-access-keys-max-two-per-user
  claim: An IAM user can have a maximum of two access keys. To update an access key, you create a second access key while the first is still active, change the first key to Inactive, and delete the first key after all applications and tools have been updated.
  scope: per IAM user; maximum; not adjustable.
  link: [two access keys](../facts/iam.md#iam-access-keys-max-two-per-user)
  link: [create a second access key](../facts/iam.md#iam-access-keys-max-two-per-user)
  say: two access keys | create a second access key while the first is still active
iam-access-keys-prefer-temporary-credentials
  claim: Access keys are long-term credentials for an IAM user or the root user; as a best practice, use temporary security credentials such as IAM roles instead of creating access keys.
  scope: IAM user and root user access keys.
  link: [Access keys are long-term credentials](../facts/iam.md#iam-access-keys-prefer-temporary-credentials)
  link: [use temporary security credentials such as IAM roles instead of creating access keys](../facts/iam.md#iam-access-keys-prefer-temporary-credentials)
iam-account-access-manager-assigns-iam-roles
  claim: Account access manager assigns the existing IAM roles in your AWS accounts to the users and groups of an IAM Identity Center organization instance; it works alongside Identity Center permission sets or on its own.
  scope: per IAM Identity Center organization instance.
  link: [assign your existing IAM roles to the users and groups](../facts/iam.md#iam-account-access-manager-assigns-iam-roles)
  say: assign existing IAM roles to Identity Center users and groups
  changed: 2026-08-10: was Previously, customers granting workforce access to AWS accounts could use one of two alternative access management approaches.
iam-account-access-manager-quota-groups-per-role
  claim: Account access manager allows 20 groups to be assigned to one IAM role by default; the quota can be increased.
  scope: per IAM role; default; adjustable.
  link: [20](../facts/iam.md#iam-account-access-manager-quota-groups-per-role)
  say: twenty
iam-account-access-manager-session-one-hour
  claim: Sessions of IAM roles assigned by account access manager use the default session duration of 1 hour, whatever maximum session duration is set on the IAM role.
  scope: per IAM role session started through account access manager; fixed; not adjustable.
  link: [1 hour](../facts/iam.md#iam-account-access-manager-session-one-hour)
  say: one hour
iam-acls-only-non-json-cross-account-only
  claim: ACLs control which principals in other accounts can access the resource they are attached to; they are the only policy type that does not use the JSON policy document structure, and they cannot grant permissions to entities in the same account.
  scope: access control lists (ACLs) on supported resources.
  link: [the only policy type that does not use the JSON policy document structure](../facts/iam.md#iam-acls-only-non-json-cross-account-only)
  link: [ACLs cannot grant permissions to entities within the same account](../facts/iam.md#iam-acls-only-non-json-cross-account-only)
iam-assume-role-replaces-original-permissions
  claim: When a user assumes a role they temporarily give up their original permissions and take on the permissions of the role; the permissions are not cumulative, and the original permissions are restored when the user exits the role.
  scope: per role session.
  link: [temporarily give up their original permissions and take on the permissions of the role](../facts/iam.md#iam-assume-role-replaces-original-permissions)
  link: [the permissions are not cumulative](../facts/iam.md#iam-assume-role-replaces-original-permissions)
  link: [restored when the user exits the role](../facts/iam.md#iam-assume-role-replaces-original-permissions)
iam-assume-role-two-permissions-checked
  claim: Adding a trusted account to a role's trust policy is only half of the cross-account trust: by default no user in the trusted account can assume the role until its administrator attaches a policy that allows the sts:AssumeRole action with the role's ARN as the Resource.
  scope: cross-account role assumption.
  link: [only half of the cross-account trust](../facts/iam.md#iam-assume-role-two-permissions-checked)
  link: [by default no user in the trusted account can assume the role](../facts/iam.md#iam-assume-role-two-permissions-checked)
  link: [allows the sts:AssumeRole action with the role's ARN as the Resource](../facts/iam.md#iam-assume-role-two-permissions-checked)
iam-aws-managed-policy-cannot-be-changed
  claim: You cannot change the permissions of an AWS managed policy; AWS updates it, for example when a new service launches, and the update applies to every principal the policy is attached to. A customer managed policy is one you create and change yourself, and IAM keeps up to five versions of it for rollback.
  scope: AWS managed and customer managed policies; maximum.
  link: [cannot change the permissions of an AWS managed policy](../facts/iam.md#iam-aws-managed-policy-cannot-be-changed)
  link: [up to five versions](../facts/iam.md#iam-aws-managed-policy-cannot-be-changed)
  link: [applies to every principal the policy is attached to](../facts/iam.md#iam-aws-managed-policy-cannot-be-changed)
iam-best-practice-aws-managed-policies-not-least-privilege
  claim: AWS managed policies are a starting point, but they might not grant least privilege for your use case because all AWS customers can use them; AWS recommends reducing permissions further with customer managed policies.
  link: [might not grant least-privilege permissions for your specific use cases](../facts/iam.md#iam-best-practice-aws-managed-policies-not-least-privilege)
iam-best-practice-boundaries-delegate-role-creation
  claim: When you delegate permissions management, for example letting developers create roles for their workloads, use permissions boundaries to set the maximum permissions you delegate.
  link: [use *permissions boundaries* to set the maximum permissions that you delegate](../facts/iam.md#iam-best-practice-boundaries-delegate-role-creation)
iam-best-practice-conditions-example-tls
  claim: Policy conditions further restrict access: for example a condition can require that all requests are sent using TLS, or allow a service action only when it is called through a specific service such as CloudFormation.
  scope: Condition element of IAM policies.
  link: [all requests must be sent using TLS](../facts/iam.md#iam-best-practice-conditions-example-tls)
iam-best-practice-ec2-use-role-not-long-term-keys
  claim: For applications on an EC2 instance, use an IAM role to manage temporary credentials; with a role you do not distribute long-term credentials such as access keys to the instance.
  link: [you can and should use an IAM role to manage *temporary* credentials](../facts/iam.md#iam-best-practice-ec2-use-role-not-long-term-keys)
  link: [you don't have to distribute long-term credentials](../facts/iam.md#iam-best-practice-ec2-use-role-not-long-term-keys)
iam-best-practice-human-users-federate-with-identity-center
  claim: IAM best practice: human users use temporary credentials by federating through an identity provider and assuming roles; for centralized access management AWS recommends IAM Identity Center.
  link: [Require your human users to use temporary credentials](../facts/iam.md#iam-best-practice-human-users-federate-with-identity-center)
  link: [we recommend that you use AWS IAM Identity Center](../facts/iam.md#iam-best-practice-human-users-federate-with-identity-center)
iam-best-practice-last-accessed-remove-unused
  claim: IAM last accessed information helps you find users, roles, permissions, policies and credentials you no longer need so you can remove them.
  link: [last accessed information](../facts/iam.md#iam-best-practice-last-accessed-remove-unused)
iam-best-practice-least-privilege-definition
  claim: Least-privilege permissions means granting only the permissions required to perform a task, by defining the actions allowed on specific resources under specific conditions.
  scope: IAM policies.
  link: [defining the actions that can be taken on specific resources under specific conditions](../facts/iam.md#iam-best-practice-least-privilege-definition)
iam-best-practice-require-mfa-for-iam-and-root-users
  claim: AWS recommends roles with temporary credentials for human users and workloads; where you still need an IAM user or the root user, require MFA.
  link: [require MFA for additional security](../facts/iam.md#iam-best-practice-require-mfa-for-iam-and-root-users)
iam-best-practice-update-access-keys-when-needed
  claim: Where IAM users need programmatic access with long-term credentials, AWS recommends updating the access keys when needed, for example when an employee leaves, and using access last used information to update and remove keys safely.
  link: [update the access keys when needed, such as when an employee leaves your company](../facts/iam.md#iam-best-practice-update-access-keys-when-needed)
iam-best-practice-workloads-outside-aws-temporary-credentials
  claim: Workloads outside AWS, such as on-premises servers, other clouds or managed CI/CD platforms, can still use temporary credentials, but you must deliver the credentials to the workload, for example with IAM Roles Anywhere using an X.509 certificate from your PKI.
  scope: workloads that run outside AWS.
  link: [can still use temporary credentials](../facts/iam.md#iam-best-practice-workloads-outside-aws-temporary-credentials)
  link: [X.509 Certificate](../facts/iam.md#iam-best-practice-workloads-outside-aws-temporary-credentials)
iam-boundary-applies-to-users-and-roles-not-slr
  claim: A permissions boundary is set with an AWS managed or customer managed policy on an IAM entity, which is a user or role; it is available for service roles but not for service-linked roles.
  scope: IAM users and roles.
  link: [an IAM entity, which is a user or role](../facts/iam.md#iam-boundary-applies-to-users-and-roles-not-slr)
  link: [available for service roles but not for service-linked roles](../facts/iam.md#iam-boundary-applies-to-users-and-roles-not-slr)
iam-boundary-limits-but-never-grants
  claim: A permissions boundary limits the permissions of a user or role but does not provide permissions on its own; the effective permissions are the intersection of the identity-based policies and the boundary, and an explicit deny in either overrides the allow.
  scope: per IAM user or role with a boundary; maximum.
  link: [does not provide permissions on its own](../facts/iam.md#iam-boundary-limits-but-never-grants)
  link: [the intersection of the identity-based policies and the boundary](../facts/iam.md#iam-boundary-limits-but-never-grants)
  link: [an explicit deny in either overrides the allow](../facts/iam.md#iam-boundary-limits-but-never-grants)
iam-boundary-role-arn-grant-limited-session-arn-not
  claim: In the same account a resource-based policy that grants permissions to an IAM role ARN is limited by an implicit deny in a permissions boundary or session policy, but a grant to the IAM role session ARN goes directly to the session and is not limited by them.
  scope: same-account resource-based policy naming a role; no explicit deny.
  link: [grants permissions to an IAM role ARN is limited by an implicit deny in a permissions boundary or session policy](../facts/iam.md#iam-boundary-role-arn-grant-limited-session-arn-not)
  link: [a grant to the IAM role session ARN goes directly to the session](../facts/iam.md#iam-boundary-role-arn-grant-limited-session-arn-not)
iam-boundary-user-arn-grant-not-limited
  claim: Within the same account a resource-based policy that grants permissions to an IAM user ARN is not limited by an implicit deny in an identity-based policy or a permissions boundary.
  scope: same-account resource-based policy naming an IAM user; the user is not an AWS STS federated user principal session.
  link: [grants permissions to an IAM user ARN is not limited by an implicit deny](../facts/iam.md#iam-boundary-user-arn-grant-not-limited)
  link: [in an identity-based policy or a permissions boundary](../facts/iam.md#iam-boundary-user-arn-grant-not-limited)
iam-case-clearwater-200-percent-more-resources
  claim: Using AWS Organizations, AWS Control Tower and AWS CloudFormation, Clearwater Analytics can manage up to 200 percent more resources than on premises. Separately, with custom automation that runs on AWS Lambda and AWS Control Tower, it takes 2 hours instead of 2 weeks to spin up an AWS account set for projects.
  scope: Clearwater Analytics case study.
  link: [manage up to 200 percent more resources](../facts/iam.md#iam-case-clearwater-200-percent-more-resources)
  link: [it takes 2 hours instead of 2 weeks to spin up an AWS account set for projects](../facts/iam.md#iam-case-clearwater-200-percent-more-resources)
iam-case-clearwater-scps-federated-access-350-accounts
  claim: Clearwater Analytics uses service control policies so developers can operate independently with minimal supervision, and uses IAM Identity Center to manage workforce access centrally across more than 350 AWS accounts and 450 applications.
  scope: Clearwater Analytics case study.
  link: [With service control policies, developers can operate independently with minimal supervision](../facts/iam.md#iam-case-clearwater-scps-federated-access-350-accounts)
  link: [more than 350 AWS accounts and 450 applications](../facts/iam.md#iam-case-clearwater-scps-federated-access-350-accounts)
iam-case-navan-identity-center-provisioning-minutes
  claim: Navan moved from manually creating users per AWS account to user management through IAM Identity Center for the whole organization; scanning 10,000 users went from 25–30 minutes to 1–2 minutes.
  scope: Navan case study.
  link: [take 25–30 minutes to scan 10,000 users](../facts/iam.md#iam-case-navan-identity-center-provisioning-minutes)
  link: [it takes 1–2 minutes](../facts/iam.md#iam-case-navan-identity-center-provisioning-minutes)
  link: [We moved from manually creating users per AWS account to streamlined user management through AWS IAM Identity Center for the whole organization](../facts/iam.md#iam-case-navan-identity-center-provisioning-minutes)
iam-case-navan-least-privilege-permission-sets
  claim: Navan follows least privilege by limiting developer access to AWS based on a list of attributes, and it keeps granular control over privileges with permission sets in IAM Identity Center; its next step is just-in-time provisioning for temporary access.
  scope: Navan case study.
  link: [limiting developer access to AWS based on a specific list of attributes](../facts/iam.md#iam-case-navan-least-privilege-permission-sets)
  link: [granular control over all privileges using permission sets](../facts/iam.md#iam-case-navan-least-privilege-permission-sets)
  link: [just-in-time provisioning capabilities](../facts/iam.md#iam-case-navan-least-privilege-permission-sets)
iam-change-access-analyzer-access-configuration-2024-11
  claim: On 2024-11-14 IAM Access Analyzer added access configuration, which lets you change the scope of which AWS accounts, IAM users and roles generate findings.
  scope: per analyzer.
  link: [2024-11-14](../facts/iam.md#iam-change-access-analyzer-access-configuration-2024-11)
  say: November fourteenth, twenty twenty-four
iam-change-access-analyzer-internal-access-2025-06
  claim: On 2025-06-16 IAM Access Analyzer added internal access analyzers, which identify which IAM users and roles inside your organization or account can access selected business-critical resources such as Amazon S3, DynamoDB and RDS resources.
  scope: per analyzer (selected resources).
  link: [2025-06-16](../facts/iam.md#iam-change-access-analyzer-internal-access-2025-06)
  link: [internal access analyzers](../facts/iam.md#iam-change-access-analyzer-internal-access-2025-06)
  say: June sixteenth, twenty twenty-five | internal access analyzers
iam-change-access-analyzer-unused-and-custom-checks-2023
  claim: On 2023-11-26 IAM Access Analyzer added unused access analyzers and custom policy checks; unused access findings highlight unused roles, unused access keys and unused passwords of IAM users.
  scope: per analyzer.
  link: [2023-11-26](../facts/iam.md#iam-change-access-analyzer-unused-and-custom-checks-2023)
  link: [unused access analyzers](../facts/iam.md#iam-change-access-analyzer-unused-and-custom-checks-2023)
  say: November twenty-sixth, twenty twenty-three | unused access analyzers
iam-change-central-root-access-2024-11
  claim: On 2024-11-14 IAM added centralized root access for member accounts of AWS Organizations: the root user credentials of member accounts can be removed centrally, and privileged root tasks run through short-term sessions from the management account or a delegated administrator for IAM.
  scope: per organization (member accounts).
  link: [2024-11-14](../facts/iam.md#iam-change-central-root-access-2024-11)
  say: November fourteenth, twenty twenty-four
iam-change-dual-stack-endpoint-2025-03
  claim: On 2025-03-20 IAM added dual-stack endpoint support, so clients can reach IAM over IPv4 or IPv6; the IAM dual-stack public endpoint is https://iam.global.api.aws, while https://iam.amazonaws.com supports only IPv4 clients.
  scope: IAM public endpoints.
  link: [2025-03-20](../facts/iam.md#iam-change-dual-stack-endpoint-2025-03)
  link: [https://iam.global.api.aws](../facts/iam.md#iam-change-dual-stack-endpoint-2025-03)
  say: March twentieth, twenty twenty-five | iam dot global dot api dot aws
iam-change-identity-center-multi-region-2026-02
  claim: On 2026-02-02 IAM Identity Center added multi-Region support: an instance can be replicated to additional Regions, so the workforce can access assigned AWS accounts and applications through every enabled Region; by default one instance can be enabled in up to 6 Regions, and this quota can be increased.
  scope: per IAM Identity Center instance.
  link: [2026-02-02](../facts/iam.md#iam-change-identity-center-multi-region-2026-02)
  link: [6](../facts/iam.md#iam-change-identity-center-multi-region-2026-02)
  say: February second, twenty twenty-six | six
iam-change-managed-policies-per-role-default-20
  claim: On 2026-08-19 the default quota of managed policies attached to one IAM role rose from 10 to 20; the maximum quota is 25.
  scope: per IAM role.
  link: [from 10 to 20](../facts/iam.md#iam-change-managed-policies-per-role-default-20)
  link: [25](../facts/iam.md#iam-change-managed-policies-per-role-default-20)
  link: [10](../facts/iam.md#iam-change-managed-policies-per-role-default-20)
  say: from ten to twenty | twenty-five | ten
  changed: 2026-08-19: was 10
iam-change-max-quotas-raised-2026-05
  claim: On 2026-05-05 IAM raised six maximum quotas: customer managed policies, instance profiles and roles per account each from 5,000 to 10,000; managed policies per role from 20 to 25; role trust policy length from 4,096 to 8,192 characters; and OpenID Connect providers per account from 100 to 700.
  scope: per AWS account or per IAM role (maximum quotas).
  link: [5,000 to 10,000](../facts/iam.md#iam-change-max-quotas-raised-2026-05)
  link: [20 to 25](../facts/iam.md#iam-change-max-quotas-raised-2026-05)
  link: [4,096 to 8,192 characters](../facts/iam.md#iam-change-max-quotas-raised-2026-05)
  link: [100 to 700](../facts/iam.md#iam-change-max-quotas-raised-2026-05)
  say: five thousand to ten thousand | twenty to twenty-five | four thousand ninety-six to eight thousand one hundred ninety-two characters | one hundred to seven hundred
  changed: 2026-05-05: was 5,000
iam-change-multiple-mfa-devices-2022-11
  claim: Since 2022-11-16 the root user and each IAM user can register up to eight MFA devices of any type (FIDO security keys, virtual authenticator apps or hardware TOTP tokens), and one device is enough to sign in.
  scope: per root user or IAM user; maximum.
  link: [2022-11-16](../facts/iam.md#iam-change-multiple-mfa-devices-2022-11)
  link: [up to eight MFA devices](../facts/iam.md#iam-change-multiple-mfa-devices-2022-11)
  say: November sixteenth, twenty twenty-two | up to eight MFA devices
iam-change-policy-autopilot-2025-11
  claim: IAM Policy Autopilot is an open source MCP server and command-line tool that analyzes application code locally to create baseline identity-based IAM policies for application roles; it is available at no additional cost.
  scope: developer tool.
  link: [open source Model Context Protocol (MCP) server and command-line tool](../facts/iam.md#iam-change-policy-autopilot-2025-11)
  say: an open source MCP server and command-line tool
iam-change-policy-evaluation-docs-2025-01
  claim: On 2025-01-30 AWS enhanced the IAM documentation of policy evaluation logic with improved flow charts and clearer explanations of how AWS decides to allow or deny a request.
  scope: IAM User Guide page.
  link: [2025-01-30](../facts/iam.md#iam-change-policy-evaluation-docs-2025-01)
  say: January thirtieth, twenty twenty-five
iam-change-policy-simulator-in-console-2026-07
  claim: On 2026-07-30 the IAM Policy Simulator moved into the IAM console, replacing the standalone simulator site, and it can now include SCPs in a simulation.
  scope: IAM policy simulator.
  link: [IAM console](../facts/iam.md#iam-change-policy-simulator-in-console-2026-07)
  link: [include SCPs](../facts/iam.md#iam-change-policy-simulator-in-console-2026-07)
  say: the IAM console | include SCPs
  changed: 2026-07-30: was the standalone simulator site
iam-change-rcp-more-services-2026-01
  claim: On 2026-01-23 AWS Organizations added more services to the list that resource control policies (RCPs) support.
  scope: per organization.
  link: [2026-01-23](../facts/iam.md#iam-change-rcp-more-services-2026-01)
  say: January twenty-third, twenty twenty-six
iam-change-rcps-launched-2024-11
  claim: On 2024-11-13 AWS Organizations added resource control policies (RCPs), which set the maximum permissions for resources in the accounts of an organization or OU; an explicit deny in an RCP overrides an allow, like an explicit deny in an SCP.
  scope: per organization, OU or account.
  link: [2024-11-13](../facts/iam.md#iam-change-rcps-launched-2024-11)
  link: [maximum permissions for resources](../facts/iam.md#iam-change-rcps-launched-2024-11)
  say: November thirteenth, twenty twenty-four | the maximum permissions for resources
iam-change-root-mfa-all-account-types-2025
  claim: On 2025-06-17 AWS extended mandatory root user MFA to member accounts, so the root user of every account type must use MFA; the requirement began with management account root users in May 2024 and standalone account root users in June 2024.
  scope: per AWS account root user.
  link: [2025-06-17](../facts/iam.md#iam-change-root-mfa-all-account-types-2025)
  link: [all account types](../facts/iam.md#iam-change-root-mfa-all-account-types-2025)
  say: June seventeenth, twenty twenty-five | all account types
  changed: 2025-06-17: was requiring MFA for AWS Organizations management account root users in May 2024
iam-change-scp-full-iam-language
  claim: AWS Organizations added full IAM policy language support for SCPs: Allow statements in an SCP can now use conditions, individual resource ARNs and the NotAction element, and SCPs can use the NotResource element and wildcards at the beginning or middle of Action strings.
  scope: per SCP statement.
  link: [conditions, individual resource ARNs, and the NotAction element with Allow statements](../facts/iam.md#iam-change-scp-full-iam-language)
  say: conditions, resource ARNs and NotAction in Allow statements
iam-change-scp-quotas-doubled-2026-05
  claim: On 2026-05-15 AWS Organizations raised the maximum number of SCPs attached to one root, OU or account from 5 to 10, and the maximum SCP size from 5,120 to 10,240 characters; RCPs stay at 5 per root, OU or account.
  scope: per root, OU or account (directly attached policies).
  link: [from 5 to 10](../facts/iam.md#iam-change-scp-quotas-doubled-2026-05)
  link: [from 5,120 to 10,240 characters](../facts/iam.md#iam-change-scp-quotas-doubled-2026-05)
  say: from five to ten | from five thousand one hundred twenty to ten thousand two hundred forty characters
  changed: 2026-05-15: was 5
iam-change-shared-oidc-provider-controls-2025-06
  claim: Since 2025-06-06 IAM requires role trust policies for recognized shared OIDC identity providers to evaluate specific JWT claims (identity-provider controls); creating or updating a role whose trust policy lacks them fails, while existing trust policies are not re-evaluated until they are modified.
  scope: per role trust policy for a shared OIDC identity provider.
  link: [2025-06-06](../facts/iam.md#iam-change-shared-oidc-provider-controls-2025-06)
  link: [identity-provider controls](../facts/iam.md#iam-change-shared-oidc-provider-controls-2025-06)
  say: June sixth, twenty twenty-five | identity-provider controls
iam-change-sso-renamed-identity-center-2022
  claim: On 2022-07-26 AWS Single Sign-On (AWS SSO) was renamed AWS IAM Identity Center; the sso and identitystore API namespaces stayed the same for backward compatibility.
  scope: service name.
  link: [2022-07-26](../facts/iam.md#iam-change-sso-renamed-identity-center-2022)
  link: [AWS IAM Identity Center](../facts/iam.md#iam-change-sso-renamed-identity-center-2022)
  say: July twenty-sixth, twenty twenty-two | AWS IAM Identity Center
  changed: 2022-07-26: was AWS Single Sign-On
iam-change-vpce-network-perimeter-keys-2025-08
  claim: On 2025-08-28 IAM added three global condition keys for network perimeters, aws:VpceAccount, aws:VpceOrgID and aws:VpceOrgPaths, which check that requests come through VPC endpoints owned by given accounts, organizations or OUs without listing each endpoint.
  scope: per policy statement (global condition keys).
  link: [2025-08-28](../facts/iam.md#iam-change-vpce-network-perimeter-keys-2025-08)
  link: [aws:VpceAccount](../facts/iam.md#iam-change-vpce-network-perimeter-keys-2025-08)
  say: August twenty-eighth, twenty twenty-five | aws VPC endpoint account
iam-compute-services-receive-role-credentials-no-keys-needed
  claim: On an AWS compute service such as EC2 or Lambda, AWS delivers the temporary credentials of an IAM role to the compute resource; SDK applications find and use them, so there is no need to distribute long-lived IAM user credentials to workloads on AWS.
  link: [AWS delivers the temporary credentials of an IAM role to that compute resource](../facts/iam.md#iam-compute-services-receive-role-credentials-no-keys-needed)
  link: [no need to distribute long lived credentials for an IAM user](../facts/iam.md#iam-compute-services-receive-role-credentials-no-keys-needed)
iam-condition-key-permissions-boundary
  claim: The IAM condition key iam:PermissionsBoundary checks that a specified policy is attached as the permissions boundary on the IAM principal resource; in the documented delegation example, a policy with this condition lets an administrator create IAM users only if the specified policy is set as their permissions boundary.
  scope: IAM principal resource (user or role).
  link: [iam:PermissionsBoundary](../facts/iam.md#iam-condition-key-permissions-boundary)
  link: [attached as permissions boundary](../facts/iam.md#iam-condition-key-permissions-boundary)
iam-condition-key-principalorgid
  claim: The aws:PrincipalOrgID key compares the organization of the requesting principal with an organization ID in the policy; it is an alternative to listing every account ID of the organization in a resource-based policy, and when you add and remove accounts, policies that use the key automatically include the correct accounts without manual updates.
  scope: global condition key aws:PrincipalOrgID; the principal is a member of an organization.
  link: [aws:PrincipalOrgID](../facts/iam.md#iam-condition-key-principalorgid)
  link: [automatically include the correct accounts](../facts/iam.md#iam-condition-key-principalorgid)
iam-condition-key-requestedregion
  claim: The aws:RequestedRegion key compares the Region called in the request with the Region in the policy, so you can control which Regions can be requested.
  scope: global condition key aws:RequestedRegion.
  link: [aws:RequestedRegion](../facts/iam.md#iam-condition-key-requestedregion)
  link: [control which Regions can be requested](../facts/iam.md#iam-condition-key-requestedregion)
iam-condition-key-resourceorgid
  claim: The aws:ResourceOrgID key compares the organization that owns the requested resource with an organization ID in the policy, so an identity-based policy can apply to all resources in an organization.
  scope: global condition key aws:ResourceOrgID.
  link: [aws:ResourceOrgID](../facts/iam.md#iam-condition-key-resourceorgid)
  link: [the organization that owns the requested resource](../facts/iam.md#iam-condition-key-resourceorgid)
iam-condition-key-securetransport
  claim: The aws:SecureTransport key checks whether the request was sent using TLS, so a policy can allow actions only over TLS.
  scope: global condition key aws:SecureTransport.
  link: [aws:SecureTransport](../facts/iam.md#iam-condition-key-securetransport)
  link: [whether the request was sent using TLS](../facts/iam.md#iam-condition-key-securetransport)
iam-condition-key-sourceip-public-only-not-via-vpce
  claim: The aws:SourceIp condition key compares the requester's IP address and can only be used for public IP address ranges; when the request comes through a VPC endpoint the key is not available, and you use a VPC-specific key such as aws:VpcSourceIp instead.
  scope: global condition key aws:SourceIp.
  link: [can only be used for public IP address ranges](../facts/iam.md#iam-condition-key-sourceip-public-only-not-via-vpce)
  link: [when the request comes through a VPC endpoint the key is not available](../facts/iam.md#iam-condition-key-sourceip-public-only-not-via-vpce)
iam-condition-key-sourcevpcarn
  claim: The global condition key aws:SourceVpcArn returns the ARN of the VPC to which the VPC endpoint of a request is attached; AWS recommends it instead of aws:SourceVpc when the target service supports it.
  scope: per request made through a VPC endpoint; supported services only.
  link: [aws:SourceVpcArn](../facts/iam.md#iam-condition-key-sourcevpcarn)
  say: aws source VPC ARN
iam-condition-key-sourcevpce-sourcevpc
  claim: The aws:SourceVpce key compares the VPC endpoint ID of the request with the endpoint ID in the policy, and aws:SourceVpc checks whether the request travels through the VPC that the VPC endpoint is attached to.
  scope: global condition keys aws:SourceVpce and aws:SourceVpc; the request travels through a VPC endpoint.
  link: [aws:SourceVpce](../facts/iam.md#iam-condition-key-sourcevpce-sourcevpc)
  link: [aws:SourceVpc](../facts/iam.md#iam-condition-key-sourcevpce-sourcevpc)
iam-condition-missing-key-is-false-except-ifexists
  claim: If a condition key named in a policy is not present in the request context, the condition is false (true for a negated operator such as StringNotLike); this logic applies to all condition operators except the ...IfExists operators and the Null check, which test whether the key is present. Adding IfExists to an operator makes a missing key evaluate as true; IfExists can be added to any operator except Null.
  scope: IAM policy Condition element; the condition key is not in the request context.
  link: [the condition is false](../facts/iam.md#iam-condition-missing-key-is-false-except-ifexists)
  link: [adding IfExists to an operator makes a missing key evaluate as true](../facts/iam.md#iam-condition-missing-key-is-false-except-ifexists)
iam-console-switch-role-session-length
  claim: A console switch-role session lasts 1 hour by default and an IAM user console session 12 hours by default; the switched session gets the role's maximum session duration or the time left in the user session, whichever is less, and assuming a role cannot extend the session.
  scope: per AWS Management Console session; default; adjustable; role maximum session duration or the remaining time in the user session, whichever is less.
  link: [1 hour by default](../facts/iam.md#iam-console-switch-role-session-length)
  link: [12 hours by default](../facts/iam.md#iam-console-switch-role-session-length)
  link: [whichever is less](../facts/iam.md#iam-console-switch-role-session-length)
  say: one hour by default | twelve hours by default | whichever is less
iam-console-switch-role-uses-original-credentials
  claim: When you switch roles in the console, AWS always uses your original sign-in credentials to authorize the switch, even when you switch from one role to another; the role session you get is the role's maximum session duration or the time remaining in your user session, whichever is less.
  scope: console role switching.
  link: [always uses your original sign-in credentials to authorize the switch](../facts/iam.md#iam-console-switch-role-uses-original-credentials)
  link: [the role's maximum session duration or the time remaining in your user session, whichever is less](../facts/iam.md#iam-console-switch-role-uses-original-credentials)
iam-credential-report-contents
  claim: A credential report lists all users in the account and the status of their credentials, including passwords, access keys and MFA devices, and you can use it for auditing and compliance.
  scope: per AWS account.
  link: [lists all users in the account and the status of their credentials](../facts/iam.md#iam-credential-report-contents)
  link: [use it for auditing and compliance](../facts/iam.md#iam-credential-report-contents)
iam-credential-report-csv-single-report
  claim: A credential report is a CSV file; AWS stores a single report, so generating a new report overwrites the previous one.
  scope: per AWS account.
  link: [comma-separated values (CSV) files](../facts/iam.md#iam-credential-report-csv-single-report)
  link: [AWS stores a single report](../facts/iam.md#iam-credential-report-csv-single-report)
iam-credential-report-every-four-hours
  claim: A credential report lists every IAM user in the account with the status of their passwords, access keys and MFA devices, and a new one can be generated at most once every four hours; a request inside that window returns the most recent report.
  scope: per AWS account; maximum; not adjustable; a report generated within the past four hours is returned instead.
  link: [once every four hours](../facts/iam.md#iam-credential-report-every-four-hours)
  link: [passwords, access keys, and MFA devices](../facts/iam.md#iam-credential-report-every-four-hours)
  say: once every four hours | passwords, access keys and MFA devices for every user
iam-credential-report-first-two-keys-only
  claim: The credential report includes only passwords, the first two access keys per user, MFA devices and X.509 signing certificates; it does not include service-specific credentials.
  scope: IAM credential report.
  link: [the first two access keys per user](../facts/iam.md#iam-credential-report-first-two-keys-only)
  link: [does not include service-specific credentials](../facts/iam.md#iam-credential-report-first-two-keys-only)
iam-cross-account-role-vs-resource-policy
  claim: With a resource-based policy the principal keeps working in the trusted account and does not give up its permissions, which suits copying data between accounts; a role is used as a proxy for services that do not support resource-based policies.
  scope: cross-account access; the resource type supports resource-based policies.
  link: [does not give up its permissions](../facts/iam.md#iam-cross-account-role-vs-resource-policy)
  link: [a role is used as a proxy for services that do not support resource-based policies](../facts/iam.md#iam-cross-account-role-vs-resource-policy)
iam-cross-account-trusted-vs-trusting
  claim: In cross-account access the account where the principal exists is the trusted account and the account where the resource exists is the trusting account; the resource-based policy in the trusting account must name the principal of the trusted account.
  scope: cross-account access.
  link: [the account where the principal exists is the trusted account](../facts/iam.md#iam-cross-account-trusted-vs-trusting)
  link: [the account where the resource exists is the trusting account](../facts/iam.md#iam-cross-account-trusted-vs-trusting)
iam-data-perimeter-definition
  claim: A data perimeter is a set of coarse-grained permission guardrails that make sure only trusted identities access trusted resources from expected networks; it does not replace fine-grained access controls.
  scope: data perimeters in AWS Organizations.
  link: [only trusted identities access trusted resources from expected networks](../facts/iam.md#iam-data-perimeter-definition)
  link: [does not replace fine-grained access controls](../facts/iam.md#iam-data-perimeter-definition)
iam-data-perimeter-identity-rcp-principalorgid
  claim: The identity perimeter (only trusted identities can access my resources) is applied on resources with an RCP, using condition keys such as aws:PrincipalOrgID and aws:PrincipalAccount.
  scope: data perimeters in AWS Organizations.
  link: [applied on resources with an RCP](../facts/iam.md#iam-data-perimeter-identity-rcp-principalorgid)
  link: [aws:PrincipalOrgID and aws:PrincipalAccount](../facts/iam.md#iam-data-perimeter-identity-rcp-principalorgid)
iam-data-perimeter-network-keys
  claim: The network perimeter (access only from expected networks) is applied on identities with an SCP and on resources with an RCP, using condition keys such as aws:SourceIp, aws:SourceVpc and aws:SourceVpce.
  scope: data perimeters in AWS Organizations.
  link: [on identities with an SCP and on resources with an RCP](../facts/iam.md#iam-data-perimeter-network-keys)
  link: [aws:SourceIp, aws:SourceVpc and aws:SourceVpce](../facts/iam.md#iam-data-perimeter-network-keys)
iam-data-perimeter-resource-scp-resourceorgid
  claim: The resource perimeter (your identities can access only trusted resources) is applied on identities with an SCP; the aws:ResourceOrgID key lets an identity-based policy apply rules to all resources in an organization.
  scope: data perimeters in AWS Organizations.
  link: [applied on identities with an SCP](../facts/iam.md#iam-data-perimeter-resource-scp-resourceorgid)
  link: [aws:ResourceOrgID](../facts/iam.md#iam-data-perimeter-resource-scp-resourceorgid)
iam-decision-guide-cognito-for-own-application-auth
  claim: In the identity decision guide, a developer who wants to build an authentication mechanism into their own application is pointed to Amazon Cognito.
  link: [Build an authentication mechanism into my own application](../facts/iam.md#iam-decision-guide-cognito-for-own-application-auth)
iam-decision-guide-criteria-who-what-where
  claim: The AWS identity decision guide chooses a service by three questions: who requires access (workforce, workloads or the applications you build), what they want to access (AWS accounts, AWS applications and data, or data in your own applications) and where they access it from (AWS, on premises, another cloud or IoT devices).
  link: [you and your workforce, a machine and your workloads, or the applications you build](../facts/iam.md#iam-decision-guide-criteria-who-what-where)
  link: [AWS accounts; AWS applications and services, and the data in them; or data in the applications you build](../facts/iam.md#iam-decision-guide-criteria-who-what-where)
  link: [from within AWS, from your on-premises environment, from another cloud environment, or from AWS IoT devices](../facts/iam.md#iam-decision-guide-criteria-who-what-where)
iam-decision-guide-workloads-assume-roles-with-temporary-credentials
  claim: For workloads, IAM is the identity service: a workload assumes an IAM role and receives temporary security credentials to call AWS APIs, for example code on EC2 or Lambda.
  link: [lets your workload assume IAM roles with temporary security credentials](../facts/iam.md#iam-decision-guide-workloads-assume-roles-with-temporary-credentials)
iam-delete-role-cli-remove-from-instance-profile-first
  claim: To delete a role with the AWS CLI you first remove the role from all its instance profiles, delete its inline policies and detach its managed policies; the instance profile itself must be deleted separately.
  scope: deleting an IAM role with the AWS CLI or API.
  link: [Remove the role from all instance profiles that the role is associated with](../facts/iam.md#iam-delete-role-cli-remove-from-instance-profile-first)
  link: [you must delete it separately](../facts/iam.md#iam-delete-role-cli-remove-from-instance-profile-first)
iam-delete-role-console-removes-policies-and-profile
  claim: Deleting a role in the console automatically detaches its managed policies, deletes its inline policies and deletes any EC2 instance profile that contains the role; deleting a role used by a running instance breaks its applications.
  scope: deleting an IAM role in the AWS Management Console.
  link: [IAM automatically detaches managed policies associated with the role](../facts/iam.md#iam-delete-role-console-removes-policies-and-profile)
  link: [will break any applications that are running on the instance](../facts/iam.md#iam-delete-role-console-removes-policies-and-profile)
iam-ec2-no-resource-based-policies
  claim: In the table of services that work with IAM, Amazon EC2 shows No for resource-based policies and Yes for temporary credentials: Amazon EC2 does not support resource-based policies.
  scope: Amazon EC2 in the table of services that work with IAM.
  link: [Amazon EC2 does not support resource-based policies](../facts/iam.md#iam-ec2-no-resource-based-policies)
  link: [No for resource-based policies](../facts/iam.md#iam-ec2-no-resource-based-policies)
iam-ec2-role-credentials-not-limited-by-max-session
  claim: The maximum session duration setting of a role does not limit sessions assumed by AWS services, and EC2 IAM role credentials are not subject to the role's maximum session duration.
  scope: role sessions assumed by AWS services.
  link: [does not limit sessions assumed by AWS services](../facts/iam.md#iam-ec2-role-credentials-not-limited-by-max-session)
  link: [not subject to the role's maximum session duration](../facts/iam.md#iam-ec2-role-credentials-not-limited-by-max-session)
iam-ec2-role-credentials-rotate-automatically
  claim: Role credentials delivered to an EC2 instance are temporary and updated automatically, so you do not manage credentials on the instance; a change to a role shared by many instances propagates to all of them, and a role can be attached to an instance that is already running.
  scope: roles for EC2.
  link: [temporary and updated automatically](../facts/iam.md#iam-ec2-role-credentials-rotate-automatically)
  link: [propagates to all of them](../facts/iam.md#iam-ec2-role-credentials-rotate-automatically)
  link: [attached to an instance that is already running](../facts/iam.md#iam-ec2-role-credentials-rotate-automatically)
iam-eval-cross-account-needs-both-policies
  claim: For a cross-account request AWS evaluates both accounts and allows the request only if both evaluations return Allow: the requester's identity-based policy in the trusted account must allow the access, and the resource-based policy in the trusting account must allow the requester.
  scope: principal and resource in different accounts.
  link: [allows the request only if both evaluations return Allow](../facts/iam.md#iam-eval-cross-account-needs-both-policies)
  link: [identity-based policy in the trusted account must allow the access](../facts/iam.md#iam-eval-cross-account-needs-both-policies)
  link: [resource-based policy in the trusting account must allow the requester](../facts/iam.md#iam-eval-cross-account-needs-both-policies)
iam-eval-deny-checked-first
  claim: The enforcement code first looks for a Deny statement in every policy that applies to the request; if it finds even one explicit deny that applies, the final decision is Deny, and only when there is no explicit deny does the evaluation continue.
  scope: every policy that applies to the request.
  link: [first looks for a Deny statement in every policy that applies](../facts/iam.md#iam-eval-deny-checked-first)
  link: [even one explicit deny that applies](../facts/iam.md#iam-eval-deny-checked-first)
  link: [only when there is no explicit deny does the evaluation continue](../facts/iam.md#iam-eval-deny-checked-first)
iam-eval-explicit-deny-overrides-allow
  claim: In policy evaluation an explicit deny overrides an explicit allow: if any applicable policy has a Deny statement that matches the request, the request is denied even when another statement allows it.
  scope: every policy type that applies to the request.
  link: [an explicit deny overrides an explicit allow](../facts/iam.md#iam-eval-explicit-deny-overrides-allow)
  link: [the Deny statement trumps the Allow statement](../facts/iam.md#iam-eval-explicit-deny-overrides-allow)
iam-eval-identity-policy-no-allow-is-implicit-deny
  claim: At the identity-based policy step of the evaluation, if no identity-based policy statement allows the requested action, the request is implicitly denied with a final decision of Deny; for an IAM user the identity-based policies include the policies of the groups the user belongs to. Exception: within the same account, depending on the type of principal, an Allow in a resource-based policy can result in a final decision of Allow even if an implicit deny in an identity-based policy is present.
  scope: identity-based policy step of the AWS enforcement code logic; no resource-based policy has already granted the request within the same account.
  link: [the request is implicitly denied](../facts/iam.md#iam-eval-identity-policy-no-allow-is-implicit-deny)
  link: [include the policies of the groups the user belongs to](../facts/iam.md#iam-eval-identity-policy-no-allow-is-implicit-deny)
iam-eval-implicit-deny-by-default
  claim: By default every request is implicitly denied; the only exception is the AWS account root user, which has full access.
  scope: every request to AWS.
  link: [all requests are implicitly denied](../facts/iam.md#iam-eval-implicit-deny-by-default)
  link: [with the exception of the AWS account root user, which has full access](../facts/iam.md#iam-eval-implicit-deny-by-default)
iam-eval-policy-types-checked-in-account
  claim: Within an account the enforcement code evaluates every applicable policy of these types: AWS Organizations SCPs and RCPs, resource-based policies, identity-based policies, IAM permissions boundaries, and session policies.
  scope: a request within one account.
  link: [SCPs and RCPs, resource-based policies, identity-based policies, IAM permissions boundaries, and session policies](../facts/iam.md#iam-eval-policy-types-checked-in-account)
  link: [every applicable policy of these types](../facts/iam.md#iam-eval-policy-types-checked-in-account)
iam-eval-same-account-identity-or-resource-allow
  claim: Within the same account the permissions of identity-based and resource-based policies are a union: if either policy type allows the action and the other does not, the request is still allowed, so a resource-based policy allow needs no additional identity-based policy.
  scope: principal and resource in the same account; no explicit deny applies.
  link: [the permissions of identity-based and resource-based policies are a union](../facts/iam.md#iam-eval-same-account-identity-or-resource-allow)
  link: [if either policy type allows the action and the other does not, the request is still allowed](../facts/iam.md#iam-eval-same-account-identity-or-resource-allow)
  link: [a resource-based policy allow needs no additional identity-based policy](../facts/iam.md#iam-eval-same-account-identity-or-resource-allow)
iam-eventually-consistent-changes-replicate
  claim: IAM is eventually consistent: a successful change to users, groups, roles or policies is stored at once but takes some time to replicate across IAM, so AWS recommends keeping IAM changes out of critical, high-availability code paths.
  scope: IAM (all Regions).
  link: [can take some time](../facts/iam.md#iam-eventually-consistent-changes-replicate)
  link: [do not include such IAM changes in the critical, high-availability code paths](../facts/iam.md#iam-eventually-consistent-changes-replicate)
  say: replication takes some time | keep IAM changes out of critical code paths
iam-external-id-is-not-a-secret
  claim: AWS does not treat the external ID as a secret: anyone with permission to view the role can see it, unlike an access key or password that cannot be viewed again after creation.
  scope: external IDs in trust policies.
  link: [AWS does not treat the external ID as a secret](../facts/iam.md#iam-external-id-is-not-a-secret)
  link: [anyone with permission to view the role can see it](../facts/iam.md#iam-external-id-is-not-a-secret)
iam-external-id-prevents-confused-deputy
  claim: The confused deputy problem is when an entity without permission coerces a more privileged entity to act for it; for third-party cross-account access the external ID is an sts:ExternalId condition in the role's trust policy, with a value generated and controlled by the third party and unique per customer. When a role's trust policy includes an external ID, anyone who wants to assume the role must be a principal in the role and must include the correct external ID.
  scope: third-party cross-account role access.
  link: [an entity without permission coerces a more privileged entity to act for it](../facts/iam.md#iam-external-id-prevents-confused-deputy)
  link: [an sts:ExternalId condition in the role's trust policy](../facts/iam.md#iam-external-id-prevents-confused-deputy)
  link: [generated and controlled by the third party and unique per customer](../facts/iam.md#iam-external-id-prevents-confused-deputy)
iam-external-id-role-not-switchable-in-console
  claim: You cannot switch to a role that requires an ExternalId in the AWS Management Console; such a role can be assumed only by calling the AssumeRole API, which supports the ExternalId parameter, and the root user cannot switch roles at all.
  scope: console role switching.
  link: [cannot switch to a role that requires an ExternalId in the AWS Management Console](../facts/iam.md#iam-external-id-role-not-switchable-in-console)
  link: [assumed only by calling the AssumeRole API](../facts/iam.md#iam-external-id-role-not-switchable-in-console)
  link: [the root user cannot switch roles at all](../facts/iam.md#iam-external-id-role-not-switchable-in-console)
iam-faq-abac-attributes-are-tags
  claim: Attribute-based access control (ABAC) defines permissions based on attributes, which in AWS are tags that you can define on AWS resources, IAM roles and role sessions.
  scope: attribute-based access control (ABAC) in AWS.
  link: [these attributes are called tags](../facts/iam.md#iam-faq-abac-attributes-are-tags)
  link: [on AWS resources, IAM roles, and in role sessions](../facts/iam.md#iam-faq-abac-attributes-are-tags)
iam-faq-abac-for-rapidly-growing-environments
  claim: ABAC helps in environments that grow rapidly, because permissions apply to new resources as they are created with specific tags.
  link: [environments that are growing rapidly](../facts/iam.md#iam-faq-abac-for-rapidly-growing-environments)
iam-faq-abac-role-tags-match-resource-tags
  claim: ABAC grants fine-grained permissions by requiring the tags on the role or session to match the tags on the resource.
  link: [requiring the tags on the role or session to match the tags on the resource](../facts/iam.md#iam-faq-abac-role-tags-match-resource-tags)
iam-faq-abac-session-tags-for-shared-role
  claim: When multiple identities use one IAM role, you can also define session tag keys and values for ABAC.
  link: [define session tag keys and values](../facts/iam.md#iam-faq-abac-session-tags-for-shared-role)
iam-faq-access-analyzer-custom-checks-automated-reasoning
  claim: IAM Access Analyzer custom policy checks use automated reasoning to validate before deployment that policies meet your security standards, for example flagging a policy change that is more permissive than the previous version.
  link: [validate before deployments](../facts/iam.md#iam-faq-access-analyzer-custom-checks-automated-reasoning)
  link: [more permissive than their previous version would be flagged for additional review](../facts/iam.md#iam-faq-access-analyzer-custom-checks-automated-reasoning)
iam-faq-access-analyzer-custom-checks-in-cicd
  claim: Teams can automate policy reviews at scale by integrating IAM Access Analyzer custom policy checks into the tools where developers author policies, such as CI/CD pipelines.
  link: [such as their CI/CD pipelines](../facts/iam.md#iam-faq-access-analyzer-custom-checks-in-cicd)
iam-faq-access-analyzer-external-and-internal-findings
  claim: IAM Access Analyzer public and cross-account findings show access that your resource policies allow from outside your organization or account; internal findings show who inside your organization can access your critical resources.
  link: [access allowed by your resource policies from outside your AWS organization or account](../facts/iam.md#iam-faq-access-analyzer-external-and-internal-findings)
  link: [who within your AWS organization has access to your critical AWS resources](../facts/iam.md#iam-faq-access-analyzer-external-and-internal-findings)
iam-faq-access-analyzer-policy-generation
  claim: IAM Access Analyzer policy generation creates a fine-grained policy from the access activity captured in your logs, so that after you run an application you can generate a policy with only the required permissions.
  scope: IAM Access Analyzer policy generation.
  link: [generates a fine-grained policy based on the access activity captured in your logs](../facts/iam.md#iam-faq-access-analyzer-policy-generation)
iam-faq-access-analyzer-policy-validation-100-checks
  claim: IAM Access Analyzer policy validation uses more than 100 policy checks to help you author and validate secure and functional policies, for new or existing policies.
  scope: per policy validation; minimum.
  link: [more than 100 policy checks](../facts/iam.md#iam-faq-access-analyzer-policy-validation-100-checks)
iam-faq-access-analyzer-unused-access-findings
  claim: Unused access findings of IAM Access Analyzer highlight unused roles, unused access keys and unused passwords of IAM users, and for active roles and users the unused services and actions.
  link: [unused roles, unused access keys for IAM users, and unused passwords for IAM users](../facts/iam.md#iam-faq-access-analyzer-unused-access-findings)
  link: [unused services and actions](../facts/iam.md#iam-faq-access-analyzer-unused-access-findings)
iam-faq-authentication-and-authorization
  claim: IAM provides both authentication and authorization for AWS services, which evaluate whether each AWS request is allowed or denied.
  link: [authentication and authorization](../facts/iam.md#iam-faq-authentication-and-authorization)
iam-faq-aws-managed-policies-owned-by-aws
  claim: AWS managed policies are created, administered and updated by AWS, cover common use cases, and are available in all AWS accounts.
  link: [owned and updated by AWS](../facts/iam.md#iam-faq-aws-managed-policies-owned-by-aws)
  link: [cover common use cases](../facts/iam.md#iam-faq-aws-managed-policies-owned-by-aws)
iam-faq-customer-managed-policies-for-specific-needs
  claim: Customer managed policies are the policies you create for your specific use cases and resources, so that you grant only the permissions required and keep refining them.
  scope: customer managed policies.
  link: [customer managed policies that are specific to your use cases and resources](../facts/iam.md#iam-faq-customer-managed-policies-for-specific-needs)
iam-faq-get-started-roles-for-workforce-and-systems
  claim: To get started, AWS says to create IAM roles: for workforce users a role that your identity provider can assume, and for systems a role that the AWS service you use (for example Amazon EC2 or AWS Lambda) can assume.
  link: [a role that can be assumed by your identity provider](../facts/iam.md#iam-faq-get-started-roles-for-workforce-and-systems)
  link: [a role that can be assumed by the service you are using](../facts/iam.md#iam-faq-get-started-roles-for-workforce-and-systems)
iam-faq-iam-users-with-keys-rotate-and-remove
  claim: Where a scenario still requires IAM users with long-term access keys, AWS recommends using IAM access last used information to rotate credentials often and to remove credentials that are not used.
  link: [rotate credentials often and remove credentials that are not being used](../facts/iam.md#iam-faq-iam-users-with-keys-rotate-and-remove)
iam-faq-inline-policy-strict-one-to-one
  claim: Inline policies are embedded in a specific IAM identity; use them when you want a strict one-to-one relationship between a policy and the identity it applies to, for example so that administrative permissions are not attached to other roles.
  scope: inline policies.
  link: [strict one-to-one relationship between a policy and the identity](../facts/iam.md#iam-faq-inline-policy-strict-one-to-one)
iam-faq-last-accessed-finds-unused-permissions
  claim: Service and last accessed information helps you identify unused permissions so that you can refine them.
  link: [reviewing service and last accessed information to identify unused permissions](../facts/iam.md#iam-faq-last-accessed-finds-unused-permissions)
iam-faq-least-privilege-definition
  claim: Least privilege means that an IAM policy grants only the permissions required to perform a task, defined as the actions allowed on specific resources under specific conditions.
  scope: IAM policies.
  link: [grant only the permissions required to perform a task](../facts/iam.md#iam-faq-least-privilege-definition)
iam-faq-least-privilege-refine-as-use-cases-mature
  claim: AWS recommends starting with broader permissions while you explore, then refining them as your use cases mature so that you grant only the permissions required, with the goal of least privilege.
  scope: IAM policies over time.
  link: [refine permissions to grant only the permissions required](../facts/iam.md#iam-faq-least-privilege-refine-as-use-cases-mature)
iam-faq-least-privilege-tools
  claim: To find the specific permissions you require, the IAM FAQ points to IAM Access Analyzer, AWS CloudTrail logs, last accessed information, and the IAM policy simulator for testing and troubleshooting policies.
  link: [Access Analyzer, review AWS CloudTrail logs, and inspect last accessed information](../facts/iam.md#iam-faq-least-privilege-tools)
  link: [IAM policy simulator to test and troubleshoot policies](../facts/iam.md#iam-faq-least-privilege-tools)
iam-faq-org-created-account-has-admin-role
  claim: When AWS Organizations creates an account, it also creates an IAM role with full administrative permissions in the new account; IAM users and IAM roles with appropriate permissions in the management account (the FAQ uses the former term master account) can assume this role to gain access to the newly created account.
  link: [creates an IAM role with full administrative permissions in the new account](../facts/iam.md#iam-faq-org-created-account-has-admin-role)
iam-faq-policies-attach-to-org-or-ou-to-restrict
  claim: Besides roles and resources, policies can be attached to an AWS organization or organizational unit to restrict access across multiple accounts.
  link: [attach policies to an AWS organization or organizational unit to restrict access across multiple accounts](../facts/iam.md#iam-faq-policies-attach-to-org-or-ou-to-restrict)
iam-faq-policy-is-json-document
  claim: An IAM policy is a JavaScript Object Notation (JSON) document whose statements grant or deny access to specific service actions, resources and conditions.
  scope: IAM policies.
  link: [JavaScript Object Notation (JSON) document](../facts/iam.md#iam-faq-policy-is-json-document)
  link: [grant or deny access to specific service actions, resources, and conditions](../facts/iam.md#iam-faq-policy-is-json-document)
iam-faq-policy-simulator-effective-permissions
  claim: The IAM policy simulator evaluates the policies you choose and determines the effective permissions for each action you specify.
  link: [determines the effective permissions for each of the actions you specify](../facts/iam.md#iam-faq-policy-simulator-effective-permissions)
iam-faq-policy-simulator-policy-types
  claim: The IAM policy simulator tests and troubleshoots identity-based policies, resource-based policies, IAM permissions boundaries and SCPs.
  link: [identity-based and resource-based policies, IAM permissions boundaries, and SCPs](../facts/iam.md#iam-faq-policy-simulator-policy-types)
iam-faq-rbac-audit-per-role
  claim: With RBAC you audit access by looking at each IAM role and its attached permissions.
  link: [looking at each IAM role and its attached permissions](../facts/iam.md#iam-faq-rbac-audit-per-role)
iam-faq-rbac-definition
  claim: Role-based access control (RBAC) assigns permissions based on a person's job function; IAM provides RBAC through IAM roles whose permissions align with job functions, and individuals are granted access to assume those roles.
  link: [assign permissions based on a person’s job function](../facts/iam.md#iam-faq-rbac-definition)
  link: [defining IAM roles with permissions that align with job functions](../facts/iam.md#iam-faq-rbac-definition)
iam-faq-rbac-must-update-policies-for-new-resources
  claim: With RBAC, when employees add new resources, you must update policies to allow access to those resources.
  scope: role-based access control (RBAC) in IAM.
  link: [you must update policies to allow access to those resources](../facts/iam.md#iam-faq-rbac-must-update-policies-for-new-resources)
iam-faq-remove-unused-with-last-used-information
  claim: To remove users and roles you no longer need, review password and access key last used information for IAM users and role last used information for roles, available in the IAM console, APIs and SDKs.
  link: [review password and access key last used information](../facts/iam.md#iam-faq-remove-unused-with-last-used-information)
  link: [review role last used information](../facts/iam.md#iam-faq-remove-unused-with-last-used-information)
iam-faq-restrict-with-deny-statement
  claim: In IAM all access is denied by default and needs a policy that grants it; to restrict access as a guardrail, you specify a Deny statement in any policy.
  scope: every IAM policy type.
  link: [specify a Deny statement in any policy](../facts/iam.md#iam-faq-restrict-with-deny-statement)
iam-faq-roles-assumed-by-services-and-idp-users
  claim: Authorized identities, which can be AWS services or users from your identity provider, assume IAM roles to make AWS requests, and you grant a role its permissions by attaching an IAM policy to it.
  link: [AWS services or users from your identity provider](../facts/iam.md#iam-faq-roles-assumed-by-services-and-idp-users)
  link: [attach an IAM policy to it](../facts/iam.md#iam-faq-roles-assumed-by-services-and-idp-users)
iam-faq-roles-for-cross-account-access
  claim: IAM roles can also grant cross-account access to services and features such as Lambda functions.
  link: [grant cross-account access](../facts/iam.md#iam-faq-roles-for-cross-account-access)
iam-faq-start-with-aws-managed-then-customer-managed
  claim: When you do not yet know the exact permissions you need, you can start with broader AWS managed policies, which are available in all AWS accounts, and then reduce permissions with customer managed policies specific to your use cases.
  scope: AWS managed and customer managed policies.
  link: [start with broader permissions](../facts/iam.md#iam-faq-start-with-aws-managed-then-customer-managed)
  link: [reduce permissions further by defining customer managed policies](../facts/iam.md#iam-faq-start-with-aws-managed-then-customer-managed)
iam-faq-temporary-delegation
  claim: IAM temporary delegation lets Amazon and AWS Partners request temporary, limited access to your AWS account for specific tasks; you review and approve each request, and the access expires automatically after a specified duration.
  link: [request temporary, limited access to your AWS account](../facts/iam.md#iam-faq-temporary-delegation)
  link: [You review and approve each request](../facts/iam.md#iam-faq-temporary-delegation)
iam-federation-cognito-identity-pools-deliver-iam-credentials
  claim: Amazon Cognito user pools add sign-up and sign-in to mobile and web apps, and Cognito identity pools deliver temporary IAM credentials (through AssumeRoleWithWebIdentity) that let app users reach protected AWS resources.
  scope: Amazon Cognito with IAM.
  link: [user pools add sign-up and sign-in](../facts/iam.md#iam-federation-cognito-identity-pools-deliver-iam-credentials)
  link: [identity pools deliver temporary IAM credentials](../facts/iam.md#iam-federation-cognito-identity-pools-deliver-iam-credentials)
iam-federation-idp-entity-oidc-or-saml
  claim: To link an external identity provider directly to IAM you create an identity provider entity in the account, which establishes trust between the account and the IdP; IAM supports IdPs compatible with OpenID Connect (OIDC) or SAML 2.0.
  scope: IAM federation in one AWS account.
  link: [create an identity provider entity](../facts/iam.md#iam-federation-idp-entity-oidc-or-saml)
  link: [OpenID Connect (OIDC) or SAML 2.0](../facts/iam.md#iam-federation-idp-entity-oidc-or-saml)
iam-federation-oidc-jwt-exchanged-for-role-credentials
  claim: With OIDC federation an application such as GitHub Actions receives a JSON Web Token (JWT) from its identity provider and exchanges it for temporary AWS credentials that map to an IAM role, so no long-term credentials are embedded in the application.
  scope: IAM OIDC federation.
  link: [exchanges it for temporary AWS credentials that map to an IAM role](../facts/iam.md#iam-federation-oidc-jwt-exchanged-for-role-credentials)
  link: [no long-term credentials are embedded in the application](../facts/iam.md#iam-federation-oidc-jwt-exchanged-for-role-credentials)
iam-federation-saml-console-sso-without-iam-users
  claim: SAML federation enables federated single sign-on, so users can sign in to the AWS Management Console or call AWS API operations without an IAM user for everyone in the organization.
  scope: IAM SAML federation.
  link: [federated single sign-on](../facts/iam.md#iam-federation-saml-console-sso-without-iam-users)
  link: [without an IAM user for everyone in the organization](../facts/iam.md#iam-federation-saml-console-sso-without-iam-users)
iam-federation-with-iam-per-account-saml-or-oidc
  claim: Federation with IAM connects an identity provider to a specific AWS account: users assume IAM roles there, and the provider can speak either OpenID Connect (OIDC) or SAML 2.0.
  scope: per AWS account.
  link: [federate workforce users through your identity provider to specific AWS accounts](../facts/iam.md#iam-federation-with-iam-per-account-saml-or-oidc)
  link: [either OpenID Connect (OIDC) or SAML 2.0](../facts/iam.md#iam-federation-with-iam-per-account-saml-or-oidc)
iam-forward-access-sessions-check-caller-permissions
  claim: With forward access sessions (FAS), a service that acts on your behalf passes your identity to downstream services, and each service checks the permissions of the same IAM principal; for example Amazon S3 calls AWS KMS to decrypt an SSE-KMS object, and KMS checks the caller's permissions.
  scope: forward access sessions.
  link: [each service checks the permissions of the same IAM principal](../facts/iam.md#iam-forward-access-sessions-check-caller-permissions)
  link: [Amazon S3 calls AWS KMS to decrypt an SSE-KMS object](../facts/iam.md#iam-forward-access-sessions-check-caller-permissions)
iam-global-service-single-endpoint-us-east-1
  claim: IAM is a global service with a single endpoint in US East (N. Virginia), so IAM calls are always made to us-east-1; a policy that denies all services outside one other Region makes IAM calls fail unless it exempts them, for example with NotAction.
  scope: AWS Identity and Access Management endpoint.
  link: [a single endpoint in US East (N. Virginia)](../facts/iam.md#iam-global-service-single-endpoint-us-east-1)
  link: [makes IAM calls fail unless it exempts them](../facts/iam.md#iam-global-service-single-endpoint-us-east-1)
iam-groups-no-nesting-not-principals
  claim: An IAM user group can contain only users, not other groups, so groups cannot be nested; a group cannot be named as a Principal in a policy because groups relate to permissions, not authentication; a user can belong to multiple groups and there is no default group that holds every user.
  scope: IAM user groups.
  link: [groups cannot be nested](../facts/iam.md#iam-groups-no-nesting-not-principals)
  link: [a group cannot be named as a Principal in a policy](../facts/iam.md#iam-groups-no-nesting-not-principals)
  link: [there is no default group that holds every user](../facts/iam.md#iam-groups-no-nesting-not-principals)
iam-groups-permissions-for-many-users
  claim: A user group is a collection of IAM users; a policy attached to the group gives its permissions to all users in the group, a group can contain many users and a user can belong to multiple groups.
  link: [all of the users in the user group receive the policy's permissions](../facts/iam.md#iam-groups-permissions-for-many-users)
  link: [a user can belong to multiple user groups](../facts/iam.md#iam-groups-permissions-for-many-users)
iam-idc-accounts-need-organizations-all-features
  claim: IAM Identity Center can manage single sign-on to any AWS account managed with AWS Organizations, and you need to enable all features in the organization to do so.
  scope: AWS accounts managed with IAM Identity Center.
  link: [any AWS account managed using AWS Organizations](../facts/iam.md#iam-idc-accounts-need-organizations-all-features)
  link: [enable all features in your organizations](../facts/iam.md#iam-idc-accounts-need-organizations-all-features)
iam-idc-browser-only-sso-to-apps
  claim: IAM Identity Center single sign-on to business applications works through web browsers only, not to native mobile and desktop applications.
  scope: IAM Identity Center single sign-on to business applications.
  link: [through web browsers only](../facts/iam.md#iam-idc-browser-only-sso-to-apps)
iam-idc-built-on-iam-for-multi-account-access
  claim: IAM Identity Center is built on top of IAM to simplify access management to multiple AWS accounts, AWS applications and other SAML-enabled cloud applications for your workforce users.
  link: [built on top of AWS Identity and Access Management (IAM)](../facts/iam.md#iam-idc-built-on-iam-for-multi-account-access)
  link: [multiple AWS accounts, AWS applications, and other SAML-enabled cloud applications](../facts/iam.md#iam-idc-built-on-iam-for-multi-account-access)
iam-idc-cli-and-console-use-permission-set-duration
  claim: For console federation and for the AWS CLI, IAM Identity Center uses the session duration setting of the permission set to control how long the session lasts.
  scope: per permission set (console and AWS CLI sessions).
  link: [uses the session duration setting on the permission set](../facts/iam.md#iam-idc-cli-and-console-use-permission-set-duration)
iam-idc-cognito-not-an-identity-source
  claim: Amazon Cognito user pools are not a supported identity source for IAM Identity Center; Cognito manages identities for customer-facing applications.
  scope: IAM Identity Center identity sources.
  link: [it is not a supported identity source in IAM Identity Center](../facts/iam.md#iam-idc-cognito-not-an-identity-source)
  link: [identities for your customer facing applications](../facts/iam.md#iam-idc-cognito-not-an-identity-source)
iam-idc-console-cli-v2-and-mobile
  claim: IAM Identity Center controls access to the AWS Management Console and AWS CLI v2 through single sign-on, and the AWS Mobile Console app also supports it.
  link: [AWS Management Console and CLI v2](../facts/iam.md#iam-idc-console-cli-v2-and-mobile)
iam-idc-creates-role-per-permission-set
  claim: IAM Identity Center creates and manages IAM roles in the individual AWS accounts for each permission set that you grant to users.
  scope: per AWS account assigned a permission set.
  link: [creates and manages IAM roles in individual AWS accounts for each permission set](../facts/iam.md#iam-idc-creates-role-per-permission-set)
iam-idc-does-not-modify-existing-iam
  claim: Enabling IAM Identity Center does not modify existing IAM roles, users or policies; it creates new roles and policies for its own use, and existing IAM roles and users keep working, so you can migrate in phases.
  scope: enabling IAM Identity Center in an organization.
  link: [does not modify any existing IAM roles, users, or policies](../facts/iam.md#iam-idc-does-not-modify-existing-iam)
  link: [migrate to IAM Identity Center in a phased approach](../facts/iam.md#iam-idc-does-not-modify-existing-iam)
iam-idc-identity-sources
  claim: IAM Identity Center can use its own identity store or connect an existing identity source such as Microsoft Active Directory, Okta Universal Directory, Microsoft Entra ID or another supported IdP.
  link: [IAM Identity Center’s identity store](../facts/iam.md#iam-idc-identity-sources)
  link: [Microsoft Active Directory, Okta Universal Directory, Microsoft Entra ID](../facts/iam.md#iam-idc-identity-sources)
iam-idc-mfa-options
  claim: With its own identity store or Active Directory as the source, IAM Identity Center supports WebAuthn with FIDO security keys and built-in biometric authenticators, and TOTP authenticator apps; with a SAML 2.0 IdP you use the provider's MFA.
  link: [Web Authentication specification](../facts/iam.md#iam-idc-mfa-options)
  link: [one-time-passwords (TOTPs)](../facts/iam.md#iam-idc-mfa-options)
  link: [enable multi-factor authentication capabilities of your provider](../facts/iam.md#iam-idc-mfa-options)
iam-idc-no-extra-charge
  claim: IAM Identity Center is offered at no extra charge.
  scope: IAM Identity Center.
  link: [no extra charge](../facts/iam.md#iam-idc-no-extra-charge)
iam-idc-no-iam-users-own-identity-store
  claim: IAM Identity Center does not create IAM users and groups; it has its own identity store, and with an external IdP it holds a synchronized copy of user attributes and group membership but no passwords or MFA devices.
  scope: IAM Identity Center identity store.
  link: [does not create IAM users and groups](../facts/iam.md#iam-idc-no-iam-users-own-identity-store)
  link: [no authentication material like passwords or MFA devices](../facts/iam.md#iam-idc-no-iam-users-own-identity-store)
iam-idc-on-premises-ad-two-options
  claim: On-premises Active Directory connects to IAM Identity Center in two ways: through AD Connector, a directory gateway that redirects requests without caching information in the cloud, or through a trust relationship with AWS Managed Microsoft AD.
  scope: on-premises Active Directory as the IAM Identity Center identity source.
  link: [use AD Connector, or (2) use an AWS Managed Microsoft AD trust relationship](../facts/iam.md#iam-idc-on-premises-ad-two-options)
  link: [without caching any information in the cloud](../facts/iam.md#iam-idc-on-premises-ad-two-options)
iam-idc-one-identity-source-at-a-time
  claim: IAM Identity Center can have only one directory or one SAML 2.0 identity provider connected at any given time, although you can change which identity source is connected.
  scope: per IAM Identity Center instance.
  link: [only one directory or one SAML 2.0 identity provider](../facts/iam.md#iam-idc-one-identity-source-at-a-time)
iam-idc-organization-instance-best-practice
  claim: IAM Identity Center has organization instances and account instances; the organization instance is the best practice, it is the only instance type that manages access to AWS accounts, and it is deployed in the AWS Organizations management account.
  scope: IAM Identity Center instances.
  link: [the only instance type that manages access to AWS accounts](../facts/iam.md#iam-idc-organization-instance-best-practice)
  link: [deployed in the AWS Organizations management account](../facts/iam.md#iam-idc-organization-instance-best-practice)
iam-idc-permission-set-session-duration
  claim: A new permission set has a session duration of 1 hour by default; the minimum is 1 hour and the maximum is 12 hours.
  scope: per permission set; default; adjustable.
  link: [1 hour](../facts/iam.md#iam-idc-permission-set-session-duration)
  link: [maximum of 12 hours](../facts/iam.md#iam-idc-permission-set-session-duration)
iam-idc-permission-sets
  claim: A permission set is a collection of permissions you create in IAM Identity Center, modeled on AWS managed policies for job functions or any AWS managed policies; IAM Identity Center applies it to the selected accounts automatically, and when users access the accounts through the AWS access portal, these permissions restrict what they can do within those accounts.
  link: [Permission sets are a collection of permissions](../facts/iam.md#iam-idc-permission-sets)
  link: [applies these permissions to the selected accounts automatically](../facts/iam.md#iam-idc-permission-sets)
iam-idc-recommended-front-door-for-workforce
  claim: AWS calls IAM Identity Center its recommended front door into AWS and the primary tool to manage the AWS access of workforce users.
  link: [recommended front door into AWS](../facts/iam.md#iam-idc-recommended-front-door-for-workforce)
  link: [primary tool to manage the AWS access of your workforce users](../facts/iam.md#iam-idc-recommended-front-door-for-workforce)
iam-idc-scim-automatic-provisioning
  claim: Identities must be provisioned into IAM Identity Center before you assign permissions; from Okta Universal Directory, Microsoft Entra ID, OneLogin and PingFederate this happens automatically through the SCIM standard, and other IdPs are provisioned through the console.
  scope: IAM Identity Center with an external identity provider.
  link: [System for Cross-domain Identity Management (SCIM) standard](../facts/iam.md#iam-idc-scim-automatic-provisioning)
  link: [must be provisioned into IAM Identity Center before you can assign permissions](../facts/iam.md#iam-idc-scim-automatic-provisioning)
iam-instance-profile-console-creates-same-name
  claim: When you create a role for EC2 in the AWS Management Console, the console creates an instance profile with the same name as the role; if you manage roles from the AWS CLI or API, you create roles and instance profiles as separate actions, and the IAM Role list in the EC2 console lists instance profile names, not role names.
  scope: roles for EC2.
  link: [creates an instance profile with the same name as the role](../facts/iam.md#iam-instance-profile-console-creates-same-name)
  link: [create roles and instance profiles as separate actions](../facts/iam.md#iam-instance-profile-console-creates-same-name)
  link: [lists instance profile names, not role names](../facts/iam.md#iam-instance-profile-console-creates-same-name)
iam-instance-profile-one-role-and-metadata-credentials
  claim: You use an instance profile to pass an IAM role to an EC2 instance; an instance profile can hold only one IAM role and this limit cannot be increased, and only one role can be assigned to an instance at a time. Applications and the AWS CLI on the instance get automatic temporary security credentials from the instance metadata, so they do not have to explicitly get the credentials.
  scope: per instance profile and per EC2 instance; maximum.
  link: [can hold only one IAM role and this limit cannot be increased](../facts/iam.md#iam-instance-profile-one-role-and-metadata-credentials)
  link: [only one role can be assigned to an instance at a time](../facts/iam.md#iam-instance-profile-one-role-and-metadata-credentials)
  link: [get automatic temporary security credentials from the instance metadata](../facts/iam.md#iam-instance-profile-one-role-and-metadata-credentials)
iam-job-function-poweruseraccess-excludes-iam-org
  claim: In the PowerUserAccess managed policy (developer power user job function), the first statement uses NotAction to allow all actions for all services and resources except IAM, AWS Organizations and AWS Account Management; a second statement grants IAM permissions to create a service-linked role, and the policy also grants Organizations permissions to view information about the user's organization. AdministratorAccess grants all actions for all services and resources in the account.
  scope: AWS managed policies for job functions.
  link: [except IAM, AWS Organizations and AWS Account Management](../facts/iam.md#iam-job-function-poweruseraccess-excludes-iam-org)
  link: [AdministratorAccess grants all actions for all services and resources](../facts/iam.md#iam-job-function-poweruseraccess-excludes-iam-org)
iam-job-function-viewonly-and-securityaudit
  claim: The ViewOnlyAccess managed policy grants List, Describe, Get, View and Lookup access to resources, and SecurityAudit grants permissions to view configuration data for many services and to review their logs.
  scope: AWS managed policies for job functions.
  link: [List, Describe, Get, View and Lookup access](../facts/iam.md#iam-job-function-viewonly-and-securityaudit)
  link: [view configuration data for many services and to review their logs](../facts/iam.md#iam-job-function-viewonly-and-securityaudit)
iam-kms-cross-account-key-policy-and-iam-policy
  claim: To let another account use a KMS key, the key policy must give the external account permission and IAM policies in the external account must delegate that permission to its users and roles; neither policy alone is sufficient.
  scope: cross-account use of an AWS KMS key.
  link: [neither policy alone is sufficient](../facts/iam.md#iam-kms-cross-account-key-policy-and-iam-policy)
  link: [the key policy must give the external account permission](../facts/iam.md#iam-kms-cross-account-key-policy-and-iam-policy)
iam-kms-grants-used-by-services
  claim: A KMS grant is a policy instrument that allows AWS principals or service principals to use KMS keys in cryptographic operations; grants are considered along with key policies and IAM policies, and you can create a grant, use it and delete it without changing your key policies or IAM policies. AWS services that encrypt data at rest commonly create a grant, use it, and retire it when the task is complete.
  scope: AWS KMS grants.
  link: [without changing your key policies or IAM policies](../facts/iam.md#iam-kms-grants-used-by-services)
  link: [create a grant, use it, and retire it](../facts/iam.md#iam-kms-grants-used-by-services)
iam-kms-iam-policy-needs-key-policy-permission
  claim: Unless the key policy explicitly allows it, IAM policies cannot allow access to a KMS key; an IAM policy can still deny access without the key policy, and the default key policy enables IAM policies.
  scope: AWS KMS key access; unless the key policy explicitly allows it.
  link: [IAM policies cannot allow access to a KMS key](../facts/iam.md#iam-kms-iam-policy-needs-key-policy-permission)
  link: [the default key policy enables IAM policies](../facts/iam.md#iam-kms-iam-policy-needs-key-policy-permission)
iam-kms-key-policy-required-primary-control
  claim: A key policy is the resource policy of a KMS key and the primary way to control access to it; every KMS key must have exactly one key policy. You can also use IAM policies and grants to control access to the key, but unless the key policy explicitly allows it, IAM policies cannot allow access to the KMS key.
  scope: per AWS KMS key; fixed.
  link: [every KMS key must have exactly one key policy](../facts/iam.md#iam-kms-key-policy-required-primary-control)
  link: [the primary way to control access](../facts/iam.md#iam-kms-key-policy-required-primary-control)
iam-kms-no-principal-has-access-unless-allowed
  claim: No AWS principal, not even the account root user or the key creator, has any permission to a KMS key unless a key policy, IAM policy or grant explicitly allows it and nothing denies it.
  scope: AWS KMS key access.
  link: [not even the account root user or the key creator](../facts/iam.md#iam-kms-no-principal-has-access-unless-allowed)
  link: [unless a key policy, IAM policy or grant explicitly allows it](../facts/iam.md#iam-kms-no-principal-has-access-unless-allowed)
iam-lambda-resource-policy-vs-execution-role
  claim: A Lambda function uses two kinds of policy: its execution role holds the permissions the function needs to reach other AWS resources, and every Lambda function must have one; a resource-based policy on the function grants other accounts and AWS services access to it, and when a service such as Amazon S3 calls the function, Lambda considers only the resource-based policy.
  scope: per Lambda function.
  link: [Lambda considers only the resource-based policy](../facts/iam.md#iam-lambda-resource-policy-vs-execution-role)
  link: [Every Lambda function must have an execution role](../facts/iam.md#iam-lambda-resource-policy-vs-execution-role)
  link: [access to your Lambda functions](../facts/iam.md#iam-lambda-resource-policy-vs-execution-role)
iam-last-accessed-access-advisor-tab
  claim: Last accessed information is shown on the Access Advisor tab of the IAM console for a user, group, role or policy.
  link: [Access Advisor](../facts/iam.md#iam-last-accessed-access-advisor-tab)
iam-last-accessed-counts-denied-attempts
  claim: Service last accessed data counts every attempt to call an AWS API, not only successful ones, so an unexpected entry does not by itself mean the account was compromised.
  scope: IAM service last accessed data.
  link: [not just the successful attempts](../facts/iam.md#iam-last-accessed-counts-denied-attempts)
  link: [the request might have been denied](../facts/iam.md#iam-last-accessed-counts-denied-attempts)
  say: not only successful attempts | the request may have been denied
iam-last-accessed-organizations-scp-services
  claim: Signed in with management account credentials, you can view service last accessed information for an organization root, OU or account; it covers services allowed by an SCP and shows which principals (root user, IAM user or role) last attempted to access each service and when.
  scope: AWS Organizations entities and policies; signed in with management account credentials.
  link: [management account credentials](../facts/iam.md#iam-last-accessed-organizations-scp-services)
  link: [services allowed by an SCP](../facts/iam.md#iam-last-accessed-organizations-scp-services)
iam-last-accessed-passrole-not-tracked
  claim: The iam:PassRole action is not tracked and does not appear in IAM action last accessed information.
  scope: IAM action last accessed information.
  link: [is not tracked](../facts/iam.md#iam-last-accessed-passrole-not-tracked)
  link: [iam:PassRole](../facts/iam.md#iam-last-accessed-passrole-not-tracked)
  say: not tracked | I-A-M pass role
iam-last-accessed-recent-activity-within-four-hours
  claim: Recent activity appears in the IAM console last accessed information within four hours.
  scope: IAM console last accessed information; maximum.
  link: [within four hours](../facts/iam.md#iam-last-accessed-recent-activity-within-four-hours)
  say: within four hours
iam-last-accessed-tracking-period-400-days
  claim: The tracking period for service last accessed information is at least 400 days, depending on when the service started tracking; for a role, last activity and last accessed data cover the trailing 400 days, or less in a Region that began supporting these features within the last year.
  scope: per IAM identity or Organizations entity; fixed; not adjustable; can be shorter in a Region that began tracking recently.
  link: [at least 400 days](../facts/iam.md#iam-last-accessed-tracking-period-400-days)
  link: [the trailing 400 days](../facts/iam.md#iam-last-accessed-tracking-period-400-days)
  say: at least four hundred days | the last four hundred days
iam-limit-account-alias-length
  claim: An alias for an AWS account ID must be 3–63 characters long.
  scope: per AWS account alias; maximum; not adjustable; cannot be increased.
  link: [3–63 characters](../facts/iam.md#iam-limit-account-alias-length)
  say: three to sixty-three characters
iam-limit-group-name-length
  claim: An IAM group name can be at most 128 characters.
  scope: per IAM group name; maximum; not adjustable; cannot be increased.
  link: [128 characters](../facts/iam.md#iam-limit-group-name-length)
  say: one hundred twenty-eight characters
iam-limit-inline-policy-size
  claim: An entity can have any number of inline policies, but their total size per entity cannot exceed 2,048 characters for a user, 10,240 characters for a role and 5,120 characters for a group; white space is not counted.
  scope: per IAM user, role or group (sum of all inline policies); maximum; not adjustable; white space is not counted.
  link: [2,048 characters](../facts/iam.md#iam-limit-inline-policy-size)
  link: [10,240 characters](../facts/iam.md#iam-limit-inline-policy-size)
  link: [5,120 characters](../facts/iam.md#iam-limit-inline-policy-size)
  say: two thousand forty-eight characters for a user | ten thousand two hundred forty characters for a role | five thousand one hundred twenty characters for a group
iam-limit-instance-profile-name-length
  claim: An instance profile name can be at most 128 characters.
  scope: per instance profile name; maximum; not adjustable; cannot be increased.
  link: [128 characters](../facts/iam.md#iam-limit-instance-profile-name-length)
  say: one hundred twenty-eight characters
iam-limit-login-password-length
  claim: A password for an IAM login profile can be 1–128 characters long.
  scope: per IAM user login profile; maximum; not adjustable; character limit; cannot be increased.
  link: [1–128 characters](../facts/iam.md#iam-limit-login-password-length)
  say: one to one hundred twenty-eight characters
iam-limit-managed-policy-size
  claim: Each customer managed policy cannot exceed 6,144 characters, not counting white space, and this limit cannot be raised.
  scope: per managed policy; maximum; not adjustable; white space is not counted.
  link: [6,144 characters](../facts/iam.md#iam-limit-managed-policy-size)
  say: six thousand one hundred forty-four characters
iam-limit-path-length
  claim: An IAM path can be at most 512 characters.
  scope: per IAM path; maximum; not adjustable; cannot be increased.
  link: [512 characters](../facts/iam.md#iam-limit-path-length)
  say: five hundred twelve characters
iam-limit-policy-name-length
  claim: An IAM policy name can be at most 128 characters.
  scope: per IAM policy name; maximum; not adjustable; cannot be increased.
  link: [128 characters](../facts/iam.md#iam-limit-policy-name-length)
  say: one hundred twenty-eight characters
iam-limit-role-name-length
  claim: A role name can be at most 64 characters, and for the console Switch Role feature the path and role name combined cannot exceed 64 characters.
  scope: per IAM role; maximum; not adjustable; path plus role name for Switch Role in the console.
  link: [64 characters](../facts/iam.md#iam-limit-role-name-length)
  say: sixty-four characters
iam-limit-role-session-duration-row
  claim: The quotas table lists the role session duration limit as 12 hours: a CLI or API caller can request from 900 seconds (15 minutes) up to the role's maximum session duration setting, which can range 1–12 hours, and gets one hour when DurationSeconds is omitted.
  scope: per role session; maximum; not adjustable; up to the role's maximum session duration setting; AWS service sessions are not limited by it.
  link: [12 hours](../facts/iam.md#iam-limit-role-session-duration-row)
  link: [900 seconds (15 minutes)](../facts/iam.md#iam-limit-role-session-duration-row)
  say: twelve hours | nine hundred seconds, fifteen minutes
iam-limit-role-session-name-length
  claim: A role session name can be at most 64 characters.
  scope: per role session name; maximum; not adjustable; cannot be increased.
  link: [64 characters](../facts/iam.md#iam-limit-role-session-name-length)
  say: sixty-four characters
iam-limit-saml-response-size
  claim: A base64-encoded SAML authentication response passed to AssumeRoleWithSAML can be at most 100,000 characters.
  scope: per AssumeRoleWithSAML call; maximum; not adjustable; base64 encoded.
  link: [100,000 characters](../facts/iam.md#iam-limit-saml-response-size)
  say: one hundred thousand characters
iam-limit-session-tags
  claim: A role session can carry up to 50 session tags; each tag key is at most 128 characters and each value at most 256 characters, and session tags add to the session token size.
  scope: per role session; maximum; not adjustable; session policies and session tags add to the session token size.
  link: [up to 50 session tags](../facts/iam.md#iam-limit-session-tags)
  link: [128 characters](../facts/iam.md#iam-limit-session-tags)
  link: [256 characters](../facts/iam.md#iam-limit-session-tags)
  say: up to fifty session tags | one hundred twenty-eight characters | two hundred fifty-six characters
iam-limit-tag-key-length
  claim: A tag key can be at most 128 characters, both for tags on IAM resources and for session tags.
  scope: per tag key (IAM resources and session tags); maximum; not adjustable; cannot be increased.
  link: [128 characters](../facts/iam.md#iam-limit-tag-key-length)
  say: one hundred twenty-eight characters
iam-limit-tag-value-length
  claim: A tag value can be at most 256 characters, both for tags on IAM resources and for session tags, and it can be empty (0 characters).
  scope: per tag value (IAM resources and session tags); maximum; not adjustable; cannot be increased.
  link: [256 characters](../facts/iam.md#iam-limit-tag-value-length)
  link: [0 characters](../facts/iam.md#iam-limit-tag-value-length)
  say: two hundred fifty-six characters | zero characters
iam-limit-user-name-length
  claim: An IAM user name can be at most 64 characters.
  scope: per IAM user name; maximum; not adjustable; cannot be increased.
  link: [64 characters](../facts/iam.md#iam-limit-user-name-length)
  say: sixty-four characters
iam-long-term-keys-valid-until-revoked-temporary-expire
  claim: Long-term access keys of IAM users and the root user stay valid until you revoke them by hand; temporary credentials from roles and STS expire after a short period, which limits the damage of an accidental exposure.
  scope: access keys and temporary security credentials.
  link: [remain valid until you manually revoke them](../facts/iam.md#iam-long-term-keys-valid-until-revoked-temporary-expire)
  link: [expire after a short period of time](../facts/iam.md#iam-long-term-keys-valid-until-revoked-temporary-expire)
  link: [reduce your risk in case credentials are accidentally exposed](../facts/iam.md#iam-long-term-keys-valid-until-revoked-temporary-expire)
iam-managed-vs-inline-policies
  claim: A managed policy is standalone and can be attached to many users, groups and roles, and AWS recommends managed policies in most cases; an inline policy is embedded in a single identity with a strict one-to-one relationship and is deleted with the identity.
  scope: identity-based policies.
  link: [can be attached to many users, groups and roles](../facts/iam.md#iam-managed-vs-inline-policies)
  link: [a strict one-to-one relationship and is deleted with the identity](../facts/iam.md#iam-managed-vs-inline-policies)
  link: [AWS recommends managed policies in most cases](../facts/iam.md#iam-managed-vs-inline-policies)
iam-mfa-age-condition
  claim: To allow access only within a set time after MFA sign-in, compare the aws:MultiFactorAuthAge key with a numeric condition (for example 3600 seconds); the key is not present if MFA was not used.
  scope: global condition key aws:MultiFactorAuthAge.
  link: [aws:MultiFactorAuthAge](../facts/iam.md#iam-mfa-age-condition)
  link: [3600 seconds](../facts/iam.md#iam-mfa-age-condition)
iam-mfa-assumerole-credentials-lack-mfa-context
  claim: Temporary credentials returned by AssumeRole do not carry MFA information in the context, so MFA is enforced when the role is assumed; to protect resources with resource-based policies by MFA you must use GetSessionToken.
  scope: MFA-protected API access.
  link: [do not carry MFA information in the context](../facts/iam.md#iam-mfa-assumerole-credentials-lack-mfa-context)
  link: [you must use GetSessionToken](../facts/iam.md#iam-mfa-assumerole-credentials-lack-mfa-context)
iam-mfa-condition-key-multifactorauthpresent
  claim: To enforce MFA for API operations, a policy must include the aws:MultiFactorAuthPresent condition key; for cross-account delegation the role's trust policy must include it. The key is present only with short-term credentials; long-term access keys do not include it.
  scope: MFA-protected API access.
  link: [the aws:MultiFactorAuthPresent condition key](../facts/iam.md#iam-mfa-condition-key-multifactorauthpresent)
  link: [the role's trust policy must include it](../facts/iam.md#iam-mfa-condition-key-multifactorauthpresent)
  link: [long-term access keys do not include it](../facts/iam.md#iam-mfa-condition-key-multifactorauthpresent)
iam-mfa-devices-up-to-eight
  claim: The root user and each IAM user can register up to eight MFA devices of any type, and only one device is needed to sign in.
  scope: per IAM user or root user; maximum; not adjustable; any mix of device types.
  link: [up to eight MFA devices](../facts/iam.md#iam-mfa-devices-up-to-eight)
  say: up to eight MFA devices
iam-mfa-protection-only-with-temporary-credentials
  claim: MFA protection for API operations is available only with temporary security credentials, which must be obtained with AssumeRole or GetSessionToken.
  scope: MFA-protected API access.
  link: [available only with temporary security credentials](../facts/iam.md#iam-mfa-protection-only-with-temporary-credentials)
  link: [obtained with AssumeRole or GetSessionToken](../facts/iam.md#iam-mfa-protection-only-with-temporary-credentials)
iam-mfa-types-supported
  claim: You can enable MFA for the root user and for IAM users, and AWS supports three MFA types: passkeys and security keys (FIDO), virtual authenticator applications (TOTP) and hardware TOTP tokens; AWS recommends phishing-resistant passkeys and security keys.
  scope: MFA devices for the root user and IAM users.
  link: [Passkeys and security keys](../facts/iam.md#iam-mfa-types-supported)
  link: [Virtual authenticator applications](../facts/iam.md#iam-mfa-types-supported)
  link: [Hardware TOTP tokens](../facts/iam.md#iam-mfa-types-supported)
  say: passkeys and security keys | virtual authenticator apps | hardware TOTP tokens
iam-offered-at-no-additional-charge
  claim: IAM is offered at no additional charge.
  scope: AWS Identity and Access Management (IAM).
  link: [no additional charge](../facts/iam.md#iam-offered-at-no-additional-charge)
iam-outbound-identity-federation
  claim: IAM outbound identity federation lets AWS workloads call the STS GetWebIdentityToken API to get short-lived signed JSON Web Tokens (JWTs) and use them to access external services, so no long-term credentials of those services are stored.
  scope: per AWS workload (IAM principal).
  link: [GetWebIdentityToken](../facts/iam.md#iam-outbound-identity-federation)
  link: [short-lived JSON Web Tokens (JWTs)](../facts/iam.md#iam-outbound-identity-federation)
  say: Get Web Identity Token | short-lived JSON web tokens
  changed: 2025-11-19: was using long-term credentials or implementing complex workarounds
iam-passrole-is-a-permission-not-api-call
  claim: PassRole is a permission, not an API call, so no CloudTrail logs are generated for IAM PassRole; you review the CloudTrail log of the call that created or modified the resource that received the role.
  scope: iam:PassRole.
  link: [PassRole is a permission, not an API call](../facts/iam.md#iam-passrole-is-a-permission-not-api-call)
  link: [no CloudTrail logs are generated for IAM PassRole](../facts/iam.md#iam-passrole-is-a-permission-not-api-call)
iam-passrole-prevents-privilege-escalation
  claim: Scope iam:PassRole so that a user cannot pass a role that has more permissions than you want the user to have; you limit it to approved roles with the Resource element and to a service with the iam:PassedToService condition key.
  scope: passing a role to an AWS service.
  link: [a role that has more permissions than you want the user to have](../facts/iam.md#iam-passrole-prevents-privilege-escalation)
  link: [the iam:PassedToService condition key](../facts/iam.md#iam-passrole-prevents-privilege-escalation)
iam-passrole-required-to-give-role-to-service
  claim: To configure many AWS services you pass an IAM role to the service, which lets the service assume the role later and act on your behalf; the user who passes the role must have the iam:PassRole permission for that role, and PassRole only works with a service in the same AWS account. In the documented EC2 example, the setup also needs a trust policy for the role that allows the service to assume the role.
  scope: passing a role to an AWS service.
  link: [must have the iam:PassRole permission for that role](../facts/iam.md#iam-passrole-required-to-give-role-to-service)
  link: [PassRole only works with a service in the same AWS account](../facts/iam.md#iam-passrole-required-to-give-role-to-service)
  link: [a trust policy for the role that allows the service to assume the role](../facts/iam.md#iam-passrole-required-to-give-role-to-service)
iam-password-expiration-enforced-immediately
  claim: A new password expiration period is enforced immediately for all existing passwords, while new minimum length and character type rules apply only the next time each user changes the password.
  scope: per AWS account, IAM user passwords.
  link: [the expiration period is enforced immediately](../facts/iam.md#iam-password-expiration-enforced-immediately)
  link: [the next time that your users change their passwords](../facts/iam.md#iam-password-expiration-enforced-immediately)
  say: expiry applies at once | length rules wait for the next password change
iam-password-expired-user-keeps-access-keys
  claim: When an IAM user's password expires, the user can no longer sign in to the AWS Management Console but can still use the user's access keys.
  scope: per IAM user; password expired.
  link: [can continue to use their access keys](../facts/iam.md#iam-password-expired-user-keeps-access-keys)
  link: [can't sign in to the AWS Management Console](../facts/iam.md#iam-password-expired-user-keeps-access-keys)
  say: access keys keep working | no console sign-in
iam-password-policy-custom-expiration-range
  claim: A custom password policy can turn on password expiration and set how long IAM user passwords stay valid after they are set: a minimum of 1 and a maximum of 1,095 days.
  scope: per AWS account, IAM user passwords; maximum; not adjustable; custom password policy with password expiration turned on.
  link: [a minimum of 1](../facts/iam.md#iam-password-policy-custom-expiration-range)
  link: [1,095 days](../facts/iam.md#iam-password-policy-custom-expiration-range)
  say: one day | one thousand ninety-five days
iam-password-policy-custom-min-length-range
  claim: In a custom account password policy, the password minimum length can be set from 6 characters up to 128 characters.
  scope: per AWS account, IAM user passwords; maximum; not adjustable; custom password policy.
  link: [6 characters](../facts/iam.md#iam-password-policy-custom-min-length-range)
  link: [128 characters](../facts/iam.md#iam-password-policy-custom-min-length-range)
  say: six characters | one hundred twenty-eight characters
iam-password-policy-custom-reuse-range
  claim: A custom password policy can prevent IAM users from reusing from 1 up to 24 previous passwords.
  scope: per AWS account, IAM user passwords; maximum; not adjustable; custom password policy with password reuse prevention.
  link: [24 previous passwords](../facts/iam.md#iam-password-policy-custom-reuse-range)
  say: twenty-four previous passwords
iam-password-policy-default-rules
  claim: When no custom password policy is set, IAM user passwords follow the default AWS password policy: a minimum length of 8 characters, a maximum length of 128 characters, and a mix of at least three of these character types: uppercase, lowercase, numbers and non-alphanumeric characters.
  scope: per AWS account, IAM user passwords; default; adjustable; no custom password policy is set.
  link: [8 characters](../facts/iam.md#iam-password-policy-default-rules)
  link: [128 characters](../facts/iam.md#iam-password-policy-default-rules)
  link: [three of the following mix of character types](../facts/iam.md#iam-password-policy-default-rules)
  say: eight characters | one hundred twenty-eight characters | three of the four character types
iam-password-policy-scope-and-lockout
  claim: The IAM password policy does not apply to the root user password or to access keys; an expired password blocks console sign-in but not access keys, and IAM cannot lock a user out after failed sign-in attempts.
  scope: per AWS account (IAM users).
  link: [does not apply to the AWS account root user password or IAM user access keys](../facts/iam.md#iam-password-policy-scope-and-lockout)
  link: [You can't create a "lockout policy"](../facts/iam.md#iam-password-policy-scope-and-lockout)
  say: it does not cover the root password or access keys | there is no lockout policy
iam-permissions-boundary-sets-maximum-does-not-grant
  claim: A permissions boundary is a managed policy that sets the maximum permissions an identity-based policy can grant to a user or role; it does not grant permissions on its own, and the entity can perform only the actions allowed by both its identity-based policies and its boundary. A boundary does not limit what a resource-based policy can grant.
  scope: per IAM user or role.
  link: [does not grant permissions](../facts/iam.md#iam-permissions-boundary-sets-maximum-does-not-grant)
  link: [maximum permissions that an identity-based policy can grant](../facts/iam.md#iam-permissions-boundary-sets-maximum-does-not-grant)
  link: [allowed by both its identity-based policies and its permissions boundaries](../facts/iam.md#iam-permissions-boundary-sets-maximum-does-not-grant)
  link: [do not define the maximum permissions that a resource-based policy can grant](../facts/iam.md#iam-permissions-boundary-sets-maximum-does-not-grant)
iam-policy-default-version-is-operative
  claim: Exactly one version of a managed policy is the default version, and it is the version in effect for every user, group and role the policy is attached to; a policy with a single version uses it as the default automatically.
  scope: per managed policy.
  link: [the default version](../facts/iam.md#iam-policy-default-version-is-operative)
  link: [automatically set as the default](../facts/iam.md#iam-policy-default-version-is-operative)
  say: the default version | set as default automatically
iam-policy-simulator-no-real-request
  claim: The IAM policy simulator does not make an actual AWS service request, so you can test requests that would otherwise change your environment; the only result is whether each action would be allowed or denied.
  scope: IAM policy simulator.
  link: [does not make an actual AWS service request](../facts/iam.md#iam-policy-simulator-no-real-request)
  link: [The only result is whether each requested action would be allowed or denied](../facts/iam.md#iam-policy-simulator-no-real-request)
iam-policy-simulator-scps-yes-rcps-no
  claim: The policy simulator tests identity-based policies, permissions boundaries, SCPs and resource-based policies that you provide; it evaluates SCPs but does not support resource control policies (RCPs).
  scope: IAM policy simulator.
  link: [identity-based policies, IAM permissions boundaries, service control policies (SCPs), and resource-based policies](../facts/iam.md#iam-policy-simulator-scps-yes-rcps-no)
  link: [does not support resource control policies (RCPs)](../facts/iam.md#iam-policy-simulator-scps-yes-rcps-no)
iam-policy-statement-required-elements
  claim: The Effect element is required and its values are Allow and Deny; a statement must include either an Action or a NotAction element and either a Resource or a NotResource element; a Condition element is optional.
  scope: IAM JSON policy statement.
  link: [The Effect element is required](../facts/iam.md#iam-policy-statement-required-elements)
  link: [either an Action or a NotAction element](../facts/iam.md#iam-policy-statement-required-elements)
  link: [either a Resource or a NotResource element](../facts/iam.md#iam-policy-statement-required-elements)
iam-policy-types-nine
  claim: AWS supports nine types of policies: identity-based policies, resource-based policies, VPC endpoint policies, permissions boundaries, Organizations SCPs, Organizations RCPs, ACLs, RAM resource shares and session policies.
  scope: policy types that AWS evaluates.
  link: [nine types of policies](../facts/iam.md#iam-policy-types-nine)
  link: [identity-based policies, resource-based policies, VPC endpoint policies, permissions boundaries](../facts/iam.md#iam-policy-types-nine)
  say: nine types of policies
iam-policy-variables-where-and-version
  claim: Policy variables such as ${aws:username} can be used in the Resource element and in string comparisons in the Condition element, and they need the Version element set to 2012-10-17; without it they are treated as literal strings.
  scope: IAM policy variables.
  link: [in the Resource element and in string comparisons in the Condition element](../facts/iam.md#iam-policy-variables-where-and-version)
  link: [set to 2012-10-17](../facts/iam.md#iam-policy-variables-where-and-version)
iam-policy-versions-cli-must-delete-before-sixth
  claim: A managed policy can have up to five versions; to change it beyond five versions with the AWS CLI or API, you first delete an existing version, while the console prompts you to delete one; inline policies have no versions.
  scope: per managed policy; maximum; AWS CLI or AWS API; the console asks which version to delete.
  link: [five versions](../facts/iam.md#iam-policy-versions-cli-must-delete-before-sixth)
  link: [you must first delete one or more existing versions](../facts/iam.md#iam-policy-versions-cli-must-delete-before-sixth)
  say: five versions | delete an old version first
iam-policy-versions-five
  claim: IAM keeps up to five versions of a customer managed policy; inline policies have no versions, any version except the default can be deleted, and rolling back means setting an older version as the default.
  scope: per customer managed policy; maximum; not adjustable; inline policies are not versioned.
  link: [up to five versions](../facts/iam.md#iam-policy-versions-five)
  link: [setting the previous version as the *default* version](../facts/iam.md#iam-policy-versions-five)
  say: up to five versions | set the previous version as the default version
iam-principal-account-delegates-to-account
  claim: Naming an AWS account in the Principal element delegates authority to that account, and an administrator there must then grant access to a user or role; the account ARN (ending in :root) does not limit the permission to the root user.
  scope: Principal element of a resource-based policy.
  link: [delegates authority to that account](../facts/iam.md#iam-principal-account-delegates-to-account)
  link: [does not limit the permission to the root user](../facts/iam.md#iam-principal-account-delegates-to-account)
iam-principal-element-not-in-identity-policies
  claim: You cannot use the Principal element in an identity-based policy; there the principal is implicitly the identity the policy is attached to.
  scope: IAM JSON policy element Principal.
  link: [cannot use the Principal element in an identity-based policy](../facts/iam.md#iam-principal-element-not-in-identity-policies)
  link: [the principal is implicitly the identity the policy is attached to](../facts/iam.md#iam-principal-element-not-in-identity-policies)
iam-principal-element-resource-policy-not-identity-policy
  claim: If you create a resource-based policy, you must indicate the account, user, role, or AWS STS federated user principal to which you would like to allow or deny access.
  scope: Principal element of a resource-based policy.
  link: [you must indicate the account, user, role, or AWS STS federated user principal](../facts/iam.md#iam-principal-element-resource-policy-not-identity-policy)
iam-principal-group-cannot-be-principal
  claim: You cannot identify a user group as a principal in a policy, because groups relate to permissions, not authentication.
  scope: IAM JSON policy element Principal.
  link: [cannot identify a user group as a principal](../facts/iam.md#iam-principal-group-cannot-be-principal)
  link: [groups relate to permissions, not authentication](../facts/iam.md#iam-principal-group-cannot-be-principal)
iam-principal-service-no-wildcard
  claim: Service roles must include a trust policy that names which principals can assume the role, sometimes a service principal you specify; the service principal in a policy can't be "Service": "*".
  scope: service principals in trust policies.
  link: [Service roles must include a trust policy](../facts/iam.md#iam-principal-service-no-wildcard)
  link: [the service principal in a policy can't be "Service": "*"](../facts/iam.md#iam-principal-service-no-wildcard)
iam-principal-wildcard-is-public
  claim: In a resource-based policy, a wildcard (*) principal with an Allow effect grants access to all users, including anonymous users (public access); principals in other accounts also need identity-based permissions in their own account.
  scope: Principal element of a resource-based policy; Allow effect.
  link: [including anonymous users (public access)](../facts/iam.md#iam-principal-wildcard-is-public)
  link: [principals in other accounts also need identity-based permissions](../facts/iam.md#iam-principal-wildcard-is-public)
iam-principals-have-no-permissions-by-default-root-has-full-access
  claim: IAM users and roles have no permissions by default and access is denied unless a policy explicitly allows it; the root user has full access by default and should be used only for tasks that require it.
  scope: per IAM user or role; default; not adjustable.
  link: [no permissions by default](../facts/iam.md#iam-principals-have-no-permissions-by-default-root-has-full-access)
  link: [denied by default and is allowed only when a policy explicitly grants access](../facts/iam.md#iam-principals-have-no-permissions-by-default-root-has-full-access)
  link: [full access by default](../facts/iam.md#iam-principals-have-no-permissions-by-default-root-has-full-access)
iam-quota-customer-managed-policies-per-account
  claim: An account can have 1500 customer managed policies by default; the quota can be raised to a maximum of 10000. Before 2026-05-05 the maximum was 5,000.
  scope: per AWS account; default; adjustable.
  link: [1500](../facts/iam.md#iam-quota-customer-managed-policies-per-account)
  link: [10000](../facts/iam.md#iam-quota-customer-managed-policies-per-account)
  say: fifteen hundred | ten thousand
  changed: 2026-05-05: was 5,000
iam-quota-groups-per-account
  claim: An account can have 300 IAM groups by default; the quota can be raised to a maximum of 500.
  scope: per AWS account; default; adjustable.
  link: [300](../facts/iam.md#iam-quota-groups-per-account)
  link: [500](../facts/iam.md#iam-quota-groups-per-account)
  say: three hundred | five hundred
iam-quota-groups-per-user
  claim: An IAM user can belong to at most 10 groups, and this quota is not adjustable.
  scope: per IAM user; maximum; not adjustable.
  link: [10](../facts/iam.md#iam-quota-groups-per-user)
  say: ten
iam-quota-idps-per-saml-provider
  claim: An IAM SAML provider object can hold up to 10 identity providers, and the quota is not adjustable.
  scope: per IAM SAML provider object; maximum; not adjustable.
  link: [10](../facts/iam.md#iam-quota-idps-per-saml-provider)
  say: ten
iam-quota-instance-profiles-per-account
  claim: An account can have 1000 instance profiles by default; the quota can be raised to a maximum of 10000. Before 2026-05-05 the maximum was 5,000.
  scope: per AWS account; default; adjustable.
  link: [1000](../facts/iam.md#iam-quota-instance-profiles-per-account)
  link: [10000](../facts/iam.md#iam-quota-instance-profiles-per-account)
  say: one thousand | ten thousand
  changed: 2026-05-05: was 5,000
iam-quota-keys-per-saml-provider
  claim: A SAML provider can have up to 10 keys assigned, and the quota is not adjustable.
  scope: per IAM SAML provider; maximum; not adjustable.
  link: [10](../facts/iam.md#iam-quota-keys-per-saml-provider)
  say: ten
iam-quota-managed-policies-per-group
  claim: An IAM group can have 10 managed policies attached, and this quota cannot be raised (default and maximum are both 10).
  scope: per IAM group; maximum; not adjustable.
  link: [10](../facts/iam.md#iam-quota-managed-policies-per-group)
  say: ten
iam-quota-managed-policies-per-role
  claim: An IAM role can have 20 managed policies attached by default, and the quota can be raised to a maximum of 25. Before August 19, 2026 the default was 10.
  scope: per IAM role; default; adjustable.
  link: [20](../facts/iam.md#iam-quota-managed-policies-per-role)
  link: [25](../facts/iam.md#iam-quota-managed-policies-per-role)
  say: twenty | twenty-five
  changed: 2026-08-19: was 10
iam-quota-managed-policies-per-user
  claim: An IAM user can have 10 managed policies attached by default; the quota can be raised to a maximum of 20.
  scope: per IAM user; default; adjustable.
  link: [10](../facts/iam.md#iam-quota-managed-policies-per-user)
  link: [20](../facts/iam.md#iam-quota-managed-policies-per-user)
  say: ten | twenty
iam-quota-oidc-providers-per-account
  claim: An account can have 100 OpenID Connect identity providers by default; the quota can be raised to a maximum of 700. Before 2026-05-05 the maximum was 100.
  scope: per AWS account; default; adjustable.
  link: [100](../facts/iam.md#iam-quota-oidc-providers-per-account)
  link: [700](../facts/iam.md#iam-quota-oidc-providers-per-account)
  say: one hundred | seven hundred
  changed: 2026-05-05: was 100
iam-quota-role-trust-policy-length
  claim: A role trust policy can be 2048 characters by default, and the quota can be raised to a maximum of 8192 characters. Before 2026-05-05 the maximum was 4,096 characters.
  scope: per IAM role; default; adjustable.
  link: [2048 characters](../facts/iam.md#iam-quota-role-trust-policy-length)
  link: [8192 characters](../facts/iam.md#iam-quota-role-trust-policy-length)
  say: two thousand forty-eight characters | eight thousand one hundred ninety-two characters
  changed: 2026-05-05: was 4,096
iam-quota-roles-per-account
  claim: An account can have 1000 IAM roles by default; the quota can be raised to a maximum of 10000. Before 2026-05-05 the maximum was 5,000.
  scope: per AWS account; default; adjustable.
  link: [1000](../facts/iam.md#iam-quota-roles-per-account)
  link: [10000](../facts/iam.md#iam-quota-roles-per-account)
  say: one thousand | ten thousand
  changed: 2026-05-05: was 5,000
iam-quota-saml-providers-per-account
  claim: An account can have up to 100 SAML providers, and the quota is not adjustable.
  scope: per AWS account; maximum; not adjustable.
  link: [100](../facts/iam.md#iam-quota-saml-providers-per-account)
  say: one hundred
iam-quota-server-certificates-per-account
  claim: An account can store 20 server certificates in IAM by default, and the maximum quota in the IAM guide table is also 20.
  scope: per AWS account; default; adjustable; the IAM guide lists default 20 and maximum 20.
  link: [20](../facts/iam.md#iam-quota-server-certificates-per-account)
  say: twenty
iam-quota-signing-certificates-per-user
  claim: An IAM user can upload up to 2 signing certificates, and the quota is not adjustable.
  scope: per IAM user; maximum; not adjustable.
  link: [2](../facts/iam.md#iam-quota-signing-certificates-per-user)
  say: two
iam-quota-ssh-public-keys-per-user
  claim: An IAM user can have up to 5 SSH public keys, and the quota is not adjustable.
  scope: per IAM user; maximum; not adjustable.
  link: [5](../facts/iam.md#iam-quota-ssh-public-keys-per-user)
  say: five
iam-quota-tags-per-role
  claim: An IAM role can have up to 50 tags, and the quota is not adjustable.
  scope: per IAM role; maximum; not adjustable.
  link: [50](../facts/iam.md#iam-quota-tags-per-role)
  say: fifty
iam-quota-tags-per-user
  claim: An IAM user can have up to 50 tags, and the quota is not adjustable.
  scope: per IAM user; maximum; not adjustable.
  link: [50](../facts/iam.md#iam-quota-tags-per-user)
  say: fifty
iam-quota-users-per-account
  claim: An AWS account can have at most 5,000 IAM users, and this quota is not adjustable.
  scope: per AWS account; maximum; not adjustable.
  link: [5,000](../facts/iam.md#iam-quota-users-per-account)
  say: five thousand
iam-ram-share-without-resource-policies
  claim: AWS RAM resource shares let you share resources across accounts, OUs or the whole organization without writing a resource-based policy for each shared resource.
  link: [without writing individual resource-based policies for each shared resource](../facts/iam.md#iam-ram-share-without-resource-policies)
iam-rcp-allow-all-still-needs-iam-policies
  claim: A user or role without any IAM permission policies has no access, even if an applicable RCP allows all services, all actions and all resources.
  scope: AWS Organizations resource control policies.
  link: [has no access, even if an applicable RCP allows all services](../facts/iam.md#iam-rcp-allow-all-still-needs-iam-policies)
  link: [without any IAM permission policies has no access](../facts/iam.md#iam-rcp-allow-all-still-needs-iam-policies)
iam-rcp-applies-to-outside-principals-and-root
  claim: An RCP limits the principals that access a resource in a member account with an applicable RCP, whether or not the principal belongs to the organization, including root users; the exception is service-linked roles, because RCPs do not apply to calls made by service-linked roles. Use an RCP to restrict external principals and an SCP to limit your own principals.
  scope: resources in member accounts with an applicable RCP.
  link: [whether the principals belong to the same organizations](../facts/iam.md#iam-rcp-applies-to-outside-principals-and-root)
  link: [This includes root users](../facts/iam.md#iam-rcp-applies-to-outside-principals-and-root)
  link: [IAM principals that are external to your organization](../facts/iam.md#iam-rcp-applies-to-outside-principals-and-root)
iam-rcp-faq-maximum-permissions-on-resources
  claim: A resource control policy (RCP) centrally sets the maximum available permissions on the AWS resources in your organization, for example to allow access only by identities that belong to your organization.
  scope: resources in the member accounts of an organization.
  link: [centrally set the maximum available permissions to your AWS resources](../facts/iam.md#iam-rcp-faq-maximum-permissions-on-resources)
  link: [only be accessed by identities that belong to your organization](../facts/iam.md#iam-rcp-faq-maximum-permissions-on-resources)
iam-rcp-never-grants-limits-resources
  claim: An RCP never grants permissions; it sets the maximum available permissions for resources in member accounts, and it does not affect resources in the management account.
  scope: resources in member accounts; maximum.
  link: [An RCP never grants permissions](../facts/iam.md#iam-rcp-never-grants-limits-resources)
  link: [the maximum available permissions for resources in member accounts](../facts/iam.md#iam-rcp-never-grants-limits-resources)
  link: [does not affect resources in the management account](../facts/iam.md#iam-rcp-never-grants-limits-resources)
iam-rcp-no-effect-on-management-account
  claim: RCPs have no effect on resources in the management account of the organization.
  scope: AWS Organizations resource control policies.
  link: [no effect on resources in the management account](../facts/iam.md#iam-rcp-no-effect-on-management-account)
  link: [RCPs have no effect](../facts/iam.md#iam-rcp-no-effect-on-management-account)
iam-rcp-no-effect-on-service-linked-roles
  claim: The permissions of service-linked roles can't be restricted by RCPs.
  scope: AWS Organizations resource control policies.
  link: [service-linked roles can't be restricted by RCPs](../facts/iam.md#iam-rcp-no-effect-on-service-linked-roles)
  link: [can't be restricted by RCPs](../facts/iam.md#iam-rcp-no-effect-on-service-linked-roles)
iam-rcp-subset-of-services
  claim: RCPs apply only to resources of a subset of AWS services, and they do not apply to AWS managed KMS keys.
  scope: RCP supported services.
  link: [apply only to resources of a subset of AWS services](../facts/iam.md#iam-rcp-subset-of-services)
  link: [do not apply to AWS managed KMS keys](../facts/iam.md#iam-rcp-subset-of-services)
iam-request-context-contents
  claim: A request to AWS carries the actions or operations, the resources, the principal, environment data (IP address, user agent, SSL enabled status, timestamp) and resource data; AWS gathers this information into a request context, which IAM evaluates to authorize the request.
  scope: every request to AWS.
  link: [principal, resources, actions, and other environmental properties](../facts/iam.md#iam-request-context-contents)
  link: [which IAM evaluates to authorize the request](../facts/iam.md#iam-request-context-contents)
  link: [user agent, SSL enabled status, and the timestamp](../facts/iam.md#iam-request-context-contents)
  link: [Data related to the resource requested](../facts/iam.md#iam-request-context-contents)
iam-resource-based-policies-grant-direct-cross-account-access
  claim: Resource-based policies define who has access to a resource and which actions they can perform with it; you can attach them, for example, to S3 buckets, SQS queues, VPC endpoints and KMS keys, and the IAM FAQ says to use resource-based policies to grant direct, cross-account access.
  link: [grant direct, cross-account access](../facts/iam.md#iam-resource-based-policies-grant-direct-cross-account-access)
  link: [Amazon S3 buckets, Amazon SQS queues, VPC endpoints, and AWS Key Management Service (AWS KMS) encryption keys](../facts/iam.md#iam-resource-based-policies-grant-direct-cross-account-access)
iam-resource-based-policies-inline-only
  claim: Resource-based policies are inline only: there are no managed resource-based policies.
  scope: resource-based policies.
  link: [Resource-based policies are inline only](../facts/iam.md#iam-resource-based-policies-inline-only)
  link: [there are no managed resource-based policies](../facts/iam.md#iam-resource-based-policies-inline-only)
iam-resource-based-policy-examples
  claim: You can attach resource-based policies to S3 buckets, SQS queues, VPC endpoints, KMS encryption keys, DynamoDB tables and streams, and AWS Sign-In resources, among others.
  scope: resource-based policies.
  link: [S3 buckets, SQS queues, VPC endpoints, KMS encryption keys, DynamoDB tables and streams](../facts/iam.md#iam-resource-based-policy-examples)
  link: [attach resource-based policies to S3 buckets](../facts/iam.md#iam-resource-based-policy-examples)
iam-resource-based-policy-names-principal-same-or-other-account
  claim: A resource-based policy grants permissions to the principal named in the policy, and that principal can be in the same account as the resource or in another account.
  link: [grant permissions to the principal that is specified in the policy](../facts/iam.md#iam-resource-based-policy-names-principal-same-or-other-account)
  link: [same account as the resource or in other accounts](../facts/iam.md#iam-resource-based-policy-names-principal-same-or-other-account)
iam-resources-global-same-role-any-region
  claim: IAM resources are global, so the same IAM role can be used in any Region.
  scope: IAM resources.
  link: [IAM resources are global](../facts/iam.md#iam-resources-global-same-role-any-region)
  link: [the same role can be used in any Region](../facts/iam.md#iam-resources-global-same-role-any-region)
  say: IAM resources are global | one role works in every Region
iam-revoke-role-sessions-denies-credentials-issued-before
  claim: Revoking active sessions of a role attaches a new inline policy that denies all actions to credentials issued before the chosen time; those credentials become invalid, while users who assume the role afterward are not affected.
  scope: per IAM role; only credentials issued before the revocation time.
  link: [issued before the specified time become invalid](../facts/iam.md#iam-revoke-role-sessions-denies-credentials-issued-before)
  link: [denies all permissions to all actions](../facts/iam.md#iam-revoke-role-sessions-denies-credentials-issued-before)
  say: older credentials stop working | a deny-all inline policy
iam-revoke-sessions-token-issue-time-condition
  claim: The revoke policy denies all permissions when aws:TokenIssueTime is earlier than the chosen time; that key exists only for requests signed with temporary credentials, so an IAM user's long-term credentials are not affected.
  scope: policy condition aws:TokenIssueTime.
  link: [aws:TokenIssueTime](../facts/iam.md#iam-revoke-sessions-token-issue-time-condition)
  link: [does not affect requests that are signed with the long-term credentials](../facts/iam.md#iam-revoke-sessions-token-issue-time-condition)
  say: A-W-S token issue time | long-term credentials are not affected
iam-role-chaining-one-hour-limit-exceptions
  claim: Role chaining is using the credentials of one role to assume another; it limits the session to one hour regardless of the role's maximum session duration, and the limit does not apply to the first assumption from user credentials or to applications on EC2 instances using instance profiles.
  scope: role sessions obtained through role chaining; maximum.
  link: [using the credentials of one role to assume another](../facts/iam.md#iam-role-chaining-one-hour-limit-exceptions)
  link: [limits the session to one hour regardless of the role's maximum session duration](../facts/iam.md#iam-role-chaining-one-hour-limit-exceptions)
  link: [does not apply to the first assumption from user credentials or to applications on EC2 instances using instance profiles](../facts/iam.md#iam-role-chaining-one-hour-limit-exceptions)
iam-role-manager-what-it-is
  claim: IAM role manager is an optional account setting that automatically provisions the IAM roles that AWS services need to act on your behalf; it is available in select AWS service consoles and works by applying a role template, a definition of a role's trust policy and permissions for a service and use case. The roles it creates behave like any other role: you can view, edit or delete them.
  scope: per AWS account.
  link: [optional account setting that automatically provisions such roles](../facts/iam.md#iam-role-manager-what-it-is)
  say: an optional setting that creates service roles for you
iam-role-max-session-duration-setting
  claim: A role's maximum session duration setting can be from 1 hour to 12 hours; when no value is set the default maximum of 1 hour applies, and the setting does not limit sessions assumed by AWS services.
  scope: per IAM role; default; adjustable; does not limit sessions assumed by AWS services.
  link: [1 hour to 12 hours](../facts/iam.md#iam-role-max-session-duration-setting)
  link: [1 hour](../facts/iam.md#iam-role-max-session-duration-setting)
  say: one to twelve hours | one hour
iam-role-permissions-policy-defines-session-permissions
  claim: The permissions policy of the role being assumed determines what the temporary credentials returned by AssumeRole, AssumeRoleWithSAML and AssumeRoleWithWebIdentity can do; the trust policy says who may assume, the permissions policy says what the session may do.
  scope: per role session.
  link: [The permissions policy of the role being assumed determines what the temporary credentials](../facts/iam.md#iam-role-permissions-policy-defines-session-permissions)
  link: [the trust policy says who may assume, the permissions policy says what the session may do](../facts/iam.md#iam-role-permissions-policy-defines-session-permissions)
iam-role-trust-policy-names-who-can-assume
  claim: A role trust policy is the IAM resource-based policy type; in IAM roles, its Principal element specifies who can assume the role, and the principals you can specify include users, roles, accounts, and services.
  scope: per IAM role.
  link: [resource-based policy type is a role trust policy](../facts/iam.md#iam-role-trust-policy-names-who-can-assume)
  link: [who can assume the role](../facts/iam.md#iam-role-trust-policy-names-who-can-assume)
  link: [users, roles, accounts, and services](../facts/iam.md#iam-role-trust-policy-names-who-can-assume)
iam-role-trust-policy-only-resource-based-policy-in-iam
  claim: The only resource-based policy in IAM is the role trust policy; a role is both an identity and a resource, so it needs both a trust policy (who can assume it) and an identity-based permissions policy (what it can do).
  scope: per role.
  link: [only one type of resource-based policy called a role trust policy](../facts/iam.md#iam-role-trust-policy-only-resource-based-policy-in-iam)
  link: [attach both a trust policy and an identity-based policy to an IAM role](../facts/iam.md#iam-role-trust-policy-only-resource-based-policy-in-iam)
  link: [define which principal entities (accounts, users, roles, and federated users) can assume the role](../facts/iam.md#iam-role-trust-policy-only-resource-based-policy-in-iam)
iam-roles-anywhere-for-on-premises-and-hybrid-workloads
  claim: IAM Roles Anywhere extends IAM to on-premises and hybrid workloads: they get temporary credentials and use the same roles and policies as workloads on AWS, which requires a PKI that can issue certificates.
  link: [extends the capabilities of IAM to on-premises and hybrid cloud workloads](../facts/iam.md#iam-roles-anywhere-for-on-premises-and-hybrid-workloads)
  link: [requires PKI, the ability to issue and manage certificates](../facts/iam.md#iam-roles-anywhere-for-on-premises-and-hybrid-workloads)
iam-roles-rely-on-temporary-credentials-not-tied-to-user
  claim: An IAM role gives access through temporary security credentials; it has a set of permissions but is not associated with a specific user or group, and trusted entities such as identity providers or AWS services assume it. AWS calls relying on short-term credentials a security best practice.
  link: [relying on temporary security credentials](../facts/iam.md#iam-roles-rely-on-temporary-credentials-not-tied-to-user)
  link: [not associated with a specific user or group](../facts/iam.md#iam-roles-rely-on-temporary-credentials-not-tied-to-user)
  link: [relying on short-term credentials, a security best practice](../facts/iam.md#iam-roles-rely-on-temporary-credentials-not-tied-to-user)
iam-root-central-access-deletes-member-credentials
  claim: After root access is centralized, you can delete root user credentials (password, access keys, signing certificates, MFA) from member accounts; new accounts created in AWS Organizations then have no root user credentials by default, and member accounts cannot sign in as root or recover the root password.
  scope: per member account of an organization; after you centralize root access.
  link: [delete root user credentials from member accounts](../facts/iam.md#iam-root-central-access-deletes-member-credentials)
  link: [no root user credentials by default](../facts/iam.md#iam-root-central-access-deletes-member-credentials)
  say: delete root user credentials from member accounts | no root user credentials by default
iam-root-centralized-root-access-member-accounts
  claim: For accounts in AWS Organizations, AWS recommends removing root user credentials from member accounts: you can remove the root password, access keys and signing certificates and delete MFA, after which member accounts cannot sign in as root or recover the root password.
  scope: member accounts of an organization.
  link: [removing root user credentials from member accounts](../facts/iam.md#iam-root-centralized-root-access-member-accounts)
  link: [Member accounts can't sign in to their root user or perform password recovery for their root user](../facts/iam.md#iam-root-centralized-root-access-member-accounts)
iam-root-do-not-create-access-keys
  claim: AWS strongly recommends that you do not create access keys for the root user, because the root user has full access to all services and resources in the account, including billing information.
  scope: AWS account root user.
  link: [do not create access keys for the root user](../facts/iam.md#iam-root-do-not-create-access-keys)
  link: [full access to all services and resources in the account, including billing information](../facts/iam.md#iam-root-do-not-create-access-keys)
iam-root-do-not-share-credentials
  claim: Use root user credentials only for the tasks that require them, and do not share the root user password, MFA, access keys, CloudFront key pairs or signing certificates with anyone except those with a strict business need.
  scope: AWS account root user.
  link: [don’t share your root user password, MFA, access keys, CloudFront key pairs, or signing certificates with anyone](../facts/iam.md#iam-root-do-not-share-credentials)
iam-root-mfa-required-all-account-types
  claim: Every AWS account type (standalone, management and member accounts) requires MFA for its root user; a root user without MFA must register a device within 35 days of the first console sign-in attempt. The expansion to member accounts was announced in a post dated Jun 17, 2025, after management accounts in May 2024 and standalone accounts in June 2024.
  scope: per AWS account root user; if MFA is not already enabled.
  link: [All AWS account types (standalone, management, and member accounts)](../facts/iam.md#iam-root-mfa-required-all-account-types)
  link: [within 35 days](../facts/iam.md#iam-root-mfa-required-all-account-types)
  say: every account type: standalone, management and member | within thirty-five days of the first sign-in attempt
  changed: 2025-06-17: was requiring MFA for AWS Organizations management account root users in May 2024
iam-root-privileged-session-short-term-scoped
  claim: With centralized root access, the management account or a delegated administrator account for IAM performs some root-only tasks on member accounts through short-term privileged sessions whose temporary credentials are scoped to specific actions, without root sign-in on the member account.
  link: [short-term privileged sessions](../facts/iam.md#iam-root-privileged-session-short-term-scoped)
  link: [temporary credentials scoped to specific privileged actions](../facts/iam.md#iam-root-privileged-session-short-term-scoped)
iam-root-privileged-session-tasks
  claim: In a privileged root session you can delete a misconfigured S3 bucket policy, delete a misconfigured SQS queue policy, delete the root user credentials of a member account, and re-enable them.
  link: [delete a misconfigured Amazon S3 bucket policy](../facts/iam.md#iam-root-privileged-session-tasks)
iam-root-task-close-standalone-account
  claim: A standalone account that is not part of AWS Organizations needs root credentials to close the account; with AWS Organizations, member accounts can be closed centrally from the management account and delegated admin accounts.
  scope: closing an AWS account.
  link: [require root credentials to close the account](../facts/iam.md#iam-root-task-close-standalone-account)
  link: [close the member accounts centrally from the management account and delegated admin accounts](../facts/iam.md#iam-root-task-close-standalone-account)
iam-root-task-restore-admin-permissions
  claim: If the only IAM administrator accidentally revokes their own permissions, you sign in as the root user to edit policies and restore those permissions.
  scope: AWS account root user.
  link: [sign in as the root user to edit policies and restore those permissions](../facts/iam.md#iam-root-task-restore-admin-permissions)
iam-root-task-standalone-email-password-keys-only
  claim: In a standalone account, only changes to the root email address, root password and root access keys need root credentials; other settings such as account name, contact information, alternate contacts, payment currency preference and Regions do not.
  scope: standalone AWS account (not in AWS Organizations).
  link: [require root credentials to update the email address, root user password, and root user access keys](../facts/iam.md#iam-root-task-standalone-email-password-keys-only)
  link: [don't require root user credentials](../facts/iam.md#iam-root-task-standalone-email-password-keys-only)
iam-root-tasks-only-root-can-do
  claim: Some tasks can be performed only when you sign in as the root user; for example, if the only IAM administrator revokes their own permissions, you sign in as the root user to restore them.
  scope: AWS account root user.
  link: [can be performed only when you sign in as the root user](../facts/iam.md#iam-root-tasks-only-root-can-do)
  link: [sign in as the root user to restore them](../facts/iam.md#iam-root-tasks-only-root-can-do)
iam-root-user-limited-by-scps-and-rcps
  claim: In an account that is a member of an organization, the root user is affected by the SCPs and RCPs for that account, and a resource-based policy can name the root user as its principal.
  scope: root user of a member account in AWS Organizations; the account is a member of an organization.
  link: [the root user is affected by the SCPs and RCPs](../facts/iam.md#iam-root-user-limited-by-scps-and-rcps)
  link: [a resource-based policy can name the root user as its principal](../facts/iam.md#iam-root-user-limited-by-scps-and-rcps)
iam-root-user-most-privileged-sometimes-unconstrained
  claim: The root user is the most privileged identity in an account, with full administrative access to all resources, and in some cases it cannot be constrained by security policies.
  scope: per AWS account.
  link: [most privileged user in an AWS account](../facts/iam.md#iam-root-user-most-privileged-sometimes-unconstrained)
  link: [in some cases cannot be constrained by security policies](../facts/iam.md#iam-root-user-most-privileged-sometimes-unconstrained)
iam-root-user-no-identity-policies-or-boundary
  claim: You cannot attach identity-based policies to the root user, and you cannot set a permissions boundary for the root user.
  scope: AWS account root user.
  link: [cannot attach identity-based policies to the root user](../facts/iam.md#iam-root-user-no-identity-policies-or-boundary)
  link: [cannot set a permissions boundary for the root user](../facts/iam.md#iam-root-user-no-identity-policies-or-boundary)
iam-root-user-not-for-everyday-tasks-roles-instead
  claim: The root user must not be used for everyday tasks, even administrative ones; sign in as root only for the tasks that require it and do everything else through users assuming roles.
  scope: per AWS account.
  link: [must not be used for everyday tasks, even administrative ones](../facts/iam.md#iam-root-user-not-for-everyday-tasks-roles-instead)
  link: [Only log in as the root user to perform AWS tasks that require root user](../facts/iam.md#iam-root-user-not-for-everyday-tasks-roles-instead)
  link: [All other actions should be performed by other users assuming appropriate roles](../facts/iam.md#iam-root-user-not-for-everyday-tasks-roles-instead)
iam-s3-mfa-delete-root-only
  claim: Amazon S3 MFA Delete is for root account access only: it is enabled when you set the bucket versioning state, it cannot be applied to an IAM user, and it is managed separately from MFA-protected API access.
  scope: Amazon S3 MFA Delete.
  link: [MFA Delete feature for *root* account access (only)](../facts/iam.md#iam-s3-mfa-delete-root-only)
  link: [cannot be applied to an IAM user](../facts/iam.md#iam-s3-mfa-delete-root-only)
iam-scp-allow-is-a-filter-not-a-grant
  claim: An Allow statement in an SCP does not grant a user permission to do anything; SCPs act as filters that specify the maximum permissions, so even a user with AdministratorAccess is limited to what the SCP allows.
  scope: SCP Allow statements; maximum.
  link: [does not grant a user permission to do anything](../facts/iam.md#iam-scp-allow-is-a-filter-not-a-grant)
  link: [SCPs act as filters that specify the maximum permissions](../facts/iam.md#iam-scp-allow-is-a-filter-not-a-grant)
iam-scp-applies-to-member-root-user
  claim: An SCP restricts permissions for IAM users and roles in member accounts, including the member account's root user; SCPs don't affect users or roles in the management account, and service-linked roles can't be restricted by SCPs.
  scope: member accounts of an organization.
  link: [including the member account's root user](../facts/iam.md#iam-scp-applies-to-member-root-user)
  link: [restricts permissions for IAM users and roles in member accounts](../facts/iam.md#iam-scp-applies-to-member-root-user)
iam-scp-boundary-identity-all-must-allow
  claim: When an SCP, a permissions boundary and an identity-based policy all apply, the request is allowed only if all three policy types allow it; the effective permissions are the intersection of all three.
  scope: member account principal with a boundary.
  link: [allowed only if all three policy types allow it](../facts/iam.md#iam-scp-boundary-identity-all-must-allow)
  link: [the intersection of all three](../facts/iam.md#iam-scp-boundary-identity-all-must-allow)
iam-scp-condition-in-allow-and-deny
  claim: An SCP can specify a Condition element in allow and deny statements, and an SCP can use a NotAction element to exclude AWS services from the effect of the policy.
  scope: SCP policy language.
  link: [a Condition element in allow and deny statements](../facts/iam.md#iam-scp-condition-in-allow-and-deny)
  link: [NotAction element to exclude AWS services](../facts/iam.md#iam-scp-condition-in-allow-and-deny)
iam-scp-faq-almost-same-syntax-no-grant
  claim: SCPs use almost the same syntax as IAM policies, but SCPs do not grant permissions.
  scope: service control policies (SCPs).
  link: [use almost the same syntax](../facts/iam.md#iam-scp-faq-almost-same-syntax-no-grant)
  link: [SCPs don’t grant permissions](../facts/iam.md#iam-scp-faq-almost-same-syntax-no-grant)
iam-scp-faq-attach-at-root-ou-or-account
  claim: An Organizations policy can be attached to the organization root (all accounts), to an OU (all accounts in it, including nested OUs), or to an individual account.
  link: [to the root of your organization](../facts/iam.md#iam-scp-faq-attach-at-root-ou-or-account)
  link: [applies to all accounts in the OU including nested OUs](../facts/iam.md#iam-scp-faq-attach-at-root-ou-or-account)
iam-scp-faq-effective-permissions-intersection
  claim: In an account with an SCP applied, a principal's effective permissions are the intersection of what the SCP allows and what the principal's IAM permission policies grant.
  scope: principals in an account with an SCP applied.
  link: [the intersection between those allowed by the SCP and the permissions granted to the principal by IAM permission policies](../facts/iam.md#iam-scp-faq-effective-permissions-intersection)
iam-scp-faq-empty-scp-denies-all
  claim: Attaching an empty SCP to an account does not allow everything: it is equivalent to attaching a policy that denies all actions, because an empty policy behaves like a default deny.
  scope: an SCP with no statements attached to an account.
  link: [equivalent to attaching a policy that explicitly denies all actions](../facts/iam.md#iam-scp-faq-empty-scp-denies-all)
iam-scp-faq-intersection-example
  claim: Example from the Organizations FAQ: if an IAM user is allowed ec2 and sqs actions and the account's SCP allows ec2 and s3 actions, the user can perform only the EC2 actions.
  scope: IAM user in a member account with an SCP.
  link: [the resultant permission for the IAM user is "Allow": "ec2:* "](../facts/iam.md#iam-scp-faq-intersection-example)
iam-scp-faq-member-principals-cannot-change-scps
  claim: Principals in a member account, including that account's root user, cannot remove or change the SCPs applied to the account.
  scope: principals of a member account.
  link: [cannot remove or change SCPs that are applied to that account](../facts/iam.md#iam-scp-faq-member-principals-cannot-change-scps)
iam-scp-faq-policy-simulator-includes-scps
  claim: The IAM policy simulator can include the effects of SCPs, so you can use it in a member account to see how SCPs affect individual principals.
  link: [the IAM policy simulator can include the effects of SCPs](../facts/iam.md#iam-scp-faq-policy-simulator-includes-scps)
iam-scp-faq-targets-accounts-and-ous
  claim: SCPs allow or deny access to AWS services for individual member accounts of an organization or for groups of accounts in an organizational unit, and affect all IAM users and roles in them, including the member account's root user.
  scope: member accounts and OUs of an organization.
  link: [for individual AWS accounts with Organizations member accounts, or for groups of accounts within an organizational unit](../facts/iam.md#iam-scp-faq-targets-accounts-and-ous)
  link: [including the root user of the member account](../facts/iam.md#iam-scp-faq-targets-accounts-and-ous)
iam-scp-limits-permissions-does-not-grant
  claim: An SCP defines the maximum permissions for IAM users and roles in the accounts of an organization or OU; it limits what identity-based and resource-based policies grant, including to each member account root user, and it does not grant permissions.
  scope: per organization, OU or account; organization with all features enabled.
  link: [SCPs do not grant permissions](../facts/iam.md#iam-scp-limits-permissions-does-not-grant)
  link: [maximum permissions for IAM users and IAM roles](../facts/iam.md#iam-scp-limits-permissions-does-not-grant)
  link: [including each AWS account root user](../facts/iam.md#iam-scp-limits-permissions-does-not-grant)
iam-scp-needs-all-features-enabled
  claim: SCPs are not available when the organization has enabled only the consolidated billing features; the organization must have all features enabled, and the same rule applies to RCPs.
  scope: per organization.
  link: [not available when the organization has enabled only the consolidated billing features](../facts/iam.md#iam-scp-needs-all-features-enabled)
  link: [must have all features enabled](../facts/iam.md#iam-scp-needs-all-features-enabled)
iam-scp-never-grants-permissions
  claim: An SCP never grants permissions; it sets a permission guardrail on the maximum permissions of IAM users and roles, and the administrator must still attach identity-based or resource-based policies to grant access.
  scope: every SCP; maximum.
  link: [An SCP never grants permissions](../facts/iam.md#iam-scp-never-grants-permissions)
  link: [a permission guardrail on the maximum permissions of IAM users and roles](../facts/iam.md#iam-scp-never-grants-permissions)
  link: [the administrator must still attach identity-based or resource-based policies](../facts/iam.md#iam-scp-never-grants-permissions)
iam-scp-no-effect-on-management-account
  claim: SCPs do not affect users or roles in the management account; they affect only the member accounts, including member accounts that are delegated administrators.
  scope: the organization's management account.
  link: [do not affect users or roles in the management account](../facts/iam.md#iam-scp-no-effect-on-management-account)
  link: [affect only the member accounts](../facts/iam.md#iam-scp-no-effect-on-management-account)
iam-scp-no-effect-on-service-linked-roles
  claim: Service-linked roles cannot be restricted by SCPs; the same is true of RCPs, which do not apply to calls made by service-linked roles.
  scope: service-linked roles.
  link: [Service-linked roles cannot be restricted by SCPs](../facts/iam.md#iam-scp-no-effect-on-service-linked-roles)
  link: [do not apply to calls made by service-linked roles](../facts/iam.md#iam-scp-no-effect-on-service-linked-roles)
iam-scp-not-outside-principals-or-resource-policies
  claim: SCPs do not affect resource-based policies directly and do not affect users or roles from accounts outside the organization; a bucket policy that grants access to an outside account is not limited by the bucket owner's SCP.
  scope: principals outside the organization.
  link: [do not affect users or roles from accounts outside the organization](../facts/iam.md#iam-scp-not-outside-principals-or-resource-policies)
  link: [do not affect resource-based policies directly](../facts/iam.md#iam-scp-not-outside-principals-or-resource-policies)
iam-scp-rcp-attach-levels
  claim: SCPs and RCPs are organization policies that manage permissions at the organization root, OU or account level: AWS recommends SCPs as guardrails for all principals and RCPs as guardrails for resources across your organization.
  link: [at the AWS organization, organizational unit (OU), or account level](../facts/iam.md#iam-scp-rcp-attach-levels)
iam-scp-resource-element-allow-and-deny
  claim: In the SCP elements summary, the Resource element, which specifies the AWS resources that the SCP applies to, lists Allow and Deny as supported effects.
  scope: SCP policy language.
  link: [the Resource element](../facts/iam.md#iam-scp-resource-element-allow-and-deny)
  link: [Allow and Deny as supported effects](../facts/iam.md#iam-scp-resource-element-allow-and-deny)
iam-service-linked-role-fixed-trust-delete-resources-first
  claim: The linked service defines both the trust policy and the permissions policy of a service-linked role, and unless defined otherwise only that service can assume it; before you can delete a service-linked role you must first delete its related resources.
  scope: service-linked roles.
  link: [only that service can assume it](../facts/iam.md#iam-service-linked-role-fixed-trust-delete-resources-first)
  link: [you must first delete its related resources](../facts/iam.md#iam-service-linked-role-fixed-trust-delete-resources-first)
iam-service-linked-role-owned-by-service
  claim: A service-linked role is predefined by and owned by the linked service: an administrator can view but not edit its permissions, cannot modify its trust policy, and must delete the service's related resources before deleting the role.
  scope: service-linked roles.
  link: [can view but not edit its permissions](../facts/iam.md#iam-service-linked-role-owned-by-service)
  link: [cannot modify its trust policy](../facts/iam.md#iam-service-linked-role-owned-by-service)
  link: [must delete the service's related resources before deleting the role](../facts/iam.md#iam-service-linked-role-owned-by-service)
iam-service-role-vs-service-linked-role
  claim: A service role is a role that a service assumes to act on your behalf and that an IAM administrator can create, modify and delete; a service-linked role is linked directly to one service, is predefined by that service, and unless defined otherwise only that service can assume it; its permissions policy cannot be attached to any other IAM entity.
  scope: service roles.
  link: [an IAM administrator can create, modify and delete](../facts/iam.md#iam-service-role-vs-service-linked-role)
  link: [unless defined otherwise only that service can assume it](../facts/iam.md#iam-service-role-vs-service-linked-role)
iam-session-policy-limits-does-not-grant
  claim: A session policy is passed when a role or federated user session is created; it limits the permissions that the identity-based policies grant to that session and does not grant permissions.
  scope: per role or federated user session.
  link: [limit the permissions that the role or user's identity-based policies grant to the session](../facts/iam.md#iam-session-policy-limits-does-not-grant)
  link: [do not grant permissions](../facts/iam.md#iam-session-policy-limits-does-not-grant)
iam-shared-responsibility-customer-applies-permissions-with-iam
  claim: Under the shared responsibility model, for abstracted services such as S3 and DynamoDB AWS runs the infrastructure, operating system and platform, while the customer is responsible for managing and classifying their data, choosing encryption options and using IAM tools to apply the right permissions.
  scope: abstracted services such as Amazon S3 and Amazon DynamoDB.
  link: [using IAM tools to apply the appropriate permissions](../facts/iam.md#iam-shared-responsibility-customer-applies-permissions-with-iam)
  link: [managing their data (including encryption options), classifying their assets](../facts/iam.md#iam-shared-responsibility-customer-applies-permissions-with-iam)
  link: [AWS operates the infrastructure layer, the operating system, and platforms](../facts/iam.md#iam-shared-responsibility-customer-applies-permissions-with-iam)
iam-shared-responsibility-security-of-versus-in-the-cloud
  claim: AWS is responsible for security of the cloud (the hardware, software, networking and facilities that run AWS services); the customer is responsible for security in the cloud, and how much the customer must configure depends on the services they select.
  scope: shared responsibility model.
  link: [protecting the infrastructure that runs all of the services offered in the AWS Cloud](../facts/iam.md#iam-shared-responsibility-security-of-versus-in-the-cloud)
  link: [determined by the AWS Cloud services that a customer selects](../facts/iam.md#iam-shared-responsibility-security-of-versus-in-the-cloud)
iam-sra-access-analyzer-in-security-tooling-account
  claim: In the AWS Security Reference Architecture, IAM Access Analyzer, GuardDuty, AWS Config, Security Hub, CloudTrail organization trails and often Macie are delegated or aggregated to the Security Tooling account.
  link: [Security Tooling account](../facts/iam.md#iam-sra-access-analyzer-in-security-tooling-account)
iam-sts-interface-vpc-endpoints-private
  claim: An interface VPC endpoint (AWS PrivateLink) for IAM or AWS STS lets resources in a VPC reach the service privately without an internet gateway, NAT or VPN; IAM interface endpoints can only be created in the Region of the IAM control plane.
  scope: interface VPC endpoints for IAM and AWS STS.
  link: [without an internet gateway, NAT or VPN](../facts/iam.md#iam-sts-interface-vpc-endpoints-private)
  link: [can only be created in the Region of the IAM control plane](../facts/iam.md#iam-sts-interface-vpc-endpoints-private)
iam-tagging-api-getresources-no-iam-roles
  claim: The Resource Groups Tagging API GetResources operation does not currently support IAM users and roles; IAM users and roles can be used only in the TagResources and UntagResources operations.
  scope: Resource Groups Tagging API, IAM users and roles.
  link: [does not currently support IAM users and roles](../facts/iam.md#iam-tagging-api-getresources-no-iam-roles)
iam-temporary-delegation-what-it-is
  claim: IAM temporary delegation lets Amazon products and qualified AWS Partners request temporary, limited permissions in your account; after you approve, the provider acts on your behalf and the permissions expire automatically after the approved duration. Customers review and approve these requests but cannot create them.
  scope: per delegation request; Amazon products and qualified AWS Partners only.
  link: [temporary, limited access](../facts/iam.md#iam-temporary-delegation-what-it-is)
  say: temporary, limited access
  changed: 2025-11-19: was create persistent IAM roles for such tasks, or perform them manually
iam-use-cases-that-still-need-user-access-keys
  claim: AWS names use cases where IAM user long-term access keys are still the answer; they include workloads that cannot use IAM roles for temporary credentials (for example WordPress plugins) and tools that don't support IAM Identity Center, such as third-party AWS clients or vendors not hosted on AWS. The list is not exhaustive.
  scope: IAM users with long-term access keys; scenarios in which you need IAM users with programmatic access.
  link: [you can't use IAM roles to provide temporary credentials, such as for WordPress plugins](../facts/iam.md#iam-use-cases-that-still-need-user-access-keys)
  link: [third-party AWS clients or vendors that are not hosted on AWS](../facts/iam.md#iam-use-cases-that-still-need-user-access-keys)
iam-users-have-long-term-credentials-roles-do-not
  claim: An IAM user has long-term credentials (a password and access keys); a role has no standard long-term credentials and gives temporary security credentials for each role session. AWS recommends relying on temporary credentials instead of creating IAM users where possible.
  scope: IAM users and IAM roles.
  link: [does not have standard long-term credentials, such as a password or access keys](../facts/iam.md#iam-users-have-long-term-credentials-roles-do-not)
  link: [IAM users have long-term credentials such as passwords and access keys](../facts/iam.md#iam-users-have-long-term-credentials-roles-do-not)
  link: [identities with long-term credentials](../facts/iam.md#iam-users-have-long-term-credentials-roles-do-not)
iam-vpc-endpoint-policy-extra-boundary
  claim: A VPC endpoint policy is attached to a VPC endpoint to control which principals can use it and which resources can be reached through it; it acts as an additional access boundary for traffic through the endpoint.
  link: [an additional access boundary scoped to traffic that traverses the endpoint](../facts/iam.md#iam-vpc-endpoint-policy-extra-boundary)
sts-assumerole-duration-default
  claim: When an AssumeRole call omits DurationSeconds, the role session lasts 3600 seconds (one hour).
  scope: per AssumeRole call; default; adjustable; DurationSeconds not specified.
  link: [3600 seconds](../facts/sts.md#sts-assumerole-duration-default)
  link: [one hour](../facts/sts.md#sts-assumerole-duration-default)
  say: thirty-six hundred seconds | one hour
sts-assumerole-duration-range
  claim: An AssumeRole call can request a session from 900 seconds (15 minutes) up to the role's maximum session duration setting, and that setting itself can be from 1 hour to 12 hours.
  scope: per AssumeRole call; maximum; not adjustable; bounded by the role's maximum session duration setting.
  link: [900 seconds (15 minutes)](../facts/sts.md#sts-assumerole-duration-range)
  link: [12 hours](../facts/sts.md#sts-assumerole-duration-range)
  say: nine hundred seconds, fifteen minutes | twelve hours
sts-assumerolewithsaml-duration
  claim: AssumeRoleWithSAML credentials last one hour by default; DurationSeconds can request from 900 seconds (15 minutes) up to the role's maximum session duration, and the session ends at the SAML response's SessionNotOnOrAfter time if that is sooner.
  scope: per AssumeRoleWithSAML call; default; adjustable; whichever is shorter: DurationSeconds or the SAML SessionNotOnOrAfter value.
  link: [one hour](../facts/sts.md#sts-assumerolewithsaml-duration)
  link: [900 seconds (15 minutes)](../facts/sts.md#sts-assumerolewithsaml-duration)
  say: one hour | nine hundred seconds, fifteen minutes
sts-assumerolewithwebidentity-duration
  claim: AssumeRoleWithWebIdentity credentials last one hour by default; DurationSeconds can request from 900 seconds (15 minutes) up to the role's maximum session duration setting, which can be from 1 hour to 12 hours.
  scope: per AssumeRoleWithWebIdentity call; default; adjustable; bounded by the role's maximum session duration setting.
  link: [one hour](../facts/sts.md#sts-assumerolewithwebidentity-duration)
  link: [900 seconds (15 minutes)](../facts/sts.md#sts-assumerolewithwebidentity-duration)
  link: [12 hours](../facts/sts.md#sts-assumerolewithwebidentity-duration)
  say: one hour | nine hundred seconds, fifteen minutes | twelve hours
sts-assumeroot-callers
  claim: AssumeRoot returns short-term credentials for privileged tasks on a member account; only credentials from the management account or a delegated administrator account for IAM can call it, and root user credentials cannot make the call.
  scope: sts:AssumeRoot (centralized root access); centralized root access enabled in AWS Organizations.
  link: [the management account or a delegated administrator account for IAM](../facts/sts.md#sts-assumeroot-callers)
  link: [root user credentials cannot make the call](../facts/sts.md#sts-assumeroot-callers)
sts-assumeroot-max-900-seconds
  claim: An AssumeRoot privileged session lasts from 0 seconds up to a maximum of 900 seconds (15 minutes), which is also the default; a higher value makes the call fail.
  scope: per AssumeRoot session; maximum; not adjustable.
  link: [900 seconds (15 minutes)](../facts/sts.md#sts-assumeroot-max-900-seconds)
  link: [a higher value makes the call fail](../facts/sts.md#sts-assumeroot-max-900-seconds)
  say: nine hundred seconds, fifteen minutes
sts-change-global-endpoint-local-2025-04
  claim: On 2025-04-18 AWS STS began serving requests to the global endpoint (sts.amazonaws.com) in the same Region as the calling workload, for Regions enabled by default; before, all global endpoint requests were served from US East (N. Virginia).
  scope: per STS request to sts.amazonaws.com; Regions enabled by default.
  link: [2025-04-18](../facts/sts.md#sts-change-global-endpoint-local-2025-04)
  say: April eighteenth, twenty twenty-five
  changed: 2025-04-18: was Previously, all requests to the STS global endpoint were served from the US East (N. Virginia) Region.
sts-compare-assumerole-row
  claim: AssumeRole can be called by an IAM user or by an IAM role with existing temporary credentials; its credentials last from 15 m up to the role's maximum session duration setting with 1 hr as the default, it supports MFA and session policies, and its credentials cannot call GetFederationToken or GetSessionToken.
  scope: per AssumeRole session.
  link: [15 m](../facts/sts.md#sts-compare-assumerole-row)
  link: [1 hr](../facts/sts.md#sts-compare-assumerole-row)
  link: [Cannot call `GetFederationToken` or `GetSessionToken`](../facts/sts.md#sts-compare-assumerole-row)
  link: [an IAM user or by an IAM role with existing temporary credentials](../facts/sts.md#sts-compare-assumerole-row)
  say: fifteen minutes | one hour | cannot call get federation token or get session token | an IAM user, or an IAM role that already has temporary credentials
sts-compare-getfederationtoken-row
  claim: GetFederationToken can be called by an IAM user (15 m to 36 hr, default 12 hr) or by the root user (15 m to 1 hr, default 1 hr); it has no MFA support, supports session policies, cannot call IAM operations through the CLI or API, and can call no STS operation except GetCallerIdentity.
  scope: per GetFederationToken session; console sessions are not limited in IAM operations.
  link: [36 hr](../facts/sts.md#sts-compare-getfederationtoken-row)
  link: [12 hr](../facts/sts.md#sts-compare-getfederationtoken-row)
  link: [1 hr](../facts/sts.md#sts-compare-getfederationtoken-row)
  say: thirty-six hours | twelve hours | one hour
sts-compare-getsessiontoken-row
  claim: GetSessionToken can be called by an IAM user (15 m to 36 hr, default 12 hr) or by the root user (15 m to 1 hr, default 1 hr); it supports MFA but not session policies, its credentials cannot call IAM API operations unless MFA information is included, can call no STS operation except AssumeRole or GetCallerIdentity, and cannot be used for SSO to the console.
  scope: per GetSessionToken session.
  link: [36 hr](../facts/sts.md#sts-compare-getsessiontoken-row)
  link: [12 hr](../facts/sts.md#sts-compare-getsessiontoken-row)
  link: [1 hr](../facts/sts.md#sts-compare-getsessiontoken-row)
  link: [unless MFA information is included with the request](../facts/sts.md#sts-compare-getsessiontoken-row)
  say: thirty-six hours | twelve hours | one hour | only with MFA information
sts-condition-keys-rolesessionname-sourceidentity
  claim: In a role trust policy, the sts:RoleSessionName condition key can require users to provide a specific session name when they assume a role, and the sts:SourceIdentity key can require them to set a specific source identity; an identity needs permission for the sts:SetSourceIdentity action to set a source identity.
  scope: role trust policies (AWS STS condition keys).
  link: [require that your users provide a specific session name when they assume a role](../facts/sts.md#sts-condition-keys-rolesessionname-sourceidentity)
  link: [require that your users set a specific source identity when they assume a role](../facts/sts.md#sts-condition-keys-rolesessionname-sourceidentity)
  link: [sts:SetSourceIdentity](../facts/sts.md#sts-condition-keys-rolesessionname-sourceidentity)
sts-credentials-include-expiration
  claim: The Credentials object returned by STS holds an access key ID that identifies the temporary security credentials, a secret access key that can be used to sign requests, a session token that users must pass to the service API to use the temporary credentials, and an Expiration: the date on which the current credentials expire.
  link: [The date on which the current credentials expire](../facts/sts.md#sts-credentials-include-expiration)
sts-credentials-work-globally
  claim: Temporary credentials from AWS STS work globally, no matter which Region they come from.
  scope: AWS STS temporary credentials.
  link: [work globally](../facts/sts.md#sts-credentials-work-globally)
  link: [no matter which Region they come from](../facts/sts.md#sts-credentials-work-globally)
sts-decode-authorization-message
  claim: Some AWS operations return an encoded authorization message with a 403 error; the message is encoded because it can hold privileged details, and a user needs permission for sts:DecodeAuthorizationMessage to decode it, which shows whether the deny was explicit or the absence of an allow.
  scope: sts:DecodeAuthorizationMessage.
  link: [sts:DecodeAuthorizationMessage](../facts/sts.md#sts-decode-authorization-message)
  link: [it can hold privileged details](../facts/sts.md#sts-decode-authorization-message)
sts-dual-stack-regional-endpoints
  claim: AWS STS provides dual-stack Regional endpoints that accept IPv4 and IPv6 clients, also reachable privately from a VPC through AWS PrivateLink.
  scope: per Region (STS Regional endpoints).
  link: [dual-stack regional endpoints](../facts/sts.md#sts-dual-stack-regional-endpoints)
  say: dual-stack Regional endpoints
sts-durationseconds-above-max-fails
  claim: With AssumeRole* APIs or assume-role* CLI commands, DurationSeconds can be from 900 seconds (15 minutes) up to the role's Maximum session duration setting; a higher value makes the operation fail, for example 12 hours requested against a 6-hour maximum.
  scope: per role session requested with AssumeRole*; maximum; not adjustable.
  link: [900 seconds (15 minutes)](../facts/sts.md#sts-durationseconds-above-max-fails)
  link: [the operation fails](../facts/sts.md#sts-durationseconds-above-max-fails)
sts-external-id-length
  claim: The external ID a third party uses to assume a role must be from 2 to 1,224 characters and alphanumeric without white space.
  scope: per external ID value; maximum; not adjustable; alphanumeric without white space.
  link: [a minimum of 2 characters and a maximum of 1,224 characters](../facts/sts.md#sts-external-id-length)
  say: two to one thousand two hundred twenty-four characters
sts-getcalleridentity-no-permissions-required
  claim: GetCallerIdentity needs no permissions: even if a policy explicitly denies sts:GetCallerIdentity, you can still call it, because the same information is returned when access is denied.
  scope: sts:GetCallerIdentity.
  link: [No permissions are required to perform this operation](../facts/sts.md#sts-getcalleridentity-no-permissions-required)
sts-getfederationtoken-duration
  claim: GetFederationToken sessions can last from 900 seconds (15 minutes) to 129,600 seconds (36 hours), with 43,200 seconds (12 hours) as the default; with root user credentials the session is limited to 3,600 seconds (one hour).
  scope: per GetFederationToken call; default; adjustable; root user credentials are limited to one hour.
  link: [900 seconds (15 minutes)](../facts/sts.md#sts-getfederationtoken-duration)
  link: [129,600 seconds (36 hours)](../facts/sts.md#sts-getfederationtoken-duration)
  link: [43,200 seconds (12 hours)](../facts/sts.md#sts-getfederationtoken-duration)
  link: [3,600 seconds (one hour)](../facts/sts.md#sts-getfederationtoken-duration)
  say: nine hundred seconds, fifteen minutes | thirty-six hours | twelve hours | one hour for the root user
sts-getfederationtoken-long-term-user-credentials
  claim: GetFederationToken must be called with the long-term credentials of an IAM user, so it suits server-based applications such as a custom identity broker where those credentials can be safeguarded; for mobile or browser apps AWS recommends Amazon Cognito or AssumeRoleWithWebIdentity.
  scope: sts:GetFederationToken.
  link: [the long-term credentials of an IAM user](../facts/sts.md#sts-getfederationtoken-long-term-user-credentials)
  link: [Amazon Cognito or AssumeRoleWithWebIdentity](../facts/sts.md#sts-getfederationtoken-long-term-user-credentials)
sts-getfederationtoken-session-limits
  claim: Credentials from GetFederationToken cannot call IAM operations through the CLI or API (console sessions excepted) and cannot call AWS STS operations except GetCallerIdentity; without a session policy the federated user session has no permissions.
  scope: sts:GetFederationToken session.
  link: [cannot call IAM operations through the CLI or API](../facts/sts.md#sts-getfederationtoken-session-limits)
  link: [without a session policy the federated user session has no permissions](../facts/sts.md#sts-getfederationtoken-session-limits)
sts-getsessiontoken-duration-iam-user
  claim: GetSessionToken for an IAM user accepts durations from 900 seconds (15 minutes) to 129,600 seconds (36 hours), with 43,200 seconds (12 hours) as the default.
  scope: per GetSessionToken call by an IAM user; default; adjustable.
  link: [900 seconds (15 minutes)](../facts/sts.md#sts-getsessiontoken-duration-iam-user)
  link: [129,600 seconds (36 hours)](../facts/sts.md#sts-getsessiontoken-duration-iam-user)
  link: [43,200 seconds (12 hours)](../facts/sts.md#sts-getsessiontoken-duration-iam-user)
  say: nine hundred seconds, fifteen minutes | thirty-six hours | twelve hours
sts-getsessiontoken-root-max-one-hour
  claim: When GetSessionToken is called with root user credentials, the session is limited to a maximum of 3,600 seconds (one hour); a longer requested duration defaults to one hour.
  scope: per GetSessionToken call by the root user; maximum; not adjustable; root user credentials.
  link: [3,600 seconds (one hour)](../facts/sts.md#sts-getsessiontoken-root-max-one-hour)
  say: one hour
sts-global-endpoint-requestedregion-us-east-1
  claim: Requests made to the AWS STS global endpoint carry the value us-east-1 for the aws:RequestedRegion condition key, whichever Region served the request.
  scope: AWS STS global endpoint.
  link: [us-east-1](../facts/sts.md#sts-global-endpoint-requestedregion-us-east-1)
  link: [whichever Region served the request](../facts/sts.md#sts-global-endpoint-requestedregion-us-east-1)
sts-global-endpoint-separate-rps-quota
  claim: Requests handled by the AWS STS global endpoint do not share a requests per second quota with Regional STS endpoints.
  scope: per account, AWS STS global endpoint versus Regional endpoints; fixed; not adjustable; Regions enabled by default.
  link: [do not share a requests per second quota](../facts/sts.md#sts-global-endpoint-separate-rps-quota)
  say: they do not share a quota
sts-global-endpoint-served-in-local-region
  claim: Requests to the AWS STS global endpoint (sts.amazonaws.com) are served in the same Region where the request originates when that Region is enabled by default and the Amazon DNS server resolves the name; requests from opt-in Regions or resolved by another DNS resolver are still served in US East (N. Virginia). AWS still recommends the Regional STS endpoints.
  scope: per STS request to sts.amazonaws.com; Region enabled by default and Amazon DNS server.
  link: [served in the same Region where the request originates](../facts/sts.md#sts-global-endpoint-served-in-local-region)
  link: [opt-in Regions](../facts/sts.md#sts-global-endpoint-served-in-local-region)
  say: in the Region where the request starts | opt-in Regions
  changed: 2025-04-18: was Previously, all requests to the AWS STS global endpoint were served by a single AWS Region, US East (N. Virginia).
sts-regional-endpoint-tokens-valid-in-all-regions
  claim: Session tokens from Regional AWS STS endpoints are valid in all AWS Regions, while session tokens from the global STS endpoint are valid only in Regions that are enabled by default.
  scope: AWS STS session tokens; global endpoint tokens can be made valid in all Regions by changing their Region compatibility.
  link: [valid in all AWS Regions](../facts/sts.md#sts-regional-endpoint-tokens-valid-in-all-regions)
  link: [valid only in AWS Regions that are enabled by default](../facts/sts.md#sts-regional-endpoint-tokens-valid-in-all-regions)
  say: valid in every Region | only in default Regions
sts-regional-endpoints-recommended
  claim: AWS recommends Regional STS endpoints over the global endpoint to reduce latency, build in redundancy and increase session token validity.
  scope: AWS STS endpoints.
  link: [reduce latency, build in redundancy, and increase session token validity](../facts/sts.md#sts-regional-endpoints-recommended)
  link: [Regional AWS Security Token Service (AWS STS) endpoints instead of the global endpoint](../facts/sts.md#sts-regional-endpoints-recommended)
  say: lower latency, redundancy, and wider token validity | Regional STS endpoints
sts-request-quota-600-rps
  claim: For AWS STS requests made using AWS credentials, the default request quota is 600 requests per second, per account, per Region; requests by AWS service principals do not consume it, and for a cross-account AssumeRole only the account making the request has its quota consumed.
  scope: per account, per Region; default; adjustable; requests made using AWS credentials; service principals do not consume it.
  link: [600 requests per second](../facts/sts.md#sts-request-quota-600-rps)
  say: six hundred requests per second
sts-role-chaining-definition
  claim: Role chaining is using a role to assume a second role; it can be done by switching roles in the console, with the CLI or with the API, and transitive session tags are passed to every later session in the chain.
  link: [use a role to assume a second role](../facts/sts.md#sts-role-chaining-definition)
  link: [transitive session tags are passed to all subsequent sessions in a role chain](../facts/sts.md#sts-role-chaining-definition)
  say: use a role to assume a second role | transitive session tags pass down the chain
sts-role-chaining-max-one-hour
  claim: Role chaining (using one role's credentials to assume a second role) limits the session to a maximum of one hour regardless of the roles' maximum session duration settings; a DurationSeconds above one hour makes the operation fail.
  scope: per role session obtained through role chaining; maximum; applies regardless of the maximum session duration configured for individual roles.
  link: [one hour](../facts/sts.md#sts-role-chaining-max-one-hour)
  link: [the operation fails](../facts/sts.md#sts-role-chaining-max-one-hour)
  say: one hour | the operation fails
sts-saml-and-web-identity-callers-no-mfa
  claim: AssumeRoleWithSAML and AssumeRoleWithWebIdentity can be called by any user who presents a SAML authentication response or an OIDC-compliant JWT from a known identity provider; both are unsigned calls, not signed with AWS credentials, and the calls do not support MFA because the user is authenticated by an external provider.
  scope: AssumeRoleWithSAML and AssumeRoleWithWebIdentity.
  link: [any user who presents a SAML authentication response or an OIDC-compliant JWT](../facts/sts.md#sts-saml-and-web-identity-callers-no-mfa)
  link: [not signed with AWS credentials](../facts/sts.md#sts-saml-and-web-identity-callers-no-mfa)
  link: [do not support MFA](../facts/sts.md#sts-saml-and-web-identity-callers-no-mfa)
sts-service-principal-requests-do-not-consume-quota
  claim: STS requests made by AWS service principals, such as a service assuming a role for its own use, do not consume the account's STS requests per second quota.
  scope: per account, per Region; fixed; not adjustable; requests by AWS service principals.
  link: [do not consume STS request per second quota](../facts/sts.md#sts-service-principal-requests-do-not-consume-quota)
  say: they do not count against the quota
sts-session-policy-intersection
  claim: A session's permissions are the intersection of the identity-based policies of the user or role that created the session and the session policies, and permissions can also come from a resource-based policy; a session policy cannot grant more permissions than the identity-based policy of the role being assumed allows, and an explicit deny in any of these policies overrides the allow.
  scope: per role session.
  link: [the intersection of the identity-based policies](../facts/sts.md#sts-session-policy-intersection)
  link: [An explicit deny in any of these policies overrides the allow](../facts/sts.md#sts-session-policy-intersection)
  say: the intersection with the identity-based policy | an explicit deny anywhere overrides the allow
sts-session-policy-limits
  claim: An AssumeRole, AssumeRoleWithSAML or AssumeRoleWithWebIdentity call can pass one inline JSON session policy and up to 10 managed policy ARNs, and the plaintext of inline and managed session policies together cannot exceed 2,048 characters.
  scope: per AssumeRole, AssumeRoleWithSAML or AssumeRoleWithWebIdentity request; maximum; not adjustable; inline and managed session policies combined.
  link: [up to 10 managed policy](../facts/sts.md#sts-session-policy-limits)
  link: [2,048 characters](../facts/sts.md#sts-session-policy-limits)
  say: up to ten managed policy ARNs | two thousand forty-eight characters
sts-session-tags-transitive-for-role-chaining
  claim: Session tags are key-value attributes passed when you assume a role or federate a user; they are valid only for the current session, and by default STS does not pass them to later role sessions unless you set them as transitive, which persist during role chaining.
  scope: AWS STS session tags; default; role chaining.
  link: [valid only for the current session](../facts/sts.md#sts-session-tags-transitive-for-role-chaining)
  link: [unless you set them as transitive](../facts/sts.md#sts-session-tags-transitive-for-role-chaining)
sts-source-identity-persists-and-cannot-change
  claim: A source identity is a custom string that identifies the person or application using a role, and it is stored as the source identity in AWS CloudTrail; once set, it is present in requests for any AWS action taken during the role session, it persists when a role is used to assume another role through the AWS CLI or AWS API (role chaining), and it cannot be changed during the role session. AWS recommends it to control the identity that assumes a role and to find in CloudTrail who used the role.
  scope: AWS STS source identity.
  link: [persists when a role is used to assume another role](../facts/sts.md#sts-source-identity-persists-and-cannot-change)
  link: [cannot be changed during the role session](../facts/sts.md#sts-source-identity-persists-and-cannot-change)
sts-temporary-credentials-advantages
  claim: Temporary credentials mean you do not have to distribute or embed long-term credentials in an application, you can give users access to your AWS resources without defining an AWS identity for them, and you do not have to update or revoke them because they expire (they have a limited lifetime); they are the basis for roles and identity federation.
  scope: AWS STS credentials.
  link: [do not have to distribute or embed long-term credentials in an application](../facts/sts.md#sts-temporary-credentials-advantages)
  link: [the basis for roles and identity federation](../facts/sts.md#sts-temporary-credentials-advantages)
  link: [do not have to update or revoke them because they expire](../facts/sts.md#sts-temporary-credentials-advantages)
sts-temporary-credentials-cannot-be-revoked-permissions-can-change
  claim: Temporary security credentials stay valid until they expire and cannot be revoked, but their permissions are evaluated on every request, so changing their access rights has the effect of revoking them.
  scope: temporary security credentials issued by AWS STS.
  link: [cannot be revoked](../facts/sts.md#sts-temporary-credentials-cannot-be-revoked-permissions-can-change)
  link: [evaluated each time a request is made](../facts/sts.md#sts-temporary-credentials-cannot-be-revoked-permissions-can-change)
  say: cannot be revoked | permissions are checked on every request
sts-temporary-credentials-expire-not-stored
  claim: Temporary security credentials are short-term and generated dynamically on request rather than stored with the user; after they expire AWS no longer accepts any API request made with them, and they cannot be reused.
  scope: every AWS STS credential.
  link: [generated dynamically on request rather than stored with the user](../facts/sts.md#sts-temporary-credentials-expire-not-stored)
  link: [after they expire AWS no longer accepts any API request made with them](../facts/sts.md#sts-temporary-credentials-expire-not-stored)
  link: [they cannot be reused](../facts/sts.md#sts-temporary-credentials-expire-not-stored)
  link: [generated dynamically and provided to the user](../facts/sts.md#sts-temporary-credentials-expire-not-stored)
sts-temporary-credentials-include-session-token
  claim: A set of temporary security credentials is an access key ID, a secret access key and a session token; every call made with them must include the session token, and they cannot be extended or refreshed beyond their original interval.
  scope: every AWS STS credential.
  link: [an access key ID, a secret access key and a session token](../facts/sts.md#sts-temporary-credentials-include-session-token)
  link: [every call made with them must include the session token](../facts/sts.md#sts-temporary-credentials-include-session-token)
  link: [cannot be extended or refreshed beyond their original interval](../facts/sts.md#sts-temporary-credentials-include-session-token)
sts-vpc-endpoint-policy-default-and-no-grant
  claim: An endpoint policy on an STS interface VPC endpoint controls which principals can use it and which STS actions; without a policy the default allows all STS actions for all principals, and endpoint policies never grant permissions on their own, so both the endpoint policy and the caller's policies must allow the request.
  scope: AWS STS interface VPC endpoint policies; default.
  link: [the default allows all STS actions for all principals](../facts/sts.md#sts-vpc-endpoint-policy-default-and-no-grant)
  link: [both the endpoint policy and the caller's policies must allow the request](../facts/sts.md#sts-vpc-endpoint-policy-default-and-no-grant)
