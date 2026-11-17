---
id: "00"
slug: start-here
title: Start here and study calendar
file: fast
tier: front
domains: []
tasks: []
services: []
minutes: {fast: 12, pass: 12, full: 25}
status: ready
updated: 2026-10-11
---

# Start here and study calendar

## What you get (2 min)
<!-- section: role=orient; route=fast; minutes=2 -->

This book prepares you for the exam [AWS Certified Solutions Architect - Associate (SAA-C03)](../facts/exam.md#exam-name-and-code). The exam has [65 questions](../facts/exam.md#exam-question-count) in [130 minutes](../facts/exam.md#exam-duration-minutes). In its September 2026 update, AWS Certification is [updating three exams](../facts/exam.md#exam-current-version-saa-c03), and [Solutions Architect - Associate (SAA-C03)](../facts/exam.md#exam-current-version-saa-c03) is not one of them. So SAA-C03 is the exam you take.

A **resilient** (rih-ZIL-yent) architecture recovers from a failure and keeps working.

<!-- table: plain -->
| Domain | Share of scored content |
|---|---|
| Design Secure Architectures | [30% of scored content](../facts/exam.md#exam-domain-weights) |
| Design Resilient Architectures | [26% of scored content](../facts/exam.md#exam-domain-weights) |
| Design High-Performing Architectures | [24% of scored content](../facts/exam.md#exam-domain-weights) |
| Design Cost-Optimized Architectures | [20% of scored content](../facts/exam.md#exam-domain-weights) |

Your diagnostic of 2026-09-18 was weakest in Secure, at 45%. <!-- no-fact: plan --> Secure is also the largest domain, so the calendar puts security first.

- Chapters 00 to 02: start here.
- Chapters 03 to 43: services and patterns.
- Chapters 44 to 49 and 52: synthesis and review sheets.
- Chapters 50 and 51: the book's own mock exams.

## Three routes (2 min)
<!-- section: role=orient; route=fast; minutes=2 -->

The calendar gives each service chapter a route. Most get Pass before the exam. A deep chapter covers a large service; a medium chapter, a smaller one.

<!-- table: plain -->
| Route | What you do | Deep chapter | Medium chapter |
|---|---|---|---|
| Fast | Read `1-fast.md` | About 20 minutes | About 12 minutes |
| Pass | Fast, the core questions, the subsections your misses point to, one spoken answer | About 50 minutes; 65 minutes for 03 IAM, 10 VPC, 16 EC2 and 21 S3 | About 22 minutes |
| Full | Every file, with the tasks in `3-do.md`; mostly after you pass | About 2 to 3 hours | About 1 hour |

On the Pass route, read only the `2-deep.md` subsections that your wrong answers in `5-quiz.md` point to. Then give one spoken answer from `4-say.md`.

Each chapter states its own minutes at the top of its first file and in the web version. When the chapter and this table differ, use the chapter.

## How a chapter works (3 min)
<!-- section: role=orient; route=fast; minutes=3 -->

A chapter is a folder of short files:

- `1-fast.md`: the short version, read first.
- `2-deep.md`: how it works, numbers, decision record, FAQ quick-fire.
- `3-do.md`: tasks in AWS CloudShell.
- `4-say.md`: spoken answers.
- `5-quiz.md`: questions.
- `sources.md`: the AWS pages behind the facts.

Parts you meet first:

- **Predict:** guess before you read. A guess is not scored.
- **Signals and traps:** the "But not if" column stops keyword matching.
- **Stop and answer:** a new case after each How-it-works subsection.
- **Go deeper:** a collapsed block with edge cases.
- **Changed recently:** old value, new value, and what older questions can assume.

> **Exam trap:** It is tempting to choose a feature that AWS launched last month. A new feature must be [generally available for 3 months](../facts/exam.md#exam-new-feature-wait) before it appears on an exam. This book labels a newer feature "not examinable yet". <!-- trap: start-here-trap-new-feature-examinable -->

Each exam question asks you to select the responses that [best complete the statement or answer the question](../facts/exam.md#exam-select-best-response-instruction). The **stem** is the scenario part of a question, before the options. The constraint in the stem, such as lowest cost, picks the best of the options that work. Find it first, then read the options.

The chapters follow Callvale, a fictional startup founded by Ana and Ben.

Every spoken answer uses four moves:

<!-- table: plain -->
| Move | Start with |
|---|---|
| Answer | "The short answer is ..." |
| How | "It works like this ..." |
| Watch | "The thing to watch is ..." |
| You | "In your case ...", then ask one question back |

Speak for 10 minutes every day. First read the 60-second model answer aloud. Then answer without the text, with a 90-second timer.

## Do this today (2 min)
<!-- section: role=plan; route=fast; minutes=2 -->

1. **Request ESL +30 first.** [ESL +30](../facts/exam.md#exam-esl-accommodation) (English as a second language) is a [30-minute exam extension](../facts/exam.md#exam-esl-accommodation) for non-native English speakers who take the exam in English. It [only needs to be requested once](../facts/exam.md#exam-esl-accommodation), before you register. Sign in at [aws.training/Certification](../facts/exam.md#exam-certification-account), your AWS Certification Account, [separate from your AWS account](../facts/exam.md#exam-certification-account). Choose `Go to your Account` > `Request Exam Accommodations` > `Request Accommodation`, select `ESL +30 MINUTES`, then `Create`.
2. **Take the free official practice set.** Use the SAA-C03 set of the free [20-question sets](../facts/exam.md#exam-official-practice-question-sets) on AWS Skill Builder as your baseline. Write each miss into `mistakes.md`.
3. **Then choose a plan in `calendar.md`, check your deadline, and book.** Use a [Pearson VUE](../facts/exam.md#exam-testing-options) test center or online proctoring, and look for a [50% discount on your next AWS Certification exam](../facts/exam.md#exam-discount-next-exam).

> **Exam trap:** It is tempting to book first, add [ESL +30](../facts/exam.md#exam-esl-accommodation) later, and request it again for each exam. Request it before you register. It will [apply to all future exam registrations](../facts/exam.md#exam-esl-accommodation). <!-- trap: start-here-trap-esl-after-booking -->

## Recap from memory (3 min)
<!-- section: role=recap; route=fast; minutes=3 -->

**Recap 1.** What do you request before booking, and where?

<details>
<summary>Answer</summary>

[ESL +30](../facts/exam.md#exam-esl-accommodation), in your AWS Certification Account.

</details>

**Recap 2.** Which route do most chapters get before the exam?

<details>
<summary>Answer</summary>

Pass: Fast, core questions, the subsections your misses point to, a spoken answer.

</details>

**Recap 3.** What are the four spoken moves?

<details>
<summary>Answer</summary>

Answer, How, Watch, You, then a question back.

</details>
