---
id: "01"
slug: how-the-exam-asks
title: How the exam asks, and exam English
file: fast
tier: front
domains: []
tasks: []
services: []
minutes: {fast: 10, pass: 23, full: 56}
status: ready
updated: 2026-10-12
---

# How the exam asks, and exam English

## Predict (1 min)
<!-- section: role=predict; route=fast; minutes=1 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** A question asks for the MOST cost-effective solution. Two options meet every requirement. A third option is cheaper, but it misses one requirement. Which option is the answer? <!-- gist-trap -->

**Predict 2.** The exam has 65 questions. How many of them count toward your score?

## What the exam measures (2 min)
<!-- section: role=orient; route=fast; minutes=2 -->

[AWS Certified Solutions Architect - Associate (SAA-C03)](../facts/exam.md#exam-name-and-code) tests whether you can [design solutions based on the AWS Well-Architected Framework](../facts/exam.md#exam-validates-well-architected).

<!-- table: plain -->
| Exam fact | Value |
|---|---|
| Questions | [65 questions](../facts/exam.md#exam-question-count) |
| Scored | [50 questions that affect your score](../facts/exam.md#exam-question-count) |
| Unscored | [15 unscored questions](../facts/exam.md#exam-question-count), [not identified on the exam](../facts/exam.md#exam-unscored-questions-not-identified) |
| Time | [130 minutes](../facts/exam.md#exam-duration-minutes) |
| Extra time in English | [ESL +30](../facts/exam.md#exam-esl-accommodation): a [30-minute exam extension](../facts/exam.md#exam-esl-accommodation) for non-native English speakers |
| Passing score | [720 on a scale of 100 to 1,000](../facts/exam.md#exam-passing-score) |
| Design Secure Architectures | [30% of scored content](../facts/exam.md#exam-domain-weights) |
| Design Resilient Architectures | [26% of scored content](../facts/exam.md#exam-domain-weights) |
| Design High-Performing Architectures | [24% of scored content](../facts/exam.md#exam-domain-weights) |
| Design Cost-Optimized Architectures | [20% of scored content](../facts/exam.md#exam-domain-weights) |
| Retake after a fail | [14 calendar days](../facts/exam.md#exam-retake-wait) |
| Where | Online or at a test center, through [Pearson VUE](../facts/exam.md#exam-testing-options) |
| Results | [within five business days](../facts/exam.md#exam-results-timing) |
| On screen | most exams [do not display your pass/fail result at the end of the test](../facts/exam.md#exam-no-result-on-screen) |

Design Secure Architectures has the largest share, and it was your weakest domain in the diagnostic.

- **Wrong belief:** You must pass each domain to pass the exam. **Truth:** The exam uses a [compensatory scoring model](../facts/exam.md#exam-compensatory-scoring): you need to [pass only the overall exam](../facts/exam.md#exam-compensatory-scoring). <!-- trap: how-the-exam-asks-trap-pass-each-domain -->
- **Wrong belief:** A score of 720 means that 72 percent of the answers were correct. **Truth:** Results are [scaled scores, rather than the raw number of questions scored correct](../facts/exam.md#exam-scaled-scoring). <!-- trap: how-the-exam-asks-trap-720-is-percent -->
- **Wrong belief:** Leave a question blank when you are not sure. **Truth:** There is [no penalty for guessing](../facts/exam.md#exam-no-guessing-penalty), and a blank question is [scored as incorrect](../facts/exam.md#exam-no-guessing-penalty). <!-- trap: how-the-exam-asks-trap-leave-blank -->
- **Wrong belief:** ESL +30 requested after booking covers the exam that you booked. **Truth:** [ESL +30](../facts/exam.md#exam-esl-accommodation) is requested before you register, and then it will [apply to all future exam registrations](../facts/exam.md#exam-esl-accommodation). <!-- trap: how-the-exam-asks-trap-esl-after-booking -->

## Read the stem in this order (2 min)
<!-- section: role=method; route=fast; minutes=2 -->

The **stem** is the scenario and the question before the options. In this book, a stem has four parts: context, a problem or change, the constraints, and the ask. A capital word in the ask, such as MOST or LEAST, is the **qualifier**.

1. **Read the ask.** Read the last sentence first, and find the capital word. With no capital word, the requirements alone decide.
2. **Mark the requirements.** Mark words such as "must", "without" and "acceptable".
3. **Predict before the options.** Say your own answer first.
4. **Remove what breaks a requirement or solves a different problem.** One missed requirement makes an option wrong, at any price.
5. **Rank what is left on the qualifier.** Only the options that remain compete on cost, effort or security. In a multiple-response question, keep as many options as the stem asks for.

![A decision ladder with three questions that you ask of each option. First: does it break a stated requirement? Yes removes it. Second: does it solve a different problem? Yes removes it. Third: does another working option rank higher on the qualifier? Yes removes it. An option that passes all three questions is the answer.](../diagrams/svg/how-the-exam-asks-option-ladder.svg)

**Figure.** An option is the answer when it meets every requirement and ranks first on the qualifier.

6. **Answer every question.** There is [no penalty for guessing](../facts/exam.md#exam-no-guessing-penalty).

- **Wrong belief:** If an option works, it is the answer. **Truth:** A multiple-choice question has [one correct response and three incorrect responses (distractors)](../facts/exam.md#exam-question-types). A wrong option is a **distractor** (dis-TRAK-ter). When several options work, the qualifier decides. <!-- trap: how-the-exam-asks-trap-works-means-correct -->
- **Wrong belief:** MOST cost-effective means the cheapest option. **Truth:** You choose what can [best complete the statement or answer the question](../facts/exam.md#exam-select-best-response-instruction). The qualifier ranks only the options that meet every requirement. <!-- trap: how-the-exam-asks-trap-cheapest-wins -->
- **Wrong belief:** An option that repeats a stem word, such as "privately", is probably right. **Truth:** Distractors are [generally plausible responses that match the content area](../facts/exam.md#exam-distractor-definition), so a matching word decides nothing. <!-- trap: how-the-exam-asks-trap-keyword-bait -->

## Exam English core words (2 min)
<!-- section: role=method; route=fast; minutes=2 -->

**MOST or LEAST in capitals** usually means that more than one option works. The capital word names the ranking rule. **MOST cost-effective** asks for the cheapest option that still meets every requirement.

**LEAST operational overhead** asks for the option where the team does the least work to run it: a managed feature, not scripts on instances. **MOST secure** asks for the strongest protection among the options that work: least privilege, temporary credentials and private access.

Strength words decide which options stay. The word **must** marks a hard requirement: an option that misses it is wrong, even when that option is cheaper.

The word **ensure** also makes a requirement hard, so read what follows it. "Ensure that no one can delete the logs" asks for a control that prevents, and an alert after the deletion is not enough. "Ensure the durability of data" can be met by backups.

The word **acceptable** relaxes a requirement, so a cheaper or simpler option is now allowed. The phrase **wants to avoid** removes every option that includes the unwanted thing.

A **highly available** system and a **fault tolerant** system both keep working when one part fails. This book reads them as two strengths: highly available accepts a short interruption, and fault tolerant accepts none. The stem decides, so find the interruption that it accepts.

The ask often ends with **these requirements**: all the needs stated before the question. Go back and count them. **Which solution will meet these requirements?** asks for the one option that meets every one of them.

The exam [uses short names of some AWS services](../facts/exam.md#exam-short-service-names-help-button): Amazon Simple Notification Service [appears on the exam as Amazon SNS](../facts/exam.md#exam-short-name-example). The full names are [available through the Help button in the exam](../facts/exam.md#exam-short-service-names-help-button). Some names are [never expanded (for example, Amazon API Gateway, Amazon EMR)](../facts/exam.md#exam-abbreviations-not-expanded).

- **Wrong belief:** The right design is the most available one, even when the stem accepts an interruption. **Truth:** AWS names this trade-off: teams can [reduce cost at the expense of reliability in development environments](../facts/well-architected.md#well-architected-tradeoff-examples-dev-versus-mission-critical). Choose what the stem asks for, not more. <!-- trap: how-the-exam-asks-trap-always-max-availability -->
- **Wrong belief:** A control that detects the action and sends an alert meets an "ensure that no one can" requirement. **Truth:** That stem asks for a control that stops the action, even for the root user when the stem names it. In the practice question, a **service control policy** (SCP) does that. It [restricts permissions for IAM users and roles in member accounts](../facts/iam.md#iam-scp-applies-to-member-root-user), [including the member account's root user](../facts/iam.md#iam-scp-applies-to-member-root-user). <!-- xref: 04 service control policies --> <!-- trap: how-the-exam-asks-trap-detect-meets-ensure -->

## Multiple-response questions (1 min)
<!-- section: role=method; route=fast; minutes=1 -->

A **multiple response** question has [two or more correct responses out of five or more response options](../facts/exam.md#exam-question-types). The stem says how many to choose, for example **(Select TWO.)**. Judge each option alone, as true or false. Then count your marks against the number in the stem.

In **Which combination of steps**, the chosen options work together as one solution, and they must not conflict. Often one option is the service and the other is its configuration. If you are not sure of the last option, still mark the full number: there is [no penalty for guessing](../facts/exam.md#exam-no-guessing-penalty).

- **Wrong belief:** In a multiple-response question, pick the best option first, then the next-best one. **Truth:** The question has [two or more correct responses out of five or more response options](../facts/exam.md#exam-question-types), so judge each option on its own. <!-- trap: how-the-exam-asks-trap-multi-response-best-one -->

## Check (1 min)
<!-- section: role=check; route=fast; minutes=1 -->

**Check 1.** The ask is LEAST operational overhead. A script on an instance and a managed feature both work. Which ranks first?

<details>
<summary>Answer</summary>

The managed feature. Both work, so the qualifier ranks them.

**Predict 1:** The cheaper of the two options that meet every requirement.

</details>

**Check 2.** The stem says "must ensure the durability of its data". Does "ensure" remove an option that takes backups?

<details>
<summary>Answer</summary>

No. The guide itself asks you to [ensure the durability and availability of data (for example, backups)](../facts/exam.md#exam-guide-backup-retention-wording).

**Predict 2:** [50 questions that affect your score](../facts/exam.md#exam-question-count), and you cannot tell which.

</details>

## Recap from memory (1 min)
<!-- section: role=recap; route=fast; minutes=1 -->

**Recap 1.** What are the six reading steps?

<details>
<summary>Answer</summary>

Read the ask; mark the requirements; predict before the options. Remove what breaks a requirement or solves a different problem; rank what is left on the qualifier; answer every question.

</details>

**Recap 2.** What does MOST cost-effective ask for?

<details>
<summary>Answer</summary>

The cheapest option that meets every requirement.

</details>

**Recap 3.** What is the passing score, and on which scale?

<details>
<summary>Answer</summary>

[720 on a scale of 100 to 1,000](../facts/exam.md#exam-passing-score).

</details>
