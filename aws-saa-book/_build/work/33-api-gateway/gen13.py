import sys; sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway")
from fh import *
MT = "api-gateway-metrics-and-dimensions"; MH = "| Metric | Description |"; SL = "set-up-logging"; PI = "private-integration"; V2 = "apigateway-vpc-links-v2"; V1 = "vpc-links-v1"; HP = "http-api-develop-integrations-private"
fs = []
fs.append(F("metrics-4xx-error-client-side", "behavior",
 "The 4XXError metric is the number of client-side errors captured in a given period, and API Gateway counts modified gateway response status codes as 4XXError errors.",
 "Which CloudWatch metric counts client-side errors?",
 ["number of client-side errors captured in a given period", "4XXError"],
 [T(MT, rowline(MT, "| 4XXError |"), MH)],
 scope="AWS/ApiGateway metrics", bullets=["2.2.K10"], tier0=True))
fs.append(F("metrics-5xx-error-server-side", "behavior",
 "The 5XXError metric is the number of server-side errors captured in a given period.",
 "Which CloudWatch metric counts server-side errors?",
 ["number of server-side errors captured in a given period", "5XXError"],
 [T(MT, rowline(MT, "| 5XXError |"), MH)],
 scope="AWS/ApiGateway metrics", bullets=["2.2.K10"], tier0=True))
fs.append(F("logging-execution-vs-access-logging", "behavior",
 "For REST APIs, execution logging records the actions API Gateway takes to process API requests, including errors and execution traces, while access logging records who accessed your API and how, in a log group, format and context variables that you choose.",
 "What is the difference between execution logging and access logging?",
 ["Execution logging", "You log who accessed your API and how"],
 [ev(SL, "Execution logging – API Gateway logs the actions taken to process API requests, including errors and execution traces. You can also configure Amazon CloudWatch Logs delivery to route execution logs to your own destinations."),
  ev(SL, "Access logging – You log who accessed your API and how. You create your own log group, choose a log format, and specify which `$context` variables to include.")],
 scope="REST APIs", bullets=["2.2.K10"], tier0=True))
fs.append(F("logging-execution-and-access-independent", "capability",
 "You can enable execution logging and access logging independently of each other.",
 "Can execution logging and access logging be turned on separately?",
 ["enable execution logging and access logging independently of each other", "independently"],
 [ev(SL, "You can enable execution logging and access logging independently of each other.")],
 scope="REST APIs", bullets=["2.2.K10"], exam="extended"))
fs.append(F("private-integration-expose-vpc-resources-outside", "capability",
 "A private integration exposes HTTP/HTTPS resources within an Amazon VPC to clients outside of the VPC, and you can control access to the API with any of the authorization methods that API Gateway supports.",
 "How can API Gateway expose resources inside a VPC to clients outside the VPC?",
 ["expose your HTTP/HTTPS resources within an Amazon VPC for access by clients outside of the VPC", "private integration"],
 [ev(PI, "Use a private integration to expose your HTTP/HTTPS resources within an Amazon VPC for access by clients outside of the VPC. This extends access to your private VPC resources beyond the VPC boundaries. You can control access to your API by using any of the authorization methods that API Gateway supports.")],
 scope="REST APIs, private integrations", bullets=["2.1.K12", "1.2.K4"], tier0=True))
fs.append(F("private-integration-needs-vpc-link-v2-alb", "behavior",
 "To create a private integration for a REST API you must first create a VPC link; API Gateway supports VPC links V2 for REST APIs, which connect your REST API to Application Load Balancers without using a Network Load Balancer.",
 "What must you create first for a private integration, and what can a VPC link V2 connect to?",
 ["you must first create a VPC link", "connect your REST API to Application Load Balancers without using an Network Load Balancer"],
 [ev(PI, "To create a private integration, you must first create a VPC link. API Gateway supports VPC links V2 for REST APIs. VPC links V2 let you create private integrations that connect your REST API to Application Load Balancers without using an Network Load Balancer.")],
 scope="REST APIs, private integrations", bullets=["2.1.K12"], tier0=True))
fs.append(F("private-integration-vpc-links-v1-legacy", "behavior",
 "VPC links V1 are considered a legacy integration type; they are supported by API Gateway, but AWS recommends that you do not create new VPC links V1.",
 "Should new private integrations use VPC links V1?",
 ["VPC links V1 are considered a legacy integration type", "we recommend that you don't create new VPC links V1"],
 [ev(PI, "VPC links V1 are considered a legacy integration type. While they are supported by API Gateway, we recommend that you don't create new VPC links V1.")],
 scope="REST APIs, private integrations", bullets=["2.1.K12"], exam="extended"))
