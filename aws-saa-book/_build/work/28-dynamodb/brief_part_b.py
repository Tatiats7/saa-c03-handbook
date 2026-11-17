# brief-28, part B: How-it-works subsections 1 to 7.


def sub(heading, minutes, words, bullets, facts, plan, route=None):
    d = {"file": "2-deep.md", "section": anchor(heading), "heading": heading, "bullets": bullets, "facts": facts,
         "status": "write", "minutes": minutes, "words_all_in": words}
    if route:
        d["route"] = route
    d["plan"] = plan
    BRIEF["sections"].append(d)


# 1 ---------------------------------------------------------------------------------------------
sub("A table stores items, and each item needs only its primary key", 3, 200, ["3.3.K8", "3.3.S4", "3.3.S2"],
    ["dynamodb-faq-managed-offload", "dynamodb-no-maintenance-windows", "dynamodb-intro-little-operational-overhead",
     "dynamodb-names-case-sensitive-utf8", "dynamodb-faq-blob-use-s3-pointers", "dynamodb-compress-large-attributes",
     "dynamodb-number-precision", "dynamodb-nested-attribute-depth", "dynamodb-sets-unique-unordered",
     "dynamodb-primary-key-attribute-types", "dynamodb-partition-key-length", "dynamodb-sort-key-length"],
    {
        "problem": ("A relational table fixes its columns before the first row, and a new kind of record needs a schema change. "
                    "DynamoDB fixes only the key, so each item can carry its own attributes."),
        "trace": [
            "**Create a table with a key.** When you create a table, [you must specify the primary key] (dynamodb-primary-key-required-at-create), and [no two items can have the same key] (dynamodb-primary-key-required-at-create).",
            "**Choose one of two key shapes.** A primary key is a [single-attribute partition key or a composite partition-sort key] (dynamodb-faq-primary-key-two-forms).",
            "**Leave the rest open.** [Other than the primary key attributes] (dynamodb-schemaless-except-primary-key), you [don't have to define any attributes] (dynamodb-schemaless-except-primary-key); the key is the [only required attribute for items in a table] (dynamodb-faq-primary-key-only-required-attribute).",
            "**Store flat or nested data.** DynamoDB supports [both key-value and document data models] (dynamodb-key-value-and-document); [The document types are list and map] (dynamodb-document-types-list-map-nesting).",
            "**Keep each item small.** An item can hold at most [400 KB] (dynamodb-item-size-max), attribute names included; a table has [no practical limit on a table's size] (dynamodb-table-size-no-practical-limit).",
        ],
        "table": ("What you define and what DynamoDB runs (columns: Part | You choose | DynamoDB does): Table | its name, primary key "
                  "and one of [on-demand or provisioned capacity mode] (dynamodb-must-choose-capacity-mode) | the servers: you "
                  "[don't need to provision any servers] (dynamodb-serverless-no-servers); Item | any attributes besides the key | "
                  "stores and replicates it; Large file | a pointer in the item: [store the Amazon S3 object identifier] "
                  "(dynamodb-large-items-store-in-s3) | nothing: the file lives in Amazon S3. One link per fact per cell; cells at "
                  "most 15 words."),
        "why": ("Why so little schema? DynamoDB is built for access patterns you know in advance: you [design your schema "
                "specifically] (dynamodb-design-schema-for-access-patterns) so that the most common queries are [as fast and as "
                "inexpensive as possible] (dynamodb-design-schema-for-access-patterns)."),
        "exam_signal": ("\"key-value lookups, session state or shopping carts at any scale\" points to DynamoDB, which AWS lists "
                        "for [session stores or shopping carts] (dynamodb-decision-guide-key-value-session-store) with "
                        "[single-digit millisecond performance at any scale] (dynamodb-decision-guide-key-value-session-store)."),
        "exam_trap": None,
        "body_extras": ("Only if words remain, one sentence: DynamoDB [doesn't support a JOIN operator] (dynamodb-no-join-operator), "
                        "and there are [no versions (major, minor, or patch)] (dynamodb-no-maintenance-windows) to upgrade. "
                        "Reference only, no sentence: attribute data types ([number, string, binary, Boolean, and null] "
                        "(dynamodb-data-type-categories); sets [must be of the same type] (dynamodb-set-types-same-type-elements) and "
                        "[cannot be an empty set] (dynamodb-empty-set-not-allowed); DynamoDB [does not natively support] "
                        "(dynamodb-no-native-date-type) a date and time type; nesting [up to 32 levels deep] "
                        "(dynamodb-document-types-list-map-nesting)); key length limits (dynamodb-partition-key-length, "
                        "dynamodb-sort-key-length); the BLOB advice of the FAQ (dynamodb-faq-blob-use-s3-pointers) is FAQ item 3."),
        "say_it": "The short answer is: a table needs only a key, and each item can differ. The thing to watch is the size of one item.",
        "stop_and_answer": ("A shop stores products. Some products have 10 attributes and some have 40. Must every item in the "
                            "table have the same attributes? Answer: no; [other than the primary key attributes] "
                            "(dynamodb-schemaless-except-primary-key), you [don't have to define any attributes] "
                            "(dynamodb-schemaless-except-primary-key), so each item can have its own set. 10 and 40 are example "
                            "values in the prompt."),
    })

