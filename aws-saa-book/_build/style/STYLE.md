# STYLE: writing rules (version 1.0 frozen 2026-10-11)

For every writer. `CONVENTIONS.md` gives the syntax; `SPEC.json` gives the numbers that lint checks; `READER.md` describes the one reader. She is an engineer, English is her second language, she skims, and she must say these things aloud to customers. A wrong fact is worse than a missing one.

**Imitate the exemplar.** `_build/style/exemplar/` is a grounded slice of chapters 03 and 10; its `README.md` lists what to copy and the common failures. Section 11 holds the rules the judging panel added. Item rules: `CONVENTIONS-2.md` section J. Which rule the lint checks and which a reviewer checks: `TOOLS-rules.md` R11.

Five principles decide every doubt:

1. **Fast first.** The short version is its own file and is read first.
2. **Design for the skim, then test past it.** Headings, tables and captions give a correct gist. Questions test what the gist misses.
3. **Every paragraph must pay.** Delete a paragraph that no question, card, signal, trap or spoken answer depends on.
4. **Explain plainly, quiz authentically.** Prose is simple. Question stems use real exam register.
5. **Say it aloud.** Every chapter gives her sentences she can say.

## 1. Sentences and paragraphs

- Average 15 words per sentence. Lint warns above 24 and fails above 30.
- One main idea per sentence, with at most one subordinate clause.
- Active voice, present tense, explicit subject: "The NAT gateway sends the request."
- Condition first, then result: "If the instance has no public IP address, the instance cannot reach the internet."
- Repeat the noun. Do not write an unclear "it" or "this". Wrong: "The role calls the bucket, and it fails."
- Keep "that" in relative clauses: "the subnet that the instance uses".
- No noun stack longer than three nouns, except official names. Wrong: "the subnet route table entry target".
- A paragraph has at most 4 sentences and 70 words. The topic sentence comes first.
- Write negatives in full: "cannot", "does not". No contractions in prose. No double negatives.
- Modal verbs have fixed meanings: **must** = AWS requires it; **cannot** = impossible; **can** = possible; **should** = best practice. Do not use "may".
- Hard numbers are digits with the unit of the fact canon: "5 Gbps", not "five gigabits".

## 2. Vocabulary and terms

- **Plain words.** Non-technical words stay common. If a rarer word is needed, teach it as a term or as Exam English.
- **One term per concept.** No variation for style. "Instance" is never "server", "box" or "machine"; "server" means a machine on premises. `data/terms.json` lists the term, the one allowed short form and the banned variants.
- **Capitalise as AWS documentation does:** Region, Availability Zone, security group, network ACL, Multi-AZ.
- **Current AWS names only.** A former name appears once, as "formerly ...".
- **Density.** At most 3 new terms in a paragraph. Spell out every abbreviation at first use in each file.

**Introduce a term in five steps:** say the idea in plain words; name the term in bold; give say-it help if needed; use the term again within two sentences; add one "not the same as".

> Some firewalls remember each connection, so the reply is allowed automatically. This is called **stateful**. A security group is stateful. A network ACL is not: it is stateless.

**Collocations are content.** She recalls terms as chunks, and prepositions are where recall breaks. Use and teach the fixed partners: assume a role; attach a policy to a role; launch an instance in a subnet; associate a route table with a subnet; mount a file system; poll a queue; invoke a function; promote a read replica; fail over to the standby; rotate a secret; encrypted at rest and in transit; behind a load balancer; across Availability Zones.

## 3. Avoid, and use instead

| Avoid | Use |
|---|---|
| set up, spin up, tear down, figure out, kick off | create, launch, delete, determine, start |
| under the hood, out of the box, rule of thumb, silver bullet, low-hanging fruit | internally, without extra configuration, general rule, or delete |
| e.g., i.e., etc., via | for example, that is, and so on, through |
| leverage, utilize, facilitate, robust, seamless, powerful | use, help, or delete |
| simply, just, easy, obviously, of course | delete: they shame a learner who finds it hard |
| since or as (cause), while (contrast), once (after), over (more than) | because, although, after, more than |
| may | can |

The full banned-word map is in `SPEC.json` under `lint.banned_words`. Three groups are taught, not avoided:

- **Phrasal verbs that are technical terms:** scale out, scale in, scale up, fail over, roll back. Also allowed, because AWS documentation uses them: turn on, turn off, sign in, back up.
- **Words customers say** (taught once in chapter 01, for listening): spin up, lift and shift, blast radius, noisy neighbour, guardrails, break-glass.
- **Confusable words:** eventually (means "after some time", not "maybe"); terminate or stop; principal or principle; role, rule or roll; route or root; affect or Effect.

No idioms. No analogy tables. At most one inline analogy per chapter, from software or machine learning, followed by where the analogy breaks: "A role is like a Kubernetes service account, except that a role keeps no key." No history, no pricing tables, no marketing adjectives, no console click paths: name the thing to find, not the clicks.

## 4. Pronunciation

Give a respelling with the stressed syllable in capitals, at first use in a file and in the words table: `**idempotent** (eye-dem-POH-tent)`. Respellings come from `data/terms.json` (for example ephemeral ih-FEM-er-ul, network ACL NAK-ul, Cognito cog-NEE-toh). Respell only a word she can mispronounce, not a common word such as "least privilege".

## 5. Formatting and tone

- GitHub-flavoured Markdown only. No footnotes, no Mermaid, no alert syntax, no emoji.
- **Bold** only for a term at its definition, a device label, the step name of a numbered trace ("**Look for a deny.**"), or the one deciding fact of a paragraph. No italics.
- A heading in "How it works" is a full-sentence claim: "A subnet is public because of one route", not "Public subnets".
- A table earns its place when two or more things are compared on the same questions, or as a truth table: one row per case, the result in the last column ("| 3 | Allows EC2, not S3 | Allows the action | Silent | Implicit deny |"). Cells hold phrases, at most 15 words.
- A diagram shows one idea. The caption is a claim sentence. The numbered steps under the picture walk through the picture.
- **Tone:** calm, direct, adult, second person. No cheerleading. A wrong Predict guess is a guess, not an error.
- **The startup.** Callvale is a call-intelligence service. Cast: Ana (CEO: cost, customers), Ben (CTO: speed, simplicity), Chen (security lead), and "you", their AWS Solutions Architect. At most 80 words in the `Startup example` callouts of a chapter. Never contradict the fact sheet, `STARTUP.md`.
- **Stop and answer** applies the text to a new case. Target: she answers 70 to 85% correctly. Never ask for a sentence she can copy from the paragraph above.

## 6. Spoken answers

One pattern, four moves, four fixed starters. Under stress a fixed scaffold removes the "how do I start the next sentence" problem.

| Move | Starter | Content |
|---|---|---|
| 1 Answer | "The short answer is" | one direct sentence |
| 2 How | "It works like this." | the mechanism in 2 to 4 short sentences |
| 3 Watch | "The thing to watch is" | one trade-off, limit, cost or "not when" |
| 4 You | "In your case" then a check-back question | an example in the customer's context |

A compare question uses the same moves; its first sentence can be "Both do X. The difference is Y." The recover pattern for a gap: "What I know is... What I would confirm is... I will check and come back to you today."

Every speak item has:

- a **10-second answer** of at most 25 words;
- a **60-second answer** of 105 to 145 words, as lines, one line per breath group;
- a **skeleton** of four cues;
- 3 to 5 **must** key points (each with a fact), up to 2 **nice** points;
- 2 or 3 **must-not-say** errors with the correction;
- 2 **follow-up questions** with answers.

Script rules: sentences of at most 16 words; contractions allowed; no brackets; no links; numbers written as she says them ("eleven nines", "fifteen minutes"); the last line is a question to the customer. She memorises the first sentence and the skeleton, never the script, so write a script that still works when one word is lost.

A follow-up answer covers every case of its rule.

## 7. Questions

All questions are original. Never use content from exam-dump sites. Sources are the exam guide, the official sample questions (format only) and AWS documentation.

**Stem**, 60 to 130 words, four parts in this order:

1. Context, 1 or 2 sentences.
2. The problem or the change.
3. 0 to 3 explicit constraints.
4. The ask, with at most one capitalised qualifier: "Which solution will meet these requirements with the LEAST operational overhead?"

