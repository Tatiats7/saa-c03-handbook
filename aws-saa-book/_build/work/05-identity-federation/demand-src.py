"""Builds brief.v0.json and mine-plan.json for chapter 05 (plan-05, 2026-10-12).

Run: python3 -I aws-saa-book/_build/work/05-identity-federation/demand-src.py
"""
import json, os, re, pathlib

ROOT = pathlib.Path("/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book")
W = ROOT / "_build/work/05-identity-federation"
SNAP = ROOT / "_build/corpus/snap"

IC = "docs/singlesignon/latest/userguide/"
DS = "docs/directoryservice/latest/admin-guide/"
CG = "docs/cognito/latest/developerguide/"
DG = "docs/decision-guides/latest/decision-guides/identity-on-aws-how-to-choose"
WA1 = "docs/wellarchitected/latest/security-pillar/identity-management"
WA2 = "docs/wellarchitected/latest/security-pillar/sec_identities_identity_provider"
SRA = "docs/prescriptive-guidance/latest/security-reference-architecture/introduction"
FAQ_IC = "www/iam/identity-center/faqs"
FAQ_DS = "www/directoryservice/faqs"
FAQ_CG = "www/cognito/faqs"
PR_DS = "www/directoryservice/pricing"
PR_CG = "www/cognito/pricing"
H_IC = IC + "doc-history"
H_DS = DS + "document_history"
H_CG = CG + "cognito-document-history"
Q_IC = IC + "limits"
Q_MAD = DS + "ms_ad_limits"
Q_ADC = DS + "ad_connector_limits"
Q_SAD = DS + "simple_ad_limits"
Q_CG = CG + "quotas"
ELB_AUTH = "docs/elasticloadbalancing/latest/application/listener-authenticate-users"
APIGW_AUTH = "docs/apigateway/latest/developerguide/apigateway-integrate-with-cognito"
IAM_OIDC = "docs/IAM/latest/UserGuide/id_roles_providers_oidc"
FSXW_AD = "docs/fsx/latest/WindowsGuide/aws-ad-integration-fsxW"

N, B, F = "numbers+changes", "behavior+decisions", "faq"

