<details>
<summary>Go deeper: a NAT gateway has limits of its own</summary>

A NAT gateway lives in [a specific Availability Zone](../facts/vpc.md#vpc-natgw-az-scope). It supports [5 Gbps](../facts/vpc.md#vpc-natgw-bandwidth) of bandwidth and scales [up to 100 Gbps](../facts/vpc.md#vpc-natgw-bandwidth). You [cannot associate a security group](../facts/vpc.md#vpc-natgw-no-security-group) with a NAT gateway. The default quota is [5 NAT gateways per Availability Zone](../facts/vpc.md#vpc-natgw-per-az-quota).

</details>

> **Try it:**