# Exemplar critique: reader lens, final check (2026-10-11)

Scope: `_build/style/exemplar/` (all files), `STYLE.md` 1.0, `SPEC.json` 1.0, `CONVENTIONS.md` 1.0, `CONVENTIONS-2.md` 1.0, `_build/reports/exemplar-spec-changes.md`. Read cold as the reader of `READER.md`. Nothing was edited. Facts checked with `saa.py facts show` (vpc-regional-nat-gateway-change, iam-change-root-mfa-all-account-types-2025).

Counts: 1 blocker, 8 major, 13 minor.

## The short answer

- Fast file: correct as a gist except Predict 1 (finding 2), but it is not finishable in 20 minutes. It declares 23 minutes. By the book's own formula (`lint.minutes_formula.time_box`: 120 words a minute plus 1 minute a prompt) it is about 31: 1,788 words is 15 minutes of reading, 12 prompts, and a 4-minute Look task. The contract allows this, so all fifty chapters will copy it (finding 1).
- Deep subsections: all three IAM subsections and both VPC subsections leave her able to explain the mechanism (trace, truth table, reason). Three lines teach a wrong gist: a `Say it` line (finding 4), the Go deeper on the root user (finding 5), and a VPC heuristic (finding 8).
- Spoken answers: you can say them aloud. `iam-s02` spends its "watch" move on EC2, which has nothing to do with the question, and it ends with a KMS question that nothing earlier sets up. The deep file's `Say it` lines quote documentation ("both evaluations return Allow") instead of speech (finding 6).
- Text written for the writer: "not the order of the code inside AWS", "The stateful and stateless difference follows from this trace", link texts that break the grammar, and unexpanded short forms (findings 13, 14, 18).

## Findings

### 1. BLOCKER. The fast file takes about 30 minutes, and the contract allows that

Place: `iam-1-fast.md` front matter `minutes: {fast: 23, pass: 76, ...}` and its time boxes; `SPEC.json` `templates.deep.files[1-fast.md]`; `iam-t01.minutes` 4 against `## Look first (3 min)`.

What is wrong:
- `READER.md` says that a file she can finish in 15 to 20 minutes gets opened. `LEARNING.md` 1.1 gives Fast 20 minutes and Pass 65 minutes for IAM. `SPEC.json` `templates.deep.minutes` says fast 20 and pass_xl 65.
- The exemplar declares fast 23 and pass 76. The honest time is higher, about 31 minutes by the `time_box` formula: Check is 140 words plus 3 prompts in a "2 min" box, and Recap is 150 words plus 5 prompts in a "2 min" box.
- The SPEC section budgets add up to 2,140 words (120+80+280+180+500+500+180+140+160), more than the file cap of 1,800. `LEARNING.md` 1.2 budgets add up to exactly 1,800 (Signals 420, Changed 90, Check plus Recap 130). The SPEC loosened each section, so the sections do not constrain the file.
- `iam-t01` is 4 minutes, but the box says 3.

Exact change:
- SPEC, `templates.deep.files[1-fast.md]`: set `words.max` to 1400. RULINGS says "at most 1,800", so a lower cap obeys it, but the orchestrator should confirm. Set `recap.counts.prompts` to 3 and `recap.words.max` to 90. Set `check.words.max` to 120. Set `signals.counts.signal_rows` to {min 6, max 8}, `traps` to {min 4, max 5} and `signals.words.max` to 380. Set `changed.words.max` to 120. Make the same change in `CONVENTIONS.md` section C, table "1-fast.md of a deep or medium chapter": row 6 "6 to 8 / 6", traps "4 to 5 / 3", row 9 "3 / 3 Recap prompts". Copy the change into the fixture SPEC.
- SPEC, `lint.minutes_formula`: add `"fast_check": "W105 when the time_box formula over 1-fast.md exceeds templates.<t>.minutes.fast by more than tolerance_minutes"`, so that the declared fast time is tested, not only summed.
- Exemplar `iam-1-fast.md`:
  - Delete Recap 3 and Recap 4 (see finding 3).
  - Delete the signals rows "require MFA for API calls" and "find buckets and roles shared outside the account". Both belong to the deep subsections on condition keys and Access Analyzer.
  - Delete trap 4 ("Code on an EC2 instance needs an access key in a file"). It restates signals row 1 and Predict 2, which README failure 7 forbids.
  - Time boxes: Predict 2, Look first 3, In one breath 3, Words 2, Choose 3, Signals 3, Changed 1, Check 2, Recap 1, for a total of 20. Front matter `fast: 20`, and recompute pass to at most 65.
