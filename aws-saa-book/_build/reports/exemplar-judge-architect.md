# Exemplar judge: architect lens (precision, depth, grounding)

Judge: senior AWS solutions architect, strict technical reviewer. Read order c, a, b. Files read in each attempt: `03-iam/1-fast.md`, `03-iam/2-deep.md`, `10-vpc/2-deep.md`, `data/03-iam/{questions,speak,tasks}.json`, `diagrams/src/iam-hero.json`, `_build/work/03-iam/attempt-notes.md`. Tool runs were made on copies in `_build/tmp/judge-architect/` (the originals were not changed): `lint 03 --draft` and `lint 10 --draft --file 2-deep.md` for each attempt. Doubtful claims were checked with `search` and `show` against the corpus.

## Result

| Attempt | Learn | Exam | Precision | Reusable | Retention | Economy | Grounding | Fatal |
|---|---|---|---|---|---|---|---|---|
| A (first principles) | 4 | 4 | 4 | 3 | 4 | 4 | 4 | no |
| B (exam operator) | 4 | 5 | 2 | 4 | 4 | 4 | 3 | **yes** |
| C (customer conversation) | 4 | 4 | 3 | 5 | 4 | 3 | 3 | **yes** |

**Ranking: A, C, B.**

The mechanical lint is clean for all three. Every error is structural, because each attempt writes only 3 of about 13 subsections and leaves the rest as "Planned". No attempt has an L3xx fact-link error. So the differences between them are in meaning: a sentence that says more than its link supports, a wrong rule given as a reflex, or a scenario that contradicts the lesson it sits in.

## The fatal defects

### C: the exam trap tells her that a real AWS action does not exist

`03-iam/2-deep.md` line 124:

> **Exam trap:** "Revoke the temporary credentials" is not a real action. Temporary credentials [cannot be revoked](...); you deny the role's old sessions or change its permissions.

AWS has a page titled exactly **"Revoke IAM role temporary security credentials"** (corpus `docs/IAM/latest/UserGuide/id_roles_use_revoke-sessions`, line 3). The console button is **Revoke active sessions**, and AWS says "All temporary credentials for that role issued before the specified time become invalid." The STS quote "cannot be revoked" is about a single issued credential. It does not say that the revoke action does not exist. Here the sentence says more than its link supports, and the extra claim is false. On the exam, "revoke the role's active sessions" is a correct answer for leaked role credentials, and this trap trains her to reject it. Attempt A gets the same point right (2-deep line 98: "'revoke sessions' adds an inline policy that [denies all permissions to all actions] for credentials issued earlier").

**Second error in C, in the same subsection.** Lines 103 to 114 show the worker role's trust policy, and it names only `ec2.amazonaws.com`. Then the Stop and answer at line 133 says: "A developer assumes the worker role from her laptop with the AWS CLI ... What happens after about one hour". With that trust policy, the developer's AssumeRole is denied at once. The subsection's own lesson is "the trust policy names who can assume the role", and the exercise quietly breaks it. Attempt B builds a Stop and answer on exactly this case and gets it right (B 2-deep line 102: trust names EC2, developer gets access denied, fix the trust policy).

Smaller precision points in C:
- The hero diagram has "Ben → App: Attach role" and "IAM role → App: Credentials". Attaching a role is an EC2 API call, and the credentials come from STS through instance metadata. A role is not an actor that sends anything. This is acceptable for a gist, but it hides the mechanism.
- VPC line 92: "For S3 the transfer itself is free" drops the scope of its fact (`vpc-data-transfer-ec2-to-s3-same-region-free`, same Region).
- In line 122, "The SDK ... finds the role credentials without a code change" holds only if the code stops passing the hard-coded key, which is itself a code change.

### B: it teaches that an in-account IAM Deny stops administrators

Three places in B teach the same wrong reflex:

- `1-fast.md` signals row: `"block this action even for administrators" | explicit Deny statement | ... | the block covers every account: Deny in an SCP`.
- `2-deep.md` line 41: "If a broader allow could cancel that Deny, the guardrail would fail on the day someone attached AdministratorAccess."
- `questions.json` iam-q005: developers, some with AdministratorAccess on their IAM users; "make sure that no developer can delete objects". Keyed answer: "Attach a policy to the Developers group with a Deny statement".

AdministratorAccess includes `iam:*`, so such a developer can detach the group policy or leave the group, and the Deny is gone. The requirement "make sure" is not met. Compare C iam-q004, which states the condition outright ("Administrators in the production account can edit IAM policies and bucket policies") and correctly keys the SCP. Secure is her weakest domain (45%), and "even administrators" points to an SCP or a guardrail the admins cannot edit, not to a group policy. Shipping B's version would train the wrong answer.

Other precision and grounding problems in B:
- 2-deep line 72: "When a stem says that a user fails to assume the role, fix the trust side." This is false across accounts, where the caller's own `sts:AssumeRole` allow is the other half. B's own step 2, nine lines later, and its trap "only half of the cross-account trust" contradict it. The twin pair q002/q006 avoids the problem only because the stem supplies the identity side.
- Line 31 says "Read them in the order that AWS reads them", and line 35 says "AWS then makes three checks, in this order: Deny, Ceiling, Grant". No fact link backs this. It is not AWS's documented order either: AWS evaluates resource-based policies before boundaries and session policies, and a same-account resource-policy grant to a user ARN is not limited by a boundary's implicit deny. Attempt A deliberately avoided this claim (its notes: "No fact gives the order ... without claiming the exact AWS order").
- Line 38: "A service control policy (SCP), a permissions boundary and a session policy ... When all of them apply, the request is [allowed only if all three policy types allow it]". The linked fact `iam-scp-boundary-identity-all-must-allow` names SCP, boundary and *identity-based policy*, not a session policy. The link is used for a different claim.
- VPC line 79: "S3 traffic through a NAT gateway is not free because S3 is in the same Region." For a reader whose English is a second language, this reads as "not free, because same Region". It means the opposite of what B intends ("not free merely because").
- In the Try task iam-t02, an access-denied result in CloudShell is explained only by the role maximum. If she signs in through a role (federation or IAM Identity Center, which is what the book recommends), the AssumeRole call is role chaining, and the 12-hour request fails for the chaining limit instead. The explanation would then teach the wrong cause.

## Attempt A: the most precise, with the deepest mechanism

Evidence of real depth, beyond surface rules:
- A truth table per rule (2-deep lines 39 to 44, and the cross-account table at lines 128 to 134), scoped correctly: the cross-account table is headed "Where is the bucket?", so it does not over-claim for KMS keys.
- Edge cases in Go deeper blocks that the other two lack: "a resource-based policy that [grants permissions to an IAM user ARN is not limited by an implicit deny] in a boundary". It also has the revoke-sessions mechanism, and "network ACLs [do not filter traffic between instances in the same subnet]".
- The VPC Stop and answer at line 57 is the best NACL discriminator in the set. The database subnet allows outbound 5432 only, and the reply goes to the client's ephemeral port, "for example one of [ports 32768-61000] on Amazon Linux". That tests the mechanism, not a memorized phrase.
- The NAT trace includes the parts that exams probe: public subnet, Elastic IP at creation, the many-to-one mapping, why a stranger cannot connect, and a cost table plus a Stop and answer where the gateway endpoint removes both the processing charge and the cross-AZ charge "and the NAT gateway stays for the patches".
- "Changed recently" applies rule 7 correctly: the managed-policies-per-role change of 2026-08-19 is labelled "not examinable yet", with "Do not let this number decide an answer."
- The questions are sound. iam-q001 and iam-q005 are an EC2 versus on-premises twin, where a private CA makes IAM Roles Anywhere a tempting distractor on EC2. iam-q006 has auditors in a group, a trust policy that names the account, and the missing `sts:AssumeRole` grant, with group-as-principal and external ID as distractors. The Try task ends with "Fix it: remove the deny policy. No new allow can fix an explicit deny."

