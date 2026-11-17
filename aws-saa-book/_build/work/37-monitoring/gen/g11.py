from lib import *
import json
facts=[]
AQ="docs/prometheus/latest/userguide/AMP_quotas"
TH="| Name | Default | Adjustable | Description |"
MP=dict(service="managed-prometheus")
MG=dict(service="managed-grafana")
facts.append(F("managed-prometheus-retention-150-days-default-max-1095","default",
 "Metrics ingested into an Amazon Managed Service for Prometheus workspace are stored for 150 days by default and then deleted automatically; you can set the retention period of a workspace up to a maximum of 1095 days (three years).",
 "How long does Amazon Managed Service for Prometheus keep metrics by default, and what is the maximum retention?",
 [("default",("150 days","one hundred fifty days")),("max",("1095 days","one thousand ninety-five days, three years"))],"per workspace","default",True,"Retention is configured on the workspace.",
 [E("docs/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus","Metrics ingested into a workspace are stored for 150 days by default, and are then automatically deleted. You can adjust the retention period by configuring your workspace up to a maximum of 1095 days (three years).")],
 rel="extended",bullets=["2.2.S3"],**MP))
facts.append(F("managed-prometheus-data-replicated-three-azs","behavior",
 "Data ingested into an Amazon Managed Service for Prometheus workspace is replicated across three Availability Zones in the same Region.",
 "Across how many Availability Zones does Amazon Managed Service for Prometheus replicate workspace data?",
 [("azs","replicated across three Availability Zones"),("region","in the same Region")],"per workspace","",False,"",
 [E("docs/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus","Amazon Managed Service for Prometheus is designed to be highly available using multiple Availability Zone (Multi-AZ) deployments. Data ingested into a workspace is replicated across three Availability Zones in the same Region.")],
 rel="extended",bullets=["2.2.S3"],**MP))
facts.append(F("managed-prometheus-quota-active-series-per-workspace","quota",
 "A workspace has a default of 50,000,000 active series, a series being active if a sample was reported in the past 2 hours; the quota is adjustable up to a maximum of 1.5 billion.",
 "How many active series can an Amazon Managed Service for Prometheus workspace hold by default?",
 [("default","50,000,000"),("max","maximum of 1.5 billion")],"per workspace","default",True,"The maximum of 1.5 billion became available on 2026-07-21 (not examinable yet).",
 [E(AQ,"| Active series per workspace | Each supported Region: 50,000,000 | Yes | The number of unique active series per workspace (up to a maximum of 1.5 billion). A series is active if a sample has been reported in the past 2 hours. Capacity from 2 M to 50 M is automatically adjusted based on the last 30 min of usage. |",TH)],
 vol="frequently-changing",rel="extended",bullets=["2.2.S3"],**MP,
 note="The 1.5 billion maximum is a change of 2026-07-21 (not examinable yet): see managed-prometheus-change-1500m-active-series-2026-07."))
facts.append(F("managed-prometheus-quota-workspaces-per-region-per-account","quota",
 "An account can have 25 workspaces per Region by default, and this quota is adjustable.",
 "How many Amazon Managed Service for Prometheus workspaces can an account have per Region?",
 [("max","25")],"per account, per Region","default",True,"",
 [E(AQ,"| Workspaces per region per account | Each supported Region: 25 | Yes | The maximum number of workspaces per region. |",TH)],
 rel="reference",bullets=["2.2.S3"],**MP))
facts.append(F("managed-prometheus-quota-labels-per-series","quota",
 "A metric series can have 150 labels by default, and this quota is adjustable.",
 "How many labels can an Amazon Managed Service for Prometheus metric series have?",
 [("max","150")],"per metric series","default",True,"",
 [E(AQ,"| Labels per metric series | Each supported Region: 150 | Yes | Number of labels per metric series. |",TH)],
 rel="reference",bullets=["2.2.S3"],**MP))
facts.append(F("managed-prometheus-quota-query-time-range-95-days","quota",
 "The maximum time range of QueryMetrics, GetSeries and GetLabels API calls is 95 days, and this quota is not adjustable.",
 "How far back can one Amazon Managed Service for Prometheus query reach?",
 [("max","95")],"per query","max",False,"",
 [E(AQ,"| Query time range in days | Each supported Region: 95 | No | The maximum time range of QueryMetrics, GetSeries, and GetLabels APIs. |",TH)],
 rel="reference",bullets=["2.2.S3"],**MP))