# 2 ---------------------------------------------------------------------------------------------
sub("A hash of the partition key picks the partition, so hot keys throttle", 4, 220, ["3.3.K3", "3.3.K1", "2.2.S2", "3.3.K4"],
    ["dynamodb-data-on-ssd-multi-az", "dynamodb-three-az-replication-built-in", "dynamodb-partition-changes-transparent",
     "dynamodb-faq-auto-scale-and-partition", "dynamodb-design-uniform-activity-all-keys", "dynamodb-throttling-key-range-hot-partitions",
     "dynamodb-adaptive-capacity-both-modes", "dynamodb-adaptive-capacity-instant", "dynamodb-burst-capacity-handles-spikes",
     "dynamodb-burst-capacity-used-for-maintenance", "dynamodb-write-sharding-calculated-suffix", "dynamodb-item-collection-splits-without-lsi",
     "dynamodb-partition-20kb-example", "dax-single-item-reads-beyond-3000-rcu", "dynamodb-occasional-throttling-normal"],
    {
        "problem": ("One server cannot hold every item of a large table, so DynamoDB splits each table into partitions. The "
                    "partition key you choose decides how evenly the work is spread over them."),
        "trace": [
            "**Hash the key.** DynamoDB feeds the partition key value into an [internal hash function] (dynamodb-partition-key-hash-decides-partition); the output [determines the partition] (dynamodb-partition-key-hash-decides-partition) that stores the item.",
            "**Keep related items together.** Items with the [same partition key value] (dynamodb-composite-key-same-pk-sorted-together) are stored together, [in sorted order by sort key value] (dynamodb-composite-key-same-pk-sorted-together); this group is [called an item collection] (dynamodb-item-collection-range-retrieval).",
            "**Copy each write into three zones.** A partition is storage [backed by solid state drives (SSDs)] (dynamodb-faq-partition-storage-ssd-multi-az), and DynamoDB synchronously replicates data across [three Availability Zones] (dynamodb-faq-sync-replication-three-azs).",
            "**Give each partition a ceiling.** Every partition delivers at most [3,000 read units per second] (dynamodb-partition-max-throughput) and [1,000 write units per second] (dynamodb-partition-max-throughput).",
            "**Throttle the hot key alone.** Traffic that one key concentrates creates [\"hot\" partitions that result in throttling] (dynamodb-hot-partitions-cause-throttling), with [throttling while other operations may remain underutilized] (dynamodb-hot-partitions-throttle-while-others-underutilized).",
        ],
        "table": ("Key design and result (columns: Partition key | Spread | Result): a key with a [small number of partition key "
                  "values] (dynamodb-few-partition-keys-spread-writes), such as a status | most requests share a few values | hot "
                  "partitions and throttling; a key with a [large number of distinct values] "
                  "(dynamodb-uniform-distribution-distinct-keys), such as a customer ID | requests spread out | even use of "
                  "capacity; a hot key plus a random suffix (write sharding) | writes [randomize the writes across the larger "
                  "space] (dynamodb-write-sharding-random-suffix) | reads must [query the items for all the suffixes] "
                  "(dynamodb-write-sharding-read-merge) and merge them. Never write that one partition key value always stays in "
                  "one partition: without an LSI, DynamoDB can [automatically split your item collection] "
                  "(dynamodb-item-collection-splits-without-lsi). One item is in one partition."),
        "why": ("Why throttle one partition and not the whole table? Each partition is its own unit of storage and throughput, and "
                "partition management is [handled entirely by DynamoDB] (dynamodb-partitions-managed-by-dynamodb), so the key is "
                "the lever you control."),
        "exam_signal": ("\"throttling on a few keys while the table has spare capacity\" points to a hot partition: choose a key "
                        "with a [large number of distinct values] (dynamodb-uniform-distribution-distinct-keys), or add write "
                        "sharding."),
        "exam_trap": None,
        "diagram": "dynamodb-hot-partition (after the table; caption and alt in diagrams)",
        "go_deeper": ("Go deeper: adaptive and burst capacity (at most 70 words). Adaptive capacity is [enabled automatically for "
                      "every DynamoDB table] (dynamodb-adaptive-capacity-automatic-no-cost) and "
                      "[rebalances your partitions] (dynamodb-adaptive-capacity-isolates-hot-items) so that hot items [don't reside "
                      "on the same partition] (dynamodb-adaptive-capacity-isolates-hot-items), as long as traffic stays under the "
                      "[total provisioned capacity or the partition maximum capacity] (dynamodb-adaptive-capacity-hot-partitions-unthrottled). "
                      "Burst capacity keeps [up to five minutes (300 seconds)] (dynamodb-burst-capacity-retention) of unused "
                      "capacity; these details [might change in the future] (dynamodb-burst-capacity-may-change-not-guaranteed)."),
        "body_extras": ("Reference only, no sentence: data on SSDs in multiple AZs (dynamodb-data-on-ssd-multi-az); the 99.99% SLA "
                        "of one Region belongs to subsection 13 (dynamodb-three-az-replication-built-in); the throttling reason "
                        "[`KeyRangeThroughputExceeded`] (dynamodb-throttling-key-range-hot-partitions); occasional throttling is "
                        "normal (dynamodb-occasional-throttling-normal); the 20 KB worked example (dynamodb-partition-20kb-example)."),
        "say_it": "The short answer is: the partition key spreads the work over partitions. The thing to watch is one key that gets most of the traffic.",
        "stop_and_answer": ("A ticket app keeps the seats left for one concert in a single item, and every purchase updates that "
                            "item. The table has far more write capacity than the purchase rate. When sales open, can purchases be "
                            "throttled? Answer: yes; the item is stored in one partition, the one the hash [determines the "
                            "partition] (dynamodb-partition-key-hash-decides-partition) for, and a partition delivers at most "
                            "[1,000 write units per second] (dynamodb-partition-max-throughput); spare capacity elsewhere does not "
                            "help. Spread the count over several items ([add a random number] "
                            "(dynamodb-write-sharding-random-suffix))."),
    }, route="pass")

