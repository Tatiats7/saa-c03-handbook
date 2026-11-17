# SAA-C03 prep book: learning design specification

Scope: pedagogy, chapter specification, study calendar. Facts marked **[verified]** I fetched from AWS pages today (Oct 4, 2026); facts marked **[ledger]** are examples the research team must still ground. I also read two files in the repo for constraints: `October.md` and `habits.md`.

## 0. Findings that change the plan

1. **There is no retake buffer.** "If you fail an exam, you must wait 14 calendar days before you are eligible to retake the exam" [verified]. `October.md` assumes Oct 20–24 "leaves one retake buffer before month end"; it does not. Only a first sitting by Oct 16–17 leaves a retake by Oct 31.
2. **ESL +30 exists and has an order rule.** "A 30-minute exam extension is available upon request to non-native English speakers"; it "only needs to be requested once, prior to registering for an exam" [verified]. That gives 160 minutes instead of 130, or 2.46 instead of 2.0 minutes per question. Her plan had the exam booked by Oct 3, so check on Monday whether the accommodation applies to an existing booking.
3. **Rescheduling is limited.** "Up to 24 hours before your scheduled exam time. Each exam appointment can only be rescheduled twice" [verified]. Book now and let the gates decide keep or move; do not book two days before.
4. **Results can be slow.** They are posted "within five business days" [verified]. A sitting on Oct 28–30 can produce a result in November.
5. **The hours do not hold six mocks plus everything else.** Six Tutorials Dojo mocks with real review cost about 18 hours. `October.md` also puts a video course inside the same 40 hours. My assumption: the book replaces the video course, five mocks fit, and the sixth is a reserve. `October.md` has a separate 12 hours for Exam 2 prep; if speaking practice is charged there, the sixth mock fits.
6. **Her own description of how she reads** (`habits.md`): long LLM-generated text intimidates her and she often does not finish it. She acts before reading and trusts the gist from one glance. Her first language is Georgian.

Five design principles follow from this:

- **P1 Fast first.** The 20-minute version of a chapter is its own short file and is read first.
- **P2 Design for the skim, then test past it.** Headings and tables carry a correct gist; questions target what the gist misses.
- **P3 Every paragraph must pay.** A paragraph that no question, card, signal, trap or spoken answer depends on is deleted (the "orphan rule").
- **P4 Explain plainly, quiz authentically.** Book prose is simple; question stems use real exam register.
- **P5 Say it aloud every day.** This matches her own daily minimum.

Sections 1–13 below follow the numbering of the request.

## 1. Chapter templates by tier

### 1.1 Three reading routes

| Route | What she does | Deep chapter | Medium chapter |
|---|---|---|---|
| **Fast** | Part 1 only | 20 min | 12 min |
| **Pass** | Fast, core questions, only the "How it works" subsections her misses point to, one spoken answer | 50 min (65 for IAM, VPC, S3, EC2) | 22 min (Fast + 4 questions) |
| **Full** | Everything | 2–2.5 h | 60–70 min |

Each chapter is a folder of short files: `1-fast.md`, `2-deep.md`, `3-do.md`, `4-say.md`, `5-quiz.md`, `sources.md`, `img/`.
Why: a file she can finish in 15 minutes gets opened; a 7,000-word file does not.

### 1.2 Deep template ("must know cold", 12 chapters)

| # | Section | Words | Route | Why it earns its place for her |
|---|---|---|---|---|
| 1 | **Predict**: 3 questions before reading, one a "gist trap" that common sense gets wrong | 120 | Fast | Pretesting improves retention and shows her the gist is not enough. Not scored. |
| 2 | **Look first**: one 3-minute read-only console task | 80 | Fast | She acts before she reads; this makes the service concrete and raises questions. |
| 3 | **In one breath**: 25-word spoken definition, the problem it solves, hero diagram with 5 numbered steps, Harken's problem in 60 words | 280 | Fast | Gives the correct gist on purpose, and the sentence she can say under stress. |
| 4 | **Words that go together**: at most 8 terms as collocations, with say-it help and "do not confuse with" | 180 | Fast | She forgets terms; terms are recalled as chunks ("assume a role"). |
| 5 | **Choose it or not**: 2–4 sibling comparison tables, each ending in one "deciding question" | 500 | Fast | The exam is a discrimination task. |
| 6 | **Signals and traps**: 8–12 signal rows (stem says, think, because, but not if) and 5–6 traps (wrong belief, truth) | 420 | Fast | Highest exam value per word; "but not if" stops blind keyword matching. |
| 7 | **Changed recently**: old, now, since, what the exam probably expects | 90 | Fast | Tutorials Dojo and older notes lag; as an SA she must give current answers. |
| 8 | **Check**: 3 questions parallel to Predict, plus "Recap from memory" (5 prompts, answers hidden) | 130 | Fast | Shows before/after gain; recall replaces a summary box she would skim. |
| | *Fast subtotal* | *≤ 1,800* | | |
| 9 | **How it works**: 5–7 subsections with assertion headings, built as "follow the packet / request / object"; each ends in a Stop-and-answer | 2,000–2,600 (XL 3,200) | Full | Causal chains are what she must be able to explain. |
| 10 | **Numbers that decide answers**: A-list (≤ 8, memorise) and B-list (recognise) | 180 | Full | Only numbers that change an answer or a sizing conversation. |
| 11 | **Harken builds it**: before/after diagrams and a decision record (context, requirement in exam English, options, decision, trade-off) | 280 | Full | A decision record is an exam question and a customer conversation in one. |
| 12 | **FAQ quick-fire**: 10 "can you or can't you" items with the verbatim FAQ quote in the reveal | 350 | Full | Keeps the FAQ grounding she asked for, as recall instead of a list. |
| 13 | **In the real world** (optional): one AWS-published case study | ≤ 80 | Full | Gives her a citable customer story. |
| 14 | **Do**: 2 Try tasks and 1 Lab with a "break it on purpose" step | 600–700 | Pass does 1 Try | She asked for "little tasks"; attempt 1 gave one 40-minute lab. |
| 15 | **Say it out loud**: 3 prompts (4 in XL), each with 10-second and 60-second model answers | 600–780 | Pass does 1 | Attempt 1 had prompts without models. |
| 16 | **Worked examples**: 2 think-alouds, one showing a wrong path | 400 | Full | Models the two-option endgame. |
| 17 | **Quiz**: 16 questions (8 core, 8 extended) | not counted | Pass: core | |

Standard deep chapters total about 6,700 words; the four XL chapters about 7,800. About 5,100 and 5,900 of that is reading; the rest is practice scripts.

### 1.3 Medium template ("know well", 13 chapters)

Same order, smaller:

- **Fast part, at most 1,000 words:** Predict (2), In one breath with diagram, Words (≤ 5), Choose it or not (1–2 tables), Signals and traps (6 signals, 3 traps), Changed recently, Check (2).
- **Full adds:** How it works (3–4 subsections, 1,150 words), Numbers (100), Harken (150), FAQ quick-fire (5 items), one Try, Say it (2 prompts), one worked example, Quiz of 8 (4 core, 4 extended).
- **Total:** about 3,000 words, cap 3,400.

### 1.4 Light template ("recognise it", about 52 service cards)

A card is 150–220 words with fixed fields:

- Name, former name, and how to say it.
- What it is, in one line.
- Two or three stem signals that point to it.
- "Do not confuse with", plus the deciding difference.
- One fact, only if the exam uses one.
- A 10-second spoken sentence.
- Source link.

Cards have no lab and no "How it works". Twenty-four cards sit inside medium chapters (for example DocumentDB, Keyspaces and Neptune in the database chapter). Twenty-eight sit in four family chapters. A family chapter adds one positioning diagram, a confusable-pairs table, 6 discrimination questions and one spoken prompt.

