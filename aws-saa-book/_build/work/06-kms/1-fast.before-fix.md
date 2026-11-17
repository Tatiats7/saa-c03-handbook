---
id: "06"
slug: kms
title: KMS and CloudHSM
file: fast
tier: medium
domains: [1]
tasks: ["1.3"]
services: [kms, cloudhsm]
minutes: {fast: 12, pass: 49, full: 105}
status: draft
updated: 2026-10-12
---

# KMS and CloudHSM

## Predict (1 min)
<!-- section: role=predict; route=fast; minutes=1 -->

**Predict 1.** An engineer's IAM policy allows every Amazon S3 action. The bucket encrypts its objects with a **customer managed key**. Can the engineer download them? <!-- gist-trap -->

**Predict 2.** AWS Key Management Service (AWS KMS) rotates the **key material** of a key. Can AWS KMS still decrypt data encrypted before the rotation?

## In one breath (2 min)
<!-- section: role=breath; route=fast; minutes=2 -->

> **Say it:** AWS KMS lets you [create and control the keys](../facts/kms.md#kms-what-it-is-create-control-keys) that protect your data. A **data key** encrypts the data.

**The problem it solves.** Stored data needs keys whose use you control and log.

**Predict the picture.** Where does the **KMS key** go when an application encrypts a file?

<details>
<summary>Show the picture</summary>

![Three actors: an application, AWS KMS and a data store. The application gets a data key from AWS KMS, stores encrypted data with the encrypted key, and later asks AWS KMS to decrypt the key.](../diagrams/svg/kms-hero.svg)

**Figure.** KMS keys [never leave the service unencrypted](../facts/kms.md#kms-keys-never-leave-unencrypted), and the application encrypts its data with a data key.

1. The application asks AWS KMS for a data key under a KMS key.
2. AWS KMS returns the data key in plaintext and [encrypted under the KMS key](../facts/kms.md#kms-generatedatakey-returns-plaintext-and-encrypted).
3. The application encrypts the data and stores the encrypted data key with it.
4. To read, the application sends the encrypted data key to AWS KMS and gets the plaintext key back.

</details>

> **Startup example:** Ostell Bank asks who controls its recording keys. Callvale uses keys that AWS manages. The bank wants Callvale to control the key and log each use.

## Words that go together (1 min)
<!-- section: role=words; route=fast; minutes=1 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| KMS key | **encrypt** with a KMS key | A key in AWS KMS that protects data or keys | access key |
| customer managed key | **create** a customer managed key | A KMS key that you create and manage | **AWS managed key** |
| key policy | a key policy **allows** a principal | Says who can use a KMS key | IAM policy |
| data key | **generate** a data key | A key that encrypts data outside AWS KMS | KMS key |
| encryption at rest | **encrypted** at rest | Protecting stored data | encryption in transit |

## Choose it or not (2 min)
<!-- section: role=choose; route=fast; minutes=2 -->

### AWS owned or AWS managed or customer managed key

<!-- table: compare -->
| Question | **AWS owned key** | AWS managed key | Customer managed key |
|---|---|---|---|
| Who controls the key policy? | The AWS service | [Controlled by service; viewable by customer](../facts/kms.md#kms-key-type-key-policy-control) | [Exclusively controlled by the customer](../facts/kms.md#kms-key-type-key-policy-control) |
| Where can you see each use? | [Not viewable by the customer](../facts/kms.md#kms-key-type-logging-owned-not-viewable) | [CloudTrail customer trail or event data store](../facts/kms.md#kms-key-type-logging-owned-not-viewable) | [CloudTrail customer trail or event data store](../facts/kms.md#kms-key-type-logging-owned-not-viewable) |
| Monthly fee? | [No fees](../facts/kms.md#kms-key-type-row-aws-owned) | [No monthly fee](../facts/kms.md#kms-key-type-row-aws-managed) | [Monthly fee (pro-rated hourly)](../facts/kms.md#kms-key-type-row-customer-managed) |

**Deciding question:** Must you control or audit the use of the key?

### AWS KMS or AWS CloudHSM

<!-- table: compare -->
| Question | AWS KMS | AWS CloudHSM |
|---|---|---|
| Who runs the hardware security modules (HSMs)? | AWS | You: [operate your own HSMs](../facts/cloudhsm.md#cloudhsm-consider-kms-if-no-hsm-ops) in a [single-tenant HSM cluster](../facts/cloudhsm.md#cloudhsm-vs-kms-faq-single-tenant-vpc-exclusive) |
| Federal Information Processing Standards (FIPS) level? | [FIPS 140-3 Security Level 3](../facts/kms.md#kms-hsm-fips-140-3-level-3) | [FIPS 140-3 Level 3](../facts/cloudhsm.md#cloudhsm-hsm2m-fips-140-3-level-3) on hsm2m.medium |
| Standard APIs such as JCE? | [no native integration](../facts/kms.md#kms-faq-no-native-openssl-jce-cng) | [PKCS#11, Java JCE, or Microsoft CNG](../facts/cloudhsm.md#cloudhsm-vs-kms-faq-single-tenant-vpc-exclusive) |

**Deciding question:** Do you need single-tenant HSMs that you control, or PKCS#11, JCE or CNG?

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "control who can use the key and audit every use" | customer managed key | [you have full control over these KMS keys](../facts/kms.md#kms-customer-managed-key-full-control) | no audit needed: AWS owned key |
| "single-tenant HSM under the company's exclusive control" | AWS CloudHSM | [single-tenant HSM cluster](../facts/cloudhsm.md#cloudhsm-vs-kms-faq-single-tenant-vpc-exclusive) | only [FIPS 140-3 Security Level 3](../facts/kms.md#kms-hsm-fips-140-3-level-3) is needed: AWS KMS |
| "rotate the key every year without changing the application" | automatic rotation | the key stays [the same logical resource](../facts/kms.md#kms-rotation-same-logical-key-transparent) | asymmetric or HMAC key: a new key |
| "decrypt in the recovery Region without a cross-Region call" | **multi-Region key** | [the same key material and key ID](../facts/kms.md#kms-mrk-same-material-no-cross-region-call) | data must stay in one Region: single-Region keys |
| "encrypt files larger than 4 KB with a KMS key" | **envelope encryption** | Encrypt takes [up to 4 KB](../facts/kms.md#kms-encrypt-max-plaintext-4096-bytes) | an AWS service stores it: server-side encryption |
| "an application in another account must decrypt the data" | key policy and IAM policy | [permission in the key policy](../facts/kms.md#kms-cross-account-key-policy-and-iam-policy) and an IAM policy | another Region: [the KMS key in the destination AWS Region](../facts/kms.md#kms-cross-region-snapshot-copy-destination-key) |

### Traps

- **Wrong belief:** Full S3 permissions download objects encrypted with a KMS key. **Truth:** A download also needs [kms:Decrypt permissions for the key](../facts/kms.md#kms-s3-sse-kms-put-get-permissions). <!-- trap: kms-trap-s3-permission-reads-encrypted -->
- **Wrong belief:** After a rotation, you must re-encrypt old data. **Truth:** AWS KMS [keeps previous versions of keys](../facts/kms.md#kms-faq-auto-rotation-no-reencrypt) <!-- trap: kms-trap-rotation-reencrypts-data -->
- **Wrong belief:** FIPS Level 3 needs AWS CloudHSM. **Truth:** AWS KMS uses HSMs validated at [FIPS 140-3 Security Level 3](../facts/kms.md#kms-hsm-fips-140-3-level-3). <!-- trap: kms-trap-fips-needs-cloudhsm -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2023-05-24) The HSM level of AWS KMS.<br>
> **Old:** [FIPS 140-2 overall Security Level 2](../facts/kms.md#kms-change-hsm-fips-140-2-level-3-2023-05).<br>
> **Now:** [FIPS 140-3 Security Level 3](../facts/kms.md#kms-change-hsm-fips-140-2-level-3-2023-05).<br>
> **The exam probably expects:** Level 3 alone is no longer a reason for CloudHSM.<br>
> **Status:** examinable.

> **Changed recently:** (2022-05) Rotation period of AWS managed keys.<br>
> **Old:** [every three years (approximately 1,095 days)](../facts/kms.md#kms-aws-managed-keys-rotate-every-year).<br>
> **Now:** [every year (approximately 365 days)](../facts/kms.md#kms-aws-managed-keys-rotate-every-year).<br>
> **The exam probably expects:** the new value.<br>
> **Status:** examinable.

## Check (1 min)
<!-- section: role=check; route=fast; minutes=1 -->

**Check 1.** Now the engineer's IAM policy also allows kms:Decrypt. The key has the default key policy. Can the engineer download them?

<details>
<summary>Answer</summary>

Yes. The default key policy lets the account [use IAM policies to allow access](../facts/kms.md#kms-default-key-policy-enables-iam).

**Predict 1:** No: a download also needs [kms:Decrypt permissions for the key](../facts/kms.md#kms-s3-sse-kms-put-get-permissions).

</details>

**Check 2.** A team turns on automatic rotation. Must its applications change the key ID?

<details>
<summary>Answer</summary>

No. Rotation [changes only the current key material](../facts/kms.md#kms-rotation-same-logical-key-transparent).

**Predict 2:** Yes: AWS KMS [keeps previous versions of keys](../facts/kms.md#kms-faq-auto-rotation-no-reencrypt).

</details>

## Recap from memory (1 min)
<!-- section: role=recap; route=fast; minutes=1 -->

**Recap 1.** Which two permissions does a role need to download a KMS-encrypted object?

<details>
<summary>Answer</summary>

S3 permission to read the object, and [kms:Decrypt permissions for the key](../facts/kms.md#kms-s3-sse-kms-put-get-permissions).

</details>

**Recap 2.** Which key type lets you control its key policy and audit each use?

<details>
<summary>Answer</summary>

A customer managed key.

</details>

**Recap 3.** What is the deciding question between AWS KMS and AWS CloudHSM?

<details>
<summary>Answer</summary>

Do you need single-tenant HSMs that you control, or PKCS#11, JCE or CNG?

</details>
