# IAM chapter: acceptance review, reader lens

Reviewer stance: Tatia as described in `_build/style/READER.md`. She is an AWS Startup SA with an AI/ML background, and English is her second language. She skims first and trusts the gist. She must explain IAM out loud next week.
Files read: `03-iam/1-fast.md`, `2-deep.md`, `3-do.md`, `4-say.md`, `5-quiz.md`, `sources.md`. Spot checks: `facts/iam.md`, `facts/sts.md`, `data/03-iam/cards.json` and the text labels of the IAM diagrams.
Date: 2026-10-12.

## Verdict

The chapter passes for this reader once 4 must-fix items are done. None of them is fatal. The structure is the strongest so far. Every claim links to a fact, every subsection has a Stop-and-answer, and the spoken answers are sayable. What remains is wording: in a few places the chapter teaches advice she would repeat to customers, and that advice contradicts AWS best practice or the chapter's own facts.

## Scores (1 to 5)

| Lens | Score | One-line reason |
|---|---|---|
| Learnability for this reader | 4 | You can finish the fast file, and the headings and tables give a correct gist. Dense 4-column tables and long verbatim link fragments slow an ESL skim. |
| Exam discrimination power | 4 | The twins are good (Q2/Q7, Q3/Q10), deciding phrases are in every question, and distractors are plausible. There is no condition-key question, Q9 is Cloud Practitioner level, and the 5,000-user row teaches the wrong lesson. |
| Technical precision | 3.5 | The facts are grounded, but some framing misleads: IAM users for founders, the MFA Deny recipe, the KMS gist in the fast file, and the "Old" line of the root MFA note. |
| Reusable explanations | 4 | Every subsection has a "Say it" line, and the 4 prompts have 10-second and 60-second answers, a skeleton, Must say and Do not say. Prompt 4 gives advice that goes against best practice. |
| Retention design | 4.5 | Predict, Check, Recap, a Stop-and-answer in each of 13 subsections, 32 cards, twins and Spot-the-bug blocks. |
| Economy | 4 | Within budget: about 1,750 visible words in fast (limit 1,800) and about 5,350 in deep (limit 5,500). Some repetition: the "explicit deny overrides" link appears about 10 times, and FAQ 1, 6, 8 and 9 repeat earlier points. |
| Grounding hygiene | 4.5 | Every hard claim has a link, and the FAQ quotes are verbatim. Two post-2022 changes have no "Changed recently" note (rule 7). |

## Time against the 20-minute claim (1-fast.md)

- First skim (headings, bold labels, table first columns): about 3 minutes. The gist is correct, with one exception: the KMS cell (must-fix 3).
- Full read: about 23 to 26 minutes, not 20.
  - "Look first" says 3 minutes, but opening CloudShell for the first time plus 3 commands and reading JSON takes 4 to 5.
  - "Choose it or not" has 3 tables with about 330 words of linked AWS fragments in 3 minutes. At her reading speed this takes 4 to 5.
  - "Signals and traps" has 236 words in 4 columns in 3 minutes. That is tight but possible.
- Can she finish it? Yes. Each section is short, so she will not stall, but the time label is about 20% low.

## How-it-works subsections: can she explain the mechanism afterwards?

| Subsection | Explains it? | Note |
|---|---|---|
| Every AWS call is a signed request | Partly | The 4 steps are clear. The rest is a grab-bag: eventual consistency, a revocation trap and a shared-responsibility signal. Q9 sends her here to review shared responsibility, but she finds one bullet. |
| Policy statement | Yes | |
| Nothing denies and something allows | Yes | It has the best table in the chapter. The IAM-user-ARN exception inside step 3 breaks the flow and contradicts the ladder figure on a skim. |
| Root user and IAM users | Yes | |
| Role and trust policy | Yes, strong | The AssumeRole walk-through plus the "call fails / next call fails" signal is exactly what she needs with customers. |
| PassRole | Yes | The CloudTrail Stop-and-answer is excellent. |
| Same-account vs cross-account | Yes, strong | |
| External ID | Yes | |
| IAM Identity Center | Yes | |
| Cognito / Roles Anywhere / OIDC | Yes | |
| Condition keys | Mostly | The missing-key rule is taught well. The MFA Deny advice right after it contradicts that rule (must-fix 4). |
| Permissions boundary | Yes | |
| KMS key policy | Yes | The Stop-and-answer answer is "No." plus an indirect trap bullet. Add one sentence on why. |
| Access Analyzer | Yes | |

