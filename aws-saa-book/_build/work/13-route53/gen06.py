import json

def ev(sid, quote, url=None, header=None):
    if url is None:
        if sid.startswith("docs/"):
            url = "https://" + "docs.aws.amazon.com/" + sid[5:] + ".html"
        elif sid.startswith("www/"):
            url = "https://aws.amazon.com/" + sid[4:] + "/"
    return {"source_id": sid, "url": url, "quote": quote, "table_header": header}

R = "docs/Route53/latest/DeveloperGuide/"

def fact(id, kind, claim, question, values, scope, evidence, hard=True, tier0=False, rel="extended", bullets=None,
         note="", vol="stable", dom="", adj=False, cond="", change_items=None, changed=None):
    f = {"id": id, "service": "route53", "home_chapter": "13", "kind": kind, "claim": claim, "question": question,
         "values": [{"key": k, "display": d} for k, d in values],
         "qualifiers": {"scope": scope, "default_or_max": dom, "adjustable": adj, "condition": cond},
         "evidence": evidence, "source_tier": 1, "hard": hard, "tier0": tier0, "volatility": vol, "changed": changed,
         "exam_relevance": rel, "bullets": bullets or []}
    if change_items:
        f["change_items"] = change_items
    if note:
        f["note"] = note
    return f

RP = R + "routing-policy"
facts = []

facts.append(fact("route53-choose-latency-routing-best-latency-region", "capability",
 "Use the latency routing policy when you have resources in multiple AWS Regions and want to route traffic to the Region that provides the best latency.",
 "Which routing policy sends users to the Region with the best latency?",
 [("use", "route traffic to the Region that provides the best latency")], "Amazon Route 53 latency routing policy",
 [ev(RP, "Latency routing policy – Use when you have resources in multiple AWS Regions and you want to route traffic to the Region that provides the best latency.")],
 tier0=True, rel="core", bullets=["3.4.S1"], note="d13-044."))

facts.append(fact("route53-choose-geolocation-routing-user-location", "capability",
 "Use the geolocation routing policy when you want to route traffic based on the location of your users.",
 "Which routing policy follows the location of the user?",
 [("use", "route traffic based on the location of your users")], "Amazon Route 53 geolocation routing policy",
 [ev(RP, "Geolocation routing policy – Use when you want to route traffic based on the location of your users.")],
 tier0=True, rel="core", bullets=["3.4.S1"], note="d13-044."))

facts.append(fact("route53-choose-geoproximity-routing-resource-location-bias", "capability",
 "Use the geoproximity routing policy when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another location.",
 "Which routing policy lets you shift traffic between resources by location?",
 [("use", "shift traffic from resources in one location to resources in another location")], "Amazon Route 53 geoproximity routing policy",
 [ev(RP, "Geoproximity routing policy – Use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another location.")],
 tier0=True, rel="core", bullets=["3.4.S1"], note="d13-044."))

facts.append(fact("route53-geoproximity-bias-expands-or-shrinks-region", "behavior",
 "With geoproximity routing you can send more or less traffic to a resource by setting a bias, which expands or shrinks the geographic region from which traffic goes to that resource.",
 "What does the bias do in geoproximity routing?",
 [("bias", "A bias expands or shrinks the geographic region")], "Amazon Route 53 geoproximity routing",
 [ev(R + "routing-policy-geoproximity", "You can also choose to send more or less traffic to a given resource by setting a value called a bias."),
  ev(R + "routing-policy-geoproximity", "A bias expands or shrinks the geographic region from which traffic goes to a resource.")],
 tier0=True, rel="core", bullets=["3.4.S1"], note="d13-044."))

facts.append(fact("route53-choose-weighted-routing-proportions", "capability",
 "Use the weighted routing policy to route traffic to multiple resources in proportions that you specify; it can be useful for load balancing and testing new versions of software.",
 "Which routing policy splits traffic in proportions, for example for testing a new software version?",
 [("use", "route traffic to multiple resources in proportions that you specify"), ("test", "testing new versions of software")], "Amazon Route 53 weighted routing policy",
 [ev(RP, "Weighted routing policy – Use to route traffic to multiple resources in proportions that you specify."),
  ev(R + "routing-policy-weighted", "This can be useful for load balancing and testing new versions of software.")],
 tier0=True, rel="core", bullets=["2.2.S2"], note="d13-045. Canary and blue/green are the exam wording; the guide says testing new versions of software."))

