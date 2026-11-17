export const meta = {
  name: 'saa-chapter-factory',
  description: 'SAA-C03 Handbook chapter factory: for each chapter in args, plan sources, mine and verify facts, brief, write, edit, verify questions, review, fix and finalize',
  phases: [
    { title: 'Plan', detail: 'select and fetch AWS pages; write the fact demand list' },
    { title: 'Mine', detail: 'extract candidate facts with verbatim quotes, one agent per lens' },
    { title: 'Verify facts', detail: 'register, independent votes per batch, adjudicate, finalize' },
    { title: 'Brief', detail: 'bind sections, traps, question slots, tasks and diagrams to verified facts' },
    { title: 'Write', detail: 'fast file, deep file, questions, tasks, cards, spoken answers, diagrams in parallel' },
    { title: 'Edit', detail: 'close the writing stages, fill fact requests, stitch, sync and lint' },
    { title: 'Verify questions', detail: 'three blind solvers per question, adjudication, one edit round' },
    { title: 'Review', detail: 'unsupported-claim hunter and red team, reader lens, exam lens' },
    { title: 'Fix and finalize', detail: 'apply findings, final gate' },
  ],
}

// args: the JSON printed by "saa.py registry wave-args WAVE", optionally with
//   through: 'verify-facts' | 'finalize' (default 'finalize')   stop after the fact stages, or run everything
//   only:    ['03', '10']                                       restrict to these chapter ids
const ROOT = '.'   // the repository root; agents run with the repo root as their working directory
const A = args || {}
const THROUGH = A.through || 'finalize'
const CHAPTERS = (A.chapters || []).filter(c => !A.only || A.only.includes(c.id))
const TOOL = 'python3 aws-saa-book/tools/saa.py'

const H = `You are one agent in a multi-agent build of a study book, the "SAA-C03 Handbook" (a prep book for the AWS Certified Solutions Architect - Associate exam), in the folder aws-saa-book/ of the repository in your working directory. Your working directory is the repo root.

READ FIRST: aws-saa-book/_build/spec/RULINGS.md (authoritative; its hard rules bind you) and aws-saa-book/_build/style/READER.md (the one reader this book is for).

GROUND RULES
- Write only inside aws-saa-book/. Never run git. Never publish artifacts. Never install system software.
- Run commands one at a time as plain commands from the repo root: ${TOOL} <subcommand> ...   No cd, no pipes, no redirects (use --out), no chaining with && or ;. Use your file tools (Read, Write, Edit) for file work. If a command is refused or asks for approval, do not retry it in another form; note it and continue.
- Evidence comes only from AWS pages saved through the tool (fetch, guide, faq, changes, cases; then search, show, tables). Never use WebFetch or curl. WebSearch is allowed only to discover the URL of an AWS page, which you then fetch with the tool. Your memory supplies questions, never answers: a number, limit, default, date, or a "can / cannot / only / always / never" claim may enter the book only as a verified fact with a verbatim quote. No content from exam-dump sites.
- The contract (read the parts your task names; they are exact): aws-saa-book/_build/style/TOOLS.md (ledger, registry, facts, lint), TOOLS-items.md (sync, questions, cards, spoken answers, tasks), TOOLS-rules.md (gates, matching rules, the brief as shared plan, item status), TOOLS-corpus.md, TOOLS-feeds.md, TOOLS-diagram.md; and for content CONVENTIONS.md, CONVENTIONS-2.md, STYLE.md, SPEC.json. If aws-saa-book/_build/style/exemplar/ exists, it holds the reference chapter: match its depth, tone and layout.
- The running startup example is Callvale: aws-saa-book/_build/style/STARTUP.md (never contradict it; question stems never name it).
- The ledger decides what runs. Before you work, run: ${TOOL} stage show <chapter id>   If the stage you were given is already "pass" and not stale, do nothing and report skipped. Use "stage begin" and "stage end" exactly where your task says, and act on the first word of the answer (GO, SKIP, BLOCKED). If a stage end fails, read the gate errors, fix them and try again; after a third failed attempt stop and report the errors.
- Keep your final answer short: only the result fields. Detail goes into files.
`

const ctx = ch => `CHAPTER ${ch.id} "${ch.title}": folder aws-saa-book/${ch.dir}/, structured data in aws-saa-book/data/${ch.dir}/, work files in aws-saa-book/_build/work/${ch.dir}/. Template: ${ch.template}${ch.xl ? ' with the XL word budget' : ''}. Services: ${(ch.services || []).join(', ') || 'none (pattern, front or synthesis chapter)'}. Exam tasks: ${(ch.tasks || []).join(', ') || 'see the registry'}. See everything about it with: ${TOOL} registry show ${ch.id}`

const S = {
  plan: { type: 'object', properties: { skipped: { type: 'boolean' }, ok: { type: 'boolean' }, sources_fetched: { type: 'integer' }, fetch_failures: { type: 'integer' }, demand_items: { type: 'integer' }, note: { type: 'string' } }, required: ['ok'] },
  mine: { type: 'object', properties: { skipped: { type: 'boolean' }, lens: { type: 'string' }, facts_added: { type: 'integer' }, mech_rejected: { type: 'integer' }, demand_not_found: { type: 'integer' }, note: { type: 'string' } }, required: ['lens', 'facts_added'] },
  register: { type: 'object', properties: { skipped: { type: 'boolean' }, ok: { type: 'boolean' }, facts_total: { type: 'integer' }, hard_total: { type: 'integer' }, conflicts: { type: 'integer' }, batches: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, lens: { type: 'string' } }, required: ['id', 'lens'] } }, note: { type: 'string' } }, required: ['ok', 'batches'] },
  vote: { type: 'object', properties: { batch: { type: 'string' }, votes: { type: 'integer' }, positive: { type: 'integer' }, not_positive: { type: 'integer' }, note: { type: 'string' } }, required: ['batch', 'votes'] },
  adjudicate: { type: 'object', properties: { ok: { type: 'boolean' }, verified: { type: 'integer' }, rejected: { type: 'integer' }, repaired: { type: 'integer' }, pending: { type: 'integer' }, stage_ended: { type: 'boolean' }, revote_batches: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, lens: { type: 'string' } }, required: ['id', 'lens'] } }, note: { type: 'string' } }, required: ['ok', 'verified'] },
  brief: { type: 'object', properties: { skipped: { type: 'boolean' }, ok: { type: 'boolean' }, sections: { type: 'integer' }, traps: { type: 'integer' }, question_slots: { type: 'integer' }, diagrams: { type: 'integer' }, tasks: { type: 'integer' }, demand_unfilled: { type: 'integer' }, note: { type: 'string' } }, required: ['ok'] },
  work: { type: 'object', properties: { skipped: { type: 'boolean' }, ok: { type: 'boolean' }, items: { type: 'integer' }, words: { type: 'integer' }, fact_requests: { type: 'integer' }, note: { type: 'string' } }, required: ['ok'] },
  closer: { type: 'object', properties: { ok: { type: 'boolean' }, prose_passed: { type: 'boolean' }, questions_passed: { type: 'boolean' }, open_fact_requests: { type: 'integer' }, packs: { type: 'array', items: { type: 'object', properties: { lens: { type: 'string' }, path: { type: 'string' } }, required: ['lens', 'path'] } }, questions_in_packs: { type: 'integer' }, note: { type: 'string' } }, required: ['ok', 'packs'] },
  requests: { type: 'object', properties: { ok: { type: 'boolean' }, filled: { type: 'integer' }, unfillable: { type: 'integer' }, batches: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, lens: { type: 'string' } }, required: ['id', 'lens'] } } }, required: ['ok', 'batches'] },
  solve: { type: 'object', properties: { lens: { type: 'string' }, answers_path: { type: 'string' }, answered: { type: 'integer' }, flagged: { type: 'integer' } }, required: ['lens', 'answers_path'] },
  adjq: { type: 'object', properties: { ok: { type: 'boolean' }, passed: { type: 'integer' }, edited: { type: 'integer' }, rejected: { type: 'integer' }, below_min: { type: 'boolean' }, stage_ended: { type: 'boolean' }, packs: { type: 'array', items: { type: 'object', properties: { lens: { type: 'string' }, path: { type: 'string' } }, required: ['lens', 'path'] } }, note: { type: 'string' } }, required: ['ok', 'packs'] },
  review: { type: 'object', properties: { lens: { type: 'string' }, findings_path: { type: 'string' }, blocking: { type: 'integer' }, should: { type: 'integer' }, notes: { type: 'integer' } }, required: ['lens', 'findings_path'] },
  final: { type: 'object', properties: { ok: { type: 'boolean' }, status: { type: 'string' }, fixed: { type: 'integer' }, removed_claims: { type: 'integer' }, questions_reset: { type: 'integer' }, gate_errors: { type: 'array', items: { type: 'string' } }, warnings: { type: 'integer' }, counts: { type: 'string' }, note: { type: 'string' } }, required: ['ok', 'status'] },
}

