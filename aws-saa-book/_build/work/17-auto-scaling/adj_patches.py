"""adjudicate-17: build one amend patch per disputed fact (repair once; claims narrowed to the quotes, or quotes added from the same pages)."""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT = pathlib.Path(__file__).resolve().parent / "adj-patches"
OUT.mkdir(exist_ok=True)

facts = {}
for svc in ("ec2-auto-scaling", "aws-auto-scaling"):
    for l in (ROOT / "data/facts" / f"{svc}.jsonl").read_text().splitlines():
        if l.strip():
            f = json.loads(l)
            facts[f["id"]] = f

DG = {"source_id": "docs/decision-guides/latest/decision-guides/choosing-aws-compute-service",
      "url": "https://docs.aws.amazon.com/decision-guides/latest/decision-guides/choosing-aws-compute-service.html",
      "title": "Choosing an AWS compute service"}

E = "ec2-auto-scaling-"
# id -> dict(claim=..., qualifiers=partial dict, values=list, add=[quotes on an existing source] or [(src_dict, quote)], replace={old_quote: new_quote}, question=..., note=...)
P = {
 "aws-auto-scaling-wa-ec2-auto-scaling-for-instances-application-auto-scaling-for-other-services": dict(
   claim="Well-Architected rule of thumb: use Amazon EC2 Auto Scaling for EC2 instances and Application Auto Scaling for other AWS services, such as AWS Lambda functions or Amazon ECS services."),
 E+"capacity-reservation-none-and-default": dict(
   claim="With the Capacity Reservation preference none, Auto Scaling does not launch instances into a Capacity Reservation and instances run as On-Demand capacity; with default, it uses the Capacity Reservation specification from the launch template, unless the group uses distribution segments, in which case it consumes reservations in the priority order of the segments.",
   add=["If your Auto Scaling group uses distribution segments, Auto Scaling instead consumes reservations according to the priority order defined in the distribution segments."]),
 E+"change-warm-pool-mixed-instances-2025": dict(
   claim="Since November 4, 2025 you can add a warm pool to an Auto Scaling group that has a mixed instances policy, when the policy is configured for On-Demand Instances only and the group does not use instance weighting (warm pools support neither Spot Instances in mixed instance groups nor weighted mixed instance groups).",
   qualifiers={"condition": "the mixed instances policy is On-Demand only and the group does not use instance weighting"},
   add=["Warm pools aren’t supported with weighted mixed instance groups.", "If your Auto Scaling group uses instance weighting, you can’t add a warm pool."],
   values_add=[{"key": "weighted", "display": "you can’t add a warm pool"}]),
 E+"control-plane-outage-no-effect": dict(
   qualifiers={"scope": "per existing Auto Scaling group"}),
 E+"dynamic-target-tracking-definition": dict(
   claim="Target tracking scaling increases and decreases the group's current capacity based on a CloudWatch metric and a target value; it works similar to a thermostat: you select a temperature and the thermostat does the rest.",
   replace={"**Target tracking scaling**—Increase and decrease the current capacity of the group based on a Amazon CloudWatch metric and a target value.":
            "**Target tracking scaling**—Increase and decrease the current capacity of the group based on a Amazon CloudWatch metric and a target value. It works similar to the way that your thermostat maintains the temperature of your home—you select a temperature and the thermostat does the rest."}),
 E+"dynamic-target-tracking-with-step-caution": dict(
   claim="Combining target tracking and step scaling policies needs caution: if a step scaling policy starts a scale-in before the target tracking policy is ready to scale in, the scale-in is not blocked, and after it completes the target tracking policy could instruct the group to scale out again.",
   add=["After the scale in activity completes, the target tracking policy could instruct the group to scale out again."]),
 E+"faq-elb-requests-before-detection-fail": dict(
   claim="When ELB notices that an instance is unhealthy it stops routing requests to it, but before it discovers that the instance is unhealthy, some requests to that instance fail.",
   question="What happens to requests that reach an instance before ELB marks it unhealthy?"),
 E+"faq-groups-created-outside-aws-auto-scaling": dict(
   claim="EC2 Auto Scaling groups must be created and configured outside of AWS Auto Scaling, for example through the EC2 console, the Auto Scaling API or CloudFormation; AWS Auto Scaling can help you configure dynamic scaling policies for existing groups."),
 E+"faq-iam-resource-level-permissions": dict(
   claim="With Amazon EC2 Auto Scaling resource-level permissions, you can restrict access to a particular Auto Scaling group or launch configuration."),
 E+"faq-predictive-policy-vs-scaling-plan": dict(
   claim="A predictive scaling policy brings a prediction algorithm similar to the one offered through an AWS Auto Scaling plan into EC2 Auto Scaling as a native scaling policy, so you do not have to create a scaling plan just to use predictive scaling."),
 E+"instance-refresh-checkpoints": dict(
   claim="A checkpoint is a point in time where the instance refresh pauses for a specified amount of time, which lets you deploy updates in phases; without checkpoints, rolling replacements are performed continuously."),
 E+"instance-refresh-retry-timeout": dict(
   claim="When an instance refresh cannot continue making replacements, because it is waiting to replace instances on standby or protected from scale in, or because the new instances do not pass their health checks, Amazon EC2 Auto Scaling keeps retrying for an hour; if the problem persists, the operation fails."),
 E+"instance-refresh-use-cases": dict(
   claim="An instance refresh can help you deploy a new AMI or user data script across the group, migrate instances to new instance types, or switch a group from a launch configuration to a launch template.",
   add=["Migrating your instances to new instance types to take advantage of the latest improvements and optimizations.",
        "Switching your Auto Scaling groups from using a launch configuration to using a launch template."]),
 E+"launch-in-az-with-fewest": dict(
   claim="EC2 Auto Scaling tries to maintain equivalent numbers of instances in each enabled Availability Zone by attempting to launch new instances in the zone with the fewest instances."),
 E+"launch-template-latest-version-passrole-risk": dict(
   claim="When a group uses the $Latest or $Default launch template version, later launches use that version, even if it has changed, with the permissions of the service-linked role, so a user who can update the template could pass an IAM role to instances without iam:PassRole; the autoscaling:LaunchTemplateVersionSpecified condition key limits who can configure groups to use $Latest or $Default.",
   add=["After the initial verification and request are complete, whenever instances launch, Amazon EC2 Auto Scaling launches them with the latest or default version, even if it has changed, using the permissions of its [service-linked role](autoscaling-service-linked-role.md#service-linked-role-permissions)."]),
 E+"lifecycle-hook-scale-in-use": dict(
   claim="An example use of a lifecycle hook on scale in: the hook pauses the instance before it is terminated and sends a notification using Amazon EventBridge; while the instance is in the wait state, you can invoke a Lambda function or connect to the instance to download logs or other data."),
 E+"lifecycle-hook-user-data-complete": dict(
   claim="A user data script can perform custom actions on instances as they launch without a notification target; to signal that the lifecycle action is complete, the script must call CompleteLifecycleAction, and you must create an IAM role with a policy that allows the instances to call this API."),
 E+"process-alarm-notification": dict(
   claim="The AlarmNotification process accepts notifications from the CloudWatch alarms that are associated with the group's dynamic scaling policies."),
 E+"rebalance-exceed-max-margin": dict(
   claim="During a rebalancing activity the group can temporarily exceed its maximum capacity, by default by 10 percent or one instance, whichever is greater; the margin is extended only if the group is at or near maximum capacity and needs rebalancing, and the extension lasts only as long as needed to rebalance (typically a few minutes).",
   add=["The extension lasts only as long as needed to rebalance the group (typically a few minutes)."]),
 E+"rebalance-triggers": dict(
   claim="A group can become unbalanced and Availability Zone rebalancing can follow when you change its Availability Zones, when you explicitly terminate or detach instances or place them in standby, when a zone that lacked capacity recovers, or when a zone's Spot price falls from above to below your maximum price.",
   add=["An Availability Zone that previously had a Spot price above your maximum price now has a Spot price below your maximum price."]),
 E+"require-imdsv2-launch-template": dict(
   claim="For extra security, you can set your users' permissions to require the use of a launch template that requires IMDSv2.",
   question="Can IAM permissions make users choose a launch template that requires IMDSv2?"),
 E+"scale-in-protection-group-setting-new-only": dict(
   claim="When you enable the group's scale-in protection setting, all new instances launched by the group have scale-in protection; enabling or disabling the setting does not affect existing instances.",
   qualifiers={"scope": "per Auto Scaling group (scale-in protection setting)"},
   add=["When you enable it, all new instances launched by the group will have instance scale-in protection enabled."]),
 E+"scaling-methods": dict(
   claim="EC2 Auto Scaling can scale by schedule, as a function of date and time; dynamically, with a scaling policy that resizes the group to meet changes in demand; and predictively, combined with dynamic scaling, to add instances in advance of daily and weekly traffic patterns.",
   question="Which scaling methods besides manual scaling does EC2 Auto Scaling offer?"),
 E+"sqs-metric-math-instead-of-custom": dict(
   claim="Instead of publishing a custom backlog-per-instance metric, you can calculate it with CloudWatch metric math (the approximate number of messages available for retrieval divided by the number of InService instances), which saves the cost and effort of publishing your own metric."),
 E+"sqs-queue-length-not-proportional": dict(
   claim="The issue with target tracking on ApproximateNumberOfMessagesVisible is that the number of messages in the queue might not change proportionally to the size of the group that processes them."),
 E+"target-tracking-creates-two-alarms": dict(
   claim="Amazon EC2 Auto Scaling creates and manages the CloudWatch alarms of a target tracking policy; in the AWS SQS walkthrough, creating the policy creates two alarms: one for scaling out and one for scaling in.",
   qualifiers={"scope": "per target tracking scaling policy (AWS SQS CLI example)"},
   add=[({"source_id": "docs/autoscaling/ec2/userguide/as-scaling-target-tracking"},
         "Amazon EC2 Auto Scaling creates and manages the CloudWatch alarms that invoke scaling events when the metric deviates from the target.")]),
 E+"target-tracking-metric-must-fall-as-capacity-grows": dict(
   claim="Target tracking assumes the metric is inversely proportional to group capacity (when capacity increases, the metric should decrease by nearly the same proportion), so converting metrics is essential; metric math is particularly useful to convert existing metrics into average per-instance values."),
 E+"target-tracking-unsuitable-metrics": dict(
   claim="The load balancer RequestCount and Latency metrics do not work for target tracking: the number of requests doesn't change based on the group's utilization, and latency can increase with utilization but doesn't necessarily change proportionally."),
 E+"unhealthy-replacement-10-percent-at-a-time": dict(
   claim="By default, Amazon EC2 Auto Scaling replaces up to 10 percent of the group's desired capacity at a time until all unhealthy instances are replaced; in a group so small that 10 percent is less than one instance it replaces them one at a time, and an instance maintenance policy can modify the 10 percent value.",
   qualifiers={"default_or_max": "default", "condition": "groups where 10 percent of desired capacity is at least one instance; no instance maintenance policy changes the rate"},
   add=["If the size of an Auto Scaling group is small enough that the resulting value of 10 percent is less than one, Amazon EC2 Auto Scaling instead replaces the unhealthy instances one at a time.",
        "You can modify the default 10 percent value by [setting an instance maintenance policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/set-instance-maintenance-policy-on-group.html) to change the rate at which Auto Scaling replaces unhealthy instances."]),
 E+"vertical-resize-instance-type": dict(
   claim="Vertical scaling (scaling up) adds more power to existing infrastructure, such as more CPU or memory for an instance; you resize an EC2 instance by changing its instance type, and you then pay the rate of the new instance type.",
   add=[(DG, "The scalability of a service can be **vertical**, allowing you to scale up by adding more power to your existing infrastructure (like increasing the CPU or memory of an instance), or **horizontal**, helping you to scale out by adding more instances to handle the load.")]),
 E+"vertical-stop-required": dict(
   claim="You must stop an EBS-backed instance before you can change its instance type, so plan for downtime while the instance is stopped."),
 E+"wa-immutable-infrastructure-definition": dict(
   claim="Well-Architected defines immutable infrastructure as a model where no updates, security patches or configuration changes happen in place on production workloads; a change is built onto new infrastructure and deployed, which also lets remote access such as SSH be disabled."),
 E+"wa-instance-scheduler-cannot-stop-group-instances": dict(
   claim="AWS Instance Scheduler cannot stop and start instances that are part of an Auto Scaling group; Auto Scaling groups have their own scheduling for the instances in the group."),
 E+"wa-predictive-scaling-before-projected-load": dict(
   claim="Well-Architected cost advice: consider predictive scaling for regular traffic spikes and applications that take a long time to start, because it initializes capacity before projected load, while dynamic scaling alone is reactive."),
 E+"wa-queue-depth-metric-for-batch-work": dict(
   claim="For a video transcoding application, 100% CPU utilization is expected and should not be the primary scaling metric; use the depth of the transcoding job queue instead, and the metric value must increase or decrease proportionally to the number of instances in the group.",
   question="What metric should a video transcoding worker tier scale on?"),
 E+"wa-scaling-metric-examples": dict(
   claim="Typical scaling metrics include CPU utilization, work queue depth such as an Amazon SQS queue, number of active users and network throughput; a scaling metric is one that corresponds to the workload's demand."),
 E+"wa-three-scaling-options": dict(
   claim="Well-Architected names three major options to scale automatically: metric-based scaling, scheduled scaling (often for predictable demand such as weekday business hours or sales events), and predictive scaling, which uses machine learning to scale resources based on anticipated demand."),
 E+"warm-pool-unnecessary-cost": dict(
   claim="Creating a warm pool when it is not required can lead to unnecessary costs: if first boot time does not cause noticeable latency issues for the application, you probably do not need a warm pool."),
 E+"whitepaper-group-per-tier": dict(
   claim="The web hosting whitepaper, which is marked as a historical reference, describes multiple Auto Scaling groups for different layers of the architecture, so each layer can scale independently, for example on network I/O for web servers and CPU utilization for application servers.",
   add=["This whitepaper is for historical reference only."]),
 E+"zonal-shift-is-arc-feature": dict(
   claim="Zonal shift is a capability of Amazon Application Recovery Controller (ARC); enabling it registers the Auto Scaling group with the ARC zonal shift service, and during an active zonal shift the group treats that Availability Zone as impaired.",
   add=["Then, you can start a zonal shift using the AWS Management Console, AWS CLI, or API and the Auto Scaling group treats the Availability Zone with an active zonal shift as impaired."]),
}