### 1.5 Cross-cutting templates

These are organised by decision or pattern and never re-explain a service; they link back.

- **Pattern chapter** (HA/DR, security, cost): the question behind the domain, one spectrum diagram, 6–10 pattern cards, a per-service table, 3 worked think-alouds, 10 multi-service questions, 2 customer prompts. A pattern card has: problem in exam English, sketch, services, cost and complexity, choose when / not when, the common wrong alternative. The fast part is the diagram, the card headers and the table.
- **Decision atlas page:** one decision per page: a flowchart of 2–4 yes/no questions, a table of at most 4 columns, a one-sentence rule, and one twin-question pair.
- **Reference architecture page:** a requirement paragraph in exam style, a numbered flow diagram, a "what breaks without it" table, and three "if the question adds X, change Y" deltas.

### 1.6 What I cut from attempt 1 and why

- **Analogy table.** Analogies are culture-bound and she is an engineer. Allow at most one inline analogy from software or ML, followed by where it breaks.
- **FAQ one-liners.** Replaced by quick-fire recall.
- **End-of-chapter summary.** A skimmer reads only that; replaced by Recap from memory.
- **The single long lab.** Replaced by small tasks placed next to the concept.
- **Console click paths.** They go stale; describe the destination, not the clicks.
- **History, pricing tables, marketing adjectives.**

### 1.7 Filled-in mini example

A "How it works" subsection:

> **A subnet is public only because of one route (3 min)**
> A subnet has no "public" switch. A subnet is public when its route table sends internet traffic (0.0.0.0/0) to an internet gateway. Remove that route, and the same subnet is private.
> An instance in a public subnet also needs a public IPv4 address. Without one, the route exists but the instance cannot use it.
> **Stop and answer.** Harken moves a worker into a public subnet. The worker has only a private IP address. Can it download a package from the internet? *(Hidden answer: No. The route is there, but the worker has no public address. Either give it one or use a NAT gateway.)*

Signal rows for the same chapter [ledger]:

| The stem says | Think | Because | But not if |
|---|---|---|---|
| "private instances must download patches" | NAT gateway | outbound only; "external services can't initiate a connection" [verified] | traffic goes only to S3 or DynamoDB: use a gateway endpoint |
| "block one IP address" | network ACL deny rule | security groups have no deny rules | the block is on request content: use AWS WAF |

## 2. Total size control

### 2.1 Budgets

| Part | Count | Words |
|---|---|---|
| Front matter (Start here; How the exam asks + Exam English; AWS map) | 3 | 6,000 |
| Deep chapters | 12 (4 XL) | 85,000 |
| Medium chapters | 13 | 39,000 |
| Light cards and family frames | 52 cards, 4 frames | 11,500 |
| Cross-cutting and review | 11 | 29,000 |
| **Prose total** | | **≈ 170,000 (hard cap 180,000)** |
| Question bank | ≈ 450 questions | ≈ 145,000, never read linearly |

### 2.2 Layers

| Layer | Content | Size | Her time |
|---|---|---|---|
| **1. Pass route** | All fast parts, flagged subsections, front matter, cross-cutting fast parts, atlas, review sheets | ≈ 56,000 words, ≈ 170 book questions, 6 Try tasks, ≈ 28 spoken answers | ≈ 25 h |
| **2. Depth route** | Remaining How it works, FAQ quick-fire, Harken, labs, extended questions, remaining prompts | ≈ 75,000 words, ≈ 215 questions | + 25–30 h, selective before the exam and complete after it |
| **3. Reference** | Light cards, glossary, change list, evidence ledgers, original mock | ≈ 40,000 words, 65 questions | lookup only |

The honest reading of this: 40 hours buys "pass comfortably". "Explain every service very well" is Layer 2 and needs about 25 more hours, mostly after the exam.

### 2.3 Time model

| Activity | Planning rate |
|---|---|
| First read of new technical prose | 120 words/min |
| Fast-part tables and review sheets | 150 words/min |
| Exam-style question in the book | 2.5 min (1.5 to answer, 1.0 for the explanation) |
| Predict, Check, Stop-and-answer item | 0.5–1 min |
| Tutorials Dojo timed set | 115 min planned, 130 limit |
| Mock review | 65 min (3 min per wrong answer, 1 min per flagged-right, 5 min logging) |
| Spoken answer with self-check | 3.5 min |
| Look / Try / Lab | 3–5 / 10–15 / 25–40 min |
| Anki | 20 new cards a day ≈ 20–25 min a day, outside the 40 h (≈ 6–7 h in total) |

- **Reading rate.** 120 words/min is a planning assumption: about half of typical native non-fiction speed, conservative on purpose. Calibrate on day 1 by timing the 800-word Start-here page and rescaling the calendar.
- **Train at 130 minutes, sit at 160.** If a typical question runs 110–160 words with options (my estimate), reading takes 50–75 seconds, so reading speed is her limit and ESL +30 matters.

### 2.4 The 40-hour budget

| Block | Hours |
|---|---|
| Orientation, diagnostic, admin | 1.6 |
| 12 deep chapters on the Pass route (8 × 50 min, 4 × 65 min) | 11.0 |
| 13 medium chapters, Fast + 4 questions | 4.8 |
| Cross-cutting chapters and review sheets | 3.4 |
| Daily mixes and mistake re-drills | 1.7 |
| Try tasks (6) | 0.7 |
| Extra speaking and dress rehearsal | 1.3 |
| Repair reading | 0.8 |
| Tutorials Dojo mocks 1–5, sitting plus review | 15.0 |
| **Total** | **40.3** |

Mock 6 adds 3 hours. It fits only if speaking moves to her Exam 2 budget, or if the Try tasks and two cross-cutting chapters are dropped.

### 2.5 Control rules

- The orphan rule (P3) is checked mechanically.
- Fast-part word caps are hard gates.
- Write 20 questions per deep chapter and ship the best 16.
- **Build in calendar order.** She starts tomorrow, so Start here, Exam English, IAM, VPC and S3 Pass-route material must be finished and verified first.

## 3. Anti-skim and retention devices

| # | Device | Exactly where | Markdown fallback |
|---|---|---|---|
| 1 | **Predict** with one gist trap | First element of every chapter | Answers appear only in the Check section |
| 2 | **Look first** | Second element of deep chapters | Same |
| 3 | **Time box** on every heading ("3 min") | All sections | Same |
| 4 | **Assertion headings** (a full-sentence claim) | Every How-it-works subsection | Same |
| 5 | **Stop and answer** | End of every How-it-works subsection, so every 250–400 words | `<details>` |
| 6 | **Predict the picture** ("Where does the NAT gateway go?") | Before each hero diagram | Question, then image inside `<details>` |
| 7 | **Spot the bug** | 1–2 per deep chapter, 1 per medium, in Harken or How it works | Text plus `<details>` |
| 8 | **Twin questions**: same scenario, one phrase changed, different answer | 2 pairs per deep quiz, 1 per medium, 12 pairs in the atlas | Twins placed apart in the file |
| 9 | **Stem-first mode**: options hidden until she picks what is optimised and taps the deciding phrase | Default for her first 100 questions in the web app | Instruction line: "Cover the options first" |
| 10 | **Confidence mark** (sure / not sure) | Every question | Column in `mistakes.md` |
| 11 | **Return questions** | Chapter opening: 3 questions from chapters N−1, N−3, N−6 | Static list |
| 12 | **Daily mix** of 10: 4 new core, 3 older, 3 from her mistakes | Calendar; phone-sized | Pre-built mixes per calendar day |
| 13 | **Mistakes log** with cause codes | After every wrong answer, including mock misses | Table template |
| 14 | **Recap from memory** | End of fast part | `<details>` |
| 15 | **Today page**: only today's 3–5 cards, with ticks for her three daily minimums (10 pages, 5 words, one rehearsal) | Web home page | `calendar.md` with links |