// ---------------------------------------------------------------- lenses

const LENS_TEXT = {
  numbers: 'LIMITS, QUOTAS, DEFAULTS AND NUMBERS. Work through the quotas or limits page and every table in the chapter pages with the tables command, and adopt rows through "facts adopt" so that the quote and its table header are produced by script. Capture every number, limit, default, range, duration, size and unit that the exam or a sizing conversation uses, each with scope, default-or-max and adjustable.',
  behavior: 'CONCEPTS, BEHAVIOUR, CAPABILITIES AND RESTRICTIONS. From the concept and how-it-works pages: what the service does, how each feature behaves, what it can and cannot do, what is required, what the default behaviour is, what is Regional, zonal or global, what survives a failure. One atomic claim per fact; prefer the sentence where AWS states it most directly. Give each behaviour fact at least two displays (short wordings a writer can link).',
  decisions: 'DECISIONS, COMPARISONS, SECURITY AND COST DIMENSIONS. From best-practice pages, decision guides, security pages and the pricing page (pricing dimensions only: what you pay for; a dollar amount only if a sentence states it together with its Region): the facts that decide between this service and its neighbours and between its own options, and the security and cost statements an architect quotes. Also find one or two official AWS case studies or blog posts about a named company (use the cases command, then fetch the page) and add case-study facts with verbatim quotes.',
  faq: 'THE AWS FAQ. Work through the FAQ pages question by question (use the parsed FAQ index to navigate; quote from the page snapshot): the can-or-cannot answers, the "what is the difference" answers and the limits the FAQ states. These feed the "FAQ quick-fire" section, so prefer short, decisive FAQ sentences. Where the FAQ and the user guide disagree, add both facts and let the conflict queue record it.',
  changes: 'CHANGES SINCE MID-2022. Triage the change feed ("changes for <service> --since 2022-07-01") and the document-history page, and test every item of aws-saa-book/_build/spec/FRESHNESS.md that concerns this chapter as a hypothesis against the current pages. For each change that alters a number, a default or a best answer: add a fact of kind change (date, what changed, and the old value only if an announcement or history row states it verbatim), and make sure a current-truth fact exists that reflects the new state, with its volatility and change items set.',
}
const LENS_SETS = {
  xl: [['numbers'], ['behavior'], ['decisions'], ['faq'], ['changes']],
  deep: [['numbers'], ['behavior'], ['decisions', 'changes'], ['faq']],
  medium: [['numbers', 'changes'], ['behavior', 'decisions'], ['faq']],
  other: [['numbers', 'behavior', 'changes'], ['decisions', 'faq']],
}
const lensesFor = ch => (ch.xl ? LENS_SETS.xl : ch.template === 'deep' ? LENS_SETS.deep : (ch.template === 'medium' || ch.template === 'pattern') ? LENS_SETS.medium : LENS_SETS.other)
  .map(keys => ({ key: keys.join('+'), text: keys.map(k => LENS_TEXT[k]).join('\n\nAND ALSO: ') }))

// ---------------------------------------------------------------- prompts: facts

const planPrompt = ch => `${H}
${ctx(ch)}
YOUR STAGE: plan. Your label for --by options: plan-${ch.id}.
1. ${TOOL} stage begin ${ch.id} plan   (if SKIP: report skipped and stop).
2. Read the registry entry and its exam-guide bullets (registry show), the chapter's entry in aws-saa-book/_build/style/STARTUP.md, the template for this chapter in SPEC.json, and the sections of aws-saa-book/_build/spec/FREQUENCY.md and FRESHNESS.md that concern its services (research input: they tell you what to look for, never what is true).
3. Build the evidence base in the corpus. For each guide of the chapter make sure its index exists (guide), search its full text for the chapter's topics and select the pages to read (deep: 40 to 80 pages; medium: 20 to 40; light family: 8 to 15 per service), then fetch them in one batch. Also fetch and parse the FAQ pages; fetch the quotas page, the pricing page and the document-history page; run "changes for" each service; list case-study candidates; fetch the decision guides, whitepapers and Well-Architected pages the registry names. For a pattern, front or synthesis chapter the whitepapers, decision guides and policy pages are the main sources.
4. Write the fact DEMAND list: the questions this chapter must be able to answer with grounded facts, each tagged to an exam-guide bullet. Cover: every number, limit and default the exam uses for these services; every can-or-cannot; every comparison with a neighbouring service that questions hinge on (FREQUENCY.md section 3); each change in FRESHNESS.md for these services, as a hypothesis; the FAQ items worth a quick-fire question; pricing dimensions; the facts behind Callvale's decision in this chapter; one or two real company examples. Aim for completeness: a missing demand item becomes a missing section.
5. Write aws-saa-book/_build/work/${ch.dir}/brief.v0.json in the shape the "plan" gate requires (TOOLS.md 3.1), and aws-saa-book/_build/work/${ch.dir}/mine-plan.json that assigns the fetched pages and the demand items to these mining lenses: ${lensesFor(ch).map(l => l.key).join(' | ')}.
6. ${TOOL} stage end ${ch.id} plan --counts sources=<n> demand=<n>
Result: ok, counts, and a one-line note.`

