from lib import *
HW="docs/awscloudtrail/latest/userguide/how-cloudtrail-works"
LIM="docs/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits"
AV="docs/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change"
PR="www/cloudtrail/pricing"
facts=[]
CT=dict(service="cloudtrail")
facts.append(F("cloudtrail-quotas-none-adjustable","restriction",
 "CloudTrail has no adjustable quotas.",
 "Can you ask for a higher CloudTrail quota?",
 [("none","no adjustable quotas"),("who","CloudTrail has no adjustable quotas")],"CloudTrail resource quotas","",False,"",
 [E(LIM,"CloudTrail has no adjustable quotas.")],rel="core",bullets=["1.3.S1"],tier0=True,**CT))
facts.append(F("cloudtrail-record-past-90-days-needs-trail-or-lake","behavior",
 "For an ongoing record of events in your account beyond the past 90 days of Event history, create a trail or a CloudTrail Lake event data store.",
 "What do you create to keep CloudTrail events longer than the 90 days of Event history?",
 [("days","past 90 days"),("how","create a trail or a CloudTrail Lake event data store")],"account","",False,"Event history covers management events in one AWS Region.",
 [E(HW,"For an ongoing record of events in your AWS account past 90 days, create a trail or a CloudTrail Lake event data store.")],rel="core",bullets=["1.3.S1"],tier0=True,**CT))
facts.append(F("cloudtrail-log-files-published-about-every-5-minutes","behavior",
 "CloudTrail publishes log files multiple times an hour, about every 5 minutes, and they contain API calls from services in the account that support CloudTrail.",
 "How often does CloudTrail publish log files to the S3 bucket of a trail?",
 [("every","about every 5 minutes"),("many","multiple times an hour")],"trails","",False,"Delivery time is not guaranteed.",
 [E(HW,"CloudTrail publishes log files multiple times an hour, about every 5 minutes. These log files contain API calls from services in the account that support CloudTrail.")],rel="core",bullets=["1.3.S1"],**CT))
facts.append(F("cloudtrail-misconfigured-trail-redelivery-30-days","behavior",
 "If a trail is misconfigured, for example the S3 bucket is unreachable, CloudTrail attempts to redeliver the log files for 30 days, and these attempts are subject to standard CloudTrail charges; deleting the trail avoids the charges.",
 "For how long does CloudTrail retry delivery to an unreachable S3 bucket, and are the retries charged?",
 [("days","for 30 days"),("charge","subject to standard CloudTrail charges")],"trails","",False,"",
 [E(HW,"If you misconfigure your trail (for example, the S3 bucket is unreachable), CloudTrail will attempt to redeliver the log files to your S3 bucket for 30 days, and these attempted-to-deliver events will be subject to standard CloudTrail charges.")],rel="reference",bullets=["1.3.S1"],**CT))
facts.append(F("cloudtrail-lake-closed-to-new-customers-2026-05-31","restriction",
 "AWS CloudTrail Lake closed to new customers starting May 31, 2026; sign-up had to happen before that date, and existing customers can continue to use the service as normal.",
 "Can a new customer start using CloudTrail Lake now?",
 [("date","May 31, 2026"),("existing","Existing customers can continue to use the service as normal")],"CloudTrail Lake","",False,"",
 [E(AV,"After careful consideration, we decided to close AWS CloudTrail Lake to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal.")],
 vol="frequently-changing",rel="core",bullets=["1.3.K1"],tier0=True,ci=[chg('cloudtrail-document-history',13)],**CT,
 note="Old practice questions may name CloudTrail Lake as the answer for SQL queries on events; for new designs the page recommends Amazon CloudWatch."))
facts.append(F("cloudtrail-lake-closure-trails-insights-unaffected","behavior",
 "Only CloudTrail Lake is closed to new customers; CloudTrail itself is fully supported, and your trails, Insights and aggregated events are not affected.",
 "Does the CloudTrail Lake closure affect CloudTrail trails and Insights?",
 [("full","AWS CloudTrail continues to be fully supported"),("only","Only AWS CloudTrail Lake is no longer open to new customers")],"CloudTrail","",False,"",
 [E(AV,"AWS CloudTrail continues to be fully supported. Only AWS CloudTrail Lake is no longer open to new customers. Your AWS CloudTrail Trails, Insights and Aggregated Events are not affected.")],
 vol="frequently-changing",rel="core",bullets=["1.3.K1"],ci=[chg('cloudtrail-document-history',13)],**CT))