Rules for the devices:

- **Stop and answer** must need the paragraph applied to a new case, never a copied sentence. The target success rate is 70–85%. In the web app the next subsection stays collapsed until she answers or skips, and skips are logged.
- **"Sure but wrong"** answers come back first, because confident errors are corrected best when surfaced.
- **Cause codes** are five: K (did not know), C (confused two similar things), W (missed a word in the stem), T (time), D (dated question that assumes an old limit).
- **Repair by code.** K sends her to the linked subsection. C sends her to the atlas page. W gives her ten stem-first questions.

Deliberately not used:

- **Hard locks** that block progress. They would push her out of the app.
- **Streaks and points.** They add noise.
- **Highlighting tools.** They feel like work without recall.

## 4. ESL-aware style guide

### 4.1 Sentences and paragraphs

- Average 15 words per sentence, maximum 24. One main idea, at most one subordinate clause.
- Active voice, present tense, explicit subject: "The NAT gateway sends…".
- Condition first, then result: "If the instance has no public IP address, it cannot…".
- Repeat the noun instead of an unclear "it" or "this".
- Keep "that" in relative clauses: "the subnet that the instance uses".
- No noun stacks longer than three nouns, except official names.
- Paragraphs: at most 4 sentences and 70 words, topic sentence first.
- Write negatives in full and never hide one: "cannot", "does not". No double negatives.
- Modals have fixed meanings: must = AWS requires it; cannot = impossible; can = possible; should = best practice. Do not use "may".

### 4.2 Vocabulary

- **Plain words.** Non-technical words stay inside common-word lists (NGSL plus an academic list). A script flags the rest; each flagged word is replaced, or taught as a term or as Exam English.
- **One term per concept.** No variation for style: "instance" is never "server", "box" or "machine"; "server" is on premises only.
- **Term bank.** `terms.yml` holds the official term, allowed short form, banned variants, respelling, plain meaning and collocations.
- **Capitalise as AWS docs do:** Region, Availability Zone, security group, network ACL, Multi-AZ.
- **Introducing a term** takes five steps: say the idea in plain words; name it in bold; give say-it help if needed; use it again within two sentences; add one "not the same as".
  Example: "Some firewalls remember each connection, so the reply is allowed automatically. This is called **stateful**. A security group is stateful. A network ACL is not: it is stateless."
- **Density.** At most 3 new terms per paragraph. Spell out every abbreviation at first use in each file.
- **Collocations are content.** Examples: assume a role; attach a policy to a role; launch an instance in a subnet; associate a route table with a subnet; mount a file system; poll a queue; invoke a function; promote a read replica; fail over to the standby; rotate a secret; encrypted at rest and in transit; behind a load balancer; across Availability Zones.
  Why: Georgian uses postpositions and has no articles, so English prepositions and verb partners are where fluent recall breaks.

### 4.3 Avoid, and what to use instead

| Avoid | Use |
|---|---|
| Phrasal verbs: set up, spin up, tear down, figure out, kick off | create, launch, delete, determine, start |
| Idioms: under the hood, out of the box, rule of thumb, silver bullet, low-hanging fruit | internally, by default, general rule, or delete |
| e.g., i.e., etc., via | for example, that is, and so on, through |
| leverage, utilize, facilitate, robust, seamless, powerful | use, help, or delete |
| simply, just, easy, obviously, of course | delete (they shame a learner who finds it hard) |
| since / as (cause), while (contrast), once (after), over (more than) | because, although, after, more than |

Three exceptions that are taught, not avoided:

- **Phrasal verbs that are technical terms:** scale out/in/up, fail over, roll back.
- **A "words customers say" list** for listening: spin up, lift and shift, blast radius, noisy neighbour, cold start, guardrails, landing zone, break-glass.
- **Confusable words that matter here:** eventually (means "after some time", not "maybe"); terminate vs stop; principal vs principle; role vs rule vs roll; route vs root; affect vs Effect.

### 4.4 Pronunciation

Use respelling with the stressed syllable in capitals. Add it at first use and in the glossary, about 80 entries. Audio comes from Anki's built-in text-to-speech field.

Starter set:

- **Everyday technical words:** cache KASH; queue KYOO; ephemeral ih-FEM-er-ul; idempotent eye-dem-POH-tent; asynchronous ay-SING-kruh-nus; throughput THROO-put; latency LAY-ten-see; resilient rih-ZIL-yent; egress EE-gress; parameter puh-RAM-ih-ter; hierarchy HY-er-ar-kee; schema SKEE-muh; archive AR-kyve.
- **Names and acronyms:** NACL NAK-ul; CIDR SY-der; IOPS EYE-ops; Aurora uh-ROR-uh; Kinesis kih-NEE-sis; Athena uh-THEE-nuh; Cognito cog-NEE-toh; Macie MAY-see; Redis RED-iss; Kubernetes koo-ber-NET-eez; Glacier GLAY-sher.

Three groups to drill, as a hypothesis to confirm with one recording, not an assumption:

- Stress shifts in long words: aVAILable / availaBILity; AUthorize / authoriZAtion.
- "th" words: throughput, throttling, health check, authentication.
- v/w words: VPC, WAF, volume, weighted, warm standby.

### 4.5 Formatting and tone

- **Markdown limits.** GFM only; no footnotes, Mermaid or alert syntax, because they may not render in VS Code.
- **Tables.** At most 4 columns in fast parts (phone width) and 5 elsewhere; cells at most 15 words.
- **Diagrams.** SVGs carry an opaque background, because the VS Code preview may be dark. At most 9 labelled elements, numbered arrows, and a caption that states the takeaway as a sentence.
- **Emphasis.** Bold only for a term at its definition or the one deciding fact in a paragraph. No italics for emphasis.
- **Callouts.** Exactly five types: Key fact, Trap, Changed recently, Try it, Say it.
- **Evidence.** IDs go in HTML comments after each hard fact (`<!--ev:S3-014-->`), invisible in preview and machine-checkable.
- **Tone.** Calm, direct, adult, second person. No cheerleading. Wrong Predict guesses are called guesses, not errors.

### 4.6 Exam English

The non-technical words in a stem often decide the answer. Teach about 90 of them, in nine groups of ten:

1. Optimisation qualifiers
2. Workload shape
3. Strength of requirement
4. Data and time
5. Operations
6. Security
7. Location and network
8. Change and migration
9. Instruction grammar ("Choose two", "which combination")

| Word in the stem | Plain meaning | What it signals |
|---|---|---|
| sporadic, intermittent, infrequent | sometimes, not regularly | pay per use; not always-on instances |
| unpredictable, spiky | you cannot plan the load | automatic scaling; on-demand capacity; a queue as buffer |
| steady-state, predictable | the same load all the time | commitment discounts; provisioned capacity |
| LEAST operational overhead | the team does the least work to run it | managed or serverless feature, not scripts on EC2 |
| MOST cost-effective | cheapest option that still meets every requirement | reject options that fail a requirement first |
| stringent, strict | very demanding | the strongest control, not the cheapest |
| near real-time | a short delay is acceptable | differs from real-time; a classic twin |
| without changing the application | keep the code | compatible managed service, not a redesign |
| can tolerate interruption | stopping is acceptable | Spot capacity |
| immutable, cannot be altered | write once | object lock, not just versioning |

How to teach them:

- **A 3,500-word chapter**, of which 1,500 is on the Pass route.
- **Explanations.** Every question explanation names the "deciding phrase".
- **Coverage.** Each word must appear in at least 3 stems across the bank.
- **Twin questions** flip one word.
- **Anki.** A 90-card deck replaces her 5-English-words-a-day for 18 days. It is the same habit with different words.

## 5. The "explain it out loud" system

### 5.1 One pattern, four moves, four fixed starters

| Move | Starter she memorises | Content |
|---|---|---|
| 1 Answer | "The short answer is…" | One sentence, direct |
| 2 How | "It works like this…" | Mechanism in 2–4 short sentences |
| 3 Watch | "The thing to watch is…" | One trade-off, limit, cost or "not when" |
| 4 You | "In your case…" then a check-back question | Example in the customer's context |

- **Compare questions** use the same four moves with a different first sentence: "Both do X. The difference is Y."
- **Recover pattern** for gaps: "What I know is… What I would confirm is… I will check and come back to you today."
- **Term rescue:** describe the function and keep going ("the managed firewall at the subnet level…").
- **Buying time:** restate the question once.

Why one pattern: under stress a fixed scaffold removes the "how do I start the next sentence" load. More patterns would mean more to forget.

### 5.2 Model answers written for speech

Every prompt has:

- A **10-second answer** of at most 25 words.
- A **60-second answer** of 105–145 words (her own plan specifies 60-second answers).
- A **keyword skeleton** of four cues.
- 3–5 **must-say facts**, 2–3 **must-not-say errors**, and 2 pre-written **follow-up questions**.

Script rules: sentences of at most 16 words; one line per breath group; contractions allowed; no brackets; numbers spoken ("eleven nines"). She memorises the first sentence and the skeleton, never the script, because a memorised script collapses when one word is lost.

Filled example. Prompt: "What is the difference between a security group and a network ACL?" [ledger]

> **10 seconds:** A security group protects one resource and remembers connections. A network ACL protects a whole subnet and checks every packet in both directions.
>
> **60 seconds:**
> The short answer is: both are firewalls, but they work at different levels.
> It works like this. A security group is attached to a resource, for example an EC2 instance.
> It has only allow rules. And it is stateful: if a request is allowed in, the reply goes out automatically.
> A network ACL is attached to a subnet. It has allow rules and deny rules, with numbers.
> It is stateless, so you must allow the request and the reply separately.
> The thing to watch is this: most of the time, security groups are all you need.
> Use a network ACL when you must block something, because a security group cannot deny.
> In your case, I'd keep the default network ACL and control access with security groups.
> Do you have a rule today that needs an explicit block?
>
> **Skeleton:** two levels · stateful / allow only · stateless / numbered allow + deny · block needs ACL
> **Must not say:** "security groups have deny rules"; "a network ACL is stateful".

### 5.3 Practice ladder and self-check

The ladder is 10 minutes a day, in a private room and standing:

1. Read the model aloud.
2. Answer from the skeleton only.
3. Answer cold with a 90-second timer.
4. Take a random prompt plus one follow-up.
5. Practise with a human.

Self-check, 5 yes/no boxes:

- Did I answer in my first sentence?
- Did I use the must-say terms, and no wrong term?
- Did I give cause and effect, not only a definition?
- Did I name one trade-off or limit?
- Did I give an example, end with a question, and stay under 90 seconds?

### 5.4 In-page Claude grading

- **Input.** She speaks, and operating-system dictation (the Mac or phone keyboard microphone) types the transcript into the box. Typing is the fallback.
- **What the page sends.** The prompt, the rubric (must-say facts with accepted paraphrases, must-not-say errors, terms, model answer, pre-written follow-ups) and her transcript. Calls are stateless, so the page stores the history.
- **What comes back:**
  - a score of 0–2 per move;
  - each must-say fact marked said / partly / missing;
  - errors quoted in her words with the correction;
  - terms misused or missing;
  - a "heard as" list of words dictation got wrong (a pronunciation hint without judging accent);
  - **her own answer repaired** in at most 130 words, keeping her wording where it was correct;
  - one thing to fix next time;
  - one follow-up question.
- **Bands.** 8–10 customer-ready; 6–7 correct but incomplete; 5 or less repair and repeat. Any must-not-say error caps the score at 5.
- **Grader rules.**
  - Grade facts strictly and English kindly.
  - Give at most two language notes, and only where meaning changes.
  - Never comment on accent or articles.
  - Correct only from the rubric; label any claim outside it "not checked".
  - Keep feedback under 150 words of simple English.
- **Structure-only mode.** For her own questions on Bedrock, credits and similar topics, the grader scores the four moves and clarity and states that facts were not checked.

### 5.5 Tie to the week of Oct 13

- **Speaking pack.** 30 prompts in customer wording: 24 from chapters, 6 cross-service (availability, cost, security review, database choice, Lambda or containers, disaster recovery). There are blank slots for questions from her three shadowed calls. This is the 30-question bank her plan already calls for.
- **Daily dose.** One answer per deep chapter, 1–2 extra on Oct 5–9, and one each on the light days Oct 7–8.
- **Oct 12 dress rehearsal.** 45 minutes in interview mode: 10 random prompts, 90 seconds each, one follow-up each. The report shows per-move averages, the top 3 missed terms and the blank-out count.
- **Teammate sessions.** Her two recorded sessions use a printable one-page score sheet with the same five boxes.
- **Speaking gate.** 8 of 10 prompts at 7/10 or better, and a one-breath answer for all 12 deep services without notes.

## 6. Question-writing standard

### 6.1 Anatomy

- **Stem**, 60–130 words, in four parts: context (1–2 sentences), problem or change, 0–3 explicit constraints, then the ask with **exactly one** capitalised qualifier ("Which solution will meet these requirements with the LEAST operational overhead?").
- **Options.** Four (A–D) for single answer; five for "Choose two". Each is 15–45 words, grammatically parallel, with lengths within ±30%.
- **Banned.** No "all/none of the above", no "always/never", no negative stems outside the Exam English chapter.
- **Key position** is balanced across letters; the app shuffles options.
- **Volatile numbers.** No question is decided by a number that changed in the last 24 months.

### 6.2 Distractors

Each distractor encodes one named misconception and carries a trap ID from the chapter's trap list. The exam guide's own definition is the bar: options "that a candidate with incomplete knowledge or skill might choose… generally plausible responses that match the content area" [verified].

Six allowed types:

1. Works, but violates the qualifier. At least one per question at level 2 and above.
2. Sibling confusion.
3. Right service, wrong configuration.
4. Solves a different problem.
5. Keyword bait.
6. Impossible feature. At most one per question, with a doc quote proving "cannot".

### 6.3 Mix and counts

| Item | Standard |
|---|---|
| Difficulty | L1 single concept 20%; L2 discriminate under a qualifier 55%; L3 multi-service with two plausible finalists 25% |
| Multiple response | 15% of the bank, nearly all "Choose two" from five, all-or-nothing |
| Deep chapter | 16 (8 core, 8 extended), including 2 twin pairs and 2–3 multiple response |
| Medium chapter | 8 (4 core, 4 extended), including 1 twin pair |
| Light family | 6 discrimination questions |
| Cross-cutting | ≈ 62 (10 each for HA/DR, security, cost; 8 architectures; 12 atlas twin pairs) |
| Original mock | 1 × 65, all new, split 20/17/15/13 by domain |
| Second mock and 4 domain drills | Samplers over unseen extended questions by tag; no new writing |
| Worked think-alouds | 2 per deep, 1 per medium, 3 per pattern chapter |

