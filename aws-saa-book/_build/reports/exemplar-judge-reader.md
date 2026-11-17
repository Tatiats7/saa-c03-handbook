# Exemplar judge: the reader lens

Judge: the reader of READER.md. She skims first, forgets terms under stress, stops at long text, and next week must explain IAM out loud.
Read in the order a, b, c: `1-fast.md`, `2-deep.md` (IAM and VPC), questions, speak, tasks, hero diagram, brief, notes.
Lint: I read each attempt's own `_build/reports/lint/03.json`. Each report is newer than the attempt's Markdown, so I did not re-run sync or lint, and I changed no attempt. None of the three has a fact-link error. All remaining errors are slice-structural (L201 word count, L106 Stop-and-answer on "Planned" stubs, L101 missing generated files). So my grounding scores come from reading the text and checking facts by hand.

## Verdict

| | Learn | Exam | Precision | Say it | Retention | Economy | Grounding |
|---|---|---|---|---|---|---|---|
| **C** customer conversation | 4 | 5 | 4 | 5 | 4 | 3 | 4 |
| **A** first principles | 4 | 4 | 4 | 3 | 4 | 4 | 4 |
| **B** exam operator | 3 | 4 | 4 | 4 | 3 | 3 | 3 |

**Ranking: C, A, B.** No attempt has a fatal technical defect. Each one has fixable precision slips, listed below.

Why C wins for this reader: C is the only attempt in which reading the chapter is rehearsing the job she has next week. Every deep subsection opens with a founder's question and then runs the four spoken moves: "**The short answer.** … **How it works.** … **The thing to watch.** … **In your case.**" Its questions also discriminate best. A is the cleanest and shortest, and it is the one I would most surely *finish*. But A teaches me to reason, not to talk, so after reading A I could pass the question but I could not yet say the answer to Ben.

## The skim test (headings and tables only)

What I learned from 60 seconds of skimming each deep file:

- **A** gave the best gist. "Same-account access needs one allow but cross-account access needs two" is a complete exam rule in one heading. "AWS allows a request only when nothing denies and something allows" is also correct. The 4-case table (SCP / identity / bucket / result → Allow, Implicit deny, Implicit deny, Explicit deny) answers questions without the prose.
- **B** misled me once. The heading "A resource-based policy names the principal and opens cross-account access" says, at a glance, that the bucket policy alone opens the door. That is exactly the trap the chapter warns against two pages earlier ("A bucket policy that names a role in another account is enough" is listed as a wrong belief). "An explicit deny wins and ceilings never grant access" is excellent.
- **C** was correct but vague in one place. "Identity-based and resource-based policies combine differently across accounts" says *that* they differ, not *how*. "AWS denies a request unless a policy allows it and no policy denies it" leaves out the ceilings. The fast-file table "Who grants and who only limits" was the best skim object in all three attempts. Its root-user row ("Yes, including the member account's root user" / "No: you cannot set a permissions boundary for the root user") gave me a fact I had not known.

## Attempt A: first principles