facts.append(F("managed-prometheus-pricing-ingestion-per-sample-volume-tiers","pricing-dimension",
 "Amazon Managed Service for Prometheus charges per metric sample ingested, with volume tiering on the total samples ingested per month.",
 "What is Amazon Managed Service for Prometheus ingestion charged by?",
 [("dim","each metric sample ingested"),("tier","Volume tiering applies")],"per month","",False,"",
 [E("www/prometheus/pricing","Amazon Managed Service for Prometheus counts each metric sample ingested to the secured Prometheus-compatible endpoint. Volume tiering applies to the total number of metric samples ingested per month (see pricing table below for tier rates).")],
 tier=2,vol="frequently-changing",rel="reference",bullets=["2.2.S3"],**MP))
facts.append(F("managed-prometheus-pricing-query-samples-processed","pricing-dimension",
 "Amazon Managed Service for Prometheus meters Query Samples Processed (QSP) from all QueryMetric API requests: the total number of data points queried with PromQL for a time range.",
 "What are Amazon Managed Service for Prometheus queries charged by?",
 [("dim","Query Samples Processed (QSP)"),("api","all QueryMetric API requests")],"queries","",False,"",
 [E("www/prometheus/pricing","Amazon Managed Service for Prometheus meters the Query Samples Processed (QSP) from all QueryMetric API requests. QSP is the total number of data points queried using Prometheus Query Language (PromQL) for a given time range.")],
 tier=2,vol="frequently-changing",rel="reference",bullets=["2.2.S3"],**MP))
facts.append(F("managed-prometheus-pricing-collector-hours-and-samples","pricing-dimension",
 "For the Amazon Managed Service for Prometheus collector you are charged for the number of hours it is turned on and the number of samples collected.",
 "What is the Amazon Managed Service for Prometheus collector charged by?",
 [("hours","number of hours it is turned on"),("samples","number of samples collected")],"collector","",False,"",
 [E("www/prometheus/pricing","For Amazon Managed Service for Prometheus collector, you are charged for the number of hours it is turned on and the number of samples collected.")],
 tier=2,vol="frequently-changing",rel="reference",bullets=["2.2.S3"],**MP))
facts.append(F("managed-prometheus-pricing-storage-gb-prorated-no-transfer-in","pricing-dimension",
 "Stored metric samples and metadata are measured in gigabytes; charges for metrics ingested and stored are prorated by the hour, and there is no Data Transfer IN charge.",
 "How is Amazon Managed Service for Prometheus storage charged?",
 [("hour","prorated by the hour"),("in","no Data Transfer IN charge")],"workspace storage","",False,"",
 [E("www/prometheus/pricing","Charges for metrics ingested and stored are prorated by the hour and billed only when you send metrics to Amazon Managed Service for Prometheus. Note that there is no Data Transfer IN charge for AMP.")],
 tier=2,vol="frequently-changing",rel="reference",bullets=["2.2.S3"],**MP))
# Grafana
facts.append(F("managed-grafana-quota-workspaces-per-region","quota",
 "An account can have 5 Amazon Managed Grafana workspaces in each Region by default, and this quota is adjustable.",
 "How many Amazon Managed Grafana workspaces can an account have per Region?",
 [("max","5")],"per account, per Region","default",True,"",
 [E("docs/grafana/latest/userguide/AMG_quotas","| Number of workspaces | Each supported Region: 5 | Yes | The maximum number of workspaces that you can have in this account in the current region. |",TH)],
 rel="reference",bullets=["2.2.S3"],**MG))
facts.append(F("managed-grafana-quota-users-per-workspace","quota",
 "An Amazon Managed Grafana workspace allows 10,000 provisioned users and 500 concurrent users, and this quota is not adjustable.",
 "How many users can an Amazon Managed Grafana workspace have?",
 [("prov","10,000 provisioned"),("conc","500 concurrent")],"per workspace","max",False,"",
 [E("docs/grafana/latest/userguide/AMG_quotas","| Users | No | 10,000 provisioned, 500 concurrent per workspace. |","| Resource | Adjustable | Default Quota |")],
 rel="reference",bullets=["2.2.S3"],**MG))
facts.append(F("managed-grafana-pricing-licenses-per-workspace-minimum-one-editor","pricing-dimension",
 "Amazon Managed Grafana user licenses are priced per workspace per month, and each workspace requires a minimum of one Editor license, even if no users log in.",
 "What are Amazon Managed Grafana licenses priced per, and is there a minimum?",
 [("unit","per workspace, per month"),("min","a minimum of one Amazon Managed Grafana Editor license")],"per workspace","",False,"",
 [E("www/grafana/pricing","All user licenses are per workspace, per month. Each workspace requires a minimum of one Amazon Managed Grafana Editor license in order to manage and log into the workspace, even if no users log in.")],
 tier=2,vol="frequently-changing",rel="extended",bullets=["2.2.S3"],**MG))
