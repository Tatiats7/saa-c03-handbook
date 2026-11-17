# Contract critique: implementer lens

Date: 2026-10-04. Reviewer role: the agent who must write `lint`, `sync`, `facts` and the question bank from the contract.

Read: `RULINGS.md`, `CONVENTIONS.md`, `STYLE.md` (scanned), `SPEC.json`, `TOOLS.md`, `TOOLS-items.md`, all 19 schemas, the fixture book, `common.py`, `schemas.py`, `PRODUCT.md` sections 1 to 4, and the task, card and pipeline parts of `LEARNING.md` and `PIPELINE.md`.

Checked by script (`tools/tests/contract_probe.py`, read-only, run with `python3 aws-saa-book/tools/tests/contract_probe.py`):

- All 60 JSON and JSONL files under `_build/schemas`, `_build/style`, `_build/registry`, `data`, `diagrams/src` and `tools/tests/fixtures` parse.
- The seed, the fixture `book.json`, the four fixture item files, both `terms.json` files, `exam-english.json`, the 7 fixture facts, the votes, the requests, the ledger file, the gate record, `exam-guide.json` and `services.json` are valid against their schemas.
- Results that are findings are cited below as "probe".

Not checked: the registry parser against the fixture exam guide pages, `TOOLS-corpus.md`, `TOOLS-feeds.md`, `TOOLS-diagram.md`. Statements about real AWS CLI syntax come from memory and must be confirmed against the CLI reference in the corpus before the rule is changed.

Severity: **blocker** = two agents would build incompatible things, or a required thing is impossible. **major** = likely rework. **minor** = small.

Counts: 7 blockers, 24 majors, 33 minors.

---

## Blockers

**1. blocker. Tag rules T106 and T108 cannot pass with real AWS commands.**
Where: `TOOLS-items.md` 8.1 (T106, T108), `SPEC.json` `tasks.tag`, `tasks.tag_task`.
Wrong: T106 requires that a create command "holds `book=saa` and `task=<task id>`" and T108 that the verify command "holds `book=saa`". Most AWS CLI commands write tags as `Key=book,Value=saa` (IAM, RDS), as `--tag-specifications 'ResourceType=...,Tags=[{Key=book,Value=saa}]'` (EC2) or as `TagSet=[{Key=book,Value=saa}]` (S3). A verify by tag is `--tag-filters Key=book,Values=saa` or `Name=tag:book,Values=saa`. None holds the literal string `book=saa` (probe, section 7). The fixture passes only because `aws widget` is invented. IAM is the pilot chapter and uses the `Key=,Value=` form.
Change: replace the literal test with a SPEC regex list. `tasks.tag_patterns`: `book=saa`, `Key=book,Value=saa`, `"Key": ?"book", ?"Value": ?"saa"`. `tasks.tag_task_patterns`: the same three forms with `task` and the task id. `tasks.verify_tag_patterns`: `book=saa`, `Key=book,Values=saa`, `tag:book,Values=saa`. T106 and T108 pass when one pattern matches. Add one fixture step in the `Key=,Value=` form.

**2. blocker. A task has no way to pass a generated id from one step to the next.**
Where: `task.schema.json` `step`, `TOOLS-items.md` T104, `PIPELINE.md` section 14.
Wrong: T104 allows one `aws` command per step and bans `$(`, backticks, pipes and `;`. The schema has no variable field. PIPELINE section 14 says each step has "argv, captured variables and expected output shape". Without capture, a step cannot use a VPC id, subnet id, instance id, allocation id or queue URL that an earlier step returned. VPC (wave 2) and EC2 tasks are then impossible, and `tasks emulate` cannot run them.
Change: add to `step` and `command_step`: `"capture": {"name": "VPC_ID", "query": "Vpc.VpcId"}` (optional, nullable). Define: the printed command for a capture step is `VPC_ID=$(<command> --query <query> --output text)`; later commands use `$VPC_ID`. T104 checks the stored `command` (still one plain `aws` command); `$NAME` is allowed only when an earlier step captures `NAME` (new code T115). `sync` prints the wrapped form. `emulate` substitutes the captured value.

**3. blocker. "Section id" has two definitions.**
Where: `SPEC.json` `templates.*.files[].sections[].id` and `headings.section_id`; `CONVENTIONS.md` G; `TOOLS.md` section 2 `lint.sections`, B01 `brief.json`, 5.6 `--where`; all item schemas `section`.
Wrong: `headings.section_id` says the id is the heading anchor without the time box (`in-one-breath`, `signals-and-traps`). The template sections carry another id (`breath`, `signals`, `look`, `choose`). About 70 SPEC ids differ from the anchor of their heading (probe, section 8). The fixture items use the anchor form (`1-fast.md#look-first`, `1-fast.md#choose-it-or-not`). `lint.sections(ch)` returns `{file: {section id: ...}}` without saying which. The web route `#ch.<slug>.<section>` and the progress keys use the same value.
Change: rename the SPEC field to `key` and add to `resolution`: "`key` names a template section inside SPEC only. The section id everywhere else (items, brief, requests, `lint.sections`, web) is `headings.section_id`." State in `TOOLS.md` section 2 that `lint.sections` keys are anchor-form ids and that H3 subsections are included.

