"""Official AWS Architecture Icons: download once, unpack, and build diagrams/icons.json.

The icons are used unmodified. "Cleaning" only removes what cannot live inside another document
(XML prolog, comments, <title>, <desc>, editor metadata) and drops id attributes that nothing
references, so that many icons can sit in one page without id collisions. Shapes, colours and
proportions are untouched.
"""
from __future__ import annotations

import re
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

from .. import common

ICONS_PAGE = "https://aws.amazon.com/architecture/icons/"
DOWNLOAD_HOST = "d1.awsstatic.com"
USER_AGENT = "saa-handbook-build/0.1 (study book; one-time icon package download)"

USAGE_STATEMENT_FALLBACK = ""


def icons_json_path() -> Path:
    return common.BOOK / "diagrams" / "icons.json"


def sprite_path() -> Path:
    return common.BOOK / "diagrams" / "icons.svg"


def notice_path() -> Path:
    return common.BOOK / "diagrams" / "ICONS-NOTICE.md"


def unpack_dir() -> Path:
    return common.TMP / "aws-icons"


# ------------------------------------------------------------------ name map
# book name -> list of candidate file stems (first match wins). A stem is the file name without
# the "Arch_" / "Res_" prefix and without the "_48" / "_48_Light" suffix, compared case-insensitively
# with "-", "_" and spaces removed.

