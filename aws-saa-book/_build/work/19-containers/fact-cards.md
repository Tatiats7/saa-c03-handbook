facts card: 676 facts
ecr-archive-storage-class-rarely-accessed
  claim: The Amazon ECR archival storage class provides low-cost, long-term storage for container images.
  scope: Amazon ECR storage classes.
  link: [low-cost, long-term storage for container images](../facts/ecr.md#ecr-archive-storage-class-rarely-accessed)
ecr-archived-image-restore-within-20-minutes
  claim: You can expect Amazon ECR to restore an archived image to the Standard storage class within 20 minutes.
  scope: per archived image.
  link: [within 20 minutes](../facts/ecr.md#ecr-archived-image-restore-within-20-minutes)
ecr-authorization-token-permission-scope
  claim: An ECR authorization token's permission scope matches that of the IAM principal used to retrieve the authentication token.
  scope: Amazon ECR authorization token.
  link: [permission scope matches that of the IAM principal](../facts/ecr.md#ecr-authorization-token-permission-scope)
  link: [authorization token's permission scope](../facts/ecr.md#ecr-authorization-token-permission-scope)
ecr-authorization-token-valid-12-hours
  claim: An ECR authentication token can be used to access any Amazon ECR registry that your IAM principal has access to, and it is valid for 12 hours.
  scope: per authorization token; fixed; not adjustable.
  link: [12 hours](../facts/ecr.md#ecr-authorization-token-valid-12-hours)
ecr-basic-scan-100000-images-per-24-hours
  claim: With ECR basic scanning, you can scan up to 100,000 images per 24 hours in a given registry.
  scope: per registry; maximum; not adjustable.
  link: [100,000 images per 24 hours](../facts/ecr.md#ecr-basic-scan-100000-images-per-24-hours)
ecr-basic-scan-once-per-24-hours
  claim: With ECR basic scanning, an image can be scanned once per 24 hours. The 24 hours include the initial scan on push, if configured, and any manual scans.
  scope: per image; maximum; not adjustable.
  link: [once per 24 hours](../facts/ecr.md#ecr-basic-scan-once-per-24-hours)
ecr-basic-scanning-aws-native-more-than-50-feeds
  claim: Amazon ECR basic scanning uses AWS native technology to scan container images for software vulnerabilities, and it sources more than 50 data feeds to generate findings for common vulnerabilities and exposures (CVEs).
  scope: ECR basic scanning.
  link: [uses AWS native technology](../facts/ecr.md#ecr-basic-scanning-aws-native-more-than-50-feeds)
  link: [more than 50 data feeds](../facts/ecr.md#ecr-basic-scanning-aws-native-more-than-50-feeds)
ecr-batchgetimage-request-rate-quota
  claim: The default rate of BatchGetImage requests is 2,000 per second in the current Region. ECR calls BatchGetImage once per image pull to retrieve the image manifest. The quota is adjustable.
  scope: per Region, requests per second; default; adjustable.
  link: [2,000 per second](../facts/ecr.md#ecr-batchgetimage-request-rate-quota)
ecr-change-archive-storage-class-2025-11
  claim: On 19 November 2025 Amazon ECR added support for archiving images for long-term retention.
  scope: document history row.
  link: [19 November 2025](../facts/ecr.md#ecr-change-archive-storage-class-2025-11)
  link: [archiving images for long-term retention](../facts/ecr.md#ecr-change-archive-storage-class-2025-11)
ecr-change-clair-scanning-deprecation-completed-2026-02
  claim: As of 2 February 2026 Clair-based image scanning has been deprecated in Amazon ECR and all ECR accounts have been migrated to AWS native basic scanning.
  scope: document history row.
  link: [2 February 2026](../facts/ecr.md#ecr-change-clair-scanning-deprecation-completed-2026-02)
  link: [the only implementation of basic scanning](../facts/ecr.md#ecr-change-clair-scanning-deprecation-completed-2026-02)
ecr-change-ecr-to-ecr-pull-through-cache-2025-03
  claim: On Mar 12, 2025 Amazon ECR announced ECR to ECR pull through cache, a capability that automatically syncs container images between two ECR private registries across AWS Regions and accounts.
  scope: What's New post.
  link: [Mar 12, 2025](../facts/ecr.md#ecr-change-ecr-to-ecr-pull-through-cache-2025-03)
  link: [ECR to ECR pull through cache](../facts/ecr.md#ecr-change-ecr-to-ecr-pull-through-cache-2025-03)
ecr-change-image-layers-200-gb-2026-08
  claim: On Aug 3, 2026 Amazon ECR increased the maximum image layer size limit to 200 GB for images pushed via Docker push.
  scope: What's New post.
  link: [200 GB](../facts/ecr.md#ecr-change-image-layers-200-gb-2026-08)
  link: [Aug 3, 2026](../facts/ecr.md#ecr-change-image-layers-200-gb-2026-08)
ecr-change-managed-signing-2025-11
  claim: On 21 November 2025 Amazon ECR added managed container image signing, which lets you verify that images are from trusted sources.
  scope: document history row.
  link: [21 November 2025](../facts/ecr.md#ecr-change-managed-signing-2025-11)
  link: [managed container image signing](../facts/ecr.md#ecr-change-managed-signing-2025-11)
ecr-change-private-registry-pull-through-cache-2025-03
  claim: On 12 March 2025 Amazon ECR added support for creating pull through cache rules for the Amazon ECR private registry.
  scope: document history row.
  link: [12 March 2025](../facts/ecr.md#ecr-change-private-registry-pull-through-cache-2025-03)
  link: [creating pull through cache rules](../facts/ecr.md#ecr-change-private-registry-pull-through-cache-2025-03)
ecr-credential-helper-no-mfa
  claim: Amazon ECR provides a Docker credential helper that makes it easier to store and use Docker credentials when pushing and pulling images, but the helper does not currently support multi-factor authentication (MFA).
  scope: Amazon ECR credential helper.
  link: [a Docker credential helper](../facts/ecr.md#ecr-credential-helper-no-mfa)
  link: [doesn't support multi-factor authentication (MFA) currently](../facts/ecr.md#ecr-credential-helper-no-mfa)
ecr-default-private-registry-per-account
  claim: Each AWS account is provided with a default private Amazon ECR registry, and its repositories can be replicated across AWS Regions and across separate accounts by configuring replication.
  scope: Amazon ECR private registry; default; not adjustable.
  link: [a default private Amazon ECR registry](../facts/ecr.md#ecr-default-private-registry-per-account)
  link: [replicated across AWS Regions](../facts/ecr.md#ecr-default-private-registry-per-account)
ecr-docker-cli-needs-token-get-login-password
  claim: The Docker CLI doesn't support native IAM authentication methods, so additional steps must be taken so that Amazon ECR can authenticate and authorize Docker push and pull requests; to authenticate Docker to an Amazon ECR registry with get-login-password, you run the aws ecr get-login-password command.
  scope: Amazon ECR private registry authentication.
  link: [doesn't support native IAM authentication methods](../facts/ecr.md#ecr-docker-cli-needs-token-get-login-password)
  link: [**aws ecr get-login-password**](../facts/ecr.md#ecr-docker-cli-needs-token-get-login-password)
ecr-dsse-kms-only-govcloud
  claim: Dual-layer server-side encryption with AWS KMS (DSSE-KMS) for Amazon ECR is only available in the AWS GovCloud (US) Regions.
  scope: Amazon ECR encryption.
  link: [only available in the AWS GovCloud (US) Regions](../facts/ecr.md#ecr-dsse-kms-only-govcloud)
  link: [Dual-layer server-side encryption with AWS KMS (DSSE-KMS)](../facts/ecr.md#ecr-dsse-kms-only-govcloud)
ecr-ecs-agent-pull-permissions
  claim: For Amazon ECS tasks to pull container images and artifacts that you host in Amazon ECR private repositories, the Amazon ECS or Fargate container agent must have permissions to make the ecr:BatchGetImage, ecr:GetDownloadUrlForLayer, and ecr:GetAuthorizationToken APIs.
  scope: Amazon ECS with Amazon ECR.
  link: [`ecr:BatchGetImage`, `ecr:GetDownloadUrlForLayer`, and `ecr:GetAuthorizationToken` APIs](../facts/ecr.md#ecr-ecs-agent-pull-permissions)
  link: [container agent must have permissions](../facts/ecr.md#ecr-ecs-agent-pull-permissions)
ecr-eks-image-name-full-registry-repository-tag
  claim: When referencing an image from Amazon ECR in Amazon EKS, you must use the full registry/repository:tag naming for the image.
  scope: Amazon EKS with Amazon ECR.
  link: [the full `registry/repository:tag` naming](../facts/ecr.md#ecr-eks-image-name-full-registry-repository-tag)
  link: [referencing an image from Amazon ECR](../facts/ecr.md#ecr-eks-image-name-full-registry-repository-tag)
ecr-encryption-default-sse-s3-aes256
  claim: Amazon ECR stores images in Amazon S3 buckets that Amazon ECR manages; by default it uses server-side encryption with Amazon S3-managed encryption keys, which encrypts your data at rest with an AES-256 encryption algorithm, requires no action on your part and is offered at no additional charge. For more control over encryption, you can use server-side encryption with KMS keys stored in AWS Key Management Service (AWS KMS).
  scope: Amazon ECR repositories; default; adjustable.
  link: [server-side encryption with Amazon S3-managed encryption keys](../facts/ecr.md#ecr-encryption-default-sse-s3-aes256)
  link: [AES-256 encryption algorithm](../facts/ecr.md#ecr-encryption-default-sse-s3-aes256)
  link: [offered at no additional charge](../facts/ecr.md#ecr-encryption-default-sse-s3-aes256)
ecr-encryption-kms-options-per-repository
  claim: For more control you can use server-side encryption with AWS KMS keys, either the default AWS managed key or your own customer managed key; each repository has its own encryption configuration, which is set when the repository is created.
  scope: Amazon ECR repositories; encryption configuration is set when the repository is created.
  link: [server-side encryption with KMS keys](../facts/ecr.md#ecr-encryption-kms-options-per-repository)
  link: [set when the repository is created](../facts/ecr.md#ecr-encryption-kms-options-per-repository)
ecr-encryption-settings-cannot-change-after-creation
  claim: The encryption settings of an Amazon ECR repository cannot be changed once the repository is created; in the console they are a view-only field when you edit the repository.
  scope: Amazon ECR private repositories; after repository creation.
  link: [can't be changed once the repository is created](../facts/ecr.md#ecr-encryption-settings-cannot-change-after-creation)
ecr-enhanced-scanning-inspector-cost
  claim: There is no additional cost from Amazon ECR to use enhanced scanning, however there is a cost from Amazon Inspector to scan your images.
  scope: Amazon ECR enhanced scanning.
  link: [no additional cost from Amazon ECR](../facts/ecr.md#ecr-enhanced-scanning-inspector-cost)
  link: [a cost from Amazon Inspector](../facts/ecr.md#ecr-enhanced-scanning-inspector-cost)
ecr-enhanced-scanning-no-manual-scans
  claim: Manual scans using enhanced scanning aren't supported; with enhanced scanning you choose which repositories are scanned on push and which are scanned continuously by setting scan filters.
  scope: Amazon ECR enhanced scanning.
  link: [Manual scans using enhanced scanning aren’t supported](../facts/ecr.md#ecr-enhanced-scanning-no-manual-scans)
  link: [setting scan filters](../facts/ecr.md#ecr-enhanced-scanning-no-manual-scans)
ecr-faq-basic-scan-and-inspector-enhanced-scan
  claim: Amazon ECR can automatically scan container images for operating system vulnerabilities, and for enhanced image scanning you can turn on Amazon Inspector.
  scope: Amazon ECR image scanning.
  link: [turn on Amazon Inspector](../facts/ecr.md#ecr-faq-basic-scan-and-inspector-enhanced-scan)
ecr-faq-cloudtrail-history-of-pulls
  claim: AWS CloudTrail on Amazon ECR gives a history of all API actions, such as who pulled an image and when tags were moved between images.
  scope: Amazon ECR.
  link: [AWS CloudTrail](../facts/ecr.md#ecr-faq-cloudtrail-history-of-pulls)
ecr-faq-cross-account-image-sharing-by-policy
  claim: Amazon ECR images can be shared across AWS accounts; the ECR FAQ gives an example of how to create and set a policy for cross-account image sharing.
  scope: Amazon ECR repositories.
  link: [cross-account image sharing](../facts/ecr.md#ecr-faq-cross-account-image-sharing-by-policy)
ecr-faq-cross-region-pull-latency-and-transfer-cost
  claim: Pulling images between Regions or out to the internet has additional latency and data transfer costs.
  scope: Amazon ECR image pulls across Regions or to the internet.
  link: [additional latency and data transfer costs](../facts/ecr.md#ecr-faq-cross-region-pull-latency-and-transfer-cost)
ecr-faq-does-not-build-images-from-dockerfile
  claim: Amazon ECR does not automatically build images from a Dockerfile, but it integrates with popular CI/CD solutions that do.
  scope: Amazon ECR.
  link: [integrates with a number of popular CI/CD solutions](../facts/ecr.md#ecr-faq-does-not-build-images-from-dockerfile)
ecr-faq-encrypted-at-rest-and-in-transit
  claim: Amazon ECR automatically encrypts images at rest using Amazon S3 server-side encryption or AWS KMS encryption, and transfers images over HTTPS.
  scope: Amazon ECR.
  link: [Amazon S3 server-side encryption or AWS KMS encryption](../facts/ecr.md#ecr-faq-encrypted-at-rest-and-in-transit)
  link: [over HTTPS](../facts/ecr.md#ecr-faq-encrypted-at-rest-and-in-transit)
ecr-faq-iam-federated-access
  claim: Amazon ECR is integrated with IAM, which supports identity federation for delegated access to the AWS Management Console or AWS APIs.
  scope: Amazon ECR.
  link: [identity federation for delegated access](../facts/ecr.md#ecr-faq-iam-federated-access)
ecr-faq-images-stored-in-s3
  claim: Amazon ECR uses Amazon S3 for storage to make container images highly available and accessible.
  scope: Amazon ECR.
  link: [Amazon Simple Storage Service (S3) for storage](../facts/ecr.md#ecr-faq-images-stored-in-s3)
ecr-faq-integrated-with-ecs-eks-lambda
  claim: Amazon ECR is integrated with Amazon ECS, Amazon EKS and AWS Lambda.
  scope: Amazon ECR.
  link: [integrated with Amazon Elastic Container Service](../facts/ecr.md#ecr-faq-integrated-with-ecs-eks-lambda)
ecr-faq-oci-compatible
  claim: Amazon ECR is compatible with the Open Container Initiative image specification, so you can push and pull OCI images and artifacts.
  scope: Amazon ECR.
  link: [Open Container Initiative (OCI) image specification](../facts/ecr.md#ecr-faq-oci-compatible)
ecr-faq-pricing-storage-and-internet-transfer
  claim: Amazon ECR has no upfront fees or commitments; you pay only for the data you store in public or private repositories and for data transferred to the internet.
  scope: Amazon ECR.
  link: [the amount of data you store](../facts/ecr.md#ecr-faq-pricing-storage-and-internet-transfer)
  link: [no upfront fees or commitments](../facts/ecr.md#ecr-faq-pricing-storage-and-internet-transfer)
ecr-faq-private-vs-public-repository
  claim: A private ECR repository requires IAM-based authentication with AWS account credentials before images can be pulled, while a public repository lets anyone anywhere pull images without an AWS account or IAM credentials.
  scope: Amazon ECR repositories.
  link: [requires Amazon IAM-based authentication](../facts/ecr.md#ecr-faq-private-vs-public-repository)
  link: [anyone anywhere to pull images](../facts/ecr.md#ecr-faq-private-vs-public-repository)
ecr-faq-privatelink-pull-without-public-internet
  claim: You can set up AWS PrivateLink endpoints so instances in a VPC pull images from private ECR repositories without traversing the public internet.
  scope: Amazon ECR private repositories.
  link: [AWS PrivateLink endpoints](../facts/ecr.md#ecr-faq-privatelink-pull-without-public-internet)
ecr-faq-public-gallery-anyone-can-download
  claim: Anyone, with or without an AWS account, can use the Amazon ECR public gallery to search for and download commonly used container images, such as operating systems and AWS published images, and files such as Helm charts for Kubernetes.
  scope: Amazon ECR public repositories.
  link: [Amazon ECR public gallery](../facts/ecr.md#ecr-faq-public-gallery-anyone-can-download)
ecr-faq-public-repository-unique-alias-per-account
  claim: You publish an image to the Amazon ECR public gallery by pushing to a public repository you create, and each account is assigned a unique alias used in the URLs of all its public images.
  scope: Amazon ECR public gallery, per account.
  link: [a unique alias per account](../facts/ecr.md#ecr-faq-public-repository-unique-alias-per-account)
ecr-faq-regional-service
  claim: Amazon ECR is a Regional service.
  scope: Amazon ECR.
  link: [Regional service](../facts/ecr.md#ecr-faq-regional-service)
ecr-faq-replicates-across-regions-and-accounts
  claim: Amazon ECR can automatically replicate images pushed in one Region to other Regions and accounts, for deployment to multi-Region clusters.
  scope: Amazon ECR replication.
  link: [automatically replicate them to other Regions and accounts](../facts/ecr.md#ecr-faq-replicates-across-regions-and-accounts)
ecr-faq-resource-based-policies-for-access
  claim: You can use IAM resource-based policies, which you create for your Amazon ECR repositories, to control and monitor who and what (for example, EC2 instances) can access your container images, and how, when and where they can access them.
  scope: Amazon ECR repositories.
  link: [IAM resource-based policies](../facts/ecr.md#ecr-faq-resource-based-policies-for-access)
ecr-faq-use-anywhere-docker-runs
  claim: You can access Amazon ECR anywhere that Docker runs, such as desktops and on-premises environments.
  scope: Amazon ECR.
  link: [anywhere that Docker runs](../facts/ecr.md#ecr-faq-use-anywhere-docker-runs)
ecr-filters-per-replication-rule-limit
  claim: One rule in an ECR replication configuration can have at most 100 filters. The quota is not adjustable.
  scope: per replication rule, per Region; maximum; not adjustable.
  link: [100 filters](../facts/ecr.md#ecr-filters-per-replication-rule-limit)
ecr-free-tier-private-500-mb-for-one-year
  claim: A new Amazon ECR customer gets 500 MB per month of storage for private repositories for one year as part of the AWS Free Tier.
  scope: per new customer; fixed; for one year.
  link: [500 MB per month of storage](../facts/ecr.md#ecr-free-tier-private-500-mb-for-one-year)
ecr-free-tier-public-50-gb-always-free
  claim: New and existing customers get 50 GB per month of always-free storage for public ECR repositories.
  scope: per customer; fixed.
  link: [50 GB per month of always-free storage](../facts/ecr.md#ecr-free-tier-public-50-gb-always-free)
ecr-free-tier-public-transfer-5-tb-authenticated
  claim: With an AWS account, you can transfer 5 TB of data per month to the internet from a public ECR repository for free. Anonymous users can transfer 500 GB per month for free.
  scope: per customer, per month; fixed.
  link: [5 TB of data](../facts/ecr.md#ecr-free-tier-public-transfer-5-tb-authenticated)
  link: [500 GB of data](../facts/ecr.md#ecr-free-tier-public-transfer-5-tb-authenticated)
ecr-get-authorization-token-requires-iam-policy
  claim: Amazon ECR requires that users have permission to call ecr:GetAuthorizationToken through an IAM policy before they can authenticate to a registry and push or pull images from any Amazon ECR repository.
  scope: Amazon ECR authentication; through an IAM policy.
  link: [the `ecr:GetAuthorizationToken` API through an IAM policy](../facts/ecr.md#ecr-get-authorization-token-requires-iam-policy)
  link: [before they can authenticate to a registry](../facts/ecr.md#ecr-get-authorization-token-requires-iam-policy)
ecr-getauthorizationtoken-request-rate-quota
  claim: The default rate of GetAuthorizationToken requests is 500 per second in the current Region. The quota is adjustable.
  scope: per Region, requests per second; default; adjustable.
  link: [500 per second](../facts/ecr.md#ecr-getauthorizationtoken-request-rate-quota)
ecr-getdownloadurlforlayer-request-rate-quota
  claim: The default rate of GetDownloadUrlForLayer requests is 3,000 per second in the current Region. ECR calls this API once per image layer that is not already cached when an image is pulled. The quota is adjustable.
  scope: per Region, requests per second; default; adjustable.
  link: [3,000 per second](../facts/ecr.md#ecr-getdownloadurlforlayer-request-rate-quota)
ecr-images-per-repository-quota
  claim: One ECR repository can hold 100,000 images by default. The quota is adjustable.
  scope: per repository, per Region; default; adjustable.
  link: [100,000 images](../facts/ecr.md#ecr-images-per-repository-quota)
ecr-lifecycle-count-more-than-and-since-pushed
  claim: A lifecycle rule with countType imageCountMoreThan keeps the youngest images and expires or archives all images beyond the specified count, while sinceImagePushed expires or archives images older than the specified number of days.
  scope: Amazon ECR lifecycle policy rules.
  link: [greater than the specified count are expired](../facts/ecr.md#ecr-lifecycle-count-more-than-and-since-pushed)
  link: [older than the specified number of days](../facts/ecr.md#ecr-lifecycle-count-more-than-and-since-pushed)
ecr-lifecycle-policy-expires-images-within-24-hours
  claim: Amazon ECR lifecycle policies provide more control over the lifecycle management of images in a private repository; once a lifecycle policy is applied to a repository, you should expect images to become expired within 24 hours after they meet the expiration criteria, and you should use the lifecycle policy preview to confirm which images the policy expires before applying it.
  scope: Amazon ECR private repositories.
  link: [more control over the lifecycle management of images](../facts/ecr.md#ecr-lifecycle-policy-expires-images-within-24-hours)
  link: [images become expired within 24 hours after they meet the expiration criteria](../facts/ecr.md#ecr-lifecycle-policy-expires-images-within-24-hours)
ecr-lifecycle-policy-length-limit
  claim: An ECR lifecycle policy can have at most 30,720 characters. The quota is not adjustable.
  scope: per lifecycle policy, per Region; maximum; not adjustable.
  link: [30,720 characters](../facts/ecr.md#ecr-lifecycle-policy-length-limit)
ecr-lifecycle-tag-pattern-or-prefix-not-both
  claim: An ECR lifecycle policy rule may specify either tagPatternList or tagPrefixList, but not both, and these parameters may only be used if the tagStatus is tagged.
  scope: Amazon ECR lifecycle policy rules.
  link: [either `tagPatternList` or `tagPrefixList`, but not both](../facts/ecr.md#ecr-lifecycle-tag-pattern-or-prefix-not-both)
  link: [may only used if the `tagStatus` is `tagged`](../facts/ecr.md#ecr-lifecycle-tag-pattern-or-prefix-not-both)
ecr-managed-container-image-registry
  claim: Amazon ECR is an AWS managed container image registry service that is secure, scalable, and reliable.
  scope: Amazon ECR.
  link: [AWS managed container image registry service](../facts/ecr.md#ecr-managed-container-image-registry)
  link: [secure, scalable, and reliable](../facts/ecr.md#ecr-managed-container-image-registry)
ecr-managed-signing-aws-signer
  claim: Amazon ECR managed signing automatically signs your container images with AWS Signer when images are pushed, which removes the need for client-side signing tools and lets you govern signing centrally as a registry configuration.
  scope: Amazon ECR managed signing.
  link: [automatically signs your container images](../facts/ecr.md#ecr-managed-signing-aws-signer)
  link: [centrally govern signing as a registry configuration](../facts/ecr.md#ecr-managed-signing-aws-signer)
ecr-migrate-one-time-copy-no-auto-update
  claim: Where ECR pull through cache is not supported, you can perform a one-time copy of container images from an external registry into your Amazon ECR private registry; Amazon ECR stores the image version you copied, and newer versions from the source registry are not pulled automatically.
  scope: Amazon ECR migration.
  link: [a one-time copy of container images](../facts/ecr.md#ecr-migrate-one-time-copy-no-auto-update)
  link: [are not pulled automatically](../facts/ecr.md#ecr-migrate-one-time-copy-no-auto-update)
ecr-pricing-dimensions-storage-transfer-actions
  claim: With Amazon ECR you pay for the amount of data you store in your repositories, data transfer from your image pushes and pulls, and image actions that you opt in to such as image signing and replication.
  scope: Amazon ECR.
  link: [the amount of data you store](../facts/ecr.md#ecr-pricing-dimensions-storage-transfer-actions)
  link: [data transfer from your image pushes and pulls](../facts/ecr.md#ecr-pricing-dimensions-storage-transfer-actions)
  link: [image actions that you opt in to](../facts/ecr.md#ecr-pricing-dimensions-storage-transfer-actions)
ecr-pricing-same-region-transfer-free
  claim: Data transferred between Amazon ECR and other services within the same Region, such as Amazon EC2, AWS Lambda or AWS Fargate, is free of charge. Data transferred between Amazon ECR and other services in different Regions is charged at internet data transfer rates on both sides.
  scope: per transfer, same Region; same Region.
  link: [is free of charge](../facts/ecr.md#ecr-pricing-same-region-transfer-free)
ecr-private-repositories-iam-resource-based-permissions
  claim: Amazon ECR supports private repositories with resource-based permissions using AWS IAM, and you can push, pull and manage Docker images, OCI images and OCI compatible artifacts with your preferred CLI.
  scope: Amazon ECR.
  link: [private repositories with resource-based permissions using AWS IAM](../facts/ecr.md#ecr-private-repositories-iam-resource-based-permissions)
  link: [OCI compatible artifacts](../facts/ecr.md#ecr-private-repositories-iam-resource-based-permissions)
ecr-privatelink-no-internet-gateway-needed
  claim: With an interface VPC endpoint powered by AWS PrivateLink, network traffic between your VPC and Amazon ECR stays on the Amazon network, and you don't need an internet gateway, a NAT device, or a virtual private gateway.
  scope: Amazon ECR interface VPC endpoints.
  link: [to the Amazon network](../facts/ecr.md#ecr-privatelink-no-internet-gateway-needed)
  link: [You don't need an internet gateway](../facts/ecr.md#ecr-privatelink-no-internet-gateway-needed)
ecr-pull-through-cache-keeps-cache-current
  claim: With a pull through cache rule Amazon ECR caches repositories of an upstream registry in your private registry and periodically reaches out to the upstream registry to ensure the cached image is up to date.
  scope: Amazon ECR private registry.
  link: [cache repositories in an upstream registry](../facts/ecr.md#ecr-pull-through-cache-keeps-cache-current)
  link: [periodically reach out to the upstream registry](../facts/ecr.md#ecr-pull-through-cache-keeps-cache-current)
ecr-pull-through-cache-revalidation-24-hours
  claim: When a customer pulls a cached image through the Amazon ECR private registry URI, Amazon ECR checks whether it has validated the image against the upstream registry within the last 24 hours; if the 24-hour window has expired, Amazon ECR sends a request upstream to check for a newer version and updates the cache if one exists.
  scope: per cached image.
  link: [within the last 24 hours](../facts/ecr.md#ecr-pull-through-cache-revalidation-24-hours)
ecr-pull-through-cache-rules-per-registry-limit
  claim: An ECR registry can have at most 50 pull-through cache rules. The quota is not adjustable.
  scope: per registry, per Region; maximum; not adjustable.
  link: [50 pull-through cache rules](../facts/ecr.md#ecr-pull-through-cache-rules-per-registry-limit)
ecr-pull-through-cache-upstream-registries-auth
  claim: Amazon ECR currently supports creating pull through cache rules for these upstream registries: Amazon ECR Public, the Kubernetes container image registry and Quay, which don't require authentication; Docker Hub, Microsoft Azure Container Registry, GitHub Container Registry, GitLab Container Registry and Chainguard Registry, which require authentication with an AWS Secrets Manager secret; and Amazon ECR, which requires authentication with an AWS IAM role.
  scope: Amazon ECR pull through cache.
  link: [Quay (doesn't require authentication)](../facts/ecr.md#ecr-pull-through-cache-upstream-registries-auth)
  link: [requires authentication with AWS Secrets Manager secret](../facts/ecr.md#ecr-pull-through-cache-upstream-registries-auth)
  link: [Amazon ECR (requires authentication with AWS IAM role)](../facts/ecr.md#ecr-pull-through-cache-upstream-registries-auth)
ecr-putimage-request-rate-quota
  claim: The default rate of PutImage requests is 10 per second in the current Region. ECR calls PutImage once per image push to create or update the image manifest and tags. The quota is adjustable.
  scope: per Region, requests per second; default; adjustable.
  link: [10 per second](../facts/ecr.md#ecr-putimage-request-rate-quota)
ecr-registered-repositories-quota
  claim: An account can create 100,000 repositories in the current Region by default. The quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [100,000 repositories](../facts/ecr.md#ecr-registered-repositories-quota)
ecr-registry-policy-private-registry-level
  claim: Amazon ECR uses a registry policy to grant permissions to an AWS principal at the private registry level, for actions such as replication configuration, pull-through cache rule creation, and repository creation.
  scope: Amazon ECR private registry.
  link: [at the private registry level](../facts/ecr.md#ecr-registry-policy-private-registry-level)
  link: [pull-through cache rule creation, and repository creation](../facts/ecr.md#ecr-registry-policy-private-registry-level)
ecr-replication-config-25-destinations-25-rules
  claim: The replication configuration of a private ECR registry may contain up to 25 unique destinations across all rules, with a maximum of 25 rules in total. Each rule may contain up to 100 filters.
  scope: per private registry; maximum; not adjustable.
  link: [up to 25 unique destinations](../facts/ecr.md#ecr-replication-config-25-destinations-25-rules)
  link: [a maximum of 25 rules total](../facts/ecr.md#ecr-replication-config-25-destinations-25-rules)
  link: [up to 100 filters](../facts/ecr.md#ecr-replication-config-25-destinations-25-rules)
ecr-replication-cross-region-cross-account
  claim: Amazon ECR supports both cross-Region and cross-account replication of a private registry, and for cross-account replication the destination account must configure a registry permissions policy that allows replication from the source registry.
  scope: Amazon ECR private registry replication.
  link: [Amazon ECR supports both cross-Region and cross-account replication](../facts/ecr.md#ecr-replication-cross-region-cross-account)
  link: [must configure a registry permissions policy](../facts/ecr.md#ecr-replication-cross-region-cross-account)
ecr-replication-destination-account-policy-only
  claim: Cross-account ECR replication requires policy configuration on the destination account only; the source account does not require any special repository or registry policies.
  scope: Amazon ECR cross-account replication.
  link: [requires policy configuration on the **destination account only**](../facts/ecr.md#ecr-replication-destination-account-policy-only)
  link: [The source account does not require](../facts/ecr.md#ecr-replication-destination-account-policy-only)
ecr-replication-most-images-under-30-minutes
  claim: The majority of images replicate in less than 30 minutes, but in rare cases the replication might take longer.
  scope: per replicated image.
  link: [less than 30 minutes](../facts/ecr.md#ecr-replication-most-images-under-30-minutes)
ecr-replication-only-new-pushes
  claim: Only repository content pushed or restored to a repository after replication is configured is replicated; preexisting content in a repository is not replicated.
  scope: Amazon ECR private registry replication.
  link: [after replication is configured is replicated](../facts/ecr.md#ecr-replication-only-new-pushes)
  link: [Any preexisting content in a repository isn't replicated](../facts/ecr.md#ecr-replication-only-new-pushes)
ecr-replication-rules-per-registry-limit
  claim: The replication configuration of a private ECR registry can have at most 25 rules, and the quota is not adjustable. On Aug 17, 2026 the maximum rose from 10 replication rules per registry to 25.
  scope: per registry, per Region; maximum; not adjustable.
  link: [25 rules](../facts/ecr.md#ecr-replication-rules-per-registry-limit)
  changed: 2026-08-17: was 10 replication rules per registry
ecr-repository-logical-collection-of-images
  claim: A repository in Amazon ECR is a logical collection where you store your Docker images, OCI images and other OCI-compatible artifacts, and a registry can hold multiple repositories to organize your container images.
  scope: Amazon ECR.
  link: [a logical collection where you can store](../facts/ecr.md#ecr-repository-logical-collection-of-images)
  link: [you can have multiple repositories](../facts/ecr.md#ecr-repository-logical-collection-of-images)
ecr-repository-policy-default-account-only
  claim: By default, only the AWS account that created an Amazon ECR repository has access to the repository; you can apply a repository policy that allows additional access to your repository.
  scope: Amazon ECR repositories; default; adjustable.
  link: [only the AWS account that created the repository](../facts/ecr.md#ecr-repository-policy-default-account-only)
  link: [a repository policy that allows additional access](../facts/ecr.md#ecr-repository-policy-default-account-only)
ecr-repository-policy-vs-iam-policy-evaluation
  claim: ECR repository policies are a subset of IAM policies scoped to individual repositories; if an action is allowed by one policy type but denied by the other, the action is denied, and a user or role needs permission for an action through only one of them for the action to be allowed. However, Amazon ECR requires that users have permission to call the ecr:GetAuthorizationToken API through an IAM policy before they can authenticate to a registry and push or pull any images.
  scope: Amazon ECR repository access.
  link: [repository policies are a subset of IAM policies](../facts/ecr.md#ecr-repository-policy-vs-iam-policy-evaluation)
  link: [the action will be denied](../facts/ecr.md#ecr-repository-policy-vs-iam-policy-evaluation)
  link: [either a repository policy or an IAM policy](../facts/ecr.md#ecr-repository-policy-vs-iam-policy-evaluation)
ecr-rules-per-lifecycle-policy-limit
  claim: An ECR lifecycle policy can have at most 50 rules. The quota is not adjustable.
  scope: per lifecycle policy, per Region; maximum; not adjustable.
  link: [50 rules](../facts/ecr.md#ecr-rules-per-lifecycle-policy-limit)
ecr-scan-on-push-each-new-image
  claim: Each ECR repository can be configured to scan on push, which ensures that each new image pushed to the repository is scanned, and you can then retrieve the results of the image scan.
  scope: Amazon ECR repositories.
  link: [configured to **scan on push**](../facts/ecr.md#ecr-scan-on-push-each-new-image)
  link: [each new image pushed to the repository](../facts/ecr.md#ecr-scan-on-push-each-new-image)
ecr-scanning-basic-vs-enhanced
  claim: Enhanced scanning integrates Amazon ECR with Amazon Inspector for automated, continuous scanning of both operating system and programming language package vulnerabilities, while basic scanning uses the CVE database to scan operating system vulnerabilities on push or manually.
  scope: Amazon ECR image scanning.
  link: [automated, continuous scanning of your repositories](../facts/ecr.md#ecr-scanning-basic-vs-enhanced)
  link: [scan for operating system vulnerabilities](../facts/ecr.md#ecr-scanning-basic-vs-enhanced)
ecr-tag-immutability-prevent-overwrite
  claim: You can prevent image tags from being overwritten by turning on tag immutability in an ECR repository. In the console setting for Immutable, you can also enter tag names or wildcards in the Immutable tag exclusion text box to enable tag updates for a few immutable tags.
  scope: Amazon ECR private repositories; the exclusion box is described in the console steps (Setting image tag mutability, AWS Management Console); the overview sentence of the same page still says tag immutability affects all tags.
  link: [prevent image tags from being overwritten](../facts/ecr.md#ecr-tag-immutability-prevent-overwrite)
  link: [Immutable tag exclusion](../facts/ecr.md#ecr-tag-immutability-prevent-overwrite)
ecr-tags-per-image-limit
  claim: One ECR image can have at most 1,000 tags. The quota is not adjustable.
  scope: per image, per Region; maximum; not adjustable.
  link: [1,000 tags](../facts/ecr.md#ecr-tags-per-image-limit)
ecr-vpc-endpoint-security-group-port-443
  claim: The security group attached to the ECR VPC endpoint must allow incoming connections on port 443 from the private subnet of the VPC.
  scope: Amazon ECR interface VPC endpoints.
  link: [must allow incoming connections on port 443](../facts/ecr.md#ecr-vpc-endpoint-security-group-port-443)
  link: [from the private subnet of the VPC](../facts/ecr.md#ecr-vpc-endpoint-security-group-port-443)
ecr-vpc-endpoints-fargate-need-ecr-and-s3
  claim: Amazon ECS tasks on Fargate using platform version 1.4.0 or later require both the Amazon ECR VPC endpoints and the Amazon S3 gateway endpoint, and tasks on Amazon EC2 instances also require both the Amazon ECR endpoints and the Amazon S3 gateway endpoint.
  scope: Amazon ECR interface VPC endpoints; Fargate platform version 1.4.0 or later.
  link: [require both Amazon ECR VPC endpoints](../facts/ecr.md#ecr-vpc-endpoints-fargate-need-ecr-and-s3)
  link: [the Amazon S3 gateway endpoint](../facts/ecr.md#ecr-vpc-endpoints-fargate-need-ecr-and-s3)
ecs-alb-recommended-for-services
  claim: AWS recommends Application Load Balancers for ECS services to take advantage of the latest features, unless the service requires a feature that is only available with Network Load Balancers or Gateway Load Balancers.
  scope: Amazon ECS services.
  link: [We recommend that you use Application Load Balancers](../facts/ecs.md#ecs-alb-recommended-for-services)
  link: [only available with Network Load Balancers](../facts/ecs.md#ecs-alb-recommended-for-services)
ecs-anywhere-external-instances-outbound-workloads
  claim: Amazon ECS Anywhere registers an external instance, such as an on-premises server or virtual machine, to your Amazon ECS cluster; external instances are optimized for applications that generate outbound traffic or process data, and applications that need inbound traffic run less efficiently because there is no Elastic Load Balancing support.
  scope: Amazon ECS Anywhere external instances.
  link: [registering an *external instance*](../facts/ecs-anywhere.md#ecs-anywhere-external-instances-outbound-workloads)
  link: [generate outbound traffic or process data](../facts/ecs-anywhere.md#ecs-anywhere-external-instances-outbound-workloads)
ecs-anywhere-external-launch-type
  claim: Amazon ECS added an EXTERNAL launch type that you use to create services or run tasks on your external instances.
  scope: Amazon ECS Anywhere.
  link: [new `EXTERNAL` launch type](../facts/ecs-anywhere.md#ecs-anywhere-external-launch-type)
  link: [run tasks on your external instances](../facts/ecs-anywhere.md#ecs-anywhere-external-launch-type)
ecs-anywhere-faq-activation-key-registers-up-to-1000
  claim: One ECS Anywhere activation key, which is configurable, can be used to register from 1 up to 1,000 VMs or bare metal servers.
  scope: per activation key; maximum; not adjustable.
  link: [up to 1,000 VMs or bare metal servers](../facts/ecs-anywhere.md#ecs-anywhere-faq-activation-key-registers-up-to-1000)
ecs-anywhere-faq-cloudwatch-and-task-roles-integrations
  claim: With ECS Anywhere you can use task IAM roles and task execution roles to give containerized applications fine-grained access control to AWS resources.
  scope: Amazon ECS Anywhere.
  link: [Task IAM Roles and Task Execution Roles](../facts/ecs-anywhere.md#ecs-anywhere-faq-cloudwatch-and-task-roles-integrations)
ecs-anywhere-faq-container-contents-not-sent-to-control-plane
  claim: The contents of container memory, disk storage and network traffic are not sent to the ECS control plane.
  scope: Amazon ECS Anywhere.
  link: [are not sent to the control plane](../facts/ecs-anywhere.md#ecs-anywhere-faq-container-contents-not-sent-to-control-plane)
ecs-anywhere-faq-disconnected-tasks-keep-running
  claim: If network connectivity between the ECS agent on the on-premises compute and the in-region ECS control plane is lost, existing ECS tasks continue to run as usual.
  scope: Amazon ECS Anywhere; loss of connectivity to the control plane.
  link: [existing ECS tasks will continue to run](../facts/ecs-anywhere.md#ecs-anywhere-faq-disconnected-tasks-keep-running)
ecs-anywhere-faq-gpu-flag-enable-gpu
  claim: You can enable GPU instances for ECS Anywhere by adding the --enable-gpu flag to the installation script.
  scope: Amazon ECS Anywhere.
  link: [--enable-gpu flag](../facts/ecs-anywhere.md#ecs-anywhere-faq-gpu-flag-enable-gpu)
ecs-anywhere-faq-link-encrypted-with-tls
  claim: The ECS agent uses the AWS Systems Manager Agent to establish trust between the on-premises server and the ECS control plane, and the connection to AWS is encrypted with TLS.
  scope: Amazon ECS Anywhere.
  link: [encrypted with Transport Layer Security (TLS)](../facts/ecs-anywhere.md#ecs-anywhere-faq-link-encrypted-with-tls)
ecs-anywhere-faq-needs-stable-internet-not-air-gapped
  claim: ECS Anywhere cannot run in air-gapped or disconnected environments, because the on-premises compute needs a stable internet connection to the ECS control plane in the AWS Region.
  scope: Amazon ECS Anywhere; the control plane runs in the AWS Region.
  link: [stable internet connection](../facts/ecs-anywhere.md#ecs-anywhere-faq-needs-stable-internet-not-air-gapped)
ecs-anywhere-faq-no-local-control-plane
  claim: With ECS Anywhere you do not install or operate local container orchestration software or manage a local control plane.
  scope: Amazon ECS Anywhere.
  link: [manage a local control plane](../facts/ecs-anywhere.md#ecs-anywhere-faq-no-local-control-plane)
ecs-anywhere-faq-no-scaling-while-disconnected
  claim: While ECS Anywhere compute is disconnected from the control plane, no data plane mutation operations, such as scaling tasks up or down, work.
  scope: Amazon ECS Anywhere; during the period of disconnection.
  link: [no data plane mutation operations](../facts/ecs-anywhere.md#ecs-anywhere-faq-no-scaling-while-disconnected)
ecs-anywhere-faq-one-task-definition-for-all-compute
  claim: You can create an ECS task definition that is compatible with on-premises compute, Fargate and EC2 in a single task definition.
  scope: Amazon ECS Anywhere task definitions.
  link: [all in a single task definition](../facts/ecs-anywhere.md#ecs-anywhere-faq-one-task-definition-for-all-compute)
ecs-anywhere-faq-register-with-closest-region
  claim: AWS recommends registering ECS Anywhere compute with the AWS Region that is geographically closest to the on-premises compute.
  scope: Amazon ECS Anywhere registration.
  link: [geographically closest to your on-premises compute](../facts/ecs-anywhere.md#ecs-anywhere-faq-register-with-closest-region)
ecs-anywhere-faq-same-cluster-on-premises-ec2-fargate
  claim: You can have on-premises compute, EC2 instances and Fargate in the same ECS cluster, which makes it easy to migrate on-premises ECS workloads to Fargate or EC2 later.
  scope: Amazon ECS Anywhere.
  link: [migrate your ECS workloads running on-premises](../facts/ecs-anywhere.md#ecs-anywhere-faq-same-cluster-on-premises-ec2-fargate)
ecs-anywhere-faq-task-role-credentials-6-hours
  claim: If the ECS agent on ECS Anywhere on-premises compute loses network connectivity to the in-Region ECS control plane, existing tasks continue to run; if tasks still have connectivity with other AWS services, they continue to communicate with them for as long as the task role credentials are active (the default expiration time is 6 hours), and once the credentials expire, tasks cannot communicate with other AWS services until connectivity with the control plane is re-established.
  scope: task role credentials of Amazon ECS Anywhere tasks; default; not adjustable.
  link: [default expiration time is 6 hours](../facts/ecs-anywhere.md#ecs-anywhere-faq-task-role-credentials-6-hours)
ecs-anywhere-faq-what-it-is
  claim: Amazon ECS Anywhere is a feature of Amazon ECS that lets you run and manage container-based applications on-premises, on your own virtual machines and bare metal servers.
  scope: Amazon ECS Anywhere.
  link: [run and manage container-based applications on-premises](../facts/ecs-anywhere.md#ecs-anywhere-faq-what-it-is)
ecs-anywhere-iam-role-ecsanywhererole-once-per-account
  claim: When you register an on-premises server or VM to your cluster it requires an IAM role (ECSAnywhereRole) to communicate with AWS APIs; you create the role only once for each AWS account, but it must be associated with each server or VM that you register.
  scope: Amazon ECS Anywhere external instances.
  link: [This role is the `ECSAnywhereRole`](../facts/ecs-anywhere.md#ecs-anywhere-iam-role-ecsanywhererole-once-per-account)
  link: [once for each AWS account](../facts/ecs-anywhere.md#ecs-anywhere-iam-role-ecsanywhererole-once-per-account)
ecs-anywhere-network-modes-no-awsvpc
  claim: Tasks that run on ECS Anywhere external instances must use the bridge, host, or none network modes, and the awsvpc network mode isn't supported.
  scope: Amazon ECS Anywhere external instances.
  link: [the `bridge`, `host`, or `none` network modes](../facts/ecs-anywhere.md#ecs-anywhere-network-modes-no-awsvpc)
  link: [The `awsvpc` network mode isn't supported](../facts/ecs-anywhere.md#ecs-anywhere-network-modes-no-awsvpc)
ecs-anywhere-no-capacity-providers-no-efs
  claim: Amazon ECS capacity providers aren't supported on ECS Anywhere, so you use the EXTERNAL launch type to create a service or run a standalone task, and Amazon EFS volumes aren't supported on external instances.
  scope: Amazon ECS Anywhere external instances.
  link: [Amazon ECS capacity providers aren't supported](../facts/ecs-anywhere.md#ecs-anywhere-no-capacity-providers-no-efs)
  link: [an `EFSVolumeConfiguration` isn't supported](../facts/ecs-anywhere.md#ecs-anywhere-no-capacity-providers-no-efs)
ecs-anywhere-no-load-balancing
  claim: Service load balancing isn't supported on Amazon ECS Anywhere external instances.
  scope: Amazon ECS Anywhere external instances.
  link: [Service load balancing isn't supported](../facts/ecs-anywhere.md#ecs-anywhere-no-load-balancing)
ecs-anywhere-no-service-discovery
  claim: Service discovery isn't supported on Amazon ECS Anywhere external instances.
  scope: Amazon ECS Anywhere external instances.
  link: [Service discovery isn't supported](../facts/ecs-anywhere.md#ecs-anywhere-no-service-discovery)
ecs-anywhere-one-cluster-at-a-time-iam-role
  claim: You can register an external instance to one cluster at a time, and your external instances require an IAM role that allows them to communicate with AWS APIs.
  scope: Amazon ECS Anywhere external instances; maximum.
  link: [to one cluster at a time](../facts/ecs-anywhere.md#ecs-anywhere-one-cluster-at-a-time-iam-role)
  link: [require an IAM role](../facts/ecs-anywhere.md#ecs-anywhere-one-cluster-at-a-time-iam-role)
ecs-anywhere-pricing-no-charge-when-deregistered
  claim: You are not charged for ECS Anywhere for the time when an on-premises instance is deregistered, shut down or terminated.
  scope: per on-premises instance.
  link: [not be charged for the time](../facts/ecs-anywhere.md#ecs-anywhere-pricing-no-charge-when-deregistered)
ecs-anywhere-pricing-per-instance-hour
  claim: ECS Anywhere is charged per hour for each managed ECS Anywhere on-premises instance.
  scope: per on-premises instance.
  link: [for each managed ECS Anywhere on-premises instance](../facts/ecs-anywhere.md#ecs-anywhere-pricing-per-instance-hour)
ecs-anywhere-ssm-credentials-refresh-on-reconnect
  claim: The SSM Agent on an external instance maintains IAM credentials that are rotated every 30 minutes using a hardware fingerprint, and if the instance loses its connection to AWS the SSM Agent automatically refreshes the credentials after the connection is re-established.
  scope: Amazon ECS Anywhere external instances.
  link: [IAM credentials that are rotated every 30 minutes](../facts/ecs-anywhere.md#ecs-anywhere-ssm-credentials-refresh-on-reconnect)
  link: [refreshes the credentials after the connection is re-established](../facts/ecs-anywhere.md#ecs-anywhere-ssm-credentials-refresh-on-reconnect)
ecs-anywhere-windows-support-deprecated
  claim: Windows support for Amazon ECS Anywhere has been deprecated.
  scope: Amazon ECS Anywhere.
  link: [Windows support for Amazon ECS Anywhere](../facts/ecs-anywhere.md#ecs-anywhere-windows-support-deprecated)
  link: [has been deprecated](../facts/ecs-anywhere.md#ecs-anywhere-windows-support-deprecated)
ecs-app2container-modernizes-java-dotnet-into-containers
  claim: AWS App2Container (A2C) is a command-line tool for modernizing .NET and Java applications into containerized applications; it packages the application artifact and dependencies into container images and generates the ECS task and Kubernetes pod definitions.
  scope: AWS App2Container.
  link: [command-line tool for modernizing .NET and Java applications](../facts/ecs.md#ecs-app2container-modernizes-java-dotnet-into-containers)
  link: [generates the ECS task and Kubernetes pod definitions](../facts/ecs.md#ecs-app2container-modernizes-java-dotnet-into-containers)
ecs-app2container-no-longer-open-to-new-customers
  claim: AWS App2Container (A2C), together with other AWS .NET modernization tools, is no longer open to new customers; to use it you had to sign up before November 7, 2025.
  scope: AWS App2Container.
  link: [is no longer open to new customers](../facts/ecs.md#ecs-app2container-no-longer-open-to-new-customers)
  link: [sign up prior to November 7, 2025](../facts/ecs.md#ecs-app2container-no-longer-open-to-new-customers)
ecs-asg-capacity-provider-new-empty-asg-recommended
  claim: AWS recommends creating a new empty Auto Scaling group for an ECS capacity provider, and recommends managed instance draining for graceful termination of EC2 instances; managed instance draining is on by default.
  scope: Amazon ECS Auto Scaling group capacity providers; default.
  link: [create a new empty Auto Scaling group](../facts/ecs.md#ecs-asg-capacity-provider-new-empty-asg-recommended)
  link: [We recommend you use managed instance draining](../facts/ecs.md#ecs-asg-capacity-provider-new-empty-asg-recommended)
ecs-awsvpc-ec2-task-eni-no-public-ip
  claim: For awsvpc tasks on Amazon EC2 Linux instances, task ENIs are not given public IP addresses, so to access the internet tasks must be launched in a private subnet configured to use a NAT gateway.
  scope: ECS tasks on Amazon EC2 Linux instances in awsvpc mode.
  link: [your task ENIs aren't given public IP addresses](../facts/ecs.md#ecs-awsvpc-ec2-task-eni-no-public-ip)
  link: [configured to use a NAT gateway](../facts/ecs.md#ecs-awsvpc-ec2-task-eni-no-public-ip)
ecs-awsvpc-eni-limits-tasks-per-instance
  claim: On EC2 with the awsvpc network mode, each task requires an ENI and an instance has a default quota of network interfaces, so the number of ENIs an instance can attach limits how many such tasks it can run.
  scope: ECS tasks on Amazon EC2 Linux instances in awsvpc mode; the primary network interface counts as one toward the quota.
  link: [network mode requires an ENI](../facts/ecs.md#ecs-awsvpc-eni-limits-tasks-per-instance)
  link: [default quota for the number of network interfaces](../facts/ecs.md#ecs-awsvpc-eni-limits-tasks-per-instance)
ecs-awsvpc-load-balancer-target-type-ip
  claim: For services with tasks that use the awsvpc network mode, you must choose ip as the target type of any target group and not instance, because the tasks are associated with an ENI and not with an EC2 instance.
  scope: ECS services in awsvpc network mode.
  link: [you must choose `ip` as the target type](../facts/ecs.md#ecs-awsvpc-load-balancer-target-type-ip)
  link: [associated with an ENI](../facts/ecs.md#ecs-awsvpc-load-balancer-target-type-ip)
ecs-awsvpc-network-mode-recommended-ec2
  claim: For ECS tasks hosted on Amazon EC2 instances, AWS recommends the awsvpc network mode unless you have a specific need to use a different network mode.
  scope: ECS tasks on Amazon EC2.
  link: [use the `awsvpc` network mode](../facts/ecs.md#ecs-awsvpc-network-mode-recommended-ec2)
  link: [use a different network mode](../facts/ecs.md#ecs-awsvpc-network-mode-recommended-ec2)
ecs-awsvpc-task-own-eni-security-groups
  claim: In the awsvpc network mode each ECS task on EC2 receives its own elastic network interface with a private IPv4 address by default, and you can use security groups and network monitoring tools at a more granular level within your tasks.
  scope: ECS awsvpc network mode.
  link: [receives its own elastic network interface](../facts/ecs.md#ecs-awsvpc-task-own-eni-security-groups)
  link: [at a more granular level within your tasks](../facts/ecs.md#ecs-awsvpc-task-own-eni-security-groups)
ecs-awsvpc-trunking-increases-eni-density
  claim: Amazon ECS supports Amazon EC2 Linux instances of supported instance types with increased ENI density: when you opt in to the awsvpcTrunking account setting and register such instances to your cluster, they have a higher ENI quota, so you can place more tasks on each instance; the instance must use version 1.28.1 or later of the container agent.
  scope: ECS tasks on Amazon EC2 Linux instances in awsvpc mode; supported instance types; container agent 1.28.1 or later.
  link: [opt in to the `awsvpcTrunking` account setting](../facts/ecs.md#ecs-awsvpc-trunking-increases-eni-density)
  link: [these instances have higher ENI quota](../facts/ecs.md#ecs-awsvpc-trunking-increases-eni-density)
ecs-az-rebalancing-best-effort-spread
  claim: For ECS services that specify Availability Zone spread as the first placement strategy, AWS makes a best effort to evenly distribute service tasks across the available Availability Zones, and AWS recommends configuring multi-task services to run across multiple Availability Zones.
  scope: Amazon ECS services; Availability Zone spread is the first placement strategy.
  link: [AWS makes a best effort](../facts/ecs.md#ecs-az-rebalancing-best-effort-spread)
  link: [run across multiple Availability Zones](../facts/ecs.md#ecs-az-rebalancing-best-effort-spread)
ecs-az-rebalancing-enabled-for-eligible-services
  claim: Starting September 5, 2025, Amazon ECS enables Availability Zone rebalancing for all eligible services; a service is eligible when Availability Zone spread is the first task placement strategy or when there is no placement strategy.
  scope: Amazon ECS services; default; adjustable; eligible services.
  link: [enables Availability Zone rebalancing for all services](../facts/ecs.md#ecs-az-rebalancing-enabled-for-eligible-services)
  link: [when there is no placement strategy](../facts/ecs.md#ecs-az-rebalancing-enabled-for-eligible-services)
ecs-az-rebalancing-launches-and-terminates
  claim: With Availability Zone rebalancing, Amazon ECS continuously monitors the distribution of tasks across Availability Zones and, when it detects an uneven distribution, automatically rebalances by launching new tasks in the zones with the fewest tasks and terminating tasks in the overloaded zones.
  scope: Amazon ECS services.
  link: [continuously monitors the distribution of tasks](../facts/ecs.md#ecs-az-rebalancing-launches-and-terminates)
  link: [with the fewest tasks](../facts/ecs.md#ecs-az-rebalancing-launches-and-terminates)
ecs-blue-green-definition-and-zero-downtime
  claim: An ECS blue/green deployment runs two identical production environments, blue and green; it lets you validate new service revisions before directing production traffic to them, and the production environment remains available throughout the deployment.
  scope: Amazon ECS blue/green deployments.
  link: [two identical production environments called blue and green](../facts/ecs.md#ecs-blue-green-definition-and-zero-downtime)
  link: [Zero downtime deployments](../facts/ecs.md#ecs-blue-green-definition-and-zero-downtime)
ecs-blue-green-doubles-resource-usage
  claim: ECS blue/green deployments temporarily run both the blue and green service revisions simultaneously, which may double your resource usage during deployments, and the blue revision is kept running until the bake time expires so rollback is easier.
  scope: Amazon ECS blue/green deployments.
  link: [may double your resource usage during deployments](../facts/ecs.md#ecs-blue-green-doubles-resource-usage)
  link: [kept running until the bake time expires](../facts/ecs.md#ecs-blue-green-doubles-resource-usage)
ecs-blue-green-native-similar-to-codedeploy
  claim: CodeDeploy blue/green and Amazon ECS blue/green deployments provide similar functionality but differ in how you configure and manage them; with Amazon ECS blue/green deployments the deployment configuration is part of the Amazon ECS service itself, and Amazon ECS handles re-routing and rollback by switching the weights on the listener rule.
  scope: Amazon ECS blue/green deployments compared with CodeDeploy blue/green.
  link: [provide similar functionality](../facts/ecs.md#ecs-blue-green-native-similar-to-codedeploy)
  link: [part of the Amazon ECS service itself](../facts/ecs.md#ecs-blue-green-native-similar-to-codedeploy)
ecs-bridge-mode-starts-faster-than-awsvpc-on-ec2
  claim: Tasks that use the bridge network mode on Amazon EC2 start faster than tasks that use the awsvpc network mode, because with awsvpc Amazon ECS attaches an ENI to the instance before launching the task; bridge tasks do not get their own security group.
  scope: Amazon ECS on Amazon EC2.
  link: [start faster than tasks that use the `awsvpc`](../facts/ecs.md#ecs-bridge-mode-starts-faster-than-awsvpc-on-ec2)
  link: [These tasks don't get their own security group](../facts/ecs.md#ecs-bridge-mode-starts-faster-than-awsvpc-on-ec2)
ecs-capacity-managed-instances
  claim: ECS Managed Instances lets you run containers on a range of Amazon EC2 instance types, such as GPU instances, while AWS handles provisioning, patching, scaling and maintenance of the underlying infrastructure.
  scope: ECS capacity options.
  link: [AWS handles provisioning, patching, scaling, and maintenance](../facts/ecs.md#ecs-capacity-managed-instances)
  link: [GPU acceleration](../facts/ecs.md#ecs-capacity-managed-instances)
ecs-capacity-provider-manages-infrastructure-scaling
  claim: Amazon ECS capacity providers manage the scaling of infrastructure for tasks in your clusters; each cluster can have one or more capacity providers and an optional capacity provider strategy, which determines how the tasks are spread across the cluster's capacity providers and consists of one or more capacity providers with a base and a weight.
  scope: Amazon ECS clusters.
  link: [manage the scaling of infrastructure](../facts/ecs.md#ecs-capacity-provider-manages-infrastructure-scaling)
  link: [the `base` and `weight` to assign to them](../facts/ecs.md#ecs-capacity-provider-manages-infrastructure-scaling)
ecs-capacity-provider-reservation-metric-range
  claim: The CapacityProviderReservation metric is the percent of container instances in use for a capacity provider; Amazon ECS sets it to a number between 0 and 100 and publishes it to CloudWatch in the AWS/ECS/ManagedScaling namespace.
  scope: Amazon ECS cluster auto scaling.
  link: [percent of container instances in use](../facts/ecs.md#ecs-capacity-provider-reservation-metric-range)
  link: [AWS/ECS/ManagedScaling namespace](../facts/ecs.md#ecs-capacity-provider-reservation-metric-range)
ecs-capacity-provider-strategy-single-type
  claim: A cluster can have a mix of all capacity provider types, but one capacity provider strategy cannot mix different capacity provider types.
  scope: per capacity provider strategy.
  link: [a mix of all capacity provider types](../facts/ecs.md#ecs-capacity-provider-strategy-single-type)
  link: [a mix of different capacity provider types](../facts/ecs.md#ecs-capacity-provider-strategy-single-type)
ecs-capacity-providers-per-cluster-limit
  claim: One ECS cluster can have at most 20 capacity providers associated with it. The quota is not adjustable.
  scope: per cluster, per Region; maximum; not adjustable.
  link: [20 capacity providers](../facts/ecs.md#ecs-capacity-providers-per-cluster-limit)
ecs-capacity-providers-recommended-over-launch-types
  claim: Capacity providers are the recommended way to configure capacity for workloads, compared to traditional launch types.
  scope: Amazon ECS capacity configuration.
  link: [Capacity providers are the recommended way](../facts/ecs.md#ecs-capacity-providers-recommended-over-launch-types)
  link: [compared to traditional launch types](../facts/ecs.md#ecs-capacity-providers-recommended-over-launch-types)
ecs-capacity-providers-three-compute-types
  claim: With ECS capacity providers you can run workloads on serverless compute with Fargate and Fargate Spot, on self-managed EC2 instances through Auto Scaling group capacity providers, or on fully managed compute through ECS Managed Instances capacity providers.
  scope: Amazon ECS capacity providers.
  link: [serverless compute with Fargate and Fargate Spot](../facts/ecs.md#ecs-capacity-providers-three-compute-types)
  link: [self-managed EC2 instances](../facts/ecs.md#ecs-capacity-providers-three-compute-types)
  link: [fully-managed compute using Amazon ECS Managed Instances](../facts/ecs.md#ecs-capacity-providers-three-compute-types)
ecs-case-study-old-mutual-fargate-no-idle-servers
  claim: Old Mutual moved from a Kubernetes-based solution to Amazon ECS on AWS Fargate because it wanted a service that needed less management and fewer advanced Kubernetes skills, and as the solution is serverless it no longer pays for idle servers or spends time rightsizing instances.
  scope: Old Mutual case study; customer-reported outcome.
  link: [advanced Kubernetes skill sets](../facts/ecs.md#ecs-case-study-old-mutual-fargate-no-idle-servers)
  link: [no longer pays for idle servers](../facts/ecs.md#ecs-case-study-old-mutual-fargate-no-idle-servers)
ecs-case-study-smartsheet-fargate-independent-deployments
  claim: Smartsheet used Amazon ECS with AWS Fargate and AWS CodePipeline to move from coupled to independent deployments, streamlined deployment, eliminated manual upgrades and patches, and reduced the engineering time to deploy from hours to minutes.
  scope: Smartsheet case study; customer-reported outcome.
  link: [transition from coupled deployments to independent deployments](../facts/ecs.md#ecs-case-study-smartsheet-fargate-independent-deployments)
  link: [deploy from hours to minutes](../facts/ecs.md#ecs-case-study-smartsheet-fargate-independent-deployments)
ecs-change-action-logs-2026-07
  claim: On Jul 21, 2026 Amazon ECS introduced Action Logs, an observability feature that delivers timestamped records of the actions ECS performs during service deployments and Managed Daemon updates.
  scope: What's New post.
  link: [Jul 21, 2026](../facts/ecs.md#ecs-change-action-logs-2026-07)
  link: [Action Logs](../facts/ecs.md#ecs-change-action-logs-2026-07)
ecs-change-app-mesh-end-of-support-2026-09-30
  claim: AWS will discontinue support for AWS App Mesh on September 30, 2026. After that date you can no longer access the App Mesh console or App Mesh resources. AWS points App Mesh users to a blog post named Migrating from AWS App Mesh to Amazon ECS Service Connect.
  scope: AWS App Mesh.
  link: [September 30, 2026](../facts/ecs.md#ecs-change-app-mesh-end-of-support-2026-09-30)
  link: [AWS will discontinue support for AWS App Mesh](../facts/ecs.md#ecs-change-app-mesh-end-of-support-2026-09-30)
ecs-change-app-runner-closed-to-new-customers-2026-04
  claim: As of April 30, 2026, AWS App Runner no longer accepts new customers; existing services continue to run.
  scope: AWS App Runner.
  link: [April 30, 2026](../facts/ecs.md#ecs-change-app-runner-closed-to-new-customers-2026-04)
  link: [no longer accepts new customers](../facts/ecs.md#ecs-change-app-runner-closed-to-new-customers-2026-04)
ecs-change-canary-deployments-2025-10
  claim: On October 28, 2025 Amazon ECS added canary deployments, which test a new application version by routing a small percentage of traffic to it while the majority stays on the stable version.
  scope: document history row.
  link: [October 28, 2025](../facts/ecs.md#ecs-change-canary-deployments-2025-10)
  link: [canary deployments](../facts/ecs.md#ecs-change-canary-deployments-2025-10)
ecs-change-configurable-circuit-breaker-2026-07
  claim: On Jul 1, 2026 Amazon ECS made the deployment circuit breaker configurable: the threshold can be a fixed task failure count or a percentage of the desired task count.
  scope: What's New post.
  link: [Jul 1, 2026](../facts/ecs.md#ecs-change-configurable-circuit-breaker-2026-07)
  link: [fixed task failure count or a percentage](../facts/ecs.md#ecs-change-configurable-circuit-breaker-2026-07)
ecs-change-early-success-criteria-2026-09
  claim: On Sep 4, 2026 Amazon ECS added Early Success Criteria for rolling service deployments, which define when a deployment is considered successful.
  scope: What's New post.
  link: [Sep 4, 2026](../facts/ecs.md#ecs-change-early-success-criteria-2026-09)
  link: [Early Success Criteria](../facts/ecs.md#ecs-change-early-success-criteria-2026-09)
ecs-change-ebs-data-volume-per-task-2024-01
  claim: On January 11, 2024 Amazon ECS added support for configuring 1 Amazon EBS data volume per task during deployment, for standalone tasks and for tasks managed by an ECS service.
  scope: document history row.
  link: [January 11, 2024](../facts/ecs.md#ecs-change-ebs-data-volume-per-task-2024-01)
  link: [1 Amazon EBS data volume per task](../facts/ecs.md#ecs-change-ebs-data-volume-per-task-2024-01)
ecs-change-ec2-task-cpu-limit-192-vcpu-2025-02
  claim: On Feb 19, 2025 Amazon ECS raised the CPU limit for ECS tasks deployed on Amazon EC2 instances to up to 192 vCPU, from the previous 10 vCPU limit.
  scope: What's New post.
  link: [up to 192 vCPU](../facts/ecs.md#ecs-change-ec2-task-cpu-limit-192-vcpu-2025-02)
  link: [10 vCPU limit](../facts/ecs.md#ecs-change-ec2-task-cpu-limit-192-vcpu-2025-02)
  changed: 2025-02-19: was 10 vCPU
ecs-change-express-mode-graviton-2026-09
  claim: On Sep 18, 2026 Amazon ECS Express Mode added support for specifying ARM64 as the CPU architecture of a service.
  scope: What's New post.
  link: [Sep 18, 2026](../facts/ecs.md#ecs-change-express-mode-graviton-2026-09)
  link: [ARM64 as the CPU architecture](../facts/ecs.md#ecs-change-express-mode-graviton-2026-09)
ecs-change-express-mode-launch-2025-11
  claim: On Nov 21, 2025 AWS announced Amazon ECS Express Mode, a feature to rapidly launch containerized applications, including web applications and APIs.
  scope: What's New post.
  link: [Nov 21, 2025](../facts/ecs.md#ecs-change-express-mode-launch-2025-11)
  link: [Express Mode, a new feature](../facts/ecs.md#ecs-change-express-mode-launch-2025-11)
ecs-change-fargate-32vcpu-2026-06
  claim: On Jun 5, 2026 Amazon ECS with AWS Fargate added 32vCPU tasks with the memory configurations 60 GiB, 120 GiB, or 244 GiB, for both x86-based and ARM-based workloads on Linux.
  scope: What's New post.
  link: [32vCPU](../facts/ecs.md#ecs-change-fargate-32vcpu-2026-06)
  link: [60 GiB, 120 GiB, or 244 GiB](../facts/ecs.md#ecs-change-fargate-32vcpu-2026-06)
  link: [Jun 5, 2026](../facts/ecs.md#ecs-change-fargate-32vcpu-2026-06)
ecs-change-fargate-new-task-sizes-2022-09
  claim: On September 16, 2022 Amazon ECS on Fargate added the 8 vCPU and 16 vCPU task sizes.
  scope: document history row.
  link: [September 16, 2022](../facts/ecs.md#ecs-change-fargate-new-task-sizes-2022-09)
  link: [8 vCPU and 16 vCPU](../facts/ecs.md#ecs-change-fargate-new-task-sizes-2022-09)
ecs-change-fargate-spot-linux-arm-2024-09
  claim: On September 6, 2024 Amazon ECS added support for Fargate Spot on Linux ARM.
  scope: document history row.
  link: [September 6, 2024](../facts/ecs.md#ecs-change-fargate-spot-linux-arm-2024-09)
  link: [Fargate Spot on Linux ARM](../facts/ecs.md#ecs-change-fargate-spot-linux-arm-2024-09)
ecs-change-fargate-vcpu-based-quotas-2022-09
  claim: On September 8, 2022 Fargate began transitioning from task count-based quotas to vCPU-based quotas.
  scope: document history row.
  link: [September 8, 2022](../facts/ecs.md#ecs-change-fargate-vcpu-based-quotas-2022-09)
  link: [vCPU-based quotas](../facts/ecs.md#ecs-change-fargate-vcpu-based-quotas-2022-09)
ecs-change-faster-service-auto-scaling-benchmark-2026-06
  claim: On Jun 18, 2026 Amazon ECS announced faster service auto scaling with high resolution (20-second) metrics. In AWS benchmarking tests, time to trigger scale-out improved from 363 seconds to 86 seconds.
  scope: What's New post.
  link: [363 seconds](../facts/ecs.md#ecs-change-faster-service-auto-scaling-benchmark-2026-06)
  link: [86 seconds](../facts/ecs.md#ecs-change-faster-service-auto-scaling-benchmark-2026-06)
ecs-change-fractional-gpu-2026-08
  claim: On Aug 6, 2026 Amazon ECS added fractional GPU scheduling with Amazon EC2 G6f instances.
  scope: What's New post.
  link: [Aug 6, 2026](../facts/ecs.md#ecs-change-fractional-gpu-2026-08)
  link: [fractional GPU scheduling](../facts/ecs.md#ecs-change-fractional-gpu-2026-08)
ecs-change-linear-deployments-2025-10
  claim: On October 28, 2025 Amazon ECS added linear deployments, which gradually shift traffic from the current service revision to a new revision in equal percentage increments.
  scope: document history row.
  link: [October 28, 2025](../facts/ecs.md#ecs-change-linear-deployments-2025-10)
  link: [linear deployments](../facts/ecs.md#ecs-change-linear-deployments-2025-10)
ecs-change-managed-instances-gpu-fee-reduction-2026-07
  claim: Beginning July 1, 2026, ECS Managed Instances management fees are reduced by 35% for G-series instances and by 60% for P-series and AWS Trainium instances.
  scope: What's New post.
  link: [reduced by 35%](../facts/ecs.md#ecs-change-managed-instances-gpu-fee-reduction-2026-07)
  link: [reduced by 60%](../facts/ecs.md#ecs-change-managed-instances-gpu-fee-reduction-2026-07)
ecs-change-managed-instances-launch-2025-09
  claim: On September 30, 2025 Amazon ECS added support for Amazon ECS Managed Instances for running containerized workloads.
  scope: document history row.
  link: [September 30, 2025](../facts/ecs.md#ecs-change-managed-instances-launch-2025-09)
  link: [Amazon ECS Managed Instances](../facts/ecs.md#ecs-change-managed-instances-launch-2025-09)
ecs-change-managed-instances-lifetime-21-days-2025-12
  claim: On December 11, 2025 the Amazon ECS documentation clarified the instance lifetime terminology of managed instances and extended the maximum instance lifetime from 14 days to 21 days.
  scope: document history row.
  link: [December 11, 2025](../facts/ecs.md#ecs-change-managed-instances-lifetime-21-days-2025-12)
  link: [from 14 days to 21 days](../facts/ecs.md#ecs-change-managed-instances-lifetime-21-days-2025-12)
ecs-change-native-blue-green-deployments-2025-07
  claim: On July 15, 2025 Amazon ECS added native blue/green deployments, which let you validate new service revisions before directing production traffic to them.
  scope: document history row.
  link: [July 15, 2025](../facts/ecs.md#ecs-change-native-blue-green-deployments-2025-07)
  link: [native blue/green deployments](../facts/ecs.md#ecs-change-native-blue-green-deployments-2025-07)
ecs-change-predictive-scaling-2024-11
  claim: On November 21, 2024 Amazon ECS added predictive scaling, which anticipates future needs and proactively increases the tasks in a service.
  scope: document history row.
  link: [November 21, 2024](../facts/ecs.md#ecs-change-predictive-scaling-2024-11)
  link: [predictive scaling](../facts/ecs.md#ecs-change-predictive-scaling-2024-11)
ecs-change-service-connect-ga-2022-11
  claim: On November 27, 2022 Amazon ECS Service Connect became generally available, adding service discovery and a service mesh that is controlled by Amazon ECS service deployments.
  scope: document history row.
  link: [November 27, 2022](../facts/ecs.md#ecs-change-service-connect-ga-2022-11)
  link: [Service Connect](../facts/ecs.md#ecs-change-service-connect-ga-2022-11)
ecs-change-service-connect-zone-aware-routing-2026-07
  claim: On Jul 23, 2026 Amazon ECS introduced zone-aware routing for ECS Service Connect, to reduce cross-AZ data transfer costs and latency by prioritizing service-to-service traffic within the same AZ.
  scope: What's New post.
  link: [Jul 23, 2026](../facts/ecs.md#ecs-change-service-connect-zone-aware-routing-2026-07)
  link: [zone-aware routing for ECS Service Connect](../facts/ecs.md#ecs-change-service-connect-zone-aware-routing-2026-07)
ecs-change-target-tracking-20-second-metrics-2026-06
  claim: On Jun 18, 2026 Amazon ECS target tracking policies for CPU and memory utilization gained 20-second metric resolution, in addition to the default 60-second resolution, for faster scaling signal detection.
  scope: What's New post.
  link: [20-second metric resolution](../facts/ecs.md#ecs-change-target-tracking-20-second-metrics-2026-06)
  link: [default 60-second resolution](../facts/ecs.md#ecs-change-target-tracking-20-second-metrics-2026-06)
  link: [Jun 18, 2026](../facts/ecs.md#ecs-change-target-tracking-20-second-metrics-2026-06)
ecs-change-vpc-lattice-blue-green-2026-10
  claim: On Oct 2, 2026 Amazon ECS added built-in blue/green, linear, and canary deployment strategies for ECS services that use Amazon VPC Lattice.
  scope: What's New post.
  link: [Oct 2, 2026](../facts/ecs.md#ecs-change-vpc-lattice-blue-green-2026-10)
  link: [blue/green, linear, and canary deployment strategies](../facts/ecs.md#ecs-change-vpc-lattice-blue-green-2026-10)
ecs-change-vpc-lattice-integration-2024-11
  claim: On November 18, 2024 Amazon ECS made VPC Lattice available for ECS services, to standardize service-to-service connectivity, security, and observability.
  scope: document history row.
  link: [November 18, 2024](../facts/ecs.md#ecs-change-vpc-lattice-integration-2024-11)
  link: [VPC Lattice is now available](../facts/ecs.md#ecs-change-vpc-lattice-integration-2024-11)
ecs-circuit-breaker-default-threshold-bounded-percent-50
  claim: For the default threshold type of the ECS deployment circuit breaker, Amazon ECS multiplies the value by the latest service desired count to calculate the failure threshold and clamps the result to a minimum of 3 and a maximum of 200; the default value is 50.
  scope: per service, deployment circuit breaker; default; adjustable.
  link: [default value of 50](../facts/ecs.md#ecs-circuit-breaker-default-threshold-bounded-percent-50)
  link: [minimum of 3](../facts/ecs.md#ecs-circuit-breaker-default-threshold-bounded-percent-50)
  link: [maximum of 200](../facts/ecs.md#ecs-circuit-breaker-default-threshold-bounded-percent-50)
ecs-circuit-breaker-rolling-controller-only
  claim: The deployment circuit breaker is only supported for Amazon ECS services that use the rolling update (ECS) deployment controller.
  scope: Amazon ECS deployment circuit breaker.
  link: [only supported for Amazon ECS services](../facts/ecs.md#ecs-circuit-breaker-rolling-controller-only)
  link: [deployment controller](../facts/ecs.md#ecs-circuit-breaker-rolling-controller-only)
ecs-circuit-breaker-rolls-back-to-completed
  claim: The ECS deployment circuit breaker is the rolling update mechanism that determines whether tasks reach a steady state, and it has an option to automatically roll back a failed deployment to the deployment that is in the COMPLETED state.
  scope: Amazon ECS rolling update deployments; rollback is an option.
  link: [determines if the tasks reach a steady state](../facts/ecs.md#ecs-circuit-breaker-rolls-back-to-completed)
  link: [automatically roll back a failed deployment](../facts/ecs.md#ecs-circuit-breaker-rolls-back-to-completed)
ecs-classic-load-balancers-per-service-limit
  claim: One ECS service can use at most 1 Classic Load Balancer. The quota is not adjustable.
  scope: per service, per Region; maximum; not adjustable.
  link: [1 Classic Load Balancer](../facts/ecs.md#ecs-classic-load-balancers-per-service-limit)
ecs-cluster-auto-scaling-managed-scaling-asg-capacity-provider
  claim: ECS cluster auto scaling lets Amazon ECS manage the scaling of the EC2 instances registered to your cluster; you turn on managed scaling when you create the Auto Scaling group capacity provider and set a target percentage (targetCapacity) for instance utilization.
  scope: Amazon ECS Auto Scaling group capacity providers.
  link: [manage the scaling of Amazon EC2 instances](../facts/ecs.md#ecs-cluster-auto-scaling-managed-scaling-asg-capacity-provider)
  link: [You turn on managed scaling](../facts/ecs.md#ecs-cluster-auto-scaling-managed-scaling-asg-capacity-provider)
ecs-cluster-auto-scaling-policy-managed-by-ecs
  claim: Amazon ECS creates the target tracking scaling policy for cluster auto scaling and attaches it to the Auto Scaling group; to update it, you update the capacity provider managed scaling settings rather than the scaling policy directly.
  scope: Amazon ECS Auto Scaling group capacity providers.
  link: [creates the target tracking scaling policy](../facts/ecs.md#ecs-cluster-auto-scaling-policy-managed-by-ecs)
  link: [update the capacity provider managed scaling settings](../facts/ecs.md#ecs-cluster-auto-scaling-policy-managed-by-ecs)
ecs-cluster-auto-scaling-reservation-above-or-below-target
  claim: When more tasks use a higher percentage of the capacity than the targetCapacity percentage, the increased CapacityProviderReservation metric causes its CloudWatch alarm to update the DesiredCapacity of the Auto Scaling group, and the group launches EC2 instances and registers them with the cluster; when fewer tasks use a lower percentage than targetCapacity and at least one instance can be terminated, the decreased metric causes the alarm to update DesiredCapacity, and the group terminates EC2 container instances and deregisters them from the cluster.
  scope: Amazon ECS cluster auto scaling.
  link: [launch EC2 instances, and then register them](../facts/ecs.md#ecs-cluster-auto-scaling-reservation-above-or-below-target)
  link: [terminate EC2 container instances, and then deregister them](../facts/ecs.md#ecs-cluster-auto-scaling-reservation-above-or-below-target)
ecs-cluster-ec2-full-control-you-manage-instances
  claim: The ECS clusters page describes Amazon EC2 instances as full control: you manage the underlying instances directly, including instance selection, configuration, and maintenance.
  scope: Amazon ECS cluster infrastructure types.
  link: [You manage the underlying Amazon EC2 instances directly](../facts/ecs.md#ecs-cluster-ec2-full-control-you-manage-instances)
  link: [including instance selection, configuration, and maintenance](../facts/ecs.md#ecs-cluster-ec2-full-control-you-manage-instances)
ecs-cluster-is-infrastructure
  claim: An Amazon ECS cluster is a logical grouping of tasks or services that provides the infrastructure capacity for your containerized applications.
  scope: Amazon ECS features.
  link: [a logical grouping of tasks or services](../facts/ecs.md#ecs-cluster-is-infrastructure)
  link: [provides the infrastructure capacity](../facts/ecs.md#ecs-cluster-is-infrastructure)
ecs-cluster-is-regional-and-mixes-capacity
  claim: ECS clusters are AWS Region specific, and one cluster can contain a mix of tasks hosted on ECS Managed Instances, AWS Fargate, Amazon EC2 instances, or external instances.
  scope: Amazon ECS clusters.
  link: [Clusters are AWS Region specific](../facts/ecs.md#ecs-cluster-is-regional-and-mixes-capacity)
  link: [A cluster can contain a mix of tasks](../facts/ecs.md#ecs-cluster-is-regional-and-mixes-capacity)
ecs-cluster-managed-instances-recommended-for-most-new-workloads
  claim: The ECS clusters page says Amazon ECS Managed Instances is the recommended choice for most new workloads because it gives the best combination of performance, cost optimization, and operational simplicity while AWS handles infrastructure management tasks.
  scope: Amazon ECS cluster infrastructure types.
  link: [the recommended choice for most new workloads](../facts/ecs.md#ecs-cluster-managed-instances-recommended-for-most-new-workloads)
  link: [combination of performance, cost optimization, and operational simplicity](../facts/ecs.md#ecs-cluster-managed-instances-recommended-for-most-new-workloads)
ecs-clusters-per-account-quota
  claim: An account can have 10,000 ECS clusters in each supported Region by default. The quota is adjustable through Service Quotas.
  scope: per account, per Region; default; adjustable.
  link: [10,000 ECS clusters](../facts/ecs.md#ecs-clusters-per-account-quota)
ecs-container-instance-role-registers-agent
  claim: ECS container instances, both Amazon EC2 and external, run the ECS container agent and require an IAM role so the service knows the agent belongs to you; the container instance role provides permissions the container agent and Docker daemon need to call AWS APIs on your behalf.
  scope: Amazon ECS container instance IAM role; EC2 or external instances.
  link: [know that the agent belongs to you](../facts/ecs.md#ecs-container-instance-role-registers-agent)
  link: [Docker daemon to call AWS APIs](../facts/ecs.md#ecs-container-instance-role-registers-agent)
ecs-container-instances-per-cluster-limit
  claim: One ECS cluster can have at most 5,000 container instances. The quota is not adjustable.
  scope: per cluster, per Region; maximum; not adjustable.
  link: [5,000 container instances](../facts/ecs.md#ecs-container-instances-per-cluster-limit)
ecs-container-stop-timeout-default-and-max
  claim: For tasks on AWS Fargate, stopTimeout is the time in seconds to wait before a container is forcefully killed if it doesn't exit normally on its own; it requires platform version 1.3.0 or later (Linux), the default value is 30 seconds if you don't specify it, and the maximum value is 120 seconds.
  scope: per container definition, tasks on AWS Fargate; default; adjustable; platform version 1.3.0 or later (Linux).
  link: [30 seconds](../facts/ecs.md#ecs-container-stop-timeout-default-and-max)
  link: [120 seconds](../facts/ecs.md#ecs-container-stop-timeout-default-and-max)
ecs-containers-consistency-portability-benefits
  claim: The AWS container decision guide lists portability (a consistent runtime environment that can run on any platform that supports the container runtime) and consistency (the application runs the same way in all environments) among the advantages of containers.
  scope: Containers on AWS.
  link: [a consistent runtime environment](../facts/ecs.md#ecs-containers-consistency-portability-benefits)
  link: [runs the same way in all environments](../facts/ecs.md#ecs-containers-consistency-portability-benefits)
ecs-containers-not-security-boundary-use-fargate-for-isolation
  claim: Containers are not a security boundary; for workloads with strict isolation requirements use Fargate, because on EC2, ECS Managed Instances and ECS Anywhere container instances there is no task isolation and containers can potentially access credentials of other tasks on the same instance.
  scope: Amazon ECS compute options; EC2, Managed Instances and ECS Anywhere share instances between tasks.
  link: [For workloads with strict isolation requirements, use Fargate](../facts/ecs.md#ecs-containers-not-security-boundary-use-fargate-for-isolation)
  link: [there is no task isolation](../facts/ecs.md#ecs-containers-not-security-boundary-use-fargate-for-isolation)
ecs-containers-per-task-definition-limit
  claim: One ECS task definition can hold at most 10 container definitions. The quota is not adjustable.
  scope: per task definition, per Region; maximum; not adjustable.
  link: [10 container definitions](../facts/ecs.md#ecs-containers-per-task-definition-limit)
ecs-daemon-minimum-healthy-percent-default
  claim: The default minimumHealthyPercent for an ECS service that uses the DAEMON service scheduler is 0% for the AWS CLI, the AWS SDKs, and the APIs and 50% for the AWS Management Console.
  scope: per service, DAEMON scheduler; default; adjustable.
  link: [0% for the AWS CLI](../facts/ecs.md#ecs-daemon-minimum-healthy-percent-default)
  link: [50% for the AWS Management Console](../facts/ecs.md#ecs-daemon-minimum-healthy-percent-default)
ecs-daemon-strategy-one-task-per-instance
  claim: The DAEMON scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints you specify; you do not need to specify a desired number of tasks, a placement strategy, or Service Auto Scaling policies.
  scope: Amazon ECS services; container instances that meet the placement constraints.
  link: [exactly one task on each active container instance](../facts/ecs.md#ecs-daemon-strategy-one-task-per-instance)
  link: [no need to specify a desired number](../facts/ecs.md#ecs-daemon-strategy-one-task-per-instance)
ecs-decision-guide-ecs-more-control-eks-flexibility
  claim: The AWS container decision guide says Amazon ECS is a good choice if you need more control over the network and security configurations without sacrificing scale or features, while Amazon EKS provides the flexibility and control over application deployment and orchestration that Kubernetes technology offers.
  scope: Amazon ECS compared with Amazon EKS.
  link: [more control over the network and security configurations](../facts/ecs.md#ecs-decision-guide-ecs-more-control-eks-flexibility)
  link: [provided by Kubernetes technology](../facts/ecs.md#ecs-decision-guide-ecs-more-control-eks-flexibility)
ecs-decision-guide-layers-capacity-orchestration-vertical
  claim: The AWS container decision guide says you can think about the universe of AWS container services in three distinct layers, and that the orchestration layer schedules and scales your environment.
  scope: AWS container services.
  link: [AWS container services in three distinct layers](../facts/ecs.md#ecs-decision-guide-layers-capacity-orchestration-vertical)
  link: [orchestration layer** schedules and scales your environment](../facts/ecs.md#ecs-decision-guide-layers-capacity-orchestration-vertical)
ecs-decision-guide-portability-and-managed-overhead
  claim: The AWS container decision guide says organizations might choose to build on managed container services to reduce their operational overhead, and that many customers want their applications to be able to run in, or move to, a different environment, so that they can preserve choice or run an application both on premises and in the cloud.
  scope: AWS container services.
  link: [reduce their operational overhead](../facts/ecs.md#ecs-decision-guide-portability-and-managed-overhead)
  link: [both on premises and in the cloud](../facts/ecs.md#ecs-decision-guide-portability-and-managed-overhead)
ecs-decision-guide-serverless-or-kubernetes-operating-model
  claim: The AWS container decision guide says one of the first considerations is your preference for either a serverless operational model or a Kubernetes operation model, and that in practice most customers use both to varying degrees.
  scope: AWS container services.
  link: [serverless operational model or a Kubernetes operation model](../facts/ecs.md#ecs-decision-guide-serverless-or-kubernetes-operating-model)
  link: [most customers use both to varying degrees](../facts/ecs.md#ecs-decision-guide-serverless-or-kubernetes-operating-model)
ecs-draining-instance-no-new-tasks
  claim: When a container instance is set to DRAINING, Amazon ECS prevents new tasks from being scheduled on it, stops service tasks on it that are in the PENDING state immediately, and starts replacement service tasks on other available container instances.
  scope: Amazon ECS container instances.
  link: [prevents new tasks from being scheduled](../facts/ecs.md#ecs-draining-instance-no-new-tasks)
  link: [replacement service tasks are started on them](../facts/ecs.md#ecs-draining-instance-no-new-tasks)
ecs-ebs-fargate-magnetic-not-supported
  claim: The magnetic (standard) Amazon EBS volume type is not supported for tasks hosted on Fargate.
  scope: EBS volumes on Fargate tasks.
  link: [Amazon EBS volume type is not supported](../facts/ecs.md#ecs-ebs-fargate-magnetic-not-supported)
  link: [tasks hosted on Fargate](../facts/ecs.md#ecs-ebs-fargate-magnetic-not-supported)
ecs-ebs-volume-one-per-task-new-volume
  claim: You can attach at most one Amazon EBS volume to each Amazon ECS task, and it must be a new volume; you cannot attach an existing volume but can create a new volume from a snapshot of an existing volume.
  scope: per ECS task; maximum; a new volume can be created from a snapshot at deployment.
  link: [at most one Amazon EBS volume](../facts/ecs.md#ecs-ebs-volume-one-per-task-new-volume)
  link: [it must be a new volume](../facts/ecs.md#ecs-ebs-volume-one-per-task-new-volume)
ecs-ebs-volume-per-task-managed-by-ecs
  claim: Amazon EBS volumes that are attached to Amazon ECS tasks are managed by Amazon ECS on your behalf; you can configure new, empty volumes or use snapshots to load data from existing volumes, and the volumes can be encrypted with AWS Key Management Service (AWS KMS) keys.
  scope: Amazon ECS tasks with EBS volumes.
  link: [managed by Amazon ECS on your behalf](../facts/ecs.md#ecs-ebs-volume-per-task-managed-by-ecs)
  link: [use snapshots to load data from existing volumes](../facts/ecs.md#ecs-ebs-volume-per-task-managed-by-ecs)
  link: [encrypted with AWS Key Management Service](../facts/ecs.md#ecs-ebs-volume-per-task-managed-by-ecs)
ecs-ebs-volume-service-task-deleted-on-termination
  claim: Amazon EBS volumes attached to tasks managed by a service are not preserved and are always deleted upon task termination.
  scope: EBS volumes of ECS service tasks.
  link: [always deleted upon task termination](../facts/ecs.md#ecs-ebs-volume-service-task-deleted-on-termination)
  link: [tasks that are managed by a service](../facts/ecs.md#ecs-ebs-volume-service-task-deleted-on-termination)
ecs-ec2-capacity-large-workloads-price-optimized
  claim: The ECS guide says to use EC2 capacity for large workloads that must be price optimized.
  scope: Amazon ECS on Amazon EC2.
  link: [Use EC2 capacity for large workloads](../facts/ecs.md#ecs-ec2-capacity-large-workloads-price-optimized)
  link: [must be price optimized](../facts/ecs.md#ecs-ec2-capacity-large-workloads-price-optimized)
ecs-ec2-tasks-launched-per-service-per-minute-limit
  claim: The ECS service scheduler can provision at most 500 tasks per service per minute on an Amazon EC2 or External instance. The quota is not adjustable.
  scope: per service, per minute, per Region; maximum; not adjustable.
  link: [500 tasks per service per minute](../facts/ecs.md#ecs-ec2-tasks-launched-per-service-per-minute-limit)
ecs-efs-fargate-platform-14-linux-only
  claim: For tasks hosted on Fargate, Amazon EFS file systems are supported on platform version 1.4.0 or later (Linux).
  scope: Amazon EFS on Fargate tasks; minimum; Linux.
  link: [platform version 1.4.0 or later (Linux)](../facts/ecs.md#ecs-efs-fargate-platform-14-linux-only)
  link: [tasks that are hosted on Fargate](../facts/ecs.md#ecs-efs-fargate-platform-14-linux-only)
ecs-efs-volumes-shared-persistent-across-instances
  claim: Amazon EFS file systems can be used with Amazon ECS to export file system data across your fleet of container instances so that tasks have access to the same persistent storage no matter the instance on which they land.
  scope: Amazon ECS with Amazon EFS.
  link: [access to the same persistent storage](../facts/ecs.md#ecs-efs-volumes-shared-persistent-across-instances)
  link: [no matter the instance on which they land](../facts/ecs.md#ecs-efs-volumes-shared-persistent-across-instances)
ecs-eventbridge-scheduler-serverless-scheduler
  claim: EventBridge Scheduler is a serverless scheduler that lets you create, run and manage tasks from one central, managed service, with one-time and recurring scheduling independent of event buses and rules, and it can schedule Amazon ECS tasks.
  scope: Amazon ECS scheduled tasks.
  link: [a serverless scheduler](../facts/ecs.md#ecs-eventbridge-scheduler-serverless-scheduler)
  link: [one-time and recurring scheduling functionality](../facts/ecs.md#ecs-eventbridge-scheduler-serverless-scheduler)
ecs-express-mode-creates-fargate-alb-autoscaling
  claim: Amazon ECS Express Mode orchestrates and configures a Fargate-based ECS service with a unique accessible URL, a load balancer with SSL/TLS, auto scaling policies, monitoring, and networking components.
  scope: Amazon ECS Express Mode.
  link: [a Fargate-based ECS service](../facts/ecs.md#ecs-express-mode-creates-fargate-alb-autoscaling)
  link: [load balancer with SSL/TLS, auto scaling policies](../facts/ecs.md#ecs-express-mode-creates-fargate-alb-autoscaling)
ecs-express-mode-no-additional-charge
  claim: There is no additional charge for using an Amazon ECS Express Mode service; you pay only for the underlying AWS resources that are created to run your application.
  scope: Amazon ECS Express Mode.
  link: [There is no additional charge](../facts/ecs.md#ecs-express-mode-no-additional-charge)
  link: [You pay only for the underlying AWS resources](../facts/ecs.md#ecs-express-mode-no-additional-charge)
ecs-express-mode-shares-alb-reduces-cost
  claim: Amazon ECS Express Mode shares Application Load Balancers across multiple Express Mode services that use the same networking configuration to reduce costs, and all the underlying AWS resources remain accessible for direct management.
  scope: Amazon ECS Express Mode; same networking configuration.
  link: [Shares Application Load Balancers](../facts/ecs.md#ecs-express-mode-shares-alb-reduces-cost)
  link: [remain accessible for direct management](../facts/ecs.md#ecs-express-mode-shares-alb-reduces-cost)
ecs-express-mode-three-inputs
  claim: An Amazon ECS Express Mode service needs only a container image, a task execution role and an infrastructure role to get started, and it reduces the complexity of deploying containerized applications by providing sensible defaults and automating the configuration of supporting AWS services.
  scope: Amazon ECS Express Mode.
  link: [requires only three things to get started](../facts/ecs.md#ecs-express-mode-three-inputs)
  link: [providing sensible defaults](../facts/ecs.md#ecs-express-mode-three-inputs)
ecs-express-mode-use-cases-web-apps-apis
  claim: Amazon ECS Express Mode services support either public or private HTTPS applications and automatically scale based on utilization or traffic; one scenario for using them is web applications and APIs, which are stateless containerized applications that serve HTTP requests.
  scope: Amazon ECS Express Mode.
  link: [Stateless containerized applications that serve HTTP requests](../facts/ecs.md#ecs-express-mode-use-cases-web-apps-apis)
  link: [automatically scale based on utilization or traffic](../facts/ecs.md#ecs-express-mode-use-cases-web-apps-apis)
ecs-failed-deployment-detection-circuit-breaker-vs-alarms
  claim: Use the circuit breaker to stop an ECS rolling deployment when the tasks can't start, and CloudWatch alarms to stop a deployment based on application metrics; both methods support rolling back to the previous service revision.
  scope: Amazon ECS rolling update deployments; methods can be used separately or together.
  link: [stop a deployment when the tasks can't start](../facts/ecs.md#ecs-failed-deployment-detection-circuit-breaker-vs-alarms)
  link: [stop a deployment based on application metrics](../facts/ecs.md#ecs-failed-deployment-detection-circuit-breaker-vs-alarms)
  link: [Both methods support rolling back](../facts/ecs.md#ecs-failed-deployment-detection-circuit-breaker-vs-alarms)
ecs-faq-app-auto-scaling-custom-cloudwatch-metric
  claim: Application Auto Scaling can also scale an Amazon ECS service on a custom metric specification that represents a CloudWatch metric you choose.
  scope: Amazon ECS service auto scaling.
  link: [custom metric specification](../facts/ecs.md#ecs-faq-app-auto-scaling-custom-cloudwatch-metric)
ecs-faq-compliance-programs-met
  claim: Amazon ECS meets the standards for PCI DSS Level 1, ISO 9001, ISO 27001, ISO 27017, ISO 27018, SOC 1, SOC 2, SOC 3 and HIPAA eligibility.
  scope: Amazon ECS.
  link: [PCI DSS Level 1](../facts/ecs.md#ecs-faq-compliance-programs-met)
ecs-faq-compute-autoscaling-fargate-and-ec2
  claim: Amazon ECS supports autoscaling of compute infrastructure for both AWS Fargate and Amazon EC2.
  scope: Amazon ECS compute infrastructure.
  link: [both AWS Fargate and Amazon EC2](../facts/ecs.md#ecs-faq-compute-autoscaling-fargate-and-ec2)
ecs-faq-container-insights-ec2-and-fargate
  claim: CloudWatch Container Insights collects, aggregates and summarizes metrics and logs for Amazon ECS clusters running on Amazon EC2 and AWS Fargate.
  scope: Amazon ECS clusters on EC2 and Fargate.
  link: [CloudWatch Container Insights](../facts/ecs.md#ecs-faq-container-insights-ec2-and-fargate)
ecs-faq-ec2-for-greater-control
  claim: Customers who need greater control of their EC2 instances, to support compliance and governance requirements or broader customization options, can choose Amazon ECS with Amazon EC2 instances instead of Fargate.
  scope: Amazon ECS compute choice; compliance, governance or customization needs.
  link: [greater control of their EC2 instances](../facts/ecs.md#ecs-faq-ec2-for-greater-control)
ecs-faq-ec2-root-access-to-os
  claim: As an Amazon EC2 customer using ECS on EC2, you have root access to the operating system of your container instances.
  scope: Amazon ECS container instances on EC2.
  link: [root access to the operating system](../facts/ecs.md#ecs-faq-ec2-root-access-to-os)
ecs-faq-ec2-split-cost-allocation-opt-in
  claim: For Amazon ECS tasks running on Amazon EC2 instances, you can access cost and usage information in AWS Cost and Usage Reports (CUR) by opting into Split Cost Allocation Data for Amazon ECS.
  scope: Amazon ECS tasks on EC2 instances; opt in.
  link: [Split Cost Allocation Data for Amazon ECS](../facts/ecs.md#ecs-faq-ec2-split-cost-allocation-opt-in)
ecs-faq-ecr-pull-needs-instance-role-policy
  claim: To configure ECS container instances to pull from Amazon ECR, you specify the Amazon ECR repository in your task definition and attach the AmazonEC2ContainerServiceforEC2Role to your instances; then Amazon ECS retrieves the appropriate images for your applications.
  scope: Amazon ECS container instances on EC2.
  link: [AmazonEC2ContainerServiceforEC2Role](../facts/ecs.md#ecs-faq-ecr-pull-needs-instance-role-policy)
ecs-faq-express-alb-shared-up-to-25-services
  claim: ECS Express Mode services that use the same subnet networking configuration can share an ALB, up to 25 services per load balancer.
  scope: per Application Load Balancer, Express Mode services with the same subnet networking configuration; maximum; not adjustable; services use the same subnet networking configuration.
  link: [up to 25 services per load balancer](../facts/ecs.md#ecs-faq-express-alb-shared-up-to-25-services)
ecs-faq-express-creates-all-resources
  claim: When you deploy with ECS Express Mode, ECS creates and configures the resources needed to receive ingress traffic: the ECS service, task definition, networking, load balancer and auto scaling.
  scope: Amazon ECS Express Mode.
  link: [the ECS service, task definition, networking](../facts/ecs.md#ecs-faq-express-creates-all-resources)
ecs-faq-express-default-fargate-and-alb
  claim: By default, ECS Express Mode creates services using AWS Fargate and includes an Application Load Balancer for incoming traffic.
  scope: Amazon ECS Express Mode services; default; not adjustable.
  link: [creates services using AWS Fargate](../facts/ecs.md#ecs-faq-express-default-fargate-and-alb)
  link: [Application Load Balancer (ALB)](../facts/ecs.md#ecs-faq-express-default-fargate-and-alb)
ecs-faq-express-keeps-full-resource-access
  claim: After deployment you maintain full access to the underlying resources that ECS Express Mode created while your application keeps running on ECS, and you can go to the Console, API or CLI for any underlying resource, such as the ECS task definition, ALB target group or AAS scaling policy, and modify settings that are specific to your application.
  scope: Amazon ECS Express Mode resources.
  link: [you maintain full access to the underlying resources](../facts/ecs.md#ecs-faq-express-keeps-full-resource-access)
ecs-faq-express-needs-only-image-and-two-roles
  claim: Getting started with ECS Express Mode requires only a container image and the IAM task execution and infrastructure roles.
  scope: Amazon ECS Express Mode.
  link: [only a container image](../facts/ecs.md#ecs-faq-express-needs-only-image-and-two-roles)
ecs-faq-express-no-additional-charge
  claim: There is no additional charge for ECS Express Mode; you pay only for the AWS resources it creates, such as Fargate, the Application Load Balancer and CloudWatch monitoring.
  scope: Amazon ECS Express Mode; you pay for the resources created.
  link: [no additional charge](../facts/ecs.md#ecs-faq-express-no-additional-charge)
ecs-faq-fargate-billing-granularity
  claim: With AWS Fargate on Amazon ECS you pay for the vCPU and memory resources that your containerized application requests, calculated from the time your container images are pulled until the task terminates, rounded up to the nearest second, with a minimum charge of one minute.
  scope: per Amazon ECS task on Fargate; minimum; from image pull until the task terminates.
  link: [rounded up to the nearest second](../facts/ecs.md#ecs-faq-fargate-billing-granularity)
  link: [one minute](../facts/ecs.md#ecs-faq-fargate-billing-granularity)
ecs-faq-fargate-cost-in-cur-automatically
  claim: Costs for Amazon ECS tasks on AWS Fargate are available automatically in AWS Cost and Usage Reports and AWS Cost Explorer.
  scope: Amazon ECS tasks on AWS Fargate.
  link: [AWS Cost and Usage Reports (CUR)](../facts/ecs.md#ecs-faq-fargate-cost-in-cur-automatically)
ecs-faq-fargate-no-ec2-management
  claim: With Amazon ECS on AWS Fargate you launch containers without provisioning or managing EC2 instances; the FAQ calls it the easiest way to launch and run containers on AWS.
  scope: Amazon ECS with AWS Fargate.
  link: [without having to provision or manage](../facts/ecs.md#ecs-faq-fargate-no-ec2-management)
ecs-faq-fargate-own-vm-and-network-interface
  claim: On Fargate every Amazon ECS task runs in a separate virtual machine and has its own network interface, so a security group can be applied to each task.
  scope: each Amazon ECS task on AWS Fargate.
  link: [every task runs in a separate virtual machine](../facts/ecs.md#ecs-faq-fargate-own-vm-and-network-interface)
  link: [own network interface](../facts/ecs.md#ecs-faq-fargate-own-vm-and-network-interface)
ecs-faq-hipaa-eligible-on-fargate-or-ec2
  claim: Amazon ECS is HIPAA-eligible; with an executed Business Associate Addendum with AWS you can process encrypted PHI using containers on the Fargate launch type or on Amazon EC2 instances.
  scope: Amazon ECS on Fargate and on EC2; an executed Business Associate Addendum with AWS; encrypted PHI.
  link: [Amazon ECS is HIPAA-eligible](../facts/ecs.md#ecs-faq-hipaa-eligible-on-fargate-or-ec2)
ecs-faq-ingress-alb-nlb
  claim: Amazon ECS integrates with Elastic Load Balancing so you can distribute traffic across containers with Application Load Balancers or Network Load Balancers.
  scope: Amazon ECS ingress traffic.
  link: [Application Load Balancers or Network Load Balancers](../facts/ecs.md#ecs-faq-ingress-alb-nlb)
ecs-faq-mi-additional-benefits-over-fargate
  claim: Compared with Fargate, ECS Managed Instances adds guaranteed performance, access to accelerated, burstable and high-bandwidth instances, and privileged containers with Linux capabilities.
  scope: Amazon ECS Managed Instances compared with AWS Fargate.
  link: [privileged containers with Linux capabilities](../facts/ecs.md#ecs-faq-mi-additional-benefits-over-fargate)
ecs-faq-mi-compute-in-your-account-billing
  claim: Unlike Fargate, with ECS Managed Instances the underlying compute lives in your own AWS account, and you are billed the EC2 instance price plus a management fee per instance, not per task.
  scope: Amazon ECS Managed Instances.
  link: [lives in the customers’ AWS account](../facts/ecs.md#ecs-faq-mi-compute-in-your-account-billing)
  link: [management fee per instance, not per task](../facts/ecs.md#ecs-faq-mi-compute-in-your-account-billing)
ecs-faq-mi-ec2-purchase-options
  claim: With ECS Managed Instances you can use familiar EC2 purchase options, such as Reserved Instances or Savings Plans, to optimize the cost of instances.
  scope: Amazon ECS Managed Instances.
  link: [Reserved Instances or Savings Plans](../facts/ecs.md#ecs-faq-mi-ec2-purchase-options)
ecs-faq-mi-instances-visible-but-restricted
  claim: The EC2 instances of ECS Managed Instances are visible in your AWS account through the EC2 console and APIs, but because AWS manages them, certain actions are restricted.
  scope: Amazon ECS Managed Instances.
  link: [visible in your AWS account](../facts/ecs.md#ecs-faq-mi-instances-visible-but-restricted)
ecs-faq-mi-network-modes
  claim: ECS Managed Instances supports two networking modes: awsvpc mode, where each task gets its own elastic network interface with a private IPv4 address, and host mode, where tasks share the network namespace with the host EC2 instance.
  scope: Amazon ECS Managed Instances.
  link: [supports two networking modes](../facts/ecs.md#ecs-faq-mi-network-modes)
ecs-faq-mi-patching-event-windows
  claim: With ECS Managed Instances you can use EC2 event windows to schedule patching within weekly maintenance windows.
  scope: Amazon ECS Managed Instances.
  link: [EC2 event windows](../facts/ecs.md#ecs-faq-mi-patching-event-windows)
ecs-faq-mi-privileged-linux-capabilities
  claim: ECS Managed Instances supports privileged Linux capabilities, including CAP_NET_ADMIN, CAP_SYS_ADMIN and CAP_BPF.
  scope: Amazon ECS Managed Instances.
  link: [supports privileged Linux capabilities](../facts/ecs.md#ecs-faq-mi-privileged-linux-capabilities)
ecs-faq-mi-same-operational-benefits-as-fargate
  claim: Amazon ECS Managed Instances shares the same operational benefits as AWS Fargate: both have AWS-managed operating systems.
  scope: Amazon ECS Managed Instances compared with AWS Fargate.
  link: [both have AWS-managed operating systems](../facts/ecs.md#ecs-faq-mi-same-operational-benefits-as-fargate)
ecs-faq-mi-secured-by-restricting-access
  claim: ECS Managed Instances are secured by restricting SSH access, Amazon SSM, modifying the instance IAM role, modifying the root volume, and attaching additional network interfaces.
  scope: Amazon ECS Managed Instances.
  link: [restricting SSH access, Amazon SSM](../facts/ecs.md#ecs-faq-mi-secured-by-restricting-access)
ecs-faq-network-mode-bridge
  claim: In bridge mode Amazon ECS creates a Linux bridge that connects all containers running on the host in a local virtual network, reached through the host's default network connection.
  scope: Amazon ECS bridge network mode.
  link: [Linux bridge](../facts/ecs.md#ecs-faq-network-mode-bridge)
ecs-faq-network-mode-host
  claim: In host mode Amazon ECS adds containers directly to the host's network stack, which exposes the containers on the host's network with no isolation.
  scope: Amazon ECS host network mode.
  link: [no isolation](../facts/ecs.md#ecs-faq-network-mode-host)
ecs-faq-network-mode-none
  claim: In none mode Amazon ECS disables external networking for containers.
  scope: Amazon ECS none network mode.
  link: [disables external networking](../facts/ecs.md#ecs-faq-network-mode-none)
ecs-faq-network-mode-vpc
  claim: In the VPC network mode, Amazon ECS assigns each running task a dedicated elastic networking interface, which gives containers full networking features in a VPC, just like Amazon EC2 instances.
  scope: Amazon ECS VPC network mode, per task.
  link: [a dedicated elastic networking interface](../facts/ecs.md#ecs-faq-network-mode-vpc)
ecs-faq-no-additional-charge
  claim: Amazon ECS itself has no additional charge; you pay for the AWS resources you create to store and run your application, such as EC2 instances, Fargate resources or EBS volumes.
  scope: Amazon ECS; you pay for the resources you create.
  link: [no additional charge for Amazon ECS](../facts/ecs.md#ecs-faq-no-additional-charge)
ecs-faq-own-ami-allowed
  claim: You can use any AMI that meets the Amazon ECS AMI specification for your container instances.
  scope: Amazon ECS container instances on EC2; the AMI meets the ECS AMI specification.
  link: [Amazon ECS AMI specification](../facts/ecs.md#ecs-faq-own-ami-allowed)
ecs-faq-predefined-fargate-capacity-providers
  claim: Amazon ECS provides predefined capacity providers for Fargate and Fargate Spot capacity for every cluster.
  scope: every Amazon ECS cluster.
  link: [predefined capacity providers](../facts/ecs.md#ecs-faq-predefined-fargate-capacity-providers)
ecs-faq-service-connect-logical-names
  claim: With Amazon ECS Service Connect you define logical names for your service endpoints and use them in client applications to connect to dependencies.
  scope: Amazon ECS Service Connect.
  link: [logical names for your service endpoints](../facts/ecs.md#ecs-faq-service-connect-logical-names)
ecs-faq-service-discovery-cloud-map
  claim: Amazon ECS is integrated with AWS Cloud Map so containerized services can discover and connect with each other.
  scope: Amazon ECS service discovery.
  link: [AWS Cloud Map](../facts/ecs.md#ecs-faq-service-discovery-cloud-map)
ecs-faq-service-metrics-cpu-memory-for-app-auto-scaling
  claim: Amazon ECS measures service utilization from the CPU and memory resources consumed by the tasks of a service and publishes the CloudWatch metrics ECSServiceAverageCPUUtilization and ECSServiceAverageMemoryUtilization; Application Auto Scaling can then use these predefined metrics with scaling policies to proportionally scale the number of tasks in a service.
  scope: Amazon ECS services.
  link: [ECSServiceAverageCPUUtilization](../facts/ecs.md#ecs-faq-service-metrics-cpu-memory-for-app-auto-scaling)
  link: [ECSServiceAverageMemoryUtilization](../facts/ecs.md#ecs-faq-service-metrics-cpu-memory-for-app-auto-scaling)
ecs-faq-service-scheduler-recovers-unhealthy-containers
  claim: The Amazon ECS service scheduler automatically recovers containers that become unhealthy (fail ELB health checks) or stop running, to keep the desired number of healthy containers.
  scope: Amazon ECS services.
  link: [automatically recover containers that become unhealthy](../facts/ecs.md#ecs-faq-service-scheduler-recovers-unhealthy-containers)
ecs-faq-service-scheduler-registers-containers-with-load-balancer
  claim: Amazon ECS automatically registers and deregisters containers from the associated load balancer.
  scope: Amazon ECS services with a load balancer.
  link: [automatically register and deregister your containers](../facts/ecs.md#ecs-faq-service-scheduler-registers-containers-with-load-balancer)
ecs-faq-sla-credit-condition
  claim: You are eligible for an Amazon ECS SLA credit under the Compute SLA if more than one Availability Zone in which you run a task, within the same Region, has a Monthly Uptime Percentage below 99.99% during a monthly billing cycle.
  scope: Amazon ECS, per monthly billing cycle; more than one Availability Zone in the same Region where you run a task.
  link: [less than 99.99%](../facts/ecs.md#ecs-faq-sla-credit-condition)
ecs-faq-sla-monthly-uptime
  claim: The Compute SLA guarantees a Monthly Uptime Percentage of at least 99.99% for Amazon ECS.
  scope: Amazon ECS, Compute SLA, monthly; minimum; at least; measured as Monthly Uptime Percentage.
  link: [99.99%](../facts/ecs.md#ecs-faq-sla-monthly-uptime)
  say: ninety-nine point nine nine percent
ecs-faq-sla-two-commitments
  claim: AWS makes two SLA commitments for Amazon ECS and AWS Fargate: a Multi-AZ Included Container Service SLA for services deployed across multiple AZs, and a Single Task/Pod SLA that governs tasks and pods individually.
  scope: Amazon ECS and AWS Fargate.
  link: [Multi-AZ Included Container Service SLA](../facts/ecs.md#ecs-faq-sla-two-commitments)
  link: [Single Task/Pod SLA](../facts/ecs.md#ecs-faq-sla-two-commitments)
ecs-faq-split-across-capacity-providers
  claim: You can split Amazon ECS tasks and services across multiple capacity providers, for example to run a service in a set percentage split across Fargate and Fargate Spot.
  scope: Amazon ECS tasks and services.
  link: [split them across multiple capacity providers](../facts/ecs.md#ecs-faq-split-across-capacity-providers)
ecs-faq-task-smallest-unit
  claim: Tasks are the smallest unit of compute in Amazon ECS; a task defines a set of containers to place together, their properties, and how they may be linked.
  scope: Amazon ECS.
  link: [smallest unit of compute](../facts/ecs.md#ecs-faq-task-smallest-unit)
ecs-faq-task-uses-iam-role
  claim: Amazon ECS tasks use an IAM role to access services and resources.
  scope: Amazon ECS tasks.
  link: [tasks use an IAM role](../facts/ecs.md#ecs-faq-task-uses-iam-role)
ecs-faq-vs-lambda
  claim: Amazon ECS runs and manages distributed applications that run in containers, while AWS Lambda is an event-driven compute service that runs your code in response to events without you managing compute infrastructure.
  scope: Amazon ECS compared with AWS Lambda.
  link: [container orchestration service](../facts/ecs.md#ecs-faq-vs-lambda)
  link: [event-driven task compute service](../facts/ecs.md#ecs-faq-vs-lambda)
ecs-fargate-capacity-providers-auto-created
  claim: Fargate and Fargate Spot capacity providers are created and managed by Amazon ECS on every cluster, so you do not need to create them.
  scope: every ECS cluster; default; not adjustable.
  link: [managed by Amazon ECS on every cluster](../facts/ecs.md#ecs-fargate-capacity-providers-auto-created)
  link: [you do not need to create them](../facts/ecs.md#ecs-fargate-capacity-providers-auto-created)
ecs-fargate-tasks-launched-per-service-per-minute-limit
  claim: The ECS service scheduler can provision at most 500 tasks per service per minute on AWS Fargate in each of the other supported Regions; in the Regions the quota row lists, such as af-south-1, and in Regions introduced after May 20, 2025, the maximum is 125 tasks per service per minute. The quota is not adjustable.
  scope: per service, per minute, per Region; maximum; not adjustable.
  link: [500 tasks per service per minute](../facts/ecs.md#ecs-fargate-tasks-launched-per-service-per-minute-limit)
  link: [125 tasks per service per minute](../facts/ecs.md#ecs-fargate-tasks-launched-per-service-per-minute-limit)
ecs-fully-managed-orchestration
  claim: Amazon ECS is a fully managed container orchestration service that helps you deploy, manage, and scale containerized applications.
  scope: Amazon ECS.
  link: [fully managed container orchestration service](../facts/ecs.md#ecs-fully-managed-orchestration)
  link: [deploy, manage, and scale containerized applications](../facts/ecs.md#ecs-fully-managed-orchestration)
ecs-iam-role-table-container-instance-role
  claim: The ECS container instance role allows your EC2 instances or external instances to register with the cluster, and it is required when your task is hosted on Amazon EC2 instances or an external instance.
  scope: Amazon ECS IAM roles.
  link: [register with the cluster](../facts/ecs.md#ecs-iam-role-table-container-instance-role)
  link: [Amazon EC2 instances or an external instance](../facts/ecs.md#ecs-iam-role-table-container-instance-role)
ecs-iam-role-table-ecs-anywhere-role
  claim: The Amazon ECS Anywhere role allows your external instances to access AWS APIs, and it is required when your task is hosted on external instances.
  scope: Amazon ECS IAM roles.
  link: [allows your external instances to access AWS APIs](../facts/ecs.md#ecs-iam-role-table-ecs-anywhere-role)
  link: [Your task is hosted on external instances](../facts/ecs.md#ecs-iam-role-table-ecs-anywhere-role)
ecs-iam-role-table-task-role
  claim: The ECS task role allows your application code on the container to use other AWS services, and it is required when your application accesses other AWS services such as Amazon S3.
  scope: Amazon ECS IAM roles.
  link: [use other AWS services](../facts/ecs.md#ecs-iam-role-table-task-role)
  link: [Your application accesses other AWS services](../facts/ecs.md#ecs-iam-role-table-task-role)
ecs-interface-endpoint-privatelink-no-igw-nat
  claim: Amazon ECS interface VPC endpoints are powered by AWS PrivateLink, which lets you privately access the Amazon ECS APIs by using private IP addresses; PrivateLink restricts all network traffic between your VPC and Amazon ECS to the Amazon network, and you don't need an internet gateway, a NAT device, or a virtual private gateway.
  scope: Amazon ECS interface VPC endpoints.
  link: [to the Amazon network](../facts/ecs.md#ecs-interface-endpoint-privatelink-no-igw-nat)
  link: [You don't need an internet gateway](../facts/ecs.md#ecs-interface-endpoint-privatelink-no-igw-nat)
ecs-interface-endpoints-incomplete-traffic-uses-public-endpoint
  claim: In the newer Regions that this consideration covers (see the condition), you must have the Region-specific Amazon ECS interface VPC endpoints that the page lists; if you do not configure all of the endpoints, your traffic will go over the public endpoints, not your VPC endpoint.
  scope: Amazon ECS interface VPC endpoints; Regions introduced starting on December 23, 2023.
  link: [your traffic will go over the public endpoints](../facts/ecs.md#ecs-interface-endpoints-incomplete-traffic-uses-public-endpoint)
  link: [do not configure all of the endpoints](../facts/ecs.md#ecs-interface-endpoints-incomplete-traffic-uses-public-endpoint)
ecs-keep-images-in-same-region-as-workload
  claim: AWS recommends that you host your container images in a repository in the same AWS Region that your workload is in and avoid traversing the internet or a VPN link to download them; Amazon ECR is a high-performance image repository that is available in every Region that Amazon ECS is available in.
  scope: Amazon ECS with Amazon ECR.
  link: [Host your images in a repository](../facts/ecs.md#ecs-keep-images-in-same-region-as-workload)
  link: [Amazon ECR is a high-performance image repository](../facts/ecs.md#ecs-keep-images-in-same-region-as-workload)
ecs-launch-type-only-for-compatibility
  claim: AWS recommends using the launch type only for defining compatibilities in your task definitions, and using capacity providers for launching tasks or services.
  scope: Amazon ECS launch types.
  link: [using the launch type only for defining compatibilities](../facts/ecs.md#ecs-launch-type-only-for-compatibility)
  link: [use capacity providers for launching tasks or services](../facts/ecs.md#ecs-launch-type-only-for-compatibility)
ecs-launch-type-to-launch-type-not-supported
  claim: Launch type to launch type updates of an ECS service are not supported; for example, from the EC2 launch type to the Fargate launch type you use the Fargate capacity provider instead.
  scope: Amazon ECS services.
  link: [launch type updates are not supported](../facts/ecs.md#ecs-launch-type-to-launch-type-not-supported)
  link: [use Fargate capacity provider instead](../facts/ecs.md#ecs-launch-type-to-launch-type-not-supported)
ecs-layer-capacity
  claim: The capacity layer of Amazon ECS is the infrastructure where your containers run.
  scope: Amazon ECS layers.
  link: [infrastructure where your containers run](../facts/ecs.md#ecs-layer-capacity)
  link: [capacity is the infrastructure](../facts/ecs.md#ecs-layer-capacity)
ecs-layer-controller
  claim: The controller layer of Amazon ECS deploys and manages the applications that run on the containers; the ECS scheduler is the software that manages your applications.
  scope: Amazon ECS layers.
  link: [Deploy and manage your applications](../facts/ecs.md#ecs-layer-controller)
  link: [software that manages your applications](../facts/ecs.md#ecs-layer-controller)
ecs-layer-provisioning
  claim: The provisioning layer of Amazon ECS is the set of tools you use to interface with the scheduler to deploy and manage applications and containers.
  scope: Amazon ECS layers.
  link: [tools that you can use to interface](../facts/ecs.md#ecs-layer-provisioning)
  link: [interface with the scheduler](../facts/ecs.md#ecs-layer-provisioning)
ecs-managed-instances-default-instance-selection
  claim: With ECS Managed Instances AWS automatically selects the most cost-optimized general-purpose EC2 instance types that meet your workload needs, or you can specify desired instance attributes including instance types, CPU manufacturers, and accelerators.
  scope: Amazon ECS Managed Instances; default.
  link: [the most cost-optimized general-purpose Amazon EC2 instance types](../facts/ecs.md#ecs-managed-instances-default-instance-selection)
  link: [specify desired instance attributes](../facts/ecs.md#ecs-managed-instances-default-instance-selection)
ecs-managed-instances-fargate-task-definition-compatible
  claim: Amazon ECS Managed Instances is compatible with existing Fargate task definitions that use platform version 1.4.0, and a task definition can specify both Fargate and Managed Instances compatibility.
  scope: Amazon ECS Managed Instances; Fargate platform version 1.4.0.
  link: [compatible with existing Fargate task definitions](../facts/ecs.md#ecs-managed-instances-fargate-task-definition-compatible)
  link: [both Fargate and Amazon ECS Managed Instances compatibility](../facts/ecs.md#ecs-managed-instances-fargate-task-definition-compatible)
ecs-managed-instances-full-range-ec2-aws-manages
  claim: Amazon ECS Managed Instances is a fully managed compute option that runs containers on the full range of Amazon EC2 instance types, with access to GPU acceleration and specialized instance types, while AWS handles provisioning, scaling, patching, and maintenance of the underlying infrastructure.
  scope: Amazon ECS Managed Instances.
  link: [fully managed compute option for Amazon ECS](../facts/ecs.md#ecs-managed-instances-full-range-ec2-aws-manages)
  link: [full range of Amazon EC2 instance types](../facts/ecs.md#ecs-managed-instances-full-range-ec2-aws-manages)
  link: [AWS handles provisioning, scaling, patching, and maintenance](../facts/ecs.md#ecs-managed-instances-full-range-ec2-aws-manages)
ecs-managed-instances-linux-bottlerocket-network-modes
  claim: Amazon ECS Managed Instances support Linux containers and support the awsvpc and host network modes.
  scope: Amazon ECS Managed Instances.
  link: [support Linux containers](../facts/ecs.md#ecs-managed-instances-linux-bottlerocket-network-modes)
  link: [support the `awsvpc` and `host` network modes](../facts/ecs.md#ecs-managed-instances-linux-bottlerocket-network-modes)
ecs-managed-instances-multi-task-placement-default
  claim: By default Amazon ECS Managed Instances runs multiple tasks on a single instance to optimize resource utilization and cost, unlike Fargate, which runs each task in its own isolated environment; if you require strong isolation, you can configure Managed Instances to run each task on a separate instance with VM-level security isolation boundaries.
  scope: Amazon ECS Managed Instances; default; adjustable.
  link: [multiple tasks on a single instance by default](../facts/ecs.md#ecs-managed-instances-multi-task-placement-default)
  link: [VM-level security isolation boundaries](../facts/ecs.md#ecs-managed-instances-multi-task-placement-default)
ecs-managed-instances-need-capacity-provider-strategy
  claim: To run workloads on Amazon ECS Managed Instances, you must use the capacity provider strategy option.
  scope: Amazon ECS services.
  link: [you must use the Capacity provider strategy option](../facts/ecs.md#ecs-managed-instances-need-capacity-provider-strategy)
  link: [run your workloads on Amazon ECS Managed Instances](../facts/ecs.md#ecs-managed-instances-need-capacity-provider-strategy)
ecs-managed-instances-privileged-capabilities-allowed
  claim: ECS Managed Instances can enable advanced networking and system administration functions within containers using privileged Linux capabilities, including CAP_NET_ADMIN, CAP_SYS_ADMIN, CAP_BPF, and CAP_PERFMON; you enable them optionally for workloads that need them.
  scope: Amazon ECS Managed Instances.
  link: [using privileged Linux capabilities](../facts/ecs.md#ecs-managed-instances-privileged-capabilities-allowed)
  link: [You can optionally enable privileged Linux capabilities](../facts/ecs.md#ecs-managed-instances-privileged-capabilities-allowed)
ecs-managed-instances-two-iam-roles
  claim: Amazon ECS Managed Instances requires two IAM roles: an infrastructure role, which allows AWS to manage the Managed Instances on your behalf, and an instance profile, which is a way to pass an IAM role to the Managed Instances.
  scope: Amazon ECS Managed Instances.
  link: [requires two IAM roles](../facts/ecs.md#ecs-managed-instances-two-iam-roles)
  link: [This role allows AWS to manage](../facts/ecs.md#ecs-managed-instances-two-iam-roles)
ecs-managed-termination-protection-only-empty-instances
  claim: With managed termination protection, Amazon ECS only terminates EC2 instances that don't have any running Amazon ECS tasks; tasks run by a service that uses the DAEMON scheduling strategy are ignored, so cluster auto scaling can terminate an instance even when it is running these tasks. You must turn on Auto Scaling instance scale-in protection on the Auto Scaling group to use managed termination protection.
  scope: Amazon ECS cluster auto scaling; Auto Scaling instance scale-in protection must be on.
  link: [don't have any running Amazon ECS tasks](../facts/ecs.md#ecs-managed-termination-protection-only-empty-instances)
  link: [Auto Scaling *instance scale-in protection*](../facts/ecs.md#ecs-managed-termination-protection-only-empty-instances)
ecs-managed-termination-protection-scale-in
  claim: The Auto Scaling group follows its termination policy during scale-in but avoids instances with instance scale-in protection turned on; cluster auto scaling can manage that protection if you turn on managed termination protection.
  scope: Amazon ECS Auto Scaling group capacity providers.
  link: [instance scale-in protection setting turned on](../facts/ecs.md#ecs-managed-termination-protection-scale-in)
  link: [if you turn on managed termination protection](../facts/ecs.md#ecs-managed-termination-protection-scale-in)
ecs-max-percent-example-200-of-four
  claim: With a maximum percent of 200 and a desired task count of four, the ECS scheduler can start four new tasks before it stops four existing tasks.
  scope: per service, rolling update.
  link: [start four new tasks](../facts/ecs.md#ecs-max-percent-example-200-of-four)
ecs-maximum-percent-meaning
  claim: The maximumPercent is the upper limit on the number of tasks that should be running for a service during a rolling deployment or when a container instance is draining, as a percent of the desired number of tasks; the value is rounded down.
  scope: Amazon ECS rolling update deployments; maximum.
  link: [upper limit on the number of tasks](../facts/ecs.md#ecs-maximum-percent-meaning)
  link: [This value is rounded down](../facts/ecs.md#ecs-maximum-percent-meaning)
ecs-min-healthy-percent-example-50-of-four
  claim: With a minimum healthy percent of 50 and a desired task count of four, the ECS scheduler can stop two existing tasks before it starts two new tasks.
  scope: per service, rolling update.
  link: [stop two existing tasks](../facts/ecs.md#ecs-min-healthy-percent-example-50-of-four)
ecs-minimum-healthy-percent-meaning
  claim: The minimumHealthyPercent is the lower limit on the number of tasks that should be running and healthy for a service during a rolling deployment or when a container instance is draining, as a percent of the desired number of tasks; the value is rounded up.
  scope: Amazon ECS rolling update deployments; minimum.
  link: [lower limit on the number of tasks](../facts/ecs.md#ecs-minimum-healthy-percent-meaning)
  link: [This value is rounded up](../facts/ecs.md#ecs-minimum-healthy-percent-meaning)
ecs-network-mode-awsvpc-own-eni
  claim: In the awsvpc network mode the ECS task is allocated its own elastic network interface and a primary private IPv4 or IPv6 address, which gives the task the same networking properties as Amazon EC2 instances.
  scope: Amazon ECS tasks on Amazon EC2; Linux and Windows containers on EC2.
  link: [allocated its own elastic network interface (ENI)](../facts/ecs.md#ecs-network-mode-awsvpc-own-eni)
  link: [same networking properties as Amazon EC2 instances](../facts/ecs.md#ecs-network-mode-awsvpc-own-eni)
ecs-network-mode-bridge-default-linux
  claim: The bridge network mode uses Docker's built-in virtual network on Linux inside each Amazon EC2 instance and is the default network mode on Linux if a network mode isn't specified in the task definition.
  scope: Amazon ECS tasks on Amazon EC2 Linux; default; adjustable; no network mode specified in the task definition.
  link: [the default network mode on Linux](../facts/ecs.md#ecs-network-mode-bridge-default-linux)
  link: [uses the `bridge` Docker network driver](../facts/ecs.md#ecs-network-mode-bridge-default-linux)
ecs-network-mode-host-one-task-per-port
  claim: In the host network mode the task bypasses Docker's virtual network by mapping container ports directly to the ENI of the EC2 instance, dynamic port mappings can't be used, and you can't run multiple tasks of the same task definition on a single instance.
  scope: Amazon ECS tasks on Amazon EC2 Linux; a container must specify a specific hostPort number.
  link: [mapping container ports directly to the ENI](../facts/ecs.md#ecs-network-mode-host-one-task-per-port)
  link: [multiple tasks of the same task definition](../facts/ecs.md#ecs-network-mode-host-one-task-per-port)
ecs-network-mode-none-no-external-connectivity
  claim: In the none network mode the ECS task has no external network connectivity.
  scope: Amazon ECS tasks on Amazon EC2 Linux.
  link: [The task has no external network connectivity](../facts/ecs.md#ecs-network-mode-none-no-external-connectivity)
  link: [`none`](../facts/ecs.md#ecs-network-mode-none-no-external-connectivity)
ecs-no-control-plane-to-manage
  claim: You can run and scale ECS container workloads across AWS Regions in the cloud and on premises without managing a control plane.
  scope: Amazon ECS.
  link: [without the complexity of managing a control plane](../facts/ecs.md#ecs-no-control-plane-to-manage)
  link: [across AWS Regions in the cloud, and on-premises](../facts/ecs.md#ecs-no-control-plane-to-manage)
ecs-no-health-check-counts-after-40-seconds
  claim: For a service without a load balancer, if a task has no essential container with a health check, the ECS scheduler waits 40 seconds after the task reaches RUNNING before it counts the task toward the minimum healthy percent.
  scope: per task, service that does not use a load balancer.
  link: [40 seconds](../facts/ecs.md#ecs-no-health-check-counts-after-40-seconds)
ecs-one-task-definition-family-per-business-purpose
  claim: Use each task definition family for only one business purpose, because if you group multiple types of application containers in one task definition you cannot scale those containers independently; also use a different IAM role for each task definition family.
  scope: Amazon ECS task definition guidelines.
  link: [for only one business purpose](../facts/ecs.md#ecs-one-task-definition-family-per-business-purpose)
  link: [different IAM roles for each task definition family](../facts/ecs.md#ecs-one-task-definition-family-per-business-purpose)
ecs-overprovision-for-az-failure-two-or-three-azs
  claim: To have immediate capacity if an Availability Zone fails, an ECS application that runs in two Availability Zones needs double its normal task count, and one that runs in three Availability Zones should run 1.5 times its normal task count, that is three tasks for every two needed for ordinary serving.
  scope: Amazon ECS services; headroom to serve demand after the loss of one Availability Zone.
  link: [you need to double your normal task count](../facts/ecs.md#ecs-overprovision-for-az-failure-two-or-three-azs)
  link: [If your application runs in three Availability Zones, we recommend that you run 1.5 times your normal task count](../facts/ecs.md#ecs-overprovision-for-az-failure-two-or-three-azs)
ecs-placement-binpack-least-unused-cpu-memory
  claim: With the binpack placement strategy, tasks are placed on container instances so as to leave the least amount of unused CPU or memory, which minimizes the number of container instances in use; on scale-in, ECS terminates the task on the instance that has the most resources left after the task ends.
  scope: Amazon ECS task placement on EC2; field is cpu or memory.
  link: [the least amount of unused CPU or memory](../facts/ecs.md#ecs-placement-binpack-least-unused-cpu-memory)
  link: [minimizes the number of container instances in use](../facts/ecs.md#ecs-placement-binpack-least-unused-cpu-memory)
ecs-placement-spread-balance-across-azs-on-scale-in
  claim: With the spread placement strategy, tasks are placed evenly based on the specified value, and on scale-in Amazon ECS selects tasks to terminate that maintain a balance across Availability Zones, choosing at random within an Availability Zone.
  scope: Amazon ECS task placement on EC2; field instanceId or an attribute such as attribute:ecs.availability-zone.
  link: [placed evenly based on the specified value](../facts/ecs.md#ecs-placement-spread-balance-across-azs-on-scale-in)
  link: [maintain a balance across Availability Zones](../facts/ecs.md#ecs-placement-spread-balance-across-azs-on-scale-in)
ecs-placement-strategies-best-effort-constraints-binding
  claim: ECS task placement strategies are a best effort and ECS still tries to place tasks when the optimal option is unavailable, but task placement constraints are binding and can prevent task placement.
  scope: Amazon ECS task placement on EC2.
  link: [Task placement strategies are a best effort](../facts/ecs.md#ecs-placement-strategies-best-effort-constraints-binding)
  link: [task placement constraints are binding](../facts/ecs.md#ecs-placement-strategies-best-effort-constraints-binding)
ecs-placement-strategy-default-for-services-spread-az
  claim: For tasks running as part of an ECS service, the default task placement strategy is spread using the attribute ecs.availability-zone; there is no default task placement constraint for tasks not in services.
  scope: Amazon ECS tasks in a service; default; adjustable; standalone tasks have no default strategy listed.
  link: [`spread` using the `attribute:ecs.availability-zone`](../facts/ecs.md#ecs-placement-strategy-default-for-services-spread-az)
  link: [There isn't a default task placement constraint](../facts/ecs.md#ecs-placement-strategy-default-for-services-spread-az)
ecs-placement-strategy-types-binpack-random-spread
  claim: The random placement strategy randomly places tasks on available candidates, the spread strategy spreads placement evenly across available candidates based on the field parameter, and the binpack strategy places tasks on available candidates that have the least available amount of the resource specified with the field parameter.
  scope: Amazon ECS task placement strategies.
  link: [randomly places tasks on available candidates](../facts/ecs.md#ecs-placement-strategy-types-binpack-random-spread)
  link: [spreads placement across available candidates evenly](../facts/ecs.md#ecs-placement-strategy-types-binpack-random-spread)
  link: [the least available amount of the resource](../facts/ecs.md#ecs-placement-strategy-types-binpack-random-spread)
ecs-predictive-scaling-historical-patterns
  claim: ECS predictive scaling looks at past load data to analyze daily or weekly patterns and proactively increases tasks in your service for anticipated needs; it is most useful for cyclical traffic, recurring on-and-off workloads and applications with long initialization times.
  scope: Amazon ECS service predictive scaling.
  link: [analyze daily or weekly patterns](../facts/ecs.md#ecs-predictive-scaling-historical-patterns)
  link: [Applications with long initialization times](../facts/ecs.md#ecs-predictive-scaling-historical-patterns)
ecs-predictive-scaling-needs-24-hours-of-history
  claim: Before ECS predictive scaling can start forecasting, it needs at least 24 hours of historical data. More data gives a better forecast, with two weeks being ideal.
  scope: per ECS service; minimum.
  link: [24 hours of historical data](../facts/ecs.md#ecs-predictive-scaling-needs-24-hours-of-history)
  link: [two weeks being ideal](../facts/ecs.md#ecs-predictive-scaling-needs-24-hours-of-history)
ecs-predictive-scaling-service-level-not-compute
  claim: ECS predictive scaling is a service-level capability that scales the tasks of your service independently from the scaling of the underlying compute capacity; for Fargate, AWS manages and automatically scales the underlying capacity.
  scope: Amazon ECS service predictive scaling.
  link: [a service-level capability](../facts/ecs.md#ecs-predictive-scaling-service-level-not-compute)
  link: [AWS manages and automatically scales the underlying capacity](../facts/ecs.md#ecs-predictive-scaling-service-level-not-compute)
ecs-pricing-ec2-no-additional-charge
  claim: For the Amazon EC2 compute option, ECS adds no extra charge. You pay for the AWS resources you create to run your application, such as EC2 instances, EBS volumes or public IPv4 addresses.
  scope: per account.
  link: [no additional charge for Amazon EC2 compute](../facts/ecs.md#ecs-pricing-ec2-no-additional-charge)
ecs-pricing-managed-instances-management-fee
  claim: For ECS Managed Instances you pay a management fee for the Amazon EC2 instances that ECS launches and manages, in addition to standard EC2 instance charges.
  scope: per instance.
  link: [management fee](../facts/ecs.md#ecs-pricing-managed-instances-management-fee)
ecs-pricing-managed-instances-per-second-one-minute
  claim: Both the ECS Managed Instances fee and the EC2 charges are billed per second, with a one-minute minimum, based on instance type and duration.
  scope: per instance; minimum.
  link: [billed per-second, with a one-minute minimum](../facts/ecs.md#ecs-pricing-managed-instances-per-second-one-minute)
ecs-private-registry-credentials-secrets-manager
  claim: With private registry authentication you store your credentials in AWS Secrets Manager and reference them in your ECS task definition, so you can use container images from private registries outside of AWS that require authentication; this is supported by tasks hosted on Fargate, Amazon EC2 instances, and external instances using Amazon ECS Anywhere.
  scope: Amazon ECS private registry authentication.
  link: [store your credentials in AWS Secrets Manager](../facts/ecs.md#ecs-private-registry-credentials-secrets-manager)
  link: [Fargate, Amazon EC2 instances, and external instances](../facts/ecs.md#ecs-private-registry-credentials-secrets-manager)
ecs-private-registry-secret-cross-region-account
  claim: The Secrets Manager secret that holds private registry credentials for an ECS task can be from a different AWS Region or a different account than the task using it.
  scope: Amazon ECS private registry authentication.
  link: [a different AWS Region or a different account](../facts/ecs.md#ecs-private-registry-secret-cross-region-account)
  link: [`repositoryCredentials` object](../facts/ecs.md#ecs-private-registry-secret-cross-region-account)
ecs-production-multi-az-lose-an-az
  claim: AWS recommends that production workloads on Amazon ECS be served from multiple Availability Zones, because if an Availability Zone fails the tasks running in the remaining Availability Zones can still serve the demand.
  scope: Amazon ECS services.
  link: [served from multiple Availability Zones](../facts/ecs.md#ecs-production-multi-az-lose-an-az)
  link: [can still serve the demand](../facts/ecs.md#ecs-production-multi-az-lose-an-az)
ecs-provisioning-tasks-per-cluster-limit
  claim: At most 500 tasks can wait in the PROVISIONING state in one cluster. The quota applies only to tasks launched with an EC2 Auto Scaling group capacity provider. It is not adjustable.
  scope: per cluster, per Region; maximum; not adjustable; only for tasks launched with an EC2 Auto Scaling group capacity provider.
  link: [500 tasks](../facts/ecs.md#ecs-provisioning-tasks-per-cluster-limit)
ecs-replica-strategy-default-spreads-azs
  claim: If no scheduling strategy is specified, the REPLICA strategy is used; the replica strategy places and maintains the desired number of tasks across your cluster and by default the service scheduler spreads tasks across Availability Zones.
  scope: Amazon ECS services; default; adjustable; applies when no scheduling strategy is specified.
  link: [the `REPLICA` strategy is used](../facts/ecs.md#ecs-replica-strategy-default-spreads-azs)
  link: [spreads tasks across Availability Zones](../facts/ecs.md#ecs-replica-strategy-default-spreads-azs)
ecs-rolling-maximum-percent-default-200
  claim: The default maximumPercent for an ECS service that uses the REPLICA service scheduler is 200%.
  scope: per service, REPLICA scheduler, rolling update (ECS) deployment type; default; adjustable.
  link: [200%](../facts/ecs.md#ecs-rolling-maximum-percent-default-200)
ecs-rolling-minimum-healthy-percent-default-100
  claim: The default minimumHealthyPercent for an ECS replica service is 100%.
  scope: per service, replica service; default; adjustable.
  link: [100%](../facts/ecs.md#ecs-rolling-minimum-healthy-percent-default-100)
ecs-rolling-update-replaces-tasks
  claim: With the rolling update (ECS) deployment type, the ECS service scheduler replaces the currently running tasks with new tasks, and the service deployment configuration controls how many tasks are added or removed during the update.
  scope: Amazon ECS rolling update deployments.
  link: [replaces the currently running tasks with new tasks](../facts/ecs.md#ecs-rolling-update-replaces-tasks)
  link: [controlled by the service deployment configuration](../facts/ecs.md#ecs-rolling-update-replaces-tasks)
ecs-scale-out-before-known-demand-shock
  claim: Because autoscaling can take time, AWS recommends that you scale out your application before the demand shock begins, and says the best way to prepare for unscheduled shocks is to over-provision resources.
  scope: Amazon ECS service auto scaling.
  link: [before the demand shock begins](../facts/ecs.md#ecs-scale-out-before-known-demand-shock)
  link: [over-provision resources](../facts/ecs.md#ecs-scale-out-before-known-demand-shock)
ecs-scaling-target-headroom-60-80-percent
  claim: As a good practice you can set your ECS scaling target between 60-80% of utilization so the application can better handle bursts of extra demand while additional capacity is still being provisioned.
  scope: Amazon ECS service auto scaling; recommendation, not a limit.
  link: [scaling target between 60-80% of utilization](../facts/ecs.md#ecs-scaling-target-headroom-60-80-percent)
  link: [better handle bursts of extra demand](../facts/ecs.md#ecs-scaling-target-headroom-60-80-percent)
ecs-security-groups-per-awsvpc-configuration-limit
  claim: An awsvpcConfiguration can specify at most 5 security groups. The quota is not adjustable.
  scope: per awsvpcConfiguration, per Region; maximum; not adjustable.
  link: [5 security groups](../facts/ecs.md#ecs-security-groups-per-awsvpc-configuration-limit)
ecs-service-auto-scaling-application-auto-scaling
  claim: ECS service auto scaling is the ability to automatically increase or decrease the desired number of tasks in your service, and Amazon ECS uses the Application Auto Scaling service to provide this.
  scope: Amazon ECS services.
  link: [increase or decrease the desired number](../facts/ecs.md#ecs-service-auto-scaling-application-auto-scaling)
  link: [leverages the Application Auto Scaling service](../facts/ecs.md#ecs-service-auto-scaling-application-auto-scaling)
ecs-service-auto-scaling-scale-in-blocked-during-deployment
  claim: Application Auto Scaling turns off scale-in processes while ECS deployments are in progress, while scale-out processes continue unless suspended; this does not apply to services that use the external deployment controller.
  scope: Amazon ECS service auto scaling; not for the external deployment controller.
  link: [turns off scale-in processes](../facts/ecs.md#ecs-service-auto-scaling-scale-in-blocked-during-deployment)
  link: [scale-out processes continue to occur, unless suspended](../facts/ecs.md#ecs-service-auto-scaling-scale-in-blocked-during-deployment)
ecs-service-auto-scaling-types-target-step-scheduled-predictive
  claim: Amazon ECS Service Auto Scaling supports target tracking on a target value for a metric, step scaling with step adjustments based on CloudWatch alarms, scheduled actions based on date and time, predictive scaling based on historical load, and scaling on an Amazon SQS queue backlog.
  scope: Amazon ECS services.
  link: [a target value for a specific metric](../facts/ecs.md#ecs-service-auto-scaling-types-target-step-scheduled-predictive)
  link: [known as step adjustments](../facts/ecs.md#ecs-service-auto-scaling-types-target-step-scheduled-predictive)
  link: [based on the date and time](../facts/ecs.md#ecs-service-auto-scaling-types-target-step-scheduled-predictive)
  link: [detect daily or weekly patterns in traffic flows](../facts/ecs.md#ecs-service-auto-scaling-types-target-step-scheduled-predictive)
  link: [backlog of messages in an Amazon SQS queue](../facts/ecs.md#ecs-service-auto-scaling-types-target-step-scheduled-predictive)
ecs-service-connect-builds-discovery-and-mesh
  claim: Amazon ECS Service Connect manages service-to-service communication as ECS configuration and builds both service discovery and a service mesh in Amazon ECS.
  scope: Amazon ECS Service Connect.
  link: [builds both service discovery and a service mesh](../facts/ecs.md#ecs-service-connect-builds-discovery-and-mesh)
  link: [management of service-to-service communication as Amazon ECS configuration](../facts/ecs.md#ecs-service-connect-builds-discovery-and-mesh)
ecs-service-connect-proxy-container-in-each-task
  claim: Service Connect defines a proxy container in the Amazon ECS service, so each task that the service makes runs a proxy container in the task.
  scope: Amazon ECS Service Connect.
  link: [runs a proxy container in the task](../facts/ecs.md#ecs-service-connect-proxy-container-in-each-task)
  link: [the proxy container in the Amazon ECS service](../facts/ecs.md#ecs-service-connect-proxy-container-in-each-task)
ecs-service-connect-recommended-for-service-to-service
  claim: If you need external connections from the internet, AWS recommends Elastic Load Balancing; to connect an application to other applications that run in Amazon ECS services without a load balancer, AWS recommends Service Connect, which provides Amazon ECS configuration for service discovery, connectivity, and traffic monitoring, and lets your applications use short names and standard ports to connect to Amazon ECS services.
  scope: Amazon ECS service interconnection.
  link: [We recommend Service Connect](../facts/ecs.md#ecs-service-connect-recommended-for-service-to-service)
  link: [we recommend using Elastic Load Balancing](../facts/ecs.md#ecs-service-connect-recommended-for-service-to-service)
ecs-service-connect-same-namespace-only
  claim: Service Connect is suitable for connections between Amazon ECS services within the same namespace, and each Amazon ECS service can belong to only one namespace.
  scope: Amazon ECS Service Connect.
  link: [within the same namespace](../facts/ecs.md#ecs-service-connect-same-namespace-only)
  link: [can belong to only one namespace](../facts/ecs.md#ecs-service-connect-same-namespace-only)
ecs-service-connecting-options-without-load-balancer
  claim: Without a load balancer, Amazon ECS services can connect to each other with Service Connect (short names and standard ports), service discovery (Route 53 namespace, DNS) or Amazon VPC Lattice (fully managed application networking, which has a cost).
  scope: Amazon ECS services.
  link: [automatic discovery using short names and standard ports](../facts/ecs.md#ecs-service-connecting-options-without-load-balancer)
  link: [Service discovery uses Route 53 to create a namespace for your service](../facts/ecs.md#ecs-service-connecting-options-without-load-balancer)
  link: [a fully managed application networking service](../facts/ecs.md#ecs-service-connecting-options-without-load-balancer)
ecs-service-discovery-cloud-map-dns
  claim: With ECS service discovery, Amazon ECS syncs the list of launched tasks to AWS Cloud Map, which maintains a DNS hostname that resolves to the internal IP addresses of one or more tasks from that service.
  scope: Amazon ECS service discovery.
  link: [syncs the list of launched tasks](../facts/ecs.md#ecs-service-discovery-cloud-map-dns)
  link: [resolves to the internal IP addresses](../facts/ecs.md#ecs-service-discovery-cloud-map-dns)
ecs-service-discovery-retry-logic-disadvantage
  claim: The main disadvantage of direct service-to-service communication using service discovery is that you must implement extra logic to have retries and deal with connection failures; DNS records have a time-to-live (TTL) period that controls how long they are cached for.
  scope: Amazon ECS service discovery.
  link: [extra logic to have retries](../facts/ecs.md#ecs-service-discovery-retry-logic-disadvantage)
  link: [DNS records have a time-to-live (TTL) period](../facts/ecs.md#ecs-service-discovery-retry-logic-disadvantage)
ecs-service-maintains-desired-count
  claim: An ECS service runs and maintains a specified number of instances of a task definition in a cluster; if a task fails or stops, the service scheduler launches another instance to replace it and so keeps the desired number of tasks.
  scope: Amazon ECS services.
  link: [maintain a specified number of instances](../facts/ecs.md#ecs-service-maintains-desired-count)
  link: [launches another instance of your task definition](../facts/ecs.md#ecs-service-maintains-desired-count)
ecs-service-optional-load-balancer
  claim: You can optionally run an ECS service behind a load balancer, which distributes traffic across the tasks associated with the service.
  scope: Amazon ECS services.
  link: [optionally run your service behind a load balancer](../facts/ecs.md#ecs-service-optional-load-balancer)
  link: [distributes traffic across the tasks](../facts/ecs.md#ecs-service-optional-load-balancer)
ecs-service-scheduler-for-long-running-stateless
  claim: AWS recommends the ECS service scheduler for long running stateless services and applications.
  scope: Amazon ECS service scheduler.
  link: [long running stateless services and applications](../facts/ecs.md#ecs-service-scheduler-for-long-running-stateless)
  link: [use the service scheduler](../facts/ecs.md#ecs-service-scheduler-for-long-running-stateless)
ecs-service-scheduler-replaces-unhealthy-tasks
  claim: The ECS service scheduler also replaces tasks that are determined to be unhealthy after a container health check or a load balancer target group health check fails.
  scope: Amazon ECS service scheduler.
  link: [container health check](../facts/ecs.md#ecs-service-scheduler-replaces-unhealthy-tasks)
  link: [load balancer target group health check](../facts/ecs.md#ecs-service-scheduler-replaces-unhealthy-tasks)
ecs-service-scheduler-reschedules-on-infrastructure-failure
  claim: The ECS service scheduler reschedules tasks when a task fails; for example, if the underlying infrastructure fails, the service scheduler reschedules a task.
  scope: Amazon ECS service scheduler.
  link: [reschedules tasks when a task fails](../facts/ecs.md#ecs-service-scheduler-reschedules-on-infrastructure-failure)
  link: [if the underlying infrastructure fails](../facts/ecs.md#ecs-service-scheduler-reschedules-on-infrastructure-failure)
ecs-service-throttle-logic-failed-starts
  claim: If a task is stopped without having entered the RUNNING state, the ECS service scheduler slows down launch attempts and sends a service event message; normal scheduling resumes after the service is updated.
  scope: Amazon ECS service scheduler.
  link: [slow down the launch attempts](../facts/ecs.md#ecs-service-throttle-logic-failed-starts)
  link: [sends out a service event message](../facts/ecs.md#ecs-service-throttle-logic-failed-starts)
ecs-service-to-strategy-needs-new-deployment
  claim: A service can be updated to use a capacity provider strategy rather than a launch type, but you must force a new deployment when you do so; a service that uses an Auto Scaling group capacity provider cannot be updated to a Fargate capacity provider, and the opposite is also the case.
  scope: Amazon ECS services.
  link: [you must force a new deployment](../facts/ecs.md#ecs-service-to-strategy-needs-new-deployment)
  link: [You can't update a service](../facts/ecs.md#ecs-service-to-strategy-needs-new-deployment)
ecs-services-per-cluster-limit
  claim: One ECS cluster can have at most 5,000 services. The quota is not adjustable.
  scope: per cluster, per Region; maximum; not adjustable.
  link: [5,000 services](../facts/ecs.md#ecs-services-per-cluster-limit)
ecs-services-per-namespace-limit
  claim: At most 300 services can run within one ECS namespace. The quota is not adjustable.
  scope: per namespace, per Region; maximum; not adjustable.
  link: [300 services](../facts/ecs.md#ecs-services-per-namespace-limit)
ecs-spot-fleet-capacity-provider-only
  claim: Spot Fleet is available only as a capacity provider and not as a launch type.
  scope: Amazon ECS.
  link: [only available as a capacity provider](../facts/ecs.md#ecs-spot-fleet-capacity-provider-only)
  link: [not as a launch type](../facts/ecs.md#ecs-spot-fleet-capacity-provider-only)
ecs-sqs-scale-in-protection-task-processing
  claim: When an ECS service scales in, Service Auto Scaling can stop a task that is still processing a message, which for long-running or non-idempotent work can cause the message to be reprocessed or its progress to be lost; to prevent this, use task scale-in protection to mark a task as protected while it is doing active work.
  scope: Amazon ECS service auto scaling with Amazon SQS.
  link: [stop a task that is still processing](../facts/ecs.md#ecs-sqs-scale-in-protection-task-processing)
  link: [use task scale-in protection](../facts/ecs.md#ecs-sqs-scale-in-protection-task-processing)
ecs-sqs-scale-on-backlog-per-task
  claim: To scale an ECS service on an Amazon SQS queue, AWS recommends scaling on the backlog per task, which is the queue depth divided by the number of running tasks, rather than on queue depth directly.
  scope: Amazon ECS service auto scaling with Amazon SQS.
  link: [scale on the *backlog per task*](../facts/ecs.md#ecs-sqs-scale-on-backlog-per-task)
  link: [not a reliable metric to scale on directly](../facts/ecs.md#ecs-sqs-scale-on-backlog-per-task)
ecs-strategy-fargate-or-asg-not-both
  claim: A capacity provider strategy can only contain either Fargate or Auto Scaling group capacity providers, but not both, although a cluster can contain a mix of both.
  scope: per capacity provider strategy.
  link: [either Fargate or Auto Scaling group capacity providers](../facts/ecs.md#ecs-strategy-fargate-or-asg-not-both)
  link: [but not both](../facts/ecs.md#ecs-strategy-fargate-or-asg-not-both)
ecs-strategy-only-one-base
  claim: In a capacity provider strategy only one capacity provider can have a defined base value; if no base is specified, the default is zero.
  scope: per capacity provider strategy; default.
  link: [can have a defined base value](../facts/ecs.md#ecs-strategy-only-one-base)
  link: [the default value of zero is used](../facts/ecs.md#ecs-strategy-only-one-base)
ecs-strategy-update-moves-service-between-compute-types
  claim: You can update the capacity provider strategy of an ECS service to move it from one compute type to another.
  scope: Amazon ECS services.
  link: [update a capacity provider strategy for a service](../facts/ecs.md#ecs-strategy-update-moves-service-between-compute-types)
  link: [from one compute type to the other](../facts/ecs.md#ecs-strategy-update-moves-service-between-compute-types)
ecs-strategy-weight-zero-not-used
  claim: When a capacity provider strategy lists several capacity providers, at least one must have a weight greater than zero; providers with a weight of zero are not used to place tasks, and a strategy where all weights are zero makes RunTask or CreateService fail.
  scope: per capacity provider strategy; when multiple capacity providers are specified.
  link: [a weight value that's greater than zero](../facts/ecs.md#ecs-strategy-weight-zero-not-used)
  link: [a weight of zero aren't used](../facts/ecs.md#ecs-strategy-weight-zero-not-used)
ecs-subnets-per-awsvpc-configuration-limit
  claim: An awsvpcConfiguration can specify at most 16 subnets. The quota is not adjustable.
  scope: per awsvpcConfiguration, per Region; maximum; not adjustable.
  link: [16 subnets](../facts/ecs.md#ecs-subnets-per-awsvpc-configuration-limit)
ecs-tags-per-resource-limit
  claim: An ECS task definition, cluster, task or service can have at most 50 tags. The quota is not adjustable.
  scope: per resource (task definition, cluster, task, service), per Region; maximum; not adjustable.
  link: [50 tags](../facts/ecs.md#ecs-tags-per-resource-limit)
ecs-target-capacity-below-100-keeps-spare-instances
  claim: A targetCapacity value of less than 100% on an ECS Auto Scaling group capacity provider represents the amount of free capacity (EC2 instances) that needs to be present in the cluster, and spare capacity helps future tasks launch more quickly because the Auto Scaling group does not have to launch more instances.
  scope: Amazon ECS Auto Scaling group capacity providers.
  link: [the amount of free capacity](../facts/ecs.md#ecs-target-capacity-below-100-keeps-spare-instances)
  link: [helps future tasks launch more quickly](../facts/ecs.md#ecs-target-capacity-below-100-keeps-spare-instances)
ecs-target-groups-per-service-limit
  claim: An ECS service that uses an Application Load Balancer or a Network Load Balancer can have at most 5 target groups. The quota is not adjustable.
  scope: per service, per Region; maximum; not adjustable; service uses an Application Load Balancer or a Network Load Balancer.
  link: [5 target groups](../facts/ecs.md#ecs-target-groups-per-service-limit)
ecs-target-tracking-easiest-step-scaling-reacts-faster
  claim: For ECS services, target tracking is the easiest scaling mode to use, since all you need to do is set a target value for a metric such as CPU average utilization, while step scaling lets you react more quickly because you define the thresholds and how many tasks to add or remove.
  scope: Amazon ECS service auto scaling.
  link: [Target tracking is the easiest mode to use](../facts/ecs.md#ecs-target-tracking-easiest-step-scaling-reacts-faster)
  link: [more quickly react to changes in demand](../facts/ecs.md#ecs-target-tracking-easiest-step-scaling-reacts-faster)
ecs-target-tracking-scale-out-fast-scale-in-slow
  claim: To ensure application availability, an ECS service with target tracking scales out proportionally to the metric as fast as it can but scales in more gradually; with several target tracking policies it scales out if any is ready but scales in only if all are ready.
  scope: Amazon ECS target tracking scaling policies.
  link: [as fast as it can](../facts/ecs.md#ecs-target-tracking-scale-out-fast-scale-in-slow)
  link: [scales in more gradually](../facts/ecs.md#ecs-target-tracking-scale-out-fast-scale-in-slow)
ecs-task-definition-json-blueprint
  claim: A task definition is a blueprint for your application: a text file in JSON format that describes the parameters and one or more containers that form your application.
  scope: Amazon ECS task definitions.
  link: [a text file in JSON format](../facts/ecs.md#ecs-task-definition-json-blueprint)
  link: [a blueprint for your application](../facts/ecs.md#ecs-task-definition-json-blueprint)
ecs-task-definition-revision-maps-to-app-version
  claim: Create a one-to-one mapping between a version of application code, a container image tag, and a task definition revision; each revision is a point-in-time snapshot of the settings for a particular container image.
  scope: Amazon ECS task definition guidelines.
  link: [Create a one-to-one mapping](../facts/ecs.md#ecs-task-definition-revision-maps-to-app-version)
  link: [a point-in-time snapshot of the settings](../facts/ecs.md#ecs-task-definition-revision-maps-to-app-version)
ecs-task-definition-revisions-per-family-limit
  claim: One task definition family can have at most 1,000,000 revisions. Deregistering or deleting a revision does not exclude it from this count. The quota is not adjustable.
  scope: per task definition family, per Region; maximum; not adjustable.
  link: [1,000,000 revisions](../facts/ecs.md#ecs-task-definition-revisions-per-family-limit)
ecs-task-definition-size-limit
  claim: A task definition can be at most 64 Kilobytes in size. The description of the quota gives the unit as KiB. The quota is not adjustable.
  scope: per task definition, per Region; maximum; not adjustable.
  link: [64 Kilobytes](../facts/ecs.md#ecs-task-definition-size-limit)
ecs-task-execution-role-for-agents
  claim: The ECS task execution role grants the Amazon ECS container and Fargate agents permission to make AWS API calls on your behalf; its permissions are not directly accessible by the containers in the task.
  scope: Amazon ECS task execution IAM role.
  link: [grants the Amazon ECS container and Fargate agents](../facts/ecs.md#ecs-task-execution-role-for-agents)
  link: [aren't directly accessible by the containers](../facts/ecs.md#ecs-task-execution-role-for-agents)
ecs-task-execution-role-use-cases
  claim: The task execution IAM role is required depending on the requirements of your task. Common use cases: a task hosted on AWS Fargate, Amazon ECS Managed Instances or an external instance that pulls a container image from an Amazon ECR private repository or sends container logs to CloudWatch Logs using the awslogs log driver; and a task hosted on AWS Fargate or Amazon EC2 instances whose task definition references sensitive data using Secrets Manager secrets or AWS Systems Manager Parameter Store parameters.
  scope: Amazon ECS task execution IAM role.
  link: [an Amazon ECR private repository](../facts/ecs.md#ecs-task-execution-role-use-cases)
  link: [the `awslogs` log driver](../facts/ecs.md#ecs-task-execution-role-use-cases)
  link: [references sensitive data using Secrets Manager secrets](../facts/ecs.md#ecs-task-execution-role-use-cases)
ecs-task-is-instantiation-of-task-definition
  claim: A task is the instantiation of a task definition within a cluster, and after you create a task definition you can run it as a task or a service.
  scope: Amazon ECS tasks.
  link: [the instantiation of a task definition](../facts/ecs.md#ecs-task-is-instantiation-of-task-definition)
  link: [as a task or a service](../facts/ecs.md#ecs-task-is-instantiation-of-task-definition)
ecs-task-role-credentials-exclusive-no-instance-inheritance
  claim: When you specify an IAM role for a task, the AWS CLI or SDKs in its containers use the credentials of the task role exclusively and do not inherit any IAM permissions from the EC2 or external instance they run on.
  scope: Amazon ECS task IAM role.
  link: [provided by the task role exclusively](../facts/ecs.md#ecs-task-role-credentials-exclusive-no-instance-inheritance)
  link: [do not inherit any IAM permissions](../facts/ecs.md#ecs-task-role-credentials-exclusive-no-instance-inheritance)
ecs-task-role-fargate-no-instance-profile
  claim: On ECS Fargate, EC2 instance profiles are not available for containers in your tasks; task IAM roles let you associate IAM permissions with your containers irrespective of the compute option when you use the AWS SDK or AWS CLI in your containers, and CloudTrail logs show which task the role credentials were vended for.
  scope: Amazon ECS task IAM role.
  link: [EC2 instance profiles are not available](../facts/ecs.md#ecs-task-role-fargate-no-instance-profile)
  link: [CloudTrail logs show which task](../facts/ecs.md#ecs-task-role-fargate-no-instance-profile)
ecs-task-role-gives-app-code-aws-permissions
  claim: The ECS task IAM role allows application code running in the container to use other AWS services, such as Amazon S3; its permissions are vended to the containers in the task and are not accessed by the ECS container and Fargate agents.
  scope: Amazon ECS task IAM role.
  link: [allows your application code (running in the container)](../facts/ecs.md#ecs-task-role-gives-app-code-aws-permissions)
  link: [aren't accessed by the Amazon ECS container](../facts/ecs.md#ecs-task-role-gives-app-code-aws-permissions)
ecs-task-role-least-privilege-per-task-definition
  claim: If you have multiple task definitions or services that need IAM permissions, consider creating a role for each specific task definition or service with the minimum required permissions to minimize the access you provide to each task.
  scope: Amazon ECS task IAM role.
  link: [a role for each specific task definition](../facts/ecs.md#ecs-task-role-least-privilege-per-task-definition)
  link: [minimum required permissions for the tasks to operate](../facts/ecs.md#ecs-task-role-least-privilege-per-task-definition)
ecs-task-size-load-test-for-requirements
  claim: Load testing your application is the key to successful resource requirement planning for ECS task sizes; a limit is the maximum CPU or memory a container or task can use, CPU above the limit is throttled and memory above the limit stops the container.
  scope: Amazon ECS task sizing.
  link: [Load testing your application is the key](../facts/ecs.md#ecs-task-size-load-test-for-requirements)
  link: [your container being stopped](../facts/ecs.md#ecs-task-size-load-test-for-requirements)
ecs-task-size-stateless-small-reservations-cost
  claim: For stateless applications that scale horizontally, smaller CPU reservations such as 256 CPU units (1/4 vCPU) scale out in a fine-grained way that minimizes cost but might not scale fast enough for big spikes, while larger CPU reservations scale faster but cost more.
  scope: Amazon ECS task sizing.
  link: [a fine-grained way that minimizes cost](../facts/ecs.md#ecs-task-size-stateless-small-reservations-cost)
  link: [larger CPU reservations are more costly](../facts/ecs.md#ecs-task-size-stateless-small-reservations-cost)
ecs-tasks-per-run-task-limit
  claim: One RunTask API call can launch at most 10 tasks. The quota is not adjustable.
  scope: per RunTask API action, per Region; maximum; not adjustable.
  link: [10 tasks](../facts/ecs.md#ecs-tasks-per-run-task-limit)
ecs-tasks-per-service-limit
  claim: One ECS service can have at most 5,000 tasks (the desired count) in each supported Region, and the quota is not adjustable; services configured to use Amazon ECS service discovery have a limit of 1,000 tasks per service because of the AWS Cloud Map service quota.
  scope: per service, per Region; maximum; not adjustable.
  link: [5,000 tasks](../facts/ecs.md#ecs-tasks-per-service-limit)
  link: [1,000 tasks per service](../facts/ecs.md#ecs-tasks-per-service-limit)
ecs-whitepaper-batch-runs-on-fargate-or-ec2
  claim: AWS Batch runs batch computing workloads as containerized applications on AWS Fargate or Amazon EC2 resources in your compute environment, and AWS Batch can scale compute capacity on Amazon EC2 instances, Fargate resources, and Amazon ECS Managed Instances.
  scope: AWS Batch on containers.
  link: [on AWS Fargate or Amazon EC2 resources](../facts/ecs.md#ecs-whitepaper-batch-runs-on-fargate-or-ec2)
  link: [Fargate resources, and Amazon ECS Managed Instances](../facts/ecs.md#ecs-whitepaper-batch-runs-on-fargate-or-ec2)
ecs-whitepaper-no-control-plane-ec2-easy-lift
  claim: The Containers on AWS whitepaper says there is no complexity of managing a control plane, add-ons, and nodes with Amazon ECS, and that with the Amazon EC2 launch type Amazon ECS provides an easy lift for applications that run on VMs.
  scope: Amazon ECS.
  link: [no complexity of managing a control plane](../facts/ecs.md#ecs-whitepaper-no-control-plane-ec2-easy-lift)
  link: [an easy lift for your applications](../facts/ecs.md#ecs-whitepaper-no-control-plane-ec2-easy-lift)
eks-access-entries-best-way-kubernetes-api-access
  claim: EKS access entries are the best way to grant users access to the Kubernetes API; an access entry associates a set of Kubernetes permissions with an IAM identity such as an IAM role.
  scope: Amazon EKS access entries.
  link: [the best way to grant users access](../facts/eks.md#eks-access-entries-best-way-kubernetes-api-access)
  link: [Kubernetes permissions with an IAM identity](../facts/eks.md#eks-access-entries-best-way-kubernetes-api-access)
eks-access-entries-per-cluster-limit
  claim: One EKS cluster can have at most 3,000 access entries. The quota is not adjustable.
  scope: per cluster, per Region; maximum; not adjustable.
  link: [3,000 access entries](../facts/eks.md#eks-access-entries-per-cluster-limit)
eks-access-entries-recommended-over-aws-auth
  claim: If an EKS cluster is at or later than the platform version listed in the Prerequisites for its Kubernetes version, AWS recommends creating access entries to give IAM principals access, and recommends migrating any entries you added to the aws-auth ConfigMap to access entries; a cluster whose platform version is earlier than that version must use the aws-auth ConfigMap.
  scope: Amazon EKS cluster authentication; access entries recommended when the cluster platform version is at or later than the version in the Prerequisites; earlier platform versions must use the aws-auth ConfigMap.
  link: [we recommend that you use this option](../facts/eks.md#eks-access-entries-recommended-over-aws-auth)
  link: [Creating access entries](../facts/eks.md#eks-access-entries-recommended-over-aws-auth)
  link: [migrate those entries to access entries](../facts/eks.md#eks-access-entries-recommended-over-aws-auth)
eks-addons-curated-managed-software
  claim: Amazon EKS add-ons provide installation and management of a curated set of add-ons for Amazon EKS clusters, and all Amazon EKS add-ons include the latest security patches and bug fixes and are validated by AWS to work with Amazon EKS.
  scope: Amazon EKS add-ons.
  link: [a curated set of add-ons](../facts/eks.md#eks-addons-curated-managed-software)
eks-anywhere-deployment-options-control-plane-customer-managed
  claim: In the EKS deployment options comparison, for Amazon EKS Anywhere the Kubernetes control plane management is customer-managed.
  scope: Amazon EKS Anywhere.
  link: [Kubernetes control plane management](../facts/eks-anywhere.md#eks-anywhere-deployment-options-control-plane-customer-managed)
  link: [Customer-managed](../facts/eks-anywhere.md#eks-anywhere-deployment-options-control-plane-customer-managed)
eks-anywhere-enterprise-subscriptions-quota
  claim: An account can have 10 EKS Anywhere Enterprise Subscriptions in the current Region by default. The quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [10 EKS Anywhere Enterprise Subscriptions](../facts/eks-anywhere.md#eks-anywhere-enterprise-subscriptions-quota)
eks-anywhere-faq-aws-does-not-manage-clusters-or-capacity
  claim: AWS does not manage Amazon EKS Anywhere clusters or the cluster infrastructure capacity; you are responsible for both.
  scope: Amazon EKS Anywhere.
  link: [customer-managed infrastructure](../facts/eks-anywhere.md#eks-anywhere-faq-aws-does-not-manage-clusters-or-capacity)
eks-anywhere-faq-bottlerocket-default-node-os
  claim: Amazon EKS Anywhere provides Bottlerocket as the default node operating system; you can alternatively use Ubuntu or Red Hat Enterprise Linux.
  scope: Amazon EKS Anywhere nodes; default; not adjustable; Ubuntu and RHEL are alternatives.
  link: [Bottlerocket](../facts/eks-anywhere.md#eks-anywhere-faq-bottlerocket-default-node-os)
eks-anywhere-faq-built-on-cluster-api-infrastructure
  claim: Amazon EKS Anywhere is built on the Kubernetes sub-project Cluster API and supports infrastructure including VMware vSphere, bare metal, Nutanix, Apache CloudStack and AWS Snow.
  scope: Amazon EKS Anywhere.
  link: [VMware vSphere, bare metal, Nutanix](../facts/eks-anywhere.md#eks-anywhere-faq-built-on-cluster-api-infrastructure)
eks-anywhere-faq-cancel-within-7-days
  claim: You can cancel an EKS Anywhere subscription within the first 7 days of purchase by filing an AWS Support ticket, and you are not charged if you cancel within that period.
  scope: Amazon EKS Anywhere Enterprise Subscriptions; maximum; cancel by filing an AWS Support ticket.
  link: [within the first 7 days of purchase](../facts/eks-anywhere.md#eks-anywhere-faq-cancel-within-7-days)
eks-anywhere-faq-connected-or-air-gapped
  claim: Amazon EKS Anywhere can run connected to an AWS Region or disconnected from an AWS Region, including in air-gapped environments.
  scope: Amazon EKS Anywhere.
  link: [including in air-gapped environments](../facts/eks-anywhere.md#eks-anywhere-faq-connected-or-air-gapped)
eks-anywhere-faq-customer-managed-product
  claim: Unlike Amazon EKS, Amazon EKS Anywhere is a customer-managed product, and customers are responsible for cluster lifecycle operations and maintenance of EKS Anywhere clusters.
  scope: Amazon EKS Anywhere.
  link: [customer-managed product](../facts/eks-anywhere.md#eks-anywhere-faq-customer-managed-product)
eks-anywhere-faq-enterprise-subscription-prerequisite
  claim: An AWS Enterprise Support or AWS Enterprise On-Ramp Support Plan is a prerequisite for purchasing Amazon EKS Anywhere Enterprise Subscriptions.
  scope: Amazon EKS Anywhere Enterprise Subscriptions.
  link: [AWS Enterprise On-Ramp Support Plan](../facts/eks-anywhere.md#eks-anywhere-faq-enterprise-subscription-prerequisite)
eks-anywhere-faq-not-supported-on-aws-cloud
  claim: Amazon EKS Anywhere is not supported on the AWS Cloud; for Kubernetes on AWS the FAQ strongly recommends Amazon EKS.
  scope: Amazon EKS Anywhere.
  link: [not supported on AWS Cloud](../facts/eks-anywhere.md#eks-anywhere-faq-not-supported-on-aws-cloud)
eks-anywhere-faq-not-supported-on-outposts
  claim: Amazon EKS Anywhere is not supported on AWS Outposts; for Kubernetes on Outposts the FAQ strongly recommends Amazon EKS on AWS Outposts.
  scope: Amazon EKS Anywhere.
  link: [not supported on AWS Outposts](../facts/eks-anywhere.md#eks-anywhere-faq-not-supported-on-outposts)
eks-anywhere-faq-uses-eks-distro
  claim: Amazon EKS Anywhere uses Amazon EKS Distro, the same Kubernetes distribution that Amazon EKS deploys, so clusters get the same software updates, security patches and version release cycle as EKS in the cloud.
  scope: Amazon EKS Anywhere.
  link: [the same Kubernetes distribution deployed by Amazon EKS](../facts/eks-anywhere.md#eks-anywhere-faq-uses-eks-distro)
eks-anywhere-software-open-source
  claim: Amazon EKS Anywhere is available as open source software that you can run on hardware in your data center or edge environment.
  scope: Amazon EKS Anywhere software.
  link: [available as open source software](../facts/eks-anywhere.md#eks-anywhere-software-open-source)
eks-anywhere-subscription-1-year-or-3-year-term
  claim: When you purchase an EKS Anywhere Enterprise Subscription, you can choose a 1-year term or a 3-year term, and you are billed monthly throughout the term.
  scope: per subscription.
  link: [1-year term or a 3-year term](../facts/eks-anywhere.md#eks-anywhere-subscription-1-year-or-3-year-term)
eks-anywhere-subscription-flat-per-cluster
  claim: The per cluster pricing of an EKS Anywhere Enterprise Subscription is flat and does not change based on cluster size.
  scope: per cluster.
  link: [does not change based on cluster size](../facts/eks-anywhere.md#eks-anywhere-subscription-flat-per-cluster)
eks-anywhere-support-needs-enterprise-subscription
  claim: You can receive support only for Amazon EKS Anywhere clusters that are licensed under an active Amazon EKS Anywhere Enterprise Subscription.
  scope: per cluster.
  link: [an active Amazon EKS Anywhere Enterprise Subscription](../facts/eks-anywhere.md#eks-anywhere-support-needs-enterprise-subscription)
eks-api-endpoint-private-access-options
  claim: You can enable private access to the Kubernetes API server so that all communication between your nodes and the API server stays within your VPC, limit the IP addresses that can reach it from the internet, or completely disable internet access to it.
  scope: Amazon EKS cluster API server endpoint; can be updated at any time.
  link: [stays within your VPC](../facts/eks.md#eks-api-endpoint-private-access-options)
  link: [completely disable internet access to the API server](../facts/eks.md#eks-api-endpoint-private-access-options)
eks-api-endpoint-public-by-default
  claim: By default the API server endpoint of a new Amazon EKS cluster is public to the internet, and access to the API server is secured using a combination of AWS IAM and native Kubernetes role-based access control.
  scope: new Amazon EKS clusters; default; adjustable; private access can be enabled and public access limited or disabled.
  link: [API server endpoint is public to the internet](../facts/eks.md#eks-api-endpoint-public-by-default)
  link: [a combination of AWS Identity and Access Management](../facts/eks.md#eks-api-endpoint-public-by-default)
eks-auto-mode-aws-manages-infrastructure
  claim: EKS Auto Mode extends AWS management of Kubernetes clusters beyond the cluster itself so AWS also sets up and manages the infrastructure for your workloads, including compute autoscaling, pod and service networking, application load balancing, cluster DNS, block storage and GPU support.
  scope: Amazon EKS Auto Mode.
  link: [extends AWS management of Kubernetes clusters](../facts/eks.md#eks-auto-mode-aws-manages-infrastructure)
  link: [compute autoscaling, pod and service networking](../facts/eks.md#eks-auto-mode-aws-manages-infrastructure)
eks-auto-mode-integrates-load-balancing-storage
  claim: EKS Auto Mode integrates with Elastic Load Balancing to automate the provisioning and configuration of load balancers for Kubernetes Services and Ingress resources, and it configures ephemeral storage for you.
  scope: Amazon EKS Auto Mode.
  link: [automating the provisioning and configuration of load balancers](../facts/eks.md#eks-auto-mode-integrates-load-balancing-storage)
  link: [EKS Auto Mode configures ephemeral storage for you](../facts/eks.md#eks-auto-mode-integrates-load-balancing-storage)
eks-auto-mode-karpenter-scaling
  claim: EKS Auto Mode automatically scales cluster compute: if a pod can't fit onto existing nodes it creates a new node, it consolidates workloads and deletes nodes, and it builds upon Karpenter.
  scope: Amazon EKS Auto Mode.
  link: [EKS Auto Mode creates a new one](../facts/eks.md#eks-auto-mode-karpenter-scaling)
  link: [EKS Auto Mode builds upon Karpenter](../facts/eks.md#eks-auto-mode-karpenter-scaling)
eks-auto-mode-node-lifetime-immutable-no-ssh
  claim: EKS Auto Mode nodes have a maximum lifetime of 21 days (which you can reduce), after which they are automatically replaced with new nodes; EKS Auto Mode locks down access to files on the AMI using SELinux enforcing mode and a read-only root file system, and prevents direct access to the nodes by disallowing SSH or SSM access.
  scope: Amazon EKS Auto Mode nodes; maximum; lifetime can be reduced.
  link: [maximum lifetime of 21 days (which you can reduce)](../facts/eks.md#eks-auto-mode-node-lifetime-immutable-no-ssh)
  link: [disallowing SSH or SSM access](../facts/eks.md#eks-auto-mode-node-lifetime-immutable-no-ssh)
eks-auto-mode-node-max-lifetime-21-days
  claim: Nodes launched by EKS Auto Mode have a maximum lifetime of 21 days, which you can reduce. After that they are automatically replaced with new nodes.
  scope: per EKS Auto Mode node; maximum; adjustable.
  link: [21 days](../facts/eks.md#eks-auto-mode-node-max-lifetime-21-days)
eks-case-study-miro-managed-eks-cut-compute-cost
  claim: Miro was managing its own clusters on AWS, and its engineers were spending 60–70 percent of their time on maintenance; Miro also created self-service infrastructure for its developers, decreased time to market, increased scalability, and cut compute costs by 80 percent.
  scope: Miro case study; customer-reported outcome.
  link: [its engineers were spending 60–70 percent of their time on maintenance](../facts/eks.md#eks-case-study-miro-managed-eks-cut-compute-cost)
  link: [cut compute costs by 80 percent](../facts/eks.md#eks-case-study-miro-managed-eks-cut-compute-cost)
eks-certified-kubernetes-conformant
  claim: Amazon EKS is certified Kubernetes-conformant, so you can deploy Kubernetes-compatible applications without refactoring and use Kubernetes community tooling and plugins.
  scope: Amazon EKS.
  link: [certified Kubernetes-conformant](../facts/eks.md#eks-certified-kubernetes-conformant)
  link: [deploy Kubernetes-compatible applications without refactoring](../facts/eks.md#eks-certified-kubernetes-conformant)
eks-change-access-entries-2023-12
  claim: On December 18, 2023 Amazon EKS added access entries as a way to grant IAM roles and users access to a cluster. Before, access was granted by adding entries to the aws-auth ConfigMap.
  scope: document history row.
  link: [December 18, 2023](../facts/eks.md#eks-change-access-entries-2023-12)
  link: [access entries](../facts/eks.md#eks-change-access-entries-2023-12)
eks-change-app-mesh-existing-customers-only-2023-09
  claim: On September 29, 2023 the Amazon EKS documentation stated that the Amazon EKS integrations with AWS App Mesh remain for existing customers of App Mesh only.
  scope: document history row.
  link: [September 29, 2023](../facts/eks.md#eks-change-app-mesh-existing-customers-only-2023-09)
  link: [remain for existing customers of App Mesh only](../facts/eks.md#eks-change-app-mesh-existing-customers-only-2023-09)
eks-change-auto-mode-launch-2024-12
  claim: On December 1, 2024 Amazon EKS added EKS Auto Mode, which fully automates Kubernetes cluster infrastructure management for compute, storage, and networking on AWS.
  scope: document history row.
  link: [December 1, 2024](../facts/eks.md#eks-change-auto-mode-launch-2024-12)
  link: [Amazon EKS Auto Mode](../facts/eks.md#eks-change-auto-mode-launch-2024-12)
eks-change-ca-rotation-2026-08
  claim: On Aug 20, 2026 Amazon EKS announced certificate authority (CA) rotation, which lets customers rotate the CA of their cluster through a managed lifecycle with automated safeguards.
  scope: What's New post.
  link: [Aug 20, 2026](../facts/eks.md#eks-change-ca-rotation-2026-08)
  link: [certificate authority (CA) rotation](../facts/eks.md#eks-change-ca-rotation-2026-08)
eks-change-capabilities-2025-11
  claim: On November 30, 2025 Amazon EKS added EKS Capabilities, which are fully managed cluster capabilities.
  scope: document history row.
  link: [November 30, 2025](../facts/eks.md#eks-change-capabilities-2025-11)
  link: [Amazon EKS Capabilities](../facts/eks.md#eks-change-capabilities-2025-11)
eks-change-envelope-encryption-default-2025-03
  claim: On Mar 5, 2025 Amazon EKS made envelope encryption of all Kubernetes API data the default. Before that, envelope encryption with Kubernetes KMS provider v1 was optional. By default AWS owns the keys used for envelope encryption. Default envelope encryption is enabled automatically for all EKS clusters running Kubernetes version 1.28 or higher.
  scope: What's New post.
  link: [a default configuration for all objects](../facts/eks.md#eks-change-envelope-encryption-default-2025-03)
  link: [AWS owns the keys](../facts/eks.md#eks-change-envelope-encryption-default-2025-03)
  changed: 2025-03-05: was optional envelope encryption with Kubernetes KMS provider v1
eks-change-extended-support-full-release-2024-01
  claim: On January 16, 2024 Amazon EKS made extended support for Kubernetes versions a full release. Extended Kubernetes version support lets you stay at a specific Kubernetes version for longer than 14 months.
  scope: document history row.
  link: [January 16, 2024](../facts/eks.md#eks-change-extended-support-full-release-2024-01)
  link: [Full release: Amazon EKS Extended Support](../facts/eks.md#eks-change-extended-support-full-release-2024-01)
eks-change-extended-support-preview-2023-10
  claim: On October 4, 2023 Amazon EKS released extended support for Kubernetes versions as a preview. Extended Kubernetes version support lets you stay at a specific Kubernetes version for longer than 14 months.
  scope: document history row.
  link: [October 4, 2023](../facts/eks.md#eks-change-extended-support-preview-2023-10)
  link: [Extended Support for Kubernetes versions](../facts/eks.md#eks-change-extended-support-preview-2023-10)
eks-change-hybrid-nodes-launch-2024-12
  claim: On December 1, 2024 Amazon EKS added Amazon EKS Hybrid Nodes, which let you run nodes on-premises that connect to an Amazon EKS cluster.
  scope: document history row.
  link: [December 1, 2024](../facts/eks.md#eks-change-hybrid-nodes-launch-2024-12)
  link: [Amazon EKS Hybrid Nodes](../facts/eks.md#eks-change-hybrid-nodes-launch-2024-12)
eks-change-kubernetes-1-37-2026-10
  claim: On Oct 2, 2026 Amazon EKS added support for Kubernetes version 1.37: you can create new clusters on it and upgrade existing clusters to it.
  scope: What's New post.
  link: [Oct 2, 2026](../facts/eks.md#eks-change-kubernetes-1-37-2026-10)
  link: [version 1.37](../facts/eks.md#eks-change-kubernetes-1-37-2026-10)
eks-change-multiple-oidc-providers-2026-08
  claim: On Aug 24, 2026 Amazon EKS added support for multiple external OIDC identity providers per cluster: you can associate up to 10 OIDC identity providers with a single cluster.
  scope: What's New post.
  link: [up to 10 OIDC identity providers](../facts/eks.md#eks-change-multiple-oidc-providers-2026-08)
  link: [Aug 24, 2026](../facts/eks.md#eks-change-multiple-oidc-providers-2026-08)
eks-change-pod-identities-2023-11
  claim: On November 26, 2023 Amazon EKS added EKS Pod Identities, which associate an IAM role with a Kubernetes service account without extended permissions on the node IAM role.
  scope: document history row.
  link: [November 26, 2023](../facts/eks.md#eks-change-pod-identities-2023-11)
  link: [Amazon EKS Pod Identities](../facts/eks.md#eks-change-pod-identities-2023-11)
eks-change-pod-identity-target-roles-2025-06
  claim: On June 11, 2025 Amazon EKS added target IAM roles to EKS Pod Identities, so a pod can automatically assume a role in another account through role chaining.
  scope: document history row.
  link: [June 11, 2025](../facts/eks.md#eks-change-pod-identity-target-roles-2025-06)
  link: [target IAM roles](../facts/eks.md#eks-change-pod-identity-target-roles-2025-06)
eks-change-provisioned-control-plane-sla-99-99-2026-03
  claim: On Mar 20, 2026 Amazon EKS began to offer a 99.99% SLA for clusters running on Provisioned Control Plane, up from the 99.95% SLA offered on standard control plane.
  scope: What's New post.
  link: [99.99%](../facts/eks.md#eks-change-provisioned-control-plane-sla-99-99-2026-03)
  link: [99.95%](../facts/eks.md#eks-change-provisioned-control-plane-sla-99-99-2026-03)
  changed: 2026-03-20: was 99.95% SLA offered on standard control plane
eks-change-version-rollback-2026-07
  claim: On Jul 1, 2026 Amazon EKS added Kubernetes version rollback, which lets you revert to the previous Kubernetes minor version within 7 days if issues arise after an upgrade.
  scope: What's New post.
  link: [Jul 1, 2026](../facts/eks.md#eks-change-version-rollback-2026-07)
  link: [within 7 days](../facts/eks.md#eks-change-version-rollback-2026-07)
eks-change-warm-pools-managed-node-groups-2026-04
  claim: On April 7, 2026 Amazon EKS managed node groups added support for Amazon EC2 Auto Scaling warm pools.
  scope: document history row.
  link: [April 7, 2026](../facts/eks.md#eks-change-warm-pools-managed-node-groups-2026-04)
  link: [warm pools](../facts/eks.md#eks-change-warm-pools-managed-node-groups-2026-04)
eks-cluster-autoscaler-uses-auto-scaling-groups
  claim: The Kubernetes Cluster Autoscaler automatically adjusts the number of nodes in your cluster when pods fail or are rescheduled onto other nodes, and it uses Auto Scaling groups.
  scope: Kubernetes Cluster Autoscaler on Amazon EKS.
  link: [adjusts the number of nodes in your cluster](../facts/eks.md#eks-cluster-autoscaler-uses-auto-scaling-groups)
  link: [The Cluster Autoscaler uses Auto Scaling groups](../facts/eks.md#eks-cluster-autoscaler-uses-auto-scaling-groups)
eks-cluster-iam-role-required
  claim: An Amazon EKS cluster IAM role is required for each cluster.
  scope: Amazon EKS clusters.
  link: [required for each cluster](../facts/eks.md#eks-cluster-iam-role-required)
  link: [cluster IAM role](../facts/eks.md#eks-cluster-iam-role-required)
eks-clusters-per-region-quota
  claim: An account can have 100 EKS clusters in each supported Region by default. The quota is adjustable through Service Quotas.
  scope: per account, per Region; default; adjustable.
  link: [100 EKS clusters](../facts/eks.md#eks-clusters-per-region-quota)
eks-compute-compare-security-groups-per-pod
  claim: In the EKS compute comparison table you can assign different VPC security groups to individual Pods on managed node groups (Linux nodes only), but not on EKS Auto Mode or Hybrid Nodes.
  scope: Amazon EKS compute options; Linux nodes only.
  link: [different VPC security groups to individual Pods](../facts/eks.md#eks-compute-compare-security-groups-per-pod)
  link: [Linux nodes only](../facts/eks.md#eks-compute-compare-security-groups-per-pod)
eks-compute-compare-ssh-into-node
  claim: In the EKS compute comparison table you can SSH into nodes of managed node groups and hybrid nodes, but not into EKS Auto Mode nodes.
  scope: Amazon EKS compute options.
  link: [Can SSH into node](../facts/eks.md#eks-compute-compare-ssh-into-node)
  link: [No](../facts/eks.md#eks-compute-compare-ssh-into-node)
eks-compute-compare-who-manages-ec2-instances
  claim: In the EKS compute comparison table, managed node groups require you to deploy and manage Amazon EC2 instances, EKS Auto Mode does not, and hybrid nodes are on-premises machines that you manage with your own tooling.
  scope: Amazon EKS compute options; managed node groups versus EKS Auto Mode versus Hybrid Nodes.
  link: [Must deploy and manage Amazon EC2 instances](../facts/eks.md#eks-compute-compare-who-manages-ec2-instances)
  link: [No](../facts/eks.md#eks-compute-compare-who-manages-ec2-instances)
eks-compute-compare-who-patches-node-os
  claim: In the EKS compute comparison table, with managed node groups you must secure, maintain, and patch the operating system of the Amazon EC2 instances, with EKS Auto Mode you do not, and with hybrid nodes you manage the operating system of your own machines.
  scope: Amazon EKS compute options.
  link: [patch the operating system of Amazon EC2 instances](../facts/eks.md#eks-compute-compare-who-patches-node-os)
  link: [No](../facts/eks.md#eks-compute-compare-who-patches-node-os)
eks-compute-compare-windows-containers
  claim: In the EKS compute comparison table, EKS managed node groups can run containers that require Windows, while EKS Auto Mode and Amazon EKS Hybrid Nodes cannot.
  scope: Amazon EKS compute options.
  link: [Can run containers that require Windows](../facts/eks.md#eks-compute-compare-windows-containers)
  link: [Yes](../facts/eks.md#eks-compute-compare-windows-containers)
eks-compute-options-pod-scheduling
  claim: An Amazon EKS cluster can schedule Pods on any combination of EKS Auto Mode managed nodes, self-managed nodes, Amazon EKS managed node groups, AWS Fargate, and Amazon EKS Hybrid Nodes.
  scope: Amazon EKS nodes.
  link: [EKS Auto Mode managed nodes](../facts/eks.md#eks-compute-options-pod-scheduling)
  link: [Amazon EKS managed node groups](../facts/eks.md#eks-compute-options-pod-scheduling)
  link: [AWS Fargate](../facts/eks.md#eks-compute-options-pod-scheduling)
eks-connector-view-only-conformant-clusters
  claim: Amazon EKS Connector registers and connects any conformant Kubernetes cluster to AWS and visualizes it in the Amazon EKS console, but you can view connected clusters and cannot manage them.
  scope: Amazon EKS Connector.
  link: [any conformant Kubernetes cluster](../facts/eks.md#eks-connector-view-only-conformant-clusters)
  link: [you can’t manage them](../facts/eks.md#eks-connector-view-only-conformant-clusters)
eks-control-plane-auto-replace-and-scale
  claim: Amazon EKS automatically scales control plane instances based on load, detects and replaces unhealthy control plane instances, and automatically patches the control plane.
  scope: Amazon EKS control plane.
  link: [detects and replaces unhealthy control plane instances](../facts/eks.md#eks-control-plane-auto-replace-and-scale)
  link: [automatically scales control plane instances based on load](../facts/eks.md#eks-control-plane-auto-replace-and-scale)
eks-control-plane-dedicated-per-cluster
  claim: Amazon EKS ensures every cluster has its own unique Kubernetes control plane, with no overlaps between clusters or AWS accounts.
  scope: Amazon EKS control plane.
  link: [its own unique Kubernetes control plane](../facts/eks.md#eks-control-plane-dedicated-per-cluster)
  link: [no overlaps between clusters or AWS accounts](../facts/eks.md#eks-control-plane-dedicated-per-cluster)
eks-control-plane-security-groups-per-cluster-limit
  claim: One EKS cluster can have at most 4 control plane security groups, which you specify when you create the cluster. The quota is not adjustable.
  scope: per cluster, per Region; maximum; not adjustable.
  link: [4 control plane security groups](../facts/eks.md#eks-control-plane-security-groups-per-cluster-limit)
eks-control-plane-three-azs-api-etcd
  claim: The Amazon EKS control plane consists of at least two API server instances and three etcd instances that run across three Availability Zones within an AWS Region.
  scope: Amazon EKS control plane; minimum; per cluster.
  link: [at least two API server instances](../facts/eks.md#eks-control-plane-three-azs-api-etcd)
  link: [three `etcd` instances](../facts/eks.md#eks-control-plane-three-azs-api-etcd)
  link: [across three Availability Zones within an AWS Region](../facts/eks.md#eks-control-plane-three-azs-api-etcd)
eks-cost-monitoring-split-cost-allocation
  claim: Amazon EKS provides two cost monitoring solutions, and with split cost allocation you see your Kubernetes costs directly alongside your other AWS spend.
  scope: Amazon EKS cost monitoring.
  link: [two cost monitoring solutions](../facts/eks.md#eks-cost-monitoring-split-cost-allocation)
  link: [alongside your other AWS spend](../facts/eks.md#eks-cost-monitoring-split-cost-allocation)
eks-daemonset-runs-on-every-node
  claim: In Kubernetes you can use a DaemonSet to ensure that the selected application runs on every node in your cluster.
  scope: Kubernetes on Amazon EKS.
  link: [runs on every node in your cluster](../facts/eks.md#eks-daemonset-runs-on-every-node)
  link: [DaemonSet](../facts/eks.md#eks-daemonset-runs-on-every-node)
eks-decision-guide-kubernetes-skills-sre-teams
  claim: The AWS container decision guide says the skills of your organization are a major factor: some organizations have the skills and resources to run Kubernetes because they invest in strong SRE teams and find value in skill portability, and these teams handle frequent cluster upgrades.
  scope: Amazon EKS compared with Amazon ECS.
  link: [skills of your organization are a major factor](../facts/eks.md#eks-decision-guide-kubernetes-skills-sre-teams)
  link: [invest in strong SRE teams](../facts/eks.md#eks-decision-guide-kubernetes-skills-sre-teams)
eks-deployment-options-control-plane-location-hybrid-outposts
  claim: In the EKS deployment options comparison, the Kubernetes control plane of Amazon EKS Hybrid Nodes is located in AWS Regions, while the control plane of Amazon EKS on AWS Outposts is located in AWS Regions or on AWS Outposts.
  scope: Amazon EKS hybrid deployment options.
  link: [Kubernetes control plane location](../facts/eks.md#eks-deployment-options-control-plane-location-hybrid-outposts)
  link: [AWS Regions or AWS Outposts](../facts/eks.md#eks-deployment-options-control-plane-location-hybrid-outposts)
eks-deployment-options-data-plane-hybrid-outposts
  claim: In the EKS deployment options comparison, the Kubernetes data plane of Amazon EKS Hybrid Nodes is customer-managed physical or virtual machines, while the data plane of Amazon EKS on AWS Outposts is Amazon EC2 self-managed nodes.
  scope: Amazon EKS hybrid deployment options.
  link: [Customer-managed physical or virtual machines](../facts/eks.md#eks-deployment-options-data-plane-hybrid-outposts)
  link: [Amazon EC2 self-managed nodes](../facts/eks.md#eks-deployment-options-data-plane-hybrid-outposts)
eks-deployment-replicaset-stateless
  claim: For a stateless application such as a web server you can use a Kubernetes Deployment to deploy Pods and ReplicaSets; a ReplicaSet defines how many instances of a Pod you want running concurrently.
  scope: Kubernetes on Amazon EKS; stateless applications.
  link: [use a Deployment to deploy Pods and ReplicaSets](../facts/eks.md#eks-deployment-replicaset-stateless)
  link: [how many instances of a Pod](../facts/eks.md#eks-deployment-replicaset-stateless)
eks-distro-extended-maintenance-up-to-14-months
  claim: EKS Distro offers extended Kubernetes maintenance support for up to 14 months, in accordance with the Amazon EKS Version Lifecycle Policy.
  scope: per Kubernetes version; maximum; not adjustable.
  link: [up to 14 months](../facts/eks-distro.md#eks-distro-extended-maintenance-up-to-14-months)
eks-distro-faq-clusters-on-ec2-on-premises-other-clouds
  claim: You can create Amazon EKS Distro clusters on AWS using Amazon EC2, on premises on your own hardware, and on other clouds using the tooling of your choice.
  scope: Amazon EKS Distro.
  link: [on premises on your own hardware](../facts/eks-distro.md#eks-distro-faq-clusters-on-ec2-on-premises-other-clouds)
eks-distro-faq-does-not-include-iam-authenticator-or-plugins
  claim: Amazon EKS Distro does not include the official Kubernetes network and storage plugins or the AWS IAM authenticator.
  scope: Amazon EKS Distro.
  link: [the official Kubernetes network, storage plugins](../facts/eks-distro.md#eks-distro-faq-does-not-include-iam-authenticator-or-plugins)
eks-distro-faq-not-every-point-release
  claim: Amazon EKS Distro does not provide a build and release for every Kubernetes point release; it only provides builds and dependency updates for versions and point releases that Amazon EKS supports.
  scope: Amazon EKS Distro.
  link: [in alignment with Kubernetes version and point releases](../facts/eks-distro.md#eks-distro-faq-not-every-point-release)
eks-distro-faq-release-channels-github-s3-ecr
  claim: You can access EKS Distro releases as open source on GitHub, or within AWS using Amazon S3 and Amazon ECR as a common source of releases and updates.
  scope: Amazon EKS Distro.
  link: [open source on GitHub](../facts/eks-distro.md#eks-distro-faq-release-channels-github-s3-ecr)
eks-distro-faq-same-kubernetes-as-eks-run-it-yourself
  claim: Amazon EKS Distro is a distribution of the same open-source Kubernetes and dependencies deployed by Amazon EKS, which helps you manually run Kubernetes clusters anywhere.
  scope: Amazon EKS Distro.
  link: [manually run Kubernetes clusters anywhere](../facts/eks-distro.md#eks-distro-faq-same-kubernetes-as-eks-run-it-yourself)
eks-distro-faq-same-versions-as-eks
  claim: Amazon EKS Distro supports the same versions of Kubernetes and point releases as Amazon EKS.
  scope: Amazon EKS Distro.
  link: [same versions of Kubernetes and point releases](../facts/eks-distro.md#eks-distro-faq-same-versions-as-eks)
eks-distro-faq-support-best-effort
  claim: For Amazon EKS Distro, AWS reviews and responds to issues customers submit, but fixes or patches are on a best-effort basis.
  scope: Amazon EKS Distro.
  link: [best effort basis](../facts/eks-distro.md#eks-distro-faq-support-best-effort)
eks-distro-faq-you-set-up-servers-and-networking
  claim: To create an Amazon EKS Distro cluster you set up the servers and networking and install a supported operating system on each server of the cluster.
  scope: Amazon EKS Distro.
  link: [set up the servers, networking](../facts/eks-distro.md#eks-distro-faq-you-set-up-servers-and-networking)
eks-ebs-csi-fargate-limits
  claim: You can run the Amazon EBS CSI controller on Fargate nodes, but the Amazon EBS CSI node DaemonSet can only run on Amazon EC2 instances, and the Amazon EBS CSI driver is not compatible with EKS Hybrid Nodes.
  scope: Amazon EBS CSI driver on Amazon EKS.
  link: [can only run on Amazon EC2 instances](../facts/eks.md#eks-ebs-csi-fargate-limits)
  link: [not compatible with Amazon EKS Hybrid Nodes](../facts/eks.md#eks-ebs-csi-fargate-limits)
eks-efs-csi-shared-file-storage-windows-hybrid
  claim: The Amazon EFS CSI driver lets Kubernetes clusters running on AWS mount Amazon EFS file systems as persistent volumes; it is not compatible with Windows-based container images or with EKS Hybrid Nodes.
  scope: Amazon EFS CSI driver on Amazon EKS.
  link: [mount Amazon EFS file systems as persistent volumes](../facts/eks.md#eks-efs-csi-shared-file-storage-windows-hybrid)
  link: [isn’t compatible with Windows-based container images](../facts/eks.md#eks-efs-csi-shared-file-storage-windows-hybrid)
eks-end-of-standard-support-announced-60-days
  claim: Amazon EKS announces the end of standard support date of a Kubernetes minor version at least 60 days in advance.
  scope: per Kubernetes minor version; minimum; not adjustable.
  link: [at least 60 days in advance](../facts/eks.md#eks-end-of-standard-support-announced-60-days)
eks-extended-support-12-months
  claim: Once an EKS Kubernetes version is past the end of standard support, it enters extended support for the next 12 months. Extended support has an additional cost per cluster hour.
  scope: per Kubernetes minor version; fixed; not adjustable.
  link: [12 months](../facts/eks.md#eks-extended-support-12-months)
eks-extended-support-enabled-by-default
  claim: Extended support is enabled by default for Amazon EKS clusters.
  scope: per cluster; default; adjustable.
  link: [Extended support is enabled by default](../facts/eks.md#eks-extended-support-enabled-by-default)
eks-extended-support-end-auto-upgrade
  claim: If you do not update your cluster before the extended support period ends, the cluster is auto-upgraded to the oldest currently supported extended version.
  scope: per cluster.
  link: [auto-upgraded to the oldest currently supported extended version](../facts/eks.md#eks-extended-support-end-auto-upgrade)
eks-faq-add-ons-manage-operational-software
  claim: EKS add-ons let you enable and manage Kubernetes operational software, which provides capabilities such as observability, scaling, networking, and AWS cloud resource integrations for your EKS clusters.
  scope: Amazon EKS clusters.
  link: [enable and manage Kubernetes operational software](../facts/eks.md#eks-faq-add-ons-manage-operational-software)
eks-faq-add-ons-one-click-install
  claim: Amazon EKS add-ons provide one-click installation and management of Kubernetes operational software.
  scope: Amazon EKS add-ons.
  link: [one-click installation and management](../facts/eks.md#eks-faq-add-ons-one-click-install)
eks-faq-anywhere-clusters-run-entirely-on-your-infrastructure
  claim: With EKS Anywhere you are responsible for managing the Kubernetes clusters, which run entirely on your infrastructure; with Hybrid Nodes the control plane is hosted in the AWS Cloud and only nodes run on your infrastructure.
  scope: Amazon EKS Hybrid Nodes compared with Amazon EKS Anywhere.
  link: [run entirely on your infrastructure](../facts/eks.md#eks-faq-anywhere-clusters-run-entirely-on-your-infrastructure)
eks-faq-anywhere-enterprise-subscription-term
  claim: With EKS Anywhere you can buy Enterprise Subscriptions for a one-year or three-year term, while EKS Hybrid Nodes has no upfront commitments or minimum fees and is billed by the hour.
  scope: Amazon EKS Anywhere Enterprise Subscriptions.
  link: [one-year or three-year term](../facts/eks.md#eks-faq-anywhere-enterprise-subscription-term)
eks-faq-anywhere-for-isolated-or-air-gapped
  claim: For isolated or air-gapped environments, the EKS option is Amazon EKS Anywhere, which is customer-managed, AWS-supported Kubernetes management software on infrastructure you manage.
  scope: Amazon EKS hybrid deployments.
  link: [isolated or air-gapped environments](../facts/eks.md#eks-faq-anywhere-for-isolated-or-air-gapped)
eks-faq-auto-mode-fully-automates-cluster-management
  claim: EKS Auto Mode fully automates Kubernetes cluster management on AWS by provisioning infrastructure, scaling resources, managing core add-ons and optimizing costs.
  scope: Amazon EKS Auto Mode.
  link: [fully automates Kubernetes cluster management](../facts/eks.md#eks-faq-auto-mode-fully-automates-cluster-management)
eks-faq-auto-mode-vs-fargate-conformant-istio
  claim: EKS Auto Mode is fully Kubernetes conformant and supports all upstream Kubernetes primitives and platform tools like Istio, which Fargate is unable to support.
  scope: Amazon EKS Auto Mode compared with EKS on AWS Fargate.
  link: [platform tools like Istio](../facts/eks.md#eks-faq-auto-mode-vs-fargate-conformant-istio)
eks-faq-auto-mode-vs-fargate-gpu-spot-purchase-options
  claim: EKS Auto Mode fully supports all EC2 runtime purchase options, including GPU and Spot instances; these capabilities are not available when using EKS with Fargate.
  scope: Amazon EKS Auto Mode compared with EKS on AWS Fargate.
  link: [including GPU and Spot instances](../facts/eks.md#eks-faq-auto-mode-vs-fargate-gpu-spot-purchase-options)
eks-faq-auto-mode-vs-fargate-recommended
  claim: EKS with Fargate remains an option, but Amazon EKS Auto Mode is the recommended approach moving forward.
  scope: Amazon EKS compute choice.
  link: [Auto Mode is the recommended approach](../facts/eks.md#eks-faq-auto-mode-vs-fargate-recommended)
eks-faq-auto-mode-vs-fargate-same-isolation
  claim: EKS Auto Mode can reach the same isolation model as Fargate by using standard Kubernetes scheduling so that each EC2 instance runs a single application container.
  scope: Amazon EKS Auto Mode; standard Kubernetes scheduling capabilities.
  link: [each EC2 instance runs a single application container](../facts/eks.md#eks-faq-auto-mode-vs-fargate-same-isolation)
eks-faq-capabilities-run-managed-by-aws-not-on-cluster
  claim: Unlike EKS add-ons, which run on your cluster's compute resources and need you to manage compute capacity, EKS Capabilities operate as fully integrated EKS features managed by AWS.
  scope: Amazon EKS Capabilities compared with EKS add-ons.
  link: [fully integrated EKS features managed by AWS](../facts/eks.md#eks-faq-capabilities-run-managed-by-aws-not-on-cluster)
eks-faq-capabilities-three-at-launch
  claim: Amazon EKS currently offers three Capabilities at launch, each serving distinct use cases in the Kubernetes ecosystem.
  scope: Amazon EKS Capabilities; at launch.
  link: [three Capabilities at launch](../facts/eks.md#eks-faq-capabilities-three-at-launch)
eks-faq-connector-no-charge
  claim: There is no charge for clusters you connect to the Amazon EKS console with the Amazon EKS Connector.
  scope: Amazon EKS Connector.
  link: [no charge for clusters you connect](../facts/eks.md#eks-faq-connector-no-charge)
eks-faq-connector-view-only-no-management
  claim: The EKS Connector lets you view connected clusters in the Amazon EKS console but does not enable management or mutating operations on them through the console.
  scope: Amazon EKS Connector.
  link: [does not enable management or mutating operations](../facts/eks.md#eks-faq-connector-view-only-no-management)
eks-faq-control-plane-multi-az-and-self-healing
  claim: Amazon EKS provisions and scales the Kubernetes control plane, including the API servers and backend persistence layer, across multiple Availability Zones, and it automatically detects and replaces unhealthy control plane nodes and patches the control plane.
  scope: Amazon EKS control plane.
  link: [across multiple AWS Availability Zones (AZs)](../facts/eks.md#eks-faq-control-plane-multi-az-and-self-healing)
  link: [automatically detects and replaces unhealthy control plane nodes](../facts/eks.md#eks-faq-control-plane-multi-az-and-self-healing)
eks-faq-dashboard-needs-organizations
  claim: The EKS Dashboard does not work with accounts that are not linked to AWS Organizations; you use the AWS Organizations management account or a member account enrolled as delegated administrator for EKS.
  scope: Amazon EKS Dashboard.
  link: [accounts not linked to AWS Organizations](../facts/eks.md#eks-faq-dashboard-needs-organizations)
eks-faq-extended-support-26-months
  claim: Amazon EKS extended support lets you use a Kubernetes minor version for up to 26 months from the time EKS makes the version generally available.
  scope: per Kubernetes minor version, from general availability in Amazon EKS; maximum; not adjustable; standard support plus extended support.
  link: [up to 26 months](../facts/eks.md#eks-faq-extended-support-26-months)
eks-faq-extended-support-gets-security-patches
  claim: EKS versions in extended support receive ongoing security patches for the Kubernetes control plane managed by Amazon EKS.
  scope: Amazon EKS versions in extended support.
  link: [ongoing security patches for the Kubernetes control plane](../facts/eks.md#eks-faq-extended-support-gets-security-patches)
eks-faq-hybrid-nodes-aws-manages-control-plane
  claim: With EKS Hybrid Nodes, AWS manages the AWS-hosted Kubernetes control plane and you manage the hybrid nodes that run in your on-premises or edge environments.
  scope: Amazon EKS Hybrid Nodes.
  link: [you manage the hybrid nodes](../facts/eks.md#eks-faq-hybrid-nodes-aws-manages-control-plane)
eks-faq-hybrid-nodes-charged-per-vcpu-hour
  claim: With EKS Hybrid Nodes you are charged per hour for the vCPU resources of your hybrid nodes while they are attached to your EKS clusters.
  scope: per hybrid node, while attached to an EKS cluster; nodes attached to an Amazon EKS cluster.
  link: [charged per hour for the vCPU resources](../facts/eks.md#eks-faq-hybrid-nodes-charged-per-vcpu-hour)
eks-faq-hybrid-nodes-feature-of-eks-anywhere-self-managed
  claim: EKS Hybrid Nodes is a feature of Amazon EKS, a managed Kubernetes service, whereas EKS Anywhere is AWS-supported Kubernetes management software that you manage.
  scope: Amazon EKS Hybrid Nodes compared with Amazon EKS Anywhere.
  link: [a feature of Amazon EKS](../facts/eks.md#eks-faq-hybrid-nodes-feature-of-eks-anywhere-self-managed)
eks-faq-hybrid-nodes-gateway-automates-pod-networking
  claim: The EKS Hybrid Nodes gateway automates networking between your EKS cluster VPC and the Kubernetes pods that run on hybrid nodes.
  scope: Amazon EKS Hybrid Nodes gateway.
  link: [automates networking between your EKS cluster VPC](../facts/eks.md#eks-faq-hybrid-nodes-gateway-automates-pod-networking)
eks-faq-hybrid-nodes-own-machines-vs-outposts-ec2
  claim: With EKS Hybrid Nodes the nodes are your own physical or virtual machines, while with EKS on AWS Outposts the nodes are Amazon EC2 instances running on AWS Outposts.
  scope: Amazon EKS Hybrid Nodes compared with Amazon EKS on AWS Outposts.
  link: [your own physical or virtual machines](../facts/eks.md#eks-faq-hybrid-nodes-own-machines-vs-outposts-ec2)
  link: [Amazon EC2 instances running on AWS Outposts](../facts/eks.md#eks-faq-hybrid-nodes-own-machines-vs-outposts-ec2)
eks-faq-hybrid-nodes-vs-anywhere-connected-vs-air-gapped
  claim: EKS Hybrid Nodes fits on-premises environments that can be connected to the cloud, while EKS Anywhere fits isolated or air-gapped on-premises environments.
  scope: Amazon EKS Hybrid Nodes compared with Amazon EKS Anywhere.
  link: [can be connected to the cloud](../facts/eks.md#eks-faq-hybrid-nodes-vs-anywhere-connected-vs-air-gapped)
  link: [isolated or air-gapped on-premises environments](../facts/eks.md#eks-faq-hybrid-nodes-vs-anywhere-connected-vs-air-gapped)
eks-faq-hybrid-three-options
  claim: There are three Amazon EKS options for hybrid deployments: Amazon EKS, Amazon EKS Anywhere and Amazon EKS Connector.
  scope: Amazon EKS hybrid deployments.
  link: [three Amazon EKS options for hybrid deployments](../facts/eks.md#eks-faq-hybrid-three-options)
eks-faq-inplace-managed-cluster-upgrades
  claim: Amazon EKS performs managed, in-place cluster upgrades for both Kubernetes versions and Amazon EKS platform versions.
  scope: Amazon EKS clusters.
  link: [managed, in-place cluster upgrades](../facts/eks.md#eks-faq-inplace-managed-cluster-upgrades)
eks-faq-managed-kubernetes-no-control-plane-to-run
  claim: Amazon EKS is a managed service for running Kubernetes on AWS without installing and operating your own Kubernetes control plane or worker nodes.
  scope: Amazon EKS.
  link: [managed service](../facts/eks.md#eks-faq-managed-kubernetes-no-control-plane-to-run)
eks-faq-manual-version-control-test-before-production
  claim: Manual control over Kubernetes cluster versioning lets you test applications against new Kubernetes versions before you upgrade production clusters.
  scope: Amazon EKS cluster versions.
  link: [test applications against new versions of Kubernetes](../facts/eks.md#eks-faq-manual-version-control-test-before-production)
eks-faq-migrate-standard-kubernetes-without-code-changes
  claim: You can migrate any standard Kubernetes application to Amazon EKS without any code modifications.
  scope: standard Kubernetes applications moving to Amazon EKS.
  link: [without any code modifications](../facts/eks.md#eks-faq-migrate-standard-kubernetes-without-code-changes)
eks-faq-outposts-local-clusters
  claim: You can deploy the entire Kubernetes cluster on AWS Outposts with Amazon EKS local clusters on AWS Outposts.
  scope: Amazon EKS on AWS Outposts.
  link: [Amazon EKS local clusters on AWS Outposts](../facts/eks.md#eks-faq-outposts-local-clusters)
eks-faq-outposts-managed-vs-hybrid-nodes-managed
  claim: AWS Outposts is AWS-managed infrastructure that runs in your facilities, whereas Amazon EKS Hybrid Nodes runs on bare metal or virtualized infrastructure that you manage in your facilities.
  scope: Amazon EKS on-premises options.
  link: [AWS-managed infrastructure that runs in your facilities](../facts/eks.md#eks-faq-outposts-managed-vs-hybrid-nodes-managed)
  link: [infrastructure that you manage in your facilities](../facts/eks.md#eks-faq-outposts-managed-vs-hybrid-nodes-managed)
eks-faq-outposts-nodes-on-42u-racks
  claim: Amazon EKS with nodes on AWS Outposts is supported on the 42U Outpost racks.
  scope: Amazon EKS on AWS Outposts, nodes on Outposts.
  link: [42U Outpost racks](../facts/eks.md#eks-faq-outposts-nodes-on-42u-racks)
eks-faq-outposts-pay-cluster-and-outposts-capacity
  claim: With EKS on AWS Outposts you pay for the EKS cluster and the Outposts capacity, and with EKS Hybrid Nodes you pay for the EKS cluster and node usage.
  scope: Amazon EKS on AWS Outposts compared with EKS Hybrid Nodes.
  link: [pay for the Amazon EKS cluster](../facts/eks.md#eks-faq-outposts-pay-cluster-and-outposts-capacity)
eks-faq-platform-version-defined
  claim: An EKS platform version represents the capabilities of the cluster control plane, such as which Kubernetes API server flags are enabled, and the current Kubernetes patch version.
  scope: Amazon EKS clusters.
  link: [represent the capabilities of the cluster control plane](../facts/eks.md#eks-faq-platform-version-defined)
eks-faq-provisioned-control-plane-select-capacity
  claim: EKS Provisioned Control Plane lets you select your cluster's control plane capacity for predictable, high performance for the most demanding workloads.
  scope: Amazon EKS Provisioned Control Plane.
  link: [select your cluster's control plane capacity](../facts/eks.md#eks-faq-provisioned-control-plane-select-capacity)
eks-faq-rollback-auto-mode-timeout
  claim: For EKS Auto Mode clusters, EKS fully manages the rollback of worker nodes, and the node rollback has a configurable timeout (default 12 hours, maximum 7 days), after which nodes converge back to the current version.
  scope: Amazon EKS Auto Mode node rollback; default; adjustable; configurable timeout; maximum 7 days.
  link: [default 12 hours](../facts/eks.md#eks-faq-rollback-auto-mode-timeout)
  link: [maximum 7 days](../facts/eks.md#eks-faq-rollback-auto-mode-timeout)
eks-faq-rollback-not-supported-for-fargate-nodes
  claim: Version rollback is not supported for Fargate worker nodes on Amazon EKS; delete the Fargate pods that run the same version as the control plane before rolling back.
  scope: Amazon EKS version rollback, Fargate worker nodes.
  link: [not supported for Fargate worker nodes](../facts/eks.md#eks-faq-rollback-not-supported-for-fargate-nodes)
eks-faq-rollback-window-7-days
  claim: After an EKS version upgrade completes, you have 7 days to roll it back; after more than 7 days rollback is no longer possible.
  scope: per EKS cluster version upgrade, from the time the upgrade completes; maximum; not adjustable; version rollback feature.
  link: [7 days](../facts/eks.md#eks-faq-rollback-window-7-days)
eks-faq-runs-open-source-kubernetes-compatible
  claim: Amazon EKS runs open-source Kubernetes, so existing Kubernetes plug-ins and tooling work, and applications on EKS are fully compatible with applications on any standard Kubernetes environment.
  scope: Amazon EKS.
  link: [any standard Kubernetes environment](../facts/eks.md#eks-faq-runs-open-source-kubernetes-compatible)
eks-faq-supported-operating-systems
  claim: Amazon EKS supports Kubernetes-compatible Linux x86, ARM and Windows Server operating system distributions.
  scope: Amazon EKS worker nodes.
  link: [Linux x86, ARM, and Windows Server](../facts/eks.md#eks-faq-supported-operating-systems)
eks-faq-update-managed-nodes-single-command
  claim: You can update EKS managed nodes to the latest EKS-optimized AMI with a single command in the EKS console, API or CLI.
  scope: Amazon EKS managed nodes.
  link: [with a single command](../facts/eks.md#eks-faq-update-managed-nodes-single-command)
eks-faq-works-with-fargate
  claim: You can run Kubernetes applications as serverless containers using AWS Fargate and Amazon EKS.
  scope: Amazon EKS.
  link: [serverless containers using AWS Fargate](../facts/eks.md#eks-faq-works-with-fargate)
eks-fargate-efs-static-provisioning-only
  claim: A Pod running on Fargate in EKS automatically mounts an Amazon EFS file system without manual driver installation, but you can't use dynamic persistent volume provisioning with Fargate nodes, only static provisioning.
  scope: Amazon EKS on AWS Fargate.
  link: [automatically mounts an Amazon EFS file system](../facts/eks.md#eks-fargate-efs-static-provisioning-only)
  link: [but you can use static provisioning](../facts/eks.md#eks-fargate-efs-static-provisioning-only)
eks-fargate-imds-unavailable-use-irsa
  claim: The Amazon EC2 instance metadata service (IMDS) isn't available to Pods deployed to Fargate nodes; Pods that need IAM credentials get them through IAM roles for service accounts.
  scope: Amazon EKS on AWS Fargate.
  link: [instance metadata service (IMDS) isn’t available](../facts/eks.md#eks-fargate-imds-unavailable-use-irsa)
  link: [IAM roles for service accounts](../facts/eks.md#eks-fargate-imds-unavailable-use-irsa)
eks-fargate-load-balancer-ip-targets-only
  claim: Network Load Balancers and Application Load Balancers can be used with Fargate in EKS with IP targets only.
  scope: Amazon EKS on AWS Fargate.
  link: [with IP targets only](../facts/eks.md#eks-fargate-load-balancer-ip-targets-only)
  link: [Network Load Balancers and Application Load Balancers (ALBs)](../facts/eks.md#eks-fargate-load-balancer-ip-targets-only)
eks-fargate-no-daemonsets
  claim: Daemonsets aren't supported on Fargate in EKS; if your application requires a daemon, reconfigure it to run as a sidecar container in your Pods.
  scope: Amazon EKS on AWS Fargate.
  link: [Daemonsets aren’t supported on Fargate](../facts/eks.md#eks-fargate-no-daemonsets)
  link: [run as a sidecar container](../facts/eks.md#eks-fargate-no-daemonsets)
eks-fargate-no-ebs-volumes
  claim: You can't mount Amazon EBS volumes to Fargate Pods in EKS.
  scope: Amazon EKS on AWS Fargate.
  link: [can’t mount Amazon EBS volumes to Fargate Pods](../facts/eks.md#eks-fargate-no-ebs-volumes)
  link: [Amazon EBS volumes](../facts/eks.md#eks-fargate-no-ebs-volumes)
eks-fargate-no-gpu
  claim: GPUs aren't currently available on Fargate in EKS.
  scope: Amazon EKS on AWS Fargate; at the time of the snapshot.
  link: [GPUs aren’t currently available on Fargate](../facts/eks.md#eks-fargate-no-gpu)
  link: [GPUs](../facts/eks.md#eks-fargate-no-gpu)
eks-fargate-no-hostport-hostnetwork
  claim: Pods running on Fargate in EKS can't specify HostPort or HostNetwork in the Pod manifest.
  scope: Amazon EKS on AWS Fargate.
  link: [`HostPort` or `HostNetwork` in the Pod manifest](../facts/eks.md#eks-fargate-no-hostport-hostnetwork)
  link: [Pods running on Fargate](../facts/eks.md#eks-fargate-no-hostport-hostnetwork)
eks-fargate-no-privileged-containers
  claim: Privileged containers aren't supported on Fargate in EKS.
  scope: Amazon EKS on AWS Fargate.
  link: [Privileged containers aren’t supported on Fargate](../facts/eks.md#eks-fargate-no-privileged-containers)
  link: [privileged containers](../facts/eks.md#eks-fargate-no-privileged-containers)
eks-fargate-no-spot
  claim: Amazon EKS doesn't support Fargate Spot.
  scope: Amazon EKS on AWS Fargate.
  link: [Amazon EKS doesn’t support Fargate Spot](../facts/eks.md#eks-fargate-no-spot)
  link: [Fargate Spot](../facts/eks.md#eks-fargate-no-spot)
eks-fargate-not-on-outposts-wavelength-local-zones
  claim: You can't deploy Fargate Pods to AWS Outposts, AWS Wavelength, or AWS Local Zones in EKS.
  scope: Amazon EKS on AWS Fargate.
  link: [can’t deploy Fargate Pods to AWS Outposts](../facts/eks.md#eks-fargate-not-on-outposts-wavelength-local-zones)
  link: [AWS Local Zones](../facts/eks.md#eks-fargate-not-on-outposts-wavelength-local-zones)
eks-fargate-pod-execution-role-required
  claim: The Amazon EKS Pod execution role is required to run Pods on AWS Fargate infrastructure: the components running on the Fargate infrastructure must make calls to AWS APIs on your behalf, for actions such as pulling container images from Amazon ECR or routing logs to other AWS services, and the role provides the IAM permissions to do this; you must specify a Pod execution role when you create a Fargate profile.
  scope: Amazon EKS on AWS Fargate.
  link: [required to run Pods on AWS Fargate infrastructure](../facts/eks.md#eks-fargate-pod-execution-role-required)
  link: [pull container images from Amazon ECR](../facts/eks.md#eks-fargate-pod-execution-role-required)
eks-fargate-pod-own-compute-boundary
  claim: Each Pod that runs on Fargate in EKS has its own compute boundary and does not share the underlying kernel, CPU resources, memory resources, or elastic network interface with another Pod; EKS Fargate runs only one Pod per node.
  scope: Amazon EKS on AWS Fargate.
  link: [has its own compute boundary](../facts/eks.md#eks-fargate-pod-own-compute-boundary)
  link: [runs only one Pod per node](../facts/eks.md#eks-fargate-pod-own-compute-boundary)
eks-fargate-pods-not-matching-profile-pending
  claim: Pods must match a Fargate profile at the time they are scheduled to run on Fargate; Pods that do not match a Fargate profile might be stuck as Pending.
  scope: Amazon EKS on AWS Fargate.
  link: [must match a Fargate profile](../facts/eks.md#eks-fargate-pods-not-matching-profile-pending)
  link: [might be stuck as `Pending`](../facts/eks.md#eks-fargate-pods-not-matching-profile-pending)
eks-fargate-private-subnets-only
  claim: Pods that run on Fargate in EKS are only supported on private subnets, with NAT gateway access to AWS services but no direct route to an Internet Gateway, so the cluster's VPC must have private subnets available.
  scope: Amazon EKS on AWS Fargate.
  link: [only supported on private subnets](../facts/eks.md#eks-fargate-private-subnets-only)
  link: [not a direct route to an Internet Gateway](../facts/eks.md#eks-fargate-private-subnets-only)
eks-fargate-profile-immutable
  claim: Fargate profiles can't be changed, but you can create a new updated profile to replace an existing profile and then delete the original.
  scope: Amazon EKS Fargate profiles.
  link: [Fargate profiles can’t be changed](../facts/eks.md#eks-fargate-profile-immutable)
  link: [create a new updated profile](../facts/eks.md#eks-fargate-profile-immutable)
eks-fargate-profile-selects-pods
  claim: Before you schedule Pods on Fargate in an EKS cluster, you must define at least one Fargate profile that specifies which Pods use Fargate when launched; Pods are matched using a namespace and the labels specified in the selector, and Pods that match a selector are scheduled on Fargate.
  scope: Amazon EKS on AWS Fargate.
  link: [you must define at least one Fargate profile](../facts/eks.md#eks-fargate-profile-selects-pods)
  link: [matched using a namespace and the labels](../facts/eks.md#eks-fargate-profile-selects-pods)
eks-fargate-profiles-per-cluster-quota
  claim: One EKS cluster can have 10 Fargate profiles by default. The quota is adjustable.
  scope: per cluster, per Region; default; adjustable.
  link: [10 Fargate profiles](../facts/eks.md#eks-fargate-profiles-per-cluster-quota)
eks-fully-managed-kubernetes-service
  claim: Amazon EKS provides a fully managed Kubernetes service that eliminates the complexity of operating Kubernetes clusters.
  scope: Amazon EKS.
  link: [fully managed Kubernetes service](../facts/eks.md#eks-fully-managed-kubernetes-service)
  link: [eliminates the complexity of operating Kubernetes clusters](../facts/eks.md#eks-fully-managed-kubernetes-service)
eks-hpa-scales-pod-count-on-cpu
  claim: The Kubernetes Horizontal Pod Autoscaler automatically scales the number of Pods in a deployment, replication controller, or replica set based on that resource's CPU utilization, and it needs a metrics source such as the Kubernetes Metrics Server installed on the cluster.
  scope: Kubernetes Horizontal Pod Autoscaler on Amazon EKS.
  link: [automatically scales the number of Pods](../facts/eks.md#eks-hpa-scales-pod-count-on-cpu)
  link: [requires that a metrics source](../facts/eks.md#eks-hpa-scales-pod-count-on-cpu)
eks-hybrid-nodes-need-reliable-connection
  claim: EKS Hybrid Nodes must have a reliable connection between your on-premises environment and AWS and are not a fit for disconnected, disrupted, intermittent or limited (DDIL) environments; if you are running in a DDIL environment, AWS suggests that you consider Amazon EKS Anywhere.
  scope: Amazon EKS Hybrid Nodes.
  link: [must have a reliable connection](../facts/eks.md#eks-hybrid-nodes-need-reliable-connection)
  link: [intermittent or limited (DDIL) environments](../facts/eks.md#eks-hybrid-nodes-need-reliable-connection)
eks-hybrid-nodes-network-connectivity-options
  claim: EKS Hybrid Nodes networking is flexible to your preferred method of connecting your on-premises networks to a VPC in AWS; documented options include AWS Site-to-Site VPN, AWS Direct Connect, or your own VPN solution.
  scope: Amazon EKS Hybrid Nodes.
  link: [AWS Site-to-Site VPN, AWS Direct Connect](../facts/eks.md#eks-hybrid-nodes-network-connectivity-options)
eks-hybrid-nodes-not-on-cloud-infrastructure
  claim: Running EKS Hybrid Nodes on cloud infrastructure, including AWS Regions, AWS Local Zones, AWS Outposts, or in other clouds, is not supported.
  scope: Amazon EKS Hybrid Nodes.
  link: [in other clouds, is not supported](../facts/eks.md#eks-hybrid-nodes-not-on-cloud-infrastructure)
  link: [Running EKS Hybrid Nodes on cloud infrastructure](../facts/eks.md#eks-hybrid-nodes-not-on-cloud-infrastructure)
eks-hybrid-nodes-on-premises-control-plane-aws
  claim: With Amazon EKS Hybrid Nodes you use your on-premises and edge infrastructure as nodes in Amazon EKS clusters; AWS manages the AWS-hosted Kubernetes control plane and you manage the hybrid nodes that run in your on-premises or edge environments.
  scope: Amazon EKS Hybrid Nodes.
  link: [on-premises and edge infrastructure as nodes](../facts/eks.md#eks-hybrid-nodes-on-premises-control-plane-aws)
  link: [AWS manages the AWS-hosted Kubernetes control plane](../facts/eks.md#eks-hybrid-nodes-on-premises-control-plane-aws)
eks-hybrid-nodes-pricing-vcpu-hour
  claim: For Amazon EKS Hybrid Nodes there are no upfront commitments or minimum fees, and you are charged per hour for the vCPU resources of your hybrid nodes when they are attached to your Amazon EKS clusters.
  scope: Amazon EKS Hybrid Nodes; while nodes are attached to the cluster.
  link: [charged per hour for the vCPU resources](../facts/eks.md#eks-hybrid-nodes-pricing-vcpu-hour)
  link: [no upfront commitments or minimum fees](../facts/eks.md#eks-hybrid-nodes-pricing-vcpu-hour)
eks-irsa-role-to-service-account
  claim: IAM roles for service accounts (IRSA) manage credentials for your applications by associating an IAM role with a Kubernetes service account and configuring your Pods to use that service account instead of the Amazon EC2 instance's role.
  scope: Amazon EKS IRSA.
  link: [IAM roles for service accounts (IRSA)](../facts/eks.md#eks-irsa-role-to-service-account)
  link: [an IAM role with a Kubernetes service account](../facts/eks.md#eks-irsa-role-to-service-account)
eks-karpenter-customer-managed-no-sla
  claim: Karpenter is open-source software that AWS customers are responsible for installing, configuring and managing in their Kubernetes clusters, and there is no AWS Service Level Agreement (SLA) for Karpenter.
  scope: Karpenter on Amazon EKS.
  link: [customers are responsible for installing, configuring, and managing](../facts/eks.md#eks-karpenter-customer-managed-no-sla)
  link: [no AWS Service Level Agreement (SLA) for Karpenter](../facts/eks.md#eks-karpenter-customer-managed-no-sla)
eks-karpenter-right-sized-compute
  claim: Karpenter is a flexible, high-performance Kubernetes cluster autoscaler that launches right-sized compute resources, such as Amazon EC2 instances, in response to changing application load in under a minute.
  scope: Karpenter on Amazon EKS.
  link: [flexible, high-performance Kubernetes cluster autoscaler](../facts/eks.md#eks-karpenter-right-sized-compute)
  link: [launches right-sized compute resources](../facts/eks.md#eks-karpenter-right-sized-compute)
eks-kubectl-talks-to-control-plane
  claim: Kubernetes administrators do many tasks with tools such as kubectl, which makes requests for services directly to the cluster's control plane.
  scope: Kubernetes on Amazon EKS.
  link: [Kubernetes tools such as `kubectl`](../facts/eks.md#eks-kubectl-talks-to-control-plane)
  link: [directly to the cluster’s control plane](../facts/eks.md#eks-kubectl-talks-to-control-plane)
eks-kubernetes-node-machine-runs-containers
  claim: A Kubernetes node is a machine that runs containerized applications.
  scope: Kubernetes on Amazon EKS.
  link: [a machine that runs containerized applications](../facts/eks.md#eks-kubernetes-node-machine-runs-containers)
eks-label-pairs-per-fargate-selector-quota
  claim: One EKS Fargate profile selector can have 5 label pairs by default. The quota is adjustable.
  scope: per Fargate profile selector, per Region; default; adjustable.
  link: [5 label pairs](../facts/eks.md#eks-label-pairs-per-fargate-selector-quota)
eks-load-balancer-controller-creates-alb-for-ingress-nlb-for-service
  claim: The AWS Load Balancer Controller creates an AWS Application Load Balancer (ALB) when you create a Kubernetes Ingress and an AWS Network Load Balancer (NLB) when you create a Kubernetes service of type LoadBalancer.
  scope: AWS Load Balancer Controller on Amazon EKS.
  link: [AWS Application Load Balancer (ALB)](../facts/eks.md#eks-load-balancer-controller-creates-alb-for-ingress-nlb-for-service)
  link: [AWS Network Load Balancer (NLB)](../facts/eks.md#eks-load-balancer-controller-creates-alb-for-ingress-nlb-for-service)
eks-managed-control-plane-across-azs
  claim: With Amazon EKS, AWS makes sure the cluster is available and scalable because it manages the control plane for you and makes it available across AWS Availability Zones.
  scope: Amazon EKS control plane.
  link: [it manages the control plane for you](../facts/eks.md#eks-managed-control-plane-across-azs)
  link: [makes it available across AWS Availability Zones](../facts/eks.md#eks-managed-control-plane-across-azs)
eks-managed-node-group-ami-shared-responsibility
  claim: When managed nodes run an Amazon EKS optimized AMI, Amazon EKS builds patched versions of the AMI, but you are responsible for deploying the patched AMI versions to your managed node groups; with a custom AMI you build and deploy the patched AMI yourself.
  scope: Amazon EKS managed node groups; Amazon EKS optimized AMI versus custom AMI.
  link: [building patched versions of the AMI](../facts/eks.md#eks-managed-node-group-ami-shared-responsibility)
  link: [you’re responsible for deploying these patched AMI versions](../facts/eks.md#eks-managed-node-group-ami-shared-responsibility)
eks-managed-node-group-asg-in-your-account
  claim: Every managed node is provisioned as part of an Amazon EC2 Auto Scaling group that Amazon EKS manages for you, all resources run within your AWS account, and each node group runs across multiple Availability Zones that you define.
  scope: Amazon EKS managed node groups.
  link: [an Amazon EC2 Auto Scaling group](../facts/eks.md#eks-managed-node-group-asg-in-your-account)
  link: [runs within your AWS account](../facts/eks.md#eks-managed-node-group-asg-in-your-account)
eks-managed-node-group-automates-ec2-lifecycle
  claim: Amazon EKS managed node groups automate the provisioning and lifecycle management of nodes (Amazon EC2 instances), and node updates and terminations automatically drain nodes to keep applications available.
  scope: Amazon EKS managed node groups.
  link: [automate the provisioning and lifecycle management of nodes](../facts/eks.md#eks-managed-node-group-automates-ec2-lifecycle)
  link: [Node updates and terminations automatically drain nodes](../facts/eks.md#eks-managed-node-group-automates-ec2-lifecycle)
eks-managed-node-group-default-on-demand
  claim: If you do not specify a capacity type, an EKS managed node group is provisioned with On-Demand Instances.
  scope: Amazon EKS managed node groups; default; adjustable; no capacity type specified.
  link: [provisioned with On-Demand Instances](../facts/eks.md#eks-managed-node-group-default-on-demand)
  link: [if you don’t specify a **Capacity Type**](../facts/eks.md#eks-managed-node-group-default-on-demand)
eks-managed-node-group-no-extra-charge
  claim: There are no additional costs to use Amazon EKS managed node groups; you only pay for the AWS resources you provision, such as Amazon EC2 instances, Amazon EBS volumes, Amazon EKS cluster hours, and any other AWS infrastructure.
  scope: Amazon EKS managed node groups.
  link: [There are no additional costs](../facts/eks.md#eks-managed-node-group-no-extra-charge)
  link: [pay for the AWS resources you provision](../facts/eks.md#eks-managed-node-group-no-extra-charge)
eks-managed-node-group-no-outposts-wavelength
  claim: Managed node groups can't be deployed on AWS Outposts or in AWS Wavelength, but they can be created on AWS Local Zones.
  scope: Amazon EKS managed node groups.
  link: [can’t be deployed on AWS Outposts](../facts/eks.md#eks-managed-node-group-no-outposts-wavelength)
  link: [can be created on AWS Local Zones](../facts/eks.md#eks-managed-node-group-no-outposts-wavelength)
eks-managed-node-group-on-demand-or-spot
  claim: When creating a managed node group you can choose either the On-Demand or Spot capacity type, and a managed node group contains only On-Demand or only Spot Instances.
  scope: Amazon EKS managed node groups.
  link: [choose either the On-Demand or Spot capacity type](../facts/eks.md#eks-managed-node-group-on-demand-or-spot)
  link: [only On-Demand or only Amazon EC2 Spot Instances](../facts/eks.md#eks-managed-node-group-on-demand-or-spot)
eks-managed-node-group-private-subnet-reach-ecr
  claim: When deploying a managed node group in private subnets, you must ensure that it can access Amazon ECR for pulling container images, by connecting a NAT gateway to the route table of the subnet or by adding AWS PrivateLink VPC endpoints.
  scope: Amazon EKS managed node groups in private subnets.
  link: [access Amazon ECR for pulling container images](../facts/eks.md#eks-managed-node-group-private-subnet-reach-ecr)
  link: [connecting a NAT gateway to the route table](../facts/eks.md#eks-managed-node-group-private-subnet-reach-ecr)
eks-managed-node-groups-per-cluster-quota
  claim: One EKS cluster can have 30 managed node groups by default. The quota is adjustable.
  scope: per cluster, per Region; default; adjustable.
  link: [30 managed node groups](../facts/eks.md#eks-managed-node-groups-per-cluster-quota)
eks-metrics-server-not-default-not-for-monitoring
  claim: The Kubernetes Metrics Server aggregates resource usage data in your cluster and is not deployed by default in Amazon EKS clusters; its metrics are for point-in-time analysis, are not an accurate source for historical analysis, and cannot be used as a monitoring solution.
  scope: Kubernetes Metrics Server on Amazon EKS; default.
  link: [isn’t deployed by default in Amazon EKS clusters](../facts/eks.md#eks-metrics-server-not-default-not-for-monitoring)
  link: [can’t be used as a monitoring solution](../facts/eks.md#eks-metrics-server-not-default-not-for-monitoring)
eks-namespace-groups-pods-of-an-application
  claim: Running all the Pods for a particular application in the same Kubernetes Namespace is a common way to secure and manage those Pods together.
  scope: Kubernetes on Amazon EKS.
  link: [secure and manage those Pods together](../facts/eks.md#eks-namespace-groups-pods-of-an-application)
  link: [all the Pods for a particular application](../facts/eks.md#eks-namespace-groups-pods-of-an-application)
eks-node-iam-role-required-before-launch
  claim: The Amazon EKS node kubelet daemon calls AWS APIs on your behalf and nodes receive the permissions through an IAM instance profile; before you launch nodes and register them into a cluster you must create an IAM role for those nodes, and this applies to both managed node groups and self-managed nodes.
  scope: Amazon EKS managed node groups and self-managed nodes; before nodes are launched and registered into a cluster.
  link: [through an IAM instance profile](../facts/eks.md#eks-node-iam-role-required-before-launch)
  link: [create an IAM role for those nodes](../facts/eks.md#eks-node-iam-role-required-before-launch)
eks-nodes-per-managed-node-group-quota
  claim: One EKS managed node group can have 450 nodes by default. The quota is adjustable.
  scope: per managed node group, per Region; default; adjustable.
  link: [450 nodes](../facts/eks.md#eks-nodes-per-managed-node-group-quota)
eks-nodes-same-vpc-as-cluster-subnets
  claim: Excluding hybrid nodes, EKS nodes must be in the same VPC as the subnets you selected when you created the cluster, but they do not have to be in the same subnets.
  scope: Amazon EKS nodes; except hybrid nodes.
  link: [must be in the same VPC](../facts/eks.md#eks-nodes-same-vpc-as-cluster-subnets)
  link: [don’t have to be in the same subnets](../facts/eks.md#eks-nodes-same-vpc-as-cluster-subnets)
eks-outposts-extended-cluster-needs-reliable-network
  claim: With extended clusters you conserve capacity on your Outpost because the Kubernetes control plane runs in the parent AWS Region, which suits reliable network connectivity from the Outpost to the Region.
  scope: Amazon EKS extended clusters on AWS Outposts.
  link: [conserve capacity on your Outpost](../facts/eks.md#eks-outposts-extended-cluster-needs-reliable-network)
  link: [reliable network connectivity from your Outpost](../facts/eks.md#eks-outposts-extended-cluster-needs-reliable-network)
eks-outposts-extended-vs-local-clusters
  claim: You can deploy Amazon EKS on AWS Outposts as extended clusters, which run the Kubernetes control plane in an AWS Region and nodes on your Outpost, or as local clusters, which run the Kubernetes control plane and nodes on your Outpost; for both deployment options, the Kubernetes control plane is fully managed by AWS.
  scope: Amazon EKS on AWS Outposts.
  link: [an AWS Region and nodes on your Outpost](../facts/eks.md#eks-outposts-extended-vs-local-clusters)
  link: [control plane and nodes on your Outpost](../facts/eks.md#eks-outposts-extended-vs-local-clusters)
eks-outposts-local-cluster-survives-disconnect
  claim: With EKS local clusters on Outposts the entire cluster runs locally, so applications remain available and you can perform cluster operations during network disconnects to the cloud; choose local clusters if you require continued Kubernetes operations through network disconnects or if data residency mandates require it.
  scope: Amazon EKS local clusters on AWS Outposts.
  link: [applications remain available](../facts/eks.md#eks-outposts-local-cluster-survives-disconnect)
  link: [continued Kubernetes operations through network disconnects](../facts/eks.md#eks-outposts-local-cluster-survives-disconnect)
eks-pod-identity-credential-isolation-imds
  claim: With EKS Pod Identity you can scope IAM permissions to a service account so only Pods that use that service account have access to them; this also eliminates the need for third-party solutions such as kiam or kube2iam.
  scope: EKS Pod Identity.
  link: [scope IAM permissions to a service account](../facts/eks.md#eks-pod-identity-credential-isolation-imds)
  link: [only Pods that use that service account](../facts/eks.md#eks-pod-identity-credential-isolation-imds)
eks-pod-identity-recommended-over-irsa
  claim: AWS recommends using EKS Pod Identities to grant access to AWS resources to your pods whenever possible; both EKS Pod Identity and IRSA grant IAM permissions to applications on Kubernetes clusters, but they differ in how you configure them, the limits supported and the features enabled.
  scope: Amazon EKS pod permissions; whenever possible.
  link: [recommends using EKS Pod Identities](../facts/eks.md#eks-pod-identity-recommended-over-irsa)
  link: [fundamentally different in how you configure them](../facts/eks.md#eks-pod-identity-recommended-over-irsa)
eks-pod-identity-role-to-service-account
  claim: EKS Pod Identity manages credentials for your applications similar to the way Amazon EC2 instance profiles provide credentials to EC2 instances: you associate an IAM role with a Kubernetes service account and configure your Pods to use the service account instead of distributing AWS credentials or using the EC2 instance's role.
  scope: EKS Pod Identity.
  link: [an IAM role with a Kubernetes service account](../facts/eks.md#eks-pod-identity-role-to-service-account)
  link: [the way that Amazon EC2 instance profiles](../facts/eks.md#eks-pod-identity-role-to-service-account)
eks-pod-smallest-deployable-unit
  claim: In Kubernetes the Pod is the smallest deployable unit and typically holds a single container, although tightly coupled containers can be in one Pod; the containers of a Pod share a single IP address and can talk to each other as if on localhost.
  scope: Kubernetes on Amazon EKS.
  link: [the smallest deployable unit](../facts/eks.md#eks-pod-smallest-deployable-unit)
  link: [share a single IP address](../facts/eks.md#eks-pod-smallest-deployable-unit)
eks-pricing-auto-mode-per-instance-duration-and-type
  claim: You pay for EKS Auto Mode based on the duration and type of the Amazon EC2 instances that EKS Auto Mode launches and manages. The EKS Auto Mode price is in addition to the Amazon EC2 instance price.
  scope: per instance.
  link: [duration and type of Amazon EC2 instances](../facts/eks.md#eks-pricing-auto-mode-per-instance-duration-and-type)
eks-pricing-auto-mode-per-second-one-minute
  claim: Like EC2 instance charges, EKS Auto Mode charges are billed per second, with a one-minute minimum.
  scope: per instance; minimum.
  link: [billed per-second, with a one-minute minimum](../facts/eks.md#eks-pricing-auto-mode-per-second-one-minute)
eks-pricing-extended-support-additional-cost-per-cluster-hour
  claim: Extended support lets you stay at a specific Kubernetes version for longer, at an additional cost per cluster hour.
  scope: per cluster.
  link: [additional cost per cluster hour](../facts/eks.md#eks-pricing-extended-support-additional-cost-per-cluster-hour)
eks-pricing-fargate-pods-per-second-one-minute
  claim: For EKS pods on AWS Fargate, pricing is calculated from the vCPU and memory resources used, from the start of the container image download until the pod terminates, rounded up to the nearest second. A minimum charge of one minute applies.
  scope: per pod; minimum.
  link: [rounded up to the nearest second](../facts/eks.md#eks-pricing-fargate-pods-per-second-one-minute)
  link: [one minute](../facts/eks.md#eks-pricing-fargate-pods-per-second-one-minute)
eks-pricing-per-cluster-per-hour-fee
  claim: All Amazon EKS clusters have a per cluster per hour fee based on the Kubernetes version of the cluster.
  scope: per cluster.
  link: [per cluster per hour fee](../facts/eks.md#eks-pricing-per-cluster-per-hour-fee)
eks-pricing-provisioned-control-plane-hourly-tier
  claim: Each EKS Provisioned Control Plane scaling tier offers specific control plane capacity and performance, and you pay an hourly rate for the scaling tier your cluster is provisioned on, with no upfront fees or long-term commitments.
  scope: per cluster.
  link: [hourly rate for the scaling tier](../facts/eks.md#eks-pricing-provisioned-control-plane-hourly-tier)
eks-pricing-worker-node-resources-paid-separately
  claim: With Amazon EKS you also pay for the resources you use to run your applications on Kubernetes worker nodes, such as Amazon EC2 instances, Amazon EBS volumes, and public IPv4 addresses, as well as any cross AZ traffic from nodes to the Kubernetes control plane.
  scope: Amazon EKS pricing.
  link: [the resources you use to run your applications](../facts/eks.md#eks-pricing-worker-node-resources-paid-separately)
eks-private-cluster-requirements
  claim: An EKS cluster without outbound internet access must pull images from a container registry that is in your VPC and must have endpoint private access enabled, which nodes need to register with the cluster endpoint; endpoint public access is optional.
  scope: private Amazon EKS clusters.
  link: [a container registry that’s in your VPC](../facts/eks.md#eks-private-cluster-requirements)
  link: [Your cluster must have endpoint private access enabled](../facts/eks.md#eks-private-cluster-requirements)
eks-public-endpoint-cidr-ranges-per-cluster-limit
  claim: One EKS cluster can have at most 40 public endpoint access CIDR ranges, which you specify when you create or update the cluster. The quota is not adjustable.
  scope: per cluster, per Region; maximum; not adjustable.
  link: [40 public endpoint access CIDR ranges](../facts/eks.md#eks-public-endpoint-cidr-ranges-per-cluster-limit)
eks-registered-clusters-quota
  claim: An account can have 10 registered EKS clusters in the current Region by default. The quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [10 registered EKS clusters](../facts/eks.md#eks-registered-clusters-quota)
eks-remote-node-networks-per-cluster-quota
  claim: One EKS cluster can have 15 remote node networks by default. The quota is adjustable.
  scope: per cluster, per Region; default; adjustable.
  link: [15 remote node networks](../facts/eks.md#eks-remote-node-networks-per-cluster-quota)
eks-remote-pod-networks-per-cluster-quota
  claim: One EKS cluster can have 15 remote pod networks by default. The quota is adjustable.
  scope: per cluster, per Region; default; adjustable.
  link: [15 remote pod networks](../facts/eks.md#eks-remote-pod-networks-per-cluster-quota)
eks-savings-plans-for-cluster-compute
  claim: You can use your Savings Plans for compute used in Amazon EKS clusters.
  scope: Amazon EKS cluster compute.
  link: [compute used in Amazon EKS clusters](../facts/eks.md#eks-savings-plans-for-cluster-compute)
eks-selectors-per-fargate-profile-quota
  claim: One EKS Fargate profile can have 5 selectors by default. The quota is adjustable.
  scope: per Fargate profile, per Region; default; adjustable.
  link: [5 selectors](../facts/eks.md#eks-selectors-per-fargate-profile-quota)
eks-self-managed-nodes-in-your-account-billed-ec2
  claim: Amazon EKS nodes run in your AWS account and connect to the control plane of your cluster through the cluster API server endpoint, and you're billed for them based on Amazon EC2 prices; all instances in a node group must use the Amazon EKS node IAM role.
  scope: Amazon EKS self-managed nodes.
  link: [Amazon EKS nodes run in your AWS account](../facts/eks.md#eks-self-managed-nodes-in-your-account-billed-ec2)
  link: [billed for them based on Amazon EC2 prices](../facts/eks.md#eks-self-managed-nodes-in-your-account-billed-ec2)
  link: [the Amazon EKS node IAM role](../facts/eks.md#eks-self-managed-nodes-in-your-account-billed-ec2)
eks-standard-support-14-months
  claim: A Kubernetes minor version is under standard support in Amazon EKS for the first 14 months after it is released.
  scope: per Kubernetes minor version; fixed; not adjustable.
  link: [14 months](../facts/eks.md#eks-standard-support-14-months)
eks-stateless-application-no-session-data-deployment
  claim: A stateless application doesn't save a client's session data, so another session doesn't need to refer back to what happened in a previous session; this makes it easier to replace Pods with new ones if they become unhealthy, or to move them around without saving state.
  scope: Kubernetes on Amazon EKS.
  link: [doesn’t save a client’s session data](../facts/eks.md#eks-stateless-application-no-session-data-deployment)
  link: [replace Pods with new ones](../facts/eks.md#eks-stateless-application-no-session-data-deployment)
eks-supports-at-least-three-versions
  claim: Amazon EKS is committed to offering support for at least three Kubernetes versions at any given time.
  scope: Amazon EKS Kubernetes version support; minimum; not adjustable.
  link: [at least three Kubernetes versions](../facts/eks.md#eks-supports-at-least-three-versions)
eks-version-rollback-within-7-days
  claim: An EKS cluster that was upgraded through an in-place upgrade can be rolled back to the previous minor version within 7 days of the upgrade completing; to roll back to a version in extended support you must first change the upgrade policy of the cluster to EXTENDED, and clusters that were automatically upgraded at the end of extended support cannot be rolled back.
  scope: per cluster, in-place upgrade; maximum; not adjustable.
  link: [within 7 days](../facts/eks.md#eks-version-rollback-within-7-days)
eks-version-total-support-26-months
  claim: Each Kubernetes version is supported in Amazon EKS for 26 months in total: 14 months of standard support plus 12 months of extended support.
  scope: per Kubernetes minor version; fixed; not adjustable.
  link: [26 months](../facts/eks.md#eks-version-total-support-26-months)
eks-vpa-adjusts-cpu-memory-reservations
  claim: The Kubernetes Vertical Pod Autoscaler automatically adjusts the CPU and memory reservations for your Pods to help right size your applications, which can improve cluster resource utilization.
  scope: Kubernetes Vertical Pod Autoscaler on Amazon EKS.
  link: [adjusts the CPU and memory reservations](../facts/eks.md#eks-vpa-adjusts-cpu-memory-reservations)
  link: [improve cluster resource utilization](../facts/eks.md#eks-vpa-adjusts-cpu-memory-reservations)
eks-vpc-cni-not-for-hybrid-nodes
  claim: The Amazon VPC CNI is not supported for use with EKS hybrid nodes.
  scope: Amazon EKS Hybrid Nodes.
  link: [isn’t supported for use with hybrid nodes](../facts/eks.md#eks-vpc-cni-not-for-hybrid-nodes)
eks-vpc-cni-pods-get-vpc-ip-addresses
  claim: The Amazon VPC CNI plugin add-on assigns a private IPv4 or IPv6 address from your VPC to each Pod, and it is the only CNI plugin supported by Amazon EKS for nodes that run on AWS infrastructure.
  scope: Amazon VPC CNI plugin on Amazon EKS.
  link: [`IPv4` or `IPv6` address from your VPC](../facts/eks.md#eks-vpc-cni-pods-get-vpc-ip-addresses)
  link: [the only CNI plugin supported by Amazon EKS](../facts/eks.md#eks-vpc-cni-pods-get-vpc-ip-addresses)
eks-whitepaper-natural-migration-path-for-kubernetes
  claim: The Containers on AWS whitepaper says Amazon EKS provides a natural migration path if you use Kubernetes already and want to continue using it on AWS, and you can migrate any standard Kubernetes application to Amazon EKS without refactoring your code.
  scope: Amazon EKS.
  link: [natural migration path if you use Kubernetes already](../facts/eks.md#eks-whitepaper-natural-migration-path-for-kubernetes)
  link: [without refactoring your code](../facts/eks.md#eks-whitepaper-natural-migration-path-for-kubernetes)
eks-zonal-shift-temporary-move-traffic-from-impaired-az
  claim: Amazon Application Recovery Controller (ARC) zonal shift is a temporary measure that moves traffic for a resource away from an impaired Availability Zone until the zonal shift expires or you cancel it, and you can start it for an EKS cluster or let AWS shift traffic for you with zonal autoshift.
  scope: Amazon EKS with ARC zonal shift.
  link: [away from an impaired AZ](../facts/eks.md#eks-zonal-shift-temporary-move-traffic-from-impaired-az)
  link: [enabling zonal autoshift](../facts/eks.md#eks-zonal-shift-temporary-move-traffic-from-impaired-az)
fargate-awsvpc-needs-subnets-and-security-groups
  claim: Amazon ECS tasks for AWS Fargate require the awsvpc network mode, which provides each task with an elastic network interface; when you run a task or create a service with this network mode, you must specify one or more subnets to attach the network interface and one or more security groups to apply to it.
  scope: AWS Fargate tasks.
  link: [you must specify one or more subnets](../facts/fargate.md#fargate-awsvpc-needs-subnets-and-security-groups)
  link: [one or more security groups](../facts/fargate.md#fargate-awsvpc-needs-subnets-and-security-groups)
fargate-cannot-detach-or-modify-enis
  claim: You cannot manually detach or modify the ENIs that Fargate creates and attaches; to release the ENIs of a task, stop the task.
  scope: Fargate task ENIs.
  link: [You can't manually detach or modify the ENIs](../facts/fargate.md#fargate-cannot-detach-or-modify-enis)
  link: [To release the ENIs for a task](../facts/fargate.md#fargate-cannot-detach-or-modify-enis)
fargate-capacity-provider-must-be-associated-first
  claim: You must associate a capacity provider with a cluster before you associate it with a capacity provider strategy.
  scope: ECS capacity providers.
  link: [associate a capacity provider with a cluster before](../facts/fargate.md#fargate-capacity-provider-must-be-associated-first)
  link: [capacity provider strategy](../facts/fargate.md#fargate-capacity-provider-must-be-associated-first)
fargate-classic-load-balancer-not-supported
  claim: Classic Load Balancer is not supported for ECS services with tasks that use Fargate.
  scope: ECS services on Fargate.
  link: [Classic Load Balancer isn't supported](../facts/fargate.md#fargate-classic-load-balancer-not-supported)
fargate-compute-savings-plans-cover-fargate-lambda
  claim: Compute Savings Plans automatically apply to your EC2 instance usage regardless of instance family, instance size, Region, operating system, or tenancy, and they also apply to your Fargate and Lambda usage.
  scope: Compute Savings Plans.
  link: [apply to your Fargate and Lambda usage](../facts/fargate.md#fargate-compute-savings-plans-cover-fargate-lambda)
fargate-containers-cannot-access-host-resources
  claim: Fargate prevents containers from accessing the underlying host's resources, such as the file system, devices, networking, and container runtime.
  scope: AWS Fargate tasks.
  link: [prevents containers from accessing the underlying host](../facts/fargate.md#fargate-containers-cannot-access-host-resources)
  link: [the file system, devices, networking, and container runtime](../facts/fargate.md#fargate-containers-cannot-access-host-resources)
fargate-ebs-volumes-need-linux-platform-1-4-0
  claim: Amazon EBS volumes on Fargate are supported on Linux with platform version 1.4.0 or later. They are not supported for Windows containers on Fargate.
  scope: per Fargate task; minimum; Linux only.
  link: [platform version 1.4.0 or later (Linux)](../facts/fargate.md#fargate-ebs-volumes-need-linux-platform-1-4-0)
fargate-ecr-endpoint-uses-private-ip
  claim: When container images are hosted in Amazon ECR, you can configure Amazon ECR to use an interface VPC endpoint and the image pull occurs over the task's private IPv4 address.
  scope: Fargate tasks pulling from Amazon ECR.
  link: [Amazon ECR to use an interface VPC endpoint](../facts/fargate.md#fargate-ecr-endpoint-uses-private-ip)
  link: [over the task's private IPv4 address](../facts/fargate.md#fargate-ecr-endpoint-uses-private-ip)
fargate-eks-pod-default-size-quarter-vcpu
  claim: If you do not specify a vCPU and memory combination for an EKS Pod on Fargate, the smallest available combination is used, which is .25 vCPU and 0.5 GB of memory.
  scope: per EKS Pod on Fargate; default; not adjustable.
  link: [.25 vCPU and 0.5 GB memory](../facts/fargate.md#fargate-eks-pod-default-size-quarter-vcpu)
fargate-eks-pod-ephemeral-storage-default-20-gib
  claim: Each EKS Pod running on Fargate receives a default 20 GiB of ephemeral storage, which is deleted after the Pod stops.
  scope: per EKS Pod on Fargate; default; not adjustable.
  link: [20 GiB](../facts/fargate.md#fargate-eks-pod-ephemeral-storage-default-20-gib)
fargate-eks-pod-ephemeral-storage-max-175-gib
  claim: The ephemeral storage of an EKS Pod on Fargate can be increased up to a maximum of 175 GiB.
  scope: per EKS Pod on Fargate; maximum; adjustable.
  link: [175 GiB](../facts/fargate.md#fargate-eks-pod-ephemeral-storage-max-175-gib)
fargate-eks-pod-size-largest-16-vcpu
  claim: For an EKS Pod on Fargate, the 16 vCPU value supports between 32 GB and 120 GB of memory in 8-GB increments.
  scope: per EKS Pod on Fargate.
  link: [16 vCPU](../facts/fargate.md#fargate-eks-pod-size-largest-16-vcpu)
  link: [Between 32 GB and 120 GB](../facts/fargate.md#fargate-eks-pod-size-largest-16-vcpu)
fargate-ephemeral-storage-cmk-audit-cloudtrail
  claim: Fargate customer managed keys for ephemeral storage can be imported into AWS KMS or created in AWS KMS, perform standard AWS KMS lifecycle actions such as rotate, disable and delete, and key access and usage can be audited in CloudTrail logs.
  scope: Fargate ephemeral storage encryption with customer managed keys.
  link: [import your own keys into AWS KMS](../facts/fargate.md#fargate-ephemeral-storage-cmk-audit-cloudtrail)
  link: [audit key access and usage in CloudTrail logs](../facts/fargate.md#fargate-ephemeral-storage-cmk-audit-cloudtrail)
fargate-ephemeral-storage-cmk-no-extra-charge
  claim: Fargate does not charge anything extra for using customer managed keys on ephemeral storage; you are only charged the standard price for using AWS KMS keys for storage and API requests.
  scope: Fargate ephemeral storage encryption with customer managed keys.
  link: [doesn't charge anything extra](../facts/fargate.md#fargate-ephemeral-storage-cmk-no-extra-charge)
  link: [the standard price for using AWS KMS keys](../facts/fargate.md#fargate-ephemeral-storage-cmk-no-extra-charge)
fargate-ephemeral-storage-default-20-gib
  claim: By default, an ECS task on Fargate with platform version 1.4.0 or later receives a minimum of 20 GiB of ephemeral storage. The total can be increased.
  scope: per Fargate task, platform version 1.4.0 or later; default; adjustable.
  link: [20 GiB](../facts/fargate.md#fargate-ephemeral-storage-default-20-gib)
fargate-ephemeral-storage-encrypted-by-default
  claim: For Fargate tasks on platform version 1.4.0 or later launched on May 28, 2020 or later, ephemeral storage is encrypted with an AES-256 encryption algorithm that uses an AWS owned encryption key, or you can create your own customer managed key.
  scope: Fargate tasks on Linux platform version 1.4.0 or later launched on May 28, 2020 or later; default; adjustable; customer managed key is optional.
  link: [encrypted with an AES-256 encryption algorithm](../facts/fargate.md#fargate-ephemeral-storage-encrypted-by-default)
  link: [an AWS owned encryption key](../facts/fargate.md#fargate-ephemeral-storage-encrypted-by-default)
fargate-ephemeral-storage-linux-only-windows-not
  claim: Each ECS task hosted on Linux containers on Fargate receives ephemeral storage for bind mounts that containers can share; this isn't supported for Windows containers on Fargate.
  scope: Fargate ephemeral storage page intro.
  link: [task hosted on Linux containers on AWS Fargate](../facts/fargate.md#fargate-ephemeral-storage-linux-only-windows-not)
  link: [This isn't supported for Windows containers](../facts/fargate.md#fargate-ephemeral-storage-linux-only-windows-not)
fargate-ephemeral-storage-max-200-gib
  claim: The total ephemeral storage of an ECS task on Fargate (platform version 1.4.0 or later) can be increased up to a maximum of 200 GiB.
  scope: per Fargate task, platform version 1.4.0 or later; maximum; adjustable.
  link: [200 GiB](../facts/fargate.md#fargate-ephemeral-storage-max-200-gib)
fargate-faq-20-gb-ephemeral-storage-included-in-price
  claim: 20 GB of ephemeral storage is available by default for every Fargate task and pod, and you only pay for any additional storage you configure.
  scope: per Fargate task or pod; default; you pay only for additional storage that you configure.
  link: [20 GB of ephemeral storage](../facts/fargate.md#fargate-faq-20-gb-ephemeral-storage-included-in-price)
fargate-faq-arm-on-ecs-via-arm64
  claim: With Amazon ECS, Fargate runs Arm-based applications when you use Arm-compatible or multi-architecture container images from Amazon ECR.
  scope: AWS Fargate with Amazon ECS; Arm-compatible or multi-architecture images.
  link: [run your Arm-based applications](../facts/fargate.md#fargate-faq-arm-on-ecs-via-arm64)
fargate-faq-arm-on-eks-not-supported
  claim: Arm workloads on Amazon EKS are not supported on Fargate according to the FAQ; use Amazon EC2 to run them.
  scope: Arm workloads on Amazon EKS with AWS Fargate; as stated in the FAQ today.
  link: [not supported on AWS Fargate today](../facts/fargate.md#fargate-faq-arm-on-eks-not-supported)
fargate-faq-billing-dimensions-and-minimum
  claim: You pay for the vCPU, memory and storage resources your containerized application provisions; vCPU and memory are billed from image pull until the task or pod terminates, rounded up to the nearest second, with a 1 minute minimum.
  scope: per Amazon ECS task or EKS pod on AWS Fargate; minimum; vCPU and memory from image pull until termination, rounded up to the nearest second.
  link: [vCPU, memory, and storage resources](../facts/fargate.md#fargate-faq-billing-dimensions-and-minimum)
  link: [1 minute](../facts/fargate.md#fargate-faq-billing-dimensions-and-minimum)
fargate-faq-choose-for-isolation-and-no-ec2-management
  claim: Choose AWS Fargate for its isolation model and security, and when you want to launch containers without provisioning or managing EC2 instances.
  scope: AWS Fargate selection.
  link: [for its isolation model and security](../facts/fargate.md#fargate-faq-choose-for-isolation-and-no-ec2-management)
fargate-faq-compliance-programs
  claim: AWS Fargate meets the standards for a wide array of compliance programs, including PCI DSS, SOC, FIPS 140-2, FedRAMP and HIPAA.
  scope: AWS Fargate.
  link: [PCI DSS, SOC, FIPS 140-2, FedRAMP, and HIPAA](../facts/fargate.md#fargate-faq-compliance-programs)
fargate-faq-dedicated-eni-per-task-or-pod
  claim: On Fargate each ECS task or Kubernetes pod gets a dedicated elastic network interface attached into your VPC, and all traffic in and out of the workload goes through this ENI.
  scope: each ECS task or Kubernetes pod on AWS Fargate.
  link: [dedicated elastic network interface (ENI)](../facts/fargate.md#fargate-faq-dedicated-eni-per-task-or-pod)
fargate-faq-efs-for-persistent-storage
  claim: Amazon EFS can provide persistent storage to workloads running on AWS Fargate.
  scope: AWS Fargate workloads.
  link: [Amazon Elastic File System (EFS)](../facts/fargate.md#fargate-faq-efs-for-persistent-storage)
fargate-faq-ephemeral-storage-20-gib-erased
  claim: Each workload that runs on AWS Fargate is given full access to 20 GiB of ephemeral storage to use as temporary storage while it runs, and data in this volume is erased once the workload stops; this ephemeral storage volume can be expanded up to 200GiB on Amazon ECS and 175 GiB on Amazon EKS.
  scope: per Fargate workload; default; adjustable; temporary; erased when the workload stops.
  link: [20 GiB](../facts/fargate.md#fargate-faq-ephemeral-storage-20-gib-erased)
fargate-faq-ephemeral-storage-expand-max
  claim: Fargate ephemeral storage can be expanded up to 200 GiB on Amazon ECS and 175 GiB on Amazon EKS.
  scope: per Fargate workload; Amazon ECS and Amazon EKS; maximum; not adjustable; configured by expanding the ephemeral volume above the default.
  link: [200GiB on Amazon ECS](../facts/fargate.md#fargate-faq-ephemeral-storage-expand-max)
  link: [175 GiB on Amazon EKS](../facts/fargate.md#fargate-faq-ephemeral-storage-expand-max)
fargate-faq-gpu-not-supported
  claim: GPU workloads are not supported on AWS Fargate according to the FAQ; use Amazon EC2 for GPU workloads.
  scope: AWS Fargate; as stated in the FAQ today; check the user guide.
  link: [not supported on AWS Fargate today](../facts/fargate.md#fargate-faq-gpu-not-supported)
fargate-faq-graviton-price-performance
  claim: Fargate on Graviton processors delivers up to 40% improved price/performance at 20% lower cost than comparable Intel x86-based Fargate.
  scope: AWS Fargate on AWS Graviton processors; maximum; compared with comparable Intel x86-based Fargate.
  link: [up to 40% improved price/performance](../facts/fargate.md#fargate-faq-graviton-price-performance)
  link: [20% lower cost](../facts/fargate.md#fargate-faq-graviton-price-performance)
fargate-faq-hipaa-eligible-with-baa
  claim: AWS Fargate is HIPAA-eligible; with an executed Business Associate Addendum with AWS you can process encrypted PHI using containers on Fargate.
  scope: AWS Fargate; an executed Business Associate Addendum with AWS; encrypted PHI.
  link: [AWS Fargate is HIPAA-eligible](../facts/fargate.md#fargate-faq-hipaa-eligible-with-baa)
fargate-faq-kaniko-rootless-image-build
  claim: Rootless image build projects such as Kaniko can be deployed within the Fargate security model and are a viable way to build container images.
  scope: AWS Fargate.
  link: [Kaniko](../facts/fargate.md#fargate-faq-kaniko-rootless-image-build)
fargate-faq-multi-account-for-tens-of-thousands-of-cores
  claim: For workloads that need significant scale, in the range of 10,000s of cores, AWS recommends a multi-account strategy.
  scope: AWS Fargate large-scale workloads.
  link: [10,000s of cores](../facts/fargate.md#fargate-faq-multi-account-for-tens-of-thousands-of-cores)
  link: [multi-account strategy](../facts/fargate.md#fargate-faq-multi-account-for-tens-of-thousands-of-cores)
fargate-faq-need-ec2-control-use-without-fargate
  claim: If you need greater control of your EC2 instances or broader customization options, use Amazon ECS or Amazon EKS without Fargate.
  scope: AWS Fargate selection.
  link: [greater control of your Amazon EC2 instances](../facts/fargate.md#fargate-faq-need-ec2-control-use-without-fargate)
fargate-faq-new-accounts-lower-quotas-raisable
  claim: New AWS accounts might have lower initial Fargate quotas that can increase over time, and you can request to raise these soft limits through the standard service quota increase process.
  scope: AWS Fargate quotas, new accounts; standard AWS service quota increase process.
  link: [raise these soft limits](../facts/fargate.md#fargate-faq-new-accounts-lower-quotas-raisable)
fargate-faq-no-privileged-mode-or-docker-socket
  claim: Building images from inside a container with Docker in Docker is not possible on Fargate because privileged mode is unavailable, and mounting the docker socket is unavailable because Fargate uses containerd as of platform version 1.4.
  scope: AWS Fargate; platform version 1.4 and later use containerd.
  link: [unavailable in AWS Fargate's security model](../facts/fargate.md#fargate-faq-no-privileged-mode-or-docker-socket)
fargate-faq-quotas-based-on-vcpu-per-region-account
  claim: Fargate service quotas are based on the number of vCPU cores used in a Region in an account.
  scope: per Region, per account.
  link: [number of vCPU cores used](../facts/fargate.md#fargate-faq-quotas-based-on-vcpu-per-region-account)
fargate-faq-security-groups-nacls-flow-logs-on-eni
  claim: On AWS Fargate, each ECS task or Kubernetes Pod is given a dedicated elastic network interface (ENI) in your VPC, and all traffic in and out of the workload goes through this ENI; therefore VPC security groups and network ACLs can be used to secure the ENI, and VPC Flow Logs can be used to monitor traffic flows.
  scope: AWS Fargate workloads.
  link: [VPC Security Groups and VPC network ACLs](../facts/fargate.md#fargate-faq-security-groups-nacls-flow-logs-on-eni)
fargate-faq-serverless-engine-for-ecs-and-eks
  claim: AWS Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS.
  scope: AWS Fargate.
  link: [serverless compute engine for containers](../facts/fargate.md#fargate-faq-serverless-engine-for-ecs-and-eks)
fargate-faq-sidecar-integration-mechanism
  claim: The common way to integrate Fargate with other systems is to run a sidecar container in the Fargate task, such as a runtime security agent or log router.
  scope: AWS Fargate tasks.
  link: [a sidecar container within a AWS Fargate task](../facts/fargate.md#fargate-faq-sidecar-integration-mechanism)
fargate-faq-single-tenant-instance-per-workload
  claim: Each Fargate workload runs on its own single-use, single-tenant compute instance, isolated by a virtualization boundary; each ECS task or Kubernetes pod runs on a newly provisioned instance.
  scope: each ECS task or Kubernetes pod on AWS Fargate.
  link: [its own single use, single tenant compute instance](../facts/fargate.md#fargate-faq-single-tenant-instance-per-workload)
fargate-faq-sla-credit-condition
  claim: You are eligible for a Fargate SLA credit under the Compute SLA if more than one Availability Zone in which you run a task, within the same Region, has a Monthly Uptime Percentage below 99.99% during a monthly billing cycle.
  scope: AWS Fargate, per monthly billing cycle; more than one Availability Zone in the same Region where you run a task.
  link: [less than 99.99%](../facts/fargate.md#fargate-faq-sla-credit-condition)
fargate-faq-sla-monthly-uptime
  claim: The Compute SLA guarantees a Monthly Uptime Percentage of at least 99.99% for AWS Fargate.
  scope: AWS Fargate, Compute SLA, monthly; minimum; at least.
  link: [99.99%](../facts/fargate.md#fargate-faq-sla-monthly-uptime)
  say: ninety-nine point nine nine percent
fargate-faq-spot-and-compute-savings-plan-pricing
  claim: AWS Fargate supports Spot and Compute Savings Plan pricing options, just like Amazon EC2 instances.
  scope: AWS Fargate.
  link: [Spot and Compute Savings Plan pricing options](../facts/fargate.md#fargate-faq-spot-and-compute-savings-plan-pricing)
fargate-faq-spot-up-to-70-percent-discount
  claim: Fargate Spot lets you run interruption-tolerant Amazon ECS tasks at up to a 70 percent discount off the Fargate price.
  scope: Fargate Spot, Amazon ECS tasks; maximum; interruption tolerant tasks.
  link: [up to a 70 percent discount](../facts/fargate.md#fargate-faq-spot-up-to-70-percent-discount)
fargate-faq-windows-license-built-into-price
  claim: AWS Fargate manages the Windows OS licenses for you, and the cost of doing so is built into the Fargate pricing.
  scope: AWS Fargate Windows containers.
  link: [manage the Windows OS licenses for you](../facts/fargate.md#fargate-faq-windows-license-built-into-price)
fargate-faq-zstd-images-start-faster
  claim: Container image layers are compressed with gzip by default; containerd supports zstd, which decompresses more quickly and gives faster task launch times on Fargate.
  scope: AWS Fargate task startup; container images built with zstd compression.
  link: [zstd](../facts/fargate.md#fargate-faq-zstd-images-start-faster)
fargate-guide-containers-run-indefinitely-no-hard-limit
  claim: The AWS decision guide says containers in Fargate can run indefinitely because there is no hard limit on execution time, which makes Fargate ideal for applications that need to run continuously.
  scope: AWS Fargate.
  link: [The containers in Fargate can run indefinitely](../facts/fargate.md#fargate-guide-containers-run-indefinitely-no-hard-limit)
  link: [there is no hard limit on execution time](../facts/fargate.md#fargate-guide-containers-run-indefinitely-no-hard-limit)
fargate-guide-ideal-long-running-microservices-batch
  claim: The AWS decision guide says Fargate is a serverless compute engine for containers that is ideal for long-running applications, microservices, or batch processing, and gives you fine-grained control over CPU and memory without managing servers.
  scope: AWS Fargate.
  link: [ideal for long-running applications, microservices, or batch processing](../facts/fargate.md#fargate-guide-ideal-long-running-microservices-batch)
  link: [fine-grained control over resource allocation (CPU, memory)](../facts/fargate.md#fargate-guide-ideal-long-running-microservices-batch)
fargate-guide-lambda-mi-for-steady-state
  claim: The AWS decision guide says that if your workloads are steady-state or predictable and benefit from EC2 pricing and specialized compute, Lambda Managed Instances might be well suited.
  scope: AWS Lambda compared with AWS Fargate.
  link: [workloads are steady-state or predictable](../facts/fargate.md#fargate-guide-lambda-mi-for-steady-state)
  link: [Lambda Managed Instances might be well suited](../facts/fargate.md#fargate-guide-lambda-mi-for-steady-state)
fargate-guide-lambda-short-lived-15-minutes
  claim: The AWS decision guide says Lambda functions have a maximum execution time of 15 minutes per invocation, which makes them well-suited for scenarios such as file processing, real-time data streaming, and HTTP request handling.
  scope: AWS Lambda compared with AWS Fargate; maximum.
  link: [maximum execution time of 15 minutes per invocation](../facts/fargate.md#fargate-guide-lambda-short-lived-15-minutes)
  link: [real-time data streaming, and HTTP request handling](../facts/fargate.md#fargate-guide-lambda-short-lived-15-minutes)
fargate-guide-lambda-stateless-state-external
  claim: In the AWS decision guide, each invocation of a standard Lambda function is independent and stateless, and any state or data that needs to persist between invocations must be managed externally.
  scope: AWS Lambda compared with AWS Fargate; standard functions.
  link: [each invocation is independent and stateless](../facts/fargate.md#fargate-guide-lambda-stateless-state-external)
  link: [must be managed externally](../facts/fargate.md#fargate-guide-lambda-stateless-state-external)
fargate-guide-not-natively-event-driven
  claim: In the AWS decision guide, Fargate can integrate with event sources such as Amazon SQS and Kinesis with some additional boilerplate logic, while Lambda handles most of this integration for you and with Fargate you must implement the integration yourself using the APIs for these services.
  scope: AWS Fargate compared with AWS Lambda.
  link: [you must implement this integration yourself](../facts/fargate.md#fargate-guide-not-natively-event-driven)
  link: [Lambda handles the bulk of this integration logic](../facts/fargate.md#fargate-guide-not-natively-event-driven)
fargate-guide-pricing-per-second-pay-for-what-you-provision
  claim: The AWS decision guide says you are billed for Fargate per second with a one-minute minimum charge, you pay for what you provision whether or not the application is processing requests, and Fargate is well-suited for predictable workloads that need specific resource configurations.
  scope: AWS Fargate.
  link: [billed per second, with a one-minute minimum charge](../facts/fargate.md#fargate-guide-pricing-per-second-pay-for-what-you-provision)
  link: [You pay for what you provision](../facts/fargate.md#fargate-guide-pricing-per-second-pay-for-what-you-provision)
fargate-launch-type-requires-task-definition-config
  claim: To use Fargate, you must configure your task definition to use the Fargate launch type; Fargate tasks do not support all ECS task definition parameters.
  scope: Fargate task definitions.
  link: [use the Fargate launch type](../facts/fargate.md#fargate-launch-type-requires-task-definition-config)
  link: [all of the Amazon ECS task definition parameters](../facts/fargate.md#fargate-launch-type-requires-task-definition-config)
fargate-limited-linux-capabilities
  claim: On Fargate, additional Linux capabilities such as CAP_SYS_ADMIN and CAP_NET_ADMIN are restricted to prevent a privilege escalation.
  scope: AWS Fargate tasks.
  link: [are restricted to prevent a privilege escalation](../facts/fargate.md#fargate-limited-linux-capabilities)
fargate-network-security-groups-nacls-ip-from-subnet
  claim: For Fargate you can use security groups and network ACLs to control inbound and outbound traffic, and Fargate tasks receive an IP address from the configured subnet in your VPC.
  scope: AWS Fargate tasks.
  link: [security groups and network ACLs](../facts/fargate.md#fargate-network-security-groups-nacls-ip-from-subnet)
  link: [receive an IP address from the configured subnet](../facts/fargate.md#fargate-network-security-groups-nacls-ip-from-subnet)
fargate-new-tasks-latest-revision-patched
  claim: A new task that runs on Fargate always runs on the latest revision of a platform version, so tasks always start on secure and patched infrastructure; to use the latest revision for an existing task you must start a new task.
  scope: AWS Fargate tasks.
  link: [the latest revision of a platform version](../facts/fargate.md#fargate-new-tasks-latest-revision-patched)
  link: [started on secure and patched infrastructure](../facts/fargate.md#fargate-new-tasks-latest-revision-patched)
fargate-no-daemon-scheduling-strategy
  claim: Fargate tasks do not support the DAEMON scheduling strategy.
  scope: AWS Fargate.
  link: [do not support the `DAEMON` scheduling strategy](../facts/fargate.md#fargate-no-daemon-scheduling-strategy)
fargate-no-docker-volumes
  claim: Fargate tasks only support bind mount host volumes, so the dockerVolumeConfiguration parameter is not supported.
  scope: Fargate task definitions.
  link: [Fargate tasks only support bind mount host volumes](../facts/fargate.md#fargate-no-docker-volumes)
  link: [`dockerVolumeConfiguration` parameter is not supported](../facts/fargate.md#fargate-no-docker-volumes)
fargate-no-host-access-ecs-exec
  claim: Neither customers nor AWS operators can connect to a host running customer workloads on Fargate; you can use ECS exec to run commands in, or get a shell to, a container running on Fargate.
  scope: AWS Fargate tasks.
  link: [Neither customers nor AWS operators can connect](../facts/fargate.md#fargate-no-host-access-ecs-exec)
  link: [use ECS exec to run commands](../facts/fargate.md#fargate-no-host-access-ecs-exec)
fargate-no-placement-constraints
  claim: If you use Fargate, task placement constraints aren't supported.
  scope: AWS Fargate.
  link: [task placement constraints aren't supported](../facts/fargate.md#fargate-no-placement-constraints)
  link: [If you use Fargate](../facts/fargate.md#fargate-no-placement-constraints)
fargate-no-placement-strategies-best-effort-az-spread
  claim: Task placement strategies and constraints are not supported for tasks using Fargate; Fargate tries its best to spread tasks across accessible Availability Zones, and when the capacity provider includes both Fargate and Fargate Spot the spread behavior is independent for each capacity provider.
  scope: Amazon ECS tasks on AWS Fargate.
  link: [Task placement strategies and constraints aren't supported](../facts/fargate.md#fargate-no-placement-strategies-best-effort-az-spread)
  link: [try its best to spread tasks](../facts/fargate.md#fargate-no-placement-strategies-best-effort-az-spread)
fargate-no-privileged-containers
  claim: Features such as privileged containers or access are currently unavailable on Fargate, which affects use cases such as running Docker in Docker.
  scope: AWS Fargate tasks.
  link: [privileged containers or access are currently unavailable](../facts/fargate.md#fargate-no-privileged-containers)
  link: [running Docker in Docker](../facts/fargate.md#fargate-no-privileged-containers)
fargate-no-provision-vm-clusters
  claim: With Fargate you no longer provision, configure, or scale clusters of virtual machines to run containers, which removes the need to choose server types, decide when to scale, or optimize cluster packing.
  scope: AWS Fargate with Amazon ECS.
  link: [provision, configure, or scale clusters](../facts/fargate.md#fargate-no-provision-vm-clusters)
  link: [choose server types](../facts/fargate.md#fargate-no-provision-vm-clusters)
fargate-ondemand-burst-launch-rate-quota
  claim: In a single burst, an account can launch up to 100 on-demand ECS tasks or EKS pods on Fargate in each of the other supported Regions; in the Regions the quota row lists, such as af-south-1, and in Regions introduced after May 20, 2025, the maximum is 25 on-demand ECS tasks or EKS pods. The quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [100 on-demand ECS tasks or EKS pods](../facts/fargate.md#fargate-ondemand-burst-launch-rate-quota)
  link: [25 on-demand ECS tasks or EKS pods](../facts/fargate.md#fargate-ondemand-burst-launch-rate-quota)
fargate-ondemand-sustained-launch-rate-quota
  claim: Fargate can launch up to 20 on-demand ECS tasks or EKS pods per second (sustained rate) in each of the other supported Regions; in the Regions the quota row lists, such as af-south-1, and in Regions introduced after May 20, 2025, the maximum is 5 on-demand ECS tasks or EKS pods per second. The quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [20 on-demand ECS tasks or EKS pods per second](../facts/fargate.md#fargate-ondemand-sustained-launch-rate-quota)
  link: [5 on-demand ECS tasks or EKS pods per second](../facts/fargate.md#fargate-ondemand-sustained-launch-rate-quota)
fargate-ondemand-vcpu-quota
  claim: The default Fargate On-Demand quota is 6 vCPUs running concurrently in an account in the current Region. The quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [6 vCPUs](../facts/fargate.md#fargate-ondemand-vcpu-quota)
fargate-ondemand-vcpu-quota-eks-page
  claim: The EKS page lists the same AWS Fargate quota: the Fargate On-Demand vCPU resource count has a default of 6 vCPUs and is adjustable.
  scope: per account, per Region; vCPUs running concurrently as Fargate On-Demand; default; adjustable.
  link: [6 vCPUs](../facts/fargate.md#fargate-ondemand-vcpu-quota-eks-page)
fargate-one-eni-per-task-flow-logs
  claim: Every ECS task on Fargate is provided an elastic network interface with a primary private IP address by default; a task can only have one ENI associated at a time, and because each task has its own ENI you can use VPC Flow Logs to monitor its traffic.
  scope: each Fargate task; default.
  link: [can only have one ENI](../facts/fargate.md#fargate-one-eni-per-task-flow-logs)
  link: [networking features such as VPC Flow Logs](../facts/fargate.md#fargate-one-eni-per-task-flow-logs)
fargate-platform-version-defined
  claim: A Fargate platform version refers to a specific runtime environment for Fargate task infrastructure; it is a combination of the kernel and container runtime versions, and you select it when you run a task or create a service.
  scope: AWS Fargate.
  link: [a specific runtime environment for Fargate task infrastructure](../facts/fargate.md#fargate-platform-version-defined)
  link: [the kernel and container runtime versions](../facts/fargate.md#fargate-platform-version-defined)
fargate-pricing-dimensions-vcpu-memory-os-arch-storage
  claim: Fargate pricing is based on the requested vCPU, memory, operating system, CPU architecture and storage of the task or pod.
  scope: per task or pod.
  link: [requested vCPU, memory, Operating Systems](../facts/fargate.md#fargate-pricing-dimensions-vcpu-memory-os-arch-storage)
fargate-pricing-dimensions-vcpu-memory-storage-per-second
  claim: With AWS Fargate you pay for the amount of vCPU, memory, and storage resources that your containerized application requests, calculated from the time container images are pulled until the task terminates, rounded up to the nearest second, with a minimum charge of one minute.
  scope: per Amazon ECS task on AWS Fargate; minimum; from image pull until the task terminates.
  link: [vCPU, memory, and storage resources](../facts/fargate.md#fargate-pricing-dimensions-vcpu-memory-storage-per-second)
  link: [rounded up to the nearest second](../facts/fargate.md#fargate-pricing-dimensions-vcpu-memory-storage-per-second)
  link: [A minimum charge of one minute applies](../facts/fargate.md#fargate-pricing-dimensions-vcpu-memory-storage-per-second)
fargate-pricing-per-second-one-minute-minimum
  claim: Fargate pricing is calculated per second with a 1-minute minimum; duration runs from the time you start to download your container image (Docker pull) until the task terminates, rounded up to the nearest second. For Windows containers, billing is calculated per second with a 5-minute minimum.
  scope: per task or pod; minimum.
  link: [per second with a 1-minute minimum](../facts/fargate.md#fargate-pricing-per-second-one-minute-minimum)
  link: [per second with a 5-minute minimum](../facts/fargate.md#fargate-pricing-per-second-one-minute-minimum)
fargate-pricing-savings-plans-up-to-50-percent
  claim: According to the Fargate pricing page, Savings Plans offer savings of up to 50% on AWS Fargate usage in exchange for a commitment to use a specific amount of compute, measured in dollars per hour, for a one- or three-year term.
  scope: per commitment; maximum.
  link: [up to 50%](../facts/fargate.md#fargate-pricing-savings-plans-up-to-50-percent)
  link: [one- or three-year term](../facts/fargate.md#fargate-pricing-savings-plans-up-to-50-percent)
fargate-pricing-windows-5-minute-minimum
  claim: For Windows containers on Fargate, billing is calculated per second with a 5-minute minimum.
  scope: per Windows task; minimum.
  link: [5-minute minimum](../facts/fargate.md#fargate-pricing-windows-5-minute-minimum)
fargate-private-subnet-image-pull-needs-nat
  claim: For a Fargate task in a private subnet to pull container images, you need a NAT gateway in the subnet to route requests to the internet; when you host your container images in Amazon ECR, you can configure Amazon ECR to use an interface VPC endpoint, and in this case the task's private IPv4 address is used for the image pull.
  scope: Fargate task in a private subnet.
  link: [you need a NAT gateway in the subnet](../facts/fargate.md#fargate-private-subnet-image-pull-needs-nat)
  link: [use an interface VPC endpoint](../facts/fargate.md#fargate-private-subnet-image-pull-needs-nat)
fargate-public-subnet-image-pull-needs-public-ip
  claim: For a Fargate task in a public subnet to pull container images, a public IP address needs to be assigned to the task's elastic network interface, with a route to the internet or to a NAT gateway.
  scope: Fargate task in a public subnet; to pull container images.
  link: [a public IP address needs to be assigned](../facts/fargate.md#fargate-public-subnet-image-pull-needs-public-ip)
  link: [route to the internet or a NAT gateway](../facts/fargate.md#fargate-public-subnet-image-pull-needs-public-ip)
fargate-requires-awsvpc-network-mode
  claim: ECS tasks on Fargate require the awsvpc network mode, which provides each task with an elastic network interface.
  scope: AWS Fargate tasks.
  link: [require the `awsvpc` network mode](../facts/fargate.md#fargate-requires-awsvpc-network-mode)
  link: [provides each task with an elastic network interface](../facts/fargate.md#fargate-requires-awsvpc-network-mode)
fargate-retirement-event-windows-precedence
  claim: As of 12/18/2025, Amazon ECS lets you configure Amazon EC2 event windows for your Fargate tasks, and when you configure an event window for your Fargate tasks, it takes precedence over your task retirement wait time configuration.
  scope: Fargate task retirement.
  link: [Amazon EC2 event windows for your Fargate tasks](../facts/fargate.md#fargate-retirement-event-windows-precedence)
  link: [takes precedence over your task retirement wait time](../facts/fargate.md#fargate-retirement-event-windows-precedence)
fargate-retirement-host-issue-no-notice
  claim: If there is an issue with an underlying Fargate host, Amazon ECS replaces the host without a task retirement notice.
  scope: AWS Fargate.
  link: [replaces the host without a task retirement notice](../facts/fargate.md#fargate-retirement-host-issue-no-notice)
  link: [an issue with an underlying Fargate host](../facts/fargate.md#fargate-retirement-host-issue-no-notice)
fargate-retirement-no-opt-out
  claim: You cannot opt out of Fargate task retirement: AWS applies the periodic platform updates automatically, and this is a benefit of Fargate compared to running workloads on EC2 instances.
  scope: AWS Fargate.
  link: [not something customers can opt-out of](../facts/fargate.md#fargate-retirement-no-opt-out)
  link: [automatically applied by AWS](../facts/fargate.md#fargate-retirement-no-opt-out)
fargate-retirement-notification-channels
  claim: Task retirement notifications are sent through the AWS Health Dashboard and by email to the registered email address.
  scope: Fargate task retirement.
  link: [sent through AWS Health Dashboard](../facts/fargate.md#fargate-retirement-notification-channels)
  link: [an email to the registered email address](../facts/fargate.md#fargate-retirement-notification-channels)
fargate-retirement-service-tasks-replaced-automatically
  claim: You do not need to take action for service tasks in response to Fargate task retirement because the ECS scheduler automatically replaces the tasks; for standalone tasks AWS stops the task on or after the retirement date and ECS does not launch a replacement.
  scope: Fargate task retirement; service tasks versus standalone tasks.
  link: [the Amazon ECS scheduler automatically replaces the tasks](../facts/fargate.md#fargate-retirement-service-tasks-replaced-automatically)
  link: [Amazon ECS doesn’t launch a replacement task](../facts/fargate.md#fargate-retirement-service-tasks-replaced-automatically)
fargate-retirement-wait-time-default
  claim: The Fargate task retirement schedule is based on the task retirement wait time, which has a default of 7 days; you can configure the wait period to 14 days if you need more time.
  scope: Fargate task retirement wait time; default; adjustable; can be configured to 14 days.
  link: [default of 7 days](../facts/fargate.md#fargate-retirement-wait-time-default)
  link: [wait period to 14 days](../facts/fargate.md#fargate-retirement-wait-time-default)
fargate-serverless-pay-as-you-go
  claim: Fargate is a serverless, pay-as-you-go compute engine; with it you do not need to manage servers, handle capacity planning, or isolate container workloads for security.
  scope: AWS Fargate with Amazon ECS.
  link: [serverless, pay-as-you-go compute engine](../facts/fargate.md#fargate-serverless-pay-as-you-go)
  link: [don't need to manage servers](../facts/fargate.md#fargate-serverless-pay-as-you-go)
  link: [handle capacity planning](../facts/fargate.md#fargate-serverless-pay-as-you-go)
fargate-service-load-balancer-types
  claim: ECS services on Fargate support the Application Load Balancer, Network Load Balancer and Gateway Load Balancer types; Application Load Balancers route HTTP/HTTPS (layer 7) traffic and Network Load Balancers route TCP or UDP (layer 4) traffic, but using a Network Load Balancer to route UDP traffic to Fargate tasks is only supported on platform version 1.4 or later.
  scope: ECS services on Fargate.
  link: [Gateway Load Balancer load balancer types](../facts/fargate.md#fargate-service-load-balancer-types)
  link: [route HTTP/HTTPS (or layer 7) traffic](../facts/fargate.md#fargate-service-load-balancer-types)
  link: [route TCP or UDP (or layer 4) traffic](../facts/fargate.md#fargate-service-load-balancer-types)
fargate-soci-lazy-loading-faster-start
  claim: ECS tasks on Fargate that use Linux platform version 1.4.0 can use Seekable OCI (SOCI) to start tasks faster; with SOCI the containers spend only a few seconds on the image pull while the image is downloaded in the background, which is called lazy loading.
  scope: AWS Fargate with Amazon ECS; Linux platform version 1.4.0.
  link: [Seekable OCI (SOCI) to help start tasks faster](../facts/fargate.md#fargate-soci-lazy-loading-faster-start)
  link: [This is called *lazy loading*](../facts/fargate.md#fargate-soci-lazy-loading-faster-start)
fargate-soci-linux-1-4-0-only-not-windows
  claim: Only Fargate tasks that run on Linux platform version 1.4.0 can use SOCI indexes, and tasks that run Windows containers on Fargate aren't supported.
  scope: AWS Fargate with Amazon ECS.
  link: [Only tasks that run on Linux platform version `1.4.0` can use SOCI indexes](../facts/fargate.md#fargate-soci-linux-1-4-0-only-not-windows)
  link: [Windows containers on Fargate aren't supported](../facts/fargate.md#fargate-soci-linux-1-4-0-only-not-windows)
fargate-soci-try-for-images-over-250-mib
  claim: AWS recommends trying SOCI lazy loading with container images greater than 250 MiB compressed in size; smaller images are less likely to show a reduction in load time.
  scope: AWS Fargate with Amazon ECS; minimum; recommendation.
  link: [greater than 250 MiB compressed in size](../facts/fargate.md#fargate-soci-try-for-images-over-250-mib)
  link: [less likely to see a reduction](../facts/fargate.md#fargate-soci-try-for-images-over-250-mib)
fargate-spot-burst-launch-rate-quota
  claim: In a single burst, an account can launch up to 100 Spot ECS tasks on Fargate in each of the other supported Regions; in the Regions the quota row lists, such as af-south-1, and in Regions introduced after May 20, 2025, the maximum is 25 Spot ECS tasks. The quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [100 Spot ECS tasks](../facts/fargate.md#fargate-spot-burst-launch-rate-quota)
  link: [25 Spot ECS tasks](../facts/fargate.md#fargate-spot-burst-launch-rate-quota)
fargate-spot-container-must-handle-sigterm
  claim: For a graceful exit on a Fargate Spot interruption, the container must receive and process the SIGTERM signal; failing to process it means the task receives SIGKILL after the configured stopTimeout, which may cause data loss or corruption.
  scope: Fargate Spot tasks.
  link: [must be received from within the container](../facts/fargate.md#fargate-spot-container-must-handle-sigterm)
  link: [may result in data loss or corruption](../facts/fargate.md#fargate-spot-container-must-handle-sigterm)
fargate-spot-interruption-tolerant-discount
  claim: Fargate Spot runs interruption tolerant ECS tasks on spare compute capacity at a rate discounted compared to the Fargate price; when AWS needs the capacity back, the tasks are interrupted with a two-minute warning.
  scope: Fargate Spot capacity provider; runs on spare compute capacity.
  link: [run interruption tolerant Amazon ECS tasks](../facts/fargate.md#fargate-spot-interruption-tolerant-discount)
  link: [discounted compared to the Fargate price](../facts/fargate.md#fargate-spot-interruption-tolerant-discount)
  link: [two-minute warning](../facts/fargate.md#fargate-spot-interruption-tolerant-discount)
fargate-spot-linux-only-pricing-page
  claim: Fargate Spot for Amazon ECS is currently only available for the Linux operating system and the x86 and ARM CPU architectures.
  scope: Fargate Spot for Amazon ECS; at the time of the snapshot.
  link: [currently only available for Linux Operating System](../facts/fargate.md#fargate-spot-linux-only-pricing-page)
  link: [x86 /ARM CPU Architecture](../facts/fargate.md#fargate-spot-linux-only-pricing-page)
fargate-spot-no-on-demand-replacement
  claim: During periods of extremely high demand, Fargate Spot capacity might be unavailable, which can delay Fargate Spot tasks; Amazon ECS services then retry launching tasks until the required capacity becomes available, and Fargate doesn't replace Spot capacity with on-demand capacity.
  scope: Fargate Spot capacity provider.
  link: [Fargate doesn't replace Spot capacity with on-demand capacity](../facts/fargate.md#fargate-spot-no-on-demand-replacement)
  link: [services retry launching tasks](../facts/fargate.md#fargate-spot-no-on-demand-replacement)
fargate-spot-single-task-service-interrupted
  claim: If you use Fargate Spot as part of a service, then at a Spot interruption the service scheduler receives the interruption signal and attempts to launch additional tasks on Fargate Spot if there's capacity available; a service with only one task is interrupted until capacity is available.
  scope: Fargate Spot capacity provider.
  link: [A service with only one task is interrupted](../facts/fargate.md#fargate-spot-single-task-service-interrupted)
  link: [attempts to launch additional tasks on Fargate Spot](../facts/fargate.md#fargate-spot-single-task-service-interrupted)
fargate-spot-sustained-launch-rate-quota
  claim: Fargate can launch up to 20 Spot ECS tasks per second (sustained rate) in each of the other supported Regions; in the Regions the quota row lists, such as af-south-1, and in Regions introduced after May 20, 2025, the maximum is 5 Spot ECS tasks per second. The quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [20 Spot ECS tasks per second](../facts/fargate.md#fargate-spot-sustained-launch-rate-quota)
  link: [5 Spot ECS tasks per second](../facts/fargate.md#fargate-spot-sustained-launch-rate-quota)
fargate-spot-two-minute-interruption-warning
  claim: Fargate Spot runs tasks on spare compute capacity. When AWS needs the capacity back, your tasks are interrupted with a two-minute warning.
  scope: per Fargate Spot task; fixed.
  link: [two-minute warning](../facts/fargate.md#fargate-spot-two-minute-interruption-warning)
fargate-spot-vcpu-quota
  claim: The default Fargate Spot quota is 6 vCPUs running concurrently in an account in the current Region. The quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [6 vCPUs](../facts/fargate.md#fargate-spot-vcpu-quota)
fargate-spot-warning-delivery-sigterm-eventbridge
  claim: When a Fargate Spot task is stopped by a Spot interruption, the two-minute warning is sent as a task state change event to Amazon EventBridge and as a SIGTERM signal to the running task.
  scope: Fargate Spot capacity provider.
  link: [task state change event to Amazon EventBridge](../facts/fargate.md#fargate-spot-warning-delivery-sigterm-eventbridge)
  link: [SIGTERM signal to the running task](../facts/fargate.md#fargate-spot-warning-delivery-sigterm-eventbridge)
fargate-storage-types-ebs-efs-bind
  claim: For ECS tasks hosted on Fargate, Amazon EBS volumes, Amazon EFS volumes for persistent storage, and bind mounts for ephemeral storage are supported.
  scope: ECS tasks on Fargate.
  link: [cost-effective, durable, high-performance block storage](../facts/fargate.md#fargate-storage-types-ebs-efs-bind)
  link: [Amazon EFS volumes for persistent storage](../facts/fargate.md#fargate-storage-types-ebs-efs-bind)
  link: [Bind mounts for ephemeral storage](../facts/fargate.md#fargate-storage-types-ebs-efs-bind)
fargate-target-group-ip-target-type
  claim: For an ECS service on Fargate you must choose ip as the target type of the target group, not instance, because awsvpc tasks are associated with an elastic network interface and not an EC2 instance.
  scope: target groups of ECS services on Fargate.
  link: [you must choose `ip` as the target type](../facts/fargate.md#fargate-target-group-ip-target-type)
  link: [associated with an elastic network interface](../facts/fargate.md#fargate-target-group-ip-target-type)
fargate-task-containers-share-resources
  claim: Containers in the same Fargate task always run on the same host, share compute resources and the task's ephemeral storage, and can talk to each other over localhost.
  scope: containers within one Fargate task.
  link: [always run on the same host](../facts/fargate.md#fargate-task-containers-share-resources)
  link: [can inter-communicate over localhost](../facts/fargate.md#fargate-task-containers-share-resources)
fargate-task-has-route-to-internet-to-pull
  claim: For a task on Fargate to pull a container image, the task must have a route to the internet: with a public subnet you can assign a public IP address to the task ENI, and with a private subnet the subnet can have a NAT gateway attached. When the container images are hosted in Amazon ECR, you can configure Amazon ECR to use an interface VPC endpoint, and the image pull occurs over the task's private IPv4 address.
  scope: Fargate tasks.
  link: [must have a route to the internet](../facts/fargate.md#fargate-task-has-route-to-internet-to-pull)
  link: [the subnet can have a NAT gateway attached](../facts/fargate.md#fargate-task-has-route-to-internet-to-pull)
fargate-task-isolation-boundary
  claim: Each Fargate task has its own isolation boundary and does not share the underlying kernel, CPU resources, memory resources, or elastic network interface with another task.
  scope: each Fargate task.
  link: [its own isolation boundary](../facts/fargate.md#fargate-task-isolation-boundary)
  link: [does not share the underlying kernel](../facts/fargate.md#fargate-task-isolation-boundary)
fargate-task-retirement-aws-maintains-infrastructure
  claim: AWS is responsible for maintaining the infrastructure for Fargate; when AWS replaces a platform version revision this is called task retirement, AWS sends a task retirement notification, and when a revision is retired all tasks running on that revision are stopped.
  scope: AWS Fargate.
  link: [AWS is responsible for maintaining the underlying infrastructure](../facts/fargate.md#fargate-task-retirement-aws-maintains-infrastructure)
  link: [This is known as task retirement](../facts/fargate.md#fargate-task-retirement-aws-maintains-infrastructure)
  link: [all tasks running on that revision are stopped](../facts/fargate.md#fargate-task-retirement-aws-maintains-infrastructure)
fargate-task-size-1-vcpu-linux-windows
  claim: A Fargate task with 1024 CPU units (1 vCPU) can have 2 GB to 8 GB of memory in 1 GB steps and runs on Linux or Windows.
  scope: per Fargate task definition (task level); fixed; not adjustable; Linux or Windows.
  link: [1024 (1 vCPU)](../facts/fargate.md#fargate-task-size-1-vcpu-linux-windows)
  link: [2 GB, 3 GB, 4 GB, 5 GB, 6 GB, 7 GB, 8 GB](../facts/fargate.md#fargate-task-size-1-vcpu-linux-windows)
fargate-task-size-16-vcpu
  claim: A Fargate task with 16384 CPU units (16 vCPU) can have between 32 GB and 120 GB of memory in 8 GB increments. It runs on Linux only and needs Linux platform 1.4.0 or later.
  scope: per Fargate task definition (task level); fixed; not adjustable; Linux platform 1.4.0 or later.
  link: [16384 (16 vCPU)](../facts/fargate.md#fargate-task-size-16-vcpu)
  link: [Between 32 GB and 120 GB](../facts/fargate.md#fargate-task-size-16-vcpu)
fargate-task-size-4-vcpu-linux-windows
  claim: A Fargate task with 4096 CPU units (4 vCPU) can have between 8 GB and 30 GB of memory in 1 GB increments and runs on Linux or Windows.
  scope: per Fargate task definition (task level); fixed; not adjustable; Linux or Windows.
  link: [4096 (4 vCPU)](../facts/fargate.md#fargate-task-size-4-vcpu-linux-windows)
  link: [Between 8 GB and 30 GB](../facts/fargate.md#fargate-task-size-4-vcpu-linux-windows)
fargate-task-size-largest-32-vcpu
  claim: On Amazon ECS, the Fargate task CPU value 32768 (32 vCPU) supports 60 GB, 120 GB, 244 GB of memory, runs on Linux, and requires Linux platform 1.4.0 or later.
  scope: per Fargate task definition (task level); Linux platform 1.4.0 or later.
  link: [32768 (32 vCPU)](../facts/fargate.md#fargate-task-size-largest-32-vcpu)
  link: [60 GB, 120 GB, 244 GB](../facts/fargate.md#fargate-task-size-largest-32-vcpu)
fargate-task-size-smallest
  claim: On Amazon ECS, the Fargate task CPU value 256 (.25 vCPU) supports 512 MiB, 1 GB, 2 GB of memory and runs on Linux.
  scope: per Fargate task definition (task level).
  link: [256 (.25 vCPU)](../facts/fargate.md#fargate-task-size-smallest)
  link: [512 MiB, 1 GB, 2 GB](../facts/fargate.md#fargate-task-size-smallest)
fargate-vs-lambda-lambda-best-for-event-driven
  claim: The AWS decision guide says Lambda functions are best suited for event-driven applications; if your project involves event-driven tasks, unpredictable workloads, or wait-heavy orchestration workflows consider Lambda, and if you need to run containerized applications with specific resource needs or persistent processes Fargate is worth considering.
  scope: AWS Fargate compared with AWS Lambda.
  link: [event-driven tasks, unpredictable workloads, or wait-heavy orchestration workflows](../facts/fargate.md#fargate-vs-lambda-lambda-best-for-event-driven)
  link: [specific resource needs or persistent processes](../facts/fargate.md#fargate-vs-lambda-lambda-best-for-event-driven)
fargate-vs-lambda-shared-serverless-benefits
  claim: Both Lambda and Fargate abstract away server management, which reduces the need for patching, maintenance, and capacity planning, and both are pay-per-use.
  scope: AWS Fargate and AWS Lambda.
  link: [Both Lambda and Fargate abstract away server management](../facts/fargate.md#fargate-vs-lambda-shared-serverless-benefits)
  link: [the need for patching, maintenance, and capacity planning](../facts/fargate.md#fargate-vs-lambda-shared-serverless-benefits)
fargate-vulnerable-revision-tasks-retired
  claim: If a security issue affects an existing Fargate platform version, AWS creates a new patched revision of the platform version and retires the tasks running on the vulnerable revision.
  scope: AWS Fargate.
  link: [a new patched revision of the platform version](../facts/fargate.md#fargate-vulnerable-revision-tasks-retired)
  link: [retires tasks running on the vulnerable revision](../facts/fargate.md#fargate-vulnerable-revision-tasks-retired)
fargate-whitepaper-own-kernel-for-ecs-and-eks
  claim: The AWS container decision guide says you can use Fargate with both Amazon ECS and Amazon EKS, and the Containers on AWS whitepaper says Fargate runs each task or pod in its own kernel, giving it its own isolated compute environment.
  scope: AWS Fargate.
  link: [Fargate with both Amazon ECS and Amazon EKS](../facts/fargate.md#fargate-whitepaper-own-kernel-for-ecs-and-eks)
  link: [each task or pod in its own kernel](../facts/fargate.md#fargate-whitepaper-own-kernel-for-ecs-and-eks)
fargate-windows-containers-x86-64-only
  claim: When you run Windows containers on AWS Fargate, you must have the X86_64 CPU architecture; Linux containers on Fargate can use X86_64 or the ARM64 architecture for ARM-based applications.
  scope: AWS Fargate tasks.
  link: [When you run Windows containers on AWS Fargate, you must have the X86\_64 CPU architecture](../facts/fargate.md#fargate-windows-containers-x86-64-only)
  link: [you can use the X86\_64 CPU architecture, or the ARM64 architecture](../facts/fargate.md#fargate-windows-containers-x86-64-only)
