from lib import *
facts=[]
facts.append(F("cloudwatch-faq-logs-insights-cancelled-query-charged","pricing-dimension",
 "If you cancel a CloudWatch Logs Insights query manually, you are charged for the amount of ingested log data scanned up to the point of cancellation.",
 "Does CloudWatch Logs Insights charge for cancelled queries?",
 [("yes","you are charged for the amount of ingested log data scanned"),("when","up to the point at which you cancelled the query")],"Logs Insights queries","",False,"",
 [E("www/cloudwatch/faqs","Yes, if you cancel a query manually, you are charged for the amount of ingested log data scanned up to the point at which you cancelled the query.")],
 tier=2,vol="frequently-changing",rel="extended",bullets=["1.3.S1"]))
facts.append(F("cloudwatch-faq-logs-insights-failed-query-not-charged","pricing-dimension",
 "You are not charged for failed CloudWatch Logs Insights queries.",
 "Does CloudWatch Logs Insights charge for failed queries?",
 [("no","not charged for failed queries"),("what","failed queries")],"Logs Insights queries","",False,"",
 [E("www/cloudwatch/faqs","No, you are not charged for failed queries.")],
 tier=2,vol="frequently-changing",rel="extended",bullets=["1.3.S1"]))
dump('../facts-numbers-15.json',facts)
