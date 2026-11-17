import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
MC, OP, CT = D + "manage-cross-account", "docs/organizations/latest/userguide/orgs_manage_policies_backup", "docs/controltower/latest/userguide/backup"
f = []
O = dict(service="organizations")
f.append(F("organizations-backup-policy-attach-root-ou-account-inheritance", "behavior",
 "A backup policy in AWS Organizations is a JSON document that you can attach to the root, an organizational unit or an account; Organizations combines the policies by inheritance into an effective backup policy for each account.",
 "Where can you attach a backup policy and how does an account get its effective policy?",
 ["attach a backup policy to any of the elements in your organization's structure", "effective backup policy"],
 [E(OP, "Backup policies in AWS Organizations combine all of those pieces into JSON text documents. You can attach a backup policy to any of the elements in your organization's structure, such as the root, organizational units (OUs), and individual accounts. Organizations applies inheritance rules to combine the policies in the organization's root, any parent OUs, or attached to the account. This results in an effective backup policy for each account.")],
 scope="AWS Organizations backup policies", tier0=True, bullets=["1.3.S1"], **O))
f.append(F("organizations-backup-policy-tags-and-iam-role-required", "behavior",
 "A backup plan in a backup policy is applied to groups of resources identified by tags, and the policy must identify an IAM role that gives AWS Backup permission to perform the backup on your behalf.",
 "What does a backup policy need to identify besides the plan rules?",
 ["groups of AWS resources identified by using tags", "grants AWS Backup permission to perform the backup operation"],
 [E(OP, "You can then apply a backup plan to groups of AWS resources identified by using tags. You must also identify an AWS Identity and Access Management (IAM) role that grants AWS Backup permission to perform the backup operation on your behalf.")],
 scope="AWS Organizations backup policies", bullets=["1.3.S1", "4.3.S1"], **O))
f.append(F("organizations-backup-policy-ou-override-of-root-default", "capability",
 "You can set a default in a backup policy at the organization root, such as backup frequency, and attach backup policies to OUs that override the default for that OU.",
 "Can an OU use a different backup frequency than the organization-wide backup policy?",
 ["attach a backup policy to OUs that override the backup frequency", "default backup frequency"],
 [E(OP, "For example, you can specify in a policy attached to the organization's root that all Amazon DynamoDB tables must be backed up. That policy can include a default backup frequency. You can then attach a backup policy to OUs that override the backup frequency according to the requirements of each OU.")],
 scope="AWS Organizations backup policies", tier0=True, bullets=["1.3.S1", "4.3.S1"], **O))
f.append(F("organizations-backup-policy-incomplete-effective-policy-not-valid", "restriction",
 "If the effective backup policy of an account does not have all required elements, AWS Backup considers the policy not valid and does not back up the affected resources.",
 "What happens if the effective backup policy of an account is incomplete?",
 ["considers the policy not valid", "does not back up the affected resources"],
 [E(OP, "When Organizations combines all of the policies for an account by using inheritance rules, the resulting effective policy must have all the required elements. Otherwise, AWS Backup considers the policy not valid and does not back up the affected resources.")],
 scope="effective backup policy of an account", bullets=["1.3.S1"], **O))
f.append(F("organizations-backup-policy-management-account-sees-all-jobs-with-trusted-access", "behavior",
 "A user in a member account sees the status and errors of the backup jobs in that account, and if trusted service access with AWS Backup is enabled, a user in the management account sees the status and errors of all backup jobs in the organization.",
 "Who can see backup job status for policy-created plans across an organization?",
 ["a user in the organization's management account can see the status and errors for all backup jobs", "trusted service access with AWS Backup"],
 [E(OP, "A user in a member account can see the status and any errors for the backup jobs in that member account. If you also enable trusted service access with AWS Backup, a user in the organization's management account can see the status and errors for all backup jobs in the organization.")],
 scope="backup jobs from policy-created plans", bullets=["1.3.S1"], **O))
