import sys; sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway")
from fh import *
C = "apigateway-control-access-to-api"; RP = "apigateway-resource-policies"; AF = "apigateway-authorization-flow"; PM = "permissions"
INA = "You can use the following mechanisms for authentication and authorization:"
INO = "You can use the following mechanisms for performing other tasks related to access control:"
INT = "You can use the following mechanisms for tracking and limiting the access that you have granted to authorized clients:"
B = ["1.2.K4"]
fs = []
fs.append(F("access-control-resource-policies-listed-auth", "capability",
 "AWS lists API Gateway resource policies as a mechanism for authentication and authorization: resource-based policies that allow or deny access to your APIs and methods from specified source IP addresses or VPC endpoints.",
 "Which REST API access-control options does AWS list as authentication and authorization, and what do resource policies control?",
 ["allow or deny access to your APIs and methods", "specified source IP addresses or VPC endpoints"],
 [ev(C, INA), ev(C, "Resource policies let you create resource-based policies to allow or deny access to your APIs and methods from specified source IP addresses or VPC endpoints.")],
 scope="REST APIs", bullets=B, tier0=True))
fs.append(F("access-control-iam-listed-auth", "capability",
 "AWS lists standard IAM roles and policies as an authentication and authorization mechanism for REST APIs; they can be applied to an entire API or individual methods and control who can create and manage APIs as well as who can invoke them.",
 "Can IAM roles and policies control who invokes a REST API as well as who manages it?",
 ["applied to an entire API or individual methods", "who can create and manage your APIs, as well as who can invoke them"],
 [ev(C, INA), ev(C, "Standard AWS IAM roles and policies offer flexible and robust access controls that can be applied to an entire API or individual methods. IAM roles and policies can be used for controlling who can create and manage your APIs, as well as who can invoke them.")],
 scope="REST APIs", bullets=B, tier0=True))
fs.append(F("access-control-lambda-authorizers-listed-auth", "capability",
 "AWS lists Lambda authorizers as an authentication and authorization mechanism: Lambda functions that control access to REST API methods using bearer token authentication as well as request parameters such as headers, paths, query strings, stage variables, or context variables.",
 "What do Lambda authorizers use to decide who may invoke a REST API method?",
 ["bearer token authentication", "headers, paths, query strings, stage variables, or context variables"],
 [ev(C, INA), ev(C, "Lambda authorizers are Lambda functions that control access to REST API methods using bearer token authentication—as well as information described by headers, paths, query strings, stage variables, or context variables request parameters. Lambda authorizers are used to control who can invoke REST API methods.")],
 scope="REST APIs", bullets=B, tier0=True))
fs.append(F("access-control-cognito-user-pools-listed-auth", "capability",
 "AWS lists Amazon Cognito user pools as an authentication and authorization mechanism that lets you create customizable solutions for your REST APIs and control who can invoke REST API methods.",
 "Can Amazon Cognito user pools control who invokes a REST API method?",
 ["customizable authentication and authorization solutions", "control who can invoke REST API methods"],
 [ev(C, INA), ev(C, "Amazon Cognito user pools let you create customizable authentication and authorization solutions for your REST APIs. Amazon Cognito user pools are used to control who can invoke REST API methods.")],
 scope="REST APIs", bullets=B, tier0=True))
fs.append(F("access-control-vpc-endpoint-policies-private-apis", "capability",
 "Endpoint policies for interface VPC endpoints let you attach IAM resource policies to interface VPC endpoints to improve the security of your private APIs.",
 "What do VPC endpoint policies add for private APIs?",
 ["attach IAM resource policies to interface VPC endpoints", "improve the security of your private APIs"],
 [ev(C, INA), ev(C, "Endpoint policies for interface VPC endpoints allow you to attach IAM resource policies to interface VPC endpoints to improve the security of your private APIs.")],
 scope="private REST APIs", bullets=B))
fs.append(F("access-control-cors-not-authentication", "behavior",
 "AWS lists cross-origin resource sharing (CORS) under other access-control tasks, not authentication: it lets you control how your REST API responds to cross-domain resource requests.",
 "Is CORS an authentication mechanism?",
 ["how your REST API responds to cross-domain resource requests", "Cross-origin resource sharing (CORS)"],
 [ev(C, INO), ev(C, "Cross-origin resource sharing (CORS) lets you control how your REST API responds to cross-domain resource requests.")],
 scope="REST APIs", bullets=B))
