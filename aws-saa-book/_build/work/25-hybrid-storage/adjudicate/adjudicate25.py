"""adjudicate-25: one repair or rejection per disputed fact of chapter 25.

Usage: python3 adjudicate25.py [--dry-run] [--only ID,ID]
Writes patches/<id>.json and appends results to amend-log.jsonl.
"""
import json, os, subprocess, sys

ROOT = '/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/'
BOOK = ROOT + 'aws-saa-book/'
HERE = BOOK + '_build/work/25-hybrid-storage/adjudicate/'
BY = 'adjudicate-25'

DT_DS = 'AWS DataSync increases scalability and performance for on-premises file transfers'
SNOW_EOS = 'On December 31, 2026, AWS will discontinue support for AWS Snowball devices in all AWS commercial Regions.'
GUIDE_EOS = 'AWS will discontinue support for AWS Snowball devices in all AWS commercial Regions on December 31, 2026. This does not affect AWS GovCloud (US) customers with active Snow jobs.'
NFS_AVAIL = 'The NFS interface is available for import jobs.'
SNOW_HIST_ROW = '| [File interface deprecated](#doc-history) | The file interface is no longer available for data transfer. | March 1, 2024 |'
HIST_HDR = '| Change | Description | Date |'
DC_LEAD = '**Direct Connect** - With [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html), you can create a dedicated connection between your storage network and AWS. From a DataSync perspective, this lets you:'


def ev(source_id, quote, table_header=None, heading=None):
    d = {'source_id': source_id, 'quote': quote, 'table_header': table_header}
    if heading:
        d['heading'] = heading
    return d


def cond_drop(note):
    return {'qual': {'condition': ''}, 'note_add': note}


D = {}

# ---------------- DataSync ----------------
D['datasync-bandwidth-limit-change-takes-effect-within-60-seconds'] = {
    'reason': 'entail partial: the quote stands under the console steps; claim narrowed to a change saved in the console.',
    'claim': 'When you change the bandwidth limit of a DataSync task execution in the DataSync console and save the changes, the new bandwidth limit takes effect within 60 seconds.',
    'qual': {'scope': 'bandwidth limit change for a task execution, saved in the DataSync console', 'condition': ''},
}
D['datasync-can-delete-destination-files-not-in-source'] = dict(
    reason='entail partial: the condition stands only in the table below the quote; condition moved to the note.',
    **cond_drop('adjudicate-25: the table of the page adds that this option cannot be combined with transferring all data (not in the quote).'))
D['datasync-change-enhanced-mode-on-premises-to-s3-2025-12'] = {
    'reason': 'entail partial: added the NFS or SMB sentence and the Posted on line as evidence; Regions condition removed.',
    'qual': {'scope': 'DataSync Enhanced mode, on-premises NFS or SMB file servers to Amazon S3', 'condition': ''},
    'evidence': [0, 1,
                 ev('www/about-aws/whats-new/2025/12/aws-datasync-scalability-performance-on-premises-file-transfers',
                    'This launch extends the capabilities of Enhanced mode to support transfers between on-premises NFS or SMB file servers, and Amazon S3.'),
                 ev('www/about-aws/whats-new/2025/12/aws-datasync-scalability-performance-on-premises-file-transfers',
                    'Posted on: Dec 12, 2025', heading=DT_DS)],
}
D['datasync-change-enhanced-mode-other-clouds-without-agent-2025-05'] = dict(
    reason='entail partial: the all-Regions condition is not in the quotes; removed.',
    **cond_drop('adjudicate-25: the post adds availability in all AWS Regions where DataSync is offered (not quoted).'))
