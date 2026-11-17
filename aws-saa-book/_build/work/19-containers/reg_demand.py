"""register-19: write demand statuses into brief.v0.json (found / partial / not-found).

Sources: mine-numbers+changes.json and mine-faq.json (their demand maps), mine-behavior+decisions.json
(its not_found notes), and the registrar's own map below for the behavior and decisions items, which
the behavior miner did not map. Superseded ids are followed to the kept fact; rejected ids are dropped.
"""
import json, collections
B = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/"
W = B + "_build/work/19-containers/"
SVCS = ["ecr", "ecs", "ecs-anywhere", "eks", "eks-anywhere", "eks-distro", "fargate"]
brief = json.load(open(W + "brief.v0.json"))
facts = {}
for s in SVCS:
    for line in open(B + "data/facts/%s.jsonl" % s):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f


def live(i):
    for _ in range(5):
        f = facts.get(i)
        if f is None:
            return None
        if f["status"] == "superseded":
            i = f["superseded_by"]
            continue
        if f["status"] == "rejected":
            return None
        return i
    return None


got = {}
ORDER = {"found": 0, "partial": 1, "not-found": 2}


def norm(s):
    s = s.lower()
    return {"filled": "found", "filled-partly": "partial", "partly-found": "partial", "found": "found"}.get(s, s)


def put(did, status, ids, note=None, force=False):
    g = got.setdefault(did, {"status": None, "facts": [], "notes": []})
    if force or g["status"] is None or ORDER[status] < ORDER[g["status"]]:
        g["status"] = status
    for i in ids:
        if i not in g["facts"]:
            g["facts"].append(i)
    if note:
        g["notes"].append(note)


num = json.load(open(W + "mine-numbers+changes.json"))
for did, x in num["demand"].items():
    put(did, norm(x["status"]), x.get("facts", []), x.get("note"))
faq = json.load(open(W + "mine-faq.json"))
for did, x in faq["demand"].items():
    put(did, norm(x["status"]), x.get("facts", []), x.get("not_found"))

