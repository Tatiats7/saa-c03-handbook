import sys; sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway")
from fh import *
B1 = ["2.1.K1"]
fs = []
fs.append(F("service-definition", "capability",
 "Amazon API Gateway is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale.",
 "What is Amazon API Gateway, and which API types does it offer?",
 ["REST, HTTP, and WebSocket APIs", "creating, publishing, maintaining, monitoring, and securing"],
 [ev("welcome", "Amazon API Gateway is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale.")],
 scope="Amazon API Gateway", bullets=B1, tier0=True))
fs.append(F("front-door-for-backends", "capability",
 "API Gateway acts as a \"front door\" for applications to access data, business logic, or functionality from backend services, such as workloads on Amazon EC2, code on AWS Lambda, any web application, or real-time communication applications.",
 "Which backends can API Gateway front, and what role does it play for them?",
 ["acts as a \"front door\"", "code running on AWS Lambda"],
 [ev("welcome", "API Gateway acts as a \"front door\" for applications to access data, business logic, or functionality from your backend services, such as workloads running on Amazon Elastic Compute Cloud (Amazon EC2), code running on AWS Lambda, any web application, or real-time communication applications.")],
 scope="Amazon API Gateway", bullets=B1, tier0=True))
fs.append(F("manages-traffic-auth-monitoring", "capability",
 "API Gateway handles the tasks of accepting and processing concurrent API calls: traffic management, authorization and access control, monitoring, and API version management.",
 "Which tasks does API Gateway take over when it accepts and processes API calls?",
 ["traffic management, authorization and access control, monitoring, and API version management", "accepting and processing"],
 [ev("welcome", "API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls. These tasks include traffic management, authorization and access control, monitoring, and API version management.")],
 scope="Amazon API Gateway", bullets=B1))
fs.append(F("rest-api-definition", "behavior",
 "A REST API in API Gateway is a collection of HTTP resources and methods that are integrated with backend HTTP endpoints, Lambda functions, or other AWS services, and that you can deploy in one or more stages.",
 "What is an API Gateway REST API and what can it be integrated with?",
 ["backend HTTP endpoints, Lambda functions, or other AWS services", "collection of HTTP resources and methods"],
 [ev("api-gateway-basic-concept", "A collection of HTTP resources and methods that are integrated with backend HTTP endpoints, Lambda functions, or other AWS services. You can deploy this collection in one or more stages.")],
 scope="REST APIs", bullets=B1))
fs.append(F("http-api-definition", "behavior",
 "An HTTP API in API Gateway is a collection of routes and methods that are integrated with backend HTTP endpoints or Lambda functions, and that you can deploy in one or more stages.",
 "What is an API Gateway HTTP API and what does it integrate with?",
 ["routes and methods", "backend HTTP endpoints or Lambda functions"],
 [ev("api-gateway-basic-concept", "A collection of routes and methods that are integrated with backend HTTP endpoints or Lambda functions. You can deploy this collection in one or more stages.")],
 scope="HTTP APIs", bullets=B1))
fs.append(F("websocket-api-definition", "behavior",
 "A WebSocket API in API Gateway is a collection of WebSocket routes and route keys integrated with backend HTTP endpoints, Lambda functions, or other AWS services; API methods are invoked through frontend WebSocket connections that you can associate with a registered custom domain name.",
 "What is an API Gateway WebSocket API made of and what does it integrate with?",
 ["WebSocket routes and route keys", "registered custom domain name"],
 [ev("api-gateway-basic-concept", "A collection of WebSocket routes and route keys that are integrated with backend HTTP endpoints, Lambda functions, or other AWS services. You can deploy this collection in one or more stages. API methods are invoked through frontend WebSocket connections that you can associate with a registered custom domain name.")],
 scope="WebSocket APIs", bullets=B1))
fs.append(F("http-api-lower-latency-lower-cost", "capability",
 "HTTP APIs let you create RESTful APIs with lower latency and lower cost than REST APIs.",
 "What does AWS say about the latency and cost of HTTP APIs compared with REST APIs?",
 ["lower latency and lower cost than REST APIs", "lower latency and lower cost"],
 [ev("api-gateway-overview-developer-experience", "HTTP APIs enable you to create RESTful APIs with lower latency and lower cost than REST APIs.")],
 scope="HTTP APIs versus REST APIs", bullets=B1, tier0=True))