**4. blocker. No command moves a task, card or speak item to `ready`, and a question cannot be edited or retired outside round 1.**
Where: `TOOLS-items.md` 7.1, 7.4, 7.6, 8; 6.2 ("Only items with `status: ready` are printed").
Wrong:
- Tasks: `tasks add` "works like `q add`", which sets `candidate`. Nothing sets a task to `ready`. `3-do.md` and every Look region then print "Nothing here yet", and T201 with `--ship` cannot pass.
- Cards and speak: "A reviewer sets `status: ready` with `--replace`", but `add` always sets `candidate`. How `--replace` carries the new status is not said.
- Questions: `q add --replace` requires `verification.round` 1. A writer cannot fix a Q203 or Q202 failure before verification, a reviewer cannot fix a finding on a verified question in the `fix` stage, and no command sets `retired` or removes a surplus item.
Change: add one subcommand per kind: `q|cards|speak|tasks set-status --chapter CH --status ready|retired|rejected ID ... [--by L] [--reason TEXT]`. `ready` is allowed only when the item passes its item rules (for a question also Q206). Define `--replace` for all four kinds: before any verification (`round` 0, no solvers) it replaces in place and keeps `rev`; for a question with `verification.status` `pass` or `edited-pass` it raises `rev` and resets `verification` to `{"status": "candidate", "round": 0, "solvers": []}` and `status` to `candidate`; at `round` 1 it is the one edit (keeps `round` 1, clears `solvers`).

**5. blocker. Gate functions: signatures differ, four are undefined, and the facts gates have no scope.**
Where: `TOOLS.md` section 0 rule 8, section 2, section 3.1; `gate.schema.json` description; `TOOLS-items.md` 7.2, 8.1.
Wrong:
- Rule 8 and the schema say `gate_<name>(ch_id, quick=False)`. Section 2 lists `gate_lint(ch, draft=False)`, `gate_sync(ch)`, `gate_questions(ch)`. The ledger agent and the module agents will not agree on the call.
- The gate names `facts-mech`, `facts-final`, `questions-verified` do not map to `gate_mech`, `gate_final`, `gate_questions_verified` by any stated rule.
- `gate_mech`, `gate_final`, `gate_cards` and `gate_speak` have no definition. `gate_tasks` is defined as `tasks lint CH --ship`, which blocks on T113 and T201 at stage 8, before any task can be `ready` or CLI-checked.
- "The facts of a chapter" is undefined: facts with `home_chapter` = chapter, or every fact the chapter links (a VPC chapter links `ec2-` facts).
Change: add a table to section 2: gate name, module, function, exact call. Use one signature `gate_x(ch_id, quick=False, **options)`; the ledger calls `lint.gate_lint(ch, draft=True)` for `prose`. Define: `gate_mech(ch)` = M1 to M12 on every non-rejected fact with `home_chapter` = ch, and at least one fact exists for a chapter with services; `gate_final(ch)` = every non-rejected, non-superseded fact with `home_chapter` = ch, plus every fact linked from the chapter's hand files and items, is `verified`, and no conflict is open. `gate_cards`, `gate_speak`, `gate_tasks` = item rules plus chapter rules without `--ship`; the `counts` gate alone uses `--ship`.

**6. blocker. Template resolution is not specified well enough to be implemented five times.**
Where: `SPEC.json` `resolution.template`, `chapter_overrides`; `TOOLS.md` 3.1 (not-applicable rules), 4.3 (`wave-args`), 6.1; `TOOLS-items.md` Q201, C201, P201, T201.
Wrong:
- `chapter_overrides["02"]` is `{"template": "medium"}`. The `resolution` text does not describe a `template` key. Chapter 02 has tier `front`.
- "Merged on top" does not say deep or shallow. Override `49` has `counts: {"speak": ...}` only and override `01` has `counts: {"questions": ...}` only. With a shallow merge `counts.questions` disappears for chapter 49 and the not-applicable rule of stage 7 raises a key error. With a deep merge, lists (`files`) must still be replaced whole.
- `ledger`, `registry`, `lint`, `qbank` and `lab` each need the resolved template, and no shared function exists (`common.py` has none; section 2 lists none).
Change: add to `resolution.template`: "If the override has `template`, that template replaces the tier template. Objects merge key by key, recursively; arrays and scalars are replaced." Add to `TOOLS.md` section 2: `lint.template(ch) -> dict` (the resolved template with `key`, `files`, `counts`, `minutes`), `lint.word_count(text)`, `lint.anchor(heading)`, `lint.section_id(heading)`. Every other module calls these (import inside the function, because `lint` also reads item files).

