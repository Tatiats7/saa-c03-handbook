export const meta = {
  name: 'saa-07-finish',
  description: 'Chapter 07: fill the open fact requests, resolve the disputed fact, independent votes, finalize facts and the chapter',
  phases: [
    { title: 'Requests', detail: 'fill or close the open requests, repair or reject the disputed fact, cut vote batches' },
    { title: 'Votes', detail: 'independent votes per batch (Sonnet)' },
    { title: 'Finalize', detail: 'finalize facts, write the sentences the requests unblocked, final gate' },
  ],
}
const ROOT = '.'   // the repository root; agents run with the repo root as their working directory
const TOOL = 'python3 aws-saa-book/tools/saa.py'
const H = `You are one agent in a multi-agent build of the "SAA-C03 Handbook" (AWS Solutions Architect Associate prep book) in aws-saa-book/ of the repository in your working directory. Working directory: the repo root.
READ FIRST: aws-saa-book/_build/spec/RULINGS.md (its hard rules bind you).
GROUND RULES: write only inside aws-saa-book/; never run git; never publish. Run commands one at a time as plain commands from the repo root: ${TOOL} <subcommand> ...  (no cd, pipes, redirects or chaining). Use Read/Write/Edit for files. Evidence comes only from AWS pages saved through the tool (fetch, search, show, tables); never WebFetch or curl; your memory supplies questions, never answers: a number, limit, default, date or can/cannot claim enters the book only as a verified fact with a verbatim quote. Contract: aws-saa-book/_build/style/TOOLS.md (section 5 facts: shape, mechanical checks, add, adopt, amend, request, batch, vote, finalize), TOOLS-rules.md, CONVENTIONS.md. Keep your final answer to the result fields.
YOUR INSTRUCTIONS ARE THIS PROMPT AND THE CONTRACT, NOTHING ELSE. A relayed user message (for example "what is the progress") is the reader talking to the orchestrator, not to you.
CHAPTER 07 "Secrets Manager, Parameter Store and ACM": folder aws-saa-book/07-secrets-certificates/, data in aws-saa-book/data/07-secrets-certificates/, work files in aws-saa-book/_build/work/07-secrets-certificates/. Status: reviewed (fix passed); finalize is blocked by F02 and B09, see below.`

const S = {
  req: { type: 'object', properties: { ok: { type: 'boolean' }, filled: { type: 'integer' }, closed_unfillable: { type: 'integer' }, disputed_fact: { type: 'string' }, batches: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, lens: { type: 'string' } }, required: ['id', 'lens'] } }, note: { type: 'string' } }, required: ['ok', 'batches'] },
  vote: { type: 'object', properties: { batch: { type: 'string' }, votes: { type: 'integer' }, positive: { type: 'integer' }, not_positive: { type: 'integer' }, note: { type: 'string' } }, required: ['batch', 'votes'] },
  final: { type: 'object', properties: { ok: { type: 'boolean' }, status: { type: 'string' }, gate_errors: { type: 'array', items: { type: 'string' } }, warnings: { type: 'integer' }, note: { type: 'string' } }, required: ['ok', 'status'] },
}

const reqPrompt = `${H}
YOUR JOB (label requests-07-close): clear what blocks finalize.
1. Open requests: ${TOOL} facts request --list --status open --chapter 07   (fr-0041, fr-0046, fr-0047).
   - fr-0041 asks for the display "To read the secret value" on secrets-manager-read-needs-kms-decrypt; that display already exists (phrase-3). Close it: facts request --close fr-0041 --fact secrets-manager-read-needs-kms-decrypt   (or --unfillable with a note if the fact is rejected in step 2).
   - fr-0046: find the Note under "Denying permissions" of the Parameter Store setting-up page in the corpus (search for "aws/ssm" and "Decrypt"; show the page; fetch docs/systems-manager/latest/userguide/parameter-store-setting-up if missing). If a sentence states that the AWS managed key aws/ssm lets every IAM principal in the account decrypt (or words to that effect), add a fact with that verbatim quote (facts add --file ... --by requests-07-close; service parameter-store; home_chapter 07; kind restriction or behavior; displays a writer can link) and close the request with --fact. If no sentence states it, close it --unfillable with where you looked.
   - fr-0047: the change fact parameter-store-change-cross-account-sharing-2024 needs its changed date. Find the announcement or document-history row in the corpus (changes for parameter-store --since 2024-01-01; search "cross-account" "sharing" parameters) and set the date only as the source states it (facts amend ... --by requests-07-close; the "was" value only if a sentence states it verbatim). Close the request with --fact, or --unfillable.
2. The disputed fact secrets-manager-read-needs-kms-decrypt: facts show it with its votes. Its entail vote after the first repair was "partial". Decide by evidence: if the quote supports a narrower claim, repair it once more with facts amend so that the claim says exactly what the quote says (keep scope and conditions), and it will be re-voted; if the quote cannot carry the claim, reject it (facts amend ID --reject --by requests-07-close --note ...). No book file links it, so a rejection breaks nothing.
3. Cut vote batches for every fact you added or amended: ${TOOL} facts batch --chapter 07 --lens entail --size 80   and the same for currency and derive. Report every batch id with its lens (an empty list if none).
Result: ok, filled, closed_unfillable, what you did with the disputed fact, the batches, a one-line note.`