## Must-fix

1. **Two places advise IAM users for people, against AWS best practice and against the chapter itself.**
   - **Where.**
     - `2-deep.md`, Decision record, "Trade-off" (line 618): "Callvale has one account, so people keep IAM users with MFA until it moves to several accounts with IAM Identity Center."
     - `4-say.md`, Prompt 4: the 10-second answer ("do daily work with your own IAM users") and the 60-second lines "So each of you gets your own IAM user with MFA" and "In your case, with one account, Ana and you each get an IAM user today. When you move to several accounts, IAM Identity Center replaces those users." The source is `data/03-iam/speak.json`, item iam-s04.
     - `1-fast.md` line 126: "IAM user, who uses it: A person or tool without role support".
   - **What is wrong.**
     - The stated reason implies that Identity Center needs several accounts. That reason is not in the fact canon.
     - The advice contradicts `iam-best-practice-human-users-federate-with-identity-center` ("Require your human users to use temporary credentials"; for workforce IAM users "AWS recommends using an identity provider and federating into AWS by assuming roles").
     - It contradicts the chapter's own trap `iam-trap-iam-users-for-people` and the correct answer of Q8 ("daily work ... through identities that use IAM roles").
     - Tatia will say Prompt 4 almost word for word to a real two-founder startup. RULINGS says "if the canon disagrees, keep the decision and change the stated reason."
   - **Fix.**
     - Keep the story decision (IAM users until stage 3), but change the reason to a trade-off that is accepted on purpose. For example: "Callvale accepts IAM users with MFA as a short first step. AWS recommends temporary credentials for people, through IAM Identity Center, and Callvale moves there in stage 3."
     - Rewrite Prompt 4's "In your case" lines so the recommendation to the customer is the AWS one: people sign in with temporary credentials through IAM Identity Center. If they start with IAM users, each user has MFA and the move is planned.
     - In the fast table, change the cell to "A workload or tool that cannot use a role".
2. **The 5,000-user row teaches the wrong lesson.**
   - **Where.** `2-deep.md`, Numbers A-list, the row "5,000 ... A ceiling, not the reason to federate".
   - **What is wrong.** Exam stems with more people than this limit use it as a deciding signal: IAM users cannot cover them, so federate. On a skim, "not the reason to federate" trains her to ignore that signal.
   - **Fix.** Change the decision column to "More people than this cannot each get an IAM user: federate (IAM Identity Center)".
3. **A false gist in a fast-file table cell.**
   - **Where.** `1-fast.md` line 137, "Same account, no deny or ceiling?", identity-based column: "Enough, except for KMS keys: [IAM policies cannot allow access to a KMS key]".
   - **What is wrong.** A skimmer reads that IAM policies never work for KMS. With the default key policy they do. Deep line 489 states this correctly, but the fast file is the one she trusts.
   - **Fix.** "Enough, except for KMS keys: [IAM policies cannot allow access to a KMS key] unless the key policy allows it; [the default key policy enables IAM policies]." Both links go to `iam-kms-iam-policy-needs-key-policy-permission`.
4. **The MFA enforcement recipe fails for access keys.**
   - **Where.** `2-deep.md` line 445, the Stop-and-answer answer in "Condition keys": "To enforce MFA, [specify a Deny statement in any policy] with the condition."
   - **What is wrong.** Five lines earlier the chapter teaches that a missing key makes the condition false. A Deny with `Bool aws:MultiFactorAuthPresent false` therefore does not match requests signed with long-term access keys, because those requests do not carry the key. Those requests pass. She would hand this recipe to customers.
   - **Fix.** Either drop the sentence (the allow-with-condition pattern in the question is already correct), or say "a Deny with BoolIfExists ... false", grounded in `iam-condition-missing-key-is-false-except-ifexists` (IfExists makes a missing key evaluate as true).

## Should-fix

1. **`1-fast.md` time labels.**
   - **Problem.** "Look first" (3 min) and "Choose it or not" (3 min) are each about 1 to 2 minutes low (see the timing section).
   - **Fix.** Retime them to 4 and 5 minutes and cut elsewhere, or trim the tables, so that the 20-minute promise holds.
