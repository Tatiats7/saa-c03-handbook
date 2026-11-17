facts card: 437 facts
elb-access-logs-off-by-default-s3
  claim: Access logs are an optional feature that is disabled by default; once enabled, Elastic Load Balancing stores them as compressed files in the S3 bucket you specify, and you pay S3 storage but not the bandwidth for delivering the logs.
  scope: Application Load Balancer access logs; default; adjustable.
  link: [disabled by default](../facts/elb.md#elb-access-logs-off-by-default-s3)
  link: [stores them in the Amazon S3 bucket](../facts/elb.md#elb-access-logs-off-by-default-s3)
  link: [not charged for the bandwidth](../facts/elb.md#elb-access-logs-off-by-default-s3)
elb-access-logs-sse-s3-encrypted
  claim: If the S3 bucket for Elastic Load Balancing access logs uses SSE-S3, Elastic Load Balancing encrypts each access log file before it stores it in the bucket and decrypts the files when you access them.
  scope: access logs in S3; SSE-S3 enabled on the bucket.
  link: [Amazon S3-managed encryption keys (SSE-S3)](../facts/elb.md#elb-access-logs-sse-s3-encrypted)
  link: [automatically encrypts each access log file](../facts/elb.md#elb-access-logs-sse-s3-encrypted)
elb-alb-502-bad-target-response
  claim: Under the troubleshooting heading for the ALB 'Bad gateway' error, a listed possible cause is a TCP RST from the target when the load balancer tries to open a connection.
  scope: Application Load Balancer HTTP 502.
  link: [received a TCP RST from the target](../facts/elb.md#elb-alb-502-bad-target-response)
  link: [when attempting to establish a connection](../facts/elb.md#elb-alb-502-bad-target-response)
elb-alb-503-no-registered-targets
  claim: Under the troubleshooting heading for the ALB 'Service unavailable' error, a listed possible cause is that the target groups have no registered targets, or all registered targets are in the unused state.
  scope: Application Load Balancer HTTP 503.
  link: [have no registered targets](../facts/elb.md#elb-alb-503-no-registered-targets)
  link: [in an `unused` state](../facts/elb.md#elb-alb-503-no-registered-targets)
elb-alb-504-nacl-ephemeral-ports
  claim: Under the troubleshooting heading for the ALB 'Gateway timeout' error, a listed possible cause is a network ACL that does not allow traffic from the targets to the load balancer nodes on the ephemeral ports (1024-65535).
  scope: Application Load Balancer HTTP 504.
  link: [The network ACL for the subnet](../facts/elb.md#elb-alb-504-nacl-ephemeral-ports)
  link: [ephemeral ports (1024-65535)](../facts/elb.md#elb-alb-504-nacl-ephemeral-ports)
elb-alb-504-target-no-response-idle-timeout
  claim: Under the troubleshooting heading for the ALB 'Gateway timeout' error, a listed possible cause is a target that accepted the connection but did not respond before the idle timeout elapsed.
  scope: Application Load Balancer HTTP 504.
  link: [before the idle timeout period elapsed](../facts/elb.md#elb-alb-504-target-no-response-idle-timeout)
  link: [established a connection to the target](../facts/elb.md#elb-alb-504-target-no-response-idle-timeout)
elb-alb-access-logs-every-5-minutes
  claim: Elastic Load Balancing publishes an access log file for each load balancer node every 5 minutes.
  scope: per load balancer node.
  link: [every 5 minutes](../facts/elb.md#elb-alb-access-logs-every-5-minutes)
  link: [for each load balancer node](../facts/elb.md#elb-alb-access-logs-every-5-minutes)
  say: every five minutes | for each load balancer node
elb-alb-acm-certs-renew-automatically
  claim: Certificates provided by ACM and deployed on the load balancer can be renewed automatically; for a certificate that you imported into ACM, you must monitor the expiration date and renew it before it expires.
  scope: Application Load Balancer listener certificates; automatic renewal applies to ACM-provided certificates; imported certificates are renewed by you.
  link: [can be renewed automatically](../facts/elb.md#elb-alb-acm-certs-renew-automatically)
  link: [you must monitor the expiration date](../facts/elb.md#elb-alb-acm-certs-renew-automatically)
elb-alb-action-types-list
  claim: ALB listener rule action types include forward (requests to the specified target groups), redirect (from one URL to another), fixed-response (a custom HTTP response) and jwt-validation (validate JWT access tokens); an HTTPS listener can have a rule with a user authentication action and a routing action.
  scope: Application Load Balancer listener rules.
  link: [Forward requests to the specified target groups](../facts/elb.md#elb-alb-action-types-list)
  link: [Redirect requests from one URL to another](../facts/elb.md#elb-alb-action-types-list)
  link: [a user authentication action and a routing action](../facts/elb.md#elb-alb-action-types-list)
elb-alb-adds-x-forwarded-headers
  claim: Application Load Balancers automatically add the X-Forwarded-For, X-Forwarded-Proto and X-Forwarded-Port headers to the request.
  scope: Application Load Balancer.
  link: [X-Forwarded-For](../facts/elb.md#elb-alb-adds-x-forwarded-headers)
  link: [X-Forwarded-Proto](../facts/elb.md#elb-alb-adds-x-forwarded-headers)
  link: [X-Forwarded-Port](../facts/elb.md#elb-alb-adds-x-forwarded-headers)
elb-alb-app-cookie-awsalbapp
  claim: With application-based stickiness the target sets a custom application cookie, and the load balancer generates its own encrypted application cookie whose name, as the client sees it, begins with AWSALBAPP-.
  scope: Application Load Balancer application-based stickiness.
  link: [set a custom application cookie](../facts/elb.md#elb-alb-app-cookie-awsalbapp)
  link: [begins with “AWSALBAPP-"](../facts/elb.md#elb-alb-app-cookie-awsalbapp)
elb-alb-app-cookie-duration-default-1-day
  claim: The application-based stickiness cookie expiration period of an Application Load Balancer is 1 day (86400 seconds) by default and can be set from 1 second to 7 days (604800 seconds).
  scope: per Application Load Balancer target group; default; adjustable.
  link: [1 day](../facts/elb.md#elb-alb-app-cookie-duration-default-1-day)
  link: [86400 seconds](../facts/elb.md#elb-alb-app-cookie-duration-default-1-day)
  link: [1 second](../facts/elb.md#elb-alb-app-cookie-duration-default-1-day)
  link: [7 days](../facts/elb.md#elb-alb-app-cookie-duration-default-1-day)
  say: one day | eighty-six thousand four hundred seconds | one second | seven days
elb-alb-atw-anomaly-mitigation-weighted-random
  claim: Automatic Target Weights (ATW) detects anomalous targets on every Application Load Balancer, but its anomaly mitigation, which routes less traffic to anomalous targets, is only available with the weighted random routing algorithm.
  scope: Application Load Balancer target groups.
  link: [anomaly mitigation function of ATW](../facts/elb.md#elb-alb-atw-anomaly-mitigation-weighted-random)
  link: [reducing the amount of traffic they're routed](../facts/elb.md#elb-alb-atw-anomaly-mitigation-weighted-random)
elb-alb-auth-complete-within-15-minutes
  claim: A client must start and complete Application Load Balancer authentication within 15 minutes or it receives an HTTP 401 error; this timeout can't be changed or removed.
  scope: per authentication attempt; fixed.
  link: [within 15 minutes](../facts/elb.md#elb-alb-auth-complete-within-15-minutes)
  link: [This timeout can't be changed or removed](../facts/elb.md#elb-alb-auth-complete-within-15-minutes)
  say: within fifteen minutes | this timeout can't be changed
elb-alb-auth-session-timeout-default-7-days
  claim: For Application Load Balancer user authentication, the SessionTimeout is 7 days by default and can be set as short as 1 second.
  scope: per authenticate action; default; adjustable.
  link: [7 days](../facts/elb.md#elb-alb-auth-session-timeout-default-7-days)
  link: [1 second](../facts/elb.md#elb-alb-auth-session-timeout-default-7-days)
  say: seven days | one second
elb-alb-backend-http11-default-protocol-version
  claim: By default an Application Load Balancer uses HTTP/1.1 on backend connections to targets, and the target group protocol version can send requests to targets with HTTP/2 or gRPC instead.
  scope: Application Load Balancer backend connections; default; adjustable; set per target group protocol version.
  link: [HTTP/1.1 on backend connections](../facts/elb.md#elb-alb-backend-http11-default-protocol-version)
  link: [using HTTP/2 or gRPC](../facts/elb.md#elb-alb-backend-http11-default-protocol-version)
elb-alb-cert-wildcard-or-san-single-cert
  claim: Without additional certificates, you can host multiple secure applications on one load balancer with a wildcard certificate or a certificate with a Subject Alternative Name for each extra domain.
  scope: Application Load Balancer HTTPS listener.
  link: [use a wildcard certificate](../facts/elb.md#elb-alb-cert-wildcard-or-san-single-cert)
  link: [add a Subject Alternative Name (SAN)](../facts/elb.md#elb-alb-cert-wildcard-or-san-single-cert)
elb-alb-client-keepalive-default-3600-seconds
  claim: The HTTP client keepalive duration of an Application Load Balancer is 3600 seconds (1 hour) by default; it cannot be turned off or set below 60 seconds, and it can be raised up to 604800 seconds (7 days).
  scope: per Application Load Balancer; default; adjustable.
  link: [3600 seconds](../facts/elb.md#elb-alb-client-keepalive-default-3600-seconds)
  link: [1 hour](../facts/elb.md#elb-alb-client-keepalive-default-3600-seconds)
  link: [60 seconds](../facts/elb.md#elb-alb-client-keepalive-default-3600-seconds)
  link: [604800 seconds](../facts/elb.md#elb-alb-client-keepalive-default-3600-seconds)
  link: [7 days](../facts/elb.md#elb-alb-client-keepalive-default-3600-seconds)
  say: three thousand six hundred seconds | one hour | sixty seconds | six hundred four thousand eight hundred seconds | seven days
elb-alb-cloudfront-global-reach
  claim: CloudFront acts as a distributed, single point of entry for web applications that use Application Load Balancers and extends the load balancer's reach globally from nearby edge locations.
  scope: Application Load Balancer with CloudFront.
  link: [distributed, single point of entry](../facts/elb.md#elb-alb-cloudfront-global-reach)
  link: [extends your Application Load Balancer's reach globally](../facts/elb.md#elb-alb-cloudfront-global-reach)
elb-alb-cloudfront-prefix-list-sg
  claim: As a security best practice, an internet-facing ALB behind CloudFront should have security groups that allow inbound traffic only from the AWS-managed prefix list for CloudFront, with other inbound rules removed.
  scope: internet-facing Application Load Balancer behind CloudFront.
  link: [AWS-managed prefix list for CloudFront](../facts/elb.md#elb-alb-cloudfront-prefix-list-sg)
  link: [remove any other inbound rules](../facts/elb.md#elb-alb-cloudfront-prefix-list-sg)
elb-alb-condition-types
  claim: ALB listener rules can route on host header, HTTP header, HTTP request method, path pattern, query string and source IP address conditions.
  scope: Application Load Balancer listener rules.
  link: [host-header](../facts/elb.md#elb-alb-condition-types)
  link: [path-pattern](../facts/elb.md#elb-alb-condition-types)
  link: [source-ip](../facts/elb.md#elb-alb-condition-types)
  link: [query-string](../facts/elb.md#elb-alb-condition-types)
elb-alb-connection-multiplexing
  claim: Application Load Balancers use connection multiplexing: requests from multiple clients on multiple front-end connections can reach a target through a single backend connection.
  scope: Application Load Balancer backend connections.
  link: [connection multiplexing](../facts/elb.md#elb-alb-connection-multiplexing)
  link: [through a single backend connection](../facts/elb.md#elb-alb-connection-multiplexing)
elb-alb-cross-zone-no-data-transfer-charge
  claim: Because cross-zone load balancing is always on with an Application Load Balancer, you are not charged for regional data transfer for it.
  scope: Application Load Balancer, cross-zone traffic.
  link: [you are not charged](../facts/elb.md#elb-alb-cross-zone-no-data-transfer-charge)
  link: [always on with Application Load Balancer](../facts/elb.md#elb-alb-cross-zone-no-data-transfer-charge)
  say: you are not charged | always on with Application Load Balancer
elb-alb-cross-zone-off-no-sticky-no-lambda
  claim: When cross-zone load balancing is off for an ALB target group, target stickiness and Lambda function targets are not supported.
  scope: Application Load Balancer target group; cross-zone load balancing off.
  link: [Target stickiness is not supported](../facts/elb.md#elb-alb-cross-zone-off-no-sticky-no-lambda)
  link: [Lambda functions as targets are not supported](../facts/elb.md#elb-alb-cross-zone-off-no-sticky-no-lambda)
elb-alb-cross-zone-on-by-default
  claim: With Application Load Balancers, cross-zone load balancing is on by default and cannot be changed at the load balancer level; it can be turned off at the target group level.
  scope: per Application Load Balancer; default; adjustable.
  link: [on by default](../facts/elb.md#elb-alb-cross-zone-on-by-default)
  link: [cannot be changed at the load balancer level](../facts/elb.md#elb-alb-cross-zone-on-by-default)
  link: [possible at the target group level](../facts/elb.md#elb-alb-cross-zone-on-by-default)
  say: on by default | cannot be changed at the load balancer level | possible at the target group level
elb-alb-default-cert-when-no-sni-match
  claim: When certificates in the certificate list match the client hostname but none of them is compatible with the client, the TLS handshake fails and the load balancer does not fall back to the default certificate.
  scope: Application Load Balancer HTTPS listener.
  link: [the handshake fails](../facts/elb.md#elb-alb-default-cert-when-no-sni-match)
  link: [does not fall back to the default certificate](../facts/elb.md#elb-alb-default-cert-when-no-sni-match)
elb-alb-default-rule-last-no-conditions
  claim: Every ALB listener has a default rule that cannot be deleted, has no conditions, and is performed last, when no other rule's conditions are met.
  scope: Application Load Balancer listener.
  link: [The default rule can't be deleted](../facts/elb.md#elb-alb-default-rule-last-no-conditions)
  link: [is always performed last](../facts/elb.md#elb-alb-default-rule-last-no-conditions)
  link: [The default rule can't have conditions](../facts/elb.md#elb-alb-default-rule-last-no-conditions)
elb-alb-default-sg-preselected
  claim: When you create an Application Load Balancer in the console, the default security group of the load balancer VPC is preselected, and you can select additional security groups.
  scope: Application Load Balancer, console creation; default; adjustable.
  link: [We preselect the default security group](../facts/elb.md#elb-alb-default-sg-preselected)
  link: [select additional security groups as needed](../facts/elb.md#elb-alb-default-sg-preselected)
elb-alb-deregistration-draining-then-unused
  claim: A deregistering target starts in the draining state; after the deregistration delay it becomes unused, and if it belongs to an Auto Scaling group it can then be terminated and replaced.
  scope: Application Load Balancer target deregistration.
  link: [deregistering target is `draining`](../facts/elb.md#elb-alb-deregistration-draining-then-unused)
  link: [the state of the target is `unused`](../facts/elb.md#elb-alb-deregistration-draining-then-unused)
  link: [it can be terminated and replaced](../facts/elb.md#elb-alb-deregistration-draining-then-unused)
elb-alb-deregistration-waits-for-in-flight
  claim: Elastic Load Balancing stops sending requests to a deregistering target and, by default, waits 300 seconds before it completes deregistration so that in-flight requests can finish.
  scope: Application Load Balancer target group; default.
  link: [stops sending requests to targets that are deregistering](../facts/elb.md#elb-alb-deregistration-waits-for-in-flight)
  link: [waits 300 seconds](../facts/elb.md#elb-alb-deregistration-waits-for-in-flight)
  link: [help in-flight requests to the target to complete](../facts/elb.md#elb-alb-deregistration-waits-for-in-flight)
elb-alb-desync-mitigation-defensive-default
  claim: ALB desync mitigation mode protects the application from HTTP desync issues; the modes are monitor, defensive and strictest, and the default is defensive.
  scope: Application Load Balancer attribute; default; adjustable.
  link: [monitor, defensive, and strictest](../facts/elb.md#elb-alb-desync-mitigation-defensive-default)
  link: [The default is the defensive mode](../facts/elb.md#elb-alb-desync-mitigation-defensive-default)
elb-alb-duration-cookie-awsalb
  claim: Duration-based stickiness uses a load balancer generated cookie named AWSALB that maps the session to the target; AWSALB is the only cookie name used across all target groups.
  scope: Application Load Balancer duration-based stickiness.
  link: [`AWSALB`](../facts/elb.md#elb-alb-duration-cookie-awsalb)
  link: [load balancer generated cookie](../facts/elb.md#elb-alb-duration-cookie-awsalb)
elb-alb-empty-subnet-503
  claim: Avoid empty subnets on an Application Load Balancer: it still exposes zonal IP addresses through DNS for empty subnets, which causes 503 errors for HTTP requests.
  scope: Application Load Balancer subnets.
  link: [Avoid creating empty subnets](../facts/elb.md#elb-alb-empty-subnet-503)
  link: [triggers 503 errors for HTTP requests](../facts/elb.md#elb-alb-empty-subnet-503)
elb-alb-fail-open-all-unhealthy
  claim: If an ALB target group contains only unhealthy targets, the load balancer routes requests to all of them regardless of health: when all targets fail health checks at once in all enabled Availability Zones, the load balancer fails open.
  scope: Application Load Balancer target group; all registered targets unhealthy.
  link: [routes requests to all those targets](../facts/elb.md#elb-alb-fail-open-all-unhealthy)
  link: [the load balancer fails open](../facts/elb.md#elb-alb-fail-open-all-unhealthy)
elb-alb-faq-authentication-no-separate-charge
  claim: Enabling user authentication on an Application Load Balancer has no separate charge; when you use Amazon Cognito with it, Amazon Cognito pricing applies.
  scope: Application Load Balancer authenticate action.
  link: [There is no separate charge](../facts/elb.md#elb-alb-faq-authentication-no-separate-charge)
  link: [Amazon Cognito pricing will apply](../facts/elb.md#elb-alb-faq-authentication-no-separate-charge)
elb-alb-faq-cloudtrail-api-history
  claim: AWS CloudTrail gives you a history of the Application Load Balancing API calls made on your account.
  scope: Application Load Balancer API.
  link: [use AWS CloudTrail](../facts/elb.md#elb-alb-faq-cloudtrail-api-history)
  link: [a history of Application Load Balancing API calls](../facts/elb.md#elb-alb-faq-cloudtrail-api-history)
elb-alb-faq-cognito-vs-native-oidc
  claim: Use Application Load Balancer authentication through Amazon Cognito for social identities (Google, Facebook, Amazon), enterprise identities (SAML) or Cognito user pools, or to federate several identity providers in one rule; use the native OIDC support to authenticate with a single OpenID Connect-compatible identity provider.
  scope: Application Load Balancer authenticate action.
  link: [social network identities (Google, Facebook, and Amazon)](../facts/elb.md#elb-alb-faq-cognito-vs-native-oidc)
  link: [enterprise identities (SAML)](../facts/elb.md#elb-alb-faq-cognito-vs-native-oidc)
  link: [a single OpenID Connect-compatible identity provider](../facts/elb.md#elb-alb-faq-cognito-vs-native-oidc)
elb-alb-faq-fixed-response-content-types
  claim: The fixed-response action of an Application Load Balancer supports the content types text/plain, text/css, text/html, application/javascript and application/json.
  scope: Application Load Balancer fixed-response action.
  link: [text/plain, text/css, text/html](../facts/elb.md#elb-alb-faq-fixed-response-content-types)
  link: [application/json](../facts/elb.md#elb-alb-faq-fixed-response-content-types)
elb-alb-faq-http-and-https-one-alb
  claim: A single Application Load Balancer can handle HTTP and HTTPS requests, with listeners for HTTP port 80 and HTTPS port 443.
  scope: Application Load Balancer.
  link: [HTTP port 80](../facts/elb.md#elb-alb-faq-http-and-https-one-alb)
  link: [HTTPS port 443](../facts/elb.md#elb-alb-faq-http-and-https-one-alb)
  link: [to a single Application Load Balancer](../facts/elb.md#elb-alb-faq-http-and-https-one-alb)
elb-alb-faq-http2-native
  claim: HTTP/2 support is enabled natively on an Application Load Balancer, and clients that support HTTP/2 connect to it over TLS.
  scope: Application Load Balancer.
  link: [HTTP/2 support is enabled natively](../facts/elb.md#elb-alb-faq-http2-native)
  link: [connect to an Application Load Balancer over TLS](../facts/elb.md#elb-alb-faq-http2-native)
elb-alb-faq-hybrid-same-target-group-migrate
  claim: An application whose targets are spread between a VPC and an on-premises location can have all of them in the same target group by IP address; to migrate without impact, you gradually add VPC targets and remove on-premises targets.
  scope: Application Load Balancer IP targets.
  link: [the same target group using their IP addresses](../facts/elb.md#elb-alb-faq-hybrid-same-target-group-migrate)
  link: [gradually add VPC targets to the target group](../facts/elb.md#elb-alb-faq-hybrid-same-target-group-migrate)
elb-alb-faq-hybrid-separate-target-groups-or-dns
  claim: For two applications, one with targets in a VPC and one on premises, you can use two target groups with content-based routing, or separate load balancers with DNS weighting.
  scope: Application Load Balancer.
  link: [use content based routing](../facts/elb.md#elb-alb-faq-hybrid-separate-target-groups-or-dns)
  link: [use DNS weighting](../facts/elb.md#elb-alb-faq-hybrid-separate-target-groups-or-dns)
elb-alb-faq-ip-target-ranges
  claim: IP targets of a load balancer can use any IP address from the load balancer's VPC CIDR inside its VPC, and any address from the RFC 1918 ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) or the RFC 6598 range (100.64.0.0/10) for targets outside that VPC, such as a peered VPC or on-premises locations reached over AWS Direct Connect or VPN.
  scope: Application Load Balancer IP targets.
  link: [IP address from the load balancer’s VPC CIDR](../facts/elb.md#elb-alb-faq-ip-target-ranges)
  link: [RFC 1918 ranges](../facts/elb.md#elb-alb-faq-ip-target-ranges)
  link: [RFC 6598 range (100.64.0.0/10)](../facts/elb.md#elb-alb-faq-ip-target-ranges)
  link: [reachable over AWS Direct Connect or VPN connection](../facts/elb.md#elb-alb-faq-ip-target-ranges)
elb-alb-faq-ipv6-supported
  claim: IPv6 is supported with an Application Load Balancer.
  scope: Application Load Balancer.
  link: [IPv6 is supported](../facts/elb.md#elb-alb-faq-ipv6-supported)
  link: [with an Application Load Balancer](../facts/elb.md#elb-alb-faq-ipv6-supported)
elb-alb-faq-lambda-bytes-metrics
  claim: Application Load Balancers report bytes processed by Lambda targets in the LambdaTargetProcessedBytes CloudWatch metric and bytes for all other targets in StandardProcessedBytes.
  scope: Application Load Balancer.
  link: [LambdaTargetProcessedBytes](../facts/elb.md#elb-alb-faq-lambda-bytes-metrics)
  link: [StandardProcessedBytes](../facts/elb.md#elb-alb-faq-lambda-bytes-metrics)
elb-alb-faq-lambda-http-and-https
  claim: An Application Load Balancer supports Lambda invocation for requests over both HTTP and HTTPS.
  scope: Application Load Balancer Lambda targets.
  link: [both HTTP and HTTPS protocol](../facts/elb.md#elb-alb-faq-lambda-http-and-https)
  link: [supports Lambda invocation](../facts/elb.md#elb-alb-faq-lambda-http-and-https)
elb-alb-faq-lcu-four-dimensions-max
  claim: For an Application Load Balancer, the LCUs per hour are set by the maximum resource consumed among four dimensions: new connections, active connections, bandwidth and rule evaluations; you are not billed on all four.
  scope: Application Load Balancer.
  link: [new connections, active connections, bandwidth and rule evaluations](../facts/elb.md#elb-alb-faq-lcu-four-dimensions-max)
  link: [maximum resource consumed amongst the four dimensions](../facts/elb.md#elb-alb-faq-lcu-four-dimensions-max)
elb-alb-faq-lcu-key-size-new-connections
  claim: Certificate key size affects only the new-connections-per-second dimension of the Application Load Balancer LCU.
  scope: Application Load Balancer LCU.
  link: [affects only the number of new connections](../facts/elb.md#elb-alb-faq-lcu-key-size-new-connections)
  link: [Certificate key size](../facts/elb.md#elb-alb-faq-lcu-key-size-new-connections)
elb-alb-faq-lcu-usage-in-cloudwatch
  claim: Application Load Balancer usage of all four LCU dimensions is exposed through Amazon CloudWatch.
  scope: Application Load Balancer.
  link: [via Amazon CloudWatch](../facts/elb.md#elb-alb-faq-lcu-usage-in-cloudwatch)
  link: [all four dimensions that constitute an LCU](../facts/elb.md#elb-alb-faq-lcu-usage-in-cloudwatch)
elb-alb-faq-multiple-certificates-same-domain
  claim: A secure listener can have multiple certificates for the same domain.
  scope: Application Load Balancer secure listener.
  link: [multiple certificates for the same domain](../facts/elb.md#elb-alb-faq-multiple-certificates-same-domain)
  link: [to a secure listener](../facts/elb.md#elb-alb-faq-multiple-certificates-same-domain)
elb-alb-faq-no-backend-server-authentication
  claim: An Application Load Balancer does not support back-end server authentication; only encryption to the back ends is supported.
  scope: Application Load Balancer.
  link: [only encryption is supported to the back-ends](../facts/elb.md#elb-alb-faq-no-backend-server-authentication)
elb-alb-faq-not-layer-4
  claim: An Application Load Balancer is not used as a Layer-4 load balancer; if you need Layer-4 features, use a Network Load Balancer.
  scope: Application Load Balancer.
  link: [you should use Network Load Balancer](../facts/elb.md#elb-alb-faq-not-layer-4)
  link: [If you need Layer-4 features](../facts/elb.md#elb-alb-faq-not-layer-4)
elb-alb-faq-request-tracing-default
  claim: Request tracing is enabled by default on an Application Load Balancer.
  scope: Application Load Balancer; default; not adjustable.
  link: [Request tracing](../facts/elb.md#elb-alb-faq-request-tracing-default)
  link: [enabled by default](../facts/elb.md#elb-alb-faq-request-tracing-default)
elb-alb-faq-rule-evaluations-defined
  claim: Rule evaluations (an ALB LCU dimension) are the number of rules processed multiplied by the request rate averaged over an hour.
  scope: Application Load Balancer LCU.
  link: [number of rules processed and the request rate](../facts/elb.md#elb-alb-faq-rule-evaluations-defined)
  link: [averaged over an hour](../facts/elb.md#elb-alb-faq-rule-evaluations-defined)
elb-alb-faq-websockets-native
  claim: WebSockets and Secure WebSockets are supported natively on an Application Load Balancer.
  scope: Application Load Balancer.
  link: [WebSockets and Secure WebSockets support](../facts/elb.md#elb-alb-faq-websockets-native)
  link: [available natively and ready for use](../facts/elb.md#elb-alb-faq-websockets-native)
elb-alb-fixed-response-action
  claim: A fixed-response action drops the client request and returns a custom HTTP response with a 2XX, 4XX or 5XX code and an optional message.
  scope: Application Load Balancer fixed-response action.
  link: [returns a custom HTTP response](../facts/elb.md#elb-alb-fixed-response-action)
  link: [2XX, 4XX, or 5XX response code](../facts/elb.md#elb-alb-fixed-response-action)
elb-alb-generated-cookie-7-day-expiry
  claim: The cookie that an Application Load Balancer generates for stickiness has its own expiry of 7 days, which cannot be configured.
  scope: per load balancer generated stickiness cookie; fixed.
  link: [7 days](../facts/elb.md#elb-alb-generated-cookie-7-day-expiry)
  link: [which is non-configurable](../facts/elb.md#elb-alb-generated-cookie-7-day-expiry)
  say: seven days | which is non-configurable
elb-alb-global-accelerator-static-ips
  claim: An accelerator for a load balancer directs traffic over the AWS global network to static IP addresses that serve as fixed endpoints in the Region nearest the client, and AWS Global Accelerator is protected by Shield Standard.
  scope: load balancer with AWS Global Accelerator.
  link: [static IP addresses that serve as fixed endpoints](../facts/elb.md#elb-alb-global-accelerator-static-ips)
  link: [protected by Shield Standard](../facts/elb.md#elb-alb-global-accelerator-static-ips)
elb-alb-grpc-http2-https-forward-only
  claim: With the gRPC protocol version on an Application Load Balancer target group, the only supported listener protocol is HTTPS, the only supported action type for listener rules is forward, and the only supported target types are instance and ip; with the gRPC or HTTP/2 protocol version, the only supported actions are forward actions.
  scope: Application Load Balancer target group with protocol version gRPC (forward-only also for HTTP/2).
  link: [The only supported listener protocol is HTTPS](../facts/elb.md#elb-alb-grpc-http2-https-forward-only)
  link: [only supported action type for listener rules](../facts/elb.md#elb-alb-grpc-http2-https-forward-only)
elb-alb-header-modification-no-code-change
  claim: An Application Load Balancer can modify HTTP request and response headers without changes to the application code.
  scope: Application Load Balancer.
  link: [for both request and response headers](../facts/elb.md#elb-alb-header-modification-no-code-change)
  link: [Without having to update your application code](../facts/elb.md#elb-alb-header-modification-no-code-change)
elb-alb-health-check-interval-default-30-seconds
  claim: The Application Load Balancer health check interval can be 5 to 300 seconds; the default is 30 seconds for instance or ip targets and 35 seconds for lambda targets.
  scope: per Application Load Balancer target group; default; adjustable.
  link: [30 seconds](../facts/elb.md#elb-alb-health-check-interval-default-30-seconds)
  link: [35 seconds](../facts/elb.md#elb-alb-health-check-interval-default-30-seconds)
  link: [5 to 300 seconds](../facts/elb.md#elb-alb-health-check-interval-default-30-seconds)
  say: thirty seconds | thirty-five seconds | five to three hundred seconds
elb-alb-health-check-logs-optional-off
  claim: The legacy Application Load Balancer health check logs, which record target health check status and failure reasons, are an optional feature that is disabled by default; when enabled, they are stored as compressed files in an Amazon S3 bucket you specify, and you pay S3 storage but not the bandwidth used to send the log files. The Application Load Balancer now also offers logging through CloudWatch Logs, with delivery to Amazon CloudWatch Logs, Amazon Data Firehose or Amazon S3.
  scope: Application Load Balancer health check logs (legacy S3 delivery); default; not adjustable; the CloudWatch Logs delivery options are configured on the load balancer's Integrations tab.
  link: [disabled by default](../facts/elb.md#elb-alb-health-check-logs-optional-off)
  link: [the Amazon S3 bucket that you specify](../facts/elb.md#elb-alb-health-check-logs-optional-off)
elb-alb-health-check-path-default-slash
  claim: The default Application Load Balancer health check path is / for HTTP/1.1 or HTTP/2 target groups and /AWS.ALB/healthcheck for gRPC target groups.
  scope: per Application Load Balancer target group; default; adjustable.
  link: [The default is /.](../facts/elb.md#elb-alb-health-check-path-default-slash)
  link: [/AWS.ALB/healthcheck](../facts/elb.md#elb-alb-health-check-path-default-slash)
  say: the default path is slash | slash AWS dot ALB slash healthcheck
elb-alb-health-check-port-default-traffic-port
  claim: By default, an Application Load Balancer health check uses the port on which each target receives traffic from the load balancer.
  scope: per Application Load Balancer target group; default; adjustable.
  link: [port on which each target receives traffic](../facts/elb.md#elb-alb-health-check-port-default-traffic-port)
  link: [The default is to use the port](../facts/elb.md#elb-alb-health-check-port-default-traffic-port)
  say: the traffic port | the default is the traffic port
elb-alb-health-check-protocol-default-http
  claim: Application Load Balancer health checks use HTTP or HTTPS with the HTTP GET method; the default protocol is HTTP.
  scope: per Application Load Balancer target group; default; adjustable.
  link: [The default is the HTTP protocol](../facts/elb.md#elb-alb-health-check-protocol-default-http)
  link: [the possible protocols are HTTP and HTTPS](../facts/elb.md#elb-alb-health-check-protocol-default-http)
  say: the default is HTTP | HTTP and HTTPS
elb-alb-health-check-success-code-default-200
  claim: For HTTP/1.1 or HTTP/2 target groups, Application Load Balancer health check success codes can be from 200 to 499 and the default is 200; for gRPC the codes are 0 to 99 and the default is 12.
  scope: per Application Load Balancer target group; default; adjustable.
  link: [200 to 499](../facts/elb.md#elb-alb-health-check-success-code-default-200)
  link: [The default value is 200](../facts/elb.md#elb-alb-health-check-success-code-default-200)
  link: [The default value is 12](../facts/elb.md#elb-alb-health-check-success-code-default-200)
  say: two hundred to four ninety-nine | the default is two hundred | the default is twelve
elb-alb-health-check-timeout-default-5-seconds
  claim: The Application Load Balancer health check timeout can be 2 to 120 seconds; the default is 5 seconds for instance or ip targets and 30 seconds for lambda targets.
  scope: per Application Load Balancer target group; default; adjustable.
  link: [5 seconds](../facts/elb.md#elb-alb-health-check-timeout-default-5-seconds)
  link: [30 seconds](../facts/elb.md#elb-alb-health-check-timeout-default-5-seconds)
  link: [2 to 120 seconds](../facts/elb.md#elb-alb-health-check-timeout-default-5-seconds)
  say: five seconds | thirty seconds | two to one hundred twenty seconds
elb-alb-health-checks-no-websockets
  claim: ALB health checks do not support WebSockets.
  scope: Application Load Balancer health checks.
  link: [Health checks do not support WebSockets](../facts/elb.md#elb-alb-health-checks-no-websockets)
elb-alb-healthy-threshold-default-5
  claim: An unhealthy Application Load Balancer target must pass 5 consecutive health checks by default before it is healthy again; the range is 2 to 10.
  scope: per Application Load Balancer target group; default; adjustable.
  link: [5 consecutive health checks](../facts/elb.md#elb-alb-healthy-threshold-default-5)
  link: [2 to 10](../facts/elb.md#elb-alb-healthy-threshold-default-5)
  say: five consecutive health checks | two to ten
elb-alb-host-conditions-many-domains-one-lb
  claim: With host conditions, one Application Load Balancer can route requests for multiple domains, based on the host field in the HTTP header.
  scope: Application Load Balancer listener rules.
  link: [route requests to multiple domains](../facts/elb.md#elb-alb-host-conditions-many-domains-one-lb)
  link: [using a single load balancer](../facts/elb.md#elb-alb-host-conditions-many-domains-one-lb)
elb-alb-http2-only-https-listeners
  claim: On an Application Load Balancer, HTTP/2 from clients works only with HTTPS listeners.
  scope: Application Load Balancer front-end connections.
  link: [HTTP/2 only with HTTPS listeners](../facts/elb.md#elb-alb-http2-only-https-listeners)
elb-alb-https-decrypt-at-target-use-nlb-tcp
  claim: If the targets, not the load balancer, must decrypt HTTPS traffic, use a Network Load Balancer with a TCP listener on port 443, which passes the encrypted traffic through to the targets without decrypting it.
  scope: end-to-end encryption to targets.
  link: [a Network Load Balancer with a TCP listener on port 443](../facts/elb.md#elb-alb-https-decrypt-at-target-use-nlb-tcp)
  link: [passes encrypted traffic through to the targets](../facts/elb.md#elb-alb-https-decrypt-at-target-use-nlb-tcp)
elb-alb-https-default-security-policy
  claim: An HTTPS listener requires a security policy; if you do not specify one, the default is ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09 in the console and ELBSecurityPolicy-2016-08 with other methods such as the AWS CLI or CloudFormation.
  scope: Application Load Balancer HTTPS listener; default; adjustable; no security policy specified.
  link: [An HTTPS listener requires a security policy](../facts/elb.md#elb-alb-https-default-security-policy)
  link: [ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09](../facts/elb.md#elb-alb-https-default-security-policy)
  link: [ELBSecurityPolicy-2016-08](../facts/elb.md#elb-alb-https-default-security-policy)
elb-alb-https-listener-terminates-and-decrypts
  claim: An HTTPS listener needs at least one SSL server certificate, which the load balancer uses to terminate the front-end connection and decrypt client requests before sending them to targets; you also specify a security policy for negotiating secure connections.
  scope: Application Load Balancer HTTPS listener.
  link: [terminate the front-end connection](../facts/elb.md#elb-alb-https-listener-terminates-and-decrypts)
  link: [specify a security policy and a certificate](../facts/elb.md#elb-alb-https-listener-terminates-and-decrypts)
elb-alb-idle-timeout-default-60-seconds
  claim: The connection idle timeout of an Application Load Balancer is 60 seconds by default; the valid range is 1 through 4000 seconds.
  scope: per Application Load Balancer; default; adjustable.
  link: [60 seconds](../facts/elb.md#elb-alb-idle-timeout-default-60-seconds)
  link: [1 through 4000 seconds](../facts/elb.md#elb-alb-idle-timeout-default-60-seconds)
  say: sixty seconds | one through four thousand seconds
elb-alb-ips-not-counted-in-eip-limits
  claim: Public IPv4 addresses allocated by an Application Load Balancer do not count against the account's Elastic IP address limits.
  scope: per account.
  link: [do not count against your account's EIP limits](../facts/elb.md#elb-alb-ips-not-counted-in-eip-limits)
  link: [IPs allocated by Application Load Balancer](../facts/elb.md#elb-alb-ips-not-counted-in-eip-limits)
  say: do not count against your EIP limits | IPs allocated by Application Load Balancer
elb-alb-jwt-verification-m2m
  claim: An Application Load Balancer can verify JSON Web Tokens (JWT) that clients send for service-to-service or machine-to-machine communication, and rejects the request when the token is not valid.
  scope: Application Load Balancer listener.
  link: [verify JSON Web Tokens (JWT)](../facts/elb.md#elb-alb-jwt-verification-m2m)
  link: [machine-to-machine (M2M) communications](../facts/elb.md#elb-alb-jwt-verification-m2m)
  link: [Otherwise, it rejects the request.](../facts/elb.md#elb-alb-jwt-verification-m2m)
elb-alb-lambda-console-adds-permission
  claim: If you create the target group and register a Lambda function as a target in the console, the console adds the required permissions to the Lambda function policy; if you register it with the AWS CLI, you must use the add-permission command to grant Elastic Load Balancing permission to invoke the function.
  scope: Application Load Balancer Lambda target.
  link: [the console adds the required permissions](../facts/elb.md#elb-alb-lambda-console-adds-permission)
  link: [to your Lambda function policy](../facts/elb.md#elb-alb-lambda-console-adds-permission)
elb-alb-lambda-request-as-json
  claim: When an ALB forwards a request to a target group with a Lambda function target, it invokes the function directly (not over a network connection) and passes the request content to it in JSON format.
  scope: Application Load Balancer Lambda target.
  link: [in JSON format](../facts/elb.md#elb-alb-lambda-request-as-json)
  link: [invokes the Lambda function directly](../facts/elb.md#elb-alb-lambda-request-as-json)
elb-alb-lambda-same-account-region
  claim: A Lambda function target and its target group must be in the same account and the same Region, and WebSockets are not supported for Lambda targets.
  scope: Application Load Balancer Lambda target.
  link: [in the same Region](../facts/elb.md#elb-alb-lambda-same-account-region)
  link: [WebSockets are not supported](../facts/elb.md#elb-alb-lambda-same-account-region)
elb-alb-layer-7
  claim: An Application Load Balancer functions at the application layer, the seventh layer of the OSI model, and evaluates listener rules in priority order to choose a target group.
  scope: Application Load Balancer.
  link: [the seventh layer of the Open Systems Interconnection](../facts/elb.md#elb-alb-layer-7)
  link: [functions at the application layer](../facts/elb.md#elb-alb-layer-7)
  say: layer seven of the OSI model | functions at the application layer
elb-alb-lb-cookie-duration-default-1-day
  claim: The duration-based stickiness cookie of an Application Load Balancer expires after 1 day (86400 seconds) by default; the duration can be set from 1 second to 7 days (604800 seconds).
  scope: per Application Load Balancer target group; default; adjustable.
  link: [1 day](../facts/elb.md#elb-alb-lb-cookie-duration-default-1-day)
  link: [86400 seconds](../facts/elb.md#elb-alb-lb-cookie-duration-default-1-day)
  link: [1 second](../facts/elb.md#elb-alb-lb-cookie-duration-default-1-day)
  link: [7 days](../facts/elb.md#elb-alb-lb-cookie-duration-default-1-day)
  say: one day | eighty-six thousand four hundred seconds | one second | seven days
elb-alb-lcu-1-gb-per-hour-processed
  claim: One Application Load Balancer LCU includes 1 GB per hour of processed bytes for EC2 instances, containers and IP addresses as targets, and 0.4 GB per hour for Lambda functions as targets.
  scope: per LCU, Application Load Balancer.
  link: [1 GB per hour](../facts/elb.md#elb-alb-lcu-1-gb-per-hour-processed)
  link: [0.4 GB per hour](../facts/elb.md#elb-alb-lcu-1-gb-per-hour-processed)
  say: one gigabyte per hour | zero point four gigabytes per hour
elb-alb-lcu-1000-rule-evaluations-per-second
  claim: One Application Load Balancer LCU includes 1,000 rule evaluations per second.
  scope: per LCU, Application Load Balancer.
  link: [1,000 rule evaluations per second](../facts/elb.md#elb-alb-lcu-1000-rule-evaluations-per-second)
  say: one thousand rule evaluations per second
elb-alb-lcu-25-new-connections-per-second
  claim: One Application Load Balancer LCU includes 25 new connections per second; for HTTPS listeners this figure applies to RSA certificates with a key size of 2K or less and ECDSA certificates with a key size of 256 or less.
  scope: per LCU, Application Load Balancer; HTTPS listeners: RSA key size 2K or less, ECDSA key size 256 or less; larger keys are covered in the pricing FAQs.
  link: [25 new connections per second](../facts/elb.md#elb-alb-lcu-25-new-connections-per-second)
  say: twenty-five new connections per second
elb-alb-lcu-3000-active-connections-per-minute
  claim: One Application Load Balancer LCU includes 3,000 active connections per minute, or 1,500 active connections per minute when Mutual TLS is used.
  scope: per LCU, Application Load Balancer.
  link: [3,000 active connections per minute](../facts/elb.md#elb-alb-lcu-3000-active-connections-per-minute)
  link: [1,500 active connections per minute](../facts/elb.md#elb-alb-lcu-3000-active-connections-per-minute)
  say: three thousand active connections per minute | fifteen hundred active connections per minute
elb-alb-lcu-first-10-rules-free
  claim: For Application Load Balancer LCU billing, the first 10 processed rules are free; with 10 or fewer rules configured, the rule evaluations dimension is ignored.
  scope: per Application Load Balancer.
  link: [first 10 processed rules are free](../facts/elb.md#elb-alb-lcu-first-10-rules-free)
  link: [10 or fewer rules](../facts/elb.md#elb-alb-lcu-first-10-rules-free)
  say: the first ten processed rules are free | ten or fewer rules
elb-alb-lcu-reservation-min-100
  claim: An LCU reservation request for an Application Load Balancer must be at least 100 LCU in total.
  scope: per Application Load Balancer reservation request; minimum; not adjustable.
  link: [at least 100 LCU](../facts/elb.md#elb-alb-lcu-reservation-min-100)
  say: at least one hundred LCUs
elb-alb-least-outstanding-requests-use
  claim: The least outstanding requests algorithm sends requests to the targets with the fewest in-progress requests and suits requests that vary in complexity or targets that vary in processing capability.
  scope: Application Load Balancer target group.
  link: [lowest number of in progress requests](../facts/elb.md#elb-alb-least-outstanding-requests-use)
  link: [vary in complexity](../facts/elb.md#elb-alb-least-outstanding-requests-use)
elb-alb-listener-ports-1-65535
  claim: An Application Load Balancer can load balance on TCP ports 1-65535.
  scope: per listener; maximum; not adjustable.
  link: [1-65535](../facts/elb.md#elb-alb-listener-ports-1-65535)
  say: one to sixty-five thousand five hundred thirty-five
elb-alb-listener-protocols-http-https
  claim: Application Load Balancer listeners support the HTTP and HTTPS protocols.
  scope: Application Load Balancer listener.
  link: [HTTP, HTTPS](../facts/elb.md#elb-alb-listener-protocols-http-https)
  link: [Protocols](../facts/elb.md#elb-alb-listener-protocols-http-https)
elb-alb-metric-healthyhostcount
  claim: The ALB CloudWatch metric HealthyHostCount is the number of targets that are considered healthy.
  scope: Application Load Balancer CloudWatch metrics (AWS/ApplicationELB).
  link: [HealthyHostCount](../facts/elb.md#elb-alb-metric-healthyhostcount)
  link: [The number of targets that are considered healthy](../facts/elb.md#elb-alb-metric-healthyhostcount)
elb-alb-metric-httpcode-elb-5xx
  claim: The ALB CloudWatch metric HTTPCode_ELB_5XX_Count counts the HTTP 5XX server error codes that originate from the load balancer itself.
  scope: Application Load Balancer CloudWatch metrics (AWS/ApplicationELB).
  link: [HTTPCode\_ELB\_5XX\_Count](../facts/elb.md#elb-alb-metric-httpcode-elb-5xx)
  link: [originate from the load balancer](../facts/elb.md#elb-alb-metric-httpcode-elb-5xx)
elb-alb-metric-targetresponsetime
  claim: The ALB CloudWatch metric TargetResponseTime is the time in seconds from when the request leaves the load balancer until the target starts to send the response headers.
  scope: Application Load Balancer CloudWatch metrics (AWS/ApplicationELB).
  link: [TargetResponseTime](../facts/elb.md#elb-alb-metric-targetresponsetime)
  link: [the target starts to send the response headers](../facts/elb.md#elb-alb-metric-targetresponsetime)
elb-alb-metric-unhealthyhostcount
  claim: The ALB CloudWatch metric UnHealthyHostCount is the number of targets that are considered unhealthy.
  scope: Application Load Balancer CloudWatch metrics (AWS/ApplicationELB).
  link: [UnHealthyHostCount](../facts/elb.md#elb-alb-metric-unhealthyhostcount)
  link: [targets that are considered unhealthy](../facts/elb.md#elb-alb-metric-unhealthyhostcount)
elb-alb-mtls-client-cert-headers
  claim: With mutual TLS the load balancer authenticates clients with certificates from a third-party CA or AWS Private CA and passes the client certificate information to the backend in HTTP headers.
  scope: Application Load Balancer mutual TLS.
  link: [to the backend using HTTP headers](../facts/elb.md#elb-alb-mtls-client-cert-headers)
  link: [AWS Private Certificate Authority (PCA)](../facts/elb.md#elb-alb-mtls-client-cert-headers)
elb-alb-mtls-passthrough-vs-verify
  claim: ALB mutual TLS has two modes: passthrough sends the whole client certificate chain to the target without verifying it, and verify makes the load balancer authenticate the client X.509 certificate during the TLS negotiation.
  scope: Application Load Balancer HTTPS listener with mutual TLS.
  link: [without verifying it](../facts/elb.md#elb-alb-mtls-passthrough-vs-verify)
  link: [performs X.509 client certificate authentication](../facts/elb.md#elb-alb-mtls-passthrough-vs-verify)
  link: [sends the entire client certificate chain](../facts/elb.md#elb-alb-mtls-passthrough-vs-verify)
elb-alb-mtls-verify-trust-store
  claim: To use mutual TLS verify mode, you create a trust store, upload your CA certificate bundle (and optionally revocation lists), and attach the trust store to the listener.
  scope: Application Load Balancer mutual TLS verify mode.
  link: [Create a new trust store resource](../facts/elb.md#elb-alb-mtls-verify-trust-store)
  link: [certificate authority (CA) bundle](../facts/elb.md#elb-alb-mtls-verify-trust-store)
  link: [Attach the trust store to the listener](../facts/elb.md#elb-alb-mtls-verify-trust-store)
elb-alb-multiple-apps-one-instance-ports
  claim: An Application Load Balancer can route to multiple applications on one EC2 instance: you register the instance or IP address with several target groups, each on a different port.
  scope: Application Load Balancer target groups.
  link: [with multiple target groups](../facts/elb.md#elb-alb-multiple-apps-one-instance-ports)
  link: [each on a different port](../facts/elb.md#elb-alb-multiple-apps-one-instance-ports)
elb-alb-needs-listener-to-receive-traffic
  claim: An Application Load Balancer must have at least one listener; with no listeners it cannot receive traffic from clients.
  scope: Application Load Balancer.
  link: [you must add at least one listener](../facts/elb.md#elb-alb-needs-listener-to-receive-traffic)
  link: [it can't receive traffic from clients](../facts/elb.md#elb-alb-needs-listener-to-receive-traffic)
elb-alb-one-ip-per-enabled-az
  claim: An Application Load Balancer has one IP address per enabled Availability Zone, and its DNS name resolves to these addresses.
  scope: per enabled Availability Zone.
  link: [one IP address per enabled Availability Zone](../facts/elb.md#elb-alb-one-ip-per-enabled-az)
  link: [resolves to these addresses](../facts/elb.md#elb-alb-one-ip-per-enabled-az)
  say: one IP address per enabled Availability Zone | resolves to these addresses
elb-alb-path-conditions-smaller-services
  claim: With path conditions, an Application Load Balancer forwards requests based on the URL, so you can split an application into smaller services and route each request to the correct service.
  scope: Application Load Balancer listener rules.
  link: [forward requests based on the URL](../facts/elb.md#elb-alb-path-conditions-smaller-services)
  link: [structure your application as smaller services](../facts/elb.md#elb-alb-path-conditions-smaller-services)
elb-alb-peered-vpc-instances-by-ip-only
  claim: An Application Load Balancer cannot register instances in a peered VPC by instance ID; it can register them by IP address.
  scope: Application Load Balancer, targets in a peered VPC.
  link: [You can't register instances by instance ID](../facts/elb.md#elb-alb-peered-vpc-instances-by-ip-only)
  link: [You can register these instances by IP address](../facts/elb.md#elb-alb-peered-vpc-instances-by-ip-only)
elb-alb-quota-ca-certificate-size
  claim: A CA certificate in a trust store can be at most 16 KB; this quota is not adjustable.
  scope: per CA certificate; maximum; not adjustable.
  link: [16 KB](../facts/elb.md#elb-alb-quota-ca-certificate-size)
  say: sixteen kilobytes
elb-alb-quota-ca-certificates-per-trust-store
  claim: The default quota is 25 CA certificates per trust store; the quota is adjustable.
  scope: per trust store; default; adjustable.
  link: [25 CA certificates](../facts/elb.md#elb-alb-quota-ca-certificates-per-trust-store)
  say: twenty-five CA certificates
elb-alb-quota-ca-subject-size-per-trust-store
  claim: The default quota for the CA certificates subject size per trust store is 10,000; the quota is adjustable.
  scope: per trust store; default; adjustable.
  link: [10,000](../facts/elb.md#elb-alb-quota-ca-subject-size-per-trust-store)
  say: ten thousand
elb-alb-quota-certificate-chain-depth
  claim: In the Application Load Balancer certificate quotas (which cover trust store CA certificates and certificate revocation lists), the maximum certificate chain depth is 4; this quota is not adjustable.
  scope: Application Load Balancer certificate quotas, per certificate chain; maximum; not adjustable.
  link: [maximum certificate chain depth is 4](../facts/elb.md#elb-alb-quota-certificate-chain-depth)
  say: a chain depth of four
elb-alb-quota-condition-values-per-rule
  claim: An Application Load Balancer rule can have at most 5 condition values; this quota is not adjustable.
  scope: per rule; maximum; not adjustable.
  link: [5 condition values](../facts/elb.md#elb-alb-quota-condition-values-per-rule)
  say: five condition values
elb-alb-quota-condition-wildcards-per-rule
  claim: An Application Load Balancer rule can have at most 6 condition wildcards; this quota is not adjustable.
  scope: per rule; maximum; not adjustable.
  link: [6 condition wildcards](../facts/elb.md#elb-alb-quota-condition-wildcards-per-rule)
  say: six condition wildcards
elb-alb-quota-http-request-header-size
  claim: On an Application Load Balancer, the entire HTTP request header can be at most 64 K; this quota is not adjustable.
  scope: per HTTP request; maximum; not adjustable.
  link: [64 K](../facts/elb.md#elb-alb-quota-http-request-header-size)
  say: sixty-four K
elb-alb-quota-http-request-line-size
  claim: On an Application Load Balancer, the HTTP request line can be at most 16 K; this quota is not adjustable.
  scope: per HTTP request; maximum; not adjustable.
  link: [16 K](../facts/elb.md#elb-alb-quota-http-request-line-size)
  say: sixteen K
elb-alb-quota-http-response-header-size
  claim: On an Application Load Balancer, the entire HTTP response header can be at most 32 K; this quota is not adjustable.
  scope: per HTTP response; maximum; not adjustable.
  link: [32 K](../facts/elb.md#elb-alb-quota-http-response-header-size)
  say: thirty-two K
elb-alb-quota-http-single-header-size
  claim: On an Application Load Balancer, a single HTTP header can be at most 16 K; this quota is not adjustable.
  scope: per HTTP header; maximum; not adjustable.
  link: [16 K](../facts/elb.md#elb-alb-quota-http-single-header-size)
  say: sixteen K
elb-alb-quota-lambda-functions-per-target-group
  claim: A target group can have 1 Lambda function as its target; this quota is not adjustable.
  scope: per target group, per Region; maximum; not adjustable.
  link: [1 Lambda function](../facts/elb.md#elb-alb-quota-lambda-functions-per-target-group)
  say: one Lambda function
elb-alb-quota-listeners-per-lb
  claim: The default quota is 50 listeners per Application Load Balancer; the quota is adjustable.
  scope: per Application Load Balancer; default; adjustable.
  link: [50 listeners](../facts/elb.md#elb-alb-quota-listeners-per-lb)
  say: fifty listeners
elb-alb-quota-load-balancers-per-region
  claim: The default quota is 50 Application Load Balancers per Region; the quota is adjustable.
  scope: per Region, per account; default; adjustable.
  link: [50 Application Load Balancers](../facts/elb.md#elb-alb-quota-load-balancers-per-region)
  say: fifty Application Load Balancers
elb-alb-quota-load-balancers-per-target-group
  claim: A target group of an Application Load Balancer can be used by 1 load balancer; this quota is not adjustable.
  scope: per target group; maximum; not adjustable.
  link: [1 load balancer](../facts/elb.md#elb-alb-quota-load-balancers-per-target-group)
  say: one load balancer
elb-alb-quota-match-evaluations-per-rule
  claim: An Application Load Balancer rule can have at most 5 match evaluations; this quota is not adjustable.
  scope: per rule; maximum; not adjustable.
  link: [5 match evaluations](../facts/elb.md#elb-alb-quota-match-evaluations-per-rule)
  say: five match evaluations
elb-alb-quota-mtls-verify-listeners-per-lb
  claim: A load balancer can have at most 2 listeners that use mutual TLS in verify mode; this quota is not adjustable.
  scope: per load balancer; maximum; not adjustable.
  link: [2 listeners](../facts/elb.md#elb-alb-quota-mtls-verify-listeners-per-lb)
  say: two listeners
elb-alb-quota-reserved-lcus-per-lb
  claim: The default quota is 15,000 reserved LCUs per Application Load Balancer; the quota is adjustable.
  scope: per Application Load Balancer; default; adjustable.
  link: [15,000 reserved LCUs](../facts/elb.md#elb-alb-quota-reserved-lcus-per-lb)
  say: fifteen thousand reserved LCUs
elb-alb-quota-reserved-lcus-per-region
  claim: The default quota for reserved Application Load Balancer LCUs per Region is 0; the quota is adjustable.
  scope: per Region, per account; default; adjustable.
  link: [LCUs per Region is 0](../facts/elb.md#elb-alb-quota-reserved-lcus-per-region)
  say: zero reserved LCUs per Region
elb-alb-quota-revocation-entries-per-trust-store
  claim: The default quota is 500,000 revocation entries per trust store; the quota is adjustable.
  scope: per trust store; default; adjustable.
  link: [500,000 revocation entries](../facts/elb.md#elb-alb-quota-revocation-entries-per-trust-store)
  say: five hundred thousand revocation entries
elb-alb-quota-revocation-list-file-size
  claim: A certificate revocation list file can be at most 50 MB; this quota is not adjustable.
  scope: per revocation list file; maximum; not adjustable.
  link: [50 MB](../facts/elb.md#elb-alb-quota-revocation-list-file-size)
  say: fifty megabytes
elb-alb-quota-revocation-lists-per-trust-store
  claim: The default quota is 30 revocation lists per trust store; the quota is adjustable.
  scope: per trust store; default; adjustable.
  link: [30 revocation lists](../facts/elb.md#elb-alb-quota-revocation-lists-per-trust-store)
  say: thirty revocation lists
elb-alb-quota-rules-per-lb
  claim: The default quota is 100 rules per Application Load Balancer, not counting default rules; the quota is adjustable.
  scope: per Application Load Balancer, excluding default rules; default; adjustable.
  link: [100 rules](../facts/elb.md#elb-alb-quota-rules-per-lb)
  say: one hundred rules
elb-alb-quota-target-groups-per-action
  claim: One rule action of an Application Load Balancer can forward to at most 5 target groups; this quota is not adjustable.
  scope: per action, per Application Load Balancer; maximum; not adjustable.
  link: [5 target groups](../facts/elb.md#elb-alb-quota-target-groups-per-action)
  say: five target groups
elb-alb-quota-target-groups-per-lb
  claim: An Application Load Balancer can use at most 100 target groups; this quota is not adjustable.
  scope: per Application Load Balancer; maximum; not adjustable.
  link: [100 target groups](../facts/elb.md#elb-alb-quota-target-groups-per-lb)
  say: one hundred target groups
elb-alb-quota-targets-per-lb
  claim: The default quota is 1,000 targets per Application Load Balancer; the quota is adjustable.
  scope: per Application Load Balancer; default; adjustable.
  link: [1,000 targets](../facts/elb.md#elb-alb-quota-targets-per-lb)
  say: one thousand targets
elb-alb-quota-tls-message-size
  claim: In the Application Load Balancer certificate quotas (which cover trust store CA certificates and certificate revocation lists), the TLS message size limit is 64 K; this quota is not adjustable.
  scope: Application Load Balancer certificate quotas, per TLS message; maximum; not adjustable.
  link: [64 K](../facts/elb.md#elb-alb-quota-tls-message-size)
  say: sixty-four K
elb-alb-quota-trust-stores-per-account
  claim: The default quota is 20 trust stores per account; the quota is adjustable.
  scope: per account; default; adjustable.
  link: [20 trust stores](../facts/elb.md#elb-alb-quota-trust-stores-per-account)
  say: twenty trust stores
elb-alb-redirect-http-to-https
  claim: An ALB redirect action can redirect HTTP to HTTP, HTTP to HTTPS and HTTPS to HTTPS, but not HTTPS to HTTP; a redirect is temporary (HTTP 302) or permanent (HTTP 301).
  scope: Application Load Balancer redirect action.
  link: [HTTP to HTTPS](../facts/elb.md#elb-alb-redirect-http-to-https)
  link: [You cannot redirect HTTPS to HTTP](../facts/elb.md#elb-alb-redirect-http-to-https)
  link: [permanent (HTTP 301)](../facts/elb.md#elb-alb-redirect-http-to-https)
elb-alb-request-tracing-x-amzn-trace-id
  claim: When an ALB receives a request, it adds or updates the X-Amzn-Trace-Id header before sending the request to the target, which lets you trace HTTP requests from clients to targets.
  scope: Application Load Balancer.
  link: [adds or updates the **X-Amzn-Trace-Id** header](../facts/elb.md#elb-alb-request-tracing-x-amzn-trace-id)
  link: [track HTTP requests from clients to targets](../facts/elb.md#elb-alb-request-tracing-x-amzn-trace-id)
elb-alb-round-robin-use
  claim: Round robin routes requests evenly across healthy targets in sequential order and suits requests of similar complexity and targets of similar capacity.
  scope: Application Load Balancer target group.
  link: [routes requests evenly across healthy targets](../facts/elb.md#elb-alb-round-robin-use)
  link: [in a sequential order](../facts/elb.md#elb-alb-round-robin-use)
  link: [similar in complexity](../facts/elb.md#elb-alb-round-robin-use)
elb-alb-routing-algorithms-three
  claim: An ALB target group uses round robin by default and can use least outstanding requests or weighted random instead; a target group has one active routing algorithm at a time.
  scope: Application Load Balancer target group; default.
  link: [round robin](../facts/elb.md#elb-alb-routing-algorithms-three)
  link: [least outstanding requests](../facts/elb.md#elb-alb-routing-algorithms-three)
  link: [weighted random](../facts/elb.md#elb-alb-routing-algorithms-three)
  link: [only have one active routing algorithm](../facts/elb.md#elb-alb-routing-algorithms-three)
elb-alb-rule-one-routing-action-last
  claim: Each ALB rule must include exactly one routing action, forward, redirect or fixed-response, and it must be the last action performed.
  scope: Application Load Balancer rule.
  link: [exactly one of the following actions](../facts/elb.md#elb-alb-rule-one-routing-action-last)
  link: [`forward`, `redirect`, or `fixed-response`](../facts/elb.md#elb-alb-rule-one-routing-action-last)
elb-alb-rule-priority-1-to-50000
  claim: An Application Load Balancer listener rule priority is a value from 1 to 50,000; when no rule matched and the default action was taken, the access log records the priority as 0.
  scope: per listener rule; maximum; not adjustable.
  link: [1 to 50,000](../facts/elb.md#elb-alb-rule-priority-1-to-50000)
  say: one to fifty thousand
elb-alb-rules-lowest-priority-first
  claim: ALB listener rules are evaluated in priority order from the lowest value to the highest, and the default rule is evaluated last.
  scope: Application Load Balancer listener rules.
  link: [from the lowest value to the highest value](../facts/elb.md#elb-alb-rules-lowest-priority-first)
  link: [The default rule is evaluated last](../facts/elb.md#elb-alb-rules-lowest-priority-first)
elb-alb-rules-priority-then-algorithm
  claim: An Application Load Balancer node evaluates the listener rules in priority order, then selects a target from the rule action's target group with that target group's routing algorithm; the default routing algorithm is round robin.
  scope: Application Load Balancer target group; default.
  link: [Evaluates the listener rules in priority order](../facts/elb.md#elb-alb-rules-priority-then-algorithm)
  link: [The default routing algorithm is round robin](../facts/elb.md#elb-alb-rules-priority-then-algorithm)
elb-alb-security-group-controls-traffic
  claim: The security group of an Application Load Balancer controls the traffic that is allowed to reach and leave the load balancer.
  scope: Application Load Balancer.
  link: [traffic that is allowed to reach and leave](../facts/elb.md#elb-alb-security-group-controls-traffic)
  link: [The security group for your Application Load Balancer](../facts/elb.md#elb-alb-security-group-controls-traffic)
elb-alb-security-policy-protocols-ciphers
  claim: A security policy is a combination of protocols and ciphers that Elastic Load Balancing uses to negotiate SSL connections between a client and the load balancer.
  scope: Application Load Balancer secure listener.
  link: [a combination of protocols and ciphers](../facts/elb.md#elb-alb-security-policy-protocols-ciphers)
  link: [negotiate SSL connections](../facts/elb.md#elb-alb-security-policy-protocols-ciphers)
elb-alb-sg-listener-and-health-check-ports
  claim: The security group rules of an Application Load Balancer must allow traffic in both directions on both the listener port and the health check port.
  scope: Application Load Balancer security groups.
  link: [allow traffic in both directions](../facts/elb.md#elb-alb-sg-listener-and-health-check-ports)
  link: [both the listener and the health check ports](../facts/elb.md#elb-alb-sg-listener-and-health-check-ports)
elb-alb-slow-start-30-to-900-seconds-default-off
  claim: Slow start for an Application Load Balancer target group can be set from 30 to 900 seconds (15 minutes); the default is 0 seconds, which means slow start is disabled.
  scope: per Application Load Balancer target group; default; adjustable.
  link: [30 to 900 seconds](../facts/elb.md#elb-alb-slow-start-30-to-900-seconds-default-off)
  link: [15 minutes](../facts/elb.md#elb-alb-slow-start-30-to-900-seconds-default-off)
  link: [0 seconds (disabled)](../facts/elb.md#elb-alb-slow-start-30-to-900-seconds-default-off)
  say: thirty to nine hundred seconds | fifteen minutes | zero seconds, disabled
elb-alb-sni-certificate-list-multiple-domains
  claim: With a certificate list, an HTTPS listener supports multiple domains on the same port with a different certificate for each, and the load balancer chooses the certificate with SNI from the hostname the client provides.
  scope: Application Load Balancer HTTPS listener.
  link: [support multiple domains on the same port](../facts/elb.md#elb-alb-sni-certificate-list-multiple-domains)
  link: [provide a different certificate for each domain](../facts/elb.md#elb-alb-sni-certificate-list-multiple-domains)
  link: [smart certificate selection algorithm with support for SNI](../facts/elb.md#elb-alb-sni-certificate-list-multiple-domains)
elb-alb-sticky-bypasses-algorithm
  claim: With sticky sessions enabled, the routing algorithm chooses only the first target; later requests from the same client go to the same target, bypassing the algorithm.
  scope: Application Load Balancer target group; sticky sessions enabled.
  link: [used for the initial target selection](../facts/elb.md#elb-alb-sticky-bypasses-algorithm)
  link: [bypassing the selected routing algorithm](../facts/elb.md#elb-alb-sticky-bypasses-algorithm)
elb-alb-sticky-duration-vs-application-cookie
  claim: ALB stickiness is enabled per target group with either a duration-based cookie or an application-based cookie: use application-based stickiness when the application has its own session cookie, and duration-based stickiness when it does not.
  scope: Application Load Balancer target group.
  link: [duration-based cookies and application-based cookies](../facts/elb.md#elb-alb-sticky-duration-vs-application-cookie)
  link: [enabled at the target group level](../facts/elb.md#elb-alb-sticky-duration-vs-application-cookie)
  link: [application-based stickiness](../facts/elb.md#elb-alb-sticky-duration-vs-application-cookie)
elb-alb-sticky-for-stateful-servers
  claim: Application Load Balancer sticky sessions are useful for servers that keep state information; the client must support cookies.
  scope: Application Load Balancer target groups.
  link: [servers that maintain state information](../facts/elb.md#elb-alb-sticky-for-stateful-servers)
  link: [the client must support cookies](../facts/elb.md#elb-alb-sticky-for-stateful-servers)
elb-alb-sticky-not-with-cross-zone-off
  claim: ALB sticky sessions are not supported when cross-zone load balancing is disabled, and application-based stickiness does not work with weighted target groups.
  scope: Application Load Balancer stickiness.
  link: [sticky sessions while cross-zone load balancing is disabled](../facts/elb.md#elb-alb-sticky-not-with-cross-zone-off)
  link: [does not work with weighted target groups](../facts/elb.md#elb-alb-sticky-not-with-cross-zone-off)
elb-alb-sticky-sessions-what
  claim: Sticky sessions (session affinity) bind a user's session to a specific target so that all of the user's requests in the session go to the same target; the client must support cookies.
  scope: Application Load Balancer target group.
  link: [also known as session affinity](../facts/elb.md#elb-alb-sticky-sessions-what)
  link: [bind a user's session to a specific target](../facts/elb.md#elb-alb-sticky-sessions-what)
  link: [the client must support cookies](../facts/elb.md#elb-alb-sticky-sessions-what)
elb-alb-subnet-min-27-eight-free-ips
  claim: To let an Application Load Balancer scale properly, each of its Availability Zone subnets should have a CIDR block of at least /27 and at least eight free IP addresses.
  scope: per Availability Zone subnet of an Application Load Balancer; minimum; not adjustable.
  link: [at least a `/27` bitmask](../facts/elb.md#elb-alb-subnet-min-27-eight-free-ips)
  link: [at least eight free IP addresses](../facts/elb.md#elb-alb-subnet-min-27-eight-free-ips)
  say: at least a slash twenty-seven | at least eight free IP addresses
elb-alb-subnets-two-azs-different
  claim: For an Application Load Balancer you must select subnets in at least two Availability Zones, and each subnet must be from a different Availability Zone.
  scope: Application Load Balancer subnets.
  link: [at least two Availability Zone subnets](../facts/elb.md#elb-alb-subnets-two-azs-different)
  link: [from a different Availability Zone](../facts/elb.md#elb-alb-subnets-two-azs-different)
elb-alb-target-connection-timeout-10-seconds
  claim: An Application Load Balancer has a 10-second connection timeout for establishing a connection to a target.
  scope: per connection to a target; fixed; not adjustable.
  link: [connection timeout expired (10 seconds)](../facts/elb.md#elb-alb-target-connection-timeout-10-seconds)
  say: ten-second connection timeout
elb-alb-target-group-one-load-balancer
  claim: An Application Load Balancer target group can be used with only one load balancer, while a target can be registered with multiple target groups.
  scope: Application Load Balancer target group.
  link: [with only one load balancer](../facts/elb.md#elb-alb-target-group-one-load-balancer)
  link: [register a target with multiple target groups](../facts/elb.md#elb-alb-target-group-one-load-balancer)
elb-alb-target-group-stickiness-awsalbtg
  claim: By default, weighted target groups do not guarantee sticky sessions; target group stickiness on the rule keeps a client on one target group with a cookie named AWSALBTG.
  scope: Application Load Balancer weighted target groups.
  link: [does not guarantee that sticky sessions are honored](../facts/elb.md#elb-alb-target-group-stickiness-awsalbtg)
  link: [enable target group stickiness for the rule](../facts/elb.md#elb-alb-target-group-stickiness-awsalbtg)
  link: [AWSALBTG](../facts/elb.md#elb-alb-target-group-stickiness-awsalbtg)
elb-alb-target-https-no-cert-validation
  claim: With an HTTPS target group, the Application Load Balancer opens TLS connections to the targets with the certificates installed on the targets but does not validate them, so self-signed or expired certificates work.
  scope: Application Load Balancer HTTPS target group.
  link: [The load balancer does not validate these certificates](../facts/elb.md#elb-alb-target-https-no-cert-validation)
  link: [self-signed certificates or certificates that have expired](../facts/elb.md#elb-alb-target-https-no-cert-validation)
elb-alb-target-optimizer-no-sticky-more-lcu
  claim: With ALB Target Optimizer enabled on a target group, sticky sessions are not supported, the routing algorithm can only be round robin, and its traffic incurs more LCU usage than traffic to regular target groups.
  scope: Application Load Balancer target groups with target optimizer.
  link: [Sticky sessions are not supported](../facts/elb.md#elb-alb-target-optimizer-no-sticky-more-lcu)
  link: [can only be round robin](../facts/elb.md#elb-alb-target-optimizer-no-sticky-more-lcu)
  link: [incurs more LCU usage](../facts/elb.md#elb-alb-target-optimizer-no-sticky-more-lcu)
elb-alb-target-protocols-http-https
  claim: An Application Load Balancer routes to targets with the protocol and port of the target group by default, and you can override the port per target when you register it.
  scope: Application Load Balancer target group; default.
  link: [using the protocol and port number](../facts/elb.md#elb-alb-target-protocols-http-https)
  link: [override the port used for routing traffic](../facts/elb.md#elb-alb-target-protocols-http-https)
elb-alb-target-state-draining
  claim: A target in the draining state is deregistering and connection draining is in progress.
  scope: Application Load Balancer registered target.
  link: [`draining`](../facts/elb.md#elb-alb-target-state-draining)
  link: [connection draining is in process](../facts/elb.md#elb-alb-target-state-draining)
elb-alb-target-state-initial
  claim: A target in the initial state is being registered, or the load balancer is running its initial health checks on it.
  scope: Application Load Balancer registered target.
  link: [`initial`](../facts/elb.md#elb-alb-target-state-initial)
  link: [performing the initial health checks on the target](../facts/elb.md#elb-alb-target-state-initial)
elb-alb-target-state-unhealthy
  claim: A target in the unhealthy state did not respond to a health check or failed the health check.
  scope: Application Load Balancer registered target.
  link: [`unhealthy`](../facts/elb.md#elb-alb-target-state-unhealthy)
  link: [did not respond to a health check](../facts/elb.md#elb-alb-target-state-unhealthy)
elb-alb-target-state-unused
  claim: A target is in the unused state when it is not registered with a target group, its target group is not used in a listener rule, its Availability Zone is not enabled, or it is stopped or terminated.
  scope: Application Load Balancer registered target.
  link: [`unused`](../facts/elb.md#elb-alb-target-state-unused)
  link: [is not used in a listener rule](../facts/elb.md#elb-alb-target-state-unused)
elb-alb-target-types-instance-ip-lambda
  claim: An Application Load Balancer target group has the target type instance (targets by instance ID), ip (targets by IP address) or lambda (a Lambda function), and the target type cannot be changed after the target group is created.
  scope: Application Load Balancer target group; target type fixed at creation.
  link: [The target is a Lambda function](../facts/elb.md#elb-alb-target-types-instance-ip-lambda)
  link: [you can't change its target type](../facts/elb.md#elb-alb-target-types-instance-ip-lambda)
elb-alb-transforms-rewrite-host-url
  claim: An Application Load Balancer rule transform rewrites the host header or the URL of a request before it is routed to targets; the rewrite does not change the routing decision.
  scope: Application Load Balancer listener rules.
  link: [rewrites inbound requests before they are routed](../facts/elb.md#elb-alb-transforms-rewrite-host-url)
  link: [does not change the routing decision](../facts/elb.md#elb-alb-transforms-rewrite-host-url)
elb-alb-unhealthy-threshold-default-2
  claim: An Application Load Balancer target is considered unhealthy after 2 consecutive failed health checks by default; the range is 2 to 10.
  scope: per Application Load Balancer target group; default; adjustable.
  link: [2 consecutive failed health checks](../facts/elb.md#elb-alb-unhealthy-threshold-default-2)
  link: [2 to 10](../facts/elb.md#elb-alb-unhealthy-threshold-default-2)
  say: two consecutive failed health checks | two to ten
elb-alb-user-authentication-idps
  claim: An ALB can authenticate users through an OIDC-compliant identity provider, through social identity providers via Amazon Cognito user pools, or through corporate identities (SAML, OIDC or OAuth) via Amazon Cognito user pools.
  scope: Application Load Balancer user authentication.
  link: [OpenID Connect (OIDC) compliant](../facts/elb.md#elb-alb-user-authentication-idps)
  link: [social IdPs, such as Amazon, Facebook, or Google](../facts/elb.md#elb-alb-user-authentication-idps)
  link: [corporate identities, using SAML](../facts/elb.md#elb-alb-user-authentication-idps)
elb-alb-waf-integration-web-acl
  claim: You can use AWS WAF with an Application Load Balancer to allow or block requests based on the rules in a web ACL; by default, if the load balancer gets no response from AWS WAF it returns HTTP 500 and does not forward the request, unless AWS WAF fail open is enabled.
  scope: Application Load Balancer with AWS WAF; default.
  link: [allow or block requests based on the rules](../facts/elb.md#elb-alb-waf-integration-web-acl)
  link: [returns an HTTP 500 error](../facts/elb.md#elb-alb-waf-integration-web-acl)
  link: [enable AWS WAF fail open](../facts/elb.md#elb-alb-waf-integration-web-acl)
elb-alb-websocket-upgrade-rules-waf-stop
  claim: Application Load Balancers support connection upgrades from HTTP to WebSockets, but after an upgrade the listener routing rules and AWS WAF integrations no longer apply.
  scope: Application Load Balancer; after a connection upgrade.
  link: [connection upgrades from HTTP to WebSockets](../facts/elb.md#elb-alb-websocket-upgrade-rules-waf-stop)
  link: [AWS WAF integrations no longer apply](../facts/elb.md#elb-alb-websocket-upgrade-rules-waf-stop)
elb-alb-weighted-forward-traffic-split
  claim: A forward action with several target groups needs a weight for each target group, and requests matching the rule are distributed to the target groups by their weights.
  scope: Application Load Balancer forward action.
  link: [specify a weight for each target group](../facts/elb.md#elb-alb-weighted-forward-traffic-split)
  link: [based on their weights](../facts/elb.md#elb-alb-weighted-forward-traffic-split)
elb-alb-weighted-no-auto-failover
  claim: If one of the weighted target groups of a rule is empty or has only unhealthy targets, the load balancer does not automatically fail over to a target group with healthy targets.
  scope: Application Load Balancer weighted target groups; one target group empty or all unhealthy.
  link: [does not automatically fail over](../facts/elb.md#elb-alb-weighted-no-auto-failover)
elb-alb-weighted-random-no-sticky-slow-start
  claim: The weighted random algorithm supports Automatic Target Weights anomaly mitigation, but it cannot be used with slow start mode or with sticky sessions; least outstanding requests also cannot be used with slow start.
  scope: Application Load Balancer target group.
  link: [Automatic Target Weights (ATW) anomaly mitigation](../facts/elb.md#elb-alb-weighted-random-no-sticky-slow-start)
  link: [can not be used with sticky sessions](../facts/elb.md#elb-alb-weighted-random-no-sticky-slow-start)
  link: [can not be used with slow start mode](../facts/elb.md#elb-alb-weighted-random-no-sticky-slow-start)
elb-alb-xff-holds-client-ip
  claim: Because the load balancer sits between clients and servers, server access logs show only the load balancer's IP address; by default the ALB stores the client IP address in the X-Forwarded-For header and passes it to the server.
  scope: Application Load Balancer; default.
  link: [only contain the IP address](../facts/elb.md#elb-alb-xff-holds-client-ip)
  link: [stores the IP address of the client](../facts/elb.md#elb-alb-xff-holds-client-ip)
elb-alb-xff-proto-original-protocol
  claim: The X-Forwarded-Proto header tells the server which protocol (HTTP or HTTPS) the client used to connect to the load balancer.
  scope: Application Load Balancer.
  link: [identify the protocol (HTTP or HTTPS)](../facts/elb.md#elb-alb-xff-proto-original-protocol)
elb-alb-zonal-shift-cross-zone-enabled
  claim: When a zonal shift starts on an Application Load Balancer with cross-zone load balancing enabled, all traffic to targets in the impaired Availability Zone is blocked and the zonal IP addresses are removed from DNS.
  scope: Application Load Balancer with cross-zone load balancing enabled.
  link: [all traffic to targets is blocked](../facts/elb.md#elb-alb-zonal-shift-cross-zone-enabled)
  link: [zonal IP addresses are removed from DNS](../facts/elb.md#elb-alb-zonal-shift-cross-zone-enabled)
elb-alb-zonal-shift-off-by-default-one-az
  claim: Zonal shift is disabled by default and must be enabled on each Application Load Balancer, and a zonal shift for one load balancer can cover only a single Availability Zone.
  scope: Application Load Balancer; default; adjustable.
  link: [Zonal shift is disabled by default](../facts/elb.md#elb-alb-zonal-shift-off-by-default-one-az)
  link: [must be enabled on each Application Load Balancer](../facts/elb.md#elb-alb-zonal-shift-off-by-default-one-az)
  link: [only for a single Availability Zone](../facts/elb.md#elb-alb-zonal-shift-off-by-default-one-az)
elb-asg-instances-auto-registered
  claim: With EC2 Auto Scaling attached to Elastic Load Balancing, instances that Auto Scaling launches are registered with the load balancer automatically, and instances it terminates are deregistered automatically.
  scope: EC2 Auto Scaling group used with a load balancer.
  link: [automatically registered with the load balancer](../facts/elb.md#elb-asg-instances-auto-registered)
  link: [automatically de-registered from the load balancer](../facts/elb.md#elb-asg-instances-auto-registered)
elb-capacity-units-billed-per-minute
  claim: Besides the hourly charge, Application, Network and Gateway Load Balancers are charged for the capacity units (LCU, NLCU or GLCU) used per minute.
  scope: per load balancer.
  link: [used per minute](../facts/elb.md#elb-capacity-units-billed-per-minute)
  link: [Load Balancer Capacity Units (LCU)](../facts/elb.md#elb-capacity-units-billed-per-minute)
  say: used per minute | Load Balancer Capacity Units
elb-case-kee-wah-order-spikes
  claim: Kee Wah Bakery uses Elastic Load Balancing and Amazon CloudFront to support order spikes on its online shop; ELB scales the shop's load balancer with traffic so that no single server instance is overloaded.
  scope: Kee Wah Bakery (case study).
  link: [to support order spikes](../facts/elb.md#elb-case-kee-wah-order-spikes)
  link: [preventing any individual server instance from becoming overloaded](../facts/elb.md#elb-case-kee-wah-order-spikes)
elb-case-kiswe-fan-interactivity
  claim: Kiswe uses Elastic Load Balancing in front of Amazon EC2 instances to handle fan interactivity, logins, chats and ticket verification for its live streaming events.
  scope: Kiswe (case study).
  link: [fan interactivity, logins, chats, and ticket verification](../facts/elb.md#elb-case-kiswe-fan-interactivity)
  link: [Elastic Load Balancing for Amazon EC2 instances](../facts/elb.md#elb-case-kiswe-fan-interactivity)
elb-case-nexon-game-launches
  claim: Nexon's Mobile Publishing Division uses Amazon DynamoDB, Amazon Aurora and Elastic Load Balancing to give players a stable online experience during launches of new game titles.
  scope: Nexon (case study).
  link: [a stable online experience for players](../facts/elb.md#elb-case-nexon-game-launches)
  link: [during launches of new game titles](../facts/elb.md#elb-case-nexon-game-launches)
elb-case-redshield-elb-flexible-resilient
  claim: RedShield, which provides DDoS protection on AWS, uses Elastic Load Balancing to make its infrastructure flexible and resilient, together with AWS Global Accelerator.
  scope: RedShield (case study).
  link: [to make its infrastructure flexible and resilient](../facts/elb.md#elb-case-redshield-elb-flexible-resilient)
  link: [virtually always-on DDoS protection](../facts/elb.md#elb-case-redshield-elb-flexible-resilient)
elb-change-alb-automatic-target-weights-2023-11
  claim: On 2023-11-26 Application Load Balancers added the Automatic Target Weights algorithm.
  scope: Application Load Balancer target groups.
  link: [2023-11-26](../facts/elb.md#elb-change-alb-automatic-target-weights-2023-11)
  link: [automatic target weights algorithm](../facts/elb.md#elb-change-alb-automatic-target-weights-2023-11)
elb-change-alb-cloudwatch-logs-2026-07
  claim: On 2026-07-23 Amazon CloudWatch Logs added Application Load Balancer access, connection and health check logs as vended logs.
  scope: Application Load Balancer logs.
  link: [2026-07-23](../facts/elb.md#elb-change-alb-cloudwatch-logs-2026-07)
  link: [Application Load Balancer (ALB) logs as vended logs](../facts/elb.md#elb-change-alb-cloudwatch-logs-2026-07)
elb-change-alb-header-modification-all-codes-2025-02
  claim: On 2025-02-28 Application Load Balancer HTTP header modification was extended to all response codes; before, it was limited to response codes 2xx and 3xx.
  scope: Application Load Balancers.
  link: [2025-02-28](../facts/elb.md#elb-change-alb-header-modification-all-codes-2025-02)
  link: [for all response codes](../facts/elb.md#elb-change-alb-header-modification-all-codes-2025-02)
  link: [limited to response codes 2xx and 3xx](../facts/elb.md#elb-change-alb-header-modification-all-codes-2025-02)
  changed: 2025-02-28: was limited to response codes 2xx and 3xx
elb-change-alb-health-check-logs-2025-11
  claim: On 2025-11-21 Application Load Balancers added health check logs, delivered to an Amazon S3 bucket every 5 minutes with no charge beyond S3 storage.
  scope: Application Load Balancers.
  link: [2025-11-21](../facts/elb.md#elb-change-alb-health-check-logs-2025-11)
  link: [every 5 minutes](../facts/elb.md#elb-change-alb-health-check-logs-2025-11)
  link: [no additional charges beyond standard S3 storage costs](../facts/elb.md#elb-change-alb-health-check-logs-2025-11)
elb-change-alb-jwt-validation-2025-11
  claim: On 2025-11-21 Application Load Balancers added validation of JSON Web Tokens (JWT) for service-to-service and machine-to-machine communication.
  scope: Application Load Balancers.
  link: [2025-11-21](../facts/elb.md#elb-change-alb-jwt-validation-2025-11)
  link: [validate JSON Web Tokens (JWT)](../facts/elb.md#elb-change-alb-jwt-validation-2025-11)
elb-change-alb-mutual-tls-2023-11
  claim: On 2023-11-26 Application Load Balancers added mutual TLS authentication.
  scope: Application Load Balancers.
  link: [2023-11-26](../facts/elb.md#elb-change-alb-mutual-tls-2023-11)
  link: [support for mutual TLS authentication](../facts/elb.md#elb-change-alb-mutual-tls-2023-11)
elb-change-alb-target-optimizer-2025-11
  claim: On 2025-11-20 Application Load Balancers launched Target Optimizer, which enforces a maximum number of concurrent requests on a target with an agent that runs on the targets; its traffic generates more LCU usage than regular target groups.
  scope: Application Load Balancer target groups.
  link: [2025-11-20](../facts/elb.md#elb-change-alb-target-optimizer-2025-11)
  link: [enforce a maximum number of concurrent requests](../facts/elb.md#elb-change-alb-target-optimizer-2025-11)
  link: [generates more LCU usage](../facts/elb.md#elb-change-alb-target-optimizer-2025-11)
elb-change-alb-tls13-policies-2023-03
  claim: On 2023-03-22 Application Load Balancers added TLS 1.3 predefined security policies; Network Load Balancers had TLS 1.3 policies since 2021-10-14.
  scope: Application Load Balancer HTTPS listeners.
  link: [2023-03-22](../facts/elb.md#elb-change-alb-tls13-policies-2023-03)
  link: [TLS 1.3 predefined security policies](../facts/elb.md#elb-change-alb-tls13-policies-2023-03)
elb-change-alb-transforms-2025-10
  claim: On 2025-10-15 Application Load Balancers added transforms that rewrite host headers and URLs of incoming requests before routing to a target.
  scope: Application Load Balancers.
  link: [2025-10-15](../facts/elb.md#elb-change-alb-transforms-2025-10)
  link: [transform host headers and URLs](../facts/elb.md#elb-change-alb-transforms-2025-10)
elb-change-alb-zonal-shift-2022-11
  claim: On 2022-11-28 Application Load Balancers added zonal shift, which routes traffic away from a single impaired Availability Zone through Amazon Application Recovery Controller (ARC).
  scope: Application Load Balancers.
  link: [2022-11-28](../facts/elb.md#elb-change-alb-zonal-shift-2022-11)
  link: [away from a single impaired Availability Zone](../facts/elb.md#elb-change-alb-zonal-shift-2022-11)
elb-change-cloudfront-vpc-origins-2024-11
  claim: On 2024-11-20 Amazon CloudFront added VPC origins, which restrict access to an Application Load Balancer, Network Load Balancer or EC2 instance origin.
  scope: Amazon CloudFront origins.
  link: [2024-11-20](../facts/elb.md#elb-change-cloudfront-vpc-origins-2024-11)
  link: [Use CloudFront VPC origins to restrict access](../facts/elb.md#elb-change-cloudfront-vpc-origins-2024-11)
elb-change-fips-140-3-policies-2023-11
  claim: On 2023-11-20 Application and Network Load Balancers added security policies that use FIPS 140-3 cryptographic modules when terminating TLS connections.
  scope: Application Load Balancer HTTPS listeners and Network Load Balancer TLS listeners.
  link: [2023-11-20](../facts/elb.md#elb-change-fips-140-3-policies-2023-11)
  link: [FIPS 140-3](../facts/elb.md#elb-change-fips-140-3-policies-2023-11)
elb-change-gwlb-tcp-reset-2026-09
  claim: On 2026-09-03 Gateway Load Balancers added optional TCP Reset packets when a target becomes unhealthy, is deregistered, or a flow's idle timeout expires; before, existing TCP connections kept going to the unhealthy target (fail-open). It is off by default.
  scope: Gateway Load Balancer target groups.
  link: [2026-09-03](../facts/elb.md#elb-change-gwlb-tcp-reset-2026-09)
  link: [aka fail-open behavior](../facts/elb.md#elb-change-gwlb-tcp-reset-2026-09)
  link: [TCP Reset is not enabled by default](../facts/elb.md#elb-change-gwlb-tcp-reset-2026-09)
  changed: 2026-09-03: was existing TCP connections would continue to be forwarded to the unhealthy target (aka fail-open behavior)
elb-change-lcu-reservation-alb-nlb-2024-11
  claim: On 2024-11-20 Application and Network Load Balancers added Capacity Unit (LCU) reservation, which sets a minimum capacity for the load balancer.
  scope: Application and Network Load Balancers.
  link: [2024-11-20](../facts/elb.md#elb-change-lcu-reservation-alb-nlb-2024-11)
  link: [set a minimum capacity for your load balancer](../facts/elb.md#elb-change-lcu-reservation-alb-nlb-2024-11)
elb-change-lcu-reservation-gwlb-2025-04
  claim: On 2025-04-10 Gateway Load Balancers added LCU reservation, to set a minimum bandwidth capacity on top of the existing automatic scaling.
  scope: Gateway Load Balancers.
  link: [2025-04-10](../facts/elb.md#elb-change-lcu-reservation-gwlb-2025-04)
  link: [set a minimum bandwidth capacity](../facts/elb.md#elb-change-lcu-reservation-gwlb-2025-04)
elb-change-nlb-listener-rules-2026-07
  claim: Network Load Balancer listener rules, which route by source IP address type on a dual-stack load balancer, appear in the NLB document history on 2026-07-10 and were announced on 2026-07-22; before, serving IPv4 and IPv6 clients with their own client IPs needed two load balancers or protocol translation.
  scope: dual-stack Network Load Balancers.
  link: [2026-07-22](../facts/elb.md#elb-change-nlb-listener-rules-2026-07)
  link: [2026-07-10](../facts/elb.md#elb-change-nlb-listener-rules-2026-07)
  link: [route connections to different target groups](../facts/elb.md#elb-change-nlb-listener-rules-2026-07)
  link: [either run two separate load balancers](../facts/elb.md#elb-change-nlb-listener-rules-2026-07)
  changed: 2026-07-22: was either run two separate load balancers (one per IP version) and split clients with DNS, or send all traffic to one target group and lose the original client IP through protocol translation
elb-change-nlb-quic-2025-11
  claim: On 2025-11-13 Network Load Balancers added QUIC and TCP_QUIC protocols, forwarding QUIC traffic in passthrough mode.
  scope: Network Load Balancers.
  link: [2025-11-13](../facts/elb.md#elb-change-nlb-quic-2025-11)
  link: [QUIC protocol in passthrough mode](../facts/elb.md#elb-change-nlb-quic-2025-11)
elb-change-nlb-remove-az-2025-02
  claim: On 2025-02-13 Network Load Balancers gained the ability to disable (remove) an Availability Zone of an existing load balancer; before, you could add Availability Zones but not remove them.
  scope: Network Load Balancers.
  link: [2025-02-13](../facts/elb.md#elb-change-nlb-remove-az-2025-02)
  link: [disable an Availability Zone](../facts/elb.md#elb-change-nlb-remove-az-2025-02)
  link: [could not remove AZs](../facts/elb.md#elb-change-nlb-remove-az-2025-02)
  changed: 2025-02-13: was customers could add AZs to an existing NLB, but could not remove AZs
elb-change-nlb-security-groups-2023-08
  claim: On 2023-08-10 Network Load Balancers added security groups, which you associate with the load balancer at creation.
  scope: Network Load Balancers.
  link: [2023-08-10](../facts/elb.md#elb-change-nlb-security-groups-2023-08)
  link: [associate security groups with your Network Load Balancers](../facts/elb.md#elb-change-nlb-security-groups-2023-08)
elb-change-nlb-weighted-target-groups-2025-11
  claim: On 2025-11-19 Network Load Balancers added weighted target groups for the default action, for blue/green and canary deployments.
  scope: Network Load Balancers.
  link: [2025-11-19](../facts/elb.md#elb-change-nlb-weighted-target-groups-2025-11)
  link: [default action with weighted target groups](../facts/elb.md#elb-change-nlb-weighted-target-groups-2025-11)
  link: [Blue-Green and Canary Deployments](../facts/elb.md#elb-change-nlb-weighted-target-groups-2025-11)
elb-change-nlb-zonal-shift-more-configs-2026-09
  claim: On 2026-09-24 zonal shift on cross-zone Network Load Balancers was extended to target groups with connection termination for unhealthy targets, UDP target groups and Application Load Balancer targets.
  scope: Network Load Balancers with cross-zone load balancing enabled.
  link: [2026-09-24](../facts/elb.md#elb-change-nlb-zonal-shift-more-configs-2026-09)
  link: [Zonal shift for additional target group configurations](../facts/elb.md#elb-change-nlb-zonal-shift-more-configs-2026-09)
elb-change-rfc9151-policies-2026-08
  claim: On 2026-08-04 Application and Network Load Balancers added TLS security policies that comply with RFC 9151 (CNSA 1.0 suite requirements).
  scope: Application Load Balancer HTTPS listeners and Network Load Balancer TLS listeners.
  link: [2026-08-04](../facts/elb.md#elb-change-rfc9151-policies-2026-08)
  link: [RFC 9151 compliant security policies](../facts/elb.md#elb-change-rfc9151-policies-2026-08)
elb-change-target-group-cross-zone-2022-11
  claim: On 2022-11-17 Application and Network Load Balancers added cross-zone load balancing settings at the target group level, and on 2022-11-28 Application Load Balancers added the option to turn off cross-zone load balancing.
  scope: Application and Network Load Balancer target groups.
  link: [2022-11-17](../facts/elb.md#elb-change-target-group-cross-zone-2022-11)
  link: [2022-11-28](../facts/elb.md#elb-change-target-group-cross-zone-2022-11)
  link: [at the target group level](../facts/elb.md#elb-change-target-group-cross-zone-2022-11)
elb-change-target-group-health-2022-11
  claim: In November 2022 (2022-11-17 for Network Load Balancers, 2022-11-28 for Application Load Balancers) target group health settings were added: a minimum count or percentage of healthy targets and the action taken when it is not met.
  scope: Application and Network Load Balancer target groups.
  link: [2022-11-17](../facts/elb.md#elb-change-target-group-health-2022-11)
  link: [2022-11-28](../facts/elb.md#elb-change-target-group-health-2022-11)
  link: [minimum count or percentage of targets](../facts/elb.md#elb-change-target-group-health-2022-11)
elb-choose-alb-for-http-flexible-management
  claim: AWS recommends an Application Load Balancer when you need to load balance HTTP requests or need flexible application management.
  scope: Elastic Load Balancing.
  link: [If you need to load balance HTTP requests](../facts/elb.md#elb-choose-alb-for-http-flexible-management)
  link: [If you need flexible application management](../facts/elb.md#elb-choose-alb-for-http-flexible-management)
elb-choose-gwlb-for-third-party-appliances
  claim: The Elastic Load Balancing FAQ says that if you need to deploy and run third-party virtual appliances, you can use a Gateway Load Balancer.
  scope: Elastic Load Balancing.
  link: [third-party virtual appliances](../facts/elb.md#elb-choose-gwlb-for-third-party-appliances)
  link: [you can use Gateway Load Balancer](../facts/elb.md#elb-choose-gwlb-for-third-party-appliances)
elb-choose-nlb-for-layer4-extreme-performance-static-ip
  claim: AWS recommends a Network Load Balancer for network and transport protocol (TCP, UDP) load balancing, for extreme performance and low latency, and when the application needs a static IP.
  scope: Elastic Load Balancing.
  link: [network/transport protocols (layer4 – TCP, UDP)](../facts/elb.md#elb-choose-nlb-for-layer4-extreme-performance-static-ip)
  link: [extreme performance and static IP is needed](../facts/elb.md#elb-choose-nlb-for-layer4-extreme-performance-static-ip)
elb-classic-previous-generation-migrate
  claim: Classic Load Balancers are the previous generation of Elastic Load Balancing load balancers, and AWS recommends migrating to a current generation load balancer.
  scope: Classic Load Balancer.
  link: [previous generation of load balancers](../facts/elb.md#elb-classic-previous-generation-migrate)
  link: [migrate to a current generation load balancer](../facts/elb.md#elb-classic-previous-generation-migrate)
elb-cloudfront-vpc-origins-alb-nlb-private-subnets
  claim: CloudFront VPC origins let CloudFront deliver content from Application Load Balancers, Network Load Balancers and EC2 instances in private subnets, so the origins need no public access.
  scope: Amazon CloudFront VPC origins.
  link: [Application Load Balancers (ALBs), Network Load Balancers (NLBs)](../facts/elb.md#elb-cloudfront-vpc-origins-alb-nlb-private-subnets)
  link: [in private subnets as VPC origins](../facts/elb.md#elb-cloudfront-vpc-origins-alb-nlb-private-subnets)
  link: [private subnets with no public access](../facts/elb.md#elb-cloudfront-vpc-origins-alb-nlb-private-subnets)
elb-cloudfront-vpc-origins-nlb-restrictions
  claim: A Network Load Balancer used as a CloudFront VPC origin must have a security group attached, and a Network Load Balancer with TLS listeners cannot be a VPC origin.
  scope: Amazon CloudFront VPC origins.
  link: [with TLS listeners cannot be added](../facts/elb.md#elb-cloudfront-vpc-origins-nlb-restrictions)
  link: [must have a security group attached to it](../facts/elb.md#elb-cloudfront-vpc-origins-nlb-restrictions)
elb-compare-gwlb-reached-by-route-table
  claim: In the AWS product comparison, Application and Network Load Balancers are reached through a virtual IP (VIP), while a Gateway Load Balancer is reached through a route table entry and does not terminate the flow.
  scope: Elastic Load Balancing.
  link: [Route table entry](../facts/elb.md#elb-compare-gwlb-reached-by-route-table)
  link: [VIP](../facts/elb.md#elb-compare-gwlb-reached-by-route-table)
elb-compare-layer-per-type
  claim: In the AWS product comparison, an Application Load Balancer works at layer 7, a Network Load Balancer at layer 4, a Gateway Load Balancer as a layer 3 gateway with layer 4 load balancing, and a Classic Load Balancer at layer 4/7.
  scope: Elastic Load Balancing.
  link: [Layer 7](../facts/elb.md#elb-compare-layer-per-type)
  link: [Layer 4](../facts/elb.md#elb-compare-layer-per-type)
  link: [Layer 3 Gateway + Layer 4 Load Balancing](../facts/elb.md#elb-compare-layer-per-type)
elb-compare-listener-protocols-per-type
  claim: In the AWS product comparison, Application Load Balancer listeners use HTTP, HTTPS and gRPC, Network Load Balancer listeners use TCP, UDP and TLS, and a Gateway Load Balancer listens for IP traffic.
  scope: Elastic Load Balancing.
  link: [HTTP, HTTPS, gRPC](../facts/elb.md#elb-compare-listener-protocols-per-type)
  link: [TCP, UDP, TLS](../facts/elb.md#elb-compare-listener-protocols-per-type)
  link: [IP](../facts/elb.md#elb-compare-listener-protocols-per-type)
elb-compare-security-groups-not-gwlb
  claim: In the AWS feature table, Application, Network and Classic Load Balancers support security groups and SSL offloading; a Gateway Load Balancer supports neither.
  scope: Elastic Load Balancing.
  link: [Security Groups](../facts/elb.md#elb-compare-security-groups-not-gwlb)
  link: [SSL Offloading](../facts/elb.md#elb-compare-security-groups-not-gwlb)
elb-compare-static-elastic-ip-nlb-only
  claim: In the AWS feature table, only the Network Load Balancer has a static or Elastic IP address; the Application, Gateway and Classic Load Balancers do not.
  scope: Elastic Load Balancing.
  link: [IP address - Static, Elastic](../facts/elb.md#elb-compare-static-elastic-ip-nlb-only)
  link: [Network Load Balancer](../facts/elb.md#elb-compare-static-elastic-ip-nlb-only)
elb-compare-target-types-per-type
  claim: In the AWS product comparison, an Application Load Balancer targets IP addresses, instances and Lambda functions; a Network Load Balancer targets IP addresses, instances and an Application Load Balancer; a Gateway Load Balancer targets IP addresses and instances.
  scope: Elastic Load Balancing.
  link: [IP, Instance, Lambda](../facts/elb.md#elb-compare-target-types-per-type)
  link: [IP, Instance, Application Load Balancer](../facts/elb.md#elb-compare-target-types-per-type)
  link: [IP, Instance](../facts/elb.md#elb-compare-target-types-per-type)
elb-compare-user-authentication-alb-only
  claim: In the AWS feature table, user authentication is a feature of the Application Load Balancer only.
  scope: Elastic Load Balancing.
  link: [User Authentication](../facts/elb.md#elb-compare-user-authentication-alb-only)
  link: [Application Load Balancer](../facts/elb.md#elb-compare-user-authentication-alb-only)
elb-cross-zone-what-it-does
  claim: With cross-zone load balancing enabled, each load balancer node distributes traffic across the registered targets in all enabled Availability Zones; with it disabled, each node uses only the targets in its own Availability Zone.
  scope: load balancer node.
  link: [registered targets in all enabled Availability Zones](../facts/elb.md#elb-cross-zone-what-it-does)
  link: [registered targets in its Availability Zone](../facts/elb.md#elb-cross-zone-what-it-does)
elb-custom-domain-route53-alias
  claim: To use a DNS name that is easier to remember, you associate a custom domain name with the DNS name of the Application Load Balancer, for example with an Amazon Route 53 alias record that points to the load balancer.
  scope: Application Load Balancer DNS name.
  link: [create a custom domain name](../facts/elb.md#elb-custom-domain-route53-alias)
  link: [create an alias record](../facts/elb.md#elb-custom-domain-route53-alias)
elb-decision-guide-lb-type-by-application-needs
  claim: The AWS networking decision guide says you can use different types of load balancers depending on the needs of your applications, and that Elastic Load Balancing helps the workloads in your VPCs scale and provide high availability.
  scope: AWS networking and content delivery decision guide.
  link: [different types of load balancers](../facts/elb.md#elb-decision-guide-lb-type-by-application-needs)
  link: [depending on the needs of your applications](../facts/elb.md#elb-decision-guide-lb-type-by-application-needs)
elb-deletion-protection-off-by-default
  claim: Deletion protection prevents a load balancer from being deleted accidentally; it is disabled by default, and while it is enabled you cannot delete the load balancer.
  scope: Application, Network and Gateway Load Balancer; default; adjustable.
  link: [deletion protection is disabled](../facts/elb.md#elb-deletion-protection-off-by-default)
  link: [You can't delete a load balancer](../facts/elb.md#elb-deletion-protection-off-by-default)
  link: [deleted accidentally](../facts/elb.md#elb-deletion-protection-off-by-default)
elb-deregister-stops-routing-draining
  claim: When a target is deregistered, the load balancer stops routing requests to it at once, and the target stays in the draining state until its in-flight requests have completed.
  scope: Application Load Balancer target deregistration.
  link: [stops routing requests to a target](../facts/elb.md#elb-deregister-stops-routing-draining)
  link: [enters the `draining` state](../facts/elb.md#elb-deregister-stops-routing-draining)
  link: [until in-flight requests have completed](../facts/elb.md#elb-deregister-stops-routing-draining)
elb-deregistration-delay-default-300-seconds
  claim: The deregistration delay of an Application, Network or Gateway Load Balancer target group is 300 seconds by default and can be set from 0 to 3600 seconds.
  scope: per target group (Application, Network and Gateway Load Balancers); default; adjustable.
  link: [300 seconds](../facts/elb.md#elb-deregistration-delay-default-300-seconds)
  link: [0 to 3600 seconds](../facts/elb.md#elb-deregistration-delay-default-300-seconds)
  say: three hundred seconds | zero to three thousand six hundred seconds
elb-disabled-az-targets-stay-registered
  claim: After you disable an Availability Zone, its targets stay registered with the load balancer, but the load balancer does not route traffic to them.
  scope: targets in a disabled Availability Zone.
  link: [remain registered with the load balancer](../facts/elb.md#elb-disabled-az-targets-stay-registered)
  link: [does not route traffic to them](../facts/elb.md#elb-disabled-az-targets-stay-registered)
elb-dns-failover-client-cache-60-seconds
  claim: With target group DNS failover, the IP addresses of unhealthy zones are removed from the load balancer DNS name, but a client DNS cache can keep them until the 60-second TTL expires.
  scope: per load balancer DNS name.
  link: [60 seconds](../facts/elb.md#elb-dns-failover-client-cache-60-seconds)
  link: [the time-to-live (TTL) in the DNS record expires](../facts/elb.md#elb-dns-failover-client-cache-60-seconds)
  say: sixty seconds | until the DNS TTL expires
elb-dns-returns-node-ips
  claim: Clients resolve the load balancer's domain name through DNS; Amazon controls the DNS entry and the Amazon DNS servers return the IP addresses of the load balancer nodes.
  scope: load balancer DNS name.
  link: [The DNS entry is controlled by Amazon](../facts/elb.md#elb-dns-returns-node-ips)
  link: [IP addresses of the load balancer nodes](../facts/elb.md#elb-dns-returns-node-ips)
elb-dns-ttl-60-seconds-remap
  claim: As traffic changes, Elastic Load Balancing scales the load balancer and updates its DNS entry, which has a TTL of 60 seconds so that the IP addresses can be remapped quickly.
  scope: load balancer DNS entry.
  link: [time-to-live (TTL) of 60 seconds](../facts/elb.md#elb-dns-ttl-60-seconds-remap)
  link: [scales your load balancer](../facts/elb.md#elb-dns-ttl-60-seconds-remap)
  link: [IP addresses can be remapped quickly](../facts/elb.md#elb-dns-ttl-60-seconds-remap)
elb-dualstack-without-public-ipv4-not-internal
  claim: With the IP address type 'dualstack without public IPv4', clients use public and private IPv6 addresses and private IPv4 addresses; this option is not supported with the internal scheme.
  scope: load balancer IP address type.
  link: [public and private IPv6 addresses and private IPv4](../facts/elb.md#elb-dualstack-without-public-ipv4-not-internal)
  link: [not supported with the `internal` load balancer scheme](../facts/elb.md#elb-dualstack-without-public-ipv4-not-internal)
elb-faq-api-private-access-vpc-endpoints
  claim: You can access the Elastic Load Balancing APIs privately from a VPC by creating VPC endpoints; the routing is handled by the AWS network without an internet gateway, NAT gateway or VPN connection.
  scope: Elastic Load Balancing.
  link: [by creating VPC endpoints](../facts/elb.md#elb-faq-api-private-access-vpc-endpoints)
  link: [privately access Elastic Load Balancing APIs](../facts/elb.md#elb-faq-api-private-access-vpc-endpoints)
  link: [handled by the AWS network](../facts/elb.md#elb-faq-api-private-access-vpc-endpoints)
elb-faq-cannot-convert-load-balancer-type
  claim: You cannot convert one load balancer type into another (for example, a Classic Load Balancer into an Application Load Balancer); you migrate instead.
  scope: Elastic Load Balancing.
  link: [you cannot convert one load balancer type](../facts/elb.md#elb-faq-cannot-convert-load-balancer-type)
  link: [You can migrate to Application Load Balancer](../facts/elb.md#elb-faq-cannot-convert-load-balancer-type)
elb-faq-classic-no-feature-parity-with-alb
  claim: The Classic Load Balancer (previous generation) has no feature parity with the Application Load Balancer, which AWS calls the foundation of its application layer load-balancing platform for the future.
  scope: Elastic Load Balancing.
  link: [there is no feature parity](../facts/elb.md#elb-faq-classic-no-feature-parity-with-alb)
  link: [the foundation of our application layer load-balancing platform](../facts/elb.md#elb-faq-classic-no-feature-parity-with-alb)
elb-faq-free-tier-credits-from-2025-07-15
  claim: Starting July 15, 2025, new AWS customers receive up to $200 in AWS Free Tier credits, which can be applied to eligible services including Elastic Load Balancing.
  scope: new AWS customers; maximum.
  link: [up to $200 in AWS Free Tier credits](../facts/elb.md#elb-faq-free-tier-credits-from-2025-07-15)
  link: [Starting July 15, 2025](../facts/elb.md#elb-faq-free-tier-credits-from-2025-07-15)
elb-faq-new-connections-not-requests
  claim: For Network Load Balancer LCUs, new connections or flows per second are not the same as requests per second, because multiple requests can be sent in a single connection.
  scope: Network Load Balancer LCU.
  link: [Multiple requests can be sent](../facts/elb.md#elb-faq-new-connections-not-requests)
  link: [in a single connection](../facts/elb.md#elb-faq-new-connections-not-requests)
elb-faq-sla-monthly-99-99
  claim: Elastic Load Balancing guarantees a monthly availability of at least 99.99% for load balancers (Classic, Application or Network).
  scope: per load balancer (Classic, Application or Network), monthly; minimum.
  link: [99.99%](../facts/elb.md#elb-faq-sla-monthly-99-99)
  link: [monthly availability](../facts/elb.md#elb-faq-sla-monthly-99-99)
elb-faq-sni-automatic-multiple-certificates
  claim: Server Name Indication (SNI) is enabled automatically when more than one TLS certificate is associated with the same secure listener, and disabled automatically when the listener has only one certificate.
  scope: secure listener (Application Load Balancer HTTPS, Network Load Balancer TLS).
  link: [SNI is automatically enabled](../facts/elb.md#elb-faq-sni-automatic-multiple-certificates)
  link: [more than one TLS certificate](../facts/elb.md#elb-faq-sni-automatic-multiple-certificates)
  link: [automatically disabled](../facts/elb.md#elb-faq-sni-automatic-multiple-certificates)
elb-features-millions-of-requests
  claim: Elastic Load Balancing is designed to handle growing traffic, can load balance millions of requests per second, and can handle sudden volatile traffic patterns.
  scope: Elastic Load Balancing (product features page).
  link: [millions of requests/sec](../facts/elb.md#elb-features-millions-of-requests)
  link: [sudden volatile traffic patterns](../facts/elb.md#elb-features-millions-of-requests)
  say: millions of requests per second | sudden volatile traffic patterns
elb-free-tier-750-hours-15-lcus
  claim: The ELB pricing page says new AWS customers receive 750 hours per month shared between Classic and Application Load Balancers, 15 GB of data processing for Classic Load Balancers, and 15 LCUs for Application Load Balancers.
  scope: per new AWS account, per month; pricing-page wording; the FAQ (elb-free-tier-faq-includes-nlb) also names Network Load Balancers; see elb-faq-free-tier-credits-from-2025-07-15 for the Free Tier credits of new customers from July 15, 2025.
  link: [750 hours per month](../facts/elb.md#elb-free-tier-750-hours-15-lcus)
  link: [15 LCUs](../facts/elb.md#elb-free-tier-750-hours-15-lcus)
  link: [15 GB](../facts/elb.md#elb-free-tier-750-hours-15-lcus)
  say: seven hundred fifty hours per month | fifteen LCUs | fifteen gigabytes
elb-free-tier-faq-includes-nlb
  claim: The ELB FAQ says the free tier for new accounts also covers Network Load Balancers: 15 LCUs each for Application and Network Load Balancers, 15 GB for Classic, and 750 load balancer hours shared between Application, Network and Classic Load Balancers.
  scope: per new AWS account; FAQ wording; the pricing page (elb-free-tier-750-hours-15-lcus) names only Classic and Application Load Balancers; see elb-faq-free-tier-credits-from-2025-07-15 for the Free Tier credits of new customers from July 15, 2025.
  link: [15 LCUs](../facts/elb.md#elb-free-tier-faq-includes-nlb)
  link: [750 load balancer hours](../facts/elb.md#elb-free-tier-faq-includes-nlb)
  say: fifteen LCUs | seven hundred fifty load balancer hours
elb-ga-alb-multiple-regions
  claim: You can use AWS Global Accelerator with Application Load Balancers to distribute incoming traffic across multiple load balancers in one or more AWS Regions.
  scope: Application Load Balancers with AWS Global Accelerator.
  link: [AWS Global Accelerator](../facts/elb.md#elb-ga-alb-multiple-regions)
  link: [load balancers in one or more AWS Regions](../facts/elb.md#elb-ga-alb-multiple-regions)
elb-gwlb-5-tuple-geneve-6081
  claim: A Gateway Load Balancer node uses a 5-tuple flow hash to select a target appliance, keeps all packets of a flow on the same appliance, and exchanges traffic with the appliances using the GENEVE protocol on port 6081.
  scope: Gateway Load Balancer.
  link: [5-tuple flow hash algorithm](../facts/elb.md#elb-gwlb-5-tuple-geneve-6081)
  link: [GENEVE protocol on port 6081](../facts/elb.md#elb-gwlb-5-tuple-geneve-6081)
  link: [consistently routed to the same target appliance](../facts/elb.md#elb-gwlb-5-tuple-geneve-6081)
elb-gwlb-cross-zone-300-targets-per-lb
  claim: A Gateway Load Balancer supports 300 targets per Availability Zone; with cross-zone load balancing on, the maximum becomes 300 targets per Gateway Load Balancer.
  scope: per Gateway Load Balancer; maximum; not adjustable; cross-zone load balancing on.
  link: [300 targets per Availability Zone](../facts/elb.md#elb-gwlb-cross-zone-300-targets-per-lb)
  link: [300 per Gateway Load Balancer](../facts/elb.md#elb-gwlb-cross-zone-300-targets-per-lb)
  say: three hundred targets per Availability Zone | three hundred per Gateway Load Balancer
elb-gwlb-dereg-existing-flows-350-120
  claim: When a Gateway Load Balancer target is deregistered, existing TCP flows are closed if they are idle for more than 350 seconds, and existing flows of other protocols are closed if idle for more than 120 seconds.
  scope: per deregistered Gateway Load Balancer target.
  link: [350 seconds](../facts/elb.md#elb-gwlb-dereg-existing-flows-350-120)
  link: [120 seconds](../facts/elb.md#elb-gwlb-dereg-existing-flows-350-120)
  say: three hundred fifty seconds | one hundred twenty seconds
elb-gwlb-endpoint-next-hop-route-table
  claim: Traffic to and from a Gateway Load Balancer endpoint is steered with route tables; the endpoint and the application servers must be in different subnets so that the endpoint can be the next hop in the application subnet's route table.
  scope: Gateway Load Balancer endpoint.
  link: [configured using route tables](../facts/elb.md#elb-gwlb-endpoint-next-hop-route-table)
  link: [as the next hop in the route table](../facts/elb.md#elb-gwlb-endpoint-next-hop-route-table)
  link: [in different subnets](../facts/elb.md#elb-gwlb-endpoint-next-hop-route-table)
elb-gwlb-endpoint-one-az
  claim: A Gateway Load Balancer endpoint uses only one Availability Zone (one subnet) that cannot be changed later; AWS recommends an endpoint in each Availability Zone you send traffic to.
  scope: Gateway Load Balancer endpoint.
  link: [You can choose only one Availability Zone](../facts/elb.md#elb-gwlb-endpoint-one-az)
  link: [endpoint in each Availability Zone](../facts/elb.md#elb-gwlb-endpoint-one-az)
elb-gwlb-endpoints-across-vpcs
  claim: Gateway Load Balancers use Gateway Load Balancer endpoints, which are VPC endpoints, to exchange traffic across VPC boundaries privately between the appliances in the service provider VPC and the application servers in the service consumer VPC.
  scope: Gateway Load Balancer.
  link: [Gateway Load Balancer endpoints](../facts/elb.md#elb-gwlb-endpoints-across-vpcs)
  link: [is a VPC endpoint](../facts/elb.md#elb-gwlb-endpoints-across-vpcs)
elb-gwlb-faq-3-or-2-tuple-for-control-data-apps
  claim: The default 5-tuple stickiness does not suit applications with separate control and data streams (FTP, Microsoft RDP, Windows RPC, SSL VPN); for them you enable 3-tuple (source IP, destination IP, IP protocol) or 2-tuple (source IP, destination IP) stickiness.
  scope: Gateway Load Balancer flow stickiness.
  link: [FTP, Microsoft RDP, Windows RPC and SSL VPN](../facts/elb.md#elb-gwlb-faq-3-or-2-tuple-for-control-data-apps)
  link: [3-tuple (source IP, destination IP, IP protocol)](../facts/elb.md#elb-gwlb-faq-3-or-2-tuple-for-control-data-apps)
  link: [2-tuple (source IP, destination IP)](../facts/elb.md#elb-gwlb-faq-3-or-2-tuple-for-control-data-apps)
elb-gwlb-faq-all-appliances-in-az-fail-drop
  claim: If all virtual appliances in an Availability Zone fail, the Gateway Load Balancer drops the network traffic; AWS recommends deploying Gateway Load Balancers in multiple AZs.
  scope: Gateway Load Balancer.
  link: [will drop the network traffic](../facts/elb.md#elb-gwlb-faq-all-appliances-in-az-fail-drop)
  link: [deploying Gateway Load Balancers in multiple AZs](../facts/elb.md#elb-gwlb-faq-all-appliances-in-az-fail-drop)
elb-gwlb-faq-appliance-shared-by-several-gwlbs
  claim: Multiple Gateway Load Balancers can point to the same set of virtual appliances.
  scope: Gateway Load Balancer.
  link: [multiple Gateway Load Balancers](../facts/elb.md#elb-gwlb-faq-appliance-shared-by-several-gwlbs)
  link: [same set of virtual appliances](../facts/elb.md#elb-gwlb-faq-appliance-shared-by-several-gwlbs)
elb-gwlb-faq-cross-zone-data-transfer-charged
  claim: With cross-zone load balancing enabled on a Gateway Load Balancer, you are charged for data transfer between Availability Zones.
  scope: Gateway Load Balancer cross-zone traffic.
  link: [charged for data transfer between Availability Zones](../facts/elb.md#elb-gwlb-faq-cross-zone-data-transfer-charged)
  link: [when cross-zone load balancing is enabled](../facts/elb.md#elb-gwlb-faq-cross-zone-data-transfer-charged)
elb-gwlb-faq-default-flow-5-tuple-both-directions
  claim: By default a Gateway Load Balancer defines a flow by the 5-tuple (source IP, destination IP, IP protocol, source port, destination port), and sends both directions of a flow to the same target.
  scope: Gateway Load Balancer flow; default; not adjustable.
  link: [a combination of a 5-tuple](../facts/elb.md#elb-gwlb-faq-default-flow-5-tuple-both-directions)
  link: [both directions of a flow](../facts/elb.md#elb-gwlb-faq-default-flow-5-tuple-both-directions)
elb-gwlb-faq-endpoint-centralize-appliances
  claim: With Gateway Load Balancer endpoints, appliances can live in different AWS accounts and VPCs, so they can be centralized in one location for easier management and less operational overhead.
  scope: Gateway Load Balancer endpoint.
  link: [can reside in different AWS accounts and VPCs](../facts/elb.md#elb-gwlb-faq-endpoint-centralize-appliances)
  link: [centralized in one location](../facts/elb.md#elb-gwlb-faq-endpoint-centralize-appliances)
elb-gwlb-faq-endpoint-privatelink-vpc-endpoint
  claim: A Gateway Load Balancer endpoint is a type of VPC endpoint that uses PrivateLink; traffic between the source and the Gateway Load Balancer flows over the AWS network and is never exposed to the internet.
  scope: Gateway Load Balancer endpoint.
  link: [VPC endpoint that uses PrivateLink technology](../facts/elb.md#elb-gwlb-faq-endpoint-privatelink-vpc-endpoint)
  link: [data is never exposed to the internet](../facts/elb.md#elb-gwlb-faq-endpoint-privatelink-vpc-endpoint)
elb-gwlb-faq-endpoint-secure-low-latency
  claim: Gateway Load Balancer endpoints create the secured, low-latency connections that traffic to and from virtual appliances needs.
  scope: Gateway Load Balancer endpoint.
  link: [create the secured, low-latency connections](../facts/elb.md#elb-gwlb-faq-endpoint-secure-low-latency)
  link: [must follow a secure connection](../facts/elb.md#elb-gwlb-faq-endpoint-secure-low-latency)
elb-gwlb-faq-endpoint-vs-interface-endpoint
  claim: A PrivateLink interface endpoint is paired with a Network Load Balancer to distribute TCP and UDP traffic destined for applications, while a Gateway Load Balancer endpoint is used with a Gateway Load Balancer to connect the source and destination of traffic through the virtual appliances.
  scope: Gateway Load Balancer endpoint.
  link: [paired with a Network Load Balancer (NLB)](../facts/elb.md#elb-gwlb-faq-endpoint-vs-interface-endpoint)
  link: [to connect the source and destination of traffic](../facts/elb.md#elb-gwlb-faq-endpoint-vs-interface-endpoint)
  link: [through the virtual appliances](../facts/elb.md#elb-gwlb-faq-endpoint-vs-interface-endpoint)
elb-gwlb-faq-endpoints-per-gwlb-recommend-50
  claim: There is no limit on how many Gateway Load Balancer endpoints can connect to a service that uses a Gateway Load Balancer, but AWS recommends no more than 50 endpoints per Gateway Load Balancer to reduce the impact of a failure.
  scope: per Gateway Load Balancer; maximum; not adjustable.
  link: [no limit on how many VPC Endpoints](../facts/elb.md#elb-gwlb-faq-endpoints-per-gwlb-recommend-50)
  link: [no more than 50 Gateway Load Balancer Endpoints](../facts/elb.md#elb-gwlb-faq-endpoints-per-gwlb-recommend-50)
elb-gwlb-faq-flow-stickiness-5-tuple-3-tuple
  claim: A Gateway Load Balancer keeps flow stickiness to one appliance using a 5-tuple for TCP/UDP flows or a 3-tuple for non-TCP/UDP flows.
  scope: Gateway Load Balancer.
  link: [5-tuple (for TCP/UDP flows)](../facts/elb.md#elb-gwlb-faq-flow-stickiness-5-tuple-3-tuple)
  link: [3-tuple (for non-TCP/UDP flows)](../facts/elb.md#elb-gwlb-faq-flow-stickiness-5-tuple-3-tuple)
elb-gwlb-faq-fragments
  claim: A Gateway Load Balancer does not fragment or reassemble packets: it forwards UDP fragments but drops TCP and ICMP fragments, because they lack the layer 4 header.
  scope: Gateway Load Balancer.
  link: [does not fragment or reassemble packets](../facts/elb.md#elb-gwlb-faq-fragments)
  link: [GWLB forwards UDP fragments](../facts/elb.md#elb-gwlb-faq-fragments)
  link: [GWLB drops TCP and ICMP fragments](../facts/elb.md#elb-gwlb-faq-fragments)
elb-gwlb-faq-ip-listener-only
  claim: A Gateway Load Balancer listens to all types of IP traffic (TCP, UDP, ICMP, GRE, ESP and others), so only an IP listener is created on it.
  scope: Gateway Load Balancer.
  link: [only IP listener is created](../facts/elb.md#elb-gwlb-faq-ip-listener-only)
  link: [listens to all types of IP traffic](../facts/elb.md#elb-gwlb-faq-ip-listener-only)
elb-gwlb-faq-layer3-gateway-layer4-bump-in-wire
  claim: A Gateway Load Balancer combines a Layer 3 gateway with Layer 4 load balancing, and is a transparent bump-in-the-wire device that does not change any part of the packet.
  scope: Gateway Load Balancer.
  link: [Layer 3 gateway and Layer 4 load balancing](../facts/elb.md#elb-gwlb-faq-layer3-gateway-layer4-bump-in-wire)
  link: [does not change any part of the packet](../facts/elb.md#elb-gwlb-faq-layer3-gateway-layer4-bump-in-wire)
  link: [transparent bump-in-the-wire device](../facts/elb.md#elb-gwlb-faq-layer3-gateway-layer4-bump-in-wire)
elb-gwlb-faq-no-tls-termination-no-app-state
  claim: A Gateway Load Balancer does not terminate TLS and does not maintain application state; the third-party virtual appliances behind it do that.
  scope: Gateway Load Balancer.
  link: [does not perform TLS termination](../facts/elb.md#elb-gwlb-faq-no-tls-termination-no-app-state)
  link: [does not maintain any application state](../facts/elb.md#elb-gwlb-faq-no-tls-termination-no-app-state)
  link: [performed by the third-party virtual appliances](../facts/elb.md#elb-gwlb-faq-no-tls-termination-no-app-state)
elb-gwlb-faq-one-appliance-fails-reroute
  claim: When a single virtual appliance instance fails, a Gateway Load Balancer removes it from the routing list and reroutes traffic to a healthy appliance instance.
  scope: Gateway Load Balancer.
  link: [removes it from the routing list](../facts/elb.md#elb-gwlb-faq-one-appliance-fails-reroute)
  link: [reroutes traffic to a healthy appliance instance](../facts/elb.md#elb-gwlb-faq-one-appliance-fails-reroute)
elb-gwlb-faq-pricing-hours-and-lcus
  claim: A Gateway Load Balancer is charged for each hour or partial hour it runs and for the LCUs it uses per hour; its LCU is set by the maximum resource consumed among new connections/flows, active connections/flows and bandwidth, and you are charged only on the highest of the three for the hour.
  scope: Gateway Load Balancer.
  link: [each hour or partial hour](../facts/elb.md#elb-gwlb-faq-pricing-hours-and-lcus)
  link: [new connections/flows, active connections/flows, and bandwidth](../facts/elb.md#elb-gwlb-faq-pricing-hours-and-lcus)
  link: [the highest for the hour](../facts/elb.md#elb-gwlb-faq-pricing-hours-and-lcus)
elb-gwlb-faq-single-az-or-multiple-azs
  claim: You can create a Gateway Load Balancer in a single Availability Zone with a single subnet, but AWS recommends multiple AZs, and you cannot add or remove Availability Zones after you create it.
  scope: Gateway Load Balancer.
  link: [You cannot add or remove availability zones](../facts/elb.md#elb-gwlb-faq-single-az-or-multiple-azs)
  link: [we recommend using multiple availability zones](../facts/elb.md#elb-gwlb-faq-single-az-or-multiple-azs)
elb-gwlb-faq-when-inline-appliances
  claim: Use a Gateway Load Balancer when deploying inline virtual appliances where the network traffic is not destined for the load balancer itself; it transparently passes all Layer 3 traffic through third-party virtual appliances and is invisible to the source and destination.
  scope: Gateway Load Balancer.
  link: [deploying inline virtual appliances](../facts/elb.md#elb-gwlb-faq-when-inline-appliances)
  link: [transparently passes all Layer 3 traffic](../facts/elb.md#elb-gwlb-faq-when-inline-appliances)
  link: [invisible to the source and destination](../facts/elb.md#elb-gwlb-faq-when-inline-appliances)
elb-gwlb-flow-stickiness-5-3-2-tuple
  claim: By default a Gateway Load Balancer keeps flows on one appliance using a 5-tuple; the stickiness type can be changed to a 3-tuple or 2-tuple, and 2-tuple and 3-tuple are not supported with Transit Gateway appliance mode.
  scope: Gateway Load Balancer target group; default; adjustable.
  link: [using 5-tuple (for TCP/UDP flows)](../facts/elb.md#elb-gwlb-flow-stickiness-5-3-2-tuple)
  link: [either 3-tuple](../facts/elb.md#elb-gwlb-flow-stickiness-5-3-2-tuple)
  link: [AWS Transit Gateway appliance mode](../facts/elb.md#elb-gwlb-flow-stickiness-5-3-2-tuple)
elb-gwlb-glcu-600-new-60000-active-1-gb
  claim: One Gateway Load Balancer GLCU includes 600 new connections or flows per second, 60,000 active connections or flows sampled per minute, and 1 GB per hour of processed bytes.
  scope: per GLCU.
  link: [600 new connections/flows per second](../facts/elb.md#elb-gwlb-glcu-600-new-60000-active-1-gb)
  link: [60,000 active connections/flows](../facts/elb.md#elb-gwlb-glcu-600-new-60000-active-1-gb)
  link: [1 GB per hour](../facts/elb.md#elb-gwlb-glcu-600-new-60000-active-1-gb)
  say: six hundred new flows per second | sixty thousand active flows | one gigabyte per hour
elb-gwlb-health-check-interval-default-10-seconds
  claim: The Gateway Load Balancer health check interval can be 5 to 300 seconds with a default of 10 seconds, and it must be greater than or equal to the health check timeout.
  scope: per Gateway Load Balancer target group; default; adjustable.
  link: [10 seconds](../facts/elb.md#elb-gwlb-health-check-interval-default-10-seconds)
  link: [5 to 300](../facts/elb.md#elb-gwlb-health-check-interval-default-10-seconds)
  say: ten seconds | five to three hundred
elb-gwlb-health-check-port-default-80
  claim: The Gateway Load Balancer health check port can be 1 to 65535; the default is 80.
  scope: per Gateway Load Balancer target group; default; adjustable.
  link: [The default is 80](../facts/elb.md#elb-gwlb-health-check-port-default-80)
  link: [1 to 65535](../facts/elb.md#elb-gwlb-health-check-port-default-80)
  say: the default is eighty | one to sixty-five thousand five hundred thirty-five
elb-gwlb-health-check-protocol-default-tcp
  claim: Gateway Load Balancer health checks can use HTTP, HTTPS or TCP; the default is TCP.
  scope: per Gateway Load Balancer target group; default; adjustable.
  link: [The default is TCP](../facts/elb.md#elb-gwlb-health-check-protocol-default-tcp)
  link: [HTTP, HTTPS, and TCP](../facts/elb.md#elb-gwlb-health-check-protocol-default-tcp)
  say: the default is TCP | HTTP, HTTPS and TCP
elb-gwlb-health-check-success-codes-200-399
  claim: For HTTP or HTTPS health checks, the Gateway Load Balancer success codes must be 200-399.
  scope: per Gateway Load Balancer target group; fixed; HTTP or HTTPS health checks.
  link: [This value must be 200-399](../facts/elb.md#elb-gwlb-health-check-success-codes-200-399)
  link: [200-399](../facts/elb.md#elb-gwlb-health-check-success-codes-200-399)
  say: it must be two hundred to three ninety-nine | two hundred to three ninety-nine
elb-gwlb-health-check-timeout-default-5
  claim: The Gateway Load Balancer health check timeout can be 2 to 120 seconds; the default is 5.
  scope: per Gateway Load Balancer target group; default; adjustable.
  link: [The default is 5](../facts/elb.md#elb-gwlb-health-check-timeout-default-5)
  link: [2 to 120](../facts/elb.md#elb-gwlb-health-check-timeout-default-5)
  say: the default is five | two to one hundred twenty
elb-gwlb-idle-timeout-only-5-tuple
  claim: A Gateway Load Balancer idle timeout can only be updated when the target group uses 5-tuple stickiness; with 3-tuple or 2-tuple stickiness the default idle timeout is used.
  scope: per Gateway Load Balancer.
  link: [5-tuple stickiness](../facts/elb.md#elb-gwlb-idle-timeout-only-5-tuple)
  link: [can only be updated](../facts/elb.md#elb-gwlb-idle-timeout-only-5-tuple)
  say: five-tuple stickiness | can only be updated
elb-gwlb-layer-3-all-ports
  claim: A Gateway Load Balancer operates at the third layer of the OSI model, the network layer; it listens for all IP packets across all ports and forwards traffic to the target group with the GENEVE protocol on port 6081.
  scope: Gateway Load Balancer.
  link: [operates at the third layer](../facts/elb.md#elb-gwlb-layer-3-all-ports)
  link: [listens for all IP packets across all ports](../facts/elb.md#elb-gwlb-layer-3-all-ports)
  link: [GENEVE protocol on port 6081](../facts/elb.md#elb-gwlb-layer-3-all-ports)
elb-gwlb-listener-no-protocol-port
  claim: A Gateway Load Balancer listener listens for all IP packets on all ports, and you cannot specify a protocol or port when you create it.
  scope: Gateway Load Balancer listener.
  link: [You cannot specify a protocol or port](../facts/elb.md#elb-gwlb-listener-no-protocol-port)
elb-gwlb-mtu-8500-bytes
  claim: The Gateway Load Balancer interface MTU supports packets up to 8,500 bytes and drops larger packets; GENEVE encapsulation adds 68 bytes, so appliances need an MTU of at least 8,568 bytes.
  scope: per Gateway Load Balancer interface; maximum; not adjustable.
  link: [8,500 bytes](../facts/elb.md#elb-gwlb-mtu-8500-bytes)
  link: [68 bytes](../facts/elb.md#elb-gwlb-mtu-8500-bytes)
  link: [8,568 bytes](../facts/elb.md#elb-gwlb-mtu-8500-bytes)
  say: eight thousand five hundred bytes | sixty-eight bytes | eight thousand five hundred sixty-eight bytes
elb-gwlb-no-security-groups
  claim: Gateway Load Balancers do not have associated security groups, so the security groups of the targets must use IP addresses to allow traffic from the load balancer; when you register EC2 instances as targets, their security groups must allow inbound and outbound traffic on port 6081.
  scope: Gateway Load Balancer; port 6081 rule stated for EC2 instances registered as targets.
  link: [do not have associated security groups](../facts/elb.md#elb-gwlb-no-security-groups)
  link: [must use IP addresses to allow traffic](../facts/elb.md#elb-gwlb-no-security-groups)
  link: [inbound and outbound traffic on port 6081](../facts/elb.md#elb-gwlb-no-security-groups)
elb-gwlb-one-eni-per-zone
  claim: Each Gateway Load Balancer uses one network interface per zone.
  scope: per Gateway Load Balancer.
  link: [one network interface per zone](../facts/elb.md#elb-gwlb-one-eni-per-zone)
  link: [Each Gateway Load Balancer uses](../facts/elb.md#elb-gwlb-one-eni-per-zone)
  say: one network interface per zone | each Gateway Load Balancer uses
elb-gwlb-quota-enis-per-vpc
  claim: The default quota is 300 Gateway Load Balancer ENIs per VPC; the quota is adjustable.
  scope: per VPC; default; adjustable.
  link: [300 Gateway Load Balancer ENIs](../facts/elb.md#elb-gwlb-quota-enis-per-vpc)
  say: three hundred Gateway Load Balancer ENIs
elb-gwlb-quota-geneve-target-groups-per-region
  claim: The default quota is 100 GENEVE target groups per Region; the quota is adjustable.
  scope: per Region, per account; default; adjustable.
  link: [100 GENEVE target groups](../facts/elb.md#elb-gwlb-quota-geneve-target-groups-per-region)
  say: one hundred GENEVE target groups
elb-gwlb-quota-listeners-per-lb
  claim: A Gateway Load Balancer can have 1 listener; this quota is not adjustable.
  scope: per Gateway Load Balancer; maximum; not adjustable.
  link: [1 listener](../facts/elb.md#elb-gwlb-quota-listeners-per-lb)
  say: one listener
elb-gwlb-quota-load-balancers-per-region
  claim: The default quota is 100 Gateway Load Balancers per Region; the quota is adjustable.
  scope: per Region, per account; default; adjustable.
  link: [100 Gateway Load Balancers](../facts/elb.md#elb-gwlb-quota-load-balancers-per-region)
  say: one hundred Gateway Load Balancers
elb-gwlb-quota-load-balancers-per-vpc
  claim: The default quota is 100 Gateway Load Balancers per VPC; the quota is adjustable.
  scope: per VPC; default; adjustable.
  link: [100 Gateway Load Balancers](../facts/elb.md#elb-gwlb-quota-load-balancers-per-vpc)
  say: one hundred Gateway Load Balancers
elb-gwlb-quota-reserved-lcus-per-region
  claim: The default quota for reserved Gateway Load Balancer LCUs per Region is 0; the quota is adjustable.
  scope: per Region, per account; default; adjustable.
  link: [LCUs per Region is 0](../facts/elb.md#elb-gwlb-quota-reserved-lcus-per-region)
  say: zero reserved LCUs per Region
elb-gwlb-quota-targets-per-az-per-lb
  claim: A Gateway Load Balancer can have at most 300 targets per Availability Zone; this quota is not adjustable.
  scope: per Availability Zone, per Gateway Load Balancer; maximum; not adjustable.
  link: [300 targets per Availability Zone](../facts/elb.md#elb-gwlb-quota-targets-per-az-per-lb)
  say: three hundred targets per Availability Zone
elb-gwlb-quota-targets-per-az-per-target-group
  claim: A GENEVE target group can have at most 300 targets per Availability Zone; this quota is not adjustable.
  scope: per Availability Zone, per GENEVE target group; maximum; not adjustable.
  link: [300 targets per Availability Zone](../facts/elb.md#elb-gwlb-quota-targets-per-az-per-target-group)
  say: three hundred targets per Availability Zone
elb-gwlb-quota-targets-per-lb
  claim: A Gateway Load Balancer can have at most 300 targets; this quota is not adjustable.
  scope: per Gateway Load Balancer; maximum; not adjustable.
  link: [300 targets](../facts/elb.md#elb-gwlb-quota-targets-per-lb)
  say: three hundred targets
elb-gwlb-target-failover-default-no-rebalance
  claim: By default (no_rebalance), a Gateway Load Balancer keeps sending existing flows to a target that has failed or been deregistered, while new flows go to healthy targets; with rebalance it rehashes existing flows to healthy targets after the deregistration delay.
  scope: Gateway Load Balancer target group; default; adjustable.
  link: [send existing flows to the same target](../facts/elb.md#elb-gwlb-target-failover-default-no-rebalance)
  link: [new flows are sent to healthy targets](../facts/elb.md#elb-gwlb-target-failover-default-no-rebalance)
  link: [rehashes existing flows](../facts/elb.md#elb-gwlb-target-failover-default-no-rebalance)
elb-gwlb-target-types-instance-ip
  claim: A Gateway Load Balancer target group has the target type instance or ip, and the target type cannot be changed after creation.
  scope: Gateway Load Balancer target group.
  link: [The targets are specified by instance ID](../facts/elb.md#elb-gwlb-target-types-instance-ip)
  link: [The targets are specified by IP address](../facts/elb.md#elb-gwlb-target-types-instance-ip)
  link: [you cannot change its target type](../facts/elb.md#elb-gwlb-target-types-instance-ip)
elb-gwlb-tcp-idle-timeout-default-350-seconds
  claim: The TCP idle timeout of a Gateway Load Balancer is 350 seconds by default and can be updated to any value between 60 and 6000 seconds.
  scope: per Gateway Load Balancer listener; default; adjustable.
  link: [350 seconds](../facts/elb.md#elb-gwlb-tcp-idle-timeout-default-350-seconds)
  link: [60-6000 seconds](../facts/elb.md#elb-gwlb-tcp-idle-timeout-default-350-seconds)
  say: three hundred fifty seconds | sixty to six thousand seconds
elb-gwlb-udp-idle-timeout-fixed-120-seconds
  claim: Elastic Load Balancing sets the idle timeout for UDP flows on a Gateway Load Balancer to 120 seconds, and this value cannot be changed.
  scope: per UDP flow on a Gateway Load Balancer; fixed.
  link: [120 seconds](../facts/elb.md#elb-gwlb-udp-idle-timeout-fixed-120-seconds)
  link: [This cannot be changed](../facts/elb.md#elb-gwlb-udp-idle-timeout-fixed-120-seconds)
  say: one hundred twenty seconds | this cannot be changed
elb-gwlb-virtual-appliances
  claim: Gateway Load Balancers let you deploy, scale and manage virtual appliances such as firewalls, intrusion detection and prevention systems, and deep packet inspection systems; a GWLB combines a transparent network gateway with load distribution.
  scope: Gateway Load Balancer.
  link: [deploy, scale, and manage virtual appliances](../facts/elb.md#elb-gwlb-virtual-appliances)
  link: [such as firewalls](../facts/elb.md#elb-gwlb-virtual-appliances)
  link: [a transparent network gateway](../facts/elb.md#elb-gwlb-virtual-appliances)
elb-health-checks-per-target-group
  claim: On Application Load Balancers and Network Load Balancers, health check settings are defined per target group; each target group uses the default health check settings unless you override them at creation or modify them later.
  scope: Application and Network Load Balancer target groups.
  link: [on a per target group basis](../facts/elb.md#elb-health-checks-per-target-group)
  link: [uses the default health check settings](../facts/elb.md#elb-health-checks-per-target-group)
elb-internal-nodes-private-ips-only
  claim: The nodes of an internal load balancer have only private IP addresses, so an internal load balancer can route requests only from clients that have access to its VPC; its DNS name is still publicly resolvable to those private addresses.
  scope: internal load balancer.
  link: [have only private IP addresses](../facts/elb.md#elb-internal-nodes-private-ips-only)
  link: [clients with access to the VPC](../facts/elb.md#elb-internal-nodes-private-ips-only)
  link: [publicly resolvable to the private IP addresses](../facts/elb.md#elb-internal-nodes-private-ips-only)
elb-internet-facing-nodes-public-ips
  claim: The nodes of an internet-facing load balancer have public IP addresses, and its DNS name resolves publicly to those addresses, so it can route requests from clients over the internet.
  scope: internet-facing load balancer.
  link: [have public IP addresses](../facts/elb.md#elb-internet-facing-nodes-public-ips)
  link: [route requests from clients over the internet](../facts/elb.md#elb-internet-facing-nodes-public-ips)
elb-ip-target-any-private-ip-same-port
  claim: On Application Load Balancers and Network Load Balancers, instance-ID targets receive traffic on the primary private IP address of the primary network interface; IP targets can use any private IP address of one or more network interfaces, which lets several applications on one instance use the same port.
  scope: Application and Network Load Balancer instance and ip targets.
  link: [primary private IP address](../facts/elb.md#elb-ip-target-any-private-ip-same-port)
  link: [to use the same port](../facts/elb.md#elb-ip-target-any-private-ip-same-port)
elb-ip-targets-no-public-addresses
  claim: With the ip target type you cannot specify publicly routable IP addresses; the addresses must come from the subnets of the target group VPC or from a listed set of private CIDR blocks.
  scope: ip target type (ALB and NLB).
  link: [You can't specify publicly routable IP addresses](../facts/elb.md#elb-ip-targets-no-public-addresses)
elb-ip-targets-peered-vpc-and-on-premises
  claim: With ip targets an Application Load Balancer can send traffic to instances in a peered VPC (same or different Region), to AWS resources addressable by IP and port, and to on-premises resources linked through Direct Connect or Site-to-Site VPN.
  scope: ip target type; target type ip.
  link: [Instances in a VPC that is peered](../facts/elb.md#elb-ip-targets-peered-vpc-and-on-premises)
  link: [On-premises resources linked to AWS](../facts/elb.md#elb-ip-targets-peered-vpc-and-on-premises)
  link: [through Direct Connect or a Site-to-Site VPN connection](../facts/elb.md#elb-ip-targets-peered-vpc-and-on-premises)
elb-ip-type-nlb-no-dualstack-without-public-ipv4
  claim: A Network Load Balancer supports IPv4 only and dualstack, but not dualstack without public IPv4.
  scope: Network Load Balancer.
  link: [Network Load Balancer](../facts/elb.md#elb-ip-type-nlb-no-dualstack-without-public-ipv4)
  link: [No](../facts/elb.md#elb-ip-type-nlb-no-dualstack-without-public-ipv4)
elb-ip-type-support-alb
  claim: An Application Load Balancer supports the IP address types IPv4 only, dualstack, and dualstack without public IPv4.
  scope: Application Load Balancer.
  link: [Application Load Balancer](../facts/elb.md#elb-ip-type-support-alb)
  link: [Yes](../facts/elb.md#elb-ip-type-support-alb)
elb-ipv6-target-group-needs-dualstack-lb
  claim: An IPv6 target group holds targets registered with IPv6 addresses and must be used with a dualstack load balancer.
  scope: IPv6 target group.
  link: [used with a dualstack load balancer](../facts/elb.md#elb-ipv6-target-group-needs-dualstack-lb)
  link: [register targets with IPv6 addresses](../facts/elb.md#elb-ipv6-target-group-needs-dualstack-lb)
elb-lambda-target-alb-only
  claim: Network Load Balancers do not support the lambda target type; Application Load Balancers are the only load balancers that support it.
  scope: lambda target type.
  link: [do not support the `lambda` target type](../facts/elb.md#elb-lambda-target-alb-only)
  link: [the only load balancers that support](../facts/elb.md#elb-lambda-target-alb-only)
elb-lambda-target-body-max-1-mb
  claim: With a Lambda function as an Application Load Balancer target, the request body sent to the function and the response JSON from the function can each be at most 1 MB.
  scope: per request and per response, Lambda target of an Application Load Balancer; maximum; not adjustable.
  link: [1 MB](../facts/elb.md#elb-lambda-target-body-max-1-mb)
  say: one megabyte
elb-lcu-charged-on-highest-dimension
  claim: Elastic Load Balancing charges capacity units only on the dimension with the highest usage, not on every dimension.
  scope: per load balancer, per hour.
  link: [dimension with the highest usage](../facts/elb.md#elb-lcu-charged-on-highest-dimension)
  link: [You are charged only on](../facts/elb.md#elb-lcu-charged-on-highest-dimension)
  say: the dimension with the highest usage | you are charged only on
elb-lcu-reservation-billing
  claim: With an LCU reservation, an Application Load Balancer is charged for its running hours, for the reserved LCUs per minute, and for any LCUs used per minute beyond the reservation.
  scope: per Application Load Balancer with LCU reservation.
  link: [reserved per minute](../facts/elb.md#elb-lcu-reservation-billing)
  link: [beyond your reserved LCUs](../facts/elb.md#elb-lcu-reservation-billing)
  say: reserved per minute | beyond your reserved LCUs
elb-lcu-reservation-static-minimum-capacity
  claim: An LCU reservation reserves a static minimum capacity for a load balancer, for example before an event with a sudden, unusually high traffic spike; the load balancer still scales up and down above that minimum.
  scope: Application, Network and Gateway Load Balancers.
  link: [reserve a static minimum capacity](../facts/elb.md#elb-lcu-reservation-static-minimum-capacity)
  link: [an upcoming event that will have a sudden](../facts/elb.md#elb-lcu-reservation-static-minimum-capacity)
  link: [continues scaling up or down](../facts/elb.md#elb-lcu-reservation-static-minimum-capacity)
elb-listener-checks-connection-requests
  claim: A listener is a process that checks for connection requests; it is configured with a protocol and a port for connections from clients to the load balancer.
  scope: listener.
  link: [a process that checks for connection requests](../facts/elb.md#elb-listener-checks-connection-requests)
  link: [configured with a protocol and port number](../facts/elb.md#elb-listener-checks-connection-requests)
elb-metrics-60-second-intervals
  claim: When requests flow through a load balancer, Elastic Load Balancing measures and sends its CloudWatch metrics in 60-second intervals.
  scope: per load balancer; only when requests flow through the load balancer.
  link: [60-second intervals](../facts/elb.md#elb-metrics-60-second-intervals)
  link: [If there are requests flowing](../facts/elb.md#elb-metrics-60-second-intervals)
  say: sixty-second intervals | if there are requests flowing
elb-multi-tier-internet-facing-plus-internal
  claim: A multi-tier application can use an internet-facing load balancer for the web servers and an internal load balancer for the application servers, and the web servers send their requests for the application tier to the internal load balancer.
  scope: multi-tier application.
  link: [register the web servers with it](../facts/elb.md#elb-multi-tier-internet-facing-plus-internal)
  link: [register the application servers with it](../facts/elb.md#elb-multi-tier-internet-facing-plus-internal)
  link: [both internal and internet-facing load balancers](../facts/elb.md#elb-multi-tier-internet-facing-plus-internal)
elb-new-target-after-first-health-check
  claim: On Application Load Balancers and Network Load Balancers, the load balancer starts routing to a newly registered target as soon as registration completes and the target passes the first initial health check, irrespective of the configured threshold.
  scope: newly registered target, Application and Network Load Balancers.
  link: [passes the first initial health check](../facts/elb.md#elb-new-target-after-first-health-check)
  link: [irrespective of the configured threshold](../facts/elb.md#elb-new-target-after-first-health-check)
elb-nlb-access-logs-sse-s3-or-kms
  claim: For Network Load Balancer access logs, the S3 bucket can use SSE-S3 or SSE-KMS with a customer managed key, and each log file is encrypted before it is stored.
  scope: Network Load Balancer access logs bucket.
  link: [Amazon S3-managed encryption keys (SSE-S3)](../facts/elb.md#elb-nlb-access-logs-sse-s3-or-kms)
  link: [(SSE-KMS CMK)](../facts/elb.md#elb-nlb-access-logs-sse-s3-or-kms)
elb-nlb-access-logs-tls-only
  claim: Network Load Balancer access logs are created only if the load balancer has a TLS listener, and they contain information about TLS requests only.
  scope: Network Load Balancer access logs.
  link: [if the load balancer has a TLS listener](../facts/elb.md#elb-nlb-access-logs-tls-only)
  link: [information about TLS requests only](../facts/elb.md#elb-nlb-access-logs-tls-only)
elb-nlb-alb-target-combines-features
  claim: With an Application Load Balancer as the target of a Network Load Balancer, the ALB takes over the load balancing decision, so you combine ALB layer 7 request routing with NLB features such as PrivateLink endpoint services and static IP addresses.
  scope: Network Load Balancer with alb target type.
  link: [takes over the load balancing decision](../facts/elb.md#elb-nlb-alb-target-combines-features)
  link: [layer 7 request-based routing](../facts/elb.md#elb-nlb-alb-target-combines-features)
  link: [endpoint services (AWS PrivateLink) and static IP addresses](../facts/elb.md#elb-nlb-alb-target-combines-features)
elb-nlb-alb-target-same-vpc-same-account
  claim: To register an Application Load Balancer as a target of a Network Load Balancer, both load balancers must be in the same VPC in the same account.
  scope: Elastic Load Balancing.
  link: [in the same VPC](../facts/elb.md#elb-nlb-alb-target-same-vpc-same-account)
  link: [within the same account](../facts/elb.md#elb-nlb-alb-target-same-vpc-same-account)
elb-nlb-alb-target-static-ip-privatelink
  claim: To give Application Load Balancer layer 7 routing a static IP address or AWS PrivateLink, you forward traffic from a Network Load Balancer to an Application Load Balancer-type target group that holds the Application Load Balancer.
  scope: Elastic Load Balancing.
  link: [static IP addresses](../facts/elb.md#elb-nlb-alb-target-static-ip-privatelink)
  link: [endpoint services (AWS PrivateLink)](../facts/elb.md#elb-nlb-alb-target-static-ip-privatelink)
  link: [forward traffic from your Network Load Balancer](../facts/elb.md#elb-nlb-alb-target-static-ip-privatelink)
elb-nlb-alb-target-up-to-two-nlbs
  claim: One Application Load Balancer can be the target of up to two Network Load Balancers, with a separate target group for each Network Load Balancer.
  scope: per Application Load Balancer; maximum; not adjustable.
  link: [up to two Network Load Balancers](../facts/elb.md#elb-nlb-alb-target-up-to-two-nlbs)
elb-nlb-at-least-one-az
  claim: When you create a Network Load Balancer, you select at least one Availability Zone and one subnet per zone.
  scope: Network Load Balancer; minimum.
  link: [select at least one Availability Zone](../facts/elb.md#elb-nlb-at-least-one-az)
  link: [select one subnet per zone](../facts/elb.md#elb-nlb-at-least-one-az)
elb-nlb-client-ip-disabled-source-is-nlb
  claim: A Network Load Balancer can preserve client source IP addresses; when client IP preservation is disabled, the source IP that targets see is the private IP address of the Network Load Balancer.
  scope: Network Load Balancer.
  link: [can preserve the source IP addresses of clients](../facts/elb.md#elb-nlb-client-ip-disabled-source-is-nlb)
  link: [private IP address of the Network Load Balancer](../facts/elb.md#elb-nlb-client-ip-disabled-source-is-nlb)
elb-nlb-client-ip-not-via-tgw-gwlbe
  claim: NLB client IP preservation is not supported when targets are reached through a transit gateway, and it has no effect on inbound AWS PrivateLink traffic, whose source is always the NLB private IP address.
  scope: Network Load Balancer client IP preservation.
  link: [reached through a transit gateway](../facts/elb.md#elb-nlb-client-ip-not-via-tgw-gwlbe)
  link: [no effect on inbound traffic from AWS PrivateLink](../facts/elb.md#elb-nlb-client-ip-not-via-tgw-gwlbe)
elb-nlb-client-ip-preservation-defaults
  claim: Client IP preservation on a Network Load Balancer is disabled by default for IP-type target groups with TCP or TLS and enabled otherwise; it cannot be disabled for UDP, TCP_UDP, QUIC and TCP_QUIC target groups.
  scope: Network Load Balancer target group; default; adjustable; TCP and TLS target groups can change it.
  link: [The default is disabled](../facts/elb.md#elb-nlb-client-ip-preservation-defaults)
  link: [Otherwise, the default is enabled](../facts/elb.md#elb-nlb-client-ip-preservation-defaults)
  link: [can't be disabled for UDP](../facts/elb.md#elb-nlb-client-ip-preservation-defaults)
elb-nlb-cross-zone-500-targets-per-lb
  claim: If cross-zone load balancing is enabled on a Network Load Balancer, the maximum is 500 targets per load balancer, regardless of the number of Availability Zones.
  scope: per Network Load Balancer; maximum; not adjustable; cross-zone load balancing enabled.
  link: [500 targets per load balancer](../facts/elb.md#elb-nlb-cross-zone-500-targets-per-lb)
  say: five hundred targets per load balancer
elb-nlb-cross-zone-lb-and-tg-level
  claim: On a Network Load Balancer, cross-zone load balancing is off by default at the load balancer level and can be turned on at any time; target groups use the load balancer setting by default but can turn it on or off explicitly.
  scope: Network Load Balancer and its target groups; default; adjustable.
  link: [off by default at the load balancer level](../facts/elb.md#elb-nlb-cross-zone-lb-and-tg-level)
  link: [on or off at the target group level](../facts/elb.md#elb-nlb-cross-zone-lb-and-tg-level)
elb-nlb-dereg-recommend-120-seconds
  claim: On a Network Load Balancer, a deregistering target changes to unused after 300 seconds by default; you can change this deregistration delay, and AWS recommends a value of at least 120 seconds so that requests complete. For QUIC traffic the value is always 300 seconds and can't be adjusted.
  scope: per Network Load Balancer target group; default; not adjustable for QUIC traffic (always 300 seconds).
  link: [300 seconds](../facts/elb.md#elb-nlb-dereg-recommend-120-seconds)
  link: [at least 120 seconds](../facts/elb.md#elb-nlb-dereg-recommend-120-seconds)
  say: three hundred seconds | at least one hundred twenty seconds
elb-nlb-drops-unintended-traffic
  claim: Network traffic that does not match a configured listener is unintended traffic, and a Network Load Balancer drops it without forwarding it to any target.
  scope: Network Load Balancer.
  link: [drop unintended traffic without forwarding it](../facts/elb.md#elb-nlb-drops-unintended-traffic)
  link: [classified as unintended traffic](../facts/elb.md#elb-nlb-drops-unintended-traffic)
elb-nlb-ec2-return-path-30-seconds
  claim: EC2 instances behind a Network Load Balancer must respond to a new request within 30 seconds to establish a return path.
  scope: per new request to an EC2 target; maximum; not adjustable.
  link: [within 30 seconds](../facts/elb.md#elb-nlb-ec2-return-path-30-seconds)
  say: within thirty seconds
elb-nlb-enable-disable-az-any-time
  claim: You can enable or disable the Availability Zones of a Network Load Balancer at any time; removing a subnet deletes its network interface and terminates all active connections in that Availability Zone.
  scope: Network Load Balancer.
  link: [enable or disable the Availability Zones](../facts/elb.md#elb-nlb-enable-disable-az-any-time)
  link: [its associated Elastic Network Interface (ENI) is deleted](../facts/elb.md#elb-nlb-enable-disable-az-any-time)
  link: [all active connections in the Availability Zone](../facts/elb.md#elb-nlb-enable-disable-az-any-time)
elb-nlb-faq-cross-zone-regional-data-transfer-charged
  claim: With cross-zone load balancing enabled on a Network Load Balancer, you are charged for regional data transfer between Availability Zones.
  scope: Network Load Balancer cross-zone traffic.
  link: [charged for regional data transfer between Availability Zones](../facts/elb.md#elb-nlb-faq-cross-zone-regional-data-transfer-charged)
  link: [when cross-zone load balancing is enabled](../facts/elb.md#elb-nlb-faq-cross-zone-regional-data-transfer-charged)
elb-nlb-faq-eip-returned-on-delete
  claim: When you delete a Network Load Balancer, its Elastic IP addresses return to your allocated pool and are available for future use.
  scope: Network Load Balancer.
  link: [will return to your allocated pool](../facts/elb.md#elb-nlb-faq-eip-returned-on-delete)
  link: [be available for future use](../facts/elb.md#elb-nlb-faq-eip-returned-on-delete)
elb-nlb-faq-internal-or-internet-facing
  claim: A Network Load Balancer can be internet-facing or internal, like an Application Load Balancer.
  scope: Network Load Balancer.
  link: [internet-facing load balancer or an internal load balancer](../facts/elb.md#elb-nlb-faq-internal-or-internet-facing)
  link: [what is possible with Application Load Balancer](../facts/elb.md#elb-nlb-faq-internal-or-internet-facing)
elb-nlb-faq-ip-targets-container-security-groups-same-port
  claim: Registering containers by IP address instead of instance ID lets each container have its own security group, and lets several containers on one instance use the same port (for example port 80).
  scope: load balancer IP targets for containers.
  link: [can now have its own security group](../facts/elb.md#elb-nlb-faq-ip-targets-container-security-groups-same-port)
  link: [use the same port (say port 80)](../facts/elb.md#elb-nlb-faq-ip-targets-container-security-groups-same-port)
elb-nlb-faq-key-features
  claim: A Network Load Balancer supports TLS termination, preserves the client source IP, provides stable IP support and zonal isolation, and supports long-running connections useful for WebSocket-type applications.
  scope: Network Load Balancer.
  link: [preserves the source IP of the clients](../facts/elb.md#elb-nlb-faq-key-features)
  link: [provides stable IP support and zonal isolation](../facts/elb.md#elb-nlb-faq-key-features)
  link: [supports long-running connections](../facts/elb.md#elb-nlb-faq-key-features)
elb-nlb-faq-millions-rps-low-latency
  claim: A Network Load Balancer is architected to handle millions of requests per second and sudden volatile traffic patterns, with extremely low latencies.
  scope: Network Load Balancer.
  link: [millions of requests per second](../facts/elb.md#elb-nlb-faq-millions-rps-low-latency)
  link: [extremely low latencies](../facts/elb.md#elb-nlb-faq-millions-rps-low-latency)
  link: [sudden volatile traffic patterns](../facts/elb.md#elb-nlb-faq-millions-rps-low-latency)
elb-nlb-faq-no-backend-server-authentication
  claim: A Network Load Balancer does not support back-end server authentication; only encryption to the back ends is supported.
  scope: Network Load Balancer.
  link: [only encryption is supported to the back-ends](../facts/elb.md#elb-nlb-faq-no-backend-server-authentication)
elb-nlb-faq-no-mix-eip-and-elb-ips
  claim: A Network Load Balancer cannot mix ELB-provided IPs with Elastic IPs or assigned private IPs: its addresses are either completely controlled by you or completely controlled by ELB, so the addresses known to clients do not change.
  scope: Network Load Balancer.
  link: [must be completely controlled by you](../facts/elb.md#elb-nlb-faq-no-mix-eip-and-elb-ips)
  link: [addresses known to your clients do not change](../facts/elb.md#elb-nlb-faq-no-mix-eip-and-elb-ips)
elb-nlb-faq-one-public-ip-per-subnet
  claim: A Network Load Balancer supports only a single public (internet-facing) IP address per associated subnet, so you cannot assign more than one Elastic IP per subnet.
  scope: Network Load Balancer, per subnet; maximum.
  link: [a single public/internet facing IP address](../facts/elb.md#elb-nlb-faq-one-public-ip-per-subnet)
  link: [For each associated subnet](../facts/elb.md#elb-nlb-faq-one-public-ip-per-subnet)
elb-nlb-faq-pricing-hours-and-lcus
  claim: A Network Load Balancer is charged for each hour or partial hour it runs and for the number of LCUs it uses per hour; an LCU is set by the maximum resource consumed among new connections/flows, active connections/flows and bandwidth.
  scope: Network Load Balancer.
  link: [each hour or partial hour](../facts/elb.md#elb-nlb-faq-pricing-hours-and-lcus)
  link: [new connections/flows, active connections/flows, and bandwidth](../facts/elb.md#elb-nlb-faq-pricing-hours-and-lcus)
elb-nlb-faq-privatelink-tcp-tls-not-udp
  claim: Network Load Balancers with TCP and TLS listeners can be used to set up AWS PrivateLink; PrivateLink cannot be set up with UDP listeners.
  scope: Network Load Balancer.
  link: [TCP and TLS Listeners can be used](../facts/elb.md#elb-nlb-faq-privatelink-tcp-tls-not-udp)
  link: [You cannot set up PrivateLink with UDP listeners](../facts/elb.md#elb-nlb-faq-privatelink-tcp-tls-not-udp)
elb-nlb-faq-route53-dns-failover
  claim: Route 53 health checks and DNS failover improve the availability of applications behind Network Load Balancers: with a multi-AZ load balancer, Route 53 fails away from an Availability Zone with no healthy instances or unhealthy load balancer nodes, and you can designate alternate load balancers for failover across Regions.
  scope: Network Load Balancer.
  link: [Route 53 health checking and DNS failover](../facts/elb.md#elb-nlb-faq-route53-dns-failover)
  link: [designate alternate load balancers for failover across regions](../facts/elb.md#elb-nlb-faq-route53-dns-failover)
  link: [fail away to alternate load balancer nodes](../facts/elb.md#elb-nlb-faq-route53-dns-failover)
elb-nlb-faq-single-az-one-subnet
  claim: You can create a Network Load Balancer in a single Availability Zone by providing a single subnet when you create it.
  scope: Network Load Balancer.
  link: [in a single AZ](../facts/elb.md#elb-nlb-faq-single-az-one-subnet)
  link: [by providing a single subnet](../facts/elb.md#elb-nlb-faq-single-az-one-subnet)
elb-nlb-faq-source-ip-and-static-ip-vs-classic
  claim: A Network Load Balancer preserves the source IP of the client, which a Classic Load Balancer does not preserve, and automatically provides a static IP per Availability Zone, with the option to assign an Elastic IP to the load balancer per Availability Zone.
  scope: Network Load Balancer.
  link: [preserves the source IP of the client](../facts/elb.md#elb-nlb-faq-source-ip-and-static-ip-vs-classic)
  link: [a static IP per Availability Zone (AZ)](../facts/elb.md#elb-nlb-faq-source-ip-and-static-ip-vs-classic)
  link: [Elastic IP to the load balancer per AZ](../facts/elb.md#elb-nlb-faq-source-ip-and-static-ip-vs-classic)
elb-nlb-faq-source-ip-preserved-with-tls
  claim: A Network Load Balancer keeps preserving the client source IP even when it terminates TLS.
  scope: Network Load Balancer TLS listener.
  link: [Source IP continues to be preserved](../facts/elb.md#elb-nlb-faq-source-ip-preserved-with-tls)
  link: [even if you terminate TLS](../facts/elb.md#elb-nlb-faq-source-ip-preserved-with-tls)
elb-nlb-faq-tcp-udp-same-port
  claim: A Network Load Balancer can process TCP and UDP traffic on the same port with a TCP+UDP listener (for example DNS on port 53), and a TCP+UDP listener must be associated with a TCP+UDP target group.
  scope: Network Load Balancer listener.
  link: [create a TCP+UDP listener on port 53](../facts/elb.md#elb-nlb-faq-tcp-udp-same-port)
  link: [a TCP+UDP listener with a TCP+UDP target group](../facts/elb.md#elb-nlb-faq-tcp-udp-same-port)
elb-nlb-faq-udp-flow-5-tuple-idle
  claim: Although UDP is connectionless, a Network Load Balancer keeps UDP flow state with a 5-tuple hash so packets of one flow go to the same target; after the idle timeout the affinity is forgotten and the next packet is load-balanced as a new flow.
  scope: Network Load Balancer UDP listener.
  link: [maintains UDP flow state based on 5-tuple hash](../facts/elb.md#elb-nlb-faq-udp-flow-5-tuple-idle)
  link: [the load balancer will forget the affinity](../facts/elb.md#elb-nlb-faq-udp-flow-5-tuple-idle)
elb-nlb-faq-websockets-tcp-no-special-handling
  claim: A Network Load Balancer passes WebSockets traffic with no special handling, because WebSockets is a layer 7 protocol and the Network Load Balancer works at layer 4.
  scope: Network Load Balancer.
  link: [no special handling exists in Network Load Balancer](../facts/elb.md#elb-nlb-faq-websockets-tcp-no-special-handling)
  link: [Network Load Balancer is operating at layer 4](../facts/elb.md#elb-nlb-faq-websockets-tcp-no-special-handling)
elb-nlb-flow-hash-target-selection
  claim: A Network Load Balancer node selects a target with a flow hash algorithm and routes each individual TCP connection to a single target for the life of the connection.
  scope: Network Load Balancer.
  link: [using a flow hash algorithm](../facts/elb.md#elb-nlb-flow-hash-target-selection)
  link: [single target for the life of the connection](../facts/elb.md#elb-nlb-flow-hash-target-selection)
elb-nlb-gwlb-cross-zone-off-by-default
  claim: On Network Load Balancers and Gateway Load Balancers, cross-zone load balancing is disabled by default, and you can enable or disable it at any time after creation.
  scope: Network Load Balancer and Gateway Load Balancer; default; adjustable.
  link: [cross-zone load balancing is disabled by default](../facts/elb.md#elb-nlb-gwlb-cross-zone-off-by-default)
  link: [cross-zone load balancing at any time](../facts/elb.md#elb-nlb-gwlb-cross-zone-off-by-default)
elb-nlb-gwlb-lcu-reservation-min-2750-per-az
  claim: An LCU reservation request for a Network or Gateway Load Balancer must be at least 2,750 LCU per Availability Zone.
  scope: per Availability Zone, Network or Gateway Load Balancer reservation; minimum; not adjustable.
  link: [at least 2,750 LCU per Availability Zone](../facts/elb.md#elb-nlb-gwlb-lcu-reservation-min-2750-per-az)
  say: at least twenty-seven fifty LCUs per Availability Zone
elb-nlb-gwlb-reserved-lcu-2-2-mbps
  claim: For Network and Gateway Load Balancer LCU reservations, each reserved LCU equals 2.2Mbps of throughput.
  scope: per reserved LCU, Network or Gateway Load Balancer.
  link: [2.2Mbps](../facts/elb.md#elb-nlb-gwlb-reserved-lcu-2-2-mbps)
  say: two point two megabits per second
elb-nlb-health-check-interval-default-30-seconds
  claim: The Network Load Balancer health check interval can be 5 to 300 seconds with a default of 30 seconds, and because the health checks are distributed, targets receive more than the configured number of checks.
  scope: per Network Load Balancer target group; default; adjustable.
  link: [30 seconds](../facts/elb.md#elb-nlb-health-check-interval-default-30-seconds)
  link: [5 to 300 seconds](../facts/elb.md#elb-nlb-health-check-interval-default-30-seconds)
  say: thirty seconds | five to three hundred seconds
elb-nlb-health-check-protocol-default-tcp
  claim: Network Load Balancer health checks can use HTTP, HTTPS or TCP; the default is TCP, and for alb target groups only HTTP and HTTPS are supported.
  scope: per Network Load Balancer target group; default; adjustable.
  link: [The default is the TCP protocol](../facts/elb.md#elb-nlb-health-check-protocol-default-tcp)
  link: [HTTP, HTTPS, and TCP](../facts/elb.md#elb-nlb-health-check-protocol-default-tcp)
  say: the default is TCP | HTTP, HTTPS and TCP
elb-nlb-health-check-success-codes-default-200-399
  claim: For HTTP or HTTPS health checks, a Network Load Balancer accepts success codes from 200 to 599, and the default is 200-399.
  scope: per Network Load Balancer target group; default; adjustable; HTTP or HTTPS health checks.
  link: [200 to 599](../facts/elb.md#elb-nlb-health-check-success-codes-default-200-399)
  link: [200-399](../facts/elb.md#elb-nlb-health-check-success-codes-default-200-399)
  say: two hundred to five ninety-nine | two hundred to three ninety-nine
elb-nlb-health-check-timeout-default
  claim: The Network Load Balancer health check timeout can be 2 to 120 seconds; the default is 6 seconds for HTTP health checks and 10 seconds for TCP and HTTPS health checks.
  scope: per Network Load Balancer target group; default; adjustable.
  link: [6 seconds](../facts/elb.md#elb-nlb-health-check-timeout-default)
  link: [10 seconds](../facts/elb.md#elb-nlb-health-check-timeout-default)
  link: [2 to 120 seconds](../facts/elb.md#elb-nlb-health-check-timeout-default)
  say: six seconds | ten seconds | two to one hundred twenty seconds
elb-nlb-healthy-threshold-default-5
  claim: A Network Load Balancer target needs 5 consecutive successful health checks by default before an unhealthy target is considered healthy; the range is 2 to 10.
  scope: per Network Load Balancer target group; default; adjustable.
  link: [5 consecutive successful health checks](../facts/elb.md#elb-nlb-healthy-threshold-default-5)
  link: [2 to 10](../facts/elb.md#elb-nlb-healthy-threshold-default-5)
  say: five consecutive successful health checks | two to ten
elb-nlb-internal-choose-private-ip
  claim: For an internal Network Load Balancer, you can enter a private IPv4 address from each subnet's range or let AWS select one.
  scope: internal Network Load Balancer, per subnet.
  link: [enter a private IPv4 address](../facts/elb.md#elb-nlb-internal-choose-private-ip)
  link: [let AWS select one for you](../facts/elb.md#elb-nlb-internal-choose-private-ip)
elb-nlb-internal-one-private-ip-per-subnet
  claim: An internal Network Load Balancer supports only a single private IP address in each subnet it is in.
  scope: per subnet, internal Network Load Balancer; maximum.
  link: [can only support a single private IP](../facts/elb.md#elb-nlb-internal-one-private-ip-per-subnet)
  link: [For each associated subnet](../facts/elb.md#elb-nlb-internal-one-private-ip-per-subnet)
  say: can only support a single private IP | for each associated subnet
elb-nlb-listener-protocols
  claim: Network Load Balancer listeners support the TCP, TLS, UDP, TCP_UDP, QUIC and TCP_QUIC protocols.
  scope: Network Load Balancer listener.
  link: [TCP, TLS, UDP](../facts/elb.md#elb-nlb-listener-protocols)
  link: [Protocols](../facts/elb.md#elb-nlb-listener-protocols)
elb-nlb-listener-rules-dual-stack-source-ip-type
  claim: Network Load Balancer listener rules route traffic by source IP address type, so IPv4 and IPv6 traffic can go to separate target groups; listener rules are only available on dual-stack Network Load Balancers.
  scope: Network Load Balancer listener rules.
  link: [only available on dual-stack Network Load Balancers](../facts/elb.md#elb-nlb-listener-rules-dual-stack-source-ip-type)
  link: [based on the source IP address type](../facts/elb.md#elb-nlb-listener-rules-dual-stack-source-ip-type)
elb-nlb-millions-of-requests-per-second
  claim: A Network Load Balancer functions at the fourth layer of the OSI model and can handle millions of requests per second.
  scope: Network Load Balancer.
  link: [millions of requests per second](../facts/elb.md#elb-nlb-millions-of-requests-per-second)
  link: [fourth layer of the Open Systems Interconnection](../facts/elb.md#elb-nlb-millions-of-requests-per-second)
  say: millions of requests per second | layer four of the OSI model
elb-nlb-nlcu-1-gb-per-hour
  claim: One Network Load Balancer NLCU includes 1 GB per hour of processed bytes for EC2 instances, containers and IP addresses as targets.
  scope: per NLCU, TCP, UDP or TLS traffic.
  link: [1 GB per hour](../facts/elb.md#elb-nlb-nlcu-1-gb-per-hour)
  say: one gigabyte per hour
elb-nlb-nlcu-tcp-800-new-100000-active
  claim: For TCP traffic, one Network Load Balancer NLCU includes 800 new TCP connections per second and 100,000 active TCP connections, sampled per minute.
  scope: per NLCU, TCP traffic.
  link: [800 new TCP connections per second](../facts/elb.md#elb-nlb-nlcu-tcp-800-new-100000-active)
  link: [100,000 active TCP connections](../facts/elb.md#elb-nlb-nlcu-tcp-800-new-100000-active)
  say: eight hundred new TCP connections per second | one hundred thousand active TCP connections
elb-nlb-nlcu-tls-50-new-3000-active
  claim: For TLS traffic, one Network Load Balancer NLCU includes 50 new TLS connections per second and 3,000 active TLS connections, sampled per minute.
  scope: per NLCU, TLS traffic.
  link: [50 new TLS connections per second](../facts/elb.md#elb-nlb-nlcu-tls-50-new-3000-active)
  link: [3,000 active TLS connections](../facts/elb.md#elb-nlb-nlcu-tls-50-new-3000-active)
  say: fifty new TLS connections per second | three thousand active TLS connections
elb-nlb-nlcu-udp-400-new-50000-active
  claim: For UDP traffic, one Network Load Balancer NLCU includes 400 new flows per second and 50,000 active UDP flows, sampled per minute.
  scope: per NLCU, UDP traffic.
  link: [400 new flows per second](../facts/elb.md#elb-nlb-nlcu-udp-400-new-50000-active)
  link: [50,000 active UDP flows](../facts/elb.md#elb-nlb-nlcu-udp-400-new-50000-active)
  say: four hundred new flows per second | fifty thousand active UDP flows
elb-nlb-no-sg-all-traffic-allowed
  claim: If a Network Load Balancer has no security group, all client traffic can reach its listeners and all traffic can leave it.
  scope: Network Load Balancer without security groups.
  link: [all client traffic can reach](../facts/elb.md#elb-nlb-no-sg-all-traffic-allowed)
  link: [all traffic can leave the Network Load Balancer](../facts/elb.md#elb-nlb-no-sg-all-traffic-allowed)
elb-nlb-one-eip-per-subnet
  claim: When you create an internet-facing Network Load Balancer, you can optionally associate one Elastic IP address per subnet, which gives the load balancer static IP addresses.
  scope: per subnet, internet-facing Network Load Balancer; maximum.
  link: [one Elastic IP address per subnet](../facts/elb.md#elb-nlb-one-eip-per-subnet)
  link: [optionally associate one Elastic IP address](../facts/elb.md#elb-nlb-one-eip-per-subnet)
  say: one Elastic IP address per subnet | optionally associate one Elastic IP address
elb-nlb-one-eni-per-zone
  claim: Each Network Load Balancer uses one network interface per zone, and the Network Load Balancer ENI quota is set at the VPC level.
  scope: per Network Load Balancer.
  link: [one network interface per zone](../facts/elb.md#elb-nlb-one-eni-per-zone)
  link: [set at the VPC level](../facts/elb.md#elb-nlb-one-eni-per-zone)
  say: one network interface per zone | set at the VPC level
elb-nlb-one-subnet-per-az
  claim: When you enable an Availability Zone for a Network Load Balancer, you must specify one subnet from that Availability Zone.
  scope: per Availability Zone, per Network Load Balancer; maximum.
  link: [one subnet from that Availability Zone](../facts/elb.md#elb-nlb-one-subnet-per-az)
  link: [you must specify one subnet](../facts/elb.md#elb-nlb-one-subnet-per-az)
  say: one subnet from that Availability Zone | you must specify one subnet
elb-nlb-proxy-protocol-v2
  claim: A Network Load Balancer can use proxy protocol version 2 to send extra connection information, such as the source and destination, to targets; proxy protocol is disabled by default.
  scope: Network Load Balancer target group; default.
  link: [send additional connection information](../facts/elb.md#elb-nlb-proxy-protocol-v2)
  link: [By default, proxy protocol is disabled](../facts/elb.md#elb-nlb-proxy-protocol-v2)
elb-nlb-quic-passthrough-tcp-quic
  claim: A Network Load Balancer QUIC listener passes QUIC traffic through to QUIC-enabled targets, and a TCP_QUIC listener supports TCP and QUIC on the same port; QUIC v1 is the only supported QUIC version.
  scope: Network Load Balancer listeners.
  link: [acts as a pass through load balancer](../facts/elb.md#elb-nlb-quic-passthrough-tcp-quic)
  link: [both TCP and QUIC on the same port](../facts/elb.md#elb-nlb-quic-passthrough-tcp-quic)
  link: [QUIC v1 is the only supported QUIC version](../facts/elb.md#elb-nlb-quic-passthrough-tcp-quic)
elb-nlb-quota-alb-targets-per-target-group
  claim: A Network Load Balancer target group can have 1 Application Load Balancer as its target; this quota is not adjustable.
  scope: per target group, per Region; maximum; not adjustable.
  link: [1 Application Load Balancer](../facts/elb.md#elb-nlb-quota-alb-targets-per-target-group)
  say: one Application Load Balancer
elb-nlb-quota-certificates-per-lb
  claim: The default quota is 25 certificates per Network Load Balancer; the quota is adjustable.
  scope: per Network Load Balancer; default; adjustable.
  link: [25 certificates](../facts/elb.md#elb-nlb-quota-certificates-per-lb)
  say: twenty-five certificates
elb-nlb-quota-enis-per-vpc
  claim: The default quota is 1,200 Network Load Balancer ENIs per VPC; the quota is adjustable.
  scope: per VPC; default; adjustable.
  link: [1,200 Network Load Balancer ENIs](../facts/elb.md#elb-nlb-quota-enis-per-vpc)
  say: twelve hundred Network Load Balancer ENIs
elb-nlb-quota-listeners-per-lb
  claim: A Network Load Balancer can have at most 50 listeners; this quota is not adjustable.
  scope: per Network Load Balancer; maximum; not adjustable.
  link: [50 listeners](../facts/elb.md#elb-nlb-quota-listeners-per-lb)
  say: fifty listeners
elb-nlb-quota-load-balancers-per-region
  claim: The default quota is 50 Network Load Balancers per Region; the quota is adjustable.
  scope: per Region, per account; default; adjustable.
  link: [50 Network Load Balancers](../facts/elb.md#elb-nlb-quota-load-balancers-per-region)
  say: fifty Network Load Balancers
elb-nlb-quota-reserved-lcus-per-lb-per-az
  claim: The default quota is 45,000 reserved LCUs per Network Load Balancer, per Availability Zone; the quota is adjustable.
  scope: per Network Load Balancer, per Availability Zone; default; adjustable.
  link: [45,000 reserved LCUs](../facts/elb.md#elb-nlb-quota-reserved-lcus-per-lb-per-az)
  say: forty-five thousand reserved LCUs
elb-nlb-quota-reserved-lcus-per-region
  claim: The default quota for reserved Network Load Balancer LCUs per Region is 0; the quota is adjustable.
  scope: per Region, per account; default; adjustable.
  link: [LCUs per Region is 0](../facts/elb.md#elb-nlb-quota-reserved-lcus-per-region)
  say: zero reserved LCUs per Region
elb-nlb-quota-rules-per-lb
  claim: A Network Load Balancer can have at most 100 listener rules; this quota is not adjustable.
  scope: per Network Load Balancer; maximum; not adjustable.
  link: [100 listener rules](../facts/elb.md#elb-nlb-quota-rules-per-lb)
  say: one hundred listener rules
elb-nlb-quota-target-groups-per-rule-action
  claim: One listener rule action of a Network Load Balancer can use at most 5 target groups; this quota is not adjustable.
  scope: per listener rule action; maximum; not adjustable.
  link: [5 target groups](../facts/elb.md#elb-nlb-quota-target-groups-per-rule-action)
  say: five target groups
elb-nlb-quota-targets-per-az
  claim: The default quota is 500 targets per Availability Zone per Network Load Balancer; the quota is adjustable.
  scope: per Availability Zone, per Network Load Balancer; default; adjustable.
  link: [500 targets per Availability Zone](../facts/elb.md#elb-nlb-quota-targets-per-az)
  say: five hundred targets per Availability Zone
elb-nlb-quota-targets-per-lb
  claim: The default quota is 3,000 targets per Network Load Balancer and is adjustable; but if cross-zone load balancing is enabled, the maximum is 500 targets per load balancer, regardless of the number of Availability Zones.
  scope: per Network Load Balancer; default; adjustable; if cross-zone load balancing is enabled, the maximum is 500 targets per load balancer.
  link: [3,000 targets](../facts/elb.md#elb-nlb-quota-targets-per-lb)
  link: [500 targets per load balancer](../facts/elb.md#elb-nlb-quota-targets-per-lb)
  say: three thousand targets | five hundred targets per load balancer
elb-nlb-secondary-ips-0-to-7
  claim: A Network Load Balancer can auto-assign 0 to 7 secondary IP addresses per subnet to resolve port allocation errors; the default is 0 and the value cannot be decreased after it is set.
  scope: per subnet, per Network Load Balancer; maximum; adjustable.
  link: [0 to 7](../facts/elb.md#elb-nlb-secondary-ips-0-to-7)
  link: [The default is 0](../facts/elb.md#elb-nlb-secondary-ips-0-to-7)
  say: zero to seven | the default is zero
elb-nlb-security-groups-only-at-creation
  claim: You can associate security groups with a Network Load Balancer only when you create it; if it is created without security groups you cannot add them later, but if it has them you can change them at any time.
  scope: Network Load Balancer.
  link: [when you create it](../facts/elb.md#elb-nlb-security-groups-only-at-creation)
  link: [you can't associate them](../facts/elb.md#elb-nlb-security-groups-only-at-creation)
  link: [change the security groups](../facts/elb.md#elb-nlb-security-groups-only-at-creation)
elb-nlb-sg-blocked-traffic-not-charged
  claim: You are not charged for traffic that the inbound security group rules of a Network Load Balancer block.
  scope: Network Load Balancer security groups.
  link: [You are not charged for traffic](../facts/elb.md#elb-nlb-sg-blocked-traffic-not-charged)
  link: [blocked by inbound security group rules](../facts/elb.md#elb-nlb-sg-blocked-traffic-not-charged)
elb-nlb-sg-reference-blocks-direct-access
  claim: If the target security groups allow traffic only from the security group of the Network Load Balancer, clients can reach the targets through the load balancer but not directly.
  scope: Network Load Balancer and its targets.
  link: [through your Network Load Balancer](../facts/elb.md#elb-nlb-sg-reference-blocks-direct-access)
  link: [prevents them from sending traffic directly](../facts/elb.md#elb-nlb-sg-reference-blocks-direct-access)
elb-nlb-static-ip-per-az-optional-eip
  claim: For a Network Load Balancer, Elastic Load Balancing creates a network interface for each enabled Availability Zone and uses it to get a static IP address; you can optionally associate one Elastic IP address with each network interface when you create the load balancer.
  scope: Network Load Balancer, per enabled Availability Zone; Elastic IP association at creation.
  link: [uses it to get a static IP address](../facts/elb.md#elb-nlb-static-ip-per-az-optional-eip)
  link: [optionally associate one Elastic IP address](../facts/elb.md#elb-nlb-static-ip-per-az-optional-eip)
  link: [when you create the Network Load Balancer](../facts/elb.md#elb-nlb-static-ip-per-az-optional-eip)
elb-nlb-sticky-source-ip
  claim: Network Load Balancer sticky sessions use the stickiness type source_ip, are off by default, and are not supported for TLS or QUIC listeners.
  scope: Network Load Balancer target group; default.
  link: [The possible value is `source_ip`](../facts/elb.md#elb-nlb-sticky-source-ip)
  link: [The default is `false`](../facts/elb.md#elb-nlb-sticky-source-ip)
  link: [not supported for TLS or QUIC listeners](../facts/elb.md#elb-nlb-sticky-source-ip)
elb-nlb-target-counts-per-target-group
  claim: For the per-Availability Zone target quota of a Network Load Balancer, a target registered with N target groups counts as N targets, and an Application Load Balancer target counts as 50 targets (100 if cross-zone load balancing is enabled).
  scope: per Availability Zone, per Network Load Balancer; maximum; not adjustable.
  link: [50 targets](../facts/elb.md#elb-nlb-target-counts-per-target-group)
  link: [100 targets](../facts/elb.md#elb-nlb-target-counts-per-target-group)
  say: fifty targets | one hundred targets
elb-nlb-target-types-instance-ip-alb
  claim: A Network Load Balancer target group has the target type instance, ip or alb; with the alb type you register a single Application Load Balancer as the target.
  scope: Network Load Balancer target group.
  link: [The target is an Application Load Balancer](../facts/elb.md#elb-nlb-target-types-instance-ip-alb)
  link: [register a single Application Load Balancer](../facts/elb.md#elb-nlb-target-types-instance-ip-alb)
elb-nlb-tcp-idle-timeout-default-350-seconds
  claim: The TCP idle timeout of a Network Load Balancer is 350 seconds by default and can be updated to any value between 60 and 6000 seconds.
  scope: per TCP listener of a Network Load Balancer; default; adjustable.
  link: [350 seconds](../facts/elb.md#elb-nlb-tcp-idle-timeout-default-350-seconds)
  link: [60-6000 seconds](../facts/elb.md#elb-nlb-tcp-idle-timeout-default-350-seconds)
  say: three hundred fifty seconds | sixty to six thousand seconds
elb-nlb-tls-ecdsa-256-supported
  claim: ECDSA 256-bit is one of the supported key algorithms for Network Load Balancer server certificates.
  scope: per Network Load Balancer TLS listener certificate.
  link: [ECDSA 256-bit](../facts/elb.md#elb-nlb-tls-ecdsa-256-supported)
  say: ECDSA two fifty-six bit
elb-nlb-tls-idle-timeout-fixed-350-seconds
  claim: The connection idle timeout for Network Load Balancer TLS listeners is 350 seconds and can't be modified.
  scope: per TLS listener of a Network Load Balancer; fixed.
  link: [350 seconds](../facts/elb.md#elb-nlb-tls-idle-timeout-fixed-350-seconds)
  link: [can't be modified](../facts/elb.md#elb-nlb-tls-idle-timeout-fixed-350-seconds)
  say: three hundred fifty seconds | can't be modified
elb-nlb-tls-keepalive-every-20-seconds
  claim: When a Network Load Balancer TLS listener receives a TCP keepalive packet, the load balancer sends TCP keepalive packets to both the front-end and back-end connections every 20 seconds.
  scope: per TLS listener of a Network Load Balancer.
  link: [every 20 seconds](../facts/elb.md#elb-nlb-tls-keepalive-every-20-seconds)
  link: [both the front-end and back-end connections](../facts/elb.md#elb-nlb-tls-keepalive-every-20-seconds)
  say: every twenty seconds | both front-end and back-end connections
elb-nlb-tls-listener-terminate-tcp-passthrough
  claim: An NLB TLS listener offloads encryption and decryption to the load balancer and needs at least one server certificate; to have targets decrypt TLS instead, create a TCP listener on port 443, which passes the encrypted traffic through.
  scope: Network Load Balancer listener.
  link: [deploy at least one SSL server certificate](../facts/elb.md#elb-nlb-tls-listener-terminate-tcp-passthrough)
  link: [create a TCP listener on port 443](../facts/elb.md#elb-nlb-tls-listener-terminate-tcp-passthrough)
  link: [passes encrypted traffic through to the targets](../facts/elb.md#elb-nlb-tls-listener-terminate-tcp-passthrough)
elb-nlb-tls-rsa-max-3072-bit
  claim: For RSA certificates on Network Load Balancer TLS listeners, the maximum supported key size is 3072-bit; an RSA 4096-bit certificate imported through IAM leaves the listener non-functional.
  scope: per Network Load Balancer TLS listener certificate; maximum; not adjustable.
  link: [3072-bit](../facts/elb.md#elb-nlb-tls-rsa-max-3072-bit)
  link: [RSA 4096-bit](../facts/elb.md#elb-nlb-tls-rsa-max-3072-bit)
  say: three thousand seventy-two bit | RSA four thousand ninety-six bit
elb-nlb-tls-target-no-cert-validation
  claim: With a TLS target group, a Network Load Balancer opens TLS connections to targets with the certificates installed on them but does not validate those certificates.
  scope: Network Load Balancer TLS target group.
  link: [The load balancer does not validate these certificates](../facts/elb.md#elb-nlb-tls-target-no-cert-validation)
elb-nlb-udp-idle-timeout-fixed-120-seconds
  claim: Elastic Load Balancing sets the idle timeout for UDP flows on a Network Load Balancer to 120 seconds, and this value cannot be changed.
  scope: per UDP flow on a Network Load Balancer; fixed.
  link: [120 seconds](../facts/elb.md#elb-nlb-udp-idle-timeout-fixed-120-seconds)
  link: [This cannot be changed](../facts/elb.md#elb-nlb-udp-idle-timeout-fixed-120-seconds)
  say: one hundred twenty seconds | this cannot be changed
elb-nlb-udp-non-udp-health-checks
  claim: For UDP and QUIC services on a Network Load Balancer, target availability is tested with non-UDP health checks: TCP, HTTP or HTTPS, on any port of the target.
  scope: Network Load Balancer UDP and QUIC target groups.
  link: [non-UDP health checks](../facts/elb.md#elb-nlb-udp-non-udp-health-checks)
  link: [(TCP, HTTP, or HTTPS)](../facts/elb.md#elb-nlb-udp-non-udp-health-checks)
elb-nlb-unhealthy-az-removed-from-dns-fail-open
  claim: If a Network Load Balancer's target groups have no healthy target in an enabled Availability Zone, the IP address for that subnet is removed from DNS; if all targets fail at the same time in all enabled zones, or the target group is empty, the load balancer fails open.
  scope: Network Load Balancer.
  link: [corresponding subnet from DNS](../facts/elb.md#elb-nlb-unhealthy-az-removed-from-dns-fail-open)
  link: [the load balancer fails open](../facts/elb.md#elb-nlb-unhealthy-az-removed-from-dns-fail-open)
  link: [when you have an empty target group](../facts/elb.md#elb-nlb-unhealthy-az-removed-from-dns-fail-open)
elb-nlb-unhealthy-threshold-default-2
  claim: A Network Load Balancer target is considered unhealthy after 2 consecutive failed health checks by default; the range is 2 to 10.
  scope: per Network Load Balancer target group; default; adjustable.
  link: [2 consecutive failed health checks](../facts/elb.md#elb-nlb-unhealthy-threshold-default-2)
  link: [2 to 10](../facts/elb.md#elb-nlb-unhealthy-threshold-default-2)
  say: two consecutive failed health checks | two to ten
elb-nlb-weighted-default-action
  claim: A Network Load Balancer default action can forward to multiple target groups by relative weight, each from 0 to 999; a weight of 0 sends no traffic, and only new connections follow a weight change.
  scope: Network Load Balancer listener default action.
  link: [a weight from 0 to 999](../facts/elb.md#elb-nlb-weighted-default-action)
  link: [A target group with a weight of 0 receives no traffic](../facts/elb.md#elb-nlb-weighted-default-action)
  link: [Existing connections are not affected](../facts/elb.md#elb-nlb-weighted-default-action)
elb-nlb-zonal-affinity-85-percent
  claim: The Network Load Balancer DNS client routing policy can be availability_zone_affinity (100 percent zonal affinity), partial_availability_zone_affinity (85 percent) or any_availability_zone (0 percent).
  scope: per Network Load Balancer.
  link: [100 percent zonal affinity](../facts/elb.md#elb-nlb-zonal-affinity-85-percent)
  link: [85 percent zonal affinity](../facts/elb.md#elb-nlb-zonal-affinity-85-percent)
  link: [0 percent zonal affinity](../facts/elb.md#elb-nlb-zonal-affinity-85-percent)
  say: one hundred percent zonal affinity | eighty-five percent zonal affinity | zero percent zonal affinity
elb-node-per-enabled-az
  claim: When you enable an Availability Zone for a load balancer, Elastic Load Balancing creates a load balancer node in that Availability Zone.
  scope: per enabled Availability Zone.
  link: [creates a load balancer node](../facts/elb.md#elb-node-per-enabled-az)
  link: [in the Availability Zone](../facts/elb.md#elb-node-per-enabled-az)
elb-node-sends-to-target-private-ip
  claim: The load balancer node that receives a request selects a healthy registered target and sends the request to the target's private IP address.
  scope: load balancer node.
  link: [selects a healthy registered target](../facts/elb.md#elb-node-sends-to-target-private-ip)
  link: [using its private IP address](../facts/elb.md#elb-node-sends-to-target-private-ip)
elb-offload-encryption-to-lb
  claim: Elastic Load Balancing can terminate HTTPS and TLS traffic from clients at the load balancer, so the load balancer does the encryption and decryption work instead of each EC2 instance.
  scope: secure listeners.
  link: [terminating HTTPS and TLS traffic from clients](../facts/elb.md#elb-offload-encryption-to-lb)
  link: [performs the work of encrypting and decrypting](../facts/elb.md#elb-offload-encryption-to-lb)
elb-partial-hour-billed-as-full-hour
  claim: Application, Network and Gateway Load Balancers are charged for each hour or partial hour that they run, and each partial hour is billed as a full hour.
  scope: per load balancer.
  link: [billed as a full hour](../facts/elb.md#elb-partial-hour-billed-as-full-hour)
  link: [each hour or partial hour](../facts/elb.md#elb-partial-hour-billed-as-full-hour)
  say: billed as a full hour | each hour or partial hour
elb-pricing-gwlbe-billed-separately
  claim: The Gateway Load Balancer endpoint (GWLBE), a VPC endpoint type powered by AWS PrivateLink, is priced and billed separately from the Gateway Load Balancer.
  scope: Gateway Load Balancer endpoint.
  link: [GWLBE is priced and billed separately](../facts/elb.md#elb-pricing-gwlbe-billed-separately)
elb-pricing-public-ipv4-and-data-transfer-extra
  claim: On top of the load balancer charges, you pay standard AWS data transfer charges and standard public IPv4 address charges for all addresses your load balancers consume.
  scope: Elastic Load Balancing.
  link: [standard AWS data transfer charges](../facts/elb.md#elb-pricing-public-ipv4-and-data-transfer-extra)
  link: [standard public IPv4 address charges](../facts/elb.md#elb-pricing-public-ipv4-and-data-transfer-extra)
elb-privatelink-needs-nlb-or-gwlb
  claim: A VPC endpoint service (AWS PrivateLink) requires either a Network Load Balancer or a Gateway Load Balancer, which receives requests from service consumers and routes them to the service.
  scope: VPC endpoint service.
  link: [Network Load Balancer or a Gateway Load Balancer](../facts/elb.md#elb-privatelink-needs-nlb-or-gwlb)
elb-privatelink-source-ip-is-lb-nodes
  claim: When consumers reach a service through an interface endpoint, the application sees the private IP addresses of the load balancer nodes, not the consumers' addresses; with proxy protocol enabled on the load balancer, the service can get the consumer addresses and endpoint IDs from the proxy protocol header.
  scope: VPC endpoint service with Network Load Balancer.
  link: [private IP addresses of the load balancer nodes](../facts/elb.md#elb-privatelink-source-ip-is-lb-nodes)
  link: [If you enable proxy protocol](../facts/elb.md#elb-privatelink-source-ip-is-lb-nodes)
elb-quota-target-groups-per-region
  claim: The default quota is 3,000 target groups per Region; the quota is adjustable.
  scope: per Region, per account; default; adjustable.
  link: [3,000 target groups](../facts/elb.md#elb-quota-target-groups-per-region)
  say: three thousand target groups
elb-quota-targets-per-target-group
  claim: The default quota is 1,000 instance or IP address targets per target group; the quota is adjustable.
  scope: per target group, per Region; default; adjustable.
  link: [1,000 instance or IP address targets](../facts/elb.md#elb-quota-targets-per-target-group)
  say: one thousand instance or IP targets
elb-route53-map-domain-to-load-balancer
  claim: AWS assigns a URL to each load balancer, and you can map your own easy-to-remember domain name to the load balancer.
  scope: Amazon Route 53 with Elastic Load Balancing.
  link: [AWS assigns URLs to your resources](../facts/elb.md#elb-route53-map-domain-to-load-balancer)
  link: [map your domain name to a load balancer](../facts/elb.md#elb-route53-map-domain-to-load-balancer)
elb-routes-only-to-healthy-targets
  claim: Elastic Load Balancing monitors the health of its registered targets and routes traffic only to the healthy targets.
  scope: Elastic Load Balancing.
  link: [monitors the health of its registered targets](../facts/elb.md#elb-routes-only-to-healthy-targets)
  link: [routes traffic only to the healthy targets](../facts/elb.md#elb-routes-only-to-healthy-targets)
elb-scales-capacity-automatically
  claim: Elastic Load Balancing scales the load balancer capacity automatically when incoming traffic changes.
  scope: Elastic Load Balancing.
  link: [scales your load balancer capacity automatically](../facts/elb.md#elb-scales-capacity-automatically)
  link: [in response to changes in incoming traffic](../facts/elb.md#elb-scales-capacity-automatically)
elb-scheme-choose-internal-or-internet-facing
  claim: When you create a load balancer, you must choose whether it is internal or internet-facing.
  scope: any load balancer; at creation.
  link: [internal load balancer or an internet-facing load balancer](../facts/elb.md#elb-scheme-choose-internal-or-internet-facing)
  link: [When you create a load balancer](../facts/elb.md#elb-scheme-choose-internal-or-internet-facing)
elb-secure-listener-ciphers-cert-acm-iam
  claim: For a secure listener you specify the cipher suites and protocol versions, plus a server certificate installed on the load balancer; certificates can be managed with AWS Certificate Manager (ACM) or IAM.
  scope: HTTPS and TLS listeners.
  link: [cipher suites and protocol versions](../facts/elb.md#elb-secure-listener-ciphers-cert-acm-iam)
  link: [server certificate to install on your load balancer](../facts/elb.md#elb-secure-listener-ciphers-cert-acm-iam)
  link: [AWS Certificate Manager (ACM)](../facts/elb.md#elb-secure-listener-ciphers-cert-acm-iam)
elb-secure-listener-type-per-lb
  claim: Application Load Balancers support HTTPS listeners, Network Load Balancers support TLS listeners, and Classic Load Balancers support both HTTPS and TLS listeners.
  scope: secure listeners per load balancer type.
  link: [Application Load Balancers support HTTPS listeners](../facts/elb.md#elb-secure-listener-type-per-lb)
  link: [Network Load Balancers support TLS listeners](../facts/elb.md#elb-secure-listener-type-per-lb)
elb-session-store-centralized-not-on-servers
  claim: AWS calls a centralized session management data store the ideal solution for HTTP sessions in modern architectures: it gives consistent user experiences across all web servers and better session durability when the web server fleet is elastic.
  scope: web applications behind a load balancer.
  link: [centralized session management data store](../facts/elb.md#elb-session-store-centralized-not-on-servers)
  link: [when your fleet of web servers is elastic](../facts/elb.md#elb-session-store-centralized-not-on-servers)
elb-shield-advanced-nlb-through-eip
  claim: AWS Shield Advanced protects Network Load Balancers through their associated Elastic IP addresses.
  scope: AWS Shield Advanced protected resources.
  link: [through associations to Amazon EC2 Elastic IP addresses](../facts/elb.md#elb-shield-advanced-nlb-through-eip)
  link: [Elastic Load Balancing (ELB) load balancers](../facts/elb.md#elb-shield-advanced-nlb-through-eip)
elb-sticky-uneven-load-nat
  claim: Sticky sessions can lead to an uneven distribution of connections; for example, all clients behind the same NAT device share one source IP address, so all of their traffic goes to the same target.
  scope: Network Load Balancer stickiness.
  link: [uneven distribution of connections and flows](../facts/elb.md#elb-sticky-uneven-load-nat)
  link: [all clients behind the same NAT device](../facts/elb.md#elb-sticky-uneven-load-nat)
elb-target-group-health-dns-failover
  claim: With target group health DNS failover, when the healthy targets in a zone fall below the threshold, the load balancer node IP addresses for that zone are marked unhealthy in DNS, so clients are routed only to healthy zones.
  scope: Application Load Balancer target group health; healthy targets in a zone below the threshold.
  link: [as unhealthy in DNS](../facts/elb.md#elb-target-group-health-dns-failover)
  link: [routed only to healthy zones](../facts/elb.md#elb-target-group-health-dns-failover)
elb-target-group-health-routing-failover
  claim: With target group health routing failover, when the healthy targets in a zone fall below the threshold, the load balancer sends traffic to all targets available to that node, including unhealthy ones.
  scope: Application Load Balancer target group health; healthy targets in a zone below the threshold.
  link: [sends traffic to all targets](../facts/elb.md#elb-target-group-health-routing-failover)
  link: [including unhealthy targets](../facts/elb.md#elb-target-group-health-routing-failover)
elb-target-group-healthy-with-one-target
  claim: By default, a target group is considered healthy as long as it has at least one healthy target; you can set a minimum count or percentage of healthy targets instead.
  scope: per target group (Application and Network Load Balancers); default; adjustable.
  link: [at least one healthy target](../facts/elb.md#elb-target-group-healthy-with-one-target)
  link: [considered healthy as long as](../facts/elb.md#elb-target-group-healthy-with-one-target)
  say: at least one healthy target | considered healthy as long as
elb-target-group-quota-shared-alb-nlb
  claim: The target groups per Region quota is shared by Application Load Balancers and Network Load Balancers.
  scope: per Region, per account; default; adjustable.
  link: [Application Load Balancers and Network Load Balancers](../facts/elb.md#elb-target-group-quota-shared-alb-nlb)
  link: [This quota is shared](../facts/elb.md#elb-target-group-quota-shared-alb-nlb)
  say: shared by Application and Network Load Balancers | this quota is shared
elb-target-sg-reference-lb-sg
  claim: To make targets accept traffic only from the load balancer, set the load balancer's security group as the source in the ingress rule of the targets' security group.
  scope: target security groups.
  link: [the load balancer's security group as the source](../facts/elb.md#elb-target-sg-reference-lb-sg)
  link: [receive traffic exclusively from the load balancer](../facts/elb.md#elb-target-sg-reference-lb-sg)
elb-targets-in-disabled-az-no-traffic
  claim: Targets that are registered in an Availability Zone that is not enabled for the load balancer do not receive traffic.
  scope: registered targets; the target's Availability Zone is not enabled.
  link: [these registered targets do not receive traffic](../facts/elb.md#elb-targets-in-disabled-az-no-traffic)
  link: [do not enable the Availability Zone](../facts/elb.md#elb-targets-in-disabled-az-no-traffic)
elb-targets-need-no-public-ip
  claim: Both internet-facing and internal load balancers route requests to targets using private IP addresses, so targets do not need public IP addresses.
  scope: targets of internal and internet-facing load balancers.
  link: [using private IP addresses](../facts/elb.md#elb-targets-need-no-public-ip)
  link: [do not need public IP addresses](../facts/elb.md#elb-targets-need-no-public-ip)
elb-tls-recommended-post-quantum-policy
  claim: For Application Load Balancer HTTPS listeners, AWS recommends the post-quantum TLS security policy ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09 or ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09.
  scope: Application Load Balancer HTTPS listeners.
  link: [ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09](../facts/elb.md#elb-tls-recommended-post-quantum-policy)
  link: [ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09](../facts/elb.md#elb-tls-recommended-post-quantum-policy)
elb-unhealthy-target-stop-resume
  claim: When the load balancer detects an unhealthy target it stops routing traffic to it, and it resumes routing when the target is healthy again.
  scope: registered target.
  link: [it stops routing traffic to that target](../facts/elb.md#elb-unhealthy-target-stop-resume)
  link: [resumes routing traffic to that target](../facts/elb.md#elb-unhealthy-target-stop-resume)
elb-wa-rel10-cross-zone-off-use-zonal-shift
  claim: Well-Architected REL10-BP01 says that if you turn off cross-zone load balancing, you should use Amazon Application Recovery Controller (ARC) to get zonal shift capability.
  scope: AWS Well-Architected Framework, reliability pillar REL10-BP01.
  link: [If you disable cross-zone load balancing](../facts/elb.md#elb-wa-rel10-cross-zone-off-use-zonal-shift)
  link: [to provide zonal shift capability](../facts/elb.md#elb-wa-rel10-cross-zone-off-use-zonal-shift)
elb-wa-rel10-cross-zone-reroute-impaired-az
  claim: Well-Architected REL10-BP01 says that with cross-zone load balancing enabled, Application and Network Load Balancers detect targets that are unreachable because of an Availability Zone impairment and reroute traffic to targets in healthy Availability Zones.
  scope: AWS Well-Architected Framework, reliability pillar REL10-BP01.
  link: [unreachable due to Availability Zone impairment](../facts/elb.md#elb-wa-rel10-cross-zone-reroute-impaired-az)
  link: [reroute traffic towards targets in healthy Availability Zones](../facts/elb.md#elb-wa-rel10-cross-zone-reroute-impaired-az)
elb-wa-rel10-load-balancers-in-front-of-compute
  claim: Well-Architected REL10-BP01 says to place traffic directors such as load balancers in front of compute resources that are spread over multiple Availability Zones.
  scope: AWS Well-Architected Framework, reliability pillar REL10-BP01.
  link: [Place traffic directors such as load balancers](../facts/elb.md#elb-wa-rel10-load-balancers-in-front-of-compute)
  link: [in front of your compute resources](../facts/elb.md#elb-wa-rel10-load-balancers-in-front-of-compute)
elb-wa-sec09-sg-allow-only-https-to-alb
  claim: Well-Architected SEC09-BP02 says to enforce encryption in transit and only allow secure protocols, for example a security group that allows only HTTPS to an Application Load Balancer.
  scope: AWS Well-Architected Framework, security pillar SEC09-BP02.
  link: [only allow secure protocols](../facts/elb.md#elb-wa-sec09-sg-allow-only-https-to-alb)
  link: [only allow the HTTPS protocol](../facts/elb.md#elb-wa-sec09-sg-allow-only-https-to-alb)
elb-waf-integrates-with-alb
  claim: You can integrate an Application Load Balancer with AWS WAF, whose rules on IP addresses, HTTP headers and URI strings can block, allow or count web requests.
  scope: Application Load Balancer.
  link: [AWS Web Application Firewall (WAF)](../facts/elb.md#elb-waf-integrates-with-alb)
  link: [block, allow, or monitor (count) web requests](../facts/elb.md#elb-waf-integrates-with-alb)
elb-weighted-target-group-weight-0-to-999
  claim: When a forward action has several target groups, on Application and Network Load Balancers each target group weight is a value from 0 to 999; the Network Load Balancer guide adds that a target group with a weight of 0 receives no traffic.
  scope: per target group in a forward action (Application and Network Load Balancers); maximum; not adjustable; the weight-0 statement is quoted from the Network Load Balancer guide.
  link: [0 to 999](../facts/elb.md#elb-weighted-target-group-weight-0-to-999)
  link: [weight of 0 receives no traffic](../facts/elb.md#elb-weighted-target-group-weight-0-to-999)
  say: zero to nine hundred ninety-nine | weight zero receives no traffic
elb-what-distributes-traffic-across-targets
  claim: Elastic Load Balancing distributes incoming traffic across multiple targets, such as EC2 instances, containers and IP addresses, in one or more Availability Zones.
  scope: Elastic Load Balancing.
  link: [automatically distributes your incoming traffic](../facts/elb.md#elb-what-distributes-traffic-across-targets)
  link: [in one or more Availability Zones](../facts/elb.md#elb-what-distributes-traffic-across-targets)
elb-zonal-autoshift-aws-shifts
  claim: With zonal autoshift you authorize AWS to shift your resource traffic away from an Availability Zone on your behalf when internal monitoring shows an Availability Zone impairment that could affect customers.
  scope: load balancer resource; zonal autoshift configured.
  link: [you authorize AWS to shift away resource traffic](../facts/elb.md#elb-zonal-autoshift-aws-shifts)
  link: [on your behalf](../facts/elb.md#elb-zonal-autoshift-aws-shifts)
elb-zonal-shift-cross-zone-off-loses-capacity
  claim: If cross-zone load balancing is off and a zonal shift removes a zonal load balancer IP address, the shifted Availability Zone also loses target capacity, so check capacity before you start a zonal shift.
  scope: load balancer with cross-zone off; cross-zone load balancing off.
  link: [also loses target capacity](../facts/elb.md#elb-zonal-shift-cross-zone-off-loses-capacity)
  link: [Always check current Availability Zone capacity](../facts/elb.md#elb-zonal-shift-cross-zone-off-loses-capacity)
elb-zonal-shift-stops-new-traffic-to-az
  claim: When a zonal shift starts, the load balancer stops sending new traffic for the resource to the affected Availability Zone; existing connections can take a short time to complete.
  scope: Application Load Balancer.
  link: [stops sending new traffic](../facts/elb.md#elb-zonal-shift-stops-new-traffic-to-az)
  link: [ARC creates the zonal shift immediately](../facts/elb.md#elb-zonal-shift-stops-new-traffic-to-az)
elb-zonal-shift-what
  claim: Zonal shift, a capability of Amazon Application Recovery Controller (ARC), shifts a load balancer's traffic away from an impaired Availability Zone with a single action so that the application keeps running from the other healthy Availability Zones in the Region.
  scope: load balancer resource.
  link: [Amazon Application Recovery Controller (ARC)](../facts/elb.md#elb-zonal-shift-what)
  link: [away from an impaired Availability Zone](../facts/elb.md#elb-zonal-shift-what)
  link: [with a single action](../facts/elb.md#elb-zonal-shift-what)
