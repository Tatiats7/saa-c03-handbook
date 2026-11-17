# Exemplar judgment: instructional designer lens

Judge: designer (retrieval practice, worked examples, cognitive load, spacing).
Read order: a, c, b. Files read in each attempt: `03-iam/1-fast.md`, `03-iam/2-deep.md`, `10-vpc/2-deep.md`, `data/03-iam/{questions,speak,tasks}.json`, the hero diagram preview, `brief.json` and `attempt-notes.md`. I did not run `lint` against the attempt folders, because the tool writes its report into the book directory and that would change an attempt. I used the lint records each attempt saved (`lint-draft.txt` for A, `lint-fast.json` and `lint-deep.json` for C) and my own per-subsection word and device count.

All three attempts write the same 3 IAM subsections and 2 VPC subsections in full and leave the rest as "Planned" stubs. I judge only the written parts.

## Scores (1 to 5)

Criteria: (1) learnability, (2) exam discrimination, (3) technical precision, (4) reusable explanations, (5) retention design, (6) economy, (7) grounding hygiene.

| Attempt | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Sum |
|---|---|---|---|---|---|---|---|---|
| A (first principles: problem, trace, table, transfer) | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 27 |
| B (exam operator: stem phrase, mechanism, why) | 4 | 5 | 3 | 4 | 4 | 4 | 3 | 27 |
| C (customer conversation: founder question, four moves) | 3 | 4 | 4 | 5 | 3 | 3 | 4 | 26 |

**Ranking: A, B, C.** A and B have the same sum. A ranks first because its one weak criterion (spoken reuse) is cheap to fix by grafting, and B's weak criterion (precision) is in the central teaching sentence of the chapter. The book must not teach a simplification as AWS fact to a reader who works at AWS.

**Fatal technical defect: none.** B's "in this order" claim (below) is a must-fix but does not make any exam answer wrong.

## Measured load per written subsection (words incl. answers and Go deeper; devices)

| Attempt | IAM eval | IAM role | IAM cross-account | VPC SG/NACL | VPC NAT |
|---|---|---|---|---|---|
| A | 486 | 453 | 476 | 552 | 535 |
| B | 492 | 499 | 498 | 543 | 607 |
| C | 553 | 535 | **617** (3 Exam traps, Spot the bug, Go deeper, table, Stop) | 594 | 541 |

LEARNING.md wants a Stop-and-answer every 250 to 400 words. All three run long. A is the leanest. C's cross-account subsection carries seven devices in a "5 min" box, so the time box is not honest.

## Attempt A: what works and what does not

**Worked example then faded practice, done right.** Every full subsection runs: "Start with the problem", then a numbered trace ("Now follow one request through four checks"), then a compression table, then a Stop-and-answer on a *new* case. That is the worked-example-to-transfer sequence the evidence supports. The 4-row table in the evaluation subsection is the best single teaching object in any attempt:

> | 3 | Allows EC2 | Allows the action | Silent | Implicit deny |
> | 4 | Allows S3 | Allows the action | Denies the action | Explicit deny |

**Stop-and-answers need transfer, not copying.** "A Lambda function in account A sends messages to an SQS queue in account B. The queue policy allows the function's role. The role's identity-based policy allows sqs:SendMessage on queues in account A." To answer, she has to run the rule on a new service and spot that the identity policy names the wrong account. That is the 70 to 85% "apply it" item LEARNING section 3 asks for. The boundary item (allows s3:\*, boundary allows only GetObject, can it PutObject?) is the same kind.

**Predict and Check are real retrieval with twins.** Check 3 is a true twin of Predict 3: "Same bucket policy, but the role is now in the bucket's account" → Yes, against No for Predict 3. One phrase changes and the answer flips. Of the three attempts, this is the clearest use of the twin device in the fast file. Recap 4 ("How do you stop a leaked set of temporary credentials before they expire?") asks for generation, not repetition.

**The honest gap.** Its notes say "No fact gives the order in which AWS checks the policy types, so the trace says 'four checks' without claiming the exact AWS order". That restraint is right.

**Weaknesses.**
- The deep prose is not shaped for speech. Nothing in a subsection gives her a sentence to say to a founder. The spoken items in `speak.json` are good four-move scripts ("The short answer is: you give the instance an IAM role instead of a key."), but the reading does not rehearse them.
- The fast file spends a Changed-recently box on a quota change it calls "not examinable yet", and the Old line is muddled: "**Old:** the default quota rose [from 10 to 20]". For this reader that is padding.
- "Key fact: An explicit deny in any of these policies overrides the allow" links to `sts-session-policy-intersection`. The quote matches, but in the policy-evaluation subsection a reader who clicks lands on a session-policy fact.
- The decision record's "Spot the bug" (`s3:*` on `*`) is the most obvious bug possible. It shows a device, not a test.
- Only one twin pair among the 6 questions (q001/q005, EC2 against data center). It is a good pair.

## Attempt C: what works and what does not