D['datasync-change-kerberos-for-smb-2025-01'] = {
    'reason': 'entail partial: the row says nothing about NTLM; clause removed.',
    'claim': 'On 2025-01-28 DataSync began to support Kerberos authentication when connecting to Server Message Block (SMB) file servers.',
}
D['datasync-change-secrets-manager-all-location-types-2026-03'] = {
    'reason': 'entail partial: the date stood only in the Posted on line; that line added as heading-scoped evidence.',
    'evidence': [0, 1, ev('www/about-aws/whats-new/2026/03/aws-datasync-secrets-manager', 'Posted on: Mar 20, 2026',
                          heading='AWS DataSync now supports AWS Secrets Manager for all location types')],
}
D['datasync-change-shared-vpcs-2026-09'] = {
    'reason': 'entail partial: old state now keeps its scope (customers that centralize networking, PrivateLink); date condition removed.',
    'claim': 'On 2026-09-15 DataSync added support for shared VPC subnets via AWS Resource Access Manager: a VPC owner can share a subnet with another account, which can then create DataSync agents in that subnet. Before this, customers that centralize their networking had to create a separate DataSync VPC endpoint in every account that connected privately through AWS PrivateLink.',
    'qual': {'condition': ''},
    'note_add': 'adjudicate-25: the What\'s New post is dated 2026-09-29 (not quoted).',
}
D['datasync-decision-guide-offline-options-dtt-partners-snow-closed-datasync-online'] = {
    'reason': 'currency outdated: the same guide now carries the Snow Family end of support card; claim drops the existing-customers clause and adds the end of support quote.',
    'claim': 'For offline or physical transfers the storage decision guide names AWS Data Transfer Terminal and AWS Partner solutions, says the Snow Family is no longer available to new customers, and names AWS DataSync for online transfers. The same guide says AWS will discontinue support for AWS Snowball devices in all AWS commercial Regions on 2026-12-31, which does not affect AWS GovCloud (US) customers with active Snow jobs.',
    'qual': {'condition': ''},
    'evidence': [0, ev('docs/decision-guides/latest/decision-guides/choosing-aws-storage-service', GUIDE_EOS)],
}
D['datasync-decision-guide-offline-row-dtt-snow-existing-only'] = {
    'reason': 'entail partial (bandwidth condition rewritten) and currency outdated (existing-only line superseded by the end of support card): claim follows the row wording and adds the end of support quote.',
    'claim': 'In the storage decision guide the Offline row is suitable for one-time or periodic uploads when data can be static in transit, makes sense when you need to use only the minimum available bandwidth and prefer the predictability of physical moves, and names AWS Data Transfer Terminal. The same guide says AWS will discontinue support for AWS Snowball devices in all AWS commercial Regions on 2026-12-31.',
    'values': [{'key': 'v1', 'display': 'one-time or periodic uploads'}, {'key': 'v2', 'display': 'AWS Data Transfer Terminal'}],
    'evidence': [0, ev('docs/decision-guides/latest/decision-guides/choosing-aws-storage-service', GUIDE_EOS)],
}
D['datasync-decision-migration-guide-file-transfer-sync-file-systems'] = {
    'reason': 'entail partial: quote extended with the sentence that names DataSync.',
    'evidence': [ev('docs/decision-guides/latest/decision-guides/migration-on-aws-how-to-choose',
                    'Organizations can also leverage AWS DataSync for efficient, high-speed data transfers. It helps synchronize on-premises file systems with AWS storage services, minimizing downtime and ensuring data consistency.')],
}
D['datasync-decision-migration-guide-large-transfer-online-limits-and-direct-connect'] = {
    'reason': 'entail partial: quote extended with the sentence that names online transfer with DataSync.',
    'claim': 'The migration guide says online data transfer with services like DataSync might be insufficient for extremely large datasets or environments with limited bandwidth, and that Direct Connect gives a dedicated private network connection with consistent, high-bandwidth connectivity for large data transfers.',
    'evidence': [ev('docs/decision-guides/latest/decision-guides/migration-on-aws-how-to-choose',
                    'For online data transfer, services like AWS DataSync employ optimized protocols to maximize data transfer speeds, reducing the time required to move data to the cloud. However, this method might be insufficient for extremely large datasets or environments with limited bandwidth.'), 1],
}
D['datasync-direct-connect-public-vif-needs-public-prefix-for-agent'] = {
    'reason': 'entail partial: added the public virtual interface sentences as evidence.',
    'claim': 'If your DataSync agent uses a public or FIPS service endpoint, you can route the transfer through Direct Connect by using a public virtual interface; you must advertise at least one public prefix to create your DataSync agent.',
    'qual': {'scope': 'DataSync with a Direct Connect public virtual interface (public or FIPS service endpoint)'},
    'evidence': [ev('docs/datasync/latest/userguide/direct-connect-architecture',
                    'If your DataSync agent uses a [public](choose-service-endpoint.md#choose-service-endpoint-public) or [Federal Information Processing Standard (FIPS)](choose-service-endpoint.md#choose-service-endpoint-fips) service endpoint, you can route your data transfer traffic through a Direct Connect connection by using a [public virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html#create-public-vif).'),
                 ev('docs/datasync/latest/userguide/direct-connect-architecture',
                    'While Direct Connect advertises all local and remote AWS Region prefixes by default, you can use [BGP community tags](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html#bgp-communities) to control the scope (Regional or global) and route preference of traffic on the public virtual interface. You must advertise at least one public prefix to create your DataSync agent.')],
}
D['datasync-direct-connect-transit-gateway-bypass-saves-processing-charges'] = {
    'reason': 'entail partial: added the next sentence (bypass of the transit gateway and its data processing charges) as evidence.',
    'evidence': [0, ev('docs/datasync/latest/userguide/direct-connect-architecture',
                       'For example, if you use [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) for normal traffic between your on-premises networks and virtual private clouds (VPCs), you can configure your network so that DataSync traffic bypasses the transit gateway and its data processing charges.')],
}
D['datasync-faq-agent-endpoint-choices'] = dict(
    reason='entail partial: the activation condition is not in the quote; removed.',
    **cond_drop('adjudicate-25: the endpoint is chosen when the agent is activated (not in the quote).'))
