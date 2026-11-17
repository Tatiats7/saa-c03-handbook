from lib import *
Q="docs/general/latest/gr/xray"
TH="| Name | Default | Adjustable | Description |"
def QR(id,claim,question,disp,scope,row,adj,rel="extended",ev_extra=None,note=None,tier0=False):
    ev=[E(Q,row,TH)]
    return F(id,"quota",claim,question,[("v",disp)],scope,"default" if adj else "max",adj,"Listed for each supported Region.",ev,rel=rel,bullets=["2.2.K12"],service="x-ray",note=note,tier0=tier0)
facts=[]
facts.append(QR("x-ray-quota-custom-sampling-rules-per-region","An account can have 25 custom sampling rules per Region by default, and this quota is adjustable.","How many custom sampling rules can X-Ray have per Region?","25","per account, per Region",
 "| Custom sampling rules per region | Each supported Region: 25 | Yes | The maximum number of custom sampling rules per region. |",True))
facts.append(QR("x-ray-quota-groups-per-account","An account can have 25 X-Ray groups in each supported Region, and this quota is not adjustable.","How many X-Ray groups can an account have?","25","per account, per Region",
 "| Groups in an account | Each supported Region: 25 | No | The maximum number of groups per account. |",False))
facts.append(QR("x-ray-quota-indexed-annotations-per-trace","A single trace can have 50 indexed annotations, and this quota is not adjustable.","How many annotations can be indexed within one X-Ray trace?","50","per trace",
 "| Indexed annotations per trace | Each supported Region: 50 | No | The maximum number of annotations that can be indexed within a single trace. |",False,rel="reference"))
facts.append(QR("x-ray-quota-segment-document-size-64-kb","The maximum size of an X-Ray segment document is 64 Kilobytes, and this quota is not adjustable.","What is the maximum size of an X-Ray segment document?","64 Kilobytes","per segment document",
 "| Segment document size | Each supported Region: 64 Kilobytes | No | The maximum size for segment documents. |",False))
facts.append(QR("x-ray-quota-segments-per-second-2600","You can send up to 2,600 segments per second to X-Ray in each supported Region, and this quota is not adjustable.","How many segments per second can you send to X-Ray?","2,600","per account, per Region",
 "| Segments per second | Each supported Region: 2,600 | No | The maximum number of segments per second you can send to X-Ray. |",False))
facts.append(QR("x-ray-quota-trace-and-service-graph-retention-30-days","X-Ray retains trace and service map data for 30 days, and this quota is not adjustable.","How long does X-Ray keep trace data and the service graph?","30","per account, per Region",
 "| Trace and service graph retention in days | Each supported Region: 30 | No | The number of days to retain trace and service map data. |",False,rel="core",tier0=True))
facts.append(QR("x-ray-quota-trace-data-modification-period-7-days","Recorded trace data can be updated at no additional cost for 7 days, and this quota is not adjustable.","For how many days can recorded X-Ray trace data be updated at no additional cost?","7","per trace",
 "| Trace data modification period in days | Each supported Region: 7 | No | The number of days to update recorded data at no additional cost. |",False,rel="reference"))
f=F("x-ray-quota-trace-document-size-500-kb","quota",
 "The maximum size of an X-Ray trace document has a dynamic upper limit of 500 Kilobytes and a lower limit of 100 Kilobytes, and these quotas are not adjustable.",
 "What are the size limits of an X-Ray trace document?",[("up","500 Kilobytes"),("low","100 Kilobytes")],"per trace document","max",False,"Listed for each supported Region.",
 [E(Q,"| Trace document size (dynamic upper limit) | Each supported Region: 500 Kilobytes | No | The maximum size of a trace document. |",TH),
  E(Q,"| Trace document size (lower limit) | Each supported Region: 100 Kilobytes | No | The maximum size of a trace document. |",TH)],
 rel="reference",bullets=["2.2.K12"],service="x-ray")
facts.append(f)
facts.append(F("x-ray-sampling-default-first-request-each-second-and-5-percent","default",
 "By default the X-Ray SDK records the first request each second and five percent of any additional requests.",
 "What is the default X-Ray sampling behavior?",
 [("pct","five percent of any additional requests"),("first","the first request each second")],"per service instance","default",False,"The reservoir is one request per second; sampling rules can be changed in the X-Ray console without redeploying code.",
 [E("docs/xray/latest/devguide/xray-console-sampling","By default, the SDK records the first request each second, and five percent of any additional requests.")],
 rel="core",bullets=["2.2.K12"],tier0=True,service="x-ray",
 note="Reuse lambda-xray-sampling-fixed for the Lambda side."))
facts.append(F("x-ray-sdk-daemon-maintenance-mode-security-fixes-only","behavior",
 "Since February 25th, 2026 the AWS X-Ray SDKs and Daemon are in maintenance mode: AWS limits releases to security issues only, and they do not get new feature enhancements.",
 "What is the support status of the X-Ray SDKs and the X-Ray daemon?",
 [("date","February 25th, 2026"),("what","address security issues only")],"X-Ray SDKs and Daemon","",False,"",
 [E("docs/xray/latest/devguide/xray-sdk-daemon-timeline","| Maintenance mode | February 25th, 2026 | N/A | AWS will limit X-Ray SDK and Daemon releases to address security issues only. The SDKs/Daemon will not receive new feature enhancements. |","| SDK and daemon phase | Start date | End date | Support provided |")],
 vol="frequently-changing",rel="core",bullets=["2.2.K12"],tier0=True,service="x-ray",
 ci=[chg('xray/latest/devguide/document-history',12)],
 note="The X-Ray service itself continues; only the SDKs and the daemon are affected. Older questions say 'install the X-Ray daemon / SDK'."))
facts.append(F("x-ray-recommend-migrate-to-opentelemetry","behavior",
 "AWS recommends migrating to OpenTelemetry solutions for instrumenting your application and sending traces to AWS X-Ray.",
 "What does AWS recommend instead of the X-Ray SDKs for instrumenting applications?",
 [("rec","migrate to OpenTelemetry solutions"),("target","sending traces to AWS X-Ray")],"X-Ray instrumentation","",False,"",
 [E("docs/xray/latest/devguide/xray-sdk-daemon-timeline","We recommend that you migrate to OpenTelemetry solutions for instrumenting your application and sending traces to AWS X-Ray.")],
 vol="frequently-changing",rel="core",bullets=["2.2.K12"],service="x-ray",ci=[chg('xray/latest/devguide/document-history',12)]))
dump('../facts-numbers-08.json',facts); print(len(facts))