f.append(F("backup-org-policy-resources-by-type-or-tag-not-arns", "restriction",
 "Backup policies select resources by resource type or by tags, but not by individual resource ARNs; to back up individual resources by ARN, use a local backup plan resource assignment.",
 "Can an Organizations backup policy select individual resources by ARN?",
 ["by resource types", "not by individual resource ARNs"],
 [E(MC, "Backup policies support resource selection by resource types (for example, `arn:aws:ec2:*:*:volume/*`) or by tags, but not by individual resource ARNs. Use backup policies for broad application across multiple accounts in an organization or OU, not for targeting individual resources.")],
 scope="Organizations backup policies", tier0=True, bullets=["1.3.S1", "4.3.S1"]))
f.append(F("backup-cross-account-management-components", "behavior",
 "Cross-account management in AWS Backup consists of cross-account monitoring, cross-account backups, backup policies and delegated administrator accounts, and not all of these elements are available in all Regions.",
 "What does cross-account management in AWS Backup consist of?",
 ["cross-account monitoring, cross-account backups, backup policies, and delegated administrator accounts", "Not all of these elements are available in all Regions"],
 [E(MC, "Cross-account management consists of cross-account monitoring, cross-account backups, backup policies, and delegated administrator accounts. Not all of these elements are available in all Regions.")],
 scope="AWS Backup cross-account management", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-cross-account-monitor-all-accounts-in-one-place", "capability",
 "With AWS Organizations set up, AWS Backup can monitor activities in all your accounts in one place, and you can create a backup policy for selected accounts and view aggregate backup job activity in the AWS Backup console.",
 "Can you monitor backup jobs of all accounts of an organization from one place?",
 ["monitor activities in all of your accounts in one place", "aggregate backup job activities"],
 [E(MC, "If you set up AWS Organizations, you can configure AWS Backup to monitor activities in all of your accounts in one place. You can also create a backup policy and apply it to selected accounts that are part of your organization and view the aggregate backup job activities directly from the AWS Backup console.")],
 scope="AWS Backup cross-account monitoring", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-org-policy-merge-only-same-plan-name", "behavior",
 "Backup policies are merged only when they share the same backup plan name; otherwise two policies can coexist in an account without merging.",
 "When are two Organizations backup policies merged into one effective plan?",
 ["only for backup policies that share the same backup plan name", "coexist in that account without any merging"],
 [E(MC, "Merging is done only for backup policies that share the same backup plan name. You can also have policy A and policy B coexist in that account without any merging.")],
 scope="Organizations backup policy inheritance", bullets=["1.3.S1", "4.3.S1"]))
f.append(F("backup-org-policy-creates-visible-plan-in-each-account", "behavior",
 "When you apply a backup policy to the whole organization, each account gets that backup policy, which creates a corresponding backup plan that is visible in that account.",
 "What does applying an Organizations backup policy create in each account?",
 ["creates a corresponding backup plan", "visible in that account"],
 [E(MC, "You choose to apply backup policy A to the whole organization. (This means that each account in the organization gets that backup policy, which creates a corresponding backup plan that is visible in that account.)")],
 scope="Organizations backup policies", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-org-management-account-opt-in-overrides-member-accounts", "behavior",
 "For backup plans managed by Organizations, the resource opt-in settings of the management account override those of a member account, even if delegated administrator accounts are configured, because delegated administrators cannot override settings the way a management account can.",
 "Which opt-in settings win for a backup plan managed by Organizations?",
 ["resource opt-in settings in the management account override", "cannot override settings like a management account can"],
 [E(MC, "For backup plans that are managed by Organizations, the resource opt-in settings in the management account override the settings in a member account for that particular backup plan, even if one or more delegated administrator accounts are configured. Delegated administrator accounts are member accounts with enhanced features and cannot override settings like a management account can.")],
 scope="Organizations-managed backup plans", rel="extended", bullets=["1.3.S1"]))