SERVICES = {
    # identity and governance
    "iam": ["AWS-Identity-and-Access-Management"],
    "sts": ["AWS-Identity-Access-Management_AWS-STS"],
    "organizations": ["AWS-Organizations"],
    "control-tower": ["AWS-Control-Tower"],
    "ram": ["AWS-Resource-Access-Manager"],
    "iam-identity-center": ["AWS-IAM-Identity-Center"],
    "directory-service": ["AWS-Directory-Service"],
    "cognito": ["Amazon-Cognito"],
    # security
    "kms": ["AWS-Key-Management-Service"],
    "cloudhsm": ["AWS-CloudHSM"],
    "secrets-manager": ["AWS-Secrets-Manager"],
    "parameter-store": ["AWS-Systems-Manager_Parameter-Store"],
    "acm": ["AWS-Certificate-Manager"],
    "waf": ["AWS-WAF"],
    "shield": ["AWS-Shield"],
    "firewall-manager": ["AWS-Firewall-Manager"],
    "network-firewall": ["AWS-Network-Firewall"],
    "guardduty": ["Amazon-GuardDuty"],
    "inspector": ["Amazon-Inspector"],
    "macie": ["Amazon-Macie"],
    "security-hub": ["AWS-Security-Hub"],
    "detective": ["Amazon-Detective"],
    "config": ["AWS-Config"],
    "artifact": ["AWS-Artifact"],
    # networking
    "vpc": ["Amazon-Virtual-Private-Cloud"],
    "vpc-peering": ["Amazon-VPC_Peering-Connection"],
    "transit-gateway": ["AWS-Transit-Gateway"],
    "vpc-endpoints": ["Amazon-VPC_Endpoints"],
    "privatelink": ["AWS-PrivateLink"],
    "site-to-site-vpn": ["AWS-Site-to-Site-VPN"],
    "direct-connect": ["AWS-Direct-Connect"],
    "client-vpn": ["AWS-Client-VPN"],
    "route53": ["Amazon-Route-53"],
    "elb": ["Elastic-Load-Balancing"],
    "cloudfront": ["Amazon-CloudFront"],
    "global-accelerator": ["AWS-Global-Accelerator"],
    # compute
    "ec2": ["Amazon-EC2"],
    "ec2-auto-scaling": ["Amazon-EC2-Auto-Scaling"],
    "aws-auto-scaling": ["AWS-Auto-Scaling"],
    "lambda": ["AWS-Lambda"],
    "ecs": ["Amazon-Elastic-Container-Service"],
    "eks": ["Amazon-Elastic-Kubernetes-Service"],
    "fargate": ["AWS-Fargate"],
    "ecr": ["Amazon-Elastic-Container-Registry"],
    "ecs-anywhere": ["Amazon-ECS-Anywhere"],
    "eks-anywhere": ["Amazon-EKS-Anywhere"],
    "eks-distro": ["Amazon-EKS-Distro"],
    "elastic-beanstalk": ["AWS-Elastic-Beanstalk"],
    "batch": ["AWS-Batch"],
    "outposts": ["AWS-Outposts-family", "AWS-Outposts-rack"],
    "local-zones": ["AWS-Local-Zones"],
    "wavelength": ["AWS-Wavelength"],
    "vmware-cloud-on-aws": ["VMware-Cloud-on-AWS"],          # not in the 2026-07 package
    "serverless-application-repository": ["AWS-Serverless-Application-Repository"],
    # storage
    "s3": ["Amazon-Simple-Storage-Service"],
    "s3-glacier": ["Amazon-Simple-Storage-Service-Glacier", "Amazon-S3-Glacier"],
    "ebs": ["Amazon-Elastic-Block-Store"],
    "instance-store": ["Amazon-EC2_Instance"],
    "efs": ["Amazon-EFS", "Amazon-Elastic-File-System"],
    "fsx": ["Amazon-FSx"],
    "backup": ["AWS-Backup"],
    "storage-gateway": ["AWS-Storage-Gateway"],
    "datasync": ["AWS-DataSync"],
    "snow-family": ["AWS-Snowball", "AWS-Snow-Family", "AWS-Snowball-Edge"],
    "transfer-family": ["AWS-Transfer-Family"],
    # databases
    "rds": ["Amazon-RDS"],
    "rds-proxy": ["Amazon-RDS-Proxy-Instance"],
    "aurora": ["Amazon-Aurora"],
    "aurora-serverless": ["Amazon-Aurora_Amazon-Aurora-Instance-alternate", "Amazon-Aurora"],
    "dynamodb": ["Amazon-DynamoDB"],
    "dax": ["Amazon-DynamoDB_Amazon-DynamoDB-Accelerator"],
    "elasticache": ["Amazon-ElastiCache"],
    "redshift": ["Amazon-Redshift"],
    "documentdb": ["Amazon-DocumentDB"],
    "neptune": ["Amazon-Neptune"],
    "keyspaces": ["Amazon-Keyspaces"],
    # integration and data
    "sqs": ["Amazon-Simple-Queue-Service"],
    "sns": ["Amazon-Simple-Notification-Service"],
    "eventbridge": ["Amazon-EventBridge"],
    "step-functions": ["AWS-Step-Functions"],
    "mq": ["Amazon-MQ"],
    "appflow": ["Amazon-AppFlow"],
    "api-gateway": ["Amazon-API-Gateway"],
    "kinesis-data-streams": ["Amazon-Kinesis-Data-Streams"],
    "data-firehose": ["Amazon-Data-Firehose", "Amazon-Kinesis-Data-Firehose"],
    "msk": ["Amazon-Managed-Streaming-for-Apache-Kafka"],
    "athena": ["Amazon-Athena"],
    "glue": ["AWS-Glue"],
    "lake-formation": ["AWS-Lake-Formation"],
    "emr": ["Amazon-EMR"],
    "opensearch": ["Amazon-OpenSearch-Service"],
    "quick": ["Amazon-Quick-Suite", "Amazon-Quick", "Amazon-QuickSight"],
    "data-exchange": ["AWS-Data-Exchange"],
    "comprehend": ["Amazon-Comprehend"],
    "lex": ["Amazon-Lex"],
    "polly": ["Amazon-Polly"],
    "rekognition": ["Amazon-Rekognition"],
    "sagemaker-ai": ["Amazon-SageMaker-AI", "Amazon-SageMaker"],
    "textract": ["Amazon-Textract"],
    "transcribe": ["Amazon-Transcribe"],
    "translate": ["Amazon-Translate"],
    "elastic-transcoder": ["Amazon-Elastic-Transcoder"],      # not in the 2026-07 package
    "kinesis-video-streams": ["Amazon-Kinesis-Video-Streams"],
    "amplify": ["AWS-Amplify"],
    "device-farm": ["AWS-Device-Farm"],
    # operations and migration
    "cloudwatch": ["Amazon-CloudWatch"],
    "cloudtrail": ["AWS-CloudTrail"],
    "x-ray": ["AWS-X-Ray"],
    "health-dashboard": ["AWS-Health-Dashboard", "AWS-Personal-Health-Dashboard"],
    "managed-grafana": ["Amazon-Managed-Grafana"],
    "managed-prometheus": ["Amazon-Managed-Service-for-Prometheus"],
    "cloudformation": ["AWS-CloudFormation"],
    "systems-manager": ["AWS-Systems-Manager"],
    "service-catalog": ["AWS-Service-Catalog"],
    "license-manager": ["AWS-License-Manager"],
    "trusted-advisor": ["AWS-Trusted-Advisor"],
    "compute-optimizer": ["AWS-Compute-Optimizer"],
    "well-architected-tool": ["AWS-Well-Architected-Tool"],
    "dms": ["AWS-Database-Migration-Service"],
    "application-migration-service": ["AWS-Application-Migration-Service"],
    # cost
    "savings-plans": ["Savings-Plans"],
    "budgets": ["AWS-Budgets"],
    "cost-explorer": ["AWS-Cost-Explorer"],
    "cost-and-usage-report": ["AWS-Cost-and-Usage-Report"],
    # front matter
    "management-console": ["AWS-Management-Console"],
    "aws-cli": ["AWS-Command-Line-Interface"],
    "well-architected": ["AWS-Well-Architected-Tool"],
    # extras that diagrams need
    "nlb": ["Elastic-Load-Balancing_Network-Load-Balancer"],
    "cloudshell": ["AWS-CloudShell"],
    "session-manager": ["AWS-Systems-Manager_Session-Manager"],
    "app-runner": ["AWS-App-Runner"],
    "cloud-map": ["AWS-Cloud-Map"],
    "app-mesh": ["AWS-App-Mesh"],
    "kinesis": ["Amazon-Kinesis"],
    "ses": ["Amazon-Simple-Email-Service"],
    "appsync": ["AWS-AppSync"],
    "bedrock": ["Amazon-Bedrock"],
    "elastic-disaster-recovery": ["AWS-Elastic-Disaster-Recovery"],
    "verified-access": ["AWS-Verified-Access"],
    "audit-manager": ["AWS-Audit-Manager"],
    "memorydb": ["Amazon-MemoryDB", "Amazon-MemoryDB-for-Redis"],
    "timestream": ["Amazon-Timestream"],
}