- **Why one original mock:** she has about 400 Tutorials Dojo questions for assessment; the book's questions are for teaching, and bulk mock writing is where machine quality is weakest.
- **Day-1 diagnostic:** use AWS's free 20-question official practice set if it is still offered (not verified today). It is the exam owner's voice, and it spends none of the book's questions.

### 6.4 Explanation format (120–200 words, fixed)

1. Answer.
2. **Deciding phrase**, quoted from the stem.
3. Why it is right, with the mechanism.
4. Why not each other option: one sentence each, naming the violated constraint or false belief.
5. **"If the stem said … instead"**: the twin, in one line.
6. Review link, and an optional one-sentence spoken version.

Tags: `id, chapter, domain, task, services[], concept, trap[], difficulty, type, qualifier, layer, evidence[], twin_of, status`.

### 6.5 Sample at the required standard [ledger]

> A company runs batch workers on Amazon EC2 instances in private subnets in two Availability Zones. The workers download large datasets from Amazon S3 and occasionally download software packages from the internet. All outbound traffic uses a NAT gateway, and NAT gateway data processing charges have increased sharply. Company policy does not allow the instances to have public IP addresses.
> Which solution will reduce cost with the LEAST operational overhead?
> A. Move the instances to public subnets and delete the NAT gateway.
> B. Create a gateway VPC endpoint for Amazon S3 and add it to the private route tables.
> C. Create interface VPC endpoints for Amazon S3 in both Availability Zones and delete the NAT gateway.
> D. Replace the NAT gateway with a NAT instance on a small instance type.
>
> **Answer:** B. **Deciding phrases:** "large datasets from Amazon S3", "data processing charges", "LEAST operational overhead".
> **Why:** A gateway endpoint sends S3 traffic through a route-table entry instead of the NAT gateway, so the large transfers stop paying NAT data processing. Package downloads still use the NAT gateway.
> **Not A:** without public IP addresses the instances lose internet access, and the policy forbids public addresses.
> **Not C:** interface endpoints have hourly and per-gigabyte charges, and deleting the NAT gateway breaks package downloads.
> **Not D:** you must patch and scale a NAT instance yourself, which is more operational overhead.
> **If the stem said** "servers on premises reach S3 over Direct Connect": interface endpoint, because a gateway endpoint works only from inside the VPC.
> `domain 4 · task 4.4 · VPC, S3 · gateway-endpoint-vs-nat · L2 · single · qualifier: cost + operations · core`

### 6.6 Think-aloud format

First person, present tense, about 200 words, always these steps:

1. "I read the last sentence first: it asks for…"
2. "I mark the constraints…"
3. "Before I look at the options, I predict…"
4. "I remove A because…"
5. "Between B and C the difference is…; the stem says…, so B."
6. "Check: B meets every constraint. Time: 90 seconds."

One per deep chapter follows a plausible wrong path and shows where it breaks.

### 6.7 Machine-written failure modes and how reviewers catch them

| Failure | Catch |
|---|---|
| Key is the longest or most detailed option; key letter is biased | Lint on lengths and letter distribution |
| Two defensible answers | Two blind solvers without the key; any disagreement means revise or kill |
| Stem under-specified, key arbitrary | Cover-the-options solve: a solver states the solution from the stem alone |
| Absurd distractors | Each must map to a trap ID; an advocate agent argues for each one |
| Key or "cannot" claim is stale or invented | Every key claim and every negative claim checked against the ledger |
| Qualifier ignored | Audit table: each option meets the requirements yes/no, plus its rank on the qualifier |
| Stem leaks the key by word overlap | Overlap lint |
| Twenty clones of one pattern | Coverage matrix: unique (concept, trap) pair, at most 2 per concept |
| Tautological explanations ("not suitable") | Each "why not" must name a constraint or belief |
| Dump contamination | **No content from brain-dump sites, ever** (she is an AWS employee). Sources are the exam guide, official samples and AWS docs |

## 7. Hands-on tasks

### 7.1 Task types

| Type | Time | Cost | Where | Count |
|---|---|---|---|---|
| **Look** (read-only) | 3–5 min | $0 | Inline; "Look first" in every deep chapter | ≈ 40 |
| **Try** (1–3 resources in CloudShell) | 10–15 min | under $0.10 | End of the relevant subsection | ≈ 30 |
| **Lab** (template builds the boring part, she does the instructive part by hand) | 25–40 min | under $1 | `3-do.md` | 5 |
| **Break** (inside a Try or Lab) | — | — | Predict, break, observe, explain, fix | ≈ 20 |

### 7.2 Safety rules

1. **Account.** Use the account her team allows for learning, in one Region. Every task card lists the permissions it needs and a read-only alternative for a locked-down account.
2. **Tagging.** Everything is tagged `book=saa, task=<id>` with name prefix `saa-`. A final command lists anything still tagged and must return empty.
3. **CloudShell only.** No local CLI, no access keys, no IAM users.
4. **Secure by default.** Never open SSH or RDP to the world. Use Session Manager. No public buckets: the public-access lesson is a *denied* attempt.
5. **Cost.** Every card shows the cost and "if you forget: about $X a day" from the pricing pages. Task 0 sets a $10 budget alert. The whole book stays under $10.
6. **Cleanup.** Reverse order, then a verify command, then a "still costs money if left" list. The list covers NAT gateways, load balancers, databases and snapshots, unattached addresses, interface endpoints, keys, versioned buckets and log groups.
7. **Stop rule.** At twice the stated time, run cleanup and move on.
8. **Honesty badge.** Every task carries "checked against docs on <date>, not executed" and a one-tap "this step failed" report.
9. **Robust instructions.** Name the thing to find, not the clicks.

### 7.3 The 25 highest-value tasks

All facts here are [ledger] unless marked.

| # | Task (type) | Misconception it kills |
|---|---|---|
| 0 | Set a budget alert (Try) | "A budget stops spending." |
| 1 | Policy simulator: add an explicit deny (Try) | "An allow somewhere wins." |
| 2 | Read your own temporary credentials in CloudShell (Look) | "Applications need stored access keys." |
| 3 | Find what makes your default subnet public (Look) | "Public is a subnet setting." |
| 4 | Start a CloudShell VPC environment in a public subnet and curl the internet (Try) | "In a public subnet means internet access." Docs: environments "created in public subnets… will not have access to public internet" [verified] |
| 5 | Remove the NAT route; S3 still works through a gateway endpoint (Lab) | "Private subnets need NAT to reach S3." |
| 6 | Block reply ports in a network ACL (Try) | "A network ACL behaves like a security group." |
| 7 | Session Manager to an instance with no inbound rules (Try) | "You need port 22 and a bastion host." |
| 8 | Stop and start an instance; watch the public IP change (Try) | "An instance keeps its public address"; "stop equals terminate." |
| 9 | Read instance metadata with a token (Try) | "The role's credentials are stored on the disk." |
| 10 | Try to attach a volume across Availability Zones, then use a snapshot (Try) | "A volume can attach anywhere in the Region." |
| 11 | Terminate one instance behind a load balancer and Auto Scaling group (Lab) | "The load balancer replaces failed instances." |
| 12 | Try to make an object public (Try) | "Buckets are public unless you lock them." |
| 13 | Delete an object in a versioned bucket, then remove the delete marker (Try) | "Delete removes the data"; "versioning is free." |
| 14 | Presigned URL that expires in 60 seconds (Try) | "To share an object you must make it public." |
| 15 | Write a lifecycle rule and read the minimums (Look) | "A colder class is always cheaper." |
| 16 | Disable the KMS key, then read the object (Try) | "S3 permission is enough for encrypted data." |
| 17 | Reboot a Multi-AZ database with failover (Lab, start it and read while it builds) | "The standby serves reads"; "failover changes the endpoint." |
| 18 | Query versus scan with consumed capacity shown (Try) | "Query and scan cost the same." |
| 19 | Look up an alias target with `dig` (Look) | "Point an A record at the load balancer's IP." |
| 20 | CloudFront in front of a private bucket (Lab) | "The bucket must be public to serve a site." |
| 21 | Fail an asynchronous Lambda call and find it in the dead-letter queue (Try) | "Failed events are lost"; "Lambda retries forever." |
| 22 | Lambda in a VPC without NAT calls a public API (Try) | "Lambda always has internet access." |
| 23 | Receive a message and do not delete it (Try) | "Receiving removes the message." |
| 24 | One topic, two queues, one filter policy (Try) | "One queue can feed many independent consumers." |
| 25 | Find who created your bucket (Look) | "CloudWatch tells you who did it." |

