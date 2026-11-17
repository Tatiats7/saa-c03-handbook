import json, sys
# usage: fixdisp.py SPEC.json  (replaces known long displays)
rep = {
 "more comprehensively than the basic monitoring provided by default": "more comprehensively than the basic monitoring",
 "a custom metric corresponding to each unique dimension combination": "each unique dimension combination",
 "without needing to run a separate trace collection daemon": "a separate trace collection daemon",
 "reduce the number of agents that you run and manage": "reduce the number of agents",
 "install the CloudWatch agent on a fleet of Amazon EC2 instances": "a fleet of Amazon EC2 instances",
 "don't need to also have the `cloudwatch:PutMetricData` permission": "`cloudwatch:PutMetricData` permission",
 "supported only for log groups in the Standard log class": "the Standard log class",
 "assign dimensions to a metric created by a metric filter": "metric created by a metric filter",
 "CloudWatch or Amazon Managed Service for Prometheus, or to both": "Amazon Managed Service for Prometheus, or to both",
 "use it when you install the agent on other servers": "install the agent on other servers",
}
p = sys.argv[1]
s = json.load(open(p))
for f in s:
    for v in f["v"]:
        if v[1] in rep:
            v[1] = rep[v[1]]
json.dump(s, open(p, "w"), indent=1)
