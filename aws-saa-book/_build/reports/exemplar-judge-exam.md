# Exemplar judge: exam lens

Judge: AWS certification exam-preparation expert (SAA-C03 item construction: scenario, constraints, one qualifier, four plausible options).
Read order: b, c, a. Files read in each attempt: `03-iam/1-fast.md`, `03-iam/2-deep.md`, `10-vpc/2-deep.md`, `data/03-iam/{questions,speak,tasks}.json`, the `iam-hero` diagram preview, `_build/work/03-iam/attempt-notes.md`. Lint results were read from each attempt's stored output and not re-run, so no attempt was changed. All three fail lint only on structure: planned subsections with no Stop-and-answer, FAQ count and deep word count. No attempt has an L8xx grounding error. So the grounding differences below are semantic: a link that does not support its sentence, or a claim with no link.

## Scores (1 to 5)

Criteria in order: learnability, exam discrimination, technical precision, reusable explanations, retention design, economy, grounding hygiene.

| Attempt | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Total |
|---|---|---|---|---|---|---|---|---|
| A (first principles) | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 27 |
| C (customer conversation) | 4 | 4 | 3 | 5 | 4 | 3 | 4 | 27 |
| B (exam operator) | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 25 |

**Ranking: A, C, B.** A and C tie on total. A wins the tie on the two things this lens weighs most: realistic items and technical precision. READER.md says "A wrong fact is worse than a missing one", and C has a scenario that contradicts its own trust policy (below). No attempt has a fatal technical defect.

## Attempt B (exam operator)

**What works for the exam.**
- Each deep subsection opens with the stem phrase that decides it. This is the best anti-rushing device of the three: "Many access questions hide one decision: allowed or denied. Three kinds of stem phrase decide it." / "When a stem says that a user fails to assume the role, fix the trust side. When the session gets access denied, fix the permissions side."
- The best twin pair in any attempt, q002/q006. Both stems are the same up to one clause: "the call fails with an access denied error" against "the call succeeds, but the next call to read a report fails". This is exactly how real items separate trust policy from permissions policy. q006 option c, a bucket policy naming the development account, is a smart distractor: "Inside the session the caller is the role, not the developer."
- The "why" paragraphs explain the rules instead of listing them, and she can say them to a customer: "If a broader allow could cancel that Deny, the guardrail would fail on the day someone attached AdministratorAccess."
- Useful traps that come from real wrong beliefs: an empty SCP "is not neutral", and "An account ARN that ends in `:root` is not the root user alone."
- The VPC sample has the strongest exam framing: "One NAT gateway is the low-cost answer. One in each zone is the high-availability answer, and older practice questions know no other pattern." It also has a Spot-the-bug with the NAT gateway placed in a private subnet.
- Task iam-t02 has a real break-it step: ask for a session longer than the role maximum.

**Defects.**
- Grounding mismatch. "A service control policy (SCP), a permissions boundary and a session policy each set a ceiling. When all of them apply, the request is [allowed only if all three policy types allow it]". The quote behind `iam-scp-boundary-identity-all-must-allow` names SCP, boundary and *identity-based policy*, not session policy. The link supports a different claim from the sentence.
- q003 (cross-account, "In the same run") builds the signal "keep its own permissions" but offers no role-in-account-B option. So the signal is never tested. The qualifier "MOST secure" only removes the IAM-user option. The twin admits as much: "a role in account B also fits".
- q004 ("Which statements about the role are correct?", difficulty 1) is a trivia item, not SAA register. Option e ("stay valid until an administrator deletes them by hand") is a throwaway.
- q005 (block deletes on an audit bucket): a real exam would very likely include S3 Object Lock as an option. The item needs either that distractor with a reason, or a stem that rules it out.
- The MFA signal row's "But not if" is muddled: "the caller uses long-term access keys: they lack it". That row should point to GetSessionToken with MFA, not stop at a dead end.
- Unlinked claims in Changed recently: "MFA on the root user of a member account was a best practice, not a requirement" and "AWS still recommends them".
- Exam trap: "Temporary credentials cannot be revoked one by one … so you change the policy instead." This never names the console action "Revoke active sessions", which is the exam-facing answer for leaked role credentials.
- Only 3 of 12 deep subsections are written, the same as the others. The two diagrams (B's and A's) are near-identical generic STS sequences.

## Attempt C (customer conversation)

