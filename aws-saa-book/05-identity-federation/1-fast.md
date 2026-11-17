---
id: "05"
slug: identity-federation
title: IAM Identity Center, Directory Service and Cognito
file: fast
tier: medium
domains: [1]
tasks: ["1.1", "1.2"]
services: [iam-identity-center, directory-service, cognito]
minutes: {fast: 12, pass: 53, full: 89}
status: ready
updated: 2026-10-12
---

# IAM Identity Center, Directory Service and Cognito

## Predict (1 min)
<!-- section: role=predict; route=fast; minutes=1 -->

**Predict 1.** Can a Cognito (cog-NEE-toh) **user pool** that trusts your corporate **identity provider** sign employees in to your AWS accounts? <!-- gist-trap -->

**Predict 2.** With AD Connector, where are the passwords of on-premises Active Directory users checked?

## Look first (1 min)
<!-- section: role=task; route=fast; minutes=1 -->

In AWS CloudShell, find the `AWSReservedSSO_` roles and any IAM users.

<!-- task:start id=identity-federation-t01 -->

Look

**It kills the belief.** "IAM Identity Center creates an IAM user for each employee."

> **Cost:** $0.

**Permissions.** `iam:ListRoles`, `iam:ListUsers`, `sso:ListInstances`

**No permission to create resources?** This task is read-only. It needs no alternative. If one step returns an access error, skip that step: the other steps still show the point.

1. Open AWS CloudShell. List the IAM roles whose names start with AWSReservedSSO_. IAM Identity Center made these roles when someone assigned a permission set to this account.

   ```bash
   aws iam list-roles --query "Roles[?starts_with(RoleName, 'AWSReservedSSO_')].RoleName"
   ```

   Expect: Zero or more role names that start with AWSReservedSSO_. Each one comes from a permission set assigned to this account. An empty list means that no permission set is assigned here.

2. List the IAM users of the same account. Compare the names with the people who sign in through the AWS access portal.

   ```bash
   aws iam list-users --query "Users[].UserName"
   ```

   Expect: A short list or an empty one. No IAM user was made for the people who sign in through IAM Identity Center: they reach the account through the AWSReservedSSO_ roles.

3. Ask IAM Identity Center for its instances. An empty list is a normal answer in many accounts.

   ```bash
   aws sso-admin list-instances --query "Instances[].[InstanceArn,IdentityStoreId,OwnerAccountId]"
   ```

   Expect: An instance ARN, an identity store ID and the owner account ID, or an empty list. The identity store holds the Identity Center users. An organization instance lives in the management account.

**Label.** checked against docs, not run in a real account. Checked 2026-10-13.

<!-- task:end -->

## In one breath (2 min)
<!-- section: role=breath; route=fast; minutes=2 -->

