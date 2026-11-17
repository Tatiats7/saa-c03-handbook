"""register-25: build reg-decisions.json, reg-patches/<id>.json and reg-patch-ids.json.

Every change is applied later through `saa.py facts amend` by reg_apply.py. This script only writes inputs and
pre-checks displays (verbatim in quote or claim, at most 8 words without a digit, unique in the fact).
"""
import json, os, re, sys
W = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(W, '..', '..', '..')
facts = {}
for s in ['storage-gateway', 'datasync', 'snow-family', 'transfer-family']:
    for line in open(os.path.join(B, 'data', 'facts', s + '.jsonl')):
        if line.strip():
            f = json.loads(line)
            facts[f['id']] = f

SUP = [
 ("datasync-bandwidth-change-takes-effect-within-60-seconds", "datasync-bandwidth-limit-change-takes-effect-within-60-seconds", "duplicate: same configure-bandwidth sentence; the kept fact states the running-or-queued scope"),
 ("datasync-faq-basic-mode-quotas-slower", "datasync-basic-mode-slower-than-enhanced-and-subject-to-quotas", "duplicate: the user guide sentence says the same as the FAQ sentence"),
 ("datasync-faq-agent-hypervisors", "datasync-agent-runs-on-hypervisors-or-ec2", "duplicate: the user guide sentence names the same hypervisors and adds the EC2 agent"),
 ("datasync-faq-what-is-online-data-movement", "datasync-definition-online-data-movement-service", "duplicate: same one-sentence definition (FAQ and features page)"),
 ("datasync-faq-ideal-online-migrations-active-data-replication", "datasync-faq-vs-transfer-family-datasync-for-storage-to-storage", "duplicate: the kept FAQ quote contains this sentence; display added there"),
 ("datasync-pricing-additional-aws-service-charges", "datasync-pricing-aws-services-request-storage-transfer-rates", "duplicate: same pricing sentence"),
 ("datasync-pricing-data-transfer-out-between-regions", "datasync-pricing-aws-to-on-premises-pays-data-transfer-out", "duplicate: same pricing sentences"),
 ("datasync-pricing-per-gb-plus-per-execution-enhanced", "datasync-pricing-per-gb-fee-and-enhanced-task-execution-fee", "duplicate: the kept quote contains these sentences"),
 ("datasync-pricing-no-upfront-no-minimum", "datasync-pricing-per-gb-fee-and-enhanced-task-execution-fee", "duplicate: the kept quote contains this sentence; display added there"),
 ("datasync-faq-scale-out-partition-with-multiple-tasks", "datasync-large-migration-partition-with-multiple-tasks", "duplicate: the user guide sentence says the same as the FAQ sentence"),
 ("datasync-pricing-s3-request-charges", "datasync-pricing-s3-requests-list-head-get-put-copy", "duplicate: the kept quote contains this sentence and the configuration condition"),
 ("datasync-pricing-multipart-uploads-incomplete-storage-charges", "datasync-s3-multipart-upload-incomplete-storage-charges", "duplicate: same multipart-upload sentences"),
 ("datasync-faq-single-task-fills-10-gbps", "datasync-single-task-can-use-10-gbps-link", "duplicate: the kept quote contains this FAQ sentence"),
 ("datasync-task-schedule-minimum-interval-1-hour", "datasync-schedule-minimum-interval-one-hour", "duplicate: same two task-scheduling sentences"),
 ("snow-family-dtt-enterprise-support-only", "snow-family-dtt-enterprise-support-customers-only", "duplicate: same sentence"),
 ("snow-family-dtt-network-requirement-100g-qsfp28-transceiver", "snow-family-dtt-requires-fiber-and-100g-transceiver-you-bring", "duplicate: the kept fact quotes the same transceiver sentence"),
 ("snow-family-faq-210-tb-per-storage-optimized-device", "snow-family-faq-data-per-job-210-tb-per-device", "duplicate: the kept FAQ quote contains this sentence"),
 ("snow-family-faq-data-in-no-transfer-fee-s3-pricing-applies", "snow-family-pricing-data-in-to-aws-no-transfer-fee", "duplicate: the kept FAQ quote contains this sentence"),
 ("snow-family-pricing-per-job-pay-as-you-go-not-for-purchase", "snow-family-faq-devices-pay-per-job-not-for-purchase", "duplicate: same FAQ sentence"),
 ("snow-family-job-must-complete-within-360-days", "snow-family-faq-job-must-complete-within-360-days", "duplicate: same FAQ sentences"),
 ("snow-family-job-provisioning-up-to-4-weeks", "snow-family-faq-provisioning-up-to-4-weeks", "duplicate: same FAQ provisioning sentence"),
 ("snow-family-default-shipping-two-day-ups", "snow-family-faq-shipping-default-two-day-ups-expedited-option", "duplicate: same FAQ sentences"),
 ("snow-family-faq-what-is-snowball-edge", "snow-family-snowball-edge-definition-device-storage-and-compute", "duplicate: same definition (FAQ and developer guide)"),
 ("snow-family-faq-opshub-gui-no-extra-charge", "snow-family-opshub-manages-devices-no-extra-cost", "duplicate: the developer guide fact covers OpsHub and its cost"),
 ("storage-gateway-faq-backup-volume-same-region-only", "storage-gateway-faq-aws-backup-same-region-only", "duplicate: same FAQ sentence"),
 ("storage-gateway-faq-deploy-locations", "storage-gateway-faq-deploy-targets", "duplicate: same FAQ sentences; displays and the hardware appliance condition moved to the kept fact"),
 ("storage-gateway-faq-ha-vmware-requirements", "storage-gateway-faq-ha-requires-vmware-ha-cluster-shared-storage", "duplicate: same FAQ sentence"),
 ("storage-gateway-faq-ha-vmware-no-extra-cost-no-data-loss", "storage-gateway-faq-ha-requires-vmware-ha-cluster-shared-storage", "duplicate: the kept fact quotes this sentence as its second evidence item"),
 ("storage-gateway-faq-local-cache-max-64-tib-on-vm", "storage-gateway-faq-max-local-cache-vm", "duplicate: same FAQ sentence"),
 ("storage-gateway-faq-s3-file-encryption-default-sse-s3-optional-kms", "storage-gateway-faq-s3-file-gateway-encryption-default-sse-s3-optional-kms", "duplicate: same FAQ sentences"),
 ("storage-gateway-pricing-file-gateway-storage-billed-by-s3", "storage-gateway-faq-billing-file-gateway-s3-storage-requests", "duplicate: same FAQ sentences"),
 ("storage-gateway-pricing-upload-transfer-free-download-billed", "storage-gateway-faq-billing-data-transfer-download-billed-upload-free", "duplicate: same FAQ sentences"),
 ("storage-gateway-faq-billing-volume-tape-used-capacity-only", "storage-gateway-pricing-volume-tape-billed-for-used-capacity", "duplicate: same FAQ sentences"),
 ("storage-gateway-faq-vpc-endpoint-billing-dimensions", "storage-gateway-pricing-vpc-endpoint-hourly-and-per-gb", "duplicate: same FAQ sentences"),
 ("storage-gateway-pricing-archived-tape-early-deletion", "storage-gateway-faq-tape-early-deletion-windows", "duplicate: same FAQ sentences"),
 ("storage-gateway-faq-vmware-ha-restart-downtime-60-seconds", "storage-gateway-faq-ha-vmware-restart-60-seconds", "duplicate: same FAQ sentences"),
 ("storage-gateway-faq-s3-file-multiple-readers-read-only-share", "storage-gateway-faq-s3-file-gateway-multiple-readers-read-only-share", "duplicate: the kept FAQ quote contains these sentences"),
 ("storage-gateway-faq-s3-file-refresh-cache-inventory", "storage-gateway-faq-s3-file-gateway-refresh-cache-methods", "duplicate: the kept FAQ quote contains this sentence"),
 ("storage-gateway-faq-s3-file-single-writer-recommended", "storage-gateway-faq-s3-file-gateway-single-writer-recommended", "duplicate: same FAQ sentences"),
 ("storage-gateway-faq-s3-file-storage-classes", "storage-gateway-faq-s3-file-gateway-storage-classes-supported", "duplicate: the kept FAQ quote contains this sentence"),
 ("storage-gateway-faq-s3-file-initial-class-lifecycle-glacier", "storage-gateway-faq-s3-file-gateway-storage-classes-supported", "duplicate: the kept FAQ quote contains this sentence"),
 ("storage-gateway-faq-s3-file-upload-notification-vs-s3-events", "storage-gateway-faq-s3-file-gateway-file-upload-notification-per-file", "duplicate: same FAQ sentences"),
 ("storage-gateway-faq-s3-file-gateway-vs-s3-api", "storage-gateway-faq-s3-file-gateway-use-vs-s3-api", "duplicate: same FAQ sentences"),
 ("storage-gateway-faq-tape-no-move-deep-archive-to-glacier", "storage-gateway-faq-tape-gateway-deep-archive-tape-cannot-move-to-glacier", "duplicate: same FAQ sentences"),
 ("storage-gateway-faq-tape-kms-key-fixed-after-creation", "storage-gateway-faq-tape-gateway-kms-key-fixed-after-creation", "duplicate: the kept FAQ quote contains this sentence"),
 ("storage-gateway-faq-tape-storage-classes", "storage-gateway-faq-tape-gateway-s3-classes-and-eject-archive", "duplicate: same FAQ sentences"),
 ("storage-gateway-faq-tape-no-s3-api-access", "storage-gateway-faq-tape-gateway-virtual-tapes-not-accessible-via-s3-api", "duplicate: same FAQ sentences"),
 ("storage-gateway-faq-tape-gateway-vtl-archive", "storage-gateway-faq-tape-gateway-vtl-components", "duplicate: same FAQ sentences; display added to the kept fact"),
 ("storage-gateway-faq-tape-worm-tape-type", "storage-gateway-faq-tape-gateway-worm-tape-type", "duplicate: the kept FAQ quote contains these sentences"),
 ("storage-gateway-faq-tape-retention-lock", "storage-gateway-faq-tape-gateway-worm-tape-type", "duplicate: the kept FAQ quote contains this sentence; display added there"),
 ("storage-gateway-faq-tape-vtl-capacity", "storage-gateway-faq-tape-library-1500-tapes-1-pb", "duplicate: same FAQ sentence"),
 ("storage-gateway-faq-tape-size-min-max", "storage-gateway-faq-tape-size-range", "duplicate: same FAQ sentence"),
 ("storage-gateway-faq-use-cases-four", "storage-gateway-faq-use-cases-four-hybrid", "duplicate: same FAQ sentence; display added to the kept fact"),
 ("storage-gateway-faq-volume-cached-mode", "storage-gateway-faq-volume-gateway-cached-mode-primary-in-s3", "duplicate: same FAQ sentence"),
 ("storage-gateway-faq-volume-gateway-iscsi-ebs-snapshots", "storage-gateway-faq-volume-gateway-block-iscsi-ebs-snapshots", "duplicate: same FAQ sentences"),
 ("storage-gateway-faq-volume-stored-mode", "storage-gateway-faq-volume-gateway-stored-mode-primary-on-premises", "duplicate: same FAQ sentence"),
 ("storage-gateway-faq-volume-data-not-visible-in-s3", "storage-gateway-faq-volume-gateway-volumes-in-service-managed-bucket", "duplicate: the kept FAQ quote contains these sentences"),
 ("storage-gateway-faq-volume-gateway-32-volumes-and-sizes", "storage-gateway-faq-volume-max-32-volumes", "duplicate: split into three scoped FAQ facts (32 volumes; cached 32 TB and 1 PB; stored 16 TB and 512 TB) that quote the same sentences"),
 ("storage-gateway-faq-volume-gateway-restore-cached-vs-stored-primary-location", "storage-gateway-faq-volume-snapshot-restore-cached-keeps-in-s3", "duplicate: same two FAQ sentences, kept as two scoped facts (cached: ...-cached-keeps-in-s3; stored: ...-stored-downloads)"),
 ("storage-gateway-faq-volume-snapshot-no-unmount", "storage-gateway-faq-volume-snapshot-no-unmount-needed", "duplicate: same FAQ sentences"),
 ("storage-gateway-faq-volume-snapshot-schedule-hours", "storage-gateway-faq-volume-snapshot-schedule-per-volume", "duplicate: same FAQ sentences"),
 ("storage-gateway-faq-vs-guide-no-glacier-instant-retrieval", "storage-gateway-s3-file-gateway-glacier-instant-retrieval-not-supported", "duplicate: same user guide sentence"),
 ("storage-gateway-faq-why-reduce-footprint", "storage-gateway-faq-why-reduce-on-premises-storage-footprint", "duplicate: same FAQ sentence"),
 ("storage-gateway-s3-file-gateway-versioning-multiple-object-versions", "storage-gateway-s3-file-versioning-adds-object-versions-cost", "duplicate: same sentence; the kept fact also quotes the 'increase S3 storage' sentence its claim needs"),
 ("transfer-family-pricing-billed-while-server-stopped", "transfer-family-faq-stopped-server-still-billed", "duplicate: the kept FAQ quote contains these sentences"),
 ("transfer-family-faq-billing-sftp-connectors-data-and-calls", "transfer-family-pricing-connectors-and-web-apps", "duplicate: the kept FAQ quote contains this sentence"),
 ("transfer-family-faq-billing-web-app-units", "transfer-family-pricing-connectors-and-web-apps", "duplicate: the kept FAQ quote contains this sentence"),
 ("transfer-family-faq-billing-hourly-per-protocol", "transfer-family-pricing-hourly-per-protocol-and-data", "duplicate: the kept FAQ quote contains this sentence"),
 ("transfer-family-faq-billing-data-as2-messages-decrypt", "transfer-family-pricing-hourly-per-protocol-and-data", "duplicate: the kept FAQ quote contains this sentence"),
]
REJECT = []

