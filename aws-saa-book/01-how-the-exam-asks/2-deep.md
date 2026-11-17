---
chapter: "01"
file: deep
title: Exam English in depth
status: ready
updated: 2026-10-12
---

# Exam English in depth

## The nine word groups (18 min)
<!-- section: role=method; route=full; minutes=18 -->

Each group answers one question about the stem. The paragraph names the group's twin: two phrases that look alike but lead to different answers.

### Optimisation qualifiers (2 min)

The qualifiers MOST secure, MOST resilient and MOST cost-effective echo the domain names, because the exam validates architectures that are [secure, resilient, high-performing, and cost-optimized](../facts/exam.md#exam-candidate-tasks). The qualifier does not tell you the domain, though: a security question often asks for LEAST operational overhead.

The classic twin is highly available against fault tolerant. The exam guide names them together, as [a highly available and/or fault-tolerant architecture across AWS Regions or Availability Zones](../facts/exam.md#exam-guide-highly-available-fault-tolerant-wording).

This book reads them as two strengths. **High availability** (hy uh-vayl-uh-BIL-ih-tee) accepts a short interruption, so automatic failover to a second copy is enough. **Fault tolerance** (FAWLT TOL-er-uns) accepts none, so spare capacity is already running and takes the load without a pause. The interruption that the stem accepts decides, not the label.

<!-- exam-english:start group=qualifiers -->

<!-- table: exam-english -->
| Word | Meaning | It signals |
|---|---|---|
| MOST cost-effective | the cheapest option that still meets every requirement | first reject every option that fails a requirement, then pick the cheapest of the rest |
| LEAST operational overhead | the team does the least work to run it | a managed or serverless feature, not scripts or software on instances |
| MOST secure | the strongest protection among options that work | least privilege, temporary credentials and private access, even when another option is cheaper |
| highly available | it keeps working when one part fails; this book: a short interruption is acceptable | more than one Availability Zone, a load balancer or automatic failover |
| fault tolerant | it keeps working when one part fails; this book: with no interruption | stronger than highly available in this book: spare capacity is already running |
| MOST resilient | it recovers from failure best | remove single points of failure and automate recovery |
| LOWEST latency | the shortest wait for a response | move data or compute closer to the user: caching, edge services, the nearest Region |
| MOST operationally efficient | it meets the need with the least ongoing work and fewest moving parts | a built-in feature of the service, not a custom solution |
| LEAST development effort | the developers write or change the least code | a configuration change or a compatible managed service, not a redesign |
| scalable | it can handle more load when the load grows | automatic scaling or a service that scales without capacity planning |

<!-- exam-english:end -->

<details>
<summary>Go deeper: the qualifiers are the exam guide's own words</summary>

The exam guide uses the qualifier words in its list of skills. For example, the cost domain lists [selecting the most cost-effective storage service for a workload](../facts/exam.md#exam-guide-cost-effective-wording). So for each skill of the guide, ask which qualifier it serves.

</details>

### Workload shape (2 min)

These words describe the load over time, and the shape chooses the pricing model and the scaling style. The guide names design principles for [stateless workloads compared with stateful workloads](../facts/exam.md#exam-guide-serverless-stateless-wording). In a stateless tier, any instance can serve any request, so instances can come and go.

The classic twin is steady-state against unpredictable or spiky. Steady-state points to a commitment discount or provisioned capacity. Unpredictable points to automatic scaling, or to a queue as a buffer. Swap them, and you pay for idle capacity or run out at the peak.

<!-- exam-english:start group=workload-shape -->

<!-- table: exam-english -->
| Word | Meaning | It signals |
|---|---|---|
| sporadic | sometimes, not regularly | pay per use; not instances that run all the time |
| intermittent | it starts and stops, with pauses between | capacity that can pause or scale to zero; pay per use |
| unpredictable | you cannot plan the load | automatic scaling, on-demand capacity, or a queue as a buffer |
| spiky | the load jumps up quickly for a short time | a buffer in front of slow parts, and scaling that reacts fast |
| steady-state | the same load all the time | a commitment discount or provisioned capacity |
| predictable | you know the load in advance | scheduled scaling or a commitment; no need for the most flexible option |
| long-running | one job runs for a long time | check the maximum run time of the compute option; containers or instances fit long jobs |
| short-lived | each job finishes quickly | functions that start on an event |
| stateless | the application keeps no memory between requests | any instance can serve any request, so instances can be added, removed or interrupted |
| can tolerate interruption | stopping the work and starting it again is acceptable | spare capacity at a discount that AWS can take back |

<!-- exam-english:end -->

### Strength of requirement (2 min)

These words say how hard a requirement is. Hard words (must, mandates, ensure, stringent) remove options, at any price. Soft words (acceptable, sufficient, at a minimum) relax a requirement and let a cheaper or simpler option back in.

The classic twin is must against acceptable. "Internet access must continue if one Availability Zone fails" and "an interruption is acceptable" give different answers with the same four options.

<!-- exam-english:start group=requirement-strength -->

<!-- table: exam-english -->
| Word | Meaning | It signals |
|---|---|---|
| must | it is a hard requirement | an option that does not meet it is wrong, even if the option is cheaper or easier |
| stringent | very demanding | the strongest control, not the cheapest |
| mandates | a rule from outside the team requires it | treat it as a hard constraint, and prefer a control that enforces it centrally |
| ensure | make it certain | a hard requirement; if an action must not happen, prevent it, not only alert |
| mission-critical | the business stops if it fails | pay for availability and fast recovery; the cheapest design is probably wrong |
| acceptable | the business allows it | a relaxed requirement: a cheaper or simpler option is now allowed |
| at a minimum | this much or more | a lower limit: check that capacity or retention never falls below it |
| wants to avoid | the company does not accept this | remove every option that includes the unwanted thing |
| sufficient | enough for the need | do not choose more than is needed; the larger option costs more |
| as soon as possible | with the shortest delay | the fastest option that meets the other constraints; watch the transfer or retrieval time |

<!-- exam-english:end -->

### Data and time (2 min)

These words set how fresh the data must be, how safe it must stay and how fast it must come back. The guide asks for [designing appropriate backup and retention policies (for example, snapshot frequency)](../facts/exam.md#exam-guide-backup-retention-wording).

The classic twin is real-time against near real-time. This is a reading rule of this book, not AWS terminology.

Real-time allows no noticeable delay. Near real-time accepts a short delay, so a delivery service that buffers the data can be enough. Read the delay that the stem accepts, not the label.

<!-- exam-english:start group=data-and-time -->

<!-- table: exam-english -->
| Word | Meaning | It signals |
|---|---|---|
| real-time | with no noticeable delay | the smallest delay; a reading rule of this book, compare with near real-time |
| near real-time | a short delay is acceptable | a short delay is allowed, so a service that buffers data can fit |
| infrequently accessed | people read the data only sometimes | a cheaper storage class; check the retrieval charge and how fast a read must be |
| immutable | nobody can change or delete the data | a lock that prevents changes, not only versioning |
| retain | keep the data for a set time | lifecycle rules and retention settings; count the required period |
| archive | store data for a long time and read it almost never | the coldest storage that still meets the retrieval time in the stem |
| durable | the data is not lost | storage that keeps copies in several places; durability is not the same as availability |
| point in time | the state of the data at one exact moment | continuous backups or snapshots; check how far back and how exact |
| eventually | after some time, not maybe | a short delay before all readers see a change is acceptable |
| transactional | several changes succeed together or fail together | a database with ACID transactions: a relational engine, or Amazon DynamoDB transactions |

<!-- exam-english:end -->

<details>
<summary>Go deeper: recovery objectives in AWS's own words</summary>

The **recovery point objective** (RPO) is the [maximum acceptable amount of time since the last data recovery point](../facts/well-architected.md#well-architected-rpo-definition). It sets how much data the business can lose. The **recovery time objective** (RTO) is the [maximum acceptable delay between the interruption of service and restoration of service](../facts/well-architected.md#well-architected-rto-definition). It sets how long the business can be down.

The guide names both with four strategies: [backup and restore, pilot light, warm standby, active-active failover](../facts/exam.md#exam-guide-disaster-recovery-rpo-rto-wording). A small RPO asks for frequent copies. A small RTO asks for capacity that is ready.

</details>

### Operations (2 min)

These words name work that the team wants to give away. The classic twin is fully managed against provision. Fully managed means AWS does the operating work. Provision means you choose and size capacity in advance, and you pay for that capacity.

Patching shows what fully managed takes away. On multi-tenant managed services such as Amazon DynamoDB and Amazon S3, the AWS responsibility is to [apply patches without requiring customer action](../facts/well-architected.md#well-architected-multi-tenant-managed-services-aws-patches-without-customer-action).

The table also holds decouple. The guide's phrase for it is [decoupling workloads so that components can scale independently](../facts/exam.md#exam-guide-loose-coupling-decoupling-wording).

<!-- exam-english:start group=operations -->

<!-- table: exam-english -->
| Word | Meaning | It signals |
|---|---|---|
| fully managed | AWS does the operating work | choose the AWS service over the same software installed on instances |
| serverless | no servers for the team to manage or size | functions, managed containers without instances, and on-demand data services |
| provision | create and size a resource in advance | provisioned means capacity you choose and pay for; the opposite is on-demand |
| patch | install software fixes | work the team wants to give away: a managed service, or an automated patch tool |
| automate | make it happen without a person | a built-in schedule, rule or policy, not a manual runbook |
| decouple | separate two parts so one keeps working when the other is slow or fails | a queue, a topic or an event bus between the parts |
| orchestrate | run several steps in order, with retries and decisions | a workflow service, not code that calls each step by hand |
| centrally manage | control many accounts or resources from one place | an organization-wide service or policy, not a setting repeated in each account |
| monitor | watch and be told when something happens | metrics and alarms for performance; an audit trail for who did what |
| a small team | few people run the system | the same as least operational overhead: prefer managed services |

<!-- exam-english:end -->

### Security (2 min)

These words say who can reach what, and where the data is protected. The guide asks for practices such as [multi-factor authentication [MFA]](../facts/exam.md#exam-guide-least-privilege-mfa-wording) and for [determining when to federate a directory service with IAM roles](../facts/exam.md#exam-guide-federate-cross-account-wording). Secure is your weakest domain, so read these ten words twice.

The classic twin is at rest against in transit, and the guide lists them as two skills. One is [encrypting data at rest (for example, AWS KMS)](../facts/exam.md#exam-guide-encryption-at-rest-in-transit-wording). The other is [encrypting data in transit (for example, AWS Certificate Manager [ACM] using TLS)](../facts/exam.md#exam-guide-encryption-at-rest-in-transit-wording). Protecting the stored copy does nothing for the data on the network.

<!-- exam-english:start group=security -->

<!-- table: exam-english -->
| Word | Meaning | It signals |
|---|---|---|
| least privilege | only the permissions that the task needs | a narrow policy on a role; never broad permissions or shared credentials |
| at rest | while the data is stored | storage encryption with a key service; check who must control the key |
| in transit | while the data moves over a network | TLS and certificates; check whether requests that are not encrypted must be refused |
| rotate | replace a key or a password with a new one on a schedule | a secrets service with built-in rotation, not a script |
| audit | keep a record of who did what and when | the API activity trail and the configuration history, not performance metrics |
| restrict | allow only some people or networks | a policy condition, a resource-based policy or a network rule that names what is allowed |
| sensitive | data that causes harm if other people see it | encryption, tight access, and a service that discovers such data |
| isolate | keep apart so that one cannot reach the other | separate accounts, VPCs, subnets or security groups, by how strong the isolation must be |
| temporary | it stops working after a set time | roles and temporary credentials, or a time-limited link; never long-term keys |
| manages its own keys | the company, not AWS, controls the encryption keys | customer managed keys in a key service; check who must control rotation |

<!-- exam-english:end -->

### Location and network (2 min)

These words say where the users, the data and the traffic are. The guide asks for [creating a network topology for various architectures (for example, global, hybrid, multi-tier)](../facts/exam.md#exam-guide-global-hybrid-topology-wording).

The classic twin is across multiple Availability Zones against cross-Region. More zones protect against the failure of one zone. A second Region protects against the loss of a Region, and it costs more. Read which failure the stem names.

<!-- exam-english:start group=location-network -->

<!-- table: exam-english -->
| Word | Meaning | It signals |
|---|---|---|
| on premises | in the company's own data center, not in AWS | a hybrid question: think about the network link, the transfer tool and where identities live |
| hybrid | AWS and the data center work together | private connectivity, and services that extend AWS storage or identity to the data center |
| privately | the traffic stays off the public internet | VPC endpoints inside AWS; a dedicated or private link from outside |
| internet-facing | users on the internet reach it directly | a public entry point with protection in front; the tiers behind it stay private |
| users around the world | users are far from one Region | edge caching, global routing or more than one Region |
| across multiple Availability Zones | copies or capacity in more than one zone of one Region | protection against a zone failure; not protection against a Region failure |
| cross-Region | between two Regions | disaster recovery or global users; replication features and their cost |
| dedicated connection | a private network line that only this company uses | a dedicated physical link, compared with a VPN that runs over the internet |
| edge | at AWS sites near the users | content delivery and protection before traffic reaches the Region |
| data residency | the law says where the data is stored | keep data and backups in the named Region; reject options that copy data elsewhere |

<!-- exam-english:end -->

<details>
<summary>Go deeper: a zone is not a Region</summary>

[Deploying your workload across multiple Availability Zones in an AWS Region is part of a high availability strategy](../facts/well-architected.md#well-architected-multi-az-is-ha-and-dr-multi-region-active-passive). Each Region is [designed to be isolated from the other Regions](../facts/global-infrastructure.md#global-infrastructure-region-isolated-for-fault-tolerance), so a second Region answers a Region outage.

AWS also says that [most customers can achieve their resilience goals in a single Region](../facts/global-infrastructure.md#global-infrastructure-most-customers-single-region-suffices). When the stem names only a zone failure, a second Region still works, and a cost or effort qualifier removes it.

</details>

### Change and migration (2 min)

These words set how much the application can change. The guide names the strict case: services that improve reliability [when application changes are not possible](../facts/exam.md#exam-guide-legacy-no-changes-wording).

The classic twin is without changing the application against minimal code changes. The first allows configuration changes only. The second allows a small edit, but not a rewrite. For databases, the guide names [heterogeneous migrations, homogeneous migrations](../facts/exam.md#exam-guide-migration-data-transfer-wording): a different engine at the target, or the same engine.

<!-- exam-english:start group=change-migration -->

<!-- table: exam-english -->
| Word | Meaning | It signals |
|---|---|---|
| migrate | move an application or data to AWS | find the size, the time limit and the network link; they decide the tool |
| lift and shift | move the application without changing it | instances and a rehosting tool, not a new serverless design |
| without changing the application | keep the code as it is | a compatible managed service or a change in configuration, not a redesign |
| minimal code changes | small code changes are acceptable | a service with a compatible interface; reject a full rewrite |
| refactor | change the design of the application | the stem allows new services such as functions, queues or containers |
| legacy | an old system that is hard to change | keep its protocols and interfaces; prefer services that support them |
| monolithic | one large application where all parts depend on each other | a question about splitting it or decoupling its parts |
| minimal downtime | the system stops for a very short time or not at all | replication before the switch, not a backup and restore |
| ongoing replication | changes keep flowing from the source to the target | a replication or change-data-capture feature, not a one-time copy |
| one-time | it happens once | no need for a permanent link or service; compare transfer time with a shipped device |

<!-- exam-english:end -->

### Instruction grammar (2 min)

These phrases frame the question and say what kind of answer to give. The instruction is to [select one or more responses that best complete the statement or answer the question](../facts/exam.md#exam-select-best-response-instruction). The classic twin is "(Select TWO.)" against "Which combination of steps". The first sets how many options to mark; the second adds that they work together.

The exam guide calls the wrong options distractors: [response options that a candidate with incomplete knowledge or skill might choose](../facts/exam.md#exam-distractor-definition). This book sorts them into six types, so that you can name the type:

1. It works, but it loses on the qualifier.
2. A similar service or feature, the sibling of the right one.
3. The right service, configured wrongly.
4. A solution to a different problem.
5. A word from the stem, with nothing behind it.
6. A feature that does not exist.

<!-- exam-english:start group=instruction-grammar -->

<!-- table: exam-english -->
| Word | Meaning | It signals |
|---|---|---|
| Which solution will meet these requirements? | choose the one option that satisfies every requirement in the stem | list the requirements first; an option that misses one requirement is wrong |
| these requirements | all the needs stated before the question | go back and count them; there are often two or three |
| (Select TWO.) | exactly that number of options are correct | judge each option as true or false on its own, then count that you marked the right number |
| Which combination of steps | the correct options work together as one solution | the chosen options must not conflict; often one is the service and one is its configuration |
| MOST or LEAST in capitals | often more than one option works; rank the options that work | the capital word names the ranking rule; find it before reading the options |
| BEST | the option that fits the stated requirements most completely | several options are possible; the stem's constraints decide, not your preference |
| currently | how the system is now | the starting point; the answer changes as little of it as the requirements allow |
| wants to | the goal of the company | the sentence with this phrase usually holds the requirement |
| needs to | a requirement, as strong as must | treat it as a hard constraint |
| However | a problem or a change follows | the sentence after it describes what is wrong; the answer fixes that one thing |

<!-- exam-english:end -->

> **Exam trap:** The newest feature is not the answer because it is new. A feature must be [generally available for 3 months](../facts/exam.md#exam-new-feature-wait) before it appears on an exam. Judge it against the requirements like any other option. <!-- trap: how-the-exam-asks-trap-newest-feature-wins -->

<details>
<summary>Go deeper: a question that seems out of date</summary>

When a service or feature changes, AWS will [replace exam questions determined to be impacted by the change](../facts/exam.md#exam-changed-service-questions-replaced). If a question still seems affected, AWS says to [choose the best available answer from the options in the question](../facts/exam.md#exam-choose-best-available-answer). Then pick the option that meets the stem as written.

</details>

## Words customers say (1 min)
<!-- section: role=method; route=full; minutes=1 -->

Founders use these words on calls. The exam and this book use other words for the same ideas. Each item gives the customer word, then the words to listen for in a stem.

- spin up: launch an instance, or create a resource.
- **lift and shift**: rehost; "migrate without changing the application".
- **blast radius** (BLAST RAY-dee-us): how far one failure or one mistake reaches; "isolate", "limit the impact", separate accounts.
- noisy neighbor: another workload on shared hardware that slows yours down; "consistent performance", "dedicated".
- guardrails: rules that limit what every account can do; "centrally manage", "restrict", "prevent".
- break-glass: emergency access for when normal sign-in fails; "emergency access", "audit".
- **cold start**: the delay when a function needs a new execution environment for a request; "latency", "initialization".
- landing zone: a prepared multi-account environment with baseline rules; "multi-account", "centrally manage".

## Confusable words (2 min)
<!-- section: role=method; route=full; minutes=2 -->

Look-alike pairs:

- Durable or available: **durability** (dyoor-uh-BIL-ih-tee) means the data is not lost; availability is the [percentage of time that a workload is available for use](../facts/well-architected.md#well-architected-availability-definition).
- **Scale up** means a larger instance; **scale out** means more instances.
- **Terminate** (TER-mih-nayt) or stop: terminate deletes the instance; stop shuts it down, which is not a pause.
- A **principal** (PRIN-sih-pul) makes a request; its sound-alike ending in -ple means a rule.
- Route or root: a route is a path in a route table; root often means the root user.
- Root user or organization root: one identity in one account, or the top of AWS Organizations, above all accounts.
- Affect or Effect: affect means to change; Effect is Allow or Deny in a policy.

Three pairs hide a trap:

- **Wrong belief:** Highly available and fault tolerant mean the same. **Truth:** The guide names both, in [a highly available and/or fault-tolerant architecture across AWS Regions or Availability Zones](../facts/exam.md#exam-guide-highly-available-fault-tolerant-wording). This book reads fault tolerant as the stronger one, but the stem decides. <!-- trap: how-the-exam-asks-trap-ha-equals-ft -->
- **Wrong belief:** "Eventually" means "maybe". **Truth:** It means after some time. An IAM change [can take some time](../facts/iam.md#iam-eventually-consistent-changes-replicate) to replicate: IAM is **eventually consistent** (ih-VEN-choo-uh-lee). <!-- trap: how-the-exam-asks-trap-eventually-means-maybe -->
- **Wrong belief:** Multi-AZ also survives a Region outage. **Truth:** Each Region is [designed to be isolated from the other Regions](../facts/global-infrastructure.md#global-infrastructure-region-isolated-for-fault-tolerance), so a Region outage needs a second Region. <!-- trap: how-the-exam-asks-trap-multi-az-covers-region -->
