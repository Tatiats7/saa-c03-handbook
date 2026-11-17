# IAM chapter (03): exam-validity acceptance review

Lens: SAA-C03 item writer and exam-preparation expert. Date: 2026-10-12.
Read: RULINGS.md, READER.md, 03-iam/1-fast.md, 2-deep.md, 4-say.md, 5-quiz.md (all 18 shipped items), data/03-iam/questions.json (22 items: 18 ready, 3 verified-not-shipped, 1 rejected), registry show 03, FREQUENCY.md rows for IAM (research input only), fact records for the facts the quiz leans on.

## Verdict

Ship after two small fixes. The 18 items are sound: every key is correct, the qualifiers are single and exam-like, option lengths are balanced (no length cue), and both twin pairs turn on one deciding phrase. The weak points are outside the quiz keys: one unsafe MFA-policy sentence in 2-deep.md, one Signals row whose gist contradicts the chapter's own trap, an uncovered bullet (1.1.S6), and no question that asks the reader to read policy JSON.

## Scores (1 to 5)

| Criterion | Score | Why |
|---|---|---|
| Learnability for this reader | 4 | Short subsections, time boxes, Stop-and-answer, a think-aloud on both worked items, a one-line Takeaway on every item. Mid-sentence fact links sometimes break the grammar ("[... determines what the temporary credentials](...) can do"). The first item she meets is the hardest format (multi-select, extended, difficulty 3). |
| Exam discrimination power | 4 | The twins q001/q005 and q002/q006 are textbook cases. Distractors are plausible, and 21 of 54 are "it works, but" options that train qualifier reading. There is no policy-JSON item, though FREQUENCY lists "reading policy JSON". Some stems give the answer away (q008: "written for an old job that no longer runs"). |
| Technical precision | 4 | All 18 keys hold. Defects: an MFA Deny sentence that fails for access keys (2-deep), the cross-account bucket-policy signal (1-fast), the q024 key that has no enforcement, and the q006 explanation that gives the wrong reason. |
| Reusable explanations | 4 | Why / Why not / Twin / Takeaway / Review is a reusable pattern. Most Why-not lines name the misconception in plain words. The q021 twin is vague. |
| Retention design | 4 | Predict, Check, Recap, trap ids, twins and spoken prompts form a loop. But 37 of 54 distractors have no `misconception`, and none links its `trap` id, so wrong answers do not feed the trap deck. |
| Economy | 4 | Explanations are tight. The multi-select items repeat their Why sentence in the bullets below it (q004, q023, q025). |
| Grounding hygiene | 3 | Every link resolves to a verified fact. But 172 of 270 number-free displays used in the chapter are paraphrases or longer than 8 words, against the 2026-10-11 display ruling, and a few links cite a fact that does not carry the sentence's claim (see must-fix 1 and should-fix 5). |

## Must-fix (2)

**M1. 2-deep.md, "Condition keys narrow an allow ..." subsection, Stop-and-answer answer (the MFA script question).**
What is wrong: "To enforce MFA, [specify a Deny statement in any policy](../facts/iam.md#iam-faq-restrict-with-deny-statement) with the condition." The reader will write `Deny` + `Bool aws:MultiFactorAuthPresent false`. A request signed with an IAM user's access key does not carry the key at all, so the plain `Bool` condition is false and the Deny does not apply. The same subsection teaches that a missing key makes the condition false. This is the classic MFA-policy trap, and the sentence teaches the trap as the fix. The cited FAQ fact is also generic ("To restrict access, specify a Deny statement in any policy") and says nothing about MFA.
Fix: either delete the sentence (the answer "No: long-term access keys do not include it" is complete), or replace it with: "To deny requests without MFA, use BoolIfExists with the value false: with plain Bool, a missing key makes [the condition false](../facts/iam.md#iam-condition-missing-key-is-false-except-ifexists) and the Deny does not apply." Check first that the IfExists fact's quote carries the IfExists exception. Keep q025's allow-with-true pattern as the taught pattern.

**M2. 1-fast.md, Signals and traps table, row "another account reads the bucket and keeps its own permissions".**
What is wrong: "Think: bucket policy." On its own, that is the false belief that trap 4 in the same section (and q004, FAQ 9) corrects: across accounts, a bucket policy alone is an implicit deny. The reader trusts the gist from one glance, and READER.md requires tables to give a correct gist on their own.
Fix: change Think to "bucket policy that names the principal, plus an allow in the caller's own policy". Keep the "but not if" (no resource-based policy: use a role).

## Should-fix

