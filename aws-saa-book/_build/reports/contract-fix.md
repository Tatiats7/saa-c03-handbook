# Contract fix 1: what was done with each review finding

Date: 2026-10-04. Input: `contract-critique-writer.md` (58 findings) and `contract-critique-implementer.md` (64 findings).

Result: 120 fixed, 1 rejected, 1 deferred. Some lines also name a part that was rejected or deferred.

After the edits: `python3 aws-saa-book/tools/tests/run.py contract` passes (66 tests), and the whole suite passes (224 tests). The contract version stays 0.9 (the tests fix it); the documents carry the note "contract fix 1".

## Files

New:

- `_build/style/CONVENTIONS-2.md`: part 2 of CONVENTIONS (pattern, front and synthesis pages; rules for JSON items; decisions 26 to 34). Needed because `CONVENTIONS.md` and `STYLE.md` have word budgets.
- `_build/style/TOOLS-rules.md`: part 3 of TOOLS (gate table, shared functions, matching rules, count keys, new codes, status commands, decisions).
- `_build/schemas/plan.schema.json`, `_build/schemas/drills.schema.json`.
- `tools/helpers/contract_fix_terms.py` (the migration of `data/terms.json`; safe to run again), `tools/tests/doc_sizes.py` (word counts of the contract documents and the fixture hashes).

Changed: `_build/style/CONVENTIONS.md`, `STYLE.md`, `SPEC.json`, `TOOLS.md`, `TOOLS-items.md`; `_build/schemas/` `question`, `task`, `card`, `speak`, `terms`, `fact`, `fact-request`, `gate`, `book`; `data/terms.json`; the fixture (`SPEC.json`, `99-sample/1-fast.md`, `2-deep.md`, `questions.json`, `cards.json`, `speak.json`, `tasks.json`, `terms.json`, `facts/widget.jsonl`, `gates/99.facts-final.json`, `README.md`); `tools/tests/test_contract.py`, `tools/tests/contract_probe.py`.

Not touched: `common.py`, `saa.py`, `RULINGS.md`, `STARTUP.md`, `TOOLS-diagram.md`, `diagram.schema.json`.

## Where two findings conflicted

| Conflict | Decision | Why |
|---|---|---|
| Writer 5 (a heading with an absolute word is grounded by a fact link in the body) against implementer 13 (forbid such headings) | Writer 5 | LEARNING requires assertion headings ("An explicit deny always wins"); a body link keeps hard rule 1. New code L308. |
| Writer 42 (marker `no-fact: plan`) against implementer 14 (exempt time units in advice roles) | Both | The unit exemption covers study times without noise; a word list (`exam_fact_words`) keeps exam rules strict; the marker covers percentages and counts of her plan. Role `plan` is now heuristic, not exempt. |
| Writer 53 (`none` only at difficulty 1) against implementer 21 (allow `none` at any difficulty, no `violates-qualifier` then) | Writer 53, with the wording of implementer 21 for Q108 | STYLE defines difficulty 2 as "discriminate under a qualifier". |
| Writer 28 (generated cards, or hand cards in chapter 01) against implementer 7 (`cards build` into chapters 01 and 49) | Generated, with the homes of implementer 7; term cards in `data/cards-terms.json` | One source per card. |
| Writer 3 (brief holds trap ids, or `prose` becomes a prerequisite) against implementer 20 (stage order) | Brief holds trap ids, headings and diagram texts; stages stay parallel; `verify-questions` is a prerequisite of `review` | Keeps the parallel build of PIPELINE section 10. |
| Writer 6 (add `facts` to the diagram spec) | No schema change; Markdown caption and steps equal the spec text and carry the links (L705) | The diagram module and its schema are built and tested; the grounding is the same. |
| Writer 16 (make `worked.steps` strict) | Rejected for that part | RULINGS exempts role `worked`; steps repeat stem conditions with "must". |
| Writer 39 (card minimum 100 words) | Rejected | RULINGS fixes 150 to 220 words. |

## For the orchestrator

