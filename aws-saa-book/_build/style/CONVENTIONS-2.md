# CONVENTIONS, part 2: pattern, front and synthesis pages; JSON items; decisions (version 1.0)

This file is part of `CONVENTIONS.md` and has the same authority. Version 1.0 adds the strict twin rule (J2) and decisions 35 to 40 (section K); the freeze of 2026-10-11 adds section U and decisions 41 to 46 (`_build/reports/exemplar-fix.md`). `RULINGS.md` overrides it; `SPEC.json` holds its numbers. Section letters continue those of `CONVENTIONS.md`: P (pattern chapters), S (front and synthesis pages), J (JSON items, continued; it also holds the additions to `STYLE.md` sections 6 to 9), U (additions of the 1.0 freeze to sections D, E and G), K (decisions, continued).

The examples use the invented service Amazon Widget Store. They show form only.

## P. Pattern chapters (40 to 43)

**`1-fast.md`.**

| H2 | role | Holds |
|---|---|---|
| `Predict` | `predict` | 2 Predict prompts, one gist trap |
| `The question behind it` | `question` | one `Say it` (the question that every pattern of the chapter answers), the bold field `**The problem it solves.**`, one `Startup example` (the Problem of the chapter in `STARTUP.md`). No diagram here. |
| `The spectrum` | `map` | Predict the picture with the hero diagram |
| `Patterns at a glance` | `glance` | one `glance` table, 6 to 10 rows, one row per pattern card of `2-deep.md`, in the same order. No `Deciding question`. |
| `Service by service` | `matrix` | one `services` table |
| `Signals and traps`, `Check`, `Recap from memory` | | as in a service chapter |

```markdown
<!-- table: glance -->
| Pattern | Problem | Choose when |
|---|---|---|
| Two shelves | One shelf is too small | The widgets stay in one Region |

<!-- table: services -->
| Service | Keeps a copy | You operate |
|---|---|---|
| Amazon Widget Store | In [one AWS Region](../facts/widget.md#widget-shelf-scope) | Nothing |
```

A `services` table has the first header `Service` and 2 or 3 more headers that the brief names for the chapter. Both tables are strict text.

**`2-deep.md`.** "The patterns" holds 6 to 10 pattern cards (D16). The H3 is the pattern name, 1 to 6 words, with a time box. `**Problem.**` is a scenario in exam English and can hold story values ("an RPO of 15 minutes"). The five other fields are strict.

```markdown
### Two shelves (2 min)

**Problem.** A company keeps 600 widgets that must stay in one Region.

**Services.** Amazon Widget Store.

**Cost and effort.** Two resources to count.

**Choose when.** The widgets are more than one shelf holds: a shelf holds [up to 500 widgets](../facts/widget.md#widget-shelf-max-widgets).

**Not when.** The widgets travel between Regions.

**Common wrong alternative.** Many crates in one Region.

**Stop and answer.** A team has 450 widgets in one Region. Does the team need this pattern?
```

A reveal follows the Stop and answer, as in D8.

**Recognise-only services.** A deep, medium or pattern chapter whose registry entry has a `cards` list adds `2-services.md` (front matter `file: services`), with one service card (D15) per key of the list. The cards are the same as in a light family chapter. Services in `cards` get no subsection in `2-deep.md`.

## S. Front and synthesis pages

A section of these chapters holds what its `counts` and `fields` in `SPEC.json` `chapter_overrides` name, and nothing else is required. The field labels there read as follows: a label that ends in `.` or `:` is a bold field; `diagram ...` is a diagram embed (section H); `table:<kind>` is one table of that kind; `callout:<Label>` is one callout; `comment:<name>` is the HTML comment `<!-- <name>: ... -->`.

**Fact rule in these chapters.** Roles `orient`, `method` and `plan` are heuristic text. The book's own study times need no link ("20 minutes a day"). Every exam rule is a fact of namespace `exam` and is linked: exam length, number of questions, passing score, result timing, retake wait, reschedule limits, the ESL accommodation. A percentage or count of her own plan ("score 75% on mock 1") ends with `<!-- no-fact: plan -->`.

### S1. Chapter 00: calendar and mistakes log

`data/plan.json` (`plan.schema.json`) holds the three plans with stable ids: plan `a`, `b`, `c`; days `d01` to `d19`; tasks `t1`, `t2`. The web app reads it for the daily checklist. `calendar.md` holds hand text around three generated regions; the tool fills each with one `plan` table (`Day | Minutes | Work`; the day cell reads "Day 1"):

