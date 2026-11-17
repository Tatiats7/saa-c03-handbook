# Exemplar judgement: plain-language editor lens

Judge: editor (plain language for a second-language reader). Read order: B, A, C.
Files read in each attempt: `03-iam/1-fast.md`, `03-iam/2-deep.md`, `10-vpc/2-deep.md`, `data/03-iam/{questions,speak,tasks}.json`, `diagrams/` (rendered previews under `_build/tmp/diagram-preview/`), `_build/work/03-iam/attempt-notes.md`, and the lint reports already in `_build/reports/lint/03.json`. I did not run sync or lint again, so no attempt folder was changed.

Lint does not separate the three attempts. All three fail on the same structural rules: L201 (deep word count), L106 (stubs without a Stop and answer, FAQ 5/10) and L903 (planned stubs). Each attempt has only a few W202 long-sentence warnings, and the sentence average is 8.2 to 8.6 words. The differences are in what lint does not catch: idioms, terms with no definition, wrong fact links, and whether the device teaches anything. I counted these by hand below.

## Scores (1 to 5)

Criteria in order: learnability, exam discrimination, technical precision, reusable explanations, retention design, economy, grounding hygiene.

| Attempt | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Sum |
|---|---|---|---|---|---|---|---|---|
| A (first principles) | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 27 |
| B (exam operator) | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 26 |
| C (customer conversation) | 3 | 4 | 3 | 4 | 4 | 3 | 3 | 24 |

Ranking: **A, B, C**. A and B are close. A wins on criterion 1, which matters most for this reader: its tables tell her the rule when she only skims. A also has the fewest STYLE violations. C has the best idea for spoken answers, but it has the most idioms and the weakest technical precision.

Fatal technical defects: none. Each attempt has wrong fact links or imprecise phrases, and each one can be fixed in one sentence.

## STYLE violation counts (by hand, prose and data items)

| Type | A | B | C |
|---|---|---|---|
| Idiom, metaphor or unclear phrasal verb (STYLE 3) | 1 | 5 | 7 |
| Abbreviation used without expansion in the file (STYLE 2) | 2 | 0 | 2 |
| Pricing table or price detail the exam does not need (STYLE 3) | 1 (table) | 1 (bullets) | 1 (table + partial-hour line) |
| Heading with commas removed, hard to parse (STYLE 5) | 0 | 2 | 1 |
| Fact link whose fact does not support the sentence | 2 | 1 | 0 |
| Unsupported advice or absolute without a link | 1 | 1 | 2 |
| Unclear or wrong sentence | 2 | 2 | 3 |
| Story that teaches the answer (RULINGS: story never teaches) | 0 | 0 | 1 |
| **Total** | **9** | **12** | **17** |

## Attempt B (exam operator)

**What works for her.**
- Each full subsection opens with the decision and the stem phrase that settles it: "When a stem says that a user fails to assume the role, fix the trust side. When the session gets access denied, fix the permissions side." This is the best exam device of the three, and q002/q006 test exactly this split. It is the only true twin pair (one changed phrase, different key) that follows STYLE 7.
- The "Why does AWS work this way?" paragraphs give her sentences that she can say to a customer: "If a broader allow could cancel that Deny, the guardrail would fail on the day someone attached AdministratorAccess." "Time limits the damage." These are short, causal and adult.
- The fast file is clean. Each of the four compare tables ends with a deciding question. The signals table has a strong "but not if" column: "the stem says "grant": an SCP grants nothing".
- The VPC "Spot the bug" (a NAT gateway in a private subnet) is a good anti-skim item.
- The speak items sound like speech: "The SDK in your code finds them, so no key sits in the code."

**Defects (quoted).**
- Grounding: "A service control policy (SCP), a permissions boundary and a session policy each set a ceiling. When all of them apply, the request is [allowed only if all three policy types allow it](...#iam-scp-boundary-identity-all-must-allow)." The linked fact is about SCP + boundary + identity policy, not session policy. The sentence claims more than the fact says.
- Idioms: "Role questions turn on one split"; "Many access questions hide one decision"; "older practice questions know no other pattern" (unclear meaning); "A role that you forget is still an open door" (task); "Three stem phrases send you here".
- Unclear: "Predict 3 misses the role side." This is a fragment, and a stressed reader cannot decode it.
- Headings with commas removed: "A policy statement names an effect actions resources and conditions", "Conditions add network MFA and organization checks to a statement".
- VPC quotes a past-tense pricing example as fact: "[There was no charge for the data transfer from the EC2 instance to S3]". Hourly and per-GB prices are in the prose, but the exam does not need them.
- Retention: the Try task (iam-t02) teaches the role's maximum session setting, which is a B-list number. It does not teach the deny rule, which is her real weakness (Secure 45%). On a CloudShell role session, the 12-hour request also fails because of role chaining, so the "explain" can mislead.
- No think-aloud with a wrong path. STYLE 7 requires one per deep chapter.