1. RULINGS says "working name Harken"; `STARTUP.md` renamed the startup to Callvale. The contract now uses Callvale everywhere. Please update RULINGS.
2. RULINGS lists `data/glossary.json`; the contract does not use it.
3. Please confirm in RULINGS: the block-level exemptions of CONVENTIONS decision 23 (narrowed, decision 33), and the ban of `create-user` in tasks.
4. The card counts per template (deep 14 + 18 and so on) now count the four hand-written card types only. Lower them if they were meant to include term cards.
5. The term bank still has 83 terms. The brief stage must list the terms of a chapter (`brief.json` `terms`, gate B11), and the bank must grow before the IAM writers start.
6. `data/plan.json` does not exist yet; the writer of chapter 00 writes it.
7. `STARTUP.md` section 7 names a story diagram pair `<slug>-before` and `<slug>-after`; CONVENTIONS names one hero diagram `<slug>-hero`. No review raised it; it needs one sentence in `STARTUP.md` or the brief (which of the two is the hero).
8. Asked of the diagram module owner: a node label with a number with a unit must repeat a value of `claim` or `say`.
9. The AWS CLI tag syntaxes (`tasks.tag_patterns`), `tasks.untaggable_operations`, the documentation account ids and the pinned `awscli` and `moto` versions were written from memory. `tasks check-cli --reference` and the `lab` implementer confirm them.

## Writer findings

