# TOOLS, part 3: gates, shared functions, matching rules, counts, item status (version 1.0; contract fix 1 and the 1.0 freeze, section R11)

This file is part of `TOOLS.md` and has the same authority. It was written after the two contract reviews (`_build/reports/contract-critique-*.md`); `_build/reports/contract-fix.md` lists what changed. Where this file and an older sentence of `TOOLS.md` or `TOOLS-items.md` differ, this file is right and the other file has an error: report it.

Numbers written here illustrate the `SPEC.json` key named beside them.

## R1. Gates: one table, one signature

Every gate function has the signature `gate_<x>(ch_id, quick=False, **options) -> dict`. `quick=True` asks for the fast form: the function can skip checks that read the corpus. Modules import each other inside functions (`lint` reads the items for L903; `qbank` and `lab` call `lint.sections`), never at module level.

| Gate | Function | Called by the ledger as | Passes when |
|---|---|---|---|
| `plan`, `brief`, `findings`, `findings-closed`, `diagrams`, `counts` | `ledger.gate_plan`, `gate_brief`, `gate_findings`, `gate_findings_closed`, `gate_diagrams`, `gate_counts` | `gate_x(ch)` | `TOOLS.md` 3.1 |
| `facts-mech` | `facts.gate_mech` | `gate_mech(ch)` | the blocking mechanical checks pass on every fact of the chapter that is not rejected or superseded; a chapter with services has at least one fact (F01) |
| `facts-final` | `facts.gate_final` | `gate_final(ch)` | every fact of the chapter (not rejected, not superseded), and every fact that the chapter's hand files and items link or list, is `verified` (F02); none is in an open conflict (F03); every `verified` status is backed by the vote log (F04); the mechanical checks still pass (M codes; skipped with `quick=True`) |
| `lint` | `lint.gate_lint` | `gate_lint(ch, draft=True)` in stage `prose`; `gate_lint(ch)` elsewhere | no blocking finding of `TOOLS.md` 6.1 |
| `sync` | `lint.gate_sync` | `gate_sync(ch)` | `sync CH --check` is clean |
| `questions` | `qbank.gate_questions` | `gate_questions(ch)` | item rules; chapter rules without `--ship` |
| `questions-verified` | `qbank.gate_questions_verified` | `gate_questions_verified(ch)` | the same with `--ship`, plus Q206 |
| `cards` | `qbank.gate_cards` | `gate_cards(ch)` | item rules; chapter rules without `--ship` |
| `speak` | `qbank.gate_speak` | `gate_speak(ch)` | item rules; chapter rules without `--ship` |
| `tasks` | `lab.gate_tasks` | `gate_tasks(ch)` | item rules; chapter rules without `--ship` |

Only the `counts` gate uses the `--ship` forms (Q201, C201, C204, P201, T201, T113): it calls `qbank.gate_questions_verified(ch)`, `qbank.gate_cards(ch, ship=True)`, `qbank.gate_speak(ch, ship=True)` and `lab.gate_tasks(ch, ship=True)`.

**"The facts of a chapter"** are the facts whose `home_chapter` is the chapter. `facts batch --chapter`, `facts finalize --chapter` and `gate_mech` use that set. `gate_final` adds the facts of other chapters that this chapter links (a VPC chapter links `ec2-` facts).

**Shared functions in `lint`** (no other module has its own copy):

- `lint.template(ch)`: the resolved template, by `SPEC.json` `resolution.template`: the tier or kind template; an override with `template` replaces it; then the override merges on top (objects key by key, recursively; arrays and scalars replaced). Keys: `key` (the template name), `files`, `counts`, `minutes`.
- `lint.word_count(text)`: `resolution.word_count`; raw HTML tags (`details`, `summary`, `br`) are not words, and four or more words joined by hyphens, slashes or underscores count as their parts.
- `lint.holds_display(text, display)`: the number-boundary comparison of `fact_links.comparison`; every module uses it (L303, C104, C109, P109, M7, the audit re-derivation). `lint.link_text_extra(text, displays)`: what a link text holds beside the displays (L303).
- `lint.anchor(heading)`: the Markdown anchor of a full heading text. `lint.section_id(heading)`: the same without the time box.
- `lint.sections(ch)`, `lint.traps()`, `lint.a_list_facts(ch)`, `lint.check_strict_text(text, where, stem=None)`: `TOOLS.md` section 2.

## R2. Matching rules of the chapter lint

These rules make L304 and its neighbours give the same result in every implementation.

**Number with a unit** (`lint.number_with_unit`). The number regex (also with a `+`), then an optional space or hyphen, then a unit (case-sensitive) or a count noun (case-insensitive), then no further letter. `5 GB`, `5GB`, `10-second` and `9000+ widgets` match, and so does a number with one or two plain words before the unit (`5 read replicas`, `7 full hours`). A currency amount always matches. Not counted as a number: heading time boxes; list and step numbers; dates (`YYYY-MM-DD`, `YYYY-MM`, a month name with a year); prompt numbers; digits inside a name (`S3`, `EC2`, `Route 53`: a number that is part of, or directly follows, a `term` or `short` of `data/terms.json` or an official service name). A number word from `zero` to `twelve` on its own is not matched; a larger or compound number word before a unit or a count noun (`nineteen hours`, `nine hundred widgets`) is. The text is NFKC-normalised, entities are decoded and zero-width characters are removed before matching.

**Absolute word** (`lint.absolute_words`, `absolute_word_match`, plus the fixed spellings and synonyms of `lint.EXTRA_ABSOLUTE`: `can not`, `no more than`, `not more than`, `at least`, `not possible`, `impossible`, `does not support`, `do not support`, `unsupported`, `exclusively`, `invariably`, `no one`, `nobody`, `unlimited`, `limited to`, `a maximum of`, `a minimum of`, `under no circumstances`, `at all times`). Case-insensitive; not preceded and not followed by a letter, a digit or a hyphen. `Only` matches; `read-only` and `must-have` do not.

**What L304 never reads** (`grounding.skips`): heading lines, image alt text, bold labels, AWS quote blocks, fenced code, and inline code that is a command or a name (inline code that reads as prose, `up to 9000 widgets`, is read). A sentence that ends with `?` is read only for a number with a unit. `<summary>` lines are read.