facts.append(F("cloudtrail-lake-recommended-alternative-cloudwatch","behavior",
 "AWS recommends that CloudTrail Lake customers migrate their Lake log data to Amazon CloudWatch.",
 "What does AWS recommend instead of CloudTrail Lake?",
 [("rec","migrate your AWS CloudTrail Lake logs data to Amazon CloudWatch")],"CloudTrail Lake customers","",False,"",
 [E(AV,"We recommend that you migrate your AWS CloudTrail Lake logs data to Amazon CloudWatch.")],
 vol="frequently-changing",rel="extended",bullets=["1.3.K1"],ci=[chg('cloudtrail-document-history',13)],**CT))
facts.append(F("cloudtrail-lake-account-event-data-stores-not-for-new-accounts","restriction",
 "With only account-level event data stores, CloudTrail Lake does not support ingestion for new accounts added to your organization; an organization event data store covers new member accounts.",
 "After the closure, which Lake event data stores keep covering new accounts in an organization?",
 [("org","Organization event data stores"),("acct","will not support ingestion for new accounts")],"CloudTrail Lake existing customers","",False,"",
 [E(AV,"If your AWS Organization has only account-level event data stores, AWS CloudTrail Lake will continue to support those existing accounts, including expansion to new AWS Regions. However, AWS CloudTrail Lake will not support ingestion for new accounts added to your organization.")],
 vol="frequently-changing",rel="reference",bullets=["1.3.K1"],ci=[chg('cloudtrail-document-history',13)],**CT))
facts.append(F("cloudtrail-lake-one-year-extendable-retention-max-10-years","limit",
 "CloudTrail Lake one-year extendable retention pricing includes the first year of retention with the ingestion cost, and retention can be extended to a maximum of 10 years. This is historical: Lake is closed to new customers.",
 "How long could CloudTrail Lake keep events with one-year extendable retention pricing?",
 [("max","maximum of 10 years"),("incl","The first year of data retention is included")],"CloudTrail Lake event data store","max",False,"Recommended for usage under 25 TB a month.",
 [E(PR,"One-year extendable retention pricing is recommended if your monthly usage is under 25 TB. The first year of data retention is included with the ingestion cost, and you can extend your retention period to a maximum of 10 years.")],
 tier=2,vol="frequently-changing",rel="reference",bullets=["1.3.K1"],ci=[chg('cloudtrail-document-history',13)],**CT))
facts.append(F("cloudtrail-lake-seven-year-retention-not-extendable","limit",
 "CloudTrail Lake seven-year retention pricing includes seven years of retention with the ingestion cost, and the retention period cannot be extended past 7 years. This is historical: Lake is closed to new customers.",
 "How long could CloudTrail Lake keep events with seven-year retention pricing?",
 [("years","Seven years of retention are included"),("cap","cannot be extended past 7 years")],"CloudTrail Lake event data store","max",False,"Recommended for usage over 25 TB a month.",
 [E(PR,"Seven-year retention pricing is recommended if your monthly usage exceeds 25 TB. Seven years of retention are included with the ingestion cost, and the retention period cannot be extended past 7 years.")],
 tier=2,vol="frequently-changing",rel="reference",bullets=["1.3.K1"],ci=[chg('cloudtrail-document-history',13)],**CT))
# changes
def CH(id,claim,question,date_line,heading,body,wn_frag,vals,bul,note=None,rel="extended"):
    SID="www/about-aws/whats-new/"+wn_frag
    return F(id,"change",claim,question,vals,"","",False,"",
      [E(SID,date_line,None,heading),E(SID,body)],tier=3,vol="frequently-changing",rel=rel,bullets=bul,ci=[chg(wn_frag.split('/',2)[2])],note=note,service="cloudtrail")
facts.append(CH("cloudtrail-change-data-event-aggregation-2025-11",
 "CloudTrail data event aggregation was announced on Nov 19, 2025: it consolidates high-volume data events into 5-minute summaries on trails.",
 "When did CloudTrail add data event aggregation, and what does it do?",
 "Posted on: Nov 19, 2025","AWS CloudTrail adds data event aggregation to simplify security monitoring",
 "Aggregation for data events streamlines security monitoring by consolidating high-volume AWS API activity into 5-minute summaries.",
 "2025/11/cloudtrail-data-event-aggregation-security-monitoring",
 [("date","Nov 19, 2025"),("sum","5-minute summaries")],["1.3.K1"],
 note="Current truth for charging: cloudtrail-pricing-data-event-aggregation-per-100000-analyzed."))
