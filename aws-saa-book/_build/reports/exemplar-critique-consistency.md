# Exemplar and contract 1.0: consistency check (2026-10-11)

Scope: `_build/style/exemplar/`, `STYLE.md` 1.0, `SPEC.json` 1.0, `CONVENTIONS.md` 1.0, `CONVENTIONS-2.md` 1.0, `_build/reports/exemplar-spec-changes.md`, checked against `RULINGS.md`, `READER.md`, `TOOLS.md`, `TOOLS-rules.md` and `TOOLS-items.md`. No contract or exemplar file was edited.

Result: **1 blocker, 8 major, 9 minor.**

## Checks run

| Check | Result |
|---|---|
| `tools/tests/run.py` | 798 tests, OK |
| Fixture `lint 99 --draft` (`--book-dir tools/tests/fixtures/book`) | 0 errors; warnings as documented in `TOOLS.md` 0.13 (3 W901, W307) plus L601/L101 "run sync" |
| `lint 03 --draft` (sandbox `_build/tmp/exemplar-final/`) | 11 errors: L201 (3,059 of 3,500 words) and L106 on the ten "Planned:" stubs; 43 warnings (16 W901 in the fast file, W307 x4, W601 x2, L903/W201 on stubs) |
| `lint 03` (no draft) | adds L905 x11: brief traps that no hand file holds (see finding 1) |
| `lint 10 --draft` | slice-structure errors only (L101 1-fast.md, L201, L106, L107 in the empty sections); W901 x7, including `network ACL` respelling |
| `q lint 03` | 0 errors; Q201, Q204 x2 |
| `speak lint 03` | 0 errors; P201 |
| `tasks lint 03` | 0 errors; T201, T113 |
| Sandbox = exemplar | `iam-1-fast.md`, `iam-2-deep.md`, `vpc-2-deep-slice.md`, `questions.json`, `speak.json`, `tasks.json`, `iam-hero.json`, `iam-brief.json` and `SPEC.json` are identical to the sandbox copies; the sandbox `STYLE.md`, `CONVENTIONS.md`, `CONVENTIONS-2.md` are the 0.9 versions (finding 18) |

Raw outputs: `_build/tmp/consistency-check/`.

## Findings

### 1. Blocker: a deep chapter cannot follow STYLE 11.1 and the brief within `callouts_max`

- **Place.** `STYLE.md` 11.1; `SPEC.json` `templates.deep.files[2-deep.md].callouts_max` (12) and `callouts.not_counted_toward_callouts_max`; `TOOLS-rules.md` L905; `exemplar/iam-brief.json` `traps`.
- **What is wrong.** STYLE 11.1 (and README item 1) put one `Exam signal` in every How-it-works subsection. `Exam signal` still counts toward the limit of 12 (only `Changed recently` and `Say it` are exempt). The IAM brief has 13 subsections, so 13 Exam signals alone exceed 12 (L402, blocking). In addition, the brief has 17 trap ids; the fast traps list holds at most 6 (`signals.counts.traps`), and `lint 03` without `--draft` reports the other 11 as L905. The only other place for a trap id is an `Exam trap` callout in `2-deep.md` (CONVENTIONS D5), which also counts. Total counted callouts for the IAM chapter as specified: 13 signals + 11 traps + at least 2 `Try it` = 26 against 12. CONVENTIONS-2 decision 36 used exactly this arithmetic to exempt `Say it`, but did not apply it to the device that 11.1 also makes per-subsection. The IAM writer of W1 hits this on the first full draft.
- **Exact change.**
  1. `SPEC.json` (and the fixture copy): `"not_counted_toward_callouts_max": ["Changed recently", "Say it", "Exam signal"]`; add to `templates.deep...sections[how].counts` and `templates.medium...sections[how].counts` the key `"exam_signal_per_subsection": 1`.
  2. `CONVENTIONS.md` E, last paragraph: "`Changed recently`, `Say it` and `Exam signal` callouts do not count." Add CONVENTIONS-2 decision 41: "Exam signal: one per How-it-works subsection (STYLE 11.1), not counted toward `callouts_max`, for the reason of decision 36."
  3. Cap the brief so the traps fit: add `SPEC.json` `templates.deep.counts.brief_traps_max: 14` (6 in the fast list + 8 `Exam trap` callouts, leaving room for 2 to 3 `Try it` and 1 `Startup example` in 12), checked by `gate_brief`; medium `brief_traps_max: 7`. Cut `exemplar/iam-brief.json` `traps` from 17 to 14 (merge `iam-trap-boundary-grants` into `iam-trap-scp-grants`, `iam-trap-trust-policy-enough` into `iam-trap-cross-account-one-policy`, and `iam-trap-root-escapes-scp` into `iam-trap-admin-ignores-scp`, or drop three that no question cites).