**Exemptions of L304**, in this order:

1. the section's role has grounding `example` (no check) or `heuristic` (only L305);
2. a prompt paragraph, and every other entry of `grounding.example_blocks`;
3. a callout whose label has grounding `example` or `heuristic`;
4. the text between `**Wrong belief:**` and `**Truth:**`;
5. the example and heuristic columns of a signals table (columns 0, 1 and 3);
6. the line that starts `**The exam probably expects:**`;
7. a sentence in `grounding.exempt_sentences`;
8. a sentence or cell that ends with `<!-- no-fact: <reason> -->` with a reason of `grounding.no_fact_reasons`. Each use is reported as W308, so that the claims reviewer sees the list.

Text inside a reveal is strict. One fact link satisfies L304 for the absolute words of its sentence or cell; a number with a unit that stands outside the link text still needs a link of its own (L304). The rest of the rule "each hard fact is its own link" is checked by the claims reviewer.

**L305 (heuristic text).** A number with a unit needs a fact link. Exception: the unit is in `grounding.heuristic_exempt_units` and the sentence holds no word of `grounding.exam_fact_words` (case-insensitive). The cells of a `plan` or `log` table are example blocks.

**L308 (headings).** An H2 or H3 heading that has a number with a unit or an absolute word, in a section whose role is strict, needs at least one fact link in the body of its own section or subsection (`headings.grounding`).

**L705 (diagrams).** The caption and the step sentences of a diagram embed are strict text under L304. When the spec exists, L702 and L703 compare alt, caption and steps with the spec `alt`, `claim` and `say`: both sides after links are replaced by their text and after `common.normalize_text`. L705: a spec `claim` or `say` that has a number with a unit or an absolute word while the equal Markdown sentence has no fact link. The check of node labels belongs to the diagram module (asked of its owner: a label with a number with a unit must repeat a value that stands in `claim` or `say`).

**Prompts, bold fields, labels** (`prompts.syntax`). A prompt is a paragraph whose bold label is a key of `prompts.labels` (`<n>` = digits). A bold field is a paragraph whose label is in `bold_fields` or in a `fields` or `subsection_fields` list of the template. L107 reports an unknown prompt label only for a bold label that ends with a period and has the form of a prompt label of another role; any other bold start is plain text. In role `realworld` the first paragraph matches `bold_fields.realworld_first_paragraph_regex`.

**Callouts.** The label is the bold text at the start of the first line of the blockquote. Later lines (`> **Old:**`) are not labels. A `Changed recently` entry: each of its first four lines ends with `<br>` (L107); its date equals `changed.date` of the fact linked in `Now:` (L107); a date after `book.exam_eligibility_cutoff` requires `Status: not examinable yet` (L107). `Old:` can be the fixed text `not available.` without a link.

**AWS quote block** (`fact_links.aws_quote`). Take the first line, strip `> ` and the first and last straight double quote, then `common.find_quote(span, evidence quote)`; the span holds whole sentences of the evidence quote (it starts at a sentence start and ends at a sentence end, or at the end of quoted speech), or is a table row (L306). The block is exempt from the sentence limits and average, L304, L801, L802, the contraction rule and L901. Its words count toward the file.

**Words.** Banned words, warn words, customer words and banned term variants match with `lint.word_match`. `may` matches in lowercase only. `over` warns only before a digit. A contraction is a match of `lint.contraction_regex`; a possessive is not a contraction. L801 does not fire on a customer word inside one of `customer_words_allowed_in`. L901: `lint.banned_term_match`.

**Terms.** W901 and W202: `lint.term_rules`. W802: a `short` value used before its full term in the file; official service names (kind `aws-name`) and the H1 are exempt. L503 for `words`: `devices.words_table`.

## R3. Counts, new codes, tests

**Count keys of L106.** A key with `{}` counts nothing. A count is checked in the section (or file) that names it.

| Key | What is counted |
|---|---|
| `prompts` | prompt paragraphs of the section's own label (`Predict <n>.` in `predict`, `Check <n>.`, `Recap <n>.`), numbered from 1 without a gap |
| `gist_traps` | `<!-- gist-trap -->` markers on Predict prompts |
| `task_regions` | `task:start` regions |
| `plan_regions`, `exam_english_regions_per_subsection` | regions of that kind (in the section; in each H3) |
| `say_it` | `Say it` callouts |
| `startup_examples` | `Startup example` callouts |
| `hero_diagrams` | embeds of the diagram `<slug>-hero` |
| `hero_steps` | items of the ordered list after the hero caption |
| `rows`, `signal_rows`, `pairs_rows`, `matrix_rows`, `glance_rows`, `services_rows`, `plan_rows` | body rows of all tables of that kind in the section (`rows`: the `words` table; `plan_rows`: the rows that `sync` will generate from `data/plan.json`) |
| `a_list_rows`, `b_list_rows` | body rows of the `numbers` tables under `### A-list` and `### B-list`; in a section without those H3 (chapter 47), all `numbers` rows count as A-list rows |
| `compare_tables` | tables of kind `compare` |
| `log_tables` | tables of kind `log` |
| `traps` | list items with a `<!-- trap: id -->` comment |
| `trap_refs` | list items with a `<!-- trap-ref: id -->` comment |
| `entries` | `Changed recently` callouts; 0 entries requires the exempt sentence |
| `items` | `FAQ <n>.` prompts |
| `quotes` | AWS quote blocks |
| `options` | list items after `**Options.**` |
| `cause_codes` | the codes of `lint.cause_codes` that the section names in bold |
| `subsections` | H3 headings of the section |
| `stop_and_answer_per_subsection` | `Stop and answer.` prompts in each H3; the prompt and its reveal are the last blocks of the subsection |
| `say_it_per_subsection` (1.0, not implemented yet: R11) | `Say it` callouts in each H3; the callout is the block directly before the `Stop and answer.` prompt, starts with `The short answer is` and holds `The thing to watch is` |
| `exam_signal_per_subsection` (1.0, not implemented yet: R11) | `Exam signal` plus `Exam heuristic` callouts in each H3 |
| `subsection_words` | W201, not L106: `devices.subsection_words_count` |
| `spot_the_bug`, `go_deeper` (file level) | `Spot the bug.` prompts; `Go deeper:` reveals |
| `diagrams` (template `counts`) | diagram embeds in the hand files of the chapter (L106) |