```markdown
## Plan A (2 min)
<!-- section: role=plan; route=fast; minutes=2 -->

Plan A is the full plan: 19 days.

<!-- plan:start id=a -->
<!-- plan:end -->
```

Day 1 of every plan holds a task with the text "request ESL +30 before booking". Readiness gates are in `plan.json` (`gates`) and are written as prose under "Readiness gates".

`mistakes.md` is filled by the reader. "Cause codes" lists the five codes of `SPEC.json` `lint.cause_codes`: K (did not know), C (confused two similar things), W (missed a word in the stem), T (time), D (dated question that assumes an old limit). "Log" holds one table with one example row:

```markdown
<!-- table: log -->
| Date | Question | Cause | Sure | Fix |
|---|---|---|---|---|
| Day 3 | sample-q002 | W | yes | Read the last sentence first |
```

`Sure` is her confidence mark (`yes` or `no`). After the chapter is `ready`, the lint checks only the front matter, the two headings and the table header of this file.

Task 0 (the budget alert) is the first Try of chapter 02.

`00-start-here/calendar-preview.md` (the preview the reader already saw) is not in the template of chapter 00: the lint reports it as L101 (a warning with `--draft`, an error from the `edit` stage on), and the file is removed when chapter 00 is finalized (RULINGS, calendar continuity).

### S2. Chapter 01: exam English

- There is no hand section "Worked examples". The two worked questions print first in `5-quiz.md`.
- "Exam English core words" (`1-fast.md`) is hand text. Each word it teaches is a `word` of `data/exam-english.json`, bold at first use. It has no table.
- "The nine word groups" (`2-deep.md`) has nine H3 subsections, one per group of `data/exam-english.json`, in file order, with the group title as heading. Each holds a short hand paragraph and one generated region:

```markdown
### Optimisation qualifiers (3 min)

These words tell you which of two working options the question wants.

<!-- exam-english:start group=qualifiers -->
<!-- exam-english:end -->
```

The H3 carries a time box, and the H3 time boxes add up to the H2 time box, as under "How it works".

The tool fills the region with a table of kind `exam-english` (`Word | Meaning | It signals`). `exam-english.md` is the same data as one generated file.

### S3. Chapter 44: architecture page (D17)

Ten H2 sections, each one page: `**Requirement.**` (a scenario in exam English; an example block), one diagram of kind `arch` or `sequence` with its numbered steps, one `breaks` table, and `**If the question adds.**` with exactly three list items of the form `- "<added phrase>": <what changes>`.

```markdown
## Widgets for two Regions (4 min)
<!-- section: role=page; route=pass; minutes=4 -->

**Requirement.** A company must serve 300 widgets to teams in two Regions with the LEAST operational overhead.

![Two Regions, each with one shelf, and a copy arrow between the shelves](../diagrams/svg/reference-architectures-two-regions.svg)

**Figure.** Each Region has its own shelf, and the second shelf is a copy.

1. The team creates a shelf in the first Region.
2. The team copies the shelf to the second Region.

<!-- table: breaks -->
| Remove this | What breaks |
|---|---|
| The copy | The second Region has no widgets: a shelf stores widgets in [one AWS Region](../facts/widget.md#widget-shelf-scope) |

**If the question adds.**

- "the widgets travel every week": use a crate instead of a copy.
- "more than 500 widgets": add a shelf, because a shelf holds [up to 500 widgets](../facts/widget.md#widget-shelf-max-widgets).
- "only the owner reads them": no change; a new shelf is [private](../facts/widget.md#widget-shelf-default-private).
```

The quoted phrase of an "If the question adds" item is an example block; the text after the colon is strict.

### S4. Chapter 45: atlas page (D18)

Twenty-four H2 sections, one per decision. Each holds one diagram of kind `ladder`, one `compare` table, the bold field `**Rule.**` (one sentence) and, when the chapter's `questions.json` has a twin pair for the decision, the comment `<!-- twins: <question id> <question id> -->` on the next line. In this role the line after the `compare` table is `**Rule.**`, not `**Deciding question:**`.

```markdown
<!-- table: compare -->
| Question | Shelf | Crate |
|---|---|---|
| Does it change Region? | No: you [cannot move a shelf](../facts/widget.md#widget-shelf-move) | Yes |

**Rule.** Widgets that stay go on a shelf; widgets that travel go in a crate.
<!-- twins: decision-atlas-q001 decision-atlas-q002 -->
```