# display replacements {id: {key: new}} and additions {id: [(key, display)]}
REPL = {
 "storage-gateway-faq-billing-data-transfer-download-billed-upload-free": {"upload": "data transfer for uploading to AWS is free"},
 "storage-gateway-faq-s3-file-existing-bucket-objects": {"keys": "used to present the objects as files"},
 "storage-gateway-faq-s3-file-gateway-nfs-smb-objects": {"protocols": "file protocols such as Network File System (NFS)"},
 "storage-gateway-faq-s3-file-headers-scan-download-on-read": {"on-read": "downloaded only when the object is read"},
 "storage-gateway-faq-volume-billing-used-data-only": {"billing": "amount of data stored on the volume"},
 "storage-gateway-faq-volume-snapshot-restore-stored-downloads": {"stored-restore": "downloads the data contained within the snapshot"},
 "storage-gateway-faq-volume-snapshots-incremental": {"incremental": "only the data that has changed"},
 "storage-gateway-gateway-cache-recently-used-data": {"v2": "low-latency access to data that is stored durably"},
 "storage-gateway-gateway-upload-buffer-staging-area": {"v2": "uploads the data to a virtual tape"},
 "storage-gateway-s3-file-gateway-uploads-only-modified-data": {"v1": "uploads the new or modified data"},
 "storage-gateway-tape-gateway-stores-virtual-tapes-in-s3": {"v1": "virtual tapes in Amazon Simple Storage Service"},
 "datasync-decision-migration-guide-large-transfer-online-limits-and-direct-connect": {"v2": "dedicated private network connection"},
 "datasync-faq-agent-endpoint-choices": {"endpoints": "public internet facing endpoints"},
 "datasync-faq-agent-types-follow-task-mode": {"agent-types": "two types of agents"},
 "datasync-faq-agent-updates-automatic-when-idle": {"updates": "automatically applied by AWS"},
 "datasync-faq-archive-cold-data-to-glacier": {"archive": "move cold data from on-premises storage systems"},
 "datasync-faq-interrupted-task-next-run-completes": {"recovery": "will transfer missing files"},
 "datasync-faq-no-vpn-required": {"no-vpn": "no need to setup a VPN/tunnel"},
 "datasync-faq-other-clouds-agent-basic-vs-enhanced": {"enhanced": "no agent is required"},
 "datasync-faq-s3-glacier-instant-retrieval-source-higher-fee": {"fee": "higher retrieval fees"},
 "datasync-faq-s3-ia-source-retrieval-fee": {"fee": "retrieval fee based on the size"},
 "datasync-faq-s3-to-s3-copies-metadata-tags-not-acls-versions": {"not-copied": "does not copy other object information"},
 "datasync-faq-source-load-and-bandwidth-limit": {"limit": "Configuring a bandwidth limit for a task"},
 "datasync-faq-vpc-endpoints-privatelink-supported": {"privatelink": "VPC endpoints are supported"},
 "datasync-faq-vs-rsync-automates-large-active-datasets": {"automation": "fully automates and accelerates moving large active datasets"},
 "datasync-faq-vs-s3-replication-datasync-and-replication-use": {"replication": "Use S3 Replication for continuous replication"},
 "datasync-faq-vs-storage-gateway-migrate-then-file-gateway": {"pair": "File Gateway configuration of AWS Storage Gateway"},
 "snow-family-faq-notice-alternatives": {"alternatives": "AWS DataSync for online transfers"},
 "snow-family-faq-transfer-time-factors": {"factors": "local network speed, file size"},
 "snow-family-faq-use-when-disconnected-or-no-bandwidth": {"when": "when bandwidth is not available"},
 "snow-family-nfs-interface-for-import-jobs-if-configured-at-order": {"v2": "configured to include it"},
 "snow-family-restriction-same-region-and-no-po-box-shipping": {"region": "the AWS Region where the devices are ordered"},
 "transfer-family-change-custom-workflow-log-groups-2026-10": {"old": "execution logs to that server’s CloudWatch log group"},
 "transfer-family-change-source-ip-preservation-behind-nlb-2026-09": {"old": "replaced the client's source IP"},
 "transfer-family-faq-billing-same-for-one-or-many-endpoints": {"no-difference": "regardless of whether same endpoint is enabled"},
 "transfer-family-faq-custom-idp-lambda-or-api-gateway": {"options": "an AWS Lambda function"},
 "transfer-family-faq-existing-clients-keep-working": {"clients": "existing file transfer client application"},
 "transfer-family-faq-fixed-ip-vpc-endpoint-elastic-ips": {"elastic-ips": "attach Elastic IPs (including BYO IPs)"},
 "transfer-family-faq-ftp-internal-vpc-access-only": {"ftp": "VPC hosted endpoint’s internal access option"},
 "transfer-family-faq-one-home-bucket-per-user": {"home": "a single bucket as the home directory"},
 "transfer-family-faq-service-managed-no-stored-passwords": {"no-passwords": "Storing passwords within the service"},
 "transfer-family-faq-sftp-connectors-copy-with-remote-sftp-servers": {"connectors": "copy files at scale"},
 "transfer-family-faq-sftp-connectors-static-ip-service-managed-default": {"static-ip": "Egress Type as Service Managed"},
 "transfer-family-faq-sftp-connectors-vpc-lattice-private-servers": {"lattice": "route SFTP connections to the remote server"},
 "transfer-family-pricing-hourly-per-protocol-and-data": {"protocol": "hourly basis for each of the protocols enabled"},
}
ADD = {
 "storage-gateway-faq-billing-data-transfer-download-billed-upload-free": [("download", "each GB downloaded from AWS to your gateway")],
 "storage-gateway-faq-s3-file-gateway-nfs-smb-objects": [("smb", "Server Message Block (SMB)")],
 "storage-gateway-faq-volume-billing-used-data-only": [("not-size", "not the size of the volume you create")],
 "storage-gateway-s3-file-gateway-uploads-only-modified-data": [("v3", "instead of uploading the whole file")],
 "datasync-faq-agent-endpoint-choices": [("fips", "Federal Information Processing Standards (FIPS) validated endpoints"), ("vpc", "endpoints within one of your VPCs")],
 "datasync-faq-agent-types-follow-task-mode": [("basic", "use the DataSync Basic mode agent")],
 "datasync-faq-agent-updates-automatic-when-idle": [("idle", "applied non-disruptively when the agent is idle")],
 "datasync-faq-interrupted-task-next-run-completes": [("consistent", "data will be complete and consistent")],
 "datasync-faq-no-vpn-required": [("ports", "standard network ports")],
 "datasync-faq-other-clouds-agent-basic-vs-enhanced": [("basic", "deploy the DataSync agent in your cloud environment")],
 "datasync-faq-s3-to-s3-copies-metadata-tags-not-acls-versions": [("copied", "object metadata and tags")],
 "datasync-faq-vpc-endpoints-privatelink-supported": [("no-internet", "doesn't traverse the public internet")],
 "datasync-faq-vs-s3-replication-datasync-and-replication-use": [("datasync", "data pipelines, and data lake ingest")],
 "datasync-faq-vs-storage-gateway-migrate-then-file-gateway": [("migrate", "migrate existing data to Amazon S3")],
 "snow-family-faq-notice-alternatives": [("dtt", "AWS Data Transfer Terminal for secure physical transfers")],
 "snow-family-faq-transfer-time-factors": [("shipping", "shipping the devices to and from your location")],
 "snow-family-faq-use-when-disconnected-or-no-bandwidth": [("edge", "rugged, austere, mobile, or disconnected")],
 "snow-family-restriction-same-region-and-no-po-box-shipping": [("po-box", "to a post office box")],
 "transfer-family-faq-custom-idp-lambda-or-api-gateway": [("apigw", "an Amazon API Gateway endpoint")],
 "transfer-family-faq-existing-clients-keep-working": [("condition", "as long as you have enabled your endpoint")],
 "transfer-family-faq-fixed-ip-vpc-endpoint-elastic-ips": [("option", "choosing the internet-facing option")],
 "transfer-family-faq-service-managed-no-stored-passwords": [("status", "currently not supported")],
 "transfer-family-faq-sftp-connectors-copy-with-remote-sftp-servers": [("between", "between remote SFTP servers and AWS storage services")],
 "transfer-family-faq-sftp-connectors-static-ip-service-managed-default": [("allow-list", "allow-list connections on your business partner’s firewall")],
 "transfer-family-faq-sftp-connectors-vpc-lattice-private-servers": [("private", "privately hosted servers")],
 "transfer-family-pricing-hourly-per-protocol-and-data": [("data", "amount of data uploaded and downloaded"), ("as2", "number of messages exchanged over AS2")],
 # merges: displays carried over from superseded duplicates
 "datasync-faq-vs-transfer-family-datasync-for-storage-to-storage": [("ideal", "online migrations for active data sets")],
 "datasync-pricing-per-gb-fee-and-enhanced-task-execution-fee": [("v3", "no upfront costs and no minimum charges")],
 "storage-gateway-faq-deploy-targets": [("vmc", "VMware Cloud on AWS"), ("ec2", "as an AMI in Amazon EC2")],
 "storage-gateway-faq-tape-gateway-vtl-components": [("v3", "iSCSI virtual tape library (VTL) interface")],
 "storage-gateway-faq-tape-gateway-worm-tape-type": [("v3", "Tape Retention Lock")],
 "storage-gateway-faq-use-cases-four-hybrid": [("v4", "four key hybrid cloud use cases")],
 "storage-gateway-pricing-volume-tape-billed-for-used-capacity": [("prorated", "prorated daily")],
 "storage-gateway-s3-file-versioning-adds-object-versions-cost": [("storage", "increase S3 storage")],
 "transfer-family-pricing-connectors-and-web-apps": [("data", "amount of data transferred")],
}
EXTRA = {
 "storage-gateway-faq-deploy-targets": {"volatility": "frequently-changing", "tier0": True,
     "qualifiers_condition": "the Storage Gateway Hardware Appliance is no longer offered to new customers (storage-gateway-hardware-appliance-end-of-availability)"},
 "transfer-family-faq-global-accelerator-for-remote-users": {"claim": "You can use AWS Global Accelerator with a Transfer Family server endpoint to improve file transfer throughput and round-trip time."},
 "datasync-bandwidth-limit-change-takes-effect-within-60-seconds": {"exam_relevance": "extended"},
 "storage-gateway-s3-file-gateway-glacier-instant-retrieval-not-supported": {"exam_relevance": "core"},
 "snow-family-pricing-data-in-to-aws-no-transfer-fee": {"tier0": True},
}