L106 also checks: fixed H3 names by section key (`headings.fixed_h3_keyed_by`; `B-list` is optional); assertion heading length where `headings.assertion_headings_apply_to` says so, or `subsection_heading_words` where the section has `assertion_headings: false`; the number of H3 marked `route=pass` (`section_flag.h3_pass_route_subsections`); `sentences_max` and `list_items` of fields; the sentence limits of `devices`.

**Codes added by contract fix 1**

| Code | Rule | Keys |
|---|---|---|
| L108 | Two headings of the chapter's hand files have the same section id | `headings.unique_section_ids` |
| L308 | A heading with a hard-fact word and no fact link in its body | `headings.grounding` |
| L705 | A grounded diagram text without a fact link (R2) | `diagram_embed.grounding` |
| L905 | Without `--draft`: a trap id or a section of `brief.json` that is in no hand file | R4 |
| W105 | Front matter `minutes.pass` or `minutes.full` differs from the formula by more than the tolerance | `lint.minutes_formula` |
| W307 | Also: a `needs-display` or `needs-term` marker in a `draft` file | `fact_links.marker_severity` |
| W308 | A `no-fact` marker (one finding per use); an unknown reason is L304 | `grounding.no_fact_*` |
| W601 | An `xref` marker; an error with `lint --all --strict` | `links.xref_rule` |
| W903 | A number in a `Startup example` callout or a Decision record that is not in the `uses_numbers` of the chapter in `data/startup.json` (skipped when the file or the entry is missing) | `startup.data` |

**Codes added by the gate-break fixes (2026-10-05) and the W0 follow-ups (2026-10-09)**

| Code | Rule | Where |
|---|---|---|
| F04 | A `verified` fact whose status the vote log does not produce (set by hand): `facts verify`, `gate_final` | `TOOLS.md` 5.3, 5.4 |
| Q207 | A second `q add --replace` in round 1 (`verification.edits`) | `TOOLS-items.md` 7.1, R5 |
| Q302 | Also at `q add`: a near-duplicate of a live question or a copy of a rejected one (`qbank.similarity`) | `TOOLS-items.md` 7.1, 7.5 |
| Q401 | A blind pack item holds more than `id`, `type`, `select`, `stem`, `options` (`q pack`) | `TOOLS-items.md` 7.3 |
| D04 | An SVG file that is not the output of its spec (`diagrams` gate) | `TOOLS.md` 3.1 |
| X03 | A gate's module or function is missing: check unavailable, exit 3, no record | `TOOLS.md` 3.3 |

Rules changed in place: L301, L306, L307, L402, L502, L503, L601, L604, L701 to L704, L801, L802, L901, W901, W902 (`TOOLS.md` 6.1). In draft mode, also (d): the missing SVG of L701 and L704, the `words` term check of L503, and L601 for a file of a chapter that is not drafted yet. A file with `reader_editable: true` and status `ready` is checked only for front matter, H2 headings and table headers. L904 searches the whole file, generated regions included.

**Must-fail tests of the chapter lint** (each changes one thing in a sandbox copy): link text without the value (L303); a fact set to `disputed` (L302); `Each shelf always keeps 3 copies.` added to "How it works" (L304); a number with a unit in an `Exam heuristic` callout (L305); an unknown callout label (L401); a missing required section (L104); flag minutes that differ from the heading (L105); a 5-column table in `1-fast.md` (L502); a bare URL (L602); `leverage` (L801); `QuickSight` (L802); an AWS quote changed by one word (L306); a link to a missing anchor (L601); the fast file padded over its word limit (L201); a Predict prompt without `?` (L107). Added: the heading `A shelf always stays in one Region (3 min)` over a body without a fact link (L308); a second H3 with the text of an existing one (L108); `box` in an alt text (L901); the `<br>` removed from a Changed recently line (L107); `must` added after the quoted phrase of the `Exam signal` callout (L304). Must pass: `read-only` in strict text; a sentence with `must` that ends with `<!-- no-fact: requirement -->` (W308 only); `The team studies 20 minutes a day.` in a `method` section.

## R4. The brief is the shared plan of the parallel stages

`brief.json` fixes, before stages 6 to 11 start: the trap ids with belief and truth (`traps`), the H3 heading texts of "How it works" and the section of every bullet (`sections`), the question slots with `layer` and `exam_english`, the terms, and the text of every diagram (`diagrams`).

- `lint.sections(ch)` returns the sections of the hand files. For a file that does not exist yet, or a brief section that the file does not have yet, it adds the brief section with `planned: true`. `lint.traps()` does the same for brief traps.
- The item rules Q109, Q111, C108, P108 and T111 accept a planned section or trap.
- From the `edit` stage on (`lint` without `--draft`), L905 reports every brief trap and brief section that is missing from the hand files. A writer who needs another heading or trap id reports it; the orchestrator changes the brief.

## R5. Item status, `--replace`, generated cards

**`q|cards|speak|tasks set-status --chapter CH --status ready|verified|retired|rejected ID ... [--by L] [--reason TEXT]`.** Under the lock of the data file. `ready` is allowed only when the item passes its item rules; for a question also Q206 (`verification.status` is `pass` or `edited-pass`). `retired` and `rejected` need `--reason`. JSON `{"set": [ids], "refused": [{"id", "errors": [findings]}]}`; exit 1 if any was refused. `q adjudicate --select` and `mocks assemble` keep setting question status themselves. A reviewer sets cards, speak items and tasks to `ready` in the stage of that kind, after the item lint is clean.

**`--replace` (all four kinds).** The id must exist.