facts.append(CH("cloudtrail-change-insights-for-data-events-2025-11",
 "CloudTrail Insights was extended to data events on Nov 20, 2025; before that, Insights analyzed only management events.",
 "When did CloudTrail Insights start analyzing data events?",
 "Posted on: Nov 20, 2025","AWS CloudTrail launches Insights for data events to automatically detect anomalies in data access",
 "Until today, Insights worked by continuously analyzing only CloudTrail management events.",
 "2025/11/cloudtrail-insights-data-events-detect-anomalies-access",
 [("date","Nov 20, 2025"),("before","analyzing only CloudTrail management events")],["1.3.K1"],
 note="Current truth for charging: cloudtrail-pricing-insights-data-events-per-100000."))
facts.append(CH("cloudtrail-change-network-activity-events-vpc-endpoints-ga-2025-02",
 "CloudTrail network activity events for VPC endpoints became generally available (What's New post of Feb 14, 2025; the CloudTrail document history lists Feb 13, 2025), covering Amazon S3, Amazon EC2, AWS KMS, AWS Secrets Manager and AWS CloudTrail.",
 "When did CloudTrail network activity events for VPC endpoints become generally available, and for which services?",
 "Posted on: Feb 14, 2025","AWS CloudTrail network activity events for VPC endpoints are now generally available",
 "You can enable network activity events for VPC endpoints for five AWS Services: Amazon S3, Amazon EC2, AWS Key Management Service (AWS KMS), AWS Secrets Manager, and AWS CloudTrail.",
 "2025/02/aws-cloudtrail-network-activity-events-vpc-endpoints-generally-available",
 [("date","Feb 14, 2025"),("services","five AWS Services")],["1.3.K1"],
 note="The service list at GA grew later (history rows add more services). Current pricing: cloudtrail-pricing-network-activity-events-per-100000."))
facts.append(CH("cloudtrail-change-cloudtrail-events-in-cloudwatch-simplified-2025-12",
 "On Dec 5, 2025 AWS launched simplified enablement of CloudTrail events in Amazon CloudWatch, which uses service-linked channels and needs no trails; you pay both CloudTrail event delivery charges and CloudWatch Logs ingestion fees.",
 "When did simplified enablement of CloudTrail events in CloudWatch launch, and what does it cost?",
 "Posted on: Dec 5, 2025","AWS launches simplified enablement of AWS CloudTrail events in Amazon CloudWatch",
 "This new integration leverages service-linked channels (SLCs) to receive events from CloudTrail without requiring trails, and also provides additional benefits such as safety-checks and termination protection.",
 "2025/12/key-enhancements-cloudtrail-events-cloudwatch",
 [("date","Dec 5, 2025"),("slc","service-linked channels (SLCs)")],["1.3.K1"]))
facts.append(CH("cloudtrail-change-event-coverage-2026-09",
 "CloudTrail Event Coverage, a console view of which services and resource types have data event logging enabled, was announced on Sep 30, 2026. Not examinable yet.",
 "When was CloudTrail Event Coverage announced?",
 "Posted on: Sep 30, 2026","Uncover blind spots in AWS data plane operations with CloudTrail Event Coverage",
 "You can now see which AWS services and resource types in your environment have data event logging enabled and which do not.",
 "2026/09/aws-cloudtrail-event-coverage",
 [("date","Sep 30, 2026"),("what","which do not")],["1.3.K1"],rel="reference",
 note="not examinable yet: general availability after 2026-07-15."))
facts.append(CH("cloudtrail-change-network-activity-identity-filter-2026-07",
 "CloudTrail network activity events can be filtered by the calling IAM identity (userIdentity.arn advanced event selector field); announced Jul 20, 2026. Not examinable yet.",
 "When did CloudTrail add identity-based filtering of network activity events?",
 "Posted on: Jul 20, 2026","Selectively log network activity events by identity in AWS CloudTrail",
 "Customers can now control which network activity events are logged based on the IAM user identity making the API call.",
 "2026/07/aws-cloudtrail-filter-useridentity-advance-selectors",
 [("date","Jul 20, 2026"),("what","based on the IAM user identity")],["1.3.K1"],rel="reference",
 note="not examinable yet: general availability after 2026-07-15 (the document history row is dated July 15, 2026)."))
dump('../facts-numbers-06.json',facts)
print(len(facts))