def norm(s):
    s = re.sub(r'\]\([^)]*\)', ']', s).replace('[', '').replace(']', '').replace('*', '')
    return re.sub(r'\s+', ' ', s).strip().lower()


errs = []
patches = {}
sup_old = {o for o, n, w in SUP}
for o, n, w in SUP:
    if o not in facts or n not in facts:
        errs.append('missing in SUP %s %s' % (o, n))
    elif n in sup_old:
        errs.append('chain %s -> %s' % (o, n))
for i in sorted(set(REPL) | set(ADD) | set(EXTRA)):
    if i not in facts:
        errs.append('missing %s' % i)
        continue
    if i in sup_old:
        errs.append('patching superseded %s' % i)
    f = facts[i]
    p = {}
    if i in REPL or i in ADD:
        vals = [dict(v) for v in f['values']]
        keys = {v['key'] for v in vals}
        for k, d in REPL.get(i, {}).items():
            if k not in keys:
                errs.append('%s no key %s' % (i, k))
            for v in vals:
                if v['key'] == k:
                    v['display'] = d
        for k, d in ADD.get(i, []):
            if k in keys:
                errs.append('%s dup key %s' % (i, k))
            vals.append({'key': k, 'display': d})
            keys.add(k)
        claim = EXTRA.get(i, {}).get('claim', f['claim'])
        hay = [norm(claim)] + [norm(e['quote']) for e in f['evidence']]
        seen = set()
        for v in vals:
            d = v['display']
            if not any(norm(d) in h for h in hay):
                errs.append('%s display not held: %s' % (i, d))
            if not re.search(r'\d', d) and len(d.split()) > 8:
                errs.append('%s display too long: %s' % (i, d))
            if d in seen:
                errs.append('%s display dup: %s' % (i, d))
            seen.add(d)
        p['values'] = vals
    ex = EXTRA.get(i, {})
    for k in ('claim', 'volatility', 'tier0', 'exam_relevance'):
        if k in ex:
            p[k] = ex[k]
    if 'qualifiers_condition' in ex:
        q = dict(f['qualifiers'])
        q['condition'] = ex['qualifiers_condition']
        p['qualifiers'] = q
    patches[i] = p
os.makedirs(os.path.join(W, 'reg-patches'), exist_ok=True)
for i, p in patches.items():
    json.dump(p, open(os.path.join(W, 'reg-patches', i + '.json'), 'w'), indent=1, ensure_ascii=False)
json.dump(sorted(patches), open(os.path.join(W, 'reg-patch-ids.json'), 'w'), indent=1)
json.dump({'supersede': SUP, 'reject': REJECT}, open(os.path.join(W, 'reg-decisions.json'), 'w'), indent=1, ensure_ascii=False)
print('patches', len(patches), 'supersede', len(SUP), 'errors', len(errs))
for e in errs:
    print('ERR', e)