D['datasync-faq-agent-types-follow-task-mode'] = {
    'reject': True,
    'reason': 'currency outdated: the FAQ rule (Enhanced agent only for NFS/SMB to S3, Basic for all other cases) is stale after the 2026-07-28 Enhanced mode additions; current agent facts: datasync-agent-two-types-basic-and-enhanced, datasync-change-enhanced-mode-hdfs-azure-object-hyper-v-2026-07.',
}
D['datasync-faq-enhanced-mode-locations-as-of-faq'] = {
    'reject': True,
    'reason': 'currency outdated: the FAQ list of Enhanced mode locations predates 2025-12 and 2026-07 changes; the current list is datasync-faq-vs-guide-enhanced-mode-locations-in-guide.',
}
D['datasync-faq-nfs-smb-access-needs-agent'] = {
    'reject': True,
    'reason': 'entail partial: the claim covers all NFS and SMB locations while the FAQ answer is about your own NFS server or SMB share; the verified fact datasync-agent-needed-when-storage-managed-by-you-or-other-cloud states the rule with its scope.',
}
D['datasync-faq-s3-access-assumes-iam-role'] = {
    'reason': 'entail partial: S3 scope stood only in the FAQ heading; added the S3 location guide sentences that name the S3 bucket.',
    'claim': 'DataSync assumes an IAM role that you provide, and the policy attached to the role determines which actions it can perform. When you create an Amazon S3 location in the console, DataSync can automatically create and assume an IAM role that normally has the right permissions to access your S3 bucket; in some situations, such as buckets with extra layers of security or buckets in a different AWS account, you might need to create this role manually.',
    'evidence': [0,
                 ev('docs/datasync/latest/userguide/create-s3-location',
                    'When [creating your Amazon S3 location](#create-s3-location-how-to) in the console, DataSync can automatically create and assume an IAM role that normally has the right permissions to access your S3 bucket.'),
                 ev('docs/datasync/latest/userguide/create-s3-location',
                    'In some situations, you might need to create this role manually (for example, accessing buckets with extra layers of security or transferring to or from a bucket in a different AWS accounts).')],
}
D['datasync-faq-vpc-endpoints-privatelink-supported'] = {
    'reason': 'entail partial: PrivateLink is not in the quote; claim narrowed to the quote.',
    'claim': 'DataSync supports VPC endpoints for data movement: with VPC endpoints, data transferred between your DataSync agent, deployed on premises or in the cloud, does not traverse the public internet or need public IP addresses.',
}
D['datasync-large-migration-low-throughput-partition-into-tasks'] = {
    'reason': 'entail partial: proof-of-concept clause removed.',
    'claim': 'If your DataSync throughput is lower than your available bandwidth, consider partitioning your dataset into multiple tasks to maximize bandwidth usage.',
}
D['datasync-large-migration-partition-by-folder-filters-manifests'] = {
    'reason': 'entail partial: no quote covers manifests; claim narrowed to locations and filters.',
    'claim': 'You can partition a dataset for DataSync by folder, directory or prefix (several source locations, each with a different path, used by multiple tasks), or apply filters to include or exclude data from the source location in a transfer.',
    'values': [{'key': 'v1', 'display': 'by folder, directory or prefix'}, {'key': 'v2', 'display': 'apply filters to include or exclude data'}],
}
D['datasync-manifest-list-of-exact-files-or-objects'] = {
    'reason': 'entail partial: the bucket example clause removed.',
    'claim': 'A manifest is a list of files or objects that you want DataSync to transfer; manifests are similar to filters but let you identify exactly which files or objects to transfer instead of data that matches a filter pattern.',
}
D['datasync-networking-direct-connect-private-path-more-predictable-than-vpn'] = {
    'reason': 'entail partial: added the Direct Connect lead-in line as evidence.',
    'evidence': [ev('docs/datasync/latest/userguide/networking-datasync', DC_LEAD), 0, 1],
}
D['datasync-networking-direct-connect-supports-any-endpoint-type'] = {
    'reason': 'entail partial: added the Direct Connect lead-in line as evidence.',
    'evidence': [ev('docs/datasync/latest/userguide/networking-datasync', DC_LEAD), 0],
}
D['datasync-networking-options-direct-connect-vpn-public-internet'] = {
    'reason': 'entail partial: added the Direct Connect option line as evidence; FAQ condition removed.',
    'qual': {'condition': ''},
    'note_add': 'adjudicate-25: the FAQ states that DataSync does not require a VPN (separate source, not quoted here).',
    'evidence': [ev('docs/datasync/latest/userguide/networking-datasync', DC_LEAD), 0, 1],
}
D['datasync-networking-three-connections-with-agent'] = {
    'reason': 'entail partial: the three named connections are not in the quote; claim narrowed.',
    'claim': 'If you need a DataSync agent, you must establish several network connections for a data transfer; the DataSync guide shows three network connections in a transfer from a storage system (on premises, in another cloud or at the edge) to an AWS storage service.',
}
D['datasync-requirement-agent-vm-disk-80-gb'] = {
    'reason': 'entail partial: added the intro sentence that gives the not-on-EC2 scope.',
    'evidence': [0, ev('docs/datasync/latest/userguide/agent-requirements',
                       'When deploying a DataSync agent that isn\'t on an Amazon EC2 instance, the agent VM requires the following resources, depending upon whether you use a Basic mode agent or an Enhanced mode agent:')],
}
D['datasync-requirement-agent-vm-ram'] = {
    'reason': 'entail partial: added the intro sentence (not-on-EC2 scope) and the general-guidelines note.',
    'claim': 'A DataSync agent VM that is not on an Amazon EC2 instance needs 32 GB of RAM for Basic mode task executions working with up to 20 million files, objects or directories, and 64 GB of RAM for more than 20 million. An Enhanced mode agent VM needs 32 GB of RAM. AWS says the Basic mode requirements for up to 20 million files, objects or directories are general guidelines.',
    'evidence': [0,
                 ev('docs/datasync/latest/userguide/agent-requirements',
                    'When deploying a DataSync agent that isn\'t on an Amazon EC2 instance, the agent VM requires the following resources, depending upon whether you use a Basic mode agent or an Enhanced mode agent:'),
                 ev('docs/datasync/latest/userguide/agent-requirements',
                    'Keep in mind that the Basic mode agent requirements for working with up to 20 million files, objects, or directories are general guidelines.')],
}
D['datasync-s3-multipart-upload-incomplete-storage-charges'] = {
    'reason': 'entail partial: bucket policy wording and the multipart condition fixed.',
    'claim': 'DataSync uses the Amazon S3 multipart upload feature to upload objects to S3 buckets, which can result in unexpected storage charges for uploads that don\'t complete successfully; if the issue is related to multipart uploads, AWS suggests configuring a policy for multipart uploads for the S3 bucket to clean up incomplete multipart uploads and reduce storage cost.',
}
D['datasync-transfer-all-data-does-not-compare-locations'] = {
    'reason': 'entail partial: scanning clause removed.',
    'claim': 'If you configure a DataSync task to transfer all data, DataSync doesn\'t compare your source and destination locations, but the task execution still has a PREPARING status.',
}
D['datasync-transfer-performance-counters-track-progress'] = {
    'reason': 'entail partial: the console and API clause and the condition are not in the quote; removed.',
    'claim': 'When you start a task, AWS DataSync provides counters to help track your data transfer\'s performance and progress.',
    'values': [{'key': 'v1', 'display': 'counters to help track your data transfer\'s performance'}],
    'qual': {'condition': ''},
    'note_add': 'adjudicate-25: the counters are viewed in the console or in a DescribeTaskExecution response; some counters are not available with every task mode (not in the quote).',
}
D['datasync-verify-all-data-point-in-time-consistent'] = {
    'reason': 'entail partial: the manifest exception of the same row added to the claim.',
    'claim': 'The Verify all data option (VerifyMode set to POINT_IN_TIME_CONSISTENT) checks the entire source and destination at the end of the transfer, or only what is listed in the manifest when you use a manifest; it is not supported in Enhanced mode and cannot be used when transferring to S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive.',
}

# ---------------- Snow Family ----------------
D['snow-family-batch-small-files-to-speed-transfer'] = {
    'reason': 'entail partial: archive-format condition added; 100 GB condition removed.',
    'claim': 'Each copy operation to Snowball Edge has overhead because of encryption, so to speed up transferring small files you can batch them together in a single archive; batched files can be auto-extracted when they are imported into Amazon S3 if they were batched in one of the supported archive formats.',
    'qual': {'condition': ''},
    'note_add': 'adjudicate-25: the page adds a size limit for auto-extracted batches (not in the quote).',
}
D['snow-family-change-closed-to-new-customers-2025-11'] = {
    'reason': 'currency unsure: the existing-customers-continue-as-normal clause no longer holds after the end of support notice; clause removed and end of support quote added.',
    'claim': 'AWS announced on 2025-10-07 that, effective 2025-11-07, AWS Snowball Edge would only be available to existing customers. AWS Snowball Edge is no longer available to new customers, and AWS no longer offers any AWS Snow Family devices for new customers to order. AWS will discontinue support for AWS Snowball devices in all AWS commercial Regions on 2026-12-31.',
    'qual': {'scope': 'AWS Snowball Edge availability, all Snow Family devices for new customers', 'condition': ''},
    'evidence': [0,
                 ev('docs/snowball/latest/developer-guide/snowball-edge-availability-change',
                    'With this change, AWS will no longer offer any AWS Snow Family devices for new customers to order.'),
                 2,
                 ev('www/snowball', SNOW_EOS)],
}
D['snow-family-change-console-access-ends-after-2026-12-31'] = {
    'reason': 'entail partial: the GovCloud and ADC exception added to the quote and claim.',
    'claim': 'After 2026-12-31 you will no longer be able to access the AWS Snow Console or AWS Snowball resources; this service availability change does not affect GovCloud or ADC Region customers who have active Snow jobs.',
    'qual': {'condition': ''},
    'evidence': [ev('www/snowball', 'After December 31, 2026, you will no longer be able to access the AWS Snow Console or AWS Snowball resources. Please note that this service availability change does not affect GovCloud or ADC Region customers who have active Snow jobs today.'),
                 ev('www/snowball', SNOW_EOS)],
}
D['snow-family-change-file-interface-deprecated-2024-03'] = {
    'reason': 'currency unsure: the file interface row and the current NFS page seemed to conflict; claim now states both, each with its quote.',
    'claim': 'On 2024-03-01 the Snowball Edge document history recorded that the file interface is no longer available for data transfer. The current Snowball Edge guide still says that the NFS interface is available for import jobs.',
    'evidence': [0, ev('docs/snowball/latest/developer-guide/shared-using-nfs', NFS_AVAIL)],
}
D['snow-family-device-access-keys-only-local-not-aws-account'] = {
    'reason': 'entail partial: added the sentence that names the keys (list-access-keys, get-secret-access-key).',
    'claim': 'The credentials shown by the Snowball Edge client commands list-access-keys and get-secret-access-key are a pair of access keys used to access the device; they are only associated with the job and the local resources on the device, don\'t map to your AWS account, and fail if used to access services and resources in the AWS Cloud.',
    'evidence': [ev('docs/snowball/latest/developer-guide/BestPractices',
                    'The credentials displayed, when you run the Snowball Edge client commands list-access-keys and get-secret-access-key, are a pair of access keys used to access your device.'), 0],
}
D['snow-family-device-storage-optimized-210-tb-usable'] = dict(
    reason='entail partial: the S3-compatible-storage condition stands only in the note; removed.',
    **cond_drop('adjudicate-25: a note on the page says usable storage differs when Amazon S3 compatible storage on Snowball Edge is used (not quoted).'))