The H2 heading is the decision as a short name ("Shelf or crate"). The "All decisions" table of `1-fast.md` is a `matrix` table with 24 rows.

### S5. Chapters 46, 47, 48, 49, 52

- **46 "Top traps".** One list, no table and no H3. Each item repeats a trap of another chapter in the form of D5 and ends with `<!-- trap-ref: <trap id> -->`. A `trap-ref` must exist as a trap in another chapter; it defines no new id.
- **47 "A-list".** One or more `numbers` tables (at most 40 rows each), no H3. Each row is an A-list row of another chapter.
- **48.** Changed recently entries as in D6.
- **49.** The six cross-service speak items carry `section` in the form `<NN-slug>/<file>#<section id>`.
- **52.** "Pacing plan" and the other `method` sections state study and pacing times freely; exam rules are linked.

## J. JSON items, continued

A JSON text field holds plain text. Strict fields can also hold fact links; no field holds other Markdown.

### J1. What the writer supplies

The input of `q add`, `cards add`, `speak add` and `tasks add` is an item without the tool-set fields.

| Item | The tool sets | Notes for the writer |
|---|---|---|
| question | `chapter`, `id` (when absent), `status`, `rev`, `keyRev`, `verification`, `volatile`, `authors` (the `--by` label; an author never solves the question) | Leave `sources` empty unless a page beyond the fact evidence is needed. |
| card | `chapter`, `id`, `status`, `rev`, `generated` | Leave `tags` empty; the export derives tags from the fields. |
| speak item | `chapter`, `id`, `status`, `rev` | Set `pack` to false; the orchestrator chooses the pack. |
| task | `chapter`, `id`, `status`, `rev`, `label`, `checked` | |

`section` is required on every item. It is `<file>#<section id>` for a section of the item's own chapter and `<NN-slug>/<file>#<section id>` for a section of another chapter (required form for pool `mock` and `drill`, and usual in chapters 40 to 45 and 49). Section ids and trap ids are valid as soon as `brief.json` names them, before the prose exists.

### J2. Questions (adds to STYLE section 7)

- **Options.** Four for a single answer; five for "(Select TWO.)"; six for "(Select THREE.)".
- **Qualifier.** `qualifier: "none"` only at difficulty 1. A question of difficulty 2 or 3 has a qualifier and at least one `violates-qualifier` option; a question without a qualifier has none.
- **Keywords** can include the qualifier phrase.
- **`why` of a correct option** says why the option is right. The app shows it after the answer; it prints per option for a multiple-response question. The word range covers every `why`.
- **Twins.** The later question of a pair carries `twin_of`; the earlier has `null`. Both have the same `layer`. At least 3 other questions stand between them in the file. The `twin` line of each quotes the changed phrase of the other. The quoted phrase after "If the stem said" is scenario text and needs no link.
- **Strict twins (1.0).** At least one twin pair of a deep or medium chapter is strict: the two stems differ in one phrase, the option texts are identical, and the key moves to another option. Write the shared options in neutral words that fit both stems ("where the application runs", not "on each server"). Example: `exemplar/questions.json`, `iam-q002` ("the call fails with an access denied error") and `iam-q006` ("the call succeeds, but the next call to read a report fails").
- **State the side the twin does not test.** When a stem tests one half of a two-sided rule, it states the other half ("Their IAM policies allow sts:AssumeRole on the role ARN"), so that exactly one option is right.
- **Think-aloud.** `worked.steps` is example text: no link is required, and every AWS fact it states is in the question's `facts`. With `wrong_path: true`, step 3 states the wrong prediction and step 5 holds one sentence that starts "My first idea breaks because".
- **Exam English.** The brief gives each question slot zero or more exam-English words. Use the word (or one of its `also` forms) in the stem and list its id in `exam_english`. `q words --need` shows the words that still need stems.
- **Topics** come from the list `questions.topics` in `SPEC.json`.
- **Bullets.** A chapter or drill question lists at least one bullet of its task.
- **Core and extended.** The brief marks each question slot `core` or `extended`. Core questions have difficulty 1 or 2.
- **Volatile facts.** Do not let a fact with a recent change decide the key (the fact card shows the change). The tool sets `volatile`; a volatile question fails the lint.
- **Drill questions** (pool `drill`) live in the `questions.json` of their topic chapter and are not printed in `5-quiz.md`.
- **Copies.** `q add` refuses a near-duplicate of any live question of the bank (a reordered or padded copy too) and a copy of a rejected question (Q302). A question that failed its first round gets one edit; a second `q add --replace` in round 1 is refused (Q207).
- **Blind solving.** The three answer files name three different solvers, none of them an author of the question; a closed-book answer states the solution before the options (`stem_only`); an ambiguity answer names a wrong option and the strongest case for it; an open-book citation names a verified fact or quotes at least 6 words from a saved page, and at least one citation per question is a fact of the question or a quote from its evidence page.
- The fixture twin pair is decided by a number with a change date. It passes only because the fixture's volatile window is 6 months. Do not copy that choice: in the book a twin pair turns on a stable fact.

