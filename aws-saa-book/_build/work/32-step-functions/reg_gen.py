"""Registrar register-32: builds amend patches (one JSON per fact) and the decisions file.
Run: python3 -I aws-saa-book/_build/work/32-step-functions/reg_gen.py
Checks every number-free display: at most 8 words and held by a quote (normalised)."""
import json, os, re, copy

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..', '..')
OUT = os.path.join(HERE, 'reg-patches')
os.makedirs(OUT, exist_ok=True)
facts = {}
for s in ['step-functions', 'mq', 'appflow']:
    for line in open(os.path.join(ROOT, 'data', 'facts', s + '.jsonl'), encoding='utf-8'):
        if line.strip():
            f = json.loads(line)
            facts[f['id']] = f

MAP = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"', '—': '-', '–': '-'})


def norm(s):
    s = (s or '').translate(MAP).replace('`', '').replace('*', '')
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip().lower()


SUPERSEDE = [
    ('appflow-overview-encrypts-in-motion-privatelink', 'appflow-faq-encrypts-in-motion-restrict-public-internet-privatelink', 'duplicate: same sentence in the AWS overview whitepaper and the AppFlow FAQ; FAQ kept'),
    ('appflow-overview-schedule-event-or-demand', 'appflow-faq-run-on-schedule-event-or-demand', 'duplicate: same sentence in the AWS overview whitepaper and the AppFlow FAQ; FAQ kept'),
    ('appflow-faq-fully-managed-saas-to-aws-transfer', 'appflow-what-is-managed-saas-integration', 'duplicate definition; the user guide sentence is kept'),
    ('mq-activemq-ebs-only-m5', 'mq-activemq-ebs-only-m5-no-active-standby', 'duplicate: the kept fact quotes the same sentence plus the single-AZ sentence'),
    ('mq-activemq-ebs-single-az-no-active-standby', 'mq-activemq-ebs-only-m5-no-active-standby', 'duplicate: the kept fact quotes the same sentence without a cut-off display'),
    ('mq-activemq-storage-efs-default-ebs-option', 'mq-activemq-storage-efs-default', 'duplicate: identical quote'),
    ('mq-faq-activemq-efs-for-durability-ebs-for-throughput', 'mq-activemq-storage-efs-default', 'duplicate: the developer guide states the same EFS/EBS choice and the default'),
    ('mq-activemq-storage-type-immutable', 'mq-activemq-storage-type-fixed-after-create', 'duplicate: identical sentence'),
    ('mq-faq-kms-manages-keys-for-at-rest-encryption', 'mq-encryption-at-rest-always-with-kms', 'duplicate: the developer guide sentence also says encryption at rest is always on'),
    ('mq-faq-managed-broker-activemq-rabbitmq', 'mq-welcome-managed-broker-activemq-rabbitmq', 'duplicate definition; the developer guide uses the current engine name ActiveMQ Classic'),
    ('mq-overview-standard-apis-and-protocols', 'mq-faq-switch-from-any-standards-based-broker', 'duplicate: same protocol list and no-rewrite statement; FAQ kept'),
    ('step-functions-async-express-result-via-logs', 'step-functions-async-express-returns-confirmation', 'duplicate: identical sentence'),
    ('step-functions-inline-map-concurrency-40', 'step-functions-map-inline-when-to-use', 'duplicate: identical sentence'),
    ('step-functions-overview-tracks-steps-and-retries', 'step-functions-faq-tracks-steps-retries-logs-state', 'duplicate: same sentence in the overview whitepaper and the FAQ'),
    ('step-functions-overview-fully-managed-visual-workflows', 'step-functions-faq-fully-managed-visual-workflows', 'duplicate: same sentence in the overview whitepaper and the FAQ'),
    ('step-functions-pricing-each-retry-extra-transition', 'step-functions-price-retry-extra-transition', 'duplicate: identical pricing sentence'),
    ('step-functions-history-hard-quota-25000', 'step-functions-max-execution-history-size', 'duplicate: the quotas page row is the more direct source and names the consequence'),
    ('step-functions-quota-open-executions', 'step-functions-open-executions-not-express', 'duplicate: same quota; the kept fact also says it does not apply to Express'),
    ('step-functions-faq-states-language-json', 'step-functions-asl-json-based-language', 'duplicate: the developer guide definition is kept'),
]
SUP_IDS = {o for o, _, _ in SUPERSEDE}

