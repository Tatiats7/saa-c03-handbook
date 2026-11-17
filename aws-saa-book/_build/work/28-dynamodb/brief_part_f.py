# brief-28, part F: terms, tasks, speak, cards, diagrams, fact requests, notes.

BRIEF["terms"] = ["eventually-consistent", "throttling", "time-to-live", "point-in-time-recovery", "serverless", "idempotent",
                  "cache", "asynchronous", "durability", "recovery-point-objective", "recovery-time-objective"]


def T(tid, term, meaning, collocations, dnc, facts, short=None, kind="aws-name", respelling=None, banned=None):
    return {"id": tid, "term": term, "kind": kind, "short": short, "banned": banned or [], "banned_case": [], "avoid": [],
            "respelling": respelling, "meaning": meaning, "collocations": collocations, "do_not_confuse": dnc, "facts": facts}


BRIEF["term_requests"] = [
    T("partition-key", "partition key", "The key attribute whose value DynamoDB hashes to choose the partition that stores an item.",
      ["choose a partition key", "a partition key with many distinct values"], ["sort key", "primary key"],
      ["dynamodb-partition-key-hash-decides-partition"], banned=["hash key (in prose)"]),
    T("sort-key", "sort key", "The second part of a composite primary key; items with the same partition key are stored in sort key order.",
      ["a sort key condition", "query a range of sort keys"], ["partition key", "secondary index"],
      ["dynamodb-composite-key-same-pk-sorted-together"], banned=["range key (in prose)"]),
    T("primary-key", "primary key", "The attribute or attributes that identify each item in a DynamoDB table: a partition key, or a partition key and a sort key.",
      ["specify the primary key", "a composite primary key"], ["partition key", "index key"], ["dynamodb-faq-primary-key-two-forms"], kind="concept"),
    T("item-collection", "item collection", "All items in a table or local secondary index that share one partition key value.",
      ["query an item collection"], ["partition"], ["dynamodb-item-collection-range-retrieval"], kind="concept"),
    T("hot-partition", "hot partition", "A partition that gets much more traffic than the others and is throttled while the rest of the table has spare capacity.",
      ["avoid a hot partition", "spread the load off a hot partition"], ["throttling of the whole table"],
      ["dynamodb-hot-partitions-cause-throttling"], kind="concept"),
    T("write-sharding", "write sharding", "Adding a suffix to a busy partition key value so that its writes spread over more key values.",
      ["shard writes with a random suffix"], ["database sharding of a relational database"], ["dynamodb-write-sharding-random-suffix"], kind="concept"),
    T("adaptive-capacity", "adaptive capacity", "A DynamoDB feature that automatically gives more throughput to the partitions that receive more traffic.",
      ["adaptive capacity rebalances partitions"], ["auto scaling"], ["dynamodb-adaptive-capacity-instant"]),
    T("strongly-consistent-read", "strongly consistent read", "A read that returns the most up-to-date data, reflecting every earlier successful write.",
      ["request a strongly consistent read", "set ConsistentRead to true"], ["eventually consistent read"],
      ["dynamodb-consistentread-parameter"], kind="concept"),
    T("read-capacity-unit", "read capacity unit", "In provisioned mode, one strongly consistent read per second, or two eventually consistent reads per second, of an item up to 4 KB.",
      ["provision read capacity units"], ["read request unit (on-demand mode)"], ["dynamodb-rcu-definition"], short="RCU"),
    T("write-capacity-unit", "write capacity unit", "In provisioned mode, one write per second of an item up to 1 KB.",
      ["provision write capacity units"], ["write request unit (on-demand mode)"], ["dynamodb-wcu-definition"], short="WCU"),
    T("read-request-unit", "read request unit", "In on-demand mode, the unit of one strongly consistent read, or two eventually consistent reads, of an item up to 4 KB.",
      ["be billed in read request units"], ["read capacity unit (provisioned mode)"], ["dynamodb-rru-definition"], short="RRU"),
    T("write-request-unit", "write request unit", "In on-demand mode, the unit of one write of an item up to 1 KB.",
      ["be billed in write request units"], ["write capacity unit (provisioned mode)"], ["dynamodb-wru-definition"], short="WRU"),
    T("on-demand-capacity-mode", "on-demand capacity mode", "A DynamoDB capacity mode that bills each read and write request and needs no capacity plan.",
      ["switch a table to on-demand capacity mode", "create the table in on-demand mode"], ["On-Demand Instance (Amazon EC2)", "provisioned capacity mode"],
      ["dynamodb-ondemand-billed-per-request-zero-traffic-free"]),
    T("provisioned-capacity-mode", "provisioned capacity mode", "A DynamoDB capacity mode in which you set reads and writes per second and pay for that capacity each hour.",
      ["set provisioned capacity", "provisioned mode with auto scaling"], ["on-demand capacity mode", "Provisioned IOPS"],
      ["dynamodb-provisioned-billing-basis"]),
    T("reserved-capacity", "reserved capacity", "A one-year or three-year commitment that lowers the price of provisioned capacity in the DynamoDB Standard table class.",
      ["buy reserved capacity"], ["Reserved Instance", "Savings Plans"], ["dynamodb-reserved-capacity-terms-and-discount"]),
    T("warm-throughput", "warm throughput", "The number of reads and writes a table or index can serve at once; you can raise it to pre-warm a table before a peak.",
      ["pre-warm a table", "raise the warm throughput"], ["provisioned capacity"], ["dynamodb-warm-throughput-definition"]),
    T("filter-expression", "filter expression", "A condition that removes items from a Query or Scan result after they are read; it does not lower the read capacity used.",
      ["add a filter expression"], ["key condition expression"], ["dynamodb-scan-filter-same-read-capacity"], kind="concept"),
    T("global-secondary-index", "global secondary index", "An index with its own partition key and optional sort key that spans the whole table; you can add it at any time, and its reads are eventually consistent.",
      ["add a global secondary index", "query a global secondary index"], ["local secondary index"],
      ["dynamodb-gsi-key-schema-can-differ", "dynamodb-index-read-consistency-gsi-vs-lsi"], short="GSI"),
    T("local-secondary-index", "local secondary index", "An index with the table's partition key and another sort key; you define it when you create the table, and it allows strongly consistent reads.",
      ["define a local secondary index", "query a local secondary index"], ["global secondary index"],
      ["dynamodb-lsi-same-partition-key", "dynamodb-lsi-created-with-table"], short="LSI"),
    T("projection", "projection", "The set of table attributes that DynamoDB copies into a secondary index.",
      ["project attributes into an index", "a KEYS_ONLY projection"], ["projection expression (attributes a read returns)"],
      ["dynamodb-projection-keys-always-projected"], kind="concept"),
    T("sparse-index", "sparse index", "An index that holds only the items that have its key attribute.",
      ["design a sparse index"], ["filter expression"], ["dynamodb-sparse-index-definition"], kind="concept"),
    T("conditional-write", "conditional write", "A write that succeeds only if the item meets a condition you give; otherwise it fails and changes nothing.",
      ["make a conditional write", "the condition check fails"], ["transaction"], ["dynamodb-conditional-write-succeeds-only-if-condition"], kind="concept"),
    T("optimistic-locking", "optimistic locking", "A version attribute on each item, so that a write succeeds only if the item still has the version you read.",
      ["use optimistic locking", "a version attribute"], ["a lock that blocks readers"], ["dynamodb-optimistic-locking-detects-conflicts-at-write"], kind="concept"),
    T("dynamodb-transaction", "transaction", "In DynamoDB, a group of reads or writes on several items that succeed or fail together.",
      ["run a transaction", "an all-or-nothing transaction"], ["batch write (can partly succeed)"],
      ["dynamodb-transactions-acid-multiple-items-tables"], kind="concept"),
    T("dynamodb-streams", "DynamoDB Streams", "An optional DynamoDB feature that records each item change of a table, in order for each item, and keeps each record for a day.",
      ["enable DynamoDB Streams", "read a stream record"], ["Kinesis Data Streams for DynamoDB", "Amazon Kinesis Data Streams"],
      ["dynamodb-streams-optional-feature", "dynamodb-stream-records-24-hours"]),
    T("stream-view-type", "stream view type", "The stream setting that decides what each record holds: the keys only, the new item, the old item, or both.",
      ["choose a stream view type"], ["projection"], ["dynamodb-streams-view-new-and-old-images"]),
    T("dynamodb-accelerator", "Amazon DynamoDB Accelerator", "A managed in-memory cache in front of DynamoDB that answers eventually consistent reads in microseconds.",
      ["put DAX in front of a table", "use the DAX client"], ["Amazon ElastiCache"], ["dax-eventually-consistent-microsecond-latency"], short="DAX"),
    T("write-through-cache", "write-through cache", "A cache that is written at the same time as the database, so that it stays current.",
      ["a write-through cache"], ["lazy loading (cache-aside)"], ["dax-is-write-through-cache"], kind="concept"),
    T("global-table", "global table", "A DynamoDB table with replica tables in two or more Regions, each of which accepts reads and writes.",
      ["create a global table", "add a replica to a global table"], ["Aurora Global Database"],
      ["dynamodb-global-table-any-replica-serves-reads-writes"]),
    T("replica-table", "replica table", "One Region's copy of a DynamoDB global table.",
      ["add a replica table in another Region"], ["read replica (Amazon RDS)", "Aurora Replica"], ["dynamodb-global-table-one-replica-per-region"]),
    T("multi-region-eventual-consistency", "multi-Region eventual consistency", "The default mode of a global table: writes replicate asynchronously, and the last writer wins a conflict.",
      ["a global table in MREC mode"], ["multi-Region strong consistency"], ["dynamodb-gt-mrec-default-last-writer-wins"], short="MREC"),
    T("multi-region-strong-consistency", "multi-Region strong consistency", "A global table mode in exactly three Regions in which a strongly consistent read returns the latest write from any Region.",
      ["a global table in MRSC mode"], ["multi-Region eventual consistency"], ["dynamodb-gt-mrsc-exactly-three-regions"], short="MRSC"),
    T("last-writer-wins", "last writer wins", "The rule that keeps the most recent write when two Regions change the same item.",
      ["resolve conflicts by last writer wins"], ["a transaction across Regions"], ["dynamodb-gt-mrec-default-last-writer-wins"], kind="concept"),
    T("table-class", "table class", "The DynamoDB table setting that trades storage price against request price: DynamoDB Standard or DynamoDB Standard-IA.",
      ["switch the table class"], ["storage class (Amazon S3)"], ["dynamodb-faq-table-classes-two"]),
    T("on-demand-backup", "on-demand backup", "A full backup of a DynamoDB table that you start yourself; it uses no table throughput.",
      ["create an on-demand backup"], ["point-in-time recovery"], ["dynamodb-backup-full-table-every-time"]),
]
BRIEF["term_amendments"] = [
    {"id": "time-to-live", "add_meaning": "In DynamoDB, a per-item expiry time after which DynamoDB deletes the item in the background.",
     "add_collocations": ["enable TTL on a table", "a TTL attribute"], "add_facts": ["dynamodb-ttl-per-item-expiration-timestamp"],
     "why": "The bank's meaning is about caches and DNS; the words table row 8 uses the DynamoDB collocation 'enable TTL on a table'."},
    {"id": "point-in-time-recovery", "add_meaning": "In DynamoDB, the restore creates a new table.", "add_short": "PITR",
     "add_facts": ["dynamodb-pitr-restores-to-new-table"],
     "why": "The bank's meaning names Aurora only; DynamoDB writes the short form PITR."},
]
BRIEF["terms_note"] = ("terms lists only bank terms (B11). Per the orchestrator note, term_requests holds every new term that the "
                       "chapter defines in bold, as a ready bank entry (id, term, kind, short, meaning, collocations, do_not_confuse, "
                       "facts); the terms agent adds them to data/terms.json right after this brief and appends their ids to terms, "
                       "and applies term_amendments. Writers then need no needs-term marker. Respell only bank respellings (STYLE 4). "
                       "'transaction' gets the id dynamodb-transaction because the plain word is common in other chapters.")