R = {
 "d19-001": ("found", ["ecs-fully-managed-orchestration", "ecs-layer-capacity", "ecs-layer-controller", "ecs-layer-provisioning", "ecs-no-control-plane-to-manage"], None),
 "d19-002": ("found", ["ecs-cluster-is-infrastructure", "ecs-cluster-is-regional-and-mixes-capacity", "ecs-task-definition-json-blueprint", "ecs-task-is-instantiation-of-task-definition", "ecs-task-runs-then-stops", "ecs-faq-task-smallest-unit", "ecs-service-long-running-stateless", "ecs-service-maintains-desired-count"], None),
 "d19-003": ("found", ["ecs-service-maintains-desired-count", "ecs-service-scheduler-reschedules-on-infrastructure-failure", "ecs-service-scheduler-replaces-unhealthy-tasks", "ecs-faq-service-scheduler-recovers-unhealthy-containers", "ecs-replica-strategy-default-spreads-azs", "ecs-daemon-strategy-one-task-per-instance", "fargate-no-daemon-scheduling-strategy", "ecs-service-throttle-logic-failed-starts", "ecs-service-scheduler-for-long-running-stateless"], None),
 "d19-004": ("found", ["ecs-task-runs-then-stops", "ecs-eventbridge-scheduler-serverless-scheduler", "ecs-whitepaper-batch-runs-on-fargate-or-ec2"], None),
 "d19-005": ("found", ["ecs-capacity-providers-three-compute-types", "ecs-capacity-ec2-you-manage", "ecs-capacity-managed-instances", "ecs-cluster-fargate-serverless-pay-for-tasks", "ecs-cluster-ec2-full-control-you-manage-instances", "ecs-cluster-managed-instances-recommended-for-most-new-workloads", "ecs-anywhere-external-launch-type", "ecs-capacity-providers-recommended-over-launch-types", "ecs-launch-type-only-for-compatibility", "ecs-launch-type-to-launch-type-not-supported"], None),
 "d19-006": ("found", ["ecs-capacity-provider-manages-infrastructure-scaling", "ecs-capacity-provider-strategy-single-type", "ecs-strategy-fargate-or-asg-not-both", "ecs-strategy-only-one-base", "ecs-strategy-weight-zero-not-used", "ecs-faq-split-across-capacity-providers", "ecs-fargate-capacity-providers-auto-created", "ecs-faq-predefined-fargate-capacity-providers", "fargate-capacity-provider-must-be-associated-first", "ecs-strategy-update-moves-service-between-compute-types", "ecs-service-to-strategy-needs-new-deployment"], "register-19: the definition was missing; added ecs-capacity-provider-manages-infrastructure-scaling from the clusters page and service_definition_parameters (base and weight)."),
 "d19-008": ("found", ["ecs-cluster-auto-scaling-managed-scaling-asg-capacity-provider", "ecs-cluster-auto-scaling-policy-managed-by-ecs", "ecs-cluster-auto-scaling-reservation-above-or-below-target", "ecs-capacity-provider-reservation-metric-range", "ecs-managed-termination-protection-only-empty-instances", "ecs-managed-termination-protection-scale-in", "ecs-target-capacity-below-100-keeps-spare-instances", "ecs-asg-capacity-provider-new-empty-asg-recommended", "ecs-cluster-auto-scaling-vs-service", "ecs-provisioning-tasks-per-cluster-limit"], None),
 "d19-009": ("found", ["ecs-service-auto-scaling-application-auto-scaling", "ecs-service-auto-scaling-types-target-step-scheduled-predictive", "ecs-target-tracking-easiest-step-scaling-reacts-faster", "ecs-target-tracking-scale-out-fast-scale-in-slow", "ecs-service-auto-scaling-scale-in-blocked-during-deployment", "ecs-predictive-scaling-historical-patterns", "ecs-predictive-scaling-service-level-not-compute", "ecs-predictive-scaling-needs-24-hours-of-history", "ecs-faq-service-metrics-cpu-memory-for-app-auto-scaling", "ecs-faq-app-auto-scaling-custom-cloudwatch-metric", "ecs-scaling-target-headroom-60-80-percent", "ecs-scale-out-before-known-demand-shock"], None),
 "d19-010": ("found", ["ecs-sqs-scale-on-backlog-per-task", "ecs-sqs-scale-in-protection-task-processing"], None),
 "d19-011": ("found", ["ecs-alb-recommended-for-services", "ecs-faq-ingress-alb-nlb", "fargate-service-load-balancer-types", "ecs-awsvpc-load-balancer-target-type-ip", "fargate-target-group-ip-target-type", "fargate-classic-load-balancer-not-supported", "ecs-service-optional-load-balancer", "ecs-faq-service-scheduler-registers-containers-with-load-balancer"], "Source conflict on Gateway Load Balancer for Fargate services: see the note on fargate-service-load-balancer-types. Teach ALB and NLB; Classic Load Balancer is not supported."),
 "d19-013": ("found", ["ecs-rolling-update-replaces-tasks", "ecs-blue-green-definition-and-zero-downtime", "ecs-blue-green-doubles-resource-usage", "ecs-blue-green-native-similar-to-codedeploy", "ecs-change-native-blue-green-deployments-2025-07", "ecs-change-canary-deployments-2025-10", "ecs-change-linear-deployments-2025-10", "ecs-failed-deployment-detection-circuit-breaker-vs-alarms"], "register-19: fetched migrate-codedeploy-to-ecs-bluegreen: CodeDeploy blue/green and ECS blue/green provide similar functionality; with ECS blue/green the configuration is part of the ECS service. No page says CodeDeploy is obsolete; do not write that."),
 "d19-015": ("found", ["ecs-circuit-breaker-rolls-back-to-completed", "ecs-circuit-breaker-rolling-controller-only", "ecs-circuit-breaker-default-threshold-bounded-percent-50", "ecs-failed-deployment-detection-circuit-breaker-vs-alarms", "ecs-change-configurable-circuit-breaker-2026-07"], None),
 "d19-016": ("found", ["ecs-placement-strategy-types-binpack-random-spread", "ecs-placement-binpack-least-unused-cpu-memory", "ecs-placement-spread-balance-across-azs-on-scale-in", "ecs-placement-strategies-best-effort-constraints-binding", "ecs-placement-strategy-default-for-services-spread-az", "fargate-no-placement-constraints", "fargate-no-placement-strategies-best-effort-az-spread"], "register-19: service-rebalancing page says task placement strategies and constraints aren't supported for tasks using Fargate (fargate-no-placement-strategies-best-effort-az-spread)."),
 "d19-017": ("found", ["ecs-faq-network-mode-vpc", "ecs-faq-network-mode-bridge", "ecs-faq-network-mode-host", "ecs-faq-network-mode-none", "ecs-network-mode-awsvpc-own-eni", "ecs-network-mode-bridge-default-linux", "ecs-network-mode-host-one-task-per-port", "ecs-network-mode-none-no-external-connectivity", "ecs-awsvpc-network-mode-recommended-ec2", "ecs-awsvpc-task-own-eni-security-groups", "fargate-requires-awsvpc-network-mode", "ecs-bridge-mode-starts-faster-than-awsvpc-on-ec2", "ecs-faq-mi-network-modes", "ecs-managed-instances-linux-bottlerocket-network-modes"], None),
 "d19-019": ("found", ["ecs-awsvpc-eni-limits-tasks-per-instance", "ecs-awsvpc-trunking-increases-eni-density", "ecs-awsvpc-ec2-task-eni-no-public-ip"], None),
 "d19-020": ("found", ["fargate-private-subnet-image-pull-needs-nat", "fargate-public-subnet-image-pull-needs-public-ip", "fargate-task-has-route-to-internet-to-pull", "fargate-ecr-endpoint-uses-private-ip", "ecr-vpc-endpoints-fargate-need-ecr-and-s3", "ecr-privatelink-no-internet-gateway-needed", "ecr-vpc-endpoint-security-group-port-443", "ecs-interface-endpoint-privatelink-no-igw-nat", "ecs-interface-endpoints-incomplete-traffic-uses-public-endpoint"], None),
 "d19-021": ("found", ["ecs-service-connect-recommended-for-service-to-service", "ecs-service-connect-builds-discovery-and-mesh", "ecs-service-connect-proxy-container-in-each-task", "ecs-service-connect-same-namespace-only", "ecs-service-connecting-options-without-load-balancer", "ecs-service-discovery-cloud-map-dns", "ecs-service-discovery-retry-logic-disadvantage", "ecs-faq-service-connect-logical-names", "ecs-faq-service-discovery-cloud-map", "ecs-change-vpc-lattice-integration-2024-11"], None),
 "d19-025": ("found", ["ecs-iam-role-table-task-role", "ecs-iam-role-table-container-instance-role", "ecs-iam-role-table-ecs-anywhere-role", "ecs-task-role-gives-app-code-aws-permissions", "ecs-task-execution-role-for-agents", "ecs-container-instance-role-registers-agent"], None),
 "d19-026": ("found", ["ecs-task-role-gives-app-code-aws-permissions", "ecs-task-role-credentials-exclusive-no-instance-inheritance", "ecs-task-role-fargate-no-instance-profile", "ecs-task-role-least-privilege-per-task-definition", "ecs-containers-not-security-boundary-use-fargate-for-isolation", "ecs-faq-task-uses-iam-role", "ecs-one-task-definition-family-per-business-purpose"], None),
 "d19-027": ("found", ["ecs-task-execution-role-use-cases", "ecs-task-execution-role-for-agents", "ecr-ecs-agent-pull-permissions"], None),
 "d19-028": ("found", ["ecs-secrets-injected-from-secrets-manager-and-parameter-store"], None),
 "d19-029": ("found", ["ecs-private-registry-credentials-secrets-manager", "ecs-private-registry-secret-cross-region-account"], None),
 "d19-030": ("found", ["fargate-storage-types-ebs-efs-bind", "ecs-ebs-volume-per-task-managed-by-ecs", "ecs-efs-volumes-shared-persistent-across-instances", "fargate-no-docker-volumes", "fargate-ephemeral-storage-linux-only-windows-not"], "FSx for Windows File Server volumes for ECS: not mined."),
 "d19-032": ("found", ["fargate-ephemeral-storage-encrypted-by-default", "fargate-ephemeral-storage-cmk-audit-cloudtrail", "fargate-ephemeral-storage-cmk-no-extra-charge", "fargate-faq-ephemeral-storage-20-gib-erased"], None),
 "d19-033": ("found", ["ecs-ebs-volume-one-per-task-new-volume", "ecs-ebs-volume-per-task-managed-by-ecs", "ecs-ebs-volume-service-task-deleted-on-termination", "ecs-ebs-fargate-magnetic-not-supported", "fargate-ebs-volumes-need-linux-platform-1-4-0", "ecs-change-ebs-data-volume-per-task-2024-01"], None),
 "d19-034": ("found", ["ecs-efs-volumes-shared-persistent-across-instances", "ecs-efs-fargate-platform-14-linux-only", "fargate-faq-efs-for-persistent-storage"], None),
 "d19-035": ("partial", ["eks-stateless-application-no-session-data-deployment", "ecs-service-long-running-stateless", "ecs-task-size-stateless-small-reservations-cost", "fargate-faq-ephemeral-storage-20-gib-erased", "fargate-faq-efs-for-persistent-storage"], "No AWS sentence says in one place to design tasks stateless and keep state outside the task; the pieces are in the listed facts."),
 "d19-036": ("found", ["fargate-serverless-pay-as-you-go", "fargate-faq-serverless-engine-for-ecs-and-eks", "fargate-no-provision-vm-clusters", "fargate-whitepaper-own-kernel-for-ecs-and-eks", "eks-faq-works-with-fargate", "fargate-task-retirement-aws-maintains-infrastructure"], None),
 "d19-037": ("found", ["fargate-task-isolation-boundary", "eks-fargate-pod-own-compute-boundary", "fargate-faq-single-tenant-instance-per-workload", "ecs-faq-fargate-own-vm-and-network-interface", "fargate-whitepaper-own-kernel-for-ecs-and-eks"], None),
 "d19-039": ("found", ["fargate-no-privileged-containers", "fargate-limited-linux-capabilities", "fargate-no-host-access-ecs-exec", "fargate-containers-cannot-access-host-resources", "fargate-no-placement-constraints", "fargate-no-placement-strategies-best-effort-az-spread", "fargate-no-daemon-scheduling-strategy", "fargate-faq-gpu-not-supported", "fargate-requires-awsvpc-network-mode", "fargate-no-docker-volumes", "fargate-launch-type-requires-task-definition-config"], None),
 "d19-040": ("found", ["fargate-platform-version-defined", "fargate-new-tasks-latest-revision-patched", "fargate-vulnerable-revision-tasks-retired", "fargate-task-retirement-aws-maintains-infrastructure"], "The meaning of LATEST was not mined."),
 "d19-041": ("found", ["fargate-spot-interruption-tolerant-discount", "fargate-spot-two-minute-interruption-warning", "fargate-spot-warning-delivery-sigterm-eventbridge", "fargate-spot-container-must-handle-sigterm", "fargate-spot-no-on-demand-replacement", "fargate-spot-single-task-service-interrupted", "fargate-faq-spot-up-to-70-percent-discount"], None),
 "d19-042": ("found", ["fargate-spot-linux-only-pricing-page", "eks-fargate-no-spot", "ecs-change-fargate-spot-linux-arm-2024-09"], None),
 "d19-043": ("found", ["fargate-windows-containers-x86-64-only", "fargate-faq-arm-on-ecs-via-arm64", "fargate-faq-arm-on-eks-not-supported", "fargate-task-size-1-vcpu-linux-windows", "fargate-faq-windows-license-built-into-price"], None),
 "d19-044": ("found", ["fargate-task-retirement-aws-maintains-infrastructure", "fargate-retirement-notification-channels", "fargate-retirement-wait-time-default", "fargate-retirement-event-windows-precedence", "fargate-retirement-no-opt-out", "fargate-retirement-service-tasks-replaced-automatically", "fargate-retirement-host-issue-no-notice"], None),
 "d19-045": ("found", ["fargate-soci-lazy-loading-faster-start", "fargate-soci-linux-1-4-0-only-not-windows", "fargate-soci-try-for-images-over-250-mib", "fargate-faq-zstd-images-start-faster", "ecs-keep-images-in-same-region-as-workload"], None),
 "d19-046": ("found", ["ecs-managed-instances-full-range-ec2-aws-manages", "ecs-capacity-managed-instances", "ecs-managed-instances-default-instance-selection", "ecs-managed-instances-multi-task-placement-default", "ecs-managed-instances-limited-lifetime-patching", "ecs-managed-instances-fargate-task-definition-compatible", "ecs-managed-instances-need-capacity-provider-strategy", "ecs-managed-instances-two-iam-roles", "ecs-managed-instances-privileged-capabilities-allowed", "ecs-faq-mi-same-operational-benefits-as-fargate", "ecs-faq-mi-additional-benefits-over-fargate", "ecs-faq-mi-compute-in-your-account-billing", "ecs-pricing-managed-instances-management-fee"], "Instance lifetime: source conflict 14 days (guide, FAQ) versus 21 days (document history 2025-12-11); state neither number as exact."),
 "d19-048": ("found", ["ecs-express-mode-creates-fargate-alb-autoscaling", "ecs-express-mode-three-inputs", "ecs-express-mode-use-cases-web-apps-apis", "ecs-express-mode-shares-alb-reduces-cost", "ecs-express-mode-no-additional-charge", "ecs-faq-express-default-fargate-and-alb", "ecs-faq-express-creates-all-resources", "ecs-faq-express-alb-shared-up-to-25-services", "ecs-change-express-mode-launch-2025-11"], None),
 "d19-050": ("found", ["ecs-anywhere-faq-what-it-is", "ecs-anywhere-external-instances-outbound-workloads", "ecs-anywhere-external-launch-type", "ecs-anywhere-faq-no-local-control-plane", "ecs-anywhere-iam-role-ecsanywhererole-once-per-account", "ecs-anywhere-ssm-credentials-refresh-on-reconnect", "ecs-anywhere-faq-activation-key-registers-up-to-1000"], None),
 "d19-051": ("found", ["ecs-anywhere-no-load-balancing", "ecs-anywhere-no-service-discovery", "ecs-anywhere-network-modes-no-awsvpc", "ecs-anywhere-no-capacity-providers-no-efs", "ecs-anywhere-one-cluster-at-a-time-iam-role", "ecs-anywhere-windows-support-deprecated"], None),
 "d19-052": ("found", ["ecs-anywhere-faq-needs-stable-internet-not-air-gapped", "ecs-anywhere-faq-disconnected-tasks-keep-running", "ecs-anywhere-faq-no-scaling-while-disconnected", "ecs-anywhere-faq-task-role-credentials-6-hours", "ecs-anywhere-faq-link-encrypted-with-tls"], None),
 "d19-054": ("found", ["eks-fully-managed-kubernetes-service", "eks-certified-kubernetes-conformant", "eks-faq-managed-kubernetes-no-control-plane-to-run", "eks-faq-runs-open-source-kubernetes-compatible", "eks-managed-control-plane-across-azs"], None),
 "d19-055": ("found", ["eks-control-plane-three-azs-api-etcd", "eks-control-plane-auto-replace-and-scale", "eks-control-plane-dedicated-per-cluster", "eks-faq-control-plane-multi-az-and-self-healing", "eks-managed-control-plane-across-azs"], None),
 "d19-056": ("partial", ["eks-pod-smallest-deployable-unit", "eks-deployment-replicaset-stateless", "eks-kubernetes-node-machine-runs-containers", "eks-daemonset-runs-on-every-node", "eks-namespace-groups-pods-of-an-application", "eks-kubectl-talks-to-control-plane", "eks-stateless-application-no-session-data-deployment"], "register-19: added the Pod and Deployment definitions from kubernetes-concepts. Kubernetes Service: the sentence sits in a bold list item with link targets that check M3 refuses; no fact."),
 "d19-057": ("found", ["eks-compute-options-pod-scheduling", "eks-compute-compare-who-manages-ec2-instances", "eks-compute-compare-who-patches-node-os", "eks-compute-compare-ssh-into-node", "eks-compute-compare-windows-containers", "eks-compute-compare-security-groups-per-pod", "eks-nodes-same-vpc-as-cluster-subnets", "eks-self-managed-nodes-in-your-account-billed-ec2"], None),
 "d19-058": ("found", ["eks-managed-node-group-automates-ec2-lifecycle", "eks-managed-node-group-asg-in-your-account", "eks-managed-node-group-on-demand-or-spot", "eks-managed-node-group-default-on-demand", "eks-managed-node-group-ami-shared-responsibility", "eks-managed-node-group-no-extra-charge", "eks-managed-node-group-no-outposts-wavelength", "eks-managed-node-group-private-subnet-reach-ecr", "eks-faq-update-managed-nodes-single-command", "eks-change-warm-pools-managed-node-groups-2026-04"], None),
 "d19-060": ("found", ["eks-auto-mode-aws-manages-infrastructure", "eks-auto-mode-karpenter-scaling", "eks-auto-mode-integrates-load-balancing-storage", "eks-auto-mode-node-lifetime-immutable-no-ssh", "eks-auto-mode-node-max-lifetime-21-days", "eks-faq-auto-mode-fully-automates-cluster-management", "eks-pricing-auto-mode-per-instance-duration-and-type", "eks-pricing-auto-mode-per-second-one-minute"], None),
 "d19-062": ("found", ["eks-fargate-profile-selects-pods", "eks-fargate-pods-not-matching-profile-pending", "eks-fargate-profile-immutable", "eks-fargate-pod-execution-role-required", "eks-fargate-pod-own-compute-boundary", "eks-fargate-private-subnets-only", "fargate-eks-pod-default-size-quarter-vcpu", "fargate-eks-pod-size-largest-16-vcpu"], None),
 "d19-063": ("found", ["eks-fargate-no-daemonsets", "eks-fargate-no-privileged-containers", "eks-fargate-no-gpu", "eks-fargate-no-hostport-hostnetwork", "eks-fargate-no-ebs-volumes", "eks-fargate-no-spot", "eks-fargate-not-on-outposts-wavelength-local-zones", "eks-fargate-imds-unavailable-use-irsa", "eks-fargate-load-balancer-ip-targets-only", "eks-fargate-efs-static-provisioning-only", "eks-ebs-csi-fargate-limits"], None),
 "d19-064": ("found", ["eks-karpenter-right-sized-compute", "eks-karpenter-customer-managed-no-sla", "eks-cluster-autoscaler-uses-auto-scaling-groups", "eks-auto-mode-karpenter-scaling"], None),
 "d19-065": ("found", ["eks-hpa-scales-pod-count-on-cpu", "eks-vpa-adjusts-cpu-memory-reservations", "eks-metrics-server-not-default-not-for-monitoring"], None),
 "d19-066": ("found", ["eks-metrics-server-not-default-not-for-monitoring"], None),
 "d19-067": ("found", ["eks-vpc-cni-pods-get-vpc-ip-addresses", "eks-vpc-cni-not-for-hybrid-nodes", "eks-security-groups-for-pods", "eks-compute-compare-security-groups-per-pod"], "Subnet IP address planning is not stated as such; the CNI fact says each Pod gets a VPC address."),
 "d19-068": ("found", ["eks-load-balancer-controller-creates-alb-for-ingress-nlb-for-service", "eks-fargate-load-balancer-ip-targets-only", "eks-auto-mode-integrates-load-balancing-storage"], None),
 "d19-069": ("found", ["eks-api-endpoint-public-by-default", "eks-api-endpoint-private-access-options", "eks-private-cluster-requirements", "eks-public-endpoint-cidr-ranges-per-cluster-limit"], None),
 "d19-070": ("found", ["eks-pod-identity-recommended-over-irsa", "eks-pod-identity-role-to-service-account", "eks-pod-identity-credential-isolation-imds", "eks-irsa-role-to-service-account", "eks-change-pod-identities-2023-11", "eks-fargate-imds-unavailable-use-irsa"], "register-19: service-accounts page says AWS recommends EKS Pod Identities whenever possible (eks-pod-identity-recommended-over-irsa)."),
 "d19-071": ("found", ["eks-access-entries-best-way-kubernetes-api-access", "eks-access-entries-recommended-over-aws-auth", "eks-cluster-iam-role-required", "eks-node-iam-role-required-before-launch", "eks-change-access-entries-2023-12", "eks-access-entries-per-cluster-limit"], "register-19: fetched create-node-role; the node IAM role fact is eks-node-iam-role-required-before-launch."),
 "d19-072": ("found", ["eks-ebs-csi-fargate-limits", "eks-efs-csi-shared-file-storage-windows-hybrid", "eks-fargate-efs-static-provisioning-only", "eks-fargate-no-ebs-volumes"], "That an EBS volume lives in one Availability Zone is an EBS fact (chapter 22); not restated here."),
 "d19-075": ("found", ["eks-addons-curated-managed-software", "eks-faq-add-ons-one-click-install", "eks-faq-add-ons-manage-operational-software", "eks-faq-capabilities-run-managed-by-aws-not-on-cluster"], None),
 "d19-076": ("found", ["eks-hybrid-nodes-on-premises-control-plane-aws", "eks-hybrid-nodes-need-reliable-connection", "eks-hybrid-nodes-network-connectivity-options", "eks-hybrid-nodes-not-on-cloud-infrastructure", "eks-hybrid-nodes-pricing-vcpu-hour", "eks-vpc-cni-not-for-hybrid-nodes", "eks-change-hybrid-nodes-launch-2024-12", "eks-faq-hybrid-nodes-gateway-automates-pod-networking"], None),
 "d19-077": ("found", ["eks-outposts-extended-vs-local-clusters", "eks-outposts-extended-cluster-needs-reliable-network", "eks-outposts-local-cluster-survives-disconnect", "eks-faq-outposts-local-clusters", "eks-faq-outposts-nodes-on-42u-racks", "eks-deployment-options-control-plane-location-hybrid-outposts"], None),
 "d19-078": ("found", ["eks-connector-view-only-conformant-clusters", "eks-faq-connector-view-only-no-management", "eks-faq-connector-no-charge"], None),
 "d19-079": ("found", ["eks-zonal-shift-temporary-move-traffic-from-impaired-az"], None),
 "d19-081": ("found", ["eks-anywhere-faq-customer-managed-product", "eks-anywhere-faq-uses-eks-distro", "eks-anywhere-faq-built-on-cluster-api-infrastructure", "eks-anywhere-faq-bottlerocket-default-node-os", "eks-anywhere-faq-aws-does-not-manage-clusters-or-capacity", "eks-anywhere-deployment-options-control-plane-customer-managed", "eks-anywhere-faq-not-supported-on-aws-cloud", "eks-anywhere-faq-not-supported-on-outposts"], None),
 "d19-082": ("found", ["eks-anywhere-faq-connected-or-air-gapped", "eks-faq-anywhere-for-isolated-or-air-gapped"], None),
 "d19-084": ("found", ["eks-distro-faq-same-kubernetes-as-eks-run-it-yourself", "eks-distro-faq-clusters-on-ec2-on-premises-other-clouds", "eks-distro-faq-same-versions-as-eks", "eks-distro-faq-you-set-up-servers-and-networking", "eks-distro-faq-does-not-include-iam-authenticator-or-plugins", "eks-distro-faq-release-channels-github-s3-ecr", "eks-distro-faq-support-best-effort", "eks-distro-extended-maintenance-up-to-14-months"], None),
 "d19-085": ("found", ["eks-deployment-options-hybrid-outposts-control-plane-aws-managed", "eks-deployment-options-control-plane-location-hybrid-outposts", "eks-deployment-options-data-plane-hybrid-outposts", "eks-anywhere-deployment-options-control-plane-customer-managed", "eks-faq-hybrid-nodes-vs-anywhere-connected-vs-air-gapped", "eks-faq-outposts-managed-vs-hybrid-nodes-managed", "ecs-anywhere-faq-needs-stable-internet-not-air-gapped", "eks-hybrid-nodes-need-reliable-connection"], None),
 "d19-086": ("found", ["ecr-managed-container-image-registry", "ecr-private-repositories-iam-resource-based-permissions", "ecr-faq-private-vs-public-repository", "ecr-faq-oci-compatible", "ecr-faq-public-gallery-anyone-can-download", "ecr-faq-integrated-with-ecs-eks-lambda"], None),
 "d19-087": ("found", ["ecr-default-private-registry-per-account", "ecr-repository-logical-collection-of-images", "ecr-docker-cli-needs-token-get-login-password", "ecr-authorization-token-permission-scope", "ecr-credential-helper-no-mfa", "ecr-get-authorization-token-requires-iam-policy", "ecr-eks-image-name-full-registry-repository-tag"], None),
 "d19-089": ("found", ["ecr-repository-policy-default-account-only", "ecr-repository-policy-vs-iam-policy-evaluation", "ecr-registry-policy-private-registry-level", "ecr-faq-resource-based-policies-for-access", "ecr-faq-cross-account-image-sharing-by-policy", "ecr-get-authorization-token-requires-iam-policy", "ecr-ecs-agent-pull-permissions"], None),
 "d19-090": ("found", ["ecr-tag-immutability-prevent-overwrite"], "The exclusion date (2025-07) was not mined as a change fact."),
 "d19-091": ("found", ["ecr-scanning-basic-vs-enhanced", "ecr-scan-on-push-each-new-image", "ecr-basic-scanning-aws-native-more-than-50-feeds", "ecr-basic-scan-once-per-24-hours", "ecr-basic-scan-100000-images-per-24-hours", "ecr-enhanced-scanning-no-manual-scans", "ecr-enhanced-scanning-inspector-cost", "ecr-faq-basic-scan-and-inspector-enhanced-scan"], None),
 "d19-093": ("found", ["ecr-lifecycle-policy-expires-images-within-24-hours", "ecr-lifecycle-count-more-than-and-since-pushed", "ecr-lifecycle-tag-pattern-or-prefix-not-both", "ecr-rules-per-lifecycle-policy-limit", "ecr-lifecycle-policy-length-limit"], None),
 "d19-094": ("found", ["ecr-replication-cross-region-cross-account", "ecr-replication-only-new-pushes", "ecr-replication-destination-account-policy-only", "ecr-faq-replicates-across-regions-and-accounts", "ecr-replication-most-images-under-30-minutes"], None),
 "d19-096": ("found", ["ecr-pull-through-cache-keeps-cache-current", "ecr-pull-through-cache-upstream-registries-auth", "ecr-pull-through-cache-revalidation-24-hours", "ecr-pull-through-cache-rules-per-registry-limit", "ecr-change-private-registry-pull-through-cache-2025-03", "ecr-change-ecr-to-ecr-pull-through-cache-2025-03"], None),
 "d19-097": ("found", ["ecr-encryption-default-sse-s3-aes256", "ecr-encryption-kms-options-per-repository", "ecr-encryption-settings-cannot-change-after-creation", "ecr-dsse-kms-only-govcloud", "ecr-faq-encrypted-at-rest-and-in-transit"], "register-19: the image-tag-mutability page says the encryption settings can't be changed once the repository is created (ecr-encryption-settings-cannot-change-after-creation)."),
 "d19-098": ("found", ["ecr-vpc-endpoints-fargate-need-ecr-and-s3", "ecr-privatelink-no-internet-gateway-needed", "ecr-vpc-endpoint-security-group-port-443", "ecr-faq-privatelink-pull-without-public-internet"], None),
 "d19-100": ("found", ["ecr-archive-storage-class-rarely-accessed", "ecr-archived-image-restore-within-20-minutes", "ecr-change-archive-storage-class-2025-11"], None),
 "d19-102": ("found", ["ecs-app2container-modernizes-java-dotnet-into-containers", "ecs-app2container-no-longer-open-to-new-customers"], None),
 "d19-103": ("found", ["ecr-migrate-one-time-copy-no-auto-update", "ecr-pull-through-cache-keeps-cache-current"], None),
 "d19-104": ("found", ["ecs-app2container-modernizes-java-dotnet-into-containers", "ecs-whitepaper-no-control-plane-ec2-easy-lift", "eks-whitepaper-natural-migration-path-for-kubernetes", "eks-faq-migrate-standard-kubernetes-without-code-changes", "ecs-containers-consistency-portability-benefits"], None),
 "d19-105": ("found", ["fargate-guide-containers-run-indefinitely-no-hard-limit", "fargate-guide-ideal-long-running-microservices-batch", "fargate-guide-lambda-short-lived-15-minutes", "fargate-guide-lambda-stateless-state-external", "fargate-guide-not-natively-event-driven", "fargate-guide-pricing-per-second-pay-for-what-you-provision", "fargate-vs-lambda-lambda-best-for-event-driven", "fargate-vs-lambda-shared-serverless-benefits", "fargate-guide-lambda-mi-for-steady-state", "ecs-faq-vs-lambda"], None),
 "d19-106": ("found", ["ecs-decision-guide-ecs-more-control-eks-flexibility", "ecs-decision-guide-serverless-or-kubernetes-operating-model", "ecs-decision-guide-portability-and-managed-overhead", "ecs-decision-guide-layers-capacity-orchestration-vertical", "eks-decision-guide-kubernetes-skills-sre-teams", "ecs-whitepaper-no-control-plane-ec2-easy-lift", "eks-whitepaper-natural-migration-path-for-kubernetes"], None),
 "d19-107": ("found", ["ecs-faq-fargate-no-ec2-management", "ecs-faq-ec2-for-greater-control", "ecs-ec2-capacity-large-workloads-price-optimized", "ecs-faq-ec2-root-access-to-os", "fargate-faq-need-ec2-control-use-without-fargate", "fargate-faq-gpu-not-supported", "ecs-cluster-ec2-full-control-you-manage-instances", "ecs-containers-not-security-boundary-use-fargate-for-isolation"], None),
 "d19-108": ("found", ["ecs-whitepaper-batch-runs-on-fargate-or-ec2", "fargate-guide-ideal-long-running-microservices-batch"], "Spot for AWS Batch on EC2 is not stated on the saved pages."),
 "d19-109": ("found", ["ecs-one-task-definition-family-per-business-purpose", "ecs-task-definition-revision-maps-to-app-version", "ecs-case-study-smartsheet-fargate-independent-deployments"], None),
 "d19-113": ("found", ["fargate-compute-savings-plans-cover-fargate-lambda", "fargate-faq-spot-and-compute-savings-plan-pricing", "eks-savings-plans-for-cluster-compute"], "That EC2 Instance Savings Plans do not cover Fargate is not quoted here; the Savings Plans chapter owns plan types."),
 "d19-114": ("found", ["ecs-task-size-load-test-for-requirements", "ecs-task-size-stateless-small-reservations-cost", "fargate-task-size-no-overhead-round-up", "ecs-scaling-target-headroom-60-80-percent"], None),
 "d19-115": ("found", ["ecs-faq-ec2-split-cost-allocation-opt-in", "ecs-faq-fargate-cost-in-cur-automatically", "ecs-faq-container-insights-ec2-and-fargate", "eks-cost-monitoring-split-cost-allocation"], None),
 "d19-116": ("found", ["ecs-spot-instance-draining-off-by-default", "ecs-draining-instance-no-new-tasks"], None),
 "d19-138": ("partial", ["fargate-serverless-pay-as-you-go", "fargate-retirement-no-opt-out", "ecs-one-task-definition-family-per-business-purpose", "ecs-whitepaper-no-control-plane-ec2-easy-lift", "ecs-faq-fargate-no-ec2-management", "ecs-decision-guide-ecs-more-control-eks-flexibility"], "No decision-guide sentence calls ECS simpler; use the grounded reasons listed (no control plane to manage, Fargate the easiest way to run containers, no instances to patch)."),
 "d19-139": ("not-found", ["ecs-ec2-capacity-large-workloads-price-optimized", "fargate-guide-pricing-per-second-pay-for-what-you-provision", "fargate-no-host-access-ecs-exec"], "No AWS sentence compares Fargate unit price with EC2 (register-19 searched 'more expensive', 'higher cost', 'cost more' near Fargate over all scopes). Writer: state the trade-off as less control of the host and paying for provisioned task size; never say Fargate costs more."),
 "d19-140": ("found", ["eks-decision-guide-kubernetes-skills-sre-teams", "ecs-decision-guide-ecs-more-control-eks-flexibility", "eks-whitepaper-natural-migration-path-for-kubernetes", "eks-faq-runs-open-source-kubernetes-compatible", "ecs-whitepaper-no-control-plane-ec2-easy-lift"], None),
 "d19-141": ("found", ["ecs-replica-strategy-default-spreads-azs", "ecs-placement-strategy-default-for-services-spread-az", "fargate-no-placement-strategies-best-effort-az-spread", "ecs-az-rebalancing-best-effort-spread", "ecs-az-rebalancing-enabled-for-eligible-services", "ecs-production-multi-az-lose-an-az", "ecs-overprovision-for-az-failure-two-or-three-azs"], None),
 "d19-142": ("found", ["ecs-case-study-smartsheet-fargate-independent-deployments", "ecs-case-study-old-mutual-fargate-no-idle-servers"], None),
 "d19-143": ("found", ["eks-case-study-miro-managed-eks-cut-compute-cost"], None)
}
for did, (st, ids, note) in R.items():
    put(did, st, ids, note, force=True)