**What works for the exam.**
- The best signals table. Its "But not if" guards are real exam discriminators, not filler: "one policy allows, another denies → the deny wins | the Deny has a condition that the request does not meet"; "more than 5,000 employees need access → federation through IAM Identity Center"; "find buckets shared outside the account → IAM Access Analyzer | the stem asks who made a call: AWS CloudTrail"; "no one, including administrators, can → SCP with a Deny | the principal is in the management account".
- The three-column grant/ceiling table has a root-user row that the exam does test: "you cannot set a permissions boundary for the root user", while an SCP reaches it "including the member account's root user".
- Question q001 has a worked think-aloud with a wrong path: "I read the last sentence first … Before I look at the options, I predict a cross-account role … My first idea breaks because…". This is the best device in any attempt for a reader who rushes stems.
- Good items:
  - q003: the boundary blocks a write and the fix is MOST secure. Options are "add PutItem on one table to the boundary", "remove the boundary" and "SCP".
  - q004: an SCP Deny that includes the root user. The distractor "boundary on every user and role" fails because a boundary cannot reach root.
  - q005: a same-account SQS queue policy alone, with the careful guard "The execution role has no permissions boundary".
  - The q001/q006 twin, S3 bucket policy against EC2 cross-account role: "Amazon EC2 does not support resource-based policies".
- Criterion 4 is clearly the best of the three. Every subsection is an answer she can say to a founder: "**The short answer.** For S3, both work. A bucket policy lets the caller stay in its own account. A role moves the caller into the other account." The speak follow-up "Is the source data encrypted with a KMS key?" is how a senior SA talks.
- It covers more examinable content than the others: KMS cross-account in Go deeper ("neither policy alone is sufficient"), RCPs, and AKIA/ASIA prefixes.

**Defects.**
- Self-contradiction on the exact discrimination the chapter teaches. The role subsection shows a trust policy with `"Principal": {"Service": "ec2.amazonaws.com"}` and the table row "Callvale's worker role | The EC2 service can assume it". Its Stop-and-answer then says: "A developer assumes the worker role from her laptop with the AWS CLI … What happens after about one hour". With that trust policy, the developer's AssumeRole fails at once. A reader who absorbs this learns the wrong model of trust policies. B uses the same setup correctly as an access-denied question. This is a must-fix, but not fatal, because no AWS fact is false.
- Exam trap: '"Revoke the temporary credentials" is not a real action.' The console's "Revoke active sessions" is real and is a likely correct option on the exam. The trap could teach her to reject it. Reword it around the revoke-sessions fact, as A does.
- q001 gives away its discriminator: "The job must keep the permissions of its own role during the copy." Real stems imply this ("copy into its own bucket in the same run"); they do not state it.
- q004 has the same Object Lock exposure as B q005. Distractor c ("review the bucket policy every day") is a strawman.
- Economy: it is the longest deep file (2,852 words), with three Exam traps in a row in one subsection. The meta line "Each subsection starts with the question a founder asks you…" spends words.
- VPC grounding: several table cells carry hard claims with no link: "A gateway endpoint for S3 and DynamoDB" and "Standard transfer charges on top of processing".
- The hero diagram, showing the instance-profile path, is the most exam-relevant picture. But it is over the size budget ("warn size-budget: the drawing is 418 wide; size 's' allows 393").

## Attempt A (first principles), the winner

**What works for the exam.**
- The most realistic question set, in true SAA register:
  - q001/q005 is a twin pair: an instance profile on EC2 against IAM Roles Anywhere on premises. The same bait sits in both stems ("The company also runs a private certificate authority"). This is a classic keyword-bait design. The distractor "Move the application to Amazon EC2 instances" is the correct "works but violates the qualifier" type.
  - q003 is a "Which combination of steps … MOST securely? (Select TWO.)" item with a wildcard-principal distractor, which is exactly real exam form.
  - q006 tests the half of cross-account trust that people forget. The trust policy names the account, but the auditors lack `sts:AssumeRole`. Two distractors probe real misconceptions: "add the auditors group … as a principal" (a group cannot be a principal) and an external ID as keyword-bait for two accounts of one company.
  - q002 includes the common belief that root escapes the SCP: "Sign in as the root user of the member account".
- Truth tables turn the rules into cases she can drill. The four-case SCP/identity/bucket table ("3 | Allows EC2 | Allows the action | Silent | Implicit deny") and the same-account against cross-account table are the best discrimination drill in any attempt.
- It is the most precise:
  - It gets revocation right: '"revoke sessions" adds an inline policy that [denies all permissions to all actions] for credentials issued earlier'.
  - It has the fine-grained same-account boundary exception: "a resource-based policy that [grants permissions to an IAM user ARN is not limited by an implicit deny] in a boundary".
  - It marks a recent quota change "not examinable yet" ("Do not let this number decide an answer"), which applies RULINGS rule 7 correctly.
- Its Stop-and-answers change one variable in a way the exam does: "The role's identity-based policy allows sqs:SendMessage on queues in account A" fails across accounts on the resource ARN, not the action. The VPC sample has the Amazon Linux ephemeral range 32768-61000.
- The signals table covers Cognito identity pools ("mobile app users upload directly to S3"), Roles Anywhere, Access Analyzer against CloudTrail, and external ID against plain trust.