**The best spoken transfer.** Each subsection opens with "**Ben asks:**" and runs The short answer / How it works / The thing to watch / In your case. Reading the book becomes rehearsal of the four moves the grader scores. For the week of Oct 13 this is the strongest asset in any attempt. "Security groups are your main control. Add a network ACL when you need a deny for a whole subnet" is a sentence she can say tomorrow.

**The best discrimination detail.** Q005 adds "The execution role has no permissions boundary" so that "queue policy alone" is correct in one account, which shows real knowledge of the same-account rule. The signal "the Deny has a condition that the request does not meet" in the "but not if" column is the sharpest exception row in any attempt. The VPC NAT Stop-and-answer (internet packages, NAT in the other AZ) ends "A gateway endpoint does not help, because the repository is not S3 or DynamoDB". That is a near-miss item that blocks keyword matching.

**The retrieval-design flaw.** The four-move form puts the answer in the second line of every subsection. "Ben asks: '…Why does the delete still fail?'" is followed at once by "**The short answer.** An allow is not enough." A question that is answered in the next sentence is not a retrieval event. It is a heading. The opening question is decoration unless she is asked to answer before she reads on, which is the generation effect Predict exists for.

**Load and repetition.** The cross-account subsection states the both-accounts rule in the prose, the table, "Exam trap" #3, the Spot-the-bug answer and the Stop answer. Three Exam-trap callouts in a row are decoration: each restates a row of the table above it.

**Story bending.** "In your case. Earlier, Ben added a Deny for object deletes on the audio bucket, as a safety net." The story invents a past event so the move has something to say. Over fifty chapters this produces story the bible does not hold.

**Fast file.** The Checks are not twins of the Predicts. Check 3 (EC2 has no resource policy) tests a different concept from Predict 3. The Recap prompts are mostly rule restatements ("Which wins when one policy allows an action and another policy denies it?").

**Diagram.** The diagram shows "IAM role → Credentials → App on EC2" and Ben sending "Attach role" straight to the app. A role does not send anything. STS and the instance metadata do. The diagram also has a size warning: "It will scroll on a phone beyond 448".

**Minor grounding.** "5,000 | IAM users in one account, not adjustable" has the number linked but not the "not adjustable" claim. "Data transfer | Standard transfer charges on top of processing" has no link.

## Attempt B: what works and what does not

**It trains her real weakness.** She "reads fast and rushes questions". Every subsection opens with the phrase in the stem that decides it: "'Denies' points to an explicit deny. 'The SCP allows' or 'a permissions boundary' points to a ceiling. 'Has no policy for' points to the default." That is constraint-finding taught as a reading skill, before the mechanism.

**The best twin pair in the set.** q002 against q006: same stem, and "the call fails with an access denied error" becomes "the call succeeds, but the next call to read a report fails". The options are identical and the key moves from the trust policy to the permissions policy. This is the twin device used exactly as LEARNING section 3 #8 defines it, and the takeaway line, "AssumeRole fails: fix the trust policy. The session fails later: fix the permissions policy", is a portable diagnostic rule.

**"Why" paragraphs make reusable explanations.** "A security team writes a Deny to stop one action permanently. If a broader allow could cancel that Deny, the guardrail would fail on the day someone attached AdministratorAccess." "An SCP is written for a whole account or organizational unit, far from the workload. It knows which services the company allows, not which bucket a job needs." These are the best customer-ready explanations in the three attempts: causal and short, with no lookup needed.

**The three-part Stop-and-answer.** "Which of these work: list a bucket, delete an object, create a DynamoDB table?" One scenario, three outcomes, each failing at a different check. Good discrimination practice inside the reading.

**Must-fix precision defect.** "AWS then makes three checks, in this order: 1. Deny check. 2. Ceiling check. 3. Grant check." and "Read them in the order that AWS reads them." Then the fast-file Recap 2 turns it into a recall card: "In which order does AWS read the policies of one request? Deny first, then every ceiling, then a grant." No fact in the canon gives this order (attempt A says so explicitly). The documented logic also does not follow it: in one account, a resource-based policy can allow a request that a permissions boundary or session policy does not cover. The card would teach her to say something false about AWS with confidence. Also in speak s02: "Only when an identity-based policy also allows it." This leaves out a same-account resource-based grant.

**Other weaknesses.**
- The Try task (`iam-t02`) breaks a B-list number (role maximum session) with `"trap": null`, while the deny-beats-allow trap goes unpractised by hand.
- The VPC Stop-and-answer 1 ("block that range now… where does the new rule go?") can be answered by copying the sentence above it ("give the deny rule a lower number").
- The fast file has 4 compare tables and bolds terms in Predict before they are defined.
- The signal "require MFA… | but not if: the caller uses long-term access keys: they lack it" names a problem without saying what to do.
- The VPC decision record is a skeleton of "Planned" lines.

## Devices across the three: working or decoration

