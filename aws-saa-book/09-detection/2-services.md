---
chapter: "09"
file: services
title: The seven detection services, card by card
status: ready
updated: 2026-10-12
---

# The seven detection services, card by card

## Amazon GuardDuty (1 min)
<!-- section: role=card; route=full; minutes=1; service=guardduty -->

**What it is.** A threat detection service that watches activity in your AWS accounts and workloads. It analyzes CloudTrail management events, VPC flow logs and DNS logs, and writes a finding about malicious or unexpected behavior.

**Stem signals.**

- "a compromised EC2 instance" or "cryptocurrency mining"
- "unusual API calls" or "credential exfiltration"
- "malware in newly uploaded S3 objects"

**Do not confuse with.** Amazon Macie finds sensitive data in S3, and GuardDuty finds threats. Amazon Inspector finds vulnerable software, and GuardDuty finds suspicious activity. Amazon Detective helps you find the cause of a GuardDuty finding.

**One fact.** Suspending GuardDuty stops the analysis, but it [will not delete your existing findings](../facts/guardduty.md#guardduty-faq-suspend-vs-disable). Disabling GuardDuty is different: [this will delete all remaining data](../facts/guardduty.md#guardduty-faq-suspend-vs-disable), findings included. Export the findings first if you need to keep them.

> **Say it:** GuardDuty watches activity in your accounts and reports threats. Turn it on in every Region that you use.

**Source.** [What is Amazon GuardDuty?](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

## Amazon Inspector (1 min)
<!-- section: role=card; route=full; minutes=1; service=inspector -->

**What it is.** An automated vulnerability management service that continually scans EC2 instances, Lambda functions and container images for software vulnerabilities and unintended network exposure. On EC2 instances, it scans with the SSM Agent or without an agent, from EBS snapshots.

**Stem signals.**

- "common vulnerabilities and exposures (CVEs) on EC2 instances"
- "scan container images in Amazon ECR"
- "Lambda function dependencies with known vulnerabilities"

**Do not confuse with.** Amazon GuardDuty watches activity, and Inspector scans software. Amazon Inspector Classic is the earlier version, which the current Amazon Inspector replaced. AWS Config checks resource settings, and Inspector checks the software inside the workload.

**One fact.** Amazon Inspector Classic reached its end of support on [May 20, 2026](../facts/inspector.md#inspector-classic-full-shutdown-2026-05). An older question about an Inspector agent or assessment runs describes Inspector Classic; answer it with what the current Amazon Inspector does.

> **Say it:** Inspector finds known vulnerabilities in your instances, container images and functions. It reads software, not activity.

**Source.** [Amazon Inspector FAQs](https://aws.amazon.com/inspector/faqs/)

## Amazon Macie (1 min)
<!-- section: role=card; route=full; minutes=1; service=macie -->

**What it is.** A data security service that discovers sensitive data in Amazon S3 by using machine learning and pattern matching. Macie also keeps an inventory of your S3 buckets and reports a bucket that becomes publicly accessible.

**Stem signals.**

- "personally identifiable information (PII) in S3 buckets"
- "classify sensitive data such as credit card numbers"
- "a bucket became publicly accessible"

**Do not confuse with.** GuardDuty S3 Protection watches API activity on S3 for threats, and Macie reads the content of the objects. Amazon Inspector scans software packages in workloads, not the data in buckets.

**One fact.** Macie does not analyze every object. It skips some storage classes, [such as S3 Glacier Deep Archive or S3 Express One Zone](../facts/macie.md#macie-unsupported-storage-classes). Inside the objects that it reads, its managed data identifiers detect [credit card numbers and bank account numbers](../facts/macie.md#macie-managed-data-identifiers).

> **Say it:** Macie finds sensitive data, such as card numbers, in your S3 buckets. It reads objects, not activity.

**Source.** [What is Amazon Macie?](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)

## AWS Security Hub (1 min)
<!-- section: role=card; route=full; minutes=1; service=security-hub -->

**What it is.** A unified cloud security service that correlates signals from Security Hub CSPM, Amazon Inspector, Amazon Macie and Amazon GuardDuty to prioritize critical issues. The earlier service with this name is now Security Hub CSPM (Cloud Security Posture Management), which runs automated best practice checks across your accounts.

**Stem signals.**

- "a single view of security findings across accounts"
- "check accounts against security best practice standards"
- "aggregate findings from all Regions into one Region"

**Do not confuse with.** Amazon Detective: Security Hub gathers and prioritizes findings, and Detective investigates one finding. Amazon GuardDuty: GuardDuty detects threats, and Security Hub shows those findings next to the others.

**One fact.** AWS recommends that you turn on both services. Without Security Hub CSPM, [Security Hub cannot use Security Hub CSPM findings](../facts/security-hub.md#security-hub-recommend-enable-both) to show risks and exposures.

> **Say it:** Security Hub is the one place where your security findings meet, with standards and priorities.

**Source.** [What are Security Hub and Security Hub CSPM?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html)

## Amazon Detective (1 min)
<!-- section: role=card; route=full; minutes=1; service=detective -->

**What it is.** A service that helps you investigate security findings and identify their root cause. Detective collects log data from your AWS resources and builds visualizations with machine learning, statistical analysis and graph theory.

**Stem signals.**

- "investigate the root cause of a GuardDuty finding"
- "visualize the activity behind a security finding"
- "analyze the log data around suspicious activity"

**Do not confuse with.** Amazon GuardDuty detects threats, and Detective helps you investigate them. AWS Security Hub gathers many findings in one list, and Detective helps you explain the cause of one of them. Amazon Macie looks at data in S3, and Detective looks at the activity around a finding.

**One fact.** From [February 2, 2024](../facts/detective.md#detective-guardduty-requirement-removed), you can enable Detective without GuardDuty. Older questions can still assume that GuardDuty comes first.

> **Say it:** Detective shows what happened around a finding, so you can find its root cause.

**Source.** [What is Amazon Detective?](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html)

## AWS Config (1 min)
<!-- section: role=card; route=full; minutes=1; service=config -->

**What it is.** A **managed service** that gives you a resource inventory, configuration history and configuration change notifications. Config rules evaluate your resources against the configurations that you want.

**Stem signals.**

- "history of configuration changes of a resource"
- "evaluate resources against desired configurations"
- "a conformance pack deployed across an organization"

**Do not confuse with.** AWS CloudTrail: CloudTrail answers who made an API call, and Config answers what the resource looked like. Security Hub CSPM: CSPM runs ready-made security standards, and a conformance pack holds the rules that you choose.

**One fact.** An aggregator collects configuration and compliance data from many accounts and Regions into one account. It is a read-only view: [you cannot deploy rules through an aggregator](../facts/config.md#config-guide-aggregator-read-only). To deploy rules to many accounts, a conformance pack can be [deployed across an entire organization](../facts/config.md#config-faq-conformance-pack-org-wide-immutable), or you [use AWS CloudFormation StackSets](../facts/config.md#config-faq-aggregation-reporting-only-use-stacksets).

> **Say it:** Config records how each resource is configured over time and checks it against your rules.

**Source.** [AWS Config FAQs](https://aws.amazon.com/config/faqs/)

## AWS Artifact (1 min)
<!-- section: role=card; route=full; minutes=1; service=artifact -->

**What it is.** A self-service portal in the AWS Management Console. It gives on-demand access to AWS compliance documents, such as ISO, PCI and SOC audit reports, and to AWS agreements.

**Stem signals.**

- "the AWS SOC report for an auditor"
- "accept the Business Associate Addendum (BAA)"
- "evidence that the AWS infrastructure is compliant"

**Do not confuse with.** Security Hub CSPM standards and AWS Config conformance packs: they check your own resources. Artifact gives the reports about AWS itself, and you remain responsible for the evidence about your own workload. AWS Audit Manager: Audit Manager collects evidence about your own controls.

**One fact.** AWS provides Artifact documents and agreements [free of charge](../facts/artifact.md#artifact-guide-free-of-charge). An agreement such as a BAA can cover one account or every account in your organization. [Only the management account in an organization](../facts/artifact.md#artifact-faq-account-vs-organization-agreements) can accept an organization agreement.

> **Say it:** Artifact is where you download the compliance reports of AWS and accept agreements such as a BAA.

**Source.** [AWS Artifact FAQ](https://aws.amazon.com/artifact/faq/)