BRIEF["tasks"] = [
    {"id": "dynamodb-t01", "type": "look", "title": "Read the throughput limits of your account",
     "section": "1-fast.md#look-first",
     "kills": "\"A DynamoDB table has no throughput limit.\"",
     "trap": None, "pass_route": False, "status": "write",
     "plan": ("In AWS CloudShell, read-only, 3 minutes, $0. (1) aws dynamodb describe-limits --output table: expect four numbers, the "
              "account and table maximum read and write capacity units of this Region; by default the account values are [80,000 "
              "read capacity units] (dynamodb-account-throughput-quota-provisioned) and the table values [40,000 read capacity units] "
              "(dynamodb-table-throughput-quota-provisioned), and both can be raised. (2) aws dynamodb list-tables --output table: "
              "expect the tables of this Region, or an empty list. Step text: quotas apply on a [per-Region basis] "
              "(dynamodb-quotas-per-region). Creates nothing. The writer confirms both operations and their output fields with tasks "
              "check-cli --reference."),
     "facts": ["dynamodb-account-throughput-quota-provisioned", "dynamodb-table-throughput-quota-provisioned", "dynamodb-quotas-per-region",
               "dynamodb-throughput-quota-not-max"]},
    {"id": "dynamodb-t02", "type": "try", "title": "Compare a Query and a Scan with consumed capacity shown",
     "section": "2-deep.md#" + anchor("A Query reads one partition key, but a Scan reads every item"),
     "kills": "\"A filter expression makes a Scan read less and cost less.\"",
     "trap": "dynamodb-trap-filter-saves-capacity", "pass_route": True, "status": "write",
     "plan": ("In AWS CloudShell, about 8 minutes. Steps: aws dynamodb create-table --table-name saa-dynamodb-t02 --attribute-definitions "
              "AttributeName=pk,AttributeType=S AttributeName=sk,AttributeType=S --key-schema AttributeName=pk,KeyType=HASH "
              "AttributeName=sk,KeyType=RANGE --billing-mode PAY_PER_REQUEST --tags Key=book,Value=saa Key=task,Value=dynamodb-t02 "
              "(KeyType values HASH and RANGE are API names: the step text calls them partition key and sort key); aws dynamodb wait "
              "table-exists --table-name saa-dynamodb-t02; three put-item steps (two items with pk 'a', one with pk 'b'; --item with "
              "inline JSON); aws dynamodb query --table-name saa-dynamodb-t02 --key-condition-expression \"pk = :p\" "
              "--expression-attribute-values '{\":p\":{\"S\":\"a\"}}' --return-consumed-capacity TOTAL: expect two items and a "
              "ConsumedCapacity value. Break it: predict 'Does a filter that keeps only pk a make the Scan cheaper than a Scan without "
              "a filter?'; aws dynamodb scan --table-name saa-dynamodb-t02 --filter-expression \"pk = :p\" with the same values and "
              "--return-consumed-capacity TOTAL, then the same scan without the filter: expect the same ConsumedCapacity for both "
              "scans; explain: the filter is [applied after a `Scan` finishes] (dynamodb-scan-filter-same-read-capacity), so the Scan "
              "[consumes the same amount of read capacity] (dynamodb-scan-filter-same-read-capacity). Fix: the Query above reads "
              "only the item collection of pk 'a'. Cleanup: aws dynamodb delete-table --table-name saa-dynamodb-t02. Verify: aws "
              "dynamodb describe-table --table-name saa-dynamodb-t02 with expect 'ResourceNotFoundException' (T108 by-name "
              "exception, R6). Cost line: 'about $0: an on-demand table that holds three small items for a few minutes and gets "
              "fewer than 20 requests; on-demand mode is [billed per read or write request] "
              "(dynamodb-ondemand-billed-per-request-zero-traffic-free)' with cost_facts [] unless a dollar amount above 0 is "
              "written (T109). If forgotten: an idle on-demand table pays nothing for throughput ([you are not charged for any "
              "throughput] (dynamodb-ondemand-billed-per-request-zero-traffic-free)); storage of a few bytes rounds to $0. Label "
              "'checked against docs, not run in a real account'. With tiny items the consumed capacity of all three reads can be "
              "small: the expect lines describe what to compare, not exact values. The writer confirms the JSON quoting and every "
              "operation with tasks check-cli --reference."),
     "facts": ["dynamodb-scan-filter-same-read-capacity", "dynamodb-query-filter-same-read-capacity", "dynamodb-scan-reads-every-item",
               "dynamodb-query-partition-key-equality-only", "dynamodb-ondemand-billed-per-request-zero-traffic-free",
               "dynamodb-read-capacity-by-items-read-not-returned"]},
    {"id": "dynamodb-t03", "type": "try", "title": "Make a conditional write refuse an overwrite",
     "section": "2-deep.md#" + anchor("Conditional writes and transactions stop one write from overwriting another"),
     "kills": "\"A second PutItem with the same key fails on its own.\"",
     "trap": None, "pass_route": False, "status": "write",
     "plan": ("In AWS CloudShell, about 6 minutes. Steps: create-table saa-dynamodb-t03 (partition key pk of type S, on-demand, tags "
              "Key=book,Value=saa Key=task,Value=dynamodb-t03); wait table-exists; put-item with pk 'job1' and status 'new'. Break "
              "it: predict 'Will a second put-item with the same key fail?'; put-item with pk 'job1' and status 'done': expect no "
              "error; get-item with --consistent-read shows status 'done'; explain: PutItem is [unconditional] "
              "(dynamodb-writes-unconditional-by-default) and [overwrites an existing item] (dynamodb-writes-unconditional-by-default). "
              "Fix: put-item with pk 'job1', status 'new' and --condition-expression \"attribute_not_exists(pk)\": expect "
              "ConditionalCheckFailedException; explain: the write succeeds only [if there is not already an item] "
              "(dynamodb-conditional-write-use-cases). Cleanup: delete-table saa-dynamodb-t03. Verify: describe-table with the name, "
              "expect 'ResourceNotFoundException' (T108 by-name exception). Cost line as in dynamodb-t02 (about $0, a few "
              "requests). Label 'checked against docs, not run in a real account'. The writer confirms the error name of the fix step "
              "with tasks check-cli --reference."),
     "facts": ["dynamodb-writes-unconditional-by-default", "dynamodb-conditional-write-use-cases",
               "dynamodb-conditional-write-succeeds-only-if-condition", "dynamodb-consistentread-parameter",
               "dynamodb-ondemand-billed-per-request-zero-traffic-free"]},
]

