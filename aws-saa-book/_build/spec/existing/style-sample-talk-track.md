# Amazon Bedrock: the talk track

*One spoken paragraph per topic, in the order you would explain them on a call. Facts match the [full briefing](bedrock-briefing.md), fetched from AWS pages on 2026-09-14.*

1. What Bedrock is

Bedrock is one AWS service that puts more than a hundred models from nineteen providers behind one set of AWS APIs. Anthropic, OpenAI, Meta, Mistral, DeepSeek, Qwen, Google's Gemma, Amazon's own Nova, and so on. You never run a GPU, you pay per token, and you get everything you already trust around it: IAM, CloudTrail, KMS, PrivateLink. The thing to understand first is that Bedrock is not a proxy. OpenAI and Anthropic handed the model weights to AWS, the models run on AWS hardware in accounts the providers cannot log into, and your request never leaves AWS. Almost every other question on this list follows from that one fact.

2. The two endpoints

There are two front doors and one engine behind both. `bedrock-runtime` is the one you recommend: it speaks every API, it has Guardrails, cross-Region routing and invocation logging. `bedrock-mantle` is a second surface on the same engine that only speaks the OpenAI and Anthropic shapes, and it exists for a few extras: AWS web search, long-running background requests, and Projects, which let you give each application its own retention policy and cost line. Same price per token on both. Two things people get wrong: mantle is not a different or less secure engine, AWS says so in the docs; and a handful of models, Gemma 4, GPT-5.4, GPT-5.5, the Mythos previews, only exist on mantle.

3. The APIs

Four ways to talk to a model. Converse is the AWS-native one, one request shape for every text model, and it is the only place Guardrails work on GPT. The OpenAI-compatible APIs, Chat Completions and Responses, mean you take an existing OpenAI codebase, change the base URL and the key, and it runs on Bedrock. The Anthropic Messages API does the same for Claude code. And InvokeModel is the raw provider format underneath. The catch is that each model supports a subset. Claude is never on the OpenAI APIs, GPT is never on the Anthropic one, and the Responses API is basically OpenAI and Grok only. If someone asks "which one do we standardize on", the answer is Converse for breadth, or whichever SDK they already have.

4. Zero operator access

The security headline is zero operator access. No AWS employee can read a prompt or a completion, not because of policy but because there is no way in: no SSH, no Session Manager, no serial console installed anywhere in the inference fleet. Software updates have to be signed, the machines attest their own configuration, and the connection is encrypted all the way to the model. The AWS VP who designed it wrote it up in a blog you can send. And separately from that, the model providers have no access to the accounts their models run in, so they cannot see prompts or logs either. Nobody trains on anything. That sentence is in the FAQ verbatim.

5. Data retention

By default Bedrock stores nothing. The nuance since this year is that retention is now a mode, not a slogan. You set a mode per account or per Project: `none` means zero retention, `default` means the model's own policy, which for nearly every model is still zero, and `aws_review` means you allow AWS to keep data and have humans look at flagged items. The clever part is that the mode is a ceiling, not a floor: setting `aws_review` does not make Opus or Nova traffic get retained, because those models declare that they allow zero and nothing is kept. And you can enforce all of this with a Service Control Policy, so nobody in the organization can ever set anything but `none`. Two traps: there is no console screen for this, it is API only; and the Responses API has its own separate `store` flag that keeps conversations thirty days unless you turn it off.

6. The models that require retention

Two model families break the zero-retention default, and it is the provider's condition, not AWS's. Claude Fable 5 and 5.1: every request is kept for thirty days inside AWS for automated abuse detection, and anything a classifier flags may be reviewed by AWS staff. You have to opt in to `aws_review` before the model even appears as available. The newest OpenAI models, GPT-6 Astra and the 5.6 family: only flagged traffic is kept, also thirty days, automated only. In both cases the data stays in AWS and the provider never receives it. Everything older, Opus 4.8, Sonnet 5, Opus 5, is untouched; AWS says so in a boxed note. If a customer needs Fable and zero retention, that is a per-account, per-model conversation with the account team and, for Claude, with Anthropic.

7. Abuse monitoring

Abuse monitoring is automated, runs inside AWS, and for almost every model keeps nothing. It looks for violations of AWS's or the provider's terms. Humans at AWS look only at flagged Fable traffic, and only because Anthropic requires it. There is one absolute exception, and you should say it before the customer finds it: child sexual abuse material. Image inputs are hash-matched, a hit is blocked with a 400 error, and AWS may keep and review that content and report it, regardless of what retention mode you set. Practical point: if a classifier flags an account, AWS emails the account contact and can suspend access if nobody answers, so keep those contacts monitored.

8. Cross-Region inference