# registrar notes on items mapped by the numbers and faq miners
EXTRA = {
 "d19-024": "register-19: no single sentence says ECS and EKS share the Fargate vCPU quota; the same quota row appears on both quota pages (fargate-ondemand-vcpu-quota, fargate-ondemand-vcpu-quota-eks-page).",
 "d19-092": "register-19: the 2024-08-06 GA date is in the What's New feed only; the post is blocked by robots.txt (fetch refused), so no fact.",
 "d19-132": "register-19: added eks-savings-plans-for-cluster-compute (what-is-eks: savings plans apply to compute used in EKS clusters). The Auto Mode specific answer stays in a FAQ table cell that check M4 refuses.",
 "d19-053": "ECS Anywhere billing minimum: the ECS pricing table says 1 hour minimum, the ECS Anywhere pricing page says 1 minute; the dedicated page wins and no minimum is stated as a fact."
}
for did, note in EXTRA.items():
    put(did, got.get(did, {}).get("status") or "partial", [], note)
put("d19-132", "partial", ["eks-savings-plans-for-cluster-compute"])

missing = []
for d in brief["demand"]:
    g = got.get(d["id"])
    if g is None:
        missing.append(d["id"])
        continue
    ids = []
    for i in g["facts"]:
        j = live(i)
        if j is None:
            print("dropped (unknown or rejected):", d["id"], i)
            continue
        if j not in ids:
            ids.append(j)
    d["status"] = g["status"] if (ids or g["status"] == "not-found") else "not-found"
    d["facts"] = ids
    if g["notes"]:
        d["note"] = " | ".join(g["notes"])
    d["registered_by"] = "register-19"
json.dump(brief, open(W + "brief.v0.json", "w"), indent=1, ensure_ascii=False)
print(collections.Counter(d["status"] for d in brief["demand"]))
print("missing", missing)
print([(d["id"], d["status"]) for d in brief["demand"] if d["status"] != "found"])