fs.append(F("access-control-client-ssl-certificate-backend", "capability",
 "Client-side SSL certificates can be used to verify that HTTP requests to your backend system are from API Gateway; AWS lists them under other access-control tasks, not authentication.",
 "How can a backend verify that HTTP requests come from API Gateway?",
 ["verify that HTTP requests to your backend system are from API Gateway", "Client-side SSL certificates"],
 [ev(C, INO), ev(C, "Client-side SSL certificates can be used to verify that HTTP requests to your backend system are from API Gateway.")],
 scope="REST APIs", bullets=B, tier0=True))
fs.append(F("access-control-waf-not-authentication", "capability",
 "AWS lists AWS WAF under other access-control tasks, not authentication: it can be used to protect your API Gateway API from common web exploits.",
 "What is AWS WAF used for in API Gateway access control?",
 ["protect your API Gateway API from common web exploits", "AWS WAF"],
 [ev(C, INO), ev(C, "AWS WAF can be used to protect your API Gateway API from common web exploits.")],
 scope="REST APIs", bullets=B))
fs.append(F("access-control-usage-plans-track-limit", "capability",
 "AWS lists usage plans under tracking and limiting access: they let you provide API keys to your customers and then track and limit usage of your API stages and methods for each API key.",
 "Do usage plans and API keys authenticate callers, or do they track and limit usage?",
 ["track and limit usage of your API stages and methods for each API key", "Usage plans"],
 [ev(C, INT), ev(C, "Usage plans let you provide API keys to your customers—and then track and limit usage of your API stages and methods for each API key.")],
 scope="REST APIs", bullets=B+["4.4.S6"], tier0=True))
fs.append(F("resource-policy-definition-and-principals", "capability",
 "API Gateway resource policies are JSON policy documents attached to an API to control whether a specified principal can invoke it; they can allow invocation by users from a specified AWS account, by specified source IP address ranges or CIDR blocks, and by specified VPCs or VPC endpoints in any account.",
 "What can an API Gateway resource policy allow or deny (accounts, IP ranges, VPCs)?",
 ["specified source IP address ranges or CIDR blocks", "VPC endpoints (in any account)"],
 [ev(RP, "Amazon API Gateway resource policies are JSON policy documents that you attach to an API to control whether a specified principal (typically an IAM role or group) can invoke the API. You can use API Gateway resource policies to allow your API to be securely invoked by:"),
  ev(RP, "Users from a specified AWS account."),
  ev(RP, "Specified source IP address ranges or CIDR blocks."),
  ev(RP, "Specified virtual private clouds (VPCs) or VPC endpoints (in any account).")],
 scope="REST APIs", bullets=B, tier0=True))
fs.append(F("resource-policy-any-endpoint-type", "capability",
 "You can attach a resource policy for any API endpoint type in API Gateway by using the AWS Management Console, AWS CLI, or AWS SDKs, and for private APIs you can use resource policies together with VPC endpoint policies.",
 "Which endpoint types can have a resource policy?",
 ["resource policy for any API endpoint type", "together with VPC endpoint policies"],
 [ev(RP, "You can attach a resource policy for any API endpoint type in API Gateway by using the AWS Management Console, AWS CLI, or AWS SDKs. For private APIs, you can use resource policies together with VPC endpoint policies to control which principals have access to which resources and actions.")],
 scope="REST APIs, all endpoint types", bullets=B))
fs.append(F("resource-policy-vs-iam-identity-policy", "behavior",
 "API Gateway resource policies are attached to resources, unlike IAM identity-based policies, which are attached to IAM users, groups, or roles; you can use resource policies together with IAM policies.",
 "How do API Gateway resource policies differ from IAM identity-based policies?",
 ["attached to resources", "together with IAM policies"],
 [ev(RP, "API Gateway resource policies are different from IAM identity-based policies. IAM identity-based policies are attached to IAM users, groups, or roles and define what actions those identities are capable of doing on which resources. API Gateway resource policies are attached to resources. You can use API Gateway resource policies together with IAM policies.")],
 scope="REST APIs", bullets=B))