**Must-fix defects of A (for the synthesis).**
1. Recap 3 says "Which **three** policy types limit access but never give it? SCPs, permissions boundaries and session policies." A's own Collect step names RCPs, which never grant either. Make it four, or scope the question to identity-side ceilings.
2. The Key fact "An explicit deny in any of these policies overrides the allow" is linked to `sts-session-policy-intersection`, a session-policy page. Relink it to `iam-scp-boundary-identity-all-must-allow`, which has the same sentence in the right context.
3. The Changed recently Old line is not an old value: "**Old:** the default quota rose [from 10 to 20]". It should read "10 managed policies per role". The root-MFA Old line ("first for management accounts, then for standalone accounts") has no link. Link it to the change fact's `was` evidence.
4. VPC: the cross-AZ charge is grounded in a blog fact (`vpc-blog-same-az-free-cross-az-charged`). Replace it with the documentation fact `vpc-natgw-cross-az-transfer-charge`, which B uses.
5. Deep subsections open with "Start with the problem", never with the stem phrase. Add B's one-line stem opener to each pass-route subsection. Without it, the traces teach the mechanism but do not train her to find the constraint first, which is READER.md's explicit need.
6. The signals table lacks three high-frequency rows: an explicit Deny (with C's guard "the Deny has a condition the request does not meet"), the MFA condition key, and "more than 5,000 users → Identity Center". The fast file has room for at most two of them, so swap out the Cognito row or merge it into the Identity Center row.
7. The cross-account truth table says "Deny" where it means "Implicit deny". Keep one term per concept (STYLE).
8. The decision record does not mark the chosen option. B and C bold it.
9. Criterion 4 is weakest here. The deep prose explains the mechanism but gives few sentences she can say to a customer. Add C's "The short answer." line (one or two spoken sentences) after the stem opener in each pass-route subsection.
10. Only 6 questions and no worked think-aloud. Add C's worked-solution format to at least the core items.

## Ideas to graft onto A

From B:
- The stem-phrase opener per subsection ("Three kinds of stem phrase decide it").
- The "Why does AWS work this way?" paragraph: a deny wins because a guardrail must survive AdministratorAccess, and a ceiling cannot grant because an SCP is written far from the workload.
- Twin pair q002/q006 (AssumeRole fails → trust policy; session fails → permissions policy). Keep it next to A's q006 so that both halves of cross-account trust are tested.
- Traps: empty SCP = deny all; `:root` principal = the whole account; a member root user cannot remove an SCP (FAQ 3).
- Task iam-t02's break-it step: ask for more than the role maximum.
- The NAT bill's three parts, with the line "older practice questions know no other pattern", and the NAT-in-private-subnet Spot the bug.
- The A-list "Why it decides an answer" column wording ("A full working day fits; a longer one does not").

From C:
- The signals rows with their guards (Deny with a condition, management account, 5,000 users, CloudTrail against Access Analyzer, MFA console-only).
- The three-column grant/ceiling table with the root-user row.
- The worked think-aloud with a wrong path (`worked.steps`, `wrong_path: true`).
- Items q003 (fix the boundary, MOST secure), q004 (SCP Deny including root, where the boundary cannot reach root), q005 (same-account queue policy alone, with the "no permissions boundary" guard) and the EC2-cross-account twin q006.
- The "The short answer." spoken line and the speak follow-up about KMS.
- KMS cross-account in Go deeper; RCPs; AKIA/ASIA.
- `exam_english` tags on every item.
- The instance-profile hero diagram, resized to budget. It shows the most-examined IAM scenario better than the generic STS sequence.

## Examinable IAM content missing or only "Planned" in all three

All three leave these as stubs, so the synthesis must make sure the full chapter covers them:
- `iam:PassRole` and privilege escalation; service roles against service-linked roles.
- **Lambda resource-based (function) policies** that let S3, SNS or API Gateway invoke a function. Every attempt's list of resource-based policies leaves this out, and it is frequent on the exam.
- Condition keys in stems: `aws:PrincipalOrgID` (organization-only bucket access), `aws:SourceVpce` / `aws:SourceIp`, `aws:SecureTransport`, `aws:RequestedRegion`; tags and ABAC; VPC endpoint policies.
- MFA-protected API access through GetSessionToken. B's MFA row stops short of this.
- Federation: IAM Identity Center permission sets, SAML 2.0 with Active Directory (AD Connector), Cognito user pools against identity pools (only A, and only as a signal row).
- External ID and the confused deputy, beyond one signal row.
- "Revoke active sessions" for leaked role credentials (only A).
- Credential report, last-accessed data, Access Analyzer policy generation, the policy simulator as a process.
- Root-only tasks and centralized root access for member accounts.
- The S3 interplay that cross-account items keep touching: Object Ownership / bucket-owner-enforced for cross-account writes, Block Public Access against a wildcard principal, and S3 Object Lock as the "no one, including root, can delete" answer. Both B q005 and C q004 are exposed to Object Lock.
- An xref to IAM database authentication for RDS, and to Secrets Manager for credentials that must exist.
