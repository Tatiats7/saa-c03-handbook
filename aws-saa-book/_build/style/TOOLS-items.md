# TOOLS, part 2: sync, question bank, cards, spoken answers, mocks, drills, tasks (version 0.9)

This file is part of `TOOLS.md` and has the same authority. It holds sections 6.2, 7 and 8; the section numbers continue those of `TOOLS.md`. Read `TOOLS.md` sections 0 (rules for every subcommand), 1 (data locations) and 2 (functions other modules call) first. Section 5 of `TOOLS.md` defines facts; section 6.1 defines the chapter lint and `lint.check_strict_text`.

| Section | Module | Subcommands |
|---|---|---|
| 6.2 | `saalib/lint.py` | `sync` |
| 7 | `saalib/qbank.py` | `q`, `cards`, `speak`, `mocks`, `drills` |
| 8 | `saalib/lab.py` | `tasks`; the rules T101 to T201 are `TOOLS-rules.md` R9 |

Numbers written here (for example "12 words") illustrate the `SPEC.json` key named beside them. Read the value from `common.STYLE_DIR / "SPEC.json"`.

## 6.2 `sync [CH | --all] [--check] [--only KIND ...]`

Generates every `source: generated` file of the chapter's template and the generated regions in hand files (`task`, `plan`, `exam-english`). `sync CH` also writes and checks the fact sheets `facts/<service>.md` of the chapter's services and of every service its hand files link (`facts.render_sheet`); `--all` writes every sheet and `glossary.md`, and `--all --check` reports a sheet that no verified fact produces. `KIND` is one of `do` (`3-do.md`), `say`, `quiz`, `sources`, `tasks` (the task regions in hand files), `plan`, `facts`, `glossary`, `exam-english`, `sheet`. Additions of contract fix 1 to this file (status commands, `--replace`, `cards build`, new rule codes) are in `TOOLS-rules.md` R5 and R6.

Rules for all output:

- Deterministic: no timestamps, items in file order unless stated, `\n` line ends, one blank line between blocks.
- Each generated file starts with the marker line (`generated_regions.generated_file_first_line`) and has no front matter. The chapter lint does not check the inside of a generated file.
- Only items with `status: ready` are printed (for questions also `verification.status` `pass` or `edited-pass`). A file with no item still gets its H1 and the line `Nothing here yet.`
- A hand file is changed only between the start and end comments of a generated region: `<!-- task:start id=... -->`, `<!-- plan:start id=a|b|c -->` (one `plan` table from `data/plan.json`; the day cell is `Day <n>`, the work cell joins the task texts with `; `), `<!-- exam-english:start group=<group id> -->` (one `exam-english` table).

Formats:

- **`5-quiz.md`** (H1 `<title>: questions`): H2 groups in the order `Worked examples` (questions with `worked`), `Core`, `Extended`. A mock prints the questions of `mock.json` in manifest order under one H2 `Questions`. Each question is a region `<!-- quiz:start id=<id> -->` ... `<!-- quiz:end -->` that holds, in this order:
  1. `### Question <n>` (numbered through the whole file; each question is printed once, a worked one only under "Worked examples"; pool `drill` is not printed) and the stem;
  2. the options as an unordered list in stored order, without letters;
  3. a reveal `Answer` with `**Answer.**` (the correct option texts), `**Deciding phrases.**` (keywords in quotes), `**Think aloud.**` (the six steps as an ordered list, when `worked`), `**Why.**` (`explanation`), `**Why not.**` (a list: the first 8 words of each wrong option in quotes, then its `why`), `**Twin.**`, `**Takeaway.**`, `**Review.**` (a link to `section`: `<file>#<markdown anchor>`, or `../<NN-slug>/<file>#<markdown anchor>` for another chapter, with the anchor from `lint.sections`). For a multiple-response question `**Why.**` also lists the `why` of each correct option.