### 2. Major: the 1.0 device "Say it per subsection" has no SPEC key and no lint code

- **Place.** `STYLE.md` 11.1; `CONVENTIONS.md` D8; CONVENTIONS-2 decision 36; `SPEC.json` how-section `counts`, `resolution.section_requires`, `callouts.labels[Say it].use`; `TOOLS.md` L106, L402; exemplar-spec-changes 5.5.
- **What is wrong.** The rule is mechanical (count `Say it` callouts per H3, check that the next block is the Stop and answer, check the two starters), but it lives only in the `use` text, which the lint does not read. `resolution.section_requires` says "a section must hold only what its counts, fields and subsection_fields name", so a How section that holds `Say it` callouts contradicts SPEC itself. `TOOLS.md` L402 still says only "`Changed recently` entries are not counted", although the lint already reads the 1.0 list from SPEC.
- **Exact change.** `SPEC.json` deep and medium how `counts`: add `"say_it_per_subsection": 1`. `TOOLS-rules.md` R3 count table: add the row "`say_it_per_subsection` | `Say it` callouts in each H3; the callout is the block directly before the `Stop and answer.` prompt and starts with `The short answer is`, and holds `The thing to watch is`" (L106). Until the tool change lands, mark the rule "(review: claims reviewer)" in CONVENTIONS D8. `TOOLS.md` L402 text: "(`callouts.not_counted_toward_callouts_max` are not counted)". Change `resolution.section_requires` to "... name, plus the callouts and reveals of CONVENTIONS D8; a role adds grounding rules, never devices".

### 3. Major: STYLE 1.0 marks no rule as review-only, and several checkable rules have no key or code

- **Place.** `STYLE.md` sections 1 to 11; `TOOLS.md` 6.1; `TOOLS-rules.md` R3.
- **What is wrong.** No STYLE rule says how it is checked, and no table maps STYLE rules to codes. Rules a reviewer must check, unmarked: 1 (one main idea, active voice, condition first, repeat the noun, keep "that", noun stack, no double negatives, modal meanings), 2 (plain words, the five term steps, collocations), 3 (idioms beyond the banned list, one analogy, no history, pricing tables or click paths in prose), 5 (bold use, tone, Stop and answer target 70 to 85%), 6 (script works when a word is lost; follow-up covers every case), 7 (four-part stem order, parallel options), 11.2 to 11.10, 11.12 (evidence, diagram actors, chapter numbers). Checkable rules without a key and code: 11.1 order and devices (findings 1, 2), 11.11 placement and closing sentence (`changed_recently.placement` exists, `_changed_entry` ignores it), J2 strict twins (no key; Q114 only proposed), STYLE 8 rule 5 "verify ... must return nothing" (finding 7), STYLE 5 cast names (`startup.cast` exists; `TOOLS.md` W902 says "not implemented"). STYLE 8 also says "Safety rules, all checked", which is not true for rule 5 and the tutorial half of rule 8.
- **Exact change.** Add `TOOLS-rules.md` section R11 "STYLE 1.0 rule map" (STYLE has 1 word of budget left): one row per STYLE rule with columns `Rule | SPEC key | Code | Else: reviewer lens`. Fill it from this list: lint-checked rules with their codes (W202/L202, L803, L801/W801, L901, L802, W802, W901, L106, L202, L702/L703, W902, Q/P/T/C codes); the review-only rules above with the lens (reader lens, claims reviewer, exam-validity lens); and for the three checkable gaps the planned code (L106 `say_it_per_subsection` and `exam_signal_per_subsection`, L107 placement, Q114 strict twins) marked "review until implemented". In STYLE 8, replace "Safety rules, all checked:" with "Safety rules (checks: `TOOLS-rules.md` R9, R11):".