facts.append(fact("route53-choose-failover-routing-active-passive", "capability",
 "Use the failover routing policy when you want to configure active-passive failover.",
 "Which routing policy gives active-passive failover?",
 [("use", "configure active-passive failover")], "Amazon Route 53 failover routing policy",
 [ev(RP, "Failover routing policy – Use when you want to configure active-passive failover.")],
 tier0=True, rel="core", bullets=["2.2.S2"], note="d13-104."))

facts.append(fact("route53-choose-multivalue-routing-up-to-eight-healthy", "capability",
 "Use the multivalue answer routing policy when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random.",
 "Which routing policy returns up to eight healthy records at random?",
 [("use", "up to eight healthy records selected at random")], "Amazon Route 53 multivalue answer routing policy",
 [ev(RP, "Multivalue answer routing policy – Use when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random.")],
 rel="core", bullets=["2.2.S2"], note="d13-044 neighbour policy."))

facts.append(fact("route53-choose-ip-based-routing-known-client-ips", "capability",
 "Use the IP-based routing policy when you want to route traffic based on the location of your users and you have the IP addresses that the traffic originates from.",
 "Which routing policy uses the client IP ranges you know about?",
 [("use", "have the IP addresses that the traffic originates from")], "Amazon Route 53 IP-based routing policy",
 [ev(RP, "IP-based routing policy – Use when you want to route traffic based on the location of your users, and have the IP addresses that the traffic originates from.")],
 rel="extended", bullets=["3.4.S1"], note="d13-044 neighbour policy."))

facts.append(fact("route53-choose-simple-routing-single-resource", "capability",
 "Use the simple routing policy for a single resource that performs a given function for your domain, for example a web server for a website.",
 "Which routing policy is for one resource that serves a domain?",
 [("use", "Use for a single resource that performs a given function")], "Amazon Route 53 simple routing policy",
 [ev(RP, "Simple routing policy – Use for a single resource that performs a given function for your domain, for example, a web server that serves content for the example.com website.")],
 rel="core", bullets=["2.2.S2"], note="d13-044 neighbour policy."))

facts.append(fact("route53-faq-latency-to-minimize-geo-for-compliance", "behavior",
 "To minimize end-user latency AWS recommends latency based routing; for compliance, localization or other cases that need stable routing from a specific geography to a specific endpoint it recommends Geo DNS (geolocation routing).",
 "When do you choose latency routing and when geolocation routing?",
 [("latency", "we recommend using Latency Based Routing"), ("geo", "we recommend using Geo DNS")], "Amazon Route 53 latency based routing compared with geolocation (Geo DNS)",
 [ev("www/route53/faqs", "If your goal is to minimize end-user latency, we recommend using Latency Based Routing. If you have compliance, localization requirements, or other use cases that require stable routing from a specific geography to a specific endpoint, we recommend using Geo DNS.", "https://aws.amazon.com/route53/faqs/")],
 tier0=True, rel="core", bullets=["3.4.S1"], note="d13-044. FAQ: What is the difference between Latency Based Routing and Geo DNS?"))

facts.append(fact("route53-best-practice-latency-vs-geo-stability", "behavior",
 "The best practices page says to use latency-based routing to minimize application latency, and to use geolocation or geoproximity routing for routing stability and predictability; routing data for latency can change frequently.",
 "Which policy minimizes latency and which gives stable, predictable routing?",
 [("latency", "To minimize application latency, use latency-based routing."), ("stable", "To provide routing stability and predictability")], "Amazon Route 53 advanced DNS routing",
 [ev(R + "best-practices-dns", "To minimize application latency, use latency-based routing. This type of routing data can change frequently."),
  ev(R + "best-practices-dns", "To provide routing stability and predictability, use either geolocation or geoproximity routing.")],
 tier0=True, rel="core", bullets=["3.4.S1"], note="d13-044."))

facts.append(fact("route53-best-practice-always-set-default-record", "behavior",
 "When you use geolocation, geoproximity or latency-based routing, always set a default, unless you want some clients to receive a no answer response.",
 "What happens to clients that match no geolocation record if you set no default record?",
 [("default", "always set a default")], "Amazon Route 53 geolocation, geoproximity and latency-based routing",
 [ev(R + "best-practices-dns", "When using geolocation, geoproximity, or latency-based routing, always set a default, unless you want some clients to receive no answer responses.")],
 tier0=True, rel="core", bullets=["3.4.S1"], note="d13-044."))