| State of the stored item | Effect |
|---|---|
| not verified yet (questions: `verification.round` 0 and no solvers; other kinds: status `candidate`) | replaced in place; `rev` stays; status `candidate` |
| question with `verification.round` 1 and status not `rejected` | the one edit: `rev` + 1, `round` stays 1, `solvers` cleared, status `candidate`, `verification.edits` 1; a second `--replace` in round 1 is refused (Q207) |
| question with `verification.status` `pass` or `edited-pass`, or a `ready` card, speak item or task | `rev` + 1; status `candidate`; a question also gets `verification` = `{"status": "candidate", "round": 0, "solvers": []}`, so it is verified again; `ledger.mark_stale` with the item stage |
| `rejected` or `retired` | refused, exit 1 |

**`cards build [--only terms|words|say]`.** Writes the generated cards (`SPEC.json` `cards.generated_*`), each with `generated: true`, `status: ready`, `section: null`: one `term` and one `meaning` card per term and one `partner` card per collocation into `data/cards-terms.json` (chapter `glossary`); one `word` card per exam-English word into `data/01-how-the-exam-asks/cards.json` (front = `stem` with the word replaced by `___`, back = the word, `extra` = `meaning` and `signals`; deck `exam-english`); one `say` card per speak item with `pack: true` into `data/49-speaking-pack/cards.json` (front = `prompt`, back = `ten_second`, `extra` = the cues joined with ` / `). Ids are stable: an existing card of the same `term`, `word` or `speak` reference keeps its id. Deterministic; `cards build --check` compares without writing (exit 1 when stale). `cards add` refuses the generated types (C110). When the expected count is 0 the file can be absent.

**`q words [--need]`.** Lists each exam-English word with the number of non-rejected stems that use it; `--need` lists only the words below `exam_english_word_min_stems`.

**`speak set-pack --chapter CH ID ... [--off]`.** Sets `pack` (orchestrator). P202 checks the total.

**Registry.** `registry set CH --cards KEY,KEY` sets the `cards` list of a chapter (service keys of the chapter that are recognise-only). `lint` then requires `2-services.md` with one card per key (L101, L104), and `registry check` reports a `cards` key that is not a service of the chapter (R02). The patch of `registry set CH --file PATCH` also takes `cards` and `notes` (`TOOLS.md` 4.2).

## R6. Tasks: notes for `lab`

- `tasks emulate` keeps a variable table: after a capture step it stores the value that `--query <query> --output text` returns and substitutes `$NAME` in later commands. Placeholders (`<NAME>`) make a task `not-supported` for emulation.
- T106 and T107 read the operation as the third word of an `aws` command. `curl` and `dig` commands are never create commands.
- The versions `awscli==1.46.1` and `moto[server]==5.2.3` in `TOOLS-items.md` 8.2 and 8.3 were written from memory. The implementer of `lab` confirms that they exist (one `uv run --script` of the helper) before pinning, and pins the versions that resolve.
- The tag syntaxes in `tasks.tag_patterns` were also written from memory. `tasks check-cli --reference` is the check before a task ships.
- T108 by-name verify (2026-10-12). Some resources no tag filter finds: the Resource Groups Tagging API does not list IAM roles (fact `iam-tagging-api-getresources-no-iam-roles`), and many `describe-*` calls take no tag filter. A Try or Lab verify without a tag filter passes T108 when it is a read-only `aws` command (`READ_VERBS`: `get-`, `describe-`, `list-`, ...), names by `--*-name`, `--bucket` or `--*-identifier` a resource that a create step of the task makes, by a name that obeys the T106 name rule (`name_prefix` `saa-`, or the path `/saa/`; `put-*` steps and capture variables do not count), and has a non-empty `expect` (for example `aws iam get-role --role-name saa-iam-t02`, expect NoSuchEntity after cleanup).

## R7. Decisions

Decisions 1 to 11 were section 10 of `TOOLS.md`.

1. Facts are in `data/facts/`; votes, requests, conflicts and batches are build state in `_build/facts/`.
2. `evidence.sha256` is the hash of the snapshot `.txt` (the text the quote is matched against), not of the raw bytes.
3. The parsed exam guide lives in `_build/registry/` (it is rebuilt from the corpus); the registry itself is `data/book.json`.
4. There is no token renderer and no `render` stage: `facts render` and `sync` generate Markdown, and `facts amend` rewrites link texts.
5. A stage is skipped by an `inputs_hash` over the registry entry, the SPEC version and the pass counters of its prerequisites. File-level staleness is detected by the gate records.
6. A failed question gets one edit and then all three lenses again (RULINGS), not two (PIPELINE).
7. Each mock draws from its own pool file, so question ids keep the chapter slug and nothing is copied.
8. Bullet coverage by mock questions is reported, not required; task statement coverage per mock is required.
9. Superseded on 2026-10-05 (gate-break fix H1; RULINGS 2026-10-09): every fact needs an entail vote, hard or not. Re-derivation runs only on audit samples.
10. The chapter lint covers hand-written Markdown; the item lints cover JSON and share `lint.check_strict_text`.
11. Mechanical quote checks do not recompute `source_id` from the URL; they compare the `url` in the snapshot meta.
12. The template resolver and the helpers `word_count`, `anchor` and `section_id` live in `lint`, because `common.py` is closed for edits. If the owner of `common.py` agrees, they can move there without a change of behaviour.
13. `verify-questions` is a prerequisite of `review`; the item stages stay parallel to `prose` through the brief (R4).
14. Front matter `status` is written by `stage end`, so that no hand edit after `fix` makes the gate records stale.
15. `diagram.schema.json` uses `oneOf`, which is outside `data_files.schema_keywords_used`; it is validated by the diagram module only, not by `saalib.schemas`.
16. The diagram spec gets no `facts` key (one review asked for it): the Markdown caption and steps equal the spec text and carry the fact links (R2, L705), so the diagram schema and renderer stay unchanged.
17. `create-user` stays banned in tasks (STYLE section 8 rule 1). RULINGS rule 9 does not name it; the orchestrator is asked to confirm.

## R8. Facts: the mechanical checks and the vote rules

Moved here from `TOOLS.md` 5.2 on 2026-10-09, with the gate-break fixes of 2026-10-05 (`_build/reports/gate-break-fixes.md`) and the W0 follow-ups (`w0c-tool-fixes.md`). `facts.mech_check(fact)` runs M1 to M13; all block except M12.