A's weaknesses are its lower score on reusable explanations: the "Start with the problem" prose explains things well but does not give her sentences to say out loud. Its precision issues are listed under must-fix below.

## Scores, criterion by criterion

1. **Learnability.** All three are 4. A gives a trace in short numbered steps, then compresses it into a table, which suits an engineer. B opens each subsection with the decision and the stem phrases, which gives the best gist at a glance. C's founder question gives each subsection a clear purpose, but the four-label ritual adds weight.
2. **Exam discrimination.** B 5: it teaches stem-phrase decoding inside the prose ("Two phrases decide most of them"), and its minimal twin pair q002/q006 (AssumeRole fails, against AssumeRole succeeds but the read fails) is the cleanest pair in the set. B also has the `:root` principal trap, the empty-SCP trap, a security group that references a security group, and the "NAT gateway in a private subnet" spot-the-bug. A 4 and C 4: C's q004 (root user and editing admins) and q005 ("The execution role has no permissions boundary", the exact condition the union rule needs) are excellent, and C alone has a worked think-aloud with a wrong path (q001).
3. **Technical precision.** A 4 (minor items below). C 3: two errors that mislead, both inside the central role subsection; the rest is careful, and its follow-up "[the maximum session setting of the role does not limit them on EC2]" is exactly right. B 2: one wrong reflex taught in three places, plus a wrong heuristic and an order claim with no source.
4. **Reusable explanations.** C 5: each subsection *is* the spoken answer (The short answer, How it works, The thing to watch, In your case), and the speak items close with a question back to the founder ("Is the source data encrypted with a KMS key?"). B 4: the "Why does AWS work this way?" paragraphs are sayable to customers. A 3.
5. **Retention.** All three are 4: Predict, Stop and answer, Spot the bug, trap ids, and a break-it step in the Try task. A's truth tables and C's worked think-aloud are the strongest single devices.
6. **Economy.** A 4: about 400 words per subsection, and the trace replaces prose instead of adding to it. B 4, though a third "Changed recently" item (the STS global endpoint) is marginal for this exam. C 3: the deep file is the longest at 2,852 words for the same 3 subsections, the four moves repeat, and some "In your case" paragraphs restate the short answer.
7. **Grounding hygiene.** A 4: its "Key fact" at line 46 borrows the session-policy fact for a general claim, and the cross-AZ row uses a blog fact. C 3: the revoke trap over-claims its link, and the S3 sentence drops the scope of its fact. B 3: a mis-scoped "all three" link, an unsourced claim about AWS's evaluation order, and an "Old" line with no link (the notes admit it).

## For the synthesis: graft onto A

From C:
1. A closing "Say it" block per How-it-works subsection, in C's four moves (short answer, how it works, the thing to watch, in your case), at most 4 sentences. This keeps A's trace and adds the spoken form she needs from the week of Oct 13.
2. The worked think-aloud in questions, with a wrong path (C iam-q001 `worked.steps`, which ends "My first idea breaks because ...").
3. C iam-q004 as written: SCP Deny against admins who can edit IAM policies and bucket policies, including the root user. It is the correct version of B's q005.
4. C iam-q005: same-account queue policy with "The execution role has no permissions boundary". This teaches the precise scope of the union rule.
5. The speak follow-up "[the maximum session setting of the role does not limit them on EC2]", and the closing question back to the founder.
6. The Go deeper on KMS cross-account ("[neither policy alone is sufficient]"), the bucket-policy spot-the-bug with a group as principal, and the role-chaining Go deeper, which should name the 1-hour cap and how to recover from it.
7. VPC: NACL rule numbers ([a number from 1 to 32766], first match wins, a deny with a lower number than the wider allow, [increments of 10 or 100]), the spot-the-bug where the NACL allows outbound 443 only, and the "attacker's SSH session survives the security group change" Stop and answer.

