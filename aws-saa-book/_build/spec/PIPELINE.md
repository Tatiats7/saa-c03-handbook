# Production and verification pipeline for the SAA-C03 book: implementation plan

I created no files; this is the whole plan. `BOOK` means `aws-saa-book`. All durations and agent counts are estimates, not measurements.

## 1. The design in brief

- **Fact canon first.** Every hard fact lives once in a per-service fact file, with a verbatim quote that a script has matched against a saved AWS page snapshot. An independent agent then confirms the quote entails the claim.
- **Writers never type numbers.** Prose, questions, flashcards and labs reference facts by token; a renderer inserts the canonical value and the source marker. This gives grounding and cross-chapter consistency by construction.
- **One network path.** All fetching goes through one cached, rate-limited script that only talks to AWS hosts. `WebFetch` and raw `curl` are denied for the build.
- **Disk is the state.** Every stage opens and closes through a ledger command that runs the stage's gate. Workflows return only paths and counts.
- **Default is reject.** Facts that cannot be grounded, questions that are not uniquely keyed and labs that fail lint are dropped and logged, never shipped.
- **Size.** About 1,850 agents, about 260 agent-hours, about 45 hours wall-clock at 8 concurrent agents (plausible range 32–60).
- **Early delivery.** Front matter at about 1.5 h, verified fact sheets at about 2 h, the first full deep chapter at about 3.7 h.

## 2. What I tested today and what it changes

| Test (read-only) | Result | Consequence |
|---|---|---|
| Docs `.md` pages | `text/markdown` with `ETag` and `Last-Modified`; `If-None-Match` returns 304. On four pages, 89–100% of markdown sentences appear in the `.html` twin. | Snapshots are faithful; revalidation is cheap. |
| Guide `llms.txt` | Every guide checked (15) also links a single-file `full.md` (VPC 1.2 MB, EC2 6.4 MB, S3 6.8 MB), with links rewritten to in-document anchors. | Use `full.md` for search only (one request per guide); cite page-level snapshots. |
| Document-history pages | Names differ per guide (`WhatsNew`, `DocumentHistory`, `document-history`, `doc-history`, `History`, `lambda-releases`, `sqs-release-notes`, `dochistory`). VPC's is a 3-column table whose newest entry is 21 Nov 2025. | Resolve by link text from `llms.txt`. Histories lag, so they cannot be the only change feed. |
| What's New | The RSS feed holds 100 items covering 11 days. The JSON API `aws.amazon.com/api/dirs/items/search?item.directoryId=whats-new-v2` works: 22,940 items, `size` up to 1000, product-tag filter works (`amazon-vpc` has 298). Paging stops at offset 10,000 (about mid-2023); the `year` tag is unreliable. `robots.txt` allows this API path and disallows What's New pages for 2020–2024. | Harvest through the API by product tag and filter by date in the script. Never crawl old post pages. |
| FAQ pages | Two markups: embedded JSON (`itemHeading`/`itemLongLoc`, VPC 173 items) and legacy `<b>Q:` paragraphs (EC2 has 821 questions, only 56 in JSON). JSON-LD holds only the first 8. Aurora's FAQ now redirects to `docs.aws.amazon.com/rds/latest/auroraextendedcontent/`. | Visible-text extraction is the evidence base. Q&A parsing is best-effort with two parsers. Always record the final URL. |
| Pricing page | Static text has example prices; the price tables load dynamically. | Price tables are not evidence (see pricing rule in section 7). |
| CLI reference | HTML only. A non-existent command URL returns 200 by redirecting to the service index. | The CLI check must compare final URL and page title, not status code. |
| Exam guide | On docs as markdown (9 pages): 4 domains, 14 task statements, 189 knowledge/skill bullets, 119 in-scope entries (118 unique), 41 out-of-scope. It uses current names ("Amazon Quick", "Amazon SageMaker AI", "Amazon Data Firehose"). | Registry and coverage matrix are parsed from it by script. |
| Certification FAQ | "A new product, service, or feature must be generally available for 3 months before it appears on any exam." I expected 6 months from memory. | Exam-eligibility cutoff is computed from her exam date. Memory is not a source. |
| Current docs vs common prep claims | Lambda timeout is "900 seconds (15 minutes)" with a new 5,400-second exception for Lambda Managed Instances. S3 default is 10,000 general purpose buckets. NAT gateway scales to 100 Gbps. Regional NAT gateways arrived 19 Nov 2025. | Canonical facts need scope qualifiers; "then vs now" notes are necessary. |
| Case studies | The API `item.directoryId=customer-references` has 4,313 items with product tags (`GLOBAL#product#dynamodb`) and customer-segment tags. 85% of recent items link to server-rendered case-study pages. | Deterministic discovery of official examples; quotes come from the page snapshot. |
| Quote-check prototype | Stdlib only, in memory. 7 of 7 true quotes matched (links inside sentences, escapes, en dashes, table rows, FAQ HTML with curly apostrophes). A paraphrase and a wrong number both failed. | Mechanical verification works with one shared normaliser. |
| WeasyPrint | Installed but fails on `--version` ("could not import some external libraries"). | PDF goes through Chrome headless. |
| PDF tools | No `pdftotext` or `mutool`. The official sample-question and exam-guide PDFs still return 200. | Agents read PDFs with the Read tool; sample questions are a style reference only. |
| Artifact rules (from the artifact skills) | 16 MB page cap; Mermaid rendered natively; `localStorage` survives republish but is not reliable; the `db` capability keeps per-user data across republishes; no print dialog; plain download links are inert. | A single-file app is feasible. Progress goes in `db` with `localStorage` as cache. PDF and Anki files are built locally. |
| Packages (metadata only) | awscli 1.46.1, botocore 1.43.108, moto 5.2.3, genanki 0.13.1, mermaid 12.1.0. uv already has Python 3.12.12 and 3.13.5. Homebrew's d2 is 0.9.0, not 0.8.1. No Anki app on this Mac. | Extras are available but untested (section 20). |
| Repo | Her 18 Sep diagnostic (`/Users/tatiatsmindashvili/Desktop/tatia/certification/study-plan.md`): 69% overall, 45% on Secure. | Ordering tweak in section 9. |