## Attempt A (first principles)

**What works for her.**
- The trace-then-table pattern is the best skim device in the three attempts. "Now follow one request through four checks" gives four bold one-word steps (Collect, Look for a deny, Check every ceiling, Find a grant). A truth table follows: "| 3 | Allows EC2 | Allows the action | Silent | Implicit deny |". The cross-account table "| Other account | Allows | Silent | Deny |" carries the whole rule even if she reads nothing else. This meets READER.md: "Headings, tables and captions must give a correct gist on their own."
- The headings are full claims in plain words, with no punctuation lost: "Same-account access needs one allow but cross-account access needs two".
- The Stop and answer prompts apply the rule to a new case, as STYLE 5 requires. One sends a Lambda function to an SQS queue across accounts ("The role's identity-based policy allows sqs:SendMessage on queues in account A"). Another tests the NACL ephemeral port range on Amazon Linux. She cannot copy either answer from the paragraph above.
- The Try task matches her weakest domain: the policy simulator shows `explicitDeny`. The next step is the fix ("No new allow can fix an explicit deny"), in the order that STYLE 8 requires.
- It is the only attempt that applies the "not examinable yet" rule: "(2026-08-19) A higher default quota of managed policies per role ... Do not let this number decide an answer."
- Twin pair q001/q005 ("EC2 instances in one AWS Region" versus "servers in the company's data center") is clean, and its exam_english tags are filled.

**Defects (quoted).**
- Wrong fact link: "> **Key fact:** [An explicit deny in any of these policies overrides the allow](../facts/sts.md#sts-session-policy-intersection)". The fact is about session policies, so this is the wrong fact for a general rule.
- Weak source: "[Traffic that crosses an Availability Zone boundary typically incurs a data transfer charge](...#vpc-blog-same-az-free-cross-az-charged)". The quote is from a blog and says "typically". Chapter 01 rejected a blog quote for this reason. Use a docs fact such as `vpc-natgw-cross-az-transfer-charge`.
- Pricing table in VPC ("| Charge | Example rate in US East (Ohio) |"). STYLE 3 says "no pricing tables".
- Idiom: "Across two accounts, each owner has a say."
- Abbreviations used without expansion: "SCPs and RCPs" (RCP is never expanded in the file); "worker runs in AZ 2".
- The Changed recently entry has a confused Old line: "**Old:** the default quota rose [from 10 to 20]". The Old line must give the old value.
- Imprecise: words table "An identity that hands out temporary credentials" (AWS STS issues the credentials, not the role); truth table "Allows EC2" (it should say "Allows EC2 only"); "Deny" in the cross-account table where the term is "implicit deny".
- An unsupported mechanism step: "A stranger tries to connect ... the NAT gateway has nowhere to send it." A flagged it as needs-display, which is honest, but B already had a usable fact (`vpc-natgw-connections-originate-inside-vpc`).
- Reusable explanation is the weakest of the three. The prose teaches the rule well but rarely gives her the sentence for a customer. "Start with the problem." repeats as a label and does not add a sayable line.
- No think-aloud with a wrong path.

## Attempt C (customer conversation)

**What works for her.**
- Each subsection uses the four spoken moves as run-in labels ("The short answer. An allow is not enough. AWS needs one allow, no explicit deny, and permission from every limit that applies."). Reading the book becomes practice for the spoken answer. Criterion 4 is strongest here.
- It is the only attempt with the required think-aloud with a wrong path (q001): "My first idea breaks because a job in a role session has only the role's permissions and cannot write to its own bucket".
- The VPC Stop and answer prompts have the best discrimination in all three attempts. One is the tracked SSH session that survives a security group change. The other is the cross-zone NAT case, which ends "A gateway endpoint does not help, because the repository is not S3 or DynamoDB."
- Precise points that the other two attempts miss: "you [cannot set a permissions boundary for the root user]" (fast table and q004); the AKIA/ASIA prefix for reading logs; signals row "more than 5,000 employees need access" with the fact behind it.

