---
chapter: "09"
file: deep
title: GuardDuty, Inspector, Macie, Security Hub, Detective, Config and Artifact in depth
status: ready
updated: 2026-10-12
---

# GuardDuty, Inspector, Macie, Security Hub, Detective, Config and Artifact in depth

## How it works (29 min)
<!-- section: role=how; route=full; minutes=29 -->

### Four services detect problems and each reads a different kind of evidence (4 min)
<!-- section: route=pass -->

Each security question has its own kind of evidence.

1. **Activity.** Amazon GuardDuty watches API calls, VPC flow logs and DNS logs [for malicious activity](../facts/guardduty.md#guardduty-dg-continuous-malicious-activity).
2. **Software.** Amazon Inspector finds [software vulnerabilities and unintended network exposure](../facts/inspector.md#inspector-dg-vulnerabilities-exposure).
3. **Data.** Amazon Macie [discovers sensitive data by using machine learning](../facts/macie.md#macie-dg-discovers-sensitive-data).
4. **Configuration.** AWS Config gives [a detailed view of the configuration](../facts/config.md#config-dg-assess-audit-evaluate).
5. **One place.** Security Hub [aggregates, organizes, and prioritizes your security alerts](../facts/detective.md#detective-vs-guardduty-vs-security-hub); Detective helps you [identify the root cause of security findings](../facts/detective.md#detective-dg-root-cause).

![A ladder of six questions. Is it suspicious activity in logs or network traffic? Yes: Amazon GuardDuty. Is it a known vulnerability in software? Yes: Amazon Inspector. Is it sensitive data inside S3 objects? Yes: Amazon Macie. Is it a resource setting or its history? Yes: AWS Config. Must findings from many services appear together? Yes: AWS Security Hub. Must you find the root cause of one finding? Yes: Amazon Detective. Each no leads to the next question.](../diagrams/svg/detection-ladder.svg)

**Figure.** The evidence in the stem decides which detection service answers it.

Why does AWS work this way? In the Well-Architected security pillar, [detection consists of two parts](../facts/guardduty.md#guardduty-wa-detect-unexpected-behavior): unwanted configuration changes and unexpected behavior.

> **Exam signal:** "continuously monitor for malicious activity" points to GuardDuty, which watches [for malicious activity](../facts/guardduty.md#guardduty-dg-continuous-malicious-activity).

> **Exam trap:** GuardDuty does not check settings. A Config rule [represents desired configurations for a resource](../facts/config.md#config-faq-rule-desired-configuration). <!-- trap: detection-trap-guardduty-checks-settings -->

> **Say it:** The short answer is: name the evidence, then the service. The thing to watch is the verb: detect, scan, discover or record.

**Stop and answer.** An **access key** opens a **security group** to the internet. Which service flags the call, and which shows the old rules?

<details>
<summary>Answer</summary>

GuardDuty watches [for malicious activity](../facts/guardduty.md#guardduty-dg-continuous-malicious-activity). AWS Config shows [how they were configured in the past](../facts/config.md#config-guide-definition-history-relationships).

</details>

### GuardDuty analyzes its own copy of your logs and stores none of them (4 min)
<!-- section: route=pass -->

Reading activity logs yourself means a pipeline to build and run.

1. **Enable it per Region.** GuardDuty is [a regional service](../facts/guardduty.md#guardduty-regional-service-detector).
2. **Pull.** It reads CloudTrail management events, VPC flow logs and [DNS logs](../facts/guardduty.md#guardduty-foundational-sources-list) as its own streams.
3. **Compare.** It checks the activity against [threat intelligence feeds](../facts/guardduty.md#guardduty-uses-threat-intel-and-ml).
4. **Report and discard.** It sends findings [to the GuardDuty console and EventBridge](../facts/guardduty.md#guardduty-findings-console-and-eventbridge), [and then discards these logs](../facts/guardduty.md#guardduty-discards-source-logs).

<!-- table: plain -->
| Source | You turn it on? | GuardDuty keeps it? |
|---|---|---|
| CloudTrail management events | No | No |
| VPC flow logs | No | No |
| DNS logs | No, if instances use the AWS DNS resolvers | No |

Why does AWS work this way? You get detection without a log pipeline: you do not [activate or pay for them separately](../facts/guardduty.md#guardduty-faq-logs-no-separate-activation-or-charge).

> **Exam signal:** "without enabling VPC Flow Logs" still points to GuardDuty: it [pulls independent data streams directly](../facts/guardduty.md#guardduty-faq-no-need-to-enable-source-logs). <!-- trap: detection-trap-guardduty-needs-log-setup -->

> **Try it:** Turn on GuardDuty without creating any logs. See [3-do.md](3-do.md). <!-- task: detection-t02 -->

> **Say it:** The short answer is: turn on GuardDuty in each Region. The thing to watch is that it keeps findings, not your logs.

**Stop and answer.** Instances use the AWS DNS resolvers, and DNS query logging is off. Does GuardDuty still get DNS data?

<details>
<summary>Answer</summary>

Yes. [If you use another DNS resolver](../facts/guardduty.md#guardduty-dns-needs-aws-resolver), GuardDuty gets no DNS data.

</details>

### Inspector rescans a workload when a new vulnerability is published (4 min)

A package safe last month can have a published vulnerability today.

1. **Inventory.** On EC2, Inspector reads packages with the [AWS Systems Manager Agent (SSM Agent)](../facts/inspector.md#inspector-faq-uses-ssm-agent-not-standalone-agent), or it [collects software inventory using Amazon EBS snapshots](../facts/inspector.md#inspector-ec2-agent-or-agentless).
2. **Match.** It compares packages with known common vulnerabilities and exposures (CVEs).
3. **Rescan.** It keeps [automatically rescanning resources in response to changes](../facts/inspector.md#inspector-no-scheduled-assessments).

<!-- table: plain -->
| Workload | A new scan starts on |
|---|---|
| EC2 instance | Agent: a changed package or a new CVE. Agentless: [every 24 hours](../facts/inspector.md#inspector-hybrid-agentless-every-24-hours) |
| ECR container image | A push, or a new CVE within the rescan duration (new accounts: [14 days](../facts/inspector.md#inspector-ecr-rescan-default-14-days-new-accounts)) |
| Lambda **function** | A changed dependency or a new CVE |

Why does AWS work this way? A new CVE arrives on its own schedule, and [all scans are automatically performed based on events](../facts/inspector.md#inspector-faq-rescans-event-based).

> **Exam signal:** "scan Amazon ECR images continuously" points to Inspector enhanced scanning: [both continual scanning and on-push scanning](../facts/inspector.md#inspector-faq-ecr-enhanced-vs-basic-frequency).

<details>
<summary>Go deeper: ECR basic scanning</summary>

Amazon ECR basic scanning [offers only on-push scanning](../facts/inspector.md#inspector-faq-ecr-enhanced-vs-basic-frequency).

</details>

> **Say it:** The short answer is: Inspector rescans when a new CVE appears. The thing to watch is the SSM Agent.

**Stop and answer.** A new CVE is published. Instance A has the SSM Agent; instance B has none. Which finding can come later?

<details>
<summary>Answer</summary>

Instance B. Agentless scans run [every 24 hours](../facts/inspector.md#inspector-hybrid-agentless-every-24-hours). With the agent, Inspector keeps [automatically rescanning resources in response to changes](../facts/inspector.md#inspector-no-scheduled-assessments), such as a newly published CVE.

</details>

### Macie samples S3 objects for sensitive data and reports exposed buckets (4 min)
<!-- section: route=pass -->

A team does not know which S3 objects hold card numbers.

1. **Flag.** For [a bucket that becomes publicly accessible](../facts/macie.md#macie-policy-finding-public-bucket), [it creates a policy finding for you](../facts/macie.md#macie-policy-finding-public-bucket).
2. **Sample and match.** Automated discovery samples objects. Managed data identifiers (built-in patterns) find [credit card numbers and bank account numbers](../facts/macie.md#macie-managed-data-identifiers).
3. **Report.** Macie [automatically publishes policy and sensitive data findings](../facts/macie.md#macie-findings-auto-to-eventbridge) to EventBridge.

<!-- table: plain -->
| Finding type | Example |
|---|---|
| Policy finding | A bucket became public |
| Sensitive data finding | Card numbers in a transcript |

For malware, GuardDuty Malware Protection for S3 scans [newly uploaded objects](../facts/guardduty.md#guardduty-malware-s3-scans-new-uploads-managed).

Why does AWS work this way? Sampling gives [broad visibility into where sensitive data might reside](../facts/macie.md#macie-automated-discovery-sampling), and a discovery job gives [deeper, more targeted analysis](../facts/macie.md#macie-discovery-jobs-targeted).

> **Exam signal:** "personally identifiable information (PII) in Amazon S3" points to Macie, which detects [personally identifiable information (PII)](../facts/macie.md#macie-managed-data-identifiers).

> **Say it:** The short answer is: Macie finds sensitive data in S3 and flags public buckets. The thing to watch is the file type.

**Stop and answer.** Callvale's recordings in callvale-audio hold spoken card numbers. Will a Macie job on that bucket report them?

<details>
<summary>Answer</summary>

No. Macie finds them in the text transcripts.

> "Macie doesn’t analyze data in images, or audio, video, and other types of multimedia content."
> — [Supported storage classes and formats](https://docs.aws.amazon.com/macie/latest/user/discovery-supported-storage.html)

</details>

### Config judges a change against your rules after the change is recorded (4 min)
<!-- section: route=pass -->

An auditor asks how a **security group** looked in March and whether it complies today.

1. **Record.** The configuration recorder [stores the configuration changes](../facts/config.md#config-guide-configuration-recorder).
2. **Evaluate.** A Config rule [represents desired configurations for a resource](../facts/config.md#config-faq-rule-desired-configuration).
3. **Flag.** AWS Config [flags the resource as noncompliant](../facts/config.md#config-guide-rules-flag-noncompliant) after the change.
4. **Remediate.** A remediation runs [AWS Systems Manager Automation documents](../facts/config.md#config-guide-remediation-ssm-automation).

<!-- table: plain -->
| Trigger type | The rule runs |
|---|---|
| Configuration change | When a resource in scope changes |
| Periodic | [At a frequency that you choose](../facts/config.md#config-guide-trigger-types) |

A proactive rule checks before deployment, but [proactive rules do not remediate resources](../facts/config.md#config-guide-proactive-vs-detective) or block it.

Why does AWS work this way? AWS Config reads configurations by [invoking the Describe or the List API call](../facts/config.md#config-guide-tracks-non-api-changes), so a detective rule judges a configuration that already exists.

> **Exam signal:** "automatically remediate noncompliant resources" points to AWS Config remediation with [AWS Systems Manager Automation documents](../facts/config.md#config-guide-remediation-ssm-automation).

> **Exam trap:** [AWS Config rules do not prevent the user](../facts/config.md#config-faq-rules-evaluate-after-change-not-prevent) from a change. To control what users create, [use AWS Identity and Access Management (IAM) Policies](../facts/config.md#config-faq-rules-evaluate-after-change-not-prevent). <!-- trap: detection-trap-config-rule-prevents --> <!-- xref: 04 service control policies -->

> **Exam trap:** Config answers "[What did my AWS resource look like?](../facts/config.md#config-faq-vs-cloudtrail)" AWS CloudTrail answers "[Who made an API call](../facts/config.md#config-faq-vs-cloudtrail)?" <!-- trap: detection-trap-config-shows-who --> <!-- xref: 37 CloudTrail -->

> **Say it:** The short answer is: Config records each change and checks your rules. The thing to watch is timing: it reports after the change.

**Stop and answer.** A team turned on AWS Config two weeks ago. Can Config show a role's IAM policy of last month?

<details>
<summary>Answer</summary>

No. Config shows [the IAM policy that was assigned](../facts/config.md#config-guide-security-analysis-history) only for times when it was recording.

</details>

### Security Hub gathers findings in one place and Detective traces their cause (5 min)

Seven accounts send findings to many consoles; a small team needs one **queue** (KYOO).

1. **Delegate.** A security account [serves as the administrator account](../facts/security-hub.md#security-hub-sra-security-tooling-account). <!-- xref: 04 delegated administrator -->
2. **Collect.** Security Hub CSPM [also receives findings from other AWS services](../facts/security-hub.md#security-hub-cspm-receives-service-findings). For most checks, it [uses service-linked rules from AWS Config](../facts/security-hub.md#security-hub-cspm-uses-config-rules).
3. **Aggregate.** Linked Regions send their findings [to a single home Region](../facts/security-hub.md#security-hub-cspm-cross-region-aggregation).
4. **Act.** It [automatically sends all new findings and all updates](../facts/security-hub.md#security-hub-cspm-eventbridge-all-findings) to EventBridge.
5. **Investigate.** A Detective behavior graph is [a linked set of extracted and analyzed data](../facts/detective.md#detective-behavior-graph-definition); a finding opens [directly into the Detective console](../facts/detective.md#detective-pivot-from-guardduty-security-hub).

<!-- table: plain -->
| Need | Service |
|---|---|
| Every finding in one list | Security Hub |
| Why one finding happened | Detective |
| An automatic response | An EventBridge rule and a Lambda function |

Why does AWS work this way? The two jobs need different data: Security Hub needs every finding, and Detective needs the activity around one.

> **Exam signal:** "a single view of findings across Regions" points to Security Hub, with aggregation [to a single home Region](../facts/security-hub.md#security-hub-cspm-cross-region-aggregation).

<details>
<summary>Go deeper: Security Hub and Security Hub CSPM</summary>

The original Security Hub [is now available as Security Hub CSPM](../facts/security-hub.md#security-hub-renamed-cspm) (cloud security posture management).

For card numbers, you configure Macie to [also send sensitive data findings](../facts/security-hub.md#security-hub-cspm-macie-policy-findings-default).

</details>

> **Exam trap:** A Config aggregator collects [configuration and compliance data from multiple source accounts](../facts/config.md#config-guide-aggregator-read-only), not GuardDuty or Macie findings. <!-- trap: detection-trap-config-collects-findings -->

**Spot the bug.** A team aggregates findings in us-east-1 from a linked us-west-2, and has enabled Security Hub CSPM and AWS Config in us-east-1 only. What is wrong?

<details>
<summary>Answer</summary>

In us-west-2, Security Hub CSPM [is not automatically enabled for an account](../facts/security-hub.md#security-hub-aggregation-no-cost-not-auto-enable), and [AWS Config must be enabled in each Region](../facts/security-hub.md#security-hub-cspm-config-required-each-region). <!-- trap: detection-trap-cspm-without-config -->

</details>

> **Say it:** The short answer is: Security Hub is the queue, and Detective explains one finding. The thing to watch is AWS Config for the checks.

**Stop and answer.** A role made unusual API calls. Which service shows its IP addresses of last week without queries, and from which data?

<details>
<summary>Answer</summary>

Detective. It reads [CloudTrail logs, VPC Flow logs, and GuardDuty findings](../facts/detective.md#detective-core-sources).

</details>

### Artifact gives the AWS side of an audit and you keep your own evidence (4 min)

An auditor wants proof for AWS and for the company's resources.

1. **Download.** Artifact gives [System and Organization Controls (SOC) reports](../facts/artifact.md#artifact-guide-on-demand-compliance-documents) and other reports, [free of charge](../facts/artifact.md#artifact-guide-free-of-charge).
2. **Agree.** A company subject to HIPAA, a US health privacy law, typically needs [a Business Associate Addendum (BAA) agreement with AWS](../facts/artifact.md#artifact-guide-baa-for-hipaa).
3. **Keep.** Before findings expire, GuardDuty can [optionally export the generated findings](../facts/guardduty.md#guardduty-export-findings-to-s3) to S3.

Why does AWS work this way? Artifact documents show [the security and compliance of the AWS infrastructure](../facts/artifact.md#artifact-guide-audit-artifacts-for-auditors), and you are [responsible for developing or obtaining documents](../facts/artifact.md#artifact-guide-audit-artifacts-for-auditors) for yours.

> **Exam signal:** "download the AWS SOC 2 report" points to AWS Artifact: [on-demand downloads of AWS security and compliance documents](../facts/artifact.md#artifact-guide-on-demand-compliance-documents).

> **Exam trap:** A passing standard in Security Hub CSPM is not an audit result. The checks [do not imply that you would pass](../facts/security-hub.md#security-hub-faq-checks-do-not-imply-audit-pass). <!-- trap: detection-trap-artifact-proves-your-compliance -->

> **Say it:** The short answer is: Artifact gives AWS's reports, and your controls give yours. The thing to watch is retention.

**Stop and answer.** An auditor wants a year of Security Hub CSPM findings that were never copied. What can the team give?

<details>
<summary>Answer</summary>

Only findings updated in the last [90 days](../facts/security-hub.md#security-hub-finding-retention-90-days). Next, copy them out: CSPM [automatically sends all new findings and all updates](../facts/security-hub.md#security-hub-cspm-eventbridge-all-findings) to EventBridge. <!-- trap: detection-trap-findings-kept-forever -->

</details>

## Numbers that decide answers (2 min)
<!-- section: role=numbers; route=full; minutes=2 -->

### A-list

<!-- table: numbers -->
| Number | What it is | Why it decides an answer |
|---|---|---|
| [90 days](../facts/guardduty.md#guardduty-finding-retention-90-days) | GuardDuty keeps a finding | Longer needs an export |
| [for only 90 days](../facts/macie.md#macie-results-90-days-export-s3-kms) | Macie keeps discovery results | Longer needs an S3 bucket |
| [7 years (2557 days)](../facts/config.md#config-retention-30-days-to-7-years) | Default Config retention | Config answers audits years later |
| [6 hours](../facts/guardduty.md#guardduty-eventbridge-subsequent-occurrences-default-6-hours) | Default event interval for repeated GuardDuty findings | Repeats: [15 minutes](../facts/guardduty.md#guardduty-eventbridge-subsequent-occurrences-default-6-hours) or [1 hour](../facts/guardduty.md#guardduty-eventbridge-subsequent-occurrences-default-6-hours) possible. New findings: [near real-time](../facts/guardduty.md#guardduty-eventbridge-new-findings-near-real-time) |

### B-list

<!-- table: numbers -->
| Number | What it is |
|---|---|
| [1](../facts/guardduty.md#guardduty-detector-one-per-region) | GuardDuty detector per account per Region |
| [90 days](../facts/security-hub.md#security-hub-finding-retention-90-days) | Security Hub CSPM keeps a finding after its last update |

> **Changed recently:** (2026-09-01) GuardDuty Custom Detection Rules.<br>
> **Old:** not available.<br>
> **Now:** available from [September 1, 2026](../facts/guardduty.md#guardduty-custom-detection-rules-2026-09).<br>
> **The exam probably expects:** no custom rules, only [your own threat lists](../facts/guardduty.md#guardduty-faq-no-custom-detections) of known bad IP addresses. Do not let this number decide an answer.<br>
> **Status:** not examinable yet.

## Decision record (3 min)
<!-- section: role=example; route=full; minutes=3 -->

**Context.** Most of the bank's 43 "no" answers ask for detection and evidence. Chen asks which service answers which question.

**Requirement.** Detect threats, vulnerabilities, sensitive data and changes in all accounts, with findings in one place and the LEAST operational overhead.

**Options.**

- A weekly manual checklist.
- Open-source scanners on EC2.
- **Managed detection services for the organization.**

**Decision.** Managed services in all accounts, with findings in Security Hub.

![The same seven accounts. Amazon GuardDuty, Amazon Inspector, Amazon Macie and AWS Config run in each account. The security account is the delegated administrator and holds AWS Security Hub and Amazon Detective. Findings flow from every account into Security Hub. AWS Artifact supplies the AWS audit reports for the bank.](../diagrams/svg/detection-after.svg)

**Figure.** Detection services run in every account, and their findings flow into AWS Security Hub in the security account.

**Trade-off.** Every finding needs an owner, and cost grows with data.

## FAQ quick-fire (2 min)
<!-- section: role=faq; route=full; minutes=2 -->

**FAQ 1.** Is GuardDuty a global service?

<details>
<summary>Answer</summary>

No. [GuardDuty is a Regional service](../facts/guardduty.md#guardduty-faq-regional-service).

> "GuardDuty is a Regional service."
> — [Amazon GuardDuty FAQs](https://aws.amazon.com/guardduty/faqs/)

</details>

**FAQ 2.** Does Inspector need an agent on EC2?

<details>
<summary>Answer</summary>

No. [Amazon Inspector also offers agentless scanning](../facts/inspector.md#inspector-faq-no-agent-required) for eligible EBS-backed instances.

> "Amazon Inspector also offers agentless scanning if you don’t have the SSM Agent deployed or configured."
> — [Amazon Inspector FAQs](https://aws.amazon.com/inspector/faqs/)

</details>

**FAQ 3.** Does Security Hub replace the GuardDuty console?

<details>
<summary>Answer</summary>

No. [Security Hub complements other AWS security services](../facts/security-hub.md#security-hub-faq-does-not-replace-service-consoles).

> "No, Security Hub complements other AWS security services by providing a unified view and advanced correlation capabilities."
> — [AWS Security Hub FAQs](https://aws.amazon.com/security-hub/faqs/)

</details>

**FAQ 4.** Can a Config rule stop a change?

<details>
<summary>Answer</summary>

No. [AWS Config rules do not prevent the user](../facts/config.md#config-faq-rules-evaluate-after-change-not-prevent).

> "AWS Config rules do not prevent the user from making changes that could be non-compliant."
> — [AWS Config FAQs](https://aws.amazon.com/config/faqs/)

</details>

**FAQ 5.** Can you share an Artifact report with customers?

<details>
<summary>Answer</summary>

Yes, [if permitted by the terms and conditions](../facts/artifact.md#artifact-faq-share-reports-per-terms).

> "You can share the AWS compliance reports with your customers directly if permitted by the terms and conditions applicable to the specific AWS compliance report."
> — [AWS Artifact FAQ](https://aws.amazon.com/artifact/faq/)

</details>

## In the real world (1 min)
<!-- section: role=realworld; route=full; minutes=1 -->

**Sony Music Entertainment Japan, 2024.** Its SMEJ Guardrail framework rests on AWS Security Hub, which [is now available as Security Hub CSPM](../facts/security-hub.md#security-hub-renamed-cspm). It runs across [more than 300 AWS accounts](../facts/security-hub.md#security-hub-case-smej-300-accounts).

> "By performing centralized management and visualization using AWS Security Hub, we were able to standardize our security levels."
> — [Sony Music Entertainment Japan Standardizes Security Using AWS Security Hub](https://aws.amazon.com/solutions/case-studies/sony-music-entertainment-japan-case-study/)

**It shows:** one place for findings gives many accounts one security level.

> **Say it:** Sony Music Entertainment Japan built its security framework on Security Hub. One view of findings gave every account one security level.