2. **`2-deep.md` line 33, Exam trap.**
   - **Problem.** "cannot be revoked; revoke the role's sessions" reads as a contradiction on a skim.
   - **Fix.** "You cannot revoke one set of temporary credentials. Use Revoke active sessions on the role: it denies every credential issued before that time."
3. **`2-deep.md` line 99.**
   - **Problem.** The exception that a same-account resource policy granting an IAM user ARN is not limited by a boundary sits inside core step 3. It breaks the 4-check flow and contradicts the ladder figure.
   - **Fix.** Move it to a "Go deeper" block.
4. **`2-deep.md`, first subsection.**
   - **Problem.** The shared-responsibility Exam signal and trap do not belong under "Every AWS call is a signed request", yet Q9 sends her there to review shared responsibility.
   - **Fix.** Give shared responsibility a 3-line block with its own heading phrase, or move it to chapter 01 or 02 and repoint Q9's Review link.
5. **Rule 7, missing "Changed recently" notes.**
   - **Problem.** Two changes since mid-2022 appear only as a date inside a sentence or a table:
     - multiple MFA devices (2022-11-16; old value: one device per user; older questions may assume one);
     - RCPs (2024-11-13; older questions do not know RCPs).
   - **Fix.** Add a note for each.
6. **`1-fast.md` line 185, root MFA note, "Old" line.**
   - **Problem.** The line describes 2024 to mid-2025. Questions older than the 2022 baseline assume that no account type required root MFA.
   - **Fix.** "Old: until May 2024 no account type required it; then management and standalone accounts did, and member accounts did not."
7. **`1-fast.md` line 140, deciding question "If yes, use one".**
   - **Problem.** This is ambiguous for an ESL reader. It is also really the cross-account choice, not the general identity-based vs resource-based choice.
   - **Fix.** "If yes, use a resource-based policy, such as a bucket policy."
8. **`5-quiz.md`: no condition-key question.**
   - **Problem.** aws:PrincipalOrgID, aws:SourceVpce and aws:RequestedRegion have Exam signals in the deep file but no question. Q9 (shared responsibility) has the weakest discrimination.
   - **Fix.** Replace Q9 with a PrincipalOrgID or SourceVpce bucket-policy question. Another option is an explicit cross-reference to the chapter that tests it.
9. **`2-deep.md` KMS Stop-and-answer (line 509).**
   - **Problem.** The visible answer is only "No."
   - **Fix.** Add one sentence: "The key policy does not enable IAM policies and does not name the role, so the role's kms:Decrypt allow has no effect, and Amazon S3 cannot decrypt the object."
10. **`2-deep.md` time box.**
    - **Problem.** "How it works (59 min)" does not match its subsections, which add up to 55.
    - **Fix.** Correct the header, or add the missing 4 minutes for the Try-it blocks to the right subsections.
11. **`3-do.md` Verify steps (iam-t02 and iam-t03).**
    - **Problem.** `resourcegroupstaggingapi get-resources` is used to prove that an IAM role is gone. The saved corpus does not show that this API returns IAM roles. If it does not, the check always shows an empty list and passes even when the role still exists.
    - **Fix.** Add or replace the check with `aws iam get-role --role-name saa-iam-t02`. Expect: a NoSuchEntity error.
12. **Small ESL wording fixes.**
    - **Problem.** In `2-deep.md` line 79, "What comes first?" is unclear.
    - **Fix.** Write "What must you do first?"
13. **`2-deep.md` line 175, low priority.**
    - **Problem.** When a trust policy names the account rather than the principal, the caller's own sts:AssumeRole allow is needed in the same account too. The text says "Across accounts" only.
    - **Fix.** Add a "Go deeper" line if a fact supports it.

## What works and must be kept

- Assertion headings that are true on their own, for example "Same-account access needs one allow but cross-account access needs two".
- The "Say it: The short answer is ... The thing to watch is ..." frame in every subsection. It is predictable, and that is good for speaking under stress.
- The Stop-and-answer items test what a skim misses:
  - the boundary with s3:*;
  - the expired password with a working access key;
  - the CloudTrail PassRole search;
  - the cross-account SQS queue.
- The quiz shows deciding phrases, think-aloud in the worked examples, a twin and a takeaway on every item, and 3 multiple-response questions.
- The hands-on tasks are secure and tagged, cost $0, and include a fallback for readers without permissions (simulate-custom-policy).