D['snow-family-dtt-does-not-encrypt-data-in-transit'] = {
    'reason': 'entail partial: at-rest clause and API-endpoint condition removed.',
    'claim': 'AWS Data Transfer Terminal does not encrypt data in transit; management of the data and its encryption in transit are the responsibility of the individual using Data Transfer Terminal.',
    'qual': {'condition': ''},
    'note_add': 'adjudicate-25: the page also covers encryption at rest and API endpoint traffic (not quoted).',
}
D['snow-family-dtt-enterprise-support-customers-only'] = dict(
    reason='entail partial: the contact-support route is not in the quote; condition removed.',
    **cond_drop('adjudicate-25: the next sentence of the page offers a route for other customers through AWS Support (not quoted).'))
D['snow-family-dtt-requires-fiber-and-100g-transceiver-you-bring'] = {
    'reason': 'entail partial: the transceiver item is a list item under a have-the-following lead-in; claim now says the requirements list it.',
    'claim': 'For a Data Transfer Terminal reservation you must bring portable devices for connectivity, including monitors, a keyboard, a mouse, and a computer or laptop. The technical requirements also list a 100G QSFP28 LR4 (100GBASE-LR4) optical QSFP transceiver, compatible with the NIC and LC connectors for the fiber cable connections provided in the facility.',
}
D['snow-family-faq-import-via-s3-endpoint-or-nfs'] = {
    'reason': 'currency unsure on the NFS file interface; claim narrowed to the S3-compatible endpoint and the Snowball client.',
    'claim': 'After you connect and activate a Snowball Edge, you can transfer data from local sources to the device through the S3-compatible endpoint on the device, and you can also use the Snowball client to copy data.',
    'values': [{'key': 'methods', 'display': 'S3-compatible endpoint'}],
}
D['snow-family-faq-provisioning-up-to-4-weeks'] = {
    'reason': 'entail partial: transfer-timeline clause removed.',
    'claim': 'After you place a job order for a Snowball device, AWS provisions, prepares and ships it; this provisioning process may take up to 4 weeks from the time of order placement and should be factored into your project plan.',
}
D['snow-family-faq-transfer-time-factors'] = {
    'reason': 'entail partial: the 210 TB scope of the total-time sentence restored.',
    'claim': 'Snowball Edge data transfer speed is affected by factors including local network speed, file size and the speed at which data can be read from your local servers; the FAQ says the total time to transfer 210 TB of data includes loading and unloading the device and shipping the devices to and from your location.',
}
D['snow-family-faq-use-when-disconnected-or-no-bandwidth'] = {
    'reason': 'currency outdated and entail partial: closure and end of support now stand in the claim with their own quotes.',
    'claim': 'The Snowball Edge FAQ says to consider Snowball Edge to run computing in rugged, austere, mobile or disconnected environments, and for large-scale data transfers and migrations when bandwidth is not available for a high-speed online transfer service such as AWS DataSync. AWS Snowball Edge is no longer available to new customers, and AWS will discontinue support for AWS Snowball devices in all AWS commercial Regions on 2026-12-31.',
    'qual': {'condition': ''},
    'evidence': [0,
                 ev('docs/snowball/latest/developer-guide/snowball-edge-availability-change', 'AWS Snowball Edge is no longer available to new customers.'),
                 ev('www/snowball', SNOW_EOS)],
}
D['snow-family-listed-in-saa-c03-in-scope-services'] = dict(
    reason='entail partial: the non-exhaustive condition is not in the quote; removed.',
    **cond_drop('adjudicate-25: the exam guide says the list is non-exhaustive and subject to change (not quoted).'))
D['snow-family-nfs-interface-for-import-jobs-if-configured-at-order'] = {
    'reason': 'currency unsure (file interface row of 2024-03-01): claim now states the current NFS page and the history row, each with its quote.',
    'claim': 'The current Snowball Edge guide says the NFS interface is available for import jobs, and that you can use it if the Snowball Edge device was configured to include it when the job to order the device was created. The document history separately records on 2024-03-01 that the file interface is no longer available for data transfer.',
    'evidence': [0, 1, ev('docs/snowball/latest/developer-guide/doc-history', SNOW_HIST_ROW, table_header=HIST_HDR)],
}
D['snow-family-nfs-interface-not-encrypted-in-transit'] = {
    'reason': 'currency unsure (file interface row of 2024-03-01): claim attributed to the current NFS page.',
    'claim': 'The current Snowball Edge NFS page says data transferred through the NFS interface is not encrypted in transit, and that when you configure the NFS interface you can provide CIDR blocks so the device restricts access to client computers with addresses in those blocks.',
}
D['snow-family-no-snow-device-for-new-customers-existing-unaffected'] = {
    'reject': True,
    'reason': 'currency unsure: existing-customers-unaffected no longer holds after the end of support notice; the closure is carried by snow-family-change-closed-to-new-customers-2025-11 and the end of support by snow-family-change-end-of-support-2026-12-31.',
}
D['snow-family-opshub-manages-devices-no-extra-cost'] = {
    'reason': 'entail partial: claim narrowed to the quoted tasks; closure condition removed.',
    'claim': 'You use AWS OpsHub on a client computer for tasks such as unlocking and configuring single or clustered Snowball Edge devices, transferring files, and launching and managing instances running on Snowball Edge; the AWS OpsHub application is available at no additional cost.',
    'qual': {'condition': ''},
}
D['snow-family-pricing-on-demand-dimensions'] = dict(
    reason='entail partial: the Region and device-type condition stands only in the next sentence; removed.',
    **cond_drop('adjudicate-25: the next sentence says fees vary by Region and device type (not quoted).'))
