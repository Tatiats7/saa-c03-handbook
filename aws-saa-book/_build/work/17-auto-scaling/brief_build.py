"""Builds _build/work/17-auto-scaling/brief.json (brief-17, 2026-10-13).

Run: python3 aws-saa-book/_build/work/17-auto-scaling/brief_build.py
Every fact id named here is checked by brief_check.py against data/facts/*.jsonl.
"""
import json
import pathlib

OUT = pathlib.Path(__file__).with_name("brief.json")
A = "ec2-auto-scaling-"
AA = "aws-auto-scaling-"


def f(*names):
    """Expand short fact names: 'x' -> ec2-auto-scaling-x; 'aa:x' -> aws-auto-scaling-x; '=x' -> x as is."""
    out = []
    for n in names:
        if n.startswith("aa:"):
            out.append(AA + n[3:])
        elif n.startswith("="):
            out.append(n[1:])
        else:
            out.append(A + n)
    return out


D = "2-deep.md#"
S1 = "an-auto-scaling-group-holds-its-desired-capacity-between-a-minimum-and-maximum"
S2 = "a-launch-template-tells-the-group-what-to-launch-in-numbered-versions"
S3 = "the-group-spreads-instances-evenly-across-its-availability-zones"
S4 = "a-new-instance-joins-the-load-balancer-before-it-becomes-inservice"
S5 = "the-group-replaces-instances-that-fail-the-health-checks-you-turned-on"
S6 = "a-target-tracking-policy-keeps-one-metric-near-the-value-you-choose"
S7 = "step-scaling-follows-alarm-size-and-warmup-replaces-the-old-cooldown"
S8 = "scheduled-and-predictive-scaling-add-capacity-before-the-load-arrives"
S9 = "a-worker-group-scales-on-the-backlog-of-messages-per-instance"
S10 = "scale-in-removes-the-instance-that-the-termination-policy-picks"
S11 = "a-mixed-instances-group-adds-spot-capacity-on-top-of-an-on-demand-base"
S12 = "stopped-instances-belong-in-a-warm-pool-not-in-the-running-group"
S13 = "an-instance-refresh-replaces-running-instances-to-roll-out-a-new-version"
SVC = "2-services.md#aws-auto-scaling"

brief = {
    "chapter": "17",
    "angle": "follow one instance through its life in a group: the group holds a desired count between a minimum and a maximum (1), a launch template says what to launch (2), the group places instances evenly over Availability Zones (3), a new instance passes Pending, an optional launch hook and load balancer registration before InService (4), health checks decide which instances are replaced (5); then follow the number: a target tracking policy moves desired capacity (6), step and simple policies react to alarms, and warmup replaces cooldown (7), scheduled and predictive scaling act before the load (8), a worker group behind a queue scales on backlog per instance (9); then the way out: scale in picks and drains one instance (10); then cost and speed: Spot on top of an On-Demand base (11), stopped instances only in a warm pool, which is also why scaling up is not the answer (12); and change without patching: an instance refresh replaces every instance (13)",
    "brief_by": "brief-17",
    "written_at": "2026-10-13",
    "base": "No exemplar slice exists for Auto Scaling. Pattern: _build/style/exemplar/iam-*.md and vpc-2-deep-slice.md (house pattern U1: problem, numbered trace with bold step names, compressing table, one Why reason, Exam signal, Exam trap or Go deeper, Say it, Stop and answer) and _build/work/14-elb/brief.json (shape of this brief; chapter 14 is ready and is the closest neighbour). Link texts in the plans are displays copied from _build/work/17-auto-scaling/fact-cards.md (chapter facts) and fact-cards-neighbours.md, fact-cards-neighbours-2.md, fact-cards-neighbours-3.md, fact-cards-ec2.md (facts of chapters 02, 14 and 16); copy them exactly, in lowercase where they stand in mid-sentence (F2). A link text in brackets is followed by its fact id in parentheses.",
    "frozen": {
        "2-deep.md": "Nothing frozen. Write all 13 subsections from the plans below, in this order.",
        "items": "No exemplar items exist for Auto Scaling; write every item from the slots below.",
    },
    "budgets": {
        "rule": "lint.word_count counts every word of the file: reveals, Go deeper blocks, prompts, image alt text and captions included (code blocks and comments excluded). Auto Scaling is not an XL chapter: 2-deep.md 3,500 to 4,500 words; How it works 2,600 to 3,500 words.",
        "2-deep.md_total_min": 3500,
        "2-deep.md_total_max": 4500,
        "how_it_works_max": 3500,
        "how_it_works_plan": "13 subsections with the words_all_in of each plan (each a maximum; sum 3,060, counted with Exam signal, Exam trap, Try it, Startup example, Say it, Stop and answer and its reveal, and the alt and caption of a diagram embedded there) + 4 Go deeper blocks of at most 70 words each (280) + 2 Spot the bug prompts with reveals of about 55 words each (110) + the H2 intro line (about 30) = about 3,480 at most; aim 100 words lower. Body plus callouts without prompts and reveals stays at 150 words or more per subsection (subsection_words min) and at most 400.",
        "per_subsection_all_in": "230 to 255 words at most (see words_all_in of each plan); keep each Stop and answer with its reveal at about 45 words, so that the body and callouts keep 160 words or more. Depth that does not fit goes into the four Go deeper blocks named in devices.go_deeper, nowhere else. Spend the words on the trace, not on lists.",
        "go_deeper_words_max_this_chapter": 70,
        "numbers_max": 300,
        "decision_record_max": 280,
        "faq_max": 450,
        "go_deeper_file_max": 6,
        "go_deeper_planned": 4,
        "spot_the_bug_file_max": 2,
        "spot_the_bug_planned": 2,
        "callouts_max_2_deep": 12,
        "callouts_planned_2_deep": "11: Exam trap x8, Try it x2 (auto-scaling-t02, auto-scaling-t03), Startup example x1 (scheduled action); Exam signal, Exam heuristic, Say it and Changed recently do not count",
        "1-fast.md_total_max": 1800,
        "fast_section_budget_note": "The section maxima of the fast file add up to 1,900 words; the file cap is 1,800. Aim: Predict 110, Look first 50, In one breath 270, Words 170, Choose it or not 450, Signals and traps 360, Changed recently 120, Check 150, Recap 80 (about 1,760).",
        "fast_callouts_max": 6,
        "fast_callouts_planned": "2: Say it (one-breath) and Startup example; Changed recently entries do not count",
        "startup_example_words": "All Startup example callouts of the chapter hold at most 80 words together: the fast one carries the Problem (about 50 words), the one in 2-deep.md at most 25 words.",
        "2-services.md": "one card, 150 to 220 words (D15)",
        "realworld": "optional; write it only if 2-deep.md stays at or under 4,380 words without it; at most 90 words; see realworld below",
    },
    "sections": [],
    "traps": [],
}

S = brief["sections"]

# ---------------------------------------------------------------- 1-fast.md
S.append({
    "file": "1-fast.md", "section": "predict", "heading": "Predict", "bullets": [], "facts": [],
    "status": "write", "minutes": 2,
    "plan": """Three prompts, each ending with '?'. Predict 1 is the gist trap (<!-- gist-trap -->): 'An application behind a load balancer stops answering requests, but its instance keeps running. Does EC2 Auto Scaling replace the instance?' (common sense says yes; with the default settings the answer is no: the group ignores the load balancer's health checks until you turn them on). Predict 2: 'Traffic rises at 09:00 every weekday. Can the group have new instances ready before 09:00, or only after the traffic arrives?' Predict 3: 'Can you hibernate the instances of an Auto Scaling group at night to save cost?' Answers appear only in Check (U4). No term is defined in a prompt; no AWS number in a prompt.""",
})
S.append({
    "file": "1-fast.md", "section": "look-first", "heading": "Look first", "bullets": ["2.2.S4"],
    "facts": f("quota-groups-per-region", "termination-default-outdated-first", "termination-az-balance-first",
               "suspend-processes-purpose"),
    "status": "write", "minutes": 3, "task": "auto-scaling-t01",
    "plan": """One task region for auto-scaling-t01 (read-only, 3 minutes, $0): list the termination policies and the scaling processes that EC2 Auto Scaling offers, and read the account's group quota. At most 80 words and at most 2 sentences around the region.""",
})
S.append({
    "file": "1-fast.md", "section": "in-one-breath", "heading": "In one breath", "bullets": ["3.2.K4", "2.2.S4"],
    "facts": f("faq-definition", "faq-group-definition", "target-tracking-service-manages-alarms",
               "scaling-policy-adjusts-desired", "launch-in-az-with-fewest", "registers-with-lb-before-inservice",
               "unhealthy-terminated-replaced", "desired-capacity-maintained"),
    "status": "write", "minutes": 3,
    "plan": """Say it (one-breath definition, at most 25 words, linked): Amazon EC2 Auto Scaling is a [fully managed service] (ec2-auto-scaling-faq-definition) that launches and terminates EC2 instances to keep the right number running for the load. Then the bold field '**The problem it solves.**' in one or two sentences: one instance cannot follow a load that changes during the day, and nobody replaces it by hand at night. Then 'Predict the picture: when traffic rises, which part decides that the group needs another instance, and which part launches it?' with the hero auto-scaling-hero inside a reveal, its caption and its 5 numbered steps (text fixed in diagrams below; link the facts named in facts_for_steps). Then the Startup example callout with the Problem of data/startup.json chapter 17 word for word (about 50 words; at most 60 with the label). Total at most 280 words: keep the hero alt at about 45 words.""",
})
S.append({
    "file": "1-fast.md", "section": "words-that-go-together", "heading": "Words that go together", "bullets": [],
    "facts": [], "status": "write", "minutes": 2,
    "plan": "A words table of 8 rows, cell 1 spelled as the term field of data/terms.json (with the respelling where the bank has one), cell 2 one collocation of the bank with exactly one bold span. See words_table.",
})
S.append({
    "file": "1-fast.md", "section": "choose-it-or-not", "heading": "Choose it or not",
    "bullets": ["3.2.K4", "2.1.K6", "4.2.S2", "3.2.S2", "2.1.S2"],
    "facts": f("faq-use-ec2-vs-aws-auto-scaling", "aa:faq-application-auto-scaling-for-non-ec2",
               "aa:wa-ec2-auto-scaling-for-instances-application-auto-scaling-for-other-services",
               "aa:faq-definition", "aa:faq-creates-target-tracking-only", "aa:aas-policy-types",
               "aa:plans-prefer-native-predictive-policies", "vertical-resize-instance-type",
               "vertical-stop-required", "decision-guide-horizontal-for-fluctuating",
               "wa-stateless-scales-horizontally", "faq-group-size-bounded-by-ec2-quota",
               "target-tracking-service-manages-alarms", "scheduled-action-sets-capacities",
               "faq-predictive-ahead-of-demand", "scheduled-vs-dynamic-when-to-use",
               "predictive-long-initialization-fit", "target-tracking-scale-in-gradual",
               "predictive-does-not-scale-in", "predictive-needs-24-hours-of-data"),
    "status": "write", "minutes": 4,
    "plan": "Three compare tables (see compare_tables), at most 4 columns each, each followed by its bold **Deciding question:** line. At most 500 words (aim for 450). If the section runs over, cut the last row of the service table, never the method table.",
})
S.append({
    "file": "1-fast.md", "section": "signals-and-traps", "heading": "Signals and traps",
    "bullets": ["2.2.S4", "3.2.S2", "3.2.S1", "4.2.S2", "4.2.K9", "2.2.K7", "2.2.S2"],
    "facts": f("health-elb-check-must-be-turned-on", "faq-suspend-health-checks", "standby-no-lb-traffic",
               "scheduled-vs-dynamic-when-to-use", "wa-predictive-patterns-vs-scheduled-times",
               "faq-target-tracking-definition", "sqs-backlog-per-instance", "sqs-dynamic-scaling-when-load-varies",
               "warm-pool-definition", "warm-pool-unnecessary-cost", "spot-price-capacity-optimized-recommended",
               "=ec2-spot-not-suitable-stateful-inflexible", "instance-refresh-use-cases",
               "faq-codedeploy-cloudformation-for-changes", "termination-hook-extends-life",
               "lifecycle-hook-spot-two-minute-notice", "elb-health-checks-ignored-by-default",
               "lb-default-ec2-checks-only", "termination-az-balance-first", "termination-default-outdated-first",
               "termination-default-billing-hour-then-random", "cannot-hibernate-group-instance",
               "warm-pool-hibernated-ram", "faq-data-not-copied-to-new-instances", "faq-persist-data-off-instance",
               "faq-regional-spans-azs-not-regions"),
    "status": "write", "minutes": 3,
    "plan": "A signals table of 8 rows (see signals; columns: The stem says | Think | Because | But not if) and the fixed H3 'Traps' with the 5 fast traps (devices.fast_traps_list), each a list item that ends with <!-- trap: <id> --> (see traps, placed_in 1-fast.md#signals-and-traps). At most 380 words (aim for 360).",
})
S.append({
    "file": "1-fast.md", "section": "changed-recently", "heading": "Changed recently", "bullets": [],
    "facts": f("launch-configurations-blocked-for-new-accounts", "launch-config-immutable",
               "change-price-capacity-optimized-2022", "spot-price-capacity-optimized-recommended",
               "change-predictive-forecasts-every-six-hours"),
    "status": "write", "minutes": 1,
    "plan": "Three examinable entries (see changed_recently.fast), in the form of CONVENTIONS D6, at most 120 words in all. The predictive scaling entry (2023-01-06) can be written now: its fact has a changed record. The launch configuration entry waits for fr-0062 and the Spot strategy entry for fr-0063 (changed.date on their facts): until filled, write them with <!-- needs-display --> markers as U3 describes, or leave them planned. If the three entries run over 120 words, keep the launch configuration and Spot entries and move the predictive one to one sentence in the scheduled and predictive subsection.",
})
S.append({
    "file": "1-fast.md", "section": "check", "heading": "Check", "bullets": [],
    "facts": f("elb-health-checks-ignored-by-default", "lb-default-ec2-checks-only", "health-elb-check-must-be-turned-on",
               "=elb-unhealthy-target-stop-resume", "scheduled-action-sets-capacities", "scheduled-vs-dynamic-when-to-use",
               "predictive-long-initialization-fit", "warm-pool-hibernated-ram", "cannot-hibernate-group-instance"),
    "status": "write", "minutes": 1,
    "plan": """Three Check prompts parallel to Predict, each answered in its reveal, with a separate '**Predict <n>:**' paragraph (U4). Check 1: 'A group of three instances behind an Application Load Balancer keeps its default health check settings. The application on one instance hangs, and the load balancer marks it unhealthy. What happens to that instance?' (It keeps running in the group and gets no requests: the load balancer stops routing to it ([it stops routing traffic to that target], elb-unhealthy-target-stop-resume), but by default the group [only replaces instances that are unhealthy or unreachable] by the EC2 checks (ec2-auto-scaling-lb-default-ec2-checks-only). Predict 1: no, not until you turn on the ELB health check type: [you must turn it on] (ec2-auto-scaling-health-elb-check-must-be-turned-on).) Check 2: 'A sale starts at 10:00 next Friday. Which scaling feature has the extra instances in service at 10:00?' (A scheduled action, which sets [desired, minimum, and maximum capacity] at a date and time (ec2-auto-scaling-scheduled-action-sets-capacities), because [the need arises on a predictable schedule] (ec2-auto-scaling-scheduled-vs-dynamic-when-to-use). Predict 2: before, with a scheduled action or predictive scaling; a metric-based policy is [which is reactive in nature] (ec2-auto-scaling-predictive-long-initialization-fit).) Check 3: 'A team wants instances that start fast with their memory already loaded. Where can such instances wait?' (In a warm pool, kept Hibernated: they [save the contents of your RAM] to the root volume (ec2-auto-scaling-warm-pool-hibernated-ram). Predict 3: no; [You can't hibernate an instance] that is in the group (ec2-auto-scaling-cannot-hibernate-group-instance).)""",
})
S.append({
    "file": "1-fast.md", "section": "recap-from-memory", "heading": "Recap from memory", "bullets": [], "facts": [],
    "status": "write", "minutes": 1,
    "plan": "Three Recap prompts, each asking only for a sentence, row or cell that 1-fast.md states above (U4): which health check type a group uses by default (trap list); which scaling method fits a load change at a known time (method table); where an instance of a group can keep its RAM while it is stopped (trap list).",
})

# ---------------------------------------------------------------- 2-deep.md
S.append({
    "file": "2-deep.md", "section": "how-it-works", "heading": "How it works", "bullets": [], "facts": [],
    "status": "write", "minutes": "sum of the subsection time boxes (54)",
    "order_note": "Teaching order follows one instance and then one number: the group and its three numbers (1), what it launches (2), where it launches (3), how a new instance enters service (4), how a failed one is found and replaced (5); then what moves the desired capacity: target tracking (6), step and simple policies with warmup (7), schedules and forecasts (8), a queue backlog (9); then how an instance leaves on scale in (10); then cost and speed: Spot above an On-Demand base (11), stopped instances in a warm pool, which also shows why scaling up does not fit a group (12); and change without patching: the instance refresh (13). The H2 intro line (about 30 words) names this path; it is not a list of subsections.",
})


def sub(section, heading, bullets, facts, minutes, words, plan, route=None, diagram=None, task=None):
    row = {"file": "2-deep.md", "section": section, "heading": heading, "bullets": bullets, "facts": facts,
           "status": "write", "minutes": minutes, "words_all_in": words, "plan": plan}
    if route:
        row["route"] = route
    if diagram:
        row["diagram"] = diagram
    if task:
        row["task"] = task
    return row


S.append(sub(S1, "An Auto Scaling group holds its desired capacity between a minimum and maximum",
    ["3.2.K4", "2.2.S1", "2.2.S4"],
    f("faq-definition", "faq-group-definition", "min-max-never-crossed", "desired-within-min-max",
      "desired-capacity-maintained", "default-no-policies-fixed-size", "health-unexpected-termination-replaced",
      "manual-scaling-definition", "scaling-policy-adjusts-desired", "dynamic-capacity-kept-within-min-max",
      "scaling-policies-capped-at-max-capacity", "console-desired-above-max-raises-max",
      "faq-fleet-management-vs-dynamic-scaling", "faq-no-additional-fees", "pricing-page-no-additional-fees",
      "billed-from-launch", "faq-group-size-bounded-by-ec2-quota", "faq-cannot-scale-past-ec2-limit",
      "faq-delete-group-terminates-instances", "unhealthy-terminated-replaced"),
    4, 230, {
        "problem": "Someone must count the running instances all day, start new ones when traffic grows and replace the ones that fail. An Auto Scaling group does that counting for you.",
        "trace": [
            "**Set three numbers.** The group has a [minimum number of instances] and a [maximum number of instances]; it [never goes below this size] and [never goes above this size] (ec2-auto-scaling-min-max-never-crossed). The desired capacity stays [within the range of your minimum and maximum] (ec2-auto-scaling-desired-within-min-max).",
            "**Hold the count.** With no policy and no scheduled action, the group keeps [maintain a fixed size] and [continues to maintain its desired capacity] (ec2-auto-scaling-default-no-policies-fixed-size); an instance that [terminates unexpectedly] gets a replacement (ec2-auto-scaling-health-unexpected-termination-replaced).",
            "**Move the count.** You can [update the desired capacity] yourself (ec2-auto-scaling-manual-scaling-definition), or a scaling policy [adjusts the desired capacity of the group], and the group [launches or terminates the instances as needed] (ec2-auto-scaling-scaling-policy-adjusts-desired).",
        ],
        "table": "Two jobs of one group (columns: Function | What it does | Example): fleet management | [automatically replaces unhealthy instances] | a failed instance is replaced; dynamic scaling | [automatically increases or decreases capacity] | more instances when CPU rises (both ec2-auto-scaling-faq-fleet-management-vs-dynamic-scaling); manual scaling | you set the desired capacity | before a planned load test.",
        "why": "Why three numbers? The minimum protects availability, the maximum protects the bill, and the desired capacity is the one number that policies move between them.",
        "exam_signal": "\"replace failed instances automatically\" with a steady load points to a group with equal minimum, maximum and desired capacity: it keeps [maintain a fixed size] (ec2-auto-scaling-default-no-policies-fixed-size); \"no more than N instances\" points to the maximum size.",
        "exam_trap": None,
        "body_extras": "One sentence: EC2 Auto Scaling has [no additional fees] (ec2-auto-scaling-faq-no-additional-fees), but instances are billed [as soon as they are launched] (ec2-auto-scaling-billed-from-launch).",
        "try_it": "auto-scaling-t02: one sentence ('Terminate an instance of a small group by hand and watch the group launch a replacement.'), then See [3-do.md](3-do.md). <!-- task: auto-scaling-t02 -->",
        "say_it": "The short answer is: the group keeps the desired number of instances between the minimum and the maximum. The thing to watch is that a policy moves only the desired number.",
        "stop_and_answer": "A group has minimum 2, maximum 4 and desired 4. A scaling policy calculates that 6 instances are needed. How many instances run? Answer: 4; the new capacity [never goes outside of the minimum and maximum] (ec2-auto-scaling-dynamic-capacity-kept-within-min-max). Prompt numbers are example values; the reveal links the fact.",
    }, task="auto-scaling-t02"))

