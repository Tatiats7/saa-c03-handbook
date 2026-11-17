import sys
p = sys.argv[1]
t = open(p).read()
G = '../facts/guardduty.md#'; I = '../facts/inspector.md#'; C = '../facts/config.md#'
S = '../facts/security-hub.md#'; D = '../facts/detective.md#'; M = '../facts/macie.md#'
R = [
# subsection 1
('1. **Activity.** Amazon GuardDuty reads API calls and network traffic [for malicious activity]',
 '1. **Activity.** Amazon GuardDuty watches API calls, VPC flow logs and DNS logs [for malicious activity]'),
('''**Stop and answer.** A company must know when an **access key** calls APIs from an unusual geolocation. Which service, and which evidence?

<details>
<summary>Answer</summary>

GuardDuty, from activity. Its account compromise findings cover such calls and [attempts to deactivate CloudTrail logging](''' + G + '''guardduty-finding-categories).''',
'''**Stop and answer.** An **access key** that never did so before opens a security group to the internet. Which service can report the call as suspicious, and which shows the rules before and after?

<details>
<summary>Answer</summary>

GuardDuty reports the call, from activity: it watches [for malicious activity](''' + G + '''guardduty-dg-continuous-malicious-activity). AWS Config shows the rules, from configuration: it records [how they were configured in the past](''' + C + '''config-guide-definition-history-relationships).'''),
# subsection 2
('| DNS logs | No, with the AWS DNS resolvers | No |', '| DNS logs | No, if instances use the AWS DNS resolvers | No |'),
('''> **Exam trap:** An auditor asks GuardDuty for old flow logs.''', '''<details>
<summary>Go deeper: protection plans</summary>

The foundational sources need no setup. You can also [enable one or more dedicated protection plans](''' + G + '''guardduty-protection-plans-optional). S3 Protection reads [AWS CloudTrail data events for Amazon S3](''' + G + '''guardduty-s3-protection-data-events). Malware Protection for S3 scans [newly uploaded objects](''' + G + '''guardduty-malware-s3-scans-new-uploads-managed). Runtime Monitoring [uses a GuardDuty security agent](''' + G + '''guardduty-runtime-needs-security-agent), so it is the exception to "no agent".

</details>

> **Exam trap:** An auditor asks GuardDuty for old flow logs.'''),
('''**Stop and answer.** EC2 instances send DNS queries to the team's own DNS servers. Which GuardDuty evidence is missing for them?

<details>
<summary>Answer</summary>

DNS logs: [If you use another DNS resolver](''' + G + '''guardduty-dns-needs-aws-resolver), GuardDuty gets no DNS data. Flow logs still arrive.''',
'''**Stop and answer.** Instances use the AWS DNS resolvers, and the team never turned on DNS query logging. Does GuardDuty still get DNS data?

<details>
<summary>Answer</summary>

Yes. The DNS logs come with GuardDuty: you do not [activate or pay for them separately](''' + G + '''guardduty-faq-logs-no-separate-activation-or-charge). The condition is the resolver. [If you use another DNS resolver](''' + G + '''guardduty-dns-needs-aws-resolver), GuardDuty gets no DNS data.'''),
# subsection 3
('1. **Inventory.** On EC2, Inspector reads packages [using the Amazon EC2 Systems Manager (SSM) agent](' + I + 'inspector-ec2-agent-or-agentless), or it',
 '1. **Inventory.** On EC2, Inspector reads packages with the [AWS Systems Manager Agent (SSM Agent)](' + I + 'inspector-faq-uses-ssm-agent-not-standalone-agent), or it'),
('| EC2 instance | A changed package or a new CVE |',
 '| EC2 instance | With the SSM Agent: a changed package or a new CVE. Agentless: [every 24 hours](' + I + 'inspector-hybrid-agentless-every-24-hours) |'),
('| ECR container image | A push or a new CVE |', '| ECR container image | A push, or a new CVE during the rescan duration |'),
('''<summary>Go deeper: ECR basic scanning</summary>

Amazon ECR basic scanning [offers only on-push scanning](''' + I + '''inspector-faq-ecr-enhanced-vs-basic-frequency).''',
'''<summary>Go deeper: ECR basic scanning and the rescan duration</summary>

Amazon ECR basic scanning [offers only on-push scanning](''' + I + '''inspector-faq-ecr-enhanced-vs-basic-frequency). With enhanced scanning, Inspector watches an image for new CVEs during its rescan duration. For new accounts, the default is [14 days](''' + I + '''inspector-ecr-rescan-default-14-days-new-accounts).'''),
('The thing to watch is how it reaches each instance.', 'The thing to watch is the SSM Agent: without it, Inspector scans EBS snapshots instead.'),
('''**Stop and answer.** A new CVE is published for a package on an EC2 instance that has not changed for a month. Does the team have to start a scan?

<details>
<summary>Answer</summary>

No. Inspector keeps [automatically rescanning resources in response to changes](''' + I + '''inspector-no-scheduled-assessments), such as [a new common vulnerabilities and exposures (CVE)](''' + I + '''inspector-no-scheduled-assessments).''',
'''**Stop and answer.** A new CVE is published today. Instance A has the SSM Agent, and instance B has none. Which instance can wait longer for its finding?

<details>
<summary>Answer</summary>

Instance B. Agentless scans run [every 24 hours](''' + I + '''inspector-hybrid-agentless-every-24-hours). With the agent, Inspector keeps [automatically rescanning resources in response to changes](''' + I + '''inspector-no-scheduled-assessments), such as a newly published CVE.'''),
# subsection 4 Macie
('2. **Sample and match.** Automated discovery samples objects. Managed data identifiers find [credit card numbers',
 '2. **Sample and match.** Automated discovery [uses sampling techniques to identify and select representative S3 objects](' + M + 'macie-automated-discovery-sampling). Managed data identifiers, which are built-in patterns, find [credit card numbers'),
('The thing to watch is that Macie reads text.', 'The thing to watch is the file type of each object.'),
# subsection 5 Config
('so it judges a configuration that already exists.', 'so a detective rule judges a configuration that already exists.'),
('''> **Exam trap:** [AWS Config rules do not prevent the user]''', '''<details>
<summary>Go deeper: proactive rules</summary>

There are [two evaluation modes for AWS Config rules](''' + C + '''config-guide-proactive-vs-detective). A detective rule can [evaluate resources that have already been deployed](''' + C + '''config-guide-proactive-vs-detective). A proactive rule checks a resource before deployment, but [proactive rules do not remediate resources](''' + C + '''config-guide-proactive-vs-detective) or block the deployment.

</details>

> **Exam trap:** [AWS Config rules do not prevent the user]'''),
# subsection 6 Security Hub
('1. **Delegate.** A security account [serves as the administrator account](' + S + 'security-hub-sra-security-tooling-account).',
 '1. **Delegate.** A security account [serves as the administrator account](' + S + 'security-hub-sra-security-tooling-account). The management account names it, for example as [the delegated GuardDuty administrator account](' + G + 'guardduty-delegated-admin-organizations). <!-- xref: 04 delegated administrator -->'),
('3. **Aggregate.** Findings go [to a single home Region]', '3. **Aggregate.** Other Regions, called linked Regions, send their findings [to a single home Region]'),
('5. **Investigate.** You pivot [directly into the Detective console](' + D + 'detective-pivot-from-guardduty-security-hub).',
 '5. **Investigate.** Detective builds a behavior graph, [a linked set of extracted and analyzed data](' + D + 'detective-behavior-graph-definition). From a GuardDuty or Security Hub finding, you go [directly into the Detective console](' + D + 'detective-pivot-from-guardduty-security-hub).'),
('| An automatic response | An EventBridge rule |', '| An automatic response | An EventBridge rule that invokes a Lambda function |'),
('Why does AWS work this way? Triage needs one queue, and Detective has [no additional software to deploy](' + D + 'detective-no-queries-to-build).',
 'Why does AWS work this way? Gathering findings and explaining one finding need different data. Security Hub needs every finding in one list, and Detective needs the activity around one finding.'),
('''(cloud security posture management).

</details>''', '''(cloud security posture management).

Macie [automatically starts sending policy findings](''' + S + '''security-hub-cspm-macie-policy-findings-default) to Security Hub CSPM. Card numbers are sensitive data findings: you configure Macie to [also send sensitive data findings](''' + S + '''security-hub-cspm-macie-policy-findings-default).

</details>

<details>
<summary>Go deeper: an automatic response</summary>

[With GuardDuty, EventBridge, and AWS Lambda](''' + G + '''guardduty-automated-remediation-eventbridge-lambda), you can set up automated remediation. For example, a Lambda function can [modify your AWS security group rules](''' + G + '''guardduty-automated-remediation-eventbridge-lambda) after a finding.

</details>'''),
('and enabled Security Hub CSPM and AWS Config in us-east-1 only.', 'and has enabled Security Hub CSPM and AWS Config in us-east-1 only.'),
# subsection 7 Artifact
('4. **Keep.** Export findings before the service deletes them.',
 '4. **Keep.** Export findings before the service deletes them. GuardDuty can [optionally export the generated findings](' + G + 'guardduty-export-findings-to-s3) to an S3 bucket.'),
('''**Stop and answer.** An auditor wants a year of GuardDuty findings that were never exported. What can the team give, and what should it change?

<details>
<summary>Answer</summary>

Only [90 days](''' + G + '''guardduty-finding-retention-90-days). Next, an EventBridge rule can [push findings to an Amazon S3 bucket](''' + G + '''guardduty-longer-retention-via-eventbridge-s3).''',
'''**Stop and answer.** An auditor wants a year of Security Hub CSPM findings that the team never sent anywhere. What can the team give, and what should it change?

<details>
<summary>Answer</summary>

Only the findings updated in the last [90 days](''' + S + '''security-hub-finding-retention-90-days). Next, keep a copy: Security Hub CSPM [automatically sends all new findings and all updates](''' + S + '''security-hub-cspm-eventbridge-all-findings) to EventBridge, and an EventBridge rule can pass them to a store that the team keeps.'''),
# numbers
('| Faster needs [15 minutes](' + G + 'guardduty-eventbridge-subsequent-occurrences-default-6-hours) |',
 '| Repeats only: set [15 minutes](' + G + 'guardduty-eventbridge-subsequent-occurrences-default-6-hours) or [1 hour](' + G + 'guardduty-eventbridge-subsequent-occurrences-default-6-hours). New findings: [near real-time](' + G + 'guardduty-eventbridge-new-findings-near-real-time) |'),
('no custom rules, only [your own threat lists](' + G + 'guardduty-faq-no-custom-detections). Do not',
 'no custom rules, only [your own threat lists](' + G + 'guardduty-faq-no-custom-detections) of known bad IP addresses. Do not'),
# decision record: drop the builder note
(None, None),
('''- A weekly manual checklist.
- Open-source scanners on EC2.''', '''- A weekly manual checklist: it sees one account, once a week.
- Open-source scanners on EC2: the team runs and patches them in every account.'''),
# FAQ 2
('No. [Amazon Inspector also offers agentless scanning](' + I + 'inspector-faq-no-agent-required).',
 'No. [Amazon Inspector also offers agentless scanning](' + I + 'inspector-faq-no-agent-required) for eligible EBS-backed instances.'),
# real world
('**Sony Music Entertainment Japan, 2018.** Its SMEJ Guardrail framework rests on AWS Security Hub. It runs',
 '**Sony Music Entertainment Japan, after 2018.** Its SMEJ Guardrail framework rests on AWS Security Hub, which [is now available as Security Hub CSPM](' + S + 'security-hub-renamed-cspm). It runs'),
('> **Say it:** Sony Music Entertainment Japan built its security framework on Security Hub. One',
 '> **Say it:** Sony Music Entertainment Japan built its security framework on Security Hub, now Security Hub CSPM. One'),
]
for a, b in R:
    if a is None:
        s = t.find('<!-- deep-09: the detection-before embed waits here.')
        assert s >= 0
        e = t.find('-->', s) + 3
        assert t[e:e + 2] == '\n\n'
        t = t[:s] + t[e + 2:]
        continue
    n = t.count(a)
    assert n == 1, (n, a[:80])
    t = t.replace(a, b)
open(p, 'w').write(t)
print('ok')