- `tasks.json` `iam-t01.minutes`: 3. The task is three read-only commands.

### 2. MAJOR. Predict 1 can be answered two ways, and its reveal gives the wrong reason

Place: `iam-1-fast.md` Predict 1 and the reveal of Check 1.

What is wrong: "An SCP on your account allows Amazon S3 actions and nothing else. Can you launch an EC2 instance?" If "your account" is the management account, the answer is Yes. The file's own signals table says so: "the management account: SCPs affect only the member accounts". The reveal answers "Predict 1 is No: an SCP never grants permissions." That reason explains why the SCP's S3 allow adds nothing. It does not explain why EC2 fails. EC2 fails because the SCP does not allow EC2, and the effective permissions are the intersection. She leaves with "SCP never grants" as the reason that an admin cannot launch EC2.

Exact change:
- Predict 1: "Your IAM role in a member account has the AdministratorAccess policy. A service control policy (SCP) on the account allows Amazon S3 actions and nothing else. Can you launch an EC2 instance? <!-- gist-trap -->"
- Check 1 reveal, last sentence: "**Predict 1:** No. The role can do only [the intersection between those allowed by the SCP and the permissions granted to the principal by IAM permission policies](../facts/iam.md#iam-scp-faq-effective-permissions-intersection), and the SCP does not allow EC2."

### 3. MAJOR. Recap asks for things the fast file never teaches

Place: `iam-1-fast.md` Recap 2 to 5 and the Words table; `CONVENTIONS.md` D7.

What is wrong:
- Recap 3 (resource control policies, session policies) and Recap 4 (revoke active sessions) appear only in the deep file.
- Recap 2 asks for the trust policy and the permissions policy. The fast file never defines "permissions policy", and "trust policy" appears only in a hero step.
- Recap 5's "one sign-in for many accounts" is never stated. The fast file names IAM Identity Center only for the 5,000-user limit and the rename.

`LEARNING.md` 1.6 says Recap "replaces a summary box". It is recall of the file she just read. A prompt about something she never read is a new question with the answer hidden, so she learns that Recap does not work.

Exact change:
- Words table: replace the row `policy` with `| trust policy | the trust policy **names** who can assume the role | The policy on a role that says who can assume it | permissions policy, which says what the session can do |`. Add `trust policy`, `permissions policy`, `implicit deny` and `explicit deny` to `data/terms.json` with these collocations. This is also exemplar-spec-changes section 6.
- Delete Recap 3 and Recap 4. In Recap 5, write "Which service does AWS recommend as the front door for employees?". The reveal stays.
- `CONVENTIONS.md` D7, add: "Each Recap prompt asks for a sentence, row or cell that `1-fast.md` states above it. A Recap prompt never introduces a term or a fact."

### 4. MAJOR. The first `Say it` in How it works teaches a false gist

Place: `iam-2-deep.md`, subsection "AWS allows a request only when nothing denies and something allows", `Say it`.

What is wrong: "The short answer is: one allow is not enough." Two subsections later the heading says "Same-account access needs one allow". In one account with no deny and no ceiling, one allow is enough. This is the sentence she will repeat to customers.

Exact change: "> **Say it:** The short answer is: a request needs one allow and no deny. The thing to watch is a ceiling, such as an SCP or a permissions boundary, because it can stop an allowed request."

### 5. MAJOR. "Go deeper: who escapes a ceiling" suggests that the root user escapes SCPs

Place: `iam-2-deep.md`, first subsection, Go deeper.

What is wrong: The block is titled "who escapes a ceiling" and opens with "The root user starts with an allow". A skimmer reads it as "the root user escapes the ceiling". In a member account the root user is limited by SCPs. The fast file tests exactly this in Check 1 and in a signals row.

Exact change: Title it "Go deeper: exceptions to the implicit deny and to SCPs". After the first sentence, add: "An SCP still limits principals [including the member account's root user](../facts/iam.md#iam-scp-applies-to-member-root-user)."

### 6. MAJOR. Two "thing to watch" moves are off topic, and the Say it lines quote documentation

Place: `speak.json` `iam-s02` (sixty_second line 8, skeleton cue 4, kp4/kp5); `iam-2-deep.md` subsection "Same-account access needs one allow but cross-account access needs two", `Say it`; contract `CONVENTIONS.md` D8 and `STYLE.md` 11.1.