S.append(sub(S2, "A launch template tells the group what to launch in numbered versions",
    ["2.2.S1", "2.2.K7"],
    f("=ec2-launch-template-stores-launch-parameters", "launch-template-ami-rule", "launch-template-versions",
      "=ec2-launch-template-versions-default", "instance-profile-for-app-credentials", "launch-template-passrole-needed",
      "no-secrets-in-user-data", "=ec2-metadata-user-data-not-protected", "launch-config-immutable",
      "faq-launch-configuration-one-and-immutable", "launch-config-no-mixed-types",
      "launch-configurations-no-new-instance-types", "launch-configurations-blocked-for-new-accounts",
      "launch-configurations-console-blocked-2023", "launch-template-newer-features", "ssm-parameter-for-ami",
      "ssm-parameter-sources", "ssm-parameter-no-warm-pools", "ssm-parameter-needs-getparameters",
      "launch-template-latest-version-passrole-risk", "require-imdsv2-launch-template",
      "customer-managed-key-needs-launch-template", "slr-no-customer-managed-key-access",
      "health-replacement-uses-current-settings", "faq-launch-configuration-change-existing-unaffected",
      "faq-group-from-instance-no-new-ami"),
    4, 235, {
        "problem": "Every new instance must be the same: same AMI, same instance type, same security groups, same role. The group needs one written recipe that it can read at any hour.",
        "trace": [
            "**Write the recipe.** A launch template stores [the AMI ID, instance type, and network settings] (ec2-launch-template-stores-launch-parameters). Its fields are optional, but without an AMI in the template [you cannot add the AMI] when you create the group (ec2-auto-scaling-launch-template-ami-rule).",
            "**Keep versions.** A group can use [multiple versions of a launch template] (ec2-auto-scaling-launch-template-versions); a launch that names no version uses the default version, and [it's the first version of the launch template] unless you change it (ec2-launch-template-versions-default).",
            "**Give it a role.** Code on the instances gets credentials when you [choose an instance profile] in the template (ec2-auto-scaling-instance-profile-for-app-credentials); the identity that creates or updates the group needs [iam:PassRole] (ec2-auto-scaling-launch-template-passrole-needed).",
            "**Keep secrets out.** AWS says to [never put confidential or sensitive information] in user data (ec2-auto-scaling-no-secrets-in-user-data).",
        ],
        "table": "Launch template or launch configuration (columns: Question | Launch template | Launch configuration): change it later | add a version | [can't modify a launch configuration] (ec2-auto-scaling-launch-config-immutable); Spot plus On-Demand, several instance types | yes | no: you [must use a launch template] (ec2-auto-scaling-launch-config-no-mixed-types); new instance types | yes | [no longer supported in launch configurations] (ec2-auto-scaling-launch-configurations-no-new-instance-types); accounts created from [October 1, 2024] | yes | [cannot create new launch configurations using any method] (ec2-auto-scaling-launch-configurations-blocked-for-new-accounts).",
        "why": "Why versions? You never edit the recipe that running instances came from; you add a version and choose which one the group launches, so the old version stays available.",
        "exam_signal": "\"launch the latest patched AMI without new launch templates or versions\" points to a Systems Manager parameter in place of the AMI ID, so the group can [use new AMI IDs] (ec2-auto-scaling-ssm-parameter-for-ami); \"mix Spot and On-Demand Instances\" points to a launch template (ec2-auto-scaling-launch-config-no-mixed-types).",
        "exam_trap": "auto-scaling-trap-launch-configuration-editable",
        "go_deeper": "Go deeper: $Latest, PassRole and AMI parameters. A group that uses `$Latest` or `$Default` launches whatever version is current, so a user who can update the template could pass a role [even if they don't have the `iam:PassRole` permission]; the condition key [autoscaling:LaunchTemplateVersionSpecified] limits that (ec2-auto-scaling-launch-template-latest-version-passrole-risk). An AMI parameter can be [a parameter shared from another AWS account] or [a public parameter for a public AMI] (ec2-auto-scaling-ssm-parameter-sources). At most 70 words.",
        "say_it": "The short answer is: the launch template is the recipe for every new instance. The thing to watch is that a new version changes new instances, not running ones.",
        "stop_and_answer": "A group launches from version 3 of a launch template. You create version 4 with a new AMI and make it the group's version. Which instances run the new AMI? Answer: only instances launched after the change, such as a replacement, which uses the [current settings of the Auto Scaling group] and its current template (ec2-auto-scaling-health-replacement-uses-current-settings); the others stay on version 3 until an instance refresh (subsection 13).",
    }))

S.append(sub(S3, "The group spreads instances evenly across its Availability Zones",
    ["2.2.S2", "2.2.S4"],
    f("desired-spread-across-azs", "launch-in-az-with-fewest", "faq-balances-across-azs", "launch-retries-other-az",
      "faq-retarget-other-azs", "az-unavailable-launch-elsewhere", "az-recovery-rebalance",
      "rebalance-launch-before-terminate", "rebalance-triggers", "rebalance-on-az-change", "process-az-rebalance",
      "faq-regional-spans-azs-not-regions", "resilience-practices", "add-az-group-and-load-balancer",
      "lb-no-traffic-to-disabled-az", "alb-minimum-two-azs", "wa-static-stability-for-az-loss",
      "control-plane-outage-no-effect", "az-strategy-balanced-best-effort", "az-distribution-balanced-only",
      "change-az-distribution-2024", "rebalance-exceed-max-margin", "zonal-shift-launches-only-in-healthy-azs",
      "zonal-shift-is-arc-feature", "zonal-shift-min-healthy-100-best-practice",
      "=global-infrastructure-single-az-failure-takes-all-instances",
      "=global-infrastructure-production-at-least-two-azs", "wa-load-balanced-clusters-use-groups"),
    4, 230, {
        "problem": "Three instances in one Availability Zone fail together when that zone fails. The group must place instances so that the loss of one zone leaves the others serving.",
        "trace": [
            "**Give it zones.** You give the group subnets in several zones, and the [desired capacity is distributed across these Availability Zones] (ec2-auto-scaling-desired-spread-across-azs).",
            "**Launch where it is thin.** A new instance goes to [the Availability Zone with the fewest instances] (ec2-auto-scaling-launch-in-az-with-fewest); if a launch fails there, the group tries [in another Availability Zone until it succeeds] (ec2-auto-scaling-launch-retries-other-az).",
            "**Lose a zone.** [If one Availability Zone becomes unavailable], the group can [launch instances in another one to compensate] (ec2-auto-scaling-az-unavailable-launch-elsewhere).",
            "**Rebalance.** When the zone recovers, the group [automatically rebalances the Auto Scaling group] (ec2-auto-scaling-az-recovery-rebalance); it [launches new instances before terminating the earlier ones] (ec2-auto-scaling-rebalance-launch-before-terminate).",
        ],
        "table": "What survives what (columns: Design | One instance fails | One zone fails): group in one zone | replaced | [none of your EC2 instances would be available] (global-infrastructure-single-az-failure-takes-all-instances); group in three zones | replaced | the other zones serve, and new instances launch there (ec2-auto-scaling-az-unavailable-launch-elsewhere).",
        "why": "Why balance? Each zone then holds a similar share, so a zone failure removes only that share; AWS recommends [at least one instance in each Availability Zone] (ec2-auto-scaling-resilience-practices).",
        "exam_signal": "\"survive the loss of an Availability Zone\" points to a group [across multiple Availability Zones] with a load balancer in the same zones (ec2-auto-scaling-resilience-practices); \"run in a second Region\" points to a second group, because groups [can span Availability Zones, but not AWS regions] (ec2-auto-scaling-faq-regional-spans-azs-not-regions).",
        "exam_trap": None,
        "body_extras": "One sentence: to add a zone you add it to the group and also do [enabling that Availability Zone for your load balancer] (ec2-auto-scaling-add-az-group-and-load-balancer); a load balancer [does not route traffic to them] in zones that it has not enabled (ec2-auto-scaling-lb-no-traffic-to-disabled-az). Chapter 14 owns load balancer zones: an xref, no detail.",
        "say_it": "The short answer is: give the group subnets in two or more zones, and it keeps them balanced. The thing to watch is the load balancer, which must use the same zones.",
        "stop_and_answer": "A group runs 6 instances, 2 in each of AZ 1, AZ 2 and AZ 3. AZ 2 becomes unavailable. Where do the replacements launch, and what happens when AZ 2 recovers? Answer: in AZ 1 and AZ 3 (ec2-auto-scaling-az-unavailable-launch-elsewhere); after recovery the group rebalances and [launches new instances before terminating the earlier ones] (ec2-auto-scaling-rebalance-launch-before-terminate).",
        "note": "Distribution strategies, the rebalancing margin and zonal shift are not in this subsection (budget); the B-list and one FAQ item do not need them. If words remain, one sentence: a zonal shift makes the group launch [in the healthy Availability Zones] (ec2-auto-scaling-zonal-shift-launches-only-in-healthy-azs).",
    }))

S.append(sub(S4, "A new instance joins the load balancer before it becomes InService",
    ["2.2.S1", "2.2.S2", "3.2.S1"],
    f("lifecycle-pending-then-inservice", "inservice-counts-toward-desired", "registers-with-lb-before-inservice",
      "lb-attach-target-group", "lb-auto-register-deregister", "lb-four-types", "process-add-to-load-balancer",
      "launch-hook-states", "terminate-hook-states", "faq-lifecycle-hooks-definition", "lifecycle-hook-purpose",
      "lifecycle-hook-lb-registration", "lifecycle-hook-heartbeat-timeout-default", "lifecycle-hook-default-result",
      "lifecycle-hook-abandon-continue", "lifecycle-hook-global-timeout", "lifecycle-hook-heartbeat-timeout-range",
      "lifecycle-hook-four-targets", "lifecycle-hook-eventbridge-default", "lifecycle-hook-eventbridge-recommended-target",
      "lifecycle-hook-lambda-direct-target", "lifecycle-hook-user-data-complete", "lifecycle-hook-target-same-region",
      "lifecycle-hook-not-for-attach-detach-standby", "no-visibility-into-applications", "billed-from-launch",
      "faq-data-not-copied-to-new-instances", "=ec2-user-data-runs-at-first-launch-by-default",
      "elastic-ip-not-moved-to-replacement", "health-ebs-volumes-detached-on-terminate"),
    4, 240, {
        "problem": "A new instance that gets requests before its software is ready returns errors. The group must hold it back until it is ready, and then hand it to the load balancer.",
        "trace": [
            "**Pending.** Instances launched in a scale-out [start in the `Pending` state] (ec2-auto-scaling-lifecycle-pending-then-inservice); billing starts [as soon as they are launched] (ec2-auto-scaling-billed-from-launch).",
            "**Wait, if you add a hook.** With an [EC2_INSTANCE_LAUNCHING] hook the instance waits in [Pending:Wait] until your code completes the action, then moves to [Pending:Proceed] (ec2-auto-scaling-launch-hook-states); a hook makes sure the application is [ready to accept traffic] (ec2-auto-scaling-lifecycle-hook-lb-registration).",
            "**Register.** The group [registers your instance with the load balancer] [before it marks the instance as] InService (ec2-auto-scaling-registers-with-lb-before-inservice); for an Application Load Balancer you [attach a target group rather than] the load balancer itself (ec2-auto-scaling-lb-attach-target-group).",
            "**InService.** From then on the instance is [counted against the desired capacity] (ec2-auto-scaling-inservice-counts-toward-desired).",
        ],
        "table": "How a lifecycle action ends (columns: Hook | Continue | Abandon): launch | the instance goes into service | the group terminates it and launches another; terminate | the instance terminates | the instance terminates and remaining hooks are skipped (ec2-auto-scaling-lifecycle-hook-abandon-continue). One sentence under the table: when nobody answers, the hook waits [3600 seconds] (ec2-auto-scaling-lifecycle-hook-heartbeat-timeout-default) and then takes its default result, [ABANDON] (ec2-auto-scaling-lifecycle-hook-default-result).",
        "diagram_embed": "auto-scaling-lifecycle after the table, with its alt and caption from diagrams below (about 45 words with the caption; it counts toward words_all_in).",
        "why": "Why a wait state? EC2 Auto Scaling has [no visibility into the applications] on its instances (ec2-auto-scaling-no-visibility-into-applications); the hook is the point where your own code says 'ready', for example a user data script that makes [add the CompleteLifecycleAction API call] (ec2-auto-scaling-lifecycle-hook-user-data-complete).",
        "exam_signal": "\"configure software before the instance receives traffic\" points to a launch lifecycle hook: [launch hooks can perform software configuration] (ec2-auto-scaling-faq-lifecycle-hooks-definition); \"new instances must start with the data of the running ones\" is not automatic: [Data is not automatically copied] (ec2-auto-scaling-faq-data-not-copied-to-new-instances).",
        "exam_trap": None,
        "say_it": "The short answer is: a launch hook holds a new instance until your setup says it is ready. The thing to watch is the timeout, which ends in abandon by default.",
        "stop_and_answer": "A launch hook keeps its default settings. The bootstrap script crashes and never completes the lifecycle action. What happens to the instance? Answer: after the heartbeat timeout the group takes the default result, [ABANDON] (ec2-auto-scaling-lifecycle-hook-default-result); at launch, abandon lets the group terminate the instance and replace it (ec2-auto-scaling-lifecycle-hook-abandon-continue).",
        "note": "Keep the four notification targets (EventBridge, SNS, SQS, Lambda) to one clause at most: [Invoke a Lambda function] is one of [four different approaches for implementing notification targets] (ec2-auto-scaling-lifecycle-hook-four-targets). The termination hook is taught in subsection 10.",
    }, diagram="auto-scaling-lifecycle"))

S.append(sub(S5, "The group replaces instances that fail the health checks you turned on",
    ["2.2.S4", "2.2.S2"],
    f("health-check-type-ec2-default", "ec2-status-checks-always-enabled", "elb-health-checks-ignored-by-default",
      "health-elb-check-must-be-turned-on", "lb-default-ec2-checks-only", "health-elb-unhealthy-replaced",
      "elb-checks-reroute-and-replace", "=elb-unhealthy-target-stop-resume", "=elb-routes-only-to-healthy-targets",
      "faq-which-health-check-type", "health-not-running-immediate", "status-check-failure-waits-few-minutes",
      "health-assumed-healthy", "grace-period-definition", "grace-period-console-300-cli-0",
      "grace-period-zero-turns-off", "grace-period-zero-with-launch-hooks", "health-optional-checks-after-grace-period",
      "health-ebs-check-must-be-turned-on", "health-vpc-lattice-check-must-be-turned-on",
      "custom-health-check-immediate-replace", "faq-set-instance-health-custom-check", "health-scheduled-event-replaced",
      "faq-replaces-impaired-instance", "faq-replacement-time-minutes", "faq-elb-requests-before-detection-fail",
      "health-draining-before-terminating-unhealthy", "health-replace-at-same-time-default",
      "unhealthy-replacement-10-percent-at-a-time", "unhealthy-replacement-after-90-percent",
      "unhealthy-replacement-small-group-one-at-a-time", "maintenance-policy-launch-before-terminating-option",
      "maintenance-policy-none-by-default", "faq-suspend-health-checks", "health-cannot-remove-ec2-checks",
      "set-instance-health-respects-grace-period", "faq-no-elb-required-ec2-health-check",
      "wa-replaces-unhealthy-instance", "unhealthy-bypasses-protection", "faq-unhealthy-instance-definition",
      "faq-works-with-alb-nlb-health-checks", "unhealthy-terminated-replaced"),
    5, 240, {
        "problem": "The application on an instance hangs, but the instance still runs. The load balancer sees the failure. The group must see it too, or nothing replaces the instance.",
        "trace": [
            "**EC2 checks, always.** Amazon EC2 status checks are the [default health check type] (ec2-auto-scaling-health-check-type-ec2-default) and are [always enabled] (ec2-auto-scaling-ec2-status-checks-always-enabled); an instance that is no longer running is [treated as an immediate failure] (ec2-auto-scaling-health-not-running-immediate).",
            "**ELB checks, only if you turn them on.** By default the group [ignores the results of the Elastic Load Balancing] health checks (ec2-auto-scaling-elb-health-checks-ignored-by-default); for the ELB health check type [you must turn it on] (ec2-auto-scaling-health-elb-check-must-be-turned-on).",
            "**Grace period.** A new instance gets the [minimum amount of time (in seconds)] before the group can terminate it as unhealthy (ec2-auto-scaling-grace-period-definition): [300 seconds] in the console and [0 seconds] with the AWS CLI or an SDK (ec2-auto-scaling-grace-period-console-300-cli-0).",
            "**Replace.** The group [terminates the unhealthy instance and launches another] (ec2-auto-scaling-unhealthy-terminated-replaced), while [Elastic Load Balancing stops sending traffic to it] (ec2-auto-scaling-elb-checks-reroute-and-replace).",
        ],
        "table": "Health check types (columns: Type | On by default | What it sees): Amazon EC2 status checks | yes, [always enabled] (ec2-auto-scaling-ec2-status-checks-always-enabled) | [hardware has become impaired] or the instance stopped running (ec2-auto-scaling-faq-unhealthy-instance-definition); Elastic Load Balancing | no, [you must turn it on] (ec2-auto-scaling-health-elb-check-must-be-turned-on) | whether the load balancer gets answers; Amazon EBS | no (ec2-auto-scaling-health-ebs-check-must-be-turned-on) | volumes [passing I/O status checks]; custom | your code calls [SetInstanceHealth] (ec2-auto-scaling-faq-set-instance-health-custom-check) | anything your code tests.",
        "why": "Why is the ELB check off by default? A group can run without a load balancer: you [don't have to use ELB] (ec2-auto-scaling-faq-no-elb-required-ec2-health-check). And the load balancer itself only routes: [it stops routing traffic to that target] (elb-unhealthy-target-stop-resume); replacing is the group's job.",
        "exam_signal": "\"instances keep running but return errors, and nothing replaces them\" points to the ELB health check type: [select an ELB health check] (ec2-auto-scaling-faq-which-health-check-type); an option that says the load balancer replaces the instance states trap elb-trap-lb-replaces-instance (chapter 14).",
        "exam_trap": None,
        "spot_the_bug": "**Spot the bug.** A team creates a group with the AWS CLI, turns on ELB health checks and keeps the default grace period. The application needs 4 minutes to start. New instances are replaced again and again. What is wrong? Reveal: with the AWS CLI the default grace period is [0 seconds] (ec2-auto-scaling-grace-period-console-300-cli-0), so an instance that is still starting fails the load balancer check and is replaced; set a grace period that covers the start, or keep [set the health check grace period to 0] with a launch lifecycle hook (ec2-auto-scaling-grace-period-zero-with-launch-hooks). About 55 words with the reveal.",
        "go_deeper": "Go deeper: how fast the group replaces. By default it replaces up to [10 percent] of the desired capacity at a time (ec2-auto-scaling-unhealthy-replacement-10-percent-at-a-time), and [new instances are provisioned at the same time] as unhealthy ones are terminated (ec2-auto-scaling-health-replace-at-same-time-default); an instance maintenance policy with [Launch before terminating] favors availability (ec2-auto-scaling-maintenance-policy-launch-before-terminating-option). To inspect a failing instance, [SuspendProcesses] stops the checks until [ResumeProcesses] (ec2-auto-scaling-faq-suspend-health-checks). At most 70 words.",
        "say_it": "The short answer is: the group replaces what fails the checks that are turned on. The thing to watch is the ELB check, which is off until you turn it on.",
        "stop_and_answer": "A group without a load balancer runs a worker. The worker process crashes, but the operating system and the instance keep running. Does the group replace the instance? Answer: not with the default checks; the group [only replaces instances that are unhealthy or unreachable] by the EC2 checks (ec2-auto-scaling-lb-default-ec2-checks-only); a custom check that calls [SetInstanceHealth] can mark it unhealthy (ec2-auto-scaling-faq-set-instance-health-custom-check).",
    }, route="pass"))

S.append(sub(S6, "A target tracking policy keeps one metric near the value you choose",
    ["3.2.S2", "3.2.K4"],
    f("dynamic-target-tracking-definition", "faq-target-tracking-definition", "faq-target-tracking-average-cpu-example",
      "target-tracking-predefined-metrics", "target-tracking-service-manages-alarms", "target-tracking-creates-two-alarms",
      "target-tracking-do-not-edit-alarms", "target-tracking-no-manual-alarms", "target-tracking-scale-in-gradual",
      "target-tracking-disable-scale-in", "target-tracking-metric-must-fall-as-capacity-grows",
      "target-tracking-unsuitable-metrics", "target-tracking-alb-resource-label",
      "target-tracking-throughput-per-instance-minute", "target-tracking-target-value-high-with-buffer",
      "wa-utilization-target-50-70-percent", "target-tracking-multiple-policies-different-metrics",
      "target-tracking-out-any-in-all", "target-tracking-no-scale-out-below-target",
      "target-tracking-insufficient-data-no-scaling", "target-tracking-conservative-rounding",
      "target-tracking-scale-to-zero-needs-min-zero", "target-tracking-metric-math-current",
      "metric-math-single-time-series", "high-resolution-target-tracking", "high-resolution-not-in-govcloud",
      "wa-memory-is-a-poor-scaling-metric", "wa-customer-experience-metric", "wa-scaling-metric-examples",
      "pauses-scale-in-unreliable-metrics", "ec2-metrics-five-minute-default", "dynamic-largest-capacity-wins",
      "change-target-tracking-metric-math-2022"),
    4, 240, {
        "problem": "Writing alarms and step sizes by hand is slow and easy to get wrong. Most teams want one thing: keep CPU, or requests per instance, near one value.",
        "trace": [
            "**Pick a metric and a value.** You choose [a Amazon CloudWatch metric and a target value] (ec2-auto-scaling-dynamic-target-tracking-definition), for example [ASGAverageCPUUtilization] or [ALBRequestCountPerTarget] (ec2-auto-scaling-target-tracking-predefined-metrics). Copy the display with its article exactly, or rephrase around [Target tracking scaling].",
            "**AWS writes the alarms.** EC2 Auto Scaling [creates and manages the CloudWatch alarms] that act [when the metric deviates from the target] (ec2-auto-scaling-target-tracking-service-manages-alarms); [Do not create, edit, or delete] them (ec2-auto-scaling-target-tracking-do-not-edit-alarms).",
            "**Out fast, in slowly.** The policy adds instances while the metric is above the target and [prioritizes availability] by [scaling in more gradually when traffic is decreasing] (ec2-auto-scaling-target-tracking-scale-in-gradual).",
            "**Several policies.** You can add more, as long as [each of them uses a different metric] (ec2-auto-scaling-target-tracking-multiple-policies-different-metrics); the group scales out if [any of the target tracking policies] is ready and scales in only if [all of the target tracking policies] are (ec2-auto-scaling-target-tracking-out-any-in-all).",
        ],
        "table": "Is the metric a good target? (columns: Metric | Falls as instances are added | Use it): average CPU of the group | yes | yes, as in [average CPU utilization at 50%] (ec2-auto-scaling-faq-target-tracking-average-cpu-example); ALB requests per target | yes | yes, with [ResourceLabel] (ec2-auto-scaling-target-tracking-alb-resource-label); load balancer RequestCount or Latency | no | no: they [do not work for target tracking] (ec2-auto-scaling-target-tracking-unsuitable-metrics); memory | no, it stays high | no: it [does not correspond to demand in both directions] (ec2-auto-scaling-wa-memory-is-a-poor-scaling-metric).",
        "why": "Why must the metric fall as instances are added? Target tracking assumes the metric is [inversely proportional to the capacity] (ec2-auto-scaling-target-tracking-metric-must-fall-as-capacity-grows): it computes how many instances bring the metric back to the target, and a metric that ignores the instance count never gets there.",
        "exam_signal": "\"keep the average CPU utilization of the fleet at 50%\" or \"the simplest scaling policy\" points to target tracking, which [adjusts the number of EC2 instances] like a [home thermostat] (ec2-auto-scaling-faq-target-tracking-definition); \"requests per instance\" points to [ALBRequestCountPerTarget] (ec2-auto-scaling-target-tracking-predefined-metrics).",
        "exam_trap": None,
        "go_deeper": "Go deeper: target values, metric math and seconds. AWS says [set the target value as high as possible] with a [reasonable buffer for unexpected traffic increases] (ec2-auto-scaling-target-tracking-target-value-high-with-buffer); Well-Architected names targets that [range between 50-70%] (ec2-auto-scaling-wa-utilization-target-50-70-percent). Metric math combines metrics but [must eventually return a single time series] (ec2-auto-scaling-metric-math-single-time-series). High-resolution metrics react [lower than 60 seconds]; the [lowest supported interval is 10 seconds] (ec2-auto-scaling-high-resolution-target-tracking). At most 70 words.",
        "try_it": "auto-scaling-t03: one sentence ('Attach a target tracking policy to an empty group and read the two alarms that AWS creates for it.'), then See [3-do.md](3-do.md). <!-- task: auto-scaling-t03 -->",
        "say_it": "The short answer is: name a metric and a target, and the group adds or removes instances to hold it. The thing to watch is a metric that does not fall when instances are added.",
        "stop_and_answer": "A group has two target tracking policies: average CPU at 50% and requests per target at 1,000. CPU sits at 30% while requests per target reach 1,400. Does the group scale out, and could it scale in? Answer: it scales out, because one ready policy is enough: [any of the target tracking policies] (ec2-auto-scaling-target-tracking-out-any-in-all); it scales in only when [all of the target tracking policies] are ready.",
    }, route="pass", task="auto-scaling-t03"))

