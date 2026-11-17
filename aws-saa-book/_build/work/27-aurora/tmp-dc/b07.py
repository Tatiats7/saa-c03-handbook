import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/27-aurora/tmp-dc")
from mk import F, write
facts = [
 F("aurora-pitr-aws-backup-plan-used-for-point-in-time-recovery", "behavior",
   "If an Aurora DB cluster is associated with a backup plan in AWS Backup, that backup plan is used for point-in-time recovery.",
   "Which backup plan is used for point-in-time recovery when an Aurora cluster is also in AWS Backup?",
   [("plan", "that backup plan is used for point-in-time recovery")],
   "Aurora DB cluster point-in-time recovery", "", False, "docs/AmazonRDS/latest/AuroraUserGuide/aurora-pitr",
   "If your DB cluster is associated with a backup plan in AWS Backup, that backup plan is used for point-in-time recovery.",
   cond="since September 2023 Aurora automated (continuous) backups can be managed in AWS Backup", exam="extended", bullets=["2.2.K6", "4.3.S3"], vol="stable",
   hard=False, change_items=["docs/AmazonRDS/latest/AuroraUserGuide/WhatsNew#84"], note="d27-073. Chapter 24 owns AWS Backup."),
]
write("facts-decisions-07.json", facts)