f.append(F("backup-org-member-accounts-need-vault-and-iam-role", "restriction",
 "Each member account needs at least one backup or logically air-gapped vault and an IAM role, because a backup policy names the Regions, vaults, resources and IAM role to use; policies that reference accounts lacking this information will not work as expected.",
 "What must a member account have for a backup policy to work?",
 ["will not work as expected", "the IAM role that will be used to create the backup"],
 [E(MC, "The backup policies you create will have a backup plan, but they will also identify the AWS Regions, the vault(s) used in the backup plan, the resources that will be backed up, and the IAM role that will be used to create the backup. Backup policies that reference accounts that lack the required information will not work as expected.")],
 scope="member accounts of an organization", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-cross-account-management-must-be-enabled-by-management-account", "restriction",
 "Before cross-account management can be used in AWS Backup, the management account must enable (opt in to) the feature; after that, backup policies can manage resources in multiple accounts.",
 "Who must opt in to cross-account management before backup policies can be used?",
 ["the management account must enable the feature", "opt in"],
 [E(MC, "Before you can use cross-account management in AWS Backup, the management account must enable the feature (that is, opt in to it). After the management account enables cross-account management, you can create backup policies that manage resources in multiple accounts.")],
 scope="AWS Backup cross-account management", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-delegated-admin-performs-most-admin-tasks-from-member-account", "capability",
 "You can delegate AWS Backup administration to a member account in AWS Organizations, so assigned users there can do most AWS Backup administrative tasks from outside the management account and across the organization.",
 "What does a delegated administrator account for AWS Backup allow?",
 ["delegate administration of AWS Backup to a member account", "outside the management account"],
 [E(MC, "Delegated administration provides a convenient way for assigned users in a registered member account to perform most AWS Backup administrative tasks. You can choose to delegate administration of AWS Backup to a member account in AWS Organizations, thereby extending the ability to manage AWS Backup from outside the management account and across the entire organization.")],
 scope="AWS Backup delegated administrator", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-delegated-admin-reduces-management-account-access", "behavior",
 "Delegated administrator accounts allow managing backup policies, minimize the number of users with access to the management account, and permit cross-account monitoring of jobs; accounts, not users, are designated as delegated administrators.",
 "Why use a delegated administrator for AWS Backup?",
 ["minimizes the number of users with access to the management account", "accounts, not users, are designated as delegated administrators"],
 [E(MC, "Note that accounts, not users, are designated as delegated administrators."),
  E(MC, "Enabling delegated administrator accounts allows the option of managing backup policies, it minimizes the number of users with access to the management account, and it permits cross-account monitoring of jobs.")],
 scope="AWS Backup delegated administrator", bullets=["1.3.S1"]))
f.append(F("backup-delegated-admin-registration-alone-does-not-enable-policy-management", "restriction",
 "Registering an account as a delegated administrator alone does not enable backup policy management; you must also complete further steps for the account to view and edit backup policies.",
 "Does registering a delegated administrator let that account edit backup policies?",
 ["alone does not enable backup policy management", "view and edit backup policies"],
 [E(MC, "Registering an account as a delegated administrator alone does not enable backup policy management. To allow the delegated administrator account to view and edit backup policies, you must also complete the following steps:")],
 scope="AWS Backup delegated administrator", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-delegated-admin-privileges-register-deregister-row", "restriction",
 "Only the management account can register or deregister delegated administrator accounts; delegated administrator and member accounts cannot.",
 "Which account type can register a delegated administrator?",
 ["Register/deregister delegated administrator accounts", "Yes | No | No"],
 [ROW(MC, 0, 0)], scope="AWS Backup delegated administration", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-delegated-admin-privileges-enable-cross-account-row", "restriction",
 "Only the management account can enable cross-account management; delegated administrator and member accounts cannot.",
 "Which account type can enable cross-account management?",
 ["Enable cross-account management", "Yes | No | No"],
 [ROW(MC, 0, 1)], scope="AWS Backup delegated administration", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-delegated-admin-privileges-manage-policies-row", "capability",
 "The management account and a delegated administrator can manage backup policies across accounts in AWS Organizations; member accounts cannot.",
 "Which account types can manage backup policies across accounts?",
 ["Manage backup policies across accounts in AWS Organizations", "Yes | Yes | No"],
 [ROW(MC, 0, 2)], scope="AWS Backup delegated administration", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-delegated-admin-privileges-monitor-jobs-row", "capability",
 "The management account and a delegated administrator can monitor cross-account jobs; member accounts cannot.",
 "Which account types can monitor cross-account jobs?",
 ["Monitor cross-account jobs", "Yes | Yes | No"],
 [ROW(MC, 0, 3)], scope="AWS Backup delegated administration", bullets=["1.3.S1"]))
