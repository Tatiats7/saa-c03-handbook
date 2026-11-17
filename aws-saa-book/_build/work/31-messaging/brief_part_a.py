# brief-31, part A: meta, naming, budgets, the sections of 1-fast.md and the H2 of How it works.
BRIEF["chapter"] = "31"
BRIEF["angle"] = (
    "follow one message through the three services: a producer sends it to an SQS queue, which stores it in several "
    "Availability Zones before the producer moves on (1); consumers poll for it, best with long polling (2); a received "
    "message stays hidden until it is deleted or the visibility timeout ends (3); a standard queue can deliver it twice, so the "
    "consumer is idempotent (4), while a FIFO queue keeps order per message group and drops duplicates (5); a message that keeps "
    "failing moves to a dead-letter queue (6); the workers scale on the backlog per instance (7), or Lambda polls the queue for "
    "you (8). When many systems need the same message, an SNS topic pushes it to every subscriber (9); a queue per subscriber "
    "keeps each copy (10); a filter policy decides which copy each subscription gets (11). Events from AWS services and SaaS "
    "partners go to EventBridge, where a rule matches content and sends events to targets (12); SNS and EventBridge retry, then "
    "drop a delivery unless a dead-letter queue catches it (13); and resource-based policies decide who may send to a queue, a "
    "topic or a bus (14)")
BRIEF["brief_by"] = "brief-31"
BRIEF["written_at"] = "2026-10-14"
BRIEF["base"] = (
    "Shape of this brief: _build/work/28-dynamodb/brief.json (same template, accepted by the brief gate). House pattern of "
    "every How-it-works subsection: CONVENTIONS-2 U1 (problem, numbered trace with bold step names, compressing table, one Why "
    "reason, Exam signal, Exam trap or Go deeper, Say it, Stop and answer). Link texts in the plans are displays copied from "
    "_build/work/31-messaging/fact-cards.md (chapter 31 facts: sqs-, sns- and eventbridge-) and from verified facts of "
    "neighbouring chapters (18 lambda-, 17 ec2-auto-scaling-, 19 ecs-, 21 s3-; their cards are in brief-lambda-cards.md and "
    "brief-as-cards.md in this folder). The notation is always a display in square brackets, a space, then the fact id in "
    "parentheses: a ready-made link <display> -> ../facts/<service>.md#<fact-id>, where <service> is the first part of the id "
    "(sqs, sns, eventbridge, lambda, ec2-auto-scaling, ecs, s3). Copy each display exactly, backticks, curly quotes and "
    "capitals included, and lowercase its first letter in mid-sentence only when the comparison allows it (case does not "
    "matter; punctuation does: CONVENTIONS-2 F2). Plain text in a plan is guidance, not wording. build_brief.py checked every "
    "display-and-id pair and every fact id of this brief against data/facts/*.jsonl on 2026-10-14.")
