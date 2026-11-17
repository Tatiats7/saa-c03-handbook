# RULINGS: the orchestrator's decisions (authoritative)

Approved plan: `~/.claude/plans/pasted-content-id-f907-i-need-curious-brook.md` (2026-10-04).

## Precedence

1. This file.
2. `_build/style/CONVENTIONS.md`, `_build/style/SPEC.json`, `_build/style/STYLE.md`, `_build/style/TOOLS.md` once written (they must not contradict this file).
3. The planning reports in `_build/spec/`. Where they disagree and this file is silent: `LEARNING.md` wins on pedagogy and chapter structure, `PIPELINE.md` wins on verification and tooling, `PRODUCT.md` wins on Markdown syntax, web app, diagrams and exports.
4. `FREQUENCY.md`, `FRESHNESS.md`, `SOURCES.md` are research input, never evidence. Every fact in the book is re-grounded in a saved AWS page.

## The reader

See `_build/style/READER.md`. In short: AWS Startup Solutions Architect, AI/ML background, English is her second language, skims long text, forgets terminology under stress, must also explain services out loud. Diagnostic 2026-09-18: 69% overall, Secure 45%, Resilient 71%, High-Performing 80%, Cost 92%. She asked for: no mid-way pause, deeper content, easier reading, more practice, English-only vocabulary cards. Exam date not fixed.

## Hard rules for every agent

1. Memory supplies questions, never answers. A hard fact (number, limit, default, price, date, "can / cannot", "only / always / never") may appear only if it exists in the fact canon with a verbatim quote that the tool matched against a saved AWS page snapshot.
2. Network access for evidence goes only through `python3 aws-saa-book/tools/saa.py fetch ...`. Never use WebFetch or raw curl as evidence (WebFetch returns a model summary, not page text). WebSearch is allowed only to discover AWS page URLs.
3. No content from exam "dump" or leaked-question sites, ever. All questions are original.
4. Write only inside `aws-saa-book/`. Never run git. Never publish artifacts (only the orchestrator publishes). Never install system software.
5. Run the tool as one plain command from the repo root: `python3 aws-saa-book/tools/saa.py <subcommand> ...`. No `cd`, no pipes, no redirects (use `--out`).
6. Current AWS names only (Amazon Data Firehose, Amazon Quick, Amazon SageMaker AI, IAM Identity Center). A former name may appear once as "formerly ...".
7. Teach current truth. Where a fact changed since mid-2022, add a "Changed recently" note with old value, new value, date, and what older exam questions may assume. A feature generally available for less than 3 months before the exam is labelled "not examinable yet" (rule from the AWS certification FAQ; treat anything GA after 2026-07-15 as not examinable yet).
8. Plain English per the style guide: short sentences, one term per concept, no idioms, no emoji, no cheerleading. English only.
9. Hands-on tasks: AWS CloudShell, never local CLI or access keys; secure by default (no public buckets, no SSH or RDP open to the world, Session Manager instead of bastions); every resource tagged `book=saa`; cost line, cleanup steps and a verify step on every Try and Lab; label "checked against docs, not run in a real account".
10. Return compact results (paths, counts, statuses). Durable state lives on disk.

## Rulings where the planning reports differ