# 3 ---------------------------------------------------------------------------------------------
sub("Read and write units depend on item size and read consistency", 4, 215, ["4.3.K5", "3.3.K4", "3.3.S2"],
    ["dynamodb-rcu-definition", "dynamodb-wcu-definition", "dynamodb-read-capacity-formula", "dynamodb-eventual-read-default-half",
     "dynamodb-getitem-round-10kb-example", "dynamodb-pricing-on-demand-10kb-read-example", "dynamodb-pricing-on-demand-10kb-write-example",
     "dynamodb-transactional-units-double", "dynamodb-gsi-and-streams-reads-eventual", "dynamodb-item-size-list-map-overhead"],
    {
        "problem": ("DynamoDB measures capacity in units, not in requests. A large item costs more units than a small one, and a "
                    "fresher read costs more than a default read."),
        "trace": [
            "**Count writes in 1 KB steps.** One write unit is one write for an item [up to 1 KB] (dynamodb-write-unit-1kb); a write rounds up to the [next 1 KB multiple] (dynamodb-write-rounding-1kb).",
            "**Count reads in 4 KB steps.** A strongly consistent read of an item up to 4 KB needs [one read unit] (dynamodb-read-unit-strong-4kb); a read rounds up to the [next 4 KB multiple] (dynamodb-read-rounding-4kb).",
            "**Read eventually by default.** [Eventually consistent is the default] (dynamodb-eventually-consistent-default) and needs [one-half read unit] (dynamodb-read-unit-eventual-4kb), but it [might not reflect the results] (dynamodb-eventually-consistent-may-lag) of a write that just finished.",
            "**Ask for the latest data.** Set the [optional `ConsistentRead` parameter] (dynamodb-consistentread-parameter) to true to get the [most up-to-date data] (dynamodb-consistentread-parameter).",
            "**Pay double for transactions.** A transactional read needs [two read units] (dynamodb-read-unit-transactional-4kb); a transactional write of 1 KB needs [2 write units] (dynamodb-write-unit-1kb).",
        ],
        "table": ("Units for one 10 KB item (columns: Request | Units): eventually consistent read | [1.5 RCUs] "
                  "(dynamodb-pricing-provisioned-10kb-example); strongly consistent read | [3 RCUs] "
                  "(dynamodb-pricing-provisioned-10kb-example); transactional read | [6 RCUs] (dynamodb-pricing-provisioned-10kb-example); "
                  "standard write | [10 WCUs] (dynamodb-pricing-provisioned-10kb-write-example); transactional write | [20 WCUs] "
                  "(dynamodb-pricing-provisioned-10kb-write-example). '10 KB' in the table title is an example value; the trace "
                  "spells out RCU and WCU first."),
        "why": ("Why does a strong read cost twice as much? It consumes [twice as many database resources] "
                "(dynamodb-strong-read-twice-eventual) as an eventually consistent read."),
        "exam_signal": ("\"must always read the most recent write\" points to strongly consistent reads, which return the [most "
                        "up-to-date data] (dynamodb-consistentread-parameter); \"lowest read cost, stale data acceptable\" points "
                        "to the default eventually consistent reads, at [half the cost of strongly consistent reads] "
                        "(dynamodb-eventually-consistent-half-cost)."),
        "exam_trap": "dynamodb-trap-gsi-strong-read",
        "exam_trap_text": ("> **Exam trap:** A strong read does not work everywhere. Strongly consistent reads are [only supported "
                           "on tables and local secondary indexes] (dynamodb-strong-reads-only-tables-and-lsi); a global secondary "
                           "index or a stream returns eventually consistent data. <!-- trap: dynamodb-trap-gsi-strong-read -->"),
        "body_extras": ("Only if words remain, one sentence: on-demand counts the same sizes in request units: one RRU is [one "
                        "strongly consistent read operation per second] (dynamodb-rru-definition) for an item up to 4 KB, and one "
                        "WRU is [one write operation per second, for an item up to 1 KB] (dynamodb-wru-definition). Reference "
                        "only: sizes are binary, [1 KB = 1024 bytes] (dynamodb-size-units-binary); list and map overhead "
                        "(dynamodb-item-size-list-map-overhead)."),
        "say_it": "The short answer is: item size and consistency decide the units. The thing to watch is that a strong read costs twice as much.",
        "stop_and_answer": ("An item is 2 KB. How many write units does one write use, and how many read units does one strongly "
                            "consistent read use? Answer: [2 write units] (dynamodb-write-2kb-example) for the write; the read size "
                            "rounds up to the [next 4 KB multiple] (dynamodb-read-rounding-4kb), so the read needs [one read unit] "
                            "(dynamodb-read-unit-strong-4kb). Do not write '2 KB' in the reveal: it is the prompt's example value, "
                            "and the reveal is strict text."),
    })