Four claude.ai connectors (Excalidraw, Gmail, Google Calendar, Google Drive) are unauthenticated in this non-interactive session. She would need to authorise them in claude.ai connector settings before use; this plan does not depend on them.

## 3. Directory layout

```
BOOK/
  README.md, CHANGELOG.md          generated: contents, status, "changed since you read it"
  NN-title.md                      reader-facing chapters, generated, only when status = ready
  assets/  labs/  evidence/        rendered diagrams (SVG), lab scripts, per-chapter quote tables
  dist/                            web/index.html, aws-saa.apkg, flashcards.tsv, book.pdf
  tools/                           saa.py + modules (stdlib only), x_lab.py, x_anki.py, tests/
  _build/                          contains a .gitignore with "*", so nothing here can be committed
    registry/   book.json, exam_guide.json, services.json, terminology.json, lifecycle.json
    style/      STYLE.md, SPEC.json, READER.md, STARTUP.md (story bible), exemplar/
    corpus/     snap/ (raw + .txt + .meta.json), full/, index/, faq/, changes/, cases/, fetch.log.jsonl
    facts/      <service>.jsonl, requests/, votes/, conflicts.jsonl
    src/NN-slug/  brief.json, sNN-*.src.md, lab-*.json, diagrams/*.mmd
    qbank/      chapter/NN.jsonl, mock/pool.jsonl, packs/, votes/, rejected.jsonl
    cards/  mocks/  reports/
    ledger/     chapters/NN.json, gates/NN.<gate>.json, runs.jsonl, events.jsonl, RUNBOOK.md
```

The reader-facing Markdown is generated from `_build/src` and is what she reads. The web app is built from the same source, and a build check asserts the two have identical text. The PDF is built from the rendered Markdown.

## 4. Tools: one CLI, `python3 BOOK/tools/saa.py <subcommand>`

The core is stdlib-only on the system Python 3.14. Extras run through `uv run --script` with inline dependencies and are launched by `saa.py`, so one allow rule covers everything. Every subcommand takes `--out FILE` and `--max-lines N`, so agents never need pipes or redirects.

Exit codes everywhere: 0 pass; 1 blocking failure (JSON report written); 2 warnings only; 3 precondition missing or stale; 4 policy refusal (host, robots, path); 5 transient, safe to retry.

| Subcommand | Purpose | Input and output |
|---|---|---|
| `fetch URL… [--batch F] [--revalidate]` | Cached, polite fetch. Allow-listed hosts: `docs.aws.amazon.com`, `aws.amazon.com`, `d1.awsstatic.com/training-and-certification/`. Enforces `robots.txt`, a global 1 request/second file lock, backoff and a daily cap. | Raw body, normalised `.txt`, `.meta.json` (url, final_url, etag, sha256, fetched_at); prints source_id and paths. |
| `guide ROOT` | Fetch `llms.txt` and `full.md`; build the page index; resolve history and quota pages. | `corpus/index/<guide>.json` |
| `search PATTERN [--scope full\|snap\|faq\|changes\|cases]` | Bounded grep over the corpus. | Hits with source_id, line, 200 characters. |
| `show SOURCE [--around TEXT]` | Bounded excerpt, so agents do not read whole files. | Text. |
| `tables SOURCE` | Parse markdown tables into header-keyed JSON rows. | Rows. |
| `faq URL`, `changes harvest\|for SVC`, `cases harvest\|for TAG` | Parse FAQ Q&A; harvest What's New and document histories; harvest the case-study directory. | JSONL in corpus. |
| `registry build\|check\|wave-args WAVE` | Parse the exam guide into IDs; validate every seed URL; print the compact args for a workflow. | JSON. |
| `facts add\|adopt\|verify\|batch\|packet\|vote\|finalize\|card\|request\|amend\|conflicts` | The only way to change the canon (file-locked, schema-checked). `adopt` builds a fact from a table row so the quote is produced by script. `packet` builds verifier inputs with script-pulled context. `finalize` computes status from votes by fixed rules. | Fact files, vote files. |
| `stage begin\|end CH STAGE` | `begin` prints SKIP (already passed with matching input hashes), GO, or BLOCKED (3 attempts used, or prerequisite gate missing). `end` runs the gate and records it. | Ledger. |
| `lint CH`, `render CH`, `diagram CH` | Chapter lint (section 11), token rendering, Mermaid compile to SVG. | Report, reader Markdown, SVG. |
| `q add\|lint\|pack --blind\|adjudicate\|dedupe` | Question bank. `pack --blind` strips keys and permutes options per solver. `adjudicate` compares solver answers to the key by script. | Bank and pack files. |
| `cards add\|lint`, `lab lint\|emulate\|render` | Flashcards; labs (section 14). | |
| `coverage`, `mocks assemble --seed N\|check` | Coverage matrix; deterministic mock assembly. | Reports, `mocks/*.json`. |
| `gate CH\|--all [--quick]`, `status`, `report wave W` | Re-run all mechanical gates; one-screen status; wave summary of at most 50 lines. | |
| `audit sample --n N --seed S`, `freshen` | Seeded random fact sample for re-verification; revalidate all ETags and re-verify quotes from changed pages. | |
| `build web\|anki\|pdf\|readme\|changelog\|factsheet CH`, `selftest` | Output builds; must-fail fixture tests for every gate. | `dist/` |

## 5. Schemas