const minePrompt = (ch, lens) => `${H}
${ctx(ch)}
YOUR STAGE: mine (another agent opens and closes this stage in the ledger; do not call stage begin or stage end). Your label for --by options: mine-${ch.id}-${lens.key}. First run: ${TOOL} stage show ${ch.id}   If "mine" is already pass and not stale, report skipped and stop.
YOUR LENS: ${lens.text}
How to work:
- Read aws-saa-book/_build/work/${ch.dir}/mine-plan.json and brief.v0.json: your pages and your demand items. Read TOOLS.md section 5 (the fact shape, the mechanical checks M1 to M13, "facts add" and "facts adopt") and the fact schema.
- Read the pages from the corpus with show, search and tables (bounded excerpts; do not dump whole pages). Fetch a page that is missing. For every demand item of your lens, find where AWS states the answer and add a fact whose quote is copied verbatim from the snapshot. Add other exam-relevant facts you meet, even if no demand item asked for them.
- One atomic claim per fact, in plain English, saying no more than the quote says: keep scope, unit, per-what, default-versus-maximum and every condition. Fill qualifiers for limits, quotas and defaults. Set kind, hard, source tier, volatility, exam relevance, the question the fact answers, and the displays writers will link (the canonical value strings). Fact ids are kebab-case and start with the service key.
- Add facts in files of 10 to 25 with: ${TOOL} facts add --file <file> --by mine-${ch.id}-${lens.key}   (and facts adopt for table rows and exact sentences). A fact that fails a mechanical check is not stored: read the error, fix the quote or the claim, and add it again. Never bend a claim to make a check pass.
- When a demand item has no answer in the AWS pages, say so: mark it "not found" in aws-saa-book/_build/work/${ch.dir}/mine-${lens.key}.json with where you looked. When the sources contradict your expectation, record what the source says.
Result: lens, facts added, facts rejected by the mechanical checks and not repaired, demand items not found.`

const registerPrompt = ch => `${H}
${ctx(ch)}
YOUR STAGES: close mine, then register, then open verify-facts. Your label: register-${ch.id}.
1. If "mine" is not yet pass: ${TOOL} stage begin ${ch.id} mine   then   ${TOOL} stage end ${ch.id} mine   (its gate re-runs the mechanical checks; fix or reject facts that fail).
2. ${TOOL} stage begin ${ch.id} register   (if SKIP go to step 5).
3. Be the registrar of this chapter's facts (TOOLS.md section 5): list them (facts list --chapter ${ch.id}); merge duplicates (keep the fact with the most direct quote; supersede or reject the other); make ids, claims and displays consistent; complete missing qualifiers; set hard and exam relevance consistently; check that each fact lives in the right service namespace; work through the conflict queue (facts conflicts --list): where two facts differ because of scope, keep both with clear scope; where one is wrong or older, reject it. Read the mine-*.json notes of the miners: for demand items still "not found" do one more targeted search of the corpus (and fetch a missing page if the registry or a search points to one); update the demand statuses in brief.v0.json.
4. ${TOOL} stage end ${ch.id} register --counts facts=<n> hard=<n>
5. ${TOOL} stage begin ${ch.id} verify-facts   (if SKIP: report batches as an empty list). Then cut the verification batches with: ${TOOL} facts batch --chapter ${ch.id} --lens entail --size 40   and the same for the lenses currency and derive.
Result: ok, the totals, the number of open conflicts, and every batch id with its lens.`

const votePrompt = (ch, b, round) => `${H}
${ctx(ch)}
YOUR JOB: independent verification of one batch of facts, lens "${b.lens}"${round > 1 ? ' (second round: these facts were repaired after a first vote)' : ''}. Your label: verify-${ch.id}-${b.id}${round > 1 ? '-r2' : ''}. You did not write these facts and you must not trust them.
1. ${TOOL} facts packet ${b.id} --out aws-saa-book/_build/facts/packets/${b.id}.json   and read that file. It is your main input (TOOLS.md 5.5).
2. For every fact give a verdict (TOOLS.md 5.4 lists the verdicts per lens):
   - entail: does the quote, read in its context and under its headings, support the claim exactly? Check scope, unit, per-what, default versus maximum, "up to" versus "exactly", every condition, and that the claim is about the same service and feature as the quote. "partial" when the claim says more than the quote or drops a condition. "unsure" when you cannot tell. Both count as not positive, which is the right outcome when in doubt.
   - currency: read the change items in the packet. Does the fact describe the state AFTER the newest relevant change? You may search and show the corpus for a newer or conflicting statement. "outdated" or "unsure" when in doubt.
   - derive: redo the derivation from the quoted numbers.
   Give a one-line reason for every verdict that is not positive.
3. Write your votes to aws-saa-book/_build/facts/votes-in/${b.id}${round > 1 ? '-r2' : ''}.json in the vote schema and submit them: ${TOOL} facts vote --file <that file> --by verify-${ch.id}-${b.id}${round > 1 ? '-r2' : ''}
Result: the batch id, votes cast, how many positive and how many not.`

const adjudicatePrompt = ch => `${H}
${ctx(ch)}
YOUR JOB: adjudicate this chapter's facts after the independent votes. Your label: adjudicate-${ch.id}.
1. ${TOOL} facts finalize --chapter ${ch.id}   and read the result (verified, disputed, rejected, pending).
2. For each disputed fact: read it with its votes (facts show). Decide by evidence, not by wish. Either repair it once with "facts amend" so that the claim says exactly what the quote supports (narrow the scope, add the condition, fix the unit), or attach a better quote that you find in the corpus, or reject it (facts amend ID --reject). Resolve open conflicts. A repaired fact needs fresh independent votes.
3. For pending facts (a required lens has no vote): they need a batch too.
4. If any fact was repaired or is pending: cut new batches (facts batch --chapter ${ch.id} --lens entail --size 40, and currency and derive) and report their ids as revote_batches; do not end the stage.
5. If nothing needs a new vote: ${TOOL} facts finalize --chapter ${ch.id}   then   ${TOOL} facts render --all   then   ${TOOL} stage end ${ch.id} verify-facts --counts verified=<n> rejected=<n>   and report stage_ended true.
Also update the demand statuses in aws-saa-book/_build/work/${ch.dir}/brief.v0.json (filled with fact ids, or not found).
Result: ok, counts, stage_ended, and the revote batches (an empty list if none).`