BRIEF["speak"] = [
    {"id": "dynamodb-s01", "kind": "decide", "persona": "Ben, CTO of Callvale",
     "prompt": "On-demand or provisioned capacity? I do not know my traffic yet.",
     "section": "2-deep.md#" + anchor("On-demand mode bills each request and needs no capacity plan"), "pass_route": True,
     "facts": ["dynamodb-on-demand-default-recommended", "dynamodb-on-demand-no-capacity-planning", "dynamodb-ondemand-billed-per-request-zero-traffic-free",
               "dynamodb-on-demand-previous-peak-double", "dynamodb-warm-throughput-prewarm-for-peak-events", "dynamodb-faq-provisioned-for-predictable",
               "dynamodb-provisioned-billing-basis", "dynamodb-reserved-capacity-terms-and-discount", "dynamodb-capacity-mode-switch-four-per-24h"],
     "note": ("Ben talks in short technical sentences and wants the fewest moving parts. Short answer: start in on-demand mode; move "
              "to provisioned capacity once the traffic is steady and you can forecast it. How it works: on-demand bills each request "
              "and sets capacity for you; provisioned bills the reads and writes per second you set, used or not, and reserved "
              "capacity lowers that rate. Watch: on-demand follows up to double the previous peak at once; before a launch far above "
              "that, pre-warm the table. In your case: 'What does your busiest hour look like after the launch?' Must not say: "
              "'on-demand has no limits'; 'provisioned is always cheaper'; 'you can never switch back'. Numbers as words from the "
              "say forms: double the previous peak; switching back to provisioned at any time. The four-per-day switch limit is "
              "volatile: say 'a few times a day', or leave it out.")},
    {"id": "dynamodb-s02", "kind": "compare", "persona": "a startup founder in office hours",
     "prompt": "DynamoDB or PostgreSQL: which database should our new app start with?",
     "section": "1-fast.md#choose-it-or-not", "pass_route": False,
     "facts": ["dynamodb-decision-guide-key-value-session-store", "dynamodb-no-join-operator", "dynamodb-decision-guide-aurora-relational-joins",
               "dynamodb-nosql-design-access-patterns-first-few-tables", "dynamodb-serverless-no-servers", "dynamodb-ondemand-billed-per-request-zero-traffic-free",
               "dynamodb-wa-oltp-dynamodb-vs-rds-joins"],
     "note": ("First sentence starts 'Both': both are managed, durable databases; the difference is how you ask for data. Short "
              "answer: DynamoDB if you know your access patterns and they are key lookups at scale; PostgreSQL if you need joins and "
              "new ad hoc queries. How it works: DynamoDB stores items by key and answers known patterns fast at any scale, with no "
              "servers and pay per request; PostgreSQL runs SQL with joins on instances you size. Watch: in DynamoDB you design the "
              "table from the questions it must answer, and a new question can need a new index. In your case: 'Can you list the "
              "five queries your app runs most?' Must not say: 'DynamoDB supports joins'; 'NoSQL means no schema at all'; "
              "'PostgreSQL cannot scale'. Numbers as words: single-digit milliseconds.")},
    {"id": "dynamodb-s03", "kind": "explain", "persona": "a startup CTO you advise",
     "prompt": "Our DynamoDB table shows spare capacity, but some writes are throttled. Why?",
     "section": "2-deep.md#" + anchor("A hash of the partition key picks the partition, so hot keys throttle"), "pass_route": False,
     "facts": ["dynamodb-partition-key-hash-decides-partition", "dynamodb-partition-max-throughput", "dynamodb-hot-partitions-throttle-while-others-underutilized",
               "dynamodb-uniform-distribution-distinct-keys", "dynamodb-write-sharding-random-suffix", "dynamodb-adaptive-capacity-isolates-hot-items",
               "dynamodb-throttling-key-range-hot-partitions"],
     "note": ("Short answer: the capacity is spread over partitions, and one hot key is hitting one partition's ceiling. How it works: "
              "DynamoDB hashes the partition key to place each item; each partition serves up to three thousand reads and one "
              "thousand writes per second; when most writes go to one key, that partition throttles while others sit idle. Watch: "
              "raising table capacity does not fix it; spread the key, for example with a random suffix, or pick a key with many "
              "values. In your case: 'Which key gets the most writes, and can we split it?' Must not say: 'add more capacity'; "
              "'switch to on-demand and it goes away'; 'DynamoDB has no limits'. Numbers as words: three thousand read units and one "
              "thousand write units per second.")},
    {"id": "dynamodb-s04", "kind": "explain", "persona": "Ana, CEO of Callvale",
     "prompt": "If the AWS Region we use goes down, do we lose our job records?",
     "section": "2-deep.md#" + anchor("In a global table, every replica accepts reads and writes"), "pass_route": False,
     "facts": ["dynamodb-faq-sync-replication-three-azs", "dynamodb-successful-write-http-200-durable", "dynamodb-pitr-automatic-continuous-backups",
               "dynamodb-global-table-any-replica-serves-reads-writes", "dynamodb-dr-global-tables-mrec-rto-zero", "dynamodb-faq-global-tables-no-failover-needed"],
     "note": ("Ana uses no AWS terms: explain a Region as 'one AWS location with several separate data centers' and an Availability "
              "Zone as 'one of those data centers' the first time. Short answer: a single data center failing loses nothing; a whole "
              "Region going down stops the service until it returns, unless we keep a copy in a second Region. How it works: each "
              "write is copied to three Availability Zones before DynamoDB confirms it; continuous backups let us restore a table; a "
              "global table later keeps a live copy in a second Region that can take over in seconds. Watch: the second Region "
              "doubles part of the database bill, so it waits for the bank's recovery requirement. In your case: 'How many minutes "
              "of downtime can our customers accept?' Must not say: 'the data is copied to another Region automatically'; 'a Region "
              "can never fail'; 'backups make us available during the outage'. Numbers as words: three Availability Zones; a few "
              "seconds of data.")},
]

