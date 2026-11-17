export const meta = {
  name: 'saa-exemplar',
  description: 'SAA-C03 Handbook exemplar panel: three independent attempts at IAM and VPC slices, five blind judges, synthesis into the frozen style, spec and reference chapter',
  phases: [
    { title: 'Attempts', detail: 'three writers with different teaching angles, each in its own sandbox' },
    { title: 'Judges', detail: 'five blind judges with different lenses score and rank the attempts' },
    { title: 'Synthesis', detail: 'winner plus grafts become the exemplar; style and spec frozen at 1.0; critic and fix' },
  ],
}

// Precondition (done by the orchestrator): facts of chapters 03 (IAM) and 10 (VPC) are verified, and three sandbox
// book directories exist: aws-saa-book/_build/tmp/exemplar-a, -b, -c (copies of data/, facts/, diagrams/icons.json,
// _build/style, _build/schemas, _build/registry; no corpus copy needed for lint).
const ROOT = '.'   // the repository root; agents run with the repo root as their working directory
const TOOL = 'python3 aws-saa-book/tools/saa.py'

const H = `You are one agent in a multi-agent build of a study book, the "SAA-C03 Handbook" (a prep book for the AWS Certified Solutions Architect - Associate exam), in the folder aws-saa-book/ of the repository in your working directory. Your working directory is the repo root.

READ FIRST: aws-saa-book/_build/spec/RULINGS.md (authoritative; its hard rules bind you) and aws-saa-book/_build/style/READER.md (the one reader this book is for).

GROUND RULES
- Write only inside aws-saa-book/. Never run git. Never publish artifacts. Never install system software.
- Run commands one at a time as plain commands from the repo root: ${TOOL} <subcommand> ...   No cd, no pipes, no redirects (use --out), no chaining with && or ;. Use your file tools (Read, Write, Edit) for file work. If a command is refused or asks for approval, do not retry it in another form; note it and continue.
- Your memory supplies questions, never answers: a number, limit, default, date, or a "can / cannot / only / always / never" claim may appear only as a link to a verified fact (CONVENTIONS.md section F). Read AWS pages only through the tool's corpus commands (search, show). No WebFetch, no curl, no exam-dump content.
- The contract: aws-saa-book/_build/style/CONVENTIONS.md, CONVENTIONS-2.md, STYLE.md, SPEC.json; the tool documents TOOLS.md, TOOLS-items.md, TOOLS-rules.md, TOOLS-diagram.md; the pedagogy specification aws-saa-book/_build/spec/LEARNING.md; the story bible aws-saa-book/_build/style/STARTUP.md (the startup is called Callvale).
- Keep your final answer short: only the result fields. Detail goes into files.
`

