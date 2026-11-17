# AWS Prescriptive Guidance Encryption best practices and features for AWS services

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
+ [Encryption best practices and features for AWS services](#introduction)
+ [AWS approach to cryptography](#aws-cryptography-services)
+ [General encryption best practices](#general-encryption-best-practices)
+ [Encryption best practices for AWS services](#services-best-practices)
   + [AWS CloudTrail](#cloudtrail)
   + [Amazon DynamoDB](#dynamodb)
   + [Amazon Elastic Compute Cloud and Amazon Elastic Block Store](#ec2-ebs)
   + [Amazon Elastic Container Registry](#ecr)
   + [Amazon Elastic Container Service](#ecs)
   + [Amazon Elastic File System](#efs)
   + [Amazon Elastic Kubernetes Service](#eks)
   + [AWS Encryption SDK](#encryption-sdk)
   + [AWS Key Management Service](#kms)
   + [AWS Lambda](#lambda)
   + [Amazon Relational Database Service](#rds)
   + [AWS Secrets Manager](#secrets-manager)
   + [Amazon Simple Storage Service](#s3)
   + [Amazon Virtual Private Cloud](#vpc)
+ [Resources](#resources)
+ [Document history](#doc-history)

-----



# Encryption best practices and features for AWS services
<a name="introduction"></a>

*Kurt Kumar and Niko Borodachuk, Amazon Web Services*

## Business value of encryption
<a name="business-value-of-encryption.da198e1c-fdb5-5a97-8c0d-8a0a5c414bc5"></a>

Encryption is a fundamental cybersecurity tool for protecting sensitive data. Safeguarding your data through robust encryption practices is an essential component of a comprehensive data protection strategy for all your business operations, including generative AI deployments. This guide helps you understand the encryption principles and the encryption capabilities that AWS offers, so you can make informed decisions on how to achieve your compliance and business goals in AWS.

Modern cybersecurity threats include the risk of unauthorized disclosure,which is loss of confidentiality of data. Data is a business asset that is unique to each organization. It can include customer information, business plans, design documents, or code. Protecting the business means protecting its data.

[Data encryption](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/about-data-encryption.html) serves as a crucial safeguard for your business data, offering defense in depth in the event of unintentional or unauthorized access to your information systems. To access encrypted data in AWS, for example, users need permissions to use the key to decrypt and need permissions to use the service where the data resides. Without both of these permissions, users are unable to decrypt and view the data.

Generally, there are three types of data that you can encrypt.
+ Data at rest is data that is stationary and dormant, such as data that is in storage or written to disk. Examples include block storage, object storage, electronic file storage (EFS), database repositories, network-attached storage (NAS), and storage-area networks (SANs).
+ Data in transit is data that is actively moving through your network, such as between network resources. Examples include web traffic (typically secured with TLS), interactive host session traffic (typically secured with SSH), and private network traffic (typically secured with IPSec and MACsec)      
+ Data in use encompasses data that is actively being processed by applications or services and is present in a system's memory at the time of processing, awaiting use by the CPU. Examples include AI/ML model inference on sensitive inputs; database query results in a buffer, or confidential data in a virtual machine's RAM.

With encryption across your AWS infrastructure, you achieve:
+ **Risk Mitigation**: Protect against  unauthorized access, even if physical security controls fail
+ **Customer Trust**: Demonstrate commitment to data protection and privacy
+ **Simplified Compliance**: Streamline adherence to regulatory requirements and meet the security expectations of your customers and partners
+ **Reduced Liability**: Minimize financial and reputational impact of potential security incidents

In addition, encryption serves as a critical control for meeting various compliance frameworks:
+ PCI-DSS: Mandatory for cardholder data protection (Requirement 3.4)
+ GDPR: Recognized as an appropriate technical measure for data protection (Article 32)
+ SOC 2: Demonstrates security controls for confidentiality and privacy
+ Healthcare data regulations: Required for protecting sensitive health information, such as HIPAA (US) or GDPR health data provisions (EU)
+ Government cloud certifications: Required for regulated government workloads, such as FedRAMP (US), C5 (Germany), or IRAP (Australia)
+ FIPS 140: Required when processing US or Canadian government data. To support this requirement, AWS provides FIPS validated cryptographic modules and dedicated FIPS endpoints for managed services.
+ Isolated computing environments provide isolated environments that prevent operators from accessing data.

This guide discusses considerations and strategies for encrypting data in transit and data at rest. It also provides an overview of options for securing data in use in AWS. Th e recommendations in this guide can help you build a consistent, defense-in-depth encryption strategy across your AWS Cloud environment. The individual service documentation provides implementation steps tailored to your workloads.

### Intended audience
<a name="intended-audience"></a>

This guide can be used by small, medium, and large organizations in both public and private sectors. Whether your organization is in the initial stages of assessing and implementing a data protection strategy or aiming to enhance existing security controls, the recommendations outlined in this guide are best suited for the following audiences:
+ Executive officers who formulate policies for their enterprise, such as chief executive officers (CEOs), chief technology officers (CTOs), chief information officers (CIOs), and chief information security officers (CISOs)
+ Technology officers who are responsible for setting up technical standards, such as technical vice presidents and directors
+ Business stakeholders and application owners who are responsible for:
  + Assessing risk posture, data classification, and protection requirements
  + Monitoring compliance with established organizational standards
+ Compliance, internal audit, and governance officers who are in charge of monitoring adherence to compliance policies, including statutory and voluntary compliance regimes

# AWS approach to cryptography
<a name="aws-cryptography-services"></a>

*Cryptographic algorithms *are mathematical constructions designed to provide security services like confidentiality (encryption), authenticity (message authentication codes and digital signatures) and non-repudiation (digital signatures). If you are new to cryptography, encryption, and related terminology, we recommend that you read [About data encryption](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/about-data-encryption.html) before proceeding with this guide.

## AWS cryptographic foundations
<a name="foundations"></a>

Cryptography is an essential part of security for AWS. AWS services support encryption for data in transit, at rest, or in memory.  You can learn more about the AWS commitment to innovation and investing in additional controls for sovereignty and encryption features in our blog post announcing the [AWS digital sovereignty pledge](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/).

AWS follows the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) to protect your data. AWS services use trusted cryptographic algorithms that meet industry standards and foster interoperability. These algorithms are vetted by public standards bodies and academic research. The associated standards are widely accepted by governments, industry, and academia.

AWS defaults to high-assurance cryptographic implementations and prefers hardware-optimized solutions that are efficient. Our cryptographic core library, [AWS-LC](https://github.com/aws/aws-lc), is available as open source for transparency and industry-wide reuse. The recommended cryptographic algorithms in AWS-LC are formally verified for correctness, and the library is validated under NIST's FIPS-140 program.

## Cryptographic algorithms
<a name="about-algorithms"></a>

We define three types of cryptographic algorithms:
+ *Asymmetric* *cryptography* uses a pair of keys: a public key for encryption (or verifying) and a private key for decryption (or signing). You can share the public key because it isn't used for decryption, but access to the private key should be highly restricted. AWS services support or plan to support post-quantum algorithms, such as ML-KEM and ML-DSA. AWS services also support traditional cryptographic algorithms, such as RSA and elliptic-curve cryptography (ECC).
+ *Symmetric* *cryptography* uses the same key to encrypt and decrypt, or authenticate and verify the data. AWS services generally integrate with AWS Key Management Service (AWS KMS) for encryption of data at rest, which uses a mode of AES-256.  
+ *Other cryptographic functions* are used in conjunction with asymmetric and symmetric cryptography to build secure, practical protocols for confidentiality, integrity, authentication, and non-repudiation applications. Examples include hash functions and key derivation functions.

## Recommended cryptographic algorithms in AWS
<a name="algorithms"></a>

The following tables summarize the cryptographic algorithms, modes, and key sizes that AWS considers suitable for deployment across its services to protect your data. This guidance will evolve over time as cryptographic standards evolve.

Algorithms available within services can vary and are explained in the documentation for each service. If you need a software library implementation for an approved algorithm, please check to see if it is included in the latest version of the [AWS-LC library](https://github.com/aws/aws-lc). 

Algorithms are approved for use in AWS under one of two categories:
+ *Preferred* algorithms meet the AWS security and performance standards.
+ *Acceptable* algorithms can be used for compatibility in some applications but are not preferred.

### Asymmetric cryptography
<a name="asymmetric-cryptography.bf5b1ec4-10bc-54db-9c8b-9a357ea882ca"></a>

The following table lists asymmetric algorithms considered suitable for use within AWS for encryption, key agreement, and digital signatures.


| 
| 
| **Type** | **Algorithm** | **Status** | 
| --- |--- |--- |
| Encryption | RSA-OAEP (≥2048-bit modulus) | Acceptable | 
| Encryption | HPKE (P-256 or P-384, HKDF and AES-GCM) | Acceptable | 
| Key agreement | ML-KEM-768 or ML-KEM-1024 | Preferred (quantum-resistant) | 
| Key agreement | ECDSA with P-256, P-384, P-521, or Ed25519 | Acceptable | 
| Key agreement | ECDH(E) with brainpoolP256r1, brainpoolP384r1, or brainpoolP512r1 | Acceptable | 
| Signatures | ML-DSA-65 or ML-DSA-87 | Preferred (quantum-resistant) | 
| Signatures | SLH-DSA | Acceptable (quantum-resistant) | 
| Signatures | ECDSA with P-384 | Acceptable | 
| Signatures | ECDSA with P-256, P-521, or Ed25519 | Acceptable | 
| Signatures | RSA (≥2048-bit modulus) | Acceptable | 

### Symmetric cryptography
<a name="symmetric-cryptography.7cb55a3e-eecb-5f61-82b7-4faa705ac662"></a>

The following table lists symmetric algorithms considered suitable for use within AWS for encryption, authenticated encryption, and key wrapping.


| 
| 
| **Type** | **Algorithm** | **Status** | 
| --- |--- |--- |
| Authenticated encryption | AES-GCM-256 | Preferred | 
| Authenticated encryption | AES-GCM-128 | Acceptable | 
| Authenticated encryption | ChaCha20/Poly1305 | Acceptable | 
| Encryption modes | AES-XTS-256 (for block storage) | Preferred | 
| Encryption modes | AES-CBC / CTR (unauthenticated modes) | Acceptable | 
| Key wrapping | AES-GCM-256 | Preferred | 
| Key wrapping | AES-KW or AES-KWP with 256-bit keys | Acceptable | 

### Other cryptographic functions
<a name="other-cryptographic-functions.f1580287-815e-5157-9e15-9a2ca3d80bfa"></a>

The following table lists algorithms considered suitable for use within AWS for hashing, key derivation, and message authentication.


| 
| 
| **Type** | **Algorithm** | **Status** | 
| --- |--- |--- |
| Hashing | SHA-384 | Preferred | 
| Hashing | SHA-256 | Acceptable | 
| Hashing | SHA3 | Acceptable | 
| Key derivation | HKDF\_Expand or HKDF with SHA-256 | Preferred | 
| Key derivation | Counter Mode KDF with HMAC-SHA-256 | Acceptable | 
| Message authentication code | HMAC-SHA-384 | Preferred | 
| Message authentication code | HMAC-SHA-256 | Acceptable | 
| Message authentication code | KMAC | Acceptable | 
| Password hashing | scrypt with SHA384 | Preferred | 
| Password hashing | PBKDF2 | Acceptable | 

## Cryptography used in AWS services
<a name="used-services"></a>

AWS services rely on secure, open-source implementations of vetted algorithms to protect your data. The specific choices and configurations of algorithms will vary by service. Some AWS tools and services use a specific algorithm. In others, you can choose between supported algorithms and key lengths, or you can use the recommended defaults.

AWS cryptographic services comply with a wide range of cryptographic security standards, so you can comply with governmental or industry regulations. For a full list of the data security standards that AWS services comply with, see [AWS compliance programs](https://aws.amazon.com/compliance/programs/).

# General encryption best practices
<a name="general-encryption-best-practices"></a>

This section provides recommendations that apply when encrypting data in the AWS Cloud. These general encryption best practices are not specific to AWS services. This section includes the following topics:
+ [Data classification](#data-classification)
+ [Encryption of data in transit](#encryption-of-data-in-transit)
+ [Encryption of data at rest](#encryption-of-data-at-rest)

## Data classification
<a name="data-classification"></a>

*Data classification* is a process for identifying and categorizing the data in your network based on its criticality and sensitivity. It is a critical component of any cybersecurity risk management strategy because it helps you determine the appropriate protection and retention controls for the data. [Data classification](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-classification.html) is a component of the security pillar in the AWS Well-Architected Framework. Categories might include *highly confidential*, *confidential*, *non-confidential*, and *public*, but the classification tiers and their names can vary from organization to organization. For more information about the data classification process, considerations, and models, see [Data classification](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification-overview.html) (AWS Whitepaper).

After you have classified your data, you can create an encryption strategy for your organization based on the level of protection required for each category. For example, your organization might decide that highly confidential data should use asymmetric encryption and that public data doesn't require encryption. For more information about designing an encryption strategy, see [Creating an enterprise encryption strategy for data at rest](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/welcome.html). Although the technical considerations and recommendations in that guide are specific to data at rest, you can use the phased approach to create an encryption strategy for data in transit as well.

## Encryption of data in transit
<a name="encryption-of-data-in-transit"></a>

All data transmitted between AWS Regions over the AWS global network is automatically encrypted by AWS at the physical layer before it leaves AWS secured facilities. AWS encrypts all traffic between Availability Zones.

For data flowing through your workloads, the following are general best practices when encrypting data in transit in the AWS Cloud:
+ Define an organizational encryption policy for data in transit, based on your data classification, organizational requirements, and any applicable regulatory or compliance standards. We strongly recommend that you encrypt data in transit that is classified as highly confidential or confidential. Your policy might also specify encryption for other categories, such as non-confidential or public data, on an as-needed basis.
+ When encrypting data in transit, we recommend using approved cryptography algorithms, block cipher modes, and key lengths, as defined in your encryption policy. We further recommend periodically reviewing the TLS policies associated with your Application Load Balancers, Amazon API Gateway resources, Amazon CloudFront resources, and Amazon Virtual Private Cloud Console (Amazon VPC) resources to make sure that they are aligned with your current encryption policy.
+ Encrypt traffic between information assets and systems within the corporate network and AWS Cloud infrastructure by using one of the following:
  + [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) connections
  + A combination of AWS Site-to-Site VPN and [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) connections, which provides an IPsec-encrypted private connection
  + Direct Connect connections that support MAC Security (MACsec) to encrypt data from corporate networks to the Direct Connect location
+ Identify access control policies for managed certificates and TLS policy configurations based on the principle of least privilege. *Least privilege* is the security best practice of granting users the minimum access they need to perform their job functions. For more information about applying least-privilege permissions, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) and [Best practices for IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies-best-practices.html).

## Encryption of data at rest
<a name="encryption-of-data-at-rest"></a>

AWS has adopted transparent encryption of data at rest as the standard security posture across its service portfolio. This encryption is transparent to the customer, ensuring that data is protected at rest and without requiring explicit configuration. Unless explicitly changed by the customer to use customer managed keys via AWS KMS, the transparent encryption mechanism remains in effect across all applicable services and deployment paths. 

You can encrypt data using server-side encryptionor client-side encryption basedon factors such as data classification, the need for end-to-end encryption, or technical limitations that prevent you from using end-to-end encryption:
+ Server-side encryption is the act of encrypting data at its destination, by the application or service that receives it and owns the security of its storage layer. Server-side encryption always happens transparently using keys managed by AWS on your behalf in AWS KMS, but you can also opt into each service using a customer-managed key from AWS KMS that you manage directly instead. Customer-managed keys in AWS KMS give you more control over creation, rotation, sharing (for example with software vendors), and governance.  With transparent encryption, the AWS service controls when the key is used to encrypt and decrypt your data in response to your requests of the service to write and read your data. With a customer managed key, you get to define permissions that control when the AWS service is allowed to use your key for encryption and decryption in response to your requests of the service to write and read your data.
+ Client-side encryption is the act of encrypting data locally before the target application or service receives it. The AWS service receives encrypted data; it does not play a role in encrypting or decrypting it. For client-side encryption, you can use the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html), optionally integrated with AWS KMS for key management, or use other encryption libraries and key management solutions.

  For more information and detailed examples for specific use cases, refer to the*Data Encryption *section of any AWS service's documentation.

# Encryption best practices for AWS services
<a name="services-best-practices"></a>

This section includes best practices and recommendations for the following AWS services:
+ [AWS CloudTrail](#cloudtrail)
+ [Amazon DynamoDB](#dynamodb)
+ [Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Elastic Block Store (Amazon EBS)](#ec2-ebs)
+ [Amazon Elastic Container Registry (Amazon ECR)](#ecr)
+ [Amazon Elastic Container Service (Amazon ECS)](#ecs)
+ [Amazon Elastic File System (Amazon EFS)](#efs)
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](#eks)
+ [AWS Encryption SDK](#encryption-sdk)
+ [AWS Key Management Service (AWS KMS)](#kms)
+ [AWS Lambda](#lambda)
+ [Amazon Relational Database Service (Amazon RDS)](#rds)
+ [AWS Secrets Manager](#secrets-manager)
+ [Amazon Simple Storage Service (Amazon S3)](#s3)
+ [Amazon Virtual Private Cloud (Amazon VPC)](#vpc)

## AWS CloudTrail
<a name="cloudtrail"></a>

[AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you audit the governance, compliance, and operational and risk of your AWS account.

Consider the following encryption best practices for this service:
+ CloudTrail logs should be encrypted using a customer managed AWS KMS key. Choose a KMS key that is in the same region as the S3 bucket that receives your log files. For more information, see [Updating a trail to use your KMS key](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-kms-key-policy-for-cloudtrail-update-trail.html).
+ As an additional security layer, enable log file validation for trails. This helps you determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it. For instructions, see [Enabling log file integrity validation for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-enabling.html).
+ Use interface VPC endpoints to enable CloudTrail to communicate with resources in other VPCs without traversing the public internet. For more information, see [Using AWS CloudTrail with interface VPC endpoints](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-and-interface-VPC.html).
+ Add an `aws:SourceArn` condition key to the KMS key policy to ensure that CloudTrail uses the KMS key only for a specific trail or trails. For more information, see [Configure AWS KMS key policies for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-kms-key-policy-for-cloudtrail.html).
+ In AWS Config, implement the [cloud-trail-encryption-enabled](https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-encryption-enabled.html) AWS managed rule to validate and enforce log file encryption.
+ If CloudTrail is configured to send notifications through Amazon Simple Notification Service (Amazon SNS) topics, add an `aws:SourceArn` (or optionally `aws:SourceAccount`) condition key to the CloudTrail policy statement to prevent unauthorized account access to the SNS topic. For more information, see [Amazon SNS topic policy for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-permissions-for-sns-notifications.html).
+ If you are using AWS Organizations, create an organization trail that logs all events for the AWS accounts in that organization. This includes the management account and all member accounts in the organization. For more information, see [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html).
+ Create a trail that [applies to all AWS Regions](https://aws.amazon.com/blogs/mt/aws-cloudtrail-best-practices/) where you store corporate data, to record AWS account activity in those Regions. When AWS launches a new Region, CloudTrail automatically includes the new Region and logs events in that Region.

## Amazon DynamoDB
<a name="dynamodb"></a>

[Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance. DynamoDB encryption at rest secures data in an encrypted table—including its primary key, local and global secondary indexes, streams, global tables, backups, and DynamoDB Accelerator (DAX) clusters whenever the data is stored in durable media.

In accordance with data classification requirements, data confidentiality and integrity can be maintained by implementing server-side or client-side encryption:

For server-side encryption, when you create a new table, you can use AWS KMS keys to encrypt the table. You can use AWS owned keys, AWS managed keys, or customer managed keys. We recommend using customer managed keys because your organization has full control of the key, and because when you use this key type, the table-level encryption key, the DynamoDB table, local and global secondary indexes, and streams are all encrypted with the same key. For more information about these key types, see [Customer keys and AWS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt).


| 
| 
| Note: You can switch between an AWS owned key, AWS managed key, and customer managed key at any given time. | 
| --- |

For client-side encryption and end-to-end protection of data, both at rest and in transit, you can use the [Amazon DynamoDB Encryption Client](https://docs.aws.amazon.com/dynamodb-encryption-client/latest/devguide/what-is-ddb-encrypt.html). In addition to encryption, which protects the confidentiality of the item attribute value, DynamoDB Encryption Client signs the item. This provides integrity protection by enabling detection of unauthorized changes to the item, including adding or deleting attributes, or substituting one encrypted value for another.

Consider the following encryption best practices for this service:
+ Limit permissions to disable or schedule deletion of the key to only those who need to perform these tasks. These states prevent all users and the DynamoDB service from being able to encrypt or decrypt data and to perform read and write operations on the table.
+ While DynamoDB encrypts data in transit by using HTTPS by default, additional security controls are recommended. You can use any of the following options:
  + AWS Site-to-Site VPN connection using IPsec for encryption.
  + AWS Direct Connect connection to establish a private connection.
  + AWS Direct Connect connection with AWS Site-to-Site VPN connection for an IPsec-encrypted private connection.
  + If access to DynamoDB is required only from within a virtual private cloud (VPC), you can use a VPC gateway endpoint and allow only resources in the VPC to access it. This prevents the traffic from traversing the public internet.
+ If you are using VPC endpoints, restrict the endpoint policies and IAM policies associated with the endpoint to only authorized users, resources, and services. For more information, see [Control access to DynamoDB endpoints by using IAM policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-ddb.html#iam-policies-ddb) and [Control access to services using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html).
+ You can implement column-level data encryption at the application level for data that requires encryption, according to your encryption policy.
+ Configure DAX clusters to encrypt data at rest, such as data in cache, configuration data, and log files, at the time of setting up the cluster. You can't enable encryption at rest on an existing cluster. This server-side encryption helps protect data from unauthorized access through the underlying storage. DAX encryption at rest automatically integrates with AWS KMS for managing the single-service default key that is used to encrypt the clusters. If a service default key doesn't exist when an encrypted DAX cluster is created, AWS KMS automatically creates a new AWS managed key. For more information, see [DAX encryption at rest](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAXEncryptionAtRest.html).


<table>
<tbody>
</tbody>
</table>

+ Configure DAX clusters to encrypt data in transit at the time of setting up the cluster. You can't enable encryption in transit on an existing cluster. DAX uses TLS to encrypt requests and responses between the application and the cluster, and it uses the cluster's x509 certificate to authenticate the identity of the cluster. For more information, see [DAX encryption in transit](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAXEncryptionInTransit.html).
+ In AWS Config, implement the [dax-encryption-enabled](https://docs.aws.amazon.com/config/latest/developerguide/dax-encryption-enabled.html) AWS managed rule to validate and maintain encryption of DAX clusters.

## Amazon Elastic Compute Cloud and Amazon Elastic Block Store
<a name="ec2-ebs"></a>

[Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down. [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) provides block-level storage volumes for use with EC2 instances.

Consider the following encryption best practices for these services:
+ Tag all EBS volumes with the appropriate data classification key and value. This helps you determine and implement the appropriate security and encryption requirements, according to your policy.
+ According to your encryption policy and the technical feasibility, configure encryption for data in transit between EC2 instances or between EC2 instances and your on-premises network.
+ Encrypt both the boot and data EBS volumes of an EC2 instance. An encrypted EBS volume protects the following data:
  + Data at rest inside the volume
  + All data moving between the volume and the instance
  + All snapshots created from the volume
  + All volumes created from those snapshots

  For more information, see [How EBS encryption works](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html).
+ Enable encryption by default for EBS volumes for your account in the current AWS Region. This enforces encryption of any new EBS volumes and snapshot copies. It has no effect on existing EBS volumes or snapshots. For more information, see [Enable encryption by default](https://docs.aws.amazon.com/ebs/latest/userguide/work-with-ebs-encr.html#encryption-by-default).
+ Encrypt the instance store root volume for an Amazon EC2 instance. This helps you protect configuration files and data stored with the operating system. For more information, see [How to protect data at rest with Amazon EC2 instance store encryption](https://aws.amazon.com/blogs/security/how-to-protect-data-at-rest-with-amazon-ec2-instance-store-encryption/) (AWS blog post)
+ In AWS Config, implement the [encrypted-volumes](https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html) rule to automated checks that validate and enforce appropriate encryption configurations.

## Amazon Elastic Container Registry
<a name="ecr"></a>

[Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that's secure, scalable, and reliable.

Amazon ECR stores images in Amazon S3 buckets that Amazon ECR manages. Each Amazon ECR repository has an encryption configuration, which is set when the repository is created. By default, Amazon ECR uses server-side encryption with Amazon S3-managed (SSE-S3) encryption keys. For more information, see [Encryption at rest](https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html) (Amazon ECR documentation).

Consider the following encryption best practices for this service:
+ Instead of using the default server-side encryption with Amazon S3-managed (SSE-S3) encryption keys, use customer managed KMS keys stored in AWS KMS. This key type provides the most granular control options.


<table>
<tbody>
</tbody>
</table>

+ Do not revoke the grants that Amazon ECR creates by default when you provision a repository. This can affect functionality, such as accessing data, encrypting new images pushed to the repository, or decrypting them when they are pulled.
+ Use AWS CloudTrail to record the requests that Amazon ECR sends to AWS KMS. The log entries contain an encryption context key to make them more easily identifiable.
+ Configure Amazon ECR policies to control access from specific Amazon VPC endpoints or specific VPCs. Effectively, this isolates network access to a specific Amazon ECR resource, allowing access from only the specific VPC. By establishing a virtual private network (VPN) connection with an Amazon VPC endpoint, you can encrypt data in transit.
+ Amazon ECR supports resource-based policies. Using these policies, you can restrict access based on the source IP address or the specific AWS service.

## Amazon Elastic Container Service
<a name="ecs"></a>

[Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a fast and scalable container management service that helps you run, stop, and manage containers on a cluster.

With Amazon ECS, you can encrypt data in transit by using any of the following approaches:
+ Create a service mesh. Using AWS App Mesh, configure TLS connections between the deployed [Envoy](https://docs.aws.amazon.com/app-mesh/latest/userguide/envoy.html) proxies and mesh endpoints, such as [virtual nodes](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html) or [virtual gateways](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html). You can use TLS certificates from AWS Private Certificate Authority or customer-provided certificates. For more information and walkthroughs, see [Enable traffic encryption between services in AWS App Mesh using AWS Certificate Manager (ACM) or customer-provided certificates](https://aws.amazon.com/blogs/containers/enable-traffic-encryption-between-services-in-aws-app-mesh-using-aws-certificate-manager-or-customer-provided-certificates/) (AWS blog post).
+ If supported, use [AWS Nitro Enclaves](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html). AWS Nitro Enclaves is an Amazon EC2 feature that allows you to create isolated execution environments, called *enclaves*, from Amazon EC2 instances. They are designed to help protect your most sensitive data. Additionally, [ACM for Nitro Enclaves](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-refapp.html) allows you to use public and private SSL/TLS certificates with your web applications and web servers running on Amazon EC2 instances with AWS Nitro Enclaves. For more information, see [AWS Nitro Enclaves – Isolated EC2 Environments to Process Confidential Data](https://aws.amazon.com/blogs/aws/aws-nitro-enclaves-isolated-ec2-environments-to-process-confidential-data/) (AWS blog post).
+ Use Server Name Indication (SNI) protocol with Application Load Balancers. You can deploy multiple applications behind a single HTTPS listener for an Application Load Balancer. Each listener has its own TLS certificate. You can certificates provided by ACM, or you can use self-signed certificates. Both [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) and [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html) support SNI. For more information, see [Application Load Balancers Now Support Multiple TLS Certificates with Smart Selection Using SNI](https://aws.amazon.com/blogs/aws/new-application-load-balancer-sni/) (AWS blog post).
+ For improved security and flexibility, use AWS Private Certificate Authority to deploy a TLS certificate with the Amazon ECS task. For more information, see [Maintaining TLS all the way to your container part 2: Using AWS Private CA](https://aws.amazon.com/blogs/compute/maintaining-transport-layer-security-all-the-way-to-your-container-part-2-using-aws-certificate-manager-private-certificate-authority/) (AWS blog post).
+ Implement mutual TLS ([mTLS](https://docs.aws.amazon.com/app-mesh/latest/userguide/mutual-tls.html)) in App Mesh by using [Secret discovery service](https://www.envoyproxy.io/docs/envoy/latest/configuration/security/secret) (Envoy) or certificates [hosted in ACM](https://github.com/aws/aws-app-mesh-examples/tree/main/walkthroughs/howto-mutual-tls-file-provided) (GitHub).

Consider the following encryption best practices for this service:
+ Where technically feasible, for enhanced security, configure [Amazon ECS interface VPC endpoints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/vpc-endpoints.html) in AWS PrivateLink. Accessing these endpoints over a VPN connection encrypts data in transit.
+ Store sensitive materials, such as API keys or database credentials, securely. You can store these as encrypted parameters in Parameter Store, a capability of AWS Systems Manager. However, we recommend you use AWS Secrets Manager because this service allows you to automatically rotate secrets, generate random secrets, and share secrets across AWS accounts.
+ If users or applications in your data center or an external third party on the web are making direct HTTPS API requests to AWS services, sign those requests with temporary security credentials obtained from AWS Security Token Service (AWS STS).

## Amazon Elastic File System
<a name="efs"></a>

[Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) helps you create and configure shared file systems in the AWS Cloud.

Consider the following encryption best practices for this service:
+ In AWS Config, implement the [efs-encrypted-check](https://docs.aws.amazon.com/config/latest/developerguide/efs-encrypted-check.html) AWS managed rule. This rule checks if Amazon EFS is configured to encrypt the file data using AWS KMS.
+ Enforce encryption for Amazon EFS file systems by creating an Amazon CloudWatch alarm that monitors CloudTrail logs for `CreateFileSystem` events and triggers an alarm if an unencrypted file system is created. For more information, see [Walkthrough: Enforcing Encryption on an Amazon EFS File System at Rest](https://docs.aws.amazon.com/efs/latest/ug/efs-enforce-encryption.html).
+ Mount the file system by using the [EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html). This sets up and maintains a TLS 1.2 tunnel between the client and the Amazon EFS service and routes all Network File System (NFS) traffic over this encrypted tunnel. The following command implements the use of TLS for in-transit encryption.

  ```
  sudo mount -t efs  -o tls file-system-id:/ /mnt/efs
  ```

  For more information, see [Using EFS mount helper to mount EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html).
+ Using AWS PrivateLink, implement interface VPC endpoints to establish a private connection between VPCs and the Amazon EFS API. Data in transit over the VPN connection to and from the endpoint is encrypted. For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html).
+ Use the `elasticfilesystem:Encrypted` condition key in IAM identity-based policies to prevent users from creating EFS file systems that aren't encrypted. For more information, see [Using IAM to enforce creating encrypted file systems](https://docs.aws.amazon.com/efs/latest/ug/using-iam-to-enforce-encryption-at-rest.html).
+ KMS keys used for EFS encryption should be configured for least-privilege access by using resource-based key policies.
+ Use the `aws:SecureTransport` condition key in the EFS file system policy to enforce use of TLS for NFS clients when connecting to an EFS file system. For more information, see [Encryption of data in transit](https://docs.aws.amazon.com/whitepapers/latest/efs-encrypted-file-systems/encryption-of-data-in-transit.html) in *Encrypting File Data with Amazon Elastic File System* (AWS Whitepaper).

## Amazon Elastic Kubernetes Service
<a name="eks"></a>

[Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes. In Kubernetes, *secrets* help you manage sensitive information, such as user certificates, passwords, or API keys. By default, these secrets are stored unencrypted in the API server's underlying data store, which is called [etcd](https://etcd.io/docs/v3.5/faq/). On Amazon EKS, the Amazon Elastic Block Store (Amazon EBS) volumes for `etcd` nodes are encrypted with [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html). Any user with API access or access to `etcd` can retrieve or modify a secret. Additionally, anyone who is authorized to create a pod in a namespace can use that access to read any secret in that namespace. You can encrypt these secrets at rest in Amazon EKS by using AWS KMS keys, either AWS managed keys or customer managed keys. An alternative approach to using `etcd` is using [AWS Secrets and Config Provider (ASCP)](https://github.com/aws/secrets-store-csi-driver-provider-aws) (GitHub repository). ASCP integrates with IAM and resource-based policies to limit and restrict access to secrets only within specific Kubernetes pods inside a cluster.

You can use the following AWS storage services with Kubernetes:
+ For Amazon EBS, you can use the in-tree storage driver or the [Amazon EBS CSI driver](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html). Both include parameters for encrypting volumes and supplying a customer managed key.
+ For Amazon Elastic File System (Amazon EFS), you can use the [Amazon EFS CSI driver](https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html) with support for both dynamic and static provisioning.

Consider the following encryption best practices for this service:
+ If you are using `etcd`, which stores secret objects unencrypted by default, do the following to help protect secrets:
  + [Encrypt secret data at rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) (Kubernetes documentation).
  + Use AWS KMS for envelope encryption of Kubernetes secrets. This allows you to encrypt your secrets with a unique data key. You can use an AWS KMS key encryption key to encrypt the data key. You can automatically rotate the key encryption key on a recurring schedule. With the AWS KMS plugin for Kubernetes, all Kubernetes secrets are stored in `etcd` in ciphertext. They can only be decrypted by the Kubernetes API server. For more information, see [Using Amazon EKS encryption provider support for defense in depth](https://aws.amazon.com/blogs/containers/using-eks-encryption-provider-support-for-defense-in-depth/) and [Encrypt Kubernetes secrets with AWS KMS on existing clusters](https://docs.aws.amazon.com/eks/latest/userguide/enable-kms.html).
  + Enable or configure authorization through role-based access control (RBAC) rules that restrict reading and writing the secret. Restrict permissions to create new secrets or replace existing ones. For more information, see [Authorization overview](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) (Kubernetes documentation).
  + If you are defining multiple containers in a pod and only one of those containers needs access to a secret, define the volume mount so that the other containers do not have access to that secret. Secrets that are mounted as volumes are instantiated as `tmpfs` volumes and are automatically removed from the node when the pod is deleted. You could also use environment variables, but we don't recommend this approach because the values of environment variables can appear in logs. For more information, see [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) (Kubernetes documentation).
  + When possible, avoid granting access to `watch` and `list` requests for secrets within a namespace. In the Kubernetes API, these requests are powerful because they allow the client to inspect the values of every secret in that namespace.
  + Allow only cluster administrators to access `etcd`, including read-only access.
  + If there are multiple `etcd` instances, ensure `etcd` is using TLS for communication between `etcd` peers.
+ If you are using ASCP, do the following to help protect secrets:
  + Use [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) to limit secret access to only authorized pods.
  + Enable encryption of Kubernetes secrets by using the [AWS Encryption Provider](https://github.com/kubernetes-sigs/aws-encryption-provider) (GitHub repository) to implement envelope encryption with a customer managed KMS key.
+ To help mitigate the risk of data leaks from environment variables, we recommend you use the [AWS Secrets Manager and Config Provider for Secret Store CSI Driver](https://github.com/aws/secrets-store-csi-driver-provider-aws) (GitHub). This driver allows you to make secrets stored in Secrets Manager and parameters stored in Parameter Store appear as files mounted in Kubernetes pods.
**Note**  
AWS Fargate is not supported.
+ Create an Amazon CloudWatch metrics filter and alarm to send alerts for administrator-specified operations, such as secret deletion or use of a secret version in the waiting period to be deleted. For more information, see [Creating an alarm based on anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html).

## AWS Encryption SDK
<a name="encryption-sdk"></a>

The [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) is an open-source, client-side encryption library. It uses industry standards and best practices to support implementation and interoperability in several [programming languages](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/programming-languages.html). AWS Encryption SDK encrypts data by using a secure, authenticated, symmetric key algorithm and offers default implementation that adheres to cryptography best practices. For more information, see [Supported algorithm suites in the AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/supported-algorithms.html). 

One of the key features of the AWS Encryption SDK is support for encrypting data in use. By adopting an encrypt-then-use approach, you can encrypt sensitive data before it is processed by your application logic. This can help protect the data from potential exposure or tampering, even if the application itself is affected by a security event. 

Consider the following best practices for this service:
+ Adhere to all of the recommendations in [Best practices for the AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/best-practices.html).
+ Select one or more wrapping keys to help protect your data keys. For more information, see [Select wrapping keys](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/configure.html#config-keys).
+ Pass the `KeyId`** **parameter to the [ReEncrypt](https://docs.aws.amazon.com/cli/latest/reference/kms/re-encrypt.html) operation to help prevent use of an untrusted KMS key. For more information, see [Improved client-side encryption: Explicit KeyIds and key commitment](https://aws.amazon.com/blogs/security/improved-client-side-encryption-explicit-keyids-and-key-commitment/) (AWS blog post).
+ When using the AWS Encryption SDK with AWS KMS, use local `KeyId` filtering. For more information, see [Improved client-side encryption: Explicit KeyIds and key commitment](https://aws.amazon.com/blogs/security/improved-client-side-encryption-explicit-keyids-and-key-commitment/) (AWS blog post).
+ For applications with large volumes of traffic requiring encryption or decryption, or if your account is exceeding AWS KMS [request quotas](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html), you can use the [data key caching](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/data-key-caching.html) feature of the AWS Encryption SDK. Note the following best practices for data key caching:
  + Configure [cache security thresholds](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/thresholds.html) to limit how long each cached data key is used and how much data is protected under each data key. For recommendations when configuring these thresholds, see [Setting cache security thresholds](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/thresholds.html).
  + Limit the local cache to the smallest number of data keys necessary to achieve the performance improvements for your specific application use case. For instructions and an example of configuring limits for the local cache, see [Using data key caching: Step-by-step](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/implement-caching.html).

  For more information, see [AWS Encryption SDK: How to Decide if Data Key Caching Is Right for Your Application](https://aws.amazon.com/blogs/security/aws-encryption-sdk-how-to-decide-if-data-key-caching-is-right-for-your-application/) (AWS blog post).

## AWS Key Management Service
<a name="kms"></a>

[AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data. AWS KMS integrates with most other AWS services that can encrypt your data. For a complete list, see [AWS services integrated with AWS KMS](https://aws.amazon.com/kms/features/#AWS_Service_Integration). AWS KMS also integrates with AWS CloudTrail to log use of your KMS keys for auditing, regulatory, and compliance needs.

KMS keys are the primary resource in AWS KMS, and they are logical representations of a cryptographic key. There are three primary types of KMS keys:
+ Customer managed keys are KMS keys that you create.
+ AWS managed keys are KMS keys that AWS services create in your account, on your behalf.
+ AWS owned keys are KMS keys that an AWS service owns and manages, for use in multiple AWS accounts.

For more information about these key types, see [Customer keys and AWS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys).

In the AWS Cloud, policies are used to control who can access resources and services. For example, in AWS Identity and Access Management (IAM), *identity-based policies* define permissions for users, user groups, or roles, and *resource-based policies* attach to a resource, such as an S3 bucket, and define which principals are allowed access, supported actions, and any other conditions that must be met. Similar to IAM policies, AWS KMS uses [key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) to control access to a KMS key. Each KMS key must have a key policy, and each key can have only one key policy. Note the following when defining policies that allow or deny access to KMS keys:
+ You can control the key policy for customer managed keys, but you can't directly control the key policy for AWS managed keys or for AWS owned keys.
+ Key policies allow for granting granular access to AWS KMS API calls within an AWS account. Unless the key policy explicitly allows it, you cannot use IAM policies to allow access to a KMS key. Without permission from the key policy, IAM policies that allow permissions have no effect. For more information, see [Allow IAM policies to allow access to the KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#key-policy-default-allow-root-enable-iam).
+ You can use an IAM policy to deny access to a customer managed key without corresponding permission from the key policy.
+ When designing key policies and IAM policies for multi-Region keys, consider the following:
  + Key policies are not [shared properties](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#mrk-sync-properties) of multi-Region keys and are not copied or synchronized among related multi-Region keys.
  + When a multi-Region key is created using the `CreateKey` and `ReplicateKey` actions, the [default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html) is applied unless a key policy is specified in the request.
  + You can implement condition keys, such as [aws:RequestedRegion](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requestedregion), to limit permissions to a particular AWS Region.
  + You can use grants to allow permissions to a multi-Region primary key or replica key. However, a single grant cannot be used to allow permissions to multiple KMS keys, even if they are related multi-Region keys.

When using AWS KMS and creating key policies, consider the following encryption best practices and other security best practices:
+ Adhere to the recommendations in the following resources for AWS KMS best practices:
  + [Best practices for AWS KMS grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant-best-practices) (AWS KMS documentation)
  + [Best practices for IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies-best-practices.html) (AWS KMS documentation)
+ In accordance with the separation of duties best practice, maintain separate identities for those who administer keys and those who use them:
  + Administrator roles that create and delete keys should not have the ability to use the key.
  + Some services may only need to encrypt data and should not be granted the ability to decrypt the data using the key.
+ Key policies should always follow a model of least privilege. Do not use `kms:*` for actions in IAM or key policies because this gives the principal permissions to both administer and use the key.
+ Limit the use of customer managed keys to specific AWS services by using the [kms:ViaService](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-via-service) condition key within the key policy.
+ If you have a choice between key types, customer managed keys are preferred because they provide the most granular control options, including the following:
  + [Managing authentication and access control](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html)
  + [Enabling and disabling keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html)
  + [Rotating AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
  + [Tagging keys](https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html)
  + [Creating aliases](https://docs.aws.amazon.com/kms/latest/developerguide/programming-aliases.html)
  + [Deleting AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html)
+ AWS KMS administrative and modification permissions must be explicitly denied to unapproved principals and AWS KMS modification permissions should not exist in an allow statement for any unauthorized principals. For more information, see [Actions, resources, and condition keys for AWS Key Management Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awskeymanagementservice.html).
+ In order to detect unauthorized usage of KMS keys, in AWS Config, implement the [iam-customer-policy-blocked-kms-actions](https://docs.aws.amazon.com/config/latest/developerguide/iam-customer-policy-blocked-kms-actions.html) and [iam-inline-policy-blocked-kms-actions](https://docs.aws.amazon.com/config/latest/developerguide/iam-inline-policy-blocked-kms-actions.html) rules. This prevents principals from using the AWS KMS decryption actions on all resources.
+ Implement service control policies (SCPs) in AWS Organizations to prevent unauthorized users or roles from deleting KMS keys, either directly as a command or through the console. For more information, see [Using SCPs as preventative controls](https://aws.amazon.com/blogs/mt/identity-guide-preventive-controls-with-aws-identity-scps/) (AWS blog post).
+ Log AWS KMS API calls in a CloudTrail log. This records the relevant event attributes, such as what requests were made, the source IP address from which the request was made, and who made the request. For more information, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html).
+ If you use [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context), it shouldn't contain any sensitive information. CloudTrail stores the encryption context in plaintext JSON files, which can be viewed by anyone with access to the S3 bucket containing the information.
+ When monitoring usage of customer managed keys, configure events to notify you if specific actions are detected, such as key creation, updates to customer managed key policies, or import of key material are detected. It's also recommended that you implement automated responses, such as an AWS Lambda function that disables the key or performs any other incident response actions as dictated by your organizational policies.
+ [Multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-auth.html) are recommended for specific scenarios, such as compliance, disaster recovery, or backups. The security properties of multi-Region keys are significantly different than single-Region keys. The following recommendations apply when authorizing the creation, management, and use of multi-Region keys:
  + Allow principals to replicate a multi-Region key only into AWS Regions that require them.
  + Give permission for multi-Region keys only to principals who need them and only for tasks that require them.

## AWS Lambda
<a name="lambda"></a>

[AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. For securing your environment variables, you can use server-side encryption to protect your data at rest and client-side encryption to protect your data in transit.

Consider the following encryption best practices for this service:
+ Lambda always provides server-side encryption at rest with an AWS KMS key. By default, Lambda uses an AWS managed key. We recommend you use a customer managed key because you have full control over the key, including management, rotation, and auditing.
+ For data in transit that requires encryption, enable helpers, which ensures that environment variables are encrypted client-side for protection in transit by using the preferred KMS key. For more information, see *Security in transit* in [Securing environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption).
+ Lambda function environment variables that hold sensitive or critical data should be encrypted in transit to help protect the data that is dynamically passed to the functions (usually access information) from unauthorized access.
+ To prevent a user from viewing environment variables, add a statement to the user's permissions in the IAM policy or to the key policy that denies access to the default key, a customer managed key, or all keys. For more information, see [Using AWS Lambda environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html).

## Amazon Relational Database Service
<a name="rds"></a>

[Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database (DB) in the AWS Cloud. Data that is encrypted at rest includes the underlying storage for the DB instances, its automated backups, read replicas, and snapshots.

The following are the approaches you can use to encrypt data at rest in RDS DB instances:
+ You can encrypt Amazon RDS DB instances with AWS KMS keys, either an AWS managed key or a customer managed key. For more information, see [AWS Key Management Service](#kms) in this guide.
+ Amazon RDS for Oracle and Amazon RDS for SQL Server support encrypting DB instances with Transparent Data Encryption (TDE). For more information, see [Oracle Transparent Data Encryption](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.AdvSecurity.html) or [Support for Transparent Data Encryption in SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.TDE.html).

  You can use both TDE and KMS keys to encrypt DB instances. However, this can slightly affect the performance of your database, and you must manage these keys separately. 

The following are the approaches you can use to encrypt data in transit to or from RDS DB instances:
+ For an Amazon RDS DB instance running MariaDB, Microsoft SQL Server, MySQL, Oracle, or PostgreSQL, you can use SSL to encrypt the connection. For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html).
+ Amazon RDS for Oracle also supports Oracle native network encryption (NNE), which encrypts data as it moves to and from a DB instance. NNE and SSL encryption cannot be used simultaneously. For more information, see [Oracle native network encryption](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.NetworkEncryption.html).

Consider the following encryption best practices for this service:
+ When connecting to Amazon RDS for SQL Server or Amazon RDS for PostgreSQL DB instances in order to process, store, or transmit data that requires encryption, use the RDS Transport Encryption feature to encrypt the connection. You can implement this by setting the `rds.force_ssl` parameter to `1` in the parameter group. For more information, see [Working with parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html). Amazon RDS for Oracle uses Oracle database native network encryption.
+ Customer managed keys for RDS DB instance encryption should be used solely for that purpose and not used with any other AWS services.
+ Before encrypting an RDS DB instance, establish KMS key requirements. The key used by the instance cannot be changed later. For example, in your encryption policy, define use and management standards for AWS managed keys or customer managed keys, based on your business requirements.
+ When authorizing access to a customer managed KMS key, follow the principle of least-privilege by using condition keys in IAM policies. For example, to allow a customer managed key to be used only for requests that originate in Amazon RDS, use the [kms:ViaService condition key](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-via-service) with the `rds.<region>.amazonaws.com` value. Additionally, you can use keys or values in the [Amazon RDS encryption context](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.Keys.html#Overview.Encryption.Keys.encryptioncontext) as a condition for using the customer managed key.
+ It is strongly recommended that you enable backups for encrypted RDS DB instances. Amazon RDS can lose access to the KMS key for a DB instance, such as when the KMS key isn't enabled or when RDS access to a KMS key is revoked. If this occurs, the encrypted DB instance goes into a recoverable state for seven days. If the DB instance does not regain access to the key after seven days, the database becomes terminally inaccessible and must be restored from a backup. For more information, see [Encrypting a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html#Overview.Encryption.Enabling).
+ If a read replica and its encrypted DB instance are in the same AWS Region, you must use the same KMS key to encrypt both.
+ In AWS Config, implement the [rds-storage-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/rds-storage-encrypted.html) AWS managed rule to validate and enforce encryption for RDS DB instances and the [rds-snapshots-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshot-encrypted.html) rule to validate and enforce encryption for RDS database snapshots.
+ Use AWS Security Hub CSPM to evaluate whether your Amazon RDS resources follow security best practices. For more information, see [Security Hub CSPM controls for Amazon RDS](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html).

## AWS Secrets Manager
<a name="secrets-manager"></a>

[AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically. Secrets Manager integrates with AWS KMS to encrypt every version of every secret value with a unique data key that is protected by an AWS KMS key. This integration protects stored secrets with encryption keys that never leave AWS KMS unencrypted. You can also define custom permissions on the KMS key to audit the operations that generate, encrypt, and decrypt the data keys that protect stored secrets. For more information, see [Secret encryption and decryption in AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html).

Consider the following encryption best practices for this service:
+ For most cases, we recommend using the `aws/secretsmanager` AWS managed key to encrypt secrets. There is no cost for using it.
+ To be able to access a secret from another account or to apply a key policy to the encryption key, use a customer managed key to encrypt the secret.
  + In the key policy, assign the value `secretsmanager.<region>.amazonaws.com` to the [kms:ViaService](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-via-service) condition key. This limits use of the key to only requests from Secrets Manager.
  + To further limit use of the key to only requests from Secrets Manager with the correct context, use keys or values in the [Secrets Manager encryption context](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html#security-encryption-encryption-context) as a condition for using the KMS key by creating:
    + A [string condition operator](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_String) in an IAM policy or key policy
    + A [grant constraint](https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html) in a grant

## Amazon Simple Storage Service
<a name="s3"></a>

[Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

For server-side encryption in Amazon S3, there are three options:
+ [Server-side encryption with Amazon S3-managed encryption keys (SSE-S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html)
+ [Server-side encryption with AWS Key Management Service (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)
+ [Server-side encryption with customer-provided encryption keys (SSE-C)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html)

Amazon S3 applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for every bucket in Amazon S3. As of January 5, 2023, all new object uploads to Amazon S3 are automatically encrypted at no additional cost and with no impact on performance. The automatic encryption status for S3 bucket default encryption configuration and for new object uploads is available in AWS CloudTrail logs, S3 Inventory, S3 Storage Lens, the Amazon S3 console, and as an additional Amazon S3 API response header in the AWS Command Line Interface (AWS CLI) and AWS SDKs. For more information, see [Default encryption FAQ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-encryption-faq.html).

If server-side encryption is used to encrypt an object at the time of upload, add the `x-amz-server-side-encryption` header to the request to tell Amazon S3 to encrypt the object using SSE-S3, SSE-KMS, or SSE-C. The following are the possible values for the `x-amz-server-side-encryption` header:
+ `AES256`, which tells Amazon S3 to use Amazon S3 managed keys.
+ `aws:kms`, which tells Amazon S3 to use AWS KMS managed keys.
+ Setting value as `True` or `False` for SSE-C

For more information, see *Defense-in-depth requirement 1: Data must be encrypted at rest and during transit* in [How to Use Bucket Policies and Apply Defense-in-Depth to Help Secure Your Amazon S3 Data](https://aws.amazon.com/blogs/security/how-to-use-bucket-policies-and-apply-defense-in-depth-to-help-secure-your-amazon-s3-data/) (AWS blog post).

For [client-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingClientSideEncryption.html) in Amazon S3, there are two options:
+ A key stored in AWS KMS
+ A key that is stored within the application

Consider the following encryption best practices for this service:
+ In AWS Config, implement the [s3-bucket-server-side-encryption-enabled](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-server-side-encryption-enabled.html) AWS managed rule to validate and enforce S3 bucket encryption.
+ Deploy an Amazon S3 bucket policy that validates that all objects being uploaded are encrypted using the `s3:x-amz-server-side-encryption` condition. For more information, see the example bucket policy in [Protecting data using SSE-S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html) and the instructions in [Adding a bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-bucket-policy.html).
+ Allow only encrypted connections over HTTPS (TLS) by using the `aws:SecureTransport` condition on S3 bucket policies. For more information, see [What S3 bucket policy should I use to comply with the AWS Config rule s3-bucket-ssl-requests-only?](https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/)
+ In AWS Config, implement the [s3-bucket-ssl-requests-only](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-ssl-requests-only.html) AWS managed rule to require requests to use SSL.
+ Use a customer managed key when you need to grant cross-account access to Amazon S3 objects. Configure the key policy to allow access from another AWS account.

## Amazon Virtual Private Cloud
<a name="vpc"></a>

[Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you've defined. This virtual network resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

Consider the following encryption best practices for this service:
+ Encrypt traffic between information assets and systems within the corporate network and VPCs by using one of the following:
  + AWS Site-to-Site VPN connections
  + A combination of AWS Site-to-Site VPN and AWS Direct Connect connections, which provides an IPsec-encrypted private connection
  + AWS Direct Connect connections that support MAC Security (MACsec) to encrypt data from corporate networks to the AWS Direct Connect location
+ Use VPC endpoints in AWS PrivateLink to privately connect your VPCs to supported AWS services without using an internet gateway. You can use AWS Direct Connect or Site-to-Site VPN services to establish this connection. Traffic between your VPC and the other service does not leave the AWS network. For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html).
+ Configure [security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html) that allow traffic only from ports associated with secure protocols, such as HTTPS over TCP/443. Periodically audit security groups and their rules.

# Resources
<a name="resources"></a>
+ [Creating an enterprise encryption strategy for data at rest](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/welcome.html) (AWS Prescriptive Guidance)
+ [Security best practices for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html) (AWS KMS documentation)
+ [How AWS services use AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/service-integration.html) (AWS KMS documentation)
+ [Security Pillar: Data protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-protection.html) (AWS Well-Architected Framework)

# Document history
<a name="doc-history"></a>

The following table describes significant changes to this guide.


| 
| 
| **Change** | **Description** | **Date** | 
| --- |--- |--- |
| Major revision | Restructured as an encryption strategy guide covering data at rest, in transit, and in use. Replaced per-service feature sections with encryption fundamentals and transparent encryption coverage. Added hardware isolation and cryptographic computing content. | September 17, 2026 | 
| Cryptography updates | We updated the [AWS approach to cryptography](#aws-cryptography-services) chapter. | February 17, 2026 | 
| Algorithm updates | We updated the [Cryptographic algorithms](#algorithms) section. | January 23, 2026 | 
| Algorithm and encryption in transit updates | We updated the [About cryptographic algorithms](#algorithms) section and the [Encryption of data in transit](#encryption-of-data-in-transit) section. | October 28, 2025 | 
| Algorithm updates | We add information about cryptography algorithms to the [Cryptography algorithms and AWS services](#aws-cryptography-services) section. | June 18, 2025 | 
| Amazon EKS updates | We updated the encryption best practices for Amazon Elastic Kubernetes Service (Amazon EKS). | January 7, 2025 | 
| Secrets Manager updates | We updated the information and recommendations for AWS Secrets Manager. | September 9, 2024 | 
| AWS service updates | We updated the information and recommendations for Amazon EKS, AWS Encryption SDK, Amazon Relational Database Service (Amazon RDS), and Amazon Simple Storage Service (Amazon S3). | September 4, 2024 | 
| Initial publication | — | December 2, 2022 | 