facts.append(fact("route53-geolocation-use-cases-language-rights", "capability",
 "Geolocation routing can show content in the language of your users, limit content to the locations where you have distribution rights, and balance load across endpoints so that each user location always goes to the same endpoint.",
 "What are typical reasons to use geolocation routing?",
 [("language", "show your content in the language of your users"), ("rights", "locations where you have distribution rights")], "Amazon Route 53 geolocation routing",
 [ev(R + "routing-policy-geo", "When you use geolocation routing, you can show your content in the language of your users. You can also use geolocation routing to limit content to only the locations where you have distribution rights. Another use is to balance load across endpoints in a way that is easy to predict and manage, so that each user location always goes to the same endpoint.")],
 rel="core", bullets=["3.4.S1"], note="d13-044."))

facts.append(fact("route53-latency-data-is-aws-traffic-not-your-resources", "behavior",
 "Latency data is based entirely on traffic between users and AWS data centers, so if you are not using resources in an AWS Region the actual latency between your users and your resources can vary significantly from AWS latency data.",
 "Is latency-based routing accurate for resources outside AWS Regions?",
 [("scope", "based entirely on traffic between users and AWS data centers")], "Amazon Route 53 latency-based routing",
 [ev(R + "routing-policy-latency", "Data about the latency between users and your resources is based entirely on traffic between users and AWS data centers. If you aren't using resources in an AWS Region, the actual latency between your users and your resources can vary significantly from AWS latency data.")],
 rel="extended", bullets=["3.4.S1"], note="d13-044."))

facts.append(fact("route53-geolocation-default-record-no-answer", "behavior",
 "If you do not create a default geolocation record, Amazon Route 53 returns a no answer response for queries from locations that it cannot identify or where you created no geolocation record.",
 "What does Route 53 return to a user in a location with no geolocation record and no default record?",
 [("noanswer", "Route 53 returns a \"no answer\" response")], "Amazon Route 53 geolocation routing",
 [ev(R + "routing-policy-geo", "If you don't create a default record, Route 53 returns a \"no answer\" response for queries from those locations.")],
 tier0=True, rel="core", bullets=["3.4.S1"], note="d13-044. Pairs with the unmapped IP address sentence on the same page."))

facts.append(fact("route53-weighted-ttl-short-before-change", "behavior",
 "For a domain or subdomain that is already in use, set a shorter TTL first (for example 300 seconds) and raise it after you confirm the new settings; a longer TTL means recursive resolvers use cached values longer before asking Amazon Route 53 for the latest information.",
 "How does resolver caching delay a traffic shift between weighted records?",
 [("short", "specify a shorter value first, such as 300 seconds")], "Amazon Route 53 record TTL",
 [ev(R + "resource-record-sets-values-weighted", "However, if you specify a longer value for TTL, it takes longer for changes to the record (for example, a new IP address) to take effect. Recursive resolvers use the values in their cache for longer periods before they ask Route 53 for the latest information."),
  ev(R + "resource-record-sets-values-weighted", "If you're changing settings for a domain or subdomain that's already in use, specify a shorter value first, such as 300 seconds, and increase the value after you confirm that the new settings are correct.")],
 tier0=True, rel="core", bullets=["2.2.S2"], note="d13-045, d13-103."))

facts.append(fact("route53-weighted-health-checked-ttl-60-or-less", "default",
 "If a record is associated with a health check, the guide says to specify a TTL of 60 seconds or less so that clients respond quickly to changes in health status.",
 "What TTL should a health-checked record use?",
 [("ttl", "a TTL of 60 seconds or less")], "Amazon Route 53 weighted records with a health check",
 [ev(R + "resource-record-sets-values-weighted", "If you're associating this record with a health check, specify a TTL of 60 seconds or less so clients respond quickly to changes in health status.")],
 tier0=True, rel="core", bullets=["2.2.S2"], dom="max", adj=True, note="d13-045, d13-103, d13-104. The shared-values page words it 'we recommend that you specify a TTL of 60 seconds or less'."))

facts.append(fact("route53-weighted-alias-elb-non-alias-ttl-60", "restriction",
 "If a group of weighted records includes weighted alias records that route traffic to an ELB load balancer, specify a TTL of 60 seconds for the non-alias weighted records with the same name and type, because other values change the effect of the weights.",
 "What TTL must non-alias weighted records use next to a weighted alias record for a load balancer?",
 [("ttl", "specify a TTL of 60 seconds"), ("elb", "the TTL for load balancers")], "Amazon Route 53 weighted records that include an alias to an ELB load balancer",
 [ev(R + "resource-record-sets-values-weighted", "If a group of weighted records includes one or more weighted alias records that route traffic to an ELB load balancer, specify a TTL of 60 seconds for all of the non-alias weighted records that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for Weight.")],
 rel="extended", bullets=["2.2.S2"], dom="fixed", note="d13-045."))