# (id, bullet, lens, kind, question, sources, existing_facts)
D = [
 # ---------- IAM Identity Center: numbers and defaults ----------
 ("d001", "1.1.K2", N, "number", "How many AWS accounts and how many applications can one IAM Identity Center instance configure by default, and can these quotas be increased?", [Q_IC], ["iam-identity-center-quota-accounts-or-applications"]),
 ("d002", "1.1.K2", N, "number", "How many users and groups does the IAM Identity Center identity store support by default?", [Q_IC], ["iam-identity-center-quota-users", "iam-identity-center-quota-groups"]),
 ("d003", "1.1.K2", N, "number", "How many permission sets per instance, provisioned permission sets per account, inline policies and managed policies per permission set does IAM Identity Center allow?", [Q_IC, IC + "permissionsetsconcept"], ["iam-identity-center-quota-permission-sets", "iam-identity-center-quota-provisioned-permission-sets-per-account", "iam-identity-center-quota-inline-policy-per-permission-set"]),
 ("d004", "1.2.S3", N, "default", "What is the default session duration of a permission set (the role session in the AWS account), and what range can it be set to?", [IC + "howtosessionduration"], ["iam-identity-center-permission-set-session-duration"]),
 ("d005", "1.2.S3", N, "default", "What is the default and the allowed range of the AWS access portal (user interactive) session duration?", [IC + "configure-user-session", IC + "authconcept"], []),
 ("d006", "1.1.K2", N, "number", "How long are the AWS CLI credentials that a user gets from the AWS access portal valid?", [FAQ_IC, IC + "howtogetcredentials"], []),
 ("d007", "1.1.K2", N, "restriction", "How many identity sources can be connected to IAM Identity Center at one time?", [IC + "manage-your-identity-source", FAQ_IC], ["iam-identity-center-one-identity-source-at-a-time"]),
 ("d008", "1.1.K2", N, "restriction", "How many IAM Identity Center instances can an account have, and in which account must an organization instance be enabled?", [Q_IC, IC + "organization-instances-identity-center", IC + "identity-center-instances"], ["iam-identity-center-quota-one-instance-per-account"]),
 ("d009", "1.1.K2", N, "change", "HYPOTHESIS (FRESHNESS): IAM Identity Center became multi-Region on 2026-02-02 (expanded 2026-07-28 to the Identity Center directory, 2026-08-06 one-click, 2026-09-30 more Regions). What does an additional Region provide (account access, applications, failover), what does it require, and which parts are GA after 2026-07-15 (not examinable yet)?", [IC + "multi-region-iam-identity-center", IC + "resiliency-regional-behavior", H_IC], []),
 ("d010", "1.2.S3", N, "change", "HYPOTHESIS: the maximum AWS access portal session duration increased from 7 days to 90 days on 2023-09-12. Confirm old value, new value and date.", [H_IC, IC + "configure-user-session"], []),
 ("d011", "1.1.K2", N, "change", "AWS Single Sign-On was renamed AWS IAM Identity Center on 2022-07-26. Confirm the rename statement and date (former name may appear once).", [H_IC, IC + "what-is"], []),
 ("d012", "1.1.K2", N, "change", "When were account instances of IAM Identity Center introduced (2023-11-17 hypothesis), and what are they for?", [IC + "account-instances-identity-center", H_IC], []),
 ("d013", "1.1.K2", N, "change", "HYPOTHESIS: on 2026-06-22 the single quota for accounts plus applications became separate quotas (7,000 each). What was the old combined quota?", [H_IC, Q_IC], ["iam-identity-center-quota-accounts-or-applications"]),
 ("d014", "1.1.K2", N, "change", "HYPOTHESIS: since 2026-08-04 management of AWS account access is optional for new organization instances. Confirm; GA after 2026-07-15, so label not examinable yet.", [H_IC, IC + "enable-identity-center"], []),
 ("d015", "1.2.S3", N, "change", "Since when (2025-09-17 hypothesis) can an organization instance use a customer managed KMS key for encryption at rest, and what does it encrypt?", [IC + "identity-center-customer-managed-keys", IC + "encryption-at-rest", H_IC], []),
 ("d016", "1.1.S6", N, "change", "HYPOTHESIS: IAM Identity Center AD Sync was deprecated on 2025-04-17 in favour of configurable AD sync. What does configurable AD sync do?", [H_IC, IC + "provision-users-from-ad-configurable-ADsync"], []),
 ("d017", "1.2.S3", N, "change", "What MFA default do new IAM Identity Center instances get (change 2023-11-16 hypothesis)?", [IC + "enable-mfa", IC + "mfa-types", H_IC], []),
 ("d018", "1.1.K2", N, "change", "Since 2022-07-14 permission sets can use customer managed policies and permissions boundaries. Confirm and state the rule that the customer managed policy must exist in each account.", [H_IC, IC + "howtocmp", IC + "permissionsetsconcept"], []),
 ("d019", "1.1.K2", N, "pricing", "What does IAM Identity Center cost?", [FAQ_IC], ["iam-identity-center-no-extra-charge"]),
 # ---------- Directory Service: numbers and changes ----------
 ("d020", "1.1.S6", N, "default", "How many domain controllers does AWS Managed Microsoft AD create by default, where are they placed, and what is the maximum per directory?", [DS + "directory_microsoft_ad", DS + "ms_ad_getting_started_what_gets_created", Q_MAD, FAQ_DS], []),
 ("d021", "1.1.S6", N, "number", "What are the Standard and Enterprise Editions of AWS Managed Microsoft AD sized for (objects, users), per the FAQ and guide?", [FAQ_DS, DS + "directory_microsoft_ad"], []),
 ("d022", "1.1.S6", N, "number", "What is the default quota of AWS Managed Microsoft AD directories per account (Standard and Enterprise; Hybrid Edition)?", [Q_MAD], []),
 ("d023", "1.1.S6", N, "number", "How many accounts can a directory be shared with (Standard, Enterprise, Hybrid)? HYPOTHESIS: sharing limits increased on 2025-08-15; find the old values only if stated.", [Q_MAD, DS + "ms_ad_directory_sharing"], []),
 ("d024", "1.1.S6", N, "restriction", "Which edition supports multi-Region replication, and how many Regions can one directory span? (2026-04-01: opt-in Regions added.)", [DS + "ms_ad_configure_multi_region_replication", Q_MAD, FAQ_DS], []),
 ("d025", "1.1.S6", N, "number", "How many manual snapshots per Managed Microsoft AD directory, and how old can a manual snapshot be?", [Q_MAD], []),
 ("d026", "1.1.S6", N, "number", "What sizes does AD Connector come in, what is each sized for, and what is the default quota of AD Connector directories?", [DS + "directory_ad_connector", Q_ADC], []),
 ("d027", "1.1.S6", N, "number", "What sizes does Simple AD come in (users, objects) and what is its directory quota?", [DS + "directory_simple_ad", Q_SAD], []),
 ("d028", "1.1.S6", N, "change", "HYPOTHESIS (FRESHNESS): Simple AD availability change announced 2026-06-30; since 2026-07-30 Simple AD is no longer open to new customers. What can existing customers still do, and which alternatives does AWS name?", [DS + "simple-ad-availability-change", H_DS], []),
 ("d029", "1.1.S6", N, "change", "Can a Managed Microsoft AD directory be upgraded from Standard to Enterprise Edition? (API 2025-10-02; console 2026-07-30 is after the cutoff.) Can it be downgraded?", [DS + "ms_ad_upgrade_edition", H_DS], []),
 ("d030", "1.1.S6", N, "change", "What is AWS Managed Microsoft AD (Hybrid Edition), added 2025-07-30?", [DS + "aws-hybrid-directory", H_DS], []),
 ("d031", "1.1.S6", N, "pricing", "What are the pricing dimensions of AWS Directory Service (Managed AD per edition and domain controller hour, extra domain controllers, directory sharing, AD Connector size, free trial)?", [PR_DS, FAQ_DS], []),
 # ---------- Cognito: numbers and changes ----------
 ("d032", "1.2.K5", N, "number", "What are the key user pool resource quotas: user pools per Region, app clients per pool, identity providers per pool, groups per pool, groups per user?", [Q_CG], []),
 ("d033", "1.2.K4", N, "default", "What are the default and allowed validity periods of the ID token, the access token and the refresh token in a user pool?", [Q_CG, CG + "amazon-cognito-user-pools-using-the-refresh-token"], []),
 ("d034", "1.2.K5", N, "number", "What are the identity pool resource quotas (identity pools per account, identity providers per pool, role mapping rules)?", [Q_CG], []),
 ("d035", "1.2.K4", N, "number", "Which user pool API request-rate quotas matter (for example UserAuthentication RPS), are they adjustable, and what is provisioned capacity (2024-01-25; self-service 2026-07-02)?", [Q_CG, H_CG], []),
 ("d036", "1.2.K5", N, "pricing", "How are Cognito user pools priced (monthly active users, feature plans Lite / Essentials / Plus, SAML or OIDC federated users, machine-to-machine), and what is in the free tier?", [PR_CG, FAQ_CG, CG + "cognito-sign-in-feature-plans"], []),
 ("d037", "1.2.K5", N, "change", "HYPOTHESIS: feature plans Lite, Essentials and Plus replaced the old pricing model on 2024-11-22, together with managed login and passwordless sign-in. Which features need Essentials and which need Plus?", [CG + "cognito-sign-in-feature-plans", CG + "feature-plans-features-essentials", CG + "feature-plans-features-plus", H_CG], []),
 ("d038", "1.2.K4", N, "change", "HYPOTHESIS: user pool multi-Region replication arrived 2026-05-28 (What's New 2026-06-04). What is replicated, how does failover work, and which plan does it need?", [CG + "user-pool-multi-region", H_CG, FAQ_CG], []),
 ("d039", "1.2.K4", N, "change", "Since 2026-05-28 can a user pool use a customer managed KMS key for encryption at rest?", [H_CG, CG + "data-protection"], []),
 ("d040", "1.2.K5", N, "change", "HYPOTHESIS: Amazon Cognito Sync is no longer open to new customers since 2026-07-30. Which services does AWS name instead?", [CG + "cognito-sync-availability-change", H_CG, FAQ_CG], []),
 ("d041", "1.2.S3", N, "change", "Since when can AWS WAF protect a user pool (2022-08 hypothesis) and managed login (2025-06-24)? Which endpoints does the web ACL cover?", [CG + "user-pool-waf", H_CG], []),
 ("d042", "1.2.K4", N, "change", "Refresh token rotation (2025-04-22): what changes when it is on?", [CG + "amazon-cognito-user-pools-using-the-refresh-token", H_CG], []),
 ("d043", "1.2.K4", N, "change", "AWS PrivateLink for user pools (2025-11-04) and identity pools (2025-12-10): which operations can go through an interface endpoint?", [CG + "vpc-interface-endpoints", H_CG], []),
 ("d044", "1.2.K4", N, "change", "Which MFA factors do user pools support now (SMS, TOTP, email since 2024-09), and what plan does email MFA need?", [CG + "user-pool-settings-mfa", H_CG], []),
 ("d045", "1.2.K4", N, "change", "What does user pool deletion protection do (2022-10-20)?", [CG + "user-pool-settings-deletion-protection", H_CG], []),
 ("d046", "1.2.K4", N, "change", "Can users be imported with their password hashes (history 2026-07-13, What's New 2026-07-15: borderline cutoff)? Before that, could imported users keep their passwords?", [CG + "cognito-user-pools-import-users", H_CG], []),
 # ---------- IAM Identity Center: behavior and decisions ----------
 ("d050", "1.1.K2", B, "behavior", "What is IAM Identity Center in one sentence: workforce single sign-on to AWS accounts and applications?", [IC + "what-is", FAQ_IC], ["iam-identity-center-workforce-sso-to-accounts-and-applications"]),
 ("d051", "1.1.S6", B, "behavior", "Does IAM Identity Center create IAM users? What does it create in each member account when a permission set is assigned (IAM roles, the reserved AWSReservedSSO_ name)?", [IC + "identity-center-and-iam-roles", IC + "permissionsetsconcept", FAQ_IC], ["iam-identity-center-creates-roles-per-permission-set-not-iam-users"]),
 ("d052", "1.1.K2", B, "behavior", "What is a permission set, what can it contain (AWS managed, customer managed and inline policies, permissions boundary), and what happens when it is changed after assignment?", [IC + "permissionsetsconcept", IC + "howtocmp"], []),
 ("d053", "1.1.K2", B, "comparison", "Organization instance vs account instance: which one can grant access to AWS accounts, and what are account instances limited to?", [IC + "identity-center-instances", IC + "organization-instances-identity-center", IC + "account-instances-identity-center"], []),
 ("d054", "1.1.K2", B, "restriction", "Does multi-account access need AWS Organizations, where is the organization instance enabled, and can a member account be the delegated administrator (and what can it not manage)?", [IC + "identity-center-and-orgs", IC + "delegated-admin", IC + "identity-center-prerequisites"], ["iam-identity-center-delegated-admin-not-management-account"]),
 ("d055", "1.1.K2", B, "capability", "Which identity sources can IAM Identity Center use (Identity Center directory, Active Directory, external SAML 2.0 IdP), and what changes when the source changes?", [IC + "manage-your-identity-source", IC + "manage-your-identity-source-considerations", IC + "confirm-identity-source"], ["iam-identity-center-one-identity-source-at-a-time"]),
 ("d056", "1.1.S6", B, "capability", "How does IAM Identity Center use an on-premises Active Directory: through AD Connector or through AWS Managed Microsoft AD with a trust? What is needed for each?", [IC + "manage-your-identity-source-ad", IC + "connectonpremad", IC + "connectawsad", FAQ_IC], []),
 ("d057", "1.1.K2", B, "behavior", "With an external IdP (Okta, Microsoft Entra ID), what does SAML 2.0 do and what does SCIM provisioning do? Are users created automatically without SCIM?", [IC + "other-idps", IC + "provision-automatically", FAQ_IC], []),
 ("d058", "1.2.K5", B, "restriction", "Can a Cognito user pool be the identity source of IAM Identity Center?", [FAQ_IC], ["iam-identity-center-cognito-is-not-an-identity-source"]),
 ("d059", "1.1.K2", B, "capability", "How does ABAC work with IAM Identity Center (attributes for access control passed as session tags)?", [IC + "abac", IC + "attributesforaccesscontrol"], []),
 ("d060", "1.1.K2", B, "behavior", "In which Region does IAM Identity Center keep its data, what happens to sign-in if that Region is impaired, and what emergency access path does AWS recommend?", [IC + "regions", IC + "resiliency-regional-behavior", IC + "emergency-access", IC + "disaster-recovery-resiliency"], []),
 ("d061", "1.2.S3", B, "capability", "Which MFA types does IAM Identity Center support (authenticator apps, FIDO2 security keys and passkeys, built-in authenticators, RADIUS MFA for AD)?", [IC + "mfa-types", IC + "enable-mfa", FAQ_IC], []),
 ("d062", "1.1.K2", B, "behavior", "How do engineers use the AWS CLI with IAM Identity Center without long-term access keys (aws configure sso, short-term credentials)?", [IC + "howtogetcredentials", IC + "integrating-aws-cli"], []),
 ("d063", "1.2.S3", B, "capability", "Can IAM Identity Center give single sign-on to SAML 2.0 business applications (Salesforce, Microsoft 365) and to OIDC applications?", [IC + "customermanagedapps", IC + "awsapps", FAQ_IC], []),
 ("d064", "1.2.S3", B, "behavior", "What is trusted identity propagation, in one sentence, and which services use it (Redshift, Athena, S3 Access Grants, Lake Formation)?", [IC + "trustedidentitypropagation-overview", FAQ_IC], []),
 ("d065", "1.2.S3", B, "behavior", "When an assignment is removed or a user is disabled, do active sessions end at once? How does a Deny policy revoke active permissions?", [IC + "authconcept", IC + "revoke-user-permissions", IC + "prereqs-revoking-user-permissions", IC + "disableuser"], []),
 ("d066", "1.1.S6", B, "comparison", "IAM Identity Center vs direct SAML federation into IAM roles in each account (IAM identity providers): when is each the right answer?", [DG, IC + "what-is", "docs/IAM/latest/UserGuide/id_roles_providers_saml"], []),
 ("d067", "1.2.K5", B, "comparison", "IAM Identity Center vs Amazon Cognito: workforce users vs customer (application) users. What does the decision guide say?", [DG, CG + "what-is-amazon-cognito", FAQ_IC], ["iam-identity-center-cognito-is-not-an-identity-source"]),
 ("d068", "1.1.K2", B, "decision", "What categories does the AWS identity decision guide use (workforce identity, customer identity, permissions for workloads) and which service does it name for each?", [DG], []),
 ("d069", "1.1.K2", B, "decision", "What does the Well-Architected security pillar recommend about a centralized identity provider (SEC02-BP04) and about identity management?", [WA2, WA1, SRA], []),
 ("d070", "1.1.K2", B, "behavior", "What can a temporary elevated access (just-in-time) setup do with IAM Identity Center, and is it built in or provided by partners?", [IC + "temporary-elevated-access"], []),
 # ---------- Directory Service: behavior and decisions ----------
 ("d071", "1.1.S6", B, "behavior", "What is AWS Directory Service and which directory types does it offer (AWS Managed Microsoft AD, AD Connector, Simple AD)?", [DS + "what_is", FAQ_DS], []),
 ("d072", "1.1.S6", B, "behavior", "What is AWS Managed Microsoft AD (actual Microsoft AD on Windows Server, managed by AWS), and which admin rights do you get or not get (no Domain Admin)?", [DS + "directory_microsoft_ad", DS + "ms_ad_getting_started_admin_account", FAQ_DS], []),
 ("d073", "1.1.S6", B, "capability", "Which trust relationships can Managed Microsoft AD create with a self-managed AD (one-way, two-way, forest, external), and what network connectivity do they need?", [DS + "ms_ad_setup_trust", DS + "ms_ad_connect_existing_infrastructure", FAQ_DS], []),
 ("d074", "1.1.S6", B, "behavior", "What is AD Connector: a proxy that redirects directory requests to an on-premises AD without caching any information in the cloud? What does it need (VPN or Direct Connect, service account)?", [DS + "directory_ad_connector", DS + "ad_connector_getting_started"], []),
 ("d075", "1.1.S6", B, "restriction", "What can AD Connector not do (share the directory with other accounts, trusts, schema extensions, store users)? Which AWS applications work with it?", [DS + "directory_ad_connector", DS + "ad_connector_app_compatibility"], []),
 ("d076", "1.1.S6", B, "behavior", "What is Simple AD (Samba 4 based, AD-compatible), and which features does it not support (trusts, MFA, schema extensions, PowerShell)?", [DS + "directory_simple_ad", DS + "simple_ad_app_compatibility"], []),
 ("d077", "1.1.S6", B, "capability", "Which directory types support seamless domain join of EC2 Windows and Linux instances?", [DS + "ms_ad_join_instance", DS + "ad_connector_join_instance", FAQ_DS], []),
 ("d078", "1.1.S6", B, "capability", "Can a Managed Microsoft AD directory be shared with other accounts (AWS Organizations or handshake), and which directory types cannot be shared?", [DS + "ms_ad_directory_sharing", FAQ_DS], []),
 ("d079", "1.1.S6", B, "behavior", "What does multi-Region replication of Managed Microsoft AD replicate, and which settings are global vs Regional?", [DS + "ms_ad_configure_multi_region_replication", DS + "multi-region-global-region-features", FAQ_DS], []),
 ("d080", "1.1.S6", B, "behavior", "How do AD users sign in to the AWS Management Console with a Directory Service directory (access URL plus IAM roles assigned to AD users or groups)? This is 'federate a directory service with IAM roles'.", [DS + "ms_ad_management_console_access", DS + "ms_ad_manage_roles", FAQ_DS], []),
 ("d081", "1.1.S6", B, "capability", "Which AWS applications and services need or use a directory (WorkSpaces, FSx for Windows File Server, RDS for SQL Server, QuickSight, IAM Identity Center), and which directory types does each accept?", [DS + "ms_ad_app_compatibility", DS + "ad_connector_app_compatibility", DS + "simple_ad_app_compatibility", FSXW_AD], []),
 ("d082", "1.2.S3", B, "capability", "How is MFA added to Managed Microsoft AD and AD Connector (RADIUS server)?", [DS + "ms_ad_mfa", DS + "ad_connector_mfa"], []),
 ("d083", "1.1.S6", B, "comparison", "Managed Microsoft AD vs Active Directory on your own EC2 instances: what does AWS manage, what can you not do (schema extensions allowed, no Domain Admin), when to choose self-managed?", [FAQ_DS, DS + "ms_ad_best_practices", DS + "ms_ad_key_concepts"], []),
 ("d084", "1.1.S6", B, "capability", "Can Managed Microsoft AD be the primary directory or a resource forest, and how are on-premises users migrated (ADMT)?", [FAQ_DS, DS + "ms_ad_migrate_users"], []),
 ("d085", "1.1.S6", B, "comparison", "AD Connector vs Managed Microsoft AD vs Simple AD: which stem signals point to each ('users must stay on premises', 'AD-aware apps in AWS with a trust', 'small, low-cost, basic')? Use the guide's 'choose' text; Simple AD now closed to new customers.", [DS + "what_is", DS + "directory_ad_connector", DS + "directory_microsoft_ad", DS + "directory_simple_ad", DG], []),
 ("d086", "1.1.S6", B, "behavior", "Do directory domain controllers run in your VPC, which subnets and Availability Zones do they need, and what security group does Directory Service create?", [DS + "ms_ad_getting_started", DS + "ms_ad_getting_started_what_gets_created", DS + "create_details_ad_connector"], []),
 ("d087", "1.1.S6", B, "capability", "Can Managed Microsoft AD provide SAML-based single sign-on to cloud applications such as Microsoft 365 (through IAM Identity Center)?", [DS + "usecase4", FAQ_DS], []),
 # ---------- Cognito: behavior and decisions ----------
 ("d090", "1.2.K5", B, "behavior", "What is a user pool (user directory and OIDC identity provider that issues JWTs) and what is an identity pool (exchanges identities for temporary AWS credentials)?", [CG + "what-is-amazon-cognito", CG + "cognito-user-pools", CG + "cognito-identity", FAQ_CG], ["cognito-user-pool-vs-identity-pool"]),
 ("d091", "1.2.K4", B, "capability", "Can an identity pool give guest (unauthenticated) users AWS credentials, and how are authenticated and unauthenticated roles used?", [CG + "iam-roles", CG + "identity-pools", FAQ_CG], ["cognito-identity-pool-guest-credentials"]),
 ("d092", "1.2.K4", B, "decision", "When are a user pool and an identity pool used together, and when is each enough alone?", [CG + "cognito-scenarios", CG + "amazon-cognito-integrating-user-pools-with-identity-pools"], ["cognito-pools-used-together-or-alone"]),
 ("d093", "1.2.K4", B, "capability", "Which third-party IdPs can a user pool federate (social: Google, Facebook, Apple, Amazon; SAML 2.0; OIDC), and does the app or Cognito store the federated user's password?", [CG + "cognito-user-pools-identity-federation", CG + "cognito-user-pools-identity-provider", FAQ_CG], []),
 ("d094", "1.2.K4", B, "capability", "SAML providers in a user pool: SP-initiated and IdP-initiated sign-in, signing and encryption (2024-02-01). What must the enterprise IdP be configured with?", [CG + "cognito-user-pools-saml-idp", CG + "cognito-user-pools-saml-idp-things-to-know"], []),
 ("d095", "1.2.S3", B, "behavior", "How does an API Gateway REST API use a Cognito user pool authorizer (which token, which header), and can API Gateway authorize with IAM using identity pool credentials?", [CG + "user-pool-accessing-resources-api-gateway-and-lambda", APIGW_AUTH], []),
 ("d096", "1.2.S3", B, "capability", "Can an Application Load Balancer authenticate users through a Cognito user pool before forwarding the request (authenticate-cognito action), and which listener protocol does it need?", [ELB_AUTH], []),
 ("d097", "1.2.K4", B, "behavior", "How does an identity pool choose the IAM role (default roles, rules-based mapping from claims, token-based roles from user pool groups with cognito:preferred_role)?", [CG + "role-based-access-control", CG + "iam-roles"], []),
 ("d098", "1.2.K4", B, "capability", "How does an identity pool support ABAC (attributes for access control mapped to principal tags)?", [CG + "attributes-for-access-control"], []),
 ("d099", "1.2.K4", B, "restriction", "What must an identity pool role trust policy contain (cognito-identity.amazonaws.com principal, aud and amr conditions), per the 2025-08-01 update?", [CG + "iam-roles", CG + "identity-pools-security-best-practices", H_CG], []),
 ("d100", "1.2.K4", B, "capability", "Which Lambda triggers can customize user pool flows (pre sign-up, pre authentication, pre token generation, user migration, custom auth challenge, inbound federation 2026-01-28)?", [CG + "cognito-user-pools-working-with-lambda-triggers"], []),
 ("d101", "1.2.K4", B, "comparison", "How are existing users migrated into a user pool: user migration Lambda trigger (users keep passwords, migrate at sign-in) vs CSV import (users reset passwords)?", [CG + "cognito-user-pools-import-users", CG + "user-pool-lambda-migrate-user", FAQ_CG], []),
 ("d102", "1.2.K4", B, "capability", "What does threat protection do (compromised-credentials detection, adaptive authentication), and which feature plan does it need?", [CG + "cognito-user-pool-settings-threat-protection", CG + "managing-security", CG + "feature-plans-features-plus"], []),
 ("d103", "1.2.K4", B, "capability", "What is managed login (formerly hosted UI), and can a user pool use a custom domain with an ACM certificate?", [CG + "cognito-user-pools-managed-login", CG + "cognito-user-pools-add-custom-domain"], []),
 ("d104", "1.2.K4", B, "capability", "How does machine-to-machine authorization work in a user pool (client credentials grant, resource servers, custom scopes)?", [CG + "cognito-user-pools-define-resource-servers", CG + "authentication"], []),
 ("d105", "1.2.K4", B, "behavior", "Which token does an app send to an API (access token vs ID token), and how can tokens be revoked?", [CG + "amazon-cognito-user-pools-using-the-access-token", CG + "amazon-cognito-user-pools-using-the-id-token", CG + "token-revocation"], []),
 ("d106", "1.2.K5", B, "comparison", "Ben's question: what is the difference between IAM Identity Center and Cognito? Collect one clean sentence each from the guides (workforce access to AWS accounts vs sign-in for application customers).", [IC + "what-is", CG + "what-is-amazon-cognito", DG], []),
 ("d107", "1.2.K4", B, "decision", "Why should a mobile or web app never embed long-term AWS keys, and what does AWS recommend instead (Cognito identity pool temporary credentials)?", [CG + "cognito-identity", FAQ_CG, IAM_OIDC], []),
 ("d108", "1.1.K2", B, "comparison", "Web identity federation with AssumeRoleWithWebIdentity directly vs through a Cognito identity pool: what does the IAM guide recommend?", [IAM_OIDC, CG + "authentication-flow"], []),
 ("d109", "1.2.K4", B, "decision", "Multi-tenant apps: per-tenant user pools vs app clients vs groups vs custom attributes. What does the guide say decides between them?", [CG + "multi-tenant-application-best-practices"], []),
 ("d110", "1.2.K4", B, "capability", "How do user pool groups carry an IAM role that an identity pool can use (precedence)?", [CG + "cognito-user-pools-user-groups", CG + "role-based-access-control"], []),
 ("d111", "1.2.K4", B, "behavior", "What is the identity pool authentication flow (enhanced vs basic), and which STS call issues the credentials?", [CG + "authentication-flow", CG + "getting-credentials"], []),
 # ---------- Callvale decision facts ----------
 ("d120", "1.1.K2", B, "decision", "Callvale: can IAM Identity Center give 14 engineers one sign-in to 7 accounts with only short-term credentials (no IAM users, no access keys)? Facts: permission sets, access portal, CLI short-term credentials.", [IC + "what-is", IC + "useraccess", IC + "howtogetcredentials"], []),
 ("d121", "1.2.K4", B, "decision", "Callvale: can a Cognito user pool federate the bank's SAML IdP so that Callvale never stores the 400 supervisors' passwords, and how are federated users billed (MAU of SAML/OIDC users)?", [CG + "cognito-user-pools-saml-idp", CG + "cognito-user-pools-identity-federation", PR_CG], []),
 ("d122", "1.1.K2", B, "decision", "Callvale accepts 'all access depends on the identity provider; one tested emergency path'. What emergency access does the IAM Identity Center guide recommend when the IdP or Identity Center is unavailable?", [IC + "emergency-access", IC + "resiliency-regional-behavior"], []),
 ("d123", "1.1.S6", B, "decision", "Callvale stage 4 (Peldon): Windows servers and FSx for Windows File Server need Active Directory. Which directory type fits when Peldon's on-premises AD must keep working until month 31 (Managed AD with a trust vs AD Connector)?", [DS + "usecase5", DS + "ms_ad_setup_trust", FSXW_AD], []),
 # ---------- Real world ----------
 ("d130", "1.2.K5", B, "case", "Dynata case study: what did Dynata use Amazon Cognito for, and which numbers does the page state (200 websites)?", ["www/solutions/case-studies/dynata-amazon-cognito-case-study"], []),
 ("d131", "1.1.K2", B, "case", "Behavox or Sophos case study: how did a company use IAM Identity Center (formerly AWS SSO) and Organizations for workforce access, and which numbers are stated?", ["www/solutions/case-studies/behavox-case-study", "www/solutions/case-studies/sophos"], []),
 ("d132", "1.1.S6", B, "case", "Banco Davivienda case study: how was AWS Directory Service used (with Amazon WorkSpaces), and which numbers are stated?", ["www/solutions/case-studies/davivienda-case-study"], []),
 # ---------- FAQ quick-fire ----------
 ("d140", "1.1.K2", F, "faq", "IdC FAQ: Will enabling IAM Identity Center modify any existing IAM roles, users or policies?", [FAQ_IC], []),
 ("d141", "1.1.K2", F, "faq", "IdC FAQ: Can I connect more than one identity source?", [FAQ_IC], ["iam-identity-center-one-identity-source-at-a-time"]),
 ("d142", "1.1.K2", F, "faq", "IdC FAQ: Does IAM Identity Center create IAM users and groups in my accounts?", [FAQ_IC], ["iam-identity-center-creates-roles-per-permission-set-not-iam-users"]),
 ("d143", "1.1.K2", F, "faq", "IdC FAQ: Which AWS accounts can I connect (accounts in the organization)?", [FAQ_IC], []),
 ("d144", "1.1.K2", F, "faq", "IdC FAQ: Can I migrate gradually, and how do existing roles move?", [FAQ_IC], []),
 ("d145", "1.2.S3", F, "faq", "IdC FAQ: Does IAM Identity Center support single sign-on to native mobile and desktop applications?", [FAQ_IC], []),
 ("d146", "1.2.S3", F, "faq", "IdC FAQ: What data does IAM Identity Center store, and how is it encrypted?", [FAQ_IC], []),
 ("d147", "1.1.S6", F, "faq", "DS FAQ: Can I configure the storage, CPU or memory of a Managed Microsoft AD directory?", [FAQ_DS], []),
 ("d148", "1.1.S6", F, "faq", "DS FAQ: Does Managed Microsoft AD support schema extensions?", [FAQ_DS], []),
 ("d149", "1.1.S6", F, "faq", "DS FAQ: Can I add domain controllers manually?", [FAQ_DS], []),
 ("d150", "1.1.S6", F, "faq", "DS FAQ: How are Managed Microsoft AD directories deployed (Availability Zones, domain controllers)?", [FAQ_DS], []),
 ("d151", "1.1.S6", F, "faq", "DS FAQ: How does Directory Service enable single sign-on to the AWS Management Console?", [FAQ_DS], []),
 ("d152", "1.1.S6", F, "faq", "DS FAQ: Can I use Microsoft 365 with users managed in Managed Microsoft AD?", [FAQ_DS], []),
 ("d153", "1.1.S6", F, "faq", "DS FAQ: Can I encrypt LDAP traffic (LDAPS) between applications and Managed Microsoft AD?", [FAQ_DS], []),
 ("d154", "1.2.K5", F, "faq", "Cognito FAQ: What is a user pool?", [FAQ_CG], []),
 ("d155", "1.2.K5", F, "faq", "Cognito FAQ: Can I set password policies?", [FAQ_CG], []),
 ("d156", "1.2.K4", F, "faq", "Cognito FAQ: How can I keep authentication available during a Regional disruption, and what happens to users during failover?", [FAQ_CG], []),
 ("d157", "1.2.K4", F, "faq", "Cognito FAQ: When using public identity providers, does Cognito identity pools store users' credentials?", [FAQ_CG], []),
 ("d158", "1.2.K4", F, "faq", "Cognito FAQ: What are unauthenticated users?", [FAQ_CG], []),
 ("d159", "1.2.K5", F, "faq", "Cognito FAQ: What are monthly active users (MAUs), and is Cognito in the AWS Free Tier?", [FAQ_CG], []),
 ("d160", "1.2.K5", F, "faq", "Cognito FAQ: What is the Amazon Cognito sync store (and its current status)?", [FAQ_CG], []),
 ("d161", "1.2.K4", F, "faq", "Cognito FAQ: Can I remember the devices of my users in a user pool?", [FAQ_CG], []),
]