The fifth lab is the serverless pipeline S3 → queue → function → table. Labs are the first hands-on items to cut (section 13).

## 8. Running example: Harken

**Company.** Harken ("to listen") is a call-intelligence service for customer-support teams. Customers upload or stream support calls and get transcripts, sentiment, topics, summaries, search and dashboards. Run a name-collision check before use.
Why this product: it gives a natural reason for almost every in-scope service, including Transcribe and Comprehend. Its B2B customers bring compliance, private connectivity and disaster recovery requirements, and it matches the startups she advises.

**Fact sheet** (one canonical `harken.yml`, never contradicted):

- 1.5 million call minutes a month by stage 2.
- Uploads peak 09:00–11:00 on weekdays.
- Audio is kept 7 years and rarely opened after 90 days.
- The bank customer requires RPO 15 minutes and RTO 1 hour.
- One 80 TB archive to import.

**Cast.** Ana (CEO: cost, customers), Ben (CTO: speed, simplicity), Chen (security lead from stage 3), and **you, their AWS Solutions Architect**. Their questions are the spoken prompts. At most 80 words of story per chapter.

| Stage | Trigger | What Harken adds | Chapters |
|---|---|---|---|
| 0 Demo day | The flawed start: one instance, root keys in code, a public bucket, default VPC, database on the instance | Nothing; this is the "before" | AWS map |
| 1 First ten customers | Paying users | Roles replace keys; custom VPC with NAT and an S3 gateway endpoint; right-sized instance and image; gp3 and snapshots; presigned uploads, encryption, lifecycle; Multi-AZ PostgreSQL | 1–5, 7 |
| 2 Launch week | Traffic spikes | Load balancer and Auto Scaling over 3 zones; DynamoDB for job state; DNS and certificates; CloudFront for app and audio; upload event → queue → workflow → Transcribe → Comprehend; events for "transcript ready"; API with customer sign-in; session cache | 6, 8–12, 16, 19 |
| 3 First bank customer | Compliance | Customer managed keys and secret rotation; multi-account with guardrails; audit trail, configuration history, threat detection, sensitive-data discovery; web firewall; PrivateLink to the bank; VPN, then Direct Connect; SFTP intake; archive import; central backup; containers on Fargate | 13–15, 17–18, 20–23 |
| 4 Global and efficient | Scale and cost review | Second Region as warm standby with failover routing; analytics lake and dashboards; Spot for batch; commitment discounts; archive tiers with object lock; everything as templates | 24–25, HA/DR, cost |

**Final architecture.** All of the above, on one master diagram that is greyed out and lights up chapter by chapter. Positions never move, which builds spatial memory. Summaries use a foundation model, with one line marked "outside the exam", because her customers will ask.

**Real companies.**

- Use only AWS-published case studies or AWS blog posts. Each box gives the URL, the year, a verbatim quote of at most 25 words, and the concept it illustrates.
- At most one box per deep chapter, 80 words. Each also gets a two-sentence speakable version for her story bank.
- If a story cannot be verified, drop it. Use them for the "why", not for architecture detail.

## 9. Flashcards (Anki)

**Card types:**

| Type | Front → back |
|---|---|
| Term (production) | "Stateless subnet-level firewall with deny rules → ?" → network ACL |
| Meaning | Term → one-breath definition, with text-to-speech audio |
| Decide | Scenario cue plus qualifier → service, with a one-line reason |
| Differ | "Security group or network ACL: which is stateful?" (one difference per card) |
| Number | Cloze, A-list numbers only |
| Cannot | "Can a volume attach to an instance in another zone?" → No, plus the reason |
| Partner | "You ___ a role." → assume |
| Word | Stem fragment with the exam-English word → meaning and signal |
| Say | Customer question → 10-second answer and skeleton (answered aloud) |

**Atomicity rules:**

- One fact per card; answer of at most 12 words (Say cards 25).
- No list answers, no "explain X" cards.
- The front names its context ("In SQS, …").
- No near-identical pairs unless tagged `pair`.
- Every card has a source field with a quote and a stable ID, so re-exports keep her scheduling.

A bad card: "Explain the differences between security groups and network ACLs."

**Counts:**

| Deck | Cards | Composition |
|---|---|---|
| Core | 270 | 14 per deep chapter, 4 per medium, 20 cross-cutting, 30 Say |
| Exam English | 90 | |
| Extended | ≈ 480 | 18 more per deep, 8 more per medium, 2 per light card, B-list numbers |

**Tags:** `saa::ch03-s3`, `tier::core|extended|reference`, `dom::1–4`, `type::…`, `trap::<id>`, `changed`.

**Order and load.** Card order follows the calendar, so cards arrive after she has read the chapter. She takes 15 core plus 5 Exam English new cards a day and sees all core cards by Oct 22.

## 10. Chapter order and study calendar

### 10.1 Order

Why this order: dependencies first, then exam weight. S3 moves up to third so the three largest topics get spaced review on the two light days.

1. **Deep:** 1 IAM · 2 VPC · 3 S3 · 4 EC2 · 5 EBS, EFS, instance store · 6 Load balancing and Auto Scaling · 7 RDS and Aurora · 8 DynamoDB · 9 Route 53 · 10 CloudFront and Global Accelerator · 11 Lambda · 12 SQS, SNS, EventBridge (with Step Functions; MQ and AppFlow as cards).
2. **Medium, security first:** 13 KMS, Secrets Manager, ACM · 14 Organizations, Control Tower, Identity Center, RAM · 15 CloudWatch, CloudTrail, Config · 16 API Gateway and Cognito · 17 ECS, EKS, Fargate, ECR · 18 WAF, Shield and threat detection · 19 ElastiCache and choosing a database · 20 Connecting VPCs (endpoints, peering, Transit Gateway, PrivateLink) · 21 VPN, Direct Connect, Client VPN · 22 Backup, Storage Gateway, FSx · 23 Migration and transfer · 24 Ingestion and analytics · 25 Deploying and operating (CloudFormation, Systems Manager, Beanstalk, Batch).
3. **Light families:** 26–29.
4. **Cross-cutting:** see section 11.

**Coverage check on her list.**

- **Promoted to deep:** SQS, SNS, EventBridge, because task 2.1 is about decoupling.
- **Merged:** load balancing with Auto Scaling.
- **Added beyond her two tiers:** Cognito, Identity Center, Control Tower, RAM, Config, the threat-detection family, Step Functions, Kinesis and Firehose, Athena, Glue, Redshift, FSx, Transfer Family, DMS, Application Migration Service, CloudFormation, Systems Manager, Beanstalk, Batch, Global Accelerator, the cost tools, and 52 recognise-only cards.

### 10.2 Plan A: exam Friday Oct 23 (≈ 40 h; Anki extra)