S.append(sub(S7, "Step scaling follows alarm size and warmup replaces the old cooldown",
    ["3.2.S2"],
    f("dynamic-step-definition", "step-simple-you-manage-alarms", "step-adjustment-types", "step-ranges-no-overlap-or-gap",
      "step-continues-until-ok", "step-warmup-single-activity", "step-percent-rounding",
      "step-bounds-console-absolute-cli-relative", "step-flapping-margin", "dynamic-simple-definition",
      "simple-single-adjustment-cooldown", "default-cooldown-300-seconds", "cooldown-applies-to-simple-scaling",
      "cooldown-target-tracking-step-do-not-wait", "cooldown-scheduled-action-does-not-wait",
      "cooldown-unhealthy-replacement-does-not-wait", "cooldown-manual-scaling-default-no-wait",
      "cooldown-policy-specific-overrides-default", "cooldown-starts-after-last-instance",
      "cooldown-scale-in-starts-at-draining", "cooldown-not-settable-at-console-create",
      "simple-scaling-not-recommended", "simple-scaling-paused-by-hooks", "default-instance-warmup-purpose",
      "default-instance-warmup-not-on-by-default", "default-instance-warmup-start-300-seconds",
      "warmup-instance-not-in-metrics", "warmup-blocks-scale-in", "warmup-fallbacks-when-unset",
      "lifecycle-hook-scale-out-metrics-wait", "ec2-metrics-five-minute-default",
      "aa:plans-detailed-monitoring-best-practice", "faq-dynamic-scaling-alarm-example",
      "dynamic-target-tracking-with-step-caution", "quota-step-adjustments-per-policy"),
    4, 235, {
        "problem": "A new instance spends its first minutes starting up, often with high CPU. If the policy counts that CPU, it adds instances that nobody needs; if it waits a fixed time, a second spike gets nothing.",
        "trace": [
            "**Your alarm, your steps.** With step scaling [you create and manage the CloudWatch alarms] (ec2-auto-scaling-step-simple-you-manage-alarms); the adjustment grows with [the size of the alarm breach] (ec2-auto-scaling-dynamic-step-definition), and the step ranges [can't overlap or have a gap] (ec2-auto-scaling-step-ranges-no-overlap-or-gap).",
            "**Simple scaling waits.** Simple scaling uses [a single scaling adjustment] and [a cooldown period between each scaling activity] (ec2-auto-scaling-dynamic-simple-definition); the default cooldown is [300 seconds] (ec2-auto-scaling-default-cooldown-300-seconds).",
            "**Step and target tracking do not wait.** They can scale out [without waiting for the cooldown period to end] (ec2-auto-scaling-cooldown-target-tracking-step-do-not-wait).",
            "**Warmup instead.** A new instance is [not counted toward the aggregated EC2 instance metrics] until its warmup ends (ec2-auto-scaling-warmup-instance-not-in-metrics). The default instance warmup: [It is not enabled or configured by default.] AWS says [strongly recommend that you enable and configure] it (ec2-auto-scaling-default-instance-warmup-not-on-by-default); start with [300 seconds] if unsure (ec2-auto-scaling-default-instance-warmup-start-300-seconds).",
        ],
        "table": "Who waits for the cooldown? (columns: Activity | Waits for the cooldown): simple scaling | yes: [scaling activities initiated by simple scaling policies] (ec2-auto-scaling-cooldown-applies-to-simple-scaling); step scaling and target tracking | no, warmup instead (ec2-auto-scaling-cooldown-target-tracking-step-do-not-wait); scheduled action | no: it can [initiate a scaling activity immediately] (ec2-auto-scaling-cooldown-scheduled-action-does-not-wait); replacing an unhealthy instance | no: it [does not wait for the cooldown period] (ec2-auto-scaling-cooldown-unhealthy-replacement-does-not-wait).",
        "why": "Why did AWS move from cooldown to warmup? A cooldown blocks every new activity for a fixed time. A warmup only keeps the new instances out of the numbers, so another breach in the same step range gives [result in a single scaling activity] (ec2-auto-scaling-step-warmup-single-activity), while a larger breach still adds more.",
        "exam_signal": "\"add more instances when the breach is larger\" points to step scaling (ec2-auto-scaling-dynamic-step-definition); \"new instances distort the metric while they start\" points to the default instance warmup, the time an instance [waits before contributing usage data] (ec2-auto-scaling-default-instance-warmup-purpose).",
        "exam_trap": "auto-scaling-trap-cooldown-for-all-policies",
        "say_it": "The short answer is: prefer target tracking or step scaling, and set an instance warmup. The thing to watch is simple scaling, which waits for the cooldown.",
        "stop_and_answer": "A group has one simple scaling policy with the default cooldown. A spike adds 2 instances; 90 seconds after they finish launching, a larger spike arrives. Can the policy act on it, and what would you change? Answer: not yet: the cooldown starts [when the last instance finishes launching or terminating] (ec2-auto-scaling-cooldown-starts-after-last-instance) and lasts [300 seconds] (ec2-auto-scaling-default-cooldown-300-seconds); AWS says [do not use simple scaling policies] (ec2-auto-scaling-simple-scaling-not-recommended).",
    }))

S.append(sub(S8, "Scheduled and predictive scaling add capacity before the load arrives",
    ["3.2.S2", "4.2.S2", "3.2.K4"],
    f("scaling-methods", "scheduled-vs-dynamic-when-to-use", "scheduled-action-sets-capacities",
      "scheduled-one-time-or-recurring", "scheduled-utc-default-time-zone", "scheduled-dst-location-time-zones",
      "scheduled-plus-policies-together", "scheduled-action-keeps-current-limits", "scheduled-unique-start-time",
      "scheduled-order-within-group-only", "scheduled-suspend-to-turn-off", "faq-predictive-ahead-of-demand",
      "predictive-long-initialization-fit", "predictive-needs-24-hours-of-data", "predictive-analyzes-up-to-14-days",
      "predictive-forecast-next-48-hours", "predictive-forecast-updated-every-6-hours", "predictive-two-full-weeks-best",
      "predictive-forecast-only-mode-first", "predictive-does-not-scale-in", "predictive-scales-at-start-of-hour",
      "predictive-pre-launch-buffer", "predictive-max-capacity-breach", "predictive-raised-max-stays",
      "predictive-assumes-homogeneous", "predictive-new-group-needs-24-hours",
      "combine-policy-types-predictive-plus-dynamic", "multiple-policies-largest-desired-wins",
      "faq-predictive-policy-vs-scaling-plan", "faq-predictive-policy-cli-console-sdk",
      "wa-predictive-patterns-vs-scheduled-times", "wa-time-based-supply-no-startup-delay", "wa-three-scaling-options",
      "change-predictive-forecasts-every-six-hours", "wa-predictive-scaling-before-projected-load",
      "sqs-backlog-per-instance"),
    5, 255, {
        "problem": "A new instance needs minutes before it serves traffic. A policy that reacts to the morning peak adds capacity only after users already wait.",
        "trace": [
            "**Schedule what you know.** A scheduled action sets [desired, minimum, and maximum capacity] at a date and time (ec2-auto-scaling-scheduled-action-sets-capacities), to [scale one time only] or [on a recurring schedule] (ec2-auto-scaling-scheduled-one-time-or-recurring); recurring actions use [Coordinated Universal Time (UTC)] unless you set a time zone (ec2-auto-scaling-scheduled-utc-default-time-zone).",
            "**Let the policy continue.** You can [use scheduled scaling and scaling policies together]; the policy's result [must fall within the minimum and maximum capacity] that the scheduled action set (ec2-auto-scaling-scheduled-plus-policies-together).",
            "**Forecast what repeats.** Predictive scaling can [proactively increase capacity ahead of upcoming demand] (ec2-auto-scaling-faq-predictive-ahead-of-demand). It needs [at least 24 hours of data] (ec2-auto-scaling-predictive-needs-24-hours-of-data), forecasts the next [48 hours] (ec2-auto-scaling-predictive-forecast-next-48-hours), and starts in [forecast only] mode (ec2-auto-scaling-predictive-forecast-only-mode-first).",
            "**Pair it.** Predictive scaling [it will not scale in to remove capacity] (ec2-auto-scaling-predictive-does-not-scale-in), so you [combine predictive scaling and dynamic scaling] (ec2-auto-scaling-combine-policy-types-predictive-plus-dynamic); with several policies, desired capacity is [set to the maximum of those] (ec2-auto-scaling-multiple-policies-largest-desired-wins).",
        ],
        "table": "Which method acts first (columns: Load pattern | Method | Why): a known time, such as a sale at 10:00 | scheduled action | [the need arises on a predictable schedule] (ec2-auto-scaling-scheduled-vs-dynamic-when-to-use); repeats daily or weekly | predictive plus dynamic | fits applications that [take a long time to initialize] (ec2-auto-scaling-predictive-long-initialization-fit); no pattern | dynamic, such as target tracking | [you don't know when the traffic will change] (ec2-auto-scaling-scheduled-vs-dynamic-when-to-use).",
        "diagram_embed": "auto-scaling-method-ladder after the table, with its alt (about 35 words) and caption from diagrams below.",
        "why": "Why not forecast everything? A forecast follows patterns that it has seen; a surprise spike still needs a dynamic policy, and the forecast does not remove capacity.",
        "exam_signal": "\"traffic rises at the same time every weekday\" points to a scheduled action or predictive scaling: [Predictive scaling uses patterns to scale out], while [scheduled scaling uses pre-defined times to scale out] (ec2-auto-scaling-wa-predictive-patterns-vs-scheduled-times); \"instances take a long time to initialize\" points to predictive scaling or a warm pool (subsection 12).",
        "exam_trap": "auto-scaling-trap-predictive-scales-in",
        "startup_example": "At most 25 words, numbers only from uses_numbers: 'Callvale's web group raises capacity to 6 at 08:45 on weekdays, before the peak window from 09:00 to 11:00; target tracking follows the traffic above it.' No AWS rule in the callout.",
        "say_it": "The short answer is: schedule what you know, forecast what repeats, and let target tracking handle the rest. The thing to watch is that the forecast does not remove capacity.",
        "stop_and_answer": "A new group replaces an old one and gets a predictive scaling policy at once. The next morning it does not add capacity before the peak. Why? Answer: a new group needs [24 hours of historical load data] before forecasts start (ec2-auto-scaling-predictive-new-group-needs-24-hours), and the policy begins in [forecast only] mode, which does not scale (ec2-auto-scaling-predictive-forecast-only-mode-first).",
    }, route="pass", diagram="auto-scaling-method-ladder"))

S.append(sub(S9, "A worker group scales on the backlog of messages per instance",
    ["3.2.S1", "3.2.S2", "2.1.S2"],
    f("whitepaper-group-per-tier", "sqs-dynamic-scaling-when-load-varies", "sqs-queue-length-not-proportional",
      "sqs-backlog-per-instance", "sqs-backlog-per-instance-metric-math", "sqs-acceptable-backlog-per-instance-target",
      "sqs-metric-math-instead-of-custom", "sqs-unprocessed-messages-return", "wa-queue-depth-metric-for-batch-work",
      "wa-scaling-metric-examples", "wa-customer-experience-metric", "target-tracking-scale-to-zero-needs-min-zero",
      "group-metric-names", "group-metrics-must-enable", "group-metrics-best-effort",
      "target-tracking-metric-must-fall-as-capacity-grows"),
    4, 230, {
        "problem": "Uploads arrive in bursts. If the web tier waits for each conversion, both tiers must grow together. With a queue between them, each tier scales on its own signal.",
        "trace": [
            "**Split the tiers.** A group for each layer means [each layer can scale independently] (ec2-auto-scaling-whitepaper-group-per-tier): the web tier sends jobs to an Amazon SQS queue, and the workers take them.",
            "**Do not scale on the queue length alone.** The number of messages [might not change proportionally] to the size of the group (ec2-auto-scaling-sqs-queue-length-not-proportional).",
            "**Divide by the workers.** Backlog per instance is the queue length divided by the running instances: [Divide that number by the fleet's running capacity] (ec2-auto-scaling-sqs-backlog-per-instance); metric math computes it as [ApproximateNumberOfMessagesVisible] divided by [GroupInServiceInstances] (ec2-auto-scaling-sqs-backlog-per-instance-metric-math).",
            "**Set the target.** Take the longest acceptable wait and [divide it by the average time] that one instance needs for a message: [10 / 0.1, which equals 100 messages] (ec2-auto-scaling-sqs-acceptable-backlog-per-instance-target).",
        ],
        "table": "A metric for each tier (columns: Tier | Scaling metric | Why): web tier | CPU or requests per target | it falls as instances are added (ec2-auto-scaling-target-tracking-metric-must-fall-as-capacity-grows); conversion workers | backlog per instance | for transcoding, [100% CPU utilization is expected and should not be your primary metric] (ec2-auto-scaling-wa-queue-depth-metric-for-batch-work); steady job rate | none: a fixed-size group | AWS suggests dynamic scaling when the number of uploads changes: [you might consider using dynamic scaling] (ec2-auto-scaling-sqs-dynamic-scaling-when-load-varies).",
        "why": "Why divide by the instances? Then the metric falls when the group grows, as target tracking needs; and metric math lets you [save the cost and effort] of publishing your own metric (ec2-auto-scaling-sqs-metric-math-instead-of-custom).",
        "exam_signal": "\"scale the workers on the number of messages in the queue\" points to target tracking on [backlog per instance] (ec2-auto-scaling-sqs-backlog-per-instance), not on the raw queue length; \"decouple the tiers\" points to a queue between two groups (ec2-auto-scaling-whitepaper-group-per-tier).",
        "exam_trap": "auto-scaling-trap-queue-length-metric",
        "body_extras": "One sentence if words remain: a worker group that should scale in to zero needs its [minimum capacity must be set to 0] (ec2-auto-scaling-target-tracking-scale-to-zero-needs-min-zero). Chapter 31 owns queues: an xref, no SQS detail.",
        "say_it": "The short answer is: put a queue between the tiers and scale workers on messages per instance. The thing to watch is the target, which comes from your acceptable delay.",
        "stop_and_answer": "Workers need 0.5 seconds for a message, and a message may wait at most 30 seconds. The queue holds 1,800 visible messages and 10 workers are InService. Should the group scale out? Answer: yes; the target is the wait [divide it by the average time] per message, here 60, and the backlog is 1,800 divided by 10, here 180 per instance (ec2-auto-scaling-sqs-acceptable-backlog-per-instance-target, ec2-auto-scaling-sqs-backlog-per-instance). Write the reveal's derived numbers without units (60, 180) so that they need no link; the prompt numbers are example values.",
    }, route="pass"))

S.append(sub(S10, "Scale in removes the instance that the termination policy picks",
    ["2.2.S4", "2.1.S2"],
    f("faq-termination-policy-and-instance-protection", "termination-az-balance-first", "termination-imbalanced-zone-first",
      "termination-default-zone-with-most", "termination-default-outdated-first",
      "termination-default-billing-hour-then-random", "termination-mixed-purchase-option-first",
      "termination-policy-oldest-instance", "termination-policy-newest-instance",
      "termination-policy-oldest-launch-template", "termination-policy-closest-to-next-hour",
      "termination-policy-allocation-strategy", "custom-termination-policy-lambda",
      "custom-termination-policy-failure-no-termination", "termination-policy-skips-unhealthy",
      "scale-in-protection-off-by-default", "scale-in-protection-not-health-replacement",
      "scale-in-protection-ec2-termination-protection-for-manual", "scale-in-protection-all-protected",
      "scale-in-protection-group-setting-new-only", "scale-in-protection-lost-on-detach", "unhealthy-bypasses-protection",
      "deregisters-on-scale-in", "cooldown-elb-deregistration-300-seconds", "=elb-deregistration-delay-default-300-seconds",
      "termination-hook-extends-life", "termination-hook-best-effort", "terminate-hook-states",
      "lifecycle-hook-scale-in-use", "no-visibility-into-applications", "stateful-drain-or-transfer",
      "faq-stateful-instance", "faq-persist-data-off-instance", "wa-offload-session-data",
      "imds-target-lifecycle-state", "instance-lifecycle-policy-retains-on-abandon",
      "retained-instances-charged-and-replaced", "sqs-unprocessed-messages-return", "standby-no-lb-traffic",
      "standby-preferred-over-detach", "standby-decrement-choice", "standby-billed", "standby-no-health-checks",
      "standby-still-managed", "detach-replace-or-decrement", "detached-keeps-running", "suspend-terminate-full-control",
      "lifecycle-matching-scale-in", "terminating-cannot-return"),
    4, 235, {
        "problem": "When the group shrinks, one instance must go. It may be in the middle of a request, a session or a long job.",
        "trace": [
            "**Balance zones first.** The group [always balances instances across Availability Zones first], [regardless of which termination policy is used] (ec2-auto-scaling-termination-az-balance-first); the default picks the zone that [has the most instances] (ec2-auto-scaling-termination-default-zone-with-most).",
            "**Apply the policy.** The default policy is built to [terminate instances that are using outdated configurations first] (ec2-auto-scaling-termination-default-outdated-first), then the one [closest to the next billing hour], and to [terminate one at random] among equals (ec2-auto-scaling-termination-default-billing-hour-then-random).",
            "**Drain.** The group [automatically deregisters the terminating instance] from the load balancer, and open requests continue [until the deregistration delay expires] (ec2-auto-scaling-deregisters-on-scale-in), [300 seconds] by default (ec2-auto-scaling-cooldown-elb-deregistration-300-seconds).",
            "**Let it finish, if you add a hook.** A termination hook [extends the life of your Amazon EC2 instance] so that it can save or hand over its work (ec2-auto-scaling-termination-hook-extends-life); [termination lifecycle hooks operate on a best-effort basis] (ec2-auto-scaling-termination-hook-best-effort).",
        ],
        "table": "Other termination policies (columns: Policy | Removes first | Use it when): OldestInstance | [Terminate the oldest instance in the group] | you move to a new instance type (ec2-auto-scaling-termination-policy-oldest-instance); NewestInstance | [Terminate the newest instance in the group] | you test a new launch configuration (ec2-auto-scaling-termination-policy-newest-instance); OldestLaunchTemplate | [Terminate instances that have the oldest launch template] | you roll out a new template (ec2-auto-scaling-termination-policy-oldest-launch-template); custom | instances that a Lambda function returns ([custom termination policy using a Lambda function], ec2-auto-scaling-custom-termination-policy-lambda) | your own rules.",
        "why": "Why zones first? Losing the balance on scale in would undo the protection of subsection 3, so zone balance comes before any policy; this is why a newer instance can go before an older one.",
        "exam_signal": "\"an instance that runs a long job must not be removed by scale in\" points to instance scale-in protection: [use instance protection to prevent] (ec2-auto-scaling-faq-termination-policy-and-instance-protection); \"users are signed out when an instance is removed\" points to session data off the instance: [database, cache, or external files] (ec2-auto-scaling-wa-offload-session-data).",
        "exam_trap": "auto-scaling-trap-scale-in-protection-protects-all",
        "say_it": "The short answer is: the group drains one instance from the fullest zone, chosen by its termination policy. The thing to watch is long work, which needs protection or a hook.",
        "stop_and_answer": "A group runs 4 instances in AZ 1 and 3 in AZ 2, all from the current launch template, with the default termination policy. Scale in removes one instance. Which zone loses it, and which instance there? Answer: AZ 1, the zone that [has the most instances] (ec2-auto-scaling-termination-default-zone-with-most); with no outdated configuration, the instance [closest to the next billing hour] goes (ec2-auto-scaling-termination-default-billing-hour-then-random).",
        "note": "Standby and detach stay out of the body (budget); FAQ and cards do not need them. Session data off the instance is the transfer to chapter 29: an xref, no ElastiCache detail.",
    }))

