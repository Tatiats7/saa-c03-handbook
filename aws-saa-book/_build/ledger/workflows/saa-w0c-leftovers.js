export const meta = {
  name: 'saa-w0c-leftovers',
  description: 'W0c: finish the chapter registry (chapters 00 to 15 and 31 to 52), run the registry critic and the corpus harvest; close the tool follow-ups and bring the contract documents up to date',
  phases: [
    { title: 'Registry', detail: 'map chapters 00 to 15 and 31 to 52, then the completeness critic' },
    { title: 'Harvest', detail: 'change feeds and case studies; shared evidence pages' },
    { title: 'Catch-up', detail: 'tool follow-up fixes, then the contract documents' },
  ],
}

const ROOT = '.'   // the repository root; agents run with the repo root as their working directory

const H = `You are one agent in a multi-agent build of a study book, the "SAA-C03 Handbook", in the folder aws-saa-book/ of the repository in your working directory. Your working directory is the repo root.

READ FIRST: aws-saa-book/_build/spec/RULINGS.md. It is authoritative and its "Hard rules for every agent" bind you.

GROUND RULES
- Write only inside aws-saa-book/. Never run git. Never publish artifacts. Never install system software. Python packages only through "uv run --script <file>" with inline (PEP 723) dependencies, for helper scripts that live under aws-saa-book/tools/.
- Run commands one at a time as plain commands from the repo root, for example: python3 aws-saa-book/tools/saa.py <subcommand> ...   or   python3 aws-saa-book/tools/tests/run.py <module>. No cd, no pipes, no redirects (use --out), no chaining with && or ;. Use your file tools (Read, Write, Edit) for all file work, including creating folders by writing files into them.
- If a command is refused or asks for approval, do not retry it in another form. Note it in your result and continue with what you can do.
- Network access for evidence goes only through the tool (fetch, guide, faq, changes, cases). Never WebFetch or curl. WebSearch only to discover the URL of an AWS page.
- Do not edit aws-saa-book/tools/saalib/common.py or aws-saa-book/tools/saa.py; if you need a change there, say so in your result.
- Other agents work in the repo at the same time (registry mapping of another chapter range, fact mining of chapters 16, 21 and 22). Never edit data/book.json by hand; always use "registry set" (it takes a lock). Never touch files under aws-saa-book/_build/work/, aws-saa-book/_build/ledger/ or aws-saa-book/data/facts/.
- Keep your final answer short; it must fit the requested result fields. Put detail in files.
`

const CORPUS_RULING = `CORPUS LAYOUT (fixed)
- source_id: a stable id made from the URL. docs.aws.amazon.com/<path>.html -> "docs/<path>" (no extension); aws.amazon.com/<path>/ -> "www/<path>"; d1.awsstatic.com/<path> -> "static/<path>"; repost.aws/<path> -> "repost/<path>"; API responses -> "api/<name>".
- Files under aws-saa-book/_build/corpus/snap: <source_id>.raw, <source_id>.txt (readable text), <source_id>.meta.json. Guides: aws-saa-book/_build/corpus/index/<guide-id>.json and _build/corpus/full/<guide-id>.md (made by "saa.py guide ROOT"). FAQ indexes under _build/corpus/faq/, change feeds under _build/corpus/changes/<service>.jsonl, the case-study index at _build/corpus/cases/index.jsonl.
- The tool documents: aws-saa-book/_build/style/TOOLS.md section 4 (registry), TOOLS-corpus.md, TOOLS-feeds.md.
`

