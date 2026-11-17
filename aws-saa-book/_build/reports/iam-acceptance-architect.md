# IAM chapter (03): acceptance review, architect lens

Reviewer lens: senior AWS solutions architect, strict technical reviewer. Date 2026-10-12.
Scope read: `03-iam/1-fast.md`, `2-deep.md`, `3-do.md`, `4-say.md`, `5-quiz.md`, `sources.md`; facts in `facts/iam.md` and `facts/sts.md`; `_build/reports/lint/03.json` (ok, 0 errors, words 1-fast 1,670 and 2-deep 5,498); `_build/reports/cli/03.json`.
Evidence: `saa.py search` over the saved corpus, and fact quotes read from the canon.

## Verdict

The chapter is strong. The evaluation logic, the role and trust model, cross-account rules, SCPs and boundaries are precise and well grounded. 211 fact links, and almost every sentence stays inside its fact. Do not accept it yet. Three errors would mislead her (FATAL), and one recommendation contradicts the chapter's own best-practice fact and quiz answer.

## Scores (1 to 5)

| Criterion | Score | Reason |
|---|---|---|
| Learnability for this reader | 4 | Short sentences (average 8 words), gist tables, time boxes, Predict and Stop-and-answer. Some cells carry long verbatim AWS clauses that are heavy for a second-language reader (1-fast line 171, "the intersection between those allowed by the SCP and ..."). |
| Exam discrimination power | 4 | Deciding phrases, twin stems (q001/q005, q002/q006), and distractors that each fail for a named reason. A few distractors are too easy, for example "AdministratorAccess outweighs the Deny" (q008) and "keep using the root key" (q020). |
| Technical precision | 3 | Of 20 statements tested, 16 hold. The 4 that fail are below: the KMS gist cell, the MFA Deny recipe, the tagging-API verify, and IAM users for people. |
| Reusable explanations | 4 | "Say it" lines, 10-second and 60-second answers, skeletons and do-not-say lines she can reuse with customers. Prompt 4 teaches a recommendation that a customer-facing AWS SA should not give (M4). |
| Retention design | 5 | Predict, Look first, Check, Recap, a Stop-and-answer in every subsection, Spot the bug, traps with markers, twins and takeaways. |
| Economy | 4 | Inside budget, but 2-deep is at 5,498 of 5,500 words. The cross-account rule "both evaluations return Allow" appears about 9 times across the files. |
| Grounding hygiene | 3 | Links match their facts closely. Exceptions: the verify steps rest on a "can" that the canon itself refutes (M1); the 1-fast KMS cell drops the fact's scope ("unless the key policy explicitly allows it") (M2); the MFA sentence turns a general FAQ fact into a recipe the fact does not support (M3). |

## The 20 statements tested