**7. blocker. The exam-English, Say and cross-cutting cards have no home, and C202 cannot pass.**
Where: `TOOLS-items.md` C202, C103; `CONVENTIONS.md` A (chapter 01 and 49 have no `cards.json`); `SPEC.json` front and synthesis `counts.cards` 0; `terms.schema.json` description; `LEARNING.md` section 9.
Wrong: C202 requires 90 `word` cards in the `exam-english` deck. Chapter 01 has no `cards.json`, its card counts are 0 and its `cards` stage is not applicable. LEARNING also counts 30 Say cards and 20 cross-cutting cards that no template holds. `terms.schema.json` says the term, meaning and partner cards "are generated from this file", while the fixture stores a hand-written `partner` card in `cards.json`. A qbank agent and an export agent will decide differently.
Change: decide and write one rule. Proposed: (a) `word` cards are generated by `cards build --exam-english` into `data/01-how-the-exam-asks/cards.json` (one per word of `exam-english.json`; front = `stem`, back = `meaning` and `signals`), and override `01` gets `counts.cards: {"core": 0, "extended": 0, "exam_english": 90}`; (b) `say` cards are generated the same way into `data/49-speaking-pack/cards.json` from speak items with `pack: true`; (c) all other types are hand-written in the chapter file; (d) correct the `terms.schema.json` description.

---

## Majors

**8. major. A light service card heading cannot equal the official service name.**
Where: `CONVENTIONS.md` C and D15, `SPEC.json` `headings.h2_h3_regex`, L103, L104, L802; `services.schema.json` `official_name`.
Wrong: `official_name` is verbatim and keeps the parentheses (fixture: "Amazon Managed Crate Service (Amazon MCS)"). The heading regex allows no parentheses (probe, section 8). An official name can also hold a former name, which L802 rejects.
Change: L104 for `sections_mode: repeat` with `service=`: the heading is the official name without a final parenthesised part, with characters outside the heading regex removed. Lint compares `common.slugify` of both. Former names inside `official_name` are not checked by L802 in headings.

**9. major. A mock or drill question cannot name its review section.**
Where: `question.schema.json` `section`, Q111, `TOOLS-items.md` 6.2 (`**Review.**`), `PRODUCT.md` routing.
Wrong: `section` is `<file>#<section id>` with no chapter. A mock question reviews a section of another chapter. Q111 "`section` resolves" has no chapter to resolve in.
Change: allow `<NN-slug>/<file>#<section id>` and require that form when `pool` is `mock` or `drill`. Q111 resolves with `lint.sections` of that chapter. `sync` prints `../<NN-slug>/<file>#<markdown anchor>`.

**10. major. `services[0]` is the focus service, but `services` can be empty.**
Where: `question.schema.json` `services`; `TOOLS-items.md` 7.7 step 2, K06.
Change: add `"minItems": 1` to `services`, and say in Q111 that `services[0]` is the focus service.

**11. major. Questions with pool `drill` have no rules.**
Where: `TOOLS-items.md` Q101, Q201, 6.2, 7.8.
Wrong: nothing says in which file a `drill` question lives, whether it counts toward `shipped`, `core` and `extended`, or whether `5-quiz.md` prints it.
Change: "A `drill` question lives in the `questions.json` of its topic chapter. It is not counted by Q201 and is not printed in `5-quiz.md`. It needs the same verification."

**12. major. Six real term ids differ from the anchor of their heading, so `sync` exits 1 on the real book.**
Where: `data/terms.json`; `TOOLS-items.md` 6.2 `glossary.md`.
Wrong: `temporary-credentials`, `scp`, `vpc`, `vpc-peering`, `rpo`, `rto` have terms whose GitHub anchors are `temporary-security-credentials`, `service-control-policy`, `virtual-private-cloud`, `vpc-peering-connection`, `recovery-point-objective`, `recovery-time-objective` (probe, section 3).
Change: rename the six ids to the anchors (nothing links them yet), and add a contract test that `anchor(term) == id` for every term.

**13. major. L304 cannot be implemented the same way twice: matching is not defined.**
Where: `TOOLS.md` 6.1 L304, L305; `SPEC.json` `lint.number_with_unit`, `lint.absolute_words`.
Wrong, each point changes results:
- "Followed by a unit": with or without a space, and with a hyphen (`5 GB`, `5GB`, `10-second`)?
- Case: is `Only` or `ONLY` an absolute word? Is a count noun matched case-sensitively?
- Compounds: `read-only`, `append-only`, `must-have` match `\bonly\b` and `\bmust\b`. "Read-only" is frequent.
- Headings: an assertion heading can hold an absolute word but cannot hold a link (the heading regex forbids brackets). Are headings checked?
- Image alt text, figure captions and bold labels: checked or not?
Change: add to `SPEC.json` `lint`: `"number_unit_regex": "<number_regex>[ -]?(<units>|<count nouns>)\\b"` (units case-sensitive, count nouns case-insensitive), `"absolute_word_match": "case-insensitive; not preceded or followed by a letter, digit or hyphen"`, `"grounding_skips": ["headings", "image alt text", "bold labels"]`. Add to CONVENTIONS D8: an assertion heading holds no number with a unit and no absolute word.

