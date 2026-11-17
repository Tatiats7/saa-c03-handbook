"""register-26: build amend patch files from reg-decisions.json (writes only under _build/work/26-rds/reg-patches)."""
import json, re, sys, copy, os

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
sys.path.insert(0, ROOT + "/tools")
from saalib.common import normalize_text  # noqa: E402

W = ROOT + "/_build/work/26-rds/"
OUT = W + "reg-patches/"
os.makedirs(OUT, exist_ok=True)

facts = {}
for p in [ROOT + "/data/facts/rds.jsonl", ROOT + "/data/facts/rds-proxy.jsonl"]:
    for line in open(p):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f

D = json.load(open(W + "reg-decisions.json"))
problems = []
gone = {o for o, n, _ in D["supersede"]} | {r[0] for r in D["reject"]}
patch = {}


def P(i):
    if i not in facts:
        problems.append("unknown " + i)
        return None
    if i in gone:
        problems.append("edit on retired fact " + i)
    return patch.setdefault(i, {})


def cur(i, k):
    return copy.deepcopy(patch.get(i, {}).get(k, facts[i].get(k)))


for i, m in D["display"].items():
    p = P(i)
    vals = cur(i, "values")
    for k, d in m.items():
        hit = [v for v in vals if v["key"] == k]
        if not hit:
            problems.append(f"{i}: no key {k}")
        for v in hit:
            v["display"] = d
    p["values"] = vals

for i, lst in D["add_values"].items():
    p = P(i)
    vals = cur(i, "values")
    for k, d in lst:
        if any(v["key"] == k for v in vals):
            problems.append(f"{i}: key exists {k}")
        vals.append({"key": k, "display": d})
    p["values"] = vals

for i in D["hard_true"]:
    if facts[i].get("hard"):
        problems.append(f"{i} already hard")
    P(i)["hard"] = True

for i, r in D["relevance"].items():
    P(i)["exam_relevance"] = r

for i, src in D["change_items_from"].items():
    ci = list(facts[i].get("change_items") or [])
    for c in facts[src].get("change_items") or []:
        if c not in ci:
            ci.append(c)
    P(i)["change_items"] = ci

# bullets of superseded facts go to the kept fact
for o, n, _ in D["supersede"]:
    if n in gone:
        problems.append(f"target retired: {n}")
    b = cur(n, "bullets") or []
    nb = list(b)
    for x in facts[o].get("bullets") or []:
        if x not in nb:
            nb.append(x)
    if nb != b:
        P(n)["bullets"] = nb

