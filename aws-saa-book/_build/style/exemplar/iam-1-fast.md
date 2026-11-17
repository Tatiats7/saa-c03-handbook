---
id: "03"
slug: iam
title: IAM
file: fast
tier: deep
xl: true
domains: [1]
tasks: ["1.1", "1.3"]
services: [iam, sts]
minutes: {fast: 20, pass: 73, full: 161}
status: draft
updated: 2026-10-11
---

# IAM

## Predict (2 min)
<!-- section: role=predict; route=fast; minutes=2 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** Your IAM role in a member account has the AdministratorAccess policy. A service control policy (SCP) on the account allows Amazon S3 actions and nothing else. Can you launch an EC2 instance? <!-- gist-trap -->

**Predict 2.** An application on an EC2 instance reads an S3 bucket. Where should the application keep its access key?

**Predict 3.** A bucket policy in account B allows a role from account A to read objects. The role's own policies say nothing about Amazon S3. Can the role read the objects?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

Open AWS CloudShell and ask AWS who you are. Then read the trust policy of one role, and look for a password or a key.

<!-- task:start id=iam-t01 -->
<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** IAM decides who can do what in AWS. By default, [all requests are implicitly denied](../facts/iam.md#iam-eval-implicit-deny-by-default), and [an explicit deny overrides an explicit allow](../facts/iam.md#iam-eval-explicit-deny-overrides-allow).

**The problem it solves.** Without IAM, everyone shares one all-powerful identity, and one leaked key opens everything. IAM gives each person and workload its own identity, and a policy should [grant only the permissions required to perform a task](../facts/iam.md#iam-faq-least-privilege-definition).

**Predict the picture.** Does a principal keep a key, or does it get credentials from AWS?

<details>
<summary>Show the picture</summary>

![A sequence with three participants: a principal, AWS STS and Amazon S3. The principal asks AWS STS to assume a role. AWS STS checks the trust policy and returns temporary credentials. The principal signs a request to Amazon S3 with them. AWS evaluates the policies, and Amazon S3 returns the object or an access denied error.](../diagrams/svg/iam-hero.svg)

**Figure.** A role gives temporary credentials, and the policies are [evaluated each time a request is made](../facts/sts.md#sts-temporary-credentials-cannot-be-revoked-permissions-can-change).

1. The principal asks AWS Security Token Service (AWS STS) to assume a role.
2. AWS STS checks that the trust policy of the role names the principal.
3. AWS STS returns temporary security credentials that expire.
4. The principal signs a request to Amazon S3 with the temporary credentials.
5. AWS evaluates the policies that apply, and [an explicit deny overrides an explicit allow](../facts/iam.md#iam-eval-explicit-deny-overrides-allow).
6. Amazon S3 returns the object, or an access denied error.

</details>

> **Startup example:** Callvale's application calls Amazon S3 and Amazon Transcribe with the root user's access key. The key is stored in the code. Ana and Ben share the root user's password. Callvale must remove long-term keys and must give each person and each workload least privilege.

## Words that go together (2 min)
<!-- section: role=words; route=fast; minutes=2 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| principal (PRIN-sih-pul) | the principal **makes** a request | The user, role or service that sends a request | the resource that the request acts on |
| IAM role | **assume** a role | An identity without long-term keys | IAM user, which has long-term keys |
| trust policy | the trust policy **names** a principal | Says who can assume the role | permissions policy: what the session can do |
| identity-based policy | **attach** an identity-based policy to a role | Says what the user, group or role can do | resource-based policy |
| resource-based policy | the policy **names** a principal | Sits on a resource and names who can use it | identity-based policy |
| temporary security credentials | the credentials **expire** | Key ID, secret key and session token with an end time | access key of an IAM user |
| least privilege | **apply** least privilege | The permissions a task needs, and no more | a broad AWS managed policy |
| service control policy | an SCP **limits** permissions | An organization policy that sets a ceiling on what an account can do | permissions boundary, for one role |

## Choose it or not (3 min)
<!-- section: role=choose; route=fast; minutes=3 -->

### IAM role or IAM user

<!-- table: compare -->
| Question | IAM role | IAM user |
|---|---|---|
| What credentials? | Temporary keys that AWS STS generates on request <!-- needs-display: sts-temporary-credentials-expire-not-stored "generated dynamically on request" --> | [IAM users have long-term credentials such as passwords and access keys](../facts/iam.md#iam-users-have-long-term-credentials-roles-do-not) |
| When does a leaked key stop working? | The keys [expire after a short period of time](../facts/iam.md#iam-long-term-keys-valid-until-revoked-temporary-expire) | The keys [remain valid until you manually revoke them](../facts/iam.md#iam-long-term-keys-valid-until-revoked-temporary-expire) |
| Who uses it? | Workloads, AWS services and federated people | A person or tool without role support |

**Deciding question:** Can this workload or person get temporary credentials instead of a stored key?

### Identity-based or resource-based policy

<!-- table: compare -->
| Question | Identity-based policy | Resource-based policy |
|---|---|---|
| Where is it attached? | A user, group or role | A resource, such as a bucket or a queue |
| Does it name a principal? | No: you [cannot use the Principal element in an identity-based policy](../facts/iam.md#iam-principal-element-not-in-identity-policies) | Yes: [you must indicate the account, user, role, or AWS STS federated user principal](../facts/iam.md#iam-principal-element-resource-policy-not-identity-policy) |
| Same account, no deny or ceiling? | Either is enough: [the permissions of identity-based and resource-based policies are a union](../facts/iam.md#iam-eval-same-account-identity-or-resource-allow) | Either, except for KMS keys: [IAM policies cannot allow access to a KMS key](../facts/iam.md#iam-kms-iam-policy-needs-key-policy-permission) <!-- xref: 06 KMS key policies --> |
| Another account? | AWS [allows the request only if both evaluations return Allow](../facts/iam.md#iam-eval-cross-account-needs-both-policies) | Both accounts allow it |

**Deciding question:** Are the principal and the resource in the same account?

### Grant or ceiling

<!-- table: compare -->
| Question | Identity-based policy | Permissions boundary | SCP |
|---|---|---|---|
| Does it grant access? | Yes | No: it [does not grant permissions](../facts/iam.md#iam-permissions-boundary-sets-maximum-does-not-grant) | No: [an SCP never grants permissions](../facts/iam.md#iam-scp-never-grants-permissions) |
| Whom does it apply to? | The identity it is attached to | One user or role | Principals of member accounts |
| Does it reach the root user? | No: you [cannot attach identity-based policies to the root user](../facts/iam.md#iam-root-user-no-identity-policies-or-boundary) | No: you [cannot set a permissions boundary for the root user](../facts/iam.md#iam-root-user-no-identity-policies-or-boundary) | Yes, [including the member account's root user](../facts/iam.md#iam-scp-applies-to-member-root-user) |

**Deciding question:** Do you want to give access, or put a ceiling on access that others give?

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "application on EC2 instances must call AWS APIs" | IAM role through an instance profile | [AWS delivers the temporary credentials of an IAM role to that compute resource](../facts/iam.md#iam-compute-services-receive-role-credentials-no-keys-needed) | the servers are on premises: IAM Roles Anywhere |
| "one policy allows the action, another denies it" | the deny wins | [an explicit deny overrides an explicit allow](../facts/iam.md#iam-eval-explicit-deny-overrides-allow) | the Deny's condition does not match the request |
| "no one in member accounts, including the root user" | Deny in an SCP | an SCP limits principals [including the member account's root user](../facts/iam.md#iam-scp-applies-to-member-root-user) | the management account: SCPs [affect only the member accounts](../facts/iam.md#iam-scp-no-effect-on-management-account) |
| "developers create roles but must not exceed their own permissions" | permissions boundary | a boundary sets the [maximum permissions that an identity-based policy can grant](../facts/iam.md#iam-permissions-boundary-sets-maximum-does-not-grant) | the limit covers a whole account: SCP |
| "a third party needs access to the company's account" | cross-account role with an external ID | the check is [an sts:ExternalId condition in the role's trust policy](../facts/iam.md#iam-external-id-prevents-confused-deputy) | both accounts belong to the company: a plain role trust |
| "another account reads the bucket and keeps its own permissions" | bucket policy | with a resource-based policy the principal [does not give up its permissions](../facts/iam.md#iam-cross-account-role-vs-resource-policy) | the service has no resource-based policy: use a role |
| "more than 5,000 employees need access to AWS" | IAM Identity Center | an account holds at most [5,000](../facts/iam.md#iam-quota-users-per-account) IAM users | the users are customers of a mobile app: Amazon Cognito |

### Traps

- **Wrong belief:** If one policy allows an action, the request succeeds. **Truth:** [An explicit deny overrides an explicit allow](../facts/iam.md#iam-eval-explicit-deny-overrides-allow). <!-- trap: iam-trap-allow-beats-deny -->
- **Wrong belief:** An SCP or a permissions boundary that allows Amazon S3 gives access to S3. **Truth:** [An SCP never grants permissions](../facts/iam.md#iam-scp-never-grants-permissions), and a boundary [does not provide permissions on its own](../facts/iam.md#iam-boundary-limits-but-never-grants). <!-- trap: iam-trap-scp-grants -->
- **Wrong belief:** A role with AdministratorAccess, or the root user, can do everything in a member account. **Truth:** Its permissions are [the intersection between those allowed by the SCP and the permissions granted to the principal by IAM permission policies](../facts/iam.md#iam-scp-faq-effective-permissions-intersection). The SCP limits principals [including the member account's root user](../facts/iam.md#iam-scp-applies-to-member-root-user). <!-- trap: iam-trap-admin-ignores-scp -->
- **Wrong belief:** A bucket policy that names a role in another account is enough. **Truth:** AWS [allows the request only if both evaluations return Allow](../facts/iam.md#iam-eval-cross-account-needs-both-policies). <!-- trap: iam-trap-cross-account-one-policy -->
- **Wrong belief:** A user who assumes a role keeps the user's permissions and adds the role's. **Truth:** [The permissions are not cumulative](../facts/iam.md#iam-assume-role-replaces-original-permissions). <!-- trap: iam-trap-role-adds-permissions -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2022-07-26) The single sign-on service has a new name.<br>
> **Old:** the service was formerly AWS Single Sign-On.<br>
> **Now:** [AWS IAM Identity Center](../facts/iam.md#iam-change-sso-renamed-identity-center-2022).<br>
> **The exam probably expects:** IAM Identity Center; older practice sets use the old name.<br>
> **Status:** examinable.

> **Changed recently:** (2025-06-17) Root user multi-factor authentication (MFA) is required in every account type.<br>
> **Old:** management and standalone accounts required root user MFA; member accounts did not.<br>
> **Now:** [All AWS account types (standalone, management, and member accounts)](../facts/iam.md#iam-root-mfa-required-all-account-types) require MFA for the root user.<br>
> **The exam probably expects:** MFA on the root user of every account.<br>
> **Status:** examinable.

## Check (2 min)
<!-- section: role=check; route=fast; minutes=2 -->

**Check 1.** An SCP on a member account denies deleting trails. Can the root user of that account delete a trail?

<details>
<summary>Answer</summary>

No. An SCP limits principals [including the member account's root user](../facts/iam.md#iam-scp-applies-to-member-root-user).

**Predict 1:** No: [SCPs act as filters that specify the maximum permissions](../facts/iam.md#iam-scp-allow-is-a-filter-not-a-grant), and this SCP does not allow EC2.

</details>

**Check 2.** A Lambda function writes to a DynamoDB table. How does it get credentials?

<details>
<summary>Answer</summary>

From its execution role: [AWS delivers the temporary credentials of an IAM role to that compute resource](../facts/iam.md#iam-compute-services-receive-role-credentials-no-keys-needed).

**Predict 2:** Nowhere: the instance gets a role, so no key is stored.

</details>

**Check 3.** Same bucket policy, but the role is now in the bucket's account. Can the role read the objects?

<details>
<summary>Answer</summary>

Yes. In one account, [the permissions of identity-based and resource-based policies are a union](../facts/iam.md#iam-eval-same-account-identity-or-resource-allow).

**Predict 3:** No: across accounts, AWS [allows the request only if both evaluations return Allow](../facts/iam.md#iam-eval-cross-account-needs-both-policies).

</details>

## Recap from memory (1 min)
<!-- section: role=recap; route=fast; minutes=1 -->

**Recap 1.** What is the one-breath definition of IAM?

<details>
<summary>Answer</summary>

IAM decides who can do what in AWS. By default, [all requests are implicitly denied](../facts/iam.md#iam-eval-implicit-deny-by-default), and [an explicit deny overrides an explicit allow](../facts/iam.md#iam-eval-explicit-deny-overrides-allow).

</details>

**Recap 2.** Which two policies does every role have, and which question does each answer?

<details>
<summary>Answer</summary>

Trust policy: who can assume the role. Permissions policy: what the session can do.

</details>

**Recap 3.** Which service gives employees access to AWS when IAM users are not enough?

<details>
<summary>Answer</summary>

IAM Identity Center, the [recommended front door into AWS](../facts/iam.md#iam-idc-recommended-front-door-for-workforce).

</details>
