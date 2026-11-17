import sys
p = sys.argv[1]
t = open(p).read()
G = '../facts/guardduty.md#'; I = '../facts/inspector.md#'; C = '../facts/config.md#'
S = '../facts/security-hub.md#'; D = '../facts/detective.md#'; M = '../facts/macie.md#'


def cut_block(t, start, end_marker):
    s = t.find(start)
    assert s >= 0, start[:60]
    e = t.find(end_marker, s)
    assert e >= 0
    e += len(end_marker)
    return t[:s] + t[e:]


R = [
# 1. Detective Changed recently in deep: removed (the card in 2-services.md carries it)
('''

> **Changed recently:** (2024-02-02) Detective no longer needs GuardDuty.<br>
> **Old:** [GuardDuty enabled in your account for 48 hours](''' + D + '''detective-guardduty-requirement-removed) before Detective.<br>
> **Now:** you are [no longer required to be a GuardDuty customer](''' + D + '''detective-guardduty-requirement-removed) to enable Detective.<br>
> **The exam probably expects:** older questions can assume that GuardDuty comes first. Today, Detective works without it.<br>
> **Status:** examinable.''', ''),
# 2. automatic response go deeper removed
('''

<details>
<summary>Go deeper: an automatic response</summary>

[With GuardDuty, EventBridge, and AWS Lambda](''' + G + '''guardduty-automated-remediation-eventbridge-lambda), you can set up automated remediation. For example, a Lambda function can [modify your AWS security group rules](''' + G + '''guardduty-automated-remediation-eventbridge-lambda) after a finding.

</details>''', ''),
# 3. proactive go deeper -> one body sentence after the trigger table
('''

<details>
<summary>Go deeper: proactive rules</summary>

There are [two evaluation modes for AWS Config rules](''' + C + '''config-guide-proactive-vs-detective). A detective rule can [evaluate resources that have already been deployed](''' + C + '''config-guide-proactive-vs-detective). A proactive rule checks a resource before deployment, but [proactive rules do not remediate resources](''' + C + '''config-guide-proactive-vs-detective) or block the deployment.

</details>''', ''),
('''| Periodic | [At a frequency that you choose](''' + C + '''config-guide-trigger-types) |
''', '''| Periodic | [At a frequency that you choose](''' + C + '''config-guide-trigger-types) |

A proactive rule checks a resource before deployment, but [proactive rules do not remediate resources](''' + C + '''config-guide-proactive-vs-detective) or block it.
'''),
# 4. sub1 stop: shorter
('''**Stop and answer.** An **access key** that never did so before opens a security group to the internet. Which service can report the call as suspicious, and which shows the rules before and after?''',
 '''**Stop and answer.** An **access key** opens a security group to the internet. Which service flags the call, and which shows the old rules?'''),
('''GuardDuty reports the call, from activity: it watches [for malicious activity](''' + G + '''guardduty-dg-continuous-malicious-activity). AWS Config shows the rules, from configuration: it records [how they were configured in the past](''' + C + '''config-guide-definition-history-relationships).''',
 '''GuardDuty, from activity: it watches [for malicious activity](''' + G + '''guardduty-dg-continuous-malicious-activity). AWS Config, from configuration: it shows [how they were configured in the past](''' + C + '''config-guide-definition-history-relationships).'''),
# 5. delegate: keep the xref only
(''' The management account names it, for example as [the delegated GuardDuty administrator account](''' + G + '''guardduty-delegated-admin-organizations).''', ''),
# 6. protection plans shorter
('''The foundational sources need no setup. You can also [enable one or more dedicated protection plans](''' + G + '''guardduty-protection-plans-optional). S3 Protection reads [AWS CloudTrail data events for Amazon S3](''' + G + '''guardduty-s3-protection-data-events). Malware Protection for S3 scans [newly uploaded objects](''' + G + '''guardduty-malware-s3-scans-new-uploads-managed). Runtime Monitoring [uses a GuardDuty security agent](''' + G + '''guardduty-runtime-needs-security-agent), so it is the exception to "no agent".''',
 '''Optional protection plans add sources. S3 Protection reads [AWS CloudTrail data events for Amazon S3](''' + G + '''guardduty-s3-protection-data-events). Runtime Monitoring [uses a GuardDuty security agent](''' + G + '''guardduty-runtime-needs-security-agent).'''),
# 7. CSPM macie lines shorter
('''Macie [automatically starts sending policy findings](''' + S + '''security-hub-cspm-macie-policy-findings-default) to Security Hub CSPM. Card numbers are sensitive data findings: you configure Macie to [also send sensitive data findings](''' + S + '''security-hub-cspm-macie-policy-findings-default).''',
 '''For card numbers, you configure Macie to [also send sensitive data findings](''' + S + '''security-hub-cspm-macie-policy-findings-default).'''),
# 8. macie step 2
('''2. **Sample and match.** Automated discovery [uses sampling techniques to identify and select representative S3 objects](''' + M + '''macie-automated-discovery-sampling). Managed data identifiers, which are built-in patterns, find''',
 '''2. **Sample and match.** Automated discovery samples objects. Managed data identifiers, which are built-in patterns, find'''),
# 9. decision record reasons reverted
('''- A weekly manual checklist: it sees one account, once a week.
- Open-source scanners on EC2: the team runs and patches them in every account.''', '''- A weekly manual checklist.
- Open-source scanners on EC2.'''),
# 10. sub7 stop shorter
('''**Stop and answer.** An auditor wants a year of Security Hub CSPM findings that the team never sent anywhere. What can the team give, and what should it change?''',
 '''**Stop and answer.** An auditor wants a year of Security Hub CSPM findings that were never copied. What can the team give?'''),
('''Only the findings updated in the last [90 days](''' + S + '''security-hub-finding-retention-90-days). Next, keep a copy: Security Hub CSPM [automatically sends all new findings and all updates](''' + S + '''security-hub-cspm-eventbridge-all-findings) to EventBridge, and an EventBridge rule can pass them to a store that the team keeps.''',
 '''Only findings updated in the last [90 days](''' + S + '''security-hub-finding-retention-90-days). Next time, copy them out: CSPM [automatically sends all new findings and all updates](''' + S + '''security-hub-cspm-eventbridge-all-findings) to EventBridge.'''),
# 11. sub2 stop answer shorter
('''Yes. The DNS logs come with GuardDuty: you do not [activate or pay for them separately](''' + G + '''guardduty-faq-logs-no-separate-activation-or-charge). The condition is the resolver. [If you use another DNS resolver]''',
 '''Yes: you do not [activate or pay for them separately](''' + G + '''guardduty-faq-logs-no-separate-activation-or-charge). The resolver is the condition. [If you use another DNS resolver]'''),
# 12. sub3 say it
('The thing to watch is the SSM Agent: without it, Inspector scans EBS snapshots instead.', 'The thing to watch is the SSM Agent.'),
# 13. ECR go deeper shorter
('''With enhanced scanning, Inspector watches an image for new CVEs during its rescan duration. For new accounts, the default is [14 days](''' + I + '''inspector-ecr-rescan-default-14-days-new-accounts).''',
 '''Enhanced scanning rescans for new CVEs during the rescan duration: [14 days](''' + I + '''inspector-ecr-rescan-default-14-days-new-accounts) by default for new accounts.'''),
# 16. aggregator trap shorter
('''> **Exam trap:** A Config aggregator does not collect GuardDuty or Macie findings. It collects [configuration and compliance data from multiple source accounts](''' + C + '''config-guide-aggregator-read-only). Security Hub CSPM receives the findings.''',
 '''> **Exam trap:** A Config aggregator collects [configuration and compliance data from multiple source accounts](''' + C + '''config-guide-aggregator-read-only), not GuardDuty or Macie findings.'''),
]
for a, b in R:
    n = t.count(a)
    assert n == 1, (n, a[:90])
    t = t.replace(a, b)
open(p, 'w').write(t)
print('ok')