const S = {
  attempt: { type: 'object', properties: { ok: { type: 'boolean' }, words_fast: { type: 'integer' }, words_deep: { type: 'integer' }, questions: { type: 'integer' }, lint_errors: { type: 'integer' }, fact_gaps: { type: 'integer' }, note: { type: 'string' } }, required: ['ok'] },
  judge: {
    type: 'object',
    properties: {
      lens: { type: 'string' },
      ranking: { type: 'array', items: { type: 'string', enum: ['a', 'b', 'c'] } },
      scores: { type: 'object', properties: { a: { type: 'array', items: { type: 'number' } }, b: { type: 'array', items: { type: 'number' } }, c: { type: 'array', items: { type: 'number' } } }, required: ['a', 'b', 'c'] },
      fatal: { type: 'array', items: { type: 'string', enum: ['a', 'b', 'c'] } },
      report_path: { type: 'string' },
    },
    required: ['lens', 'ranking', 'scores', 'report_path'],
  },
  done: { type: 'object', properties: { ok: { type: 'boolean' }, files: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' }, problems: { type: 'array', items: { type: 'string' } } }, required: ['ok', 'summary'] },
  critique: { type: 'object', properties: { report_path: { type: 'string' }, blockers: { type: 'integer' }, majors: { type: 'integer' }, minors: { type: 'integer' } }, required: ['report_path', 'blockers', 'majors', 'minors'] },
}

const ATTEMPTS = [
  { key: 'a', angle: 'FIRST PRINCIPLES. Teach by building the mechanism from the ground up: start from the problem the service solves, then follow one request step by step through the system, so that every rule the exam tests can be derived rather than memorised. Your risk is length and abstraction; counter it with concrete traces and short subsections.' },
  { key: 'b', angle: 'EXAM OPERATOR. Teach through decisions: lead with the discriminations the exam forces (this or that, and the phrase that decides), then give exactly the mechanism needed to make each decision reliably, then the traps. Your risk is a list of tips without understanding; counter it by explaining why each rule holds.' },
  { key: 'c', angle: 'CUSTOMER CONVERSATION. Teach as a solutions architect explains to a customer: start from a real situation (Callvale and its people), the question they ask, the answer in plain words, then the mechanism behind the answer and what to watch. Your risk is story without rigour; counter it with exact facts and sharp comparison tables.' },
]

const attemptPrompt = t => `${H}
YOUR TASK: you are one of three writers who each produce, independently, a sample of the book's most important chapter, so that judges can choose the approach that teaches this reader best. The winner's approach will be copied by about fifty chapters. Your teaching angle: ${t.angle}
All three attempts must obey the same contract (structure, devices, fact links, word limits); the angle changes how you explain, order and choose examples inside it.

Work ONLY in your sandbox book directory aws-saa-book/_build/tmp/exemplar-${t.key}/ and pass --book-dir aws-saa-book/_build/tmp/exemplar-${t.key} on every tool command. The sandbox has the verified facts of chapter 03 (IAM) and chapter 10 (VPC). Get the ready-made fact links with: ${TOOL} --book-dir aws-saa-book/_build/tmp/exemplar-${t.key} facts card --chapter 03 --out aws-saa-book/_build/tmp/exemplar-${t.key}/_build/work/03-iam/fact-cards.md   (and the same for chapter 10 into _build/work/10-vpc/). To understand a mechanism you may read the AWS pages in the real corpus (${TOOL} search ... and show ..., without --book-dir), but every hard claim you write must be a link to a verified fact. If a fact you need is missing, leave the sentence out and list the gap in your notes.

Read first: LEARNING.md (sections 1 to 9: the templates, devices, style, spoken answers, question standard, tasks, the running example; note that RULINGS.md raises the depth budget), CONVENTIONS.md, STYLE.md, the deep template in SPEC.json, the IAM and VPC entries of STARTUP.md, and the registry entry of chapter 03 (${TOOL} registry show 03).

Produce, inside your sandbox:
1. _build/work/03-iam/brief.json: your plan for the WHOLE IAM chapter in the shape of the "brief" gate (TOOLS.md 3.1): every section and every "How it works" subsection as an assertion heading in teaching order, traps, question slots, tasks, spoken prompts, diagrams.
2. 03-iam/1-fast.md: complete, every section and device, within the limit.
3. 03-iam/2-deep.md: the complete section structure with all subsection headings, and THREE subsections written in full: how a request is evaluated (explicit deny, allow, implicit deny, and how service control policies and permissions boundaries limit it); roles and AssumeRole (trust policy and permissions policy, temporary credentials); identity-based versus resource-based policies and cross-account access. Also write in full the Numbers section, the decision record and five FAQ quick-fire items. Leave the other subsections as headings with a one-line note of what they will teach.
4. 10-vpc/2-deep.md: only TWO subsections written in full, to show the approach on a different kind of topic: security groups versus network ACLs; the NAT gateway and outbound traffic including its cost dimensions.
5. data/03-iam/questions.json: 6 questions on the parts you wrote (one twin pair, one multiple-response, at least three built on traps), added with "q add" and clean in "q lint". data/03-iam/speak.json: 2 spoken-answer items (speak add, speak lint). data/03-iam/tasks.json: one Look and one Try task (tasks lint). One diagram: the hero diagram of IAM or the AssumeRole flow (spec in diagrams/src/, built, screenshot taken and LOOKED at with your Read tool).
6. Run the chapter lint in draft mode on your files (lint 03 --draft and lint 10 --file 2-deep.md --draft) and fix errors. Report the number of errors that remain.
7. _build/work/03-iam/attempt-notes.md: in at most 300 words, why your approach serves this reader, what you would change in the contract (a budget that is wrong, a device that does not work), and the fact gaps you met.
Write the real thing at full quality: depth she can use with a customer, in sentences she can read fast.

Result: ok, word counts, questions written, lint errors left, fact gaps.`

const CRITERIA = ['learnability for this reader', 'exam discrimination power', 'technical precision', 'reusable explanations (can she say it to a customer)', 'retention design (anti-skim devices that work)', 'economy (no padding, every paragraph pays)', 'grounding hygiene (fact links, no unsupported claims)']
const WEIGHTS = [20, 20, 20, 10, 10, 10, 10]
const JUDGES = [
  { key: 'reader', order: ['a', 'b', 'c'], lens: 'You ARE the reader described in READER.md: a strong engineer, new to cloud detail, English is your second language, you skim, long text makes you stop, you forget terms under stress, and next week you must explain IAM out loud to colleagues. Read each attempt the way she would: skim first, then read. Which one would you actually finish? After which one could you answer an unseen exam question and explain the service to a customer? Where did you get lost, bored or misled by your own skim?' },
  { key: 'exam', order: ['b', 'c', 'a'], lens: 'You are an AWS certification exam-preparation expert who knows how SAA-C03 questions are built: scenario, constraints, one qualifier, four plausible options. Which attempt best builds the discriminations the exam demands? Are the signals real and guarded, the traps common beliefs, the questions realistic in register and difficulty with plausible distractors and explanations that teach? What examinable IAM content is missing?' },
  { key: 'architect', order: ['c', 'a', 'b'], lens: 'You are a senior AWS solutions architect and a strict technical reviewer. Check precision: is every statement exactly right, with the right scope and conditions? Check the attempts against the AWS pages in the corpus (search and show) where you doubt a claim, and look for sentences that say more than their fact link supports. Is the depth real (mechanism, edge cases, failure modes) or surface? Name any attempt with a technical error that would mislead her as having a FATAL defect.' },
  { key: 'designer', order: ['a', 'c', 'b'], lens: 'You are an instructional designer who works with evidence on retrieval practice, worked examples, cognitive load and spacing. Which attempt makes the best use of the devices (Predict, Stop and answer, twin questions, Recap from memory, worked think-alouds, the spoken four moves)? Where do devices exist only as decoration? Is the load per subsection right? Does the fast file work as a correct gist and the deep file as real understanding?' },
  { key: 'editor', order: ['b', 'a', 'c'], lens: 'You are a plain-language editor for second-language readers. Judge sentence length and clarity, term consistency, how terms are introduced, idioms and phrasal verbs, whether tables and headings carry the meaning, whether spoken answers sound like speech, and the quality of the tone (calm, direct, adult). Count concrete violations of STYLE.md per attempt.' },
]
const judgePrompt = j => `${H}
YOUR TASK: you are one of five judges who choose the approach for the whole book. ${j.lens}
Three anonymous attempts are in aws-saa-book/_build/tmp/exemplar-a/, exemplar-b/ and exemplar-c/ (in each: 03-iam/1-fast.md, 03-iam/2-deep.md, 10-vpc/2-deep.md, data/03-iam/questions.json, speak.json and tasks.json, the diagram under diagrams/, and _build/work/03-iam/brief.json and attempt-notes.md). Read them in this order: ${j.order.join(', ')}. To see generated files run the tool with --book-dir on a sandbox (sync, lint --draft); do not change any attempt.
Score each attempt from 1 to 5 on these seven criteria, in this order: ${CRITERIA.map((c, i) => `(${i + 1}) ${c}`).join('; ')}. Use the full scale; a 5 means you would copy it for fifty chapters as it is. Then rank the three, best first. Then list, for the synthesis: the specific ideas from the non-winning attempts that should be grafted onto the winner, and the must-fix defects of the winner. Judge the writing and teaching, not which angle you like in theory.
Write your reasoning, with quoted lines as evidence, to aws-saa-book/_build/reports/exemplar-judge-${j.key}.md.
Result: your lens key "${j.key}", the ranking (best first), the scores as seven numbers per attempt in the criteria order, the attempts with a fatal technical defect (if any), and the report path.`

const synthesisPrompt = verdict => `${H}
YOUR TASK: turn the judging panel's result into the frozen reference for the whole book. This is the most leveraged writing in the project: about fifty chapters will imitate what you produce.
The panel result (computed by script from the five judges): ${verdict}
Read: the five judge reports aws-saa-book/_build/reports/exemplar-judge-*.md; all three attempts under aws-saa-book/_build/tmp/exemplar-a, -b and -c (files and attempt-notes.md); the current contract (CONVENTIONS.md, CONVENTIONS-2.md, STYLE.md, SPEC.json).
Produce:
1. The exemplar in aws-saa-book/_build/style/exemplar/: start from the winning attempt and graft the ideas the judges named from the others; fix every must-fix defect. Files: iam-1-fast.md (complete), iam-2-deep.md (the three full subsections plus Numbers, the decision record and the FAQ quick-fire), vpc-2-deep-slice.md, questions.json (the six questions, improved), speak.json, tasks.json, the diagram spec, and README.md: what a writer must imitate (ten concrete points, each with a quoted example from the exemplar) and the ten most common ways the attempts went wrong.
2. STYLE.md version 1.0: keep its rules, add what the panel learned (as rules with examples), remove what proved wrong.
3. SPEC.json version 1.0: adjust word limits, counts and lint parameters only where the judges gave evidence that a value is wrong (for example a section that cannot hold its devices, or a limit that forces padding). Stay within RULINGS.md. List every changed key with the reason in aws-saa-book/_build/reports/exemplar-spec-changes.md.
4. CONVENTIONS.md and CONVENTIONS-2.md: change only where a device has to change; bump their version line to 1.0.
5. Keep the tool consistent: if you changed SPEC keys or conventions, update the fixture under aws-saa-book/tools/tests/fixtures/ so the tests still describe the contract, and run python3 aws-saa-book/tools/tests/run.py until it passes. Do not edit tool code except test fixtures; if a tool change is needed, describe it in the report.
6. Check the exemplar against the tool in a sandbox copy (use aws-saa-book/_build/tmp/exemplar-final/ created as a copy of the winning sandbox with your files in place): lint in draft mode, q lint, speak lint, tasks lint must be clean.
Result: ok, the files written, a three-line summary of the chosen approach, and open problems.`

const critics = [
  { key: 'consistency', lens: 'Check that the frozen contract is consistent: every rule in STYLE.md 1.0 has an example; every checkable rule has a SPEC.json key and a lint code in TOOLS.md or TOOLS-rules.md, or is marked as a review-only rule; the exemplar obeys every rule (run lint in draft mode, q lint, speak lint, tasks lint on aws-saa-book/_build/tmp/exemplar-final/ with --book-dir); no change contradicts RULINGS.md; the fixture and the test suite pass (python3 aws-saa-book/tools/tests/run.py).' },
  { key: 'reader', lens: 'Read the exemplar as the reader in READER.md, cold. Is the fast file finishable in twenty minutes and correct as a gist? Does each written deep subsection leave you able to explain the mechanism? Are the spoken answers sayable? Is anything still written for the writer rather than for her (jargon, long sentences, padding, decoration)? This is the last chance to fix the model before it is copied fifty times.' },
]
const criticPrompt = c => `${H}
YOUR TASK: final check of the exemplar and the frozen contract (aws-saa-book/_build/style/exemplar/, STYLE.md, SPEC.json, CONVENTIONS.md, CONVENTIONS-2.md, and aws-saa-book/_build/reports/exemplar-spec-changes.md). ${c.lens}
Write numbered findings with severity (blocker, major, minor), place, what is wrong and the exact change to aws-saa-book/_build/reports/exemplar-critique-${c.key}.md. Do not edit the files.
Result: the report path and the counts by severity.`

const fixPrompt = `${H}
YOUR TASK: apply the findings in aws-saa-book/_build/reports/exemplar-critique-consistency.md and exemplar-critique-reader.md to the exemplar (aws-saa-book/_build/style/exemplar/) and the contract files. Fix every blocker and major and the cheap minors; keep everything consistent with RULINGS.md; keep the test suite passing (python3 aws-saa-book/tools/tests/run.py). Then write "version 1.0 frozen" with today's date at the top of STYLE.md and set "version": "1.0" in SPEC.json if not already set. Record one line per finding in aws-saa-book/_build/reports/exemplar-fix.md.
Result: ok, counts fixed, rejected and deferred, and the test suite status.`

phase('Attempts')
const attempts = await parallel(ATTEMPTS.map(t => () => agent(attemptPrompt(t), { label: `attempt:${t.key}`, phase: 'Attempts', schema: S.attempt, effort: 'high' })))
log(`Attempts done: ${attempts.map((a, i) => `${ATTEMPTS[i].key}=${a && a.ok ? 'ok' : 'failed'}`).join(', ')}`)

phase('Judges')
const judges = (await parallel(JUDGES.map(j => () => agent(judgePrompt(j), { label: `judge:${j.key}`, phase: 'Judges', schema: S.judge, effort: 'high' })))).filter(Boolean)

// script aggregation: Borda count plus weighted mean; the winner must be in the reader judge's top two and have no fatal defect
const keys = ['a', 'b', 'c']
const borda = { a: 0, b: 0, c: 0 }
const mean = { a: 0, b: 0, c: 0 }
const fatal = new Set()
for (const j of judges) {
  (j.ranking || []).forEach((k, i) => { if (borda[k] !== undefined) borda[k] += 2 - i })
  for (const k of keys) {
    const sc = (j.scores && j.scores[k]) || []
    let w = 0, tot = 0
    sc.slice(0, 7).forEach((v, i) => { w += WEIGHTS[i]; tot += WEIGHTS[i] * Number(v || 0) })
    mean[k] += w ? tot / w : 0
  }
  for (const k of (j.fatal || [])) fatal.add(k)
}
for (const k of keys) mean[k] = judges.length ? Math.round((mean[k] / judges.length) * 100) / 100 : 0
const reader = judges.find(j => j.lens === 'reader')
const readerTop2 = reader ? (reader.ranking || []).slice(0, 2) : keys
const ordered = keys.slice().sort((x, y) => (borda[y] - borda[x]) || (mean[y] - mean[x]))
const winner = ordered.find(k => !fatal.has(k) && readerTop2.includes(k)) || ordered.find(k => !fatal.has(k)) || ordered[0]
const verdict = `winner: attempt ${winner}. Borda points: a=${borda.a}, b=${borda.b}, c=${borda.c}. Weighted mean scores (1 to 5): a=${mean.a}, b=${mean.b}, c=${mean.c}. Attempts with a fatal technical defect: ${[...fatal].join(', ') || 'none'}. The reader judge ranked: ${reader ? reader.ranking.join(' > ') : 'no reader verdict'}. Angles: a = first principles, b = exam operator, c = customer conversation.`
log(`Panel: ${verdict}`)

phase('Synthesis')
const synthesis = await agent(synthesisPrompt(verdict), { label: 'synthesis', phase: 'Synthesis', schema: S.done, effort: 'high' })
const critiques = (await parallel(critics.map(c => () => agent(criticPrompt(c), { label: `critic:${c.key}`, phase: 'Synthesis', schema: S.critique, effort: 'high' })))).filter(Boolean)
const fix = await agent(fixPrompt, { label: 'freeze', phase: 'Synthesis', schema: S.done, effort: 'high' })

return {
  workflow: 'exemplar panel',
  attempts: attempts.map((a, i) => a ? { key: ATTEMPTS[i].key, ok: a.ok, words_fast: a.words_fast, words_deep: a.words_deep, lint_errors: a.lint_errors, fact_gaps: a.fact_gaps } : { key: ATTEMPTS[i].key, ok: false }),
  verdict,
  judges: judges.map(j => ({ lens: j.lens, ranking: j.ranking })),
  synthesis: synthesis ? { ok: synthesis.ok, summary: String(synthesis.summary || '').slice(0, 400), problems: (synthesis.problems || []).slice(0, 5) } : null,
  critiques,
  freeze: fix ? { ok: fix.ok, summary: String(fix.summary || '').slice(0, 300) } : null,
}
