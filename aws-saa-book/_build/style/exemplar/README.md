# Exemplar: the reference slice for every chapter (version 1.0, frozen 2026-10-11)

This folder is the model that about fifty chapters imitate. It is a slice, not a chapter: the IAM fast file is complete; the IAM deep file has three full How-it-works subsections, the numbers, the decision record and all ten FAQ items; the VPC deep file has two full subsections. The "Planned:" stubs and the "Not part of this sample." lines only keep the section structure.

| File | What it is | Where it lives in a real chapter |
|---|---|---|
| `iam-1-fast.md` | complete fast file of chapter 03 | `03-iam/1-fast.md` |
| `iam-2-deep.md` | three full subsections, Numbers, Decision record, FAQ quick-fire | `03-iam/2-deep.md` |
| `vpc-2-deep-slice.md` | two full subsections of chapter 10 | `10-vpc/2-deep.md` |
| `questions.json` | seven questions: two strict twin pairs, one multi-select, two think-alouds (one with a wrong path), one of difficulty 1 (`iam-q007`) | `data/03-iam/questions.json` |
| `speak.json` | three spoken answers (one explain, two compare) | `data/03-iam/speak.json` |
| `tasks.json` | one Look, one Try with a break-it step | `data/03-iam/tasks.json` |
| `cards.json` | one card of each written type: `decide`, `differ`, `number` (A-list "one hour"), `cannot` | `data/03-iam/cards.json` |
| `iam-hero.json` | hero diagram spec (sequence) | `diagrams/src/iam-hero.json` |
| `iam-brief.json` | the brief after the panel (13 traps, slots, speak plan) | `_build/work/03-iam/brief.json` |

How it was made: three attempts (a first principles, b exam operator, c customer conversation) were judged blind by five lenses (architect, designer, editor, exam, reader). Attempt a won (Borda a 9, c 4, b 2); b and c each had a fatal technical defect. The judges' must-fix lists were applied and their best ideas from b and c were grafted. At the freeze, the consistency check and the reader lens were applied too (`_build/reports/exemplar-fix.md`). Tool check (sandbox `_build/tmp/exemplar-final/`, 2026-10-11): `q lint`, `speak lint`, `tasks lint`, `cards lint` and `diagram lint` have no errors; `lint 03 --draft` and `lint 10 --draft` have no error in any written block. The remaining errors are the structure of a slice: L201 (the deep file is below 3,500 words), L106 (the eleven "Planned:" stubs have no Stop and answer), and in VPC the empty Numbers, Decision record and FAQ.

## Ten things to imitate

1. **The subsection runs problem, trace, table, reason, signal, rehearsal, transfer.** It opens with the problem in plain words, with no label: "Many policies can apply to one request, and they can disagree. AWS needs one rule for every case." Then a numbered trace with bold step names ("**Look for a deny.**"), a table that compresses the trace when it has two or more cases, one "Why" reason, an `Exam signal` (an `Exam heuristic` when no AWS fact decides the stem phrase, as in the NAT subsection), Go deeper, a `Say it` and the Stop and answer (`CONVENTIONS-2.md` U1). Each full subsection stays at or under 400 words before its reveals, and its time box is 5 min; a planned stub carries an honest time box (4 min here).

2. **A truth table carries the rule when she only skims.** "| 3 | Allows EC2, not S3 | Allows the action | Silent | Implicit deny |" and "| Other account | Allows | Silent | Implicit deny |". One row per case, the result in the last column, one term per concept ("Implicit deny", never just "Deny").

3. **Every heading is a true claim on its own.** "Same-account access needs one allow but cross-account access needs two." A reader who reads only the headings learns the rule and not the trap.

4. **One "Why does AWS work this way?" reason per subsection, said as a customer would hear it.** "Why does a deny win? A security team writes a Deny to stop one action. If a later allow could cancel it, the guardrail would fail on the day someone attached AdministratorAccess." And: "Why two allows? Each owner decides for its own side."

5. **The stem phrase comes after the mechanism, as an `Exam signal`, and covers both sides of the rule.** "> **Exam signal:** "the AssumeRole call fails" points to the trust side: the trust policy, and across accounts also the caller's own allow for sts:AssumeRole. "The call succeeds, but the next call fails" points to the permissions policy."

6. **A `Say it` line before every Stop and answer rehearses the spoken moves.** "> **Say it:** The short answer is: use a role, not a key. The thing to watch is the trust policy, which names who can use the role." Write it for speech: "across accounts, both sides have to say yes", not "both evaluations return Allow"; the watch move stays on the subsection's own answer (a KMS key there, not EC2). The full four moves live in `speak.json` (`iam-s01` ends "Which other services does the worker call, besides Amazon S3 and Transcribe?").

7. **The Stop and answer changes one variable and cannot be copied.** "The role's identity-based policy allows sqs:SendMessage on queues in account A. Does the call succeed?" The reader runs the rule on a new service and finds the wrong account in the resource ARN. In VPC: the database subnet allows outbound 5432 only, and the reply goes to "one of [ports 32768-61000] on Amazon Linux".

8. **Precision lives in Go deeper, with the exact scope of each quote.** "Temporary credentials [cannot be revoked] one by one ... So "Revoke active sessions" on the role adds an inline policy that [denies all permissions to all actions]." And: "A **KMS key** breaks the union." The `:root` principal "[does not limit the permission to the root user]".