# id -> {old display: new display (None removes)}
D = {
    'mq-decision-guide-managed-open-source-automation-portability': {
        'compatible with many popular deployment tools used for on-premises deployments': 'compatible with many popular deployment tools',
        'Managed open source services (such as Amazon MQ and Amazon MSK)': 'Managed open source services'},
    'step-functions-express-only-request-response': {'the same integrations but not the same integration patterns': 'not the same integration patterns'},
    'mq-rabbitmq-iam-auth-via-sts-jwt': {'obtain JWT tokens from AWS Security Token Service (STS)': 'obtain JWT tokens from AWS Security Token Service'},
    'appflow-encrypts-data-at-rest-and-in-transit': {'We encrypt your data at rest and in transit': 'encrypt your data at rest and in transit'},
    'appflow-salesforce-api-preference-automatic-default': {'selects the API to use based on the number of records that the run transfers': 'based on the number of records'},
    'mq-migration-replatform-almost-as-is': {'replacing some components to take advantage of a cloud architecture': 'replacing some components'},
    'step-functions-parallel-failure-lambda-keeps-running': {'activity workers processing a task token are not stopped': 'processing a task token are not stopped'},
    'step-functions-price-express-request-count': {'counts a request each time it starts executing a workflow': 'counts a request each time it starts'},
    'mq-migration-ibm-mq-tibco-minimal-code-changes': {'commercial brokers, such as IBM MQ and TIBCO Enterprise Management Service (EMS)': 'commercial brokers, such as IBM MQ and TIBCO',
                                                       'migrate applications with minimal code changes': 'migrate applications with minimal code changes'},
    'step-functions-continue-as-new-from-task-state': {'starting a new workflow execution from the Task state': 'starting a new workflow execution'},
    'step-functions-callback-wait-up-to-one-year': {'wait for an external process or workflow to complete': 'wait for an external process or workflow'},
    'step-functions-express-history-only-cloudwatch-logs': {"Express Workflows don't record execution history in AWS Step Functions": "don't record execution history in AWS Step Functions"},
    'mq-faq-who-should-use-standard-messaging-without-operating-broker': {'without the operational burden of managing the message broker': 'without the operational burden'},
    'step-functions-lambda-guide-human-approval-waitfortasktoken': {'Choice state to route workflows based on function output': 'route workflows based on function output'},
    'step-functions-xray-not-for-distributed-map-children': {"doesn't support X-Ray tracing for the child workflow executions": "doesn't support X-Ray tracing"},
    'mq-faq-kms-three-key-options-at-rest': {'a KMS key in your account that you create and manage': 'that you create and manage',
                                            'a KMS key in the Amazon MQ service account': 'KMS key in the Amazon MQ service account'},
    'mq-activemq-auth-simple-and-ldap': {'created and managed through the Amazon MQ console or API': 'through the Amazon MQ console or API'},
    'step-functions-parallel-branch-failure-fails-state': {'the entire Parallel state is considered to have failed': 'entire Parallel state is considered to have failed'},
    'step-functions-express-console-history-from-cwlogs-three-hours': {'retrieves log data gathered through a CloudWatch Logs log group': 'a CloudWatch Logs log group'},
    'step-functions-task-timeoutseconds-default': {'maximum time an activity or a task can run': 'Specifies the maximum time'},
    'mq-cloudwatch-integration-broker-metrics': {'the Amazon MQ console, the CloudWatch console, command line, and API': 'the CloudWatch console, command line, and API'},
    'appflow-faq-three-triggers-on-demand-event-scheduled': {'on demand, based on business events, or on a schedule': 'based on business events, or on a schedule'},
    'mq-serverless-guide-event-source-mapping-reads-from-mq': {'DynamoDB Streams, Amazon Kinesis, Amazon MQ, Amazon MSK, self-managed Apache Kafka, and Amazon SQS': 'process items from a stream or queue'},
    'step-functions-callback-pauses-until-token-returned': {'pause a workflow until a task token is returned': 'until a task token is returned'},
    'step-functions-state-wait-pauses-workflow': {'delays the state machine from continuing for a specified time': 'delays the state machine from continuing'},
    'step-functions-faq-vs-swf-external-signals-child-processes': {'child processes that return a result to a parent': 'child processes that return a result'},
    'step-functions-bp-migrate-standard-to-express-requirements': {'does not use the .waitForTaskToken or .sync service integration patterns': 'does not use the .waitForTaskToken or .sync'},
    'step-functions-optimized-integrations-recommended': {'automatically converts API output from escaped JSON to a JSON object': 'converts API output from escaped JSON'},
    'step-functions-pricing-state-transitions-include-retries': {'counts a state transition each time a step of your workflow is executed': 'counts a state transition each time a step'},
    'step-functions-activity-heartbeat-wait-up-to-a-year': {'configuring a long timeout duration and actively sending a heartbeat': 'actively sending a heartbeat'},
    'mq-activemq-storage-type-fixed-after-create': {"can't change the broker storage type after you create the broker": "can't change the broker storage type"},
    'mq-activemq-reboot-or-maintenance-causes-failover': {'Maintenance windows and broker reboots you initiate will cause a failover': 'broker reboots you initiate will cause a failover'},
    'step-functions-price-retry-extra-transition': {'each retry will be charged as an additional state transition': 'charged as an additional state transition'},
    'appflow-flow-sync-on-demand-or-schedule': {'keep data in sync across your SaaS applications and AWS services': 'keep data in sync'},
    'step-functions-eventbridge-standard-only-emit-events': {'monitor the execution of express workflows, you can use CloudWatch Logs': 'you can use CloudWatch Logs'},
    'mq-faq-vs-ec2-offload-operational-overhead': {'broker provisioning, security patching, setup, configuration, broker version upgrades, or recovery': 'broker provisioning, security patching, setup, configuration'},
    'mq-faq-cloudwatch-cloudtrail-monitoring-integrations': {'Log, continuously monitor, and retain Amazon MQ API calls': 'retain Amazon MQ API calls'},
    'appflow-schedule-full-or-incremental': {'transfers a snapshot of all records at the time of the flow run': 'a snapshot of all records',
                                             'only the records that have been added or changed since the last successful flow run': 'changed since the last successful flow run'},
    'mq-welcome-encryption-private-endpoint-iam': {'encryption of your messages at rest and in transit': 'messages at rest and in transit',
                                                   'restricted to a private endpoint within your Amazon VPC': 'a private endpoint within your Amazon VPC'},
    'step-functions-encryption-cost-owned-key-free-cmk-kms-charges': {'AWS KMS charges apply when using a customer managed key': 'AWS KMS charges apply'},
    'mq-rabbitmq-multiple-auth-methods-simultaneously': {'multiple authentication and authorization methods to be used simultaneously': 'methods to be used simultaneously'},
    'mq-rabbitmq-single-instance-nlb-stable-endpoint': {'one broker in one Availability Zone behind a Network Load Balancer': 'behind a Network Load Balancer (NLB)',
                                                        'broker endpoint remains unchanged if the broker instance is replaced': 'broker endpoint remains unchanged'},
    'mq-decision-guide-protocol-portability': {'Advanced Message Queuing Protocol (AMQP) or MQ Telemetry Transport (MQTT)': 'Advanced Message Queuing Protocol (AMQP)'},
    'appflow-price-flows-and-data-volume': {'the number of flows they run and the volume of data processed': 'the number of flows they run'},
    'step-functions-task-token-same-account-only': {"won't work if you send them from principals in a different AWS account": 'principals in a different AWS account'},
    'step-functions-wa-avoid-polling-loops-use-callback-or-sync': {'avoid the pattern of managing an asynchronous job by using a polling loop': 'using a polling loop',
                                                                   'prefer instead to use Callbacks or the .sync Service integration': 'use Callbacks or the .sync Service integration'},
    'step-functions-redrive-keeps-successful-steps': {'preserves the results and execution history of the successful steps': 'execution history of the successful steps',
                                                      'which are not rerun when you redrive an execution': 'not rerun when you redrive an execution'},
    'appflow-api-calls-count-against-saas-limits': {'API calls that Amazon AppFlow makes to data sources and destinations': 'makes to data sources and destinations'},
    'mq-crdr-switchover-consistency-over-availability': {'guaranteed to have identical state when this failover operation completes': 'guaranteed to have identical state'},
    'step-functions-activity-worker-outside': {'performed by a worker running outside of Step Functions': 'a worker running outside of Step Functions',
                                               'Amazon Elastic Compute Cloud (Amazon EC2), Amazon Elastic Container Service (Amazon ECS), or even mobile devices': 'or even mobile devices'},
    'mq-activemq-two-endpoints-failover-transport': {'connect to either endpoint by using the Failover Transport': 'either endpoint by using the Failover Transport'},
    'step-functions-map-vs-parallel': {'Dynamically iterate steps for each element of an input array': 'each element of an input array',
                                       'execute the same steps for multiple entries of an array': 'the same steps for multiple entries'},
    'step-functions-whitepaper-mwaa-for-open-source-portability': {'use Amazon MWAA if you prioritize open source and portability': 'prioritize open source and portability'},
    'appflow-catalog-output-in-glue-data-catalog': {'creates metadata tables in the AWS Glue Data Catalog': 'metadata tables in the AWS Glue Data Catalog',
                                                    "You don't have to use crawlers to populate the Data Catalog": "don't have to use crawlers"},
    'mq-rabbitmq-cluster-classic-mirroring-default-policy': {'sets the ha-mode to all and ha-sync-mode to automatic': 'ha-mode to all and ha-sync-mode to automatic'},
    'step-functions-vpc-interface-endpoint-no-igw-nat': {'without requiring an internet gateway, network address translation (NAT) instance, or VPN connection': 'without requiring an internet gateway'},
    'mq-rabbitmq-simple-auth-is-default': {'broker users are stored internally in the RabbitMQ broker': 'stored internally in the RabbitMQ broker'},
    'appflow-private-flows-use-privatelink': {'use AWS PrivateLink to route data over AWS infrastructure': 'route data over AWS infrastructure'},
    'mq-crdr-promote-from-replica-only': {'You cannot initiate switchover or failover on a primary broker': 'You cannot initiate switchover or failover',
                                          'promote the replica broker to the primary broker role': 'promote the replica broker'},
    'appflow-mapping-masking-filtering': {'A filter controls which data records are transferred to the destination': 'A filter controls which data records are transferred'},
    'mq-rabbitmq-cluster-maintenance-one-node-at-a-time': {'client connections to that node are severed and need to be re-established': 'client connections to that node are severed'},
    'mq-crdr-async-replication-primary-to-replica': {'the current replica broker is promoted to the primary broker role': 'the current replica broker is promoted'},
    'step-functions-pricing-additional-charges-for-integrated-services': {'additional charges if the operation of your application workflow utilizes other AWS services': 'utilizes other AWS services or transfers data',
                                                                         'billed for each request and for the duration of each Lambda function': 'the duration of each Lambda function'},
    'mq-rabbitmq-cluster-no-inter-node-encryption': {'RabbitMQ cluster replication traffic only transits your broker’s VPC': 'replication traffic only transits your broker’s VPC'},
    'appflow-faq-vs-datasync-bulk-versus-operational': {'bulk data migration, processing, and backup or disaster recovery': 'bulk data migration'},
    'step-functions-decision-guide-express-fit': {'IoT data ingestion, streaming transforms, and high-rate event processing': 'streaming transforms, and high-rate event processing'},
    'step-functions-activity-worker-polls-getactivitytask': {'any application that can make an HTTP connection, hosted anywhere': 'can make an HTTP connection, hosted anywhere'},
    'step-functions-welcome-states-workflows-executions': {'Each step in a workflow is called a state': 'step in a workflow is called a state'},
    'mq-activemq-active-standby-one-active-failover': {'only one of the broker instances is active at any time': 'only one of the broker instances is active'},
    'step-functions-lambda-guide-more-sophisticated-error-handling': {'Step Functions offers more sophisticated error handling for complex workflows': 'more sophisticated error handling for complex workflows',
                                                                      'use Catch to route errors to a fallback state': 'route errors to a fallback state'},
    'mq-activemq-no-vpc-endpoints-uses-eni': {'provisions an elastic network interface (ENI) in the VPC': 'an elastic network interface (ENI) in the VPC'},
    'step-functions-human-approval-pauses-until-user-approves': {'pause during a task, and wait for a user to respond to an email': 'a user to respond to an email',
                                                                 'progresses to the next state once the user has approved the task': 'once the user has approved the task'},
    'step-functions-http-task-connection-secret-in-secrets-manager': {'stores the connection and authorization parameters in an encrypted form': 'parameters in an encrypted form'},
    'step-functions-map-inline-mode': {"adds the execution history of these iterations to the parent workflow's execution history": "to the parent workflow's execution history"},
    'step-functions-state-pass-passes-input': {'filter, transform, and add fixed data into the output': 'add fixed data into the output'},
    'step-functions-lambda-guide-sfn-reduces-custom-orchestration-code': {'complex processes with multiple types of failure and retry logic': 'multiple types of failure and retry logic'},
    'appflow-faq-public-apis-managed-connector-replacement': {'manages the life-cycle of access tokens and API keys': 'life-cycle of access tokens and API keys'},
    'step-functions-pricing-distributed-map-transition-per-iteration': {'no state transition for starting each iteration when you use an Inline Map': 'no state transition for starting each iteration'},
    'mq-faq-cloudformation-iam-kms-integrations': {'Automate the process of creating, updating, and deleting message brokers': 'creating, updating, and deleting message brokers',
                                                   'Create and control keys used to encrypt your data': 'keys used to encrypt your data'},
    'mq-migration-without-interruption-may-reorder': {'might cause messages to be delivered out of order': 'messages to be delivered out of order'},
    'appflow-event-trigger-only-saas-with-change-events': {'available only for SaaS applications that provide change events': 'only for SaaS applications that provide change events',
                                                           'You must choose the event when you choose the source': 'choose the event when you choose the source'},
    'step-functions-one-query-language-per-state': {'cannot mix JSONPath and JSONata within a single step': 'cannot mix JSONPath and JSONata'},
    'appflow-three-trigger-types': {'in response to an event from a SaaS application': 'in response to an event'},
    'appflow-s3-same-region-no-cross-account': {'must be in the same AWS Region as your console and flow': 'same AWS Region as your console and flow'},
    'step-functions-faq-genai-prompt-chaining': {'choose the best model for each stage of the chain': 'best model for each stage of the chain'},
    'step-functions-history-standard-listable-express-unlimited-in-cwlogs': {'Executions can be inspected in CloudWatch Logs or the Step Functions console by enabling logging on your state machine': 'inspected in CloudWatch Logs'},
    'mq-whitepaper-preexisting-messaging-system-replacement': {'a good choice if you have a pre-existing messaging system': 'a pre-existing messaging system'},
    'appflow-faq-privacy-aws-managed-or-custom-keys-vpc-endpoints': {'AWS managed keys or bring your own custom keys': 'bring your own custom keys'},
    'appflow-s3-destination-key-choice-managed-or-customer': {'either an AWS managed CMK or a customer managed CMK': 'AWS managed CMK or a customer managed CMK',
                                                              'We recommend that you use a customer managed CMK': 'recommend that you use a customer managed CMK'},
    'step-functions-task-states-unit-of-work-other-service': {'a unit of work that another AWS service performs': 'unit of work that another AWS service performs'},
    'step-functions-express-console-logs-insights-scan-charges': {'a larger time range that includes more execution events': 'your costs will increase'},
    'mq-tls-required-activemq-and-rabbitmq': {'requires strong Transport Layer Security (TLS) encryption for all client connections': 'requires strong Transport Layer Security (TLS) encryption',
                                              'Amazon MQ for RabbitMQ': 'for all client connections'},
    'mq-rabbitmq-deployment-single-or-cluster': {'three RabbitMQ broker nodes behind a Network Load Balancer': 'three RabbitMQ broker nodes'},
    'mq-privatelink-only-for-api-not-brokers': {'only available for the Amazon MQ API endpoint, not the broker endpoint': 'only available for the Amazon MQ API endpoint',
                                                'private connectivity between virtual private clouds (VPCs) and the Amazon MQ API': 'not the broker endpoint'},
    'mq-rabbitmq-quorum-queues-survive-node-loss-across-azs': {'message delivery continues with the newly elected leader replica': 'continues with the newly elected leader replica'},
    'step-functions-wa-express-cheaper-for-high-throughput': {'Consider using Express Workflows for a high throughput system': 'Express Workflows for a high throughput system',
                                                              'more cost-efficient compared to Standard Workflows for the same level of throughput': 'more cost-efficient compared to Standard Workflows'},
    'mq-serverless-guide-standards-based-portability-cost': {'higher operational complexity and less tight integration with other AWS services': 'higher operational complexity'},
    'appflow-faq-run-on-schedule-event-or-demand': {'on a schedule, in response to a business event, or on demand': 'in response to a business event'},
    'step-functions-flow-states-choice-wait-map-parallel': {'Map states run child workflows for each item in a dataset': 'run child workflows for each item'},
    'appflow-case-save-the-children-spain-salesforce-ingestion': {'automated the ingestion of information from Salesforce and other sources': 'ingestion of information from Salesforce'},
    'step-functions-retry-maxdelayseconds-caps-interval': {'maximum value, in seconds, up to which a retry interval can increase': 'up to which a retry interval can increase'},
    'mq-rabbitmq-migration-export-import-definitions': {'export the configuration from your self-managed RabbitMQ cluster and import it into Amazon MQ for RabbitMQ': 'export the configuration'},
    'mq-rabbitmq-cluster-az-outage-relocates-nodes': {'automatically attempt to relocate the affected RabbitMQ nodes to a different AZ': 'affected RabbitMQ nodes to a different AZ'},
    'step-functions-bp-no-default-timeout-stuck-execution': {'stuck waiting for a response that will never come': 'a response that will never come'},
    'mq-activemq-user-changes-need-reboot-or-window': {'does not apply the changes to the user immediately': 'not apply the changes to the user immediately',
                                                       'wait for the next maintenance window or reboot the broker': 'next maintenance window or reboot the broker'},
    'step-functions-async-express-same-name-concurrent': {'Starting multiple workflows with the same name results in concurrent executions': 'results in concurrent executions'},
    'step-functions-state-map-iterates-items': {'run a set of workflow steps for each item in a dataset': 'workflow steps for each item in a dataset',
                                                'a JSON array, a list of Amazon S3 objects, or a CSV file': 'a list of Amazon S3 objects'},
    'mq-case-shgardi-amazon-mq-microservices': {'allows diverse applications on various platforms to communicate and exchange information': 'diverse applications on various platforms'},
    'appflow-private-flow-metadata-calls-use-public-endpoints': {'the actual data transfer during the flow run happens over Amazon VPC endpoints': 'happens over Amazon VPC endpoints',
                                                                 'metadata API calls to populate a list of objects and fields in the console over the public endpoints': 'in the console over the public endpoints'},
    'mq-faq-activemq-version-may-end-without-notice': {'prevent the creation of new brokers with these versions': 'prevent the creation of new brokers'},
    'mq-faq-network-of-brokers-own-store-single-broker-holds-message': {'stored by a single broker at any given time': 'stored by a single broker'},
    'step-functions-variables-store-data-across-steps': {'store data in a step and retrieve that data in future steps': 'retrieve that data in future steps',
                                                         'state output can only be used as input to the very next step': 'input to the very next step'},
    'step-functions-iam-role-required-for-access': {'grant Step Functions access to those resources by using an IAM role': 'by using an IAM role'},
    'mq-maintenance-ha-minimizes-downtime': {'maintenance operations one instance at a time, and at least one instance remains available': 'at least one instance remains available'},
    'step-functions-faq-cloudtrail-captures-api-calls': {'captures all API calls for Step Functions as events': 'captures all API calls for Step Functions'},
    'step-functions-workflow-type-immutable': {'can not be updated after you create a state machine': 'can not be updated after you create'},
    'step-functions-redrive-same-definition-and-arn': {'use the same state machine definition and execution ARN': 'same state machine definition and execution ARN',
                                                       'you must start a new execution if you update your state machine definition': 'you must start a new execution'},
    'step-functions-decision-guide-lambda-15-minutes-and-distributed-map': {'Lambda durable functions checkpoint progress and resume across invocations': 'checkpoint progress and resume across invocations',
                                                                            'Distributed Map can process millions of items from Amazon S3, Athena, or JSON in parallel': 'can process millions of items from Amazon S3'},
    'step-functions-sync-express-api-gateway-microservices-decision-guide': {'Amazon API Gateway Gateway for routing requests': 'AWS Lambda for compute'},
    'step-functions-console-logging-default-by-type': {'will not be configured to send logs to CloudWatch Logs': 'will not be configured to send logs',
                                                       'by default be configured to send logs to CloudWatch Logs': 'by default be configured to send logs'},
    'step-functions-error-default-fails-execution': {'failing the entire state machine execution': 'catch errors, retry failed states'},
    'step-functions-use-case-human-in-the-loop': {'include human approval steps in the workflow': 'include human approval steps in the workflow',
                                                  'a callback and a task token': 'Human in the loop'},
}
ADD_VALUES = {
    'appflow-price-flows-and-data-volume': [{'key': 'volume', 'display': 'the volume of data processed'}],
    'step-functions-history-standard-listable-express-unlimited-in-cwlogs': [{'key': 'express-unlimited', 'display': 'Unlimited execution history'}],
}
CLAIMS = {
    'step-functions-use-case-human-in-the-loop': 'Step Functions can include human approval steps in the workflow (human in the loop).',
}
EXTRA = {
    'step-functions-bp-migrate-standard-to-express-requirements': {
        'evidence_add': {'source_id': 'docs/step-functions/latest/dg/sfn-best-practices',
                         'url': 'https://docs.aws.amazon.com/step-functions/latest/dg/sfn-best-practices.html',
                         'quote': 'Your workflow conforms to an at-least-once execution model, which means each step in the workflow may run more than exactly once.',
                         'insert_at': 2}},
    'mq-welcome-migrate-without-rewriting-messaging-code': {'qualifiers': {'scope': 'Amazon MQ', 'default_or_max': '', 'adjustable': False, 'condition': ''}},
    'step-functions-decision-workflows-category': {'qualifiers': {'scope': 'integration decision guide, workflows category (Step Functions and Amazon MWAA)', 'default_or_max': '', 'adjustable': False, 'condition': ''}},
}