C = BRIEF["cards"] = []


def card(t, deck, section, facts, trap, front, back):
    C.append({"id": "dynamodb-c%03d" % (len(C) + 1), "type": t, "deck": deck, "section": section, "facts": facts, "trap": trap,
              "front": front, "back": back})


card("number", "core", sec("A table stores"), ["dynamodb-item-size-max"], None,
     "In DynamoDB, what is the maximum size of one item?", "400 KB, attribute names included.")
card("number", "core", sec("A hash of the partition key"), ["dynamodb-partition-max-throughput"], "dynamodb-trap-spare-capacity-no-throttle",
     "In DynamoDB, what can one partition serve at most?", "3,000 read units per second and 1,000 write units per second.")
card("number", "core", sec("Read and write units"), ["dynamodb-read-rounding-4kb"], None,
     "In DynamoDB, how is the size of a read rounded?", "Up to the next 4 KB multiple.")
card("number", "core", sec("Read and write units"), ["dynamodb-write-rounding-1kb"], None,
     "In DynamoDB, how is the size of a write rounded?", "Up to the next 1 KB multiple.")
card("number", "core", sec("A Query reads"), ["dynamodb-query-result-1mb"], None,
     "In DynamoDB, how much data can one Query call return?", "1 MB per call; continue with LastEvaluatedKey.")
