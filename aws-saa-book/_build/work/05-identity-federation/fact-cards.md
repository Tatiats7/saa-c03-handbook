facts card: 409 facts
cognito-access-token-validity-range
  claim: The validity of a user pool access token can be set from 5 minutes to 1 day.
  scope: user pool access tokens (token validity setting in user pools); maximum; not adjustable; allowed setting range.
  link: [5 minutes](../facts/cognito.md#cognito-access-token-validity-range)
  link: [1 day](../facts/cognito.md#cognito-access-token-validity-range)
  say: five minutes | one day
cognito-alb-authenticate-cognito-https-only
  claim: An Application Load Balancer can authenticate users before they reach the application, through an OIDC-compliant IdP or through Cognito user pools (social IdPs and corporate SAML, OIDC or OAuth identities); the authenticate-cognito and authenticate-oidc actions are supported only on HTTPS listeners.
  scope: Application Load Balancer listener rules.
  link: [offload the work of authenticating users](../facts/cognito.md#cognito-alb-authenticate-cognito-https-only)
  link: [supported only with HTTPS listeners](../facts/cognito.md#cognito-alb-authenticate-cognito-https-only)
cognito-api-gateway-aws-iam-with-identity-pool
  claim: To let a user sign in with Cognito and also use temporary credentials with the permissions of an IAM role, use Cognito identity pools (federated identities) and set the API Gateway method authorization type to AWS_IAM.
  scope: API Gateway REST APIs.
  link: [to `AWS_IAM`](../facts/cognito.md#cognito-api-gateway-aws-iam-with-identity-pool)
  link: [obtain temporary credentials](../facts/cognito.md#cognito-api-gateway-aws-iam-with-identity-pool)
cognito-api-gateway-cognito-user-pools-authorizer
  claim: To protect a REST API with a Cognito user pool, you create a COGNITO_USER_POOLS authorizer in API Gateway and enable it on API methods; the client signs in, gets an identity or access token, and sends it, typically in the Authorization header, and the call succeeds only with a valid token.
  scope: API Gateway REST APIs.
  link: [an authorizer of the `COGNITO_USER_POOLS` type](../facts/cognito.md#cognito-api-gateway-cognito-user-pools-authorizer)
  link: [supply the appropriate token in the `Authorization` header](../facts/cognito.md#cognito-api-gateway-cognito-user-pools-authorizer)
  link: [the supplied token is valid](../facts/cognito.md#cognito-api-gateway-cognito-user-pools-authorizer)
cognito-api-gateway-id-vs-access-token-scopes
  claim: With a Cognito user pool authorizer, the identity token authorizes API calls based on the signed-in user's identity claims, and the access token authorizes calls based on custom scopes of access-protected resources.
  scope: API Gateway REST APIs with a Cognito user pool authorizer.
  link: [based on identity claims of the signed-in user](../facts/cognito.md#cognito-api-gateway-id-vs-access-token-scopes)
  link: [based on the custom scopes](../facts/cognito.md#cognito-api-gateway-id-vs-access-token-scopes)
cognito-api-gateway-validates-user-pool-token
  claim: To protect your own API, you can use the user pool access token to authorize requests to server-side resources, or let Amazon API Gateway validate the token and gate access to a Lambda function or your API.
  scope: Cognito user pool tokens with API Gateway.
  link: [let Amazon API Gateway validate the token](../facts/cognito.md#cognito-api-gateway-validates-user-pool-token)
  link: [gate access to a Lambda function](../facts/cognito.md#cognito-api-gateway-validates-user-pool-token)
cognito-authentication-session-token-range
  claim: The validity of a user pool authentication session token can be set from 3 minutes to 15 minutes.
  scope: user pool authentication session tokens (validity setting in user pools); maximum; not adjustable; allowed setting range.
  link: [3 minutes](../facts/cognito.md#cognito-authentication-session-token-range)
  link: [15 minutes](../facts/cognito.md#cognito-authentication-session-token-range)
  say: three minutes | fifteen minutes
cognito-bulk-import-new-password-required
  claim: After a bulk CSV import into a Cognito user pool, users must verify their account and create a new password with a code sent by email or phone at their first sign-in.
  scope: users imported into a user pool from a CSV file; bulk migration by CSV import.
  link: [create a new password](../facts/cognito.md#cognito-bulk-import-new-password-required)
cognito-case-olx-ciam-on-cognito
  claim: OLX, which runs online classifieds platforms in nine countries, runs its customer identity and access management (hCIAM) on Amazon Cognito; the hCIAM is OAuth 2.0 and OIDC compliant and its backend works alongside Amazon Cognito.
  scope: OLX case study.
  link: [runs its hCIAM using Amazon Cognito](../facts/cognito.md#cognito-case-olx-ciam-on-cognito)
  link: [OAuth 2.0 and OIDC compliant](../facts/cognito.md#cognito-case-olx-ciam-on-cognito)
cognito-case-olx-waf-bot-control-protects-sign-up
  claim: OLX runs its hCIAM, which validates registration and login for its users, on Amazon Cognito and uses AWS WAF Bot Control against bot traffic: on a regular day it processes 2 million requests and rejects around 13,000, and during one bot event it processed 2.1 million requests and rejected 250,000 false requests.
  scope: OLX case study.
  link: [processes 2 million requests and rejects around 13,000](../facts/cognito.md#cognito-case-olx-waf-bot-control-protects-sign-up)
  link: [rejected 250,000 false requests](../facts/cognito.md#cognito-case-olx-waf-bot-control-protects-sign-up)
cognito-change-client-secret-rotation-2026-01
  claim: Since 2026-01-30 an app client can have up to two secrets for secret rotation, and you can provide your own custom secret value.
  scope: per app client; maximum.
  link: [January 30, 2026](../facts/cognito.md#cognito-change-client-secret-rotation-2026-01)
  link: [up to two secrets per app client](../facts/cognito.md#cognito-change-client-secret-rotation-2026-01)
  say: January thirtieth, twenty twenty-six | two secrets
cognito-change-customer-managed-kms-key-2026-05
  claim: Since 2026-05-28 you can configure user pool encryption at rest with your own custom KMS key.
  scope: per user pool.
  link: [May 28, 2026](../facts/cognito.md#cognito-change-customer-managed-kms-key-2026-05)
  link: [your own custom KMS key](../facts/cognito.md#cognito-change-customer-managed-kms-key-2026-05)
  say: May twenty-eighth, twenty twenty-six | your own KMS key
cognito-change-deletion-protection-default-2022-10
  claim: Since 2022-10-20 a new user pool that you create with the AWS Management Console is protected against deletion by default.
  scope: per user pool; default; user pool created with the AWS Management Console.
  link: [October 20, 2022](../facts/cognito.md#cognito-change-deletion-protection-default-2022-10)
  link: [protected against deletion by default](../facts/cognito.md#cognito-change-deletion-protection-default-2022-10)
  say: October twentieth, twenty twenty-two | on by default in the console
cognito-change-email-mfa-2024-09
  claim: On September 12, 2024 Amazon Cognito user pools added the ability to send multi-factor authentication (MFA) codes by email message, as part of advanced security features. Today MFA with email one-time codes is a feature of the Essentials and Plus feature plans.
  scope: per user pool; at launch: with advanced security features; today: Essentials or Plus feature plan.
  link: [September 12, 2024](../facts/cognito.md#cognito-change-email-mfa-2024-09)
  link: [send multi-factor authentication (MFA) codes by email message](../facts/cognito.md#cognito-change-email-mfa-2024-09)
  say: September twelfth, twenty twenty-four | email MFA codes
cognito-change-feature-plans-2024-11
  claim: On 2024-11-21 the user pool billing model changed to feature plans: advanced security features became threat protection, and its components moved into the Essentials and Plus feature plans.
  scope: per user pool.
  link: [November 21, 2024](../facts/cognito.md#cognito-change-feature-plans-2024-11)
  link: [Essentials and Plus feature plans](../facts/cognito.md#cognito-change-feature-plans-2024-11)
  link: [Advanced security features are now threat protection](../facts/cognito.md#cognito-change-feature-plans-2024-11)
  say: November twenty-first, twenty twenty-four | Essentials and Plus | advanced security is now threat protection
  changed: 2024-11-21: was Advanced security features
cognito-change-identity-pool-trust-policy-aud-2025-08
  claim: Since 2025-08-01 you can change a role trust policy for the Amazon Cognito identity pools service principal only when a condition key scopes the audience for OIDC (web identity) federation to one or more identity pools.
  scope: IAM roles trusted by Cognito identity pools.
  link: [August 1, 2025](../facts/cognito.md#cognito-change-identity-pool-trust-policy-aud-2025-08)
  link: [scopes the audience for OIDC (web identity) federation](../facts/cognito.md#cognito-change-identity-pool-trust-policy-aud-2025-08)
  say: August first, twenty twenty-five | the trust policy must name your identity pools
cognito-change-inbound-federation-trigger-2026-01
  claim: Since 2026-01-28 user pools have an inbound federation Lambda trigger that transforms federated user attributes during authentication with external identity providers.
  scope: Cognito user pool Lambda triggers.
  link: [January 28, 2026](../facts/cognito.md#cognito-change-inbound-federation-trigger-2026-01)
  link: [transform federated user attributes](../facts/cognito.md#cognito-change-inbound-federation-trigger-2026-01)
  say: January twenty-eighth, twenty twenty-six | change federated user attributes at sign-in
cognito-change-m2m-without-domain-2026-07
  claim: Since 2026-07-29 you can issue access tokens for machine-to-machine (M2M) authorization with the GetClientToken API operation, without a user pool domain.
  scope: per app client.
  link: [July 29, 2026](../facts/cognito.md#cognito-change-m2m-without-domain-2026-07)
  link: [without a user pool domain](../facts/cognito.md#cognito-change-m2m-without-domain-2026-07)
  say: July twenty-ninth, twenty twenty-six | no domain needed
cognito-change-managed-login-2024-11
  claim: On 2024-11-21 Amazon Cognito launched managed login, an update to the hosted UI.
  scope: per user pool domain.
  link: [November 21, 2024](../facts/cognito.md#cognito-change-managed-login-2024-11)
  link: [managed login, an update to the hosted UI](../facts/cognito.md#cognito-change-managed-login-2024-11)
  say: November twenty-first, twenty twenty-four | managed login is the new hosted UI
  changed: 2024-11-21: was the hosted UI
cognito-change-multi-region-replication-2026-05
  claim: Since 2026-05-28 you can set up an additional copy of a user pool in an additional AWS Region (multi-Region replication).
  scope: per user pool.
  link: [May 28, 2026](../facts/cognito.md#cognito-change-multi-region-replication-2026-05)
  link: [an additional copy of your user pools](../facts/cognito.md#cognito-change-multi-region-replication-2026-05)
  say: May twenty-eighth, twenty twenty-six | a copy in another Region
cognito-change-passkeys-otp-2024-11
  claim: Since 2024-11-21 users can sign in to Amazon Cognito user pools with passkeys and one-time passwords.
  scope: per user pool.
  link: [November 21, 2024](../facts/cognito.md#cognito-change-passkeys-otp-2024-11)
  link: [passkeys and one-time passwords](../facts/cognito.md#cognito-change-passkeys-otp-2024-11)
  say: November twenty-first, twenty twenty-four | passkeys and one-time passwords
cognito-change-password-hash-import-2026-07
  claim: Since 2026-07-13 you can import users with their existing password hashes, so they can sign in at once without a password reset.
  scope: per user import job.
  link: [July 13, 2026](../facts/cognito.md#cognito-change-password-hash-import-2026-07)
  link: [import users with their existing password hashes](../facts/cognito.md#cognito-change-password-hash-import-2026-07)
  say: July thirteenth, twenty twenty-six | import with password hashes
cognito-change-privatelink-identity-pools-2025-12
  claim: Since 2025-12-10 you can send requests to Amazon Cognito identity pool API operations through VPC endpoints (AWS PrivateLink).
  scope: per VPC endpoint.
  link: [December 10, 2025](../facts/cognito.md#cognito-change-privatelink-identity-pools-2025-12)
  say: December tenth, twenty twenty-five
cognito-change-privatelink-user-pools-2025-11
  claim: Since 2025-11-04 you can send requests to Amazon Cognito user pools API operations through VPC endpoints (AWS PrivateLink).
  scope: per VPC endpoint.
  link: [November 4, 2025](../facts/cognito.md#cognito-change-privatelink-user-pools-2025-11)
  link: [through VPC endpoints](../facts/cognito.md#cognito-change-privatelink-user-pools-2025-11)
  say: November fourth, twenty twenty-five | through VPC endpoints
cognito-change-provisioned-limit-apis-2026-07
  claim: Since July 2, 2026 you can manage provisioned limits for your user pool with the Amazon Cognito provisioning APIs.
  scope: per user pool.
  link: [July 2, 2026](../facts/cognito.md#cognito-change-provisioned-limit-apis-2026-07)
  say: July second, twenty twenty-six
cognito-change-purchase-quota-capacity-2024-01
  claim: Since 2024-01-25 you can purchase additional capacity for Amazon Cognito request-rate quotas.
  scope: per account, per Region.
  link: [January 25, 2024](../facts/cognito.md#cognito-change-purchase-quota-capacity-2024-01)
  link: [purchase additional capacity](../facts/cognito.md#cognito-change-purchase-quota-capacity-2024-01)
  say: January twenty-fifth, twenty twenty-four | buy more request-rate capacity
cognito-change-refresh-token-rotation-2025-04
  claim: Since 2025-04-22 refresh-token requests can return new refresh tokens and invalidate the originals (refresh token rotation).
  scope: per app client.
  link: [April 22, 2025](../facts/cognito.md#cognito-change-refresh-token-rotation-2025-04)
  link: [get new refresh tokens and invalidate the originals](../facts/cognito.md#cognito-change-refresh-token-rotation-2025-04)
  say: April twenty-second, twenty twenty-five | new refresh token, old one invalidated
cognito-change-saml-signing-idp-initiated-2024-02
  claim: Since February 1, 2024 you can sign SAML requests, encrypt SAML responses and set up IdP-initiated SAML SSO for SAML identity providers in a Cognito user pool.
  scope: SAML identity providers in a Cognito user pool.
  link: [February 1, 2024](../facts/cognito.md#cognito-change-saml-signing-idp-initiated-2024-02)
  link: [set up IdP-initiated SAML SSO](../facts/cognito.md#cognito-change-saml-signing-idp-initiated-2024-02)
  say: February first, twenty twenty-four | IdP-initiated SAML sign-in
cognito-change-sync-closed-to-new-customers-2026-07
  claim: Since 2026-07-31 the history marks Amazon Cognito Sync as no longer open to new customers; AWS names AWS AppSync and DynamoDB as alternatives.
  scope: all new customers.
  link: [July 31, 2026](../facts/cognito.md#cognito-change-sync-closed-to-new-customers-2026-07)
  link: [AWS AppSync and DynamoDB](../facts/cognito.md#cognito-change-sync-closed-to-new-customers-2026-07)
  say: July thirty-first, twenty twenty-six | AppSync and DynamoDB
  changed: 2026-07-31: was Amazon Cognito Sync
cognito-change-sync-closure-announced-2026-06
  claim: On 2026-06-30 AWS announced that Amazon Cognito Sync will no longer be open to new customers starting July 30, 2026, and that existing customers can continue using the service.
  scope: existing and new customers.
  link: [June 30, 2026](../facts/cognito.md#cognito-change-sync-closure-announced-2026-06)
  link: [July 30, 2026](../facts/cognito.md#cognito-change-sync-closure-announced-2026-06)
  link: [Existing Amazon Cognito Sync customers can continue](../facts/cognito.md#cognito-change-sync-closure-announced-2026-06)
  say: June thirtieth, twenty twenty-six | July thirtieth, twenty twenty-six | existing customers keep it
cognito-change-waf-managed-login-2025-06
  claim: Since 2025-06-24 you can apply AWS WAF web ACL rules to user pool app clients that have the managed login branding version.
  scope: per app client (managed login).
  link: [June 24, 2025](../facts/cognito.md#cognito-change-waf-managed-login-2025-06)
  say: June twenty-fourth, twenty twenty-five
cognito-change-waf-user-pool-2022-08
  claim: Since 2022-08-03 you can associate an AWS WAF web ACL with an Amazon Cognito user pool.
  scope: per user pool.
  link: [August 3, 2022](../facts/cognito.md#cognito-change-waf-user-pool-2022-08)
  link: [associate a AWS WAF web ACL](../facts/cognito.md#cognito-change-waf-user-pool-2022-08)
  say: August third, twenty twenty-two | attach a WAF web ACL to a user pool
cognito-compromised-credentials-check
  claim: Cognito can check for compromised credentials at sign-up, sign-in and password change so that users do not use a password compromised at another site.
  scope: Cognito user pool threat protection.
  link: [compromised credentials checking](../facts/cognito.md#cognito-compromised-credentials-check)
cognito-compromised-credentials-not-srp-or-custom
  claim: Compromised-credentials detection compares users' credentials with leaked credential lists and common passwords in username-and-password standard authentication flows; it does not detect compromised credentials in SRP or custom authentication. Adaptive authentication reviews location and device information and responds to risk automatically.
  scope: Cognito threat protection; Plus feature plan.
  link: [doesn't detect compromised credentials](../facts/cognito.md#cognito-compromised-credentials-not-srp-or-custom)
  link: [review location and device information](../facts/cognito.md#cognito-compromised-credentials-not-srp-or-custom)
cognito-custom-domain-acm-us-east-1-cloudfront
  claim: A user pool custom domain for managed login needs an SSL certificate managed with AWS Certificate Manager in US East (N. Virginia); Amazon Cognito creates a CloudFront distribution secured with that certificate, and you create a DNS record pointing to it.
  scope: Cognito user pool custom domains.
  link: [in US East (N. Virginia)](../facts/cognito.md#cognito-custom-domain-acm-us-east-1-cloudfront)
  link: [creates a Amazon CloudFront distribution](../facts/cognito.md#cognito-custom-domain-acm-us-east-1-cloudfront)
cognito-customer-managed-kms-multi-region-keys
  claim: Cognito supports customer managed AWS KMS keys for user data, and multi-Region keys give the same encryption in the primary and secondary Regions.
  scope: Cognito user data encryption at rest.
  link: [supports customer managed keys](../facts/cognito.md#cognito-customer-managed-kms-multi-region-keys)
  link: [multi-Region keys](../facts/cognito.md#cognito-customer-managed-kms-multi-region-keys)
cognito-decision-guide-build-authentication-row
  claim: In the identity decision guide table, a developer who wants to build an authentication mechanism into their own application is pointed to Amazon Cognito.
  scope: AWS identity decision guide.
  link: [Build an authentication mechanism into my own application](../facts/cognito.md#cognito-decision-guide-build-authentication-row)
cognito-decision-guide-ciam-for-apps-you-build
  claim: The AWS identity decision guide places Amazon Cognito under the applications you build: it implements customer identity and access management (CIAM) in web and mobile applications and also supports service-to-service authentication and authorization.
  scope: AWS identity decision guide.
  link: [customer identity and access management (CIAM)](../facts/cognito.md#cognito-decision-guide-ciam-for-apps-you-build)
  link: [service-to-service authentication and authorization](../facts/cognito.md#cognito-decision-guide-ciam-for-apps-you-build)
cognito-domain-requests-per-source-ip
  claim: A user pool domain accepts at most 300 requests per second from one source IP address, and this quota is not adjustable.
  scope: per source IP address, per user pool domain; maximum; not adjustable.
  link: [300](../facts/cognito.md#cognito-domain-requests-per-source-ip)
  say: three hundred requests per second
cognito-feature-plan-per-user-pool-default-essentials
  claim: A feature plan applies to one whole user pool, not to separate app clients; different user pools in one account can use different plans, and the default plan for new user pools is Essentials.
  scope: per user pool; default; adjustable.
  link: [for new user pools is Essentials](../facts/cognito.md#cognito-feature-plan-per-user-pool-default-essentials)
  link: [Feature-plan selections apply to one user pool](../facts/cognito.md#cognito-feature-plan-per-user-pool-default-essentials)
  say: Essentials | per user pool
cognito-federated-idp-auto-group
  claim: Amazon Cognito creates a user group for each OIDC, SAML and social identity provider added to a user pool, and each automatically generated IdP user profile is added to that group; groups have no additional cost.
  scope: Cognito user pool groups.
  link: [automatically added to this group](../facts/cognito.md#cognito-federated-idp-auto-group)
  link: [no additional cost for using groups](../facts/cognito.md#cognito-federated-idp-auto-group)
cognito-federated-user-profile-maps-idp-claims
  claim: To an external IdP, Cognito is a service provider: the IdP passes an OIDC ID token or SAML assertion, Cognito maps the claims to a user profile in the user pool, and then acts as an OIDC and OAuth 2.0 IdP to the app, issuing access, ID and refresh tokens; a local user exists only in the user pool directory.
  scope: Cognito user pool federation.
  link: [Amazon Cognito is a service provider (SP)](../facts/cognito.md#cognito-federated-user-profile-maps-idp-claims)
  link: [access tokens, ID tokens, and refresh tokens](../facts/cognito.md#cognito-federated-user-profile-maps-idp-claims)
  link: [exists exclusively in your user pool directory](../facts/cognito.md#cognito-federated-user-profile-maps-idp-claims)
cognito-first-factor-and-mfa-options
  claim: Cognito first-factor sign-in supports username and password, email OTP, SMS OTP and WebAuthn passkeys; its MFA factors are email OTP, SMS OTP and TOTP authenticators.
  scope: Cognito user pool sign-in and MFA.
  link: [WebAuthn passkeys](../facts/cognito.md#cognito-first-factor-and-mfa-options)
  link: [email OTP, SMS OTP, and TOTP authenticators](../facts/cognito.md#cognito-first-factor-and-mfa-options)
cognito-forgot-password-code-validity
  claim: A user pool forgot-password code is valid for 1 hour, and this quota is not adjustable.
  scope: per password reset code; fixed; not adjustable.
  link: [1 hour](../facts/cognito.md#cognito-forgot-password-code-validity)
  say: one hour
cognito-free-tier-10000-mau
  claim: The Amazon Cognito user pools SKU and Essentials SKU are free for the first 10,000 MAUs (users who sign in directly or through a social identity provider). Customers with existing user pools created on or before 10:00am Pacific Time, November 22, 2024 keep a free tier of the first 50,000 MAUs.
  scope: per month per account or per AWS organization; user pools (Lite) and Essentials SKUs; maximum; 50,000 MAUs only for user pools created on or before 10:00am PT, November 22, 2024.
  link: [free for the first 10,000 MAUs](../facts/cognito.md#cognito-free-tier-10000-mau)
  link: [50,000 MAUs](../facts/cognito.md#cognito-free-tier-10000-mau)
  changed: 2024-11-22: was 50,000 MAUs
cognito-group-precedence-preferred-role
  claim: A user pool group can carry an IAM role; when a user is in several groups, the cognito:preferred_role claim of the ID token is set to the role of the group with the best (lowest) precedence value, and the identity pool can use it to issue credentials.
  scope: Cognito user pool groups with identity pools.
  link: [role to a group](../facts/cognito.md#cognito-group-precedence-preferred-role)
  link: [the best (lowest) `Precedence` value](../facts/cognito.md#cognito-group-precedence-preferred-role)
  link: [the better (lower) precedence will be chosen](../facts/cognito.md#cognito-group-precedence-preferred-role)
cognito-id-token-validity-range
  claim: The validity of a user pool ID token can be set from 5 minutes to 1 day.
  scope: per app client (user pool tokens); maximum; not adjustable; allowed setting range.
  link: [5 minutes](../facts/cognito.md#cognito-id-token-validity-range)
  link: [1 day](../facts/cognito.md#cognito-id-token-validity-range)
  say: five minutes | one day
cognito-id-token-vs-access-token-use
  claim: An app accepts the user pool's ID token to authenticate the user and set up the user's profile, and an API accepts the access token, whose OIDC scopes authorize the user's API calls.
  scope: Cognito user pool tokens.
  link: [Accept an ID token in your app](../facts/cognito.md#cognito-id-token-vs-access-token-use)
  link: [Accept an access token in your API](../facts/cognito.md#cognito-id-token-vs-access-token-use)
cognito-identity-id-per-user-s3-folder
  claim: The unique identifier Cognito generates for each user can be used in an S3 bucket policy so each user can reach only their own folder.
  scope: Cognito identity pool identity IDs.
  link: [access to their own folder](../facts/cognito.md#cognito-identity-id-per-user-s3-folder)
cognito-identity-platform-definition
  claim: Amazon Cognito is an identity platform for web and mobile apps: a user directory, an authentication server, and an authorization service for OAuth 2.0 access tokens and AWS credentials.
  scope: Amazon Cognito.
  link: [an identity platform for web and mobile apps](../facts/cognito.md#cognito-identity-platform-definition)
  link: [a user directory, an authentication server](../facts/cognito.md#cognito-identity-platform-definition)
cognito-identity-pool-abac-principal-tags
  claim: For attributes for access control, an identity pool reads attributes from the user's claims and maps them to principal tags in the user's temporary session, which IAM policies can match with the aws:PrincipalTag condition.
  scope: Cognito identity pool attributes for access control.
  link: [maps them to principal tags](../facts/cognito.md#cognito-identity-pool-abac-principal-tags)
  link: [in your user’s temporary session](../facts/cognito.md#cognito-identity-pool-abac-principal-tags)
cognito-identity-pool-credentials-from-sts
  claim: When a user presents trusted claims from a SAML 2.0, OIDC or OAuth 2.0 social IdP, the identity pool associates the user with an identity, and the token the identity pool creates for that identity retrieves temporary session credentials from AWS STS.
  scope: Cognito identity pool.
  link: [temporary session credentials from AWS Security Token Service](../facts/cognito.md#cognito-identity-pool-credentials-from-sts)
  link: [associate your user with an identity](../facts/cognito.md#cognito-identity-pool-credentials-from-sts)
cognito-identity-pool-directory-of-federated-identities
  claim: A Cognito identity pool is a directory of federated identities that can be exchanged for AWS credentials; it accepts an ID or access token, a user pool token, a SAML assertion or a social-provider OAuth token, and users can start as guests and sign in later to unlock more access.
  scope: Cognito identity pools.
  link: [a directory of federated identities](../facts/cognito.md#cognito-identity-pool-directory-of-federated-identities)
  link: [a SAML assertion, or a social-provider OAuth token](../facts/cognito.md#cognito-identity-pool-directory-of-federated-identities)
  link: [Users can start out as guests](../facts/cognito.md#cognito-identity-pool-directory-of-federated-identities)
cognito-identity-pool-enhanced-flow-one-hour-credentials
  claim: Identity pools have two authentication flows with public providers, enhanced and basic. In the enhanced flow the identity pool configuration handles IAM role selection (a default role, RBAC or ABAC) and credentials retrieval, and the AWS credentials are valid for one hour; in the basic flow your application selects the IAM role.
  scope: Cognito identity pool authentication flows.
  link: [enhanced and basic](../facts/cognito.md#cognito-identity-pool-enhanced-flow-one-hour-credentials)
  link: [valid for one hour](../facts/cognito.md#cognito-identity-pool-enhanced-flow-one-hour-credentials)
  link: [your application selects the IAM role](../facts/cognito.md#cognito-identity-pool-enhanced-flow-one-hour-credentials)
cognito-identity-pool-get-credentials-rps
  claim: The identity pool GetCredentialsForIdentity operation, which retrieves AWS credentials in the enhanced workflow, has a default quota of 200 requests per second, adjustable through your account team. The default quota is the minimum for the identity pools in any AWS Region in your account; the quota might be higher in some Regions.
  scope: per AWS account; the default is the minimum across Regions; default; adjustable; increase: contact your account team; might be higher in some Regions.
  link: [200](../facts/cognito.md#cognito-identity-pool-get-credentials-rps)
  say: two hundred requests per second
cognito-identity-pool-getid-rps
  claim: The identity pool GetId operation, which retrieves an identity ID, has a default quota of 25 requests per second, adjustable through your account team. The default quota is the minimum for the identity pools in any AWS Region in your account; the quota might be higher in some Regions.
  scope: per AWS account; the default is the minimum across Regions; default; adjustable; increase: contact your account team; might be higher in some Regions.
  link: [25](../facts/cognito.md#cognito-identity-pool-getid-rps)
  say: twenty-five requests per second
cognito-identity-pool-guest-and-authenticated-store
  claim: An identity pool provides temporary AWS credentials both to guest (unauthenticated) users and to authenticated users who received a token, and it is a store of user identifiers linked to external identity providers.
  scope: Cognito identity pools.
  link: [users who are guests (unauthenticated)](../facts/cognito.md#cognito-identity-pool-guest-and-authenticated-store)
  link: [a store of user identifiers](../facts/cognito.md#cognito-identity-pool-guest-and-authenticated-store)
cognito-identity-pool-guest-credentials
  claim: An identity pool can also issue limited-privilege AWS credentials to guest users who have not signed in, without any token.
  scope: Cognito identity pool guest users.
  link: [issue limited-privilege credentials to guest users](../facts/cognito.md#cognito-identity-pool-guest-credentials)
cognito-identity-pool-no-user-credentials-stored
  claim: With public identity providers, Cognito identity pools do not receive or store user credentials; they use the provider's token to get a unique user identifier and store only a one-way hash of it.
  scope: Cognito identity pools with public identity providers; public identity providers.
  link: [does not receive or store user credentials](../facts/cognito.md#cognito-identity-pool-no-user-credentials-stored)
  link: [a one-way hash](../facts/cognito.md#cognito-identity-pool-no-user-credentials-stored)
cognito-identity-pool-provider-types
  claim: Cognito identity pools accept Amazon, Facebook, Twitter, Sign in with Apple and Google, OIDC and SAML identity providers, Cognito user pools, and custom developer providers.
  scope: Cognito identity pool identity providers.
  link: [Amazon Cognito user pools](../facts/cognito.md#cognito-identity-pool-provider-types)
  link: [custom developer providers](../facts/cognito.md#cognito-identity-pool-provider-types)
cognito-identity-pool-role-per-user-or-group
  claim: Cognito identity pools control each user's permissions with IAM roles: rules can choose the role per user, or roles can be assigned by Cognito user pool group.
  scope: Cognito identity pool permissions.
  link: [define rules to choose the IAM role](../facts/cognito.md#cognito-identity-pool-role-per-user-or-group)
  link: [assign IAM roles based on groups](../facts/cognito.md#cognito-identity-pool-role-per-user-or-group)
cognito-identity-pool-role-selection-options
  claim: With role-based access control, the identity pool chooses the IAM role to request: a default role, a role from rules that query the user's claims, or a role from the user's group membership in a user pool; the role trust policy can be set so that IAM trusts only your identity pool.
  scope: Cognito identity pool role-based access control.
  link: [a default role](../facts/cognito.md#cognito-identity-pool-role-selection-options)
  link: [rules that query your user’s claims](../facts/cognito.md#cognito-identity-pool-role-selection-options)
  link: [your user’s group membership in a user pool](../facts/cognito.md#cognito-identity-pool-role-selection-options)
  link: [IAM trusts only your identity pool](../facts/cognito.md#cognito-identity-pool-role-selection-options)
cognito-identity-pool-role-trust-policy-aud-amr
  claim: AWS says it is important to add a trust policy to each role so that it can only be assumed by Amazon Cognito for authenticated users in your identity pool. In the documented example policy, federated users from cognito-identity.amazonaws.com can assume the role, the policy restricts the aud of the token to the identity pool ID, and one member of the amr claim of the token has the value authenticated.
  scope: IAM roles for authenticated users of a Cognito identity pool (documented example policy).
  link: [can only be assumed by Amazon Cognito](../facts/cognito.md#cognito-identity-pool-role-trust-policy-aud-amr)
  link: [restricts the `aud` of the token](../facts/cognito.md#cognito-identity-pool-role-trust-policy-aud-amr)
  link: [has the value `authenticated`](../facts/cognito.md#cognito-identity-pool-role-trust-policy-aud-amr)
cognito-identity-pool-rules-first-match-then-role-resolution
  claim: Rule-based role mapping evaluates rules in order and uses the IAM role of the first matching rule, unless CustomRoleArn is specified to override the order; if no rule matches, the Role resolution setting either uses the default authenticated role or denies the request.
  scope: Cognito identity pool rule-based role mapping.
  link: [the first matching rule is used](../facts/cognito.md#cognito-identity-pool-rules-first-match-then-role-resolution)
  link: [Use default authenticated role](../facts/cognito.md#cognito-identity-pool-rules-first-match-then-role-resolution)
  link: [Deny request](../facts/cognito.md#cognito-identity-pool-rules-first-match-then-role-resolution)
cognito-identity-pool-temporary-credentials-broker
  claim: Cognito identity pools act as a credential broker that gives users temporary, limited-privilege AWS credentials to reach AWS resources or services behind API Gateway.
  scope: Cognito identity pools.
  link: [as a credential broker](../facts/cognito.md#cognito-identity-pool-temporary-credentials-broker)
  link: [temporary, limited privilege AWS credentials](../facts/cognito.md#cognito-identity-pool-temporary-credentials-broker)
cognito-identity-pool-trust-policy-aud-condition-enforced
  claim: When the principal of an IAM role trust policy is cognito-identity.amazonaws.com, the policy cannot permit any identity pool to assume the role: the action needs a condition such as cognito-identity.amazonaws.com:aud that limits AssumeRoleWithWebIdentity to your identity pools, aud is required, and IAM returns an error if the condition is missing.
  scope: IAM roles trusted by Cognito identity pools.
  link: [permit any identity pool to assume the role](../facts/cognito.md#cognito-identity-pool-trust-policy-aud-condition-enforced)
  link: [but `aud` is required](../facts/cognito.md#cognito-identity-pool-trust-policy-aud-condition-enforced)
  link: [IAM returns an error](../facts/cognito.md#cognito-identity-pool-trust-policy-aud-condition-enforced)
cognito-identity-pool-unauthenticated-guest-role
  claim: Unauthenticated users of a Cognito identity pool do not sign in with any identity provider but use the app as guests, and you can give them a separate IAM role with limited permissions.
  scope: Cognito identity pool unauthenticated users.
  link: [access your app as a guest](../facts/cognito.md#cognito-identity-pool-unauthenticated-guest-role)
  link: [a separate IAM role](../facts/cognito.md#cognito-identity-pool-unauthenticated-guest-role)
cognito-identity-pools-no-charge
  claim: Using Cognito identity pools to authenticate users and generate unique identifiers is provided at no charge.
  scope: Cognito identity pool pricing.
  link: [provided at no charge](../facts/cognito.md#cognito-identity-pools-no-charge)
cognito-identity-pools-store-no-profiles
  claim: Cognito identity pools do not store user profiles; the same end user gets a different unique identifier in each of two different identity pools.
  scope: Cognito identity pools.
  link: [Identity Pools do not store any user profiles](../facts/cognito.md#cognito-identity-pools-store-no-profiles)
cognito-lambda-trigger-points
  claim: Cognito can call custom Lambda functions at pre-registration, post-confirmation, pre-authentication, during authentication and at post-authentication.
  scope: Cognito user pool Lambda triggers.
  link: [pre-registration, post-confirmation (registration), pre-authentication](../facts/cognito.md#cognito-lambda-trigger-points)
cognito-lambda-triggers-customize-auth
  claim: User pool Lambda triggers let you add your own authentication challenges, migrate users from another identity store, customize messages and modify JWTs; a trigger can even prevent sign-in by a user who would otherwise succeed.
  scope: Cognito user pool Lambda triggers.
  link: [introduce your own authentication challenges](../facts/cognito.md#cognito-lambda-triggers-customize-auth)
  link: [modify JSON web tokens (JWTs)](../facts/cognito.md#cognito-lambda-triggers-customize-auth)
  link: [prevent sign-in by a user](../facts/cognito.md#cognito-lambda-triggers-customize-auth)
cognito-lambda-triggers-no-extra-charge
  claim: Cognito adds no charge for using its events to trigger Lambda functions, but normal Lambda and other service rates apply while the functions run.
  scope: Lambda functions triggered by Cognito events.
  link: [no additional charge](../facts/cognito.md#cognito-lambda-triggers-no-extra-charge)
cognito-m2m-app-client-needs-client-secret
  claim: An application that calls an API with machine-to-machine (M2M) authorization must have a client ID and a client secret, so its user pool app client must have a client secret.
  scope: per app client used for M2M authorization.
  link: [must have a client ID and client secret](../facts/cognito.md#cognito-m2m-app-client-needs-client-secret)
  say: a client ID and a client secret
cognito-m2m-client-credentials-grant
  claim: Machine-to-machine (M2M) authorization in a user pool issues an access token to an app, service or device that authenticates as itself with the client_credentials grant, with no human user in the loop.
  scope: Cognito user pool machine-to-machine authorization.
  link: [authenticates as itself](../facts/cognito.md#cognito-m2m-client-credentials-grant)
  link: [with no human user in the loop](../facts/cognito.md#cognito-m2m-client-credentials-grant)
cognito-managed-login-custom-domain-instead-of-prefix
  claim: With a custom domain, users sign in to the application through managed login at your own web address instead of the default amazoncognito.com prefix domain.
  scope: Cognito managed login.
  link: [using your own web address](../facts/cognito.md#cognito-managed-login-custom-domain-instead-of-prefix)
  link: [the default `amazoncognito.com`](../facts/cognito.md#cognito-managed-login-custom-domain-instead-of-prefix)
cognito-managed-login-essentials-plus-hosted-ui-all
  claim: Managed login is available in the Essentials and Plus plans; the classic hosted UI is available in all feature plans, including Lite.
  scope: per user pool.
  link: [available in the Essentials and Plus tiers](../facts/cognito.md#cognito-managed-login-essentials-plus-hosted-ui-all)
  say: Essentials and Plus
cognito-managed-login-functions-and-hosted-ui
  claim: Adding a domain gives a user pool managed login: an authorization server, ready-to-use sign-in, sign-out and password pages, and a service provider to SAML, OIDC and social IdPs; the classic hosted UI is the first-generation alternative, the two are not used together, and in the Lite plan the classic hosted UI is the only option.
  scope: Cognito user pool domains.
  link: [A ready-to-use user interface (UI)](../facts/cognito.md#cognito-managed-login-functions-and-hosted-ui)
  link: [The classic hosted UI is a first-generation version](../facts/cognito.md#cognito-managed-login-functions-and-hosted-ui)
  link: [the classic hosted UI is your only option](../facts/cognito.md#cognito-managed-login-functions-and-hosted-ui)
cognito-managed-login-session-cookie-1-hour
  claim: When a user signs in with managed login or the hosted UI, or with a third-party provider, Amazon Cognito sets a session cookie in the browser that lets the user sign in again with the same authentication method for 1 hour; signing in with the cookie does not reset the cookie duration.
  scope: managed login and hosted UI session cookie (per browser); fixed; not adjustable; not reset when the user signs in with the cookie.
  link: [1 hour](../facts/cognito.md#cognito-managed-login-session-cookie-1-hour)
  say: one hour
cognito-mfa-code-validity
  claim: A user pool multi-factor authentication (MFA) code is valid for 3 to 15 minutes, and this quota is not adjustable.
  scope: per MFA code; maximum; not adjustable.
  link: [3–15 minutes](../facts/cognito.md#cognito-mfa-code-validity)
  say: three to fifteen minutes
cognito-migrate-user-trigger-at-sign-in-or-forgot-password
  claim: Cognito invokes the migrate user Lambda trigger when a user who does not exist in the user pool signs in with a password or uses the forgot-password flow, and creates the user after the function returns successfully; it is not invoked for passwordless sign-in.
  scope: Cognito migrate user Lambda trigger.
  link: [doesn't exist in the user pool](../facts/cognito.md#cognito-migrate-user-trigger-at-sign-in-or-forgot-password)
  link: [creates the user in the user pool](../facts/cognito.md#cognito-migrate-user-trigger-at-sign-in-or-forgot-password)
  link: [passwordless sign-in](../facts/cognito.md#cognito-migrate-user-trigger-at-sign-in-or-forgot-password)
cognito-migration-lambda-keeps-passwords-vs-csv-bulk
  claim: Users can be moved into a user pool in two ways: with a user migration Lambda trigger at first sign-in, where users keep their existing passwords and do not reset them, or in bulk by uploading a CSV file with the user profile attributes.
  scope: importing users into a Cognito user pool.
  link: [users can continue using their existing passwords](../facts/cognito.md#cognito-migration-lambda-keeps-passwords-vs-csv-bulk)
  link: [uploading a CSV file](../facts/cognito.md#cognito-migration-lambda-keeps-passwords-vs-csv-bulk)
cognito-mobile-app-never-embed-access-keys
  claim: For a mobile app, the IAM guide says not to embed access keys in the app, even in encrypted storage, and to use Amazon Cognito to manage user identities and the Cognito credentials provider to manage the credentials the app uses for AWS requests.
  scope: mobile apps that call AWS.
  link: [Don't embed access keys with the app](../facts/cognito.md#cognito-mobile-app-never-embed-access-keys)
  link: [even in encrypted storage](../facts/cognito.md#cognito-mobile-app-never-embed-access-keys)
  link: [the Amazon Cognito credentials provider](../facts/cognito.md#cognito-mobile-app-never-embed-access-keys)
cognito-multi-region-client-credentials-synced
  claim: With multi-Region replication, Cognito synchronizes client IDs and client credentials across Regions, so machine-to-machine authentication continues during a Regional transition.
  scope: Cognito user pool multi-Region replication; multi-Region replication is enabled.
  link: [synchronizes client IDs and client credentials across Regions](../facts/cognito.md#cognito-multi-region-client-credentials-synced)
cognito-multi-region-replication-failover
  claim: With Cognito multi-Region replication turned on, Cognito keeps copies of user and machine attribute data and the user pool configuration in another Region, and registered users can keep signing in through a secondary Region if the primary Region becomes unavailable.
  scope: Cognito user pool multi-Region replication; multi-Region replication is enabled.
  link: [automatically maintains copies of your user](../facts/cognito.md#cognito-multi-region-replication-failover)
  link: [continue signing in through a secondary Region](../facts/cognito.md#cognito-multi-region-replication-failover)
cognito-multi-region-sessions-stay-valid
  claim: During a Regional failover with Cognito multi-Region replication, existing user sessions stay valid across Regions, so users do not sign in again.
  scope: Cognito user pool multi-Region replication; multi-Region replication is enabled.
  link: [Existing user sessions remain valid](../facts/cognito.md#cognito-multi-region-sessions-stay-valid)
cognito-multi-tenant-quotas-shared-and-session-cookie
  claim: Cognito quotas apply per AWS account and Region and are shared by all tenants of an application; the managed login session cookie authenticates local users for all app clients of the same user pool, and per-tenant user pools are one way to prevent sign-in across app clients.
  scope: multi-tenant applications on Cognito.
  link: [shared across all tenants in your application](../facts/cognito.md#cognito-multi-tenant-quotas-shared-and-session-cookie)
  link: [all app clients in the same user pool](../facts/cognito.md#cognito-multi-tenant-quotas-shared-and-session-cookie)
  link: [Separate your users into per-tenant user pools.](../facts/cognito.md#cognito-multi-tenant-quotas-shared-and-session-cookie)
cognito-pools-used-together-or-alone
  claim: Use a user pool and an identity pool together when the app signs users in and must give them direct AWS access, but neither requires the other.
  scope: Cognito user pools and identity pools.
  link: [Neither component requires the other](../facts/cognito.md#cognito-pools-used-together-or-alone)
cognito-preferred-over-direct-web-identity-federation
  claim: The IAM guide recommends Amazon Cognito whenever possible for mobile and web app federation, because it does most of the work with public identity providers and also supports anonymous sign-ins; working directly with an OIDC-compatible provider is for more advanced scenarios.
  scope: federation for mobile and web apps.
  link: [Whenever possible, use Amazon Cognito](../facts/cognito.md#cognito-preferred-over-direct-web-identity-federation)
  link: [also supports anonymous sign-ins](../facts/cognito.md#cognito-preferred-over-direct-web-identity-federation)
  link: [for more advanced scenarios](../facts/cognito.md#cognito-preferred-over-direct-web-identity-federation)
cognito-price-example-essentials-mau
  claim: In the AWS pricing example for the Essentials tier, the price per MAU above the free tier is $0.015.
  scope: per MAU above the free tier, per month; AWS pricing example (Essentials tier).
  link: [$0.015](../facts/cognito.md#cognito-price-example-essentials-mau)
  say: one and a half cents per MAU
cognito-price-example-plus-mau
  claim: In the AWS pricing example for the Plus tier, every MAU is billed (free tier 0) at $0.020 per MAU.
  scope: per MAU, per month; AWS pricing example (Plus tier).
  link: [$0.020](../facts/cognito.md#cognito-price-example-plus-mau)
  say: two cents per MAU
cognito-pricing-federated-free-tier-50-mau
  claim: For users who sign in through SAML or OIDC federation, user pools have a free tier of 50 MAUs, and the price per MAU above that free tier is $0.015.
  scope: per MAU above the free tier; SAML or OIDC federated users.
  link: [50 MAUs](../facts/cognito.md#cognito-pricing-federated-free-tier-50-mau)
  link: [$0.015](../facts/cognito.md#cognito-pricing-federated-free-tier-50-mau)
  say: fifty monthly active users free | one and a half cents per MAU
cognito-pricing-higher-rps-per-rps-month
  claim: Higher API request-rate quotas are priced per 1 RPS of incremental capacity over the default quotas per month, each API category is charged separately, and the minimum duration is 1 day.
  scope: per API category, per month; minimum; RPS increases need AWS approval.
  link: [per 1 RPS of incremental capacity](../facts/cognito.md#cognito-pricing-higher-rps-per-rps-month)
  link: [1 day](../facts/cognito.md#cognito-pricing-higher-rps-per-rps-month)
  say: per extra RPS per month | one day
cognito-pricing-lite-is-pre-2024-capabilities
  claim: The Lite tier includes all Cognito user pool capabilities, without advanced security features, that were available before November 22, 2024.
  scope: per user pool.
  link: [available before November 22, 2024](../facts/cognito.md#cognito-pricing-lite-is-pre-2024-capabilities)
  say: the pre-November 2024 feature set
cognito-pricing-m2m-per-token-no-app-client-charge
  claim: For machine-to-machine authorization, Amazon Cognito charges monthly per successful token response, with no additional charge for the number of registered app clients.
  scope: per account, per month; client credentials flow.
  link: [per successful token response](../facts/cognito.md#cognito-pricing-m2m-per-token-no-app-client-charge)
  say: per token response
cognito-pricing-no-free-tier-plus
  claim: For users who sign in directly or through a social identity provider, the user pool free tier applies only to user pools configured to the Lite or Essentials tier; there is no free tier for the Plus tier.
  scope: user pool MAUs who sign in directly or through a social identity provider.
  link: [no free tier for the Plus tier](../facts/cognito.md#cognito-pricing-no-free-tier-plus)
  say: no free tier for Plus
cognito-pricing-three-tiers-essentials-default
  claim: User pools have three pricing tiers, Lite, Essentials and Plus; Essentials is the default tier for new user pools, and you can switch a user pool between tiers at any time.
  scope: per user pool; default; adjustable; switch tiers anytime.
  link: [Essentials will be the default tier](../facts/cognito.md#cognito-pricing-three-tiers-essentials-default)
  link: [Lite, Essentials, or Plus](../facts/cognito.md#cognito-pricing-three-tiers-essentials-default)
  say: Essentials | Lite, Essentials or Plus
cognito-privatelink-identity-pools-all-operations
  claim: Amazon Cognito identity pools support all API operations through AWS PrivateLink; identity pools have no domain endpoints.
  scope: per interface VPC endpoint.
  link: [support all API operations through AWS PrivateLink](../facts/cognito.md#cognito-privatelink-identity-pools-all-operations)
  say: all of them
cognito-privatelink-user-pool-apis-not-domain-endpoints
  claim: Through an interface VPC endpoint (AWS PrivateLink) you can call all user pools API operations, but not operations that your application requests from the user pool OAuth 2.0 authorization server: M2M authorization with the OAuth 2.0 client credentials flow from the token endpoint, and sign-in with managed login and the classic hosted UI, are not supported. M2M authorization with the GetClientToken API operation is supported, because it doesn't require a user pool domain.
  scope: per interface VPC endpoint.
  link: [all user pools API operations](../facts/cognito.md#cognito-privatelink-user-pool-apis-not-domain-endpoints)
  say: the user pools API only
cognito-quota-app-clients-per-user-pool
  claim: A user pool can have 1,000 app clients by default; the quota is adjustable up to a maximum of 10,000.
  scope: per user pool; default; adjustable.
  link: [1,000](../facts/cognito.md#cognito-quota-app-clients-per-user-pool)
  link: [10,000](../facts/cognito.md#cognito-quota-app-clients-per-user-pool)
  say: one thousand | ten thousand
cognito-quota-client-authentication-rps
  claim: The ClientAuthentication category (client_credentials grant requests to the token endpoint, which generate credentials for machine-to-machine requests) has a default quota of 150 requests per second, and it is not adjustable.
  scope: per account, per Region (all user pools); default; not adjustable.
  link: [150](../facts/cognito.md#cognito-quota-client-authentication-rps)
  say: one hundred fifty requests per second
cognito-quota-custom-attributes-per-user-pool
  claim: A user pool can have at most 50 custom attributes, and this quota is not adjustable.
  scope: per user pool; maximum; not adjustable.
  link: [50](../facts/cognito.md#cognito-quota-custom-attributes-per-user-pool)
  say: fifty
cognito-quota-custom-domains-per-region
  claim: An account can have at most 4 custom domains for user pools per Region, and this quota is not adjustable.
  scope: per account, per Region; maximum; not adjustable.
  link: [4](../facts/cognito.md#cognito-quota-custom-domains-per-region)
  say: four
cognito-quota-email-messages-daily-default
  claim: A user pool can send at most 50 email messages per day per AWS account with the default email configuration, and this quota is not adjustable; for a higher email delivery volume you configure the user pool to use your Amazon SES email configuration.
  scope: per AWS account, per day; maximum; not adjustable; default Cognito email feature only; Amazon SES configuration lifts it.
  link: [50](../facts/cognito.md#cognito-quota-email-messages-daily-default)
  link: [use your Amazon SES email configuration](../facts/cognito.md#cognito-quota-email-messages-daily-default)
  say: fifty a day | use Amazon SES
cognito-quota-groups-per-user
  claim: A user pool user can belong to at most 100 groups, and this quota is not adjustable.
  scope: per user; maximum; not adjustable.
  link: [100](../facts/cognito.md#cognito-quota-groups-per-user)
  say: one hundred
cognito-quota-groups-per-user-pool
  claim: A user pool can have at most 10,000 groups, and this quota is not adjustable.
  scope: per user pool; maximum; not adjustable.
  link: [10,000](../facts/cognito.md#cognito-quota-groups-per-user-pool)
  say: ten thousand
cognito-quota-identities-per-identity-pool-unlimited
  claim: The number of identities per identity pool is unlimited.
  scope: per identity pool; maximum; not adjustable.
  link: [Unlimited](../facts/cognito.md#cognito-quota-identities-per-identity-pool-unlimited)
  say: unlimited
cognito-quota-identity-pools-per-account
  claim: An account can have 1,000 identity pools by default, and the quota is adjustable.
  scope: per account (per Region, per the page intro); default; adjustable.
  link: [1,000](../facts/cognito.md#cognito-quota-identity-pools-per-account)
  say: one thousand
cognito-quota-identity-providers-per-user-pool
  claim: A user pool can have 300 identity providers by default; the quota is adjustable up to a maximum of 1,000.
  scope: per user pool; default; adjustable.
  link: [300](../facts/cognito.md#cognito-quota-identity-providers-per-user-pool)
  link: [1,000](../facts/cognito.md#cognito-quota-identity-providers-per-user-pool)
  say: three hundred | one thousand
cognito-quota-linked-identities-per-user
  claim: At most 5 identities can be linked to one user pool user, and this quota is not adjustable.
  scope: per user; maximum; not adjustable.
  link: [5](../facts/cognito.md#cognito-quota-linked-identities-per-user)
  say: five
cognito-quota-rbac-rules
  claim: For each user pool or other authentication provider that you configure for an identity pool, you can create up to 25 role-based access control (RBAC) rules, and this limit is not adjustable.
  scope: per authentication provider (user pool or other provider) configured for an identity pool; maximum; not adjustable.
  link: [25](../facts/cognito.md#cognito-quota-rbac-rules)
  say: twenty-five
cognito-quota-role-mapping-identity-providers
  claim: Role mappings can be specified for at most 10 identity providers in an identity pool, and this quota is not adjustable.
  scope: per identity pool; maximum; not adjustable.
  link: [10](../facts/cognito.md#cognito-quota-role-mapping-identity-providers)
  say: ten
cognito-quota-user-authentication-rps
  claim: The UserAuthentication category of user pool operations (sign-in with InitiateAuth, RespondToAuthChallenge, token refresh and managed login sign-in) has a default quota of 120 requests per second, and it is adjustable.
  scope: per account, per Region (all user pools); default; adjustable.
  link: [120](../facts/cognito.md#cognito-quota-user-authentication-rps)
  say: one hundred twenty requests per second
cognito-quota-user-creation-rps
  claim: The UserCreation category of user pool operations (SignUp, ConfirmSignUp, AdminCreateUser and AdminConfirmSignUp) has a default quota of 50 requests per second, and it is adjustable.
  scope: per account, per Region (all user pools); default; adjustable.
  link: [50](../facts/cognito.md#cognito-quota-user-creation-rps)
  say: fifty requests per second
cognito-quota-user-federation-rps
  claim: The UserFederation category, which covers sign-in through a third-party identity provider, has a default quota of 25 requests per second, and it is adjustable.
  scope: per account, per Region (all user pools); default; adjustable.
  link: [25](../facts/cognito.md#cognito-quota-user-federation-rps)
  say: twenty-five requests per second
cognito-quota-user-import-csv
  claim: A user import CSV file can be at most 100 MB, and this quota is not adjustable.
  scope: per CSV file (user import job); maximum; not adjustable.
  link: [100 MB](../facts/cognito.md#cognito-quota-user-import-csv)
  say: one hundred megabytes
cognito-quota-user-pool-providers-per-identity-pool
  claim: An identity pool can have 50 Amazon Cognito user pool providers by default; the quota is adjustable up to a maximum of 1000.
  scope: per identity pool; default; adjustable.
  link: [50](../facts/cognito.md#cognito-quota-user-pool-providers-per-identity-pool)
  link: [1000](../facts/cognito.md#cognito-quota-user-pool-providers-per-identity-pool)
  say: fifty | one thousand
cognito-quota-user-pools-per-region
  claim: An account can have 1,000 user pools per Region by default; the quota is adjustable up to a maximum of 10,000.
  scope: per account, per Region; default; adjustable.
  link: [1,000](../facts/cognito.md#cognito-quota-user-pools-per-region)
  link: [10,000](../facts/cognito.md#cognito-quota-user-pools-per-region)
  say: one thousand | ten thousand
cognito-quota-users-per-import-csv
  claim: A user import CSV file can hold at most 500,000 users, and this quota is not adjustable.
  scope: per CSV file (user import job); maximum; not adjustable.
  link: [500,000](../facts/cognito.md#cognito-quota-users-per-import-csv)
  say: five hundred thousand
cognito-quota-users-per-user-pool
  claim: A user pool can hold 40,000,000 users by default, and the quota is adjustable through your account team.
  scope: per user pool; default; adjustable; higher values: contact your account team.
  link: [40,000,000](../facts/cognito.md#cognito-quota-users-per-user-pool)
  say: forty million
cognito-refresh-token-default-30-days
  claim: By default a user pool refresh token expires 30 days after the user signs in; for each app client you can set the refresh token expiration to any value between 60 minutes and 10 years.
  scope: per app client; default; adjustable.
  link: [30 days](../facts/cognito.md#cognito-refresh-token-default-30-days)
  link: [60 minutes](../facts/cognito.md#cognito-refresh-token-default-30-days)
  link: [10 years](../facts/cognito.md#cognito-refresh-token-default-30-days)
  say: thirty days | sixty minutes | ten years
cognito-refresh-token-rotation-behavior
  claim: With refresh token rotation on, every token refresh returns a new ID, access and refresh token and invalidates the original refresh token; the new refresh token is valid only for the remaining time of the original, and the original can keep a grace period of up to 60 seconds.
  scope: per app client; maximum; refresh token rotation enabled.
  link: [up to 60 seconds](../facts/cognito.md#cognito-refresh-token-rotation-behavior)
  link: [the remaining duration of the original refresh token](../facts/cognito.md#cognito-refresh-token-rotation-behavior)
  say: up to sixty seconds | no extension of the window
cognito-refresh-token-rotation-not-with-refresh-token-auth
  claim: REFRESH_TOKEN_AUTH isn't available in app clients with refresh token rotation enabled; in app clients with refresh token rotation active, you use the GetTokensFromRefreshToken API operation.
  scope: per app client.
  link: [isn't available in app clients](../facts/cognito.md#cognito-refresh-token-rotation-not-with-refresh-token-auth)
  say: not with rotation
cognito-refresh-token-validity-range
  claim: The validity of a user pool refresh token can be set from 1 hour to 3,650 days.
  scope: per app client (user pool tokens); maximum; not adjustable; allowed setting range.
  link: [1 hour](../facts/cognito.md#cognito-refresh-token-validity-range)
  link: [3,650 days](../facts/cognito.md#cognito-refresh-token-validity-range)
  say: one hour | three thousand six hundred fifty days, about ten years
cognito-remember-devices-suppress-mfa
  claim: A Cognito user pool can remember the devices users sign in from and can use remembered devices to suppress second-factor challenges when MFA is set up.
  scope: Cognito user pool MFA with remembered devices; multi-factor authentication is set up.
  link: [remember devices used to access your application](../facts/cognito.md#cognito-remember-devices-suppress-mfa)
  link: [suppress second factor challenges](../facts/cognito.md#cognito-remember-devices-suppress-mfa)
cognito-request-quotas-per-region-per-account
  claim: Each Amazon Cognito quota is a maximum volume of requests in one AWS Region in one AWS account, and AWS grants a quota increase in one Region at a time.
  scope: per account, per Region.
  link: [in one AWS Region in one AWS account](../facts/cognito.md#cognito-request-quotas-per-region-per-account)
  say: per Region, per account
cognito-request-quotas-two-million-mau
  claim: User pool category quotas are measured in monthly active users (MAUs): AWS accounts with fewer than two million MAUs can operate within the default quota.
  scope: per account, per Region.
  link: [two million MAUs](../facts/cognito.md#cognito-request-quotas-two-million-mau)
  say: two million monthly active users
cognito-resource-server-custom-scopes
  claim: A resource server is an OAuth 2.0 API server that checks that access tokens from the user pool contain the scopes that authorize the requested method and path; custom scopes, which you define on resource servers, authorize requests to the APIs that the resource servers protect.
  scope: Cognito user pool resource servers and custom scopes.
  link: [is an OAuth 2.0 API server](../facts/cognito.md#cognito-resource-server-custom-scopes)
  link: [Custom scopes authorize requests to the external APIs](../facts/cognito.md#cognito-resource-server-custom-scopes)
  say: an OAuth API server | custom scopes authorize API calls
cognito-saml-idp-initiated-app-client-saml-only
  claim: When an app client supports a SAML 2.0 IdP with IdP-initiated sign-in, you can add only other SAML 2.0 IdPs to that app client; the user pool directory and all non-SAML external identity providers cannot be added to it.
  scope: per app client with IdP-initiated SAML sign-in; a SAML 2.0 IdP that supports IdP-initiated sign-in is active in the app client.
  link: [you can only add other SAML 2.0 IdPs](../facts/cognito.md#cognito-saml-idp-initiated-app-client-saml-only)
  link: [all non-SAML external identity providers](../facts/cognito.md#cognito-saml-idp-initiated-app-client-saml-only)
  say: only other SAML providers | no local users and no social or OIDC providers
cognito-saml-idp-must-support-saml-2
  claim: Web and mobile app users can sign in to a user pool through a SAML IdP such as AD FS or Shibboleth, which must support SAML 2.0; Cognito processes the SAML assertions and issues its own JWTs, and the IdP is configured with the user pool's SP entity ID and ACS URL.
  scope: SAML identity providers in a Cognito user pool.
  link: [issues JSON web tokens (JWTs)](../facts/cognito.md#cognito-saml-idp-must-support-saml-2)
  link: [assertion consumer service (ACS) URL](../facts/cognito.md#cognito-saml-idp-must-support-saml-2)
cognito-saml-sign-requests-encrypt-responses
  claim: A user pool signs all SAML single logout requests and can be set to sign SAML single sign-on requests to any external SAML IdP; an IdP configured for SAML encryption encrypts its SAML responses with the encryption certificate that Amazon Cognito generates for that provider.
  scope: SAML identity providers in a Cognito user pool.
  link: [signs all single logout (SLO) requests](../facts/cognito.md#cognito-saml-sign-requests-encrypt-responses)
  link: [encrypt SAML responses with the encryption certificate](../facts/cognito.md#cognito-saml-sign-requests-encrypt-responses)
  say: it signs SAML requests | the IdP can encrypt responses
cognito-security-in-the-cloud-not-pci-dss
  claim: AWS's security of the cloud for Amazon Cognito is compliant with SOC 1-3, PCI DSS and ISO 27001 and is HIPAA-BAA eligible, but the security in the cloud that a customer designs in Amazon Cognito can be compliant with SOC1-3, ISO 27001 and HIPAA-BAA, but not PCI DSS.
  scope: Amazon Cognito compliance under the shared responsibility model.
  link: [but not PCI DSS](../facts/cognito.md#cognito-security-in-the-cloud-not-pci-dss)
  link: [is HIPAA-BAA eligible](../facts/cognito.md#cognito-security-in-the-cloud-not-pci-dss)
cognito-signup-confirmation-code-validity
  claim: A user pool sign-up confirmation code is valid for 24 hours, and this quota is not adjustable.
  scope: per confirmation code; fixed; not adjustable.
  link: [24 hours](../facts/cognito.md#cognito-signup-confirmation-code-validity)
  say: twenty-four hours
cognito-sms-charged-separately
  claim: SMS messages that Cognito sends for phone verification, password reset codes or MFA are charged separately.
  scope: SMS messages sent by Cognito.
  link: [is charged separately](../facts/cognito.md#cognito-sms-charged-separately)
cognito-sync-store-key-value-per-identity
  claim: The Cognito FAQ describes the Amazon Cognito Sync store as a key/value pair store linked to an Amazon Cognito identity, with no limit to the number of identities in identity pools and the sync store. Amazon Cognito Sync is no longer open to new customers.
  scope: identities in identity pools and the sync store; maximum; not adjustable.
  link: [a key/value pair store](../facts/cognito.md#cognito-sync-store-key-value-per-identity)
  link: [no limit to the number of identities](../facts/cognito.md#cognito-sync-store-key-value-per-identity)
cognito-threat-protection-plus-plan-audit-mode
  claim: Threat protection (formerly advanced security features) monitors and can automatically shut down malicious activity in a user pool, can run in audit mode that only publishes metrics to CloudWatch, and is available in the Plus feature plan.
  scope: Cognito user pool threat protection.
  link: [available in the Plus feature plan](../facts/cognito.md#cognito-threat-protection-plus-plan-audit-mode)
  link: [use audit mode to gather metrics](../facts/cognito.md#cognito-threat-protection-plus-plan-audit-mode)
  link: [formerly called *advanced security features*](../facts/cognito.md#cognito-threat-protection-plus-plan-audit-mode)
  changed: 2024-11: was advanced security features
cognito-tier-adaptive-auth-plus-only
  claim: Risk-based adaptive authentication is available only in the Plus tier.
  scope: per user pool.
  link: [Risk-based adaptive authentication](../facts/cognito.md#cognito-tier-adaptive-auth-plus-only)
  say: Plus only
cognito-tier-compromised-credentials-plus-only
  claim: Compromised credentials detection to protect against unsafe passwords is available only in the Plus tier.
  scope: per user pool.
  link: [Compromised credentials detection](../facts/cognito.md#cognito-tier-compromised-credentials-plus-only)
  say: Plus only
cognito-tier-email-mfa-essentials-plus
  claim: MFA with email one-time codes is available in the Essentials and Plus tiers, not in Lite.
  scope: per user pool.
  link: [MFA with email one-time codes](../facts/cognito.md#cognito-tier-email-mfa-essentials-plus)
  say: Essentials and Plus only
cognito-tier-multi-region-addon-essentials-plus
  claim: Multi-Region replication is an add-on for the Essentials and Plus tiers and is not offered in Lite.
  scope: per user pool.
  link: [Multi-Region replication](../facts/cognito.md#cognito-tier-multi-region-addon-essentials-plus)
  say: add-on for Essentials and Plus
cognito-tier-passkeys-essentials-plus
  claim: Passkey sign-in with biometrics and hardware keys is available in the Essentials and Plus tiers, not in Lite.
  scope: per user pool.
  link: [Passkeys sign-in with biometrics and hardware keys](../facts/cognito.md#cognito-tier-passkeys-essentials-plus)
  say: passkeys: Essentials and Plus
cognito-tier-refresh-token-rotation-essentials-plus
  claim: Refresh token rotation is supported in the Essentials and Plus tiers, not in Lite.
  scope: per user pool.
  link: [Support for refresh token rotation](../facts/cognito.md#cognito-tier-refresh-token-rotation-essentials-plus)
  say: Essentials and Plus
cognito-tier-sla-99-9
  claim: All three tiers (Lite, Essentials and Plus) come with a 99.9% service level agreement.
  scope: per tier.
  link: [99.9%](../facts/cognito.md#cognito-tier-sla-99-9)
  say: ninety-nine point nine percent
cognito-tier-sms-totp-mfa-all-tiers
  claim: MFA with authenticator apps and SMS one-time codes is available in all three tiers: Lite, Essentials and Plus.
  scope: per user pool.
  link: [MFA with authenticator apps and SMS one-time codes](../facts/cognito.md#cognito-tier-sms-totp-mfa-all-tiers)
  say: authenticator app and SMS MFA in every tier
cognito-token-revocation-enabled-by-default
  claim: Token revocation is enabled by default when a new user pool app client is created, and refresh tokens can be revoked only in app clients with token revocation enabled.
  scope: per Cognito user pool app client; default; adjustable; new user pool clients.
  link: [token revocation is enabled by default](../facts/cognito.md#cognito-token-revocation-enabled-by-default)
  link: [only in app clients with token revocation enabled](../facts/cognito.md#cognito-token-revocation-enabled-by-default)
cognito-token-revocation-refresh-token-and-global-signout
  claim: Revoking a refresh token invalidates all access tokens issued from it; GlobalSignOut (authorized by the user's access token) and AdminUserGlobalSignOut (authorized by an administrator's IAM credentials) revoke all of a user's refresh, ID and access tokens; revoked JWTs still pass a check by any JWT library that only verifies signature and expiration.
  scope: Cognito user pool tokens; token revocation enabled on the app client.
  link: [issued by that refresh token become invalid](../facts/cognito.md#cognito-token-revocation-refresh-token-and-global-signout)
  link: [target user's refresh, ID, and access tokens](../facts/cognito.md#cognito-token-revocation-refresh-token-and-global-signout)
  link: [revoked tokens will still be valid](../facts/cognito.md#cognito-token-revocation-refresh-token-and-global-signout)
cognito-unauthenticated-role-more-restrictive
  claim: An identity pool can have default IAM roles for authenticated and unauthenticated users; the unauthenticated identities are assumed by users who do not log in, so their permissions should typically be more restrictive than those for authenticated identities.
  scope: Cognito identity pool roles.
  link: [default IAM roles for authenticated and unauthenticated users](../facts/cognito.md#cognito-unauthenticated-role-more-restrictive)
  link: [should be more restrictive](../facts/cognito.md#cognito-unauthenticated-role-more-restrictive)
cognito-user-migration-jit-lambda-no-reset
  claim: Users move into Cognito user pools by just-in-time migration or bulk migration; the just-in-time Lambda trigger migrates users at sign-in without forcing a password reset.
  scope: migrating users into a Cognito user pool; just-in-time migration with the Lambda trigger.
  link: [just-in-time (JIT) migration and bulk migration](../facts/cognito.md#cognito-user-migration-jit-lambda-no-reset)
  link: [without forcing them to reset their password](../facts/cognito.md#cognito-user-migration-jit-lambda-no-reset)
cognito-user-pool-federated-users-get-profile-and-jwt
  claim: Federated and local users both have a user profile in the user pool; the user pool accepts tokens and assertions from third-party IdPs and collects the user attributes into a JWT that it issues to the app, so the app works with one set of JWTs.
  scope: Cognito user pool federation.
  link: [Federated and local users have a user profile](../facts/cognito.md#cognito-user-pool-federated-users-get-profile-and-jwt)
  link: [collect the user attributes into a JWT](../facts/cognito.md#cognito-user-pool-federated-users-get-profile-and-jwt)
  link: [standardize your app on one set of JWTs](../facts/cognito.md#cognito-user-pool-federated-users-get-profile-and-jwt)
cognito-user-pool-federation-independent-of-identity-pool
  claim: Sign-in through a third-party IdP is a feature of Cognito user pools and is independent of federation through identity pools, which must be set up separately in each identity pool; a user pool can be a third-party IdP to an identity pool.
  scope: Cognito federation.
  link: [independent of federation through Amazon Cognito identity pools](../facts/cognito.md#cognito-user-pool-federation-independent-of-identity-pool)
  link: [third-party IdP to an identity pool](../facts/cognito.md#cognito-user-pool-federation-independent-of-identity-pool)
cognito-user-pool-is-user-directory
  claim: A Cognito user pool is a tenant-based user directory for web and mobile apps that stores users' profile attributes and supports a custom schema.
  scope: Cognito user pools.
  link: [a tenant-based user directory](../facts/cognito.md#cognito-user-pool-is-user-directory)
  link: [supports a custom schema](../facts/cognito.md#cognito-user-pool-is-user-directory)
cognito-user-pool-password-policies
  claim: A Cognito user pool can set password policies such as password length, character complexity and password history.
  scope: per user pool.
  link: [set up password policies](../facts/cognito.md#cognito-user-pool-password-policies)
  link: [password history requirements](../facts/cognito.md#cognito-user-pool-password-policies)
cognito-user-pool-sp-and-idp-dual-role
  claim: A Cognito user pool can act both as a service provider to external IdPs and as an IdP to your app, connecting to consumer IdPs such as Facebook and Google or workforce IdPs such as Okta and AD FS.
  scope: Cognito user pool federation.
  link: [a dual role as a service provider (SP)](../facts/cognito.md#cognito-user-pool-sp-and-idp-dual-role)
  link: [consumer IdPs like Facebook and Google](../facts/cognito.md#cognito-user-pool-sp-and-idp-dual-role)
  link: [workforce IdPs like Okta](../facts/cognito.md#cognito-user-pool-sp-and-idp-dual-role)
cognito-user-pool-vs-identity-pool
  claim: A Cognito user pool is a user directory that authenticates users and issues JSON web tokens to your app or API; a Cognito identity pool exchanges a trusted token for temporary, limited-privilege AWS credentials so the app can call AWS services on the user's behalf.
  scope: Cognito user pools and identity pools.
  link: [issue JSON web tokens (JWTs)](../facts/cognito.md#cognito-user-pool-vs-identity-pool)
  link: [temporary, limited-privilege AWS credentials](../facts/cognito.md#cognito-user-pool-vs-identity-pool)
cognito-user-pool-workforce-sso-in-your-app
  claim: With user pools you can provide single sign-on in your app for an organization's workforce identities in SAML 2.0 and OIDC IdPs, and for customer identities from Amazon, Google, Apple and Facebook.
  scope: Cognito user pool federation.
  link: [workforce identities in SAML 2.0 and OIDC IdPs](../facts/cognito.md#cognito-user-pool-workforce-sso-in-your-app)
  link: [Amazon, Google, Apple and Facebook](../facts/cognito.md#cognito-user-pool-workforce-sso-in-your-app)
cognito-user-pools-billed-by-mau
  claim: Cognito user pools are billed by monthly active users (MAUs): a user counts once in a calendar month when an identity operation such as sign-up, sign-in, sign-out, token refresh or password change happens for that user; inactive users are not charged.
  scope: per calendar month.
  link: [monthly active users (MAUs)](../facts/cognito.md#cognito-user-pools-billed-by-mau)
  link: [not charged for subsequent sessions](../facts/cognito.md#cognito-user-pools-billed-by-mau)
cognito-wa-centralized-idp-for-application-users
  claim: For users of the applications you build, the security pillar says to use Amazon Cognito as a centralized identity provider; Cognito's identity store scales to millions of users and supports social and enterprise identity federation.
  scope: users of applications you build.
  link: [a centralized identity provider towards your applications](../facts/cognito.md#cognito-wa-centralized-idp-for-application-users)
  link: [scales to millions of users](../facts/cognito.md#cognito-wa-centralized-idp-for-application-users)
  link: [supports social and enterprise identity federation](../facts/cognito.md#cognito-wa-centralized-idp-for-application-users)
cognito-waf-all-plans-billed-separately
  claim: AWS WAF web ACLs are available in all user pool feature plans, complement Amazon Cognito threat protection, and AWS WAF bills separately for inspecting user pool requests.
  scope: per user pool.
  link: [available in all user pool feature plans](../facts/cognito.md#cognito-waf-all-plans-billed-separately)
  link: [AWS WAF bills separately](../facts/cognito.md#cognito-waf-all-plans-billed-separately)
  say: every plan | WAF bills separately
cognito-waf-covers-managed-login-and-public-apis
  claim: An AWS WAF web ACL on a user pool inspects requests to the managed login and classic hosted UI endpoints and to the public (unauthenticated or token-authorized) user pool API operations such as InitiateAuth; you can associate one web ACL with each user pool.
  scope: per user pool; maximum.
  link: [managed login, and Amazon Cognito API](../facts/cognito.md#cognito-waf-covers-managed-login-and-public-apis)
  link: [one web ACL with each user pool](../facts/cognito.md#cognito-waf-covers-managed-login-and-public-apis)
  say: hosted UI, managed login and the public APIs | one web ACL per user pool
directory-service-ad-connector-aws-apps-only-no-third-party
  claim: AD Connector is an Active Directory proxy for AWS created applications and services only; no third-party applications work with AD Connector.
  scope: AD Connector.
  link: [for AWS created applications and services only](../facts/directory-service.md#directory-service-ad-connector-aws-apps-only-no-third-party)
  link: [no third-party applications that work](../facts/directory-service.md#directory-service-ad-connector-aws-apps-only-no-third-party)
directory-service-ad-connector-console-sign-in-and-radius-mfa
  claim: AD Connector lets users access the AWS Management Console with their existing Active Directory credentials, and it can enable MFA for AWS application users by connecting to the existing RADIUS-based MFA infrastructure.
  scope: AD Connector.
  link: [access the AWS Management Console](../facts/directory-service.md#directory-service-ad-connector-console-sign-in-and-radius-mfa)
  link: [your existing RADIUS-based MFA infrastructure](../facts/directory-service.md#directory-service-ad-connector-console-sign-in-and-radius-mfa)
directory-service-ad-connector-console-without-saml
  claim: AD Connector can authenticate AWS Management Console users with their Active Directory credentials without setting up SAML infrastructure.
  scope: AD Connector.
  link: [without setting up SAML infrastructure](../facts/directory-service.md#directory-service-ad-connector-console-without-saml)
directory-service-ad-connector-ec2-join-bypasses-connector
  claim: Through AD Connector, EC2 Windows or Linux instances can use seamless domain join to join the self-managed (on-premises) Active Directory; once joined, the instance communicates directly with Active Directory and bypasses AD Connector.
  scope: EC2 seamless domain join with AD Connector.
  link: [bypasses AD Connector](../facts/directory-service.md#directory-service-ad-connector-ec2-join-bypasses-connector)
  link: [communicates directly with your Active Directory](../facts/directory-service.md#directory-service-ad-connector-ec2-join-bypasses-connector)
directory-service-ad-connector-gateway-no-caching
  claim: AD Connector is a directory gateway that redirects directory requests to your on-premises Microsoft Active Directory without caching any information in the cloud.
  scope: AD Connector.
  link: [a directory gateway](../facts/directory-service.md#directory-service-ad-connector-gateway-no-caching)
  link: [without caching any information in the cloud](../facts/directory-service.md#directory-service-ad-connector-gateway-no-caching)
directory-service-ad-connector-is-a-proxy
  claim: AD Connector is a proxy service that connects compatible AWS applications, such as WorkSpaces, Amazon Quick and EC2 Windows Server instances, to an existing on-premises Microsoft Active Directory; it forwards users' sign-in requests to the on-premises domain controllers for authentication.
  scope: AD Connector.
  link: [AD Connector is a proxy service](../facts/directory-service.md#directory-service-ad-connector-is-a-proxy)
  link: [forwards sign-in requests to your on-premises Active Directory](../facts/directory-service.md#directory-service-ad-connector-is-a-proxy)
directory-service-ad-connector-needs-vpn-or-direct-connect
  claim: AD Connector needs a VPC with at least two subnets, each in a different Availability Zone, and the VPC must be connected to the existing network through a VPN connection or AWS Direct Connect.
  scope: AD Connector prerequisites.
  link: [(VPN) connection or Direct Connect](../facts/directory-service.md#directory-service-ad-connector-needs-vpn-or-direct-connect)
  link: [At least two subnets](../facts/directory-service.md#directory-service-ad-connector-needs-vpn-or-direct-connect)
  link: [in a different Availability Zone](../facts/directory-service.md#directory-service-ad-connector-needs-vpn-or-direct-connect)
directory-service-ad-connector-no-data-replicated
  claim: With AD Connector, all directory data remains on the existing domain controllers; Directory Service does not replicate any of the directory data.
  scope: AD Connector.
  link: [remains on your domain controllers](../facts/directory-service.md#directory-service-ad-connector-no-data-replicated)
  link: [does not replicate any of your directory data](../facts/directory-service.md#directory-service-ad-connector-no-data-replicated)
directory-service-ad-connector-no-directory-sync
  claim: AD Connector removes the need for directory synchronization and for hosting a federation infrastructure; you keep managing users, groups and passwords in the on-premises Active Directory with standard tools.
  scope: AD Connector.
  link: [eliminates the need of directory synchronization](../facts/directory-service.md#directory-service-ad-connector-no-directory-sync)
  link: [manage your Active Directory as you do now](../facts/directory-service.md#directory-service-ad-connector-no-directory-sync)
directory-service-ad-connector-no-transitive-trusts
  claim: AD Connector does not support Active Directory transitive trusts; AD Connectors and on-premises domains have a 1-to-1 relationship, so each on-premises domain, including child domains, needs its own AD Connector.
  scope: AD Connector.
  link: [does not support Active Directory transitive trusts](../facts/directory-service.md#directory-service-ad-connector-no-transitive-trusts)
  link: [have a 1-to-1 relationship](../facts/directory-service.md#directory-service-ad-connector-no-transitive-trusts)
  link: [you must create a unique AD Connector](../facts/directory-service.md#directory-service-ad-connector-no-transitive-trusts)
directory-service-ad-connector-not-rds-sql-server
  claim: AD Connector is not compatible with Amazon RDS for SQL Server.
  scope: AD Connector.
  link: [not compatible with RDS SQL Server](../facts/directory-service.md#directory-service-ad-connector-not-rds-sql-server)
directory-service-ad-connector-not-shareable-not-multi-vpc
  claim: AD Connector cannot be shared with other AWS accounts (AWS suggests sharing AWS Managed Microsoft AD instead), and it is not multi-VPC aware, so applications such as WorkSpaces must be provisioned in the same VPC as the AD Connector.
  scope: AD Connector.
  link: [cannot be shared with other AWS accounts](../facts/directory-service.md#directory-service-ad-connector-not-shareable-not-multi-vpc)
  link: [not multi-VPC aware](../facts/directory-service.md#directory-service-ad-connector-not-shareable-not-multi-vpc)
  link: [the same VPC as your AD Connector](../facts/directory-service.md#directory-service-ad-connector-not-shareable-not-multi-vpc)
directory-service-ad-connector-two-sizes
  claim: AD Connector comes in two sizes, small and large: small for smaller organizations with a low number of operations per second, large for a moderate to high number; it has no enforced user or connection limits, and you can spread load across several AD Connectors.
  scope: per AD Connector; fixed; not adjustable.
  link: [two sizes, small and large](../facts/directory-service.md#directory-service-ad-connector-two-sizes)
  link: [no enforced user or connection limits](../facts/directory-service.md#directory-service-ad-connector-two-sizes)
  say: small and large | no user or connection limits
directory-service-ad-connector-when-to-use
  claim: AD Connector is the best choice when you want to use your existing on-premises directory with compatible AWS services.
  scope: AWS Directory Service directory types.
  link: [use your existing on-premises directory](../facts/directory-service.md#directory-service-ad-connector-when-to-use)
directory-service-change-edition-upgrade-api-2025-10
  claim: Since 2025-10-02 you can upgrade AWS Managed Microsoft AD from Standard to Enterprise Edition yourself through the UpdateDirectorySetup API, without a support ticket.
  scope: per directory; through the UpdateDirectorySetup API.
  link: [2025-10-02](../facts/directory-service.md#directory-service-change-edition-upgrade-api-2025-10)
  link: [upgrade Managed Microsoft AD from Standard to Enterprise](../facts/directory-service.md#directory-service-change-edition-upgrade-api-2025-10)
  say: October second, twenty twenty-five | Standard to Enterprise upgrade
directory-service-change-hybrid-edition-2025-07
  claim: On 2025-07-30 AWS added AWS Managed Microsoft AD (Hybrid Edition), which connects your self-managed Active Directory with AWS Directory Service for Microsoft Active Directory.
  scope: per directory.
  link: [July 30, 2025](../facts/directory-service.md#directory-service-change-hybrid-edition-2025-07)
  link: [connects your self-managed Active Directory](../facts/directory-service.md#directory-service-change-hybrid-edition-2025-07)
  say: July thirtieth, twenty twenty-five | connects your own AD to AWS
directory-service-change-multi-region-opt-in-2026-04
  claim: Since 2026-04-01 AWS Managed Microsoft AD supports multi-Region replication in AWS opt-in Regions, except Middle East (UAE) and Middle East (Bahrain); you pay by the hour for the domain controllers in each Region plus cross-Region data transfer.
  scope: per AWS Managed Microsoft AD directory; opt-in Regions where AWS Managed Microsoft AD is available, except UAE and Bahrain.
  link: [2026-04-01](../facts/directory-service.md#directory-service-change-multi-region-opt-in-2026-04)
  link: [You pay by the hour](../facts/directory-service.md#directory-service-change-multi-region-opt-in-2026-04)
  say: April first, twenty twenty-six | hourly per domain controller, plus data transfer
directory-service-change-sharing-limits-2025-08
  claim: On 2025-08-15 AWS raised the directory sharing limits of AWS Managed Microsoft AD: Standard Edition from 5 to 25 accounts and Enterprise Edition from 125 to 500 accounts.
  scope: per directory.
  link: [2025-08-15](../facts/directory-service.md#directory-service-change-sharing-limits-2025-08)
  link: [from 5 to 25 accounts](../facts/directory-service.md#directory-service-change-sharing-limits-2025-08)
  link: [from 125 to 500 accounts](../facts/directory-service.md#directory-service-change-sharing-limits-2025-08)
  say: August fifteenth, twenty twenty-five | five to twenty-five | one hundred twenty-five to five hundred
  changed: 2025-08-15: was The Standard Edition limit has increased from 5 to 25 accounts
directory-service-change-simple-ad-announced-2026-06
  claim: On 2026-06-30 AWS announced that Simple AD will no longer be open to new customers starting July 30, 2026, and that existing customers retain full functionality.
  scope: existing and new customers.
  link: [June 30, 2026](../facts/directory-service.md#directory-service-change-simple-ad-announced-2026-06)
  link: [Existing customers retain full functionality](../facts/directory-service.md#directory-service-change-simple-ad-announced-2026-06)
  say: June thirtieth, twenty twenty-six | existing customers keep everything
directory-service-change-simple-ad-closed-2026-07
  claim: On 2026-07-30 the guide history marks Simple AD as no longer open to new customers.
  scope: new customers.
  link: [July 30, 2026](../facts/directory-service.md#directory-service-change-simple-ad-closed-2026-07)
  say: July thirtieth, twenty twenty-six
  changed: 2026-07-30: was Simple AD
directory-service-console-access-iam-roles-access-url
  claim: Directory members have no access to AWS resources by default; to give them AWS Management Console access you assign IAM roles to directory users or groups, and the directory must have an access URL.
  scope: AWS Management Console access with AWS Managed Microsoft AD credentials.
  link: [do not have access to any AWS resources](../facts/directory-service.md#directory-service-console-access-iam-roles-access-url)
  link: [You assign IAM roles to your directory members](../facts/directory-service.md#directory-service-console-access-iam-roles-access-url)
  link: [your directory must have an access URL](../facts/directory-service.md#directory-service-console-access-iam-roles-access-url)
directory-service-console-sso-iam-roles
  claim: AWS Directory Service lets you assign IAM roles to users and groups in AWS Managed Microsoft AD, Simple AD, or an on-premises Active Directory through AD Connector, and gives a customer-specific console URL where they sign in with corporate credentials.
  scope: AWS Management Console access with directory credentials.
  link: [assign IAM roles](../facts/directory-service.md#directory-service-console-sso-iam-roles)
  link: [a customer-specific URL](../facts/directory-service.md#directory-service-console-sso-iam-roles)
directory-service-decision-guide-ad-dependent-workloads-row
  claim: In the identity decision guide table, to run Active Directory dependent workloads in AWS, the recommended service is AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD).
  scope: AWS identity decision guide.
  link: [Run Active Directory dependent workloads in AWS](../facts/directory-service.md#directory-service-decision-guide-ad-dependent-workloads-row)
  link: [also known as AWS Managed Microsoft AD](../facts/directory-service.md#directory-service-decision-guide-ad-dependent-workloads-row)
directory-service-decision-guide-join-on-premises-ad-row
  claim: In the identity decision guide table, to join AWS workloads to an on-premises Microsoft Active Directory Domain Services, the recommended service is AWS Managed Microsoft AD.
  scope: AWS identity decision guide.
  link: [Join my AWS workloads to my on-premises](../facts/directory-service.md#directory-service-decision-guide-join-on-premises-ad-row)
  link: [also known as AWS Managed Microsoft AD](../facts/directory-service.md#directory-service-decision-guide-join-on-premises-ad-row)
directory-service-decision-guide-managed-ad
  claim: The decision guide describes AWS Managed Microsoft AD as a highly available, fully managed Microsoft Active Directory service that extends on-premises Microsoft AD configurations to AWS and can join AWS resources such as EC2 instances, WorkSpaces desktops and RDS for SQL Server to the domain.
  scope: AWS Managed Microsoft AD.
  link: [a highly available, fully managed Microsoft Active Directory](../facts/directory-service.md#directory-service-decision-guide-managed-ad)
  link: [extends your on-premises Microsoft AD configurations to AWS](../facts/directory-service.md#directory-service-decision-guide-managed-ad)
  link: [Amazon EC2 instances, Amazon WorkSpaces managed desktops](../facts/directory-service.md#directory-service-decision-guide-managed-ad)
directory-service-edition-upgrade-one-way
  claim: An upgrade of AWS Managed Microsoft AD from Standard to Enterprise Edition cannot be reverted, earlier snapshots cannot restore the upgraded directory, the upgrade takes four to five hours, and it adds cost.
  scope: per directory; Standard to Enterprise upgrade.
  link: [can't be reverted back to its previous edition](../facts/directory-service.md#directory-service-edition-upgrade-one-way)
  link: [four to five hours](../facts/directory-service.md#directory-service-edition-upgrade-one-way)
  say: no downgrade | four to five hours
directory-service-extend-on-prem-ad-trust-no-sync-or-admt
  claim: To extend an existing Active Directory to AWS, AWS Managed Microsoft AD connects to it with Active Directory trusts so users keep their on-premises credentials without synchronizing users, groups or passwords; alternatively, the on-premises domain can be migrated to AWS Managed Microsoft AD with the Active Directory Migration Toolkit (ADMT) and the Password Export Service.
  scope: AWS Managed Microsoft AD with an existing Active Directory.
  link: [synchronize users, groups, or passwords](../facts/directory-service.md#directory-service-extend-on-prem-ad-trust-no-sync-or-admt)
  link: [Active Directory Migration Toolkit (ADMT)](../facts/directory-service.md#directory-service-extend-on-prem-ad-trust-no-sync-or-admt)
directory-service-free-trial-1500-dc-hours
  claim: The Directory Service 30-day limited free trial gives 1,500 domain controller hours across all your managed directories during your first 30 days as a Directory Service customer; directory sharing does not qualify for the free trial.
  scope: per new Directory Service customer; maximum; first 30 days; sharing and multi-Region data transfer excluded.
  link: [1,500 domain controller hours](../facts/directory-service.md#directory-service-free-trial-1500-dc-hours)
  link: [30-day limited free trial](../facts/directory-service.md#directory-service-free-trial-1500-dc-hours)
  say: one thousand five hundred domain controller hours | thirty-day trial
directory-service-fsx-windows-needs-managed-ad-or-self-managed
  claim: An FSx for Windows File Server file system is joined to an Active Directory domain, either AWS Managed Microsoft AD or a self-managed Microsoft Active Directory; Amazon FSx does not support AD Connector or Simple AD.
  scope: FSx for Windows File Server Active Directory integration.
  link: [Amazon FSx does not support](../facts/directory-service.md#directory-service-fsx-windows-needs-managed-ad-or-self-managed)
  link: [Using a self-managed Microsoft Active Directory](../facts/directory-service.md#directory-service-fsx-windows-needs-managed-ad-or-self-managed)
directory-service-hybrid-edition-extends-existing-forest
  claim: With Hybrid Edition, you extend an existing Active Directory to AWS without a full migration: the AWS Managed Microsoft AD domain controllers join your existing forest and AD data replicates into AWS.
  scope: Hybrid Edition.
  link: [extend your existing Active Directory to AWS](../facts/directory-service.md#directory-service-hybrid-edition-extends-existing-forest)
  link: [become part of your existing AD forest](../facts/directory-service.md#directory-service-hybrid-edition-extends-existing-forest)
directory-service-managed-ad-actual-windows-server-ad
  claim: AWS Managed Microsoft AD is powered by an actual Microsoft Windows Server Active Directory, managed by AWS in the AWS Cloud, and lets you migrate a broad range of Active Directory-aware applications to AWS.
  scope: AWS Managed Microsoft AD.
  link: [an actual Microsoft Windows Server Active Directory](../facts/directory-service.md#directory-service-managed-ad-actual-windows-server-ad)
  link: [managed by AWS in the AWS Cloud](../facts/directory-service.md#directory-service-managed-ad-actual-windows-server-ad)
directory-service-managed-ad-admin-account-limited-to-ou
  claim: The Admin account that AWS creates in AWS Managed Microsoft AD can manage users, groups, computers, group policies and OUs inside the AWS-created OU, plus some domain-wide DNS and log tasks, but it lacks permissions for directory actions outside that OU, such as on the parent OU.
  scope: AWS Managed Microsoft AD Admin account.
  link: [Only the actions listed here are allowed](../facts/directory-service.md#directory-service-managed-ad-admin-account-limited-to-ou)
  link: [outside of your specific OU](../facts/directory-service.md#directory-service-managed-ad-admin-account-limited-to-ou)
  link: [Create and link group policies.](../facts/directory-service.md#directory-service-managed-ad-admin-account-limited-to-ou)
directory-service-managed-ad-aws-and-third-party-apps
  claim: AWS Managed Microsoft AD is compatible with multiple AWS services and with third-party applications; AWS cannot guarantee that every third-party application is or will stay compatible.
  scope: AWS Managed Microsoft AD application compatibility.
  link: [multiple AWS services and third-party applications](../facts/directory-service.md#directory-service-managed-ad-aws-and-third-party-apps)
  link: [unable to guarantee that any application](../facts/directory-service.md#directory-service-managed-ad-aws-and-third-party-apps)
directory-service-managed-ad-aws-provides-snapshots-recovery
  claim: With AWS Managed Microsoft AD, AWS provides monitoring, daily snapshots and recovery as part of the service, while you add users and groups and administer Group Policy with familiar Active Directory tools from a Windows computer joined to the domain.
  scope: AWS Managed Microsoft AD.
  link: [monitoring, daily snapshots, and recovery](../facts/directory-service.md#directory-service-managed-ad-aws-provides-snapshots-recovery)
  link: [administer Group Policy using familiar Active Directory tools](../facts/directory-service.md#directory-service-managed-ad-aws-provides-snapshots-recovery)
directory-service-managed-ad-console-and-identity-center
  claim: On its own, AWS Managed Microsoft AD lets users sign in to the AWS Management Console with Active Directory credentials; together with IAM Identity Center, users can also get short-term credentials for the AWS SDK and CLI and use preconfigured SAML integrations to sign in to many cloud applications.
  scope: AWS Managed Microsoft AD.
  link: [supports federated use cases using Active Directory credentials](../facts/directory-service.md#directory-service-managed-ad-console-and-identity-center)
  link: [short-term credentials for use with the AWS SDK](../facts/directory-service.md#directory-service-managed-ad-console-and-identity-center)
  link: [preconfigured SAML integrations](../facts/directory-service.md#directory-service-managed-ad-console-and-identity-center)
directory-service-managed-ad-daily-backup-encrypted-ebs
  claim: AWS Managed Microsoft AD takes a backup automatically once per day, and its EBS volumes are encrypted at rest.
  scope: per AWS Managed Microsoft AD directory.
  link: [once per day](../facts/directory-service.md#directory-service-managed-ad-daily-backup-encrypted-ebs)
  link: [volumes are encrypted](../facts/directory-service.md#directory-service-managed-ad-daily-backup-encrypted-ebs)
directory-service-managed-ad-dc-pair-across-azs
  claim: AWS Managed Microsoft AD creates a highly available pair of domain controllers in your Amazon VPC across different Availability Zones, and AWS automatically manages host monitoring, recovery, data replication, snapshots and software updates.
  scope: per AWS Managed Microsoft AD directory.
  link: [a highly available pair of domain controllers](../facts/directory-service.md#directory-service-managed-ad-dc-pair-across-azs)
  link: [across different Availability Zones](../facts/directory-service.md#directory-service-managed-ad-dc-pair-across-azs)
  link: [host monitoring, recovery, data replication, snapshots](../facts/directory-service.md#directory-service-managed-ad-dc-pair-across-azs)
directory-service-managed-ad-delegated-ou-admin
  claim: When you create an AWS Managed Microsoft AD directory, you get an organizational unit (OU) and an administrative account with delegated administrative rights for that OU.
  scope: per AWS Managed Microsoft AD directory.
  link: [delegated administrative rights for the OU](../facts/directory-service.md#directory-service-managed-ad-delegated-ou-admin)
directory-service-managed-ad-eni-per-dc-never-delete
  claim: AWS Managed Microsoft AD creates an elastic network interface for each domain controller in your VPC; these ENIs are essential for connectivity and should never be deleted.
  scope: per AWS Managed Microsoft AD domain controller.
  link: [elastic network interface (ENI)](../facts/directory-service.md#directory-service-managed-ad-eni-per-dc-never-delete)
  link: [should never be deleted](../facts/directory-service.md#directory-service-managed-ad-eni-per-dc-never-delete)
directory-service-managed-ad-enterprise-object-capacity
  claim: AWS Managed Microsoft AD Enterprise and Hybrid Editions include 17 GB of directory object storage, which AWS estimates supports up to 100,000 users or 500,000 objects.
  scope: per Enterprise or Hybrid Edition directory; maximum; not adjustable; estimate; object sizes vary by company.
  link: [17 GB of directory object storage](../facts/directory-service.md#directory-service-managed-ad-enterprise-object-capacity)
  link: [up to 100,000 users](../facts/directory-service.md#directory-service-managed-ad-enterprise-object-capacity)
  link: [500,000 objects](../facts/directory-service.md#directory-service-managed-ad-enterprise-object-capacity)
directory-service-managed-ad-failed-dc-replaced-same-az-ip
  claim: A failed AWS Managed Microsoft AD domain controller is replaced automatically in the same Availability Zone with the same IP address, and a full disaster recovery can use the latest backup.
  scope: AWS Managed Microsoft AD domain controllers.
  link: [automatically replaced in the same Availability Zone](../facts/directory-service.md#directory-service-managed-ad-failed-dc-replaced-same-az-ip)
  link: [using the same IP address](../facts/directory-service.md#directory-service-managed-ad-failed-dc-replaced-same-az-ip)
directory-service-managed-ad-hipaa-pci
  claim: AWS Managed Microsoft AD has the controls to help you meet HIPAA requirements and is in scope for PCI DSS.
  scope: AWS Managed Microsoft AD compliance.
  link: [HIPAA](../facts/directory-service.md#directory-service-managed-ad-hipaa-pci)
  link: [Payment Card Industry Data Security Standard (PCI DSS)](../facts/directory-service.md#directory-service-managed-ad-hipaa-pci)
directory-service-managed-ad-ldaps-ports
  claim: AWS Managed Microsoft AD supports LDAPS in both client and server roles; as a server it supports LDAPS over ports 636 (SSL) and 389 (TLS).
  scope: LDAPS with AWS Managed Microsoft AD; server-side LDAPS needs a certificate installed on the domain controllers.
  link: [in both client and server roles](../facts/directory-service.md#directory-service-managed-ad-ldaps-ports)
  link: [ports 636 (SSL) and 389 (TLS)](../facts/directory-service.md#directory-service-managed-ad-ldaps-ports)
directory-service-managed-ad-mfa-and-ldap
  claim: AWS Managed Microsoft AD can enable multi-factor authentication for users who access AWS applications from the internet, and because Active Directory is an LDAP directory it can serve Linux SSH authentication and other LDAP-enabled applications.
  scope: AWS Managed Microsoft AD.
  link: [an additional layer of security](../facts/directory-service.md#directory-service-managed-ad-mfa-and-ldap)
  link: [Linux Secure Shell (SSH) authentication](../facts/directory-service.md#directory-service-managed-ad-mfa-and-ldap)
  link: [Active Directory is an LDAP directory](../facts/directory-service.md#directory-service-managed-ad-mfa-and-ldap)
directory-service-managed-ad-mfa-needs-radius
  claim: MFA for AWS Managed Microsoft AD requires an MFA solution that is a RADIUS server, or an MFA plugin to a RADIUS server in your infrastructure; the directory's RADIUS client sends the username and OTP code to the RADIUS server before authenticating the user against Active Directory.
  scope: AWS Managed Microsoft AD MFA.
  link: [(RADIUS) server](../facts/directory-service.md#directory-service-managed-ad-mfa-needs-radius)
  link: [includes a RADIUS client](../facts/directory-service.md#directory-service-managed-ad-mfa-needs-radius)
directory-service-managed-ad-minimum-two-domain-controllers
  claim: For each AWS Managed Microsoft AD directory, AWS creates the minimum of two domain controllers automatically, in different Availability Zones of your VPC, to provide high availability; you can add more domain controllers.
  scope: per directory (per Region); minimum; adjustable; you can create additional domain controllers.
  link: [two domain controllers](../facts/directory-service.md#directory-service-managed-ad-minimum-two-domain-controllers)
  link: [across different Availability Zones](../facts/directory-service.md#directory-service-managed-ad-minimum-two-domain-controllers)
  say: two domain controllers | in different Availability Zones
directory-service-managed-ad-no-direct-dc-host-access
  claim: AWS Managed Microsoft AD does not allow direct host access to domain controllers through Remote Desktop, PowerShell Remoting, Telnet or SSH.
  scope: AWS Managed Microsoft AD domain controllers.
  link: [does not allow direct host access](../facts/directory-service.md#directory-service-managed-ad-no-direct-dc-host-access)
directory-service-managed-ad-no-domain-admin-for-customer
  claim: In AWS Managed Microsoft AD, AWS has exclusive control of the Domain Administrator and Enterprise Administrator privileged users and groups, so that AWS can perform operational management of the directory.
  scope: AWS Managed Microsoft AD.
  link: [exclusive control of the Domain Administrator](../facts/directory-service.md#directory-service-managed-ad-no-domain-admin-for-customer)
  link: [perform operational management of your directory](../facts/directory-service.md#directory-service-managed-ad-no-domain-admin-for-customer)
directory-service-managed-ad-no-manual-dc-promotion
  claim: You add domain controllers to AWS Managed Microsoft AD through the Directory Service console or API; promoting EC2 instances to domain controllers manually is not supported.
  scope: adding domain controllers to AWS Managed Microsoft AD.
  link: [AWS Directory Service console or API](../facts/directory-service.md#directory-service-managed-ad-no-manual-dc-promotion)
  link: [manually is not supported](../facts/directory-service.md#directory-service-managed-ad-no-manual-dc-promotion)
directory-service-managed-ad-no-migration-tools-standard-enterprise
  claim: For Standard and Enterprise Editions, AWS provides no tools to migrate an existing Active Directory into AWS Managed Microsoft AD; you plan the migration yourself, including password resets.
  scope: Standard and Enterprise Editions.
  link: [does not provide any migration tools](../facts/directory-service.md#directory-service-managed-ad-no-migration-tools-standard-enterprise)
directory-service-managed-ad-no-monitoring-agents-on-dcs
  claim: AWS does not allow monitoring agents to be installed on AWS Managed Microsoft AD domain controllers.
  scope: AWS Managed Microsoft AD domain controllers.
  link: [does not allow the installation of monitoring agents](../facts/directory-service.md#directory-service-managed-ad-no-monitoring-agents-on-dcs)
directory-service-managed-ad-office-365-sign-in
  claim: By adding Microsoft Entra Connect, and optionally AD FS, users can sign in to Microsoft Office 365 and other cloud applications with credentials stored in AWS Managed Microsoft AD.
  scope: AWS Managed Microsoft AD; Microsoft Entra Connect added.
  link: [By adding Microsoft Entra Connect](../facts/directory-service.md#directory-service-managed-ad-office-365-sign-in)
  link: [sign in to Microsoft Office 365](../facts/directory-service.md#directory-service-managed-ad-office-365-sign-in)
directory-service-managed-ad-office-365-via-ad-connect-adfs
  claim: Users in AWS Managed Microsoft AD can use Office 365: identities sync to Azure AD with Azure AD Connect, and AD FS with AWS Managed Microsoft AD authenticates the users.
  scope: Office 365 with AWS Managed Microsoft AD users.
  link: [Azure AD Connect](../facts/directory-service.md#directory-service-managed-ad-office-365-via-ad-connect-adfs)
  link: [Microsoft Active Directory Federation Services (AD FS)](../facts/directory-service.md#directory-service-managed-ad-office-365-via-ad-connect-adfs)
directory-service-managed-ad-resource-forest
  claim: AWS Managed Microsoft AD Standard and Enterprise can be a resource forest of mainly computers and groups, with trust relationships to your directory on premises or in the cloud.
  scope: Standard and Enterprise Editions.
  link: [as a resource forest](../facts/directory-service.md#directory-service-managed-ad-resource-forest)
  link: [with trust relationships](../facts/directory-service.md#directory-service-managed-ad-resource-forest)
directory-service-managed-ad-resource-forest-trust
  claim: AWS Managed Microsoft AD Standard and Enterprise Editions create new managed AD domains that act as resource forests with trust relationships to existing AD domains on premises, in AWS or in other clouds; user identities stay in the existing domains while the resource forest manages the AWS resources.
  scope: AWS Managed Microsoft AD Standard Edition and Enterprise Edition; trust relationship with the existing AD domains.
  link: [establish resource forests](../facts/directory-service.md#directory-service-managed-ad-resource-forest-trust)
  link: [User identities stay in your existing AD domains](../facts/directory-service.md#directory-service-managed-ad-resource-forest-trust)
directory-service-managed-ad-resources-by-edition
  claim: AWS provides the compute, storage and memory of an AWS Managed Microsoft AD directory; you state your needs by choosing an edition (Standard, Enterprise or Hybrid), and you add domain controllers when you need more resources.
  scope: per AWS Managed Microsoft AD directory.
  link: [AWS provides the compute, storage, and memory resources](../facts/directory-service.md#directory-service-managed-ad-resources-by-edition)
  link: [add additional domain controllers to your directory](../facts/directory-service.md#directory-service-managed-ad-resources-by-edition)
directory-service-managed-ad-schema-extend-not-modify
  claim: AWS Managed Microsoft AD Standard and Enterprise editions accept schema extensions submitted as an LDIF file; you may extend but not modify the core Active Directory schema.
  scope: Standard and Enterprise editions.
  link: [LDAP Data Interchange Format (LDIF) file](../facts/directory-service.md#directory-service-managed-ad-schema-extend-not-modify)
  link: [extend but not modify](../facts/directory-service.md#directory-service-managed-ad-schema-extend-not-modify)
directory-service-managed-ad-seamless-join-at-launch
  claim: An EC2 instance can be seamlessly joined to the AWS Managed Microsoft AD domain when it is launched, or launched and joined from the Directory Service console with AWS Systems Manager Automation.
  scope: AWS Managed Microsoft AD domain join.
  link: [seamlessly join an Amazon EC2 instance](../facts/directory-service.md#directory-service-managed-ad-seamless-join-at-launch)
  link: [AWS Systems Manager Automation](../facts/directory-service.md#directory-service-managed-ad-seamless-join-at-launch)
directory-service-managed-ad-security-group-local-vpc-only
  claim: AWS Managed Microsoft AD creates a security group for its domain controllers whose default inbound rules allow only the ports Active Directory needs, from the primary IPv4 CIDR block or the IPv6 CIDR block associated with the VPC; the ENIs do not have Elastic IPs and you cannot attach one, so by default only the local VPC can reach the directory until you change the rules.
  scope: per AWS Managed Microsoft AD directory; default; adjustable; security group rules can be changed to allow other sources.
  link: [the only inbound traffic that can communicate](../facts/directory-service.md#directory-service-managed-ad-security-group-local-vpc-only)
  link: [do not have Elastic IPs attached to them](../facts/directory-service.md#directory-service-managed-ad-security-group-local-vpc-only)
directory-service-managed-ad-snapshot-max-age-180-days
  claim: A manual snapshot of AWS Managed Microsoft AD can be at most 180 days old for a restore; this cannot be changed, because of the Active Directory tombstone lifetime.
  scope: per manual snapshot; maximum; not adjustable.
  link: [180 days](../facts/directory-service.md#directory-service-managed-ad-snapshot-max-age-180-days)
  say: one hundred eighty days
directory-service-managed-ad-standard-object-capacity
  claim: AWS Managed Microsoft AD Standard Edition includes 1 GB of directory object storage, which AWS estimates supports up to 5,000 users or 30,000 directory objects.
  scope: per Standard Edition directory; maximum; not adjustable; estimate; object sizes vary by company.
  link: [1 GB of directory object storage](../facts/directory-service.md#directory-service-managed-ad-standard-object-capacity)
  link: [up to 5,000 users](../facts/directory-service.md#directory-service-managed-ad-standard-object-capacity)
  link: [30,000 directory objects](../facts/directory-service.md#directory-service-managed-ad-standard-object-capacity)
directory-service-managed-ad-trust-access-via-identity-center
  claim: You can configure trust relationships between AWS Managed Microsoft AD and an existing self-managed Microsoft Active Directory, giving users and groups access to resources in either domain through IAM Identity Center.
  scope: AWS Managed Microsoft AD; trust with the self-managed AD.
  link: [access to resources in either domain](../facts/directory-service.md#directory-service-managed-ad-trust-access-via-identity-center)
  link: [configure trust relationships](../facts/directory-service.md#directory-service-managed-ad-trust-access-via-identity-center)
directory-service-managed-ad-trust-to-existing-ad
  claim: Applications that work with AWS Managed Microsoft AD can use user credentials stored in the directory, or the directory can connect with a trust to an existing Active Directory running on premises or on EC2 Windows and use its credentials.
  scope: AWS Managed Microsoft AD; a trust to the existing Active Directory.
  link: [with a trust and use credentials](../facts/directory-service.md#directory-service-managed-ad-trust-to-existing-ad)
  link: [running on-premises or on EC2 Windows](../facts/directory-service.md#directory-service-managed-ad-trust-to-existing-ad)
directory-service-managed-ad-two-azs-default
  claim: By default an AWS Managed Microsoft AD directory is deployed across two Availability Zones in a Region and connected to your VPC.
  scope: per AWS Managed Microsoft AD directory, per Region; default; adjustable; more domain controllers can be added.
  link: [two Availability Zones](../facts/directory-service.md#directory-service-managed-ad-two-azs-default)
  say: two Availability Zones
directory-service-managed-ad-when-to-use
  claim: AWS Managed Microsoft AD is the best choice when you need actual Active Directory features for AWS applications or Windows workloads (including RDS for SQL Server), a standalone Active Directory in the AWS Cloud that supports Office 365, or an LDAP directory for Linux applications.
  scope: AWS Directory Service directory types.
  link: [need actual Active Directory features](../facts/directory-service.md#directory-service-managed-ad-when-to-use)
  link: [a standalone Active Directory in the AWS Cloud](../facts/directory-service.md#directory-service-managed-ad-when-to-use)
  link: [an LDAP directory to support your Linux applications](../facts/directory-service.md#directory-service-managed-ad-when-to-use)
directory-service-multi-az-auto-replace-snapshots
  claim: Every AWS Directory Service directory is deployed across multiple Availability Zones, monitoring detects and replaces failed domain controllers, and data replication and automated daily snapshots are configured for you.
  scope: every directory.
  link: [deployed across multiple Availability Zones](../facts/directory-service.md#directory-service-multi-az-auto-replace-snapshots)
  link: [automated daily snapshots](../facts/directory-service.md#directory-service-multi-az-auto-replace-snapshots)
directory-service-multi-region-cannot-remove-primary
  claim: You cannot remove the primary Region of a replicated AWS Managed Microsoft AD directory unless you delete the directory.
  scope: AWS Managed Microsoft AD multi-Region replication; unless the directory is deleted.
  link: [You cannot remove the primary Region](../facts/directory-service.md#directory-service-multi-region-cannot-remove-primary)
directory-service-multi-region-failover-other-regions-stay-up
  claim: If all domain controllers in one Region are down, AWS Managed Microsoft AD recovers them and replicates the directory data automatically, while domain controllers in other Regions stay up and running; AWS services such as RDS for SQL Server and FSx connect to the local instance of the global directory.
  scope: AWS Managed Microsoft AD multi-Region replication.
  link: [other Regions stay up and running](../facts/directory-service.md#directory-service-multi-region-failover-other-regions-stay-up)
  link: [local instances of the global directory](../facts/directory-service.md#directory-service-multi-region-failover-other-regions-stay-up)
directory-service-multi-region-opt-in-primary-restriction
  claim: You can extend multi-Region replication of AWS Managed Microsoft AD to additional Regions only if the primary Region is an AWS default Region; with an opt-in primary Region you cannot add Regions.
  scope: per directory (primary Region).
  link: [only extend Multi-Region replication to additional Regions](../facts/directory-service.md#directory-service-multi-region-opt-in-primary-restriction)
  say: only from a default-Region primary
directory-service-multi-region-replicates-all-directory-data
  claim: Multi-Region replication of AWS Managed Microsoft AD uses native Active Directory replication to copy all customer directory data, including users, groups, group policies and schema, to additional Regions, where it creates two domain controllers in the selected VPC.
  scope: AWS Managed Microsoft AD Enterprise Edition multi-Region replication.
  link: [replicates all customer directory data](../facts/directory-service.md#directory-service-multi-region-replicates-all-directory-data)
  link: [uses native Active Directory replication](../facts/directory-service.md#directory-service-multi-region-replicates-all-directory-data)
  link: [creates two domain controllers in the selected VPC](../facts/directory-service.md#directory-service-multi-region-replicates-all-directory-data)
directory-service-multi-region-replication-enterprise-only
  claim: Multi-Region replication of AWS Managed Microsoft AD is available in Enterprise Edition only, for new and existing directories.
  scope: AWS Managed Microsoft AD multi-Region replication.
  link: [Enterprise Edition](../facts/directory-service.md#directory-service-multi-region-replication-enterprise-only)
  link: [for new and existing directories](../facts/directory-service.md#directory-service-multi-region-replication-enterprise-only)
directory-service-multi-region-same-directory-id
  claim: With multi-Region replication, the directory keeps the same directory ID in the new Region and is deployed in the same AWS account as the primary Region.
  scope: AWS Managed Microsoft AD multi-Region replication; multi-Region replication.
  link: [remains the same in the new region](../facts/directory-service.md#directory-service-multi-region-same-directory-id)
directory-service-multi-region-sharing-not-replicated
  claim: With multi-Region replication, directory sharing settings are not replicated from the primary Region automatically; you share the directory with other accounts per Region.
  scope: per Region; multi-Region replication.
  link: [not automatically replicated from the primary region](../facts/directory-service.md#directory-service-multi-region-sharing-not-replicated)
directory-service-multi-region-two-dcs-per-new-region
  claim: When you add a Region to an AWS Managed Microsoft AD directory, the service creates two domain controllers in the selected VPC in the new Region in the same AWS account, and the directory ID stays the same in all Regions.
  scope: per added Region; default; adjustable; you can add more domain controllers later.
  link: [creates two domain controllers](../facts/directory-service.md#directory-service-multi-region-two-dcs-per-new-region)
  say: two domain controllers
directory-service-price-example-enterprise-ohio
  claim: In the AWS pricing example for an Enterprise Edition directory in US East (Ohio), the hourly cost per managed directory is $0.40 per hour, and the bill shows it as two domain controllers at $0.20 per hour each.
  scope: per managed directory (two domain controllers), US East (Ohio); Enterprise Edition; prices vary by Region.
  link: [$0.40 per hour](../facts/directory-service.md#directory-service-price-example-enterprise-ohio)
  link: [$0.20 per hour](../facts/directory-service.md#directory-service-price-example-enterprise-ohio)
  say: forty cents per hour per directory | twenty cents per domain controller hour
directory-service-price-example-sharing-hour
  claim: In the AWS pricing example (Enterprise Edition, US East (Ohio)), directory sharing costs $0.06 per shared directory hour for each additional account.
  scope: per additional account, per hour, US East (Ohio); Enterprise Edition example.
  link: [$0.06 per shared directory hour](../facts/directory-service.md#directory-service-price-example-sharing-hour)
  say: six cents per shared directory hour
directory-service-pricing-billed-per-domain-controller
  claim: AWS Managed Microsoft AD is priced hourly per managed directory, and the bill lists each domain controller as a separate line item; additional domain controllers are billed on top of the managed directory rate.
  scope: AWS Managed Microsoft AD pricing.
  link: [each domain controller as an individual line item](../facts/directory-service.md#directory-service-pricing-billed-per-domain-controller)
  link: [plus any additional domain controllers](../facts/directory-service.md#directory-service-pricing-billed-per-domain-controller)
directory-service-pricing-multi-region-data-transfer
  claim: Multi-Region replication of AWS Managed Microsoft AD (Enterprise Edition) has a per-GB charge for data transferred out of your domain controllers to the other Regions where the directory is deployed.
  scope: per GB, per Region pair; Enterprise Edition multi-Region replication.
  link: [a charge per GB for the data transferred](../facts/directory-service.md#directory-service-pricing-multi-region-data-transfer)
  say: per GB of data transferred out
directory-service-pricing-sharing-per-account-hour
  claim: Sharing an AWS Managed Microsoft AD directory has an hourly charge for each additional account you share it with; there is no sharing charge for additional VPCs or for the account that owns the directory.
  scope: per additional account shared with.
  link: [an hourly sharing charge for each additional account](../facts/directory-service.md#directory-service-pricing-sharing-per-account-hour)
  link: [no sharing charge for additional VPCs](../facts/directory-service.md#directory-service-pricing-sharing-per-account-hour)
  say: hourly, per additional account | VPCs are free
directory-service-pricing-type-and-size-no-minimum
  claim: With AWS Directory Service you pay only for the type and size of the managed directory you use, with no up-front commitment and no minimum fee.
  scope: AWS Directory Service pricing.
  link: [pay only for the type and size](../facts/directory-service.md#directory-service-pricing-type-and-size-no-minimum)
  link: [no up-front commitment and no minimum fee](../facts/directory-service.md#directory-service-pricing-type-and-size-no-minimum)
directory-service-quota-ad-connector-directories
  claim: An account can have 10 AD Connector directories per Region by default, and the quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [10](../facts/directory-service.md#directory-service-quota-ad-connector-directories)
  say: ten
directory-service-quota-domain-controllers-per-directory
  claim: An AWS Managed Microsoft AD directory can have 20 domain controllers by default, and the quota is adjustable.
  scope: per directory; default; adjustable.
  link: [20](../facts/directory-service.md#directory-service-quota-domain-controllers-per-directory)
  say: twenty
directory-service-quota-managed-ad-directories
  claim: An account can have 20 AWS Managed Microsoft AD directories (Standard and Enterprise Editions) and 5 Hybrid Edition directories per Region by default. The Standard and Enterprise directory quota is adjustable.
  scope: per account, per Region; default; adjustable; adjustability stated for the Standard and Enterprise quota (Service Quotas); Hybrid not listed.
  link: [20](../facts/directory-service.md#directory-service-quota-managed-ad-directories)
  link: [5](../facts/directory-service.md#directory-service-quota-managed-ad-directories)
  say: twenty | five
directory-service-quota-managed-ad-manual-snapshots
  claim: A Standard or Enterprise Edition AWS Managed Microsoft AD directory can have 5 manual snapshots, and this quota cannot be changed.
  scope: per directory; maximum; not adjustable.
  link: [5 per AWS Managed Microsoft AD](../facts/directory-service.md#directory-service-quota-managed-ad-manual-snapshots)
  say: five per directory
directory-service-quota-regions-per-enterprise-directory
  claim: A single AWS Managed Microsoft AD (Enterprise Edition) directory can span at most 5 AWS Regions in total, counting the primary Region.
  scope: per directory (Enterprise Edition); maximum; not adjustable; multi-Region replication; the quota pages do not say whether it can be raised.
  link: [5](../facts/directory-service.md#directory-service-quota-regions-per-enterprise-directory)
  say: five Regions
directory-service-quota-shared-accounts-per-edition
  claim: The default shared-domain quota of AWS Managed Microsoft AD, which is the number of accounts that an individual directory can be shared to, is 25 for Standard Edition, 500 for Enterprise Edition and 125 for Hybrid Edition. Before the August 2025 increase the limits were 5 accounts (Standard) and 125 accounts (Enterprise).
  scope: per directory (accounts it can be shared to); default; default quota; the quota page does not say whether it can be raised.
  link: [25](../facts/directory-service.md#directory-service-quota-shared-accounts-per-edition)
  link: [500](../facts/directory-service.md#directory-service-quota-shared-accounts-per-edition)
  link: [125](../facts/directory-service.md#directory-service-quota-shared-accounts-per-edition)
  say: twenty-five accounts | five hundred accounts | one hundred twenty-five accounts
  changed: 2025-08-15: was The Standard Edition limit has increased from 5 to 25 accounts
directory-service-quota-simple-ad-directories
  claim: An account can have 10 Simple AD directories per Region by default (adjustable), and each Simple AD can have 5 manual snapshots.
  scope: per account, per Region; default; adjustable; Simple AD is no longer open to new customers.
  link: [10](../facts/directory-service.md#directory-service-quota-simple-ad-directories)
  link: [5 per Simple AD](../facts/directory-service.md#directory-service-quota-simple-ad-directories)
  say: ten | five snapshots
directory-service-rds-needs-managed-ad
  claim: Amazon RDS is compatible with AWS Managed Microsoft AD only and is not compatible with AD Connector.
  scope: Amazon RDS Active Directory integration.
  link: [compatible with AWS Managed Microsoft AD only](../facts/directory-service.md#directory-service-rds-needs-managed-ad)
  link: [is not compatible with AD Connector](../facts/directory-service.md#directory-service-rds-needs-managed-ad)
directory-service-seamless-join-not-for-existing-instances
  claim: Seamless domain join from the console works only at instance launch; existing EC2 Windows or Linux instances are joined with the EC2 API or PowerShell on the instance instead.
  scope: EC2 seamless domain join; existing instances.
  link: [You cannot use the seamless domain join feature](../facts/directory-service.md#directory-service-seamless-join-not-for-existing-instances)
  link: [using the EC2 API](../facts/directory-service.md#directory-service-seamless-join-not-for-existing-instances)
directory-service-sharing-across-accounts
  claim: A single AWS Managed Microsoft AD directory can be shared with other AWS accounts inside the same organization or outside it; the consumer account gets a shared directory whose metadata lets its EC2 instances seamlessly join the domain.
  scope: AWS Managed Microsoft AD directory sharing.
  link: [share a single directory](../facts/directory-service.md#directory-service-sharing-across-accounts)
  link: [outside your organization](../facts/directory-service.md#directory-service-sharing-across-accounts)
  link: [seamlessly join the domain](../facts/directory-service.md#directory-service-sharing-across-accounts)
directory-service-sharing-fee-charged-to-consumer
  claim: AWS charges an additional fee for directory sharing, and the account that uses the shared AWS Managed Microsoft AD pays the sharing fees.
  scope: AWS Managed Microsoft AD directory sharing.
  link: [an additional fee for directory sharing](../facts/directory-service.md#directory-service-sharing-fee-charged-to-consumer)
  link: [the account charged the sharing fees](../facts/directory-service.md#directory-service-sharing-fee-charged-to-consumer)
directory-service-sharing-methods-organizations-or-handshake
  claim: Directory sharing uses either the AWS Organizations method, which needs All features enabled and the directory in the management account and does not require consumer accounts to accept, or the handshake method, which requires the consumer account to accept the sharing request.
  scope: AWS Managed Microsoft AD directory sharing.
  link: [in the organization management account](../facts/directory-service.md#directory-service-sharing-methods-organizations-or-handshake)
  link: [doesn't require the directory consumer accounts to accept](../facts/directory-service.md#directory-service-sharing-methods-organizations-or-handshake)
  link: [The handshake method requires the directory consumer account](../facts/directory-service.md#directory-service-sharing-methods-organizations-or-handshake)
directory-service-sharing-needs-network-connectivity
  claim: Network connectivity between the VPCs, for example VPC peering, Transit Gateway or VPN, is a prerequisite for a directory sharing relationship across AWS accounts.
  scope: AWS Managed Microsoft AD directory sharing.
  link: [Network connectivity is a prerequisite](../facts/directory-service.md#directory-service-sharing-needs-network-connectivity)
directory-service-simple-ad-closed-to-new-customers
  claim: Simple AD is no longer open to new customers; for similar capabilities AWS points to AWS Managed Microsoft AD or AD Connector.
  scope: new customers.
  link: [no longer open to new customers](../facts/directory-service.md#directory-service-simple-ad-closed-to-new-customers)
  link: [explore AWS Managed Microsoft AD or AD Connector](../facts/directory-service.md#directory-service-simple-ad-closed-to-new-customers)
  say: closed to new customers | Managed Microsoft AD or AD Connector
directory-service-simple-ad-existing-customers-keep-it
  claim: Only new customer onboarding to Simple AD is not permitted: existing Simple AD customers retain full functionality, their directories and workloads are not affected, and they can continue to create new Simple AD directories.
  scope: existing Simple AD customers.
  link: [Existing Simple AD customers retain full functionality](../facts/directory-service.md#directory-service-simple-ad-existing-customers-keep-it)
  link: [continue to create new Simple AD directories](../facts/directory-service.md#directory-service-simple-ad-existing-customers-keep-it)
  say: existing customers keep full functionality | they can still create directories
directory-service-simple-ad-samba-4-basic-features
  claim: Simple AD is a Microsoft Active Directory-compatible directory powered by Samba 4 that supports basic features such as user accounts, group memberships, domain join of Linux and Windows EC2 instances, Kerberos-based SSO and group policies.
  scope: Simple AD.
  link: [powered by Samba 4](../facts/directory-service.md#directory-service-simple-ad-samba-4-basic-features)
  link: [Kerberos-based SSO, and group policies](../facts/directory-service.md#directory-service-simple-ad-samba-4-basic-features)
directory-service-simple-ad-subset-of-managed-ad
  claim: Simple AD is a standalone managed directory powered by a Samba 4 Active Directory Compatible Server that offers a subset of AWS Managed Microsoft AD features; it does not support MFA, trusts with other domains, PowerShell, the AD recycle bin, group managed service accounts or schema extensions for POSIX and Microsoft applications.
  scope: Simple AD.
  link: [a subset of the features](../facts/directory-service.md#directory-service-simple-ad-subset-of-managed-ad)
  link: [trust relationships with other domains](../facts/directory-service.md#directory-service-simple-ad-subset-of-managed-ad)
directory-service-simple-ad-two-sizes
  claim: Simple AD comes in two sizes: Small supports up to 500 users (about 2,000 objects) and Large supports up to 5,000 users (about 20,000 objects).
  scope: per Simple AD directory; maximum; not adjustable; object counts are approximate.
  link: [500 users](../facts/directory-service.md#directory-service-simple-ad-two-sizes)
  link: [5,000 users](../facts/directory-service.md#directory-service-simple-ad-two-sizes)
  link: [2,000 objects](../facts/directory-service.md#directory-service-simple-ad-two-sizes)
  link: [20,000 objects](../facts/directory-service.md#directory-service-simple-ad-two-sizes)
  say: five hundred users | five thousand users | about two thousand objects | about twenty thousand objects
directory-service-simple-ad-unsupported-features
  claim: Simple AD does not support MFA, trust relationships, DNS dynamic update, schema extensions, LDAPS, PowerShell AD cmdlets or FSMO role transfer, and it is not compatible with RDS SQL Server; customers who need an actual Microsoft Active Directory should use AWS Managed Microsoft AD.
  scope: Simple AD.
  link: [does not support multi-factor authentication (MFA), trust relationships](../facts/directory-service.md#directory-service-simple-ad-unsupported-features)
  link: [schema extensions, communication over LDAPS](../facts/directory-service.md#directory-service-simple-ad-unsupported-features)
  link: [not compatible with RDS SQL Server](../facts/directory-service.md#directory-service-simple-ad-unsupported-features)
directory-service-simple-ad-user-sizing
  claim: AWS advises adding no more than 500 users to a Small Simple AD directory and no more than 5,000 users to a Large Simple AD directory.
  scope: per Simple AD directory; maximum; not adjustable; guidance (generally).
  link: [500 users](../facts/directory-service.md#directory-service-simple-ad-user-sizing)
  link: [5,000 users](../facts/directory-service.md#directory-service-simple-ad-user-sizing)
  say: five hundred users | five thousand users
directory-service-simple-ad-when-to-use
  claim: Simple AD can be used as a standalone directory in the cloud for Windows workloads that need basic Active Directory features, for compatible AWS applications, or for Linux workloads that need an LDAP service.
  scope: AWS Directory Service directory types.
  link: [a standalone directory in the cloud](../facts/directory-service.md#directory-service-simple-ad-when-to-use)
  link: [need basic Active Directory features](../facts/directory-service.md#directory-service-simple-ad-when-to-use)
directory-service-trust-needs-network-connection-to-vpc
  claim: Before creating a trust with a self-managed directory, the self-managed network must be connected to the VPC that contains AWS Managed Microsoft AD, with the required Active Directory ports open on both firewalls, and DNS conditional forwarders must be set up on the self-managed domain.
  scope: trusts between AWS Managed Microsoft AD and a self-managed AD.
  link: [connect your self-managed network to the Amazon VPC](../facts/directory-service.md#directory-service-trust-needs-network-connection-to-vpc)
  link: [set up DNS conditional forwarders](../facts/directory-service.md#directory-service-trust-needs-network-connection-to-vpc)
directory-service-trust-types-and-directions
  claim: AWS Managed Microsoft AD supports one-way and two-way external and forest trusts with self-managed (on-premises) directories and with other AWS Managed Microsoft AD directories, in all three directions: incoming, outgoing and two-way.
  scope: AWS Managed Microsoft AD trusts.
  link: [one and two-way external and forest trust relationships](../facts/directory-service.md#directory-service-trust-types-and-directions)
  link: [Incoming, Outgoing and Two-way (Bi-directional)](../facts/directory-service.md#directory-service-trust-types-and-directions)
directory-service-two-way-trust-for-aws-apps-one-way-for-ec2-rds-fsx
  claim: A two-way trust is required for AWS enterprise apps such as IAM Identity Center, WorkSpaces, Amazon Quick, WorkMail and the AWS Management Console, because AWS Managed Microsoft AD must query users and groups in the self-managed AD; Amazon EC2, Amazon RDS and Amazon FSx work with either a one-way or a two-way trust.
  scope: trusts between AWS Managed Microsoft AD and a self-managed AD.
  link: [two-way trust is required](../facts/directory-service.md#directory-service-two-way-trust-for-aws-apps-one-way-for-ec2-rds-fsx)
  link: [either a one-way or two-way trust](../facts/directory-service.md#directory-service-two-way-trust-for-aws-apps-one-way-for-ec2-rds-fsx)
directory-service-what-it-is
  claim: AWS Directory Service provides multiple ways to use Microsoft Active Directory with other AWS services, with directory choices for existing Microsoft AD or LDAP-aware applications in the cloud.
  scope: AWS Directory Service.
  link: [multiple ways to use Microsoft Active Directory (AD)](../facts/directory-service.md#directory-service-what-it-is)
  link: [multiple directory choices for customers](../facts/directory-service.md#directory-service-what-it-is)
directory-service-which-to-choose-row
  claim: The Directory Service 'Which to choose' table says: use AWS Managed Microsoft AD (Standard or Enterprise Edition) for an actual Microsoft AD in the cloud or LDAP for Linux apps; Hybrid Edition to extend an existing self-managed AD into AWS; AD Connector if you only need on-premises users to log in to AWS applications with their AD credentials (it can also join EC2 instances to the existing domain); Simple AD for a low-scale, low-cost directory with basic AD compatibility. Simple AD is no longer open to new customers; for similar capabilities AWS points to AWS Managed Microsoft AD or AD Connector.
  scope: AWS Directory Service directory types.
  link: [only need to allow your on-premises users](../facts/directory-service.md#directory-service-which-to-choose-row)
  link: [low-scale, low-cost directory with basic Active Directory compatibility](../facts/directory-service.md#directory-service-which-to-choose-row)
  link: [extend your existing self-managed AD](../facts/directory-service.md#directory-service-which-to-choose-row)
directory-service-which-to-choose-saas-cognito-row
  claim: The Directory Service 'Which to choose' table says: if you develop high-scale SaaS applications and need a scalable directory to manage and authenticate your subscribers that works with social media identities, use Amazon Cognito.
  scope: AWS Directory Service directory types.
  link: [develop high-scale SaaS applications](../facts/directory-service.md#directory-service-which-to-choose-saas-cognito-row)
  link: [works with social media identities](../facts/directory-service.md#directory-service-which-to-choose-saas-cognito-row)
iam-identity-center-abac-attributes-as-session-tags
  claim: For attribute-based access control, IAM Identity Center passes selected user attributes from the identity source to the accessed account as session tags, which policies reference with the aws:PrincipalTag condition key.
  scope: attributes for access control in IAM Identity Center.
  link: [sent as session tags](../facts/iam-identity-center.md#iam-identity-center-abac-attributes-as-session-tags)
  link: [existing attributes in the users' identity source](../facts/iam-identity-center.md#iam-identity-center-abac-attributes-as-session-tags)
iam-identity-center-abac-fewer-permission-sets
  claim: With ABAC in IAM Identity Center, user attributes from any identity source act as tags, so users who share one permission set get access only to resources with matching tags, and a change of the attribute in the corporate directory changes access without permission updates in AWS.
  scope: ABAC with IAM Identity Center.
  link: [these attributes are called tags](../facts/iam-identity-center.md#iam-identity-center-abac-fewer-permission-sets)
  link: [only to the AWS resources with matching tags](../facts/iam-identity-center.md#iam-identity-center-abac-fewer-permission-sets)
  link: [without requiring any permissions updates in AWS](../facts/iam-identity-center.md#iam-identity-center-abac-fewer-permission-sets)
iam-identity-center-abac-saml-attributes-directory-precedence
  claim: An external IdP can send attributes as session tags through SAML assertions; if an ABAC mapping for the same attribute is also configured on the Attributes for access control page, the Identity Center directory value takes precedence and replaces the IdP value.
  scope: external IdP as identity source with ABAC.
  link: [send attributes as session tags through SAML assertions](../facts/iam-identity-center.md#iam-identity-center-abac-saml-attributes-directory-precedence)
  link: [Identity Center directory takes precedence](../facts/iam-identity-center.md#iam-identity-center-abac-saml-attributes-directory-precedence)
iam-identity-center-account-instance-bound-to-one-account
  claim: An account instance of IAM Identity Center is bound to a single AWS account and is visible only within that account and the Region where it is enabled; AWS says to use account instances only for isolated deployments of select AWS managed applications.
  scope: account instance of IAM Identity Center.
  link: [bound to a single AWS account](../facts/iam-identity-center.md#iam-identity-center-account-instance-bound-to-one-account)
  link: [visible only within the AWS account](../facts/iam-identity-center.md#iam-identity-center-account-instance-bound-to-one-account)
  link: [isolated deployments of select AWS managed applications](../facts/iam-identity-center.md#iam-identity-center-account-instance-bound-to-one-account)
iam-identity-center-account-instance-creation-nov-2023
  claim: When an organization has an organization instance of IAM Identity Center, a member account can create an account instance only if the instance administrator permits creation of account instances (organization instances created after November 15, 2023) or manually enabled it (organization instances created before November 15, 2023). In addition, no service control policy may prevent it, the account must not already have an IAM Identity Center instance in any AWS Region, and IAM Identity Center must be available in the Region.
  scope: AWS Organizations member accounts; an organization instance exists in the organization.
  link: [November 15, 2023](../facts/iam-identity-center.md#iam-identity-center-account-instance-creation-nov-2023)
  say: November fifteenth, twenty twenty-three
iam-identity-center-account-instance-one-per-account
  claim: You are limited to one account instance of IAM Identity Center per AWS account, and it manages access only for supported applications in the same account and Region.
  scope: per AWS account; maximum; not adjustable.
  link: [one account instance per AWS account](../facts/iam-identity-center.md#iam-identity-center-account-instance-one-per-account)
  say: one per account
iam-identity-center-account-instances-not-for-resiliency
  claim: AWS does not recommend account instances of IAM Identity Center as a resiliency measure, because they do not support AWS account access and create a second, isolated control point not connected to the organization instance.
  scope: account instances of IAM Identity Center.
  link: [they do not support AWS account access](../facts/iam-identity-center.md#iam-identity-center-account-instances-not-for-resiliency)
  link: [a second, isolated control point](../facts/iam-identity-center.md#iam-identity-center-account-instances-not-for-resiliency)
iam-identity-center-accounts-global-any-region
  claim: Although IAM Identity Center determines access from the Region where it is enabled, AWS accounts are global: after signing in, users can operate in any Region of the AWS accounts they access through IAM Identity Center.
  scope: AWS account access through IAM Identity Center.
  link: [AWS accounts are global](../facts/iam-identity-center.md#iam-identity-center-accounts-global-any-region)
  link: [they can operate in any Region](../facts/iam-identity-center.md#iam-identity-center-accounts-global-any-region)
iam-identity-center-accounts-need-organizations-all-features
  claim: Any AWS account managed with AWS Organizations can be added to IAM Identity Center, and the organization needs all features enabled for account single sign-on.
  scope: AWS accounts managed with AWS Organizations (account single sign-on).
  link: [any AWS account managed using AWS Organizations](../facts/iam-identity-center.md#iam-identity-center-accounts-need-organizations-all-features)
  link: [enable all features in your organizations](../facts/iam-identity-center.md#iam-identity-center-accounts-need-organizations-all-features)
iam-identity-center-ad-connector-single-domain-no-portal-reset
  claim: With AD Connector as the IAM Identity Center identity source, IAM Identity Center has access only to the users and groups of the single domain AD Connector attaches to, and password resets must be done in AD, not in the AWS access portal.
  scope: AD Connector as the IAM Identity Center identity source.
  link: [the single domain to which AD Connector attaches](../facts/iam-identity-center.md#iam-identity-center-ad-connector-single-domain-no-portal-reset)
  link: [must be done from within AD](../facts/iam-identity-center.md#iam-identity-center-ad-connector-single-domain-no-portal-reset)
  link: [not be able to reset their passwords](../facts/iam-identity-center.md#iam-identity-center-ad-connector-single-domain-no-portal-reset)
iam-identity-center-ad-directory-in-management-or-delegated-account
  claim: To use Active Directory as the identity source, an AD Connector or AWS Managed Microsoft AD directory in AWS Directory Service must reside in the AWS Organizations management account, or in the IAM Identity Center delegated administrator account when delegated admin is used.
  scope: Active Directory as the IAM Identity Center identity source.
  link: [must reside within your AWS Organizations management account](../facts/iam-identity-center.md#iam-identity-center-ad-directory-in-management-or-delegated-account)
  link: [residing in the delegated admin account](../facts/iam-identity-center.md#iam-identity-center-ad-directory-in-management-or-delegated-account)
iam-identity-center-ad-pass-through-no-passwords-synced
  claim: With Active Directory as the identity source, IAM Identity Center uses the Directory Service connection for pass-through authentication to the source AD; it synchronizes users, groups and memberships, but no password information, because authentication happens in the source directory.
  scope: Active Directory as the IAM Identity Center identity source.
  link: [pass-through authentication to the source AD instance](../facts/iam-identity-center.md#iam-identity-center-ad-pass-through-no-passwords-synced)
  link: [No password information is synchronized](../facts/iam-identity-center.md#iam-identity-center-ad-pass-through-no-passwords-synced)
iam-identity-center-ad-via-trust-to-self-managed
  claim: IAM Identity Center can connect a self-managed Active Directory or an AWS Managed Microsoft AD directory through AWS Directory Service; with AWS Managed Microsoft AD as the source it can work with users from any domain connected through an AD trust.
  scope: Active Directory as the IAM Identity Center identity source.
  link: [connect a self-managed directory in Active Directory](../facts/iam-identity-center.md#iam-identity-center-ad-via-trust-to-self-managed)
  link: [any domain connected through an AD trust](../facts/iam-identity-center.md#iam-identity-center-ad-via-trust-to-self-managed)
iam-identity-center-admin-can-end-user-session
  claim: An IAM Identity Center administrator can end a user's session; this works as if the user signed out, so administrators can require the user to sign in again.
  scope: IAM Identity Center user sessions.
  link: [as if users signed out themselves](../facts/iam-identity-center.md#iam-identity-center-admin-can-end-user-session)
  link: [require users to sign in again](../facts/iam-identity-center.md#iam-identity-center-admin-can-end-user-session)
iam-identity-center-admin-only-from-primary-region
  claim: IAM Identity Center supports most administrative functions only from the primary Region, including the external IdP connection, user and group synchronization, and creating and assigning permission sets; applications are managed in the Region where they were created.
  scope: per IAM Identity Center instance.
  link: [most administrative functions only from the primary Region](../facts/iam-identity-center.md#iam-identity-center-admin-only-from-primary-region)
  link: [Region where the application was created](../facts/iam-identity-center.md#iam-identity-center-admin-only-from-primary-region)
iam-identity-center-app-assignments-required-by-default
  claim: By default, assignments are required for AWS managed applications, so only users assigned to the application directly or through a group see its tile in the AWS access portal; an application administrator can choose not to require assignments.
  scope: per AWS managed application; default; adjustable; the application administrator can choose whether to require assignments.
  link: [assignments are required for AWS managed applications](../facts/iam-identity-center.md#iam-identity-center-app-assignments-required-by-default)
  link: [can view the application tile](../facts/iam-identity-center.md#iam-identity-center-app-assignments-required-by-default)
iam-identity-center-application-session-1-hour-refresh
  claim: Application sessions with AWS managed applications have a one hour lifetime by default and are refreshed automatically while the user interactive session is valid; after the user interactive session ends, they end at their next refresh, typically within 30 minutes.
  scope: per application session; default; not adjustable; AWS managed applications.
  link: [one hour lifetime](../facts/iam-identity-center.md#iam-identity-center-application-session-1-hour-refresh)
  link: [typically within 30 minutes](../facts/iam-identity-center.md#iam-identity-center-application-session-1-hour-refresh)
  say: one hour | within about thirty minutes
iam-identity-center-apps-sso-browser-only
  claim: IAM Identity Center gives single sign-on to business applications through web browsers only; the FAQ answers no for native mobile and desktop applications.
  scope: single sign-on to business applications.
  link: [through web browsers only](../facts/iam-identity-center.md#iam-identity-center-apps-sso-browser-only)
iam-identity-center-availability-design-goals
  claim: In a single Region, IAM Identity Center is designed for 99.95% availability of the data plane (including sign-in) and 99.90% of the control plane; these are design goals, not a Service Level Agreement.
  scope: per Region; design goal, not an SLA.
  link: [99.95%](../facts/iam-identity-center.md#iam-identity-center-availability-design-goals)
  link: [99.90%](../facts/iam-identity-center.md#iam-identity-center-availability-design-goals)
  say: ninety-nine point nine five percent | ninety-nine point nine percent
iam-identity-center-break-glass-recommended
  claim: Even when IAM Identity Center is replicated to additional Regions, AWS recommends break-glass access for a small group of privileged users; the emergency access option uses external IdP identities instead of IAM users and does not protect against a disruption in the external IdP.
  scope: access during an IAM Identity Center or IdP disruption.
  link: [a small group of privileged users](../facts/iam-identity-center.md#iam-identity-center-break-glass-recommended)
  link: [does not protect against a disruption](../facts/iam-identity-center.md#iam-identity-center-break-glass-recommended)
  link: [Even if your IAM Identity Center is replicated](../facts/iam-identity-center.md#iam-identity-center-break-glass-recommended)
iam-identity-center-change-ad-sync-deprecated-2025-04
  claim: Since 2025-04-17 you can no longer provision Active Directory users with IAM Identity Center AD Sync; you use IAM Identity Center configurable AD sync instead.
  scope: Active Directory identity source.
  link: [April 17, 2025](../facts/iam-identity-center.md#iam-identity-center-change-ad-sync-deprecated-2025-04)
  link: [IAM Identity Center configurable AD Sync](../facts/iam-identity-center.md#iam-identity-center-change-ad-sync-deprecated-2025-04)
  say: April seventeenth, twenty twenty-five | configurable AD sync
  changed: 2025-04-17: was IAM Identity Center AD Sync
iam-identity-center-change-customer-managed-kms-keys-2025-09
  claim: On 2025-09-17 IAM Identity Center added support for customer managed KMS keys to encrypt workforce identity data at rest.
  scope: per IAM Identity Center instance.
  link: [September 17, 2025](../facts/iam-identity-center.md#iam-identity-center-change-customer-managed-kms-keys-2025-09)
  link: [customer managed KMS keys](../facts/iam-identity-center.md#iam-identity-center-change-customer-managed-kms-keys-2025-09)
  say: September seventeenth, twenty twenty-five | customer managed KMS keys
iam-identity-center-change-customer-managed-policies-2022-07
  claim: On 2022-07-14 permission sets gained support for customer managed IAM policies and permissions boundaries, in addition to AWS managed policies.
  scope: per permission set.
  link: [July 14, 2022](../facts/iam-identity-center.md#iam-identity-center-change-customer-managed-policies-2022-07)
  say: July fourteenth, twenty twenty-two
iam-identity-center-change-group-membership-immediate-2026-05
  claim: Since 2026-05-28 the guide states that permission and application access changes from group membership changes take effect immediately when new sessions are created.
  scope: per user session; new sessions.
  link: [May 28, 2026](../facts/iam-identity-center.md#iam-identity-center-change-group-membership-immediate-2026-05)
  link: [take effect immediately when creating new sessions](../facts/iam-identity-center.md#iam-identity-center-change-group-membership-immediate-2026-05)
  say: May twenty-eighth, twenty twenty-six | immediately, for new sessions
iam-identity-center-change-multi-account-permissions-optional-2026-08
  claim: Since 2026-08-04 you can choose whether to enable multi-account permissions when you create an organization instance; they are enabled by default and can be enabled later.
  scope: new organization instances; default.
  link: [August 4, 2026](../facts/iam-identity-center.md#iam-identity-center-change-multi-account-permissions-optional-2026-08)
  link: [By default, multi-account permissions are enabled](../facts/iam-identity-center.md#iam-identity-center-change-multi-account-permissions-optional-2026-08)
  say: August fourth, twenty twenty-six | on by default
iam-identity-center-change-multi-region-2026-02
  claim: On 2026-02-02 IAM Identity Center added multi-Region support: replication to additional Regions, AWS account access and use of AWS managed applications in additional Regions.
  scope: per IAM Identity Center instance.
  link: [February 2, 2026](../facts/iam-identity-center.md#iam-identity-center-change-multi-region-2026-02)
  link: [replication to additional Regions](../facts/iam-identity-center.md#iam-identity-center-change-multi-region-2026-02)
  say: February second, twenty twenty-six | replication to additional Regions
iam-identity-center-change-multi-region-identity-center-directory-2026-07
  claim: On 2026-07-28 multi-Region support was extended to instances that use the Identity Center directory as the identity source, in addition to external identity providers.
  scope: per IAM Identity Center instance; Identity Center directory as identity source.
  link: [July 28, 2026](../facts/iam-identity-center.md#iam-identity-center-change-multi-region-identity-center-directory-2026-07)
  say: July twenty-eighth, twenty twenty-six
iam-identity-center-change-one-click-multi-region-2026-08
  claim: Since 2026-08-06 a new organization instance can be created with a Multi-Region option that automatically creates a customer managed KMS key and replicates the instance to an additional Region.
  scope: new organization instances; supported Regions.
  link: [August 6, 2026](../facts/iam-identity-center.md#iam-identity-center-change-one-click-multi-region-2026-08)
  link: [automatically creating a customer managed KMS key](../facts/iam-identity-center.md#iam-identity-center-change-one-click-multi-region-2026-08)
  say: August sixth, twenty twenty-six | it creates a customer managed KMS key for you
iam-identity-center-change-renamed-from-aws-sso-2022-07
  claim: On 2022-07-26 AWS Single Sign-On (AWS SSO) was renamed AWS IAM Identity Center; its features include application assignments, multi-account permissions and an AWS access portal.
  scope: service name.
  link: [July 26, 2022](../facts/iam-identity-center.md#iam-identity-center-change-renamed-from-aws-sso-2022-07)
  link: [AWS Single Sign-On (AWS SSO)](../facts/iam-identity-center.md#iam-identity-center-change-renamed-from-aws-sso-2022-07)
  say: July twenty-sixth, twenty twenty-two | AWS Single Sign-On
iam-identity-center-change-separate-account-application-quotas-2026-06
  claim: On 2026-06-22 IAM Identity Center began to enforce separate quotas for AWS accounts and for applications, with a new default of 7,000 for each; before, they shared a single combined quota.
  scope: per IAM Identity Center instance; default.
  link: [June 22, 2026](../facts/iam-identity-center.md#iam-identity-center-change-separate-account-application-quotas-2026-06)
  link: [7,000](../facts/iam-identity-center.md#iam-identity-center-change-separate-account-application-quotas-2026-06)
  say: June twenty-second, twenty twenty-six | seven thousand each
  changed: 2026-06-22: was a single combined quota
iam-identity-center-change-source-may-remove-assignments
  claim: Changing the identity source of IAM Identity Center might remove all user and group assignments; if that happens, all users, including the administrative user, lose single sign-on access to their AWS accounts and applications.
  scope: changing the identity source; users and groups already managed in one identity source.
  link: [might remove all user and group assignments](../facts/iam-identity-center.md#iam-identity-center-change-source-may-remove-assignments)
  link: [will lose single sign-on access](../facts/iam-identity-center.md#iam-identity-center-change-source-may-remove-assignments)
iam-identity-center-change-to-ad-changes-portal-url
  claim: Changing the identity source type to or from Active Directory changes the Identity Store ID, and the default AWS access portal URL changes with it.
  scope: changing the identity source type to or from Active Directory.
  link: [the Identity Store ID will change](../facts/iam-identity-center.md#iam-identity-center-change-to-ad-changes-portal-url)
  link: [Your default AWS access portal URL will change](../facts/iam-identity-center.md#iam-identity-center-change-to-ad-changes-portal-url)
iam-identity-center-cli-recommended-at-scale
  claim: AWS recommends the AWS CLI and APIs to administer IAM Identity Center centrally when you have more than 50,000 users, 10,000 groups, 500 permission sets or 3,000 applications.
  scope: per IAM Identity Center instance; recommendation, not a quota.
  link: [50,000 users](../facts/iam-identity-center.md#iam-identity-center-cli-recommended-at-scale)
  link: [10,000 groups](../facts/iam-identity-center.md#iam-identity-center-cli-recommended-at-scale)
  link: [500 permission sets](../facts/iam-identity-center.md#iam-identity-center-cli-recommended-at-scale)
  link: [3,000 applications](../facts/iam-identity-center.md#iam-identity-center-cli-recommended-at-scale)
  say: fifty thousand users | ten thousand groups | five hundred permission sets | three thousand applications
iam-identity-center-cli-v2-sign-in-short-term-credentials
  claim: With AWS CLI version 2 integration, developers sign in to the AWS CLI with the same IAM Identity Center or Active Directory credentials they use for IAM Identity Center, can list and switch between assigned accounts and roles, and the CLI manages short-term credentials automatically.
  scope: AWS CLI version 2 with IAM Identity Center.
  link: [IAM Identity Center credentials](../facts/iam-identity-center.md#iam-identity-center-cli-v2-sign-in-short-term-credentials)
  link: [list and switch between accounts and roles](../facts/iam-identity-center.md#iam-identity-center-cli-v2-sign-in-short-term-credentials)
  link: [The CLI manages short-term credentials automatically](../facts/iam-identity-center.md#iam-identity-center-cli-v2-sign-in-short-term-credentials)
iam-identity-center-coexists-with-iam-federation
  claim: IAM Identity Center can be used for access to AWS managed applications only, AWS accounts only, or both, and an existing IAM federation for AWS account access can continue while IAM Identity Center serves application access.
  scope: adopting IAM Identity Center.
  link: [applications only, AWS accounts only, or both](../facts/iam-identity-center.md#iam-identity-center-coexists-with-iam-federation)
  link: [you can continue to do so](../facts/iam-identity-center.md#iam-identity-center-coexists-with-iam-federation)
iam-identity-center-cognito-is-not-an-identity-source
  claim: Amazon Cognito manages identities for customer-facing applications and is not a supported identity source for IAM Identity Center; workforce identities come from the Identity Center store or an external source such as Active Directory, Okta or Microsoft Entra ID.
  scope: IAM Identity Center identity sources.
  link: [not a supported identity source](../facts/iam-identity-center.md#iam-identity-center-cognito-is-not-an-identity-source)
  link: [manage identities for your customer facing applications](../facts/iam-identity-center.md#iam-identity-center-cognito-is-not-an-identity-source)
iam-identity-center-configurable-ad-sync-scope
  claim: IAM Identity Center configurable AD sync lets you explicitly choose which Active Directory users and groups are synchronized into IAM Identity Center and control the synchronization, for example by pausing and resuming it.
  scope: per Active Directory identity source.
  link: [explicitly configure the identities in Microsoft Active Directory](../facts/iam-identity-center.md#iam-identity-center-configurable-ad-sync-scope)
  say: you choose which AD users and groups sync
iam-identity-center-configures-account-permissions-automatically
  claim: Users of the connected directory can be given permissions to the management account or member accounts based on common job functions or custom permissions, and IAM Identity Center configures all the necessary user permissions in the AWS accounts automatically.
  scope: single sign-on access to AWS accounts.
  link: [configures all the necessary user permissions](../facts/iam-identity-center.md#iam-identity-center-configures-account-permissions-automatically)
  link: [use custom permissions](../facts/iam-identity-center.md#iam-identity-center-configures-account-permissions-automatically)
iam-identity-center-console-and-cli-v2-sso
  claim: IAM Identity Center controls access to the AWS Management Console and AWS CLI v2 with single sign-on, and the AWS Console Mobile App also supports it.
  scope: single sign-on to the AWS Management Console and AWS CLI v2.
  link: [AWS Management Console and CLI v2](../facts/iam-identity-center.md#iam-identity-center-console-and-cli-v2-sso)
iam-identity-center-creates-roles-per-permission-set-not-iam-users
  claim: IAM Identity Center does not create IAM users or groups; it keeps its own identity store and creates and manages an IAM role in each assigned account for every permission set.
  scope: AWS accounts with permission set assignments.
  link: [does not create IAM users and groups](../facts/iam-identity-center.md#iam-identity-center-creates-roles-per-permission-set-not-iam-users)
  link: [creates and manages IAM roles](../facts/iam-identity-center.md#iam-identity-center-creates-roles-per-permission-set-not-iam-users)
iam-identity-center-custom-saml-applications
  claim: A business application that is not in the pre-integrated list can still use IAM Identity Center if it supports SAML 2.0, configured as a custom SAML 2.0 application.
  scope: business applications that are not pre-integrated; the application supports SAML 2.0.
  link: [a custom SAML 2.0 application](../facts/iam-identity-center.md#iam-identity-center-custom-saml-applications)
iam-identity-center-customer-managed-policy-must-preexist
  claim: When a permission set uses customer managed policies or a permissions boundary, IAM Identity Center does not create those policies; they must be created in advance in each target account with a matching name and path, and the assignment fails if the policy does not exist in the member account.
  scope: permission sets with customer managed policies or permissions boundaries.
  link: [doesn't create a policy in any AWS accounts](../facts/iam-identity-center.md#iam-identity-center-customer-managed-policy-must-preexist)
  link: [create those policies in advance in each account](../facts/iam-identity-center.md#iam-identity-center-customer-managed-policy-must-preexist)
  link: [fails to assign the permission set](../facts/iam-identity-center.md#iam-identity-center-customer-managed-policy-must-preexist)
iam-identity-center-data-stored-in-enabled-region
  claim: All data configured in IAM Identity Center, including directory configurations, permission sets, application instances and user assignments, is stored in the Region where IAM Identity Center was enabled.
  scope: per IAM Identity Center instance.
  link: [stored in the Region where you enabled it](../facts/iam-identity-center.md#iam-identity-center-data-stored-in-enabled-region)
  link: [directory configurations, permission sets, application instances](../facts/iam-identity-center.md#iam-identity-center-data-stored-in-enabled-region)
iam-identity-center-decision-guide-federation-with-iam
  claim: As an alternative to IAM Identity Center, the decision guide says IAM can federate workforce users through an identity provider to specific AWS accounts, using an IdP that speaks OpenID Connect (OIDC) or SAML 2.0; users then assume IAM roles in the account.
  scope: workforce federation directly with IAM.
  link: [to specific AWS accounts](../facts/iam-identity-center.md#iam-identity-center-decision-guide-federation-with-iam)
  link: [either OpenID Connect (OIDC) or SAML 2.0](../facts/iam-identity-center.md#iam-identity-center-decision-guide-federation-with-iam)
  link: [Users assume IAM roles](../facts/iam-identity-center.md#iam-identity-center-decision-guide-federation-with-iam)
iam-identity-center-decision-guide-workforce-account-access-row
  claim: In the identity decision guide table, to configure workforce access to AWS accounts and the resources in them, the recommended services are IAM Identity Center or federation with IAM, with AWS Control Tower, centralized root access and temporary security credentials as additional capabilities.
  scope: AWS identity decision guide.
  link: [Configure workforce access to AWS accounts](../facts/iam-identity-center.md#iam-identity-center-decision-guide-workforce-account-access-row)
  link: [Federation with IAM](../facts/iam-identity-center.md#iam-identity-center-decision-guide-workforce-account-access-row)
iam-identity-center-default-identity-source-directory
  claim: When IAM Identity Center is enabled for the first time, it is automatically configured with the Identity Center directory as the default identity source unless a different identity source is chosen.
  scope: per IAM Identity Center instance; default; adjustable; unless a different identity source is chosen.
  link: [Identity Center directory as your default identity source](../facts/iam-identity-center.md#iam-identity-center-default-identity-source-directory)
iam-identity-center-delegated-admin-cannot-alter-management-permission-sets
  claim: A permission set used for access to the management account can only be modified by an IAM Identity Center administrator in the management account; the delegated administrator cannot alter permission sets provisioned in the management account.
  scope: permission sets for the AWS Organizations management account.
  link: [can't alter permission sets provisioned](../facts/iam-identity-center.md#iam-identity-center-delegated-admin-cannot-alter-management-permission-sets)
  link: [can only be modified by](../facts/iam-identity-center.md#iam-identity-center-delegated-admin-cannot-alter-management-permission-sets)
iam-identity-center-delegated-admin-member-account
  claim: The IAM Identity Center organization instance always resides in the management account, but administration can be delegated to a member account in AWS Organizations, which reduces the number of people who need access to the management account.
  scope: organization instance of IAM Identity Center.
  link: [must always reside in the management account](../facts/iam-identity-center.md#iam-identity-center-delegated-admin-member-account)
  link: [to a member account in AWS Organizations](../facts/iam-identity-center.md#iam-identity-center-delegated-admin-member-account)
  link: [Minimizes the number of people who require access](../facts/iam-identity-center.md#iam-identity-center-delegated-admin-member-account)
iam-identity-center-delegated-admin-not-management-account
  claim: IAM Identity Center runs in the Org Management account by default, but to apply least privilege its administration can be delegated to a member account; in the AWS SRA the Shared Services account is its delegated administrator.
  scope: IAM Identity Center administration in AWS Organizations.
  link: [runs in the Org Management account by default](../facts/iam-identity-center.md#iam-identity-center-delegated-admin-not-management-account)
  link: [the Shared Services account is the delegated administrator](../facts/iam-identity-center.md#iam-identity-center-delegated-admin-not-management-account)
iam-identity-center-deleted-user-sessions-continue
  claim: If users are deleted or disabled in IAM Identity Center through Identity Store APIs, users with active sessions can continue to access integrated applications and accounts.
  scope: users deleted or disabled using Identity Store APIs; the user has an active session.
  link: [users with active sessions can continue to access](../facts/iam-identity-center.md#iam-identity-center-deleted-user-sessions-continue)
  link: [integrated applications and accounts](../facts/iam-identity-center.md#iam-identity-center-deleted-user-sessions-continue)
iam-identity-center-disabled-user-keeps-assuming-roles
  claim: If a user has an active AWS access portal session and is disabled, the user can continue to assume new roles until their permission set assignments are removed; deleting the user's active session makes the user lose access to the AWS access portal immediately.
  scope: revoking IAM Identity Center user access; the user has an active AWS access portal session.
  link: [they can continue to assume new roles](../facts/iam-identity-center.md#iam-identity-center-disabled-user-keeps-assuming-roles)
  link: [immediately lose access to the AWS access portal](../facts/iam-identity-center.md#iam-identity-center-disabled-user-keeps-assuming-roles)
iam-identity-center-disabled-user-timing
  claim: When a user's access is disabled, the user loses IAM Identity Center access and cannot create new application sessions immediately, loses existing application sessions within 30 minutes, and loses existing AWS account sessions within 12 hours or less, depending on the permission set session duration.
  scope: per user; maximum; user's access disabled.
  link: [Effective immediately](../facts/iam-identity-center.md#iam-identity-center-disabled-user-timing)
  link: [Within 30 minutes](../facts/iam-identity-center.md#iam-identity-center-disabled-user-timing)
  link: [Within 12 hours or less](../facts/iam-identity-center.md#iam-identity-center-disabled-user-timing)
  say: immediately | within thirty minutes | within twelve hours or less
iam-identity-center-does-not-modify-existing-iam
  claim: Enabling IAM Identity Center does not modify existing IAM roles, users or policies in your AWS accounts; it creates new roles and policies for its own use.
  scope: existing IAM roles, users and policies when IAM Identity Center is enabled.
  link: [does not modify any existing IAM roles](../facts/iam-identity-center.md#iam-identity-center-does-not-modify-existing-iam)
  link: [creates new roles and policies](../facts/iam-identity-center.md#iam-identity-center-does-not-modify-existing-iam)
iam-identity-center-emergency-access-direct-federation
  claim: The recommended emergency access configuration lets emergency operations users sign in to the AWS Management Console through direct SAML federation to individual accounts with their usual credentials; it works when IAM Identity Center is unavailable but the IAM data plane and the external IdP are available, and it must be deployed before a disruption.
  scope: emergency access to the AWS Management Console; IAM Identity Center unavailable, IAM data plane and external IdP available.
  link: [through direct federation](../facts/iam-identity-center.md#iam-identity-center-emergency-access-direct-federation)
  link: [IAM data plane and your external identity provider](../facts/iam-identity-center.md#iam-identity-center-emergency-access-direct-federation)
  link: [deploy this configuration before a disruption occurs](../facts/iam-identity-center.md#iam-identity-center-emergency-access-direct-federation)
iam-identity-center-encryption-at-rest-kms
  claim: By default IAM Identity Center encrypts its data at rest with AWS owned KMS keys; you can instead provide your own customer managed KMS keys for identity data such as user and group attributes.
  scope: IAM Identity Center data at rest; default; adjustable; customer managed keys are optional.
  link: [AWS-owned KMS keys](../facts/iam-identity-center.md#iam-identity-center-encryption-at-rest-kms)
  link: [your own customer-managed KMS keys](../facts/iam-identity-center.md#iam-identity-center-encryption-at-rest-kms)
iam-identity-center-encryption-in-transit-tls
  claim: IAM Identity Center encrypts data in transit with TLS 1.2 and TLS 1.3.
  scope: IAM Identity Center data in transit.
  link: [TLS 1.2 and TLS 1.3](../facts/iam-identity-center.md#iam-identity-center-encryption-in-transit-tls)
iam-identity-center-external-idp-no-passwords-stored
  claim: With an external identity provider, IAM Identity Center holds a synchronized copy of user attributes and group membership but no authentication material such as passwords or MFA devices.
  scope: external identity provider as the identity source; when using an external identity provider.
  link: [a synchronized copy of user attributes](../facts/iam-identity-center.md#iam-identity-center-external-idp-no-passwords-stored)
  link: [no authentication material](../facts/iam-identity-center.md#iam-identity-center-external-idp-no-passwords-stored)
iam-identity-center-instance-compare-customer-managed-kms-key
  claim: In the instance comparison table, encryption at rest using a customer managed KMS key is available (Yes) for an instance in the AWS Organizations management account and not (No) for an instance in a member account or in a standalone AWS account.
  scope: IAM Identity Center instance types.
  link: [Encryption at rest using a customer-managed KMS key](../facts/iam-identity-center.md#iam-identity-center-instance-compare-customer-managed-kms-key)
iam-identity-center-instance-compare-delegated-admin
  claim: In the instance comparison table, a delegated administrator can manage an instance in the AWS Organizations management account (Yes) but not an instance in a member account or in a standalone AWS account (No).
  scope: IAM Identity Center instance types.
  link: [Delegated administrator can manage instance](../facts/iam-identity-center.md#iam-identity-center-instance-compare-delegated-admin)
iam-identity-center-instance-compare-multi-account-permissions
  claim: In the instance comparison table, multi-account permissions are available (Yes) for an instance in the AWS Organizations management account and not available (No) for an instance in a member account or in a standalone AWS account.
  scope: IAM Identity Center instance types.
  link: [Multi-account permissions](../facts/iam-identity-center.md#iam-identity-center-instance-compare-multi-account-permissions)
iam-identity-center-instance-compare-multi-region-replication
  claim: In the instance comparison table, replicating IAM Identity Center to additional Regions is available (Yes) for an instance in the AWS Organizations management account and not (No) for an instance in a member account or in a standalone AWS account.
  scope: IAM Identity Center instance types.
  link: [Replicating IAM Identity Center to additional Regions](../facts/iam-identity-center.md#iam-identity-center-instance-compare-multi-region-replication)
iam-identity-center-instance-compare-saml-apps
  claim: In the instance comparison table, SAML 2.0 customer managed applications are supported (Yes) only by an instance in the AWS Organizations management account, not (No) by an instance in a member account or in a standalone AWS account.
  scope: IAM Identity Center instance types.
  link: [SAML 2.0 customer managed applications](../facts/iam-identity-center.md#iam-identity-center-instance-compare-saml-apps)
iam-identity-center-managed-ad-same-region
  claim: With AWS Managed Microsoft AD as the identity source, IAM Identity Center must be enabled in the same AWS Region as the directory, and the AWS access portal uses the directory's access URL.
  scope: AWS Managed Microsoft AD as the identity source.
  link: [in the same AWS Region](../facts/iam-identity-center.md#iam-identity-center-managed-ad-same-region)
  link: [uses the same access URL as your directory](../facts/iam-identity-center.md#iam-identity-center-managed-ad-same-region)
iam-identity-center-management-account-assign-users-not-groups
  claim: AWS recommends assigning users directly, not groups, to permission sets that grant access to the management account, because anyone who can change group membership could change who has management account access.
  scope: access to the AWS Organizations management account.
  link: [assign users directly to permission sets](../facts/iam-identity-center.md#iam-identity-center-management-account-assign-users-not-groups)
  link: [and avoid groups](../facts/iam-identity-center.md#iam-identity-center-management-account-assign-users-not-groups)
iam-identity-center-mfa-context-aware-prompts
  claim: IAM Identity Center MFA settings can require MFA on every sign-in attempt from a new device or browser, or from an unknown IP address.
  scope: IAM Identity Center MFA settings.
  link: [from a new device or browser](../facts/iam-identity-center.md#iam-identity-center-mfa-context-aware-prompts)
  link: [from an unknown IP address](../facts/iam-identity-center.md#iam-identity-center-mfa-context-aware-prompts)
iam-identity-center-mfa-device-types
  claim: IAM Identity Center MFA supports FIDO authenticators (built-in authenticators and security keys), virtual authenticator apps, and your own RADIUS MFA connected through AWS Managed Microsoft AD; all MFA types work for browser console access and for the AWS CLI v2.
  scope: IAM Identity Center MFA.
  link: [built-in authenticators and security keys](../facts/iam-identity-center.md#iam-identity-center-mfa-device-types)
  link: [connected through AWS Managed Microsoft AD](../facts/iam-identity-center.md#iam-identity-center-mfa-device-types)
  link: [browser-based console access as well as using the AWS CLI v2](../facts/iam-identity-center.md#iam-identity-center-mfa-device-types)
iam-identity-center-mfa-devices-per-user
  claim: Each Identity Center directory user can register up to 2 virtual authenticator apps and 6 FIDO authenticators, for a total of 8 MFA devices.
  scope: per user; maximum; not adjustable.
  link: [8 MFA devices](../facts/iam-identity-center.md#iam-identity-center-mfa-devices-per-user)
  link: [2 virtual authenticator apps](../facts/iam-identity-center.md#iam-identity-center-mfa-devices-per-user)
  link: [6 FIDO authenticators](../facts/iam-identity-center.md#iam-identity-center-mfa-devices-per-user)
  say: eight MFA devices | two authenticator apps | six FIDO authenticators
iam-identity-center-mfa-on-by-default
  claim: IAM Identity Center comes with multi-factor authentication (MFA) turned on by default, so all Identity Center directory users must sign in with MFA in addition to their user name and password.
  scope: per IAM Identity Center instance (Identity Center directory users); default; adjustable; Identity Center directory as identity source; not external IdPs.
  link: [turned on by default](../facts/iam-identity-center.md#iam-identity-center-mfa-on-by-default)
  say: on by default
iam-identity-center-mfa-phishing-resistant-fido
  claim: FIDO credentials used for IAM Identity Center MFA are phishing-resistant because they are unique to the website where they were created, such as AWS.
  scope: FIDO authenticators in IAM Identity Center.
  link: [FIDO credentials are phishing-resistant](../facts/iam-identity-center.md#iam-identity-center-mfa-phishing-resistant-fido)
  link: [unique to the website](../facts/iam-identity-center.md#iam-identity-center-mfa-phishing-resistant-fido)
iam-identity-center-migrate-roles-attach-same-policies
  claim: IAM Identity Center provisions new roles in your accounts; to migrate an existing IAM role, you attach the same policies to the new IAM Identity Center roles.
  scope: migrating existing IAM roles to IAM Identity Center.
  link: [provisions new roles](../facts/iam-identity-center.md#iam-identity-center-migrate-roles-attach-same-policies)
  link: [attach the same policies](../facts/iam-identity-center.md#iam-identity-center-migrate-roles-attach-same-policies)
iam-identity-center-multi-region-not-with-active-directory
  claim: Multi-Region support of IAM Identity Center is not available when Active Directory is the identity source.
  scope: IAM Identity Center replicated to additional Regions.
  link: [Multi-Region support is not available for Active Directory](../facts/iam-identity-center.md#iam-identity-center-multi-region-not-with-active-directory)
iam-identity-center-multiple-permission-sets-pick-per-session
  claim: A user can be granted several permission sets for one account and picks which one to assume for each session in the user portal.
  scope: permission sets assigned to one user for one AWS account.
  link: [grant multiple permission sets to your users](../facts/iam-identity-center.md#iam-identity-center-multiple-permission-sets-pick-per-session)
  link: [pick which permission set they want](../facts/iam-identity-center.md#iam-identity-center-multiple-permission-sets-pick-per-session)
iam-identity-center-needs-organizations-all-features
  claim: To add IAM Identity Center to an existing organization, all features of AWS Organizations must be enabled.
  scope: an existing organization in AWS Organizations; adding IAM Identity Center to the organization.
  link: [all AWS Organizations features are enabled](../facts/iam-identity-center.md#iam-identity-center-needs-organizations-all-features)
iam-identity-center-needs-two-way-trust-not-one-way
  claim: To give users of a self-managed AD single sign-on through AWS Managed Microsoft AD, IAM Identity Center requires a two-way trust between AWS Managed Microsoft AD and the self-managed domain; one-way trusts do not work with IAM Identity Center.
  scope: self-managed AD connected through AWS Managed Microsoft AD.
  link: [requires a two-way trust](../facts/iam-identity-center.md#iam-identity-center-needs-two-way-trust-not-one-way)
  link: [One-way trusts do not work](../facts/iam-identity-center.md#iam-identity-center-needs-two-way-trust-not-one-way)
iam-identity-center-no-extra-charge
  claim: IAM Identity Center is offered at no extra charge.
  scope: IAM Identity Center pricing.
  link: [no extra charge](../facts/iam-identity-center.md#iam-identity-center-no-extra-charge)
iam-identity-center-no-outbound-sync-to-idp
  claim: IAM Identity Center does not support outbound synchronization: changes made to users and groups in IAM Identity Center are not sent back to the external IdP.
  scope: external identity provider as identity source.
  link: [doesn't support outbound synchronization](../facts/iam-identity-center.md#iam-identity-center-no-outbound-sync-to-idp)
  link: [will not automatically update](../facts/iam-identity-center.md#iam-identity-center-no-outbound-sync-to-idp)
iam-identity-center-on-prem-ad-two-options
  claim: There are two ways to connect an on-premises Active Directory to IAM Identity Center: AD Connector, or a trust relationship with AWS Managed Microsoft AD.
  scope: on-premises Active Directory as the identity source.
  link: [use AD Connector](../facts/iam-identity-center.md#iam-identity-center-on-prem-ad-two-options)
  link: [AWS Managed Microsoft AD trust relationship](../facts/iam-identity-center.md#iam-identity-center-on-prem-ad-two-options)
iam-identity-center-one-ad-directory-managed-ad-for-multiple-forests
  claim: IAM Identity Center can connect only one AD Connector directory or one AWS Managed Microsoft AD directory at a time; to support multiple domains or forests, AWS says to use AWS Managed Microsoft AD.
  scope: Active Directory as the IAM Identity Center identity source.
  link: [connect only one AD Connector directory](../facts/iam-identity-center.md#iam-identity-center-one-ad-directory-managed-ad-for-multiple-forests)
  link: [support multiple domains or forests](../facts/iam-identity-center.md#iam-identity-center-one-ad-directory-managed-ad-for-multiple-forests)
iam-identity-center-one-identity-source-at-a-time
  claim: IAM Identity Center can be connected to only one directory or one SAML 2.0 identity provider at a time, although you can change the connected source.
  scope: per IAM Identity Center instance; maximum.
  link: [only one directory or one SAML 2.0 identity provider](../facts/iam-identity-center.md#iam-identity-center-one-identity-source-at-a-time)
iam-identity-center-one-org-instance-per-management-account
  claim: An organization instance of IAM Identity Center must be enabled in the management account, and there can be only one organization instance for each management account in AWS Organizations.
  scope: per management account in AWS Organizations.
  link: [must be enabled in your management account](../facts/iam-identity-center.md#iam-identity-center-one-org-instance-per-management-account)
  link: [only one organization instance for each management account](../facts/iam-identity-center.md#iam-identity-center-one-org-instance-per-management-account)
iam-identity-center-one-point-of-federation
  claim: IAM Identity Center is one point of federation: you federate once and, with a SAML 2.0 identity provider, have only one certificate to manage for multiple AWS managed applications and AWS accounts.
  scope: IAM Identity Center with an external identity provider.
  link: [you only federate once](../facts/iam-identity-center.md#iam-identity-center-one-point-of-federation)
  link: [only one certificate to manage](../facts/iam-identity-center.md#iam-identity-center-one-point-of-federation)
iam-identity-center-one-sign-in-all-assignments
  claim: When a user signs in to the AWS access portal, IAM Identity Center creates an authentication session, and the user can then access all assigned AWS accounts, AWS managed applications and customer managed applications without additional sign-ins.
  scope: AWS access portal sign-in.
  link: [without additional sign ins](../facts/iam-identity-center.md#iam-identity-center-one-sign-in-all-assignments)
  link: [creates an authentication session](../facts/iam-identity-center.md#iam-identity-center-one-sign-in-all-assignments)
iam-identity-center-operates-across-multiple-azs
  claim: IAM Identity Center is fully managed and operates across multiple Availability Zones so that it stays available during an Availability Zone disruption.
  scope: IAM Identity Center in its Region.
  link: [operates across multiple Availability Zones](../facts/iam-identity-center.md#iam-identity-center-operates-across-multiple-azs)
  link: [The IAM Identity Center service is fully managed](../facts/iam-identity-center.md#iam-identity-center-operates-across-multiple-azs)
iam-identity-center-opt-in-region-enable-in-all-accounts
  claim: If IAM Identity Center is deployed in an opt-in Region, that Region must be enabled in every account whose access is managed through IAM Identity Center, including accounts added later.
  scope: IAM Identity Center in an opt-in Region; instance deployed in an opt-in Region.
  link: [enable this Region in all the accounts](../facts/iam-identity-center.md#iam-identity-center-opt-in-region-enable-in-all-accounts)
  link: [repeat this action when you add new accounts](../facts/iam-identity-center.md#iam-identity-center-opt-in-region-enable-in-all-accounts)
iam-identity-center-org-instance-controls-account-instances
  claim: An organization instance supports all IAM Identity Center features, including managing permissions for multiple AWS accounts, assigning access to customer managed applications and multi-Region replication. It also lets you control whether member accounts can create account instances, as long as you haven't deployed the organization instance in an opt-in Region (a Region that is disabled by default).
  scope: organization instance of IAM Identity Center; control of account instances needs the instance not to be in an opt-in Region.
  link: [Support for all features of IAM Identity Center](../facts/iam-identity-center.md#iam-identity-center-org-instance-controls-account-instances)
  link: [Central control of the creation of account instances](../facts/iam-identity-center.md#iam-identity-center-org-instance-controls-account-instances)
iam-identity-center-org-instance-enabled-from-management-account
  claim: An organization instance of IAM Identity Center is enabled by signing in to the AWS Organizations management account; with administrative credentials from a member account you can enable an account instance.
  scope: enabling an IAM Identity Center instance.
  link: [your AWS Organizations management account](../facts/iam-identity-center.md#iam-identity-center-org-instance-enabled-from-management-account)
  link: [you can enable an account instance](../facts/iam-identity-center.md#iam-identity-center-org-instance-enabled-from-management-account)
iam-identity-center-org-instance-only-one-for-account-access
  claim: An organization instance of IAM Identity Center is deployed in the AWS Organizations management account and is the only instance type that can manage access to AWS accounts; AWS recommends it for all production use of applications.
  scope: organization instance of IAM Identity Center.
  link: [deployed in the AWS Organizations management account](../facts/iam-identity-center.md#iam-identity-center-org-instance-only-one-for-account-access)
  link: [manage access to AWS accounts](../facts/iam-identity-center.md#iam-identity-center-org-instance-only-one-for-account-access)
  link: [recommended for all production use of applications](../facts/iam-identity-center.md#iam-identity-center-org-instance-only-one-for-account-access)
iam-identity-center-organizations-recommended-not-required
  claim: AWS Organizations is recommended but not required for IAM Identity Center; enabling IAM Identity Center with AWS Organizations creates an organization instance.
  scope: enabling IAM Identity Center.
  link: [recommended, but not required](../facts/iam-identity-center.md#iam-identity-center-organizations-recommended-not-required)
  link: [creates an organization instance](../facts/iam-identity-center.md#iam-identity-center-organizations-recommended-not-required)
iam-identity-center-permission-set-change-updates-roles
  claim: When a permission set is assigned, IAM Identity Center creates IAM Identity Center-controlled IAM roles in each account and attaches the permission set's policies; when the permission set is modified, IAM Identity Center updates the corresponding IAM policies and roles.
  scope: accounts where the permission set is assigned.
  link: [attaches the policies specified in the permission set](../facts/iam-identity-center.md#iam-identity-center-permission-set-change-updates-roles)
  link: [corresponding IAM policies and roles are updated accordingly](../facts/iam-identity-center.md#iam-identity-center-permission-set-change-updates-roles)
iam-identity-center-permission-set-is-policy-template
  claim: A permission set is a template, created and maintained by the administrator, that defines a collection of one or more IAM policies and is used to assign AWS account access to users and groups.
  scope: IAM Identity Center permission set.
  link: [a template that you create and maintain](../facts/iam-identity-center.md#iam-identity-center-permission-set-is-policy-template)
  link: [simplify the assignment of AWS account access](../facts/iam-identity-center.md#iam-identity-center-permission-set-is-policy-template)
iam-identity-center-permission-set-policy-types
  claim: A permission set can hold AWS managed policies, customer managed policies, inline policies and AWS managed policies for job functions, and can use an AWS managed policy or a customer managed policy as a permissions boundary.
  scope: IAM Identity Center permission set.
  link: [AWS managed policy or a customer managed policy](../facts/iam-identity-center.md#iam-identity-center-permission-set-policy-types)
  link: [to your permission sets](../facts/iam-identity-center.md#iam-identity-center-permission-set-policy-types)
iam-identity-center-permission-set-session-duration
  claim: A new permission set has a session duration of 1 hour by default; it can be set from 1 hour up to 12 hours, and the IAM roles that IAM Identity Center creates for permission sets have a maximum session duration of 12 hours.
  scope: per permission set; default; adjustable; AWS account access through IAM Identity Center.
  link: [1 hour](../facts/iam-identity-center.md#iam-identity-center-permission-set-session-duration)
  link: [12 hours](../facts/iam-identity-center.md#iam-identity-center-permission-set-session-duration)
  say: one hour | twelve hours
iam-identity-center-permission-sets-applied-automatically
  claim: Permission sets are a collection of permissions that you create in IAM Identity Center, modelled on AWS managed policies for job functions or any AWS managed policies, and you can also fully customize them; IAM Identity Center applies these permissions to the selected accounts automatically.
  scope: IAM Identity Center permission sets.
  link: [a collection of permissions](../facts/iam-identity-center.md#iam-identity-center-permission-sets-applied-automatically)
  link: [applies these permissions to the selected accounts automatically](../facts/iam-identity-center.md#iam-identity-center-permission-sets-applied-automatically)
iam-identity-center-permission-sets-need-organization-instance
  claim: Permission sets are available only with an organization instance of IAM Identity Center.
  scope: IAM Identity Center permission sets.
  link: [need to use an Organization instance](../facts/iam-identity-center.md#iam-identity-center-permission-sets-need-organization-instance)
  link: [available only for organization instances](../facts/iam-identity-center.md#iam-identity-center-permission-sets-need-organization-instance)
iam-identity-center-phased-migration-existing-iam-keeps-working
  claim: After IAM Identity Center is enabled, existing IAM roles and users keep working as before, so you can migrate to it in phases without disrupting existing access.
  scope: existing IAM roles and users after IAM Identity Center is enabled.
  link: [will continue to function as-is](../facts/iam-identity-center.md#iam-identity-center-phased-migration-existing-iam-keeps-working)
  link: [in a phased approach](../facts/iam-identity-center.md#iam-identity-center-phased-migration-existing-iam-keeps-working)
iam-identity-center-portal-credentials-for-cli-sdk
  claim: After signing in to the AWS access portal, an IAM Identity Center user can get temporary credentials and use them in the AWS CLI or AWS SDKs to access resources in an AWS account.
  scope: IAM Identity Center users with an assigned permission set; the user is assigned a permission set in the account.
  link: [you can get temporary credentials](../facts/iam-identity-center.md#iam-identity-center-portal-credentials-for-cli-sdk)
  link: [in the AWS CLI or AWS SDKs](../facts/iam-identity-center.md#iam-identity-center-portal-credentials-for-cli-sdk)
iam-identity-center-primary-region-cannot-change
  claim: When IAM Identity Center is enabled it is deployed to the currently selected Region, called the primary Region, and the primary Region cannot be changed after IAM Identity Center is enabled.
  scope: per IAM Identity Center instance.
  link: [referred to as the "primary Region"](../facts/iam-identity-center.md#iam-identity-center-primary-region-cannot-change)
  link: [the primary Region cannot be changed](../facts/iam-identity-center.md#iam-identity-center-primary-region-cannot-change)
iam-identity-center-provision-before-assign
  claim: Identities from an existing IdP must be provisioned into IAM Identity Center before you can assign permissions to them.
  scope: external identity provider as the identity source; identities from an existing IdP.
  link: [must be provisioned into IAM Identity Center](../facts/iam-identity-center.md#iam-identity-center-provision-before-assign)
iam-identity-center-quota-accounts-or-applications
  claim: IAM Identity Center can configure 7000 AWS accounts and 7000 applications by default, and the quota can be increased.
  scope: per IAM Identity Center instance (accounts and applications counted separately); default; adjustable.
  link: [7000](../facts/iam-identity-center.md#iam-identity-center-quota-accounts-or-applications)
  say: seven thousand
iam-identity-center-quota-connected-directories
  claim: IAM Identity Center can have 1 connected directory at a time, and this quota cannot be increased.
  scope: per IAM Identity Center instance; maximum; not adjustable; Active Directory as the identity source.
  link: [1](../facts/iam-identity-center.md#iam-identity-center-quota-connected-directories)
  say: one
iam-identity-center-quota-groups
  claim: The IAM Identity Center identity store supports 100000 groups by default, and the quota can be increased.
  scope: per IAM Identity Center identity store; default; adjustable.
  link: [100000](../facts/iam-identity-center.md#iam-identity-center-quota-groups)
  say: one hundred thousand
iam-identity-center-quota-groups-per-permission-set-per-account
  claim: At most 100 groups can be assigned to one permission set in one AWS account, or to one application, and this quota cannot be increased.
  scope: per permission set per AWS account, or per application; maximum; not adjustable.
  link: [100](../facts/iam-identity-center.md#iam-identity-center-quota-groups-per-permission-set-per-account)
  say: one hundred
iam-identity-center-quota-increase-from-management-or-delegated-admin
  claim: A quota increase request for IAM Identity Center must come from the management account or the delegated administrator account.
  scope: per organization.
  link: [a management or delegated administrator account](../facts/iam-identity-center.md#iam-identity-center-quota-increase-from-management-or-delegated-admin)
  say: the management account or the delegated administrator account
iam-identity-center-quota-inline-policy-per-permission-set
  claim: A permission set can have 1 inline policy, and the quota cannot be increased.
  scope: per permission set; maximum; not adjustable.
  link: [1](../facts/iam-identity-center.md#iam-identity-center-quota-inline-policy-per-permission-set)
  say: one
iam-identity-center-quota-inline-policy-size
  claim: The inline policy of a permission set can be at most 32,768 bytes, with at most 10,240 bytes of non-whitespace characters, and this quota cannot be increased.
  scope: per permission set (inline policy); maximum; not adjustable.
  link: [32,768 bytes](../facts/iam-identity-center.md#iam-identity-center-quota-inline-policy-size)
  link: [10,240 bytes](../facts/iam-identity-center.md#iam-identity-center-quota-inline-policy-size)
  say: thirty-two thousand seven hundred sixty-eight bytes | ten thousand two hundred forty bytes
iam-identity-center-quota-one-instance-per-account
  claim: An account can have 1 instance of IAM Identity Center, and the quota cannot be increased.
  scope: per AWS account; maximum; not adjustable.
  link: [1](../facts/iam-identity-center.md#iam-identity-center-quota-one-instance-per-account)
  say: one
iam-identity-center-quota-permission-sets
  claim: IAM Identity Center allows 3500 permission sets by default, and the quota can be increased.
  scope: per IAM Identity Center instance; default; adjustable.
  link: [3500](../facts/iam-identity-center.md#iam-identity-center-quota-permission-sets)
  say: three thousand five hundred
iam-identity-center-quota-provisioned-permission-sets-per-account
  claim: An AWS account can have 500 provisioned permission sets by default, and the quota can be increased.
  scope: per AWS account; default; adjustable.
  link: [500](../facts/iam-identity-center.md#iam-identity-center-quota-provisioned-permission-sets-per-account)
  say: five hundred
iam-identity-center-quota-regions-per-instance
  claim: One IAM Identity Center instance can have at most 6 AWS Regions enabled by default, and this quota can be increased.
  scope: per IAM Identity Center instance; default; adjustable; multi-Region IAM Identity Center.
  link: [6](../facts/iam-identity-center.md#iam-identity-center-quota-regions-per-instance)
  say: six
iam-identity-center-quota-saml-assertion-size
  claim: A SAML assertion in IAM Identity Center can hold at most 50,000 characters, and this quota cannot be increased.
  scope: per SAML assertion (applications); maximum; not adjustable.
  link: [50,000 characters](../facts/iam-identity-center.md#iam-identity-center-quota-saml-assertion-size)
  say: fifty thousand characters
iam-identity-center-quota-trusted-token-issuers
  claim: IAM Identity Center allows 10 trusted token issuers in total, and this quota cannot be increased.
  scope: per IAM Identity Center instance; maximum; not adjustable.
  link: [10](../facts/iam-identity-center.md#iam-identity-center-quota-trusted-token-issuers)
  say: ten
iam-identity-center-quota-users
  claim: The IAM Identity Center identity store supports 200000 users by default, and the quota can be increased.
  scope: per IAM Identity Center identity store; default; adjustable.
  link: [200000](../facts/iam-identity-center.md#iam-identity-center-quota-users)
  say: two hundred thousand
iam-identity-center-radius-mfa-with-directory-service
  claim: An existing RADIUS MFA setup can be used with IAM Identity Center and AWS Directory Service as a second form of verification.
  scope: IAM Identity Center MFA with AWS Directory Service; with AWS Directory Service.
  link: [Remote Authentication Dial-In User Service (RADIUS) MFA configuration](../facts/iam-identity-center.md#iam-identity-center-radius-mfa-with-directory-service)
iam-identity-center-recommended-front-door
  claim: AWS calls IAM Identity Center its recommended front door into AWS and the primary tool to manage the AWS access of workforce users.
  scope: workforce access to AWS.
  link: [our recommended front door into AWS](../facts/iam-identity-center.md#iam-identity-center-recommended-front-door)
  link: [primary tool](../facts/iam-identity-center.md#iam-identity-center-recommended-front-door)
iam-identity-center-region-accessible-and-app-colocation
  claim: For single sign-on to AWS accounts, the Region where IAM Identity Center is enabled must be accessible by all users in the organization, and most AWS managed applications require IAM Identity Center to be available in the same Region as the application.
  scope: choosing the IAM Identity Center Region.
  link: [accessible by all of the users](../facts/iam-identity-center.md#iam-identity-center-region-accessible-and-app-colocation)
  link: [available in the same Region as the application](../facts/iam-identity-center.md#iam-identity-center-region-accessible-and-app-colocation)
iam-identity-center-replication-keeps-access-in-regional-disruption
  claim: Replicating an IAM Identity Center instance to additional Regions maintains AWS account access with already provisioned permissions during a Regional disruption.
  scope: organization instance replicated to additional Regions; the instance is replicated to additional Regions.
  link: [maintain account access with already provisioned permissions](../facts/iam-identity-center.md#iam-identity-center-replication-keeps-access-in-regional-disruption)
  link: [in the event of a Regional disruption](../facts/iam-identity-center.md#iam-identity-center-replication-keeps-access-in-regional-disruption)
iam-identity-center-replication-to-additional-regions
  claim: When an IAM Identity Center instance is replicated to additional Regions, IAM Identity Center automatically replicates users, groups, permission sets and their assignments, and other metadata and configuration to those Regions.
  scope: organization instance replicated to additional Regions; the instance is replicated to additional Regions.
  link: [automatically replicates users, groups, permission sets](../facts/iam-identity-center.md#iam-identity-center-replication-to-additional-regions)
  link: [permission sets and their assignments](../facts/iam-identity-center.md#iam-identity-center-replication-to-additional-regions)
iam-identity-center-revoke-keep-deny-12-hours
  claim: AWS's general procedure to revoke an active permission set session assumes a deny-all policy in a service control policy (SCP): you add the user's ID to that Deny policy and leave it in place for at least 12 hours; otherwise a user with an active IAM role session gets the role's actions back, and after 12 hours the active sessions expire.
  scope: revoking active permission set sessions; a deny policy for the user in an SCP.
  link: [If you wait 12 hours](../facts/iam-identity-center.md#iam-identity-center-revoke-keep-deny-12-hours)
  link: [active sessions expire](../facts/iam-identity-center.md#iam-identity-center-revoke-keep-deny-12-hours)
  link: [will have restored actions with the IAM role](../facts/iam-identity-center.md#iam-identity-center-revoke-keep-deny-12-hours)
iam-identity-center-role-sessions-persist-up-to-12-hours
  claim: IAM role sessions created from a permission set operate independently once established: they last for the duration configured in the permission set, up to 12 hours, regardless of the status of the original sign-in session.
  scope: per IAM role session (permission set); maximum; duration set in the permission set.
  link: [up to 12 hours](../facts/iam-identity-center.md#iam-identity-center-role-sessions-persist-up-to-12-hours)
  link: [regardless of the status of the original](../facts/iam-identity-center.md#iam-identity-center-role-sessions-persist-up-to-12-hours)
  link: [operate independently once established](../facts/iam-identity-center.md#iam-identity-center-role-sessions-persist-up-to-12-hours)
  say: up to twelve hours | sign-out does not end them | they run on their own
iam-identity-center-roles-named-awsreservedsso
  claim: IAM roles whose names begin with AWSReservedSSO_ are the roles IAM Identity Center created in the account when a permission set was assigned to it.
  scope: member accounts with permission set assignments.
  link: [came from assigning a permission set](../facts/iam-identity-center.md#iam-identity-center-roles-named-awsreservedsso)
  link: [the IAM Identity Center service has created](../facts/iam-identity-center.md#iam-identity-center-roles-named-awsreservedsso)
iam-identity-center-saml-and-oauth-customer-apps
  claim: IAM Identity Center can assign your users access to SAML 2.0 applications (a SAML 2.0 application connects to an organization instance), including AWS services such as Connect Customer and AWS Client VPN, which integrate with IAM Identity Center exclusively using SAML. If an application supports JSON Web Tokens (JWTs), the trusted identity propagation feature lets it request access to data in AWS services on behalf of your users.
  scope: customer managed applications.
  link: [exclusively using SAML](../facts/iam-identity-center.md#iam-identity-center-saml-and-oauth-customer-apps)
  link: [request access to data in AWS services](../facts/iam-identity-center.md#iam-identity-center-saml-and-oauth-customer-apps)
  link: [Connect Customer and AWS Client VPN](../facts/iam-identity-center.md#iam-identity-center-saml-and-oauth-customer-apps)
iam-identity-center-saml-customer-apps-public-url
  claim: IAM Identity Center can authenticate and authorize access to SAML-based customer managed applications that are reachable through a public URL, whatever platform or cloud the application is built on.
  scope: customer managed applications; the application is reachable through a public URL.
  link: [SAML-based customer managed applications](../facts/iam-identity-center.md#iam-identity-center-saml-customer-apps-public-url)
  link: [reachable through a public URL](../facts/iam-identity-center.md#iam-identity-center-saml-customer-apps-public-url)
iam-identity-center-saml-idp-uses-provider-mfa
  claim: When a SAML 2.0 IdP is the identity source, you enable the MFA capabilities of that provider; with the Identity Center store or Active Directory, IAM Identity Center supports WebAuthn security keys and built-in biometric authenticators.
  scope: IAM Identity Center MFA by identity source; depends on the identity source.
  link: [multi-factor authentication capabilities of your provider](../facts/iam-identity-center.md#iam-identity-center-saml-idp-uses-provider-mfa)
  link: [the Web Authentication specification](../facts/iam-identity-center.md#iam-identity-center-saml-idp-uses-provider-mfa)
iam-identity-center-saml-nameid-must-match-username
  claim: With an external SAML IdP, the assertion's Subject NameID must exactly match the Username of a user provisioned in IAM Identity Center; sign-in fails without a match even when the IdP authenticated the user.
  scope: external SAML identity provider.
  link: [must exactly match the **Username**](../facts/iam-identity-center.md#iam-identity-center-saml-nameid-must-match-username)
  link: [Sign-in fails](../facts/iam-identity-center.md#iam-identity-center-saml-nameid-must-match-username)
iam-identity-center-scim-automatic-provisioning
  claim: IAM Identity Center supports automatic provisioning (synchronization) of user and group information from an external IdP into IAM Identity Center with the SCIM v2.0 protocol, configured in the IdP with the IAM Identity Center SCIM endpoint and a bearer token.
  scope: external identity provider as identity source.
  link: [automatic provisioning (synchronization) of user and group information](../facts/iam-identity-center.md#iam-identity-center-scim-automatic-provisioning)
  link: [a bearer token that you create](../facts/iam-identity-center.md#iam-identity-center-scim-automatic-provisioning)
iam-identity-center-scim-automatic-sync
  claim: IAM Identity Center can synchronize user and group information automatically from Okta Universal Directory, Microsoft Entra ID, OneLogin and PingFederate with the SCIM standard.
  scope: external identity provider as the identity source.
  link: [System for Cross-domain Identity Management (SCIM)](../facts/iam-identity-center.md#iam-identity-center-scim-automatic-sync)
iam-identity-center-scim-changes-after-idp-sends
  claim: With SCIM, the identity provider controls provisioning and update intervals; changes to users and groups in the IdP appear in IAM Identity Center only after the IdP sends them.
  scope: SCIM provisioning from an external identity provider.
  link: [controlled by your identity provider](../facts/iam-identity-center.md#iam-identity-center-scim-changes-after-idp-sends)
  link: [only reflected in IAM Identity Center after](../facts/iam-identity-center.md#iam-identity-center-scim-changes-after-idp-sends)
iam-identity-center-signout-app-sessions-end-within-30-minutes
  claim: When a user signs out of the AWS access portal, existing application sessions do not end instantly but within approximately 30 minutes at their next refresh, and existing IAM role sessions continue until they expire, which could be up to 12 hours later.
  scope: sessions after sign-out from the AWS access portal.
  link: [don't end instantly](../facts/iam-identity-center.md#iam-identity-center-signout-app-sessions-end-within-30-minutes)
  link: [within approximately 30 minutes](../facts/iam-identity-center.md#iam-identity-center-signout-app-sessions-end-within-30-minutes)
  link: [up to 12 hours later](../facts/iam-identity-center.md#iam-identity-center-signout-app-sessions-end-within-30-minutes)
iam-identity-center-simple-ad-not-identity-source
  claim: IAM Identity Center does not support Samba 4-based Simple AD as an identity source or as a connected directory.
  scope: IAM Identity Center identity source.
  link: [does not support SAMBA4-based Simple AD](../facts/iam-identity-center.md#iam-identity-center-simple-ad-not-identity-source)
  link: [Simple AD as a connected directory](../facts/iam-identity-center.md#iam-identity-center-simple-ad-not-identity-source)
iam-identity-center-stores-attributes-assignments-permissions
  claim: IAM Identity Center stores user and group attributes, the metadata of which accounts and applications are assigned to which users and groups, and the permissions granted for AWS account access.
  scope: data that IAM Identity Center stores.
  link: [stores your user and group attributes](../facts/iam-identity-center.md#iam-identity-center-stores-attributes-assignments-permissions)
iam-identity-center-temporary-elevated-access-via-partners
  claim: Temporary elevated access (just-in-time access) is a way to request, approve and track the use of a permission for a specific task during a specified time; IAM Identity Center provides it by integrating with solutions from AWS Security Competency partners.
  scope: temporary elevated access with IAM Identity Center.
  link: [also known as just-in-time access](../facts/iam-identity-center.md#iam-identity-center-temporary-elevated-access-via-partners)
  link: [request, approve, and track](../facts/iam-identity-center.md#iam-identity-center-temporary-elevated-access-via-partners)
  link: [solutions from AWS Security Competency partners](../facts/iam-identity-center.md#iam-identity-center-temporary-elevated-access-via-partners)
iam-identity-center-throttle-limits-per-enabled-region
  claim: When an IAM Identity Center instance is enabled in multiple AWS Regions, its API throttle limits apply equally to each enabled Region.
  scope: per enabled Region; multi-Region instance.
  link: [apply equally to each enabled Region](../facts/iam-identity-center.md#iam-identity-center-throttle-limits-per-enabled-region)
  say: each enabled Region gets the same limits
iam-identity-center-tip-built-on-oauth
  claim: Trusted identity propagation is built on the OAuth 2.0 Authorization Framework and can exchange identity tokens from an external OAuth 2.0 authorization server for tokens issued by IAM Identity Center that AWS services recognize, so an application can request data access on behalf of a user.
  scope: trusted identity propagation.
  link: [built on the OAuth 2.0 Authorization Framework](../facts/iam-identity-center.md#iam-identity-center-tip-built-on-oauth)
  link: [exchange identity tokens](../facts/iam-identity-center.md#iam-identity-center-tip-built-on-oauth)
iam-identity-center-tip-identity-context
  claim: Trusted identity propagation adds identity context to an IAM role to identify the user requesting access, propagates it to other AWS services so their administrators can grant permissions based on user attributes such as group associations, and lets them audit who accessed what data in service logs or CloudTrail.
  scope: trusted identity propagation.
  link: [identity context is added to an IAM role](../facts/iam-identity-center.md#iam-identity-center-tip-identity-context)
  link: [user attributes such as group associations](../facts/iam-identity-center.md#iam-identity-center-tip-identity-context)
  link: [audit who accessed what data](../facts/iam-identity-center.md#iam-identity-center-tip-identity-context)
iam-identity-center-tip-user-identity-audit
  claim: With trusted identity propagation, AWS managed applications such as Amazon Quick can securely share a user's identity with other AWS managed applications such as Amazon Redshift and authorize access to AWS resources based on the user's identity; CloudTrail events are logged based on the user and the actions the user initiated.
  scope: trusted identity propagation.
  link: [securely share a user’s identity](../facts/iam-identity-center.md#iam-identity-center-tip-user-identity-audit)
  link: [CloudTrail events are logged based on the user](../facts/iam-identity-center.md#iam-identity-center-tip-user-identity-audit)
iam-identity-center-trusted-identity-propagation-oauth
  claim: Trusted identity propagation is built on the OAuth 2.0 Authorization Framework and lets applications access data on behalf of a specific user without sharing that user's credentials.
  scope: trusted identity propagation.
  link: [OAuth 2.0 Authorization Framework](../facts/iam-identity-center.md#iam-identity-center-trusted-identity-propagation-oauth)
  link: [without sharing that user's credentials](../facts/iam-identity-center.md#iam-identity-center-trusted-identity-propagation-oauth)
iam-identity-center-user-interactive-session-default-8-hours
  claim: The default duration of an AWS access portal (user interactive) session is 8 hours; you can set it from 15 minutes to 90 days.
  scope: user interactive sessions (AWS access portal); default; adjustable; settable from 15 minutes to 90 days.
  link: [8 hours](../facts/iam-identity-center.md#iam-identity-center-user-interactive-session-default-8-hours)
  link: [15 minutes](../facts/iam-identity-center.md#iam-identity-center-user-interactive-session-default-8-hours)
  link: [90 days](../facts/iam-identity-center.md#iam-identity-center-user-interactive-session-default-8-hours)
  say: eight hours | fifteen minutes | ninety days
iam-identity-center-user-interactive-session-max-90-days
  claim: An AWS access portal (user interactive) session lasts for the duration configured in IAM Identity Center, which can be up to 90 days; it ends when the user signs out or an administrator ends it.
  scope: per user interactive session; maximum; adjustable; duration is configured by the administrator.
  link: [up to 90 days](../facts/iam-identity-center.md#iam-identity-center-user-interactive-session-max-90-days)
  say: up to ninety days
iam-identity-center-users-get-temporary-credentials
  claim: Users in IAM Identity Center are different from IAM users: IAM users have long-term credentials, while IAM Identity Center users get temporary credentials that are generated every time they sign in, which AWS recommends as a security best practice.
  scope: IAM Identity Center users.
  link: [IAM users are granted long-term credentials](../facts/iam-identity-center.md#iam-identity-center-users-get-temporary-credentials)
  link: [are granted temporary credentials](../facts/iam-identity-center.md#iam-identity-center-users-get-temporary-credentials)
  link: [generated every time you sign in](../facts/iam-identity-center.md#iam-identity-center-users-get-temporary-credentials)
iam-identity-center-wa-customer-rotates-scim-tokens-and-certificates
  claim: The customer is responsible for rotating SCIM access tokens and the certificates that support identity federation.
  scope: external identity provider federation.
  link: [the rotation of SCIM access tokens](../facts/iam-identity-center.md#iam-identity-center-wa-customer-rotates-scim-tokens-and-certificates)
  link: [rotating the certificates supporting your identity federation](../facts/iam-identity-center.md#iam-identity-center-wa-customer-rotates-scim-tokens-and-certificates)
iam-identity-center-wa-remove-iam-users-after-federation
  claim: After workforce federation is in place, the security pillar says to identify and remove IAM users, IAM groups and long-lived credentials that are no longer needed; an SCP can help prevent the creation of new IAM users and groups so that access to AWS is through federated identities.
  scope: workforce users federated to AWS.
  link: [long-lived user credentials (passwords and access keys)](../facts/iam-identity-center.md#iam-identity-center-wa-remove-iam-users-after-federation)
  link: [prevent the creation of new IAM users](../facts/iam-identity-center.md#iam-identity-center-wa-remove-iam-users-after-federation)
  link: [access to AWS is via federated identities](../facts/iam-identity-center.md#iam-identity-center-wa-remove-iam-users-after-federation)
iam-identity-center-wa-two-federation-approaches
  claim: The security pillar names two levels for federating workforce users to AWS: direct federation to each AWS account with IAM, or IAM Identity Center for single sign-on to multiple AWS accounts in an AWS organization.
  scope: workforce users accessing AWS.
  link: [direct federation to each AWS account](../facts/iam-identity-center.md#iam-identity-center-wa-two-federation-approaches)
  link: [single sign-on to multiple AWS accounts](../facts/iam-identity-center.md#iam-identity-center-wa-two-federation-approaches)
  link: [directly to each AWS account](../facts/iam-identity-center.md#iam-identity-center-wa-two-federation-approaches)
iam-identity-center-wa-workforce-centralized-idp
  claim: The Well-Architected security pillar (SEC02-BP04) says to rely on an identity provider that manages workforce identities (employees and contractors) in a centralized place.
  scope: workforce identities.
  link: [rely on an identity provider](../facts/iam-identity-center.md#iam-identity-center-wa-workforce-centralized-idp)
  link: [manage identities in a centralized place](../facts/iam-identity-center.md#iam-identity-center-wa-workforce-centralized-idp)
iam-identity-center-workforce-sso-to-accounts-and-applications
  claim: IAM Identity Center gives employees single sign-on from an existing identity provider to user-facing AWS applications and to the AWS Management Console, including the AWS accounts assigned to them.
  scope: workforce single sign-on to AWS accounts and AWS applications.
  link: [single sign-on experience of your employees](../facts/iam-identity-center.md#iam-identity-center-workforce-sso-to-accounts-and-applications)
  link: [including any AWS accounts that are assigned](../facts/iam-identity-center.md#iam-identity-center-workforce-sso-to-accounts-and-applications)
  say: workforce single sign-on | the console for their assigned accounts
