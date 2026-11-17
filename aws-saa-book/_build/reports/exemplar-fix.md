# Exemplar and contract 1.0: fixes at the freeze (2026-10-11)

Input: `exemplar-critique-consistency.md` (C1 to C18) and `exemplar-critique-reader.md` (R1 to R22). Result: 39 fixed, 1 rejected, 0 deferred as a whole; the parts that need the orchestrator, the registrar or a tool change are listed under "Work orders". `STYLE.md` is marked "version 1.0 frozen 2026-10-11"; `SPEC.json` stays "1.0". Tests: `python3 aws-saa-book/tools/tests/run.py`, 798 tests, OK. Sandbox (`_build/tmp/exemplar-final/`, refreshed with every changed file): `lint 03 --draft` and `lint 10 --draft` have no error in a written block (only the slice structure: L201, L106 on stubs, VPC empty sections); `q lint`, `speak lint`, `tasks lint`, `cards lint 03` and `diagram lint iam-hero` have no errors.

## One line per finding

- C1 (blocker) fixed: `Exam signal` and `Exam heuristic` added to `callouts.not_counted_toward_callouts_max` (real and fixture SPEC, with `not_counted_reason`); `exam_signal_per_subsection` and `say_it_per_subsection` in deep and medium how counts; `brief_traps_max` deep 13, medium 7 (13, not 14, because R1 cuts the fast traps list to 4 to 5); exemplar brief cut from 17 to 13 traps (three merges as proposed, plus `iam-trap-external-id-secret` dropped; no question cited any of the four); CONVENTIONS E, CONVENTIONS-2 U1, U5 and decision 41.
- C2 (major) fixed: SPEC how counts `say_it_per_subsection`; R3 rows for both new keys, marked not implemented; `TOOLS.md` L402 text; `resolution.section_requires` names the D8/D9 callouts and reveals; `Say it` `use` text states the speech rule.
- C3 (major) fixed: new `TOOLS-rules.md` R11 rule map (rule, SPEC key, code, reviewer lens, "review until implemented") with the list of tool changes; STYLE 8 "Safety rules (checks: `TOOLS-rules.md` R9, R11)"; STYLE intro points to R11.
- C4 (major) fixed by relaxing the rule: STYLE 11.1, CONVENTIONS-2 U1 and README item 1 now say "a table when the trace has two or more cases" and "an `Exam heuristic` when no fact decides the stem phrase".
- C5 (major) fixed: deep Old line is `10 per role.` with `<!-- needs-display: iam-change-managed-policies-per-role-default-20 "10" -->`; the display request itself is a work order.
- C6 (major) fixed in the contract: CONVENTIONS F sentence, CONVENTIONS-2 F2 bullet, SPEC `fact_links.number_free_display_words_max` 8 and `number_free_display_rule` (real and fixture), R8 M7 note, STYLE 11.2; re-cutting the verified long displays is a work order for the orchestrator (decision 43).
- C7 (major) fixed: SPEC `verify_tag_patterns` gain `task=<task id>` patterns plus `tasks.verify_rule`; `tools/saalib/lab.py` T108 now replaces `<task id>` (one line, as T106 does); J5, STYLE 8 rule 5, decision 44; `iam-t02` verifies with `Key=task,Values=iam-t02`, expect "An empty list."; README "does not settle" names the fact request and the get-role fallback.
- C8 (major) fixed in the contract: SPEC `lint.term_rules` (per hand file, brief terms, prompts skipped, with the interim rule), CONVENTIONS-2 U6, decision 45, STYLE 4 example uses "network ACL NAK-ul"; the term-bank data fix and the W901 code change are work orders.
- C9 (major) fixed: SPEC `lint.abbreviation_rule` (only `services.json` names and the H1 are exempt, interim rule stated); exemplar expands MFA (fast Changed recently heading, deep root-user stub), AWS STS (fast hero step 1, `iam-hero.json`, brief `say`; deep role step 2) and ARN (deep Go deeper, before its first use); the bank shorts and the W802 code change are work orders.
- C10 (minor) fixed: STYLE 11.11 wording; CONVENTIONS-2 U3 gives a `not examinable yet` example.
- C11 (minor) fixed: second sentence in SPEC `grounding.exempt_sentences`; CONVENTIONS D6 and U3.
- C12 (minor) rejected: SPEC fast stays 20 minutes (the reader needs 20; R1's cuts bring the exemplar to 20 by its time boxes); README now says "the 20-minute file".
- C13 (minor) fixed: STYLE 1 wrong examples (unclear "it", noun stack), STYLE 3 analogy example; duplicated exemplar pointers removed from STYLE 6 and 7; exemplar gains `cards.json` (decide, differ, number "one hour", cannot) and `iam-q007` (difficulty 1); CONVENTIONS D8 sample shows Exam signal, Go deeper and Say it.
- C14 (minor) fixed: covered by C8 ("in each hand file").
- C15 (minor) fixed: `TOOLS.md` and `TOOLS-rules.md` titles 1.0; L402; W902 note points to R11.
- C16 (minor) fixed: fast cell "Either, except for KMS keys: [IAM policies cannot allow access to a KMS key]".
- C17 (minor) fixed: explicit deny "not an implicit one: a Deny statement causes it"; permissions policy "It is not the same as the trust policy."; VPC leads with the idea ("The firewall of a resource is a **security group**").
- C18 (minor) fixed: sandbox holds the 1.0 contract files and the fixed exemplar; `registry build` for `style_version` is a work order.
- R1 (blocker) fixed: SPEC deep fast signals 6 to 8 rows, traps 4 to 5, signals 380 words, changed 120, recap 3 prompts and 90 words; Check 150 words, not 120, because R20 adds three Predict paragraphs; `lint.minutes_formula.fast_check` and `resolution.minutes` note; CONVENTIONS C table; exemplar: Recap 3 and 4 deleted, signals rows MFA and Access Analyzer deleted, trap "keys on instance" deleted, Roles Anywhere row deleted (it repeated row 1's "But not if"), time boxes 2/3/3/2/3/3/1/2/1 = 20, front matter `{fast: 20, pass: 73, full: 161}` (formula values), `iam-t01` 3 minutes; the 1,400-word cap is a work order (RULINGS budget, decision 42).
- R2 (major) fixed: Predict 1 names the member account and the SCP; its answer links `iam-scp-allow-is-a-filter-not-a-grant` ("SCPs act as filters that specify the maximum permissions"), because the intersection display made a 32-word sentence.
- R3 (major) fixed: words row `trust policy`; Recap 3 and 4 deleted; Recap 3 asks what the signals table taught; CONVENTIONS-2 U4 and SPEC `prompts.recap_rule`; bank terms are a work order.
- R4 (major) fixed: "The short answer is: a request needs one allow and no deny. The thing to watch is a ceiling, such as an SCP." (the proposed text had 34 words).
- R5 (major) fixed: Go deeper retitled "exceptions to the implicit deny and to SCPs", with the SCP root-user sentence.
- R6 (major) fixed: `iam-s02` watch line, cue 4 and kp4/kp5 swapped; deep Say it "both sides have to say yes ... a KMS key: [neither policy alone is sufficient]"; CONVENTIONS-2 U2 and SPEC `Say it` use.
- R7 (major) fixed: fast Old line "management and standalone accounts required root user MFA; member accounts did not."; deep Old line per C5 (the proposed "10 managed policies ..." fails L304: a number with a count noun outside a link).
- R8 (major) fixed: NAT heuristic names older questions and the regional NAT gateway; the VPC brief entry is a work order (there is no VPC brief yet).
- R9 (major) fixed: federation split into an IAM Identity Center and a Cognito/Roles Anywhere subsection (14 subsections); condition keys cut to four, ABAC and data perimeter to Go deeper; stubs carry 4 minutes, not 5, because 14 subsections share at most 4,400 words (U1); How it works 59 minutes; brief sections and slots updated.
- R10 (minor) fixed: MFA, AWS STS, ARN spelled out; `iam-s03` cue "organizational units"; `iam-q003` say "administrators".
- R11 (minor) fixed: "ceiling" as noun and "limit" as verb in the words row, `iam-s03` (ten_second, lines 4 and 6), deep step 3 and the boundary stub.
- R12 (minor) fixed: "Maximum length of one customer managed policy", "Default length limit of a role trust policy", "Default quota of managed policies on one role" ("default maximum" would be wrong: 20 is the default quota, 25 the maximum).
- R13 (minor) fixed: NACL sentence uses the existing display "starting with the lowest numbered rule" and drops the "we" display; lowercase "the ID of a security group" and "connections must always be initiated ..." (the comparison ignores case); role cell "Temporary keys that AWS STS generates on request" with a `needs-display` marker; CONVENTIONS-2 F2 and STYLE 11.2 rule.
- R14 (minor) fixed: "Use them as a checklist: the result is the same in any order."; VPC sentence deleted; STYLE 11.3 and README failure 2 updated.
- R15 (minor) fixed: "Now count the charges"; NAT respelling dropped; heading "... charges hourly and per gigabyte" (14 words); gateway endpoint defined in bold with a fact link before the "Why" question.
- R16 (minor) fixed: step 3 names the RCP and links "an RCP never grants permissions".
- R17 (minor) fixed: least privilege "a broad AWS managed policy"; the `policy` row is gone (R3); "Whom does it apply to?".
- R18 (minor) fixed: `iam-s01` lines 3 and 9; `iam-s03` line 7 and kp1.
- R19 (minor) fixed: `iam-q001` option d why; `iam-q004` step 5 (README item 10 quotes the new text).
- R20 (minor) fixed: CONVENTIONS D1, SPEC `prompts.check_answers_predict`, U4 example; three reveals end with `**Predict <n>:**` paragraphs.
- R21 (minor) fixed: prompt "Does a principal keep a key, or does it get credentials from AWS?"; a diagram aside is left to the diagram agent (README).
- R22 (minor) fixed: full `simulate-custom-policy` command (syntax from the CLI example page in the corpus) with the expected result; `iam:SimulateCustomPolicy` added to permissions.

## Work orders (not done here)

- Orchestrator, term bank (`data/terms.json`): respelling null for least privilege, health check, hybrid, volume, durability, high availability, fault tolerance, fail over, blast radius, lifecycle rule, NAT gateway; `network-acl` respelling "NAK-ul"; add trust policy, permissions policy, implicit deny, explicit deny, permissions boundary, instance profile; add the shorts MFA (multi-factor authentication), ARN (Amazon Resource Name), RCP (resource control policy), OU (organizational unit). Then put `trust-policy` in the brief `terms`.
- Orchestrator: decide the 1,400-word fast cap (R1, RULINGS budget); decide whether verified displays over 8 words are re-cut (C6); run `registry build` and `status` for 00 to 03 so `style_version` follows SPEC 1.0 (C18).
- IAM registrar or writer (chapter 03): `facts request` for the displays "10" (`iam-change-managed-policies-per-role-default-20`) and "generated dynamically on request" (`sts-temporary-credentials-expire-not-stored`); `facts request --question "Does the Resource Groups Tagging API GetResources operation return IAM roles?" --where "data/03-iam/tasks.json#iam-t02"`. Not filed here, so that no open request blocks the counts gate of the live chapter 03.
- VPC writer (W2): Changed recently entry for `vpc-regional-nat-gateway-change` in the VPC brief and fast file; fact request for the default deny of a custom network ACL.
- Tool owner (all listed in `TOOLS-rules.md` R11): L106 `say_it_per_subsection` and `exam_signal_per_subsection`; L107 placement; W901 per file and brief; W802 exemption by `services.json`; M7 display length; `gate_brief` `brief_traps_max`; W105 `fast_check`; Q114 strict twins; T108 get-role exception.
- Diagram agent: optional aside on `iam-hero` ("on EC2, AWS makes this call").

## Files changed

`_build/style/`: `STYLE.md`, `CONVENTIONS.md` (4,900 of 4,900 counted words), `CONVENTIONS-2.md` (section U, decisions 41 to 46, J5, F2), `SPEC.json`, `TOOLS.md`, `TOOLS-rules.md` (R3, R8, R9, R11); `_build/style/exemplar/`: `README.md`, `iam-1-fast.md`, `iam-2-deep.md`, `vpc-2-deep-slice.md`, `questions.json`, `speak.json`, `tasks.json`, `cards.json` (new), `iam-hero.json`, `iam-brief.json`; `tools/saalib/lab.py` (T108 `<task id>`); `tools/tests/fixtures/book/_build/style/SPEC.json` (new keys only, values unchanged); sandbox copies in `_build/tmp/exemplar-final/`.