f.append(F("control-tower-backup-enable-landing-zone-then-ous-local-vaults", "behavior",
 "In AWS Control Tower you enable AWS Backup for the landing zone, which creates resources in several accounts, and then on individual OUs, and the accounts in an enabled OU receive local AWS Backup vaults.",
 "How do you turn on AWS Backup in AWS Control Tower, and what do accounts in an OU get?",
 ["Enable AWS Backup for your landing zone", "the accounts in that OU receive local AWS Backup vaults"],
 [E(CT, "Enable AWS Backup for your landing zone. You can do this on the Landing zone settings page in the AWS Control Tower console. When you turn on AWS Backup, resources are created in several accounts."),
  E(CT, "Enable AWS Backup on the individual OUs you wish to include. You can do this task on the OU details page in the console, after you've enabled AWS Backup at the landing zone level. When you enable AWS Backup on an OU, the accounts in that OU receive local AWS Backup vaults.")],
 scope="AWS Control Tower landing zone", service="control-tower", tier0=True, bullets=["1.3.S1"]))
f.append(F("control-tower-backup-tags-set-frequency", "behavior",
 "In AWS Control Tower, the tag on a resource denotes the backup frequency for that resource, and the backup plan follows the schedule specified by the resource tags.",
 "How does AWS Control Tower decide how often a resource is backed up?",
 ["The tag denotes the frequency of backups", "schedule specified by the resource tags"],
 [E(CT, "Tag the selected resources to include in the backups. The tag denotes the frequency of backups for that resource. Your backup plan follows the schedule specified by the resource tags on each resource.")],
 scope="AWS Control Tower backups", service="control-tower", bullets=["1.3.S1"]))
f.append(F("control-tower-backup-no-extra-control-tower-cost", "pricing-dimension",
 "No cost is incurred when you configure AWS Backup with AWS Control Tower, but you incur AWS Backup cost.",
 "Does configuring AWS Backup with AWS Control Tower add a charge?",
 ["No cost is incurred when you configure AWS Backup with AWS Control Tower", "You will incur cost from AWS Backup"],
 [E(CT, "No cost is incurred when you configure AWS Backup with AWS Control Tower. You will incur cost from AWS Backup.")],
 scope="AWS Control Tower backups", service="control-tower", bullets=["4.3.S1"]))
f.append(F("control-tower-backup-plans-not-set-up-in-backup-alone", "restriction",
 "AWS Control Tower does not support setting up backup plans for Control Tower resources directly through the AWS Backup service without also enabling it in AWS Control Tower.",
 "Can you set up backup plans for Control Tower resources only in the AWS Backup service?",
 ["does not support setting up backup plans", "without also enabling it in the AWS Control Tower service"],
 [E(CT, "AWS Control Tower does not support setting up backup plans for AWS Control Tower resources through the AWS Backup service directly, without also enabling it in the AWS Control Tower service.")],
 scope="AWS Control Tower backups", service="control-tower", bullets=["1.3.S1"]))
dump("facts-behavior-09.json", f)
