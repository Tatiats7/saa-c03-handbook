export const meta = {
  name: 'saa-webapp',
  description: 'W0b of the SAA-C03 Handbook build: the web version (reader, quizzes, mock exam, progress, Claude features) built and tested on the fixture book',
  phases: [
    { title: 'Architecture', detail: 'one contract for the build pipeline, modules, data shapes and tests; reviewed and fixed' },
    { title: 'Build', detail: 'five implementers: site build, shell and reader, practice, state, Claude features and search' },
    { title: 'Integrate', detail: 'assemble, run the browser self-tests, take screenshots, fix' },
    { title: 'Review', detail: 'visual and functional review on screenshots, one repair pass' },
  ],
}

const ROOT = '.'   // the repository root; agents run with the repo root as their working directory

const H = `You are one agent in a multi-agent build of a study book, the "SAA-C03 Handbook", in the folder aws-saa-book/ of the repository in your working directory. Your working directory is the repo root. You are working on its WEB VERSION, a single-page app that the orchestrator will publish as a claude.ai Artifact.

READ FIRST: aws-saa-book/_build/spec/RULINGS.md (authoritative) and aws-saa-book/_build/spec/ARTIFACT-RULES.md (the platform rules; design within them).

GROUND RULES
- Write only inside aws-saa-book/. Never run git. Never publish artifacts (only the orchestrator publishes). Never install system software. Python packages only through "uv run --script <file>" with inline (PEP 723) dependencies, for helper scripts under aws-saa-book/tools/. No npm install: browser code is plain JavaScript without a bundler; node may be used only to run dependency-free test files (node aws-saa-book/tools/web/tests/<file>.mjs).
- Run commands one at a time as plain commands from the repo root, for example: python3 aws-saa-book/tools/saa.py <subcommand> ...   No cd, no pipes, no redirects, no chaining with && or ;. Use your file tools (Read, Write, Edit) for all file work.
- If a command is refused or asks for approval, do not retry it in another form. Note it in your result and continue.
- The tool: aws-saa-book/tools/saa.py loads modules from aws-saa-book/tools/saalib/. Shared helpers are in saalib/common.py (do not edit common.py or saa.py). Documentation: aws-saa-book/_build/style/TOOLS.md and TOOLS-*.md (TOOLS-items.md, TOOLS-rules.md, TOOLS-corpus.md, TOOLS-feeds.md, TOOLS-diagram.md). Content contract: aws-saa-book/_build/style/CONVENTIONS.md and CONVENTIONS-2.md, STYLE.md, SPEC.json, schemas in aws-saa-book/_build/schemas/. The running startup example is called Callvale (aws-saa-book/_build/style/STARTUP.md).
- Other agents are finishing the Python tool modules in aws-saa-book/tools/saalib/ and their tests in aws-saa-book/tools/tests/ right now. Do not edit those, and keep every test of the web version under aws-saa-book/tools/web/tests/ until the web integrator moves them. Test content: the fixture book under aws-saa-book/tools/tests/fixtures/book/ (use it through a sandbox copy and --book-dir).
- Screenshots: use the tool's screenshot command documented in TOOLS-diagram.md (diagram shot --file ... --out ...) or the web commands defined in the architecture contract, then LOOK at the PNG with your Read tool.
- Keep your final answer short; put detail in files.
`

