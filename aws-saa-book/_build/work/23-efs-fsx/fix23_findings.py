"""fix-23: record status and resolution of every finding of chapter 23."""
import json
from pathlib import Path

DIR = Path(__file__).resolve().parent / "findings"
P = "fix-23: "
EXPL = " (explanation only; stem, options and key unchanged, so the passed blind verification stands; q lint --ship clean)"

R = {
 "claims": {
  "claims-23-01": ("fixed", "q015 option a why now reads: 'This configuration does not exist: backups are supported only on FSx for Lustre persistent file systems not linked to an Amazon S3 data repository. Its data is replicated too, which this job does not need.' Think-aloud steps 4 and 5 now remove both backup options for the same reason; fact fsx-lustre-backups-persistent-only-not-s3-linked-not-scratch added to the question's facts." + EXPL),
  "claims-23-02": ("fixed", "FAQ 2 now asks 'Does EFS IA have a minimum storage duration?' Answer: 'No: EFS IA has no minimum storage duration. Reads from IA still have billed data access charges' (efs-ia-archive-billed-per-class-plus-access-charges)."),
  "claims-23-03": ("fixed", "Item lints clean; cards c001-c032, speak s01-s04 and tasks t01-t03 set to ready with set-status (--by fix-23); sync 23 regenerated 3-do.md, 4-say.md, 5-quiz.md and the t01 region in 1-fast.md Look first."),
  "claims-23-04": ("fixed", "The exam-expects line now says: 'older questions can use a lower limit, and you can request an increase. Do not choose on the count alone.' It no longer claims an option is right under both values. The 2023 change from 120 to 1,000 has no fact in the canon, so no value is stated for it."),
  "claims-23-05": ("fixed", "The exam-expects line of the Archive entry now says older questions know only EFS Standard and EFS IA, 'not the file system types Regional and One Zone' (the same change record, efs-change-archive-storage-class-and-file-system-types-2023-11, adds file system types)."),
  "claims-23-06": ("fixed", "1-fast hero step 1 and 2-deep mount-target step 2 now say 'Domain Name System (DNS) name' outside the link; the hero spec say was changed to match and efs-fsx-hero.svg rebuilt (diagram build). The 'resolves to the IP address of the EFS' link keeps the fact."),
  "claims-23-07": ("fixed", "2-deep throughput: 'You can change the throughput mode later; after a move to Provisioned, wait at least 24 hours before the next change' (efs-provisioned-24-hour-wait-before-switch-or-decrease). The Archive block is now lifecycle step 3: 'When a policy moves files to Archive, you cannot change the throughput mode to Bursting or Provisioned' (efs-archive-needs-elastic-throughput-no-bursting-provisioned)."),
  "claims-23-08": ("fixed", "Stop and answer now: 'A 50 GiB Bursting file system serves a job that reads at one high rate all day, and it has no burst credits left.' Answer: Provisioned, because the load is steady."),
  "claims-23-09": ("fixed", "The question now asks 'Which servers pay data transfer charges between zones?'"),
  "claims-23-10": ("fixed", "Say it now: 'security groups decide who connects; a file system policy decides who mounts. The thing to watch is the open default policy.' The line before it keeps the fact that the default policy grants full access to any anonymous client."),
  "claims-23-11": ("rejected", "The canon has no fact for the aws:SecureTransport condition key, and a new fact needs the entail vote pipeline, which a fix stage cannot run. The Exam signal sentence as written is correct and linked. Left as a gap for the security drill or a later facts run (no fact request filed, so finalize is not blocked)."),
  "claims-23-12": ("fixed", "Replication vs Backup table: the Keeps cell now reads 'In the default backup plan, daily backups with a 35-day retention period'; a new row 'On for a new file system?' says 'Console: yes. CLI or API: enabled by default only for One Zone' (efs-backup-cli-api-default-only-one-zone). The unlinked 'Protects against' row was removed."),
  "claims-23-13": ("removed", "The price comparison is gone. Trade-off now states the story's own reason: 'The old file code stays for now. Reports move to Amazon S3 when the code is rewritten.'"),
  "claims-23-14": ("fixed", "Decision now links elb-alb-sticky-sessions-what: 'Sticky sessions bind a user's session to a specific target; a colleague's download is another session. Amazon S3 needs a code change that cannot happen this year.'"),
  "claims-23-15": ("fixed", "s04 follow-up answer now: 'While the file system has a lifecycle policy that moves data to Archive, you cannot change the throughput mode to Bursting or Provisioned.'"),
  "claims-23-16": ("fixed", "t03 verify expect adds a check without tags: describe-file-systems --creation-token saa-efs-fsx-t03 (us-east-1) and --file-system-id $DEST_ID (us-west-2) each return FileSystemNotFound once deleted (docs/efs/latest/APIReference/API_DeleteFileSystem: 'If you pass file system ID or creation token for the deleted file system, the DescribeFileSystems returns a 404 FileSystemNotFound error'). The tagging-API fact stays disputed; the T108 by-name exception does not accept a creation token, so the tag filter stays the primary verify."),
  "claims-23-17": ("fixed", "FAQ 7 now adds 'not linked to an Amazon S3 data repository' with its link."),
  "claims-23-18": ("fixed", "Row now reads 'Regional, across multiple geographically separated Availability Zones, or One Zone, in one zone'."),
  "claims-23-19": ("fixed", "Stop and answer now: 'A short-term job of three days ... Which deployment type costs the least?' Answer names 'cost-optimized storage for short-term, processing-heavy workloads', that data is not replicated, and to export the results. The persistent cell of the table now links 'sensitive to disruptions in availability'."),
  "claims-23-20": ("fixed", "1-fast: ONTAP cell now links 'primary storage and capacity pool storage' and 'migrate your NetApp ONTAP file systems'; OpenZFS clients cell says 'all over NFS'. 2-deep protocol row explains iSCSI (block storage) and the custom POSIX-compliant Lustre protocol. Cells with no number or absolute word stay unlinked."),
  "claims-23-21": ("fixed", "Step now: 'Each volume's tiering policy decides what moves there, some after a cooling period'. Table adds Snapshot-only ('moves only snapshot data'; AWS CLI and API default) and marks Auto as the console default."),
  "claims-23-22": ("fixed", "Check 3 answer: 'Only the files it reads: content is imported automatically from S3 only when you access the file. The file list comes first.' 2-deep 'Why load lazily?' and the s03 ten-second answer say the same."),
  "claims-23-23": ("fixed", "q007 /tmp why: 'the files are not guaranteed to persist'." + EXPL),
  "claims-23-24": ("rejected", "t02 step 3 reads the lifecycle policies back (TransitionToPrimaryStorageClass AFTER_1_ACCESS) and its expect states the trap ('Without the third entry, a file that someone reads stays in EFS IA or EFS Archive'). No brief trap covers throughput switching; re-pointing the trap id needs a brief change by the orchestrator."),
  "claims-23-25": ("fixed", "Now: 'A file system gives every client the same folders and files, with strong consistency and file locking' (efs-faq-efs-semantics-strong-consistency-locking)."),
  "claims-23-26": ("fixed", "q012 b why links ebs-gp3-use-cases ('medium sized single instance databases'); d why links ebs-gp3-lowest-cost-ssd and ebs-io2-use-cases; the three facts added." + EXPL),
  "claims-23-27": ("fixed", "Answer now: 'To go from SSD to HDD, restore a backup to a new file system that uses HDD' with the fact link."),
  "claims-23-28": ("fixed", "Step 2 now lists the three triggers, each with the fact link."),
  "claims-23-29": ("fixed", "q005 explanation adds: 'Backups do not decide it; from the CLI they are enabled by default only for One Zone' (efs-backup-cli-api-default-only-one-zone, added to facts)." + EXPL),
  "claims-23-30": ("fixed", "Cell now reads 'No: using EFS with Microsoft Windows-based Amazon EC2 instances is not supported'."),
  "claims-23-31": ("fixed", "Step 4 adds that on-premises servers 'must have a Linux-based operating system' (efs-onpremises-server-must-be-linux)."),
  "claims-23-32": ("fixed", "'within minutes' removed from the Why-both line (step 3 links the 15-minute RPO). A-list cell now says what the RPO means: 'Data a failover can lose'."),
 },
 "exam": {
  "exam-01": ("fixed", "Same fix as claims-23-01: option a why now says the configuration does not exist, and think-aloud step 5 no longer says the job avoids paying for backups. The option text is unchanged, so the passed verification stands; the question now has two impossible-feature distractors, which still leaves one key."),
  "exam-02": ("fixed", "2-deep Stop and answer fixed (short-term three-day job, 'costs the least'). The q015 stem keeps 'short-lived ... for two weeks': a stem change resets verification, and the key does not depend on it (all three solvers chose d; scratch is the lowest-cost option that meets the stated constraints). Stem wording left for the next question revision."),
  "exam-03": ("fixed", "Shipped set changed with q set-status: ready q013 (d1, core), q021 (d3, multi), q019 (d3); back to verified q014, q008, q004. Mix now d1 3, d2 10, d3 5 (0.17/0.56/0.28, inside tolerance); 9 core, 9 extended; multi q012, q017, q021; twin pairs q001/q006, q005/q009; every bullet keeps a question (4.1.K7 moves to q019). q lint --ship clean."),
  "exam-04": ("fixed", "q013 (4.1.S4) is shipped (see exam-03)."),
  "exam-05": ("fixed", "q021 (cross-Region replication DR) is shipped (see exam-03)."),
  "exam-06": ("rejected", "Needs a new question slot (brief change by the orchestrator) and a blind-panel run; not possible in fix. Reported as a gap for the security drill. The prose now has an access-point step (reader-14)."),
  "exam-07": ("fixed", "Go deeper: 'Max I/O is a previous generation mode ... It is not supported for One Zone file systems or file systems that use Elastic throughput' (efs-max-io-not-supported-one-zone-or-elastic). No claim about older practice items is made (memory is not evidence)."),
  "exam-08": ("fixed", "But-not-if cell now: 'tiny files: one smaller than 128 KiB is billed at that size' (efs-faq-ia-archive-128-kib-billing). The Archive guard is in 2-deep lifecycle step 3."),
  "exam-09": ("fixed", "Tiering table adds Snapshot-only (AWS CLI and API default) and marks Auto as the console default; the Say it names the difference."),
  "exam-10": ("fixed", "But-not-if cell now: 'no compute job, only shared Linux files: Amazon EFS'."),
  "exam-11": ("rejected", "2-deep is at its 4,500-word limit after the fixes and DataSync belongs to the migration chapter; the speak item s02 already names DataSync with a verified fact. Left for chapter 25."),
  "exam-12": ("fixed", "Same fix as claims-23-29 (explanation only)."),
 },
 "reader": {
  "reader-01": ("fixed", "Same fix as claims-23-02."),
  "reader-02": ("fixed", "Same fix as claims-23-03."),
  "reader-03": ("fixed", "Table header is now 'Average throughput compared with peak'; rows 'Low or spiky: 5% or less of the peak throughput' and 'Steady: 5% or more of the average-to-peak ratio, or you know your workload's performance requirements'."),
  "reader-04": ("fixed", "Bursting step now: 'It spends burst credits, deducted when throughput exceeds the base rate' (efs-bursting-credits-accrue-below-base-and-deducted-above)."),
  "reader-05": ("fixed", "Lifecycle step 3 'Archive needs Elastic' with efs-faq-archive-regional-elastic-only and efs-archive-needs-elastic-throughput-no-bursting-provisioned."),
  "reader-06": ("fixed", "1-fast OpenZFS clients cell: 'Windows, Linux and macOS, all over NFS'; 2-deep OpenZFS trap truth adds 'so a Windows client of OpenZFS uses NFS'."),
  "reader-07": ("fixed", "Protocol row explains iSCSI (block storage over the network) and the custom POSIX-compliant Lustre protocol; the unused SVM step is removed; throughput capacity gets a clause; capacity pool storage is explained in the ONTAP step; 1-fast links capacity pool storage and SnapMirror to facts."),
  "reader-08": ("rejected", "The terms sit in verified question stems and options (changing them resets verification) and in the t01 expect; 2-deep is at its word limit. Single-AZ 2 and failover cluster instances are distractor or stem context, not the key."),
  "reader-09": ("fixed", "Check 1 is now a transfer item (NFS and SMB on the same files: ONTAP); Check 2 asks where a report is on day 7 with default settings. The 2-deep Stop-and-answer items stay."),
  "reader-10": ("fixed", "Persistent cell: 'Long jobs sensitive to disruptions in availability'; the Stop and answer is now a short-term, lowest-cost question (see claims-23-19)."),
  "reader-11": ("fixed", "Watch-points are now full clauses ('that it copies mistakes too', 'that Lustre serves Linux clients', 'that Linux clients wait for failback', 'that scratch data is not replicated', 'that read files stay there', 'the default tiering policy: console and CLI differ'); all Say it callouts are within 25 words."),
  "reader-12": ("fixed", "s03 sixty-second answer now opens 'The short answer is no: link FSx for Lustre to the bucket instead.'"),
  "reader-13": ("fixed", "Cards c003 and c023 say 'a lifecycle policy with default settings'; s04 kp2 says 'With a lifecycle policy at default settings'."),
  "reader-14": ("fixed", "Security step 5 'Scope': an EFS access point can enforce a different root directory for one application."),
  "reader-15": ("fixed", "Same fix as claims-23-06."),
  "reader-16": ("fixed", "Lifecycle intro now 'read often for some weeks and then rarely'; step 1 says 'Move when unread'; the ONTAP table says 'Unread data'. The heading word 'Cold' is fixed by the brief."),
  "reader-17": ("fixed", "Step 4 now: 'You delete the replication configuration, and then the replica becomes writeable.'"),
  "reader-18": ("fixed", "Intro now names Amazon EBS: 'An Amazon EBS volume must be in the same Availability Zone as its instance. EFS gives each Availability Zone (AZ) a network address instead.'"),
  "reader-19": ("rejected", "Both lines rest on verified facts (fsx-windows-migrate-with-datasync-or-robocopy, fsx-windows-dns-aliases-keep-existing-names); 2-deep is at its word limit, so no sentence was added there."),
  "reader-20": ("fixed", "Decision now gives the reason against S3 ('needs a code change that cannot happen this year'); the decision record is back under its word budget (no W201)."),
 },
}

for lens, table in R.items():
    path = DIR / f"{lens}.json"
    doc = json.loads(path.read_text(encoding="utf-8"))
    seen = set()
    for row in doc["findings"]:
        if row["id"] in table:
            status, text = table[row["id"]]
            row["status"] = status
            row["resolution"] = P + text
            seen.add(row["id"])
    missing = [r["id"] for r in doc["findings"] if r["id"] not in seen]
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(lens, "updated", len(seen), "missing", missing)