From B:
1. One or two opening sentences per subsection that name the stem phrases that decide it ("'Keep its own permissions' chooses a resource-based policy over a role"). This is the strongest device for "she rushes the stem".
2. The minimal twin pair q002/q006 (AssumeRole fails, against AssumeRole succeeds but the read fails), with the identity side stated in the stem.
3. Traps: the `:root` account principal "[does not limit the permission to the root user]"; an empty SCP is "[equivalent to attaching a policy that explicitly denies all actions]"; "[Service-linked roles cannot be restricted by SCPs]".
4. One "Why does AWS work this way?" sentence for each core rule (each owner decides for its own side; a ceiling is written far from the workload). Rewrite the "deny wins" rationale so that it adds: admins can delete an in-account Deny, so a guardrail against admins is an SCP.
5. VPC: a security group can name another security group as its source; the spot-the-bug with a NAT gateway in a private subnet; the "LEAST cost against highly available" count of NAT gateways; regional NAT gateways "[do not support private NAT]"; the cross-AZ charge from the doc fact `vpc-natgw-cross-az-transfer-charge`.
6. FAQ items: the member-account root user "[cannot remove or change SCPs]"; the policy simulator tests SCPs. The B-list row: GetSessionToken up to [129,600 seconds (36 hours)].
7. Task hygiene: `--query Credentials.Expiration`, so that the secret is never printed to the screen.

## Must-fix defects of the winner (A)

1. **Recap 3** (1-fast line 212): "Which three policy types limit access but never give it? SCPs, permissions boundaries and session policies." RCPs are missing, and A's own deep step 1 lists RCPs. Reword it to "Name policy types that limit but never grant", and accept RCPs.
2. **A borrowed link** (2-deep line 46): the general "explicit deny overrides" Key fact links `sts-session-policy-intersection`. Relink it to `iam-eval-explicit-deny-overrides-allow`, or to `iam-scp-boundary-identity-all-must-allow`, whose quote has the same sentence.
3. **An overclaim** (10-vpc line 28): "Every difference that the exam tests follows from this trace." Rule numbering and first match do not follow from it. Delete the sentence, or narrow it to "the stateful and stateless difference".
4. **A scope mismatch** (10-vpc line 26): an internet client's reply port is linked to the NAT gateway, ELB and Lambda ephemeral-port fact. Use `vpc-nacl-ephemeral-open-1024-65535`, as C does.
5. **A blog-sourced charge** (10-vpc line 87): replace `vpc-blog-same-az-free-cross-az-charged` with the documentation fact `vpc-natgw-cross-az-transfer-charge`.
6. **The union rule without its scope** in the fast "Choose" table ("Either policy is enough"). Add "when no boundary or deny applies; KMS keys differ (chapter 13)". The deep table is already scoped to buckets. The planned KMS subsection must keep B's line "Unless the key policy allows it, [IAM policies cannot allow access to a KMS key]".
7. **Changed recently, managed policies** (1-fast line 156): the "Old" line reads "the default quota rose from 10 to 20". Old should be the old value (10). The new value belongs on the Now line.
8. **Decision record**: move the Spot-the-bug out of the `example` section and into the role subsection, and mark the chosen option in bold, as B and C do.
9. **The VPC slice lacks NACL rule numbering** and the security-group-as-source rule. Graft both (see above). They carry many exam answers.
10. **Budget**: 1-fast is at 1,798 of 1,800 words. Each graft must replace text, not add to it. The "Say it" blocks belong in 2-deep.
11. **Shared by all three attempts**: the verify step of iam-t02 relies on the Resource Groups Tagging API returning IAM roles, which is not verified (all three notes say so). Verify with `aws iam get-role --role-name <name>` and expect a NoSuchEntity error, which needs no unverified assumption.
12. **Shared by all three attempts**: no fast file warns that a *custom* network ACL starts by denying everything, while the default network ACL allows everything. A states only the default case (10-vpc line 23). Add the custom case with a fact link when the VPC fast file is written.