- **Markdown is the source for prose.** There is no token renderer. A hard fact in prose is a Markdown link whose text is the value: `[up to 100 Gbps](../facts/vpc.md#vpc-natgw-bandwidth)`. Lint fails when the link text does not contain the canonical value string, when the fact is not verified, or when an explanatory section contains a bare number-with-unit or an absolute word (only, always, never, cannot, must, by default, up to, at most, not supported) in a sentence without a fact link. Story and example numbers (the running startup, task values) are exempt inside sections whose role is `example`, `task` or `worked`.
- **Structured items are JSON, and their Markdown is generated.** Questions, flashcards, spoken-answer items, labs/tasks with commands, diagram specs and facts live as JSON; `5-quiz.md`, `4-say.md`, the task command blocks, `facts/<service>.md` and `glossary.md` are generated from them between marker comments by the tool.
- **Chapter = folder of short files** (ids and slugs in `_build/registry/book.seed.json`): `1-fast.md`, `2-deep.md`, `3-do.md`, `4-say.md`, `5-quiz.md`, `sources.md`. Section order and devices follow `LEARNING.md` section 1 (Predict, Look first, In one breath, Words that go together, Choose it or not, Signals and traps with a "but not if" column, Changed recently, Check and Recap from memory; then How it works with assertion headings, time boxes and a Stop-and-answer per subsection, Numbers that decide answers, the running startup's decision record, FAQ quick-fire with verbatim FAQ quotes, In the real world).
- **Budgets (she asked for deeper).** Deep: `1-fast.md` at most 1,800 words; `2-deep.md` 3,500 to 4,500 words (IAM, VPC, S3, EC2: up to 5,500), as 8 to 14 short subsections, with edge cases in collapsed "Go deeper" blocks. Medium: fast at most 1,000; deep 1,800 to 2,400. Light: service cards of 150 to 220 words in family chapters.
- **Counts.** Questions shipped: deep 18 (9 core, 9 extended; at least 2 twin pairs, 2 to 3 multiple-response), medium 10, light family 6. Writers produce 20% more and the weakest are cut. Two original 65-question mock exams (domain split 20/17/15/13), never reusing chapter questions. Spoken prompts: deep 4, medium 2, light family 1, each with a 10-second and a 60-second model answer. Flashcards per `LEARNING.md` section 9, plus a 90-word "exam English" deck, English only.
- **Chapter list** is the service-level outline in `book.seed.json`, not the merged list in `LEARNING.md` section 10. Study order and the calendar still follow `LEARNING.md` (security first), written as Day 1 to Day 19 with the three variants and the readiness gates; Day 1 includes "request ESL +30 before booking".
- **Running example:** the fictional startup of `LEARNING.md` section 8 (working name Harken, a call-intelligence service). One fact sheet, never contradicted.
- **Diagrams:** JSON spec rendered by our own grid renderer to SVG (`PRODUCT.md` section 5), official AWS icons, pilot gate of 8 diagrams. Fallback is D2 only if the pilot fails. Mermaid is not used.
- **Web app:** `PRODUCT.md` design. Shell plus per-chapter JSON with a `--single` fallback, title "SAA-C03 Handbook", extending the tokens and exam engine of `/Users/tatiatsmindashvili/Desktop/tatia/certification/saa-c03-diagnostic.html`.
- **Tooling:** one CLI, `aws-saa-book/tools/saa.py`, stdlib core, module files under `aws-saa-book/tools/saalib/`, extras through `uv run --script` with inline dependencies. Fetch allow-list: docs.aws.amazon.com, aws.amazon.com, d1.awsstatic.com, repost.aws, pricing.us-east-1.amazonaws.com.
- **Verification depth (trimmed from `PIPELINE.md`).** Mechanical quote check on every fact. Independent entailment vote on every hard fact; currency vote on every fact touched by a change item; re-derivation on a seeded audit sample. Three-lens blind solve (closed-book, open-book with citations, ambiguity hunter) on every question; unanimous or one edit then reject. Review lenses per chapter: unsupported-claim hunter plus technical red team, reader lens, exam-validity lens.
- **Exemplar:** slices from IAM and VPC judged blind; IAM is the pilot chapter.

## Directory layout

```
aws-saa-book/
  README.md                      contents, status, links (generated)
  NN-slug/                       reader-facing chapter folders
  facts/<service>.md             generated fact sheets: claim | exact AWS sentence | link | date checked
  glossary.md                    generated
  diagrams/src/*.json  diagrams/svg/*.svg
  data/                          structured sources: book.json, facts/<service>.jsonl, <chapter>/{questions,cards,speak,tasks}.json, glossary.json, terms.json
  exports/                       PDFs, Anki deck
  tools/                         saa.py, saalib/, tests/, web/ (app sources)
  _build/                        ignored by git: spec/, style/, registry/, corpus/, ledger/, site/, reports/, tmp/
```

## Build waves

W0 foundation · W1 IAM pilot + front matter (00, 01, 02) · W2 VPC, S3 · W3 security block (04 to 09) · W4 EC2, EBS, ELB, Auto Scaling · W5 RDS, Aurora, DynamoDB, Route 53 · W6 CloudFront, Lambda, messaging, EFS and FSx · W7 HA/DR, cost · W8 11, 12, 19, 33, 29 · W9 24, 25, 34, 35, 32 · W10 37, 38, 39, 42, 43 · W11 light families 20, 30, 36 · W12 synthesis 44 to 49, 52, glossary · W13 mocks 50, 51 and domain drills · W14 whole-book review · W15 release.

## Rulings added during the build (2026-10-04, after the story bible)

- **The running startup is called Callvale** (the working name Harken collides with real companies that sell conversation intelligence). The story bible is `_build/style/STARTUP.md`; its machine-readable twin is `data/startup.json`. The name Harken must not appear anywhere in the book.
- **Story budget:** at most 80 words of narrative story in any one section. The decision record is a structured section with its own word limit in `SPEC.json`; it is not counted as narrative.
- **Accepted story event:** Callvale acquires Peldon Systems at month 25; this is what brings DMS, SCT, Application Migration Service, Amazon MQ, FSx for Windows File Server, Directory Service and DocumentDB into the story.
- **Story diagrams:** the before and after pair of a chapter uses the diagram ids `<slug>-before` and `<slug>-after`.
- **Question stems never name Callvale.** They say "A company", as the real exam does. The story appears only in the chapter prose, the decision record and the spoken prompts.
- **Light family chapters have no decision record.** The story's decision feeds one question and the spoken prompt instead.
- **Spelling:** American English everywhere (data center, analyze, optimize), to match AWS documentation and the exam.
- **The story never teaches a fact.** Where a trade-off in STARTUP.md names an AWS behaviour, the writer must ground it in the fact canon; if the canon disagrees, keep the decision and change the stated reason.
- **Calendar continuity.** The reader has already seen `00-start-here/calendar-preview.md` (written 2026-10-04). The calendar in chapter 00 must start from it: keep its Day 1 to Day 19 structure, its routes per chapter and its gates unless there is a stated reason to change one, and mention any change in a short "Changed since the preview" note. When chapter 00 is finalized, the preview file is removed.

## Rulings added 2026-10-09 (build resumed after the usage-credit stop of 2026-10-04)

- **Startup data file.** The machine-readable story file is `data/startup.json`. `data/harken.json` was deleted on 2026-10-09; every contract document now names `data/startup.json`.
- **Every fact needs an entailment vote**, not only hard facts (gate-break fix H1; stricter than the plan's "entailment vote on every hard fact"). Currency votes on facts touched by a change item and re-derivation on the audit sample stay as planned.
- **Fact-link exemptions are the narrowed ones** of `CONVENTIONS-2.md` decision 33 (confirming `CONVENTIONS.md` decision 23): `Exam signal` is strict after its quoted phrase; role `plan` is heuristic, not exempt; think-aloud steps are example text; every other exception needs the visible `no-fact` marker.
- **No IAM users in hands-on tasks.** `create-user` is banned in task commands (STYLE section 8 rule 1); an IAM user is only ever shown read-only.
- **Exam-policy facts live in chapter 01** (fact namespace `exam`). Chapter 01 must verify, among others, the four facts the web shell reads: `exam-question-count`, `exam-duration-minutes` (replaced `exam-duration`, rejected on 2026-10-11 for a blog quote; a fact id is never reused), `exam-passing-score`, `exam-esl-accommodation`.
- **Heading-scoped evidence (2026-10-11).** A fact may quote one whole value line under a heading when the evidence names that heading (`"heading"`), the way a table row names its header; the mechanical check M4 verifies the heading is the nearest one above the line. Rule text in `TOOLS-rules.md` R8.
- **Registry tool.** `registry check --urls` accepts a guide root in `sources.guides` when the index made by `saa.py guide` exists; the `registry set` patch accepts the key `notes` (frequency notes, marked as third-party research).
- **Synthesis and mock chapters carry exam-guide bullets only where they teach them**; the mock chapters (50, 51) carry all 14 task statements and no bullets.
- **Concurrency.** The ledger hashes a chapter's own registry entry, not the whole `data/book.json`, so fact mining for mapped chapters may run while other chapters are still being mapped. A registry change to a chapter that is already past `plan` is picked up by its `brief` stage.
- **Displays of number-free facts (2026-10-11, from the W1 spot audit).** A display of a fact without numbers is a short phrase (at most 8 words) copied verbatim from one of the fact's quotes, never a paraphrase: the re-derivation audit matches displays word for word, and a long paraphrased display turns a correct fact into a false audit failure. Registrars enforce this when they merge a chapter's facts; the W14 150-fact audit reads `_build/reports/audit/*.review.md` before expanding a chapter.
- **Calendar preview (2026-10-12).** `00-start-here/calendar-preview.md` was moved to `_build/work/00-start-here/calendar-preview.md` once `calendar.md` carried its content and the "Changed since the preview" note: the edit gate's full lint (L101) forbids a file outside the template, so the removal happens at edit, not at finalize.
- **Tag spellings (2026-10-12).** Services whose CLI tag shape is lowercase (`key=book,value=saa`, for example AWS RAM) and filter shapes such as `tagKey=…,tagValues=…` count as the required tags: `SPEC.json` `tasks.tag_patterns`, `tag_task_patterns` and `verify_tag_patterns` list them.

## Rulings added 2026-10-13

### The light process (agreed with the reader on 2026-10-12)
- Model per stage. Mechanical stages run on Sonnet 5.5: fact mining, fact votes (entail, currency, derive), the open-book and the ambiguity blind solvers. Everything that plans, registers, adjudicates, briefs, writes, edits, reviews or fixes runs on Opus 5.5, and so does the closed-book solver (its value is model knowledge). Factory script: saa-chapter-factory.v4-light.js.
- Vote batches hold 80 facts (was 40). The three lenses stay; every fact still needs its entail vote.
- Two reviewers per chapter instead of four: one agent carries the claims and technical lenses (findings/claims.json), one carries the reader and exam lenses (findings/reader.json and findings/exam.json). The findings gate (B05) is unchanged.
- Three blind solvers stay (q adjudicate needs three lenses from three different solvers); only their models changed.
- The orchestrator spawns an agent only for a stage the ledger has not passed; a resumed chapter costs only its remaining stages. Agents still check the ledger themselves (stage show) and skip a passed stage.
- Pacing: one writing run and one facts run at a time, two chapters each. The reader is told once per finished chapter and at publishes, not per stage.
- Not negotiable under the light process: every number, limit, default and can-or-cannot claim in the book is a verified fact with a verbatim quote from a saved AWS page; every shipped question passed the blind panel.
- Tag spellings: SPEC tasks.tag_patterns also accept `TagKey=book,TagValue=saa` and `TagKey=task,TagValue=<task id>` (KMS create-key and other TagKey/TagValue APIs).

### Entail votes on Sonnet: audited 2026-10-13, kept with two safeguards
- Audit (report `_build/reports/audit/sonnet-entail-20261013.md`): an Opus re-judgement of 60 Sonnet-verified facts of chapters 27 and 28 found 4 partial (6.7%), none materially wrong: claim clauses, scopes or exceptions that stand in the surrounding text but not in the quote. The tool's seeded audit matched 20 of 20.
- Decision: entail votes stay on Sonnet. Safeguard 1: the entail packet instruction and the vote prompt now say that a clause, scope, condition or exception found only in the surrounding text makes the verdict `partial`, as does a universal claim with a nearby exception. Safeguard 2: after the first vote round and before adjudication, an Opus spot check re-judges 30 random facts of the chapter and amends what it would not have verified; the adjudicator sends those to a fresh vote. Three or more misses in a spot check are logged as a flag; two flagged chapters in a row move entail votes back to Opus.
- Audit tool backlog (W14): `audit --chapter` ignores the seed (takes the first tier-0 facts alphabetically); the output file name has no chapter and overwrites; the match rule marks agreeing facts as mismatches on wording.
- 2026-10-13 evening: the spot checks of chapters 15 (3 of 30 not positive) and 23 (6 of 30) both flagged, so entail votes run on Opus again from the next facts launch; currency and derive votes stay on Sonnet; the Opus spot check stays as the measure. The amended facts of 15 and 23 were re-voted inside their runs.
- Twin pairing metadata (2026-10-13): `twin_of` is pairing metadata that no blind solver sees. When a verified question's twin is rejected, the orchestrator may clear or re-point its `twin_of` by editing the question file directly, without `q add --replace` and without a verification reset, provided the stem, options, key and explanation stay byte-identical. The replacement twin is a new candidate that goes through the blind panel. (Chapter 17: q006's twin q002 was rejected; q006.twin_of cleared; the new twin is added with twin_of = q006.)
- Measured 2026-10-13 night: voter misses in the 30-fact spot checks (facts the first-round entail voter marked support but the Opus checker did not): Sonnet entail votes, chapter 23: 4 of 30; Opus entail votes, chapters 31 and 19: 1 of 30 each. Opus entail votes stay. The spot check's flag now counts voter misses, not every partial verdict (a partial the voter had already caught is the process working).
- Snapshots (2026-10-14): a re-fetch of a page that verified facts quote changes the snapshot and fails those facts' M2/M3 checks (chapter 23 lost 12 decision-guide facts to a re-fetch made by another chapter's plan). Until the corpus versions its snapshots, agents fetch only pages that are not yet in the corpus (fetch --batch skips cached pages; never pass a refresh option), and a fact that fails M2/M3 after a refresh is re-quoted from the current snapshot and re-voted, not rejected.

