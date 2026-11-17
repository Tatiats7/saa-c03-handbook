# brief-27, part A: meta, budgets, the sections of 1-fast.md and the H2 of How it works.
BRIEF["chapter"] = "27"
BRIEF["angle"] = (
    "follow one Aurora cluster: what it is, DB instances on one shared volume (1); where a write lands, six copies in three "
    "Availability Zones (2), and how the volume grows and is billed (3); then follow the reads: Aurora Replicas read that same "
    "volume (4), the reader endpoint hands out connections (5); follow a failure: a replica is promoted behind the same endpoint (6); "
    "follow the load: Aurora Auto Scaling adds replicas (7) and Aurora Serverless v2 resizes the instance in ACUs (8); follow the data "
    "to another Region: Aurora Global Database (9), and the primary role moving by failover or switchover (10); follow the copies: "
    "continuous backups, restores to a new cluster, Backtrack and clones (11); follow the bill: Aurora Standard or I/O-Optimized (12); "
    "follow the data in: migrations from RDS and from other engines (13); close with encryption and access (14)")
BRIEF["brief_by"] = "brief-27"
BRIEF["written_at"] = "2026-10-14"
BRIEF["base"] = (
    "Shape of this brief: _build/work/26-rds/brief.json (same wave, same template). House pattern of every How-it-works subsection: "
    "CONVENTIONS-2 U1 (problem, numbered trace with bold step names, compressing table, one Why reason, Exam signal, Exam trap or "
    "Go deeper, Say it, Stop and answer). Link texts in the plans are displays copied from _build/work/27-aurora/fact-cards.md "
    "(chapter 27 facts: aurora- and aurora-serverless-) and from _build/work/27-aurora/nb-cards.md (verified facts of chapters 18, 26 "
    "and 28: rds-, rds-proxy-, dynamodb-, lambda-). The notation is always a display in square brackets, a space, then the fact id in "
    "parentheses: a ready-made link <display> -> ../facts/<service>.md#<fact-id>, where <service> is aurora for aurora- ids, "
    "aurora-serverless for aurora-serverless- ids, rds, rds-proxy, dynamodb or lambda. Copy each display exactly, backticks and straight or "
    "curly quotes included, and lowercase its first letter in mid-sentence (CONVENTIONS-2 F2). Plain text in a plan is guidance, not "
    "wording. build_brief.py checked every display-and-id pair and every fact id of this brief against data/facts/*.jsonl on 2026-10-14 "
    "(all verified).")
