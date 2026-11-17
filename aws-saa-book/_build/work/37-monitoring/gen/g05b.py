from lib import *
import json
def A(fn,*a,**k):
    f=F(*a,[],**k); del f['evidence']
    json.dump([f],open('../'+fn,'w'),indent=1,ensure_ascii=False)
A("adopt-ct14.json","cloudtrail-quota-event-size-256-kb-cloudwatch-logs-eventbridge","quota",
 "CloudTrail does not send events over 256 KB to CloudWatch Logs or Amazon EventBridge, because each of them allows a maximum event size of 256 KB; from event version 1.05 CloudTrail events themselves have a maximum size of 256 KB. This quota cannot be increased.",
 "What happens to CloudTrail events larger than 256 KB, and which services does the 256 KB limit apply to?",
 [("max","256 KB")],"per CloudTrail event","max",False,"CloudWatch Logs now accepts 1 MB log events, but the CloudTrail delivery rule for CloudWatch Logs and EventBridge on this page still names 256 KB.",
 rel="extended",bullets=["1.3.S1"],service="cloudtrail",
 note="Do not confuse with the CloudWatch Logs event size quota (1,024 KB since 2025-04-02): this row is the CloudTrail delivery rule.")
A("adopt-ct15.json","cloudtrail-quota-data-resources-250-per-trail","quota",
 "The total number of data resources across all event selectors of a trail cannot exceed 250, and this quota cannot be increased.",
 "How many data resources can the event selectors of one trail hold in total?",
 [("max","250 across all event selectors in a trail")],"per trail","max",False,"",
 rel="reference",bullets=["1.3.S1"],service="cloudtrail")
