export const meta = {
  name: 'saa-foundation',
  description: 'W0 of the SAA-C03 Handbook build: tooling with tests, the authoring and tool contracts, the chapter registry, the corpus harvest and the diagram renderer with its pilot gate',
  phases: [
    { title: 'Canary', detail: 'check that background agents can write, run the tool, use uv and search' },
    { title: 'Contract', detail: 'content contract, tool contract, two critics, one fixer' },
    { title: 'Corpus tools', detail: 'fetch cache, then FAQ / change / case-study harvesters' },
    { title: 'Diagram renderer', detail: 'grid renderer core, then the other diagram kinds' },
    { title: 'Modules', detail: 'ledger, facts, registry, lint, question bank, tasks' },
    { title: 'Integrate', detail: 'end-to-end smoke test on real AWS pages, then gate breakers and fixes' },
    { title: 'Registry and corpus', detail: 'sources and exam-guide mapping per chapter, completeness check, harvest' },
    { title: 'Diagram pilot', detail: 'eight pilot diagrams and a visual judge' },
  ],
}

const ROOT = '.'   // the repository root; agents run with the repo root as their working directory

const H = `You are one agent in a multi-agent build of a study book, the "SAA-C03 Handbook", in the folder aws-saa-book/ of the repository in your working directory. Your working directory is the repo root.

READ FIRST: aws-saa-book/_build/spec/RULINGS.md. It is authoritative and its "Hard rules for every agent" bind you.

GROUND RULES
- Write only inside aws-saa-book/. Never run git. Never publish artifacts. Never install system software. Python packages only through "uv run --script <file>" with inline (PEP 723) dependencies, for helper scripts that live under aws-saa-book/tools/.
- Run commands one at a time as plain commands from the repo root, for example: python3 aws-saa-book/tools/saa.py <subcommand> ...   or   python3 aws-saa-book/tools/tests/run.py <module>. No cd, no pipes, no redirects, no chaining with && or ;. Use your file tools (Read, Write, Edit) for all file work, including creating folders by writing files into them.
- If a command is refused or asks for approval, do not retry it in another form. Note it in your result and continue with what you can do.
- Shared library: aws-saa-book/tools/saalib/common.py (paths, exit codes, JSON and JSONL helpers with locks, normalize_text and find_quote, emit, add_common_args, load_book). The dispatcher aws-saa-book/tools/saa.py loads every module aws-saa-book/tools/saalib/<name>.py (or package folder) that defines register(subparsers). Do not edit common.py or saa.py; if you need a change there, say so in your result.
- Reference paths as common.X at call time (never "from saalib.common import X") so tests can patch them. Tests and experiments must not touch real data: use a sandbox with the global option --book-dir aws-saa-book/_build/tmp/<sandbox-name> (a copy of the book layout), or patch the paths.
- Core code is standard library only and must run on the system python3 (3.14).
- Tests live in aws-saa-book/tools/tests/test_<module>.py (unittest) and run with: python3 aws-saa-book/tools/tests/run.py <module>. Every gate needs at least one "must fail" test: a bad input that the gate is required to reject.
- Keep your final answer short; it must fit the requested result fields. Put detail in files.
`

const CORPUS_RULING = `CORPUS LAYOUT (fixed; other modules code against it)
- source_id: a stable id made from the URL. docs.aws.amazon.com/<path>.html -> "docs/<path>" (no extension); aws.amazon.com/<path>/ -> "www/<path>"; d1.awsstatic.com/<path> -> "static/<path>"; repost.aws/<path> -> "repost/<path>"; API responses -> "api/<name>".
- Files under common.CORPUS / "snap": <source_id>.raw (bytes as fetched), <source_id>.txt (readable text: the Markdown itself for docs pages, visible text for HTML pages), <source_id>.meta.json with keys source_id, url (the canonical human URL to cite; .html for docs), fetched_url, final_url, status, content_type, etag, last_modified, sha256 (of raw), text_sha256, fetched_at, title, bytes.
- For a docs.aws.amazon.com page the tool fetches the .md twin of the .html URL (same path, .md extension), which is verbatim Markdown.
- A quote is verified with common.find_quote(quote, <text of the .txt file>).
- Python API in saalib/corpus.py: source_id_for(url) -> str; snapshot_paths(source_id) -> dict with raw, txt and meta paths; load_text(source_id) -> str or None; load_meta(source_id) -> dict or None; fetch(url, revalidate=False) -> meta dict (raises PolicyError for a host outside common.ALLOWED_HOSTS).
`