**14. major. Advice sections cannot state study times.**
Where: `SPEC.json` `roles.orient`, `roles.method` (grounding `heuristic`), L305; overrides 00, 01, 49, 52.
Wrong: heuristic text forbids a number with a unit without a fact link. "Three routes" (00), "Pacing plan" (52), "The practice ladder" (49) and "The four moves" must say things like "20 minutes", "10 seconds", "60 seconds". These are the book's own values; no AWS page grounds them.
Change: add `"heuristic_exempt_units": ["second", "seconds", "minute", "minutes", "hour", "hours", "day", "days", "week", "weeks"]` under `grounding`, used only for roles `orient` and `method`. Exam facts in those sections (number of questions, exam time, passing score) keep the link rule because `%` and count nouns stay strict.

**15. major. Scenario fields in strict roles are not exempt.**
Where: `CONVENTIONS.md` D16 (`**Problem.**` "in exam English"), override 44 (`Requirement.` in role `page`), `TOOLS.md` role exemptions.
Wrong: a pattern card's `Problem.` and a reference architecture's `Requirement.` are scenarios with story values ("an RPO of 15 minutes"). Their roles (`how`, `page`) are strict, and the exemption list does not name them.
Change: add `"bold field:Problem."` and `"bold field:Requirement."` to `grounding.example_blocks` and to the exemption list in 6.1.

**16. major. The quoted phrase of a twin is scenario data but is checked as strict text.**
Where: `SPEC.json` `questions.strict_text_fields` (`twin`), Q110.
Wrong: `If the stem said "retrieval within 12 hours" instead: ...` holds a number that is not in the stem. The fixture passes only because every twin also has a link in the same sentence.
Change: in `check_strict_text`, text inside straight double quotes directly after `twin_prefix` is exempt. Add the key `questions.twin_quoted_phrase_exempt: true`.

**17. major. Prompt, bold field and free bold label share one syntax.**
Where: `SPEC.json` `prompts.syntax`, `bold_fields`, `grounding.example_blocks` ("prompt paragraph (starts with a bold device label)"); `CONVENTIONS.md` D13; L107; exemption 2.
Wrong: "a paragraph that starts with a bold label ending in a period" also describes `**Decision.**`, `**Figure.**`, `**The problem it solves.**`, the service-card fields and `**Tallis Freight, 2025.**`. Is `**The problem it solves.**` exempt from L304 as a prompt paragraph? Is the company label an unknown prompt label (L107)?
Change: "A prompt is a paragraph whose bold label matches a key of `prompts.labels` (`<n>` = digits). A bold field is a paragraph whose label is in `bold_fields` or in a template `fields` or `subsection_fields` list. Only prompts are example blocks. Any other paragraph that starts with `**...**` and a period is plain text, except in role `realworld`, where the first paragraph must match `^\*\*[^*]+, 20[0-9]{2}\.\*\* `." Add `bold_fields.card` and `bold_fields.pattern` so all labels are in one place.

**18. major. L604 and `lint.traps()` conflict with chapter 46.**
Where: L604; `SPEC.json` override 46 (`traps_must_exist_in_chapters`); `TOOLS.md` section 2 `lint.traps`.
Wrong: "Top traps" in chapter 46 repeats 30 to 40 trap ids of other chapters. L604 rejects an id that does not start with the slug or is used twice. `traps()` maps a trap id to one chapter "from every hand file".
Change: in a section with `traps_must_exist_in_chapters`, a trap comment is a reference: it must exist in another chapter, is exempt from the slug and uniqueness tests, and is skipped by `lint.traps()`.

**19. major. Most `counts` keys have no counting rule.**
Where: L106; `SPEC.json` `sections[].counts`, `files[].counts`.
Wrong: L106 names 10 things. SPEC uses about 24 keys: `task_regions`, `say_it`, `hero_diagrams`, `hero_steps`, `startup_examples`, `rows`, `signal_rows`, `pairs_rows`, `matrix_rows`, `plan_rows`, `a_list_rows`, `b_list_rows`, `compare_tables`, `traps`, `entries`, `items`, `quotes`, `options`, `subsections`, `subsection_words`, `stop_and_answer_per_subsection`, `prompts`, `gist_traps`, and the file-level `spot_the_bug`, `go_deeper`.
Change: add a table to 6.1: key, what is counted, code. For example `items` = `FAQ <n>.` prompts; `entries` = `Changed recently` callouts (0 entries requires the exempt sentence); `quotes` = AWS quote blocks; `options` = list items after `**Options.**`; `hero_steps` = items of the ordered list after the hero caption; `subsection_words` is W201, not L106. Say that a key with `{}` counts nothing.

