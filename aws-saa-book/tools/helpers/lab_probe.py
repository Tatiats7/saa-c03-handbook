#!/usr/bin/env python3
"""Development probe for the lab module: runs the CLI model helper on a few sample commands.

    python3 aws-saa-book/tools/helpers/lab_probe.py

It is the "one uv run of the helper" that TOOLS-rules.md R6 asks for before the version is pinned.
"""
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SAMPLES = [
    "aws ec2 run-instances --image-id ami-1 --instance-type t3.micro --launch-template LaunchTemplateName=x "
    "--tag-specifications 'ResourceType=instance,Tags=[{Key=book,Value=saa}]'",
    "aws ec2 run-instances --image-idd ami-1",
    "aws ec2 create-vpc --cidr-block 10.0.0.0/16 --query Vpc.VpcId --output text",
    "aws ec2 wait instance-running --instance-ids $ID",
    "aws ec2 describe-instances --filters Name=tag:book,Values=saa --region eu-west-1",
    "aws s3 cp a.txt s3://saa-bucket/a.txt --sse aws:kms",
    "aws s3api create-bucket --bucket saa-x",
    "aws s3api put-bucket-tagging --bucket saa-x",
    "aws widget list-shelves",
    "aws ec2 make-coffee",
    "aws sts get-caller-identity",
    "aws configure list",
    "aws kms create-key --tags TagKey=book,TagValue=saa",
    "aws sqs create-queue --queue-name saa-q --tags book=saa,task=x-t01",
    "aws --region eu-west-1 sqs list-queues",
    "curl https://example.com",
]
if len(sys.argv) > 1 and sys.argv[1] == "emulate":
    task = {"task": "probe-t01",
            "steps": [{"command": "aws sqs create-queue --queue-name saa-probe --tags book=saa,task=probe-t01",
                       "capture": {"name": "QUEUE_URL", "query": "QueueUrl"}, "break_it": False},
                      {"command": "aws sqs get-queue-attributes --queue-url $QUEUE_URL-missing", "capture": None, "break_it": True},
                      {"command": "aws sqs get-queue-attributes --queue-url $QUEUE_URL --attribute-names All", "capture": None, "break_it": False}],
            "cleanup": ["aws sqs delete-queue --queue-url $QUEUE_URL"],
            "verify": "aws sqs list-queues --queue-name-prefix saa-"}
    start = time.time()
    proc = subprocess.run(["uv", "run", "--script", str(HERE / "emulate.py")], input=json.dumps(task),
                          capture_output=True, text=True, timeout=900)
    print("rc", proc.returncode, "seconds", round(time.time() - start, 1))
    print(proc.stdout[-2500:] if proc.returncode == 0 else proc.stderr[-3000:])
    sys.exit(proc.returncode)

start = time.time()
proc = subprocess.run(["uv", "run", "--script", str(HERE / "cli_model.py")], input=json.dumps(SAMPLES),
                      capture_output=True, text=True, timeout=600)
print("rc", proc.returncode, "seconds", round(time.time() - start, 1))
if proc.returncode != 0:
    print(proc.stderr[-3000:])
    sys.exit(1)
data = json.loads(proc.stdout)
print("awscli", data["awscli"])
for r in data["results"]:
    print("OK  " if r["ok"] else "FAIL", r["service"], "|", r["operation"], "|", r["errors"], "|", r["tag_options"])