S.append(sub(S11, "A mixed instances group adds Spot capacity on top of an On-Demand base",
    ["4.2.S2", "4.2.K9", "2.1.S2"],
    f("faq-single-group-mixed-purchase-options", "purchase-options-need-launch-template", "faq-on-demand-base-spot-above",
      "faq-all-spot-or-all-on-demand", "spot-price-capacity-optimized-recommended", "spot-lowest-price-not-recommended",
      "spot-capacity-optimized-pools", "=ec2-spot-be-flexible-types-and-azs", "=ec2-spot-discount-up-to-90-percent",
      "=ec2-spot-recommended-stateless-fault-tolerant-flexible", "=ec2-spot-not-suitable-stateful-inflexible",
      "spot-interruption-bypasses-all-protection", "spot-terminated-replacement",
      "no-capacity-rebalancing-replace-after-interruption", "capacity-rebalancing-spot",
      "capacity-rebalancing-exceeds-max-10-percent", "capacity-rebalancing-hook-under-two-minutes",
      "spot-rebalance-recommendation-and-two-minute-notice", "=ec2-spot-rebalance-recommendation-earlier-signal",
      "=ec2-spot-interruption-notice-two-minutes", "=ec2-spot-interruption-notice-channels",
      "lifecycle-hook-spot-two-minute-notice", "faq-instance-type-weights", "weights-equal-by-default",
      "weights-units-toward-desired", "weights-desired-in-units", "weights-can-exceed-max",
      "faq-ri-discount-applies-to-on-demand", "on-demand-prioritized-uses-reserved-instances",
      "termination-mixed-purchase-option-first", "wa-attribute-based-selection-newer-types",
      "faq-update-mixed-instances-settings", "change-price-capacity-optimized-2022",
      "capacity-reservation-types-supported", "odcr-no-term-commitment", "capacity-reservation-preference-values",
      "change-capacity-reservation-preference-2024"),
    4, 230, {
        "problem": "Spot Instances cost much less, but Amazon EC2 can take them back. A worker fleet wants the low price without losing all of its capacity at once.",
        "trace": [
            "**One group, two purchase options.** A group can use [On-Demand, RIs and Spot purchase options] with a [desired split between On-Demand and Spot capacity] (ec2-auto-scaling-faq-single-group-mixed-purchase-options), [only when you use a launch template] (ec2-auto-scaling-purchase-options-need-launch-template).",
            "**Base, then a percentage.** You let the [base capacity be fulfilled with On-Demand instances]; above it comes a [specified percentage mix of On-Demand or Spot instances] (ec2-auto-scaling-faq-on-demand-base-spot-above).",
            "**Spread over pools.** Be [flexible about which instance types you request] (ec2-spot-be-flexible-types-and-azs) and use the [price and capacity optimized allocation strategy] (ec2-auto-scaling-spot-price-capacity-optimized-recommended).",
            "**Replace early.** Capacity Rebalancing launches a new Spot Instance when one is [at an elevated risk of interruption] and [then terminates an earlier instance] (ec2-auto-scaling-capacity-rebalancing-spot); without it, replacement waits [until after the Amazon EC2 Spot service interrupts] (ec2-auto-scaling-no-capacity-rebalancing-replace-after-interruption).",
        ],
        "table": "Spot allocation strategies (columns: Strategy | Picks | AWS advice): price-capacity-optimized | pools [least likely to be interrupted] with a low price | recommended (ec2-auto-scaling-spot-price-capacity-optimized-recommended); capacity-optimized | the [most available pools] | for work that is expensive to restart (ec2-auto-scaling-spot-capacity-optimized-pools); lowest-price | the cheapest pools | not recommended: [highest risk of interruption] (ec2-auto-scaling-spot-lowest-price-not-recommended).",
        "why": "Why an On-Demand base? It keeps a floor of capacity when Spot capacity is reclaimed, because those interruptions [bypass all Amazon EC2 Auto Scaling protection mechanisms] (ec2-auto-scaling-spot-interruption-bypasses-all-protection).",
        "exam_signal": "\"stateless, fault-tolerant workers at the lowest cost\" points to Spot in a mixed instances group: AWS recommends Spot for [stateless, fault-tolerant, flexible applications] (ec2-spot-recommended-stateless-fault-tolerant-flexible); \"cannot be interrupted\" or \"stateful\" points to On-Demand: Spot is not for work that is [inflexible, stateful, fault-intolerant, or tightly coupled] (ec2-spot-not-suitable-stateful-inflexible).",
        "exam_trap": "auto-scaling-trap-lifecycle-hook-stops-spot",
        "spot_the_bug": "**Spot the bug.** A worker group runs only Spot Instances of one instance type in one Availability Zone, with the lowest-price allocation strategy. Workers are interrupted often. What is wrong? Reveal: one pool and lowest-price carry the [highest risk of interruption] (ec2-auto-scaling-spot-lowest-price-not-recommended); list several instance types and zones (ec2-spot-be-flexible-types-and-azs) and use price-capacity-optimized. About 55 words with the reveal.",
        "say_it": "The short answer is: keep an On-Demand base and add Spot above it across many instance types. The thing to watch is the short warning before Amazon EC2 takes a Spot Instance back.",
        "stop_and_answer": "A group has an On-Demand base of 2 and 50 percent Spot above the base. Desired capacity is 10. How many instances are On-Demand? Answer: 6, the base of 2 plus half of the other 8 (ec2-auto-scaling-faq-on-demand-base-spot-above). Write the reveal numbers without units.",
        "note": "Instance weights, Reserved Instance pricing and Capacity Reservations stay out of the body (budget); cards c018 and the FAQ carry the mixed-purchase facts. Chapter 41 owns purchase options: an xref.",
    }))

S.append(sub(S12, "Stopped instances belong in a warm pool not in the running group",
    ["4.2.K9", "4.2.S2", "2.1.K6"],
    f("vertical-resize-instance-type", "vertical-stop-required", "=ec2-resize-must-stop-instance",
      "vertical-stopped-group-instance-unhealthy", "cannot-hibernate-group-instance",
      "decision-guide-horizontal-for-fluctuating", "wa-stateless-scales-horizontally", "wa-stateless-servers-replaceable",
      "warm-pool-definition", "warm-pool-states", "warm-pool-stopped-instances-pay-volumes-only",
      "warm-pool-hibernated-ram", "warm-pool-ebs-root-required", "warm-pool-stop-ignores-user-data",
      "warm-pool-depleted-cold-start", "warm-pool-size-default", "warm-pool-reuse-policy", "warm-pool-unnecessary-cost",
      "warm-pool-no-spot-no-weights", "change-warm-pool-mixed-instances-2025", "=ec2-hibernate-saves-ram-to-root-volume",
      "=ec2-faq-hibernate-vs-stop-ram", "=ec2-hibernate-root-volume-requirements", "=ec2-hibernate-ram-limits-linux-windows",
      "=ec2-hibernate-max-duration", "=ec2-hibernate-no-instance-fee-ebs-rates",
      "=ec2-hibernate-supported-families-no-bare-metal", "=ec2-faq-hibernate-trigger-stopinstances",
      "wa-instance-scheduler-cannot-stop-group-instances", "ssm-parameter-no-warm-pools",
      "instance-refresh-warm-pool-order", "default-no-policies-fixed-size"),
    4, 230, {
        "problem": "Two ideas come up when instances are slow or idle: stop one and give it a larger instance type, or hibernate the instances at night. Inside a group, both stop an instance that the group expects to run.",
        "trace": [
            "**Scaling up stops the instance.** You resize by changing the instance type, and [You must stop your instance] first, so [plan for downtime] (ec2-auto-scaling-vertical-stop-required); in a group the group [marks the stopped instance as unhealthy] and may replace it (ec2-auto-scaling-vertical-stopped-group-instance-unhealthy).",
            "**Hibernating is not allowed in the group.** [You can't hibernate an instance] that is in an Auto Scaling group (ec2-auto-scaling-cannot-hibernate-group-instance).",
            "**Prepare instances in a warm pool.** A warm pool is a [pool of pre-initialized EC2 instances] beside the group (ec2-auto-scaling-warm-pool-definition), kept [Stopped, Running, or Hibernated] (ec2-auto-scaling-warm-pool-states); a Hibernated one can [save the contents of your RAM] (ec2-auto-scaling-warm-pool-hibernated-ram).",
            "**Scale out from the pool.** On scale-out the group takes pool instances, which [count toward the desired capacity] only when they leave the pool (ec2-auto-scaling-warm-pool-definition); an empty pool means a [cold start] (ec2-auto-scaling-warm-pool-depleted-cold-start).",
        ],
        "table": "Stop or hibernate (columns: Question | Stop | Hibernate): RAM | [RAM is cleared] | [the RAM data persisted] (ec2-faq-hibernate-vs-stop-ram); root volume | EBS for a pool instance: [only if it has an Amazon EBS volume] (ec2-auto-scaling-warm-pool-ebs-root-required) | an [EBS volume] that [must be encrypted] (ec2-hibernate-root-volume-requirements); while waiting you pay for | [pay only for the volumes that you use] and Elastic IP addresses (ec2-auto-scaling-warm-pool-stopped-instances-pay-volumes-only) | EBS storage, including the saved RAM (ec2-auto-scaling-warm-pool-hibernated-ram).",
        "why": "Why can the group not stop its own instances? It keeps [continues to maintain its desired capacity] of running instances (ec2-auto-scaling-default-no-policies-fixed-size); a stopped instance looks failed. Scaling out instead is [essential for dynamic workloads with fluctuating demands] (ec2-auto-scaling-decision-guide-horizontal-for-fluctuating).",
        "exam_signal": "\"instances take a long time to initialize, and scale-out must be fast at low cost\" points to a warm pool of stopped instances, [an effective way to minimize costs] (ec2-auto-scaling-warm-pool-states); \"keep the in-memory state while waiting\" points to Hibernated pool instances (ec2-auto-scaling-warm-pool-hibernated-ram).",
        "exam_trap": "auto-scaling-trap-scale-up-without-downtime",
        "say_it": "The short answer is: keep prepared instances stopped in a warm pool and let the group scale out. The thing to watch is cost when the first boot is already fast.",
        "stop_and_answer": "An application starts in 20 seconds, and users notice no delay when the group scales out. A colleague wants a warm pool. What do you say? Answer: probably not needed; a pool that is not required [can lead to unnecessary costs] (ec2-auto-scaling-warm-pool-unnecessary-cost).",
        "note": "Hibernation limits (RAM size, 60 days, families) belong to chapter 16: an xref, no numbers here. AWS Instance Scheduler [cannot stop and start instances] of a group (ec2-auto-scaling-wa-instance-scheduler-cannot-stop-group-instances): one clause only if words remain.",
    }))

S.append(sub(S13, "An instance refresh replaces running instances to roll out a new version",
    ["2.2.K7", "2.2.S1"],
    f("wa-immutable-infrastructure-definition", "wa-immutable-rollback-benefit", "instance-refresh-use-cases",
      "instance-refresh-rolling-default", "instance-refresh-min-max-healthy", "instance-refresh-min-healthy-percentage-default",
      "instance-refresh-max-healthy-percentage-default", "instance-refresh-ten-percent-at-a-time",
      "instance-refresh-launch-before-terminate", "instance-refresh-one-at-a-time", "instance-refresh-all-at-once",
      "instance-refresh-healthy-percentage-difference", "instance-refresh-warmup-default", "instance-refresh-checkpoints",
      "instance-refresh-checkpoints-default", "instance-refresh-checkpoint-delay-default",
      "instance-refresh-skip-matching-default", "instance-refresh-skip-matching-user-data-gap",
      "instance-refresh-auto-rollback-alarm", "instance-refresh-auto-rollback-default",
      "instance-refresh-cloudwatch-alarm-default", "instance-refresh-retry-timeout", "instance-refresh-max-duration",
      "instance-refresh-scale-out-uses-desired-config", "instance-refresh-standby-default",
      "instance-refresh-scale-in-protected-default", "replace-root-volume-preserves",
      "root-volume-replacement-keeps-instance-running", "root-volume-replacement-limits",
      "replace-root-volume-requirements", "max-instance-lifetime-purpose", "max-instance-lifetime-min-one-day",
      "max-instance-lifetime-replacement-uses-current-template", "max-instance-lifetime-honors-scale-in-protection",
      "max-instance-lifetime-clear-with-0", "max-instance-lifetime-not-at-console-create",
      "max-instance-lifetime-batch-replacement", "max-instance-lifetime-terminate-then-launch",
      "maintenance-policy-none-by-default", "maintenance-policy-custom", "maintenance-policy-low-min-healthy-faster",
      "maintenance-policy-does-not-block-scaling", "faq-codedeploy-cloudformation-for-changes",
      "faq-launch-configuration-change-existing-unaffected", "change-instance-refresh-rollback-2023",
      "change-instance-refresh-alarm-rollback-2023", "instance-refresh-warm-pool-order"),
    4, 230, {
        "problem": "A security patch is in a new AMI. Signing in to every instance to patch it is slow, and each instance drifts a little. Immutable infrastructure replaces instances instead of changing them.",
        "trace": [
            "**Build new, do not patch.** Immutable infrastructure means [no updates, security patches, or configuration changes] happen in place on production workloads (ec2-auto-scaling-wa-immutable-infrastructure-definition); a new launch template version holds the new AMI.",
            "**Start the refresh.** An instance refresh helps with [Deploying a new Amazon Machine Image (AMI)] (ec2-auto-scaling-instance-refresh-use-cases); by default it uses the [Rolling strategy (default)] (ec2-auto-scaling-instance-refresh-rolling-default).",
            "**Keep enough healthy.** The minimum healthy percentage defaults to [90 percent] (ec2-auto-scaling-instance-refresh-min-healthy-percentage-default) and the maximum to [100 percent] (ec2-auto-scaling-instance-refresh-max-healthy-percentage-default), so it replaces [10 percent] of the capacity at a time (ec2-auto-scaling-instance-refresh-ten-percent-at-a-time).",
            "**Roll back on trouble.** It can [Automatically roll back if the instance refresh fails] or when your alarm fires (ec2-auto-scaling-instance-refresh-auto-rollback-alarm), but auto rollback is [Disabled (false)] by default (ec2-auto-scaling-instance-refresh-auto-rollback-default).",
        ],
        "table": "Minimum healthy percentage and its effect (columns: Setting | Result): defaults, [90 percent] minimum (ec2-auto-scaling-instance-refresh-min-healthy-percentage-default) and [100 percent] maximum (ec2-auto-scaling-instance-refresh-max-healthy-percentage-default) | [10 percent] at a time (ec2-auto-scaling-instance-refresh-ten-percent-at-a-time); minimum [100 percent] | [Launch the new instances first] (ec2-auto-scaling-instance-refresh-launch-before-terminate); minimum and maximum both [100 percent] | one instance at a time (ec2-auto-scaling-instance-refresh-one-at-a-time); minimum [0 percent] | all instances at once (ec2-auto-scaling-instance-refresh-all-at-once).",
        "why": "Why replace instead of patch? With an immutable deployment [the previous working version is not changed] (ec2-auto-scaling-wa-immutable-rollback-benefit), so a rollback returns to something that worked.",
        "exam_signal": "\"roll out a new AMI to every instance of the group with minimal downtime\" points to an instance refresh (ec2-auto-scaling-instance-refresh-use-cases); \"deploy new application code to the instances\" points to [AWS CodeDeploy or CloudFormation] (ec2-auto-scaling-faq-codedeploy-cloudformation-for-changes).",
        "exam_trap": "auto-scaling-trap-update-template-updates-instances",
        "go_deeper": "Go deeper: checkpoints, skip matching, root volumes and lifetimes. A checkpoint [pauses for a specified amount of time] (ec2-auto-scaling-instance-refresh-checkpoints). Skip matching [doesn't check for code changes] from user data (ec2-auto-scaling-instance-refresh-skip-matching-user-data-gap). The replace root volume strategy works by [replacing only the root EBS volume] while the instance runs (ec2-auto-scaling-root-volume-replacement-keeps-instance-running), but [Root volume replacement doesn’t support Elastic Load Balancing] (ec2-auto-scaling-replace-root-volume-requirements). A maximum instance lifetime of [at least 86,400 seconds (one day)] replaces instances on a schedule (ec2-auto-scaling-max-instance-lifetime-min-one-day). At most 70 words.",
        "say_it": "The short answer is: put the change in a new template version and let an instance refresh replace the instances. The thing to watch is rollback, which is off by default.",
        "stop_and_answer": "A group of 20 instances starts an instance refresh with the default settings. How many instances does each step replace, and what happens when the new instances never pass their health checks? Answer: 2, which is [10 percent] (ec2-auto-scaling-instance-refresh-ten-percent-at-a-time); the group keeps retrying for [an hour] and then the refresh fails (ec2-auto-scaling-instance-refresh-retry-timeout).",
    }))

S.append({
    "file": "2-deep.md", "section": "numbers-that-decide-answers", "heading": "Numbers that decide answers", "bullets": [],
    "facts": f("default-cooldown-300-seconds", "grace-period-console-300-cli-0", "lifecycle-hook-heartbeat-timeout-default",
               "lifecycle-hook-default-result", "predictive-needs-24-hours-of-data", "lifecycle-hook-spot-two-minute-notice",
               "instance-refresh-min-healthy-percentage-default", "max-instance-lifetime-min-one-day",
               "cooldown-elb-deregistration-300-seconds", "quota-groups-per-region", "quota-scaling-policies-per-group",
               "quota-scheduled-actions-per-group", "quota-lifecycle-hooks-per-group", "quota-step-adjustments-per-policy",
               "predictive-forecast-next-48-hours", "predictive-forecast-updated-every-6-hours",
               "predictive-analyzes-up-to-14-days", "lifecycle-hook-heartbeat-timeout-range", "lifecycle-hook-global-timeout",
               "unhealthy-replacement-10-percent-at-a-time", "high-resolution-target-tracking",
               "instance-refresh-max-duration", "change-batch-termination-2026"),
    "status": "write", "minutes": 3,
    "plan": "Fixed H3 'A-list' (8 rows, each with one number card) and 'B-list' (12 rows); see numbers. At most 300 words. Under the B-list, one Changed recently entry that is not examinable yet (see changed_recently.deep_under_b_list), in the U3 form, only when fr-0064 is filled; otherwise leave it out (the fast Changed recently section then keeps its examinable entries, and no exempt sentence is needed).",
})
S.append({
    "file": "2-deep.md", "section": "decision-record", "heading": "Decision record",
    "bullets": ["3.2.S2", "4.2.S2", "2.2.S4"],
    "facts": f("default-no-policies-fixed-size", "wa-demand-based-pay-for-use", "billed-from-launch",
               "scheduled-vs-dynamic-when-to-use", "scheduled-action-sets-capacities", "scheduled-plus-policies-together",
               "faq-target-tracking-definition", "health-elb-check-must-be-turned-on", "default-instance-warmup-purpose",
               "warmup-instance-not-in-metrics", "predictive-long-initialization-fit", "scheduled-dst-location-time-zones",
               "scheduled-utc-default-time-zone", "resilience-practices"),
    "status": "write", "minutes": 3,
    "plan": "See story and decision_record. Fields in order: Context (at most 80 words, the trigger of the JSON), Requirement (the requirements of the Problem with the qualifier MOST cost-effective in capitals), Options (three list items after **Options.**, the choice in bold), Decision, Trade-off. Embed auto-scaling-before after Context and auto-scaling-after after Decision; keep both alts at about 30 words (alt text counts toward the 280 words). Every AWS reason carries a fact link; story numbers only from uses_numbers.",
})
S.append({
    "file": "2-deep.md", "section": "faq-quick-fire", "heading": "FAQ quick-fire", "bullets": [],
    "facts": f("faq-regional-spans-azs-not-regions", "faq-data-not-copied-to-new-instances",
               "faq-delete-group-terminates-instances", "faq-launch-configuration-one-and-immutable",
               "faq-no-elb-required-ec2-health-check", "faq-single-group-mixed-purchase-options",
               "faq-cannot-scale-past-ec2-limit", "faq-group-from-instance-no-new-ami",
               "faq-predictive-policy-vs-scaling-plan", "faq-does-not-add-volumes"),
    "status": "write", "minutes": 4,
    "plan": "Ten 'FAQ <n>.' prompts (see faq), each answered in one clause in its reveal and followed by an AWS quote block of whole sentences from the fact's evidence quote. At most 450 words.",
})

# ---------------------------------------------------------------- 2-services.md
S.append({
    "file": "2-services.md", "section": "aws-auto-scaling", "heading": "AWS Auto Scaling", "role": "card",
    "service": "aws-auto-scaling", "minutes": 1, "bullets": ["3.2.K4"],
    "facts": f("aa:faq-definition", "aa:faq-scaling-plan-definition", "aa:faq-scalable-resource-list",
               "aa:faq-creates-target-tracking-only", "aa:faq-three-scaling-strategies", "aa:faq-discovery-scans-stack-or-tags",
               "aa:faq-when-to-use", "aa:plans-prefer-native-predictive-policies", "aa:change-scaling-plan-migration-2024",
               "aa:faq-application-auto-scaling-for-non-ec2",
               "aa:wa-ec2-auto-scaling-for-instances-application-auto-scaling-for-other-services",
               "faq-use-ec2-vs-aws-auto-scaling", "aa:faq-free-cloudwatch-fees-apply", "aa:plans-one-plan-per-resource",
               "faq-groups-created-outside-aws-auto-scaling", "aa:aas-scalable-target-identity", "aa:aas-policy-types",
               "aa:aas-scalable-dimension-examples", "faq-predictive-policy-vs-scaling-plan"),
    "status": "write",
    "plan": """Service card D15, 150 to 220 words, flag <!-- section: role=card; route=full; minutes=1; service=aws-auto-scaling -->. What it is: AWS Auto Scaling lets you [scale collections of related resources] [across the full infrastructure stack] (aws-auto-scaling-faq-definition) with a scaling plan, a [collection of scaling instructions for multiple AWS resources] (aws-auto-scaling-faq-scaling-plan-definition). Stem signals (2 or 3 list items): 'scale the EC2 instances, DynamoDB tables and Aurora replicas of one application together' (aws-auto-scaling-faq-scalable-resource-list, aws-auto-scaling-faq-when-to-use); 'choose to optimize availability, cost, or a balance' ([optimize availability, optimize costs, or balance the two], aws-auto-scaling-faq-three-scaling-strategies). Do not confuse with: Amazon EC2 Auto Scaling (only EC2 groups: [only need to scale Amazon EC2 Auto Scaling], ec2-auto-scaling-faq-use-ec2-vs-aws-auto-scaling) and Application Auto Scaling (the API for one non-EC2 resource: [you can use the Application Auto Scaling API], aws-auto-scaling-faq-application-auto-scaling-for-non-ec2). One fact: a scaling plan creates [target tracking scaling policies only] (aws-auto-scaling-faq-creates-target-tracking-only); for predictive scaling alone AWS recommends policies [directly on your Auto Scaling resources instead] (aws-auto-scaling-plans-prefer-native-predictive-policies). Say it (at most 25 words): 'AWS Auto Scaling builds one scaling plan for the resources of one application. For a single EC2 group, use EC2 Auto Scaling.' Source: [What is a scaling plan?](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-a-scaling-plan.html).""",
})

# ---------------------------------------------------------------- traps
T = brief["traps"]


def trap(tid, belief, truth, facts, placed):
    T.append({"id": tid, "belief": belief, "truth": truth, "facts": facts, "placed_in": placed})


trap("auto-scaling-trap-elb-checks-on-by-default",
     "A group behind a load balancer replaces the instances that fail the load balancer's health checks, with the default settings.",
     "By default EC2 Auto Scaling ignores Elastic Load Balancing health checks and replaces only instances that the EC2 status checks find unhealthy; you must turn on the ELB health check type for the group.",
     f("elb-health-checks-ignored-by-default", "lb-default-ec2-checks-only", "health-elb-check-must-be-turned-on"),
     "1-fast.md#signals-and-traps")
trap("auto-scaling-trap-oldest-terminated-first",
     "On scale in, the group terminates its oldest instance first.",
     "The group balances Availability Zones first, whatever the termination policy; the default policy then removes an instance with an outdated configuration, then the one closest to the next billing hour, then one at random. OldestInstance is a policy that you choose.",
     f("termination-az-balance-first", "termination-default-zone-with-most", "termination-default-outdated-first",
       "termination-default-billing-hour-then-random", "termination-policy-oldest-instance"),
     "1-fast.md#signals-and-traps")
trap("auto-scaling-trap-hibernate-group-instance",
     "You can hibernate the instances of an Auto Scaling group at night to save cost.",
     "You cannot hibernate an instance in an Auto Scaling group: the group marks the stopped instance unhealthy and may replace it. Instances can wait Hibernated in a warm pool, and a scheduled action can lower capacity at night.",
     f("cannot-hibernate-group-instance", "warm-pool-hibernated-ram", "warm-pool-states", "scheduled-action-sets-capacities"),
     "1-fast.md#signals-and-traps")
trap("auto-scaling-trap-new-instance-data-copied",
     "A new instance that the group launches starts with the data of the instances that already run.",
     "Data is not automatically copied to new instances. Data that must survive belongs off the instance, in a service such as Amazon S3, Amazon RDS or Amazon DynamoDB.",
     f("faq-data-not-copied-to-new-instances", "faq-persist-data-off-instance"),
     "1-fast.md#signals-and-traps")
