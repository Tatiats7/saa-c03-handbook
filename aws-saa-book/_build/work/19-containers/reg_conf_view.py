"""register-19: list the conflicts that involve chapter 19 facts (read-only)."""
import json
W = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/19-containers/"
c = json.load(open(W + "reg-conflicts.json"))
pre = ("ecr-", "ecs-", "eks-", "fargate-")
for x in c["conflicts"]:
    if any(f.startswith(pre) for f in x["facts"]):
        print(x["id"], x.get("status"), " / ".join(x["facts"]), "|", (x.get("reason") or "")[:160])
