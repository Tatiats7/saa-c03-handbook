---
chapter: "03"
file: deep
title: IAM in depth
status: draft
updated: 2026-10-11
---

# IAM in depth

## How it works (59 min)
<!-- section: role=how; route=full; minutes=59 -->

### Every AWS call is a signed request that IAM answers (4 min)

Planned: the four parts of a request (principal, action, resource, context), and authentication against authorization. Then IAM as a global service, and the customer's half of the shared responsibility model.

### A policy statement pairs an effect with actions and resources (4 min)

Planned: the JSON statement (Effect, Action, Resource, Condition), managed against inline policies, policy versions, and how least privilege looks in a real statement.

### AWS allows a request only when nothing denies and something allows (5 min)
<!-- section: route=pass -->

Many policies can apply to one request, and they can disagree. AWS needs one rule for every case.

The rule starts from No: by default, [all requests are implicitly denied](../facts/iam.md#iam-eval-implicit-deny-by-default). This is an **implicit deny**. <!-- needs-term: implicit deny -->

Now follow one request through four checks. Use them as a checklist: the result is the same in any order.

1. **Collect.** AWS evaluates [every applicable policy of these types](../facts/iam.md#iam-eval-policy-types-checked-in-account). They are service control policies (SCPs), resource control policies (RCPs), resource-based and identity-based policies, permissions boundaries and session policies.
2. **Look for a deny.** AWS [first looks for a Deny statement in every policy that applies](../facts/iam.md#iam-eval-deny-checked-first). [Even one explicit deny that applies](../facts/iam.md#iam-eval-deny-checked-first) ends the evaluation with Deny. This is an **explicit deny**, not an implicit one: a Deny statement causes it. <!-- needs-term: explicit deny -->
3. **Check every ceiling.** An SCP, an RCP, a permissions boundary and a session policy each set a ceiling. They give nothing: [an SCP never grants permissions](../facts/iam.md#iam-scp-never-grants-permissions), [an RCP never grants permissions](../facts/iam.md#iam-rcp-never-grants-limits-resources), and a boundary [does not provide permissions on its own](../facts/iam.md#iam-boundary-limits-but-never-grants).
4. **Find a grant.** An identity-based or a resource-based policy allows the action. If none does, [the request is implicitly denied](../facts/iam.md#iam-eval-identity-policy-no-allow-is-implicit-deny).

With an SCP, a boundary and an identity-based policy, a request is [allowed only if all three policy types allow it](../facts/iam.md#iam-scp-boundary-identity-all-must-allow). One action, s3:GetObject, by a role in a member account:

<!-- table: plain -->
| Case | SCP | Identity-based policy | Bucket policy | Result |
|---|---|---|---|---|
| 1 | Allows S3 | Allows the action | Silent | Allow |
| 2 | Allows S3 | Silent | Silent | Implicit deny |
| 3 | Allows EC2, not S3 | Allows the action | Silent | Implicit deny |
| 4 | Allows S3 | Allows the action | Denies the action | Explicit deny |

Why does a deny win? A security team writes a Deny to stop one action. If a later allow could cancel it, the guardrail would fail on the day someone attached AdministratorAccess. So [an explicit deny overrides an explicit allow](../facts/iam.md#iam-eval-explicit-deny-overrides-allow), and the fix for an explicit deny is to remove it.

> **Exam signal:** "no one, including administrators" points to a Deny in an SCP. An administrator can delete a Deny inside the account, but member account principals [cannot remove or change SCPs that are applied to that account](../facts/iam.md#iam-scp-faq-member-principals-cannot-change-scps).

<details>
<summary>Go deeper: exceptions to the implicit deny and to SCPs</summary>

The root user starts with an allow: the implicit deny applies [with the exception of the AWS account root user, which has full access](../facts/iam.md#iam-eval-implicit-deny-by-default). In a member account, an SCP still limits principals [including the member account's root user](../facts/iam.md#iam-scp-applies-to-member-root-user).

In one account, a resource-based policy can name a user by its Amazon Resource Name (ARN). A policy that [grants permissions to an IAM user ARN is not limited by an implicit deny](../facts/iam.md#iam-boundary-user-arn-grant-not-limited) in a boundary. An explicit deny still wins in both cases.

Two principals escape SCPs: SCPs [do not affect users or roles in the management account](../facts/iam.md#iam-scp-no-effect-on-management-account), and [Service-linked roles cannot be restricted by SCPs](../facts/iam.md#iam-scp-no-effect-on-service-linked-roles).

</details>

> **Try it:** Give a test role an allow and a deny for the same action, and watch the policy simulator choose. See [3-do.md](3-do.md). <!-- task: iam-t02 -->

> **Say it:** The short answer is: a request needs one allow and no deny. The thing to watch is a ceiling, such as an SCP.

**Stop and answer.** A developer role has an identity-based policy that allows s3:\* on every bucket. Its permissions boundary allows s3:GetObject and nothing else. No policy has a Deny statement. Can the role upload an object with s3:PutObject?

<details>
<summary>Answer</summary>

No. The boundary is a ceiling, and it does not allow PutObject, so the result is an implicit deny. The role can do only the actions [allowed by both its identity-based policies and its permissions boundaries](../facts/iam.md#iam-permissions-boundary-sets-maximum-does-not-grant).

</details>

### The root user and IAM users hold long-term credentials (4 min)

Planned: why the root user is for a few tasks, root multi-factor authentication (MFA), and centralized root access for member accounts. Then IAM users, groups, access keys and their rotation, and why people should federate instead.

### A role gives temporary credentials to principals that its trust policy names (5 min)
<!-- section: route=pass -->

An access key works until someone deletes it: long-term keys [remain valid until you manually revoke them](../facts/iam.md#iam-long-term-keys-valid-until-revoked-temporary-expire). A leaked key stays useful to an attacker.

The fix is an identity that keeps no key and gets short-lived credentials on request. That identity is an **IAM role**. A role [does not have standard long-term credentials, such as a password or access keys](../facts/iam.md#iam-users-have-long-term-credentials-roles-do-not). You [attach both a trust policy and an identity-based policy to an IAM role](../facts/iam.md#iam-role-trust-policy-only-resource-based-policy-in-iam):

- The **trust policy** <!-- needs-term: trust policy --> answers "Who can use me?" Its Principal element [names who can assume the role](../facts/iam.md#iam-role-trust-policy-names-who-can-assume).
- The **permissions policy** <!-- needs-term: permissions policy --> answers "What can the session do?" [The permissions policy of the role being assumed determines what the temporary credentials](../facts/iam.md#iam-role-permissions-policy-defines-session-permissions) can do. It is not the same as the trust policy.

Now follow one AssumeRole call.

1. A principal calls sts:AssumeRole with the ARN of the role.
2. AWS Security Token Service (AWS STS) reads the trust policy. If the trust policy does not name the principal, AWS STS refuses. Across accounts, the trust policy is [only half of the cross-account trust](../facts/iam.md#iam-assume-role-two-permissions-checked): the caller's own policy must also allow sts:AssumeRole on the role ARN.
3. AWS STS returns [an access key ID, a secret access key and a session token](../facts/sts.md#sts-temporary-credentials-include-session-token), with [the date on which the current credentials expire](../facts/sts.md#sts-credentials-include-expiration).
4. The session has the role's permissions, not the caller's: [the permissions are not cumulative](../facts/iam.md#iam-assume-role-replaces-original-permissions).
5. At the end, [after they expire AWS no longer accepts any API request made with them](../facts/sts.md#sts-temporary-credentials-expire-not-stored).

On EC2, your code does not call AssumeRole itself. Code on the instance can [get automatic temporary security credentials from the instance metadata](../facts/iam.md#iam-instance-profile-one-role-and-metadata-credentials), and they are [temporary and updated automatically](../facts/iam.md#iam-ec2-role-credentials-rotate-automatically).

Why does AWS prefer a role to a key? Time limits the damage. A leaked session stops working when it expires; a leaked key works until a person acts.

> **Exam signal:** "the AssumeRole call fails" points to the trust side: the trust policy, and across accounts also the caller's own allow for sts:AssumeRole. "The call succeeds, but the next call fails" points to the permissions policy.

<details>
<summary>Go deeper: session length and role chaining</summary>

Without DurationSeconds, a session lasts [one hour](../facts/sts.md#sts-assumerole-duration-default). Role chaining is [using the credentials of one role to assume another](../facts/iam.md#iam-role-chaining-one-hour-limit-exceptions). It [limits the session to one hour regardless of the role's maximum session duration](../facts/iam.md#iam-role-chaining-one-hour-limit-exceptions).

A long job in a chained session assumes the second role again before the hour ends. On EC2, role credentials are [not subject to the role's maximum session duration](../facts/iam.md#iam-ec2-role-credentials-not-limited-by-max-session).

</details>

<details>
<summary>Go deeper: leaked credentials</summary>

Temporary credentials [cannot be revoked](../facts/sts.md#sts-temporary-credentials-cannot-be-revoked-permissions-can-change) one by one, but their permissions are [evaluated each time a request is made](../facts/sts.md#sts-temporary-credentials-cannot-be-revoked-permissions-can-change). So "Revoke active sessions" on the role adds an inline policy that [denies all permissions to all actions](../facts/iam.md#iam-revoke-role-sessions-denies-credentials-issued-before). Credentials [issued before the specified time become invalid](../facts/iam.md#iam-revoke-role-sessions-denies-credentials-issued-before). In a log, key IDs that [begin with ASIA are temporary credentials](../facts/iam.md#iam-access-key-prefix-akia-vs-asia), and IDs that [begin with AKIA are long-term credentials](../facts/iam.md#iam-access-key-prefix-akia-vs-asia).

</details>

> **Say it:** The short answer is: use a role, not a key. The thing to watch is the trust policy, which names who can use the role.

**Stop and answer.** A contractor's IAM user in account A can write to a bucket in account A. The contractor assumes a role in account B that can read one bucket in account B. During the role session, can the contractor write to the bucket in account A?

<details>
<summary>Answer</summary>

No. During the session the contractor has the role's permissions only, because [the permissions are not cumulative](../facts/iam.md#iam-assume-role-replaces-original-permissions). The contractor gets the user's permissions back after leaving the role.

</details>

### Passing a role to a service needs the PassRole permission (4 min)

Planned: how a user gives a role to EC2 or Lambda with iam:PassRole, how that stops privilege escalation, and service roles against service-linked roles. Also the resource-based policy of a Lambda function, which lets Amazon S3 or Amazon SNS invoke it.

### Same-account access needs one allow but cross-account access needs two (5 min)
<!-- section: route=pass -->

A permission can live in two places: on the identity, or on the resource.

- An **identity-based policy** is attached to a user, group or role. You [cannot use the Principal element in an identity-based policy](../facts/iam.md#iam-principal-element-not-in-identity-policies); the principal is the identity that holds the policy.
- A **resource-based policy** is attached to a resource, for example [S3 buckets, SQS queues, VPC endpoints, KMS encryption keys, DynamoDB tables and streams](../facts/iam.md#iam-resource-based-policy-examples). It names its principal: [you must indicate the account, user, role, or AWS STS federated user principal](../facts/iam.md#iam-principal-element-resource-policy-not-identity-policy).

Now ask: who owns each side? In one account, one owner controls both policies, so one allow is enough: [the permissions of identity-based and resource-based policies are a union](../facts/iam.md#iam-eval-same-account-identity-or-resource-allow).

Across two accounts, AWS evaluates both accounts and [allows the request only if both evaluations return Allow](../facts/iam.md#iam-eval-cross-account-needs-both-policies). [The account where the principal exists is the trusted account](../facts/iam.md#iam-cross-account-trusted-vs-trusting), and [the account where the resource exists is the trusting account](../facts/iam.md#iam-cross-account-trusted-vs-trusting).

<!-- table: plain -->
| Where is the bucket? | Identity-based policy | Bucket policy | Result |
|---|---|---|---|
| Same account | Allows | Silent | Allow |
| Same account | Silent | Allows | Allow |
| Other account | Allows | Silent | Implicit deny |
| Other account | Silent | Allows | Implicit deny |
| Other account | Allows | Allows | Allow |

The table assumes that no deny and no ceiling applies. Why two allows? Each owner decides for its own side. Account A decides what its role can do, and account B decides who can use its bucket.

There are two ways to reach a resource in another account.

1. **Resource-based policy.** The principal [does not give up its permissions](../facts/iam.md#iam-cross-account-role-vs-resource-policy), so it can copy data between its own bucket and the other bucket.
2. **Role in the other account.** The principal gives up its own permissions for the session. [A role is used as a proxy for services that do not support resource-based policies](../facts/iam.md#iam-cross-account-role-vs-resource-policy), and [Amazon EC2 does not support resource-based policies](../facts/iam.md#iam-ec2-no-resource-based-policies).

> **Exam signal:** "access the bucket from another account and keep its own permissions" points to a bucket policy, because the principal [does not give up its permissions](../facts/iam.md#iam-cross-account-role-vs-resource-policy).

<details>
<summary>Go deeper: principals and keys</summary>

Naming an account [delegates authority to that account](../facts/iam.md#iam-principal-account-delegates-to-account). An account ARN that ends in :root [does not limit the permission to the root user](../facts/iam.md#iam-principal-account-delegates-to-account). A wildcard principal with Allow grants access [including anonymous users (public access)](../facts/iam.md#iam-principal-wildcard-is-public).

A **KMS key** breaks the union. [IAM policies cannot allow access to a KMS key](../facts/iam.md#iam-kms-iam-policy-needs-key-policy-permission) unless the key policy allows it. Across accounts, [neither policy alone is sufficient](../facts/iam.md#iam-kms-cross-account-key-policy-and-iam-policy). <!-- xref: 06 KMS key policies -->

</details>

**Spot the bug.** A team writes this statement in the bucket policy of example-reports, for the analysts in account 444455556666. What is wrong?

```json
{
  "Effect": "Allow",
  "Principal": {"AWS": "arn:aws:iam::444455556666:group/analysts"},
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::example-reports/*"
}
```

<details>
<summary>Answer</summary>

The principal is a group, and you [cannot identify a user group as a principal](../facts/iam.md#iam-principal-group-cannot-be-principal). Name a role of that account instead. The role also needs its own allow, because the [identity-based policy in the trusted account must allow the access](../facts/iam.md#iam-eval-cross-account-needs-both-policies).

</details>

> **Say it:** The short answer is: across accounts, both sides have to say yes. The thing to watch is a KMS key: [neither policy alone is sufficient](../facts/iam.md#iam-kms-cross-account-key-policy-and-iam-policy).

**Stop and answer.** A Lambda function in account A sends messages to an SQS queue in account B. The queue policy allows the function's role. The role's identity-based policy allows sqs:SendMessage on queues in account A. Does the call succeed?

<details>
<summary>Answer</summary>

No. The call crosses accounts, so the [identity-based policy in the trusted account must allow the access](../facts/iam.md#iam-eval-cross-account-needs-both-policies) too. The role's policy names queues in account A, not in account B, so account A's side is an implicit deny.

</details>

### An external ID stops the confused deputy in third-party roles (4 min)

Planned: why a vendor that serves many customers needs an external ID in the trust policy. Also why the external ID is not a secret.

### IAM Identity Center gives employees one sign-in for many accounts (4 min)

Planned: one trace of an employee sign-in. The identity source is the built-in directory, Active Directory or an external SAML provider. A permission set becomes a role that IAM Identity Center creates in each account. Then why AWS calls it the front door for employees.

### Cognito and Roles Anywhere give app users and servers temporary credentials (4 min)

Planned: one trace for a mobile app user and one for a server on premises. A Cognito user pool signs the user in, and an identity pool exchanges the token for role credentials. IAM Roles Anywhere exchanges a certificate. One table compares both with IAM Identity Center.

### Condition keys narrow an allow to the right organization or network (4 min)

Planned: aws:PrincipalOrgID, aws:SourceVpce, aws:SecureTransport and aws:MultiFactorAuthPresent, each with the stem phrase that asks for it. Go deeper: tags for attribute-based access control, and the data perimeter idea.

### A permissions boundary lets developers create roles without escalating (4 min)

Planned: the delegation pattern: developers create roles for their workloads, and a boundary limits what those roles can ever receive.

### A KMS key policy decides whether IAM policies count for the key (4 min)

Planned: the key policy as the primary control, how it enables IAM policies, grants for AWS services, and cross-account use of a key. Keep this sentence: unless the key policy allows it, [IAM policies cannot allow access to a KMS key](../facts/iam.md#iam-kms-iam-policy-needs-key-policy-permission).

### Access Analyzer and last-accessed data find permissions to remove (4 min)

Planned: external and unused access findings, policy generation from CloudTrail, last accessed information, the credential report and the policy simulator.

## Numbers that decide answers (3 min)
<!-- section: role=numbers; route=full; minutes=3 -->

### A-list

<!-- table: numbers -->
| Number | What it is | Why it decides an answer |
|---|---|---|
| [one hour](../facts/sts.md#sts-assumerole-duration-default) | AssumeRole session when DurationSeconds is not set | A stem with long jobs needs a longer requested session |
| [900 seconds (15 minutes)](../facts/sts.md#sts-assumerole-duration-range) | Shortest session that AssumeRole accepts | A shorter value fails |
| [1 hour to 12 hours](../facts/iam.md#iam-role-max-session-duration-setting) | Range of a role's maximum session duration setting | A full working day fits; a longer one does not |
| [one hour](../facts/sts.md#sts-role-chaining-max-one-hour) | Session limit when one role assumes another | Role chaining caps long sessions |
| [5,000](../facts/iam.md#iam-quota-users-per-account) | IAM users in one account | More people point to federation |
| [up to eight MFA devices](../facts/iam.md#iam-mfa-devices-up-to-eight) | MFA devices for one user or the root user | A backup device needs no second user |
| [two access keys](../facts/iam.md#iam-access-keys-max-two-per-user) | Access keys for one IAM user | Rotation uses the second key slot |

### B-list

<!-- table: numbers -->
| Number | What it is |
|---|---|
| [10](../facts/iam.md#iam-quota-groups-per-user) | Groups that one IAM user can join |
| [up to five versions](../facts/iam.md#iam-policy-versions-five) | Stored versions of a customer managed policy |
| [6,144 characters](../facts/iam.md#iam-limit-managed-policy-size) | Maximum length of one customer managed policy |
| [2048 characters](../facts/iam.md#iam-quota-role-trust-policy-length) | Default length limit of a role trust policy |
| [up to 50 session tags](../facts/iam.md#iam-limit-session-tags) | Session tags on one role session |
| [129,600 seconds (36 hours)](../facts/sts.md#sts-getsessiontoken-duration-iam-user) | Longest GetSessionToken session of an IAM user |
| [within 35 days](../facts/iam.md#iam-root-mfa-required-all-account-types) | Time to register root MFA after the first sign-in attempt |
| [20](../facts/iam.md#iam-quota-managed-policies-per-role) | Default quota of managed policies on one role, after the change below |

> **Changed recently:** (2026-08-19) Default quota of managed policies on one IAM role.<br>
> **Old:** 10 per role. <!-- needs-display: iam-change-managed-policies-per-role-default-20 "10" --><br>
> **Now:** [20](../facts/iam.md#iam-quota-managed-policies-per-role) managed policies per role by default.<br>
> **The exam probably expects:** the old value of 10, if any. Do not let this number decide an answer.<br>
> **Status:** not examinable yet.

## Decision record (3 min)
<!-- section: role=example; route=full; minutes=3 -->

**Context.** A customer's purchase form asks who can access the recordings. Ben finds the root user's access key in the code and on 3 laptops. Callvale's application calls Amazon S3 and Amazon Transcribe with that key, and Ana and Ben share the root user's password.

**Requirement.** The application must call Amazon S3 and Amazon Transcribe without long-term credentials in code or on disk. Each person and each workload must have least privilege. Which solution is the MOST secure?

**Options.**

- Move the access key out of the code into a configuration file on the instance.
- Create an IAM user with an access key for each workload.
- **Attach an IAM role to the instance through an instance profile.**

**Decision.** An IAM role for the workload. People sign in as IAM users with MFA, in two groups, for now. The root user gets MFA and no access key. The role's credentials are [temporary and updated automatically](../facts/iam.md#iam-ec2-role-credentials-rotate-automatically), so no key remains to leak.

**Trade-off.** Each workload needs its own tested policy. IAM users for people stay until IAM Identity Center replaces them at stage 3.

## FAQ quick-fire (5 min)
<!-- section: role=faq; route=full; minutes=5 -->

**FAQ 1.** Can an SCP give a user a permission?

<details>
<summary>Answer</summary>

No: [an SCP never grants permissions](../facts/iam.md#iam-scp-never-grants-permissions).

> "SCPs do not grant permissions."
> — [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

</details>

**FAQ 2.** Does an empty SCP on an account allow every action?

<details>
<summary>Answer</summary>

No. It is [equivalent to attaching a policy that explicitly denies all actions](../facts/iam.md#iam-scp-faq-empty-scp-denies-all).

> "Attaching an empty SCP to an account is equivalent to attaching a policy that explicitly denies all actions."
> — [AWS Organizations FAQs](https://aws.amazon.com/organizations/faqs/)

</details>

**FAQ 3.** Can a member account's root user remove its SCP?

<details>
<summary>Answer</summary>

No. Its principals [cannot remove or change SCPs that are applied to that account](../facts/iam.md#iam-scp-faq-member-principals-cannot-change-scps).

> "Principals in a member account (including the root user for the member account) cannot remove or change SCPs that are applied to that account."
> — [AWS Organizations FAQs](https://aws.amazon.com/organizations/faqs/)

</details>

**FAQ 4.** Can any policy type hold a Deny statement?

<details>
<summary>Answer</summary>

Yes. You can [specify a Deny statement in any policy](../facts/iam.md#iam-faq-restrict-with-deny-statement).

> "To restrict access, specify a Deny statement in any policy."
> — [AWS Identity and Access Management (IAM) FAQs](https://aws.amazon.com/iam/faqs/)

</details>

**FAQ 5.** Can the IAM policy simulator test an SCP?

<details>
<summary>Answer</summary>

Yes. It tests [identity-based and resource-based policies, IAM permissions boundaries, and SCPs](../facts/iam.md#iam-faq-policy-simulator-policy-types).

> "Use the policy simulator to test and troubleshoot identity-based and resource-based policies, IAM permissions boundaries, and SCPs."
> — [AWS Identity and Access Management (IAM) FAQs](https://aws.amazon.com/iam/faqs/)

</details>

**FAQ 6.** Can an identity-based policy hold a Principal element?

<details>
<summary>Answer</summary>

No. You [cannot use the Principal element in an identity-based policy](../facts/iam.md#iam-principal-element-not-in-identity-policies).

> "You cannot use the `Principal` element in an identity-based policy."
> — [IAM JSON policy elements: Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html)

</details>

**FAQ 7.** Can you revoke one set of temporary credentials?

<details>
<summary>Answer</summary>

No; they [cannot be revoked](../facts/sts.md#sts-temporary-credentials-cannot-be-revoked-permissions-can-change). Revoke the role's active sessions instead.

> "After AWS STS issues temporary security credentials, they are valid through the expiration period and cannot be revoked."
> — [Permissions for temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access.html)

</details>

**FAQ 8.** In one account, can a bucket policy alone allow a role to read?

<details>
<summary>Answer</summary>

Yes, without a deny or a ceiling: [a resource-based policy allow needs no additional identity-based policy](../facts/iam.md#iam-eval-same-account-identity-or-resource-allow).

> "If either the identity-based policy or the resource-based policy within the same account allows the request and the other doesn't, the request is still allowed."
> — [Policy evaluation for requests within a single account](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-basics.html)

</details>

**FAQ 9.** Across accounts, can a bucket policy alone give a role access?

<details>
<summary>Answer</summary>

No. AWS [allows the request only if both evaluations return Allow](../facts/iam.md#iam-eval-cross-account-needs-both-policies).

> "The request is allowed only if both evaluations return a decision of `Allow`."
> — [Cross-account policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.html)

</details>

**FAQ 10.** Can one instance profile hold two IAM roles?

<details>
<summary>Answer</summary>

No. It [can hold only one IAM role and this limit cannot be increased](../facts/iam.md#iam-instance-profile-one-role-and-metadata-credentials).

> "An instance profile can contain only one IAM role, although a role can be included in multiple instance profiles."
> — [Use instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)

</details>