What is wrong:
- `iam-s02` asks how a job reads a bucket in another account. The watch move is "EC2: it takes no resource-based policy, so use a role". That is not part of her answer. Then the check-back question asks about a KMS key that the answer never mentions.
- The deep `Say it`, "across accounts, AWS allows the request only if both evaluations return Allow. The thing to watch is EC2: use a role", is documentation wording. "The thing to watch is EC2" makes no sense when said aloud.
- `STYLE.md` section 6 forbids links and doc wording in scripts. D8 does not apply this to the `Say it` lines.

Exact change:
- `iam-s02` line 8: "The thing to watch is encryption: with a KMS key, the key policy has to allow the job too."
- `iam-s02`: skeleton cue 4 becomes "KMS key needs its own allow". kp5 (KMS) becomes `must` and kp4 (EC2) becomes `nice`.
- Deep `Say it`: "> **Say it:** The short answer is: across accounts, both sides have to allow the request. The thing to watch is a KMS key, because [neither policy alone is sufficient](../facts/iam.md#iam-kms-cross-account-key-policy-and-iam-policy)."
- `CONVENTIONS.md` D8: after "A `Say it` callout with two starters", add: "written for speech: sentences of at most 16 words and no documentation wording. The watch move names a limit of this subsection's answer. Prefer wording without an absolute word, so that the line needs no link."

### 7. MAJOR. Both "Changed recently" entries put the change in `Old:`, not the old value

Place: `iam-1-fast.md`, root MFA entry; `iam-2-deep.md`, managed-policy quota entry under the B-list.

What is wrong: "**Old:** management and standalone accounts first; member accounts joined on 2025-06-17" is a history line, and "joined" is an idiom. "**Old:** 10 per role: the default quota rose [from 10 to 20]" reads badly with two colons and states the change again. `CONVENTIONS.md` D6 says "`Old:` holds the old value, never the change". README failure 8 and STYLE 11.11 say the same, so the model contradicts its own rule.

Exact change:
- Fast: "> **Old:** management and standalone accounts required root user MFA; member accounts did not.<br>"
- Deep: "> **Old:** 10 managed policies per role, before the quota rose [from 10 to 20](../facts/iam.md#iam-change-managed-policies-per-role-default-20).<br>"
- In the fast entry's heading line, write "Root user multi-factor authentication (MFA) is required in every account type." See finding 10.

### 8. MAJOR. The VPC NAT heuristic and its Go deeper give two answers

Place: `vpc-2-deep-slice.md`, NAT subsection, `Exam heuristic` and "Go deeper: one zone or every zone".

What is wrong: The heuristic says "'Highly available' points to one NAT gateway in each Availability Zone". The Go deeper below it says that regional NAT gateways expand across zones automatically. Fact `vpc-regional-nat-gateway-change`: GA 2025-11-19, examinable, and its note says that older questions assume one NAT gateway in each zone. She works at AWS. Telling a customer that high availability means one gateway in each zone is out of date, but the exam probably expects it. The slice does not say which answer to use where.

Exact change:
- Replace the heuristic with: "> **Exam heuristic:** "LEAST cost" points to one NAT gateway. "Highly available" points to one NAT gateway in each Availability Zone in older questions; a regional NAT gateway is the current answer when an option names it."
- The VPC fast file must carry the Changed recently entry for `vpc-regional-nat-gateway-change`, with Old "one zonal NAT gateway in each Availability Zone". Add this to the VPC brief.

### 9. MAJOR. Two planned subsections cannot fit their time boxes, and writers will copy them

Place: `iam-2-deep.md` stubs "Federation lets outside identities assume roles without IAM users (3 min)" and "Condition keys narrow an allow to the right organization or network (3 min)". All stubs use 3 min, and How it works says 45 min.

What is wrong: The federation stub lists SAML, OIDC, IAM Identity Center, Active Directory, Cognito user pools against identity pools, and Roles Anywhere. The condition-keys stub lists six keys, MFA with GetSessionToken, ABAC and the data perimeter. Neither fits 400 words as a mechanism with a trace; each becomes a list, which is what she does not finish. Every written subsection needed 5 minutes, so the 3-minute stubs and the 45-minute total teach writers a false budget.