**20. major. Stage order: reviewers see an empty `5-quiz.md`, and reset items are never rebuilt.**
Where: `TOOLS.md` 3.1, section 2 `mark_stale`, 5.7 step 2; `TOOLS-items.md` 6.2, 7.4.
Wrong:
- `sync` prints only `ready` questions. A question becomes `ready` in `q adjudicate --select`, inside `verify-questions` (stage 15), whose only prerequisite is `questions`. `review` (stage 13) depends on `edit` only, so the exam lens can read a `5-quiz.md` with no question.
- `facts amend` sets dependent cards, speak items and tasks to `candidate`. `mark_stale` marks `edit` and later stages only. `stage begin` for `cards`, `speak` or `tasks` then answers SKIP (already passed), and nothing returns the items to `ready`.
Change: make `verify-questions` a prerequisite of `review` (renumber it to 12 and put it before `edit`, or add it to the prerequisites of `edit`). In `mark_stale`, the default stage list also holds each of `questions`, `cards`, `speak`, `tasks` for which the caller reset at least one item (add a parameter `item_stages=[...]`, passed by `facts amend` and `freshen`).

**21. major. Q108 requires a `violates-qualifier` option on a question without a qualifier.**
Where: `TOOLS-items.md` Q108; `SPEC.json` `violates_qualifier_min_from_difficulty`, `no_qualifier_share_max`.
Change: "difficulty 2 and 3 with `qualifier` other than `none` have at least one `violates-qualifier` option; a question with `qualifier: none` has none."

**22. major. P106 forbids "Route 53" and "gp3" in a spoken script.**
Where: `SPEC.json` `speak.digits_allowed_inside_names_regex`; P106.
Wrong: the regex `\b[A-Z][A-Za-z]*[0-9]+\b` accepts `S3`, `EC2`, `IPv4` and rejects `Route 53`, `gp3`, `io2`, `t3` (probe, section 5). Chapter 13 cannot name its service.
Change: use the lint rule: a digit is allowed when it is part of, or directly follows, a `term` or `short` of `data/terms.json` or an official service name; keep the regex as a second allowance and add `|\b[a-z]{1,3}[0-9]\b`.

**23. major. M5 has no exemption for digits in names and dates.**
Where: `TOOLS.md` 5.2 M5.
Wrong: "Every number in `claim` ... appears literally in a quote." A claim that says "Amazon S3", "Route 53", "EC2" or a date ("November 19, 2025", in the fixture claim) fails when the quote does not repeat that string. The lint has this exemption (6.1, "Not counted as a number"); M5 does not.
Change: M5 uses the same "not counted as a number" list as 6.1 for names. A date in the claim must equal `changed.date` or stand in a quote.

**24. major. Two status vocabularies, and no owner for the front matter status.**
Where: `SPEC.json` `statuses.chapter` (`planned`, `draft`, `reviewed`, `ready`); `ledger-chapter.schema.json` (`planned`, `facts-verified`, `drafted`, `reviewed`, `ready`, `blocked`); B08; L307; `PRODUCT.md` manifest (`planned | draft | ready`).
Wrong: B08 (in `finalize`) requires front matter `status: ready` in every hand file. No stage or command sets it. If a writer sets it by hand after `fix`, the hand file changes and the `lint` and `sync` records are stale.
Change: front matter `status` is written by the tool: `stage end` sets `draft` on `prose`, `reviewed` on `fix`, `ready` on `finalize` (a one-line rewrite of the hand files, done before the gates of that stage run). Remove B08 or turn it into "the tool could set the status". State the manifest mapping: ledger `ready` = `ready`; `drafted` and `reviewed` = `draft`; everything else = `planned`.

**25. major. The web app needs a plan data file that the contract lacks.**
Where: `PRODUCT.md` section 2 (P2), section 3 (`plan: {"d03": {"t1": ...}}`, `planShift`), section 1 (`plan.json`); `CONVENTIONS.md` A (chapter 00: data "none").
Wrong: the day-by-day checklist needs stable day ids and task ids for three plan variants. The calendar is hand-written Markdown with a `plan` table and no ids.
Change: add `data/plan.json` with `plan.schema.json`: `{"v": 1, "plans": [{"id": "a", "title", "days": [{"id": "d01", "minutes", "tasks": [{"id": "t1", "text", "chapter", "route", "minutes"}]}]}], "gates": [...]}`. Generate the three plan tables of `calendar.md` from it between `plan:start` / `plan:end` regions (add `plan` to `generated_regions.kinds` and `in_hand_files`).

**26. major. `topics` has no vocabulary.**
Where: `question.schema.json` `topics`; `CONVENTIONS.md` K18 ("the registry has them"); `book.schema.json` (no `topics` key); `PRODUCT.md` (`qindex.json`, `weakTopics`, attempt `topics`).
Wrong: K18 says the registry holds topics; the registry schema has none. The fixture uses `storage` and `security` freely. The dashboard groups by topic.
Change: add `SPEC.json` `topics` (a fixed list, for example the part ids of the seed plus `cost`, `resilience`, `performance`), and to Q111: "every topic is in `SPEC.topics`".

