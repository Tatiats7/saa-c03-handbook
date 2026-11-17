---
id: "21"
slug: s3
title: Amazon S3
file: fast
tier: deep
xl: true
domains: [1, 2, 3, 4]
tasks: ["3.1", "4.1", "1.3", "2.2", "1.1"]
services: [s3, s3-glacier]
minutes: {fast: 20, pass: 78, full: 178}
status: ready
updated: 2026-10-12
---

# Amazon S3

## Predict (2 min)
<!-- section: role=predict; route=fast; minutes=2 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** Amazon S3 stores every object in S3 Standard in several Availability Zones. An engineer deletes a recording by mistake. The bucket has no versioning and no backup. Can AWS bring the recording back? <!-- gist-trap -->

**Predict 2.** Customers start to open old recordings again. Can a lifecycle rule move the recordings from an archive storage class back to S3 Standard?

**Predict 3.** A bucket is private. Can a customer's browser upload a file straight into the bucket, without passing through your application server?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

In AWS CloudShell, read the **Block Public Access** settings of your account and the default encryption of one bucket that you own. The task creates nothing.

<!-- task:start id=s3-t01 -->

Look

**It kills the belief.** "A new bucket is public and unencrypted until you change its settings."

> **Cost:** $0.

**Permissions.** `sts:GetCallerIdentity`, `s3:GetAccountPublicAccessBlock`, `s3:ListAllMyBuckets`, `s3:GetBucketPublicAccessBlock`, `s3:GetEncryptionConfiguration`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. Keep your account ID in the variable ACCOUNT_ID for the next step.

   ```bash
   ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
   ```

   Expect: No output. The variable ACCOUNT_ID now holds your account ID.

2. Read the Block Public Access settings of the whole account. S3 combines them with the settings of each bucket and applies the most restrictive combination.

   ```bash
   aws s3control get-public-access-block --account-id $ACCOUNT_ID
   ```

   Expect: Either the four settings BlockPublicAcls, IgnorePublicAcls, BlockPublicPolicy and RestrictPublicBuckets with true or false, or an error. An error that no configuration was found means the account has no account-level setting.

3. List the names of your buckets. If the list is empty, stop here: the last two steps need a bucket.

   ```bash
   aws s3api list-buckets --query "Buckets[].Name"
   ```

   Expect: A list of bucket names, or an empty list.

4. Pick one bucket from the list as <BUCKET>. Read the Block Public Access settings of that bucket.

   ```bash
   aws s3api get-public-access-block --bucket <BUCKET>
   ```

   Expect: The same four settings, each true for a bucket that kept its defaults. An error that no configuration was found means the bucket has no setting of its own; the account settings of step 2 still apply.

5. Read the default encryption of the same bucket.

   ```bash
   aws s3api get-bucket-encryption --bucket <BUCKET> --query "ServerSideEncryptionConfiguration.Rules[].ApplyServerSideEncryptionByDefault.SSEAlgorithm"
   ```

   Expect: ["AES256"], the name of SSE-S3, for a bucket that kept its defaults. A bucket that uses SSE-KMS shows aws:kms instead. Every bucket shows a value, because every bucket has default encryption.

**Label.** checked against docs, not run in a real account. Checked 2026-10-13.

