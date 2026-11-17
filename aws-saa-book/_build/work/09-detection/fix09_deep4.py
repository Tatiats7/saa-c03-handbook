import sys
p = sys.argv[1]
t = open(p).read()
G = '../facts/guardduty.md#'; I = '../facts/inspector.md#'; C = '../facts/config.md#'
S = '../facts/security-hub.md#'; D = '../facts/detective.md#'; M = '../facts/macie.md#'
R = [
# protection plans go deeper removed (fast table now says "for its foundational sources")
('''

<details>
<summary>Go deeper: protection plans</summary>

Optional protection plans add sources, such as S3 Protection. Runtime Monitoring [uses a GuardDuty security agent](''' + G + '''guardduty-runtime-needs-security-agent).

</details>''', ''),
# exam trap of sub2 restated the table (STYLE 11.8); its trap id belongs to the no-log-setup signal
('''> **Exam signal:** "without enabling VPC Flow Logs" still points to GuardDuty: it [pulls independent data streams directly](''' + G + '''guardduty-faq-no-need-to-enable-source-logs).''',
 '''> **Exam signal:** "without enabling VPC Flow Logs" still points to GuardDuty: it [pulls independent data streams directly](''' + G + '''guardduty-faq-no-need-to-enable-source-logs). <!-- trap: detection-trap-guardduty-needs-log-setup -->'''),
('''> **Exam trap:** An auditor asks GuardDuty for old flow logs. But [GuardDuty does not manage or retain your logs](''' + G + '''guardduty-does-not-retain-logs). Keep your own. <!-- trap: detection-trap-guardduty-needs-log-setup -->

''', ''),
# sub7 retention table duplicated the A-list
('''<!-- table: plain -->
| Evidence | Kept in the service |
|---|---|
| GuardDuty findings | [90 days](''' + G + '''guardduty-finding-retention-90-days) |
| Macie discovery results | [For only 90 days](''' + M + '''macie-results-90-days-export-s3-kms) |
| Config configuration items | [7 years (2557 days)](''' + C + '''config-retention-30-days-to-7-years) by default |

''', ''),
]
for a, b in R:
    n = t.count(a)
    assert n == 1, (n, a[:90])
    t = t.replace(a, b)
open(p, 'w').write(t)
print('ok')
