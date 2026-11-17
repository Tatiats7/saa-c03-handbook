# brief-28, part A: meta, naming, budgets, the sections of 1-fast.md and the H2 of How it works.
BRIEF["chapter"] = "28"
BRIEF["angle"] = (
    "follow one item through DynamoDB: what a table and an item are (1); where the item lands, by a hash of its partition key, "
    "in three Availability Zones, and why one hot key throttles (2); what each read and write costs in units and how consistent a "
    "read is (3); who pays for those units: on-demand per request (4) or provisioned capacity that auto scaling moves (5); how you "
    "find items again: Query against Scan (6) and secondary indexes (7); how two writers stay correct: conditions and transactions "
    "(8); how items leave: Time to Live (9) and how changes leave: DynamoDB Streams (10); how repeated reads get faster: DAX (11); "
    "how lost data comes back: backups and point-in-time recovery (12); how the item reaches other Regions: global tables (13); "
    "close with who may read it and how it is protected (14)")
BRIEF["brief_by"] = "brief-28"
BRIEF["written_at"] = "2026-10-14"
BRIEF["base"] = (
    "Shape of this brief: _build/work/27-aurora/brief.json (same wave, same template, accepted by the brief gate). House pattern of "
    "every How-it-works subsection: CONVENTIONS-2 U1 (problem, numbered trace with bold step names, compressing table, one Why "
    "reason, Exam signal, Exam trap or Go deeper, Say it, Stop and answer). Link texts in the plans are displays copied from "
    "_build/work/28-dynamodb/fact-cards.md (chapter 28 facts: dynamodb- and dax-) and from verified facts of neighbouring chapters "
    "(18 lambda-, 10 vpc-, 11 vpc-endpoints-, 29 elasticache-). The notation is always a display in square brackets, a space, then "
    "the fact id in parentheses: a ready-made link <display> -> ../facts/<service>.md#<fact-id>, where <service> is dynamodb for "
    "dynamodb- ids, dax for dax- ids, lambda, vpc, vpc-endpoints or elasticache. Copy each display exactly, backticks and quotes "
    "included, and lowercase its first letter in mid-sentence (CONVENTIONS-2 F2). Plain text in a plan is guidance, not wording. "
    "build_brief.py checked every display-and-id pair and every fact id of this brief against data/facts/*.jsonl on 2026-10-14.")
