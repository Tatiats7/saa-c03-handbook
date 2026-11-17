from lib import *
import json
def A(fn,*a,**k):
    f=F(*a,[],**k)
    del f['evidence']
    json.dump([f],open('../'+fn,'w'),indent=1,ensure_ascii=False)
Q="Q"
# CloudTrail quota rows
A("adopt-ct1.json","cloudtrail-quota-trails-per-region","quota",
 "An account can have 5 trails per Region, and this quota cannot be increased.",
 "How many trails can you create per Region, and can the quota be raised?",
 [("max","5")],"per account, per Region","default",False,"Row comment: the maximum number of trails per AWS Region; this quota cannot be increased.",
 rel="core",bullets=["1.3.S1"],tier0=True,service="cloudtrail",
 note="Matches cloudtrail-faq-five-trails-per-region (FAQ). A trail that applies to all Regions counts as one trail in each Region.")
A("adopt-ct2.json","cloudtrail-quota-event-selectors-per-trail","quota",
 "A trail can have 5 event selectors, and this quota cannot be increased.",
 "How many event selectors can one trail have?",
 [("max","5 per trail")],"per trail","max",False,"",
 rel="extended",bullets=["1.3.S1"],service="cloudtrail")
A("adopt-ct3.json","cloudtrail-quota-advanced-event-selector-conditions-500","quota",
 "If a trail or event data store uses advanced event selectors, a maximum of 500 total values for all conditions in all advanced event selectors is allowed, and this quota cannot be increased.",
 "How many conditions can the advanced event selectors of a trail have in total?",
 [("max","500 conditions across all advanced event selectors")],"per trail or event data store","max",False,"",
 rel="extended",bullets=["1.3.S1"],service="cloudtrail")
A("adopt-ct4.json","cloudtrail-quota-log-file-size-50-mb-before-compression","quota",
 "CloudTrail sends management, data and network activity events to Amazon S3 in compressed gzip files, and the maximum file size before compression is 50 MB.",
 "What is the maximum size of a CloudTrail log file sent to Amazon S3?",
 [("max","50 MB before compression")],"per log file sent to S3","max",False,"",
 rel="extended",bullets=["1.3.S1"],service="cloudtrail")
A("adopt-ct5.json","cloudtrail-insights-events-viewable-90-days","limit",
 "After you enable CloudTrail Insights on a trail, you can view up to 90 days of Insights events in the console or the AWS CLI.",
 "How long can you view the Insights events of a trail?",
 [("max","up to 90 days of Insights events")],"per trail with Insights enabled","max",False,"",
 rel="extended",bullets=["1.3.S1"],service="cloudtrail")
A("adopt-ct6.json","cloudtrail-pricing-management-events-after-first-copy-per-100000","pricing-dimension",
 "Management events delivered to Amazon S3 by trails are charged per 100,000 events delivered after the first free copy.",
 "How are additional copies of management events delivered by CloudTrail charged?",
 [("unit","per 100,000 management events delivered"),("first","after first free copy")],"trails","","False" == "x" ,"",
 rel="core",bullets=["1.3.S1"],service="cloudtrail",tier=2,vol="frequently-changing")
A("adopt-ct7.json","cloudtrail-pricing-data-events-per-100000","pricing-dimension",
 "Data events delivered to Amazon S3 by trails are charged per 100,000 data events delivered.",
 "How are CloudTrail data events charged?",
 [("unit","per 100,000 data events delivered")],"trails","",False,"",
 rel="core",bullets=["1.3.S1"],service="cloudtrail",tier=2,vol="frequently-changing")
A("adopt-ct8.json","cloudtrail-pricing-network-activity-events-per-100000","pricing-dimension",
 "Network activity events delivered to Amazon S3 by trails are charged per 100,000 network activity events delivered.",
 "How are CloudTrail network activity events charged?",
 [("unit","per 100,000 network activity events delivered")],"trails","",False,"",
 rel="extended",bullets=["1.3.S1"],service="cloudtrail",tier=2,vol="frequently-changing")
A("adopt-ct9.json","cloudtrail-pricing-data-event-aggregation-per-100000-analyzed","pricing-dimension",
 "Data event aggregations are charged per 100,000 data events analyzed for aggregation, in addition to the data events charges.",
 "How is CloudTrail data event aggregation charged?",
 [("unit","per 100,000 data events analyzed for aggregation")],"trails","",False,"",
 rel="reference",bullets=["1.3.K1"],service="cloudtrail",tier=2,vol="frequently-changing")
A("adopt-ct10.json","cloudtrail-pricing-delivery-to-cloudwatch-logs-per-gb","pricing-dimension",
 "Delivering CloudTrail management and data events to a CloudWatch Logs group is charged per GB of events delivered, and CloudWatch Logs ingestion fees apply on top.",
 "How is the delivery of CloudTrail events to CloudWatch Logs charged?",
 [("unit","per GB of events delivered to a CloudWatch Logs group")],"CloudWatch Logs delivery","",False,"",
 rel="extended",bullets=["1.3.S1"],service="cloudtrail",tier=2,vol="frequently-changing")
A("adopt-ct11.json","cloudtrail-pricing-insights-management-events-per-100000","pricing-dimension",
 "CloudTrail Insights for management events is charged per 100,000 events analyzed per insight type.",
 "How are CloudTrail Insights for management events charged?",
 [("unit","per 100,000 events analyzed per insight type")],"Insights","",False,"",
 rel="extended",bullets=["1.3.S1"],service="cloudtrail",tier=2,vol="frequently-changing")
A("adopt-ct12.json","cloudtrail-pricing-insights-data-events-per-100000","pricing-dimension",
 "CloudTrail Insights for data events is charged per 100,000 events analyzed per insight type.",
 "How are CloudTrail Insights for data events charged?",
 [("unit","per 100,000 events analyzed per insight type")],"Insights","",False,"",
 rel="reference",bullets=["1.3.K1"],service="cloudtrail",tier=2,vol="frequently-changing")
A("adopt-ct13.json","cloudtrail-pricing-trails-one-copy-management-events-free","pricing-dimension",
 "You can deliver one copy of your ongoing management events to your Amazon S3 bucket for free by creating trails; limits may apply.",
 "Is delivering management events to S3 with a trail free?",
 [("free","one copy of your ongoing management events"),("s3","to your Amazon Simple Storage Service (S3) bucket for free")],"trails","",False,"",
 rel="core",bullets=["1.3.S1"],service="cloudtrail",tier=2,vol="frequently-changing")
