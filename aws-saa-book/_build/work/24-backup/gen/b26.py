import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
OS = "docs/organizations/latest/userguide/orgs_manage_policies_backup_syntax"
O = dict(service="organizations")
f = []
f.append(F("organizations-backup-policy-must-specify-regions-resources-and-iam-role", "restriction",
 "A backup policy must specify the AWS Regions and resources to be backed up and the IAM role that AWS Backup assumes.",
 "What must an Organizations backup policy specify besides the plan rules?",
 ["Policies must specify the AWS Regions and resources to be backed up", "Policies must specify the IAM role that AWS Backup assumes"],
 [E(OS, "Policies must specify the AWS Regions and resources to be backed up."),
  E(OS, "Policies must specify the IAM role that AWS Backup assumes.")],
 scope="AWS Organizations backup policies", tier0=True, bullets=["1.3.S1", "4.3.S1"], **O))
f.append(F("organizations-backup-policy-vaults-must-exist-in-each-account-and-region", "restriction",
 "Vaults must exist in each specified Region before a backup plan can run, and for each AWS account that receives the effective policy.",
 "What must already exist in a member account for a backup policy to run?",
 ["Vaults must exist in each specified AWS Regions before a backup plan can run", "Vaults must exist for each AWS account that receives the effective policy"],
 [E(OS, "Vaults must exist in each specified AWS Regions before a backup plan can run."),
  E(OS, "Vaults must exist for each AWS account that receives the effective policy.")],
 scope="AWS Organizations backup policies", tier0=True, bullets=["1.3.S1"], **O))
f.append(F("organizations-backup-policy-iam-role-must-exist-and-have-permissions", "restriction",
 "The IAM role named in a backup policy must exist when you create a backup plan for the first time, and must have permission to access resources identified by the tag query and to perform the backup.",
 "What must be true of the IAM role used by an Organizations backup policy?",
 ["The IAM role must exist when creating a backup plan for the first time", "The IAM role must have permission to perform the backup"],
 [E(OS, "The IAM role must exist when creating a backup plan for the first time."),
  E(OS, "The IAM role must have permission to access resources identified by tag query."),
  E(OS, "The IAM role must have permission to perform the backup.")],
 scope="AWS Organizations backup policies", bullets=["1.3.S1", "2.2.S5"], **O))
f.append(F("organizations-backup-policy-stack-sets-create-vaults-and-roles", "behavior",
 "AWS recommends using CloudFormation stack sets and their integration with Organizations to automatically create and configure backup vaults and IAM roles for each member account.",
 "How can you create the backup vaults and IAM roles that backup policies need in every member account?",
 ["AWS CloudFormation stack sets", "automatically create and configure backup vaults and IAM roles"],
 [E(OS, "We recommend that you use AWS CloudFormation stack sets and its integration with Organizations to automatically create and configure backup vaults and IAM roles for each member account in the organization.")],
 scope="AWS Organizations backup policies", tier0=True, bullets=["1.3.S1", "4.3.S1"], **O))
f.append(F("organizations-backup-policy-selection-tags-or-resources-one-required", "restriction",
 "An effective backup policy must have either tags or resources in its selection to be valid; the two elements are mutually exclusive.",
 "Can a backup policy selection use tags and resources together?",
 ["two mutually exclusive elements: tags and resources", "must have either tags or resources in the selection to be valid"],
 [E(OS, "There are two mutually exclusive elements: `tags` and `resources`. An effective policy **must** `have` either tags or `resources` in the selection to be valid.")],
 scope="AWS Organizations backup policy selections", rel="extended", bullets=["1.3.S1"], **O))
f.append(F("organizations-backup-policy-parent-can-block-child-changes-with-none-operator", "capability",
 "A parent backup policy that uses the @@operators_allowed_for_child_policies @@none operator at every node stops a child policy from changing the plan or adding plans to the effective policy.",
 "How can a parent backup policy prevent child policies from overriding it?",
 ["a child policy can't make changes of any kind to the plan", "Nor can a child policy add additional plans to the effective policy"],
 [E(OS, "The presence of `\"@@operators_allowed_for_child_policies\": [\"@@none\"]` at every node of the policy means that a child policy can't make changes of any kind to the plan. Nor can a child policy add additional plans to the effective policy.")],
 scope="AWS Organizations backup policy inheritance", tier0=True, bullets=["1.3.S1"], **O))
dump("facts-behavior-26.json", f)