### J3. Spoken answers (adds to STYLE section 6)

- In a compare prompt, a first sentence that starts with "Both " replaces "The short answer is". The other three starters stay.
- Numbers in a script are words. Copy the `spoken` form of the fact from the fact card ("five hundred widgets"); the lint compares it. A number with a unit in `key_points[].point`, `must_not_say[].correct` or `follow_ups[].answer` uses the `display` of a fact of the item.
- A digit is allowed only inside a name (S3, EC2, Route 53, gp3).
- A key point has at most 30 words, a follow-up answer 60 and a `must_not_say` correction 40 (`4-say.md` prints them).

### J4. Flashcards (adds to STYLE section 9)

- Writers write `decide`, `differ`, `number` and `cannot` cards. `cards build` generates `term`, `meaning` and `partner` cards from `data/terms.json`, `word` cards from `data/exam-english.json`, and `say` cards from the speak items of the pack. The counts in `SPEC.json` count the four written types.
- Every A-list row has one `number` card.
- A number with a unit on the front or the back uses a `display` of a fact in `facts`.

### J5. Tasks (adds to STYLE section 8)

- **Commands.** One plain command per step: no line break, no `>` or `<` redirect, no `${NAME}` or lowercase `$name`; `--cli-input-json` and `file://` are not used for rule or policy options; a `curl` command uses only the allowed options. It starts with `aws `, or with `curl ` or `dig ` for a read-only check. `aws configure list` is allowed; `aws configure export-credentials`, `sts get-session-token` and every other command that prints credentials are banned (T105), as is every form of `aws configure` that writes.
- **A value from an earlier step.** Give the earlier step a `capture`: `{"name": "VPC_ID", "query": "Vpc.VpcId"}`. The tool prints that step as `VPC_ID=$(<command> --query Vpc.VpcId --output text)`. Later commands use `$VPC_ID`.
- **A value she chooses or reads.** An uppercase placeholder in angle brackets (`<ACCOUNT_ID>`), explained in the step `text`.
- **Tags.** Write `book=saa` and `task=<task id>` in the tag syntax of the service, inside the tag option itself (the lint reads only the values of tag options). Where a create operation takes no tag, give the resource a name that starts with `saa-` and tag it in the next step with the tagging operation of the service. The verify command filters by the tag `task=<task id>` (`SPEC.json` `tasks.verify_rule`), so that it returns nothing after this task's cleanup. A verify through the Resource Groups Tagging API needs a verified fact that the API lists that resource type; without one, file a fact request and park the task.
- **Cleanup.** Every create step (also `import`, `register`, `restore`, `request`, `provision`, `purchase`, `s3 mb` and `put-<noun>`) has its own delete in `cleanup`, in reverse order, naming the capture variable or the resource name; `--dry-run` is not a cleanup. A Look holds only read-only operations. A security group rule never opens port 22 or 3389 to the world or to a large range. Write amounts in the cost line as `$4.50`; a money word without an amount is an error.
- **Break-it step.** `predict` (the question), `command`, `expect` (what she sees, without AWS facts) and `explain` (why, with the fact link). The next step is the fix.
- **Lab.** `template` names the file `data/<NN-slug>/templates/<task id>.yaml`, which builds the routine part. The writer supplies that file; its resources carry the two tags.
- **Title** uses letters, digits, spaces and hyphens only (it becomes a heading). **`kills`** is the wrong belief in straight double quotes.
- **Routes.** Look tasks belong to the Fast route (`pass_route: false`). Exactly one Try of a chapter has `pass_route: true`.
- **Try it.** Every Try and Lab has exactly one `Try it` callout in the section that its `section` names.
- **IAM users.** A task creates no IAM user and no access key. It can list or read existing ones.

