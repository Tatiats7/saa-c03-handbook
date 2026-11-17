from lib import *
import json
def A(fn,*a,**k):
    f=F(*a,[],**k); del f['evidence']
    json.dump([f],open('../'+fn,'w'),indent=1,ensure_ascii=False)
X="x-ray"
A("adopt-x1.json","x-ray-sdk-daemon-end-of-support-2027-02-25","restriction",
 "On February 25th, 2027 AWS X-Ray will discontinue support for the AWS X-Ray SDKs and Daemon; AWS recommends migrating to OpenTelemetry. The X-Ray service itself is not retired.",
 "When does AWS end support for the X-Ray SDKs and the X-Ray daemon?",
 [("date","February 25th, 2027")],"X-Ray SDKs and Daemon","",False,"",
 service=X,vol="frequently-changing",rel="core",bullets=["2.2.K12"],tier0=True,ci=[chg('xray/latest/devguide/document-history',13)],
 note="The support timeline page lists only the maintenance phase from February 25th, 2026; the end-of-support date comes from the document history notice. Older practice questions still say 'install the X-Ray daemon / SDK'.")
A("adopt-x2.json","x-ray-change-sdk-daemon-end-of-support-notice-2025-08","change",
 "The X-Ray document history added an end-of-support notice for the AWS X-Ray SDKs and Daemon on August 22, 2025 (end of support February 25th, 2027).",
 "When did AWS announce the end of support of the X-Ray SDKs and Daemon?",
 [("notice","August 22, 2025"),("end","February 25th, 2027")],"","",False,"",
 service=X,vol="frequently-changing",rel="core",bullets=["2.2.K12"],tier=3,ci=[chg('xray/latest/devguide/document-history',13)],
 note="Current truth: x-ray-sdk-daemon-end-of-support-2027-02-25.")
A("adopt-x3.json","x-ray-change-sdk-daemon-maintenance-timeline-2025-11","change",
 "The X-Ray document history row dated November 26, 2025 updated the SDKs and Daemon support timeline: on February 25th, 2026 they enter maintenance mode, limited to security fixes.",
 "When was the X-Ray SDK and daemon maintenance mode announced and when does it start?",
 [("updated","November 26, 2025"),("start","February 25th, 2026")],"","",False,"",
 service=X,vol="frequently-changing",rel="core",bullets=["2.2.K12"],tier=3,ci=[chg('xray/latest/devguide/document-history',12)],
 note="Current truth: x-ray-sdk-daemon-maintenance-mode-security-fixes-only.")
A("adopt-x4.json","x-ray-change-otlp-endpoint-2024-11","change",
 "AWS X-Ray started supporting the OpenTelemetry Protocol (OTLP) endpoint on November 21, 2024.",
 "When did X-Ray add the OpenTelemetry Protocol endpoint?",
 [("date","November 21, 2024")],"","",False,"",
 service=X,vol="frequently-changing",rel="extended",bullets=["2.2.K12"],tier=3,ci=[chg('xray/latest/devguide/document-history',16)])