| Date | Hours | Work |
|---|---|---|
| Mon Oct 5 | 2.75 | Request ESL +30 and check the booking; Start here (timed); official 20-question diagnostic; Exam English core; AWS map; **Ch1 IAM**; Task 0; 2 spoken answers |
| Tue Oct 6 | 2.8 | **Ch2 VPC** + task 4; **Ch3 S3** + task 13; mix of 8; 2 spoken |
| Wed Oct 7 | 0.35 | Light: mix of 8 on phone; 1 spoken answer |
| Thu Oct 8 | 0.15 | Social day: 1 spoken answer; Anki only |
| Fri Oct 9 | 2.95 | **Ch4 EC2**; **Ch5 EBS/EFS**; **Ch6 Load balancing and Auto Scaling**; 1 task; 3 spoken |
| Sat Oct 10 | 2.95 | **Ch7 RDS/Aurora**; **Ch8 DynamoDB** + task 18; **Ch9 Route 53**; mix of 10; 3 spoken |
| Sun Oct 11 | 3.2 | **Ch10 CloudFront**; **Ch11 Lambda**; **Ch12 SQS/SNS/EventBridge** + task 23; HA/DR fast part; 4 spoken |
| Mon Oct 12 | 2.45 | **Speaking dress rehearsal (45 min)**; Ch13, 14, 15; cost patterns fast part |
| Tue Oct 13 | 0.95 | Spoken warm-up; security patterns fast part; Ch16. Keep 10 min of speaking a day until Exam 2 is done |
| Wed Oct 14 | 3.0 | **Mock 1** + review with cause codes |
| Thu Oct 15 | 1.9 | Ch17–20; atlas part 1 |
| Fri Oct 16 | 3.0 | **Mock 2** + review |
| Sat Oct 17 | 2.25 | Ch21–25; reference architectures |
| Sun Oct 18 | 3.0 | **Mock 3** + review. Gate 1 |
| Mon Oct 19 | 1.4 | Repair day: flagged deep subsections; light families through atlas part 2; mistakes re-drill |
| Tue Oct 20 | 3.0 | **Mock 4** + review |
| Wed Oct 21 | 3.0 | **Mock 5** + review. Gate 2, decided before the 24-hour reschedule limit |
| Thu Oct 22 | 1.25 | Signals, numbers and traps sheets; mistakes; exam-day page. Stop by 18:00 |
| Fri Oct 23 | — | Exam. Warm-up only: 5 easy questions and the traps sheet |

**Dropped in Plan A, honestly:**

- Full track on most chapters.
- All labs, and most Try tasks.
- Light services beyond the atlas.
- The book's own mock.
- The sixth Tutorials Dojo mock, held in reserve.

**Load warning.** Oct 14–21 carries about 20 hours while her project build is due Oct 20. Mock days need a quiet two-hour block.

**Gates:**

| Gate | When | Rule |
|---|---|---|
| Speaking | Oct 12 | 8 of 10 prompts ≥ 7/10; one-breath answers for 12 deep services |
| Gate 1 | After mock 3 | Mocks 2 and 3 both ≥ 80%: ahead; mock 5 becomes optional and the time goes to weak chapters. Mock 3 < 65%: move the exam now (first of two reschedules) |
| Gate 2 | After mock 5 | **Go** if the last two first-attempt timed scores are ≥ 80% (her rule). **Also go** at ≥ 75% twice with no domain under 65% and 10 minutes left on the clock. **Move** to Oct 27–28 if below that |

Only first attempts in timed mode count. Why the softer second rule: no retake is possible on either date, so waiting only helps if she actually moves the exam.

### 10.3 Plan B: exam Tue Oct 27 or Wed Oct 28

Do not sit on Oct 30; results can take five business days.

- **Calendar.** Same through Oct 18, then mock 4 on Oct 20, mock 5 on Oct 22 and mock 6 on Oct 24, each followed by a repair day. Sheets on the last day.
- **Cost.** About 44 hours minimum; about 50 with the full track on her three weakest deep chapters and one more measure (Tutorials Dojo's Final Test, or the book's mock).
- **What it buys.** All six mocks, properly reviewed.
- **What it costs.** A direct collision with slides (Oct 24) and the panel week (Oct 27), no retake, and a result that may land in November.

Use Plan B only when Gate 1 or Gate 2 says move.

### 10.4 Plan C: exam Fri Oct 16 or Sat Oct 17 (≈ 28 h)

- **Calendar.** Week 1 as in Plan A. Then mock 1 on Oct 13, Ch16–20 with security patterns and the atlas on Oct 14, mock 2 on Oct 15, sheets on Oct 16.
- **Dropped.**
  - Mocks 3–6, and with them her 80%-twice rule. The replacement is weaker: mock 1 ≥ 70% and mock 2 ≥ 75%.
  - Chapters 21–25, except their atlas pages.
  - Reference architectures.
  - Every repair day.
  - All tasks after week 1.
  - All depth reading.
- **Collision.** Exam 2 prep and exam cramming share the same days.
- **What it buys.** The only schedule with a retake before Oct 31. Confirm the exact eligible date in her certification account.
- **Fallback.** If mock 2 is under 75%, reschedule to Oct 23 at least 24 hours ahead and continue Plan A.

My recommendation is Plan A. Consider Plan C only if the day-1 diagnostic is 70% or higher and a recorded fail carries no cost for her.

## 11. Cross-cutting and review material

| Chapter | Must contain | Words |
|---|---|---|
| **30 HA, fault tolerance, DR** | RPO/RTO in plain words; the four DR strategies on one cost-versus-recovery diagram; "what survives a zone failure by default" table for every major service; scope table (global / Regional / zonal); 6 pattern cards | 3,800 |
| **31 Security patterns** | "Who can reach what" reasoning order (identity, resource policy, network, encryption); cross-account access; private access to AWS services; protecting data at rest and in transit; the "which security service" table | 3,500 |
| **32 Cost patterns** | One section per task 4.1–4.4; purchase options; data-transfer costs; the cost-tool cards | 3,500 |
| **33 Reference architectures** | 10 pages: three-tier web; static site with CDN; serverless API; event-driven fan-out; queue-buffered workers; container services; data lake; streaming; hybrid connectivity; multi-account landing zone | 3,500 |
| **34 Decision atlas** | 24 decisions | 5,000 |
| **35 Signals** | All signal rows, grouped by domain, with "but not if"; a warning that keywords are also used as bait | 2,000 |
| **36 Numbers to know** | A-list ≤ 40, B-list ≈ 60, with a column "older material says" | 1,200 |
| **37 Traps sheet** | One page, 40 lines of "wrong belief → truth", ranked by frequency times damage. This is the "gotchas" list her plan wants and her Exam 2 cheat sheet | 700 |
| **38 Final week and exam day** | Gates; pacing plan for 160 minutes; reading order (ask first); multiple-response method; guess rule; 60-second reset when stuck; logistics; the night before | 1,800 |
| **39 What changed recently** | Change, old, now, since, source, what to answer on the exam, what to tell a customer | 1,200 |
| **40 Speaking pack** | Section 5.5 | 2,500 |
| Glossary and repair index | Generated from `terms.yml`; an index from keywords to sections for mock misses | generated |

**The 24 atlas decisions:** storage type; S3 class; file system; EBS type; database; cache layer; compute; container option; purchase option; scaling policy; load balancer; routing policy; edge service; messaging; streaming; VPC-to-VPC connectivity; endpoint type; hybrid link; identity mechanism; encryption option; secret store; security detective service; DR strategy; migration tool.

**Pacing and guess rules in chapter 38:**