BRIEF["frozen"] = {
    "2-deep.md": "Nothing frozen. Write all 14 subsections from the plans below, in this order.",
    "items": "No exemplar items exist for DynamoDB; write every item from the slots below.",
}
BRIEF["naming"] = {
    "service": "Amazon DynamoDB at first use in each file, then DynamoDB. Never 'Dynamo' or 'DDB'.",
    "dax": ("Amazon DynamoDB Accelerator (DAX) at first use in each file, then DAX. 'DAX cluster', 'DAX client', 'item cache', 'query "
            "cache'."),
    "capacity_modes": ("'on-demand capacity mode' or 'on-demand mode' (lowercase, with a hyphen); 'provisioned capacity mode' or "
                       "'provisioned mode'. Never 'On-Demand' with capitals: that is Amazon EC2 On-Demand Instances. 'reserved "
                       "capacity' is the DynamoDB discount for provisioned capacity, never 'Reserved Instances'."),
    "units": ("read capacity unit (RCU), write capacity unit (WCU) in provisioned mode; read request unit (RRU), write request unit "
              "(WRU) in on-demand mode. Spell each short form out at first use in each file (U6)."),
    "keys": ("partition key, sort key, primary key (a partition key, or a partition key and a sort key). Never 'hash key' or 'range "
             "key' in prose (AWS's older names); a quote block keeps AWS's words."),
    "indexes": "global secondary index (GSI), local secondary index (LSI); 'index' alone after the full name.",
    "ttl": ("Write the bank term 'time to live (TTL)' in lowercase in prose; AWS writes 'Time to Live (TTL)', which stays inside quote "
            "blocks and link texts. A heading starts with a capital: 'Time to Live deletes ...'."),
    "pitr": "point-in-time recovery (PITR), with hyphens (the term bank bans 'point in time recovery').",
    "streams": ("'DynamoDB Streams' is the feature (capital S); 'a stream' is one table's stream; 'stream record'. The other model is "
                "'Kinesis Data Streams for DynamoDB' (the FAQ's name); write it in full every time."),
    "global_tables": ("'global table' (lowercase); 'replica table' at first use in each file, then 'replica'. Write 'replica table' "
                      "before any bare 'replica', because the term bank uses 'replica' as the short form of 'read replica' (W802). "
                      "Modes: multi-Region eventual consistency (MREC), multi-Region strong consistency (MRSC)."),
    "table_classes": "DynamoDB Standard and DynamoDB Standard-Infrequent Access (DynamoDB Standard-IA); then 'Standard-IA'.",
    "regions": ("Question stems may use real Region codes (us-east-1, us-west-2, eu-west-1). Story text uses US East (N. Virginia) and "
                "US West (Oregon) only."),
    "story_names": ("Callvale's table is 'jobs'; its index is 'by-customer'. Write 'call ID' and 'customer ID' in plain words in the "
                    "story; do not invent attribute names for Callvale. Generic examples in How it works may use code-style "
                    "attribute names (`customer_id`, `order_date`, `expires_at`)."),
}
BRIEF["budgets"] = {
    "rule": ("lint.word_count counts every word of a file: reveals, Go deeper blocks, prompts, alt text and captions included (code "
             "blocks and comments excluded). DynamoDB is not an XL chapter: 2-deep.md 3,500 to 4,500 words; How it works 2,600 to "
             "3,500 words; 8 to 14 subsections."),
    "2-deep.md_total_min": 3500,
    "2-deep.md_total_max": 4500,
    "how_it_works_max": 3500,
    "how_it_works_plan": ("14 subsections at 200 to 225 words all-in each (sum of words_all_in: 3,000; body, table, Exam signal, "
                          "Exam trap, Try it, Startup example, Spot the bug, Say it, Stop and answer with its reveal, and the alt "
                          "and caption of an embedded diagram) + 6 Go deeper blocks of at most 70 words (420) + the H2 intro line "
                          "(about 25) = about 3,445 of the 3,500 cap. Body plus callouts without prompts, reveals and Go deeper "
                          "stays at 150 to 400 words per subsection (W201)."),
    "per_subsection_all_in": ("200 to 225 words (words_all_in of each plan). Spend the words on the trace. A body_extras sentence is "
                              "written only if the subsection stays inside its words_all_in; depth that does not fit goes into the "
                              "six planned Go deeper blocks, nowhere else. If How it works runs over, cut body_extras first, then "
                              "the Go deeper of subsection 6, then the Go deeper of subsection 5."),
    "go_deeper_words_max_this_chapter": 70,
    "go_deeper_planned": 6,
    "spot_the_bug_planned": 2,
    "numbers_max": 290,
    "decision_record_max": 270,
    "faq_max": 430,
    "callouts_max_2_deep": 12,
    "callouts_planned_2_deep": ("11: Exam trap x8 (subsections 3, 4, 5, 6, 7, 8, 10, 12), Try it x2 (dynamodb-t02 in 6, "
                                "dynamodb-t03 in 8), Startup example x1 (subsection 4); Exam signal, Say it and Changed recently do "
                                "not count"),
    "1-fast.md_total_max": 1800,
    "fast_section_budget_note": ("The section maxima of the fast file add up to 1,900 words; the file cap is 1,800. Keep Choose it "
                                 "or not at about 440, Signals and traps at about 360 and Changed recently at about 105."),
    "fast_callouts_max": 6,
    "fast_callouts_planned": "2: Say it (one-breath) and Startup example; Changed recently entries do not count",
    "startup_example_words_chapter_max": 80,
    "startup_example_split": ("1-fast.md In one breath: the Problem word for word (49 words with the label); 2-deep.md subsection 4: "
                              "at most 30 words."),
    "realworld": "optional; write it only if 2-deep.md stays at or under 4,390 words without it; at most 100 words; see realworld",
}