const S = {
  done: { type: 'object', properties: { ok: { type: 'boolean' }, files: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' }, problems: { type: 'array', items: { type: 'string' } } }, required: ['ok', 'summary'] },
  critique: { type: 'object', properties: { report_path: { type: 'string' }, blockers: { type: 'integer' }, majors: { type: 'integer' }, minors: { type: 'integer' } }, required: ['report_path', 'blockers', 'majors', 'minors'] },
  review: { type: 'object', properties: { verdict: { type: 'string', enum: ['ready', 'not-ready'] }, blocking: { type: 'integer' }, report_path: { type: 'string' }, worst: { type: 'array', items: { type: 'string' } } }, required: ['verdict', 'blocking'] },
}
const brief = r => r ? { ok: r.ok, summary: String(r.summary || '').slice(0, 280), problems: (r.problems || []).slice(0, 4).map(x => String(x).slice(0, 200)) } : null

const architectPrompt = `${H}
YOUR TASK: write the ARCHITECTURE CONTRACT for the web version, so that five implementers can build it in parallel and their parts fit together without asking questions.

Read fully:
- aws-saa-book/_build/spec/PRODUCT.md (the product design: section 1 app architecture, 2 features including the two Claude-powered features, 3 data model in db, 4 Markdown conventions, 6 exports and the Get files view, 7 visual design, 8 build and test, 9 risks and the fallback)
- aws-saa-book/_build/style/CONVENTIONS.md and CONVENTIONS-2.md, SPEC.json, the schemas (including plan.schema.json and drills.schema.json), and the fixture book (the real content shapes). Where PRODUCT.md section 4 and CONVENTIONS.md differ on Markdown syntax, file layout or section names, CONVENTIONS.md wins: adapt the design. In particular a chapter is a folder of files (1-fast.md, 2-deep.md, 3-do.md, 4-say.md, 5-quiz.md, sources.md) with three reading routes (Fast, Pass, Full), and a hard fact is a Markdown link [value](../facts/<service>.md#<fact-id>) that becomes an evidence chip.
- aws-saa-book/_build/style/TOOLS.md (data locations), TOOLS-items.md (sync: how 3-do.md, 4-say.md, 5-quiz.md and sources.md are generated) and TOOLS-diagram.md (render_inline for diagrams)
- aws-saa-book/_build/spec/LEARNING.md sections 3 (anti-skim devices: stem-first mode, confidence mark, daily mix, mistakes log with cause codes, Today page), 5 (the explain-out-loud system and the grading rubric) and 10 (calendar and gates)
- The existing artifact she already uses, aws-saa-book/_build/spec/existing/saa-c03-diagnostic.html: its tokens, fonts, exam engine, hot boot and db save are to be ported, not reinvented
- The capability type definitions in aws-saa-book/_build/spec/existing/capabilities/ (db, user, sample, downloads, permissions, claude)

Write aws-saa-book/tools/web/ARCHITECTURE.md (precise and complete; about 6,000 to 8,000 words) covering:
1. File layout under aws-saa-book/tools/web/ (JavaScript modules in load order, CSS, tokens.json, the shell template, stubs, tests) and the published layout under aws-saa-book/_build/site/ with size budgets and the publish-plan file.
2. The build: module aws-saa-book/tools/saalib/site.py exposing "build web" (options --only-ready, --single, --preview, --out) plus "web selftest" and "web shots"; it may call a helper script with inline dependencies through uv for Markdown parsing (markdown-it-py) and code highlighting. Define the Markdown-to-HTML pipeline as an exact mapping table: for every device, role, callout and construct in CONVENTIONS.md, the HTML structure and class names it becomes. Define every JSON file the build emits (manifest.json, chapter content files, chapter data files with questions, cards and speak items, mock files, qindex.json, glossary.json, plan.json, the search corpus) with field-level shapes. Define --preview (wraps index in an emulation of the publish skeleton and loads the stub), the budget checks that fail the build, and how chapters with status planned, draft and ready appear.
3. The JavaScript architecture: one global namespace, each module's public functions with signatures, the event names, the state shape, the router table (hash tokens with "." as separator), the DOM contract (ids and classes of mounts), and the boot sequence including the hot snapshot hook.
4. CSS: the token names (extend the existing artifact's tokens as PRODUCT.md section 7 lists), the generated dark blocks, component class names for every component (callouts by label, tables by kind, quiz, exam, evidence chip, glossary popover, figure card, route switch Fast / Pass / Full, section rail, Today cards, progress bars, speak widget), and the phone layout rules.
5. State: the db paths, document shapes, rules declaration, the local-first store with outbox and merge algorithm, the localStorage keys, the coach digest, and the degraded modes (PRODUCT.md section 3).
6. The Claude features: prompt builders, input caps, JSON validators, page-side verification of quotes, every failure state and its message (PRODUCT.md section 2), using sample.json.
7. Practice features: chapter quiz with per-option explanations, confidence mark and stem-first mode; the timed mock (65 questions, 130 minutes with an option for 160, flag, answer sheet, resume, domain breakdown, review); mistakes log with cause codes and retry; daily mix; domain drills; quick card review.
8. The Today page and the study plan checklist driven by plan.json (relative days: Day 1 to Day 19), and the progress dashboard with the readiness gate.
9. Tests: scoring unit tests in node without dependencies; a render-all self-test route and an exam simulation route that the tool runs in headless Chrome and reads from the dumped DOM; the list of screenshots (desktop and 400 px wide, light and dark); accessibility and performance rules; the lint that rejects literal colours outside tokens, 100vh, window.print, alert( and <a download.
10. A work split for exactly these five implementers, with the files each one owns and no overlaps: (A) site build and the tool commands; (B) shell, CSS, router, content loader, reader, popovers, evidence and glossary; (C) scoring, quiz, exam, mistakes, cards; (D) store, Today, plan, dashboard, files view and the window.claude stub; (E) Claude features, speak practice and search. For each: the functions they must provide and the functions of others they may call.
Scope: everything PRODUCT.md marks P0 and P1. P2 only where it is nearly free. Decide every open choice. Prefer the simplest design that satisfies the platform rules.

Result: the file path, and any risk you see.`

const CRITICS = [
  { key: 'platform', lens: 'Check it line by line against aws-saa-book/_build/spec/ARTIFACT-RULES.md and the capability type definitions in aws-saa-book/_build/spec/existing/capabilities/: anything the frame would block, a capability call that does not match the type definitions, state that would be lost on republish, a theme token defined in only one block, a layout that scrolls sideways on a phone, a first frame that depends on script or storage.' },
  { key: 'implementer', lens: 'Read it as each of the five implementers in turn: find every function that one part calls and no part provides, every data shape defined twice differently, every construct in CONVENTIONS.md, SPEC.json or the schemas that has no mapping to HTML or no place in the JSON files, every ambiguity that two implementers would resolve differently, and any P0 feature of PRODUCT.md section 2 that is missing.' },
]
const criticPrompt = c => `${H}
YOUR TASK: adversarial review of the web architecture contract aws-saa-book/tools/web/ARCHITECTURE.md before five implementers build from it. ${c.lens}
Write aws-saa-book/_build/reports/web-arch-critique-${c.key}.md: numbered findings with severity (blocker, major, minor), the place, what is wrong, and the exact change you propose. Do not edit the contract yourself.
Result: the report path and the counts by severity.`

const archFixPrompt = `${H}
YOUR TASK: apply the review findings in aws-saa-book/_build/reports/web-arch-critique-platform.md and web-arch-critique-implementer.md to aws-saa-book/tools/web/ARCHITECTURE.md. Fix every blocker and major, and cheap minors; keep the document internally consistent; record one line per finding (fixed, rejected with reason, deferred with reason) in aws-saa-book/_build/reports/web-arch-fix.md.
Result: counts, and anything left open.`

const PARTS = [
  { key: 'A', title: 'site build and tool commands', extra: 'You own aws-saa-book/tools/saalib/site.py and the build helper scripts. Build the fixture book (sandbox copy, --book-dir) into a preview site as early as possible, even before the browser code of the other implementers exists, so that they can test against real output: produce the JSON files and a minimal index first, then complete the pipeline. Write unit tests for the Markdown-to-HTML mapping (every device and callout of CONVENTIONS.md) in aws-saa-book/tools/web/tests/test_site.py, runnable with: python3 aws-saa-book/tools/web/tests/test_site.py' },
  { key: 'B', title: 'shell, CSS, router, content loader, reader, popovers, evidence chips and glossary', extra: 'Port the tokens and fonts from aws-saa-book/_build/spec/existing/saa-c03-diagnostic.html and extend them as the contract says. The reader is where she spends hours: get the typography, the Fast / Pass / Full route switch, the section rail, callouts, tables on a phone, figures with zoom and the evidence chip right. Take screenshots at desktop and 400 px width in light and dark and LOOK at them.' },
  { key: 'C', title: 'scoring, quiz, exam, mistakes and cards', extra: 'Port the exam engine from aws-saa-book/_build/spec/existing/saa-c03-diagnostic.html (65 questions, timer on active time, flag, answer sheet, resume, domain breakdown). scoring.js must be pure and importable by node; write aws-saa-book/tools/web/tests/test_scoring.mjs without dependencies and make it pass with: node aws-saa-book/tools/web/tests/test_scoring.mjs' },
  { key: 'D', title: 'store, Today, plan, dashboard, files view and the window.claude stub', extra: 'Read the db, user and downloads type definitions closely. The store is local-first with an outbox; it must work with db = null, with localStorage throwing, and with both. The stub (aws-saa-book/tools/web/stubs/claude-stub.js) must emulate use() for db, user, sample and downloads with switchable modes (ok, none, errors) so that every degraded mode can be exercised locally.' },
  { key: 'E', title: 'the Claude features, speak practice and search', extra: 'Read the sample type definition closely. Implement "check my explanation" and "ask about this section" exactly as the contract specifies, including the page-side verification of quotes and every failure state; they must be hidden cleanly when sample is null. Speak practice must work without Claude (timer, key-point self-check, model answer). Search: jump-to over titles, headings and glossary, plus full text in a worker.' },
]
const partPrompt = p => `${H}
YOUR TASK: implement part ${p.key} of the web version: ${p.title}. Follow aws-saa-book/tools/web/ARCHITECTURE.md exactly (read all of it once, then your part closely; also the review fix log aws-saa-book/_build/reports/web-arch-fix.md). Four other implementers are building the other parts right now: code against the documented functions and data shapes, own only your files, and do not edit theirs. If the contract is wrong or incomplete for your part, choose the smallest reasonable interpretation, implement it, and record it in aws-saa-book/_build/reports/web-part-${p.key}.md so the integrator can reconcile.
${p.extra}
Result: the files you wrote, what works when tested alone, and the deviations you recorded.`

const integratePrompt = `${H}
YOUR TASK: integrate the web version and make it work end to end on the fixture book. Five implementers have just written their parts against aws-saa-book/tools/web/ARCHITECTURE.md; read it and their notes aws-saa-book/_build/reports/web-part-A.md to web-part-E.md.
1. Build the preview site from a sandbox copy of the fixture book (python3 aws-saa-book/tools/saa.py --book-dir ... build web --preview) and fix build errors.
2. Run the browser self-tests through the tool (web selftest: the render-all route and the exam simulation route in headless Chrome) and the node scoring tests; fix failures. You may edit any web file; keep each fix minimal.
3. Take the screenshots (web shots) and LOOK at every PNG with your Read tool: Today, contents, a chapter's fast file, a deep section with a callout, a table, code and a figure, an open evidence chip, a quiz question before and after checking, the mock exam in progress with the answer sheet, the results, the mistakes log, speak practice with a result, search. Each at desktop and 400 px width, in light and in dark. Fix what is broken: overlap, clipping, sideways scroll on the phone, unreadable colours in dark, controls that do nothing.
4. Exercise the degraded modes with the stub: capabilities absent; storage throwing; sample returning each error.
5. Build the single-file variant (--single) and report the sizes of both variants against the limits.
6. Run the web Python tests (python3 aws-saa-book/tools/web/tests/test_site.py). If the file aws-saa-book/_build/reports/w0-integration.md exists (the tool integration by other agents is finished), also copy the web Python tests into aws-saa-book/tools/tests/ as test_site.py so that the main suite covers them, and run the full suite: python3 aws-saa-book/tools/tests/run.py
Write aws-saa-book/_build/reports/web-integration.md: what works, what you fixed, what is still broken, and the paths of the final screenshots.
Result: status of self-tests, sizes, open problems.`

const reviewPrompt = round => `${H}
YOUR TASK: you are the reviewer who decides whether the web version is ready for its first publish${round > 1 ? ' (second round, after a repair pass)' : ''}. Rebuild the preview from the fixture, take fresh screenshots through the tool, and LOOK at every PNG with your Read tool (desktop and 400 px width, light and dark). Then judge as the reader (aws-saa-book/_build/style/READER.md: second-language reader who skims and studies for hours, often on a phone) and against aws-saa-book/_build/spec/ARTIFACT-RULES.md:
- Reading: is the text comfortable (line length, size, spacing)? Do headings, callout labels, tables and captions give a correct gist at a glance? Is the Fast / Pass / Full route obvious?
- Phone: no sideways page scroll, tables and figures usable, controls reachable.
- Dark theme: every text and border legible; diagrams legible.
- Practice: can she answer a question, see per-option explanations, mark confidence, run and resume a mock, see a domain breakdown, find her mistakes?
- First frame: real content without waiting.
- Design: consistent with her existing artifact, not a generic template; no emoji markers; no decoration without meaning.
- Platform rules: nothing the frame blocks.
Write aws-saa-book/_build/reports/web-review.md with blocking defects (must be fixed before she sees it) and non-blocking ones, each with the screenshot it refers to.
Result: verdict ready or not-ready, the number of blocking defects, the worst three.`

const repairPrompt = `${H}
YOUR TASK: fix the blocking defects (then the cheap non-blocking ones) listed in aws-saa-book/_build/reports/web-review.md. After each group of fixes rebuild the preview, take screenshots and LOOK at them. Keep the browser self-tests, the node scoring tests and the tool test suite passing. Append what you fixed and what remains to the report.
Result: defects fixed, defects left, tests status.`

phase('Architecture')
const arch = await agent(architectPrompt, { label: 'web:architect', phase: 'Architecture', schema: S.done, effort: 'high' })
const critiques = (await parallel(CRITICS.map(c => () => agent(criticPrompt(c), { label: `web:critic:${c.key}`, phase: 'Architecture', schema: S.critique, effort: 'high' })))).filter(Boolean)
const archFix = await agent(archFixPrompt, { label: 'web:arch-fix', phase: 'Architecture', schema: S.done, effort: 'high' })
log(`Web architecture ready (${critiques.map(c => `${c.blockers} blockers, ${c.majors} majors`).join(' / ')} reviewed)`)

phase('Build')
const parts = await parallel(PARTS.map(p => () => agent(partPrompt(p), { label: `web:part-${p.key}`, phase: 'Build', schema: S.done, effort: 'high' })))

phase('Integrate')
const integration = await agent(integratePrompt, { label: 'web:integrate', phase: 'Integrate', schema: S.done, effort: 'high' })

phase('Review')
let review = await agent(reviewPrompt(1), { label: 'web:review', phase: 'Review', schema: S.review, effort: 'high' })
let repair = null
if (!review || review.verdict !== 'ready') {
  repair = await agent(repairPrompt, { label: 'web:repair', phase: 'Review', schema: S.done, effort: 'high' })
  review = await agent(reviewPrompt(2), { label: 'web:review-2', phase: 'Review', schema: S.review, effort: 'high' })
}

return {
  workflow: 'W0b web app',
  architecture: brief(arch),
  critiques,
  archFix: brief(archFix),
  parts: parts.map(brief),
  integration: brief(integration),
  review,
  repair: brief(repair),
  reports: 'aws-saa-book/_build/reports/web-*.md',
}