Most of the new flagship models do not have an in-Region model ID any more. You call an inference profile instead: `us.` routes anywhere in the US, `eu.` anywhere in the EU, and `global.` anywhere in the world for roughly ten percent less. Data stays on the AWS network and encrypted, and the geographic ones never leave their geography, so residency is fine as long as you avoid `global.`. One detail that matters for the retention conversation: whatever is kept for abuse detection is stored in the Region that processed the request, not the one you called. And Fable 5.1 today has only US and global profiles, no EU one yet.

9. Model access

Model access flipped this year: every model is enabled by default in every commercial Region. The first time you call a third-party model, Bedrock quietly creates the Marketplace subscription and accepts the licence agreement for you. That is convenient and it is also the trap. If legal wants to read the EULA first, you have to block the model with an IAM deny on InvokeModel; denying the Marketplace subscribe permission does nothing, and Amazon, Meta, Mistral, DeepSeek and Qwen models are not even sold through Marketplace. Anthropic still wants a one-time use-case form per account on the runtime endpoint. And models retire: legacy ones take no new customers, and an account that goes quiet for fifteen days can lose access.

10. Quotas and throughput

Access and throughput are two different things, and customers mix them up. Access is on by default. Throughput is a quota, per model, per Region, and every new model arrives with a default one already attached, so the day GPT-6 or Fable 5.1 launches you can call it, but only up to that default. On the runtime endpoint the quota is tokens per minute, input and output added together, shared across every API you use for that model, plus a tokens-per-day cap that is simply the per-minute number times the minutes in a day, and for some models a requests-per-minute limit too. New accounts get reduced defaults, and AWS says increases go first to customers who are already consuming what they have, so "raise it before we generate traffic" usually gets denied. You raise it in Service Quotas, and one ticket covers the in-Region, cross-Region and daily quotas together. Two more traps: AWS will not raise quotas on a legacy model, and the mantle endpoint has its own separate quota pool, input and output counted separately, no RPM at all, most models with no published number yet, and increases go through a Support case rather than Service Quotas. Beyond quotas there are the service tiers, priority for speed, flex for cheaper off-peak, and reserved dedicated throughput through the account team.

11. Open-weight models and Marketplace

The open-weight story is better than it was and still behind. In February and March AWS added Qwen3, GLM 5, Kimi K2.5, DeepSeek V3.2 and MiniMax M2.5, then Gemma 4 in June, all serverless, all under Bedrock's terms. The problem is that every one of those labs has shipped a new flagship since July, GLM-5.3, Kimi K3, Qwen3.8, DeepSeek V4, and none of those are in the catalog. Phi, Granite and Falcon were never serverless at all. The honest answer is: the serverless catalog lags six to twelve weeks. If you need the newest one today, you deploy it yourself through Bedrock Marketplace or SageMaker JumpStart on a SageMaker endpoint, and you accept that it is outside Bedrock's compliance scope and outside the zero-retention, zero-operator story.

12. Compliance and AWS Artifact

Bedrock is HIPAA eligible, in scope for SOC 1, 2 and 3, PCI, the ISO 27000 family, ISO 42001 which is the AI management standard AWS was first to get, FedRAMP Moderate and High, HITRUST, IRAP and the German C5. Eligible is not compliant, though. The customer accepts the Business Associate Addendum in AWS Artifact, once per account or once for the whole Organization from the management account, keeps PHI in eligible services, encrypts with their own KMS keys, uses PrivateLink, and remembers that if they turn on invocation logging, the PHI lands in their own bucket. All the reports are self-serve in Artifact, watermarked, for auditors and regulators, not for websites. One line to read out: every SOC, PCI and ISO entry says "excludes Amazon Bedrock Marketplace".

13. Bedrock versus going direct

When someone asks why Bedrock instead of calling OpenAI or Anthropic directly, the answer is about who is in the path. Direct, the provider runs the service, keeps thirty days of abuse logs by default, and zero retention is a sales negotiation. Through Bedrock the provider never sees the prompt, zero retention is the default, and you can enforce it with policy. The price you pay is features that only exist next to the provider's own API, because the provider's servers are not involved: OpenAI's hosted file search, image generation, remote MCP; Anthropic's web search, code execution, Files API, batches, Agent Skills. AWS replaces some of it, its own web search on mantle, your own Lambda tools, Bedrock batch. And watch the name "Claude Platform on AWS": that is an Anthropic-operated service billed through Marketplace, not Bedrock, and none of Bedrock's statements apply to it.

14. Mythos

Mythos is Fable with the dual-use safety measures removed, so it is the model for vulnerability research, red teaming and biodefense, and Anthropic decides who gets it through its trusted access programs. It is not a console click. Data handling is the same as Fable 5.1: thirty days inside AWS, AWS-only review of flagged items, nothing to Anthropic, and you opt in through the retention mode first. Mythos 5.1 is on the runtime endpoint through US or global profiles; the older Mythos 5 and the Glasswing research preview are on mantle in Virginia only, invitation lists managed by the account teams. If a customer says the word, ask which one they mean and who invited them.