card("number", "core", sec("DynamoDB Streams"), ["dynamodb-stream-records-24-hours"], "dynamodb-trap-stream-keeps-changes",
     "In DynamoDB Streams, how long does a stream record live?", "A lifetime of 24 hours.")
card("number", "core", sec("Secondary indexes"), ["dynamodb-index-limits-20-gsi-5-lsi"], "dynamodb-trap-lsi-added-later",
     "In DynamoDB, how many local secondary indexes can one table have?", "Up to 5 local secondary indexes, defined with the table.")
card("number", "core", sec("Secondary indexes"), ["dynamodb-lsi-collection-one-partition"], None,
     "In DynamoDB, how large can an item collection grow in a table with an LSI?", "10 GB.")
card("differ", "core", sec("Read and write units"), ["dynamodb-eventually-consistent-default"], "dynamodb-trap-default-read-is-latest",
     "In DynamoDB, which read is the default: eventually consistent or strongly consistent?", "Eventually consistent.")
card("decide", "core", sec("On-demand mode"), ["dynamodb-ondemand-better-for-fluctuating-traffic"], None,
     "In DynamoDB, a new app's traffic is unknown and spiky. Which capacity mode?", "On-demand capacity mode.")
card("cannot", "core", sec("Read and write units"), ["dynamodb-index-read-consistency-gsi-vs-lsi"], "dynamodb-trap-gsi-strong-read",
     "In DynamoDB, can a global secondary index serve a strongly consistent read?", "No. GSI queries support eventual consistency only.")
card("cannot", "core", sec("A Query reads"), ["dynamodb-scan-filter-same-read-capacity"], "dynamodb-trap-filter-saves-capacity",
     "In DynamoDB, does a filter expression lower the read capacity of a Scan?", "No. The Scan consumes the same amount of read capacity.")
card("decide", "core", sec("Conditional writes"), ["dynamodb-transactwriteitems-all-or-nothing"], "dynamodb-trap-batch-write-is-atomic",
     "In DynamoDB, two items must change together or not at all. Which API?", "TransactWriteItems.")
card("cannot", "core", sec("In a global table"), ["dynamodb-faq-global-tables-no-failover-needed"], "dynamodb-trap-global-table-primary-region",
     "In a DynamoDB global table, does a Region outage need a database failover?", "No. A global table has no primary Region.")
# extended (18)
card("cannot", "extended", sec("Secondary indexes"), ["dynamodb-index-online-operations-gsi-vs-lsi"], "dynamodb-trap-lsi-added-later",
     "In DynamoDB, can you add a local secondary index to an existing table?", "No. Add a global secondary index instead.")
card("differ", "extended", sec("DynamoDB Streams"), ["dynamodb-streams-vs-kds-retention"], "dynamodb-trap-stream-keeps-changes",
     "DynamoDB Streams or Kinesis Data Streams for DynamoDB: which keeps records up to 1 year?", "Kinesis Data Streams for DynamoDB.")
card("cannot", "extended", sec("Time to Live"), ["dynamodb-ttl-deletes-within-days-no-wcu"], "dynamodb-trap-ttl-deletes-on-time",
     "In DynamoDB, does TTL delete an item at the moment it expires?", "No. Within a few days of their expiration time.")
card("cannot", "extended", sec("DAX answers"), ["dax-passes-through-strong-reads-and-transactions"], "dynamodb-trap-dax-speeds-every-read",
     "In DAX, are strongly consistent reads cached?", "No. DAX passes them to DynamoDB.")
card("cannot", "extended", sec("Every restore"), ["dynamodb-restore-cannot-overwrite-existing-table"], "dynamodb-trap-restore-in-place",
     "In DynamoDB, can a restore overwrite the existing table?", "No. Every restore creates a new table.")
card("cannot", "extended", sec("On-demand mode"), ["dynamodb-on-demand-previous-peak-double"], "dynamodb-trap-on-demand-absorbs-any-spike",
     "In DynamoDB on-demand mode, is any spike absorbed at once?", "No. Up to double the previous peak; pre-warm for more.")
card("cannot", "extended", sec("Provisioned mode"), ["dynamodb-throttling-with-autoscaling-possible"], "dynamodb-trap-auto-scaling-prevents-throttling",
     "In DynamoDB, does auto scaling prevent throttling in a sudden spike?", "No. It does not respond instantly.")
card("decide", "extended", sec("A hash of the partition key"), ["dynamodb-write-sharding-random-suffix"], "dynamodb-trap-spare-capacity-no-throttle",
     "In DynamoDB, one key gets most writes and is throttled. What do you change?", "The key: add a random suffix to spread the writes.")
card("decide", "extended", sec("DAX answers"), ["dax-api-compatible-minimal-changes", "dax-eventually-consistent-microsecond-latency"], None,
     "In DynamoDB, repeated reads need microsecond latency with minimal code change. What do you add?", "DAX, the DynamoDB-compatible in-memory cache.")
card("differ", "extended", sec("DAX answers"), ["dax-vs-elasticache-complex-queries"], None,
     "DAX or ElastiCache: which one caches lists, sets and hashes for many data sources?", "ElastiCache.")
card("decide", "extended", sec("IAM controls access"), ["dynamodb-faq-gateway-endpoint-no-igw-nat"], None,
     "In DynamoDB, private subnets must reach a table without a NAT device. What do you add?", "A gateway endpoint for DynamoDB.")
card("differ", "extended", sec("IAM controls access"), ["dynamodb-faq-gateway-endpoint-limits-use-privatelink"], None,
     "In DynamoDB, which endpoint serves on-premises servers: gateway or interface?", "An interface endpoint (AWS PrivateLink).")