const S = {
  done: { type: 'object', properties: { ok: { type: 'boolean' }, files: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' }, problems: { type: 'array', items: { type: 'string' } } }, required: ['ok', 'summary'] },
  registry: { type: 'object', properties: { ok: { type: 'boolean' }, chapters_completed: { type: 'array', items: { type: 'string' } }, bullets_mapped: { type: 'integer' }, services_placed: { type: 'integer' }, check_errors_for_my_range: { type: 'integer' }, summary: { type: 'string' }, problems: { type: 'array', items: { type: 'string' } } }, required: ['ok', 'chapters_completed', 'summary'] },
  critic: { type: 'object', properties: { ok: { type: 'boolean' }, bullets_total: { type: 'integer' }, bullets_mapped: { type: 'integer' }, services_total: { type: 'integer' }, services_placed: { type: 'integer' }, check_errors: { type: 'integer' }, check_warnings: { type: 'integer' }, gaps_fixed: { type: 'integer' }, gaps_left: { type: 'array', items: { type: 'string' } }, report_path: { type: 'string' } }, required: ['ok', 'check_errors', 'report_path'] },
}

const brief = r => r ? { ok: r.ok, summary: String(r.summary || '').slice(0, 400), problems: (r.problems || []).slice(0, 6).map(x => String(x).slice(0, 240)) } : null

const REG_GROUPS = [
  { key: 'a', ids: '00 to 15', parts: 'start, identity, security, networking', resume: `RESUMING AN INTERRUPTED TASK. A previous agent for this range was cut off before it recorded anything in the registry. Its scratch files are in aws-saa-book/_build/tmp/reg-00-15/ (urls-quotas.txt, urls-pricing.txt, fetch-*.json, case-tags.txt, whatsnew-tags.txt): reuse them. Chapters 16 to 30 are complete and are your model: read aws-saa-book/_build/tmp/reg-16-30/result.json (its decisions and problems) and aws-saa-book/_build/tmp/reg-16-30/patch-21.json for the patch shape (keys sources, bullets, cards, service_map, notes). Write one patch per chapter to aws-saa-book/_build/tmp/reg-00-15/patch-NN.json and apply it with: python3 aws-saa-book/tools/saa.py registry set NN --file aws-saa-book/_build/tmp/reg-00-15/patch-NN.json --by reg-00-15
Open items in your range right now: the task statements 1.1 and 1.2 have no bullet mapped anywhere (their bullets belong to chapters 03 to 10); the in-scope names Amazon Route 53 (home: chapter 13) and AWS CLI (home: chapter 02, light card) have no service key. Chapter 10 (VPC) is the owner of VPC basics and introduces endpoints; chapter 11 owns peering, Transit Gateway, endpoints and PrivateLink; chapter 15 owns Global Accelerator.
Front chapters 00, 01 and 02 have no services but need sources: the certification policy pages (aws-saa-book/_build/spec/SOURCES.md Part 1: before-testing, during-testing, after-testing, the certification FAQ, the SAA-C03 exam page), the exam guide pages (already in the corpus under docs/aws-certification/latest/solutions-architect-associate-03/), the AWS global infrastructure page, the shared responsibility model page, the Well-Architected Framework pages and the general-information page with the service short names (SOURCES.md Parts 2 and 3). Chapter 01 owns the fact namespace "exam" (exam policy facts). Chapter 02 teaches the general bullets about Regions, Availability Zones, edge locations and the shared responsibility model: map those bullets to it in addition to their service chapters.
Write your summary to aws-saa-book/_build/tmp/reg-00-15/result.json in the shape of reg-16-30/result.json.` },
  { key: 'c', ids: '31 to 52', parts: 'integration, operations, patterns, review', resume: `RESUMING AN INTERRUPTED TASK. A previous agent wrote patches for chapters 31 to 50 and 52 to aws-saa-book/_build/tmp/reg-31-52/patch-NN.json but was cut off before applying them: data/book.json holds none of them (confirm with registry show 31). Its URL list is aws-saa-book/_build/tmp/reg-31-52/batch-all-urls.txt (375 URLs). Chapters 16 to 30 are complete and are your model: read aws-saa-book/_build/tmp/reg-16-30/result.json (decisions and problems) and aws-saa-book/_build/tmp/reg-16-30/patch-21.json.
Do this: review every patch (are the bullets right for that chapter? are the URLs on allowed hosts and do they fetch? are the in-scope names of the chapter mapped?), fix what is wrong, then apply each with: python3 aws-saa-book/tools/saa.py registry set NN --file aws-saa-book/_build/tmp/reg-31-52/patch-NN.json --by reg-31-52   Write the missing patch for chapter 51 (mock exam 2: the same policy and exam-guide sources as chapter 50 and all 14 task statements) and check 49 and 52. Make every URL in the patches present in the corpus (registry check --urls --fetch, or fetch --batch with the URL list; a cached page costs no request). Run "guide" on every guide root that has no index yet.
Open items in your range right now: task statement 4.4 (cost-optimized network architectures) has no bullet mapped anywhere; map its bullets to chapter 41 (cost optimization) and, where they fit, to 43 or 44, so that none stays unmapped (another agent may also map some of them to the networking chapters 11, 12 and 15; a bullet may have several chapters). The in-scope names Amazon Kinesis (home: chapter 34), Amazon OpenSearch Service (35) and Amazon Managed Service for Prometheus (37) have no service key yet.
Write your summary to aws-saa-book/_build/tmp/reg-31-52/result.json in the shape of reg-16-30/result.json.` },
]

const registryPrompt = g => `${H}
${CORPUS_RULING}
YOUR TASK: fill the chapter registry for chapters ${g.ids} (parts: ${g.parts}). The registry (aws-saa-book/data/book.json) drives every later workflow: it tells each chapter's agents which AWS pages to read and which exam-guide bullets to teach. Read aws-saa-book/_build/style/TOOLS.md section 4 (registry), TOOLS-corpus.md and TOOLS-feeds.md first. Use only the tool for network access.
${g.resume}

For every chapter in your range that has services, resolve and record through "registry set":
- guides: the documentation guide roots (for example https://docs.aws.amazon.com/vpc/latest/userguide/). Find them in the master index (fetch https://docs.aws.amazon.com/llms.txt once, then search it), and run "guide" on each so that its index and full.md are saved.
- faq: the FAQ page URLs (fetch each one and confirm that the parser finds questions; note redirects).
- quotas and history: the quotas or limits page and the document-history page of each guide.
- pricing: the pricing page URL (for pricing dimensions only).
- whatsnew_tags and case_tags: the product tags used by the What's New and the case-study APIs ("changes tags" and "cases tags").
- extra pages: the decision guides (https://docs.aws.amazon.com/decision-guides/latest/decision-guides/...), whitepapers and Well-Architected pages that the chapter should use (in sources.pages); aws-saa-book/_build/spec/SOURCES.md Part 3 lists verified URLs.
- tasks and bullets: the exam-guide task statements and bullet ids (exam-guide.json, built by "registry build") that this chapter must teach. Every bullet that concerns your chapters must be mapped to at least one chapter; a bullet may map to several chapters. Keep lists teachable: deep at most 18 bullets, medium at most 8, light at most 6, as the 16-30 agent did.
- in-scope services: map each official in-scope entry that belongs to your chapters to its home chapter and level (deep, medium, light card; --map "Official name=key"). If an in-scope service has no natural home, put it into the closest chapter as a light card and report it.
For pattern, front, synthesis and mock chapters record the whitepapers, Well-Architected pages, decision guides and exam or certification policy pages they need (SOURCES.md Parts 1 to 3). A synthesis chapter carries a bullet only where it really teaches it; the mock chapters carry all 14 task statements and no bullets.
Also use aws-saa-book/_build/spec/FREQUENCY.md to add a frequency note per chapter (patch key "notes"), marked as third-party research and not evidence.
Another agent maps the other chapter range at the same time: apply patches one chapter at a time through the tool. Finish with "registry check" and fix what it reports for your chapters; findings about the other range are not yours.

Result: ok, chapters completed, bullets mapped, in-scope services placed, check errors left for your range, a summary, and problems (for example pages that do not fetch).`

const registryCriticPrompt = `${H}
${CORPUS_RULING}
YOUR TASK: completeness check of the whole registry, after three mapping agents filled it. Run "registry check" and "registry show" (TOOLS.md section 4). Then verify by judgment, not only by script: every knowledge and skill bullet of the exam guide is mapped to a chapter where it will really be taught (open the bullet text, the chapter title and its services; when unsure, treat it as not covered); every in-scope service has a home chapter and a level; no chapter with services lacks a guide, a FAQ page (where AWS has one) or a history page; shared topics have one owner (VPC endpoints: chapter 11 owns them and chapter 10 introduces them; DAX: chapter 28; RDS Proxy: chapter 26; Global Accelerator: chapter 15; Elastic Disaster Recovery and the DR strategies: chapter 40; data transfer cost and purchasing options: chapter 41; S3 Glacier storage classes: chapter 21; the exam policy facts: chapter 01). Fix gaps directly with "registry set ... --by registry-critic". The whole book must reach "registry check" with 0 errors; a warning may stay with a stated reason.
Chapters 16, 21 and 22 are being mined for facts while you work: you may add bullets or sources to them (their brief stage reads the registry again), but remove nothing from them.
Write aws-saa-book/_build/reports/registry-review.md with the final coverage numbers, the per-chapter bullet counts, and every judgment call.
Result: bullets total and mapped, services total and placed, check errors and warnings, gaps fixed, gaps left, the report path.`

const HARVESTS = [
  { key: 'changes', body: 'Harvest the change feed for every service in the registry: for each What\'s New product tag recorded in aws-saa-book/data/book.json (sources.whatsnew_tags of every chapter) run "changes harvest" with --since 2022-07-01, and for each guide parse its document-history page with "changes history". The chapter 16-30 mapping agent already harvested the feeds of about 77 services (files under aws-saa-book/_build/corpus/changes/); the tool caches, so running a tag again is cheap, but skip a feed that is already complete. Then harvest the case-study directory for every case tag ("cases harvest --tag ..."; the full index at _build/corpus/cases/index.jsonl already exists). Report the item counts per chapter, and list the services for which no tag or history page worked.' },
  { key: 'pages', body: 'Pre-fetch the shared evidence pages so that later agents find them in the cache: every FAQ page in the registry (run "faq" on each and report the number of questions parsed; many are already cached); the exam guide pages; the certification policy pages (before-testing, during-testing, after-testing, the certification FAQ, the SAA-C03 exam page, the general-information page with the service short names; URLs in aws-saa-book/_build/spec/SOURCES.md Part 1); the decision guides, whitepapers and Well-Architected pages listed in the registry and in SOURCES.md Part 3; the AWS global infrastructure page and the shared responsibility model page; the service lifecycle pages (the maintenance, sunset and full-shutdown lists) named in aws-saa-book/_build/spec/FRESHNESS.md. Report every URL that failed, redirected, or produced an empty text snapshot.' },
]
const harvestPrompt = h => `${H}
${CORPUS_RULING}
YOUR TASK (corpus harvest: ${h.key}). Read aws-saa-book/_build/style/TOOLS-corpus.md and TOOLS-feeds.md. ${h.body}
Use only the tool for network access; it rate-limits itself (one request per second across all processes), so let it run and do not start several commands at once; a cached page costs no request. Write a summary to aws-saa-book/_build/reports/harvest-${h.key}.md.
Result: counts and failures.`

const toolFixPrompt = `${H}
YOUR TASK: close the tool follow-ups that the W0 integration left open. Read aws-saa-book/_build/reports/w0-integration.md ("What still does not work", items 3 and 4), aws-saa-book/_build/reports/gate-break-fixes.md (H13 and the practice holes) and the function holds_display in aws-saa-book/tools/saalib/lint.py.
1. Use lint.holds_display (or one shared helper with the same number-boundary rule, placed where every module can import it with a guarded import) in: facts.py check M7 (a display is a substring of the claim or of a quote); qbank.py numbers_outside_displays (C109, P109); the re-derivation match of the audit in facts.py. A display that sits inside a longer number ("5 Gbps" inside "45 Gbps", "500 widgets" inside "2 500 widgets", "1,000" inside "11,000") must not count as present.
2. facts.render_sheet: a quote that contains a Markdown link or image prints the link text only (the fact sheet facts/<service>.md is a reader file and must not carry a link to a host outside the allow-list); the stored quote itself does not change. Table-row quotes too.
3. The ledger deviation recorded in aws-saa-book/_build/reports/w0-result.json (modules.ledger.problems): a failed finalize leaves "status: ready" in the hand files. Make "stage end finalize" put the previous status line back when its gates fail. Skip this item only if it needs more than a small change; say so.
For every item write the failing regression test first (in the existing hole test files: test_facts_holes.py, test_qbank_holes.py, test_ledger.py), then the fix, then the full suite: python3 aws-saa-book/tools/tests/run.py   and   python3 aws-saa-book/tools/saa.py selftest
Other agents run the tool while you work: keep every module importable at every moment (write a whole file at once; never leave a syntax error on disk), keep each edit small, and do not change the meaning of any existing command.
Write aws-saa-book/_build/reports/w0c-tool-fixes.md (what changed, where, tests added, suite status).
Result: ok, summary, problems.`

const docsPrompt = `${H}
YOUR TASK: bring the tool contract documents up to date with the code, so that the chapter agents who read them are not misled. This task changes no code.
Read, in this order: aws-saa-book/_build/reports/gate-break-fixes.md (its section "Changes that the contract documents must take over", 8 items, and the "Notes"); aws-saa-book/_build/reports/w0-integration.md (fixes 1 to 4); aws-saa-book/_build/tmp/reg-16-30/result.json (key "tool_changes": registry check --urls accepts a guide root when its index exists; the registry set patch key "notes"); aws-saa-book/_build/reports/w0-result.json (every "deviations" list of the module builders under modules: ledger, builders (facts, registry, lint, qbank, lab), corpus, diagram; each deviation is a behaviour that differs from the contract and must be documented where it is true in the code); aws-saa-book/_build/reports/w0c-tool-fixes.md (just written by another agent).
For each item: find the place in aws-saa-book/_build/style/TOOLS.md, TOOLS-items.md, TOOLS-rules.md, TOOLS-corpus.md, TOOLS-feeds.md, TOOLS-diagram.md, CONVENTIONS.md, CONVENTIONS-2.md or SPEC.json that describes the old behaviour; confirm the new behaviour in the code (read the function; if unsure, run the command on a sandbox copy of the fixture with --book-dir aws-saa-book/_build/tmp/docs-check); then rewrite the sentence. Keep the documents' style: short, exact, with the command form. Do not change a rule that the code does not implement; where code and document disagree and the code looks wrong, list it in the report instead of changing the document. The startup data file is data/startup.json (renamed today; the documents already say so). Do not change RULINGS.md (the orchestrator owns it) or STYLE.md.
Write aws-saa-book/_build/reports/w0c-docs-catchup.md: one line per item (document, section, what changed) and the list of code-versus-document disagreements left.
Result: ok, summary (items documented), problems (disagreements left).`

const registryTrack = (async () => {
  phase('Registry')
  const groups = await parallel(REG_GROUPS.map(g => () => agent(registryPrompt(g), { label: `registry:${g.key}`, phase: 'Registry', schema: S.registry, effort: 'high' })))
  log(`Registry mapping: ${groups.map((r, i) => `${REG_GROUPS[i].key}=${r && r.ok ? 'ok' : 'failed'} (${r ? (r.chapters_completed || []).length : 0} chapters)`).join(', ')}`)
  const critic = await agent(registryCriticPrompt, { label: 'registry:critic', phase: 'Registry', schema: S.critic, effort: 'high' })
  log(`Registry critic: ${critic ? `${critic.check_errors} errors, ${critic.check_warnings || 0} warnings, ${critic.gaps_fixed || 0} gaps fixed` : 'no result'}`)
  phase('Harvest')
  const harvest = await parallel(HARVESTS.map(h => () => agent(harvestPrompt(h), { label: `harvest:${h.key}`, phase: 'Harvest', schema: S.done, effort: 'medium' })))
  return { groups: groups.map(r => r ? { ok: r.ok, chapters: r.chapters_completed, bullets: r.bullets_mapped, services: r.services_placed, errors_left: r.check_errors_for_my_range, summary: String(r.summary || '').slice(0, 300), problems: (r.problems || []).slice(0, 8).map(x => String(x).slice(0, 240)) } : null), critic, harvest: harvest.map(brief) }
})()

const catchupTrack = (async () => {
  const fix = await agent(toolFixPrompt, { label: 'catchup:tool-fixes', phase: 'Catch-up', schema: S.done, effort: 'high' })
  const docs = await agent(docsPrompt, { label: 'catchup:docs', phase: 'Catch-up', schema: S.done, effort: 'high' })
  return { fix: brief(fix), docs: brief(docs) }
})()

const [registry, catchup] = await Promise.all([registryTrack, catchupTrack])
return { workflow: 'W0c foundation leftovers', registry, catchup, reports: 'aws-saa-book/_build/reports/ (registry-review.md, harvest-*.md, w0c-*.md)' }