**Registry** (`_build/registry/book.json`):
```json
{"book":{"exam":"SAA-C03","snapshot_date":"2026-10-04","change_window_start":"2022-07-01",
         "exam_date_target":"2026-10-22","exam_eligibility_cutoff":"2026-07-22","style_version":"1.0","mock_seed":20261004},
 "chapters":[{"id":"05","slug":"vpc","title":"Amazon VPC","tier":"deep","wave":"W1","priority":1,
   "services":["vpc"],"owns_fact_namespaces":["vpc"],"tasks":["1.2","2.2","3.4","4.4"],"bullets":["1.2.S1","1.2.S2"],
   "sources":{"guides":["vpc/latest/userguide"],"faq":["https://aws.amazon.com/vpc/faqs/"],"history":"…/WhatsNew.md",
              "quotas":["…/amazon-vpc-limits.md"],"whatsnew_tags":["amazon-vpc"],"case_tags":["vpc"]},
   "budget":{"words":[8000,12000],"facts":[160,260],"questions":18,"multi_response":3,"cards":35,"labs":1,"spoken":6},
   "owns_tables":["sg-vs-nacl","gateway-vs-interface-endpoint"],"uses_tables":["alb-nlb-gwlb"]}]}
```
`exam_guide.json` holds every bullet as `{id:"1.2.K3", kind, text (verbatim), source_id}`. `services.json` holds every in-scope entry as `{id, official_name (verbatim), former_names, home_chapter, level}`.

**Fact** (`_build/facts/<service>.jsonl`):
```json
{"id":"vpc.natgw.bandwidth","service":"vpc","home_chapter":"05",
 "kind":"limit",   // limit|quota|default|behavior|capability|restriction|pricing-dimension|price|sla|change|exam-policy|case-study
 "claim":"A NAT gateway supports 5 Gbps of bandwidth and automatically scales up to 100 Gbps.",
 "values":[{"key":"base","display":"5 Gbps","spoken":"five gigabits per second"},{"key":"max","display":"100 Gbps"}],
 "qualifiers":{"scope":"per NAT gateway","default_or_max":"max","adjustable":false,"condition":""},
 "evidence":[{"source_id":"docs/vpc/latest/userguide/nat-gateway-basics","url":"https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-basics.html",
              "quote":"A NAT gateway supports 5 Gbps of bandwidth and automatically scales up to 100 Gbps.","sha256":"…","match":[1234,1318],"table_header":null}],
 "source_tier":1,"hard":true,"tier0":true,"volatility":"changed-since-2022",
 "changed":{"date":"…","was":"…","was_evidence":{}},"exam_relevance":"core",
 "status":"verified",   // candidate|mech-pass|verified|disputed|rejected|superseded
 "votes":[{"lens":"entail","verdict":"support"},{"lens":"contra","verdict":"no-contradiction"},{"lens":"rederive","verdict":"match"}],"rev":1}
```

**Question** (`_build/qbank/…jsonl`):
```json
{"id":"q-05-012","pool":"chapter","chapter":"05","domain":1,"task":"1.2","bullets":["1.2.S1"],"services":["vpc"],"concepts":["sg-vs-nacl"],
 "type":"single","choose":1,"stem":"…","constraint_keyword":"MOST secure",
 "options":[{"key":"A","text":"…","correct":true,"rationale":"… {{f:vpc.sg.stateful}}","misconception":null},
            {"key":"B","text":"…","correct":false,"rationale":"… {{f:vpc.nacl.stateless}}","misconception":"treats NACLs as stateful"}],
 "takeaway":"…","fact_ids":["vpc.sg.stateful","vpc.nacl.stateless"],"volatile":false,
 "difficulty":{"target":"medium","estimated":null},"signature":"1.2|sg-vs-nacl|sg|stateful-return",
 "verification":{"status":"candidate","round":0,"solvers":[]}}
```

**Flashcard**: `{"id":"c-05-007","chapter":"05","kind":"number|compare|trigger|term|cloze","front":"…","back":"… {{v:vpc.natgw.bandwidth#max}}","fact_ids":[…],"tags":["d1","vpc"],"guid_seed":"c-05-007"}`

**Ledger** (`_build/ledger/chapters/05.json`):
```json
{"chapter":"05","rev":2,"style_version":"1.0","status":"ready",   // planned|facts-verified|drafted|reviewed|ready|blocked
 "stages":{"plan":{"status":"pass","attempts":1,"inputs_hash":"…","ts":"…","run":"…"},
           "facts":{"status":"pass","counts":{"candidate":241,"verified":221,"rejected":12}},
           "review":{"status":"pass","findings":23,"fixed":21,"removed_claims":2},
           "questions":{"status":"pass","written":22,"pass":17,"fixed":2,"rejected":3},
           "lab":{"status":"pass","emulated":"pass"},"final_gate":{"status":"pass","hash":"…"}},
 "warnings":["pending table alb-nlb-gwlb"],"published":{"web_rev":3}}
```
Gate records carry the SHA-256 of every input file, so a stale gate is detectable. `events.jsonl` is append-only.

## 6. Grounding (requirement 1)

**Corpus and tiers.**
- Tier 1: user guides, API references, quota pages.
- Tier 2: FAQ pages, pricing page text, Well-Architected, whitepapers, the exam guide.
- Tier 3: What's New posts and document-history rows. These supply only dates and old-versus-new deltas, never current truth on their own.
- Tier 4: case-study pages, for company examples only.
- When tiers disagree, Tier 1 wins and the conflict is logged to `conflicts.jsonl` and to `reports/aws-doc-inconsistencies.md`. As an AWS employee she can file doc feedback from that report.

**Mechanical fact checks (script, all blocking).**
- The snapshot exists, is on an allow-listed host, and its hash matches.
- The normalised quote is a contiguous substring of the normalised snapshot. The normaliser applies NFKC, unifies quotes and dashes, strips link targets, emphasis, escapes, anchors and table pipes, collapses whitespace and lowercases.
- The quote is 8–80 words, or a table row.
- Every number and unit in the claim and display strings appears literally in the quote. `TB` and `TiB` are different; number words are mapped. A derived value needs a `derivation` field and a model check.
- Limits, quotas and defaults must carry scope, default-or-max, and adjustable.
- For a table quote, the script attaches the header row itself, so "5" can be checked to sit under "Default".
- The quote is not from navigation or footer text.
- Facts with the same subject and different values go to the conflict queue.