ids = [d[0] for d in D]
assert len(ids) == len(set(ids)), "duplicate demand id"

def exists(sid):
    return (SNAP / (sid + ".txt")).exists()

# URLs selected for this chapter
url_files = ["urls-1.txt", "urls-2.txt"]
urls = []
for f in url_files:
    for line in open(W / f):
        u = line.strip()
        if u and u not in urls:
            urls.append(u)

def sid_for(u):
    if u.startswith("https://docs.aws.amazon.com/"):
        return "docs/" + re.sub(r"\.html$", "", u[len("https://docs.aws.amazon.com/"):])
    if u.startswith("https://aws.amazon.com/"):
        return "www/" + u[len("https://aws.amazon.com/"):].rstrip("/")
    return u

fetched = [sid_for(u) for u in urls if exists(sid_for(u))]
not_yet = [sid_for(u) for u in urls if not exists(sid_for(u))]
registry_required = [FAQ_IC, FAQ_DS, FAQ_CG, H_IC, H_DS, H_CG, Q_IC, Q_MAD, Q_ADC, Q_SAD, Q_CG, PR_DS, PR_CG, DG, WA1, WA2, SRA]
# also count cached FAQ snapshots that are not in the url lists
for s in registry_required:
    if exists(s) and s not in fetched:
        fetched.append(s)