trap("auto-scaling-trap-group-spans-regions",
     "One Auto Scaling group can span two Regions, so it also gives disaster recovery.",
     "An Auto Scaling group is a Regional construct: it spans Availability Zones, not Regions. A second Region needs its own group.",
     f("faq-regional-spans-azs-not-regions"),
     "1-fast.md#signals-and-traps")
trap("auto-scaling-trap-launch-configuration-editable",
     "To give the group a new AMI, you edit its launch configuration.",
     "A launch configuration cannot be modified after you create it, and accounts created on or after October 1, 2024 cannot create one at all. A launch template takes a new version instead.",
     f("launch-config-immutable", "launch-configurations-blocked-for-new-accounts", "launch-template-versions"),
     D + S2)
trap("auto-scaling-trap-cooldown-for-all-policies",
     "Every scaling policy waits for the default cooldown of 300 seconds between scaling activities.",
     "The cooldown applies to simple scaling policies. Target tracking and step scaling policies can scale out without waiting for it; new instances get a warmup instead.",
     f("cooldown-applies-to-simple-scaling", "cooldown-target-tracking-step-do-not-wait", "default-cooldown-300-seconds"),
     D + S7)
trap("auto-scaling-trap-predictive-scales-in",
     "A predictive scaling policy on its own also removes capacity when the forecast expects less load.",
     "Predictive scaling does not scale in; you need a dynamic scaling policy, such as target tracking, to remove capacity.",
     f("predictive-does-not-scale-in", "combine-policy-types-predictive-plus-dynamic"),
     D + S8)
trap("auto-scaling-trap-queue-length-metric",
     "Target tracking on the number of visible messages in the queue scales a worker group correctly.",
     "The number of messages might not change proportionally to the size of the group. Scale on backlog per instance: the queue length divided by the InService instances.",
     f("sqs-queue-length-not-proportional", "sqs-backlog-per-instance"),
     D + S9)
trap("auto-scaling-trap-scale-in-protection-protects-all",
     "Scale-in protection keeps an instance safe from every kind of termination.",
     "Scale-in protection does not protect against health check replacement or manual termination, and Spot interruptions bypass every EC2 Auto Scaling protection. EC2 termination protection covers manual termination.",
     f("scale-in-protection-not-health-replacement", "scale-in-protection-ec2-termination-protection-for-manual",
       "spot-interruption-bypasses-all-protection"),
     D + S10)
trap("auto-scaling-trap-lifecycle-hook-stops-spot",
     "A termination lifecycle hook keeps a Spot Instance alive until its work is done.",
     "A lifecycle hook does not prevent a Spot Instance from terminating when Amazon EC2 needs the capacity back, with a two-minute interruption notice. Capacity Rebalancing launches a replacement earlier.",
     f("lifecycle-hook-spot-two-minute-notice", "capacity-rebalancing-spot"),
     D + S11)
trap("auto-scaling-trap-scale-up-without-downtime",
     "Moving to a larger instance type is a scaling step without downtime.",
     "You must stop an EBS-backed instance before you change its instance type, so you plan for downtime; in a group, the stopped instance is marked unhealthy. Scaling out with more instances fits fluctuating demand.",
     f("vertical-stop-required", "vertical-stopped-group-instance-unhealthy", "decision-guide-horizontal-for-fluctuating"),
     D + S12)
trap("auto-scaling-trap-update-template-updates-instances",
     "A new launch template version, or a new launch configuration, updates the instances that already run.",
     "Existing instances are not affected (AWS says so for a launch configuration); only new and replacement instances use the current settings. An instance refresh replaces the running instances.",
     f("faq-launch-configuration-change-existing-unaffected", "health-replacement-uses-current-settings",
       "instance-refresh-use-cases"),
     D + S13)

brief["traps_from_other_chapters"] = {
    "rule": "Question writers can tag a distractor with a trap id of another chapter when the distractor states exactly that trap's belief (lint.traps() knows them). Q205 needs a trap id on at least half of the wrong options; reuse is allowed. Candidates that fit Auto Scaling stems:",
    "ids": [
        "elb-trap-lb-replaces-instance",
        "elb-trap-all-unhealthy-stops-traffic",
        "elb-trap-sticky-sessions-keep-state",
        "elb-trap-one-az-enough",
        "aws-map-trap-one-az-is-highly-available",
        "aws-map-trap-multi-region-for-high-availability",
        "how-the-exam-asks-trap-cheapest-wins",
        "how-the-exam-asks-trap-works-means-correct",
        "how-the-exam-asks-trap-ha-equals-ft",
        "how-the-exam-asks-trap-always-max-availability",
        "how-the-exam-asks-trap-keyword-bait",
        "iam-trap-keys-on-instance",
    ],
}

# ---------------------------------------------------------------- compare tables, signals, words
brief["compare_tables"] = [
    {
        "title": "EC2 Auto Scaling, Application Auto Scaling or AWS Auto Scaling",
        "section": "1-fast.md#choose-it-or-not",
        "neighbours": ["Amazon EC2 Auto Scaling", "Application Auto Scaling", "AWS Auto Scaling"],
        "rows": "Columns: Question | EC2 Auto Scaling | Application Auto Scaling | AWS Auto Scaling (4 columns). Scales: EC2 instances in Auto Scaling groups | other resources such as [Amazon ECS services, Amazon EC2 Spot fleets] and [provisioned read and write capacity for Amazon DynamoDB] (aws-auto-scaling-faq-application-auto-scaling-for-non-ec2) | [scale collections of related resources] (aws-auto-scaling-faq-definition). Policies: target tracking, step, simple, scheduled, predictive (ec2-auto-scaling-scaling-methods) | [Target tracking scaling], [Step scaling], [Scheduled scaling], [Predictive scaling] (aws-auto-scaling-aas-policy-types) | [target tracking scaling policies only] (aws-auto-scaling-faq-creates-target-tracking-only). Choose it for: [only need to scale Amazon EC2 Auto Scaling] groups or fleet health | one AWS service other than EC2 ([For other AWS services, use Application Auto Scaling], aws-auto-scaling-wa-ec2-auto-scaling-for-instances-application-auto-scaling-for-other-services) | [multiple resources across multiple services] (ec2-auto-scaling-faq-use-ec2-vs-aws-auto-scaling).",
        "deciding_question": "Does only an EC2 fleet scale, one other AWS resource, or several resources of one application together?",
    },
    {
        "title": "Scale out or scale up",
        "section": "1-fast.md#choose-it-or-not",
        "neighbours": ["horizontal scaling (scale out)", "vertical scaling (scale up)"],
        "rows": "Columns: Question | Scale out (horizontal) | Scale up (vertical) (3 columns). How: add instances to a group | [resize your instance by changing its instance type] (ec2-auto-scaling-vertical-resize-instance-type). Downtime: the other instances keep serving; stateless servers can be [replaced at will without causing an availability impact] (ec2-auto-scaling-wa-stateless-servers-replaceable) | [You must stop your instance], so [plan for downtime] (ec2-auto-scaling-vertical-stop-required). Fluctuating demand: [essential for dynamic workloads with fluctuating demands] (ec2-auto-scaling-decision-guide-horizontal-for-fluctuating) | one size all day. Needs: an application that keeps no state on the instance: stateless applications [they can scale horizontally] (ec2-auto-scaling-wa-stateless-scales-horizontally) | nothing new in the application.",
        "deciding_question": "Can the application run as several identical copies, or must one instance grow?",
    },
    {
        "title": "Which scaling method",
        "section": "1-fast.md#choose-it-or-not",
        "neighbours": ["dynamic scaling (target tracking)", "scheduled scaling", "predictive scaling"],
        "rows": "Columns: Question | Target tracking | Scheduled action | Predictive scaling (4 columns). Acts: [when the metric deviates from the target] (ec2-auto-scaling-target-tracking-service-manages-alarms) | at a date and time it sets [desired, minimum, and maximum capacity] (ec2-auto-scaling-scheduled-action-sets-capacities) | [proactively increase capacity ahead of upcoming demand] (ec2-auto-scaling-faq-predictive-ahead-of-demand). Fits: [you don't know when the traffic will change] | [the need arises on a predictable schedule] (ec2-auto-scaling-scheduled-vs-dynamic-when-to-use) | regular patterns, apps that [take a long time to initialize] (ec2-auto-scaling-predictive-long-initialization-fit). Scales in: yes, [scaling in more gradually when traffic is decreasing] (ec2-auto-scaling-target-tracking-scale-in-gradual) | when a later action lowers the numbers | no: [it will not scale in to remove capacity] (ec2-auto-scaling-predictive-does-not-scale-in). Needs: a metric that falls as instances are added | a schedule | [at least 24 hours of data] (ec2-auto-scaling-predictive-needs-24-hours-of-data).",
        "deciding_question": "Is the load change a surprise, a known time, or a pattern that repeats?",
    },
]

brief["signals"] = [
    {"stem": "instances fail the load balancer health checks but are never replaced",
     "think": "turn on the ELB health check type of the group",
     "fact": A + "health-elb-check-must-be-turned-on",
     "but_not_if": "you need the instance for inspection: put it in Standby, where it [do not actively handle load balancer traffic] (ec2-auto-scaling-standby-no-lb-traffic), or suspend the health checks (ec2-auto-scaling-faq-suspend-health-checks)"},
    {"stem": "traffic rises at the same time every weekday",
     "think": "a scheduled action before the peak, plus target tracking",
     "fact": A + "scheduled-vs-dynamic-when-to-use",
     "but_not_if": "the time moves but the daily or weekly pattern repeats: predictive scaling plus a dynamic policy (ec2-auto-scaling-wa-predictive-patterns-vs-scheduled-times)"},
    {"stem": "keep average CPU utilization at 50% with the least effort",
     "think": "a target tracking scaling policy",
     "fact": A + "faq-target-tracking-definition",
     "but_not_if": "the work waits in a queue: scale on backlog per instance (ec2-auto-scaling-sqs-backlog-per-instance)"},
    {"stem": "workers process messages from an SQS queue at a rate that varies",
     "think": "target tracking on backlog per instance",
     "fact": A + "sqs-backlog-per-instance",
     "but_not_if": "the rate of jobs never changes: a fixed-size group is enough (ec2-auto-scaling-sqs-dynamic-scaling-when-load-varies)"},
    {"stem": "instances take a long time to initialize, so scale-out is slow",
     "think": "a warm pool of stopped or hibernated instances",
     "fact": A + "warm-pool-definition",
     "but_not_if": "first boot causes no noticeable latency: a warm pool [can lead to unnecessary costs] (ec2-auto-scaling-warm-pool-unnecessary-cost)"},
    {"stem": "lowest cost for stateless workers that can tolerate interruption",
     "think": "Spot above an On-Demand base, several instance types, price-capacity-optimized",
     "fact": A + "spot-price-capacity-optimized-recommended",
     "but_not_if": "the work is stateful or cannot be interrupted: On-Demand (ec2-spot-not-suitable-stateful-inflexible)"},
    {"stem": "roll out a new AMI to every instance with minimal downtime",
     "think": "a new launch template version and an instance refresh",
     "fact": A + "instance-refresh-use-cases",
     "but_not_if": "only application code changes: [AWS CodeDeploy or CloudFormation] (ec2-auto-scaling-faq-codedeploy-cloudformation-for-changes)"},
    {"stem": "save logs or finish a job before an instance is terminated",
     "think": "a termination lifecycle hook",
     "fact": A + "termination-hook-extends-life",
     "but_not_if": "Amazon EC2 reclaims a Spot Instance: a hook does not stop that; act on the [two-minute interruption notice] (ec2-auto-scaling-lifecycle-hook-spot-two-minute-notice)"},
]

brief["words_table"] = [
    {"term": "Auto Scaling group", "collocation": "set the desired capacity (bold: set)"},
    {"term": "scale out", "collocation": "scale out on a metric (bold: metric)"},
    {"term": "scale up", "collocation": "scale up the database instance (bold: instance)"},
    {"term": "health check", "collocation": "fail a health check (bold: fail)"},
    {"term": "stateless", "collocation": "a stateless application tier (bold: tier)"},
    {"term": "decouple", "collocation": "decouple the tiers with a queue (bold: tiers)"},
    {"term": "single point of failure", "collocation": "remove a single point of failure (bold: remove)"},
    {"term": "deregistration delay", "collocation": "the target drains during the deregistration delay (bold: drains)"},
]

# ---------------------------------------------------------------- numbers
brief["numbers"] = {
    "a_list": [
        {"display": "300 seconds", "fact": A + "default-cooldown-300-seconds", "card": "auto-scaling-c007",
         "what": "default cooldown", "why": "only simple scaling waits for it; step scaling and target tracking use warmup"},
        {"display": "300 seconds / 0 seconds", "fact": A + "grace-period-console-300-cli-0", "card": "auto-scaling-c008",
         "what": "health check grace period: console / AWS CLI or SDK",
         "why": "a group made with the CLI can replace a new instance that is still starting; two links in one cell, one per value"},
        {"display": "3600 seconds", "fact": A + "lifecycle-hook-heartbeat-timeout-default", "card": "auto-scaling-c009",
         "what": "default heartbeat timeout of a lifecycle hook",
         "why": "then the default result [ABANDON] applies (ec2-auto-scaling-lifecycle-hook-default-result)"},
        {"display": "at least 24 hours of data", "fact": A + "predictive-needs-24-hours-of-data", "card": "auto-scaling-c010",
         "what": "history that predictive scaling needs", "why": "a new group cannot forecast on its first day"},
        {"display": "two-minute interruption notice", "fact": A + "lifecycle-hook-spot-two-minute-notice",
         "card": "auto-scaling-c011", "what": "warning before Amazon EC2 reclaims a Spot Instance",
         "why": "a lifecycle hook cannot hold a Spot Instance longer"},
        {"display": "90 percent", "fact": A + "instance-refresh-min-healthy-percentage-default", "card": "auto-scaling-c012",
         "what": "default minimum healthy percentage of an instance refresh",
         "why": "the refresh replaces [10 percent] at a time (ec2-auto-scaling-instance-refresh-ten-percent-at-a-time)"},
        {"display": "86,400 seconds", "fact": A + "max-instance-lifetime-min-one-day", "card": "auto-scaling-c013",
         "what": "shortest maximum instance lifetime", "why": "the fastest scheduled replacement is daily"},
        {"display": "300 seconds", "fact": A + "cooldown-elb-deregistration-300-seconds", "card": "auto-scaling-c014",
         "what": "default deregistration delay (connection draining)", "why": "in-flight requests get this long on scale in"},
    ],
    "b_list": [
        {"display": "500 Auto Scaling groups", "fact": A + "quota-groups-per-region", "what": "default per Region, adjustable"},
        {"display": "50 scaling policies", "fact": A + "quota-scaling-policies-per-group", "what": "per group, fixed"},
        {"display": "125 scheduled actions", "fact": A + "quota-scheduled-actions-per-group", "what": "per group, fixed"},
        {"display": "50 lifecycle hooks", "fact": A + "quota-lifecycle-hooks-per-group", "what": "per group, fixed"},
        {"display": "20 step adjustments", "fact": A + "quota-step-adjustments-per-policy", "what": "per step scaling policy"},
        {"display": "48 hours", "fact": A + "predictive-forecast-next-48-hours", "what": "predictive forecast horizon"},
        {"display": "every 6 hours", "fact": A + "predictive-forecast-updated-every-6-hours", "what": "forecast update"},
        {"display": "14 days", "fact": A + "predictive-analyzes-up-to-14-days", "what": "history that predictive scaling reads"},
        {"display": "30 to 7200 seconds", "fact": A + "lifecycle-hook-heartbeat-timeout-range",
         "what": "heartbeat timeout range; global limit [48 hours] (ec2-auto-scaling-lifecycle-hook-global-timeout)"},
        {"display": "10 percent", "fact": A + "unhealthy-replacement-10-percent-at-a-time",
         "what": "share of desired capacity replaced at a time when instances are unhealthy"},
        {"display": "lowest supported interval is 10 seconds", "fact": A + "high-resolution-target-tracking",
         "what": "high-resolution target tracking"},
        {"display": "14 days", "fact": A + "instance-refresh-max-duration", "what": "longest instance refresh"},
    ],
    "not_used": "Application Auto Scaling and scaling plan quotas (aws-auto-scaling-quota-*) and the per-call API limits (attach, detach, standby) decide no exam answer; they stay out.",
}

brief["changed_recently"] = {
    "fast": [
        {"date": "2024-10-01", "what": "New accounts cannot create launch configurations",
         "fact": A + "launch-configurations-blocked-for-new-accounts",
         "old_display": "pending fr-0062 (changed.was)",
         "now_display": "cannot create new launch configurations using any method",
         "exam_probably_expects": "older questions may build a group from a launch configuration; today choose a launch template, and never an answer that edits a launch configuration ([can't modify a launch configuration], ec2-auto-scaling-launch-config-immutable)",
         "status": "examinable",
         "pending": "fr-0062 (changed.date 2024-10-01 and changed.was with evidence); until filled, write the Old line with <!-- needs-display --> or leave the entry planned"},
        {"date": "2022-11-10", "what": "The price-capacity-optimized Spot allocation strategy",
         "fact": A + "change-price-capacity-optimized-2022",
         "old_display": "not available. (fixed text, no link)",
         "now_display": "price and capacity optimized allocation strategy",
         "exam_probably_expects": "older questions may treat lowest-price or capacity-optimized as the best answer; today AWS recommends price-capacity-optimized (ec2-auto-scaling-spot-price-capacity-optimized-recommended)",
         "status": "examinable",
         "pending": "fr-0063 (changed.date 2022-11-10); until filled, leave the entry planned"},
        {"date": "2023-01-06", "what": "Predictive scaling forecasts update every six hours",
         "fact": A + "change-predictive-forecasts-every-six-hours",
         "old_display": "daily", "now_display": "update every six hours",
         "exam_probably_expects": "either value; it rarely decides an answer, and a forecast still needs history first",
         "status": "examinable", "pending": None,
         "note": "Ready: the fact has changed.date 2023-01-06 and changed.was 'daily'."},
    ],
    "deep_under_b_list": [
        {"date": "2026-08-17", "what": "Batch termination of up to 100 instances in one call",
         "fact": A + "change-batch-termination-2026",
         "old_display": "pending fr-0064 (changed.was: one instance ID per call)",
         "now_display": "up to 100 instance IDs",
         "exam_probably_expects": "one instance per TerminateInstanceInAutoScalingGroup call, if a question asks. Do not let this number decide an answer.",
         "status": "not examinable yet",
         "note": "GA after the cut-off 2026-07-15. Write it only when fr-0064 is filled."},
    ],
    "considered_not_used": [
        {"fact": A + "change-instance-refresh-cloudformation-2026", "why": "2026-07-29, after the cut-off: not examinable yet; no answer depends on it"},
        {"fact": A + "az-distribution-reservations-then-balanced", "why": "2026-06-30, inside the window but niche; no answer depends on it"},
        {"fact": A + "change-instance-maintenance-policy-2023", "why": "taught as current truth (Go deeper of the health check subsection); no changed record"},
        {"fact": A + "change-ssm-parameter-ami-2023", "why": "taught as current truth (exam signal of the launch template subsection)"},
        {"fact": A + "change-target-tracking-metric-math-2022", "why": "taught as current truth (Go deeper of the target tracking subsection)"},
        {"fact": A + "high-resolution-target-tracking", "why": "taught as current truth (Go deeper and B-list)"},
        {"fact": A + "zonal-shift-launches-only-in-healthy-azs", "why": "one optional sentence in the zone subsection; chapter 14 and 40 own zonal shift"},
        {"fact": A + "change-warm-pool-mixed-instances-2025", "why": "niche; warm pool limits stay out of the body"},
        {"fact": A + "lifecycle-hook-lambda-direct-target", "why": "niche; notification targets are one clause"},
        {"fact": A + "root-volume-replacement-keeps-instance-running", "why": "2025-11-20, one clause in a Go deeper block"},
        {"fact": A + "instance-lifecycle-policy-retains-on-abandon", "why": "2025-11-20, niche"},
        {"fact": A + "synchronous-provisioning-launchinstances", "why": "2025-11-18, niche"},
        {"fact": AA + "change-scaling-plan-migration-2024", "why": "service card fact; AWS points scaling plan users to native predictive policies"},
    ],
}

# ---------------------------------------------------------------- FAQ
FAQ = "https://aws.amazon.com/ec2/autoscaling/faqs/"
brief["faq"] = [
    {"n": 1, "q": "Can one Auto Scaling group span two AWS Regions?", "answer": "No; it spans Availability Zones in one Region",
     "fact": A + "faq-regional-spans-azs-not-regions", "url": FAQ},
    {"n": 2, "q": "Is the data on a running instance copied to the new instances that the group launches?",
     "answer": "No; use lifecycle hooks or keep the data off the instance", "fact": A + "faq-data-not-copied-to-new-instances", "url": FAQ},
    {"n": 3, "q": "What happens to the running instances when you delete their Auto Scaling group?",
     "answer": "They are terminated", "fact": A + "faq-delete-group-terminates-instances", "url": FAQ},
    {"n": 4, "q": "Can you change a launch configuration after you create it?",
     "answer": "No; create a new one and update the group", "fact": A + "faq-launch-configuration-one-and-immutable", "url": FAQ},
    {"n": 5, "q": "Do you need Elastic Load Balancing to use EC2 Auto Scaling?",
     "answer": "No; the EC2 health check finds and replaces unhealthy instances", "fact": A + "faq-no-elb-required-ec2-health-check", "url": FAQ},
    {"n": 6, "q": "Can one group mix On-Demand Instances, Reserved Instances and Spot Instances?",
     "answer": "Yes, with a split that you choose", "fact": A + "faq-single-group-mixed-purchase-options", "url": FAQ},
    {"n": 7, "q": "Can a group scale past the account's EC2 instance limit?",
     "answer": "No; request a higher EC2 limit", "fact": A + "faq-cannot-scale-past-ec2-limit", "url": FAQ},
    {"n": 8, "q": "When you create a group from an existing instance, is a new AMI created?",
     "answer": "No", "fact": A + "faq-group-from-instance-no-new-ami", "url": FAQ},
    {"n": 9, "q": "Do you need an AWS Auto Scaling scaling plan to use predictive scaling for a group?",
     "answer": "No; predictive scaling is a native policy of EC2 Auto Scaling", "fact": A + "faq-predictive-policy-vs-scaling-plan", "url": FAQ},
    {"n": 10, "q": "Does EC2 Auto Scaling add an EBS volume when the disk of an instance fills up?",
     "answer": "No; it attaches volumes only to the new instances that it launches", "fact": A + "faq-does-not-add-volumes", "url": FAQ},
]
brief["faq_alternatives"] = [A + "faq-suspend-health-checks", A + "faq-ri-discount-applies-to-on-demand",
                             A + "faq-cloudwatch-agent-from-ami", A + "faq-without-elb-route53-or-proxy"]