BRIEF["frozen"] = {
    "2-deep.md": "Nothing frozen. Write all 14 subsections from the plans below, in this order.",
    "items": "No exemplar items exist for Aurora; write every item from the slots below.",
}
BRIEF["naming"] = {
    "serverless": (
        "Write 'Aurora Serverless v2' (the exam's and the story's name; services.json lists 'Amazon Aurora Serverless'). The user guide now "
        "writes 'Aurora serverless' for the same thing; quote blocks and link texts keep AWS's spelling. Say once, in subsection 8 or the "
        "FAQ, that Aurora Serverless v1 is [a deprecated product with a different architecture] (aurora-serverless-platform-versions-not-serverless-v1); "
        "never teach v1 features."),
    "switchover": (
        "The fail-over term bans the variant 'switch over' (two words). The Aurora Global Database operation is 'switchover', one word, "
        "as a noun ('run a switchover'); never write 'switch over'. 'Failover' (noun) and 'fail over' (verb) follow the term bank."),
    "replica_words": (
        "'Aurora Replica' (capital R) is an instance of the same cluster. 'Aurora read replica' is AWS's name for a cluster that "
        "replicates from an RDS DB instance (migration, subsection 13) or, for Aurora MySQL, a cross-Region binlog replica cluster "
        "(subsection 9). 'read replica' alone means the RDS feature of chapter 26. Never write 'read-only replica' or 'reader database'."),
    "endpoints": "cluster endpoint (also called writer endpoint; say 'cluster endpoint'), reader endpoint, custom endpoint, instance endpoint, global writer endpoint (Aurora Global Database).",
    "regions": "Question stems may use real Region codes (us-east-1, us-west-2, eu-west-1). Story text uses US East (N. Virginia) and US West (Oregon) only.",
}
BRIEF["budgets"] = {
    "rule": ("lint.word_count counts every word of a file: reveals, Go deeper blocks, prompts, image alt text and captions included (code "
             "blocks and comments excluded). Aurora is not an XL chapter: 2-deep.md 3,500 to 4,500 words; How it works 2,600 to 3,500 words; "
             "8 to 14 subsections."),
    "2-deep.md_total_min": 3500,
    "2-deep.md_total_max": 4500,
    "how_it_works_max": 3500,
    "how_it_works_plan": ("14 subsections at about 215 words all-in each (sum of words_all_in: 3,010; body, table, Exam signal, Exam trap, "
                          "Try it, Startup example, Spot the bug, Say it, Stop and answer with its reveal, and the alt and caption of an embedded "
                          "diagram) + 5 Go deeper blocks of at most 70 words (350) + the H2 intro line (about 25) = about 3,385 of the 3,500 cap. "
                          "Body plus callouts without prompts, reveals and Go deeper stays at 150 to 400 words per subsection (W201)."),
    "per_subsection_all_in": ("190 to 225 words (words_all_in of each plan). Spend the words on the trace, not on lists. A body_extras sentence "
                              "is written only if the subsection stays inside its words_all_in; depth that does not fit goes into the five planned "
                              "Go deeper blocks, nowhere else."),
    "go_deeper_words_max_this_chapter": 70,
    "go_deeper_planned": 5,
    "spot_the_bug_planned": 2,
    "numbers_max": 290,
    "decision_record_max": 270,
    "faq_max": 430,
    "callouts_max_2_deep": 12,
    "callouts_planned_2_deep": ("11: Exam trap x8 (subsections 2, 5, 7, 8, 9, 10, 11, 12), Try it x2 (aurora-t02 in 10, aurora-t03 in 14), "
                                "Startup example x1 (subsection 4); Exam signal, Say it and Changed recently do not count"),
    "1-fast.md_total_max": 1800,
    "fast_section_budget_note": ("The section maxima of the fast file add up to 1,900 words; the file cap is 1,800. Keep Choose it or not at "
                                 "about 440 and Signals and traps at about 360."),
    "fast_callouts_max": 6,
    "fast_callouts_planned": "2: Say it (one-breath) and Startup example; Changed recently entries do not count",
    "startup_example_words_chapter_max": 80,
    "startup_example_split": "1-fast.md In one breath: the Problem word for word (48 words with the label); 2-deep.md subsection 4: at most 30 words.",
    "realworld": "optional; write it only if 2-deep.md stays at or under 4,390 words without it; at most 100 words; see realworld below",
}