## F2. Fact links: what the lint matches (adds to `CONVENTIONS.md` section F; 2026-10-09)

- **The value in a link text.** A `display` that starts or ends with a digit must not touch another digit of a longer number: `up to 45 Gbps` does not hold `5 Gbps`, `2 500 widgets` does not hold `500 widgets`, `11,000` does not hold `1,000` (`lint.holds_display`). Beside the value the link text holds no other number and no negation (`not`, `never`, `without`, `except`, `but`, `instead of`, `rather than`, `no longer`, `n't`): `[not 500 widgets](...)` and `[not 500 widgets but 9000 widgets](...)` are errors (L303).
- **A number with a unit** is also: a number with one or two plain words before the unit (`5 read replicas`, `7 full hours`); a number with a plus sign (`9000+ requests`); a number word above twelve, or a compound one, before a unit or a count noun (`nineteen hours`, `nine hundred widgets`; `three laptops` is not matched). A number with a unit that stands outside the link text of its sentence needs a link of its own, even when the sentence has another fact link (L304).
- **Absolute words** include their spellings and synonyms: `can not`, `no more than`, `not more than`, `at least`, `not possible`, `impossible`, `does not support`, `do not support`, `unsupported`, `exclusively`, `invariably`, `no one`, `nobody`, `unlimited`, `limited to`, `a maximum of`, `a minimum of`, `under no circumstances`, `at all times`.
- **What is read.** The text is normalised first (full-width digits, non-breaking spaces, entities, zero-width characters), so none of them hides a claim. Inline code that reads as prose (`up to 9000 widgets`) is checked; inline code that is a command, an option or a name is not. A sentence that ends with a question mark is checked for a number with a unit, not for absolute words. `<summary>` lines are checked.
- **Short displays (RULINGS, 2026-10-11).** A display without a digit is a verbatim phrase of at most 8 words from one quote of the fact (`SPEC.json` `fact_links.number_free_display_words_max`); a `needs-display` request follows the same rule. The link text is the short display; the rest of the sentence carries the scope in plain words. Displays verified before the ruling stay valid until the orchestrator re-cuts them.
- **The link text reads as part of your sentence.** The comparison ignores case, so write a display in lowercase in mid-sentence (`the [connections must always be initiated ...]`, not `[Connections ...]`). Do not link a display that says "we" for AWS, or that repeats a preposition of your sentence; request another display instead.
- **AWS quote blocks** (D12) hold whole sentences of the evidence quote of a verified fact: the span starts at a sentence start and ends at a sentence end, or at the end of quoted speech; a table-row quote is the row. A span cut from the middle of a sentence is an error (L306).

## U. Additions of the 1.0 freeze (2026-10-11)

These rules add to `CONVENTIONS.md` sections D, E and G. `CONVENTIONS.md` is at its word budget, so they live here. Reason and source of each: `_build/reports/exemplar-fix.md`.

### U1. How-it-works subsection (adds to D8 and STYLE 11.1)

The blocks come in this order:

1. The problem in one or two plain sentences, with no label.
2. A numbered trace with bold step names.
3. A table that compresses the trace, when the trace has two or more cases (a truth table: one row per case, the result in the last column).
4. One "Why does AWS work this way?" reason.
5. One `Exam signal`. Where no AWS fact decides the stem phrase, an `Exam heuristic` replaces it.
6. Go deeper reveals (D9, optional), and `Try it` and `Spot the bug` where the chapter places them.
7. One `Say it` (U2), the block directly before the Stop and answer.
8. The Stop and answer and its reveal, the last blocks of the subsection.

Counts: `say_it_per_subsection` and `exam_signal_per_subsection` in `SPEC.json` (deep and medium). The lint checks them after the tool change of `TOOLS-rules.md` R11; the claims reviewer checks them until then. Neither callout counts toward `callouts_max` (decision 41).

Time box: the `time_box` guidance of `SPEC.json` `lint.minutes_formula`. A full subsection of about 400 words with its reveals takes 5 minutes. With 14 subsections, "How it works" holds at most 4,400 words, so a subsection averages about 4 minutes. A planned stub carries the time box of the subsection that it will become, never a placeholder.