# 4 ---------------------------------------------------------------------------------------------
sub("On-demand mode bills each request and needs no capacity plan", 4, 220, ["4.3.S3", "4.3.K5", "3.3.K4"],
    ["dynamodb-faq-on-demand-billing-units", "dynamodb-faq-on-demand-scale-to-zero-pay", "dynamodb-on-demand-optional-max-throughput",
     "dynamodb-ondemand-max-throughput-best-effort", "dynamodb-ondemand-max-throughput-smallest", "dynamodb-warm-throughput-cannot-decrease",
     "dynamodb-no-account-quota-on-demand", "dynamodb-table-throughput-quota-on-demand", "dynamodb-dg-serverless-databases-pay-for-use",
     "dynamodb-new-ondemand-table-4000-writes-12000-reads"],
    {
        "problem": ("A new product does not know its traffic yet. Capacity bought in advance is wasted at night and too small at "
                    "the peak."),
        "trace": [
            "**Choose a mode for each table.** When you create a table, you [must select] (dynamodb-must-choose-capacity-mode) either [on-demand or provisioned capacity mode] (dynamodb-must-choose-capacity-mode); [On-demand mode is the default] (dynamodb-on-demand-default-recommended).",
            "**Set no numbers.** For on-demand tables you [don't need to specify] (dynamodb-on-demand-no-capacity-planning) the reads and writes that you expect.",
            "**Pay per request.** On-demand is [billed per read or write request] (dynamodb-ondemand-billed-per-request-zero-traffic-free); an idle table [scales down to zero] (dynamodb-on-demand-scales-to-zero), and [there are no cold starts] (dynamodb-on-demand-scales-to-zero).",
            "**Absorb peaks, up to a point.** On-demand [instantly accommodates up to double the previous peak] (dynamodb-on-demand-previous-peak-double); [throttling can occur] (dynamodb-on-demand-throttle-if-double-within-30-min) if you [exceed double your previous peak within 30 minutes] (dynamodb-on-demand-throttle-if-double-within-30-min).",
            "**Keep the same service.** On-demand tables give the [same single-digit millisecond latency] (dynamodb-on-demand-same-latency-sla-security) and the same SLA as provisioned tables.",
        ],
        "table": ("On-demand settings (columns: Setting | Effect): nothing set | capacity follows the traffic; a maximum throughput "
                  "| the table's [maximum read or write (or both) throughput] (dynamodb-on-demand-optional-max-throughput) caps it, "
                  "to [keep table-level usage and costs bounded] (dynamodb-on-demand-optional-max-throughput); a higher warm "
                  "throughput | the table [can instantaneously support] (dynamodb-warm-throughput-definition) more at once, and "
                  "for pre-warming [you will be charged for those requests] (dynamodb-warm-throughput-default-free-prewarm-charged). "
                  "Do not use the volatile fact dynamodb-ondemand-max-throughput-throttles-above-limit here."),
        "why": ("Why is on-demand the default? It removes capacity planning: you create a table [without worrying about capacity "
                "planning] (dynamodb-ondemand-fits-no-capacity-planning), and AWS calls it the [default and recommended throughput "
                "option] (dynamodb-on-demand-default-recommended) for most workloads."),
        "exam_signal": ("\"unpredictable traffic\", \"a new application\" or \"pay only for what is used\" points to on-demand: "
                        "[On-demand capacity mode is the better choice] (dynamodb-ondemand-better-for-fluctuating-traffic) for "
                        "traffic with spikes."),
        "exam_trap": "dynamodb-trap-on-demand-absorbs-any-spike",
        "exam_trap_text": ("> **Exam trap:** On-demand does not absorb every spike at once. It [instantly accommodates up to "
                           "double the previous peak] (dynamodb-on-demand-previous-peak-double); before a launch far above any "
                           "earlier peak, raise the warm throughput ([pre-warming] (dynamodb-warm-throughput-prewarm-for-peak-events)). "
                           "<!-- trap: dynamodb-trap-on-demand-absorbs-any-spike -->"),
        "startup_example": ("At most 30 words, numbers from uses_numbers only: 'Callvale's job writes swing from 2 calls a minute "
                            "at night to 40 at peak. In on-demand mode, nobody sets capacity for either.' (story; the claim about "
                            "on-demand is already linked in the trace)."),
        "body_extras": ("Only if words remain, one sentence: '[No account-level read and write throughput quotas] "
                        "(dynamodb-no-account-quota-on-demand) apply to on-demand tables, but each table has a default quota of "
                        "[40,000 read request units] (dynamodb-table-throughput-quota-on-demand).' Reference only, no "
                        "sentence: the initial throughput of a new on-demand table (dynamodb-new-ondemand-table-4000-writes-12000-reads, "
                        "volatile); the best-effort note on the maximum (dynamodb-ondemand-max-throughput-best-effort)."),
        "say_it": "The short answer is: on-demand charges per request and plans capacity for you. The thing to watch is a peak far above any earlier peak.",
        "stop_and_answer": ("A table in on-demand mode gets no traffic from Friday night to Monday morning. What does the weekend "
                            "cost for throughput, and is the first request on Monday slow? Answer: nothing for throughput: on a table "
                            "with no traffic [you are not charged for any throughput] "
                            "(dynamodb-ondemand-billed-per-request-zero-traffic-free); and [there are no cold starts] "
                            "(dynamodb-on-demand-scales-to-zero). Storage is still billed."),
    }, route="pass")

