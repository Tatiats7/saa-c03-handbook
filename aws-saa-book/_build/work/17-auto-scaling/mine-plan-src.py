import json
urls = [u.strip() for u in open("/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/17-auto-scaling/urls.txt") if u.strip()]
import re
def sid(u):
    u = re.sub(r"^https://docs\.aws\.amazon\.com/", "docs/", u)
    u = re.sub(r"^https://aws\.amazon\.com/", "www/", u)
    u = re.sub(r"\.html$", "", u).rstrip("/")
    return u
brief = json.load(open("/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/17-auto-scaling/brief.v0.json"))
lenses = {
 "numbers": {"what": "Every number, limit, default and quota: quotas tables (use `tables`), default cooldown, grace period, warmup, hook timeout, refresh percentages, max instance lifetime minimum, predictive scaling history and horizon, hibernation limits, pricing lines. Adopt table rows with their header text.", "pages": [], "demand": []},
 "behavior": {"what": "How each mechanism works and every can / cannot / only / by default statement: health checks and replacement, lifecycle and hooks, scaling policy types and their interaction, termination, protection, standby, AZ balance, launch templates vs configurations, warm pools, hibernation prerequisites, mixed instances and Spot, vertical vs horizontal.", "pages": [], "demand": []},
 "decisions+changes": {"what": "Decision guidance (Well-Architected, whitepaper, decision guide, scaling-method page), the Callvale decision facts, real company examples, and every change item since 2022-07 as a change fact with date and old value only where the history row states it; mark GA after 2026-07-15 as not examinable yet.", "pages": [], "demand": []},
 "faq": {"what": "The two FAQ pages: one fact per quick-fire item with the verbatim FAQ sentence (quote from the snapshot, not the index); EC2 Auto Scaling vs AWS Auto Scaling vs Application Auto Scaling; pricing answers.", "pages": [], "demand": []},
}
page_lens = {}
for u in urls:
    s = sid(u)
    if "/faqs" in s: page_lens[s] = ["faq"]
    elif "/pricing" in s: page_lens[s] = ["numbers", "faq"]
    elif "case-studies" in s or "wellarchitected" in s or "whitepapers" in s or "decision-guides" in s or "DocumentHistory" in s or "doc-history" in s or "plans/userguide" in s or "scaling-overview" in s or "scale-your-group" in s or "migrate-to-launch-templates" in s: page_lens[s] = ["decisions+changes"]
    elif "quotas" in s: page_lens[s] = ["numbers"]
    else: page_lens[s] = ["behavior"]
# pages that also carry numbers
for key in ["ec2-auto-scaling-scaling-cooldowns", "health-check-grace-period", "ec2-auto-scaling-default-instance-warmup", "lifecycle-hooks-overview", "predictive-scaling-policy-overview", "asg-max-instance-lifetime", "understand-instance-refresh-default-values", "as-enter-exit-standby", "hibernating-prerequisites", "instance-hibernate-overview", "asg-capacity-limits", "spot-interruptions", "ec2-auto-scaling-detach-attach-instances", "as-scaling-target-tracking", "ec2-auto-scaling-warm-pools"]:
    for s in page_lens:
        if s.endswith("/" + key) and "numbers" not in page_lens[s]: page_lens[s].append("numbers")
# pages that also carry change facts
for key in ["launch-configurations", "policy-creating-high-resolution-metrics", "ec2-auto-scaling-target-tracking-metric-math", "replace-root-volume", "instance-lifecycle-policy", "launch-instances-synchronously", "ec2-auto-scaling-zonal-shift", "ec2-auto-scaling-availability-zone-balanced", "use-ec2-capacity-reservations", "prepare-for-lifecycle-notifications", "ec2-auto-scaling-warm-pools", "ec2-auto-scaling-instance-maintenance-policy", "allocation-strategies", "as-using-sqs-queue"]:
    for s in page_lens:
        if s.endswith("/" + key) and "decisions+changes" not in page_lens[s]: page_lens[s].append("decisions+changes")
for s, ls in page_lens.items():
    for l in ls: lenses[l]["pages"].append(s)
for item in brief["demand"]:
    lenses[item["lens"]]["demand"].append(item["id"])
plan = {"chapter": "17", "by": "plan-17", "url_list": "_build/work/17-auto-scaling/urls.txt", "fetch_report": "_build/work/17-auto-scaling/fetch-batch.txt",
        "feeds": {"changes": ["_build/work/17-auto-scaling/changes-ec2-auto-scaling.txt", "_build/work/17-auto-scaling/changes-aws-auto-scaling.txt"], "faq_lists": ["_build/work/17-auto-scaling/faq-ec2-auto-scaling.txt", "_build/work/17-auto-scaling/faq-aws-auto-scaling.txt"], "cases": ["_build/work/17-auto-scaling/cases-ec2-auto-scaling.txt", "_build/work/17-auto-scaling/cases-auto-scaling.txt"]},
        "rules": ["Quote only from page snapshots (snap/), never from full.md or the faq index.", "Each demand item lists `look_in` source ids; mark it filled, contradicted (with what the page says) or not-found.", "A change item becomes a change fact with its date; old value only when the history row or What's New item states it verbatim.", "Anything GA after 2026-07-15 is labelled not examinable yet (RULINGS rule 7).", "Facts live in the namespace of their service key: ec2-auto-scaling or aws-auto-scaling (Application Auto Scaling facts go under aws-auto-scaling unless the registry says otherwise)."],
        "lenses": lenses}
json.dump(plan, open("/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/17-auto-scaling/mine-plan.json", "w"), indent=1)
print({k: (len(v["pages"]), len(v["demand"])) for k, v in lenses.items()}, len(page_lens))