Exact change:
- Split federation into "IAM Identity Center gives employees one sign-in for many accounts (5 min)" and "Cognito and Roles Anywhere give app users and servers temporary credentials (5 min)". The chapter then has 14 subsections, the maximum.
- Condition keys: keep aws:PrincipalOrgID, aws:SourceVpce, aws:SecureTransport and aws:MultiFactorAuthPresent. Move ABAC and the data perimeter into its Go deeper.
- Put "(5 min)" on every stub and recompute How it works and `full`.
- README "Ten things to imitate", item 1: add "and its time box is 5 min".

### 10. MINOR. Short forms are not spelled out

Place:
- `iam-1-fast.md`: MFA (first use in the signals table), STS ("AWS STS" in the words table and the hero).
- `iam-2-deep.md`: STS, and ARN ("with the ARN of the role").
- `speak.json` `iam-s03`: the skeleton cue "OUs".
- `questions.json` `iam-q003` say: "admins".

What is wrong: README failure 9 and STYLE 12 require every short form to be spelled out in each file. The lint cannot catch these, because the short forms are not in `data/terms.json`.

Exact change: At first use in each file, write "multi-factor authentication (MFA)", "AWS Security Token Service (AWS STS)" and "Amazon Resource Name (ARN)". Change "OUs" to "organizational units" and "admins" to "administrators". Add MFA, STS, ARN, SCP, RCP, OU and SDK as `short` values in `data/terms.json`, so that the abbreviation lint enforces the rule in later chapters.

### 11. MINOR. One concept has four words: ceiling, cap, limit, maximum

Place: `iam-1-fast.md` words row "caps what an account can do"; `speak.json` `iam-s03` ten_second and sixty_second ("cap", "caps"); `iam-2-deep.md` ("ceiling", "set the most").

Exact change: Use "ceiling" as the noun and "limit" as the verb everywhere. Words row: "An organization policy that sets a ceiling on what an account can do". `iam-s03` ten_second: "Both are ceilings and grant nothing. An SCP limits whole accounts in an organization. A boundary limits one user or one role." Replace "caps" with "limits" in sixty_second lines 4 and 6, and "caps" with "limits" in the stub "A permissions boundary lets developers create roles without escalating".

### 12. MINOR. B-list labels call a maximum a "size"

Place: `iam-2-deep.md` B-list rows "Size of one customer managed policy", "Default size of a role trust policy", "Default number of managed policies on one role".

Exact change: "Maximum size of one customer managed policy", "Default maximum length of a role trust policy", "Default maximum of managed policies on one role, after the change below".

### 13. MINOR. Link texts that break the sentence

Place:
- `vpc-2-deep-slice.md`: "numbers its rules from [a number from 1 to 32766]"; "[we do not evaluate any additional rules]", where "we" is AWS; "Its rule source can be [The ID of a security group]"; "because [Connections must always be initiated ...]". The last two are capitalized in mid-sentence.
- `iam-1-fast.md`: the role column reads "Keys [generated dynamically on request rather than stored with the user]", which names a user in the role column.

Exact change:
- "Each rule has [a number from 1 to 32766](...), and the network ACL stops at the first rule that matches <!-- needs-display: vpc-nacl-rule-order-first-match "do not evaluate any additional rules" -->".
- Request lowercase displays: needs-display "the ID of a security group" and "must always be initiated from within the VPC".
- Role cell: "Temporary keys that AWS STS [generated dynamically on request](...)", with a needs-display marker if that span is not a display.
- STYLE 11.2, add: "The link text reads as part of your sentence: no capital in mid-sentence, no 'we', no repeated preposition."

### 14. MINOR. Sentences written for the writer, not for her

Place: `iam-2-deep.md` "They are a checklist, not the order of the code inside AWS."; `vpc-2-deep-slice.md` "The stateful and stateless difference follows from this trace."

Exact change: IAM: "Use the four checks as a checklist: the result is the same in any order." This follows from the rule and adds no fact. VPC: delete the sentence. STYLE 11.3, change the quoted model sentence to the same wording.

### 15. MINOR. VPC slice: an idiom, a respelled common word, a partial heading, an undefined term

Place: `vpc-2-deep-slice.md` NAT subsection.