| Device | Works best in | Decoration in |
|---|---|---|
| Predict → Check (twin) | A (Check 3 flips Predict 3); B (Check 3 mirrors Predict 3 from the identity side) | C (Checks test other concepts) |
| Stop and answer (transfer) | A (Lambda→SQS, boundary PutObject); C (tracked SSH session, NAT AZ near-miss) | B VPC #1 (copy-able) |
| Twin questions | B q002/q006 (one phrase, options identical) | none. A and C pairs are sound but change more than one phrase |
| Recap from memory | A Recap 4 (generative) | C (rule restatements) |
| Worked think-aloud | **absent in all three**. LEARNING section 6.6 asks for 2 per deep chapter, one with a wrong path | |
| Spoken four moves | C (the whole deep file); all three `speak.json` follow it well | A and B reading never rehearses it |
| Exam trap callouts | B (one per subsection, each new) | C (three restating one table) |
| Spot the bug | C (group principal; NACL outbound 443); B (NAT in private subnet) | A and B decision record (`s3:*` on `*`) |

## Does the fast file give a correct gist? Does the deep file give understanding?

- **Fast, A:** a correct gist. The headings and tables alone teach the three exam rules (deny wins, ceilings never grant, one allow in an account and two across accounts). Minor padding.
- **Fast, B:** a correct gist, except Recap 2, which seeds a false ordering rule.
- **Fast, C:** a correct gist. The best signal table. Weaker retrieval pairing.
- **Deep, A:** real understanding. She can rebuild the rule from the trace.
- **Deep, B:** real understanding, with the best "why". The order claim is the flaw.
- **Deep, C:** understanding wrapped in conversation. The mechanism is present but sits between pre-given answers, and the load is highest.

## For the synthesis

### Winner: A. Grafts from the non-winning attempts

1. **From B: a "stem phrases that decide this" opener of 2 to 3 lines** before A's "Start with the problem". Put the quoted stem phrases in bold quotes. This is the cheapest anti-skim device for her and it costs about 40 words.
2. **From B: one "Why does AWS work this way?" paragraph per subsection** (the deny-guardrail and the SCP-far-from-workload paragraphs as the model). It is the causal sentence she says to a customer.
3. **From B: twin questions in the strict form.** Same stem, one phrase changed, identical options (q002/q006). Require at least one such pair per deep chapter.
4. **From B: the multi-outcome Stop-and-answer** ("Which of these work: X, Y, Z?") as an allowed variant.
5. **From C: a closing "Say it" line per full subsection, not a four-move frame.** After the Stop-and-answer, give a 2 to 3 sentence four-move answer to a founder question ("Ben asks: … The short answer is …"). This keeps C's speech rehearsal without putting the answer before the retrieval. Better still: ask the founder question *before* the trace as the Predict for the subsection, and reveal the four-move answer in `<details>` after it.
6. **From C: the "but not if" sharpness** ("the Deny has a condition that the request does not meet"; "more than 5,000 employees"), the Spot-the-bug items (group as principal; NACL that allows only 443 outbound), the near-miss NAT Stop-and-answer ("A gateway endpoint does not help, because the repository is not S3 or DynamoDB"), and Q005's precise "no permissions boundary" stem.
7. **From C: the root-user row** in the grant-or-ceiling table ("Does it limit the root user? … cannot set a permissions boundary for the root user").
8. **From C's Try task:** add a third action the Deny does not name (`s3:PutObject` still allowed), so she sees a deny is scoped to its actions.
9. **From B's VPC:** a security group that names another security group as its source, and the Spot-the-bug "NAT gateway in a private subnet".

### Winner: A. Must-fix defects

1. **Add worked think-alouds** (missing in all three): 2 per deep chapter in the LEARNING 6.6 six-step form, one with a wrong path. A's numbered trace is the natural base.
2. **Cap each full subsection at about 400 words** before Go deeper (A's run 453 to 552). Move the Exam signal or the second table into Go deeper where needed, or split the subsection.
3. **Fix the Key-fact link** in the evaluation subsection. It should link to an evaluation-logic fact, not to `sts-session-policy-intersection`.
4. **Remove the "not examinable yet" quota box** from the fast file, or move it to the deep file. Rewrite its Old line ("the default quota rose from 10 to 20" is the change, not the old value).
5. **Replace the decision-record Spot-the-bug** (`s3:*` on `*`) with a non-obvious bug, for example a trust policy that names the account but no `sts:AssumeRole` on the caller side, or a group as principal.
6. **Recap 3** should mention RCPs as a ceiling too, or say "for principals" to scope it, because the deep file lists RCPs.
7. **Link the "management account: SCPs do not apply there" cell** in the signals table to `iam-scp-no-effect-on-management-account`.
8. Keep A's refusal to state an evaluation order. Do **not** import B's "in this order" sentence or its Recap 2.

### Notes for whichever attempt is not chosen (if the panel picks B)

- Delete or reword "AWS then makes three checks, in this order" and Recap 2. Say "Think of it as three questions" and do not claim AWS order.
- Fix the speak s02 follow-up so it also allows a same-account resource-based grant.
- Point the Try task at the core trap, not at a B-list number.