**Referencing from prose and questions.**

| Token in source | Meaning | Reader sees |
|---|---|---|
| `{{v:FACT#key}}` | Value from the canon | The display string plus a source marker |
| `{{f:FACT}}` | This sentence is supported by FACT | A source marker |
| `{{eg:text}}` | Illustrative number in an explanatory section | The text |
| `{{table:ID}}` | Single-sourced comparison table | The table |
| `{{x:CH#anchor\|text}}`, `{{fig:ID}}` | Cross-reference, diagram | Link, image with caption |

**Reader-facing sources without clutter.**
- One superscript number per sentence at most, linking straight to the AWS page.
- A numbered Sources list at the chapter end with page title, URL and snapshot date. "Numbers to know" tables get a source column instead of inline markers.
- The verbatim quotes live in `BOOK/evidence/NN.md` and in a tap-to-open popover in the web app.

**A claim that cannot be grounded.**
1. It becomes a fact request and gets one targeted search round (corpus first, then `WebSearch` restricted to AWS domains to find a page, fetched through the script).
2. If still ungrounded, it is rewritten to what the sources do support, or removed.
3. It is never shipped as fact. Every removal is counted in the ledger and listed in `reports/NN.ungrounded.md`.

Statements about the exam itself that AWS does not publish are a separate class. They appear only in visibly labelled "exam heuristic" boxes.

## 7. Freshness (requirement 2)

- **Change feed per service**, window 2022-07-01 (just before SAA-C03 launched) to today: parsed document-history rows plus What's New items by product tag.
- **Change lens.** A dedicated miner triages every item into change facts (date, what changed, old value only if the announcement or history row states it verbatim, pointer to the current-truth fact). It also carries a seed list of well-known shifts to check as hypotheses.
- **Currency vote.** Any hard fact whose subject matches a change item gets the second verification lens. That lens must confirm the fact reflects the post-change state.
- **Presentation.**
  - Main text always teaches current truth.
  - Each chapter has a "Then vs now" box: change, date, current truth, what older material may assume, how to answer. Its heuristic line reads: "prefer the option that is right under both".
  - Items generally available after `exam_eligibility_cutoff` (exam date minus 3 months, grounded in the certification FAQ snapshot) are labelled "not examinable yet; know it for customers".
  - A generated book-level "What changed since most prep material was written" digest collects all of them.
- **Questions.** They are keyed to current truth. A question whose key depends on a fact changed in the last 12 months is tagged `volatile` and excluded from mocks.
- **Pricing.** Pricing dimensions are grounded in docs. Exact prices appear only when verbatim in a static snapshot, with Region and date, and always through tokens.
- **Re-checkable later.** `saa.py freshen` revalidates every cited page by ETag and re-runs quote checks. She can run it the week before the exam.

## 8. Consistency across chapters (requirement 3)

1. **Value tokens and single ownership.** A fact belongs to its service's home namespace. Other chapters reuse the ID or file a fact request; they never restate. A correction is one `facts amend`, then a mechanical re-render of every chapter, card and question that uses it. Affected questions go back to verification and a CHANGELOG line is generated.
2. **Single-sourced comparison tables.** About 40 cross-service tables each have one owning chapter, assigned in the registry. Everyone else transcludes. A table whose owner is not yet written renders as a "coming in chapter N" stub: a warning now, a blocker at release.
3. **STYLE.md, SPEC.json and the exemplar** fix section order, per-tier word budgets, voice and devices. A structure lint enforces them.
4. **Terminology registry.** Official names come verbatim from the in-scope list. Former names are allowed once as "formerly …"; deprecated names are lint errors.
5. **Story bible** (`STARTUP.md`): one fictional startup with fixed names, numbers and an architecture timeline per chapter. A continuity lint checks entity names.
6. **Generated synthesis.** The numbers sheet, the atlas rows, the freshness digest and the glossary are built from structured data, then edited. They cannot drift from the chapters.

## 9. Workflow sequence

The orchestrator runs these in order and does the checks in section 16 between them.

| Workflow | Purpose | Agents | Hours | Gate before the next |
|---|---|---|---|---|
| W0 `saa-foundation` | Permission canary first. Core tools, then remaining tools, with must-fail fixtures supplied by the orchestrator. Three adversarial "gate breakers" try to pass bad inputs through each gate. Registry from the exam guide plus a registry critic. Corpus indexes, change and case harvest. Web shell on fixtures. VPC plan, mining and fact verification start as soon as core tools pass. | ~45 | ~1.1 | `selftest` exits 0; every bullet and in-scope service is assigned; canary saw no prompt |
| W1 `saa-exemplar` | Section 12. Also front matter (exam blueprint, how to use, study plan) and pre-mining of facts for IAM, S3 and EC2 in spare slots. | ~125 | ~2.5 | Acceptance panel; orchestrator reviews pilot metrics and tunes prompts |
| W2 `saa-chapter-factory` wave A1 | IAM, S3, EC2 (facts already verified). | ~85 | ~2 | Final gates |
| W3 wave S1 | Five medium security chapters: Organizations and Identity Center, KMS, secrets and certificates, edge protection, detection services. | ~165 | ~3.3 | |
| W4–W6 waves A2–A4 | EBS, ELB, Auto Scaling, Route 53. Then RDS, Aurora, DynamoDB, CloudFront. Then Lambda, SQS/SNS, cost, HA/DR. | ~190 each | ~4.4 each | |
| W7–W9 waves B2–B4 | The other 14 medium chapters. | ~155 each | ~3.1 each | |
| W10 wave C | 8 light chapters. | ~145 | ~2.4 | |
| W11 `saa-synthesis` | Reference architectures (written); atlas, numbers sheet, freshness digest and glossary (generated, then edited); domain drills; final-week checklist. | ~95 | ~3 | |
| W12 `saa-mocks` | Section 13. | ~90 | ~2 | Mock check |
| W13 `saa-bookreview` | Section 15. | ~90 | ~3 | Zero blocking findings |
| W14 `saa-release` | Final web, Anki and PDF builds, smoke tests, final report. | ~6 | ~0.7 | |

