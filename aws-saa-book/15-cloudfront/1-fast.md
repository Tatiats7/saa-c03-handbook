---
id: "15"
slug: cloudfront
title: CloudFront and Global Accelerator
file: fast
tier: deep
domains: [1, 2, 3, 4]
tasks: ["1.3", "2.1", "3.2", "3.4", "4.4"]
services: [cloudfront, global-accelerator]
minutes: {fast: 20, pass: 75, full: 204}
status: ready
updated: 2026-10-14
---

# CloudFront and Global Accelerator

## Predict (2 min)
<!-- section: role=predict; route=fast; minutes=2 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** Your call recordings are in a private S3 bucket. To let CloudFront serve them, do you have to make the bucket public? <!-- gist-trap -->

**Predict 2.** A game sends player moves with UDP to servers in two Regions. Can CloudFront speed up this traffic?

**Predict 3.** You change a style sheet at the origin. When do users who already got the old file from CloudFront see the new one?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

Open AWS CloudShell and read the managed cache policies: they decide what CloudFront puts in the cache key. Then find the AWS-managed prefix list that holds the addresses CloudFront uses to reach your origins; the task creates nothing.

<!-- task:start id=cloudfront-t01 -->

Look

**It kills the belief.** "CloudFront puts every header, cookie and query string in the cache key by default."

> **Cost:** $0.

**Permissions.** `cloudfront:ListCachePolicies`, `cloudfront:GetCachePolicy`, `ec2:DescribeManagedPrefixLists`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. List the cache policies that AWS manages for CloudFront, with the ID and the name of each one.

   ```bash
   aws cloudfront list-cache-policies --type managed --query "CachePolicyList.Items[].CachePolicy.[Id,CachePolicyConfig.Name]"
   ```

   Expect: Pairs of an ID and a name. Find the two names that contain CachingOptimized and CachingDisabled. Their IDs are the ones in steps 2 and 3.

2. Predict first: which headers, cookies and query strings does CachingOptimized put in the cache key? Then read its cache key settings.

   ```bash
   aws cloudfront get-cache-policy --id 658327ea-f89d-4fab-a63d-7e88639e58f6 --query "CachePolicy.CachePolicyConfig.ParametersInCacheKeyAndForwardedToOrigin.[HeadersConfig.HeaderBehavior,CookiesConfig.CookieBehavior,QueryStringsConfig.QueryStringBehavior,EnableAcceptEncodingGzip]"
   ```

   Expect: none, none, none and true. No header, cookie or query string goes into the cache key, only the normalized Accept-Encoding header. Two viewers with different cookies share one cached copy.

3. Read the three time to live (TTL) settings of CachingDisabled in seconds: the minimum, the default and the maximum.

   ```bash
   aws cloudfront get-cache-policy --id 4135ea2d-6df8-44a3-9df3-4b5a84be39ad --query "CachePolicy.CachePolicyConfig.[MinTTL,DefaultTTL,MaxTTL]"
   ```

   Expect: 0, 0 and 0. A copy that lives 0 seconds is no copy: this is how the policy disables caching. It is meant for dynamic content, such as API calls.

4. Find the prefix list that AWS manages for CloudFront: the list whose name contains cloudfront. A security group of an origin can name this list to accept traffic from CloudFront and from nothing else.

   ```bash
   aws ec2 describe-managed-prefix-lists --query "PrefixLists[?contains(PrefixListName, 'cloudfront')].[PrefixListName,PrefixListId,OwnerId]"
   ```

   Expect: One row: the name of the list, an ID that starts with pl- and an owner that is not your account ID. CloudFront keeps the addresses in this list up to date for you. If the result is empty, add --region us-east-1 and run the command again.

**Label.** checked against docs, not run in a real account. Checked 2026-10-14.

