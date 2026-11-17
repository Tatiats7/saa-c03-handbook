facts card: 313 facts
cloudhsm-app-not-required-same-vpc
  claim: The application need not be in the same VPC as the CloudHSM cluster, but the server running the application and HSM client must have network reachability to all HSMs, for example through VPC peering, VPN or Direct Connect.
  link: [network (IP) reachability to all HSMs](../facts/cloudhsm.md#cloudhsm-app-not-required-same-vpc)
  link: [with VPC peering, with a VPN connection](../facts/cloudhsm.md#cloudhsm-app-not-required-same-vpc)
cloudhsm-aws-cannot-operate-on-hsms
  claim: AWS cannot view or modify your HSM users or keys and cannot perform cryptographic operations with those keys; the appliance user that CloudHSM uses can perform cloning and synchronization operations on the cluster's HSMs.
  link: [cannot view or modify your users or keys](../facts/cloudhsm.md#cloudhsm-aws-cannot-operate-on-hsms)
  link: [cloning and synchronization operations](../facts/cloudhsm.md#cloudhsm-aws-cannot-operate-on-hsms)
cloudhsm-aws-cannot-recover-keys
  claim: Amazon has no access to your CloudHSM keys or credentials and has no way to recover your keys if you lose your HSM credentials.
  link: [has no way to recover your keys](../facts/cloudhsm.md#cloudhsm-aws-cannot-recover-keys)
  link: [does not have access to your keys](../facts/cloudhsm.md#cloudhsm-aws-cannot-recover-keys)
cloudhsm-aws-services-via-kms-custom-key-store
  claim: AWS services integrate with AWS KMS, which is integrated with CloudHSM through the KMS custom key store feature; to use the server-side encryption of services such as EBS, S3 or Amazon RDS with CloudHSM, you configure a custom key store in AWS KMS.
  link: [through the KMS custom key store feature](../facts/cloudhsm.md#cloudhsm-aws-services-via-kms-custom-key-store)
  link: [configuring a custom key store in AWS KMS](../facts/cloudhsm.md#cloudhsm-aws-services-via-kms-custom-key-store)
cloudhsm-backup-copy-cross-region
  claim: You can copy CloudHSM cluster backups to other Regions for cross-Region resilience, global workloads and disaster recovery; a cluster built from the copy is not linked to the original and is managed independently, and backups cannot be copied between partitions.
  link: [across Regions](../facts/cloudhsm.md#cloudhsm-backup-copy-cross-region)
  link: [are not linked](../facts/cloudhsm.md#cloudhsm-backup-copy-cross-region)
  link: [cannot be copied between AWS partitions](../facts/cloudhsm.md#cloudhsm-backup-copy-cross-region)
cloudhsm-backup-retention-default-90-days
  claim: When you create a CloudHSM cluster, the default backup retention period is 90 days, and you can set a value between 7 and 379 days.
  scope: per cluster; default; adjustable; the service never deletes a cluster's last backup.
  link: [90 days](../facts/cloudhsm.md#cloudhsm-backup-retention-default-90-days)
  link: [between 7 and 379 days](../facts/cloudhsm.md#cloudhsm-backup-retention-default-90-days)
  say: ninety days | between seven and three hundred seventy-nine days
cloudhsm-backups-encrypted-aws-cannot-decrypt
  claim: CloudHSM makes periodic backups of the cluster's users, keys and policies; the HSM encrypts all data before sending it, the data never leaves the HSM in plaintext, and AWS cannot decrypt the backups.
  link: [backups cannot be decrypted by AWS](../facts/cloudhsm.md#cloudhsm-backups-encrypted-aws-cannot-decrypt)
  link: [never leaves the HSM in plaintext form](../facts/cloudhsm.md#cloudhsm-backups-encrypted-aws-cannot-decrypt)
cloudhsm-bp-three-hsms-new-key-durability
  claim: For applications that need durability of newly generated keys, AWS recommends at least three HSMs spread across different Availability Zones, and spreading HSMs across as many AZs as possible.
  link: [at least three HSMs](../facts/cloudhsm.md#cloudhsm-bp-three-hsms-new-key-durability)
  link: [across as many Availability Zones as possible](../facts/cloudhsm.md#cloudhsm-bp-three-hsms-new-key-durability)
cloudhsm-change-hsm2m-non-fips-2024
  claim: On 2024-06-10 CloudHSM launched the hsm2m.medium HSM type and the non-FIPS cluster mode; on 2024-08-20 hsm2m.medium became available for FIPS mode clusters.
  scope: AWS CloudHSM.
  link: [2024-06-10](../facts/cloudhsm.md#cloudhsm-change-hsm2m-non-fips-2024)
  link: [2024-08-20](../facts/cloudhsm.md#cloudhsm-change-hsm2m-non-fips-2024)
  say: June tenth, twenty twenty-four | August twentieth, twenty twenty-four
cloudhsm-client-sdks-standard-apis
  claim: Customers whose public key infrastructure uses PKCS #11, Java Cryptographic Extension (JCE), Cryptography API: Next Generation (CNG) or Key Storage Provider (KSP) can migrate to CloudHSM with fewer application changes.
  link: [PKCS #11](../facts/cloudhsm.md#cloudhsm-client-sdks-standard-apis)
  link: [Java Cryptographic Extension (JCE)](../facts/cloudhsm.md#cloudhsm-client-sdks-standard-apis)
cloudhsm-cluster-keeps-hsms-in-sync
  claim: A CloudHSM cluster is a collection of HSMs that CloudHSM keeps in sync. If the keys on the HSMs fall out of synchronization, CloudHSM automatically resynchronizes them; this automatic resynchronization applies only to keys, not to users and policies.
  link: [keeps in sync](../facts/cloudhsm.md#cloudhsm-cluster-keeps-hsms-in-sync)
  link: [automatically resynchronizes them](../facts/cloudhsm.md#cloudhsm-cluster-keeps-hsms-in-sync)
cloudhsm-cluster-mode-fixed-at-creation
  claim: A CloudHSM cluster's mode (FIPS or non-FIPS) cannot be changed after the cluster is created; FIPS mode allows only FIPS validated keys and algorithms.
  scope: per cluster; non-FIPS mode is available only with hsm2m.medium.
  link: [cannot be changed after it is created](../facts/cloudhsm.md#cloudhsm-cluster-mode-fixed-at-creation)
cloudhsm-clusters-before-2024-06-10-fips-hsm1
  claim: Every CloudHSM cluster created before June 10, 2024 is in FIPS mode and uses the hsm1.medium HSM type.
  scope: clusters created before June 10, 2024.
  link: [June 10, 2024](../facts/cloudhsm.md#cloudhsm-clusters-before-2024-06-10-fips-hsm1)
  say: June tenth, twenty twenty-four
cloudhsm-consider-kms-if-no-hsm-ops
  claim: If you want a managed service for creating and controlling encryption keys but do not want to operate your own HSMs, AWS suggests AWS KMS; for payment HSMs and keys, AWS Payment Cryptography.
  link: [operate your own HSMs](../facts/cloudhsm.md#cloudhsm-consider-kms-if-no-hsm-ops)
  link: [consider using AWS Payment Cryptography](../facts/cloudhsm.md#cloudhsm-consider-kms-if-no-hsm-ops)
cloudhsm-durability-customer-between-backups
  claim: AWS takes automatic encrypted backups of a CloudHSM cluster daily and on lifecycle events; for the 24-hour period between backups you alone are responsible for the durability of key material created or imported in the cluster.
  link: [you are solely responsible for the durability](../facts/cloudhsm.md#cloudhsm-durability-customer-between-backups)
  link: [on a daily basis](../facts/cloudhsm.md#cloudhsm-durability-customer-between-backups)
cloudhsm-eni-in-your-subnet
  claim: When you create an HSM, CloudHSM puts an elastic network interface in your subnet as the interface to the HSM; the HSM itself resides in a separate VPC in an AWS account owned by CloudHSM.
  link: [an elastic network interface (ENI)](../facts/cloudhsm.md#cloudhsm-eni-in-your-subnet)
  link: [resides in a separate VPC](../facts/cloudhsm.md#cloudhsm-eni-in-your-subnet)
cloudhsm-faq-api-cannot-access-hsm-contents
  claim: The CloudHSM API manages clusters and HSMs (create, modify, delete, status) but cannot access the contents of the HSM or modify its users, policies or other settings.
  link: [cannot access the contents of the HSM](../facts/cloudhsm.md#cloudhsm-faq-api-cannot-access-hsm-contents)
cloudhsm-faq-aws-manages-firmware
  claim: You do not manage HSM firmware: AWS manages the firmware on the hardware, and only firmware signed by the FIPS key, which AWS cannot access, can be installed.
  link: [AWS manages the firmware on the hardware.](../facts/cloudhsm.md#cloudhsm-faq-aws-manages-firmware)
cloudhsm-faq-brute-force-lockout
  claim: HSMs lock out an admin or crypto officer after a fixed number of failed login attempts, and lock out a crypto user, who must then be unlocked by a CO or admin.
  link: [will lock the admin/CO out](../facts/cloudhsm.md#cloudhsm-faq-brute-force-lockout)
  link: [must be unlocked by a CO or admin](../facts/cloudhsm.md#cloudhsm-faq-brute-force-lockout)
cloudhsm-faq-client-side-services-see-ciphertext
  claim: If you do all encryption in a CloudHSM-integrated application, AWS services such as Amazon S3 and Amazon EBS see only your encrypted data.
  link: [will only see your data encrypted](../facts/cloudhsm.md#cloudhsm-faq-client-side-services-see-ciphertext)
cloudhsm-faq-client-traffic-end-to-end
  claim: All communication between the CloudHSM client and your HSM is encrypted end to end, and AWS cannot see or intercept it.
  link: [encrypted end to end](../facts/cloudhsm.md#cloudhsm-faq-client-traffic-end-to-end)
  link: [AWS cannot see or intercept this communication](../facts/cloudhsm.md#cloudhsm-faq-client-traffic-end-to-end)
cloudhsm-faq-cloudtrail-api-calls
  claim: AWS CloudTrail records the AWS API calls made for CloudHSM in your account.
  link: [AWS CloudTrail records AWS API calls](../facts/cloudhsm.md#cloudhsm-faq-cloudtrail-api-calls)
cloudhsm-faq-cloudwatch-metrics
  claim: CloudHSM publishes CloudWatch metrics for clusters and individual HSMs, which you can read and alarm on.
  link: [multiple Amazon CloudWatch metrics](../facts/cloudhsm.md#cloudhsm-faq-cloudwatch-metrics)
cloudhsm-faq-cluster-multi-az-synchronized
  claim: A CloudHSM cluster can contain multiple HSMs spread across multiple Availability Zones in a Region, and the HSMs in a cluster are automatically synchronized and load-balanced.
  link: [spread across multiple Availability Zones](../facts/cloudhsm.md#cloudhsm-faq-cluster-multi-az-synchronized)
  link: [automatically synchronized and load-balanced](../facts/cloudhsm.md#cloudhsm-faq-cluster-multi-az-synchronized)
cloudhsm-faq-daily-encrypted-backups
  claim: AWS takes automatic encrypted backups of your CloudHSM cluster on a daily basis.
  link: [on a daily basis](../facts/cloudhsm.md#cloudhsm-faq-daily-encrypted-backups)
  link: [automatic encrypted backups](../facts/cloudhsm.md#cloudhsm-faq-daily-encrypted-backups)
cloudhsm-faq-dedicated-hsms-compliance
  claim: AWS CloudHSM helps meet corporate, contractual and regulatory compliance requirements by using dedicated HSM instances in the AWS Cloud, so that keys are accessible only by you.
  link: [dedicated Hardware Security Module (HSM) instances](../facts/cloudhsm.md#cloudhsm-faq-dedicated-hsms-compliance)
  link: [accessible only by you](../facts/cloudhsm.md#cloudhsm-faq-dedicated-hsms-compliance)
cloudhsm-faq-export-wrapped-unless-non-exportable
  claim: Besides the daily AWS backups, keys can be exported (wrapped) out of a CloudHSM cluster and stored on premises, as long as they were not generated as non-exportable.
  link: [exported (“wrapped”) out of your cluster](../facts/cloudhsm.md#cloudhsm-faq-export-wrapped-unless-non-exportable)
cloudhsm-faq-failed-hsm-auto-replaced
  claim: If an HSM fails or loses network connectivity, it is replaced automatically.
  link: [the HSM will be automatically replaced](../facts/cloudhsm.md#cloudhsm-faq-failed-hsm-auto-replaced)
cloudhsm-faq-fee-not-usage-based
  claim: The CloudHSM hourly fee varies by Region and does not depend on how much you use the HSM, or on how many users or keys you create.
  link: [does not depend on how much you use](../facts/cloudhsm.md#cloudhsm-faq-fee-not-usage-based)
cloudhsm-faq-fips-l3-required-use-cases
  claim: FIPS 140-2 Level 3 is a requirement of certain use cases, including document signing, payments, and operating as a public Certificate Authority for SSL certificates.
  link: [document signing, payments](../facts/cloudhsm.md#cloudhsm-faq-fips-l3-required-use-cases)
  link: [public Certificate Authority](../facts/cloudhsm.md#cloudhsm-faq-fips-l3-required-use-cases)
cloudhsm-faq-ha-automatic-two-azs
  claim: High availability is automatic when a cluster has at least two HSMs across two Availability Zones; a failed HSM is replaced automatically and clients are updated without interrupting processing.
  link: [at least two HSMs](../facts/cloudhsm.md#cloudhsm-faq-ha-automatic-two-azs)
  link: [replaced automatically](../facts/cloudhsm.md#cloudhsm-faq-ha-automatic-two-azs)
cloudhsm-faq-has-sla
  claim: AWS CloudHSM has a service level agreement (SLA).
  link: [service level agreement (SLA)](../facts/cloudhsm.md#cloudhsm-faq-has-sla)
cloudhsm-faq-hsm-is-network-resource-in-vpc
  claim: You get dedicated, single-tenant access to each HSM in your cluster, and each HSM appears as a network resource in your VPC.
  link: [single-tenant access to each HSM](../facts/cloudhsm.md#cloudhsm-faq-hsm-is-network-resource-in-vpc)
  link: [appears as a network resource](../facts/cloudhsm.md#cloudhsm-faq-hsm-is-network-resource-in-vpc)
cloudhsm-faq-no-aws-personnel-access
  claim: AWS CloudHSM monitors the health of your HSMs automatically, but no AWS personnel have access to your keys or data.
  link: [no AWS personnel have access](../facts/cloudhsm.md#cloudhsm-faq-no-aws-personnel-access)
cloudhsm-faq-no-free-tier
  claim: There is no free tier for AWS CloudHSM.
  link: [no free tier](../facts/cloudhsm.md#cloudhsm-faq-no-free-tier)
cloudhsm-faq-no-reserved-pricing
  claim: AWS does not offer reserved instance pricing for AWS CloudHSM.
  link: [we do not offer reserved instance pricing](../facts/cloudhsm.md#cloudhsm-faq-no-reserved-pricing)
cloudhsm-faq-no-scheduled-maintenance
  claim: CloudHSM has no scheduled maintenance windows, but AWS may need maintenance for upgrades or faulty hardware; you are responsible for architecting the cluster for high availability.
  link: [may need to conduct maintenance](../facts/cloudhsm.md#cloudhsm-faq-no-scheduled-maintenance)
  link: [your responsibility to architect your cluster](../facts/cloudhsm.md#cloudhsm-faq-no-scheduled-maintenance)
cloudhsm-faq-on-prem-hsm-key-wrap
  claim: CloudHSM does not interoperate directly with on-premises HSMs, but you can transfer exportable keys between CloudHSM and most commercial HSMs with supported RSA key wrap methods.
  link: [does not interoperate directly with on-premises HSMs](../facts/cloudhsm.md#cloudhsm-faq-on-prem-hsm-key-wrap)
  link: [supported RSA key wrap methods](../facts/cloudhsm.md#cloudhsm-faq-on-prem-hsm-key-wrap)
cloudhsm-faq-payment-cryptography-not-cloudhsm
  claim: CloudHSM provides general-purpose HSMs; for PIN block translation and other debit payment cryptography, AWS Payment Cryptography provides cryptography operations for cloud-hosted payment applications.
  link: [general-purpose HSMs](../facts/cloudhsm.md#cloudhsm-faq-payment-cryptography-not-cloudhsm)
  link: [AWS Payment Cryptography](../facts/cloudhsm.md#cloudhsm-faq-payment-cryptography-not-cloudhsm)
cloudhsm-faq-production-two-hsms-mission-critical-three
  claim: AWS strongly recommends at least two HSMs in two different Availability Zones for any production workload, and at least three HSMs in at least two AZs for mission-critical workloads.
  link: [at least two HSMs](../facts/cloudhsm.md#cloudhsm-faq-production-two-hsms-mission-critical-three)
  link: [For mission-critical workloads](../facts/cloudhsm.md#cloudhsm-faq-production-two-hsms-mission-critical-three)
cloudhsm-faq-requires-vpc
  claim: AWS CloudHSM must be provisioned inside an Amazon VPC, to protect and isolate your cluster from other customers; you cannot use it without a VPC.
  link: [must be provisioned inside an Amazon VPC](../facts/cloudhsm.md#cloudhsm-faq-requires-vpc)
cloudhsm-faq-rotation-strategy-yours
  claim: In CloudHSM, key rotation depends on your type of application and is a process you run, for example by creating a new key; for envelope encryption without an existing rotation tool and process, you need to create one.
  link: [depend on your type of application](../facts/cloudhsm.md#cloudhsm-faq-rotation-strategy-yours)
  link: [you will need to create one](../facts/cloudhsm.md#cloudhsm-faq-rotation-strategy-yours)
cloudhsm-faq-standard-apis
  claim: Custom applications can use the standard APIs that CloudHSM supports: PKCS#11, Java JCE, OpenSSL Dynamic Engine and Microsoft KSP/CNG.
  link: [PKCS#11](../facts/cloudhsm.md#cloudhsm-faq-standard-apis)
  link: [Java JCE](../facts/cloudhsm.md#cloudhsm-faq-standard-apis)
  link: [OpenSSL Dynamic Engine](../facts/cloudhsm.md#cloudhsm-faq-standard-apis)
  link: [Microsoft KSP/CNG](../facts/cloudhsm.md#cloudhsm-faq-standard-apis)
cloudhsm-faq-sync-keys-two-azs-durability
  claim: Between daily backups you are responsible for key durability, and AWS strongly recommends synchronizing keys to at least two HSMs in two different Availability Zones.
  link: [synchronized to at least two HSMs](../facts/cloudhsm.md#cloudhsm-faq-sync-keys-two-azs-durability)
cloudhsm-faq-tamper-zeroization
  claim: CloudHSM has physical and logical tamper detection and response mechanisms that trigger key deletion (zeroization) of the hardware.
  link: [key deletion (zeroization)](../facts/cloudhsm.md#cloudhsm-faq-tamper-zeroization)
cloudhsm-faq-tested-oracle-apache-nginx
  claim: AWS has tested CloudHSM with third-party software such as Oracle Database 19c, Apache and Nginx web servers for SSL offload, and Windows Server as a CA.
  link: [SSL offload](../facts/cloudhsm.md#cloudhsm-faq-tested-oracle-apache-nginx)
  link: [configuring a Windows Server as a CA](../facts/cloudhsm.md#cloudhsm-faq-tested-oracle-apache-nginx)
cloudhsm-ha-two-hsms-different-azs
  claim: HSMs in different Availability Zones give automatic high availability, and AWS recommends a minimum of two HSMs in each cluster, each in a different Availability Zone of the Region; a cluster with more than one HSM is load balanced automatically.
  link: [a minimum of two HSMs in each cluster](../facts/cloudhsm.md#cloudhsm-ha-two-hsms-different-azs)
  link: [you automatically get high availability](../facts/cloudhsm.md#cloudhsm-ha-two-hsms-different-azs)
cloudhsm-hsm-users-not-iam
  claim: Access to resources inside a CloudHSM cluster uses HSM users directly on the HSMs, not IAM users or IAM policies. IAM users with the correct credentials can create HSMs through the AWS API; after an HSM is created, operations on it are authenticated with HSM user credentials.
  link: [you use HSM users directly on HSMs](../facts/cloudhsm.md#cloudhsm-hsm-users-not-iam)
  link: [IAM users or IAM policies](../facts/cloudhsm.md#cloudhsm-hsm-users-not-iam)
cloudhsm-hsm1-end-of-support-2026
  claim: The CloudHSM hsm1.medium instance type reaches end of support on March 31st, 2026. Starting April 2025 you cannot create new hsm1.medium clusters, and starting January 2026 AWS begins to migrate existing hsm1.medium clusters automatically to the hsm2m.medium instance type.
  scope: hsm1.medium clusters.
  link: [March 31st, 2026](../facts/cloudhsm.md#cloudhsm-hsm1-end-of-support-2026)
  link: [Starting April 2025](../facts/cloudhsm.md#cloudhsm-hsm1-end-of-support-2026)
  say: March thirty-first, twenty twenty-six
cloudhsm-hsm2m-fips-140-3-level-3
  claim: CloudHSM offers hsm2m.medium HSMs that are single-tenant and FIPS 140-3 Level 3 certified, with a non-FIPS mode option for use cases outside FIPS 140-3 restrictions.
  scope: hsm2m.medium HSMs.
  link: [FIPS 140-3 Level 3](../facts/cloudhsm.md#cloudhsm-hsm2m-fips-140-3-level-3)
  say: FIPS one-forty-three, Level three
cloudhsm-logging-cloudtrail-vs-cloudwatch
  claim: CloudTrail captures all AWS CloudHSM API calls, but it does not include HSM device or access logs; CloudHSM sends HSM audit logs to CloudWatch Logs on your behalf.
  link: [HSM device or access logs](../facts/cloudhsm.md#cloudhsm-logging-cloudtrail-vs-cloudwatch)
  link: [sends them to Amazon CloudWatch Logs](../facts/cloudhsm.md#cloudhsm-logging-cloudtrail-vs-cloudwatch)
cloudhsm-max-keys-per-cluster
  claim: A CloudHSM cluster holds at most 3,300 keys with hsm1.medium, and at most 16,666 keys in total with hsm2m.medium, of which at most 3,333 can be asymmetric; the quota is not adjustable.
  scope: per cluster; maximum; not adjustable; value depends on the HSM type.
  link: [3,300](../facts/cloudhsm.md#cloudhsm-max-keys-per-cluster)
  link: [16,666](../facts/cloudhsm.md#cloudhsm-max-keys-per-cluster)
  link: [3,333](../facts/cloudhsm.md#cloudhsm-max-keys-per-cluster)
  say: three thousand three hundred | sixteen thousand six hundred sixty-six | three thousand three hundred thirty-three
cloudhsm-max-users-per-cluster
  claim: A CloudHSM cluster has at most 250 users with hsm1.medium and 1,024 users with hsm2m.medium.
  scope: per cluster; maximum; not adjustable; value depends on the HSM type.
  link: [250](../facts/cloudhsm.md#cloudhsm-max-users-per-cluster)
  link: [1,024](../facts/cloudhsm.md#cloudhsm-max-users-per-cluster)
  say: two hundred fifty | one thousand twenty-four
cloudhsm-more-responsibility-than-managed
  claim: Because the CloudHSM data plane is end-to-end encrypted and not visible to AWS, you control your own user management, and the trade-off is more responsibility than with a managed AWS service.
  link: [you have more responsibility](../facts/cloudhsm.md#cloudhsm-more-responsibility-than-managed)
  link: [not visible to AWS](../facts/cloudhsm.md#cloudhsm-more-responsibility-than-managed)
cloudhsm-price-hourly-per-hsm-no-upfront
  claim: CloudHSM has no upfront costs: you pay an hourly fee for each HSM from launch until you terminate it.
  scope: per HSM.
  link: [an hourly fee for each HSM](../facts/cloudhsm.md#cloudhsm-price-hourly-per-hsm-no-upfront)
cloudhsm-pricing-hourly-per-hsm
  claim: CloudHSM charges an hourly fee for each hour or partial hour an HSM is provisioned to a cluster; a cluster with no HSMs is not billed, automatic storage of encrypted backups is not billed, and network data transfer is charged separately.
  link: [an hourly fee](../facts/cloudhsm.md#cloudhsm-pricing-hourly-per-hsm)
  link: [A cluster with no HSMs](../facts/cloudhsm.md#cloudhsm-pricing-hourly-per-hsm)
cloudhsm-quota-clusters-per-region
  claim: An account can have 4 CloudHSM clusters per Region by default, and the quota is adjustable.
  scope: per AWS account and Region; default; adjustable.
  link: [4](../facts/cloudhsm.md#cloudhsm-quota-clusters-per-region)
  say: four
cloudhsm-quota-hsms-per-cluster
  claim: A CloudHSM cluster can hold 28 HSMs, and this quota is not adjustable.
  scope: per cluster; maximum; not adjustable.
  link: [28](../facts/cloudhsm.md#cloudhsm-quota-hsms-per-cluster)
  say: twenty-eight
cloudhsm-quota-hsms-per-region
  claim: An account can have 6 HSMs per Region by default, and the quota is adjustable.
  scope: per AWS account and Region; default; adjustable.
  link: [6](../facts/cloudhsm.md#cloudhsm-quota-hsms-per-region)
  say: six
cloudhsm-rds-oracle-tde-via-kms
  claim: CloudHSM does not directly support Amazon RDS Oracle TDE; use AWS KMS with a custom key store to protect RDS data with keys generated and stored in your CloudHSM cluster.
  link: [Not directly.](../facts/cloudhsm.md#cloudhsm-rds-oracle-tde-via-kms)
  link: [Custom Key Store](../facts/cloudhsm.md#cloudhsm-rds-oracle-tde-via-kms)
cloudhsm-single-hsm-can-lose-keys
  claim: A CloudHSM cluster with a single HSM can lose keys created since the most recent daily backup if the HSM fails; clusters with two or more HSMs, ideally in separate AZs, do not lose keys when a single HSM fails.
  link: [possible to lose keys](../facts/cloudhsm.md#cloudhsm-single-hsm-can-lose-keys)
  link: [will not lose keys](../facts/cloudhsm.md#cloudhsm-single-hsm-can-lose-keys)
cloudhsm-single-tenant-access
  claim: With CloudHSM you receive single-tenant access to each HSM: underlying hardware may be shared with other customers, but the HSM is accessible only to you.
  link: [single-tenant access to the HSM](../facts/cloudhsm.md#cloudhsm-single-tenant-access)
  link: [accessible only to you](../facts/cloudhsm.md#cloudhsm-single-tenant-access)
cloudhsm-system-quotas-not-adjustable
  claim: The CloudHSM system quotas (keys, users, connections per cluster and similar) cannot be adjusted.
  scope: per cluster.
  link: [are not adjustable](../facts/cloudhsm.md#cloudhsm-system-quotas-not-adjustable)
cloudhsm-use-cases
  claim: Named CloudHSM use cases include offloading SSL/TLS processing for web servers, storing the TDE master encryption key for transparent data encryption, and storing the private keys of an issuing certificate authority for signing.
  link: [offloading some of this](../facts/cloudhsm.md#cloudhsm-use-cases)
  link: [storing the TDE master encryption key](../facts/cloudhsm.md#cloudhsm-use-cases)
cloudhsm-user-types-admin-cu
  claim: In CloudHSM CLI, the admin HSM user can perform user management operations, such as creating and deleting users and changing user passwords; a crypto user (CU) can create, delete, share, import, and export cryptographic keys and use them for encryption, decryption, signing and verifying.
  scope: HSM user types for CloudHSM CLI.
  link: [user management operations](../facts/cloudhsm.md#cloudhsm-user-types-admin-cu)
  link: [Create, delete, share, import, and export](../facts/cloudhsm.md#cloudhsm-user-types-admin-cu)
cloudhsm-users-not-auto-synced
  claim: Unlike keys, HSM users and policies are not automatically resynchronized across the cluster; the CloudHSM CLI makes a best-effort synchronization and you may need to resolve inconsistencies manually.
  link: [applies only to keys](../facts/cloudhsm.md#cloudhsm-users-not-auto-synced)
  link: [are not automatically resynchronized](../facts/cloudhsm.md#cloudhsm-users-not-auto-synced)
cloudhsm-vs-kms-faq-single-tenant-vpc-exclusive
  claim: Compared with AWS KMS, CloudHSM gives you a validated single-tenant HSM cluster in your VPC with exclusive control over key use through an authentication mechanism independent from AWS, and cryptographic functions through PKCS#11, Java JCE or Microsoft CNG interfaces.
  link: [single-tenant HSM cluster](../facts/cloudhsm.md#cloudhsm-vs-kms-faq-single-tenant-vpc-exclusive)
  link: [exclusive control over how your keys are used](../facts/cloudhsm.md#cloudhsm-vs-kms-faq-single-tenant-vpc-exclusive)
  link: [PKCS#11, Java JCE, or Microsoft CNG](../facts/cloudhsm.md#cloudhsm-vs-kms-faq-single-tenant-vpc-exclusive)
cloudhsm-what-it-is-hsm
  claim: A hardware security module (HSM) is a computing device that processes cryptographic operations and provides secure storage for cryptographic keys; AWS CloudHSM provides such HSMs in the AWS Cloud.
  link: [processes cryptographic operations](../facts/cloudhsm.md#cloudhsm-what-it-is-hsm)
  link: [secure storage for cryptographic keys](../facts/cloudhsm.md#cloudhsm-what-it-is-hsm)
kms-account-principal-delegates-to-iam
  claim: When the principal in a key policy statement is the account principal, the statement gives no IAM principal permission itself; it lets the account delegate the permissions with IAM policies.
  link: [doesn't give any IAM principal permission](../facts/kms.md#kms-account-principal-delegates-to-iam)
  link: [use IAM policies to delegate the permissions](../facts/kms.md#kms-account-principal-delegates-to-iam)
kms-asymmetric-for-outside-aws-users
  claim: Asymmetric KMS keys suit encryption outside AWS by users who cannot call AWS KMS; for data stored or managed in an AWS service, use a symmetric encryption KMS key.
  link: [users who cannot call AWS KMS](../facts/kms.md#kms-asymmetric-for-outside-aws-users)
  link: [use a symmetric encryption KMS key](../facts/kms.md#kms-asymmetric-for-outside-aws-users)
kms-asymmetric-private-key-stays-public-downloadable
  claim: The private key of an asymmetric KMS key is created in KMS and never leaves it unencrypted; you can download the public key and use it outside AWS KMS.
  link: [never leaves AWS KMS unencrypted](../facts/kms.md#kms-asymmetric-private-key-stays-public-downloadable)
  link: [download the public key](../facts/kms.md#kms-asymmetric-private-key-stays-public-downloadable)
kms-aws-managed-key-alias-prefix-reserved
  claim: AWS managed keys have aliases in the format aws/<service-name>, such as aws/redshift; the aws/ prefix is reserved for AWS managed keys and you cannot create an alias with it.
  link: [reserved for AWS managed keys](../facts/kms.md#kms-aws-managed-key-alias-prefix-reserved)
  link: [You cannot create an alias with this prefix](../facts/kms.md#kms-aws-managed-key-alias-prefix-reserved)
kms-aws-managed-key-cannot-change
  claim: You can view AWS managed keys, their key policies and their use in CloudTrail, but you cannot change their properties, rotate them, change their key policies or schedule them for deletion, and you cannot use them directly in cryptographic operations.
  link: [cannot change any properties of AWS managed keys](../facts/kms.md#kms-aws-managed-key-cannot-change)
  link: [audit their use in AWS CloudTrail logs](../facts/kms.md#kms-aws-managed-key-cannot-change)
  link: [cannot use AWS managed keys](../facts/kms.md#kms-aws-managed-key-cannot-change)
kms-aws-managed-key-created-by-service
  claim: AWS managed keys are KMS keys in your account that an integrated AWS service creates, manages and uses on your behalf.
  link: [created, managed, and used on your behalf](../facts/kms.md#kms-aws-managed-key-created-by-service)
  link: [AWS managed keys](../facts/kms.md#kms-aws-managed-key-created-by-service)
kms-aws-managed-keys-legacy-since-2021
  claim: AWS managed keys are a legacy key type: since 2021 they are no longer created for new AWS services, which use AWS owned keys to encrypt customer data by default.
  scope: AWS managed keys.
  link: [a legacy key type](../facts/kms.md#kms-aws-managed-keys-legacy-since-2021)
  link: [2021](../facts/kms.md#kms-aws-managed-keys-legacy-since-2021)
  say: twenty twenty-one
kms-aws-managed-keys-rotate-every-year
  claim: AWS KMS rotates AWS managed keys automatically every year (approximately 365 days), and you cannot enable or disable their rotation. Before May 2022 they rotated every three years (approximately 1,095 days).
  scope: per AWS managed key; fixed.
  link: [every year (approximately 365 days)](../facts/kms.md#kms-aws-managed-keys-rotate-every-year)
  link: [every three years (approximately 1,095 days)](../facts/kms.md#kms-aws-managed-keys-rotate-every-year)
  say: every year | every three years
  changed: 2022-05: was every three years (approximately 1,095 days)
kms-aws-owned-key-good-choice-unless-audit
  claim: Unless you are required to audit or control the key that protects your resources, an AWS owned key is a good choice: it has no fees, does not count against KMS quotas and needs no key policy.
  link: [required to audit or control the encryption key](../facts/kms.md#kms-aws-owned-key-good-choice-unless-audit)
  link: [completely free of charge](../facts/kms.md#kms-aws-owned-key-good-choice-unless-audit)
kms-aws-owned-keys-not-in-account
  claim: AWS owned keys are KMS keys that an AWS service owns and manages for use in multiple accounts; they are not in your account, yet the service can use them to protect resources in your account.
  link: [not in your AWS account](../facts/kms.md#kms-aws-owned-keys-not-in-account)
  link: [an AWS service owns and manages](../facts/kms.md#kms-aws-owned-keys-not-in-account)
kms-aws-transparent-encryption-at-rest-standard
  claim: AWS has adopted transparent encryption of data at rest as the standard security posture across its services, protecting data at rest without explicit configuration.
  link: [the standard security posture](../facts/kms.md#kms-aws-transparent-encryption-at-rest-standard)
  link: [without requiring explicit configuration](../facts/kms.md#kms-aws-transparent-encryption-at-rest-standard)
kms-case-kaia-health
  claim: Kaia Health, a German digital health company, uses AWS KMS to encrypt its data to help comply with data protection regulations in various countries; it says DiGA certification requires it to be in control of its data.
  link: [encrypt its data to help comply](../facts/kms.md#kms-case-kaia-health)
  link: [we’re in control of our data](../facts/kms.md#kms-case-kaia-health)
kms-change-dual-stack-2025-06
  claim: On 2025-06-18 KMS added dual-stack support.
  scope: AWS KMS endpoints.
  link: [2025-06-18](../facts/kms.md#kms-change-dual-stack-2025-06)
  say: June eighteenth, twenty twenty-five
kms-change-ecdh-key-agreement-2024-06
  claim: On 2024-06-13 KMS added the KeyUsage type KEY_AGREEMENT for NIST-recommended elliptic curve (ECC) KMS keys and for SM2 KMS keys (China Regions only), and added support to derive shared secrets (DeriveSharedSecret).
  scope: NIST-recommended ECC KMS keys; SM2 KMS keys in the China Regions only.
  link: [2024-06-13](../facts/kms.md#kms-change-ecdh-key-agreement-2024-06)
  say: June thirteenth, twenty twenty-four
kms-change-eddsa-key-spec-2025-11
  claim: On 2025-11-07 AWS KMS added support for the new KeySpec ECC_NIST_EDWARDS25519.
  scope: asymmetric ECC KMS keys.
  link: [2025-11-07](../facts/kms.md#kms-change-eddsa-key-spec-2025-11)
  say: November seventh, twenty twenty-five
kms-change-external-key-store-2022-11
  claim: On 2022-11-29 KMS added external key stores, which protect AWS resources with cryptographic keys kept outside of AWS.
  scope: AWS KMS.
  link: [2022-11-29](../facts/kms.md#kms-change-external-key-store-2022-11)
  say: November twenty-ninth, twenty twenty-two
kms-change-hsm-fips-140-2-level-3-2023-05
  claim: AWS KMS HSMs were certified under FIPS 140-2 overall Security Level 2 continuously since 2017. Today all AWS KMS keys are protected by HSMs validated under FIPS 140-3 Security Level 3; FIPS 140-3 does not apply to AWS KMS in the China (Beijing) and China (Ningxia) Regions.
  scope: AWS KMS HSMs outside the China (Beijing) and China (Ningxia) Regions.
  link: [FIPS 140-2 overall Security Level 2](../facts/kms.md#kms-change-hsm-fips-140-2-level-3-2023-05)
  link: [FIPS 140-3 Security Level 3](../facts/kms.md#kms-change-hsm-fips-140-2-level-3-2023-05)
  changed: 2023-05-24: was FIPS 140-2 overall Security Level 2
kms-change-import-all-key-types-2023-06
  claim: On 2023-06-05 KMS added support for importing key material into all types of KMS keys except keys in custom key stores, so asymmetric and HMAC keys can also use imported key material.
  scope: KMS keys outside custom key stores.
  link: [2023-06-05](../facts/kms.md#kms-change-import-all-key-types-2023-06)
  say: June fifth, twenty twenty-three
kms-change-imported-key-on-demand-rotation-2025-06
  claim: On 2025-06-05 KMS added on-demand rotation of symmetric encryption KMS keys with imported key material (EXTERNAL origin), and on 2025-11-26 extended it to multi-Region keys with imported key material.
  scope: symmetric encryption KMS keys with imported key material.
  link: [2025-06-05](../facts/kms.md#kms-change-imported-key-on-demand-rotation-2025-06)
  link: [2025-11-26](../facts/kms.md#kms-change-imported-key-on-demand-rotation-2025-06)
  say: June fifth, twenty twenty-five | November twenty-sixth, twenty twenty-five
kms-change-keys-quota-100000-2022-07
  claim: On 2022-07-08 KMS increased the KMS keys resource quota to 100,000 KMS keys in each account and Region.
  scope: per account and Region.
  link: [2022-07-08](../facts/kms.md#kms-change-keys-quota-100000-2022-07)
  link: [100,000](../facts/kms.md#kms-change-keys-quota-100000-2022-07)
  say: July eighth, twenty twenty-two | one hundred thousand
kms-change-last-usage-tracking-2026-04
  claim: On 2026-04-27 KMS started to show the last cryptographic operation performed with each KMS key (timestamp, operation type and CloudTrail event ID), so you no longer need to query logs by hand, and added the kms:TrailingDaysWithoutKeyUsage condition key.
  scope: all KMS keys, all Regions where KMS is available; GA before 2026-07-15, so examinable by the book's rule.
  link: [2026-04-27](../facts/kms.md#kms-change-last-usage-tracking-2026-04)
  say: April twenty-seventh, twenty twenty-six
kms-change-ml-dsa-signatures-2025-06
  claim: On 2025-06-13 KMS added ML-DSA post-quantum digital signatures.
  scope: asymmetric signing KMS keys.
  link: [2025-06-13](../facts/kms.md#kms-change-ml-dsa-signatures-2025-06)
  say: June thirteenth, twenty twenty-five
kms-change-request-quotas-raised-2024-07
  claim: On 2024-07-08 KMS increased the default request quotas for cryptographic operations with symmetric encryption, RSA, and ECC and SM2 KMS keys.
  scope: per account and Region.
  link: [2024-07-08](../facts/kms.md#kms-change-request-quotas-raised-2024-07)
  say: July eighth, twenty twenty-four
kms-change-rotation-flexible-2024-04
  claim: On 2024-04-12 KMS added support for custom rotation periods for automatic key rotations, on-demand key rotations, and visibility into your key material rotations.
  scope: KMS key rotation.
  link: [2024-04-12](../facts/kms.md#kms-change-rotation-flexible-2024-04)
  link: [custom rotation periods](../facts/kms.md#kms-change-rotation-flexible-2024-04)
  say: April twelfth, twenty twenty-four
kms-change-rotation-pricing-cap-2024-04
  claim: On 2024-04-12, in the same announcement as custom rotation periods and on-demand rotation, KMS changed rotation pricing: previously each rotation of a KMS key added $1/month per rotation; now only the first and second rotation add $1/month, and rotations after the second are not billed.
  scope: per KMS key.
  link: [2024-04-12](../facts/kms.md#kms-change-rotation-pricing-cap-2024-04)
  link: [$1/month per rotation](../facts/kms.md#kms-change-rotation-pricing-cap-2024-04)
  say: April twelfth, twenty twenty-four
  changed: 2024-04-12: was each rotation of a KMS key added $1/month per rotation
kms-change-service-principal-grants-2026-03
  claim: On 2026-03-06 KMS added grants for AWS service principals (GranteeServicePrincipal and RetiringServicePrincipal in CreateGrant) and the SourceArn grant constraint.
  scope: KMS grants.
  link: [2026-03-06](../facts/kms.md#kms-change-service-principal-grants-2026-03)
  say: March sixth, twenty twenty-six
kms-client-vs-server-side-encryption
  claim: Server-side encryption is done by the service that receives the data; with client-side encryption, data is encrypted locally before the service receives it and the service plays no role in encrypting or decrypting it.
  link: [encrypting data locally](../facts/kms.md#kms-client-vs-server-side-encryption)
  link: [does not play a role in encrypting](../facts/kms.md#kms-client-vs-server-side-encryption)
kms-cloudhsm-key-store-low-tps
  claim: A CloudHSM key store provides single-tenant HSM instances you own and manage, and it gives low TPS, with availability, durability and performance dependent on your CloudHSM cluster.
  link: [provides low TPS](../facts/kms.md#kms-cloudhsm-key-store-low-tps)
  link: [dependent on your AWS CloudHSM cluster](../facts/kms.md#kms-cloudhsm-key-store-low-tps)
kms-cloudhsm-key-store-ops-in-cluster
  claim: In a CloudHSM key store, the key material never leaves your HSMs unencrypted, and cryptographic operations are performed in the HSMs of the cluster.
  link: [never leaves your HSMs unencrypted](../facts/kms.md#kms-cloudhsm-key-store-ops-in-cluster)
  link: [performed in the HSMs in the cluster](../facts/kms.md#kms-cloudhsm-key-store-ops-in-cluster)
kms-cloudhsm-key-store-same-api-cloudtrail
  claim: Requests to use a KMS key in a CloudHSM-backed custom key store go through the AWS KMS API in the same way, with the same authentication and authorization, and are logged to CloudTrail in the same way; only the cryptographic operations happen in the custom key store.
  link: [handled in the same way](../facts/kms.md#kms-cloudhsm-key-store-same-api-cloudtrail)
  link: [logged to CloudTrail in the same way](../facts/kms.md#kms-cloudhsm-key-store-same-api-cloudtrail)
kms-cloudhsm-key-store-two-hsms-two-azs
  claim: An AWS CloudHSM key store needs an active CloudHSM cluster with at least two active HSMs in different Availability Zones.
  link: [at least two active HSMs](../facts/kms.md#kms-cloudhsm-key-store-two-hsms-two-azs)
  link: [in different Availability Zones](../facts/kms.md#kms-cloudhsm-key-store-two-hsms-two-azs)
kms-cloudtrail-logs-all-calls
  claim: CloudTrail captures all API calls to AWS KMS as events, including calls by users, roles and other AWS services; by default all KMS actions are logged, although you can exclude KMS events from a trail.
  link: [records all calls to AWS KMS](../facts/kms.md#kms-cloudtrail-logs-all-calls)
  link: [you can exclude AWS KMS actions](../facts/kms.md#kms-cloudtrail-logs-all-calls)
kms-condition-caller-account
  claim: The kms:CallerAccount condition key allows or denies access to all identities (users and roles) in an AWS account, used with a Principal element that specifies all AWS identities.
  link: [all identities (users and roles)](../facts/kms.md#kms-condition-caller-account)
  link: [kms:CallerAccount](../facts/kms.md#kms-condition-caller-account)
kms-condition-encryption-context
  claim: The kms:EncryptionContext:context-key condition key can require a particular encryption context when controlling access to a symmetric encryption KMS key.
  link: [require a particular encryption context](../facts/kms.md#kms-condition-encryption-context)
  link: [kms:EncryptionContext:context-key](../facts/kms.md#kms-condition-encryption-context)
kms-condition-viaservice
  claim: The kms:ViaService condition key limits use of a KMS key to requests from specified AWS services.
  link: [requests from specified AWS services](../facts/kms.md#kms-condition-viaservice)
  link: [kms:ViaService](../facts/kms.md#kms-condition-viaservice)
kms-cost-s3-bucket-keys-99
  claim: The KMS best-practice guide says S3 Bucket Keys can reduce the cost of high-volume KMS requests from S3 by up to 99%, and recommends them instead of disabling encryption to save cost.
  link: [up to 99%](../facts/kms.md#kms-cost-s3-bucket-keys-99)
  link: [a recommended alternative to disabling encryption](../facts/kms.md#kms-cost-s3-bucket-keys-99)
kms-createkey-default-keyspec-symmetric
  claim: The default value of the KeySpec parameter in a CreateKey request is SYMMETRIC_DEFAULT; a request with no KeySpec parameter uses it.
  scope: CreateKey KeySpec parameter; default; adjustable; when the CreateKey request has no KeySpec parameter.
  link: [SYMMETRIC_DEFAULT, which is the default value](../facts/kms.md#kms-createkey-default-keyspec-symmetric)
kms-cross-account-key-policy-and-iam-policy
  claim: Cross-account use of a KMS key requires permission in the key policy of the key and in an IAM policy in the external user's account.
  link: [permission in the key policy](../facts/kms.md#kms-cross-account-key-policy-and-iam-policy)
  link: [an IAM policy in the external user's account](../facts/kms.md#kms-cross-account-key-policy-and-iam-policy)
kms-cross-account-only-some-operations
  claim: Cross-account permission on a KMS key is effective only for cryptographic operations and a few key operations such as CreateGrant and DescribeKey; permissions for other operations, such as ScheduleKeyDeletion, have no effect for another account.
  link: [effective only for the following operations](../facts/kms.md#kms-cross-account-only-some-operations)
  link: [those permissions have no effect](../facts/kms.md#kms-cross-account-only-some-operations)
kms-cross-account-requests-throttle-caller
  claim: For a cross-account request, KMS counts the request against the quota of the account that makes the request, not the account that owns the KMS key.
  scope: per calling account and Region.
  link: [throttles the account that makes the requests](../facts/kms.md#kms-cross-account-requests-throttle-caller)
kms-cross-region-snapshot-copy-destination-key
  claim: To copy an encrypted RDS snapshot to another Region you must specify a KMS key in the destination Region, because KMS keys are specific to the Region where they are created.
  link: [the KMS key in the destination AWS Region](../facts/kms.md#kms-cross-region-snapshot-copy-destination-key)
  link: [specific to the AWS Region](../facts/kms.md#kms-cross-region-snapshot-copy-destination-key)
kms-custom-key-store-cost-two-hsms
  claim: KMS prices are unaffected by the use of a custom key store. For a custom key store backed by CloudHSM, the CloudHSM cluster must contain at least two HSMs, charged at the standard AWS CloudHSM prices.
  scope: custom key stores backed by AWS CloudHSM.
  link: [at least two HSMs](../facts/kms.md#kms-custom-key-store-cost-two-hsms)
  link: [charged at the standard AWS CloudHSM prices](../facts/kms.md#kms-custom-key-store-cost-two-hsms)
kms-custom-key-store-customer-managed-only
  claim: Only customer managed KMS keys can be stored in a CloudHSM-backed custom key store; AWS managed keys are always generated and stored in the default AWS KMS key store.
  link: [only customer managed KMS keys](../facts/kms.md#kms-custom-key-store-customer-managed-only)
  link: [always generated and stored](../facts/kms.md#kms-custom-key-store-customer-managed-only)
kms-custom-key-store-extra-skills
  claim: To use a CloudHSM custom key store you set up a CloudHSM cluster, add HSMs, manage HSM users and possibly restore HSMs from backup, which are security-sensitive tasks.
  link: [manage HSMs users](../facts/kms.md#kms-custom-key-store-extra-skills)
  link: [These are security sensitive tasks](../facts/kms.md#kms-custom-key-store-extra-skills)
kms-custom-key-store-only-if-mandated
  claim: AWS suggests a custom key store only when regulations explicitly mandate key material protection in a single-tenant HSM or in an HSM you control outside AWS, and only when that risk outweighs the extra cost, operational complexity and reduced performance.
  link: [mandate key material protection in a single-tenant HSM](../facts/kms.md#kms-custom-key-store-only-if-mandated)
  link: [additional cost, operational complexity, and reduced performance](../facts/kms.md#kms-custom-key-store-only-if-mandated)
kms-custom-key-store-two-types
  claim: Besides the standard key store, AWS KMS supports two custom key store types: AWS CloudHSM key stores backed by a customer-owned CloudHSM cluster, and external key stores backed by an HSM or key manager outside the AWS Cloud.
  link: [dedicated, customer-owned AWS CloudHSM cluster](../facts/kms.md#kms-custom-key-store-two-types)
  link: [outside the AWS Cloud](../facts/kms.md#kms-custom-key-store-two-types)
kms-customer-managed-key-full-control
  claim: Customer managed keys are the KMS keys you create, own and manage in your account; you have full control over them, including key policies, IAM policies and grants, enabling and disabling, rotation, tags, aliases and scheduling deletion.
  link: [you create, own, and manage](../facts/kms.md#kms-customer-managed-key-full-control)
  link: [You have full control over these KMS keys](../facts/kms.md#kms-customer-managed-key-full-control)
kms-data-key-caching-reduces-requests
  claim: If you exceed the GenerateDataKey request quota, the data key caching feature of the AWS Encryption SDK can reduce how often you call AWS KMS.
  link: [data key caching feature](../facts/kms.md#kms-data-key-caching-reduces-requests)
  link: [Reusing data keys](../facts/kms.md#kms-data-key-caching-reduces-requests)
kms-default-key-policy-enables-iam
  claim: The critical default key policy statement gives the owning AWS account full access to the KMS key and lets the account use IAM policies to allow access in addition to the key policy.
  link: [full access to the KMS key](../facts/kms.md#kms-default-key-policy-enables-iam)
  link: [use IAM policies to allow access](../facts/kms.md#kms-default-key-policy-enables-iam)
kms-default-key-policy-prevents-unmanageable
  claim: The default key policy statement reduces the risk of the key becoming unmanageable by giving access control permission to account administrators, including the account root user, which cannot be deleted.
  link: [the key becoming unmanageable](../facts/kms.md#kms-default-key-policy-prevents-unmanageable)
  link: [the account root user, which cannot be deleted](../facts/kms.md#kms-default-key-policy-prevents-unmanageable)
kms-deletion-irreversible-data-unrecoverable
  claim: Deleting a KMS key is destructive and irreversible: it deletes the key material and all metadata, and data encrypted under the key can no longer be decrypted and becomes unrecoverable. The only exceptions are multi-Region replica keys and asymmetric and HMAC KMS keys with imported key material.
  link: [destructive and potentially dangerous](../facts/kms.md#kms-deletion-irreversible-data-unrecoverable)
  link: [that data becomes unrecoverable](../facts/kms.md#kms-deletion-irreversible-data-unrecoverable)
kms-deletion-may-run-24-hours-late
  claim: The actual waiting period before deletion can be up to 24 hours longer than the one you scheduled.
  scope: per KMS key deletion; maximum; use DescribeKey to see the actual deletion date.
  link: [24 hours](../facts/kms.md#kms-deletion-may-run-24-hours-late)
  say: twenty-four hours
kms-deletion-waiting-period-7-to-30-days
  claim: KMS requires a waiting period of 7 – 30 days before it deletes a KMS key, and the default waiting period is 30 days; a key cannot be deleted immediately.
  scope: per KMS key deletion; default; not adjustable; minimum 7 days, maximum 30 days, default 30 days.
  link: [7 – 30 days](../facts/kms.md#kms-deletion-waiting-period-7-to-30-days)
  link: [30 days](../facts/kms.md#kms-deletion-waiting-period-7-to-30-days)
  say: seven to thirty days | thirty days
kms-dg-security-services-positioning
  claim: The AWS security services decision guide positions AWS KMS as creating and controlling the keys that protect your data, AWS CloudHSM as cloud-based HSMs, ACM for SSL/TLS certificates, AWS Private CA for private CA hierarchies and Secrets Manager for credentials and other secrets.
  link: [creates and controls the cryptographic keys](../facts/kms.md#kms-dg-security-services-positioning)
  link: [cloud-based hardware security modules (HSMs)](../facts/kms.md#kms-dg-security-services-positioning)
  link: [private certificate authority hierarchies](../facts/kms.md#kms-dg-security-services-positioning)
kms-disable-instead-of-delete
  claim: If you are not sure you no longer need a KMS key, AWS suggests disabling it instead of deleting it: a disabled key can be re-enabled and a scheduled deletion can be cancelled, but a deleted key cannot be recovered.
  link: [disabling the KMS key instead of deleting it](../facts/kms.md#kms-disable-instead-of-delete)
  link: [you cannot recover a deleted KMS key](../facts/kms.md#kms-disable-instead-of-delete)
kms-disabled-key-no-crypto-until-reenabled
  claim: A KMS key is enabled by default when created; a disabled key cannot be used in any cryptographic operation until you re-enable it.
  link: [enabled by default](../facts/kms.md#kms-disabled-key-no-crypto-until-reenabled)
  link: [until you re-enable it](../facts/kms.md#kms-disabled-key-no-crypto-until-reenabled)
kms-disabled-keys-still-charged
  claim: A disabled KMS key cannot be used for cryptographic operations but still exists and can be re-enabled; disabled keys continue to incur storage charges, and AWS recommends disabling keys instead of deleting them until you are sure they protect no data.
  link: [Disabled keys continue to incur storage charges](../facts/kms.md#kms-disabled-keys-still-charged)
  link: [disable keys instead of deleting them](../facts/kms.md#kms-disabled-keys-still-charged)
kms-does-not-store-data-keys
  claim: AWS KMS generates, encrypts and decrypts data keys but does not store, manage or track them or do cryptographic operations with them; you use and manage data keys outside KMS.
  link: [does not store, manage, or track](../facts/kms.md#kms-does-not-store-data-keys)
  link: [manage data keys outside of AWS KMS](../facts/kms.md#kms-does-not-store-data-keys)
kms-dryrun-checks-request
  claim: The KMS Encrypt operation accepts an optional DryRun parameter that checks whether the request will succeed.
  link: [Checks if your request will succeed.](../facts/kms.md#kms-dryrun-checks-request)
  link: [DryRun is an optional parameter.](../facts/kms.md#kms-dryrun-checks-request)
kms-dynamodb-always-encrypted-three-key-types
  claim: All user data stored in DynamoDB is fully encrypted at rest. When creating a table you choose an AWS owned key (the default encryption type, no additional charge), an AWS managed key or a customer managed key, and you can switch between these key types at any time.
  link: [Default encryption type.](../facts/kms.md#kms-dynamodb-always-encrypted-three-key-types)
  link: [switch between these key types at any time](../facts/kms.md#kms-dynamodb-always-encrypted-three-key-types)
kms-dynamodb-encryption-cannot-disable
  claim: DynamoDB enables server-side encryption at rest by default and you cannot disable it; the KMS best-practice guide recommends a customer managed key for DynamoDB tables.
  link: [you can't disable it](../facts/kms.md#kms-dynamodb-encryption-cannot-disable)
  link: [use a customer managed key](../facts/kms.md#kms-dynamodb-encryption-cannot-disable)
kms-ebs-default-key-aws-ebs-or-cmk
  claim: Encryption by default is a Region-specific setting of your AWS account. When you enable it, you keep the AWS managed key aws/ebs as the default encryption key or choose a symmetric customer managed key.
  scope: per Region, per account; default; not adjustable.
  link: [the AWS managed key with the alias aws/ebs](../facts/kms.md#kms-ebs-default-key-aws-ebs-or-cmk)
  link: [a symmetric customer managed encryption key](../facts/kms.md#kms-ebs-default-key-aws-ebs-or-cmk)
kms-ebs-encryption-by-default-region-setting
  claim: EBS encryption by default is a Region-specific setting; once enabled for a Region, you cannot disable it for individual volumes or snapshots in that Region, and it has no effect on existing volumes or snapshots.
  link: [a Region-specific setting](../facts/kms.md#kms-ebs-encryption-by-default-region-setting)
  link: [no effect on existing EBS volumes or snapshots](../facts/kms.md#kms-ebs-encryption-by-default-region-setting)
kms-ebs-encryption-status-fixed-at-create
  claim: An EBS volume's encryption status is set when the volume is created and cannot be changed; you can apply a new encryption status while copying a snapshot. Snapshots of encrypted volumes, and volumes made from them, are encrypted automatically.
  link: [cannot change the encryption status](../facts/kms.md#kms-ebs-encryption-status-fixed-at-create)
  link: [while copying a snapshot](../facts/kms.md#kms-ebs-encryption-status-fixed-at-create)
kms-encrypt-max-plaintext-4096-bytes
  claim: The KMS Encrypt operation encrypts plaintext of up to 4,096 bytes using a KMS key. AWS KMS supports sending data up to 4 KB to be encrypted directly, but envelope encryption can offer significant performance benefits.
  scope: per Encrypt request; maximum; not adjustable.
  link: [4,096 bytes](../facts/kms.md#kms-encrypt-max-plaintext-4096-bytes)
  link: [4 KB](../facts/kms.md#kms-encrypt-max-plaintext-4096-bytes)
  say: four thousand ninety-six bytes | four kilobytes
kms-encryption-context-not-secret-in-cloudtrail
  claim: Encryption context is not secret and not encrypted; it appears in plaintext in CloudTrail logs, so it should not include sensitive information.
  link: [not secret and not encrypted](../facts/kms.md#kms-encryption-context-not-secret-in-cloudtrail)
  link: [appears in plaintext in AWS CloudTrail Logs](../facts/kms.md#kms-encryption-context-not-secret-in-cloudtrail)
kms-encryption-context-same-to-decrypt
  claim: Encryption context is an optional set of non-secret key-value pairs; it is cryptographically bound to the ciphertext, so the same encryption context is required to decrypt the data.
  link: [the same encryption context is required](../facts/kms.md#kms-encryption-context-same-to-decrypt)
  link: [cryptographically bound to the ciphertext](../facts/kms.md#kms-encryption-context-same-to-decrypt)
kms-envelope-encryption-why
  claim: Envelope encryption reduces network load because only the small data key request and delivery go over the network, while the data key is used locally; KMS supports direct encryption of data up to 4 KB.
  link: [up to 4 KB](../facts/kms.md#kms-envelope-encryption-why)
  link: [reduces the network load](../facts/kms.md#kms-envelope-encryption-why)
kms-envelope-store-encrypted-data-key
  claim: After encrypting data with the plaintext data key, remove it from memory as soon as possible and store the encrypted data key with the encrypted data.
  link: [remove it from memory as soon as possible](../facts/kms.md#kms-envelope-store-encrypted-data-key)
  link: [safely store the encrypted data key](../facts/kms.md#kms-envelope-store-encrypted-data-key)
kms-external-key-store-customer-responsible
  claim: With an external key store, you are responsible for the security, reliability, durability and performance of the keys in your external key manager, whereas for standard KMS keys AWS KMS is responsible for their security, availability, latency and durability.
  scope: KMS keys in an external key store.
  link: [the balance of responsibility shifts in your direction](../facts/kms.md#kms-external-key-store-customer-responsible)
kms-external-key-store-key-never-leaves
  claim: In an external key store, AWS KMS cannot create, delete or manage external keys, and the key material never leaves your external key manager; you are responsible for its availability, durability and latency.
  link: [never leaves your external key manager](../facts/kms.md#kms-external-key-store-key-never-leaves)
  link: [availability, durability, and latency](../facts/kms.md#kms-external-key-store-key-never-leaves)
kms-external-key-store-not-recommended
  claim: External key stores are not recommended; consider one only with an explicit, unchangeable requirement to keep key material outside AWS.
  link: [External key stores are not recommended.](../facts/kms.md#kms-external-key-store-not-recommended)
  link: [keep key material outside AWS](../facts/kms.md#kms-external-key-store-not-recommended)
kms-faq-asym-hmac-no-auto-rotation-alias
  claim: Automatic key rotation is not supported for asymmetric or HMAC KMS keys; if needed you rotate them manually by creating a new KMS key and pointing the existing alias at it.
  link: [Automatic key rotation is not supported](../facts/kms.md#kms-faq-asym-hmac-no-auto-rotation-alias)
  link: [mapping an existing key alias](../facts/kms.md#kms-faq-asym-hmac-no-auto-rotation-alias)
kms-faq-asym-key-encrypt-or-sign-not-both
  claim: A single asymmetric KMS key cannot be used for both encryption and signing: you choose its use when you create it, and an RSA key can be used for signing or encryption, but not both.
  link: [signing or encryption operations, but not both](../facts/kms.md#kms-faq-asym-key-encrypt-or-sign-not-both)
  link: [must specify whether the key can be used](../facts/kms.md#kms-faq-asym-key-encrypt-or-sign-not-both)
kms-faq-asym-no-custom-key-store
  claim: You cannot use the custom key store feature with asymmetric KMS keys.
  link: [cannot use the custom key store functionality](../facts/kms.md#kms-faq-asym-no-custom-key-store)
kms-faq-asym-rps-limits-differ
  claim: Asymmetric KMS keys have service limits of their own: the request per second rate limits are different for different key types and algorithms.
  link: [rate limits are different for different key types](../facts/kms.md#kms-faq-asym-rps-limits-differ)
kms-faq-asymmetric-data-limit-4kb
  claim: Data sent to AWS KMS for asymmetric operations is limited to 4 KB; data for Encrypt, Decrypt or Re-Encrypt with asymmetric operations must be less than 4 KB.
  scope: per asymmetric operation request; maximum; not adjustable.
  link: [4 KB](../facts/kms.md#kms-faq-asymmetric-data-limit-4kb)
kms-faq-auto-rotation-no-reencrypt
  claim: With automatic rotation you do not have to re-encrypt your data: AWS KMS keeps previous versions of the key to decrypt data encrypted under an old version, and encrypts all new requests under the newest version.
  link: [you don’t have to re-encrypt your data](../facts/kms.md#kms-faq-auto-rotation-no-reencrypt)
  link: [keeps previous versions of keys](../facts/kms.md#kms-faq-auto-rotation-no-reencrypt)
kms-faq-aws-managed-no-direct-control
  claim: AWS managed keys are created in your account and all their usage is logged in CloudTrail, but you have no direct control over the keys themselves.
  link: [no direct control over the keys themselves](../facts/kms.md#kms-faq-aws-managed-no-direct-control)
  link: [all usage is logged in CloudTrail](../facts/kms.md#kms-faq-aws-managed-no-direct-control)
kms-faq-aws-owned-no-policy-no-logs
  claim: AWS owned keys are the most automated; they encrypt your data within AWS but give no policy controls and no CloudTrail logs of their key activity.
  link: [do not provide policy controls or CloudTrail logs](../facts/kms.md#kms-faq-aws-owned-no-policy-no-logs)
  link: [the most automated](../facts/kms.md#kms-faq-aws-owned-no-policy-no-logs)
kms-faq-billing-keys-and-requests
  claim: AWS KMS charges for every KMS key you create and for API requests each month above a free tier, with no minimum fee and no setup fees.
  link: [all KMS keys you create](../facts/kms.md#kms-faq-billing-keys-and-requests)
  link: [API requests](../facts/kms.md#kms-faq-billing-keys-and-requests)
  link: [no minimum fee](../facts/kms.md#kms-faq-billing-keys-and-requests)
kms-faq-cloudhsm-cluster-shared-with-apps
  claim: AWS KMS does not need exclusive access to your CloudHSM cluster, so the cluster can also serve other applications, though heavy load on either side can reduce throughput for the other.
  link: [does not require exclusive access](../facts/kms.md#kms-faq-cloudhsm-cluster-shared-with-apps)
  link: [reduced throughput](../facts/kms.md#kms-faq-cloudhsm-cluster-shared-with-apps)
kms-faq-cloudhsm-ks-availability-risk
  claim: With a CloudHSM key store you are responsible for key availability: CloudHSM configuration errors or accidental deletion of key material in the cluster could impact availability, and the number of HSMs and choice of AZs affect resilience.
  link: [could impact availability](../facts/kms.md#kms-faq-cloudhsm-ks-availability-risk)
  link: [number of HSMs you use](../facts/kms.md#kms-faq-cloudhsm-ks-availability-risk)
kms-faq-cloudhsm-ks-extra-audit-logs
  claim: A CloudHSM key store adds audit sources beyond KMS CloudTrail logs: CloudHSM API activity in CloudTrail, local cluster logs of user and key management activity, and copies of those logs in CloudWatch.
  link: [three further auditing mechanisms](../facts/kms.md#kms-faq-cloudhsm-ks-extra-audit-logs)
  link: [local user and key management activity logs](../facts/kms.md#kms-faq-cloudhsm-ks-extra-audit-logs)
kms-faq-cloudhsm-ks-keys-generated-only-in-hsms
  claim: Importing your own key material into a CloudHSM custom key store is not supported; its keys can only be generated in the HSMs of your CloudHSM cluster.
  link: [is not supported](../facts/kms.md#kms-faq-cloudhsm-ks-keys-generated-only-in-hsms)
  link: [can only be generated in the HSMs](../facts/kms.md#kms-faq-cloudhsm-ks-keys-generated-only-in-hsms)
kms-faq-cloudhsm-ks-lower-request-rate
  claim: Keys in a CloudHSM custom key store can be used through KMS API calls at lower rates than keys in the default AWS KMS key store.
  link: [lower than for keys stored in the default](../facts/kms.md#kms-faq-cloudhsm-ks-lower-request-rate)
kms-faq-cloudhsm-ks-manual-rotation-alias
  claim: Keys in a custom key store cannot be rotated automatically; you rotate them manually by creating new keys and re-mapping the KMS aliases your application uses.
  link: [must be performed manually](../facts/kms.md#kms-faq-cloudhsm-ks-manual-rotation-alias)
  link: [re-mapping AWS KMS key aliases](../facts/kms.md#kms-faq-cloudhsm-ks-manual-rotation-alias)
kms-faq-cloudhsm-ks-no-import-no-auto-rotation
  claim: In a CloudHSM custom key store you cannot import key material and AWS KMS cannot rotate keys automatically; otherwise keys are managed like any other customer managed KMS key.
  link: [You cannot import key material](../facts/kms.md#kms-faq-cloudhsm-ks-no-import-no-auto-rotation)
  link: [you cannot have AWS KMS automatically rotate keys](../facts/kms.md#kms-faq-cloudhsm-ks-no-import-no-auto-rotation)
kms-faq-cloudtrail-all-api-requests
  claim: CloudTrail logs show all AWS KMS API requests, both management requests (create, rotate, disable, policy edits) and cryptographic requests (encrypt and decrypt).
  link: [all AWS KMS API requests](../facts/kms.md#kms-faq-cloudtrail-all-api-requests)
  link: [management requests](../facts/kms.md#kms-faq-cloudtrail-all-api-requests)
  link: [cryptographic requests](../facts/kms.md#kms-faq-cloudtrail-all-api-requests)
kms-faq-data-keys-exportable
  claim: Data keys and data key pairs can be exported out of the HSMs: symmetric data keys with GenerateDataKey or GenerateDataKeyWithoutPlaintext, asymmetric data key pairs with GenerateDataKeyPair or GenerateDataKeyPairWithoutPlaintext.
  link: [GenerateDataKey API](../facts/kms.md#kms-faq-data-keys-exportable)
  link: [GenerateDataKeyWithoutPlaintext API](../facts/kms.md#kms-faq-data-keys-exportable)
  link: [GenerateDataKeyPair API](../facts/kms.md#kms-faq-data-keys-exportable)
kms-faq-disable-keys-temporarily
  claim: You can temporarily disable KMS keys so that no one can use them, and re-enable them later.
  link: [Temporarily disable keys](../facts/kms.md#kms-faq-disable-keys-temporarily)
kms-faq-disabled-keys-count-toward-limit
  claim: Both enabled and disabled KMS keys count toward the KMS key limit of an account in a Region, so AWS recommends deleting disabled keys you no longer use; you may request a limit increase through the AWS Support Center.
  scope: per account per Region; default; adjustable.
  link: [both enabled and disabled KMS keys count](../facts/kms.md#kms-faq-disabled-keys-count-toward-limit)
kms-faq-ecc-ecdh-key-agreement
  claim: With elliptic curve key types, AWS KMS supports the ECDH key agreement algorithms.
  link: [ECDH key agreement algorithms](../facts/kms.md#kms-faq-ecc-ecdh-key-agreement)
kms-faq-ecc-keys-no-encryption
  claim: Encryption algorithms cannot be used with the elliptic curve KMS key types ECC NIST P-256, ECC NIST P-384, ECC NIST-521 and ECC SECG P-256k1; AWS KMS supports the RSAES_OAEP_SHA_1 and RSAES_OAEP_SHA_256 encryption algorithms with the RSA 2048, RSA 3072 and RSA 4096 key types.
  link: [Encryption algorithms cannot be used](../facts/kms.md#kms-faq-ecc-keys-no-encryption)
kms-faq-endpoints-tls-pfs-only
  claim: The KMS API endpoints receive requests over HTTPS using only TLS cipher suites that support perfect forward secrecy.
  link: [perfect forward secrecy](../facts/kms.md#kms-faq-endpoints-tls-pfs-only)
kms-faq-exported-data-key-encrypted-under-kms-key
  claim: A data key that AWS KMS returns is encrypted under a KMS key you define, and only users with permission to use that KMS key to decrypt can decrypt the encrypted data key.
  link: [decrypted by only users with permissions](../facts/kms.md#kms-faq-exported-data-key-encrypted-under-kms-key)
kms-faq-fips-140-2-endpoints-commercial-regions
  claim: Applications use the FIPS 140-2 validated KMS endpoints by connecting to the unique Regional FIPS HTTPS endpoints, which are available in all commercial Regions where AWS KMS is available.
  link: [FIPS 140-2 validated API endpoints](../facts/kms.md#kms-faq-fips-140-2-endpoints-commercial-regions)
  link: [all commercial Regions where AWS KMS is available](../facts/kms.md#kms-faq-fips-140-2-endpoints-commercial-regions)
kms-faq-fips-140-3-hsms-all-regions
  claim: FIPS 140-3 Security Level 3 validated HSMs are deployed in all AWS Regions where AWS KMS is offered; by regulation, KMS in China Regions uses OSCCA certified HSMs instead of NIST FIPS HSMs.
  link: [FIPS 140-3 Security Level 3](../facts/kms.md#kms-faq-fips-140-3-hsms-all-regions)
  link: [all AWS Regions where AWS KMS is offered](../facts/kms.md#kms-faq-fips-140-3-hsms-all-regions)
  link: [cannot use NIST FIPS HSMs](../facts/kms.md#kms-faq-fips-140-3-hsms-all-regions)
kms-faq-free-tier-excludes-asymmetric
  claim: API requests that involve asymmetric KMS keys, and requests to GenerateDataKeyPair and GenerateDataKeyPairWithoutPlaintext, are excluded from the KMS free tier.
  link: [excluded from the Free Tier](../facts/kms.md#kms-faq-free-tier-excludes-asymmetric)
  link: [API requests involving asymmetric KMS keys](../facts/kms.md#kms-faq-free-tier-excludes-asymmetric)
kms-faq-import-expiry-cloudwatch-countdown
  claim: After you import key material, a CloudWatch metric counts down the time to expiration every few minutes, and a CloudWatch event is sent when the imported key expires.
  link: [counts down the time to expiration](../facts/kms.md#kms-faq-import-expiry-cloudwatch-countdown)
  link: [CloudWatch Event](../facts/kms.md#kms-faq-import-expiry-cloudwatch-countdown)
kms-faq-import-key-types
  claim: You can import symmetric keys, asymmetric keys (RSA and elliptic curve) and HMAC keys into AWS KMS.
  link: [symmetric keys](../facts/kms.md#kms-faq-import-key-types)
  link: [asymmetric keys (RSA and elliptic curve)](../facts/kms.md#kms-faq-import-key-types)
  link: [HMAC keys](../facts/kms.md#kms-faq-import-key-types)
kms-faq-import-own-keys-byok
  claim: You can import a copy of your key from your own key management infrastructure into AWS KMS and use it with any integrated AWS service or in your own applications.
  link: [import a copy of your key](../facts/kms.md#kms-faq-import-own-keys-byok)
kms-faq-import-wrapped-with-kms-public-key
  claim: During import, your key must be wrapped by an AWS KMS-provided public key using the supported wrapping algorithm; this verifies that your encrypted key can be decrypted only by AWS KMS.
  link: [wrapped by an AWS KMS-provided public key](../facts/kms.md#kms-faq-import-wrapped-with-kms-public-key)
kms-faq-imported-key-why
  claim: Imported keys help meet compliance requirements such as generating or keeping a secure copy of the key in your own infrastructure and being able to delete the imported copy from AWS immediately.
  link: [immediately delete the imported copy of the key](../facts/kms.md#kms-faq-imported-key-why)
kms-faq-imported-material-delete-now-or-expire
  claim: For a KMS key with imported key material, you can delete the key material on demand without a waiting period, or set an expiration time when you import it; you can re-import the material later.
  link: [without a waiting period](../facts/kms.md#kms-faq-imported-material-delete-now-or-expire)
  link: [define an expiration time](../facts/kms.md#kms-faq-imported-material-delete-now-or-expire)
  link: [re-import your key material](../facts/kms.md#kms-faq-imported-material-delete-now-or-expire)
kms-faq-imported-you-keep-copy
  claim: For imported keys you are responsible for keeping a copy in your own key management infrastructure so you can re-import them; for keys generated by AWS KMS, AWS ensures availability, security and durability until you schedule deletion.
  link: [maintaining a copy of your imported keys](../facts/kms.md#kms-faq-imported-you-keep-copy)
kms-faq-integrated-services-key-choice
  claim: AWS KMS is integrated with most other AWS services; some encrypt data by default with keys owned and managed by the service, and some let you choose between managing the keys yourself and letting the service manage them.
  link: [integrated with most other AWS services](../facts/kms.md#kms-faq-integrated-services-key-choice)
  link: [encrypted by default](../facts/kms.md#kms-faq-integrated-services-key-choice)
  link: [choice of managing the keys yourself](../facts/kms.md#kms-faq-integrated-services-key-choice)
kms-faq-key-quota-100000-aws-managed-excluded
  claim: You can create up to 100,000 KMS keys per account per Region; AWS managed KMS keys created on your behalf do not count against this limit.
  scope: per account per Region; default; adjustable; limit increase requests through the AWS Support Center.
  link: [100,000 KMS keys](../facts/kms.md#kms-faq-key-quota-100000-aws-managed-excluded)
  link: [do not count against this limit](../facts/kms.md#kms-faq-key-quota-100000-aws-managed-excluded)
kms-faq-kms-asymmetric-without-certificates
  claim: AWS KMS generates, manages and uses asymmetric keys for digital signing and encryption operations that do not require certificates.
  link: [operations that don’t require certificates](../facts/kms.md#kms-faq-kms-asymmetric-without-certificates)
kms-faq-kms-key-not-exportable-for-apps
  claim: AWS KMS keys cannot be exported for use in your own applications; they are created and used only within the service so that your policies are enforced and their use is logged centrally.
  link: [created and used only within the service](../facts/kms.md#kms-faq-kms-key-not-exportable-for-apps)
kms-faq-kms-keys-never-exported-plaintext
  claim: No KMS key, and no private portion of an asymmetric KMS key, can be exported in plain text from the HSMs; only the public portion of an asymmetric KMS key can be exported, from the console or with the GetPublicKey API.
  link: [cannot be exported in plain text](../facts/kms.md#kms-faq-kms-keys-never-exported-plaintext)
  link: [Only the public portion](../facts/kms.md#kms-faq-kms-keys-never-exported-plaintext)
  link: [GetPublicKey API](../facts/kms.md#kms-faq-kms-keys-never-exported-plaintext)
kms-faq-kms-no-certificates-stored
  claim: AWS KMS does not store digital certificates or associate them with the asymmetric KMS keys it creates; a certificate authority such as AWS Private CA can issue a certificate for the public portion of the key.
  link: [doesn’t store or associate digital certificates](../facts/kms.md#kms-faq-kms-no-certificates-stored)
kms-faq-manual-rotation-may-reencrypt
  claim: If you rotate imported or custom key store keys manually, you may have to re-encrypt your data, depending on whether you keep old versions of the keys available.
  link: [you may have to re-encrypt your data](../facts/kms.md#kms-faq-manual-rotation-may-reencrypt)
kms-faq-multi-region-same-partition
  claim: With AWS KMS multi-Region keys you can replicate a multi-Region primary key into multiple Regions within the same AWS partition.
  link: [replicate a multi-Region primary key](../facts/kms.md#kms-faq-multi-region-same-partition)
  link: [within the same AWS partition](../facts/kms.md#kms-faq-multi-region-same-partition)
kms-faq-no-limit-on-data-keys
  claim: There is no limit to the number of data keys that can be derived from a KMS key.
  link: [no limit to the number of data keys](../facts/kms.md#kms-faq-no-limit-on-data-keys)
kms-faq-no-migration-between-key-stores
  claim: Migrating keys between the different types of AWS KMS key store is not supported. All keys must be created in the key store where they will be used, except when you import your own key material into the default AWS KMS key store.
  link: [migrate keys between the different types](../facts/kms.md#kms-faq-no-migration-between-key-stores)
  link: [must be created in the key store](../facts/kms.md#kms-faq-no-migration-between-key-stores)
kms-faq-no-native-openssl-jce-cng
  claim: AWS KMS offers no native integration with other cryptographic API providers such as OpenSSL, JCE, Bouncy Castle or CNG; you must use the KMS APIs directly or through the AWS SDK.
  link: [no native integration](../facts/kms.md#kms-faq-no-native-openssl-jce-cng)
  link: [use AWS KMS APIs directly](../facts/kms.md#kms-faq-no-native-openssl-jce-cng)
kms-faq-no-one-retrieves-plaintext-keys
  claim: AWS KMS is designed so that no one, including AWS employees, can retrieve your plaintext KMS keys from the service.
  link: [no one, including AWS employees](../facts/kms.md#kms-faq-no-one-retrieves-plaintext-keys)
kms-faq-pci-dss-3-2-1
  claim: AWS KMS has been validated as having the functionality and security controls to help you meet the encryption and key management requirements of PCI DSS 3.2.1.
  link: [PCI DSS 3.2.1](../facts/kms.md#kms-faq-pci-dss-3-2-1)
kms-faq-plaintext-keys-stay-in-hsm-memory
  claim: Plaintext KMS keys never leave the HSMs, are never written to disk, and are used only in the volatile memory of the HSMs for the time needed to perform the requested operation.
  link: [never leave the HSMs](../facts/kms.md#kms-faq-plaintext-keys-stay-in-hsm-memory)
  link: [never written to disk](../facts/kms.md#kms-faq-plaintext-keys-stay-in-hsm-memory)
kms-faq-recommend-customer-managed-kms-hsms
  claim: AWS recommends customer managed keys created and stored in the KMS HSMs, because they offer the most flexibility, policy control, lifecycle management (including automatic and on-demand rotation for symmetric encryption keys) and complete auditability.
  link: [We recommend you choose customer managed keys](../facts/kms.md#kms-faq-recommend-customer-managed-kms-hsms)
  link: [the most flexibility, policy control, lifecycle management](../facts/kms.md#kms-faq-recommend-customer-managed-kms-hsms)
kms-faq-rotation-imported-on-demand-xks-yours
  claim: AWS KMS supports rotation of imported keys through on-demand rotation; for keys in an external key store (XKS), you manage all key lifecycle events, including rotation, in your own key manager.
  link: [rotation for imported keys using on-demand rotation](../facts/kms.md#kms-faq-rotation-imported-on-demand-xks-yours)
  link: [you manage all key lifecycle events including rotation](../facts/kms.md#kms-faq-rotation-imported-on-demand-xks-yours)
kms-faq-sign-large-data-digest
  claim: To sign data larger than 4 KB with an asymmetric KMS key, you can send a message digest of the data; the Sign request says whether it carries the full message or a digest.
  scope: per Sign request.
  link: [larger than 4 KB](../facts/kms.md#kms-faq-sign-large-data-digest)
  link: [create a message digest of the data](../facts/kms.md#kms-faq-sign-large-data-digest)
kms-faq-sla-service-credit
  claim: AWS KMS has an SLA that provides a service credit if your monthly uptime percentage is below the service commitment in a billing cycle.
  link: [service credit](../facts/kms.md#kms-faq-sla-service-credit)
  link: [monthly uptime percentage](../facts/kms.md#kms-faq-sla-service-credit)
kms-faq-symmetric-256-bit-aes-gcm
  claim: AWS KMS creates 256-bit symmetric KMS keys for encryption, and when it uses one to encrypt or decrypt it uses AES in Galois Counter Mode (AES-GCM).
  scope: per symmetric encryption KMS key; fixed.
  link: [256-bit](../facts/kms.md#kms-faq-symmetric-256-bit-aes-gcm)
  link: [AES-GCM](../facts/kms.md#kms-faq-symmetric-256-bit-aes-gcm)
kms-faq-two-tier-endpoints-then-hsms
  claim: AWS KMS is a two-tier service: the API endpoints authenticate and authorize each request before passing the cryptographic operation to the KMS HSMs, or to your CloudHSM cluster when you use a custom key store.
  link: [a two-tier service](../facts/kms.md#kms-faq-two-tier-endpoints-then-hsms)
  link: [authenticate and authorize the request](../facts/kms.md#kms-faq-two-tier-endpoints-then-hsms)
kms-faq-vs-cloudhsm-kms-central-control
  claim: AWS KMS manages all your keys centrally, so you can enforce who can use your keys under which conditions, when they get rotated and who can manage them, and audit their use through CloudTrail.
  link: [Centralized management of all your keys](../facts/kms.md#kms-faq-vs-cloudhsm-kms-central-control)
  link: [audit the use of your keys](../facts/kms.md#kms-faq-vs-cloudhsm-kms-central-control)
kms-faq-where-data-encrypted-three-ways
  claim: Data is typically encrypted with AWS KMS in three ways: by calling the KMS APIs directly, by having AWS services encrypt it with data keys protected by your KMS keys, or with the AWS Encryption SDK inside your own applications, in AWS or not.
  link: [three scenarios](../facts/kms.md#kms-faq-where-data-encrypted-three-ways)
  link: [whether they operate in AWS or not](../facts/kms.md#kms-faq-where-data-encrypted-three-ways)
kms-faq-why-cloudhsm-key-store
  claim: A CloudHSM custom key store is useful in three cases: keys must be protected in a single-tenant HSM or one under your direct control; you must remove key material immediately and prove it by independent means; or you must audit all key use independently of AWS KMS or CloudTrail.
  link: [single tenant HSM](../facts/kms.md#kms-faq-why-cloudhsm-key-store)
  link: [immediately remove key material](../facts/kms.md#kms-faq-why-cloudhsm-key-store)
  link: [independently of AWS KMS or CloudTrail](../facts/kms.md#kms-faq-why-cloudhsm-key-store)
kms-faq-xks-any-cmk-service
  claim: XKS keys can encrypt data in any AWS service that integrates with AWS KMS using customer managed keys.
  link: [any AWS service that integrates with AWS KMS](../facts/kms.md#kms-faq-xks-any-cmk-service)
kms-faq-xks-authorization-same
  claim: IAM policies, KMS key policies and grants work the same way for KMS keys in external key stores as for other KMS keys. In addition, you or your external key manager partners can implement a secondary layer of authorization controls based on request metadata that AWS KMS sends to the XKS proxy.
  link: [work the same way for KMS keys](../facts/kms.md#kms-faq-xks-authorization-same)
kms-faq-xks-availability-risk
  claim: With XKS you are responsible for the availability of the XKS Proxy and external key material; for example, if the proxy or key manager cannot decrypt an EBS volume key, the EC2 instance fails to launch.
  link: [responsible for the availability of the XKS Proxy](../facts/kms.md#kms-faq-xks-availability-risk)
  link: [your EC2 instance will fail to launch](../facts/kms.md#kms-faq-xks-availability-risk)
kms-faq-xks-client-side-encryption
  claim: XKS keys also work in your own applications with client-side symmetric encryption that uses AWS KMS as its key provider, such as the AWS Encryption SDK, the S3 Encryption Client and the DynamoDB Encryption Client.
  link: [used from within your own applications](../facts/kms.md#kms-faq-xks-client-side-encryption)
kms-faq-xks-definition
  claim: An external key store (XKS) is a custom key store backed by key management infrastructure that you own and manage outside AWS; all encryption and decryption with its KMS keys run in your key manager.
  link: [outside of AWS](../facts/kms.md#kms-faq-xks-definition)
  link: [physically inaccessible to AWS](../facts/kms.md#kms-faq-xks-definition)
kms-faq-xks-double-encryption
  claim: With XKS, data keys are double encrypted, first by a KMS key in AWS KMS and then by the key in your external key manager, so no ciphertext can be decrypted without the external key material.
  link: [no ciphertext can ever be decrypted](../facts/kms.md#kms-faq-xks-double-encryption)
  link: [encrypted a second time](../facts/kms.md#kms-faq-xks-double-encryption)
kms-faq-xks-durability-risk
  claim: With XKS you alone are responsible for the durability of external keys; if the external key is permanently lost or deleted, all ciphertext encrypted under the XKS key is unrecoverable.
  link: [solely responsible for the durability](../facts/kms.md#kms-faq-xks-durability-risk)
  link: [unrecoverable](../facts/kms.md#kms-faq-xks-durability-risk)
kms-faq-xks-excluded-from-sla
  claim: Use of XKS is excluded from the public AWS KMS availability SLA, and XKS keys are also excluded from the availability SLA of any AWS service where you configure them to encrypt data.
  link: [specifically exclude the use of XKS](../facts/kms.md#kms-faq-xks-excluded-from-sla)
  link: [excluded in the availability SLA](../facts/kms.md#kms-faq-xks-excluded-from-sla)
kms-faq-xks-key-price
  claim: Like all customer managed keys, XKS keys cost $1 per month per key until they are deleted, and their requests are charged at the same rate as other symmetric KMS keys.
  scope: per customer managed KMS key; fixed.
  link: [$1 per month per key](../facts/kms.md#kms-faq-xks-key-price)
  link: [charged at the same rate](../facts/kms.md#kms-faq-xks-key-price)
kms-faq-xks-latency-500ms-400-error
  claim: If a single request from AWS KMS to the XKS Proxy, including one retry, takes more than 500ms, AWS KMS returns a 400 error to its caller; KMS retries once any request that takes 250ms.
  scope: per request from AWS KMS to the XKS Proxy; maximum; not adjustable.
  link: [more than 500ms](../facts/kms.md#kms-faq-xks-latency-500ms-400-error)
  link: [400 error](../facts/kms.md#kms-faq-xks-latency-500ms-400-error)
  link: [250ms](../facts/kms.md#kms-faq-xks-latency-500ms-400-error)
kms-faq-xks-no-migration-of-existing-keys
  claim: Existing KMS keys cannot be migrated into XKS keys; all XKS keys must be created as new keys in KMS. You can re-encrypt existing data under newly generated XKS keys, assuming the AWS service or your own application supports the action.
  link: [You cannot migrate existing KMS keys](../facts/kms.md#kms-faq-xks-no-migration-of-existing-keys)
  link: [created as new keys in KMS](../facts/kms.md#kms-faq-xks-no-migration-of-existing-keys)
kms-faq-xks-proxy-in-your-network
  claim: AWS KMS forwards XKS requests to a component in your network called an XKS Proxy, which passes them to your key management infrastructure.
  link: [called an XKS Proxy](../facts/kms.md#kms-faq-xks-proxy-in-your-network)
kms-faq-xks-revoke-caching-5min-24h
  claim: After you disable, block or delete an XKS key, the next API call fails for services that do not cache keys; services that cache data keys may keep them from 5 mins to 24 hrs, and resources in use react differently.
  scope: per AWS service that caches data keys; maximum.
  link: [using this XKS KMS key will fail](../facts/kms.md#kms-faq-xks-revoke-caching-5min-24h)
  link: [5 mins to 24 hrs](../facts/kms.md#kms-faq-xks-revoke-caching-5min-24h)
kms-faq-xks-rotation-in-external-manager
  claim: Automatic rotation of XKS keys is possible but happens entirely in the external key manager; it is supported by the XKS specification and offered by most XKS vendors.
  link: [occurs entirely in the external key manager](../facts/kms.md#kms-faq-xks-rotation-in-external-manager)
kms-faq-xks-symmetric-operations-only
  claim: External keys support the symmetric encryption operations Encrypt, ReEncrypt, Decrypt and GenerateDataKey.
  link: [Encrypt, ReEncrypt, Decrypt, and GenerateDataKey](../facts/kms.md#kms-faq-xks-symmetric-operations-only)
kms-faq-xks-why-regulation
  claim: Use an external key store when rules or regulations require encryption keys to be stored and used outside AWS under your control.
  link: [stored and used outside of AWS](../facts/kms.md#kms-faq-xks-why-regulation)
kms-faq-you-define-who-uses-keys
  claim: AWS KMS enforces the usage and management policies you define, and you can allow IAM users and roles from your account or other accounts to use and manage your keys.
  link: [usage and management policies that you define](../facts/kms.md#kms-faq-you-define-who-uses-keys)
  link: [from your account or other accounts](../facts/kms.md#kms-faq-you-define-who-uses-keys)
kms-free-tier-20000-requests
  claim: The KMS free tier is 20,000 requests/month, calculated across all Regions where KMS is available.
  scope: calculated across all Regions where AWS KMS is available; requests that use asymmetric KMS keys and GenerateDataKeyPair requests are excluded from the free tier.
  link: [20,000 requests/month](../facts/kms.md#kms-free-tier-20000-requests)
  say: twenty thousand requests a month
kms-generatedatakey-returns-plaintext-and-encrypted
  claim: GenerateDataKey returns a plaintext copy of the data key and a copy encrypted under the symmetric encryption KMS key you specify.
  link: [a plaintext copy of the data key](../facts/kms.md#kms-generatedatakey-returns-plaintext-and-encrypted)
  link: [encrypted under the KMS key](../facts/kms.md#kms-generatedatakey-returns-plaintext-and-encrypted)
kms-grant-allow-not-deny-delete-removes
  claim: A grant can allow access to a KMS key but not deny it; an authorized principal can delete a grant by retiring or revoking it, which removes all permissions the grant allowed.
  link: [but not deny access](../facts/kms.md#kms-grant-allow-not-deny-delete-removes)
  link: [eliminates all permissions that the grant allowed](../facts/kms.md#kms-grant-allow-not-deny-delete-removes)
kms-grant-allow-only-one-key-temporary
  claim: A KMS grant allows a principal or service principal to use one KMS key; it can allow but not deny, can be for a key in another account, and is often used for temporary permissions because it can be created, used and deleted without changing key policies or IAM policies.
  link: [Grants are often used for temporary permissions](../facts/kms.md#kms-grant-allow-only-one-key-temporary)
  link: [exactly one KMS key](../facts/kms.md#kms-grant-allow-only-one-key-temporary)
  link: [but not deny access](../facts/kms.md#kms-grant-allow-only-one-key-temporary)
kms-grant-eventual-consistency-token
  claim: The KMS API is eventually consistent: a change to a grant typically takes less than a few seconds to propagate, but in some cases it can take several minutes. A grant token lets the grantee use the grant until the grant has fully propagated.
  link: [it can take several minutes](../facts/kms.md#kms-grant-eventual-consistency-token)
  link: [until the grant has fully propagated](../facts/kms.md#kms-grant-eventual-consistency-token)
kms-grant-subset-operations
  claim: Grants can allow only a subset of AWS KMS operations: viewing the key, using it in cryptographic operations, and creating and retiring grants.
  link: [only a subset of AWS KMS operations](../facts/kms.md#kms-grant-subset-operations)
  link: [create and retire grants](../facts/kms.md#kms-grant-subset-operations)
kms-grants-used-by-integrated-services
  claim: AWS services that integrate with KMS commonly use grants: the service creates a grant for a user, uses it, and retires it as soon as the task is complete.
  link: [as soon as its task is complete](../facts/kms.md#kms-grants-used-by-integrated-services)
kms-hsm-fips-140-3-level-3
  claim: All AWS KMS keys, whatever their creation date or origin, are automatically protected by HSMs validated under FIPS 140-3 Security Level 3, and NIST validates the AWS KMS cryptographic module at FIPS 140-3 Security Level 3. FIPS 140-3 does not apply to AWS KMS in the China (Beijing) and China (Ningxia) Regions.
  scope: all AWS KMS keys outside the China (Beijing) and China (Ningxia) Regions.
  link: [FIPS 140-3 Security Level 3](../facts/kms.md#kms-hsm-fips-140-3-level-3)
  say: FIPS one-forty-three, Security Level three
kms-iam-least-privilege-key-arns
  claim: AWS KMS best practice for IAM policies is least privilege: give principals only the permissions they need on only the keys they must use, name each key ARN in the Resource element, and use a wildcard Resource only for permissions that require it.
  link: [only the permissions they need](../facts/kms.md#kms-iam-least-privilege-key-arns)
  link: [specify the key ARN of each KMS key](../facts/kms.md#kms-iam-least-privilege-key-arns)
kms-iam-policy-allow-needs-key-policy
  claim: Unless the key policy explicitly allows it, IAM policies cannot allow access to a KMS key: without permission from the key policy, IAM allow statements have no effect, although an IAM policy can deny a KMS permission without it; the default key policy enables IAM policies.
  link: [IAM policies that allow permissions have no effect](../facts/kms.md#kms-iam-policy-allow-needs-key-policy)
  link: [The default key policy enables IAM policies](../facts/kms.md#kms-iam-policy-allow-needs-key-policy)
kms-import-asymmetric-hmac-interoperable
  claim: For asymmetric and HMAC keys, importing key material creates compatible keys that work both inside and outside AWS.
  scope: asymmetric and HMAC KMS keys with imported key material; you cannot import key material into keys in custom key stores.
  link: [operate within and outside of AWS](../facts/kms.md#kms-import-asymmetric-hmac-interoperable)
kms-imported-asym-hmac-same-material-only
  claim: For asymmetric and HMAC keys with imported key material, the KMS key is permanently associated with that key material: you can reimport the same material but not different material, and you cannot enable automatic rotation (manual rotation is possible).
  link: [permanently associated with that key material](../facts/kms.md#kms-imported-asym-hmac-same-material-only)
  link: [cannot import different key material](../facts/kms.md#kms-imported-asym-hmac-same-material-only)
kms-imported-cannot-export
  claim: You cannot export imported key material: AWS KMS cannot return it in any form, so you must keep a copy outside AWS, preferably in an HSM, to reimport it.
  link: [cannot return the imported key material](../facts/kms.md#kms-imported-cannot-export)
  link: [maintain a copy of your imported key material](../facts/kms.md#kms-imported-cannot-export)
kms-imported-symmetric-multiple-materials
  claim: Symmetric encryption keys with imported key material support on-demand rotation: you can import multiple key materials and the current one is used for encryption and decryption, while older ones only decrypt.
  link: [support on-demand rotation](../facts/kms.md#kms-imported-symmetric-multiple-materials)
  link: [can only be used for decryption](../facts/kms.md#kms-imported-symmetric-multiple-materials)
kms-imported-you-own-durability
  claim: With imported key material you remain responsible for the key material; AWS KMS does not maintain the durability of imported key material at the same level as key material it generates.
  link: [you remain responsible for the key material](../facts/kms.md#kms-imported-you-own-durability)
  link: [does not maintain the durability](../facts/kms.md#kms-imported-you-own-durability)
kms-integrated-services-symmetric-only
  claim: AWS services integrated with KMS use only symmetric encryption KMS keys to encrypt your data and do not support encryption with asymmetric KMS keys.
  link: [use only symmetric encryption KMS keys](../facts/kms.md#kms-integrated-services-symmetric-only)
  link: [do not support encryption with asymmetric KMS keys](../facts/kms.md#kms-integrated-services-symmetric-only)
kms-key-administrators-cannot-use-key
  claim: Key administrators in the console default key policy can manage the KMS key but cannot use it in cryptographic operations; because they can change the key policy and create grants, they can give themselves and others more permissions.
  link: [do not have permissions to use](../facts/kms.md#kms-key-administrators-cannot-use-key)
  link: [change the key policy and create grants](../facts/kms.md#kms-key-administrators-cannot-use-key)
kms-key-last-usage-tracking
  claim: KMS records the last successful cryptographic operation performed with each KMS key, with the CloudTrail event ID, which helps you find unused keys.
  scope: per KMS key; use of a data key outside AWS KMS is not reflected in the last usage information; for some AWS services you must not rely on last usage alone to decide whether a key can be deleted.
  link: [the last successful cryptographic operation](../facts/kms.md#kms-key-last-usage-tracking)
kms-key-policy-max-length
  claim: The key policy document passed to PutKeyPolicy has a minimum length of 1 and a maximum length of 32768.
  scope: per KMS key policy; maximum; not adjustable; if the key policy exceeds the length constraint, AWS KMS returns LimitExceededException.
  link: [32768](../facts/kms.md#kms-key-policy-max-length)
  say: thirty-two thousand seven hundred sixty-eight
kms-key-policy-no-automatic-account-permission
  claim: Unlike other AWS resource policies, a KMS key policy does not automatically give permission to the account or any of its identities; account administrators need an explicit key policy statement.
  link: [does not automatically give permission to the account](../facts/kms.md#kms-key-policy-no-automatic-account-permission)
  link: [an explicit statement](../facts/kms.md#kms-key-policy-no-automatic-account-permission)
kms-key-policy-primary-exactly-one
  claim: A key policy is the resource policy of a KMS key and the primary way to control access to it; every KMS key must have exactly one key policy, and IAM policies and grants can also control access.
  link: [the primary way to control access](../facts/kms.md#kms-key-policy-primary-exactly-one)
  link: [exactly one key policy](../facts/kms.md#kms-key-policy-primary-exactly-one)
kms-key-policy-regional-iam-policies-global
  claim: IAM policies are global, but KMS key policies are Regional: a key policy controls access only to a KMS key in its own Region.
  scope: per KMS key.
  link: [key policies are Regional](../facts/kms.md#kms-key-policy-regional-iam-policies-global)
  link: [IAM policies, which are global](../facts/kms.md#kms-key-policy-regional-iam-policies-global)
  say: key policies are Regional | IAM policies are global
kms-key-states-overview
  claim: All KMS keys can be in the Enabled, Disabled and PendingDeletion states; PendingImport applies only to keys with imported key material and Unavailable only to keys in a custom key store.
  link: [Enabled, Disabled, and PendingDeletion states](../facts/kms.md#kms-key-states-overview)
  link: [The PendingImport state applies only](../facts/kms.md#kms-key-states-overview)
kms-key-type-key-policy-control
  claim: The key policy of a customer managed key is exclusively controlled by the customer; the key policy of an AWS managed key is controlled by the service and viewable by the customer; the key policy of an AWS owned key is controlled and viewable only by the AWS service.
  link: [Exclusively controlled by the customer](../facts/kms.md#kms-key-type-key-policy-control)
  link: [Controlled by service; viewable by customer](../facts/kms.md#kms-key-type-key-policy-control)
kms-key-type-logging-owned-not-viewable
  claim: Use of customer managed keys and AWS managed keys is logged to your CloudTrail trail or event data store; logging for AWS owned keys is not viewable by the customer.
  link: [Not viewable by the customer](../facts/kms.md#kms-key-type-logging-owned-not-viewable)
  link: [CloudTrail customer trail or event data store](../facts/kms.md#kms-key-type-logging-owned-not-viewable)
kms-key-type-row-aws-managed
  claim: For an AWS managed key you can view its metadata but cannot manage it; it is created in your account, its automatic rotation is required every year (approximately 365 days), and it has no monthly fee but a per-use fee that some AWS services pay for you.
  link: [Required. Every year (approximately 365 days).](../facts/kms.md#kms-key-type-row-aws-managed)
  link: [No monthly fee](../facts/kms.md#kms-key-type-row-aws-managed)
kms-key-type-row-aws-owned
  claim: For an AWS owned key you cannot view its metadata or manage it, it is not created in your account, the AWS service manages its rotation strategy, and it has no fees.
  link: [The AWS service manages the rotation strategy](../facts/kms.md#kms-key-type-row-aws-owned)
  link: [No fees](../facts/kms.md#kms-key-type-row-aws-owned)
kms-key-type-row-customer-managed
  claim: For a customer managed key you can view its metadata and manage it, it is created in your account, automatic rotation is optional, and it has a monthly fee (pro-rated hourly) plus a per-use fee.
  link: [Optional.](../facts/kms.md#kms-key-type-row-customer-managed)
  link: [Monthly fee (pro-rated hourly)](../facts/kms.md#kms-key-type-row-customer-managed)
kms-key-unmanageable-contact-support
  claim: If a key policy gives only one user access and that user is deleted, the key becomes unmanageable and you must contact AWS Support to regain access.
  link: [the key becomes unmanageable](../facts/kms.md#kms-key-unmanageable-contact-support)
  link: [contact AWS Support to regain access](../facts/kms.md#kms-key-unmanageable-contact-support)
kms-key-users-crypto-and-services
  claim: The console default key policy gives key users two statements: one to use the key directly in cryptographic operations, and one to allow integrated AWS services to use the key on their behalf, for example for S3 buckets and DynamoDB tables.
  link: [use the KMS key directly](../facts/kms.md#kms-key-users-crypto-and-services)
  link: [to use the KMS key on their behalf](../facts/kms.md#kms-key-users-crypto-and-services)
kms-keys-never-leave-unencrypted
  claim: KMS keys are created, managed, used and deleted entirely within AWS KMS and never leave the service unencrypted.
  link: [never leave the service unencrypted](../facts/kms.md#kms-keys-never-leave-unencrypted)
  link: [deleted entirely within AWS KMS](../facts/kms.md#kms-keys-never-leave-unencrypted)
kms-kms-star-gives-admin-and-usage
  claim: Allowing all actions (kms:*) in both the key policy and the identity-based policy gives a principal both administrative and usage permissions on the KMS key.
  link: [both administrative and usage permissions](../facts/kms.md#kms-kms-star-gives-admin-and-usage)
  link: [allow all actions (kms:*)](../facts/kms.md#kms-kms-star-gives-admin-and-usage)
kms-manual-rotation-new-key-alias
  claim: Manual key rotation means creating a new KMS key and using it in place of the current one; you must update references to the key ID or ARN, and pointing an alias at the new key avoids editing application code.
  link: [manual key rotation](../facts/kms.md#kms-manual-rotation-new-key-alias)
  link: [update references to the KMS key ID](../facts/kms.md#kms-manual-rotation-new-key-alias)
kms-mrk-cannot-convert
  claim: The multi-Region property is set when a key is created and cannot be changed: you cannot convert a single-Region key to a multi-Region key or the reverse; to move workloads you re-encrypt data with new multi-Region keys.
  link: [You cannot convert a single-Region key](../facts/kms.md#kms-mrk-cannot-convert)
  link: [you must re-encrypt your data](../facts/kms.md#kms-mrk-cannot-convert)
kms-mrk-data-residency-harder
  claim: Multi-Region keys make compliance with data residency mandates more complex; with single-Region keys, keys in a Region can decrypt sensitive data only in that Region.
  link: [Compliance with data residency mandates](../facts/kms.md#kms-mrk-data-residency-harder)
  link: [decrypt sensitive data only in that Region](../facts/kms.md#kms-mrk-data-residency-harder)
kms-mrk-disable-no-effect-on-related
  claim: Enabling or disabling a multi-Region key has no effect on its related multi-Region keys.
  link: [has no effect on related multi-Region keys](../facts/kms.md#kms-mrk-disable-no-effect-on-related)
  link: [Enabling or disabling a multi-Region key](../facts/kms.md#kms-mrk-disable-no-effect-on-related)
kms-mrk-independent-policies-grants-aliases
  claim: Each multi-Region key must be managed independently: aliases, tags, key policies, grants and enabled or disabled state are set per key, not shared.
  link: [manage each multi-Region key independently](../facts/kms.md#kms-mrk-independent-policies-grants-aliases)
  link: [setting their key policies and grants](../facts/kms.md#kms-mrk-independent-policies-grants-aliases)
kms-mrk-not-global-never-auto-replicated
  claim: Multi-Region keys are not global: you replicate a primary key into Regions you select within a partition, and AWS never creates or replicates multi-Region keys automatically; AWS managed keys are always single-Region keys.
  link: [Multi-Region keys are not global.](../facts/kms.md#kms-mrk-not-global-never-auto-replicated)
  link: [are always single-Region keys](../facts/kms.md#kms-mrk-not-global-never-auto-replicated)
kms-mrk-not-in-custom-key-store
  claim: You cannot create multi-Region keys in a custom key store.
  link: [You cannot create multi-Region keys](../facts/kms.md#kms-mrk-not-in-custom-key-store)
  link: [in a custom key store](../facts/kms.md#kms-mrk-not-in-custom-key-store)
kms-mrk-primary-delete-waits-for-replicas
  claim: AWS KMS does not delete a multi-Region primary key until all of its replica keys are deleted; until then the primary key is in the PendingReplicaDeletion state.
  link: [until all of its replica keys are deleted](../facts/kms.md#kms-mrk-primary-delete-waits-for-replicas)
  link: [PendingReplicaDeletion state](../facts/kms.md#kms-mrk-primary-delete-waits-for-replicas)
kms-mrk-rotation-on-primary-only
  claim: For symmetric encryption multi-Region keys with AWS_KMS origin, you enable and disable automatic rotation, and initiate on-demand rotation, only on the primary key; KMS creates new key material for the primary key and copies the new key material across Region boundaries to all related replica keys.
  scope: symmetric encryption multi-Region keys with AWS_KMS origin.
  link: [only on the primary key](../facts/kms.md#kms-mrk-rotation-on-primary-only)
  link: [copies the new key material across Region boundaries](../facts/kms.md#kms-mrk-rotation-on-primary-only)
kms-mrk-s3-crr-reencrypts
  claim: Most integrated AWS services treat multi-Region keys as single-Region keys; for example, S3 Cross-Region Replication decrypts and re-encrypts data keys under the KMS key in the destination Region even when both keys are related multi-Region keys.
  link: [decrypts and re-encrypts the data keys](../facts/kms.md#kms-mrk-s3-crr-reencrypts)
  link: [the KMS key in the destination Region](../facts/kms.md#kms-mrk-s3-crr-reencrypts)
kms-mrk-same-material-no-cross-region-call
  claim: Related multi-Region keys have the same key material and key ID, so data encrypted in one Region can be decrypted in another without re-encrypting or a cross-Region call to AWS KMS.
  link: [the same key material and key ID](../facts/kms.md#kms-mrk-same-material-no-cross-region-call)
  link: [without re-encrypting or making a cross-Region call](../facts/kms.md#kms-mrk-same-material-no-cross-region-call)
kms-mrk-use-cases
  claim: Multi-Region keys suit backup and recovery architectures (processing encrypted data through a Region outage), globally distributed data, and active-active applications that span Regions.
  link: [backup and recovery architecture](../facts/kms.md#kms-mrk-use-cases)
  link: [active-active architectures](../facts/kms.md#kms-mrk-use-cases)
kms-mrk-use-only-when-needed
  claim: AWS advises using a multi-Region key only when you need one; for most data security needs, standard single-Region keys are the best fit because of Regional isolation and fault tolerance.
  link: [only when you need one](../facts/kms.md#kms-mrk-use-only-when-needed)
  link: [a best-fit solution](../facts/kms.md#kms-mrk-use-only-when-needed)
kms-never-deletes-unless-scheduled
  claim: AWS KMS never deletes your KMS keys unless you explicitly schedule them for deletion and the mandatory waiting period expires.
  link: [never deletes your KMS keys](../facts/kms.md#kms-never-deletes-unless-scheduled)
  link: [the mandatory waiting period expires](../facts/kms.md#kms-never-deletes-unless-scheduled)
kms-no-principal-has-access-unless-allowed
  claim: No AWS principal, not even the account root user or the key creator, has permissions to a KMS key unless they are explicitly allowed, and never denied, in a key policy, IAM policy or grant.
  link: [including the account root user or key creator](../facts/kms.md#kms-no-principal-has-access-unless-allowed)
kms-on-demand-rotation-imported-symmetric
  claim: On-demand key rotation is supported on symmetric encryption KMS keys with AWS KMS key material and on symmetric encryption KMS keys with imported key material.
  link: [symmetric encryption KMS keys with imported key material](../facts/kms.md#kms-on-demand-rotation-imported-symmetric)
  link: [On-demand key rotation is supported](../facts/kms.md#kms-on-demand-rotation-imported-symmetric)
kms-on-demand-rotation-keeps-schedule
  claim: An on-demand rotation does not change the existing automatic rotation schedule of the key.
  scope: per KMS key.
  link: [do not change existing automatic rotation schedules](../facts/kms.md#kms-on-demand-rotation-keeps-schedule)
kms-pending-deletion-no-crypto-cancel-possible
  claim: During the waiting period the key state is Pending deletion and the key cannot be used in any cryptographic operation; you can cancel the deletion before the waiting period ends, but not after it.
  link: [cannot be used in any cryptographic operations](../facts/kms.md#kms-pending-deletion-no-crypto-cancel-possible)
  link: [cancel key deletion before the waiting period ends](../facts/kms.md#kms-pending-deletion-no-crypto-cancel-possible)
kms-price-key-storage-per-month
  claim: Each KMS key you create costs $1/month (prorated hourly), the same for symmetric, asymmetric, HMAC, imported, CloudHSM key store and external key store keys, and for each primary and each replica multi-Region key.
  scope: per KMS key; prorated hourly; request charges are separate.
  link: [$1/month](../facts/kms.md#kms-price-key-storage-per-month)
  link: [each primary and each replica multi-Region key](../facts/kms.md#kms-price-key-storage-per-month)
  say: one dollar a month
kms-price-rotation-capped-at-second
  claim: For a KMS key rotated automatically or on demand, the first and the second rotation each add $1/month (prorated hourly); later rotations are not billed.
  scope: per KMS key; applies to automatic and on-demand rotation.
  link: [$1/month](../facts/kms.md#kms-price-rotation-capped-at-second)
  link: [capped at the second rotation](../facts/kms.md#kms-price-rotation-capped-at-second)
  say: one dollar a month
kms-pricing-aws-managed-free-storage-requests-charged
  claim: You are not charged for creation and storage of AWS managed keys, but you are charged on any API request made to AWS managed keys.
  link: [not charged for creation and storage](../facts/kms.md#kms-pricing-aws-managed-free-storage-requests-charged)
  link: [charged on any API request](../facts/kms.md#kms-pricing-aws-managed-free-storage-requests-charged)
kms-pricing-cross-account-caller-pays
  claim: When a KMS key is used from a different AWS account, the account that makes the API request is charged for the key use.
  link: [the AWS account that makes the API request](../facts/kms.md#kms-pricing-cross-account-caller-pays)
  link: [is charged for the key use](../facts/kms.md#kms-pricing-cross-account-caller-pays)
kms-pricing-no-charge-scheduled-deletion
  claim: Customer managed KMS keys that are scheduled for deletion are not charged; if you cancel the deletion, the key is charged as though it was never scheduled.
  link: [scheduled for deletion](../facts/kms.md#kms-pricing-no-charge-scheduled-deletion)
  link: [as though it was never scheduled for deletion](../facts/kms.md#kms-pricing-no-charge-scheduled-deletion)
kms-private-ca-for-tls-certificates
  claim: For asymmetric keys used in TLS termination on web servers, load balancers, API Gateway endpoints, EC2 instances or containers, AWS suggests AWS Private CA for issuing certificates instead of raw KMS asymmetric keys.
  link: [TLS termination](../facts/kms.md#kms-private-ca-for-tls-certificates)
  link: [consider using AWS Private CA](../facts/kms.md#kms-private-ca-for-tls-certificates)
kms-quota-aliases-per-key
  claim: Each customer managed KMS key can have 50 customer created aliases by default, and the quota is adjustable.
  scope: per customer managed key, per account and Region; default; adjustable; aliases that AWS associates with AWS managed keys do not count.
  link: [50](../facts/kms.md#kms-quota-aliases-per-key)
  say: fifty
kms-quota-aliases-per-region-eliminated
  claim: KMS no longer has an aliases-per-Region quota; the per-key alias quota replaced it.
  scope: per account and Region.
  link: [eliminated the Aliases per Region quota](../facts/kms.md#kms-quota-aliases-per-region-eliminated)
kms-quota-custom-key-stores
  claim: An account can have 10 custom key stores in each Region by default, and the quota is adjustable. The quota counts all AWS CloudHSM key stores and external key stores together, regardless of their connection state.
  scope: per AWS account and Region; default; adjustable; counts AWS CloudHSM key stores and external key stores, regardless of their connection state.
  link: [10](../facts/kms.md#kms-quota-custom-key-stores)
  say: ten
kms-quota-customer-managed-keys
  claim: An account can have 100,000 customer managed KMS keys by default in each Region, and the quota is adjustable.
  scope: per AWS account, per Region; default; adjustable; AWS managed keys and AWS owned keys do not count.
  link: [100,000](../facts/kms.md#kms-quota-customer-managed-keys)
  say: one hundred thousand
kms-quota-grants-per-key
  claim: A customer managed KMS key can have 50,000 grants by default, and the quota is adjustable.
  scope: per customer managed key; default; adjustable; does not apply to AWS managed keys or AWS owned keys.
  link: [50,000](../facts/kms.md#kms-quota-grants-per-key)
  say: fifty thousand
kms-quota-on-demand-rotations-per-key
  claim: You can rotate a KMS key on demand at most 25 times, and this quota is not adjustable.
  scope: per KMS key; maximum; not adjustable; customer managed keys; cannot be raised through Service Quotas or AWS Support.
  link: [25 times](../facts/kms.md#kms-quota-on-demand-rotations-per-key)
  link: [25](../facts/kms.md#kms-quota-on-demand-rotations-per-key)
  say: twenty-five times | twenty-five
kms-quota-request-cloudhsm-key-store
  claim: Cryptographic operations on KMS keys in one AWS CloudHSM key store share a request quota of 1800 requests per second, and this quota is not adjustable.
  scope: per AWS CloudHSM key store; default; not adjustable; requests for cryptographic operations on KMS keys in a custom key store also count toward the symmetric cryptographic request quota of the account and Region.
  link: [1800](../facts/kms.md#kms-quota-request-cloudhsm-key-store)
  say: one thousand eight hundred
kms-quota-request-createkey
  claim: The CreateKey operation has a default request quota of 5 requests per second; KMS request quotas apply to all requests from the principals of an AWS account in a Region, and this quota is adjustable.
  scope: per account and Region; default; adjustable.
  link: [5](../facts/kms.md#kms-quota-request-createkey)
  say: five
kms-quota-request-ecc-crypto
  claim: Cryptographic operations with elliptic curve (ECC) and SM2 KMS keys share a default request quota of 1,000 requests per second per account and Region.
  scope: per account and Region, shared by ECC and SM2 cryptographic operations; default; adjustable; SM2 keys exist only in China Regions.
  link: [1,000](../facts/kms.md#kms-quota-request-ecc-crypto)
  say: one thousand
kms-quota-request-external-key-store
  claim: Cryptographic operations on KMS keys in one external key store count toward a request quota of 1800 requests per second for that key store by default; the custom key store quota table marks this quota as not adjustable.
  scope: per external key store; default; not adjustable; the same page's text says all KMS request quotas except the AWS CloudHSM key store quota are adjustable and mentions adjusting the external key store request quota; the table says No.
  link: [1800](../facts/kms.md#kms-quota-request-external-key-store)
  say: one thousand eight hundred
kms-quota-request-rsa-crypto
  claim: Cryptographic operations with RSA KMS keys share a default request quota of 1,000 requests per second per account and Region.
  scope: per account and Region, shared by RSA cryptographic operations; default; adjustable; RSA asymmetric KMS keys only.
  link: [1,000](../facts/kms.md#kms-quota-request-rsa-crypto)
  say: one thousand
kms-quota-request-symmetric-crypto
  claim: Cryptographic operations on symmetric KMS keys (Encrypt, Decrypt, GenerateDataKey and others) share one request quota per account and Region: 10,000 requests per second by default, 20,000 in some Regions, and 100,000 in US East (N. Virginia), US West (Oregon) and Europe (Ireland).
  scope: per account and Region, shared by all symmetric cryptographic operations; default; adjustable; value depends on the Region; requests that AWS services make on your behalf count too.
  link: [10,000](../facts/kms.md#kms-quota-request-symmetric-crypto)
  link: [20,000](../facts/kms.md#kms-quota-request-symmetric-crypto)
  link: [100,000](../facts/kms.md#kms-quota-request-symmetric-crypto)
  say: ten thousand | twenty thousand | one hundred thousand
kms-quotas-per-region-per-account
  claim: KMS resource quotas and request quotas are each calculated separately for every Region of every AWS account.
  scope: per account and Region.
  link: [for each Region of each AWS account](../facts/kms.md#kms-quotas-per-region-per-account)
kms-rcp-customer-managed-keys-guardrail
  claim: Resource control policies (RCPs) can limit permissions to customer managed KMS keys in an organization, but an RCP grants no permissions; key policies or identity-based policies still grant access.
  scope: customer managed KMS keys in an AWS Organizations organization; RCPs do not apply to AWS managed keys.
  link: [No permissions are granted by an RCP](../facts/kms.md#kms-rcp-customer-managed-keys-guardrail)
kms-rds-aws-managed-key-snapshot-no-share
  claim: You cannot share an RDS snapshot encrypted with the sharing account's AWS managed key.
  link: [can't share a snapshot](../facts/kms.md#kms-rds-aws-managed-key-snapshot-no-share)
  link: [encrypted using the AWS managed key](../facts/kms.md#kms-rds-aws-managed-key-snapshot-no-share)
kms-rds-cannot-change-key-or-disable
  claim: After an encrypted RDS DB instance is created you cannot change its KMS key, and you cannot turn off its encryption.
  link: [you can't change the KMS key](../facts/kms.md#kms-rds-cannot-change-key-or-disable)
  link: [can't turn off encryption](../facts/kms.md#kms-rds-cannot-change-key-or-disable)
kms-rds-encrypt-only-at-create-snapshot-copy
  claim: An RDS DB instance can be encrypted only when it is created; to add encryption, snapshot the instance, make an encrypted copy of the snapshot and restore from it.
  link: [only encrypt an Amazon RDS DB instance](../facts/kms.md#kms-rds-encrypt-only-at-create-snapshot-copy)
  link: [create an encrypted copy of that snapshot](../facts/kms.md#kms-rds-encrypt-only-at-create-snapshot-copy)
kms-recommend-cmk-in-kms-hsms
  claim: AWS recommends customer managed keys created and stored in the KMS HSMs; compared with keys in a CloudHSM custom key store or an external key store, they offer higher performance, lower latency and a service level agreement for cryptographic operations.
  link: [created and stored in the KMS HSMs](../facts/kms.md#kms-recommend-cmk-in-kms-hsms)
  link: [higher performance, lower latency](../facts/kms.md#kms-recommend-cmk-in-kms-hsms)
kms-requests-on-your-behalf-count
  claim: KMS throttling counts requests from all principals in the account, including requests that AWS services make on your behalf (for example S3 with SSE-KMS).
  scope: per account and Region.
  link: [including requests from AWS services on your behalf](../facts/kms.md#kms-requests-on-your-behalf-count)
kms-rotated-key-counts-once-in-quota
  claim: A rotated KMS key still counts as one key in the KMS key quota, however many key material versions it has.
  scope: per KMS key.
  link: [counts as one key](../facts/kms.md#kms-rotated-key-counts-once-in-quota)
kms-rotation-best-practice-only-if-required
  claim: The AWS KMS best-practice guide does not recommend key rotation unless you are required to rotate keys, for example by regulation, because KMS keeps earlier key material that can still decrypt data.
  link: [required to rotate keys for regulatory compliance](../facts/kms.md#kms-rotation-best-practice-only-if-required)
  link: [doesn't provide any additional security benefits](../facts/kms.md#kms-rotation-best-practice-only-if-required)
kms-rotation-default-period-365-days
  claim: When you enable automatic key rotation without a rotation period, KMS uses the default period of 365 days.
  scope: per customer managed key; default; adjustable; set a custom value with RotationPeriodInDays.
  link: [365 days](../facts/kms.md#kms-rotation-default-period-365-days)
  say: three hundred sixty-five days
kms-rotation-disabled-by-default-cmk
  claim: Automatic key rotation is disabled by default for customer managed keys; you enable it per key.
  scope: customer managed KMS keys; automatic key rotation; default; adjustable; until you enable automatic rotation for the key.
  link: [key rotation is disabled for customer managed keys](../facts/kms.md#kms-rotation-disabled-by-default-cmk)
kms-rotation-no-reencrypt-of-data
  claim: Key rotation has no effect on the data the KMS key protects: it does not rotate the data keys the KMS key generated or re-encrypt any data, and it does not mitigate a compromised data key.
  link: [has no effect on the data](../facts/kms.md#kms-rotation-no-reencrypt-of-data)
  link: [not mitigate the effect of a compromised](../facts/kms.md#kms-rotation-no-reencrypt-of-data)
kms-rotation-not-for-asymmetric-hmac-custom-store
  claim: Neither automatic nor on-demand rotation is supported for asymmetric KMS keys, HMAC KMS keys or KMS keys in custom key stores; you can rotate these keys manually.
  link: [not eligible for automatic or on-demand key rotation](../facts/kms.md#kms-rotation-not-for-asymmetric-hmac-custom-store)
  link: [asymmetric KMS keys, HMAC KMS keys](../facts/kms.md#kms-rotation-not-for-asymmetric-hmac-custom-store)
kms-rotation-only-customer-managed-symmetric
  claim: Automatic key rotation is supported only on symmetric encryption KMS keys with key material that AWS KMS generates; it is optional for customer managed keys, AWS always rotates AWS managed keys every year, and the owning service manages rotation of AWS owned keys.
  link: [Automatic rotation is optional](../facts/kms.md#kms-rotation-only-customer-managed-symmetric)
  link: [always rotates the key material](../facts/kms.md#kms-rotation-only-customer-managed-symmetric)
kms-rotation-period-range-90-2560-days
  claim: A custom automatic rotation period can be set between 90 and 2560 days.
  scope: per customer managed key; maximum; not adjustable; minimum 90 days.
  link: [between 90 and 2560 days](../facts/kms.md#kms-rotation-period-range-90-2560-days)
  link: [90](../facts/kms.md#kms-rotation-period-range-90-2560-days)
  link: [2560](../facts/kms.md#kms-rotation-period-range-90-2560-days)
  say: between ninety and two thousand five hundred sixty days | ninety | two thousand five hundred sixty
kms-rotation-recommend-auto-then-on-demand-then-manual
  claim: When you must rotate KMS keys, AWS recommends automatic rotation where supported, on-demand rotation if automatic is not supported, and manual rotation when neither is supported.
  link: [use automatic key rotation where it is supported](../facts/kms.md#kms-rotation-recommend-auto-then-on-demand-then-manual)
  link: [manual key rotation](../facts/kms.md#kms-rotation-recommend-auto-then-on-demand-then-manual)
kms-rotation-retains-old-material
  claim: AWS KMS keeps all key material of a KMS key with AWS_KMS origin, even if rotation is disabled, and deletes key material only when the KMS key is deleted.
  link: [retains all key material](../facts/kms.md#kms-rotation-retains-old-material)
  link: [deletes key material only when you delete](../facts/kms.md#kms-rotation-retains-old-material)
kms-rotation-same-logical-key-transparent
  claim: Key rotation changes only the current key material; the KMS key stays the same logical resource with the same properties, and KMS decrypts with the key material that encrypted the data, so applications and AWS services need no code changes.
  link: [changes only the current key material](../facts/kms.md#kms-rotation-same-logical-key-transparent)
  link: [without code changes](../facts/kms.md#kms-rotation-same-logical-key-transparent)
  link: [the same logical resource](../facts/kms.md#kms-rotation-same-logical-key-transparent)
kms-s3-sse-kms-put-get-permissions
  claim: To upload an object to S3 encrypted with a KMS key you need kms:GenerateDataKey on the key, and to download such an object you need kms:Decrypt on the key.
  link: [kms:GenerateDataKey permissions on the key](../facts/kms.md#kms-s3-sse-kms-put-get-permissions)
  link: [kms:Decrypt permissions for the key](../facts/kms.md#kms-s3-sse-kms-put-get-permissions)
kms-separate-key-users-and-admins
  claim: To implement role-based access control in AWS KMS, AWS recommends separating the permissions for key users and key administrators.
  link: [separating the permissions for key users](../facts/kms.md#kms-separate-key-users-and-admins)
  link: [implement RBAC](../facts/kms.md#kms-separate-key-users-and-admins)
kms-single-region-key-stays-in-region
  claim: A single-Region KMS key generated by AWS KMS is stored and used only in the Region where it was created; multi-Region keys let you replicate a primary key into other Regions of the same partition.
  link: [stored and used only in the Region](../facts/kms.md#kms-single-region-key-stays-in-region)
  link: [in which it was created](../facts/kms.md#kms-single-region-key-stays-in-region)
kms-throttling-request-quota-backoff
  claim: AWS KMS throttles requests, returning a ThrottlingException, when the rate exceeds the request quota for an account and Region; respond with a backoff and retry strategy.
  link: [returns a ThrottlingException error](../facts/kms.md#kms-throttling-request-quota-backoff)
  link: [use a backoff and retry strategy](../facts/kms.md#kms-throttling-request-quota-backoff)
kms-unusable-key-data-keys-delayed-effect
  claim: When a KMS key becomes unusable, cryptographic requests with it fail almost at once, but the effect on data keys it encrypted, and on data they encrypt, is delayed until the KMS key is used again, for example to decrypt a data key.
  link: [the effect is almost immediate](../facts/kms.md#kms-unusable-key-data-keys-delayed-effect)
  link: [delayed until the KMS key is used again](../facts/kms.md#kms-unusable-key-data-keys-delayed-effect)
kms-unusable-key-ebs-attach-fails
  claim: Making a KMS key unusable has no immediate effect on an attached encrypted EBS volume, but after the volume is detached, the next attachment fails because EBS cannot decrypt the volume's data key.
  link: [no immediate effect on the EC2 instance](../facts/kms.md#kms-unusable-key-ebs-attach-fails)
  link: [the attachment fails](../facts/kms.md#kms-unusable-key-ebs-attach-fails)
kms-vpc-endpoint-all-api-cloudtrail
  claim: Through a KMS VPC endpoint you can call all AWS KMS API operations, and CloudTrail logs let you audit use of KMS keys through the endpoint; KMS supports VPC endpoints and endpoint policies in all Regions where it is supported.
  link: [call all AWS KMS API operations](../facts/kms.md#kms-vpc-endpoint-all-api-cloudtrail)
  link: [VPC endpoints and VPC endpoint policies](../facts/kms.md#kms-vpc-endpoint-all-api-cloudtrail)
kms-vpc-endpoint-privatelink-no-igw
  claim: AWS KMS supports interface VPC endpoints powered by AWS PrivateLink; the endpoint connects your VPC to KMS without an internet gateway, NAT device, VPN or Direct Connect, and instances need no public IP addresses.
  link: [powered by AWS PrivateLink](../facts/kms.md#kms-vpc-endpoint-privatelink-no-igw)
  link: [without an internet gateway, NAT device](../facts/kms.md#kms-vpc-endpoint-privatelink-no-igw)
kms-wa-default-key-store-best-balance
  claim: Well-Architected advises that for customer managed keys the default key store gives the best balance of agility, security, data sovereignty and availability; other use cases may need CloudHSM or external custom key stores.
  link: [the best balance between agility, security](../facts/kms.md#kms-wa-default-key-store-best-balance)
  link: [consider the default key store](../facts/kms.md#kms-wa-default-key-store-best-balance)
kms-wa-encrypt-by-default-anti-pattern
  claim: Well-Architected SEC08-BP02 lists not using encrypt-by-default configurations as a common anti-pattern; its desired outcome is mechanisms that encrypt private data at rest by default.
  link: [Not using encrypt-by-default configurations.](../facts/kms.md#kms-wa-encrypt-by-default-anti-pattern)
  link: [encrypt private data by default when at rest](../facts/kms.md#kms-wa-encrypt-by-default-anti-pattern)
kms-wa-key-policies-primary-monitor-use
  claim: Well-Architected guidance says to tightly control access to keys with key policies and IAM policies, key policies being the primary way, and to monitor key use in CloudTrail, paying special attention to key destruction events.
  link: [the primary way to control access](../facts/kms.md#kms-wa-key-policies-primary-monitor-use)
  link: [monitoring key destruction events](../facts/kms.md#kms-wa-key-policies-primary-monitor-use)
kms-wa-keys-same-account-as-workload
  claim: Well-Architected SEC08-BP01 says that in a multi-account strategy you should keep KMS keys in the same account as the workload that uses them; a centralized key account needs extra cross-account policies.
  link: [in the same account as the workload](../facts/kms.md#kms-wa-keys-same-account-as-workload)
  link: [requires additional policies](../facts/kms.md#kms-wa-keys-same-account-as-workload)
kms-what-it-is-create-control-keys
  claim: AWS KMS is an AWS managed service for creating and controlling the keys used to encrypt and sign data.
  link: [create and control the keys](../facts/kms.md#kms-what-it-is-create-control-keys)
  link: [an AWS managed service](../facts/kms.md#kms-what-it-is-create-control-keys)