**Ordering tweak (recommended).** S1 runs straight after A1 because Secure is 30% of the exam and her weakest domain at 45%. It is one `priority` field in the registry if you prefer strict deep-first.

**Deep count.** The brief names 16 deep topics; I batch those 16.

**Why waves are separate workflow runs.** A wave of 4 deep or 5 medium chapters keeps priority order strict. It also gives a natural publish point. Resume does not rely on the cache: stages skip themselves through the ledger even on a cache miss.

Each workflow returns `{wave, ready:[ids], blocked:[{id, stage, reason}], counts:{facts, questions, cards}, capped:[…], report:"path"}`.

## 10. The per-chapter pipeline (`saa-chapter-factory`)

Agent counts are deep / medium / light. Every stage starts with `stage begin` and ends with `stage end`. Every prompt carries the same twelve-line rule block: memory supplies questions, never answers; network only through `saa.py fetch`; edit only your chapter's directory; numbers only by token; return the schema, not prose.

| Stage | Agents, effort | Role and prompt essentials | Returns | Pass rule |
|---|---|---|---|---|
| S1 Plan | 1; medium | Reads the registry entry, the chapter's exam-guide bullets and the guide indexes. Searches `full.md`. Selects and fetches pages (deep 40–80), FAQ, quotas, pricing, change feed and case-study candidates. Writes `brief.v0.json` with a fact demand list: questions to answer, each tagged to a bullet. | `{sources_fetched, fetch_failures[], demand_items, change_items}` | Every bullet has at least one demand item; failures listed |
| S2 Mine | 5 / 3 / 2; medium | One lens each: concepts and behaviour; limits and defaults (through `tables` and `facts adopt`); FAQ; changes; decisions, pricing dimensions and security. Reads snapshots only. Marks each demand item filled, contradicted (with what the source says), or not found. | `{lens, facts_added, mech_rejected, demand_unfilled[]}` | Every added fact passes the mechanical checks |
| S3 Register | 1; high | Merges duplicates, assigns canonical IDs and display strings, completes qualifiers, queues conflicts, flags hard and tier-0 facts, cuts verification batches of 30. | `{facts_total, hard_total, conflicts, batches[]}` | Batches cover every fact |
| S4 Verify facts | ~14 / 7 / 3; high, adjudicator max | Section 11. Verifiers see only script-built packets. | `{verified, repaired, rejected}` | Every fact ends verified or rejected |
| S5 Brief | 1; high | Binds each section's points to verified fact IDs. Sets budgets from SPEC, story beats, case studies, tables, diagrams, the lab, question slots (bullet × concept × difficulty × type) and a misconception catalogue. | `{sections[], question_slots, lab}` | Every bullet maps to a section and a question slot; nothing depends on an unverified fact |
| S6a Prose | 3 / 2 / 1; xhigh | Each writer gets its sections, their fact cards, STYLE, SPEC and the matching exemplar sections. A missing fact becomes a fact request, not a sentence. | `{files[], words, fact_requests[], lint}` | Section lint clean |
| S6b Questions | 3 / 1 / with writer; xhigh | Writes 1.2 times the target from the slots, through `q add`. | `{written, lint_pass}` | Question lint clean |
| S6c Lab | 1; high | Lab JSON from an official tutorial snapshot (section 14). | `{lint, emulated, cleanup_pairs_ok}` | Lab lint passes |
| S6d Cards | 1; medium | One fact per card, values by token. | `{cards}` | Card lint clean |
| S7 Edit | 1; high | Stitches, removes repetition, runs `lint` and `render` until clean. | `{lint}` | Zero lint errors |
| S8 Review | 4 / 3 / 2 lenses, plus lab auditor and card reviewer; high | (a) Unsupported-claim hunter on the rendered text. (b) Technical red-team: pick the 15–20 riskiest statements and try to refute each from the corpus, with quotes. (c) Reader and pedagogy lens using READER.md. (d) Trigger-and-trap validity (deep only). | `{lens, findings_path, counts}` | Findings carry location, type and evidence |
| S9 Fix, recheck | 2; high | Applies findings. Ungroundable hard claims are removed or softened. The recheck lens re-reads changed spans. Two rounds at most. | `{fixed, removed_claims}` | Zero blocking findings |
| S10 Verify questions | ~7; high, adjudicator max | Section 13. | `{pass, fixed, rejected, below_min}` | Passed count meets the tier minimum |
| S11 Finalize | 1; low | Final gate, render, coverage update, ledger. | `{status, rev, counts, warnings}` | Chapter is `ready` |

S6a–S6d run in parallel after S5.

Control-flow skeleton (plain JavaScript; fan-out sizes come from agent returns because the script cannot read files):
```js
const out = await pipeline(args.chapters,
  ch => agent(planPrompt(ch), {phase:'Plan', schema:PLAN, effort:'medium'}),
  (p, ch) => parallel(ch.lenses.map(l => () => agent(minePrompt(ch,l), {phase:'Mine', schema:MINE, effort:'medium'}))),
  async (m, ch) => { const reg = await agent(registerPrompt(ch), {phase:'Verify facts', schema:REG});
    await parallel(reg.batches.map(b => () => agent(votePrompt(ch,b), {phase:'Verify facts', schema:VOTE, effort:'high'})));
    return agent(adjudicateFactsPrompt(ch), {phase:'Verify facts', schema:ADJ, effort:'max'}) },
  (v, ch) => agent(briefPrompt(ch), {phase:'Brief', schema:BRIEF}),
  (b, ch) => parallel([() => proseTrack(ch), () => questionTrack(ch), () => labTrack(ch), () => cardTrack(ch)]),
  (t, ch) => agent(finalizePrompt(ch), {phase:'Finalize', schema:FINAL, effort:'low'}))
return summarize(out)   // lab and card tracks catch their own errors so they cannot drop a chapter
```