fs.append(F("private-api-needs-resource-policy", "restriction",
 "A private API needs a resource policy, but you do not need to create a custom VPC endpoint policy; the resource policy specifies which principals can access the API, and the endpoint policy specifies who can access the VPC and which APIs can be called from the VPC endpoint.",
 "Is a resource policy required for a private API?",
 ["Your private API needs a resource policy", "don't need to create a custom VPC endpoint policy"],
 [ev("apigateway-vpc-endpoint-policies", "VPC endpoint policies can be used together with API Gateway resource policies. The API Gateway resource policy specifies which principals can access the API. The endpoint policy specifies who can access the VPC and which APIs can be called from the VPC endpoint. Your private API needs a resource policy but you don't need to create a custom VPC endpoint policy.")],
 scope="private REST APIs", bullets=B, tier0=True))
fs.append(F("auth-flow-resource-policy-only", "behavior",
 "When a resource policy is attached and no authentication type is defined, API Gateway looks for an explicit allow based on the caller's inbound criteria, and an implicit denial or any explicit denial denies the caller.",
 "How is a resource policy evaluated when no other authentication type is defined?",
 ["seeking an explicit allow", "An implicit denial or any explicit denial results in denying the caller"],
 [ev(AF, "In this workflow, an API Gateway resource policy is attached to the API, but no authentication type is defined for the API. Evaluation of the policy involves seeking an explicit allow based on the inbound criteria of the caller. An implicit denial or any explicit denial results in denying the caller.")],
 scope="REST APIs, resource policy only", bullets=B, hard=True))
fs.append(F("auth-flow-lambda-authorizer-two-phase", "behavior",
 "With a Lambda authorizer and a resource policy, the resource policy is evaluated in two phases: API Gateway first checks it for explicit denials before calling the authorizer and denies immediately if one is found, then evaluates the authorizer's returned policy document together with the resource policy.",
 "How is a resource policy evaluated together with a Lambda authorizer?",
 ["evaluated in two phases", "checks for any explicit denials"],
 [ev(AF, "The resource policy is evaluated in two phases. Before calling the Lambda authorizer, API Gateway first evaluates the policy and checks for any explicit denials. If found, the caller is denied access immediately. Otherwise, the Lambda authorizer is called, and it returns a policy document, which is evaluated in conjunction with the resource policy. If your authorizer uses caching, API Gateway might return the cached policy document.")],
 scope="REST APIs, Lambda authorizer with resource policy", bullets=B, tier0=True, hard=True))
fs.append(F("auth-flow-iam-cross-account-both-allow", "behavior",
 "With IAM authentication and a resource policy, if the caller and API owner are in separate accounts, both the IAM policies and the resource policy must explicitly allow the caller to proceed.",
 "What must allow a cross-account caller when IAM authentication and a resource policy are both used?",
 ["both the IAM policies and the resource policy explicitly allow the caller", "separate accounts"],
 [ev(AF, "If the caller and API owner are from separate accounts, both the IAM policies and the resource policy explicitly allow the caller to proceed.")],
 scope="REST APIs, cross-account callers", bullets=B, tier0=True, hard=True))
fs.append(F("auth-flow-iam-same-account-either-allow", "behavior",
 "With IAM authentication and a resource policy, if the caller and the API owner are in the same AWS account, either the IAM user policies or the resource policy must explicitly allow the caller to proceed.",
 "What must allow a same-account caller when IAM authentication and a resource policy are both used?",
 ["either the IAM user policies or the resource policy", "same AWS account"],
 [ev(AF, "However, if the caller and the API owner are in the same AWS account, then either the IAM user policies or the resource policy must explicitly allow the caller to proceed.")],
 scope="REST APIs, same-account callers", bullets=B, tier0=True, hard=True))
fs.append(F("auth-flow-cognito-explicit-allow-required", "behavior",
 "With an Amazon Cognito authorizer and a resource policy, API Gateway first authenticates the caller through Cognito, and if that succeeds the resource policy is evaluated independently and an explicit allow is required; a deny or neither allow nor deny results in a deny.",
 "How is a resource policy evaluated after Cognito authentication succeeds?",
 ["an explicit allow is required", "resource policy is evaluated independently"],
 [ev(AF, "API Gateway first attempts to authenticate the caller through Amazon Cognito. This is typically performed through a JWT token that is provided by the caller. If authentication is successful, the resource policy is evaluated independently, and an explicit allow is required. A deny or \"neither allow or deny\" results in a deny.")],
 scope="REST APIs, Cognito authorizer with resource policy", bullets=B, hard=True))