**Options.** Four for a single answer. Five for a multiple-response question, whose stem ends "(Select TWO.)". Each option is 15 to 45 words, grammatically parallel to the others, and within 30% of the mean option length. The key is not the longest or the most detailed option. Banned: "all of the above", "none of the above", "always", "never", negative stems (outside chapter 01). No question is decided by a number that changed in the last 24 months. Do not name option letters in any text: the app shuffles options.

**Distractors.** Each wrong option encodes one named misconception. It carries a trap id from a chapter trap list, or a `misconception` sentence when no trap fits. The bar is the exam guide's own: a distractor is an option that a candidate with incomplete knowledge might choose. Six types are allowed:

1. `violates-qualifier`: it works, but breaks the qualifier. At least one in every question of difficulty 2 or 3.
2. `sibling-confusion`: the similar service or feature.
3. `wrong-configuration`: the right service, configured wrongly.
4. `different-problem`: it solves another problem.
5. `keyword-bait`: it matches a word in the stem and nothing else.
6. `impossible-feature`: at most one per question, with a fact that proves "cannot".

**Mix.** Difficulty 1 (one concept) 20%; difficulty 2 (discriminate under a qualifier) 55%; difficulty 3 (several services, two plausible finalists) 25%. Multiple response is 15% of the bank. A twin pair is two questions with the same scenario and one changed phrase, with different keys; place the twins apart.

**Explanation.** 120 to 200 words in total, stored as fields:

1. The answer (from the `correct` flags).
2. The deciding phrases, copied from the stem (`keywords`).
3. Why the key is right, with the mechanism (`explanation`).
4. Why not each other option: one sentence each that names the violated constraint or the false belief (`why`). "Not suitable" is not a reason.
5. The twin line (`twin`): "If the stem said "..." instead: ..., because ...".
6. The review link (`section`), one-sentence `takeaway`, and an optional spoken version (`say`).

Grounded samples: `exemplar/questions.json` (README items 9 and 10).

**Think-aloud** (`worked.steps`): first person, present tense, about 200 words, always these six steps:

1. "I read the last sentence first: it asks for..."
2. "I mark the constraints..."
3. "Before I look at the options, I predict..."
4. "I remove ... because..."
5. "Between ... and ... the difference is...; the stem says..., so..."
6. "Check: ... meets every constraint. Time: 90 seconds."

One think-aloud per deep chapter follows a plausible wrong path and shows where it breaks (`wrong_path: true`): step 3 states the wrong prediction, and step 5 holds the sentence "My first idea breaks because ...".

**Failure modes of machine-written questions, and the check that catches each:**

| Failure | Check |
|---|---|
| Two defensible answers | three blind solvers; any disagreement means one edit, then reject |
| The stem is under-specified | a solver states the solution from the stem alone |
| A stale or invented key, or an invented "cannot" | every key claim and negative claim links a verified fact |
| The qualifier is ignored | each option is rated: meets the requirements or not, and its rank on the qualifier |
| The stem leaks the key by word overlap | overlap lint |
| Clones of one pattern | a unique (concept, trap) pair; at most 2 questions per concept |
## 8. Hands-on tasks

| Type | Time | Cost | What it is |
|---|---|---|---|
| Look | 3 to 5 min | $0 | read-only; "Look first" in every deep chapter |
| Try | 10 to 15 min | under $0.10 | 1 to 3 resources in AWS CloudShell |
| Lab | 25 to 40 min | under $1 | a template builds the routine part; she does the instructive part by hand |

Each task kills one named misconception (`kills`), for example "A budget stops spending." A break-it step follows the order predict, break, observe, explain (`explain`, with the fact link); the fix is the next step.

Safety rules (checks: `TOOLS-rules.md` R9, R11):

1. AWS CloudShell only. No local CLI, no access keys, no IAM users.
2. Secure by default. Never open SSH or RDP to the world; use Session Manager. No public buckets: the public-access lesson is a denied attempt.
3. Tag every resource `book=saa` and `task=<task-id>`, in the tag syntax of the service (for example `Key=book,Value=saa`); name prefix `saa-`. Where an operation takes no tag, tag in the next step.
4. Every Try and Lab has a cost line, a "if you forget" cost per day, the permissions it needs, and a read-only alternative for a locked-down account.
5. Cleanup in reverse order of creation, then a verify command that filters by `task=<task-id>` and must return nothing, then the "still costs money if left" list.
6. Stop rule: at twice the stated time, run the cleanup and move on.
7. Every task carries the label "checked against docs, not run in a real account".
8. Name the thing to find, never the clicks. Commands come from an official tutorial or CLI example page that is in the corpus.