## 11. Verification design (requirement 1 and 4 in detail)

| Object | Mechanical (script) | Independent model checks | Pass rule | On failure |
|---|---|---|---|---|
| Fact | Section 6 checks | Entailment vote on every fact (does the quote, with script-pulled context, support the claim including scope and unit). Contradiction-and-currency vote on hard facts (search the corpus for a conflicting or newer statement). Independent re-derivation on tier-0 facts and audit samples: the verifier gets only the question, finds the answer in the corpus, and the script compares. | All votes support; anything else is "disputed" | Adjudicator at max effort may repair the claim to what the quote supports, or attach better evidence. A repaired fact needs a fresh entailment vote. Otherwise rejected. |
| Prose | Chapter lint (below) | Four lenses in S8, one vote each | Zero blocking findings after at most two rounds | Sentence removed or softened; logged |
| Question | Question lint | Section 13 | Unanimous and unflagged | Edit once or reject |
| Lab | Lab lint, emulator | One cleanup-and-order auditor | All pass | Lab withheld; chapter marked "lab pending" |
| Flashcard | Card lint | One reviewer | | Fix or drop |

Uncertain always counts as reject.

**Chapter lint.** Blocking:
- Required sections present and in SPEC order.
- Every token resolves to a verified fact.
- In explanatory sections, no bare number outside a token or `{{eg:}}`.
- Sentences with absolute or limit words (only, always, never, cannot, must, by default, up to, at most, not supported) carry a fact marker.
- No deprecated service names.
- Every external link is an AWS page that exists in the corpus.
- Diagrams compile.
- Minimum counts met for questions, cards and spoken answers.

Warnings: word budgets within tolerance, sentence length, pending shared tables, duplicated tables, story-name mismatches.

The `{{eg:}}` wrappers in explanatory sections are listed for the unsupported-claim hunter, so the wrapper cannot hide a fact.

**Blocks versus warns.** A chapter is published only when `ready`. Warnings travel with it into the ledger and the wave report. The release gate requires zero pending tables, zero stale questions and zero open blocking findings.

## 12. The exemplar judge panel (requirement 5)

**Subject: VPC.** It exercises every template element (limits, comparisons, pricing dimensions, diagrams, a billable lab with cleanup) and sits in her weakest domain (task 1.2). IAM follows in the next wave.

1. **Story bible and reader card.** One agent writes `STARTUP.md`. The orchestrator writes `READER.md` from `/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/habits.md`, `October.md` and the diagnostic: second-language English, skims, forgets terms under stress, 40 study hours, spoken customer exam the week of 13 October.
2. **Three independent attempts**, each from a different angle: first-principles narrative; exam-operator (decision tables and traps first); customer-conversation. Each delivers a full outline with section order and word budgets, two fully written slices (security groups versus network ACLs; NAT gateway and egress including cost), the quiz block for those slices, and the one-page summary. Slices avoid writing three full chapters to discard two.
3. **Five judges, blind to authorship, attempt order rotated.** The lenses are the reader persona, an exam-prep expert, a senior AWS architect, an instructional designer and a plain-language editor. Each returns rubric scores, a ranking, ideas to graft and must-fix defects.

   | Rubric criterion | Weight |
   |---|---|
   | Learnability for this reader | 20 |
   | Exam discrimination power | 20 |
   | Technical precision | 20 |
   | Reusable explanations | 10 |
   | Retention design | 10 |
   | Economy | 10 |
   | Grounding hygiene (fed by the lint score) | 10 |

4. **Script aggregation.** Borda count plus weighted means. The winner must be in the reader judge's top two and have no fatal technical defect.
5. **Synthesis.** One agent writes `STYLE.md` and `SPEC.json` from the winner plus grafts. The spec includes a mandatory ten-minute fast path per chapter and per-tier budgets, plus a condensed light-tier sample. A spec critic checks every rule has an example and, where possible, a lint check.
6. **Pilot.** The full VPC chapter is produced by the standard factory under the new spec. This is also the end-to-end pilot of the pipeline.
7. **Acceptance.** Three judges (reader, technical, exam) accept or request revision, two rounds at most. Then the style version is frozen and hash-pinned.

There is no pause for her. If she comments later, the orchestrator records it in `style/FEEDBACK.md`, bumps the style version for unwritten chapters, and queues a restyle only for structural changes.

## 13. Question bank and mock exams (requirement 4)

**Volumes.** About 436 chapter questions (deep 16, medium 8, light 5, synthesis ~20) plus 195 mock questions drawn from 225 written. Drills are filtered views over chapter questions plus about 15 new integration questions per domain.

**Writing rules.**
- Scenario stem with a business requirement and one constraint keyword. All needed information is in the stem.
- Four options with one correct, or five options with "(Select TWO.)", matching the exam guide's formats.
- Every distractor is a real in-scope service or setting that fails a stated requirement for a fact-grounded reason, and names the misconception it embodies.
- No "all of the above", no negative stems. Recall-only questions are capped at 10%.
- The official sample-question PDF is a format reference only. Third-party question sites are not consulted at all (section 17).

**Mechanical lint.**
- Schema; option and key counts; "(Select N.)" consistency.
- The correct option is not the longest by more than 30%; absolute words are balanced across options.
- Tokens resolve; each rationale cites a fact; services are in scope.
- Near-duplicate stems (token similarity) and duplicate concept signatures across the whole bank, including mocks against chapters.