1. **Coverage, bullet 1.1.S6 (federate a directory service with IAM roles).** No shipped question carries it (q022 was rejected). The prose covers only Identity Center identity sources and one AD Connector trap. SAML 2.0 federation directly to IAM (an IdP entity, AssumeRoleWithSAML, console SSO without IAM users) is not taught, although verified facts exist: `iam-federation-with-iam-per-account-saml-or-oidc`, `iam-federation-saml-console-sso-without-iam-users`, `iam-federation-idp-entity-oidc-or-saml`. Add one row to the Cognito / Roles Anywhere table ("employees in an existing SAML IdP, one account": IAM SAML federation) and one item, or confirm that chapter 05 ships an S6 question before W14. Chapter 05 is not built yet.
2. **Missing item type: reading policy JSON.** FREQUENCY reports it as an IAM sub-topic, and the real exam shows policy documents. All 18 items are prose-only. The two Spot-the-bug blocks in 2-deep are good material: promote one JSON item into the extended set, for example the NotIpAddress Deny that breaks VPC-endpoint access, or a Deny + Condition statement where the reader picks the effect. The verified-but-unshipped q007 (group as principal) could be recast as a JSON item.
3. **Commonly tested topics with verified facts but no teaching:** ABAC with tags (5 verified facts: `iam-faq-abac-*`, `iam-abac-*`), policy variables / a per-user S3 prefix (`iam-policy-variables-where-and-version`), and the IAM password policy (`iam-password-policy-*`). Add a one-row mention or a Go-deeper block each: ABAC as "permissions that follow tags, for fast-growing teams"; `${aws:username}` home prefixes; "the password policy does not apply to the root user or to access keys". Also aws:PrincipalOrgID: q012 was verified and then cut, so the topic now lives only in prose. Consider swapping it in for one of the six 1.1.S3 items.
4. **Bullet balance and tags.** 1.1.S3 carries 6 of 18 items. q025 (MFA for IAM users) is tagged 1.3.K1 but tests 1.1.S1. q027 (STS session revocation) is tagged 1.1.S2 and fits 1.1.S3. q011 (PassRole least privilege) fits 1.1.S2/1.1.K4. Retag these. 1.3.K1 then needs a real carrier: q026 (Access Analyzer) can take it.
5. **q006, Why not for the bucket-policy option.** It cites "[the permissions are not cumulative]" as the reason. The real reason is that the caller inside the session is the production-account role, so a bucket policy that names the development account does not match it. Rewrite the line around the principal. In q002, the same option's second clause ("across accounts AWS allows the request only if both evaluations return Allow") is beside the point. Cut it.
6. **q024 key.** "Set a managed policy ... as the permissions boundary of each role that the developers create" does not say how the boundary is enforced. A developer could create a role without it. Append "and require it with the iam:PermissionsBoundary condition on iam:CreateRole" (fact `iam-condition-key-permissions-boundary`). This makes the key airtight against an ambiguity challenge.
7. **Twin leakage.** q001's Twin line states the answer to q005, and q002's states the answer to q006. Both twins ship as separate items later in the same file. If quiz scores feed a readiness gate, these two items measure recall, not reasoning. Either replace those two Twin lines with a different variant (for example "Lambda function" or "the call fails across accounts and the caller's own allow is missing") or exclude the second twin from gate scoring.
8. **Distractor metadata.** 37 of 54 distractors have `misconception: null`, and every `trap` is null. Name the misconception on each distractor and link the chapter traps that already exist: q004 c → iam-trap-wildcard-principal-means-account, q004 e and q024 c → iam-trap-scp-grants, q008 b/d → iam-trap-allow-beats-deny, q006 c → iam-trap-role-adds-permissions, q013 a/b → iam-trap-kms-without-key-policy, q026 a → iam-trap-access-analyzer-global, q026 b → iam-trap-audit-tool-shows-activity, q010 a → iam-trap-cognito-vs-identity-center, q020 b → iam-trap-boundary-limits-root, q027 a → iam-trap-revoke-temporary-credentials, q023 b → iam-trap-trust-policy-grants-actions, q023 d → iam-trap-external-id-chosen-by-customer. This closes the loop from a wrong answer to a trap card.
9. **Display ruling (grounding).** 172 of 270 number-free displays used by this chapter are paraphrases or longer than 8 words. Examples: "AdministratorAccess grants all actions for all services and resources" (9 words, paraphrase, and filed under a fact named `...poweruseraccess...`), "An SCP never grants permissions" (the quote says "SCPs do not grant permissions"), "except IAM, AWS Organizations and AWS Account Management". The 2026-10-11 audit already reports this. Re-register the displays as verbatim phrases of 8 words or fewer before the W14 audit, or the chapter will fail re-derivation on wording alone.
10. **Signals table additions (1-fast).** The 7 rows are real and their guards hold. Add two high-yield rows: "only accounts in our organization" → aws:PrincipalOrgID (but not if: named partner accounts outside the organization); "kms:Decrypt is allowed in IAM, but access is denied" → key policy (but not if: the key policy enables IAM policies). Also, the boundary row's guard "the limit covers a whole account: SCP" should say "every principal in member accounts", because a standalone account has no SCP.
11. **4-say.md, Prompt 4.** The 10-second answer ("do daily work with your own IAM users") is consistent with the story, but it is the opposite of the exam key in q020 and of trap iam-trap-iam-users-for-people. She will say it to founders. Add "AWS recommends IAM Identity Center; IAM users with MFA are a stopgap while you have one account" to the 10-second line.
12. **Order and economy in 5-quiz.md.** Print worked q001 (single answer, core) before q004 (multi-select, extended). In q004, q023 and q025, the bullet list under Why repeats the Why sentences. Keep one.
13. **q021 Twin.** "the company owns more of the stack" names no deciding answer. Say "the company also patches the guest operating system and the database software".
14. **Stem scaffolding.** q008 ("written for an old job that no longer runs") and q013 (deciding phrase "manages its own keys", which decides nothing) carry phrases that either give the answer away or mislabel what decides it. Change q008 to "The Deny statement is no longer needed" and drop "manages its own keys" from q013's deciding phrases. "The key policy has one statement" is the deciding phrase.