| # | Place | Statement | Result |
|---|---|---|---|
| 1 | 1-fast line 137 | Same account, identity-based policy is "Enough, except for KMS keys: IAM policies cannot allow access to a KMS key" | **Refuted.** Fact `iam-kms-iam-policy-needs-key-policy-permission` is scoped "unless the key policy explicitly allows it", and the same quote says "The default key policy enables IAM policies." With the default key policy, an IAM policy alone is enough. (M2) |
| 2 | 2-deep line 445 | "To enforce MFA, specify a Deny statement in any policy with the condition." | **Misleading.** A Deny with `Bool aws:MultiFactorAuthPresent false` does not match access-key requests, because the key is missing ("long-term access keys do not include it") and a missing key makes the condition false (`iam-condition-missing-key-is-false-except-ifexists`). The Deny needs `BoolIfExists`. The canon has the fact, but the chapter never uses it. (M3) |
| 3 | 3-do lines 137 and 241 | Verify with `resourcegroupstaggingapi get-resources --tag-filters Key=task,...` and expect an empty list | **Refuted by the canon.** `iam-tagging-api-getresources-no-iam-roles`: "The `GetResources` operation does not currently support IAM users and roles." The list is always empty, even when the role still exists. The same issue was raised in `exemplar-critique-consistency.md` item 7 and is still open. (M1) |
| 4 | 2-deep lines 608 to 618; 4-say lines 190 to 200 | Founders get IAM users with MFA "because Callvale has one account" | **Contradicts the canon.** `iam-best-practice-human-users-federate-with-identity-center`: "Require your human users to use temporary credentials"; the IAM FAQ quote says to federate instead of using IAM users for the workforce. `iam-idc-accounts-need-organizations-all-features` says "any AWS account managed using AWS Organizations", so a single-account organization qualifies and "one account" is not a reason. This also conflicts with the chapter's own trap (2-deep line 151) and with the quiz q020 answer ("identities that use IAM roles"). (M4) |
| 5 | 1-fast lines 184 to 188 | Root MFA "Old: management and standalone accounts required it; member accounts did not" | Holds for the state just before 2025-06-17 (fact: May 2024 management, June 2024 standalone). Incomplete: before May 2024, no account type required it. (S1) |
| 6 | 2-deep line 73 | PowerUserAccess allows all services except IAM, Organizations and Account Management | Holds (first statement of the policy). The service-linked-role and organization-read exceptions are left out, which is acceptable for the exam signal. |
| 7 | 2-deep line 99 | A same-account resource policy that grants to an IAM user ARN is not limited by a boundary's implicit deny | Holds (verbatim, `iam-boundary-user-arn-grant-not-limited`). |
| 8 | 2-deep lines 175 and 184 | The caller's own sts:AssumeRole allow is needed "across accounts" | Oversimplified. In one account, a trust policy that names only the account also needs the caller's allow. (S6) |
| 9 | 2-deep line 189 | Role chaining caps the session at one hour, regardless of the role's maximum | Holds (`iam-role-chaining-one-hour-limit-exceptions`, `sts-role-chaining-max-one-hour`). |
| 10 | 2-deep line 225 | When S3 invokes a function, Lambda considers only the resource-based policy | Holds (verbatim). |
| 11 | 2-deep line 347 | Identity Center for many accounts needs Organizations with all features | Holds. |
| 12 | 2-deep line 360 | Identity Center connects one directory or one SAML 2.0 IdP at a time | Holds. |
| 13 | 2-deep lines 402 and 434 | A missing key makes a condition false, a negated operator true, and aws:SourceIp is absent through a VPC endpoint | Holds (both facts are verbatim). The Spot-the-bug answer is correct. |
| 14 | 2-deep line 411 | A Deny on aws:RequestedRegion makes IAM calls fail unless it exempts them | Holds (`iam-global-service-single-endpoint-us-east-1`). |
| 15 | 2-deep line 447 | S3 MFA Delete cannot be applied to an IAM user | Holds (verbatim). |
| 16 | 2-deep line 545 | An external access analyzer covers only its own Region | Holds. |
| 17 | 2-deep lines 577 to 583 | 20 managed policies per role by default since 2026-08-19, not examinable yet | Holds (quota table and What's New). The presentation is risky (S5). |
| 18 | 2-deep line 573 | Role trust policy has a default length of 2048 characters | Holds. The maximum changed from 4,096 to 8,192 on 2026-05-05; the chapter does not use the maximum. |
| 19 | 3-do iam-t03 step 6 | The simulator applies the attached boundary, so PutObject is implicitDeny | Holds. The saved `API_EvaluationResult` and `API_SimulatePrincipalPolicy` pages carry `PermissionsBoundaryDecisionDetail`; the IAM user guide says a boundary "is included by default". |
| 20 | 2-deep lines 33 and 700; 4-say line 53 | Temporary credentials cannot be revoked; revoke the role's sessions | Holds (verbatim, `sts-temporary-credentials-cannot-be-revoked-permissions-can-change`, `iam-revoke-role-sessions-denies-credentials-issued-before`). |

Also confirmed: RCPs on 2024-11-13; the SSO rename on 2022-07-26; eight MFA devices since 2022-11-16; GetSessionToken up to 129,600 seconds; AssumeRole from 900 seconds and one hour by default; the 1 to 12 hour role maximum; PassRole as a permission with no CloudTrail event; one role per instance profile; and the trusted and trusting account terms.

## Hands-on tasks: security and cleanup

- Security is good. The tasks use CloudShell and no access keys. No IAM user is created. The test roles trust only `ec2.amazonaws.com`, and no instance profile is created, so the roles cannot be used. Every created resource is tagged `book=saa` and `task=<id>`. Each task has a cost line of $0, cleanup in the correct order, and the label.
- The cleanup cannot be verified as written (M1). This is the one blocking task defect.
- The example bucket name `saa-example-bucket` may be a real bucket in another account, because bucket names are global (S2).
- IAM is eventually consistent (the chapter teaches it in 2-deep line 27), so a simulation run right after `put-role-policy` can show the old result. The tasks give no warning (S3).
- If the CloudShell session restarts, `$ROLE_ARN` is empty and the simulator call fails with a confusing error (S4).

## Must-fix defects

**M1. FATAL. The verify step proves nothing.**
- **Where.** `3-do.md` iam-t02 Verify (line 137) and iam-t03 Verify (line 241); the source is `data/03-iam/tasks.json` `verify` of iam-t02 and iam-t03 (the Markdown is generated). The `tag:GetResources` entry in both Permissions lines.
- **What is wrong.** The canon fact `iam-tagging-api-getresources-no-iam-roles` says GetResources "does not currently support IAM users and roles". The expected empty list appears even when the role was not deleted, so she is told the cleanup worked when it may not have.
- **Fix.** Verify with `aws iam get-role --role-name saa-iam-t02` (and `saa-iam-t03`). Expect: "An error that says NoSuchEntity." Remove `tag:GetResources` from Permissions. Optionally add one sentence linked to `iam-tagging-api-getresources-no-iam-roles` to explain why the tag search does not work for roles. Re-run `tasks lint` and `check-cli`.

**M2. FATAL. The KMS gist cell is wrong for the default key policy.**
- **Where.** `1-fast.md` line 137, the "Same account, no deny or ceiling?" row, Identity-based column.
- **What is wrong.** "Enough, except for KMS keys: IAM policies cannot allow access to a KMS key" drops the scope of its fact ("unless the key policy explicitly allows it"). It contradicts the same quote, which says "The default key policy enables IAM policies." She trusts the gist and will answer that an IAM policy is never enough for a KMS key.
- **Fix.** Change the cell to: "Enough. For a KMS key, only if the key policy allows it: [IAM policies cannot allow access to a KMS key](...) unless the key policy allows it, and [the default key policy enables IAM policies](...)."

**M3. FATAL. The MFA enforcement recipe lets access keys through.**
- **Where.** `2-deep.md` line 445, the Stop-and-answer answer in the condition-keys subsection.
- **What is wrong.** "To enforce MFA, specify a Deny statement in any policy with the condition." A Deny with `Bool` and `aws:MultiFactorAuthPresent` set to `false` does not apply to requests signed with access keys, because the key is absent and the condition is then false. She would give customers a policy that access keys bypass. The linked FAQ fact is about Deny statements in general, not about MFA, so the sentence also says more than its fact.
- **Fix.** "To enforce MFA with a Deny, use BoolIfExists with aws:MultiFactorAuthPresent false: [adding IfExists to an operator makes a missing key evaluate as true](../facts/iam.md#iam-condition-missing-key-is-false-except-ifexists), so requests signed with access keys are denied too." Add one trap marker and one quiz or flashcard item for this case (Bool versus BoolIfExists).

**M4. The founders get IAM users, against the chapter's own best practice.**
- **Where.** `2-deep.md` decision record: the after-diagram alt text (line 608), step 4 (line 615), Trade-off (line 618). `4-say.md` Prompt 4: the 10-second answer (line 178), lines 190 and 198 to 200, the Skeleton (line 204) and Must say. The `iam-after.svg` spec.
- **What is wrong.** The story and the spoken answer recommend IAM users with MFA for people. The chapter's trap (2-deep line 151), the fact `iam-best-practice-human-users-federate-with-identity-center` and the quiz q020 answer all say people use roles through federation or Identity Center. The stated reason, "Callvale has one account", is not true in the canon: Identity Center covers "any AWS account managed using AWS Organizations", and an organization can have one account. She will say this to founders in her first customer weeks.
- **Fix.** Keep the decision for the workload (an instance profile role). For people, change it to: "Create an organization, enable IAM Identity Center with all features, and give Ana and Ben Identity Center users with MFA and a permission set. The root user has MFA and no access key." Trade-off: "one more service to set up, but no IAM users to remove later." Update Prompt 4 to match: "each of you signs in through IAM Identity Center with MFA". Do-not-say: "give each founder an IAM user". Regenerate the after-diagram. If the story bible requires IAM users, keep them only as a stated short-term exception and give a reason the canon supports.

## Should-fix items

- **S1.** 1-fast lines 184 to 188. In the root MFA "Old" line, add "before May 2024, no account type required it", which `iam-root-mfa-required-all-account-types` supports. Older practice questions assume that state, not the 2024 state.
- **S2.** 3-do iam-t02 and iam-t03 (`tasks.json`). Replace `saa-example-bucket` with a name that no customer can own, for example a bucket ARN that contains her own account ID, or AWS's documentation placeholder bucket name. Ground the placeholder if it is presented as reserved.
- **S3.** 3-do iam-t02 steps 3, 5 and 7, and iam-t03 steps 4 and 6. Add: "If the result looks old, wait a few seconds and run it again: an IAM change [can take some time](../facts/iam.md#iam-eventually-consistent-changes-replicate)." This also reinforces the fact.
- **S4.** 3-do iam-t02 and iam-t03. Before the first simulation, add a recovery line: `ROLE_ARN=$(aws iam get-role --role-name saa-iam-t02 --query Role.Arn --output text)`, for a CloudShell session that restarted.
- **S5.** 2-deep B-list line 577. Show both values: "10 (what older questions assume) / 20 (now, not examinable yet)", so that a skim of the table does not train the new number for the exam.
- **S6.** 2-deep lines 175 and 184. The caller's own sts:AssumeRole allow is also needed in one account when the trust policy names only the account. Reword to "when the trust policy names an account, not the principal, the caller's own policy must also allow sts:AssumeRole", and ground it from the Principal or trust-policy page.
- **S7.** 2-deep step 3, line 99, and the gates figure. Add one line: RCPs apply only to the services that support them. Mark it with xref 04 if the Organizations chapter teaches it.
- **S8.** 2-deep decision record, line 615. "In two groups" for two founders is unexplained. Remove it with the M4 change.
- **S9.** 1-fast Look first (iam-t01). Reading a trust policy does not by itself show that a role has no key. Add one sentence to the Expect line: access-key commands such as `list-access-keys` take a user name, and no such command exists for a role. This needs grounding, or keep the belief smaller: "a trust policy holds no password or key".
- **S10.** 1-fast line 171 and similar cells. Shorten long verbatim link texts in gist tables to the short "Write it as" display (the 2026-10-11 ruling on displays), for second-language skimming.
- **S11.** Economy. Collapse a few of the about 9 restatements of "both evaluations return Allow" (1-fast lines 138, 172 and 222; 2-deep lines 254 and 295; FAQ 9; 4-say) to a back-reference. This frees words in 2-deep, which is at 5,498 of 5,500.

## Result

- Must-fix: 4 (M1, M2 and M3 are FATAL; M4 is not FATAL).
- FATAL: true.