RESOURCES = {
    # generic
    "user": ["User"],
    "users": ["Users"],
    "client": ["Client"],
    "server": ["Traditional-server", "Server"],
    "servers": ["Servers"],
    "internet": ["Internet", "Internet-alt1"],
    "corporate-data-center": ["Office-building", "Corporate-data-center"],
    "mobile-client": ["Mobile-client"],
    "generic-database": ["Database", "Generic-database"],
    "generic-application": ["Generic-Application", "Application"],
    "firewall": ["Firewall"],
    "globe": ["Globe"],
    "document": ["Document"],
    "documents": ["Documents"],
    "email": ["Email"],
    "saml-token": ["SAML-token"],
    "ssl-padlock": ["SSL-padlock"],
    "credentials": ["Credentials"],
    "gear": ["Gear"],
    "alert": ["Alert"],
    "logs": ["Logs"],
    "metrics": ["Metrics"],
    "disk": ["Disk"],
    "tape-storage": ["Tape-storage"],
    "source-code": ["Source-Code"],
    "authenticated-user": ["Authenticated-User"],
    "shield-generic": ["Shield"],
    # VPC
    "internet-gateway": ["Amazon-VPC_Internet-Gateway"],
    "nat-gateway": ["Amazon-VPC_NAT-Gateway"],
    "route-table": ["Amazon-Route-53_Route-Table", "Amazon-VPC_Route-Table"],
    "router": ["Amazon-VPC_Router"],
    "endpoint": ["Amazon-VPC_Endpoints"],
    "network-interface": ["Amazon-VPC_Elastic-Network-Interface"],
    "network-acl": ["Amazon-VPC_Network-Access-Control-List"],
    "peering-connection": ["Amazon-VPC_Peering-Connection"],
    "customer-gateway": ["Amazon-VPC_Customer-Gateway"],
    "vpn-gateway": ["Amazon-VPC_VPN-Gateway"],
    "vpn-connection": ["Amazon-VPC_VPN-Connection"],
    "flow-logs": ["Amazon-VPC_Flow-Logs"],
    "carrier-gateway": ["Amazon-VPC_Carrier-Gateway"],
    "transit-gateway-attachment": ["AWS-Transit-Gateway_Attachment"],
    "direct-connect-gateway": ["AWS-Direct-Connect_Gateway"],
    # S3
    "bucket": ["Amazon-Simple-Storage-Service_Bucket"],
    "bucket-with-objects": ["Amazon-Simple-Storage-Service_Bucket-With-Objects"],
    "object": ["Amazon-Simple-Storage-Service_Object"],
    "s3-standard": ["Amazon-Simple-Storage-Service_S3-Standard"],
    "s3-standard-ia": ["Amazon-Simple-Storage-Service_S3-Standard-IA"],
    "s3-one-zone-ia": ["Amazon-Simple-Storage-Service_S3-One-Zone-IA"],
    "s3-intelligent-tiering": ["Amazon-Simple-Storage-Service_S3-Intelligent-Tiering"],
    "s3-glacier-instant": ["Amazon-Simple-Storage-Service_S3-Glacier-Instant-Retrieval"],
    "s3-glacier-flexible": ["Amazon-Simple-Storage-Service_S3-Glacier-Flexible-Retrieval"],
    "s3-glacier-deep-archive": ["Amazon-Simple-Storage-Service_S3-Glacier-Deep-Archive"],
    "s3-replication": ["Amazon-Simple-Storage-Service_S3-Replication"],
    "s3-object-lock": ["Amazon-Simple-Storage-Service_S3-Object-Lock"],
    "s3-access-points": ["Amazon-Simple-Storage-Service_S3-Multi-Region-Access-Points", "Amazon-Simple-Storage-Service_Access-Points"],
    "vault": ["Amazon-Simple-Storage-Service-Glacier_Vault"],
    # AWS Backup resource icons (added for chapter 24; the service icon is "backup")
    "backup-plan": ["AWS-Backup_Backup-Plan"],
    "backup-vault": ["AWS-Backup_Backup-Vault"],
    "vault-lock": ["AWS-Backup_Vault-Lock"],
    "backup-restore": ["AWS-Backup_Backup-Restore"],
    # EC2 and scaling
    "instance": ["Amazon-EC2_Instance"],
    "instances": ["Amazon-EC2_Instances"],
    "spot-instance": ["Amazon-EC2_Spot-Instance"],
    "ami": ["Amazon-EC2_AMI"],
    "auto-scaling-group": ["Amazon-EC2_Auto-Scaling"],
    "elastic-ip": ["Amazon-EC2_Elastic-IP-Address"],
    "db-on-instance": ["Amazon-EC2_DB-Instance"],
    "volume": ["Amazon-Elastic-Block-Store_Volume"],
    "snapshot": ["Amazon-Elastic-Block-Store_Snapshot"],
    # load balancers
    "alb": ["Elastic-Load-Balancing_Application-Load-Balancer"],
    "nlb-resource": ["Elastic-Load-Balancing_Network-Load-Balancer"],
    "gwlb": ["Elastic-Load-Balancing_Gateway-Load-Balancer"],
    "clb": ["Elastic-Load-Balancing_Classic-Load-Balancer"],
    # Lambda, containers
    "lambda-function": ["AWS-Lambda_Lambda-Function"],
    "container": ["Amazon-Elastic-Container-Service_Container-1"],
    "ecs-task": ["Amazon-Elastic-Container-Service_Task"],
    "ecs-service": ["Amazon-Elastic-Container-Service_Service"],
    "ecr-image": ["Amazon-Elastic-Container-Registry_Image"],
    # messaging
    "queue": ["Amazon-Simple-Queue-Service_Queue"],
    "message": ["Amazon-Simple-Queue-Service_Message"],
    "topic": ["Amazon-Simple-Notification-Service_Topic"],
    "email-notification": ["Amazon-Simple-Notification-Service_Email-Notification"],
    "http-notification": ["Amazon-Simple-Notification-Service_HTTP-Notification"],
    "event-bus": ["Amazon-EventBridge_Custom-Event-Bus", "Amazon-EventBridge_Default-Event-Bus"],
    "event-rule": ["Amazon-EventBridge_Rule"],
    "event": ["Amazon-EventBridge_Event"],
    "scheduler": ["Amazon-EventBridge_Scheduler"],
    # databases
    "table": ["Amazon-DynamoDB_Table"],
    "item": ["Amazon-DynamoDB_Item"],
    "items": ["Amazon-DynamoDB_Items"],
    "global-secondary-index": ["Amazon-DynamoDB_Global-secondary-index"],
    "dynamodb-stream": ["Amazon-DynamoDB_Stream"],
    "db-instance": ["Amazon-Aurora_Amazon-RDS-Instance", "Amazon-RDS_DB-Instance"],
    "db-instance-standby": ["Amazon-Aurora_Amazon-RDS-Instance-Aternate", "Amazon-Aurora_Amazon-RDS-Instance-Alternate"],
    "multi-az": ["Amazon-RDS_Multi-AZ"],
    "multi-az-db-cluster": ["Amazon-RDS_Multi-AZ-DB-Cluster"],
    "aurora-instance": ["Amazon-Aurora-Instance"],
    "cache-node": ["Amazon-ElastiCache_Cache-Node"],
    "redis": ["Amazon-ElastiCache_ElastiCache-for-Redis", "Amazon-ElastiCache_ElastiCache-for-Valkey"],
    "memcached": ["Amazon-ElastiCache_ElastiCache-for-Memcached"],
    # IAM and security
    "role": ["AWS-Identity-Access-Management_Role"],
    "policy": ["AWS-Identity-Access-Management_Permissions"],
    "temporary-credential": ["AWS-Identity-Access-Management_Temporary-Security-Credential"],
    "long-term-credential": ["AWS-Identity-Access-Management_Long-Term-Security-Credential"],
    "mfa-token": ["AWS-Identity-Access-Management_MFA-Token"],
    "add-on": ["AWS-Identity-Access-Management_Add-on"],
    "data-encryption-key": ["AWS-Identity-Access-Management_Data-Encryption-Key"],
    "encrypted-data": ["AWS-Identity-Access-Management_Encrypted-Data"],
    "iam-access-analyzer": ["AWS-Identity-Access-Management_IAM-Access-Analyzer"],
    "iam-roles-anywhere": ["AWS-Identity-Access-Management_IAM-Roles-Anywhere"],
    "key": ["AWS-Identity-Access-Management_Data-Encryption-Key"],
    "external-key-store": ["AWS-Key-Management-Service_External-Key-Store"],
    "certificate-authority": ["AWS-Certificate-Manager_Certificate-Authority"],
    "waf-rule": ["AWS-WAF_Rule"],
    "organizations-account": ["AWS-Organizations_Account"],
    "organizational-unit": ["AWS-Organizations_Organizational-Unit"],
    "management-account": ["AWS-Organizations_Management-Account"],
    # edge and DNS
    "hosted-zone": ["Amazon-Route-53-Hosted-Zone", "Amazon-Route-53_Hosted-Zone"],
    "resolver": ["Amazon-Route-53_Resolver"],
    "edge-location": ["Amazon-CloudFront_Edge-Location"],
    "cloudfront-distribution": ["Amazon-CloudFront_Download-Distribution"],
    "api-endpoint": ["Amazon-API-Gateway_Endpoint"],
    # operations
    "alarm": ["Amazon-CloudWatch_Alarm"],
    "cloudwatch-logs": ["Amazon-CloudWatch_Logs"],
    "cloudwatch-rule": ["Amazon-CloudWatch_Rule"],
    "stack": ["AWS-CloudFormation_Stack"],
    "template": ["AWS-CloudFormation_Template"],
    "change-set": ["AWS-CloudFormation_Change-Set"],
    "file-system": ["Amazon-Elastic-File-System_File-System", "Amazon-EFS_File-System"],
    "file-gateway": ["AWS-Storage-Gateway_File-Gateway", "AWS-Storage-Gateway_Amazon-S3-File-Gateway"],
    "volume-gateway": ["AWS-Storage-Gateway_Volume-Gateway"],
    "tape-gateway": ["AWS-Storage-Gateway_Tape-Gateway"],
    "datasync-agent": ["AWS-DataSync_Agent"],
    "cloudtrail-lake": ["AWS-CloudTrail_CloudTrail-Lake"],
}