**What worked for me.**
- Short numbered traces, one line per step, then a table that compresses them. In VPC: "Now follow one HTTPS request … and then its reply", then "Every difference that the exam tests follows from this trace." I remembered why a NACL needs the ephemeral range, not just that it does.
- The Stop-and-answers make me run the trace on a new case. One example: "Its permissions boundary allows s3:GetObject and nothing else … Can the role upload an object with s3:PutObject?" Another is the NACL 5432 case, which uses the Linux ephemeral range.
- The questions have a true twin pair: q001 (EC2 → instance profile) and q005 ("servers in the company's data center" → IAM Roles Anywhere). Only one phrase changes. This is exactly the "find the constraint in the stem" training she needs. q006 (the trust policy names the account, but the auditors' group has no `sts:AssumeRole`) is a very good discriminator.
- The Check answers close every Predict explicitly: "Predict 3 is No: across accounts …".
- Changed recently gives exam advice I can act on: "Do not let this number decide an answer."

**Where I got bored or lost.**
- "Start with the problem." opens all five full subsections word for word. By the third time I skipped it.
- The deep body gives me rules, but no sentences to say. The speak items are good ("The short answer is: you give the instance an IAM role instead of a key."), but they live only in JSON, away from the prose.
- In the numbers table, "[only one role can be assigned to an instance at a time]" sits in the *Number* column, which is not a number. It broke my scan of the table.
- In the fast file, Changed recently spends 4 lines on a quota change (managed policies per role, 10 to 20) that is "not examinable yet". That is padding in the 15-minute file.

**Precision.**
- The Key fact "An explicit deny in any of these policies overrides the allow" links `sts-session-policy-intersection`. That quote is about identity, session and resource-based policies, but A places it under an SCP / bucket-policy table. Use `iam-eval-explicit-deny-overrides-allow` instead.
- Otherwise exact. q003 (multi-select, wildcard principal makes the bucket public) and q004 ("Fix an explicit deny by removing it") are correct and sharp.

## Attempt B: exam operator

**What worked for me.**
- "Why does a deny win? A security team writes a Deny to stop one action permanently. If a broader allow could cancel that Deny, the guardrail would fail on the day someone attached AdministratorAccess." This is the best customer explanation in all three attempts. Its partner, "Why can a ceiling not grant? An SCP is written … far from the workload", is almost as good.
- The trust/permissions split, said as a stem rule: "When a stem says that a user fails to assume the role, fix the trust side. When the session gets access denied, fix the permissions side." The twin pair q002/q006 tests exactly this and nothing else. It is clean.
- Precision gems: "An account ARN that ends in `:root` is not the root user alone". "A security group can name another security group as its source". The NAT spot-the-bug ("creates a NAT gateway in a private subnet").
- Speak s02 (SCP compared with permissions boundary) is the compare prompt I will most likely be asked.

**Where I got lost.**
- The meta openings: "Many access questions hide one decision: allowed or denied. Three kinds of stem phrase decide it. 'Denies' points to an explicit deny. 'The SCP allows' or 'a permissions boundary' points to a ceiling." This is stem advice about terms I have not met yet in this subsection. I skipped it, and then I had to come back to it.
- Some cells are too terse to understand. One is "the caller uses long-term access keys: they lack it" (in the MFA row). Another is the Check 3 answer "Predict 3 misses the role side.", which does not say yes or no.
- The fast file has four compare tables plus eight signals. Under stress, that is too many matrices in one sitting.
- The skim-misleading heading noted above.

**Precision.**
- q005 has a weak key. Developers who "have the AdministratorAccess managed policy" can detach the Deny from the Developers group themselves. "Make sure that no developer can delete" is therefore not guaranteed by option a, and an exam-validity solver would argue for d. C's q004 tests the same idea correctly.
- Ceiling check, step 2: "A service control policy (SCP), a permissions boundary and a session policy … the request is allowed only if all three policy types allow it". The linked fact is about SCP + boundary + *identity-based* policy, so the "three" are different things.
- Recap 2, "Deny first, then every ceiling, then a grant", states an evaluation order that no fact supports. B's own attempt notes and A's notes both say that no such fact exists. The root-MFA "Old:" line and "AWS still recommends them" (STS) are unlinked.
- Speak follow-up "A role can be attached to an instance that is already running" is grounded in `iam-ec2-role-credentials-rotate-automatically`. The quote is there, but the fact id names a different claim, so a reviewer would doubt it.
- Task iam-t02 teaches a number (the session-duration error), not a trap. A and C spend the same 12 minutes on "a deny beats an allow", which is the first trap of the chapter.

## Attempt C: customer conversation

**What worked for me.**
- Each subsection opens with a question I will really hear: "**Ben asks:** 'The policy on the worker role allows every S3 action. Why does the delete still fail?'" After it come the short answer, the mechanism, the thing to watch, and the client's case. This is the same order the speak grader scores, so reading is rehearsal. Speak s01 and s02 reuse the subsection questions word for word.
- The short answers are sentences I can say tomorrow: "For S3, both work. A bucket policy lets the caller stay in its own account. A role moves the caller into the other account."
- The questions are the strongest set:
  - q003: the boundary blocks DynamoDB, so the MOST secure fix adds one action to the *boundary*.
  - q004: SCP Deny for "no principal …, including the root user", with distractors that each fail for a fact-linked reason.
  - q005: same-account union, decided by "the team that owns the queue wants to control in one place".
  - q001/q006 twin: copy S3 objects needs a bucket policy; stop EC2 instances needs a role, because "Amazon EC2 does not support resource-based policies".
- The best "but not if" column: "the Deny has a condition that the request does not meet", and "more than 5,000 employees need access" → federation.
- Practical precision: ASIA vs AKIA key prefixes. The follow-up "The maximum session setting of the role does not limit them on EC2" (grounded in `iam-ec2-role-credentials-not-limited-by-max-session`).
- VPC spot-the-bug: the NACL allows outbound 443 only, so "Users cannot load the page". This is the best NACL exercise of the three. Also the Stop-and-answer about a tracked SSH session that survives a security group change.

**Where I got lost or bored.**
- It is the longest. Fast is 28 minutes against A's 23 (lint: Check 154 words against the cap of 140). It has ten signal rows. The B-list carries trivia that will never decide an answer: "600 requests per second" (STS quota), "1000" roles. The FAQ quotes run three lines each (FAQ 3, FAQ 4).
- "**In your case.** Earlier, Ben added a Deny for object deletes on the audio bucket". The answer depends on a backstory that I was never told. While skimming, I thought the Deny was invented to make the answer fit.

**Precision.**
- Internal contradiction. The subsection shows the worker role's trust policy (`"Principal": {"Service": "ec2.amazonaws.com"}`). Its Stop-and-answer then says "A developer assumes the worker role from her laptop with the AWS CLI". With that trust policy she cannot. The example also uses a laptop CLI, which the book's CloudShell rule bans.
- Hero diagram: the "IAM role" lifeline *sends* "Credentials" to the app. In reality STS delivers them through the instance metadata, and a role is not an actor. The diagram also warns "the drawing is 418 wide; size 's' allows 393. It will scroll on a phone".
- VPC table cell "Standard transfer charges on top of processing" is an unlinked claim in an explanatory section.

## For the synthesis

### Graft onto C from A
1. **The trace-then-table move inside "How it works".** Keep C's four spoken moves. Inside the "How it works" move, use A's one-line numbered trace, then A's compressing table. Take A's 4-case evaluation table and A's 5-row same-account / other-account table as written.
2. **A's skim-proof assertion headings.** Replace C's "Identity-based and resource-based policies combine differently across accounts" with A's "Same-account access needs one allow but cross-account access needs two". Make every heading pass the skim test: the gist alone must be correct.
3. **A's EC2 / Roles Anywhere twin pair (q001/q005)** and **q006** (the trust names the account, but the trusted side lacks `sts:AssumeRole`). These cover gaps in C's set.
4. **The explicit Predict closure in each Check answer** ("Predict 3 is No: …"). C already does this; make it a rule.
5. **"Do not let this number decide an answer."** Make this a standard line in Changed recently.
6. **The VPC request-and-reply trace** ("Every difference that the exam tests follows from this trace"), placed before C's compare table.

### Graft onto C from B
1. **One "Why does AWS work this way?" sentence** inside "The thing to watch" or "How it works": the AdministratorAccess guardrail argument for deny-wins, and the "SCP written far from the workload" argument. These are the reasons she can say to a founder.
2. **A stem-rule line per subsection**, as an `Exam signal` callout and *after* the mechanism, not before it: "AssumeRole fails → trust policy; the session fails later → permissions policy." Add B's **q002/q006 twin pair**, which tests exactly this.
3. **B's precision traps:** the `:root` account principal is not "root user only"; a security group can name another security group as source; the NAT gateway placed in a private subnet (spot the bug).
4. **Speak prompt "SCP or permissions boundary?"** (B's s02) as a third spoken item.
5. **B's fast compare "Cross-account role or resource-based policy"** (kept or given up; EC2 has no resource policy). C has this only in the deep file.

### Must-fix defects of C (the winner)
1. Fix the contradiction in the role subsection's Stop-and-answer. The worker role trusts only `ec2.amazonaws.com`, so use a different role whose trust names the account, and run the example in CloudShell, not on a laptop.
2. Move the hidden Deny into Ben's question ("Ben added a Deny for deletes last month. The role allows s3:\*. Why does the delete fail?"). Never let "In your case" add a fact that the reader has not seen.
3. Redraw the hero diagram. Credentials come from AWS STS through the instance metadata, not from an "IAM role" actor. Fit the 's' width budget (393).
4. Cut for economy. Fast to at most 1,600 words: eight signal rows, no "not examinable" items. Remove B-list trivia (STS 600 rps, 1000 roles). Trim each FAQ quote to the one sentence that answers.
5. Link or delete the VPC cell "Standard transfer charges on top of processing" (link to the data-transfer-out example fact or the cross-AZ NAT fact).
6. Mark a second twin pair. Only q006 → q001 is marked; the contract needs at least two.
7. Open issue for all three attempts: no one has confirmed that the Resource Groups Tagging API returns IAM roles. Until a fact confirms it, the verify step of iam-t02 is unverified. Replace it with `aws iam get-role --role-name … ` and expect NoSuchEntity.

### Keep from C as the house pattern
- The founder question, then the four run-in moves. The short answer is at most two sentences.
- The "Who grants and who only limits" table, with its root-user row.
- The speak items reuse the subsection's question, so the prose, the speak card and the quiz all rehearse one answer.
