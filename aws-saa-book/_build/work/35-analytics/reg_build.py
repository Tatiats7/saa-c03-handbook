"""register-35: build the amend patches for chapter 35 (read-only on the canon).

Reads reg-decisions.json, writes reg-patches/<id>.json and reg-build-report.json.
Each patch is checked with facts.mech_check before it is written, so the apply step should not be refused.
Changes per live fact (one patch per fact):
  - merge: a keeper takes the displays of the facts it supersedes (when its own quotes hold them),
    the union of bullets and the higher exam relevance (and the change items of glue-job-run-queuing-behavior);
  - displays: a number-free display is a verbatim phrase of a quote with at most 8 words (RULINGS 2026-10-11);
    long auto-slug keys of the faq lens become short keys;
  - qualifiers.scope: filled where empty, from the service and the id;
  - manual overrides from reg-decisions.json.
"""
import copy, json, os, re, sys

REPO = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans"
ROOT = REPO + "/aws-saa-book"
W = ROOT + "/_build/work/35-analytics/"
sys.path.insert(0, ROOT + "/tools")
from saalib import facts as F  # noqa: E402
from saalib.common import normalize_text  # noqa: E402
from saalib import lint as L  # noqa: E402

SERVICES = ["athena", "glue", "lake-formation", "emr", "opensearch", "quick", "data-exchange"]
D = json.load(open(W + "reg-decisions.json"))
canon = {}
for s in SERVICES:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        if line.strip():
            f = json.loads(line)
            if f["status"] not in ("rejected", "superseded") and str(f.get("home_chapter")) == "35":
                canon[f["id"]] = f

drops = {d for d, k, _ in D["supersede"]}
for d, k, _ in D["supersede"]:
    assert d in canon and k in canon and k not in drops, (d, k)

REL = {"core": 3, "extended": 2, "reference": 1}
EDGE = set("a an the and or of to in on for with by that which from as at is are be your their its so but if when than then into such like also was were has have".split())
CRIT = set("not no never only cannot without must all every always default none nor unless except".split())


def crit(w):
    w = w.lower().strip(".,;:()\"'")
    return w in CRIT or w.endswith("n't") or w.endswith("n’t")


def clean_edges(ws):
    ws = list(ws)
    while ws and ws[0].lower().strip(",;:") in EDGE and not crit(ws[0]):
        ws = ws[1:]
    while ws and (ws[-1].lower().strip(",;:.") in EDGE and not crit(ws[-1])):
        ws = ws[:-1]
    if ws:
        ws[-1] = ws[-1].rstrip(",;:")
    if ws:
        ws[0] = ws[0].lstrip(",;:")
    return ws


def balanced(ws):
    t = " ".join(ws)
    return t.count("(") == t.count(")") and t.count("\"") % 2 == 0


def shorten(display, maxw=8):
    ws = display.split()
    if len(ws) <= maxw:
        return display
    ncrit = [i for i, w in enumerate(ws) if crit(w)]
    best = None
    for L_ in range(maxw, 2, -1):
        for s in range(0, len(ws) - L_ + 1):
            cand = clean_edges(ws[s:s + L_])
            if len(cand) < 3 or not balanced(cand):
                continue
            # positions covered
            e = s + L_
            covered = sum(1 for i in ncrit if s <= i < e)
            score = covered * 4 + len(cand) + (1 if s == 0 else 0)
            if e == len(ws):
                score += 3
            elif re.search(r"[,;:]$", ws[e - 1]):
                score += 2
            if s > 0 and re.search(r"[,;:]$", ws[s - 1]):
                score += 1
            if crit(cand[-1]) and e < len(ws):
                score -= 4
            if re.search(r"[,;:]$", cand[0]) or (s > 0 and cand[0] == ws[s] and re.search(r"[,;:]$", ws[s])):
                score -= 2
            if best is None or score > best[0]:
                best = (score, cand)
    if best is None:
        return " ".join(clean_edges(ws[:maxw]))
    return " ".join(best[1])


def held(text, display):
    return L.holds_display(normalize_text(text), normalize_text(display)) or \
        normalize_text(display).lower() in normalize_text(text).lower()


def in_quotes(f, display):
    return any(held(e.get("quote") or "", display) or held(e.get("table_header") or "", display) for e in f["evidence"])


