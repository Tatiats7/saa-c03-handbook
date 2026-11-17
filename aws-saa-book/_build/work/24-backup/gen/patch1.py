import json
json.dump({
 "claim": "After you enable AWS Backup's advanced DynamoDB features in a Region, DynamoDB backups inherit the tags of their source tables, so you can use those tags to set permissions and service control policies.",
 "values": [{"key": "v1", "display": "Backups inherit tags from their source DynamoDB tables"}, {"key": "v2", "display": "service control policies (SCPs)"}]
}, open('/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup/patch-ddb-benefits.json','w'), indent=1)