- **`4-say.md`** (H1 `<title>: say it`): per item a region `speak:start` ... `speak:end` with `### Prompt <n>`, `**A customer asks.**` and the prompt, then a reveal `Answer` with `**In 10 seconds.**`, `**In 60 seconds.**` (the lines as paragraphs), `**Skeleton.**` (cues joined with ` / `), `**Must say.**` (list), `**Do not say.**` (list: the error, then the correction), `**Follow-up questions.**` (question and answer pairs). Chapter 49 appends the items of other chapters with `pack: true`, in chapter order.
- **`3-do.md`** (H1 `<title>: do it`): per task an H2 `<title> (<minutes> min)`, then the task body inside `<!-- task:start id=<id> -->` ... `<!-- task:end -->`. A task region in a hand file gets the same body without the H2. A step with `capture` prints its command as `<NAME>=$(<command> --query <query> --output text)`; a break-it step prints `**Why.**` and `explain` after `Expect:`; a Lab prints `**Template.**` and the template path before the steps. Body, in order: a line `Look`, `Try` or `Lab`; `**It kills the belief.**` and `kills`; `> **Cost:** <cost>. If you forget the cleanup: <cost_if_forgotten>.`; `**Permissions.**`; `**No permission to create resources?**` and `read_only_alternative`; the steps as an ordered list (text, the command in a `bash` fence, `Expect:`; a break-it step first prints `**Predict.**`); `> **Clean up:**` and the cleanup list with commands; `**Verify.**`; `**Still costs money if left.**`; `> **Careful:** <tasks.stop_rule>`; the label with the `checked` date. A Look task prints no cleanup, verify, stop-rule or cost-if-forgotten lines.
- **`sources.md`** (H1 `<title>: sources`): one list item per AWS page cited by a fact that the chapter uses (links in hand files, `facts` of its items), sorted by title: `- [<title>](<url>). Checked <retrieved>. Facts: [<id>](../facts/<service>.md#<id>), ...`.
- **`glossary.md`**: H1 `Glossary`; per term, sorted by `term`: `### <term>` (the GitHub anchor must equal the term id, else exit 1), the respelling, `meaning`, `**Words that go with it.**`, `**Do not confuse with.**`.
- **`exam-english.md`** (chapter 01): the nine groups as H2, each word as a row of a `plain` table (`Word | Meaning | It signals`).
- **`sheet.md`** (46, 47, 48): 46 lists every signals row and trap of every chapter, grouped by chapter; 47 every A-list and B-list row; 48 every Changed recently entry and every fact with `changed`, newest first.

`sync --check` writes nothing: it builds every output in memory and compares bytes. JSON `{"checked": 6, "stale": ["99-sample/5-quiz.md"], "missing": []}`; exit 1 when either list is not empty. `sync` without `--check` prints `{"written": [paths], "unchanged": 3}`. `sync` exits 3 when a data file is not valid against its schema. `lint.gate_sync(ch)` is `sync CH --check` as a gate dict (code `S01` per stale or missing file).

**Must-fail tests:** after a change to one `takeaway`, `sync --check` exits 1 and names `5-quiz.md`; a hand edit inside a task region is reported stale; a candidate question is not printed; running `sync` twice gives identical bytes; a fresh sandbox reports the generated files as missing.

## 7. Question bank (`saalib/qbank.py`): `q`, `cards`, `speak`, `mocks`, `drills`

### 7.1 `q add --chapter CH --file F [--replace] [--by L]`

Under the lock of `questions.json` (created with the wrapper `{"v": 1, "chapter": "<slug>", "items": []}` when missing). For each item:

- `chapter` = slug; an item without `id` gets the next free `<slug>-q<3 digits>`;
- set `status: candidate`, `rev` 1, `keyRev` 1, `verification` `{"status": "candidate", "round": 0, "solvers": []}`;
- `pool` defaults to `mock` in a mock chapter, else `chapter`;
- set `volatile` (`questions.volatile_rule`);
- add the `--by` label to `authors` (an author cannot solve the question);
- run the item rules Q101 to Q116; an item with an error is not stored, and neither is a near-duplicate of a live question or a copy of a rejected one (Q302, `TOOLS-rules.md` R10).

