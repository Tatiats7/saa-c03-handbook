import json
D = 'aws-saa-book/_build/work/09-detection/findings/'
P = 'fix-09 (2026-10-13): '
BUDGET = 'the deep file is at its 2,400-word limit (L201) and at most 3 Go deeper blocks (L106)'
RES = {
 # claims
 'claims-01': ('fixed', 'Check 1 now asks: "A company turns on the new AWS Security Hub alone. Does Macie start looking for card numbers?" Answer: No, Macie [is not automatically enabled] (same fact); turn it on and set it to [also send sensitive data findings] (security-hub-cspm-macie-policy-findings-default).'),
 'claims-02': ('fixed', 'The Security Hub Go deeper in 2-deep.md now says: for card numbers, you configure Macie to [also send sensitive data findings] (security-hub-cspm-macie-policy-findings-default); fast Check 1 says the same. The hero and after diagram texts are spec-bound (L702, L703) and unchanged; card c010 and s01 kp5 stay true for policy findings.'),
 'claims-03': ('fixed', 'EC2 row: "Agent: a changed package or a new CVE. Agentless: [every 24 hours]" (inspector-hybrid-agentless-every-24-hours). FAQ 2: agentless scanning "for eligible EBS-backed instances". The H3 heading is fixed by brief.json (L905; question and task section anchors) and stays.'),
 'claims-04': ('fixed', 'ECR row: "A push, or a new CVE within the rescan duration (new accounts: [14 days])" (inspector-ecr-rescan-default-14-days-new-accounts).'),
 'claims-05': ('fixed', 'Why now: "so a detective rule judges a configuration that already exists". New sentence after the trigger table: a proactive rule checks before deployment, but [proactive rules do not remediate resources] or block it (config-guide-proactive-vs-detective). Card c007 back: "No. A rule reports noncompliance but does not block the change." The brief-fixed heading stays.'),
 'claims-06': ('fixed', 'A-list cell now: "Repeats: [15 minutes] or [1 hour] possible. New findings: [near real-time]" (both values of the fact; guardduty-eventbridge-new-findings-near-real-time added).'),
 'claims-07': ('fixed', 'q010 explanation (explanation only; stem, options and key unchanged): the reference architecture exports findings [to a central S3 bucket in the Log Archive account] to [retain the findings beyond 90 days]; [GuardDuty is a Regional service] and its findings stay in their Region, so the administrator sets the export in each Region. The old sentence is gone. q010 is no longer shipped (exam-04).'),
 'claims-08': ('fixed', 'Case box year is now 2024, the date of the AWS case study in the corpus case index (2024-02-26); 2018 was the year of the parent company guidelines. The service is named "AWS Security Hub, which [is now available as Security Hub CSPM]". The ellipsis part is not applied: the saved page holds the quoted sentence ending at "levels." (fact security-hub-case-smej-standardized-levels, M3 match; L306 passes).'),
 'claims-09': ('fixed', 'Now: a conformance pack can be [deployed across an entire organization] (config-faq-conformance-pack-org-wide-immutable), or you [use AWS CloudFormation StackSets] (config-faq-aggregation-reporting-only-use-stacksets).'),
 'claims-10': ('fixed', 'Tasks t01 and t02, speak s01 and s02 and all 12 cards set to ready after a clean --ship item lint; sync wrote 3-do.md, 4-say.md and the Look first task region.'),
 'claims-11': ('removed', 'The unlinked sentence about S3 Intelligent-Tiering and S3 One Zone-IA was removed. The card keeps the linked storage-class sentence and adds a linked managed data identifiers sentence.'),
 'claims-12': ('fixed', 'Added: "[Only the management account in an organization] can accept an organization agreement." (artifact-faq-account-vs-organization-agreements).'),
 'claims-13': ('rejected', 'The step sentences must equal the say lines of the detection-hero spec (L703). No display of the named facts stands in steps 3 to 6, so a link needs a spec and brief change in the diagrams stage (orchestrator). The steps hold no number and no absolute word.'),
 'claims-14': ('fixed', 'Partial: the builder comment is removed from 2-deep.md. The detection-before embed needs its spec claim changed (drop "At month 19, ") and the diagram text in brief.json, which belong to the diagrams stage: left for the orchestrator.'),
 'claims-15': ('rejected', 'The Detective change is told in the 2-services.md card with date, old rule and what older questions assume. A Changed recently entry was written in 1-fast.md and then in the B-list, and removed both times: 1-fast.md is at its 1,000-word limit and ' + BUDGET + '. Inspector Classic stays in its card, as exam-09 allows.'),
 'claims-16': ('fixed', 'Trap now: "GuardDuty S3 Protection reads [AWS CloudTrail data events for Amazon S3]."'),
 # technical
 'technical-01': ('fixed', 'Same fix as claims-01.'),
 'technical-02': ('fixed', 'The Keep step now names the built-in route: GuardDuty can [optionally export the generated findings] to S3 (guardduty-export-findings-to-s3). The EventBridge-to-S3 sentence is gone. The Stop and answer now asks about Security Hub CSPM findings (reader-12).'),
 'technical-03': ('fixed', 'Same fix as claims-07. The archived-findings condition is not added: no verified fact holds it, and the key does not depend on it.'),
 'technical-04': ('fixed', 'Same fix as claims-06: both faster values, and new findings reach EventBridge [near real-time].'),
 'technical-05': ('fixed', 'Same fixes as claims-03 and claims-04.'),
 'technical-06': ('fixed', 'Same fix as claims-05.'),
 'technical-07': ('fixed', 'Partial: T108 needs a tag filter or a by-name verify, and list-detectors names nothing, so the verify command stays. Its expect now also asks for aws guardduty list-detectors with an empty list, and to run the cleanup again if an ID shows. fr-0032 closed as unfillable (the only candidate fact is disputed).'),
 'technical-08': ('fixed', 'q005 explanation (explanation only) now says most integrations [are activated automatically], and Macie is the exception to check: you configure it to [also send sensitive data findings] (fact added to q005).'),
 'technical-09': ('fixed', 'Same fix as claims-08.'),
 'technical-10': ('fixed', 'Step 5 expect: some optional protection plans can also show ENABLED, because GuardDuty turns some on automatically (guardduty-first-enable-all-plans-except-runtime added to the task facts). The first still-costs line now names the protection plans that are on.'),
 'technical-11': ('fixed', 's02 line now: "With continuous recording, Config records a configuration item each time the group changes." (config-guide-continuous-or-daily-recording added to s02 facts).'),
 'technical-12': ('fixed', 'GuardDuty cell now: "No, for its foundational sources: it [pulls independent data streams directly]".'),
 'technical-13': ('fixed', 'Step 1 now: "Amazon GuardDuty watches API calls, VPC flow logs and DNS logs [for malicious activity]".'),
 # reader
 'reader-01': ('fixed', 'Same fix as claims-01.'),
 'reader-02': ('fixed', 'Proactive rules are now taught in the Config subsection, right after the trigger table (config-guide-proactive-vs-detective).'),
 'reader-03': ('fixed', 'Partial: 1-fast.md now expands CSPM and says Security Hub CSPM is the original Security Hub, renamed; the real-world box names CSPM. The diagram alt texts and captions (hero, ladder, after) are spec-bound (L702, L703) and keep "AWS Security Hub": a diagrams-stage change.'),
 'reader-04': ('fixed', '"Security Hub CSPM (cloud security posture management) is the original Security Hub, renamed."'),
 'reader-05': ('fixed', 'Cell now: "Yours, against standards such as [AWS Foundational Security Best Practices (FSBP)]".'),
 'reader-06': ('fixed', 'Inspector cell now: "No. Without the Systems Manager (SSM) Agent, it [collects software inventory using Amazon EBS snapshots]". The former-name display is gone from 1-fast.md and from 2-deep.md step 1 (now [AWS Systems Manager Agent (SSM Agent)]).'),
 'reader-07': ('rejected', 'The startup example was cut (238 to 224 words). The rest of the section is the one-breath definition, the required problem field and the hero alt text and steps, which must equal the spec (L702, L703). W201 is a warning.'),
 'reader-08': ('rejected', 'The H3 text is fixed by brief.json (L905), and question and task sections link its anchor. The table and exam signal teach that GuardDuty pulls its own streams.'),
 'reader-09': ('fixed', 'DNS cell: "No, if instances use the AWS DNS resolvers". The Stop and answer now changes another variable: DNS query logging is off; does GuardDuty still get DNS data? (Yes; the resolver is the condition.)'),
 'reader-10': ('fixed', 'Stop and answer now: instance A has the SSM Agent and instance B has none; which finding can come later? (B: agentless scans run [every 24 hours].)'),
 'reader-11': ('rejected', 'A new subsection is not in brief.json (L905, L106; orchestrator). The retention table that duplicated the A-list was removed from the Artifact subsection; the A-list holds the numbers, and q010 is no longer shipped.'),
 'reader-12': ('fixed', 'Stop and answer now asks about Security Hub CSPM findings ([90 days] after the last update; copy them out through EventBridge).'),
 'reader-13': ('fixed', 'Stop and answer now: an access key opens a security group to the internet; which service flags the call (GuardDuty) and which shows the old rules (Config)?'),
 'reader-14': ('fixed', 'Step 5 now defines the behavior graph, [a linked set of extracted and analyzed data] (detective-behavior-graph-definition); "pivot" and "Triage" are gone from 2-deep.md.'),
 'reader-15': ('fixed', 'Partial: the table row now reads "An EventBridge rule and a Lambda function". A Go deeper trace with guardduty-automated-remediation-eventbridge-lambda was written and removed because ' + BUDGET + '.'),
 'reader-16': ('rejected', 'A protection-plans Go deeper was written and removed because ' + BUDGET + '. The fast table now says "for its foundational sources", the fast trap names GuardDuty S3 Protection, and the Macie subsection names Malware Protection for S3.'),
 'reader-17': ('fixed', 'Step 3 now: "Linked Regions send their findings [to a single home Region]"; the Spot the bug says "has enabled".'),
 'reader-18': ('fixed', 'Why now: "The two jobs need different data: Security Hub needs every finding, and Detective needs the activity around one."'),
 'reader-19': ('fixed', 'Say it now ends "The thing to watch is the SSM Agent." (the 25-word Say it limit, L202, blocks the longer line).'),
 'reader-20': ('fixed', 'The Stop and answer was rewritten; the ungrammatical display is no longer used in 2-deep.md.'),
 'reader-21': ('fixed', 'Same fix as claims-06.'),
 'reader-22': ('fixed', 'Partial: "only [your own threat lists] of known bad IP addresses". The ending "Do not let this number decide an answer." is the fixed form of STYLE 11.11.'),
 'reader-23': ('fixed', 'Say it now: "The thing to watch is the file type." The Stop and answer still has to apply it to audio.'),
 'reader-24': ('fixed', 'Partial: "Managed data identifiers (built-in patterns)". Automated discovery is glossed by the sampling Why line below the trace.'),
 'reader-25': ('fixed', 'xref marker to chapter 04 (delegated administrator) on the Delegate step.'),
 'reader-26': ('fixed', 'Items set to ready and synced; the Look first lead sentence that gave away the answer was removed.'),
 'reader-27': ('fixed', 's01 kp5 now "... in one place."; items set to ready and synced.'),
 'reader-28': ('fixed', 'The behavior graph is now defined in 2-deep.md step 5; think-aloud step 4 already says the insight "groups findings but does not trace the activity of one role".'),
 'reader-29': ('fixed', 'Same fix as claims-07.'),
 'reader-30': ('rejected', 'The builder comment was removed. Reasons per rejected option were written and removed: the deep file is at its 2,400-word limit. The before picture is claims-14 (orchestrator).'),
 'reader-31': ('rejected', '"beside its checks" was tried and removed for the 1,000-word fast limit. The link text must hold a display of the fact (L303), and the display contains "also".'),
 # exam
 'exam-01': ('fixed', 'Same fix as claims-01.'),
 'exam-02': ('fixed', 'Same fix as claims-07: guardduty-sra-export-findings-log-archive and guardduty-faq-regional-service ground the explanation; "one setting covers every member account" is gone.'),
 'exam-03': ('rejected', 'The medium template ships exactly 5 core questions and q005 is core, q009 extended (Q201). Each core question is the only one for its service, or half of the required twin pair. q005 stays verified for drills and mocks, with its explanation fixed (technical-08).'),
 'exam-04': ('fixed', 'q007 set to ready (edited-pass), q010 set to verified. q lint 09 --ship: ok, multi 2, twin pairs 1.'),
 'exam-05': ('rejected', 'A stem or option change alters what the blind solvers saw and needs a new verification round (R5); all three lenses agreed on the keys. Listed for the next question revision.'),
 'exam-06': ('fixed', 'Deciding question now: "Reports about AWS (Artifact), a ready-made standard (Security Hub CSPM), or your own rules and history (Config)?"'),
 'exam-07': ('fixed', 'But-not-if now: "patch the instances: AWS Systems Manager Patch Manager" with an xref marker to chapter 38.'),
 'exam-08': ('fixed', 'Partial: the table row names an EventBridge rule and a Lambda function. A Go deeper was removed for the word budget (reader-15); a new question needs a verification round.'),
 'exam-09': ('rejected', 'Same as claims-15 for Detective. Fact guardduty-malware-protection-s3-ga-2024-06 has no changed record, and L107 needs the entry date to equal changed.date of the Now fact.'),
 'exam-10': ('fixed', 'Partial: the row stays in the A-list because card c006 is a number card (C104 needs an A-list fact). The cell now says the interval is for repeats and that new findings arrive [near real-time].'),
 'exam-11': ('fixed', 'Same fix as claims-10.'),
 'exam-12': ('rejected', 'Trap ids and beliefs belong to brief.json (orchestrator). The option still carries a belief close to the trap (Security Hub explains or detects by itself).'),
 'exam-13': ('rejected', 'An option text change needs a new verification round (R5).'),
 'exam-14': ('rejected', 'A stem change needs a new verification round (R5); all three lenses agreed on the key.'),
 'exam-15': ('fixed', 'Same fix as technical-12.'),
 'exam-16': ('fixed', 'q002 explanation now links [on a recurring basis for periodic analysis] (macie-discovery-jobs-targeted).'),
 'exam-17': ('fixed', 'Same fix as reader-22.'),
}
seen = set()
counts = {}
for lens in ('claims', 'technical', 'reader', 'exam'):
    p = D + lens + '.json'
    d = json.load(open(p))
    for f in d['findings']:
        st, res = RES[f['id']]
        f['status'] = st
        f['resolution'] = P + res
        seen.add(f['id'])
        counts[st] = counts.get(st, 0) + 1
    open(p, 'w').write(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
assert seen == set(RES), set(RES) ^ seen
print(counts)