def _norm(stem: str) -> str:
    return re.sub(r"[\s_\-]+", "", stem).lower()


_RE_SUFFIX = re.compile(r"_(?:16|32|48|64)(?:_(Light|Dark))?$")


def scan_package(root: Path) -> dict:
    """Index every 48 px SVG of the unpacked package.

    Returns {"service": {norm: path}, "resource": {norm: path}, "resource_dark": {norm: path}}.
    """
    index = {"service": {}, "resource": {}, "resource_dark": {}, "group": {}}
    for path in sorted(root.rglob("*.svg")):
        parts = "/".join(path.relative_to(root).parts)
        if "__MACOSX" in parts or path.name.startswith("._"):
            continue
        stem = path.stem
        match = _RE_SUFFIX.search(stem)
        variant = match.group(1) if match else None
        size_ok = "_48" in stem
        base = _RE_SUFFIX.sub("", stem)
        if base.startswith("Arch_") and size_ok and "Architecture-Service" in parts:
            index["service"].setdefault(_norm(base[5:]), path)
        elif base.startswith("Res_") and size_ok:
            bucket = "resource_dark" if (variant == "Dark" or "_Dark/" in parts or "Dark/" in parts) else "resource"
            index[bucket].setdefault(_norm(base[4:]), path)
        elif "Architecture-Group" in parts:
            index["group"].setdefault(_norm(re.sub(r"_32$", "", base)), path)
    return index