S = BRIEF["sections"] = []
S.append({
    "file": "1-fast.md", "section": "predict", "heading": "Predict", "bullets": [], "facts": [], "status": "write", "minutes": 1,
    "plan": ("Three prompts, each ending with '?'. Predict 1 is the gist trap (<!-- gist-trap -->): 'A provisioned table uses only a "
             "fifth of its write capacity. Can writes to one popular item still be throttled?' (common sense says no, because the "
             "table has spare capacity; the answer is yes: one item lives in one partition, and each partition has its own ceiling). "
             "Predict 2: 'An application writes an item and reads it back at once with a default GetItem call. Is the new value "
             "guaranteed?' Predict 3: 'A global table has replica tables in two Regions. Can an application write to the replica "
             "table in the second Region?' Answers appear only in Check (U4). No term is defined in a prompt; no AWS number in a "
             "prompt. 'replica table', not 'replica' (naming)."),
})
S.append({
    "file": "1-fast.md", "section": "look-first", "heading": "Look first", "bullets": ["3.3.K4"],
    "facts": ["dynamodb-account-throughput-quota-provisioned", "dynamodb-table-throughput-quota-provisioned", "dynamodb-quotas-per-region"],
    "status": "write", "minutes": 3, "task": "dynamodb-t01",
    "plan": ("One task region for dynamodb-t01 (read-only, 3 minutes): read the account's and the table's maximum read and write "
             "capacity units with describe-limits, and list the tables of the Region. At most 80 words and at most 2 sentences "
             "around the region. The sentence may say that the numbers are quotas of the Region you are in: quotas apply on a "
             "[per-Region basis] (dynamodb-quotas-per-region)."),
})
S.append({
    "file": "1-fast.md", "section": "in-one-breath", "heading": "In one breath", "bullets": ["3.3.K8", "3.3.S4", "3.3.K1"],
    "facts": ["dynamodb-key-value-and-document", "dynamodb-decision-guide-key-value-session-store", "dynamodb-serverless-no-servers",
              "lambda-ddb-http-api-no-connections", "dynamodb-no-join-operator", "dynamodb-partition-key-hash-decides-partition",
              "dynamodb-faq-sync-replication-three-azs", "dynamodb-successful-write-http-200-durable",
              "dynamodb-eventually-consistent-default", "dynamodb-consistentread-parameter"],
    "status": "write", "minutes": 3,
    "plan": ("Say it (one-breath definition, at most 25 words, linked): 'Amazon DynamoDB is a serverless database for [key-value and "
             "document] (dynamodb-key-value-and-document) data. It gives [single-digit millisecond performance at any scale] "
             "(dynamodb-decision-guide-key-value-session-store), with no servers to manage.' (24 words; do not add words; 'no "
             "servers to manage' may instead link [don't need to provision any servers] (dynamodb-serverless-no-servers) if the "
             "count stays at 25). Then the bold field '**The problem it solves.**' in one or two sentences: a relational database "
             "keeps a connection and row locks for each client, and one busy server sets the ceiling; DynamoDB is an HTTP API "
             "([DynamoDB uses an HTTP API] (lambda-ddb-http-api-no-connections)) that spreads items over partitions, so it scales "
             "with the key, not with one server. Then 'Predict the picture: when an application writes one item, where does "
             "DynamoDB store it, and when does it say the write is safe?' with the hero dynamodb-hero inside a reveal, its caption "
             "and its 5 numbered steps (text fixed in diagrams below; link the facts named in facts_for_steps). Then the Startup "
             "example callout with the Problem of data/startup.json chapter 28 word for word (47 words, 4 sentences). Total at most "
             "280 words: keep the hero alt at about 45 words."),
})
S.append({
    "file": "1-fast.md", "section": "words-that-go-together", "heading": "Words that go together", "bullets": [], "facts": [],
    "status": "write", "minutes": 1,
    "plan": ("A words table of 8 rows (see words_table): cell 1 is the term field of data/terms.json with the respelling where the "
             "bank has one; cell 2 one collocation with exactly one bold partner word. Six of the eight terms are term_requests that "
             "the terms agent adds to data/terms.json right after this brief (orchestrator note); write them as plain bank terms, "
             "with no needs-term marker. If a row's term is still missing from the bank when you write, report it; do not invent a "
             "marker."),
})
S.append({
    "file": "1-fast.md", "section": "choose-it-or-not", "heading": "Choose it or not",
    "bullets": ["3.3.S4", "4.3.K9", "4.3.S3", "3.3.K8", "3.3.K2", "4.3.K5"],
    "facts": [],
    "status": "write", "minutes": 4,
    "plan": ("Four compare tables (see compare_tables), at most 4 columns and 3 rows each, each followed by its bold **Deciding "
             "question:** line. Each table title is an H3 inside this section; the titles are fixed below (unique section ids). At "
             "most 500 words (aim for 440). If the section runs over, cut row 3 of tables 1 and 4 first, never a row that a question "
             "slot needs."),
})
S.append({
    "file": "1-fast.md", "section": "signals-and-traps", "heading": "Signals and traps",
    "bullets": ["3.3.K2", "4.3.K4", "2.2.S2", "3.3.S2", "4.3.S3", "2.2.S5", "3.3.K3"],
    "facts": [],
    "status": "write", "minutes": 3,
    "plan": ("A signals table of 8 rows (see signals; columns: The stem says | Think | Because | But not if) and the fixed H3 'Traps' "
             "with the 5 fast traps, each a list item that ends with <!-- trap: <id> --> (see devices.fast_traps_list and "
             "devices.fast_traps_links). At most 380 words (aim for 360). If over budget, cut signal rows 7 then 8 (PITR, gateway "
             "endpoint), never fewer than 6 rows."),
})
S.append({
    "file": "1-fast.md", "section": "changed-recently", "heading": "Changed recently", "bullets": [],
    "facts": ["dynamodb-change-ondemand-price-cut-2024-11", "dynamodb-change-capacity-mode-switch-limit-2025-08",
              "dynamodb-change-gsi-multi-attribute-keys-2025-11", "dynamodb-change-mrsc-global-tables-ga-2025-06"],
    "status": "write", "minutes": 1,
    "plan": ("Three examinable entries (see changed_recently.fast), in the form of CONVENTIONS D6, at most 120 words in all (aim for "
             "105). The three facts have a changed record (date and was), and their dates are before book.exam_eligibility_cutoff "
             "2026-07-15, so each is examinable. The MRSC entry (changed_recently.pending) waits for the fact request filed by "
             "brief-28 (fact_requests): when it is filled, it replaces the GSI-keys entry; do not write it before."),
})
S.append({
    "file": "1-fast.md", "section": "check", "heading": "Check", "bullets": [],
    "facts": [],
    "status": "write", "minutes": 2,
    "plan": ("Three Check prompts parallel to Predict, each answered in its reveal, with a separate '**Predict <n>:**' paragraph (U4). "
             "Check 1: 'A table's partition key is `country`, and most users live in one country. The table has spare write "
             "capacity. Can writes for that country still be throttled at the peak?' (Yes: a key with a [small number of partition "
             "key values] (dynamodb-few-partition-keys-spread-writes) can create [\"hot\" partitions that result in throttling] "
             "(dynamodb-hot-partitions-cause-throttling). Predict 1: yes; the item is stored in the partition that the hash "
             "[determines the partition] (dynamodb-partition-key-hash-decides-partition), and a partition delivers at most [1,000 "
             "write units per second] (dynamodb-partition-max-throughput).) Check 2: 'A function writes an order. The next function "
             "reads it through a global secondary index. Can that read be strongly consistent?' (No: queries on global secondary "
             "indexes [support eventual consistency only] (dynamodb-index-read-consistency-gsi-vs-lsi); read the table itself with "
             "the [optional `ConsistentRead` parameter] (dynamodb-consistentread-parameter). Predict 2: no; [Eventually consistent "
             "is the default] (dynamodb-eventually-consistent-default).) Check 3: 'Two users change the same item at the same "
             "moment, one in us-east-1 and one in eu-west-1, in a global table with default settings. Which change remains?' (The "
             "later one: the default mode resolves conflicts by [last writer wins] (dynamodb-gt-mrec-default-last-writer-wins). "
             "Predict 3: yes; [Any global table replica] can [serve reads and writes] "
             "(dynamodb-global-table-any-replica-serves-reads-writes).) Write 'replica table' at first use (naming)."),
})
S.append({
    "file": "1-fast.md", "section": "recap-from-memory", "heading": "Recap from memory", "bullets": [], "facts": [], "status": "write",
    "minutes": 2,
    "plan": ("Three Recap prompts, each asking only for a sentence, row or cell that 1-fast.md states above (U4): what each capacity "
             "mode bills for (second compare table, row 2); which option the signals table gives for 'run code when an item "
             "changes', and its 'But not if' (signals row 5); when Time to Live deletes an expired item (trap list)."),
})
S.append({
    "file": "2-deep.md", "section": "how-it-works", "heading": "How it works", "bullets": [], "facts": [], "status": "write",
    "minutes": "sum of the subsection time boxes (54)",
    "order_note": ("Teaching order follows one item: the table and its key (1); where the item lands and why a hot key throttles "
                   "(2); what a read or write costs and how fresh a read is (3); who pays: on-demand (4) or provisioned with auto "
                   "scaling (5); finding items: Query and Scan (6), secondary indexes (7); keeping concurrent writes correct (8); "
                   "items leaving: Time to Live (9); changes leaving: DynamoDB Streams (10); faster repeated reads: DAX (11); "
                   "getting data back: backups and point-in-time recovery (12); other Regions: global tables (13); the guard: "
                   "IAM, encryption and private access (14). The H2 intro line (about 25 words) names this path; it is not a list "
                   "of subsections."),
})