**27. major. Section ids are not required to be unique inside a chapter.**
Where: L103; `PRODUCT.md` routing (`#ch.vpc.nat-gateways`) and `state/progress` (`read` keyed by section id).
Wrong: the route and the progress map have no file part. Two headings with the same id in `1-fast.md` and `2-deep.md`, or two equal H3 headings in one file, collide. GitHub also renames the second anchor (`-1`).
Change: new rule L108: a section id is unique in the chapter folder (the fixed H3 names `Traps`, `A-list`, `B-list` appear once per chapter by template).

**28. major. The solver answer format does not fit `verification.solvers`.**
Where: `TOOLS-items.md` 7.3 and 7.4; `question.schema.json` `verification.solvers`.
Wrong: a solver returns `citations` as an object per label whose values are fact ids or `{source_id, quote}` objects, plus `stem_only`, `case` and `solver`. The schema allows `citations` as a list of strings and forbids other keys. 7.4 says "the result is stored" without a mapping.
Change: state the mapping: `answer` = option ids; `citations` = the sorted unique fact ids, and each quote citation as the string `<source_id>#<first 40 characters of the quote>`; add the optional schema keys `solver` (string), `stem_only` (string or null), `case_option` (option id or null), `citations_ok` (boolean).

**29. major. `create_command_regex` matches options, and several create operations cannot carry tags or have no delete.**
Where: `SPEC.json` `tasks.create_command_regex`, `banned_command_patterns`; T106, T107, T105.
Wrong:
- `\b(create|copy|run|allocate|launch)-` matches `--launch-template` and `--copy-source` (probe: `run-instances --launch-template` counts as two creates).
- T106 demands tags on operations that take none (for example `create-route`, `create-policy-version`, `create-tags` itself).
- T107 needs a `delete-<noun>` pair for operations that have none (`create-key` is undone by `schedule-key-deletion`; `create-tags` by `delete-tags` on another noun).
- `authorize-security-group-ingress.*(22|3389)` matches a group id such as `sg-0a22b` (probe).
- `create-user` is banned, so no IAM task can show a user; this may be intended, but RULINGS rule 9 does not say it.
Change: apply the create regex to the operation only (the third token of the command). Add `tasks.untaggable_operations` (exempt from T106) and `tasks.cleanup_pairs` (extra pairs, for example `"create-key": "schedule-key-deletion"`). Change the port pattern to `authorize-security-group-ingress.*--port (22|3389)\b` and add the `FromPort=22` form. Confirm the `create-user` ban in RULINGS or drop it.

**30. major. The unchanged fixture breaks Q103.**
Where: fixture `data/99-sample/questions.json`, `sample-q003`, option `a`, `why`; fixture `SPEC.json` `questions.why_words.min` 8.
Wrong: "By default, a new shelf is [private](...)." has 7 words (probe, section 5). The must-pass test of section 7 fails unless `why_words` covers wrong options only, which Q103 ("each why") does not say.
Change: lengthen the `why` to 8 words or more ("By default, a new shelf is [private](...) for its owner."), and state in Q103 that the range covers every option.

**31. major. The unchanged fixture breaks L901.**
Where: fixture `99-sample/1-fast.md` line 46; fixture `terms.json` term `crate` (`banned: ["box", "parcel"]`).
Wrong: the alt text "A Region box that contains one shelf, and a team outside the box" holds the banned variant `box`. 6.1 removes front matter, comments, code and generated regions before the text rules, not alt text. L901 is blocking and not marked (d).
Change: either change the alt text ("A Region frame ...") or add "image alt text" to the removed parts for L801, L901 and L304 (see finding 13). Proposed: change the fixture and keep alt text checked by L801 and L901.

---

## Minors

**32. minor. `customer_words` and `banned_words` both hold "spin up".** `SPEC.json` `lint`. L801 fires in `01/2-deep.md#words-customers-say`, where L902 allows the word. Also the allowed place is written `01/...`, not `01-how-the-exam-asks/...`. Change: L801 skips a customer word inside its allowed places; write the place as `01-how-the-exam-asks/2-deep.md#words-customers-say`.

**33. minor. Banned-word matching is not exact.** `SPEC.json` `lint.banned_words`, L801. "Word-boundary match" fails after `e.g.`, `etc.`, `vs.` (no boundary after a period). `may` matches the month "May". The warn word `as` fires in most paragraphs. Change: match with `(?<![A-Za-z0-9-])<phrase>(?![A-Za-z0-9-])`, case-insensitive, except `may` (lowercase only); drop `as` from `warn_words` or limit it to the start of a clause.

**34. minor. `amend` cannot change `volatility`, `hard`, `source_tier` or `bullets`.** `TOOLS.md` 5.7. A patch that sets `changed` then fails M9 because `volatility` stays `stable`. Change: add the four keys to the patch list; `hard` is recomputed by M11.

