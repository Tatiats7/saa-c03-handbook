"""fix-28: write status and resolution into the three findings files of chapter 28.

Run once from the repo root: python3 -I aws-saa-book/_build/work/28-dynamodb/fix_28_apply.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent / "findings"

R = {
    # claims lens
    "claims-01": ("fixed", "fix-28: after the item fixes below (c003, c028, s01 kp5, s04 ten_second), tasks lint, speak lint and cards lint were clean, and tasks t01-t03, speak s01-s04 and cards c001-c032 were set to ready (set-status --by fix-28). sync 28 now prints 3-do.md, 4-say.md and the Look first task region in 1-fast.md."),
    "claims-02": ("fixed", "fix-28: dynamodb-q007 explanation only (stem, options and key byte-identical, same precedent as fix-18 lambda-q010): 'on-demand costs less when average utilization is [below 35%] or has quiet periods. This table runs near full use all day, so reserved capacity lowers the rate of the base load.' The word 'only' is gone; the quoted second sentence of the fact (quiet periods) is reflected."),
    "claims-03": ("fixed", "fix-28: 'None:' replaced by 'No reserved capacity: it is not for Standard-IA tables [or on-demand capacity mode]', which the linked fact supports. Database Savings Plans: verified facts exist (dynamodb-faq-database-savings-plans-18-percent, dynamodb-database-savings-plans-cover-dynamodb), but no saved quote says whether on-demand throughput is covered (the FAQ says 'your Amazon DynamoDB usage'), so no Savings Plans claim was placed in the on-demand column."),
    "claims-04": ("fixed", "fix-28: 2-deep provisioned subsection now reads 'it costs less at average use [below 35%], and often above when quiet periods mix with peaks', the condition of the fact's second quoted sentence."),
    "claims-05": ("fixed", "fix-28: Stop and answer rewritten: 'jumps fivefold and stays high for ten minutes. What do clients see?' Answer: 'Throttled requests, after [burst capacity] is spent and before auto scaling catches up' (verified fact dynamodb-burst-capacity-handles-spikes)."),
    "claims-06": ("fixed", "fix-28: hero spec claim and the 1-fast caption now say 'A write lands in the partition that the key's hash picks, and DynamoDB replicates it across three Availability Zones.' (no 'before it confirms'); diagram build dynamodb-hero re-rendered the SVG. Step 4 keeps the HTTP 200 durable fact. speak s04 ten_second: 'DynamoDB replicates each record across three Availability Zones, and a confirmed write is durable.'"),
    "claims-07": ("fixed", "fix-28: TTL step 3 is now 'Delete later, with no write units' and adds 'A global table is [charged for the replicated delete] in other Regions' (verified fact dynamodb-mrec-ttl-replicated-delete-charged). Say it and the Stop and answer say 'without write units' instead of 'for free'. The 1-fast signals row keeps 'no extra cost' only as a quoted stem phrase; its Because cell names write throughput."),
    "claims-08": ("fixed", "fix-28: step 2 now reads 'with `dynamodb:LeadingKeys` and the `ForAllValues` modifier, a condition on [the partition key]'. This also teaches card c030."),
    "claims-09": ("fixed", "fix-28: step 1 now says 'IAM policies decide each request. It also [supports resource-based policies for tables and streams]' (verified fact dynamodb-faq-resource-policies-tables-streams)."),
    "claims-10": ("fixed", "fix-28: the unsupported sentence ('row locks per client', 'one server sets the ceiling') is gone. New text: 'In a relational database, each client holds a connection, and updates to one row wait for its lock. [DynamoDB uses an HTTP API] with no open connection, and a key hash spreads items over partitions.' The hash mechanism is linked in hero step 2."),
    "claims-11": ("fixed", "fix-28: answer now 'Vault Lock in compliance mode: that lock [cannot be altered or deleted by any user]' (verified fact backup-vault-lock-compliance-immutable-by-anyone)."),
    "claims-12": ("fixed", "fix-28: card c028 back 'AWS Backup Vault Lock in compliance mode.'; extra names governance mode as removable with IAM permissions; facts backup-vault-lock-compliance-immutable-by-anyone and backup-vault-lock-governance-lock-removable-with-iam added."),
    "claims-13": ("fixed", "fix-28: card c003 extra 'A small item still costs a full block: one unit for a strong read, half a unit for an eventually consistent read.'; facts dynamodb-read-unit-strong-4kb and dynamodb-read-unit-eventual-4kb added."),
    "claims-14": ("fixed", "fix-28: B-list row now 'PITR period per table, since [January 7, 2025]', so the change date is shown. A full Changed recently entry is not added: the change fact records no old value (no `changed.was`, and no saved quote states a fixed 35-day period), and the section already holds its maximum of 4 entries."),
    "claims-15": ("fixed", "fix-28: dynamodb-q022 option b why only (stem, options, key unchanged): 'so every write from Europe and Asia still travels to the primary cluster's Region.'"),
    "claims-16": ("fixed", "fix-28: decision now says 'Time to live expires each job record 90 days after the call.' (expiry, not deletion); the TTL subsection and fast trap teach the few-days delay."),
    "claims-17": ("rejected", "fix-28: not changed. Both facts are verified and say different things: the DR guide's RPO of seconds (data lost) and the latest restorable time five minutes back. A reconciling clause needs a per-second restore fact and 2-deep sits at its blocking 4,500-word ceiling. Logged for the next revision."),
    "claims-18": ("fixed", "fix-28: speak s01 kp5 now 'a one-year or three-year commitment'."),
    "claims-19": ("fixed", "fix-28: Stop and answer now adds 'or with enhanced fan-out [20 simultaneous consumers per shard]'. The 1 year retention stays labelled 'up to 1 year' (a maximum), as the fact's display says."),
    "claims-20": ("fixed", "fix-28: now 'An item that rounds up to [12 KB], three blocks of [4 KB], costs:'. The 10 KB value itself has no display in the canon (L304), so the rounding is shown through the 12 KB and 4 KB displays of the same fact."),
    "claims-21": ("fixed", "fix-28: the Aurora and RDS columns are merged into 'Aurora or RDS'; the cost cell is softened to 'Database instances or serverless capacity, plus storage' (no number or absolute word)."),
    "claims-22": ("fixed", "fix-28: 'for most workloads' added after the on-demand default link; Look first now says 'Quotas apply on a [per-Region basis] unless AWS says otherwise.'"),
    "claims-23": ("fixed", "fix-28: MRSC cell now '[Exactly three Regions]: three replicas, or [two replicas and one witness]'. Checked against the newer verified fact dynamodb-change-mrsc-more-regions-2026-09: it widens which Regions qualify (any three of 15), not the count, and it is after 2026-07-15 (not examinable yet), so it is not taught."),
    # reader lens
    "reader-01": ("fixed", "fix-28: same fix as claims-01: all tasks, speak items and cards set to ready after clean item lints; sync 28 printed 3-do.md, 4-say.md and the task region."),
    "reader-02": ("fixed", "fix-28: four deep Stop-and-answer items now need a step the heading does not give: item size (photos past 400 KB go to S3), the hot key fix (what do you change: shard the key), DAX with reads that must show the latest score (strong reads pass through), and the global table (what must the team do: route users; no database failover). Fast Check 2 kept: the Check section re-tests the compare tables by design and its reveal also carries Predict 2."),
    "reader-03": ("fixed", "fix-28: caption softened as claims-06; the spec claim changed and the SVG was rebuilt. Hero step 5 keeps the eventually consistent default with its fact, so the caption no longer implies that every copy exists before success."),
    "reader-04": ("fixed", "fix-28: rewritten as cause and effect with the Lambda fact (see claims-10); 'row locks per client' removed."),
    "reader-05": ("fixed", "fix-28: 'An item that rounds up to [12 KB], three blocks of [4 KB], costs:' (see claims-20)."),
    "reader-06": ("fixed", "fix-28: step 3 now names it first: 'Auto scaling aims at a [target utilization], the share of capacity in use. It acts when use stays above it for [two consecutive minutes]...' (verified fact dynamodb-autoscaling-target-utilization)."),
    "reader-07": ("removed", "fix-28: the dangling SDK retry sentence ('this exception') was removed; the new answer (claims-05) names throttled requests and burst capacity and needs no exception name."),
    "reader-08": ("fixed", "fix-28: the trap now defines it: 'The **warm throughput** is what a table [can instantaneously support]' (dynamodb-warm-throughput-definition), then pre-warming, with the change date [November 13, 2024]."),
    "reader-09": ("fixed", "fix-28: one sentence added: 'In multi-Region strong consistency (MRSC), writes are [synchronously replicated to at least one other Region]: strong reads [always return the latest version of an item]' (dynamodb-gt-mrsc-synchronous-latest-reads); the table names the witness option."),
    "reader-10": ("fixed", "fix-28: 'its recovery time objective (RTO), the time the application is down, is an [RTO of zero]'."),
    "reader-11": ("fixed", "fix-28: each rejected option now has its reason ('updates still wait on row locks'; ElastiCache is an [ephemeral cache for frequently accessed data], not a job record). The two numbered lists stay: L703 requires the four spec steps under each figure (removing them failed lint). The section stays above 280 words (W201, warning)."),
    "reader-12": ("fixed", "fix-28: now 'Choose an answer that is right under old and new prices.'"),
    "reader-13": ("fixed", "fix-28: the Why line now gives the cause and adaptive capacity: 'Each item lives in one partition. Adaptive capacity [rebalances your partitions] to split hot items, but one hot item still meets its ceiling.' The Stop and answer adds the 1,000 write units ceiling and the sharding fix."),
    "reader-14": ("fixed", "fix-28: Try line retitled to what the task shows: 'Watch a filter leave a Scan's units unchanged; compare ScannedCount with a Query.' The task itself (verified, ready) is unchanged."),
    "reader-15": ("rejected", "fix-28: kept. The cell must hold a display of dynamodb-reserved-capacity-not-for-ia-on-demand, and both displays name Standard-IA; the new signals row in the same file ('storage is most of the bill' -> the Standard-IA table class) explains the class, and the fast file is at 1,800 words."),
    "reader-16": ("fixed", "fix-28: Check 3 now says 'almost at the same time'."),
    "reader-17": ("fixed", "fix-28: Look first no longer promises 'list your tables'; it now matches the task (account and new-table quotas, in two Regions). The belief the task kills is a task-stage choice that passed its gate; the per-partition ceiling is not visible through describe-limits, so the task is not changed."),
    "reader-18": ("fixed", "fix-28: dynamodb-q012 option c why only: 'adds a replicated write request unit (rWRU) charge, [one rWRU per replica table] for every write'."),
    "reader-19": ("fixed", "fix-28: stem now 'for two weeks'; Why line now 'Your code's role carries its permissions, so no password is stored.'"),
    "reader-20": ("fixed", "fix-28: A-list cell now 'Ask for more with `LastEvaluatedKey`' (the fact's own wording)."),
    "reader-21": ("fixed", "fix-28: c030 taught in IAM step 2 (ForAllValues); c032 taught in the BatchWriteItem trap ('it [does not support] `UpdateItem` requests', dynamodb-batchwriteitem-no-updateitem); c024 taught by the new DAX/ElastiCache compare row 'Queries beyond key-value access?' ([ElastiCache (Redis OSS) supports advanced data structures])."),
    # exam lens
    "exam-01": ("fixed", "fix-28: same as claims-02 (q007 explanation edited without 'only'; key unchanged)."),
    "exam-02": ("fixed", "fix-28: same as claims-04; the deep sentence now carries the quiet-periods exception, which matches the 2024 price-cut note."),
    "exam-03": ("fixed", "fix-28: PrivateLink entry added to Changed recently (2024-03-19; Old: gateway endpoint for traffic from a VPC; Now: also [interface VPC endpoints and private IP addresses]; exam expects gateway in a VPC, interface from on premises), the 4th and last allowed entry. Warm throughput: the deep trap now dates it ('new on [November 13, 2024]'). PITR: B-list shows 'since [January 7, 2025]' (no old-value quote exists). MRSC: left out, its change fact is still unverified (fr-0101)."),
    "exam-04": ("fixed", "fix-28: the dynamodb-q001 record moved earlier in data/28-dynamodb/questions.json (before q009; content byte-identical). Printed order now: q001 is Question 6 and q007 Question 10, three questions between them; q004 (3) and q010 (9) also meet the rule."),
    "exam-05": ("rejected", "fix-28: not changed. The Twin line of q004 quotes the one deciding sentence, which carries both conditions (new table, strong reads); a one-phrase twin needs a new q010 stem, which resets a verified question (R5). Logged for the next revision."),
    "exam-06": ("fixed", "fix-28: dynamodb-q011 (core, edited-pass, bullets 3.3.S4 and 3.3.K8) set to ready and dynamodb-q003 (core, bullet 3.3.S2, still carried by q014 and q021) set to verified. q lint 28 --ship: ok, ready 18, multi 2, twin pairs intact."),
    "exam-07": ("fixed", "fix-28: the TTL subsection adds the other side: 'Its reads and writes cost more: Standard tables have [lower costs for reads and writes]'; a signals row added in 1-fast ('storage is most of the bill' -> Standard-IA table class; but not if heavy reads and writes)."),
    "exam-08": ("fixed", "fix-28: signals row added: 'private subnets, no NAT gateway' -> a gateway endpoint, [without requiring an internet gateway or NAT device]; but not if on premises: [you must use AWS PrivateLink]."),
    "exam-09": ("fixed", "fix-28: q022 option b why as claims-15; option a why now begins 'It keeps the slow writes:' instead of 'It works'. Explanation-only edits; stem, options and key unchanged."),
    "exam-10": ("fixed", "fix-28: two rows added to the DAX or ElastiCache table: 'What happens to a write?' (DAX: [first written to the DynamoDB table], then to DAX) and 'Queries beyond key-value access?' (ElastiCache: [ElastiCache (Redis OSS) supports advanced data structures]); the deciding question now uses the same words. Strong reads stay in the DAX signals row and the DAX trap."),
    "exam-11": ("fixed", "fix-28: Aurora and RDS merged into one 'Aurora or RDS' column (see claims-21); the Aurora versus RDS split stays in chapters 26 and 27."),
    "exam-12": ("rejected", "fix-28: not changed. Dropping the 'because' clause changes option text that the blind solvers saw, which resets a verified question (R5). Logged for the next revision of dynamodb-q020."),
    "exam-13": ("rejected", "fix-28: not added. 2-deep is at its blocking 4,500-word ceiling, and FREQUENCY.md does not list export to S3 among the top DynamoDB sub-topics. The facts (dynamodb-export-requires-pitr, dynamodb-export-full-and-incremental) stay available for the next revision."),
}

seen = set()
for name in ("claims.json", "reader.json", "exam.json"):
    path = HERE / name
    data = json.loads(path.read_text(encoding="utf-8"))
    for f in data["findings"]:
        if f["id"] in R:
            f["status"], f["resolution"] = R[f["id"]]
            seen.add(f["id"])
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

missing = sorted(set(R) - seen)
counts = {}
for s, _ in R.values():
    counts[s] = counts.get(s, 0) + 1
print("applied", len(seen), "missing", missing, counts)
