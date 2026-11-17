facts card: 8 facts
iam-condition-key-principalorgid
  claim: The aws:PrincipalOrgID key compares the organization of the requesting principal with an organization ID in the policy; it is an alternative to listing every account ID of the organization in a resource-based policy, and when you add and remove accounts, policies that use the key automatically include the correct accounts without manual updates.
  scope: global condition key aws:PrincipalOrgID; the principal is a member of an organization.
  link: [aws:PrincipalOrgID](../facts/iam.md#iam-condition-key-principalorgid)
  link: [automatically include the correct accounts](../facts/iam.md#iam-condition-key-principalorgid)
iam-root-centralized-root-access-member-accounts
  claim: For accounts in AWS Organizations, AWS recommends removing root user credentials from member accounts: you can remove the root password, access keys and signing certificates and delete MFA, after which member accounts cannot sign in as root or recover the root password.
  scope: member accounts of an organization.
  link: [removing root user credentials from member accounts](../facts/iam.md#iam-root-centralized-root-access-member-accounts)
  link: [Member accounts can't sign in to their root user or perform password recovery for their root user](../facts/iam.md#iam-root-centralized-root-access-member-accounts)
iam-change-scp-quotas-doubled-2026-05
  claim: On 2026-05-15 AWS Organizations raised the maximum number of SCPs attached to one root, OU or account from 5 to 10, and the maximum SCP size from 5,120 to 10,240 characters; RCPs stay at 5 per root, OU or account.
  scope: per root, OU or account (directly attached policies).
  link: [from 5 to 10](../facts/iam.md#iam-change-scp-quotas-doubled-2026-05)
  link: [from 5,120 to 10,240 characters](../facts/iam.md#iam-change-scp-quotas-doubled-2026-05)
  say: from five to ten | from five thousand one hundred twenty to ten thousand two hundred forty characters
  changed: 2026-05-15: was 5
iam-change-rcps-launched-2024-11
  claim: On 2024-11-13 AWS Organizations added resource control policies (RCPs), which set the maximum permissions for resources in the accounts of an organization or OU; an explicit deny in an RCP overrides an allow, like an explicit deny in an SCP.
  scope: per organization, OU or account.
  link: [2024-11-13](../facts/iam.md#iam-change-rcps-launched-2024-11)
  link: [maximum permissions for resources](../facts/iam.md#iam-change-rcps-launched-2024-11)
  say: November thirteenth, twenty twenty-four | the maximum permissions for resources
iam-data-perimeter-resource-scp-resourceorgid
  claim: The resource perimeter (your identities can access only trusted resources) is applied on identities with an SCP; the aws:ResourceOrgID key lets an identity-based policy apply rules to all resources in an organization.
  scope: data perimeters in AWS Organizations.
  link: [applied on identities with an SCP](../facts/iam.md#iam-data-perimeter-resource-scp-resourceorgid)
  link: [aws:ResourceOrgID](../facts/iam.md#iam-data-perimeter-resource-scp-resourceorgid)
iam-data-perimeter-identity-rcp-principalorgid
  claim: The identity perimeter (only trusted identities can access my resources) is applied on resources with an RCP, using condition keys such as aws:PrincipalOrgID and aws:PrincipalAccount.
  scope: data perimeters in AWS Organizations.
  link: [applied on resources with an RCP](../facts/iam.md#iam-data-perimeter-identity-rcp-principalorgid)
  link: [aws:PrincipalOrgID and aws:PrincipalAccount](../facts/iam.md#iam-data-perimeter-identity-rcp-principalorgid)
iam-idc-accounts-need-organizations-all-features
  claim: IAM Identity Center can manage single sign-on to any AWS account managed with AWS Organizations, and you need to enable all features in the organization to do so.
  scope: AWS accounts managed with IAM Identity Center.
  link: [any AWS account managed using AWS Organizations](../facts/iam.md#iam-idc-accounts-need-organizations-all-features)
  link: [enable all features in your organizations](../facts/iam.md#iam-idc-accounts-need-organizations-all-features)
iam-scp-needs-all-features-enabled
  claim: SCPs are not available when the organization has enabled only the consolidated billing features; the organization must have all features enabled, and the same rule applies to RCPs.
  scope: per organization.
  link: [not available when the organization has enabled only the consolidated billing features](../facts/iam.md#iam-scp-needs-all-features-enabled)
  link: [must have all features enabled](../facts/iam.md#iam-scp-needs-all-features-enabled)