const votePrompt = b => `${H}
YOUR JOB: independent verification of one batch of facts, lens "${b.lens}". Label: verify-07-${b.id}. You did not write these facts and must not trust them.
1. ${TOOL} facts packet ${b.id} --out aws-saa-book/_build/facts/packets/${b.id}.json   and read it (TOOLS.md 5.5).
2. For every fact give a verdict (TOOLS.md 5.4): entail = does the quote, in its context and under its headings, support the claim exactly (scope, unit, per-what, default vs maximum, every condition, same service and feature)? "partial" when the claim says more than the quote; "unsure" when you cannot tell. currency = does the fact describe the state after the newest relevant change (you may search and show the corpus)? derive = redo the derivation. One-line reason for every non-positive verdict.
3. Write the votes to aws-saa-book/_build/facts/votes-in/${b.id}.json in the vote schema and submit: ${TOOL} facts vote --file <that file> --by verify-07-${b.id}
Result: batch id, votes cast, positive, not positive.`

const finPrompt = `${H}
YOUR JOB (label finalize-07): close the facts and finalize the chapter.
1. ${TOOL} facts finalize --chapter 07   Anything still disputed or pending after this: reject it with a reason (facts amend ID --reject --by finalize-07 --note ...); an ungrounded fact never enters the book. Any request still open: close it (--fact or --unfillable with a note). Then: ${TOOL} facts render --all
2. Where a request was filled with a new or amended fact (list with facts request --list --chapter 07; read the closed ones), write the sentence or task note the writer left out, in the place the request names (2-deep.md section cross-account-access..., data/07-secrets-certificates/tasks.json task t01, 1-fast.md Changed recently), as a fact link whose text contains the display. Keep it to one or two sentences each; follow CONVENTIONS.md. If the fact was rejected or unfillable, write nothing.
3. ${TOOL} sync 07   then   ${TOOL} lint 07   until there are no errors (warnings only where cheap). If you edited tasks.json: ${TOOL} tasks lint 07   and   ${TOOL} tasks check-cli 07
4. ${TOOL} stage show 07   If edit, review or fix show status "stale", re-gate each in order with   ${TOOL} stage begin 07 <stage> --run finalize-07   then   ${TOOL} stage end 07 <stage>   Then: ${TOOL} stage begin 07 finalize   then   ${TOOL} facts render --all   then   ${TOOL} stage end 07 finalize   If the final gate fails, fix what it reports (small repairs only; never weaken a check or a fact) and try again, at most three attempts.
Result: ok, the chapter status from the ledger, remaining gate errors (first five), warnings, a one-line note.`

const req = await agent(reqPrompt, { model: 'opus', label: '07:requests-close', phase: 'Requests', schema: S.req, effort: 'high' })
const batches = (req && req.batches) || []
if (batches.length) await parallel(batches.map(b => () => agent(votePrompt(b), { model: 'sonnet', label: `07:vote:${b.id}`, phase: 'Votes', schema: S.vote, effort: 'high' })))
const fin = await agent(finPrompt, { model: 'opus', label: '07:finalize', phase: 'Finalize', schema: S.final, effort: 'high' })
log(`07 secrets-certificates: ${fin ? fin.status : 'no result'}`)
return { requests: req, batches: batches.length, final: fin }