**35. minor. A hard fact needs `question`, but the schema allows null.** `fact.schema.json`, `TOOLS.md` 5.5, 5.9. The rederive packet holds only `id`, `rev`, `service`, `question`. All 7 fixture facts have no `question` (probe). Change: new check M13: `hard` true requires a non-empty `question`; add `question` to the fixture facts.

**36. minor. `derive` verdicts differ.** `vote.schema.json` description (no `partial`) and `TOOLS.md` 5.4 (`partial` allowed). Change: one list; proposed without `partial`.

**37. minor. `fact-request.schema.json` has status `duplicate`; `TOOLS.md` 5.6 never stores a duplicate.** Change: remove `duplicate` from the enum and fix the `fact` description.

**38. minor. `changed.was_evidence` is nullable in the schema; M9 requires an index.** Change: `"type": "integer"`.

**39. minor. M11 is one-directional but reads as a definition.** The fixture fact `widget-shelf-scope` (kind `behavior`, no number, no absolute word) has `hard: true`. Change: "M11: `hard` must be true when ...; it can also be true otherwise."

**40. minor. M12 is listed under "all blocking" but is "a queue, not a rejection".** Tokenisation is also undefined. Change: move M12 out of the blocking list; define tokens as lowercase `[a-z]+` words after removing every token that holds a digit.

**41. minor. Status table 5.1 says `amend` sets `candidate`; 5.7 says `amend` ends in `mech-pass` or is refused.** Also unclear: does an `amend` of a `verified` fact set `repairs`? Change: fix the table; "`repairs` is raised only when the fact was `disputed`."

**42. minor. When a `rederive` vote changes a status is not said.** 5.4 rule 1 skips `verified` facts, yet a `mismatch` "sets a `verified` fact to `disputed`". Change: "`facts vote` applies a negative `rederive` verdict at once and calls `ledger.mark_stale`."

**43. minor. `facts vote` with the default `--by` (`unknown`) and a fact whose `author` is `unknown` or null.** Change: `facts add`, `adopt` and `vote` exit 3 when the label resolves to `unknown`.

**44. minor. `facts adopt --sentence`: sentence splitting of a snapshot is undefined.** Change: "the snapshot line that holds TEXT, cut at `lint.sentence.split` boundaries".

**45. minor. `facts verify`: does a passing run write `match`, `mech` and `retrieved`?** All fixture evidence has `match: null`; a write changes the hash in `gates/99.facts-final.json`. Change: "`verify` writes the file only when a status changes; `match` is filled by `add`, `adopt` and `amend`." Also say who writes the schema field `mech`, or remove it; `supersedes` likewise.

**46. minor. L306 does not say to strip the outer quotes, and how a case-study quote is recognised.** With the quotes kept, the fixture case quote is not found; the CONVENTIONS D13 example (period inside the quotes) is not found either (probe, section 6). Change: "strip `> ` and the first and last straight double quote, then `find_quote`"; "a case-study quote is one whose matching fact has kind `case-study`"; remove the period in D13.

**47. minor. Callout parsing of a multi-line callout.** `CONVENTIONS.md` D6, L401. The lines `> **Old:**`, `> **Now:**` look like callout labels. Change: "the label of a callout is the bold text at the start of the first line of the blockquote; later lines are not labels." Note for the site build: without a hard break the five lines render as one paragraph on GitHub.

**48. minor. Contraction detection is undefined.** L803. A possessive (`Harken's`) is not a contraction. Change: add `lint.contraction_regex`: `\b\w+(n't|'re|'ve|'ll|'d|'m)\b|\b(it|that|there|what|let|he|she)'s\b`.

**49. minor. L503 `words`: column 1 holds the respelling.** Fixture: `crate (KRAYT)`; CONVENTIONS: `CIDR (SY-der) block`. Change: "remove each parenthesised part, collapse spaces, then compare with `term` case-insensitively." Also add the check "column 2 holds one bold span".

**50. minor. W901 and W202 use undefined words.** "A term defined" (where?) and "new bold terms". Change: W901 = the first occurrence of a term in the chapter's hand files, in file order, is bold and is followed by `(respelling)` when the term has one; W202 counts bold spans that equal a term of `terms.json`.

**51. minor. `minutes.pass` and `minutes.full` are not checked and not derivable.** Fixture: fast 16, pass 22, full 30; the time boxes give 19 and 28. CONVENTIONS B shows `full: 150` for a deep XL chapter; SPEC has `full: 135` and no XL value. Change: say that lint checks `fast` only, or define `pass` = `fast` + pass-route H3 time boxes + template task and quiz minutes.

**52. minor. Cut-off date: RULINGS "after 2026-07-15", CONVENTIONS "on or after", and two constants.** `book.exam_eligibility_cutoff` and `SPEC.callouts.changed_recently.not_examinable_from`. Change: one source (`book.json`); wording "after"; add to L107: a Changed recently date later than the cut-off requires `Status: not examinable yet`.