# ---------------------------------------------------------------- story and decision record
brief["story"] = {
    "stage": 2, "month": 11,
    "trigger": "The same load test. Traffic also has a fixed shape: the peak comes from 09:00 to 11:00 Eastern on weekdays.",
    "problem": "Callvale's web tier needs 3 instances at night and up to 12 at peak. The peak comes every weekday from 09:00 to 11:00. A new instance needs 4 minutes before it serves traffic. Callvale must replace failed instances automatically and must not pay for 12 instances all day.",
    "uses_numbers": ["web_group_min", "web_group_max", "web_group_scheduled_capacity", "web_group_scheduled_time",
                     "instance_start_minutes", "peak_window", "worker_group_max"],
    "state_at_month_11": "Stage 2, story order ... 10, 26, 14, 17, 15, 13. Before this chapter: one custom VPC with private application subnets in AZ 1, AZ 2 and AZ 3 (chapter 10; stage 2 uses three zones); instances built from an AMI with a launch template and Session Manager (chapter 16); Amazon RDS for PostgreSQL Multi-AZ (chapter 26); IAM roles (chapter 03); an Application Load Balancer in three zones with one web instance in each, a target group with health checks, and sticky sessions (chapter 14, decided at the same load test). No CloudFront and no Route 53 hosted zone yet (chapters 15 and 13 come after). No queues, no Lambda functions and no conversion worker group yet (chapters 31 and 18, month 12).",
    "rules": "Question stems never name Callvale. The story never teaches a fact. Ben's question is the speak item auto-scaling-s01; it matches trap elb-trap-lb-replaces-instance of chapter 14, which questions and cards here reuse instead of a second trap with the same belief. No dollar amounts in story text. The worker group (0 to 40) appears only in the 'later' sentence.",
}
brief["decision_record"] = {
    "status": "write",
    "context": "The trigger of data/startup.json chapter 17, at most 80 words: the same load test as chapter 14; the peak comes every weekday from 09:00 to 11:00 (peak_window); a new web instance needs 4 minutes before it serves traffic (instance_start_minutes); the web tier needs 3 instances at night and up to 12 at peak (web_group_min, web_group_max).",
    "requirement": "Replace failed instances automatically, have capacity in service when the weekday peak starts, and not pay for 12 instances all day, in the MOST cost-effective way (qualifier of the JSON: most cost-effective).",
    "options": ["12 instances all the time", "scheduled scaling only",
                "target tracking plus a scheduled action at 08:45 on weekdays (chosen)"],
    "requirement_qualifier": "MOST cost-effective",
    "reasons_with_facts": [
        "Option 1: a group with no policy keeps [maintain a fixed size] and replaces failed instances (ec2-auto-scaling-default-no-policies-fixed-size), but pays for idle capacity at night: instances are billed [as soon as they are launched] (ec2-auto-scaling-billed-from-launch), while supplying resources by demand means you [pay for the resources you use only] (ec2-auto-scaling-wa-demand-based-pay-for-use).",
        "Option 2: a schedule fits the morning because [the need arises on a predictable schedule], but launch week and other spikes come when [you don't know when the traffic will change] (ec2-auto-scaling-scheduled-vs-dynamic-when-to-use); a schedule alone does not follow them.",
        "Option 3: the scheduled action sets [desired, minimum, and maximum capacity] at 08:45 (ec2-auto-scaling-scheduled-action-sets-capacities), and you can [use scheduled scaling and scaling policies together] (ec2-auto-scaling-scheduled-plus-policies-together); target tracking [adjusts the number of EC2 instances] around the target (ec2-auto-scaling-faq-target-tracking-definition). The group uses the ELB health check type ([you must turn it on], ec2-auto-scaling-health-elb-check-must-be-turned-on) and a default instance warmup that matches the 4-minute start (ec2-auto-scaling-default-instance-warmup-purpose).",
    ],
    "tradeoff": "A sudden spike is still served late by about 4 minutes, so the minimum stays at 3. AWS reason: metric-based scaling is [which is reactive in nature] (ec2-auto-scaling-predictive-long-initialization-fit), and a new instance is [not counted toward the aggregated EC2 instance metrics] until its warmup ends (ec2-auto-scaling-warmup-instance-not-in-metrics).",
    "also_added": "One sentence after the Decision: the scheduled action uses the time zone America/New_York, because recurring actions otherwise use [Coordinated Universal Time (UTC)] (ec2-auto-scaling-scheduled-utc-default-time-zone) and a location-based zone can [automatically adjust for DST] (ec2-auto-scaling-scheduled-dst-location-time-zones); the group keeps one instance in each of the three zones at night ([at least one instance in each Availability Zone], ec2-auto-scaling-resilience-practices).",
    "later": "One sentence at most: after launch day, a second group of conversion workers (0 to 40) scales on the backlog of the convert queue (chapter 31); at stage 3 the web group is retired when the services move to AWS Fargate (chapter 19), and the worker group stays. No new option in the record.",
    "diagrams": ["auto-scaling-before", "auto-scaling-after"],
    "story_conflict": "data/startup.json chapter 17 'diagram' says 'Before: one fixed instance', but chapter 14 left one web instance in each of three zones (fixed capacity of 3). The before diagram therefore says 'fixed capacity' and names no count; reported in notes_for_orchestrator.",
}
brief["realworld"] = {
    "status": "optional",
    "company": "NASA JPL",
    "facts": [A + "case-nasa-jpl-spot-fleets"],
    "point": "NASA JPL processes satellite data on [automatic scaling fleets]: Spot Instances for the fault-tolerant processing and On-Demand Instances with Capacity Reservations for critical processing (ec2-auto-scaling-case-nasa-jpl-spot-fleets). One AWS quote block of one whole sentence of the fact's evidence, at most 25 words. It shows: an On-Demand base for critical work and Spot for the rest. Never part of Callvale's story. Alternative: Canva (ec2-auto-scaling-case-canva-46-percent-purchase-mix).",
    "rule": "Write it only if 2-deep.md stays at or under 4,380 words without it. It is not in the sections list, so leaving it out is no L905 error.",
}

# ---------------------------------------------------------------- devices
brief["devices"] = {
    "exam_trap_callouts_2_deep": {
        S2: "auto-scaling-trap-launch-configuration-editable",
        S7: "auto-scaling-trap-cooldown-for-all-policies",
        S8: "auto-scaling-trap-predictive-scales-in",
        S9: "auto-scaling-trap-queue-length-metric",
        S10: "auto-scaling-trap-scale-in-protection-protects-all",
        S11: "auto-scaling-trap-lifecycle-hook-stops-spot",
        S12: "auto-scaling-trap-scale-up-without-downtime",
        S13: "auto-scaling-trap-update-template-updates-instances",
    },
    "exam_trap_form": "> **Exam trap:** <wrong belief in plain words>. <truth with its fact link>. <!-- trap: <id> -->  Each one adds a new case; never restate the table above it.",
    "fast_traps_list": [
        "auto-scaling-trap-elb-checks-on-by-default",
        "auto-scaling-trap-oldest-terminated-first",
        "auto-scaling-trap-hibernate-group-instance",
        "auto-scaling-trap-new-instance-data-copied",
        "auto-scaling-trap-group-spans-regions",
    ],
    "go_deeper": [
        S2 + ": $Latest, PassRole and AMI parameters",
        S5 + ": how fast the group replaces",
        S6 + ": target values, metric math and seconds",
        S13 + ": checkpoints, skip matching, root volumes and lifetimes",
    ],
    "spot_the_bug": [
        S5 + ": a group made with the AWS CLI that keeps a grace period of zero and replaces starting instances",
        S11 + ": Spot workers of one instance type in one zone with lowest-price",
    ],
    "try_it": [S1 + ": auto-scaling-t02", S6 + ": auto-scaling-t03"],
    "startup_example_2_deep": [S8 + ": Callvale's scheduled action at 08:45, target tracking above it (at most 25 words)"],
    "predict_the_picture": "In one breath: 'When traffic rises, which part decides that the group needs another instance, and which part launches it?' before the hero auto-scaling-hero (LEARNING device 6).",
    "route_pass_subsections": [S5, S6, S8, S9],
    "xref_markers": [
        "03 IAM (instance profiles and iam:PassRole)",
        "10 VPC (subnets in three Availability Zones)",
        "14 Elastic Load Balancing (target groups, health checks, deregistration delay, the trap elb-trap-lb-replaces-instance)",
        "16 EC2 (AMIs, launch templates, hibernation limits, Spot interruptions, instance types)",
        "18 Lambda (functions as lifecycle hook targets)",
        "19 Containers (ECS service auto scaling; the web group moves to Fargate at stage 3)",
        "29 ElastiCache (session data off the instance)",
        "31 SQS, SNS and EventBridge (the queue between the tiers; EventBridge events of Auto Scaling)",
        "37 CloudWatch (alarms and metrics behind scaling policies)",
        "38 CloudFormation and Systems Manager (deployments; AMI parameters)",
        "40 HA and DR (static stability, a second Region)",
        "41 Cost optimization (Spot, Savings Plans, right sizing)",
    ],
}

# ---------------------------------------------------------------- question slots
QS = []


def slot(sid, bullet, concept, diff, typ, layer, ee, section, trap_id, note, **extra):
    row = {"id": sid, "bullet": bullet, "concept": concept, "difficulty": diff, "type": typ, "layer": layer,
           "exam_english": ee, "section": section, "trap": trap_id, "note": note}
    row.update(extra)
    QS.append(row)


slot("q01", "3.2.K4", "application-auto-scaling-for-non-ec2", 1, "single", "core", [], SVC, None,
     "A company runs an Amazon ECS service and an Amazon DynamoDB table in provisioned mode; it wants the number of tasks and the read and write capacity to follow the load. Which AWS service scales these resources? (qualifier none, difficulty 1). Key: Application Auto Scaling (aws-auto-scaling-faq-application-auto-scaling-for-non-ec2, aws-auto-scaling-aas-scalable-dimension-examples). Distractors: an EC2 Auto Scaling group for the tasks and the table (misconception: EC2 Auto Scaling scales EC2 groups, ec2-auto-scaling-faq-use-ec2-vs-aws-auto-scaling); Elastic Load Balancing (misconception: a load balancer spreads traffic, it adds no capacity); an AWS Auto Scaling scaling plan with step scaling policies (impossible feature: [target tracking scaling policies only], aws-auto-scaling-faq-creates-target-tracking-only).")
slot("q02", "2.2.S4", "elb-health-check-type", 2, "single", "core", ["ee-ensure", "ee-least-operational-overhead"], D + S5,
     "auto-scaling-trap-elb-checks-on-by-default",
     "Strict twin A (with q06). Shared stem: a web application runs on EC2 instances in an Auto Scaling group behind an Application Load Balancer; the group keeps its default health check settings; the company must ensure that failed instances are replaced automatically with the LEAST operational overhead. Changed phrase of q02: 'Sometimes the application on an instance stops answering HTTP requests, but the instance keeps running.' Shared options (identical in q06): A 'Turn on Elastic Load Balancing health checks for the Auto Scaling group.' B 'Keep the current health check settings of the Auto Scaling group.' C 'Create a CloudWatch alarm on the instance status check that reboots the instance.' D 'Increase the health check grace period of the Auto Scaling group.' Key A (ec2-auto-scaling-elb-health-checks-ignored-by-default, ec2-auto-scaling-health-elb-check-must-be-turned-on, ec2-auto-scaling-health-elb-unhealthy-replaced). B carries this trap; C misconception (a reboot does not replace, ec2-alarm-reboot-instance-check-recover-system-check); D misconception (the grace period only delays health-based termination, ec2-auto-scaling-grace-period-definition). Distractor trap for an option that says the load balancer replaces the instance: elb-trap-lb-replaces-instance.",
     twin="q06", twin_kind="strict")
slot("q03", "3.2.S2", "scheduled-plus-target-tracking", 2, "single", "core", ["ee-most-cost-effective", "ee-predictable"], D + S8,
     "auto-scaling-trap-predictive-scales-in",
     "Strict twin B (with q07). Shared stem: web instances in an Auto Scaling group; a new instance needs several minutes before it serves traffic; 'The company must have enough capacity in service when traffic rises and must not pay for peak capacity while traffic is low.' MOST cost-effective. Changed phrase of q03: 'Traffic rises to a peak from 09:00 to 11:00 every weekday.' Shared options: A 'A target tracking scaling policy on average CPU utilization only.' B 'A scheduled action that raises capacity before 09:00 on weekdays, plus a target tracking scaling policy on average CPU utilization.' C 'A predictive scaling policy only, which adds and removes instances from its forecast.' D 'A fixed group size that matches the peak load.' Key B (ec2-auto-scaling-scheduled-vs-dynamic-when-to-use, ec2-auto-scaling-scheduled-plus-policies-together). C carries this trap (ec2-auto-scaling-predictive-does-not-scale-in); A reacts after the rise (ec2-auto-scaling-predictive-long-initialization-fit, violates the requirement); D violates cost (trap how-the-exam-asks-trap-always-max-availability fits only if the option text says 'maximum availability').",
     twin="q07", twin_kind="strict")
slot("q04", "2.1.K6", "scale-out-vs-scale-up", 1, "single", "core", ["ee-minimal-downtime"], D + S12,
     "auto-scaling-trap-scale-up-without-downtime",
     "A stateless application runs on one EC2 instance; CPU reaches 100% at peaks and the load varies during the day; growth must be handled with minimal downtime. Which solution? (difficulty 1, qualifier none). Key: an Auto Scaling group across two Availability Zones behind a load balancer, with a target tracking policy (ec2-auto-scaling-decision-guide-horizontal-for-fluctuating, ec2-auto-scaling-wa-stateless-scales-horizontally). Distractors: change the instance to a larger instance type (this trap; ec2-auto-scaling-vertical-stop-required); turn on detailed monitoring (misconception: monitoring adds no capacity); add a second network interface (misconception).")
slot("q05", "3.2.S1", "queue-backlog-per-instance", 2, "single", "core", ["ee-decouple", "ee-scalable"], D + S9,
     "auto-scaling-trap-queue-length-metric",
     "A web tier sends image jobs to an Amazon SQS queue; workers in an Auto Scaling group need about 2 seconds for each message; each message must be processed within 60 seconds; the number of jobs changes during the day. Which scaling configuration keeps processing within the limit in the MOST cost-effective way? Key: target tracking on backlog per instance (metric math ApproximateNumberOfMessagesVisible divided by GroupInServiceInstances) with a target of 30 (ec2-auto-scaling-sqs-backlog-per-instance, ec2-auto-scaling-sqs-backlog-per-instance-metric-math, ec2-auto-scaling-sqs-acceptable-backlog-per-instance-target). Distractors: target tracking on ApproximateNumberOfMessagesVisible with a target of 30 (this trap); target tracking on average CPU at 50% (misconception: for queue work CPU is not the primary metric, ec2-auto-scaling-wa-queue-depth-metric-for-batch-work); a scheduled action that doubles the workers every hour (violates cost).")
slot("q06", "2.2.S4", "ec2-status-check-default", 2, "single", "core", ["ee-ensure", "ee-least-operational-overhead"], D + S5,
     "auto-scaling-trap-elb-checks-on-by-default",
     "Strict twin of q02: same stem and the same four options; the changed phrase is 'Sometimes the underlying hardware of an instance fails, and the instance fails its EC2 system status check.' Key B (no change: EC2 status checks are [always enabled] and are the [default health check type]; the group replaces impaired instances: ec2-auto-scaling-ec2-status-checks-always-enabled, ec2-auto-scaling-health-check-type-ec2-default, ec2-auto-scaling-faq-unhealthy-instance-definition). A works but adds a change (violates-qualifier, LEAST operational overhead); C reboots instead of replacing; D misconception. The trap id sits on the explanation of B's truth and on any option text that says the ELB checks are already on.",
     twin_of="q02", twin_kind="strict")
slot("q07", "3.2.S2", "target-tracking-for-unpredictable", 2, "single", "core", ["ee-most-cost-effective", "ee-unpredictable"], D + S8,
     "auto-scaling-trap-predictive-scales-in",
     "Strict twin of q03: same stem and the same four options; the changed phrase is 'Traffic rises to a peak several times a day at unpredictable times, with no daily or weekly pattern.' Key A (ec2-auto-scaling-scheduled-vs-dynamic-when-to-use: [you don't know when the traffic will change]). B pays for a morning step that the pattern does not need (violates-qualifier); C needs a pattern and does not scale in (this trap); D violates cost.",
     twin_of="q03", twin_kind="strict")
slot("q08", "2.2.S4", "protect-long-jobs-from-termination", 3, "multi", "extended", ["ee-select-two", "ee-ensure", "ee-long-running"], D + S10,
     "auto-scaling-trap-scale-in-protection-protects-all",
     "(Select TWO.) On-Demand workers in a group run jobs of up to 2 hours; scale in must not stop a running job, and after a job the instance may be removed; operators sometimes terminate worker instances by mistake in the EC2 console, and that must also be prevented. Keys: the worker turns on instance scale-in protection for itself while a job runs and turns it off after (ec2-auto-scaling-faq-termination-policy-and-instance-protection, ec2-auto-scaling-sqs-unprocessed-messages-return); turn on Amazon EC2 termination protection for the instances (ec2-auto-scaling-scale-in-protection-ec2-termination-protection-for-manual). Distractors: rely on scale-in protection to also block terminations in the console (this trap); suspend the Terminate process for good (AWS recommends it [We only recommend using this option] when other options do not give enough control, and it stops every scale in: ec2-auto-scaling-suspend-terminate-full-control); move the workers to Spot Instances with a termination lifecycle hook so that Amazon EC2 waits for each job (trap auto-scaling-trap-lifecycle-hook-stops-spot).")
slot("q09", "2.2.K7", "instance-refresh-new-ami", 2, "single", "core", ["ee-immutable", "ee-least-operational-overhead"], D + S13,
     "auto-scaling-trap-update-template-updates-instances",
     "Worked (no wrong path). A company must replace every instance of a group with instances from a new, patched AMI; at least 90% of the capacity must stay in service; the team keeps immutable infrastructure; LEAST operational overhead. Key: create a launch template version with the new AMI, make it the group's version, and start an instance refresh with the default minimum healthy percentage (ec2-auto-scaling-instance-refresh-use-cases, ec2-auto-scaling-instance-refresh-min-healthy-percentage-default). Distractors: create the new launch template version and wait (this trap); edit the group's launch configuration (trap auto-scaling-trap-launch-configuration-editable); patch each instance in place through Session Manager (misconception: immutable infrastructure makes [no updates, security patches, or configuration changes] in place, ec2-auto-scaling-wa-immutable-infrastructure-definition).",
     worked=True, wrong_path=False)
slot("q10", "2.2.S1", "migrate-to-launch-template", 2, "single", "extended", ["ee-least-operational-overhead"], D + S2,
     "auto-scaling-trap-launch-configuration-editable",
     "A group uses a launch configuration; the company now wants Spot and On-Demand Instances of several instance types in the same group with the LEAST operational overhead. Key: create a launch template with the same settings and update the group to use it with a mixed instances policy (ec2-auto-scaling-launch-config-no-mixed-types, ec2-auto-scaling-purchase-options-need-launch-template). Distractors: modify the launch configuration to add Spot Instances (this trap); attach a second launch configuration for the Spot Instances (impossible: [only specify one launch configuration], ec2-auto-scaling-faq-launch-configuration-one-and-immutable); run a separate Spot Fleet next to the group (works, violates-qualifier).")
slot("q11", "4.2.S2", "spot-mixed-instances-cost", 3, "multi", "extended",
     ["ee-select-two", "ee-most-cost-effective", "ee-can-tolerate-interruption", "ee-stateless"], D + S11,
     "how-the-exam-asks-trap-cheapest-wins",
     "(Select TWO.) Stateless video workers can tolerate interruption; at least 2 workers must always run; MOST cost-effective. Keys: a mixed instances policy with an On-Demand base capacity of 2 and Spot Instances above it (ec2-auto-scaling-faq-on-demand-base-spot-above); several instance types with the price-capacity-optimized allocation strategy (ec2-auto-scaling-spot-price-capacity-optimized-recommended, ec2-spot-be-flexible-types-and-azs). Distractors: the lowest-price strategy with one instance type (trap how-the-exam-asks-trap-cheapest-wins on its distractor; fact ec2-auto-scaling-spot-lowest-price-not-recommended); all On-Demand Instances with a scheduled action (violates cost); Spot Instances only, with scale-in protection on every instance (trap auto-scaling-trap-scale-in-protection-protects-all: interruptions [bypass all Amazon EC2 Auto Scaling protection mechanisms], ec2-auto-scaling-spot-interruption-bypasses-all-protection). Five options. The slot trap is a distractor trap of another chapter.")
slot("q12", "4.2.K9", "warm-pool-for-slow-start", 2, "single", "extended", ["ee-most-cost-effective"], D + S12,
     "auto-scaling-trap-hibernate-group-instance",
     "An application loads a large data set into memory when it starts, which takes many minutes; scale-out at the daily peaks is too slow; the fix must be MOST cost-effective. Key: add a warm pool and keep its instances Hibernated (or Stopped) (ec2-auto-scaling-warm-pool-definition, ec2-auto-scaling-warm-pool-hibernated-ram, ec2-auto-scaling-warm-pool-states). Distractors: hibernate the group's own instances at night and start them in the morning (this trap; ec2-auto-scaling-cannot-hibernate-group-instance); raise the minimum capacity to the peak size (works, violates-qualifier; trap how-the-exam-asks-trap-works-means-correct); move to a larger instance type (trap auto-scaling-trap-scale-up-without-downtime).")
slot("q13", "2.2.S2", "add-az-group-and-load-balancer", 2, "single", "core", ["ee-across-availability-zones", "ee-highly-available"], D + S3,
     "auto-scaling-trap-group-spans-regions",
     "A group runs all its instances in one Availability Zone behind an Application Load Balancer; the application must be highly available. Which change? Key: add a subnet in a second Availability Zone to the group and enable that zone on the load balancer (ec2-auto-scaling-add-az-group-and-load-balancer, ec2-auto-scaling-lb-no-traffic-to-disabled-az). Distractors: add the second zone to the group only (misconception: the load balancer does not route to a zone it has not enabled); extend the group into a second Region (this trap); double the desired capacity in the same zone (trap aws-map-trap-one-az-is-highly-available). The official sample question has this shape; write an original stem.")
slot("q14", "3.2.S2", "simple-to-target-tracking-with-warmup", 3, "single", "extended", ["ee-spiky"], D + S7,
     "auto-scaling-trap-cooldown-for-all-policies",
     "A group uses one simple scaling policy with the default cooldown; traffic is spiky; a second spike during the cooldown gets no capacity, and new instances report high CPU while they start, which once caused extra scale-out. Which change is MOST effective? Key: replace the simple policy with a target tracking (or step) policy and turn on a default instance warmup (ec2-auto-scaling-cooldown-target-tracking-step-do-not-wait, ec2-auto-scaling-default-instance-warmup-purpose, ec2-auto-scaling-simple-scaling-not-recommended). Distractors: keep simple scaling and set the default cooldown to 60 seconds (misconception: start-up CPU still counts); add a target tracking policy and lower its cooldown, because it waits for the cooldown too (this trap); add a second simple scaling policy with a larger adjustment (misconception: the cooldown still blocks it).")