def ev_from(base, quote):
    e = {k: base[k] for k in ("source_id", "url", "title", "sha256") if k in base}
    e["quote"] = quote
    e["table_header"] = None
    return e

for fid, p in P.items():
    f = facts[fid]
    assert f["status"] == "disputed", fid
    patch = {}
    if "claim" in p:
        patch["claim"] = p["claim"]
    if "question" in p:
        patch["question"] = p["question"]
    if "qualifiers" in p:
        q = dict(f["qualifiers"]); q.update(p["qualifiers"]); patch["qualifiers"] = q
    if "values_add" in p:
        patch["values"] = f["values"] + p["values_add"]
    if "add" in p or "replace" in p:
        ev = []
        for e in f["evidence"]:
            e2 = {k: e[k] for k in ("source_id", "url", "quote", "table_header", "sha256", "title") if k in e}
            if "heading" in e:
                e2["heading"] = e["heading"]
            if p.get("replace") and e["quote"] in p["replace"]:
                e2["quote"] = p["replace"][e["quote"]]
                e2.pop("sha256", None)
            ev.append(e2)
        for a in p.get("add", []):
            if isinstance(a, tuple):
                src, quote = a
                same = [e for e in f["evidence"] if e["source_id"] == src["source_id"]]
                base = same[0] if same else src
                if not same and "url" not in base:
                    sid = src["source_id"]
                    base = dict(src, url="https://docs.aws.amazon.com/" + sid[len("docs/"):] + ".html")
                ev.append(ev_from(base, quote))
            else:
                ev.append(ev_from(f["evidence"][0], a))
        patch["evidence"] = ev
    (OUT / f"{fid}.json").write_text(json.dumps(patch, indent=1, ensure_ascii=False) + "\n")
print(f"wrote {len(P)} patches to {OUT}")
