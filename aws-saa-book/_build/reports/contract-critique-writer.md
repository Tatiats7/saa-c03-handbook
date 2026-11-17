# Contract critique: the writer's view (IAM pilot)

Reviewer role: a writer who must produce chapter 03 (IAM, deep, XL) from `CONVENTIONS.md`, `STYLE.md` and `SPEC.json` (all version 0.9). Checked against `RULINGS.md`, `TOOLS.md`, `TOOLS-items.md`, `TOOLS-diagram.md`, the schemas, the fixture book, `LEARNING.md`, `PRODUCT.md` section 4 and `PIPELINE.md` section 10. No contract file was edited.

Severity: **blocker** = two agents would build incompatible things, or a required thing is impossible. **major** = likely rework. **minor** = small guess or inconsistency.

Counts: 3 blockers, 34 majors, 21 minors (58 findings).

Short names: CONV = `CONVENTIONS.md`, SPEC = `SPEC.json`, T-items = `TOOLS-items.md`, fixture = `tools/tests/fixtures/book/`.

---

## Blockers

1. **blocker. SPEC `tables.rows_max` (16) against three required tables.**
   `chapter_overrides.00` calendar "Plan A" needs `plan_rows` 19. `chapter_overrides.45` "All decisions" needs `matrix_rows` 24. `chapter_overrides.47` "A-list" needs 20 to 40 rows. L502 fails every table above 16 rows, and no text says that a count can be split over several tables.
   **Change:** add `rows_max` per kind in `tables.kinds` (`plan`: 19, `numbers`: 40, `matrix`: 24), or state in CONV G: "a row count in `counts` is the sum over all tables of that kind in the section; split a long table under H3 headings". Pick one and say it in both files.

2. **blocker. T-items T106 and T108, SPEC `tasks.tag`, `tasks.create_command_regex`; STYLE section 8 rule 3.**
   T106 requires the literal strings `book=saa` and `task=<id>` in every create command, and T108 requires `book=saa` in the verify command. Real AWS CLI syntax for the pilot does not contain these strings: IAM uses `--tags Key=book,Value=saa Key=task,Value=iam-t02`; EC2 uses `--tag-specifications 'ResourceType=...,Tags=[{Key=book,Value=saa}]'`; the tagging API uses `--tag-filters Key=book,Values=saa`. Some operations that match `create_command_regex` cannot carry a tag at all (`s3api create-bucket`, `ec2 create-route`, `iam create-policy-version`, `ec2 create-tags`, `s3api copy-object`). A deep chapter needs 2 to 3 Try tasks, so the IAM pilot cannot pass `tasks lint`.
   **Change:** in SPEC add `tasks.tag_patterns`: `["book=saa", "Key=book,Value=saa", "Key=book,Values=saa", "{Key=book,Value=saa}"]` (same for `task`), and `tasks.untaggable_operations` (a list that T106 skips, each needing a following tagging step or a `saa-` name). Rewrite T106 and T108 to use them. In STYLE section 8 rule 3 add: "Use the tag syntax of the service; where an operation takes no tag, tag in the next step or rely on the `saa-` name."

3. **blocker. Trap ids and section ids are not fixed before the parallel stages. TOOLS 3.1 (stages 6 to 10 all have the single prerequisite `brief`), the `brief.json` shape, CONV D5 and I.**
   Trap ids are born in the prose writer's `### Traps` list. Question, card and task writers must cite them (Q109, C108, T111), and `section` must resolve against the real headings (Q111, C108, P108, T111). `q add` does not store an item with an error. If the stages run in parallel, as PIPELINE section 10 plans, every item is rejected, or two writers invent different ids for one belief. `brief.json` holds section ids but no trap list.
   **Change:** add to `brief.json`: `"traps": [{"id", "belief", "truth", "facts"}]` and state in CONV D5 and D8: "Trap ids and H2/H3 heading texts come from the brief. A writer does not rename them; a needed change is reported in the result." Also make `prose` a prerequisite of `questions`, `cards`, `speak` and `tasks` in TOOLS 3.1, or make Q109/Q111/C108/P108/T111 warnings until the `edit` stage.

## Majors: deep chapter (IAM)

4. **major. Trap supply. SPEC `templates.deep...signals.counts.traps` (5 to 6), `questions.trap_share_min` (0.5), CONV D5, CONV E (`Exam trap`).**
   A deep chapter ships 18 questions with about 57 wrong options; at least half need a trap id, but the chapter may define only 5 to 6 traps, and only in the `### Traps` list. The `Exam trap` callout has no id syntax. The writer must guess whether heavy reuse is intended or whether ids can be defined elsewhere.
   **Change:** CONV E: "An `Exam trap` callout in `2-deep.md` can end with `<!-- trap: <id> -->`; `lint.traps()` collects ids from the traps list and from these callouts." State in STYLE section 7 that one trap id can be cited by several questions with different `concept` values.