slot("q15", "3.2.S2", "predictive-needs-dynamic", 3, "single", "extended", ["ee-predictable", "ee-most-cost-effective"], D + S8,
     "auto-scaling-trap-predictive-scales-in",
     "Worked, wrong path. A group uses only a predictive scaling policy in forecast and scale mode; morning scale-out works, but capacity stays high at night and cost grew. MOST cost-effective fix. Key: add a target tracking policy so that the group can scale in (ec2-auto-scaling-predictive-does-not-scale-in, ec2-auto-scaling-combine-policy-types-predictive-plus-dynamic). Distractors: switch the policy to forecast only mode (misconception: forecast only does not scale at all, ec2-auto-scaling-predictive-forecast-only-mode-first); lower the maximum capacity (blocks the morning peak, violates the requirement); let predictive scaling raise and lower the maximum capacity automatically (impossible: a raised maximum [does not automatically decrease back], ec2-auto-scaling-predictive-raised-max-stays). Step 3 states the wrong prediction 'forecast only mode removes the extra instances'; step 5: 'My first idea breaks because forecast only mode does not scale the group at all, in either direction.'",
     worked=True, wrong_path=True)
slot("q16", "2.2.S4", "default-termination-policy", 1, "single", "extended", [], D + S10,
     "auto-scaling-trap-oldest-terminated-first",
     "Difficulty 1, qualifier none. A group has 3 instances in AZ 1, one of them launched from an older launch template version, and 2 instances in AZ 2, one of them the oldest instance of the group; the group uses the default termination policy and scales in by one. Which instance is terminated? Key: the instance in AZ 1 that uses the older launch template version (ec2-auto-scaling-termination-default-zone-with-most, ec2-auto-scaling-termination-default-outdated-first). Distractors: the oldest instance, in AZ 2 (this trap); the newest instance of the group (misconception: NewestInstance is a policy you choose, ec2-auto-scaling-termination-policy-newest-instance); a random instance from either zone (misconception: zone balance comes first, ec2-auto-scaling-termination-az-balance-first).")
slot("q17", "2.2.S1", "launch-hook-bootstrap", 2, "single", "core", ["ee-ensure", "ee-automate"], D + S4, None,
     "New instances run a script that downloads configuration for several minutes; the load balancer sends them requests before they are ready, and users see errors; the company must ensure that no instance gets traffic before the script ends, with the LEAST operational overhead. Key: a launch lifecycle hook that the script completes with CompleteLifecycleAction (ec2-auto-scaling-lifecycle-hook-lb-registration, ec2-auto-scaling-lifecycle-hook-user-data-complete, ec2-auto-scaling-registers-with-lb-before-inservice). Distractors: raise the health check grace period (misconception: it delays health-based replacement, not traffic, ec2-auto-scaling-grace-period-definition); turn on slow start on the target group (misconception: the instance still gets requests, only fewer at first, elb-alb-slow-start-30-to-900-seconds-default-off); use a larger instance type (misconception).")
slot("q18", "2.2.S4", "termination-hook-copy-logs", 2, "single", "extended", ["ee-ensure"], D + S10, None,
     "On-Demand instances of a group write logs to local disk; before scale in terminates an instance, its logs must be copied to Amazon S3; the copy takes a few minutes; LEAST operational overhead. Key: a termination lifecycle hook that invokes an AWS Lambda function (or a script) to copy the logs and then completes the lifecycle action (ec2-auto-scaling-lifecycle-hook-scale-in-use, ec2-auto-scaling-termination-hook-extends-life). Distractors: turn on scale-in protection for every instance (misconception: it stops scale in instead of delaying it); a longer deregistration delay on the target group (misconception: it drains connections, it runs no code, ec2-auto-scaling-deregisters-on-scale-in); a user data script that copies the logs at shutdown (misconception: user data runs [run only during the boot cycle] of the first launch by default, ec2-user-data-runs-at-first-launch-by-default).")
slot("q19", "2.1.S2", "session-state-off-instance", 2, "single", "core", ["ee-stateless", "ee-scalable"], D + S10,
     "auto-scaling-trap-new-instance-data-copied",
     "Users are signed out when the group removes an instance during scale in; sessions live in instance memory; the tier must keep scaling in and users must keep their sessions; MOST scalable fix. Key: store session data in a shared store such as Amazon ElastiCache or Amazon DynamoDB (ec2-auto-scaling-wa-offload-session-data, ec2-auto-scaling-faq-persist-data-off-instance). Distractors: let the group copy session data from running instances to new ones (this trap); turn on sticky sessions on the load balancer (trap elb-trap-sticky-sessions-keep-state); turn on scale-in protection for all instances (misconception: the tier then cannot scale in).")
slot("q20", "3.2.K4", "native-predictive-policy-no-plan", 2, "single", "extended", ["ee-least-operational-overhead"], SVC, None,
     "An EC2 Auto Scaling group has a daily traffic pattern; the team plans an AWS Auto Scaling scaling plan only to get predictive scaling; LEAST operational overhead. Key: add a predictive scaling policy to the group directly (ec2-auto-scaling-faq-predictive-policy-vs-scaling-plan, aws-auto-scaling-plans-prefer-native-predictive-policies). Distractors: create the scaling plan with predictive scaling (works, violates-qualifier); use Application Auto Scaling for the EC2 group (misconception: EC2 instances use EC2 Auto Scaling, aws-auto-scaling-wa-ec2-auto-scaling-for-instances-application-auto-scaling-for-other-services); write a Lambda function that creates scheduled actions from CloudWatch history (violates-qualifier).")
slot("q21", "2.2.S2", "static-stability-across-azs", 3, "multi", "extended",
     ["ee-select-two", "ee-fault-tolerant", "ee-across-availability-zones"], D + S3,
     "how-the-exam-asks-trap-ha-equals-ft",
     "(Select TWO.) A web application needs 6 instances at peak; it must keep full capacity with no waiting even if one Availability Zone fails. Keys: run the group across three Availability Zones behind a load balancer in the same zones (ec2-auto-scaling-resilience-practices); size the group so that two zones alone carry the peak, 9 instances with 3 in each zone (static stability: [static stability is preferred for high availability], ec2-auto-scaling-wa-static-stability-for-az-loss). Distractors: rely on the group to launch replacements in the other zones after a failure (works for high availability, not for 'no waiting': this trap of chapter 01; ec2-auto-scaling-faq-replacement-time-minutes); one group that spans two Regions (trap auto-scaling-trap-group-spans-regions); all instances in a cluster placement group in one zone (trap aws-map-trap-one-az-is-highly-available). Five options.")
slot("q22", "4.2.S2", "capacity-rebalancing-spot", 2, "single", "extended", ["ee-can-tolerate-interruption", "ee-most-resilient"], D + S11,
     "auto-scaling-trap-lifecycle-hook-stops-spot",
     "A worker group runs on Spot Instances; when Amazon EC2 reclaims capacity, the group loses workers before replacements start; the MOST resilient change that keeps Spot pricing. Key: turn on Capacity Rebalancing, so the group launches a replacement when an instance is [at an elevated risk of interruption] (ec2-auto-scaling-capacity-rebalancing-spot, ec2-auto-scaling-no-capacity-rebalancing-replace-after-interruption). Distractors: a termination lifecycle hook that delays the reclaim until the job ends (this trap); scale-in protection on every instance (trap auto-scaling-trap-scale-in-protection-protects-all); switch the allocation strategy to lowest-price (misconception: [highest risk of interruption], ec2-auto-scaling-spot-lowest-price-not-recommended).")

brief["question_slots"] = QS
brief["question_plan"] = {
    "write": 22,
    "difficulty": {"1": 3, "2": 14, "3": 5},
    "layer": {"core": 11, "extended": 11},
    "multi": 3,
    "twin_pairs": [
        "q02 / q06 (strict: 'the application on an instance stops answering HTTP requests, but the instance keeps running' / 'the underlying hardware of an instance fails, and the instance fails its EC2 system status check'; same four options; key A / key B)",
        "q03 / q07 (strict: 'Traffic rises to a peak from 09:00 to 11:00 every weekday' / 'Traffic rises to a peak several times a day at unpredictable times, with no daily or weekly pattern'; same four options; key B / key A)",
    ],
    "worked": ["q09 (no wrong path)", "q15 (wrong path)"],
    "slots_on_a_trap": 19,
    "every_trap_cited": "each of the 13 trap ids is the slot trap or a planned distractor trap of at least one slot: elb-checks-on-by-default q02 q06; oldest-terminated-first q16; hibernate-group-instance q12; new-instance-data-copied q19; group-spans-regions q13 q21; launch-configuration-editable q10 q09; cooldown-for-all-policies q14; predictive-scales-in q03 q07 q15; queue-length-metric q05; scale-in-protection-protects-all q08 q11 q22; lifecycle-hook-stops-spot q22 q08; scale-up-without-downtime q04 q12; update-template-updates-instances q09",
    "bullets_covered": "all 11 bullets of the registry entry: 3.2.K4 q01 q20; 3.2.S1 q05; 3.2.S2 q03 q07 q14 q15; 2.1.K6 q04; 2.1.S2 q19; 4.2.K9 q12; 4.2.S2 q11 q22; 2.2.K7 q09; 2.2.S1 q10 q17; 2.2.S2 q13 q21; 2.2.S4 q02 q06 q08 q16 q18",
    "q205_rule": "Every wrong option names a trap id where one fits (this brief's 13, or traps_from_other_chapters); at least half of the wrong options must carry one. A distractor gets a trap id only when its text states exactly that trap's belief; otherwise it carries a misconception and a distractor_type.",
    "rule": "Question ids are auto-scaling-q001 to auto-scaling-q022 in slot order (q01 = auto-scaling-q001). Protect the two strict twin pairs, the three multiple-response questions and both worked questions when the weakest four are cut. At most 2 questions per concept; a unique (concept, trap) pair per question. Stems never name Callvale; they may reuse its situation and numbers. Keep at most one impossible-feature distractor per question, and give it a fact. Never key an answer on a launch configuration or on a change that is not examinable yet (batch termination, the CloudFormation instance refresh policy). Do not let a fact with a recent change decide a key (the predictive forecast cadence changed in 2023: never key on 'every 6 hours'). No question keys on an API error that no fact states (for example a desired capacity above the maximum through the API).",
}

brief["terms"] = ["auto-scaling-group", "scale-out", "scale-up", "health-check", "stateless", "decouple",
                  "single-point-of-failure", "deregistration-delay", "high-availability", "fault-tolerance"]
brief["term_requests"] = [
    "launch template", "desired capacity", "scaling policy", "target tracking scaling policy", "step scaling policy",
    "simple scaling policy", "scheduled action", "predictive scaling", "cooldown (scaling cooldown)",
    "instance warmup (default instance warmup)", "health check grace period", "lifecycle hook", "termination policy",
    "scale-in protection (instance scale-in protection)", "warm pool", "instance refresh", "mixed instances policy",
    "Capacity Rebalancing", "immutable infrastructure", "backlog per instance", "maximum instance lifetime",
    "instance maintenance policy", "hibernation", "Standby (instance state of a group; the bank term 'standby' means a database standby)",
]

# ---------------------------------------------------------------- tasks
brief["tasks"] = [
    {"id": "auto-scaling-t01", "type": "look", "title": "List the termination policies and the processes of EC2 Auto Scaling",
     "section": "1-fast.md#look-first", "kills": "\"On scale in, the group terminates its oldest instance first.\"",
     "trap": "auto-scaling-trap-oldest-terminated-first", "pass_route": False, "status": "write",
     "plan": "In AWS CloudShell, read-only, 3 minutes, $0. aws autoscaling describe-termination-policy-types: the expected output lists Default, OldestInstance, NewestInstance, OldestLaunchConfiguration, OldestLaunchTemplate, ClosestToNextInstanceHour and AllocationStrategy (exact list from the CLI reference page; tasks check-cli --reference): the oldest instance is one policy that you choose, not the default (ec2-auto-scaling-termination-default-outdated-first, ec2-auto-scaling-termination-az-balance-first). aws autoscaling describe-scaling-process-types: the processes that you can suspend (ec2-auto-scaling-suspend-processes-purpose). aws autoscaling describe-account-limits: MaxNumberOfAutoScalingGroups; the default quota is [500 Auto Scaling groups] (ec2-auto-scaling-quota-groups-per-region). Optionally aws autoscaling describe-auto-scaling-groups (may be empty). Creates nothing.",
     "facts": f("termination-default-outdated-first", "termination-az-balance-first", "suspend-processes-purpose",
                "quota-groups-per-region", "termination-policy-oldest-instance")},
    {"id": "auto-scaling-t02", "type": "try", "title": "Terminate an instance by hand and watch the group replace it",
     "section": D + S1, "kills": "\"An instance that someone terminates by hand is gone until someone launches a new one.\"",
     "trap": None, "pass_route": False, "status": "write",
     "plan": "In AWS CloudShell, in the default VPC, one small instance for about 20 minutes (cost line: EC2 bills [You pay only for the seconds] the instance runs with a [60-second minimum] (ec2-on-demand-billing-per-second-60s-minimum); EC2 Auto Scaling adds [no additional fees] (ec2-auto-scaling-pricing-page-no-additional-fees); the writer needs a verified price fact for the instance type or files a fact request; no price from memory). Create a security group saa-auto-scaling-t02 with no inbound rules, tagged book=saa and task=auto-scaling-t02. Create a launch template saa-auto-scaling-t02 whose ImageId is the public Amazon Linux parameter (resolve:ssm:/aws/service/ami-amazon-linux-latest/...; [a public parameter for a public AMI], ec2-auto-scaling-ssm-parameter-sources), the smallest general purpose instance type, that security group, no key pair, and tag specifications with both tags. Create the group saa-auto-scaling-t02 with min 1, max 1, desired 1 in two default subnets of different zones, with both tags and PropagateAtLaunch. Wait, then describe-auto-scaling-groups and capture the InService instance ID. Break it: predict 'After you terminate this instance with the EC2 API, does the group stay empty?', run aws ec2 terminate-instances on the captured ID, then describe-scaling-activities: expect a new launch activity, because an instance that [terminates unexpectedly] is replaced: [automatically launch a replacement instance] (ec2-auto-scaling-health-unexpected-termination-replaced). Fix (the intended way to shrink): update-auto-scaling-group with min 0 and desired 0; the group terminates its instance (ec2-auto-scaling-desired-capacity-maintained). Cleanup: delete-auto-scaling-group --force-delete (its instances are terminated: ec2-auto-scaling-faq-delete-group-terminates-instances), delete-launch-template, delete-security-group (after the instance is gone). Verify by name (R6 T108): aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names saa-auto-scaling-t02 returns an empty list. The writer confirms with tasks check-cli --reference that a launch template accepts the resolve:ssm form for ImageId; if not, read the parameter with aws ssm get-parameters first and capture the AMI ID. Label 'checked against docs, not run in a real account'.",
     "facts": ["=ec2-on-demand-billing-per-second-60s-minimum"] + f("pricing-page-no-additional-fees", "ssm-parameter-sources",
                "health-unexpected-termination-replaced", "desired-capacity-maintained", "faq-delete-group-terminates-instances",
                "billed-from-launch")},
    {"id": "auto-scaling-t03", "type": "try", "title": "Attach a target tracking policy and a scheduled action to an empty group",
     "section": D + S6, "kills": "\"You create the CloudWatch alarms of a target tracking policy yourself.\"",
     "trap": None, "pass_route": True, "status": "write",
     "plan": "In AWS CloudShell, no instances at any time ($0 compute; cost line: the two alarms carry CloudWatch fees, [service fees apply and are billed separately] (ec2-auto-scaling-faq-no-additional-fees); the writer finds a CloudWatch alarm price fact or files a request). Create a launch template saa-auto-scaling-t03 (same form as t02, tagged book=saa and task=auto-scaling-t03) and the group saa-auto-scaling-t03 with min 0, max 1, desired 0 in two default subnets, both tags. Put a target tracking policy saa-cpu-50 on ASGAverageCPUUtilization with target 50 ([ASGAverageCPUUtilization], ec2-auto-scaling-target-tracking-predefined-metrics). describe-alarms with --alarm-name-prefix TargetTracking-saa-auto-scaling-t03: expect [two alarms], one for scaling out and one for scaling in (ec2-auto-scaling-target-tracking-creates-two-alarms), created by the service ([creates and manages the CloudWatch alarms], ec2-auto-scaling-target-tracking-service-manages-alarms); their state is INSUFFICIENT_DATA because no instance reports CPU ([cannot scale your group until new data points], ec2-auto-scaling-target-tracking-insufficient-data-no-scaling). Add a one-time scheduled action saa-once-a at <FUTURE_TIME> (an ISO time she picks, at least one day ahead) with min 0, max 1, desired 0. Break it: predict 'Can a second action start at the same time?', put saa-once-b at the same <FUTURE_TIME>: expect an error, because each action needs [must have a unique time value] and [the call is rejected] (ec2-auto-scaling-scheduled-unique-start-time). Fix: put saa-once-b one hour later. Cleanup: delete-scheduled-action for both, delete-policy (the service manages the alarms: [Do not create, edit, or delete] them, ec2-auto-scaling-target-tracking-do-not-edit-alarms), delete-auto-scaling-group, delete-launch-template. Verify by name: describe-auto-scaling-groups --auto-scaling-group-names saa-auto-scaling-t03 returns an empty list. Label 'checked against docs, not run in a real account'.",
     "facts": f("faq-no-additional-fees", "target-tracking-predefined-metrics", "target-tracking-creates-two-alarms",
                "target-tracking-service-manages-alarms", "target-tracking-insufficient-data-no-scaling",
                "scheduled-unique-start-time", "target-tracking-do-not-edit-alarms", "scheduled-one-time-or-recurring")},
]

# ---------------------------------------------------------------- speak
brief["speak"] = [
    {"id": "auto-scaling-s01", "kind": "explain", "persona": "Ben, CTO of Callvale",
     "prompt": "The load balancer has health checks. Is it not the load balancer that replaces a broken instance?",
     "section": D + S5, "pass_route": True,
     "facts": ["=elb-unhealthy-target-stop-resume"] + f("elb-checks-reroute-and-replace", "elb-health-checks-ignored-by-default",
               "health-elb-check-must-be-turned-on", "grace-period-console-300-cli-0", "faq-elb-requests-before-detection-fail",
               "unhealthy-terminated-replaced"),
     "note": "Short answer: no; the load balancer only stops sending requests to a broken instance, and the Auto Scaling group replaces it, but only after we turn on the ELB health check type. How it works: the load balancer marks the instance unhealthy and routes around it; the group checks the load balancer's verdict and, when it says unhealthy, terminates the instance and launches a new one. Watch: the grace period must cover our four-minute start, or the group replaces instances that are still starting. In your case: 'Is the ELB health check type turned on for our web group, and how long is its grace period?' Must not say: 'the load balancer terminates and replaces the instance'; 'the group uses the load balancer health checks by default'; 'no request ever fails' (some requests fail before the failure is noticed: ec2-auto-scaling-faq-elb-requests-before-detection-fail)."},
    {"id": "auto-scaling-s02", "kind": "decide", "persona": "Ana, CEO of Callvale",
     "prompt": "Why not run 12 instances all day, so that launch week is safe? What does each choice cost us?",
     "section": "2-deep.md#decision-record", "pass_route": False,
     "facts": f("default-no-policies-fixed-size", "wa-demand-based-pay-for-use", "billed-from-launch",
                "scheduled-vs-dynamic-when-to-use", "scheduled-plus-policies-together", "faq-no-additional-fees"),
     "note": "Ana uses no AWS terms: say 'a schedule' and 'a rule that adds servers when they get busy' before the AWS names. No dollar amounts, no computed shares. Short answer: no; twelve all day pays for idle servers every night, while a schedule plus automatic scaling gives us six before the morning peak and more only when traffic needs them. How it works: at 08:45 on weekdays the group starts more instances; during the day a rule keeps the servers' load near a target and removes extra ones in the evening. Watch: a surprise spike outside the morning still waits about four minutes for new servers, which is why we keep three running at night. In your case: 'Is a four-minute delay acceptable for a surprise spike in the afternoon?' Must not say: 'automatic scaling is free' without the instance cost; 'twelve servers all day removes every risk'."},
    {"id": "auto-scaling-s03", "kind": "decide", "persona": "a startup founder in office hours",
     "prompt": "Our workers pull jobs from a queue. Should the worker group scale on CPU?",
     "section": D + S9, "pass_route": False,
     "facts": f("wa-queue-depth-metric-for-batch-work", "sqs-backlog-per-instance", "sqs-queue-length-not-proportional",
                "sqs-acceptable-backlog-per-instance-target", "target-tracking-scale-to-zero-needs-min-zero",
                "sqs-unprocessed-messages-return"),
     "note": "Short answer: usually not; scale on the backlog per worker, the messages in the queue divided by the running workers. How it works: you decide how long a job may wait, divide by how long one worker needs for a job, and set that as the target; target tracking then adds or removes workers. Watch: busy workers often sit near full CPU, so CPU says little about the queue; and a worker that is removed in the middle of a job returns its message to the queue. In your case: 'How long may a job wait in the queue before a customer notices?' Must not say: 'scale on the total number of messages in the queue'; 'CPU always tells you the load'."},
    {"id": "auto-scaling-s04", "kind": "compare", "persona": "a startup CTO you advise",
     "prompt": "Bigger instance or more instances: how should we scale our API servers?",
     "section": D + S12, "pass_route": False,
     "facts": f("vertical-resize-instance-type", "vertical-stop-required", "decision-guide-horizontal-for-fluctuating",
                "wa-stateless-scales-horizontally", "wa-offload-session-data", "vertical-stopped-group-instance-unhealthy"),
     "note": "First sentence may start 'Both'. Short answer: both add capacity, but more instances fit a load that changes, and a bigger instance means a stop. How it works: a larger instance type needs the instance stopped, so you plan for downtime; an Auto Scaling group adds and removes identical instances while the others keep serving. Watch: more instances work only if the servers keep no session data on the instance; put sessions in a cache or a database. In your case: 'Does your API keep anything in server memory between requests?' Must not say: 'you can change the instance type with no downtime'; 'scaling out works for any application as it is'."},
]

# ---------------------------------------------------------------- cards
C = []


def card(cid, typ, deck, section, facts, front, back=None, trap_id=None):
    row = {"id": cid, "type": typ, "deck": deck, "section": section, "facts": facts, "front": front}
    if back is not None:
        row["back"] = back
    if trap_id:
        row["trap"] = trap_id
    C.append(row)