# 5 ---------------------------------------------------------------------------------------------
sub("Provisioned mode bills the capacity you set, and auto scaling follows within minutes", 4, 220, ["4.3.K5", "3.3.K4", "4.3.S3"],
    ["dynamodb-autoscaling-policy-min-max", "dynamodb-autoscaling-target-utilization", "dynamodb-autoscaling-target-range",
     "dynamodb-autoscaling-scale-down-15-points", "dynamodb-autoscaling-console-enabled-by-default", "dynamodb-autoscaling-new-gsi-not-enabled",
     "dynamodb-autoscaling-not-deleted-with-table", "dynamodb-provisioned-no-rapid-increase", "dynamodb-provisioned-target-utilization-cost-lever",
     "dynamodb-rightsize-under-20-percent-over-provisioned", "dynamodb-rightsize-under-provisioned-over-80-percent",
     "dynamodb-switch-to-ondemand-takes-minutes", "dynamodb-sdk-exponential-backoff", "dynamodb-exponential-backoff-concept",
     "dynamodb-reserved-capacity-quota", "dynamodb-min-throughput-provisioned", "dynamodb-account-throughput-quota-provisioned",
     "dynamodb-pricing-savings-no-combine-reserved", "dynamodb-faq-database-savings-plans-18-percent"],
    {
        "problem": ("A steady workload that runs at a high rate all day pays more per request than it needs to. Provisioned mode "
                    "trades flexibility for a fixed, predictable bill."),
        "trace": [
            "**Set reads and writes per second.** You [must specify the number of reads and writes] (dynamodb-provisioned-must-specify-reads-writes) per second that the application needs.",
            "**Pay for what you set.** You pay for the [hourly read and write capacity you have provisioned] (dynamodb-provisioned-billing-basis), used or not.",
            "**Throttle above the setting.** [Provisioned capacity throttling] (dynamodb-provisioned-throttling-when-exceeded) happens when the [consumption rate exceeds the read or write capacity] (dynamodb-provisioned-throttling-when-exceeded); the AWS SDKs [automatically retry requests that receive this exception] (dynamodb-sdk-retries-throttled-requests).",
            "**Let auto scaling move the setting.** DynamoDB auto scaling uses the [AWS Application Auto Scaling service] (dynamodb-autoscaling-uses-application-auto-scaling) and a target utilization; AWS recommends [70%] (dynamodb-autoscaling-target-recommended).",
            "**Expect minutes, not seconds.** Scaling starts after the target is breached for [two consecutive minutes] (dynamodb-autoscaling-two-consecutive-minutes), and it [takes several minutes to update the provisioned capacity] (dynamodb-autoscaling-update-takes-minutes-throttle).",
        ],
        "table": ("How often you can change it (columns: Change | Allowed): raise capacity | [as often as necessary] "
                  "(dynamodb-capacity-increase-unlimited-frequency); lower capacity | [4 available decreases] "
                  "(dynamodb-capacity-decreases-per-day) at the start of each day, up to [27 times] (dynamodb-capacity-decreases-per-day) "
                  "in a full day; switch to on-demand | [up to four times in a 24-hour rolling window] "
                  "(dynamodb-capacity-mode-switch-four-per-24h); switch back to provisioned | [at any time] "
                  "(dynamodb-capacity-mode-switch-four-per-24h). The switch fact is volatile (changed 2025-08-12): it can stand in "
                  "this table, never in a question key."),
        "why": ("Why choose it? For [steady workloads with predictable growth] (dynamodb-provisioned-fits-steady-forecastable), "
                "provisioned capacity gives [cost predictability] (dynamodb-provisioned-cost-predictability), and reserved capacity "
                "lowers the rate: [up to 54% off standard rates for a one-year term] (dynamodb-reserved-capacity-terms-and-discount)."),
        "exam_signal": ("\"steady, predictable traffic\" with \"MOST cost-effective\" points to provisioned capacity with auto "
                        "scaling, made for [consistent or predictable traffic] (dynamodb-faq-provisioned-for-predictable); add "
                        "reserved capacity for a long, steady base."),
        "exam_trap": "dynamodb-trap-auto-scaling-prevents-throttling",
        "exam_trap_text": ("> **Exam trap:** Auto scaling does not prevent throttling in a sudden spike. [Throttling can occur "
                           "regardless] (dynamodb-throttling-with-autoscaling-possible) of auto scaling, because it [does not "
                           "respond instantly] (dynamodb-throttling-with-autoscaling-possible). "
                           "<!-- trap: dynamodb-trap-auto-scaling-prevents-throttling -->"),
        "go_deeper": ("Go deeper: reserved capacity and the 35% rule (at most 70 words). Reserved capacity is bought in [100 WCUs or "
                      "100 RCUs] (dynamodb-reserved-capacity-increment) allocations; you [can't sell, cancel, or transfer] "
                      "(dynamodb-reserved-capacity-no-transfer) it, and it is [not available for tables using the DynamoDB "
                      "Standard-IA] (dynamodb-reserved-capacity-not-for-ia-on-demand) class [or on-demand capacity mode] "
                      "(dynamodb-reserved-capacity-not-for-ia-on-demand). A rule of thumb: on-demand costs less when average "
                      "utilization is [below 35%] (dynamodb-ondemand-cheaper-below-35-percent-utilization)."),
        "body_extras": ("Reference only, no sentence unless words remain: the target range [between 20 and 90 percent] "
                        "(dynamodb-autoscaling-target-range); target utilization as [the primary means of cost optimization] "
                        "(dynamodb-provisioned-target-utilization-cost-lever); a new GSI on an existing table starts without auto "
                        "scaling (dynamodb-autoscaling-new-gsi-not-enabled); scaling policies are [not automatically deleted with "
                        "it] (dynamodb-autoscaling-not-deleted-with-table) when the table is deleted; the account quota of "
                        "[80,000 read capacity units] (dynamodb-account-throughput-quota-provisioned); Database Savings Plans "
                        "(dynamodb-faq-database-savings-plans-18-percent, volatile; chapter 41 owns discounts): no sentence."),
        "say_it": "The short answer is: provisioned mode bills the capacity you set, used or not. The thing to watch is auto scaling, which reacts in minutes.",
        "stop_and_answer": ("A provisioned table with auto scaling serves a flash sale. Traffic jumps to five times the normal rate "
                            "within ten seconds. What do clients see in the first minutes? Answer: throttled requests: auto scaling "
                            "waits for [two consecutive minutes] (dynamodb-autoscaling-two-consecutive-minutes) and then [takes "
                            "several minutes to update the provisioned capacity] (dynamodb-autoscaling-update-takes-minutes-throttle); "
                            "the SDKs [automatically retry requests that receive this exception] "
                            "(dynamodb-sdk-retries-throttled-requests). For spikes like this, on-demand mode fits better."),
    })