failures = []
fr = W / "fetch-2.txt"
if fr.exists():
    for line in open(fr):
        if line.startswith("error"):
            parts = line.split(None, 2)
            failures.append({"url": parts[1] if len(parts) > 1 else line.strip(), "reason": line.strip()})
for s in registry_required:
    if not exists(s) and not any(s in f["url"] or s in f["reason"] for f in failures):
        failures.append({"url": s, "reason": "not in the corpus after the plan fetch; miners fetch on demand"})

demand = []
for (i, bullet, lens, kind, q, src, facts) in D:
    demand.append({"id": i, "bullet": bullet, "lens": lens, "kind": kind, "question": q,
                   "status": "open", "facts": facts, "sources": src,
                   "sources_missing": [s for s in src if not exists(s)]})

brief = {
 "chapter": "05",
 "title": "IAM Identity Center, Directory Service and Cognito",
 "template": "medium",
 "services": ["iam-identity-center", "directory-service", "cognito"],
 "written_by": "plan-05",
 "written_at": "2026-10-12",
 "note": ("Security block chapter (reader's weakest domain). The docs host has Crawl-delay 5 shared by every agent, so the plan fetched a focused set "
          "(medium template: about 40 guide pages) plus every registry source; pages named in demand `sources` that are not yet saved are listed in "
          "`sources_missing` and in mine-plan `on_demand`, and miners fetch them with `saa.py fetch`. Facts already mined by chapter 03 in the "
          "iam-identity-center and cognito namespaces are named in `facts` (status mech-pass, not yet verified). Displays of number-free facts are "
          "verbatim phrases of at most 8 words (RULINGS 2026-10-11)."),
 "sources_fetched": len(fetched),
 "fetch_failures": failures,
 "guides": {
   "singlesignon-userguide": "aws-saa-book/_build/corpus/index/singlesignon-userguide.json",
   "directoryservice-admin-guide": "aws-saa-book/_build/corpus/index/directoryservice-admin-guide.json",
   "cognito-developerguide": "aws-saa-book/_build/corpus/index/cognito-developerguide.json"},
 "feeds": {
   "faq": ["aws-saa-book/_build/corpus/faq/iam-identity-center.jsonl", "aws-saa-book/_build/corpus/faq/directoryservice.jsonl", "aws-saa-book/_build/corpus/faq/cognito.jsonl"],
   "changes": ["aws-saa-book/_build/corpus/changes/iam-identity-center.jsonl", "aws-saa-book/_build/corpus/changes/directory-service.jsonl", "aws-saa-book/_build/corpus/changes/cognito.jsonl"],
   "work_files": ["changes-iam-identity-center.txt", "changes-directory-service.txt", "changes-cognito.txt", "faq-iam-identity-center.txt", "faq-directory-service.txt", "faq-cognito.txt", "cases-cognito.txt", "cases-sso.txt", "cases-directory-service.txt", "fetch-1.txt", "fetch-2.txt"]},
 "story": {
   "stage": "3 First bank customer, month 18, order 21",
   "trigger": "7 accounts for each engineer; the bank wants its 400 supervisors to sign in with the bank's identity provider",
   "decision": "IAM users in every account / IAM users in one account who assume roles / CHOSEN: IAM Identity Center for engineers, Cognito federation for the bank",
   "accepts": "all access depends on the identity provider; one tested emergency path",
   "stage4": "AWS Directory Service for Peldon",
   "question": "Ben: What is the difference between IAM Identity Center and Cognito? Both look like sign-in to me.",
   "diagrams": ["identity-federation-before", "identity-federation-after: two sign-in paths, engineers through IAM Identity Center, bank supervisors through a Cognito user pool"],
   "demand": ["d120", "d121", "d122", "d123"]},
 "orchestrator_focus": [
   "can-or-cannot completeness: d007, d051, d054, d058, d075, d076, d078, d091, d099",
   "neighbour comparisons: IdC vs Cognito (d067, d106), IdC vs direct IAM SAML federation (d066), user pool vs identity pool (d090, d092), AD Connector vs Managed AD vs Simple AD (d085), Managed AD vs self-managed (d083), AssumeRoleWithWebIdentity vs identity pool (d108)",
   "changes since mid-2022: d009-d018, d028-d030, d037-d046 (GA after 2026-07-15 is not examinable yet)",
   "numbers: d001-d008, d020-d027, d032-d035"],
 "demand": demand,
}
json.dump(brief, open(W / "brief.v0.json", "w"), indent=1)