5. **major. Are headings strict text? CONV C/D8/F, STYLE section 5, TOOLS L304.**
   An assertion heading is a claim ("An explicit deny always wins", "A role session lasts at most 12 hours"). The heading regex forbids links, and L304 speaks only of "a sentence or table cell". CONV silently changed LEARNING's "public only because of one route" to "public because of one route", which suggests headings are checked. Lint builder and writer will decide differently.
   **Change:** CONV F, add to the exempt list: "H2 and H3 headings. A heading with an absolute word or a number with a unit needs at least one fact link to the same fact in the body of its subsection (L304 reports the heading line otherwise)." Add `headings.grounding: "body-link"` to SPEC.

6. **major. Diagram text is ungrounded. CONV H, `TOOLS-diagram.md` (spec keys), RULINGS hard rule 1.**
   A diagram spec has `claim`, `say` sentences and labels, and no `facts` key. A caption such as "A role session lasts up to 12 hours" is a hard fact with no check. CONV does not say whether the `**Figure.**` caption can hold a fact link.
   **Change:** add optional `facts: []` to the diagram spec; `diagram` lint runs `lint.check_strict_text` logic on `claim` and `say` (a number or absolute word needs a listed fact whose `display` is in the text). CONV H: "The caption can hold fact links; lint compares caption and `claim` after `normalize_text`."

7. **major. Two sources for caption, steps and alt text. CONV H and D14, SPEC `diagram_embed`, `hero_steps`.**
   The spec has `claim`, `say` per step and `alt` (at least 20 characters). The Markdown has the caption, a hand-written step list and alt text (at least 10 characters). Nothing says they must be equal, or who writes which. Also `hero_steps` needs 4 to 6 steps, but only `arch` and `sequence` return steps; a writer who picks a `ladder` for policy evaluation as the IAM hero cannot meet the count.
   **Change:** CONV H: "Caption = spec `claim`, step sentences = spec `say`, alt = spec `alt`, each equal after `normalize_text` (L702, L703). The hero diagram is of kind `arch` or `sequence`." Set both alt minimums to 20. Say in CONV H who writes the spec (the chapter writer, or the diagram agent from the brief).

8. **major. The prose gate cannot pass before the diagrams exist. TOOLS 3.1 (`prose` and `diagrams` both depend only on `brief`), L701, L704.**
   L701 ("has no SVG file") and L704 are not marked (d), so `lint --draft` fails until the `diagrams` stage has rendered the files. Three failed ends block the chapter.
   **Change:** mark "has no SVG file" in L701 and L704 as (d), or make `diagrams` a prerequisite of `prose`.

9. **major. No way to write a forward cross-reference. CONV G ("Link to a section only after it exists"), L601.**
   IAM is written in W1. It must point to SCPs (04), Identity Center (05), KMS key policies (06), S3 bucket policies (21). Pattern chapters 40 and 41 (W7) "link back" to chapters of W8 to W10. A link to a missing file is a blocking error, even in draft.
   **Change:** CONV G: add a marker `<!-- xref: <chapter id> <topic words> -->` after the sentence; W-code in draft and `reviewed`, resolved to a real link in W14 (error at `ready` only in the whole-book pass). Mark the "missing file of a later wave" case of L601 as (d).

10. **major. Story budget cannot hold the required story. SPEC `startup.story_max_words_per_chapter` (80), W902, STYLE section 5, SPEC `decision.words.max` (280), CONV C ("startup example" in In one breath).**
    W902 counts the Startup example callouts plus the Decision record against 80 words. The Decision record alone has five fields and up to 280 words. The fixture has about 111 words (27 in the callout, 84 in the Decision record) and breaks the rule.
    **Change:** define story as the `Startup example` callouts only: W902 "more than 80 words in the Startup example callouts of a chapter". Leave the Decision record to its own section limit.

11. **major. Section budgets that cannot hold the required devices. SPEC `templates.deep.files[0].sections` and `resolution.word_count` ("text inside details blocks count").**
    - `recap`: 5 prompts with answers in 110 words is 22 words per prompt and answer; the fixture needs 25 to 27. LEARNING's 130 words did not count hidden answers.
    - `check`: 3 prompts with answers in 110 words; the fixture needs about 37 each.
    - `signals`: 12 rows (about 27 words each) plus 6 traps (about 24 each) is about 480 against 420.
    - `numbers` (`2-deep.md`): 8 A-list rows of 3 cells plus up to 12 B-list rows is about 280 against 180.
    - `changed`: 4 entries of about 40 words against 140.
    **Change:** either exclude reveal text from section counts (keep it in the file count), or raise: `recap` 160, `check` 140, `signals` 500, `numbers` 300, `changed` 180. State the choice in `resolution.word_count`.