<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** CloudFront caches content near users. Global Accelerator gives [two IPv4 static IP addresses](../facts/global-accelerator.md#global-accelerator-faq-two-static-ipv4-independent-network-zones) and carries TCP or UDP over the AWS global network.

**The problem it solves.** Far away, every request crosses the internet and loads your instances. CloudFront is [a web service that speeds up distribution](../facts/cloudfront.md#cloudfront-what-is-web-service-cdn) of web content, and Global Accelerator gives a [fixed entry point to your applications](../facts/global-accelerator.md#global-accelerator-faq-what-it-is-static-entry-point).

**Predict the picture.** On a cache miss at the edge location, where does CloudFront look next?

<details>
<summary>Show the picture</summary>

![A sequence with four participants: a viewer, an edge location, a regional edge cache and the origin. The viewer's request reaches the edge location, which has no copy. The edge location asks the regional edge cache, which also has no copy, and that cache asks the origin. The object travels back through both caches to the viewer, and both caches keep a copy.](../diagrams/svg/cloudfront-hero.svg)

**Figure.** A request goes to the nearest edge location, and a cache miss travels on through the regional edge cache to the origin.

1. [DNS routes the request](../facts/cloudfront.md#cloudfront-dns-routes-to-pop) to the edge location that can best serve it, typically the nearest one.
2. The edge location checks its cache and returns the object when it has a copy.
3. On a miss, the request typically goes to the regional edge cache, which has [a larger cache](../facts/cloudfront.md#cloudfront-rec-larger-cache-than-pop).
4. On a second miss, CloudFront forwards the request to the origin.
5. [As soon as the first byte arrives](../facts/cloudfront.md#cloudfront-first-byte-forwarded-and-cached), CloudFront forwards it to the viewer and [adds the object to the cache](../facts/cloudfront.md#cloudfront-first-byte-forwarded-and-cached).

</details>

> **Startup example:** Callvale's instances in one Region serve every request, and 70% are for static files. Only signed-in users can play a recording, for a limited time.

## Words that go together (2 min)
<!-- section: role=words; route=fast; minutes=2 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| edge location | **cache** at the edge | A site near users where CloudFront keeps copies | Region |
| distribution | **create** a distribution in front of an origin | Your CloudFront setup with its domain name and rules | origin |
| origin | **fetch** an object from the origin | Where the original files or the application live | edge location |
| cache behavior | a path pattern **matches** a cache behavior | A rule for one path: origin, caching and access | cache policy |
| cache key | **include** a header in the cache key | The values that make two requests the same object | URL |
| invalidation | **create** an invalidation for a path | Removing a copy from the edge before it expires | versioned file names |
| signed URL | the signed URL **expires** | A link that CloudFront accepts until a set time | presigned URL of Amazon S3 |
| accelerator | route traffic **through** an accelerator | Your Global Accelerator setup with its two static addresses | load balancer |

## Choose it or not (4 min)
<!-- section: role=choose; route=fast; minutes=4 -->

### CloudFront or Global Accelerator

<!-- table: compare -->
| Question | Amazon CloudFront | AWS Global Accelerator |
|---|---|---|
| What does it carry? | [Content that can be sent using the HTTP](../facts/cloudfront.md#cloudfront-faq-content-types-http-websocket) or WebSocket protocols | [Both TCP and UDP protocols](../facts/global-accelerator.md#global-accelerator-faq-protocols-tcp-and-udp) |
| Does it answer from a cache? | Yes: hits are [served directly from the CloudFront cache](../facts/cloudfront.md#cloudfront-cache-hit-ratio-definition) | No: it works by [proxying packets at the edge](../facts/global-accelerator.md#global-accelerator-faq-vs-cloudfront-content-types) |
| Which addresses do users reach? | Addresses [vary based on your end user’s location](../facts/route53.md#route53-faq-cloudfront-ip-addresses-vary-by-location), or [request Anycast static IPs from CloudFront](../facts/cloudfront.md#cloudfront-change-anycast-static-ips-2024-11) | [Two IPv4 static IP addresses](../facts/global-accelerator.md#global-accelerator-faq-two-static-ipv4-independent-network-zones) |
| How does it fail over? | Origin group, [only when the HTTP method of the viewer](../facts/cloudfront.md#cloudfront-failover-only-get-head-options) is GET, HEAD or OPTIONS | Takes an unhealthy endpoint out of service in [less than one minute](../facts/global-accelerator.md#global-accelerator-faq-failover-detect-under-one-minute) |
| When does AWS suggest it? | For [any publicly accessible web application](../facts/cloudfront.md#cloudfront-dec-consider-for-any-public-web-application) | For [gaming (UDP), IoT (MQTT), or Voice over IP](../facts/global-accelerator.md#global-accelerator-faq-good-fit-non-http-static-ip-fast-failover) |

**Deciding question:** Does the traffic need HTTP caching at the edge, or fixed addresses for TCP or UDP with fast failover between Regions?

### Origin access control or signed access

<!-- table: compare -->
| Question | Origin access control (OAC) | Signed URL | Signed cookies |
|---|---|---|---|
| What does it stop? | Direct S3 URLs: users [cannot access it directly by using Amazon S3 URLs](../facts/cloudfront.md#cloudfront-private-s3-oac-plus-signed-urls) | Users without a valid signed URL | Users without a valid signed cookie |
| What does it cover? | The S3 origin | One file: [restrict access to individual files](../facts/cloudfront.md#cloudfront-signed-url-when-individual-files-or-no-cookies) | Many files: [access to multiple restricted files](../facts/cloudfront.md#cloudfront-signed-cookies-when-multiple-files-or-keep-urls) |
| Who signs? | CloudFront, with the recommended setting: [CloudFront always signs all requests](../facts/cloudfront.md#cloudfront-oac-signing-always-recommended) | Your application, with [a trusted key group that you create](../facts/cloudfront.md#cloudfront-signer-key-group-recommended) | Your application, the same way as for a signed URL |
| Which stem phrase? | "through CloudFront, not with S3 URLs" | "a paid user downloads one file" | "all segments of one video" |

**Deciding question:** Must you stop direct access to the bucket, or decide which users get which files?

AWS recommends both for private content. Signed access decides which users get a file, and OAC on the bucket is recommended too: [this prevents someone from bypassing CloudFront](../facts/cloudfront.md#cloudfront-private-s3-oac-plus-signed-urls).

### CloudFront Functions or edge Lambda functions

<!-- table: compare -->
| Question | CloudFront Functions | Lambda@Edge |
|---|---|---|
| Which events? | Viewer request and viewer response | Viewer events, plus [Origin request](../facts/lambda.md#lambda-edge-event-sources-row) and origin response |
| How long can it run? | [Submillisecond](../facts/cloudfront.md#cloudfront-edge-compare-duration) | [Up to 30 seconds](../facts/cloudfront.md#cloudfront-edge-compare-duration) |
| How large can the code be? | [10 KB](../facts/cloudfront.md#cloudfront-edge-compare-code-size) | [50 MB](../facts/cloudfront.md#cloudfront-edge-compare-code-size) |
| Network and request body? | No [network access](../facts/cloudfront.md#cloudfront-functions-no-network-no-body-fs-access), no [access to the request body](../facts/cloudfront.md#cloudfront-functions-no-network-no-body-fs-access) | Yes: [make network calls to external resources](../facts/cloudfront.md#cloudfront-lambda-edge-network-calls-allowed); viewer request body: [40 KB](../facts/cloudfront.md#cloudfront-lambda-edge-body-truncated-viewer-request-40kb) |
| Which languages? | [JavaScript (ECMAScript 5.1 compliant)](../facts/cloudfront.md#cloudfront-edge-compare-languages) | [Node.js and Python](../facts/cloudfront.md#cloudfront-edge-compare-languages) |

**Deciding question:** Does the code need the network, the request body or more than a few milliseconds?

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "users around the world, lower latency" | Amazon CloudFront | suggested for [any publicly accessible web application](../facts/cloudfront.md#cloudfront-dec-consider-for-any-public-web-application) | UDP traffic or fixed IP addresses: AWS Global Accelerator |
| "UDP, gaming, allow-list static IP addresses" | AWS Global Accelerator | fits [gaming (UDP), IoT (MQTT), or Voice over IP](../facts/global-accelerator.md#global-accelerator-faq-good-fit-non-http-static-ip-fast-failover) | cacheable HTTP downloads: Amazon CloudFront |
| "S3 files only through CloudFront" | origin access control | users [cannot access it directly by using Amazon S3 URLs](../facts/cloudfront.md#cloudfront-private-s3-oac-plus-signed-urls) | an S3 website endpoint, [also considered a custom origin](../facts/cloudfront.md#cloudfront-oac-s3-website-endpoint-not-supported), so no OAC |
| "only paying subscribers, for a limited time" | signed URLs or signed cookies | made for [users who have paid a fee](../facts/cloudfront.md#cloudfront-dec-signed-urls-cookies-for-paying-users) | all segments of one video: signed cookies |
| "fail over between Regions within seconds" | AWS Global Accelerator | [change propagation takes a matter of seconds](../facts/global-accelerator.md#global-accelerator-faq-no-dns-cache-dependency-seconds) | a second origin behind CloudFront: an origin group |
| "add headers, rewrite URLs, millions of requests" | CloudFront Functions | made for [header manipulation](../facts/cloudfront.md#cloudfront-functions-use-cases) and [URL redirects or rewrites](../facts/cloudfront.md#cloudfront-functions-use-cases) | a call to another service: Lambda@Edge |
| "low cache hit ratio, overloaded origin" | a smaller cache key | [forward only the query string parameters](../facts/cloudfront.md#cloudfront-cache-hit-ratio-forward-only-needed-values) that change the response | dynamic content: the CachingDisabled policy |
| "frequent updates, users see the old version" | versioned file names | [versioning is less expensive](../facts/cloudfront.md#cloudfront-invalidation-prefer-versioning-for-frequent-updates) than invalidation | harmful content must go before it expires: an invalidation |

### Traps

- **Wrong belief:** CloudFront serves files from an S3 bucket only if the bucket is public. **Truth:** With origin access control, the bucket stays private and allows the [CloudFront service principal (cloudfront.amazonaws.com)](../facts/cloudfront.md#cloudfront-oac-bucket-policy-cloudfront-service-principal) for your distribution. <!-- trap: cloudfront-trap-public-bucket -->
- **Wrong belief:** An origin access identity (OAI) is the recommended way to keep an S3 origin private. **Truth:** AWS writes: [we recommend that you use OAC instead](../facts/cloudfront.md#cloudfront-oac-oai-two-ways-oac-recommended). Older practice questions still name OAI. <!-- trap: cloudfront-trap-oai-is-current -->
- **Wrong belief:** Global Accelerator caches files at edge locations. **Truth:** It works by [proxying packets at the edge](../facts/global-accelerator.md#global-accelerator-faq-vs-cloudfront-content-types). CloudFront is the cache. <!-- trap: cloudfront-trap-ga-caches -->
- **Wrong belief:** A Route 53 failover record moves users to the second Region as fast as Global Accelerator. **Truth:** Resolvers cache DNS answers [according to their time to live (TTL)](../facts/route53.md#route53-faq-resolver-caches-by-ttl-outside-control). Global Accelerator does not rely on [the IP address caching settings of client devices](../facts/global-accelerator.md#global-accelerator-faq-no-dns-cache-dependency-seconds). <!-- trap: cloudfront-trap-dns-failover-same -->
- **Wrong belief:** CloudFront in front of Amazon S3 adds a transfer charge from S3 to CloudFront. **Truth:** Transfer to CloudFront is [always free when using AWS origins](../facts/cloudfront.md#cloudfront-price-origin-to-cloudfront-always-free-aws-origins). You pay for [the outbound data transfer from CloudFront](../facts/cloudfront.md#cloudfront-price-origin-to-cloudfront-always-free-aws-origins). <!-- trap: cloudfront-trap-origin-fetch-charged -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2024-11-20) VPC origins for private subnets.<br>
> **Old:** not available.<br>
> **Now:** AWS calls VPC origins [the newest and recommended solution](../facts/cloudfront.md#cloudfront-dec-ddos-wp-vpc-origins-newest-recommended).<br>
> **The exam probably expects:** an internet-facing Application Load Balancer that allows the [AWS-managed prefix list for CloudFront](../facts/elb.md#elb-alb-cloudfront-prefix-list-sg) and checks a secret custom header. Prefer an option that is right under both.<br>
> **Status:** examinable.

> **Changed recently:** (2024-11-20) Static IP addresses for CloudFront.<br>
> **Old:** not available.<br>
> **Now:** you can [request Anycast static IPs from CloudFront](../facts/cloudfront.md#cloudfront-change-anycast-static-ips-2024-11).<br>
> **The exam probably expects:** "static IP addresses" points to Global Accelerator.<br>
> **Status:** examinable.

## Check (1 min)
<!-- section: role=check; route=fast; minutes=1 -->

**Check 1.** Photos are in a private S3 bucket. What lets the distribution read the files, but nobody else?

<details>
<summary>Answer</summary>

Origin access control: the bucket policy allows the [CloudFront service principal (cloudfront.amazonaws.com)](../facts/cloudfront.md#cloudfront-oac-bucket-policy-cloudfront-service-principal) for that distribution.

**Predict 1:** No. The bucket stays private behind OAC.

</details>

**Check 2.** Voice calls use UDP to reach two Regions, and customer firewalls allow fixed addresses only. CloudFront or Global Accelerator?

<details>
<summary>Answer</summary>

Global Accelerator: [both TCP and UDP protocols](../facts/global-accelerator.md#global-accelerator-faq-protocols-tcp-and-udp) and [two IPv4 static IP addresses](../facts/global-accelerator.md#global-accelerator-faq-two-static-ipv4-independent-network-zones).

**Predict 2:** No. CloudFront carries [content that can be sent using the HTTP](../facts/cloudfront.md#cloudfront-faq-content-types-http-websocket) or WebSocket protocols, not UDP.

</details>

**Check 3.** Customers worldwide upload large files to one S3 bucket, and uploads are slow. Does CloudFront fit?

<details>
<summary>Answer</summary>

No. S3 Transfer Acceleration fits customers who [upload to a centralized general purpose bucket](../facts/s3.md#s3-transfer-acceleration-when-to-use).

**Predict 3:** When the copy expires, after an invalidation, or right away with a new file name.

</details>

## Recap from memory (1 min)
<!-- section: role=recap; route=fast; minutes=1 -->

**Recap 1.** Which service carries UDP traffic from two static IP addresses?

<details>
<summary>Answer</summary>

AWS Global Accelerator: [two IPv4 static IP addresses](../facts/global-accelerator.md#global-accelerator-faq-two-static-ipv4-independent-network-zones) and [both TCP and UDP protocols](../facts/global-accelerator.md#global-accelerator-faq-protocols-tcp-and-udp).

</details>

**Recap 2.** Signed URL or signed cookies: which one fits all the segment files of one video?

<details>
<summary>Answer</summary>

Signed cookies, which give [access to multiple restricted files](../facts/cloudfront.md#cloudfront-signed-cookies-when-multiple-files-or-keep-urls).

</details>

**Recap 3.** Which edge code can make a network call: CloudFront Functions or Lambda@Edge?

<details>
<summary>Answer</summary>

Lambda@Edge, which can [make network calls to external resources](../facts/cloudfront.md#cloudfront-lambda-edge-network-calls-allowed). CloudFront Functions have no [network access](../facts/cloudfront.md#cloudfront-functions-no-network-no-body-fs-access).

</details>
