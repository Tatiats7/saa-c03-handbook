facts card: 519 facts
client-vpn-active-directory-via-directory-service-ad-connector
  claim: Client VPN integrates with Directory Service to authenticate clients against existing Active Directory groups, in AWS or on premises. For an on-premises Active Directory without an existing AWS Managed Microsoft AD, you must configure an AD Connector.
  scope: Client VPN Active Directory authentication.
  link: [Active Directory support by integrating with Directory Service](../facts/client-vpn.md#client-vpn-active-directory-via-directory-service-ad-connector)
  link: [configure an Active Directory Connector (AD Connector)](../facts/client-vpn.md#client-vpn-active-directory-via-directory-service-ad-connector)
client-vpn-ad-endpoint-same-account-as-directory
  claim: With Active Directory authentication, the Client VPN endpoint must belong to the same account as the AWS Directory Service resource. With SAML federated authentication it must belong to the same account as the IAM SAML identity provider.
  scope: Client VPN endpoint.
  link: [same account as the AWS Directory Service resource](../facts/client-vpn.md#client-vpn-ad-endpoint-same-account-as-directory)
  link: [same account as the IAM SAML identity provider](../facts/client-vpn.md#client-vpn-ad-endpoint-same-account-as-directory)
client-vpn-authentication-alone-or-mutual-plus-user-based
  claim: You can use one Client VPN authentication method alone, or combine mutual authentication with a user-based method. If you combine them, both methods must be used to authenticate.
  scope: Client VPN client authentication.
  link: [combination of mutual authentication with a user-based method](../facts/client-vpn.md#client-vpn-authentication-alone-or-mutual-plus-user-based)
  link: [both methods must then be used](../facts/client-vpn.md#client-vpn-authentication-alone-or-mutual-plus-user-based)
client-vpn-authentication-methods-ad-certificate-saml
  claim: AWS Client VPN supports authentication with Active Directory using AWS Directory Service, certificate-based authentication, and federated authentication using SAML-2.0.
  scope: AWS Client VPN.
  link: [authentication with Active Directory using AWS Directory Services](../facts/client-vpn.md#client-vpn-authentication-methods-ad-certificate-saml)
  link: [Certificate-based authentication](../facts/client-vpn.md#client-vpn-authentication-methods-ad-certificate-saml)
  link: [Federated Authentication using SAML-2.0](../facts/client-vpn.md#client-vpn-authentication-methods-ad-certificate-saml)
client-vpn-authorization-rule-group-limits-access-to-network
  claim: For each network you want to enable access to, you configure authorization rules with the Active Directory group or SAML-based IdP group that is allowed, and only users who belong to that group can access that network. If you do not use Active Directory or SAML-based federated authentication, or you want to open access to all users, you can specify a rule that grants access to all clients.
  scope: Client VPN authorization rules.
  link: [Active Directory group or the SAML-based IdP group](../facts/client-vpn.md#client-vpn-authorization-rule-group-limits-access-to-network)
  link: [Only users who belong to the specified group](../facts/client-vpn.md#client-vpn-authorization-rule-group-limits-access-to-network)
client-vpn-authorization-rules-default-deny-no-restrict-rules
  claim: By default there are no authorization rules, and access to a destination network is denied until you add an authorization rule. You cannot add an authorization rule to restrict access to a network.
  scope: Client VPN endpoint authorization rules; default; adjustable; add authorization rules to allow access.
  link: [The default behavior is to deny access](../facts/client-vpn.md#client-vpn-authorization-rules-default-deny-no-restrict-rules)
  link: [cannot add an authorization rule to restrict access](../facts/client-vpn.md#client-vpn-authorization-rules-default-deny-no-restrict-rules)
client-vpn-authorization-security-groups-and-network-rules
  claim: Client VPN supports two types of client authorization: security groups and network-based authorization using authorization rules.
  scope: Client VPN endpoint.
  link: [security groups and network-based authorization](../facts/client-vpn.md#client-vpn-authorization-security-groups-and-network-rules)
  link: [security groups](../facts/client-vpn.md#client-vpn-authorization-security-groups-and-network-rules)
client-vpn-billing-elastic-ip-when-vpc-has-internet-gateway
  claim: If the VPC of the associated subnet has an internet gateway, AWS associates Elastic IP addresses with the Client VPN network interfaces, and these are charged as in-use public IPv4 addresses.
  scope: Client VPN endpoints in a VPC with an internet gateway.
  link: [we associate Elastic IP addresses](../facts/client-vpn.md#client-vpn-billing-elastic-ip-when-vpc-has-internet-gateway)
  link: [charged as in-use public IPv4 addresses](../facts/client-vpn.md#client-vpn-billing-elastic-ip-when-vpc-has-internet-gateway)
client-vpn-billing-endpoint-association-and-connection-hours
  claim: You are charged for each Client VPN endpoint association and each VPN connection on an hourly basis. There is no additional cost for using IPv6 or dual-stack endpoints.
  scope: AWS Client VPN.
  link: [each endpoint association and each VPN connection](../facts/client-vpn.md#client-vpn-billing-endpoint-association-and-connection-hours)
  link: [There is no additional cost for using IPv6 or dual-stack endpoints](../facts/client-vpn.md#client-vpn-billing-endpoint-association-and-connection-hours)
client-vpn-billing-logging-and-lambda-extra-charges
  claim: If you enable connection logging you must create a CloudWatch Logs log group and charges apply for it. If you enable the client connect handler you create and invoke a Lambda function, and Lambda charges apply.
  scope: Client VPN optional features.
  link: [Charges apply for using log groups](../facts/client-vpn.md#client-vpn-billing-logging-and-lambda-extra-charges)
  link: [Charges apply for invoking Lambda functions](../facts/client-vpn.md#client-vpn-billing-logging-and-lambda-extra-charges)
client-vpn-certificate-revocation-list-supported
  claim: Client VPN supports a statically configured Certificate Revocation List (CRL), so you can block specific client certificates.
  scope: Client VPN mutual authentication.
  link: [statically-configured Certificate Revocation List (CRL)](../facts/client-vpn.md#client-vpn-certificate-revocation-list-supported)
  link: [revoke access to a Client VPN endpoint](../facts/client-vpn.md#client-vpn-certificate-revocation-list-supported)
client-vpn-change-client-route-enforcement
  claim: On April 20, 2025 Client VPN added the client route enforcement feature.
  scope: per Client VPN endpoint; fixed.
  link: [client route enforcement feature](../facts/client-vpn.md#client-vpn-change-client-route-enforcement)
client-vpn-change-concurrent-connections-per-client
  claim: On January 22, 2025 Client VPN added concurrent VPN connections: a user can connect to multiple VPN profiles at the same time, with the AWS-supplied client version 5.0 or later; before, only one VPN profile at a time.
  scope: AWS-supplied Client VPN client; fixed.
  link: [connect to multiple VPN profiles](../facts/client-vpn.md#client-vpn-change-concurrent-connections-per-client)
  changed: 2025-01-22: was you could only connect to one VPN profile at a time
client-vpn-change-device-posture-2026-10
  claim: On October 5, 2026 Client VPN added device posture assessment: it can check device signals from CrowdStrike, Jamf or JumpCloud before it allows a connection. Before that, Client VPN authenticated users through certificates, SAML, or Active Directory.
  scope: per Client VPN endpoint; fixed; requires AWS VPN Client version 6.2.0 or later.
  link: [device posture assessment](../facts/client-vpn.md#client-vpn-change-device-posture-2026-10)
  link: [Oct 5, 2026](../facts/client-vpn.md#client-vpn-change-device-posture-2026-10)
  changed: 2026-10-05: was Client VPN authenticated users through certificates, SAML, or Active Directory
client-vpn-change-disconnect-on-session-timeout
  claim: On January 13, 2025 Client VPN session timeout gained support for disconnect on session timeout, which applies when the maximum session duration is reached.
  scope: per Client VPN endpoint; fixed.
  link: [disconnect on session timeout](../facts/client-vpn.md#client-vpn-change-disconnect-on-session-timeout)
client-vpn-change-ipv6-support
  claim: On August 26, 2025 Client VPN added support for IPv6 resources through IPv6-only or dual-stack endpoints; before, it supported remote access only to IPv4-enabled AWS workloads.
  scope: per Client VPN endpoint; fixed.
  link: [IPv6-only or dual-stack Client VPN endpoints](../facts/client-vpn.md#client-vpn-change-ipv6-support)
  changed: 2025-08-26: was Client VPN only supported remote access to IPv4-enabled AWS workloads
client-vpn-change-quota-increase-2025-03
  claim: On March 13, 2025 the Client VPN authorization rules per endpoint quota increased from 50 to 200.
  scope: per Client VPN endpoint; fixed.
  link: [from 50 to 200](../facts/client-vpn.md#client-vpn-change-quota-increase-2025-03)
  changed: 2025-03-13: was from 50 to 200
client-vpn-change-transit-gateway-integration
  claim: On April 23, 2026 Client VPN added native Transit Gateway integration: the endpoint attaches to a transit gateway, which removes the intermediate VPC that connecting Client VPN to multiple VPCs needed.
  scope: per Client VPN endpoint; fixed.
  link: [Native Transit Gateway attachment](../facts/client-vpn.md#client-vpn-change-transit-gateway-integration)
  changed: 2026-04-23: was connecting Client VPN to multiple VPCs required provisioning and managing an intermediate VPC
client-vpn-change-vpn-client-v6
  claim: AWS Client VPN introduced a rebuilt AWS VPN Client v6.0.x with command-line interface support, enterprise administrative controls and faster connection establishment.
  scope: per client device; fixed.
  link: [AWS VPN Client v6.0.x](../facts/client-vpn.md#client-vpn-change-vpn-client-v6)
client-vpn-client-cidr-between-slash-22-and-slash-12
  claim: Client CIDR ranges must have a block size of at least /22 and must not be larger than /12.
  scope: Client VPN client CIDR range; maximum.
  link: [must not be greater than /12](../facts/client-vpn.md#client-vpn-client-cidr-between-slash-22-and-slash-12)
  link: [at least /22](../facts/client-vpn.md#client-vpn-client-cidr-between-slash-22-and-slash-12)
client-vpn-client-cidr-cannot-change-after-creation
  claim: The client CIDR range cannot be changed after you create the Client VPN endpoint, and you should plan twice the addresses you need for the maximum concurrent connections.
  scope: Client VPN endpoint.
  link: [The client CIDR range cannot be changed](../facts/client-vpn.md#client-vpn-client-cidr-cannot-change-after-creation)
  link: [twice the number of IP addresses](../facts/client-vpn.md#client-vpn-client-cidr-cannot-change-after-creation)
client-vpn-client-cidr-no-overlap-with-vpc-or-routes
  claim: Client CIDR ranges cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or with any routes manually added to the Client VPN endpoint's route table.
  scope: Client VPN client CIDR range.
  link: [overlap with the local CIDR of the VPC](../facts/client-vpn.md#client-vpn-client-cidr-no-overlap-with-vpc-or-routes)
  link: [any routes manually added](../facts/client-vpn.md#client-vpn-client-cidr-no-overlap-with-vpc-or-routes)
client-vpn-connect-handler-lambda-authorizes-connection
  claim: A client connect handler lets you run custom logic that authorizes a new connection based on device, user and connection attributes. Currently the only supported type of client connect handler is an AWS Lambda function.
  scope: Client VPN endpoint.
  link: [run custom logic that authorizes a new connection](../facts/client-vpn.md#client-vpn-connect-handler-lambda-authorizes-connection)
  link: [supported is a Lambda function](../facts/client-vpn.md#client-vpn-connect-handler-lambda-authorizes-connection)
client-vpn-connection-logging-cloudwatch-logs
  claim: Connection logging captures connection events such as a client connecting, attempting to connect or disconnecting, and the logs are published to a CloudWatch Logs log group in your account. Failed mutual authentication attempts are not logged.
  scope: Client VPN connection logging.
  link: [published to a CloudWatch Logs log group](../facts/client-vpn.md#client-vpn-connection-logging-cloudwatch-logs)
  link: [Failed mutual authentication attempts are not logged](../facts/client-vpn.md#client-vpn-connection-logging-cloudwatch-logs)
client-vpn-cre-enforces-routes-on-connected-device
  claim: Client Route Enforcement enforces administrator-defined routes on devices connected through the VPN, so network traffic from a connected client is not inadvertently sent outside the VPN tunnel.
  scope: Client VPN Client Route Enforcement.
  link: [enforce administrator-defined routes on devices](../facts/client-vpn.md#client-vpn-cre-enforces-routes-on-connected-device)
  link: [not inadvertently sent outside the VPN tunnel](../facts/client-vpn.md#client-vpn-cre-enforces-routes-on-connected-device)
client-vpn-default-session-duration-24-hours
  claim: By default, the maximum VPN session duration of a Client VPN endpoint is 24 hours; you can configure a shorter maximum duration.
  scope: per Client VPN endpoint; default; adjustable.
  link: [24 hours](../facts/client-vpn.md#client-vpn-default-session-duration-24-hours)
  say: twenty-four hours
client-vpn-default-tgw-availability-zones-2
  claim: When you attach a Client VPN endpoint to a Transit Gateway and do not specify Availability Zones, AWS selects 2 Availability Zones automatically.
  scope: per Client VPN endpoint; default; adjustable.
  link: [2 Availability Zones](../facts/client-vpn.md#client-vpn-default-tgw-availability-zones-2)
  say: two Availability Zones
client-vpn-definition-managed-client-based-vpn-openvpn
  claim: AWS Client VPN is a managed client-based VPN service that lets you securely access your AWS resources and resources in your on-premises network from any location using an OpenVPN-based VPN client.
  scope: AWS Client VPN.
  link: [a managed client-based VPN service](../facts/client-vpn.md#client-vpn-definition-managed-client-based-vpn-openvpn)
  link: [using an OpenVPN-based VPN client](../facts/client-vpn.md#client-vpn-definition-managed-client-based-vpn-openvpn)
client-vpn-device-posture-controls-access-by-device-health
  claim: With AWS Client VPN device posture, you can control access to your network based on the security health of the connecting device, not just the identity of the user.
  scope: Client VPN device posture.
  link: [the security health of the connecting device](../facts/client-vpn.md#client-vpn-device-posture-controls-access-by-device-health)
  link: [not just the identity of the user](../facts/client-vpn.md#client-vpn-device-posture-controls-access-by-device-health)
client-vpn-endpoint-regional-sessions-terminate-there
  claim: The Client VPN endpoint is a Regional construct that you configure. The VPN sessions of the end users terminate at the endpoint.
  scope: Client VPN endpoint.
  link: [The Client VPN endpoint is a regional construct](../facts/client-vpn.md#client-vpn-endpoint-regional-sessions-terminate-there)
  link: [terminate at the Client VPN endpoint](../facts/client-vpn.md#client-vpn-endpoint-regional-sessions-terminate-there)
client-vpn-faq-acm-subordinate-ca-rotation
  claim: You can use AWS Certificate Manager as a subordinate CA chained to an external root CA; ACM then generates the server certificate for AWS Client VPN and also rotates it.
  scope: Client VPN server certificate; ACM used as a subordinate CA chained to an external root CA.
  link: [subordinate CA chained to an external root CA](../facts/client-vpn.md#client-vpn-faq-acm-subordinate-ca-rotation)
client-vpn-faq-authorization-rules-by-group
  claim: You configure authorization rules that limit which users can access a network: for a destination network you name the Active Directory group or identity provider group that is allowed, and only users in that group can access the network.
  scope: per destination network.
  link: [rules that limit the users who can access](../facts/client-vpn.md#client-vpn-faq-authorization-rules-by-group)
client-vpn-faq-connection-logs-15-minutes
  claim: Client VPN exports the connection log as a best effort to CloudWatch Logs, periodically at 15 minute intervals; the logs include details on created and terminated connection requests.
  scope: per Client VPN endpoint; exported as a best effort.
  link: [15 minute intervals](../facts/client-vpn.md#client-vpn-faq-connection-logs-15-minutes)
  say: every fifteen minutes
client-vpn-faq-cross-region-via-peering
  claim: To reach a VPC in a different Region by private IP address, set up a cross-region peering connection between that VPC and the Client VPN associated VPC, and add a route and an access rule for the destination VPC in the Client VPN endpoint.
  scope: Client VPN endpoint and VPCs in other Regions.
  link: [set up a cross-region peering connection](../facts/client-vpn.md#client-vpn-faq-cross-region-via-peering)
  say: peer the VPCs across Regions, then add a route and rule
client-vpn-faq-federated-metadata-update-hours
  claim: With federated authentication you can upload a new metadata document in the IAM identity provider associated with the Client VPN endpoint, and updated metadata is reflected in 2 to 4 hours.
  scope: per Client VPN endpoint with federated authentication.
  link: [2 to 4 hours](../facts/client-vpn.md#client-vpn-faq-federated-metadata-update-hours)
  say: two to four hours
client-vpn-faq-flow-logs-in-associated-vpc
  claim: Client VPN does not support Amazon VPC Flow Logs on the endpoint; you can use VPC Flow Logs in the associated VPC.
  scope: Client VPN endpoint logging.
  link: [Amazon VPC Flow Logs in the associated VPC](../facts/client-vpn.md#client-vpn-faq-flow-logs-in-associated-vpc)
client-vpn-faq-mfa-via-ad-or-idp
  claim: AWS Client VPN supports multi-factor authentication through Active Directory using AWS Directory Services and through external identity providers such as Okta.
  scope: Client VPN user authentication.
  link: [supports MFA through Active Directory](../facts/client-vpn.md#client-vpn-faq-mfa-via-ad-or-idp)
  say: MFA through Active Directory or an external identity provider
client-vpn-faq-monitor-and-terminate-connections
  claim: Using the CLI or console, you can view the current active connections of a Client VPN endpoint and terminate active connections.
  scope: per Client VPN endpoint.
  link: [terminate active connections](../facts/client-vpn.md#client-vpn-faq-monitor-and-terminate-connections)
  say: you can see and end active connections
client-vpn-faq-mutual-auth-root-certificate
  claim: AWS Client VPN supports mutual authentication; when it is enabled, the customer has to upload to the server the root certificate used to issue the client certificate.
  scope: Client VPN mutual authentication; mutual authentication enabled.
  link: [root certificate used to issue the client certificate](../facts/client-vpn.md#client-vpn-faq-mutual-auth-root-certificate)
client-vpn-faq-onprem-ad-via-directory-service
  claim: AWS Client VPN integrates with AWS Directory Service, which lets you connect to an on-premises Active Directory to authenticate users.
  scope: Client VPN Active Directory authentication.
  link: [integrates with AWS Directory Service](../facts/client-vpn.md#client-vpn-faq-onprem-ad-via-directory-service)
  say: through AWS Directory Service
client-vpn-faq-openvpn-protocol
  claim: AWS Client VPN, including the software client, supports the OpenVPN protocol.
  scope: AWS Client VPN and its software client.
  link: [supports the OpenVPN protocol](../facts/client-vpn.md#client-vpn-faq-openvpn-protocol)
  say: Client VPN uses the OpenVPN protocol
client-vpn-faq-security-group-default-applied
  claim: Client VPN supports security groups: you can specify a security group for the group of associations, and when a subnet is associated, the default security group of the subnet's VPC is applied automatically.
  scope: per subnet association; default; adjustable; applies when a subnet is associated.
  link: [apply the default security group of the VPC](../facts/client-vpn.md#client-vpn-faq-security-group-default-applied)
client-vpn-faq-security-group-restrict-app-to-vpn-users
  claim: To limit an application to Client VPN users, allow access only from the security groups that were applied to the associated subnet.
  scope: applications in the VPC of the associated subnet.
  link: [allow access only from the security groups](../facts/client-vpn.md#client-vpn-faq-security-group-restrict-app-to-vpn-users)
  say: allow only the security group applied to the associated subnet
client-vpn-faq-server-certificate-in-acm
  claim: To bring your own server certificate to AWS Client VPN, you upload the certificate, the root certification authority certificate and the server private key to AWS Certificate Manager.
  scope: Client VPN server certificate.
  link: [uploaded to AWS Certificate Manager](../facts/client-vpn.md#client-vpn-faq-server-certificate-in-acm)
  say: upload them to AWS Certificate Manager
client-vpn-faq-setup-admin-and-user-steps
  claim: The IT administrator creates a Client VPN endpoint, associates a target network and sets up access policies, then distributes the configuration file; end users download an OpenVPN client and use the file to create their VPN session.
  scope: Client VPN setup by the administrator and the end user.
  link: [creates a Client VPN endpoint](../facts/client-vpn.md#client-vpn-faq-setup-admin-and-user-steps)
client-vpn-faq-software-client-free
  claim: The AWS Client VPN software client is provided free of charge; you are billed only for AWS Client VPN service usage.
  scope: AWS-provided Client VPN software client.
  link: [provided free of charge](../facts/client-vpn.md#client-vpn-faq-software-client-free)
  say: the client software is free
client-vpn-faq-split-tunnel-routing
  claim: With split tunnel enabled, traffic for routes configured on the endpoint goes through the VPN tunnel and all other traffic uses the local network interface; with split tunnel disabled, all traffic from the device goes through the VPN tunnel.
  scope: per Client VPN endpoint; split tunnel enabled versus disabled.
  link: [routed via your local network interface](../facts/client-vpn.md#client-vpn-faq-split-tunnel-routing)
  link: [will traverse through the VPN tunnel](../facts/client-vpn.md#client-vpn-faq-split-tunnel-routing)
client-vpn-faq-target-network-is-subnet
  claim: A target network is a network that you associate to the Client VPN endpoint to give secure access to your AWS resources and to on-premises; currently the target network is a subnet in your Amazon VPC.
  scope: per Client VPN endpoint.
  link: [a subnet in your Amazon VPC](../facts/client-vpn.md#client-vpn-faq-target-network-is-subnet)
client-vpn-faq-transport-tcp-or-udp
  claim: You can choose either TCP or UDP for the Client VPN session.
  scope: per VPN session.
  link: [either TCP or UDP](../facts/client-vpn.md#client-vpn-faq-transport-tcp-or-udp)
  say: TCP or UDP
client-vpn-federated-idp-list-includes-iam-identity-center
  claim: The Client VPN guide lists AWS IAM Identity Center among the SAML-based identity providers you can configure for federated authentication, with a blog on using it for authentication and authorization.
  scope: Client VPN SAML-based federated authentication.
  link: [AWS IAM Identity Center](../facts/client-vpn.md#client-vpn-federated-idp-list-includes-iam-identity-center)
  link: [Using IAM Identity Center with AWS Client VPN](../facts/client-vpn.md#client-vpn-federated-idp-list-includes-iam-identity-center)
client-vpn-high-availability-multiple-subnets-different-azs
  claim: Each subnet associated with a Client VPN endpoint must be in a different Availability Zone, and AWS recommends associating at least two subnets for Availability Zone redundancy.
  scope: Client VPN endpoint.
  link: [associate at least two subnets](../facts/client-vpn.md#client-vpn-high-availability-multiple-subnets-different-azs)
  link: [associate multiple subnets with a Client VPN endpoint](../facts/client-vpn.md#client-vpn-high-availability-multiple-subnets-different-azs)
client-vpn-internet-access-rule-0-0-0-0-and-default-route
  claim: For internet access through Client VPN, add an authorization rule for 0.0.0.0/0, and make sure the route table of the associated subnets has a default route that targets an internet gateway or a NAT gateway.
  scope: Client VPN endpoint; clients that cannot reach the internet (troubleshooting steps).
  link: [For access to the internet, add an authorization rule for 0.0.0.0/0](../facts/client-vpn.md#client-vpn-internet-access-rule-0-0-0-0-and-default-route)
  link: [default route that targets either an internet gateway](../facts/client-vpn.md#client-vpn-internet-access-rule-0-0-0-0-and-default-route)
client-vpn-limit-baseline-bandwidth-50-mbps
  claim: Each Client VPN user connection has a maximum baseline bandwidth of 50 Mbps; if you hit the maximum bandwidth limit you can request an increase through AWS Support.
  scope: per user connection; maximum; adjustable.
  link: [maximum baseline bandwidth of 50 Mbps](../facts/client-vpn.md#client-vpn-limit-baseline-bandwidth-50-mbps)
  say: fifty megabits per second
client-vpn-limit-device-posture-reevaluation-5-minutes
  claim: With device posture, Client VPN evaluates the authorization policy when a device connects and again every 5 minutes for the life of the session.
  scope: per session; fixed; not adjustable.
  link: [every 5 minutes](../facts/client-vpn.md#client-vpn-limit-device-posture-reevaluation-5-minutes)
  say: every five minutes
client-vpn-limit-login-banner-1400-characters
  claim: The client login banner text of a Client VPN endpoint can have a maximum of 1400 characters, in UTF-8 encoded characters only.
  scope: per Client VPN endpoint; maximum; not adjustable.
  link: [1400 characters](../facts/client-vpn.md#client-vpn-limit-login-banner-1400-characters)
  say: fourteen hundred characters
client-vpn-limit-minimum-bandwidth-10-mbps
  claim: A minimum bandwidth of 10 Mbps is supported per Client VPN user connection.
  scope: per user connection; minimum; not adjustable.
  link: [10 Mbps](../facts/client-vpn.md#client-vpn-limit-minimum-bandwidth-10-mbps)
  say: ten megabits per second
client-vpn-limit-tgw-availability-zones
  claim: A Client VPN endpoint attached to a Transit Gateway can specify up to 5 Availability Zones.
  scope: per Client VPN endpoint; maximum; not adjustable.
  link: [up to 5 Availability Zones](../facts/client-vpn.md#client-vpn-limit-tgw-availability-zones)
  say: up to five Availability Zones
client-vpn-limit-username-length-1024-bytes
  claim: The maximum username length is 1024 bytes, and Client VPN rejects connections with longer usernames.
  scope: per user name; maximum; not adjustable.
  link: [1024 bytes](../facts/client-vpn.md#client-vpn-limit-username-length-1024-bytes)
  say: one thousand twenty-four bytes
client-vpn-mfa-with-active-directory-and-idp
  claim: Client VPN supports multi-factor authentication (MFA) when it is enabled for AWS Managed Microsoft AD or AD Connector, and when it is enabled in your SAML identity provider.
  scope: Client VPN authentication.
  link: [AWS Managed Microsoft AD or AD Connector](../facts/client-vpn.md#client-vpn-mfa-with-active-directory-and-idp)
  link: [supported when it's enabled in your IdP](../facts/client-vpn.md#client-vpn-mfa-with-active-directory-and-idp)
client-vpn-mutual-auth-certificates-server-cert-in-acm
  claim: With mutual authentication, Client VPN uses certificates to authenticate between the client and the server. You must upload the server certificate to AWS Certificate Manager and specify it when you create the endpoint.
  scope: Client VPN mutual authentication.
  link: [uses certificates to perform authentication](../facts/client-vpn.md#client-vpn-mutual-auth-certificates-server-cert-in-acm)
  link: [upload the server certificate to AWS Certificate Manager](../facts/client-vpn.md#client-vpn-mutual-auth-certificates-server-cert-in-acm)
client-vpn-no-dedicated-tenancy-vpc-subnet-association
  claim: A Client VPN endpoint does not support subnet associations in a dedicated tenancy VPC.
  scope: Client VPN target networks.
  link: [subnet associations in a dedicated tenancy VPC](../facts/client-vpn.md#client-vpn-no-dedicated-tenancy-vpc-subnet-association)
  link: [dedicated tenancy VPC](../facts/client-vpn.md#client-vpn-no-dedicated-tenancy-vpc-subnet-association)
client-vpn-no-traffic-initiated-toward-client-device
  claim: A resource cannot initiate any traffic or connection towards a user's device using Client VPN.
  scope: Client VPN.
  link: [a resource cannot initiate any traffic or connection](../facts/client-vpn.md#client-vpn-no-traffic-initiated-toward-client-device)
  link: [towards a user's device](../facts/client-vpn.md#client-vpn-no-traffic-initiated-toward-client-device)
client-vpn-options-row-openvpn-clients-only
  claim: The software remote access options table lists AWS Client VPN as an AWS managed remote access solution to Amazon VPC and internal networks, with managed high availability and scalability, and a limitation of OpenVPN clients only.
  scope: software remote access connectivity options table.
  link: [OpenVPN clients only](../facts/client-vpn.md#client-vpn-options-row-openvpn-clients-only)
  link: [AWS managed remote access solution to Amazon VPC](../facts/client-vpn.md#client-vpn-options-row-openvpn-clients-only)
client-vpn-other-networks-need-route-and-authorization-rule
  claim: To enable connectivity to other networks, add a route to the specific network in the Client VPN route table and add an authorization rule that enables access to that network.
  scope: Client VPN endpoint.
  link: [add a route to the specific network](../facts/client-vpn.md#client-vpn-other-networks-need-route-and-authorization-rule)
  link: [add authorization rule enabling access](../facts/client-vpn.md#client-vpn-other-networks-need-route-and-authorization-rule)
client-vpn-ports-443-1194-default-443
  claim: AWS Client VPN supports ports 443 and 1194 for both TCP and UDP. The default is port 443.
  scope: Client VPN endpoint; default; adjustable; you can choose port 1194 instead.
  link: [ports 443 and 1194 for both TCP and UDP](../facts/client-vpn.md#client-vpn-ports-443-1194-default-443)
  link: [The default is port 443](../facts/client-vpn.md#client-vpn-ports-443-1194-default-443)
client-vpn-pricing-endpoint-and-connection-hourly-fees
  claim: In the AWS pricing example for Client VPN, you pay an endpoint hourly fee for the Client VPN endpoint and a connection hourly fee for the active Client VPN connections.
  scope: per Client VPN endpoint and per connection.
  link: [endpoint hourly fee](../facts/client-vpn.md#client-vpn-pricing-endpoint-and-connection-hourly-fees)
  link: [connection hourly fee](../facts/client-vpn.md#client-vpn-pricing-endpoint-and-connection-hourly-fees)
client-vpn-pricing-public-ipv4-address-charge
  claim: Each Client VPN connection uses a unique public IPv4 address for the tunnels, and you incur standard public IPv4 address charges on it.
  scope: per Client VPN connection.
  link: [standard public IPv4 address charges](../facts/client-vpn.md#client-vpn-pricing-public-ipv4-address-charge)
client-vpn-quota-authorization-policy-size
  claim: The authorization policy document of a Client VPN endpoint can be 10,000 bytes; this quota cannot be increased.
  scope: per Client VPN endpoint; maximum; not adjustable.
  link: [10,000 bytes](../facts/client-vpn.md#client-vpn-quota-authorization-policy-size)
  say: ten thousand bytes
client-vpn-quota-authorization-rules-per-endpoint
  claim: The default quota is 200 authorization rules per Client VPN endpoint, shared between IPv4 and IPv6 routes on dual-stack endpoints, and you can request an increase. Before March 2025 the default was 50.
  scope: per Client VPN endpoint; default; adjustable.
  link: [200 authorization rules](../facts/client-vpn.md#client-vpn-quota-authorization-rules-per-endpoint)
  say: two hundred
  changed: 2025-03-18: was 50 authorization rules per endpoint
client-vpn-quota-concurrent-connections-per-endpoint
  claim: The concurrent client connections per Client VPN endpoint depend on the number of subnet associations: 7,000 with 1 subnet, 36,500 with 2, 66,500 with 3, 96,500 with 4 and 126,000 with 5; on dual-stack endpoints the limit is shared between IPv4 and IPv6 connections, and you can request an increase.
  scope: per Client VPN endpoint, by number of subnet associations; default; adjustable; depends on the number of subnet associations per endpoint.
  link: [7,000](../facts/client-vpn.md#client-vpn-quota-concurrent-connections-per-endpoint)
  link: [36,500](../facts/client-vpn.md#client-vpn-quota-concurrent-connections-per-endpoint)
  link: [66,500](../facts/client-vpn.md#client-vpn-quota-concurrent-connections-per-endpoint)
  link: [96,500](../facts/client-vpn.md#client-vpn-quota-concurrent-connections-per-endpoint)
  link: [126,000](../facts/client-vpn.md#client-vpn-quota-concurrent-connections-per-endpoint)
  say: seven thousand | thirty-six thousand five hundred | sixty-six thousand five hundred | ninety-six thousand five hundred | one hundred twenty-six thousand
client-vpn-quota-concurrent-operations
  claim: The quota is 10 concurrent operations per Client VPN endpoint, and it cannot be increased.
  scope: per Client VPN endpoint; maximum; not adjustable.
  link: [10 concurrent operations](../facts/client-vpn.md#client-vpn-quota-concurrent-operations)
  say: ten
client-vpn-quota-crl-entries
  claim: A client certificate revocation list for Client VPN endpoints can have 20,000 entries; this quota cannot be increased.
  scope: per client certificate revocation list; maximum; not adjustable.
  link: [20,000 entries](../facts/client-vpn.md#client-vpn-quota-crl-entries)
  say: twenty thousand
client-vpn-quota-endpoints-per-region
  claim: The default quota is 5 Client VPN endpoints per Region, and you can request an increase.
  scope: per Region, per account; default; adjustable.
  link: [5 Client VPN endpoints](../facts/client-vpn.md#client-vpn-quota-endpoints-per-region)
  say: five
client-vpn-quota-groups-per-user
  claim: With Active Directory or a SAML-based identity provider, a user can belong to at most 200 groups, and Client VPN ignores any groups after the 200th group.
  scope: per user; maximum; not adjustable.
  link: [200 groups](../facts/client-vpn.md#client-vpn-quota-groups-per-user)
  say: two hundred
client-vpn-quota-routes-per-association
  claim: The default quota is 100 routes per Client VPN target network association, shared between IPv4 and IPv6 routes on dual-stack endpoints, and you can request an increase. Before the increase the default was 10.
  scope: per Client VPN target network association; default; adjustable.
  link: [100 routes](../facts/client-vpn.md#client-vpn-quota-routes-per-association)
  say: one hundred
  changed: 2025-03-18: was 10 routes per association
client-vpn-remote-access-preferred-by-smaller-companies
  claim: A software remote access VPN is typically preferred by smaller companies with less extensive remote networks or that have not already built and deployed remote access solutions for their employees.
  scope: software remote access VPN.
  link: [typically preferred by smaller companies](../facts/client-vpn.md#client-vpn-remote-access-preferred-by-smaller-companies)
  link: [low cost, elastic, and secure services](../facts/client-vpn.md#client-vpn-remote-access-preferred-by-smaller-companies)
client-vpn-restriction-tgw-no-mixing-associations
  claim: You cannot mix VPC subnet associations and Transit Gateway associations in a single Client VPN endpoint; you choose one association type when you create the endpoint.
  scope: per Client VPN endpoint; fixed.
  link: [mix VPC subnet associations and Transit Gateway associations](../facts/client-vpn.md#client-vpn-restriction-tgw-no-mixing-associations)
client-vpn-restriction-tgw-no-route-propagation
  claim: For Client VPN endpoints attached to a Transit Gateway, automatic route propagation from the Transit Gateway is not supported.
  scope: per Client VPN endpoint; fixed.
  link: [route propagation from Transit Gateway is not supported](../facts/client-vpn.md#client-vpn-restriction-tgw-no-route-propagation)
client-vpn-restriction-tgw-no-security-group-authorization
  claim: For Client VPN endpoints attached to a Transit Gateway, security group-based authorization is not supported; you use network-based authorization rules only.
  scope: per Client VPN endpoint; fixed.
  link: [Security group-based authorization is not supported](../facts/client-vpn.md#client-vpn-restriction-tgw-no-security-group-authorization)
client-vpn-route-table-subnet-association-adds-vpc-route
  claim: When you associate a subnet with a Client VPN endpoint, a route for the VPC is automatically added to the endpoint route table. To reach other networks you must add a route manually.
  scope: Client VPN endpoint route table.
  link: [a route for the VPC is automatically added](../facts/client-vpn.md#client-vpn-route-table-subnet-association-adds-vpc-route)
  link: [you must manually add a route](../facts/client-vpn.md#client-vpn-route-table-subnet-association-adds-vpc-route)
client-vpn-saml-federated-authentication-single-idp
  claim: Client VPN supports identity federation with SAML 2.0, so users connect with centralized credentials from an identity provider. A Client VPN endpoint supports a single IdP only.
  scope: Client VPN endpoint.
  link: [AWS Client VPN supports identity federation with Security Assertion Markup Language 2.0 (SAML 2.0)](../facts/client-vpn.md#client-vpn-saml-federated-authentication-single-idp)
  link: [supports a single IdP only](../facts/client-vpn.md#client-vpn-saml-federated-authentication-single-idp)
client-vpn-saml-requires-aws-provided-client
  claim: With SAML-based federated authentication, users must use the AWS provided client to connect, and a third-party OpenVPN client cannot be used.
  scope: Client VPN endpoints with federated authentication.
  link: [must use the AWS provided client to connect](../facts/client-vpn.md#client-vpn-saml-requires-aws-provided-client)
  link: [use the AWS Client VPN software client](../facts/client-vpn.md#client-vpn-saml-requires-aws-provided-client)
client-vpn-security-group-default-applied-to-association
  claim: When you associate a subnet with a Client VPN endpoint, AWS automatically applies the default security group of the VPC. You can change the security groups after you create the endpoint.
  scope: Client VPN target network association; default; adjustable; you can change the security groups after you create the endpoint.
  link: [we automatically apply the VPC's default security group](../facts/client-vpn.md#client-vpn-security-group-default-applied-to-association)
  link: [You can change the security groups](../facts/client-vpn.md#client-vpn-security-group-default-applied-to-association)
client-vpn-self-service-portal-download-client-and-config
  claim: The Client VPN self-service portal is a web page where end users download the latest AWS VPN Desktop Client and the latest endpoint configuration file. The administrator can enable or disable it for the endpoint.
  scope: Client VPN endpoint.
  link: [latest version of the AWS VPN Desktop Client](../facts/client-vpn.md#client-vpn-self-service-portal-download-client-and-config)
  link: [administrator can enable or disable the self-service portal](../facts/client-vpn.md#client-vpn-self-service-portal-download-client-and-config)
client-vpn-self-service-portal-not-for-mutual-auth
  claim: The self-service portal is not available for clients that authenticate using mutual authentication.
  scope: Client VPN self-service portal.
  link: [The self-service portal is not available](../facts/client-vpn.md#client-vpn-self-service-portal-not-for-mutual-auth)
  link: [self-service portal](../facts/client-vpn.md#client-vpn-self-service-portal-not-for-mutual-auth)
client-vpn-server-certificate-in-acm-always-required
  claim: To create a Client VPN endpoint you must provision a server certificate in AWS Certificate Manager, regardless of the type of authentication you use.
  scope: Client VPN endpoint creation.
  link: [provision a server certificate in AWS Certificate Manager](../facts/client-vpn.md#client-vpn-server-certificate-in-acm-always-required)
  link: [regardless of the type of authentication](../facts/client-vpn.md#client-vpn-server-certificate-in-acm-always-required)
client-vpn-snat-ipv4-client-source-translated-to-eni
  claim: For IPv4 traffic, Client VPN applies source NAT: the source IP address from the client CIDR range is translated to the IP address of the Client VPN network interface. For IPv6 traffic, SNAT is not applied.
  scope: Client VPN traffic sent to the VPC.
  link: [is translated to the Client VPN network interface](../facts/client-vpn.md#client-vpn-snat-ipv4-client-source-translated-to-eni)
  link: [For IPv6 traffic, SNAT is not applied](../facts/client-vpn.md#client-vpn-snat-ipv4-client-source-translated-to-eni)
client-vpn-split-tunnel-benefit-lower-data-transfer-cost
  claim: Split-tunnel lets only AWS-destined traffic use the VPN tunnel, and it reduces the volume of outgoing traffic from AWS, which reduces the data transfer cost.
  scope: Client VPN split-tunnel.
  link: [reducing the data transfer cost](../facts/client-vpn.md#client-vpn-split-tunnel-benefit-lower-data-transfer-cost)
  link: [AWS destined traffic traverse the VPN tunnel](../facts/client-vpn.md#client-vpn-split-tunnel-benefit-lower-data-transfer-cost)
client-vpn-split-tunnel-default-off-all-traffic-through-tunnel
  claim: By default all traffic from Client VPN clients is routed over the VPN tunnel. With split-tunnel turned on, only traffic destined for a network that matches a route in the endpoint route table goes over the tunnel.
  scope: Client VPN endpoint; default; adjustable; enable split-tunnel on the endpoint.
  link: [all traffic from clients is routed](../facts/client-vpn.md#client-vpn-split-tunnel-default-off-all-traffic-through-tunnel)
  link: [only traffic with a destination to the network](../facts/client-vpn.md#client-vpn-split-tunnel-default-off-all-traffic-through-tunnel)
client-vpn-split-tunnel-disabled-by-default-at-creation
  claim: By default, split-tunnel on a Client VPN endpoint is disabled. You can turn it on for a new or an existing endpoint.
  scope: Client VPN endpoint; default; adjustable; enable at creation or modify later.
  link: [split-tunnel on a Client VPN endpoint is disabled](../facts/client-vpn.md#client-vpn-split-tunnel-disabled-by-default-at-creation)
  link: [on a new or existing Client VPN endpoint](../facts/client-vpn.md#client-vpn-split-tunnel-disabled-by-default-at-creation)
client-vpn-subnet-associations-add-connection-capacity
  claim: You can associate multiple subnets with a Client VPN endpoint for high availability and to enable additional connection capacity. The number of subnet associations also depends on the number of Availability Zones in the Region.
  scope: Client VPN endpoint.
  link: [to enable additional connection capacity](../facts/client-vpn.md#client-vpn-subnet-associations-add-connection-capacity)
  link: [depends on the number of Availability Zones](../facts/client-vpn.md#client-vpn-subnet-associations-add-connection-capacity)
client-vpn-subnet-same-account-as-endpoint
  claim: The subnet associated with a Client VPN endpoint has to be in the same account as the endpoint.
  scope: Client VPN target network association.
  link: [in the same account as Client VPN endpoint](../facts/client-vpn.md#client-vpn-subnet-same-account-as-endpoint)
client-vpn-subnets-same-vpc-one-per-availability-zone
  claim: The subnets associated with a Client VPN endpoint must be in the same VPC, and you cannot associate multiple subnets from the same Availability Zone.
  scope: Client VPN target network associations.
  link: [must be in the same VPC](../facts/client-vpn.md#client-vpn-subnets-same-vpc-one-per-availability-zone)
  link: [multiple subnets from the same Availability Zone](../facts/client-vpn.md#client-vpn-subnets-same-vpc-one-per-availability-zone)
client-vpn-target-network-is-subnet-at-least-one
  claim: A target network is a subnet in a VPC. A Client VPN endpoint must have at least one target network so that clients can connect to it and establish a VPN connection.
  scope: Client VPN endpoint; minimum.
  link: [target network is a subnet in a VPC](../facts/client-vpn.md#client-vpn-target-network-is-subnet-at-least-one)
  link: [must have at least one target network](../facts/client-vpn.md#client-vpn-target-network-is-subnet-at-least-one)
client-vpn-transport-default-udp-not-changeable
  claim: By default the Client VPN endpoint uses the UDP transport protocol; you can choose TCP at creation. You cannot change the transport protocol after you create the endpoint.
  scope: Client VPN endpoint; default; not adjustable; choose TCP when you create the endpoint.
  link: [uses the UDP transport protocol](../facts/client-vpn.md#client-vpn-transport-default-udp-not-changeable)
  link: [You cannot change the transport protocol](../facts/client-vpn.md#client-vpn-transport-default-udp-not-changeable)
client-vpn-vs-site-to-site-decision-guide-remote-users
  claim: The AWS networking decision guide says to consider AWS Client VPN to securely connect remote users to your VPCs.
  scope: AWS networking decision guide.
  link: [securely connect remote users to your VPCs](../facts/client-vpn.md#client-vpn-vs-site-to-site-decision-guide-remote-users)
  link: [remote users](../facts/client-vpn.md#client-vpn-vs-site-to-site-decision-guide-remote-users)
client-vpn-whitepaper-managed-secure-software-remote-access
  claim: AWS Client VPN is an AWS managed high availability and scalability service for secure software remote access, with a secure TLS connection between remote clients and your VPCs.
  scope: AWS Client VPN.
  link: [an AWS managed high availability and scalability service](../facts/client-vpn.md#client-vpn-whitepaper-managed-secure-software-remote-access)
  link: [a secure TLS connection](../facts/client-vpn.md#client-vpn-whitepaper-managed-secure-software-remote-access)
direct-connect-active-active-same-community-tag
  claim: To load balance across multiple Direct Connect connections (active/active), apply the same local preference community tag across the prefixes of the connections.
  scope: private and transit virtual interfaces.
  link: [apply the same community tag](../facts/direct-connect.md#direct-connect-active-active-same-community-tag)
  link: [load balance traffic across multiple Direct Connect connections](../facts/direct-connect.md#direct-connect-active-active-same-community-tag)
direct-connect-active-passive-higher-preference-on-primary
  claim: For failover across multiple Direct Connect connections (active/passive), apply a higher-preference community tag to the prefixes of the primary virtual interface and a lower preference to the backup virtual interface.
  scope: private and transit virtual interfaces.
  link: [a community tag with a higher preference](../facts/direct-connect.md#direct-connect-active-passive-higher-preference-on-primary)
  link: [lower preference to the prefixes for the backup](../facts/direct-connect.md#direct-connect-active-passive-higher-preference-on-primary)
direct-connect-allowed-prefixes-tgw-only-listed-prefixes-advertised
  claim: For transit gateway associations, only the allowed prefixes that you enter are advertised to on-premises, and they show as originating from the Direct Connect gateway ASN. For virtual private gateways the allowed prefixes act as a filter.
  scope: allowed prefixes list on a Direct Connect gateway.
  link: [only the allowed prefixes entered will be advertised](../facts/direct-connect.md#direct-connect-allowed-prefixes-tgw-only-listed-prefixes-advertised)
  link: [allow the same or smaller CIDRs](../facts/direct-connect.md#direct-connect-allowed-prefixes-tgw-only-listed-prefixes-advertised)
direct-connect-aws-is-not-first-or-last-mile-provider
  claim: AWS does not provide the first-mile or last-mile circuit. You make the connections between your local service providers and the Direct Connect location, or work with a Direct Connect Delivery Partner.
  scope: connecting on-premises locations to Direct Connect locations.
  link: [local service providers used at your on-premises locations](../facts/direct-connect.md#direct-connect-aws-is-not-first-or-last-mile-provider)
  link: [work with an AWS Direct Connect Delivery Partner](../facts/direct-connect.md#direct-connect-aws-is-not-first-or-last-mile-provider)
direct-connect-backup-lower-cost-vpn-primary-dx-with-vpn-backup
  claim: Some customers want one or more Direct Connect connections as primary connectivity, with a lower-cost backup connection. To achieve this they can establish Direct Connect connections with a VPN backup.
  scope: Direct Connect backup.
  link: [coupled with a lower-cost backup connection](../facts/direct-connect.md#direct-connect-backup-lower-cost-vpn-primary-dx-with-vpn-backup)
  link: [AWS Direct Connect connections with a VPN backup](../facts/direct-connect.md#direct-connect-backup-lower-cost-vpn-primary-dx-with-vpn-backup)
direct-connect-backup-vpn-bandwidth-limit-not-above-1-gbps
  claim: Site-to-Site VPN supports up to 1.25 Gbps throughput per tunnel and does not support ECMP for the egress path across several tunnels on the same virtual private gateway, so AWS does not recommend a VPN as the backup for Direct Connect connections faster than 1 Gbps.
  scope: VPN backup for Direct Connect, virtual private gateway.
  link: [we do not recommend customers use AWS Site to Site VPN as a backup for AWS Direct Connect connections with speeds greater than 1 Gbps](../facts/direct-connect.md#direct-connect-backup-vpn-bandwidth-limit-not-above-1-gbps)
  link: [up to 1.25 Gbps throughput per VPN tunnel](../facts/direct-connect.md#direct-connect-backup-vpn-bandwidth-limit-not-above-1-gbps)
direct-connect-backup-vpn-not-recommended-for-critical-workloads-cost-note
  claim: Combining Direct Connect as the primary path with a Site-to-Site VPN over the internet as backup is technically feasible and very cost effective, but it has technical downsides and can be more difficult to manage. AWS does not recommend it for highly critical or critical workloads.
  scope: VPN over the internet as backup for Direct Connect.
  link: [While technically feasible and very cost effective](../facts/direct-connect.md#direct-connect-backup-vpn-not-recommended-for-critical-workloads-cost-note)
  link: [AWS doesn’t recommend this for highly critical](../facts/direct-connect.md#direct-connect-backup-vpn-not-recommended-for-critical-workloads-cost-note)
direct-connect-backup-vpn-on-tgw-ecmp-up-to-50-gbps
  claim: A Site-to-Site VPN ending on a transit gateway can be a cost-effective backup for Direct Connect; ECMP across multiple VPN tunnels allows throughput up to 50Gbps, even though each tunnel is capped at 1.25 Gbps, and Direct Connect is still the most effective choice for stable connectivity.
  scope: VPN backup on a transit gateway.
  link: [as a cost-effective backup](../facts/direct-connect.md#direct-connect-backup-vpn-on-tgw-ecmp-up-to-50-gbps)
  link: [throughput of up to 50Gbps](../facts/direct-connect.md#direct-connect-backup-vpn-on-tgw-ecmp-up-to-50-gbps)
direct-connect-backup-vpn-vpc-traffic-fails-over-automatically
  claim: If you configured a backup IPsec VPN connection, all VPC traffic fails over to the VPN automatically, and traffic to public resources such as Amazon S3 goes over the internet. Without a backup Direct Connect link or IPsec VPN link, Amazon VPC traffic is dropped when the connection fails.
  scope: Direct Connect failure with and without a backup.
  link: [will failover to the VPN connection automatically](../facts/direct-connect.md#direct-connect-backup-vpn-vpc-traffic-fails-over-automatically)
  link: [Amazon VPC traffic will be dropped](../facts/direct-connect.md#direct-connect-backup-vpn-vpc-traffic-fails-over-automatically)
direct-connect-bandwidth-choose-per-throughput-and-failover-needs
  claim: Bandwidth requirements can change over time: initial deployment, normal operations, new workloads and failover scenarios can all need different bandwidth.
  scope: hybrid connectivity bandwidth.
  link: [the bandwidth requirements can change over time](../facts/direct-connect.md#direct-connect-bandwidth-choose-per-throughput-and-failover-needs)
  link: [can all have different bandwidth requirements](../facts/direct-connect.md#direct-connect-bandwidth-choose-per-throughput-and-failover-needs)
direct-connect-behavior-flat-rate-port-pair-no-extra-bandwidth
  claim: In flat-rate billing the second port of a port-pair exists solely for redundancy and does not add throughput; a 10 Gbps port-pair gives 10 Gbps of usable capacity, not 20 Gbps.
  scope: per port-pair; fixed.
  link: [10 Gbps, not 20 Gbps](../facts/direct-connect.md#direct-connect-behavior-flat-rate-port-pair-no-extra-bandwidth)
  say: ten gigabits per second, not twenty
direct-connect-behavior-hosted-traffic-policing
  claim: AWS uses traffic policing on hosted connections: when the traffic rate reaches the configured maximum rate, excess traffic is dropped, so bursty traffic can get a lower throughput than non-bursty traffic.
  scope: per hosted connection; fixed.
  link: [excess traffic is dropped](../facts/direct-connect.md#direct-connect-behavior-hosted-traffic-policing)
  link: [AWS uses traffic policing on hosted connections](../facts/direct-connect.md#direct-connect-behavior-hosted-traffic-policing)
direct-connect-behavior-jumbo-frames-update-30-seconds
  claim: Setting a virtual interface to jumbo frames can update the underlying physical connection, and that update disrupts connectivity for all virtual interfaces on the connection for up to 30 seconds.
  scope: per connection; maximum.
  link: [up to 30 seconds](../facts/direct-connect.md#direct-connect-behavior-jumbo-frames-update-30-seconds)
  say: up to thirty seconds
direct-connect-behavior-mtu-1500-when-routes-overlap
  claim: If two private virtual interfaces advertise the same route with different MTU values, or a Site-to-Site VPN advertises the same route, an MTU of 1500 is used.
  scope: per route; fixed.
  link: [1500 MTU](../facts/direct-connect.md#direct-connect-behavior-mtu-1500-when-routes-overlap)
  say: fifteen hundred
direct-connect-bfd-default-interval-300-multiplier-3
  claim: AWS sets the BFD liveness detection minimum interval to 300 and the BFD liveness detection multiplier to 3.
  scope: BFD on Direct Connect virtual interfaces; default; not adjustable; applies after BFD is configured on your router.
  link: [BFD liveness detection minimum interval to 300](../facts/direct-connect.md#direct-connect-bfd-default-interval-300-multiplier-3)
  link: [BFD liveness detection multiplier to 3](../facts/direct-connect.md#direct-connect-bfd-default-interval-300-multiplier-3)
direct-connect-bfd-enabled-on-aws-side-needs-router-config
  claim: Asynchronous BFD is automatically enabled for each Direct Connect virtual interface, but it does not take effect until you configure it on your router.
  scope: each Direct Connect virtual interface; default; not adjustable; takes effect only after you configure BFD on your router.
  link: [Asynchronous BFD is automatically enabled](../facts/direct-connect.md#direct-connect-bfd-enabled-on-aws-side-needs-router-config)
  link: [does not take effect until you configure it](../facts/direct-connect.md#direct-connect-bfd-enabled-on-aws-side-needs-router-config)
direct-connect-case-discover-transactions-into-s3
  claim: Using AWS Direct Connect, Discover migrates transactions into Amazon S3 for pricing and settlement.
  scope: one customer (Discover).
  link: [for pricing and settlement](../facts/direct-connect.md#direct-connect-case-discover-transactions-into-s3)
  link: [migrates transactions into Amazon S3](../facts/direct-connect.md#direct-connect-case-discover-transactions-into-s3)
direct-connect-case-nium-cloudhsm-direct-connect-clearing-systems
  claim: Nium combined AWS CloudHSM with AWS Direct Connect to establish direct and secure connections with clearing systems in Singapore and the Single Euro Payments Area.
  scope: one customer (Nium).
  link: [combined AWS CloudHSM with AWS Direct Connect](../facts/direct-connect.md#direct-connect-case-nium-cloudhsm-direct-connect-clearing-systems)
  link: [clearing systems in Singapore](../facts/direct-connect.md#direct-connect-case-nium-cloudhsm-direct-connect-clearing-systems)
direct-connect-change-4-byte-asn
  claim: Direct Connect virtual interfaces support 4-byte AS numbers, using the entire range supported by RFC 6793 up to 4,294,967,294; before, the limit was 65,536 possible 2-byte AS numbers.
  scope: per virtual interface; maximum.
  link: [up to 4,294,967,294](../facts/direct-connect.md#direct-connect-change-4-byte-asn)
  changed: 2025-09-12: was 65,536 possible 2-byte AS numbers
direct-connect-change-400g-dedicated
  claim: On July 18, 2024 the Direct Connect guide added support for 400G connections.
  scope: Direct Connect connections; fixed.
  link: [400G](../facts/direct-connect.md#direct-connect-change-400g-dedicated)
  say: four hundred gigabits
direct-connect-change-bgp-route-visibility
  claim: On July 30, 2026 Direct Connect added BGP route visibility: you can view the BGP routes AWS accepted from your router and the routes AWS advertises to you on your virtual interfaces.
  scope: per virtual interface; fixed.
  link: [BGP route visibility](../facts/direct-connect.md#direct-connect-change-bgp-route-visibility)
direct-connect-change-cloud-wan-association
  claim: On November 25, 2024 Direct Connect added the option to create a Direct Connect gateway association directly with an AWS Cloud WAN core network.
  scope: per Direct Connect gateway; fixed.
  link: [AWS Network Manager core network](../facts/direct-connect.md#direct-connect-change-cloud-wan-association)
direct-connect-change-flat-rate-billing
  claim: On September 15, 2026 Direct Connect added flat-rate billing for dedicated connections: for 10 Gbps and 100 Gbps connections it gives a single fixed monthly price that eliminates data transfer out charges within the selected pricing tier. Before, billing was pay-as-you-go.
  scope: per dedicated connection; fixed.
  link: [single fixed monthly price](../facts/direct-connect.md#direct-connect-change-flat-rate-billing)
  changed: 2026-09-15: was pay-as-you-go pricing, paying only for the port hours and data transfer out (DTO) they use
direct-connect-change-interconnect-last-mile-ga
  claim: AWS Interconnect - last mile became generally available as a fully managed way to connect branch offices, data centers and remote locations to AWS.
  scope: per account; fixed.
  link: [AWS Interconnect - last mile](../facts/direct-connect.md#direct-connect-change-interconnect-last-mile-ga)
direct-connect-change-interconnect-multicloud-ga
  claim: AWS Interconnect - multicloud became generally available, providing private, high-speed connections to other cloud service providers.
  scope: per account; fixed.
  link: [AWS Interconnect - multicloud](../facts/direct-connect.md#direct-connect-change-interconnect-multicloud-ga)
direct-connect-change-prefix-controls
  claim: Inbound prefix controls (announced 2026-08-20) let you allocate up to 1,000 prefixes each for IPv4 and IPv6 on a private or transit virtual interface; before, a VIF accepted a maximum of 100 route prefixes. The default allocation stays 100.
  scope: per private or transit virtual interface; maximum.
  link: [up to 1,000 prefixes each for IPv4 and IPv6](../facts/direct-connect.md#direct-connect-change-prefix-controls)
  changed: 2026-08-20: was a maximum of 100 route prefixes
direct-connect-change-vif-rate-limiters
  claim: VIF Rate Limiters let you set a maximum bandwidth for up to 10 VIFs on a dedicated connection, with increments from 50 Mbps to 1.6 Tbps when using a link aggregation group.
  scope: per dedicated connection; maximum.
  link: [up to 10 VIFs](../facts/direct-connect.md#direct-connect-change-vif-rate-limiters)
  link: [50 Mbps to 1.6 Tbps](../facts/direct-connect.md#direct-connect-change-vif-rate-limiters)
  say: up to ten VIFs | fifty megabits per second to one point six terabits per second
direct-connect-components-connection-and-virtual-interface
  claim: A connection is created in a Direct Connect location to link your premises to an AWS Region. A virtual interface is created to enable access to AWS services: public for public services such as Amazon S3, private for your VPC.
  scope: AWS Direct Connect.
  link: [from your premises to an AWS Region](../facts/direct-connect.md#direct-connect-components-connection-and-virtual-interface)
  link: [virtual interface to enable access to AWS services](../facts/direct-connect.md#direct-connect-components-connection-and-virtual-interface)
direct-connect-cost-calculate-breakeven-point
  claim: If you are not sure whether to use the internet or a private connection, calculate the breakeven point where Direct Connect becomes less expensive than the internet.
  scope: cost comparison of Direct Connect and the internet.
  link: [calculate a breakeven point](../facts/direct-connect.md#direct-connect-cost-calculate-breakeven-point)
  link: [the internet or a private connection](../facts/direct-connect.md#direct-connect-cost-calculate-breakeven-point)
direct-connect-cost-data-ingress-to-aws-is-free
  claim: Data ingress to AWS is free, and good application design keeps data processing within AWS to minimize unnecessary data egress charges.
  scope: hybrid connectivity data transfer.
  link: [Data ingress to AWS is free](../facts/direct-connect.md#direct-connect-cost-data-ingress-to-aws-is-free)
  link: [minimizes unnecessary data egress charges](../facts/direct-connect.md#direct-connect-cost-data-ingress-to-aws-is-free)
direct-connect-cost-permanent-high-volume-dx-temporary-vpn
  claim: If the data volume makes Direct Connect cheaper and you need permanent connectivity, Direct Connect is the optimal choice. If connectivity is temporary and the internet meets your other requirements, Site-to-Site VPN over the internet can be cheaper.
  scope: cost comparison of Direct Connect and VPN.
  link: [AWS Direct Connect is the optimal connectivity choice](../facts/direct-connect.md#direct-connect-cost-permanent-high-volume-dx-temporary-vpn)
  link: [it can be cheaper to use AWS S2S VPN over the internet due to the elasticity of the internet](../facts/direct-connect.md#direct-connect-cost-permanent-high-volume-dx-temporary-vpn)
direct-connect-cost-reduces-bandwidth-and-data-transfer-costs
  claim: Direct Connect can lower network cost in two ways: you reduce the bandwidth costs paid to your internet service provider, and data transferred over your dedicated connection is charged at the reduced Direct Connect data transfer rate instead of internet rates.
  scope: Direct Connect compared with internet data transfer.
  link: [bandwidth costs paid to your internet service provider](../facts/direct-connect.md#direct-connect-cost-reduces-bandwidth-and-data-transfer-costs)
  link: [the reduced AWS Direct Connect data transfer rate](../facts/direct-connect.md#direct-connect-cost-reduces-bandwidth-and-data-transfer-costs)
direct-connect-decision-guide-more-consistent-performance-than-internet
  claim: The AWS networking decision guide says to consider a direct connection from your on-premises network to AWS (Direct Connect) if you require more consistent performance than the internet can provide.
  scope: AWS networking decision guide.
  link: [more consistent performance than the internet can provide](../facts/direct-connect.md#direct-connect-decision-guide-more-consistent-performance-than-internet)
  link: [Direct Connect](../facts/direct-connect.md#direct-connect-decision-guide-more-consistent-performance-than-internet)
direct-connect-dedicated-billing-starts-port-active-or-90-days-after-loa
  claim: For a dedicated connection, billing starts when the port is active or 90 days after the LOA has been issued, whichever comes first. You avoid charges by deleting the port before activation or within 90 days of the LOA being issued.
  scope: dedicated connection port hours; fixed; whichever comes first.
  link: [Billing automatically starts when the port is active or 90 days after the LOA has been issued, whichever comes first](../facts/direct-connect.md#direct-connect-dedicated-billing-starts-port-active-or-90-days-after-loa)
  link: [deleting the port prior to activation or within 90 days of the LOA being issued](../facts/direct-connect.md#direct-connect-dedicated-billing-starts-port-active-or-90-days-after-loa)
direct-connect-dedicated-connection-physical-port-single-customer
  claim: A dedicated connection is a physical Ethernet connection associated with a single customer. You request it through the Direct Connect console, the CLI, or the API.
  scope: Direct Connect dedicated connection.
  link: [physical Ethernet connection associated with a single customer](../facts/direct-connect.md#direct-connect-dedicated-connection-physical-port-single-customer)
direct-connect-dedicated-info-request-respond-within-7-days
  claim: If AWS asks for more information about a dedicated connection request, you must respond within 7 days or the connection is deleted.
  scope: dedicated connection requests; maximum.
  link: [or the connection is deleted](../facts/direct-connect.md#direct-connect-dedicated-info-request-respond-within-7-days)
  link: [7 days](../facts/direct-connect.md#direct-connect-dedicated-info-request-respond-within-7-days)
direct-connect-dedicated-port-speed-fixed-after-request
  claim: You cannot change the port speed of a dedicated connection after you create the connection request. To change the speed you create and configure a new connection.
  scope: dedicated connections.
  link: [You can't change the port speed](../facts/direct-connect.md#direct-connect-dedicated-port-speed-fixed-after-request)
  link: [you must create and configure a new connection](../facts/direct-connect.md#direct-connect-dedicated-port-speed-fixed-after-request)
direct-connect-default-cloudwatch-5-minute-interval
  claim: By default, CloudWatch provides Direct Connect metric data in 5-minute intervals.
  scope: per metric; default; adjustable.
  link: [5-minute intervals](../facts/direct-connect.md#direct-connect-default-cloudwatch-5-minute-interval)
  say: five-minute intervals
direct-connect-default-dxgw-asn-64512
  claim: If you do not choose an ASN for the AWS side of the BGP session, AWS provides an ASN of 64512 for the Direct Connect gateway.
  scope: per Direct Connect gateway; default; adjustable.
  link: [ASN of 64512](../facts/direct-connect.md#direct-connect-default-dxgw-asn-64512)
  say: six four five one two
direct-connect-default-local-preference-region-distance-when-no-community
  claim: If you do not specify local preference communities for a private virtual interface, the default local preference is based on the distance from the local Region to the Direct Connect locations, and egress across multiple virtual interfaces from multiple locations may be arbitrary.
  scope: private virtual interface egress from AWS; default; adjustable; no local preference community is set.
  link: [default local preference is based on the distance](../facts/direct-connect.md#direct-connect-default-local-preference-region-distance-when-no-community)
  link: [egress behavior across multiple VIFs](../facts/direct-connect.md#direct-connect-default-local-preference-region-distance-when-no-community)
direct-connect-default-vifs-use-100-percent-capacity
  claim: By default, all VIFs on a Direct Connect connection can use 100% of the underlying connection's capacity, which is why one VIF can congest the others.
  scope: per VIF; default; adjustable.
  link: [100%](../facts/direct-connect.md#direct-connect-default-vifs-use-100-percent-capacity)
  say: one hundred percent
direct-connect-definition-fiber-cable-bypass-isp
  claim: Direct Connect links your internal network to a Direct Connect location over a standard Ethernet fiber-optic cable. Through it you create virtual interfaces to public AWS services or to Amazon VPC, bypassing internet service providers in your network path.
  scope: AWS Direct Connect.
  link: [over a standard Ethernet fiber-optic cable](../facts/direct-connect.md#direct-connect-definition-fiber-cable-bypass-isp)
  link: [bypassing internet service providers in your network path](../facts/direct-connect.md#direct-connect-definition-fiber-cable-bypass-isp)
  say: a standard Ethernet fiber-optic cable
direct-connect-design-dxgw-with-tgw-multi-region-public-vif-for-s3
  claim: In the Direct Connect gateway with transit gateways design for multiple Regions, a Direct Connect public virtual interface is used to access AWS public resources such as Amazon S3 directly over the Direct Connect connections, and the design scales up to thousands of VPCs per AWS Transit Gateway over a single BGP session.
  scope: DXGW with transit gateway, multi-Region reference design.
  link: [used to access AWS public resources](../facts/direct-connect.md#direct-connect-design-dxgw-with-tgw-multi-region-public-vif-for-s3)
  link: [thousands of VPCs per AWS Transit Gateway](../facts/direct-connect.md#direct-connect-design-dxgw-with-tgw-multi-region-public-vif-for-s3)
direct-connect-design-dxgw-with-vgw-single-region-dual-dx
  claim: The reference design for one Region uses dual Direct Connect connections to independent Direct Connect locations with a Direct Connect gateway attached to the VPCs through virtual private gateways. It offers automated failover with dynamic routing (BGP).
  scope: DXGW with VGW, single Region reference design.
  link: [Dual AWS Direct Connect Connections](../facts/direct-connect.md#direct-connect-design-dxgw-with-vgw-single-region-dual-dx)
  link: [Offers automated failover with dynamic routing (BGP)](../facts/direct-connect.md#direct-connect-design-dxgw-with-vgw-single-region-dual-dx)
direct-connect-design-tgw-adds-data-processing-cost-vgw-does-not
  claim: A design with a Direct Connect gateway and virtual private gateways does not incur transit gateway data processing cost between AWS and on-premises, while a design that uses a transit gateway incurs additional transit gateway processing cost for that data transfer.
  scope: DXGW with VGW versus DXGW with transit gateway.
  link: [not incur AWS Transit Gateway related processing cost](../facts/direct-connect.md#direct-connect-design-tgw-adds-data-processing-cost-vgw-does-not)
  link: [Incurs additional AWS Transit Gateway processing costs](../facts/direct-connect.md#direct-connect-design-tgw-adds-data-processing-cost-vgw-does-not)
direct-connect-dto-does-not-include-internet-transfers
  claim: Direct Connect data transfer out is data sent through the connections at your Direct Connect location. It does not transfer data over the internet, which is priced on the EC2 pricing page.
  scope: Direct Connect data transfer out.
  link: [It does not transfer data over the internet](../facts/direct-connect.md#direct-connect-dto-does-not-include-internet-transfers)
  link: [connections made at your AWS Direct Connect location](../facts/direct-connect.md#direct-connect-dto-does-not-include-internet-transfers)
direct-connect-dxgw-associates-with-tgw-for-many-vpcs
  claim: You associate a Direct Connect gateway with a transit gateway when you have multiple VPCs in the same Region.
  scope: Direct Connect gateway associations.
  link: [multiple VPCs in the same Region](../facts/direct-connect.md#direct-connect-dxgw-associates-with-tgw-for-many-vpcs)
direct-connect-dxgw-data-does-not-pass-through-only-routing-information
  claim: A Direct Connect gateway is a globally available service that distributes routing information like a BGP route reflector. Data does not pass through it; it only handles routing information.
  scope: Direct Connect gateway.
  link: [Data does not pass through a DXGW](../facts/direct-connect.md#direct-connect-dxgw-data-does-not-pass-through-only-routing-information)
  link: [similarly to BGP route reflectors](../facts/direct-connect.md#direct-connect-dxgw-data-does-not-pass-through-only-routing-information)
direct-connect-dxgw-ecmp-across-transit-vifs
  claim: A single Direct Connect gateway supports ECMP across multiple transit virtual interfaces, so AWS recommends using only a single Direct Connect gateway rather than several gateways to get ECMP.
  scope: Direct Connect gateway with transit virtual interfaces.
  link: [supports ECMP across multiple transit virtual interfaces](../facts/direct-connect.md#direct-connect-dxgw-ecmp-across-transit-vifs)
  link: [use only a single Direct Connect gateway](../facts/direct-connect.md#direct-connect-dxgw-ecmp-across-transit-vifs)
direct-connect-dxgw-global-resource-any-region-not-china
  claim: A Direct Connect gateway is a globally available resource. You can connect to any Region globally with it, including AWS GovCloud (US) but not the AWS China Regions.
  scope: Direct Connect gateway.
  link: [a globally available resource](../facts/direct-connect.md#direct-connect-dxgw-global-resource-any-region-not-china)
  link: [it does not include the AWS China Regions](../facts/direct-connect.md#direct-connect-dxgw-global-resource-any-region-not-china)
direct-connect-dxgw-multi-account-association-proposal
  claim: You can associate a Direct Connect gateway with a transit gateway owned by any AWS account. The transit gateway owner creates an association proposal and the Direct Connect gateway owner must accept it.
  scope: Direct Connect gateway and transit gateway associations.
  link: [owned by any AWS account](../facts/direct-connect.md#direct-connect-dxgw-multi-account-association-proposal)
  link: [must accept the association proposal](../facts/direct-connect.md#direct-connect-dxgw-multi-account-association-proposal)
direct-connect-dxgw-no-charge-remote-region-egress-and-port-hours-apply
  claim: There are no charges for using a Direct Connect gateway. You pay the applicable egress data charges based on the source remote Region, plus port hour charges.
  scope: Direct Connect gateway and remote Regions.
  link: [There are no charges for using](../facts/direct-connect.md#direct-connect-dxgw-no-charge-remote-region-egress-and-port-hours-apply)
  link: [applicable egress data charges](../facts/direct-connect.md#direct-connect-dxgw-no-charge-remote-region-egress-and-port-hours-apply)
direct-connect-dxgw-no-direct-traffic-between-attached-vifs
  claim: A Direct Connect gateway supports communication between attached private virtual interfaces and associated virtual private gateways only, and may enable a virtual private gateway to another private gateway. Traffic flows that are not supported include direct communication between the virtual interfaces attached to a single Direct Connect gateway, and between those virtual interfaces and a VPN connection on a virtual private gateway associated with the same Direct Connect gateway.
  scope: Direct Connect gateway with virtual private gateway associations.
  link: [Direct communication between the virtual interfaces](../facts/direct-connect.md#direct-connect-dxgw-no-direct-traffic-between-attached-vifs)
  link: [associated virtual private gateways only](../facts/direct-connect.md#direct-connect-dxgw-no-direct-traffic-between-attached-vifs)
direct-connect-dxgw-no-traffic-between-associated-gateways-with-supernet-exception
  claim: A Direct Connect gateway does not let gateway associations on the same gateway send traffic to each other. The exception is when a supernet is advertised across two or more VPCs whose virtual private gateways are associated to the same Direct Connect gateway and virtual interface.
  scope: associations on one Direct Connect gateway; exception: supernet advertised on the same virtual interface.
  link: [does not allow gateway associations](../facts/direct-connect.md#direct-connect-dxgw-no-traffic-between-associated-gateways-with-supernet-exception)
  link: [supernet is advertised across two or more VPCs](../facts/direct-connect.md#direct-connect-dxgw-no-traffic-between-associated-gateways-with-supernet-exception)
direct-connect-dxgw-not-between-vpn-and-vif
  claim: A Direct Connect gateway will not route traffic between a VPN and a Direct Connect virtual interface. For that you create a VPN in the Region of the virtual interface and attach both to the same virtual private gateway.
  scope: Direct Connect gateway.
  link: [will not route traffic between a VPN](../facts/direct-connect.md#direct-connect-dxgw-not-between-vpn-and-vif)
  link: [VIF and the VPN to the same VGW](../facts/direct-connect.md#direct-connect-dxgw-not-between-vpn-and-vif)
direct-connect-dxgw-one-vif-type-only
  claim: A Direct Connect gateway can only have one type of virtual interface attached, and a transit gateway can only be associated with a Direct Connect gateway that has a transit virtual interface attached.
  scope: Direct Connect gateway.
  link: [only have one type of virtual interface attached](../facts/direct-connect.md#direct-connect-dxgw-one-vif-type-only)
  link: [attached to transit virtual interface](../facts/direct-connect.md#direct-connect-dxgw-one-vif-type-only)
direct-connect-dxgw-route-reflectors-no-single-point-of-failure
  claim: A Direct Connect gateway acts as a distributed set of BGP route reflectors outside the data traffic path, so it creates no single point of failure and no dependency on specific Regions. High availability is built in, so you do not need multiple gateways for it.
  scope: Direct Connect gateway.
  link: [a distributed set of BGP route reflectors](../facts/direct-connect.md#direct-connect-dxgw-route-reflectors-no-single-point-of-failure)
  link: [it avoids creating a single point of failure](../facts/direct-connect.md#direct-connect-dxgw-route-reflectors-no-single-point-of-failure)
direct-connect-dxgw-tgw-association-takes-up-to-40-minutes
  claim: It can take up to 40 minutes to establish an association between a transit gateway and a Direct Connect gateway.
  scope: transit gateway association with a Direct Connect gateway; maximum; not adjustable.
  link: [up to 40 minutes](../facts/direct-connect.md#direct-connect-dxgw-tgw-association-takes-up-to-40-minutes)
direct-connect-dxgw-tgw-not-with-vgw-or-private-vif
  claim: You cannot attach a Direct Connect gateway to a transit gateway when the Direct Connect gateway is already associated with a virtual private gateway or is attached to a private virtual interface.
  scope: Direct Connect gateway.
  link: [already associated with a virtual private gateway](../facts/direct-connect.md#direct-connect-dxgw-tgw-not-with-vgw-or-private-vif)
  link: [is attached to a private virtual interface](../facts/direct-connect.md#direct-connect-dxgw-tgw-not-with-vgw-or-private-vif)
direct-connect-dxgw-vgw-reference-design-up-to-20-vpcs-per-dxgw
  claim: In the Direct Connect gateway with virtual private gateways design, up to 20 VPCs can be connected per Direct Connect gateway over a single BGP session. If you need more than 20, add Direct Connect gateways or consider Transit Gateway integration.
  scope: per Direct Connect gateway with virtual private gateways; maximum; not adjustable.
  link: [Up to 20 VPCs can be connected per DXGW over a single BGP session](../facts/direct-connect.md#direct-connect-dxgw-vgw-reference-design-up-to-20-vpcs-per-dxgw)
  link: [consider using Transit Gateway integration](../facts/direct-connect.md#direct-connect-dxgw-vgw-reference-design-up-to-20-vpcs-per-dxgw)
direct-connect-encrypt-private-connection-vpn-over-dx-or-macsec
  claim: If encryption in transit is required over a private network connection, establish a VPN over Direct Connect (over a public or transit virtual interface), or consider MACsec on a 10Gbps or 100Gbps dedicated connection.
  scope: encryption in transit over Direct Connect.
  link: [establish a VPN over Direct Connect](../facts/direct-connect.md#direct-connect-encrypt-private-connection-vpn-over-dx-or-macsec)
  link: [consider using MACsec on a 10Gbps or 100Gbps Dedicated connection](../facts/direct-connect.md#direct-connect-encrypt-private-connection-vpn-over-dx-or-macsec)
direct-connect-example-corp-vpn-for-dev-test-direct-connect-for-production
  claim: In the whitepaper's worked example, Example Corp. Automotive uses Site-to-Site VPN over the internet to a transit gateway for development and testing, and Direct Connect with a Direct Connect gateway and a second transit gateway for production traffic.
  scope: worked example in the hybrid connectivity whitepaper.
  link: [uses AWS S2S VPN over the internet terminating on AWS Transit Gateway for development and testing](../facts/direct-connect.md#direct-connect-example-corp-vpn-for-dev-test-direct-connect-for-production)
  link: [second AWS Transit Gateway for the production traffic](../facts/direct-connect.md#direct-connect-example-corp-vpn-for-dev-test-direct-connect-for-production)
direct-connect-failover-test-disables-bgp-session
  claim: The Direct Connect Failover Testing feature tests the resiliency of your connection by disabling the BGP session between your on-premises networks and AWS. It can be run from the console or the API.
  scope: Direct Connect Resiliency Toolkit failover test.
  link: [disabling the Border Gateway Protocol session](../facts/direct-connect.md#direct-connect-failover-test-disables-bgp-session)
  link: [the resiliency of your AWS Direct Connect connection](../facts/direct-connect.md#direct-connect-failover-test-disables-bgp-session)
direct-connect-failover-test-duration-1-to-180-minutes
  claim: You set the duration of a failover test between a minimum of 1 minute and a maximum of 180 minutes, and you can cancel the test while it is running.
  scope: per failover test; maximum; adjustable.
  link: [1 minute](../facts/direct-connect.md#direct-connect-failover-test-duration-1-to-180-minutes)
  link: [cancel the test while it is running](../facts/direct-connect.md#direct-connect-failover-test-duration-1-to-180-minutes)
  link: [180 minutes](../facts/direct-connect.md#direct-connect-failover-test-duration-1-to-180-minutes)
direct-connect-failover-test-history-kept-365-days
  claim: AWS preserves the failover test history for 365 days. If you delete the virtual interface, its test history is also deleted.
  scope: failover test history; fixed; not adjustable.
  link: [365 days](../facts/direct-connect.md#direct-connect-failover-test-history-kept-365-days)
  link: [your test history is also deleted](../facts/direct-connect.md#direct-connect-failover-test-history-kept-365-days)
direct-connect-failover-test-only-owner-of-vif-account
  claim: Only the owner of the AWS account that includes the virtual interface can initiate a failover test.
  scope: failover test.
  link: [Only the owner of the AWS account](../facts/direct-connect.md#direct-connect-failover-test-only-owner-of-vif-account)
  link: [the owner of the AWS account](../facts/direct-connect.md#direct-connect-failover-test-only-owner-of-vif-account)
direct-connect-failure-detection-bfd-for-dx-dpd-for-vpn
  claim: Failure detection can be improved with Dead Peer Detection (DPD) for VPN links and Bidirectional Forwarding Detection (BFD) for Direct Connect links.
  scope: failover time of hybrid links.
  link: [Bidirectional Forwarding Detection (BFD)](../facts/direct-connect.md#direct-connect-failure-detection-bfd-for-dx-dpd-for-vpn)
  link: [Dead Peer Detection (DPD) for VPN links](../facts/direct-connect.md#direct-connect-failure-detection-bfd-for-dx-dpd-for-vpn)
direct-connect-faq-bypasses-internet-dedicated-private
  claim: AWS Direct Connect bypasses the internet and uses dedicated, private network connections between your network and AWS.
  scope: Direct Connect compared with an IPsec VPN connection.
  link: [AWS Direct Connect bypasses the internet](../facts/direct-connect.md#direct-connect-faq-bypasses-internet-dedicated-private)
  link: [dedicated, private network connections](../facts/direct-connect.md#direct-connect-faq-bypasses-internet-dedicated-private)
  say: Direct Connect skips the internet and uses a private line
direct-connect-faq-cloudfront-origin-needs-public-vif
  claim: If you use Amazon CloudFront with an origin in your own data center, you can use Direct Connect to transfer the objects stored there. You must have a Direct Connect public VIF, you must import all Anycast routes if you filter route imports, and you must advertise your custom origin's prefix to AWS.
  scope: CloudFront origin reached over Direct Connect; origin in your own data center; route imports filtered.
  link: [You must have a Direct Connect Public VIF](../facts/direct-connect.md#direct-connect-faq-cloudfront-origin-needs-public-vif)
  say: a public virtual interface is required for a CloudFront origin
direct-connect-faq-dedicated-vs-hosted
  claim: A dedicated connection is made through a 1 Gbps, 10 Gbps, 100 Gbps, or 400 Gbps Ethernet port dedicated to a single customer, while hosted connections are sourced from an AWS Direct Connect Partner that has a network link between itself and AWS.
  scope: Direct Connect connection types.
  link: [Ethernet port dedicated to a single customer](../facts/direct-connect.md#direct-connect-faq-dedicated-vs-hosted)
  link: [sourced from a AWS Direct Connect Partner](../facts/direct-connect.md#direct-connect-faq-dedicated-vs-hosted)
  say: a dedicated connection is a port reserved for one customer | a hosted connection comes from a Direct Connect Partner
direct-connect-faq-dxgw-any-region-from-any-location
  claim: With an AWS Direct Connect gateway you can access any AWS Region from any AWS Direct Connect location, excluding China.
  scope: per Direct Connect gateway; excluding China.
  link: [any AWS Region](../facts/direct-connect.md#direct-connect-faq-dxgw-any-region-from-any-location)
direct-connect-faq-dxgw-asn-immutable-after-creation
  claim: You cannot modify the AWS side ASN of a Direct Connect gateway after creation; you delete the gateway and recreate it with the desired private ASN.
  scope: per Direct Connect gateway.
  link: [cannot modify the AWS side ASN after creation](../facts/direct-connect.md#direct-connect-faq-dxgw-asn-immutable-after-creation)
direct-connect-faq-dxgw-definition-global
  claim: An AWS Direct Connect gateway is a grouping of virtual private gateways and private virtual interfaces; it is a globally available resource that you can create in any Region and access from all other Regions.
  scope: per Direct Connect gateway.
  link: [a globally available resource](../facts/direct-connect.md#direct-connect-faq-dxgw-definition-global)
  say: a Direct Connect gateway is global
direct-connect-faq-dxgw-needs-vgw-attached-to-vpc
  claim: You cannot associate a virtual private gateway that is not attached to a VPC with an AWS Direct Connect gateway.
  scope: per virtual private gateway.
  link: [you cannot associate an unattached VGW](../facts/direct-connect.md#direct-connect-faq-dxgw-needs-vgw-attached-to-vpc)
  say: the virtual private gateway must be attached to a VPC first
direct-connect-faq-dxgw-no-cloudhub-support
  claim: AWS Direct Connect gateway does not support AWS VPN CloudHub functionality, but if a Site-to-Site VPN connection is on a virtual gateway associated with your Direct Connect gateway, you can use the VPN connection for failover.
  scope: per Direct Connect gateway; VPN connection to a virtual gateway associated with the Direct Connect gateway can be used for failover.
  link: [does not support AWS VPN CloudHub functionality](../facts/direct-connect.md#direct-connect-faq-dxgw-no-cloudhub-support)
  say: no CloudHub through a Direct Connect gateway, but a VPN can be the failover
direct-connect-faq-dxgw-no-vpc-to-vpc-routing
  claim: A Direct Connect gateway only routes traffic from Direct Connect VIFs to virtual private gateways associated with VPCs, so traffic between two VPCs on the same Direct Connect gateway does not work; to send traffic between two VPCs you must configure a VPC peering connection.
  scope: per Direct Connect gateway; VPCs associated with the same Direct Connect gateway.
  link: [you must configure a VPC peering connection](../facts/direct-connect.md#direct-connect-faq-dxgw-no-vpc-to-vpc-routing)
  say: a Direct Connect gateway does not route VPC to VPC; use VPC peering
direct-connect-faq-dxgw-share-private-vif-up-to-20-vpcs
  claim: With a Direct Connect gateway you can share one private virtual interface with up to 20 VPCs, which reduces the number of BGP sessions between your on-premises network and AWS.
  scope: per private virtual interface attached to a Direct Connect gateway; maximum; not adjustable.
  link: [up to 20 VPCs](../facts/direct-connect.md#direct-connect-faq-dxgw-share-private-vif-up-to-20-vpcs)
  say: up to twenty VPCs
direct-connect-faq-dxgw-shortest-path-not-home-region
  claim: With a Direct Connect gateway, traffic takes the shortest path between your Direct Connect location and the destination AWS Region, regardless of the home Region of the location; it does not go through the home Region.
  scope: per Direct Connect gateway.
  link: [your traffic will take the shortest path](../facts/direct-connect.md#direct-connect-faq-dxgw-shortest-path-not-home-region)
  say: traffic takes the shortest path, not via the home Region
direct-connect-faq-dxgw-transit-vif-dedicated-no-private-vif
  claim: Once a transit VIF is connected to an AWS Direct Connect gateway, that gateway cannot also host a private VIF; it is dedicated to the transit VIF.
  scope: per Direct Connect gateway; a transit VIF is connected to the gateway.
  link: [it is dedicated to the transit VIF](../facts/direct-connect.md#direct-connect-faq-dxgw-transit-vif-dedicated-no-private-vif)
  say: a Direct Connect gateway with a transit VIF cannot take a private VIF
direct-connect-faq-dxgw-up-to-six-transit-gateways
  claim: You can associate up to six transit gateways with an AWS Direct Connect gateway as long as the IP CIDR blocks announced from the transit gateways do not overlap.
  scope: per Direct Connect gateway; maximum; not adjustable; the IP CIDR blocks announced from the transit gateways do not overlap.
  link: [up to six Transit Gateway](../facts/direct-connect.md#direct-connect-faq-dxgw-up-to-six-transit-gateways)
  say: up to six transit gateways
direct-connect-faq-high-availability-multiple-locations
  claim: To achieve high availability connectivity to AWS, AWS recommends making connections at multiple AWS Direct Connect locations.
  scope: ordering Direct Connect connections for high availability.
  link: [making connections at multiple AWS Direct Connect locations](../facts/direct-connect.md#direct-connect-faq-high-availability-multiple-locations)
  say: connect at more than one Direct Connect location
direct-connect-faq-lag-active-active
  claim: Links in a LAG are in active/active mode: AWS ports send LACP Data Units continuously.
  scope: per LAG.
  link: [They are in active/active](../facts/direct-connect.md#direct-connect-faq-lag-active-active)
  say: LAG links are active/active
direct-connect-faq-lag-definition-lacp
  claim: A link aggregation group (LAG) is a logical interface that uses LACP to aggregate multiple dedicated connections at a single Direct Connect endpoint so you can treat them as one managed connection; the LAG configuration applies to all connections in the group.
  scope: per LAG; dedicated connections at a single Direct Connect endpoint.
  link: [uses the link aggregation control protocol](../facts/direct-connect.md#direct-connect-faq-lag-definition-lacp)
direct-connect-faq-lag-max-links
  claim: A LAG holds a maximum of 4 links when using 1 or 10 Gbps connections and 2 links when using 100 or 400 Gbps connections.
  scope: per LAG; maximum; not adjustable; 4 links for 1 or 10 Gbps connections; 2 links for 100 or 400 Gbps connections.
  link: [4x in a LAG group when using 1 or 10 Gbps connections](../facts/direct-connect.md#direct-connect-faq-lag-max-links)
  link: [2x when using 100 or 400 Gbps connections](../facts/direct-connect.md#direct-connect-faq-lag-max-links)
  say: four links for 1 or 10 gigabit ports | two links for 100 or 400 gigabit ports
direct-connect-faq-lag-minimum-links-default-zero
  claim: If you do not select minimum links when you order a LAG bundle, it defaults to zero.
  scope: per LAG; default; adjustable; minimum links not selected when ordering the bundle.
  link: [it will default to zero](../facts/direct-connect.md#direct-connect-faq-lag-minimum-links-default-zero)
  say: zero by default
direct-connect-faq-lag-minimum-links-meaning
  claim: Minimum links is a LACP setting for the minimum number of links that must be active for the LAG bundle to be active and pass traffic; for example, with four ports and minimum links set to three, a bundle with only two active ports is not active.
  scope: per LAG.
  link: [minimum number of links that must be active](../facts/direct-connect.md#direct-connect-faq-lag-minimum-links-meaning)
direct-connect-faq-lag-same-port-type
  claim: You cannot mix interface types in one LAG: the FAQ answers no and says a LAG is created using the same type of ports.
  scope: per LAG.
  link: [using the same type of ports](../facts/direct-connect.md#direct-connect-faq-lag-same-port-type)
direct-connect-faq-local-pref-failover-with-communities
  claim: You can build failover with local preference communities by advertising prefixes over the primary or active virtual interface with a community for higher local preference than the prefixes advertised over the backup or passive virtual interface.
  scope: per private virtual interface.
  link: [advertising prefixes over the primary/active virtual interface](../facts/direct-connect.md#direct-connect-faq-local-pref-failover-with-communities)
  say: give the primary VIF a higher local preference community than the backup
direct-connect-faq-local-zone-no-vpn-backup
  claim: Unlike connectivity to a Region, you cannot use a Site-to-Site VPN as a backup to a Direct Connect connection to an AWS Local Zone; for redundancy you must use two or more Direct Connect connections.
  scope: Direct Connect connections to an AWS Local Zone.
  link: [you cannot use an AWS Site-to-Site VPN](../facts/direct-connect.md#direct-connect-faq-local-zone-no-vpn-backup)
  link: [two or more AWS Direct Connect connections](../facts/direct-connect.md#direct-connect-faq-local-zone-no-vpn-backup)
direct-connect-faq-macsec-needs-capable-device
  claim: To use MACsec you need a MACsec-capable device on your end of the Ethernet connection to an AWS Direct Connect location.
  scope: MACsec on a Direct Connect connection.
  link: [You will need a MACsec-capable device](../facts/direct-connect.md#direct-connect-faq-macsec-needs-capable-device)
  say: you need a MACsec-capable device on your side
direct-connect-faq-macsec-what-it-encrypts
  claim: MACsec (802.1AE) is an IEEE standard that provides data confidentiality, data integrity, and data origin authenticity; on MACsec-capable connections it encrypts data from your on-premises network or collocated device to the Direct Connect point of presence.
  scope: from the on-premises network or collocated device to the Direct Connect point of presence; connections that support MACsec.
  link: [your chosen AWS Direct Connect point of presence](../facts/direct-connect.md#direct-connect-faq-macsec-what-it-encrypts)
direct-connect-faq-maintenance-notice-14-7-1-days
  claim: For scheduled Direct Connect maintenance AWS sends 3 notifications, at 14 calendar days, 7 calendar days and 1 calendar day; emergency maintenance may happen at any time with up to 60-minute notification.
  scope: per scheduled maintenance event; emergency maintenance may be performed at any time with up to 60-minute notification depending on the maintenance.
  link: [14 calendar days, followed by 7 calendar days and followed by 1 calendar day](../facts/direct-connect.md#direct-connect-faq-maintenance-notice-14-7-1-days)
direct-connect-faq-multi-account-dxgw-limits
  claim: Multi-account support lets you associate up to 20 VPCs or up to six AWS Transit Gateways from multiple AWS accounts with an AWS Direct Connect gateway.
  scope: per Direct Connect gateway; maximum; not adjustable; associations come from multiple AWS accounts.
  link: [up to 20 Amazon Virtual Private Clouds](../facts/direct-connect.md#direct-connect-faq-multi-account-dxgw-limits)
  link: [up to six AWS Transit Gateways](../facts/direct-connect.md#direct-connect-faq-multi-account-dxgw-limits)
direct-connect-faq-multiple-vifs-per-connection
  claim: Each Direct Connect connection can be configured with one or more virtual interfaces, so one connection can reach AWS services over public IP space and VPC resources over private IP space at the same time.
  scope: per Direct Connect connection.
  link: [one or more virtual interfaces](../facts/direct-connect.md#direct-connect-faq-multiple-vifs-per-connection)
  say: one connection can carry several virtual interfaces
direct-connect-faq-no-data-limit-up-to-port-capacity
  claim: There is no limit on the amount of data you can transfer using Direct Connect other than the capacity of your selected port.
  scope: per port; maximum; not adjustable; up to the limit of the selected port capacity.
  link: [the limit of your selected port capacity](../facts/direct-connect.md#direct-connect-faq-no-data-limit-up-to-port-capacity)
direct-connect-faq-no-layer-2
  claim: Layer 2 connections between a VPC and your network are not supported.
  scope: Direct Connect connections.
  link: [Layer 2 connections are not supported](../facts/direct-connect.md#direct-connect-faq-no-layer-2)
  say: no Layer 2 connections
direct-connect-faq-offers-sla
  claim: AWS Direct Connect offers a Service Level Agreement (SLA).
  scope: AWS Direct Connect.
  link: [AWS Direct Connect offers an SLA](../facts/direct-connect.md#direct-connect-faq-offers-sla)
  say: Direct Connect has an SLA
direct-connect-faq-private-vif-not-to-tgw
  claim: You cannot attach a private virtual interface to an AWS Transit Gateway.
  scope: private virtual interface.
  link: [you cannot attach private virtual interface](../facts/direct-connect.md#direct-connect-faq-private-vif-not-to-tgw)
direct-connect-faq-private-vif-one-dxgw-or-one-vgw
  claim: One private virtual interface can only attach to one AWS Direct Connect gateway or one virtual private gateway.
  scope: per private virtual interface.
  link: [only attach to one AWS Direct Connect gateway](../facts/direct-connect.md#direct-connect-faq-private-vif-one-dxgw-or-one-vgw)
direct-connect-faq-regional-transfer-not-dx-rate
  claim: Data transfer between Availability Zones in a Region is billed at the regular Regional data transfer rate, not at the Direct Connect rate.
  scope: data transfer between Availability Zones in a Region; data transfer between Availability Zones in a Region.
  link: [billed at the regular Regional data transfer rate](../facts/direct-connect.md#direct-connect-faq-regional-transfer-not-dx-rate)
  say: Regional transfer keeps the regular Regional rate
direct-connect-faq-requires-bgp
  claim: AWS Direct Connect requires Border Gateway Protocol (BGP) for a virtual interface to a VPC.
  scope: per virtual interface to a VPC.
  link: [requires Border Gateway Protocol (BGP)](../facts/direct-connect.md#direct-connect-faq-requires-bgp)
  say: Direct Connect needs BGP
direct-connect-faq-resiliency-toolkit-wizard
  claim: The AWS Direct Connect Resiliency Toolkit provides a connection wizard that helps you choose between multiple resiliency models.
  scope: Direct Connect Resiliency Toolkit.
  link: [a connection wizard](../facts/direct-connect.md#direct-connect-faq-resiliency-toolkit-wizard)
  say: a wizard that helps you pick a resiliency model and order the connections
direct-connect-faq-same-account-rules-vifs-dxgw
  claim: Private virtual interfaces and Direct Connect gateways must be in the same AWS account, and so must transit virtual interfaces and Direct Connect gateways; virtual private gateways and transit gateways can be in different accounts than the Direct Connect gateway owner.
  scope: per Direct Connect gateway; private VIF and transit VIF with the Direct Connect gateway: same account; virtual private gateway and transit gateway: can be in different accounts.
  link: [must be in the same AWS account](../facts/direct-connect.md#direct-connect-faq-same-account-rules-vifs-dxgw)
  say: VIFs and their Direct Connect gateway share an account; gateways can be in other accounts
direct-connect-faq-second-connection-redundant-equipment
  claim: AWS recommends a second connection for redundancy; when you request multiple ports at the same Direct Connect location, they are provisioned on redundant AWS equipment.
  scope: per Direct Connect location; multiple ports requested at the same location.
  link: [provisioned on redundant AWS equipment](../facts/direct-connect.md#direct-connect-faq-second-connection-redundant-equipment)
  say: multiple ports at one location land on redundant equipment
direct-connect-faq-sitelink-bypasses-regions
  claim: When AWS Direct Connect SiteLink is enabled at two or more Direct Connect locations, you can send data between those locations bypassing AWS Regions; SiteLink works with both hosted and dedicated connections.
  scope: Direct Connect SiteLink; enabled at two or more Direct Connect locations.
  link: [bypassing AWS Regions](../facts/direct-connect.md#direct-connect-faq-sitelink-bypasses-regions)
  say: SiteLink sends data between locations without going through a Region
direct-connect-faq-sitelink-requires-bgp
  claim: AWS Direct Connect SiteLink requires BGP.
  scope: Direct Connect SiteLink.
  link: [SiteLink requires BGP](../facts/direct-connect.md#direct-connect-faq-sitelink-requires-bgp)
  say: SiteLink needs BGP
direct-connect-faq-transit-vif-not-to-vgw
  claim: You cannot attach a transit virtual interface to a virtual private gateway.
  scope: transit virtual interface.
  link: [you cannot attach transit virtual interface](../facts/direct-connect.md#direct-connect-faq-transit-vif-not-to-vgw)
direct-connect-faq-two-charges-port-hours-data-transfer
  claim: The Direct Connect FAQ says AWS Direct Connect has two separate charges, port hours and data transfer; pricing is per port-hour consumed for each port type, partial port hours are billed as full hours, and the account that owns the port is charged the port-hour charges. Since September 15, 2026 Direct Connect also supports flat-rate billing, a fixed-price billing mode for dedicated connections that you set per connection.
  scope: per port type.
  link: [two separate charges: port hours and data transfer](../facts/direct-connect.md#direct-connect-faq-two-charges-port-hours-data-transfer)
  link: [billed as full hours](../facts/direct-connect.md#direct-connect-faq-two-charges-port-hours-data-transfer)
  say: port hours and data transfer
direct-connect-faq-vgw-in-one-dxgw-only
  claim: A VGW-VPC pair cannot be part of more than one AWS Direct Connect gateway.
  scope: per VGW-VPC pair.
  link: [more than one AWS Direct Connect gateway](../facts/direct-connect.md#direct-connect-faq-vgw-in-one-dxgw-only)
direct-connect-faq-vif-public-vs-private
  claim: A virtual interface (VIF) is necessary to access AWS services and is either public or private: a public virtual interface enables access to public services such as Amazon S3, and a private virtual interface enables access to your VPC.
  scope: Direct Connect virtual interfaces.
  link: [enables access to public services](../facts/direct-connect.md#direct-connect-faq-vif-public-vs-private)
  link: [enables access to your VPC](../facts/direct-connect.md#direct-connect-faq-vif-public-vs-private)
direct-connect-faq-vlan-only-separates-vifs
  claim: You cannot extend one of your VLANs to the AWS Cloud with Direct Connect: VLANs are used only to separate traffic between virtual interfaces.
  scope: VLANs on Direct Connect.
  link: [only to separate traffic between virtual interfaces](../facts/direct-connect.md#direct-connect-faq-vlan-only-separates-vifs)
direct-connect-faq-vpn-ipsec-over-internet-quick-low-bandwidth
  claim: VPN connections use IPsec to give encrypted connectivity between your intranet and an Amazon VPC over the public internet; they can be configured in minutes and suit an immediate need, low to modest bandwidth, and tolerance of the variability of internet-based connectivity.
  scope: Site-to-Site VPN compared with Direct Connect; immediate need, low to modest bandwidth, tolerance of internet variability.
  link: [can be configured in minutes](../facts/direct-connect.md#direct-connect-faq-vpn-ipsec-over-internet-quick-low-bandwidth)
  link: [low to modest bandwidth requirements](../facts/direct-connect.md#direct-connect-faq-vpn-ipsec-over-internet-quick-low-bandwidth)
  link: [over the public internet](../facts/direct-connect.md#direct-connect-faq-vpn-ipsec-over-internet-quick-low-bandwidth)
  say: a VPN is fast to set up and fits low to modest bandwidth
direct-connect-fis-resilience-testing-bgp-failover
  claim: Direct Connect supports resilience testing with AWS Fault Injection Service, which lets you test how applications respond when the BGP sessions over your virtual interfaces are disrupted.
  scope: AWS Fault Injection Service action for Direct Connect.
  link: [resilience testing with AWS Fault Injection Service](../facts/direct-connect.md#direct-connect-fis-resilience-testing-bgp-failover)
  link: [sessions over your Virtual Interfaces are disrupted](../facts/direct-connect.md#direct-connect-fis-resilience-testing-bgp-failover)
direct-connect-hosted-connection-not-orderable-in-console-must-accept
  claim: You cannot request a hosted connection through the Direct Connect console. A partner creates and configures it, and you must accept it before you can use it.
  scope: hosted connections.
  link: [You can't request a hosted connection](../facts/direct-connect.md#direct-connect-hosted-connection-not-orderable-in-console-must-accept)
  link: [You must accept the hosted connection](../facts/direct-connect.md#direct-connect-hosted-connection-not-orderable-in-console-must-accept)
direct-connect-hosted-connection-provisioned-by-partner
  claim: A hosted connection is a physical Ethernet connection that an AWS Direct Connect Partner provisions on behalf of a customer. You request it by contacting a partner in the Direct Connect Partner Program.
  scope: Direct Connect hosted connection.
  link: [provisions on behalf of a customer](../facts/direct-connect.md#direct-connect-hosted-connection-provisioned-by-partner)
  link: [request a hosted connection by contacting a partner](../facts/direct-connect.md#direct-connect-hosted-connection-provisioned-by-partner)
direct-connect-hosted-connection-speed-changed-only-by-partner
  claim: Connection port speeds of a hosted connection can only be changed by your AWS Direct Connect Partner.
  scope: hosted connections.
  link: [changed by your AWS Direct Connect Partner](../facts/direct-connect.md#direct-connect-hosted-connection-speed-changed-only-by-partner)
  link: [AWS Direct Connect Partner](../facts/direct-connect.md#direct-connect-hosted-connection-speed-changed-only-by-partner)
direct-connect-hosted-connection-supports-one-vif
  claim: Hosted connections support only one virtual interface.
  scope: per hosted connection; maximum.
  link: [Hosted connections support only one virtual interface](../facts/direct-connect.md#direct-connect-hosted-connection-supports-one-vif)
  link: [Hosted connections](../facts/direct-connect.md#direct-connect-hosted-connection-supports-one-vif)
direct-connect-hosted-port-hours-billed-while-provisioned
  claim: Port hours of a hosted connection are billed once you accept it and continue as long as it is provisioned for your use. To stop the charges, work with your partner to cancel the hosted connection.
  scope: hosted connections.
  link: [billed once you have accepted the Hosted Connection](../facts/direct-connect.md#direct-connect-hosted-port-hours-billed-while-provisioned)
  link: [as long as the Hosted Connection is provisioned](../facts/direct-connect.md#direct-connect-hosted-port-hours-billed-while-provisioned)
direct-connect-hosted-vif-another-account-must-accept
  claim: A hosted virtual interface lets another account use your Direct Connect connection; the owner of the other account must accept it before using it. It works the same as a standard virtual interface and can connect to public resources or a VPC.
  scope: Direct Connect hosted virtual interface.
  link: [create a hosted virtual interface for that account](../facts/direct-connect.md#direct-connect-hosted-vif-another-account-must-accept)
  link: [must accept the hosted virtual interface](../facts/direct-connect.md#direct-connect-hosted-vif-another-account-must-accept)
direct-connect-lag-active-active-mode
  claim: All connections in a LAG operate in Active/Active mode.
  scope: Direct Connect LAG.
  link: [operate in Active/Active mode](../facts/direct-connect.md#direct-connect-lag-active-active-mode)
  link: [Active/Active](../facts/direct-connect.md#direct-connect-lag-active-active-mode)
direct-connect-lag-definition-lacp-single-managed-connection
  claim: A link aggregation group (LAG) is a logical interface that uses LACP to aggregate multiple connections at a single Direct Connect endpoint, so you treat them as one managed connection.
  scope: Direct Connect LAG.
  link: [uses the Link Aggregation Control Protocol (LACP)](../facts/direct-connect.md#direct-connect-lag-definition-lacp-single-managed-connection)
  link: [treat them as a single, managed connection](../facts/direct-connect.md#direct-connect-lag-definition-lacp-single-managed-connection)
direct-connect-lag-max-members-two-100-400-or-four-below-100
  claim: A LAG can have a maximum of two 100 Gbps or 400 Gbps connections, or four connections with a port speed below 100 Gbps.
  scope: per LAG; maximum; not adjustable.
  link: [a maximum of two 100 Gbps or 400 Gbps connections](../facts/direct-connect.md#direct-connect-lag-max-members-two-100-400-or-four-below-100)
  link: [four connections with a port speed less than 100 Gbps](../facts/direct-connect.md#direct-connect-lag-max-members-two-100-400-or-four-below-100)
direct-connect-lag-minimum-links-default-zero
  claim: A LAG has an attribute for the minimum number of connections that must be operational. By default new LAGs set it to 0. If you set a higher value, the whole LAG becomes non-operational when fewer connections than that are operational.
  scope: Direct Connect LAG minimum links; default; adjustable; you can update the value.
  link: [set to 0](../facts/direct-connect.md#direct-connect-lag-minimum-links-default-zero)
  link: [your entire LAG becomes non-operational](../facts/direct-connect.md#direct-connect-lag-minimum-links-default-zero)
direct-connect-lag-no-extra-charge-dynamic-lacp-only
  claim: There is no extra charge for using a LAG. Dynamic LACP bundles are used and static LACP bundles are not supported.
  scope: Direct Connect LAG.
  link: [no extra charge for using a LAG](../facts/direct-connect.md#direct-connect-lag-no-extra-charge-dynamic-lacp-only)
  link: [static LACP bundles are not supported](../facts/direct-connect.md#direct-connect-lag-no-extra-charge-dynamic-lacp-only)
direct-connect-lag-no-multi-chassis
  claim: Multi-chassis LAG (MLAG) is not supported by AWS; a LAG only includes ports on the same Direct Connect device.
  scope: Direct Connect LAG.
  link: [Multi-chassis LAG (MLAG) is not supported by AWS](../facts/direct-connect.md#direct-connect-lag-no-multi-chassis)
  link: [ports on the same AWS Direct Connect devices](../facts/direct-connect.md#direct-connect-lag-no-multi-chassis)
direct-connect-lag-not-more-resilient-against-device-failure
  claim: A LAG does not make connectivity to AWS more resilient. With more than one link and minimum links set to one, it protects against a single link failure, but not against a single device failure or device maintenance at AWS where the LAG terminates.
  scope: Direct Connect LAG.
  link: [doesn't make your connectivity to AWS more resilient](../facts/direct-connect.md#direct-connect-lag-not-more-resilient-against-device-failure)
  link: [will not protect against a single device failure](../facts/direct-connect.md#direct-connect-lag-not-more-resilient-against-device-failure)
direct-connect-lag-rule-dedicated-connections-only
  claim: All connections in a LAG must be dedicated connections with a port speed of 1 Gbps, 10 Gbps, 100 Gbps, or 400 Gbps. Hosted connections cannot be in a LAG.
  scope: Direct Connect LAG.
  link: [All connections must be dedicated connections](../facts/direct-connect.md#direct-connect-lag-rule-dedicated-connections-only)
  link: [Only Dedicated Connections support LAGs](../facts/direct-connect.md#direct-connect-lag-rule-dedicated-connections-only)
direct-connect-lag-rule-same-bandwidth-same-endpoint
  claim: All connections in a LAG must use the same bandwidth and must terminate at the same Direct Connect endpoint.
  scope: Direct Connect LAG.
  link: [must use the same bandwidth](../facts/direct-connect.md#direct-connect-lag-rule-same-bandwidth-same-endpoint)
  link: [must terminate at the same Direct Connect endpoint](../facts/direct-connect.md#direct-connect-lag-rule-same-bandwidth-same-endpoint)
direct-connect-limit-dedicated-port-speeds
  claim: A Direct Connect dedicated connection has a port speed of 1 Gbps, 10 Gbps, 100 Gbps, or 400 Gbps.
  scope: per dedicated connection; fixed; not adjustable.
  link: [1 Gbps, 10 Gbps, 100 Gbps, and 400 Gbps](../facts/direct-connect.md#direct-connect-limit-dedicated-port-speeds)
  link: [400 Gbps](../facts/direct-connect.md#direct-connect-limit-dedicated-port-speeds)
  say: one, ten, one hundred and four hundred gigabits per second | four hundred gigabits per second
direct-connect-limit-ecmp-multipath-16-next-hops
  claim: AWS multipaths traffic to your network per prefix at up to 16 next-hops wide, where each next-hop is a unique AWS endpoint.
  scope: per prefix; maximum; not adjustable.
  link: [up to 16 next-hops wide](../facts/direct-connect.md#direct-connect-limit-ecmp-multipath-16-next-hops)
  say: up to sixteen next-hops wide
direct-connect-limit-hosted-port-speeds
  claim: A Direct Connect hosted connection has a speed of 50 Mbps, 100 Mbps, 200 Mbps, 300 Mbps, 400 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, or 25 Gbps.
  scope: per hosted connection; fixed; not adjustable.
  link: [50 Mbps, 100 Mbps, 200 Mbps, 300 Mbps, 400 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, and 25 Gbps](../facts/direct-connect.md#direct-connect-limit-hosted-port-speeds)
  link: [50 Mbps](../facts/direct-connect.md#direct-connect-limit-hosted-port-speeds)
  link: [25 Gbps](../facts/direct-connect.md#direct-connect-limit-hosted-port-speeds)
  say: fifty megabits per second up to twenty-five gigabits per second | fifty megabits per second | twenty-five gigabits per second
direct-connect-limit-loa-cfa-expires-90-days
  claim: If the cross connect is not completed within 90 days, the authority granted by the LOA-CFA expires, and you can download it again from the Direct Connect console.
  scope: per LOA-CFA; maximum; not adjustable.
  link: [within 90 days](../facts/direct-connect.md#direct-connect-limit-loa-cfa-expires-90-days)
  say: within ninety days
direct-connect-limit-maintenance-notice-14-days
  claim: Planned Direct Connect maintenance events are scheduled 14 days in advance and typically occur during a four-hour window in low-traffic hours at the Direct Connect location.
  scope: per maintenance event; fixed; not adjustable.
  link: [14 days in advance](../facts/direct-connect.md#direct-connect-limit-maintenance-notice-14-days)
  link: [four-hour window](../facts/direct-connect.md#direct-connect-limit-maintenance-notice-14-days)
  say: fourteen days in advance | four-hour window
direct-connect-limit-mtu-private-vif
  claim: The MTU of a Direct Connect private virtual interface can be either 1500 or 9001 (jumbo frames).
  scope: per private virtual interface; maximum; adjustable.
  link: [1500](../facts/direct-connect.md#direct-connect-limit-mtu-private-vif)
  link: [9001](../facts/direct-connect.md#direct-connect-limit-mtu-private-vif)
  say: fifteen hundred | nine thousand one
direct-connect-limit-mtu-transit-vif
  claim: The MTU of a Direct Connect transit virtual interface can be either 1500 or 8500 (jumbo frames).
  scope: per transit virtual interface; maximum; adjustable.
  link: [1500](../facts/direct-connect.md#direct-connect-limit-mtu-transit-vif)
  link: [8500](../facts/direct-connect.md#direct-connect-limit-mtu-transit-vif)
  say: fifteen hundred | eighty-five hundred
direct-connect-limit-prefix-controls-default-allocation
  claim: With inbound prefix controls, the default allocation per virtual interface is 100 per address family (IPv4 and IPv6). Public VIFs are not managed by inbound prefix controls.
  scope: per VIF; default; adjustable; public VIFs are not managed by inbound prefix controls.
  link: [100 per address family](../facts/direct-connect.md#direct-connect-limit-prefix-controls-default-allocation)
  say: one hundred per address family
direct-connect-limit-prefix-controls-dxgw-total
  claim: With inbound prefix controls, total allocations per Direct Connect gateway are 10,000, counting IPv4 and IPv6 together. Public VIFs are not managed by inbound prefix controls.
  scope: per Direct Connect gateway; maximum; adjustable; public VIFs are not managed by inbound prefix controls.
  link: [10,000](../facts/direct-connect.md#direct-connect-limit-prefix-controls-dxgw-total)
  say: ten thousand
direct-connect-limit-prefix-controls-max-allocation
  claim: With inbound prefix controls, the maximum allocation per virtual interface is 1,000 per address family (IPv4 and IPv6). Public VIFs are not managed by inbound prefix controls.
  scope: per VIF; maximum; adjustable; public VIFs are not managed by inbound prefix controls.
  link: [1,000 per address family](../facts/direct-connect.md#direct-connect-limit-prefix-controls-max-allocation)
  say: one thousand per address family
direct-connect-limit-prefix-controls-pool-per-connection
  claim: With inbound prefix controls, the prefix pool per dedicated connection is 5,000 for 1 and 10 Gbps, 30,000 for 100 Gbps and 50,000 for 400 Gbps. Public VIFs are not managed by inbound prefix controls.
  scope: per dedicated connection; maximum; adjustable; public VIFs are not managed by inbound prefix controls.
  link: [5,000 (1/10 Gbps), 30,000 (100 Gbps), 50,000 (400 Gbps)](../facts/direct-connect.md#direct-connect-limit-prefix-controls-pool-per-connection)
  say: five thousand, thirty thousand and fifty thousand
direct-connect-limit-prefix-controls-public-vif-1000
  claim: Public virtual interfaces are not managed by inbound prefix controls and keep the existing limit of 1,000 inbound prefixes.
  scope: per public virtual interface; maximum; not adjustable.
  link: [1,000 inbound prefixes](../facts/direct-connect.md#direct-connect-limit-prefix-controls-public-vif-1000)
  say: one thousand inbound prefixes
direct-connect-limit-private-asn-ranges
  claim: For the AWS side of a Direct Connect gateway you can choose any private ASN: 64512 to 65534 for 16-bit ASNs, or 4200000000 to 4294967294 for 32-bit ASNs.
  scope: per Direct Connect gateway; maximum; not adjustable.
  link: [64512 to 65534](../facts/direct-connect.md#direct-connect-limit-private-asn-ranges)
  link: [4200000000 and 4294967294](../facts/direct-connect.md#direct-connect-limit-private-asn-ranges)
  say: six four five one two to six five five three four
direct-connect-limit-rate-limiter-range-1g
  claim: On a 1 Gbps dedicated connection you can set VIF rate limiters between 50 Mbps and 1 Gbps.
  scope: per VIF rate limiter; maximum; not adjustable.
  link: [50 Mbps](../facts/direct-connect.md#direct-connect-limit-rate-limiter-range-1g)
  link: [1 Gbps](../facts/direct-connect.md#direct-connect-limit-rate-limiter-range-1g)
  say: fifty megabits per second | one gigabit per second
direct-connect-limit-tgw-jumbo-frames-8500
  claim: Jumbo frames on Transit Gateways support only 8500 bytes.
  scope: per transit gateway; maximum; not adjustable.
  link: [8500 bytes](../facts/direct-connect.md#direct-connect-limit-tgw-jumbo-frames-8500)
  say: eighty-five hundred bytes
direct-connect-loa-cfa-authorization-needed-for-cross-connect
  claim: The LOA-CFA is the authorization to connect to AWS. Your network provider needs it to order a cross connect for you, and you cannot order a cross connect yourself without equipment in the Direct Connect location.
  scope: dedicated connections.
  link: [LOA-CFA is the authorization to connect to AWS](../facts/direct-connect.md#direct-connect-loa-cfa-authorization-needed-for-cross-connect)
  link: [your network provider to order a cross connect](../facts/direct-connect.md#direct-connect-loa-cfa-authorization-needed-for-cross-connect)
direct-connect-local-pref-communities-private-and-transit-only
  claim: Local preference BGP communities are available for private and transit virtual interfaces only, not for public virtual interfaces.
  scope: local preference BGP communities.
  link: [available for private and transit virtual interfaces only](../facts/direct-connect.md#direct-connect-local-pref-communities-private-and-transit-only)
  link: [No, this feature is currently available](../facts/direct-connect.md#direct-connect-local-pref-communities-private-and-transit-only)
direct-connect-local-pref-evaluated-before-as-path
  claim: Local preference BGP community tags are evaluated before any AS_PATH attribute, in order from lowest to highest preference, where the highest preference is preferred.
  scope: private and transit virtual interfaces.
  link: [evaluated before any AS_PATH attribute](../facts/direct-connect.md#direct-connect-local-pref-evaluated-before-as-path)
  link: [where highest preference is preferred](../facts/direct-connect.md#direct-connect-local-pref-evaluated-before-as-path)
direct-connect-local-pref-recommended-for-active-passive-same-prefix-length
  claim: Local preference is the BGP attribute AWS recommends for active/passive connections when the advertised prefix lengths are the same.
  scope: private and transit virtual interfaces.
  link: [Local preference is the BGP attribute recommended](../facts/direct-connect.md#direct-connect-local-pref-recommended-for-active-passive-same-prefix-length)
  link: [the prefix lengths advertised are the same](../facts/direct-connect.md#direct-connect-local-pref-recommended-for-active-passive-same-prefix-length)
direct-connect-location-gives-access-to-associated-region-and-all-public-regions
  claim: A Direct Connect location provides access to AWS in the Region with which it is associated, and you can use a single connection in a public Region or AWS GovCloud (US) to access public AWS services in all other public Regions.
  scope: Direct Connect locations.
  link: [the Region with which it is associated](../facts/direct-connect.md#direct-connect-location-gives-access-to-associated-region-and-all-public-regions)
  link: [public AWS services in all other public Regions](../facts/direct-connect.md#direct-connect-location-gives-access-to-associated-region-and-all-public-regions)
direct-connect-macsec-cipher-suites
  claim: For 100 Gbps and 400 Gbps connections AWS supports the GCM-AES-XPN-256 cipher suite. For 10Gbps connections it supports GCM-AES-256 and GCM-AES-XPN-256.
  scope: MACsec on Direct Connect by port speed.
  link: [the GCM-AES-XPN-256 cipher suite](../facts/direct-connect.md#direct-connect-macsec-cipher-suites)
  link: [GCM-AES-256](../facts/direct-connect.md#direct-connect-macsec-cipher-suites)
direct-connect-macsec-encrypts-to-direct-connect-location
  claim: MACsec is an IEEE standard that provides data confidentiality, integrity and origin authenticity. With a MACsec-capable Direct Connect connection you encrypt data from your corporate data center to the Direct Connect location.
  scope: MACsec-capable Direct Connect connections.
  link: [corporate data center to the Direct Connect location](../facts/direct-connect.md#direct-connect-macsec-encrypts-to-direct-connect-location)
  link: [MAC Security (MACsec) is an IEEE standard](../facts/direct-connect.md#direct-connect-macsec-encrypts-to-direct-connect-location)
direct-connect-macsec-layer2-over-cross-connect
  claim: MACsec provides Layer 2 point-to-point encryption over the cross-connect to AWS, operating between two Layer 3 routers.
  scope: MACsec on Direct Connect.
  link: [Layer 2 point-to-point encryption over the cross-connect to AWS](../facts/direct-connect.md#direct-connect-macsec-layer2-over-cross-connect)
  link: [operating between two Layer 3 routers](../facts/direct-connect.md#direct-connect-macsec-layer2-over-cross-connect)
direct-connect-macsec-layer2-point-to-point-not-end-to-end
  claim: MACsec provides point-to-point security on Ethernet links, so it does not provide end-to-end encryption across multiple sequential Ethernet or other network segments.
  scope: MACsec on Direct Connect.
  link: [does not provide end-to-end encryption](../facts/direct-connect.md#direct-connect-macsec-layer2-point-to-point-not-end-to-end)
  link: [MACsec provides point-to-point security on Ethernet links](../facts/direct-connect.md#direct-connect-macsec-layer2-point-to-point-not-end-to-end)
direct-connect-macsec-new-connections-default-should-encrypt
  claim: New MACsec-enabled connections are set to should_encrypt mode by default, which falls back to unencrypted traffic if MACsec negotiation fails. The must_encrypt mode sends no traffic if encryption cannot be established.
  scope: MACsec-enabled Direct Connect connections; default; adjustable; the encryption mode can be modified later.
  link: [new MACsec-enabled connections are set to "should_encrypt" mode](../facts/direct-connect.md#direct-connect-macsec-new-connections-default-should-encrypt)
  link: [fall back to unencrypted communication](../facts/direct-connect.md#direct-connect-macsec-new-connections-default-should-encrypt)
direct-connect-macsec-no-extra-charge
  claim: There is no additional charge for MACsec on Direct Connect.
  scope: MACsec on Direct Connect.
  link: [there is no additional charge for MACsec](../facts/direct-connect.md#direct-connect-macsec-no-extra-charge)
direct-connect-macsec-not-a-replacement-for-other-encryption
  claim: MACsec is not intended as a replacement for any specific encryption technology. For defense in depth, continue to use the encryption you already use; MACsec is an additional option.
  scope: MACsec on Direct Connect.
  link: [MACsec is not intended as a replacement](../facts/direct-connect.md#direct-connect-macsec-not-a-replacement-for-other-encryption)
  link: [continue to use any encryption technologies](../facts/direct-connect.md#direct-connect-macsec-not-a-replacement-for-other-encryption)
direct-connect-macsec-not-on-1gbps-or-hosted
  claim: MACsec is not supported on 1 Gbps dedicated connections or on any hosted connections.
  scope: Direct Connect connections.
  link: [not supported on 1 Gbps dedicated connections](../facts/direct-connect.md#direct-connect-macsec-not-on-1gbps-or-hosted)
  link: [any hosted connections](../facts/direct-connect.md#direct-connect-macsec-not-on-1gbps-or-hosted)
direct-connect-macsec-supported-dedicated-10-100-400-gbps
  claim: MACsec is supported on 10 Gbps, 100 Gbps, and 400 Gbps dedicated Direct Connect connections at selected points of presence.
  scope: dedicated connections at selected points of presence.
  link: [10 Gbps, 100 Gbps, and 400 Gbps dedicated AWS Direct Connect connections](../facts/direct-connect.md#direct-connect-macsec-supported-dedicated-10-100-400-gbps)
  link: [at selected points of presence](../facts/direct-connect.md#direct-connect-macsec-supported-dedicated-10-100-400-gbps)
direct-connect-maintenance-notify-aws-health-email
  claim: Direct Connect emails notifications about planned and emergency maintenance events to the email address of the AWS account that owns the connection or virtual interface. For planned maintenance, you can also receive notifications in your monitoring or ticketing system by integrating with AWS Health.
  scope: Direct Connect maintenance notifications.
  link: [sends email notifications about planned and emergency maintenance](../facts/direct-connect.md#direct-connect-maintenance-notify-aws-health-email)
  link: [integrating with AWS Health](../facts/direct-connect.md#direct-connect-maintenance-notify-aws-health-email)
direct-connect-maintenance-prepare-redundant-connection-or-vpn-backup
  claim: To prepare for Direct Connect maintenance, request a redundant Direct Connect connection or configure a Site-to-Site VPN as a backup. The best practice is to shift traffic to another circuit during maintenance.
  scope: Direct Connect maintenance.
  link: [Request a redundant Direct Connect connection](../facts/direct-connect.md#direct-connect-maintenance-prepare-redundant-connection-or-vpn-backup)
  link: [Configure a AWS Site-to-Site VPN](../facts/direct-connect.md#direct-connect-maintenance-prepare-redundant-connection-or-vpn-backup)
  link: [shift your traffic to another circuit](../facts/direct-connect.md#direct-connect-maintenance-prepare-redundant-connection-or-vpn-backup)
direct-connect-maintenance-redundant-setup-scheduled-at-different-times
  claim: If you follow the high availability and resilience recommendations, AWS maintenance scheduling detects your redundant setup and schedules maintenance at different times for each connection. If all your connections are on the same AWS logical device, you are impacted by the maintenance.
  scope: multiple connections to one Direct Connect location.
  link: [schedule maintenance at different times for each connection](../facts/direct-connect.md#direct-connect-maintenance-redundant-setup-scheduled-at-different-times)
  link: [you will be impacted by the maintenance](../facts/direct-connect.md#direct-connect-maintenance-redundant-setup-scheduled-at-different-times)
direct-connect-maintenance-types-planned-and-emergency
  claim: Direct Connect maintenance is of two types, planned and emergency. With a non-resilient setup or a single connection, you experience an interruption in connectivity between your on-premises network and AWS resources.
  scope: Direct Connect maintenance.
  link: [divided into two types - planned and emergency](../facts/direct-connect.md#direct-connect-maintenance-types-planned-and-emergency)
  link: [a non-resilient network setup or a single connection](../facts/direct-connect.md#direct-connect-maintenance-types-planned-and-emergency)
direct-connect-metric-connection-bps-egress
  claim: The ConnectionBpsEgress metric is the bitrate for outbound data from the AWS side of the connection, in bits per second.
  scope: Direct Connect CloudWatch connection metric.
  link: [ConnectionBpsEgress](../facts/direct-connect.md#direct-connect-metric-connection-bps-egress)
  link: [outbound data from the AWS side](../facts/direct-connect.md#direct-connect-metric-connection-bps-egress)
direct-connect-metric-connection-bps-ingress
  claim: The ConnectionBpsIngress metric is the bitrate for inbound data to the AWS side of the connection, in bits per second.
  scope: Direct Connect CloudWatch connection metric.
  link: [ConnectionBpsIngress](../facts/direct-connect.md#direct-connect-metric-connection-bps-ingress)
  link: [inbound data to the AWS side](../facts/direct-connect.md#direct-connect-metric-connection-bps-ingress)
direct-connect-metric-connection-state-up-down
  claim: The ConnectionState metric shows whether a connection is up or down. It is available for dedicated and hosted connections.
  scope: Direct Connect CloudWatch connection metric.
  link: [ConnectionState](../facts/direct-connect.md#direct-connect-metric-connection-state-up-down)
  link: [available for dedicated and hosted connections](../facts/direct-connect.md#direct-connect-metric-connection-state-up-down)
direct-connect-metric-vif-bgp-prefixes-accepted
  claim: The VirtualInterfaceBgpPrefixesAccepted metric counts the BGP prefixes accepted from the BGP peer on the virtual interface.
  scope: Direct Connect CloudWatch virtual interface metric.
  link: [VirtualInterfaceBgpPrefixesAccepted](../facts/direct-connect.md#direct-connect-metric-vif-bgp-prefixes-accepted)
  link: [BGP prefixes accepted from the BGP peer](../facts/direct-connect.md#direct-connect-metric-vif-bgp-prefixes-accepted)
direct-connect-metric-vif-bgp-prefixes-advertised
  claim: The VirtualInterfaceBgpPrefixesAdvertised metric counts the BGP prefixes advertised to the BGP peer on the virtual interface.
  scope: Direct Connect CloudWatch virtual interface metric.
  link: [VirtualInterfaceBgpPrefixesAdvertised](../facts/direct-connect.md#direct-connect-metric-vif-bgp-prefixes-advertised)
  link: [BGP prefixes advertised to the BGP peer](../facts/direct-connect.md#direct-connect-metric-vif-bgp-prefixes-advertised)
direct-connect-metric-vif-bgp-status-up-down
  claim: The VirtualInterfaceBgpStatus metric shows the state of the BGP peering session of a virtual interface, up or down.
  scope: Direct Connect CloudWatch virtual interface metric.
  link: [VirtualInterfaceBgpStatus](../facts/direct-connect.md#direct-connect-metric-vif-bgp-status-up-down)
  link: [The state of the BGP peering session](../facts/direct-connect.md#direct-connect-metric-vif-bgp-status-up-down)
direct-connect-no-setup-charge-no-minimum-term
  claim: Direct Connect has no setup charges, and you may cancel at any time. Services from AWS Direct Connect Partners may have other terms or restrictions.
  scope: AWS Direct Connect service charges; services provided by Direct Connect Partners may have other terms or restrictions.
  link: [There are no setup charges](../facts/direct-connect.md#direct-connect-no-setup-charge-no-minimum-term)
  link: [you may cancel at any time](../facts/direct-connect.md#direct-connect-no-setup-charge-no-minimum-term)
direct-connect-not-encrypted-by-default-use-service-encryption
  claim: Direct Connect does not encrypt traffic in transit by default. To encrypt data that crosses Direct Connect you must use the transit encryption options for that service.
  scope: traffic in transit over Direct Connect; default; adjustable.
  link: [does not encrypt your traffic](../facts/direct-connect.md#direct-connect-not-encrypted-by-default-use-service-encryption)
  link: [use the transit encryption options for that service](../facts/direct-connect.md#direct-connect-not-encrypted-by-default-use-service-encryption)
direct-connect-options-row-direct-connect-predictable-private-lines
  claim: The connectivity options table lists AWS Direct Connect as a dedicated network connection over private lines, with more predictable network performance and reduced bandwidth costs, and a limitation that it might need additional telecom and hosting provider relationships or new circuits.
  scope: Network-to-Amazon VPC connectivity options table.
  link: [Dedicated network connection over private lines](../facts/direct-connect.md#direct-connect-options-row-direct-connect-predictable-private-lines)
  link: [More predictable network performance](../facts/direct-connect.md#direct-connect-options-row-direct-connect-predictable-private-lines)
direct-connect-partners-extend-network-to-location
  claim: If your network is not present at a Direct Connect location, AWS Direct Connect Partners can help you extend your data center or office network to the location.
  scope: customers without equipment at a location.
  link: [can help you extend your preexisting data center](../facts/direct-connect.md#direct-connect-partners-extend-network-to-location)
  link: [to a AWS Direct Connect location](../facts/direct-connect.md#direct-connect-partners-extend-network-to-location)
direct-connect-plus-site-to-site-vpn-ipsec-encrypted-private-connection
  claim: Combining Direct Connect dedicated connections with the Amazon VPC VPN gives an IPsec-encrypted private connection that also reduces network costs, increases bandwidth throughput, and gives a more consistent network experience than internet-based VPN connections.
  scope: Direct Connect combined with Site-to-Site VPN.
  link: [an IPsec-encrypted private connection](../facts/direct-connect.md#direct-connect-plus-site-to-site-vpn-ipsec-encrypted-private-connection)
  link: [a more consistent network experience](../facts/direct-connect.md#direct-connect-plus-site-to-site-vpn-ipsec-encrypted-private-connection)
direct-connect-plus-vpn-public-vif-ipsec-more-consistent-than-internet-vpn
  claim: Direct Connect public virtual interfaces establish a dedicated network connection to public AWS resources such as a Site-to-Site VPN endpoint, and you can then create IPsec connections to the VPC virtual private gateways. This combines end-to-end IPsec security with the low latency and increased bandwidth of Direct Connect, for a more consistent network experience than internet-based VPN connections.
  scope: Direct Connect with Site-to-Site VPN.
  link: [end-to-end secure IPsec connection](../facts/direct-connect.md#direct-connect-plus-vpn-public-vif-ipsec-more-consistent-than-internet-vpn)
  link: [a more consistent network experience](../facts/direct-connect.md#direct-connect-plus-vpn-public-vif-ipsec-more-consistent-than-internet-vpn)
direct-connect-plus-vpn-tgw-ipsec-encrypted-over-dedicated-connection
  claim: Direct Connect with Transit Gateway and Site-to-Site VPN enables end-to-end IPsec-encrypted connections between your networks and a regional centralized router over a private dedicated connection.
  scope: Direct Connect with Transit Gateway and Site-to-Site VPN.
  link: [end-to-end IPsec-encrypted connections](../facts/direct-connect.md#direct-connect-plus-vpn-tgw-ipsec-encrypted-over-dedicated-connection)
  link: [over a private dedicated connection](../facts/direct-connect.md#direct-connect-plus-vpn-tgw-ipsec-encrypted-over-dedicated-connection)
direct-connect-port-hours-charged-even-when-no-data
  claim: Port hours measure the time a port is provisioned for your use. You are charged for port hours even when no data is passing through the port.
  scope: dedicated and hosted connection port hours.
  link: [no data is passing through the port](../facts/direct-connect.md#direct-connect-port-hours-charged-even-when-no-data)
  link: [the time that a port is provisioned](../facts/direct-connect.md#direct-connect-port-hours-charged-even-when-no-data)
direct-connect-pricing-data-transfer-in-free
  claim: Data transfer in over Direct Connect is $0.00 per gigabyte at all Direct Connect locations.
  scope: per gigabyte, per location.
  link: [$0.00 per gigabyte](../facts/direct-connect.md#direct-connect-pricing-data-transfer-in-free)
  say: zero dollars per gigabyte
direct-connect-pricing-dedicated-port-hours-while-provisioned
  claim: Dedicated connection port hours are billed as long as the port is provisioned for your use.
  scope: per dedicated connection.
  link: [billed as long as that port is provisioned](../facts/direct-connect.md#direct-connect-pricing-dedicated-port-hours-while-provisioned)
direct-connect-pricing-dto-account-private-vif
  claim: For a private virtual interface, the AWS account that owns the AWS resources responsible for the data transfer out is charged.
  scope: per private virtual interface.
  link: [the AWS account that owns the AWS resources](../facts/direct-connect.md#direct-connect-pricing-dto-account-private-vif)
direct-connect-pricing-dto-by-region-and-location
  claim: Direct Connect data transfer out (DTO) pricing depends on the source AWS Region or Local Zone and the Direct Connect location.
  scope: per gigabyte.
  link: [source AWS Region or Local Zone](../facts/direct-connect.md#direct-connect-pricing-dto-by-region-and-location)
direct-connect-pricing-factors-capacity-port-hours-data-transfer-out
  claim: Three factors determine Direct Connect pricing for connecting to resources in an AWS Region: capacity, port hours, and data transfer out through the Direct Connect location.
  scope: AWS Direct Connect.
  link: [capacity, port hours, and data transfer out](../facts/direct-connect.md#direct-connect-pricing-factors-capacity-port-hours-data-transfer-out)
  link: [three factors that determine pricing](../facts/direct-connect.md#direct-connect-pricing-factors-capacity-port-hours-data-transfer-out)
direct-connect-pricing-flat-rate-second-port-included
  claim: With flat-rate pricing the second connection of a port-pair is included at no additional charge.
  scope: per port-pair; fixed.
  link: [included at no additional charge](../facts/direct-connect.md#direct-connect-pricing-flat-rate-second-port-included)
direct-connect-private-connection-more-consistent-than-internet
  claim: Direct Connect delivers data through a private network connection between your facilities and AWS instead of the internet. In many circumstances, private connections can reduce costs, increase bandwidth, and give a more consistent network experience than internet-based connections.
  scope: AWS Direct Connect compared with internet-based connections.
  link: [a more consistent network experience](../facts/direct-connect.md#direct-connect-private-connection-more-consistent-than-internet)
  link: [private network connection between your facilities and AWS](../facts/direct-connect.md#direct-connect-private-connection-more-consistent-than-internet)
  link: [an alternative to using the internet](../facts/direct-connect.md#direct-connect-private-connection-more-consistent-than-internet)
direct-connect-private-vif-one-dxgw-or-one-vgw
  claim: You cannot associate a virtual private gateway with more than one Direct Connect gateway, and you cannot attach a private virtual interface to more than one Direct Connect gateway.
  scope: Direct Connect gateway associations.
  link: [a virtual private gateway with more than one](../facts/direct-connect.md#direct-connect-private-vif-one-dxgw-or-one-vgw)
  link: [a private virtual interface to more than one](../facts/direct-connect.md#direct-connect-private-vif-one-dxgw-or-one-vgw)
direct-connect-private-vif-single-vpc-or-dxgw-many-regions
  claim: A private virtual interface connects directly to a single VPC in the same Region. Connected to a Direct Connect gateway, it reaches multiple virtual private gateways across any account and AWS Region except the AWS China Regions.
  scope: private virtual interface.
  link: [a single VPC per private virtual interface](../facts/direct-connect.md#direct-connect-private-vif-single-vpc-or-dxgw-many-regions)
  link: [across any account and AWS Region](../facts/direct-connect.md#direct-connect-private-vif-single-vpc-or-dxgw-many-regions)
direct-connect-private-vif-with-dxgw-reaches-vpcs-any-region
  claim: A private virtual interface with a Direct Connect gateway reaches VPCs in any AWS Region. A transit virtual interface with a Direct Connect gateway reaches transit gateways in any AWS Region.
  scope: Direct Connect gateway.
  link: [— Reaches VPCs in any AWS Region](../facts/direct-connect.md#direct-connect-private-vif-with-dxgw-reaches-vpcs-any-region)
  link: [— Reaches transit gateways in any AWS Region](../facts/direct-connect.md#direct-connect-private-vif-with-dxgw-reaches-vpcs-any-region)
direct-connect-private-vif-without-dxgw-reaches-associated-region-only
  claim: A private virtual interface without a Direct Connect gateway reaches a VPC in the associated Region only, and the VPC must have a virtual private gateway in the same Region as the connection.
  scope: private virtual interface attached directly to a virtual private gateway.
  link: [Reaches a VPC in the associated Region only](../facts/direct-connect.md#direct-connect-private-vif-without-dxgw-reaches-associated-region-only)
  link: [a virtual private gateway in the same Region](../facts/direct-connect.md#direct-connect-private-vif-without-dxgw-reaches-associated-region-only)
direct-connect-public-prefixes-global-by-default-without-scope-community
  claim: If you do not apply any scope community tags to the public prefixes you advertise, the prefixes are advertised to all public AWS Regions (global) by default.
  scope: public virtual interface prefixes; default; adjustable.
  link: [all public AWS Regions (global) by default](../facts/direct-connect.md#direct-connect-public-prefixes-global-by-default-without-scope-community)
  link: [If you do not apply any community tags](../facts/direct-connect.md#direct-connect-public-prefixes-global-by-default-without-scope-community)
direct-connect-public-vif-access-all-public-regions-from-any-location
  claim: From any Direct Connect location in a public Region or AWS GovCloud (US), you can access all public AWS Regions (except those in China (Beijing and Ningxia)), AWS GovCloud (US) Regions, and AWS Local Zones.
  scope: Direct Connect locations.
  link: [you can access all public AWS Regions](../facts/direct-connect.md#direct-connect-public-vif-access-all-public-regions-from-any-location)
  link: [AWS Local Zones](../facts/direct-connect.md#direct-connect-public-vif-access-all-public-regions-from-any-location)
direct-connect-public-vif-prefixes-not-readvertised-outside-aws
  claim: AWS does not re-advertise customer prefixes received over Direct Connect public virtual interfaces to networks outside of AWS. Prefixes advertised on a public virtual interface are visible to all customers on AWS.
  scope: public virtual interface.
  link: [AWS does not re-advertise customer prefixes](../facts/direct-connect.md#direct-connect-public-vif-prefixes-not-readvertised-outside-aws)
  link: [visible to all customers on AWS](../facts/direct-connect.md#direct-connect-public-vif-prefixes-not-readvertised-outside-aws)
direct-connect-public-vif-reaches-amazon-prefixes-not-non-amazon
  claim: Over a public virtual interface you can access all AWS prefixes, such as public IPs used by EC2 instances, Amazon S3 and AWS API endpoints. You do not have access to non-Amazon prefixes.
  scope: public virtual interface.
  link: [access all AWS prefixes](../facts/direct-connect.md#direct-connect-public-vif-reaches-amazon-prefixes-not-non-amazon)
  link: [You do not have access to non-Amazon prefixes](../facts/direct-connect.md#direct-connect-public-vif-reaches-amazon-prefixes-not-non-amazon)
direct-connect-quota-active-connections-per-location
  claim: An account can have 10 active Direct Connect connections per Direct Connect location per Region by default; for more, contact your Solutions Architect or Technical Account Manager.
  scope: per Direct Connect location, per Region, per account; default; adjustable; contact your Solutions Architect or Technical Account Manager.
  link: [10 active Direct Connect connections](../facts/direct-connect.md#direct-connect-quota-active-connections-per-location)
  say: ten
direct-connect-quota-cloud-wan-advertised-prefixes
  claim: At most 5,000 route prefixes can be advertised from an AWS Cloud WAN core network Direct Connect gateway attachment to on-premises by default; all transit virtual interfaces attached to that Direct Connect gateway receive them, and for more you contact your Solutions Architect or Technical Account Manager.
  scope: per Cloud WAN core network Direct Connect gateway attachment; maximum; adjustable; contact your Solutions Architect or Technical Account Manager.
  link: [5,000 route prefixes](../facts/direct-connect.md#direct-connect-quota-cloud-wan-advertised-prefixes)
  say: five thousand
direct-connect-quota-dedicated-connections-per-lag
  claim: A link aggregation group can hold 4 dedicated connections when the port speed is less than 100G, and 2 when the port speed is 100G.
  scope: per link aggregation group (LAG); maximum; not adjustable.
  link: [4 when the port speed is less than 100G](../facts/direct-connect.md#direct-connect-quota-dedicated-connections-per-lag)
  link: [2 when the port speed is 100G](../facts/direct-connect.md#direct-connect-quota-dedicated-connections-per-lag)
  say: four | two
direct-connect-quota-dxgws-per-tgw
  claim: A transit gateway can be associated with at most 20 Direct Connect gateways; this limit cannot be increased.
  scope: per transit gateway; maximum; not adjustable.
  link: [20 Direct Connect gateways](../facts/direct-connect.md#direct-connect-quota-dxgws-per-tgw)
  say: twenty
direct-connect-quota-gateways-per-account
  claim: An account can have 200 Direct Connect gateways by default; for more, contact your Solutions Architect or Technical Account Manager.
  scope: per account; default; adjustable; contact your Solutions Architect or Technical Account Manager.
  link: [200 Direct Connect gateways](../facts/direct-connect.md#direct-connect-quota-gateways-per-account)
  say: two hundred
direct-connect-quota-lags-per-region
  claim: An account can have 10 link aggregation groups per Region by default; for more, contact your Solutions Architect or Technical Account Manager.
  scope: per Region, per account; default; adjustable; contact your Solutions Architect or Technical Account Manager.
  link: [10 link aggregation groups](../facts/direct-connect.md#direct-connect-quota-lags-per-region)
  say: ten
direct-connect-quota-prefixes-per-tgw-to-onprem
  claim: From a transit gateway to on-premises on a transit virtual interface, 200 prefixes in total for IPv4 and IPv6 combined is the default; for more, contact your Solutions Architect or Technical Account Manager.
  scope: per AWS Transit Gateway, from AWS to on-premises on a transit virtual interface; maximum; adjustable; contact your Solutions Architect or Technical Account Manager.
  link: [200 combined total for IPv4 and IPv6](../facts/direct-connect.md#direct-connect-quota-prefixes-per-tgw-to-onprem)
  say: two hundred combined total for IPv4 and IPv6
direct-connect-quota-rate-limiters-per-dedicated
  claim: A Direct Connect dedicated connection supports 10 rate limiters. For more, the quotas page says to contact your Solutions Architect or Technical Account Manager, while the VIF rate limiters page says you can request a limit increase through AWS Service Quotas.
  scope: per dedicated connection; default; adjustable.
  link: [10 rate limiters](../facts/direct-connect.md#direct-connect-quota-rate-limiters-per-dedicated)
  say: ten
direct-connect-quota-routes-per-bgp-session-private-transit
  claim: On a private or transit virtual interface the default is 100 routes each for IPv4 and IPv6 per BGP session from on-premises to AWS; if you advertise more route prefixes than your configured allocations, the BGP session goes idle and is reported DOWN. The quotas row also says prefix controls can raise the allocation up to 1,000 each.
  scope: per BGP session on a private or transit virtual interface, from on-premises to AWS; default; adjustable; can be increased using prefix controls up to 1,000 each for IPv4 and IPv6.
  link: [100 each for IPv4 and IPv6](../facts/direct-connect.md#direct-connect-quota-routes-per-bgp-session-private-transit)
  say: one hundred each for IPv4 and IPv6
  changed: 2026-08-20: was a maximum of 100 route prefixes
direct-connect-quota-routes-per-bgp-session-public
  claim: On a public virtual interface the quota is 1,000 routes per BGP session; this limit cannot be increased.
  scope: per BGP session on a public virtual interface; maximum; not adjustable.
  link: [1,000 routes](../facts/direct-connect.md#direct-connect-quota-routes-per-bgp-session-public)
  say: one thousand
direct-connect-quota-sitelink-prefix-limit
  claim: The SiteLink prefix limit is up to 1,000 each for IPv4 and IPv6, configured on a private or transit virtual interface using prefix controls; for more, contact your Solutions Architect or Technical Account Manager.
  scope: per private or transit virtual interface with SiteLink; maximum; adjustable; configured using prefix controls.
  link: [up to 1,000 each for IPv4 and IPv6](../facts/direct-connect.md#direct-connect-quota-sitelink-prefix-limit)
direct-connect-quota-tgws-per-dxgw
  claim: A Direct Connect gateway can have at most 6 transit gateways associated; this limit cannot be increased.
  scope: per Direct Connect gateway; maximum; not adjustable.
  link: [6 transit gateways](../facts/direct-connect.md#direct-connect-quota-tgws-per-dxgw)
  say: six
direct-connect-quota-transit-vifs-per-dedicated
  claim: A Direct Connect dedicated connection supports 4 transit virtual interfaces by default; for more, contact your Solutions Architect or Technical Account Manager.
  scope: per dedicated connection; default; adjustable; contact your Solutions Architect or Technical Account Manager.
  link: [4 transit virtual interfaces](../facts/direct-connect.md#direct-connect-quota-transit-vifs-per-dedicated)
  say: four
direct-connect-quota-vgws-per-dxgw
  claim: A Direct Connect gateway can have at most 20 virtual private gateways associated; this limit cannot be increased.
  scope: per Direct Connect gateway; maximum; not adjustable.
  link: [20 virtual private gateways](../facts/direct-connect.md#direct-connect-quota-vgws-per-dxgw)
  say: twenty
direct-connect-quota-vifs-per-dxgw
  claim: A Direct Connect gateway can have at most 30 private or transit virtual interfaces; this limit cannot be increased.
  scope: per Direct Connect gateway; maximum; not adjustable.
  link: [30 private or transit virtual interfaces](../facts/direct-connect.md#direct-connect-quota-vifs-per-dxgw)
  say: thirty
direct-connect-quota-vifs-per-hosted-connection
  claim: A Direct Connect hosted connection supports 1 private, public, or transit virtual interface; this limit cannot be increased.
  scope: per hosted connection; maximum; not adjustable.
  link: [1 private, public, or transit virtual interface](../facts/direct-connect.md#direct-connect-quota-vifs-per-hosted-connection)
  say: one
direct-connect-quota-vifs-per-lag
  claim: A link aggregation group supports at most 51 virtual interfaces, with up to four of them transit virtual interfaces; this limit cannot be increased.
  scope: per link aggregation group (LAG); maximum; not adjustable.
  link: [51 virtual interfaces](../facts/direct-connect.md#direct-connect-quota-vifs-per-lag)
  say: fifty-one
direct-connect-quota-vifs-per-vgw-no-limit
  claim: There is no limit on the number of virtual interfaces per virtual private gateway.
  scope: per virtual private gateway; maximum; not adjustable.
  link: [There is no limit](../facts/direct-connect.md#direct-connect-quota-vifs-per-vgw-no-limit)
direct-connect-quota-vifs-private-public-per-dedicated
  claim: A Direct Connect dedicated connection supports at most 50 private or public virtual interfaces; this limit cannot be increased.
  scope: per dedicated connection; maximum; not adjustable.
  link: [50 private or public virtual interfaces](../facts/direct-connect.md#direct-connect-quota-vifs-private-public-per-dedicated)
  say: fifty
direct-connect-quota-vifs-total-per-dedicated
  claim: A Direct Connect dedicated connection supports at most 51 virtual interfaces in total, counting the transit virtual interfaces; this limit cannot be increased.
  scope: per dedicated connection; maximum; not adjustable.
  link: [51 virtual interfaces](../facts/direct-connect.md#direct-connect-quota-vifs-total-per-dedicated)
  say: fifty-one
direct-connect-reliability-level-should-match-site-importance-cost
  claim: Not every hybrid connectivity solution needs a high level of reliability, and increasing levels of reliability have a corresponding increase in cost.
  scope: hybrid connectivity reliability.
  link: [requires a high level of reliability](../facts/direct-connect.md#direct-connect-reliability-level-should-match-site-importance-cost)
  link: [a corresponding increase in cost](../facts/direct-connect.md#direct-connect-reliability-level-should-match-site-importance-cost)
direct-connect-requirement-802-1q-vlan-whole-path
  claim: 802.1Q VLAN encapsulation must be supported across the entire Direct Connect connection, including intermediate devices.
  scope: Direct Connect connection path.
  link: [802.1Q VLAN encapsulation must be supported across the entire connection](../facts/direct-connect.md#direct-connect-requirement-802-1q-vlan-whole-path)
  link: [including intermediate devices](../facts/direct-connect.md#direct-connect-requirement-802-1q-vlan-whole-path)
direct-connect-requirement-bgp-and-md5-on-your-device
  claim: Your device must support Border Gateway Protocol (BGP) and BGP MD5 authentication.
  scope: customer router for Direct Connect.
  link: [Your device must support Border Gateway Protocol (BGP) and BGP MD5 authentication](../facts/direct-connect.md#direct-connect-requirement-bgp-and-md5-on-your-device)
  link: [Border Gateway Protocol (BGP)](../facts/direct-connect.md#direct-connect-requirement-bgp-and-md5-on-your-device)
direct-connect-requirement-single-mode-fiber-transceivers
  claim: Your network must use single-mode fiber with a transceiver that matches the port speed: 1000BASE-LX for 1 gigabit Ethernet, 10GBASE-LR for 10 gigabit, 100GBASE-LR4 for 100 gigabit and 400GBASE-LR4 for 400 Gbps.
  scope: dedicated connections of 1 Gbps or higher; fixed.
  link: [single-mode fiber](../facts/direct-connect.md#direct-connect-requirement-single-mode-fiber-transceivers)
  link: [a 10GBASE-LR (1310 nm) transceiver for 10 gigabit](../facts/direct-connect.md#direct-connect-requirement-single-mode-fiber-transceivers)
direct-connect-resiliency-dev-test-one-location-no-location-failure-protection
  claim: The development and test model uses separate connections that terminate on separate devices in one location, for non-critical workloads. It protects against device failure but not against location failure.
  scope: Direct Connect Resiliency Toolkit development and test model.
  link: [terminate on separate devices in one location](../facts/direct-connect.md#direct-connect-resiliency-dev-test-one-location-no-location-failure-protection)
  link: [does not provide resiliency against location failure](../facts/direct-connect.md#direct-connect-resiliency-dev-test-one-location-no-location-failure-protection)
direct-connect-resiliency-high-sla-99-9
  claim: The high resiliency model in the Resiliency Toolkit lets you order dedicated connections to achieve an SLA of 99.9%, if you meet all requirements specified in the Direct Connect Service Level Agreement.
  scope: Resiliency Toolkit high resiliency model; fixed; you meet all requirements of the Direct Connect Service Level Agreement.
  link: [an SLA of 99.9%](../facts/direct-connect.md#direct-connect-resiliency-high-sla-99-9)
  link: [High Resiliency](../facts/direct-connect.md#direct-connect-resiliency-high-sla-99-9)
direct-connect-resiliency-high-two-connections-multiple-locations
  claim: High resiliency for critical workloads uses two single connections to multiple locations. It protects against connectivity failures caused by a fiber cut or a device failure, and helps prevent a complete location failure.
  scope: Direct Connect Resiliency Toolkit high resiliency model.
  link: [two single connections to multiple locations](../facts/direct-connect.md#direct-connect-resiliency-high-two-connections-multiple-locations)
  link: [a fiber cut or a device failure](../facts/direct-connect.md#direct-connect-resiliency-high-two-connections-multiple-locations)
direct-connect-resiliency-maximum-multi-site-redundant-critical
  claim: Maximum resilience is achieved by separate connections terminating on separate devices in more than one location, which gives resilience to device failure, connectivity failure and complete location failure.
  scope: Direct Connect maximum resiliency for critical production workloads.
  link: [separate devices in more than one location](../facts/direct-connect.md#direct-connect-resiliency-maximum-multi-site-redundant-critical)
  link: [connectivity failure, and complete location failure](../facts/direct-connect.md#direct-connect-resiliency-maximum-multi-site-redundant-critical)
direct-connect-resiliency-maximum-separate-devices-more-than-one-location
  claim: Maximum resiliency for critical workloads uses separate connections that terminate on separate devices in more than one location. It gives resiliency against device, connectivity and complete location failures.
  scope: Direct Connect Resiliency Toolkit maximum resiliency model.
  link: [separate devices in more than one location](../facts/direct-connect.md#direct-connect-resiliency-maximum-separate-devices-more-than-one-location)
  link: [resiliency against device, connectivity, and complete location failures](../facts/direct-connect.md#direct-connect-resiliency-maximum-separate-devices-more-than-one-location)
direct-connect-resiliency-maximum-sla-99-99
  claim: The maximum resiliency model in the Resiliency Toolkit lets you order dedicated connections to achieve an SLA of 99.99%, if you meet all requirements specified in the Direct Connect Service Level Agreement.
  scope: Resiliency Toolkit maximum resiliency model; fixed; you meet all requirements of the Direct Connect Service Level Agreement.
  link: [an SLA of 99.99%](../facts/direct-connect.md#direct-connect-resiliency-maximum-sla-99-99)
  link: [Maximum Resiliency](../facts/direct-connect.md#direct-connect-resiliency-maximum-sla-99-99)
direct-connect-resiliency-production-use-multi-site-only
  claim: For production workloads, AWS does not recommend any deployment other than a multi-site redundant deployment or a multi-site non-redundant deployment.
  scope: production workloads on Direct Connect.
  link: [AWS does not recommend using any Deployment](../facts/direct-connect.md#direct-connect-resiliency-production-use-multi-site-only)
  link: [Multi-Site Redundant Deployment](../facts/direct-connect.md#direct-connect-resiliency-production-use-multi-site-only)
direct-connect-resiliency-use-dynamic-routing-active-active
  claim: AWS recommends multiple dynamically routed, rather than statically routed, connections to AWS at multiple Direct Connect locations so that remote connections fail over automatically.
  scope: Direct Connect resiliency.
  link: [dynamically routed, rather than statically routed, connections](../facts/direct-connect.md#direct-connect-resiliency-use-dynamic-routing-active-active)
  link: [remote connections to fail over automatically](../facts/direct-connect.md#direct-connect-resiliency-use-dynamic-routing-active-active)
direct-connect-restriction-flat-rate-dedicated-only
  claim: Flat-rate billing applies to dedicated connections only; hosted connections provisioned by a Direct Connect partner are not eligible.
  scope: per connection; fixed.
  link: [dedicated connections only](../facts/direct-connect.md#direct-connect-restriction-flat-rate-dedicated-only)
direct-connect-restriction-hosted-25g-needs-100g-location
  claim: 25 Gbps hosted connections are available only in Direct Connect locations where 100 Gbps port speeds are available.
  scope: per Direct Connect location; fixed.
  link: [only in Direct Connect locations where 100 Gbps port speeds are available](../facts/direct-connect.md#direct-connect-restriction-hosted-25g-needs-100g-location)
direct-connect-restriction-hosted-high-speeds-select-partners
  claim: Only Direct Connect partners that have met specific requirements may create a 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, or 25 Gbps hosted connection.
  scope: per hosted connection; fixed.
  link: [1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, or 25 Gbps](../facts/direct-connect.md#direct-connect-restriction-hosted-high-speeds-select-partners)
direct-connect-restriction-rate-limiters-dedicated-only
  claim: VIF Rate Limiters are supported only on dedicated connections, not on hosted connections; hosted connections are always rate-limited to the purchased capacity.
  scope: per connection; fixed.
  link: [only supported on Dedicated connections](../facts/direct-connect.md#direct-connect-restriction-rate-limiters-dedicated-only)
direct-connect-scalability-fewer-bgp-sessions-with-dxgw
  claim: To reduce the number of BGP peering sessions, use a Direct Connect gateway with a virtual private gateway or a transit gateway, where a single BGP session can provide connectivity to multiple VPCs.
  scope: Direct Connect scalability.
  link: [Minimize your number of BGP peering sessions](../facts/direct-connect.md#direct-connect-scalability-fewer-bgp-sessions-with-dxgw)
  link: [a single BGP session can provide connectivity](../facts/direct-connect.md#direct-connect-scalability-fewer-bgp-sessions-with-dxgw)
direct-connect-sdwan-or-software-vpn-only-as-reliable-as-transport
  claim: SD-WAN and customer-managed VPNs can run over the internet or Direct Connect, and are only as reliable as the underlying network transport.
  scope: customer-managed VPN and SD-WAN.
  link: [as reliable as the underlying network transport](../facts/direct-connect.md#direct-connect-sdwan-or-software-vpn-only-as-reliable-as-transport)
  link: [can run over internet or AWS Direct Connect](../facts/direct-connect.md#direct-connect-sdwan-or-software-vpn-only-as-reliable-as-transport)
direct-connect-sitelink-not-in-govcloud-and-china
  claim: SiteLink is not available in AWS GovCloud (US) and the China Regions.
  scope: Direct Connect SiteLink.
  link: [SiteLink is not available in AWS GovCloud (US)](../facts/direct-connect.md#direct-connect-sitelink-not-in-govcloud-and-china)
  link: [AWS GovCloud (US) and the China Regions](../facts/direct-connect.md#direct-connect-sitelink-not-in-govcloud-and-china)
direct-connect-sitelink-pop-to-pop-bypass-regions
  claim: SiteLink is an optional Direct Connect feature for private virtual interfaces. It connects any two Direct Connect points of presence in the same AWS partition by the shortest path over the AWS network, so your traffic does not need to route through a Region.
  scope: Direct Connect SiteLink.
  link: [any two Direct Connect points of presence (PoPs)](../facts/direct-connect.md#direct-connect-sitelink-pop-to-pop-bypass-regions)
  link: [route your traffic through a Region](../facts/direct-connect.md#direct-connect-sitelink-pop-to-pop-bypass-regions)
direct-connect-sitelink-private-or-transit-vif-with-dxgw
  claim: You can use SiteLink when you create a private or transit virtual interface, and the SiteLink-enabled virtual interfaces must connect to a Direct Connect gateway.
  scope: Direct Connect SiteLink.
  link: [a private or transit virtual interface](../facts/direct-connect.md#direct-connect-sitelink-private-or-transit-vif-with-dxgw)
  link: [to an AWS Direct Connect gateway](../facts/direct-connect.md#direct-connect-sitelink-private-or-transit-vif-with-dxgw)
direct-connect-sitelink-separate-pricing-fee-off-by-default
  claim: There is a separate pricing fee for using SiteLink, and the SiteLink feature is off by default and can be turned on or off at any time.
  scope: Direct Connect SiteLink; default; turn on or off at any time.
  link: [There's a separate pricing fee for using SiteLink](../facts/direct-connect.md#direct-connect-sitelink-separate-pricing-fee-off-by-default)
  link: [The SiteLink feature is off by default](../facts/direct-connect.md#direct-connect-sitelink-separate-pricing-fee-off-by-default)
direct-connect-sitelink-vs-cloud-wan
  claim: Cloud WAN can create and manage networks of VPCs across multiple Regions, while Direct Connect SiteLink connects Direct Connect locations together, bypassing AWS Regions to improve performance. You might choose one, the other, or both.
  scope: Direct Connect SiteLink versus Cloud WAN.
  link: [networks of VPCs across multiple Regions](../facts/direct-connect.md#direct-connect-sitelink-vs-cloud-wan)
  link: [connects DX locations together, bypassing AWS Regions](../facts/direct-connect.md#direct-connect-sitelink-vs-cloud-wan)
direct-connect-sla-classic-95
  claim: A Classic Direct Connect connection has a 95% SLA but does not provide resiliency or redundancy.
  scope: per Classic connection; fixed.
  link: [95% SLA](../facts/direct-connect.md#direct-connect-sla-classic-95)
  say: ninety-five percent
direct-connect-sla-multi-site-non-redundant-definition
  claim: A Multi-Site Non-Redundant Deployment has at least two Connections across at least two different Direct Connect locations and needs an Enterprise Support plan.
  scope: per deployment; minimum.
  link: [at least two Connections](../facts/direct-connect.md#direct-connect-sla-multi-site-non-redundant-definition)
  say: at least two
direct-connect-sla-multi-site-redundant-definition
  claim: A Multi-Site Redundant Deployment has at least four Connections across at least two different Direct Connect locations, with no fewer than two in each location and each Connection on a unique AWS device.
  scope: per deployment; minimum.
  link: [at least four Connections](../facts/direct-connect.md#direct-connect-sla-multi-site-redundant-definition)
  say: at least four
direct-connect-sla-multi-site-redundant-support-and-review
  claim: For a Multi-Site Redundant Deployment under the Direct Connect SLA you must have an Enterprise Support plan and have completed a Well-Architected Review with an AWS Solutions Architect.
  scope: per deployment; fixed.
  link: [Enterprise Support plan in place](../facts/direct-connect.md#direct-connect-sla-multi-site-redundant-support-and-review)
direct-connect-sla-not-for-hosted
  claim: The Direct Connect SLAs do not apply to Direct Connect services accessed through an APN Direct Connect Partner integration using a hosted connection or hosted virtual interfaces. They apply to dedicated connections that you access through services of an APN Direct Connect Partner, provided those dedicated connections are owned by your AWS account.
  scope: per connection; fixed.
  link: [do not apply](../facts/direct-connect.md#direct-connect-sla-not-for-hosted)
direct-connect-sla-three-commitments
  claim: AWS makes three SLA commitments for Direct Connect: a Multi-Site Redundant SLA, a Multi-Site Non-Redundant SLA, and a Single Connection SLA for individual Connections.
  scope: per account; fixed.
  link: [three SLA commitments](../facts/direct-connect.md#direct-connect-sla-three-commitments)
  say: three
direct-connect-sla-unavailable-120-seconds
  claim: In the Direct Connect SLA, a Deployment or Connection is Unavailable after the complete inability to send or receive data through it for at least 120 consecutive seconds.
  scope: per Deployment or Connection; minimum.
  link: [at least 120 consecutive seconds](../facts/direct-connect.md#direct-connect-sla-unavailable-120-seconds)
  say: at least one hundred twenty consecutive seconds
direct-connect-sla-whitepaper-formal-sla-recommended
  claim: Direct Connect offers a formal SLA with service credits calculated as a percentage of port hour charges, and the hybrid connectivity whitepaper calls it the recommended transport if an SLA is required.
  scope: per account; fixed.
  link: [the recommended transport if an SLA is required](../facts/direct-connect.md#direct-connect-sla-whitepaper-formal-sla-recommended)
direct-connect-sla-whitepaper-responsibility-ends-at-port
  claim: The AWS responsibility for Direct Connect ends at the Direct Connect location at the Direct Connect port; once AWS hands traffic off to your network, it is no longer the responsibility of AWS.
  scope: per connection; fixed.
  link: [ends at the AWS Direct Connect location](../facts/direct-connect.md#direct-connect-sla-whitepaper-responsibility-ends-at-port)
direct-connect-tgw-attachment-single-connection-for-many-vpcs
  claim: Attaching a transit gateway to a Direct Connect gateway with a transit virtual interface lets you manage a single connection for multiple VPCs or VPNs in the same Region and advertise prefixes in both directions.
  scope: transit gateway attachment to a Direct Connect gateway.
  link: [a single connection for multiple VPCs or VPNs](../facts/direct-connect.md#direct-connect-tgw-attachment-single-connection-for-many-vpcs)
  link: [Advertise prefixes from on-premises to AWS](../facts/direct-connect.md#direct-connect-tgw-attachment-single-connection-for-many-vpcs)
direct-connect-traffic-stays-on-aws-global-network-backbone
  claim: All networking traffic stays on the AWS global network backbone, whether you access public AWS services or a VPC.
  scope: Direct Connect access to AWS Regions.
  link: [remains on the AWS global network backbone](../facts/direct-connect.md#direct-connect-traffic-stays-on-aws-global-network-backbone)
  link: [public AWS services or a VPC](../facts/direct-connect.md#direct-connect-traffic-stays-on-aws-global-network-backbone)
direct-connect-transit-vif-attaches-only-to-dxgw
  claim: A transit virtual interface is a virtual interface you can create on any Direct Connect connection, and it can only be attached to a Direct Connect gateway.
  scope: transit virtual interface.
  link: [attached to an AWS Direct Connect gateway](../facts/direct-connect.md#direct-connect-transit-vif-attaches-only-to-dxgw)
  link: [create on any AWS Direct Connect connection](../facts/direct-connect.md#direct-connect-transit-vif-attaches-only-to-dxgw)
direct-connect-vgw-dxgw-and-vpn-failover-needs-route-to-vgw
  claim: With a virtual private gateway attached to both a VPN and a Direct Connect gateway, VPC traffic routes out to the VPN if the Direct Connect circuit goes down, as long as the VPC route table has routes to the virtual private gateway towards the VPN.
  scope: virtual private gateway with VPN and Direct Connect gateway.
  link: [has routes to the virtual private gateway (VGW)](../facts/direct-connect.md#direct-connect-vgw-dxgw-and-vpn-failover-needs-route-to-vgw)
direct-connect-vif-private-access-vpc-private-ips
  claim: A private virtual interface is used to access an Amazon VPC using private IP addresses.
  scope: Direct Connect virtual interfaces.
  link: [access an Amazon VPC using private IP addresses](../facts/direct-connect.md#direct-connect-vif-private-access-vpc-private-ips)
  link: [access an Amazon VPC](../facts/direct-connect.md#direct-connect-vif-private-access-vpc-private-ips)
direct-connect-vif-public-access-aws-public-services
  claim: A public virtual interface can access all AWS public services using public IP addresses.
  scope: Direct Connect virtual interfaces.
  link: [all AWS public services using public IP addresses](../facts/direct-connect.md#direct-connect-vif-public-access-aws-public-services)
  link: [all AWS public services](../facts/direct-connect.md#direct-connect-vif-public-access-aws-public-services)
direct-connect-vif-transit-access-transit-gateways-any-speed
  claim: A transit virtual interface is used to access one or more Amazon VPC transit gateways associated with Direct Connect gateways. It can be used with any dedicated or hosted connection of any speed.
  scope: Direct Connect virtual interfaces.
  link: [one or more Amazon VPC Transit Gateways](../facts/direct-connect.md#direct-connect-vif-transit-access-transit-gateways-any-speed)
  link: [dedicated or hosted connection of any speed](../facts/direct-connect.md#direct-connect-vif-transit-access-transit-gateways-any-speed)
direct-connect-vpn-over-dx-adds-encryption-reduces-mtu
  claim: Using a VPN over Direct Connect adds encryption but reduces the MTU size, which might reduce throughput. MACsec does not have the same MTU or throughput considerations as Site-to-Site VPN.
  scope: encryption over Direct Connect.
  link: [it reduces the MTU size](../facts/direct-connect.md#direct-connect-vpn-over-dx-adds-encryption-reduces-mtu)
  link: [MACsec does not have the same MTU](../facts/direct-connect.md#direct-connect-vpn-over-dx-adds-encryption-reduces-mtu)
direct-connect-vpn-same-vpc-failover-only-dx-path-preferred
  claim: You can use Direct Connect and a VPN connection to the same VPC at the same time, but only for failover. The Direct Connect path is always preferred when established, regardless of AS path prepending, so the VPN connections must handle the failover traffic.
  scope: Direct Connect with Site-to-Site VPN on the same VPC.
  link: [Yes, but only for failover](../facts/direct-connect.md#direct-connect-vpn-same-vpc-failover-only-dx-path-preferred)
  link: [regardless of AS path prepending](../facts/direct-connect.md#direct-connect-vpn-same-vpc-failover-only-dx-path-preferred)
  link: [will always be preferred, when established](../facts/direct-connect.md#direct-connect-vpn-same-vpc-failover-only-dx-path-preferred)
direct-connect-vs-vpn-bandwidth-tgw-ecmp-scales-vpn-horizontally
  claim: AWS Transit Gateway lets customers scale the number of VPN connections horizontally and raise throughput accordingly with equal-cost multi-path routing (ECMP).
  scope: Site-to-Site VPN on a transit gateway.
  link: [horizontally scale the number of VPN connections](../facts/direct-connect.md#direct-connect-vs-vpn-bandwidth-tgw-ecmp-scales-vpn-horizontally)
  link: [Equal-cost multi-path routing (ECMP)](../facts/direct-connect.md#direct-connect-vs-vpn-bandwidth-tgw-ecmp-scales-vpn-horizontally)
direct-connect-vs-vpn-internet-vpn-best-effort-low-cost-widely-available
  claim: AWS managed Site-to-Site VPN over the internet can be attractive because of low cost and wide availability, but performance over the internet is best effort and internet congestion and latency can be unpredictable.
  scope: Site-to-Site VPN over the internet.
  link: [performance over the internet is best effort](../facts/direct-connect.md#direct-connect-vs-vpn-internet-vpn-best-effort-low-cost-widely-available)
  link: [low cost and is widely available](../facts/direct-connect.md#direct-connect-vs-vpn-internet-vpn-best-effort-low-cost-widely-available)
direct-connect-vs-vpn-performance-dx-for-predictable-latency-throughput
  claim: When predictable latency and throughput are required, Direct Connect is the recommended choice because it provides deterministic performance. AWS recommends it when you need a more consistent network experience than internet-based connections can provide.
  scope: hybrid connectivity performance.
  link: [it provides deterministic performance](../facts/direct-connect.md#direct-connect-vs-vpn-performance-dx-for-predictable-latency-throughput)
  link: [a more consistent network experience](../facts/direct-connect.md#direct-connect-vs-vpn-performance-dx-for-predictable-latency-throughput)
direct-connect-vs-vpn-security-internet-uses-vpn-private-uses-dx
  claim: If you can use the internet, AWS Site-to-Site VPN creates encrypted tunnels over it. If you require a private network connection, AWS recommends Direct Connect dedicated or hosted connections.
  scope: hybrid connectivity security requirements.
  link: [create encrypted tunnels between your network](../facts/direct-connect.md#direct-connect-vs-vpn-security-internet-uses-vpn-private-uses-dx)
  link: [Dedicated Connections or Hosted Connections](../facts/direct-connect.md#direct-connect-vs-vpn-security-internet-uses-vpn-private-uses-dx)
direct-connect-vs-vpn-selection-criteria-five-considerations
  claim: The considerations that affect the hybrid connectivity type you select include time to deploy, security, SLA, performance, and cost.
  scope: hybrid connectivity type selection.
  link: [time to deploy, security, SLA, performance, and cost](../facts/direct-connect.md#direct-connect-vs-vpn-selection-criteria-five-considerations)
  link: [the connectivity type you select for your workload](../facts/direct-connect.md#direct-connect-vs-vpn-selection-criteria-five-considerations)
direct-connect-vs-vpn-time-dedicated-weeks-to-months
  claim: A new dedicated Direct Connect connection can take from several weeks to a few months to install, depending on the service provider, the location of your site, and other physical factors.
  scope: net-new dedicated connections.
  link: [from several weeks to a few months](../facts/direct-connect.md#direct-connect-vs-vpn-time-dedicated-weeks-to-months)
  link: [Depending on the service provider](../facts/direct-connect.md#direct-connect-vs-vpn-time-dedicated-weeks-to-months)
direct-connect-vs-vpn-time-hosted-faster-than-dedicated
  claim: Hosted connections can often be provisioned faster than dedicated connections, because the partner provisions each one using existing infrastructure that is connected to the AWS backbone.
  scope: hosted versus dedicated connections.
  link: [can often be provisioned faster than Dedicated Connections](../facts/direct-connect.md#direct-connect-vs-vpn-time-hosted-faster-than-dedicated)
  link: [using their existing infrastructure](../facts/direct-connect.md#direct-connect-vs-vpn-time-hosted-faster-than-dedicated)
direct-connect-vs-vpn-time-to-deploy-provisioning-row
  claim: The whitepaper rates provisioning time as hours to days for internet-based connectivity, days for a dedicated connection with equipment already in the location, several weeks to months for a net-new dedicated connection, and hours to days for a hosted connection on an existing partner port.
  scope: time to deploy comparison in the hybrid connectivity whitepaper.
  link: [Hours to days](../facts/direct-connect.md#direct-connect-vs-vpn-time-to-deploy-provisioning-row)
  link: [Several weeks to months](../facts/direct-connect.md#direct-connect-vs-vpn-time-to-deploy-provisioning-row)
direct-connect-vs-vpn-time-vpn-hours-days-existing-connection
  claim: If you need AWS connectivity within hours or days, you will most likely use an existing network connection, which often means a VPN over the public internet. A new hosted connection from an existing Direct Connect Partner could be provisioned within hours.
  scope: time to deploy for hybrid connectivity.
  link: [VPN connection to AWS over the public internet](../facts/direct-connect.md#direct-connect-vs-vpn-time-vpn-hours-days-existing-connection)
  link: [could be provisioned within hours](../facts/direct-connect.md#direct-connect-vs-vpn-time-vpn-hours-days-existing-connection)
direct-connect-vs-vpn-vpn-throughput-limited-by-overhead-mtu
  claim: VPNs can limit throughput because of tunneling overheads, lower MTU limits, or hardware bandwidth limitations.
  scope: VPN throughput.
  link: [tunneling overheads, lower MTU limits](../facts/direct-connect.md#direct-connect-vs-vpn-vpn-throughput-limited-by-overhead-mtu)
  link: [tunneling overheads](../facts/direct-connect.md#direct-connect-vs-vpn-vpn-throughput-limited-by-overhead-mtu)
direct-connect-wa-anti-pattern-overestimating-vpn-backup-bandwidth
  claim: Well-Architected lists as anti-patterns relying on one network connection, using one VPN tunnel or tunnels that end in the same Availability Zone, and ignoring the bandwidth limits of VPN tunnels so that you overestimate their backup capability.
  scope: REL02-BP02 redundant connectivity.
  link: [creates a single point of failure](../facts/direct-connect.md#direct-connect-wa-anti-pattern-overestimating-vpn-backup-bandwidth)
  link: [overestimate their backup capabilities](../facts/direct-connect.md#direct-connect-wa-anti-pattern-overestimating-vpn-backup-bandwidth)
direct-connect-wa-max-resiliency-separate-devices-more-than-one-location
  claim: The Well-Architected Framework says you achieve maximum network resiliency (SLA of 99.99%) with separate connections that end on distinct devices in more than one on-premises location and more than one Direct Connect location.
  scope: REL02-BP02 redundant connectivity.
  link: [maximum network resiliency (SLA of 99.99%)](../facts/direct-connect.md#direct-connect-wa-max-resiliency-separate-devices-more-than-one-location)
  link: [distinct devices in more than one on-premises location](../facts/direct-connect.md#direct-connect-wa-max-resiliency-separate-devices-more-than-one-location)
site-to-site-vpn-accelerated-cannot-toggle-on-existing
  claim: You cannot turn acceleration on or off for an existing Site-to-Site VPN connection. You create a new connection with acceleration on or off, point the device to it, and delete the old connection.
  scope: existing Site-to-Site VPN connections.
  link: [You cannot turn on or turn off acceleration](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-cannot-toggle-on-existing)
  link: [create a new Site-to-Site VPN connection](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-cannot-toggle-on-existing)
site-to-site-vpn-accelerated-design-optimized-vpn-over-internet-with-tgw
  claim: The accelerated Site-to-Site VPN with transit gateway reference design provides optimized VPN connections over the public internet, and can reach higher bandwidth by configuring multiple VPN tunnels with ECMP.
  scope: accelerated Site-to-Site VPN with Transit Gateway, single Region.
  link: [optimized VPN connections over the public internet](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-design-optimized-vpn-over-internet-with-tgw)
  link: [configuring multiple VPN tunnels with ECMP](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-design-optimized-vpn-over-internet-with-tgw)
site-to-site-vpn-accelerated-disabled-by-default
  claim: By default, acceleration is disabled when you create a Site-to-Site VPN connection; you can enable it when you create a new VPN attachment on a transit gateway.
  scope: new Site-to-Site VPN connections; default; adjustable; enable at creation on a transit gateway attachment.
  link: [acceleration is disabled](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-disabled-by-default)
  link: [You can optionally enable acceleration](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-disabled-by-default)
site-to-site-vpn-accelerated-nat-t-required-ike-from-cgw
  claim: NAT traversal is required for an accelerated VPN connection and is enabled by default. IKE negotiation for accelerated tunnels must be initiated from the customer gateway device.
  scope: accelerated Site-to-Site VPN.
  link: [NAT-traversal (NAT-T) is required](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-nat-t-required-ike-from-cgw)
  link: [must be initiated from the customer gateway device](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-nat-t-required-ike-from-cgw)
site-to-site-vpn-accelerated-no-public-dx-vif
  claim: An accelerated Site-to-Site VPN connection cannot be used with an AWS Direct Connect public virtual interface.
  scope: accelerated Site-to-Site VPN.
  link: [an AWS Direct Connect public virtual interface](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-no-public-dx-vif)
  link: [Accelerated Site-to-Site VPN connection](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-no-public-dx-vif)
site-to-site-vpn-accelerated-transit-gateway-only
  claim: Acceleration is supported only for Site-to-Site VPN connections attached to a transit gateway. Virtual private gateways do not support accelerated VPN connections.
  scope: accelerated Site-to-Site VPN.
  link: [Acceleration is only supported for Site-to-Site VPN connections](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-transit-gateway-only)
  link: [do not support accelerated VPN connections](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-transit-gateway-only)
site-to-site-vpn-accelerated-two-accelerators-managed-by-aws
  claim: AWS creates and manages two accelerators for an accelerated VPN connection, one for each tunnel. You cannot view or manage them in the AWS Global Accelerator console or APIs.
  scope: accelerated Site-to-Site VPN.
  link: [we create and manage two accelerators](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-two-accelerators-managed-by-aws)
  link: [You cannot view or manage these accelerators yourself](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-two-accelerators-managed-by-aws)
site-to-site-vpn-accelerated-uses-global-accelerator-nearest-edge
  claim: An accelerated Site-to-Site VPN connection uses AWS Global Accelerator to route traffic from your on-premises network to the AWS edge location closest to your customer gateway device.
  scope: accelerated Site-to-Site VPN.
  link: [uses AWS Global Accelerator to route traffic](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-uses-global-accelerator-nearest-edge)
  link: [closest to your customer gateway device](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-uses-global-accelerator-nearest-edge)
site-to-site-vpn-accelerated-why-consistent-experience
  claim: Accelerated Site-to-Site VPN makes the user experience more consistent by using the highly available and congestion-free AWS global network instead of multiple public internet networks.
  scope: accelerated Site-to-Site VPN.
  link: [makes user experience more consistent](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-why-consistent-experience)
  link: [the highly available and congestion-free AWS global network](../facts/site-to-site-vpn.md#site-to-site-vpn-accelerated-why-consistent-experience)
site-to-site-vpn-aws-initiated-ike-needs-cgw-public-ip-and-ikev2
  claim: For AWS to initiate IKE negotiation, AWS requires the public IP address of your customer gateway device, and IKE initiation from the AWS side is supported for IKEv2 only.
  scope: AWS-initiated IKE (startup action).
  link: [public IP address of your customer gateway device](../facts/site-to-site-vpn.md#site-to-site-vpn-aws-initiated-ike-needs-cgw-public-ip-and-ikev2)
  link: [supported for IKEv2 only](../facts/site-to-site-vpn.md#site-to-site-vpn-aws-initiated-ike-needs-cgw-public-ip-and-ikev2)
site-to-site-vpn-aws-managed-vpn-endpoint-automated-redundancy
  claim: The connectivity options whitepaper says to use Site-to-Site VPN when you want an AWS-managed VPN endpoint with automated redundancy and failover built into the AWS side. The virtual private gateway also supports multiple customer gateway connections so you can add redundancy on your side.
  scope: Site-to-Site VPN on a virtual private gateway.
  link: [automated redundancy and failover](../facts/site-to-site-vpn.md#site-to-site-vpn-aws-managed-vpn-endpoint-automated-redundancy)
  link: [supports and encourages multiple user gateway connections](../facts/site-to-site-vpn.md#site-to-site-vpn-aws-managed-vpn-endpoint-automated-redundancy)
site-to-site-vpn-bgp-recommended-liveness-failover
  claim: AWS recommends BGP-capable devices when available, because BGP offers robust liveness detection checks that can help failover to the second VPN tunnel when the first goes down.
  scope: Site-to-Site VPN routing.
  link: [use BGP-capable devices, when available](../facts/site-to-site-vpn.md#site-to-site-vpn-bgp-recommended-liveness-failover)
  link: [robust liveness detection checks](../facts/site-to-site-vpn.md#site-to-site-vpn-bgp-recommended-liveness-failover)
site-to-site-vpn-billing-connection-hour-while-available
  claim: VPN connection-hours are billed for any time your VPN connections are in the available state. To avoid further charges you terminate the VPN connection.
  scope: Site-to-Site VPN connection-hours.
  link: [in the "available" state](../facts/site-to-site-vpn.md#site-to-site-vpn-billing-connection-hour-while-available)
  link: [terminate the VPN connection](../facts/site-to-site-vpn.md#site-to-site-vpn-billing-connection-hour-while-available)
site-to-site-vpn-billing-public-ipv4-per-connection
  claim: Each Site-to-Site VPN connection uses unique public IPv4 addresses for its tunnels, and you incur standard public IPv4 address charges for them.
  scope: Site-to-Site VPN connection.
  link: [unique public IPv4 address for the tunnels](../facts/site-to-site-vpn.md#site-to-site-vpn-billing-public-ipv4-per-connection)
  link: [standard public IPv4 address charges](../facts/site-to-site-vpn.md#site-to-site-vpn-billing-public-ipv4-per-connection)
site-to-site-vpn-capability-concentrator-suitable-sites
  claim: VPN Concentrator suits customers who need to connect 25+ remote sites to AWS, with each site needing low bandwidth (under 100 Mbps).
  scope: per VPN Concentrator; minimum.
  link: [25+ remote sites](../facts/site-to-site-vpn.md#site-to-site-vpn-capability-concentrator-suitable-sites)
  link: [under 100 Mbps](../facts/site-to-site-vpn.md#site-to-site-vpn-capability-concentrator-suitable-sites)
  say: twenty-five or more remote sites | under one hundred megabits per second
site-to-site-vpn-capability-modify-tunnel-bandwidth
  claim: Large Bandwidth Tunnels are available only for VPN connections attached to a transit gateway or to Cloud WAN, not for virtual private gateway attachments, and you can modify the tunnel bandwidth of existing VPN connections.
  scope: Large Bandwidth Tunnels; VPN connections on a transit gateway or Cloud WAN.
  link: [modify the tunnel bandwidth of existing VPN connections](../facts/site-to-site-vpn.md#site-to-site-vpn-capability-modify-tunnel-bandwidth)
site-to-site-vpn-certificate-auth-private-ca
  claim: Instead of pre-shared keys, you can use a private certificate from AWS Private Certificate Authority to authenticate the VPN.
  scope: Site-to-Site VPN tunnels.
  link: [a private certificate from AWS Private Certificate Authority](../facts/site-to-site-vpn.md#site-to-site-vpn-certificate-auth-private-ca)
  link: [do not want to use pre-shared keys](../facts/site-to-site-vpn.md#site-to-site-vpn-certificate-auth-private-ca)
site-to-site-vpn-cgw-asn-ranges-private-16-and-32-bit
  claim: For dynamic routing, the BGP ASN of a customer gateway can be in the range 1–4,294,967,295 (some public ASNs such as 7224 are reserved). Without a public ASN you can use a private ASN in the range 64,512–65,534 or 4,200,000,000–4,294,967,294. The default ASN is 64512.
  scope: customer gateway BGP ASN, dynamic routing only; default; adjustable; you can use your own public ASN instead, except the reserved ones.
  link: [64,512–65,534](../facts/site-to-site-vpn.md#site-to-site-vpn-cgw-asn-ranges-private-16-and-32-bit)
  link: [4,200,000,000–4,294,967,294](../facts/site-to-site-vpn.md#site-to-site-vpn-cgw-asn-ranges-private-16-and-32-bit)
  link: [The default ASN is 64512](../facts/site-to-site-vpn.md#site-to-site-vpn-cgw-asn-ranges-private-16-and-32-bit)
site-to-site-vpn-cgw-behind-nat-use-nat-public-ip
  claim: If you place the customer gateway behind a router or firewall that does NAT, you give AWS the public IP address of the NAT device.
  scope: customer gateway behind a router or firewall.
  link: [the public IP address of your NAT device](../facts/site-to-site-vpn.md#site-to-site-vpn-cgw-behind-nat-use-nat-public-ip)
site-to-site-vpn-cgw-initiates-ike-by-default
  claim: By default, your customer gateway device must bring up the tunnels by generating traffic and starting the IKE negotiation. You can configure the tunnels so that AWS initiates or restarts the negotiation instead.
  scope: Site-to-Site VPN tunnels; default; adjustable; set the startup action to make AWS initiate.
  link: [customer gateway device must bring up the tunnels](../facts/site-to-site-vpn.md#site-to-site-vpn-cgw-initiates-ike-by-default)
  link: [AWS must initiate or restart the IKE negotiation](../facts/site-to-site-vpn.md#site-to-site-vpn-cgw-initiates-ike-by-default)
site-to-site-vpn-cgw-resource-does-not-configure-device
  claim: Creating the customer gateway resource in AWS does not configure or create the customer gateway device. You must configure the device yourself.
  scope: customer gateway resource.
  link: [not configure or create the customer gateway device](../facts/site-to-site-vpn.md#site-to-site-vpn-cgw-resource-does-not-configure-device)
  link: [You must configure the device yourself](../facts/site-to-site-vpn.md#site-to-site-vpn-cgw-resource-does-not-configure-device)
site-to-site-vpn-change-bgp-logging
  claim: On November 20, 2025 Site-to-Site VPN added BGP logs from VPN tunnels to CloudWatch; before, customers only had tunnel activity logs showing IKE and IPsec tunnel details.
  scope: per VPN tunnel; fixed.
  link: [detailed BGP logs](../facts/site-to-site-vpn.md#site-to-site-vpn-change-bgp-logging)
  changed: 2025-11-20: was customers only had access to tunnel activity logs showing IKE/IPSec tunnel details
site-to-site-vpn-change-ipv6-outer-tunnel-ips
  claim: On July 1, 2025 Site-to-Site VPN added IPv6 addresses for the outer tunnel IPs on Transit Gateway and Cloud WAN VPN connections.
  scope: per VPN connection; fixed.
  link: [IPv6 addresses for the outer tunnel IPs](../facts/site-to-site-vpn.md#site-to-site-vpn-change-ipv6-outer-tunnel-ips)
site-to-site-vpn-change-large-bandwidth-tunnels
  claim: On November 12, 2025 Site-to-Site VPN announced up to 5 Gbps bandwidth per tunnel, a 4x improvement from the existing limit of 1.25 Gbps; the document history lists Large Bandwidth Tunnels for transit gateway and Cloud WAN attachments on September 25, 2025.
  scope: per VPN tunnel; maximum.
  link: [up to 5 Gbps bandwidth per tunnel](../facts/site-to-site-vpn.md#site-to-site-vpn-change-large-bandwidth-tunnels)
  link: [1.25 Gbps](../facts/site-to-site-vpn.md#site-to-site-vpn-change-large-bandwidth-tunnels)
  say: up to five gigabits per second per tunnel | one point two five gigabits per second
  changed: 2025-11-12: was 1.25 Gbps
site-to-site-vpn-change-modify-tunnel-bandwidth
  claim: On May 6, 2026 Site-to-Site VPN added modifying tunnel bandwidth between standard (up to 1.25 Gbps) and large (up to 5 Gbps) on existing connections, preserving IP addresses, CIDR blocks, pre-shared keys and configuration; before, changing tunnel bandwidth required deleting and recreating the connection.
  scope: per VPN connection; fixed.
  link: [modifying tunnel bandwidth](../facts/site-to-site-vpn.md#site-to-site-vpn-change-modify-tunnel-bandwidth)
  changed: 2026-05-06: was changing tunnel bandwidth required deleting and recreating the connection
site-to-site-vpn-change-recommended-configuration
  claim: The GetVpnConnectionDeviceSampleConfiguration API has a recommended parameter that uses IKE version 2, DH group 20, SHA-384 integrity and AES-GCM-256 encryption.
  scope: per customer gateway configuration; fixed.
  link: [IKE version 2, DH group 20, SHA-384 integrity algorithm, and AES-GCM-256 encryption algorithm](../facts/site-to-site-vpn.md#site-to-site-vpn-change-recommended-configuration)
site-to-site-vpn-change-secrets-manager-psk
  claim: On May 27, 2025 Site-to-Site VPN added AWS Secrets Manager for storing a pre-shared key; when stored there, VPN connection API responses redact the key and show the Secrets Manager ARN.
  scope: per VPN connection; fixed.
  link: [AWS Secrets Manager for storing a pre-shared key](../facts/site-to-site-vpn.md#site-to-site-vpn-change-secrets-manager-psk)
site-to-site-vpn-cloudhub-hub-and-spoke-between-sites
  claim: AWS VPN CloudHub lets several Site-to-Site VPN connections give your sites secure communication with each other, not only with the VPC. It uses a hub-and-spoke model that works with or without a VPC, and the design suits multiple branch offices with existing internet connections that want a potentially low-cost hub-and-spoke model for primary or backup connectivity between the sites.
  scope: multiple Site-to-Site VPN connections to one virtual private gateway.
  link: [a simple hub-and-spoke model](../facts/site-to-site-vpn.md#site-to-site-vpn-cloudhub-hub-and-spoke-between-sites)
  link: [communicate with each other](../facts/site-to-site-vpn.md#site-to-site-vpn-cloudhub-hub-and-spoke-between-sites)
site-to-site-vpn-cloudhub-over-internet-existing-connections
  claim: VPN CloudHub is suitable if you have multiple branch offices with existing internet connections and want a convenient, potentially low-cost hub-and-spoke model for primary or backup connectivity between the sites.
  scope: AWS VPN CloudHub.
  link: [multiple branch offices and existing internet connections](../facts/site-to-site-vpn.md#site-to-site-vpn-cloudhub-over-internet-existing-connections)
  link: [potentially low-cost hub-and-spoke model](../facts/site-to-site-vpn.md#site-to-site-vpn-cloudhub-over-internet-existing-connections)
site-to-site-vpn-cloudhub-unique-asn-per-customer-gateway
  claim: For VPN CloudHub you create one virtual private gateway and a dynamically routed VPN connection from each customer gateway. You must use a unique BGP ASN for each customer gateway, and the sites must not have overlapping IP ranges.
  scope: AWS VPN CloudHub.
  link: [Autonomous System Number (ASN) for each customer gateway](../facts/site-to-site-vpn.md#site-to-site-vpn-cloudhub-unique-asn-per-customer-gateway)
  link: [The sites must not have overlapping IP ranges](../facts/site-to-site-vpn.md#site-to-site-vpn-cloudhub-unique-asn-per-customer-gateway)
site-to-site-vpn-cloudwatch-metrics-statistics-15-months
  claim: CloudWatch collects raw VPN data into near real-time metrics for VPN tunnels, and the statistics are recorded for a period of 15 months.
  scope: Site-to-Site VPN CloudWatch metrics; fixed.
  link: [recorded for a period of 15 months](../facts/site-to-site-vpn.md#site-to-site-vpn-cloudwatch-metrics-statistics-15-months)
  link: [readable, near real-time metrics](../facts/site-to-site-vpn.md#site-to-site-vpn-cloudwatch-metrics-statistics-15-months)
site-to-site-vpn-concentrator-aggregate-5-gbps-site-100-mbps
  claim: Site-to-Site VPN Concentrators currently support 5 Gbps aggregate bandwidth, and each site can support a maximum of 100 Mbps; if you need higher bandwidth, reach out to AWS Support.
  scope: per Site-to-Site VPN Concentrator and per site; maximum; adjustable; if you need higher bandwidth, reach out to AWS Support.
  link: [5 Gbps aggregate bandwidth](../facts/site-to-site-vpn.md#site-to-site-vpn-concentrator-aggregate-5-gbps-site-100-mbps)
  link: [a maximum of 100 Mbps](../facts/site-to-site-vpn.md#site-to-site-vpn-concentrator-aggregate-5-gbps-site-100-mbps)
site-to-site-vpn-concentrator-bgp-only-no-static
  claim: Site-to-Site VPN Concentrators support BGP routing only. Static routing is not supported.
  scope: Site-to-Site VPN Concentrator.
  link: [support BGP (Border Gateway Protocol) routing only](../facts/site-to-site-vpn.md#site-to-site-vpn-concentrator-bgp-only-no-static)
  link: [Static routing is not supported](../facts/site-to-site-vpn.md#site-to-site-vpn-concentrator-bgp-only-no-static)
site-to-site-vpn-concept-customer-gateway-is-aws-resource
  claim: A customer gateway is an AWS resource that gives AWS information about your customer gateway device. The customer gateway device is the physical device or software application on your side of the connection.
  scope: AWS Site-to-Site VPN.
  link: [An AWS resource which provides information to AWS](../facts/site-to-site-vpn.md#site-to-site-vpn-concept-customer-gateway-is-aws-resource)
  link: [A physical device or software application](../facts/site-to-site-vpn.md#site-to-site-vpn-concept-customer-gateway-is-aws-resource)
site-to-site-vpn-concept-vpn-tunnel-encrypted-link
  claim: A VPN tunnel is an encrypted link where data can pass from the customer network to or from AWS.
  scope: AWS Site-to-Site VPN.
  link: [An encrypted link where data can pass](../facts/site-to-site-vpn.md#site-to-site-vpn-concept-vpn-tunnel-encrypted-link)
  link: [encrypted link](../facts/site-to-site-vpn.md#site-to-site-vpn-concept-vpn-tunnel-encrypted-link)
site-to-site-vpn-decision-guide-connect-entire-network-to-vpcs
  claim: The AWS networking decision guide says to consider AWS Site-to-Site VPN to securely connect an entire on-premises network to your VPCs.
  scope: AWS networking decision guide.
  link: [connect an entire on-premises network to your VPCs](../facts/site-to-site-vpn.md#site-to-site-vpn-decision-guide-connect-entire-network-to-vpcs)
  link: [an entire on-premises network](../facts/site-to-site-vpn.md#site-to-site-vpn-decision-guide-connect-entire-network-to-vpcs)
site-to-site-vpn-default-vgw-asn-64512
  claim: If you do not choose an ASN for the Amazon side of a virtual private gateway, then after June 30th 2018 Amazon provides an ASN of 64512.
  scope: per virtual private gateway; default; adjustable.
  link: [ASN of 64512](../facts/site-to-site-vpn.md#site-to-site-vpn-default-vgw-asn-64512)
  say: six four five one two
site-to-site-vpn-definition-ipsec-vpc-to-on-premises
  claim: In the AWS guide, a Site-to-Site VPN connection is the connection between your VPC and your own on-premises network, and the service supports IPsec VPN connections.
  scope: AWS Site-to-Site VPN.
  link: [between your VPC and your own on-premises network](../facts/site-to-site-vpn.md#site-to-site-vpn-definition-ipsec-vpc-to-on-premises)
  link: [Internet Protocol security (IPsec) VPN connections](../facts/site-to-site-vpn.md#site-to-site-vpn-definition-ipsec-vpc-to-on-premises)
  say: IPsec VPN connections
site-to-site-vpn-dh-groups-phase1-phase2
  claim: Site-to-Site VPN supports Diffie-Hellman groups 2 and 14-24 in Phase 1, and groups 2, 5 and 14-24 in Phase 2.
  scope: Site-to-Site VPN tunnels.
  link: [Phase 1 DH groups 2, 14-24](../facts/site-to-site-vpn.md#site-to-site-vpn-dh-groups-phase1-phase2)
  link: [Phase 2 DH groups 2, 5, 14-24](../facts/site-to-site-vpn.md#site-to-site-vpn-dh-groups-phase1-phase2)
site-to-site-vpn-dpd-timeout-action-default-stops-ike
  claim: By default, when dead peer detection times out, the IKE session is stopped, the tunnel goes down and the routes are removed. You can set AWS to restart the IKE session, or to take no action.
  scope: DPD timeout action of a tunnel; default; adjustable; after dead peer detection (DPD) timeout occurs.
  link: [the IKE session is stopped](../facts/site-to-site-vpn.md#site-to-site-vpn-dpd-timeout-action-default-stops-ike)
  link: [restart the IKE session when DPD timeout occurs](../facts/site-to-site-vpn.md#site-to-site-vpn-dpd-timeout-action-default-stops-ike)
site-to-site-vpn-dpd-timeout-default-40-seconds
  claim: The dead peer detection (DPD) timeout of a Site-to-Site VPN tunnel is the number of seconds after which a DPD timeout occurs. You can specify 30 or higher, and the default is 40.
  scope: DPD timeout tunnel option; default; adjustable; 30 seconds or higher can be specified.
  link: [Default: 40](../facts/site-to-site-vpn.md#site-to-site-vpn-dpd-timeout-default-40-seconds)
  link: [You can specify 30 or higher](../facts/site-to-site-vpn.md#site-to-site-vpn-dpd-timeout-default-40-seconds)
site-to-site-vpn-dynamic-routing-device-needs-bgp-and-dpd
  claim: A device that supports dynamically routed Site-to-Site VPN connections must be able to establish BGP peering, bind tunnels to logical interfaces (route-based VPN), and use IPsec Dead Peer Detection.
  scope: customer gateway devices for dynamically routed connections.
  link: [Establish Border Gateway Protocol (BGP) peering](../facts/site-to-site-vpn.md#site-to-site-vpn-dynamic-routing-device-needs-bgp-and-dpd)
  link: [Utilize IPsec Dead Peer Detection](../facts/site-to-site-vpn.md#site-to-site-vpn-dynamic-routing-device-needs-bgp-and-dpd)
site-to-site-vpn-ecmp-needs-dynamic-routing-not-static
  claim: On a transit gateway you can use ECMP to get higher VPN bandwidth by aggregating several VPN tunnels. The VPN connection must use dynamic routing; ECMP is not supported with static routing.
  scope: Site-to-Site VPN connections on a transit gateway.
  link: [must be configured for dynamic routing](../facts/site-to-site-vpn.md#site-to-site-vpn-ecmp-needs-dynamic-routing-not-static)
  link: [ECMP is not supported on VPN connections](../facts/site-to-site-vpn.md#site-to-site-vpn-ecmp-needs-dynamic-routing-not-static)
site-to-site-vpn-ecmp-not-on-vgw-supported-on-tgw
  claim: On a virtual private gateway, one tunnel across all VPN connections on the gateway is selected, and ECMP is not supported. ECMP is supported for Site-to-Site VPN connections on a transit gateway.
  scope: virtual private gateway versus transit gateway.
  link: [ECMP is not supported for Site-to-Site VPN connections](../facts/site-to-site-vpn.md#site-to-site-vpn-ecmp-not-on-vgw-supported-on-tgw)
  link: [Site-to-Site VPN connections on a transit gateway](../facts/site-to-site-vpn.md#site-to-site-vpn-ecmp-not-on-vgw-supported-on-tgw)
site-to-site-vpn-elc-aws-health-notifications
  claim: With tunnel endpoint lifecycle control enabled, you receive AWS Health notifications for upcoming tunnel endpoint replacements. If you do not apply the update before the Maintenance auto applied after time, AWS replaces the endpoint soon after.
  scope: tunnels with lifecycle control enabled.
  link: [AWS Health notifications for upcoming tunnel endpoint replacements](../facts/site-to-site-vpn.md#site-to-site-vpn-elc-aws-health-notifications)
  link: [AWS will automatically perform the tunnel endpoint replacement](../facts/site-to-site-vpn.md#site-to-site-vpn-elc-aws-health-notifications)
site-to-site-vpn-elc-control-schedule-of-endpoint-replacements
  claim: Tunnel endpoint lifecycle control gives you control over when AWS managed tunnel endpoint replacements happen. Use it if you have short-term business needs or can only support a single tunnel per VPN connection. In rare circumstances AWS might apply critical updates to tunnel endpoints immediately, even with the feature enabled.
  scope: AWS managed tunnel endpoint replacements.
  link: [control over the schedule of endpoint replacements](../facts/site-to-site-vpn.md#site-to-site-vpn-elc-control-schedule-of-endpoint-replacements)
  link: [a time that works best for your business](../facts/site-to-site-vpn.md#site-to-site-vpn-elc-control-schedule-of-endpoint-replacements)
site-to-site-vpn-endpoint-replacement-interrupts-tunnel
  claim: During a tunnel endpoint replacement, connectivity over the tunnel might be interrupted while the new tunnel endpoint is provisioned. Replacement happens when AWS performs tunnel updates or when you modify your VPN connection.
  scope: Site-to-Site VPN tunnel endpoints.
  link: [connectivity over the tunnel might be interrupted](../facts/site-to-site-vpn.md#site-to-site-vpn-endpoint-replacement-interrupts-tunnel)
  link: [when AWS performs tunnel updates](../facts/site-to-site-vpn.md#site-to-site-vpn-endpoint-replacement-interrupts-tunnel)
site-to-site-vpn-endpoint-update-one-tunnel-at-a-time
  claim: AWS applies tunnel endpoint updates to one tunnel of a VPN connection at a time. During an update the connection might briefly lose redundancy, so both tunnels should be configured for high availability.
  scope: AWS managed tunnel endpoint replacements.
  link: [applies tunnel endpoint updates to one tunnel](../facts/site-to-site-vpn.md#site-to-site-vpn-endpoint-update-one-tunnel-at-a-time)
  link: [might experience a brief loss of redundancy](../facts/site-to-site-vpn.md#site-to-site-vpn-endpoint-update-one-tunnel-at-a-time)
site-to-site-vpn-faq-accelerated-convert-by-recreate
  claim: To convert an existing Site-to-Site VPN to an Accelerated one you create a new accelerated VPN, point your customer gateway device at it, and delete the old connection; you get new tunnel endpoint IP addresses because accelerated VPNs use separate IP address ranges.
  scope: existing Site-to-Site VPN connection.
  link: [Create a new Accelerated Site-to-Site VPN](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-accelerated-convert-by-recreate)
  say: create a new accelerated VPN and delete the old one
site-to-site-vpn-faq-accelerated-enable-option
  claim: You create an Accelerated Site-to-Site VPN by setting the option Enable Acceleration to true when you create the VPN connection.
  scope: accelerated Site-to-Site VPN; set when creating the VPN connection.
  link: [Enable Acceleration](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-accelerated-enable-option)
  say: turn on the Enable Acceleration option
site-to-site-vpn-faq-accelerated-nat-t-required
  claim: NAT-T is required and enabled by default for Accelerated Site-to-Site VPN connections.
  scope: per accelerated VPN connection; default.
  link: [NAT-T is required and is enabled by default](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-accelerated-nat-t-required)
  say: NAT-T is required and on by default
site-to-site-vpn-faq-accelerated-not-in-global-accelerator
  claim: Accelerated Site-to-Site VPN can only be created through AWS Site-to-Site VPN, and it cannot be created through the AWS Global Accelerator console or API.
  scope: accelerated Site-to-Site VPN.
  link: [cannot be created through the AWS Global Accelerator](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-accelerated-not-in-global-accelerator)
site-to-site-vpn-faq-accelerated-not-over-public-vif
  claim: Accelerated Site-to-Site VPN over public Direct Connect virtual interfaces is not available; in most cases it would give no acceleration benefit there.
  scope: accelerated Site-to-Site VPN; public Direct Connect virtual interface.
  link: [public Direct Connect virtual interfaces is not available](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-accelerated-not-over-public-vif)
site-to-site-vpn-faq-accelerated-same-protocols
  claim: NAT-T is required and enabled by default for accelerated Site-to-Site VPN connections; apart from that, accelerated and non-accelerated VPN tunnels support the same IPsec and IKE protocols and offer the same bandwidth, tunnel options, routing options, and authentication types.
  scope: accelerated Site-to-Site VPN.
  link: [offer the same bandwidth, tunnel options, routing options](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-accelerated-same-protocols)
  say: same bandwidth, options and routing as a normal VPN
site-to-site-vpn-faq-accelerated-transit-gateway-only
  claim: Only a transit gateway supports Accelerated Site-to-Site VPN, so you specify a transit gateway when you create the VPN connection; the AWS-side VPN endpoint is created on the transit gateway.
  scope: per accelerated VPN connection.
  link: [Only Transit Gateway supports Accelerated Site-to-Site VPN](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-accelerated-transit-gateway-only)
  say: only a transit gateway supports accelerated VPN
site-to-site-vpn-faq-accelerated-two-tunnels
  claim: Each Accelerated Site-to-Site VPN connection offers two tunnels for high availability.
  scope: per VPN connection.
  link: [two tunnels for high availability](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-accelerated-two-tunnels)
  say: two tunnels
site-to-site-vpn-faq-advertised-routes-to-cgw-max
  claim: A Site-to-Site VPN connection advertises a maximum of 1,000 routes to the customer gateway device.
  scope: per VPN connection, AWS to customer gateway device; maximum; not adjustable.
  link: [a maximum of 1,000 routes](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-advertised-routes-to-cgw-max)
  say: up to one thousand routes
site-to-site-vpn-faq-bgp-resets-over-route-max
  claim: For a VPN connection with BGP, the BGP session resets if the customer gateway attempts to advertise more than the maximum number of routes for the gateway type.
  scope: per VPN connection with BGP; more routes advertised than the maximum for the gateway type.
  link: [the BGP session will reset](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-bgp-resets-over-route-max)
  say: the BGP session resets
site-to-site-vpn-faq-cgw-ike-initiator-default
  claim: By default the customer gateway must initiate the IKE session; the AWS VPN endpoints can initiate it if you enable the appropriate options.
  scope: per VPN tunnel; default; adjustable; the AWS VPN endpoints can initiate when the appropriate options are enabled.
  link: [your Customer Gateway (CGW) must initiate IKE](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-cgw-ike-initiator-default)
  say: the customer gateway starts IKE
site-to-site-vpn-faq-ipv6-on-transit-gateway
  claim: VPN connections to an AWS Transit Gateway can carry either IPv4 or IPv6 traffic, selected when you create the connection; the tunnel endpoint and customer gateway IP addresses are IPv4 only.
  scope: VPN connections to an AWS Transit Gateway; select IPv6 with the tunnel option Inside IP Version.
  link: [IPv4 only](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-ipv6-on-transit-gateway)
  say: tunnel endpoint and customer gateway addresses stay IPv4
site-to-site-vpn-faq-logs-enable-interrupts-tunnel
  claim: Enabling Site-to-Site VPN logs on an existing connection through the modify tunnel options interrupts connectivity over the tunnel for up to several minutes; enable logging one tunnel at a time so only the modified tunnel is impacted.
  scope: per tunnel; logs enabled on an existing connection with the modify tunnel options.
  link: [interrupted for up to several minutes](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-logs-enable-interrupts-tunnel)
  say: the tunnel is interrupted for a few minutes
site-to-site-vpn-faq-private-ip-bandwidth
  claim: Like regular Site-to-Site VPN connections, each private IP VPN connection supports 1.25Gbps and 5Gbps of bandwidth, and ECMP across multiple private IP VPN connections of both types increases effective bandwidth.
  scope: per private IP VPN connection.
  link: [1.25Gbps](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-private-ip-bandwidth)
  link: [5Gbps](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-private-ip-bandwidth)
site-to-site-vpn-faq-private-ip-bgp-recommended
  claim: AWS recommends BGP-capable devices when available, because BGP offers robust liveness detection checks that can assist failover to the second VPN tunnel if the first tunnel goes down.
  scope: private IP Site-to-Site VPN routing; customer gateway device supports BGP.
  link: [robust liveness detection checks](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-private-ip-bgp-recommended)
  say: BGP detects a dead tunnel and helps fail over to the second one
site-to-site-vpn-faq-private-ip-mtu
  claim: Private IP VPN connections support 1500 bytes of MTU.
  scope: per private IP VPN connection; maximum; not adjustable.
  link: [1500 bytes of MTU](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-private-ip-mtu)
  say: fifteen hundred bytes
site-to-site-vpn-faq-private-ip-over-dx-transit-vif
  claim: The Private IP Site-to-Site VPN feature lets you deploy VPN connections to an AWS Transit Gateway using private IP addresses, and it works over an AWS Direct Connect transit virtual interface.
  scope: private IP Site-to-Site VPN.
  link: [an AWS Direct Connect transit virtual interface](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-private-ip-over-dx-transit-vif)
site-to-site-vpn-faq-routes-from-cgw-max
  claim: You can advertise a maximum of 100 routes from the customer gateway device to a Site-to-Site VPN connection on a virtual private gateway, or a maximum of 1000 routes to a connection on an AWS Transit Gateway.
  scope: per VPN connection, customer gateway device to AWS; depends on the gateway type; maximum; not adjustable; 100 for a virtual private gateway, 1000 for an AWS Transit Gateway.
  link: [a maximum of 100 routes](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-routes-from-cgw-max)
  link: [a maximum of 1000 routes](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-routes-from-cgw-max)
  say: up to one hundred routes on a virtual private gateway | up to one thousand routes on a transit gateway
site-to-site-vpn-faq-static-routes-max
  claim: For a VPN connection with static routes, you cannot add more than 100 static routes.
  scope: per VPN connection with static routes; maximum; not adjustable.
  link: [more than 100 static routes](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-static-routes-max)
  say: no more than one hundred static routes
site-to-site-vpn-faq-tgw-for-higher-throughput
  claim: To connect to multiple VPCs and achieve higher throughput limits than a virtual private gateway gives, the VPN FAQ says to use AWS Transit Gateway.
  scope: Site-to-Site VPN throughput.
  link: [use AWS Transit Gateway](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-tgw-for-higher-throughput)
  say: use AWS Transit Gateway
site-to-site-vpn-faq-throughput-factors
  claim: VPN connection throughput can depend on the customer gateway capability, the capacity of your connection, average packet size, the protocol, TCP versus UDP, and the network latency between the customer gateway and the virtual private gateway.
  scope: Site-to-Site VPN connection throughput.
  link: [the capability of your customer gateway](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-throughput-factors)
  say: the capability of your customer gateway
site-to-site-vpn-faq-tunnel-max-pps
  claim: Each Site-to-Site VPN connection has two tunnels, and a standard VPN tunnel supports up to 140,000 packets per second (the VPN FAQ states this value for each tunnel; the quotas page gives it for a standard tunnel).
  scope: packets per second per standard VPN tunnel; a connection has two tunnels; maximum; not adjustable.
  link: [up to 140,000](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-tunnel-max-pps)
  say: up to one hundred forty thousand packets per second
site-to-site-vpn-faq-tunnel-max-throughput
  claim: Each Site-to-Site VPN connection has two tunnels, and a standard VPN tunnel supports up to 1.25 Gbps (the VPN FAQ states this value for each tunnel; the quotas page gives it for a standard tunnel). For a connection to a virtual private gateway, aggregated throughput limits apply.
  scope: bandwidth per standard VPN tunnel; a connection has two tunnels; maximum; not adjustable; connection to a virtual private gateway: aggregated throughput limits apply.
  link: [1.25 Gbps](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-tunnel-max-throughput)
  say: one point two five gigabits per second
site-to-site-vpn-faq-vgw-aggregate-throughput
  claim: Multiple VPN connections to the same virtual private gateway are bound by an aggregate throughput limit from AWS to on-premises of up to 1.25 Gbps; for Direct Connect on a virtual private gateway, the throughput is bound by the Direct Connect physical port.
  scope: per virtual private gateway, all VPN connections together, AWS to on-premises; maximum; not adjustable; VPN connections to a virtual private gateway.
  link: [up to 1.25 Gbps](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-vgw-aggregate-throughput)
  say: up to one point two five gigabits per second
site-to-site-vpn-faq-vgw-asn-immutable-after-creation
  claim: You cannot modify the Amazon side ASN of a virtual private gateway after creation; you delete the virtual gateway and recreate it with the desired ASN.
  scope: per virtual private gateway.
  link: [cannot modify the Amazon side ASN after creation](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-vgw-asn-immutable-after-creation)
site-to-site-vpn-faq-vgw-asn-private-range
  claim: You can choose any private ASN for the Amazon side of the BGP session: 16-bit private ASNs from 64512 to 65534, or 32-bit ASNs between 4200000000 and 4294967294.
  scope: per virtual private gateway; private ASNs only.
  link: [64512 to 65534](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-vgw-asn-private-range)
  link: [between 4200000000 and 4294967294](../facts/site-to-site-vpn.md#site-to-site-vpn-faq-vgw-asn-private-range)
site-to-site-vpn-hybrid-dns-route-53-resolver-forwards-to-on-premises
  claim: You can configure Route 53 Resolver to forward queries to customer-managed authoritative DNS servers hosted on premises, and to respond to DNS queries that your on-premises DNS servers forward to your VPC.
  scope: hybrid DNS between a VPC and on-premises.
  link: [customer-managed authoritative DNS servers hosted on-premises](../facts/site-to-site-vpn.md#site-to-site-vpn-hybrid-dns-route-53-resolver-forwards-to-on-premises)
  link: [DNS queries that your on-premises DNS servers forward](../facts/site-to-site-vpn.md#site-to-site-vpn-hybrid-dns-route-53-resolver-forwards-to-on-premises)
site-to-site-vpn-ipsec-aes-sha-dh-pfs
  claim: Traffic in each tunnel can be encrypted with AES128 or AES256 and uses Diffie-Hellman groups for key exchange, which provides Perfect Forward Secrecy. AWS authenticates with SHA1 or SHA2 hashing functions.
  scope: each Site-to-Site VPN tunnel.
  link: [encrypted with AES128 or AES256](../facts/site-to-site-vpn.md#site-to-site-vpn-ipsec-aes-sha-dh-pfs)
  link: [SHA1 or SHA2 hashing functions](../facts/site-to-site-vpn.md#site-to-site-vpn-ipsec-aes-sha-dh-pfs)
  link: [Perfect Forward Secrecy](../facts/site-to-site-vpn.md#site-to-site-vpn-ipsec-aes-sha-dh-pfs)
  say: AES 128-bit or AES 256-bit encryption
site-to-site-vpn-ipv4-inside-tunnel-by-default
  claim: By default, a Site-to-Site VPN connection supports IPv4 traffic inside the VPN tunnels. You can configure a new connection on a transit gateway to support IPv6 traffic inside the tunnels instead.
  scope: Site-to-Site VPN connection on a transit gateway; default; adjustable; IPv6 inside the tunnels needs a new connection.
  link: [supports IPv4 traffic inside the VPN tunnels](../facts/site-to-site-vpn.md#site-to-site-vpn-ipv4-inside-tunnel-by-default)
  link: [support IPv6 traffic inside the VPN tunnels](../facts/site-to-site-vpn.md#site-to-site-vpn-ipv4-inside-tunnel-by-default)
site-to-site-vpn-ipv6-not-on-virtual-private-gateway
  claim: IPv6 traffic is not supported for VPN connections on a virtual private gateway. IPv6 for outer tunnel IPs is supported only on Transit Gateway and Cloud WAN.
  scope: Site-to-Site VPN target gateways.
  link: [VPN connections on a virtual private gateway](../facts/site-to-site-vpn.md#site-to-site-vpn-ipv6-not-on-virtual-private-gateway)
  link: [only supported on Transit Gateway and Cloud WAN](../facts/site-to-site-vpn.md#site-to-site-vpn-ipv6-not-on-virtual-private-gateway)
site-to-site-vpn-ipv6-one-ip-version-per-connection-no-convert
  claim: A single VPN connection cannot carry both IPv4 and IPv6 traffic; you need separate connections. You also cannot enable IPv6 on an existing connection; you must delete it and create a new one.
  scope: Site-to-Site VPN connection.
  link: [cannot support both IPv4 and IPv6 traffic simultaneously](../facts/site-to-site-vpn.md#site-to-site-vpn-ipv6-one-ip-version-per-connection-no-convert)
  link: [You cannot modify an existing IPv4 VPN connection](../facts/site-to-site-vpn.md#site-to-site-vpn-ipv6-one-ip-version-per-connection-no-convert)
site-to-site-vpn-limit-accelerated-unassociated-count-toward-total
  claim: Both accelerated and unassociated connections count towards the total Site-to-Site VPN connections per Region quota.
  scope: Site-to-Site VPN connections per Region quota.
  link: [count towards the total Site-to-Site VPN connections](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-accelerated-unassociated-count-toward-total)
site-to-site-vpn-limit-bandwidth-concentrator-tunnel
  claim: A Site-to-Site VPN Concentrator VPN tunnel supports a maximum bandwidth of up to 100 Mbps; this quota cannot be increased.
  scope: per VPN Concentrator VPN tunnel; maximum; not adjustable.
  link: [up to 100 Mbps](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-bandwidth-concentrator-tunnel)
  say: up to one hundred megabits per second
site-to-site-vpn-limit-bandwidth-large-tunnel
  claim: A large bandwidth Site-to-Site VPN tunnel supports a maximum bandwidth of up to 5 Gbps; this quota cannot be increased. Before large bandwidth tunnels, the limit was 1.25 Gbps per tunnel.
  scope: per large bandwidth VPN tunnel; maximum; not adjustable.
  link: [up to 5 Gbps](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-bandwidth-large-tunnel)
  link: [1.25 Gbps](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-bandwidth-large-tunnel)
  say: up to five gigabits per second | one point two five gigabits per second
  changed: 2025-11-12: was 1.25 Gbps
site-to-site-vpn-limit-bandwidth-standard-tunnel
  claim: A standard Site-to-Site VPN tunnel supports a maximum bandwidth of up to 1.25 Gbps; this quota cannot be increased.
  scope: per standard VPN tunnel; maximum; not adjustable.
  link: [up to 1.25 Gbps](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-bandwidth-standard-tunnel)
  say: up to one point two five gigabits per second
site-to-site-vpn-limit-concentrator-routes-per-site
  claim: Each site connecting to a Site-to-Site VPN Concentrator can send a maximum of 5,000 routes from the transit gateway to a customer gateway and 1,000 routes from the customer gateway to the transit gateway.
  scope: per site connected to a VPN Concentrator; maximum; not adjustable.
  link: [5,000 routes](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-concentrator-routes-per-site)
  link: [1,000 routes](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-concentrator-routes-per-site)
  say: five thousand routes | one thousand routes
site-to-site-vpn-limit-ecmp-20-gbps-example
  claim: For more than 5 Gbps per tunnel, use ECMP across multiple VPN connections; for example, two connections with Large Bandwidth Tunnels and ECMP across all four tunnels reach 20 Gbps.
  scope: across multiple VPN connections; two connections with Large Bandwidth Tunnels, ECMP across four tunnels.
  link: [20 Gbps](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-ecmp-20-gbps-example)
  say: twenty gigabits per second
site-to-site-vpn-limit-ipv6-same-as-ipv4
  claim: IPv6 VPNs support the same throughput (Gbps and PPS), MTU and route limits as IPv4 VPNs, with no performance difference between IPv4 and IPv6 VPN connections.
  scope: per VPN connection.
  link: [same throughput (Gbps and PPS)](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-ipv6-same-as-ipv4)
site-to-site-vpn-limit-mtu-mss
  claim: Site-to-Site VPN supports a maximum transmission unit (MTU) of 1446 bytes and a corresponding maximum segment size (MSS) of 1406 bytes.
  scope: per VPN connection; maximum; not adjustable.
  link: [1446 bytes](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-mtu-mss)
  link: [1406 bytes](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-mtu-mss)
  say: fourteen forty-six bytes | fourteen oh six bytes
site-to-site-vpn-limit-pps-concentrator-tunnel
  claim: A Site-to-Site VPN Concentrator VPN tunnel supports a maximum of up to 10,000 packets per second (PPS); this quota cannot be increased.
  scope: per VPN Concentrator VPN tunnel; maximum; not adjustable.
  link: [up to 10,000](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-pps-concentrator-tunnel)
  say: up to ten thousand
site-to-site-vpn-limit-pps-large-tunnel
  claim: A large bandwidth Site-to-Site VPN tunnel supports a maximum of up to 400,000 packets per second (PPS); this quota cannot be increased.
  scope: per large bandwidth VPN tunnel; maximum; not adjustable.
  link: [up to 400,000](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-pps-large-tunnel)
  say: up to four hundred thousand
site-to-site-vpn-limit-pps-standard-tunnel
  claim: A standard Site-to-Site VPN tunnel supports a maximum of up to 140,000 packets per second (PPS); this quota cannot be increased.
  scope: per standard VPN tunnel; maximum; not adjustable.
  link: [up to 140,000](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-pps-standard-tunnel)
  say: up to one hundred forty thousand
site-to-site-vpn-limit-private-ip-vpn-route-scale
  claim: Private IP VPN connections offer higher route limits (5000 outbound routes and 1000 inbound routes) than Direct Connect alone, which currently has a limit of 200 outbound and 100 inbound routes.
  scope: per private IP VPN connection; maximum; not adjustable.
  link: [5000 outbound routes](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-private-ip-vpn-route-scale)
  link: [1000 inbound routes](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-private-ip-vpn-route-scale)
  link: [200 outbound](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-private-ip-vpn-route-scale)
  link: [100 inbound](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-private-ip-vpn-route-scale)
  say: five thousand outbound routes | one thousand inbound routes | two hundred outbound | one hundred inbound
site-to-site-vpn-limit-routes-cgw-to-tgw-dynamic
  claim: A customer gateway device can advertise at most 1,000 dynamic routes to a Site-to-Site VPN connection on a transit gateway; this quota cannot be increased.
  scope: per Site-to-Site VPN connection on a transit gateway; maximum; not adjustable.
  link: [1,000 dynamic routes](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-routes-cgw-to-tgw-dynamic)
  say: one thousand
site-to-site-vpn-limit-routes-cgw-to-vgw-dynamic
  claim: A customer gateway device can advertise at most 100 dynamic routes to a Site-to-Site VPN connection on a virtual private gateway; this quota cannot be increased.
  scope: per Site-to-Site VPN connection on a virtual private gateway; maximum; not adjustable.
  link: [100 dynamic routes](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-routes-cgw-to-vgw-dynamic)
  say: one hundred
site-to-site-vpn-limit-routes-tgw-to-cgw
  claim: A Site-to-Site VPN connection on a transit gateway can advertise at most 5,000 routes to the customer gateway device; this quota cannot be increased.
  scope: per Site-to-Site VPN connection on a transit gateway; maximum; not adjustable.
  link: [5,000 routes](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-routes-tgw-to-cgw)
  say: five thousand
site-to-site-vpn-limit-routes-vgw-to-cgw
  claim: A Site-to-Site VPN connection on a virtual private gateway can advertise at most 1,000 routes to the customer gateway device; this quota cannot be increased.
  scope: per Site-to-Site VPN connection on a virtual private gateway; maximum; not adjustable.
  link: [1,000 routes](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-routes-vgw-to-cgw)
  say: one thousand
site-to-site-vpn-limit-static-routes-cgw-to-vgw
  claim: A customer gateway device can have at most 100 static routes to a Site-to-Site VPN connection on a virtual private gateway; this quota cannot be increased.
  scope: per Site-to-Site VPN connection on a virtual private gateway; maximum; not adjustable.
  link: [100 static routes](../facts/site-to-site-vpn.md#site-to-site-vpn-limit-static-routes-cgw-to-vgw)
  say: one hundred
site-to-site-vpn-local-route-preferred-over-propagated
  claim: If propagated routes from a Site-to-Site VPN or Direct Connect connection overlap with the local route of the VPC, the local route is the most preferred, even if the propagated routes are more specific.
  scope: VPC route table with propagated routes.
  link: [the local route is most preferred](../facts/site-to-site-vpn.md#site-to-site-vpn-local-route-preferred-over-propagated)
  link: [overlap with the local route for your VPC](../facts/site-to-site-vpn.md#site-to-site-vpn-local-route-preferred-over-propagated)
site-to-site-vpn-logs-tunnel-activity-to-cloudwatch-logs
  claim: Site-to-Site VPN logs give details on IPsec tunnel establishment, IKE negotiations, DPD messages, and BGP status and routing updates, and they can be published to Amazon CloudWatch Logs.
  scope: Site-to-Site VPN logs.
  link: [IP Security (IPsec) tunnel establishment](../facts/site-to-site-vpn.md#site-to-site-vpn-logs-tunnel-activity-to-cloudwatch-logs)
  link: [published to Amazon CloudWatch Logs](../facts/site-to-site-vpn.md#site-to-site-vpn-logs-tunnel-activity-to-cloudwatch-logs)
site-to-site-vpn-longest-prefix-match-most-specific-route
  claim: The VPC uses the most specific route in the route table that matches the traffic to decide how to route it (longest prefix match). Exception: if propagated Site-to-Site VPN or Direct Connect routes overlap with the VPC local route, the local route is most preferred even if the propagated routes are more specific.
  scope: VPC route table.
  link: [the most specific route in your route table](../facts/site-to-site-vpn.md#site-to-site-vpn-longest-prefix-match-most-specific-route)
  link: [(longest prefix match)](../facts/site-to-site-vpn.md#site-to-site-vpn-longest-prefix-match-most-specific-route)
site-to-site-vpn-metric-tunnel-data-in-counted-after-decryption
  claim: The TunnelDataIn metric reports the bytes received on the AWS side of the connection through the VPN tunnel from a customer gateway, and it counts the data after decryption.
  scope: Site-to-Site VPN CloudWatch metric.
  link: [TunnelDataIn](../facts/site-to-site-vpn.md#site-to-site-vpn-metric-tunnel-data-in-counted-after-decryption)
  link: [This metric counts the data after decryption](../facts/site-to-site-vpn.md#site-to-site-vpn-metric-tunnel-data-in-counted-after-decryption)
site-to-site-vpn-metric-tunnel-data-out-counted-before-encryption
  claim: The TunnelDataOut metric reports the bytes sent from the AWS side of the connection through the VPN tunnel to the customer gateway, and it counts the data before encryption.
  scope: Site-to-Site VPN CloudWatch metric.
  link: [TunnelDataOut](../facts/site-to-site-vpn.md#site-to-site-vpn-metric-tunnel-data-out-counted-before-encryption)
  link: [This metric counts the data before encryption](../facts/site-to-site-vpn.md#site-to-site-vpn-metric-tunnel-data-out-counted-before-encryption)
site-to-site-vpn-metric-tunnel-state-values
  claim: The TunnelState CloudWatch metric shows the state of the tunnels: for BGP VPNs 1 means ESTABLISHED and 0 all other states, for static VPNs 0 means DOWN and 1 means UP, and a value between 0 and 1 means at least one tunnel is not UP.
  scope: Site-to-Site VPN CloudWatch metric.
  link: [TunnelState](../facts/site-to-site-vpn.md#site-to-site-vpn-metric-tunnel-state-values)
  link: [values between 0 and 1 indicate at least one tunnel is not UP](../facts/site-to-site-vpn.md#site-to-site-vpn-metric-tunnel-state-values)
site-to-site-vpn-nat-device-needs-idr-identity
  claim: In the rules and limitations for Site-to-Site VPN tunnel initiation options: if the customer gateway device is behind a firewall or other device that uses NAT, it must have an identity (IDr) configured.
  scope: VPN tunnel initiation options (rules and limitations).
  link: [it must have an identity (IDr) configured](../facts/site-to-site-vpn.md#site-to-site-vpn-nat-device-needs-idr-identity)
  link: [behind a firewall or other device](../facts/site-to-site-vpn.md#site-to-site-vpn-nat-device-needs-idr-identity)
site-to-site-vpn-nat-t-udp-4500-if-not-disabled
  claim: If you do not plan to use NAT-T, you must disable it on your device. Otherwise AWS tries to establish the tunnel over UDP port 4500, and the tunnel does not establish if that port is not open.
  scope: NAT traversal on the customer gateway device.
  link: [UDP port 4500](../facts/site-to-site-vpn.md#site-to-site-vpn-nat-t-udp-4500-if-not-disabled)
  link: [the tunnel will not establish](../facts/site-to-site-vpn.md#site-to-site-vpn-nat-t-udp-4500-if-not-disabled)
site-to-site-vpn-options-row-managed-ipsec-over-internet-to-single-vpc
  claim: The connectivity options table lists AWS Site-to-Site VPN as an AWS managed IPsec VPN connection over the internet to an individual VPC, whose limitations include that network latency, variability and availability depend on internet conditions and that you are responsible for redundancy and failover.
  scope: Network-to-Amazon VPC connectivity options table.
  link: [AWS managed IPsec VPN connection over the internet](../facts/site-to-site-vpn.md#site-to-site-vpn-options-row-managed-ipsec-over-internet-to-single-vpc)
  link: [responsible for implementing redundancy and failover](../facts/site-to-site-vpn.md#site-to-site-vpn-options-row-managed-ipsec-over-internet-to-single-vpc)
site-to-site-vpn-policy-based-device-limit-single-sa
  claim: The AWS VPN service is route-based. If a device uses a policy-based solution, you need to limit it to a single security association.
  scope: customer gateway device configuration.
  link: [the service is a route-based solution](../facts/site-to-site-vpn.md#site-to-site-vpn-policy-based-device-limit-single-sa)
  link: [limit to a single SA](../facts/site-to-site-vpn.md#site-to-site-vpn-policy-based-device-limit-single-sa)
site-to-site-vpn-pricing-5gbps-connection-hour
  claim: A Site-to-Site VPN 5Gbps connection is charged for each VPN connection-hour that it is provisioned and available, plus standard AWS data transfer charges for the data transferred via the VPN connection.
  scope: per VPN connection.
  link: [each VPN connection-hour](../facts/site-to-site-vpn.md#site-to-site-vpn-pricing-5gbps-connection-hour)
site-to-site-vpn-pricing-accelerated-extra-charges
  claim: An accelerated Site-to-Site VPN connection pays the normal VPN connection price plus hourly charges for two Global Accelerators per VPN connection and Data Transfer Out Premium (DT-Premium) fees; non-accelerated VPNs have no Global Accelerator charges.
  scope: per accelerated VPN connection.
  link: [two Global Accelerators per VPN connection](../facts/site-to-site-vpn.md#site-to-site-vpn-pricing-accelerated-extra-charges)
  link: [Data Transfer Out Premium (DT-Premium) fees](../facts/site-to-site-vpn.md#site-to-site-vpn-pricing-accelerated-extra-charges)
  link: [not incur any AWS Global Accelerator charges](../facts/site-to-site-vpn.md#site-to-site-vpn-pricing-accelerated-extra-charges)
site-to-site-vpn-pricing-concentrator-hours
  claim: A Site-to-Site VPN Concentrator is charged for each VPN Concentrator-hour that it is provisioned and available, and each VPN connection through the concentrator is also charged per connection-hour.
  scope: per VPN Concentrator.
  link: [each VPN Concentrator-hour](../facts/site-to-site-vpn.md#site-to-site-vpn-pricing-concentrator-hours)
  link: [each VPN connection-hour](../facts/site-to-site-vpn.md#site-to-site-vpn-pricing-concentrator-hours)
site-to-site-vpn-pricing-data-transfer-out-ec2-rates
  claim: Data transfer out on Site-to-Site VPN incurs data transfer out charges that the EC2 on-demand pricing page explains.
  scope: Site-to-Site VPN data transfer out.
  link: [data transfer out charges](../facts/site-to-site-vpn.md#site-to-site-vpn-pricing-data-transfer-out-ec2-rates)
site-to-site-vpn-pricing-logs-no-extra-charge
  claim: There are no additional Site-to-Site VPN service-specific charges for enabling Site-to-Site VPN logs, but you pay standard CloudWatch charges for publishing the logs.
  scope: per VPN connection.
  link: [no additional Site-to-Site VPN service-specific charges](../facts/site-to-site-vpn.md#site-to-site-vpn-pricing-logs-no-extra-charge)
site-to-site-vpn-pricing-transit-gateway-attachment-hourly
  claim: In the AWS pricing examples, a Site-to-Site VPN connection on a transit gateway also pays an hourly fee for the Transit Gateway attachment.
  scope: per transit gateway attachment.
  link: [hourly fee for creating AWS Transit Gateway attachment](../facts/site-to-site-vpn.md#site-to-site-vpn-pricing-transit-gateway-attachment-hourly)
site-to-site-vpn-private-ip-vpn-ipsec-over-dx-no-public-ip
  claim: Private IP VPN lets you deploy IPsec VPN over Direct Connect, which encrypts traffic between your on-premises network and AWS without public IP addresses or additional third-party VPN equipment.
  scope: private IP Site-to-Site VPN.
  link: [deploy IPsec VPN over Direct Connect](../facts/site-to-site-vpn.md#site-to-site-vpn-private-ip-vpn-ipsec-over-dx-no-public-ip)
  link: [without the use of public IP addresses](../facts/site-to-site-vpn.md#site-to-site-vpn-private-ip-vpn-ipsec-over-dx-no-public-ip)
site-to-site-vpn-private-ip-vpn-needs-dx-transit-vif-dx-gateway-tgw
  claim: Private IP Site-to-Site VPN works over a Direct Connect transit virtual interface and uses a Direct Connect gateway and a transit gateway.
  scope: private IP Site-to-Site VPN.
  link: [an Direct Connect transit virtual interface (VIF)](../facts/site-to-site-vpn.md#site-to-site-vpn-private-ip-vpn-needs-dx-transit-vif-dx-gateway-tgw)
  link: [an Direct Connect gateway and a transit gateway](../facts/site-to-site-vpn.md#site-to-site-vpn-private-ip-vpn-needs-dx-transit-vif-dx-gateway-tgw)
site-to-site-vpn-private-ip-vpn-needs-transit-gateway-and-dx-attachment
  claim: You need a transit gateway to deploy private IP VPN connections, and a private IP VPN attachment on the transit gateway requires a Direct Connect attachment for transport.
  scope: private IP Site-to-Site VPN.
  link: [you need a Transit gateway](../facts/site-to-site-vpn.md#site-to-site-vpn-private-ip-vpn-needs-transit-gateway-and-dx-attachment)
  link: [requires a Direct Connect attachment for transport](../facts/site-to-site-vpn.md#site-to-site-vpn-private-ip-vpn-needs-transit-gateway-and-dx-attachment)
site-to-site-vpn-private-ip-vpn-transit-vif-instead-of-public-vif
  claim: Before private IP VPN, encrypting traffic over Direct Connect meant using a public virtual interface, which needs public IP addresses for VPN endpoints. Private IP VPN allows the encryption over a transit virtual interface with private IPs instead.
  scope: encrypting traffic over Direct Connect.
  link: [use a public Direct Connect virtual interface (VIF)](../facts/site-to-site-vpn.md#site-to-site-vpn-private-ip-vpn-transit-vif-instead-of-public-vif)
  link: [over Direct Connect transit VIFs](../facts/site-to-site-vpn.md#site-to-site-vpn-private-ip-vpn-transit-vif-instead-of-public-vif)
site-to-site-vpn-psk-default-authentication
  claim: You can use pre-shared keys or certificates to authenticate Site-to-Site VPN tunnel endpoints. A pre-shared key is the default authentication option for Site-to-Site VPN tunnels. You can specify your own key or let AWS generate one.
  scope: Site-to-Site VPN tunnels; default; adjustable; you can choose a certificate instead.
  link: [the default authentication option](../facts/site-to-site-vpn.md#site-to-site-vpn-psk-default-authentication)
  link: [allow AWS to auto-generate one for you](../facts/site-to-site-vpn.md#site-to-site-vpn-psk-default-authentication)
site-to-site-vpn-psk-store-in-secrets-manager
  claim: You can store pre-shared keys in AWS Secrets Manager rather than directly in the Site-to-Site VPN service.
  scope: pre-shared key storage.
  link: [store pre-shared keys (PSKs) in AWS Secrets Manager](../facts/site-to-site-vpn.md#site-to-site-vpn-psk-store-in-secrets-manager)
  link: [rather than directly in the Site-to-Site VPN service](../facts/site-to-site-vpn.md#site-to-site-vpn-psk-store-in-secrets-manager)
  say: store the pre-shared key in AWS Secrets Manager
site-to-site-vpn-quota-accelerated-connections
  claim: The default quota is 10 accelerated Site-to-Site VPN connections per Region, and you can request an increase.
  scope: per Region, per account; default; adjustable.
  link: [10 accelerated](../facts/site-to-site-vpn.md#site-to-site-vpn-quota-accelerated-connections)
  say: ten
site-to-site-vpn-quota-concentrators-per-region
  claim: The default quota is 50 Site-to-Site VPN Concentrators per Region, and you can request an increase.
  scope: per Region, per account; default; adjustable.
  link: [50 Site-to-Site VPN Concentrators](../facts/site-to-site-vpn.md#site-to-site-vpn-quota-concentrators-per-region)
  say: fifty
site-to-site-vpn-quota-concentrators-per-tgw
  claim: The default quota is 5 Site-to-Site VPN Concentrators per Transit Gateway or Cloud WAN, and you can request an increase.
  scope: per Transit Gateway or Cloud WAN; default; adjustable.
  link: [5 Site-to-Site VPN Concentrators](../facts/site-to-site-vpn.md#site-to-site-vpn-quota-concentrators-per-tgw)
  say: five
site-to-site-vpn-quota-connections-per-region
  claim: The default quota is 50 Site-to-Site VPN connections per Region, and you can request an increase.
  scope: per Region, per account; default; adjustable.
  link: [50 Site-to-Site VPN connections](../facts/site-to-site-vpn.md#site-to-site-vpn-quota-connections-per-region)
  say: fifty
site-to-site-vpn-quota-connections-per-vgw
  claim: The default quota is 10 Site-to-Site VPN connections per virtual private gateway, and you can request an increase.
  scope: per virtual private gateway; default; adjustable.
  link: [10 Site-to-Site VPN connections](../facts/site-to-site-vpn.md#site-to-site-vpn-quota-connections-per-vgw)
  say: ten
site-to-site-vpn-quota-customer-gateways
  claim: The default quota is 50 customer gateways per Region, and you can request an increase.
  scope: per Region, per account; default; adjustable.
  link: [50 customer gateways](../facts/site-to-site-vpn.md#site-to-site-vpn-quota-customer-gateways)
  say: fifty
site-to-site-vpn-quota-large-bandwidth-tunnel-connections
  claim: The default quota is 50 Large Bandwidth Tunnel connections per Region, and you can request an increase.
  scope: per Region, per account; default; adjustable.
  link: [50 Large Bandwidth Tunnel connections](../facts/site-to-site-vpn.md#site-to-site-vpn-quota-large-bandwidth-tunnel-connections)
  say: fifty
site-to-site-vpn-quota-remote-sites-per-concentrator
  claim: The default quota is 100 remote sites per Site-to-Site VPN Concentrator, and you can request an increase.
  scope: per Site-to-Site VPN Concentrator; default; adjustable.
  link: [100 remote sites](../facts/site-to-site-vpn.md#site-to-site-vpn-quota-remote-sites-per-concentrator)
  say: one hundred
site-to-site-vpn-quota-unassociated-connections
  claim: The default quota is 10 unassociated Site-to-Site VPN connections per Region, and you can request an increase.
  scope: per Region, per account; default; adjustable.
  link: [10 unassociated](../facts/site-to-site-vpn.md#site-to-site-vpn-quota-unassociated-connections)
  say: ten
site-to-site-vpn-quota-virtual-private-gateways
  claim: The default quota is 5 virtual private gateways per Region, and you can request an increase.
  scope: per Region, per account; default; adjustable.
  link: [5 virtual private gateways](../facts/site-to-site-vpn.md#site-to-site-vpn-quota-virtual-private-gateways)
  say: five
site-to-site-vpn-redundant-second-vpn-second-cgw-device
  claim: To protect against the loss of the customer gateway device, set up a second Site-to-Site VPN connection to the same virtual private gateway by adding a second customer gateway device. Both devices should advertise the same IP ranges; BGP routing decides the path, and if one device fails the virtual private gateway directs all traffic to the working device.
  scope: Site-to-Site VPN on a virtual private gateway.
  link: [adding a second customer gateway device](../facts/site-to-site-vpn.md#site-to-site-vpn-redundant-second-vpn-second-cgw-device)
  link: [all traffic to the working customer gateway device](../facts/site-to-site-vpn.md#site-to-site-vpn-redundant-second-vpn-second-cgw-device)
site-to-site-vpn-restriction-concentrator-transit-gateway-only
  claim: VPN Concentrators are supported only with Transit Gateway; this feature is not supported with Cloud WAN or a virtual private gateway.
  scope: per VPN Concentrator; fixed.
  link: [only supported with Transit Gateway](../facts/site-to-site-vpn.md#site-to-site-vpn-restriction-concentrator-transit-gateway-only)
site-to-site-vpn-restriction-lbt-gateways
  claim: Large Bandwidth Tunnels are available only for VPN connections attached to a transit gateway or to Cloud WAN; they are not supported for virtual private gateway attachments.
  scope: per VPN connection; fixed.
  link: [a transit gateway or to Cloud WAN](../facts/site-to-site-vpn.md#site-to-site-vpn-restriction-lbt-gateways)
site-to-site-vpn-restriction-lbt-no-accelerated
  claim: In the requirements and limitations of Large Bandwidth Tunnels, accelerated VPN is not supported.
  scope: per VPN connection; fixed.
  link: [Accelerated VPN is not supported](../facts/site-to-site-vpn.md#site-to-site-vpn-restriction-lbt-no-accelerated)
site-to-site-vpn-restriction-lbt-same-bandwidth-both-tunnels
  claim: Both tunnels of a VPN connection must use the same bandwidth configuration: both 1.25 Gbps or both 5 Gbps.
  scope: per VPN connection; fixed.
  link: [both 1.25 Gbps or both 5 Gbps](../facts/site-to-site-vpn.md#site-to-site-vpn-restriction-lbt-same-bandwidth-both-tunnels)
site-to-site-vpn-restriction-no-jumbo-frames
  claim: In the MTU section of the Site-to-Site VPN quotas, jumbo frames are not supported.
  scope: per VPN connection.
  link: [Jumbo frames are not supported](../facts/site-to-site-vpn.md#site-to-site-vpn-restriction-no-jumbo-frames)
site-to-site-vpn-restriction-no-path-mtu-discovery
  claim: A Site-to-Site VPN connection does not support Path MTU Discovery.
  scope: per VPN connection.
  link: [does not support Path MTU Discovery](../facts/site-to-site-vpn.md#site-to-site-vpn-restriction-no-path-mtu-discovery)
site-to-site-vpn-route-priority-dx-bgp-before-vpn-static-before-vpn-bgp
  claim: When the prefixes are the same, a virtual private gateway prefers BGP routes from a Direct Connect connection first, then manually added static routes of a Site-to-Site VPN connection, then BGP routes from a Site-to-Site VPN connection.
  scope: virtual private gateway route selection for identical prefixes.
  link: [BGP propagated routes from an Direct Connect connection](../facts/site-to-site-vpn.md#site-to-site-vpn-route-priority-dx-bgp-before-vpn-static-before-vpn-bgp)
  link: [Manually added static routes](../facts/site-to-site-vpn.md#site-to-site-vpn-route-priority-dx-bgp-before-vpn-static-before-vpn-bgp)
  link: [BGP propagated routes from a Site-to-Site VPN connection](../facts/site-to-site-vpn.md#site-to-site-vpn-route-priority-dx-bgp-before-vpn-static-before-vpn-bgp)
  say: Direct Connect BGP routes come first
site-to-site-vpn-route-priority-shortest-as-path
  claim: For matching prefixes where each Site-to-Site VPN connection uses BGP, the prefix with the shortest AS PATH is preferred.
  scope: Site-to-Site VPN connections that use BGP.
  link: [the shortest AS PATH is preferred](../facts/site-to-site-vpn.md#site-to-site-vpn-route-priority-shortest-as-path)
  link: [the AS PATH is compared](../facts/site-to-site-vpn.md#site-to-site-vpn-route-priority-shortest-as-path)
site-to-site-vpn-routing-bgp-if-device-supports-else-static
  claim: If the customer gateway device supports BGP, specify dynamic routing. If the device does not support BGP, specify static routing.
  scope: Site-to-Site VPN routing type.
  link: [supports Border Gateway Protocol (BGP), specify dynamic routing](../facts/site-to-site-vpn.md#site-to-site-vpn-routing-bgp-if-device-supports-else-static)
  link: [does not support BGP, specify static routing](../facts/site-to-site-vpn.md#site-to-site-vpn-routing-bgp-if-device-supports-else-static)
site-to-site-vpn-sec09-use-ipsec-vpn-for-network-to-network
  claim: The Well-Architected security pillar says to consider an IPsec VPN for securing point-to-point or network-to-network connections, to provide both data privacy and integrity.
  scope: Well-Architected SEC09-BP02 enforce encryption in transit.
  link: [Consider using an IPsec VPN](../facts/site-to-site-vpn.md#site-to-site-vpn-sec09-use-ipsec-vpn-for-network-to-network)
  link: [to help provide both data privacy and integrity](../facts/site-to-site-vpn.md#site-to-site-vpn-sec09-use-ipsec-vpn-for-network-to-network)
site-to-site-vpn-software-vpn-ec2-you-manage-appliance-single-point-of-failure
  claim: A software VPN appliance on Amazon EC2 is recommended if you must manage both ends of the VPN connection, for compliance or for gateway devices that Site-to-Site VPN does not support. You manage the appliance configuration, patches and upgrades, and a single instance is a potential single point of failure.
  scope: software VPN appliance on Amazon EC2.
  link: [manage both ends of the VPN connection](../facts/site-to-site-vpn.md#site-to-site-vpn-software-vpn-ec2-you-manage-appliance-single-point-of-failure)
  link: [you must manage the software appliance](../facts/site-to-site-vpn.md#site-to-site-vpn-software-vpn-ec2-you-manage-appliance-single-point-of-failure)
  link: [a potential single point of failure](../facts/site-to-site-vpn.md#site-to-site-vpn-software-vpn-ec2-you-manage-appliance-single-point-of-failure)
site-to-site-vpn-static-route-beats-propagated-same-cidr
  claim: When a propagated Site-to-Site VPN or Direct Connect route has the same destination CIDR block as an existing static route, the VPC prioritizes the static routes whose targets are an internet gateway, a virtual private gateway, a network interface, an instance ID, a VPC peering connection, a NAT gateway, a transit gateway, or a gateway VPC endpoint.
  scope: VPC route table.
  link: [we prioritize the static routes](../facts/site-to-site-vpn.md#site-to-site-vpn-static-route-beats-propagated-same-cidr)
  link: [the same destination CIDR block](../facts/site-to-site-vpn.md#site-to-site-vpn-static-route-beats-propagated-same-cidr)
site-to-site-vpn-static-routes-device-without-bgp-enter-prefixes
  claim: With a device that does not support BGP advertising, you select static routing and enter the IP prefixes of your network. With a BGP device you do not specify static routes, because the device advertises its routes itself.
  scope: Site-to-Site VPN routing.
  link: [select static routing and enter the routes](../facts/site-to-site-vpn.md#site-to-site-vpn-static-routes-device-without-bgp-enter-prefixes)
  link: [you don't specify static routes](../facts/site-to-site-vpn.md#site-to-site-vpn-static-routes-device-without-bgp-enter-prefixes)
site-to-site-vpn-target-gateway-can-change-vgw-to-tgw
  claim: You can modify the target gateway of a Site-to-Site VPN connection from a virtual private gateway to a transit gateway.
  scope: existing Site-to-Site VPN connections.
  link: [virtual private gateway to a transit gateway](../facts/site-to-site-vpn.md#site-to-site-vpn-target-gateway-can-change-vgw-to-tgw)
  link: [modify the target gateway](../facts/site-to-site-vpn.md#site-to-site-vpn-target-gateway-can-change-vgw-to-tgw)
site-to-site-vpn-target-gateway-generic-term
  claim: Target gateway is a generic term for the VPN endpoint on the Amazon side of the connection; it can be a virtual private gateway or a transit gateway.
  scope: AWS Site-to-Site VPN.
  link: [A generic term for the VPN endpoint](../facts/site-to-site-vpn.md#site-to-site-vpn-target-gateway-generic-term)
  link: [a VPN endpoint for the Amazon side](../facts/site-to-site-vpn.md#site-to-site-vpn-target-gateway-generic-term)
site-to-site-vpn-tgw-ecmp-not-between-different-attachment-types
  claim: ECMP is not supported between different attachment types on a transit gateway; for example you cannot enable ECMP between a VPN and a VPC attachment. Routes are evaluated and traffic goes to the evaluated route instead.
  scope: transit gateway ECMP.
  link: [ECMP is not supported between different attachment types](../facts/site-to-site-vpn.md#site-to-site-vpn-tgw-ecmp-not-between-different-attachment-types)
  link: [ECMP between a VPN and a VPC attachment](../facts/site-to-site-vpn.md#site-to-site-vpn-tgw-ecmp-not-between-different-attachment-types)
site-to-site-vpn-tgw-prefers-dx-gateway-route-over-vpn
  claim: A transit gateway shows only a preferred route. If you advertise the same routes over the Direct Connect gateway and over Site-to-Site VPN, the transit gateway shows only the routes received from the Direct Connect gateway (the preferred route); the VPN route is the backup and appears only when the Direct Connect gateway route is no longer advertised.
  scope: transit gateway route table.
  link: [which is the preferred route](../facts/site-to-site-vpn.md#site-to-site-vpn-tgw-prefers-dx-gateway-route-over-vpn)
  link: [which is the backup route](../facts/site-to-site-vpn.md#site-to-site-vpn-tgw-prefers-dx-gateway-route-over-vpn)
site-to-site-vpn-tgw-vpn-attachment-supports-static-dynamic-ipv4-ipv6
  claim: You can connect a Site-to-Site VPN attachment to a transit gateway to connect your VPCs and on-premises networks. Both dynamic and static routes are supported, as well as IPv4 and IPv6.
  scope: transit gateway VPN attachment.
  link: [a Site-to-Site VPN attachment to a transit gateway](../facts/site-to-site-vpn.md#site-to-site-vpn-tgw-vpn-attachment-supports-static-dynamic-ipv4-ipv6)
  link: [Both dynamic and static routes are supported](../facts/site-to-site-vpn.md#site-to-site-vpn-tgw-vpn-attachment-supports-static-dynamic-ipv4-ipv6)
site-to-site-vpn-tgw-vpn-counts-against-attachment-limit
  claim: Site-to-Site VPN connections on a transit gateway are subject to the total transit gateway attachments limit.
  scope: per transit gateway; maximum.
  link: [subject to the total transit gateway attachments limit](../facts/site-to-site-vpn.md#site-to-site-vpn-tgw-vpn-counts-against-attachment-limit)
  link: [Site-to-Site VPN connections on a transit gateway](../facts/site-to-site-vpn.md#site-to-site-vpn-tgw-vpn-counts-against-attachment-limit)
site-to-site-vpn-tgw-vpn-ecmp-requires-dynamic-routing-whitepaper
  claim: When VPN connections end on a transit gateway, ECMP aggregates multiple VPN tunnels for higher bandwidth, and it requires dynamic routing in the VPN connections; ECMP is not supported with static routing.
  scope: Site-to-Site VPN on a transit gateway.
  link: [configure dynamic routing in the VPN connections](../facts/site-to-site-vpn.md#site-to-site-vpn-tgw-vpn-ecmp-requires-dynamic-routing-whitepaper)
  link: [ECMP is not supported using static routing](../facts/site-to-site-vpn.md#site-to-site-vpn-tgw-vpn-ecmp-requires-dynamic-routing-whitepaper)
site-to-site-vpn-tgw-vpn-many-vpcs-without-multiple-vpn-connections
  claim: Use Transit Gateway with Site-to-Site VPN when you want an AWS-managed VPN endpoint for multiple VPCs in the same Region without the cost and management of multiple IPsec VPN connections to multiple VPCs.
  scope: Site-to-Site VPN on a transit gateway.
  link: [without the additional cost and management](../facts/site-to-site-vpn.md#site-to-site-vpn-tgw-vpn-many-vpcs-without-multiple-vpn-connections)
  link: [an AWS-managed VPN endpoint](../facts/site-to-site-vpn.md#site-to-site-vpn-tgw-vpn-many-vpcs-without-multiple-vpn-connections)
site-to-site-vpn-tunnel-health-precedes-other-routing-attributes
  claim: The health of a tunnel endpoint takes precedence over other routing attributes, for VPNs on virtual private gateways and on transit gateways.
  scope: VPNs on virtual private gateways and transit gateways.
  link: [takes precedence over other routing attributes](../facts/site-to-site-vpn.md#site-to-site-vpn-tunnel-health-precedes-other-routing-attributes)
  link: [VPNs on virtual private gateways and Transit Gateways](../facts/site-to-site-vpn.md#site-to-site-vpn-tunnel-health-precedes-other-routing-attributes)
site-to-site-vpn-two-tunnels-different-availability-zones
  claim: The two tunnels of a Site-to-Site VPN connection end in different Availability Zones. If a device fails inside AWS, the connection fails over to the second tunnel so access is not interrupted.
  scope: per Site-to-Site VPN connection.
  link: [each terminating in a different Availability Zone](../facts/site-to-site-vpn.md#site-to-site-vpn-two-tunnels-different-availability-zones)
  link: [automatically fails over to the second tunnel](../facts/site-to-site-vpn.md#site-to-site-vpn-two-tunnels-different-availability-zones)
  say: each tunnel ends in a different Availability Zone | it fails over to the second tunnel on its own
site-to-site-vpn-two-tunnels-unique-public-ip-configure-both
  claim: Each Site-to-Site VPN connection has two tunnels, each with a unique public IP address. AWS says to configure both tunnels for redundancy; when one is unavailable, traffic is routed automatically to the other.
  scope: per Site-to-Site VPN connection; fixed.
  link: [each tunnel using a unique public IP address](../facts/site-to-site-vpn.md#site-to-site-vpn-two-tunnels-unique-public-ip-configure-both)
  link: [configure both tunnels for redundancy](../facts/site-to-site-vpn.md#site-to-site-vpn-two-tunnels-unique-public-ip-configure-both)
  link: [automatically routed to the available tunnel](../facts/site-to-site-vpn.md#site-to-site-vpn-two-tunnels-unique-public-ip-configure-both)
site-to-site-vpn-use-ikev2-recommended
  claim: AWS strongly recommends IKEv2 for a Site-to-Site VPN connection and says to use IKEv1 only if the customer gateway device does not support IKEv2.
  scope: Site-to-Site VPN connection.
  link: [We strongly recommend using IKEv2](../facts/site-to-site-vpn.md#site-to-site-vpn-use-ikev2-recommended)
  link: [only use IKEv1 if your customer gateway device does not support IKEv2](../facts/site-to-site-vpn.md#site-to-site-vpn-use-ikev2-recommended)
site-to-site-vpn-vgw-amazon-side-asn-default-64512-not-changeable
  claim: If you do not specify an ASN when you create a virtual private gateway, it gets the default ASN 64512. You cannot change the ASN after you create the virtual private gateway.
  scope: virtual private gateway Amazon-side ASN; default; not adjustable.
  link: [default ASN (64512)](../facts/site-to-site-vpn.md#site-to-site-vpn-vgw-amazon-side-asn-default-64512-not-changeable)
  link: [You cannot change the ASN](../facts/site-to-site-vpn.md#site-to-site-vpn-vgw-amazon-side-asn-default-64512-not-changeable)
site-to-site-vpn-vgw-attaches-to-single-vpc
  claim: A virtual private gateway can be attached to a single VPC, and you can attach one virtual private gateway to a VPC at a time. To connect the same Site-to-Site VPN connection to several VPCs, AWS recommends exploring a transit gateway instead.
  scope: per virtual private gateway; maximum; one VPC at a time.
  link: [one virtual private gateway to a VPC](../facts/site-to-site-vpn.md#site-to-site-vpn-vgw-attaches-to-single-vpc)
  link: [explore using a transit gateway instead](../facts/site-to-site-vpn.md#site-to-site-vpn-vgw-attaches-to-single-vpc)
site-to-site-vpn-vgw-regional-terminates-vpn-and-private-vifs
  claim: A virtual private gateway (VGW) is a regional, highly redundant service that provides IP routing and forwarding at the VPC level. It can terminate Site-to-Site VPN connections and Direct Connect private virtual interfaces.
  scope: virtual private gateway.
  link: [a regional, highly redundant service](../facts/site-to-site-vpn.md#site-to-site-vpn-vgw-regional-terminates-vpn-and-private-vifs)
  link: [VGW can terminate AWS S2S VPN connections and AWS Direct Connect Private VIFs](../facts/site-to-site-vpn.md#site-to-site-vpn-vgw-regional-terminates-vpn-and-private-vifs)
site-to-site-vpn-vpc-route-table-route-to-vgw-and-propagation
  claim: In the VPC route table you add a route for the remote network with the virtual private gateway as target. You can also enable route propagation so that network routes are added to the table automatically.
  scope: VPC route table of a VPC with a virtual private gateway.
  link: [specify the virtual private gateway as the target](../facts/site-to-site-vpn.md#site-to-site-vpn-vpc-route-table-route-to-vgw-and-propagation)
  link: [enable route propagation for your route table](../facts/site-to-site-vpn.md#site-to-site-vpn-vpc-route-table-route-to-vgw-and-propagation)
site-to-site-vpn-vpn-over-internet-inconsistent-performance
  claim: A standard VPN connection crosses multiple public networks on the internet before it reaches the AWS VPN endpoint, which can give inconsistent availability and performance.
  scope: VPN connections that are not accelerated.
  link: [traverses through multiple public networks on the internet](../facts/site-to-site-vpn.md#site-to-site-vpn-vpn-over-internet-inconsistent-performance)
  link: [inconsistent availability and performance](../facts/site-to-site-vpn.md#site-to-site-vpn-vpn-over-internet-inconsistent-performance)