D['snow-family-quota-default-devices-per-account-per-region'] = {
    'reason': 'entail partial: quote extended with the contact-support sentence.',
    'claim': 'The default service limit for the number of Snowball Edge devices you can have at one time is 1 per account, per AWS Region; to increase the limit or create a cluster job, contact AWS Support.',
    'evidence': [ev('docs/snowball/latest/developer-guide/limits',
                    'The default service limit for the number of Snowball Edge Edge devices you can have at one time is 1 per account, per AWS Region. If you want to increase your service limit or create a cluster job, contact [AWS Support](https://aws.amazon.com/premiumsupport/).')],
}
D['snow-family-quota-import-object-size-range-5-tb'] = dict(
    reason='entail partial: the 50 TB S3 condition is not supported by the quote; moved to the note.',
    **cond_drop('adjudicate-25: the S3 object maximum is now 50 TB (s3-change-max-object-size-50-tb-2025-12); this Snowball page still says 5 TB.'))
D['snow-family-snowball-edge-definition-device-storage-and-compute'] = dict(
    reason='entail partial: the closure condition stands only in the page banner; removed.',
    **cond_drop('adjudicate-25: Snowball Edge is closed to new customers (see snow-family-change-closed-to-new-customers-2025-11).'))
D['snow-family-three-job-types'] = dict(
    reason='entail partial: the job type names are not in the quote; condition removed.',
    **cond_drop('adjudicate-25: the page lists import, export and local compute and storage jobs (not in the quote).'))

# ---------------- Storage Gateway ----------------
D['storage-gateway-activate-gateway-in-vpc-private-connection'] = {
    'reason': 'entail partial: added the VPC endpoint sentences that say how the private connection is made.',
    'claim': 'You can create a private connection between your on-premises gateway appliance and cloud-based storage infrastructure and use it to activate your gateway and transfer data to AWS storage services without communicating over the public internet: you create a VPC endpoint for Storage Gateway and specify its ID when you create and activate the gateway, and an S3 File Gateway also needs a separate VPC endpoint for Amazon S3 that you specify when you create file shares.',
    'qual': {'scope': 'Storage Gateway activation in a VPC'},
    'evidence': [0,
                 ev('docs/filegateway/latest/files3/gateway-private-link',
                    'To activate your gateway in a VPC, use the Amazon VPC Console to [create a VPC endpoint for Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/create-vpc-endpoint) and get the VPC endpoint ID, then specify this VPC endpoint ID when you create and activate the gateway.'),
                 ev('docs/filegateway/latest/files3/gateway-private-link',
                    'To configure your S3 File Gateway to transfer data through the VPC, you must create a separate VPC endpoint for Amazon S3, then specify this VPC endpoint when you create file shares for the gateway.')],
}
D['storage-gateway-change-console-copy-file-shares-2026-07'] = {
    'reason': 'entail partial: the Posted on line added as heading-scoped evidence.',
    'evidence': [0, 1, ev('www/about-aws/whats-new/2026/07/aws-storage-gateway-console-copy-file-shares', 'Posted on: Jul 14, 2026',
                          heading='AWS Storage Gateway adds console support for copying file shares across gateways')],
}
D['storage-gateway-change-fips-privatelink-s3-file-2026-09'] = {
    'reason': 'entail partial: the Posted on line added as heading-scoped evidence.',
    'evidence': [0, 1, 2, ev('www/about-aws/whats-new/2026/09/storage-gateway-fips-privatelink-s3', 'Posted on: Sep 10, 2026',
                             heading='AWS Storage Gateway now supports FIPS-compliant private connectivity for Amazon S3 File Gateway')],
}
D['storage-gateway-change-fips-privatelink-tape-volume-2026-08'] = {
    'reason': 'entail partial: the Posted on line added as heading-scoped evidence.',
    'evidence': [0, 1, 2, ev('www/about-aws/whats-new/2026/08/storage-gateway-fips-privatelink', 'Posted on: Aug 19, 2026',
                             heading='AWS Storage Gateway now supports FIPS-compliant private connectivity for Tape and Volume Gateway')],
}
D['storage-gateway-change-ipv6-2025-09'] = dict(
    reason='entail partial: the IPv4 condition stands only in the next sentence; removed.',
    **cond_drop('adjudicate-25: the post adds that the existing IPv4-only endpoints remain available (not quoted).'))
D['storage-gateway-faq-aws-backup-benefits-central-policies-retention'] = {
    'reason': 'entail partial: the central monitoring clause removed.',
    'claim': 'Using AWS Backup to back up Volume Gateway volumes simplifies and centralizes backup management, lets you set customizable scheduled backup policies, and lets you set backup retention and expiration rules so you no longer need to develop custom scripts or manually manage point-in-time backups of the volumes.',
}
D['storage-gateway-faq-fips-endpoints-gateway-types'] = {
    'reject': True,
    'reason': 'currency outdated: the FAQ says FIPS 140-2 while the current guide and the 2026 posts name FIPS 140-3; current FIPS facts: storage-gateway-change-fips-privatelink-s3-file-2026-09 and storage-gateway-change-fips-privatelink-tape-volume-2026-08.',
}
for _id, _n in [
        ('storage-gateway-faq-fsx-file-gateway-smb-to-fsx-windows', 'adjudicate-25: FSx File Gateway is closed to new customers (see fsx-change-fsx-file-gateway-maintenance-2024-10).'),
        ('storage-gateway-faq-hardware-appliance-for-sites-without-virtual-infrastructure', 'adjudicate-25: the hardware appliance is no longer offered to new customers (see storage-gateway-hardware-appliance-end-of-availability).'),
        ('storage-gateway-faq-hardware-appliance-gateway-types', 'adjudicate-25: the hardware appliance is no longer offered to new customers (see storage-gateway-hardware-appliance-end-of-availability).'),
        ('storage-gateway-faq-hardware-appliance-two-models-cache', 'adjudicate-25: the expansion of the 5 TB model is not in the quote; the hardware appliance is no longer offered to new customers.'),
        ('storage-gateway-faq-s3-file-gateway-multiple-readers-read-only-share', 'adjudicate-25: a note on the FAQ says a share that is not read-only is not monitored for writes by readers (not quoted).'),
        ('storage-gateway-faq-s3-file-gateway-same-bucket-nfs-and-smb-not-mapped', 'adjudicate-25: one gateway can still export a mix of NFS and SMB shares (separate FAQ answer).'),
        ('storage-gateway-faq-s3-file-gateway-storage-classes-supported', 'adjudicate-25: the user guide adds that S3 Glacier Instant Retrieval is not supported (not quoted).'),
        ('storage-gateway-faq-s3-file-gateway-upload-notification-cloudwatch-events', 'adjudicate-25: CloudWatch Events is now Amazon EventBridge.'),
        ('storage-gateway-s3-file-gateway-file-operations-replace-objects', 'adjudicate-25: the page table lists rename, folder rename, permission change, ownership change and append as examples (not quoted).'),
        ('storage-gateway-s3-file-gateway-smb-client-negotiated-trades-security-for-throughput', 'adjudicate-25: the note below says to wait for the share status Available and reconnect SMB clients (not quoted).'),
        ('storage-gateway-fsx-file-gateway-alternative-access-fsx-windows-directly', 'adjudicate-25: the condition is not in the quote; removed.'),
]:
    D[_id] = dict(reason='entail partial: the condition qualifier is not in the quote; moved to the note.', **cond_drop(_n))
