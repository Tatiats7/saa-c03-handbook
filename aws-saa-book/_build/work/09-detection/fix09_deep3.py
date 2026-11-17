import sys
p = sys.argv[1]
t = open(p).read()
G = '../facts/guardduty.md#'; I = '../facts/inspector.md#'; C = '../facts/config.md#'
S = '../facts/security-hub.md#'; D = '../facts/detective.md#'; M = '../facts/macie.md#'
R = [
# a. FAQ 1 quote: first sentence only
('''> "GuardDuty is a Regional service. Even when multiple accounts are enabled and multiple AWS Regions are used, the GuardDuty security findings remain in the same Regions where the underlying data was generated."''',
 '''> "GuardDuty is a Regional service."'''),
# b. sub6 why
('Why does AWS work this way? Gathering findings and explaining one finding need different data. Security Hub needs every finding in one list, and Detective needs the activity around one finding.',
 'Why does AWS work this way? The two jobs need different data: Security Hub needs every finding, and Detective needs the activity around one.'),
# c. protection plans
('''Optional protection plans add sources. S3 Protection reads [AWS CloudTrail data events for Amazon S3](''' + G + '''guardduty-s3-protection-data-events). Runtime Monitoring [uses a GuardDuty security agent](''' + G + '''guardduty-runtime-needs-security-agent).''',
 '''Optional protection plans add sources, such as S3 Protection. Runtime Monitoring [uses a GuardDuty security agent](''' + G + '''guardduty-runtime-needs-security-agent).'''),
# d. sub2 stop answer
('''Yes: you do not [activate or pay for them separately](''' + G + '''guardduty-faq-logs-no-separate-activation-or-charge). The resolver is the condition. [If you use another DNS resolver](''' + G + '''guardduty-dns-needs-aws-resolver), GuardDuty gets no DNS data.''',
 '''Yes. The resolver is the condition: [If you use another DNS resolver](''' + G + '''guardduty-dns-needs-aws-resolver), GuardDuty gets no DNS data.'''),
# e. sub7 step 3 removed, step 4 shorter
('''3. **Check yourself.** Security Hub CSPM runs standards on your own resources.
4. **Keep.** Export findings before the service deletes them. GuardDuty can [optionally export the generated findings](''' + G + '''guardduty-export-findings-to-s3) to an S3 bucket.''',
 '''3. **Keep.** Before findings expire, GuardDuty can [optionally export the generated findings](''' + G + '''guardduty-export-findings-to-s3) to S3.'''),
# f. sub1 stop answer
('''GuardDuty, from activity: it watches [for malicious activity](''' + G + '''guardduty-dg-continuous-malicious-activity). AWS Config, from configuration: it shows [how they were configured in the past](''' + C + '''config-guide-definition-history-relationships).''',
 '''GuardDuty watches [for malicious activity](''' + G + '''guardduty-dg-continuous-malicious-activity). AWS Config shows [how they were configured in the past](''' + C + '''config-guide-definition-history-relationships).'''),
# g. sub6 step 5
('''5. **Investigate.** Detective builds a behavior graph, [a linked set of extracted and analyzed data](''' + D + '''detective-behavior-graph-definition). From a GuardDuty or Security Hub finding, you go [directly into the Detective console](''' + D + '''detective-pivot-from-guardduty-security-hub).''',
 '''5. **Investigate.** A Detective behavior graph is [a linked set of extracted and analyzed data](''' + D + '''detective-behavior-graph-definition); a finding opens [directly into the Detective console](''' + D + '''detective-pivot-from-guardduty-security-hub).'''),
# h. real world say it
('built its security framework on Security Hub, now Security Hub CSPM. One', 'built its security framework on Security Hub. One'),
('**Sony Music Entertainment Japan, after 2018.**', '**Sony Music Entertainment Japan, 2024.**'),
# i. numbers cell
('| Repeats only: set [15 minutes](' + G + 'guardduty-eventbridge-subsequent-occurrences-default-6-hours) or [1 hour](' + G + 'guardduty-eventbridge-subsequent-occurrences-default-6-hours). New findings: [near real-time](' + G + 'guardduty-eventbridge-new-findings-near-real-time) |',
 '| Repeats: [15 minutes](' + G + 'guardduty-eventbridge-subsequent-occurrences-default-6-hours) or [1 hour](' + G + 'guardduty-eventbridge-subsequent-occurrences-default-6-hours) possible. New findings: [near real-time](' + G + 'guardduty-eventbridge-new-findings-near-real-time) |'),
# j. ECR: default in the cell, go deeper back to basic scanning only
('| ECR container image | A push, or a new CVE during the rescan duration |',
 '| ECR container image | A push, or a new CVE within the rescan duration (new accounts: [14 days](' + I + 'inspector-ecr-rescan-default-14-days-new-accounts)) |'),
('''<summary>Go deeper: ECR basic scanning and the rescan duration</summary>''', '''<summary>Go deeper: ECR basic scanning</summary>'''),
(''' Enhanced scanning rescans for new CVEs during the rescan duration: [14 days](''' + I + '''inspector-ecr-rescan-default-14-days-new-accounts) by default for new accounts.''', ''),
# k. sub3 stop
('**Stop and answer.** A new CVE is published today. Instance A has the SSM Agent, and instance B has none. Which instance can wait longer for its finding?',
 '**Stop and answer.** A new CVE is published. Instance A has the SSM Agent; instance B has none. Which finding can come later?'),
# o. proactive
('A proactive rule checks a resource before deployment, but [proactive rules', 'A proactive rule checks before deployment, but [proactive rules'),
# q. macie gloss
('Managed data identifiers, which are built-in patterns, find', 'Managed data identifiers (built-in patterns) find'),
# t. sub2 step1
('''1. **Enable it per Region.** GuardDuty is [a regional service](''' + G + '''guardduty-regional-service-detector); AWS recommends that you [enable GuardDuty in all AWS Regions](''' + G + '''guardduty-enable-in-all-regions).''',
 '''1. **Enable it per Region.** GuardDuty is [a regional service](''' + G + '''guardduty-regional-service-detector).'''),
]
for a, b in R:
    n = t.count(a)
    assert n == 1, (n, a[:90])
    t = t.replace(a, b)
open(p, 'w').write(t)
print('ok')