<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** Amazon S3 is an [object storage service](../facts/s3.md#s3-object-storage-definition) that keeps objects in buckets. An object [can be accessed only if you explicitly grant](../facts/s3.md#s3-private-by-default) access.

**The problem it solves.** Data grows and has to survive hardware failures. Amazon S3 stores an [unlimited](../facts/s3.md#s3-faq-storage-unlimited) amount. It is designed for [11 nines](../facts/s3.md#s3-faq-durability-11-nines) of **durability** (dyoor-uh-BIL-ih-tee): how unlikely it is that stored data is lost.

**Predict the picture.** Does the recording pass through the application server?

<details>
<summary>Show the picture</summary>

![A sequence with three actors: a browser, an application server and Amazon S3. The browser asks the server for a link, the server signs a presigned URL and returns it, the browser sends the recording directly to Amazon S3, and Amazon S3 checks the URL and stores the object.](../diagrams/svg/s3-hero.svg)

**Figure.** The recording travels from the browser straight to the private bucket, not through the application server.

1. The browser asks the application server for a link to upload one recording.
2. The application server signs a presigned URL for that object with its own credentials.
3. The server returns the URL, which works until its expiry time or until the server's credentials expire, [whichever occurs first](../facts/s3.md#s3-presigned-url-expires-with-temporary-credentials).
4. The browser sends the recording directly to Amazon S3 with a PUT request to that URL.
5. Amazon S3 checks the signature and the signer's permission, then stores the object encrypted.

</details>

> **Startup example:** Callvale stores recordings in a public bucket so that the browser can play them. Recordings contain personal data and must be private. Customers must still upload and play recordings from the browser. Callvale keeps recordings for 7 years, and 2% are opened after 90 days.

## Words that go together (1 min)
<!-- section: role=words; route=fast; minutes=1 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| bucket | **upload** an object to a bucket | The named store that holds objects | a prefix in an object key |
| object | the object **key** | Data stored with its key and metadata | a file in a file system |
| storage class | **transition** an object to a storage class | The price and access level of one object | an EBS volume type |
| lifecycle rule (LYFE-sy-kul) | **add** a lifecycle rule to a bucket | Moves or deletes objects at a set age | a replication rule |
| versioning | **restore** an earlier version | Keeps earlier versions of each object | **Object Lock**, which blocks deletes |
| presigned URL (pree-SYND) | **generate** a presigned URL | A link with time-limited access to one object | a CloudFront signed URL |
| durability (dyoor-uh-BIL-ih-tee) | **designed** for durability | How unlikely it is that stored data is lost | availability: you can reach the data now |
| encryption at rest | **encrypt** data at rest and in transit | Protecting stored data | encryption in transit |

## Choose it or not (4 min)
<!-- section: role=choose; route=fast; minutes=4 -->

### Amazon S3 or Amazon EBS or Amazon EFS

<!-- table: compare -->
| Question | Amazon S3 | Amazon EBS | File storage (Amazon EFS, Amazon FSx) |
|---|---|---|---|
| How is the data reached? | Object storage, through [an application programming interface (API) over the internet](../facts/s3.md#s3-object-storage-api-read-heavy) | Block storage, [direct-attached to a compute instance](../facts/s3.md#s3-vs-block-storage-direct-attached) | File storage, through [industry-standard protocols like NFS and SMB](../facts/s3.md#s3-vs-file-storage-shared-mount) |
| What does it fit? | [Read-heavy workloads](../facts/s3.md#s3-object-storage-api-read-heavy), with [unlimited](../facts/s3.md#s3-faq-storage-unlimited) total storage | Applications that need [fast and consistent I/O operations](../facts/s3.md#s3-vs-block-storage-direct-attached) | [Shared data across multiple compute instances](../facts/s3.md#s3-vs-file-storage-shared-mount) |

**Deciding question:** Does the application need objects over an API, a disk for one instance, or files that many instances share? <!-- xref: 22 EBS and 23 EFS and FSx (block and file storage) -->

### S3 Standard-IA or S3 One Zone-IA or S3 Intelligent-Tiering

<!-- table: compare -->
| Question | S3 Standard-IA | S3 One Zone-IA | S3 Intelligent-Tiering |
|---|---|---|---|
| Access pattern? | About [once a month](../facts/s3.md#s3-class-standard-ia-profile) | Rare reads, and you can [re-create the data if the Availability Zone fails](../facts/s3.md#s3-standard-ia-vs-one-zone-ia-use) | [Unknown, changing, or unpredictable access patterns](../facts/s3.md#s3-intelligent-tiering-ideal-for-unknown-access) |
| Survives the loss of an Availability Zone? | Yes: use it for the [primary or only copy of data](../facts/s3.md#s3-standard-ia-vs-one-zone-ia-use) | No: it is [not resilient to the physical loss](../facts/s3.md#s3-one-zone-ia-az-loss) of its zone | Yes, unlike One Zone-IA ([not resilient to the loss of availability](../facts/s3.md#s3-faq-one-zone-ia-not-resilient)) |
| **Retrieval fee**? | Yes: S3 [charges a retrieval fee for these objects](../facts/s3.md#s3-ia-classes-millisecond-access-retrieval-fee) | Yes, as for S3 Standard-IA | No: [no retrieval charges](../facts/s3.md#s3-faq-it-no-retrieval-fees) |
| **Minimum storage duration**? | [30 days](../facts/s3.md#s3-ia-min-duration-charge) | [30 days](../facts/s3.md#s3-class-one-zone-ia-profile) | None: [no minimum storage duration](../facts/s3.md#s3-faq-it-no-min-duration) |

**Deciding question:** Do you know how often the data is read, and could you re-create the data if one Availability Zone were lost?

### S3 Glacier Instant Retrieval or Flexible Retrieval or Deep Archive

<!-- table: compare -->
| Question | S3 Glacier Instant Retrieval | S3 Glacier Flexible Retrieval | S3 Glacier Deep Archive |
|---|---|---|---|
| How long does a read take? | [Milliseconds](../facts/s3.md#s3-class-glacier-ir-compare-row) | [Minutes to 12 hours](../facts/s3.md#s3-class-glacier-flexible-compare-row) | Standard: [within 12 hours](../facts/s3.md#s3-archive-retrieval-times-deep) |
| Needs a **restore request** first? | No: you [do not need to issue a Restore request](../facts/s3.md#s3-faq-instant-retrieval-no-restore) | Yes: first [retrieve data using the RestoreObject REST API](../facts/s3.md#s3-archive-restore-needed-flexible-deep) | Yes, as for Flexible Retrieval |
| Read about how often? | [Quarterly](../facts/s3.md#s3-class-glacier-ir-compare-row) | [Semi-annually](../facts/s3.md#s3-class-glacier-flexible-compare-row) | [Annually](../facts/s3.md#s3-class-deep-archive-compare-row) |
| Minimum storage duration? | [90 days](../facts/s3.md#s3-class-glacier-ir-compare-row) | [90 days](../facts/s3.md#s3-class-glacier-flexible-compare-row) | [180 days](../facts/s3.md#s3-class-deep-archive-compare-row) |

**Deciding question:** How fast must the first byte come back, and how often is the data read?

### Versioning with multi-factor authentication delete or Object Lock

<!-- table: compare -->
| Question | Versioning with multi-factor authentication (MFA) delete | Object Lock governance mode | Object Lock compliance mode |
|---|---|---|---|
| Who can still delete a protected version? | The bucket owner, with [two forms of authentication](../facts/s3.md#s3-mfa-delete-protected-operations) | Users who have [s3:BypassGovernanceRetention](../facts/s3.md#s3-object-lock-governance-mode) | No user can remove the lock, [including the root account](../facts/s3.md#s3-faq-object-lock-modes) |
| Can the protection end early? | There is no **retention period** | Yes, for users who have [s3:BypassGovernanceRetention](../facts/s3.md#s3-object-lock-governance-mode) | No: the only way is to [delete the associated AWS account](../facts/s3.md#s3-object-lock-compliance-mode) |

**Deciding question:** Must even an administrator or the root user be unable to delete the data until a date?

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "write once, read many (WORM), even for the root user" | S3 Object Lock in compliance mode | the lock holds for every user, [including the root account](../facts/s3.md#s3-faq-object-lock-modes) | privileged users must unlock it: governance mode |
| "unknown or changing access patterns, MOST cost-effective" | S3 Intelligent-Tiering | [unknown, changing, or unpredictable access patterns](../facts/s3.md#s3-intelligent-tiering-ideal-for-unknown-access) | objects are under [128 KB](../facts/s3.md#s3-int-tiering-small-objects): they are never moved |
| "infrequently accessed data that can be re-created" | S3 One Zone-IA | its data sits in [1 Availability Zone](../facts/s3.md#s3-class-one-zone-ia-profile) | it is the only copy: S3 Standard-IA |
| "archive for years, retrieval within 12 hours, lowest cost" | S3 Glacier Deep Archive | [the lowest cost storage in the cloud](../facts/s3.md#s3-class-deep-archive-lowest-cost-twelve-hours) | some restores must finish in minutes: Flexible Retrieval |
| "users without AWS credentials upload for a limited time" | presigned URLs | it gives [time-limited access](../facts/s3.md#s3-presigned-url-time-limited-creator-credentials) | files are served through CloudFront: CloudFront signed URLs or cookies |
| "users around the world upload large files to one bucket, slowly" | S3 Transfer Acceleration | users [upload to a centralized general purpose bucket](../facts/s3.md#s3-transfer-acceleration-when-to-use) | users around the world download the same files: CloudFront |
| "copy objects automatically to another Region" | S3 Cross-Region Replication | [automatic, asynchronous copying of objects](../facts/s3.md#s3-crr-for-compliance-distance-requirements) | the objects already exist: S3 Batch Replication |
| "AWS must never store the encryption keys" | server-side encryption with customer-provided keys (SSE-C) | with SSE-C, [you retain control of the encryption keys](../facts/s3.md#s3-faq-sse-c-keys) | data is encrypted before it leaves the data center: client-side encryption |

### Traps

- **Wrong belief:** Eleven nines of durability make backups unnecessary. **Truth:** Durability [does not protect against accidental or malicious deletes](../facts/s3.md#s3-faq-durability-not-delete-protection). Use versioning, replication or Object Lock. <!-- trap: s3-trap-durability-is-backup -->
- **Wrong belief:** S3 One Zone-IA is fine for the only copy of data. **Truth:** S3 One Zone-IA is [not resilient to the physical loss](../facts/s3.md#s3-one-zone-ia-az-loss) of its Availability Zone. <!-- trap: s3-trap-one-zone-for-only-copy -->
- **Wrong belief:** A GET or an Expedited retrieval reads any S3 Glacier object in minutes. **Truth:** In Flexible Retrieval and Deep Archive, you must first [restore a temporary copy of it](../facts/s3.md#s3-archive-restore-temporary-copy). From Deep Archive, Expedited retrieval is [not available](../facts/s3.md#s3-archive-retrieval-times-deep). <!-- trap: s3-trap-glacier-read-directly -->
- **Wrong belief:** With versioning on, nobody can delete data for good. **Truth:** If a DELETE names a version ID, [that object version is permanently deleted](../facts/s3.md#s3-versioning-delete-with-version-id-permanent). <!-- trap: s3-trap-versioning-stops-deletes -->
- **Wrong belief:** Replication also copies the objects already in the bucket. **Truth:** Live replication [replicates newly uploaded objects as they are written](../facts/s3.md#s3-batch-replication-for-existing-objects). Existing objects need S3 Batch Replication. <!-- trap: s3-trap-replication-copies-existing -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2025-12-02) The maximum size of one object.<br>
> **Old:** [5 TB](../facts/s3.md#s3-object-max-size).<br>
> **Now:** [50 TB](../facts/s3.md#s3-object-max-size).<br>
> **The exam probably expects:** older questions can say [5 TB](../facts/s3.md#s3-object-max-size). One PUT still uploads [5 GB](../facts/s3.md#s3-single-put-max) at most, so large objects need **multipart upload**.<br>
> **Status:** examinable.

> **Changed recently:** (2023-04-27) Block Public Access and access control lists (ACLs) of new buckets.<br>
> **Old:** until [2023-04-27](../facts/s3.md#s3-change-bpa-acls-default-new-buckets-2023-04), API and AWS CloudFormation buckets had Block Public Access off and ACLs on.<br>
> **Now:** [Block Public Access turned on by default](../facts/s3.md#s3-change-bpa-acls-default-new-buckets-2023-04), and [ACLs are disabled by default](../facts/s3.md#s3-change-bpa-acls-default-new-buckets-2023-04).<br>
> **The exam probably expects:** older questions grant access with ACLs. Prefer a **bucket policy**.<br>
> **Status:** examinable.

> **Changed recently:** (2026-04) SSE-C on new buckets.<br>
> **Old:** a bucket accepted SSE-C requests without a setting.<br>
> **Now:** [SSE-C is disabled by default](../facts/s3.md#s3-sse-c-disabled-by-default-2026-04) for new general purpose buckets.<br>
> **The exam probably expects:** SSE-C when keys stay outside AWS. In a new bucket, turn SSE-C on first.<br>
> **Status:** examinable.

## Check (2 min)
<!-- section: role=check; route=fast; minutes=2 -->

**Check 1.** Versioning is on. A user deletes report.pdf without naming a version. Is the data gone?

<details>
<summary>Answer</summary>

No. Amazon S3 adds a **delete marker**, which [becomes the current (or newest) version](../facts/s3.md#s3-delete-marker-soft-delete).

**Predict 1:** No. Without versioning or a backup, deleted data [cannot be recovered by AWS](../facts/s3.md#s3-faq-delete-is-immediate).

</details>

**Check 2.** An object in S3 Glacier Deep Archive must move to S3 Standard. What do you do?

<details>
<summary>Answer</summary>

Restore, then copy into S3 Standard: you [make a temporary copy of the object first](../facts/s3.md#s3-lifecycle-no-transition-out-of-archive).

**Predict 2:** No. Transitions follow [a waterfall model for transitioning between storage classes](../facts/s3.md#s3-lifecycle-transition-waterfall), toward colder classes.

</details>

**Check 3.** An IAM role cannot read customer-42/call.wav. Can the role sign a working presigned URL for that object?

<details>
<summary>Answer</summary>

No. A presigned URL is [limited by the permissions of the user](../facts/s3.md#s3-presigned-url-creator-needs-permission) who signed it, so the download fails.

**Predict 3:** Yes. A presigned URL allows [an upload without requiring another party](../facts/s3.md#s3-presigned-url-upload-no-credentials-needed) to have AWS credentials.

</details>

## Recap from memory (1 min)
<!-- section: role=recap; route=fast; minutes=1 -->

**Recap 1.** Which storage class fits data with an unknown or changing access pattern?

<details>
<summary>Answer</summary>

S3 Intelligent-Tiering, for [unknown, changing, or unpredictable access patterns](../facts/s3.md#s3-intelligent-tiering-ideal-for-unknown-access).

</details>

**Recap 2.** What does a presigned URL let a browser do, and until when?

<details>
<summary>Answer</summary>

Upload or read one object directly in Amazon S3, with [time-limited access](../facts/s3.md#s3-presigned-url-time-limited-creator-credentials) that ends at the expiry time.

</details>

**Recap 3.** Which Object Lock mode stops even the root user from removing the lock?

<details>
<summary>Answer</summary>

Compliance mode: no user can remove the lock, [including the root account](../facts/s3.md#s3-faq-object-lock-modes).

</details>