- **M1** Valid against `fact.schema.json`. `id` starts with `<service>-` and is unique in the whole canon; it does not start with `<Y>-` for another service key or namespace Y that is longer than `service`. `service` is a chapter service key or a key of `book.fact_namespaces`; `home_chapter` is that chapter.
- **M2** For each evidence item: the URL host is in `common.ALLOWED_HOSTS`; `corpus.load_text(source_id)` exists; the `url` in the snapshot meta equals `evidence.url`; the SHA-256 of the snapshot `.txt` equals `evidence.sha256`. (`add` and `adopt` fill `sha256`, `title` and `match`; a later mismatch is `M2 snapshot-changed`.) The snapshot was made by `saa.py fetch`: the meta file has `sha256` and `text_sha256`, the `.txt` has the hash `text_sha256`, the `.raw` body exists with the hash `sha256`, and `fetch.log.jsonl` names the source id. A snapshot with `fixture: true` counts only in a sandbox book, never in the real book.
- **M3** `common.find_quote(quote, text)` finds the quote; `match` is stored. The quote stands literally on the page: a quote that holds a tag, a link target, a list or heading prefix, a zero-width character or a line break that is not in the snapshot text fails, even when `find_quote` would match it.
- **M4** The quote has 8 to 80 words, or 4 to 7 words when it is one complete sentence of the snapshot (it starts after a sentence end or a line start and ends with `.`), or is a table row (it starts with `|`). A quote of 8 words or more starts at a sentence start and ends at a sentence end of the snapshot (or at a line start or end); a quote that cannot be placed on whole lines of the snapshot (for example one that crosses a multi-line Markdown link) fails, and so does free text taken from a table, which is quoted as one row. A table row needs a `table_header` that `find_quote` finds in the same snapshot, that has the same number of cells, and that is the header row of the table that holds the row. An evidence item with `heading` (2026-10-11, `_build/reports/w0c-heading-evidence.md`) is a heading-scoped quote, for a value stated as a heading and a short value line (`### Exam duration`, then `130 minutes`): the 8-word minimum and the complete-sentence rule do not apply; instead the quote is one whole line of the snapshot (line start to line end after `normalize_text`, a `text` line of `ctx.layout`, not a heading or a table row) with 1 to 80 words, `heading` is the text of a heading line of the snapshot and the nearest heading above that line, the line is within the next 5 non-empty lines after the heading, and `table_header` is empty. Every other check (M2, M3, M5, M8 and the rest) applies to the quote unchanged. A failed condition is an M4 finding that says what to do.
- **M5** Every number in `claim`, in each `display` and in `changed.was` appears in a quote or `table_header` of the fact. Numbers are compared by value: thousands separators are removed; `50 thousand` and `50K` are 50000; a number word from `zero` to `twelve` in a quote counts as its digit (in the claim only before a unit or a count noun); a larger or compound number word (`nineteen`, `nine hundred`) counts everywhere. Not counted as a number: digits inside a name, by the list of R2 (`S3`, `EC2`, `Route 53`). A date in the claim equals `changed.date` or stands in a quote. A number that is followed, directly or after one or two plain words (`7 full hours`), by a unit from `lint.number_with_unit.units` must be followed by the same unit in a quote, or stand in a table row whose row or header holds that unit; the check runs on the claim, the displays and `changed.was`. Singular and plural of one unit, `percent` and `%`, `millisecond(s)` and `ms` are one unit; otherwise the unit is case-sensitive (`TB` is not `TiB`). A number that fails is allowed only when `derivation` is a non-empty string; the fact then needs a `derive` vote.
- **M6** `kind` `limit`, `quota` or `default`: `qualifiers.scope` and `default_or_max` are not empty.
- **M7** Every `display` is, after `normalize_text`, held by the normalised `claim` or by a normalised quote, where "held" is the `holds_display` comparison of `SPEC.json` `fact_links.comparison` (a display that starts or ends with a digit must not touch another digit of a longer number: `2 500 widgets` does not hold `500 widgets`). Displays are unique in the fact. A display without a digit has at most `fact_links.number_free_display_words_max` words (RULINGS 2026-10-11); registrars enforce this at merge, and the check is not in M7 yet (R11).
- **M8** The quote is not page furniture: its normalised text holds none of the phrases in the constant `BOILERPLATE` (`javascript is disabled`, `thanks for letting us know`, `did this page help you`, `cookie preferences`, `all rights reserved`, `next topic`, `previous topic`, `skip to main content`, `sign in to the console`, `site terms`, `create an aws account`, `contact us`, `feedback preferences`, `privacy site terms`, `document conventions`), it does not run across a heading, and it is not a single heading line.
- **M9** `changed` is set: `was_evidence` is an index into `evidence` and `volatility` is not `stable`. `changed` is null: `volatility` is not `changed-since-2022`.
- **M10** Tiers: `source_tier` is 4 if and only if `kind` is `case-study`. Evidence item 0 (current truth) is not a What's New post (URL path under `/about-aws/whats-new/`) unless `kind` is `change`.
- **M11** `hard` must be true when `kind` is one of `limit`, `quota`, `default`, `restriction`, `price`, `sla`, `change`, `exam-policy`, or when the claim holds a number with a unit or an absolute word (`lint.absolute_words`); it can also be true otherwise.
- **M13** A fact with `hard` true has a non-empty `question`.
- **M12** Conflict scan (a queue, never a rejection of the input): another non-rejected fact of the same service whose claim has a token Jaccard similarity of 0.6 or more and a different set of numbers. Tokens are the lowercase `[a-z]+` words of the claim after every token that holds a digit is removed. Each pair is appended once to `conflicts.jsonl` as `{"id": "cf-0001", "facts": [a, b], "status": "open", "created"}`. A fact in an open conflict cannot become `verified`.

**F04 (hand-edited status).** A `verified` fact whose required lenses have no positive counting vote in the vote log at its current `rev` fails `gate_final`, and `facts verify` sets it back to `candidate` with `stale: status-not-backed-by-votes`. `gate_final` also re-runs M1 to M13 on verified facts (skipped with `quick=True`); `facts finalize` re-runs them before it sets `verified`, and a failure goes to `candidate`, pending `mech`.