# ------------------------------------------------------------------ cleaning

_RE_PROLOG = re.compile(r"<\?xml[^>]*\?>|<!DOCTYPE[^>]*>", re.I)
_RE_COMMENT = re.compile(r"<!--.*?-->", re.S)
_RE_TITLE = re.compile(r"<(title|desc|metadata)\b[^>]*>.*?</\1>|<(?:title|desc|metadata)\b[^>]*/>", re.S)
_RE_ID = re.compile(r'\s+id="([^"]*)"')
_RE_SVG_OPEN = re.compile(r"<svg\b([^>]*)>", re.S)
_RE_VIEWBOX = re.compile(r'viewBox="([^"]+)"')
_RE_WH = re.compile(r'\b(width|height)="([0-9.]+)(?:px)?"')


def clean_svg(text: str, prefix: str) -> dict:
    """Return {"viewBox": "...", "body": inner markup}. Geometry and colours are not changed."""
    text = _RE_PROLOG.sub("", text)
    text = _RE_COMMENT.sub("", text)
    text = _RE_TITLE.sub("", text)
    open_match = _RE_SVG_OPEN.search(text)
    if not open_match:
        raise ValueError("no <svg> element")
    attrs = open_match.group(1)
    vb = _RE_VIEWBOX.search(attrs)
    if vb:
        view_box = " ".join(vb.group(1).split())
    else:
        dims = dict(_RE_WH.findall(attrs))
        view_box = f"0 0 {dims.get('width', '48')} {dims.get('height', '48')}"
    end = text.rfind("</svg>")
    body = text[open_match.end():end if end >= 0 else len(text)]
    referenced = set(re.findall(r"url\(#([^)]+)\)", body)) | set(re.findall(r'href="#([^"]+)"', body))

    def fix_id(match):
        ident = match.group(1)
        if ident in referenced:
            return f' id="{prefix}-{ident}"'
        return ""

    body = _RE_ID.sub(fix_id, body)
    for ident in sorted(referenced, key=len, reverse=True):
        body = body.replace(f"url(#{ident})", f"url(#{prefix}-{ident})")
        body = body.replace(f'href="#{ident}"', f'href="#{prefix}-{ident}"')
    body = re.sub(r">\s+<", "><", body).strip()
    body = re.sub(r"\s{2,}", " ", body)
    return {"viewBox": view_box, "body": body}


