---
chapter: "99"
file: deep
title: Amazon Widget Store in depth
status: draft
updated: 2026-10-04
---

# Amazon Widget Store in depth

## How it works (6 min)
<!-- section: role=how; route=full; minutes=6 -->

### A shelf belongs to one Region for its whole life (3 min)
<!-- section: route=pass -->

When you create a shelf, you choose a Region. The shelf is a [Regional resource](../facts/widget.md#widget-shelf-scope), so the widgets on the shelf stay in that Region.

Some resources stay in the Region where you create them. This is called **Regional**. A shelf is Regional. A crate is not the same: a crate travels between Regions.

You [cannot move a shelf](../facts/widget.md#widget-shelf-move) to another Region. If a team needs the same widgets in a second Region, the team can [copy the shelf](../facts/widget.md#widget-shelf-move). The signals for this decision are in [Signals and traps](1-fast.md#signals-and-traps-2-min).

> **Key fact:** A shelf stores widgets in [one AWS Region](../facts/widget.md#widget-shelf-scope).

> **Exam signal:** "The widgets must stay in one Region" points to a shelf, not to a crate.

A description of a shelf names its Region:

```json
{"Shelf": "saa-sample-shelf", "Region": "eu-central-1", "Widgets": 300}
```

<details>
<summary>Go deeper: the shelf quota</summary>

The default quota is [20 shelves per Region](../facts/widget.md#widget-shelves-per-region). You can ask AWS to raise this quota.

</details>

> **Try it:** Create a shelf, then try to move it to another Region. See [3-do.md](3-do.md). <!-- task: sample-t02 -->

> **Say it:** The short answer is: a shelf stays in its Region. The thing to watch is a second Region: you copy the shelf there.

**Stop and answer.** Callvale has a shelf in Frankfurt with 300 widgets. A new customer wants the same widgets in the Tokyo Region. What do you do with the shelf?

<details>
<summary>Answer</summary>

You [copy the shelf](../facts/widget.md#widget-shelf-move) to the Tokyo Region. You [cannot move a shelf](../facts/widget.md#widget-shelf-move), and the customers in Germany still need the first shelf.

</details>

### A new shelf is private until the owner changes it (3 min)

A new shelf starts closed. By default, a new shelf is [private](../facts/widget.md#widget-shelf-default-private). At first, [only its owner can read it](../facts/widget.md#widget-shelf-default-private).

This default protects the widgets of a new project from a mistake. The owner decides later who else reads the shelf.

> **Exam trap:** A new shelf is not public. A new shelf is [private](../facts/widget.md#widget-shelf-default-private).

> **Exam heuristic:** When two options both meet the requirements, the exam usually prefers the option that keeps the secure default.

**Spot the bug.** Ben plans one shelf in Frankfurt for 800 widgets. What is wrong?

<details>
<summary>Answer</summary>

A shelf holds [up to 500 widgets](../facts/widget.md#widget-shelf-max-widgets). Ben needs two shelves in Frankfurt.

</details>

**Stop and answer.** Chen creates a shelf for audit samples and changes no setting. Ana signs in with her own account. Can Ana read the shelf?

<details>
<summary>Answer</summary>

No. A new shelf is [private](../facts/widget.md#widget-shelf-default-private), and [only its owner can read it](../facts/widget.md#widget-shelf-default-private). Chen is the owner.

</details>

## Numbers that decide answers (1 min)
<!-- section: role=numbers; route=full; minutes=1 -->

### A-list

<!-- table: numbers -->
| Number | What it is | Why it decides an answer |
|---|---|---|
| [500 widgets](../facts/widget.md#widget-shelf-max-widgets) | Maximum on one shelf | A stem with more widgets needs a second shelf |

### B-list

<!-- table: numbers -->
| Number | What it is |
|---|---|
| [20 shelves per Region](../facts/widget.md#widget-shelves-per-region) | Default quota, adjustable |
| [50 widgets](../facts/widget.md#widget-crate-capacity) | Maximum in one crate |

<!-- needs-fact: After how many days does Widget Store delete an empty crate? -->

## Decision record (2 min)
<!-- section: role=example; route=full; minutes=2 -->

**Context.** Callvale stores 300 demo widgets for customers in Germany. Next month Callvale adds 300 more.

**Requirement.** All widgets must stay in the Frankfurt Region. The company wants the solution with the LEAST operational overhead.

**Options.**

- Keep one shelf in Frankfurt for all 600 widgets.
- Create a second shelf in Frankfurt.
- Pack the new widgets in six crates.

**Decision.** Create a second shelf in Frankfurt.

**Trade-off.** Two shelves mean two places to count. Callvale accepts that, because a shelf holds [up to 500 widgets](../facts/widget.md#widget-shelf-max-widgets).

## FAQ quick-fire (2 min)
<!-- section: role=faq; route=full; minutes=2 -->

**FAQ 1.** Can you move a shelf to another Region?

<details>
<summary>Answer</summary>

No. You [cannot move a shelf](../facts/widget.md#widget-shelf-move). You [copy the shelf](../facts/widget.md#widget-shelf-move) to the other Region.

> "You cannot move a shelf to another Region."
> — [Amazon Widget Store limits](https://docs.aws.amazon.com/widget-store/latest/userguide/limits.html)

</details>

**FAQ 2.** Can every user in the account read a new shelf?

<details>
<summary>Answer</summary>

No. By default, a new shelf is [private](../facts/widget.md#widget-shelf-default-private).

> "By default, a new shelf is private and only its owner can read it."
> — [Amazon Widget Store limits](https://docs.aws.amazon.com/widget-store/latest/userguide/limits.html)

</details>

## In the real world (1 min)
<!-- section: role=realworld; route=full; minutes=1 -->

**Tallis Freight, 2025.** [Tallis Freight](../facts/widget.md#widget-case-tallis-freight) is a logistics company. The company moved its widget inventory from its own data center to Amazon Widget Store.

> "We moved our widget inventory to Amazon Widget Store and stopped running our own storage servers"
> — [Tallis Freight case study](https://aws.amazon.com/solutions/case-studies/tallis-freight/)

**It shows:** a managed service removes operational work from a small team.

> **Say it:** Tallis Freight moved its widget inventory to Widget Store. The team stopped running its own storage servers.