fs.append(F("http-api-minimal-features-lower-price", "decision",
 "REST APIs support more features than HTTP APIs, while HTTP APIs are designed with minimal features so that they can be offered at a lower price.",
 "Why are HTTP APIs cheaper than REST APIs?",
 ["designed with minimal features", "offered at a lower price"],
 [ev("http-api", "REST APIs and HTTP APIs are both RESTful API products. REST APIs support more features than HTTP APIs, while HTTP APIs are designed with minimal features so that they can be offered at a lower price.")],
 scope="REST APIs versus HTTP APIs", bullets=B1, tier0=True) if False else
 F("http-api-minimal-features-lower-price", "behavior",
 "REST APIs support more features than HTTP APIs, while HTTP APIs are designed with minimal features so that they can be offered at a lower price.",
 "Why are HTTP APIs cheaper than REST APIs?",
 ["designed with minimal features", "offered at a lower price"],
 [ev("http-api", "REST APIs and HTTP APIs are both RESTful API products. REST APIs support more features than HTTP APIs, while HTTP APIs are designed with minimal features so that they can be offered at a lower price.")],
 scope="REST APIs versus HTTP APIs", bullets=B1, tier0=True))
fs.append(F("choose-rest-or-http-guidance", "behavior",
 "AWS says to choose REST APIs if you need features such as API keys, per-client throttling, request validation, AWS WAF integration, or private API endpoints, and to choose HTTP APIs if you do not need the features included with REST APIs.",
 "When should you choose a REST API over an HTTP API?",
 ["Choose REST APIs if you need features", "API keys, per-client throttling, request validation"],
 [ev("http-api-vs-rest", "Choose REST APIs if you need features such as API keys, per-client throttling, request validation, AWS WAF integration, or private API endpoints. Choose HTTP APIs if you don't need the features included with REST APIs.")],
 scope="REST APIs versus HTTP APIs", bullets=B1, tier0=True))
fs.append(F("http-api-oidc-oauth-cors-auto-deploy", "capability",
 "HTTP APIs support OpenID Connect and OAuth 2.0 authorization, and come with built-in support for cross-origin resource sharing (CORS) and automatic deployments.",
 "Which authorization standards and built-in features do HTTP APIs support?",
 ["OpenID Connect and OAuth 2.0 authorization", "built-in support for cross-origin resource sharing (CORS) and automatic deployments"],
 [ev("http-api", "HTTP APIs support OpenID Connect and OAuth 2.0 authorization. They come with built-in support for cross-origin resource sharing (CORS) and automatic deployments.")],
 scope="HTTP APIs", bullets=B1))
fs.append(F("http-api-backends-lambda-or-http", "capability",
 "You can use HTTP APIs to send requests to AWS Lambda functions or to any publicly routable HTTP endpoint.",
 "Which backends can an HTTP API send requests to?",
 ["AWS Lambda functions", "any publicly routable HTTP endpoint"],
 [ev("api-gateway-overview-developer-experience", "You can use HTTP APIs to send requests to AWS Lambda functions or to any publicly routable HTTP endpoint.")],
 scope="HTTP APIs", bullets=B1))
fs.append(F("websocket-two-way-server-push", "capability",
 "In a WebSocket API, the client and the server can both send messages to each other at any time, so backend servers can push data to connected users and devices without polling.",
 "What problem does an API Gateway WebSocket API solve?",
 ["both send messages to each other at any time", "avoiding the need to implement complex polling mechanisms"],
 [ev("api-gateway-overview-developer-experience", "In a WebSocket API, the client and the server can both send messages to each other at any time. Backend servers can easily push data to connected users and devices, avoiding the need to implement complex polling mechanisms.")],
 scope="WebSocket APIs", bullets=B1, tier0=True))
fs.append(F("websocket-use-cases", "capability",
 "Targeted WebSocket API use cases are real-time applications such as chat applications, real-time dashboards such as stock tickers, and real-time alerts and notifications.",
 "Which applications are typical uses of an API Gateway WebSocket API?",
 ["Chat applications", "Real-time dashboards such as stock tickers"],
 [ev("api-gateway-overview-developer-experience", "You can use API Gateway WebSocket APIs to build secure, real-time communication applications without having to provision or manage any servers to manage connections or large-scale data exchanges.")],
 scope="WebSocket APIs", bullets=B1, exam="extended") if False else
 F("websocket-no-servers-for-connections", "capability",
 "You can use API Gateway WebSocket APIs to build secure, real-time communication applications without provisioning or managing any servers to manage connections or large-scale data exchanges.",
 "Do you need servers to manage connections for a real-time WebSocket application on API Gateway?",
 ["real-time communication applications", "without having to provision or manage any servers"],
 [ev("api-gateway-overview-developer-experience", "You can use API Gateway WebSocket APIs to build secure, real-time communication applications without having to provision or manage any servers to manage connections or large-scale data exchanges.")],
 scope="WebSocket APIs", bullets=B1))