**Votes.** `facts vote` stores `content` = `facts.content_hash(fact)`: the SHA-256 of `claim`, `kind`, `hard`, `values`, `qualifiers`, `changed`, `change_items`, `derivation`, `volatility` and the `source_id`, `url`, `quote` and `table_header` of each evidence item (and its `heading` when that is set, so the hash of a fact without one is unchanged). A vote counts only while the fact has that hash and that `rev`. Voter labels are compared without case, spaces and punctuation (`Miner-A`, `miner_a` and `miner a` are one voter). The author and every label in `amended_by` cannot vote on the fact (`facts amend --by` is required for a patch that changes `rev`, and stores the label). A voter votes once per fact, rev and lens for `entail`, `derive` and `currency`: a second vote is refused, and every counting vote counts, so a later positive line cannot cancel a negative one. A vote on a `rejected` or `superseded` fact is refused.

**Fixture votes.** The vote log of the fixture book carries `content` hashes written by `tests/stamp_fixture_votes.py` (fixture only); run it after a change to a fixture fact or to `content_hash`. No real vote log existed when the hash was introduced, so nothing is migrated.

**Fact sheet.** `facts.render_sheet` prints every quote with its Markdown links and images replaced by their link or alt text, so a reader file never carries a link to a host outside the allow-list; the stored quote and every mechanical check are unchanged, and the evidence line under the quote keeps its URL. A heading-scoped quote prints as `> <heading>: "<quote>"`, and `facts packet` gives its `heading` next to the `quote` (with `context` around that line); `facts card` is unchanged.

**What stays with the reviewers.** `freshen` (without `--offline`) and `audit sample --revalidate` fetch every cited page again (a hand-made snapshot); the orchestrator sets `SAA_AGENT` per agent and never lets the miner vote (one agent, two labels); the `facts-final` gate record lists the SHA-256 of the vote log (a hand-written vote line); the claims reviewer reads every W308 line and every decision record.

## R9. Task rules T101 to T201

Moved here from `TOOLS-items.md` 8.1 on 2026-10-09, with the gate-break fixes. A command is every `steps[].command`, `cleanup[].command` and `verify.command`. Blocking rules (`tasks.*`) unless marked:

- **T101** Schema (a schema error of a task is T101, not X01; it fixes the label); id starts with the slug.
- **T102** Minutes and step count in the range of the type; a step text over 40 words.
- **T103** Required fields. Try and Lab: `cost`, `cost_if_forgotten`, non-empty `cleanup`, `verify`, non-empty `permissions`, `read_only_alternative`; steps that change the account need a cleanup command that deletes. Look: empty `cleanup`, `verify` null, `cost` `$0`, no create command, and only read-only operations (`describe`, `list`, `get`, ...).
- **T104** Command form: starts with a prefix of `allowed_command_prefixes`; one command (no `;`, `&&`, `||`, `|`, backtick, `$(`, line break or redirect `>`, `<`, `<(`); no `--profile`, no `sudo`; no `${NAME}` or lowercase `$name`; no `--cli-input-json` or `file://` for a rule or policy option. The stored `command` of a capture step is the plain command; `sync` adds the wrapper. A `curl` command obeys `read_only_tools_rule` and uses only allowed options. A `<PLACEHOLDER>` (`placeholder_regex`) is allowed when the step `text` names it.
- **T115** A `$NAME` (`variable_regex`) that no earlier step of the task captures; two captures with one name.
- **T105** Secure by default: a command matches an entry of `banned_command_patterns`, or one of the built-in patterns: for every rule operation (`authorize-security-group-ingress`, `modify-security-group-rules`, `create-network-acl-entry`, ...), an IPv4 range shorter than /8 or an IPv6 range shorter than /16 in any spelling (`--cidr`, `--ip-permissions`, ...), or a prefix list, that covers port 22 or 3389 (port ranges, protocol `-1` or `all` included; port 443 to the world stays allowed, RULINGS rule 9); a public access block turned off; a public ACL; a grant to `AllUsers` or `AuthenticatedUsers`; a policy with principal `*` and `Allow` without a condition; `--publicly-accessible`; a snapshot or image shared with `all`; `--principal *`; `--auth-type NONE`; `aws configure export-credentials`, `sts get-session-token`, metadata credentials; an access key in the text.
- **T106** Tags: the operation of a step command (its third word) matches `create_command_regex`, is not in `untaggable_operations`, and the command matches no entry of `tag_patterns` or no entry of `tag_task_patterns`. The tag text is searched only in the values of tag options (`--tags`, `--tag-specifications`, ...), never in the whole command. A create operation in `untaggable_operations` needs a name that starts with `saa-`, or a later step that tags the resource.
- **T107** Cleanup pairing. A create command is `<verb>-<noun>` with a verb of `create_command_regex`, or `import`, `register`, `restore`, `request`, `provision` or `purchase`, or `s3 mb` (the operation only); a `put-<noun>` needs `delete-<noun>` or the delete of the resource that holds it (`put-bucket-policy`: `delete-bucket-policy` or `delete-bucket`). Its pair is a cleanup command `<undo>-<noun>` with `<undo>` from `{"create": ["delete"], "copy": ["delete"], "run": ["terminate", "stop", "delete"], "allocate": ["release"], "launch": ["terminate", "delete"], "import": ["delete"], "register": ["deregister", "delete"], "restore": ["delete"], "request": ["delete", "cancel"], "provision": ["deprovision", "delete", "terminate"], "purchase": ["delete", "cancel"], "put": ["delete", "remove"], "mb": ["rb", "delete"]}`, or the operation that `cleanup_pairs` names for it; nouns match with or without a final `s`. Each create command needs its own pair (as many cleanup commands per noun as create commands). The nouns of the paired cleanup commands, in order, are the nouns of the create commands in reverse order (`cleanup_order`). The cleanup command names the capture variable or the name of the created resource; `--dry-run` and `--generate-cli-skeleton` do not count as a cleanup.
- **T108** Try and Lab: the verify command matches no entry of `verify_tag_patterns` (searched in the values of filter and tag options only; `<task id>` is replaced by the task id, as in T106, since 1.0). `tasks.verify_rule` asks for the task tag. Exception: a read-only verify that names the task's own `saa-` resource, with an `expect` (R6).
- **T109** Cost line. Every dollar amount above 0 in `cost` or `cost_if_forgotten` needs `cost_facts`: each `verified`, of kind `price` or `pricing-dimension`, and the amount is in a `display` of one of them. An amount is read as `$4.50`, `4.50 USD`, `USD 4.50`, `5 dollars` or `20 cents`; a money word without an amount fails. The amount in `cost` is at most `cost_usd_max` of the type.
- **T110** A break-it step without `predict`, `expect` or `explain`; an `explain` that fails `lint.check_strict_text` or links a fact that is not in `facts`; a break-it step that is the last step.
- **T111** `trap` is not a known trap id; a fact in `facts` is not `verified`; `section` does not resolve; a `sources` URL is neither in the corpus nor the evidence URL of a verified fact.
- **T112** A banned word in a text field.
- **T113** CLI check: no report `_build/reports/cli/<chapter id>.json` whose `commands_sha256` equals the SHA-256 of all task commands of the chapter joined with `\n`, or the report is not `ok`, lacks an `ok` row for one of the commands, or was not made with the pinned `awscli` version. Blocking only with `--ship`; otherwise a warning. A file is still no proof of a run: the orchestrator runs `tasks check-cli CH` in the `finalize` step before the `tasks` gate (the ledger does not run it).
- **T114** An emulation report for the task with result `fail`.
- **T116** (warning) a `--name`-like option value that does not start with `saa-`.
- **T117** (warning) a click path in a step text (`click`, ` > `).
- **T118** (warning, from `check-cli`) the CLI model shows a tag option for an operation in `untaggable_operations`, or none for a create operation that is not in the list.
- **T119** (`--all`) the sum of the `cost` amounts of all tasks is over `book_cost_usd_max`.
- **T120** A Lab whose `template` is null or names a missing file; a `template` on a Look or Try.
- **T201** (warning; blocking with `--ship`) chapter counts per type, `break_it_steps_min`, and `try_pass_route` (the number of Try tasks with `pass_route: true`; a Look with `pass_route: true` is always an error).