lenses = {
 N: {"what": "Every quota, default, range and price: IdC limits (tables), Managed AD / AD Connector / Simple AD quota tables, Cognito quotas (10 tables; quote the row plus header_text), token validity, session durations, pricing dimensions; and every change item since 2022-07 as a change fact with date (old value only when the history row or page states it). GA after 2026-07-15 is labelled not examinable yet.", "pages": [], "demand": []},
 B: {"what": "How each service works and every can / cannot / only / by default statement; the comparisons the exam hinges on (IdC vs Cognito, user pool vs identity pool, AD Connector vs Managed AD vs Simple AD, IdC vs direct IAM federation); decision guide, Well-Architected and SRA guidance; the Callvale decision facts; the case studies.", "pages": [], "demand": []},
 F: {"what": "The three FAQ pages: one fact per quick-fire item with the verbatim FAQ sentence from the snapshot (not the faq index).", "pages": [FAQ_IC, FAQ_DS, FAQ_CG], "demand": []},
}
numbers_pages = {Q_IC, Q_MAD, Q_ADC, Q_SAD, Q_CG, PR_DS, PR_CG, H_IC, H_DS, H_CG,
                 DS + "simple-ad-availability-change", DS + "ms_ad_upgrade_edition", DS + "aws-hybrid-directory",
                 CG + "cognito-sign-in-feature-plans", CG + "user-pool-multi-region", CG + "cognito-sync-availability-change",
                 IC + "multi-region-iam-identity-center", IC + "howtosessionduration", IC + "account-instances-identity-center"}