fs.append(F("websocket-chat-lambda-example", "capability",
 "A serverless chat application can use an API Gateway WebSocket API and AWS Lambda to send and receive messages to and from individual users or groups of users in a chat room, and a WebSocket API can invoke backend services such as Lambda, Kinesis, or an HTTP endpoint based on message content.",
 "What backends can a WebSocket API invoke based on message content?",
 ["AWS Lambda, Amazon Kinesis, or an HTTP endpoint", "based on message content"],
 [ev("api-gateway-overview-developer-experience", "For example, you could build a serverless application using an API Gateway WebSocket API and AWS Lambda to send and receive messages to and from individual users or groups of users in a chat room. Or you could invoke backend services such as AWS Lambda, Amazon Kinesis, or an HTTP endpoint based on message content.")],
 scope="WebSocket APIs", bullets=B1, exam="extended"))
fs.append(F("websocket-connection-persistent-client-side-only", "behavior",
 "API Gateway maintains a persistent connection between clients and API Gateway itself; there is no persistent connection between API Gateway and backend integrations such as Lambda functions, which are invoked as needed based on the content of messages from clients.",
 "Is there a persistent connection between API Gateway and a Lambda backend in a WebSocket API?",
 ["no persistent connection between API Gateway and backend integrations", "persistent connection between clients and API Gateway"],
 [ev("api-gateway-basic-concept", "API Gateway maintains a persistent connection between clients and API Gateway itself. There is no persistent connection between API Gateway and backend integrations such as Lambda functions. Backend services are invoked as needed, based on the content of messages received from clients.")],
 scope="WebSocket APIs", bullets=B1, tier0=True))
fs.append(F("deployment-needs-stage", "behavior",
 "An API deployment is a point-in-time snapshot of your API; to be available for clients to use, the deployment must be associated with one or more API stages.",
 "Must an API be deployed to a stage before clients can call it?",
 ["point-in-time snapshot of your API Gateway API", "must be associated with one or more API stages"],
 [ev("api-gateway-basic-concept", "A point-in-time snapshot of your API Gateway API. To be available for clients to use, the deployment must be associated with one or more API stages.")],
 scope="API deployments", bullets=B1, tier0=True))
fs.append(F("stage-lifecycle-reference", "behavior",
 "An API stage is a logical reference to a lifecycle state of your API, for example dev, prod, beta or v2, identified by API ID and stage name.",
 "What is an API Gateway stage and how is it identified?",
 ["logical reference to a lifecycle state of your API", "identified by API ID and stage name"],
 [ev("api-gateway-basic-concept", "A logical reference to a lifecycle state of your API (for example, 'dev', 'prod', 'beta', 'v2'). API stages are identified by API ID and stage name.")],
 scope="API stages", bullets=B1))
fs.append(F("rest-resource-method-definition", "behavior",
 "A REST API is made up of resources and methods: a resource is a logical entity that an app can access through a resource path, and a method corresponds to a REST API request submitted by the user and the response returned to the user.",
 "What are a resource and a method in an API Gateway REST API?",
 ["made up of resources and methods", "logical entity that an app can access through a resource path"],
 [ev("api-gateway-overview-developer-experience", "An API Gateway REST API is made up of resources and methods. A resource is a logical entity that an app can access through a resource path. A method corresponds to a REST API request that is submitted by the user of your API and the response returned to the user.")],
 scope="REST APIs", bullets=B1))
fs.append(F("rest-method-and-integration-requests", "behavior",
 "In API Gateway REST APIs, the frontend is encapsulated by method requests and method responses, and the API interfaces with the backend by means of integration requests and integration responses.",
 "How does a REST API separate the client side from the backend side?",
 ["encapsulated by method requests and method responses", "integration requests and integration responses"],
 [ev("api-gateway-overview-developer-experience", "The app doesn't need to know where the requested data is stored and fetched from on the backend. In API Gateway REST APIs, the frontend is encapsulated by method requests and method responses. The API interfaces with the backend by means of integration requests and integration responses.")],
 scope="REST APIs", bullets=B1))
fs.append(F("mapping-template-vtl", "behavior",
 "A mapping template is a Velocity Template Language (VTL) script that transforms a request body from the frontend data format to the backend data format, or a response body from the backend format to the frontend format.",
 "What is a mapping template in API Gateway?",
 ["Velocity Template Language (VTL)", "transforms a request body from the frontend data format to the backend data format"],
 [ev("api-gateway-basic-concept", "A script in Velocity Template Language (VTL) that transforms a request body from the frontend data format to the backend data format, or that transforms a response body from the backend data format to the frontend data format.")],
 scope="REST API and WebSocket API integrations", bullets=B1, exam="extended"))
fs.append(F("mock-integration-no-backend", "capability",
 "In a mock integration, API responses are generated from API Gateway directly, without the need for an integration backend.",
 "What is a mock integration in API Gateway?",
 ["generated from API Gateway directly", "without the need for an integration backend"],
 [ev("api-gateway-basic-concept", "In a mock integration, API responses are generated from API Gateway directly, without the need for an integration backend.")],
 scope="mock integrations", bullets=B1, exam="extended"))
write("facts-behavior-01.json", fs)