# ------------------------------------------------------------------ download

def _get(url: str, host: str, binary: bool = False, timeout: int = 120):
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or parsed.hostname != host:
        raise PermissionError(f"refused: {url} is not https://{host}/")
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        final = urllib.parse.urlparse(response.geturl())
        if final.hostname != host:
            raise PermissionError(f"refused: redirected to {final.hostname}")
        data = response.read()
    return data if binary else data.decode("utf-8", "replace")


def find_zip_url(page_html: str):
    """The newest icon package link on the AWS Architecture Icons page."""
    text = page_html.replace("\\u002F", "/").replace("\\/", "/").replace("&#x2F;", "/")
    links = re.findall(r"https://d1\.awsstatic\.com/[A-Za-z0-9_\-./%]+?\.zip", text)
    links = [u for u in dict.fromkeys(links) if re.search(r"icon|asset", u, re.I)]
    packages = [u for u in links if re.search(r"Asset-Package|Icon-Package|icons?[_-]", u, re.I)
                and not re.search(r"toolkit|pptx|sketch|figma|drawio|lucid", u, re.I)]
    return (packages or links or [None])[0], links


def download(zip_url: str = None) -> dict:
    """Fetch the package zip (once) and unpack it under TMP/aws-icons."""
    target = common.ensure_dir(unpack_dir())
    meta_path = target / "package.json"
    meta = common.read_json(meta_path)
    if meta and (target / "unpacked").is_dir() and (zip_url is None or meta.get("zip_url") == zip_url):
        return meta
    usage = ""
    if zip_url is None:
        page = _get(ICONS_PAGE, "aws.amazon.com")
        zip_url, _ = find_zip_url(page)
        if not zip_url:
            raise RuntimeError("no icon package link found on " + ICONS_PAGE)
        usage = find_usage_statement(page)
    data = _get(zip_url, DOWNLOAD_HOST, binary=True, timeout=300)
    zip_path = target / "package.zip"
    zip_path.write_bytes(data)
    out = target / "unpacked"
    with zipfile.ZipFile(zip_path) as archive:
        for member in archive.infolist():
            dest = (out / member.filename).resolve()
            if not str(dest).startswith(str(out.resolve())):
                raise PermissionError(f"refused: unsafe path in zip: {member.filename}")
        archive.extractall(out)
    meta = {"zip_url": zip_url, "sha256": common.sha256_bytes(data), "bytes": len(data),
            "release": release_from_url(zip_url), "usage_statement": usage,
            "downloaded": common.today()}
    common.write_json(meta_path, meta)
    return meta


