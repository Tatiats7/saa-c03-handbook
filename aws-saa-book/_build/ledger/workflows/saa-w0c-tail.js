export const meta = {
  name: 'saa-w0c-tail',
  description: 'Finish the W0c leftovers that the usage limit cut off: the registry completeness critic, then the two corpus harvests',
  phases: [
    { title: 'Registry critic', detail: 'completeness check of the whole registry by judgment, gaps fixed through registry set' },
    { title: 'Harvest', detail: 'change feeds and case studies; shared evidence pages' },
  ],
}

const ROOT = '.'   // the repository root; agents run with the repo root as their working directory

const H = `You are one agent in a multi-agent build of a study book, the "SAA-C03 Handbook", in the folder aws-saa-book/ of the repository in your working directory. Your working directory is the repo root.

READ FIRST: aws-saa-book/_build/spec/RULINGS.md. It is authoritative and its "Hard rules for every agent" bind you.

GROUND RULES
- Write only inside aws-saa-book/. Never run git. Never publish artifacts. Never install system software.
- Run commands one at a time as plain commands from the repo root, for example: python3 aws-saa-book/tools/saa.py <subcommand> ...   No cd, no pipes, no redirects (use --out), no chaining with && or ;. Use your file tools (Read, Write, Edit) for all file work.
- If a command is refused or asks for approval, do not retry it in another form. Note it in your result and continue with what you can do.
- Network access for evidence goes only through the tool (fetch, guide, faq, changes, cases). Never WebFetch or curl. WebSearch only to discover the URL of an AWS page.
- Do not edit aws-saa-book/tools/saalib/common.py or aws-saa-book/tools/saa.py.
- Other agents work in the repo at the same time (fact mining of chapters 00, 01, 02, 03 and 10). Never edit data/book.json by hand; always use "registry set" (it takes a lock). Never touch files under aws-saa-book/_build/work/, aws-saa-book/_build/ledger/ or aws-saa-book/data/facts/.
- A batch fetch waits about one second per request (shared limiter): give a long fetch command a timeout of 600000 ms and split batches into chunks of at most 40 URLs. A cached page costs no request.
- Keep your final answer short; it must fit the requested result fields. Put detail in files.
`

const CORPUS_RULING = `CORPUS LAYOUT (fixed)
- source_id: a stable id made from the URL. docs.aws.amazon.com/<path>.html -> "docs/<path>" (no extension); aws.amazon.com/<path>/ -> "www/<path>"; d1.awsstatic.com/<path> -> "static/<path>"; repost.aws/<path> -> "repost/<path>"; API responses -> "api/<name>".
- Files under aws-saa-book/_build/corpus/snap: <source_id>.raw, <source_id>.txt (readable text), <source_id>.meta.json. Guides: aws-saa-book/_build/corpus/index/<guide-id>.json and _build/corpus/full/<guide-id>.md (made by "saa.py guide ROOT"). FAQ indexes under _build/corpus/faq/, change feeds under _build/corpus/changes/<service>.jsonl, the case-study index at _build/corpus/cases/index.jsonl.
- The tool documents: aws-saa-book/_build/style/TOOLS.md section 4 (registry), TOOLS-corpus.md, TOOLS-feeds.md.
`

const S = {
  done: { type: 'object', properties: { ok: { type: 'boolean' }, summary: { type: 'string' }, problems: { type: 'array', items: { type: 'string' } } }, required: ['ok', 'summary'] },
  critic: { type: 'object', properties: { ok: { type: 'boolean' }, bullets_total: { type: 'integer' }, bullets_mapped: { type: 'integer' }, services_total: { type: 'integer' }, services_placed: { type: 'integer' }, check_errors: { type: 'integer' }, check_warnings: { type: 'integer' }, gaps_fixed: { type: 'integer' }, gaps_left: { type: 'array', items: { type: 'string' } }, report_path: { type: 'string' } }, required: ['ok', 'check_errors', 'report_path'] },
}

