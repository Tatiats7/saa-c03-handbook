---
chapter: "02"
file: services
title: The AWS map tools to recognize
status: ready
updated: 2026-10-12
---

# The AWS map tools to recognize

## AWS CLI (1 min)
<!-- section: role=card; route=full; minutes=1; service=aws-cli -->

**Say the name.** A-W-S C-L-I.

**What it is.** The AWS CLI is [an open source tool that enables you to interact with AWS services using commands in your command-line shell](../facts/aws-cli.md#aws-cli-definition-open-source-command-line-tool). It gives you [functionality equivalent to that provided by the browser-based AWS Management Console](../facts/aws-cli.md#aws-cli-definition-open-source-command-line-tool).

**Stem signals.**

- "automate the task with scripts"
- "run the commands from a terminal"
- "without storing long-term access keys" (AWS CloudShell, or short-term credentials)

**Do not confuse with.** AWS CloudShell: a terminal inside the console, signed in as you. [The AWS CLI is pre-installed on the shell's compute environment](../facts/management-console.md#management-console-cloudshell-console-credentials-no-configuration).

**One fact.** The CLI guide does not recommend the access keys of an IAM user: [(Not recommended) Use long-term credentials, which have no expiration](../facts/aws-cli.md#aws-cli-long-term-iam-user-credentials-not-recommended). Instead: [Use short-term credentials by logging into the AWS CLI with your console credentials](../facts/aws-cli.md#aws-cli-recommended-short-term-console-credentials).

> **Say it:** The AWS CLI does from a terminal what the console does in a browser. Use short-term credentials, not stored keys.

**Source.** [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)

## AWS Management Console (1 min)
<!-- section: role=card; route=full; minutes=1; service=management-console -->

**What it is.** The console is a web application with [centralized access to all individual AWS service consoles](../facts/management-console.md#management-console-console-unified-navigation-features). Its Unified Navigation lets you [search for services, view notifications, access AWS CloudShell, access account and billing information, and customize your general console settings](../facts/management-console.md#management-console-console-unified-navigation-features).

**Stem signals.**

- "a web-based interface" to manage resources
- "run AWS CLI commands from the browser" (AWS CloudShell)
- "limit the console to known AWS accounts for traffic from the VPC" (Console Private Access)

**Do not confuse with.** AWS CLI: the same actions from a terminal, so you can put them in scripts and run them again.

**One fact.** AWS CloudShell is [a browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console](../facts/management-console.md#management-console-cloudshell-browser-based-pre-authenticated). You run CLI commands there without creating access keys.

> **Say it:** The console is the browser front door to every AWS service, and CloudShell gives you a signed-in terminal inside it.

**Source.** [What is the AWS Management Console?](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/what-is.html)