NUM = D.rstrip("#") + "#numbers-that-decide-answers"
card("auto-scaling-c001", "decide", "core", D + S5, f("health-elb-check-must-be-turned-on"),
     "In EC2 Auto Scaling, instances fail the load balancer health checks but are never replaced. What do you change?",
     "Turn on the ELB health check type for the group.", "auto-scaling-trap-elb-checks-on-by-default")
card("auto-scaling-c002", "cannot", "core", D + S3, f("faq-regional-spans-azs-not-regions"),
     "In EC2 Auto Scaling, can one Auto Scaling group span two Regions?",
     "No. It spans Availability Zones, not Regions.", "auto-scaling-trap-group-spans-regions")
card("auto-scaling-c003", "decide", "core", D + S8, f("scheduled-vs-dynamic-when-to-use"),
     "In EC2 Auto Scaling, the load rises at the same known time every weekday. What adds capacity before it?",
     "A scheduled action.")
card("auto-scaling-c004", "decide", "core", D + S6, f("faq-target-tracking-definition"),
     "In EC2 Auto Scaling, keep average CPU near one value with the least setup. Which policy?",
     "A target tracking scaling policy.")
card("auto-scaling-c005", "decide", "core", D + S9, f("sqs-backlog-per-instance"),
     "In EC2 Auto Scaling, workers process an SQS queue. Which metric do they scale on?",
     "Backlog per instance: visible messages divided by InService instances.", "auto-scaling-trap-queue-length-metric")
card("auto-scaling-c006", "cannot", "core", D + S12, f("cannot-hibernate-group-instance"),
     "In EC2 Auto Scaling, can you hibernate an instance that is in the group?",
     "No. The group marks it unhealthy and may replace it.", "auto-scaling-trap-hibernate-group-instance")
card("auto-scaling-c007", "number", "core", NUM, f("default-cooldown-300-seconds"),
     "In EC2 Auto Scaling, the default cooldown of a group is {{c1::300 seconds}}.")
card("auto-scaling-c008", "number", "core", NUM, f("grace-period-console-300-cli-0"),
     "In EC2 Auto Scaling, the default health check grace period is {{c1::300 seconds}} in the console and {{c2::0 seconds}} with the AWS CLI.")
card("auto-scaling-c009", "number", "core", NUM, f("lifecycle-hook-heartbeat-timeout-default"),
     "In EC2 Auto Scaling, the default heartbeat timeout of a lifecycle hook is {{c1::3600 seconds}}.")
card("auto-scaling-c010", "number", "core", NUM, f("predictive-needs-24-hours-of-data"),
     "In EC2 Auto Scaling, a predictive scaling policy needs {{c1::at least 24 hours of data}} before it forecasts.")
card("auto-scaling-c011", "number", "core", NUM, f("lifecycle-hook-spot-two-minute-notice"),
     "In EC2 Auto Scaling, Amazon EC2 reclaims a Spot Instance with a {{c1::two-minute interruption notice}}.")
card("auto-scaling-c012", "number", "core", NUM, f("instance-refresh-min-healthy-percentage-default"),
     "In EC2 Auto Scaling, the default minimum healthy percentage of an instance refresh is {{c1::90 percent}}.")
card("auto-scaling-c013", "number", "core", NUM, f("max-instance-lifetime-min-one-day"),
     "In EC2 Auto Scaling, the maximum instance lifetime must be at least {{c1::86,400 seconds}}.")
card("auto-scaling-c014", "number", "core", NUM, f("cooldown-elb-deregistration-300-seconds"),
     "In EC2 Auto Scaling with a load balancer, connection draining waits {{c1::300 seconds}} by default.")
card("auto-scaling-c015", "differ", "extended", D + S7, f("cooldown-applies-to-simple-scaling"),
     "In EC2 Auto Scaling, which policy type waits for the cooldown between activities?",
     "Simple scaling. Step and target tracking use warmup.", "auto-scaling-trap-cooldown-for-all-policies")
card("auto-scaling-c016", "decide", "extended", D + S13, f("instance-refresh-use-cases"),
     "In EC2 Auto Scaling, a new AMI must reach every running instance. Which feature?",
     "An instance refresh with a new launch template version.", "auto-scaling-trap-update-template-updates-instances")
card("auto-scaling-c017", "cannot", "extended", D + S2, f("launch-config-immutable"),
     "In EC2 Auto Scaling, can you modify a launch configuration after you create it?",
     "No. Create a new one; better, use a launch template.", "auto-scaling-trap-launch-configuration-editable")
card("auto-scaling-c018", "decide", "extended", D + S11, f("purchase-options-need-launch-template"),
     "In EC2 Auto Scaling, one group must mix Spot and On-Demand Instances. What must it launch from?",
     "A launch template.")
card("auto-scaling-c019", "decide", "extended", D + S11, f("spot-price-capacity-optimized-recommended"),
     "In EC2 Auto Scaling, which Spot allocation strategy does AWS recommend?", "price-capacity-optimized.")
card("auto-scaling-c020", "cannot", "extended", D + S10, f("scale-in-protection-not-health-replacement"),
     "In EC2 Auto Scaling, does scale-in protection stop the replacement of an unhealthy instance?",
     "No. It protects only against scale in.", "auto-scaling-trap-scale-in-protection-protects-all")
card("auto-scaling-c021", "decide", "extended", D + S10, f("termination-hook-extends-life"),
     "In EC2 Auto Scaling, an instance must save its work before scale in terminates it. What do you add?",
     "A termination lifecycle hook.")
card("auto-scaling-c022", "cannot", "extended", D + S11, f("lifecycle-hook-spot-two-minute-notice"),
     "In EC2 Auto Scaling, does a lifecycle hook keep a Spot Instance running until its job ends?",
     "No. Amazon EC2 still reclaims it after the notice.", "auto-scaling-trap-lifecycle-hook-stops-spot")
card("auto-scaling-c023", "differ", "extended", D + S10, f("termination-default-zone-with-most", "termination-default-outdated-first"),
     "In EC2 Auto Scaling, which instance does the default termination policy remove first?",
     "In the fullest zone, one with an outdated configuration.", "auto-scaling-trap-oldest-terminated-first")
card("auto-scaling-c024", "cannot", "extended", D + S8, f("predictive-does-not-scale-in"),
     "In EC2 Auto Scaling, does a predictive scaling policy scale in on its own?",
     "No. Add a dynamic policy, such as target tracking.", "auto-scaling-trap-predictive-scales-in")
card("auto-scaling-c025", "decide", "extended", D + S12, f("warm-pool-definition"),
     "In EC2 Auto Scaling, instances take long to initialize and scale-out must be fast and cheap. What do you add?",
     "A warm pool of stopped instances.")
card("auto-scaling-c026", "cannot", "extended", D + S4, f("faq-data-not-copied-to-new-instances"),
     "In EC2 Auto Scaling, is the data of running instances copied to new instances?",
     "No. Keep data off the instance or copy it with a hook.", "auto-scaling-trap-new-instance-data-copied")
card("auto-scaling-c027", "decide", "extended", D + S4, f("faq-lifecycle-hooks-definition"),
     "In EC2 Auto Scaling, software must be configured before a new instance gets traffic. What do you use?",
     "A launch lifecycle hook.")
card("auto-scaling-c028", "differ", "extended", SVC, f("faq-use-ec2-vs-aws-auto-scaling"),
     "EC2 Auto Scaling or AWS Auto Scaling: what decides it?",
     "Only EC2 groups, or many resources of one application.")
card("auto-scaling-c029", "decide", "extended", SVC, ["aws-auto-scaling-faq-application-auto-scaling-for-non-ec2"],
     "In AWS, an ECS service or a DynamoDB table must scale automatically. Which service?",
     "Application Auto Scaling.")
card("auto-scaling-c030", "cannot", "extended", D + S6, f("target-tracking-no-scale-out-below-target"),
     "In EC2 Auto Scaling, can a target tracking policy scale out while the metric is below the target?",
     "No.")
card("auto-scaling-c031", "differ", "extended", D + S12, f("vertical-stop-required"),
     "In Amazon EC2, scale up or scale out: which one needs the instance stopped?",
     "Scale up: you stop it to change the instance type.", "auto-scaling-trap-scale-up-without-downtime")
card("auto-scaling-c032", "decide", "extended", D + S3, f("add-az-group-and-load-balancer"),
     "In EC2 Auto Scaling, you add an Availability Zone to a group behind a load balancer. What two changes?",
     "Add the zone to the group and enable it on the load balancer.")

brief["cards"] = C
brief["card_plan"] = {
    "core": 14, "extended": 18, "number_cards_equal_a_list_rows": 8,
    "rule": "Fronts and backs above are drafts for the card writer: one fact per card (c023 names two facts of one rule; keep both or split), an answer of at most 12 words, a display of a fact for any number with a unit (300 seconds, 0 seconds, 3600 seconds, at least 24 hours of data, two-minute interruption notice, 90 percent, 86,400 seconds are the facts' displays), and the context named at the start of the front. Ben's question already has card elb-c004 in chapter 14; do not repeat it here. c013 says 'at least' outside the cloze: the display '86,400 seconds' is inside the cloze; if the lint asks for it, use the display 'at least 86,400 seconds (one day)' as the cloze text.",
}

# ---------------------------------------------------------------- diagrams
brief["diagrams"] = [
    {"id": "auto-scaling-hero", "kind": "arch",
     "placement": "1-fast.md#in-one-breath (behind 'Predict the picture: when traffic rises, which part decides that the group needs another instance, and which part launches it?')",
     "title": "How a group grows and heals",
     "claim": "A policy changes the desired capacity, and the group launches, registers and replaces instances to keep that number.",
     "alt": "An architecture with users on the left, an Application Load Balancer, and an Auto Scaling group across two Availability Zones with one instance in each and a new instance starting. A CloudWatch alarm and a scaling policy sit above the group; a launch template sits beside it. Numbered arrows show the path.",
     "say": [
         "CloudWatch alarms that the target tracking policy manages watch the group's metric.",
         "When the metric moves away from the target, the policy changes the desired capacity of the group.",
         "The group launches a new instance from its launch template in the Availability Zone with the fewest instances.",
         "The group registers the new instance with the load balancer before it marks the instance InService.",
         "When an instance fails its health checks, the group terminates it and launches another.",
     ],
     "facts_for_steps": f("target-tracking-service-manages-alarms", "scaling-policy-adjusts-desired", "launch-in-az-with-fewest",
                          "registers-with-lb-before-inservice", "unhealthy-terminated-replaced"),
     "facts_for_caption": f("scaling-policy-adjusts-desired", "desired-capacity-maintained"),
     "note": "Size s or m, two Availability Zones (the story uses three; the hero stays generic). At most 10 nodes: users (user icon), ALB (alb icon), CloudWatch alarm (cloudwatch icon), scaling policy (a label or the auto-scaling icon), launch template (a label), the Auto Scaling group as a group frame across both zones, two InService instances and one new instance (emph). Steps 1 to 5 are numbered; step 5 marks an unhealthy instance being replaced (dashed). In the Markdown steps link step 1 to ec2-auto-scaling-target-tracking-service-manages-alarms ([creates and manages the CloudWatch alarms]), step 2 to ec2-auto-scaling-scaling-policy-adjusts-desired ([adjusts the desired capacity of the group]), step 3 to ec2-auto-scaling-launch-in-az-with-fewest ([the Availability Zone with the fewest instances]), step 4 to ec2-auto-scaling-registers-with-lb-before-inservice ([registers your instance with the load balancer]) and step 5 to ec2-auto-scaling-unhealthy-terminated-replaced ([terminates the unhealthy instance and launches another]). No AWS number in labels or steps."},
    {"id": "auto-scaling-lifecycle", "kind": "states",
     "placement": D + S4 + " (after the table)",
     "title": "The life of an instance in a group",
     "claim": "A lifecycle hook holds an instance in a wait state at launch or at termination before it moves on.",
     "alt": "A state diagram with seven states. Pending leads to InService, or first to Pending:Wait when a launch hook exists. InService can move to Standby and back. InService leads to Terminating, then to Terminated, or first to Terminating:Wait when a termination hook exists.",
     "states": ["Pending (start)", "Pending:Wait", "InService (emph)", "Standby", "Terminating", "Terminating:Wait",
                "Terminated (final)"],
     "transitions": ["Pending -> Pending:Wait: launch hook", "Pending:Wait -> InService: action completed",
                     "Pending -> InService: no hook", "InService -> Standby: enter standby",
                     "Standby -> InService: exit standby", "InService -> Terminating: scale in",
                     "Terminating -> Terminating:Wait: termination hook", "Terminating:Wait -> Terminated: action completed",
                     "Terminating -> Terminated: no hook"],
     "say": [],
     "facts_for_caption": f("launch-hook-states", "terminate-hook-states", "lifecycle-hook-purpose"),
     "note": "Size s, cols 2, rows 4, flow down: main path in column A (Pending, InService, Terminating, Terminated), side states in column B (Pending:Wait, Standby, Terminating:Wait). Seven states, nine transitions (limits 8 and 12); labels at most 3 words. Pending:Proceed and Terminating:Proceed are left out to stay readable; the trace of the subsection names them. The caption links ec2-auto-scaling-launch-hook-states ([Pending:Wait]) and ec2-auto-scaling-terminate-hook-states ([Terminating:Wait])."},
    {"id": "auto-scaling-method-ladder", "kind": "ladder",
     "placement": D + S8 + " (after the table)",
     "title": "Which scaling method?",
     "claim": "How the load changes decides the method: a schedule, a forecast, a queue backlog or a utilization target.",
     "alt": "A decision ladder with three questions. A known time leads to a scheduled action; a daily or weekly pattern leads to predictive plus dynamic scaling; work in a queue leads to backlog per instance; otherwise target tracking on utilization.",
     "rungs": ["Do you know when the load changes? -> Scheduled action",
               "Does the load repeat daily or weekly? -> Predictive plus dynamic (emph)",
               "Does the work wait in a queue? -> Backlog per instance"],
     "else": "Target tracking on utilization",
     "say": [],
     "facts_for_caption": f("scheduled-vs-dynamic-when-to-use", "wa-predictive-patterns-vs-scheduled-times", "sqs-backlog-per-instance"),
     "note": "Ladder kind: questions at most 9 words, outcomes at most 4 words; no numbers in labels. The caption links ec2-auto-scaling-scheduled-vs-dynamic-when-to-use and ec2-auto-scaling-sqs-backlog-per-instance; it must not say 'only' or 'always'."},
    {"id": "auto-scaling-before", "kind": "timeline",
     "placement": "2-deep.md#decision-record (after Context)",
     "title": "Callvale before: fixed web capacity",
     "claim": "The web tier keeps the same capacity all day, so it is idle at night and short at the weekday peak.",
     "alt": "Before: a weekday timeline from night to evening. Traffic is low, then peaks from 09:00 to 11:00, then falls. Web capacity is one flat bar, fixed by hand, all day.",
     "ticks": ["Night", "08:45", "09:00", "11:00", "Evening"],
     "lanes": ["Traffic: Night->09:00 'Low'; 09:00->11:00 'Peak window' (emph); 11:00->Evening 'Falling'",
               "Web capacity: Night->Evening 'Fixed, set by hand'"],
     "events": ["09:00 'Load test fails'"],
     "say": [],
     "note": "Story picture, timeline kind (A7 rule 13: same ticks and lanes as auto-scaling-after, so that only the capacity lane changes). No numbers with units in labels or claim; the times are tick labels. The JSON diagram text says 'one fixed instance', but chapter 14 left one web instance in each of three zones: keep 'fixed capacity' and no count (story_conflict)."},
    {"id": "auto-scaling-after", "kind": "timeline",
     "placement": "2-deep.md#decision-record (after Decision)",
     "title": "Callvale after: capacity follows the curve",
     "claim": "A scheduled action raises capacity before the weekday peak, and target tracking follows the traffic after it.",
     "alt": "After: the same weekday timeline. Capacity stays at the minimum at night, a scheduled step raises it at 08:45, target tracking adds instances during the peak and removes them in the evening.",
     "ticks": ["Night", "08:45", "09:00", "11:00", "Evening"],
     "lanes": ["Traffic: Night->09:00 'Low'; 09:00->11:00 'Peak window' (emph); 11:00->Evening 'Falling'",
               "Web capacity: Night->08:45 'Minimum size'; 08:45->09:00 'Scheduled step' (emph); 09:00->11:00 'Target tracking adds'; 11:00->Evening 'Scales in slowly'"],
     "events": ["08:45 'Scheduled action'"],
     "say": [],
     "facts_for_caption": f("scheduled-plus-policies-together", "target-tracking-scale-in-gradual"),
     "note": "Same ticks and lanes as auto-scaling-before. The caption sits in the Decision record (role example) but is strict under L705 for absolute words: it has none. If the writer links it, use [use scheduled scaling and scaling policies together] (ec2-auto-scaling-scheduled-plus-policies-together)."},
]

brief["fact_requests"] = [
    {"id": "fr-0062", "service": "ec2-auto-scaling", "where": "1-fast.md#changed-recently",
     "question": "Set changed.date 2024-10-01 and changed.was (before: an account could create launch configurations through the API, the AWS CLI and CloudFormation) with evidence on ec2-auto-scaling-launch-configurations-blocked-for-new-accounts",
     "effect": "without it the launch configuration entry of Changed recently fails the date rule (L107); the entry stays planned or carries a needs-display marker. Filed 2026-10-13 by brief-17."},
    {"id": "fr-0063", "service": "ec2-auto-scaling", "where": "1-fast.md#changed-recently",
     "question": "Set changed.date 2022-11-10 (new feature, changed.was: not available) with evidence on ec2-auto-scaling-change-price-capacity-optimized-2022",
     "effect": "without it the Spot strategy entry stays planned. Filed 2026-10-13 by brief-17."},
    {"id": "fr-0064", "service": "ec2-auto-scaling", "where": "2-deep.md#numbers-that-decide-answers",
     "question": "Set changed.date 2026-08-17 and changed.was (before: TerminateInstanceInAutoScalingGroup took one instance ID per call) with evidence on ec2-auto-scaling-change-batch-termination-2026",
     "effect": "without it the not-examinable entry under the B-list is left out; nothing else depends on it. Filed 2026-10-13 by brief-17."},
]

brief["notes_for_orchestrator"] = [
    "Only verified facts are named: chapter-17 facts from fact-cards.md (522 verified, 2026-10-13), plus verified facts of other chapters: ec2- (chapter 16: launch templates, resize, hibernation, Spot, user data, billing), elb- (chapter 14: health checks, deregistration delay, slow start, sticky sessions), global-infrastructure- (chapter 02). brief_check.py checks every fact id in this file (not only the sections and traps that gate_brief reads) and every bracketed display against the canon; its last run is in brief_check.out.",
    "Structure: 13 How-it-works subsections (the deep template allows 8 to 14). A 14-subsection plan was dropped because, at the 3,500-word cap, each subsection would have kept about 70 words of trace after its five devices. Horizontal versus vertical scaling (2.1.K6) is therefore taught in the fast compare table and in subsection 12 (stopped instances, warm pools, hibernation), not in a subsection of its own; AWS Auto Scaling and Application Auto Scaling are taught in the fast compare table and the 2-services.md card (registry cards: aws-auto-scaling).",
    "File budget: How it works = 13 subsections at 230 to 255 words all-in at most (sum 3,060) + 4 Go deeper blocks of at most 70 words + 2 Spot the bug prompts (about 110) + the intro line, at most about 3,480 of the 3,500 cap; writers aim about 100 words lower and cut the body_extras sentences first. 2-deep.md: about 3,400 + Numbers 290 + Decision record 270 + FAQ 430 = about 4,390 of the 4,500 cap; the real-world box fits only if the file stays at or under 4,380 words without it, which is unlikely.",
    "Traps: 13 (the U5 cap): 5 in the fast list, 8 as Exam trap callouts in 2-deep.md. 2-deep.md callouts: 8 Exam trap + 2 Try it + 1 Startup example = 11 of 12. Ben's question (STARTUP chapter 17) is chapter 14's trap elb-trap-lb-replaces-instance and card elb-c004: this brief reuses that id (traps_from_other_chapters, q02 distractors, s01) and defines the different trap auto-scaling-trap-elb-checks-on-by-default (the group ignores ELB checks by default).",
    "Changed recently: three examinable fast entries. The predictive forecast cadence entry (2023-01-06) is ready. The launch configuration entry (2024-10-01, fr-0062) and the Spot strategy entry (2022-11-10, fr-0063) need changed records on their facts. Under the B-list: the not-examinable batch termination change (2026-08-17, fr-0064), written only when filled. These three requests are open; the counts gate (B09) blocks finalize until they are filled or closed as unfillable.",
    "STARTUP check: the decision record keeps the three options, the qualifier 'most cost-effective', the choice (target tracking plus a scheduled action that raises capacity to 6 at 08:45 on weekdays; minimum 3, maximum 12) and the trade-off (a spike waits about 4 minutes, so the minimum stays at 3) of data/startup.json. Story conflict to fix in data/startup.json or accept: its chapter-17 'diagram' says 'Before: one fixed instance', but chapter 14's decision left one web instance in each of three zones; the before diagram here says 'fixed capacity' with no count.",
    "Demand gaps kept from brief.v0: d05 was contradicted (the grace period is 300 seconds only in the console; 0 with the AWS CLI or an SDK: the chapter teaches both); d12 (no fact states what the API does when desired capacity is set outside the minimum and maximum: no sentence and no key on it); d28 (the two-alarm count is stated only in the SQS walkthrough: t03 and the trace cite ec2-auto-scaling-target-tracking-creates-two-alarms with that scope); d49 (no AWS page calls a resized single instance a single point of failure: the book says only what the facts say); d78 partial (only NASA JPL and Canva case facts are verified).",
    "Task costs: t02 needs a price fact for the smallest instance type and t03 one for CloudWatch alarms; neither is in the canon as far as this brief knows. The task writer checks the ec2 and monitoring facts and files requests where needed; no price from memory.",
    "Term requests: launch template, desired capacity, scaling policy, target tracking scaling policy, step scaling policy, simple scaling policy, scheduled action, predictive scaling, cooldown, instance warmup, health check grace period, lifecycle hook, termination policy, scale-in protection, warm pool, instance refresh, mixed instances policy, Capacity Rebalancing, immutable infrastructure, backlog per instance, maximum instance lifetime, instance maintenance policy, hibernation and Standby are not in data/terms.json; writers use needs-term markers until they are added. The bank's 'standby' means a database standby; the Auto Scaling state needs its own entry or a respelling note.",
    "Not examinable yet and left out of answers: the CloudFormation AutoScalingInstanceRefresh update policy (2026-07-29) and batch termination (2026-08-17). The 'reservations then balanced' Availability Zone strategy (2026-06-30) is inside the window but niche: left out.",
]

OUT.write_text(json.dumps(brief, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {OUT} sections={len(brief['sections'])} traps={len(brief['traps'])} slots={len(brief['question_slots'])} "
      f"cards={len(brief['cards'])} diagrams={len(brief['diagrams'])}")