def release_from_url(url: str) -> str:
    name = url.rsplit("/", 1)[-1]
    match = re.search(r"(\d{8})", name)
    if match:
        digits = match.group(1)
        # AWS names packages MMDDYYYY
        if int(digits[4:]) > 2000:
            return f"{digits[4:]}-{digits[:2]}-{digits[2:4]}"
        return f"{digits[:4]}-{digits[4:6]}-{digits[6:]}"
    return name


def find_usage_statement(page_html: str) -> str:
    """The sentence on the icons page that states how customers and partners may use the icons."""
    text = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", page_html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    import html as _html
    text = re.sub(r"\s+", " ", _html.unescape(text))
    for sentence in re.split(r"(?<=[.!?])\s+", text):
        low = sentence.lower()
        if "customers and partners" in low and ("permitted" in low or "allow" in low) and len(sentence) < 600:
            return sentence.strip()
    return ""


# ------------------------------------------------------------------ build icons.json

def build(root: Path, meta: dict) -> dict:
    index = scan_package(root)
    icons = {}
    missing = []

    def add(name, candidates, kind):
        pools = [index["service"], index["resource"]] if kind == "service" else [index["resource"], index["service"]]
        for cand in candidates:
            key = _norm(cand)
            for pool in pools:
                path = pool.get(key)
                if path is None:
                    continue
                entry = clean_svg(path.read_text(encoding="utf-8"), "ic-" + name)
                entry["kind"] = "service" if pool is index["service"] else "resource"
                entry["file"] = "/".join(path.relative_to(root).parts)
                dark = index["resource_dark"].get(key) if pool is index["resource"] else None
                if dark is not None:
                    entry["dark"] = clean_svg(dark.read_text(encoding="utf-8"), "ic-" + name + "-d")["body"]
                icons[name] = entry
                return
        missing.append(name)

    for name in sorted(SERVICES):
        add(name, SERVICES[name], "service")
    for name in sorted(RESOURCES):
        add(name, RESOURCES[name], "resource")
    result = {
        "meta": {"package": meta.get("zip_url", ""), "release": meta.get("release", ""),
                 "sha256": meta.get("sha256", ""), "count": len(icons), "missing": sorted(missing)},
        "icons": {k: icons[k] for k in sorted(icons)},
    }
    return result