A stub ("Planned:") names only what fits 400 words as one mechanism with a trace. Move a list of features into Go deeper, or split the subsection.

### U2. Say it in How it works

`> **Say it:** The short answer is ... The thing to watch is ...`: at most 25 words, written for speech. Sentences have at most 16 words and no documentation wording: "both evaluations return Allow" is documentation; "both sides have to allow the request" is speech. The watch move names a limit of this subsection's own answer, not another topic. Prefer wording without an absolute word, so that the line needs no link.

### U3. Changed recently entries that are not examinable yet (adds to D6)

```markdown
> **Changed recently:** (2026-08-19) Default number of widgets on a shelf.<br>
> **Old:** [200 widgets](../facts/widget.md#widget-shelf-max-widgets).<br>
> **Now:** [500 widgets](../facts/widget.md#widget-shelf-max-widgets).<br>
> **The exam probably expects:** the old value, if any. Do not let this number decide an answer.<br>
> **Status:** not examinable yet.
```

The entry stands in `2-deep.md` directly under the B-list. Its `The exam probably expects:` line ends "Do not let this number decide an answer."; the Status line is last (L107). `Old:` links a display of the old value (`changed.was` of the fact). When that display is missing, write the value without a link and add `<!-- needs-display: <fact id> "<value>" -->`. When every change of a chapter is not examinable yet, the fast section holds the second sentence of `grounding.exempt_sentences`: "No examinable change since July 2022 affects an answer in this chapter; a newer change is under the B-list in 2-deep.md."

### U4. Check reveals and Recap prompts (adds to D1 and D7)

```markdown
**Check 1.** A team in Frankfurt also wants its widgets in Paris. Can the team use its Frankfurt shelf?

<details>
<summary>Answer</summary>

No. A shelf stores widgets in [one AWS Region](../facts/widget.md#widget-shelf-scope).

**Predict 1:** No, for the same reason: the shelf stays in its Region.

</details>
```

Each Recap prompt asks for a sentence, a row or a cell that `1-fast.md` states above it. A Recap prompt never introduces a term or a fact: a prompt about something she has not read is a new question with a hidden answer (`SPEC.json` `prompts.recap_rule`).

### U5. The brief's traps fit the callout limit

`brief.json` holds at most `templates.<template>.counts.brief_traps_max` traps (deep 13, medium 7): the fast traps list (deep at most 5, medium 3) plus the `Exam trap` callouts that `2-deep.md` can hold beside its `Try it` callouts. The orchestrator merges or drops traps that no question cites. `gate_brief` checks the cap after the tool change of `TOOLS-rules.md` R11; the orchestrator counts until then.

### U6. Terms and short forms in each file (adds to G)

The first use, in each hand file, of a term of the chapter's `brief.json` `terms` is bold (or cell 1 of a words table) and carries the respelling when the bank has one. A term of another chapter is not bolded, and a Predict prompt does not define a term. Every short form (AZ, SCP, VPC, MFA, ARN, AWS STS, OU, RCP) is spelled out at first use in each file; only the names in `_build/registry/services.json` and the H1 are exempt (`SPEC.json` `lint.term_rules`, `lint.abbreviation_rule`). The lint implements both after the tool change of `TOOLS-rules.md` R11; the reader lens checks them until then.

## K. Decisions, continued

26. Startup name: the working name Harken (R, L) collides with real companies; `STARTUP.md` renames the startup to Callvale. `SPEC.json` `startup.name` is Callvale; the data file is `data/startup.json` (it was `data/harken.json` until 2026-10-09). RULINGS records both.
27. L devices that need no writer action, because the web app builds them from the JSON items: return questions at the chapter opening (from the `questions.json` of earlier chapters in study order), the daily mix, the stem-first instruction line, the confidence mark in the app, the Today page and the repair index. A generated region for return questions was rejected: it would make `1-fast.md` stale whenever another chapter's bank changes.
28. Cards: L counts nine card types. Writers write four; the tool generates `term`, `meaning`, `partner`, `word` and `say` cards, so that no card has two sources. The template counts keep their numbers and now count the four written types; the orchestrator can lower them.
29. Headings and facts: an assertion heading can hold an absolute word; the grounding is a fact link in the body. One review asked to forbid such headings; L's assertion headings need them, and hard rule 1 is still met.
30. Study times in advice sections need no fact link; exam rules do. One review proposed a unit exemption, the other a marker; the unit exemption covers study times, a word list keeps exam rules strict, and the marker covers the rest.
31. A template section has a `key` in `SPEC.json`; "section id" always means the heading anchor without the time box.
32. Light service card: R fixes 150 to 220 words, so the minimum stays (a review asked for 100). The range is a warning, and `What it is.` can have two sentences.
33. Fact-link exemptions are narrower than in version 0.9: `Exam signal` is strict after its quoted phrase; role `plan` is heuristic, not exempt; think-aloud steps stay example text (R: role `worked`); every other exception needs the visible `no-fact` marker. The orchestrator is asked to confirm decision 23 in RULINGS.
34. Stages stay parallel: trap ids, section headings and diagram texts are fixed in `brief.json`, and item lints resolve against the brief until the prose exists (one review also offered to make `prose` a prerequisite of the item stages; that would cost the parallel build of PL section 10).