## Item-by-item notes (keys checked)

| # | id | Key correct | Qualifier | Notes |
|---|---|---|---|---|
| 1 | q004 | yes (A,B) | MOST securely | Good multi-select. The wrong-path step is real. |
| 2 | q001 | yes | LEAST overhead | Twin of q005. The Twin line leaks q005's answer (S7). |
| 3 | q002 | yes | LEAST overhead | Twin of q006. One explanation clause is beside the point (S5). |
| 4 | q003 | yes | LEAST overhead | Root-vs-each-account attachment is a good discriminator. |
| 5 | q008 | yes | LEAST overhead | The stem over-signals (S14). |
| 6 | q009 | yes | LEAST overhead | Clean workforce item. |
| 7 | q005 | yes | LEAST overhead | Clean. |
| 8 | q020 | yes | none | Clean. Best-practice register. |
| 9 | q021 | yes | none | Easy (difficulty 1). Three distractors from the AWS side. Vague twin. |
| 10 | q006 | yes | LEAST overhead | Wrong reason in one Why-not (S5). |
| 11 | q010 | yes | MOST securely | Good: B vs D isolates least privilege. |
| 12 | q011 | yes | LEAST overhead | Strong PassRole item. Retag (S4). |
| 13 | q013 | yes | LEAST overhead | Strong KMS item. |
| 14 | q024 | yes | LEAST overhead | Add enforcement to the key (S6). |
| 15 | q025 | yes (B,D) | LEAST overhead | Correct and grounded. Retag to 1.1.S1. |
| 16 | q027 | yes | LEAST overhead | Strong. Names the "revoke one token" misconception. |
| 17 | q023 | yes (C,E) | MOST securely | Strong. Covers the confused deputy fully. |
| 18 | q026 | yes | LEAST overhead | Strong. Regional-analyzer twin with the unused-access analyzer. |

Counts check: 9 core, 9 extended, 2 worked (1 with wrong path), 2 twin pairs, 3 multi-select. All match SPEC.json. Correct-answer positions: A 3, B 4, C 4, D 4 (balanced).

## Signals and traps (1-fast.md)

- Signals: 7 rows. All are real exam phrasings. Six guards hold. The bucket-policy row fails (M2).
- Traps: all 5 are common, real beliefs, and each one is corrected with a fact link. Trap 3 (AdministratorAccess or root vs SCP) is especially high-yield.

## Coverage of exam-guide bullets (registry 03)

| Bullet | Prose | Shipped items |
|---|---|---|
| 1.1.K1 multi-account access | yes | q003, q026 |
| 1.1.K2 federation and identity services | yes | q009, q010 (q005 by content) |
| 1.1.K4 least privilege | yes | q024, q026 |
| 1.1.K5 shared responsibility | thin (one trap) | q021 |
| 1.1.S1 root and IAM user best practices, MFA | yes | q020 (q025 by content) |
| 1.1.S2 flexible authorization model | yes; no ABAC | q008, q027 |
| 1.1.S3 RBAC, STS, cross-account | yes | 6 items |
| 1.1.S5 resource policies | yes | q004 |
| 1.1.S6 federate a directory with IAM roles | partial; no SAML-to-IAM | none (S1) |
| 1.3.K1 data access and governance | yes (Access Analyzer) | q025 by tag only (S4) |
| 1.3.S4 access policies for encryption keys | yes | q013 |