### 4. Major: two of five exemplar subsections lack the table, one lacks the Exam signal that STYLE 11.1 requires

- **Place.** `STYLE.md` 11.1; README item 1; `exemplar/iam-2-deep.md` lines 76 to 125 ("A role gives temporary credentials ..."); `exemplar/vpc-2-deep-slice.md` lines 70 to 120 ("A NAT gateway lets private instances ...").
- **What is wrong.** 11.1 lists "a table that compresses it" and "an `Exam signal`" as parts of every subsection. The IAM role subsection has no table. The NAT gateway subsection has no table and uses an `Exam heuristic` instead of an `Exam signal`. Writers who copy the exemplar break the rule; writers who obey the rule add tables that compress nothing.
- **Exact change.** `STYLE.md` 11.1: "a numbered trace, a table that compresses it when the trace has two or more cases, one ... reason, an `Exam signal` (or an `Exam heuristic` when no AWS fact decides the stem phrase), Go deeper, ...". Same wording in README item 1. If the panel wants the stricter rule instead, add to the NAT subsection a `plain` table "| Charge | When it applies | How to remove it |" with the three charges, and an `Exam signal` ("\"data processing charges\" points to a gateway endpoint for Amazon S3, because ...", with the `vpc-gateway-endpoint-no-hourly-or-processing-charge` link), then re-check W201 (400 words).

### 5. Major: the exemplar's not-examinable entry repeats the failure that STYLE 11.11 and README failure 8 forbid