card("decide", "extended", sec("Time to Live"), ["dynamodb-table-class-standard-ia-lower-storage-cost"], None,
     "In DynamoDB, storage is most of a table's bill, and old items are rarely read. Which table class?", "DynamoDB Standard-IA.")
card("decide", "extended", sec("Every restore"), ["dynamodb-aws-backup-vault-lock-worm", "dynamodb-aws-backup-copy-multiple-accounts-regions"], None,
     "In DynamoDB, backups must survive deletion by an admin and exist in another account. What do you use?", "AWS Backup with Vault Lock and cross-account copies.")
card("differ", "extended", sec("In a global table"), ["dynamodb-gt-mrec-default-last-writer-wins"], None,
     "In a DynamoDB global table with default settings, which write wins a conflict?", "The last writer wins.")
card("decide", "extended", sec("IAM controls access"), ["dynamodb-leadingkeys-condition-key-partition-key"], None,
     "In DynamoDB, users may read only items whose partition key is their own ID. Which condition key?", "dynamodb:LeadingKeys.")
card("cannot", "extended", sec("Conditional writes"), ["dynamodb-transaction-single-account-region"], None,
     "In DynamoDB, can one transaction write to tables in two Regions?", "No. One account and one Region only.")
card("cannot", "extended", sec("Conditional writes"), ["dynamodb-batchwriteitem-no-updateitem"], "dynamodb-trap-batch-write-is-atomic",
     "In DynamoDB, can BatchWriteItem run UpdateItem requests?", "No. BatchWriteItem does not support UpdateItem requests.")

BRIEF["card_plan"] = {
    "core": 14, "extended": 18, "number_cards_equal_a_list_rows": 8,
    "rule": ("Fronts and backs above are drafts for the card writer: one fact per card, an answer of at most 12 words, a display of a "
             "card fact for any number with a unit (400 KB, 3,000 read units per second, 1,000 write units per second, next 4 KB "
             "multiple, next 1 KB multiple, 1 MB per call, lifetime of 24 hours, up to 5 local secondary indexes, 10 GB, Up to 1 "
             "year, double the previous peak are the displays; write the back so that the display stands in it: c006's back holds "
             "'lifetime of 24 hours', c016's front 'up to 1 year' (case is ignored)), and the context named at the start of the "
             "front. No front holds a number with a unit that is not a display of a card fact. No absolute word without a fact of the "
             "card that supports it: c031 ('only') rests on dynamodb-transaction-single-account-region, c032 ('does not support') on "
             "dynamodb-batchwriteitem-no-updateitem. c017's back uses the display 'within a few days of their expiration time'; if "
             "it passes 12 words, write 'No. Within a few days of their expiration time.' (9 words)."),
}