# 6 ---------------------------------------------------------------------------------------------
sub("A Query reads one partition key, but a Scan reads every item", 4, 215, ["3.3.K3", "3.3.S2", "3.3.K4"],
    ["dynamodb-query-descending-scanindexforward", "dynamodb-query-filter-no-key-attributes", "dynamodb-query-lastevaluatedkey-end",
     "dynamodb-scan-result-1mb", "dynamodb-scan-filter-any-attribute", "dynamodb-scan-limit-before-filter",
     "dynamodb-scan-eventually-consistent-default", "dynamodb-scan-spike-throttles-other-requests",
     "dynamodb-read-capacity-by-items-read-not-returned", "dynamodb-batchget-limits", "dynamodb-batchwrite-limits",
     "dynamodb-partiql-structured-semistructured-nested", "dynamodb-partiql-same-performance-as-data-plane", "dynamodb-expression-max-length",
     "dynamodb-expression-max-operators"],
    {
        "problem": ("A read that walks through the whole table gets slower and costlier as the table grows. DynamoDB gives a cheap "
                    "read for keys you know and an expensive one for everything else."),
        "trace": [
            "**Name one partition key.** A Query must give the partition key and [a single value for that attribute] (dynamodb-query-partition-key-equality-sort-key-optional), [as an equality condition] (dynamodb-query-partition-key-equality-only).",
            "**Narrow with the sort key.** You can [optionally provide a second condition] (dynamodb-query-optional-sort-key-condition) on the sort key with [`begins_with`, `between`, `>`, `<`] (dynamodb-query-sort-key-range-operators); items come back in [ascending order by sort key] (dynamodb-query-ascending-order-default).",
            "**Scan reads everything.** A Scan [reads every item in a table] (dynamodb-scan-reads-every-item) or index, and [the `Scan` operation slows] (dynamodb-scan-slows-as-table-grows) as the table grows.",
            "**Read page by page.** A Query or a Scan returns at most [1 MB per call] (dynamodb-query-result-1mb); you continue with `LastEvaluatedKey`, and you are done only when [`LastEvaluatedKey` is empty] (dynamodb-query-lastevaluatedkey-not-end).",
            "**Filter after reading.** A filter expression is [applied after a `Scan` finishes] (dynamodb-scan-filter-same-read-capacity), so the Scan [consumes the same amount of read capacity] (dynamodb-scan-filter-same-read-capacity).",
        ],
        "table": ("What each read operation reads (columns: Operation | Reads | Use it for): GetItem | one item by its full key | one "
                  "known item; Query | one item collection, or part of it | items that share a partition key; Scan | it [always "
                  "scans the entire table or secondary index] (dynamodb-scan-less-efficient-than-query) | rare full reads and small "
                  "tables."),
        "why": ("Why is a Query so narrow? A NoSQL table is [queried efficiently in a limited number of ways] "
                "(dynamodb-nosql-queries-efficient-in-limited-ways); outside them, [queries can be expensive and slow] "
                "(dynamodb-nosql-queries-efficient-in-limited-ways)."),
        "exam_signal": ("\"a Scan with a filter uses too much read capacity\" points to a design in which the application can [use "
                        "`Query` instead of `Scan`] (dynamodb-use-query-instead-of-scan), often through a secondary index."),
        "exam_trap": "dynamodb-trap-filter-saves-capacity",
        "exam_trap_text": ("> **Exam trap:** A filter does not lower the bill of a Query either. A Query also [consumes the same "
                           "amount of read capacity] (dynamodb-query-filter-same-read-capacity) with or without a filter expression. "
                           "<!-- trap: dynamodb-trap-filter-saves-capacity -->"),
        "try_it": "dynamodb-t02 (Try it callout, one line, in this subsection: 'Compare a Query and a Scan with consumed capacity shown' in 3-do.md)",
        "go_deeper": ("Go deeper: big scans without hurting the application (at most 70 words). A parallel scan is [much faster than "
                      "a sequential one] (dynamodb-parallel-scan-faster-for-large-tables), but it can [consume all of your table's "
                      "provisioned read capacity] (dynamodb-parallel-scan-heavy-demand). Lower the impact by [setting a smaller page "
                      "size] (dynamodb-scan-reduce-page-size), or run scans on a table that is [not taking \"mission-critical\" "
                      "traffic] (dynamodb-scan-isolate-from-critical-table). For a full copy, export to Amazon S3 (subsection 12)."),
        "body_extras": ("Reference only, no sentence: a projection or filter does not change Scan capacity "
                        "(dynamodb-read-capacity-by-items-read-not-returned); `Limit` applies [prior to filter expression evaluation] "
                        "(dynamodb-scan-limit-before-filter); BatchGetItem and BatchWriteItem limits (dynamodb-batchget-limits, "
                        "dynamodb-batchwrite-limits); PartiQL gives [SQL-compatible query access] "
                        "(dynamodb-partiql-structured-semistructured-nested) but no joins (no fact says it adds none: no sentence "
                        "about joins and PartiQL); expression limits (dynamodb-expression-max-length, dynamodb-expression-max-operators)."),
        "say_it": "The short answer is: a Query reads one key's items, and a Scan reads them all. The thing to watch is a filter, which hides items you still pay for.",
        "stop_and_answer": ("A table has the partition key `customer_id` and the sort key `order_date`. The application needs one "
                            "customer's orders from March. Which operation, with which conditions? Answer: a Query with "
                            "`customer_id` [as an equality condition] (dynamodb-query-partition-key-equality-only) and a `between` "
                            "condition on `order_date`, one of the range operators [`begins_with`, `between`, `>`, `<`] "
                            "(dynamodb-query-sort-key-range-operators); no Scan."),
    })