**Blind solving, three lenses, one agent per lens per batch.**
1. Closed-book expert.
2. Open-book verifier. It must cite fact IDs or quotes for the key and for rejecting each distractor.
3. Ambiguity hunter. It builds the strongest case that each distractor is correct and flags missing constraints or wording cues.

Packs are blind and option-permuted per solver.

**Decision rule (script).** An item passes only if all three match the key, none flags ambiguity, and the open-book citations verify. Anything else goes to an adjudicator at max effort who edits once or rejects. An edited item needs two fresh blind passes or it is rejected. Writers over-produce by 20%, so there is no top-up loop unless a chapter falls below its minimum.

**Difficulty.** A low-effort quick solver plus two rubric raters (number of constraints, closeness of the top two options, need for a numeric fact, multi-select). It is labelled "estimated".

**Mock assembly (`mocks assemble`, seeded and deterministic).**
- Three mocks of 65 from a separate pool, never chapter questions.
- Domain split 20 / 17 / 15 / 13, the same as her September diagnostic. Largest-remainder rounding of 30/26/24/20% gives 19/17/16/13; either is defensible, and this choice keeps scores comparable.
- Every one of the 14 tasks appears in every mock. No service is the focus of more than four questions. About eight multi-response items. Difficulty balanced within 5% across mocks. No `volatile` items.
- Two agents then sit each full mock blind, and a third hunts for one question leaking another's answer. Any miss is adjudicated and replaced from the spare pool.

## 14. Labs (requirement 8)

Labs are authored as structured JSON. Each step has argv, captured variables and expected output shape. The Markdown and the `.sh` file are rendered from that JSON, so what was validated is what is printed.

1. **Provenance.** The base is an official tutorial or CLI example snapshot. Every command points to its source line; deviations are listed.
2. **Static lint.** Each `aws` command and option is checked against the awscli model in-process, and against the CLI reference snapshot (final URL must end in the command name).
3. **Emulated dry run where supported.** The runner executes the argv list itself against a local moto server with dummy credentials. The endpoint is forced to loopback and the config files are nulled. This catches wrong `--query` paths, variable plumbing and ordering.
4. **Cleanup completeness.** A lifecycle table pairs every create, allocate and run command with its delete. Order rules are grounded as facts. Every resource is tagged `saa-lab=<id>`, and the last step lists leftovers by tag.
5. **Cost block.** Billable resources and their pricing dimensions come from facts. Dollar figures appear only if grounded.
6. **Label on every lab.** "Validated against the AWS CLI reference and tutorial on <date>; emulator run: pass / not supported; not run against a real AWS account."

Labs are CLI-first and written for AWS CloudShell.

## 15. Whole-book review (requirement: completeness and consistency)

- **Coverage matrix (script).**
  - Each of the 189 bullets needs a tagged section, at least two bank questions and at least one mock question.
  - Each of the 118 services needs a home or atlas entry, at least one fact, one card and one question. Core services need five questions.
  - A zero cell for a bullet or core service blocks release.
- **Completeness critics.** One per domain plus one for services. They open the tagged sections and confirm each bullet is actually taught. The default is "not covered" unless shown.
- **Consistency finders.** One per service group (networking, storage, databases, security, integration, compute, operations, cost). They read summaries, numbers and tables side by side, alongside script reports on token-usage clusters, duplicate paragraphs and cross-references. They loop until a round finds nothing new, three rounds at most; hitting the cap is logged.
- **Read-through panel.** Per Part: reader persona, AWS expert red-team ("find the ten statements most likely to be wrong") and exam coach.
- **Finding verification.** Every finding is checked by a skeptic before a fixer touches the text. Changed chapters re-run their gates.
- **Sampling audit.** 150 hard facts, seeded random. Sources are revalidated live and each fact is re-derived from scratch by fresh agents. If two or more fail, the audit expands to every hard fact in the affected chapters. The result is reported to her as a number.

## 16. Resilience, permissions, politeness (requirements 7 and 9)

**Permissions.** She must approve these as part of the plan, because an agent's message cannot authorise a permission change. Confirm exact syntax with the `update-config` skill.
```json
{"permissions":{
  "allow":["Bash(python3 aws-saa-book/tools/saa.py:*)",
           "Edit(/aws-saa-book/**)","Read(/aws-saa-book/**)","WebSearch"],
  "deny":["WebFetch","Bash(curl:*)","Bash(wget:*)","Bash(git add:*)","Bash(git commit:*)","Bash(git push:*)"]}}
```
- Agents call the tool as one simple command with that exact prefix.
- The deny rules also bind the orchestrator for the duration of the build.
- W0 begins with a two-agent canary that exercises write, tool call and search, and confirms nothing prompts.
- The first Artifact publish happens at about 1.5 h, so that prompt arrives while she is present.

**Politeness.**
- Each URL is fetched once: content-addressed cache, per-snapshot metadata files, no shared manifest.
- One request per second across all processes through a file lock; `robots.txt` enforced; backoff on 429 and 503.
- Expected total is about 3,400 requests over the whole build.
- The What's New and case-study APIs are bulk-harvested once.

**Resumability.**
- `stage begin` makes every stage idempotent.
- Chapter agents write only inside their chapter directory.
- Shared stores (facts, tables) change only through locked commands.
- Three failed attempts mark a chapter `blocked` without stopping the others.
- `_build/ledger/RUNBOOK.md` records the current wave, run IDs and the next action, so a fresh session can continue.
- The Mac must not sleep (keep it plugged in, or allow `caffeinate`).

**Orchestrator checks between workflows (a few thousand tokens per wave).**
1. `saa.py status`
2. `saa.py gate --all --quick`
3. `saa.py report wave W`
4. `saa.py audit sample --n 20`, and eyeball the 20 claim-and-quote pairs.
5. Read one random rendered section.
6. `build web`, smoke test, republish to the same Artifact, `build anki`, update README and CHANGELOG.

**Early delivery (requirement 6).**