**Defects (quoted).**
- The story teaches the answer: Ben asks "Why does the delete still fail?" The answer depends on a fact that he did not give: "Earlier, Ben added a Deny for object deletes on the audio bucket, as a safety net." The reader cannot reason to this answer, and the scene breaks the rule that the story never teaches.
- Idioms and metaphors: "EC2 has no bucket-style door", "as a safety net", "Why would I ever touch a network ACL?", "You cannot take back issued credentials early", "hops through two roles", "One NAT gateway lives in one zone", "the large audio transfers then skip the NAT gateway".
- Imprecise: "The role hands out keys that expire". Speak s01 says "the role's permissions are now the only limit" (SCPs and boundaries still limit). The hero diagram draws the IAM role as an actor that sends "Credentials" to the app and leaves out AWS STS. It shows only the success path, and it has a size-budget warning ("will scroll on a phone beyond 448").
- A term with no explanation: "Every other packet meets the asterisk rule."
- Unsupported advice: "Keep traffic inside the Region where you can". Signals cell: "a third-party tool cannot use roles" (a "cannot" with no link).
- Abbreviations used without expansion: "AZ 1", and "OU" in the fast table.
- Economy: three Exam trap callouts in a row in one subsection. A "What does it cost? no additional charge" row on the firewall table. "Each partial NAT Gateway-hour consumed is billed as a full hour". The STS 600 requests per second quota on the B-list. The "Ben asks" frame adds words to every subsection, and her time budget pays for them.
- Twins q001/q006 change the whole task, not one phrase. The Try task (iam-t02) has no fix step after the break step.

## Shared defects (fix whatever is chosen)

- Every task has `"checked": "2026-10-12"`, which is later than the build date (2026-10-11).
- No attempt gets a role ARN in the verify step without the Resource Groups Tagging API, and all three note that it is unknown whether that API lists IAM roles. Use `aws iam get-role` with the expected NoSuchEntity error, or a `list-roles` query on the `saa-` prefix.
- The respelling "least privilege (leest PRIV-ih-lij)" respells a common word. Keep respellings for words that she can mispronounce (STYLE 4).

## For the synthesis

**Winner: A.** Ideas to graft onto A:

1. From B: one "Why does AWS work this way?" paragraph per full subsection, of 2 or 3 sentences, after the truth table ("Time limits the damage."; the guardrail-survives-AdministratorAccess reason; "Neither owner can give away the permission of the other owner").
2. From B: a stem-phrase line per subsection ("AssumeRole fails: fix the trust policy. The session fails later: fix the permissions policy."). Put it after the term is defined, not before.
3. From B: the q002/q006 twin pair (trust side versus permissions side). Also the VPC Spot the bug (NAT gateway in a private subnet), and the NAT "how many" decision ("One NAT gateway is the low-cost answer. One in each zone is the high-availability answer").
4. From C: the think-aloud with a wrong path (C q001), which STYLE 7 requires. Neither A nor B has one.
5. From C: a closing "Say it" line per subsection that uses the four starters ("The short answer is ...", "The thing to watch is ..."). Use it as a one-line rehearsal, not as the whole structure.
6. From C: the two VPC Stop and answer prompts (tracked connection survives a security group change; cross-zone NAT where the gateway endpoint does not help). Also the root-user row: you "cannot set a permissions boundary for the root user", with question q004 (an SCP Deny that reaches the member root user).
7. From C: the trust/permissions compare table with a "Callvale's worker role" row, and the AKIA/ASIA prefix line in a Go deeper block.
8. From C: speak s02 (bucket policy or cross-account role) with its KMS check-back question.

**Must-fix defects of A:**

1. Replace the Key fact link `sts-session-policy-intersection` with `iam-eval-explicit-deny-overrides-allow`.
2. Replace the blog-sourced cross-AZ fact with a docs fact (`vpc-natgw-cross-az-transfer-charge` or `vpc-natgw-same-az-reduces-charges`).
3. Remove the pricing table in VPC. Keep the three charge dimensions as a list without prices, or drop the Ohio prices.
4. "each owner has a say" becomes "each owner decides for its own side".
5. Expand RCP (resource control policy) and AZ (Availability Zone) at first use, or write the full term.
6. Rewrite the Changed recently Old line: "Old: 10 managed policies per role by default."
7. Truth tables: "Allows EC2" becomes "Allows EC2 only"; "Deny" becomes "Implicit deny" in the cross-account table.
8. Words table: "An identity that hands out temporary credentials" becomes "An identity with permissions and no long-term keys; AWS STS issues its temporary credentials."
9. Ground the NAT "stranger tries to connect" step with `vpc-natgw-connections-originate-inside-vpc`, and remove the needs-display marker.
10. Add the think-aloud with a wrong path (graft 4) and fix the task `checked` dates.