def short_key(display, used):
    base = re.sub(r"[^a-z0-9]+", "-", display.lower()).strip("-")
    parts = [p for p in base.split("-") if p and p not in EDGE]
    k = "-".join(parts[:2])[:20] or "v"
    out, n = k, 2
    while out in used:
        out = "%s-%d" % (k, n)
        n += 1
    used.add(out)
    return out


def scope_for(f):
    i = f["id"]
    s = f["service"]
    rules = [
        ("athena-spark", "Amazon Athena for Apache Spark"), ("athena-faq-athena-spark", "Amazon Athena for Apache Spark"),
        ("athena-capacity", "Athena capacity reservations"), ("athena-workgroups", "Athena workgroups"),
        ("athena-federated", "Athena Federated Query"), ("athena-faq-federated", "Athena Federated Query"),
        ("athena-partition-projection", "Athena partition projection"), ("athena-ctas", "Athena CTAS and INSERT INTO queries"),
        ("athena-unload", "the Athena UNLOAD statement"), ("athena-iceberg", "Apache Iceberg tables in Athena"),
        ("athena-acid", "Apache Iceberg tables in Athena"), ("athena-encryption", "encryption of Athena table data and query results"),
        ("athena-results", "Athena query results"), ("athena-managed-results", "Athena managed query results"),
        ("athena-reuse", "Athena query result reuse"), ("athena-lake-formation", "Athena queries on Lake Formation registered data"),
        ("athena-tune", "Athena query performance tuning"), ("athena-faq-price", "Athena pricing"), ("athena-faq-capacity", "Athena capacity reservations"),
        ("athena-faq-both", "Athena pricing"), ("athena-faq-less", "Athena per query pricing"), ("athena-faq-optimize", "Athena capacity reservations"),
        ("athena-faq-emr", "Amazon EMR compared with Athena"), ("athena-faq-use-emr", "Amazon EMR compared with Athena"),
        ("athena-faq-redshift", "Amazon Redshift compared with Athena"), ("athena-decision-redshift", "Amazon Redshift compared with Athena"),
        ("athena-cross-account", "cross-account access to Amazon S3 data from Athena"), ("athena-vpc", "Athena access from a VPC"),
        ("athena-interface-vpc", "Athena access from a VPC"), ("athena-cloudtrail", "Athena queries on CloudTrail logs"),
        ("athena-", "Amazon Athena"),
        ("emr-serverless", "Amazon EMR Serverless"), ("emr-faq-serverless", "Amazon EMR Serverless"), ("emr-on-eks", "Amazon EMR on EKS"),
        ("emr-faq-on-eks", "Amazon EMR on EKS"), ("emr-managed-scaling", "Amazon EMR managed scaling"), ("emr-auto-termination", "Amazon EMR auto-termination policies"),
        ("emr-spot", "Spot Instances in Amazon EMR on EC2 clusters"), ("emr-fleet", "Amazon EMR instance fleets"), ("emr-bpa", "Amazon EMR block public access"),
        ("emr-lake-formation", "Amazon EMR with Lake Formation"), ("emr-security", "Amazon EMR security configurations and security groups"),
        ("emr-case", "AWS customer case study"), ("emr-decision", "Amazon EMR in the AWS analytics decision guide"),
        ("emr-whitepaper", "Amazon EMR"), ("emr-lens", "Amazon EMR"), ("emr-faq", "Amazon EMR on EC2 clusters"), ("emr-", "Amazon EMR on EC2 clusters"),
        ("glue-faq-flex", "AWS Glue Flex execution class"), ("glue-flex", "AWS Glue Flex execution class"), ("glue-crawler", "AWS Glue crawlers"),
        ("glue-faq-crawler", "AWS Glue crawlers"), ("glue-job-bookmark", "AWS Glue job bookmarks"), ("glue-streaming", "AWS Glue streaming ETL jobs"),
        ("glue-faq-streaming", "AWS Glue streaming ETL jobs"), ("glue-data-catalog", "AWS Glue Data Catalog"), ("glue-catalog", "AWS Glue Data Catalog"),
        ("glue-faq-data-catalog", "AWS Glue Data Catalog"), ("glue-studio", "AWS Glue Studio"), ("glue-faq-studio", "AWS Glue Studio"),
        ("glue-workflow", "AWS Glue workflows"), ("glue-trigger", "AWS Glue triggers"), ("glue-data-quality", "AWS Glue Data Quality"),
        ("glue-vpc", "AWS Glue connections to resources in a VPC"), ("glue-encryption", "AWS Glue encryption"), ("glue-job", "AWS Glue jobs"),
        ("glue-faq-vs", "AWS Glue compared with other AWS services"), ("glue-pii", "AWS Glue sensitive data detection"),
        ("glue-sensitive", "AWS Glue sensitive data detection"), ("glue-relationalize", "the AWS Glue Relationalize transform"),
        ("glue-partition-index", "AWS Glue partition indexes"), ("glue-worker", "AWS Glue worker types"), ("glue-decision", "AWS Glue in the AWS analytics decision guide"),
        ("glue-", "AWS Glue"),
        ("lake-formation-lf-tag", "Lake Formation tag-based access control (LF-Tags)"), ("lake-formation-lf-tbac", "Lake Formation tag-based access control (LF-Tags)"),
        ("lake-formation-faq-lf-tbac", "Lake Formation tag-based access control (LF-Tags)"),
        ("lake-formation-data-filter", "Lake Formation data filters"), ("lake-formation-cell", "Lake Formation data filters"),
        ("lake-formation-row", "Lake Formation data filters"), ("lake-formation-column", "Lake Formation data filters"),
        ("lake-formation-iamallowed", "the IAMAllowedPrincipals group in Lake Formation"), ("lake-formation-case", "AWS customer case study"),
        ("lake-formation-decision", "Lake Formation in the AWS analytics decision guide"), ("lake-formation-", "AWS Lake Formation"),
        ("opensearch-serverless", "Amazon OpenSearch Serverless"), ("opensearch-ingestion", "Amazon OpenSearch Ingestion"),
        ("opensearch-ultrawarm", "UltraWarm storage of OpenSearch Service domains"), ("opensearch-cold", "cold storage of OpenSearch Service domains"),
        ("opensearch-multiaz", "OpenSearch Service domains with Multi-AZ with Standby"), ("opensearch-faq-multi-az", "OpenSearch Service domains with Multi-AZ with Standby"),
        ("opensearch-dedicated-master", "dedicated master nodes of OpenSearch Service domains"), ("opensearch-faq-dedicated", "dedicated master nodes of OpenSearch Service domains"),
        ("opensearch-encryption", "encryption of OpenSearch Service domains"), ("opensearch-node-to-node", "encryption of OpenSearch Service domains"),
        ("opensearch-vpc", "OpenSearch Service domains in a VPC"), ("opensearch-faq-vpc", "OpenSearch Service domains in a VPC"),
        ("opensearch-case", "AWS customer case study"), ("opensearch-", "Amazon OpenSearch Service"),
        ("quick-spice", "SPICE in Amazon Quick Sight"), ("quick-rls", "row-level security in Amazon Quick Sight"), ("quick-embedding", "embedded Amazon Quick Sight dashboards"),
        ("quick-case", "AWS customer case study"), ("quick-", "Amazon Quick"),
        ("data-exchange-open-data", "open data on AWS through AWS Data Exchange"), ("data-exchange-", "AWS Data Exchange"),
    ]
    for p, sc in rules:
        if i.startswith(p):
            base = sc
            break
    else:
        base = s
    if "-whitepaper-" in i or "-wp-" in i:
        base += ", as stated in an AWS whitepaper"
    elif "-lens-" in i:
        base += ", as stated in the AWS Well-Architected Analytics Lens"
    elif "-decision-guide-" in i:
        base += ", as stated in the AWS analytics decision guide"
    return base