12. **major. What counts in a "How it works" subsection. CONV D8 ("Body: 150 to 400 words"), SPEC `subsection_words`, `lint.stop_and_answer_interval_words`.**
    Unclear whether the 150 to 400 words include the Stop and answer, its reveal, a Go deeper block (up to 150 words), callouts and a Spot the bug. With a Go deeper block counted, the body shrinks to 250 words. Also `stop_and_answer_interval_words.min` 250 contradicts `subsection_words.min` 150 (each subsection ends with a Stop and answer).
    **Change:** SPEC: `"subsection_words_count": "paragraphs, lists, tables and callouts of the subsection; not Go deeper blocks, prompts or reveals"`; set `stop_and_answer_interval_words.min` to 150 or delete `min`. Repeat the sentence in CONV D8.

13. **major. Absolute words that are not AWS facts. CONV F, SPEC `tables.kinds.signals`, L304.**
    The "But not if" column describes a stem condition ("traffic goes only to S3": LEARNING's own sample row) and is strict, so it needs a fact link in a 15-word cell. Requirement language in prose ("when the workload must not store keys") is flagged too. A writer will add false links or twist sentences.
    **Change:** (a) SPEC `signals.heuristic_columns: [1, 3]` and CONV F heuristic list: add "the 'But not if' column". (b) Add an escape marker in CONV F: `<!-- no-fact: requirement -->` or `<!-- no-fact: stem -->` at the end of the sentence; lint accepts it, counts it in the report, and the claims reviewer checks every use.

14. **major. Heuristic text is a hole in hard rule 1. CONV F ("Heuristic text"), K23, SPEC `callouts.labels` (`Exam signal`: heuristic).**
    An `Exam signal` callout inside "How it works" can say "points to a network ACL, because a security group cannot deny" with no link and pass. RULINGS exempts only roles `example`, `task`, `worked`; CONV adds `predict`, `plan` and the whole heuristic class.
    **Change:** make `Exam signal` strict outside its quoted stem phrase (`grounding: "strict"`, plus "text in double quotes at the start of an Exam signal is an example block"). Ask the orchestrator to confirm K23 in RULINGS.

15. **major. Twin questions: three guesses. CONV J, STYLE section 7, schema `twin_of`, Q114, T-items 6.2.**
    (a) Is `twin_of` set on one question of the pair (the fixture) or on both? (b) "Place the twins apart" has no meaning in JSON: file order is print order, and no rule says how far, or whether both twins share a layer (the Pass route does core only). (c) The quoted alternative phrase in `twin` is strict text: `If the stem said "for 2 hours" instead: ...` needs a fact link in the same sentence only because of the quoted number.
    **Change:** CONV J: "The later question of a pair carries `twin_of`; the earlier has null. Both twins have the same `layer`. At least 3 questions stand between them in the file (lint Q114)." CONV F: "text in double quotes after `If the stem said` is an example block." The `twin` line of a question that has a real twin quotes the changed phrase of that twin.

16. **major. The wrong-path think-aloud has no form. STYLE section 7 ("Think-aloud"), SPEC `questions.worked_step_starters`, schema `worked`.**
    Six fixed steps with fixed starters leave no place for the wrong path, and no example has `wrong_path: true` (the fixture count is 0). Also unclear: are `worked.steps` strict text? Steps 4 and 5 state AWS facts ("I remove ... because a security group cannot deny"), but the field is in neither `strict_text_fields` nor `no_link_fields`.
    **Change:** STYLE: "With `wrong_path: true`, step 3 states the wrong prediction, and step 5 contains the sentence that starts `My first idea breaks because`." Add that string to SPEC as `worked_wrong_path_marker` and a fixture question that uses it. Add `worked.steps[]` to `strict_text_fields` (stem numbers exempt).

17. **major. Hard facts in fields without links cannot be checked. CONV F last bullet, STYLE section 6, P-rules, SPEC `speak`, `questions.no_link_fields`.**
    Scripts write numbers as words ("five hundred"), and `key_points[].point`, `must_not_say[].correct`, `follow_ups[].answer`, card `front` and `back` carry digits and absolute words as plain text. No rule ties them to the item's `facts`.
    **Change:** new rules P109 and C109: "a number written as words in a script contains a `spoken` string of a fact in `facts`; a number with a unit in `point`, `correct`, `answer`, card `front` or `back` contains a `display` of a fact in the item's `facts`." Say in STYLE section 6: "copy the spoken form from the fact card."

18. **major. Break-it step has no "explain". STYLE section 8 ("predict, break, observe, explain, fix"), schema `step`, SPEC `tasks.break_it_step_needs`.**
    The step has `predict`, `command`, `expect`. The fixture puts the explanation, an AWS fact, into `expect` as plain text.
    **Change:** add `explain` (string, strict text with fact links, required when `break_it` is true) to the step schema and to `break_it_step_needs`; T-items 6.2 prints it as `**Why.**`. State that the fix is the next step.

19. **major. No placeholder for values she must fill in. T104, SPEC `code.banned_patterns` (`[0-9]{12}`), CONV G ("no account ids").**
    IAM commands and IAM policy examples need an account id or an ARN from an earlier step (`sts assume-role --role-arn`, a cross-account `Principal`). `$(` is banned, a variable assignment is not an `aws` command, and the 12-digit ban also hits the example ids that AWS documentation uses.
    **Change:** define one placeholder style in CONV G and T104: uppercase in angle brackets (`<ACCOUNT_ID>`, `<ROLE_ARN>`), each explained in the step `text`; allow the documentation ids `111122223333` and `444455556666` in fenced `json` blocks (add `code.allowed_account_ids`).

20. **major. Commands that are not `aws` commands, and read-only `aws configure`. T104, SPEC `tasks.banned_command_patterns`.**
    LEARNING's top tasks need `curl` and `dig` (tasks 4, 9, 19), and reading the CloudShell credentials (task 2, IAM) is naturally `aws configure export-credentials` or `aws configure list`, which the pattern `aws configure` bans.
    **Change:** SPEC `tasks.allowed_command_prefixes: ["aws ", "curl ", "dig "]`; change the banned pattern to `aws configure( set|$| sso| import)`.

21. **major. A Lab has no place for its template. STYLE section 8 (Lab: "a template builds the routine part"), schema `task`.**
    No field holds the template or its path, and code blocks stop at 12 lines.
    **Change:** add `template` (path under `data/<dir>/templates/<task-id>.yaml`) to the task schema; T-items 6.2 prints the upload instruction; `tasks lint` checks that the file exists.

22. **major. Exam-English coverage has no mechanism. LEARNING 4.6, SPEC `questions.exam_english_word_min_stems`, Q303.**
    Each of 90 words must stand in at least 3 stems, but a question has no field for it, the brief assigns no words, and the match rule (word, `also` forms, case) is undefined. The IAM writer cannot know which words to use.
    **Change:** add optional `exam_english: ["ee-..."]` to the question schema (lint: the `word` or an `also` form is in the stem, case-insensitive); add `exam_english` to each `question_slots` entry of `brief.json`; add `q words --need` that lists words below 3 stems. One sentence in STYLE section 7.

23. **major. LEARNING devices with no home in the contract. LEARNING section 3 (devices 9 to 13, 15), CONV K.**
    Return questions (3 questions from chapters N-1, N-3, N-6 at the chapter opening), the daily mix, the stem-first instruction line, the confidence mark, the Today page and the repair index have no section, region, field or decision.
    **Change:** add a decision to CONV K for each: "built by the web app from `questions.json`; no writer action", or define it. For return questions, the smallest fix is a generated region at the top of `1-fast.md` (`<!-- return:start -->` ... `<!-- return:end -->`, add `return` to `generated_regions.in_hand_files`).

24. **major. The Harken fact sheet does not exist. STYLE section 5 ("Never contradict the Harken fact sheet"), RULINGS, SPEC `startup`.**
    SPEC holds only the name and the cast. The numbers and the stage table are in LEARNING section 8 with the old chapter numbers.
    **Change:** write `_build/style/HARKEN.md` (or `data/harken.json`): the fixed numbers, the stage of each chapter id of `book.seed.json`, and what Harken has already built before that chapter. Name the file in STYLE section 5 and lint Harken numbers in example blocks against it.

25. **major. Which words must be in `data/terms.json`, and how to ask for one. CONV G ("Use only terms from `data/terms.json`"), L503, L901, W901.**
    The bank has 9 IAM terms. The chapter needs about 15 more (trust policy, permissions boundary, session policy, instance profile, root user, managed policy, federation, ARN, MFA, external ID). Unclear: can prose use them unlisted, or only not define them in bold and not put them in the words table? `term_requests` in the result is the only path; there is no command and no marker, and L503 blocks even in draft.
    **Change:** CONV G: "Every word in bold as a definition and every row of a words table is a term of the bank. Other AWS nouns are free. Request a term with `<!-- needs-term: <term> -->` (warning in draft, error from `reviewed`)." Mark the `words` part of L503 as (d). Grow the bank before W1 from the brief.

26. **major. `banned` entries in the real `data/terms.json` are not matchable. `terms.schema.json` ("variants that must not appear in prose"), L901.**
    Entries such as `server (for EC2)`, `zone (for a Region)`, `region (lowercase, for an AWS Region)` carry conditions in parentheses. A literal match never fires; a match on the first word hits "hosted zone", "Local Zone", "landing zone".
    **Change:** split the field: `banned: [{"text": "zone", "unless_after": ["hosted", "Local", "landing", "Availability"], "note": "..."}]`, or keep `banned` literal and move conditions to a `banned_note`.

27. **major. Customer words that are official AWS terms. SPEC `lint.customer_words`, `customer_words_allowed_in`, L902.**
    "landing zone" is the official Control Tower term (chapter 04), "cold start" is the Lambda term (18), "guardrails" describes SCPs and permissions boundaries (03, 04). "`data/terms.json`" in the allowed list can mean the file, or any word that is a term.
    **Change:** `customer_words_allowed_in`: add `"where the word is a term of data/terms.json with kind aws-name or concept"`; remove "landing zone" and "cold start" from `customer_words`.

28. **major. Who makes term, meaning, partner, word and say cards. `terms.schema.json` ("term, meaning and partner flashcards are generated from this file"), CONV J, fixture `cards.json` (a hand-written `partner` card), SPEC `cards.exam_english_cards`, C202.**
    Writers and the Anki export will both produce these cards. The 90 `word` cards have no file: chapter 01 has no `cards.json` (CONV A) and its card counts are 0.
    **Change:** decide and state in CONV J: "`term`, `meaning`, `partner` cards are generated from `data/terms.json`, `word` cards from `data/exam-english.json`, `say` cards from `speak.json`; writers write only `decide`, `differ`, `number`, `cannot`", and adjust `counts.cards`; or the reverse, with `data/01-how-the-exam-asks/cards.json` added to CONV A. Fix the fixture to match.

29. **major. Fact id prefixes collide. CONV F ("The fact id starts with `<service>-`"), SPEC `fact_links.id_must_start_with_file_stem`, M1.**
    `iam-identity-center-...` starts with `iam-`; the same holds for `s3`/`s3-glacier`, `ec2`/`ec2-auto-scaling`, `vpc`/`vpc-endpoints`, `rds`/`rds-proxy`, `eks`, `ecs`, `aurora`. A link `../facts/iam.md#iam-identity-center-x` passes the prefix check.
    **Change:** L301 and M1: "the `service` field of the fact equals the file stem; and a fact id of service X does not start with `<Y>-` for a longer service key Y."

30. **major. No way to ask for another display of an existing fact. CONV F, TOOLS 5.6.**
    Link text must contain a canon string. For "cannot" and behaviour facts the display is a phrase (`only its owner can read it`), which forces grammar and an unclear "it" that STYLE forbids. `facts request` covers only missing facts.
    **Change:** `facts request --fact ID --display "<wanted string>"` (the registrar adds it when M7 passes), and the marker `<!-- needs-display: <fact id> "<string>" -->`. In the brief stage, give each non-numeric fact at least two displays (a noun phrase and a verb phrase).

31. **major. AWS quote blocks: undefined lint treatment, and a CONV example that fails. CONV D12, D13; L202, L306, L802, L901.**
    (a) AWS sentences are often over 30 words, contain former names ("AWS SSO") and banned variants ("server"); only L304 and L801 name quotes as exempt. (b) `normalize_text` keeps punctuation, so the D13 example quote, which ends with a period, is not inside the fixture evidence quote (`...storage servers," said`); the fixture file leaves the period out. (c) "verbatim FAQ quote" (RULINGS) against "verbatim AWS sentence" (CONV): must the page be an FAQ page? (d) The fixture real-world box links a fact in the bold field; the CONV example does not.
    **Change:** CONV D12: "An AWS quote block is exempt from L202, L304, L801, L802, L803 (contractions), L901 and from the sentence average; its words count toward the file." Remove the final period in the D13 example and add: "copy the span exactly, punctuation included; the span can be part of the evidence quote." State: "any saved AWS page; prefer the service FAQ." Add the fact link to the D13 example.

32. **major. The fixture twin pair is decided by a volatile number. Fixture `questions.json` (q001, q002), STYLE section 7, Q112.**
    Both keys depend on `widget-shelf-max-widgets`, changed 2025-11-19, inside the 24-month window, with `volatile: false`. Writers copy the fixture as the model of a twin pair.
    **Change:** move the fixture change date before the window (for example 2023-03-14, with the snapshot and hashes updated), or base q001 and q002 on a stable fact.

33. **major. The STYLE sample question breaks SPEC. STYLE section 7 ("Sample at the required standard"), SPEC `questions.option_words` (15 to 45).**
    Two of the four options have 11 and 13 words ("Move the instances to public subnets and delete the NAT gateway."; "Replace the NAT gateway with a NAT instance on a small instance type.").
    **Change:** lengthen the two options to 15 words or more, or set `option_words.min` to 10 (real exam options are often that short). Then run the sample through `q lint` once the tool exists.

34. **major. Minutes. CONV B (`minutes: {fast: 20, pass: 65, full: 150}`), SPEC `templates.deep.minutes` (`full`: 135), CONV C (H3 `route=pass`).**
    Unclear: is `templates.*.minutes` a rule, a default or a target (the CONV example has 150 against 135)? How is a time box derived from words? How are `pass` and `full` computed? How many subsections get `route=pass`, and by what criterion?
    **Change:** CONV B: "`fast` = sum of the H2 time boxes of `1-fast.md` and equals the template value; `pass` and `full` are written by `sync` from the formula in SPEC" (add `minutes_formula`: reading at 120 words a minute, 1 minute per prompt, 2.5 per question, 3.5 per spoken answer). CONV C: "Mark 2 to 4 subsections `route=pass`: the ones the core questions review."

35. **major. Writer fields against tool fields; `topics`; `bullets`. CONV J, T-items 7.1, schemas.**
    The schema requires `rev`, `keyRev`, `status`, `verification`, `label`, `checked`, which the tool sets; CONV J does not say what a writer puts in the `--file` input. `topics` (at least one, required) has no vocabulary (fixture: `storage`, `security`). `bullets` is empty in every fixture question, but coverage (V01) and the brief slots need it.
    **Change:** CONV J: one line per item type, "Writer supplies: ...; tool sets: ...". Add `questions.topics` (the allowed list) to SPEC. Rule: "a question of pool `chapter` lists at least one bullet of its task" (new Q116), and fill `bullets` in the fixture.

## Majors: pattern, light, front, synthesis, mock

36. **major. Pattern `1-fast.md` reuses roles whose rules do not fit. SPEC `templates.pattern`, `bold_fields`, CONV C.**
    "The question behind it" has role `breath`: does it need `**The problem it solves.**`, Predict the picture and a startup example? "Patterns at a glance" has role `choose` but holds a `matrix` table: does it need `**Deciding question:**`? The columns of both matrix tables are undefined.
    **Change:** give the pattern sections their own roles (`question`, `glance`) or key `bold_fields` by section id; add to `tables.kinds`: `glance` (`Pattern | Problem | Choose when`) and `services` (`Service | <2 to 3 named columns per chapter in chapter_overrides>`). Show one filled pattern fast file in CONV.

37. **major. Pattern cards and the assertion-heading rule. CONV D16, SPEC `templates.pattern...patterns` (role `how`), `headings.assertion_heading_words`.**
    A pattern card is naturally named ("Warm standby"), but role `how` demands a sentence of 5 to 14 words. `**Problem.**` is "in exam English", so it carries scenario numbers and "must" inside a strict role.
    **Change:** CONV D16: "The H3 is the pattern name (1 to 6 words); the assertion rule does not apply" (SPEC: `assertion_headings: false` on that section). CONV F exempt list: add "the `Problem.` field of a pattern card and the `Requirement.` field of an architecture page".

38. **major. Recognise-only services inside deep, medium and pattern chapters have no device. LEARNING 1.4 ("Twenty-four cards sit inside medium chapters"), CONV C ("No other H2 is allowed"), D15.**
    Examples: chapter 09 (7 services), 37 (Managed Grafana, Managed Prometheus), 19 (ECS Anywhere, EKS Distro), 41 (the cost tools), 03 has `sts` (fine). Service cards exist only in `2-services.md` of light chapters.
    **Change:** allow an optional hand file `2-services.md` (role `card`, D15) in the deep, medium and pattern templates, with `registry` naming which service keys are cards (`cards: [...]` in the chapter entry).

39. **major. Light service card: minimum words out of reach, and the `Formerly.` field trips L802. CONV D15, SPEC `light_card`, `lint.former_name_allowed_once_after`.**
    With one sentence for "What it is", 2 to 3 short signals, one fact and a 25-word Say it, a card reaches about 110 to 145 words; the minimum is 150. `**Formerly.** Amazon Old Name.` does not put the name "directly after `formerly `".
    **Change:** `light_card.words.min` 100; L802: "also allowed directly after the bold label `**Formerly.**`".

40. **major. Chapter 01: contradictions and double sources. CONV A ("Worked examples are not prose files"), SPEC `chapter_overrides.01`.**
    `2-deep.md` has a hand section "Worked examples" (role `worked`, 200 to 500 words) while worked examples are question blocks. "Exam English core words" and "The nine word groups" repeat `data/exam-english.json` by hand next to the generated `exam-english.md`, with no table kind and no word syntax.
    **Change:** delete the hand section "Worked examples" (the two `worked` questions print in `5-quiz.md`), or define it as a generated region. Define a table kind `exam-english` (`Word | Meaning | It signals`), filled by a generated region in both sections, with hand text only around it.

41. **major. Chapter 00: `mistakes.md` and Task 0 are undefined. SPEC `chapter_overrides.00`, LEARNING section 3 (cause codes K, C, W, T, D; confidence column) and 7.2 (Task 0, the budget alert).**
    The log table has no kind and no columns, the five cause codes are in no contract file, and the reader edits this file, so lint limits (200 words) will fail later. Task 0 has no chapter (00 has no `tasks.json`).
    **Change:** SPEC: table kind `log` (`Date | Question | Cause | Sure | Fix`), `lint.cause_codes`, and `"reader_editable": true` on `mistakes.md` (lint checks only the first table header). Put Task 0 in chapter 02 (medium template, 1 Try required) and say so.

42. **major. Role `plan` exempts AWS policy facts. SPEC `roles.plan` (example), chapters 00 and 52 ("Logistics", "Gates", "The night before").**
    Retake wait, reschedule limits, result timing and the exam length are hard facts in namespace `exam`, and `plan` needs no links at all.
    **Change:** `plan`: "cells of a `plan` table are example text; paragraphs and lists are heuristic text (a number with a unit needs a fact link, except minutes and percent of her own plan marked `<!-- no-fact: plan -->`)".

43. **major. Synthesis pages have no syntax. SPEC `chapter_overrides.44` and `.45` (`fields` labels), CONV C.**
    The labels `diagram with numbered steps`, `table:breaks`, `If the question adds.`, `diagram of kind ladder`, `table:compare`, `Rule.`, `comment:twins` are a small language that CONV never defines. Unknown: the form of an "If the question adds" item, the `twins` comment, whether the atlas `compare` table still needs `**Deciding question:**` (the kind demands it; the page has `Rule.` instead), and whether `Requirement.` is exempt (see 37).
    **Change:** add CONV D17 (architecture page) and D18 (atlas page) with one filled example each. Proposed: `**If the question adds.**` then a list of `- <added phrase>: <change>`; `<!-- twins: <question id> <question id> -->` after `**Rule.**`; in role `atlas` the `compare` table is followed by `**Rule.**` (SPEC `followed_by` per role).

44. **major. Chapters 46 and 47 collide with the roles they reuse. SPEC `chapter_overrides.46` ("Top traps", role `signals`, `traps_must_exist_in_chapters`), `.47` ("A-list", role `numbers`), `headings.fixed_h3`, L604.**
    Copying 30 to 40 trap ids into chapter 46 makes each id appear twice in hand files ("used twice" in L604; `lint.traps()` maps one id to one chapter). Role `signals` implies a signals table and `### Traps`; role `numbers` implies `### A-list` and `### B-list` under an H2 that is itself named "A-list".
    **Change:** in 46 cite with `<!-- trap-ref: <id> -->` (L604 ignores it; a new check resolves it). Apply `fixed_h3` by section id, not by role, and state that the 46 and 47 sections hold one list and one table with no H3.

45. **major. `section` cannot point to another chapter. Schemas (`'<file>#<section id>'`), Q111, chapters 40 to 45, 50, 51, drills.**
    Mock, pattern, atlas and architecture questions review a section of a service chapter. The format is chapter-relative, so the field must be null and the review link (STYLE section 7, item 6) is lost.
    **Change:** allow `"<NN-slug>/<file>#<section id>"`; `lint.sections` resolves it; T-items 6.2 prints `../<NN-slug>/<file>#<anchor>`.

## Minors

46. **minor. Numbers that are in CONV but not in SPEC (CONV says SPEC holds every number).** The 25-word limit of the one-breath `Say it` (only `light_card` has it); "at most two sentences" and the two-sentence `Say it` of D13; "5 to 14 words" is present, "one sentence" for Look first is not. **Change:** add `say_it_words_max: 25` to the `breath` sections, `realworld.sentences_max: 2`, `look.sentences_max`.

47. **minor. Fixture against CONV in small things.** Look first has two sentences (CONV C: "one sentence"). Predict has an unlabelled intro line that promises answers in Check, but Check asks new cases, so a Predict question is never answered. The words table bolds the term in row 3 ("an **idempotent** request"), not the partner. `2-deep.md` defines "**Regional**" in bold, which is not in the fixture term bank. **Change:** fix the fixture or the rule; add to D1: "the Check reveal also answers the matching Predict question in one sentence."

48. **minor. Words table details. CONV D3.** The respelling sits inside the term in the example (`CIDR (SY-der) block`) and after it in the fixture; the match to `terms.json` is undefined. Unclear whether "Plain meaning", the collocation and "Do not confuse with" are copied from the bank or free. **Change:** "Cell 1 is `<term>` or `<term> (<respelling>)`; lint strips one parenthesis group anywhere in the cell. Cell 2 is one of the term's `collocations` with the partner word in bold. Cells 3 and 4 are free and must not contradict the bank."

49. **minor. Where a term is "defined" in `1-fast.md`. STYLE section 2 (five steps), W901.** The fast file has no prose for the five steps. **Change:** "In `1-fast.md` the words table is the definition. The five steps apply at first use in `2-deep.md`."

50. **minor. Abbreviations. STYLE section 2, W802, seed title "IAM".** The H1 of chapter 03 is itself an abbreviation, and no list says which short forms need spelling out (IAM, STS, MFA, ARN, S3, EC2). **Change:** "Short forms are the `short` values of the bank; official service names (`kind: aws-name`) and the H1 are exempt."

51. **minor. Changed recently entry. CONV D6.** Five `>` lines render as one run-on paragraph in VS Code and GitHub (no hard breaks). The entry date is not tied to `changed.date` of the fact. No form for a new feature with no old value. **Change:** end each line with two spaces or `<br>` (allowed tag); lint: date equals `changed.date` of the fact linked in `Now:`; "for a new feature write `**Old:** not available.`".

52. **minor. Word lint noise. SPEC `lint.warn_words` and `banned_words`.** "as" warns on nearly every paragraph ("such as", "the same as"); "may" also matches the month in "May 2025"; "over" matches "fail over" contexts and "over time". **Change:** drop "as" or match only sentence-initial `As `; exempt `May` followed by a year; keep `over` only before a digit.

53. **minor. Question rules that need one sentence each.** STYLE says five options for multiple response; SPEC also allows six with "(Select THREE.)". A question with `qualifier: "none"` at difficulty 2 or 3 cannot have a `violates-qualifier` option (Q108): say "`none` only at difficulty 1". Should `keywords` include the qualifier (fixture and sample do)? The correct option's `why` is never printed for a single-answer question: say what it is for. `sources`, `volatile` and core against extended have no writer rule. **Change:** add the sentences to STYLE section 7 and CONV J ("`sources`: leave empty, `sync` derives sources from facts"; "`volatile`: set by `q add` from `facts.is_volatile`"; "core = one question per must-know bullet at difficulty 1 or 2").

54. **minor. Speak and card details.** With a compare prompt, does "Both ..." replace "The short answer is" or follow it (P103)? Who sets `pack: true` (30 in total, 24 from chapters, but there are 15 deep service chapters)? A `say` card back is "the 10-second answer and the skeleton" within 25 words, which cannot fit. Card `tags` have no documented format (fixture: `saa::ch::sample`, `saa::d2`). **Change:** "Both ... replaces starter 1"; "the orchestrator sets `pack`; writers set false"; "`say` card: back = `ten_second`, `extra` = skeleton"; "writers leave `tags` empty; the export derives tags from fields".

55. **minor. Task details.** `title` becomes an H2 in `3-do.md` but has no character rule (a colon breaks the anchor rule). `pass_route` count per chapter is unstated. `kills` "in quotes" is only in the schema description. Unstated whether every Try needs a `Try it` callout (and those count toward 12). **Change:** schema pattern for `title` equal to the heading regex; "exactly one Try has `pass_route: true`"; "every Try and Lab has one `Try it` callout at its `section`".

56. **minor. Callout and diagram counts. SPEC `callouts_max`.** In a deep fast file, `Say it` + `Startup example` + up to 4 `Changed recently` already use all 6. In `2-deep.md`, 12 callouts are fewer than 14 subsections, so `Key fact` cannot be one per subsection. No template says how many diagrams a chapter has beyond the hero. **Change:** do not count `Changed recently` entries toward `callouts_max`; state "`Key fact` is optional"; add `counts.diagrams: {min, max}` per template.

57. **minor. Rules a writer cannot know from the three files.** `normalize_text` is case-insensitive and keeps punctuation (matters for link text and quotes): say so in CONV F. Number words ("twelve hours") escape L304: state "facts use digits; small story counts use words". One link satisfies a sentence with two hard facts: state "each hard fact is its own link". A JSON item that waits for a missing fact has no marker: "do not add it; list it in the result as `parked`". Bold-led paragraphs: only the labels in `prompts.labels` are example blocks; bold fields are strict in strict roles (labels end in `.` or `:` as listed in `bold_fields`). `Amazon SageMaker` (without AI) is missing from `lint.former_names`.

58. **minor. Smaller structure points.** Markdown anchors include the time box, so retiming a section breaks links from other chapters: add `lint --fix-anchors` or let `sync` rewrite them. `section_flag.regex` does not match the H3 form `<!-- section: route=pass -->`: add `h3_regex`. `resolution.template` says overrides are "merged": state that `files` is replaced as a whole and `counts` is merged per key. `### B-list` with 0 rows: state "leave the H3 out". "A-list numbers become Number flashcards": state whether every A-list row needs a `number` card. An exempt role can still state a real AWS "cannot" (fixture Decision record: "one shelf cannot hold 600 widgets"): add a writer rule "link AWS facts in example sections too; lint does not require it".