1. fixed: `rows_max` per table kind (`matrix` 24, `numbers` 40, `plan` 19, `log` 400); a row count is the sum over the tables of the kind; new test.
2. fixed: `tasks.tag_patterns`, `tag_task_patterns`, `verify_tag_patterns`, `untaggable_operations`; T106 and T108 rewritten; STYLE section 8 rule 3; fixture step and must-fail test.
3. fixed: `brief.json` holds `traps`, heading texts and diagram texts; item rules accept brief ids until the prose exists; L905 from the `edit` stage (`TOOLS-rules.md` R4).
4. fixed: an `Exam trap` callout can carry a trap id; one trap id can serve several questions.
5. fixed: `headings.grounding` (body link), L308.
6. fixed: caption and step sentences are strict and equal the spec text; L705. No `facts` key in the spec (see the conflict table).
7. fixed: alt, caption and steps equal the spec (L702, L703); the hero is `arch` or `sequence`; alt minimum 20; the brief is the source of the text.
8. fixed: the missing SVG of L701 and L704 is a draft warning.
9. fixed: `<!-- xref: ... -->` marker, W601, error only in the whole-book strict pass.
10. fixed: the story budget counts `Startup example` callouts only.
11. fixed: section limits raised (deep: recap 160, check 140, signals 500, numbers 300, changed 180; medium scaled); reveals count, stated in `resolution.word_count`.
12. fixed: `devices.subsection_words_count`; the interval minimum is removed.
13. fixed: "But not if" is a heuristic column; `no-fact` marker with W308.
14. fixed: `Exam signal` is strict after its quoted phrase. RULINGS confirmation asked.
15. fixed: `twin_of` on the later question, same layer, 3 questions between, quoted phrase exempt (Q114).
16. fixed: wrong-path marker in SPEC, STYLE and the fixture. The part "make `worked.steps` strict" is rejected (RULINGS: role `worked`); the steps are declared example text.
17. fixed: P109 and C109.
18. fixed: `explain` on a break-it step (schema, `break_it_step_needs`, T110, `sync`, fixture).
19. fixed: placeholders `<UPPER_CASE>`; `capture` for values of earlier steps; documentation account ids allowed in `json` blocks.
20. fixed: `allowed_command_prefixes` (`aws`, `curl`, `dig`); only the writing forms of `aws configure` are banned.
21. fixed: `template` on a Lab (schema, T120, `sync`).
22. fixed: `exam_english` on a question, in the brief slots, `q words --need`, Q303 match rule.
23. fixed: decision 27 (the web app builds these devices; no writer action). A generated region for return questions is rejected, with the reason.
24. fixed: the fact sheet exists as `STARTUP.md` and `data/harken.json`; STYLE and SPEC name it; the name is Callvale; W903.
25. fixed: which words must be terms; `needs-term` marker; the words part of L503 is a draft warning; brief `terms` with gate B11. Growing the bank itself is left to the brief stage (orchestrator note 5).
26. fixed: `banned` is literal; new `banned_case` and `avoid`; 45 conditional entries moved by the helper; L901 match rule.
27. fixed: "landing zone" and "cold start" removed from the customer words; terms of the bank are allowed; `cold start` is now kind `concept`.
28. fixed: writers write four card types; `cards build` generates the other five; fixture card changed.
29. fixed: the `service` of the fact equals the file stem; no id starts with a longer service key (L301, M1).
30. fixed: `facts request --fact ID --display TEXT`, `needs-display` marker, B12.
31. fixed: quote blocks are exempt from the sentence, word and term rules; the D13 example has no final period and has the fact link; "any saved AWS page".
32. fixed: the fixture volatile window is 6 months, with a warning in the fixture README and in `CONVENTIONS-2.md` J2 not to copy the choice.
33. fixed: the two short options of the STYLE sample have 16 words now.
34. fixed: `lint.minutes_formula`; template minutes are targets; W105; criterion for `route=pass`.
35. fixed: `CONVENTIONS-2.md` J1 (who supplies what); `questions.topics`; Q116; fixture bullets.
36. fixed: roles `question` and `glance`; table kinds `glance` and `services`; examples of both tables (not a whole filled file).
37. fixed: a pattern card heading is a name of 1 to 6 words; `Problem.` and `Requirement.` are example blocks.
38. fixed: optional `2-services.md` in the deep, medium and pattern templates; registry key `cards`.
39. rejected (RULINGS fixes 150 to 220 words; the range is only a warning, and `What it is.` can have two sentences). The `**Formerly.**` part is fixed (L802).
40. fixed: no hand section "Worked examples"; `exam-english` regions and table kind.
41. fixed: table kind `log`, `lint.cause_codes`, `reader_editable`, Task 0 in chapter 02.
42. fixed: role `plan` is heuristic; exam rules need links.
43. fixed: architecture page and atlas page defined with examples (`CONVENTIONS-2.md` S3, S4).
44. fixed: `trap-ref` in chapter 46; fixed H3 by section key.
45. fixed: `section` can name another chapter (`<NN-slug>/<file>#<section id>`).
46. fixed: `callouts.say_it_words_max`, `devices.*`.
47. fixed: Look first has one or two sentences; a Predict intro line is allowed; the Check reveal answers Predict; fixture words table and term bank corrected.
48. fixed: `devices.words_table`.
49. fixed: `devices.term_definition`.
50. fixed: `lint.abbreviation_rule`.
51. fixed: `<br>` line ends, date rule, form for a new feature.
52. fixed: `as` is no warn word; `may` and `over` rules.
53. fixed: `CONVENTIONS-2.md` J2.
54. fixed: `CONVENTIONS-2.md` J3, J4; `speak set-pack`; `say` card form; tags.
55. fixed: title pattern, `try_pass_route`, `kills` in quotes, one `Try it` per task.
56. fixed: Changed recently entries are not counted; `Key fact` is optional; `counts.diagrams`.
57. fixed: the listed sentences are in CONVENTIONS F and `CONVENTIONS-2.md`; `former_name_regexes` for Amazon SageMaker.
58. fixed: `h3_regex`, merge rule, optional B-list, C204, the writer rule for example sections. The anchor rewrite tool is deferred (L601 reports broken anchors; a tool needs its own design).

## Implementer findings