D['storage-gateway-fsx-file-gateway-alternative-access-fsx-windows-directly']['claim'] = (
    'The AWS list of services in maintenance names Amazon FSx File Gateway with the announcement date October 28, 2024, and links the resource \'Switch your file share access from Amazon FSx File Gateway to Amazon FSx for Windows File Server\'.')
D['storage-gateway-fsx-file-gateway-alternative-access-fsx-windows-directly']['reason'] = 'entail partial: the row only lists the blog post as the resource; claim now says that.'
D['storage-gateway-faq-s3-file-max-file-size-5-tb'] = {
    'reject': True,
    'reason': 'currency unsure: the FAQ reason (5 TB is the S3 object maximum) is stale and the current quotas page describes other behavior; the S3 File Gateway maximum is storage-gateway-s3-file-quota-max-file-size (5 TiB).',
}
D['storage-gateway-faq-volume-gateway-volumes-in-service-managed-bucket'] = {
    'reason': 'entail partial: the added only removed.',
    'claim': 'Volume Gateway volumes are stored in an S3 bucket maintained by the Storage Gateway service and are accessible for I/O operations through Storage Gateway; you cannot directly access them using Amazon S3 API actions, and AWS points to File Gateway for working with data natively in S3.',
}
D['storage-gateway-requirement-vm-disk-80-gib'] = {
    'reason': 'entail partial: on-premises scope and the VM image purpose removed.',
    'claim': 'In addition to 80 GiB of disk space for the VM, an S3 File Gateway needs additional disks for the gateway.',
    'qual': {'scope': 'S3 File Gateway VM disk space', 'condition': ''},
}
D['storage-gateway-s3-file-gateway-multipart-uploads-abort-lifecycle-rule'] = {
    'reason': 'entail partial: claim narrowed to the quote.',
    'claim': 'As a best practice for minimizing Amazon S3 storage costs from incomplete multipart uploads, AWS recommends configuring an S3 bucket lifecycle rule that uses the AbortIncompleteMultipartUpload API action to automatically stop unsuccessful transfers and delete associated file parts after a designated number of days.',
}
D['storage-gateway-s3-file-gateway-upload-notification-for-two-gateway-content-distribution'] = {
    'reason': 'entail partial: the two-gateway sentences added as evidence.',
    'claim': 'For content distribution you can have two S3 File Gateways that map to the same S3 bucket; files that clients of Gateway1 upload are not visible to Gateway2 because it uses a locally cached version of files in S3, so you can request file upload notification from Gateway1 and use CloudWatch Events to automatically issue a RefreshCache request for the file share on Gateway2.',
    'evidence': [ev('docs/filegateway/latest/files3/monitoring-file-gateway',
                    'For content distribution use cases, you can have two S3 File Gateways that map to the same Amazon S3 bucket. The file share client for Gateway1 could upload new files to Amazon S3, and the files are read by file share clients on Gateway2.'), 0],
}
D['storage-gateway-s3-file-versioning-adds-object-versions-cost'] = {
    'reason': 'entail partial: the scenarios behind the storage increase added to the quote and claim.',
    'claim': 'Uploading files from an S3 File Gateway to Amazon S3 when S3 versioning is turned on commonly results in more than one version of an S3 object; large files written in several steps, or a gateway cache that must free up space under high file-write rates, can create multiple S3 object versions, and these scenarios increase S3 storage if S3 Versioning is turned on and increase the transfer costs associated with CRR.',
    'evidence': [0, ev('docs/filegateway/latest/files3/avoid-unanticipated-costs',
                       'Certain workflows involving large files and file-writing patterns such as file uploads that are performed in several steps can increase the number of stored S3 object versions. If the File Gateway cache needs to free up space due to high file-write rates, multiple S3 object versions might be created. These scenarios increase S3 storage if S3 Versioning is turned on and increase the transfer costs associated with CRR.')],
}
D['storage-gateway-tape-gateway-preconfigured-media-changer-and-drives'] = {
    'reason': 'entail partial: the tape cartridge clause removed.',
    'claim': 'Each Tape Gateway is preconfigured with a media changer and tape drives, which are available to your existing client backup applications as iSCSI devices.',
}
D['storage-gateway-volume-gateway-optimize-iscsi-settings-initiator'] = {
    'reason': 'entail partial: scope narrowed to Volume Gateway (the page is the Volume Gateway guide).',
    'qual': {'scope': 'Volume Gateway'},
}
D['storage-gateway-volume-gateway-restore-snapshot-to-gateway-or-ebs'] = {
    'reason': 'entail partial: the 16 TiB condition added to the claim.',
    'claim': 'You can restore an Amazon EBS snapshot to a gateway storage volume to recover a backup of your data; alternatively, for snapshots up to 16 TiB in size, you can use the snapshot as a starting point for a new Amazon EBS volume that you attach to an Amazon EC2 instance.',
    'qual': {'condition': 'the EBS-volume route is for snapshots up to 16 TiB'},
}
D['storage-gateway-volume-gateway-snapshots-incremental-as-ebs-snapshots'] = {
    'reason': 'entail partial: the scheduling clause removed.',
    'claim': 'Volume Gateway point-in-time snapshots are stored in Amazon S3 as Amazon EBS snapshots, and when you take a new snapshot only the data that has changed since your last snapshot is stored.',
}
D['storage-gateway-volume-gateway-upload-buffer-full-pass-through'] = {
    'reason': 'entail partial: the until-clause removed.',
    'claim': 'When the upload buffer of a Volume Gateway reaches its capacity, the volume goes to PASS THROUGH status: new data that your application writes is persisted locally but not uploaded to AWS immediately, so you cannot take new snapshots.',
}
D['storage-gateway-volume-tape-gateway-separate-physical-disks-cache-and-upload-buffer'] = {
    'reason': 'entail partial: scope narrowed to Volume Gateway (the page is the Volume Gateway guide).',
    'qual': {'scope': 'Volume Gateway'},
}