fs.append(F("private-integration-same-account", "restriction",
 "For a REST API private integration, all resources, including the load balancer, the VPC link and the REST API, must be owned by the same AWS account.",
 "Can a private integration use a load balancer from another AWS account?",
 ["All resources must be owned by the same AWS account", "load balancer, VPC link and REST API"],
 [ev(PI, "All resources must be owned by the same AWS account. This includes the load balancer, VPC link and REST API.")],
 scope="REST APIs, private integrations", bullets=["2.1.K12"], exam="extended"))
fs.append(F("private-integration-http-default-https-via-uri", "default",
 "By default, private integration traffic uses the HTTP protocol; to use HTTPS for a REST API private integration you specify a URI that contains a secure server name.",
 "Which protocol does private integration traffic use by default?",
 ["private integration traffic uses the HTTP protocol", "specify an `uri` that contains a secure server name"],
 [ev(PI, "By default, private integration traffic uses the HTTP protocol. To use HTTPS, specify an `uri` that contains a secure server name, such as `https://example.com:443/test`.")],
 scope="REST APIs, private integrations", dm="default", bullets=["2.1.K12"], exam="extended"))
fs.append(F("private-integration-vpc-link-v2-enis", "behavior",
 "A VPC link V2 lets you connect your API routes to private resources in a VPC, such as Application Load Balancers or Amazon ECS container-based applications, and API Gateway creates and manages elastic network interfaces for the VPC link in your account.",
 "What does a VPC link V2 connect to, and what does API Gateway create in your account?",
 ["Application Load Balancers or Amazon ECS container-based applications", "creates and manages elastic network interfaces"],
 [ev(V2, "VPC links enable you to create private integrations that connect your API routes to private resources in a VPC, such as Application Load Balancers or Amazon ECS container-based applications. A private integration uses a VPC link V2 to encapsulate connections between API Gateway and targeted VPC resources. You can reuse VPC links across different resources and APIs."),
  ev(V2, "When you create a VPC link, API Gateway creates and manages elastic network interfaces for the VPC link V2 in your account.")],
 scope="VPC links V2", bullets=["2.1.K12"]))
fs.append(F("private-integration-vpc-links-v1-need-nlb", "restriction",
 "With the legacy VPC links V1 you must first create a Network Load Balancer with a listener that routes requests to resources in your VPC, and the Network Load Balancer and API must be owned by the same AWS account.",
 "What does a legacy VPC link V1 private integration require?",
 ["you must first create a Network Load Balancer", "must be owned by the same AWS account"],
 [ev(V1, "To create a private integration, you must first create a Network Load Balancer. Your Network Load Balancer must have a listener that routes requests to resources in your VPC. To improve the availability of your API, ensure that your Network Load Balancer routes traffic to resources in more than one Availability Zone in the AWS Region. Then, you create a VPC link that you use to connect your API and your Network Load Balancer. After you create a VPC link, you create private integrations to route traffic from your API to resources in your VPC through your VPC link and Network Load Balancer. The Network Load Balancer and API must be owned by the same AWS account.")],
 scope="REST APIs, VPC links V1", bullets=["2.1.K12"], exam="extended") if False else
 F("private-integration-vpc-links-v1-nlb-multi-az", "behavior",
 "For a legacy VPC link V1 private integration, AWS says that to improve the availability of your API you should make sure the Network Load Balancer routes traffic to resources in more than one Availability Zone in the Region.",
 "How do you improve the availability of a private integration that uses a Network Load Balancer?",
 ["improve the availability of your API", "routes traffic to resources in more than one Availability Zone"],
 [ev(V1, "To improve the availability of your API, ensure that your Network Load Balancer routes traffic to resources in more than one Availability Zone in the AWS Region.")],
 scope="REST APIs, VPC links V1", bullets=["2.1.K12", "2.2.K10"], exam="extended"))
fs.append(F("private-integration-http-api-targets-alb-nlb-cloud-map", "capability",
 "After you create a VPC link V2, an HTTP API private integration can connect to an Application Load Balancer, a Network Load Balancer, or resources registered with an AWS Cloud Map service.",
 "Which targets can an HTTP API private integration connect to?",
 ["Application Load Balancer, Network Load Balancer, or resources registered with an AWS Cloud Map service", "VPC link V2"],
 [ev(HP, "After you’ve created a VPC link V2, you can set up private integrations that connect to an Application Load Balancer, Network Load Balancer, or resources registered with an AWS Cloud Map service.")],
 scope="HTTP APIs, private integrations", bullets=["2.1.K12"], exam="extended"))
fs.append(F("private-integration-cloud-map-not-supported-rest", "restriction",
 "Private integrations with AWS Cloud Map are not supported for REST APIs.",
 "Can a REST API private integration use AWS Cloud Map?",
 ["Private integrations with AWS Cloud Map aren't supported", "AWS Cloud Map"],
 [ev(PI, "Private integrations with AWS Cloud Map aren't supported.")],
 scope="REST APIs, private integrations", bullets=["2.1.K12"], exam="extended"))
write("facts-behavior-13.json", fs)