BRIEF["frozen"] = {
    "2-deep.md": "Nothing frozen. Write all 14 subsections from the plans below, in this order.",
    "items": "No exemplar items exist for messaging; write every item from the slots below.",
}
BRIEF["naming"] = {
    "services": ("Amazon Simple Queue Service (Amazon SQS), Amazon Simple Notification Service (Amazon SNS) and Amazon "
                 "EventBridge at first use in each file, then SQS, SNS and EventBridge. Never 'Simple Queue' alone, never "
                 "'CloudWatch Events' (former name of EventBridge; it may appear once as 'formerly Amazon CloudWatch Events' "
                 "only if a writer needs it; this brief does not need it). 'EventBridge Scheduler' and 'EventBridge Pipes' are "
                 "features: write 'Amazon EventBridge Scheduler' once at first use in a file, then 'EventBridge Scheduler'."),
    "queues": ("'standard queue' and 'FIFO queue' (FIFO in capitals, never 'Fifo'); 'queue' alone after the first mention. "
               "Say FIFO as letters or as 'FY-foh' (bank respelling of fifo-queue). Queue attributes keep AWS's API spelling in "
               "code style when named: `VisibilityTimeout`, `MessageRetentionPeriod`, `ReceiveMessageWaitTimeSeconds`, "
               "`DelaySeconds`, `maxReceiveCount`, `RedrivePolicy`. In prose prefer the plain words: visibility timeout, "
               "retention period, receive message wait time, delay, maximum receives."),
    "messages": ("'producer' sends, 'consumer' receives (both bank term requests). Never 'client' for a consumer. 'in-flight "
                 "message' = received, not yet deleted. 'poison-pill message' is AWS's phrase for a message that always fails."),
    "dlq": ("'dead-letter queue' with a hyphen (bank). The short form DLQ only after the full term in the same file, and only "
            "inside a link text or a quote that already writes DLQ."),
    "sns": ("'topic', 'subscription', 'subscriber', 'publish'. A queue is 'subscribed to' a topic. 'fan-out' as a noun, 'fan "
            "out' as a verb. 'filter policy' (lowercase)."),
    "eventbridge": ("'event bus' (default event bus, custom event bus, partner event bus), 'rule', 'event pattern', 'target'. "
                    "This chapter teaches the bus that AWS now calls 'Custom Event Bus - Classic' (rules and targets); the "
                    "new 'Custom Event Bus' of 2026-09-24 is not examinable yet and appears only in notes_for_orchestrator. "
                    "Never call an EventBridge rule a 'subscription'."),
    "regions": "Question stems may use real Region codes (us-east-1). Story text uses US East (N. Virginia) only (stage 2).",
    "story_names": ("Callvale's queues: uploads, convert, webhooks, indexing, each with <queue>-dlq (uploads-dlq, convert-dlq). "
                    "Topic: transcript-ready. Functions: start-job, save-results, notify. Write the names in code style in "
                    "prose (`uploads`), plain in diagram labels. Callvale has no FIFO queue and no ops-alerts rule yet "
                    "(ops-alerts arrives at stage 3, chapter 37)."),
    "slug": ("The chapter slug is 'messaging': trap ids messaging-trap-*, question ids messaging-q001 to messaging-q022, card "
             "ids messaging-c001 to messaging-c032, speak ids messaging-s01 to messaging-s04, task ids messaging-t01 to "
             "messaging-t03, diagram ids messaging-hero, messaging-fanout, messaging-eventbridge-routing, messaging-before, "
             "messaging-after."),
}
BRIEF["budgets"] = {
    "rule": ("lint.word_count counts every word of a file: reveals, Go deeper blocks, prompts, alt text and captions included "
             "(code blocks and comments excluded). Messaging is not an XL chapter: 2-deep.md 3,500 to 4,500 words; How it works "
             "2,600 to 3,500 words; 8 to 14 subsections."),
    "2-deep.md_total_min": 3500,
    "2-deep.md_total_max": 4500,
    "how_it_works_max": 3500,
    "how_it_works_plan": ("14 subsections at 195 to 225 words all-in each (sum of words_all_in: 2,975; body, table, Exam "
                          "signal, Exam trap, Try it, Startup example, Spot the bug, Say it, Stop and answer with its reveal, "
                          "and the alt and caption of an embedded diagram) + 6 Go deeper blocks of at most 60 words (360) + "
                          "the H2 intro line (about 25) = about 3,360 of the 3,500 cap. Body plus callouts without prompts, "
                          "reveals and Go deeper stays at 150 to 400 words per subsection (W201)."),
    "per_subsection_all_in": ("words_all_in of each plan. Spend the words on the trace. A body_extras sentence is written only "
                              "if the subsection stays inside its words_all_in; depth that does not fit goes into the six "
                              "planned Go deeper blocks, nowhere else. If How it works runs over, cut body_extras first, then "
                              "the Go deeper of subsection 3, then the Go deeper of subsection 12."),
    "go_deeper_words_max_this_chapter": 60,
    "go_deeper_planned": 6,
    "spot_the_bug_planned": 2,
    "numbers_max": 290,
    "decision_record_max": 270,
    "faq_max": 440,
    "callouts_max_2_deep": 12,
    "callouts_planned_2_deep": ("11: Exam trap x8 (subsections 3, 5, 6, 8, 10, 11, 13, 14), Try it x2 (messaging-t02 in 3, "
                                "messaging-t03 in 10), Startup example x1 (subsection 7); Exam signal, Say it and Changed "
                                "recently do not count"),
    "1-fast.md_total_max": 1800,
    "fast_section_budget_note": ("The section maxima of the fast file add up to 1,900 words; the file cap is 1,800. Aim: Predict "
                                 "95, Look first 60, In one breath 270, Words 150, Choose it or not 440, Signals and traps "
                                 "360, Changed recently 115, Check 140, Recap 75 = 1,705."),
    "fast_callouts_max": 6,
    "fast_callouts_planned": "2: Say it (one-breath) and Startup example; Changed recently entries do not count",
    "startup_example_words_chapter_max": 80,
    "startup_example_split": ("1-fast.md In one breath: the Problem word for word (48 words with the label); 2-deep.md "
                              "subsection 7: at most 30 words."),
    "realworld": "not written (see realworld): no verified case fact gives the year that the first paragraph needs",
}