S = BRIEF["sections"] = []
S.append({
    "file": "1-fast.md", "section": "predict", "heading": "Predict", "bullets": [], "facts": [], "status": "write", "minutes": 1,
    "plan": ("Three prompts, each ending with '?'. Predict 1 is the gist trap (<!-- gist-trap -->): 'An Aurora cluster has only one DB instance, "
             "and its storage keeps copies in three Availability Zones. If that DB instance fails, is the database back within seconds?' "
             "(common sense says yes, because the data is safe; the answer is no: without an Aurora Replica, Aurora recreates the instance). "
             "Predict 2: 'Your company runs an Aurora global database in two Regions. Can an application in the second Region write to the "
             "database there?' Predict 3: 'An Aurora Serverless v2 database has no users at night. Do you still pay for its compute at "
             "night?' Answers appear only in Check (U4). No term is defined in a prompt; no AWS number in a prompt."),
})
S.append({
    "file": "1-fast.md", "section": "look-first", "heading": "Look first", "bullets": ["3.3.K8"],
    "facts": ["aurora-quota-db-clusters-per-region", "aurora-serverless-db-serverless-instance-class-type", "aurora-is-managed-relational-engine"],
    "status": "write", "minutes": 3, "task": "aurora-t01",
    "plan": ("One task region for aurora-t01 (read-only, 3 minutes): read the account's DB cluster quota, the default Aurora PostgreSQL version "
             "with its parameter group family, and find db.serverless as an instance class of an ordinary Aurora cluster. At most 80 words "
             "and at most 2 sentences around the region."),
})
S.append({
    "file": "1-fast.md", "section": "in-one-breath", "heading": "In one breath", "bullets": ["3.3.K8", "3.3.S2"],
    "facts": ["aurora-is-managed-relational-engine", "aurora-storage-six-copies-three-azs", "aurora-cluster-endpoint-connects-to-current-primary",
              "aurora-synchronous-replication-to-six-storage-nodes", "aurora-reader-endpoint-balances-replicas",
              "aurora-adding-replicas-read-same-volume-offload", "aurora-auto-failover-to-replica", "aurora-cluster-endpoint-stays-same-after-failover"],
    "status": "write", "minutes": 3,
    "plan": ("Say it (one-breath definition, at most 25 words, linked): 'Amazon Aurora is a [fully managed relational database engine] "
             "(aurora-is-managed-relational-engine) for MySQL and PostgreSQL. DB instances share one volume that keeps [six copies] "
             "(aurora-storage-six-copies-three-azs) of the data.' (25 words; do not add words). Then the bold field '**The problem it solves.**' "
             "in one or two sentences: on a single-server database every replica and every new server needs its own full copy of the data; "
             "Aurora keeps the data in one shared, replicated volume, so replicas and failover need no copy. Then 'Predict the picture: when "
             "an application writes to an Aurora cluster with two Aurora Replicas, where does the data go, and where do the replicas read "
             "it from?' with the hero aurora-hero inside a reveal, its caption and its 5 numbered steps (text fixed in diagrams below; link "
             "the facts named in facts_for_steps). Then the Startup example callout with the Problem of data/startup.json chapter 27 word for "
             "word (48 words, 4 sentences). Total at most 280 words: keep the hero alt at about 45 words."),
})
S.append({
    "file": "1-fast.md", "section": "words-that-go-together", "heading": "Words that go together", "bullets": [], "facts": [],
    "status": "write", "minutes": 1,
    "plan": ("A words table of 8 rows (see words_table): cell 1 is the term field of data/terms.json with the respelling where the bank has one; "
             "cell 2 one collocation with exactly one bold partner word. Row 8 (reader endpoint) is not in the bank yet: write it with a "
             "needs-term marker (term_requests); L503 warns in draft."),
})
S.append({
    "file": "1-fast.md", "section": "choose-it-or-not", "heading": "Choose it or not",
    "bullets": ["3.3.S4", "4.3.K9", "3.3.K8", "2.1.K15", "4.3.S3", "2.2.S2"],
    "facts": ["aurora-is-managed-relational-engine", "rds-decision-guide-rds-row", "dynamodb-decision-guide-key-value-session-store",
              "aurora-storage-six-copies-three-azs", "rds-storage-ebs-striping", "rds-decision-guide-relational-joins",
              "dynamodb-no-joins-heart-of-nosql-modeling", "aurora-adding-replicas-read-same-volume-offload", "rds-read-replica-async-read-only",
              "rds-multi-az-instance-standby-no-reads", "aurora-auto-failover-to-replica", "rds-compare-failover-vs-promote",
              "aurora-failover-time-with-replica-guide", "rds-read-replica-promote-reboot-minutes", "rds-multi-az-instance-failover-time",
              "aurora-serverless-provisioned-suited-to-steady-workloads", "aurora-serverless-choose-variable-spiky-workloads",
              "aurora-instance-class-determines-compute-memory", "aurora-serverless-acu-about-2-gib-memory",
              "aurora-serverless-provisioned-constant-capacity-predict-ahead", "aurora-serverless-billing-unit-acu-hours",
              "aurora-global-db-only-primary-writes", "dynamodb-global-table-any-replica-serves-reads-writes",
              "aurora-global-db-failover-cross-region-to-secondary", "dynamodb-gt-multi-active-no-failover-needed",
              "aurora-dg-use-when-relational-modernize"],
    "status": "write", "minutes": 4,
    "plan": ("Four compare tables (see compare_tables), at most 4 columns and 3 rows each, each followed by its bold **Deciding question:** line. "
             "Each table title is an H3 inside this section; the titles are fixed below (unique section ids). At most 500 words (aim for 440). "
             "If the section runs over, cut the third row of tables 1 and 3 first, never a row that a question slot needs."),
})
S.append({
    "file": "1-fast.md", "section": "signals-and-traps", "heading": "Signals and traps",
    "bullets": ["3.3.S1", "2.1.K15", "4.3.S3", "2.2.K6", "2.2.S2", "3.3.S4"],
    "facts": ["aurora-adding-replicas-read-same-volume-offload", "dynamodb-decision-guide-key-value-session-store",
              "aurora-serverless-choose-variable-spiky-workloads", "aurora-pricing-reserved-instances-steady-state",
              "aurora-global-replication-latency-under-1-second", "aurora-no-cross-region-automated-backup-replication",
              "aurora-cmp-global-db-low-latency-reads-worldwide", "dynamodb-global-table-any-replica-serves-reads-writes",
              "aurora-auto-failover-to-replica", "aurora-failover-time-with-replica-guide", "aurora-failover-time-without-replica",
              "aurora-clone-shares-data-pages-separate-volume", "aurora-clone-same-region-only",
              "aurora-backtrack-in-minutes-no-new-cluster", "aurora-backtrack-not-for-postgresql",
              "aurora-io-optimized-no-io-charges", "aurora-standard-best-when-io-under-25-percent",
              "aurora-adding-replicas-read-same-volume-offload", "aurora-cluster-endpoint-only-one-for-writes",
              "aurora-reader-endpoint-balances-each-connection-read-only-session", "aurora-global-db-only-primary-writes",
              "aurora-global-db-write-forwarding-auto-forwards-to-primary", "aurora-global-db-switchover-healthy-only-unplanned-use-failover",
              "aurora-global-db-failover-use-for-unplanned-outage", "aurora-encryption-cannot-convert-unencrypted-in-place",
              "aurora-restore-unencrypted-snapshot-specify-kms-key", "aurora-replica-lag-under-100-ms"],
    "status": "write", "minutes": 3,
    "plan": ("A signals table of 8 rows (see signals; columns: The stem says | Think | Because | But not if) and the fixed H3 'Traps' with the "
             "5 fast traps, each a list item that ends with <!-- trap: <id> --> (see devices.fast_traps_list). At most 380 words (aim for 360). "
             "If over budget, cut signal rows 7 then 6 (Backtrack, clones), never fewer than 6 rows."),
})
S.append({
    "file": "1-fast.md", "section": "changed-recently", "heading": "Changed recently", "bullets": [],
    "facts": ["aurora-change-global-failover-managed-unplanned", "aurora-serverless-change-scale-to-zero",
              "aurora-global-secondary-regions-max-10", "aurora-change-storage-max-256-tib"],
    "status": "write", "minutes": 1,
    "plan": ("Three examinable entries (see changed_recently.fast), in the form of CONVENTIONS D6, at most 120 words in all. All three facts have "
             "a changed record (date and was) and dates before book.exam_eligibility_cutoff 2026-07-15, so each is examinable. The 256 TiB entry "
             "is the alternate: write it only if the three entries stay under 90 words. The default-encryption entry waits for the fact "
             "request fr-0092 (fact_requests); do not write it before the request is filled."),
})
S.append({
    "file": "1-fast.md", "section": "check", "heading": "Check", "bullets": [],
    "facts": ["aurora-failover-time-with-replica-guide", "aurora-az-outage-readers-in-other-azs-promoted", "aurora-failover-time-without-replica",
              "aurora-global-db-only-primary-writes", "aurora-write-forwarding-off-by-default-secondary",
              "aurora-write-forwarding-secondary-forward-sql-writes", "aurora-serverless-min-capacity-above-zero-no-pause",
              "aurora-serverless-auto-pause-min-capacity-zero"],
    "status": "write", "minutes": 2,
    "plan": ("Three Check prompts parallel to Predict, each answered in its reveal, with a separate '**Predict <n>:**' paragraph (U4). "
             "Check 1: 'A cluster has its writer in AZ 1 and one Aurora Replica in AZ 2. AZ 1 has an outage. What happens to the writer role, "
             "and about how long does it take?' (Aurora can [promote one of those reader instances] (aurora-az-outage-readers-in-other-azs-promoted); "
             "service is typically back in [less than 60 seconds] (aurora-failover-time-with-replica-guide). Predict 1: no; with no replica, "
             "Aurora recreates the instance, which typically takes [less than 10 minutes] (aurora-failover-time-without-replica).) "
             "Check 2: 'A secondary cluster of an Aurora global database runs in Europe. An application there sends an INSERT. What must be true "
             "for the INSERT to work without connecting to the primary Region?' (The secondary needs write forwarding: secondaries "
             "[forward SQL statements that perform write operations] (aurora-write-forwarding-secondary-forward-sql-writes) to the primary, and "
             "[write forwarding isn't enabled] when you add a secondary (aurora-write-forwarding-off-by-default-secondary). Predict 2: no; "
             "[Only the primary cluster performs write operations] (aurora-global-db-only-primary-writes).) Check 3: 'An Aurora Serverless v2 "
             "cluster has a minimum capacity of 0.5 ACUs and no connections at night. Does it pause?' (No: with a minimum [higher than zero "
             "ACUs] the instances [don't automatically pause] (aurora-serverless-min-capacity-above-zero-no-pause). Predict 3: it depends on the "
             "minimum: pausing needs the minimum capacity set [for the cluster to zero ACUs] (aurora-serverless-auto-pause-min-capacity-zero).) "
             "AZ 1 and AZ 2 are labels; 0.5 ACUs is an example value in the prompt."),
})
S.append({
    "file": "1-fast.md", "section": "recap-from-memory", "heading": "Recap from memory", "bullets": [], "facts": [], "status": "write", "minutes": 2,
    "plan": ("Three Recap prompts, each asking only for a sentence, row or cell that 1-fast.md states above (U4): where an Aurora Replica gets "
             "its data and where an RDS read replica gets its data (second compare table, first row); which option the signals table gives for "
             "'unpredictable or spiky load' and its 'But not if' (signals row 2); which Region of an Aurora global database accepts writes "
             "(trap list)."),
})
S.append({
    "file": "2-deep.md", "section": "how-it-works", "heading": "How it works", "bullets": [], "facts": [], "status": "write",
    "minutes": "sum of the subsection time boxes (50)",
    "order_note": ("Teaching order follows one cluster: what it is (1), where a write lands (2) and how the volume grows and is billed (3); "
                   "the reads: Aurora Replicas on the same volume (4) and the reader endpoint (5); a failure: promotion behind the same "
                   "endpoint (6); the load: Aurora Auto Scaling for readers (7) and Aurora Serverless v2 for capacity (8); a second Region: "
                   "Aurora Global Database (9) and failover or switchover (10); the copies: backups and restores (11); the bill: Standard "
                   "or I/O-Optimized (12); the way in: migrations (13); the guard: encryption and access (14). The H2 intro line (about 25 "
                   "words) names this path; it is not a list of subsections."),
})