9. **Strict twin questions: one phrase changes, the options stay identical, the key moves.** `iam-q002` "the call fails with an access denied error" against `iam-q006` "the call succeeds, but the next call to read a report fails". The stem states the side it does not test: "Their IAM policies allow sts:AssumeRole on the role ARN." The same holds for `iam-q001`/`iam-q005` ("Amazon EC2 instances in one AWS Region" against "servers in the company's data center"), with neutral option words ("where the application runs").

10. **A think-aloud with a wrong path shows where the gist breaks.** `iam-q004`, step 5: "My first idea breaks because the role and the bucket are in different accounts, so both accounts must allow the read; the bucket is in account B and the role is in account A, so I also choose the identity-based policy of the role." Step 3 states the plausible wrong prediction first.

Also copy: the Try task breaks, observes and fixes in that order ("Fix it: remove the deny policy. No new allow can fix an explicit deny."), shows that a deny is scoped to its actions (`s3:PutObject` "still shows allowed"), gives a full read-only alternative command, and verifies by its own `task` tag. The FAQ answers in one clause and quotes one whole sentence ("> "To restrict access, specify a Deny statement in any policy.""). A `not examinable yet` change sits under the B-list, its Old line holds the old value ("10 per role"), and its "The exam probably expects:" line ends "Do not let this number decide an answer." Each Check reveal answers its Predict in its own paragraph ("**Predict 1:** No: ..."), and each Recap prompt asks only for what the fast file states.

## The ten most common ways the attempts went wrong

1. **A sentence claimed more than its link.** "'Revoke the temporary credentials' is not a real action" linked a quote about one credential; AWS has "Revoke active sessions". "A service control policy (SCP), a permissions boundary and a session policy ... [allowed only if all three policy types allow it]" linked a fact about identity-based policies.
2. **An order or mechanism that no fact gives.** "AWS then makes three checks, in this order: Deny, Ceiling, Grant", turned into a recall card. Write "Use them as a checklist: the result is the same in any order."
3. **A key that the strongest actor in the stem can defeat.** Developers with AdministratorAccess and "make sure that no developer can delete", keyed to a group Deny that they can detach. Use an SCP.
4. **An exercise that breaks its own subsection.** The trust policy names `ec2.amazonaws.com`, then "A developer assumes the worker role from her laptop".
5. **A borrowed or weak link.** A general "explicit deny overrides" key fact linked a session-policy fact; a cross-zone charge linked a blog quote that says "typically". Link the most specific documentation fact.
6. **Story that teaches the answer.** "In your case. Earlier, Ben added a Deny for object deletes" adds a fact the reader never saw. A cross-account scene at stage 1 adds accounts that Callvale does not have yet; write "A team".
7. **Decoration instead of devices.** Three `Exam trap` callouts in a row that restate the table above them; a founder question answered in the next line (not a retrieval event); "Start with the problem." as a repeated label; a Spot the bug as obvious as `s3:*` on `*`.
8. **Padding in the fast file.** A `not examinable yet` quota box in the 20-minute file, with an Old line that gave the change ("the default quota rose from 10 to 20") instead of the old value; a pricing table with example rates in VPC.
9. **Plain-language slips.** Idioms ("each owner has a say", "as a safety net", "Role questions turn on one split"), unexpanded short forms (RCP, AZ, OU), headings with lost commas, a respelling of a common word ("least privilege"), and a "But not if" cell that names a problem and no answer ("they lack it").
10. **Diagram and cross-reference errors.** A hero diagram where an "IAM role" actor sends credentials (a role sends nothing; AWS STS and the instance metadata deliver them), drawn wider than its size budget; a cross-reference to KMS as chapter 13 (it is chapter 06: read `book.seed.json`).

## What this exemplar does not settle

- The verify step of `iam-t02` filters by its own tag (`Key=task,Values=iam-t02`, decision 44), so it returns nothing after the cleanup. No fact yet confirms that the Resource Groups Tagging API lists IAM roles: the IAM writer files that fact request ("Does the Resource Groups Tagging API GetResources operation return IAM roles?"). If the fact cannot be grounded, the verify becomes `aws iam get-role --role-name saa-iam-t02` (expect NoSuchEntity), which needs the T108 exception of `exemplar-spec-changes.md` 5.2.
- The core IAM terms (trust policy, permissions policy, implicit deny, explicit deny) are not in `data/terms.json`, so the files carry `needs-term` markers (W307) and the words table row `trust policy` is an L503 warning in draft. The respellings of common words and of `network ACL` and `NAT gateway` still differ from STYLE 4, so W901 warns on the fast file and the VPC slice until the orchestrator's term-bank fix (`exemplar-fix.md`).
- Three link texts wait for a display: `needs-display` markers for "10" (the Old line) and "generated dynamically on request" (role column). The orchestrator or the IAM registrar files these requests.
- Many displays that this slice links are longer than the 8 words that RULINGS now allows for a display without a digit (F2). They were verified before the ruling; whether they are re-cut is the orchestrator's decision. New requests follow the limit.
- The fast file is 20 minutes by its time boxes but about 27 by the `time_box` guidance (1,632 words, 10 prompts, a 3-minute Look). A 1,400-word cap would close the gap; it is a RULINGS budget, so the orchestrator decides (decision 42).
- No fact says that a custom network ACL starts by denying all traffic; request it before the VPC fast file is written. The VPC fast file needs a Changed recently entry for `vpc-regional-nat-gateway-change` (Old: one zonal NAT gateway in each Availability Zone); add it to the VPC brief.
- The hero picture shows a principal that calls AssumeRole. On EC2, AWS makes this call for the code (deep subsection on roles); the Predict the picture prompt now asks about a principal, not "the code". A diagram aside that says so is left to the diagram agent.