both = {IC + "multi-region-iam-identity-center", DS + "simple-ad-availability-change", CG + "cognito-sign-in-feature-plans", CG + "user-pool-multi-region",
        DS + "ms_ad_configure_multi_region_replication", DS + "directory_ad_connector", DS + "directory_simple_ad", DS + "directory_microsoft_ad", IC + "howtosessionduration", IC + "permissionsetsconcept"}
for s in fetched:
    if s in (FAQ_IC, FAQ_DS, FAQ_CG):
        continue
    if s in numbers_pages:
        lenses[N]["pages"].append(s)
        if s in both:
            lenses[B]["pages"].append(s)
    else:
        lenses[B]["pages"].append(s)
        if s in both:
            lenses[N]["pages"].append(s)
for d in demand:
    lenses[d["lens"]]["demand"].append(d["id"])
on_demand = sorted({s for d in demand for s in d["sources_missing"]} | set(not_yet))
plan = {
 "chapter": "05", "written_by": "plan-05", "written_at": "2026-10-12",
 "rules": [
  "Quote only from page snapshots (snap/<source_id>.txt); full:<guide> search hits and faq/changes index rows are pointers, never evidence.",
  "Each demand item lists `sources`; a source not yet saved is in `sources_missing` and in `on_demand`: fetch it with `python3 aws-saa-book/tools/saa.py fetch <url>` (docs host Crawl-delay is 5 seconds, shared: fetch only what the item needs).",
  "Mark each demand item filled, contradicted (say what the page says) or not-found in the mine report.",
  "HYPOTHESIS items come from FRESHNESS.md or the change feeds: confirm the date from the document-history snapshot or a What's New page; take the current value from the guide page.",
  "Anything GA after 2026-07-15 is labelled not examinable yet (RULINGS rule 7).",
  "Facts live in the namespace of their service key: iam-identity-center, directory-service, cognito. Chapter 03 already mined 14 iam-identity-center and 3 cognito facts (named in demand `facts`): reuse, do not duplicate.",
  "Displays of number-free facts are verbatim phrases of at most 8 words from the quote (RULINGS 2026-10-11). Quota facts quote the table row plus header_text.",
  "Current names only: IAM Identity Center (formerly AWS Single Sign-On, once), managed login (formerly hosted UI)."],
 "lenses": lenses,
 "on_demand": on_demand,
}
json.dump(plan, open(W / "mine-plan.json", "w"), indent=1)
print("demand", len(demand), "fetched", len(fetched), "not_yet", len(not_yet), "failures", len(failures), "on_demand", len(on_demand),
      {k: (len(v["pages"]), len(v["demand"])) for k, v in lenses.items()})
