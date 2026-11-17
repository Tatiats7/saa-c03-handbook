"""Builds brief.v0.json and mine-plan.json for chapter 09 (detection services).

Run from the repo root after the page batches have finished:
    python3 aws-saa-book/_build/work/09-detection/make-brief.py
It reads the corpus to count which sources are saved and lists the rest as
fetch_failures. No network access.
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from saalib import corpus  # noqa: E402

WORK = ROOT / "_build/work/09-detection"
registry = json.load(open(ROOT / "data/book.json"))
chapters = registry["chapters"] if isinstance(registry, dict) and "chapters" in registry else registry
entry = next(c for c in chapters if c.get("id") == "09")
src = entry["sources"]

batch_urls = []
for name in ("urls-1.txt", "urls-2.txt", "urls-3.txt", "urls-cases.txt"):
    batch_urls += [u.strip() for u in open(WORK / name) if u.strip()]
universe = []
for key in ("pages", "faq", "history", "quotas", "pricing"):
    universe += src[key]
universe += batch_urls
seen, ordered = set(), []
for u in universe:
    if u not in seen:
        seen.add(u)
        ordered.append(u)

fetched, failures = [], []
for u in ordered:
    sid = corpus.source_id_for(u)
    if corpus.load_text(sid) is not None:
        fetched.append(sid)
    else:
        failures.append({"url": u, "source_id": sid,
                         "reason": "still queued behind the shared 1-request-per-second rate slot when plan ended (plan closed early to start mining sooner); miners fetch on demand: saa.py fetch --batch aws-saa-book/_build/work/09-detection/urls-pending.txt"})
with open(WORK / "urls-pending.txt", "w") as fh:
    fh.write("".join(f["url"] + "\n" for f in failures))

GD = "docs/guardduty/latest/ug/"
INS = "docs/inspector/latest/user/"
MAC = "docs/macie/latest/user/"
SH = "docs/securityhub/latest/userguide/"
DET = "docs/detective/latest/userguide/"
CFG = "docs/config/latest/developerguide/"
ART = "docs/artifact/latest/ug/"
DG = "docs/decision-guides/latest/decision-guides/choosing-aws-security-services"
WP = "docs/whitepapers/latest/aws-overview/security-services"
WPC = "docs/whitepapers/latest/aws-overview/security-and-compliance"
SRA = "docs/prescriptive-guidance/latest/security-reference-architecture/introduction"
WAD = "docs/wellarchitected/latest/security-pillar/detection"
F = {s: f"www/{s}/faqs" for s in ("guardduty", "inspector", "security-hub", "detective", "config")}
F["macie"] = "www/macie/faq"
F["artifact"] = "www/artifact/faq"
P = {s: f"www/{s}/pricing" for s in ("guardduty", "inspector", "macie", "security-hub", "detective", "config")}

B = {"k5": "1.2.K5", "k3": "1.3.K3", "s1": "1.3.S1"}
N, BD, FQ = "numbers+changes", "behavior+decisions", "faq"

# (bullet, lens, service, question, source hints)
D = [
    # ---------------- Decision map: which service for which finding
    ("k5", BD, "security-hub", "Decision map: for 'detect threats', 'find sensitive data (PII) in S3', 'scan for software vulnerabilities', 'investigate the root cause of a finding', 'see all findings in one place', 'record configuration changes and check compliance', 'download a compliance report': which service does AWS name for each (one quotable sentence per service)?", [DG, WP, WAD]),
    ("k5", BD, "security-hub", "One-sentence definition of each of the seven services from the AWS overview whitepaper and the security decision guide (for 'In one breath').", [WP, WPC, DG]),
    ("k5", BD, "guardduty", "GuardDuty versus Inspector: threat detection from activity (logs, runtime) versus vulnerability and exposure scanning of workloads; what does each page say the service looks at?", [GD + "what-is-guardduty", INS + "what-is-inspector", DG]),
    ("k5", BD, "macie", "Macie versus GuardDuty S3 Protection versus GuardDuty Malware Protection for S3: sensitive data in objects versus suspicious access to S3 versus malware in uploaded objects.", [MAC + "what-is-macie", GD + "s3-protection", GD + "gdu-malware-protection-s3"]),
    ("k5", BD, "detective", "Detective versus GuardDuty versus Security Hub: who finds the threat, who aggregates it, who helps investigate it (behavior graph); what does the Detective page say it does not do (it does not generate the original findings)?", [DET + "what-is-detective", F["detective"], DG]),
    ("k5", BD, "config", "Config versus CloudTrail versus CloudWatch (pointer to chapter 37): configuration history and rules versus API activity versus metrics; the Config FAQ answer on how Config differs from CloudTrail.", [F["config"], CFG + "WhatIsConfig"]),
    ("s1", BD, "config", "Config rules versus Security Hub CSPM controls: does Security Hub CSPM run its controls through AWS Config rules, and must the Config recorder be on for those controls?", [SH + "securityhub-setup-prereqs", SH + "securityhub-controls-finding-generation", F["security-hub"]]),
    ("s1", BD, "config", "Config conformance packs versus Security Hub CSPM standards versus AWS Audit Manager (pointer): which one 'checks resources against a framework' and which one 'collects audit evidence'?", [CFG + "conformance-packs", SH + "standards-reference", DG]),
    ("s1", BD, "artifact", "Artifact versus Config versus Audit Manager: Artifact gives AWS's own compliance reports and agreements, not an assessment of your resources; where does AWS state this?", [ART + "what-is-aws-artifact", F["artifact"], DG]),
    ("k5", BD, "security-hub", "Which services send findings into Security Hub automatically (GuardDuty, Inspector, Macie, Config, IAM Access Analyzer, Firewall Manager and others), and in which format (ASFF for CSPM, OCSF for the new Security Hub)?", [SH + "securityhub-internal-providers", SH + "what-is-securityhub-v2", SH + "securityhub-v2-concepts"]),
    ("k5", BD, "security-hub", "Which services send findings to Amazon EventBridge for automated response (GuardDuty, Inspector, Macie, Security Hub, Config) and what is the usual remediation chain (EventBridge rule to Lambda or Systems Manager Automation)?", [GD + "guardduty_findings_eventbridge", MAC + "findings-monitor", SH + "securityhub-cwe-integration-types", CFG + "remediation"]),
    ("k5", BD, "security-hub", "Security reference architecture: which account runs these services (Security Tooling account, delegated administrator) and how does the reference architecture describe each service's role?", [SRA, GD + "guardduty_organizations"]),
    ("k5", BD, "security-hub", "Well-Architected security pillar, detection: which best practices name these services (configure service and application logging, analyze logs findings and metrics centrally)?", [WAD]),
    # ---------------- GuardDuty
    ("k5", BD, "guardduty", "What is GuardDuty: a threat detection service that continuously monitors which foundational data sources (CloudTrail management events, VPC Flow Logs, Route 53 Resolver DNS query logs)?", [GD + "what-is-guardduty", GD + "guardduty_data-sources"]),
    ("k5", BD, "guardduty", "Does GuardDuty need you to turn on VPC Flow Logs, DNS logs or a CloudTrail trail yourself, and does it change your logging or store your logs (independent data streams)?", [GD + "guardduty_data-sources", F["guardduty"]]),
    ("k5", BD, "guardduty", "Does enabling GuardDuty affect the performance or availability of workloads (no agents for the foundational sources)?", [F["guardduty"], GD + "what-is-guardduty"]),
    ("k5", BD, "guardduty", "Which protection plans exist (S3 Protection, EKS Protection, Runtime Monitoring, Malware Protection for EC2, Malware Protection for S3, RDS Protection, Lambda Protection, AI Protection) and what does each monitor?", [GD + "protection-plans-overview", GD + "what-is-guardduty"]),
    ("k5", BD, "guardduty", "S3 Protection: which events does GuardDuty analyze (CloudTrail data events for S3) and which threats does it find (suspicious access, data exfiltration)?", [GD + "s3-protection", F["guardduty"]]),
    ("k5", BD, "guardduty", "Malware Protection for S3: scans newly uploaded objects in selected buckets; can it be used without enabling GuardDuty itself; how are results reported (object tags, EventBridge); what does it not scan?", [GD + "gdu-malware-protection-s3", F["guardduty"]]),
    ("k5", BD, "guardduty", "Malware Protection for EC2: agentless scan of EBS volumes, GuardDuty-initiated versus on-demand scans; what triggers a GuardDuty-initiated scan?", [GD + "malware-protection", F["guardduty"]]),
    ("k5", BD, "guardduty", "Runtime Monitoring: which compute (EKS, ECS on Fargate, EC2) and does it need the GuardDuty security agent?", [GD + "runtime-monitoring", F["guardduty"]]),
    ("k5", BD, "guardduty", "RDS Protection: which engines (Aurora, RDS for PostgreSQL, MySQL, MariaDB) and which activity (login events) does it analyze?", [GD + "rds-protection"]),
    ("k5", BD, "guardduty", "Extended Threat Detection: what is an attack sequence finding, is it on by default, and at what cost?", [GD + "guardduty-extended-threat-detection", F["guardduty"]]),
    ("k5", BD, "guardduty", "Trusted IP lists and threat lists: what does each change in findings, and how many of each per account?", [GD + "guardduty_upload-lists", GD + "guardduty_limits"]),
    ("k5", BD, "guardduty", "Findings: what are the severity levels and ranges, and does GuardDuty block or remediate threats by itself (no: detection only)?", [GD + "guardduty_findings-severity", F["guardduty"], GD + "guardduty_concepts"]),
    ("k5", BD, "guardduty", "Example finding types the exam uses (cryptocurrency mining, communication with known malicious IPs, unusual API calls, credential exfiltration, root credential use): which family names do they belong to?", [GD + "guardduty_concepts", F["guardduty"]]),
    ("k5", BD, "guardduty", "Multi-account: delegated administrator through AWS Organizations, auto-enable for new member accounts; is GuardDuty a Regional service that must be enabled in every Region?", [GD + "guardduty_organizations", GD + "guardduty_regions", F["guardduty"]]),
    ("k5", BD, "guardduty", "What happens when you suspend versus disable GuardDuty (findings and configuration kept or deleted)?", [GD + "guardduty_suspend-disable"]),
    ("k5", N, "guardduty", "Free trial length for GuardDuty and for each protection plan, and the cost estimate shown in the console.", [F["guardduty"], GD + "guardduty-pricing", P["guardduty"]]),
    ("k5", N, "guardduty", "Pricing dimensions: per GB or per million events analyzed (CloudTrail management events, VPC Flow Logs and DNS logs, S3 data events, EKS audit logs, runtime vCPU, EBS GB scanned, S3 GB scanned, RDS login events).", [P["guardduty"], GD + "guardduty-pricing"]),
    ("k5", N, "guardduty", "Quotas: member accounts per administrator, findings retention period, trusted IP and threat lists per account, suppression rules (filters) per Region.", [GD + "guardduty_limits", F["guardduty"]]),
    ("k5", N, "guardduty", "How long does GuardDuty keep findings (days), and how do you keep them longer (export to S3 through EventBridge or the export feature)?", [GD + "guardduty_limits", F["guardduty"], GD + "guardduty_findings_eventbridge"]),
    ("k5", N, "guardduty", "How often are updated findings published to EventBridge by default (minutes), and can this be changed?", [GD + "guardduty_findings_eventbridge"]),
    ("k5", N, "guardduty", "Changed recently (hypothesis): Malware Protection for S3 (2024-06-11) replaces build-your-own Lambda antivirus as the best answer; verify date and wording.", [GD + "doc-history", GD + "gdu-malware-protection-s3"]),
    ("k5", N, "guardduty", "Changed recently (hypotheses): Extended Threat Detection (2024-12-01), Runtime Monitoring consolidated (2023/2024), RDS Protection (2023), Lambda Protection (2023), Malware Protection for Backup (2025-11-19), Malware Protection for S3 on-demand (2025-11-17), AI Protection (2026-07-13), Custom Detection Rules (2026-09-01): dates and examinability.", [GD + "doc-history"]),
    # ---------------- Inspector
    ("k5", BD, "inspector", "What is Inspector: automated vulnerability management that scans which resources (EC2 instances, container images in ECR, Lambda functions, code repositories) for which issues (software vulnerabilities, unintended network exposure)?", [INS + "what-is-inspector", INS + "scanning-resources", F["inspector"]]),
    ("k5", BD, "inspector", "EC2 scanning: agent-based (SSM Agent) versus agentless (EBS snapshots) and hybrid mode; what is needed for agent-based scanning (Systems Manager managed instance)?", [INS + "scanning-ec2", F["inspector"]]),
    ("k5", BD, "inspector", "ECR scanning: basic scanning (ECR) versus enhanced scanning (Inspector); continuous rescans when a new CVE is published; scan on push.", [INS + "scanning-ecr", F["inspector"]]),
    ("k5", BD, "inspector", "Lambda scanning: standard scanning (dependencies) versus code scanning (code vulnerabilities).", [INS + "scanning-lambda"]),
    ("k5", BD, "inspector", "Does Inspector scan continuously and automatically (no scheduled assessment runs), and what triggers a rescan?", [INS + "what-is-inspector", F["inspector"]]),
    ("k5", BD, "inspector", "Inspector risk score: how is it computed from the CVSS base score and what does it add (network reachability, exploit availability)?", [INS + "findings-understanding-score"]),
    ("k5", BD, "inspector", "Network reachability findings: what does Inspector check about open paths to EC2 instances?", [INS + "scanning-ec2", INS + "what-is-inspector"]),
    ("s1", BD, "inspector", "CIS scans: on-demand or scheduled CIS benchmark assessments of EC2 operating systems; what do they check?", [INS + "scanning-cis", F["inspector"]]),
    ("k5", BD, "inspector", "SBOM export: what format (CycloneDX, SPDX) and where does Inspector deliver it?", [INS + "sbom-export"]),
    ("k5", BD, "inspector", "Code security: which repositories (GitHub, GitLab) and what it finds (SAST, secrets, infrastructure as code).", [INS + "code-security-assessments"]),
    ("k5", BD, "inspector", "Multi-account: delegated administrator, up to how many member accounts, auto-enable.", [INS + "admin-member-relationship", INS + "quotas"]),
    ("k5", N, "inspector", "Free trial length and pricing dimensions (per instance per month, per image scanned and rescanned, per Lambda function, CIS scans).", [P["inspector"], F["inspector"]]),
    ("k5", N, "inspector", "Quotas: member accounts per administrator, how long ECR images keep being rescanned (rescan duration settings), and other limits the exam may use.", [INS + "quotas", INS + "scanning-ecr"]),
    ("k5", N, "inspector", "Changed recently (hypothesis): Inspector Classic (agent-based assessment templates) fully shut down 2026-05-20; Inspector VM Scanner 2026-05-29 (not examinable yet); older questions may show assessment templates and the Inspector agent.", [INS + "doc-history", INS + "inspector-vm-scanner", F["inspector"]]),
    ("k5", N, "inspector", "Changed recently (hypotheses): agentless EC2 scanning GA (2024), Lambda code scanning (2023), CIS scans (2024), code security (2025); dates.", [INS + "doc-history"]),
    # ---------------- Macie
    ("k3", BD, "macie", "What is Macie: discovers sensitive data in which storage (S3 only) using machine learning and pattern matching, and evaluates bucket security and access controls?", [MAC + "what-is-macie", F["macie"]]),
    ("k3", BD, "macie", "Two ways to discover sensitive data: automated sensitive data discovery (sampling across the estate) versus sensitive data discovery jobs (targeted, one-time or scheduled).", [MAC + "discovery-asdd", MAC + "discovery-jobs"]),
    ("k3", BD, "macie", "Managed data identifiers (credit card numbers, credentials, personal information) versus custom data identifiers (regular expression plus keywords) versus allow lists.", [MAC + "managed-data-identifiers", MAC + "custom-data-identifiers", MAC + "allow-lists"]),
    ("k3", BD, "macie", "Two kinds of findings: policy findings (bucket made public, encryption off, shared outside account) versus sensitive data findings.", [MAC + "findings-types"]),
    ("k3", BD, "macie", "S3 bucket inventory and security posture: what does Macie monitor automatically (public access, encryption, sharing) once enabled?", [MAC + "monitoring-s3"]),
    ("k3", BD, "macie", "Which file and storage formats can Macie analyze, and which S3 storage classes or encryption types does it skip?", [MAC + "discovery-supported-storage"]),
    ("k3", BD, "macie", "Where do findings and discovery results go: Security Hub, EventBridge, and the discovery results repository in an S3 bucket (with KMS key); how long are results kept in Macie?", [MAC + "findings-monitor", MAC + "discovery-results-repository-s3", MAC + "macie-quotas"]),
    ("k3", BD, "macie", "Multi-account: Macie administrator through AWS Organizations; up to how many member accounts?", [MAC + "macie-accounts", MAC + "macie-quotas"]),
    ("k3", BD, "macie", "Does Macie remediate (delete, mask or encrypt) the data it finds (no), and what is the usual follow-up (EventBridge to Lambda, S3 Object Lock, lifecycle)?", [MAC + "what-is-macie", F["macie"]]),
    ("k3", N, "macie", "Free trial length and what it covers (bucket inventory, automated discovery); pricing dimensions: per bucket evaluated per month, per GB inspected, objects monitored.", [MAC + "account-mgmt-free-trial", P["macie"], F["macie"]]),
    ("k3", N, "macie", "Quotas: data processed per account per day by jobs, custom data identifiers per account, member accounts, finding retention days.", [MAC + "macie-quotas"]),
    ("k3", N, "macie", "Changed recently (hypotheses): automated sensitive data discovery (2022-11-28), allow lists (2022), Macie VPC endpoints (2025-07-02, no exam effect); verify.", [MAC + "doc-history"]),
    # ---------------- Security Hub
    ("k5", BD, "security-hub", "Two products today: the new unified AWS Security Hub (GA 2025-12-02) and AWS Security Hub CSPM (the original service, renamed); what does each do according to 'What are the Security Hub services'?", [SH + "what-are-securityhub-services", SH + "what-is-securityhub-v2", SH + "what-is-securityhub"]),
    ("k5", BD, "security-hub", "Security Hub CSPM: security best practice checks (controls in standards) plus aggregation of findings from AWS services and partners; what is a control, a standard, a security score?", [SH + "what-is-securityhub", SH + "standards-reference"]),
    ("s1", BD, "security-hub", "Which standards does Security Hub CSPM support (AWS Foundational Security Best Practices, CIS AWS Foundations Benchmark, NIST SP 800-53, PCI DSS, AWS Resource Tagging) and which is enabled by default?", [SH + "standards-reference", SH + "fsbp-standard"]),
    ("s1", BD, "security-hub", "Does Security Hub CSPM need AWS Config enabled with resource recording, and which controls are change-triggered versus periodic?", [SH + "securityhub-setup-prereqs", SH + "securityhub-controls-finding-generation"]),
    ("k5", BD, "security-hub", "New Security Hub: exposure findings and correlation of signals from GuardDuty, Inspector, Macie and CSPM; what does it add over CSPM (risk prioritization, attack paths)?", [SH + "what-is-securityhub-v2", SH + "exposure-findings", SH + "securityhub-v2-concepts"]),
    ("k5", BD, "security-hub", "Cross-Region aggregation: one home Region collects findings from linked Regions; does it apply to both Security Hub and CSPM?", [SH + "security-hub-region-aggregation", SH + "finding-aggregation"]),
    ("k5", BD, "security-hub", "Central configuration: the delegated administrator configures Security Hub CSPM for the organization from the home Region with configuration policies.", [SH + "central-configuration-intro"]),
    ("k5", BD, "security-hub", "Automation rules: update or suppress findings automatically in near real time; custom actions and EventBridge for response.", [SH + "automation-rules", SH + "securityhub-cwe-integration-types"]),
    ("k5", BD, "security-hub", "Is Security Hub a Regional service, and does it need to be enabled in each account and Region (or through Organizations auto-enable)?", [SH + "what-is-securityhub", F["security-hub"], SH + "central-configuration-intro"]),
    ("k5", N, "security-hub", "How long does Security Hub CSPM keep findings: active findings, archived findings (days), and the 2025 change of archived retention.", [SH + "securityhub-data-retention", SH + "doc-history"]),
    ("k5", N, "security-hub", "Pricing dimensions: Security Hub CSPM per security check and per finding ingestion event; new Security Hub per resource or per account; free trial length.", [P["security-hub"], F["security-hub"]]),
    ("k5", N, "security-hub", "Quotas: member accounts per administrator, automation rules per Region, insights, custom actions.", [SH + "securityhub_limits"]),
    ("k5", N, "security-hub", "Changed recently (hypotheses): rename to Security Hub CSPM (2025-06), new unified Security Hub GA (2025-12-02), archived finding retention 90 to 30 days (2025-06-20), central configuration (2023-11-27), automation rules (2023-06-13), Remediation plans (2026-09-30, not examinable yet). Older questions say just 'Security Hub'.", [SH + "doc-history", SH + "what-are-securityhub-services"]),
    # ---------------- Detective
    ("k5", BD, "detective", "What is Detective: analyzes, investigates and identifies the root cause of findings or suspicious activity using a behavior graph built from which data (CloudTrail, VPC Flow Logs, GuardDuty findings, EKS audit logs, security findings)?", [DET + "what-is-detective", DET + "detective-source-data-about"]),
    ("k5", BD, "detective", "Does Detective require GuardDuty to be enabled first (the requirement was removed 2024-02-02: verify) and how long must an account be enabled before the graph is useful (training period)?", [DET + "detective-prerequisites", DET + "behavior-graph-data-about", DET + "doc-history"]),
    ("k5", BD, "detective", "Finding groups and investigations: what do they do (group related findings, investigate IAM users and roles for indicators of compromise)?", [DET + "groups-about", DET + "investigations-about"]),
    ("k5", BD, "detective", "Multi-account: administrator account and members, Organizations delegated administrator.", [DET + "accounts-designate-admin"]),
    ("k5", N, "detective", "How much historical data does the behavior graph keep (up to how many days), and the maximum data volume per behavior graph per day.", [DET + "regions-limitations", DET + "behavior-graph-data-about", F["detective"]]),
    ("k5", N, "detective", "Pricing dimension (per GB ingested), free trial length, and how the projected cost is shown.", [P["detective"], DET + "usage-projected-cost-calculation", F["detective"]]),
    ("k5", N, "detective", "Quotas: member accounts per behavior graph.", [DET + "regions-limitations"]),
    # ---------------- Config
    ("s1", BD, "config", "What is AWS Config: a detailed view of resource configuration, how resources relate, configuration history over time, and evaluation against desired configurations?", [CFG + "WhatIsConfig", CFG + "how-does-config-work"]),
    ("s1", BD, "config", "Configuration recorder, configuration items, delivery channel (S3 bucket, SNS topic): what is each?", [CFG + "config-concepts", CFG + "how-does-config-work"]),
    ("s1", BD, "config", "Which resources does Config record (all supported types or a selected list), and recording frequency continuous versus daily (periodic recording).", [CFG + "select-resources", CFG + "config-concepts"]),
    ("s1", BD, "config", "Config rules: AWS managed rules versus custom rules (Lambda or Guard); trigger types change-triggered versus periodic; evaluation modes detective versus proactive.", [CFG + "evaluate-config", CFG + "evaluate-config_components", CFG + "managed-rules-by-trigger-type", CFG + "evaluate-config_turn-on-proactive-rules"]),
    ("s1", BD, "config", "Does a Config rule prevent a non-compliant change (no: it evaluates and reports), and what does proactive evaluation check before deployment?", [CFG + "evaluate-config", CFG + "evaluate-config_turn-on-proactive-rules", F["config"]]),
    ("s1", BD, "config", "Remediation: manual versus automatic remediation with Systems Manager Automation documents; retries.", [CFG + "remediation", CFG + "setup-autoremediation"]),
    ("s1", BD, "config", "Conformance packs: a collection of rules and remediation actions deployed as one entity in an account and Region or across an organization; sample templates (for example operational best practices for PCI DSS, HIPAA).", [CFG + "conformance-packs"]),
    ("s1", BD, "config", "Aggregators: a multi-account, multi-Region view of configuration and compliance data; with Organizations or individual account authorization.", [CFG + "aggregate-data"]),
    ("s1", BD, "config", "Organization rules and conformance packs deployed from the management account or delegated administrator.", [CFG + "config-rule-multi-account-deployment"]),
    ("s1", BD, "config", "Advanced query: SQL-like queries of current configuration state across accounts through an aggregator.", [CFG + "querying-AWS-resources"]),
    ("s1", BD, "config", "Notifications: configuration changes and compliance changes to SNS and EventBridge.", [CFG + "notifications-for-AWS-Config"]),
    ("k3", N, "config", "Data retention: default retention of configuration items (7 years?), the configurable retention period range (days), and that S3 delivered history is not deleted by it.", [CFG + "delete-config-data-with-retention-period", F["config"]]),
    ("s1", N, "config", "Pricing dimensions: per configuration item recorded (continuous versus periodic), per rule evaluation, per conformance pack evaluation.", [P["config"], F["config"]]),
    ("s1", N, "config", "Quotas: maximum Config rules per account per Region, conformance packs per account, aggregators per account.", [CFG + "configlimits"]),
    ("s1", N, "config", "Changed recently (hypotheses): periodic (daily) recording option (2023-11), proactive evaluation (2022-11), service-linked configuration recorders (2024-11-27), CloudWatch usage metrics (2024-04-26); dates.", [CFG + "DocumentHistory"]),
    # ---------------- Artifact
    ("s1", BD, "artifact", "What is AWS Artifact: on-demand access to AWS security and compliance reports (SOC, PCI, ISO) and online agreements (BAA); is it free?", [ART + "what-is-aws-artifact", F["artifact"]]),
    ("s1", BD, "artifact", "Agreements: accept for one account or for the whole organization (management account); which agreement is typical for HIPAA (BAA)?", [ART + "managing-agreements", F["artifact"]]),
    ("s1", BD, "artifact", "Reports: who can download them (IAM permissions), NDA or terms acceptance, third-party (ISV) reports through AWS Marketplace Vendor Insights.", [ART + "downloading-documents", F["artifact"]]),
    ("s1", BD, "artifact", "Notifications: email notifications for new reports and agreements; Assurance Assistant for compliance inquiries (2026-07-01, not examinable yet).", [ART + "managing-notifications", ART + "managing-compliance-inquiries", ART + "doc-history"]),
    ("s1", BD, "artifact", "Does Artifact certify your own workload as compliant (no: shared responsibility); where does AWS say the reports cover AWS infrastructure and services?", [ART + "what-is-aws-artifact", F["artifact"], WPC]),
    ("s1", N, "artifact", "Changed recently (hypotheses): third-party reports GA (2023-01-27), email notifications (2023-08), previous versions of reports (2025-12-16), Assurance Assistant (2026-06-30); dates.", [ART + "doc-history"]),
    # ---------------- Data classification and retention (1.3.K3)
    ("k3", BD, "macie", "Data classification: how does AWS describe classifying data by sensitivity, and which service discovers and classifies sensitive data in S3 (Macie)?", [MAC + "what-is-macie", DG, WP]),
    ("k3", BD, "config", "Retention of security evidence: how long each service keeps findings or history (GuardDuty, Security Hub CSPM, Macie, Detective, Config), and the pattern of exporting to S3 for longer retention.", [GD + "guardduty_limits", SH + "securityhub-data-retention", MAC + "macie-quotas", DET + "regions-limitations", CFG + "delete-config-data-with-retention-period"]),
    # ---------------- Callvale decision and real world
    ("s1", BD, "security-hub", "Callvale decision facts: delegated administrator for each service in an organization, auto-enable for new accounts, findings in one place (Security Hub), cross-Region aggregation; 'every finding needs an owner' (automation rules, workflow status).", [GD + "guardduty_organizations", SH + "central-configuration-intro", SH + "security-hub-region-aggregation", SH + "automation-rules"]),
    ("k3", BD, "macie", "Callvale decision facts: Macie finds card numbers in transcripts (managed data identifier for credit card numbers) and cost grows with data inspected (pricing per GB).", [MAC + "managed-data-identifiers", P["macie"]]),
    ("k5", BD, "guardduty", "Callvale decision facts: managed detection instead of open-source scanners on EC2: no agents or log pipelines to run for GuardDuty foundational sources; Inspector continuous scanning.", [GD + "what-is-guardduty", INS + "what-is-inspector"]),
    ("k5", BD, "security-hub", "Real company example: a case study that uses GuardDuty and Security Hub together (Sony Music Entertainment Japan or Games24x7).", ["www/solutions/case-studies/sony-music-entertainment-japan-case-study", "www/solutions/case-studies/games24x7-case-study-2024"]),
    ("k3", BD, "macie", "Real company example: Oportun uses Macie for sensitive data discovery (financial services).", ["www/solutions/case-studies/oportun-case-study"]),
    ("k5", BD, "inspector", "Real company example (optional): EDF Energy uses Inspector; Omni HR (startup) uses GuardDuty.", ["www/solutions/case-studies/edf-energy-security-case-study", "www/solutions/case-studies/omnihr-case-study"]),
    # ---------------- FAQ quick-fire
    ("k5", FQ, "guardduty", "FAQ quick-fire (GuardDuty): 'Does GuardDuty manage or keep my logs?', 'Does enabling GuardDuty affect performance?', 'Is GuardDuty a Regional or global service?', 'Can GuardDuty take automated actions?'", [F["guardduty"]]),
    ("k5", FQ, "guardduty", "FAQ quick-fire (GuardDuty): free trial, how GuardDuty is priced, and how findings are delivered (console, EventBridge, Security Hub, Detective).", [F["guardduty"]]),
    ("k5", FQ, "inspector", "FAQ quick-fire (Inspector): 'How is Amazon Inspector different from Inspector Classic?', 'Do I need an agent?', 'How often does Inspector scan?', 'How does Inspector work with ECR basic scanning?'", [F["inspector"]]),
    ("k3", FQ, "macie", "FAQ quick-fire (Macie): what Macie is, which data it analyzes, how it is priced, and the free trial.", [F["macie"]]),
    ("k5", FQ, "security-hub", "FAQ quick-fire (Security Hub): how Security Hub relates to GuardDuty, Inspector and Macie; is it a replacement for them; the difference between Security Hub and Security Hub CSPM.", [F["security-hub"]]),
    ("k5", FQ, "detective", "FAQ quick-fire (Detective): how Detective differs from GuardDuty and Security Hub; which data it uses; whether it needs agents.", [F["detective"]]),
    ("s1", FQ, "config", "FAQ quick-fire (Config): how Config differs from CloudTrail; what a configuration item is; does Config support multi-account multi-Region aggregation; what is a conformance pack.", [F["config"]]),
    ("s1", FQ, "artifact", "FAQ quick-fire (Artifact): what Artifact is, cost, who can access it, what a BAA is, and whether the reports can be shared with customers or auditors.", [F["artifact"]]),
]

demand = []
for n, (b, lens, service, q, hints) in enumerate(D, start=1):
    demand.append({"id": f"d{n:03d}", "bullet": B[b], "question": q, "status": "open", "facts": [],
                   "lens": lens, "service": service, "sources": hints})

covered = {d["bullet"] for d in demand}
missing = [b for b in entry["bullets"] if b not in covered]
if missing:
    print("BULLETS WITHOUT A DEMAND ITEM:", missing)
    sys.exit(1)

brief = {
    "chapter": "09",
    "slug": "detection",
    "title": entry["title"],
    "template": "medium",
    "services": entry["services"],
    "sources_fetched": len(fetched),
    "fetch_failures": failures,
    "sources": fetched,
    "demand": demand,
    "notes": [
        "Plan stage, run plan-09. Every demand item is a question; no answer is recorded here.",
        "FREQUENCY.md and FRESHNESS.md items appear only as hypotheses to check against the saved pages.",
        "Seven services, seven fact namespaces: guardduty-, inspector-, macie-, security-hub-, detective-, config-, artifact-. Prefer decision facts (which service for which finding) over feature lists.",
        "Displays of number-free facts are short phrases (at most 8 words) copied verbatim from a quote (RULINGS 2026-10-11).",
        "Examinability: GA after 2026-07-15 is 'not examinable yet' (GuardDuty Custom Detection Rules 2026-09-01, Security Hub Remediation plans 2026-09-30, Artifact Assurance Assistant 2026-07-01 is before the cutoff but within 3 months of an Oct exam: label per RULINGS rule 7 using the GA date from the saved page).",
        "Security Hub naming: the new unified AWS Security Hub (GA 2025-12-02) and AWS Security Hub CSPM (the original service). Older exam questions say 'Security Hub' for what is now CSPM; the chapter teaches both names once.",
        "Neighbour facts that live elsewhere: CloudTrail and CloudWatch (chapter 37), IAM Access Analyzer (chapter 03 or 05), Firewall Manager, WAF, Shield, Network Firewall (chapter 08), KMS (chapter 06), Organizations and SCPs (chapter 03 or 04), S3 Object Lock (chapter 21), Audit Manager (pointer only).",
    ],
}
json.dump(brief, open(WORK / "brief.v0.json", "w"), indent=1)

# ---- mine plan: pages and demand items per lens
pages = {N: [], BD: [], FQ: []}
for sid in fetched + [f["source_id"] for f in failures]:
    if sid.startswith("www/") and (sid.endswith("/faqs") or sid.endswith("/faq")):
        pages[FQ].append(sid)
        continue
    if any(k in sid for k in ("limits", "quotas", "regions-limitations", "/pricing", "guardduty-pricing", "doc-history",
                              "DocumentHistory", "data-retention", "delete-config-data-with-retention-period",
                              "free-trial", "projected-cost", "findings-severity", "findings-understanding-score")):
        pages[N].append(sid)
    if not any(k in sid for k in ("doc-history", "DocumentHistory", "/pricing")):
        pages[BD].append(sid)

plan = {
    "chapter": "09",
    "lenses": {
        lens: {"what": what, "pages": pages[lens], "demand": [d["id"] for d in demand if d["lens"] == lens],
               "extra_indexes": extra}
        for lens, what, extra in [
            (N, "Every number, limit, default, retention period, free-trial length, quota and price dimension of the seven services; every FRESHNESS hypothesis checked against the saved history page with its date (label GA after 2026-07-15 'not examinable yet'). Quote table rows with their header; one fact per value.",
             ["_build/corpus/changes/guardduty.jsonl", "_build/corpus/changes/inspector.jsonl", "_build/corpus/changes/macie.jsonl",
              "_build/corpus/changes/security-hub.jsonl", "_build/corpus/changes/detective.jsonl", "_build/corpus/changes/config.jsonl",
              "_build/corpus/changes/artifact.jsonl"]),
            (BD, "Can / cannot / only / does-not claims and the choice rules: which service detects, scans, classifies, investigates, aggregates, records, reports; data sources; agent or agentless; Regional scope and Organizations delegated administrator; integrations into Security Hub and EventBridge; Config rules, remediation, conformance packs, aggregators; Artifact reports and agreements; case-study sentences. Short verbatim displays (at most 8 words).",
             ["_build/corpus/cases/index.jsonl"]),
            (FQ, "Verbatim FAQ sentences for the quick-fire items and the comparison answers (GuardDuty vs Detective vs Security Hub, Config vs CloudTrail, Inspector vs Inspector Classic); quote from the FAQ snapshot, matched with find_quote.",
             ["_build/corpus/faq/guardduty.jsonl", "_build/corpus/faq/inspector.jsonl", "_build/corpus/faq/macie.jsonl",
              "_build/corpus/faq/security-hub.jsonl", "_build/corpus/faq/detective.jsonl", "_build/corpus/faq/config.jsonl",
              "_build/corpus/faq/artifact.jsonl"]),
        ]
    },
    "pending_fetch": [f["source_id"] for f in failures],
    "pending_fetch_command": "python3 aws-saa-book/tools/saa.py fetch --batch aws-saa-book/_build/work/09-detection/urls-pending.txt --out aws-saa-book/_build/work/09-detection/fetch-pending.txt",
    "work_files": sorted(p.name for p in WORK.glob("*.txt")),
    "rules": [
        "Quote only from snap/<source_id>.txt; full:<guide> hits are pointers.",
        "A FAQ or What's New row is an index, never the evidence; the fact's quote comes from the page snapshot.",
        "Fact namespaces per service; a comparison fact lives in the namespace of the service the question is about.",
        "Current AWS names only; 'Inspector Classic' and the plain name 'Security Hub' for CSPM may appear once as former names.",
    ],
}
json.dump(plan, open(WORK / "mine-plan.json", "w"), indent=1)
print(f"sources_fetched={len(fetched)} failures={len(failures)} demand={len(demand)}")
for f in failures:
    print("  missing:", f["url"])
for lens, v in plan["lenses"].items():
    print(f"  {lens}: pages={len(v['pages'])} demand={len(v['demand'])}")