## Rulings added 2026-10-22

### Models (the reader's standing rule: no Fable)
- The orchestrator thread runs on Opus 5.5. Every subagent runs on Opus 5.5 or Sonnet 5.5, set explicitly on every agent call; Fable is never used for this build.
- Opus 5.5: plan, register, fact adjudication, spot check, entail votes, brief, fast, deep, questions, tasks, cards and spoken answers, edit, closed-book solver, question adjudication, top-up, both reviewers, fix, and ad-hoc repairs that change facts or chapter text.
- Sonnet 5.5: miners, currency and derive votes, open-book and ambiguity solvers, terms, closer and repack, diagrams, fact requests, close-facts, finalize, and ad-hoc mechanical work (glossary entries, marker cleanup, re-gating).
- Only one thread orchestrates the build at a time. A new thread starts from aws-saa-book/_build/ledger/HANDOFF.md.

## Rulings added 2026-11-16

- The build lives in its own Git repository, `saa-c03-handbook`, synced through a private GitHub repository. One machine and one thread run the build at a time; the thread pulls before it starts and commits after each finished chapter and each publish. The `2026-plans/aws-saa-book` copy is a frozen backup.
- `.gitattributes` disables line-ending conversion for every file. Facts check SHA-256 hashes of the saved pages, so this setting must not change.
- Run args come from `workflows/make_args.py`, which passes each chapter's passed stages to the factory.