facts.append(F("managed-grafana-price-editor-license-per-active-user","price",
 "An Amazon Managed Grafana Editor license costs $9 per active editor or administrator user per workspace per month. The pricing page does not name a Region.",
 "How much is an Amazon Managed Grafana Editor license?",
 [("price","$9 per active editor or administrator user per workspace")],"per active editor or administrator user per workspace per month","",False,"",
 [E("www/grafana/pricing","An Amazon Managed Grafana Editor license costs $9 per active editor or administrator user per workspace and provides the user with administrative permissions for managing workspace users, creating and managing dashboards and alerts, and assigning permissions to access data sources.")],
 tier=2,vol="frequently-changing",rel="reference",bullets=["2.2.S3"],**MG))
facts.append(F("managed-grafana-price-viewer-license-per-active-user","price",
 "An Amazon Managed Grafana Viewer license costs $5 per active user per workspace per month and gives view-only access. The pricing page does not name a Region.",
 "How much is an Amazon Managed Grafana Viewer license?",
 [("price","$5 per active user per workspace")],"per active user per workspace per month","",False,"",
 [E("www/grafana/pricing","For customers who need only view access, an Amazon Managed Grafana Viewer license costs $5 per active user per workspace and provides the user with view-only access to the Amazon Managed Grafana workspace.")],
 tier=2,vol="frequently-changing",rel="reference",bullets=["2.2.S3"],**MG))
facts.append(F("managed-grafana-price-enterprise-plugins-additional-per-user","price",
 "The Amazon Managed Grafana Enterprise Plugins license costs an additional $45 per active user per workspace. The pricing page does not name a Region.",
 "How are Amazon Managed Grafana Enterprise plugins billed?",
 [("price","$45 per active user per workspace"),("extra","additional")],"per active user per workspace per month","",False,"",
 [E("www/grafana/pricing","To access Enterprise Plugins to connect to third-party Enterprise data sources listed here, an Amazon Managed Grafana Enterprise Plugins license costs an additional $45 per active user per workspace.")],
 tier=2,vol="frequently-changing",rel="reference",bullets=["2.2.S3"],**MG))
facts.append(F("managed-grafana-free-trial-90-days-five-users","default",
 "Amazon Managed Grafana offers a 90-day free trial with up to five free users per account.",
 "What free trial does Amazon Managed Grafana offer?",
 [("days","90-day free trial"),("users","up to five free users per account")],"per account","default",False,"",
 [E("www/grafana/pricing","Amazon Managed Grafana offers a 90-day free trial, with up to five free users per account.")],
 tier=2,vol="frequently-changing",rel="reference",bullets=["2.2.S3"],**MG))
# Health
HW="docs/health/latest/ug/what-is-aws-health"
facts.append(F("health-dashboard-free-no-setup-all-customers","behavior",
 "The AWS Health Dashboard is available to all AWS customers at no additional cost and needs no setup, and all customers can receive AWS Health events through Amazon EventBridge at no additional cost.",
 "Is the AWS Health Dashboard free, and does it need setup?",
 [("free","at no additional cost"),("setup","requires no setup")],"all AWS customers","",False,"",
 [E(HW,"The AWS Health Dashboard is available for all AWS customers at no additional cost.")],
 rel="extended",bullets=["2.2.S3"],service="health-dashboard"))
facts.append(F("health-dashboard-api-needs-business-or-enterprise-support","restriction",
 "To use the AWS Health API you need an AWS Business Support+, AWS Enterprise Support or AWS Unified Operations plan; in Regions without these plans, or before transitioning, a Business, Enterprise On-Ramp or Enterprise Support plan works.",
 "Which AWS Support plans allow use of the AWS Health API?",
 [("api","you can use the AWS Health API"),("plans","AWS Enterprise Support")],"AWS Health API","",False,"The AWS Health Dashboard itself needs no support plan.",
 [E(HW,"If you have an AWS Business Support\\+, AWS Enterprise Support, or AWS Unified Operations plan, you can use the AWS Health API to integrate with in-house and third-party systems.")],
 rel="extended",bullets=["2.2.S3"],service="health-dashboard",note="Older sources say Business, Enterprise On-Ramp or Enterprise Support; the page also lists those for Regions without the new plans."))