| Time (est.) | She can read |
|---|---|
| ~1.5 h | Exam blueprint, how to use, study plan |
| ~2 h | Generated fact-sheet pages (verified facts only) for VPC, then IAM, S3 and EC2 as they verify |
| ~3.7 h | Full VPC chapter |
| ~6 h | IAM, S3, EC2 |
| ~9.5 h | Security wave |
| ~23 h | All deep chapters |
| ~45 h | Everything |

Because she starts early, every later correction to a published chapter appears in a "changed since you read it" list.

**Output builds.**
- **Web:** one HTML file, chapters lazy-rendered from embedded JSON, native Mermaid, progress in the `db` capability with `localStorage` as cache. In-progress mock state is saved on every answer, so a republish cannot lose it. Publish private, because it embeds quotes.
- **Anki:** genanki with deterministic GUIDs, so re-importing after each wave updates cards without losing scheduling. A TSV fallback is also built.
- **PDF:** pandoc to print HTML, then Chrome headless.
- **Diagrams:** Mermaid source compiled to SVG for Markdown and PDF. d2 is the close alternative if nested VPC layouts look poor in the exemplar.

## 17. Failure modes: top five risks, ranked

1. **The quote is real but the claim drifts** (default versus maximum, per-AZ versus per-Region, one storage class generalised to all).
   - Mitigations: number-subset check; mandatory qualifiers; script-attached table headers; entailment votes that default to reject; re-derivation for tier-0 facts; the 150-fact audit.
2. **Questions with a defensible second answer, hidden by same-model blind spots.**
   - Mitigations: three different lenses including citations and an ambiguity hunter; unanimity; one edit then reject; a second blind sitting per mock.
   - Optional: run one solver on a different model tier if the orchestrator confirms one is available.
3. **A 45-hour unattended run stalls or wastes work** (permission prompt, laptop sleep, context loss, resume miss).
   - Mitigations: canary; one allow rule; ledger-driven idempotent stages; wave-sized workflows; RUNBOOK; compact returns.
4. **Official sources are stale or disagree** (FAQ behind docs, new exceptions such as the Lambda 90-minute case).
   - Mitigations: tiering; conflict queue; change feed from two sources; currency vote; `freshen`.
5. **Correct but unread.** About 300,000 words against 40 study hours and a reader who skims, plus drift across 50 chapters.
   - Mitigations: budgets locked by the reader-persona judge; mandatory fast path; single-sourced tables and facts; duplicate-paragraph detection.

**Other failure modes.**
- **Labs unexecuted:** section 14 and the label.
- **Integrity:** as an AWS employee she should not have leaked-question sites anywhere in the pipeline. Topic emphasis comes from the exam guide, official materials and her diagnostic only.
- **Corrections after she has read a chapter:** CHANGELOG.
- **AWS throttling:** cache and backoff.
- **Fact ID collisions across concurrent chapters:** locked `facts add` with near-duplicate warnings.

## 18. Cost realism (requirement 10)

| Unit | Agents | Agent-minutes |
|---|---|---|
| Deep chapter | ~47 | ~420 |
| Medium chapter | ~33 | ~250 |
| Light chapter | ~18 | ~120 |

- **Totals:** 16 deep (752 agents), 19 medium (627), 8 light (144), synthesis and front matter (~95), exemplar extras (~16), foundation (~21 plus VPC mining), mocks (~90), review (~90), release (~6). That is about 1,850 agents and about 260 agent-hours.
- **Wall-clock:** about 45 hours at 8 slots and roughly 80% utilisation.
- **Biggest lever:** if the harness allows two workflows at once, mine facts for wave N+1 while writing wave N, for roughly 25–28 hours. The file locks already make that safe.

**Where lower effort is safe:** plan-stage fetching, finalize, build and smoke agents, card formatting, the quick difficulty solver, registry URL resolution. Miners can run at medium, because their output is mechanically checked and independently voted.

**Where it is not safe:** entailment and currency verifiers, adjudicators and judges (max), the registrar, writers, question writers, red-team reviewers and ambiguity hunters.

**Wasted-work controls:** demand-driven mining; exemplar slices instead of three full drafts; 20% over-production instead of top-up loops; hash-based gate skipping; span-level fixes.

## 19. Close calls

| Choice | Recommended | Alternative |
|---|---|---|
| Exemplar | VPC | IAM first if you weight her weakest area over template coverage |
| Chapter source | Token source rendered to clean Markdown | One file with hidden HTML-comment markers |
| Pipeline shape | Per-chapter pipelines with a shared canon | A global fact foundry before any writing |
| Diagrams | Mermaid | d2 |
| Mock split | 20/17/15/13 | 19/17/16/13 |

## 20. Assumptions I could not test read-only; W0 must validate them

- Workflow subagents inherit the project permission rules without prompting, and the rule syntax above is exact.
- `uv run --script` can reach PyPI from the Bash tool.
- The awscli in-process lint works; moto covers the lab APIs.
- genanki works on Python 3.12/3.13.
- Mermaid compiles to SVG through headless Chrome.
- Chrome's `@page` page numbers and PDF outline work.
- An 8 MB single-file app loads acceptably on her phone.
- What's New product tags exist for every in-scope service.
- Two workflows can run at once.
- Agent durations match the estimates. The W1 pilot measures them, and the orchestrator should re-forecast after it.

### Critical Files for Implementation
- aws-saa-book/tools/saa.py (to create: the single CLI behind every gate, fetch and build)
- aws-saa-book/_build/registry/book.json (to create: chapters, tiers, waves, budgets, sources; drives every workflow's args)
- aws-saa-book/_build/style/SPEC.json (to create in W1 with STYLE.md: the frozen anchor for all writers and lints)
- /Users/tatiatsmindashvili/Desktop/tatia/2026-plans/.claude/settings.json (to create with her approval: the narrow allow and deny rules)
- /Users/tatiatsmindashvili/Desktop/tatia/certification/study-plan.md (existing: her diagnostic, which sets the reader card and the security-first ordering)