# ---------------- Transfer Family ----------------
D['transfer-family-availability-zones-redundancy-built-in'] = {
    'reason': 'entail partial: the single-subnet note for VPC endpoints added as evidence and to the claim.',
    'claim': 'For all Transfer Family endpoints, Availability Zone-level redundancy is built into the service, there are redundant fleets for each AZ, and this redundancy is provided automatically. For endpoints in a VPC you can provide a single subnet, but AWS recommends creating endpoints in multiple Availability Zones to reduce the risk of service disruptions during Availability Zone outages.',
    'qual': {'condition': ''},
    'evidence': [0, ev('docs/transfer/latest/userguide/disaster-recovery-resiliency',
                       'For endpoints in a Virtual Private Cloud (VPC), it is possible to provide a single subnet. However, we recommend that you create endpoints in multiple availability zones within your VPC, to reduce the risk of service disruptions during Availability Zone outages.')],
}
D['transfer-family-case-myriota-replaced-presigned-url-apis-with-sftp'] = {
    'reason': 'entail partial: the IoT description removed.',
    'claim': 'Myriota used REST APIs to generate pre-signed URLs so partners could upload data to Amazon S3, and as the alternative chose AWS Transfer for SFTP, a fully managed service that transfers files directly into and out of Amazon S3 using SFTP.',
}
D['transfer-family-change-fsx-for-ontap-2026-01'] = dict(
    reason='entail partial: the select-Regions condition is not in the quotes; removed.',
    **cond_drop('adjudicate-25: the post says the feature is available in select AWS Regions (not quoted).'))
D['transfer-family-change-sftp-connector-quota-auto-approval-1000-2026-09'] = dict(
    reason='entail partial: the egress-type condition is in no quote; removed.',
    **cond_drop('adjudicate-25: per the post, automatic approval applies to connectors with service-managed or VPC Lattice egress; above 1,000 you submit a higher quota request (not quoted).'))
D['transfer-family-change-source-ip-preservation-behind-nlb-2026-09'] = {
    'reason': 'entail partial: VPC-hosted scope and per-server condition removed.',
    'qual': {'scope': 'SFTP servers behind a Network Load Balancer', 'condition': ''},
    'note_add': 'adjudicate-25: the setting is per server, for VPC-hosted endpoints (not quoted).',
}
D['transfer-family-custom-idp-api-gateway-for-restful-and-waf'] = {
    'reason': 'entail partial: quote extended with the sentences that name API Gateway.',
    'evidence': [ev('docs/transfer/latest/userguide/custom-idp-intro',
                    'You can provide a RESTful interface with a single Amazon API Gateway method. Transfer Family calls this method to connect to your identity provider, which authenticates and authorizes your users for access to Amazon S3 or Amazon EFS. Use this option if you need a RESTful API to integrate your identity provider or if you want to use AWS WAF to leverage its capabilities for geo-blocking or rate-limiting requests.')],
}
D['transfer-family-events-go-to-eventbridge-default-event-bus'] = {
    'reason': 'entail partial: the rules clause removed.',
    'claim': 'Transfer Family generates and sends events to the Amazon EventBridge default event bus, which is automatically provisioned in every AWS account.',
}
D['transfer-family-faq-corporate-domain-name-route53'] = {
    'reason': 'entail partial: quote extended with the internet-facing-only sentence.',
    'claim': 'You can use your own domain name for a Transfer Family endpoint: the service supplies a domain name by default, and you can use Amazon Route 53 or any DNS service to route traffic from your registered domain to the server endpoint; the documentation on how AWS Transfer Family uses Amazon Route 53 for custom domain names applies to internet-facing endpoints only.',
    'evidence': [ev('www/aws-transfer-family/faqs',
                    'Yes. The service supplies a domain name by default to access your endpoint. If you already have a domain name, you can use Amazon Route 53 or any DNS service to route your users’ traffic from your registered domain to the server endpoint in AWS. Refer to the documentation on how AWS Transfer Family uses Amazon Route 53 for custom domain names (applicable to internet facing endpoints only).')],
}
D['transfer-family-faq-sftp-connectors-up-to-5-concurrent-connections'] = {
    'reason': 'entail partial: adjustability is not supported; the value is a connector setting, so kind changed from limit to capability.',
    'kind': 'capability',
    'qual': {'adjustable': False},
}
D['transfer-family-faq-sftp-ssh-keys-per-user-10'] = {
    'reject': True,
    'reason': 'entail partial: the FAQ value of 10 conflicts with the quotas table (50 SSH keys per service-managed user, transfer-family-quota-ssh-keys-per-service-managed-user); key types are in transfer-family-ssh-key-types-rsa-ecdsa-ed25519.',
}
D['transfer-family-faq-stopped-server-still-billed'] = {
    'reason': 'entail partial: the configure-access condition of the billing start added.',
    'claim': 'A stopped Transfer Family server is still billed: stopping it in the console, with the stop-server CLI command or the StopServer API does not impact billing, which is hourly from the time you create the server endpoint and configure access to it over one or more protocols until you delete it.',
}
D['transfer-family-faq-unsupported-file-operations'] = {
    'reason': 'entail partial: added the sentences that place the answer in Amazon S3 storage; protocol scope removed.',
    'claim': 'For Transfer Family users whose files are stored in Amazon S3, common commands to create, read, update and delete files and directories are supported, but directory rename operations, append operations, changing ownerships, permissions and timestamps, and use of symbolic and hard links are currently not supported.',
    'qual': {'scope': 'AWS Transfer Family users with Amazon S3 storage', 'condition': ''},
    'evidence': [ev('www/aws-transfer-family/faqs',
                    'Common commands to create, read, update, and delete, files and directories are supported. Files are stored as individual objects in your Amazon S3 bucket. Directories are managed as folder objects in S3, using the same syntax as the S3 console.'), 0],
}
D['transfer-family-s3-directories-inferred-from-object-keys'] = {
    'reason': 'entail partial: quote extended with the first-class-concept sentence.',
    'evidence': [ev('docs/transfer/latest/userguide/configure-storage',
                    'For example, directories are not a first-class concept in Amazon S3 but instead are based on object keys. AWS Transfer Family infers a directory path by splitting an object\'s key by the forward slash character (**/**), treating the last element as the file name, then grouping file names which have the same prefix together under the same path.')],
}
D['transfer-family-sftp-connector-quota-pending-queue-size'] = dict(
    reason='entail partial: the ThrottlingException condition is not in the quote; removed.',
    **cond_drop('adjudicate-25: exceeding the queue returns a ThrottlingException (not quoted).'))