BRIEF["diagrams"] = [
    {"id": "dynamodb-hero", "kind": "sequence",
     "placement": "1-fast.md#in-one-breath (behind 'Predict the picture: when an application writes one item, where does DynamoDB store it, and when does it say the write is safe?')",
     "title": "One write: from the key to three Availability Zones",
     "claim": "A write lands in the partition that the key's hash picks, and DynamoDB copies it to three Availability Zones before it confirms the write.",
     "alt": ("A sequence with four participants: an application, DynamoDB, one partition, and its copies in three Availability Zones. "
             "The application sends a write with the item's key. DynamoDB hashes the partition key and picks the partition. The "
             "partition stores the item in three zones. DynamoDB returns success. A later read is eventually consistent unless it "
             "asks for a strong read."),
     "say": [
         "The application sends a write that holds the item's primary key.",
         "DynamoDB feeds the partition key value into an internal hash function, which determines the partition.",
         "DynamoDB synchronously replicates the item across three Availability Zones.",
         "When the write returns HTTP 200 (OK), it has been durably persisted.",
         "Eventually consistent is the default for a later read; a strongly consistent read returns the most up-to-date data.",
     ],
     "facts_for_steps": ["dynamodb-partition-key-hash-decides-partition", "dynamodb-faq-sync-replication-three-azs",
                         "dynamodb-successful-write-http-200-durable", "dynamodb-eventually-consistent-default", "dynamodb-consistentread-parameter"],
     "note": ("Size s. Participants: Application (users or a Lambda function icon), DynamoDB (dynamodb icon, label 'DynamoDB'), "
              "Partition (dynamodb icon or generic box, label 'Partition'), Three AZs (label 'Copies in three AZs'). Messages: 1 "
              "application to DynamoDB 'write item'; 2 DynamoDB aside 'hash the key'; 3 DynamoDB to partition 'store'; 4 partition "
              "to three AZs 'copy'; 5 DynamoDB to application, dashed, 'success'; 6 application to DynamoDB 'read'. Labels at most 4 "
              "words, no digits. In the Markdown steps, step 2 links [internal hash function] and [determines the partition] "
              "(dynamodb-partition-key-hash-decides-partition); step 3 links [three Availability Zones] "
              "(dynamodb-faq-sync-replication-three-azs) (the word 'synchronously' is the fact's own claim); step 4 links [durably "
              "persisted] (dynamodb-successful-write-http-200-durable); step 5 links [Eventually consistent is the default] "
              "(dynamodb-eventually-consistent-default) and [most up-to-date data] (dynamodb-consistentread-parameter). If a step "
              "changes to fit its link, change say here and in the spec together (L703). The caption equals the claim; it holds "
              "'three' (a number word) and no absolute word, so it needs no link; if the claims reviewer asks for one, link [three "
              "Availability Zones] (dynamodb-faq-sync-replication-three-azs) in the caption.")},
    {"id": "dynamodb-hot-partition", "kind": "compare",
     "placement": "2-deep.md#a-hash-of-the-partition-key-picks-the-partition-so-hot-keys-throttle (after the table)",
     "title": "Many key values or one hot key",
     "claim": "Requests spread over many key values use every partition, but requests to one hot key meet the ceiling of one partition.",
     "alt": ("Two panels. Many key values: requests with different keys go to three partitions in even shares, and all are served. "
             "One hot key: almost every request carries the same key and goes to one partition, which throttles, while the other two "
             "partitions are nearly idle."),
     "panels": [
         "Many key values: nodes 'Requests', 'Partition A', 'Partition B', 'Partition C'; edges requests to each partition 'some keys'",
         "One hot key: nodes 'Requests', 'Partition A' (emph: throttled), 'Partition B', 'Partition C'; edges requests to partition A 'hot key' (thick), dashed edges to B and C 'few'",
     ],
     "say": [],
     "facts_for_caption": ["dynamodb-partition-key-hash-decides-partition", "dynamodb-hot-partitions-throttle-while-others-underutilized"],
     "note": ("Size m, two panels, at most 6 nodes and 7 edges per panel; 'Requests' in the same cell in both panels. No numbers in "
              "labels. The caption equals the claim; 'ceiling' is plain text. If the claims reviewer asks for a link, add [throttling "
              "while other operations may remain underutilized] (dynamodb-hot-partitions-throttle-while-others-underutilized) in a "
              "sentence after the figure, not in the caption.")},
    {"id": "dynamodb-dax-read", "kind": "sequence",
     "placement": "2-deep.md#dax-answers-repeated-eventually-consistent-reads-from-memory-in-microseconds (after the trace)",
     "title": "A read and a write through DAX",
     "claim": "DAX answers cache hits from memory and sends misses, writes and strongly consistent reads on to the table.",
     "alt": ("A sequence with three participants: an application with the DAX client, the DAX cluster and the DynamoDB table. A read "
             "that DAX has cached returns from DAX. A read that DAX has not cached goes on to the table, and DAX keeps the item. A "
             "write goes to the table first, then to DAX. A strongly consistent read goes through DAX to the table."),
     "say": [
         "The DAX client directs all of your application's DynamoDB API requests to the DAX cluster.",
         "On a cache hit, DAX returns the item with microsecond latency.",
         "On a cache miss, DAX sends the request to DynamoDB and keeps the returned item in its item cache.",
         "A write is first written to the DynamoDB table and then to DAX.",
         "DAX passes strongly consistent read requests to DynamoDB and does not cache the results.",
     ],
     "facts_for_steps": ["dax-client-routes-requests-to-cluster", "dax-eventually-consistent-microsecond-latency",
                         "dax-cache-miss-reads-dynamodb-and-fills-cache", "dax-write-through-both-table-and-dax",
                         "dax-passes-through-strong-reads-and-transactions"],
     "note": ("Size s. Participants: Application (users icon, label 'App with DAX client'), DAX (dax icon), Table (dynamodb icon). "
              "Messages: 1 app to DAX 'read'; 2 DAX to app 'hit'; 3 DAX to table 'miss: read'; 4 table to DAX, dashed, 'item'; 5 "
              "app to DAX 'write'; 6 DAX to table 'write first'; 7 app to DAX 'strong read'; 8 DAX to table 'pass through'. At most "
              "10 messages. Step links: 1 [directs all of your application's DynamoDB API requests] "
              "(dax-client-routes-requests-to-cluster); 2 [with microsecond latency] (dax-eventually-consistent-microsecond-latency); "
              "3 [DAX sends the request to DynamoDB] (dax-cache-miss-reads-dynamodb-and-fills-cache) and [item cache] "
              "(dax-item-cache-getitem-batchgetitem); 4 [first written to the DynamoDB "
              "table] (dax-write-through-both-table-and-dax); 5 [DAX passes strongly consistent read requests to DynamoDB] and [it "
              "does not cache the results] (dax-passes-through-strong-reads-and-transactions).")},
    {"id": "dynamodb-before", "kind": "arch", "placement": "2-deep.md#decision-record (after Context)",
     "title": "Callvale before: job status in PostgreSQL",
     "claim": "Every pipeline step updates the call's status row in PostgreSQL, and at peak the updates queue behind locks and connections.",
     "alt": ("Before: the S3 upload event starts the start-job function; the pipeline functions for converting, transcribing and "
             "saving results each update the call's status row in the PostgreSQL database through RDS Proxy; the dashboard reads the "
             "same table."),
     "say": [
         "An upload to Amazon S3 starts the start-job function.",
         "Each pipeline step updates the status row of the call in PostgreSQL.",
         "The dashboard reads the same status rows to list a customer's jobs.",
         "At peak, row locks and connections slow every update.",
     ],
     "facts_for_steps": [],
     "note": ("Story picture (pipeline state P2 of STARTUP.md B1). Steps are story, not AWS rules: no fact link, no number, no "
              "absolute word. At most 12 nodes: 'Uploads' (S3 icon), 'start-job' (lambda-function icon), 'Pipeline functions' "
              "(lambda icon), 'RDS Proxy' (rds-proxy icon), 'PostgreSQL' (rds icon, emph: the bottleneck), 'Dashboard'. Leave out the "
              "queues, topic and conversion workers (not part of this decision). Keep spec say and Markdown steps equal (L703).")},
    {"id": "dynamodb-after", "kind": "arch", "placement": "2-deep.md#decision-record (after Decision)",
     "title": "Callvale after: the jobs table in DynamoDB",
     "claim": "The pipeline steps read and write each job by call ID in the jobs table, and the dashboard lists a customer's jobs through the index by-customer.",
     "alt": ("After: the S3 upload event starts the start-job function, which starts the state machine call-pipeline. Each step reads "
             "and writes the job item by call ID in the DynamoDB table jobs. The dashboard queries the global secondary index "
             "by-customer. Time to live removes old job items."),
     "say": [
         "The start-job function starts the state machine call-pipeline for each upload.",
         "Each step reads and writes the job item by its call ID in the jobs table.",
         "The dashboard lists one customer's jobs through the global secondary index by-customer.",
         "Time to live deletes old job items without consuming any write throughput.",
     ],
     "facts_for_steps": ["dynamodb-faq-ttl-no-write-throughput"],
     "note": ("At most 12 nodes. Same cells as dynamodb-before where possible: 'Uploads' (S3), 'start-job' (lambda-function), "
              "'call-pipeline' (step-functions icon) replaces 'Pipeline functions', 'jobs table' (dynamodb icon, emph) replaces "
              "RDS Proxy and PostgreSQL, 'by-customer index' as a label on the dashboard edge or a small node, 'Dashboard'. Step 4 "
              "links [without consuming any write throughput] (dynamodb-faq-ttl-no-write-throughput); steps 1 to 3 are story with no "
              "AWS rule. No second Region (stage 4). Keep spec say and Markdown steps equal (L703).")},
]