facts.append(F("health-dashboard-events-viewable-90-days","limit",
 "You can view AWS Health events in the AWS Health Dashboard or the AWS Health API for up to 90 days.",
 "How far back can you view AWS Health events?",
 [("max","up to 90 days")],"AWS Health events","max",False,"",
 [E("docs/health/latest/ug/aws-health-concepts-and-terms","The event status tells you if the Health event is open, closed, or upcoming. You can view Health events in the AWS Health Dashboard or the AWS Health API for up to 90 days.")],
 rel="extended",bullets=["2.2.S3"],service="health-dashboard"))
facts.append(F("health-dashboard-organizational-events-90-days-not-adjustable","limit",
 "Organizational AWS Health events are available for 90 days before they are deleted, and this quota can't be increased.",
 "How long are AWS Health organizational view events available?",
 [("max","90 days")],"organizational view events","max",False,"",
 [E("docs/health/latest/ug/aggregate-events","Organizational events are available for 90 days before they're deleted. This quota can't be increased.")],
 rel="reference",bullets=["2.2.S3"],service="health-dashboard"))
facts.append(F("health-dashboard-service-health-no-account-needed","behavior",
 "You can view the AWS Health Dashboard - Service health page for the health of all AWS services without signing in or having an AWS account.",
 "Do you need an AWS account to see the public AWS service health page?",
 [("noacct","You don't need to sign in or have an AWS account"),("what","health of all AWS services")],"Service health page","",False,"",
 [E("docs/health/latest/ug/aws-health-dashboard-status","You don't need to sign in or have an AWS account to access the AWS Health Dashboard – Service health page.")],
 rel="reference",bullets=["2.2.S3"],service="health-dashboard"))
# changes with heading date
def CH(id,service,claim,question,date_line,heading,body,wn,vals,bul,note=None,rel="reference",ci=None):
    SID="www/about-aws/whats-new/"+wn
    return F(id,"change",claim,question,vals,"","",False,"",[E(SID,date_line,None,heading),E(SID,body)],tier=3,vol="frequently-changing",rel=rel,bullets=bul,ci=[chg(wn.split('/',2)[2])],note=note,service=service)
facts.append(CH("managed-prometheus-change-1500m-active-series-2026-07","managed-prometheus",
 "On Jul 21, 2026 Amazon Managed Service for Prometheus began to support up to 1.5 billion active metric time series and up to 200,000 total recording and alerting rules per workspace. Not examinable yet.",
 "When did Amazon Managed Service for Prometheus raise the active series and rule maximums per workspace?",
 "Posted on: Jul 21, 2026","Amazon Managed Service for Prometheus supports 1.5B active metrics and 200K rules per workspace",
 "Amazon Managed Service for Prometheus now supports up to 1.5 billion active metric time series and up to 200,000 total recording and alerting rules per workspace.",
 "2026/07/amazon-managed-service-prometheus-1500m-metrics-workspace",
 [("date","Jul 21, 2026"),("series","1.5 billion active metric time series"),("rules","200,000 total recording and alerting rules")],["2.2.S3"],
 note="not examinable yet: announced after 2026-07-15. Current default quota: managed-prometheus-quota-active-series-per-workspace."))
facts.append(CH("managed-grafana-change-grafana-13-2-workspaces-2026-09","managed-grafana",
 "On Sep 30, 2026 Amazon Managed Grafana began to support creating new workspaces with Grafana version 13.2. Not examinable yet.",
 "When did Amazon Managed Grafana add Grafana 13.2 workspaces?",
 "Posted on: Sep 30, 2026","Amazon Managed Grafana now supports creating Grafana 13.2 workspaces",
 "Amazon Managed Grafana now supports creating new workspaces with Grafana version 13.2.",
 "2026/09/amazon-managed-grafana-now-supports-creating-grafana-13-2-workspaces",
 [("date","Sep 30, 2026"),("ver","Grafana version 13.2")],["2.2.S3"],
 note="not examinable yet: announced after 2026-07-15."))
facts.append(CH("health-dashboard-change-version-catalog-2026-10","health-dashboard",
 "On Oct 2, 2026 AWS Health introduced the version catalog, a centralized source of lifecycle information for software versions across AWS services. Not examinable yet.",
 "When did AWS Health introduce the version catalog?",
 "Posted on: Oct 2, 2026","AWS Health introduces the version catalog for software lifecycle management",
 "Today, AWS Health introduces the version catalog which provides a centralized source of lifecycle information for software versions across AWS services.",
 "2026/10/aws-health-introduces-version-catalog-software-lifecycle-management",
 [("date","Oct 2, 2026"),("what","centralized source of lifecycle information")],["2.2.S3"],
 note="not examinable yet: announced after 2026-07-15."))
dump('../facts-numbers-11.json',facts); print(len(facts))
