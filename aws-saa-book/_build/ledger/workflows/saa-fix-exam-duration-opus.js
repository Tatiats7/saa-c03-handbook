export const meta = {
  name: 'saa-fix-exam-duration-opus',
  description: 'Replace the rejected exam-duration fact with a properly quoted one (Opus agents), vote on it independently, finalize, and point the web shell at the new id',
  phases: [
    { title: 'Add', detail: 'new fact exam-duration-minutes from the certification page' },
    { title: 'Vote', detail: 'independent entailment and currency votes' },
    { title: 'Close', detail: 'finalize, update tools/web/shell.json, check the web build' },
  ],
}
const ROOT = '.'   // the repository root; agents run with the repo root as their working directory
const TOOL = 'python3 aws-saa-book/tools/saa.py'
const H = `You are one agent in a multi-agent build of a study book, the "SAA-C03 Handbook", in the folder aws-saa-book/ of the repository in your working directory. Your working directory is the repo root (if your shell starts elsewhere, use absolute paths under ${ROOT}).
READ FIRST: aws-saa-book/_build/spec/RULINGS.md (its hard rules bind you) and aws-saa-book/_build/style/TOOLS.md section 5 (facts).
GROUND RULES: write only inside aws-saa-book/; never run git; never publish; run the tool one plain command at a time (${TOOL} <subcommand> ...), no pipes or redirects (use --out). Evidence only from pages saved in the corpus (search, show). Do not touch aws-saa-book/_build/ledger/ or _build/work/ except the work folder of chapter 01 for your JSON file. Other agents mine chapters 02, 03 and 10 at the same time; do not touch their facts. Keep the final answer to the result fields.`

const S = {
  add: { type: 'object', properties: { ok: { type: 'boolean' }, fact_id: { type: 'string' }, batches: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, lens: { type: 'string' } }, required: ['id', 'lens'] } }, note: { type: 'string' } }, required: ['ok', 'fact_id', 'batches'] },
  vote: { type: 'object', properties: { batch: { type: 'string' }, votes: { type: 'integer' }, positive: { type: 'integer' }, note: { type: 'string' } }, required: ['batch', 'votes'] },
  done: { type: 'object', properties: { ok: { type: 'boolean' }, status: { type: 'string' }, note: { type: 'string' } }, required: ['ok'] },
}

const addPrompt = `${H}
YOUR TASK: the fact exam-duration (chapter 01, namespace exam) was rejected because its quote came from a blog post. A fact id is never reused, so add a replacement with the id exam-duration-minutes, home chapter 01, by label fix-01-duration. First check whether a previous attempt already added it (${TOOL} facts show exam-duration-minutes); if it exists as mech-pass or candidate, skip to cutting the batches. Evidence: the SAA-C03 certification page saved as www/certification/certified-solutions-architect-associate (run: ${TOOL} show www/certification/certified-solutions-architect-associate --around "Exam duration" --chars 600). Its heading "Exam duration" is followed by the line "130 minutes"; quote exactly what the page says (a short quote is fine; if the tool asks for the heading as context, include it the way TOOLS.md 5 describes). Claim: the SAA-C03 exam lasts 130 minutes. Values: one value with display "130 minutes" and a spoken form. Mark it hard, the kind the schema allows for a duration, exam_relevance high, source tier 1, the question it answers ("How long is the SAA-C03 exam?"). If the exam guide snapshot (docs/aws-certification/latest/solutions-architect-associate-03/...) also states the duration, add it as a second evidence entry. Add with: ${TOOL} facts add --file <your json file under aws-saa-book/_build/work/01-how-the-exam-asks/> --by fix-01-duration   Fix any mechanical finding and add again. Then cut the verification batches: ${TOOL} facts batch --chapter 01 --lens entail --size 40   and   --lens currency   (report every batch id the tool creates; an empty list for a lens is fine).
Result: ok, the fact id, the batches with their lens, a one-line note.`

const votePrompt = b => `${H}
YOUR TASK: independent verification of batch ${b.id}, lens ${b.lens}, label verify-01-${b.id}. You did not write these facts and must not trust them. ${TOOL} facts packet ${b.id} --out aws-saa-book/_build/facts/packets/${b.id}.json   then read that file. For every fact give the verdict of this lens (TOOLS.md 5.4): entail = does the quote, read under its heading, support the claim exactly (scope, unit, which exam)? currency = is the fact the current state (you may search the corpus for a newer statement)? Write the votes to aws-saa-book/_build/facts/votes-in/${b.id}.json in the vote schema and submit: ${TOOL} facts vote --file aws-saa-book/_build/facts/votes-in/${b.id}.json --by verify-01-${b.id}
Result: the batch id, votes cast, how many positive, a one-line note.`

const closePrompt = `${H}
YOUR TASK: close the replacement of the exam-duration fact. 1. ${TOOL} facts finalize --chapter 01   and confirm that exam-duration-minutes is verified (${TOOL} facts show exam-duration-minutes). If it is disputed, report that and stop. 2. ${TOOL} facts render --all 3. Edit aws-saa-book/tools/web/shell.json: in examFacts set "minutes" to "exam-duration-minutes" (keep the other three ids and every other key). 4. ${TOOL} build web --preview   and confirm that no WB10 warning names "minutes" any more (the WB05 plan.json warning is expected). 5. ${TOOL} gate 01 --quick   and report its result.
Result: ok, the fact status, a one-line note.`

phase('Add')
const added = await agent(addPrompt, { model: 'opus', label: 'fix:add', phase: 'Add', schema: S.add, effort: 'medium' })
if (!added || !added.ok) return { ok: false, at: 'add', note: added && added.note }
phase('Vote')
const votes = await parallel((added.batches || []).map(b => () => agent(votePrompt(b), { model: 'opus', label: `fix:vote:${b.id}`, phase: 'Vote', schema: S.vote, effort: 'high' })))
phase('Close')
const closed = await agent(closePrompt, { model: 'opus', label: 'fix:close', phase: 'Close', schema: S.done, effort: 'medium' })
return { ok: !!(closed && closed.ok), fact: added.fact_id, votes: votes.filter(Boolean), close: closed }