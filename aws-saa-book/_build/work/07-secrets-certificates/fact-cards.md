facts card: 388 facts
acm-account-separation
  claim: ACM best practice: use account-level separation and keep production certificates in separate accounts from test and development certificates.
  scope: per AWS account.
  link: [Keep your production certificates in separate accounts](../facts/acm.md#acm-account-separation)
  link: [Use account-level separation](../facts/acm.md#acm-account-separation)
acm-acme-certificate-validity
  claim: ACME certificates from ACM are valid for a maximum of 45 days, and ACME-enrolled certificates are charged per domain at issuance and at each automatic renewal.
  scope: per ACME-issued certificate; maximum; not adjustable.
  link: [a maximum of 45 days](../facts/acm.md#acm-acme-certificate-validity)
  say: at most forty-five days
acm-acme-not-for-integrated-services
  claim: With ACME, the private key is generated and held by your ACME client and never leaves your systems; certificates issued through ACME appear in the ACM inventory but cannot be bound to AWS integrated services.
  scope: per ACME certificate.
  link: [cannot be bound to AWS integrated services](../facts/acm.md#acm-acme-not-for-integrated-services)
  link: [never leaves your systems](../facts/acm.md#acm-acme-not-for-integrated-services)
acm-alb-certificate-from-acm-or-iam
  claim: Instead of an ACM-issued certificate, you can get a certificate signed by a CA from your own CSR and import it into ACM or upload it to IAM for use with an Application Load Balancer.
  scope: per load balancer.
  link: [import the certificate into ACM](../facts/acm.md#acm-alb-certificate-from-acm-or-iam)
  link: [upload the certificate](../facts/acm.md#acm-alb-certificate-from-acm-or-iam)
acm-alb-certificates-per-load-balancer
  claim: An Application Load Balancer can have 25 certificates by default, not counting default certificates, and the quota is adjustable.
  scope: per Application Load Balancer, excluding default certificates; default; adjustable.
  link: [25](../facts/acm.md#acm-alb-certificates-per-load-balancer)
  say: twenty-five
acm-alb-https-listener-default-certificate
  claim: When you create an HTTPS listener on an Application Load Balancer, you must specify exactly one certificate, known as the default certificate; a certificate list lets the load balancer support multiple domains on the same port with a different certificate for each domain, and the load balancer selects a certificate with support for SNI.
  scope: per HTTPS listener.
  link: [you must specify exactly one certificate](../facts/acm.md#acm-alb-https-listener-default-certificate)
acm-alb-renewal-in-flight
  claim: Renewing or replacing an ALB certificate does not affect in-flight requests; after renewal, new requests use the renewed certificate, and ACM certificates deployed on the load balancer can be renewed automatically.
  scope: per load balancer.
  link: [does not affect in-flight requests](../facts/acm.md#acm-alb-renewal-in-flight)
  link: [can be renewed automatically](../facts/acm.md#acm-alb-renewal-in-flight)
acm-alb-supported-key-lengths
  claim: For Application Load Balancer certificates, ACM supports RSA certificates with 2048, 3072 and 4096-bit key lengths, and all ECDSA certificates.
  scope: certificates for Application Load Balancer listeners.
  link: [2048, 3072, and 4096-bit](../facts/acm.md#acm-alb-supported-key-lengths)
  link: [all ECDSA certificates](../facts/acm.md#acm-alb-supported-key-lengths)
  say: two thousand forty-eight, three thousand seventy-two and four thousand ninety-six bit
acm-amazon-trust-services
  claim: ACM public certificates are trusted by all major browsers, including Chrome, Edge, Firefox and Safari.
  scope: per public certificate.
  link: [trusted by all major browsers](../facts/acm.md#acm-amazon-trust-services)
  link: [Java also trusts ACM certificates](../facts/acm.md#acm-amazon-trust-services)
acm-amplify-issues-certificate
  claim: When you connect a custom domain to an Amplify application, the Amplify console issues an ACM certificate to secure it.
  scope: per Amplify app custom domain.
  link: [the Amplify console issues an ACM certificate](../facts/acm.md#acm-amplify-issues-certificate)
  link: [connect a custom domain](../facts/acm.md#acm-amplify-issues-certificate)
acm-api-gateway-custom-domain
  claim: To set up a custom domain name in API Gateway you must provide an SSL/TLS certificate, and you can use ACM to generate or import it.
  scope: per API Gateway custom domain.
  link: [You can use ACM to generate or import](../facts/acm.md#acm-api-gateway-custom-domain)
  link: [you must provide an SSL/TLS certificate](../facts/acm.md#acm-api-gateway-custom-domain)
acm-approaching-expiration-event
  claim: ACM sends daily expiration events for all active certificates (public, private and imported), starting 45 days before expiration for private and imported certificates and 30 days before expiration for public certificates; this timing can be changed with the PutAccountConfiguration action of the ACM API.
  scope: per active certificate; default; adjustable; changeable with PutAccountConfiguration.
  link: [45 days](../facts/acm.md#acm-approaching-expiration-event)
  link: [30 days](../facts/acm.md#acm-approaching-expiration-event)
  link: [daily expiration events](../facts/acm.md#acm-approaching-expiration-event)
  say: forty-five days | thirty days
acm-caa-error-update-and-rerequest
  claim: If a CAA error appears after the ACM request was validated, you must update the CAA records and request the certificate again.
  scope: per certificate request.
  link: [you must update your CAA records](../facts/acm.md#acm-caa-error-update-and-rerequest)
  link: [request a certificate again](../facts/acm.md#acm-caa-error-update-and-rerequest)
acm-caa-optional-checked-after-validation
  claim: A CAA record is optional; ACM checks for one after it validates the domain during the certificate request.
  scope: per certificate request.
  link: [Configuring a CAA record is optional](../facts/acm.md#acm-caa-optional-checked-after-validation)
  link: [checks for the presence of a CAA record](../facts/acm.md#acm-caa-optional-checked-after-validation)
acm-caa-record-limits-cas
  claim: A CAA DNS record names the certificate authorities allowed to issue certificates for a domain or subdomain; it does not replace domain-ownership validation.
  scope: per domain or subdomain.
  link: [allowed to issue certificates for a domain](../facts/acm.md#acm-caa-record-limits-cas)
  link: [isn't a substitute for the security requirements](../facts/acm.md#acm-caa-record-limits-cas)
acm-caa-route53-supports
  claim: Route 53 supports CAA records.
  scope: per hosted zone.
  link: [Route 53 supports CAA records](../facts/acm.md#acm-caa-route53-supports)
acm-case-trainline-issue-certificates-acm
  claim: After the migration, Trainline's team can quickly issue new certificates for new domains using AWS Certificate Manager.
  scope: one customer.
  link: [quickly issue new certificates for new domains](../facts/acm.md#acm-case-trainline-issue-certificates-acm)
  link: [AWS Certificate Manager (ACM)](../facts/acm.md#acm-case-trainline-issue-certificates-acm)
acm-case-trainline-manual-certificates-before
  claim: Before moving its CDN to CloudFront, Trainline had to submit a request to another provider and wait whenever it needed to update certificates.
  scope: one customer.
  link: [submit a request to another provider and wait](../facts/acm.md#acm-case-trainline-manual-certificates-before)
  link: [Trainline](../facts/acm.md#acm-case-trainline-manual-certificates-before)
acm-certificate-extra-names
  claim: Each ACM certificate must include at least one fully qualified domain name and can include more names, including the bare domain: you can request www.example.com and include example.com.
  scope: per certificate.
  link: [can include additional names](../facts/acm.md#acm-certificate-extra-names)
  link: [This applies to bare domains](../facts/acm.md#acm-certificate-extra-names)
acm-certificates-regional
  claim: ACM certificates are Regional resources: to use the same domain names with Elastic Load Balancing in more than one Region, you request or import a certificate in each Region, and you cannot copy a certificate between Regions.
  scope: per Region.
  link: [Certificates in ACM are regional resources](../facts/acm.md#acm-certificates-regional)
  link: [You cannot copy a certificate between regions](../facts/acm.md#acm-certificates-regional)
acm-change-acme-2026
  claim: ACM added the ACME protocol for public certificates: the ACM document history dates it 2026-06-18 and the What's New post is dated 2026-07-06; ACME endpoints issue public TLS certificates with a 45 day validity.
  scope: ACM public certificates; both dates are before the book's 2026-07-15 examinability cutoff; low exam weight.
  link: [2026-06-18](../facts/acm.md#acm-change-acme-2026)
  link: [2026-07-06](../facts/acm.md#acm-change-acme-2026)
  say: June eighteenth, twenty twenty-six | July sixth, twenty twenty-six
acm-change-ct-logging-optout-removed-2026
  claim: On 2026-06-01 ACM removed the certificate transparency logging opt-out; all public ACM certificates are automatically recorded in certificate transparency logs.
  scope: ACM public certificates.
  link: [2026-06-01](../facts/acm.md#acm-change-ct-logging-optout-removed-2026)
  link: [opt-out is no longer available](../facts/acm.md#acm-change-ct-logging-optout-removed-2026)
  say: June first, twenty twenty-six
acm-change-ecdsa-2022
  claim: On 2022-11-08 ACM added support for ECDSA when requesting a public ACM certificate.
  scope: ACM public certificate requests.
  link: [2022-11-08](../facts/acm.md#acm-change-ecdsa-2022)
  say: November eighth, twenty twenty-two
acm-change-email-to-dns-switch-2026
  claim: On 2026-08-13 ACM announced that existing public certificates can switch from email to DNS validation without reissue or a new ARN, with up to 72 hours to add the DNS records; before, the ACM guide said that an email-validated certificate cannot switch to DNS validation and must be deleted and requested again.
  scope: existing ACM public certificates; maximum; not examinable yet (announced after the book's cutoff); ACM will phase out its support for email validation throughout 2027.
  link: [2026-08-13](../facts/acm.md#acm-change-email-to-dns-switch-2026)
  link: [up to 72 hours](../facts/acm.md#acm-change-email-to-dns-switch-2026)
  link: [you cannot switch to validating it with DNS](../facts/acm.md#acm-change-email-to-dns-switch-2026)
  say: August thirteenth, twenty twenty-six | up to seventy-two hours
  changed: 2026-08-13: was you cannot switch to validating it with DNS
acm-change-exportable-public-certificates-2025
  claim: On 2025-06-17 ACM introduced exportable public certificates that can be used on EC2 instances, containers or on-premises hosts; previously ACM-issued public certificates could only be used with integrated AWS services.
  scope: ACM public certificates.
  link: [2025-06-17](../facts/acm.md#acm-change-exportable-public-certificates-2025)
  link: [could only be used with integrated AWS services](../facts/acm.md#acm-change-exportable-public-certificates-2025)
  say: June seventeenth, twenty twenty-five
  changed: 2025-06-17: was could only be used with integrated AWS services
acm-change-http-validation-cloudfront-2025
  claim: On 2025-04-24 ACM added HTTP validation of domain ownership for certificates issued for CloudFront distributions.
  scope: certificates for CloudFront distributions.
  link: [2025-04-24](../facts/acm.md#acm-change-http-validation-cloudfront-2025)
  say: April twenty-fourth, twenty twenty-five
acm-change-mx-email-validation-removed-2024
  claim: On 2024-07-11 the ACM console stopped supporting mail exchanger (MX) email validation.
  scope: ACM email validation.
  link: [2024-07-11](../facts/acm.md#acm-change-mx-email-validation-removed-2024)
  say: July eleventh, twenty twenty-four
acm-change-searchcertificates-2026
  claim: On 2026-03-31 the ACM guide moved to the SearchCertificates API for finding and filtering certificates.
  scope: ACM certificate management; low exam weight.
  link: [2026-03-31](../facts/acm.md#acm-change-searchcertificates-2026)
  say: March thirty-first, twenty twenty-six
acm-change-validity-198-days-2026
  claim: On 2026-02-18 ACM cut the maximum validity of new and renewed public certificates to 198 days, from the previous validity period of 395 days; existing 395-day certificates stay valid until they renew or expire.
  scope: ACM public certificates; maximum; no customer action required.
  link: [2026-02-18](../facts/acm.md#acm-change-validity-198-days-2026)
  link: [198 days](../facts/acm.md#acm-change-validity-198-days-2026)
  link: [395 days](../facts/acm.md#acm-change-validity-198-days-2026)
  say: February eighteenth, twenty twenty-six | one hundred ninety-eight days | three hundred ninety-five days
  changed: 2026-02-18: was 395 days
acm-change-whois-email-deprecation-2024
  claim: On 2024-02-05 the ACM guide added a note that WHOIS email verification is deprecated starting in June 2024.
  scope: ACM email validation.
  link: [2024-02-05](../facts/acm.md#acm-change-whois-email-deprecation-2024)
  say: February fifth, twenty twenty-four
acm-change-workload-credentials-provider-2026
  claim: On 2026-06-11 AWS announced AWS Workload Credentials Provider, a client-side provider that automates deployment of exported ACM certificates on Windows and Linux with NGINX and Apache.
  scope: exported ACM certificates; low exam weight.
  link: [2026-06-11](../facts/acm.md#acm-change-workload-credentials-provider-2026)
  say: June eleventh, twenty twenty-six
acm-cloudformation-wildcard-for-tests
  claim: If CloudFormation quickly creates and deletes many test environments, AWS recommends that you do not create a separate ACM certificate for each environment, which would quickly exhaust your certificate quota; instead, create one wildcard certificate that covers all of the domain names that you use for testing.
  scope: per account.
  link: [do not create a separate ACM certificate](../facts/acm.md#acm-cloudformation-wildcard-for-tests)
  link: [quickly exhaust your certificate quota](../facts/acm.md#acm-cloudformation-wildcard-for-tests)
acm-cloudfront-managed-certificates
  claim: Certificates that use HTTP validation with CloudFront show CLOUDFRONT in the ManagedBy field and can only be used through CloudFront.
  scope: per CloudFront-managed certificate.
  link: [These certificates can only be used through CloudFront](../facts/acm.md#acm-cloudfront-managed-certificates)
  link: [ManagedBy](../facts/acm.md#acm-cloudfront-managed-certificates)
acm-cloudfront-no-acm-cert-from-other-account
  claim: With certificates provided by ACM, you cannot configure CloudFront to use a certificate that was created by a different AWS account.
  scope: ACM-provided certificates used with CloudFront; the certificate is provided by ACM (not a third-party certificate).
  link: [you can't configure CloudFront to use certificates](../facts/acm.md#acm-cloudfront-no-acm-cert-from-other-account)
  link: [created by a different AWS account](../facts/acm.md#acm-cloudfront-no-acm-cert-from-other-account)
acm-cloudfront-one-cert-per-distribution
  claim: You can associate only one certificate with each CloudFront distribution.
  scope: per CloudFront distribution; maximum.
  link: [only one certificate with each distribution](../facts/acm.md#acm-cloudfront-one-cert-per-distribution)
  link: [You can associate only one certificate](../facts/acm.md#acm-cloudfront-one-cert-per-distribution)
acm-cloudfront-origin-certificate-any-region
  claim: For HTTPS between CloudFront and an Elastic Load Balancing origin, the load balancer's certificate can be requested or imported in any AWS Region; only the viewer certificate must be in US East (N. Virginia).
  scope: per origin load balancer.
  link: [import the certificate in any AWS Region](../facts/acm.md#acm-cloudfront-origin-certificate-any-region)
  link: [US East (N. Virginia) Region](../facts/acm.md#acm-cloudfront-origin-certificate-any-region)
acm-cloudfront-same-cert-many-distributions
  claim: You can use the same certificate for any or all of the CloudFront distributions that serve HTTPS requests.
  scope: certificates for CloudFront distributions that serve HTTPS.
  link: [the same certificate for any or all](../facts/acm.md#acm-cloudfront-same-cert-many-distributions)
  link: [of the CloudFront distributions](../facts/acm.md#acm-cloudfront-same-cert-many-distributions)
acm-cloudfront-us-east-1
  claim: To use an ACM certificate with Amazon CloudFront, you must request or import it in the US East (N. Virginia) Region; it is then distributed to all locations of the distribution.
  scope: per CloudFront distribution.
  link: [US East (N. Virginia)](../facts/acm.md#acm-cloudfront-us-east-1)
  link: [distributed to all the geographic locations](../facts/acm.md#acm-cloudfront-us-east-1)
acm-cname-works-any-region
  claim: While the CNAME record stays in place you can request more certificates for the same name without validating again, and because the CNAME token works for any Region you can re-create the same certificate in several Regions.
  scope: per domain name; CNAME record still in place.
  link: [CNAME validation token works for any AWS Region](../facts/acm.md#acm-cname-works-any-region)
  link: [Without the need to repeat validation](../facts/acm.md#acm-cname-works-any-region)
acm-config-rule-expiration-check
  claim: The AWS Config managed rule acm-certificate-expiration-check checks whether ACM certificates in your account are marked for expiration within a specified number of days, and it notes that ACM does not automatically renew certificates that you import.
  scope: per ACM certificate in the account; AWS Config managed rule acm-certificate-expiration-check.
  link: [marked for expiration](../facts/acm.md#acm-config-rule-expiration-check)
  link: [does not automatically renew certificates that you import](../facts/acm.md#acm-config-rule-expiration-check)
acm-days-to-expiry-metric
  claim: ACM publishes the CloudWatch metric DaysToExpiry, the number of days until a certificate expires, for every certificate until it expires.
  scope: per certificate.
  link: [DaysToExpiry](../facts/acm.md#acm-days-to-expiry-metric)
  link: [Number of days until a certificate expires](../facts/acm.md#acm-days-to-expiry-metric)
acm-decision-guide-optimized-for
  claim: The AWS security services decision guide lists AWS KMS as optimized for cryptographic keys, AWS Certificate Manager for private SSL/TLS X.509 certificates and keys, AWS Private CA for creating private certificate authority hierarchies, and Secrets Manager for credentials, OAuth tokens, API keys and other secrets.
  scope: per service.
  link: [Optimized for cryptographic keys](../facts/acm.md#acm-decision-guide-optimized-for)
  link: [Optimized for creating private certificate authority hierarchies](../facts/acm.md#acm-decision-guide-optimized-for)
acm-dns-cname-records
  claim: With DNS validation, ACM gives you CNAME records to add to your DNS database once; ACM renews the certificate automatically as long as the certificate is in use and the CNAME record remains.
  scope: per domain name.
  link: [added to your DNS database only once](../facts/acm.md#acm-dns-cname-records)
  link: [your CNAME record remains in place](../facts/acm.md#acm-dns-cname-records)
acm-dns-renewal-criteria
  claim: Managed renewal is fully automated for DNS-validated certificates when two criteria hold: the certificate is in use by an AWS service, and all required ACM CNAME records are present and reachable in public DNS.
  scope: per DNS-validated certificate.
  link: [currently in use by an AWS service](../facts/acm.md#acm-dns-renewal-criteria)
  link: [present and accessible via public DNS](../facts/acm.md#acm-dns-renewal-criteria)
acm-dns-validation-recommended
  claim: AWS recommends DNS validation over email validation: with Amazon Route 53 you can update records through ACM directly, and ACM automatically renews DNS-validated certificates as long as the certificate is in use and the DNS record is in place.
  scope: per public certificate.
  link: [We recommend using DNS validation over email validation](../facts/acm.md#acm-dns-validation-recommended)
  link: [automatically renews DNS-validated certificates](../facts/acm.md#acm-dns-validation-recommended)
acm-dns-without-route53
  claim: If Route 53 is not your DNS provider, you enter the ACM CNAME records in your provider's database yourself; if you cannot edit the domain's DNS database, you must use email validation.
  scope: per domain name.
  link: [manually enter CNAME records provided by ACM](../facts/acm.md#acm-dns-without-route53)
  link: [into your provider's database](../facts/acm.md#acm-dns-without-route53)
acm-do-not-pin
  claim: ACM generates a new key pair when it renews a certificate, so an application that pins an ACM certificate might be unable to connect after renewal; AWS recommends not pinning ACM certificates.
  scope: per certificate.
  link: [ACM generates a new public-private key pair](../facts/acm.md#acm-do-not-pin)
  link: [you don't pin an ACM certificate](../facts/acm.md#acm-do-not-pin)
acm-domain-names-public-ct-logs
  claim: Do not put confidential information in public certificate domain names, because public certificates, including ACM ones, are logged to public, append-only Certificate Transparency logs.
  scope: per public certificate.
  link: [public, append-only Certificate Transparency logs](../facts/acm.md#acm-domain-names-public-ct-logs)
  link: [Do not include confidential or sensitive information](../facts/acm.md#acm-domain-names-public-ct-logs)
acm-domain-validated-only
  claim: ACM certificates are domain validated: they identify only a domain name, and when you request one you must prove ownership or control of every specified domain.
  scope: per public certificate.
  link: [ACM certificates are domain validated](../facts/acm.md#acm-domain-validated-only)
  link: [identifying only a domain name](../facts/acm.md#acm-domain-validated-only)
acm-ec2-needs-nitro-enclave
  claim: Associating an ACM-managed certificate directly with an Amazon EC2 instance requires a Nitro Enclave.
  scope: per EC2 instance.
  link: [requires a Nitro Enclave](../facts/acm.md#acm-ec2-needs-nitro-enclave)
  link: [directly with an Amazon EC2 instance](../facts/acm.md#acm-ec2-needs-nitro-enclave)
acm-elb-deploys-on-load-balancer
  claim: Load balancers need SSL/TLS certificates on either the load balancer or the back-end EC2 instance, and ACM is integrated with Elastic Load Balancing to deploy ACM certificates on the load balancer.
  scope: per load balancer.
  link: [deploy ACM certificates on the load balancer](../facts/acm.md#acm-elb-deploys-on-load-balancer)
  link: [either the load balancer or the back-end Amazon EC2 instance](../facts/acm.md#acm-elb-deploys-on-load-balancer)
acm-email-five-addresses
  claim: For email validation, ACM sends validation messages to five common system addresses of each domain (administrator, hostmaster, postmaster, webmaster and admin), and you prove ownership by selecting the link in the email.
  scope: per domain name; fixed; or at a superdomain you specify as the validation domain.
  link: [five common system emails](../facts/acm.md#acm-email-five-addresses)
  link: [select the validation link included in these emails](../facts/acm.md#acm-email-five-addresses)
  say: five common system emails
acm-email-validation-needs-owner-action
  claim: Email-validated certificates need an action by the domain owner to be renewed: ACM sends renewal notices with a link, and after all domains are validated it issues the renewed certificate with the same ARN.
  scope: per email-validated certificate.
  link: [require an action by the domain owner](../facts/acm.md#acm-email-validation-needs-owner-action)
  link: [issues a renewed certificate with the same ARN](../facts/acm.md#acm-email-validation-needs-owner-action)
acm-exportable-charged
  claim: Exportable public SSL/TLS certificates from ACM have an additional charge.
  scope: per exportable certificate.
  link: [You are subject to an additional charge](../facts/acm.md#acm-exportable-charged)
  link: [exportable public SSL/TLS certificates](../facts/acm.md#acm-exportable-charged)
acm-exportable-use-anywhere
  claim: ACM exportable public certificates let you deploy ACM public certificates anywhere, including EC2 instances, containers and on-premises hosts, beyond integrated AWS services.
  scope: per exportable certificate.
  link: [beyond integrated AWS services](../facts/acm.md#acm-exportable-use-anywhere)
  link: [Export the certificate, private key, and certificate chain](../facts/acm.md#acm-exportable-use-anywhere)
acm-exportable-you-deploy
  claim: For exported certificates, ACM manages renewals and sends notifications when new certificates are available, and the ACM guide says that you must manage the deployment process yourself; the guide also says that you can automate exportable certificates issued from ACM through AWS Workload Credentials Provider.
  scope: per exportable certificate.
  link: [You must manage the deployment process](../facts/acm.md#acm-exportable-you-deploy)
  link: [ACM manages renewals and sends notifications](../facts/acm.md#acm-exportable-you-deploy)
acm-faq-99-percent-ubiquity
  claim: ACM-provided certificates have 99% browser and operating system ubiquity, including Windows XP SP3 and Java 6 and later.
  scope: ACM-provided certificates.
  link: [99% browser and operating system ubiquity](../facts/acm.md#acm-faq-99-percent-ubiquity)
  say: ninety-nine percent
acm-faq-avoid-downtime-managed-renewals
  claim: By managing renewals, ACM can help you avoid downtime caused by misconfigured, revoked or expired certificates.
  scope: ACM-managed certificates.
  link: [misconfigured, revoked, or expired certificates](../facts/acm.md#acm-faq-avoid-downtime-managed-renewals)
  link: [by managing renewals](../facts/acm.md#acm-faq-avoid-downtime-managed-renewals)
  link: [avoid downtime](../facts/acm.md#acm-faq-avoid-downtime-managed-renewals)
acm-faq-bare-domain-email-resolve
  claim: For an email-validated public certificate with a bare domain, make sure a DNS lookup of the bare domain resolves to the AWS resource associated with the certificate so ACM can renew it.
  scope: email-validated public certificates with a bare (apex) domain; email validation was chosen.
  link: [a DNS lookup of the bare domain resolves](../facts/acm.md#acm-faq-bare-domain-email-resolve)
  link: [resolves to the AWS resource](../facts/acm.md#acm-faq-bare-domain-email-resolve)
acm-faq-caa-record-must-name-amazon
  claim: If your DNS configuration has a CAA record, it must specify amazon.com, amazontrust.com, awstrust.com or amazonaws.com before Amazon can issue a certificate for the domain.
  scope: per domain; when a CAA record is present.
  link: [amazon.com, amazontrust.com, awstrust.com, or amazonaws.com](../facts/acm.md#acm-faq-caa-record-must-name-amazon)
  link: [must specify one of the following CAs](../facts/acm.md#acm-faq-caa-record-must-name-amazon)
acm-faq-central-management-per-region
  claim: ACM lets you use the console, the AWS CLI or the ACM APIs to centrally manage all ACM certificates in an AWS Region.
  scope: per AWS Region.
  link: [in an AWS Region](../facts/acm.md#acm-faq-central-management-per-region)
  link: [centrally manage all of the SSL/TLS ACM certificates](../facts/acm.md#acm-faq-central-management-per-region)
acm-faq-certificate-same-region-as-resource
  claim: ACM certificates must be in the same Region as the resource where they are being used; the only exception is Amazon CloudFront.
  scope: per certificate; except Amazon CloudFront.
  link: [must be in the same Region](../facts/acm.md#acm-faq-certificate-same-region-as-resource)
  link: [The only exception is Amazon CloudFront](../facts/acm.md#acm-faq-certificate-same-region-as-resource)
acm-faq-cloudtrail-elb-kms-decrypt
  claim: CloudTrail shows which user associated an ACM certificate with an Elastic Load Balancer, and when Elastic Load Balancing decrypted the key with a KMS API call.
  scope: ACM certificates used with Elastic Load Balancing.
  link: [decrypted the key with a KMS API call](../facts/acm.md#acm-faq-cloudtrail-elb-kms-decrypt)
  link: [which user made an API call](../facts/acm.md#acm-faq-cloudtrail-elb-kms-decrypt)
acm-faq-cloudtrail-private-key-use
  claim: Using AWS CloudTrail, you can review logs that tell you when the private key for a certificate was used.
  scope: per certificate.
  link: [AWS CloudTrail](../facts/acm.md#acm-faq-cloudtrail-private-key-use)
  link: [the private key for the certificate was used](../facts/acm.md#acm-faq-cloudtrail-private-key-use)
acm-faq-copied-across-regions-only-cloudfront
  claim: ACM copies certificates across Regions only if the certificate is associated with a CloudFront distribution.
  scope: per certificate; associated with a CloudFront distribution.
  link: [only copied across Regions](../facts/acm.md#acm-faq-copied-across-regions-only-cloudfront)
  link: [associated with a CloudFront distribution](../facts/acm.md#acm-faq-copied-across-regions-only-cloudfront)
acm-faq-default-rsa-2048-sha-256
  claim: By default, certificates issued in ACM use RSA keys with a 2048-bit modulus and SHA-256.
  scope: per ACM-issued certificate; default; adjustable.
  link: [RSA keys with a 2048-bit modulus](../facts/acm.md#acm-faq-default-rsa-2048-sha-256)
  link: [SHA-256](../facts/acm.md#acm-faq-default-rsa-2048-sha-256)
  say: RSA keys with a twenty forty-eight bit modulus | SHA two fifty-six
acm-faq-dns-renew-indefinitely
  claim: With DNS validation, ACM can renew a certificate indefinitely without further action from you, as long as the certificate is in use (associated with other AWS resources) and the CNAME record stays in place.
  scope: DNS-validated ACM certificates; the certificate is in use and the CNAME record remains in place.
  link: [renew your certificate indefinitely](../facts/acm.md#acm-faq-dns-renew-indefinitely)
  link: [your CNAME record remains in place](../facts/acm.md#acm-faq-dns-renew-indefinitely)
acm-faq-dns-validation-any-provider
  claim: DNS validation works with any DNS provider that allows you to add a CNAME record.
  scope: per domain; provider allows CNAME records.
  link: [with any DNS provider](../facts/acm.md#acm-faq-dns-validation-any-provider)
  link: [allows you to add a CNAME record](../facts/acm.md#acm-faq-dns-validation-any-provider)
acm-faq-ecdsa-p256-p384
  claim: You can request ECDSA certificates in ACM with either P-256 or P-384.
  scope: per certificate request.
  link: [P-256 or P-384](../facts/acm.md#acm-faq-ecdsa-p256-p384)
  link: [Elliptic Curve Digital Signature Algorithm (ECDSA) certificates](../facts/acm.md#acm-faq-ecdsa-p256-p384)
  say: P two fifty-six or P three eighty-four
acm-faq-email-base-domain-superdomain
  claim: You cannot configure the approval email addresses for email validation, but you can configure the base domain name the validation email goes to, and that base domain must be a superdomain of the requested domain name.
  scope: per certificate request with email validation; email validation is chosen.
  link: [configure the base domain name](../facts/acm.md#acm-faq-email-base-domain-superdomain)
  link: [must be a superdomain of the domain name](../facts/acm.md#acm-faq-email-base-domain-superdomain)
acm-faq-email-renewal-conditions
  claim: For an email-validated certificate, ACM is better able to renew and deploy it automatically when the certificate is in use, all its domain names resolve to your site, and all its domain names are reachable from the Internet.
  scope: email-validated ACM certificates; email validation was chosen in the request.
  link: [all domain names are reachable from the Internet](../facts/acm.md#acm-faq-email-renewal-conditions)
  link: [ensuring that the certificate is in use](../facts/acm.md#acm-faq-email-renewal-conditions)
acm-faq-email-validation-still-supported
  claim: ACM continues to support email validation for customers who cannot change their DNS configuration, but ACM will no longer issue email-validated certificates starting March 31 2027 and will stop renewing email-validated certificates on September 30 2027.
  scope: public certificate requests.
  link: [ACM continues to support email validation](../facts/acm.md#acm-faq-email-validation-still-supported)
  link: [customers who can’t change their DNS configuration](../facts/acm.md#acm-faq-email-validation-still-supported)
acm-faq-exportable-pay-issuance-renewal
  claim: If you issue exportable public certificates, you pay for certificate issuance, certificate renewal and related API usage.
  scope: per exportable public certificate; exportable public certificates only.
  link: [you pay for certificate issuance, certificate renewal](../facts/acm.md#acm-faq-exportable-pay-issuance-renewal)
  link: [exportable public certificates](../facts/acm.md#acm-faq-exportable-pay-issuance-renewal)
acm-faq-free-with-integrated-services
  claim: Public and private certificates provisioned through ACM for use with ACM-integrated services, such as Elastic Load Balancing, Amazon CloudFront and Amazon API Gateway, are free.
  scope: per certificate; used with ACM-integrated services.
  link: [are free](../facts/acm.md#acm-faq-free-with-integrated-services)
  link: [for use with ACM-integrated services](../facts/acm.md#acm-faq-free-with-integrated-services)
acm-faq-http-validation-cloudfront-saas-manager
  claim: For certificates used with Amazon CloudFront SaaS Manager, ACM issues HTTP validated certificates automatically.
  scope: per certificate; certificates for CloudFront SaaS Manager.
  link: [ACM issues HTTP validated certificates automatically](../facts/acm.md#acm-faq-http-validation-cloudfront-saas-manager)
  link: [Amazon CloudFront SaaS Manager](../facts/acm.md#acm-faq-http-validation-cloudfront-saas-manager)
acm-faq-import-third-party-for-integrated-services
  claim: To use a third-party certificate with Amazon CloudFront, Elastic Load Balancing or Amazon API Gateway, you can import it into ACM with the console, AWS CLI or ACM APIs.
  scope: per imported certificate.
  link: [you may import it into ACM](../facts/acm.md#acm-faq-import-third-party-for-integrated-services)
  link: [third-party certificate](../facts/acm.md#acm-faq-import-third-party-for-integrated-services)
acm-faq-imported-no-managed-renewal
  claim: ACM does not manage the renewal process for imported certificates; you are responsible for monitoring their expiration dates and renewing them before they expire.
  scope: per imported certificate; imported third-party certificates.
  link: [does not manage the renewal process](../facts/acm.md#acm-faq-imported-no-managed-renewal)
  link: [You are responsible for monitoring the expiration date](../facts/acm.md#acm-faq-imported-no-managed-renewal)
acm-faq-issuance-several-hours
  claim: After all domain names in a request are validated, issuing the certificate may take several hours or longer.
  scope: per certificate request; after all domain names are validated.
  link: [several hours or longer](../facts/acm.md#acm-faq-issuance-several-hours)
  link: [have been validated](../facts/acm.md#acm-faq-issuance-several-hours)
acm-faq-issued-status
  claim: When the certificate is issued, the request status changes to Issued and you can start using the certificate with AWS services integrated with ACM.
  scope: per public certificate request; after all domain names are validated and the certificate is issued.
  link: [changes to Issued](../facts/acm.md#acm-faq-issued-status)
  link: [you can start using it](../facts/acm.md#acm-faq-issued-status)
acm-faq-key-pair-per-certificate
  claim: ACM creates a key pair for each certificate it provides.
  scope: per ACM-provided certificate.
  link: [A key pair is created for each certificate](../facts/acm.md#acm-faq-key-pair-per-certificate)
  link: [provided by ACM](../facts/acm.md#acm-faq-key-pair-per-certificate)
acm-faq-max-lifetime-under-100-days-2027
  claim: As of March 15, 2027, the maximum lifetime for a public TLS certificate issued will be less than 100 days.
  scope: per public TLS certificate; maximum; not adjustable; certificates issued as of March 15, 2027.
  link: [less than 100 days](../facts/acm.md#acm-faq-max-lifetime-under-100-days-2027)
  link: [March 15, 2027](../facts/acm.md#acm-faq-max-lifetime-under-100-days-2027)
  say: less than one hundred days | March fifteenth, twenty twenty-seven
acm-faq-max-lifetime-under-47-days-2029
  claim: As of March 15, 2029, the maximum lifetime for a public TLS certificate issued will be less than 47 days.
  scope: per public TLS certificate; maximum; not adjustable; certificates issued as of March 15, 2029.
  link: [less than 47 days](../facts/acm.md#acm-faq-max-lifetime-under-47-days-2029)
  link: [March 15, 2029](../facts/acm.md#acm-faq-max-lifetime-under-47-days-2029)
  say: less than forty-seven days | March fifteenth, twenty twenty-nine
acm-faq-no-sla
  claim: ACM does not have a service level agreement (SLA).
  scope: per service.
  link: [ACM does not have an SLA](../facts/acm.md#acm-faq-no-sla)
acm-faq-notify-if-cannot-validate
  claim: If ACM cannot validate domain ownership during renewal, it tells the AWS account owner.
  scope: public ACM certificates during managed renewal; ACM cannot validate domain ownership.
  link: [let you (the AWS account owner) know](../facts/acm.md#acm-faq-notify-if-cannot-validate)
  link: [If ACM cannot validate domain ownership](../facts/acm.md#acm-faq-notify-if-cannot-validate)
acm-faq-one-validation-method-per-certificate
  claim: Each ACM certificate can have only one validation method.
  scope: per certificate.
  link: [only one validation method](../facts/acm.md#acm-faq-one-validation-method-per-certificate)
acm-faq-pending-validation-status
  claim: While ACM tries to validate that you own or control the domain, the certificate request has the status Pending validation.
  scope: per public certificate request; domain validation is in progress.
  link: [Pending validation](../facts/acm.md#acm-faq-pending-validation-status)
  link: [attempts to validate that you own or control](../facts/acm.md#acm-faq-pending-validation-status)
acm-faq-private-ca-certs-on-own-servers
  claim: You can use private certificates issued with AWS Private CA on EC2 instances, on containers and on your own servers.
  scope: private certificates from AWS Private CA.
  link: [private certificates issued with Private CA](../facts/acm.md#acm-faq-private-ca-certs-on-own-servers)
  link: [EC2 instances, containers, and on your own servers](../facts/acm.md#acm-faq-private-ca-certs-on-own-servers)
acm-faq-private-ca-monthly-fee
  claim: You pay a monthly fee for the operation of each private CA until you delete it, and for private certificates you issue that are not used exclusively with ACM-integrated services.
  scope: per private CA, per month.
  link: [You pay a monthly fee](../facts/acm.md#acm-faq-private-ca-monthly-fee)
  link: [for the operation of each private CA](../facts/acm.md#acm-faq-private-ca-monthly-fee)
  link: [until you delete it](../facts/acm.md#acm-faq-private-ca-monthly-fee)
acm-faq-private-export-ec2-iot
  claim: You can export private certificates from ACM and use them with EC2 instances, containers, on-premises servers and IoT devices.
  scope: private certificates managed through ACM.
  link: [export private certificates from ACM](../facts/acm.md#acm-faq-private-export-ec2-iot)
  link: [on-premises servers, and IoT devices](../facts/acm.md#acm-faq-private-export-ec2-iot)
acm-faq-private-key-stored-in-request-region
  claim: The private key of each ACM certificate is stored in the Region in which you request the certificate.
  scope: per certificate.
  link: [stored in the Region](../facts/acm.md#acm-faq-private-key-stored-in-request-region)
  link: [in which you request the certificate](../facts/acm.md#acm-faq-private-key-stored-in-request-region)
acm-faq-private-renewal-ca-active
  claim: ACM can renew and deploy private certificates issued through ACM as long as the private CA that issued the certificate remains in the Active state.
  scope: per private certificate; issuing private CA is Active.
  link: [remains in the Active state](../facts/acm.md#acm-faq-private-renewal-ca-active)
  link: [ACM can renew and deploy private certificates](../facts/acm.md#acm-faq-private-renewal-ca-active)
acm-faq-public-cert-internal-load-balancer
  claim: You can use public certificates for internal Elastic Load Balancing load balancers, but you can also consider AWS Private CA private certificates, which ACM can renew without validation.
  scope: per internal load balancer; load balancer with no public internet access.
  link: [renew without validation](../facts/acm.md#acm-faq-public-cert-internal-load-balancer)
  link: [consider using AWS Private CA](../facts/acm.md#acm-faq-public-cert-internal-load-balancer)
acm-faq-public-internet-private-networks
  claim: Public certificates identify resources on the public Internet, whereas private certificates do the same for private networks.
  scope: per certificate.
  link: [resources on the public Internet](../facts/acm.md#acm-faq-public-internet-private-networks)
  link: [do the same for private networks](../facts/acm.md#acm-faq-public-internet-private-networks)
acm-faq-public-validity-and-private-ca-any-period
  claim: Public certificates issued through ACM are valid for 198 days, except ACME-issued certificates, which are valid for 45 days; private certificates issued directly from a private CA without ACM certificate management can use any validity period.
  scope: per certificate.
  link: [198 days](../facts/acm.md#acm-faq-public-validity-and-private-ca-any-period)
  link: [you can choose any validity period](../facts/acm.md#acm-faq-public-validity-and-private-ca-any-period)
  link: [45 days](../facts/acm.md#acm-faq-public-validity-and-private-ca-any-period)
  say: one hundred ninety-eight days | forty-five days
acm-faq-public-vs-private-trust
  claim: Applications and browsers trust public certificates automatically by default, whereas an administrator must explicitly configure applications to trust private certificates.
  scope: per certificate; default.
  link: [trust public certificates automatically by default](../facts/acm.md#acm-faq-public-vs-private-trust)
  link: [must explicitly configure applications to trust](../facts/acm.md#acm-faq-public-vs-private-trust)
acm-faq-recommend-dns-validation
  claim: AWS recommends DNS validation when you can change the DNS configuration for your domain; use email validation if you cannot.
  scope: per certificate request; certificates issued directly from ACM.
  link: [we recommend that you use DNS validation](../facts/acm.md#acm-faq-recommend-dns-validation)
  link: [you should use email validation](../facts/acm.md#acm-faq-recommend-dns-validation)
acm-faq-remove-cname-stops-renewal
  claim: ACM cannot issue or renew certificates for your domain using DNS validation if you remove the CNAME record.
  scope: per domain; DNS validation, CNAME record removed.
  link: [cannot issue or renew certificates](../facts/acm.md#acm-faq-remove-cname-stops-renewal)
  link: [if you remove the CNAME record](../facts/acm.md#acm-faq-remove-cname-stops-renewal)
acm-faq-renew-public-without-extra-validation
  claim: ACM can renew and deploy public ACM certificates without any additional validation from the domain owner.
  scope: public ACM certificates.
  link: [without any additional validation from the domain owner](../facts/acm.md#acm-faq-renew-public-without-extra-validation)
  link: [renew and deploy public ACM certificates](../facts/acm.md#acm-faq-renew-public-without-extra-validation)
acm-faq-renewal-existing-connections-unaffected
  claim: When ACM deploys a renewed certificate, existing connections are not affected; connections established after deployment use the new certificate.
  scope: per deployed certificate; after ACM deploys the renewed certificate.
  link: [existing connections are not affected](../facts/acm.md#acm-faq-renewal-existing-connections-unaffected)
  link: [use the new certificate](../facts/acm.md#acm-faq-renewal-existing-connections-unaffected)
acm-faq-renewal-without-prior-notice
  claim: ACM may renew or rekey a certificate and replace the old one without prior notice.
  scope: per certificate.
  link: [without prior notice](../facts/acm.md#acm-faq-renewal-without-prior-notice)
  link: [renew or rekey the certificate](../facts/acm.md#acm-faq-renewal-without-prior-notice)
acm-faq-revoke-exportable-api
  claim: Exportable public certificates can be revoked with the revoke-certificate API.
  scope: per exportable public certificate.
  link: [revoke-certificate API](../facts/acm.md#acm-faq-revoke-exportable-api)
  link: [Exportable public certificates](../facts/acm.md#acm-faq-revoke-exportable-api)
acm-faq-revoke-public-via-support-case
  claim: To have ACM revoke a public certificate, you create a case in the AWS Support Center.
  scope: per public certificate; public certificates that are not exportable.
  link: [the AWS Support Center and creating a case](../facts/acm.md#acm-faq-revoke-public-via-support-case)
  link: [revoke a public certificate](../facts/acm.md#acm-faq-revoke-public-via-support-case)
acm-faq-route53-console-adds-records
  claim: For Route 53 DNS customers, the ACM console can add the validation records to the DNS configuration when you request a certificate, if the hosted zone is in the same AWS account.
  scope: per hosted zone; hosted zone in the same AWS account; sufficient Route 53 permissions.
  link: [the ACM console can add records](../facts/acm.md#acm-faq-route53-console-adds-records)
  link: [configured in the same AWS account](../facts/acm.md#acm-faq-route53-console-adds-records)
acm-faq-unique-cname-per-domain-name
  claim: Each domain name must have a unique CNAME record for ACM DNS validation; one record cannot validate all subdomains.
  scope: per domain name; DNS validation.
  link: [must have a unique CNAME record](../facts/acm.md#acm-faq-unique-cname-per-domain-name)
  link: [must be validated separately](../facts/acm.md#acm-faq-unique-cname-per-domain-name)
acm-faq-www-and-apex-need-both-names
  claim: A certificate for www.example.com does not also cover example.com; to serve both names you must request a certificate that includes both names.
  scope: per certificate; site reached by both www and apex names.
  link: [you must request a certificate](../facts/acm.md#acm-faq-www-and-apex-need-both-names)
  link: [includes both names](../facts/acm.md#acm-faq-www-and-apex-need-both-names)
acm-generates-key-automates-renewal
  claim: Use ACM for certificates on integrated services such as Elastic Load Balancing, CloudFront and API Gateway or when you want AWS to manage the lifecycle; ACM generates and manages the private key and automates renewal.
  scope: per certificate.
  link: [ACM generates and manages the private key](../facts/acm.md#acm-generates-key-automates-renewal)
  link: [want AWS to manage the certificate lifecycle](../facts/acm.md#acm-generates-key-automates-renewal)
  link: [automates renewal](../facts/acm.md#acm-generates-key-automates-renewal)
acm-http-validation-cloudfront-only
  claim: HTTP validation is for certificates used with CloudFront and is currently available only through the CloudFront Distribution Tenants feature; it uses HTTP redirects and offers automatic renewal like DNS validation.
  scope: per CloudFront certificate.
  link: [only available through the CloudFront Distribution Tenants feature](../facts/acm.md#acm-http-validation-cloudfront-only)
  link: [uses HTTP redirects to prove domain ownership](../facts/acm.md#acm-http-validation-cloudfront-only)
acm-http-validation-no-wildcard
  claim: With CloudFront, HTTP validation does not support wildcard certificates; a wildcard certificate needs DNS or email validation, and AWS recommends DNS validation.
  scope: certificates used with CloudFront.
  link: [HTTP validation does not support wildcard certificates](../facts/acm.md#acm-http-validation-no-wildcard)
  link: [We recommend DNS validation](../facts/acm.md#acm-http-validation-no-wildcard)
acm-import-pem-encoded
  claim: To import a certificate into ACM, the certificate, private key and certificate chain must all be PEM-encoded; DER-encoded materials cause an error.
  scope: per imported certificate.
  link: [must be PEM–encoded](../facts/acm.md#acm-import-pem-encoded)
  link: [Uploading DER–encoded materials results in an error](../facts/acm.md#acm-import-pem-encoded)
acm-import-reasons
  claim: You might import a certificate into ACM because you already have one from a third-party CA, or because of application-specific requirements that ACM-issued certificates do not meet.
  scope: per certificate.
  link: [from a third-party certificate authority (CA)](../facts/acm.md#acm-import-reasons)
  link: [not met by ACM issued certificates](../facts/acm.md#acm-import-reasons)
acm-imported-regional-cloudfront
  claim: Imported certificates are Regional too: import into each Region where a load balancer uses it, and into US East (N. Virginia) for CloudFront.
  scope: per Region.
  link: [including the certificates that you import](../facts/acm.md#acm-imported-regional-cloudfront)
  link: [US East (N. Virginia)](../facts/acm.md#acm-imported-regional-cloudfront)
acm-network-firewall-tls-inspection
  claim: AWS Network Firewall integrates with ACM for TLS inspection, and you must configure an ACM certificate to decrypt and re-encrypt the inspected traffic.
  scope: per Network Firewall TLS inspection configuration.
  link: [integrates with ACM for TLS inspection](../facts/acm.md#acm-network-firewall-tls-inspection)
  link: [you must configure an ACM certificate](../facts/acm.md#acm-network-firewall-tls-inspection)
acm-no-validation-private-or-imported
  claim: Domain validation applies only to publicly trusted certificates issued by ACM; imported and private certificates are not validated by ACM.
  scope: per certificate.
  link: [Validation applies only to publicly trusted certificates](../facts/acm.md#acm-no-validation-private-or-imported)
  link: [requires no validation](../facts/acm.md#acm-no-validation-private-or-imported)
acm-no-whois-email-validation
  claim: ACM no longer supports WHOIS email validation for new certificates or renewals; the common system addresses remain supported.
  scope: per email-validated certificate.
  link: [no longer supports WHOIS email validation](../facts/acm.md#acm-no-whois-email-validation)
  link: [Common system addresses remain supported](../facts/acm.md#acm-no-whois-email-validation)
acm-option-best-for-row
  claim: AWS's option table says ACM is best for public or private certificates for integrated services, ACM with ACME for public certificates on customer-managed infrastructure, and AWS Private CA direct issuance for private certificates where you supply the CSR and manage the private key.
  scope: per certificate.
  link: [Public or private certificates for AWS integrated services](../facts/acm.md#acm-option-best-for-row)
  link: [Public certificates for customer-managed infrastructure](../facts/acm.md#acm-option-best-for-row)
  link: [Private certificates where you supply the CSR](../facts/acm.md#acm-option-best-for-row)
acm-option-private-key-row
  claim: In AWS's option table, AWS generates and manages the private key for ACM certificates (you can export it for use outside AWS); with ACME your client holds the key; with Private CA direct issuance you generate and hold it.
  scope: per certificate.
  link: [AWS generates and manages the private key](../facts/acm.md#acm-option-private-key-row)
  link: [you can export it for use outside AWS](../facts/acm.md#acm-option-private-key-row)
acm-option-renewal-row
  claim: In AWS's option table, renewal is automatic ACM managed renewal for ACM certificates, client-driven for ACME, and manual (you call IssueCertificate again) for AWS Private CA direct issuance.
  scope: per certificate.
  link: [ACM managed renewal (automatic)](../facts/acm.md#acm-option-renewal-row)
  link: [Manual (you call IssueCertificate again)](../facts/acm.md#acm-option-renewal-row)
acm-price-acme-fqdn-first-tier
  claim: The first 1k fully qualified domain names issued on ACME certificates cost $1.00 per domain, per account per month.
  scope: per account per month, first 1k fully qualified domain names; lower prices apply at higher volume tiers.
  link: [$1.00 per domain](../facts/acm.md#acm-price-acme-fqdn-first-tier)
  say: one dollar per domain
acm-price-exportable-certificate
  claim: An exportable public certificate costs $7.00 per standard fully qualified domain name and $79.00 per wildcard name, charged upon issuance and again only on certificate renewal; with the reduction in validity from 395 to 198 days, AWS reduced these prices from $15/FQDN and $149/wildcard name.
  scope: per name in an exportable public certificate; charged upon issuance and again only on certificate renewal; an initial tier of 10,000 API calls for exportable certificates is available at no charge.
  link: [$7.00](../facts/acm.md#acm-price-exportable-certificate)
  link: [$79.00](../facts/acm.md#acm-price-exportable-certificate)
  say: seven dollars per fully qualified domain name | seventy-nine dollars per wildcard name
  changed: 2026-02-18: was $15/FQDN
acm-price-public-certificate-integrated
  claim: ACM issues public (non-exportable) certificates at no cost for use with services integrated with ACM.
  scope: per non-exportable public certificate.
  link: [No cost](../facts/acm.md#acm-price-public-certificate-integrated)
  link: [at no cost for use with services integrated](../facts/acm.md#acm-price-public-certificate-integrated)
acm-private-ca-cross-account-policy
  claim: AWS Private CA can sign ACM certificates across accounts: the signing CA and the ACM certificate reside in different AWS accounts, and access to the CA has been granted to the account where the certificate resides.
  scope: per private CA.
  link: [reside in different AWS accounts](../facts/acm.md#acm-private-ca-cross-account-policy)
  link: [access to the CA has been granted](../facts/acm.md#acm-private-ca-cross-account-policy)
acm-private-ca-free-trial
  claim: Any AWS account can try AWS Private CA with no CA operation charge for the first 30 days for the first private CA created in the account in each Region; certificates issued during the trial are charged.
  scope: first private CA per account per Region; covers the CA operation charge only.
  link: [the first 30 days](../facts/acm.md#acm-private-ca-free-trial)
  say: the first thirty days
acm-private-ca-not-public
  claim: Certificates issued by a private CA are not publicly trusted and cannot be used on the public internet; use AWS Private CA directly when you need private certificates with full control of the private key.
  scope: per private certificate.
  link: [not publicly trusted](../facts/acm.md#acm-private-ca-not-public)
  link: [cannot be used on the public internet](../facts/acm.md#acm-private-ca-not-public)
  link: [want full control over the private key](../facts/acm.md#acm-private-ca-not-public)
acm-private-ca-price-per-ca-month
  claim: Operating an AWS Private CA costs $400 per private CA per month in general-purpose mode and $50 per private CA per month in short-lived certificate mode.
  scope: per private CA, per month; pro-rated for partial months; certificates are charged separately.
  link: [$400 per private CA per month](../facts/acm.md#acm-private-ca-price-per-ca-month)
  link: [$50 per private CA per month](../facts/acm.md#acm-private-ca-price-per-ca-month)
  say: four hundred dollars per private CA per month | fifty dollars per private CA per month
acm-private-ca-short-lived-mode-7-days
  claim: AWS Private CA general-purpose mode can issue certificates with any validity period, while short-lived certificate mode can only issue certificates valid for up to 7 days.
  scope: per certificate from a short-lived certificate mode private CA; maximum; not adjustable; general-purpose mode has no such limit.
  link: [up to 7 days](../facts/acm.md#acm-private-ca-short-lived-mode-7-days)
  say: up to seven days
acm-private-certificate-validity
  claim: Private certificates through ACM remain valid for 13 months (395 days) after the 2026-02-18 change to public certificates.
  scope: per private certificate managed by ACM; fixed; not adjustable; applies to private certificates managed by ACM.
  link: [13 months (395 days)](../facts/acm.md#acm-private-certificate-validity)
  say: thirteen months, three hundred ninety-five days
acm-private-needs-existing-private-ca
  claim: If you have access to an existing private CA created by AWS Private CA, ACM can request a private certificate from it; the CA can be in your account or shared with you by a different account.
  scope: per private certificate.
  link: [an existing private CA](../facts/acm.md#acm-private-needs-existing-private-ca)
  link: [shared with you by a different account](../facts/acm.md#acm-private-needs-existing-private-ca)
acm-private-renewal-only-acm-issued
  claim: ACM certificates signed by a private CA from AWS Private CA are eligible for managed renewal, but with AWS Private CA direct issuance renewal is manual: you call IssueCertificate again.
  scope: per private certificate.
  link: [Manual (you call IssueCertificate again)](../facts/acm.md#acm-private-renewal-only-acm-issued)
  link: [eligible for managed renewal](../facts/acm.md#acm-private-renewal-only-acm-issued)
acm-private-renewed-deploys-if-integrated
  claim: ACM can fully automate renewal and deployment of private certificates issued with AWS Private CA and used with ACM-integrated services such as Elastic Load Balancing and API Gateway, as long as the private CA that issued the certificate remains in the Active state; for private certificates you export from ACM, ACM renews them automatically, but you are responsible for retrieving the new certificate and private key and deploying them.
  scope: per renewed certificate; the issuing private CA remains in the Active state.
  link: [fully automate renewal and deployment](../facts/acm.md#acm-private-renewed-deploys-if-integrated)
  link: [You are responsible for retrieving the new certificate](../facts/acm.md#acm-private-renewed-deploys-if-integrated)
acm-public-certificate-renewal-window
  claim: Since 2026-02-18, ACM renews public certificates 45 days before expiration; certificates that still have the older validity renew 60 days before expiry.
  scope: per ACM public certificate; fixed; not adjustable; ACM automatically renews DNS-validated certificates while a certificate remains in use and the DNS record is in place; email-validated certificates require an action by the domain owner.
  link: [45 days before expiration](../facts/acm.md#acm-public-certificate-renewal-window)
  link: [60 days before expiry](../facts/acm.md#acm-public-certificate-renewal-window)
  say: forty-five days before expiration | sixty days before expiry
  changed: 2026-02-18: was 60 days before expiry
acm-public-certificate-validity
  claim: ACM public certificates are valid for 198 days, except ACME-issued certificates, which are valid for 45 days; before 2026-02-18 ACM public certificates were valid for 13 months (395 days).
  scope: per ACM public certificate; fixed; not adjustable; applies to new and renewed ACM public certificates other than ACME-issued certificates; private certificates through ACM remain valid for 13 months.
  link: [198 days](../facts/acm.md#acm-public-certificate-validity)
  link: [395 days](../facts/acm.md#acm-public-certificate-validity)
  link: [45 days](../facts/acm.md#acm-public-certificate-validity)
  say: one hundred ninety-eight days | three hundred ninety-five days, about thirteen months | forty-five days
  changed: 2026-02-18: was 13 months (395 days)
acm-quota-acme-domain-names-per-certificate
  claim: A certificate issued through ACME can include up to 100 domain names, and this quota is fixed and cannot be increased.
  scope: per ACME-issued certificate; fixed; not adjustable.
  link: [up to 100 domain names](../facts/acm.md#acm-quota-acme-domain-names-per-certificate)
  say: up to one hundred domain names
acm-quota-acme-endpoints
  claim: An account can have 50 ACME endpoints in each Region by default, and the quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [50](../facts/acm.md#acm-quota-acme-endpoints)
  say: fifty
acm-quota-certificates-per-region
  claim: An account can have 2,500 ACM certificates in each Region by default, and the quota is adjustable.
  scope: per account, per Region; default; adjustable; certificates signed by a CA from AWS Private CA and certificates issued through ACME do not count; the General Reference says only certificates in the PENDING or ISSUED state count, while the ACM quotas page says expired and revoked certificates continue to count.
  link: [2,500](../facts/acm.md#acm-quota-certificates-per-region)
  say: two thousand five hundred
acm-quota-certificates-per-year
  claim: An account can request 5,000 ACM certificates in the last 365 days in each Region by default, and the quota is adjustable.
  scope: per account, per Region, per 365 days; default; adjustable.
  link: [5,000](../facts/acm.md#acm-quota-certificates-per-year)
  say: five thousand
acm-quota-domain-names-per-certificate
  claim: An ACM certificate can include 10 domain names by default; the quota is adjustable and you can request up to 100 domain names. The quota does not apply to imported certificates.
  scope: per ACM-provided certificate; default; adjustable; does not apply to imported certificates; the first name becomes the subject common name and all names go into the Subject Alternative Name extension.
  link: [10](../facts/acm.md#acm-quota-domain-names-per-certificate)
  link: [up to 100 domain names](../facts/acm.md#acm-quota-domain-names-per-certificate)
  say: ten domain names | up to one hundred domain names
acm-quota-imported-certificates
  claim: An account can have 2,500 imported certificates in each Region by default, and can import 5,000 certificates in the last 365 days; both quotas are adjustable.
  scope: per account, per Region; default; adjustable.
  link: [2,500](../facts/acm.md#acm-quota-imported-certificates)
  link: [5,000](../facts/acm.md#acm-quota-imported-certificates)
  say: two thousand five hundred | five thousand per year
acm-reimport-keeps-arn
  claim: To renew an imported certificate, you get a new certificate from your issuer and reimport it into ACM, which keeps the certificate's associations and its ARN.
  scope: per imported certificate; reimport before it expires.
  link: [This action preserves the certificate's association](../facts/acm.md#acm-reimport-keeps-arn)
  link: [preserving the AWS service associations](../facts/acm.md#acm-reimport-keeps-arn)
  link: [Amazon Resource name (ARN)](../facts/acm.md#acm-reimport-keeps-arn)
acm-renewal-eligibility
  claim: A certificate is eligible for automatic renewal if it is associated with another AWS service such as Elastic Load Balancing or CloudFront, or has been exported since it was issued or last renewed; imported certificates, already expired certificates, private certificates issued by calling the AWS Private CA IssueCertificate API, and certificates issued through ACME are not eligible for ACM managed renewal.
  scope: per certificate.
  link: [ELIGIBLE if associated with another AWS service](../facts/acm.md#acm-renewal-eligibility)
  link: [NOT ELIGIBLE if already expired](../facts/acm.md#acm-renewal-eligibility)
acm-renewal-keeps-arn-per-region
  claim: When ACM renews a certificate its ARN stays the same, and certificates for the same domain in several Regions are renewed independently.
  scope: per certificate.
  link: [Amazon Resource Name (ARN) remains the same](../facts/acm.md#acm-renewal-keeps-arn-per-region)
  link: [each of these certificates must be renewed independently](../facts/acm.md#acm-renewal-keeps-arn-per-region)
acm-renewal-status-failed
  claim: A renewal status of Failed means one or more domain names were not validated before the certificate expired and ACM did not renew it; Pending validation means you must act to validate the domain names or the certificate will not be renewed.
  scope: per certificate.
  link: [ACM did not renew the certificate](../facts/acm.md#acm-renewal-status-failed)
  link: [You must take action to validate](../facts/acm.md#acm-renewal-status-failed)
acm-renewal-status-where
  claim: You can check the renewal status of an ACM certificate in the ACM console, the ACM API, the AWS CLI or the Health Dashboard.
  scope: per certificate.
  link: [the Health Dashboard to check the renewal status](../facts/acm.md#acm-renewal-status-where)
  link: [Renewal status](../facts/acm.md#acm-renewal-status-where)
acm-renewal-uses-same-method
  claim: When a public certificate comes up for renewal, ACM re-validates ownership with the same method you chose when you requested it.
  scope: per public certificate.
  link: [uses the same method that you chose earlier](../facts/acm.md#acm-renewal-uses-same-method)
  link: [to re-validate your ownership](../facts/acm.md#acm-renewal-uses-same-method)
acm-stop-dns-renewal
  claim: You stop automatic renewal of a DNS-validated certificate by removing it from the AWS service it is associated with or by deleting the CNAME record.
  scope: per certificate.
  link: [You can stop automatic renewal](../facts/acm.md#acm-stop-dns-renewal)
  link: [by deleting the CNAME record](../facts/acm.md#acm-stop-dns-renewal)
acm-three-certificate-types
  claim: ACM supports three types of certificates: public certificates trusted across the internet, private certificates that are not publicly trusted and are used inside an organization, and imported certificates from third-party certificate authorities.
  scope: per certificate.
  link: [supports three types of certificates](../facts/acm.md#acm-three-certificate-types)
  link: [Publicly trusted across the internet](../facts/acm.md#acm-three-certificate-types)
acm-three-validation-methods
  claim: ACM must prove that you own or control every domain name in the request; you can choose DNS validation, email validation or HTTP validation.
  scope: per public certificate.
  link: [email validation, or HTTP validation](../facts/acm.md#acm-three-validation-methods)
  link: [own or control all of the domain names](../facts/acm.md#acm-three-validation-methods)
acm-wa-alb-apigw-mtls
  claim: Both API Gateway and Application Load Balancer support mutual TLS (mTLS) with client certificates.
  scope: per API Gateway API or ALB.
  link: [support mutual TLS (mTLS) using client certificates](../facts/acm.md#acm-wa-alb-apigw-mtls)
acm-wa-alb-strongest-security-policy
  claim: For a load balancer listener, choose the security policy with the strongest cipher suites that the connecting clients support.
  scope: per load balancer listener.
  link: [the strongest cipher suites supported by the clients](../facts/acm.md#acm-wa-alb-strongest-security-policy)
acm-wa-aws-apis-tls-12-minimum
  claim: Clients should call AWS APIs with at least TLS 1.2, because AWS deprecated earlier TLS versions as of February 2024.
  scope: per client call to an AWS API endpoint; minimum; not adjustable.
  link: [at least TLS 1.2](../facts/acm.md#acm-wa-aws-apis-tls-12-minimum)
acm-wa-ca-hierarchy-separate-accounts
  claim: Well-Architected recommends deploying each level of a private CA hierarchy in a separate AWS account, with the root CA in its own account used only to issue intermediate CA certificates.
  scope: per workload.
  link: [into separate AWS accounts](../facts/acm.md#acm-wa-ca-hierarchy-separate-accounts)
  link: [should reside in its own separate account](../facts/acm.md#acm-wa-ca-hierarchy-separate-accounts)
acm-wa-cert-anti-patterns
  claim: Well-Architected SEC09-BP01 lists as common anti-patterns manual steps during certificate deployment or renewal, and self-signed certificates for public resources.
  scope: per workload.
  link: [Using self-signed certificates for public resources](../facts/acm.md#acm-wa-cert-anti-patterns)
  link: [manual steps during the certificate deployment or renewal](../facts/acm.md#acm-wa-cert-anti-patterns)
acm-wa-encrypt-outside-vpc
  claim: Well-Architected SEC09-BP02 says to use only encrypted protocols when sending sensitive data outside your VPC.
  scope: per workload.
  link: [Only use protocols with encryption](../facts/acm.md#acm-wa-encrypt-outside-vpc)
  link: [outside of your virtual private cloud (VPC)](../facts/acm.md#acm-wa-encrypt-outside-vpc)
acm-wa-key-material-no-humans
  claim: Well-Architected's desired outcome for certificate management is that key material is never accessible to human identities and certificates renew automatically.
  scope: per workload.
  link: [never be accessible to human identities](../facts/acm.md#acm-wa-key-material-no-humans)
  link: [automatically renews the certificate on a periodic basis](../facts/acm.md#acm-wa-key-material-no-humans)
acm-wa-primary-certificate-service
  claim: The Well-Architected Framework names ACM as the primary service to provision, manage and deploy certificates for both public-facing and private AWS workloads.
  scope: per workload.
  link: [ACM is the primary service](../facts/acm.md#acm-wa-primary-certificate-service)
  link: [both public-facing as well as private AWS workloads](../facts/acm.md#acm-wa-primary-certificate-service)
acm-wa-private-ca-own-trust-chain
  claim: AWS Private CA lets you set up your own root or subordinate certificate authority and issue TLS certificates through an API, for cases where you control the trust chain on the client side.
  scope: per workload.
  link: [establish your own root or subordinate certificate authority](../facts/acm.md#acm-wa-private-ca-own-trust-chain)
  link: [you control and manage the trust chain](../facts/acm.md#acm-wa-private-ca-own-trust-chain)
acm-wa-recommend-tls-13
  claim: The Well-Architected Framework recommends TLS 1.3 for encryption in transit.
  scope: per workload.
  link: [TLS 1.3](../facts/acm.md#acm-wa-recommend-tls-13)
acm-wa-security-group-https-only
  claim: To enforce encryption in transit, a security group can allow only HTTPS to an Application Load Balancer or EC2 instance, and insecure HTTP can be blocked in a VPC with security groups.
  scope: per workload.
  link: [only allow the HTTPS protocol](../facts/acm.md#acm-wa-security-group-https-only)
  link: [audited and blocked](../facts/acm.md#acm-wa-security-group-https-only)
acm-wa-transit-anti-patterns
  claim: Well-Architected SEC09-BP02 lists as anti-patterns allowing unencrypted HTTP traffic to or from public-facing resources and not monitoring and replacing X.509 certificates before they expire.
  scope: per workload.
  link: [Allowing unencrypted (HTTP) traffic](../facts/acm.md#acm-wa-transit-anti-patterns)
  link: [Not monitoring and replacing X.509 certificates prior to expiration](../facts/acm.md#acm-wa-transit-anti-patterns)
acm-what-it-does
  claim: AWS Certificate Manager (ACM) handles creating, storing and renewing public and private SSL/TLS X.509 certificates and keys that protect AWS websites and applications.
  scope: per certificate.
  link: [creating, storing, and renewing public and private SSL/TLS X.509 certificates](../facts/acm.md#acm-what-it-does)
  link: [handles the complexity](../facts/acm.md#acm-what-it-does)
acm-wildcard-one-level-not-apex
  claim: In a wildcard certificate the asterisk must be leftmost and protects only one subdomain level, and *.example.com protects only subdomains, not the apex example.com; request both names to cover both.
  scope: per wildcard certificate.
  link: [protects only one subdomain level](../facts/acm.md#acm-wildcard-one-level-not-apex)
  link: [not the bare or apex domain](../facts/acm.md#acm-wildcard-one-level-not-apex)
acm-wildcard-unlimited-subdomains
  claim: ACM certificates can secure single domain names, several specific domain names, wildcard domains or combinations, and a wildcard certificate can protect an unlimited number of subdomains.
  scope: per certificate.
  link: [can protect an unlimited number of subdomains](../facts/acm.md#acm-wildcard-unlimited-subdomains)
  link: [multiple specific domain names, wildcard domains](../facts/acm.md#acm-wildcard-unlimited-subdomains)
parameter-store-ami-data-type-validation
  claim: Parameter Store performs no validation on the text you enter as a parameter value, with one exception: for a String parameter with the data type aws:ec2:image, it validates that the value is in the proper format for an Amazon EC2 AMI.
  scope: per String parameter; data type aws:ec2:image.
  link: [performs no validation on the text you enter](../facts/parameter-store.md#parameter-store-ami-data-type-validation)
  link: [aws:ec2:image](../facts/parameter-store.md#parameter-store-ami-data-type-validation)
parameter-store-ami-parameter-in-run-instances
  claim: A parameter with data type aws:ec2:image holds an AMI ID that you reference in templates, commands and scripts, so you do not have to update them each time the AMI changes.
  scope: per String parameter; data type aws:ec2:image.
  link: [avoid updating all your scripts and templates](../facts/parameter-store.md#parameter-store-ami-parameter-in-run-instances)
  link: [reference this parameter in your templates](../facts/parameter-store.md#parameter-store-ami-parameter-in-run-instances)
parameter-store-api-interaction-definition
  claim: A Parameter Store API interaction is one API request with one individual parameter, so a Get request that returns ten parameters counts as ten interactions.
  scope: per API request.
  link: [counts as ten Parameter Store API interactions](../facts/parameter-store.md#parameter-store-api-interaction-definition)
parameter-store-change-cross-account-sharing-2024
  claim: On 2024-02-21 Parameter Store added cross-account sharing of advanced parameters through resource sharing (AWS RAM) or within an AWS Organization.
  scope: advanced parameters.
  link: [2024-02-21](../facts/parameter-store.md#parameter-store-change-cross-account-sharing-2024)
  say: February twenty-first, twenty twenty-four
parameter-store-default-tier-new-only
  claim: Changing the default parameter tier affects only new parameters created without a tier; existing parameters are not affected.
  scope: per account and Region.
  link: [Existing parameters aren't affected](../facts/parameter-store.md#parameter-store-default-tier-new-only)
  link: [affects only new parameters](../facts/parameter-store.md#parameter-store-default-tier-new-only)
parameter-store-default-tier-options
  claim: The default parameter tier of an account and Region can be set to Standard, Advanced or Intelligent-Tiering; standard is the default tier.
  scope: per AWS account and Region; default; adjustable; changing the default tier affects only new parameters created without a tier.
  link: [`Standard`, `Advanced`, or `Intelligent-Tiering`](../facts/parameter-store.md#parameter-store-default-tier-options)
  link: [This is the default.](../facts/parameter-store.md#parameter-store-default-tier-options)
parameter-store-deny-all-get-actions
  claim: To deny access to a parameter, deny every action that can return its value (GetParameter, GetParameters, GetParameterHistory and GetParametersByPath); a deny on the parameter's own ARN does not stop the parameter from being returned by a call against a path above it.
  scope: per IAM policy.
  link: [deny every action that can return the value](../facts/parameter-store.md#parameter-store-deny-all-get-actions)
  link: [a call against a path above it](../facts/parameter-store.md#parameter-store-deny-all-get-actions)
parameter-store-ecs-env-resolved-at-start
  claim: Environment variables from Parameter Store are resolved when an ECS task starts; a running task needs a new task or a forced deployment to pick up a changed value.
  scope: per ECS task.
  link: [resolved when a task starts](../facts/parameter-store.md#parameter-store-ecs-env-resolved-at-start)
  link: [needs a new task or a forced deployment](../facts/parameter-store.md#parameter-store-ecs-env-resolved-at-start)
parameter-store-eventbridge-change-events
  claim: You can use Amazon EventBridge and Amazon SNS to be notified when a parameter or label version is created, updated or deleted, and about parameter policy events; events are emitted on a best-effort basis.
  scope: per account and Region.
  link: [Events are emitted on a best effort basis](../facts/parameter-store.md#parameter-store-eventbridge-change-events)
  link: [is created, updated, or deleted](../facts/parameter-store.md#parameter-store-eventbridge-change-events)
parameter-store-expiration-deletes
  claim: The Expiration policy deletes the parameter when its expiration date and time is reached.
  scope: per advanced parameter.
  link: [This policy deletes the parameter](../facts/parameter-store.md#parameter-store-expiration-deletes)
  link: [Expiration](../facts/parameter-store.md#parameter-store-expiration-deletes)
parameter-store-hierarchy-forward-slashes
  claim: A parameter hierarchy is a parameter name that includes a path you define with forward slashes, which helps you organize and manage parameters.
  scope: per parameter name.
  link: [define by using forward slashes](../facts/parameter-store.md#parameter-store-hierarchy-forward-slashes)
  link: [use parameter hierarchies to help you organize](../facts/parameter-store.md#parameter-store-hierarchy-forward-slashes)
parameter-store-hierarchy-max-levels
  claim: A parameter hierarchy can have at most 15 levels.
  scope: per parameter hierarchy; maximum; not adjustable.
  link: [15 levels](../facts/parameter-store.md#parameter-store-hierarchy-max-levels)
  say: fifteen levels
parameter-store-high-throughput-extra-cost
  claim: Parameter Store has a default throughput suited to lower-scale workloads; applications that need higher request rates can enable high-throughput mode for an additional cost.
  scope: per account and Region; default.
  link: [enable high-throughput mode for an additional cost](../facts/parameter-store.md#parameter-store-high-throughput-extra-cost)
  link: [default throughput suitable for lower-scale workloads](../facts/parameter-store.md#parameter-store-high-throughput-extra-cost)
parameter-store-intelligent-tiering
  claim: With Intelligent-Tiering as the default, Parameter Store creates a parameter in the standard tier when it meets the standard criteria and in the advanced tier when it does not.
  scope: per account and Region; default tier set to Intelligent-Tiering.
  link: [creates the parameter in the standard tier](../facts/parameter-store.md#parameter-store-intelligent-tiering)
  link: [creates the parameter in the advanced tier](../facts/parameter-store.md#parameter-store-intelligent-tiering)
parameter-store-labels-per-version
  claim: A parameter version can have at most 10 labels.
  scope: per parameter version; maximum; not adjustable.
  link: [ten labels](../facts/parameter-store.md#parameter-store-labels-per-version)
  say: ten labels
parameter-store-lambda-extension-cache
  claim: The AWS Parameters and Secrets Lambda Extension lets a Lambda function read and cache Parameter Store parameters and Secrets Manager secrets without an SDK, which reduces API calls (cost) and latency.
  scope: per Lambda function.
  link: [retrieves parameter values and caches them](../facts/parameter-store.md#parameter-store-lambda-extension-cache)
  link: [Parameter Store and AWS Secrets Manager](../facts/parameter-store.md#parameter-store-lambda-extension-cache)
parameter-store-lambda-extension-no-auto-refresh
  claim: The Lambda extension does not detect parameter value changes and does not refresh the cache before the TTL expires, so AWS recommends a shorter TTL for values that change often.
  scope: per Lambda function using the extension.
  link: [doesn't detect changes to the parameter value](../facts/parameter-store.md#parameter-store-lambda-extension-no-auto-refresh)
  link: [setting a shorter TTL value](../facts/parameter-store.md#parameter-store-lambda-extension-no-auto-refresh)
parameter-store-lambda-extension-ttl
  claim: The AWS Parameters and Secrets Lambda Extension uses a cached parameter value until its time-to-live (TTL) expires, then retrieves the value from Parameter Store again; you set the TTL with the SSM_PARAMETER_STORE_TTL environment variable. The extension uses the same credentials as those used to run the Lambda function, so the function's IAM role needs permissions to interact with Parameter Store.
  scope: per Lambda function; TTL set with SSM_PARAMETER_STORE_TTL.
  link: [Cached values expire after they pass their time-to-live](../facts/parameter-store.md#parameter-store-lambda-extension-ttl)
  link: [the same credentials as those used to run](../facts/parameter-store.md#parameter-store-lambda-extension-ttl)
parameter-store-lambda-extension-ttl-default
  claim: The AWS Parameters and Secrets Lambda Extension keeps a parameter in its cache for 300 s by default, and SSM_PARAMETER_STORE_TTL accepts 0 to 300 s; 0 bypasses the cache.
  scope: per Lambda function using the extension; default; adjustable; set with SSM_PARAMETER_STORE_TTL; ignored when the cache size is 0.
  link: [300 s](../facts/parameter-store.md#parameter-store-lambda-extension-ttl-default)
  say: three hundred seconds, which is five minutes
parameter-store-new-policy-overwrites
  claim: If you add a new policy to a parameter that already has policies, Systems Manager overwrites the attached policies and the existing ones are deleted.
  scope: per advanced parameter.
  link: [overwrites the policies attached to the parameter](../facts/parameter-store.md#parameter-store-new-policy-overwrites)
  link: [The existing policies are deleted](../facts/parameter-store.md#parameter-store-new-policy-overwrites)
parameter-store-no-automatic-rotation
  claim: Parameter Store does not provide automatic rotation for stored secrets; instead you can store the secret in Secrets Manager and reference it as a Parameter Store parameter.
  scope: per parameter.
  link: [doesn't provide automatic rotation services](../facts/parameter-store.md#parameter-store-no-automatic-rotation)
  link: [reference the secret as a Parameter Store parameter](../facts/parameter-store.md#parameter-store-no-automatic-rotation)
parameter-store-no-sensitive-in-string
  claim: Do not store sensitive data in a String or StringList parameter; for sensitive data that must stay encrypted, use only the SecureString type.
  scope: per parameter.
  link: [use only the `SecureString` parameter type](../facts/parameter-store.md#parameter-store-no-sensitive-in-string)
  link: [Don't store sensitive data in a `String`](../facts/parameter-store.md#parameter-store-no-sensitive-in-string)
parameter-store-nochange-notification
  claim: The NoChangeNotification policy sends an event in EventBridge if a parameter has not been modified for a set period, for example when an approved AMI ID must be reviewed.
  scope: per advanced parameter.
  link: [for a specified period of time](../facts/parameter-store.md#parameter-store-nochange-notification)
  link: [NoChangeNotification](../facts/parameter-store.md#parameter-store-nochange-notification)
parameter-store-only-value-encrypted
  claim: Only the value of a SecureString parameter is encrypted; the parameter name, description and other properties are not.
  scope: per SecureString parameter.
  link: [Parameter names, descriptions, and other properties aren't encrypted](../facts/parameter-store.md#parameter-store-only-value-encrypted)
parameter-store-policies-advanced-only
  claim: Parameter policies are available only for parameters in the advanced tier; the standard tier does not support them.
  scope: per parameter.
  link: [use the advanced parameters tier](../facts/parameter-store.md#parameter-store-policies-advanced-only)
  link: [Parameter policies are available for parameters](../facts/parameter-store.md#parameter-store-policies-advanced-only)
parameter-store-policies-async-scans
  claim: Parameter Store enforces parameter policies with asynchronous, periodic scans; after you create a policy, Parameter Store performs its action without further steps from you.
  scope: per parameter policy.
  link: [asynchronous, periodic scans](../facts/parameter-store.md#parameter-store-policies-async-scans)
  link: [you don't need to perform additional actions](../facts/parameter-store.md#parameter-store-policies-async-scans)
parameter-store-policy-types
  claim: Parameter Store offers three parameter policy types: Expiration, ExpirationNotification and NoChangeNotification.
  scope: per advanced parameter; advanced tier only.
  link: [`Expiration`, `ExpirationNotification`, and `NoChangeNotification`](../facts/parameter-store.md#parameter-store-policy-types)
  link: [an expiration date or *time to live*](../facts/parameter-store.md#parameter-store-policy-types)
parameter-store-price-advanced-parameter
  claim: Standard parameters have no additional charge; an advanced parameter costs $0.05 per month, prorated hourly when stored for less than a month.
  scope: per parameter, per month; prorated hourly for less than a month.
  link: [$0.05 per advanced parameter per month](../facts/parameter-store.md#parameter-store-price-advanced-parameter)
  link: [No additional charge](../facts/parameter-store.md#parameter-store-price-advanced-parameter)
  say: five cents per advanced parameter per month
parameter-store-price-api-interactions
  claim: Standard parameters with standard throughput have no API charge; with higher throughput, and for advanced parameters at any throughput, API interactions cost $0.05 per 10,000.
  scope: per 10,000 API interactions; free only for standard parameters with standard throughput.
  link: [$0.05 per 10,000 Parameter Store API interactions](../facts/parameter-store.md#parameter-store-price-api-interactions)
  say: five cents per ten thousand API interactions
parameter-store-public-ami-parameter-latest
  claim: Systems Manager provides public parameters for public AMIs maintained by AWS; when you launch instances with a public parameter, such as one under /aws/service/ami-amazon-linux-latest, you use the latest AMI, because the parameter always points to the latest AMI version in the Region.
  scope: per public AMI parameter, per Region; public AMIs maintained by AWS.
  link: [public parameters for public AMIs maintained by AWS](../facts/parameter-store.md#parameter-store-public-ami-parameter-latest)
  link: [always points to the latest version](../facts/parameter-store.md#parameter-store-public-ami-parameter-latest)
parameter-store-public-parameters-ami
  claim: Some AWS services publish public parameters; for example, Amazon EC2 publishes information about AMIs as public parameters.
  scope: per Region.
  link: [publishes information about Amazon Machine Images (AMIs)](../facts/parameter-store.md#parameter-store-public-parameters-ami)
  link: [as public parameters](../facts/parameter-store.md#parameter-store-public-parameters-ami)
parameter-store-reference-honors-secret-iam
  claim: Parameter Store honors the IAM policies on Secrets Manager secrets, and parameters that reference secrets cannot use Parameter Store versioning or history.
  scope: per reference.
  link: [honors AWS Identity and Access Management (IAM) policies](../facts/parameter-store.md#parameter-store-reference-honors-secret-iam)
  link: [can't use the Parameter Store versioning or history](../facts/parameter-store.md#parameter-store-reference-honors-secret-iam)
parameter-store-reference-pass-through
  claim: For references to Secrets Manager secrets, Parameter Store is a pass-through service: it keeps no data or metadata about the secret, and the reference is stateless.
  scope: per reference.
  link: [functions as a pass-through service](../facts/parameter-store.md#parameter-store-reference-pass-through)
  link: [The reference is stateless](../facts/parameter-store.md#parameter-store-reference-pass-through)
parameter-store-reference-secrets-manager-prefix
  claim: Parameter Store can reference Secrets Manager secrets, but the name must start with the reserved path /aws/reference/secretsmanager/.
  scope: per reference.
  link: [must begin with the following reserved path](../facts/parameter-store.md#parameter-store-reference-secrets-manager-prefix)
  link: [/aws/reference/secretsmanager/](../facts/parameter-store.md#parameter-store-reference-secrets-manager-prefix)
parameter-store-securestring-kms-keys
  claim: Parameter Store uses AWS KMS keys to encrypt SecureString values when you create or change them and to decrypt them when you access them; for both standard and advanced SecureString parameters, if you do not specify a key, it uses the AWS managed key aws/ssm, and you can use a customer managed key instead.
  scope: per SecureString parameter; default; you can specify a customer managed key instead.
  link: [AWS managed key that Systems Manager automatically creates](../facts/parameter-store.md#parameter-store-securestring-kms-keys)
  link: [aws/ssm](../facts/parameter-store.md#parameter-store-securestring-kms-keys)
parameter-store-securestring-needs-kms-decrypt
  claim: Retrieving a decrypted SecureString value requires kms:Decrypt on the KMS key that encrypted it, whatever Parameter Store operation is used; denying kms:Decrypt blocks decryption on every retrieval path.
  scope: per SecureString parameter.
  link: [requires `kms:Decrypt` permission on the key](../facts/parameter-store.md#parameter-store-securestring-needs-kms-decrypt)
  link: [regardless of which Parameter Store operation is used](../facts/parameter-store.md#parameter-store-securestring-needs-kms-decrypt)
parameter-store-securestring-no-charge-kms-may
  claim: Parameter Store does not charge to create a SecureString parameter, but AWS KMS charges can apply.
  scope: per SecureString parameter.
  link: [There is no charge from Parameter Store](../facts/parameter-store.md#parameter-store-securestring-no-charge-kms-may)
  link: [charges for using AWS KMS can apply](../facts/parameter-store.md#parameter-store-securestring-no-charge-kms-may)
parameter-store-securestring-not-for-secrets
  claim: AWS suggests SecureString for configuration values that need encryption, and recommends AWS Secrets Manager for secrets such as database credentials, API keys or tokens, because it offers automatic rotation and cross-Region replication.
  scope: per secret.
  link: [we recommend AWS Secrets Manager](../facts/parameter-store.md#parameter-store-securestring-not-for-secrets)
  link: [automatic rotation and cross-region replication](../facts/parameter-store.md#parameter-store-securestring-not-for-secrets)
parameter-store-separate-sensitive-path
  claim: AWS recommends granting narrow access rather than denying broad access, and keeping sensitive parameters under their own path.
  scope: per IAM policy.
  link: [Prefer granting narrow access over denying broad access](../facts/parameter-store.md#parameter-store-separate-sensitive-path)
  link: [Separate sensitive parameters into their own path](../facts/parameter-store.md#parameter-store-separate-sensitive-path)
parameter-store-share-securestring-cmk
  claim: To share a SecureString parameter, it must be encrypted with a customer managed key that you share separately through AWS KMS; AWS managed keys cannot be shared.
  scope: per SecureString parameter.
  link: [AWS managed keys cannot be shared](../facts/parameter-store.md#parameter-store-share-securestring-cmk)
  link: [must be encrypted with a customer managed key](../facts/parameter-store.md#parameter-store-share-securestring-cmk)
parameter-store-shared-billing
  claim: For a shared advanced parameter, the owning account pays for storage and each consuming account that calls the API pays for its usage.
  scope: per shared advanced parameter.
  link: [The owning account is charged for storage](../facts/parameter-store.md#parameter-store-shared-billing)
  link: [is charged for the parameter usage](../facts/parameter-store.md#parameter-store-shared-billing)
parameter-store-shared-full-arn
  claim: To read a parameter from another account you must give its full ARN as the name.
  scope: per shared parameter.
  link: [specify the full parameter ARN](../facts/parameter-store.md#parameter-store-shared-full-arn)
  link: [retrieve the parameter from another account](../facts/parameter-store.md#parameter-store-shared-full-arn)
parameter-store-shared-read-only
  claim: Consumer accounts get read-only access to shared parameters: they cannot update, delete or re-share them.
  scope: per shared parameter.
  link: [receive read-only access](../facts/parameter-store.md#parameter-store-shared-read-only)
  link: [can't update or delete the parameter](../facts/parameter-store.md#parameter-store-shared-read-only)
parameter-store-sharing-advanced-ram
  claim: Parameter Store shares parameters with other AWS accounts through AWS RAM, and a parameter must be in the advanced tier to be shared.
  scope: per parameter.
  link: [it must be in the advanced parameter tier](../facts/parameter-store.md#parameter-store-sharing-advanced-ram)
  link: [integrates with AWS Resource Access Manager (AWS RAM)](../facts/parameter-store.md#parameter-store-sharing-advanced-ram)
parameter-store-standard-free-with-restrictions
  claim: Standard parameters are available at no cost but have size and feature restrictions; the advanced tier offers higher limits and extra features at a cost.
  scope: per parameter.
  link: [higher limits and extra features, at a cost](../facts/parameter-store.md#parameter-store-standard-free-with-restrictions)
  link: [The advanced tier offers higher limits](../facts/parameter-store.md#parameter-store-standard-free-with-restrictions)
parameter-store-standard-is-default-tier
  claim: If you do not specify a tier, the default tier setting decides it, and by default Parameter Store sets that default to the standard tier.
  scope: per account and Region; default; adjustable; change it with UpdateServiceSetting.
  link: [the default setting to the standard parameter tier](../facts/parameter-store.md#parameter-store-standard-is-default-tier)
  link: [the default tier setting determines the tier](../facts/parameter-store.md#parameter-store-standard-is-default-tier)
parameter-store-standard-securestring-direct-kms
  claim: Parameter Store performs no cryptographic operations itself: it relies on AWS KMS, and standard SecureString parameters are encrypted and decrypted directly under the KMS key you specify.
  scope: per SecureString parameter; standard tier.
  link: [encrypted and decrypted directly under the KMS key](../facts/parameter-store.md#parameter-store-standard-securestring-direct-kms)
  link: [does not perform any cryptographic operations](../facts/parameter-store.md#parameter-store-standard-securestring-direct-kms)
parameter-store-standard-upgradeable-not-downgradeable
  claim: You can change a standard parameter to an advanced parameter, but you cannot change an advanced parameter back to standard.
  scope: per parameter.
  link: [can't change an advanced parameter](../facts/parameter-store.md#parameter-store-standard-upgradeable-not-downgradeable)
  link: [Not downgradeable](../facts/parameter-store.md#parameter-store-standard-upgradeable-not-downgradeable)
parameter-store-three-parameter-types
  claim: Parameter Store supports three parameter types: String, StringList and SecureString.
  scope: per parameter; fixed.
  link: [`String`, `StringList`, and `SecureString`](../facts/parameter-store.md#parameter-store-three-parameter-types)
  link: [three types of parameters](../facts/parameter-store.md#parameter-store-three-parameter-types)
  say: three types of parameters
parameter-store-throughput-delete-apis
  claim: DeleteParameter and DeleteParameters get 3 TPS by default and 5 TPS with higher throughput.
  scope: per account and Region, for DeleteParameter and DeleteParameters; default; adjustable; the higher value needs higher throughput enabled.
  link: [3 TPS](../facts/parameter-store.md#parameter-store-throughput-delete-apis)
  link: [5 TPS](../facts/parameter-store.md#parameter-store-throughput-delete-apis)
  say: three transactions per second | five transactions per second
parameter-store-throughput-get-default
  claim: With default throughput, GetParameter, GetParameters and GetParametersByPath share 40 TPS combined.
  scope: per account and Region, shared by GetParameter, GetParameters and GetParametersByPath; default; adjustable; can be raised by enabling higher throughput, which incurs a charge.
  link: [40 TPS](../facts/parameter-store.md#parameter-store-throughput-get-default)
  say: forty transactions per second
parameter-store-throughput-get-higher
  claim: With higher throughput enabled, GetParameter reaches 10,000 TPS, GetParameters 1,000 TPS and GetParametersByPath 100 TPS.
  scope: per account and Region, per API action; maximum; not adjustable; higher throughput must be enabled and incurs a charge; SecureString throughput can be further limited by AWS KMS quotas.
  link: [10,000 TPS](../facts/parameter-store.md#parameter-store-throughput-get-higher)
  link: [1,000 TPS](../facts/parameter-store.md#parameter-store-throughput-get-higher)
  link: [100 TPS](../facts/parameter-store.md#parameter-store-throughput-get-higher)
  say: ten thousand transactions per second | one thousand transactions per second | one hundred transactions per second
parameter-store-throughput-write-apis
  claim: PutParameter, DescribeParameters, GetParameterHistory and the label APIs get 3 TPS by default and 10 TPS with higher throughput.
  scope: per account and Region, for DescribeParameters, GetParameterHistory, LabelParameterVersion, UnlabelParameterVersion and PutParameter; default; adjustable; the higher value needs higher throughput enabled.
  link: [3 TPS](../facts/parameter-store.md#parameter-store-throughput-write-apis)
  link: [10 TPS](../facts/parameter-store.md#parameter-store-throughput-write-apis)
  say: three transactions per second | ten transactions per second
parameter-store-tier-max-parameters
  claim: An AWS account can have up to 10,000 standard parameters and up to 100,000 advanced parameters in each AWS Region.
  scope: per AWS account and AWS Region, per tier; maximum; not adjustable; advanced parameters incur a charge.
  link: [10,000](../facts/parameter-store.md#parameter-store-tier-max-parameters)
  link: [100,000](../facts/parameter-store.md#parameter-store-tier-max-parameters)
  say: ten thousand | one hundred thousand
parameter-store-tier-max-value-size
  claim: A standard parameter value can be at most 4 KB and an advanced parameter value at most 8 KB.
  scope: per parameter value, per tier; maximum; not adjustable.
  link: [4 KB](../facts/parameter-store.md#parameter-store-tier-max-value-size)
  link: [8 KB](../facts/parameter-store.md#parameter-store-tier-max-value-size)
  say: four kilobytes | eight kilobytes
parameter-store-tier-per-parameter
  claim: You configure each parameter individually to use the standard or the advanced tier, and you can mix both tiers in one account and Region.
  scope: per parameter.
  link: [Configure each parameter individually](../facts/parameter-store.md#parameter-store-tier-per-parameter)
  link: [You can mix standard and advanced parameters](../facts/parameter-store.md#parameter-store-tier-per-parameter)
parameter-store-update-takes-effect-next-read
  claim: A parameter update takes effect on the next read, with no validation, gradual rollout or automatic revert; for configuration where a bad value could cause an outage, AWS AppConfig adds a managed deployment workflow.
  scope: per parameter.
  link: [takes effect on the next read](../facts/parameter-store.md#parameter-store-update-takes-effect-next-read)
  link: [no validation, gradual rollout, or automatic revert](../facts/parameter-store.md#parameter-store-update-takes-effect-next-read)
parameter-store-versions-retained
  claim: Parameter Store keeps up to 100 versions of a parameter; after 100, each new version removes the oldest version from history.
  scope: per parameter; maximum; not adjustable; the oldest version is removed to make room.
  link: [100 versions](../facts/parameter-store.md#parameter-store-versions-retained)
  say: one hundred versions
parameter-store-vs-secrets-manager-cost-row
  claim: In AWS's comparison table, Parameter Store's standard tier is free while the advanced tier and higher throughput are billed; Secrets Manager is billed per secret per month and per API call.
  scope: per service.
  link: [Standard tier free](../facts/parameter-store.md#parameter-store-vs-secrets-manager-cost-row)
  link: [advanced tier and higher throughput billed](../facts/parameter-store.md#parameter-store-vs-secrets-manager-cost-row)
  link: [Billed per secret per month](../facts/parameter-store.md#parameter-store-vs-secrets-manager-cost-row)
parameter-store-vs-secrets-manager-deployment-row
  claim: In AWS's comparison table, Parameter Store offers versioning without pre-deployment validation or automatic rollback, and Secrets Manager offers versioning with staging labels.
  scope: per service.
  link: [Versioning without pre-deployment validation or automatic rollback](../facts/parameter-store.md#parameter-store-vs-secrets-manager-deployment-row)
  link: [Versioning with staging labels](../facts/parameter-store.md#parameter-store-vs-secrets-manager-deployment-row)
parameter-store-vs-secrets-manager-encryption-row
  claim: In the AWS comparison table, encryption in Parameter Store is optional with SecureString and AWS KMS, while for Secrets Manager the table lists AWS KMS encryption at rest with an AWS managed or customer managed key.
  scope: per service.
  link: [Optional with `SecureString` and AWS KMS](../facts/parameter-store.md#parameter-store-vs-secrets-manager-encryption-row)
  link: [AWS KMS encryption at rest](../facts/parameter-store.md#parameter-store-vs-secrets-manager-encryption-row)
parameter-store-vs-secrets-manager-rotation-row
  claim: In AWS's comparison table, credential rotation is None for Parameter Store and Automatic, with native database integrations, for Secrets Manager.
  scope: per service.
  link: [None](../facts/parameter-store.md#parameter-store-vs-secrets-manager-rotation-row)
  link: [Automatic, with native database integrations](../facts/parameter-store.md#parameter-store-vs-secrets-manager-rotation-row)
parameter-store-what-it-is
  claim: Parameter Store is a centralized configuration data store for named values called parameters; a parameter is any piece of data stored in Parameter Store, such as a block of text, a list of names, an AMI ID or a license key.
  scope: per account and Region.
  link: [a centralized configuration data store](../facts/parameter-store.md#parameter-store-what-it-is)
  link: [named values called parameters](../facts/parameter-store.md#parameter-store-what-it-is)
parameter-store-with-decryption
  claim: A SecureString value is returned encrypted unless you set WithDecryption to true on GetParameter; Parameter Store then calls the AWS KMS Decrypt operation on your behalf, and GetParameter returns a plaintext parameter value.
  scope: per GetParameter request.
  link: [set the `WithDecryption` parameter of `GetParameter` to `true`](../facts/parameter-store.md#parameter-store-with-decryption)
  link: [its value is encrypted](../facts/parameter-store.md#parameter-store-with-decryption)
secrets-manager-alarm-on-deleted-secret-access
  claim: If you do not know whether an application still uses a secret, you can create an Amazon CloudWatch alarm that alerts you to any attempt to access the secret during its recovery window.
  scope: per secret; during the recovery window.
  link: [create an Amazon CloudWatch alarm](../facts/secrets-manager.md#secrets-manager-alarm-on-deleted-secret-access)
  link: [access a secret during the recovery window](../facts/secrets-manager.md#secrets-manager-alarm-on-deleted-secret-access)
secrets-manager-alternating-users-both-valid
  claim: After an alternating-users rotation, both the user and user_clone credentials are valid, so applications are even less likely to get a deny than with single-user rotation.
  scope: per database secret; alternating-users rotation by Lambda function.
  link: [credentials are valid](../facts/secrets-manager.md#secrets-manager-alternating-users-both-valid)
  link: [even less chance of applications getting a deny](../facts/secrets-manager.md#secrets-manager-alternating-users-both-valid)
secrets-manager-alternating-users-high-availability
  claim: Alternating-users rotation suits applications that need high availability: an application that reads the secret during rotation still gets a valid set of credentials.
  scope: per database secret; alternating-users rotation by Lambda function.
  link: [applications that require high availability](../facts/secrets-manager.md#secrets-manager-alternating-users-high-availability)
  link: [still gets a valid set of credentials](../facts/secrets-manager.md#secrets-manager-alternating-users-high-availability)
secrets-manager-alternating-users-needs-superuser
  claim: Alternating-users rotation updates two users in one secret, and you must provide the credentials of a superuser in another secret, because most users cannot clone themselves.
  scope: per database secret; alternating-users rotation by Lambda function.
  link: [credentials for a `superuser` in another secret](../facts/secrets-manager.md#secrets-manager-alternating-users-needs-superuser)
  link: [two users in one secret](../facts/secrets-manager.md#secrets-manager-alternating-users-needs-superuser)
secrets-manager-arn-random-suffix
  claim: Secrets Manager adds six random characters to the end of the secret name in the ARN, so that the ARN is unique.
  scope: per secret ARN; fixed.
  link: [six random characters](../facts/secrets-manager.md#secrets-manager-arn-random-suffix)
  link: [ensure that the secret ARN is unique](../facts/secrets-manager.md#secrets-manager-arn-random-suffix)
  say: six random characters
secrets-manager-aws-managed-key-free
  claim: You can encrypt secrets with the AWS managed key aws/secretsmanager for free; your own KMS keys are charged at the AWS KMS rate.
  scope: per KMS key; free only for the AWS managed key.
  link: [to encrypt your secrets for free](../facts/secrets-manager.md#secrets-manager-aws-managed-key-free)
  link: [aws/secretsmanager](../facts/secrets-manager.md#secrets-manager-aws-managed-key-free)
  link: [charges you at the current AWS KMS rate](../facts/secrets-manager.md#secrets-manager-aws-managed-key-free)
secrets-manager-aws-managed-key-policy-fixed
  claim: The key policy of the AWS managed key aws/secretsmanager does not let any user use the key directly, and you cannot change that key policy, only view it.
  scope: per AWS managed key aws/secretsmanager.
  link: [You cannot change the key policy](../facts/secrets-manager.md#secrets-manager-aws-managed-key-policy-fixed)
  link: [does not allow any user to use](../facts/secrets-manager.md#secrets-manager-aws-managed-key-policy-fixed)
secrets-manager-aws-managed-key-vs-customer-key
  claim: For most cases AWS recommends the AWS managed key aws/secretsmanager at no cost; use a customer managed key if you need to access the secret from another AWS account, or want to rotate the key or apply a key policy yourself.
  scope: per secret.
  link: [access the secret from another AWS account](../facts/secrets-manager.md#secrets-manager-aws-managed-key-vs-customer-key)
  link: [use a customer managed key](../facts/secrets-manager.md#secrets-manager-aws-managed-key-vs-customer-key)
secrets-manager-awscurrent-returned-by-default
  claim: A secret always has a version labeled AWSCURRENT, and Secrets Manager returns that version by default when you read the secret value.
  scope: per secret; default.
  link: [returns that version by default](../facts/secrets-manager.md#secrets-manager-awscurrent-returned-by-default)
  link: [AWSCURRENT](../facts/secrets-manager.md#secrets-manager-awscurrent-returned-by-default)
secrets-manager-batchgetsecretvalue-max-secrets
  claim: One BatchGetSecretValue call retrieves the secret values of up to 20 secrets.
  scope: per BatchGetSecretValue call; maximum; not adjustable.
  link: [up to 20 secrets](../facts/secrets-manager.md#secrets-manager-batchgetsecretvalue-max-secrets)
  say: up to twenty secrets
secrets-manager-block-public-policy
  claim: Resource policy validation and the BlockPublicPolicy parameter help prevent public access from being granted through resource policies attached directly to secrets; AWS says to also inspect identity-based policies attached to associated principals such as IAM roles, and resource-based policies attached to associated resources such as AWS KMS keys.
  scope: per secret resource policy; inspect identity-based policies and resource-based policies of associated resources, such as KMS keys, separately.
  link: [preventing public access from being granted](../facts/secrets-manager.md#secrets-manager-block-public-policy)
  link: [directly attached to your secrets](../facts/secrets-manager.md#secrets-manager-block-public-policy)
secrets-manager-block-public-policy-recommended
  claim: AWS recommends BlockPublicPolicy: true in identity policies that allow PutResourcePolicy, so users can attach a resource policy only if it does not allow broad access; Secrets Manager uses Zelkova automated reasoning to check for broad access.
  scope: per identity policy.
  link: [if the policy doesn't allow broad access](../facts/secrets-manager.md#secrets-manager-block-public-policy-recommended)
  link: [uses Zelkova automated reasoning](../facts/secrets-manager.md#secrets-manager-block-public-policy-recommended)
secrets-manager-cache-cost-latency
  claim: Reading a cached secret is faster than reading it from Secrets Manager, and because Secrets Manager API calls cost money, a client-side cache can reduce costs.
  scope: per application.
  link: [using a cache can reduce your costs](../facts/secrets-manager.md#secrets-manager-cache-cost-latency)
  link: [Retrieving a cached secret is faster](../facts/secrets-manager.md#secrets-manager-cache-cost-latency)
secrets-manager-cache-refresh-hourly-default
  claim: The Secrets Manager Python caching component refreshes cached secrets every hour by default, and the refresh interval is configurable.
  scope: per caching client; default; adjustable; Python caching component.
  link: [every hour](../facts/secrets-manager.md#secrets-manager-cache-refresh-hourly-default)
  link: [By default, the cache refreshes secrets every hour](../facts/secrets-manager.md#secrets-manager-cache-refresh-hourly-default)
  say: every hour
secrets-manager-cannot-delete-replicated-primary
  claim: You cannot delete a primary secret while it is replicated to other Regions: delete the replicas first; a replica is deleted immediately.
  scope: per primary secret; the secret is replicated.
  link: [can't delete a primary secret](../facts/secrets-manager.md#secrets-manager-cannot-delete-replicated-primary)
  link: [it is deleted immediately](../facts/secrets-manager.md#secrets-manager-cannot-delete-replicated-primary)
secrets-manager-cannot-delete-version-directly
  claim: You cannot delete a version of a secret directly; you remove all its staging labels, which marks it deprecated so that Secrets Manager can delete it in the background.
  scope: per secret version.
  link: [can't directly delete a version of a secret](../facts/secrets-manager.md#secrets-manager-cannot-delete-version-directly)
  link: [remove all staging labels from the version](../facts/secrets-manager.md#secrets-manager-cannot-delete-version-directly)
secrets-manager-case-sony-retrieve-rotate
  claim: Sony Interactive Entertainment (SIE) uses AWS Secrets Manager to retrieve and rotate credentials and other assets as part of its unified platform on Amazon EKS.
  scope: one customer.
  link: [to retrieve and rotate credentials and other assets](../facts/secrets-manager.md#secrets-manager-case-sony-retrieve-rotate)
  link: [SIE also uses AWS Secrets Manager](../facts/secrets-manager.md#secrets-manager-case-sony-retrieve-rotate)
secrets-manager-change-cost-allocation-tags-2025
  claim: On 2025-05-27 Secrets Manager added support for cost allocation tags, so costs can be tracked by department, team or application.
  scope: per secret.
  link: [2025-05-27](../facts/secrets-manager.md#secrets-manager-change-cost-allocation-tags-2025)
  say: May twenty-seventh, twenty twenty-five
secrets-manager-change-describesecret-rate-2025
  claim: On 2025-03-04 the DescribeSecret request rate rose to 40,000 requests per second; an earlier increase had set it to 10,000 requests per second.
  scope: per account, per Region.
  link: [40,000 requests per second](../facts/secrets-manager.md#secrets-manager-change-describesecret-rate-2025)
  link: [10,000 requests per second](../facts/secrets-manager.md#secrets-manager-change-describesecret-rate-2025)
  say: forty thousand requests per second | ten thousand requests per second
  changed: 2025-03-04: was 10,000 requests per second
secrets-manager-change-kms-key-reencrypts-labeled
  claim: You can change the KMS key of an existing secret; Secrets Manager then re-encrypts the AWSCURRENT, AWSPENDING and AWSPREVIOUS versions with the new key and keeps the existing versions encrypted with the previous key too.
  scope: per secret; you need kms:Decrypt on the previous key for re-encryption.
  link: [change the encryption key for your secret](../facts/secrets-manager.md#secrets-manager-change-kms-key-reencrypts-labeled)
  link: [existing versions encrypted with the previous key](../facts/secrets-manager.md#secrets-manager-change-kms-key-reencrypts-labeled)
secrets-manager-change-managed-external-secrets-2025
  claim: On 2025-11-19 AWS announced managed external secrets in Secrets Manager.
  scope: Secrets Manager.
  link: [2025-11-19](../facts/secrets-manager.md#secrets-manager-change-managed-external-secrets-2025)
  say: November nineteenth, twenty twenty-five
secrets-manager-change-sla-2023
  claim: AWS raised the Secrets Manager SLA commitment to a Monthly Uptime Percentage of at least 99.99% for each AWS Region during any monthly billing cycle; the earlier SLA committed to at least 99.9%.
  scope: per AWS Region, per monthly billing cycle.
  link: [99.99%](../facts/secrets-manager.md#secrets-manager-change-sla-2023)
  link: [99.9%](../facts/secrets-manager.md#secrets-manager-change-sla-2023)
  say: ninety-nine point nine nine percent | ninety-nine point nine percent
  changed: 2023-12-05: was 99.9%
secrets-manager-change-update-notifications-2026
  claim: On 2026-07-22 AWS announced that Secrets Manager publishes secret update notifications to Amazon EventBridge.
  scope: Secrets Manager events; not examinable yet (generally available after 2026-07-15).
  link: [2026-07-22](../facts/secrets-manager.md#secrets-manager-change-update-notifications-2026)
  say: July twenty-second, twenty twenty-six
secrets-manager-cli-history-risk
  claim: Most command shells log commands and show the last command entered, so typing a secret into the AWS CLI can expose it.
  scope: per command shell.
  link: [could compromise your secrets](../facts/secrets-manager.md#secrets-manager-cli-history-risk)
  link: [see the last entered command](../facts/secrets-manager.md#secrets-manager-cli-history-risk)
secrets-manager-clone-permissions-not-synced
  claim: Secrets Manager creates the cloned user with the same permissions as the original user; if you later change the original user's permissions, you must also change the clone's permissions.
  scope: per database secret; alternating-users rotation.
  link: [same permissions as the original user](../facts/secrets-manager.md#secrets-manager-clone-permissions-not-synced)
  link: [must also change the cloned user's permissions](../facts/secrets-manager.md#secrets-manager-clone-permissions-not-synced)
secrets-manager-cloudformation-dynamic-references
  claim: CloudFormation dynamic references let a template specify external values stored and managed in other services, such as secure string parameters in Parameter Store or secrets in Secrets Manager, and so decouple sensitive information from the template; CloudFormation retrieves the value during stack and change set operations.
  scope: per stack template.
  link: [decouple sensitive information from your infrastructure-as-code templates](../facts/secrets-manager.md#secrets-manager-cloudformation-dynamic-references)
  link: [retrieves the value of the specified reference](../facts/secrets-manager.md#secrets-manager-cloudformation-dynamic-references)
secrets-manager-cloudformation-no-secure-in-custom
  claim: Dynamic references cannot be used for secure values from Parameter Store or Secrets Manager in custom resources, and are not supported in AWS::CloudFormation::Init metadata or EC2 UserData properties.
  scope: per stack template.
  link: [can't be used for secure values](../facts/secrets-manager.md#secrets-manager-cloudformation-no-secure-in-custom)
  link: [not supported in `AWS::CloudFormation::Init` metadata](../facts/secrets-manager.md#secrets-manager-cloudformation-no-secure-in-custom)
secrets-manager-cloudtrail-management-events
  claim: Secrets Manager logs all of its events in AWS CloudTrail as management events.
  scope: per account and Region.
  link: [logs all events as management events](../facts/secrets-manager.md#secrets-manager-cloudtrail-management-events)
  link: [management events](../facts/secrets-manager.md#secrets-manager-cloudtrail-management-events)
secrets-manager-codeguru-finds-hardcoded
  claim: CodeGuru Reviewer integrates with Secrets Manager and uses a secrets detector to find unprotected secrets, such as hard-coded passwords, in code.
  scope: per code repository.
  link: [finds unprotected secrets in your code](../facts/secrets-manager.md#secrets-manager-codeguru-finds-hardcoded)
  link: [searches for hardcoded passwords](../facts/secrets-manager.md#secrets-manager-codeguru-finds-hardcoded)
secrets-manager-config-checks-rotation
  claim: You can use AWS Config rules to check whether secrets rotate in line with your standards and to find secrets that do not conform; the data can be aggregated across accounts and Regions.
  scope: per account and Region, or aggregated.
  link: [use AWS Config to evaluate your secrets](../facts/secrets-manager.md#secrets-manager-config-checks-rotation)
  link: [identify secrets that don't conform to your rules](../facts/secrets-manager.md#secrets-manager-config-checks-rotation)
secrets-manager-cross-account-needs-both-policies
  claim: To let users in one account read secrets in another account, you must allow access both in a resource policy on the secret and in an identity policy.
  scope: per secret, cross-account.
  link: [a resource policy and in an identity policy](../facts/secrets-manager.md#secrets-manager-cross-account-needs-both-policies)
  link: [cross-account access](../facts/secrets-manager.md#secrets-manager-cross-account-needs-both-policies)
secrets-manager-cross-account-no-aws-managed-key
  claim: You cannot use the AWS managed key aws/secretsmanager for cross-account access; the secret must be encrypted with a KMS key you create, whose key policy allows the other account.
  scope: per secret, cross-account.
  link: [can't use the AWS managed key](../facts/secrets-manager.md#secrets-manager-cross-account-no-aws-managed-key)
  link: [a KMS key that you create](../facts/secrets-manager.md#secrets-manager-cross-account-no-aws-managed-key)
secrets-manager-cross-account-throttling
  claim: For a cross-account request, Secrets Manager throttles the account of the identity that makes the request, not the account that owns the secret.
  scope: cross-account requests.
  link: [throttles the account of the identity](../facts/secrets-manager.md#secrets-manager-cross-account-throttling)
  link: [not the account that owns the secret](../facts/secrets-manager.md#secrets-manager-cross-account-throttling)
secrets-manager-db-rotation-needs-json-structure
  claim: To turn on automatic rotation for a database secret, the secret must contain the database connection information in the correct JSON structure.
  scope: per database secret; only when automatic rotation is turned on.
  link: [in the correct JSON structure](../facts/secrets-manager.md#secrets-manager-db-rotation-needs-json-structure)
  link: [must contain connection information for the database](../facts/secrets-manager.md#secrets-manager-db-rotation-needs-json-structure)
secrets-manager-deletion-not-immediate
  claim: Secrets Manager does not delete a secret immediately: it makes the secret inaccessible at once and schedules deletion after a recovery window; the AWS CLI can also delete a secret immediately without a recovery window, and then you can't recover it.
  scope: per secret; unless you delete the secret immediately without a recovery window.
  link: [does not immediately delete secrets](../facts/secrets-manager.md#secrets-manager-deletion-not-immediate)
  link: [immediately makes the secrets inaccessible](../facts/secrets-manager.md#secrets-manager-deletion-not-immediate)
secrets-manager-deny-aws-managed-key
  claim: You can deny permission to the AWS managed key aws/secretsmanager in a policy and so require that secrets are encrypted with a customer managed key.
  scope: per IAM policy.
  link: [encrypted with a customer managed key](../facts/secrets-manager.md#secrets-manager-deny-aws-managed-key)
  link: [deny permission to the AWS managed key](../facts/secrets-manager.md#secrets-manager-deny-aws-managed-key)
secrets-manager-ecs-compare-parameter-store
  claim: The Amazon ECS guide says Secrets Manager and Parameter Store are both managed key-value stores that use AWS KMS to encrypt sensitive data, and that Secrets Manager also includes the ability to automatically rotate secrets, generate random secrets and share secrets across accounts; to use these features use Secrets Manager, otherwise use encrypted parameters in Parameter Store.
  scope: per secret.
  link: [automatically rotate secrets, generate random secrets](../facts/secrets-manager.md#secrets-manager-ecs-compare-parameter-store)
  link: [share secrets across accounts](../facts/secrets-manager.md#secrets-manager-ecs-compare-parameter-store)
  link: [use encrypted parameters in Systems Manager Parameter Store](../facts/secrets-manager.md#secrets-manager-ecs-compare-parameter-store)
secrets-manager-ecs-env-var-leak-risk
  claim: The ECS guide warns of an elevated risk of data leakage with environment variables and suggests a sidecar container that reads secrets from Secrets Manager and writes them to a shared volume.
  scope: per ECS task.
  link: [elevated risk of data leakage with environment variables](../facts/secrets-manager.md#secrets-manager-ecs-env-var-leak-risk)
  link: [run a sidecar container](../facts/secrets-manager.md#secrets-manager-ecs-env-var-leak-risk)
secrets-manager-ecs-inject-secrets
  claim: Amazon ECS can inject secrets from Secrets Manager and Systems Manager Parameter Store into containers, for example as environment variables through the secrets container definition parameter.
  scope: per ECS task definition.
  link: [injected into containers from AWS Secrets Manager](../facts/secrets-manager.md#secrets-manager-ecs-inject-secrets)
  link: [the `secrets` container definition parameter](../facts/secrets-manager.md#secrets-manager-ecs-inject-secrets)
secrets-manager-ecs-redeploy-for-new-value
  claim: When a secret injected into an ECS container changes, you must force a new deployment or launch a new task to get the latest value.
  scope: per ECS task or service; secret injected through the task definition.
  link: [you must force a new deployment](../facts/secrets-manager.md#secrets-manager-ecs-redeploy-for-new-value)
  link: [launch a new task](../facts/secrets-manager.md#secrets-manager-ecs-redeploy-for-new-value)
  link: [retrieve the latest secret value](../facts/secrets-manager.md#secrets-manager-ecs-redeploy-for-new-value)
secrets-manager-encrypts-at-rest-tls-in-transit
  claim: Secrets Manager encrypts secrets at rest with keys in AWS KMS, and when you retrieve a secret it decrypts it and sends it to you over TLS.
  scope: per secret.
  link: [encrypts secrets at rest](../facts/secrets-manager.md#secrets-manager-encrypts-at-rest-tls-in-transit)
  link: [transmits it securely over TLS](../facts/secrets-manager.md#secrets-manager-encrypts-at-rest-tls-in-transit)
secrets-manager-endpoint-policy-default-full
  claim: The default endpoint policy of a Secrets Manager interface endpoint allows full access to Secrets Manager; to limit access from the VPC, attach a custom endpoint policy.
  scope: per interface endpoint; default; adjustable; replace it with a custom endpoint policy.
  link: [allows full access to Secrets Manager](../facts/secrets-manager.md#secrets-manager-endpoint-policy-default-full)
  link: [attach a custom endpoint policy](../facts/secrets-manager.md#secrets-manager-endpoint-policy-default-full)
secrets-manager-endpoint-private-dns
  claim: If you enable private DNS for the Secrets Manager endpoint, applications can call Secrets Manager with its default Regional DNS name.
  scope: per interface endpoint; private DNS enabled.
  link: [If you enable private DNS for the endpoint](../facts/secrets-manager.md#secrets-manager-endpoint-private-dns)
  link: [its default DNS name for the Region](../facts/secrets-manager.md#secrets-manager-endpoint-private-dns)
secrets-manager-endpoint-same-vpc-as-rotation
  claim: AWS recommends a Secrets Manager endpoint in the same VPC as the database, so that requests from the Lambda rotation function to Secrets Manager do not leave the Amazon network.
  scope: per VPC; rotation by Lambda function.
  link: [a Secrets Manager endpoint in the same VPC](../facts/secrets-manager.md#secrets-manager-endpoint-same-vpc-as-rotation)
  link: [don't leave the Amazon network](../facts/secrets-manager.md#secrets-manager-endpoint-same-vpc-as-rotation)
secrets-manager-envelope-encryption-data-key
  claim: Secrets Manager does not encrypt the secret value directly with the KMS key: it uses the KMS key to generate and encrypt a data key, encrypts the value with that data key, and requests a new data key whenever the value changes.
  scope: per secret value.
  link: [does not use the KMS key](../facts/secrets-manager.md#secrets-manager-envelope-encryption-data-key)
  link: [requests a new data key from AWS KMS](../facts/secrets-manager.md#secrets-manager-envelope-encryption-data-key)
secrets-manager-eventbridge-from-cloudtrail
  claim: In Amazon EventBridge you can match Secrets Manager events from CloudTrail log entries and send new events to a target to take action.
  scope: per account and Region.
  link: [match Secrets Manager events from CloudTrail log entries](../facts/secrets-manager.md#secrets-manager-eventbridge-from-cloudtrail)
  link: [send new generated events to a target](../facts/secrets-manager.md#secrets-manager-eventbridge-from-cloudtrail)
secrets-manager-faq-audit-monitor-integrations
  claim: You can audit and monitor secrets because Secrets Manager integrates with AWS CloudTrail, Amazon CloudWatch and Amazon SNS.
  scope: per account.
  link: [audit and monitor secrets](../facts/secrets-manager.md#secrets-manager-faq-audit-monitor-integrations)
  link: [AWS CloudTrail, Amazon CloudWatch](../facts/secrets-manager.md#secrets-manager-faq-audit-monitor-integrations)
secrets-manager-faq-custom-rotation-lambda
  claim: You can extend Secrets Manager to rotate other secrets, such as credentials for Oracle databases on EC2, by modifying sample AWS Lambda functions.
  scope: per secret; for secrets without native rotation.
  link: [by modifying sample AWS Lambda functions](../facts/secrets-manager.md#secrets-manager-faq-custom-rotation-lambda)
  link: [Oracle databases hosted on EC2](../facts/secrets-manager.md#secrets-manager-faq-custom-rotation-lambda)
secrets-manager-faq-default-kms-key-created
  claim: If you do not provide a KMS key, Secrets Manager creates AWS KMS default keys for your account automatically.
  scope: per account; default; not adjustable; when no KMS key is provided.
  link: [creates AWS KMS default keys](../facts/secrets-manager.md#secrets-manager-faq-default-kms-key-created)
  link: [If you do not provide a KMS key](../facts/secrets-manager.md#secrets-manager-faq-default-kms-key-created)
secrets-manager-faq-envelope-encryption-aes-256
  claim: Secrets Manager uses envelope encryption with the AES-256 algorithm to encrypt your secrets in AWS KMS.
  scope: per secret.
  link: [envelope encryption](../facts/secrets-manager.md#secrets-manager-faq-envelope-encryption-aes-256)
  link: [AES-256](../facts/secrets-manager.md#secrets-manager-faq-envelope-encryption-aes-256)
secrets-manager-faq-free-tier-credits
  claim: Starting July 15, 2025, new AWS customers receive up to $200 in AWS Free Tier credits that can be applied to eligible services, including Secrets Manager.
  scope: per new AWS account; maximum; new AWS customers from July 15, 2025.
  link: [up to $200 in AWS Free Tier credits](../facts/secrets-manager.md#secrets-manager-faq-free-tier-credits)
  link: [July 15, 2025](../facts/secrets-manager.md#secrets-manager-faq-free-tier-credits)
  say: up to two hundred dollars in Free Tier credits | July fifteenth, twenty twenty-five
secrets-manager-faq-iam-policies-control-access
  claim: You use IAM policies to control which users and applications can access secrets in Secrets Manager.
  scope: per secret.
  link: [control which users and applications can access](../facts/secrets-manager.md#secrets-manager-faq-iam-policies-control-access)
  link: [AWS Identity and Access Management (IAM) policies](../facts/secrets-manager.md#secrets-manager-faq-iam-policies-control-access)
secrets-manager-faq-iam-policy-before-retrieval
  claim: Before an application can use a secret, you must write an IAM policy that permits the application to access the specific secrets.
  scope: per application that retrieves secrets; the application retrieves secrets through the Secrets Manager APIs.
  link: [must write an AWS Identity and Access Management](../facts/secrets-manager.md#secrets-manager-faq-iam-policy-before-retrieval)
  link: [access specific secrets](../facts/secrets-manager.md#secrets-manager-faq-iam-policy-before-retrieval)
secrets-manager-faq-kinds-of-secrets
  claim: Secrets Manager can manage database credentials, on-premises resource credentials, SaaS application credentials, third-party API keys and SSH keys.
  scope: per secret.
  link: [third-party API keys](../facts/secrets-manager.md#secrets-manager-faq-kinds-of-secrets)
  link: [Secure Shell (SSH) keys](../facts/secrets-manager.md#secrets-manager-faq-kinds-of-secrets)
secrets-manager-faq-last-rotated-console-api
  claim: You can see when Secrets Manager last rotated a secret in the Secrets Manager console or through its APIs.
  scope: per secret.
  link: [last rotated a secret](../facts/secrets-manager.md#secrets-manager-faq-last-rotated-console-api)
  link: [the Secrets Manager console or APIs](../facts/secrets-manager.md#secrets-manager-faq-last-rotated-console-api)
secrets-manager-faq-managed-rotation-whole-process
  claim: With managed rotation turned on, Secrets Manager handles the entire rotation process: it generates new credentials, updates the secret value and coordinates with the associated service or database.
  scope: per secret with managed rotation; managed rotation is enabled.
  link: [automatically handles the entire rotation process](../facts/secrets-manager.md#secrets-manager-faq-managed-rotation-whole-process)
  link: [generating new credentials, updating the secret value](../facts/secrets-manager.md#secrets-manager-faq-managed-rotation-whole-process)
secrets-manager-faq-native-rotation-services
  claim: Secrets Manager can natively rotate credentials for Amazon RDS, Amazon DocumentDB and Amazon Redshift, and third-party secrets for integrated partners.
  scope: per secret.
  link: [natively rotate credentials](../facts/secrets-manager.md#secrets-manager-faq-native-rotation-services)
  link: [Amazon DocumentDB, and Amazon Redshift](../facts/secrets-manager.md#secrets-manager-faq-native-rotation-services)
secrets-manager-faq-no-minimum-fee
  claim: With Secrets Manager you pay only for what you use, and there is no minimum fee.
  scope: per account.
  link: [there is no minimum fee](../facts/secrets-manager.md#secrets-manager-faq-no-minimum-fee)
  link: [you pay only for what you use](../facts/secrets-manager.md#secrets-manager-faq-no-minimum-fee)
secrets-manager-faq-no-own-infrastructure
  claim: Secrets Manager protects access to applications, services and IT resources without the upfront investment and ongoing maintenance costs of operating your own infrastructure.
  scope: service-wide.
  link: [operating your own infrastructure](../facts/secrets-manager.md#secrets-manager-faq-no-own-infrastructure)
  link: [without the upfront investment](../facts/secrets-manager.md#secrets-manager-faq-no-own-infrastructure)
secrets-manager-faq-no-persistent-cache
  claim: By default, Secrets Manager does not write or cache the secret to persistent storage.
  scope: per secret; default; not adjustable.
  link: [does not write or cache the secret](../facts/secrets-manager.md#secrets-manager-faq-no-persistent-cache)
  link: [persistent storage](../facts/secrets-manager.md#secrets-manager-faq-no-persistent-cache)
secrets-manager-faq-no-setup-fees
  claim: Secrets Manager has no set-up fees or commitments to begin using the service.
  scope: per account.
  link: [no set-up fees or commitments](../facts/secrets-manager.md#secrets-manager-faq-no-setup-fees)
  link: [to begin using the service](../facts/secrets-manager.md#secrets-manager-faq-no-setup-fees)
secrets-manager-faq-replace-hardcoded-secrets
  claim: Developers can replace hardcoded secrets in their applications by retrieving the secrets programmatically from Secrets Manager.
  scope: per application.
  link: [replace hardcoded secrets in their applications](../facts/secrets-manager.md#secrets-manager-faq-replace-hardcoded-secrets)
  link: [retrieve secrets programmatically from Secrets Manager](../facts/secrets-manager.md#secrets-manager-faq-replace-hardcoded-secrets)
secrets-manager-faq-rotate-schedule-or-on-demand
  claim: You can rotate passwords on a schedule or on demand for supported database types hosted on AWS, without a risk of impacting applications.
  scope: per secret; for supported database types hosted on AWS.
  link: [on a schedule or on demand](../facts/secrets-manager.md#secrets-manager-faq-rotate-schedule-or-on-demand)
  link: [without a risk of impacting applications](../facts/secrets-manager.md#secrets-manager-faq-rotate-schedule-or-on-demand)
secrets-manager-faq-rotation-clone-user
  claim: As an example of safe rotation, the Secrets Manager FAQ says that for database secrets, when Secrets Manager initiates a rotation, it uses the database admin credentials you provide to create a clone user with the same privileges but a different password.
  scope: per database secret; given in the FAQ as an example for database secrets.
  link: [create a clone user with the same privileges](../facts/secrets-manager.md#secrets-manager-faq-rotation-clone-user)
  link: [database admin credentials provided by you](../facts/secrets-manager.md#secrets-manager-faq-rotation-clone-user)
secrets-manager-faq-rotation-notification-events
  claim: You can configure Amazon CloudWatch Events to receive a notification when Secrets Manager rotates a secret.
  scope: per secret.
  link: [Amazon CloudWatch Events](../facts/secrets-manager.md#secrets-manager-faq-rotation-notification-events)
  link: [receive a notification](../facts/secrets-manager.md#secrets-manager-faq-rotation-notification-events)
secrets-manager-faq-rotation-open-connections
  claim: When Secrets Manager rotates a database credential, the open database connection is not re-authenticated, because authentication happens when a connection is established.
  scope: per database secret rotation.
  link: [the open database connection is not re-authenticated](../facts/secrets-manager.md#secrets-manager-faq-rotation-open-connections)
  link: [Authentication happens when a connection is established](../facts/secrets-manager.md#secrets-manager-faq-rotation-open-connections)
secrets-manager-faq-scope-aws-third-party-on-premises
  claim: Secrets Manager can secure and manage secrets used to access resources in the AWS Cloud, on third-party services, and on-premises.
  scope: per secret.
  link: [on third-party services, and on-premises](../facts/secrets-manager.md#secrets-manager-faq-scope-aws-third-party-on-premises)
  link: [resources in the AWS Cloud](../facts/secrets-manager.md#secrets-manager-faq-scope-aws-third-party-on-premises)
secrets-manager-faq-secret-size-64-kb
  claim: Secrets Manager lets you store a JSON document, so you can manage any text blurb that is 64 KB or smaller.
  scope: per secret value; maximum; not adjustable.
  link: [64 KB or smaller](../facts/secrets-manager.md#secrets-manager-faq-secret-size-64-kb)
  say: sixty-four kilobytes or smaller
secrets-manager-force-delete-without-recovery
  claim: A secret deleted with the ForceDeleteWithoutRecovery parameter has no recovery window: you have no opportunity to recover it and lose it permanently.
  scope: per DeleteSecret call; AWS CLI option --force-delete-without-recovery.
  link: [no opportunity to recover the secret](../facts/secrets-manager.md#secrets-manager-force-delete-without-recovery)
  link: [You lose the secret permanently](../facts/secrets-manager.md#secrets-manager-force-delete-without-recovery)
secrets-manager-interface-endpoint-privatelink
  claim: You can connect a VPC privately to Secrets Manager with an interface VPC endpoint; instances then need no public IP addresses and the traffic does not leave the AWS network.
  scope: per VPC.
  link: [creating an *interface VPC endpoint*](../facts/secrets-manager.md#secrets-manager-interface-endpoint-privatelink)
  link: [does not leave the AWS network](../facts/secrets-manager.md#secrets-manager-interface-endpoint-privatelink)
secrets-manager-ip-condition-breaks-rotation
  claim: A Lambda rotation function calls Secrets Manager from an AWS-internal address space, so a policy that filters on your corporate IP address range makes those requests fail.
  scope: per policy statement; aws:SourceIp or IP address condition operators.
  link: [from an AWS-internal address space](../facts/secrets-manager.md#secrets-manager-ip-condition-breaks-rotation)
  link: [with the IP address filter fail](../facts/secrets-manager.md#secrets-manager-ip-condition-breaks-rotation)
secrets-manager-json-key-value-recommended
  claim: To store several string values in one secret, AWS recommends a JSON text string with key-value pairs.
  scope: per secret.
  link: [JSON text string with key-value pairs](../facts/secrets-manager.md#secrets-manager-json-key-value-recommended)
  link: [multiple string values in one secret](../facts/secrets-manager.md#secrets-manager-json-key-value-recommended)
secrets-manager-kms-key-same-region
  claim: The KMS key that encrypts a secret must be in the same Region as the secret.
  scope: per secret.
  link: [in the same region as the secret](../facts/secrets-manager.md#secrets-manager-kms-key-same-region)
secrets-manager-label-updated-event
  claim: To detect that the active value of a secret changed, AWS recommends matching the native Secret Label Updated event for AWSCURRENT; it is enabled by default for all secrets and goes to the default EventBridge event bus.
  scope: per secret; default.
  link: [enabled by default for all secrets](../facts/secrets-manager.md#secrets-manager-label-updated-event)
  link: [Secret Label Updated](../facts/secrets-manager.md#secrets-manager-label-updated-event)
secrets-manager-labeled-versions-never-removed
  claim: Secrets Manager never removes labeled versions of a secret; versions without a label are considered deprecated.
  scope: per secret.
  link: [never removes labeled versions](../facts/secrets-manager.md#secrets-manager-labeled-versions-never-removed)
  link: [unlabeled versions are considered deprecated](../facts/secrets-manager.md#secrets-manager-labeled-versions-never-removed)
secrets-manager-lambda-extension-cache-size-default
  claim: The AWS Parameters and Secrets Lambda Extension cache holds up to 1000 items by default; the valid range is 0 to 1000, and 0 bypasses the cache.
  scope: per Lambda function using the extension; default; adjustable; set with PARAMETERS_SECRETS_EXTENSION_CACHE_SIZE.
  link: [1000](../facts/secrets-manager.md#secrets-manager-lambda-extension-cache-size-default)
  say: one thousand items
secrets-manager-lambda-extension-http-port-default
  claim: The AWS Parameters and Secrets Lambda Extension runs a local HTTP server on port 2773 by default.
  scope: per Lambda function using the extension; default; adjustable; set with PARAMETERS_SECRETS_EXTENSION_HTTP_PORT.
  link: [2773](../facts/secrets-manager.md#secrets-manager-lambda-extension-http-port-default)
  say: port two seven seven three
secrets-manager-lambda-extension-ttl-default
  claim: The AWS Parameters and Secrets Lambda Extension keeps a secret in its cache for 300 s (5 minutes) by default, and SECRETS_MANAGER_TTL accepts 0 to 300 s; 0 bypasses the cache.
  scope: per Lambda function using the extension; default; adjustable; set with the SECRETS_MANAGER_TTL environment variable; ignored when the cache size is 0.
  link: [300 s (5 minutes)](../facts/secrets-manager.md#secrets-manager-lambda-extension-ttl-default)
  say: three hundred seconds, which is five minutes
secrets-manager-managed-rotation-aurora-master-user
  claim: Amazon Aurora offers managed rotation for master user credentials stored in Secrets Manager.
  scope: per Aurora DB cluster secret.
  link: [managed rotation for master user credentials](../facts/secrets-manager.md#secrets-manager-managed-rotation-aurora-master-user)
  link: [Amazon Aurora](../facts/secrets-manager.md#secrets-manager-managed-rotation-aurora-master-user)
secrets-manager-managed-rotation-documentdb-master-user
  claim: Amazon DocumentDB offers managed rotation for master user credentials stored in Secrets Manager.
  scope: per DocumentDB cluster secret.
  link: [managed rotation for master user credentials](../facts/secrets-manager.md#secrets-manager-managed-rotation-documentdb-master-user)
  link: [Amazon DocumentDB](../facts/secrets-manager.md#secrets-manager-managed-rotation-documentdb-master-user)
secrets-manager-managed-rotation-ecs-service-connect
  claim: Amazon ECS Service Connect offers managed rotation for AWS Private Certificate Authority TLS certificates.
  scope: per ECS Service Connect TLS configuration.
  link: [AWS Private Certificate Authority TLS certificates](../facts/secrets-manager.md#secrets-manager-managed-rotation-ecs-service-connect)
  link: [Service Connect](../facts/secrets-manager.md#secrets-manager-managed-rotation-ecs-service-connect)
secrets-manager-managed-rotation-no-lambda
  claim: With managed rotation, the managing service configures and manages rotation, and you do not use a Lambda function to update the secret and the database credentials.
  scope: per managed secret; for services that offer managed rotation, such as Amazon RDS for master user credentials.
  link: [you don't use an AWS Lambda function](../facts/secrets-manager.md#secrets-manager-managed-rotation-no-lambda)
  link: [With managed rotation](../facts/secrets-manager.md#secrets-manager-managed-rotation-no-lambda)
secrets-manager-managed-rotation-rds-master-user
  claim: Amazon RDS offers managed rotation for master user credentials stored in Secrets Manager.
  scope: per RDS DB instance secret.
  link: [managed rotation for master user credentials](../facts/secrets-manager.md#secrets-manager-managed-rotation-rds-master-user)
  link: [Amazon RDS](../facts/secrets-manager.md#secrets-manager-managed-rotation-rds-master-user)
secrets-manager-managed-rotation-redshift-admin
  claim: Amazon Redshift offers managed rotation for admin passwords stored in Secrets Manager.
  scope: per Redshift admin secret.
  link: [managed rotation for admin passwords](../facts/secrets-manager.md#secrets-manager-managed-rotation-redshift-admin)
  link: [Amazon Redshift](../facts/secrets-manager.md#secrets-manager-managed-rotation-redshift-admin)
secrets-manager-managed-rotation-within-one-minute
  claim: Rotation of a managed secret typically completes within one minute, and during rotation new connections that read the secret may still get the previous credentials.
  scope: per managed secret rotation; typical duration, not a guarantee.
  link: [within one minute](../facts/secrets-manager.md#secrets-manager-managed-rotation-within-one-minute)
  link: [may get the previous version of the credentials](../facts/secrets-manager.md#secrets-manager-managed-rotation-within-one-minute)
  say: within one minute
secrets-manager-managed-secret-created-by-service-only
  claim: Only the AWS service that manages a managed secret can create it, and managed secrets use a naming convention that includes the managing service ID.
  scope: per managed secret.
  link: [only be created by the AWS service](../facts/secrets-manager.md#secrets-manager-managed-secret-created-by-service-only)
  link: [includes the managing service ID](../facts/secrets-manager.md#secrets-manager-managed-secret-created-by-service-only)
secrets-manager-managed-secret-restrictions
  claim: A managed secret is a secret that the service that created it helps manage; the managing service might restrict you from updating it or deleting it without a recovery period, because the managing service depends on the secret.
  scope: per managed secret; depends on the managing service.
  link: [might also restrict you from updating secrets](../facts/secrets-manager.md#secrets-manager-managed-secret-restrictions)
  link: [deleting them without a recovery period](../facts/secrets-manager.md#secrets-manager-managed-secret-restrictions)
secrets-manager-manual-update-counts-as-rotation
  claim: If you update a secret value by hand while automatic rotation is set up, Secrets Manager counts it as a valid rotation when it calculates the next rotation date.
  scope: per secret; automatic rotation is set up.
  link: [considers that a valid rotation](../facts/secrets-manager.md#secrets-manager-manual-update-counts-as-rotation)
  link: [calculates the next rotation date](../facts/secrets-manager.md#secrets-manager-manual-update-counts-as-rotation)
secrets-manager-metadata-not-encrypted
  claim: Secrets Manager encrypts the secret value, but it does not encrypt the secret name and description, the rotation settings, the ARN of the KMS key associated with the secret, or any attached AWS tags.
  scope: per secret.
  link: [encrypts the secret value](../facts/secrets-manager.md#secrets-manager-metadata-not-encrypted)
  link: [does not encrypt the following](../facts/secrets-manager.md#secrets-manager-metadata-not-encrypted)
secrets-manager-move-hardcoded-then-rotate
  claim: For plaintext database credentials in code, AWS recommends moving them to Secrets Manager and then rotating them immediately, which revokes the old hard-coded password.
  scope: per database credential.
  link: [move the credentials to Secrets Manager](../facts/secrets-manager.md#secrets-manager-move-hardcoded-then-rotate)
  link: [then rotate them immediately](../facts/secrets-manager.md#secrets-manager-move-hardcoded-then-rotate)
  link: [revokes the current hardcoded password](../facts/secrets-manager.md#secrets-manager-move-hardcoded-then-rotate)
secrets-manager-no-charge-marked-for-deletion
  claim: Secrets Manager does not charge for secrets that are marked for deletion.
  scope: per secret; during the recovery window.
  link: [no charge for secrets](../facts/secrets-manager.md#secrets-manager-no-charge-marked-for-deletion)
  link: [marked for deletion](../facts/secrets-manager.md#secrets-manager-no-charge-marked-for-deletion)
secrets-manager-no-charge-new-versions
  claim: Rotating a secret creates a new version of the secret, and Secrets Manager does not charge for creating new versions.
  scope: per secret.
  link: [not charged for creating new versions](../facts/secrets-manager.md#secrets-manager-no-charge-new-versions)
secrets-manager-no-linear-version-history
  claim: Secrets Manager does not keep a linear history of secret versions; it tracks three specific versions with the labels AWSCURRENT, AWSPREVIOUS and AWSPENDING.
  scope: per secret.
  link: [doesn't store a linear history of secrets](../facts/secrets-manager.md#secrets-manager-no-linear-version-history)
  link: [three specific versions by labeling them](../facts/secrets-manager.md#secrets-manager-no-linear-version-history)
secrets-manager-not-changed-more-likely-compromised
  claim: Secrets that are not changed for a long time become more likely to be compromised, which is why AWS recommends rotating them.
  scope: per secret.
  link: [become more likely to be compromised](../facts/secrets-manager.md#secrets-manager-not-changed-more-likely-compromised)
  link: [for a long period of time](../facts/secrets-manager.md#secrets-manager-not-changed-more-likely-compromised)
secrets-manager-pay-per-secret-and-call
  claim: With Secrets Manager you pay based on the number of secrets stored and the API calls made, with no upfront costs or long-term contracts.
  scope: per account.
  link: [number of secrets stored and API calls made](../facts/secrets-manager.md#secrets-manager-pay-per-secret-and-call)
  link: [no upfront costs or long-term contracts](../facts/secrets-manager.md#secrets-manager-pay-per-secret-and-call)
secrets-manager-promote-replica-for-dr
  claim: You might promote a replica secret to a standalone secret for disaster recovery when the primary secret becomes unavailable, or to turn on rotation for the replica.
  scope: per replica secret.
  link: [as a disaster recovery solution](../facts/secrets-manager.md#secrets-manager-promote-replica-for-dr)
  link: [if the primary secret becomes unavailable](../facts/secrets-manager.md#secrets-manager-promote-replica-for-dr)
secrets-manager-promote-replica-standalone
  claim: Promoting a replica secret disconnects it from the primary and makes it a standalone secret; later changes to the primary no longer replicate to it.
  scope: per replica secret.
  link: [makes the replica secret a standalone secret](../facts/secrets-manager.md#secrets-manager-promote-replica-standalone)
  link: [Changes to the primary secret won't replicate](../facts/secrets-manager.md#secrets-manager-promote-replica-standalone)
secrets-manager-put-resource-policy-replaces
  claim: If a secret already has a resource policy, PutResourcePolicy replaces it with the new policy.
  scope: per secret.
  link: [replaces it with the new policy](../facts/secrets-manager.md#secrets-manager-put-resource-policy-replaces)
  link: [already a policy attached](../facts/secrets-manager.md#secrets-manager-put-resource-policy-replaces)
secrets-manager-putresourcepolicy-escalation
  claim: A resource policy that grants secretsmanager:PutResourcePolicy lets principals, even in other accounts, change the resource policy and so escalate their permissions; AWS recommends least privilege.
  scope: per secret resource policy.
  link: [the ability to modify your resource-based policies](../facts/secrets-manager.md#secrets-manager-putresourcepolicy-escalation)
  link: [even those in other accounts](../facts/secrets-manager.md#secrets-manager-putresourcepolicy-escalation)
secrets-manager-quota-batchgetsecretvalue-rate
  claim: Secrets Manager accepts BatchGetSecretValue requests at 100 per second in each supported Region, and this quota is not adjustable.
  scope: per account, per Region; maximum; not adjustable.
  link: [100 per second](../facts/secrets-manager.md#secrets-manager-quota-batchgetsecretvalue-rate)
  say: one hundred per second
secrets-manager-quota-createsecret-rate
  claim: Secrets Manager accepts CreateSecret requests at 50 per second in each supported Region, and this quota is not adjustable.
  scope: per account, per Region; maximum; not adjustable.
  link: [50 per second](../facts/secrets-manager.md#secrets-manager-quota-createsecret-rate)
  say: fifty per second
secrets-manager-quota-describesecret-rate
  claim: Secrets Manager accepts DescribeSecret requests at 40,000 per second in each supported Region, and this quota is not adjustable.
  scope: per account, per Region; maximum; not adjustable.
  link: [40,000 per second](../facts/secrets-manager.md#secrets-manager-quota-describesecret-rate)
  say: forty thousand per second
secrets-manager-quota-getsecretvalue-rate
  claim: Secrets Manager accepts GetSecretValue requests at 10,000 per second in each supported Region, and this quota is not adjustable.
  scope: per account, per Region; maximum; not adjustable; for cross-account requests the quota of the calling identity's account applies.
  link: [10,000 per second](../facts/secrets-manager.md#secrets-manager-quota-getsecretvalue-rate)
  say: ten thousand per second
secrets-manager-quota-listsecrets-rate
  claim: Secrets Manager accepts ListSecrets requests at 100 per second in each supported Region, and this quota is not adjustable.
  scope: per account, per Region; maximum; not adjustable.
  link: [100 per second](../facts/secrets-manager.md#secrets-manager-quota-listsecrets-rate)
  say: one hundred per second
secrets-manager-quota-resource-policy-length
  claim: A resource-based permissions policy attached to a secret can have at most 20,480 characters, and this limit is not adjustable.
  scope: per secret; maximum; not adjustable.
  link: [20,480](../facts/secrets-manager.md#secrets-manager-quota-resource-policy-length)
  say: twenty thousand four hundred eighty characters
secrets-manager-quota-rotatesecret-rate
  claim: RotateSecret and CancelRotateSecret requests share a combined rate of 50 per second in each supported Region, and this quota is not adjustable.
  scope: per account, per Region; combined across RotateSecret and CancelRotateSecret; maximum; not adjustable.
  link: [50 per second](../facts/secrets-manager.md#secrets-manager-quota-rotatesecret-rate)
  say: fifty per second
secrets-manager-quota-secret-value-size
  claim: An encrypted secret value can be at most 65,536 Bytes; for a string secret this is the number of characters allowed. The limit is not adjustable.
  scope: per secret value; maximum; not adjustable; for a string secret the limit counts characters.
  link: [65,536 Bytes](../facts/secrets-manager.md#secrets-manager-quota-secret-value-size)
  say: sixty-five thousand five hundred thirty-six bytes, which is sixty-four kilobytes
secrets-manager-quota-secrets-per-region
  claim: An AWS account can have at most 500,000 secrets in each AWS Region, and this quota is not adjustable.
  scope: per account, per Region; maximum; not adjustable.
  link: [500,000](../facts/secrets-manager.md#secrets-manager-quota-secrets-per-region)
  say: five hundred thousand
secrets-manager-quota-staging-labels-per-secret
  claim: At most 20 staging labels can be attached across all versions of one secret, and this limit is not adjustable.
  scope: per secret, across all its versions; maximum; not adjustable.
  link: [20](../facts/secrets-manager.md#secrets-manager-quota-staging-labels-per-secret)
  say: twenty
secrets-manager-quota-versions-per-secret
  claim: A secret can have at most 100 versions, and this limit is not adjustable.
  scope: per secret; maximum; not adjustable.
  link: [100](../facts/secrets-manager.md#secrets-manager-quota-versions-per-secret)
  say: one hundred
secrets-manager-quota-write-apis-rate
  claim: PutSecretValue, UpdateSecret, UpdateSecretVersionStage and the replication API requests share a combined rate of 50 per second in each supported Region, and this quota is not adjustable.
  scope: per account, per Region; combined across PutSecretValue, RemoveRegionsFromReplication, ReplicateSecretToRegion, StopReplicationToReplica, UpdateSecret and UpdateSecretVersionStage; maximum; not adjustable.
  link: [50 per second](../facts/secrets-manager.md#secrets-manager-quota-write-apis-rate)
  say: fifty per second
secrets-manager-rds-generates-master-password
  claim: When you let Amazon RDS manage the master user password in Secrets Manager, RDS generates the password and stores it in Secrets Manager; you can use a customer managed key or the key provided by Secrets Manager.
  scope: per RDS DB instance or Multi-AZ DB cluster.
  link: [RDS generates the password](../facts/secrets-manager.md#secrets-manager-rds-generates-master-password)
  link: [a customer managed key to encrypt the secret](../facts/secrets-manager.md#secrets-manager-rds-generates-master-password)
secrets-manager-rds-integration-not-blue-green
  claim: RDS management of master user passwords in Secrets Manager is not supported for some features, including Amazon RDS Blue/Green Deployments, Amazon RDS Custom, and creating a read replica from a source that manages credentials this way (except RDS for SQL Server and RDS for Db2).
  scope: per RDS DB instance or cluster.
  link: [isn't supported for the following features](../facts/secrets-manager.md#secrets-manager-rds-integration-not-blue-green)
  link: [Amazon RDS Blue/Green Deployments](../facts/secrets-manager.md#secrets-manager-rds-integration-not-blue-green)
secrets-manager-rds-managed-rotation-default
  claim: When Amazon RDS manages the master user password in Secrets Manager, RDS rotates the secret every seven days by default, and you can change the rotation schedule.
  scope: per RDS-managed master user secret; default; adjustable; RDS manages the secret settings; the rotation schedule can be modified.
  link: [every seven days](../facts/secrets-manager.md#secrets-manager-rds-managed-rotation-default)
  say: every seven days
secrets-manager-rds-managed-secret-charged
  claim: When Amazon RDS (including Aurora) creates a managed secret for the master user credentials, you are charged for that secret.
  scope: per RDS-managed secret.
  link: [You are charged for that secret](../facts/secrets-manager.md#secrets-manager-rds-managed-secret-charged)
secrets-manager-rds-rotates-without-app-changes
  claim: With RDS-managed master passwords, RDS rotates the database credentials regularly without requiring application changes.
  scope: per RDS DB instance or cluster.
  link: [without requiring application changes](../facts/secrets-manager.md#secrets-manager-rds-rotates-without-app-changes)
  link: [RDS rotates database credentials regularly](../facts/secrets-manager.md#secrets-manager-rds-rotates-without-app-changes)
secrets-manager-rds-secret-deleted-with-instance
  claim: If you delete a DB instance whose master password is managed in Secrets Manager, the secret and its metadata are deleted too.
  scope: per RDS DB instance; RDS manages the master user password.
  link: [its associated metadata are also deleted](../facts/secrets-manager.md#secrets-manager-rds-secret-deleted-with-instance)
  link: [If you delete a DB instance](../facts/secrets-manager.md#secrets-manager-rds-secret-deleted-with-instance)
secrets-manager-read-needs-kms-decrypt
  claim: To read a secret value that is encrypted with a customer managed key, the principal needs kms:Decrypt on that key; to create or change the value it also needs kms:GenerateDataKey.
  scope: per principal and KMS key; customer managed key.
  link: [the principal needs `kms:Decrypt`](../facts/secrets-manager.md#secrets-manager-read-needs-kms-decrypt)
  link: [also grant `kms:GenerateDataKey`](../facts/secrets-manager.md#secrets-manager-read-needs-kms-decrypt)
secrets-manager-recover-during-window
  claim: Until the recovery window ends, you can recover a secret that you deleted; after Secrets Manager deletes it permanently, you cannot recover it.
  scope: per secret; before the recovery window ends.
  link: [Until the recovery window ends](../facts/secrets-manager.md#secrets-manager-recover-during-window)
  link: [you can recover a secret you previously deleted](../facts/secrets-manager.md#secrets-manager-recover-during-window)
secrets-manager-recovery-window-default
  claim: If a DeleteSecret call sets neither a recovery window nor force deletion, Secrets Manager uses a 30 day recovery window by default.
  scope: per DeleteSecret call; default; adjustable; applies when neither RecoveryWindowInDays nor ForceDeleteWithoutRecovery is set.
  link: [30 day](../facts/secrets-manager.md#secrets-manager-recovery-window-default)
  say: thirty days
secrets-manager-recovery-window-range
  claim: When you delete a secret, the recovery window is a number of days from 7 to 30 that Secrets Manager waits before it deletes the secret permanently.
  scope: per DeleteSecret call; maximum; not adjustable; the minimum is 7 days; ForceDeleteWithoutRecovery skips the window.
  link: [from 7 to 30](../facts/secrets-manager.md#secrets-manager-recovery-window-range)
  say: from seven to thirty days
secrets-manager-recreated-secret-new-arn
  claim: If a secret is deleted and a new secret is created with the same name, users with access to the old secret do not automatically get access to the new one, because the ARNs differ.
  scope: per secret; the old secret was deleted and a new one created with the same name.
  link: [don't automatically get access to the new secret](../facts/secrets-manager.md#secrets-manager-recreated-secret-new-arn)
  link: [the ARNs are different](../facts/secrets-manager.md#secrets-manager-recreated-secret-new-arn)
secrets-manager-replica-linked-to-primary
  claim: When you replicate a secret to another Region, the replica secret stays linked to the primary secret.
  scope: per replica secret; until the replica is promoted to a standalone secret.
  link: [remains linked to the primary secret](../facts/secrets-manager.md#secrets-manager-replica-linked-to-primary)
  link: [The replica secret remains linked](../facts/secrets-manager.md#secrets-manager-replica-linked-to-primary)
secrets-manager-replica-own-kms-key
  claim: A replica secret has the same value and metadata as the primary but can be encrypted with a different KMS key; apart from its encryption key, it cannot be updated independently of the primary.
  scope: per replica secret; until promoted to a standalone secret.
  link: [can be encrypted with a different KMS key](../facts/secrets-manager.md#secrets-manager-replica-own-kms-key)
  link: [can't be updated independently from its primary secret](../facts/secrets-manager.md#secrets-manager-replica-own-kms-key)
secrets-manager-replica-same-arn-except-region
  claim: The ARN of a replica secret is the same as the ARN of the primary secret except for the Region.
  scope: per replica secret.
  link: [same as the primary secret](../facts/secrets-manager.md#secrets-manager-replica-same-arn-except-region)
  link: [except for the Region](../facts/secrets-manager.md#secrets-manager-replica-same-arn-except-region)
secrets-manager-replicates-data-and-metadata
  claim: Secrets Manager replicates the encrypted secret data and metadata, such as tags and resource policies, across the Regions you specify.
  scope: per replicated secret.
  link: [replicates the encrypted secret data and metadata](../facts/secrets-manager.md#secrets-manager-replicates-data-and-metadata)
  link: [such as tags and resource policies](../facts/secrets-manager.md#secrets-manager-replicates-data-and-metadata)
secrets-manager-replication-for-dr
  claim: Secrets Manager can automatically replicate secrets to multiple AWS Regions to meet resiliency or disaster recovery requirements.
  scope: per secret.
  link: [automatically replicate your secrets to multiple AWS Regions](../facts/secrets-manager.md#secrets-manager-replication-for-dr)
  link: [resiliency or disaster recovery requirements](../facts/secrets-manager.md#secrets-manager-replication-for-dr)
secrets-manager-replication-not-to-special-regions
  claim: You can replicate secrets across all your enabled commercial Regions, but you cannot replicate between commercial Regions and special Regions such as AWS GovCloud (US) or China; the target Region must be enabled first.
  scope: per secret.
  link: [across all of your enabled AWS Regions](../facts/secrets-manager.md#secrets-manager-replication-not-to-special-regions)
  link: [You can't replicate a secret](../facts/secrets-manager.md#secrets-manager-replication-not-to-special-regions)
  link: [to a specialized Region](../facts/secrets-manager.md#secrets-manager-replication-not-to-special-regions)
secrets-manager-resource-policy-who-and-what
  claim: A resource-based policy on a secret says who can access the secret and which actions they can perform; it can grant access to users or roles in other AWS accounts.
  scope: per secret.
  link: [you specify who can access the secret](../facts/secrets-manager.md#secrets-manager-resource-policy-who-and-what)
  link: [users or roles in other AWS accounts](../facts/secrets-manager.md#secrets-manager-resource-policy-who-and-what)
secrets-manager-rotation-function-called-per-step
  claim: During rotation, Secrets Manager calls the same Lambda rotation function several times, each time with different parameters (the steps create_secret, set_secret, test_secret and finish_secret).
  scope: per rotation; rotation by Lambda function.
  link: [calls the same function several times](../facts/secrets-manager.md#secrets-manager-rotation-function-called-per-step)
  link: [each time with different parameters](../facts/secrets-manager.md#secrets-manager-rotation-function-called-per-step)
secrets-manager-rotation-function-needs-endpoint
  claim: A Lambda rotation function must be able to reach a Secrets Manager endpoint; if it can reach the internet it can use the public endpoint.
  scope: per rotation function; rotation by Lambda function.
  link: [access a Secrets Manager endpoint](../facts/secrets-manager.md#secrets-manager-rotation-function-needs-endpoint)
  link: [you can use a public endpoint](../facts/secrets-manager.md#secrets-manager-rotation-function-needs-endpoint)
secrets-manager-rotation-function-same-vpc
  claim: If the database runs on an Amazon EC2 instance in a VPC, AWS recommends running the rotation function in the same VPC so that it can talk to the database directly.
  scope: per rotation function; database or service in a VPC.
  link: [run in the same VPC](../facts/secrets-manager.md#secrets-manager-rotation-function-same-vpc)
  link: [can communicate directly with your service](../facts/secrets-manager.md#secrets-manager-rotation-function-same-vpc)
secrets-manager-rotation-nat-gateway-more-risk
  claim: Giving the rotation function a NAT gateway or internet gateway to reach the public endpoint exposes the VPC to more risk, because the gateway's IP address can be attacked from the internet.
  scope: per VPC; NAT gateway or internet gateway used instead of a VPC endpoint.
  link: [This exposes your VPC to more risk](../facts/secrets-manager.md#secrets-manager-rotation-nat-gateway-more-risk)
  link: [can be attacked from the public Internet](../facts/secrets-manager.md#secrets-manager-rotation-nat-gateway-more-risk)
secrets-manager-rotation-private-vpc-use-endpoint
  claim: If the rotation function runs in a VPC without internet access, AWS recommends configuring Secrets Manager private endpoints in the VPC.
  scope: per VPC; rotation function in a VPC without internet access.
  link: [Secrets Manager service private endpoints within your VPC](../facts/secrets-manager.md#secrets-manager-rotation-private-vpc-use-endpoint)
  link: [a VPC that doesn't have internet access](../facts/secrets-manager.md#secrets-manager-rotation-private-vpc-use-endpoint)
secrets-manager-rotation-propagates-to-replicas
  claim: If rotation is on for a primary secret, Secrets Manager rotates it in the primary Region and the new value propagates to all replica secrets; you do not manage rotation for each replica.
  scope: per replicated secret; rotation turned on for the primary secret.
  link: [rotates the secret in the primary Region](../facts/secrets-manager.md#secrets-manager-rotation-propagates-to-replicas)
  link: [propagates to all of the associated replica secrets](../facts/secrets-manager.md#secrets-manager-rotation-propagates-to-replicas)
secrets-manager-rotation-retries-in-window
  claim: If any rotation step fails, Secrets Manager retries the whole rotation several times during the open rotation windows of the secret.
  scope: per secret; rotation by Lambda function.
  link: [retries the entire rotation process multiple times](../facts/secrets-manager.md#secrets-manager-rotation-retries-in-window)
  link: [during the open rotation windows](../facts/secrets-manager.md#secrets-manager-rotation-retries-in-window)
secrets-manager-rotation-schedule-utc
  claim: Secrets Manager rotation schedules use the UTC time zone, and the secret rotates at any time during the rotation window that you set.
  scope: per secret.
  link: [use UTC time zone](../facts/secrets-manager.md#secrets-manager-rotation-schedule-utc)
  link: [at any time during the rotation window](../facts/secrets-manager.md#secrets-manager-rotation-schedule-utc)
secrets-manager-rotation-schedule-utc-and-year
  claim: A cron() rotation schedule must have * in the year field, because Secrets Manager does not support rotation schedules that are more than a year apart; with a rate() expression the maximum rotation period is 999 days. Rotation schedules use the UTC time zone.
  scope: per rotation schedule.
  link: [more than a year apart](../facts/secrets-manager.md#secrets-manager-rotation-schedule-utc-and-year)
  link: [use UTC time zone](../facts/secrets-manager.md#secrets-manager-rotation-schedule-utc-and-year)
secrets-manager-rotation-security-groups
  claim: For the rotation function to reach the database, its security groups must allow outbound connections to the database, and the database's security groups must allow inbound connections from the function.
  scope: per rotation function and database; rotation by Lambda function.
  link: [allow outbound connections to the database or service](../facts/secrets-manager.md#secrets-manager-rotation-security-groups)
  link: [allow inbound connections from the Lambda rotation function](../facts/secrets-manager.md#secrets-manager-rotation-security-groups)
secrets-manager-rotation-shortest-and-longest
  claim: A secret can be rotated as often as every four hours, and the maximum rotation period is 999 days.
  scope: per secret rotation schedule; maximum; not adjustable; the minimum interval is four hours.
  link: [every four hours](../facts/secrets-manager.md#secrets-manager-rotation-shortest-and-longest)
  link: [999 days](../facts/secrets-manager.md#secrets-manager-rotation-shortest-and-longest)
  say: every four hours | nine hundred ninety-nine days
secrets-manager-rotation-templates-ready-lambda
  claim: Secrets Manager provides rotation function templates, ready-to-use Lambda functions for single-user and alternating-users rotation of many database systems, plus a generic template as a starting point for any type of secret.
  scope: per account.
  link: [ready-to-use Lambda functions](../facts/secrets-manager.md#secrets-manager-rotation-templates-ready-lambda)
  link: [generic template that serves as a starting point](../facts/secrets-manager.md#secrets-manager-rotation-templates-ready-lambda)
secrets-manager-rotation-window-minimum
  claim: A rotation window can be as small as one hour, and it must not extend into the next rotation window.
  scope: per rotation schedule; minimum; not adjustable; the window must not extend into the next rotation window.
  link: [one hour](../facts/secrets-manager.md#secrets-manager-rotation-window-minimum)
  say: one hour
secrets-manager-rotation-window-starts-on-hour
  claim: Secrets Manager rotation windows always start on the hour, and a window must not extend into the next rotation window.
  scope: per secret.
  link: [always start on the hour](../facts/secrets-manager.md#secrets-manager-rotation-window-starts-on-hour)
  link: [must not extend into the next rotation window](../facts/secrets-manager.md#secrets-manager-rotation-window-starts-on-hour)
secrets-manager-rotation-without-redeploy
  claim: Because the credentials are no longer stored with the application, rotating them no longer requires updating the application and deploying changes to its clients.
  scope: per secret; the application reads the secret at run time.
  link: [no longer requires updating your applications](../facts/secrets-manager.md#secrets-manager-rotation-without-redeploy)
  link: [no longer stored with the application](../facts/secrets-manager.md#secrets-manager-rotation-without-redeploy)
secrets-manager-runtime-call-replaces-hardcoded
  claim: With Secrets Manager you replace hard-coded credentials with a runtime call that retrieves the credentials when the application needs them.
  scope: per application.
  link: [runtime call to the Secrets Manager service](../facts/secrets-manager.md#secrets-manager-runtime-call-replaces-hardcoded)
  link: [retrieve credentials dynamically when you need them](../facts/secrets-manager.md#secrets-manager-runtime-call-replaces-hardcoded)
secrets-manager-scheduled-secret-not-accessible
  claim: Secrets Manager treats a secret that is scheduled for deletion as deprecated, and you can no longer access it directly.
  scope: per secret; during the recovery window.
  link: [you can no longer directly access it](../facts/secrets-manager.md#secrets-manager-scheduled-secret-not-accessible)
  link: [considers a secret scheduled for deletion](../facts/secrets-manager.md#secrets-manager-scheduled-secret-not-accessible)
secrets-manager-secret-same-region-as-db
  claim: For the lowest latency, store the secret in the same Region as the database.
  scope: per database secret.
  link: [in the same Region as the database](../facts/secrets-manager.md#secrets-manager-secret-same-region-as-db)
  link: [For the lowest latency](../facts/secrets-manager.md#secrets-manager-secret-same-region-as-db)
secrets-manager-single-user-rotation-keeps-connections
  claim: With the single-user rotation strategy, open database connections are not dropped when the secret rotates; new connections use the new credentials after rotation.
  scope: per database secret; single-user rotation by Lambda function.
  link: [open database connections are not dropped](../facts/secrets-manager.md#secrets-manager-single-user-rotation-keeps-connections)
  link: [new connections use the new credentials](../facts/secrets-manager.md#secrets-manager-single-user-rotation-keeps-connections)
secrets-manager-single-user-short-deny-risk
  claim: During single-user rotation there is a short period between the password change in the database and the secret update, with a low risk that the database denies calls that use the rotated credentials; a retry strategy reduces this risk.
  scope: per database secret; single-user rotation by Lambda function.
  link: [low risk of the database denying calls](../facts/secrets-manager.md#secrets-manager-single-user-short-deny-risk)
  link: [there is a short period of time](../facts/secrets-manager.md#secrets-manager-single-user-short-deny-risk)
secrets-manager-single-user-strategy-for-most-cases
  claim: Single-user rotation updates the credentials of one user in one secret; AWS calls it the simplest strategy and appropriate for most use cases.
  scope: per database secret; rotation by Lambda function.
  link: [This is the simplest rotation strategy](../facts/secrets-manager.md#secrets-manager-single-user-strategy-for-most-cases)
  link: [appropriate for most use cases](../facts/secrets-manager.md#secrets-manager-single-user-strategy-for-most-cases)
secrets-manager-source-vpce-condition
  claim: To allow or deny requests from a particular VPC or VPC endpoint, use the condition key aws:SourceVpc or aws:SourceVpce in the policy.
  scope: per policy statement.
  link: [requests from the specified VPC endpoint](../facts/secrets-manager.md#secrets-manager-source-vpce-condition)
  link: [aws:SourceVpce](../facts/secrets-manager.md#secrets-manager-source-vpce-condition)
secrets-manager-staging-label-unique
  claim: Two versions of one secret cannot carry the same staging label, but one version can have several labels.
  scope: per secret.
  link: [can't have the same staging label](../facts/secrets-manager.md#secrets-manager-staging-label-unique)
  link: [Versions can have multiple labels](../facts/secrets-manager.md#secrets-manager-staging-label-unique)
secrets-manager-unique-data-key-per-secret
  claim: Every secret in Secrets Manager is encrypted with a unique data key, and each data key is protected by a KMS key; Secrets Manager never stores the data key unencrypted.
  scope: per secret.
  link: [encrypted with a unique data key](../facts/secrets-manager.md#secrets-manager-unique-data-key-per-secret)
  link: [never stores the data key in unencrypted form](../facts/secrets-manager.md#secrets-manager-unique-data-key-per-secret)
secrets-manager-unlabeled-versions-cleanup
  claim: Secrets Manager never removes labeled versions; it removes deprecated (unlabeled) versions when there are more than 100, but not versions created less than 24 hours ago.
  scope: per secret; applies to unlabeled (deprecated) versions only.
  link: [more than 100](../facts/secrets-manager.md#secrets-manager-unlabeled-versions-cleanup)
  link: [24 hours](../facts/secrets-manager.md#secrets-manager-unlabeled-versions-cleanup)
  say: more than one hundred | twenty-four hours
secrets-manager-update-rate-recommendation
  claim: AWS recommends not calling PutSecretValue or UpdateSecret at a sustained rate of more than once every 10 minutes, because faster updates create versions faster than Secrets Manager removes them.
  scope: per secret; sustained rate; a recommendation, not an enforced quota.
  link: [once every 10 minutes](../facts/secrets-manager.md#secrets-manager-update-rate-recommendation)
  say: once every ten minutes
secrets-manager-use-secret-cross-region-without-replication
  claim: An application can use a secret from another Region without replicating it by calling the Secrets Manager endpoint in the Region where the secret is stored.
  scope: per secret.
  link: [without replicating it](../facts/secrets-manager.md#secrets-manager-use-secret-cross-region-without-replication)
  link: [in the Region where the secret is stored](../facts/secrets-manager.md#secrets-manager-use-secret-cross-region-without-replication)
secrets-manager-value-string-or-binary
  claim: A secret value can be a string or binary data.
  scope: per secret value.
  link: [can be a string or binary](../facts/secrets-manager.md#secrets-manager-value-string-or-binary)
  link: [string or binary](../facts/secrets-manager.md#secrets-manager-value-string-or-binary)
secrets-manager-vpc-condition-can-block-services
  claim: VPC or VPC endpoint conditions in a secret's resource policy can unintentionally deny AWS services that read the secret on your behalf.
  scope: per secret resource policy; aws:SourceVpc or aws:SourceVpce conditions.
  link: [you can inadvertently deny access to services](../facts/secrets-manager.md#secrets-manager-vpc-condition-can-block-services)
  link: [access secrets on your behalf](../facts/secrets-manager.md#secrets-manager-vpc-condition-can-block-services)
secrets-manager-wa-anti-patterns
  claim: Well-Architected SEC02-BP03 lists as common anti-patterns storing long-term credentials in source code or configuration files, and storing credentials at rest unencrypted.
  scope: per workload.
  link: [credentials in source code or configuration files](../facts/secrets-manager.md#secrets-manager-wa-anti-patterns)
  link: [Storing credentials at rest unencrypted](../facts/secrets-manager.md#secrets-manager-wa-anti-patterns)
secrets-manager-wa-benefits-credential-vending
  claim: Well-Architected names as benefits of a secrets service that secrets are encrypted at rest and in transit, access is gated through an API like a credential vending machine, and every read and write of a credential is audited and logged.
  scope: per workload.
  link: [stored encrypted at rest and in transit](../facts/secrets-manager.md#secrets-manager-wa-benefits-credential-vending)
  link: [is audited and logged](../facts/secrets-manager.md#secrets-manager-wa-benefits-credential-vending)
  link: [credential vending machine](../facts/secrets-manager.md#secrets-manager-wa-benefits-credential-vending)
secrets-manager-wa-db-credentials-rotate
  claim: Well-Architected SEC02-BP03 suggests replacing a hard-coded AWS secret access key, a long-term credential, with a temporary credential using IAM roles.
  scope: per workload.
  link: [a temporary credential using IAM roles](../facts/secrets-manager.md#secrets-manager-wa-db-credentials-rotate)
  link: [instead of hard-coding an AWS secret access key](../facts/secrets-manager.md#secrets-manager-wa-db-credentials-rotate)
secrets-manager-wa-remove-replace-rotate
  claim: Well-Architected SEC02-BP03 says the best approach to secrets management is remove, replace and rotate: the most secure credential is one you do not have to store, manage or handle.
  scope: per workload.
  link: [remove, replace, and rotate](../facts/secrets-manager.md#secrets-manager-wa-remove-replace-rotate)
  link: [one that you do not have to store](../facts/secrets-manager.md#secrets-manager-wa-remove-replace-rotate)
secrets-manager-what-it-manages
  claim: AWS Secrets Manager helps you manage, retrieve, and rotate database credentials, application credentials, OAuth tokens, API keys, and other secrets through their lifecycle.
  scope: per secret.
  link: [manage, retrieve, and rotate database credentials](../facts/secrets-manager.md#secrets-manager-what-it-manages)
  link: [OAuth tokens, API keys, and other secrets](../facts/secrets-manager.md#secrets-manager-what-it-manages)
