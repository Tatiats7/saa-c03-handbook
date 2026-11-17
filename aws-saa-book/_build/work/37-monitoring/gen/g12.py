from lib import *
import json
def A(fn,*a,**k):
    f=F(*a,[],**k); del f['evidence']
    json.dump([f],open('../'+fn,'w'),indent=1,ensure_ascii=False)
A("adopt-h1.json","health-dashboard-rebranded-from-phd-and-shd","change",
 "The Service Health Dashboard and the AWS Personal Health Dashboard were rebranded to the AWS Health Dashboard (document history row dated February 28, 2022).",
 "What were the Personal Health Dashboard and the Service Health Dashboard renamed to?",
 [("name","rebranded to the AWS Health Dashboard"),("date","February 28, 2022")],"","",False,"",
 service="health-dashboard",rel="extended",bullets=["2.2.S3"],tier=1,
 note="Older questions and some docs still say Personal Health Dashboard (PHD). Write: AWS Health Dashboard (formerly Personal Health Dashboard). The date is before mid-2022, so no Changed recently note is needed beyond the name.")
d=[{"id":"health-dashboard-eventbridge-events-free-all-customers","service":"health-dashboard","home_chapter":"37","kind":"behavior",
 "claim":"All AWS customers can receive AWS Health events through Amazon EventBridge at no additional cost.",
 "question":"Do you need a support plan or pay extra to receive AWS Health events in Amazon EventBridge?",
 "values":[{"key":"free","display":"at no additional cost"},{"key":"all","display":"All AWS customers"}],
 "qualifiers":{"scope":"AWS Health events through EventBridge","default_or_max":"","adjustable":False,"condition":""},
 "evidence":[E("docs/health/latest/ug/what-is-aws-health","All AWS customers can receive AWS Health events through Amazon EventBridge at no additional cost.")],
 "source_tier":1,"hard":True,"tier0":False,"volatility":"stable","changed":None,"exam_relevance":"extended","bullets":["2.2.S3"]}]
json.dump(d,open('../facts-numbers-12.json','w'),indent=1,ensure_ascii=False)
# corrected health free fact
f=F("health-dashboard-free-all-customers","behavior",
 "The AWS Health Dashboard is available for all AWS customers at no additional cost.",
 "Is the AWS Health Dashboard free for every customer?",
 [("free","at no additional cost"),("who","available for all AWS customers")],"all AWS customers","",False,"",
 [E("docs/health/latest/ug/what-is-aws-health","The AWS Health Dashboard is available for all AWS customers at no additional cost.")],
 rel="extended",bullets=["2.2.S3"],service="health-dashboard")
d=json.load(open('../facts-numbers-12.json')); d.append(f); json.dump(d,open('../facts-numbers-12.json','w'),indent=1,ensure_ascii=False)