**`tasks check-cli`.** The report has `tag_options` per command and a top-level `warnings` list (T118). The helper `cli_model.py` also checks stray words, single-dash options, shorthand keys, enum values, and the `--query` syntax and fields against the output shape.

**`tasks emulate`.** The helper passes `--endpoint-url` on every command (awscli 1.46.1 ignores `AWS_ENDPOINT_URL` alone) and sets `HTTP_PROXY`, `HTTPS_PROXY`, `http_proxy` and `https_proxy` to the dead proxy `http://127.0.0.1:9` (`NO_PROXY` = `127.0.0.1,localhost`), so a request that does not go to the local moto server fails.

## R10. Question bank: the gate-break additions (2026-10-05)

- **`q add`.** `authors`: the `--by` label of every `q add` and `q add --replace` is added to the question's `authors` (`question.schema.json`); none of these labels can be a solver of it. Q302 at `q add`: `qbank.similarity` against every live question of the bank and against the rejected ones (the chapter's `rejected` items and `_build/qbank/rejected.jsonl`); twins are exempt. Q207: a second `q add --replace` in round 1 (`verification.edits` is 1 after the first).
- **Q102.** Two options with the same normalised text.
- **Q104.** At any mean: the key is longer (or shorter) than every wrong option by 3 words or more and by more than `option_length_spread_max` of the longest (shortest) wrong option.
- **Q105.** An option that points at other options (`None of these options`); a negative stem also as `which ... is not`, `except`, `incorrect` or `least likely` in the question sentence, in any case; a text field that names an option by its position or letter (`the second option`, `(C)`, `B is ...`, `option 2`).
- **Q112.** Recomputed at lint time: a fact linked in the explanation or in a correct option's `why` that is volatile now.
- **Q113.** Also: 70% or more of the key's own content tokens (at least 4) stand in the stem, and that share exceeds the best wrong option's by `max(stem_key_overlap_margin_max, 0.4)`.
- **`qbank.similarity(a, b, threshold=0.6)`.** Duplicate when the Jaccard similarity of the 3-word shingles of the stems' content tokens is at or above the threshold; or stem plus options share 85% of their words in any order (`BAG_DUPLICATE`); or the options are the same (80% common words, `OPTIONS_SAME`) and one stem holds the threshold share of the other's shingles. Used by `q dedupe`, `q add` (Q302), `q lint` and `mocks check` (K04).
- **`q pack`.** Q401 (exit 1): a pack item holds anything but `id`, `type`, `select`, `stem`, `options` (`label`, `text`). Every pack appends to `_build/qbank/packs.jsonl` `{"ts", "pack", "chapter", "lens", "round", "items": {id: hash}}`; the hash covers the stem, the option ids and texts, and the key.
- **`q adjudicate`.** The three answer files are refused as a whole (exit 3, nothing stored) when: the lenses are not three different ones of one round; a file names no `solver` (fewer than 2 characters, or `unknown`); two files are signed by one label (compared without case, spaces and punctuation); a solver is in the `authors` of a question it answers; a question was in no pack of that lens and round, or its text changed after the pack went out; a file has two rows for one id; a closed-lens row has no `stem_only` of at least 3 words; an ambiguity row has no `case` with the label of an option and a text of at least 3 words. Citations (open lens): every label has at least one; a fact citation is `verified`; a quote citation passes `find_quote` and has at least 6 words; the labels do not all carry one identical citation; at least one citation is a fact of the question's `facts` or a quote from a page that is evidence of one of them.
- **Cards and speak.** C105: a list answer is also one comma followed by `and` or `or`, or two slashes. C106: also when one front holds 95% of the other's tokens (both with at least 4). C109 and P109: the comparison with a `display` is `holds_display`. P102: a key point has at most 30 words, a follow-up answer 60, a `must_not_say` correction 40 (`speak.key_point_words_max`, `follow_up_answer_words_max`, `must_not_say_words_max`; optional keys with these defaults). P109 spoken numbers: also `seventeen` to `nineteen` and `dozen`, and a unit or count noun after one or two words. Open rest: the spoken-form check compares number words as substrings (`two hundred widgets` inside `five thousand two hundred widgets` passes); the technical red team lens on `4-say.md` must catch it.