# 7 ---------------------------------------------------------------------------------------------
sub("Secondary indexes give the same items a second key to query", 5, 220, ["3.3.S2", "3.3.K3", "3.3.K4"],
    ["dynamodb-index-limits-20-gsi-5-lsi", "dynamodb-index-comparison-key-schema", "dynamodb-index-comparison-projected-attributes",
     "dynamodb-index-projects-key-attributes", "dynamodb-projection-keys-always-projected", "dynamodb-projection-all-largest",
     "dynamodb-projected-attributes-max", "dynamodb-gsi-key-values-not-unique", "dynamodb-gsi-key-attribute-types",
     "dynamodb-gsi-read-with-query-scan-only", "dynamodb-lsi-read-with-query-scan-only", "dynamodb-gsi-inherits-capacity-mode",
     "dynamodb-gsi-own-provisioned-throughput", "dynamodb-gsi-propagation-fraction-of-second", "dynamodb-gsi-replica-for-read-isolation",
     "dynamodb-gsi-same-table-class-as-base", "dynamodb-gsi-sparse-by-default", "dynamodb-sparse-index-definition",
     "dynamodb-sparse-gsi-lower-write-throughput", "dynamodb-gsi-creation-can-throttle-base-table", "dynamodb-gsi-insufficient-write-throttles-table",
     "dynamodb-gsi-throttle-base-table-write-reason", "dynamodb-gsi-one-per-updatetable", "dynamodb-gsi-delete-with-updatetable",
     "dynamodb-lsi-query-fetches-unprojected-attributes", "dynamodb-lsi-collection-limit-exception", "dynamodb-lsi-item-collection-max",
     "dynamodb-lsi-item-size-400kb-limit", "dynamodb-lsi-shares-table-provisioned-throughput", "dynamodb-lsi-sort-key-not-unique",
     "dynamodb-lsi-sort-key-one-scalar-attribute", "dynamodb-faq-gsi-primary-key-attributes"],
    {
        "problem": ("A table answers fast only for its own key. A new question, such as 'all open orders' or 'one customer's "
                    "orders by amount', needs another key."),
        "trace": [
            "**Copy items under a new key.** You can [retrieve data from the index using a `Query`] (dynamodb-gsi-queried-like-a-table), and [DynamoDB maintains indexes automatically] (dynamodb-indexes-maintained-automatically) when items change.",
            "**Global: any key, any time.** A GSI's [index key schema can be different] (dynamodb-gsi-key-schema-can-differ), it lets you [query over the entire table, across all partitions] (dynamodb-index-queries-span-table-gsi-vs-single-partition-lsi), and you can [add a new global secondary index] (dynamodb-index-online-operations-gsi-vs-lsi) to an existing table.",
            "**Global copies lag.** GSIs are [updated asynchronously, using an eventually consistent model] (dynamodb-gsi-updated-asynchronously), and their queries [support eventual consistency only] (dynamodb-index-read-consistency-gsi-vs-lsi).",
            "**Local: same partition key, another sort key.** An LSI has the [same partition key as the base table] (dynamodb-lsi-same-partition-key) and [a different sort key] (dynamodb-lsi-same-partition-key); it is [created when the table is created] (dynamodb-lsi-created-with-table) and allows [either eventually consistent or strongly consistent reads] (dynamodb-lsi-strongly-consistent-allowed).",
            "**Project what you will read.** [global secondary index queries cannot fetch attributes] (dynamodb-gsi-query-cannot-fetch-from-table) from the table, so project them; the [`KEYS_ONLY` option] (dynamodb-projection-keys-only-smallest) gives the [smallest possible secondary index] (dynamodb-projection-keys-only-smallest).",
        ],
        "table": ("Capacity and size (columns: Index | Capacity | Size): GSI | [its own provisioned throughput capacity] "
                  "(dynamodb-autoscaling-supports-gsi-own-capacity) | [no size restrictions for global secondary indexes] "
                  "(dynamodb-index-lsi-size-limit-per-partition-key); LSI | it uses the table's: LSIs [consume capacity from the "
                  "base table] (dynamodb-rightsize-lsi-uses-base-table-capacity) | each item collection [10 GB or less] "
                  "(dynamodb-index-lsi-size-limit-per-partition-key). The GSI-or-LSI decision table is in 1-fast.md; this table "
                  "adds capacity and size only."),
        "why": ("Why two kinds? An LSI keeps each item collection in one partition, which allows strong reads but caps the collection "
                "at [10 GB] (dynamodb-lsi-collection-one-partition); a GSI is [stored separately from the data] "
                "(dynamodb-gsi-data-stored-separately) of the table, so it grows freely but lags."),
        "exam_signal": ("\"query on an attribute that is not the key\" points to a GSI; DynamoDB queries nonkey attributes with "
                        "[global secondary indexes and local secondary indexes] (dynamodb-faq-query-nonkey-via-gsi-lsi), and while "
                        "a GSI is added, [the table continues to be available] (dynamodb-gsi-add-to-existing-table)."),
        "exam_trap": "dynamodb-trap-lsi-added-later",
        "exam_trap_text": ("> **Exam trap:** A table that already exists cannot get a new LSI. You [cannot add a local secondary "
                           "index] (dynamodb-index-online-operations-gsi-vs-lsi) to an existing table; add a GSI instead. "
                           "<!-- trap: dynamodb-trap-lsi-added-later -->"),
        "go_deeper": ("Go deeper: sparse indexes and back-pressure (at most 70 words). A GSI [only tracks data items] "
                      "(dynamodb-gsi-only-items-with-key-attributes) whose [key attributes actually exist] "
                      "(dynamodb-gsi-only-items-with-key-attributes), so an attribute that only open orders carry makes a sparse "
                      "index; it is [faster and less expensive to query that index] (dynamodb-sparse-index-faster-cheaper-than-scan) "
                      "than to scan. If a GSI lacks write capacity, DynamoDB [throttles writes to the base table] "
                      "(dynamodb-gsi-back-pressure-definition)."),
        "body_extras": ("Reference only, no sentence unless words remain: index limits [up to 20 global secondary indexes] and [up "
                        "to 5 local secondary indexes] (dynamodb-index-limits-20-gsi-5-lsi) are in Numbers; a GSI's write capacity "
                        "should be [equal or greater than the write capacity] (dynamodb-gsi-write-capacity-equal-or-greater) of the "
                        "table; an LSI query can fetch unprojected attributes at a cost "
                        "(dynamodb-lsi-query-fetches-unprojected-attributes); multi-attribute GSI keys "
                        "(dynamodb-faq-gsi-primary-key-attributes, volatile): Changed recently only."),
        "say_it": "The short answer is: an index gives your items a second key. The thing to watch is that a global index lags behind the table.",
        "stop_and_answer": ("An `orders` table has the partition key `order_id` and holds a year of data. Support staff need all "
                            "orders of one email address, newest first. What do you add? Answer: a GSI with the partition key "
                            "`email` and the sort key `order_date`, because its [index key schema can be different] "
                            "(dynamodb-gsi-key-schema-can-differ); query it in descending order ([request descending order] "
                            "(dynamodb-query-ascending-order-default)). An LSI cannot help: it keeps the table's partition key."),
    }, route="pass")