- **Place.** `exemplar/iam-2-deep.md` line 254; `STYLE.md` 11.11; `CONVENTIONS.md` D6; README "ten most common ways" item 8.
- **What is wrong.** The Old line reads "**Old:** 10 per role: the default quota rose [from 10 to 20](...)". README item 8 names "an Old line that gave the change ('the default quota rose from 10 to 20') instead of the old value" as a failure, and STYLE 11.11 says the Old line holds "10 per role", not the change. The canon cannot support the correct form yet: `iam-change-managed-policies-per-role-default-20` has the displays "from 10 to 20" and "25" only, so a link whose text is "10" fails L303.
- **Exact change.** File `facts request --chapter 03 --service iam --fact iam-change-managed-policies-per-role-default-20 --display "10" --where "2-deep.md#numbers-that-decide-answers"` (the value is `changed.was`, and the What's New quote holds it). Then line 254 becomes `> **Old:** [10](../facts/iam.md#iam-change-managed-policies-per-role-default-20) per role.<br>`. Until then: `> **Old:** 10 per role. <!-- needs-display: iam-change-managed-policies-per-role-default-20 "10" --><br>`.

### 6. Major: the exemplar models fact displays far longer than RULINGS allows, and the contract does not state the RULINGS limit

- **Place.** `RULINGS.md` "Displays of number-free facts (2026-10-11)"; `CONVENTIONS.md` F; `SPEC.json` `fact_links`; `TOOLS-rules.md` R8 M7; every exemplar Markdown file.
- **What is wrong.** RULINGS: a display of a fact without numbers is at most 8 words, copied verbatim. The facts that the exemplar links carry 95 number-free displays of 9 to 25 words, and the exemplar's link texts use them throughout, for example 21 words (`vpc-natgw-troubleshoot-route-placement`, VPC slice line 105), 19 (`iam-scp-faq-effective-permissions-intersection`, fast file line 137), 17 (`vpc-def-security-group`, VPC slice line 19; `vpc-natgw-one-az-redundant-in-zone`, line 96), 13 (`iam-eval-implicit-deny-by-default`, deep line 53). STYLE 11.2 ("A link carries its whole sentence") and the exemplar together teach writers to request long displays, and no contract file (CONVENTIONS F, F2, SPEC, M7) states the 8-word limit, so writers learn it only when a registrar refuses their request.
- **Exact change.** `CONVENTIONS.md` F, third bullet, add: "A display of a fact without numbers is a verbatim phrase of at most 8 words (RULINGS 2026-10-11); a `needs-display` request follows the same rule." `SPEC.json` `fact_links`: add `"number_free_display_words_max": 8`. `TOOLS-rules.md` R8 M7: add "a display without a digit has at most `number_free_display_words_max` words" (registrars enforce it at merge, as RULINGS says). STYLE 11.2: add "The link text is the short display; the rest of the sentence carries the scope in plain words." The orchestrator decides whether the verified 03 and 10 displays are re-cut now (then the exemplar link texts must be rewritten to the new displays) or grandfathered (then RULINGS needs a scope line).

### 7. Major: the Try task's verify step rests on an ungrounded behaviour and cannot "return nothing"

- **Place.** `exemplar/tasks.json` `iam-t02.verify`; `STYLE.md` 8 rule 5; `CONVENTIONS-2.md` J5 ("The verify command filters by the tag `book=saa`") and decision 40; `SPEC.json` `tasks.verify_tag_patterns`; `TOOLS-rules.md` T108; `RULINGS.md` hard rules 1 and 9.
- **What is wrong.** (a) The verify uses `resourcegroupstaggingapi get-resources`; no fact says that this API lists IAM roles, and a corpus search finds no supported-resources page. If it does not, the verify prints an empty list while the role still exists, so it verifies nothing: an ungrounded "can" behind a RULINGS rule 9 step. Decision 40 freezes this knowingly. (b) STYLE 8 rule 5 says the verify "must return nothing", but SPEC and J5 force a `book=saa` filter, which also returns every other book resource that she has not cleaned up yet; the exemplar softens `expect` to "An empty list, or no ARN that contains saa-iam-t02", which contradicts STYLE.
- **Exact change.** `SPEC.json` `tasks.verify_tag_patterns`: add `"Key=task,Values=<task id>"` and `"tag:task,Values=<task id>"`; `CONVENTIONS-2.md` J5: "The verify command filters by the tag `task=<task id>`." For `iam-t02`, file `facts request --chapter 03 --service iam --question "Does the Resource Groups Tagging API GetResources operation return IAM roles?" --where "data/03-iam/tasks.json#iam-t02"` (page to fetch: the Resource Groups Tagging API supported-services page). If the fact verifies: verify command `aws resourcegroupstaggingapi get-resources --tag-filters Key=task,Values=iam-t02 --query "ResourceTagMappingList[].ResourceARN"`, expect "An empty list." If it does not: implement the T108 exception of exemplar-spec-changes 5.2 and use `aws iam get-role --role-name saa-iam-t02`, expect "An error that says NoSuchEntity." Update README "What this exemplar does not settle" accordingly.

### 8. Major: W901 contradicts STYLE 5 and SPEC `devices.term_definition`, so the frozen fast file cannot be warning-free

- **Place.** `SPEC.json` `lint.term_rules`, `devices.term_definition`; `STYLE.md` 4 and 5; `data/terms.json`; `exemplar/iam-1-fast.md` (16 W901); `exemplar/vpc-2-deep-slice.md` line 19.
- **What is wrong.** (a) W901 asks that the first use in the chapter of every bank term be bold. It fires on terms that belong to other chapters (`instance`, `bucket`, `object`, `queue`, `function`, `secret`, `on premises`, `hybrid` in the IAM chapter) and on terms first used in Predict prompts. STYLE 5 allows bold only "for a term at its definition", and `devices.term_definition` makes the words table the definition in the fast file, so obeying W901 breaks STYLE 5. (b) STYLE 4 (new in 1.0) says "Respell only a word she can mispronounce, not a common word such as least privilege", but `data/terms.json` still respells `least privilege` (leest PRIV-ih-lij), `health check`, `hybrid`, `volume`, `durability`, `high availability`, `fault tolerance`, `fail over`, `blast radius`, `lifecycle rule`, and W901 requires the respelling whenever the bank has one. (c) The respelling of `network ACL` is "NAK-ul (spoken short form)", so the VPC slice's correct "(NAK-ul)" fires W901.
- **Exact change.** `SPEC.json` `lint.term_rules`: "W901: the first occurrence, in each hand file, of a term that the chapter's `brief.json` lists in `terms`, outside prompt paragraphs, is bold (or is cell 1 of a words table) and is followed by `(respelling)` when the term has one." Orchestrator data fix in `data/terms.json`: set `respelling` to null for the common words listed in (b) (keep `route table`, `principal`, `ephemeral`, `throughput`, `latency`: real ESL stress traps), and set `network-acl.respelling` to "NAK-ul". Add the IAM core terms (trust policy, permissions policy, implicit deny, explicit deny, permissions boundary, instance profile) so the four W307 markers clear.

### 9. Major: STYLE 11.12 "expand every abbreviation (RCP, AZ)" is contradicted by the SPEC key and broken by the exemplar

- **Place.** `STYLE.md` 2 ("Spell out every abbreviation at first use in each file") and 11.12; `SPEC.json` `lint.abbreviation_rule`; `tools/saalib/lint.py` line 1999; `exemplar/iam-1-fast.md` lines 53, 130, 151; `exemplar/iam-2-deep.md` lines 88, 236.
- **What is wrong.** `abbreviation_rule` exempts "an official service name (kind aws-name)", and the lint skips every term of kind `aws-name`, which includes `Availability Zone` (short `AZ`), `service control policy` (`SCP`) and `virtual private cloud` (`VPC`). So the AZ example in STYLE 11.12 is never checked. The exemplar also leaves MFA (fast file lines 130, 151; deep line 236), ARN (deep line 88) and AWS STS (fast file line 53) unexpanded; none of them is in the bank, so W802 cannot see them.
- **Exact change.** `SPEC.json` `lint.abbreviation_rule`: "the short forms are the `short` values of data/terms.json; a name in `_build/registry/services.json` and the H1 are exempt; every other short form (AZ, SCP, VPC) needs its full term first in each file". Lint line 1999: skip only terms whose `term` is an official service name. Bank: add `multi-factor authentication` (short MFA), `Amazon Resource Name` (ARN), `resource control policy` (RCP), `organizational unit` (OU). Exemplar: fast file line 130 column 2 "multi-factor authentication (MFA) condition in the policy"; line 53 and the matching `say` of step 1 in `iam-hero.json` and the brief: "The principal asks AWS Security Token Service (AWS STS) to assume a role."; deep line 88 "with the Amazon Resource Name (ARN) of the role"; deep line 236 column 2 "Multi-factor authentication (MFA) devices for one user or the root user".

### 10. Minor: STYLE 11.11 says the entry "ends" with the warning sentence; the exemplar and D6 put it before the Status line

- **Place.** `STYLE.md` 11.11; `CONVENTIONS.md` D6; `exemplar/iam-2-deep.md` line 256.
- **What is wrong.** The sentence "Do not let this number decide an answer." ends the `The exam probably expects:` line; the entry ends with `**Status:** not examinable yet.` (L107 requires that order). D6 has no example of a `not examinable yet` entry.
- **Exact change.** STYLE 11.11: "... under the B-list, and its `The exam probably expects:` line ends "Do not let this number decide an answer."" Add to D6 a second example: `> **Changed recently:** (2026-08-19) Default number of widgets on a shelf.<br>` / `> **Old:** [200 widgets](...).<br>` / `> **Now:** [500 widgets](...).<br>` / `> **The exam probably expects:** the old value, if any. Do not let this number decide an answer.<br>` / `> **Status:** not examinable yet.`

### 11. Minor: a fast file whose only changes are not examinable must print a false sentence

- **Place.** `CONVENTIONS.md` D6 last sentence; `SPEC.json` `grounding.exempt_sentences`; `callouts.changed_recently.placement`.
- **What is wrong.** When every entry of a chapter moves to `2-deep.md`, the fast section has 0 entries and must hold "No change since July 2022 affects an answer in this chapter." That is untrue: a change exists, it is only not examinable yet.
- **Exact change.** Add to `exempt_sentences` and D6: "No examinable change since July 2022 affects an answer in this chapter; a newer change is under the B-list in 2-deep.md." D6: "With no examinable entry, the section holds exactly one of the two sentences."

### 12. Minor: the fast file takes 23 minutes; SPEC, READER and README say 20 or 15

- **Place.** `exemplar/iam-1-fast.md` front matter `minutes.fast: 23`; `SPEC.json` `templates.deep.minutes.fast` (20); `READER.md` ("15 to 20 minutes"); README ("the 15-minute file").
- **What is wrong.** With 1,788 words and 12 prompts, the time-box formula gives more than 20 minutes, so the 1,800-word budget of RULINGS and the 20-minute target cannot both hold. README calls it the 15-minute file.
- **Exact change.** README: "the 20-minute file". `SPEC.json` `templates.deep.minutes.fast`: 23, the exemplar's value (a planning target; the time-box guidance gives about 27 for 1,800 words and 12 prompts), with that note in `resolution.minutes`. The reader's 15-to-20-minute need is met by the Pass route split, not by this number.

### 13. Minor: some STYLE rules have no example, and the exemplar has no card, Lab or difficulty-1 question

- **Place.** `STYLE.md` 1 (one main idea, repeat the noun, noun stack, double negatives), 2 (plain words), 3 (the one analogy and where it breaks), 7 (difficulty 1 with short options, `option_words_difficulty_1`), 8 (Lab), 9 (no `cards.json` in the exemplar); `CONVENTIONS.md` D8 code sample.
- **What is wrong.** The task asks for an example per rule. The D8 sample still shows only "Body" and the Stop and answer, without the 1.0 `Say it` and `Exam signal`.
- **Exact change.** STYLE 1: append "Wrong: "it" after two nouns; "the VPC subnet route table entry target"." STYLE 3: "Analogy: "A role is like a service account in Kubernetes. It breaks here: a role has no key."" (inside the 3,000 budget, remove the duplicated sentence "Grounded examples: `exemplar/speak.json`." from 6, which README already gives). Exemplar: add `cards.json` with one `decide`, `differ`, `number` (A-list `one hour`) and `cannot` card, and one difficulty-1 question. CONVENTIONS D8 sample: insert `> **Exam signal:** "..." points to ...` and `> **Say it:** The short answer is ... The thing to watch is ...` before the Stop and answer.

### 14. Minor: STYLE says "per file", SPEC says "per chapter" for the first-use term rule

- **Place.** `STYLE.md` 4 ("at first use in a file"); `CONVENTIONS.md` G ("give the respelling at first use"); `SPEC.json` `lint.term_rules` ("first occurrence ... in the chapter's hand files").
- **What is wrong.** The exemplar follows STYLE (deep file re-introduces `IAM role`, VPC re-introduces `network ACL`), the lint follows SPEC.
- **Exact change.** Covered by the `term_rules` text of finding 8 ("in each hand file").

### 15. Minor: the tool documents were not moved to 1.0

- **Place.** `TOOLS.md` line 1 and L402 row; `TOOLS-rules.md` line 1; `TOOLS.md` W902 row.
- **What is wrong.** Both still say version 0.9. L402 describes the old exemption list. W902 says the `startup.cast` check is not implemented, while STYLE 5 states the cast as a rule.
- **Exact change.** Title lines "(version 1.0)"; L402 as in finding 2; W902: keep the note and add "STYLE 5 cast: review (claims reviewer) until implemented".

### 16. Minor: one fast-file cell states an exception without a fact link

- **Place.** `exemplar/iam-1-fast.md` line 100.
- **What is wrong.** "Either is enough, except for KMS keys" is a can-or-cannot claim (CONVENTIONS F) with no link; L304 misses it because it holds no absolute word. STYLE 11.2 asks for the most specific fact, which exists.
- **Exact change.** Cell: `Either, except for KMS keys: [IAM policies cannot allow access to a KMS key](../facts/iam.md#iam-kms-iam-policy-needs-key-policy-permission) <!-- xref: 06 KMS key policies -->` (14 words).

### 17. Minor: the term introductions in the exemplar skip the "not the same as" step

- **Place.** `STYLE.md` 2 (five steps); `exemplar/iam-2-deep.md` lines 27, 32, 83, 84; `exemplar/vpc-2-deep-slice.md` line 19.
- **What is wrong.** `implicit deny`, `explicit deny`, `trust policy` and `permissions policy` get no "not the same as" sentence; `security group` and `network ACL` name the term before the plain idea.
- **Exact change.** After line 32: "An explicit deny is not the same as an implicit deny: a Deny statement causes it, so only removing that statement fixes it." Line 84 bullet end: "It is not the same as the trust policy." VPC line 19: lead with the idea ("A firewall on each resource is a **security group** ..."). Re-check W201 (400 words) after each edit.

### 18. Minor: the sandbox and the registry still carry 0.9

- **Place.** `_build/tmp/exemplar-final/_build/style/{STYLE,CONVENTIONS,CONVENTIONS-2}.md`; `data/book.json` `style_version`.
- **What is wrong.** The sandbox copies are 0.9 (the lint does not read them, so the tool results stand, but an agent who reads the sandbox sees old rules). `style_version` is "0.9" while SPEC is "1.0"; the SPEC version is part of every stage `inputs_hash` (`TOOLS-rules.md` R7 decision 5), so chapters 00 to 03 go stale when `registry build` runs.
- **Exact change.** Copy the 1.0 files into the sandbox; the orchestrator runs `registry build` and `status` for 00 to 03 before W1 resumes (exemplar-spec-changes 6).

## Rulings check

No 1.0 change contradicts a hard rule or a ruling directly. Two exemplar parts conflict with RULINGS: the long displays (finding 6, ruling of 2026-10-11) and the ungrounded verify behaviour (finding 7, hard rules 1 and 9). The `Say it` exemption, the B-list placement of `not examinable yet` entries (the note still exists, rule 7), the strict twins and the banned-word additions are consistent with RULINGS.

## Notes

- Open question for the registrar, not a finding: the RCP fact `iam-rcp-never-grants-limits-resources` has no `changed` block; if RCPs are a post-2022 feature, the IAM fast file needs a `Changed recently` entry with `**Old:** not available.` (rule 7). Ground it before writing.
- My fixture lint run created `tools/tests/fixtures/book/_build/reports/lint/99.json`; I removed that folder again, so the fixture is unchanged. A later analysis script in the scratchpad was refused by the permission system and was not retried; its question (changed facts linked by the exemplar) was answered with `facts card` instead.