S = BRIEF["sections"] = []
S.append({
    "file": "1-fast.md", "section": "predict", "heading": "Predict", "bullets": [], "facts": [], "status": "write", "minutes": 1,
    "plan": ("Three prompts, each ending with '?'. One plain line before them may say that the answers are in Check. Predict 1 "
             "is the gist trap (<!-- gist-trap -->): 'A worker receives a message from a queue and then crashes before it "
             "finishes the work. Is the message lost?' (common sense says yes, because the worker took it; the answer is no: "
             "the message stays in the queue, hidden, and comes back). Predict 2: 'Three services poll the same queue. Does "
             "each service get every message?' Predict 3: 'The target of an event rule is down for an hour. Does the event "
             "wait for it?' Answers appear only in Check (U4). No term is defined in a prompt; no AWS number in a prompt. At "
             "most 100 words."),
})
S.append({
    "file": "1-fast.md", "section": "look-first", "heading": "Look first", "bullets": ["2.1.K5"],
    "facts": ["eventbridge-default-bus-receives-aws-service-events"], "status": "write", "minutes": 3, "task": "messaging-t01",
    "plan": ("One task region for messaging-t01 (read-only, 3 minutes): list the queues, topics and event buses of the Region. "
             "At most 80 words and at most 2 sentences around the region. The sentence may say that the list of event buses "
             "already holds one bus, because every account has a [default event bus] "
             "(eventbridge-default-bus-receives-aws-service-events)."),
})
S.append({
    "file": "1-fast.md", "section": "in-one-breath", "heading": "In one breath", "bullets": ["2.1.K11", "3.2.K3", "2.1.S3"],
    "facts": ["sqs-wa-make-component-interactions-asynchronous", "sqs-send-stored-multi-az-before-ack",
              "sqs-receive-keeps-message-hidden", "sqs-manual-delete-after-processing", "sqs-undeleted-message-visible-again"],
    "status": "write", "minutes": 3,
    "plan": ("Say it (one-breath definition, at most 25 words, no absolute word, so it needs no link): 'Amazon SQS holds "
             "messages until a consumer pulls them. Amazon SNS pushes a copy to every subscriber. Amazon EventBridge sends "
             "events to targets by rules.' (24 words; do not add words). Then the bold field '**The problem it solves.**' in "
             "one or two sentences: a direct call makes the caller wait for the slowest part, and a failure on either side "
             "loses the request; these services let you [make component interactions asynchronous where possible] "
             "(sqs-wa-make-component-interactions-asynchronous). Then '**Predict the picture.** When a producer sends a "
             "message to a queue, where does the message wait, and when does it leave the queue?' with the hero "
             "messaging-hero inside a reveal (summary 'Show the picture'), its caption and its 5 numbered steps (text fixed in "
             "diagrams below; link the facts named in facts_for_steps). Then the Startup example callout with the Problem of "
             "data/startup.json chapter 31 word for word (46 words, 4 sentences): 'After each upload, Callvale's web "
             "application calls the worker and waits. On launch day, the worker was overloaded and 1,900 uploads failed. No "
             "upload can be lost again, and one failed recording must not block the others. Several systems must learn when a "
             "transcript is ready.' Total at most 280 words: keep the hero alt at about 50 words."),
})
S.append({
    "file": "1-fast.md", "section": "words-that-go-together", "heading": "Words that go together", "bullets": [], "facts": [],
    "status": "write", "minutes": 1,
    "plan": ("A words table of 8 rows (see words_table): cell 1 is the term field of data/terms.json with the respelling where "
             "the bank has one; cell 2 one collocation with exactly one bold partner word; cell 3 a plain meaning; cell 4 'do "
             "not confuse with'. Three of the eight terms (message group ID, fan-out, event bus) are term_requests that the "
             "terms agent adds to data/terms.json right after this brief (orchestrator note); write them as plain bank terms, "
             "with no needs-term marker. If a row's term is still missing from the bank when you write, report it. At most 160 "
             "words."),
})
S.append({
    "file": "1-fast.md", "section": "choose-it-or-not", "heading": "Choose it or not",
    "bullets": ["2.1.S3", "2.1.K2", "2.1.K11", "3.2.K3", "2.1.S1"], "facts": [], "status": "write", "minutes": 4,
    "plan": ("Four compare tables (see compare_tables), at most 4 columns and 3 rows each, each followed by its bold "
             "**Deciding question:** line. Each table title is an H3 inside this section; the titles are fixed below (unique "
             "section ids). At most 500 words (aim for 440). If the section runs over, cut the rows marked 'cut first', never "
             "a row that a question slot or a Recap prompt needs (table 1 row 2 is Recap 1)."),
})
S.append({
    "file": "1-fast.md", "section": "signals-and-traps", "heading": "Signals and traps",
    "bullets": ["2.1.S3", "3.2.S2", "2.1.K5", "2.1.S1", "3.2.S1"], "facts": [], "status": "write", "minutes": 3,
    "plan": ("A signals table of 8 rows (see signals; columns: The stem says | Think | Because | But not if) and the fixed H3 "
             "'Traps' with the 5 fast traps, each a list item '**Wrong belief:** ... **Truth:** ...' that ends with <!-- trap: "
             "<id> --> (see devices.fast_traps_list and devices.fast_traps_links). At most 380 words (aim for 360). If over "
             "budget, cut signal rows 8 then 7 (worker scaling, long polling), never fewer than 6 rows; row 6 is Recap 2."),
})
S.append({
    "file": "1-fast.md", "section": "changed-recently", "heading": "Changed recently", "bullets": [],
    "facts": ["sqs-change-max-message-size-1mib-2025", "eventbridge-change-event-size-1mb-2026", "sqs-change-fifo-dlq-redrive-2023"],
    "status": "write", "minutes": 1,
    "plan": ("Three examinable entries (see changed_recently.fast), in the form of CONVENTIONS D6, at most 120 words in all "
             "(aim for 115). Each fact has a changed record (date and was), and each date is before book.exam_eligibility_cutoff "
             "2026-07-15, so each is examinable. The not-examinable SNS entry (2026-09-18) stands in 2-deep.md under the B-list "
             "(changed_recently.deep), not here. If the section runs over, shorten the 'The exam probably expects:' lines, never "
             "drop the dates."),
})
S.append({
    "file": "1-fast.md", "section": "check", "heading": "Check", "bullets": [], "facts": [], "status": "write", "minutes": 2,
    "plan": ("Three Check prompts parallel to Predict, each answered in its reveal, with a separate '**Predict <n>:**' paragraph "
             "(U4). Check 1: 'A consumer receives a message and then loses its network connection before it deletes the "
             "message. The queue keeps its default settings. What happens to the message?' (It [becomes visible again in the "
             "queue] (sqs-undeleted-message-visible-again) when the visibility timeout ends, and another consumer can process "
             "it. Predict 1: no, it is not lost; messages [aren't lost even if the initial processing fails] "
             "(sqs-failed-processing-message-not-lost).) Check 2: 'A billing service and an email service must each get every "
             "order event, and must not lose events while they are down. What do you build?' (An SNS topic with one SQS queue "
             "for each service: [multiple SQS standard queues to the SNS topic] "
             "(sns-faq-fanout-identical-messages-to-multiple-sqs-queues). Predict 2: no; a queue gives each message to one "
             "consumer, which is [a single subscriber typically] (sqs-typically-single-subscriber-order-and-loss).) Check 3: 'An "
             "SNS subscription delivers to a partner's HTTPS endpoint, which is down for a whole day. Does SNS keep the "
             "message?' (No: the retry policy ends, and SNS [stops retrying the delivery and discards the message] "
             "(sns-retry-exhausted-discards-unless-dlq) unless [a dead-letter queue is attached to the subscription] "
             "(sns-retry-exhausted-discards-unless-dlq). Predict 3: it waits only while EventBridge retries, by default "
             "[24 hours] (eventbridge-retry-default-24h-185-attempts); then [the event is dropped] "
             "(eventbridge-retry-exhausted-event-dropped) unless a dead-letter queue catches it.) At most 150 words."),
})
S.append({
    "file": "1-fast.md", "section": "recap-from-memory", "heading": "Recap from memory", "bullets": [], "facts": [],
    "status": "write", "minutes": 2,
    "plan": ("Three Recap prompts, each asking only for a sentence, row or cell that 1-fast.md states above (U4): what each of "
             "SQS, SNS and EventBridge does with a message after it arrives (compare table 1, row 2); which option the signals "
             "table gives for 'a message fails again and again', and its 'But not if' (signals row 6); the truth of the trap "
             "about an SNS topic and an offline subscriber (trap list). At most 90 words."),
})
S.append({
    "file": "2-deep.md", "section": "how-it-works", "heading": "How it works", "bullets": [], "facts": [], "status": "write",
    "minutes": "sum of the subsection time boxes (51)",
    "order_note": ("Teaching order follows one message: into the queue (1); out by polling (2); hidden while it is processed "
                   "(3); delivered twice in a standard queue (4) or once and in order in a FIFO queue (5); set aside after "
                   "repeated failure (6); processed by workers that scale on the backlog (7) or by Lambda (8). Then one "
                   "message for many receivers: an SNS topic (9), one queue per receiver (10), a filter per subscription "
                   "(11). Then events from AWS and SaaS: EventBridge rules (12); what push services do when delivery fails "
                   "(13); who may send at all: resource-based policies (14). The H2 intro line (about 25 words) names this "
                   "path; it is not a list of subsections."),
})
