---
id: "09"
slug: detection
title: GuardDuty, Inspector, Macie, Security Hub, Detective, Config and Artifact
file: fast
tier: medium
domains: [1]
tasks: ["1.2", "1.3"]
services: [guardduty, inspector, macie, security-hub, detective, config, artifact]
minutes: {fast: 14, pass: 56, full: 99}
status: ready
updated: 2026-10-12
---

# GuardDuty, Inspector, Macie, Security Hub, Detective, Config and Artifact

## Predict (1 min)
<!-- section: role=predict; route=fast; minutes=1 -->

**Predict 1.** A company turns on only AWS Security Hub. Will it report an EC2 **instance** that talks to a known malicious IP address? <!-- gist-trap -->

**Predict 2.** An AWS Config rule checks that each S3 **bucket** is not public. Does the rule stop an engineer who makes a bucket public?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

List the GuardDuty detectors in two Regions and compare them.

<!-- task:start id=detection-t01 -->

Look

**It kills the belief.** "GuardDuty is a global service, so one switch covers every Region."

> **Cost:** $0.

**Permissions.** `ec2:DescribeAvailabilityZones`, `guardduty:ListDetectors`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. Ask AWS which Region your shell uses.

   ```bash
   aws ec2 describe-availability-zones --query "AvailabilityZones[0].RegionName"
   ```

   Expect: One Region code, for example "us-east-1".

2. List the GuardDuty detectors in this Region.

   ```bash
   aws guardduty list-detectors
   ```

   Expect: "DetectorIds" with one detector ID if GuardDuty is on in this Region, or an empty list if it is off.

3. Choose a second Region as <OTHER_REGION>, for example eu-west-1, or us-east-1 if your shell already uses eu-west-1. List the detectors there.

   ```bash
   aws guardduty list-detectors --region <OTHER_REGION>
   ```

   Expect: An empty list, or one detector ID that is not the ID from step 2.

**Label.** checked against docs, not run in a real account. Checked 2026-10-12.

<!-- task:end -->

## In one breath (2 min)
<!-- section: role=breath; route=fast; minutes=2 -->

> **Say it:** GuardDuty watches activity, Inspector scans software, Macie finds **sensitive data** in S3, Config records settings, and Security Hub gathers their findings.

**The problem it solves.** No team can read every log and **object** by hand.

**Predict the picture.** Do findings stay in each service, or meet in one place?

<details>
<summary>Show the picture</summary>

![On the left, four kinds of evidence in an AWS account: activity logs, workloads, S3 buckets and resource configurations. Each feeds one service: Amazon GuardDuty, Amazon Inspector, Amazon Macie and AWS Config. Arrows carry their findings to AWS Security Hub. From Security Hub, findings go to Amazon EventBridge, and Amazon Detective investigates one finding.](../diagrams/svg/detection-hero.svg)

**Figure.** GuardDuty, Inspector, Macie and AWS Config each read one kind of evidence, and Security Hub gathers their findings in one place.