## R11. STYLE 1.0 rule map (2026-10-11)

Each rule of `STYLE.md` 1.0 and `CONVENTIONS-2.md` U, with the `SPEC.json` key and the code that checks it. Where no code checks a rule, the last column names the reviewer lens that does (`PIPELINE` review lenses: claims reviewer, reader lens, exam-validity lens, technical red team). "Review until implemented" marks a rule whose key exists but whose check is a tool change still to be made (list at the end).

| STYLE rule | SPEC key | Code | Else: reviewer lens |
|---|---|---|---|
| 1 sentence and paragraph length, sentence average | `lint.sentence`, `lint.paragraph` | W202, L202 | |
| 1 one main idea, active voice, condition first, repeat the noun, keep "that", noun stack, double negatives, modal meanings | | | reader lens |
| 1 contractions in prose | `lint.contractions_in_prose` | L803 | |
| 1 digits with the unit of the canon | `lint.number_with_unit` | L303, L304 | |
| 2 plain words, five term steps, collocations, at most 3 new terms in a paragraph | `lint.paragraph.new_bold_terms_max` | W202 (bold terms only) | reader lens |
| 2 one term per concept, banned variants | `lint.banned_term_match` | L901 | |
| 2 current names, former name once | `lint.former_names` | L802 | |
| 2 short forms spelled out in each file | `lint.abbreviation_rule` | W802 (bank shorts; aws-name terms skipped: review until implemented) | reader lens |
| 3 banned words, warn words | `lint.banned_words`, `lint.warn_words` | L801, W801 | |
| 3 idioms beyond the list, one analogy and where it breaks, no history, pricing tables or click paths | | T117 (click paths in tasks) | reader lens |
| 4 respelling at first use in each file | `lint.term_rules` | W901 (0.9 form; 1.0 form review until implemented) | reader lens |
| 5 Markdown only, no italics, no emoji | `lint.emphasis_italic`, `lint.emoji` | L803 | |
| 5 bold only at a definition, a label, a step name, the deciding fact | | | reader lens |
| 5 assertion headings | `headings.assertion_heading_words` | L106 | reader lens (is it a true claim) |
| 5 tables: cell words, columns, rows | `tables.*` | L202, L502 | |
| 5 diagram caption and steps | `diagram_embed.*` | L702, L703 | |
| 5 tone; Stop and answer target 70 to 85% | | | reader lens |
| 5 story budget and former name | `startup.story_max_words_per_chapter` | W902 | |
| 5 cast names | `startup.cast` | not implemented (W902 note) | claims reviewer |
| 6 spoken answers: four moves, word ranges, cues, points, follow-ups, digits | `speak.*` | P-codes (`TOOLS-items.md` 7.6) | |
| 6 script still works when a word is lost; follow-up covers every case | | | reader lens, technical red team |
| 7 stem, options, distractors, mix, explanation fields, think-aloud | `questions.*` | Q-codes (`TOOLS-items.md` 7.2) | |
| 7 four-part stem order, parallel options | | | exam-validity lens |
| 7 strict twins (J2) | | Q114 (review until implemented) | exam-validity lens |
| 8 task safety rules 1 to 4, 6, 7 | `tasks.*` | T101 to T120 (R9) | |
| 8 rule 5: verify filters by `task=<task id>` and returns nothing | `tasks.verify_tag_patterns`, `tasks.verify_rule`, `tasks.name_prefix` | T108 (by-name exception, R6) | technical red team (that the API lists the resource; that the expect of a by-name verify is right) |
| 8 rule 8: commands from an official page in the corpus | | T113 (CLI model) | technical red team |
| 9 flashcards | `cards.*` | C-codes (`TOOLS-items.md` 7.6) | |
| 11.1 subsection order and devices | `sections[how].counts` | L106 (`stop_and_answer_per_subsection`); `say_it_per_subsection`, `exam_signal_per_subsection` review until implemented | claims reviewer |
| 11.2 a link carries its whole sentence; most specific fact | `fact_links.*` | L303 | claims reviewer |
| 11.2 short display, at most 8 words without a digit | `fact_links.number_free_display_words_max` | registrar at merge; M7 review until implemented | |
| 11.3 no invented order; 11.4 strongest actor; 11.5 exercise obeys its subsection; 11.6 no hidden story fact; 11.7 Spot the bug not obvious; 11.8 Exam trap is new; 11.9 But not if names the alternative | | | claims reviewer, exam-validity lens |
| 11.10 headings survive the skim | | | reader lens |
| 11.11 Changed recently lines and date | `callouts.changed_recently` | L107 | |
| 11.11 placement of a not examinable entry | `callouts.changed_recently.placement` | L107 (review until implemented) | claims reviewer |
| 11.12 evidence quality, diagram actors, chapter numbers | | | claims reviewer |
| U4 Recap recalls only the fast file | `prompts.recap_rule` | | reader lens |
| U5 brief traps cap | `templates.*.counts.brief_traps_max` | B-code of `gate_brief` (review until implemented) | orchestrator |
| fast-file reading time | `lint.minutes_formula.fast_check` | W105 (review until implemented) | reader lens |

**Tool changes still to make** (the contract names them; the tool does not check them yet): L106 `say_it_per_subsection` and `exam_signal_per_subsection`; L107 placement of a `not examinable yet` entry (`_changed_entry` reads `changed_recently.placement`); W901 per hand file, for brief terms only, skipping prompt paragraphs; W802 exempting only the names of `_build/registry/services.json`; M7 `number_free_display_words_max`; `gate_brief` `brief_traps_max`; W105 `fast_check`; Q114 strict twins (identical option texts, one changed stem phrase, a moved key). Made on 2026-10-11: T108 replaces `<task id>` in `verify_tag_patterns`. Made on 2026-10-12: the T108 exception for a read-only verify on the task's own `saa-` name with an `expect` (R6; `exemplar-spec-changes.md` 5.2).
