"""Builds brief.v0.json and mine-plan.json for chapter 08 (WAF, Shield, Firewall Manager, Network Firewall).

Run from the repo root after the fetch batches have finished:
    python3 aws-saa-book/_build/work/08-edge-protection/make-brief.py
Reads the corpus to count saved sources; anything not saved goes to fetch_failures. No network access.
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from saalib import corpus  # noqa: E402

WORK = ROOT / "_build/work/08-edge-protection"
REL = "aws-saa-book/_build/work/08-edge-protection"

book = json.load(open(ROOT / "data/book.json"))
chs = book["chapters"] if isinstance(book, dict) and "chapters" in book else book
entry = next(c for c in chs if c.get("id") == "08")
src = entry["sources"]

batch_urls = []
for i in range(1, 6):
    batch_urls += [u.strip() for u in open(WORK / f"urls-{i}.txt") if u.strip()]
universe = []
for key in ("pages", "faq", "history", "quotas", "pricing"):
    universe += src[key]
universe += batch_urls
seen, ordered = set(), []
for u in universe:
    if u not in seen:
        seen.add(u)
        ordered.append(u)

REFUSED = {
    "https://aws.amazon.com/about-aws/whats-new/2024/04/aws-firewall-manager-central-deployment-management-vpc-nacls/",
    "https://aws.amazon.com/about-aws/whats-new/2024/08/aws-waf-rate-based-rules-lower-rate-limits/",
}
fetched, failures = [], []
for u in ordered:
    sid = corpus.source_id_for(u)
    if corpus.load_meta(sid) is not None:
        fetched.append(sid)
    elif u in REFUSED:
        failures.append({"url": u, "source_id": sid,
                         "reason": "fetch refused by policy (exit 4, robots or allow-list); use the WAF / Firewall Manager doc-history row for the same change instead"})
    else:
        failures.append({"url": u, "source_id": sid,
                         "reason": "still queued on the shared rate limiter (about 5 s per request across agents) when the plan stage ended; "
                                   "the batch may finish it; else miners fetch on demand with saa.py fetch <url> (free if already cached)"})
fetched_set = set(fetched)

W = "docs/waf/latest/developerguide/"
N = "docs/network-firewall/latest/developerguide/"
DG = "docs/decision-guides/latest/decision-guides/"
WA = "docs/wellarchitected/latest/security-pillar/"
WP_DDOS = "docs/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-best-practices-ddos-resiliency"
WP_WAF = "docs/whitepapers/latest/guidelines-for-implementing-aws-waf/guidelines-for-implementing-aws-waf"
WN = "www/about-aws/whats-new/"
CS = "www/solutions/case-studies/"
FAQ = {"waf": "www/waf/faqs", "shield": "www/shield/faqs", "fms": "www/firewall-manager/faqs", "nfw": "www/network-firewall/faqs"}
PRICE = {"waf": "www/waf/pricing", "shield": "www/shield/pricing", "fms": "www/firewall-manager/pricing", "nfw": "www/network-firewall/pricing"}
QUOTA = {"waf": W + "limits", "shield": W + "shield-limits", "fms": W + "fms-limits", "nfw": N + "quotas"}
HIST = {"waf": W + "doc-history", "nfw": N + "document-history"}
SUNSET = "docs/general/latest/gr/sunset_services"
CH = {"waf": f"{REL}/changes-waf.txt", "shield": f"{REL}/changes-shield.txt",
      "fms": f"{REL}/changes-firewall-manager.txt", "nfw": f"{REL}/changes-network-firewall.txt"}

K3, K6, S3 = "1.2.K3", "1.2.K6", "1.2.S3"
NC, BD, FQ = "numbers+changes", "behavior+decisions", "faq"


def w(*p):
    return [W + x for x in p]


def n(*p):
    return [N + x for x in p]


# (bullet, lens, kind, service, question, sources, extra)
D = [
    # ---------- AWS WAF: what it is and what it protects
    (S3, BD, "fact", "waf", "What is AWS WAF in one sentence: a web application firewall that watches HTTP(S) requests to a protected resource and allows, blocks or counts them by rules?", w("what-is-aws-waf", "how-aws-waf-works") + [FAQ["waf"]], {}),
    (S3, BD, "fact", "waf", "Which resource types can a protection pack (web ACL) protect today: CloudFront distributions, Application Load Balancers, API Gateway REST APIs, AppSync GraphQL APIs, Cognito user pools, App Runner services, Verified Access instances, Amplify apps (list exactly what the page lists)?", w("how-aws-waf-works-resources") + [FAQ["waf"]], {}),
    (S3, BD, "fact", "waf", "Which resources can AWS WAF NOT be attached to that exam options offer (Network Load Balancer, EC2 instance directly, API Gateway HTTP API, Global Accelerator)? Ground each 'cannot' in a page sentence, or record it as unsupported and drop it.", w("how-aws-waf-works-resources") + [FAQ["waf"], FAQ["nfw"]], {"note": "HTTP API gap: see docs/apigateway/latest/developerguide/http-api-vs-rest (fetch on demand); FRESHNESS row says HTTP APIs still lack WAF."}),
    (S3, BD, "fact", "waf", "What is the scope difference between a global (CloudFront) protection pack and a Regional one, and in which Region must a CloudFront protection pack be created or managed (US East (N. Virginia))?", w("how-aws-waf-works-resources", "web-acl-associating-aws-resource", "cloudfront-features"), {}),
    (S3, NC, "fact", "waf", "How many protection packs (web ACLs) can one resource be associated with at a time, and can one web ACL protect many resources? What is the quota on ALB associations per web ACL (changed 2025-10-22 and 2026-05-01)?", w("web-acl-associating-aws-resource") + [QUOTA["waf"], HIST["waf"]], {}),
    (S3, BD, "fact", "waf", "Can AWS WAF protect a website that is not hosted in AWS (through a CloudFront distribution with a custom origin)?", [FAQ["waf"], W + "cloudfront-features"], {}),
    (S3, BD, "fact", "waf", "When an ALB sits behind CloudFront, where does the web ACL go, and how do you stop clients from bypassing CloudFront to reach the ALB directly?", w("cloudfront-features", "waf-tokens-with-alb-and-cf") + [WP_DDOS, WP_WAF], {"note": "waf-tokens-with-alb-and-cf not in the batch; fetch on demand."}),
    # ---------- WAF: rules, actions, evaluation
    (K6, BD, "fact", "waf", "How does a protection pack evaluate a request: rules in priority order, the first terminating action stops evaluation, and the default action (Allow or Block) applies when no rule matches?", w("web-acl-processing", "web-acl-processing-order", "web-acl-default-action", "web-acl-rule-actions"), {}),
    (K6, BD, "fact", "waf", "Which rule actions exist (Allow, Block, Count, CAPTCHA, Challenge), which are terminating, and what does Count do (match, label, keep evaluating) for safe testing of a new rule?", w("waf-rule-action", "web-acl-rule-actions", "web-acl-rule-group-override-options"), {}),
    (K6, BD, "fact", "waf", "Which rule statement detects SQL injection, and what does the sensitivity level option (added 2022-07) change?", w("waf-rule-statement-type-sqli-match") + [CH["waf"]], {}),
    (K6, BD, "fact", "waf", "Which rule statement detects cross-site scripting (XSS), and which request parts can it inspect?", w("waf-rule-statement-type-xss-match", "waf-rule-statements"), {}),
    (K6, BD, "fact", "waf", "What does a geographic match statement do (block or allow by country; Region-level granularity added 2022-11; adds labels), and how is it different from CloudFront geographic restrictions?", w("waf-rule-statement-type-geo-match", "cloudfront-features") + [FAQ["waf"]], {}),
    (K6, BD, "fact", "waf", "How do you block a list of IP addresses or CIDR ranges in AWS WAF (IP set match; IPv4 and IPv6 sets)?", w("waf-ip-set-managing", "waf-rule-statements") + [FAQ["waf"]], {}),
    (K6, NC, "fact", "waf", "What is the maximum number of IP addresses or ranges in one IP set, and how many IP sets per account per Region?", [QUOTA["waf"]], {}),
    (K6, BD, "fact", "waf", "What do the ASN match (2025-06), size constraint, string match and regex match statements inspect, in one line each?", w("waf-rule-statement-type-asn-match", "waf-rule-statement-type-size-constraint-match", "waf-rule-statements") + [CH["waf"]], {}),
    (K6, NC, "fact", "waf", "How much of a request body does AWS WAF inspect by default for each resource type (ALB and AppSync vs CloudFront, API Gateway, Cognito, App Runner, Verified Access), and what is the largest configurable limit (changed 2023-04-11 and 2024-03-07)?", w("web-acl-setting-body-inspection-limit") + [QUOTA["waf"], HIST["waf"]], {}),
    (K6, BD, "fact", "waf", "What does AWS WAF do with the part of a body (or headers, cookies) beyond the inspection limit (oversize handling: continue, match, no match)?", w("web-acl-setting-body-inspection-limit", "waf-oversize-request-components"), {"note": "waf-oversize-request-components fetch on demand."}),
    (K6, BD, "fact", "waf", "How does AWS WAF find the real client IP behind a proxy or CDN (forwarded IP configuration, X-Forwarded-For)?", w("waf-rule-statement-forwarded-ip-address"), {}),
    # ---------- WAF: rate-based rules
    (K6, BD, "fact", "waf", "What does a rate-based rule do: count requests per aggregation key over an evaluation window and apply its action to keys over the limit; which aggregation keys exist (source IP, forwarded IP, header, URI path, ASN, JA3/JA4, custom keys)?", w("waf-rule-statement-type-rate-based", "waf-rule-statement-type-rate-based-aggregation-options") + [FAQ["waf"]], {}),
    (K6, NC, "fact", "waf", "What is the lowest rate limit a rate-based rule accepts today, and what was it before 2024-08-30?", w("waf-rule-statement-type-rate-based-high-level-settings") + [WN + "2024/08/aws-waf-rate-based-rules-lower-rate-limits", HIST["waf"]], {"changed": True}),
    (K6, NC, "fact", "waf", "Which evaluation windows can a rate-based rule use (configurable since 2024-02-28), and what was the only window before?", w("waf-rule-statement-type-rate-based-high-level-settings") + [HIST["waf"], CH["waf"]], {"changed": True}),
    (K6, BD, "fact", "waf", "Rate-based rule caveats: is the count exact, and how quickly does WAF start and stop limiting a key?", w("waf-rule-statement-type-rate-based-caveats"), {}),
    (K6, BD, "fact", "waf", "How do you rate-limit only one part of a site, such as the login page (scope-down statement), and can you exempt trusted IP ranges?", w("waf-rule-statement-type-rate-based", "waf-rate-based-example-limit-login-page") + [FAQ["waf"]], {"note": "example page fetch on demand."}),
    (K6, BD, "fact", "waf", "Why does a rate-based rule stop a distributed attack from many IP addresses better than a static IP block list (Callvale: 60,000 attempts from 1,400 addresses)?", w("waf-rule-statement-type-rate-based") + [FAQ["waf"], WP_WAF, WP_DDOS], {"callvale": True}),
    # ---------- WAF: capacity, managed rules, intelligent threat mitigation
    (S3, NC, "fact", "waf", "What are web ACL capacity units (WCUs), what is the maximum WCU per protection pack and per rule group, and above how many WCUs is extra cost charged (changed 2023-04-11)?", w("aws-waf-capacity-units") + [QUOTA["waf"], PRICE["waf"], HIST["waf"]], {"changed": True}),
    (S3, NC, "fact", "waf", "Other AWS WAF quotas the exam can touch: web ACLs per account per Region, rule groups, regex pattern sets, rules per rule group, geo match countries per rule (quota added 2025-08-29).", [QUOTA["waf"]], {}),
    (S3, BD, "fact", "waf", "What are managed rule groups: AWS Managed Rules (free for most) vs AWS Marketplace seller rule groups (subscription)? Which AWS Managed Rules groups need an extra fee?", w("waf-managed-rule-groups", "aws-managed-rule-groups", "marketplace-rule-groups") + [FAQ["waf"], PRICE["waf"]], {}),
    (K6, BD, "fact", "waf", "What do the baseline AWS Managed Rules groups cover (core rule set and OWASP-style risks, known bad inputs, admin protection), and the use-case groups (SQL database, Linux, PHP, WordPress)?", w("aws-managed-rule-groups-baseline", "aws-managed-rule-groups-use-case"), {}),
    (K6, BD, "fact", "waf", "What do the Amazon IP reputation list and the Anonymous IP list rule groups block?", w("aws-managed-rule-groups-ip-rep"), {}),
    (S3, BD, "fact", "waf", "What is AWS WAF Bot Control (common vs targeted inspection levels), and is it charged on top of the protection pack?", w("waf-bot-control", "waf-managed-protections") + [PRICE["waf"], FAQ["waf"]], {}),
    (S3, BD, "fact", "waf", "What does Fraud Control account takeover prevention (ATP) protect (login page, stolen credentials, credential stuffing), and how is it different from Bot Control and from account creation fraud prevention (ACFP)?", w("waf-atp", "waf-acfp") + [FAQ["waf"]], {"callvale": True}),
    (K6, BD, "fact", "waf", "What do the CAPTCHA and Challenge actions do, how do tokens work, and when is each the right action?", w("waf-captcha-and-challenge", "waf-tokens") + [FAQ["waf"]], {"note": "waf-tokens fetch on demand."}),
    (K6, BD, "fact", "waf", "What is the AWS WAF Anti-DDoS managed rule group / application layer (L7) DDoS protection (2025-06), and what is resource-level DDoS protection for ALB?", w("waf-anti-ddos", "waf-anti-ddos-alb") + [FAQ["waf"], WN + "2025/06/aws-waf-automatic-application-layer-ddos-protection", WN + "2025/06/aws-waf-general-availability-resource-level-ddos-protection-alb"], {"changed": True}),
    (S3, BD, "fact", "waf", "Can a blocked request get a custom response (status code, body, headers), and can WAF insert custom headers into allowed requests?", w("customizing-the-response-for-blocked-requests") + [FAQ["waf"]], {}),
    # ---------- WAF: logging, pricing, changes
    (S3, BD, "fact", "waf", "Where can AWS WAF send full request logs (CloudWatch Logs, Amazon S3, Amazon Data Firehose), and how many destinations per protection pack?", w("logging", "logging-destinations"), {}),
    (S3, NC, "fact", "waf", "AWS WAF pricing dimensions: per protection pack per month, per rule per month, per million requests, extra for Bot Control / Fraud Control / CAPTCHA, extra WCU above the included amount.", [PRICE["waf"], FAQ["waf"]], {}),
    (S3, NC, "change", "waf", "Hypothesis (FRESHNESS): AWS WAF Classic reached end of support on 2026-10-07; confirm date and the migration path to current AWS WAF.", [SUNSET, W + "waf-migrating-from-classic", HIST["waf"]], {"changed": True}),
    (S3, NC, "change", "waf", "Hypothesis: CloudFront flat-rate pricing plans (2025-11-18) bundle AWS WAF and DDoS protection with a distribution; what exactly is included?", [WN + "2025/11/aws-flat-rate-pricing-plans", HIST["waf"]], {"changed": True}),
    (S3, NC, "change", "waf", "Hypothesis: AWS WAF added free vended logs based on request volume (2025-09-08); what is free and up to what amount?", [WN + "2025/09/aws-waf-free-vended-logs-request-volume", PRICE["waf"]], {"changed": True}),
    (S3, NC, "change", "waf", "Hypothesis: the AWS WAF console renamed web ACLs to 'protection packs' (new console 2025-06-17). Which name do the docs use now, and how do we say it once ('protection pack (web ACL)')?", w("web-acl", "working-with-console") + [HIST["waf"]], {"changed": True}),
    (S3, NC, "change", "waf", "Other WAF changes since mid-2022 worth a 'Changed recently' line: Challenge action and targeted Bot Control (2022-10-27), ATP (2022-08-24), JA3/JA4 matching, URI fragment, header order; which matter for SAA?", [HIST["waf"], CH["waf"]], {"changed": True}),
    (S3, BD, "fact", "waf", "How long does AWS WAF take to propagate a rule change, and how do you see if rules work (CloudWatch metrics, sampled requests, logs)?", [FAQ["waf"]] + w("web-acl-working-with", "logging"), {}),
    (S3, BD, "fact", "waf", "Can AWS WAF inspect HTTPS traffic (it sees the request after the protected service terminates TLS)?", [FAQ["waf"]], {}),
    # ---------- Shield
    (K6, BD, "fact", "shield", "What is AWS Shield Standard: automatic, no extra charge, for every AWS customer; which attack types and layers does it protect against (network and transport layer, for example SYN floods and UDP reflection)?", w("ddos-standard-summary", "ddos-overview") + [FAQ["shield"]], {}),
    (K6, BD, "fact", "shield", "What does AWS Shield Advanced add over Standard: enhanced detection, Shield Response Team, DDoS cost protection, automatic application layer mitigation, health-based detection, visibility and reports?", w("ddos-advanced-summary", "ddos-advanced-summary-capabilities") + [FAQ["shield"]], {}),
    (K6, BD, "fact", "shield", "Which resource types can Shield Advanced protect (CloudFront, Route 53 hosted zones, Global Accelerator, ALB, Elastic IP addresses for EC2 and NLB)?", w("ddos-advanced-summary-protected-resources", "ddos-protections-by-resource-type") + [FAQ["shield"]], {}),
    (K6, NC, "fact", "shield", "What does Shield Advanced cost (monthly subscription fee, commitment term, data transfer out usage fees), and does one fee cover all accounts in an organization?", [PRICE["shield"], FAQ["shield"], W + "ddos-advanced-summary-deciding"], {"callvale": True}),
    (K6, BD, "fact", "shield", "Does Shield Advanced include AWS WAF (and Firewall Manager) usage for protected resources at no extra cost?", [PRICE["shield"], FAQ["shield"]], {}),
    (K6, BD, "fact", "shield", "What is DDoS cost protection: credits for scaling charges caused by a DDoS attack on protected resources; how is a credit requested?", w("ddos-request-service-credit") + [FAQ["shield"]], {}),
    (K6, BD, "fact", "shield", "Who can contact the Shield Response Team (SRT), which AWS Support plan is required, and what can the SRT do in your account?", w("ddos-srt-support") + [FAQ["shield"]], {}),
    (K6, BD, "fact", "shield", "What is proactive engagement, and what must be configured for it (Route 53 health checks on protected resources, contacts)?", w("ddos-srt-proactive-engagement", "ddos-advanced-health-checks"), {}),
    (K6, BD, "fact", "shield", "How does Shield Advanced automatic application layer DDoS mitigation work: it needs a web ACL on the resource and manages rules in a Shield rule group (Count or Block)?", w("ddos-automatic-app-layer-response") + [FAQ["shield"]], {}),
    (K6, BD, "fact", "shield", "What are Shield Advanced protection groups, and what does health-based detection add?", w("ddos-protection-groups", "ddos-advanced-health-checks"), {}),
    (K6, NC, "fact", "shield", "Shield Advanced quotas that the exam can touch (protections, protection groups).", [QUOTA["shield"]], {}),
    (K6, BD, "fact", "shield", "What are the common DDoS attack types by layer (UDP reflection, SYN flood at layers 3 and 4; HTTP floods, cache-busting at layer 7)?", w("types-of-ddos-attacks") + [WP_DDOS], {}),
    (K6, BD, "decision", "shield", "What does a DDoS-resilient architecture look like (CloudFront and Route 53 at the edge, Global Accelerator, ELB, Auto Scaling, reduce the attack surface, security groups and NACLs)?", w("ddos-resiliency") + [WP_DDOS, WA + "protecting-networks"], {}),
    (K6, BD, "fact", "shield", "Can AWS Shield protect resources that run outside AWS (on premises), and how (CloudFront or Global Accelerator in front)?", [FAQ["shield"]], {}),
    (K6, NC, "fact", "shield", "How quickly does Shield detect and mitigate events, and how fast is an event notification?", [FAQ["shield"]] + w("ddos-event-detection"), {"note": "ddos-event-detection fetch on demand."}),
    (K6, BD, "fact", "shield", "How do AWS WAF L7 DDoS protection (Anti-DDoS managed rule group) and Shield Advanced relate: can the WAF feature be bought without Shield Advanced, and do Shield Advanced customers pay extra?", [FAQ["waf"], FAQ["shield"]], {}),
    (K6, NC, "change", "shield", "Hypothesis: AWS Shield network security director (preview 2025-06-17) became 'AWS Network Security Manager', GA 2026-09-24 in us-east-1. Label it not examinable yet; what does it do in one line?", w("nsd-chapter") + [FAQ["shield"], CH["shield"]], {"changed": True, "examinable": "no (GA after 2026-07-15)"}),
    (K6, BD, "decision", "shield", "When is Shield Advanced worth buying, according to AWS (ddos-advanced-summary-deciding), and why did Callvale decide not to buy it at stage 3?", w("ddos-advanced-summary-deciding") + [PRICE["shield"], DG + "waf-or-shield"], {"callvale": True}),
    # ---------- Firewall Manager
    (S3, BD, "fact", "firewall-manager", "What is AWS Firewall Manager: central configuration and management of firewall rules across the accounts and applications of an organization?", w("fms-chapter") + [FAQ["fms"]], {}),
    (S3, BD, "fact", "firewall-manager", "What are the prerequisites of Firewall Manager (AWS Organizations with all features, a Firewall Manager administrator account, AWS Config enabled, AWS RAM for Network Firewall and DNS Firewall policies)?", w("fms-prereq", "enable-integration", "enable-config", "enable-ram") + [FAQ["fms"]], {}),
    (S3, BD, "fact", "firewall-manager", "Which policy types does Firewall Manager manage (AWS WAF, Shield Advanced, security groups: common, content audit, usage audit; network ACLs; Network Firewall; Route 53 Resolver DNS Firewall; third-party firewalls)?", w("working-with-policies", "getting-started-fms-intro") + [FAQ["fms"]], {}),
    (S3, BD, "fact", "firewall-manager", "Does Firewall Manager apply a policy automatically to new accounts and new resources in scope, and can you run a policy without automatic remediation (audit only)?", w("policy-scope", "working-with-policies") + [FAQ["fms"]], {}),
    (S3, BD, "fact", "firewall-manager", "How is policy scope set (include or exclude accounts and OUs, resource types, resource tags)?", w("policy-scope") + [FAQ["fms"]], {}),
    (S3, BD, "fact", "firewall-manager", "Is a Firewall Manager policy Regional? How do you cover several Regions, and how is a CloudFront (global) WAF policy handled?", [FAQ["fms"]] + w("create-policy", "waf-policies"), {"note": "create-policy fetch on demand."}),
    (S3, BD, "fact", "firewall-manager", "How does a Firewall Manager AWS WAF policy manage web ACLs in member accounts (first and last rule groups set centrally, account owners add rules in between; can retrofit existing web ACLs since 2024-10)?", w("waf-policies") + [CH["fms"], HIST["waf"]], {"changed": True}),
    (S3, NC, "fact", "firewall-manager", "What does Firewall Manager cost (per policy per Region per month, plus AWS Config and protected-service charges), and is it included with Shield Advanced?", [PRICE["fms"], FAQ["fms"], PRICE["shield"]], {}),
    (S3, NC, "fact", "firewall-manager", "Firewall Manager quotas (policies per organization per Region, accounts in scope, administrators).", [QUOTA["fms"], FAQ["fms"]], {}),
    (S3, BD, "fact", "firewall-manager", "Can there be more than one Firewall Manager administrator account (multiple administrators since 2023-04), and what can each administer?", w("fms-administrators") + [CH["fms"]], {"changed": True}),
    (S3, BD, "fact", "firewall-manager", "How do you see compliance of a policy, and where do findings go (AWS Security Hub)?", w("fms-compliance", "fms-findings") + [FAQ["fms"]], {"note": "fms-findings fetch on demand."}),
    (K3, BD, "fact", "firewall-manager", "What do Firewall Manager security group policies do (common: apply a security group to accounts; content audit: check rules; usage audit: remove unused or redundant groups)?", w("security-group-policies") + [FAQ["fms"]], {}),
    (K3, NC, "change", "firewall-manager", "Hypothesis: Firewall Manager added network ACL policies on 2024-04-25/29. Confirm and state what they enforce.", w("network-acl-policies") + [HIST["waf"], WN + "2024/04/aws-firewall-manager-central-deployment-management-vpc-nacls"], {"changed": True}),
    (S3, BD, "fact", "firewall-manager", "What does a Firewall Manager Shield Advanced policy do (adds protection to in-scope resources in every account; can enable automatic application layer mitigation)?", w("shield-policies") + [FAQ["shield"]], {}),
    (K3, BD, "fact", "firewall-manager", "What does a Firewall Manager Network Firewall policy create in member VPCs (firewall subnets, endpoints, route tables), and what does a DNS Firewall policy do?", w("network-firewall-policies", "dns-firewall-policies", "resource-sharing"), {}),
    # ---------- Network Firewall
    (K3, BD, "fact", "network-firewall", "What is AWS Network Firewall: a stateful, managed network firewall and intrusion detection and prevention service for VPCs?", n("what-is-aws-network-firewall") + [FAQ["nfw"]], {}),
    (K3, BD, "fact", "network-firewall", "Which traffic can Network Firewall filter (to and from an internet gateway, NAT gateway, VPN, Direct Connect, between VPCs through Transit Gateway)?", n("what-is-aws-network-firewall", "how-it-works") + [FAQ["nfw"]], {}),
    (K3, BD, "fact", "network-firewall", "How is it deployed: a firewall endpoint in a dedicated firewall subnet in each Availability Zone, and VPC route tables send traffic to the endpoint?", n("firewall-components", "vpc-config-subnets", "route-tables", "firewall-high-level-steps"), {}),
    (K3, BD, "fact", "network-firewall", "Why must traffic of one Availability Zone use the firewall endpoint of the same AZ in both directions (asymmetric routing breaks stateful inspection)?", n("asymmetric-routing", "route-tables", "arch-two-zone-igw"), {}),
    (K3, BD, "fact", "network-firewall", "Where does the firewall sit in the internet gateway plus NAT gateway pattern (route from the NAT gateway subnet to the firewall endpoint, then to the IGW)?", n("arch-igw-ngw", "route-tables"), {}),
    (K3, BD, "fact", "network-firewall", "What are the stateless and stateful rules engines, and in which order does a packet meet them (stateless first; pass, drop or forward to stateful)?", n("firewall-rules-engines", "firewall-policy-processing", "rule-action"), {}),
    (K3, BD, "fact", "network-firewall", "Stateful rules: which formats are supported (Suricata-compatible rule strings, 5-tuple standard rules, domain lists), and what are the stateful actions (pass, drop, reject, alert)?", n("rule-groups", "stateful-rule-groups-suricata", "rule-action") + [FAQ["nfw"]], {}),
    (K3, BD, "fact", "network-firewall", "How does a domain list rule group allow only approved outside domains (HTTP Host header and TLS SNI inspection; allowlist or denylist), and does it need TLS decryption?", n("stateful-rule-groups-domain-names") + [FAQ["nfw"]], {"callvale": True}),
    (K3, BD, "fact", "network-firewall", "Strict rule order versus action order for stateful rules, and which default actions exist under strict order (drop established, drop all, alert)?", n("firewall-policy-settings", "suricata-rule-evaluation-order"), {"note": "suricata-rule-evaluation-order fetch on demand."}),
    (K3, BD, "fact", "network-firewall", "What does TLS inspection do (decrypt, inspect, re-encrypt; inbound and outbound), and which certificates does it need (ACM)?", n("tls-inspection-configurations", "tls-inspection-considerations") + [FAQ["nfw"]], {}),
    (K3, BD, "fact", "network-firewall", "Geographic IP filtering (2024-08) and URL / domain category filtering (2026-01): what can each rule match?", n("rule-groups-geo-ip-filtering", "rule-groups-url-filtering") + [CH["nfw"]], {"changed": True}),
    (K3, BD, "fact", "network-firewall", "Which AWS managed rule groups exist for Network Firewall (domain and IP lists, threat signatures, active threat defense), and is active threat defense on by default now (2025-11)?", n("nwfw-managed-rule-groups", "aws-managed-rule-groups-atd", "aws-managed-rule-groups-domain-list") + [FAQ["nfw"], WN + "2025/11/active-threat-defense-default-network-firewall"], {"changed": True}),
    (K3, NC, "fact", "network-firewall", "What throughput does one firewall endpoint support, and how does it scale?", [QUOTA["nfw"], FAQ["nfw"]] + n("disaster-recovery-resiliency"), {}),
    (K3, NC, "fact", "network-firewall", "Network Firewall quotas: firewalls per account per Region, firewall policies, rule groups, stateful rules per policy (adjustable since 2024-05), domains per domain list, IP set references, VPC endpoint associations.", [QUOTA["nfw"], HIST["nfw"]], {}),
    (K3, NC, "change", "network-firewall", "Hypothesis: Network Firewall can attach directly to a transit gateway (native attachment, 2025-06-16) instead of an inspection VPC. Confirm, and say what changes for centralized inspection answers.", n("tgw-firewall", "tgw-firewall-considerations") + [WN + "2025/06/aws-network-firewall-transit-gateway-native-integration", HIST["nfw"]], {"changed": True}),
    (K3, NC, "change", "network-firewall", "Hypothesis: one firewall can serve other VPCs through VPC endpoint associations (2025-05-28). Confirm and state the limit.", n("firewall-owners-and-vpc-endpoint-association-owners", "firewalls") + [QUOTA["nfw"], HIST["nfw"]], {"changed": True}),
    (K3, BD, "fact", "network-firewall", "Which logs does Network Firewall produce (alert, flow, TLS) and where can it send them (Amazon S3, CloudWatch Logs, Amazon Data Firehose)?", n("firewall-logging", "firewall-logging-destinations"), {}),
    (K3, NC, "fact", "network-firewall", "Network Firewall pricing dimensions: per firewall endpoint hour, per GB processed, extra for TLS inspection and advanced features; NAT gateway charges offset; price reductions 2026-02.", [PRICE["nfw"], FAQ["nfw"], WN + "2026/02/aws-network-firewall-new-price-reduction"], {}),
    (K3, BD, "fact", "network-firewall", "Does Network Firewall protect against DDoS attacks (FAQ answer), and which service does?", [FAQ["nfw"]], {}),
    (K3, BD, "decision", "network-firewall", "Network Firewall versus Gateway Load Balancer with third-party appliances: when is each the answer?", [FAQ["nfw"]] + n("what-is-aws-network-firewall"), {}),
    (K3, BD, "fact", "network-firewall", "How is Network Firewall managed across many accounts (share firewall policies and rule groups with AWS RAM; central policies through Firewall Manager)?", n("sharing") + [FAQ["nfw"]] + w("network-firewall-policies"), {}),
    (K3, BD, "fact", "network-firewall", "Is a firewall endpoint zonal, and what is the resilience advice (one endpoint per AZ in use)?", n("disaster-recovery-resiliency", "firewall-and-firewall-endpoints-considerations"), {}),
    (K3, NC, "change", "network-firewall", "Hypothesis: Network Firewall proxy / no-source-preservation mode (preview 2025-11-25; docs 2026-08-03). Label not examinable yet; one line on what it does.", n("nfw-no-source-preservation", "nfw-nosource-client-config") + [FAQ["nfw"], CH["nfw"]], {"changed": True, "examinable": "no (preview or GA after 2026-07-15)"}),
    (K3, NC, "change", "network-firewall", "Other Network Firewall changes since mid-2022 worth one line: reject action (2023-01), IPv6 support (2023-01), ingress and egress TLS inspection (2023-03, 2023-12), PrivateLink interface endpoints (2024-09).", [HIST["nfw"], CH["nfw"]], {"changed": True}),
    # ---------- Comparisons and layers
    (K6, BD, "decision", "all", "One line each: AWS WAF vs Shield Standard vs Shield Advanced vs Network Firewall vs Firewall Manager (layer 7 rules vs DDoS vs VPC traffic inspection vs central policy). Use the decision guides' own words.", [DG + "waf-or-shield", DG + "choosing-aws-security-services", FAQ["nfw"], FAQ["fms"]], {}),
    (S3, BD, "decision", "all", "What does the 'AWS WAF or AWS Shield?' decision guide say about when to use each and when to combine them?", [DG + "waf-or-shield"], {}),
    (K3, BD, "decision", "all", "Where does each control act: AWS WAF on HTTP requests to a resource, Network Firewall on VPC traffic, security groups on ENIs (stateful, allow only), network ACLs on subnets (stateless, allow and deny), Route 53 Resolver DNS Firewall on DNS queries?", [DG + "choosing-aws-security-services", DG + "choosing-networking-and-content-delivery-service", WA + "sec_network_protection_create_layers", WA + "sec_network_protection_layered", FAQ["nfw"]], {"reuse_facts": ["vpc-sg-allow-rules-only", "vpc-def-network-acl", "vpc-network-firewall-stateful-managed"]}),
    (K6, BD, "decision", "all", "To block an IP range: network ACL deny rule vs AWS WAF IP set vs security group (cannot deny). Why is a NACL a poor fit for 1,400 addresses (rules per NACL quota)?", [W + "waf-ip-set-managing", QUOTA["waf"], "docs/vpc/latest/userguide/amazon-vpc-limits"], {"callvale": True, "reuse_facts": ["vpc-quota-rules-per-network-acl", "vpc-sg-allow-rules-only", "vpc-nacl-deny-rule-lower-number"]}),
    (K3, BD, "decision", "all", "What do the Well-Architected security pillar best practices say about network layers and inspection at each layer (SEC05: create network layers, control traffic at all layers, implement inspection)?", [WA + "protecting-networks", WA + "sec_network_protection_create_layers", WA + "sec_network_protection_layered"], {}),
    (S3, BD, "decision", "all", "What do the AWS WAF implementation guidelines whitepaper recommend for rollout (start in Count, managed rules first, rate-based rules, logging)? Note: registry snapshot of the whitepaper URL may be empty; prefer Developer Guide pages.", [WP_WAF, W + "web-acl-testing"], {"note": "orchestrator: the whitepaper snapshot is empty; cite WAF Developer Guide pages."}),
    (K6, BD, "decision", "all", "Reference web-application pattern: CloudFront + AWS WAF + Shield Advanced + Route 53 in front of an ALB; which piece stops which threat?", w("ddos-resiliency", "ddos-resiliency-example-web") + [WP_DDOS], {"note": "ddos-resiliency-example-web fetch on demand."}),
    (S3, BD, "decision", "all", "GuardDuty (detects threats) vs AWS WAF (blocks web requests) vs Network Firewall (filters VPC traffic): the 'detect vs block' signal in stems (detail in chapter 09).", [DG + "choosing-aws-security-services"], {}),
    # ---------- Callvale decision record
    (S3, BD, "decision", "all", "Callvale decision facts: AWS WAF on CloudFront and the ALB, deployed through Firewall Manager so that every account (and new accounts) gets the same web ACL rules.", w("waf-policies", "policy-scope", "fms-chapter") + [FAQ["fms"]], {"callvale": True}),
    (K3, BD, "decision", "network-firewall", "Callvale decision facts: production workloads may connect only to approved outside domains: Network Firewall domain allowlist on outbound traffic, endpoint per AZ, NAT gateway path.", n("stateful-rule-groups-domain-names", "arch-igw-ngw") + [FAQ["nfw"]], {"callvale": True}),
    (K6, BD, "decision", "shield", "Callvale accepts 'no paid DDoS support' and 'rate limits need tuning': which facts state what Shield Standard already gives for free and why rate limits need testing in Count mode first?", w("ddos-standard-summary", "waf-rule-statement-type-rate-based-caveats", "waf-rule-action") + [FAQ["shield"]], {"callvale": True}),
    # ---------- Real companies
    (S3, BD, "case", "all", "Real example: ENGIE secures 51 business entities with AWS WAF and Firewall Manager (one sentence, quoted).", [CS + "engie-security-waf-firewall-manager"], {}),
    (K6, BD, "case", "all", "Real example: OLX (AWS WAF Bot Control) or Moovit (AWS WAF against bots and DDoS) - one quoted outcome.", [CS + "olx-waf-case-study", CS + "moovit-case-study"], {}),
    (K3, BD, "case", "all", "Real example: Rapid7 with AWS Network Firewall, or OutSystems with Shield Advanced - one quoted outcome.", [CS + "rapid7-network-firewall-case-study", CS + "outsystems-case-study"], {}),
    # ---------- FAQ quick-fire (verbatim FAQ answers)
    (S3, FQ, "faq", "waf", "FAQ quick-fire: 'Can I use AWS WAF to protect web sites not hosted in AWS?'", [FAQ["waf"]], {"faq_id": "waf#4"}),
    (K6, FQ, "faq", "waf", "FAQ quick-fire: 'How does a Rate-based rule compare to a regular AWS WAF Rule?'", [FAQ["waf"]], {"faq_id": "waf#17"}),
    (K6, FQ, "faq", "waf", "FAQ quick-fire: 'Can I use Rate-based rule to mitigate Web layer DDoS attacks?'", [FAQ["waf"]], {"faq_id": "waf#21"}),
    (K6, FQ, "faq", "waf", "FAQ quick-fire: 'Can I exempt certain high-traffic source IP ranges from being blocked by my Rate-based Rule(s)?'", [FAQ["waf"]], {"faq_id": "waf#24"}),
    (S3, FQ, "faq", "waf", "FAQ quick-fire: 'How long does it take AWS WAF to propagate my rules?'", [FAQ["waf"]], {"faq_id": "waf#39"}),
    (S3, FQ, "faq", "waf", "FAQ quick-fire: 'Can AWS WAF inspect HTTPS traffic?'", [FAQ["waf"]], {"faq_id": "waf#43"}),
    (K6, FQ, "faq", "waf", "FAQ quick-fire: 'Can AWS WAF application layer (L7) DDoS protection be purchased standalone, or does it require an AWS Shield Advanced subscription?'", [FAQ["waf"]], {"faq_id": "waf#69"}),
    (S3, FQ, "faq", "waf", "FAQ quick-fire: 'Does AWS WAF support IPv6?' and 'What services does AWS WAF support?'", [FAQ["waf"]], {"faq_id": "waf#8,waf#12"}),
    (K6, FQ, "faq", "shield", "FAQ quick-fire: 'Can I use AWS Shield to protect web sites not hosted in AWS?'", [FAQ["shield"]], {"faq_id": "shield#18"}),
    (K6, FQ, "faq", "shield", "FAQ quick-fire: 'Do I need a special support plan to contact the AWS Shield Response Team?'", [FAQ["shield"]], {"faq_id": "shield#33"}),
    (K6, FQ, "faq", "shield", "FAQ quick-fire: 'Can I choose to only protect some of my resources with AWS Shield Advanced?'", [FAQ["shield"]], {"faq_id": "shield#53"}),
    (K6, FQ, "faq", "shield", "FAQ quick-fire: 'How can I enable AWS Shield Advanced across multiple AWS Accounts?'", [FAQ["shield"]], {"faq_id": "shield#54"}),
    (K6, FQ, "faq", "shield", "FAQ quick-fire: 'How am I charged for AWS Shield Standard?' and 'How many resources can I enable for AWS Shield Standard protection?'", [FAQ["shield"]], {"faq_id": "shield#51,shield#26"}),
    (S3, FQ, "faq", "firewall-manager", "FAQ quick-fire: 'Can I create a Firewall Manager policy but not remediate automatically?'", [FAQ["fms"]], {"faq_id": "firewall-manager#9"}),
    (S3, FQ, "faq", "firewall-manager", "FAQ quick-fire: 'Can I create security policies across regions?'", [FAQ["fms"]], {"faq_id": "firewall-manager#12"}),
    (S3, FQ, "faq", "firewall-manager", "FAQ quick-fire: 'Which AWS resources can AWS Firewall Manager configure rules on?'", [FAQ["fms"]], {"faq_id": "firewall-manager#4"}),
    (K3, FQ, "faq", "network-firewall", "FAQ quick-fire: 'Can I use AWS Network Firewall for protection against DDoS attacks?'", [FAQ["nfw"]], {"faq_id": "network-firewall#5"}),
    (K3, FQ, "faq", "network-firewall", "FAQ quick-fire: 'Can I use AWS Network Firewall with my Transit Gateway (TGW)?'", [FAQ["nfw"]], {"faq_id": "network-firewall#19"}),
    (K3, FQ, "faq", "network-firewall", "FAQ quick-fire: 'Can I use AWS Network Firewall with AWS Gateway Load Balancer (GWLB)?'", [FAQ["nfw"]], {"faq_id": "network-firewall#20"}),
    (K3, FQ, "faq", "network-firewall", "FAQ quick-fire: 'Can AWS Network Firewall inspect encrypted traffic?' and 'Which TLS versions does AWS Network Firewall support?'", [FAQ["nfw"]], {"faq_id": "network-firewall#25,network-firewall#29"}),
    (K3, FQ, "faq", "network-firewall", "FAQ quick-fire: 'Which types of outbound traffic control does AWS Network Firewall support?'", [FAQ["nfw"]], {"faq_id": "network-firewall#22"}),
    (K3, FQ, "faq", "network-firewall", "FAQ quick-fire: 'How is AWS Network Firewall different from other firewall offerings on AWS and the AWS Marketplace?'", [FAQ["nfw"]], {"faq_id": "network-firewall#6"}),
]

demand = []
for i, (bullet, lens, kind, service, q, sources, extra) in enumerate(D, 1):
    item = {"id": f"d{i:03d}", "bullet": bullet, "question": q, "status": "open", "facts": [],
            "lens": lens, "kind": kind, "service": service, "sources": sources}
    for k, v in extra.items():
        item[k] = v
    missing = [s for s in sources if not s.startswith("aws-saa-book/") and s not in fetched_set]
    if missing:
        item["sources_not_saved"] = missing
    demand.append(item)

brief = {
    "chapter": "08",
    "slug": "edge-protection",
    "title": entry["title"],
    "template": entry.get("tier"),
    "services": entry["services"],
    "sources_fetched": len(fetched),
    "fetch_failures": failures,
    "demand": demand,
    "feeds": {
        "faq": [f"aws-saa-book/_build/corpus/faq/{x}.jsonl" for x in ("waf", "shield", "firewall-manager", "network-firewall")],
        "changes": list(CH.values()),
        "cases": [f"{REL}/cases-{x}.txt" for x in ("waf", "shield", "firewall-mgr", "network-firewall")],
    },
    "notes": [
        "Security block chapter: the reader's weakest domain. Completeness of can / cannot facts, comparisons with neighbours (security groups, network ACLs, GuardDuty, Gateway Load Balancer, DNS Firewall) and changes since mid-2022 matter most.",
        "Cite AWS WAF Developer Guide pages, not the WAF implementation whitepaper (its registry snapshot is empty).",
        "Displays of number-free facts: a verbatim phrase of at most 8 words from a quote.",
        "Shield and Firewall Manager are documented inside the WAF Developer Guide (one guide, one history page).",
        "Neighbour facts already verified in chapter 10 (vpc-*) can be linked, not re-mined: see reuse_facts on d-items.",
        "Not examinable yet (GA after 2026-07-15 or preview): AWS Network Security Manager (formerly Shield network security director), Network Firewall proxy mode.",
        "Research input (FREQUENCY, FRESHNESS) gave the questions only; every answer must come from a saved page.",
        "Case pages: the ENGIE and OutSystems snapshots carry the generic title 'Customer Success Stories...' (likely redirected to the index); check final_url before quoting and prefer OLX, Moovit or Rapid7.",
        "Plan stage ended before the shared-rate-limit queue drained: unsaved pages are listed in fetch_failures and per item in sources_not_saved; fetch them at mine start (cached pages cost nothing).",
    ],
}
json.dump(brief, open(WORK / "brief.v0.json", "w"), indent=1, ensure_ascii=False)

lenses = [NC, BD, FQ]
pages = {l: [] for l in lenses}
dem = {l: [] for l in lenses}
for d in demand:
    dem[d["lens"]].append(d["id"])
    for s in d["sources"]:
        if not s.startswith("aws-saa-book/") and s not in pages[d["lens"]]:
            pages[d["lens"]].append(s)
mine = {
    "chapter": "08",
    "lenses": lenses,
    "about": {
        NC: "Every limit, default, size, count, price dimension and dated change: WAF quotas (IP sets, WCUs, web ACLs, associations), body inspection limits, rate-based rule minimum and windows, Shield Advanced fee and term, Firewall Manager and Network Firewall quotas and pricing, endpoint throughput. Quote table rows with their header (saa.py tables). Change items: confirm each hypothesis against the doc-history page or the What's New page and record old value, new value and date; label anything GA after 2026-07-15 'not examinable yet'.",
        BD: "Can / cannot / only / by default claims and comparisons: what each service protects, where it sits, rule evaluation, actions, managed rule groups, Shield Standard vs Advanced, Firewall Manager prerequisites, policy types and scope, Network Firewall deployment, engines, domain filtering, TLS inspection, plus the neighbour comparisons and the facts behind Callvale's decision and the case studies. Displays of number-free facts are verbatim phrases of at most 8 words.",
        FQ: "Quick-fire items with verbatim FAQ answers: saa.py faq <url> --find TEXT on the four FAQ pages (parsed stores under _build/corpus/faq/). One fact per FAQ answer that a stem could turn on; skip marketing lines.",
    },
    "pages": pages,
    "demand": dem,
    "feeds": brief["feeds"],
    "guides": {
        "waf-developerguide": "536 pages (WAF, Shield, Firewall Manager), index built 2026-10-05; history doc-history; quotas limits, shield-limits, fms-limits",
        "network-firewall-developerguide": "152 pages, index built 2026-10-05; history document-history; quotas quotas",
    },
    "fetch_failures": failures,
}
json.dump(mine, open(WORK / "mine-plan.json", "w"), indent=1, ensure_ascii=False)
print(f"sources_fetched={len(fetched)} failures={len(failures)} demand={len(demand)} "
      + " ".join(f"{l}={len(dem[l])}" for l in lenses))
not_saved = sorted({s for d in demand for s in d.get("sources_not_saved", [])})
print("demand sources not saved:", len(not_saved))
for s in not_saved:
    print("  ", s)