# scopes for live facts without one
SCOPE_RULES = [
    (r"^rds-proxy-", "Amazon RDS Proxy"),
    (r"^rds-(faq-)?blue-green-|^rds-change-blue-green-", "RDS Blue/Green Deployments"),
    (r"^rds-multi-az-cluster-", "Multi-AZ DB cluster deployments"),
    (r"^rds-compare-maz-", "RDS deployment options: Single-AZ, Multi-AZ with one standby, Multi-AZ with two readable standbys"),
    (r"^rds-compare-", "non-Aurora RDS: Multi-AZ deployments, multi-Region deployments and read replicas"),
    (r"^rds-faq-multiaz-two-readable", "Multi-AZ DB cluster deployments (two readable standbys) with RDS Proxy"),
    (r"^rds-(faq-)?multi-?az|^rds-faq-multi-az", "Multi-AZ DB instance deployments"),
    (r"^rds-cross-region-replica|^rds-faq-read-replica-cross-region", "cross-Region read replicas"),
    (r"^rds-cross-region-backup", "cross-Region automated backups"),
    (r"^rds-(faq-)?read-replica|^rds-replica", "RDS DB instance read replicas"),
    (r"^rds-(faq-)?ri-", "RDS reserved DB instances"),
    (r"^rds-extended-support|^rds-change-extended-support", "RDS Extended Support"),
    (r"^rds-(faq-)?encrypt|^rds-kms-|^rds-faq-tde", "RDS encryption at rest"),
    (r"^rds-export-snapshot", "snapshot export to Amazon S3"),
    (r"database-insights|performance-insights", "CloudWatch Database Insights and Performance Insights"),
    (r"enhanced-monitoring", "RDS Enhanced Monitoring"),
    (r"^rds-decision-guide", "AWS database decision guide (Choosing an AWS database service)"),
    (r"^rds-wa-", "AWS Well-Architected Framework guidance"),
    (r"^rds-case-", "AWS customer case study"),
    (r"^rds-sec-bp-", "RDS security best practices"),
    (r"^rds-bp-", "RDS basic operational guidelines"),
    (r"^rds-(faq-)?(savings-plans|database-savings)|^rds-change-database-savings", "Database Savings Plans"),
    (r"^rds-pricing-|^rds-faq-billing-|^rds-billing-", "Amazon RDS billing"),
    (r"^rds-ena-express|^rds-change-ena-express", "Cross-AZ ENA Express for Multi-AZ DB instances"),
    (r"^rds-(tls|faq-ssl)", "encryption in transit (SSL/TLS) to RDS databases"),
    (r"^rds-secrets-manager|^rds-change-secrets-manager", "RDS-managed master user password in AWS Secrets Manager"),
    (r"^rds-vs-ec2-", "Amazon RDS compared with a database on Amazon EC2 or on premises"),
    (r"^rds-class-", "DB instance classes"),
    (r"^rds-(faq-)?parameter|^rds-option-group", "DB parameter groups and option groups"),
    (r"^rds-restore-|^rds-faq-restore", "restoring a DB instance from a snapshot or a point in time"),
    (r"^rds-(share|snapshot)|^rds-faq-snapshots", "DB snapshots"),
    (r"^rds-(faq-)?delete|^rds-retained", "deleting a DB instance and its backups"),
    (r"^rds-(faq-)?(backup|automated-backup|aws-backup|retention|backups)|^rds-faq-automated-backups|^rds-keep-automated|^rds-resilience-pitr|^rds-faq-pitr|^rds-faq-retention", "RDS automated backups and snapshots"),
    (r"^rds-(faq-)?storage|^rds-faq-piops|^rds-faq-general-purpose|^rds-faq-magnetic|^rds-faq-optimized|^rds-optimized|^rds-change-(gp3|io2|magnetic|dedicated|additional-storage)", "RDS DB instance storage and performance"),
    (r"maintenance|upgrade|patching|deprecation", "RDS maintenance and engine upgrades"),
    (r"^rds-change-(optimized)", "RDS Optimized Reads and Optimized Writes"),
    (r"^rds-change-zero-etl|^rds-zero-etl", "RDS zero-ETL integrations"),
    (r"^rds-change-postgresql-delayed|^rds-delayed-replica|delayed-replication", "delayed read replicas"),
    (r"^rds-change-read-replicas", "RDS DB instance read replicas"),
    (r"^rds-change-proxy", "Amazon RDS Proxy"),
    (r"^rds-change-cross-region-cross-account", "DB snapshot copy across Regions and accounts"),
    (r"^rds-change-custom|^rds-custom", "Amazon RDS Custom"),
]
OVERRIDE = {
    "rds-apply-immediately-downtime-risk": "DB instance modifications",
    "rds-cloudwatch-monitor-capacity-limits": "RDS basic operational guidelines",
    "rds-console-dms-cdc-keeps-target-available": "RDS console migration with AWS DMS",
    "rds-customer-owns-query-tuning": "RDS shared responsibility",
    "rds-default-choice-relational": "relational database deployments on AWS",
    "rds-ec2-database-user-error-risk": "self-managed database on Amazon EC2",
    "rds-engine-upgrade-downtime-blue-green": "RDS maintenance and engine upgrades",
    "rds-event-subscription-sns": "RDS event notifications",
    "rds-events-eventbridge-rules": "RDS events in Amazon EventBridge",
    "rds-faq-apply-immediately-pending-changes": "DB instance modifications",
    "rds-faq-aws-config-records-rds": "configuration monitoring of RDS resources",
    "rds-faq-cloudtrail-api-history": "RDS API call history",
    "rds-faq-compute-scale-brief-outage": "DB instance class changes (Single-AZ)",
    "rds-faq-ec2-connection-automation": "RDS console database creation",
    "rds-faq-engines": "Amazon RDS engines",
    "rds-faq-existing-code-works": "Amazon RDS engines",
    "rds-faq-hipaa-eligible": "all RDS database engines",
    "rds-faq-iam-policies-tags": "access control to RDS resources",
    "rds-faq-lambda-connection-recommends-proxy": "RDS console Lambda connection setup",
    "rds-faq-onprem-access-security-groups": "network access to RDS databases",
    "rds-faq-private-subnet-backend": "RDS DB instances in a VPC",
    "rds-faq-rds-vs-ec2-ami": "Amazon RDS compared with a database AMI on Amazon EC2",
    "rds-faq-scale-beyond-largest-partitioning": "scaling beyond one DB instance",
    "rds-faq-storage-scale-stays-available": "storage increases of a DB instance",
    "rds-faq-subnet-group-every-az": "DB subnet groups",
    "rds-faq-use-dns-name-ip-changes": "connecting to a DB instance",
    "rds-firewall-blocks-until-sg-rules": "new DB instances",
    "rds-iam-manages-resources-not-login": "access to RDS resources and databases",
    "rds-instance-class-changeable": "DB instance classes",
    "rds-managed-tasks": "Amazon RDS managed operations",
    "rds-faq-backup-patching-managed": "Amazon RDS managed operations",
    "rds-multi-region-async-replica-survives-region": "cross-Region read replicas",
    "rds-on-outposts-hybrid": "Amazon RDS on Outposts",
    "rds-other-vpc-access-peering": "access from an EC2 instance in another VPC",
    "rds-private-access-vpn-direct-connect": "DB instances in a VPC that are not publicly accessible",
    "rds-private-subnet-web-tier-pattern": "DB instances in a VPC",
    "rds-security-group-source-sg": "VPC security groups for DB instances",
    "rds-security-managed-processes": "security configuration for RDS",
    "rds-separate-azs-protect-location-failure": "DB instances in several Availability Zones",
    "rds-vpc-no-additional-cost": "DB instances in a VPC",
    "rds-change-database-insights-2025-02": "CloudWatch Database Insights and Performance Insights",
    "rds-change-performance-insights-eol-announced-2025-05": "CloudWatch Database Insights and Performance Insights",
    "rds-performance-insights-eol-migrated-database-insights": "CloudWatch Database Insights and Performance Insights",
    "rds-change-storage-modifications-four-2026-07": "storage modifications of a DB instance",
    "rds-mysql-delayed-replication-dr": "RDS for MySQL delayed replication",
    "rds-postgresql-delayed-replication-purpose": "RDS for PostgreSQL delayed replication",
    "rds-long-term-backup-export-s3": "RDS for MariaDB, MySQL and PostgreSQL",
    "rds-snapshots-incremental": "DB snapshots",
    "rds-faq-snapshots-user-initiated-kept-until-deleted": "manual DB snapshots",
    "rds-faq-read-replica-cross-region-lag": "cross-Region read replicas",
    "rds-encryption-kms-regional-replica": "encrypted cross-Region read replicas",
    "rds-encryption-cannot-turn-off": "encrypted DB instances",
    "rds-resilience-replica-promote-dr": "RDS DB instance read replicas",
    "rds-resilience-snapshot-restore-dr": "DB snapshots",
    "rds-multi-az-one-vs-two-standbys": "Multi-AZ DB instance and Multi-AZ DB cluster deployments",
    "rds-faq-read-replica-mysql-ddl": "RDS for MySQL and RDS for PostgreSQL read replicas",
    "rds-faq-read-replica-oracle-sqlserver-no-cascade": "RDS for Oracle and RDS for SQL Server read replicas",
    "rds-faq-read-replica-source-deleted-mysql": "RDS for MySQL and RDS for MariaDB read replicas",
    "rds-faq-read-replica-source-deleted-postgresql": "RDS for PostgreSQL read replicas",
    "rds-faq-read-replica-three-tiers": "Aurora, RDS for MySQL and RDS for MariaDB read replicas",
    "rds-faq-read-replica-asynchronous": "read replicas of RDS for MySQL, MariaDB, PostgreSQL, Oracle and SQL Server",
    "rds-faq-tde-oracle-sqlserver": "RDS for Oracle and RDS for SQL Server",
    "rds-faq-optimized-writes-2x": "RDS for MySQL",
    "rds-faq-optimized-reads-nvme-2x": "RDS for MySQL and RDS for MariaDB",
    "rds-faq-general-purpose-ssd-3-iops-per-gb": "General Purpose (SSD) storage as the RDS FAQ describes it",
    "rds-faq-compute-scale-brief-outage": "DB instance class changes",
}
scopes = {}
for i, f in sorted(facts.items()):
    if f["status"] in ("rejected", "superseded") or i in gone:
        continue
    q = f.get("qualifiers") or {}
    if q.get("scope"):
        continue
    s = OVERRIDE.get(i)
    if s is None:
        for rx, val in SCOPE_RULES:
            if re.search(rx, i):
                s = val
                break
    if s is None:
        problems.append("no scope rule for " + i)
        continue
    q2 = copy.deepcopy(cur(i, "qualifiers") or {})
    q2["scope"] = s
    P(i)["qualifiers"] = q2
    scopes[i] = s


def norm(s):
    return normalize_text(s or "").lower()


# display checks: verbatim (number-free: <= 8 words, held by a quote)
for i, p in patch.items():
    if "values" not in p:
        continue
    quotes = [norm(e.get("quote")) for e in facts[i]["evidence"]]
    for v in p["values"]:
        d = v["display"]
        nd = norm(d)
        if not re.search(r"\d", d):
            if len(d.split()) > 8:
                problems.append(f"{i}: display over 8 words: {d}")
            if not any(nd in q for q in quotes):
                problems.append(f"{i}: display not verbatim in a quote: {d}")
    keys = [v["key"] for v in p["values"]]
    if len(set(keys)) != len(keys):
        problems.append(f"{i}: duplicate keys")

for i, p in patch.items():
    json.dump(p, open(OUT + i + ".json", "w"), ensure_ascii=False, indent=1)
json.dump({"patches": sorted(patch), "scopes": scopes, "problems": problems}, open(W + "reg-build-report.json", "w"), ensure_ascii=False, indent=1)
print("patches", len(patch), "scopes", len(scopes), "problems", len(problems))
for x in problems:
    print("PROBLEM", x)
