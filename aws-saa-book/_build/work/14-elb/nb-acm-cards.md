facts card: 13 facts
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
acm-certificates-regional
  claim: ACM certificates are Regional resources: to use the same domain names with Elastic Load Balancing in more than one Region, you request or import a certificate in each Region, and you cannot copy a certificate between Regions.
  scope: per Region.
  link: [Certificates in ACM are regional resources](../facts/acm.md#acm-certificates-regional)
  link: [You cannot copy a certificate between regions](../facts/acm.md#acm-certificates-regional)
acm-faq-certificate-same-region-as-resource
  claim: ACM certificates must be in the same Region as the resource where they are being used; the only exception is Amazon CloudFront.
  scope: per certificate; except Amazon CloudFront.
  link: [must be in the same Region](../facts/acm.md#acm-faq-certificate-same-region-as-resource)
  link: [The only exception is Amazon CloudFront](../facts/acm.md#acm-faq-certificate-same-region-as-resource)
acm-elb-deploys-on-load-balancer
  claim: Load balancers need SSL/TLS certificates on either the load balancer or the back-end EC2 instance, and ACM is integrated with Elastic Load Balancing to deploy ACM certificates on the load balancer.
  scope: per load balancer.
  link: [deploy ACM certificates on the load balancer](../facts/acm.md#acm-elb-deploys-on-load-balancer)
  link: [either the load balancer or the back-end Amazon EC2 instance](../facts/acm.md#acm-elb-deploys-on-load-balancer)
acm-faq-imported-no-managed-renewal
  claim: ACM does not manage the renewal process for imported certificates; you are responsible for monitoring their expiration dates and renewing them before they expire.
  scope: per imported certificate; imported third-party certificates.
  link: [does not manage the renewal process](../facts/acm.md#acm-faq-imported-no-managed-renewal)
  link: [You are responsible for monitoring the expiration date](../facts/acm.md#acm-faq-imported-no-managed-renewal)
acm-wa-alb-strongest-security-policy
  claim: For a load balancer listener, choose the security policy with the strongest cipher suites that the connecting clients support.
  scope: per load balancer listener.
  link: [the strongest cipher suites supported by the clients](../facts/acm.md#acm-wa-alb-strongest-security-policy)
acm-wa-alb-apigw-mtls
  claim: Both API Gateway and Application Load Balancer support mutual TLS (mTLS) with client certificates.
  scope: per API Gateway API or ALB.
  link: [support mutual TLS (mTLS) using client certificates](../facts/acm.md#acm-wa-alb-apigw-mtls)
acm-faq-public-cert-internal-load-balancer
  claim: You can use public certificates for internal Elastic Load Balancing load balancers, but you can also consider AWS Private CA private certificates, which ACM can renew without validation.
  scope: per internal load balancer; load balancer with no public internet access.
  link: [renew without validation](../facts/acm.md#acm-faq-public-cert-internal-load-balancer)
  link: [consider using AWS Private CA](../facts/acm.md#acm-faq-public-cert-internal-load-balancer)
acm-alb-supported-key-lengths
  claim: For Application Load Balancer certificates, ACM supports RSA certificates with 2048, 3072 and 4096-bit key lengths, and all ECDSA certificates.
  scope: certificates for Application Load Balancer listeners.
  link: [2048, 3072, and 4096-bit](../facts/acm.md#acm-alb-supported-key-lengths)
  link: [all ECDSA certificates](../facts/acm.md#acm-alb-supported-key-lengths)
  say: two thousand forty-eight, three thousand seventy-two and four thousand ninety-six bit
acm-generates-key-automates-renewal
  claim: Use ACM for certificates on integrated services such as Elastic Load Balancing, CloudFront and API Gateway or when you want AWS to manage the lifecycle; ACM generates and manages the private key and automates renewal.
  scope: per certificate.
  link: [ACM generates and manages the private key](../facts/acm.md#acm-generates-key-automates-renewal)
  link: [want AWS to manage the certificate lifecycle](../facts/acm.md#acm-generates-key-automates-renewal)
  link: [automates renewal](../facts/acm.md#acm-generates-key-automates-renewal)