- A first pass at 2 minutes or less per question, then flagged questions, then a final check.
- Treat each multiple-response option as true or false.
- Never leave a blank: "unanswered questions are scored as incorrect; there is no penalty for guessing" [verified].
- An odd question may be one of the 15 unscored ones, so do not let it cost time.

**Verified examples for chapter 39** that show why it matters:

| Item | Older material says | Docs today |
|---|---|---|
| SQS maximum message | 256 KB | 1 MiB [verified] |
| S3 maximum object | 5 TB | 50 TB through multipart [verified] |
| gp3 maximum | 16,000 IOPS, 16 TiB | 80,000 IOPS, 2,000 MiB/s, 64 TiB [verified] |
| NAT gateway availability | "one per zone" is the only pattern | The user guide now has "Regional NAT gateways for automatic multi-AZ expansion" [verified, title only] |

## 12. Scoring rubric for a finished chapter

**Ship rule:** mean of 4.3 or higher, no criterion below 4, zero hard-gate failures. A reviewer must quote lines for any score under 5.

| Criterion | 5/5 | 2/5 |
|---|---|---|
| **1 Accuracy and grounding** | Every hard fact has an evidence ID whose verbatim quote supports it; changed items flagged with old and new; nothing from memory | Several facts unsourced, or quotes that do not support the claim; one stale limit presented as current |
| **2 Clarity for a non-native reader** | Lint clean (sentence length, banned words, one term per concept); terms introduced by the five steps; collocations taught; reads aloud naturally | Idioms and phrasal verbs; synonyms for the same thing; 30-word sentences; terms used before they are defined |
| **3 Exam usefulness** | Sibling tables end in a deciding question; signals have "but not if"; traps are real, common beliefs; every task statement the chapter touches is named | Feature tour; signals are bare keywords; traps are trivia |
| **4 Explanation depth** | Each mechanism is a causal chain she could redraw; fundamentals reach exam depth; each diagram is walked through by number | Definitions and lists; "it is managed and scalable"; diagram unexplained |
| **5 Question quality** | Passes all section 6.7 checks; every distractor has a trap ID; twins present; explanations name the deciding phrase and each false belief | Disputed keys; absurd distractors; longest option is the key; "B is not suitable" explanations |
| **6 Spoken-answer models** | Four moves; 105–145 words; sentences ≤ 16 words; skeleton, must-say, must-not-say and follow-ups present; sounds like a person | Essay paragraphs; no trade-off; no check-back; cannot be said in 60 seconds |
| **7 Hands-on value and safety** | Each task kills one named misconception; has permissions, cost, cleanup, verify and a locked-down alternative; break steps present | Button tour; no misconception; cleanup vague; opens ports or creates keys |
| **8 Skim resistance** | Passes the two reader tests below; Stop-and-answer every 250–400 words; no give-away summary | Skim reader scores the same as full reader; a summary box contains everything |
| **9 Diagrams** | One idea each; ≤ 9 labels; legible at phone width and in dark preview; caption is a claim; consistent visual grammar | Decorative icon wall; tiny text; no caption |
| **10 Size discipline** | Within budget; fast part under cap; no orphan paragraphs; template order kept | Over cap; padding; sections out of order |

**Hard gates (automatic fail):**

- An ungrounded hard fact.
- An unresolved disputed key.
- A Try or Lab without a cost line, cleanup and verify.
- A task that exposes SSH or RDP to the world, makes a bucket public, or creates long-lived keys.
- A fast part over 1,800 words (deep) or 1,000 (medium).

**Three mechanical tests reviewers run:**

1. **Two-reader test.** A skim agent reads only headings, bold text, tables and captions; a full agent reads everything. The skim agent must state the one-breath definition and the top three decisions, but score under 60% on Stop-and-answer and twin questions. The full agent must score 85% or more.
2. **Blind solve** of every question by two agents.
3. **Read-aloud timing** of every 60-second answer.

## 13. Risks and what to cut first

| Risk | Mitigation |
|---|---|
| Volume outruns verification; a wrong fact is worse than a missing one | Build and verify in calendar order; Pass route first; over-produce and cull |
| She opens the book, sees its size, and stops | Today page; short files; fast part first; time boxes |
| Machine-written questions are weak in bulk | Section 6.7 pipeline; one original mock only; 80% keep rate |
| Labs were never executed | Honesty badge; few labs, many small tasks; fail report; the stop rule |
| Exam and practice sets lag current docs | Teach both values; never let a changed number decide a question; cause code D |
| Signal tables train keyword matching | "But not if" column; twins; stem-first mode |
| The grader invents corrections | Rubric-only corrections; "not checked" label; pre-written follow-ups |
| 40 hours has no slack | Mock 6 in reserve; gates; speaking charged to her Exam 2 hours |
| Integrity | No dump-derived content |
| Harken drift; unverifiable company stories | One fact sheet; verify or drop |
| Logistics | ESL +30 on day 1; two reschedules only; no retake after Oct 17 |

**Cut order when quality and size conflict, first to last:**

1. Real-company boxes (keep the best 5).
2. Light cards shrunk to 80 words plus their atlas entry.
3. In-app flashcards and any diagram-occlusion cards (the Anki export stays).
4. Extended questions: medium 4 → 2, then deep 8 → 6.
5. Labs (keep VPC routing and the load balancer lab); keep every Look and Try.
6. FAQ quick-fire in medium chapters.
7. "How it works" for chapters 23–25.
8. The original 65-question mock.
9. The glossary long form.

**Never cut:**

- The evidence ledger.
- All 25 fast parts.
- The decision atlas.
- The traps and numbers sheets.
- The speaking pack with model answers.
- The core questions with full explanations.
- Cleanup steps.

## Sources

- [AWS Certification policies: before testing](https://aws.amazon.com/certification/policies/before-testing/)
- [AWS Certification policies: after testing](https://aws.amazon.com/certification/policies/after-testing/)
- [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html)
- [Using AWS CloudShell in Amazon VPC](https://docs.aws.amazon.com/cloudshell/latest/userguide/using-cshell-in-vpc.html)
- [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
- [Amazon SQS message quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html)
- [Uploading objects to Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html)
- [EBS General Purpose SSD volumes](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html)
- [Tutorials Dojo SAA-C03 practice exams](https://portal.tutorialsdojo.com/product/aws-certified-solutions-architect-associate-practice-exams/). The product page lists 401 questions and five modes; the number of timed sets differed between pages, so confirm it in her portal.

Not verified today, because the web-search budget ran out: the official 20-question practice set, pricing figures, and every [ledger] item.

Connector note: the Excalidraw, Gmail, Google Calendar and Google Drive connectors are not authorised in this session. They are not needed for this specification; to use them later, authorise them in claude.ai connector settings.

### Critical Files for Implementation

No book files exist yet. The first two are existing inputs; the last three are proposed locations for the files that control everything else.

- /Users/tatiatsmindashvili/Desktop/tatia/2026-plans/October.md — existing; dates, hour budgets, her Exam 2 and Exam 3 plans, the retake assumption to correct
- /Users/tatiatsmindashvili/Desktop/tatia/2026-plans/habits.md — existing; reader profile behind P1–P5
- /Users/tatiatsmindashvili/Desktop/tatia/2026-plans/saa-book/_spec/chapter-templates.md — proposed; sections 1, 2, 3 and the section 12 rubric
- /Users/tatiatsmindashvili/Desktop/tatia/2026-plans/saa-book/_spec/terms.yml — proposed; controlled vocabulary, respellings, collocations, Exam English list (drives style lint, glossary, Anki)
- /Users/tatiatsmindashvili/Desktop/tatia/2026-plans/saa-book/00-start/calendar.md — proposed; Plans A, B and C, the gates and the Today cards