## 9. Flashcards

Writers write `decide`, `differ`, `number` and `cannot` cards. The tool generates the other five types.

| Type | Front, then back |
|---|---|
| `term` | "Stateless subnet-level firewall with deny rules: what is it called?" then "network ACL" |
| `meaning` | the term, then its one-breath definition |
| `decide` | scenario cue plus qualifier, then the service and a one-line reason |
| `differ` | "Security group or network ACL: which is stateful?" (one difference per card) |
| `number` | a cloze, A-list numbers only: "In SQS, the maximum message size is {{c1::...}}." |
| `cannot` | "Can an EBS volume attach to an instance in another Availability Zone?" then "No", with the reason in `extra` |
| `partner` | "You ___ a role." then "assume" |
| `word` | a stem fragment with the exam-English word, then meaning and signal |
| `say` | a customer question, then the 10-second answer; the skeleton is in `extra` (answered aloud) |

Atomicity rules:

- One fact per card. The answer has at most 12 words (25 on a `say` card).
- No list answers. No "explain X" cards.
- The front names its context: "In SQS, ...".
- No near-identical pairs unless both carry `pair`.
- Every `decide`, `differ`, `number` and `cannot` card lists its fact, so the export can show the AWS quote.
- English only.

## 10. Before you return

1. Run the lint on your chapter until it reports no errors.
2. Check each "How it works" subsection: can she redraw the causal chain from it?
3. Read every spoken script aloud once, at normal speed. It must fit in 60 seconds.
4. Every fact you wanted and did not find is a fact request and a `needs-fact` marker, not a sentence.

## 11. What the exemplar panel added (1.0)

1. **Subsection order** (`CONVENTIONS-2.md` U1). The problem in one or two sentences (no repeated label), a numbered trace, a table when the trace has two or more cases, one "Why does AWS work this way?" reason, an `Exam signal` (an `Exam heuristic` when no fact decides the stem phrase), Go deeper, a `Say it` written for speech, then the Stop and answer. The reason is what she tells a customer: "If a later allow could cancel it, the guardrail would fail."
2. **A link carries its whole sentence.** Keep the scope of the quote (same account, same Region, buckets but not KMS keys). Wrong: ""Revoke the temporary credentials" is not a real action". Link the most specific fact, not a neighbour whose quote happens to match. The link text is the short display (at most 8 words without a digit) and reads as part of your sentence: no capital in mid-sentence, no "we".
3. **No invented order.** When no fact gives an order, write "Use the checks as a checklist: the result is the same in any order." Wrong: "AWS then makes three checks, in this order".
4. **Test the key against the strongest actor.** If the stem gives users AdministratorAccess, a Deny they can detach does not "ensure" anything: "no one, including administrators" is an SCP.
5. **A Stop and answer obeys its own subsection.** If the trust policy names `ec2.amazonaws.com`, no developer assumes that role.
6. **The story adds no hidden fact.** Wrong: "In your case. Earlier, Ben added a Deny for object deletes." A story component exists only from its chapter; otherwise write "A team".
7. **Spot the bug is not obvious.** Not `s3:*` on `*`; use a group as principal, a NAT gateway in a private subnet, or a network ACL that allows outbound 443 only.
8. **Each Exam trap is new**, never a restatement of the table above it.
9. **"But not if" names the alternative.** Wrong: "the caller uses long-term access keys: they lack it". Right: "the users are customers of a mobile app: Amazon Cognito".
10. **Headings survive the skim.** Wrong: "A resource-based policy names the principal and opens cross-account access" (it suggests the trap). Right: "Same-account access needs one allow but cross-account access needs two".
11. **Changed recently.** The Old line holds the old value ("10 per role"), not the change. A `not examinable yet` entry goes to the deep file under the B-list; its "The exam probably expects:" line ends "Do not let this number decide an answer."
12. **Evidence and form.** Prefer documentation facts to blog quotes ("typically" is not a rule). No example rates. A diagram shows real actors: a role sends nothing. Chapter numbers come from the registry (KMS is chapter 06). Expand every abbreviation in each file (RCP, AZ).