> **Say it:** IAM Identity Center signs employees in to AWS accounts. Cognito is [an identity platform for web and mobile apps](../facts/cognito.md#cognito-identity-platform-definition). Directory Service runs or connects AD.

**The problem it solves.** Without them, you manage access account by account, and each app stores passwords.

**Predict the picture.** Which path does an employee take?

<details>
<summary>Show the picture</summary>

![Two paths. Top: an employee signs in through an identity provider to IAM Identity Center, which opens a role in each assigned AWS account. Bottom: an app user signs in to a Cognito user pool, the app gets tokens, and an identity pool gives AWS credentials for Amazon S3.](../diagrams/svg/identity-federation-hero.svg)

**Figure.** Employees reach AWS accounts through IAM Identity Center; app users sign in to a Cognito user pool and reach AWS through an identity pool.

1. An employee signs in once through the identity provider to IAM Identity Center.
2. IAM Identity Center opens a role in each assigned AWS account, created from a permission set.
3. An app user signs in to a Cognito user pool, which issues JSON web tokens (JWTs) to the app.
4. An identity pool exchanges the token for temporary AWS credentials, and the app calls Amazon S3.

</details>

> **Startup example:** Callvale's 14 engineers need one sign-in for seven AWS accounts. The bank's 400 supervisors use bank identities; Callvale stores no passwords.

## Words that go together (1 min)
<!-- section: role=words; route=fast; minutes=1 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| identity provider (IdP) | **federate** with an identity provider | Checks who a person is | identity source |
| permission set | **assign** a permission set to a group for an account | Becomes a role in each account | **IAM role** |
| user pool | users **sign in** to a user pool | The user directory of your app | identity pool |
| identity pool | an identity pool **exchanges** a token for AWS credentials | Gives app users temporary AWS credentials | user pool |

## Choose it or not (2 min)
<!-- section: role=choose; route=fast; minutes=2 -->

### IAM Identity Center or Cognito

<!-- table: compare -->
| Question | IAM Identity Center | Cognito user pool | Cognito identity pool |
|---|---|---|---|
| Who signs in, to what? | Employees, to AWS accounts | Users, to your app | Nobody: it gives AWS credentials, also to [users who are guests (unauthenticated)](../facts/cognito.md#cognito-identity-pool-guest-and-authenticated-store) |
| What do they get? | A role in each assigned account | Tokens: they [issue JSON web tokens (JWTs)](../facts/cognito.md#cognito-user-pool-vs-identity-pool) | [Temporary, limited-privilege AWS credentials](../facts/cognito.md#cognito-user-pool-vs-identity-pool) |

**Deciding question:** Do people sign in to AWS accounts, or to an app that you build?

### AD Connector or AWS Managed Microsoft AD

<!-- table: compare -->
| Question | AD Connector | AWS Managed Microsoft AD | Simple AD |
|---|---|---|---|
| What is it? | [AD Connector is a proxy service](../facts/directory-service.md#directory-service-ad-connector-is-a-proxy) | [An actual Microsoft Windows Server Active Directory](../facts/directory-service.md#directory-service-managed-ad-actual-windows-server-ad) | [Powered by Samba 4](../facts/directory-service.md#directory-service-simple-ad-samba-4-basic-features); [no longer open to new customers](../facts/directory-service.md#directory-service-simple-ad-closed-to-new-customers) (not examinable yet) |
| Directory data in AWS? | None: it [does not replicate any of your directory data](../facts/directory-service.md#directory-service-ad-connector-no-data-replicated) | Yes, on at least [two domain controllers](../facts/directory-service.md#directory-service-managed-ad-minimum-two-domain-controllers) | Yes |
| Trust with on-premises Active Directory (AD)? | Not needed: it forwards sign-ins | Yes: [one and two-way external and forest trust relationships](../facts/directory-service.md#directory-service-trust-types-and-directions) | No: it [does not support multi-factor authentication (MFA), trust relationships](../facts/directory-service.md#directory-service-simple-ad-unsupported-features) |

**Deciding question:** Is sign-in to AWS applications the only need, or must a directory run in AWS?

## Signals and traps (2 min)
<!-- section: role=signals; route=fast; minutes=2 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "employees sign in to many AWS accounts" | IAM Identity Center | single sign-on [including any AWS accounts that are assigned](../facts/iam-identity-center.md#iam-identity-center-workforce-sso-to-accounts-and-applications) | an app you build: a Cognito user pool |
| "customers sign in with social or corporate accounts" | Cognito user pool | [customer identity and access management (CIAM)](../facts/cognito.md#cognito-decision-guide-ciam-for-apps-you-build) | they need AWS accounts: IAM Identity Center |
| "the REST API accepts only signed-in users" | `COGNITO_USER_POOLS` authorizer | you [let Amazon API Gateway validate the token](../facts/cognito.md#cognito-api-gateway-validates-user-pool-token) | requests signed with identity pool credentials: `AWS_IAM` |
| "users must stay in the on-premises Active Directory" | AD Connector | [AD Connector is a proxy service](../facts/directory-service.md#directory-service-ad-connector-is-a-proxy) | several forests: AWS Managed Microsoft AD, to [support multiple domains or forests](../facts/iam-identity-center.md#iam-identity-center-one-ad-directory-managed-ad-for-multiple-forests) |
| "run Active Directory-aware workloads in AWS" | AWS Managed Microsoft AD | chosen to [run Active Directory dependent workloads in AWS](../facts/directory-service.md#directory-service-decision-guide-ad-dependent-workloads-row) | sign-in to AWS apps only: AD Connector |
| "federate the directory to IAM roles in one account" | direct federation with IAM | [users assume IAM roles](../facts/iam-identity-center.md#iam-identity-center-decision-guide-federation-with-iam) in that account | many accounts: IAM Identity Center |

### Traps

- **Wrong belief:** A Cognito user pool can sign employees in to AWS accounts. **Truth:** Cognito is [not a supported identity source](../facts/iam-identity-center.md#iam-identity-center-cognito-is-not-an-identity-source) of IAM Identity Center. <!-- trap: identity-federation-trap-cognito-for-workforce -->
- **Wrong belief:** The app calls Amazon S3 with user pool tokens. **Truth:** An identity pool exchanges the token for [temporary, limited-privilege AWS credentials](../facts/cognito.md#cognito-user-pool-vs-identity-pool). <!-- trap: identity-federation-trap-user-pool-gives-aws-credentials -->
- **Wrong belief:** AD Connector copies users and passwords into AWS. **Truth:** It forwards sign-ins [without caching any information in the cloud](../facts/directory-service.md#directory-service-ad-connector-gateway-no-caching). <!-- trap: identity-federation-trap-ad-connector-stores-users -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2022-07-26) The name of the service.<br>
> **Old:** formerly AWS Single Sign-On.<br>
> **Now:** [AWS IAM Identity Center](../facts/iam.md#iam-change-sso-renamed-identity-center-2022).<br>
> **The exam probably expects:** IAM Identity Center; older questions use the old name.<br>
> **Status:** examinable.

## Check (1 min)
<!-- section: role=check; route=fast; minutes=1 -->

**Check 1.** Staff sign in with the corporate identity provider to an app their company built. IAM Identity Center or a Cognito user pool?

<details>
<summary>Answer</summary>

A Cognito user pool, for [workforce identities in SAML 2.0 and OIDC IdPs](../facts/cognito.md#cognito-user-pool-workforce-sso-in-your-app).

**Predict 1:** No: Cognito is [not a supported identity source](../facts/iam-identity-center.md#iam-identity-center-cognito-is-not-an-identity-source).

</details>

**Check 2.** An app holds user pool tokens and must write to Amazon S3. What is missing?

<details>
<summary>Answer</summary>

An identity pool, for [temporary, limited-privilege AWS credentials](../facts/cognito.md#cognito-user-pool-vs-identity-pool).

**Predict 2:** On premises: AD Connector [forwards sign-in requests to your on-premises Active Directory](../facts/directory-service.md#directory-service-ad-connector-is-a-proxy).

</details>

## Recap from memory (1 min)
<!-- section: role=recap; route=fast; minutes=1 -->

**Recap 1.** Which service signs people in to AWS accounts, and which to your app?

<details>
<summary>Answer</summary>

IAM Identity Center; Amazon Cognito.

</details>

**Recap 2.** Which Directory Service option runs an actual Active Directory?

<details>
<summary>Answer</summary>

AWS Managed Microsoft AD.

</details>

**Recap 3.** Which option forwards sign-ins to on-premises AD?

<details>
<summary>Answer</summary>

AD Connector.

</details>