def load() -> dict:
    """The icon manifest. A sandbox book (--book-dir) without its own icons.json reads the real one,
    as schemas.load() does for the schema folder; `diagram icons` still writes only to common.BOOK."""
    path = icons_json_path()
    if not path.exists():
        path = common.REAL_BOOK / "diagrams" / "icons.json"
    data = common.read_json(path, {"meta": {}, "icons": {}})
    return data.get("icons", {})


def sprite(icons: dict, names=None) -> str:
    """One <svg> of <symbol id="ic-NAME"> (and ic-NAME-dark) for the web shell."""
    out = ['<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" style="position:absolute" aria-hidden="true">']
    for name in sorted(names if names is not None else icons):
        entry = icons.get(name)
        if not entry:
            continue
        out.append(f'<symbol id="ic-{name}" viewBox="{entry["viewBox"]}">{entry["body"]}</symbol>')
        if entry.get("dark"):
            out.append(f'<symbol id="ic-{name}-dark" viewBox="{entry["viewBox"]}">{entry["dark"]}</symbol>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def write_notice(meta: dict, result: dict) -> None:
    usage = meta.get("usage_statement") or "(not captured automatically; see the page linked above)"
    lines = [
        "# AWS Architecture Icons: notice",
        "",
        "The diagrams in this book use the official AWS Architecture Icons, unmodified.",
        "",
        f"- Source page: <{ICONS_PAGE}>",
        f"- Package: <{meta.get('zip_url', '')}>",
        f"- Package release: {meta.get('release', '')}",
        f"- Downloaded: {meta.get('downloaded', '')}",
        f"- SHA-256 of the zip: `{meta.get('sha256', '')}`",
        f"- Icons extracted into `icons.json`: {result['meta']['count']}",
        "",
        "## AWS usage statement",
        "",
        "Quoted from the source page on the download date:",
        "",
        f"> {usage}",
        "",
        "## What the build does to the files",
        "",
        "Each icon is the 48 px SVG from the package. The build removes the XML prolog, comments, "
        "`<title>` and `<desc>`, and unreferenced `id` attributes so that many icons can share one page. "
        "Shapes, colours and proportions are not changed. Icons are drawn at one size.",
        "",
        "## Names not found in this release",
        "",
        (", ".join(f"`{n}`" for n in result["meta"]["missing"]) or "None.") ,
        "",
    ]
    path = notice_path()
    common.ensure_dir(path.parent)
    path.write_text("\n".join(lines), encoding="utf-8")