const S = {
  canary: { type: 'object', properties: { write_ok: { type: 'boolean' }, tool_ok: { type: 'boolean' }, uv_ok: { type: 'boolean' }, websearch_ok: { type: 'boolean' }, refused: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' } }, required: ['write_ok', 'tool_ok', 'uv_ok', 'websearch_ok'] },
  done: { type: 'object', properties: { ok: { type: 'boolean' }, files: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' }, problems: { type: 'array', items: { type: 'string' } } }, required: ['ok', 'summary'] },
  critique: { type: 'object', properties: { report_path: { type: 'string' }, blockers: { type: 'integer' }, majors: { type: 'integer' }, minors: { type: 'integer' } }, required: ['report_path', 'blockers', 'majors', 'minors'] },
  module: { type: 'object', properties: { module: { type: 'string' }, tests_pass: { type: 'boolean' }, tests_run: { type: 'integer' }, files: { type: 'array', items: { type: 'string' } }, deviations: { type: 'array', items: { type: 'string' } }, problems: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['module', 'tests_pass'] },
  judge: { type: 'object', properties: { verdict: { type: 'string', enum: ['pass', 'fail'] }, average: { type: 'number' }, worst_defects: { type: 'array', items: { type: 'string' } }, report_path: { type: 'string' } }, required: ['verdict', 'average'] },
}

const brief = r => r ? { ok: (r.ok !== undefined ? r.ok : r.tests_pass), module: r.module, tests_run: r.tests_run, summary: String(r.summary || '').slice(0, 280), problems: (r.problems || []).slice(0, 4).map(x => String(x).slice(0, 200)), deviations: (r.deviations || []).slice(0, 4).map(x => String(x).slice(0, 200)) } : null

// ---------------------------------------------------------------- prompts

const canaryPrompt = i => `${H}
YOUR TASK: permission canary number ${i}. Do exactly these four things and report what happened for each.
1. With your Write tool, create aws-saa-book/_build/tmp/canary-${i}.txt containing the word ok.
2. Run: python3 aws-saa-book/tools/saa.py ping
3. With your Write tool, create aws-saa-book/tools/tests/canary_uv_${i}.py with exactly this content:
# /// script
# requires-python = ">=3.12"
# dependencies = ["markdown-it-py==3.0.0"]
# ///
import markdown_it
print("uv ok", markdown_it.__version__)
   Then run: uv run --script aws-saa-book/tools/tests/canary_uv_${i}.py
4. Use WebSearch (load it with ToolSearch "select:WebSearch" if it is not loaded) for: NAT gateway basics site:docs.aws.amazon.com
Report whether each step succeeded, and list any step that was refused or seemed to wait for approval.`

const contentContractPrompt = `${H}
YOUR TASK: write the CONTENT CONTRACT that every writer agent and every checking script will follow. Everything downstream depends on it, so be precise, complete and concrete. Where the planning reports disagree, RULINGS.md decides.

Read fully before writing:
- aws-saa-book/_build/spec/RULINGS.md and aws-saa-book/_build/style/READER.md
- aws-saa-book/_build/spec/LEARNING.md (all of it; this is the pedagogy specification)
- aws-saa-book/_build/spec/PRODUCT.md sections 2 (the Claude features need key points on spoken-answer items), 3 (data shapes), 4 (Markdown authoring conventions) and 5 (diagram kinds and style guide)
- aws-saa-book/_build/spec/PIPELINE.md sections 5, 6, 11, 13 and 14
- aws-saa-book/_build/registry/book.seed.json (chapter ids, tiers, kinds)
- For the style she already uses: aws-saa-book/_build/spec/existing/style-sample-cheat-sheet.md and style-sample-talk-track.md

Write these files:

1. aws-saa-book/_build/style/CONVENTIONS.md (the authoring contract; at most about 4,500 words; it will be given to every writer, so it must stand alone). It must define, each with the exact syntax and one small filled example:
   a. The chapter folder for each tier and kind (deep, medium, light family, front, pattern, synthesis, mock): exact file names, and which files are hand-written Markdown and which are generated. Ruling: in service chapters only 1-fast.md and 2-deep.md are hand-written prose. 3-do.md, 4-say.md, 5-quiz.md and sources.md are generated by the tool from JSON in aws-saa-book/data/<NN-slug>/ (tasks.json, speak.json, questions.json, cards.json) and from the facts the chapter links to. Decide the file lists of front, pattern, synthesis and mock chapters from LEARNING.md sections 1.5 and 11.
   b. YAML front matter for 1-fast.md (chapter metadata: id, slug, title, tier, domains, tasks, services, minutes for the Fast, Pass and Full routes, status, updated) and for the other hand-written files.
   c. For every hand-written file, the ordered sections with exact H2 heading text and a stable role id, following LEARNING.md section 1 (Predict, Look first, In one breath, Words that go together, Choose it or not, Signals and traps, Changed recently, Check, Recap from memory; then How it works, Numbers that decide answers, the startup's decision record, FAQ quick-fire, In the real world). Give the section-flag comment syntax that carries role, route and minutes.
   d. The exact Markdown shape of every device: Predict and Check items; the one-breath definition; the collocation table; comparison tables that end in a deciding question; the signals table (stem says, think, because, but not if) and the traps list with trap ids; Changed recently entries (old, now, since, what the exam probably expects, examinable or not yet); Recap from memory; a How-it-works subsection (assertion heading with a time box, body, Stop and answer in a details block); collapsed Go deeper blocks for edge cases; the numbers table (A-list and B-list); the decision record; a FAQ quick-fire item (the can-or-cannot question, the short answer, then the verbatim FAQ sentence as an AWS quote block with its link); the real-world case box; "Predict the picture" before a diagram; "Spot the bug".
   e. The fixed set of callout labels (reconcile the five in LEARNING.md 4.5 with the twelve in PRODUCT.md 4 into one final list) and the callout syntax.
   f. Fact links: syntax [value](../facts/<service>.md#<fact-id>), when one is required, the rule that the link text must contain the canonical value string, which section roles are exempt (example, task, worked), and how a writer asks for a missing fact (the fact request queue) instead of writing an ungrounded sentence.
   g. Tables (kind comment, column and cell limits), code blocks, cross-references between files and chapters, heading and anchor rules, glossary terms.
   h. Diagram embeds: the image syntax pointing at ../diagrams/svg/<diagram-id>.svg, id naming, the caption (a claim sentence) and the numbered step list under it. Do not define the diagram spec itself; the diagram module owns it (aws-saa-book/_build/style/TOOLS-diagram.md, being written by another agent).
   i. ID formats, all kebab-case: fact ids <service>-<topic>[-<detail>], question ids <slug>-q001, card ids, speak ids, task ids, trap ids, diagram ids, concept tags.
   j. A short summary of each JSON item shape (the schemas below are the authority).
   k. An appendix "Decisions" that lists every conflict between the planning reports that you resolved, one line each.

2. aws-saa-book/_build/style/SPEC.json (machine-readable, "version": "0.9"): for every tier and kind, the files, and for each hand-written file the ordered sections with id, heading, role, required flag, route and word limits; whole-file word limits (use the budgets in RULINGS.md, with the XL override for IAM, VPC, S3 and EC2); the counts per tier (questions shipped, core and extended, twin pairs, multiple-response range, spoken prompts, cards, tasks by type); the callout labels; table kinds; lint parameters (average and maximum sentence length, paragraph limits, the absolute-word list, the banned-word map with replacements, the allowed phrasal verbs, the raw-HTML allow-list); question parameters (stem, option and explanation word ranges, difficulty mix, multiple-response share); spoken-answer parameters. Every rule that a script can check must be expressed here as data, because the lint is driven by this file and the judging panel in the next workflow may change values.

3. aws-saa-book/_build/style/STYLE.md ("version 0.9", at most about 2,800 words): the writing rules for writers, taken from LEARNING.md sections 3 to 9: sentences and paragraphs, vocabulary and term introduction, the avoid list, pronunciation respelling, formatting and tone; spoken-answer script rules and the four-move pattern; the question-writing standard (stem anatomy, distractor rules, explanation format, think-aloud format, failure modes); hands-on task rules; flashcard atomicity rules. Include the filled examples from LEARNING.md.

4. JSON Schemas (draft 2020-12) in aws-saa-book/_build/schemas/: question.schema.json, card.schema.json, speak.schema.json, task.schema.json, terms.schema.json, exam-english.schema.json. The question shape must carry everything the web app in PRODUCT.md needs (per option: text, correct flag, why, concept, misconception or trap id; stem; keywords or deciding phrases; explanation; takeaway; the "if the stem said ... instead" twin line; facts; sources; domain; task; bullets; topics; difficulty; type; select; layer core or extended; twin_of; rev and keyRev; status and a verification block). The speak shape must carry prompt, persona, ten_second, sixty_second (as lines), skeleton, key points with id and must or nice, must_not_say, terms, follow_ups, facts. The task shape must carry type (look, try or lab), title, the misconception it kills, time, cost line, what it costs per day if forgotten, permissions needed, a read-only alternative, steps (text plus optional command, expected result, and a break-it flag), cleanup steps, a verify command, the "still costs money if left" list, and the label "checked against docs, not run in a real account".

5. aws-saa-book/data/terms.json (the controlled vocabulary seed: at least 60 terms with official term, allowed short form, banned variants, respelling where pronunciation is hard, plain meaning, collocations, do-not-confuse) and aws-saa-book/data/exam-english.json (the 90 exam-English words and phrases of LEARNING.md 4.6 in nine groups of ten: word or phrase, plain meaning, what it signals, a stem fragment that uses it). English only.

6. A fixture for the tool tests under aws-saa-book/tools/tests/fixtures/book/ (a miniature book layout): data/book.json with one deep chapter 99-sample about an invented service "Amazon Widget Store" (invented, so that no real AWS fact is implied); 99-sample/1-fast.md and 99-sample/2-deep.md that use EVERY device and section in a few sentences each; data/99-sample/questions.json (4 questions including one twin pair and one multiple-response), cards.json (3), speak.json (1), tasks.json (one look, one try with cleanup); a corpus snapshot _build/corpus/snap/docs/fixture/widget-store/limits.txt with its .meta.json (an invented page of about 20 lines including one table) and data/facts/widget.jsonl with 6 facts that quote it verbatim (follow the fact shape in PIPELINE.md section 5 with kebab-case ids; the tool contract agent will formalise that schema right after you and must stay compatible with your fixture); plus _build/style/SPEC.json for the fixture with the same structure as the real one but tiny word limits so that the miniature chapter passes. The fixture must conform completely to CONVENTIONS.md: it is the reference example that implementers test against.

Quality bar: a writer who has only CONVENTIONS.md, STYLE.md and SPEC.json must be able to produce a chapter that passes lint without guessing, and an implementer must be able to write the lint and the web build from them without asking questions. Prefer exact strings over descriptions.

Result: the files you wrote and any open questions.`

const toolContractPrompt = `${H}
${CORPUS_RULING}
YOUR TASK: write the TOOL CONTRACT: the complete command-line and data contract for aws-saa-book/tools/saa.py, so that several implementers can build modules in parallel and the modules fit together.

Read fully before writing:
- aws-saa-book/_build/spec/RULINGS.md
- aws-saa-book/_build/spec/PIPELINE.md (all of it; sections 4, 5, 6, 7, 8, 10, 11, 13, 14, 15 and 16 are your main source)
- aws-saa-book/_build/spec/PRODUCT.md section 4 (sync and lint behaviour) and section 8 (build scripts; reserve their subcommands)
- The content contract written just before you: aws-saa-book/_build/style/CONVENTIONS.md, SPEC.json, STYLE.md, aws-saa-book/_build/schemas/*.json, and the fixture under aws-saa-book/tools/tests/fixtures/book/
- aws-saa-book/tools/saalib/common.py and aws-saa-book/tools/saa.py (already written; fixed)
- If they exist yet: aws-saa-book/_build/style/TOOLS-corpus.md, TOOLS-feeds.md, TOOLS-diagram.md. Other agents are implementing those modules right now and own those documents; reference them, do not redefine them.

Module ownership (fixed):
- saalib/ledger.py: stage, gate, status, report, selftest
- saalib/corpus.py: fetch, guide, search, show, tables (in progress; its owner writes TOOLS-corpus.md)
- saalib/feeds.py: faq, changes, cases (in progress; its owner writes TOOLS-feeds.md)
- saalib/facts.py: facts (add, adopt, verify, batch, packet, vote, finalize, card, request, amend, conflicts, render, list, show), audit, freshen
- saalib/registry.py: registry (build, set, check, show, wave-args), coverage
- saalib/lint.py: lint, sync
- saalib/qbank.py: q (add, lint, pack, adjudicate, dedupe, list), cards (add, lint), speak (add, lint), mocks (assemble, check), drills
- saalib/lab.py: tasks (add, lint, check-cli, emulate)
- saalib/diagram/ (package): diagram (in progress; its owner writes TOOLS-diagram.md)
- reserved for later: saalib/site.py (build web), saalib/exports.py (build anki, build pdf, build readme)

Write:
1. aws-saa-book/_build/style/TOOLS.md (at most about 6,500 words). For every subcommand of the modules ledger, facts, registry, lint, qbank and lab: arguments, exact behaviour, the files it reads and writes, the JSON it prints, exit codes, and the must-fail cases its tests have to include. Also define:
   - Data locations (per RULINGS.md: structured sources under aws-saa-book/data/, generated reader files at the book root, caches and ledger under aws-saa-book/_build/).
   - The fact lifecycle (candidate, mech-pass, verified, disputed, rejected, superseded); the mechanical checks from PIPELINE.md section 6 adapted to RULINGS.md (facts are referenced by Markdown links, not tokens); how votes are recorded and how "finalize" computes status from votes by fixed rules; what "packet" gives a verifier; how "amend" finds dependents; the fact request queue; the generated fact sheet facts/<service>.md (one anchor per fact id; claim; the exact AWS sentence; link to the AWS page; date checked; change note).
   - Chapter lint as a numbered list of blocking rules and warnings, each tied to SPEC.json keys: structure, word budgets, fact links (resolve, verified, value match), the bare-number and absolute-word rule with role exemptions, callouts, tables, cross-references, diagram references, style rules, terminology.
   - "sync": how 3-do.md, 4-say.md, 5-quiz.md, sources.md, facts/<service>.md and glossary.md are generated from JSON, and "sync --check".
   - Question bank: add, mechanical lint (LEARNING.md 6.7 and PIPELINE.md 13), blind packs (keys stripped, options permuted per solver), the adjudication rule, duplicate detection, coverage tags; cards and speak lint; mock assembly (seeded, domain split 20/17/15/13, every task statement present, no chapter question reused, no volatile items) and mock check; drills.
   - Task and lab lint (required fields, secure-by-default rules, cleanup pairing, tags, cost line), the CLI check against the AWS CLI command model through a uv helper script, optional emulation.
   - The ledger: stage begin and end semantics (SKIP, GO, BLOCKED; input hashes; three attempts), gate records, chapter status values, "status", "report wave", "gate CH" and "gate --all --quick", and the stage names of the per-chapter pipeline in PIPELINE.md section 10 as adapted by RULINGS.md.
   - Registry: how "registry build" parses the exam guide pages into bullet ids such as 1.2.K3 and 1.2.S1 and into the in-scope and out-of-scope service lists; how data/book.json is created from the seed; how "registry set" merges sources and mappings per chapter under a lock; what "registry check" verifies; the compact JSON printed by "registry wave-args"; the coverage matrix.
   - Audit sample and freshen.
2. JSON Schemas in aws-saa-book/_build/schemas/: fact, vote, fact-request, book (the registry), exam-guide, services, ledger-chapter, gate, change-item, case-item, mock. Stay compatible with the fixture facts already written; if the fixture has to change, change it and say so.
3. Extend the fixture where the tool needs it (for example a fixture ledger, an exam-guide excerpt, vote files), and write aws-saa-book/tools/tests/fixtures/README.md that explains how tests copy the fixture into a sandbox and run the CLI with --book-dir.

Be exact: the implementer of one module must be able to work from their section alone. Give JSON examples. Do not leave choices open; decide.

Result: the files you wrote and any open questions.`

const CRITICS = [
  { key: 'writer', lens: 'You are a WRITER who must produce a deep chapter (IAM) using only CONVENTIONS.md, STYLE.md and SPEC.json. Find every place where you would have to guess: a device with no exact syntax, an example that contradicts a rule, a heading that differs between files, a budget that cannot hold the required devices, a rule you cannot follow for a pattern, front or synthesis chapter, a JSON field whose meaning is unclear, a missing way to do something LEARNING.md requires (twin questions, trap ids, deciding phrases, think-alouds, must-say facts, break-it steps, return questions, the exam-English coverage rule).' },
  { key: 'implementer', lens: 'You are an IMPLEMENTER who must write the lint, the sync generator, the facts module and the question bank from TOOLS.md, SPEC.json, the schemas and the fixture. Find every contradiction between TOOLS.md, CONVENTIONS.md, SPEC.json, the schemas, the fixture and RULINGS.md; every rule that cannot be checked mechanically as written; every subcommand whose inputs, outputs or exit codes are ambiguous; every schema field that the web app in PRODUCT.md sections 2 to 4 needs but the schemas lack; every place where the fixture does not conform. Check that every JSON file parses (you may write a small script under aws-saa-book/tools/tests/ and run it with python3).' },
]
const criticPrompt = c => `${H}
YOUR TASK: adversarial review of the contract documents before anyone builds on them. ${c.lens}

Read: aws-saa-book/_build/spec/RULINGS.md; then aws-saa-book/_build/style/CONVENTIONS.md, STYLE.md, SPEC.json and TOOLS.md, every file in aws-saa-book/_build/schemas/, the fixture under aws-saa-book/tools/tests/fixtures/, and the relevant parts of aws-saa-book/_build/spec/LEARNING.md, PRODUCT.md and PIPELINE.md to check against.

Write your findings to aws-saa-book/_build/reports/contract-critique-${c.key}.md as a numbered list. For each finding give: severity (blocker = two agents would build incompatible things, or a required thing is impossible; major = likely rework; minor), the file and place, what is wrong, and the exact change you propose. Do not edit the contract files yourself. When unsure, report it.

Result: the report path and the counts by severity.`

const contractFixPrompt = `${H}
YOUR TASK: apply the review findings to the contract documents.
Read aws-saa-book/_build/reports/contract-critique-writer.md and contract-critique-implementer.md (if one is missing, continue with the other), then RULINGS.md, then the contract files they refer to (aws-saa-book/_build/style/CONVENTIONS.md, STYLE.md, SPEC.json, TOOLS.md, aws-saa-book/_build/schemas/, the fixture under aws-saa-book/tools/tests/fixtures/, aws-saa-book/data/terms.json and exam-english.json).
Fix every blocker and every major finding in the files, keeping all documents consistent with each other and with RULINGS.md; fix minor findings when the fix is cheap. Where two findings conflict, decide and record why. After editing, re-read the changed parts once to check that examples, schemas, SPEC.json and the fixture still agree. Write aws-saa-book/_build/reports/contract-fix.md with one line per finding: "fixed", "rejected (reason)" or "deferred (reason)".
Result: counts fixed, rejected and deferred, and the files changed.`

const corpusPrompt = `${H}
${CORPUS_RULING}
YOUR TASK: implement the corpus module, aws-saa-book/tools/saalib/corpus.py, with the subcommands fetch, guide, search, show and tables. This is the only network path for evidence in the whole build, so it must be polite, cached and strict.

Read: aws-saa-book/_build/spec/RULINGS.md; aws-saa-book/_build/spec/PIPELINE.md sections 2 (what was tested on the real AWS sites), 4 (subcommand table), 6 (corpus and tiers) and 16 (permissions and politeness); aws-saa-book/_build/spec/SOURCES.md Part 5 (notes on FAQ pages, llms.txt and .md twins).

Requirements:
- fetch URL... [--batch FILE] [--revalidate] [--binary-to PATH]: only hosts in common.ALLOWED_HOSTS (exit code 4 otherwise); obey robots.txt (cached per host); at most one request per second across ALL processes, enforced with a lock file plus timestamp under common.CORPUS; retry with backoff on 429 and 5xx (exit 5 if it still fails); a daily request cap (default 6,000) recorded on disk; a browser-like User-Agent; follow redirects only within the allow-list and record final_url. For a docs.aws.amazon.com .html URL fetch the .md twin and store it as the snapshot text; if the twin is missing, fall back to the HTML and extract visible text. For other HTML pages extract visible text with the standard library html.parser (drop script, style, nav, header and footer; keep headings, paragraphs, list items and table rows on their own lines; keep link text). JSON responses are stored as they are. Store raw, txt and meta as in the corpus layout. A cached snapshot is returned without a request unless --revalidate is given (then use If-None-Match and If-Modified-Since, and keep the old snapshot on 304). Print source_id and paths; never print the page body. Append one line per request to common.CORPUS / "fetch.log.jsonl". --binary-to saves a binary download (for example the AWS icon zip) to a path inside the book.
- guide ROOT: fetch <root>/llms.txt and <root>/full.md (store full.md under common.CORPUS / "full"); write common.CORPUS / "index" / <guide-id>.json with the page list (title, url, md url, source_id) and best-effort pointers to the guide's document-history page and its quotas or limits page (match by link text and title; names differ per guide).
- search PATTERN [--scope full|snap|faq|changes|cases|all] [--guide ID] [--regex] [--limit N]: bounded search over saved text; each hit gives the source_id (or the guide id plus nearest heading for full.md), the line number and about 200 characters of context.
- show SOURCE [--around TEXT] [--lines A:B] [--chars N]: a bounded excerpt of a snapshot, so that agents do not read whole files.
- tables SOURCE [--index N]: parse the Markdown tables in a snapshot into rows keyed by the header cells, with the header row text and the nearest preceding heading, so that a limit can be quoted together with its column header.
- The small Python API described in the corpus layout, for other modules.
- All subcommands take the common options (--out, --max-lines, --json).
Tests (aws-saa-book/tools/tests/test_corpus.py): offline by default (patch the opener); cover the allow-list refusal, the robots refusal, the .md twin logic, a cache hit, a 304 revalidation, visible-text extraction, table parsing with headers, search bounds, and that fetch never prints a page body. You may make at most 15 real requests in total to check behaviour against the live sites (for example the VPC user guide llms.txt, the nat-gateway-basics page, the VPC FAQ page).
Document the final CLI and Python API, with examples, in aws-saa-book/_build/style/TOOLS-corpus.md.

Result: module name, whether all tests pass, counts, files written, deviations from this brief.`

const feedsPrompt = `${H}
${CORPUS_RULING}
YOUR TASK: implement aws-saa-book/tools/saalib/feeds.py with the subcommands faq, changes and cases, on top of the corpus module (aws-saa-book/tools/saalib/corpus.py and aws-saa-book/_build/style/TOOLS-corpus.md, just written by another agent; use its fetch function for every request).

Read: RULINGS.md; aws-saa-book/_build/spec/PIPELINE.md sections 2 (tested findings: the What's New JSON API, the two FAQ markups, the document-history page names, the case-study directory API), 4 and 7; aws-saa-book/_build/spec/SOURCES.md Part 5.

Requirements:
- faq URL [--list] [--find TEXT]: fetch through corpus, then parse questions and answers with two parsers (embedded JSON items with itemHeading and itemLongLoc; legacy "Q:" paragraphs) and write common.CORPUS / "faq" / <name>.jsonl with question, answer text, section heading and position. The visible-text snapshot stays the evidence base; the parsed file is a convenience index. Handle the Aurora FAQ, which now redirects to the docs guide "auroraextendedcontent". Record the final URL.
- changes harvest --tag PRODUCT_TAG --service NAME [--since 2022-07-01] and changes history URL --service NAME: harvest What's New items through the JSON API by product tag (page size up to 1000, stop at the paging limit, filter by date in the script, never crawl old post pages that robots.txt disallows) and parse a guide's document-history page (a Markdown table) into dated rows; store common.CORPUS / "changes" / <service>.jsonl with date, title, summary, url and source (whatsnew or history). "changes for SERVICE [--since DATE]" prints a bounded list. "changes tags [--find TEXT]" lists the product tags the API knows, so that other agents can map services to tags.
- cases harvest [--tag TAG] and cases for TAG: the customer-references directory API with product tags; store title, customer, url, date, tags, summary. Quotes for the book always come from a fetched page snapshot, never from this index.
- Common options on every subcommand; bounded output; exit codes per common.py.
Tests (test_feeds.py): offline, against small saved samples of each markup that you capture once (keep them small); at most 20 live requests in total for checking.
Document the CLI in aws-saa-book/_build/style/TOOLS-feeds.md.

Result: module name, tests status, files, deviations.`

const diagramCorePrompt = `${H}
YOUR TASK: build the core of the diagram system: a declarative JSON spec rendered by our own grid renderer to SVG. Package aws-saa-book/tools/saalib/diagram/ with register(subparsers) in __init__.py; subcommand "diagram" with the actions build, lint, preview, shot, sheet and icons.

Read: RULINGS.md; aws-saa-book/_build/spec/PRODUCT.md section 5 in full (choice, spec, kinds, renderer modules, CLI, style guide, QA loop, dark mode and phones) and the token list in section 7 (the --dg-* tokens); aws-saa-book/_build/style/READER.md.

Your scope is the "arch" kind and everything shared:
- The spec schema aws-saa-book/_build/schemas/diagram.schema.json and its validation (standard library; write a small validator, do not depend on jsonschema).
- layout_grid.py (columns and rows, nested groups with a gutter lane per nested border and a label band per group); route.py (orthogonal edges through gutter mid-lines, port spreading, edge labels, numbered step badges, emphasis); textmetrics.py (real advance widths: generate a width table once for a common system font such as Arial or Helvetica with fontTools through a uv helper script, commit the table as a Python dict with a safety margin; the runtime stays standard library); svg.py with render_standalone (light palette baked in, opaque ground, icons embedded; for the Markdown preview, PDF and Anki) and render_inline (classes bound to the --dg-* tokens, no ids, icons by <use>; for the web app); lint.py (the limits from the style guide, and geometry: text fits its node, labels do not overlap, no edge crosses a node, crossings counted).
- Icons: "diagram icons" downloads the official AWS Architecture Icons package once (find the zip link on https://aws.amazon.com/architecture/icons/ ; if the corpus module offers a binary download use it, otherwise use urllib restricted to d1.awsstatic.com), unpacks it under common.TMP / "aws-icons", and builds aws-saa-book/diagrams/icons.json (name to cleaned SVG) for the services and resources this book needs: all services in aws-saa-book/_build/registry/book.seed.json plus generic items (user, users, client, server, internet, corporate data center, mobile client) and resource icons (internet gateway, NAT gateway, route table, endpoint, network interface, bucket, object, instance, Auto Scaling group, the load balancer types, Lambda function, queue, topic, table, role, policy, key, and similar). Use the official icons unmodified. Record the package release and AWS's usage statement in aws-saa-book/diagrams/ICONS-NOTICE.md.
- Group types with the AWS conventions (Region, VPC, Availability Zone, public subnet, private subnet, security group, Auto Scaling group, account, corporate data center, generic), each with a distinct border style as well as a colour.
- preview and shot: write a four-panel HTML page (desktop width and 368 px wide, light and dark) under common.TMP / "diagram-preview" and screenshot it to PNG with headless Chrome (path in common.CHROME; call it with subprocess from inside the tool, with flags such as --headless=new --screenshot=<png> --window-size=W,H --hide-scrollbars). sheet: one contact-sheet PNG of all diagrams. Also provide "diagram shot --file <any .html or .svg inside the book> --out <png> [--width W --height H --dark]" because other agents need screenshots of pages.
- Output files: specs in aws-saa-book/diagrams/src/<id>.json, standalone SVGs in aws-saa-book/diagrams/svg/<id>.svg.
- Tests (test_diagram.py): schema must-fail cases; geometry must-fail cases (overlap, overflow, an edge through a node); deterministic output (the same spec gives the same bytes); a golden test on one sample.
Then prove it. Write two sample specs yourself (a two-AZ VPC with public and private subnets, an internet gateway, NAT gateways and an S3 gateway endpoint; a three-tier web application with a numbered request flow), build them, take the screenshots, LOOK at the PNG files with your Read tool, and fix the renderer until both are clean in all four panels: no overlap or clipping, arrows end on node edges, labels readable at phone width, consistent spacing, official icons, a professional AWS look.
Document the spec for diagram authors, with both samples, in aws-saa-book/_build/style/TOOLS-diagram.md, including the style guide (must have, must not have) from PRODUCT.md section 5.

Result: tests status, the sample PNG paths, what is not supported yet, deviations.`

const diagramKindsPrompt = `${H}
YOUR TASK: extend the diagram system with the remaining kinds. The core (the arch kind, shared SVG, lint, icons, preview and shot) was just built by another agent: read aws-saa-book/_build/style/TOOLS-diagram.md and the code in aws-saa-book/tools/saalib/diagram/ first, and keep its visual language.

Read also: aws-saa-book/_build/spec/PRODUCT.md section 5 (kinds table, style guide, QA loop).

Add, each in its own layout file, with schema support, lint rules and tests:
- sequence (lifelines, at most 5 actors, numbered messages, optional notes; for flows such as AssumeRole, a presigned URL, envelope encryption)
- ladder (a decision tree: a vertical spine of questions, answers branch to the right, at most 6 rungs)
- compare (two or three small arch panels side by side that stack on phones; emitted as separate SVGs plus a wrapper)
- states (a lifecycle with state shapes and labelled transitions)
- timeline (an axis with lanes; for S3 lifecycle transitions, RPO and RTO)
- raw (a hand-written SVG that is checked only for the shared classes and size)
For each kind write one sample spec, build it, screenshot it, LOOK at the PNG with your Read tool, and fix until it is clean in all four preview panels. Update aws-saa-book/_build/style/TOOLS-diagram.md with the spec of each kind and its sample. Do not break the arch kind: run the full diagram tests at the end.

Result: tests status, sample PNG paths, the limits of each kind, deviations.`

const ledgerPrompt = `${H}
YOUR TASK: implement aws-saa-book/tools/saalib/ledger.py: the subcommands stage, gate, status, report and selftest, exactly as specified in aws-saa-book/_build/style/TOOLS.md (read all of TOOLS.md once, then your section closely) and the schemas ledger-chapter and gate in aws-saa-book/_build/schemas/. "gate" composes checks owned by other modules (lint, facts, q, tasks, diagram): call them through their Python functions when the modules are present, and report "check unavailable" (exit 3) when one is missing, so that this module can be finished before the others. "selftest" runs the unit tests (it wraps aws-saa-book/tools/tests/run.py) and reports per module.
Tests in test_ledger.py, including the must-fail cases: stage end when the gate fails; a fourth attempt is BLOCKED; a stale gate is detected when an input file hash changes; SKIP when the inputs are unchanged.
Result: tests status, files, deviations from TOOLS.md (with the reason).`

const BUILDERS = [
  { name: 'facts', file: 'aws-saa-book/tools/saalib/facts.py', extra: 'The mechanical checks decide what may ever be stated as a fact in this book. Implement every check of PIPELINE.md section 6 as adapted in TOOLS.md. In particular: the quote must be found by common.find_quote in the snapshot text; every number and unit in the claim and in the display values must appear in the quote (TB and TiB are different units; map number words to digits); limits, quotas and defaults must carry scope, default-or-max and adjustable; a table-row quote gets its header row attached by script. Must-fail tests: a paraphrased quote, a wrong number, a unit mismatch, a quote from navigation text, a host outside the allow-list, a missing qualifier, a fact finalized without the required votes, a hand-edited status.' },
  { name: 'registry', file: 'aws-saa-book/tools/saalib/registry.py', extra: 'The exam guide lives at https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/ (pages solutions-architect-associate-03, solutions-architect-associate-03-domain1 to -domain4, saa-technologies-concepts, saa-service-mentions, saa-03-in-scope-services, saa-03-out-of-scope-services). Test the parsing offline against small saved excerpts; the real build runs later. The seed is aws-saa-book/_build/registry/book.seed.json.' },
  { name: 'lint', file: 'aws-saa-book/tools/saalib/lint.py', extra: 'The lint is driven by SPEC.json (never hard-code headings or limits). Must-fail tests, each on a sandbox copy of the fixture with one defect injected: a missing required section; sections out of order; a file over its word limit; a fact link to an unknown fact; a fact link whose text does not contain the canonical value; a link to an unverified fact; a bare number with a unit in an explanatory section; an absolute word without a fact link; an unknown callout label; a banned word; a sentence over the maximum; a broken cross-reference; a missing diagram file; stale generated files (sync --check).' },
  { name: 'qbank', file: 'aws-saa-book/tools/saalib/qbank.py', extra: 'Must-fail tests: a wrong option count; a multiple-response question whose select count does not match its keys or its "(Select TWO.)" text; a key much longer than the other options; an explanation that names an option letter; a duplicate signature; a near-duplicate stem; a fact id that does not resolve; a blind pack that still contains the key; an adjudication with one dissenting solver that still passes; a mock with the wrong domain split or with a reused chapter question; a card with a list answer; a 60-second answer far over the word limit.' },
  { name: 'lab', file: 'aws-saa-book/tools/saalib/lab.py', extra: 'The CLI check validates each aws command against the AWS CLI command model offline, through a helper script with inline dependencies run by uv (awscli or botocore: decide which gives reliable validation of service, operation and parameter names without credentials and without network calls to AWS). Emulation with moto is optional: implement it only if it is quick and reliable, otherwise mark it "not supported" honestly. Must-fail tests: a create without a matching delete; a missing cost line; a missing verify step; a security group rule that opens port 22 or 3389 to 0.0.0.0/0 or ::/0; a public bucket setting; an access key creation; a missing tag; an unknown CLI option.' },
]
const builderPrompt = b => `${H}
${CORPUS_RULING}
YOUR TASK: implement ${b.file} exactly as specified in aws-saa-book/_build/style/TOOLS.md (read all of TOOLS.md once, then your section closely), the schemas in aws-saa-book/_build/schemas/, and for content rules aws-saa-book/_build/style/CONVENTIONS.md and SPEC.json. Use the fixture under aws-saa-book/tools/tests/fixtures/ (see its README) for tests.
${b.extra}
Write the tests in aws-saa-book/tools/tests/test_${b.name}.py, including the must-fail cases that TOOLS.md lists for your subcommands, and run them until they pass: python3 aws-saa-book/tools/tests/run.py ${b.name}. Other modules are being written at the same time by other agents; code against their documented Python API and guard imports, so that your module loads and its tests pass even if another module is not there yet.
Result: tests status, files, deviations from TOOLS.md (with the reason).`

const integrationPrompt = `${H}
${CORPUS_RULING}
YOUR TASK: integrate the tool and prove it end to end. All modules have just been written by different agents: ledger, corpus, feeds, facts, registry, lint, qbank, lab and the diagram package. Read aws-saa-book/_build/style/TOOLS.md and the TOOLS-*.md files.

1. Run the whole test suite (python3 aws-saa-book/tools/tests/run.py). Fix failures and cross-module mismatches. You may edit any module; keep each fix minimal and add a regression test.
2. A real end-to-end smoke test in a sandbox book directory (aws-saa-book/_build/tmp/smoke/, used through --book-dir) with real AWS pages: fetch https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-basics.html and the VPC quotas page; add four facts with real verbatim quotes (one through the table path, "adopt"); run the mechanical verification; record votes; finalize; render the fact sheet; write a tiny chapter file that links those facts; run sync and lint (must pass); put a wrong number into one link text (lint must fail); add two questions, build a blind pack, adjudicate; lint a small task; build one diagram; run a stage begin and end cycle; print status.
3. The real registry: run the registry build against the live exam guide pages in the REAL book directory, so that aws-saa-book/data/book.json, the exam guide file and the services file exist (expect 4 domains, 14 task statements, about 189 knowledge and skill bullets and about 118 in-scope services; report the real counts). Do not map chapters; other agents do that next.
4. Make sure python3 aws-saa-book/tools/saa.py selftest passes and python3 aws-saa-book/tools/saa.py status runs.
Write aws-saa-book/_build/reports/w0-integration.md (what you ran, what you fixed, what still does not work).

Result: suite status, registry counts, fixes made, open problems.`

const BREAKERS = [
  { key: 'grounding', scope: 'the grounding gates: fact add and verify, vote and finalize, the fact-link rules in lint, sync --check, amend. Example attacks: a fabricated quote; a quote stitched from two sentences; a real quote with a claim that carries a different number or unit; default versus maximum confusion; a quote taken from navigation text or a table header; a fact whose snapshot hash no longer matches; a link text that hides the number in words; a bare number disguised with a non-breaking space or written as a word ("five"); an absolute claim split across two sentences; giving a section an exempt role to hide a fact; a claim hidden in an HTML comment or a details block; editing the facts file by hand to set status verified without votes.' },
  { key: 'practice', scope: 'the practice gates: question add and lint, blind packs, adjudication, mock assembly and check, cards and speak lint, task lint and CLI check, diagram lint. Example attacks: two correct options marked as a single-answer question; a multiple-response item with one key; the key leaked through option length or through word overlap with the stem; an explanation that names an option letter; a near-duplicate of an existing question with reordered words; a blind pack from which the key can be recovered (option order, ids, rationale text); an adjudication file with a missing solver; a mock that reuses a chapter question under a new id; a card with a list answer; a 60-second answer of 300 words; a task that deletes nothing; a security group opened to the world through ::/0 or a prefix list; a command with a misspelled option; a diagram with overlapping labels.' },
]
const breakerPrompt = b => `${H}
YOUR TASK: you are a GATE BREAKER. Try to get bad inputs through ${b.scope}
Work only in a sandbox book directory: copy the fixture into aws-saa-book/_build/tmp/breaker-${b.key}/ and use --book-dir. Read aws-saa-book/_build/style/TOOLS.md to learn how the gates are supposed to work, then attack them: at least 15 distinct attempts, including ones that are not listed above. For each attempt record what you did, what the gate answered (exit code and message), and whether the bad input got through.
Write aws-saa-book/_build/reports/gate-break-${b.key}.md with one entry per attempt and a final list of HOLES (bad inputs that passed), each with the smallest reproduction. Do not fix the tool.
Result: attempts made, holes found, report path.`

const breakerFixPrompt = `${H}
YOUR TASK: close the holes that the gate breakers found. Read aws-saa-book/_build/reports/gate-break-grounding.md and gate-break-practice.md. For every HOLE: add a failing regression test first, then fix the module so that the bad input is rejected, then run the full suite (python3 aws-saa-book/tools/tests/run.py). If a hole cannot be closed mechanically, say so and name the review step in the pipeline that must catch it instead. Write aws-saa-book/_build/reports/gate-break-fixes.md.
Result: holes closed, holes left open (with the reason), suite status.`

const REG_GROUPS = [
  { key: 'a', ids: '00 to 15', parts: 'start, identity, security, networking' },
  { key: 'b', ids: '16 to 30', parts: 'compute, storage, databases' },
  { key: 'c', ids: '31 to 52', parts: 'integration, operations, patterns, review' },
]
const registryPrompt = g => `${H}
${CORPUS_RULING}
YOUR TASK: fill the chapter registry for chapters ${g.ids} (parts: ${g.parts}). The registry (aws-saa-book/data/book.json, created from the seed by "registry build") drives every later workflow: it tells each chapter's agents which AWS pages to read and which exam-guide bullets to teach. Read aws-saa-book/_build/style/TOOLS.md (the registry section), TOOLS-corpus.md and TOOLS-feeds.md first. Use only the tool for network access.

For every chapter in your range that has services, resolve and record through "registry set":
- guides: the documentation guide roots (for example https://docs.aws.amazon.com/vpc/latest/userguide/). Find them in the master index (fetch https://docs.aws.amazon.com/llms.txt once and search it), and run "guide" on each so that its index and full.md are saved.
- faq: the FAQ page URLs (fetch each one and confirm that the parser finds questions; note redirects, for example Aurora).
- quotas and history: the quotas or limits page and the document-history page of each guide.
- pricing: the pricing page URL (for pricing dimensions only).
- whatsnew_tags and case_tags: the product tags used by the What's New and the case-study APIs (use "changes tags" and the cases listing).
- extra: the decision guides (https://docs.aws.amazon.com/decision-guides/latest/decision-guides/...), whitepapers and Well-Architected pages that the chapter should use; aws-saa-book/_build/spec/SOURCES.md Part 3 lists verified URLs.
- tasks and bullets: the exam-guide task statements and bullet ids (from the exam guide file built by "registry build") that this chapter must teach. Every bullet that concerns your chapters must be mapped to at least one chapter; a bullet may map to several chapters.
- in-scope services: map each official in-scope service entry that belongs to your chapters to its home chapter and level (deep, medium, light card). If an in-scope service has no natural home in the seed, put it into the closest chapter as a light card and report it.
For pattern, front and synthesis chapters record the whitepapers, Well-Architected pages, decision guides and exam or certification policy pages they need (SOURCES.md Parts 1 to 3).
Also use aws-saa-book/_build/spec/FREQUENCY.md to add a "frequency" note per chapter (how often the topic is reported, and which sub-topics), marked as third-party research and not evidence.
Finish with "registry check" and fix what it reports for your chapters.

Result: chapters completed, in-scope services placed, bullets mapped, problems (for example pages that do not fetch).`

const registryCriticPrompt = `${H}
YOUR TASK: completeness check of the registry. Run "registry check" and "registry show" (see aws-saa-book/_build/style/TOOLS.md). Then verify by judgment, not only by script: every knowledge and skill bullet of the exam guide is mapped to a chapter where it will really be taught (open the bullet text, the chapter title and its services; when unsure, treat it as not covered); every in-scope service has a home chapter and a level; no chapter with services lacks a guide, a FAQ page (where AWS has one) or a history page; shared topics have one owner (VPC endpoints: chapter 11 owns them and chapter 10 introduces them; DAX: chapter 28; RDS Proxy: chapter 26; Global Accelerator: chapter 15; Elastic Disaster Recovery and DR strategy: chapter 40; data transfer cost and purchasing options: chapter 41; S3 Glacier storage classes: chapter 21). Fix gaps directly with "registry set". Write aws-saa-book/_build/reports/registry-review.md with the final coverage numbers and every judgment call.
Result: bullets total and mapped, services total and placed, gaps fixed, gaps left.`

const HARVESTS = [
  { key: 'changes', body: 'Harvest the change feed for every service in the registry: for each What\'s New product tag recorded in aws-saa-book/data/book.json run "changes harvest" with --since 2022-07-01, and for each guide parse its document-history page with "changes history". Then harvest the case-study directory for every case tag. Report the item counts per chapter, and list the services for which no tag or history page worked.' },
  { key: 'pages', body: 'Pre-fetch the shared evidence pages so that later agents find them in the cache: every FAQ page in the registry (run "faq" on each and report the number of questions parsed); the exam guide pages; the certification policy pages (before-testing, during-testing, after-testing, the certification FAQ, the SAA-C03 exam page, the general-information page with the service short names); the decision guides, whitepapers and Well-Architected pages listed in the registry and in aws-saa-book/_build/spec/SOURCES.md Part 3; the AWS global infrastructure page and the shared responsibility model page; the service lifecycle pages (the maintenance, sunset and full-shutdown lists) named in aws-saa-book/_build/spec/FRESHNESS.md. Report every URL that failed, redirected, or produced an empty text snapshot.' },
]
const harvestPrompt = h => `${H}
${CORPUS_RULING}
YOUR TASK (corpus harvest: ${h.key}). Read aws-saa-book/_build/style/TOOLS-corpus.md and TOOLS-feeds.md. ${h.body}
Use only the tool for network access; it rate-limits itself, so let it run and do not start several commands at once. Write a summary to aws-saa-book/_build/reports/harvest-${h.key}.md.
Result: counts and failures.`

const PILOTS = [
  { key: 'p1', items: '(1) pilot-vpc-two-az (arch): a VPC across two Availability Zones with public and private subnets, an internet gateway, one NAT gateway per zone, private route tables and an S3 gateway endpoint; the claim: private instances reach the internet through the NAT gateway in their own zone. (2) pilot-web-three-tier (arch): users, CloudFront, an Application Load Balancer in public subnets, an Auto Scaling group of instances in private subnets, a Multi-AZ database in data subnets, with a numbered request flow.' },
  { key: 'p2', items: '(1) pilot-s3-presigned-url (sequence): a browser asks the application for an upload URL, the application signs it with its role, the browser uploads straight to S3. (2) pilot-iam-cross-account-role (sequence or arch): a user in account A assumes a role in account B through STS and reads a bucket there; show the trust policy and the permissions policy as the two checks.' },
  { key: 'p3', items: '(1) pilot-elb-choose (ladder): choose between Application, Network and Gateway Load Balancer with three or four yes/no questions. (2) pilot-rds-multi-az-vs-replica (compare): a Multi-AZ standby (synchronous, same endpoint, for availability) next to a read replica (asynchronous, own endpoint, for read scaling).' },
  { key: 'p4', items: '(1) pilot-s3-lifecycle (timeline): an object moves from S3 Standard to Standard-IA to Glacier Flexible Retrieval to expiry, with the day marks as labelled placeholders ("day N" style labels, no real numbers). (2) pilot-hybrid-connectivity (arch, the wide stress case): a corporate data centre connected to two VPCs in one Region through Direct Connect with a Site-to-Site VPN backup and a transit gateway.' },
]
const pilotPrompt = p => `${H}
YOUR TASK: author two pilot diagrams with the book's diagram system and judge honestly whether the system is good enough. Read aws-saa-book/_build/style/TOOLS-diagram.md (spec, kinds, style guide) first.
Diagrams: ${p.items}
For each: write the spec to aws-saa-book/diagrams/src/<id>.json, build it, run lint, create the preview and the screenshot, then LOOK at the PNG with your Read tool and check: no overlap or clipping; arrows end on node edges and do not cross nodes; every arrow is labelled or numbered; labels are readable in the phone-width panel; both themes are legible; the claim is obvious at a glance; official icons; at most 12 nodes. Improve the spec and rebuild, at most three rounds per diagram. Do not put memorised AWS limits or numbers into diagrams. If the renderer itself is the problem (not your spec), do not patch it: describe the defect precisely.
Result: for each diagram the spec path, the final PNG path, the rounds used and the remaining defects; plus the renderer defects you found.`

const pilotJudgePrompt = round => `${H}
YOUR TASK: you are the visual judge of the diagram pilot gate${round > 1 ? ' (second round, after a repair pass)' : ''}. Eight pilot diagrams were authored (aws-saa-book/diagrams/src/pilot-*.json). Read the style guide in aws-saa-book/_build/style/TOOLS-diagram.md. Build the contact sheet ("diagram sheet") and the per-diagram preview screenshots, and LOOK at every PNG with your Read tool: each diagram in the desktop and the phone-width panel, in light and in dark.
Judge as the reader would (aws-saa-book/_build/style/READER.md: she skims, so a diagram must give a correct gist in five seconds) and as a professional who knows AWS reference architecture diagrams. Score each diagram 1 to 5 on: correctness of layout (no overlap, no clipping, no edge through a node); legibility at phone width; clarity of the single claim; consistency with the other diagrams; professional look. The gate passes only if every diagram scores at least 4 on the first two criteria and the average over all scores is at least 4.
Write aws-saa-book/_build/reports/diagram-pilot.md with the scores, the defects per diagram, and a list of renderer defects in order of impact (separate from spec defects).
Result: the verdict (pass or fail), the average score, the worst three defects, the report path.`

const pilotFixPrompt = `${H}
YOUR TASK: the diagram pilot gate failed. Read aws-saa-book/_build/reports/diagram-pilot.md and fix the renderer defects in aws-saa-book/tools/saalib/diagram/ in order of impact (and the spec defects in aws-saa-book/diagrams/src/pilot-*.json where the spec is at fault). After each fix rebuild the affected pilot diagrams, screenshot them and LOOK at the PNGs with your Read tool. Keep all diagram tests passing, and add tests for the defects you fix. Stop when every pilot diagram is clean or after three full passes.
Result: defects fixed, defects left, tests status.`

// ---------------------------------------------------------------- orchestration

phase('Canary')
const canary = (await parallel([1, 2].map(i => () => agent(canaryPrompt(i), { label: `canary-${i}`, phase: 'Canary', schema: S.canary, effort: 'low' })))).filter(Boolean)
const canaryOk = canary.length === 2 && canary.every(c => c.write_ok && c.tool_ok && c.uv_ok)
if (!canaryOk) {
  log('Canary failed: stopping so that permissions can be fixed')
  return { stopped: 'canary', canary }
}
log('Canary passed' + (canary.every(c => c.websearch_ok) ? '' : ' (web search was not available to at least one agent)'))

const contractTrack = (async () => {
  const content = await agent(contentContractPrompt, { label: 'contract:content', phase: 'Contract', schema: S.done, effort: 'high' })
  const tools = await agent(toolContractPrompt, { label: 'contract:tools', phase: 'Contract', schema: S.done, effort: 'high' })
  const critiques = (await parallel(CRITICS.map(c => () => agent(criticPrompt(c), { label: `critic:${c.key}`, phase: 'Contract', schema: S.critique, effort: 'high' })))).filter(Boolean)
  const fix = await agent(contractFixPrompt, { label: 'contract:fix', phase: 'Contract', schema: S.done, effort: 'high' })
  log(`Contract ready: ${critiques.map(c => `${c.blockers} blockers, ${c.majors} majors`).join(' / ')} reviewed and fixed`)
  return { content: brief(content), tools: brief(tools), critiques, fix: brief(fix) }
})()

const corpusTrack = (async () => {
  const corpus = await agent(corpusPrompt, { label: 'module:corpus', phase: 'Corpus tools', schema: S.module, effort: 'high' })
  const feeds = await agent(feedsPrompt, { label: 'module:feeds', phase: 'Corpus tools', schema: S.module, effort: 'high' })
  return { corpus: brief(corpus), feeds: brief(feeds) }
})()

const diagramTrack = (async () => {
  const core = await agent(diagramCorePrompt, { label: 'module:diagram-core', phase: 'Diagram renderer', schema: S.module, effort: 'high' })
  const kinds = await agent(diagramKindsPrompt, { label: 'module:diagram-kinds', phase: 'Diagram renderer', schema: S.module, effort: 'high' })
  return { core: brief(core), kinds: brief(kinds) }
})()

const contract = await contractTrack

const ledgerP = agent(ledgerPrompt, { label: 'module:ledger', phase: 'Modules', schema: S.module, effort: 'high' })
const buildersP = parallel(BUILDERS.map(b => () => agent(builderPrompt(b), { label: `module:${b.name}`, phase: 'Modules', schema: S.module, effort: 'high' })))
const [ledgerR, buildersR, corpusR, diagramR] = await Promise.all([ledgerP, buildersP, corpusTrack, diagramTrack])
log('All modules written; integrating')

const integration = await agent(integrationPrompt, { label: 'integrate', phase: 'Integrate', schema: S.done, effort: 'high' })

const breakTrack = (async () => {
  const reports = (await parallel(BREAKERS.map(b => () => agent(breakerPrompt(b), { label: `breaker:${b.key}`, phase: 'Integrate', schema: S.done, effort: 'high' })))).filter(Boolean)
  const fix = await agent(breakerFixPrompt, { label: 'breaker:fix', phase: 'Integrate', schema: S.done, effort: 'high' })
  return { reports: reports.map(brief), fix: brief(fix) }
})()

const registryTrack = (async () => {
  const groups = await parallel(REG_GROUPS.map(g => () => agent(registryPrompt(g), { label: `registry:${g.key}`, phase: 'Registry and corpus', schema: S.done })))
  const critic = await agent(registryCriticPrompt, { label: 'registry:critic', phase: 'Registry and corpus', schema: S.done, effort: 'high' })
  const harvest = await parallel(HARVESTS.map(h => () => agent(harvestPrompt(h), { label: `harvest:${h.key}`, phase: 'Registry and corpus', schema: S.done, effort: 'medium' })))
  return { groups: groups.map(brief), critic: brief(critic), harvest: harvest.map(brief) }
})()

const pilotTrack = (async () => {
  const authors = await parallel(PILOTS.map(p => () => agent(pilotPrompt(p), { label: `pilot:${p.key}`, phase: 'Diagram pilot', schema: S.done })))
  let judge = await agent(pilotJudgePrompt(1), { label: 'pilot:judge', phase: 'Diagram pilot', schema: S.judge, effort: 'high' })
  let repair = null
  if (!judge || judge.verdict !== 'pass') {
    log('Diagram pilot gate failed on the first round; running one repair pass')
    repair = await agent(pilotFixPrompt, { label: 'pilot:repair', phase: 'Diagram pilot', schema: S.done, effort: 'high' })
    judge = await agent(pilotJudgePrompt(2), { label: 'pilot:judge-2', phase: 'Diagram pilot', schema: S.judge, effort: 'high' })
  }
  return { authors: authors.map(brief), judge, repair: brief(repair) }
})()

const [breakers, registry, pilot] = await Promise.all([breakTrack, registryTrack, pilotTrack])

return {
  workflow: 'W0 foundation',
  canary: canary.map(c => ({ write_ok: c.write_ok, tool_ok: c.tool_ok, uv_ok: c.uv_ok, websearch_ok: c.websearch_ok, refused: (c.refused || []).slice(0, 3) })),
  contract,
  modules: { ledger: brief(ledgerR), builders: (buildersR || []).map(brief), corpus: corpusR, diagram: diagramR },
  integration: brief(integration),
  breakers,
  registry,
  pilot,
  reports: 'aws-saa-book/_build/reports/',
}
