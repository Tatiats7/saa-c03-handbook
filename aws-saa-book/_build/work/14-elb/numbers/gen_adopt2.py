"""Adopt input files for health-check settings tables and other table rows (chapter 14, numbers lens)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
D = "docs/elasticloadbalancing/latest/"
AH = D + "application/target-group-health-checks"
NH = D + "network/target-group-health-checks"
GH = D + "gateway/health-checks"
AL = D + "application/load-balancer-access-logs"

# (file, src, table, row, id, kind, claim, question, [(display, spoken)], scope, dom, adj, bullets, relevance, tier0, condition)
R = [
 ("h-alb-protocol", AH, 0, 0, "elb-alb-health-check-protocol-default-http", "default",
  "Application Load Balancer health checks use HTTP or HTTPS with the HTTP GET method; the default protocol is HTTP.",
  "Which protocols can Application Load Balancer health checks use, and which is the default?",
  [("The default is the HTTP protocol", "the default is HTTP"), ("the possible protocols are HTTP and HTTPS", "HTTP and HTTPS")],
  "per Application Load Balancer target group", "default", True, ["2.2.K8"], "core", False, ""),
 ("h-alb-port", AH, 0, 1, "elb-alb-health-check-port-default-traffic-port", "default",
  "By default, an Application Load Balancer health check uses the port on which each target receives traffic from the load balancer.",
  "Which port does an Application Load Balancer health check use by default?",
  [("port on which each target receives traffic", "the traffic port"), ("The default is to use the port", "the default is the traffic port")],
  "per Application Load Balancer target group", "default", True, ["2.2.K8"], "extended", False, ""),
 ("h-alb-path", AH, 0, 2, "elb-alb-health-check-path-default-slash", "default",
  "The default Application Load Balancer health check path is / for HTTP/1.1 or HTTP/2 target groups and /AWS.ALB/healthcheck for gRPC target groups.",
  "What is the default health check path of an Application Load Balancer target group?",
  [("The default is /.", "the default path is slash"), ("/AWS.ALB/healthcheck", "slash AWS dot ALB slash healthcheck")],
  "per Application Load Balancer target group", "default", True, ["2.2.K8"], "extended", False, ""),
 ("h-alb-timeout", AH, 0, 3, "elb-alb-health-check-timeout-default-5-seconds", "default",
  "The Application Load Balancer health check timeout can be 2 to 120 seconds; the default is 5 seconds for instance or ip targets and 30 seconds for lambda targets.",
  "What is the default health check timeout of an Application Load Balancer target group, and what range is allowed?",
  [("5 seconds", "five seconds"), ("30 seconds", "thirty seconds"), ("2 to 120 seconds", "two to one hundred twenty seconds")],
  "per Application Load Balancer target group", "default", True, ["2.2.K8"], "extended", False, ""),
 ("h-alb-interval", AH, 0, 4, "elb-alb-health-check-interval-default-30-seconds", "default",
  "The Application Load Balancer health check interval can be 5 to 300 seconds; the default is 30 seconds for instance or ip targets and 35 seconds for lambda targets.",
  "What is the default health check interval of an Application Load Balancer target group, and what range is allowed?",
  [("30 seconds", "thirty seconds"), ("35 seconds", "thirty-five seconds"), ("5 to 300 seconds", "five to three hundred seconds")],
  "per Application Load Balancer target group", "default", True, ["2.2.K8"], "core", True, ""),
 ("h-alb-healthy", AH, 0, 5, "elb-alb-healthy-threshold-default-5", "default",
  "An unhealthy Application Load Balancer target must pass 5 consecutive health checks by default before it is healthy again; the range is 2 to 10.",
  "How many consecutive successful health checks does an Application Load Balancer need by default before a target is healthy?",
  [("5 consecutive health checks", "five consecutive health checks"), ("2 to 10", "two to ten")],
  "per Application Load Balancer target group", "default", True, ["2.2.K8"], "extended", False, ""),
 ("h-alb-unhealthy", AH, 0, 6, "elb-alb-unhealthy-threshold-default-2", "default",
  "An Application Load Balancer target is considered unhealthy after 2 consecutive failed health checks by default; the range is 2 to 10.",
  "How many consecutive failed health checks make an Application Load Balancer target unhealthy by default?",
  [("2 consecutive failed health checks", "two consecutive failed health checks"), ("2 to 10", "two to ten")],
  "per Application Load Balancer target group", "default", True, ["2.2.K8"], "core", False, ""),
 ("h-alb-matcher", AH, 0, 7, "elb-alb-health-check-success-code-default-200", "default",
  "For HTTP/1.1 or HTTP/2 target groups, Application Load Balancer health check success codes can be from 200 to 499 and the default is 200; for gRPC the codes are 0 to 99 and the default is 12.",
  "What success codes does an Application Load Balancer health check accept by default?",
  [("200 to 499", "two hundred to four ninety-nine"), ("The default value is 200", "the default is two hundred"), ("The default value is 12", "the default is twelve")],
  "per Application Load Balancer target group", "default", True, ["2.2.K8"], "extended", False, ""),
 ("h-nlb-protocol", NH, 0, 0, "elb-nlb-health-check-protocol-default-tcp", "default",
  "Network Load Balancer health checks can use HTTP, HTTPS or TCP; the default is TCP, and for alb target groups only HTTP and HTTPS are supported.",
  "Which protocols can Network Load Balancer health checks use, and which is the default?",
  [("The default is the TCP protocol", "the default is TCP"), ("HTTP, HTTPS, and TCP", "HTTP, HTTPS and TCP")],
  "per Network Load Balancer target group", "default", True, ["2.2.K8"], "core", False, ""),
 ("h-nlb-timeout", NH, 0, 3, "elb-nlb-health-check-timeout-default", "default",
  "The Network Load Balancer health check timeout can be 2 to 120 seconds; the default is 6 seconds for HTTP health checks and 10 seconds for TCP and HTTPS health checks.",
  "What is the default health check timeout of a Network Load Balancer target group?",
  [("6 seconds", "six seconds"), ("10 seconds", "ten seconds"), ("2 to 120 seconds", "two to one hundred twenty seconds")],
  "per Network Load Balancer target group", "default", True, ["2.2.K8"], "reference", False, ""),
 ("h-nlb-interval", NH, 0, 4, "elb-nlb-health-check-interval-default-30-seconds", "default",
  "The Network Load Balancer health check interval can be 5 to 300 seconds with a default of 30 seconds, and because the health checks are distributed, targets receive more than the configured number of checks.",
  "What is the default health check interval of a Network Load Balancer target group?",
  [("30 seconds", "thirty seconds"), ("5 to 300 seconds", "five to three hundred seconds")],
  "per Network Load Balancer target group", "default", True, ["2.2.K8"], "extended", False, ""),
 ("h-nlb-healthy", NH, 0, 5, "elb-nlb-healthy-threshold-default-5", "default",
  "A Network Load Balancer target needs 5 consecutive successful health checks by default before an unhealthy target is considered healthy; the range is 2 to 10.",
  "What is the default healthy threshold of a Network Load Balancer target group?",
  [("5 consecutive successful health checks", "five consecutive successful health checks"), ("2 to 10", "two to ten")],
  "per Network Load Balancer target group", "default", True, ["2.2.K8"], "reference", False, ""),
 ("h-nlb-unhealthy", NH, 0, 6, "elb-nlb-unhealthy-threshold-default-2", "default",
  "A Network Load Balancer target is considered unhealthy after 2 consecutive failed health checks by default; the range is 2 to 10.",
  "What is the default unhealthy threshold of a Network Load Balancer target group?",
  [("2 consecutive failed health checks", "two consecutive failed health checks"), ("2 to 10", "two to ten")],
  "per Network Load Balancer target group", "default", True, ["2.2.K8"], "reference", False, ""),
 ("h-nlb-matcher", NH, 0, 7, "elb-nlb-health-check-success-codes-default-200-399", "default",
  "For HTTP or HTTPS health checks, a Network Load Balancer accepts success codes from 200 to 599, and the default is 200-399.",
  "What HTTP success codes does a Network Load Balancer health check use by default?",
  [("200 to 599", "two hundred to five ninety-nine"), ("200-399", "two hundred to three ninety-nine")],
  "per Network Load Balancer target group", "default", True, ["2.2.K8"], "reference", False, "HTTP or HTTPS health checks"),
 ("h-gwlb-protocol", GH, 0, 0, "elb-gwlb-health-check-protocol-default-tcp", "default",
  "Gateway Load Balancer health checks can use HTTP, HTTPS or TCP; the default is TCP.",
  "Which protocols can Gateway Load Balancer health checks use, and which is the default?",
  [("The default is TCP", "the default is TCP"), ("HTTP, HTTPS, and TCP", "HTTP, HTTPS and TCP")],
  "per Gateway Load Balancer target group", "default", True, ["2.2.K8"], "reference", False, ""),
 ("h-gwlb-port", GH, 0, 1, "elb-gwlb-health-check-port-default-80", "default",
  "The Gateway Load Balancer health check port can be 1 to 65535; the default is 80.",
  "Which port does a Gateway Load Balancer health check use by default?",
  [("The default is 80", "the default is eighty"), ("1 to 65535", "one to sixty-five thousand five hundred thirty-five")],
  "per Gateway Load Balancer target group", "default", True, ["2.2.K8"], "reference", False, ""),
 ("h-gwlb-timeout", GH, 0, 3, "elb-gwlb-health-check-timeout-default-5", "default",
  "The Gateway Load Balancer health check timeout can be 2 to 120 seconds; the default is 5.",
  "What is the default health check timeout of a Gateway Load Balancer target group?",
  [("The default is 5", "the default is five"), ("2 to 120", "two to one hundred twenty")],
  "per Gateway Load Balancer target group", "default", True, ["2.2.K8"], "reference", False, ""),
 ("h-gwlb-interval", GH, 0, 4, "elb-gwlb-health-check-interval-default-10-seconds", "default",
  "The Gateway Load Balancer health check interval can be 5 to 300 seconds with a default of 10 seconds, and it must be greater than or equal to the health check timeout.",
  "What is the default health check interval of a Gateway Load Balancer target group?",
  [("10 seconds", "ten seconds"), ("5 to 300", "five to three hundred")],
  "per Gateway Load Balancer target group", "default", True, ["2.2.K8"], "reference", False, ""),
 ("h-gwlb-matcher", GH, 0, 7, "elb-gwlb-health-check-success-codes-200-399", "restriction",
  "For HTTP or HTTPS health checks, the Gateway Load Balancer success codes must be 200-399.",
  "Which HTTP success codes does a Gateway Load Balancer health check use?",
  [("This value must be 200-399", "it must be two hundred to three ninety-nine"), ("200-399", "two hundred to three ninety-nine")],
  "per Gateway Load Balancer target group", "fixed", False, ["2.2.K8"], "reference", False, "HTTP or HTTPS health checks"),
]

cmds = []
for (fname, src, t, row, fid, kind, claim, q, vals, scope, dom, adj, bullets, rel, tier0, cond) in R:
    fact = {
        "id": fid, "service": "elb", "home_chapter": "14", "kind": kind,
        "claim": claim, "question": q,
        "values": [{"key": "v%d" % i, "display": d, "spoken": s} for i, (d, s) in enumerate(vals)],
        "qualifiers": {"scope": scope, "default_or_max": dom, "adjustable": adj, "condition": cond},
        "source_tier": 1, "hard": True, "tier0": tier0, "volatility": "stable",
        "changed": None, "change_items": [], "bullets": bullets,
        "exam_relevance": rel, "note": None,
    }
    path = os.path.join(HERE, fname + ".json")
    with open(path, "w") as f:
        json.dump(fact, f, indent=1)
    cmds.append("--source %s --table %d --row %d --file %s" % (src, t, row, path))
with open(os.path.join(HERE, "adopt2-cmds.txt"), "w") as f:
    f.write("\n".join(cmds) + "\n")
print(len(cmds))