report = {"patches": [], "supersede": [[d, k, r] for d, k, r in D["supersede"]], "conflicts_both": D["conflicts_both"],
          "refused": [], "display_changes": [], "scope_filled": 0, "keys_renamed": 0}
os.makedirs(W + "reg-patches", exist_ok=True)
ctx = F._Ctx()

# merge info
merge_into = {}
for d, k, _ in D["supersede"]:
    merge_into.setdefault(k, []).append(d)

for fid in sorted(canon):
    if fid in drops:
        continue
    f = canon[fid]
    new = copy.deepcopy(f)
    man = D["manual"].get(fid, {})
    # merges
    for d in merge_into.get(fid, []):
        g = canon[d]
        have = {normalize_text(v["display"]).lower() for v in new["values"]}
        for v in g["values"]:
            if normalize_text(v["display"]).lower() in have:
                continue
            if in_quotes(new, v["display"]) or held(new["claim"], v["display"]):
                vv = {"key": v["key"], "display": v["display"]}
                if v.get("spoken"):
                    vv["spoken"] = v["spoken"]
                new["values"].append(vv)
                have.add(normalize_text(v["display"]).lower())
        new["bullets"] = sorted(set(new.get("bullets") or []) | set(g.get("bullets") or []))
        if REL.get(g.get("exam_relevance"), 0) > REL.get(new.get("exam_relevance"), 0):
            new["exam_relevance"] = g["exam_relevance"]
        if d == "glue-job-run-queuing-behavior":
            new["change_items"] = sorted(set(new.get("change_items") or []) | set(g.get("change_items") or []))
            new["volatility"] = g["volatility"]
    if fid in D.get("bullets_add", {}):
        new["bullets"] = sorted(set(new.get("bullets") or []) | set(D["bullets_add"][fid]))
    for k in ("claim", "values", "hard"):
        if k in man:
            new[k] = copy.deepcopy(man[k])
    if man.get("drop_keys"):
        new["values"] = [v for v in new["values"] if v["key"] not in man["drop_keys"]]
    # displays
    used = set()
    vals = []
    seen = set()
    for v in new["values"]:
        v = dict(v)
        dsp = v["display"]
        ov = D.get("display_override", {}).get(fid, {})
        if dsp in ov:
            if ov[dsp] is None:
                report["display_changes"].append([fid, dsp, None])
                continue
            dsp = v["display"] = ov[dsp]
        if not re.search(r"\d", dsp):
            if not in_quotes(new, dsp):
                # number-free display that no quote holds: drop it when another display remains
                report["display_changes"].append([fid, dsp, None])
                continue
            sd = shorten(dsp)
            if sd != dsp:
                report["display_changes"].append([fid, dsp, sd])
                v["display"] = sd
        nk = normalize_text(v["display"]).lower()
        if nk in seen:
            continue
        seen.add(nk)
        if len(v["key"]) > 14 and v["key"].count("-") >= 2:
            v["key"] = short_key(v["display"], used)
            report["keys_renamed"] += 1
        elif v["key"] in used:
            v["key"] = short_key(v["display"], used)
        else:
            used.add(v["key"])
        vals.append(v)
    if not vals:
        vals = copy.deepcopy(f["values"])
        report["refused"].append({"id": fid, "why": "no display left; kept the old values"})
    new["values"] = vals
    # scope
    q = dict(new.get("qualifiers") or {})
    if not (q.get("scope") or "").strip():
        q["scope"] = scope_for(new)
        report["scope_filled"] += 1
        if fid.startswith("emr-faq-") and "master" in new["claim"].lower() and not (q.get("condition") or "").strip():
            q["condition"] = "The EMR FAQ says master node; the current EMR documentation says primary node."
    q.setdefault("default_or_max", "")
    q.setdefault("adjustable", False)
    q.setdefault("condition", "")
    new["qualifiers"] = q
    patch = {}
    for k in ("claim", "values", "qualifiers", "bullets", "exam_relevance", "change_items", "volatility", "hard"):
        if new.get(k) != f.get(k):
            patch[k] = new[k]
    if not patch:
        continue
    findings = F.mech_check(new, ctx)
    if findings:
        report["refused"].append({"id": fid, "errors": findings, "patch": patch})
        continue
    json.dump(patch, open(W + "reg-patches/%s.json" % fid, "w"), ensure_ascii=False, indent=1)
    report["patches"].append(fid)

json.dump(report, open(W + "reg-build-report.json", "w"), ensure_ascii=False, indent=1)
print("patches", len(report["patches"]), "refused", len(report["refused"]), "display changes", len(report["display_changes"]),
      "scope filled", report["scope_filled"], "keys renamed", report["keys_renamed"], "supersede", len(report["supersede"]))