const criticPrompt = `${H}
${CORPUS_RULING}
YOUR TASK: completeness check of the whole chapter registry (aws-saa-book/data/book.json), after three mapping agents filled it (their notes: aws-saa-book/_build/tmp/reg-00-15/result.json and reg-16-30/result.json; the agent for 31 to 52 applied its patches from aws-saa-book/_build/tmp/reg-31-52/patch-*.json but wrote no summary). "registry check" currently passes with 0 errors and 3 R11 warnings. Run "registry check" and "registry show" (TOOLS.md section 4). Then verify by judgment, not only by script: every knowledge and skill bullet of the exam guide is mapped to a chapter where it will really be taught (open the bullet text, the chapter title and its services; when unsure, treat it as not covered); every in-scope service has a home chapter and a level; no chapter with services lacks a guide, a FAQ page (where AWS has one) or a history page; shared topics have one owner (VPC endpoints: chapter 11 owns them and chapter 10 introduces them; DAX: chapter 28; RDS Proxy: chapter 26; Global Accelerator: chapter 15; Elastic Disaster Recovery and the DR strategies: chapter 40; data transfer cost and purchasing options: chapter 41; S3 Glacier storage classes: chapter 21; the exam policy facts: chapter 01). Fix gaps directly with "registry set ... --by registry-critic". The whole book must stay at "registry check" with 0 errors; a warning may stay with a stated reason.
Chapters 00, 01, 02, 03 and 10 are being mined for facts while you work, and 16, 17, 18, 21 were mined earlier: you may add bullets or sources to them (their brief stage reads the registry again), but remove nothing from them.
Write aws-saa-book/_build/reports/registry-review.md with the final coverage numbers, the per-chapter bullet counts, and every judgment call.
Result: bullets total and mapped, services total and placed, check errors and warnings, gaps fixed, gaps left, the report path.`

const HARVESTS = [
  { key: 'changes', body: 'Harvest the change feed for every service in the registry: for each What\'s New product tag recorded in aws-saa-book/data/book.json (sources.whatsnew_tags of every chapter) run "changes harvest" with --since 2022-07-01, and for each guide parse its document-history page with "changes history". The chapter 16-30 mapping agent already harvested the feeds of about 77 services (files under aws-saa-book/_build/corpus/changes/); the tool caches, so running a tag again is cheap, but skip a feed that is already complete. Then harvest the case-study directory for every case tag ("cases harvest --tag ..."; the full index at _build/corpus/cases/index.jsonl already exists). Report the item counts per chapter, and list the services for which no tag or history page worked.' },
  { key: 'pages', body: 'Pre-fetch the shared evidence pages so that later agents find them in the cache: every FAQ page in the registry (run "faq" on each and report the number of questions parsed; many are already cached); the exam guide pages; the certification policy pages (before-testing, during-testing, after-testing, the certification FAQ, the SAA-C03 exam page, the general-information page with the service short names; URLs in aws-saa-book/_build/spec/SOURCES.md Part 1); the decision guides, whitepapers and Well-Architected pages listed in the registry and in SOURCES.md Part 3; the AWS global infrastructure page and the shared responsibility model page; the service lifecycle pages (the maintenance, sunset and full-shutdown lists) named in aws-saa-book/_build/spec/FRESHNESS.md. Report every URL that failed, redirected, or produced an empty text snapshot.' },
]
const harvestPrompt = h => `${H}
${CORPUS_RULING}
YOUR TASK (corpus harvest: ${h.key}). Read aws-saa-book/_build/style/TOOLS-corpus.md and TOOLS-feeds.md. ${h.body}
Use only the tool for network access; it rate-limits itself, so let it run and do not start several commands at once. Write a summary to aws-saa-book/_build/reports/harvest-${h.key}.md.
Result: counts and failures.`

phase('Registry critic')
const critic = await agent(criticPrompt, { label: 'registry:critic', phase: 'Registry critic', schema: S.critic, effort: 'high' })
log(`Registry critic: ${critic ? `${critic.check_errors} errors, ${critic.check_warnings || 0} warnings, ${critic.gaps_fixed || 0} gaps fixed` : 'no result'}`)
phase('Harvest')
const harvest = await parallel(HARVESTS.map(h => () => agent(harvestPrompt(h), { label: `harvest:${h.key}`, phase: 'Harvest', schema: S.done, effort: 'medium' })))
return { workflow: 'W0c tail', critic, harvest: harvest.map(r => r ? { ok: r.ok, summary: String(r.summary || '').slice(0, 400), problems: (r.problems || []).slice(0, 6) } : null) }