`--replace` replaces an existing id (`TOOLS-rules.md` R5 has the three cases: before verification, the one edit at `verification.round` 1, and a verified question; a second edit in round 1 is Q207); `keyRev` + 1 when the set of correct options changed.

JSON `{"added": ["vpc-q019"], "replaced": [], "rejected": [{"index": 2, "id": null, "errors": [findings]}]}`; exit 1 if any was rejected.

### 7.2 `q lint CH [--ship]`, `q lint --all`

**Item rules (blocking)**

| Code | Rule | SPEC.json `questions.*` |
|---|---|---|
| Q101 | Schema (an item's schema error is Q101, not X01); id starts with the slug; `pool` is `mock` exactly in mock chapters | |
| Q102 | Option count for the type; correct options = `select`; `single` has `select` 1; two options with the same normalised text; a multi stem ends with the instruction, a single stem has none | `options`, `select_allowed`, `multi_instruction` |
| Q103 | Word ranges of stem, options (difficulty 1 has its own), explanation, each why (of every option, correct or wrong), takeaway, twin, and the explanation total | `*_words`, `explanation_total_words` |
| Q104 | When the mean option length is 10 words or more: an option outside 30% of the mean; at any mean, a key longer or shorter than every wrong option by 3 words and the spread (R10) | `option_length_spread_max`, `option_length_spread_applies_from_mean_words` |
| Q105 | Banned text in an option, or an option that points at other options; a negative stem (R10; unless the chapter override allows it); an option letter or position reference in any field (R10) | `banned_in_options`, `negative_stem_regex`, `letter_reference_regex` |
| Q106 | `qualifier` is `none` (only at difficulty 1), or stands verbatim in the stem and starts with a qualifier word; the stem has at most one qualifier word in capitals | `qualifier_words`, `qualifiers_per_stem`, `no_qualifier_only_at_difficulty` |
| Q107 | Each keyword is a substring of the stem | `keywords` |
| Q108 | A wrong option has a `trap` or a `misconception` and a `distractor_type`; a correct option has none of the three; at most one `impossible-feature`, whose `why` links a fact; difficulty 2 and 3 have a `violates-qualifier` option; a question with `qualifier` `none` has none | `wrong_option_needs`, `distractor_types`, `impossible_feature_*`, `violates_qualifier_rule` |
| Q109 | A trap id that `lint.traps()` does not know (hand files and briefs) | |
| Q110 | Every id in `facts` is `verified`; `explanation` holds at least one fact link; strict fields pass `lint.check_strict_text` with the stem as scenario (the quoted phrase after the twin prefix is exempt); each linked fact is in `facts`; no link in the no-link fields; `worked.steps` is example text | `strict_text_fields`, `example_text_fields`, `no_link_fields`, `stem_numbers_exempt_in_strict_fields`, `twin_quoted_phrase_exempt` |
| Q111 | `task` is in the exam guide and starts with `domain`; `bullets` belong to the task; `services` are in-scope keys and `services[0]` is the focus service; every topic is in `questions.topics`; `section` resolves (`lint.sections` of the item's chapter, or of the chapter named in `<NN-slug>/...`; that form is required for pool `mock` and `drill`); each `sources` URL is in the corpus or is an evidence URL of a fact in `facts`; each `exam_english` id matches the stem | `topics`, `sources_rule`, `exam_english_match` |
| Q112 | `volatile` is true, or a fact linked in the explanation or a correct `why` is volatile now (`facts.is_volatile`) | `volatile_window_months`, `volatile_rule` |
| Q113 | Overlap: Jaccard of content tokens between the stem and the key option, minus the highest such value of a wrong option, is over the margin; or the key is made of stem words (R10) | `stem_key_overlap_margin_max` |
| Q114 | `twin` prefix; `twin_of` names an earlier question of the chapter with a different set of correct option texts, the same `layer` and `twin_of` null, with at least `twin_min_questions_between` questions between the two in the file; `worked` has six steps with the starters in order and the word range; the wrong-path marker is in step 5 exactly when `wrong_path` is true | `twin_*`, `worked_*` |
| Q115 | A banned word outside stem and option text | `lint.banned_words_scope` |
| Q116 | A question of pool `chapter` or `drill` without a bullet | `bullets_rule` |

Content tokens: lowercase words of 3 or more letters that are not in the module's stop-word list. For a multi question, the "key option" of Q113 is the correct options joined.

**Chapter rules** (warnings; blocking with `--ship`, which the `questions-verified` and `counts` gates use)

| Code | Rule | Keys |
|---|---|---|
| Q201 | Counts (pool `drill` is not counted): without `--ship`, at least `shipped` questions that are not rejected exist; with `--ship`, the `ready` questions are exactly `shipped`, split into `core` and `extended`, with the twin pairs, multi range, worked and wrong-path counts | `templates.<t>.counts.questions` |
| Q202 | From 10 questions: one option position is the key in more than 40%; the key is the longest option in more than 35% | `key_position_share_max`, `key_is_longest_share_max` |
| Q203 | More than 2 questions on one `concept`; two questions with the same concept and the same set of traps (twins exempt) | `questions_per_concept_max`, `unique_concept_trap_pair` |
| Q204 | Questions without a qualifier above 25% (always blocking); difficulty mix outside the tolerance (always a warning) | `no_qualifier_share_max`, `difficulty_mix` |
| Q205 | Fewer than half of the wrong options carry a trap id | `trap_share_min` |

**Bank rules** (`--all`): Q301 duplicate ids; Q302 near-duplicates (`qbank.similarity`, R10; also per chapter in `q lint CH`); Q303 (warning) an exam-English word in fewer than 3 stems (`exam_english_match`; `q words --need` prints the same list); Q304 (warning) the multi share of the bank differs from 15% by more than 5 points.

JSON of `q lint`: `{"chapter": "99", "ok": true, "errors": [], "warnings": [findings], "counts": {"total": 4, "candidate": 0, "verified": 0, "ready": 4, "rejected": 0, "multi": 1, "twin_pairs": 1}}`. Exit 1, 2 or 0.

`gate_questions` = item rules + chapter rules without `--ship`. `gate_questions_verified` = the same with `--ship`, plus: every `ready` question has `verification.status` `pass` or `edited-pass` (Q206).

### 7.3 Blind packs: `q pack --chapter CH --lens closed|open|ambiguity [--round N] [--ids ...] --out FILE`

Takes the questions with `verification.status: candidate` and `verification.round` = N (default 0). The pack:

```json
{"pack": "vpc-r0-closed", "chapter": "10", "lens": "closed", "round": 0, "instructions": "...",
 "items": [{"id": "vpc-q012", "type": "single", "select": 1, "stem": "...",
            "options": [{"label": "A", "text": "..."}, {"label": "B", "text": "..."}]}]}
```

- **Keys:** a pack item holds exactly `id`, `type`, `select`, `stem` and `options` (each option: `label`, `text`). Nothing else of the question is in a pack.
- **Options permuted per solver:** `random.Random(sha256("<mock_seed>|<id>|<lens>|<round>").hexdigest()).shuffle(options)`, then labels `A` to `F` in the new order. No key file is written; `adjudicate` recomputes the permutation.
- **Self-check and record:** Q401 (exit 1) when a pack item holds any other key; `packs.jsonl` records a hash of what the solver saw (R10).

A solver returns:

```json
{"pack": "vpc-r0-open", "lens": "open", "solver": "label", "answers": [
  {"id": "vpc-q012", "answer": ["B"], "flag": null, "stem_only": null,
   "citations": {"A": ["vpc-sg-stateful"], "B": [{"source_id": "docs/vpc/latest/userguide/x", "quote": "..."}], "C": ["..."], "D": ["..."]},
   "case": null}]}
```

- `stem_only` (closed lens): the solution stated before reading the options.
- `citations` (open lens): an entry for every label: why the key is right, and why each other option is wrong.
- `case` (ambiguity lens): `{"label", "text"}`, the strongest case for one wrong option.
- `flag`: a sentence when the solver sees a second defensible answer or a missing constraint, else null.

### 7.4 `q adjudicate --chapter CH --answers F1 F2 F3` and `q adjudicate --chapter CH --select`

The three answer files are refused as a whole (exit 3, nothing stored) unless they pass the checks of R10 (one round; three different solvers, none an author; a pack for every question; `stem_only`; `case`). Then, for each question: map labels back to option ids; `agree` = the answer set equals the key set. Citations verify when every label has at least one citation, every cited fact id is `verified`, every `{source_id, quote}` passes `find_quote`, and the R10 conditions hold (6 words, not one citation for all, one citation from the question's own facts or evidence). The result is stored in `verification.solvers`, one entry per lens: `answer` = the option ids; `agree`; `flag`; `solver`; `stem_only` (closed); `case_option` = the option id of `case.label` (ambiguity); `citations` = the sorted unique fact ids, with each quote citation as `<source_id>#<first 40 characters of the quote>`, and `citations_ok` (open).

- **Pass:** all three agree, no flag, citations verify. `verification.status` = `pass` in round 0, `edited-pass` in round 1; `status: verified`; `checked` = today.
- **Fail in round 0:** `verification.round` = 1, `note` = the reasons. The question is listed in `needs_edit`. One edit with `q add --replace`, then three fresh packs with `--round 1`.
- **Fail in round 1:** `status: rejected`, `verification.status: rejected`; the item is appended to `_build/qbank/rejected.jsonl`.

JSON `{"pass": [ids], "needs_edit": [{"id", "reasons": ["closed disagrees", "ambiguity flag"]}], "rejected": [ids], "below_min": false}`. `below_min` is true when the questions that are `ready`, `verified` or still `candidate` are fewer than `shipped`. Exit 1 when `below_min`, else 0.

`--select` chooses the shipped set from `verified` and `ready` questions and sets exactly those to `ready` (the others to `verified`): take twin pairs first until `twin_pairs_min`, then worked questions up to `worked`, then fill `core` and `extended` to their counts while `multi` stays in range. Order of preference inside each step: `pass` before `edited-pass`, then questions with a bullet that no chosen question has, then id. Exit 1 when the counts cannot be met; nothing is changed then.

### 7.5 `q dedupe [--threshold 0.6]`, `q list`

`q dedupe` compares every pair of non-rejected questions in the whole bank, mocks included, with `qbank.similarity` (R10: stem shingles at or above the threshold, a reordered copy, a padded copy); a pair is a `duplicate` unless one is the `twin_of` the other. A pair in different chapters with the same `concept`, the same traps and the same correct option concepts is reported as `same-signature` (warning). JSON `{"pairs": [{"a": "vpc-q003", "b": "mock-exam-1-q017", "similarity": 0.71, "kind": "duplicate"}]}`; exit 1 when a duplicate exists, 2 with only same-signature pairs.

`q list [--chapter] [--status] [--pool] [--task]` prints `id status verification difficulty type task concept`.

### 7.6 `cards add|lint`, `speak add|lint`

`cards add --chapter CH --file F` and `speak add --chapter CH --file F` work like `q add` (ids `<slug>-c<3 digits>`, `<slug>-s<2 digits>`; `status: candidate`; item rules block). `--replace` replaces an item in place (`rev` + 1, `status: candidate`). A reviewer sets `status: ready` with `cards set-status` or `speak set-status` (`TOOLS-rules.md` R5). `cards add` refuses a generated type; `cards build` writes those (R5). `cards lint CH [--ship]`, `speak lint CH [--ship]` and `--all` print the same JSON shape as `q lint`.

Card rules (`cards.*`):

- **C101** Schema; id starts with the slug.
- **C102** Back over 12 words (25 on a `say` card); front over 30 words.
- **C103** A type without its required `facts`, `term`, `word` or `speak` reference, or a reference that does not exist (facts `verified`; term in `data/terms.json`; word in `data/exam-english.json`; speak item in the chapter).
- **C104** A `number` card without the cloze, or whose cloze text holds no `display` of its fact (`holds_display`), or whose fact is not in `lint.a_list_facts(ch)`.
- **C105** A banned front start; a list answer (the back has a line break, a semicolon, more than one comma, one comma followed by `and` or `or`, or two slashes; type `say` is exempt).
- **C106** Two cards whose fronts have a content-token Jaccard of 0.8 or more, or one front holds 95% of the other's tokens, without the same `pair` value.
- **C107** `extra` fails `lint.check_strict_text`; a banned word in any field.
- **C108** `section` does not resolve (null is allowed on a generated card); `trap` is not a known trap id.
- **C109** A number with a unit in `front` or `back` that no `display` of a fact in `facts` holds (`holds_display`).
- **C201** (warning; blocking with `--ship`) chapter counts per template (`counts.cards`; hand types only).
- **C202** (`--all`) `data/01-how-the-exam-asks/cards.json` does not hold `cards.exam_english_cards` generated `word` cards, one per word of `data/exam-english.json`.
- **C204** (warning; blocking with `--ship`) an A-list fact (`lint.a_list_facts`) without a `number` card.
- **C203** (warning) a front that names no term, no service name and no word of the chapter title.

Speak rules (`speak.*`):

- **P101** Schema; id starts with the slug.
- **P102** `ten_second` over 25 words; `sixty_second` outside 105 to 145 words or 7 to 12 lines; a sentence over 16 words; a key point over 30 words, a follow-up answer over 60, a `must_not_say` correction over 40 (`speak.*_words_max`).
- **P103** The four starters missing or out of order (in a `compare` item a first sentence that starts with `Both ` replaces the first starter); the last line does not end with `?`.
- **P104** Not 4 skeleton cues; a cue over 6 words.
- **P105** Must points outside 3 to 5; nice points over 2; a must point without a `verified` fact; `must_not_say` outside 2 to 3, or with a fact that is not `verified`; not 2 follow-ups.
- **P106** A digit (outside a name: `digits_allowed_inside_names_regex` and `digits_allowed_rule`), a bracket or a link in `ten_second` or `sixty_second`.
- **P107** An `avoid` word of `terms`, or a banned word, in a script.
- **P108** `section` does not resolve.
- **P109** A spoken number in a script (R10) that is not a `spoken` form of a fact in `facts`; a number with a unit in a key point, correction or follow-up answer that no `display` of its facts holds (`speak.spoken_number_rule`).
- **P201** (warning; blocking with `--ship`) chapter count and `pass_route` count.
- **P202** (`--all`) the speak items with `pack: true` are not exactly `speak.pack_total`. `speak set-pack --chapter CH ID ... [--off]` (orchestrator) sets the flag.

### 7.7 `mocks assemble [--mock 50|51|all] [--seed N]`, `mocks check [--mock ...]`

The pool of a mock is its own `data/<dir>/questions.json` (writers add `counts.questions.write` items with pool `mock`). Candidates: `status` `verified` or `ready`, `verification.status` `pass` or `edited-pass`, `volatile` false. Seed: `--seed`, else `book.mock_seed` + the chapter id as a number. With `rng = random.Random(seed)` and candidates sorted by id:

1. For each task statement of `exam-guide.json`, in id order: `rng.choice` of the unused candidates of that task. No candidate: fail.
2. For each domain 1 to 4: shuffle the remaining candidates of the domain with `rng`; take them in that order until the domain has its `domain_split` count. Skip a candidate whose focus service (`services[0]`) already has `max_questions_per_service` questions, or that would put the multi count above its maximum.
3. If the multi count is below its minimum: for each missing one, swap the last-taken single question of a domain (not one chosen in step 1) for the first unused multi candidate of the same domain that keeps the service limit.
4. `rng.shuffle` the chosen ids. Write `mock.json`; set the chosen questions to `ready` and the other candidates to `verified`.

Any shortfall: exit 1, nothing written, JSON `{"mock": "50", "ok": false, "short": [{"domain": 3, "need": 15, "have": 12}], "missing_tasks": ["3.5"]}`. Success: `{"mock": "50", "ok": true, "seed": 20261054, "counts": {...}, "spares": 9}`. The same seed and bank give the same manifest.

`mocks check` (codes K..; blocking unless marked):

- **K01** Manifest schema; as many unique ids as the sum of `domain_split`; each exists in the mock's file with pool `mock`.
- **K02** The domain split is exact (`templates.mock.mock.domain_split`).
- **K03** Every task statement of the exam guide appears.
- **K04** No reuse: an id that is in the other mock or has pool `chapter`; a `q dedupe` duplicate with any chapter question or with the other mock.
- **K05** A volatile question.
- **K06** A focus service with more than `max_questions_per_service` questions.
- **K07** The multi count is outside `counts.questions.multi`.
- **K08** A question that is not `ready` with a passed verification.
- **K09** Q202 on the mock.
- **K10** (warning) the share of any difficulty differs by more than 5 points between the mocks.

JSON `{"mocks": [{"mock": "50", "ok": true, "errors": [], "warnings": [], "counts": {...}}]}`.

### 7.8 `drills build [--seed N] [--size 20]`, `drills check`

Writes `data/drills.json` = `{"v": 1, "seed": 20261004, "drills": [{"id": "drill-d1", "domain": 1, "title": "Domain 1 drill", "questions": [ids]}]}`, one drill per domain. Candidates: `ready` questions with pool `drill`, or with pool `chapter` and layer `extended`. With `random.Random(seed + domain)`: one question per task statement of the domain first, then shuffled candidates up to `--size`, at most 2 per chapter. A drill shorter than `--size`: warning, exit 2. `drills check` verifies that every id exists, is `ready`, belongs to the domain and is in no mock (exit 1 otherwise). Drills are read by the web app; no Markdown is generated.

**Must-fail tests of section 7:**

- `q add` rejects: two correct options on a single (Q102); a key twice as long as the other options (Q104); `always` in an option (Q105); `Option B` in an explanation (Q105); a keyword that is not in the stem (Q107); a wrong option without trap and misconception (Q108); an explanation with `up to 500 widgets` as plain text (Q110); an unverified fact (Q110); a stem that repeats the key's words (Q113).
- A pack holds no `correct` and no `why`; two lenses get different option orders for at least one question; the same lens and round give the same order twice.
- `adjudicate` fails a question when one solver disagrees, when the ambiguity solver sets a flag, and when a citation quote is not in the snapshot; a second failure rejects the question.
- `q dedupe` finds a copied stem.
- `mocks assemble` fails with one task statement missing; `mocks check` fails on a 19/18/15/13 split, on a chapter-pool id and on a volatile question; the same seed gives the same manifest. (Tests build a synthetic pool in the sandbox from the fixture questions.)
- `cards lint` fails a 14-word back and a `number` card outside the A-list; `cards add` refuses a `partner` card; `speak lint` fails a script with a digit, one without "The thing to watch is", and one that says "six hundred widgets" (P109).
- `q add` rejects a difficulty 2 question with qualifier `none` (Q106) and a question without a bullet (Q116); `q set-status --status ready` refuses a question whose verification has not passed.

## 8. Tasks (`saalib/lab.py`): `tasks`

`tasks add --chapter CH --file F [--replace]` works like `q add` (id `<slug>-t<2 digits>`; the tool sets `label` to `tasks.label` and `checked` to today).

### 8.1 `tasks lint CH [--ship]`, `tasks lint --all`

A command is every `steps[].command`, `cleanup[].command` and `verify.command`. The rules T101 to T201 are in `TOOLS-rules.md` R9 (moved there on 2026-10-09 with the gate-break changes).

JSON as for `q lint`. `gate_tasks` = `tasks lint CH` without `--ship` (item rules block; T113 and T201 warn). The `counts` gate runs the `--ship` form. A task becomes `ready` with `tasks set-status` (`TOOLS-rules.md` R5).

### 8.2 `tasks check-cli CH | --all [--reference]`

Runs the helper `tools/helpers/cli_model.py` with `uv run --script` (inline dependency `awscli==1.46.1`). The helper reads a JSON list of commands on standard input and prints JSON; it makes no AWS call and reads no credentials. For each command it splits with `shlex`, loads the AWS CLI command table and checks: the service exists; the operation exists; every `--option` exists for the operation or is a global option; every required option is present; no stray word, single-dash option, unknown shorthand key or enum value; the `--query` fields exist (R9). Result per command: `{"command", "service", "operation", "ok", "errors": ["unknown option --tag"], "tag_options": [...]}`.

The tool writes `_build/reports/cli/<chapter id>.json` = `{"chapter", "awscli": "1.46.1", "checked": "2026-10-06", "commands_sha256", "ok", "commands": [...], "warnings": [T118]}`.

`--reference` also calls `corpus.fetch("https://docs.aws.amazon.com/cli/latest/reference/<service>/<operation>.html")` and requires that `final_url` ends with `/<operation>.html` (a wrong command redirects to an index page).

Exit 0 when all commands are ok; 1 for an unknown service, operation or option; 5 when `uv` or the package index cannot be reached (nothing is written). Tests patch `lab._run_helper(commands) -> list`.

### 8.3 `tasks emulate CH [--task ID]` (optional, never required)

Runs the helper `tools/helpers/emulate.py` with `uv run --script` (`moto[server]==5.2.3`, `awscli==1.46.1`). The helper starts a moto server on `127.0.0.1` with a free port, sets dummy credentials, sets `AWS_CONFIG_FILE` and `AWS_SHARED_CREDENTIALS_FILE` to `/dev/null` and `AWS_ENDPOINT_URL` to the local server, passes `--endpoint-url` to every command (the variable alone is ignored) and sends every other request to a dead local proxy (R9), and runs steps, cleanup and verify as argument lists (no shell). A break-it step must fail; every other command must return 0.

Result in `_build/reports/emulate/<task id>.json`: `{"task", "result": "pass|fail|not-supported", "steps": [{"command", "rc", "ok"}]}`; `not-supported` when moto does not implement an operation. Exit 0 for `pass` and `not-supported`, 1 for `fail`, 5 when the helper cannot start. The printed label of a task does not change.

**Must-fail tests of section 8:** a Try without cleanup (T103); a create command without a book tag in any accepted syntax (T106; `--tags Key=book,Value=saa Key=task,Value=<id>` must pass); `--launch-template` on `run-instances` is not a second create (T107); a `$VPC_ID` without a capture (T115); a break-it step without `explain` (T110); `aws s3api put-bucket-acl --acl public-read` (T105); `authorize-security-group-ingress` on port 22 (T105); a cleanup list that deletes one of two created resources (T107); cleanup in creation order for two different nouns (T107); `aws configure` (T105); a cost of `$0.05` without a cost fact (T109); a command with a pipe (T104); a label other than the fixed one (T101); a verify without a tag filter that names a resource without the `saa-` prefix, names a `saa-` resource the task does not create, is not read-only, or names nothing (T108; `aws iam get-role --role-name saa-<task id>` on a role the task creates, with an `expect`, must pass); `check-cli` on the fixture's invented `aws widget` commands exits 1 (with `lab._run_helper` patched to report an unknown service). The unchanged fixture tasks pass `tasks lint` without `--ship`.