BRIEF["fact_requests"] = [
    {"id": "fr-0101", "service": "dynamodb", "where": "1-fast.md#changed-recently",
     "question": ("Set changed.date 2025-06-30 and a changed.was on dynamodb-change-mrsc-global-tables-ga-2025-06 (before multi-Region "
                  "strong consistency became generally available on June 30, 2025, global tables offered only multi-Region eventual "
                  "consistency), from a saved AWS page that states the old behaviour or the date of the change, with a display of the "
                  "old value (for example 'eventually consistent'); close as unfillable if no saved page states it."),
     "effect": ("without it, the MRSC entry of Changed recently is not written (changed_recently.pending), and the GSI-keys entry "
                "stays. Filed 2026-10-14 by brief-28.")},
]

BRIEF["notes_for_orchestrator"] = [
    "Only verified facts are named: chapter-28 dynamodb- and dax- facts from _build/work/28-dynamodb/fact-cards.md (707 verified, 2026-10-13), plus verified facts of chapters 10 (vpc-), 11 (vpc-endpoints-), 18 (lambda-), 26 (rds-), 29 (elasticache-), 31 (eventbridge-) and 02 (well-architected-). build_brief.py checked every fact id and every display-and-id pair against data/facts/*.jsonl before stage end; the generator and its six data parts stay in _build/work/28-dynamodb/ (brief_part_a.py to brief_part_f.py) for later edits.",
    "Terms (orchestrator note): term_requests holds 35 complete bank entries for every new term the chapter defines in bold, plus 2 term_amendments (time-to-live, point-in-time-recovery). The terms agent adds them to data/terms.json and appends their ids to brief.json terms, so that no writer needs a needs-term marker. The words table (8 rows) uses six of them.",
    "Traps: 13 (the U5 cap): 5 in the fast list, 8 as Exam trap callouts in 2-deep.md. 2-deep.md callouts: 8 Exam trap + 2 Try it + 1 Startup example = 11 of 12. Subsections without an Exam trap: 1, 2, 9, 11, 13, 14 (9 and 14 carry the two Spot the bug prompts). 14 of 22 slots are built on a trap; all 13 trap ids are cited by a slot.",
    "Twin pairs: three strict pairs (q01/q07 capacity mode, q04/q10 GSI or LSI, q12/q16 global table or cross-Region backups), so that the chapter still ships two whole pairs after one rejection. Each pair has identical options and qualifiers and turns on stable facts.",
    "Changed recently: three examinable fast entries with changed records (2024-11-01 on-demand prices, 2025-08-12 capacity-mode switches, 2025-11-19 multi-attribute GSI keys). The 2025-06-30 MRSC entry waits for fact request fr-0101, filed by brief-28 (open requests block the counts gate, B09, until closed as filled or unfillable). Not-examinable changes (2026-08-19 streams ABAC, 2026-09 MRSC Regions, 2026-10-01 filtered export) have no changed record, so no B-list entry is planned.",
    "Volatile facts: 75 chapter-28 facts are volatile (frequently-changing or changed within 24 months), among them every MRSC fact, the capacity-mode switch limit, the 2024 price change, the PITR period, pricing examples, multi-account global tables, vector search and zero-ETL. build_brief.py lists them in question_plan.volatile_facts_never_in_explanation_or_correct_why (Q112). Prose and cards may link them where a plan names them; every key rests on the stable key_facts of its slot.",
    "Demand gaps kept out of the prose (brief.v0 partial items): PartiQL does not add joins, but no saved page says so (d016): no sentence about joins and PartiQL; the 50% and 67% price cuts of 2024 are not verified figures (d043): the Changed recently entry states the change without percentages; Database Savings Plans figures are volatile and chapter 41 owns them (d046); the TTL stream record fields userIdentity and principalId are not verified (d067): the book says 'service deletions'; export does not consume read capacity is not verified (d076): no sentence; the console's default global tables version (d087): no sentence; table names unique per account and Region (d095): no sentence; restore of settings other than tags (d104): only tags are named; DAX data transfer charges (d123): no sentence; FIPS endpoints (d132): no sentence; vector search release date (d183): no sentence, vector search is outside this chapter's plan.",
    "Source disagreements kept out of one sentence: global table replication 'typically within a second or less' (guide) against 'usually within one to two seconds' (product page): the brief links the guide only; Database Savings Plans 'up to 18%' for DynamoDB (FAQ) against 'up to 35%' plan-wide: no sentence; DAX hit rate 'exceed 90%' (best) against '85-95 percent' (typical): reference only.",
    "Displays to avoid in links (F2): dax-can-subvert-dynamodb-iam-policies (its display holds bold markup); dynamodb-faq-on-demand-for-unpredictable 'on-demand is better suited to customers' reads oddly mid-sentence (use dynamodb-ondemand-better-for-fluctuating-traffic); dynamodb-scan-isolate-from-critical-table holds straight quotes ('not taking \"mission-critical\" traffic'): copy exactly. Displays with backticks (`ConsistentRead`, `LeadingKeys`, `KEYS_ONLY`, `NEW_AND_OLD_IMAGES`, `Scan`, `Query`, `LastEvaluatedKey`, `ConditionalCheckFailedException`, `BatchWriteItem`) are copied exactly.",
    "STARTUP check: the decision record keeps the three options, the qualifier 'least operational overhead', the choice (one jobs table, on-demand, one global secondary index) and the trade-off of data/startup.json word for word; TTL after 90 days and the index by-customer come from the JSON adds and note; DAX is weighed at stage 4 and not used (not in this record). uses_numbers: job_updates_per_call (12), peak_uploads_per_minute (40 at stage 2), night_uploads_per_minute (2), job_record_ttl_days (90), launch_day_incident (900 connections, 47 minutes). Pipeline states P2 before and P3 after (shared with chapter 32).",
    "Spoken numbers: speak items write numbers as words from the fact cards' say forms (three thousand read units, one thousand write units per second; double the previous peak; three Availability Zones; a few seconds).",
    "Tasks: all three cost about $0 (one Look; two Tries on an on-demand table with a few small items and fewer than 20 requests). No price fact is used in a cost line; if a writer wants a dollar amount above 0, T109 needs a price fact (only example prices exist, all volatile). dynamodb-t02 is the pass-route Try (Query against Scan, trap filter-saves-capacity).",
    "Section count for stage end: 9 sections of 1-fast.md + the How it works H2 + 14 subsections + Numbers + Decision record + FAQ = 27 brief sections; the optional real-world box is not a brief section.",
]
