"""register-33: writes the demand statuses of brief.v0.json from the miners' notes,
replacing superseded fact ids by the kept ids and adding the registrar's own facts.
Run: python3 -I aws-saa-book/_build/work/33-api-gateway/reg_update_brief.py <repo root>"""
import json, sys

ROOT = sys.argv[1]
W = ROOT + "/aws-saa-book/_build/work/33-api-gateway/"
brief = json.load(open(W + "brief.v0.json"))
dec = json.load(open(W + "reg-decisions.json"))
sup = {o: n for o, n, _ in dec["supersede"]}
# rejected at mine (conflict cf kept the numbers-lens duplicate)
sup["api-gateway-private-integration-http-default-https-via-uri"] = "api-gateway-private-integration-default-http"
facts = {}
for line in open(ROOT + "/aws-saa-book/data/facts/api-gateway.jsonl"):
    if line.strip():
        f = json.loads(line)
        facts[f["id"]] = f

notes = {}
for name in ("mine-numbers+changes.json", "mine-behavior+decisions.json", "mine-faq.json"):
    m = json.load(open(W + name))
    for did, rec in m["demand"].items():
        notes.setdefault(did, []).append(rec)

EXTRA = {
 "d023": {"status": "filled", "add": ["api-gateway-usage-plan-quota-period-day-week-month"],
          "note": "register-33: the quota period values (DAY, WEEK, MONTH) were not on the saved guide pages; one more search found none, so the API reference QuotaSettings page was fetched and quoted (api-gateway-usage-plan-quota-period-day-week-month). Usage plans cover REST and WebSocket APIs (api-gateway-usage-plan-rest-or-websocket); HTTP APIs have no API keys or per-client throttling (table facts)."},
 "d037": {"status": "filled", "add": ["lambda-async-service-gets-no-function-response"],
          "note": "register-33: no API Gateway page states the HTTP status the client gets for an asynchronous (Event) invocation; a search of the API Gateway guide for Event and InvocationType found nothing more. Teach only what is grounded: the method does not return the result (api-gateway-lambda-custom-integration-sync-by-default) and Lambda queues the event and returns no function response (verified neighbour lambda-async-service-gets-no-function-response). Do not state a status code."},
 "d048": {"status": "filled", "add": ["api-gateway-vs-alb-caching-none-on-alb", "api-gateway-vs-alb-rate-limiting-usage-plans"],
          "note": "register-33: the ELB page lists no comparison; a corpus search pointed to the AWS Prescriptive Guidance 'Choosing the right AWS service for your microservice endpoints'; its comparison table (fetched) says Caching is None for Application Load Balancer and Lambda function URLs, and that API Gateway adds throttling and quotas with API keys and usage plans while ALB rate limiting is AWS WAF rate-based rules. Size limits: elb-lambda-target-request-body-max, elb-lambda-target-response-json-max, elb-lambda-target-same-account-region (elb namespace, chapter 14). Reuse lambda-trigger-alb-sync. No saved sentence says ALB lacks request validation: do not claim it."},
 "d049": {"status": "contradicted",
          "note": "The facts answer the item, but its hypothesis 'retry with backoff' is contradicted: REL05-BP02 says the consumer can handle the error and retry later (api-gateway-wa-rel05-bp02-client-handles-error-retries-later); it does not mention backoff. Do not attribute backoff to this page."},
 "d033": {"note_add": "The private DNS note stands on the private APIs page (apigateway-private-apis), not on the important-notes page."},
}

changed = 0
for d in brief["demand"]:
    recs = notes.get(d["id"], [])
    ids, ns, st = [], [], []
    for r in recs:
        for i in r.get("facts", []):
            i = sup.get(i, i)
            if i not in ids:
                ids.append(i)
        if r.get("note"):
            ns.append(r["note"])
        st.append(r.get("status", ""))
    ex = EXTRA.get(d["id"], {})
    for i in ex.get("add", []):
        if i not in ids:
            ids.append(i)
    live = []
    for i in ids:
        f = facts.get(i)
        if f is not None and f["status"] in ("rejected", "superseded"):
            raise SystemExit("not live: %s in %s" % (i, d["id"]))
        if i.startswith("api-gateway-") and f is None:
            raise SystemExit("unknown: %s in %s" % (i, d["id"]))
        live.append(i)
    status = ex.get("status") or ("filled" if live and all(s.startswith("filled") or s == "partial" for s in st) else (st[0] if st else "open"))
    if not live and status == "filled":
        status = "not-found"
    note = " ".join(ns)
    if ex.get("note"):
        note = (note + " " + ex["note"]).strip()
    if ex.get("note_add"):
        note = (note + " " + ex["note_add"]).strip()
    d["status"] = status
    d["facts"] = live
    if note:
        d["note"] = note
    changed += 1
brief["registered_by"] = "register-33"
brief["registered"] = "2026-10-14"
json.dump(brief, open(W + "brief.v0.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(changed, Counter(d["status"] for d in brief["demand"]))
for d in brief["demand"]:
    if d["status"] != "filled":
        print(d["id"], d["status"], len(d["facts"]))