D['transfer-family-sftp-connector-rate-100-file-paths-per-second'] = {
    'reason': 'entail partial: adjustability now rests on the quoted General Reference row.',
    'claim': 'You can request up to 100 file paths per second for transfer with each SFTP connector; the General Reference quota Rate of StartFileTransfer files per SFTP connector is 100 per second and adjustable.',
    'qual': {'condition': ''},
    'evidence': [0, ev('docs/general/latest/gr/transfer-service',
                       '| Rate of StartFileTransfer files per SFTP connector | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/transfer/quotas/L-57D537DE)  | Maximum number of StartFileTransfer files sent per second per SFTP connector |',
                       table_header='| Name | Default | Adjustable | Description |')],
}
D['transfer-family-storage-s3-or-efs'] = dict(
    reason='entail partial: the FSx for ONTAP condition is not in the quote; removed.',
    **cond_drop('adjudicate-25: since January 2026 Amazon FSx for NetApp ONTAP is reached through S3 access points (transfer-family-change-fsx-for-ontap-2026-01).'))
D['transfer-family-tls-12-required-clients-pfs-cipher-suites'] = {
    'reason': 'entail partial: added the lead-in sentence (API calls, clients must support).',
    'evidence': [ev('docs/transfer/latest/userguide/infrastructure-security',
                    'You use AWS published API calls to access AWS Transfer Family through the network. Clients must support the following:'), 0, 1],
}
D['transfer-family-web-app-vpc-endpoint-private-s3-without-public-internet'] = {
    'reason': 'entail partial: the three extra components of the note added; date condition removed.',
    'claim': 'You can host a Transfer Family web app\'s endpoint inside a VPC to transfer data to and from an Amazon S3 bucket without going over the public internet; to ensure a private end-to-end data flow you must implement three additional components: a PrivateLink endpoint for Amazon S3 Control API operations, an endpoint for Amazon S3 data access, and bucket policies that only permit traffic from these VPC endpoints.',
    'qual': {'condition': ''},
    'hard': True,
    'question': 'What do you need so that a Transfer Family web app in a VPC keeps its data flow to Amazon S3 private?',
    'evidence': [0, ev('docs/transfer/latest/userguide/create-webapp-in-vpc',
                       'To ensure a private end-to-end data flow when using a Transfer Family web app VPC endpoint, you must implement three additional components. First, set up a PrivateLink endpoint for Amazon S3 Control API operations, which is necessary for Amazon S3 Access Grants API calls.'),
                 ev('docs/transfer/latest/userguide/create-webapp-in-vpc',
                    'Third, lock down your Amazon S3 bucket access by updating the bucket policies to only permit traffic from these VPC endpoints.')],
}


def load_fact(fid):
    for svc in ['datasync', 'snow-family', 'storage-gateway', 'transfer-family']:
        if fid.startswith(svc + '-'):
            for line in open(BOOK + 'data/facts/%s.jsonl' % svc):
                if line.strip():
                    f = json.loads(line)
                    if f['id'] == fid:
                        return f
    raise KeyError(fid)


def url_of(source_id):
    meta = json.load(open(BOOK + '_build/corpus/snap/%s.meta.json' % source_id))
    return meta['url']


def build_patch(fid, d):
    f = load_fact(fid)
    p = {}
    if 'claim' in d:
        p['claim'] = d['claim']
    if 'values' in d:
        p['values'] = d['values']
    if 'kind' in d:
        p['kind'] = d['kind']
    for k in ('hard', 'question'):
        if k in d:
            p[k] = d[k]
    if 'qual' in d:
        q = dict(f['qualifiers'])
        q.update(d['qual'])
        p['qualifiers'] = q
    if 'evidence' in d:
        evs = []
        for e in d['evidence']:
            if isinstance(e, int):
                old = f['evidence'][e]
                n = {k: old.get(k) for k in ('source_id', 'url', 'quote', 'table_header')}
                if old.get('heading'):
                    n['heading'] = old['heading']
            else:
                n = dict(e)
                n['url'] = url_of(n['source_id'])
            evs.append(n)
        p['evidence'] = evs
    if 'note_add' in d:
        old = f.get('note') or ''
        p['note'] = (old + ' ' + d['note_add']).strip()
    return p


def main():
    dry = '--dry-run' in sys.argv
    only = None
    if '--only' in sys.argv:
        only = set(sys.argv[sys.argv.index('--only') + 1].split(','))
    os.makedirs(HERE + 'patches', exist_ok=True)
    log = open(HERE + ('amend-dry.jsonl' if dry else 'amend-log.jsonl'), 'a')
    ok = bad = 0
    for fid, d in D.items():
        if only and fid not in only:
            continue
        cmd = ['python3', 'aws-saa-book/tools/saa.py', 'facts', 'amend', fid]
        if d.get('reject'):
            if dry:
                continue
            cmd += ['--reject', '--reason', 'adjudicate-25: ' + d['reason'], '--by', BY]
        else:
            p = build_patch(fid, d)
            pf = HERE + 'patches/%s.json' % fid
            json.dump(p, open(pf, 'w'), indent=1, ensure_ascii=False)
            cmd += ['--file', 'aws-saa-book/_build/work/25-hybrid-storage/adjudicate/patches/%s.json' % fid,
                    '--reason', 'adjudicate-25: ' + d['reason'], '--by', BY]
            if dry:
                cmd.append('--dry-run')
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        rec = {'id': fid, 'rc': r.returncode, 'out': r.stdout[-1500:], 'err': r.stderr[-1500:]}
        log.write(json.dumps(rec) + '\n')
        if r.returncode == 0:
            ok += 1
        else:
            bad += 1
            print('FAIL', fid, r.returncode, (r.stderr or r.stdout)[-600:])
    print('ok', ok, 'failed', bad, 'decisions', len(D))


if __name__ == '__main__':
    main()