1. Amazon GuardDuty analyzes activity such as CloudTrail management events, VPC flow logs and [DNS logs](../facts/guardduty.md#guardduty-foundational-sources-list).
2. Amazon Inspector scans workloads for [software vulnerabilities and unintended network exposure](../facts/inspector.md#inspector-dg-vulnerabilities-exposure).
3. Amazon Macie discovers sensitive data in Amazon S3.
4. AWS Config records how each resource is configured over time.
5. AWS Security Hub receives the findings of these services in one place.
6. Findings go on to Amazon EventBridge, and Amazon Detective helps you find the root cause of one finding.

</details>

> **Startup example:** Callvale's bank asks about changes, card numbers, weak software and stolen credentials.

## Words that go together (1 min)
<!-- section: role=words; route=fast; minutes=1 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| finding | **generate** a finding | A report of a possible problem | a CloudWatch alarm |
| vulnerability (vul-ner-uh-BIL-ih-tee) | **scan** for vulnerabilities | A known weakness in software | a threat |
| sensitive data | **discover** sensitive data | Data such as card numbers | encrypted data |
| configuration item | **record** a configuration item | One resource's settings at one time | a CloudTrail event |

## Choose it or not (2 min)
<!-- section: role=choose; route=fast; minutes=2 -->

### GuardDuty or Inspector or Macie

<!-- table: compare -->
| Question | Amazon GuardDuty | Amazon Inspector | Amazon Macie |
|---|---|---|---|
| What does it read? | Activity, such as [AWS CloudTrail management events](../facts/guardduty.md#guardduty-foundational-sources-list) | Software packages in workloads | Objects in S3 buckets |
| Typical finding | [cryptocurrency mining](../facts/guardduty.md#guardduty-finding-categories) | A package with a known vulnerability | [credit card numbers and bank account numbers](../facts/macie.md#macie-managed-data-identifiers) |
| Agent or log setup first? | No, for its foundational sources: it [pulls independent data streams directly](../facts/guardduty.md#guardduty-faq-no-need-to-enable-source-logs) | No. Without the Systems Manager (SSM) Agent, it [collects software inventory using Amazon EBS snapshots](../facts/inspector.md#inspector-ec2-agent-or-agentless) | No agent |

**Deciding question:** Does the **stem** describe suspicious activity, a vulnerable package, or sensitive data in S3?

### Security Hub CSPM or Config or Artifact

Security Hub CSPM (cloud security posture management) is the original Security Hub, renamed.

<!-- table: compare -->
| Question | Security Hub CSPM | AWS Config | AWS Artifact |
|---|---|---|---|
| Whose compliance? | Yours, against standards such as [AWS Foundational Security Best Practices (FSBP)](../facts/security-hub.md#security-hub-cspm-supported-standards) | Yours, against your own rules | AWS: [the security and compliance of the AWS infrastructure](../facts/artifact.md#artifact-guide-audit-artifacts-for-auditors) |
| What do you get? | Control findings | Rule results and history | You [submit AWS Artifact documents to your auditors](../facts/artifact.md#artifact-guide-audit-artifacts-for-auditors) |

**Deciding question:** Reports about AWS (Artifact), a ready-made standard (Security Hub CSPM), or your own rules and history (Config)?

## Signals and traps (2 min)
<!-- section: role=signals; route=fast; minutes=2 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "cryptocurrency mining" | Amazon GuardDuty | it detects [cryptocurrency mining](../facts/guardduty.md#guardduty-finding-categories) | root cause of a finding: Amazon Detective |
| "known software vulnerabilities in EC2 instances" | Amazon Inspector | [software vulnerabilities and unintended network exposure](../facts/inspector.md#inspector-dg-vulnerabilities-exposure) | patch the instances: AWS Systems Manager Patch Manager <!-- xref: 38 Patch Manager --> |
| "credit card numbers stored in S3" | Amazon Macie | it [discovers sensitive data by using machine learning](../facts/macie.md#macie-dg-discovers-sensitive-data) | malware in uploaded objects: GuardDuty Malware Protection for S3 |
| "a single view of security findings" | AWS Security Hub | it [also receives findings from other AWS services](../facts/security-hub.md#security-hub-cspm-receives-service-findings) | why one finding happened: Amazon Detective |
| "history of configuration changes" | AWS Config | [resource inventory, configuration history, and configuration change notifications](../facts/config.md#config-faq-what-it-is) | who made the change: AWS CloudTrail |
| "AWS compliance reports for an auditor" | AWS Artifact | [on-demand downloads of AWS security and compliance documents](../facts/artifact.md#artifact-guide-on-demand-compliance-documents) | checks of your own resources: Security Hub CSPM |

### Traps

- **Wrong belief:** GuardDuty and Inspector find the same problems. **Truth:** Inspector finds [software vulnerabilities and unintended network exposure](../facts/inspector.md#inspector-dg-vulnerabilities-exposure). GuardDuty looks [for malicious activity](../facts/guardduty.md#guardduty-dg-continuous-malicious-activity). <!-- trap: detection-trap-guardduty-inspector-same-job -->
- **Wrong belief:** Macie watches S3 for threats. **Truth:** Macie is a [fully managed sensitive data discovery service](../facts/guardduty.md#guardduty-faq-vs-macie). GuardDuty S3 Protection reads [AWS CloudTrail data events for Amazon S3](../facts/guardduty.md#guardduty-s3-protection-data-events). <!-- trap: detection-trap-macie-finds-threats -->
- **Wrong belief:** Security Hub or Detective detects threats by itself. **Truth:** GuardDuty [continuously monitors for malicious activity and unauthorized behavior](../facts/detective.md#detective-vs-guardduty-vs-security-hub). Security Hub gathers findings; Detective investigates them. <!-- trap: detection-trap-hub-or-detective-detects -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2025-12-02) Security Hub is now two services.<br>
> **Old:** AWS Security Hub: findings and best practice checks.<br>
> **Now:** that service [is now available as Security Hub CSPM](../facts/security-hub.md#security-hub-renamed-cspm); a new unified AWS Security Hub became available on [December 2, 2025](../facts/security-hub.md#security-hub-unified-ga-2025-12).<br>
> **The exam probably expects:** Security Hub CSPM when an older question says "Security Hub".<br>
> **Status:** examinable.

## Check (1 min)
<!-- section: role=check; route=fast; minutes=1 -->

**Check 1.** A company turns on the new AWS Security Hub alone. Does Macie start looking for card numbers?

<details>
<summary>Answer</summary>

No. Macie [is not automatically enabled](../facts/security-hub.md#security-hub-enables-cspm-not-macie). Turn it on, and set it to [also send sensitive data findings](../facts/security-hub.md#security-hub-cspm-macie-policy-findings-default).

**Predict 1:** No. Turn on GuardDuty to detect the traffic.

</details>

**Check 2.** A proactive Config rule finds a template noncompliant. Is the deployment blocked?

<details>
<summary>Answer</summary>

No. [Proactive rules do not remediate resources](../facts/config.md#config-guide-proactive-vs-detective) or block deployment.

**Predict 2:** No. [AWS Config rules do not prevent the user](../facts/config.md#config-faq-rules-evaluate-after-change-not-prevent) from the change.

</details>

## Recap from memory (1 min)
<!-- section: role=recap; route=fast; minutes=1 -->

**Recap 1.** Which service watches activity, and which records settings?

<details>
<summary>Answer</summary>

GuardDuty. AWS Config.

</details>

**Recap 2.** Which service finds card numbers in S3, and which finds malware in uploads?

<details>
<summary>Answer</summary>

Amazon Macie. GuardDuty Malware Protection for S3.

</details>

**Recap 3.** Which service gives AWS audit reports?

<details>
<summary>Answer</summary>

AWS Artifact.

</details>