Exact change:
- "Now follow the money for the same packet." becomes "Now count the charges for the same packet."
- "**NAT gateway** (NAT GAYT-way)" becomes "**NAT gateway** (NAT, said as one word: nat)", or drop the respelling of "gateway" (STYLE section 4).
- Heading: "A NAT gateway lets private instances start connections and charges by the hour and the gigabyte (5 min)", or shorten it to 14 words.
- "Why does a gateway endpoint save money?" is the first use of the term. Write "A **gateway endpoint** sends Amazon S3 traffic from the route table straight to Amazon S3. Why does it save money?", with a needs-term marker if the term is missing from the bank. The reason must stay about the NAT path.

### 16. MINOR. Step 3 of the IAM trace leaves out a ceiling that step 1 and the fast file name

Place: `iam-2-deep.md` step 3, "Check every ceiling".

Exact change: Add the sentence "An RCP sets the ceiling for a resource: [an RCP never grants permissions](../facts/iam.md#iam-rcp-never-grants-limits-resources)."

### 17. MINOR. Weak cells in the fast tables

Place: `iam-1-fast.md`.

Exact change:
- Words row `least privilege`: the "Do not confuse with" cell "read access for everyone" is not a real confusion. Write "a broad AWS managed policy".
- If the `policy` row stays (see finding 3), "a permission set in IAM Identity Center" introduces a term she has not met. Write "a role, which holds policies".
- Table "Grant or ceiling": the row question "Whom does it limit?" is wrong for an identity-based policy. Write "Whom does it apply to?"

### 18. MINOR. Spoken details that break when said to a founder

Place: `speak.json`.

Exact change:
- `iam-s01` line 9: "In your case, I'd create one role for the worker first, then delete the root key." Today's line deletes the key that the running app uses.
- Introduce "the worker" in line 3: "You attach the role to the worker's instance through an instance profile."
- `iam-s03` line 7: "In both cases, an identity-based or resource-based policy still has to grant the action." Replace "a normal policy".

### 19. MINOR. Question text that is hard to parse

Place: `questions.json`.

Exact change:
- `iam-q001` option d `why`: "The application already runs on EC2, so a role on the current instances does the same job without a migration."
- `iam-q004` worked step 5, end: "the bucket is in account B and the role is in account A, so I also choose the identity-based policy of the role."

### 20. MINOR. The Check reveal mixes two answers in one paragraph

Place: `iam-1-fast.md`, Check 1 to 3 reveals ("Predict 3 is No: ..."); `CONVENTIONS.md` D1.

What is wrong: A skimmer reads "No ... Predict 3 is No" in one paragraph and cannot tell which answer belongs to which question.

Exact change: In D1, change "that reveal also answers Predict `<n>` in one sentence" to "that reveal ends with a separate paragraph `**Predict <n>:** <answer in one sentence>`". Apply this to the three reveals.

### 21. MINOR. The picture and the prompt before it describe two different paths

Place: `iam-1-fast.md`, "Predict the picture" and the hero.

What is wrong: The prompt asks how "the code" gets credentials, and the startup example is code on EC2. The picture shows a principal that calls AssumeRole. Code on EC2 does not call AssumeRole itself (deep subsection 2), so she can leave with the wrong path for the most common case.

Exact change: Prompt: "Does a principal keep a key, or does it get credentials from AWS?" After hero step 3, add a note to the step list in `iam-brief.json` and `iam-hero.json`, or add to the caption: "On EC2, AWS makes this call for the code (see How it works)." Keep the caption within 24 words.

### 22. MINOR. The Try task's read-only alternative cannot be done as written

Place: `tasks.json` `iam-t02.read_only_alternative`.

What is wrong: It names `aws iam simulate-custom-policy` but gives no command. A reader in a locked-down account cannot run it.

Exact change: Give the full command with two inline policy documents, the same as the `put-role-policy` JSON in steps 2 and 4, plus `--action-names s3:GetObject s3:PutObject` and the expected result (explicitDeny for GetObject, allowed for PutObject).

## What works and must be kept

- The trace, truth table and Why order. The deny reason ("the guardrail would fail on the day someone attached AdministratorAccess") and "Time limits the damage" are the clearest explanations of the mechanism in the slice.
- Headings that state a claim. A reader who reads only the headings learns the rules correctly.
- Stop and answer prompts that change one variable (the SQS queue ARN, the Amazon Linux port range). She cannot answer them by copying.
- Strict twins `iam-q002`/`iam-q006` and `iam-q001`/`iam-q005`, and the wrong-path think-aloud.
- The FAQ quick-fire, with one-clause answers and one quoted sentence each.