const adjudicateClosePrompt = ch => `${H}
${ctx(ch)}
YOUR JOB: close the fact verification of this chapter after the second vote. Your label: close-facts-${ch.id}.
1. ${TOOL} facts finalize --chapter ${ch.id}   (a repaired fact that is disputed again becomes rejected; that is intended).
2. Anything still pending or in an open conflict: reject it with a reason (facts amend ID --reject, or facts conflicts --resolve). An ungrounded fact must not block the chapter and must not enter it.
3. ${TOOL} facts render --all   then   ${TOOL} stage end ${ch.id} verify-facts --counts verified=<n> rejected=<n>
4. Update the demand statuses in aws-saa-book/_build/work/${ch.dir}/brief.v0.json.
Result: ok, counts, stage_ended.`

// ---------------------------------------------------------------- prompts: brief and writing

const briefPrompt = ch => `${H}
${ctx(ch)}
YOUR STAGE: brief. Your label: brief-${ch.id}. The brief is the shared plan from which six writers work IN PARALLEL without seeing each other's output, so it must fix every name they share. Read TOOLS-rules.md R4 and the "brief" gate in TOOLS.md 3.1 first.
1. If "verify-facts" is still running, close it: ${TOOL} facts finalize --chapter ${ch.id}   then   ${TOOL} stage end ${ch.id} verify-facts
2. ${TOOL} stage begin ${ch.id} brief   (if SKIP: report skipped).
3. Inputs: the verified facts (${TOOL} facts card --chapter ${ch.id} --out aws-saa-book/_build/work/${ch.dir}/fact-cards.md, then read it; also the facts of neighbouring chapters you want to reuse by id), brief.v0.json (the demand list and what stayed unfilled), the registry entry with its bullets, the chapter's entry in STARTUP.md, the template of this chapter in SPEC.json (sections, word limits, counts), CONVENTIONS.md (and CONVENTIONS-2.md for a pattern, front or synthesis chapter), STYLE.md, LEARNING.md section 1 (what each section is for) and section 3 (anti-skim devices), and the frequency notes for this chapter.
4. Write aws-saa-book/_build/work/${ch.dir}/brief.json exactly in the shape the gate requires, and decide in it:
   - sections: for each hand-written file every section with its exact heading text and section id; for "How it works" every subsection as an assertion heading (a full-sentence claim that a verified fact supports) in teaching order, built as a causal chain (follow the request, the packet or the object), each with its facts and bullets. Depth matters: the reader asked for more detail and nuance than a 5,700-word chapter gave; put edge cases into "Go deeper" blocks.
   - traps: the real, common wrong beliefs for this chapter, each with a trap id, the belief, the truth and its facts. Questions and the Signals and traps section draw on these ids.
   - the comparison tables (which neighbours, which deciding question), the signal rows with their "but not if", the numbers A-list and B-list, the FAQ quick-fire items (each from a verified FAQ fact), the Changed recently entries (each from a change fact), the Callvale problem and decision record, the real-world case (only if a verified case-study fact exists).
   - question_slots: one slot per question to write (the template's write count), each with bullet, concept, difficulty, type, layer and exam-English words, covering every bullet, with the twin pairs and multiple-response slots planned, and at least half of the slots built on a trap.
   - terms, tasks (type, title, the misconception each one kills), spoken prompts (customer wording, taken from STARTUP.md where it fits), cards, and diagrams (id, kind, claim, alt text and the step sentences; include the Callvale before and after pair).
   Use only verified facts. Where the chapter needs a fact that does not exist, do not plan a sentence on it: file a fact request (TOOLS.md 5.6) and note it.
5. ${TOOL} stage end ${ch.id} brief --counts sections=<n> traps=<n> slots=<n>
Result: ok and the counts.`

const fastPrompt = ch => `${H}
${ctx(ch)}
YOUR JOB: write the file aws-saa-book/${ch.dir}/1-fast.md (stage "prose"; another agent opens and closes the stage, so do not call stage begin or stage end). Your label: fast-${ch.id}. If the stage "prose" is already pass and not stale, report skipped.
This is the file the reader opens first and can finish in about twenty minutes. She skims: headings, tables and captions must give a CORRECT gist on their own, and the Predict, Check and Recap items must test what a skim misses.
Read: aws-saa-book/_build/work/${ch.dir}/brief.json (it fixes headings, section ids, traps, tables and diagram ids; follow it exactly), fact-cards.md in the same folder (ready-made fact links), CONVENTIONS.md sections A to I (and CONVENTIONS-2.md for a pattern, front or synthesis chapter), STYLE.md, the template limits in SPEC.json, the chapter's entry in STARTUP.md, and the exemplar if it exists.
Write every section of the template in order, with every device in its exact syntax. Every hard fact is a fact link whose text contains the canonical value. If you need a fact that is not verified, do not write the sentence: file a request (${TOOL} facts request --chapter ${ch.id} ...) and leave the sentence out. Plain English for a second-language reader: short sentences, one term per concept, terms introduced as STYLE.md says, no idioms, no emoji.
Check your file until it has no errors: ${TOOL} lint ${ch.id} --file 1-fast.md --draft
Result: ok, the word count, and the number of fact requests you filed.`

const deepPrompt = ch => `${H}
${ctx(ch)}
YOUR JOB: write the file aws-saa-book/${ch.dir}/2-deep.md (stage "prose"; another agent opens and closes the stage, so do not call stage begin or stage end). Your label: deep-${ch.id}. If the stage "prose" is already pass and not stale, report skipped.
This is where the reader gets real understanding: enough to explain the service to a customer and to reason through an exam question she has never seen. She asked for MORE depth than a typical prep chapter, delivered in short subsections she can finish one at a time.
Read: aws-saa-book/_build/work/${ch.dir}/brief.json (it fixes headings, section ids, the order of the subsections, traps and diagram ids; follow it exactly), fact-cards.md in the same folder, the pages behind the facts where you need to understand a mechanism (show and search on the corpus; understanding may come from the pages, but every hard claim you write must be a verified fact link), CONVENTIONS.md sections A to I (and CONVENTIONS-2.md for a pattern, front or synthesis chapter), STYLE.md, the template limits in SPEC.json (use the budget: reach at least the minimum words), the chapter's entry in STARTUP.md, and the exemplar if it exists.
How it works: each subsection has an assertion heading with a time box, explains a mechanism as cause and effect in order (follow the request, the packet or the object), names what breaks and why, and ends with a Stop and answer that applies the idea to a new case. Put edge cases and nuance into collapsed Go deeper blocks. Then the numbers that decide answers, Callvale's decision record, the FAQ quick-fire with the verbatim FAQ sentences, and the real-world case if the brief has one. No padding: a paragraph that no question, card, signal, trap or spoken answer could depend on does not belong.
Every hard fact is a fact link whose text contains the canonical value. If you need a fact that is not verified, do not write the sentence: file a request (${TOOL} facts request --chapter ${ch.id} ...).
Check your file until it has no errors: ${TOOL} lint ${ch.id} --file 2-deep.md --draft
Result: ok, the word count, and the number of fact requests you filed.`