facts.append(fact("route53-best-practice-shorten-ttl-before-critical-change", "behavior",
 "Before you change critical DNS entries, temporarily shorten the TTLs, make the change, observe and roll back quickly if needed, then raise the TTL again once the change works as expected.",
 "How should you plan the TTL when you change a critical DNS record?",
 [("plan", "temporarily shorten the TTLs")], "Amazon Route 53 record TTL best practice",
 [ev(R + "best-practices-dns", "When you want to make changes to critical DNS entries, we recommend that you temporarily shorten the TTLs. Then you can make the changes, observe, and rollback quickly if you need to. After the changes are finalized and working as expected, you can increase the TTL.")],
 tier0=True, rel="core", bullets=["2.2.S2"], note="d13-045, d13-103. Callvale: resolvers cache answers, so every change needs planning."))

facts.append(fact("route53-best-practice-ttl-failover-60-or-120", "behavior",
 "For records that change as part of a rapid failover mechanism, especially health-checked records, lower TTLs are appropriate and a TTL of 60 or 120 seconds is a common choice; for delegation (NS) records and other rarely changed records longer TTLs are recommended.",
 "Which TTL fits a health-checked failover record and which fits an NS record?",
 [("failover", "Setting a TTL of 60 or 120 seconds is a common choice"), ("ns", "A value between an hour (3600s) and a day (86,400s) is a common choice")], "Amazon Route 53 record TTL best practice",
 [ev(R + "best-practices-dns", "For records that need to be altered as part of a rapid failover mechanism (especially records that are health checked), lower TTLs are appropriate. Setting a TTL of 60 or 120 seconds is a common choice for this scenario."),
  ev(R + "best-practices-dns", "This is especially true on delegations (NS record sets), or other records that rarely change, for example MX records. For these records, longer TTLs are recommended. A value between an hour (3600s) and a day (86,400s) is a common choice.")],
 rel="core", bullets=["2.2.S2"], dom="", note="d13-103, d13-104."))

facts.append(fact("route53-migrate-ns-ttl-two-days-lower-first", "behavior",
 "The typical TTL of an NS record is 172800 seconds (two days); if you do not lower it before migrating DNS to Amazon Route 53, your domain could be unavailable on the internet for up to two days if something goes wrong.",
 "Why lower the NS record TTL before moving DNS service to Route 53?",
 [("typical", "172800 seconds, or two days"), ("risk", "unavailable on the internet for up to two days")], "NS record TTL before a DNS migration",
 [ev(R + "migrate-dns-domain-in-use", "The typical TTL setting for the NS record is 172800 seconds, or two days."),
  ev(R + "migrate-dns-domain-in-use", "If you don't lower the TTL, your domain could be unavailable on the internet for up to two days if something goes wrong.")],
 tier0=True, rel="core", bullets=["2.2.S2"], dom="default", adj=True, note="d13-103. Callvale: the NS record TTL at the registrar."))

facts.append(fact("route53-migrate-lower-ns-ttl-60-to-900-wait-two-days", "behavior",
 "When you migrate DNS to Amazon Route 53 the guide recommends lowering the NS record TTL to a value between 60 seconds and 900 seconds, then waiting two days after lowering it before switching name servers, and raising the TTL again afterwards.",
 "Which NS TTL does the migration guide recommend and how long do you wait?",
 [("ttl", "a value between 60 seconds and 900 seconds"), ("wait", "wait for two days after you lowered the TTL")], "NS record TTL during a DNS migration to Route 53",
 [ev(R + "migrate-dns-domain-in-use", "We recommend that you specify a value between 60 seconds and 900 seconds (15 minutes)."),
  ev(R + "migrate-dns-domain-in-use", "To make sure that migrating DNS service to Route 53 happens all at one time, wait for two days after you lowered the TTL.")],
 rel="core", bullets=["2.2.S2"], dom="", note="d13-103."))

if __name__ == "__main__":
    json.dump(facts, open("aws-saa-book/_build/work/13-route53/facts-dc-06a.json", "w"), indent=0, ensure_ascii=False)
    print(len(facts))