1. fixed (writer 2).
2. fixed: `capture` on a step, T115, printed form, emulation note.
3. fixed: the template field is `key`; "section id" is the heading anchor everywhere.
4. fixed: `set-status` for the four kinds; `--replace` defined for every state (`TOOLS-rules.md` R5).
5. fixed: gate table and one signature (R1); `gate_mech`, `gate_final`, `gate_cards`, `gate_speak` defined; `gate_tasks` without `--ship`; "the facts of a chapter" defined.
6. fixed: `resolution.template`; `lint.template`, `word_count`, `anchor`, `section_id`.
7. fixed (writer 28): `cards build`, homes of the generated cards, C202, schema text.
8. fixed: `heading_rule` of a service card.
9. fixed (writer 45).
10. fixed: `services` has at least one item; `services[0]` is the focus service.
11. fixed: `questions.drill_pool`.
12. fixed: six term ids renamed; contract test and must-fail test.
13. fixed: `number_with_unit.match`, `absolute_word_match`, `grounding.skips`. The proposed ban of absolute words in headings is rejected (conflict table).
14. fixed: `heuristic_exempt_units` with `exam_fact_words`.
15. fixed: `Problem.` and `Requirement.` are example blocks.
16. fixed: `twin_quoted_phrase_exempt`.
17. fixed: `prompts.syntax`; `bold_fields.card`, `pattern`, `page`, `atlas`; the real-world first paragraph regex.
18. fixed (writer 44).
19. fixed: the count key table (`TOOLS-rules.md` R3).
20. fixed: `review` needs `verify-questions`; `mark_stale(item_stages=...)`.
21. fixed: Q108 (see the conflict table).
22. fixed: `digits_allowed_inside_names_regex` and `digits_allowed_rule`.
23. fixed: M5 name and date exemptions.
24. fixed: the tool writes front matter `status`; B08 changed; manifest mapping.
25. fixed: `plan.schema.json`, `plan` regions, `data/plan.json` in the data table. The data file is content for the chapter 00 writer.
26. fixed (writer 35).
27. fixed: L108.
28. fixed: solver mapping and schema keys.
29. fixed: the create regex applies to the operation; `untaggable_operations`; `cleanup_pairs`; port patterns. The `create-user` ban stays (orchestrator note 3).
30. fixed: the fixture `why` has 13 words; Q103 covers every option.
31. fixed: fixture alt text; alt text is checked by L801 and L901 only.
32. fixed: customer word rule; the place is written with the full folder name.
33. fixed: `lint.word_match`.
34. fixed: `amend` can change `volatility`, `hard`, `source_tier`, `bullets`.
35. fixed: M13; fixture facts have `question`; gate hash updated.
36. fixed: `derive` has no `partial`.
37. fixed: status `duplicate` removed.
38. fixed: `was_evidence` is an integer.
39. fixed: M11 wording.
40. fixed: M12 is not blocking; tokens defined.
41. fixed: status table; `repairs` rule.
42. fixed: `facts vote` applies a negative `rederive` at once.
43. fixed: exit 3 for the label `unknown`.
44. fixed: sentence rule of `adopt`.
45. fixed: `verify` writes only on a status change; `mech` and `supersedes` described.
46. fixed (writer 31).
47. fixed: `callouts.label_rule`; `<br>`.
48. fixed: `lint.contraction_regex`.
49. fixed (writer 48).
50. fixed: `lint.term_rules`.
51. fixed (writer 34).
52. fixed: one cut-off source (`book.exam_eligibility_cutoff`), wording "after", L107 status check.
53. fixed: `callouts.say_it_words_max`.
54. fixed: documented as "diagram module only" (`TOOLS-rules.md` R7, decision 15).
55. fixed: `diagram.pipeline.` prefixes.
56. fixed: region kinds are `task`, `plan`, `exam-english`, `quiz`, `speak`; `do` and `tasks` defined.
57. fixed: numbering, one print per question, the Review link; `lint.sections` values.
58. fixed: task regions in `3-do.md`.
59. fixed: `freshen` ends with `sync --only sources,facts`.
60. fixed: `follow_ups[].facts` in the dependents scan.
61. fixed: `pass_route` in CONVENTIONS J; `section` is required in the four item schemas.
62. fixed: `volatile_rule` (Q112), `sources_rule`, P202, `strict_field_content`.
63. fixed: rule 13 exceptions; `needs-fact` marker in the fixture; `book.artifact_url`; `aliases`; `drills.schema.json`; warning string form; C105 exempts `say`; mock `write` 78; medium "How it works" minimum 1,300; pack item keys; short complete-sentence quotes (M4); imports inside functions. Deferred parts: schemas for `brief.json`, findings files, packs and packets (the inline shapes in `TOOLS.md` stay the contract); the RULINGS line about `data/glossary.json` (orchestrator); the `awscli` and `moto` versions (the `lab` implementer confirms them, `TOOLS-rules.md` R6).
64. deferred (no change was required; the helpers live in `lint`; moving them to `common.py` is for the owner of `common.py`, decision 12).
