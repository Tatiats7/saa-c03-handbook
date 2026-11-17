"""adjudicate-31: FIFO throughput patches whose quotes are exact substrings of quotas-messages line 31."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
line = open(os.path.join(HERE, "adj-quotas-messages.txt")).read().split("\n")[30]
if line.startswith("  - "):
    pass

def cut(start, end_marker):
    i = line.find(start)
    assert i >= 0, start
    j = line.find(end_marker, i)
    assert j >= 0, end_marker
    return line[i:j + len(end_marker)]

SRC = {"source_id": "docs/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages",
       "url": "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html",
       "table_header": None}
def ev(q):
    d = dict(SRC); d["quote"] = q; return d

q3000 = cut("To enable high-throughput mode, see", "each with a batch of 10 messages.")
q70k = cut("For high throughput mode, these API request limits", "Up to 70,000 transactions per second (TPS).")
q2400 = cut("Up to 4,500 TPS.", "Default throughput of 2,400 TPS.")
q700k = cut("For more information, see [Increasing", "(10x the non-batch limit of 70,000 TPS).")
for name, q in [("3000", q3000), ("70k", q70k), ("2400", q2400), ("700k", q700k)]:
    print(name, len(q.split()), repr(q[:90]))

P = {
 "sqs-fifo-3000-is-300-calls-of-10": {
   "claim": "If you use batching, non-high throughput FIFO queues support up to 3,000 messages per second, per API action; the 3,000 messages per second represent 300 API calls, each with a batch of 10 messages.",
   "evidence": [ev(q3000)]},
 "sqs-fifo-ht-top-regions-70000-tps": {
   "claim": "For SQS FIFO queues in high throughput mode, with non-batched API calls, US East (N. Virginia), US West (Oregon) and Europe (Ireland) support up to 70,000 transactions per second (TPS).",
   "evidence": [ev(q70k)]},
 "sqs-fifo-ht-other-regions-2400-tps": {
   "claim": "For SQS FIFO queues in high throughput mode, with non-batched API calls, all other AWS Regions have a default throughput of 2,400 TPS.",
   "evidence": [ev(q70k), ev(q2400)]},
 "sqs-fifo-ht-top-regions-batched-700000": {
   "claim": "For SQS FIFO queues in high throughput mode, with batched API calls, US East (N. Virginia), US West (Oregon) and Europe (Ireland) support up to 700,000 messages per second, which is 10x the non-batch limit of 70,000 TPS.",
   "evidence": [ev(q70k), ev(q700k)]},
}
for fid, p in P.items():
    with open(os.path.join(HERE, "adj-patches", fid + ".json"), "w") as fh:
        json.dump(p, fh, indent=1, ensure_ascii=False)
print("written", len(P))