**53. minor. The 25-word limit of the one-breath `Say it` has no SPEC key outside `light_card`.** Change: add `callouts.say_it_words_max: 25`, used by L202.

**54. minor. `diagram.schema.json` uses `oneOf`,** which is not in `schema_keywords_used` and is ignored by `schemas.validate` (probe). Change: list it as "diagram module only", or remove it.

**55. minor. `TOOLS.md` section 2, row `diagram`.** `spec_path`, `svg_path` and `caption` are in `saalib/diagram/pipeline.py`, not in the package root. Change: write `diagram.pipeline.` before each.

**56. minor. `generated_regions.kinds` lists `cards`, `numbers`, `sources`, `sheet`, `exam-english`; no format uses them. `sync --only` has both `do` and `tasks`.** Change: keep `task`, `quiz`, `speak` (and `plan`, finding 25); say `tasks` = the regions in hand files, `do` = `3-do.md`.

**57. minor. `5-quiz.md` details.** Is `### Question <n>` numbered through the whole file? Is a worked question printed again under Core? How is `**Review.**` built from a section id that has no time box? Change: number through the file; print each question once (worked ones under "Worked examples"); the link is `<file>#<markdown anchor>` from `lint.sections` (add `anchor`, `route`, `minutes`, `level`, `parent` to its values; the site build needs them too).

**58. minor. `3-do.md` has no per-task marker.** The site needs task and step ids for the lab checkboxes (`PRODUCT.md` R5). Change: wrap each task in `<!-- task:start id=... -->` / `<!-- task:end -->` in `3-do.md` as well.

**59. minor. `freshen` changes `retrieved`, which `sources.md` and the fact sheets print.** Every freshen makes `sync --check` stale. Change: `freshen` ends with `sync --only sources,facts` for the touched chapters, or say that the wave workflow does.

**60. minor. Dependents scan misses `follow_ups[].facts`.** `TOOLS.md` 5.7; `speak.schema.json`. Change: add it to the list.

**61. minor. Schema and CONVENTIONS J differ.** `task.pass_route` is in the schema only. `section` is optional in all four item schemas though every rule needs it. Change: add `pass_route` to J; make `section` required (nullable only for pool `mock` if finding 9 is refused).

**62. minor. Rules with no check.** `volatile_may_decide_key` (Q112 cannot know which fact decides the key); question `sources` (no rule; tasks have T111); `pack_total: 30` (override 49); JSON text fields as inline Markdown. Change: drop the first key or define "decides" as "is linked in `explanation`"; add to Q111 "each `sources` URL is in the corpus or is an evidence URL of a fact in `facts`"; add P202 (`--all`): exactly `pack_total` speak items have `pack: true`; say "strict JSON fields hold plain text and fact links only".

**63. minor. Smaller items.**
- Rule 13 of section 0 says the fixture passes every rule, but the fixture fails `diagrams` (D01, stated in the README), `counts` (B09, open request `fr-0001`) and `tasks` with `--ship` (T113, invented commands). List the known exceptions in rule 13.
- The open request `fr-0001` has no `needs-fact` marker in `2-deep.md`, against CONVENTIONS F.
- `book.schema.json` has no place for the artifact URL that `PRODUCT.md` wants in `book.json`; add `book.artifact_url`.
- `terms.schema.json` has no `aliases` (plural and short forms) for the glossary auto-link and search.
- `data/drills.json`, `brief.json`, `brief.v0.json`, the findings files, packs and packets have no schema; the web app reads `drills.json`. Add at least `drills.schema.json`.
- Ledger `warnings` is a list of strings, but "gate warnings replace that gate's entries": define the string as `<gate>: <code> <msg>`.
- C105 rejects a back with more than one comma; a 25-word `say` back often has two. Exempt type `say`.
- `counts.questions.write` for a mock is 75; 20% more than 65 is 78.
- Medium `2-deep.md`: the minimum of "How it works" (1,200) plus the other sections at their maximum without the optional case box gives 1,700, below the file minimum of 1,800.
- RULINGS lists `data/glossary.json`; `TOOLS.md` section 1 drops it. RULINGS has precedence, so RULINGS needs the edit.
- The pack example includes `services`, which hints at the answer; and the list of stripped keys is open-ended. Say "a pack item holds exactly `id`, `type`, `select`, `stem`, `options`".
- `awscli==1.46.1` and `moto[server]==5.2.3` are version numbers from memory; confirm that they exist before pinning.
- M4 requires 8 words; many decisive AWS sentences are shorter ("Security groups are stateful."). Allow a quote of 4 to 7 words when it is a complete sentence of the snapshot.
- `lint` needs the items (L903) and `qbank` needs `lint.sections`: say that cross-module imports happen inside functions.

**64. minor. Requests for `common.py` or `saa.py`.** None are required. Finding 6 could instead put the template resolver, `word_count`, `anchor` and `section_id` in `common.py`; that is the cleaner home if the owner agrees.