const questionPrompt = (ch, part, parts) => `${H}
${ctx(ch)}
YOUR JOB: write original exam-style questions for this chapter (stage "questions"; another agent opens and closes the stage, so do not call stage begin or stage end). Your label: questions-${ch.id}-${part}. If the stage "questions" is already pass and not stale, report skipped.
Read: aws-saa-book/_build/work/${ch.dir}/brief.json (question_slots, traps), fact-cards.md in the same folder, STYLE.md (the question-writing standard: stem anatomy, one qualifier, distractor types, explanation format, think-aloud format, failure modes), CONVENTIONS.md section J and CONVENTIONS-2.md section J (the JSON shape), the question schema, TOOLS-items.md 7.1 and 7.2 (add and lint), and data/exam-english.json. For the register of real questions read the official sample questions if they are in the corpus (search for "AWS-Certified-Solutions-Architect-Associate_Sample-Questions"), as a format reference only.
${parts > 1 ? `There are ${parts} question writers. You are writer ${part}: write the question_slots whose position in the list (counting from 1) leaves remainder ${part % parts} when divided by ${parts}. Twin pairs: write both twins if the first twin's slot is yours.` : 'Write every slot of the brief.'}
Each question: a scenario stem with a business requirement and exactly one qualifier; options that are parallel in form and similar in length; every distractor a real in-scope service or setting that fails a stated requirement for a fact-grounded reason and that encodes one named misconception (a trap id where one fits); the explanation in the fixed format (deciding phrase, why right, why not each other option, the "if the stem said ... instead" twin line, review link); facts cited by id; tags complete. Stems say "A company", never Callvale. No question may be decided by a number that changed in the last 24 months. Never copy or paraphrase a question from any exam-dump or practice-test site.
Add them with: ${TOOL} q add --chapter ${ch.id} --file <file> --by questions-${ch.id}-${part}   and run   ${TOOL} q lint ${ch.id}   until your questions have no errors.
Result: ok, questions added, fact requests filed.`

const tasksPrompt = ch => `${H}
${ctx(ch)}
YOUR STAGE: tasks. Your label: tasks-${ch.id}.
1. ${TOOL} stage begin ${ch.id} tasks   (if SKIP: report skipped).
2. Read brief.json (the planned tasks and the misconception each one kills), STYLE.md (hands-on task rules), LEARNING.md section 7, the task schema, TOOLS-items.md section 8 and TOOLS-rules.md R6. Write aws-saa-book/data/${ch.dir}/tasks.json: small tasks the reader does in her own AWS account, in AWS CloudShell: Look tasks (read-only, 3 to 5 minutes), Try tasks (1 to 3 resources, 10 to 15 minutes, with a break-it-on-purpose step where it teaches), and a Lab only if the template allows one. Base each on an official tutorial or CLI example in the corpus where one exists (fetch it) and note the source. Secure by default; tag everything; a cost line; what it costs per day if forgotten; cleanup in reverse order; a verify command; a read-only alternative for a locked-down corporate account; the label "checked against docs, not run in a real account". Describe the place to look, not a click path.
3. ${TOOL} tasks lint ${ch.id}   and   ${TOOL} tasks check-cli ${ch.id}   until clean.
4. ${TOOL} stage end ${ch.id} tasks --counts tasks=<n>
Result: ok and the number of tasks.`

const cardsSpeakPrompt = ch => `${H}
${ctx(ch)}
YOUR STAGES: cards, then speak. Your label: say-${ch.id}.
A. Cards. ${TOOL} stage begin ${ch.id} cards   (if SKIP go to B). Read brief.json, fact-cards.md, STYLE.md (flashcard atomicity rules), LEARNING.md section 9, the card schema and TOOLS-items.md 7.6 and TOOLS-rules.md R5 (which card types are hand-written and which are generated). Write the hand-written cards for this chapter (one fact per card, short answers, the front names its context, values by fact id) with "cards add", run "cards lint ${ch.id}" until clean, then   ${TOOL} stage end ${ch.id} cards --counts cards=<n>
B. Spoken answers. ${TOOL} stage begin ${ch.id} speak   (if SKIP stop). Read LEARNING.md section 5 (the four moves with their fixed starters, the 10-second and 60-second answers written for speech, the skeleton, must-say facts, must-not-say errors, follow-ups) and its filled example, STYLE.md, the speak schema, and the customer questions planned in brief.json and STARTUP.md. Write the spoken-answer items: each prompt in a customer's words, a 10-second answer, a 60-second answer as lines for speech (short sentences, one line per breath group, numbers written as spoken), the keyword skeleton, key points marked must or nice with their fact ids, must-not-say errors, terms, and two follow-up questions. Read every 60-second answer back to yourself: it must sound like a person talking to a customer, not like an essay. Add with "speak add", run "speak lint ${ch.id}" until clean, then   ${TOOL} stage end ${ch.id} speak --counts speak=<n>
Result: ok and the number of cards and spoken items.`

const diagramsPrompt = ch => `${H}
${ctx(ch)}
YOUR STAGE: diagrams. Your label: diagrams-${ch.id}.
1. ${TOOL} stage begin ${ch.id} diagrams   (if SKIP: report skipped).
2. Read aws-saa-book/_build/style/TOOLS-diagram.md (spec, kinds, style guide) and the diagrams planned in aws-saa-book/_build/work/${ch.dir}/brief.json (ids, kinds, claims, alt text and step sentences are fixed there; keep them).
3. For each planned diagram: write the spec to aws-saa-book/diagrams/src/<id>.json, build it, run the diagram lint, make the preview screenshot, then LOOK at the PNG with your Read tool and check: no overlap or clipping; arrows end on node edges and cross no node; every arrow labelled or numbered; readable in the phone-width panel; both themes legible; the one claim obvious in five seconds; official icons; at most 12 nodes. Improve and rebuild, at most three rounds per diagram. A diagram shows structure and flow: put no AWS number or limit into it unless it is the display string of a verified fact named in the brief. If a diagram cannot be made clean, simplify it rather than ship a crowded one.
4. ${TOOL} stage end ${ch.id} diagrams --counts diagrams=<n>
Result: ok and the number of diagrams built.`

const closerPrompt = ch => `${H}
${ctx(ch)}
YOUR JOB: close the two multi-writer stages and open question verification. Your label: closer-${ch.id}.
1. Prose. If "prose" is not yet pass: ${TOOL} stage begin ${ch.id} prose   then   ${TOOL} stage end ${ch.id} prose   Its gate is the chapter lint in draft mode over the hand-written files. If it fails, fix the reported errors in the files (structure, fact links, banned words, budgets; do not weaken content to pass) and repeat begin and end, at most three attempts.
2. Questions. If "questions" is not yet pass and this template has questions: ${TOOL} stage begin ${ch.id} questions   then   ${TOOL} stage end ${ch.id} questions   Fix lint errors in the questions (with "q add --replace"), remove near-duplicates between the writers (q dedupe), and repeat, at most three attempts.
3. Count the open fact requests: ${TOOL} facts request --list --status open --chapter ${ch.id}
4. If the template has questions: ${TOOL} stage begin ${ch.id} verify-questions   then build the three blind packs (TOOLS-items.md 7.3): ${TOOL} q pack --chapter ${ch.id} --lens closed --out aws-saa-book/_build/qbank/packs/${ch.id}-r0-closed.json   and the same for the lenses open and ambiguity. If the stage answers SKIP, report an empty pack list.
Result: ok, whether each stage passed, the number of open fact requests, the packs with their lens and path, and the number of questions in a pack.`

const requestsPrompt = ch => `${H}
${ctx(ch)}
YOUR JOB: fill the open fact requests of this chapter. Writers left out sentences because a fact was missing. Your label: requests-${ch.id}.
List them (${TOOL} facts request --list --status open --chapter ${ch.id}). For each: search the corpus, fetch a page if needed, and either add the fact with a verbatim quote (facts add or facts adopt, --by requests-${ch.id}), or, for a request for another display of an existing fact, add the display with facts amend, or close the request as unfillable with a note that says where you looked (facts request --close ID --unfillable --note ...). Then cut verification batches for the new facts (facts batch --chapter ${ch.id} --lens entail --size 40; also currency and derive).
Result: ok, filled, unfillable, and the batch ids with their lens (an empty list if there are none).`

const editPrompt = ch => `${H}
${ctx(ch)}
YOUR STAGE: edit. Your label: edit-${ch.id}. Several writers worked in parallel from one brief; you make their work one chapter.
1. ${TOOL} stage begin ${ch.id} edit   (if SKIP: report skipped; if BLOCKED because a writing stage has not passed, report that).
2. Facts: ${TOOL} facts finalize --chapter ${ch.id}   then close each filled request (facts request --close ID --fact FACT) and, where a request was filled, write the sentence the writer left out, in the right place. A sentence whose request is unfillable stays out.
3. Read the whole chapter as the reader would: 1-fast.md, then 2-deep.md, then the generated files after "${TOOL} sync ${ch.id}". Fix: repetition between the fast and the deep file (the fast file gives the gist, the deep file the mechanism); terms used before they are introduced; a different name for the same thing; a diagram, trap or section the text refers to that does not exist; contradictions with STARTUP.md; places where a skim would give a wrong gist; sentences that are too long or use idioms. Check that every exam-guide bullet of the chapter is really taught somewhere (registry show ${ch.id}).
4. ${TOOL} sync ${ch.id}   and   ${TOOL} lint ${ch.id}   until there are no errors; reduce warnings where it is cheap.
5. ${TOOL} stage end ${ch.id} edit --counts words=<n>
Result: ok, the word count, and anything you could not resolve.`

const SOLVERS = {
  closed: 'You are the CLOSED-BOOK EXPERT. Answer from your own knowledge of AWS, as a well-prepared candidate would, without the corpus and without the web. For each item first state, before reading the options, what the solution should be (field stem_only); then choose.',
  open: 'You are the OPEN-BOOK VERIFIER. For each item find the answer in the AWS pages saved in the corpus (search and show; fetch a page if it is missing) and in the verified facts (facts list, facts show). In "citations" give, for EVERY option label, a verified fact id or a source_id with a verbatim quote: why the correct option is right, and why each other option fails a requirement in the stem.',
  ambiguity: 'You are the AMBIGUITY HUNTER. For each item choose the best answer, then build the strongest honest case that one of the OTHER options is also correct, or that the stem lacks a constraint needed to decide, or that wording cues give the answer away (field "case"). Set "flag" to a sentence whenever a careful candidate could defend a second answer.',
}
const solvePrompt = (ch, pack, round) => `${H}
${ctx(ch)}
YOUR JOB: blind solving of this chapter's questions, round ${round}. ${SOLVERS[pack.lens]} Your label: solve-${ch.id}-${pack.lens}-r${round}.
STRICT: your only input about the questions is the pack file ${pack.path} (TOOLS-items.md 7.3 describes it and the answer format). Do not open anything under aws-saa-book/data/ that holds questions, any 5-quiz.md, any file under aws-saa-book/_build/qbank/ other than your pack, or any other solver's answers: that would make your vote worthless. Set "flag" whenever you see a second defensible answer or a missing constraint; do not guess what the author meant.
Write your answers to ${pack.path.replace('.json', '.answers.json')} in the answer format.
Result: lens, the answers path, items answered, items flagged.`

const adjQPrompt = (ch, packs, round) => `${H}
${ctx(ch)}
YOUR JOB: adjudicate the blind solving of this chapter's questions, round ${round}. Your label: adjq-${ch.id}-r${round}. Read TOOLS-items.md 7.4.
1. ${TOOL} q adjudicate --chapter ${ch.id} --answers ${packs.map(p => p.path.replace('.json', '.answers.json')).join(' ')}
${round === 0 ? `2. For every question in needs_edit: read the reasons and the solvers' flags and cases (they are in the question's verification block: q list, then read the question), and edit the question ONCE so that exactly the intended answer is correct and no wording cue gives it away (add the missing constraint to the stem, make a distractor clearly fail a stated requirement, fix a stale fact). If a question is unsound at the root, do not rescue it: let it be rejected. Save edits with "q add --replace".
3. If any question was edited: build three fresh packs for round 1 (q pack --chapter ${ch.id} --lens closed --round 1 --out aws-saa-book/_build/qbank/packs/${ch.id}-r1-closed.json, and the same for open and ambiguity) and report them; do not end the stage.
4. If no question needed an edit: ${TOOL} q adjudicate --chapter ${ch.id} --select   then   ${TOOL} sync ${ch.id}   then   ${TOOL} stage end ${ch.id} verify-questions --counts verified=<n> rejected=<n>   and report an empty pack list and stage_ended true.` : `2. Questions that fail again are rejected by the tool; that is intended.
3. ${TOOL} q adjudicate --chapter ${ch.id} --select   If it reports that the counts cannot be met (below the shipped count), report below_min true and do not end the stage. Otherwise   ${TOOL} sync ${ch.id}   then   ${TOOL} stage end ${ch.id} verify-questions --counts verified=<n> rejected=<n>   and report stage_ended true with an empty pack list.`}
Result: ok, passed, edited, rejected, below_min, stage_ended, and the round-1 packs (lens and path) if any.`

const topUpPrompt = ch => `${H}
${ctx(ch)}
YOUR JOB: this chapter has fewer verified questions than it must ship. Your label: topup-${ch.id}. Find out how many are missing and which slots lost their question (${TOOL} q list --chapter ${ch.id}, the brief's question_slots, and aws-saa-book/_build/qbank/rejected.jsonl with the reasons). Write replacements for the missing slots plus two spares, to the full standard in STYLE.md, avoiding the defects that got the earlier ones rejected. Add them with "q add --by topup-${ch.id}", lint them, then build three fresh packs for the new candidates: ${TOOL} q pack --chapter ${ch.id} --lens closed --out aws-saa-book/_build/qbank/packs/${ch.id}-r2-closed.json   and the same for open and ambiguity.
Result: ok, and the packs (lens and path).`

const REVIEW = {
  claims: 'LENS "claims": the unsupported-claim hunter and technical red team. (a) Read every sentence of the hand-written files and the generated files and hunt for claims that are stated as fact without a fact link, or whose link does not really support the sentence around it (the link text is right but the sentence says more). (b) Pick the 15 to 20 statements most likely to be wrong, outdated or oversimplified, and try to refute each from the AWS pages in the corpus, with quotes. Also check tables row by row, the spoken answers, the task steps and the diagram texts.',
  reader: 'LENS "reader": read as the reader in READER.md. First skim only headings, bold text, tables and captions: is the gist you get correct, and could you answer the Stop-and-answer and Check items from the skim alone (you should not be able to)? Then read fully: where is a term used before it is explained, a sentence too long, an idiom, a leap in the explanation, a mechanism described but not explained as cause and effect, a section that is padding, a spoken answer that does not sound like speech, a task that teaches nothing? Is the depth there: could she now explain this service to a customer and reason through an unseen question?',
  exam: 'LENS "exam": the exam coach. Are the signals real and do their "but not if" guards hold? Are the traps common beliefs rather than trivia? Does every exam-guide bullet of the chapter have a section and questions? Do the comparison tables end in the question that actually decides? Read the questions as an item writer: realistic register, one qualifier, plausible distractors with named misconceptions, explanations that teach; is the difficulty mix right; do twins differ by one deciding phrase? Is anything examinable missing that FREQUENCY.md reports as commonly asked?',
}
const reviewPrompt = (ch, lens) => `${H}
${ctx(ch)}
YOUR JOB: review this finished chapter. ${REVIEW[lens]} Your label: review-${ch.id}-${lens}. You did not write it; assume it contains errors and find them.
Run   ${TOOL} sync ${ch.id}   first so the generated files are current, then read all files of aws-saa-book/${ch.dir}/ and the data in aws-saa-book/data/${ch.dir}/.
Write your findings to aws-saa-book/_build/work/${ch.dir}/findings/${lens}.json in the shape the "findings" gate requires (TOOLS.md 3.1): each with file, section, a quote of the place, type, severity (blocking = wrong, ungrounded or misleading; should; note), your evidence (a fact id, or a source_id with a verbatim quote, or the rule broken), status open. Do not edit the chapter.
Result: lens, the findings path, and the counts by severity.`

const fixPrompt = ch => `${H}
${ctx(ch)}
YOUR STAGES: close review, then fix, then finalize. Your label: fix-${ch.id}.
1. ${TOOL} stage begin ${ch.id} review   then   ${TOOL} stage end ${ch.id} review   (its gate checks that the findings files exist).
2. ${TOOL} stage begin ${ch.id} fix   Read every findings file in aws-saa-book/_build/work/${ch.dir}/findings/. For each finding, blocking first: check it against the evidence, then fix the text, or remove or soften an ungroundable claim, or reject the finding with a reason. A hard claim that cannot be grounded is removed, never kept on trust. Record status and resolution in the findings files. For a defective question: fix it only if the fix cannot change which answer is correct (wording, explanation); otherwise retire it if the chapter still has enough verified questions, or reset it for a new verification (TOOLS-rules.md R5) and count it as questions_reset.
3. ${TOOL} sync ${ch.id}   and   ${TOOL} lint ${ch.id}   until clean; then   ${TOOL} stage end ${ch.id} fix --counts fixed=<n> removed=<n>
4. If you reset no question: ${TOOL} stage begin ${ch.id} finalize   then   ${TOOL} facts render --all   then   ${TOOL} stage end ${ch.id} finalize   If the final gate fails, fix what it reports and try again (at most three attempts). If you reset questions, do not finalize; report questions_reset.
Result: ok, the chapter status from the ledger, counts, questions_reset, remaining gate errors (first five), and the number of warnings.`

const finalizePrompt = ch => `${H}
${ctx(ch)}
YOUR STAGE: finalize. Your label: finalize-${ch.id}.
${TOOL} stage begin ${ch.id} finalize   then   ${TOOL} sync ${ch.id}   then   ${TOOL} facts render --all   then   ${TOOL} stage end ${ch.id} finalize   If the final gate fails, fix what it reports (small repairs only; never weaken a check or a fact) and try again, at most three attempts.
Result: ok, the chapter status from the ledger, remaining gate errors (first five), the number of warnings.`

// ---------------------------------------------------------------- orchestration

const short = (s, n) => String(s || '').slice(0, n || 200)
const hasQuestions = ch => !ch.counts || (ch.counts.questions_ship || 0) > 0
const ORDER = ['plan', 'mine', 'register', 'verify-facts', 'brief', 'prose', 'questions', 'tasks', 'cards', 'speak', 'diagrams', 'edit', 'verify-questions', 'review', 'fix', 'finalize']
const needs = (ch, stage) => ORDER.indexOf(ch.next_stage || 'plan') <= ORDER.indexOf(stage)

async function votes(ch, batches, round) {
  if (!batches || !batches.length) return []
  return (await parallel(batches.map(b => () => agent(votePrompt(ch, b, round), { label: `${ch.id}:vote:${b.id}${round > 1 ? ':r2' : ''}`, phase: 'Verify facts', schema: S.vote, effort: 'high' })))).filter(Boolean)
}

async function factsPhase(ch) {
  const plan = await agent(planPrompt(ch), { label: `${ch.id}:plan`, phase: 'Plan', schema: S.plan, effort: 'high' })
  if (!plan || !plan.ok) return { ok: false, at: 'plan', note: short(plan && plan.note) }
  const mined = (await parallel(lensesFor(ch).map(l => () => agent(minePrompt(ch, l), { label: `${ch.id}:mine:${l.key}`, phase: 'Mine', schema: S.mine, effort: 'medium' })))).filter(Boolean)
  const reg = await agent(registerPrompt(ch), { label: `${ch.id}:register`, phase: 'Verify facts', schema: S.register, effort: 'high' })
  if (!reg || !reg.ok) return { ok: false, at: 'register', note: short(reg && reg.note) }
  await votes(ch, reg.batches, 1)
  let adj = await agent(adjudicatePrompt(ch), { label: `${ch.id}:adjudicate`, phase: 'Verify facts', schema: S.adjudicate, effort: 'high' })
  if (adj && adj.revote_batches && adj.revote_batches.length) {
    await votes(ch, adj.revote_batches, 2)
    adj = await agent(adjudicateClosePrompt(ch), { label: `${ch.id}:close-facts`, phase: 'Verify facts', schema: S.adjudicate, effort: 'medium' })
  }
  const facts = { mined: mined.reduce((n, m) => n + (m.facts_added || 0), 0), verified: adj && adj.verified, rejected: adj && adj.rejected }
  log(`${ch.id} ${ch.slug}: facts verified ${facts.verified} (mined ${facts.mined}, rejected ${facts.rejected})`)
  return { ok: !!(adj && adj.ok), at: 'verify-facts', facts }
}

async function verifyQuestions(ch, packs) {
  let round = 0
  let current = packs
  let adj = null
  let toppedUp = false
  while (current && current.length === 3) {
    await parallel(current.map(p => () => agent(solvePrompt(ch, p, round), { label: `${ch.id}:solve:${p.lens}:r${round}`, phase: 'Verify questions', schema: S.solve, effort: 'high' })))
    adj = await agent(adjQPrompt(ch, current, round === 0 ? 0 : 1), { label: `${ch.id}:adjq:r${round}`, phase: 'Verify questions', schema: S.adjq, effort: 'high' })
    if (!adj) break
    if (adj.packs && adj.packs.length === 3) { current = adj.packs; round += 1; continue }
    if (adj.below_min && !toppedUp) {
      toppedUp = true
      const top = await agent(topUpPrompt(ch), { label: `${ch.id}:topup`, phase: 'Verify questions', schema: S.adjq, effort: 'high' })
      if (top && top.packs && top.packs.length === 3) { current = top.packs; round = 0; continue }
    }
    break
  }
  return adj
}

async function writePhase(ch) {
  const brief = await agent(briefPrompt(ch), { label: `${ch.id}:brief`, phase: 'Brief', schema: S.brief, effort: 'high' })
  if (!brief || !brief.ok) return { ok: false, at: 'brief', note: short(brief && brief.note) }
  const qParts = hasQuestions(ch) ? (ch.template === 'deep' ? 2 : 1) : 0
  const writers = [
    () => agent(fastPrompt(ch), { label: `${ch.id}:fast`, phase: 'Write', schema: S.work, effort: 'high' }),
    () => agent(deepPrompt(ch), { label: `${ch.id}:deep`, phase: 'Write', schema: S.work, effort: 'high' }),
    () => agent(tasksPrompt(ch), { label: `${ch.id}:tasks`, phase: 'Write', schema: S.work }),
    () => agent(cardsSpeakPrompt(ch), { label: `${ch.id}:cards-speak`, phase: 'Write', schema: S.work, effort: 'high' }),
    () => agent(diagramsPrompt(ch), { label: `${ch.id}:diagrams`, phase: 'Write', schema: S.work }),
  ]
  for (let p = 1; p <= qParts; p++) writers.push(() => agent(questionPrompt(ch, p, qParts), { label: `${ch.id}:questions:${p}`, phase: 'Write', schema: S.work, effort: 'high' }))
  await parallel(writers)

  const closer = await agent(closerPrompt(ch), { label: `${ch.id}:closer`, phase: 'Edit', schema: S.closer, effort: 'medium' })
  if (closer && closer.open_fact_requests > 0) {
    const req = await agent(requestsPrompt(ch), { label: `${ch.id}:requests`, phase: 'Edit', schema: S.requests, effort: 'high' })
    if (req && req.batches && req.batches.length) await votes(ch, req.batches, 1)
  }
  const editP = agent(editPrompt(ch), { label: `${ch.id}:edit`, phase: 'Edit', schema: S.work, effort: 'high' })
  const verifyP = (closer && closer.packs && closer.packs.length === 3) ? verifyQuestions(ch, closer.packs) : Promise.resolve(null)
  const [edit, adjq] = await Promise.all([editP, verifyP])

  const lenses = (ch.template === 'deep' || ch.template === 'medium' || ch.template === 'pattern') ? ['claims', 'reader', 'exam'] : ['claims', 'reader']
  const reviews = (await parallel(lenses.map(l => () => agent(reviewPrompt(ch, l), { label: `${ch.id}:review:${l}`, phase: 'Review', schema: S.review, effort: 'high' })))).filter(Boolean)
  let fin = await agent(fixPrompt(ch), { label: `${ch.id}:fix`, phase: 'Fix and finalize', schema: S.final, effort: 'high' })
  if (fin && fin.questions_reset > 0) {
    const again = await agent(closerPrompt(ch), { label: `${ch.id}:repack`, phase: 'Verify questions', schema: S.closer, effort: 'low' })
    if (again && again.packs && again.packs.length === 3) await verifyQuestions(ch, again.packs)
    fin = await agent(finalizePrompt(ch), { label: `${ch.id}:finalize`, phase: 'Fix and finalize', schema: S.final, effort: 'medium' })
  }
  log(`${ch.id} ${ch.slug}: ${fin ? fin.status : 'no final result'}`)
  return {
    ok: !!(fin && fin.ok), at: 'finalize', status: fin && fin.status,
    questions: adjq ? { passed: adjq.passed, edited: adjq.edited, rejected: adjq.rejected, below_min: !!adjq.below_min } : null,
    review: reviews.map(r => `${r.lens}: ${r.blocking || 0} blocking, ${r.should || 0} should`),
    fix: fin ? { fixed: fin.fixed, removed_claims: fin.removed_claims, warnings: fin.warnings, gate_errors: (fin.gate_errors || []).slice(0, 5).map(e => short(e, 160)) } : null,
    edit_note: short(edit && edit.note, 160),
  }
}

async function runChapter(ch) {
  const out = { id: ch.id, slug: ch.slug }
  if (needs(ch, 'verify-facts')) {
    out.facts = await factsPhase(ch)
    if (!out.facts.ok) { out.blocked = out.facts.at; return out }
  }
  if (THROUGH === 'verify-facts') return out
  out.write = await writePhase(ch)
  if (!out.write.ok) out.blocked = out.write.at
  return out
}

if (!CHAPTERS.length) return { error: 'no chapters in args' }
log(`Factory: ${CHAPTERS.map(c => c.id + ' ' + c.slug).join(', ')} (through ${THROUGH})`)
const results = await parallel(CHAPTERS.map(ch => () => runChapter(ch)))
return {
  workflow: 'chapter factory',
  wave: A.wave,
  through: THROUGH,
  ready: results.filter(r => r && r.write && r.write.status === 'ready').map(r => r.id),
  facts_done: results.filter(r => r && r.facts && r.facts.ok).map(r => r.id),
  blocked: results.filter(r => r && r.blocked).map(r => ({ id: r.id, at: r.blocked })),
  chapters: results,
}
