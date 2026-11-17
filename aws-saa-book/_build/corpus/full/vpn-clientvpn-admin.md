# AWS Client VPN Administrator Guide

-----
*****Copyright &copy; Amazon Web Services, Inc. and/or its affiliates. All rights reserved.*****

-----
Amazon's trademarks and trade dress may not be used in
connection with any product or service that is not Amazon's,
in any manner that is likely to cause confusion among customers,
or in any manner that disparages or discredits Amazon. All other
trademarks not owned by Amazon are the property of their respective
owners, who may or may not be affiliated with, connected to, or
sponsored by Amazon.

-----
## Contents
+ [What is AWS Client VPN?](#what-is)
   + [Rules and best practices for using AWS Client VPN](#what-is-best-practices)
+ [How AWS Client VPN works](#how-it-works)
   + [Client authentication in AWS Client VPN](#client-authentication)
      + [Active Directory authentication in Client VPN](#ad)
      + [Mutual authentication in AWS Client VPN](#mutual)
         + [Enable mutual authentication for AWS Client VPN](#client-auth-mutual-enable)
         + [Renew your server certificate for AWS Client VPN](#mutual-renew)
      + [Single sign-on — SAML 2.0-based federated authentication — in Client VPN](#federated-authentication)
         + [Enable SAML for AWS Client VPN](#client-auth-enable-saml)
   + [Client authorization in AWS Client VPN](#client-authorization)
      + [Create an AWS Client VPN endpoint security group rule](#client-auth-rule-create)
   + [Connection authorization in AWS Client VPN](#connection-authorization)
   + [Split-tunnel on AWS Client VPN endpoints](#split-tunnel-vpn)
   + [Connection logging for an AWS Client VPN endpoint](#connection-logging)
   + [Client VPN scaling considerations](#scaling-considerations)
+ [Get started with AWS Client VPN](#cvpn-getting-started)
+ [Work with AWS Client VPN](#cvpn-working)
   + [AWS Client VPN access to the self-service portal](#cvpn-self-service-portal)
   + [AWS Client VPN authorization rules](#cvpn-working-rules)
      + [Add an authorization rule to an AWS Client VPN endpoint](#cvpn-working-rule-authorize-add)
      + [Remove an authorization rule from an AWS Client VPN endpoint](#cvpn-working-rule-remove)
      + [View AWS Client VPN authorization rules](#cvpn-working-rule-view)
   + [AWS Client VPN client certificate revocation lists](#cvpn-working-certificates)
      + [Generate an AWS Client VPN client certificate revocation list](#cvpn-working-certificates-generate)
      + [Import an AWS Client VPN client certificate revocation list](#cvpn-working-certificates-import)
      + [Export an AWS Client VPN client certificate revocation list](#cvpn-working-certificates-export)
   + [AWS Client VPN client connections](#cvpn-working-connections)
      + [View AWS Client VPN client connections](#cvpn-working-connections-view)
      + [Terminate an AWS Client VPN client connection](#cvpn-working-connections-disassociate)
   + [AWS Client VPN client login banners](#cvpn-working-login-banner)
      + [Configure a client login banner for an existing AWS Client VPN endpoint](#configure-login-banner-existing-endpoint)
      + [Deactivate a client login banner for an existing AWS Client VPN endpoint](#disable-login-banner)
      + [Modify existing banner text on a AWS Client VPN endpoint](#modify-banner-text)
      + [View a currently configured AWS Client VPN login banner](#display-login-banner)
   + [AWS Client VPN Client Route Enforcement](#cvpn-working-cre)
      + [Activate Client Route Enforcement for an AWS Client VPN endpoint](#activate-cre)
      + [Deactivate Client Route Enforcement from an AWS Client VPN endpoint](#deactivate-cre)
      + [Troubleshoot IPv6 Client Route Enforcement](#cre-ipv6-troubleshooting)
   + [AWS Client VPN endpoints](#cvpn-working-endpoints)
      + [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create)
      + [View AWS Client VPN endpoints](#cvpn-working-endpoint-view)
      + [Modify an AWS Client VPN endpoint](#cvpn-working-endpoint-modify)
      + [Delete an AWS Client VPN endpoint](#cvpn-working-endpoint-delete)
   + [AWS Client VPN connection logs](#cvpn-working-with-connection-logs)
      + [Enable connection logging for a new AWS Client VPN endpoint](#create-connection-log-new)
      + [Enable connection logging for an existing AWS Client VPN endpoint](#create-connection-log-existing)
      + [View AWS Client VPN connection logs](#view-connection-logs)
      + [Turn off AWS Client VPN connection logging](#disable-connection-logs)
   + [AWS Client VPN endpoint configuration file export](#cvpn-working-endpoint-export)
      + [Export the AWS Client VPN client configuration file](#export-client-config-file)
      + [Add the AWS Client VPN client certificate and key information for mutual authentication](#add-config-file-cert-key)
   + [AWS Client VPN routes](#cvpn-working-routes)
      + [Create an AWS Client VPN endpoint route](#cvpn-working-routes-create)
      + [View AWS Client VPN endpoint routes](#cvpn-working-routes-view)
      + [Delete an AWS Client VPN endpoint route](#cvpn-working-routes-delete)
   + [AWS Client VPN target networks](#cvpn-working-target)
      + [Associate a target network with an AWS Client VPN endpoint](#cvpn-working-target-associate)
      + [Apply a security group to a target network in AWS Client VPN](#cvpn-working-target-apply)
      + [View AWS Client VPN target networks](#cvpn-working-target-view)
      + [Disassociate a target network from an AWS Client VPN endpoint](#cvpn-working-target-disassociate)
   + [AWS Client VPN maximum VPN session duration timeout](#cvpn-working-max-duration)
      + [View AWS Client VPN current maximum VPN session duration](#display-max-duration)
      + [Modify the maximum AWS Client VPN session duration and timeout behavior](#modify-max-timeout)
   + [Transit Gateway integration with Client VPN](#cvpn-tgw)
+ [Device posture for AWS Client VPN](#device-posture)
   + [How device posture works](#device-posture-how-it-works)
   + [Concepts](#device-posture-concepts)
   + [Prerequisites](#device-posture-prerequisites)
   + [Step 1: Configure a device trust provider](#device-posture-step1)
   + [Step 2: Author an authorization policy](#device-posture-step2)
   + [Step 3: Test the policy in shadow mode](#device-posture-step3)
   + [Step 4: Enforce the policy](#device-posture-step4)
   + [Supported device trust providers](#device-posture-providers)
      + [Configuring a trust provider](#device-posture-providers-config)
      + [Trust data reference](#device-posture-providers-trust-data)
         + [CrowdStrike (context.crowdstrike.*)](#device-posture-trust-data-crowdstrike)
         + [Jamf (context.jamf.*)](#device-posture-trust-data-jamf)
         + [JumpCloud (context.jumpcloud.*)](#device-posture-trust-data-jumpcloud)
   + [Authoring device posture authorization policies](#device-posture-policies)
      + [Test policy](#device-posture-policy-assistant)
         + [Step 1: Select filters and test the policy](#device-posture-policy-assistant-step1)
         + [Step 2: Review and save the policy](#device-posture-policy-assistant-step2)
      + [How Client VPN uses Cedar](#device-posture-policies-cedar)
      + [Create or update a policy](#device-posture-policies-create)
      + [View a policy](#device-posture-policies-view)
      + [Delete a policy](#device-posture-policies-delete)
      + [Considerations when writing policies](#device-posture-policies-considerations)
+ [Security in AWS Client VPN](#security)
   + [Data protection in AWS Client VPN](#data-protection)
   + [Identity and access management for AWS Client VPN](#security-iam)
      + [How AWS Client VPN works with IAM](#security_iam_service-with-iam)
      + [Identity-based policy examples for AWS Client VPN](#security_iam_id-based-policy-examples)
      + [Troubleshooting AWS Client VPN identity and access](#security_iam_troubleshoot)
      + [Using service-linked roles for AWS Client VPN](#using-service-linked-roles)
         + [Using roles for AWS Client VPN](#using-service-linked-roles-cvpn-slr)
         + [Using roles for connection authorization in Client VPN;](#using-service-linked-roles-client-connect-handler)
   + [Resilience in AWS Client VPN](#disaster-recovery-resiliency)
   + [Infrastructure security in AWS Client VPN](#infrastructure-security)
   + [Security best practices for AWS Client VPN](#security-best-practices)
   + [IPv6 considerations for AWS Client VPN](#ipv6-considerations)
+ [Monitoring AWS Client VPN](#monitoring-overview)
   + [Amazon CloudWatch metrics for AWS Client VPN](#monitoring-cloudwatch)
      + [View Client VPN endpoint metrics in Amazon CloudWatch](#viewing-metrics)
+ [AWS Client VPN quotas](#limits)
+ [Troubleshooting AWS Client VPN](#troubleshooting)
   + [Troubleshooting AWS Client VPN: Unable to resolve the Client VPN endpoint DNS name](#resolve-host-name)
   + [Troubleshooting AWS Client VPN: Traffic is not being split between subnets](#split-traffic)
   + [Troubleshooting AWS Client VPN: Authorization rules for Active Directory groups not working as expected](#ad-group-auth-rules)
   + [Troubleshooting AWS Client VPN: Clients can't access a peered VPC, Amazon S3, or the internet](#no-internet-access)
   + [Troubleshooting AWS Client VPN: Access to a peered VPC, Amazon S3, or the internet is intermittent](#intermittent-access)
   + [Troubleshooting AWS Client VPN: Client software returns a TLS error when trying to connect to Client VPN](#client-cannot-connect)
   + [Troubleshooting AWS Client VPN: Client software returns user name and password errors — Active Directory authentication](#client-user-name-password-mfa)
   + [Troubleshooting AWS Client VPN: Client software returns user name and password errors — federated authentication](#missing-attribute)
   + [Troubleshooting AWS Client VPN: Clients cannot connect — mutual authentication](#client-cannot-connect-mutual)
   + [Troubleshooting AWS Client VPN: Client returns a credentials exceed max size error in Client VPN — federated authentication](#client-credentials-exceeded)
   + [Troubleshooting AWS Client VPN: Client does not open browser for an endpoint — federated authentication](#client-no-browser)
   + [Troubleshooting AWS Client VPN: Client returns no available ports error — federated authentication](#client-no-port)
   + [Troubleshooting AWS Client VPN: A connection is terminated due to an IP mismatch](#server-ip-mismatch)
   + [Troubleshooting AWS Client VPN: Routing traffic to LAN not working as expected](#routing-to-lan)
   + [Troubleshooting AWS Client VPN: Verify the bandwidth limit for a Client VPN endpoint](#test-throughput)
   + [Troubleshooting AWS Client VPN: Tunnel connectivity issues to a VPC](#VPNTunnelConnectivityTroubleshooting)
+ [Document history for the Client VPN User Guide](#WhatsNew)

-----



# What is AWS Client VPN?
<a name="what-is"></a>

AWS Client VPN is a managed client-based VPN service that enables you to securely access your AWS resources and resources in your on-premises network. With Client VPN, you can access your resources from any location using an OpenVPN-based VPN client.



**Topics**
+ [Features of Client VPN](#what-is-features)
+ [Components of Client VPN](#what-is-components)
+ [Working with Client VPN](#what-is-access)
+ [Pricing for Client VPN](#what-is-pricing)
+ [Rules and best practices](#what-is-best-practices)

## Features of Client VPN
<a name="what-is-features"></a>

Client VPN offers the following features and functionality:
+ **Secure connections** — Establishes encrypted TLS connections from any location through the OpenVPN client, ensuring data privacy and integrity.
+ **Managed service** — Eliminates the operational burden of deploying and maintaining third-party remote access VPN solutions through complete AWS management.
+ **High availability and elasticity** — Dynamically scales to accommodate varying numbers of users connecting to your AWS and on-premises resources without manual intervention.
+ **Authentication** — Supports multiple authentication methods including Active Directory integration, federated authentication, and certificate-based authentication for flexible identity management.
+ **Granular control** — Implements precise security controls through network-based access rules configurable at the Active Directory group level and security group-based access control.
+ **Ease of use** — Provides unified access to both AWS and on-premises resources through a single VPN tunnel, simplifying the end-user experience.
+ **Manageability** — Offers comprehensive visibility through detailed connection logs and real-time management capabilities, including the ability to monitor and terminate active client connections when necessary.
+ **Deep integration** — Seamlessly integrates with existing AWS services, including AWS Directory Service and Amazon VPC, enhancing your cloud infrastructure's connectivity capabilities.
+ **Flexible network architecture** — Supports both VPC subnet associations and direct Transit Gateway attachments. For more information, see [Transit Gateway integration with Client VPN](#cvpn-tgw).
+ **IPv6 support** — Enables full IPv6 connectivity for Client VPN endpoints, supporting connections to IPv6 resources in your VPCs and from clients on IPv6 networks for modern networking requirements.
+ **Device posture** — You can grant access based on the health of the connecting device in addition to the identity of the user. Client VPN integrates with device trust providers (CrowdStrike, Jamf, and JumpCloud) and evaluates an authorization policy against each device's posture token when it connects and every 5 minutes throughout the session. For more information, see [Device posture for AWS Client VPN](#device-posture).

## Components of Client VPN
<a name="what-is-components"></a>

The following are the key concepts for Client VPN:

**Client VPN endpoint**  
The Client VPN endpoint is the resource that you create and configure to enable and manage client VPN sessions. It's the termination point for all client VPN sessions.

**Target network**  
A target network is the network that you associate with a Client VPN endpoint. You can associate VPC subnets or attach directly to an AWS Transit Gateway. For more information about Transit Gateway integration, see [Transit Gateway integration with Client VPN](#cvpn-tgw).

**Route**  
Each Client VPN endpoint has a route table that describes the available destination network routes. Each route in the route table specifies the path for traffic to specific resources or networks.

**Authorization rules**  
An authorization rule restricts the users who can access a network. For a specified network, you configure the Active Directory or identity provider (IdP) group that is allowed access. Only users belonging to this group can access the specified network. By default, there are no authorization rules and you must configure authorization rules to enable users to access resources and networks. 

**Authorization policy**  
An authorization policy defines the requirements that a connection must meet, written in the Cedar policy language. Client VPN evaluates the policy when a device connects and on each re-evaluation during the session.

**Client**  
The end user connecting to the Client VPN endpoint to establish a VPN session. End users need to download an OpenVPN client and use the Client VPN configuration file that you created to establish a VPN session.

**Client CIDR range**  
An IP address range from which to assign client IP addresses. Each connection to the Client VPN endpoint is assigned a unique IP address from the client CIDR range. For IPv4 traffic, you choose the client CIDR range, for example, `10.2.0.0/16`. For IPv6 traffic, AWS Client VPN automatically assigns the client CIDR range.

**Client VPN ports**  
AWS Client VPN supports ports 443 and 1194 for both TCP and UDP. The default is port 443.

**Client VPN network interfaces**  
When you associate a subnet with your Client VPN endpoint, we create Client VPN network interfaces in that subnet. Traffic that's sent to the VPC from the Client VPN endpoint is sent through a Client VPN network interface. For IPv4 traffic, source network address translation (SNAT) is applied, where the source IP address from the client CIDR range is translated to the Client VPN network interface IP address. For IPv6 traffic, SNAT is not applied, providing enhanced visibility into the connected user's IP address.

**Connection logging**  
You can enable connection logging for your Client VPN endpoint to log connection events. You can use this information to run forensics, analyze how your Client VPN endpoint is being used, or debug connection issues.

**Self-service portal**  
Client VPN provides a self-service portal as a web page to end users to download the latest version of the AWS VPN Desktop Client and the latest version of the Client VPN endpoint configuration file, which contains the settings required to connect to their endpoint. The Client VPN endpoint administrator can enable or disable the self-service portal for the Client VPN endpoint. Self-service portal is a Global service backed by service stacks in the following Regions: US East (N. Virginia), Asia Pacific (Tokyo), Europe (Ireland), and AWS GovCloud (US-West).

**Endpoint IP address type**  
The IP address type for the Client VPN endpoint, which can be IPv4, IPv6, or dual-stack (both IPv4 and IPv6). 

**Traffic IP address type**  
The IP address type for traffic flowing through the Client VPN endpoint, which can be IPv4, IPv6, or dual-stack (both IPv4 and IPv6). This determines the type of inner traffic (the actual payload or original traffic that is tunneled through the VPN connection), client CIDR ranges, subnet association, routes, and rules per endpoint.

## Working with Client VPN
<a name="what-is-access"></a>

You can work with Client VPN in any of the following ways:

**AWS Management Console**  
The console provides a web-based user interface for Client VPN.   
The console provides a web-based user interface for Client VPN with two setup methods:   
+ Quickstart setup: Streamlined endpoint creation with AWS-recommended defaults
+ Standard setup: Full control over all configuration options
 If you've signed up for an AWS account, you can sign into the [Amazon VPC](https://console.aws.amazon.com/vpc/) console and select Client VPN in the navigation pane.

**AWS Command Line Interface (AWS CLI)**  
The AWS CLI provides direct access to the Client VPN public APIs. It is supported on Windows, macOS, and Linux. For more information about getting started with the AWS CLI, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/). For more information about the commands for Client VPN, see the [EC2 section](https://docs.aws.amazon.com/cli/latest/reference/ec2/) of the *Amazon EC2 Command Line Reference*.

**AWS Tools for Windows PowerShell**  
AWS provides commands for a broad set of AWS offerings for those who script in the PowerShell environment. For more information about getting started with the AWS Tools for Windows PowerShell, see the [AWS Tools for Windows PowerShell User Guide](https://docs.aws.amazon.com/powershell/latest/userguide/). For more information about the cmdlets for Client VPN, see the [AWS Tools for Windows PowerShell Cmdlet Reference](https://docs.aws.amazon.com/powershell/latest/reference/).

**Query API**  
The Client VPN HTTPS Query API gives you programmatic access to Client VPN and AWS. The HTTPS Query API lets you issue HTTPS requests directly to the service. When you use the HTTPS API, you must include code to digitally sign requests using your credentials. For more information, see the [AWS Client VPN actions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-cvpn.html).

## Pricing for Client VPN
<a name="what-is-pricing"></a>

You are charged for each endpoint association and each VPN connection on an hourly basis. There is no additional cost for using IPv6 or dual-stack endpoints; they are charged at the same rate as IPv4 endpoints. For more information, see [AWS Client VPN pricing](https://aws.amazon.com/vpn/pricing/#AWS_Client_VPN_pricing).

You are charged for data transfer out from Amazon EC2 to the internet. For more information, see [Data Transfer](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer) on the Amazon EC2 On-Demand Pricing age.

If you enable connection logging for your Client VPN endpoint, you must create a CloudWatch Logs log group in your account. Charges apply for using log groups. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/) (under **Paid tier**, choose **Logs**).

If you enable the client connect handler for your Client VPN endpoint, you must create and invoke a Lambda function. Charges apply for invoking Lambda functions. For more information, see [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/).

Client VPN endpoints are associated with a target network, which is a subnet in a VPC. If this VPC has an Internet Gateway, we associate Elastic IP addresses with the Client VPN elastic network interfaces (ENIs). These Elastic IP addresses are charged as in-use public IPv4 addresses. For more information, see the Public IPv4 Address tab on the [VPC pricing page](https://aws.amazon.com/vpc/pricing/). 

**Note**  
Client VPN endpoints require Elastic IP addresses when associated with a VPC subnet that has an Internet Gateway because these EIPs enable direct internet connectivity for VPN clients. When connecting through a Client VPN endpoint, they need a public IP address to communicate with internet resources. Elastic IPs serve this purpose by providing a consistent, public-facing endpoint. These EIPs are attached to the Client VPN elastic network interfaces (ENIs) and are essential for maintaining stable, secure internet access for VPN clients while ensuring proper routing of traffic. Since these Elastic IP addresses are allocated and actively used for the Client VPN service, AWS charges them as in-use public IPv4 addresses, following their standard pricing model for allocated and associated EIPs.

## Rules and best practices for using AWS Client VPN
<a name="what-is-best-practices"></a>

The following sections describe the rules and best practices for using AWS Client VPN:

**Topics**
+ [Networking and bandwidth requirements](#bp-nw)
+ [Subnet and VPC configuration](#bp-subnet)
+ [Authentication and security](#bp-auth)
+ [Connection and DNS requirements](#bp-dns)
+ [Limitations and restrictions](#bp-limits)

### Networking and bandwidth requirements
<a name="bp-nw"></a>
+ AWS Client VPN is a fully-managed service that automatically scales to accommodate additional user connections and bandwidth requirements. Each user connection has a maximum baseline bandwidth of 50 Mbps. 

  The actual bandwidth you experience connecting through a Client VPN endpoint can vary based on several factors. These factors include packet size, traffic composition (TCP/UDP mix), network policies (shaping or throttling) on intermediate networks, internet conditions, application-specific requirements, and the total number of concurrent user connections. If you are hitting the maximum bandwidth limit, you can request an increase through AWS Support. 
+ Client CIDR ranges cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or any routes manually added to the Client VPN endpoint's route table.
+ Client CIDR ranges must have a block size of at least /22 and must not be greater than /12.
+ A portion of the addresses in the client CIDR range are used to support the availability model of the Client VPN endpoint, and cannot be assigned to clients. Therefore, we recommend that you assign a CIDR block that contains twice the number of IP addresses that are required to enable the maximum number of concurrent connections that you plan to support on the Client VPN endpoint.
+ The client CIDR range cannot be changed after you create the Client VPN endpoint.
+ Client VPN supports IPv4, IPv6, and dual-stack (both IPv4 and IPv6) traffic. For more details on IPv6 support, see [IPv6 considerations for AWS Client VPN](#ipv6-considerations).
+ Client VPN performs Port Address Translation (PAT) only when concurrent users are connecting to the same target. Port translation is automatic and necessary to support multiple simultaneous connections through the same VPN endpoint.
  + For the source IP translation the source IP address is translated to the Client VPN's IP address.
  + For the source port translation for single client connections, the original source port number might remain unchanged.
  + For the source port translation for multiple clients connecting to the same destination (the same target IP address and port), Client VPN performs port translation to ensure unique connections.

  For example, when two clients, client 1 and client 2, connect to the same destination server and port through a Client VPN endpoint:
  + The original port for client 1 — for example, `9999` — might be translated to a different port — for example, port `4306`.
  + The original port for client 2 — for example, `9999` — might be translated to a unique port different form client 1 — for example, port `63922`.
+ For IPv6 traffic, Client VPN does not perform Network Address Translation (NAT). This provides enhanced visibility into the connected user's IPv6 address.

### Subnet and VPC configuration
<a name="bp-subnet"></a>
+ The subnets associated with a Client VPN endpoint must be in the same VPC.
+ You cannot associate multiple subnets from the same Availability Zone with a Client VPN endpoint.
+ A Client VPN endpoint does not support subnet associations in a dedicated tenancy VPC.
+ For IPv6 or dual-stack traffic, the associated subnets must have IPv6 or dual-stack CIDR ranges.
+ For dual-stack endpoints, you cannot associate more than one subnet per Availability Zone.

### Authentication and security
<a name="bp-auth"></a>
+ The self-service portal is not available for clients that authenticate using mutual authentication.
+ If multi-factor authentication (MFA) is disabled for your Active Directory, user passwords cannot use the following format.

  ```
  SCRV1:{{base64_encoded_string}}:{{base64_encoded_string}}
  ```
+ Certificates used in AWS Client VPN must adhere to [RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](https://datatracker.ietf.org/doc/html/rfc5280), including the Certificate Extensions specified in section 4.2 of the memo.
+ User names with special characters might cause connection errors.
+ The maximum username length is 1024 bytes. Connections with longer usernames will be rejected.

### Connection and DNS requirements
<a name="bp-dns"></a>
+ We do not recommend connecting to a Client VPN endpoint using IP addresses. Because Client VPN is a managed service, you will occasionally see changes in the IP addresses to which the DNS name resolves. In addition, you will see Client VPN network interfaces deleted and recreated in your CloudTrail logs. We recommend connecting to the Client VPN endpoint using the DNS name provided.
+ The Client VPN service requires that the IP address the client is connected to matches the IP that the Client VPN endpoint's DNS name resolves to. In other words, if you set a custom DNS record for the Client VPN endpoint, then forward the traffic to the actual IP address the endpoint's DNS name resolves to, this setup will not work using recent AWS provided clients. This rule was added to mitigate a server IP attack as described here: [TunnelCrack](https://tunnelcrack.mathyvanhoef.com/).
+ You can use an AWS provided client to connect to multiple concurrent DNS sessions. However, for name resolution to work correctly, the DNS servers of all connections should have synchronized records.
+ The Client VPN service requires that the local area network (LAN) IP address ranges of client devices be within the following standard private IP address ranges: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, or `169.254.0.0/16`. If the client LAN address range is detected to fall outside of the above ranges, the Client VPN endpoint will automatically push the OpenVPN directive "redirect-gateway block-local" to the client, forcing all LAN traffic into the VPN. Therefore, if you require LAN access during VPN connections, it is advised that you use the conventional address ranges listed above for your LAN. This rule is enforced to mitigate chances of a local net attack as described here: [TunnelCrack](https://tunnelcrack.mathyvanhoef.com/).
+ In Windows, when a full-tunnel endpoint is used, all DNS traffic is forced through the tunnel, regardless of the endpoint's IP address type (IPv4 IPv6, or dual stack). For DNS to function, a DNS server must be set up and reachable within the tunnel.

### Limitations and restrictions
<a name="bp-limits"></a>
+ IP forwarding is not currently supported when using the AWS Client VPN desktop application. IP forwarding is supported from other clients.
+ Client VPN does not support multi-Region replication in AWS Managed Microsoft AD. The Client VPN endpoint must be in the same Region as the AWS Managed Microsoft AD resource.
+ You can't establish a VPN connection from a computer if there are multiple users logged into the operating system.
+ Client-to-client communication is not supported for IPv6 clients. If an IPv6 client tries to communicate with another IPv6 client, the traffic will be dropped.
+ IPv6 and dual-stack endpoints require that user devices and internet service providers (ISPs) support the corresponding IP configuration.

# How AWS Client VPN works
<a name="how-it-works"></a>

With AWS Client VPN, there are two types of user personas that interact with the Client VPN endpoint: administrators and clients.

Client VPN supports IPv4, IPv6, and dual-stack (both IPv4 and IPv6) connectivity. You can create endpoints that use IPv4, IPv6, or both, allowing you to connect to IPv6 resources in your VPCs or connect from clients on IPv6 networks. This flexibility helps organizations that have already implemented or are transitioning to IPv6 infrastructure.

The *administrator* is responsible for setting up and configuring the service. This involves creating the Client VPN endpoint, associating the target network, configuring the authorization rules, and setting up additional routes (if required). After the Client VPN endpoint is set up and configured, the administrator downloads the Client VPN endpoint configuration file and distributes it to the clients who need access. The Client VPN endpoint configuration file includes the DNS name of the Client VPN endpoint and authentication information that's required to establish a VPN session. For more information about setting up the service, see [Get started with AWS Client VPN](#cvpn-getting-started).

The *client* is the end user. This is the person who connects to the Client VPN endpoint to establish a VPN session. The client establishes the VPN session from their local computer or mobile device using an OpenVPN-based VPN client application. After they have established the VPN session, they can securely access the resources in the VPC in which the associated subnet is located. They can also access other resources in AWS, an on-premises network, or other clients if the required route and authorization rules have been configured. For more information about connecting to a Client VPN endpoint to establish a VPN session, see [Getting Started](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/user-getting-started.html) in the *AWS Client VPN User Guide*.

The following graphic illustrates the basic Client VPN architecture.

![Client VPN architecture](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/architecture.png)


## Scenarios and examples for Client VPN
<a name="scenario"></a>

AWS Client VPN is a fully-managed remote access VPN solution that you use to allow clients secure access to resources within both AWS and your on-premises network. There are multiple options for how you configure access. This section provides examples for creating and configuring Client VPN access for your clients.

**Scenarios**
+ [Access a VPC using Client VPN](#scenario-vpc)
+ [Access a peered VPC using Client VPN](#scenario-peered)
+ [Access an on-premises network using Client VPN](#scenario-onprem)
+ [Access the internet using Client VPN](#scenario-internet)
+ [Client-to-client access using Client VPN](#scenario-client-to-client)
+ [Restrict access to your network using Client VPN](#scenario-restrict)

### Access a VPC using Client VPN
<a name="scenario-vpc"></a>

The AWS Client VPN configuration for this scenario includes a single target VPC. We recommend this configuration if you need to give clients access to the resources inside a single VPC only.

![Client VPN accessing a VPC](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/client-vpn-scenario-vpc.png)


Before you begin, do the following:
+ Create or identify a VPC with at least one subnet. Identify the subnet in the VPC to associate with the Client VPN endpoint and note its IPv4 CIDR ranges.
+ Identify a suitable CIDR range for the client IP addresses that does not overlap with the VPC CIDR. 
+ Review the rules and limitations for Client VPN endpoints in [Rules and best practices for using AWS Client VPN](#what-is-best-practices).

**To implement this configuration**

1. Create a Client VPN endpoint in the same Region as the VPC. To do this, perform the steps described in [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create).

1. Associate the subnet with the Client VPN endpoint. To do this, perform the steps described in [Associate a target network with an AWS Client VPN endpoint](#cvpn-working-target-associate) and select the subnet and the VPC you identified earlier.

1. Add an authorization rule to give clients access to the VPC. To do this, perform the steps described in [Add an authorization rule](#cvpn-working-rule-authorize-add), and for **Destination network**, enter the IPv4 CIDR range of the VPC.

1. Add a rule to your resources' security groups to allow traffic from the security group that was applied to the subnet association in step 2. For more information, see [Security groups](#security-groups).

### Access a peered VPC using Client VPN
<a name="scenario-peered"></a>

The AWS Client VPN configuration for this scenario includes a target VPC (VPC A) that is peered with an additional VPC (VPC B). We recommend this configuration if you need to give clients access to the resources inside a target VPC and to other VPCs that are peered with it (such as VPC B).

**Note**  
The procedure for allowing access to a peered VPC (outlined following the network diagram) is required only if the Client VPN endpoint was configured for split-tunnel mode. In full-tunnel mode, access to the peered VPC is allowed by default.

![Client VPN accessing a peer VPC](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/client-vpn-scenario-peer-vpc.png)


Before you begin, do the following:
+ Create or identify a VPC with at least one subnet. Identify the subnet in the VPC to associate with the Client VPN endpoint and note its IPv4 CIDR ranges.
+ Identify a suitable CIDR range for the client IP addresses that does not overlap with the VPC CIDR. 
+ Review the rules and limitations for Client VPN endpoints in [Rules and best practices for using AWS Client VPN](#what-is-best-practices).

**To implement this configuration**

1. Establish the VPC peering connection between the VPCs. Follow the steps at [Creating and accepting a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html) in the *Amazon VPC Peering Guide*. Confirm that instances in VPC A can communicate with instances in VPC B using the peering connection.

1. Create a Client VPN endpoint in the same Region as the target VPC. In the diagram, this is VPC A. Perform the steps described in [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create).

1. Associate the subnet that you identified with the Client VPN endpoint that you created. To do this, perform the steps described in [Associate a target network with an AWS Client VPN endpoint](#cvpn-working-target-associate), selecting the VPC and the subnet. By default, we associate the default security group of the VPC with the Client VPN endpoint. You can associate a different security group using the steps described in [Apply a security group to a target network in AWS Client VPN](#cvpn-working-target-apply).

1. Add an authorization rule to give clients access to the target VPC. To do this, perform the steps described in [Add an authorization rule](#cvpn-working-rule-authorize-add). For **Destination network to enable **, enter the IPv4 CIDR range of the VPC.

1. Add a route to direct traffic to the peered VPC. In the diagram, this is VPC B. To do this, perform the steps described in [Create an AWS Client VPN endpoint route](#cvpn-working-routes-create). For **Route destination**, enter the IPv4 CIDR range of the peered VPC. For **Target VPC Subnet ID**, select the subnet you associated with the Client VPN endpoint.

1. Add an authorization rule to give clients access to peered VPC. To do this, perform the steps described in [Add an authorization rule](#cvpn-working-rule-authorize-add). For **Destination network**, enter the IPv4 CIDR range of the peered VPC.

1. Add a rule to the security groups for your instances in VPC A and VPC B to allow traffic from the security group that was applied the Client VPN endpoint in step 3. For more information, see [Security groups](#security-groups).

### Access an on-premises network using Client VPN
<a name="scenario-onprem"></a>

The AWS Client VPN configuration for this scenario includes access to an on-premises network only. We recommend this configuration if you need to give clients access to the resources inside an on-premises network only.

![Client VPN accessing an on-premises network](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/client-vpn-scenario-on-premises.png)


Before you begin, do the following:
+ Create or identify a VPC with at least one subnet. Identify the subnet in the VPC to associate with the Client VPN endpoint and note its IPv4 CIDR ranges.
+ Identify a suitable CIDR range for the client IP addresses that does not overlap with the VPC CIDR. 
+ Review the rules and limitations for Client VPN endpoints in [Rules and best practices for using AWS Client VPN](#what-is-best-practices).

**To implement this configuration**

1. Enable communication between the VPC and your own on-premises network over an AWS Site-to-Site VPN connection. To do this, perform the steps described in [Getting started](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html) in the *AWS Site-to-Site VPN User Guide*. 
**Note**  
Alternatively, you can implement this scenario by using an Direct Connect connection between your VPC and your on-premises network. For more information, see the [Direct Connect User Guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/).

1. Test the AWS Site-to-Site VPN connection you created in the previous step. To do this, perform the steps described in [Testing the Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/HowToTestEndToEnd_Linux.html) in the *AWS Site-to-Site VPN User Guide*. If the VPN connection is functioning as expected, continue to the next step.

1. Create a Client VPN endpoint in the same Region as the VPC. To do this, perform the steps described in [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create).

1. Associate the subnet that you identified earlier with the Client VPN endpoint. To do this, perform the steps described in [Associate a target network with an AWS Client VPN endpoint](#cvpn-working-target-associate) and select the VPC and the subnet.

1. Add a route that allows access to the AWS Site-to-Site VPN connection. To do this, perform the steps described in [Create an AWS Client VPN endpoint route](#cvpn-working-routes-create); for **Route destination**, enter the IPv4 CIDR range of the AWS Site-to-Site VPN connection, and for **Target VPC Subnet ID**, select the subnet you associated with the Client VPN endpoint.

1. Add an authorization rule to give clients access to the AWS Site-to-Site VPN connection. To do this, perform the steps described in [Add an authorization rule to an AWS Client VPN endpoint](#cvpn-working-rule-authorize-add); for **Destination network**, enter the AWS Site-to-Site VPN connection IPv4 CIDR range.

### Access the internet using Client VPN
<a name="scenario-internet"></a>

The AWS Client VPN configuration for this scenario includes a single target VPC and access to the internet. We recommend this configuration if you need to give clients access to the resources inside a single target VPC and also allow access to the internet.

If you completed the [Get started with AWS Client VPN](#cvpn-getting-started) tutorial, then you've already implemented this scenario.

![Client VPN accessing the internet](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/client-vpn-scenario-igw.png)


Before you begin, do the following:
+ Create or identify a VPC with at least one subnet. Identify the subnet in the VPC to associate with the Client VPN endpoint and note its IPv4 CIDR ranges.
+ Identify a suitable CIDR range for the client IP addresses that does not overlap with the VPC CIDR. 
+ Review the rules and limitations for Client VPN endpoints in [Rules and best practices for using AWS Client VPN](#what-is-best-practices).

**To implement this configuration**

1. Ensure that the security group that you'll use for the Client VPN endpoint allows outbound traffic to the internet. To do this, add outbound rules that allow traffic to 0.0.0.0/0 for HTTP and HTTPS traffic.

1. Create an internet gateway and attach it to your VPC. For more information, see [Creating and Attaching an Internet Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html#Add_IGW_Attach_Gateway) in the *Amazon VPC User Guide*.

1. Make your subnet public by adding a route to the internet gateway to its route table. In the VPC console, choose **Subnets**, select the subnet you intend to associate with the Client VPN endpoint, choose **Route Table**, and then choose the route table ID. Choose **Actions**, choose **Edit routes**, and choose **Add route**. For **Destination**, enter `0.0.0.0/0`, and for **Target**, choose the internet gateway from the previous step.

1. Create a Client VPN endpoint in the same Region as the VPC. To do this, perform the steps described in [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create).

1. Associate the subnet that you identified earlier with the Client VPN endpoint. To do this, perform the steps described in [Associate a target network with an AWS Client VPN endpoint](#cvpn-working-target-associate) and select the VPC and the subnet.

1. Add an authorization rule to give clients access to the VPC. To do this, perform the steps described in [Add an authorization rule](#cvpn-working-rule-authorize-add); and for **Destination network to enable **, enter the IPv4 CIDR range of the VPC.

1. Add a route that enables traffic to the internet. To do this, perform the steps described in [Create an AWS Client VPN endpoint route](#cvpn-working-routes-create); for **Route destination**, enter `0.0.0.0/0`, and for **Target VPC Subnet ID**, select the subnet you associated with the Client VPN endpoint.

1. Add an authorization rule to give clients access to the internet. To do this, perform the steps described in [Add an authorization rule](#cvpn-working-rule-authorize-add); for **Destination network**, enter `0.0.0.0/0`.

1. Ensure that the security groups for the resources in your VPC have a rule that allows access from the security group associated with the Client VPN endpoint. This enables your clients to access the resources in your VPC.

### Client-to-client access using Client VPN
<a name="scenario-client-to-client"></a>

The AWS Client VPN configuration for this scenario enables clients to access a single VPC, and enables clients to route traffic to each other. We recommend this configuration if the clients that connect to the same Client VPN endpoint also need to communicate with each other. Clients can communicate with each other using the unique IP address that's assigned to them from the client CIDR range when they connect to the Client VPN endpoint.

![Client-to-client access](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/client-vpn-scenario-client-to-client.png)


Before you begin, do the following:
+ Create or identify a VPC with at least one subnet. Identify the subnet in the VPC to associate with the Client VPN endpoint and note its IPv4 CIDR ranges.
+ Identify a suitable CIDR range for the client IP addresses that does not overlap with the VPC CIDR. 
+ Review the rules and limitations for Client VPN endpoints in [Rules and best practices for using AWS Client VPN](#what-is-best-practices).

**Note**  
Network-based authorization rules using Active Directory groups or SAML-based IdP groups are not supported in this scenario.

**To implement this configuration**

1. Create a Client VPN endpoint in the same Region as the VPC. To do this, perform the steps described in [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create).

1. Associate the subnet that you identified earlier with the Client VPN endpoint. To do this, perform the steps described in [Associate a target network with an AWS Client VPN endpoint](#cvpn-working-target-associate) and select the VPC and the subnet.

1. Add a route to the local network in the route table. To do this, perform the steps described in [Create an AWS Client VPN endpoint route](#cvpn-working-routes-create). For **Route destination**, enter the client CIDR range, and for **Target VPC Subnet ID**, specify `local`.

1. Add an authorization rule to give clients access to the VPC. To do this, perform the steps described in [Add an authorization rule](#cvpn-working-rule-authorize-add). For **Destination network to enable **, enter the IPv4 CIDR range of the VPC.

1. Add an authorization rule to give clients access to the client CIDR range. To do this, perform the steps described in [Add an authorization rule](#cvpn-working-rule-authorize-add). For **Destination network to enable**, enter the client CIDR range.

### Restrict access to your network using Client VPN
<a name="scenario-restrict"></a>

You can configure your AWS Client VPN endpoint to restrict access to specific resources in your VPC. For user-based authentication, you can also restrict access to parts of your network, based on the user group that accesses the Client VPN endpoint.

#### Restrict access using security groups
<a name="scenario-restrict-security-groups"></a>

You can grant or deny access to specific resources in your VPC by adding or removing security group rules that reference the security group that was applied to the target network association (the Client VPN security group). This configuration expands on the scenario described in [Access a VPC using Client VPN](#scenario-vpc). This configuration is applied in addition to the authorization rule configured in that scenario.

To grant access to a specific resource, identify the security group that's associated with the instance on which your resource is running. Then, create a rule that allows traffic from the Client VPN security group. 

In the following diagram, security group A is the Client VPN security group, security group B is associated with an EC2 instance, and security group C is associated with an EC2 instance. If you add a rule to security group B that allows access from security group A, then clients can access the instance associated with security group B. If security group C does not have a rule that allows access from security group A, then clients can't access the instance associated with security group C.

![Restricting access to resources in a VPC](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/client-vpn-scenario-security-groups.png)


Before you begin, check if the Client VPN security group is associated with other resources in your VPC. If you add or remove rules that reference the Client VPN security group, you might grant or deny access for the other associated resources too. To prevent this, use a security group that is specifically created for use with your Client VPN endpoint.

**To create a security group rule**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security Groups**.

1. Choose the security group that's associated with the instance on which your resource is running.

1. Choose **Actions**, **Edit inbound rules**.

1. Choose **Add rule**, and then do the following:
   + For **Type**, choose **All traffic**, or a specific type of traffic that you want to allow.
   + For **Source**, choose **Custom**, and then enter or choose the ID of the Client VPN security group.

1. Choose **Save rules**

To remove access to a specific resource, check the security group that's associated with the instance on which your resource is running. If there is a rule that allows traffic from the Client VPN security group, delete it.

**To check your security group rules**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security Groups**.

1. Choose **Inbound Rules**.

1. Review the list of rules. If there is a rule where **Source** is the Client VPN security group, choose **Edit Rules**, and choose **Delete** (the x icon) for the rule. Choose **Save rules**.

#### Restrict access based on user groups
<a name="scenario-restrict-groups"></a>

If your Client VPN endpoint is configured for user-based authentication, you can grant specific groups of users access to specific parts of your network. To do this, complete the following steps:

1. Configure users and groups in Directory Service or your IdP. For more information, see the following topics:
   + [Active Directory authentication in Client VPN](#ad)
   + [Requirements and considerations for SAML-based federated authentication](#saml-requirements)

1. Create an authorization rule for your Client VPN endpoint that allows a specified group access to all or part of your network. For more information, see [AWS Client VPN authorization rules](#cvpn-working-rules).

If your Client VPN endpoint is configured for mutual authentication, you cannot configure user groups. When you create an authorization rule, you must grant access to all users. To enable specific groups of users access to specific parts of your network, you can create multiple Client VPN endpoints. For example, for each group of users that accesses your network, do the following:

1. Create a set of server and client certificates and keys for that group of users. For more information, see [Mutual authentication in AWS Client VPN](#mutual).

1. Create a Client VPN endpoint. For more information, see [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create).

1. Create an authorization rule that grants access to all or part of your network. For example, for a Client VPN endpoint that is used by administrators, you might create an authorization rule that grants access to the entire network. For more information, see [Add an authorization rule](#cvpn-working-rule-authorize-add).

## Client authentication in AWS Client VPN
<a name="client-authentication"></a>

Client authentication is implemented at the first point of entry into the AWS Cloud. It is used to determine whether clients are allowed to connect to the Client VPN endpoint. If authentication succeeds, clients connect to the Client VPN endpoint and establish a VPN session. If authentication fails, the connection is denied and the client is prevented from establishing a VPN session.

Client VPN offers the following types of client authentication: 
+ [Active Directory authentication](#ad) (user-based)
+ [Mutual authentication](#mutual) (certificate-based)
+ [Single sign-on (SAML-based federated authentication)](#federated-authentication) (user-based)

You can use one of the preceding methods alone, or you can use a combination of mutual authentication with a user-based method such as the following:
+ Mutual authentication and federated authentication
+ Mutual authentication and Active Directory authentication

**Important**  
To create a Client VPN endpoint, you must provision a server certificate in AWS Certificate Manager, regardless of the type of authentication that you use. For more information about creating and provisioning a server certificate, see the steps in [Mutual authentication in AWS Client VPN](#mutual).
If you use a combination of mutual authentication and user-based authentication, both methods must then be used to correctly authenticate in VPN. 

### Active Directory authentication in Client VPN
<a name="ad"></a>

Client VPN provides Active Directory support by integrating with Directory Service. With Active Directory authentication, clients are authenticated against existing Active Directory groups. Using Directory Service, Client VPN can connect to existing Active Directories provisioned in AWS or in your on-premises network. This allows you to use your existing client authentication infrastructure. If you are using an on-premises Active Directory and you do not have an existing AWS Managed Microsoft AD, you must configure an Active Directory Connector (AD Connector). You can use one Active Directory server to authenticate the users. For more information about Active Directory integration, see the [AWS Directory Service Administration Guide](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/).

Client VPN supports multi-factor authentication (MFA) when it's enabled for AWS Managed Microsoft AD or AD Connector. If MFA is enabled, clients must enter a user name, password, and MFA code when they connect to a Client VPN endpoint. For more information about enabling MFA, see [Enable Multi-Factor Authentication for AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html) and [Enable Multi-Factor Authentication for AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_mfa.html) in the *AWS Directory Service Administration Guide*. 

For quotas and rules for configuring users and groups in Active Directory, see [Users and groups quotas](#quotas-users-groups).

### Mutual authentication in AWS Client VPN
<a name="mutual"></a>

With mutual authentication, Client VPN uses certificates to perform authentication between the client and the server. Certificates are a digital form of identification issued by a certificate authority (CA). The server uses client certificates to authenticate clients when they attempt to connect to the Client VPN endpoint. You must create a server certificate and key, and at least one client certificate and key.

You must upload the server certificate to AWS Certificate Manager (ACM) and specify it when you create a Client VPN endpoint. When you upload the server certificate to ACM, you also specify the certificate authority (CA). You only need to upload the client certificate to ACM when the CA of the client certificate is different from the CA of the server certificate. For more information about ACM, see the [AWS Certificate Manager User Guide](https://docs.aws.amazon.com/acm/latest/userguide/). 

You can create a separate client certificate and key for each client that will connect to the Client VPN endpoint. This enables you to revoke a specific client certificate if a user leaves your organization. In this case, when you create the Client VPN endpoint, you can specify the server certificate ARN for the client certificate, provided that the client certificate has been issued by the same CA as the server certificate.

Certificates used in AWS Client VPN must adhere to [RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](https://datatracker.ietf.org/doc/html/rfc5280), including the Certificate Extensions specified in section 4.2 of the memo.

**Note**  
A Client VPN endpoint supports 1024-bit and 2048-bit RSA key sizes only. Also, the client certificate must have the CN attribute in the Subject field.  
When certificates being used with the Client VPN service are updated, whether through ACM auto-rotation, manually importing a new certificate, or metadata updates to IAM Identity Center the Client VPN service will automatically update theClient VPN endpoint with the newer certificate. This is an automated process that can take up to 5 hours. 

**Topics**
+ [Enable mutual authentication](#client-auth-mutual-enable)
+ [Renew your server certificate](#mutual-renew)

#### Enable mutual authentication for AWS Client VPN
<a name="client-auth-mutual-enable"></a>

You can enable mutual authentication in Client VPN in either Linux/MacOS or Windows.

------
#### [ Linux/macOS ]

The following procedure uses OpenVPN easy-rsa to generate the server and client certificates and keys, and then uploads the server certificate and key to ACM. For more information, see the [Easy-RSA 3 Quickstart README](https://github.com/OpenVPN/easy-rsa/blob/v3.0.6/README.quickstart.md).

**To generate the server and client certificates and keys and upload them to ACM**

1. Clone the OpenVPN easy-rsa repo to your local computer and navigate to the `easy-rsa/easyrsa3` folder.

   ```
   $ git clone https://github.com/OpenVPN/easy-rsa.git
   ```

   ```
   $ cd easy-rsa/easyrsa3
   ```

1. Initialize a new PKI environment.

   ```
   $ ./easyrsa init-pki
   ```

1. To build a new certificate authority (CA), run this command and follow the prompts.

   ```
   $ ./easyrsa build-ca nopass
   ```

1. Generate the server certificate and key.

   ```
   $ ./easyrsa --san=DNS:server build-server-full server nopass
   ```

1. Generate the client certificate and key.

   Make sure to save the client certificate and the client private key because you will need them when you configure the client.

   ```
   $ ./easyrsa build-client-full client1.domain.tld nopass
   ```

   You can optionally repeat this step for each client (end user) that requires a client certificate and key.

1. Copy the server certificate and key and the client certificate and key to a custom folder and then navigate into the custom folder.

   Before you copy the certificates and keys, create the custom folder by using the `mkdir` command. The following example creates a custom folder in your home directory.

   ```
   $ mkdir ~/{{custom_folder}}/
   $ cp pki/ca.crt ~/{{custom_folder}}/
   $ cp pki/issued/server.crt ~/{{custom_folder}}/
   $ cp pki/private/server.key ~/{{custom_folder}}/
   $ cp pki/issued/client1.domain.tld.crt ~/{{custom_folder}}
   $ cp pki/private/client1.domain.tld.key ~/{{custom_folder}}/
   $ cd ~/{{custom_folder}}/
   ```

1. Upload the server certificate and key and the client certificate and key to ACM. Be sure to upload them in the same Region in which you intend to create the Client VPN endpoint. The following commands use the AWS CLI to upload the certificates. To upload the certificates using the ACM console instead, see [Import a certificate](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate-api-cli.html) in the *AWS Certificate Manager User Guide*.

   ```
   $ aws acm import-certificate --certificate fileb://server.crt --private-key fileb://server.key --certificate-chain fileb://ca.crt
   ```

   ```
   $ aws acm import-certificate --certificate fileb://client1.domain.tld.crt --private-key fileb://client1.domain.tld.key --certificate-chain fileb://ca.crt
   ```

   You do not necessarily need to upload the client certificate to ACM. If the server and client certificates have been issued by the same Certificate Authority (CA), you can use the server certificate ARN for both server and client when you create the Client VPN endpoint. In the steps above, the same CA has been used to create both certificates. However, the steps to upload the client certificate are included for completeness.

------
#### [ Windows ]

The following procedure installs Easy-RSA 3.x software and uses it to generate server and client certificates and keys.

**To generate server and client certificates and keys and upload them to ACM**

1. Open the [EasyRSA releases](https://github.com/OpenVPN/easy-rsa/releases) page and download the ZIP file for your version of Windows and extract it.

1. Open a command prompt and navigate to the location that the `EasyRSA-3.x` folder was extracted to.

1. Run the following command to open the EasyRSA 3 shell.

   ```
   C:\Program Files\EasyRSA-3.x> .\EasyRSA-Start.bat
   ```

1. Initialize a new PKI environment.

   ```
   # ./easyrsa init-pki
   ```

1. To build a new certificate authority (CA), run this command and follow the prompts.

   ```
   # ./easyrsa build-ca nopass
   ```

1. Generate the server certificate and key.

   ```
   # ./easyrsa --san=DNS:server build-server-full server nopass
   ```

1. Generate the client certificate and key.

   ```
   # ./easyrsa build-client-full client1.domain.tld nopass
   ```

   You can optionally repeat this step for each client (end user) that requires a client certificate and key.

1. Exit the EasyRSA 3 shell.

   ```
   # exit
   ```

1. Copy the server certificate and key and the client certificate and key to a custom folder and then navigate into the custom folder.

   Before you copy the certificates and keys, create the custom folder by using the `mkdir` command. The following example creates a custom folder in your C:\\ drive.

   ```
   C:\Program Files\EasyRSA-3.x> mkdir C:\{{custom_folder}}
   C:\Program Files\EasyRSA-3.x> copy pki\ca.crt C:\{{custom_folder}}
   C:\Program Files\EasyRSA-3.x> copy pki\issued\server.crt C:\{{custom_folder}}
   C:\Program Files\EasyRSA-3.x> copy pki\private\server.key C:\{{custom_folder}}
   C:\Program Files\EasyRSA-3.x> copy pki\issued\client1.domain.tld.crt C:\{{custom_folder}}
   C:\Program Files\EasyRSA-3.x> copy pki\private\client1.domain.tld.key C:\{{custom_folder}}
   C:\Program Files\EasyRSA-3.x> cd C:\{{custom_folder}}
   ```

1. Upload the server certificate and key and the client certificate and key to ACM. Be sure to upload them in the same Region in which you intend to create the Client VPN endpoint. The following commands use the AWS CLI to upload the certificates. To upload the certificates using the ACM console instead, see [Import a certificate](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate-api-cli.html) in the *AWS Certificate Manager User Guide*.

   ```
   aws acm import-certificate \
       --certificate fileb://server.crt \ 
       --private-key fileb://server.key \
       --certificate-chain fileb://ca.crt
   ```

   ```
   aws acm import-certificate \
       --certificate fileb://client1.domain.tld.crt \
       --private-key fileb://client1.domain.tld.key \
       --certificate-chain fileb://ca.crt
   ```

   You do not necessarily need to upload the client certificate to ACM. If the server and client certificates have been issued by the same Certificate Authority (CA), you can use the server certificate ARN for both server and client when you create the Client VPN endpoint. In the steps above, the same CA has been used to create both certificates. However, the steps to upload the client certificate are included for completeness.

------

#### Renew your server certificate for AWS Client VPN
<a name="mutual-renew"></a>

You can renew and re-import a Client VPN server certificate that has expired. Depending on the version of OpenVPN easy-rsa that you're using, the procedure will vary. See [Easy-RSA 3 Certificate Renewal and Revocation Documentation](https://github.com/OpenVPN/easy-rsa/blob/master/doc/EasyRSA-Renew-and-Revoke.md) for more details.

**To renew your server certificate**

1. Do **one** of the following:
   + Easy-RSA version 3.1.x

     1. Run the certificate renew command.

       ```
       $ ./easyrsa renew server nopass
       ```
   + Easy-RSA version 3.2.x

     1. Run the expire command.

        ```
        $ ./easyrsa expire server
        ```

     1. Sign a new certificate.

        ```
        $ ./easyrsa --san=DNS:server sign-req server server
        ```

1. Create a custom folder, copy the new files to it, then navigate into the folder.

   ```
   $ mkdir ~/{{custom_folder2}}
   $ cp pki/ca.crt ~/{{custom_folder2}}/
   $ cp pki/issued/server.crt ~/{{custom_folder2}}/
   $ cp pki/private/server.key ~/{{custom_folder2}}/
   $ cd ~/{{custom_folder2}}/
   ```

1. Import the new files to ACM. Be sure to import them in the same Region as the Client VPN endpoint. 

   ```
   $ aws acm import-certificate \
       --certificate fileb://server.crt \
       --private-key fileb://server.key \
       --certificate-chain fileb://ca.crt \
       --certificate-arn arn:aws:acm:{{region}}:{{123456789012}}:certificate/{{12345678-1234-1234-1234-12345678901}}
   ```

### Single sign-on — SAML 2.0-based federated authentication — in Client VPN
<a name="federated-authentication"></a>

AWS Client VPN supports identity federation with Security Assertion Markup Language 2.0 (SAML 2.0) for Client VPN endpoints. You can use identity providers (IdPs) that support SAML 2.0 to create centralized user identities. You can then configure a Client VPN endpoint to use SAML-based federated authentication, and associate it with the IdP. Users then connect to the Client VPN endpoint using their centralized credentials.

**Topics**
+ [Enable SAML](#client-auth-enable-saml)
+ [Authentication workflow](#federated-authentication-workflow)
+ [Requirements and considerations for SAML-based federated authentication](#saml-requirements)
+ [SAML-based IdP configuration resources](#saml-config-resources)

#### Authentication workflow
<a name="federated-authentication-workflow"></a>

The following diagram provides an overview of the authentication workflow for a Client VPN endpoint that uses SAML-based federated authentication. When you create and configure the Client VPN endpoint, you specify the IAM SAML identity provider.

![Authentication workflow](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/federated-auth-workflow.png)


1. The user opens the AWS provided client on their device and initiates a connection to the Client VPN endpoint.

1. The Client VPN endpoint sends an IdP URL and authentication request back to the client, based on the information that was provided in the IAM SAML identity provider.

1. The AWS provided client opens a new browser window on the user's device. The browser makes a request to the IdP and displays a login page.

1. The user enters their credentials on the login page, and the IdP sends a signed SAML assertion back to the client.

1. The AWS provided client sends the SAML assertion to the Client VPN endpoint.

1. The Client VPN endpoint validates the assertion and either allows or denies access to the user.

#### Requirements and considerations for SAML-based federated authentication
<a name="saml-requirements"></a>

The following are the requirements and considerations for SAML-based federated authentication.
+ For quotas and rules for configuring users and groups in a SAML-based IdP, see [Users and groups quotas](#quotas-users-groups).
+ The SAML assertion and response must be signed.
+ AWS Client VPN only supports "AudienceRestriction" and "NotBefore and NotOnOrAfter" conditions in SAML assertions.
+ The maximum supported size for SAML responses is 128 KB.
+ AWS Client VPN does not provide signed authentication requests.
+ SAML single logout is not supported. Users can log out by disconnecting from the AWS provided client, or you can [terminate the connections](#cvpn-working-connections-disassociate).
+ A Client VPN endpoint supports a single IdP only.
+ Multi-factor authentication (MFA) is supported when it's enabled in your IdP.
+ Users must use the AWS provided client to connect to the Client VPN endpoint. They must use version 1.2.0 or later. For more information, see [Connect using the AWS provided client](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/connect-aws-client-vpn-connect.html).
+ The following browsers are supported for IdP authentication: Apple Safari, Google Chrome, Microsoft Edge, and Mozilla Firefox.
+ The AWS provided client reserves TCP port 35001 on users' devices for the SAML response.
+ If the metadata document for the IAM SAML identity provider is updated with an incorrect or malicious URL, this can cause authentication issues for users, or result in phishing attacks. Therefore, we recommend that you use AWS CloudTrail to monitor updates that are made to the IAM SAML identity provider. For more information, see [Logging IAM and AWS STS calls with AWS CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html) in the *IAM User Guide*.
+ AWS Client VPN sends an AuthN request to the IdP via an HTTP Redirect binding. Therefore, the IdP should support HTTP Redirect binding and it should be present in the IdP's metadata document.
+ For the SAML assertion, you must use an email address format for the `NameID` attribute.
+ The maximum username (`NameID`) length is 1024 bytes. Connections with longer usernames will be rejected.
+ When certificates being used with the Client VPN service are updated, whether through ACM auto-rotation, manually importing a new certificate, or metadata updates to IAM Identity Center the Client VPN service will automatically update the Client VPN endpoint with the newer certificate. This is an automated process that can take up to 5 hours.

#### SAML-based IdP configuration resources
<a name="saml-config-resources"></a>

The following table lists the SAML-based IdPs that we have tested for use with AWS Client VPN, and resources that can help you configure the IdP.


| IdP | Resource | 
| --- | --- | 
| Okta | [Authenticate AWS Client VPN users with SAML](https://aws.amazon.com/blogs/networking-and-content-delivery/authenticate-aws-client-vpn-users-with-saml/) | 
| Microsoft Entra ID (formerly Azure Active Directory) | For more information, see [Tutorial: Microsoft Entra single sign-on (SSO) integration with AWS ClientVPN](https://learn.microsoft.com/en-gb/entra/identity/saas-apps/aws-clientvpn-tutorial) on the Microsoft documentation website. | 
| JumpCloud | [Integrate with AWS Client VPN](https://jumpcloud.com/support/integrate-with-aws-client-vpn) | 
| AWS IAM Identity Center | [Using IAM Identity Center with AWS Client VPN for authentication and authorization](https://aws.amazon.com/blogs/networking-and-content-delivery/using-aws-sso-with-aws-client-vpn-for-authentication-and-authorization/)  | 

##### Service provider information for creating an app
<a name="saml-config-service-provider-info"></a>

To create a SAML-based app using an IdP that is not listed in the preceding table, use the following information to configure the AWS Client VPN service provider information.
+ Assertion Consumer Service (ACS) URL: `http://127.0.0.1:35001`
+ Audience URI: `urn:amazon:webservices:clientvpn`

At least one attribute must be included in the SAML response from the IdP. The following are example attributes.


| Attribute | Description | 
| --- | --- | 
| FirstName | The first name of the user. | 
| LastName | The last name of the user. | 
| memberOf | The group or groups that the user belongs to. | 

**Note**  
The `memberOf` attribute is required for using Active Directory or SAML IdP group-based authorization rules. It is also case-sensitive, and must be configured exactly as specified. See [Network-based authorization](#auth-rules) and [AWS Client VPN authorization rules](#cvpn-working-rules) for more information.

##### Support for the self-service portal
<a name="saml-self-service-support"></a>

If you enable the self-service portal for your Client VPN endpoint, users log into the portal using their SAML-based IdP credentials.

If your IdP supports multiple Assertion Consumer Service (ACS) URLs, add the following ACS URL to your app.

```
https://self-service.clientvpn.amazonaws.com/api/auth/sso/saml
```

If you are using the Client VPN endpoint in a GovCloud region, use the following ACS URL instead. If you use the same IDP app to authenticate for both standard and GovCloud regions, you can add both URLs.

```
https://gov.self-service.clientvpn.amazonaws.com/api/auth/sso/saml
```

If your IdP does not support multiple ACS URLs, do the following: 

1. Create an additional SAML-based app in your IdP and specify the following ACS URL.

   ```
   https://self-service.clientvpn.amazonaws.com/api/auth/sso/saml
   ```

1. Generate and download a federation metadata document.

1. Create an IAM SAML identity provider in the same AWS account as the Client VPN endpoint. For more information, see [Creating IAM SAML Identity Providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html) in the *IAM User Guide*. 
**Note**  
You create this IAM SAML identity provider in addition to the one you [create for the main app](#federated-authentication).

1. [Create the Client VPN endpoint](#cvpn-working-endpoint-create), and specify both of the IAM SAML identity providers that you created.

#### Enable SAML for AWS Client VPN
<a name="client-auth-enable-saml"></a>

 You can enable SAML for single sign-on for Client VPN by completing the following steps. Alternatively, if you enabled the self-service portal for your Client VPN endpoint, instruct your users to go to the self-service portal to get the configuration file and AWS provided client. For more information, see [AWS Client VPN access to the self-service portal](#cvpn-self-service-portal).

**To enable your SAML-based IdP to work with a Client VPN endpoint, you must do the following.**

1. Create a SAML-based app in your chosen IdP to use with AWS Client VPN, or use an existing app.

1. Configure your IdP to establish a trust relationship with AWS. For resources, see [SAML-based IdP configuration resources](#saml-config-resources).

1. In your IdP, generate and download a federation metadata document that describes your organization as an IdP. 

   This signed XML document is used to establish the trust relationship between AWS and the IdP.

1. Create an IAM SAML identity provider in the same AWS account as the Client VPN endpoint. 

   The IAM SAML identity provider defines your organization's IdP to AWS trust relationship using the metadata document generated by the IdP. For more information, see [Creating IAM SAML Identity Providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html) in the *IAM User Guide*. If you later update the app configuration in the IdP, generate a new metadata document and update your IAM SAML identity provider.
**Note**  
You do not need to create an IAM role to use the IAM SAML identity provider.

1. Create a Client VPN endpoint. 

   Specify federated authentication as the authentication type, and specify the IAM SAML identity provider that you created. For more information, see [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create).

1. Export the [client configuration file](#cvpn-working-endpoint-export) and distribute it to your users. Instruct your users to download the latest version of the [AWS provided client](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/connect-aws-client-vpn-connect.html), and to use it to load the configuration file and connect to the Client VPN endpoint.

## Client authorization in AWS Client VPN
<a name="client-authorization"></a>

Client VPN supports two types of client authorization: security groups and network-based authorization (using authorization rules).

### Security groups
<a name="security-groups"></a>

When you create a Client VPN endpoint, you can specify the security groups from a specific VPC to apply to the Client VPN endpoint. When you associate a subnet with a Client VPN endpoint, we automatically apply the VPC's default security group. You can change the security groups after you create the Client VPN endpoint. For more information, see [Apply a security group to a target network in AWS Client VPN](#cvpn-working-target-apply). The security groups are associated with the Client VPN network interfaces. 

You can enable Client VPN users to access your applications in a VPC by adding a rule to your applications' security groups to allow traffic from the security group that was applied to the association. 

Conversely, you can restrict access for Client VPN users by not specifying the security group that was applied to the association, or by removing the rule that references the Client VPN endpoint security group. The security group rules that you require might also depend on the kind of VPN access that you want to configure. For more information, see [Scenarios and examples for Client VPN](#scenario).

For more information about security groups, see [Security groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) in the *Amazon VPC User Guide*.

### Network-based authorization
<a name="auth-rules"></a>

Network-based authorization is implemented using authorization rules. For each network that you want to enable access, you must configure authorization rules that limit the users who have access. For a specified network, you configure the Active Directory group or the SAML-based IdP group that is allowed access. Only users who belong to the specified group can access the specified network. If you are not using Active Directory or SAML-based federated authentication, or you want to open access to all users, you can specify a rule that grants access to all clients. For more information, see [AWS Client VPN authorization rules](#cvpn-working-rules).

### Authorization policy
<a name="device-posture-authorization"></a>

You can define an authorization policy to control connections based on device health, user identity, and connection details. When an authorization policy is configured, Client VPN evaluates it when a device connects and again every 5 minutes for the life of the session. Sessions that no longer meet your requirements are disconnected. Authorization policies are written in the Cedar policy language and can evaluate device posture tokens, user identity, or both. For setup instructions, see [Device posture for AWS Client VPN](#device-posture).

**Topics**
+ [Security groups](#security-groups)
+ [Network-based authorization](#auth-rules)
+ [Authorization policy](#device-posture-authorization)
+ [Create an endpoint security group rule](#client-auth-rule-create)

### Create an AWS Client VPN endpoint security group rule
<a name="client-auth-rule-create"></a>

The default security group for the VPC applied when you associate a subnet with a Client VPN might restrict traffic from the default security group traffic that you want to allow, while simultaneously allowing traffic that you don't want. Use the following steps to create a Client VPN endpoint security group rule that either allows or restricts traffic for an endpoint security group associated with a resource or application. For more information about security group rules, see [Security groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) in the *Amazon VPC User Guide*.

**To add a rule that allows traffic from the Client VPN endpoint security group**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security Groups**.

1. Choose the security group that's associated with your resource or application, and choose **Actions**, **Edit inbound rules**.

1. Choose **Add rule**.

1. For **Type**, choose **All traffic**. Alternatively, you can restrict access to a specific type of traffic, for example, **SSH**. 

   For **Source**, specify the ID of the security group that's associated with the target network (subnet) for the Client VPN endpoint.

1. Choose **Save rules**.

## Connection authorization in AWS Client VPN
<a name="connection-authorization"></a>

You can configure a *client connect handler* for your Client VPN endpoint. The handler enables you to run custom logic that authorizes a new connection, based on device, user, and connection attributes. The client connect handler runs after the Client VPN service has authenticated the device and user. 

To configure a client connect handler for your Client VPN endpoint, create an AWS Lambda function that takes device, user, and connection attributes as inputs, and returns a decision to the Client VPN service to allow or deny a new connection. You specify the Lambda function in your Client VPN endpoint. When devices connect to your Client VPN endpoint, the Client VPN service invokes the Lambda function on your behalf. Only connections that are authorized by the Lambda function are allowed to connect to the Client VPN endpoint.

**Note**  
Currently, the only type of client connect handler that is supported is a Lambda function. 

You can also define Cedar-based authorization policies that evaluate device posture tokens and user identity. For more information, see [Device posture for AWS Client VPN](#device-posture).

### Requirements and considerations
<a name="client-connect-handler-reqs"></a>

The following are the requirements and considerations for the client connect handler:
+ The name of the Lambda function must begin with the `AWSClientVPN-` prefix.
+ Qualified Lambda functions are supported. 
+ The Lambda function must be in the same AWS Region and the same AWS account as the Client VPN endpoint.
+ The Lambda function times out after 30 seconds. This value cannot be changed.
+ The Lambda function is invoked synchronously. It's invoked after device and user authentication, and before the authorization rules are evaluated.
+ If the Lambda function is invoked for a new connection and the Client VPN service does not get an expected response from the function, the Client VPN service denies the connection request. For example, this can occur if the Lambda function is throttled, times out, or encounters other unexpected errors, or if the function's response is not in a valid format.
+ We recommend that you configure [provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) for the Lambda function to enable it to scale without fluctuations in latency.
+ If you update your Lambda function, existing connections to the Client VPN endpoint are not affected. You can terminate the existing connections, and then instruct your clients to establish new connections. For more information, see [Terminate an AWS Client VPN client connection](#cvpn-working-connections-disassociate).
+ If clients use the AWS provided client to connect to the Client VPN endpoint, they must use version 1.2.6 or later for Windows, and version 1.2.4 or later for macOS. For more information, see [Connect using the AWS provided client](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/connect-aws-client-vpn-connect.html).

### Lambda interface
<a name="connection-authorization-lambda"></a>

The Lambda function takes device attributes, user attributes, and connection attributes as inputs from the Client VPN service. It must then return a decision to the Client VPN service whether to allow or deny the connection.

**Request schema**  
The Lambda function takes a JSON blob containing the following fields as input.

```
{
    "connection-id": {{<connection ID>}},
    "endpoint-id": {{<client VPN endpoint ID>}},
    "common-name": {{<cert-common-name>}},
    "username": {{<user identifier>}},
    "platform": {{<OS platform>}},
    "platform-version": {{<OS version>}},
    "public-ip": {{<public IP address>}},
    "client-openvpn-version": {{<client OpenVPN version>}},
    "aws-client-version": {{<AWS client version>}},
    "groups": {{<group identifier>}},
    "schema-version": "{{v3}}"
}
```
+ `connection-id` — The ID of the client connection to the Client VPN endpoint.
+ `endpoint-id` — The ID of the Client VPN endpoint.
+ `common-name` — The device identifier. In the client certificate that you create for the device, the common name uniquely identifies the device.
+ `username` — The user identifier, if applicable. For Active Directory authentication, this is the user name. For SAML-based federated authentication, this is `NameID`. For mutual authentication, this field is empty.
+ `platform` — The client operating system platform. 
+ `platform-version` — The version of the operating system. The Client VPN service provides a value when the `--push-peer-info` directive is present in the OpenVPN client configuration when clients connect to a Client VPN endpoint, and when the client is running the Windows platform.
+ `public-ip` — The public IP address of the connecting device.
+ `client-openvpn-version` — The OpenVPN version that the client is using.
+ `aws-client-version` — The AWS client version.
+ `groups` — The group identifier, if applicable. For Active Directory authentication, this will be a list of Active Directory groups. For SAML-based federated authentication, this will be a list of identity provider (IdP) groups. For mutual authentication, this field is empty.
+ `schema-version` — The schema version. The default is `v3`.

**Response schema**  
The Lambda function must return the following fields.

```
{
    "allow": {{boolean}},
    "error-msg-on-denied-connection": "",
    "posture-compliance-statuses": [],
    "schema-version": "{{v3}}"
}
```
+ `allow` — Required. A boolean (`true` \| `false`) that indicates whether to allow or deny the new connection.
+ `error-msg-on-denied-connection` — Required. A string of up to 255 characters that can be used to provide steps and guidance to clients if the connection is denied by the Lambda function. In the event of failures during the running of the Lambda function (for example, due to throttling) the following default message is returned to clients by the Client VPN service.

  ```
  Error establishing connection. Please contact your administrator.
  ```
+ `posture-compliance-statuses` — Required. If you use the Lambda function for [custom connection authorization](#connection-authorization-posture-assessment), this is a list of statuses for the connecting device. You define the status names according to your assessment categories for devices, for example, `compliant`, `quarantined`, `unknown`, and so on. Each name can be up to 255 characters in length. You can specify up to 10 statuses.
+ `schema-version` — Required. The schema version. The default is `v3`.

You can use the same Lambda function for multiple Client VPN endpoints in the same Region.

For more information about creating a Lambda function, see [Getting started with AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html) in the *AWS Lambda Developer Guide*.

### Custom connection authorization
<a name="connection-authorization-posture-assessment"></a>

You can use custom connection authorization to integrate your Client VPN endpoint with your existing device management solution to evaluate the compliance of connecting devices. For the Lambda function to work as a device authorization handler, use [mutual authentication](#mutual) for your Client VPN endpoint. Create a unique client certificate and key for each client (device) that will connect to the Client VPN endpoint. The Lambda function can use the unique common name for the client certificate (that's passed from the Client VPN service) to identify the device and fetch its compliance status from your device management solution. You can use mutual authentication combined with user-based authentication. 

Alternatively, you can do a basic device assessment in the Lambda function itself. For example, you can assess the `platform` and `platform-version` fields that are passed to the Lambda function by the Client VPN service.

**Note**  
While the connection handler can be used to enforce a minimum AWS Client VPN application version, the field `aws-client-version` in the connection handler, is only applicable to the AWS Client VPN application and is being populated from environment variables on the user device.

### Enable the client connect handler
<a name="enable-client-connect-handler"></a>

To enable the client connect handler, create or modify a Client VPN endpoint and specify the Amazon Resource Name (ARN) of the Lambda function. For more information, see [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create) and [Modify an AWS Client VPN endpoint](#cvpn-working-endpoint-modify). 

### Service-linked role
<a name="connection-authorization-slr"></a>

AWS Client VPN automatically creates a service-linked role in your account called **AWSServiceRoleForClientVPNConnections**. The role has permissions to invoke the Lambda function when a connection is made to the Client VPN endpoint. For more information, see [Using service-linked roles for AWS Client VPN](#using-service-linked-roles).

### Monitor connection authorization failures
<a name="connection-authorization-monitoring"></a>

You can view the connection authorization status of connections to the Client VPN endpoint. For more information, see [View AWS Client VPN client connections](#cvpn-working-connections-view).

When using custom connection authorization, you can also view the compliance statuses of devices that connect to your Client VPN endpoint in the connection logs. For more information, see [Connection logging for an AWS Client VPN endpoint](#connection-logging). 

If a device fails connection authorization, the `connection-attempt-failure-reason` field in the connection logs returns one of the following failure reasons:
+ `client-connect-failed` — The Lambda function prevented the connection from being established.
+ `client-connect-handler-timed-out` — The Lambda function timed out.
+ `client-connect-handler-other-execution-error` — The Lambda function encountered an unexpected error.
+ `client-connect-handler-throttled` — The Lambda function was throttled.
+ `client-connect-handler-invalid-response` — The Lambda function returned a response that was not valid.
+ `client-connect-handler-service-error` — There was a service-side error during the connection attempt.

## Split-tunnel on AWS Client VPN endpoints
<a name="split-tunnel-vpn"></a>

By default, when you have a Client VPN endpoint, all traffic from clients is routed over the Client VPN tunnel. When you enable split-tunnel on the Client VPN endpoint, we push the routes on the [Client VPN endpoint route table](#cvpn-working-routes) to the device that is connected to the Client VPN endpoint. This ensures that only traffic with a destination to the network matching a route from the Client VPN endpoint route table is routed over the Client VPN tunnel. 

You can use a split-tunnel Client VPN endpoint when you do not want all user traffic to route through the Client VPN endpoint. 

In the following example, split-tunnel is enabled on the Client VPN endpoint. Only traffic that's destined for the VPC (`172.31.0.0/16`) is routed over the Client VPN tunnel. Traffic that's destined for on-premises resources is not routed over the Client VPN tunnel.

![Split-tunnel Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/client-vpn-split-tunnel.png)


### Split-tunnel benefits
<a name="split-tunnel-benefits"></a>

Split-tunnel on Client VPN endpoints offers the following benefits:
+ You can optimize the routing of traffic from clients by having only the AWS destined traffic traverse the VPN tunnel.
+ You can reduce the volume of outgoing traffic from AWS, therefore reducing the data transfer cost.

### Routing considerations
<a name="split-tunnel-routing"></a>
+ When you enable split-tunnel mode, all of the routes in the Client VPN endpoint's route table are added to the client's route table when the VPN connection is established. This operation is different from the default behavior, which overwrites the client's route table with the entry `0.0.0.0/0` to route all traffic over the VPN.
**Note**  
Adding a 0.0.0.0/0 route to the Client VPN endpoint's route table when using split-tunnel mode may cause connectivity disruption and is not recommended
+ When split-tunnel mode is enabled, any modification to the Client VPN endpoint route table will result in all client connections being reset.

### Enabling split-tunnel
<a name="split-tunnel-enable"></a>

You can enable split-tunnel on a new or existing Client VPN endpoint. For more information, see the following topics:
+ [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create)
+ [Modify an AWS Client VPN endpoint](#cvpn-working-endpoint-modify)

## Connection logging for an AWS Client VPN endpoint
<a name="connection-logging"></a>

Connection logging is a feature of AWS Client VPN that enables you to capture *connection logs* for your Client VPN endpoint. 

A connection log contains *connection log entries* that capture information about connection events, such as when a client (end user) connects, attempts to connect, or disconnects from your Client VPN endpoint. You can use this information to run forensics, analyze how your Client VPN endpoint is being used, or debug connection issues.

Connection logging is available in all Regions where AWS Client VPN is available. Connection logs are published to a CloudWatch Logs log group in your account.

**Note**  
Failed mutual authentication attempts are not logged.

### Connection log entries
<a name="connection-log-entries"></a>

A connection log entry is a JSON-formatted blob of key-value pairs. The following is an example connection log entry.

```
{
    "connection-log-type": "connection-attempt",
    "connection-attempt-status": "successful",
    "connection-reset-status": "NA",
    "connection-attempt-failure-reason": "NA",
    "connection-id": "cvpn-connection-abc123abc123abc12",
    "client-vpn-endpoint-id": "cvpn-endpoint-aaa111bbb222ccc33",
    "transport-protocol": "udp",
    "connection-start-time": "2020-03-26 20:37:15",
    "connection-last-update-time": "2020-03-26 20:37:15",
    "client-ip": "10.0.1.2",
    "common-name": "client1",
    "device-type": "mac",
    "device-ip": "98.247.202.82",
    "port": "50096",
    "ingress-bytes": "0",
    "egress-bytes": "0",
    "ingress-packets": "0",
    "egress-packets": "0",
    "connection-end-time": "NA",
    "username": "joe"
    }
```

A connection log entry contains the following keys:
+ `connection-log-type` — The type of connection log entry (`connection-attempt` or `connection-reset`).
+ `connection-attempt-status` — The status of the connection request (`successful`, `failed`, `waiting-for-assertion`, or `NA`).
+ `connection-reset-status` — The status of a connection reset event (`NA` or `assertion-received`).
+ `connection-attempt-failure-reason` — The reason for the connection failure, if applicable. When the authorization policy denies a connection, the value is `authorization-policy-deny`.
+ `connection-id` — The ID of the connection.
+ `client-vpn-endpoint-id` — The ID of the Client VPN endpoint to which the connection was made.
+ `transport-protocol` — The transport protocol that was used for the connection.
+ `connection-start-time` — The start time of the connection.
+ `connection-last-update-time` — The last update time of the connection. This value is periodically updated in the logs.
+ `client-ip` — The IP address of the client, which is allocated from the client IPv4 CIDR range for the Client VPN endpoint.
+ `common-name` — The common name of the certificate that's used for certificate-based authentication.
+ `device-type` — The type of device used for the connection by the end user.
+ `device-ip` — The public IP address of the device.
+ `port` — The port number for the connection.
+ `ingress-bytes` — The number of ingress (inbound) bytes for the connection. This value is periodically updated in the logs.
+ `egress-bytes` — The number of egress (outbound) bytes for the connection. This value is periodically updated in the logs.
+ `ingress-packets` — The number of ingress (inbound) packets for the connection. This value is periodically updated in the logs.
+ `egress-packets` — The number of egress (outbound) packets for the connection. This value is periodically updated in the logs.
+ `connection-end-time` — The end time of the connection. The value is `NA` if the connection is still in progress or if the connection attempt failed.
+ `posture-compliance-statuses` — The compliance statuses returned by the [client connect handler](#connection-authorization) for [custom connection authorization](#connection-authorization-posture-assessment), if applicable.
+ `authorization-policy-evaluation` — The result of evaluating the authorization policy, if an authorization policy is configured. This value contains the following subfields:
  + `result` — The authorization decision (`permit`, `deny`, or `error`). An `error` result can occur when a Cedar policy references an attribute that is absent from the connection context, among other reasons. For example, the client doesn't provide a device token and the policy references that provider's context. An error can also occur when the policy references a SAML or AD attribute that isn't present for the user. When shadow mode is `disabled`, Client VPN denies the connection.
  + `evaluation-type` — The type of evaluation (`connection-attempt` or `periodic`). A `connection-attempt` evaluation occurs when the client connects. A `periodic` evaluation occurs during a re-evaluation of an active session.
  + `shadow-mode` — A string that indicates the shadow mode setting (`enabled` or `disabled`). When `enabled`, Client VPN evaluates the policy without enforcing the decision. When `disabled`, Client VPN enforces `deny` and `error` decisions.
  + `reason` — The reason for the authorization decision. This field is present only for `deny` and `error` results. The current emitted value is `policy-deny`.
  + `device-token-status` — An object that contains the device token status for each device trust provider. Each provider entry contains a `status` subfield (`validated` or `failed`). If the status is `failed`, the entry also includes a `reason` subfield that describes the failure.
  + `context` — The full authorization policy evaluation context. This subfield is included only when `IncludeAuthorizationPolicyContext` is enabled.
+ `username` — The username is recorded when user-based authentication (AD or SAML) is used for the endpoint.
+ `connection-duration-seconds` — The duration of a connection in seconds. Equal to the difference between "connection-start-time" and "connection-end-time".

For more information about enabling connection logging, see [AWS Client VPN connection logs](#cvpn-working-with-connection-logs).

When you enable connection logging for a new or existing endpoint, you can set `IncludeAuthorizationPolicyContext` to include the full authorization policy evaluation context in your connection log entries. For more information, see [Connection logging options](#connection-log-options).

### Device token status failure reasons
<a name="device-token-status-failure-reasons"></a>

When the `status` of a `device-token-status` provider entry is `failed`, the entry includes a `reason` subfield. The `reason` subfield can have one of the following values.
+ `token-expired`
+ `signature-invalid`
+ `token-malformed`
+ `tenant-mismatch`
+ `key-resolution-failed`
+ `network-error`
+ `internal-error`

### Connection logging options
<a name="connection-log-options"></a>

You can configure the following option to control the content of your connection logs:
+ `IncludeAuthorizationPolicyContext` — When `true`, connection log entries include the full authorization policy evaluation context. The default is `false`.

### Authorization policy connection log examples
<a name="connection-log-examples-device-posture"></a>

When an authorization policy is configured, connection log entries record the authorization decision. The following example shows a successful connection that was permitted by the authorization policy.

```
{
  "connection-log-type": "connection-attempt",
  "connection-attempt-status": "successful",
  "connection-attempt-failure-reason": "NA",
  "connection-id": "cvpn-connection-01f248f0e3084e4f2",
  "client-vpn-endpoint-id": "cvpn-endpoint-0f2d58d4869ece501",
  "transport-protocol": "udp",
  "connection-start-time": "2026-09-24 22:22:25",
  "connection-last-update-time": "2026-09-24 22:22:25",
  "client-ip": "172.1.0.162",
  "client-ip-v6": "NA",
  "common-name": "client1.domain.tld",
  "device-type": "linux",
  "device-ip": "72.21.198.66",
  "port": "5567",
  "ingress-bytes": "0",
  "egress-bytes": "0",
  "ingress-packets": "0",
  "egress-packets": "0",
  "authorization-policy-evaluation": {
    "result": "permit",
    "evaluation-type": "connection-attempt",
    "shadow-mode": "disabled",
    "device-token-status": {
      "crowdstrike": {
        "status": "validated"
      }
    }
  },
  "connection-end-time": "NA",
  "connection-duration-seconds": "0"
}
```

The following example shows a connection that was denied by the authorization policy.

```
{
  "connection-log-type": "connection-attempt",
  "connection-attempt-status": "failed",
  "connection-attempt-failure-reason": "authorization-policy-deny",
  "connection-id": "cvpn-connection-0a39f1b3b7082abbb",
  "client-vpn-endpoint-id": "cvpn-endpoint-0f2d58d4869ece501",
  "transport-protocol": "udp",
  "connection-start-time": "NA",
  "connection-last-update-time": "2026-09-25 17:14:11",
  "client-ip": "NA",
  "client-ip-v6": "NA",
  "common-name": "client1.domain.tld",
  "device-type": "linux",
  "device-ip": "72.21.198.66",
  "port": "28081",
  "ingress-bytes": "0",
  "egress-bytes": "0",
  "ingress-packets": "0",
  "egress-packets": "0",
  "authorization-policy-evaluation": {
    "result": "error",
    "evaluation-type": "connection-attempt",
    "shadow-mode": "disabled",
    "reason": "policy-deny",
    "device-token-status": {
      "crowdstrike": {
        "status": "failed",
        "reason": "token-malformed"
      }
    }
  },
  "connection-end-time": "NA",
  "connection-duration-seconds": "NA"
}
```

The following example shows a session that was terminated when a periodic re-evaluation of the authorization policy no longer met the requirements.

```
{
  "connection-log-type": "connection-reset",
  "connection-attempt-status": "NA",
  "connection-attempt-failure-reason": "NA",
  "connection-id": "cvpn-connection-01f248f0e3084e4f2",
  "client-vpn-endpoint-id": "cvpn-endpoint-0f2d58d4869ece501",
  "transport-protocol": "udp",
  "connection-start-time": "2026-09-24 22:22:25",
  "connection-last-update-time": "2026-09-24 22:27:43",
  "client-ip": "172.1.0.162",
  "client-ip-v6": "NA",
  "common-name": "client1.domain.tld",
  "device-type": "linux",
  "device-ip": "72.21.198.66",
  "port": "5567",
  "ingress-bytes": "21017",
  "egress-bytes": "16438",
  "ingress-packets": "330",
  "egress-packets": "325",
  "authorization-policy-evaluation": {
    "result": "deny",
    "evaluation-type": "periodic",
    "shadow-mode": "disabled",
    "reason": "policy-deny",
    "device-token-status": {
      "crowdstrike": {
        "status": "validated"
      }
    }
  },
  "connection-end-time": "2026-09-24 22:27:43",
  "connection-reset-status": "NA",
  "connection-duration-seconds": "318"
}
```

## Client VPN scaling considerations
<a name="scaling-considerations"></a>

When you create a Client VPN endpoint, consider the maximum number of concurrent VPN connections that you plan to support. You should take into account the number of clients that you currently support, and whether your Client VPN endpoint can scale to meet additional demand if needed. 

The following factors affect the maximum number of concurrent VPN connections that can be supported on a Client VPN endpoint:

**Client CIDR range size**  
When you [create a Client VPN endpoint](#cvpn-working-endpoint-create), you must specify a client CIDR range, which is an IPv4 CIDR block between a /12 and /22 netmask. Each VPN connection to the Client VPN endpoint is assigned a unique IP address from the client CIDR range. A portion of the addresses in the client CIDR range are also used to support the availability model of the Client VPN endpoint, and cannot be assigned to clients. You cannot change the client CIDR range after you create the Client VPN endpoint.  
In general, we recommend that you specify a client CIDR range that contains twice the number of IP addresses (and therefore concurrent connections) that you plan to support on the Client VPN endpoint. 

**Number of associated subnets**  
When you [associate a subnet](#cvpn-working-target) with a Client VPN endpoint, you enable users to establish VPN sessions to the Client VPN endpoint. You can associate multiple subnets with a Client VPN endpoint for high availability, and to enable additional connection capacity.   
The following are the number of supported concurrent VPN connections based on the number of subnet associations for the Client VPN endpoint.  


<table>
<thead>
  <tr><th>Subnet associations</th><th>Supported number of connections</th></tr>
</thead>
<tbody>
  <tr><td>1</td><td>7,000</td></tr>
  <tr><td>2</td><td>36,500</td></tr>
  <tr><td>3</td><td>66,500</td></tr>
  <tr><td>4</td><td>96,500</td></tr>
  <tr><td>5</td><td>126,000</td></tr>
</tbody>
</table>


You cannot associate multiple subnets from the same Availability Zone with a Client VPN endpoint. Therefore, the number of subnet associations also depends on the number of Availability Zones that are available in an AWS Region.

For example, if you expect to support 8,000 VPN connections to your Client VPN endpoint, specify a minimum client CIDR range size of `/18` (16,384 IP addresses), and associate at least 2 subnets with the Client VPN endpoint.

If you’re unsure what the number of expected VPN connections is for your Client VPN endpoint, we recommend that you specify a size `/16` CIDR block or larger.

For more information about the rules and limitations for working with client CIDR ranges and target networks, see [Rules and best practices for using AWS Client VPN](#what-is-best-practices).

For more information about quotas for your Client VPN endpoint, see [AWS Client VPN quotas](#limits).

# Get started with AWS Client VPN
<a name="cvpn-getting-started"></a>

In this tutorial, you will create a AWS Client VPN endpoint that does the following:
+ Provides all clients with access to a single VPC.
+ Provides all clients with access to the internet.
+ Uses [mutual authentication](#mutual).

The following diagram represents the configuration of your VPC and Client VPN endpoint after you've completed this tutorial.

![Client VPN accessing the internet](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/client-vpn-scenario-igw.png)


**Topics**
+ [Prerequisites](#cvpn-getting-started-prereq)
+ [Step 1: Choose your endpoint type](#cvpn-getting-started-choose-type)
+ [Step 2: Generate server and client certificates and keys](#cvpn-getting-started-certs)
+ [Step 3: Create a Client VPN endpoint](#cvpn-getting-started-endpoint)
+ [Step 4: Associate a target network](#cvpn-getting-started-target)
+ [Step 5: Add an authorization rule for the VPC](#cvpn-getting-started-rules)
+ [Step 6: Provide access to the internet](#cvpn-getting-started-routes)
+ [Step 7: Verify security group requirements](#cvpn-getting-started-sec-groups)
+ [Step 8: Download the Client VPN endpoint configuration file](#cvpn-getting-started-config)
+ [Step 9: Connect to the Client VPN endpoint](#cvpn-getting-started-connect)

## Prerequisites
<a name="cvpn-getting-started-prereq"></a>

Before you begin this getting started tutorial, make sure that you have the following:
+ The permissions required to work with Client VPN endpoints.
+ The permissions required to import certificates into AWS Certificate Manager.
+ A VPC with at least one subnet and an internet gateway. The route table that's associated with your subnet must have a route to the internet gateway.

## Step 1: Choose your endpoint type
<a name="cvpn-getting-started-choose-type"></a>

Client VPN supports two endpoint types: VPC subnet association for single-VPC access, and Transit Gateway association for multi-VPC and hybrid network scenarios. This tutorial covers VPC-associated endpoints. For Transit Gateway endpoints, see [Transit Gateway integration with Client VPN](#cvpn-tgw).

## Step 2: Generate server and client certificates and keys
<a name="cvpn-getting-started-certs"></a>

This tutorial uses mutual authentication. With mutual authentication, Client VPN uses certificates to perform authentication between clients and the Client VPN endpoint. You will need to have a server certificate and key, and at least one client certificate and key. At minimum, the server certificate will need to be imported into AWS Certificate Manager (ACM) and specified when you create the Client VPN endpoint. Importing the client certificate into ACM is optional.

If you don't already have certificates to use for this purpose, they can be created using the OpenVPN easy-rsa utility. For detailed steps to generate the server and client certificates and keys using the [OpenVPN easy-rsa utility](https://github.com/OpenVPN/easy-rsa), and import them into ACM see [Mutual authentication in AWS Client VPN](#mutual).

**Note**  
The server certificate must be provisioned with or imported into AWS Certificate Manager (ACM) in the same AWS Region where you'll create the Client VPN endpoint.

## Step 3: Create a Client VPN endpoint
<a name="cvpn-getting-started-endpoint"></a>

The Client VPN endpoint is the resource that you create and configure to enable and manage client VPN sessions. It's the termination point for all client VPN sessions.

**To create a Client VPN endpoint**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints** and then choose **Create Client VPN endpoint**.

1. (Optional) Provide a name tag and description for the Client VPN endpoint.

1. For **Client IPv4 CIDR**, specify an IP address range, in CIDR notation, from which to assign client IP addresses.
**Note**  
The address range cannot overlap with the target network address range, the VPC address range, or any of the routes that will be associated with the Client VPN endpoint. The client address range must be at minimum /22 and not greater than /12 CIDR block size. You cannot change the client address range after you create the Client VPN endpoint.

1. For **Server certificate ARN**, select the ARN of the server certificate that you generated in [Step 2](#cvpn-getting-started-certs).

1. Under **Authentication options**, choose **Use mutual authentication**, and then for **Client certificate ARN**, select the ARN of the certificate you want to use as the client certificate.

   If the server and client certificates are signed by the same certificate authority (CA), you have the option of specifying the server certificate ARN for *both* the client and server certificates. In this scenario, any client certificate that corresponds with the server certificate can be used to authenticate.
**Note**  
To require device health checks on this endpoint, configure device posture options with one or more device trust providers when you create the endpoint. See [Device posture for AWS Client VPN](#device-posture).

1. (Optional) Specify which DNS servers to use for DNS resolution. To use custom DNS servers, for **DNS Server 1 IP address** and **DNS Server 2 IP address**, specify the IP addresses of the DNS servers to use. To use VPC DNS server, for either **DNS Server 1 IP address** or **DNS Server 2 IP address**, specify the IP addresses, and add the VPC DNS server IP address.
**Note**  
Verify that the DNS servers can be reached by clients.

1. Keep the rest of the default settings, and choose **Create Client VPN endpoint**.

After you create the Client VPN endpoint, its state is `pending-associate`. Clients can only establish a VPN connection after you associate at least one target network.

For more information about the options that you can specify for a Client VPN endpoint, see [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create).

## Step 4: Associate a target network
<a name="cvpn-getting-started-target"></a>

To allow clients to establish a VPN session, you associate a target network with the Client VPN endpoint. A target network is a subnet in a VPC. 

**To associate a target network with the Client VPN endpoint**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint that you created in the preceding procedure, and then choose **Target network associations**, **Associate target network**.

1. For **VPC**, choose the VPC in which the subnet is located. 

1. For **Choose a subnet to associate**, choose the subnet to associate with the Client VPN endpoint.

1. Choose **Associate target network**.

1. If authorization rules allow it, one subnet association is enough for clients to access a VPC's entire network. You can associate additional subnets to provide high availability in case an Availability Zones becomes impaired.

When you associate the first subnet with the Client VPN endpoint, the following happens:
+ The state of the Client VPN endpoint changes to `available`. Clients can now establish a VPN connection, but they cannot access any resources in the VPC until you add the authorization rules.
+ The local route of the VPC is automatically added to the Client VPN endpoint route table. 
+ The VPC's default security group is automatically applied for the Client VPN endpoint.

## Step 5: Add an authorization rule for the VPC
<a name="cvpn-getting-started-rules"></a>

For clients to access the VPC, there needs to be a route to the VPC in the Client VPN endpoint's route table and an authorization rule. The route was already added automatically in the previous step. For this tutorial, we want to grant all users access to the VPC.

**To add an authorization rule for the VPC**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to which to add the authorization rule. Choose **Authorization rules**, and then choose **Add authorization rule**.

1. For **Destination network to enable access**, enter the CIDR of the network for which you want to allow access. For example, to allow access to the entire VPC, specify the IPv4 CIDR block of the VPC.

1. For **Grant access to**, choose **Allow access to all users**.

1. (Optional) For **Description**, enter a brief description of the authorization rule.

1. Choose **Add authorization rule**.

## Step 6: Provide access to the internet
<a name="cvpn-getting-started-routes"></a>

You can provide access to additional networks connected to the VPC, such as AWS services, peered VPCs, on-premises networks, and the internet. For each additional network, you add a route to the network in the Client VPN endpoint's route table and configure an authorization rule to give clients access.

For this tutorial, we want to grant all users access to the internet and also to the VPC. You've already configured access to the VPC, so this step is for access to the internet.

**To provide access to the internet**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint that you created for this tutorial. Choose **Route Table**, and then choose **Create Route**.

1. For **Route destination**, enter `0.0.0.0/0`. For **Subnet ID for target network association**, specify the ID of the subnet through which to route traffic.

1. Choose **Create Route**.

1. Choose **Authorization rules**, and then choose **Add authorization rule**.

1. For **Destination network to enable access**, enter `0.0.0.0/0`, and choose **Allow access to all users**.

1. Choose **Add authorization rule**.

## Step 7: Verify security group requirements
<a name="cvpn-getting-started-sec-groups"></a>

In this tutorial, no security groups were specified during the creation of the Client VPN endpoint in Step 3. That means that the default security group for the VPC is automatically applied to the Client VPN endpoint when a target network is associated. As a result, the default security group for the VPC should now be associated with the Client VPN endpoint.

**Verify the following security group requirements**
+ That the security group associated with subnet you are routing traffic through (in this case the default VPC security group) allows outbound traffic to the internet. To do this, add an outbound rule that allows all traffic to destination `0.0.0.0/0`.
+ That the security groups for the resources in your VPC have a rule that allows access from the security group that's applied to the Client VPN endpoint (in this case the default VPC security group). This enables your clients to access the resources in your VPC. 

For more information, see [Security groups](#security-groups).

## Step 8: Download the Client VPN endpoint configuration file
<a name="cvpn-getting-started-config"></a>

The next step is to download and prepare the Client VPN endpoint configuration file. The configuration file includes the Client VPN endpoint details and certificate information required to establish a VPN connection. You provide this file to the end users who need to connect to the Client VPN endpoint. The end user uses the file to configure their VPN client application. 

**To download and prepare the Client VPN endpoint configuration file**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint that you created for this tutorial, and choose **Download client configuration**.

1. Locate the client certificate and key that were generated in [Step 2](#cvpn-getting-started-certs). The client certificate and key can be found in the following locations in the cloned OpenVPN easy-rsa repo: 
   + Client certificate — `easy-rsa/easyrsa3/pki/issued/client1.domain.tld.crt`
   + Client key — `easy-rsa/easyrsa3/pki/private/client1.domain.tld.key`

1. Open the Client VPN endpoint configuration file using your preferred text editor. Add `<cert>``</cert>` and `<key>``</key>` tags to the file. Place the contents of the client certificate and the contents of the private key between the corresponding tags, as such:

   ```
   <cert>
   {{Contents of client certificate (.crt) file}}
   </cert>
   
   <key>
   {{Contents of private key (.key) file}}
   </key>
   ```

1. Save and close the Client VPN endpoint configuration file.

1. Distribute the Client VPN endpoint configuration file to your end users.

For more information about the Client VPN endpoint configuration file, see [AWS Client VPN endpoint configuration file export](#cvpn-working-endpoint-export).

## Step 9: Connect to the Client VPN endpoint
<a name="cvpn-getting-started-connect"></a>

You can connect to the Client VPN endpoint using the AWS provided client or another OpenVPN-based client application and the configuration file that you just created. For more information, see the [AWS Client VPN User Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/).

# Work with AWS Client VPN
<a name="cvpn-working"></a>

The following topics explain the primary administrative tasks needed to work with Client VPN:
+ **Access the self-service portal** — Configure access to the Client VPN self-service portal so that clients can download the Client VPN endpoint configuration file themselves. For information on accessing the self-service portal, see [AWS Client VPN access to the self-service portal](#cvpn-self-service-portal).
+ **Authorization rules** — Add authorization rules to control client access to specified networks. For information on adding authorization rules, see [AWS Client VPN authorization rules](#cvpn-working-rules).
+ **Authorization policies** — Define Cedar-based authorization policies that control connections based on device posture, user identity, and connection details. For information about authorization policies, see [Authoring device posture authorization policies](#device-posture-policies).
+ **Client certificate revocation lists** — Use client certificate revocation lists to revoke access to a Client VPN endpoint. For information about client certificate revocation lists, see [AWS Client VPN client certificate revocation lists](#cvpn-working-certificates).
+ **Client connections** — View or terminate a client connection to a Client VPN endpoint. For information about viewing or terminating a client connection, see [AWS Client VPN client connections](#cvpn-working-connections).
+ **Client login banner** — Add a text banner on a Client VPN desktop application when a VPN session is established. You can use the text banner to meet your regulatory and compliance needs. For information about login banners, see [AWS Client VPN client login banners](#cvpn-working-login-banner).
+ **Client Route Enforcement** — Enforce administrator-defined routes on devices connected through the VPN. For more information about Client Route Enforcement, see [AWS Client VPN Client Route Enforcement](#cvpn-working-cre). 
+ **Client VPN endpoints** — Configure Client VPN endpoints to manage and control all VPN sessions. For information about configuring endpoints, see [AWS Client VPN endpoints](#cvpn-working-endpoints).
+ **Connection logs** — Enable connection logging for new or existing Client VPN endpoints to start capturing connection logs. For information about connection logging, see [AWS Client VPN connection logs](#cvpn-working-with-connection-logs).
+ **Client configuration file export** — Configure the client configuration file that Client VPN clients need in order to establish VPN connections. After configuring the file, download (export) it for distribution to clients. For more information about exporting a client configuration file, see [AWS Client VPN endpoint configuration file export](#cvpn-working-endpoint-export).
+ **Routes** — Add routes to enable access to additional destination networks. For information about configuring routes, see [AWS Client VPN routes](#cvpn-working-routes).
+ **Target networks** — Associate VPC subnets or attach directly to an AWS Transit Gateway to enable clients to connect and establish a VPN connection. For information about target networks, see [AWS Client VPN target networks](#cvpn-working-target). For information about Transit Gateway integration, see [Transit Gateway integration with Client VPN](#cvpn-tgw).
+ **Maximum VPN session duration** — Set options for maximum VPN session duration to meet your security and compliance requirements. For information about maximum VPN session duration, see [AWS Client VPN maximum VPN session duration timeout](#cvpn-working-max-duration).

## AWS Client VPN access to the self-service portal
<a name="cvpn-self-service-portal"></a>

If you enabled the self-service portal for your Client VPN endpoint, you can provide your clients with a self-service portal URL. Clients can access the portal in a web browser, and use their user-based credentials to log in. In the portal, clients can download the Client VPN endpoint configuration file and they can download the latest version of the AWS provided client.

The following rules apply:
+ The self-service portal is not available for clients that authenticate using mutual authentication.
+ The configuration file that's available in the self-service portal is the same configuration file that you export using the Amazon VPC console or AWS CLI. If you need to customize the configuration file before distributing it to clients, you must distribute the customized file to clients yourself.
+ You must enable the self-service portal option for your Client VPN endpoint, or clients cannot access the portal. If this option is not enabled, you can modify your Client VPN endpoint to enable it.

After you have enabled the self-service portal option, provide your clients with one of the following URLs:
+ `https://self-service.clientvpn.amazonaws.com/`

  If clients access the portal using this URL, they must enter the ID of the Client VPN endpoint before they can log in.
+ `https://self-service.clientvpn.amazonaws.com/endpoints/{{<endpoint-id>}}`

  Replace {{<endpoint-id>}} in the preceding URL with the ID of your Client VPN endpoint, for example, `cvpn-endpoint-0123456abcd123456`.

You can also view the URL for the self-service portal in the output of the [describe-client-vpn-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-endpoints.html) AWS CLI command. Alternatively, the URL is available in the **Details** tab on the **Client VPN Endpoints** page in the Amazon VPC console.

For more information about configuring the self-service portal for use with federated authentication, see [Support for the self-service portal](#saml-self-service-support).

## AWS Client VPN authorization rules
<a name="cvpn-working-rules"></a>

Authorization rules act as ﬁrewall rules that grant access to networks. By adding authorization rules, you grant specific clients access to the specified network. You should have an authorization rule for each network you want to grant access to. You can add authorization rules to a Client VPN endpoint using the console and the AWS CLI.

**Note**  
Client VPN uses longest prefix matching when evaluating authorization rules. See the troubleshooting topic [Troubleshooting AWS Client VPN: Authorization rules for Active Directory groups not working as expected](#ad-group-auth-rules) and [Route priority](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#route-tables-priority) in the *Amazon VPC User Guide* for more details.

### Key points for understanding authorization rules
<a name="key-points-summary"></a>

The following points explain some of the behavior of authorization rules:
+ To allow access to a destination network, an authorization rule must be explicitly added. The default behavior is to deny access.
+ You cannot add an authorization rule to *restrict* access to a destination network.
+ The `0.0.0.0/0` CIDR is handled as a special case. It is processed last, regardless of the order in which the authorization rules were created.
+ The `0.0.0.0/0` CIDR can be thought of as "any destination," or "any destination not defined by other authorization rules."
+ The longest prefix match is the rule that takes precedence.

**Topics**
+ [Key points](#key-points-summary)
+ [Example scenarios](#auth-rule-example-scenarios)
+ [Add an authorization rule](#cvpn-working-rule-authorize-add)
+ [Remove an authorization rule](#cvpn-working-rule-remove)
+ [View authorization rules](#cvpn-working-rule-view)

### Example scenarios for Client VPN authorization rules
<a name="auth-rule-example-scenarios"></a>

This section describes how authorization rules work for AWS Client VPN. It includes key points for understanding authorization rules, an example architecture, and discussion of example scenarios that map to the example architecture.

**Scenarios**
+ [Example architecture for authorization rule scenarios](#example-arch-auth-rules)
+ [Access to a single destination](#auth-rules1)
+ [Use any destination (0.0.0.0/0) CIDR](#auth-rules2)
+ [Longer IP prefix match](#auth-rules3)
+ [Overlapping CIDR (same group)](#auth-rules4)
+ [Additional 0.0.0.0/0 rule](#auth-rules5)
+ [Add a rule for 192.168.0.0/24](#auth-rules6)
+ [SAML federated authentication](#auth-rules7)
+ [Access for all user groups](#auth-rules8)

#### Example architecture for authorization rule scenarios
<a name="example-arch-auth-rules"></a>

The following diagram shows the example architecture that is used for the example scenarios found in this section.

![Example Client VPN architecture](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/cvpn-auth-rules.png)


#### Access to a single destination
<a name="auth-rules1"></a>


| Rule description | Group ID | Allow access to all users | Destination CIDR | 
| --- | --- | --- | --- | 
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 | 
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 | 
| Provide manager group access to Client VPN VPC | S-xxxxx16 | False | 192.168.0.0/24 | 

**Resulting behavior**
+ The engineering group can access only `172.16.0.0/24`.
+ The development group can access only `10.0.0.0/16`.
+ The manager group can access only `192.168.0.0/24`.
+ All other traffic is dropped by the Client VPN endpoint.

**Note**  
In this scenario, no user group has access to the public internet.

#### Use any destination (0.0.0.0/0) CIDR
<a name="auth-rules2"></a>


| Rule description | Group ID | Allow access to all users | Destination CIDR | 
| --- | --- | --- | --- | 
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 | 
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 | 
| Provide manager group access to any destination | S-xxxxx16 | False | 0.0.0.0/0 | 

**Resulting behavior**
+ The engineering group can access only `172.16.0.0/24`.
+ The development group can access only `10.0.0.0/16`.
+ The manager group can access the public internet *and* `192.168.0.0/24`, but cannot access `172.16.0.0/24` or `10.0.0/16`.

**Note**  
In this scenario, because no rules are referencing `192.168.0.0/24`, access to that network is also provided by the `0.0.0.0/0` rule.  
A rule containing `0.0.0.0/0` is always evaluated last regardless of the order in which the rules were created. Because of this, keep in mind that the rules evaluated before `0.0.0.0/0` play a role in determining which networks `0.0.0.0/0` grants access to.

#### Longer IP prefix match
<a name="auth-rules3"></a>


| Rule description | Group ID | Allow access to all users | Destination CIDR | 
| --- | --- | --- | --- | 
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 | 
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 | 
| Provide manager group access to any destination | S-xxxxx16 | False | 0.0.0.0/0 | 
| Provide manager group access to a single host in development VPC | S-xxxxx16 | False | 10.0.2.119/32 | 

**Resulting behavior**
+ The engineering group can access only `172.16.0.0/24`.
+ The development group can access `10.0.0.0/16`, *except* for the single host `10.0.2.119/32`.
+ The manager group can access the public internet, `192.168.0.0/24`, and a single host (`10.0.2.119/32`) within the development VPC, but does not have access to `172.16.0.0/24` or any of the remaining hosts in the development VPC.

**Note**  
Here you see how a rule with a longer IP prefix takes precedence over a rule with a shorter IP prefix. If you want the development group to have access to `10.0.2.119/32`, an additional rule granting the development team access to `10.0.2.119/32` needs to be added.

#### Overlapping CIDR (same group)
<a name="auth-rules4"></a>


| Rule description | Group ID | Allow access to all users | Destination CIDR | 
| --- | --- | --- | --- | 
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 | 
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 | 
| Provide manager group access to any destination | S-xxxxx16 | False | 0.0.0.0/0 | 
| Provide manager group access to single host in development VPC | S-xxxxx16 | False | 10.0.2.119/32 | 
| Provide engineering group access to a smaller subnet within on-premises network | S-xxxxx14 | False | 172.16.0.128/25 | 

**Resulting behavior**
+ The development group can access `10.0.0.0/16`, *except* for the single host `10.0.2.119/32`.
+ The manager group can access the public internet, `192.168.0.0/24`, and a single host (`10.0.2.119/32`) within the `10.0.0.0/16` network, but does not have access to `172.16.0.0/24` or any of the remaining hosts in the `10.0.0.0/16` network.
+ The engineering group has access to `172.16.0.0/24`, including the more specific subnet `172.16.0.128/25`.

#### Additional 0.0.0.0/0 rule
<a name="auth-rules5"></a>


| Rule description | Group ID | Allow access to all users | Destination CIDR | 
| --- | --- | --- | --- | 
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 | 
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 | 
| Provide manager group access to any destination | S-xxxxx16 | False | 0.0.0.0/0 | 
| Provide manager group access to single host in development VPC | S-xxxxx16 | False | 10.0.2.119/32 | 
| Provide engineering group access to a smaller subnet within on-premises network | S-xxxxx14 | False | 172.16.0.128/25 | 
| Provide engineering group access to any destination | S-xxxxx14 | False | 0.0.0.0/0 | 

**Resulting behavior**
+ The development group can access `10.0.0.0/16`, *except* for the single host `10.0.2.119/32`.
+ The manager group can access the public internet, `192.168.0.0/24`, and a single host (`10.0.2.119/32`) within the `10.0.0.0/16` network, but does not have access to `172.16.0.0/24` or any of the remaining hosts in the `10.0.0.0/16` network.
+ The engineering group can access the public internet, `192.168.0.0/24`, and `172.16.0.0/24`, including the more specific subnet `172.16.0.128/25`.

**Note**  
Notice that both the engineering and manager groups can now access `192.168.0.0/24`. This is because both groups have access to `0.0.0.0/0` (any destination) *and* no other rules are referencing `192.168.0.0/24`.

#### Add a rule for 192.168.0.0/24
<a name="auth-rules6"></a>


| Rule description | Group ID | Allow access to all users | Destination CIDR | 
| --- | --- | --- | --- | 
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 | 
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 | 
| Provide manager group access to any destination | S-xxxxx16 | False | 0.0.0.0/0 | 
| Provide manager group access to single host in development VPC | S-xxxxx16 | False | 10.0.2.119/32 | 
| Provide engineering group access to a subnet in the on-premises network | S-xxxxx14 | False | 172.16.0.128/25 | 
| Provide engineering group access to any destination | S-xxxxx14 | False | 0.0.0.0/0 | 
| Provide manager group access to Client VPN VPC | S-xxxxx16 | False | 192.168.0.0/24 | 

**Resulting behavior**
+ The development group can access `10.0.0.0/16`, *except* for the single host `10.0.2.119/32`.
+ The manager group can access the public internet, `192.168.0.0/24`, and a single host (`10.0.2.119/32`) within the `10.0.0.0/16` network, but does not have access to `172.16.0.0/24` or any of the remaining hosts in the `10.0.0.0/16` network.
+ The engineering group can access the public internet, `172.16.0.0/24`, and `172.16.0.128/25`.

**Note**  
Notice how adding the rule for the manager group to access `192.168.0.0/24` results in the development group no longer having access to that destination network.

#### SAML federated authentication
<a name="auth-rules7"></a>


| Rule description | Group ID | Allow access to all users | Destination CIDR | 
| --- | --- | --- | --- | 
| Provide engineering group access to on-premises network | Engineering | False | 172.16.0.0/24 | 
| Provide development group access to development VPC | Developers | False | 10.0.0.0/16 | 
| Provide manager group access to Client VPN VPC | Managers | False | 192.168.0.0/24 | 

**Resulting behavior**
+ Users authenticated via SAML with the "Engineering" group attribute can access only `172.16.0.0/24`.
+ Users authenticated via SAML with the "Developers" group attribute can access only `10.0.0.0/16`.
+ Users authenticated via SAML with the "Managers" group attribute can access only `192.168.0.0/24`.
+ All other traffic is dropped by the Client VPN endpoint.

**Note**  
When using SAML federated authentication, the Group ID field corresponds to the SAML attribute value that identifies the user's group membership. This attribute is configured in your SAML identity provider and passed to Client VPN during authentication.

#### Access for all user groups
<a name="auth-rules8"></a>


| Rule description | Group ID | Allow access to all users | Destination CIDR | 
| --- | --- | --- | --- | 
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 | 
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 | 
| Provide manager group access to any destination | S-xxxxx16 | False | 0.0.0.0/0 | 
| Provide manager group access to single host in development VPC | S-xxxxx16 | False | 10.0.2.119/32 | 
| Provide engineering group access to a subnet in the on-premises network | S-xxxxx14 | False | 172.16.0.128/25 | 
| Provide engineering group access to all networks | S-xxxxx14 | False | 0.0.0.0/0 | 
| Provide manager group access to Client VPN VPC | S-xxxxx16 | False | 192.168.0.0/24 | 
| Provide access to all groups | N/A | True | 0.0.0.0/0 | 

**Resulting behavior**
+ The development group can access `10.0.0.0/16`, *except* for the single host `10.0.2.119/32`.
+ The manager group can access the public internet, `192.168.0.0/24`, and a single host (`10.0.2.119/32`) within the `10.0.0.0/16` network, but does not have access to `172.16.0.0/24` or any of the remaining hosts in the `10.0.0.0/16` network.
+ The engineering group can access the public internet, `172.16.0.0/24`, and `172.16.0.128/25`.
+ Any other user group, for example "admin group," can access the public internet, but not any other destination networks defined in the other rules.

### Add an authorization rule to an AWS Client VPN endpoint
<a name="cvpn-working-rule-authorize-add"></a>

You can add an authorization rule to grant or restrict access to a Client VPN endpoint by using the AWS Management Console. An authorization rule can be added to a Client VPN endpoint using either the Amazon VPC Console or by using the command line or API. 

**To add an authorization rule to a Client VPN endpoint using AWS Management Console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to which to add the authorization rule, choose **Authorization rules**, and choose **Add authorization rule**.

1. For **Destination network to enable access**, enter the IP address, in CIDR notation, of the network that you want users to access (for example, the CIDR block of your VPC).

1. Specify which clients are allowed to access the specified network. For **For grant access to**, do one of the following:
   + To grant access to all clients, choose **Allow access to all users**.
   + To restrict access to specific clients, choose **Allow access to users in a specific access group**, and then for **Access group ID**, enter the ID for the group to grant access to. For example, the security identifier (SID) of an Active Directory group, or the ID/name of a group defined in a SAML-based identity provider (IdP).
     + (Active Directory) To get the SID, you can use the Microsoft Powershell [Get-ADGroup](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup) cmdlet, for example:

       ```
       Get-ADGroup -Filter 'Name -eq "<{{Name of the AD Group}}>"'
       ```

       Alternatively, open the Active Directory Users and Computers tool, view the properties for the group, go to the Attribute Editor tab, and get the value for `objectSID`. If necessary, first choose **View**, **Advanced Features** to enable the Attribute Editor tab.
     + (SAML-based federated authentication) The group ID/name should match the group attribute information that is returned in the SAML assertion.

1. For **Description**, enter a brief description of the authorization rule.

1. Choose **Add authorization rule**.

**To add an authorization rule to a Client VPN endpoint (AWS CLI)**  
Use the [authorize-client-vpn-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/authorize-client-vpn-ingress.html) command.

### Remove an authorization rule from an AWS Client VPN endpoint
<a name="cvpn-working-rule-remove"></a>

You can remove authorization rules for a specific Client VPN endpoint using the console and the AWS CLI.

**To remove authorization rules (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint for which to which the authorization rule was added, and then choose **Authorization rules**.

1. Select the authorization rule to delete, choose **Remove authorization rule**, and then choose **Remove authorization rule **again to confirm the deletion.

**To remove authorization rules (AWS CLI)**  
Use the [revoke-client-vpn-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/revoke-client-vpn-ingress.html) command.

### View AWS Client VPN authorization rules
<a name="cvpn-working-rule-view"></a>

You can view authorization rules for a specific Client VPN endpoint using the console and the AWS CLI.

**To view authorization rules (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint for which to view authorization rules and choose **Authorization rules**.

**To view authorization rules (AWS CLI)**  
Use the [describe-client-vpn-authorization-rules](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-authorization-rules.html) command.

## AWS Client VPN client certificate revocation lists
<a name="cvpn-working-certificates"></a>

Client VPN client certificate revocation lists are used to revoke access to a Client VPN endpoint for specific client certificates. You can either generate a revocation list or import an existing list. You can also export your current list a revocation list file. Generating a list is performed using the OpenVPN software on either Linux/macOS or on Windows. Importing and exporting can be done using either the Amazon VPC Console or by using the AWS CLI. 

For more information about generating the server and client certificates and keys, see [Mutual authentication in AWS Client VPN](#mutual)

**Note**  
If a client certificate revocation list has expired, you cannot connect to the Client VPN endpoint. You'll need to create a new one and import it into the Client VPN endpoint. 

You can add only a limited number of entries to a client certificate revocation list. For more information about the number of entries you can add to a revocation list, see [Client VPN quotas](#quotas-endpoints).

**Topics**
+ [Generate a client certificate revocation list](#cvpn-working-certificates-generate)
+ [Import a client certificate revocation list](#cvpn-working-certificates-import)
+ [Export a client certificate revocation list](#cvpn-working-certificates-export)

### Generate an AWS Client VPN client certificate revocation list
<a name="cvpn-working-certificates-generate"></a>

You can generate a Client VPN certificate revocation list on either a Linux/macOS or Windows operating system. The revocation list is used to revoke access to a Client VPN endpoint for specific certificates. For more information about client certificate revocation lists, see [Client certificate revocation lists](#cvpn-working-certificates).

------
#### [ Linux/macOS ]

In the following procedure, you generate a client certificate revocation list using the OpenVPN easy-rsa command line utility.

**To generate a client certificate revocation list using OpenVPN easy-rsa**

1. Log on to the server hosting the easyrsa installation used to generate the certificate.

1. Navigate into the `easy-rsa/easyrsa3` folder in your local repo.

   ```
   $ cd easy-rsa/easyrsa3
   ```

1. Revoke the client certificate and generate the client revocation list.

   ```
   $ ./easyrsa revoke {{client1.domain.tld}}
   $ ./easyrsa gen-crl
   ```

   Enter `yes` when prompted.

------
#### [ Windows ]

The following procedure uses the OpenVPN software to generate a client revocation list. It assumes that you followed the [steps for using the OpenVPN software](#mutual) to generate the client and server certificates and keys.

**To generate a client certificate revocation list using EasyRSA version 3.x.x**

1. Open a command prompt and navigate to the EasyRSA-3.x.x directory, which will depend on where it is installed on your system.

   ```
   C:\> cd c:\{{Users}}\{{windows}}\EasyRSA-3.{{x.x}}
   ```

1. Run the `EasyRSA-Start.bat` file to start the EasyRSA shell.

   ```
   C:\> .\EasyRSA-Start.bat
   ```

1. In the EasyRSA shell, revoke the client certificate.

   ```
   # ./easyrsa revoke {{client_certificate_name}}
   ```

1. Enter `yes` when prompted.

1. Generate the client revocation list.

   ```
   # ./easyrsa gen-crl
   ```

1. The client revocation list will be created in the following location:

   ```
   c:\{{Users}}\{{windows}}\EasyRSA-3.{{x.x}}\pki\crl.pem
   ```

**To generate a client certificate revocation list using previous EasyRSA versions**

1. Open a command prompt and navigate to the OpenVPN directory.

   ```
   C:\> cd \Program Files\OpenVPN\easy-rsa
   ```

1. Run the `vars.bat` file.

   ```
   C:\> vars
   ```

1. Revoke the client certificate and generate the client revocation list.

   ```
   C:\> revoke-full {{client_certificate_name}}
   C:\> more crl.pem
   ```

------

### Import an AWS Client VPN client certificate revocation list
<a name="cvpn-working-certificates-import"></a>

You must have a Client VPN client certificate revocation list file to import. For more information about generating a client certificate revocation list, see [Generate an AWS Client VPN client certificate revocation list](#cvpn-working-certificates-generate).

You can import a client certificate revocation list using the console and the AWS CLI.

**To import a client certificate revocation list (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint for which to import the client certificate revocation list.

1. Choose **Actions**, and choose **Import Client Certificate CRL**.

1. For **Certificate Revocation List**, enter the contents of the client certificate revocation list file, and choose **Import client certificate CRL**.

**To import a client certificate revocation list (AWS CLI)**  
Use the [import-client-vpn-client-certificate-revocation-list](https://docs.aws.amazon.com/cli/latest/reference/ec2/import-client-vpn-client-certificate-revocation-list.html) command.

```
$ aws ec2 import-client-vpn-client-certificate-revocation-list --certificate-revocation-list file://{{path_to_CRL_file}} --client-vpn-endpoint-id {{endpoint_id}} --region {{region}}
```

### Export an AWS Client VPN client certificate revocation list
<a name="cvpn-working-certificates-export"></a>

You can export Client VPN client certificate revocation lists using the console and the AWS CLI.

**To export a client certificate revocation list (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint for which to export the client certificate revocation list.

1. Choose **Actions**, choose **Export Client Certificate CRL**, and choose **Export Client Certificate CRL**.

**To export a client certificate revocation (AWS CLI)**  
Use the [export-client-vpn-client-certificate-revocation-list](https://docs.aws.amazon.com/cli/latest/reference/ec2/export-client-vpn-client-certificate-revocation-list.html) command.

## AWS Client VPN client connections
<a name="cvpn-working-connections"></a>

AWS Client VPN connections are active VPN sessions that have been established by clients to a specific Client VPN endpoint as well as connections that had been terminated within the last 60 minutes for that endpoint. A connection is established when a client successfully connects to a Client VPN endpoint. Terminating a session ends that client connection to the Client VPN endpoint.

You can view and terminate Client VPN connections. Viewing connection information returns information such as the IP address assigned from the client CIDR block range, the endpoint ID, and timestamp. Terminating a session ends the specified VPN connection to the endpoint. Viewing and terminating sessions can be done using either the Amazon VPC Console or the AWS CLI. If you're unable to connect to the endpoint, and depending on the error, see [Troubleshooting AWS Client VPN](#troubleshooting) for steps to take to resolve the issue.

**Topics**
+ [View client connections](#cvpn-working-connections-view)
+ [Terminate a client connection](#cvpn-working-connections-disassociate)

### View AWS Client VPN client connections
<a name="cvpn-working-connections-view"></a>

You can view the active Client VPN connections using either the Amazon VPC Console or the AWS CLI.

**To view Client VPN client connections (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint for which to view client connections.

1. Choose the **Connections** tab. The **Connections** tab lists all active and terminated client connections.

**To view Client VPN client connections (AWS CLI)**  
Use the [describe-client-vpn-connections](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-connections.html) command.

### Terminate an AWS Client VPN client connection
<a name="cvpn-working-connections-disassociate"></a>

You can terminate a Client VPN client connection using the Amazon VPC Console or the AWS CLI.

**To terminate a Client VPN client connection (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to which the client is connected, and choose **Connections**.

1. Select the connection to terminate, choose **Terminate Connection**, and then choose **Terminate Connection** again to confirm the termination.

**To terminate a Client VPN client connection (AWS CLI)**  
Use the [terminate-client-vpn-connections](https://docs.aws.amazon.com/cli/latest/reference/ec2/terminate-client-vpn-connections.html) command.

## AWS Client VPN client login banners
<a name="cvpn-working-login-banner"></a>

AWS Client VPN provides the option to display a text banner on AWS provided Client VPN desktop applications when a VPN session is established. You can define the contents of the text banner to meet your regulatory and compliance needs. A maximum of 1400 UTF-8 encoded characters can be used.

**Note**  
When a client login banner has been enabled, it will be displayed on newly created VPN sessions only. Existing VPN sessions are not interrupted, though the banner will be displayed when an existing session is re-established.

### Banner creation
<a name="configure-login-banner-endpoint-creation"></a>

Login banners are initially created and enabled during the creation of the Client VPN endpoint. For the steps to enable a client login banner during creation of a Client VPN endpoint, see [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create).

**Topics**
+ [Banner creation](#configure-login-banner-endpoint-creation)
+ [Configure a client login banner for an existing endpoint](#configure-login-banner-existing-endpoint)
+ [Deactivate a client login banner for an endpoint](#disable-login-banner)
+ [Modify existing banner text](#modify-banner-text)
+ [View a currently configured login banner](#display-login-banner)

### Configure a client login banner for an existing AWS Client VPN endpoint
<a name="configure-login-banner-existing-endpoint"></a>

Use the following steps to configure a client login banner for an existing Client VPN endpoint.

**Enable client login banner on a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint that you want to modify, choose **Actions**, and then choose **Modify Client VPN Endpoint**.

1. Scroll down the page to the **Other parameters** section.

1. Turn on **Enable client login banner**.

1. For **Client login banner text**, enter the text that will be displayed in a banner on AWS provided clients when a VPN session is established. Use UTF-8 encoded characters only, with a maximum of 1400 characters allowed.

1. Choose **Modify Client VPN endpoint**.

**Enable client login banner on a Client VPN endpoint (AWS CLI)**  
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.

### Deactivate a client login banner for an existing AWS Client VPN endpoint
<a name="disable-login-banner"></a>

Use the following steps to deactivate a client login banner for an existing Client VPN endpoint.

**Deactivate client login banner on a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint that you want to modify, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. Scroll down the page to the **Other parameters** section.

1. Turn off **Enable client login banner?**.

1. Choose **Modify Client VPN endpoint**.

**Deactivate client login banner on a Client VPN endpoint (AWS CLI)**  
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.

### Modify existing banner text on a AWS Client VPN endpoint
<a name="modify-banner-text"></a>

Use the following steps to modify existing text on a Client VPN client login banner.

**Modify existing banner text on a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint that you want to modify, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. For **Enable client login banner?**, verify that it's turned on.

1. For **Client login banner text**, replace the existing text with new text that you want displayed in a banner on AWS provided clients when a VPN session is established. Use UTF-8 encoded characters only, with a maximum of 1400 characters.

1. Choose **Modify Client VPN endpoint**.

**Modify client login banner on a Client VPN endpoint (AWS CLI)**  
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.

### View a currently configured AWS Client VPN login banner
<a name="display-login-banner"></a>

Use the following steps to view a currently configured Client VPN client login banner.

**View current login banner for a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint that you want to view.

1. Verify that the **Details** tab is selected.

1. View the currently configured login banner text next to **Client login banner text**. 

**View currently configured login banner for a Client VPN endpoint (AWS CLI)**  
Use the [describe-client-vpn-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-endpoints.html) command.

## AWS Client VPN Client Route Enforcement
<a name="cvpn-working-cre"></a>

Client Route Enforcement helps enforce administrator-defined routes on devices connected through the VPN. This feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.

Client Route Enforcement monitors the main routing table of the connected device and ensures that outbound network traffic goes to a VPN tunnel, according to network routes configured in the client VPN endpoint. This includes modifying routing tables on a device if routes conflicting with VPN tunnel are detected. Client Route Enforcement supports both IPv4 and IPv6 address families.

### Requirements
<a name="requirements-cre"></a>

Client Route Enforcement only works with the following AWS provided Client VPN versions:
+ Windows version 5.2.0 or higher (IPv4 support)
+ macOS version 5.2.0 or higher (IPv4 support)
+ Ubuntu version 5.2.0 or higher (IPv4 support)
+ Windows version 5.3.0 or higher (IPv6 support)
+ macOS version 5.3.0 or higher (IPv6 support)
+ Ubuntu version 5.3.0 or higher (IPv6 support)

For dual-stack endpoints, the Client Route Enforcement setting applies to both IPv4 and IPv6 stacks simultaneously. It is not possible to enable Client Route Enforcement for only one stack.

### Routing conflicts
<a name="route-conflict-cre"></a>

While a client is connected to VPN, a comparison is made between the client's local route table, and the endpoint's network routes. A routing conflict will occur if there is network overlap between two route table entries. An example of overlapping networks is:
+ `172.31.0.0/16`
+ `172.31.1.0/24`

In this example, these CIDR blocks constitute a routing conflict. For example, `172.31.0.0/16` might be the VPN tunnel CIDR. Since `172.31.1.0/24` is more specific because it has a longer prefix, it typically takes precedence and potentially redirects VPN traffic within the `172.31.1.0/24` IP range to another destination. This could lead to unintended routing behavior. However, when Client Route Enforcement is enabled, the latter CIDR would be removed. When using this feature potential routing conflicts should be taken into consideration.

Full tunnel VPN connections direct all network traffic through the VPN connection. As a result, devices connected to the VPN will not be able to access local network (LAN) resources, if Client Route Enforcement feature is enabled. If local LAN access is required, consider using split-tunnel mode instead of full-tunnel mode. For more information about split-tunnel, see [Split-tunnel Client VPN](#split-tunnel-vpn).

### Considerations
<a name="considerations-cre"></a>

The following information should be taken into consideration before activating Client Route Enforcement.
+ At the time of connection, if a routing conflict is detected, the feature will update the client's route table to direct the traffic into the VPN tunnel. The routes that existed before the connection was established, and were deleted by this feature, will be restored.
+ The feature is enforced only on the main routing table and does not apply to other routing mechanisms. For example, enforcement is not applied to the following:
  + policy-based routing
  + interface-scoped routing
+ Client Route Enforcement protects the VPN tunnel while it's open. There is no protection after the tunnel is disconnected or while the client is reconnecting.

#### OpenVPN directives impact on Cloud Route Enforcement
<a name="considerations-openvpn"></a>

Some custom directives in the OpenVPN configuration file have specific interactions with Client Route Enforcement:
+ The `route` directive 
  + When adding routes to a VPN gateway. For example, adding the route `192.168.100.0 255.255.255.0` to a VPN gateway.

    Routes added to a VPN gateway are monitored by Client Route Enforcement similarly to any other VPN route. Any conflicting routes within them will be detected and removed. 
  + When adding routes to a non-VPN gateway. For example, adding the route `192.168.200.0 255.255.255.0 net_gateway`.

    Routes added to a non-VPN gateway are excluded from Client Route Enforcement as they bypass the VPN tunnel. Conflicting routes are allowed within them. In the example, above the route will be excluded from monitoring by Client Route Enforcement. 
  + Similar to IPv4 routes, IPv6 routes added to a VPN gateway are monitored by Client Route Enforcement, while routes added to a non-VPN gateway are excluded from monitoring.

#### Ignored routes
<a name="cre-ignored"></a>

Routes to the following IPv4 networks will be ignored by Client Route Enforcement:
+ `127.0.0.0/8` — Reserved for the local host
+ `169.254.0.0/16` — Reserved for link-local addresses
+ `224.0.0.0/4` — Reserved for multicast
+ `255.255.255.255/32` — Reserved for broadcast

Routes to the following IPv6 networks will be ignored by Client Route Enforcement:
+ `::1/128` — Reserved for loopback 
+ `fe80::/10` — Reserved for link-local addresses 
+ `ff00::/8` — Reserved for multicast 

**Topics**
+ [Requirements](#requirements-cre)
+ [Routing conflicts](#route-conflict-cre)
+ [Considerations](#considerations-cre)
+ [Activate Client Route Enforcement](#activate-cre)
+ [Deactivate Client Route Enforcement](#deactivate-cre)
+ [Troubleshoot IPv6 Client Route Enforcement](#cre-ipv6-troubleshooting)

### Activate Client Route Enforcement for an AWS Client VPN endpoint
<a name="activate-cre"></a>

You can activate Client Route Enforcement on existing Client VPN endpoints using either the console or the AWS CLI.

**To activate Client Route Enforcement using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN endpoints**.

1. Choose the Client VPN endpoint that you want to modify, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. Scroll down the page to the **Other parameters** section.

1. Turn on **Client Route Enforcement**.

1. Choose **Modify Client VPN endpoint**.

**To activate Client Route Enforcement using the AWS CLI)**
+ Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.

### Deactivate Client Route Enforcement from an AWS Client VPN endpoint
<a name="deactivate-cre"></a>

You can deactivate Client Route Enforcement on Client VPN endpoints using either the console or the AWS CLI.

**To deactivate Client Route Enforcement using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN endpoints**.

1. Choose the Client VPN endpoint that you want to modify, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. Scroll down the page to the **Other parameters** section.

1. Turn off **Client Route Enforcement**.

1. Choose **Modify Client VPN endpoint**.

**To deactivate Client Route Enforcement using the AWS CLI**
+ Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.

### Troubleshoot IPv6 Client Route Enforcement
<a name="cre-ipv6-troubleshooting"></a>

If you encounter issues with IPv6 Client Route Enforcement, consider the following troubleshooting steps:

Verify client version  
Ensure that you are using AWS VPN Client version 5.3.0 or higher, which is required for IPv6 Client Route Enforcement support.

Check endpoint configuration  
Verify that the endpoint has Client Route Enforcement enabled and is configured for IPv6 or dual-stack traffic.

Examine client logs  
Review the AWS VPN Client logs for any error messages related to IPv6 Client Route Enforcement. Look for entries containing "IPv6" and "Client Route Enforcement" or "CRM".

Inspect routing table  
Use the appropriate command for your operating system to view the IPv6 routing table:  
+ Windows: `netsh interface ipv6 show route`
+ macOS: `netstat -rn -f inet6`
+ Linux: `ip -6 route`

Check for conflicting routes  
Look for any IPv6 routes that might conflict with the VPN routes. Pay special attention to routes with the same destination but different gateways.

Verify ISP IPv6 support  
Ensure that your internet service provider (ISP) properly supports IPv6.

If you continue to experience issues with IPv6 Client Route Enforcement after trying these troubleshooting steps, contact AWS Support for further assistance.

## AWS Client VPN endpoints
<a name="cvpn-working-endpoints"></a>

All AWS Client VPN sessions establish communication with a Client VPN endpoint. You can manage the Client VPN endpoint to create, modify, view, and delete client VPN sessions with that endpoint. Endpoints can be created and modified using either the Amazon VPC Console or by using the AWS CLI.

### Requirements for creating Client VPN endpoints
<a name="cvpn-working-create-req"></a>

**Important**  
A Client VPN endpoint must be created in the same AWS account in which the intended target network is provisioned. You'll also need to generate a server certificate, and if required, a client certificate. For more information, see [Client authentication in AWS Client VPN](#client-authentication).

Before you begin, ensure that you do the following:
+ Review the rules and limitations in [Rules and best practices for using AWS Client VPN](#what-is-best-practices).
+ Generate the server certificate, and if required, the client certificate. For more information, see [Client authentication in AWS Client VPN](#client-authentication).

### IP address types
<a name="cvpn-ip-address-types"></a>

AWS Client VPN supports IPv4-only, IPv6-only, and dual-stack configurations for both endpoint connectivity and traffic routing. The following guidance helps you select the appropriate IP address type based on your client device capabilities, network infrastructure, and application requirements.

#### Endpoint address type
<a name="cvpn-endpoint-types"></a>

The endpoint address type determines which IP protocols your Client VPN endpoint supports for client connections. This setting cannot be changed after endpoint creation.

**Choose IPv4-only when:**
+ Your client devices only support IPv4 VPN connections
+ Your security tools are optimized for IPv4 traffic inspection

**Choose IPv6-only when:**
+ All client devices fully support IPv6 connections
+ You're in networks where IPv4 addresses are depleted

**Choose dual-stack when:**
+ You have a mix of client devices with varying IP capabilities
+ You're gradually transitioning from IPv4 to IPv6

#### Traffic IP address type
<a name="cvpn-traffic-ip-considerations"></a>

The traffic IP address type controls how Client VPN routes traffic between clients and your VPC resources, independent of the endpoint's supported protocols.

**Route traffic as IPv4 when:**
+ Target applications in your VPC only support IPv4
+ You have complex IPv4 security groups and network ACLs
+ You're connecting to legacy systems

**Route traffic as IPv6 when:**
+ Your VPC infrastructure is primarily IPv6
+ You want to future-proof your network architecture
+ You have modern applications built for IPv6

### Endpoint modification
<a name="cvpn-endpoints-modify-req"></a>

**Note**  
Client VPN endpoints created using quickstart setup can be modified using the same procedures as endpoints created with standard setup. All configuration options are available regardless of the setup method used during creation.

After a Client VPN has been created, you can modify any of the following settings: 
+ The description
+ The server certificate
+ The client connection logging options
+ The client connect handler option
+ The DNS servers
+ The split-tunnel option
+ Routes (when using the split-tunnel option)
+ Certificate Revocation List (CRL)
+ Authorization rules
+ The VPC and security group associations
+ The VPN port number
+ The self-service portal option
+ The maximum VPN session duration
+ Enable or disable automatic reconnection on session timeout
+ Enable or disable client login banner text
+ Client login banner text

**Note**  
Modifications to Client VPN endpoints, including Certificate Revocation List (CRL) changes, will take effect up to 4 hours after a request is accepted by the Client VPN service.  
You cannot modify the client IPv4 CIDR range, authentication options, client certificate or transport protocol after the Client VPN endpoint has been created.

When you modify any of the following parameters on a Client VPN endpoint, the connection resets:
+ The server certificate
+ The DNS servers
+ The split-tunnel option (turning support on or off)
+ Routes (when you use the split-tunnel option)
+  Certificate Revocation List (CRL)
+ Authorization rules
+ The VPN port number

**Topics**
+ [Requirements for creating Client VPN endpoints](#cvpn-working-create-req)
+ [IP address types](#cvpn-ip-address-types)
+ [Endpoint modification](#cvpn-endpoints-modify-req)
+ [Create an endpoint](#cvpn-working-endpoint-create)
+ [View endpoints](#cvpn-working-endpoint-view)
+ [Modify an endpoint](#cvpn-working-endpoint-modify)
+ [Delete an endpoint](#cvpn-working-endpoint-delete)

### Create an AWS Client VPN endpoint
<a name="cvpn-working-endpoint-create"></a>

Create a AWS Client VPN endpoint to enable your clients to establish a VPN session using either the Amazon VPC Console or the AWS CLI.Client VPN supports all combinations of endpoint type (split-tunnel and full-tunnel) with traffic type (IPv4, IPv6, and dual-stack) during initial creation. 

Before creating an endpoint, familiarize yourself with the requirements. For more information, see [Requirements for creating Client VPN endpoints](#cvpn-working-create-req).

**To create a Client VPN endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints** and then choose **Create Client VPN Endpoint**.

1. Under "Choose setup method", select one of the following: 
   + Quickstart - Create an endpoint with AWS-recommended defaults
   + Standard - Manually configure all settings for the endpoint

**Quickstart setup:**

1. For "Choose setup method", select Quickstart.

1.  For "Client IPv4 CIDR", enter the IP address range from which to assign client IP addresses. AWS recommends using a /22 CIDR block (for example, 10.0.0.0/22). 

1.  For "VPC", select the VPC to associate with the Client VPN endpoint. 

1.  For "Subnets", select one or more subnets in the VPC. These subnets will be used for target network associations. 

1.  For Server certificate ARN, specify the ARN for the TLS certificate to be used by the server. Clients use the server certificate to authenticate the Client VPN endpoint to which they are connecting. 

1.  Choose "Create Client VPN endpoint". 

AWS automatically creates the following resources: 
+ Authorization rule allowing all users to access the VPC CIDR
+ Target network association with the selected VPC subnets
+ Route table entries for the VPC CIDR

 After the endpoint is created, you can download the client configuration file from the endpoint details page and distribute it to your users along with the client certificate and key. 

**Standard setup:**

1. For "Choose setup method", select Standard.

1. (Optional) Provide a name tag and description for the Client VPN endpoint.

1. For **Endpoint IP address type**, choose the IP address type for the endpoint:
   + **IPv4**: The endpoint uses IPv4 addresses for outer VPN tunnel traffic.
   + **IPv6**: The endpoint uses IPv6 addresses for outer VPN tunnel traffic.
   + **Dual-stack**: The endpoint uses both IPv4 and IPv6 addresses for outer VPN tunnel traffic.

1. For **Traffic IP address type**, choose the IP address type for traffic flowing through the endpoint:
   + **IPv4**: The endpoint supports IPv4 traffic only.
   + **IPv6**: The endpoint supports IPv6 traffic only.
   + **Dual-stack**: The endpoint supports both IPv4 and IPv6 traffic.

1. For **Client IPv4 CIDR**, specify an IP address range, in CIDR notation, from which to assign client IP addresses. For example, `10.0.0.0/22`. This is required if you selected IPv4 or Dual-stack for the Traffic IP address type.
**Note**  
The address range cannot overlap with the target network address range, the VPC address range or any of the routes that will be associated with the Client VPN endpoint. The client address range must be at minimum /22 and not greater than /12 CIDR block size. You cannot change the client address range after you create the Client VPN endpoint.
When you select IPv6 as the endpoint IP address type, the Client IPv4 CIDR field is disabled. The Client VPN endpoint allocates client IPv6 addresses from an associated subnet, and you can associate the subnet after creating the endpoint.
**Note**  
For IPv6 traffic, you do not need to specify a client CIDR range. Amazon automatically assigns IPv6 CIDR ranges for clients.

1. For **Server certificate ARN**, specify the ARN for the TLS certificate to be used by the server. Clients use the server certificate to authenticate the Client VPN endpoint to which they are connecting.
**Note**  
The server certificate must be present in AWS Certificate Manager (ACM) in the region you are creating the Client VPN endpoint. The certificate can either be provisioned with ACM or imported into ACM.  
For the steps to provision or import a certificate into ACM, see [AWS Certificate Manager Certificates](https://docs.aws.amazon.com/acm/latest/userguide/gs.html) in the *AWS Certificate Manager User Guide*.

1. Specify the authentication method to be used to authenticate clients when they establish a VPN connection. You must select an authentication method.
   + To use user-based authentication, select **Use user-based authentication**, and then choose one of the following:
     + **Active Directory authentication**: Choose this option for Active Directory authentication. For **Directory ID**, specify the ID of the Active Directory to use.
     + **Federated authentication**: Choose this option for SAML-based federated authentication. 

       For **SAML provider ARN**, specify the ARN of the IAM SAML identity provider. 

       (Optional) For **Self-service SAML provider ARN**, specify the ARN of the IAM SAML identity provider that you created to [support the self-service portal](#saml-self-service-support), if applicable.
   + To use mutual certificate authentication, select **Use mutual authentication**, and then for **Client certificate ARN**, specify the ARN of the client certificate that's provisioned in AWS Certificate Manager (ACM).
**Note**  
If the server and client certificates have been issued by the same Certificate Authority (CA), you can use the server certificate ARN for both server and client. If the client certificate was issued by a different CA, then the client certificate ARN should be specified.

1. (Optional) For **Connection logging**, specify whether to log data about client connections using Amazon CloudWatch Logs. Turn on **Enable log details on client connections**. For **CloudWatch Logs log group name**, enter the name of the log group to use. For **CloudWatch Logs log stream name**, enter the name of the log stream to use, or leave this option blank to let us create a log stream for you. 

1. (Optional) For **Client Connect Handler**, turn on **Enable client connect handler** to run custom code that allows or denies a new connection to the Client VPN endpoint. For **Client Connect Handler ARN**, specify the Amazon Resource Name (ARN) of the Lambda function that contains the logic that allows or denies connections.

1. (Optional) For **Device posture**, turn on **Enable device posture** to authorize connections based on the health of the connecting device. Configure one or more device trust providers and the authorization policy to evaluate. For more information, see [Device posture for AWS Client VPN](#device-posture).

1. (Optional) Specify which DNS servers to use for DNS resolution. To use custom DNS servers, for **DNS Server 1 IP address** and **DNS Server 2 IP address**, specify the IPv4 addresses of the DNS servers to use. For IPv6 or dual-stack endpoints, you can also specify **DNS Server IPv6 1** and **DNS Server IPv6 2** addresses. To use VPC DNS server, for either **DNS Server 1 IP address** or **DNS Server 2 IP address**, specify the IP addresses, and add the VPC DNS server IP address.
**Note**  
Verify that the DNS servers can be reached by clients.

1. (Optional) By default, the Client VPN endpoint uses the `UDP` transport protocol. To use the `TCP` transport protocol instead, for **Transport Protocol**, select **TCP**.
**Note**  
UDP typically offers better performance than TCP. You cannot change the transport protocol after you create the Client VPN endpoint.

1. (Optional) To have the endpoint be a split-tunnel Client VPN endpoint, turn on **Enable split-tunnel**. By default, split-tunnel on a Client VPN endpoint is disabled.

1. (Optional) For **VPC ID**, choose the VPC to associate with the Client VPN endpoint. For **Security Group IDs**, choose one or more of the VPC's security groups to apply to the Client VPN endpoint.

1. (Optional) For **VPN port**, choose the VPN port number. The default is 443.

1. (Optional) To generate a [self-service portal URL](#cvpn-self-service-portal) for clients, turn on **Enable self-service portal**.

1. (Optional) For **Session timeout hours**, choose the desired maximum VPN session duration time in hours from the available options, or leave set to default of 24 hours.

1. (Optional) For **Disconnect on session timeout**, choose if you want to terminate the session when the maximum session time is reached. Choosing this option requires that users reconnect manually to the endpoint when the session times out; otherwise, Client VPN will automatically try to reconnect.

1. (Optional) Specify whether to enable client login banner text. Turn on **Enable client login banner**. For **Client login banner text**, enter the text that will be displayed in a banner on AWS provided clients when a VPN session is established. UTF-8 encoded characters only. Maximum of 1400 characters.

1. Choose **Create Client VPN endpoint**.

After you create the Client VPN endpoint, do the following to complete the configuration and enable clients to connect:
+ The initial state of the Client VPN endpoint is `pending-associate`. Clients can only connect to the Client VPN endpoint after you associate the first [target network](#cvpn-working-target-associate).
+ Create an [authorization rule](#cvpn-working-rules) to specify which clients have access to the network.
+ Download and prepare the Client VPN endpoint [configuration file](#cvpn-working-endpoint-export) to distribute to your clients.
+ Instruct your clients to use the AWS provided client or another OpenVPN-based client application to connect to the Client VPN endpoint. For more information, see the [AWS Client VPN User Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/).

**To create a Client VPN endpoint using the AWS CLI**  
Use the [create-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-client-vpn-endpoint.html) command.

Example for creating an IPv4 endpoint:

```
aws ec2 create-client-vpn-endpoint \
  --client-cidr-block "172.31.0.0/16" \
  --server-certificate-arn arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE \
  --authentication-options Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE} \
  --connection-log-options Enabled=false
```

Example for creating an IPv6 endpoint:

```
aws ec2 create-client-vpn-endpoint \
  --endpoint-ip-address-type "ipv6" \
  --traffic-ip-address-type "ipv6" \
  --server-certificate-arn arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE \
  --authentication-options Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE} \
  --connection-log-options Enabled=false
```

Example for creating a dual-stack endpoint:

```
aws ec2 create-client-vpn-endpoint \
  --endpoint-ip-address-type "dual-stack" \
  --traffic-ip-address-type "dual-stack" \
  --client-cidr-block "172.31.0.0/16" \
  --server-certificate-arn arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE \
  --authentication-options Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE} \
  --connection-log-options Enabled=false
```

#### Device posture options
<a name="cvpn-device-posture-options"></a>

To require device health checks on an endpoint, specify the `DevicePostureOptions` parameter when you create or modify the endpoint. This parameter contains the following fields:
+ `Enabled` — Whether device posture is enabled for the endpoint.
+ `TrustProviders` — One or more device trust providers to evaluate. Each trust provider contains the following fields:
  + `TrustProviderType` — The type of device trust provider (for example, CrowdStrike, Jamf, or JumpCloud).
  + `TenantId` — The tenant identifier for the device trust provider.
  + `PublicSigningKeyUrl` — The URL of the public signing key used to verify device posture tokens.

For more information, see [Device posture for AWS Client VPN](#device-posture).

### View AWS Client VPN endpoints
<a name="cvpn-working-endpoint-view"></a>

You can view information about Client VPN endpoints by using the Amazon VPC Console or the AWS CLI.

**To view Client VPN endpoints (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to view.

1. Use the **Details**, **Target network associations**, **Security groups**, **Authorization rules**, **Route table**, **Connections** and **Tags** tabs to view information about existing Client VPN endpoints.

   You can also use filters to help refine your search.

**To view Client VPN endpoints (AWS CLI)**  
Use the [describe-client-vpn-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-endpoints.html) command.

### Modify an AWS Client VPN endpoint
<a name="cvpn-working-endpoint-modify"></a>

You can modify a Client VPN endpoint by using the Amazon VPC Console or the AWS CLI. For more information about the fields you can Client VPN fields you can modify, see [Endpoint modification](#cvpn-endpoints-modify-req).

#### Limitations
<a name="endpoints-limits"></a>

The following limitations apply when modifying an endpoint 
+  Modifications to Client VPN endpoints, including Certificate Revocation List (CRL) changes, will take effect up to 4 hours after a request is accepted by the Client VPN service.
+ You cannot modify the client IPv4 CIDR range, authentication options, client certificate or transport protocol after the Client VPN endpoint has been created.
+ Client VPN does not support modification of endpoint type (IPv4, IPv6, dual-stack) or traffic type (IPv4, IPv6, dual-stack) after creation.
+ Modifying a Client VPN with a specific combination of endpoint type and traffic type is not supported. You cannot change to any other combination. The endpoint must be deleted and recreated with the desired configuration.
+ Client-to-client communication for IPv6 traffic is not supported.

#### Modify a Client VPN endpoint
<a name="endpoint-modify"></a>

You can modify a Client VPN endpoint using either the console or the AWS CLI. 

**To modify a Client VPN endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to modify, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. For **Description**, enter a brief description for the Client VPN endpoint.

1. For **Server certificate ARN**, specify the ARN for the TLS certificate to be used by the server. Clients use the server certificate to authenticate the Client VPN endpoint to which they are connecting.
**Note**  
The server certificate must be present in AWS Certificate Manager (ACM) in the region you are creating the Client VPN endpoint. The certificate can either be provisioned with ACM or imported into ACM.

1. Specify whether to log data about client connections using Amazon CloudWatch Logs. For **Enable log details on client connections**, do one of the following:
   + To activate client connection logging, turn on **Enable log details on client connections**. For **CloudWatch Logs log group name**, select the name of the log group to use. For **CloudWatch Logs log stream name**, select the name of the log stream to use, or leave this option blank to let us create a log stream for you.
   + To deactivate client connection logging, turn off **Enable log details on client connections**.

1. For **Client connect handler**, to activate the [client connect handler](#connection-authorization) turn on **Enable client connect handler**. For **Client Connect Handler ARN**, specify the Amazon Resource Name (ARN) of the Lambda function that contains the logic that allows or denies connections.

1. Turn on or off **Enable DNS servers**. To use custom DNS servers, for **DNS Server 1 IP address** and **DNS Server 2 IP address**, specify the IPv4 addresses of the DNS servers to use. For IPv6 or dual-stack endpoints, you can also specify **DNS Server IPv6 1** and **DNS Server IPv6 2** addresses. To use VPC DNS server, for either **DNS Server 1 IP address** or **DNS Server 2 IP address**, specify the IP addresses, and add the VPC DNS server IP address.
**Note**  
Verify that the DNS servers can be reached by clients.

1. Turn on or off **Enable split-tunnel**. By default, split-tunnel on a VPN endpoint is off.

1. For **VPC ID**, choose the VPC to associate with the Client VPN endpoint. For **Security Group IDs**, choose one or more of the VPC's security groups to apply to the Client VPN endpoint.

1. For **VPN port**, choose the VPN port number. The default is 443.

1. To generate a [self-service portal URL](#cvpn-self-service-portal) for clients, turn on **Enable self-service portal**.

1. For **Session timeout hours**, choose the desired maximum VPN session duration time in hours from the available options, or leave set to default of 24 hours.

1. For **Disconnect on session timeout**, choose if you want to terminate the session when the maximum session time is reached. Choosing this option requires that users reconnect manually to the endpoint when the session times out; otherwise, Client VPN will automatically try to reconnect.

1. Turn on or off **Enable client login banner**. If you want to use the client login banner, enter the text that will be displayed in a banner on AWS provided clients when a VPN session is established. UTF-8 encoded characters only. Maximum of 1400 characters.

1. Choose **Modify Client VPN endpoint**.

**To modify a Client VPN endpoint using the AWS CLI**  
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.

### Delete an AWS Client VPN endpoint
<a name="cvpn-working-endpoint-delete"></a>

You will need to disassociate all target networks before you can delete a Client VPN endpoint. When you delete a Client VPN endpoint, its state is changed to `deleting` and clients can no longer connect to it. 

You can delete a Client VPN endpoint by using the console or the AWS CLI.

**To delete a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to delete. Choose **Actions**, **Delete Client VPN endpoint**.

1. Enter *delete* into the confirmation window and choose** Delete**.

**To delete a Client VPN endpoint (AWS CLI)**  
Use the [delete-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-client-vpn-endpoint.html) command.

## AWS Client VPN connection logs
<a name="cvpn-working-with-connection-logs"></a>

You can enable connection logging for a new or existing Client VPN endpoint, and start capturing connection logs. Connection logs show the sequence of log events for the Client VPN endpoint. When you enable connection logging, you can specify the name of a log stream in the log group. If you do not specify a log stream, the Client VPN service creates one for you. Connection logging then logs the following information: client connection requests, client connection results (successful or unsuccessful), reasons for unsuccessful connection results, and the client termination time from the endpoint. 

Before you begin, you must have a CloudWatch Logs log group in your account. For more information, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide*. Charges apply for using CloudWatch Logs. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

Client VPN connection logs can be created using either the Amazon VPC Console or the AWS CLI.

**Topics**
+ [Enable connection logging for a new endpoint](#create-connection-log-new)
+ [Enable connection logging for an existing endpoint](#create-connection-log-existing)
+ [View connection logs](#view-connection-logs)
+ [Turn off connection logging](#disable-connection-logs)

### Enable connection logging for a new AWS Client VPN endpoint
<a name="create-connection-log-new"></a>

You can enable connection logging when you create a new Client VPN endpoint by using the console or the command line.

**To enable connection logging for a new Client VPN endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**, and then choose **Create Client VPN endpoint.**

1. Complete the options until you reach the **Connection Logging** section. For more information about the options, see [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create).

1. Under **Connection logging**, turn on **Enable log details on client connections**.

1. For **CloudWatch Logs log group name**, choose the name of the CloudWatch Logs log group.

1. (Optional) For **CloudWatch Logs log stream name**, choose the name of the CloudWatch Logs log stream.

1. Choose **Create Client VPN endpoint**.

**To enable connection logging for a new Client VPN endpoint using the AWS CLI**  
Use the [create-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-client-vpn-endpoint.html) command, and specify the `--connection-log-options` parameter. You can specify the connection logs information in JSON format, as shown in the following example.

```
{
    "Enabled": true,
    "CloudwatchLogGroup": "ClientVpnConnectionLogs",
    "CloudwatchLogStream": "NewYorkOfficeVPN"
}
```

### Enable connection logging for an existing AWS Client VPN endpoint
<a name="create-connection-log-existing"></a>

You can enable connection logging for an existing Client VPN endpoint by using the console or the command line.

**To enable connection logging for an existing Client VPN endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. Under **Connection logging**, turn on **Enable log details on client connections**.

1. For **CloudWatch Logs log group name**, choose the name of the CloudWatch Logs log group.

1. (Optional) For **CloudWatch Logs log stream name**, choose the name of the CloudWatch Logs log stream.

1. Choose **Modify Client VPN endpoint**.

**To enable connection logging for an existing Client VPN endpoint using the AWS CLI**  
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command and specify the `--connection-log-options` parameter. You can specify the connection logs information in JSON format, as shown in the following example.

```
{
    "Enabled": true,
    "CloudwatchLogGroup": "ClientVpnConnectionLogs",
    "CloudwatchLogStream": "NewYorkOfficeVPN"
}
```

### View AWS Client VPN connection logs
<a name="view-connection-logs"></a>

You can view your Client VPN connection logs using the CloudWatch Logs console.

**To view your connection logs using the console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Log groups**, and select the log group that contains your connection logs. 

1. Select the log stream for your Client VPN endpoint.
**Note**  
The **Timestamp** column displays the time that the connection log was published to CloudWatch Logs, not the time of the connection.

For more information about searching log data, see [Search Log Data Using Filter Patterns](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SearchDataFilterPattern.html) in the *Amazon CloudWatch Logs User Guide*.

### Turn off AWS Client VPN connection logging
<a name="disable-connection-logs"></a>

You can turn off connection logging for a Client VPN endpoint by using the console or the command line. When you turn off connection logging, existing connection logs in CloudWatch Logs are not deleted.

**To turn off connection logging using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. Under **Connection logging**, turn off **Enable log details on client connections**.

1. Choose **Modify Client VPN endpoint**.

**To turn off connection logging using the AWS CLI**  
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command, and specify the `--connection-log-options` parameter. Ensure that `Enabled` is set to `false`.

## AWS Client VPN endpoint configuration file export
<a name="cvpn-working-endpoint-export"></a>

The AWS Client VPN endpoint configuration file is the file that clients (users) use to establish a VPN connection with the Client VPN endpoint. You must download (export) this file and distribute it to all clients who need access to the VPN. Alternatively, if you enabled the self-service portal for your Client VPN endpoint, clients can log into the portal and download the configuration file themselves. For more information, see [AWS Client VPN access to the self-service portal](#cvpn-self-service-portal).

If your Client VPN endpoint uses mutual authentication, you must [add the client certificate and the client private key to the .ovpn configuration file](#add-config-file-cert-key) that you download. After you add the information, clients can import the .ovpn file into the OpenVPN client software.

**Important**  
If you do not add the client certificate and the client private key information to the file, clients that authenticate using mutual authentication cannot connect to the Client VPN endpoint.

By default, the “remote-random-hostname” option in the OpenVPN client configuration enables wildcard DNS. Because wildcard DNS is enabled, the client does not cache the IP address of the endpoint and you will not be able to ping the DNS name of the endpoint. 

If your Client VPN endpoint uses Active Directory authentication and if you enable multi-factor authentication (MFA) on your directory after you distribute the client configuration file, you must download a new file and redistribute it to your clients. Clients cannot use the previous configuration file to connect to the Client VPN endpoint.

**Topics**
+ [Export the client configuration file](#export-client-config-file)
+ [Add the client certificate and key information for mutual authentication](#add-config-file-cert-key)

### Export the AWS Client VPN client configuration file
<a name="export-client-config-file"></a>

You can export the Client VPN client configuration by using the console or the AWS CLI.

**To export client configuration (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint for which to download the client configuration and choose **Download Client Configuration**.

**To export client configuration (AWS CLI)**  
Use the [export-client-vpn-client-configuration](https://docs.aws.amazon.com/cli/latest/reference/ec2/export-client-vpn-client-configuration.html) command and specify the output file name.

```
$ aws ec2 export-client-vpn-client-configuration --client-vpn-endpoint-id {{endpoint_id}} --output text>{{config_filename}}.ovpn
```

### Add the AWS Client VPN client certificate and key information for mutual authentication
<a name="add-config-file-cert-key"></a>

If your Client VPN endpoint uses mutual authentication, you must add the client certificate and the client private key to the .ovpn configuration file that you download.

You cannot modify the client certificate when you use mutual authentication.

**To add the client certificate and key information (mutual authentication)**  
You can use one of the following options.

(Option 1) Distribute the client certificate and key to clients along with the Client VPN endpoint configuration file. In this case, specify the path to the certificate and key in the configuration file. Open the configuration file using your preferred text editor, and add the following to the end of the file. Replace {{/path/}} with the location of the client certificate and key (the location is relative to the client that's connecting to the endpoint).

```
cert /{{path}}/client1.domain.tld.crt
key /{{path}}/client1.domain.tld.key
```

(Option 2) Add the contents of the client certificate between `<cert>``</cert>` tags and the contents of the private key between `<key>``</key>` tags to the configuration file. If you choose this option, you distribute only the configuration file to your clients.

If you generated separate client certificates and keys for each user that will connect to the Client VPN endpoint, repeat this step for each user.

The following is an example of the format of a Client VPN configuration file that includes the client certificate and key.

```
client
dev tun
proto udp
remote cvpn-endpoint-0011abcabcabcabc1.prod.clientvpn.eu-west-2.amazonaws.com 443
remote-random-hostname
resolv-retry infinite
nobind
remote-cert-tls server
cipher AES-256-GCM
verb 3

<ca>
{{Contents of CA}}
</ca>

<cert>
{{Contents of client certificate (.crt) file}}
</cert>

<key>
{{Contents of private key (.key) file}}
</key>

reneg-sec 0
```

## AWS Client VPN routes
<a name="cvpn-working-routes"></a>

Each AWS Client VPN endpoint has a route table that describes the available destination network routes. Each route in the route table determines where the network traffic is directed. You must configure authorization rules for each Client VPN endpoint route to specify which clients have access to the destination network.

When you associate a subnet from a VPC with a Client VPN endpoint, a route for the VPC is automatically added to the Client VPN endpoint's route table. To enable access for additional networks, such as peered VPCs, on-premises networks, the local network (to enable clients to communicate with each other), or the internet, you must manually add a route to the Client VPN endpoint's route table.

**Note**  
If you are associating multiple subnets to the Client VPN endpoint, you should make sure to create a route for each subnet as described here [Troubleshooting AWS Client VPN: Access to a peered VPC, Amazon S3, or the internet is intermittent](#intermittent-access). Each associated subnet should have an identical set of routes.

### Considerations for using split-tunnel on Client VPN endpoints
<a name="split-tunnel-routes"></a>

When you use split-tunnel on a Client VPN endpoint, all of the routes that are in the Client VPN route tables are added to the client route table when the VPN is established. If you add a route after the VPN is established, you must reset the connection so that the new route is sent to the client.

We recommend that you account for the number of routes that the client device can handle before you modify the Client VPN endpoint route table.

**Topics**
+ [Considerations for using split-tunnel on Client VPN endpoints](#split-tunnel-routes)
+ [Create an endpoint route](#cvpn-working-routes-create)
+ [View endpoint routes](#cvpn-working-routes-view)
+ [Delete an endpoint route](#cvpn-working-routes-delete)

### Create an AWS Client VPN endpoint route
<a name="cvpn-working-routes-create"></a>

When you create a Client VPN endpoint route, you specify how traffic for the destination network should be directed.

To allow clients to access the internet, add a destination `0.0.0.0/0` route.

You can add routes to a Client VPN endpoint by using the console and the AWS CLI.

**To create a Client VPN endpoint route (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to which to add the route, choose **Route table**, and then choose **Create route**.

1. For **Route destination**, specify the IPv4 CIDR range for the destination network. For example:
   + To add a route for the VPC of the Client VPN endpoint, enter the VPC's IPv4 CIDR range.
   + To add a route for internet access, enter `0.0.0.0/0`.
   + To add a route for a peered VPC, enter the peered VPC's IPv4 CIDR range.
   + To add a route for an on-premises network, enter the AWS Site-to-Site VPN connection's IPv4 CIDR range.

1. For **Subnet ID for target network association**, select the subnet that is associated with the Client VPN endpoint.

   Alternatively, if you're adding a route for the local Client VPN endpoint network, select `local`.

1. (Optional) For **Description**, enter a brief description for the route.

1. Choose **Create route**.

**To create a Client VPN endpoint route (AWS CLI)**  
Use the [create-client-vpn-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-client-vpn-route.html) command.

### View AWS Client VPN endpoint routes
<a name="cvpn-working-routes-view"></a>

You can view the routes for a specific Client VPN endpoint by using the console or the AWS CLI.

**To view Client VPN endpoint routes (console)**

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint for which to view routes and choose **Route table**.

**To view Client VPN endpoint routes (AWS CLI)**  
Use the [describe-client-vpn-routes](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-routes.html) command.

### Delete an AWS Client VPN endpoint route
<a name="cvpn-working-routes-delete"></a>

You can only delete Client VPN routes that you added manually. You can't delete routes that were automatically added when you associated a subnet with the Client VPN endpoint. To delete routes that were automatically added, you must disassociate the subnet that initiated its creation from the Client VPN endpoint.

You can delete a route from a Client VPN endpoint by using the console or the AWS CLI.

**To delete a Client VPN endpoint route (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint from which to delete the route and choose **Route table**.

1. Select the route to delete, choose **Delete route**, and choose **Delete route**.

**To delete a Client VPN endpoint route (AWS CLI)**  
Use the [delete-client-vpn-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-client-vpn-route.html) command.

## AWS Client VPN target networks
<a name="cvpn-working-target"></a>

A target network is a subnet in a VPC. An AWS Client VPN endpoint must have at least one target network to enable clients to connect to it and establish a VPN connection. 

For more information about the kinds of access that you can configure (such as enabling your clients to access the internet), see [Scenarios and examples for Client VPN](#scenario).

### Client VPN target network requirements
<a name="cvpn-create-target-reqs"></a>

When creating a target network, the following rules apply:
+ The subnet must have a CIDR block with at least a /27 bitmask, for example 10.0.0.0/27. The subnet must also have at least 20 available IP addresses at all times.
+ The subnet's CIDR block cannot overlap with the client CIDR range of the Client VPN endpoint.
+ If you associate more than one subnet with a Client VPN endpoint, each subnet must be in a different Availability Zone. We recommend that you associate at least two subnets to provide Availability Zone redundancy.
+ If you specified a VPC when you created the Client VPN endpoint, the subnet must be in the same VPC. If you haven't yet associated a VPC with the Client VPN endpoint, you can choose any subnet in any VPC. 

  All further subnet associations must be from the same VPC. To associate a subnet from a different VPC, you must first modify the Client VPN endpoint and change the VPC that's associated with it. For more information, see [Modify an AWS Client VPN endpoint](#cvpn-working-endpoint-modify).

When you associate a subnet with a Client VPN endpoint, we automatically add the local route of the VPC in which the associated subnet is provisioned to the Client VPN endpoint's route table.

**Note**  
After your target networks are associated, when you add or remove additional CIDRs to your attached VPC, you must perform one of the following operations to update the local route for your Client VPN endpoint route table:  
Disassociate your Client VPN endpoint from the target network, and then associate the Client VPN endpoint to the target network.
Manually add the route to, or remove the route from the Client VPN endpoint route table.

After you associate the first subnet with the Client VPN endpoint, the Client VPN endpoint's status changes from `pending-associate` to `available` and clients are able to establish a VPN connection.

**Topics**
+ [Requirements for creating a target network](#cvpn-create-target-reqs)
+ [Associate a target network with an endpoint](#cvpn-working-target-associate)
+ [Apply a security group to a target network](#cvpn-working-target-apply)
+ [View target networks](#cvpn-working-target-view)
+ [Disassociate a target network from an endpoint](#cvpn-working-target-disassociate)

### Associate a target network with an AWS Client VPN endpoint
<a name="cvpn-working-target-associate"></a>

You can associate one or more target networks (subnets) with a Client VPN endpoint using either the Amazon VPC Console or the AWS CLI. Before you associate a target network with a Client VPN endpoint, familiarize yourself with the requirements. See [Requirements for creating a target network](#cvpn-create-target-reqs).

**To associate a target network with a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint with which to associate the target network, choose **Target network associations**, and then choose **Associate target network**.

1. For **VPC**, choose the VPC in which the subnet is located. If you specified a VPC when you created the Client VPN endpoint or if you have previous subnet associations, it must be the same VPC.

1. For **Choose a subnet to associate**, choose the subnet to associate with the Client VPN endpoint.

1. Choose **Associate target network**.

**To associate a target network with a Client VPN endpoint (AWS CLI)**  
Use the [associate-client-vpn-target-network](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-client-vpn-target-network.html) command.

### Apply a security group to a target network in AWS Client VPN
<a name="cvpn-working-target-apply"></a>

When you create a Client VPN endpoint, you can specify the security groups to apply to the target network. When you associate the first target network with a Client VPN endpoint, we automatically apply the default security group of the VPC in which the associated subnet is located. For more information, see [Security groups](#security-groups).

You can change the security groups for the Client VPN endpoint. The security group rules that you require depend on the kind of VPN access you want to configure. For more information, see [Scenarios and examples for Client VPN](#scenario).

**To apply a security group to a target network (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to which to apply the security groups.

1. Choose **Security Groups**, and then choose **Apply Security Groups**.

1. Select the appropriate security group(s) from **Security group IDs**.

1. Choose **Apply Security Groups**.

**To apply a security group to a target network (AWS CLI)**  
Use the [apply-security-groups-to-client-vpn-target-network](https://docs.aws.amazon.com/cli/latest/reference/ec2/apply-security-groups-to-client-vpn-target-network.html) command.

### View AWS Client VPN target networks
<a name="cvpn-working-target-view"></a>

You can view the targets associated with a Client VPN endpoint using the console or the AWS CLI.

**To view target networks (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the appropriate Client VPN endpoint and choose **Target network associations**.

**To view target networks using the AWS CLI**  
Use the [describe-client-vpn-target-networks](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-target-networks.html) command.

### Disassociate a target network from an AWS Client VPN endpoint
<a name="cvpn-working-target-disassociate"></a>

When you disassociate a target network, any routes that were manually added to the Client VPN endpoint's route table are deleted, as well as the route that was automatically created when the target network association was made (the local route of the VPC). If you disassociate all target networks from a Client VPN endpoint, clients can no longer establish a VPN connection. 

**To disassociate a target network from a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint with which the target network is associated and choose **Target network associations**.

1. Select the target network to disassociate, choose **Disassociate**, and then choose **Disassociate target network**.

**To disassociate a target network from a Client VPN endpoint (AWS CLI)**  
Use the [disassociate-client-vpn-target-network](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-client-vpn-target-network.html) command.

## AWS Client VPN maximum VPN session duration timeout
<a name="cvpn-working-max-duration"></a>

AWS Client VPN provides several options for the maximum VPN session duration, which is the maximum time allowed for a client connection to the Client VPN endpoint. You can configure a shorter maximum VPN session duration to help meet security and compliance requirements. By default, the maximum VPN session duration is 24 hours. Once you set the maximum session duration, you can control what happens with that session when that timeout is reached. The disconnect on session timeout option allows you to terminate the session or to automatically attempt a reconnection to the endpoint. Terminating a session allows you more control over endpoint security by enforcing maximum VPN session duration. If a session is set to terminate when the maximum time is reached, users will need to reconnect and provide their authentication credentials in order to re-establish the VPN connection. 

When disconnect on session timeout is set to automatically reconnect, and the maximum session time is reached, 
+ a new session is automatically established in the case of cached user credentials (Active Directory) or certificate-based authentication (Mutual Authentication). To fully disconnect and not automatically reconnect, these users should manually disconnect. 
+ a new session is not automatically established in the case of federated authentication (SAML). These users must authenticate again after session timeout expiration to re-establish the VPN connection.

**Note**  
When the maximum VPN session duration value is decreased from its current value, any active VPN sessions that are connected to the endpoint for a time frame longer than the newly set duration are disconnected.
Changing the disconnect on session timeout option applies the new setting to any currently open sessions.
Client VPN enforces the maximum session duration for each connection. If a connection drops and a new connection is started, the maximum session duration timer resets for the new connection.

### Configure the maximum VPN session during creation of an AWS Client VPN endpoint
<a name="configure-max-duration-endpoint-creation"></a>

The duration of a VPN session is configured during the creation of a Client VPN endpoint. See [Create an AWS Client VPN endpoint](#cvpn-working-endpoint-create) for the steps to create a Client VPN endpoint and set the maximum session duration.

**Topics**
+ [Configure the maximum VPN session during creation of an endpoint](#configure-max-duration-endpoint-creation)
+ [View current maximum VPN session duration](#display-max-duration)
+ [Modify the maximum VPN session duration](#modify-max-timeout)

### View AWS Client VPN current maximum VPN session duration
<a name="display-max-duration"></a>

Use the following steps to view the current Client VPN maximum VPN session duration.

**View current maximum VPN session duration for a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint that you want to view.

1. Verify that the **Details** tab is selected.

1. View the current maximum VPN session duration next to **Session timeout hours** and if **Disconnect on timeout** is enabled or disabled.

**View current maximum VPN session duration for a Client VPN endpoint (AWS CLI)**  
Use the [describe-client-vpn-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-endpoints.html) command.

### Modify the maximum AWS Client VPN session duration and timeout behavior
<a name="modify-max-timeout"></a>

Use the following steps to modify an existing Client VPN maximum VPN session duration and change the disconnect on session timeout behavior.

**Modify an existing maximum VPN session duration for a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN endpoints**.

1. Select the Client VPN endpoint that you want to modify, choose **Actions**, and then choose **Modify Client VPN Endpoint**.

1. For **Session timeout hours**, choose the desired maximum VPN session duration time in hours.

1. For **Disconnect on session timeout**, choose if you want to disconnect a session when the maximum session timeout is reached. By default, this is turned off the first time you modify an endpoint. 

1. Choose **Modify Client VPN endpoint**.

**Modify an existing maximum VPN session duration for a Client VPN endpoint (AWS CLI)**  
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.

## Transit Gateway integration with Client VPN
<a name="cvpn-tgw"></a>

You can attach a Client VPN endpoint natively to a Transit Gateway for secure remote access to multiple VPCs, on-premises networks, and other resources connected to the Transit Gateway. This eliminates the need to create separate VPN endpoints for each VPC or manage complex routing through intermediate VPCs.

**Topics**
+ [Overview](#cvpn-tgw-overview)
+ [Benefits](#cvpn-tgw-benefits)
+ [How Transit Gateway integration works](#cvpn-tgw-how-it-works)
+ [Prerequisites](#cvpn-tgw-prerequisites)
+ [Create a Transit Gateway Client VPN endpoint](#cvpn-tgw-create)
+ [Manage routes](#cvpn-tgw-routes)
+ [Configure authorization](#cvpn-tgw-authorization)
+ [Manage Availability Zones](#cvpn-tgw-manage-azs)
+ [Cross-account Transit Gateway access](#cvpn-tgw-cross-account)
+ [Considerations and limitations](#cvpn-tgw-limitations)

### Overview
<a name="cvpn-tgw-overview"></a>

When you associate a Transit Gateway with a Client VPN endpoint, the connected VPN clients can access all the resources connected to the Transit Gateway if appropriate routes and authorization rules are configured in the Client VPN endpoint.

Transit Gateway-associated endpoints preserve the client source IP address. Source network address translation (SNAT) is not applied, which provides enhanced visibility into client traffic.

**Important**  
You cannot mix VPC subnet associations and Transit Gateway associations in a single Client VPN endpoint. Choose one association type when you create the endpoint.

### Benefits
<a name="cvpn-tgw-benefits"></a>

Transit Gateway integration with Client VPN provides the following benefits:
+ **Simplified management** — Eliminate the need for separate VPN endpoints per VPC. No need to create intermediate VPCs solely for VPN termination.
+ **Centralized routing** — Leverage Transit Gateway as a central routing hub. Simplify route management across your network.
+ **Enhanced visibility** — Preserve client source IP addresses (no SNAT). Provides flow logs support for Client VPN.
+ **Scalability** — Easily add new VPCs to your Transit Gateway which can be accessed through Client VPN. Scale to support large remote workforces and business units.
+ **Centralized security** — Implement consistent security policies across all connected networks. Maintain comprehensive audit trails.

### How Transit Gateway integration works
<a name="cvpn-tgw-how-it-works"></a>

The following describes how Client VPN works with Transit Gateway:

1. **Endpoint creation** — You create a Client VPN endpoint and specify the Transit Gateway ID.

1. **Attachment creation** — AWS automatically creates a Transit Gateway attachment of type `client-vpn` for the endpoint.

1. **Availability Zone selection** — You specify which Availability Zones to use, or AWS selects 2 Availability Zones automatically.

1. **Route configuration** — You add routes to the Client VPN endpoint route table to direct client traffic to destination networks through the Transit Gateway.

1. **Client connection flow** — When a client connects, traffic flows from the client through the Client VPN endpoint to the Transit Gateway, and then to the destination network based on Transit Gateway route tables.

![Transit Gateway traffic flow with Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/cvpn-tgw-traffic-flow.png)


### Prerequisites
<a name="cvpn-tgw-prerequisites"></a>

Before you create a Transit Gateway-associated Client VPN endpoint, verify the following requirements.

Transit Gateway requirements  
+ An existing Transit Gateway in the same Region as the Client VPN endpoint.
+ For cross-account access, the Transit Gateway must be shared with your account through AWS Resource Access Manager.
+ The Transit Gateway must have an IPv4 CIDR block assigned. If you plan to use IPv6 or dual-stack configuration, also assign an IPv6 CIDR block.

Network requirements  
+ The client CIDR range must not overlap with the CIDR ranges of VPCs attached to the Transit Gateway.
+ The Availability Zones you select must be supported by the Transit Gateway.
+ Return routes must be configured in VPC route tables to direct traffic destined for the client CIDR range to the Transit Gateway.

Certificate requirements  
+ A server certificate provisioned in AWS Certificate Manager (ACM) in the same Region as the Client VPN endpoint.
+ If you use mutual authentication, a client certificate provisioned in ACM.

### Create a Transit Gateway Client VPN endpoint
<a name="cvpn-tgw-create"></a>

You can create a Client VPN endpoint associated with a Transit Gateway by using the console or the AWS CLI.

**To create a Transit Gateway Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints** and then choose **Create Client VPN Endpoint**.

1. (Optional) For **Name tag** and **Description**, enter a name and description for the endpoint.

1. For **Traffic IP address type**, choose one of the following:
   + **IPv4** — Specify a client IPv4 CIDR range (for example, `10.0.0.0/22`).
   + **IPv6** — AWS automatically assigns the client IPv6 CIDR range.
   + **Dual stack** — Specify a client IPv4 CIDR range. AWS automatically assigns the client IPv6 CIDR range.

1. For **Server certificate ARN**, specify the ARN for the TLS certificate provisioned in ACM.

1. Choose your authentication method. For more information, see [Client authentication in AWS Client VPN](#client-authentication).

1. (Optional) For **Connection logging**, turn on **Enable log details on client connections** and specify the CloudWatch Logs log group and log stream.

1. For **Network Infrastructure**, choose **Transit Gateway**.

1. For **Transit Gateway ID**, select the Transit Gateway from the dropdown list.

1. (Optional) For **Availability Zones**, select up to 5 Availability Zones. If you do not select Availability Zones, AWS automatically selects 2.

1. (Optional) Configure additional settings such as DNS servers, transport protocol, split-tunnel, VPN port, session timeout, and login banner.

1. Choose **Create Client VPN endpoint**.

**Note**  
After creation, the endpoint state is `pending-associate`. The Transit Gateway attachment is created automatically. Clients can connect after the attachment becomes available.

**To create a Transit Gateway Client VPN endpoint (AWS CLI)**  
Use the [create-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-client-vpn-endpoint.html) command with the `--transit-gateway-id` parameter.

The following example creates a Client VPN endpoint with specific Availability Zones:

```
aws ec2 create-client-vpn-endpoint \
    --client-cidr-block 10.0.0.0/22 \
    --server-certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE \
    --authentication-options Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:us-east-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE} \
    --connection-log-options Enabled=false \
    --transit-gateway-id tgw-0a1b2c3d4e5f6EXAMPLE \
    --availability-zone-list us-east-1a us-east-1b us-east-1c
```

Example output:

```
{
    "ClientVpnEndpointId": "cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE",
    "Status": {
        "Code": "pending-associate"
    },
    "DnsName": "cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE.prod.clientvpn.us-east-1.amazonaws.com"
}
```

To let AWS automatically select 2 Availability Zones, omit the `--availability-zone-list` parameter:

```
aws ec2 create-client-vpn-endpoint \
    --client-cidr-block 10.0.0.0/22 \
    --server-certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE \
    --authentication-options Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:us-east-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE} \
    --connection-log-options Enabled=false \
    --transit-gateway-id tgw-0a1b2c3d4e5f6EXAMPLE
```

#### Verify the Transit Gateway attachment
<a name="cvpn-tgw-verify"></a>

After you create the endpoint, verify that the Transit Gateway attachment was created.

**To verify the Transit Gateway attachment (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit Gateway Attachments**.

1. Locate the attachment with **Resource type** = `client-vpn` and **Resource ID** matching your Client VPN endpoint ID.

1. Verify that the **State** is `available`.

**To verify the Transit Gateway attachment (AWS CLI)**  
Use the [describe-transit-gateway-attachments](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-attachments.html) command.

```
aws ec2 describe-transit-gateway-attachments \
    --filters Name=transit-gateway-id,Values=tgw-0a1b2c3d4e5f6EXAMPLE Name=resource-type,Values=client-vpn
```

To view the Transit Gateway configuration for the endpoint, use the [describe-client-vpn-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-endpoints.html) command:

```
aws ec2 describe-client-vpn-endpoints \
    --client-vpn-endpoint-ids cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE
```

The output includes a `TransitGatewayConfiguration` object with the Transit Gateway ID and associated Availability Zones.

### Manage routes
<a name="cvpn-tgw-routes"></a>

**Important**  
For Transit Gateway-associated endpoints, you do not specify a target subnet ID when you create routes. Traffic is automatically directed through the Transit Gateway attachment.

**To add a route (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint, choose **Route table**, and then choose **Create route**.

1. For **Route destination**, enter the destination CIDR range (for example, `10.1.0.0/16` for a VPC or `0.0.0.0/0` for all traffic).

1. (Optional) For **Description**, enter a description for the route.

1. Choose **Create route**.

**To add a route (AWS CLI)**  
Use the [create-client-vpn-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-client-vpn-route.html) command without the `--target-vpc-subnet-id` parameter.

```
aws ec2 create-client-vpn-route \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --destination-cidr-block 10.1.0.0/16
```

To add multiple routes, run the command for each destination CIDR range:

```
# Route to VPC 1
aws ec2 create-client-vpn-route \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --destination-cidr-block 10.1.0.0/16

# Route to VPC 2
aws ec2 create-client-vpn-route \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --destination-cidr-block 10.2.0.0/16

# Route to on-premises network
aws ec2 create-client-vpn-route \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --destination-cidr-block 192.168.0.0/16
```

**To delete a route (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint, choose **Route table**, select the route, and then choose **Delete route**.

1. Choose **Delete route** to confirm.

**To delete a route (AWS CLI)**  
Use the [delete-client-vpn-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-client-vpn-route.html) command.

```
aws ec2 delete-client-vpn-route \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --destination-cidr-block 10.1.0.0/16
```

### Configure authorization
<a name="cvpn-tgw-authorization"></a>

**Important**  
Security group-based authorization is not supported for Transit Gateway-associated Client VPN endpoints. You must use network-based authorization rules to control client access.

**To add an authorization rule (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint, choose **Authorization rules**, and then choose **Add authorization rule**.

1. For **Destination network to enable access**, enter the destination CIDR range (for example, `10.1.0.0/16`).

1. For **Grant access to**, choose one of the following:
   + **Allow access to all users** — All authenticated clients can access the destination network.
   + **Allow access to users in a specific access group** — Enter the Active Directory group SID or IdP group name in **Access group ID**.

1. Choose **Add authorization rule**.

**To add an authorization rule (AWS CLI)**  
Use the [authorize-client-vpn-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/authorize-client-vpn-ingress.html) command.

The following example authorizes all users to access the `10.1.0.0/16` network:

```
aws ec2 authorize-client-vpn-ingress \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --target-network-cidr 10.1.0.0/16 \
    --authorize-all-groups
```

The following example authorizes a specific Active Directory group:

```
aws ec2 authorize-client-vpn-ingress \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --target-network-cidr 10.1.0.0/16 \
    --access-group-id S-1-2-34-1234567890-1234567890-1234567890-1234
```

### Manage Availability Zones
<a name="cvpn-tgw-manage-azs"></a>

You can modify the Availability Zones for a Transit Gateway-associated Client VPN endpoint after creation.

**To add a single Availability Zone (AWS CLI)**  
Use the [associate-client-vpn-target-network](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-client-vpn-target-network.html) command with the `--availability-zone` parameter.

```
aws ec2 associate-client-vpn-target-network \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --availability-zone us-east-1c
```

**To remove a single Availability Zone (AWS CLI)**  
First, use the [describe-client-vpn-target-networks](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-target-networks.html) command to find the association ID for the Availability Zone.

```
aws ec2 describe-client-vpn-target-networks \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE
```

Then use the [disassociate-client-vpn-target-network](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-client-vpn-target-network.html) command with the association ID.

```
aws ec2 disassociate-client-vpn-target-network \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --association-id cvpn-assoc-0a1b2c3d4e5f6EXAMPLE
```

### Cross-account Transit Gateway access
<a name="cvpn-tgw-cross-account"></a>

You can create a Client VPN endpoint associated with a Transit Gateway that is owned by a different AWS account. To do this, the Transit Gateway owner must share the Transit Gateway with your account through AWS Resource Access Manager.

Prerequisites  
+ **Transit Gateway owner account** — An existing Transit Gateway and permissions to create resource shares in AWS Resource Access Manager.
+ **Client VPN endpoint account** — Permissions to create Client VPN endpoints and accept AWS Resource Access Manager resource shares.

In the Client VPN endpoint account, accept the resource share in the AWS Resource Access Manager console or by using the [accept-resource-share-invitation](https://docs.aws.amazon.com/cli/latest/reference/ram/accept-resource-share-invitation.html) command. After you accept the share, the Transit Gateway appears in the Transit Gateway ID dropdown when you create a Client VPN endpoint.

### Considerations and limitations
<a name="cvpn-tgw-limitations"></a>

Consider the following when you use Transit Gateway integration with Client VPN:
+ **Association restrictions**
  + You cannot mix VPC subnet associations and Transit Gateway associations in a single endpoint.
  + Each endpoint must use exclusively one association type.
+ **Security groups**
  + Security group-based authorization is not supported for Transit Gateway endpoints.
  + Use network-based authorization rules only.
+ **Route management**
  + Automatic route propagation from Transit Gateway is not supported.
  + You must manually define routes for destination networks.
+ **CIDR overlap**
  + Client VPN CIDR block should not overlap with other Transit Gateway attachments or Transit Gateway CIDR blocks.
  + Transit Gateway does not support overlapping CIDR ranges across attached VPCs.
+ **Regional limitation**
  + Client VPN endpoint and Transit Gateway must be in the same AWS Region.
  + Cross-region Transit Gateway peering is not supported for Client VPN.
+ **Availability Zones**
  + You can specify up to 5 Availability Zones per endpoint.
  + If not specified, AWS automatically assigns 2 Availability Zones.
  + All specified Availability Zones must be supported by both Client VPN and Transit Gateway.
+ **Return routing**
  + VPCs connected to the Transit Gateway must have return routes configured to route traffic destined for the Client VPN CIDR back to the Transit Gateway.
  + Without proper return routing, VPN clients cannot access resources in the VPCs.
    + **For IPv4**: The Client VPN CIDR is known at endpoint creation time.
    + **For IPv6**: You must describe the Transit Gateway route table to determine the IPv6 CIDR range assigned to the Client VPN endpoint (the largest CIDR range in the Transit Gateway Route Table associated with the Client VPN endpoint), as IPv6 client CIDR ranges are automatically assigned by AWS Client VPN.
+ **Connection and flow logs**
  + [Transit Gateway flow logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html) can be enabled to capture information about the IP traffic going to and from your Transit Gateways. [Client VPN connection logs](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-with-connection-logs.html) can be enabled to capture information about Client VPN connection events.
  + You can correlate a Transit Gateway flow log event to a Client VPN connection by comparing a client IP and time stamp in a Transit Gateway flow log event to the same client IP and time period in the Client VPN connection logs.
+ **Internet connectivity**
  + To access the internet through Client VPN with Transit Gateway, without split tunnel, an attached VPC must have NAT configured.
    + **For IPv4**: Configure a NAT Gateway to replace Client VPN client IPs with a public IP address.
    + **For IPv6**: See [Centralized internet outbound traffic with IPv6](https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/advanced-dual-stack-and-ipv6-only-network-designs.html#centralized-internet-outbound-traffic-with-ipv6).

# Device posture for AWS Client VPN
<a name="device-posture"></a>

With AWS Client VPN device posture, you can control access to your network based on the security health of the connecting device, not just the identity of the user. When device posture is enabled, Client VPN evaluates the health of each device before it grants access, and continues to evaluate it for the life of the session.

To use device posture, you configure a device trust provider (CrowdStrike, Jamf, or JumpCloud) on your Client VPN endpoint. The provider makes a device posture token available on each device — a signed claim that describes the device's health, such as its compliance status or disk encryption state. You define the requirements that a device must meet in an authorization policy. Client VPN evaluates the token against this policy each time a device connects, and again every 5 minutes for the life of the session. Client VPN denies connections and disconnects sessions that do not meet your requirements. For example, you can require that only devices with disk encryption enabled can connect, or that only devices with an active firewall can remain connected.

**Important**  
Device posture relies on device trust providers that you configure and manage. AWS does not control or operate these third-party providers. You are responsible for configuring your device trust provider, defining your authorization policy, and ensuring your devices meet your compliance requirements. Client VPN evaluates the device posture tokens that these providers make available, but does not independently verify the health of your devices.

Each device trust provider must also be set up on the connecting device. For links to each provider's setup documentation, see [Supported device trust providers](#device-posture-providers). Device-side setup steps for your end users are documented in the AWS Client VPN User Guide.

## How device posture works
<a name="device-posture-how-it-works"></a>

Device posture builds on your existing Client VPN authentication. It requires the AWS provided client version 6.2.0 or later. When device posture is enabled on an endpoint, Client VPN adds a device health check to each connection:

1. A user initiates a connection and authenticates as they do today, using mutual authentication, SAML, or Active Directory.

1. Before the connection is established, the AWS provided client obtains the device posture token that the device trust provider makes available on the device, and sends it to Client VPN.

1. Client VPN validates the device posture token, then evaluates your authorization policy against a combination of the device posture token, the authenticated user identity, and the connection details.

1. If the policy allows the request, the connection is established. If the policy denies the request, the connection is refused and the AWS provided client displays the message `Authorization policy evaluation failed`.

1. Every 5 minutes, Client VPN re-evaluates the policy against the most recent device posture token. The AWS provided client refreshes the token independently, on its own schedule. If a device no longer meets your requirements, Client VPN ends the session. If the device stops providing a token, Client VPN evaluates against the last token it received for up to 15 minutes. After 15 minutes without a new token, Client VPN drops the token.

## Concepts
<a name="device-posture-concepts"></a>

The following concepts are central to how device posture works.

**Device trust provider**  
The configuration on an endpoint that represents your third-party device trust vendor (CrowdStrike, Jamf, or JumpCloud). In the API, device trust providers are configured under `DevicePostureOptions`, which has an `Enabled` field that you must set to `true` to turn on device posture, and a `TrustProviders` list. Each entry has a `TrustProviderType` of `crowdstrike`, `jamf`, or `jumpcloud`. You can configure one or more trust providers on an endpoint.

**Device posture token**  
A signed claim, made available on the device by the device trust provider, that describes the device's health, such as compliance status, disk encryption state, or a risk score. The device posture token is the input Client VPN evaluates to decide whether a device meets your requirements. The AWS provided client refreshes the token on its own schedule, independently of Client VPN's policy re-evaluation.

**Authorization policy**  
A policy, written in the Cedar policy language, that defines the requirements a connection must meet. You attach one policy to an endpoint. Client VPN evaluates it when a device connects and on each re-evaluation during the session.

**Shadow mode**  
A mode in which Client VPN evaluates the authorization policy and records the decision in your connection logs without blocking any connections. Use shadow mode to validate a policy against real traffic before you enforce it.

## Prerequisites
<a name="device-posture-prerequisites"></a>

Before you configure device posture, make sure you have the following.
+ An account with a supported device trust provider (CrowdStrike, Jamf, or JumpCloud), configured on each device that connects. For details, see [Supported device trust providers](#device-posture-providers).
+ The AWS provided client, version 6.2.0 or later. Device posture is not supported with third-party OpenVPN clients.
+ A Client VPN endpoint, either an existing one or a new one that you create when you configure device posture.

## Step 1: Configure a device trust provider
<a name="device-posture-step1"></a>

Configure your device trust provider on the endpoint using device posture options. You can set this when you create an endpoint or modify an existing one. Set `Enabled` to `true` to turn on device posture, and provide one or more trust providers. Each trust provider specifies the provider type, your tenant identifier with that provider, and the URL of the provider's public signing key, which Client VPN uses to validate the device posture tokens it receives.

```
aws ec2 create-client-vpn-endpoint \
  --client-cidr-block 10.0.0.0/16 \
  --server-certificate-arn arn:aws:acm:us-east-1:111122223333:certificate/EXAMPLE \
  --authentication-options Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:us-east-1:111122223333:certificate/EXAMPLE} \
  --device-posture-options '{"Enabled":true,"TrustProviders":[{"TrustProviderType":"crowdstrike","TenantId":"EXAMPLE-TENANT-ID","PublicSigningKeyUrl":"https://assets-public.falcon.crowdstrike.com/zta/jwk.json"}]}' \
  --connection-log-options '{"Enabled":true,"CloudwatchLogGroup":"/aws/clientvpn/logs","CloudwatchLogStream":"cvpn-stream","IncludeAuthorizationPolicyContext":true}'
```

You can configure more than one trust provider on a single endpoint (for example, to allow both macOS devices managed by Jamf and Windows devices managed by CrowdStrike). Verify the configuration with `describe-client-vpn-endpoints`; the response includes a `DevicePostureOptions` block listing each configured trust provider.

## Step 2: Author an authorization policy
<a name="device-posture-step2"></a>

An authorization policy is a Cedar document that defines the requirements a connection must meet. Client VPN evaluates the policy against a context made up of three kinds of information:
+ Device signals — the health signals carried in the device posture token. Namespaces: `context.crowdstrike.*`, `context.jamf.*`, `context.jumpcloud.*`.
+ User identity — captured once when the device connects. Namespace depends on auth type: `context.saml.*`, `context.active-directory.*`, or `context.mutual-authentication.*`.
+ Connection details — always available: `context.connection.*` (endpoint ID, connection ID, platform, platform version, public IP address, client OpenVPN version, and AWS provided client version).

```
permit(principal, action, resource)
when { context.crowdstrike.assessment.overall > 50 };
```

For more examples, the policy API, and guidance on writing conditions, see [Authoring device posture authorization policies](#device-posture-policies).

## Step 3: Test the policy in shadow mode
<a name="device-posture-step3"></a>

Attach the policy with shadow mode enabled. In shadow mode, Client VPN evaluates the policy and records the decision in your connection logs, but never blocks a connection.

```
aws ec2 modify-client-vpn-endpoint-authorization-policy \
  --client-vpn-endpoint-id cvpn-endpoint-EXAMPLE \
  --policy-document 'permit(principal, action, resource) when { context.crowdstrike.assessment.overall > 50 };' \
  --description "Require CrowdStrike ZTA" \
  --shadow-mode enabled
```

Confirm the attached policy with `get-client-vpn-endpoint-authorization-policy`.

## Step 4: Enforce the policy
<a name="device-posture-step4"></a>

When you are satisfied with the shadow-mode results, disable shadow mode to start enforcing the policy.

```
aws ec2 modify-client-vpn-endpoint-authorization-policy \
  --client-vpn-endpoint-id cvpn-endpoint-EXAMPLE \
  --shadow-mode disabled
```

**Note**  
Client VPN disconnects all active sessions on an endpoint when you add or update a Cedar policy with shadow mode disabled, or when you change shadow mode from enabled to disabled.

To stop evaluating device posture, remove the policy with `delete-client-vpn-endpoint-authorization-policy`. This stops evaluation for both new connections and existing sessions on the endpoint, but the AWS provided client continues to provide a device posture token as long as the client profile contains the `aws-auth-device-posture` directive. To turn off device posture completely, also remove the trust provider from the endpoint's device posture options, then have users download the client configuration again and re-import the profile so that the device posture configuration is no longer present.

For information about monitoring device posture decisions, see [Monitoring AWS Client VPN](#monitoring-overview). For device posture considerations and limits, see [AWS Client VPN quotas](#limits).

## Supported device trust providers
<a name="device-posture-providers"></a>

AWS Client VPN device posture supports the following device trust providers. You configure each one on your endpoint. The provider makes a device posture token available on the connecting device, which Client VPN evaluates against your authorization policy.


**Provider support by operating system**  

| Device trust provider | Supported operating systems | 
| --- | --- | 
| CrowdStrike | macOS, Windows | 
| Jamf | macOS | 
| JumpCloud | macOS, Windows, Ubuntu | 

Each provider documents how to set up device trust on the connecting device. For more information, see the following documentation on each provider's website:
+ CrowdStrike — [CrowdStrike Zero Trust Assessment](https://developer.crowdstrike.com/falcon-mcp/modules/zero-trust-assessment/)
+ Jamf — [Jamf Trusted Access](https://trusted.jamf.com/docs/enabling-access-for-trusted-devices)
+ JumpCloud — [JumpCloud Device Trust](https://www.jumpcloud.com/support/understand-device-trust-readiness)

### Configuring a trust provider
<a name="device-posture-providers-config"></a>

For each trust provider you configure on an endpoint, supply these values in the endpoint's device posture options:


**Trust provider fields**  

| Field | Example | Description | 
| --- | --- | --- | 
| TrustProviderType | crowdstrike, jamf, jumpcloud | The type of device trust provider. | 
| TenantId | EXAMPLE-TENANT-ID | Your tenant identifier with the provider. | 
| PublicSigningKeyUrl | https://assets-public.falcon.crowdstrike.com/zta/jwk.json | The URL of the provider's public signing key. This example is specific to CrowdStrike. | 

**Note**  
`PublicSigningKeyUrl` is not required when the trust provider type is `jamf`.

### Trust data reference
<a name="device-posture-providers-trust-data"></a>

Each device trust provider populates its own Cedar namespace with health signals carried in the device posture token. You reference these fields in your authorization policy conditions. The available fields depend on the provider.

#### CrowdStrike (context.crowdstrike.\*)
<a name="device-posture-trust-data-crowdstrike"></a>

When CrowdStrike is configured as a trust provider, the following fields are available in the Cedar context under the `context.crowdstrike` namespace.


| Field | Type | Description | 
| --- | --- | --- | 
| assessment.overall | integer | A single metric between 1-100 that is a weighted average of the OS and sensor config scores. | 
| assessment.os | integer | A single metric between 1-100 that accounts for OS-specific settings monitored on the host. | 
| assessment.sensor\_config | integer | A single metric between 1-100 that accounts for the sensor policies monitored on the host. | 
| assessment.version | string | The version of the scoring algorithm. | 
| cid | string | Customer ID (CID) unique to the customer's environment. | 
| platform | string | Operating system of the endpoint (Windows 10, Windows 11, or macOS). | 
| serial\_number | string | The serial number of the device. | 

The following example policy permits access when the overall assessment score is greater than 50.

```
permit(principal, action, resource)
when { context.crowdstrike.assessment.overall > 50 };
```

#### Jamf (context.jamf.\*)
<a name="device-posture-trust-data-jamf"></a>

When Jamf is configured as a trust provider, the following fields are available in the Cedar context under the `context.jamf` namespace.


| Field | Type | Description | 
| --- | --- | --- | 
| risk | string | A Jamf-reported level of risk associated with the device. Valid values: HIGH, MEDIUM, LOW, SECURE, NOT\_APPLICABLE. | 
| groups | array of strings | Group IDs from the UEM connector sync. | 
| osv | string | The version of the OS currently running, in Apple version number format. | 

The following example policy permits access when the reported risk is `LOW` or `SECURE`.

```
permit(principal, action, resource)
when { ["LOW", "SECURE"].contains(context.jamf.risk) };
```

#### JumpCloud (context.jumpcloud.\*)
<a name="device-posture-trust-data-jumpcloud"></a>

When JumpCloud is configured as a trust provider, the following fields are available in the Cedar context under the `context.jumpcloud` namespace.


| Field | Type | Description | 
| --- | --- | --- | 
| device.is\_managed | boolean | Indicates whether the device is under management. | 
| org\_id | string | The JumpCloud organization ID. | 
| system | string | The JumpCloud system ID. | 
| durt\_id | string | Device User Refresh Token ID. A unique ID that represents the device and user combination. | 

The following example policy permits access when the device is under management.

```
permit(principal, action, resource)
when { context.jumpcloud.device.is_managed == true };
```

## Authoring device posture authorization policies
<a name="device-posture-policies"></a>

A device posture authorization policy defines the requirements a device must meet to connect to your Client VPN endpoint and to stay connected. You write the policy in Cedar, an open-source policy language. Client VPN evaluates the policy against a context that combines the device posture token, the authenticated user identity, and the connection details, and returns an allow or deny decision.

For an introduction to the Cedar language and its syntax, see the [Cedar documentation](https://docs.cedarpolicy.com/) and the [Cedar policy syntax reference](https://docs.cedarpolicy.com/policies/syntax-policy.html).

### Test policy
<a name="device-posture-policy-assistant"></a>

Test policy is a tool in the AWS Management Console, on the **Authorization** tab of your Client VPN endpoint, that you can use to test and develop your authorization policies. It presents the authorization policy, the device posture token context, and the user identity context on one screen, where you can test policies and make edits.

Device posture token formats vary across different trust providers, and you might not know the exact format a particular trust provider uses. Test policy shows you the trust context alongside your policy, so you can develop and test policies against real data.

The following sections describe how to use Test policy.

#### Step 1: Select filters and test the policy
<a name="device-posture-policy-assistant-step1"></a>

In the **Test policy** view, you select filters to load a connection's context, then edit and test your policy against that context. The Client VPN endpoint is selected automatically. You can set the following filters:
+ **Authorization decision** (required) — the most recent allow or deny decision to use from the connection logs.
+ **Device identifier** (optional) — the unique device identifier.
+ **User** (optional) — the user identifier.
+ **Operating system** (optional) — the device operating system.

**To select filters and test a policy**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN endpoints**, then choose the endpoint ID for the endpoint you want to work with.

1. Choose the **Authorization** tab, then choose **Test policy**.

1. Set **Authorization decision**, which is required. Optionally, set **Device identifier**, **User**, and **Operating system**.

1. Choose **Search connections**. Test policy displays the trust context sent by your device trust provider, the user identity context, and the Cedar authorization policy for the Client VPN endpoint.

1. Review the trust context alongside the policy. Edit the Cedar policy, then choose **Test policy** to evaluate it against the loaded context. Repeat until you are satisfied with the result.

1. Choose **Save**.

**Note**  
The trust and identity contexts are static. You can view them alongside the policy to understand what data is available for your policy conditions, but you cannot edit them.

#### Step 2: Review and save the policy
<a name="device-posture-policy-assistant-step2"></a>

After you choose **Save** in Step 1, review your changes in the policy to confirm they are correct.

**To review and save the policy**

1. Review the changes in the policy.

1. Choose **Save policy**.

### How Client VPN uses Cedar
<a name="device-posture-policies-cedar"></a>

A Client VPN authorization policy is made up of one or more Cedar `permit` and `forbid` statements. A connection is allowed only if it satisfies at least one `permit` statement and is not matched by any `forbid` statement. A `forbid` statement always takes precedence.

The following example permits a connection when the CrowdStrike overall assessment score is greater than 50.

```
permit(principal, action, resource)
when { context.crowdstrike.assessment.overall > 50 };
```

The following example combines a device signal with a user identity signal. It permits a connection only when the device has disk encryption enabled (a Jamf signal) and the user belongs to the `Engineering` SAML group.

```
permit(principal, action, resource)
when {
    context.jamf.diskEncryptionEnabled == true &&
    context.saml.memberOf.contains("Engineering")
};
```

The following example combines a `permit` statement with a `forbid` statement. It permits connections that meet the assessment score requirement, but always denies connections from devices that report a jailbroken state, regardless of any `permit` statement.

```
permit(principal, action, resource)
when { context.crowdstrike.assessment.overall > 50 };

forbid(principal, action, resource)
when { context.crowdstrike.jailbroken == true };
```

### Create or update a policy
<a name="device-posture-policies-create"></a>

To attach or replace the authorization policy on an endpoint, use `modify-client-vpn-endpoint-authorization-policy`.

```
aws ec2 modify-client-vpn-endpoint-authorization-policy \
  --client-vpn-endpoint-id cvpn-endpoint-EXAMPLE \
  --policy-document 'permit(principal, action, resource) when { context.crowdstrike.assessment.overall > 50 };' \
  --description "Require CrowdStrike ZTA" \
  --shadow-mode enabled
```

### View a policy
<a name="device-posture-policies-view"></a>

To retrieve the authorization policy attached to an endpoint, use `get-client-vpn-endpoint-authorization-policy`.

```
aws ec2 get-client-vpn-endpoint-authorization-policy \
  --client-vpn-endpoint-id cvpn-endpoint-EXAMPLE
```

### Delete a policy
<a name="device-posture-policies-delete"></a>

To remove the authorization policy from an endpoint, use `delete-client-vpn-endpoint-authorization-policy`. This stops evaluation for both new connections and existing sessions on the endpoint.

```
aws ec2 delete-client-vpn-endpoint-authorization-policy \
  --client-vpn-endpoint-id cvpn-endpoint-EXAMPLE
```

### Considerations when writing policies
<a name="device-posture-policies-considerations"></a>

Keep the following in mind when you write authorization policies.
+ A policy document can be a maximum of 10,000 bytes.
+ Namespace availability depends on your trust provider configuration. A namespace is available only when you have configured the corresponding trust provider on the endpoint.
+ User identity signals are captured once when the device connects, and do not change during a session.

# Security in AWS Client VPN
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data centers and network architectures that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS Client VPN, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations. 

AWS Client VPN is part of the Amazon VPC service. For more information about security in Amazon VPC, see [Security](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html) in the *Amazon VPC User Guide*. 

This documentation helps you understand how to apply the shared responsibility model when using Client VPN. The following topics show you how to configure Client VPN to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Client VPN resources. 

**Topics**
+ [Data protection](#data-protection)
+ [Identity and access management](#security-iam)
+ [Resilience](#disaster-recovery-resiliency)
+ [Infrastructure security](#infrastructure-security)
+ [Best practices](#security-best-practices)
+ [IPv6 considerations](#ipv6-considerations)

## Data protection in AWS Client VPN
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS Client VPN. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Client VPN or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

### Encryption in transit
<a name="encryption-in-transit"></a>

AWS Client VPN provides secure connections from any location using Transport Layer Security (TLS) 1.2 or later.

### Internetwork traffic privacy
<a name="internetwork-traffic-privacy"></a>

**Enabling internetwork access**  
You can enable clients to connect to your VPC and other networks through a Client VPN endpoint. For more information and examples, see [Scenarios and examples for Client VPN](#scenario).

**Restricting access to networks**  
You can configure your Client VPN endpoint to restrict access to specific resources in your VPC. For user-based authentication, you can also restrict access to parts of your network, based on the user group that accesses the Client VPN endpoint. For more information, see [Restrict access to your network using Client VPN](#scenario-restrict).

**Authenticating clients**  
Authentication is implemented at the first point of entry into the AWS Cloud. It is used to determine whether clients are allowed to connect to the Client VPN endpoint. If authentication succeeds, clients connect to the Client VPN endpoint and establish a VPN session. If authentication fails, the connection is denied and the client is prevented from establishing a VPN session.  
Client VPN offers the following types of client authentication:   
+ [Active Directory authentication](#ad) (user-based)
+ [Mutual authentication](#mutual) (certificate-based)
+ [Single sign-on (SAML-based federated authentication)](#federated-authentication) (user-based)

## Identity and access management for AWS Client VPN
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use Client VPN resources. IAM is an AWS service that you can use with no additional charge.

**Topics**
+ [Audience](#security_iam_audience)
+ [Authenticating with identities](#security_iam_authentication)
+ [Managing access using policies](#security_iam_access-manage)
+ [How AWS Client VPN works with IAM](#security_iam_service-with-iam)
+ [Identity-based policy examples](#security_iam_id-based-policy-examples)
+ [Troubleshooting](#security_iam_troubleshoot)
+ [Using service-linked roles](#using-service-linked-roles)

### Audience
<a name="security_iam_audience"></a>

How you use AWS Identity and Access Management (IAM) differs based on your role:
+ **Service user** - request permissions from your administrator if you cannot access features (see [Troubleshooting AWS Client VPN identity and access](#security_iam_troubleshoot))
+ **Service administrator** - determine user access and submit permission requests (see [How AWS Client VPN works with IAM](#security_iam_service-with-iam))
+ **IAM administrator** - write policies to manage access (see [Identity-based policy examples for AWS Client VPN](#security_iam_id-based-policy-examples))

### Authenticating with identities
<a name="security_iam_authentication"></a>

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in the *IAM User Guide*.

#### AWS account root user
<a name="security_iam_authentication-rootuser"></a>

 When you create an AWS account, you begin with one sign-in identity called the AWS account *root user* that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) in the *IAM User Guide*. 

#### Federated identity
<a name="security_iam_authentication-federated"></a>

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A *federated identity* is a user from your enterprise directory, web identity provider, or Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) in the *AWS IAM Identity Center User Guide*.

#### IAM users and groups
<a name="security_iam_authentication-iamuser"></a>

An *[IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)* is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) in the *IAM User Guide*.

An [*IAM group*](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html) specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/gs-identities-iam-users.html) in the *IAM User Guide*.

#### IAM roles
<a name="security_iam_authentication-iamrole"></a>

An *[IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)* is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html) or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage-assume.html) in the *IAM User Guide*.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

### Managing access using policies
<a name="security_iam_access-manage"></a>

You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy defines permissions when associated with an identity or resource. AWS evaluates these policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For more information about JSON policy documents, see [Overview of JSON policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json) in the *IAM User Guide*.

Using policies, administrators specify who has access to what by defining which **principal** can perform **actions** on what **resources**, and under what **conditions**.

By default, users and roles have no permissions. An IAM administrator creates IAM policies and adds them to roles, which users can then assume. IAM policies define permissions regardless of the method used to perform the operation.

#### Identity-based policies
<a name="security_iam_access-manage-id-based-policies"></a>

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

Identity-based policies can be *inline policies* (embedded directly into a single identity) or *managed policies* (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.html) in the *IAM User Guide*.

#### Resource-based policies
<a name="security_iam_access-manage-resource-based-policies"></a>

Resource-based policies are JSON policy documents that you attach to a resource. Examples include IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy.

Resource-based policies are inline policies that are located in that service. You can't use AWS managed policies from IAM in a resource-based policy.

#### Other policy types
<a name="security_iam_access-manage-other-policies"></a>

AWS supports additional policy types that can set the maximum permissions granted by more common policy types:
+ **Permissions boundaries** – Set the maximum permissions that an identity-based policy can grant to an IAM entity. For more information, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.
+ **Service control policies (SCPs)** – Specify the maximum permissions for an organization or organizational unit in AWS Organizations. For more information, see [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*.
+ **Resource control policies (RCPs)** – Set the maximum available permissions for resources in your accounts. For more information, see [Resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) in the *AWS Organizations User Guide*.
+ **Session policies** – Advanced policies passed as a parameter when creating a temporary session for a role or federated user. For more information, see [Session policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session) in the *IAM User Guide*.

#### Multiple policy types
<a name="security_iam_access-manage-multiple-policies"></a>

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines whether to allow a request when multiple policy types are involved, see [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) in the *IAM User Guide*.

### How AWS Client VPN works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Client VPN, learn what IAM features are available to use with Client VPN.


**IAM features you can use with AWS Client VPN**  

| IAM feature | Client VPN support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes | 
| [Policy condition keys (service-specific)](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Yes | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) |  Yes | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  Yes | 

#### Identity-based policies for Client VPN
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

##### Identity-based policy examples for Client VPN
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>

To view examples of Client VPN identity-based policies, see [Identity-based policy examples for AWS Client VPN](#security_iam_id-based-policy-examples).

#### Resource-based policies within Client VPN
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

#### Policy actions for Client VPN
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Client VPN actions, see [Actions defined by AWS Client VPN](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in Client VPN use the following prefix before the action:

```
ec2
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "ec2:{{action1}}",
      "ec2:{{action2}}"
         ]
```

To view examples of Client VPN identity-based policies, see [Identity-based policy examples for AWS Client VPN](#security_iam_id-based-policy-examples).

#### Policy resources for Client VPN
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of Client VPN resource types and their ARNs, see [Resources defined by AWS Client VPN](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions defined by AWS Client VPN](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-actions-as-permissions).

To view examples of Client VPN identity-based policies, see [Identity-based policy examples for AWS Client VPN](#security_iam_id-based-policy-examples).

#### Policy condition keys for Client VPN
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of Client VPN condition keys, see [Condition keys for AWS Client VPN](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-policy-keys) in the *Service Authorization Reference*. To learn with which actions and resources you can use a condition key, see [Actions defined by AWS Client VPN](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-actions-as-permissions).

To view examples of Client VPN identity-based policies, see [Identity-based policy examples for AWS Client VPN](#security_iam_id-based-policy-examples).

#### ACLs in Client VPN
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

#### ABAC with Client VPN
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

#### Using temporary credentials with Client VPN
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

#### Cross-service principal permissions for Client VPN
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

 Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

#### Service roles for Client VPN
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** Yes

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

#### Service-linked roles for Client VPN
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

### Identity-based policy examples for AWS Client VPN
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify Client VPN resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by Client VPN, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Client VPN](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)

#### Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete Client VPN resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

#### Allow users to view their own permissions
<a name="security_iam_id-based-policy-examples-view-own-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

### Troubleshooting AWS Client VPN identity and access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with Client VPN and IAM.

**Topics**
+ [I am not authorized to perform an action in Client VPN](#security_iam_troubleshoot-no-permissions)
+ [I am not authorized to perform iam:PassRole](#security_iam_troubleshoot-passrole)
+ [I want to allow people outside of my AWS account to access my Client VPN resources](#security_iam_troubleshoot-cross-account-access)

#### I am not authorized to perform an action in Client VPN
<a name="security_iam_troubleshoot-no-permissions"></a>

If you receive an error that you're not authorized to perform an action, your policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user tries to use the console to view details about a fictional `{{my-example-widget}}` resource but doesn't have the fictional `ec2:{{GetWidget}}` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: ec2:{{GetWidget}} on resource: {{my-example-widget}}
```

In this case, the policy for the `mateojackson` user must be updated to allow access to the `{{my-example-widget}}` resource by using the `ec2:{{GetWidget}}` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

#### I am not authorized to perform iam:PassRole
<a name="security_iam_troubleshoot-passrole"></a>

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Client VPN.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in Client VPN. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

#### I want to allow people outside of my AWS account to access my Client VPN resources
<a name="security_iam_troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether Client VPN supports these features, see [How AWS Client VPN works with IAM](#security_iam_service-with-iam).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

### Using service-linked roles for AWS Client VPN
<a name="using-service-linked-roles"></a>

AWS Client VPN uses AWS Identity and Access Management (IAM) service-linked roles. A service-linked role is a unique type of IAM role that is linked directly to Client VPN. Service-linked roles are predefined by Client VPN and include all the permissions that the service requires to call other AWS services on your behalf. 

**Topics**
+ [Client VPN usage](#using-service-linked-roles-cvpn-slr)
+ [Connection authorization](#using-service-linked-roles-client-connect-handler)

#### Using roles for AWS Client VPN
<a name="using-service-linked-roles-cvpn-slr"></a>

AWS Client VPN uses AWS Identity and Access Management (IAM) service-linked roles. A service-linked role is a unique type of IAM role that is linked directly to Client VPN. Service-linked roles are predefined by Client VPN and include all the permissions that the service requires to call other AWS services on your behalf. 

A service-linked role makes setting up Client VPN easier because you don’t have to manually add the necessary permissions. Client VPN defines the permissions of its service-linked roles, and unless defined otherwise, only Client VPN can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your Client VPN resources because you can't inadvertently remove permission to access the resources.

##### Service-linked role permissions for Client VPN
<a name="service-linked-role-permissions-cvpn-slr"></a>

Client VPN uses the service-linked role named **AWSServiceRoleForClientVPN** – Allow Client VPN to create and manage resources related to your VPN connections.

The **AWSServiceRoleForClientVPN** service-linked role trusts the following service to assume the role:
+ `clientvpn.amazonaws.com`

This service-linked role uses the managed policy ClientVPNServiceRolePolicy. To view the permissions for this policy, see [ClientVPNServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ClientVPNServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

##### Create a service-linked role for Client VPN
<a name="create-service-linked-role-cvpn-slr"></a>

You don't need to manually create a service-linked role. When you create the first Client VPN endpoint in your account with the AWS Management Console, the AWS CLI, or the AWS API, Client VPN creates the service-linked role for you. 

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create the first Client VPN endpoint in your account, Client VPN creates the service-linked role for you again. 

##### Edit a service-linked role for Client VPN
<a name="edit-service-linked-role-cvpn-slr"></a>

Client VPN does not allow you to edit the AWSServiceRoleForClientVPN service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Edit a service-linked role description](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-service-linked-role.html#edit-service-linked-role-iam-console) in the *IAM User Guide*.

##### Delete a service-linked role for Client VPN
<a name="delete-service-linked-role-cvpn-slr"></a>

If you no longer need to use Client VPN, we recommend that you delete the **AWSServiceRoleForClientVPN** service-linked role.

You must first delete the related Client VPN resources. This ensures that you do not inadvertently remove permission to access the resources.

Use the IAM console, the IAM CLI, or the IAM API to delete the service-linked roles. For more information, see [Delete a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#id_roles_manage_delete_slr) in the *IAM User Guide*.

#### Using roles for connection authorization in Client VPN;
<a name="using-service-linked-roles-client-connect-handler"></a>

AWS Client VPN uses AWS Identity and Access Management (IAM) service-linked roles. A service-linked role is a unique type of IAM role that is linked directly to Client VPN. Service-linked roles are predefined by Client VPN and include all the permissions that the service requires to call other AWS services on your behalf. 

A service-linked role makes setting up Client VPN easier because you don’t have to manually add the necessary permissions. Client VPN defines the permissions of its service-linked roles, and unless defined otherwise, only Client VPN can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your Client VPN resources because you can't inadvertently remove permission to access the resources.

##### Service-linked role permissions for Client VPN
<a name="service-linked-role-permissions-client-connect-handler"></a>

Client VPN uses the service-linked role named **AWSServiceRoleForClientVPNConnections** – Service Linked Role for Client VPN connections.

The AWSServiceRoleForClientVPNConnections service-linked role trusts the following services to assume the role:
+ `clientvpn-connections.amazonaws.com`

The role permissions policy named ClientVPNServiceConnectionsRolePolicy allows Client VPN to complete the following actions on the specified resources:
+ Action: `lambda:InvokeFunction` on `arn:aws:lambda:*:*:function:AWSClientVPN-*`

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#service-linked-role-permissions) in the *IAM User Guide*.

##### Create a service-linked role for Client VPN
<a name="create-service-linked-role-client-connect-handler"></a>

You don't need to manually create a service-linked role. When you create the first Client VPN endpoint in your account with the AWS Management Console, the AWS CLI, or the AWS API, Client VPN creates the service-linked role for you. 

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create the first Client VPN endpoint in your account, Client VPN creates the service-linked role for you again. 

##### Edit a service-linked role for Client VPN
<a name="edit-service-linked-role-client-connect-handler"></a>

Client VPN does not allow you to edit the AWSServiceRoleForClientVPNConnections service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Edit a service-linked role description](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-service-linked-role.html#edit-service-linked-role-iam-console) in the *IAM User Guide*.

##### Delete a service-linked role for Client VPN
<a name="delete-service-linked-role-client-connect-handler"></a>

If you no longer need to use Client VPN, we recommend that you delete the **AWSServiceRoleForClientVPNConnections** service-linked role.

You must first delete the related Client VPN resources. This ensures that you do not inadvertently remove permission to access the resources.

Use the IAM console, the IAM CLI, or the IAM API to delete the service-linked roles. For more information, see [Delete a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#id_roles_manage_delete_slr) in the *IAM User Guide*.

## Resilience in AWS Client VPN
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In addition to the AWS global infrastructure, AWS Client VPN offers features to help support your data resiliency and backup needs.

### Multiple target networks for high availability
<a name="high-availability"></a>

You associate a target network with a Client VPN endpoint to enable clients to establish VPN sessions. Target networks are subnets in your VPC. Each subnet that you associate with the Client VPN endpoint must belong to a different Availability Zone. You can associate multiple subnets with a Client VPN endpoint for high availability. 

## Infrastructure security in AWS Client VPN
<a name="infrastructure-security"></a>

As a managed service, AWS Client VPN is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access Client VPN through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

## Security best practices for AWS Client VPN
<a name="security-best-practices"></a>

AWS Client VPN provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

**Authorization rules**  
Use authorization rules to restrict which users can access your network. For more information, see [Authorization rules](#cvpn-working-rules).

**Security groups**  
Use security groups to control which resources users can access in your VPC. For more information, see [Security groups](#security-groups).

**Client certificate revocation lists**  
Use client certificate revocation lists to revoke access to a Client VPN endpoint for specific client certificates. For example, when a user leaves your organization. For more information, see [Client certificate revocation lists](#cvpn-working-certificates).

**Disconnect on session timeout**  
Disconnect a session when the maximum Client VPN session time is reached, enforcing a maximum VPN session duration. For more information, see [Maximum VPN session duration](#cvpn-working-max-duration).

**Monitoring tools**  
Use monitoring tools to keep track of availability and performance of your Client VPN endpoints. For more information, see [Monitoring Client VPN](#monitoring-overview).

**Identity and access management**  
Manage access to Client VPN resources and APIs by using IAM policies for your IAM users and IAM roles. For more information, see [Identity and access management for AWS Client VPN](#security-iam).

**Use the AWS provided VPN client**  
Use the AWS provided client for AWS Client VPN, available from the [AWS Client VPN download page](https://aws.amazon.com/vpn/client-vpn-download/).

**Use the exported client configuration**  
Use the client configuration file exported from your AWS Client VPN endpoint. For more information, see [Export the client configuration file](#export-client-config-file). Do not modify the cipher or TLS settings in the configuration file. AWS Client VPN endpoints only support the following algorithms:
+ TLS 1.3: `TLS_AES_256_GCM_SHA384` and `TLS_AES_128_GCM_SHA256`
+ TLS 1.2: `TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384`, `TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256`, `TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384`, and `TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256`
+ Data channel: `AES-256-GCM`

## IPv6 considerations for AWS Client VPN
<a name="ipv6-considerations"></a>

Client VPN now supports native IPv6 connectivity alongside existing IPv4 capabilities. You can create IPv6-only, IPv4-only, or dual-stack (both IPv4 and IPv6) endpoints to meet your networking requirements.

### Key components of IPv6 support
<a name="ipv6-key-components"></a>

When working with IPv6 in Client VPN, there are two key configuration parameters:

Endpoint IP address type  
This parameter defines the endpoint management IP type, which determines the type of EC2 instance provisioned for the endpoint. This IP type is used for managing outer VPN tunnel traffic (the encrypted traffic that flows between the OpenVPN client and server over the public internet).

Traffic IP address type  
This parameter defines the type of traffic that flows through the VPN tunnel. This IP type is used for managing inner encrypted traffic (the actual payload), client CIDR ranges, subnet association, routes, and rules per endpoint.

### IPv6 client CIDR assignment
<a name="ipv6-client-cidr"></a>

For IPv6 client CIDR, you do not need to specify a CIDR block. Amazon automatically assigns CIDR ranges for IPv6 clients. This auto-assignment enables no-SNATing for IPv6 tunnel traffic, providing enhanced visibility into the connected user's IPv6 address.

### Compatibility requirements
<a name="ipv6-compatibility"></a>

IPv6 and dual-stack endpoints have dependencies on user devices and internet service providers (ISPs):
+ User devices running the CVPN client must support the required IP configuration as shown in the compatibility table below.
+ ISPs must support the required IP configuration for the connection to work properly.
+ For IPv6 or dual-stack traffic, the associated VPC subnets must have IPv6 or dual-stack CIDR ranges.

### DNS support
<a name="ipv6-dns"></a>

DNS is supported in all types of endpoints - IPv4, IPv6, and dual-stack. For IPv6 endpoints, you can configure IPv6 DNS servers using the `--dns-server-ipv6` parameter. AAAA DNS records are supported on both the service and client end.

### Limitations
<a name="ipv6-feature-limitations"></a>

The following are the limitations with IPv6:
+ Client-to-client (C2C) communication is not supported for IPv6 clients. If an IPv6 client tries to communicate with another IPv6 client, the traffic will be dropped.

### Client Routes Enforcement for IPv6
<a name="ipv6-cre"></a>

Client VPN now supports Client Routes Enforcement for IPv6 traffic. This feature helps ensure that IPv6 network traffic from connected clients follows the routes defined by the administrator and is not inadvertently sent outside the VPN tunnel.

Key aspects of IPv6 Client Route Enforcement support:
+ The existing `ClientRouteEnforcementOptions.enforced` flag enables CRE for both IPv4 and IPv6 stacks.
+ IPv6 Client Route Enforcement excludes certain IPv6 ranges to maintain critical IPv6 functionalities:
  + `::1/128` — Reserved for loopback
  + `fe80::/10` — Reserved for link-local addresses
  + `ff00::/8` — Reserved for multicast
+ IPv6 Client Route Enforcement is available in AWS VPN Client version 5.3.0 and higher on Windows, macOS, and Ubuntu.

For more detailed information about CRE, including how to enable and configure it, see [AWS Client VPN Client Route Enforcement](#cvpn-working-cre).

### IPv6 leak prevention (legacy information)
<a name="ipv6-leak-prevention"></a>

For older configurations that don't use the native IPv6 support, you may still need to prevent IPv6 leak. IPv6 leak can happen when both IPv4 and IPv6 are enabled and connected to the VPN, but the VPN doesn't route IPv6 traffic into its tunnel. In this case, when connecting to an IPv6 enabled destination, you are actually still connecting with your IPv6 address provided by your ISP. This will leak your real IPv6 address. The instructions below explain how to route IPv6 traffic into the VPN tunnel.

The following IPv6-related directives should be added to your Client VPN configuration file to prevent IPv6 leak:

```
ifconfig-ipv6 arg0 arg1
route-ipv6 arg0
```

An example might be:

```
ifconfig-ipv6 fd15:53b6:dead::2 fd15:53b6:dead::1
route-ipv6 2000::/4
```

In this example, `ifconfig-ipv6 fd15:53b6:dead::2 fd15:53b6:dead::1` will set the local tunnel device IPv6 address to be `fd15:53b6:dead::2` and the remote VPN endpoint IPv6 address to be `fd15:53b6:dead::1`. 

The next command, `route-ipv6 2000::/4` will route IPv6 addresses from `2000:0000:0000:0000:0000:0000:0000:0000` to `2fff:ffff:ffff:ffff:ffff:ffff:ffff:ffff` into the VPN connection.

**Note**  
For "TAP" device routing in Windows for example, the second parameter of `ifconfig-ipv6` will be used as route target for `--route-ipv6`.

Organizations should configure the two parameters of `ifconfig-ipv6` themselves, and can use addresses in `100::/64` (from `0100:0000:0000:0000:0000:0000:0000:0000` to `0100:0000:0000:0000:ffff:ffff:ffff:ffff`) or `fc00::/7` (from `fc00:0000:0000:0000:0000:0000:0000:0000` to `fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff`). `100::/64` is Discard-Only Address Block, and `fc00::/7` is Unique-Local.

Another example:

```
ifconfig-ipv6 fd15:53b6:dead::2 fd15:53b6:dead::1
route-ipv6 2000::/3
route-ipv6 fc00::/7
```

In this example, the configuration will route all currently allocated IPv6 traffic into the VPN connection.

**Verification**  
Your organization will likely have its own tests. A basic verification is to set up a full tunnel VPN connection, then run ping6 to an IPv6 server using the IPv6 address. The IPv6 address of the server should be in the range specified by the `route-ipv6` command. This ping test should fail. However, this may change if IPv6 support is added to the Client VPN service in the future. If the ping is successful and you are able to access public sites when connected in full tunnel mode, you may need to do further troubleshooting. There are also some publicly available tools.

# Monitoring AWS Client VPN
<a name="monitoring-overview"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Client VPN and your other AWS solutions. You can use the following features to monitor your Client VPN endpoints, analyze traffic patterns, and troubleshoot issues with your Client VPN endpoints.

Monitoring authorization policy. When authorization policy is enabled on an endpoint, Client VPN records the authorization decision for every evaluated connection in your connection logs, and optionally the full evaluation context. Amazon CloudWatch metrics in the AWS/ClientVPN namespace count authorization policy denials, evaluations, and session terminations. For details, see [Connection logging for an AWS Client VPN endpoint](#connection-logging) and [Amazon CloudWatch metrics for AWS Client VPN](#monitoring-cloudwatch).

**Amazon CloudWatch**  
Monitors your AWS resources and the applications you run on AWS in real time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track CPU usage or other metrics of your Amazon EC2 instances and automatically launch new instances when needed. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**AWS CloudTrail**  
Captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. All Client VPN actions are logged by CloudTrail and are documented in the [Amazon EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-cvpn.html).

**Amazon CloudWatch Logs**  
Enables you to monitor connection attempts made to your AWS Client VPN endpoint. You can view the connection attempts and connection resets for the Client VPN connections. For the connection attempts, you can see both the successful and failed connection attempts. You can specify the CloudWatch Logs log stream to log the connection details. For more information, see [Connection logging for an AWS Client VPN endpoint](#connection-logging) and the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/).

**Topics**
+ [CloudWatch metrics](#monitoring-cloudwatch)

## Amazon CloudWatch metrics for AWS Client VPN
<a name="monitoring-cloudwatch"></a>

AWS Client VPN publishes the following metrics to Amazon CloudWatch for your Client VPN endpoints. Metrics are published to Amazon CloudWatch every five minutes.


| Metric | Description | 
| --- | --- | 
| ActiveConnectionsCount | The number of active connections to the Client VPN endpoint.<br />Units: Count | 
| AuthenticationFailures | The number of authentication failures for the Client VPN endpoint.<br />Units: Count | 
| CrlDaysToExpiry | The number of days until the Certificate Revocation List (CRL) which is configured on the Client VPN endpoint expires.<br />Units: Days | 
| EgressBytes | The number of bytes sent from the Client VPN endpoint.<br />Units: Bytes | 
| EgressPackets | The number of packets sent from the Client VPN endpoint.<br />Units: Count | 
| IdpCertDaysToExpiry | The number of days until the identity provider (IdP) certificate which is configured on the Client VPN endpoint expires. This metric is only reported for endpoints configured with SAML-based federated authentication.<br />Units: Days | 
| IngressBytes | The number of bytes received by the Client VPN endpoint.<br />Units: Bytes | 
| IngressPackets | The number of packets received by the Client VPN endpoint.<br />Units: Count | 
| SelfServicePortalClientConfigurationDownloads | The number of downloads of the Client VPN endpoint configuration file from the self-service portal.<br />Unit: Count | 

AWS Client VPN publishes the following authorization metrics for your Client VPN endpoints. These cover two separate authorization mechanisms. The [custom connection authorization](#connection-authorization-posture-assessment) metrics (prefixed `ClientConnectHandler`) apply to the Lambda-based client connect handler. The authorization policy metrics (prefixed `AuthorizationPolicy`) apply to Cedar-based authorization policies. The two sets of metrics are reported independently.


| Metric | Description | 
| --- | --- | 
| ClientConnectHandlerTimeouts | The number of timeouts on invoking the client connect handler for connections to the Client VPN endpoint.Units: Count | 
| ClientConnectHandlerInvalidResponses | The number of invalid responses returned by the client connect handler for connections to the Client VPN endpoint.<br />Units: Count | 
| ClientConnectHandlerOtherExecutionErrors | The number of unexpected errors while running the client connect handler for connections to the Client VPN endpoint.<br />Units: Count | 
| ClientConnectHandlerThrottlingErrors | The number of throttling errors on invoking the client connect handler for connections to the Client VPN endpoint.<br />Units: Count | 
| ClientConnectHandlerDeniedConnections | The number of connections denied by the client connect handler for connections to the Client VPN endpoint.<br />Units: Count | 
| ClientConnectHandlerFailedServiceErrors | The number of service side errors while running the client connect handler for connections to the Client VPN endpoint.<br />Units: Count | 
| AuthorizationPolicyDeniedConnections | The number of connections denied by the authorization policy for the Client VPN endpoint.<br />Units: Count | 
| AuthorizationPolicyEvaluationCount | The number of authorization policy evaluations performed for the Client VPN endpoint.<br />Units: Count | 
| AuthorizationPolicyTerminatedConnections | The number of sessions terminated by a periodic re-evaluation of the authorization policy for the Client VPN endpoint.<br />Units: Count | 

You can filter the metrics for your Client VPN endpoint by endpoint.

CloudWatch enables you to retrieve statistics about those data points as an ordered set of time series data, known as metrics. Think of a metric as a variable to monitor, and the data points as the values of that variable over time. Each data point has an associated timestamp and an optional unit of measurement.

You can use metrics to verify that your system is performing as expected. For example, you can create a CloudWatch alarm to monitor a specified metric and initiate an action (such as sending a notification to an email address) if the metric goes outside what you consider an acceptable range.

For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Topics**
+ [View CloudWatch metrics](#viewing-metrics)

### View Client VPN endpoint metrics in Amazon CloudWatch
<a name="viewing-metrics"></a>

You can view the metrics for your Client VPN endpoint as follows.

**To view metrics using the CloudWatch console**

Metrics are grouped first by the service namespace, and then by the various dimension combinations within each namespace.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Under **All metrics**, choose the **ClientVPN** metric namespace.

1. To view the metrics, select the metric dimension **by endpoint**.

**To view metrics using the AWS CLI**  
At a command prompt, use the following command to list the metrics that are available for the Client VPN 

```
aws cloudwatch list-metrics --namespace "AWS/ClientVPN"
```

# AWS Client VPN quotas
<a name="limits"></a>

Your AWS account has the following quotas, formerly referred to as limits, related to Client VPN endpoints. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

To request a quota increase for an adjustable quota, choose **Yes** in the **Adjustable** column. For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

## Client VPN quotas
<a name="quotas-endpoints"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Authorization rules per Client VPN endpoint | 200 For dual-stack endpoints, this limit is shared between IPv4 and IPv6 routes. | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-9A1BC94B) | 
| Client VPN endpoints per Region | 5 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8EA77D34) | 
| Concurrent client connections per Client VPN endpoint | This value depends on the number of subnet associations per endpoint.+  1 – 7,000 <br />+  2 – 36,500 <br />+  3 – 66,500 <br />+  4 – 96,500 <br />+  5 – 126,000 <br />For dual-stack endpoints, this limit is shared between IPv4 and IPv6 connections. | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C4B238BF) | 
| Concurrent operations per Client VPN endpoint † | 10 | No | 
| Entries in a client certificate revocation list for Client VPN endpoints | 20,000 | No | 
| Routes per Client VPN target network association | 100 For dual-stack endpoints, this limit is shared between IPv4 and IPv6 routes. | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-401D78F7) | 
| Authorization policy document size per Client VPN endpoint | 10,000 bytes | No | 

† Operations include:
+ Associate or disassociate subnets
+ Create or delete security groups

## Users and groups quotas
<a name="quotas-users-groups"></a>

When you configure users and groups for Active Directory or a SAML-based IdP, the following quotas apply:
+ Users can belong to a maximum of 200 groups. We ignore any groups after the 200th group.
+ The maximum length for the group ID is 255 characters.
+ The maximum length for the name ID is 255 characters. We truncate characters after the 255th character.

## General considerations
<a name="quotas-general"></a>

Take the following into consideration when you use Client VPN endpoints:
+ If you use Active Directory to authenticate the user, the Client VPN endpoint must belong to the same account as the AWS Directory Service resource used for Active Directory authentication.
+ If you use SAML-based federated authentication to authenticate a user, the Client VPN endpoint must belong to the same account as the IAM SAML identity provider that you create to define the IdP to AWS trust relationship. The IAM SAML identity provider can be shared across multiple Client VPN endpoints in the same AWS account.

## Device posture considerations
<a name="quotas-device-posture"></a>

Take the following into consideration when you enable device posture on a Client VPN endpoint:
+ The authorization policy document cannot exceed 10,000 bytes.
+ Client VPN evaluates the authorization policy when a device connects and again every 5 minutes for the life of the session.
+ Device posture requires one or more supported device trust providers (CrowdStrike, Jamf, or JumpCloud). For more information, see [Device posture for AWS Client VPN](#device-posture).

# Troubleshooting AWS Client VPN
<a name="troubleshooting"></a>

The following sections can help you troubleshoot problems that you might have with a Client VPN endpoint.

For more information about troubleshooting OpenVPN-based software that clients use to connect to a Client VPN, see [Troubleshooting Your Client VPN Connection](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/troubleshooting.html) in the *AWS Client VPN User Guide*.

**Topics**
+ [Unable to resolve the Client VPN endpoint DNS name](#resolve-host-name)
+ [Traffic is not being split between subnets](#split-traffic)
+ [Authorization rules for Active Directory groups not working as expected](#ad-group-auth-rules)
+ [Clients can't access a peered VPC, Amazon S3, or the internet](#no-internet-access)
+ [Access to a peered VPC, Amazon S3, or the internet is intermittent](#intermittent-access)
+ [Client software returns TLS error](#client-cannot-connect)
+ [Client software returns user name and password errors — Active Directory authentication](#client-user-name-password-mfa)
+ [Client software returns user name and password errors — federated authentication](#missing-attribute)
+ [Clients cannot connect — mutual authentication](#client-cannot-connect-mutual)
+ [Client returns a credentials exceed max size error — federated authentication](#client-credentials-exceeded)
+ [Client does not open browser — federated authentication](#client-no-browser)
+ [Client returns no available ports error — federated authentication](#client-no-port)
+ [VPN connection terminated due to IP mismatch](#server-ip-mismatch)
+ [Routing traffic to LAN not working as expected](#routing-to-lan)
+ [Verify the bandwidth limit for an endpoint](#test-throughput)
+ [Client VPN tunnel connectivity](#VPNTunnelConnectivityTroubleshooting)

## Troubleshooting AWS Client VPN: Unable to resolve the Client VPN endpoint DNS name
<a name="resolve-host-name"></a>

**Problem**  
I am unable to resolve the Client VPN endpoint's DNS name.

**Cause**  
The Client VPN endpoint configuration file includes a parameter called `remote-random-hostname`. This parameter forces the client to prepend a random string to the DNS name to prevent DNS caching. Some clients do not recognize this parameter and therefore, they do not prepend the required random string to the DNS name.

**Solution**  
Open the Client VPN endpoint configuration file using your preferred text editor. Locate the line that specifies the Client VPN endpoint DNS name, and prepend a random string to it so that the format is {{random\_string.displayed\_DNS\_name}}. For example:
+ Original DNS name: `cvpn-endpoint-0102bc4c2eEXAMPLE.clientvpn.us-west-2.amazonaws.com`
+ Modified DNS name: `asdfa.cvpn-endpoint-0102bc4c2eEXAMPLE.clientvpn.us-west-2.amazonaws.com`

## Troubleshooting AWS Client VPN: Traffic is not being split between subnets
<a name="split-traffic"></a>

**Problem**  
I am trying to split network traffic between two subnets. Private traffic should be routed through a private subnet, while internet traffic should be routed through a public subnet. However, only one route is being used even though I have added both routes to the Client VPN endpoint route table.

**Cause**  
You can associate multiple subnets with a Client VPN endpoint, but you can associate only one subnet per Availability Zone. The purpose of multiple subnet association is to provide high availability and Availability Zone redundancy for clients. However, Client VPN does not enable you to selectively split traffic between the subnets that are associated with the Client VPN endpoint.

Clients connect to a Client VPN endpoint based on the DNS round-robin algorithm. This means that their traffic can be routed through any of the associated subnets when they establish a connection. Therefore, they might experience connectivity issues if they land on an associated subnet that does not have the required route entries.

For example, say that you configure the following subnet associations and routes:
+ Subnet associations
  + Association 1: Subnet-A (us-east-1a)
  + Association 2: Subnet-B (us-east-1b)
+ Routes
  + Route 1: 10.0.0.0/16 routed to Subnet-A
  + Route 2: 172.31.0.0/16 routed to Subnet-B

In this example, clients that land on Subnet-A when they connect cannot access Route 2, while clients that land on Subnet-B when they connect cannot access Route 1.

**Solution**  
Verify that the Client VPN endpoint has the same route entries with targets for each associated network. This ensures that clients have access to all routes regardless of the subnet through which their traffic is routed.

## Troubleshooting AWS Client VPN: Authorization rules for Active Directory groups not working as expected
<a name="ad-group-auth-rules"></a>

**Problem**  
I have configured authorization rules for my Active Directory groups, but they are not working as I expected. I have added an authorization rule for `0.0.0.0/0` to authorize traffic for all networks, but traffic still fails for specific destination CIDRs.

**Cause**  
Authorization rules are indexed on network CIDRs. Authorization rules must grant Active Directory groups access to specific network CIDRs. Authorization rules for `0.0.0.0/0` are handled as a special case, and are therefore evaluated last, regardless of the order in which the authorization rules are created.

For example, say that you create five authorization rules in the following order:
+ Rule 1: Group 1 access to `10.1.0.0/16`
+ Rule 2: Group 1 access to `0.0.0.0/0`
+ Rule 3: Group 2 access to `0.0.0.0/0`
+ Rule 4: Group 3 access to `0.0.0.0/0`
+ Rule 5: Group 2 access to `172.131.0.0/16`

In this example, Rule 2, Rule 3, and Rule 4 are evaluated last. Group 1 has access to `10.1.0.0/16` only, and Group 2 has access to `172.131.0.0/16` only. Group 3 does not have access to `10.1.0.0/16` or `172.131.0.0/16`, but it has access to all other networks. If you remove Rules 1 and 5, all three groups have access to all networks.

Client VPN uses longest prefix matching when evaluating authorization rules. See [Route priority](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#route-tables-priority) in the *Amazon VPC User Guide* for more details.

**Solution**  
Verify that you create authorization rules that explicitly grant Active Directory groups access to specific network CIDRs. If you add an authorization rule for `0.0.0.0/0`, keep in mind that it will be evaluated last, and that previous authorization rules may limit the networks to which it grants access.

## Troubleshooting AWS Client VPN: Clients can't access a peered VPC, Amazon S3, or the internet
<a name="no-internet-access"></a>

**Problem**  
I have properly configured my Client VPN endpoint routes, but my clients can't access a peered VPC, Amazon S3, or the internet. 

**Solution**  
The following flow chart contains the steps to diagnose internet, peered VPC, and Amazon S3 connectivity issues.

![Client VPN troubleshooting steps](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/cvpn-flow.png)


1. For access to the internet, add an authorization rule for `0.0.0.0/0`.

   For access to a peered VPC, add an authorization rule for the IPv4 CIDR range of the VPC.

   For access to S3, specify the IP address of the Amazon S3 endpoint.

1. Check whether you are able to resolve the DNS name.

   If you are unable to resolve the DNS name, verify that you have specified the DNS servers for the Client VPN endpoint. If you manage your own DNS server, specify its IP address. Verify that the DNS server is accessible from the VPC. 

   If you're unsure about which IP address to specify for the DNS servers, specify the VPC DNS resolver at the .2 IP address in your VPC.

1. For internet access, check if you are able to ping a public IP address or a public website, for example, `amazon.com`. If you do not get a response, make sure that the route table for the associated subnets has a default route that targets either an internet gateway or a NAT gateway. If the route is in place, verify that the associated subnet does not have network access control list rules that block inbound and outbound traffic.

   If you are unable to reach a peered VPC, verify that the associated subnet's route table has a route entry for the peered VPC.

   If you are unable to reach Amazon S3, verify that the associated subnet's route table has a route entry for the gateway VPC endpoint.

1. Check whether you can ping a public IP address with a payload larger than 1400 bytes. Use one of the following commands:
   + Windows

     ```
     C:\> ping  8.8.8.8 -l 1480 -f
     ```
   + Linux

     ```
     $ ping -s 1480 8.8.8.8 -M do
     ```

   If you cannot ping an IP address with a payload larger than 1400 bytes, open the Client VPN endpoint `.ovpn` configuration file using your preferred text editor, and add the following.

   ```
   mssfix 1328
   ```

## Troubleshooting AWS Client VPN: Access to a peered VPC, Amazon S3, or the internet is intermittent
<a name="intermittent-access"></a>

**Problem**  
I have intermittent connectivity issues when connecting to a peered VPC, Amazon S3, or the internet, but access to associated subnets is unaffected. I need to disconnect and reconnect in order to resolve the connectivity issues.

**Cause**  
Clients connect to a Client VPN endpoint based on the DNS round-robin algorithm. This means that their traffic can be routed through any of the associated subnets when they establish a connection. Therefore, they might experience connectivity issues if they land on an associated subnet that does not have the required route entries.

**Solution**  
Verify that the Client VPN endpoint has the same route entries with targets for each associated network. This ensures that clients have access to all routes regardless of the associated subnet through which their traffic is routed.

For example, say that your Client VPN endpoint has three associated subnets (Subnet A, B, and C), and you want to enable internet access for your clients. To do this, you must add three `0.0.0.0/0` routes - one that targets each associated subnet:
+ Route 1: `0.0.0.0/0` for Subnet A
+ Route 2: `0.0.0.0/0` for Subnet B
+ Route 3: `0.0.0.0/0` for Subnet C

## Troubleshooting AWS Client VPN: Client software returns a TLS error when trying to connect to Client VPN
<a name="client-cannot-connect"></a>

**Problem**  
I used to be able to connect my clients to the Client VPN successfully, but now the OpenVPN-based client returns one of the following errors when it tries to connect: 

```
TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity) 
TLS Error: TLS handshake failed
```

```
Connection failed because of a TLS handshake error. Contact your IT administrator.
```

**Possible cause \#1**  
If you use mutual authentication and you imported a client certificate revocation list, the client certificate revocation list might have expired. During the authentication phase, the Client VPN endpoint checks the client certificate against the client certificate revocation list that you imported. If the client certificate revocation list has expired, you cannot connect to the Client VPN endpoint.

**Solution \#1**  
Check the expiry date of your client certificate revocation list by using the OpenSSL tool. 

```
$ openssl crl -in {{path_to_crl_pem_file}} -noout -nextupdate
```

The output displays the expiry date and time. If the client certificate revocation list has expired, you must create a new one and import it to the Client VPN endpoint. For more information, see [AWS Client VPN client certificate revocation lists](#cvpn-working-certificates).

**Possible cause \#2**  
The server certificate being used for the Client VPN endpoint has expired.

**Solution \#2**  
Check the status of your server certificate in the AWS Certificate Manager console or by using the AWS CLI. If the server certificate is expired, create a new certificate and upload to ACM. For detailed steps to generate the server and client certificates and keys using the [OpenVPN easy-rsa utility](https://github.com/OpenVPN/easy-rsa), and import them into ACM see [Mutual authentication in AWS Client VPN](#mutual).

Alternatively, there might be an issue with the OpenVPN-based software that the client is using to connect to the Client VPN. For more information about troubleshooting OpenVPN-based software, see [Troubleshooting Your Client VPN Connection](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/troubleshooting.html) in the *AWS Client VPN User Guide*.

## Troubleshooting AWS Client VPN: Client software returns user name and password errors — Active Directory authentication
<a name="client-user-name-password-mfa"></a>

**Problem**  
I use Active Directory authentication for my Client VPN endpoint and I used to be able to connect my clients to the Client VPN successfully. But now, clients are getting invalid user name and password errors.

**Possible causes**  
If you use Active Directory authentication and if you enabled multi-factor authentication (MFA) after you distributed the client configuration file, the file does not contain the necessary information to prompt users to enter their MFA code. Users are prompted to enter their user name and password only, and authentication fails.

**Solution**  
Download a new client configuration file and distribute it to your clients. Verify that the new file contains the following line.

```
static-challenge "Enter MFA code " 1
```

For more information, see [AWS Client VPN endpoint configuration file export](#cvpn-working-endpoint-export). Test the MFA configuration for your Active Directory without using the Client VPN endpoint to verify that MFA is working as expected.

## Troubleshooting AWS Client VPN: Client software returns user name and password errors — federated authentication
<a name="missing-attribute"></a>

**Problem**  
Trying to log in with a user name and password with federated authentication and getting the error "The credentials received were incorrect. Contact your IT administrator."

**Cause**  
This error can be caused by not having at least one attribute included in the SAML response from the IdP.

**Solution**  
Make sure at least one attribute is included in the SAML response from the IdP. See [SAML-based IdP configuration resources](#saml-config-resources) for more information.

## Troubleshooting AWS Client VPN: Clients cannot connect — mutual authentication
<a name="client-cannot-connect-mutual"></a>

**Problem**  
I use mutual authentication for my Client VPN endpoint. Clients are getting TLS key negotiation failed errors and timeout errors.

**Possible causes**  
The configuration file that was provided to the clients does not contain the client certificate and the client private key, or the certificate and key are incorrect.

**Solution**  
Ensure that the configuration file contains the correct client certificate and key. If necessary, fix the configuration file and redistribute it to your clients. For more information, see [AWS Client VPN endpoint configuration file export](#cvpn-working-endpoint-export).

## Troubleshooting AWS Client VPN: Client returns a credentials exceed max size error in Client VPN — federated authentication
<a name="client-credentials-exceeded"></a>

**Problem**  
I use federated authentication for my Client VPN endpoint. When clients enter their user name and password in the SAML-based identity provider (IdP) browser window, they get an error that the credentials exceed the maximum supported size.

**Cause**  
The SAML response returned by the IdP exceeds the maximum supported size. For more information, see [Requirements and considerations for SAML-based federated authentication](#saml-requirements).

**Solution**  
Try to reduce the number of groups that the user belongs to in the IdP, and try connecting again.

## Troubleshooting AWS Client VPN: Client does not open browser for an endpoint — federated authentication
<a name="client-no-browser"></a>

**Problem**  
I use federated authentication for my Client VPN endpoint. When clients try to connect to the endpoint, the client software does not open a browser window, and instead displays a user name and password popup window.

**Cause**  
The configuration file that was provided to the clients does not contain the `auth-federate` flag.

**Solution**  
[Export the latest configuration file](#cvpn-working-endpoint-export), import it to the AWS provided client, and try connecting again.

## Troubleshooting AWS Client VPN: Client returns no available ports error — federated authentication
<a name="client-no-port"></a>

**Problem**  
I use federated authentication for my Client VPN endpoint. When clients try to connect to the endpoint, the client software returns the following error:

```
The authentication flow could not be initiated. There are no available ports. 
```

**Cause**  
The AWS provided client requires the use of TCP port 35001 to complete authentication. For more information, see [Requirements and considerations for SAML-based federated authentication](#saml-requirements).

**Solution**  
Verify that the client's device is not blocking TCP port 35001 or is using it for a different process.

## Troubleshooting AWS Client VPN: A connection is terminated due to an IP mismatch
<a name="server-ip-mismatch"></a>

**Problem**  
VPN connection terminated and the client software returns the following error: `"The VPN connection is being terminated due to a discrepancy between the IP address of the connected server and the expected VPN server IP. Please contact your network administrator for assistance in resolving this issue."`

**Cause**  
The AWS provided client requires that the IP address that it is connected to matches the IP of the VPN server backing the Client VPN endpoint. For more information, see [Rules and best practices for using AWS Client VPN](#what-is-best-practices).

**Solution**  
Verify that there is no DNS proxy between the AWS provided client and the Client VPN endpoint.

## Troubleshooting AWS Client VPN: Routing traffic to LAN not working as expected
<a name="routing-to-lan"></a>

**Problem**  
Trying to route traffic to local area network (LAN) not working as expected when the LAN IP address ranges are not within the following standard private IP address ranges: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, or `169.254.0.0/16`.

**Cause**  
If the client LAN address range is detected to fall outside of the above standard ranges, the Client VPN endpoint will automatically push the OpenVPN directive "redirect-gateway block-local" to the client, forcing all LAN traffic into the VPN. For more information, see [Rules and best practices for using AWS Client VPN](#what-is-best-practices).

**Solution**  
If you require LAN access during VPN connections, it is advised that you use the conventional address ranges listed above for your LAN.

## Troubleshooting AWS Client VPN: Verify the bandwidth limit for a Client VPN endpoint
<a name="test-throughput"></a>

**Problem**  
I need to verify the bandwidth limit for a Client VPN endpoint. 

**Cause**  
The throughput depends on multiple factors, such as the capacity of your connection from your location, and the network latency between your Client VPN desktop application on your computer and the VPC endpoint. A minimum bandwidth of 10 Mbps is supported per user connection.

**Solution**  
Run the following commands to verify the bandwidth. 

```
sudo iperf3 -s -V
```

On the client:

```
sudo iperf -c {{server IP address}} -p {{port}} -w 512k -P 60
```

## Troubleshooting AWS Client VPN: Tunnel connectivity issues to a VPC
<a name="VPNTunnelConnectivityTroubleshooting"></a>

When experiencing connectivity issues with your AWS Client VPN connection, follow this systematic troubleshooting approach to identify and resolve the problem. This section provides step-by-step procedures to diagnose common Client VPN connectivity issues between remote clients and Amazon VPC resources. 

**Topics**
+ [Network connectivity prerequisites](#NetworkConnectivityPrerequisites)
+ [Check Client VPN endpoint status](#CheckClientVPNEndpointStatus)
+ [Verify client connections](#VerifyClientConnections)
+ [Verify client authentication](#ClientAuthentication)
+ [Check authorization rules](#AuthorizationRules)
+ [Validate Client VPN routes](#ValidateClientVPNRoutes)
+ [Verify security groups and network ACLs](#SecurityGroupNACLVerification)
+ [Test client connectivity](#TestClientConnectivity)
+ [Diagnose the client device](#ClientSideDiagnostics)
+ [Troubleshoot DNS resolution](#DNSTroubleshooting)
+ [Troubleshoot performance](#PerformanceTroubleshooting)
+ [Monitor Client VPN metrics](#MonitorClientVPNMetrics)
+ [Check Client VPN logs](#CheckClientVPNLogs)
+ [Common issues and solutions](#CommonIssues)

### Network connectivity prerequisites
<a name="NetworkConnectivityPrerequisites"></a>

Before troubleshooting Client VPN connectivity, verify these network prerequisites:
+ Ensure the Client VPN endpoint subnet has internet connectivity (via Internet Gateway or NAT Gateway).
+ Verify that the Client VPN endpoint is associated with subnets in different Availability Zones for high availability.
+ Check that the VPC has sufficient IP address space and doesn't conflict with client CIDR blocks.
+ Confirm that target subnets have proper route table associations.

### Check Client VPN endpoint status
<a name="CheckClientVPNEndpointStatus"></a>

First, verify that your Client VPN endpoint is in the correct state:

1. Use the AWS CLI to check the Client VPN endpoint status:

   ```
   aws ec2 describe-client-vpn-endpoints --region {{your-region}}
   ```

1. Look for the endpoint state in the output. The state should be `available`.

1. Verify that the endpoint has associated target networks (subnets).

1. If the state is not `available`, check for any error messages or pending states that might indicate configuration issues.

### Verify client connections
<a name="VerifyClientConnections"></a>

Check the status of client connections to your Client VPN endpoint:

1. Check active client connections:

   ```
   aws ec2 describe-client-vpn-connections --client-vpn-endpoint-id {{cvpn-endpoint-id}} --region {{your-region}}
   ```

1. Review connection status and any error messages in the output.

1. Check client authentication logs for failed authentication attempts.

1. Verify that clients are receiving IP addresses from the configured client CIDR block.

**Note**  
If clients cannot connect, the issue is likely with authentication configuration, authorization rules, or network connectivity.

### Verify client authentication
<a name="ClientAuthentication"></a>

Authentication issues are common causes of Client VPN connectivity problems:
+ For mutual authentication, ensure client certificates are valid and not expired.
+ For Active Directory authentication, verify user credentials and domain connectivity.
+ For SAML-based federated authentication, check IdP configuration and user permissions.
+ Review authentication logs in CloudWatch for detailed error information.
+ Verify that the authentication method configured on the endpoint matches the client configuration.

### Check authorization rules
<a name="AuthorizationRules"></a>

Authorization rules control which network resources clients can access:

1. List current authorization rules:

   ```
   aws ec2 describe-client-vpn-authorization-rules --client-vpn-endpoint-id {{cvpn-endpoint-id}} --region {{your-region}}
   ```

1. Verify that rules exist for the target networks clients need to access.

1. Check that the rules specify the correct Active Directory groups (if using AD authentication).

1. Ensure that authorization rules are in `active` state.

### Validate Client VPN routes
<a name="ValidateClientVPNRoutes"></a>

Proper routing configuration is essential for Client VPN connectivity:

1. Check Client VPN endpoint routes:

   ```
   aws ec2 describe-client-vpn-routes --client-vpn-endpoint-id {{cvpn-endpoint-id}} --region {{your-region}}
   ```

1. Verify routes exist for target networks that clients need to access.

1. Check Amazon VPC route tables to ensure return traffic can reach the Client VPN endpoint:

   ```
   aws ec2 describe-route-tables --filters "Name=vpc-id,Values={{vpc-id}}" --region {{your-region}}
   ```

1. Verify that target network associations are configured correctly.

### Verify security groups and network ACLs
<a name="SecurityGroupNACLVerification"></a>

Security groups and network ACLs can block Client VPN traffic:

1. Check security groups for target EC2 instances:

   ```
   aws ec2 describe-security-groups --group-ids {{sg-xxxxxxxxx}} --region {{your-region}}
   ```

1. Verify inbound rules allow traffic from Client VPN CIDR block:
   + SSH (port 22) from Client VPN CIDR: `10.0.0.0/16`
   + HTTP (port 80) from Client VPN CIDR: `10.0.0.0/16`
   + HTTPS (port 443) from Client VPN CIDR: `10.0.0.0/16`
   + Custom application ports as needed

1. For Client VPN endpoint security group (if applicable), ensure it allows:
   + UDP port 443 (OpenVPN) from 0.0.0.0/0
   + All traffic outbound to VPC CIDR blocks

1. Check that network ACLs are not blocking the traffic. Network ACLs are stateless, so both inbound and outbound rules must be configured.

1. Verify both inbound and outbound rules for the specific traffic you're trying to send.

### Test client connectivity
<a name="TestClientConnectivity"></a>

Test connectivity from Client VPN clients to Amazon VPC resources:

1. From a connected Client VPN client, test connectivity to Amazon VPC resources:

   ```
   ping {{vpc-resource-ip}}
   traceroute {{vpc-resource-ip}}
   ```

1. Test specific application connectivity:

   ```
   telnet {{vpc-resource-ip}} {{port}}
   ```

1. Verify DNS resolution if using private DNS names:

   ```
   nslookup {{private-dns-name}}
   ```

1. Test connectivity to internet resources if split tunneling is enabled.

### Diagnose the client device
<a name="ClientSideDiagnostics"></a>

Perform these checks on the client device:

1. Verify client configuration file (.ovpn) contains correct settings:
   + Correct server endpoint URL
   + Valid client certificate and private key
   + Proper authentication method configuration

1. Check client logs for connection errors:
   + Windows: Event Viewer → Applications and Services Logs → OpenVPN
   + macOS: Console app, search for "Tunnelblick" or "OpenVPN"
   + Linux: `/var/log/openvpn/` or systemd journal

1. Test basic network connectivity from client:

   ```
   ping 8.8.8.8
   nslookup {{cvpn-endpoint-id}}.cvpn.{{region}}.amazonaws.com
   ```

### Troubleshoot DNS resolution
<a name="DNSTroubleshooting"></a>

DNS issues can prevent access to resources using private DNS names:

1. Check if DNS servers are configured in the Client VPN endpoint:

   ```
   aws ec2 describe-client-vpn-endpoints --client-vpn-endpoint-ids {{cvpn-endpoint-id}} --query 'ClientVpnEndpoints[0].DnsServers'
   ```

1. Test DNS resolution from client:

   ```
   nslookup {{private-resource.internal}}
   dig {{private-resource.internal}}
   ```

1. Verify Route 53 Resolver rules if using custom DNS resolution.

1. Check that security groups allow DNS traffic (UDP/TCP port 53) from Client VPN CIDR to DNS servers.

### Troubleshoot performance
<a name="PerformanceTroubleshooting"></a>

Address performance issues with Client VPN connections:
+ Monitor bandwidth utilization using CloudWatch metrics for ingress/egress bytes.
+ Check for packet loss using continuous ping tests from clients.
+ Verify that Client VPN endpoint is not hitting connection limits.
+ Consider using multiple Client VPN endpoints for load distribution.
+ Test with different client locations to identify regional performance issues.

### Monitor Client VPN metrics
<a name="MonitorClientVPNMetrics"></a>

Monitor Client VPN endpoint metrics using CloudWatch:

1. Check active connection metrics:

   ```
   aws cloudwatch get-metric-statistics \
     --namespace AWS/ClientVPN \
     --metric-name ActiveConnectionsCount \
     --dimensions Name=Endpoint,Value={{cvpn-endpoint-id}} \
     --start-time {{start-time}} \
     --end-time {{end-time}} \
     --period 300 \
     --statistics Average
   ```

1. Review authentication failure metrics:

   ```
   aws cloudwatch get-metric-statistics \
     --namespace AWS/ClientVPN \
     --metric-name AuthenticationFailures \
     --dimensions Name=Endpoint,Value={{cvpn-endpoint-id}} \
     --start-time {{start-time}} \
     --end-time {{end-time}} \
     --period 300 \
     --statistics Sum
   ```

1. Review other available metrics such as ingress and egress bytes and packets.

### Check Client VPN logs
<a name="CheckClientVPNLogs"></a>

Client VPN connection logs provide detailed information about connection attempts and errors:
+ Enable Client VPN connection logging if not already configured.
+ Review CloudWatch logs for connection attempts, authentication failures, and authorization errors.
+ Look for specific error codes and messages that indicate the root cause of connectivity issues.
+ Check for patterns in failed connections that might indicate configuration problems.

### Common issues and solutions
<a name="CommonIssues"></a>

Common issues that can affect Client VPN connectivity:

Authentication failures  
Client certificates expired or invalid, or Active Directory credentials incorrect. Verify authentication configuration and credential validity.

Missing authorization rules  
Clients cannot access target networks due to missing or incorrect authorization rules. Add appropriate authorization rules for the required networks.

Split tunneling issues  
Traffic routing incorrectly due to split tunneling configuration. Review and adjust split tunneling settings as needed.

Client IP pool exhaustion  
No available IP addresses in the client CIDR block. Expand the client CIDR range or disconnect unused clients.

MTU issues  
Large packets are being dropped due to MTU size limitations. Try setting the MTU to 1436 bytes or enable Path MTU Discovery on client devices.

DNS resolution problems  
Clients cannot resolve private DNS names. Verify DNS server configuration and ensure DNS traffic is allowed through security groups.

Overlapping IP ranges  
Client CIDR blocks conflict with local network ranges. Check for and resolve any overlapping IP address ranges between client CIDR and local networks.

TLS handshake failures  
Connection fails during TLS negotiation. Check certificate validity, ensure correct cipher suites, and verify that client and server certificates are properly configured.

Route propagation delays  
New routes not immediately available to clients. Allow 1-2 minutes for route propagation after making changes to Client VPN routes.

Connection drops/instability  
Frequent disconnections or unstable connections. Check for network congestion, firewall interference, or power management settings on client devices.

# Document history for the Client VPN User Guide
<a name="WhatsNew"></a>

The following table describes the AWS Client VPN Administrator Guide updates.

| Change | Description | Date | 
| --- |--- |--- |
| [IPv6 support](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/ipv6-considerations.html) | Client VPN now enables full IPv6 connectivity for Client VPN endpoints, supporting connections to IPv6 resources in your VPCs and from clients on IPv6 networks. | August 25, 2025 | 
| [Client route enforcement feature](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-cre.html) | Addition of client route enforcement feature. | April 20, 2025 | 
| [Increased Client VPN quota](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/limits.html) | Increased the Authorization rules per Client VPN endpoint quota from 50 to 200. | March 13, 2025 | 
| [Support for disconnect on session timeout](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-max-duration.html) | Session timeout now supports disconnect on when maximum session duration is reached. | January 13, 2025 | 
| [Increased quotas](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/limits.html) | The quotas for Authorization rules per Client VPN endpoint and Routes per Client VPN endpoint increased from 50 and 10 respectively to 100. | December 19, 2024 | 
| [Authorization rule examples](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/how-it-works.html#scenario) | Addition of example scenarios for authorization rules. | September 15, 2022 | 
| [VPN session maximum duration](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-max-duration.html) | You can configure a shorter maximum VPN session duration to meet security and compliance requirements. | January 20, 2022 | 
| [Client login banner](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-login-banner.html) | You can enable a text banner on AWS provided Client VPN desktop applications when a VPN session is established to meet regulatory and compliance needs. | January 20, 2022 | 
| [Client connect handler](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/connection-authorization.html) | You can enable the client connect handler for your Client VPN endpoint to run custom logic that authorizes new connections. | November 4, 2020 | 
| [Self-service portal](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-self-service-portal.html) | You can enable a self-service portal on your Client VPN endpoint for your clients. | October 29, 2020 | 
| [Client-to-client access](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/how-it-works.html#scenario) | You can enable clients that connect to a Client VPN endpoint to connect to each other. | September 29, 2020 | 
| [SAML 2.0-based federated authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-authentication.html#federated-authentication) | You can authenticate Client VPN users using SAML 2.0-based federated authentication. | May 19, 2020 | 
| [Specify security groups during creation](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-create.html) | You can specify a VPC and security groups when you create your AWS Client VPN endpoint. | March 5, 2020 | 
| [Configurable VPN ports](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-create.html) | You can specify a supported VPN port number for your AWS Client VPN endpoint. | January 16, 2020 | 
| [Support for multi-factor authentication (MFA)](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rules.html) | Your AWS Client VPN endpoint supports MFA if it's enabled for your Active Directory. | September 30, 2019 | 
| [Support for split-tunnel](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html) | You can enable split-tunnel on your AWS Client VPN endpoint. | July 24, 2019 | 
| [Initial release](#WhatsNew) | This release introduces AWS Client VPN. | December 18, 2018 | 