Decisions of version 1.0 (2026-10-11, the exemplar panel: five judges, three attempts; report `_build/reports/exemplar-spec-changes.md`):

35. House pattern: attempt A (first principles: problem, numbered trace, compressing table, transfer question) won. Its skim-proof headings and truth tables stay. The reader judge preferred attempt C, so C's spoken form is grafted as a device, not as the frame.
36. Spoken rehearsal: every How-it-works subsection carries one `Say it` callout before its Stop and answer (D8). It does not count toward `callouts_max` (`SPEC.json` `callouts.not_counted_toward_callouts_max`), because 8 to 14 subsections with one line each would fill the limit of 12 and push out the traps and signals. C's founder-question frame was rejected as the structure: it gives the answer in the line after the question, so the question is not a retrieval event.
37. Stem phrases: B's "the phrase that decides it" opener moves to an `Exam signal` callout after the mechanism, because the reader skipped stem advice that named terms not yet defined.
38. Changed recently: a `not examinable yet` entry stands in `2-deep.md` under the B-list (D6), because two judges found it padding in the 15-minute file; `SPEC.json` `callouts.changed_recently.placement`.
39. Twins: at least one strict twin pair per deep or medium chapter (J2). The lint does not check identical options yet; the claims reviewer does.
40. Tasks: the verify step keeps the tag filter that T108 requires. Whether the Resource Groups Tagging API lists IAM roles is unverified; the judges' alternative (`aws iam get-role`, expect NoSuchEntity) needs a tool change, described in the report. Amended by decision 44.

Decisions of the 1.0 freeze (2026-10-11, the consistency check and the reader lens; report `_build/reports/exemplar-fix.md`):

41. Exam signal: one per How-it-works subsection (U1). It does not count toward `callouts_max`, for the reason of decision 36; an `Exam heuristic` that replaces it does not count either. The brief's traps are capped (U5), so that the fast list and the `Exam trap` callouts of `2-deep.md` can hold every brief trap (L905).
42. Fast-file reading time: the deep `1-fast.md` keeps the 1,800-word cap of RULINGS and the 20-minute target, but its sections shrink (signals 6 to 8 rows, traps 4 to 5, Recap 3 prompts, smaller Signals, Changed and Recap budgets; Check grows from 140 to 150 words for the separate Predict paragraphs of U4). The reader lens also asked for a file cap of 1,400 words; that is a RULINGS budget, so the orchestrator decides it. `lint.minutes_formula.fast_check` states the reading-time check (review until the lint implements it). The consistency check's proposal to raise the fast target to 23 minutes was rejected: the reader needs a file that she can finish in 20.
43. Displays: the RULINGS limit of 8 words for a display without a digit is now in F2 and in `SPEC.json`. The long displays that the exemplar links were verified before the ruling; they stay until the orchestrator decides whether to re-cut them.
44. Task verify: the verify command filters by `task=<task id>` (J5), so that it returns nothing after the task's cleanup; T108 replaces `<task id>` in `verify_tag_patterns` as T106 does. Whether the Resource Groups Tagging API lists IAM roles is still unverified (exemplar README).
45. Terms and short forms follow U6 (per file, per brief). The term-bank fixes (respellings of common words set to null, the IAM core terms, the short forms MFA, ARN, RCP and OU) are data changes for the orchestrator, listed in `exemplar-fix.md`.
46. Check reveals answer Predict in their own paragraph, and Recap prompts recall only the fast file (U4), because a skimmer could not tell two answers apart in one paragraph, and a Recap about unread content teaches her that Recap does not work.