fs.append(F("auth-flow-cross-account-silent-denied", "behavior",
 "If either the IAM policy (or Cognito user pools authorizer) or the resource policy is silent (neither allow nor deny) for a cross-account call, access is denied, because cross-account access requires that both explicitly grant access.",
 "Does a cross-account call succeed when only one of the IAM policy and the resource policy allows it?",
 ["cross-account access is denied", "requires that both the resource policy and the IAM policy"],
 [ev(AF, "If either is silent (neither allow nor deny), cross-account access is denied. This is because cross-account access requires that both the resource policy and the IAM policy or Amazon Cognito user pools authorizer explicitly grant access.")],
 scope="REST APIs, cross-account callers", bullets=B, hard=True))
fs.append(F("auth-flow-same-account-resource-policy-allow-suffices", "behavior",
 "In the same account, a resource policy Allow is enough when the IAM policy (or Lambda authorizer) is neither Allow nor Deny: the resulting behavior is Allow.",
 "In the same account, what happens when the IAM policy is silent and the resource policy allows?",
 ["Neither Allow nor Deny", "Allow"],
 [ev(AF, "Table A lists the resulting behavior when access to an API Gateway API is controlled by an IAM policy or a Lambda authorizer and an API Gateway resource policy, both of which are in the same AWS account."),
  T(AF, "| Neither Allow nor Deny | Allow | Allow |", "| **IAM policy (or Lambda authorizer)** | **API Gateway resource policy** | **Resulting behavior** |")],
 scope="REST APIs, same account", bullets=B, hard=True))
fs.append(F("auth-flow-cross-account-silent-iam-allow-rp-implicit-deny", "behavior",
 "In different accounts, an IAM policy (or Cognito authorizer) Allow with a resource policy that is neither Allow nor Deny gives an Implicit Deny.",
 "In different accounts, what happens when the IAM policy allows but the resource policy is silent?",
 ["Implicit Deny", "Neither Allow nor Deny"],
 [ev(AF, "Table B lists the resulting behavior when access to an API Gateway API is controlled by an IAM policy or a Amazon Cognito user pools authorizer and an API Gateway resource policy, which are in different AWS accounts. If either is silent (neither allow nor deny), cross-account access is denied."),
  T(AF, "| Allow | Neither Allow nor Deny | Implicit Deny |", "| **IAM policy (or Amazon Cognito user pools authorizer)** | **API Gateway resource policy** | **Resulting behavior** |")],
 scope="REST APIs, different accounts", bullets=B, hard=True))
fs.append(F("auth-flow-explicit-deny-wins", "behavior",
 "An explicit Deny in the resource policy overrides an Allow from the IAM policy or Lambda authorizer in the same account: the resulting behavior is Explicit Deny.",
 "Does an explicit deny in a resource policy override an IAM allow?",
 ["Explicit Deny", "Allow | Deny"],
 [ev(AF, "Table A lists the resulting behavior when access to an API Gateway API is controlled by an IAM policy or a Lambda authorizer and an API Gateway resource policy, both of which are in the same AWS account."),
  T(AF, "| Allow | Deny | Explicit Deny |", "| **IAM policy (or Lambda authorizer)** | **API Gateway resource policy** | **Resulting behavior** |")],
 scope="REST APIs, same account", bullets=B, hard=True))
fs.append(F("waf-evaluated-before-other-access-controls", "behavior",
 "When AWS WAF is enabled on an API, WAF rules are evaluated before other access control features such as resource policies, IAM policies, Lambda authorizers and Cognito authorizers; if WAF blocks a CIDR block that a resource policy allows, WAF takes precedence and the resource policy is not evaluated.",
 "Is AWS WAF evaluated before or after resource policies and authorizers?",
 ["AWS WAF rules are evaluated before other access control features", "AWS WAF takes precedence"],
 [ev("apigateway-control-access-aws-waf", "AWS WAF is your first line of defense against web exploits. When AWS WAF is enabled on an API, AWS WAF rules are evaluated before other access control features, such as resource policies, IAM policies, Lambda authorizers, and Amazon Cognito authorizers. For example, if AWS WAF blocks access from a CIDR block that a resource policy allows, AWS WAF takes precedence and the resource policy isn't evaluated.")],
 scope="REST APIs with AWS WAF", bullets=B, tier0=True, hard=True))
write("facts-behavior-05.json", fs)