problems, written = [], []


def check(fid, disp, quotes):
    if re.search(r'\d', disp):
        return
    if len(disp.split()) > 8:
        problems.append('%s: over 8 words: %s' % (fid, disp))
    if not any(norm(disp) in q for q in quotes):
        problems.append('%s: not in a quote: %s' % (fid, disp))


ids = set(D) | set(ADD_VALUES) | set(CLAIMS) | set(EXTRA)
for fid in sorted(ids):
    f = facts.get(fid)
    if f is None or f['status'] in ('rejected', 'superseded') or fid in SUP_IDS:
        problems.append('%s: missing, not live, or superseded' % fid)
        continue
    patch = {}
    quotes = [norm(e['quote']) for e in f['evidence']]
    if fid in D or fid in ADD_VALUES:
        vals = []
        olds = {v['display'] for v in f['values']}
        for o in D.get(fid, {}):
            if o not in olds:
                problems.append('%s: old display not found: %s' % (fid, o))
        for v in f['values']:
            nd = D.get(fid, {}).get(v['display'], v['display'])
            if nd is None:
                continue
            vals.append(dict(v, display=nd))
        vals += ADD_VALUES.get(fid, [])
        if len({v['display'] for v in vals}) != len(vals):
            problems.append('%s: duplicate displays' % fid)
        patch['values'] = vals
    if fid in CLAIMS:
        patch['claim'] = CLAIMS[fid]
    if fid in EXTRA:
        ex = copy.deepcopy(EXTRA[fid])
        if 'evidence_add' in ex:
            ea = ex.pop('evidence_add')
            ev = [{k: e.get(k) for k in ('source_id', 'url', 'quote', 'table_header') if k in e} for e in f['evidence']]
            for e, src in zip(ev, f['evidence']):
                if src.get('heading'):
                    e['heading'] = src['heading']
            pos = ea.pop('insert_at', len(ev))
            ev.insert(pos, {'source_id': ea['source_id'], 'url': ea['url'], 'quote': ea['quote'], 'table_header': None})
            patch['evidence'] = ev
            quotes.append(norm(ea['quote']))
        patch.update(ex)
    for v in patch.get('values', f['values']):
        check(fid, v['display'], quotes + [norm(patch.get('claim', ''))] if fid in CLAIMS else quotes)
    with open(os.path.join(OUT, fid + '.json'), 'w', encoding='utf-8') as o:
        json.dump(patch, o, ensure_ascii=False, indent=1)
    written.append(fid)

# remaining long displays in live facts not touched
for fid, f in facts.items():
    if f['status'] in ('rejected', 'superseded') or fid in SUP_IDS or fid in ids or f.get('home_chapter') != '32':
        continue
    for v in f['values']:
        if not re.search(r'\d', v['display']) and len(v['display'].split()) > 8:
            problems.append('%s: untouched long display: %s' % (fid, v['display']))

json.dump({'patch_ids': written, 'supersede': SUPERSEDE}, open(os.path.join(HERE, 'reg-decisions.json'), 'w'), indent=1)
for p in problems:
    print('PROBLEM', p)
print('patches', len(written), 'supersede', len(SUPERSEDE))
