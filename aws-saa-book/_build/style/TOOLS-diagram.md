# Diagrams: author guide

A diagram is a small JSON spec. Our own grid renderer turns it into SVG. You never write coordinates.

- Spec: `aws-saa-book/diagrams/src/<id>.json`
- Output: `aws-saa-book/diagrams/svg/<id>.svg` (standalone: light palette, opaque ground, icons embedded). A `compare` diagram also gets `<id>.p1.svg`, `<id>.p2.svg`, one per panel.
- Schema: `aws-saa-book/_build/schemas/diagram.schema.json`
- Code: `aws-saa-book/tools/saalib/diagram/`
- Icons: `aws-saa-book/diagrams/icons.json` (official AWS Architecture Icons, release 2026-07-31; see `diagrams/ICONS-NOTICE.md`). A sandbox book (`--book-dir`) without its own `icons.json` reads the real book's; writing still goes only to the real book.

Seven kinds exist. Pick the one that matches what the figure says:

| Kind | Use it for | Section |
|---|---|---|
| `arch` | What is connected to what; a numbered request path | "The spec (`kind: "arch"`)" |
| `sequence` | Order in time between 2 to 5 actors (AssumeRole, a presigned URL, envelope encryption) | "Kind: sequence" |
| `ladder` | A decision: questions down a spine, each with one answer that ends on an outcome | "Kind: ladder" |
| `compare` | Two or three small architectures side by side | "Kind: compare" |
| `states` | A lifecycle: states and labelled transitions | "Kind: states" |
| `timeline` | Things that last over time, on an axis (S3 Lifecycle, RPO and RTO) | "Kind: timeline" |
| `raw` | The escape hatch: a hand-written SVG | "Kind: raw" |

Every kind needs `id`, `kind`, `title`, `claim` (exactly one sentence) and `alt`, and takes the optional `size`, `chapter`, `sample` and `notes` (bookkeeping, not drawn). Labels inside a drawing are a few words, never a sentence. The QA loop is the same for every kind.

## Commands

Run each as one plain command from the repo root.

```
python3 aws-saa-book/tools/saa.py diagram build <id>          # validate, lint, write diagrams/svg/<id>.svg
python3 aws-saa-book/tools/saa.py diagram build --all
python3 aws-saa-book/tools/saa.py diagram lint <id>           # same checks, writes nothing
python3 aws-saa-book/tools/saa.py diagram lint --file <spec.json>
python3 aws-saa-book/tools/saa.py diagram preview <id>        # four-panel HTML page
python3 aws-saa-book/tools/saa.py diagram shot <id>           # PNG of that page
python3 aws-saa-book/tools/saa.py diagram sheet               # one PNG with every built diagram
python3 aws-saa-book/tools/saa.py diagram icons --list        # icon names you can use
python3 aws-saa-book/tools/saa.py diagram icons --find nat,gateway   # search the AWS package
python3 aws-saa-book/tools/saa.py diagram css                 # stylesheet for inline diagrams (web app)
python3 aws-saa-book/tools/saa.py diagram sprite              # <symbol id="ic-NAME"> sprite (web app)
```

Screenshot of any page (for other agents):

```
python3 aws-saa-book/tools/saa.py diagram shot --file <page.html or image.svg inside the book> --out <png inside the book> [--width 1280] [--height 900] [--full] [--dark] [--scale 2]
```

- `--full` measures the page and captures its whole height (capped at 16,000 px). An `.svg` is always captured in full.
- `--dark` asks Chrome for the dark colour scheme and also sets `data-theme="dark"` on `<html>`.
- The tool screenshots a temporary copy under `_build/tmp/diagram-preview/` with a `<base>` to the original folder, so relative links keep working.

Preview files land in `aws-saa-book/_build/tmp/diagram-preview/`: `<id>.html`, `<id>.png`, `<id>.standalone.svg`, `sheet.png`.

Exit codes: 0 clean, 1 an error blocks the build, 2 warnings only, 3 precondition missing, 4 path outside the book, 5 Chrome or network problem (retry).

The `diagrams` gate of the ledger also fails (D04) when `diagrams/svg/<id>.svg` or a panel file is not the output of the current spec (`pipeline.stale_files`): run `diagram build <id>` after every change to a spec.

## The QA loop

1. Write the spec. Run `diagram build <id>`. Fix every error.
2. Run `diagram shot <id>`. Open the PNG with the Read tool.
3. Check: no overlap or clipping; arrows end on node edges; the claim is true of the picture; the phone panels are readable; the dark panels are readable.
4. Fix the spec. Three rounds at most, then simplify the figure.
5. `diagram sheet` gives one image for a consistency review.

The four panels are desktop and 368 px phone, each in light and dark, drawn with the inline renderer and the web app's token values. A fifth strip shows the standalone file as an image. The phone panel prints its scale; if it says "scrolls sideways", the figure is too wide for a phone at the minimum scale of 0.75.

## The spec (`kind: "arch"`)

```json
{
  "id": "vpc-two-az",
  "kind": "arch",
  "size": "s",
  "title": "A VPC across two Availability Zones",
  "claim": "Private instances reach the internet through the NAT gateway in their own Availability Zone.",
  "alt": "Text for a reader who cannot see the figure.",
  "cols": 2, "rows": 6, "flow": "down",
  "groups": [ {"id": "vpc", "type": "vpc", "label": "VPC 10.0.0.0/16", "cells": "A2:B5"},
              {"id": "az1", "type": "az", "label": "Availability Zone a", "in": "vpc", "cells": "A3:A4"} ],
  "nodes":  [ {"id": "igw", "icon": "internet-gateway", "label": "Internet gateway", "at": "A2:B2"} ],
  "edges":  [ {"from": "app1", "to": "nat1", "label": "0.0.0.0/0", "step": 1, "emph": true,
               "say": "The private route table sends internet traffic to the NAT gateway."} ]
}
```

### Top level

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Lower case, digits and hyphens. Must equal the file name. |
| `kind` | yes | `arch`. |
| `title` | yes | Goes in the caption, not in the drawing. |
| `claim` | yes | Exactly one sentence, ending with a full stop. Goes in the caption. |
| `alt` | yes | At least 20 characters. Becomes `<desc>` and `aria-label`. |
| `cols`, `rows` | yes | Grid size, 1 to 8 each. |
| `size` | no | `s` (up to 445 units wide, fits a phone without scrolling), `m` (up to 720, default), `l` (up to 1040). Lint warns when the drawing is wider. |
| `flow` | no | `down` (default, a request path) or `right` (a pipeline). A tie-breaker for routing. |
| `chapter`, `sample`, `notes` | no | Bookkeeping; not drawn. |

### Cells

Columns are letters, rows are numbers: `A1` is the top-left cell. A range `A2:B5` runs from its top-left cell to its bottom-right cell. All columns have the same width.

### Nodes

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Unique in the diagram. |
| `label` | yes | At most 4 words, no full stop. Wraps to 2 lines at most. Force a break with `\n`. |
| `at` | yes | A cell, or a range. In a range the node is centred, which is how you put one node between two columns. |
| `icon` | no | A name from `diagram icons --list`. Without an icon the node is drawn as a labelled box. |
| `emph` | no | `true` draws the highlight ring. |

Use service icons (coloured squares, for example `s3`, `lambda`, `rds`) for a service as a whole and resource icons (line art, for example `bucket`, `instance`, `nat-gateway`, `alb`, `role`, `queue`) for one resource. Generic items: `user`, `users`, `client`, `mobile-client`, `server`, `internet`, `corporate-data-center`.

### Groups

| Field | Required | Meaning |
|---|---|---|
| `id`, `label`, `cells` | yes | Label: at most 5 words. |
| `type` | yes | See the table below. |
| `in` | when nested | The id of the parent group. A group must lie inside its parent. |

Groups form a tree. Two groups may not cross each other. A node must lie fully inside or fully outside each group.

| `type` | AWS convention | Border | Colour token |
|---|---|---|---|
| `region` | Region | dotted | `--dg-teal` |
| `vpc` | VPC | solid, heavy | `--dg-vpc` |
| `az` | Availability Zone | long dashes | `--dg-teal` |
| `subnet-public` | Public subnet | solid, tinted | `--dg-pub` |
| `subnet-private` | Private subnet | dash-dot, tinted | `--dg-teal` |
| `security-group` | Security group | short dashes | `--dg-sg` |
| `auto-scaling-group` | Auto Scaling group | dash-dot-dot | `--dg-asg` |
| `account` | AWS account | long-short dashes | `--dg-acct` |
| `corporate-data-center` | Corporate data center | very long dashes, tinted | `--dg-muted` |
| `generic` | Any other boundary | sparse dashes | `--dg-muted` |

Every type differs by border pattern or weight as well as by colour, so the figure still reads in greyscale.

### Edges

| Field | Required | Meaning |
|---|---|---|
| `from`, `to` | yes | Node ids. The arrow points at `to`. |
| `label` | one of the two | At most 3 words. |
| `step` | one of the two | Step number. Steps must run 1, 2, 3 with no gap. Two edges may share a step (for example the same hop in each Availability Zone). |
| `say` | once per step | One sentence for the numbered list under the figure. |
| `emph` | no | Highlight colour and a heavier line. |
| `dashed` | no | Dashed line, for example for replication or an asynchronous hop. |
| `arrow` | no | `end` (default), `none`, `both`. `both` gives a lint warning. |
| `fromSide`, `toSide` | no | `top`, `right`, `bottom`, `left`. Forces the side when the automatic route is not what you want. |

## How layout and routing behave

- The renderer places each node at the top of its cell: icon first, label under it. Icons in one row line up.
- Each nested group border adds one lane of space to the gutter it sits in. Each group has a label band at its top; the label is regular weight, 11.5 units, in ink colour (not the group colour), so the group type is carried by the border colour and dash pattern.
- Edges are orthogonal. An edge runs straight, makes one bend through a cell centre line, or travels along the mid-line of a gutter. Parallel edges in one gutter get separate tracks, and arrows on one side of a node are spread.
- A group label moves to the right end of its band when an edge would run through it on the left. When both ends are blocked, all columns grow until the label fits (up to 220 units). This is why a figure can come out wider than you expect. Shorter group labels, or a group that is two columns wide, keep the figure narrow.
- Step badges sit on the line. Edge labels sit beside the line.

Fixes that work:

| Lint says | Try |
|---|---|
| `text-overflow`, `text-lines` | Shorten the label, or break it with `\n`. |
| `edge-through-node`, `edge-on-label` | Move a node to another cell, or set `fromSide` / `toSide`. |
| `edge-label-no-room` | Shorten the label, or leave an empty row or column so the edge has a longer segment. |
| `limit-crossings`, `edge-overlap` | Reorder nodes so that connected nodes are neighbours. |
| `size-budget` | Fewer columns, shorter group labels, or a larger `size`. |
| `label-on-border` (warning) | Usually acceptable; look at the screenshot. |
| `layout` (groups overlap) | Add `"in"`, or redraw so the groups nest. |

## Style guide

**Every diagram must have:**

- a title and a one-sentence claim in the caption, not in the drawing;
- alt text;
- a label or step number on every arrow, with numbered steps repeated as a list under the figure;
- official icons at one size, unmodified;
- AWS group conventions;
- reading direction top to bottom for a request path, left to right for a pipeline;
- names taken from the glossary;
- one highlight colour, for the one thing the figure is about.

**No diagram may have:**

- more than 12 nodes or 14 edges;
- more than two AZs drawn;
- Region or account boxes unless the point is multi-Region or multi-account;
- sentences inside the drawing;
- more than two edge crossings;
- literal colours, rotated text, shadows or gradients;
- colour as the only carrier of meaning (borders also differ by dash pattern);
- a two-headed arrow where it matters who starts the connection.

What the tool enforces, and what you must check yourself:

| Rule | Enforced by |
|---|---|
| Title, claim (one sentence), alt | schema and lint (error) |
| Label or step on every arrow; steps without gaps; `say` for each step | lint (error) |
| Official icons, one size | by construction; unknown icon name is an error |
| Node, edge and AZ limits; crossings | lint (error) |
| A single Region or account box | lint (error) |
| Sentences in the drawing | lint (error): word limits and no full stop |
| Literal colours, rotated text, shadows, gradients | by construction: the spec has no such fields |
| Border pattern per group type | by construction, and a unit test |
| Two-headed arrow | lint (warning) |
| More than 4 highlighted items | lint (warning) |
| Text fits its node; labels do not overlap; no edge through a node or a label; arrows end on node edges; nothing clipped | geometry lint (error) |
| Reading direction, glossary names, a true claim | you |

Hard facts in a figure (a CIDR, a port, a limit) follow the same rule as prose: they must exist in the fact canon. The two samples are demonstrations of the renderer, not checked book content.

## Sample 1: a two-AZ VPC

`aws-saa-book/diagrams/src/sample-vpc-two-az.json` gives `aws-saa-book/diagrams/svg/sample-vpc-two-az.svg` (444 x 776 units; fits a phone at scale 0.75).

```json
{
  "id": "sample-vpc-two-az", "kind": "arch", "size": "s", "sample": true,
  "title": "A VPC across two Availability Zones",
  "claim": "Private instances reach the internet through the NAT gateway in their own Availability Zone.",
  "alt": "A VPC with two Availability Zones. Each zone has a public subnet with a NAT gateway and a private subnet with an app server. The app servers send internet traffic to the NAT gateway in the same zone, then to the internet gateway. Traffic for Amazon S3 goes through a gateway endpoint instead.",
  "cols": 2, "rows": 6, "flow": "down",
  "groups": [
    {"id": "vpc", "type": "vpc", "label": "VPC 10.0.0.0/16", "cells": "A2:B5"},
    {"id": "az1", "type": "az", "label": "Availability Zone a", "in": "vpc", "cells": "A3:A4"},
    {"id": "az2", "type": "az", "label": "Availability Zone b", "in": "vpc", "cells": "B3:B4"},
    {"id": "pub1", "type": "subnet-public", "label": "Public subnet", "in": "az1", "cells": "A3"},
    {"id": "pub2", "type": "subnet-public", "label": "Public subnet", "in": "az2", "cells": "B3"},
    {"id": "priv1", "type": "subnet-private", "label": "Private subnet", "in": "az1", "cells": "A4"},
    {"id": "priv2", "type": "subnet-private", "label": "Private subnet", "in": "az2", "cells": "B4"}
  ],
  "nodes": [
    {"id": "internet", "icon": "internet", "label": "Internet", "at": "A1:B1"},
    {"id": "igw", "icon": "internet-gateway", "label": "Internet gateway", "at": "A2:B2"},
    {"id": "nat1", "icon": "nat-gateway", "label": "NAT gateway", "at": "A3"},
    {"id": "nat2", "icon": "nat-gateway", "label": "NAT gateway", "at": "B3"},
    {"id": "app1", "icon": "instance", "label": "App server", "at": "A4"},
    {"id": "app2", "icon": "instance", "label": "App server", "at": "B4"},
    {"id": "s3ep", "icon": "endpoint", "label": "Gateway endpoint", "at": "A5:B5"},
    {"id": "s3", "icon": "s3", "label": "Amazon S3", "at": "A6:B6"}
  ],
  "edges": [
    {"from": "app1", "to": "nat1", "label": "0.0.0.0/0", "step": 1, "emph": true,
     "say": "The private route table sends internet traffic to the NAT gateway in the same Availability Zone."},
    {"from": "app2", "to": "nat2", "label": "0.0.0.0/0", "step": 1, "emph": true},
    {"from": "nat1", "to": "igw", "step": 2, "say": "The NAT gateway forwards the traffic to the internet gateway."},
    {"from": "nat2", "to": "igw", "step": 2},
    {"from": "igw", "to": "internet", "step": 3, "say": "The internet gateway connects the VPC to the internet."},
    {"from": "app1", "to": "s3ep", "step": 4,
     "say": "Traffic for Amazon S3 follows the gateway endpoint route and does not use the NAT gateway."},
    {"from": "app2", "to": "s3ep", "step": 4},
    {"from": "s3ep", "to": "s3", "label": "S3 traffic"}
  ]
}
```

Points to copy: one column per Availability Zone; nodes shared by both zones sit in a two-column range (`A2:B2`); the same step number on the matching edge in each zone.

## Sample 2: a three-tier web application with a numbered request flow

`aws-saa-book/diagrams/src/sample-three-tier.json` gives `aws-saa-book/diagrams/svg/sample-three-tier.svg` (356 x 578 units).

```json
{
  "id": "sample-three-tier", "kind": "arch", "size": "s", "sample": true,
  "title": "A three-tier web application",
  "claim": "A request passes through three tiers, and the load balancer is the only tier in a public subnet.",
  "alt": "Users send requests to an Application Load Balancer in public subnets. The load balancer forwards each request to one of two app servers in an Auto Scaling group in private subnets. The app servers use a primary DB instance, which replicates to a standby DB instance.",
  "cols": 2, "rows": 4, "flow": "down",
  "groups": [
    {"id": "vpc", "type": "vpc", "label": "VPC", "cells": "A2:B4"},
    {"id": "web", "type": "subnet-public", "label": "Public subnets", "in": "vpc", "cells": "A2:B2"},
    {"id": "app", "type": "subnet-private", "label": "Private subnets: app", "in": "vpc", "cells": "A3:B3"},
    {"id": "asg", "type": "auto-scaling-group", "label": "Auto Scaling group", "in": "app", "cells": "A3:B3"},
    {"id": "data", "type": "subnet-private", "label": "Private subnets: data", "in": "vpc", "cells": "A4:B4"}
  ],
  "nodes": [
    {"id": "users", "icon": "users", "label": "Users", "at": "A1:B1"},
    {"id": "alb", "icon": "alb", "label": "Application Load Balancer", "at": "A2:B2"},
    {"id": "app1", "icon": "instance", "label": "App server", "at": "A3"},
    {"id": "app2", "icon": "instance", "label": "App server", "at": "B3"},
    {"id": "db1", "icon": "db-instance", "label": "Primary DB", "at": "A4"},
    {"id": "db2", "icon": "db-instance-standby", "label": "Standby DB", "at": "B4"}
  ],
  "edges": [
    {"from": "users", "to": "alb", "label": "HTTPS", "step": 1, "emph": true,
     "say": "A user sends an HTTPS request to the Application Load Balancer."},
    {"from": "alb", "to": "app1", "step": 2, "say": "The load balancer forwards the request to a healthy app server."},
    {"from": "alb", "to": "app2", "step": 2},
    {"from": "app1", "to": "db1", "label": "SQL", "step": 3,
     "say": "The app server reads and writes data on the primary DB instance."},
    {"from": "app2", "to": "db1", "step": 3},
    {"from": "db1", "to": "db2", "label": "replication", "step": 4, "dashed": true,
     "say": "Amazon RDS copies the data to the standby DB instance in the other Availability Zone."}
  ]
}
```

Points to copy: tiers as rows; an Auto Scaling group nested in the subnet group with the same cells; a dashed edge for replication. An Auto Scaling group that spans two Availability Zone boxes cannot be drawn (groups may not cross), so this figure groups by tier instead.

## Kind: sequence

Actors stand across the top, each with a lifeline. Messages run from top to bottom and are numbered 1, 2, 3 in the order of the list. Each message has a short `label` in the drawing and a `say` sentence for the numbered list under the figure.

| Field | Required | Meaning |
|---|---|---|
| `actors[]` | yes, 2 to 5 | `id`, `label` (at most 4 words), optional `icon`, optional `emph`. Left to right in list order. |
| `messages[]` | yes, 1 to 10 | `from`, `to` (actor ids), `label` (at most 4 words), `say` (exactly one sentence). Optional `dashed` (use it for a reply) and `emph`. |
| `asides[]` | no, at most 3 | A note box on a lifeline: `after` (message number; 0 puts it before the first message), `over` (actor id), `text` (at most 6 words, no full stop). |

- `from` equal to `to` draws a loop on the actor's own lifeline (for a local step such as "Sign URL").
- The distance between two lifelines grows until the label fits in the gap next to the sender. Long labels make a wide figure; three actors with labels of two or three words fit a phone.
- Every actor must send or receive at least one message.

Lint codes: `limit-actors`, `limit-messages`, `limit-asides`, `ref-unknown`, `ref-duplicate`, `sentence`, `say`, `aside-after`, `actor-unused`, `icon-unknown`.

Sample: `diagrams/src/sample-seq-presigned-url.json` (328 x 400 units, fits a phone at scale 1).

```json
{
  "id": "sample-seq-presigned-url", "kind": "sequence", "size": "s", "sample": true,
  "title": "A download with a presigned URL",
  "claim": "The file travels directly from Amazon S3 to the user, not through the app server.",
  "alt": "A sequence with three actors: a user, an app server and Amazon S3. ...",
  "actors": [
    {"id": "user", "icon": "user", "label": "User"},
    {"id": "app", "icon": "instance", "label": "App server"},
    {"id": "s3", "icon": "s3", "label": "Amazon S3"}
  ],
  "messages": [
    {"from": "user", "to": "app", "label": "Ask for file", "say": "The user asks the app server for a file."},
    {"from": "app", "to": "app", "label": "Sign URL", "say": "The app server signs a URL for the object with its own credentials."},
    {"from": "app", "to": "user", "label": "Presigned URL", "dashed": true, "say": "The app server returns the presigned URL to the user."},
    {"from": "user", "to": "s3", "label": "GET with URL", "emph": true, "say": "The user sends a GET request with the presigned URL directly to Amazon S3."},
    {"from": "s3", "to": "user", "label": "Object", "dashed": true, "say": "Amazon S3 checks the signature and returns the object."}
  ],
  "asides": [ {"after": 3, "over": "user", "text": "URL works until it expires"} ]
}
```

## Kind: ladder

A vertical spine of questions. Each question (a rung) has one answer that leaves to the right and ends on an outcome. The other answer goes down to the next question. The spine ends on the `else` outcome. Questions are boxes; outcomes are icons or pills.

| Field | Required | Meaning |
|---|---|---|
| `rungs[]` | yes, 1 to 6 | `q`: the question, at most 9 words, may end with a question mark, wraps to 3 lines. `then`: the outcome on the right. `answer`: label of the arrow to the right (default `Yes`). `next`: label of the arrow down (default `No`). Both at most 3 words. |
| `else` | yes | The outcome at the bottom of the spine. |
| outcome | | `label` (at most 4 words), optional `icon`, optional `emph`. |

- Order the questions so that the first "yes" is the answer. Put the most decisive question first.
- A highlighted outcome also highlights its arrow.

Lint codes: `limit-rungs`, `sentence`, `answers-equal`, `icon-unknown`, and the geometry codes (`text-overflow` for one word that is wider than the question box).

Sample: `diagrams/src/sample-ladder-load-balancer.json` (365 x 454 units).

```json
{
  "id": "sample-ladder-load-balancer", "kind": "ladder", "size": "s", "sample": true,
  "title": "Which load balancer?",
  "claim": "The kind of traffic decides the type of load balancer.",
  "alt": "A decision ladder with three questions. ...",
  "rungs": [
    {"q": "Must traffic pass through virtual appliances?", "then": {"label": "Gateway Load Balancer", "icon": "gwlb"}},
    {"q": "Route requests by HTTP path or host?", "then": {"label": "Application Load Balancer", "icon": "alb", "emph": true}},
    {"q": "TCP, UDP or TLS traffic?", "then": {"label": "Network Load Balancer", "icon": "nlb"}}
  ],
  "else": {"label": "Read the requirement again"}
}
```

## Kind: compare

Two or three small `arch` panels. Each panel has a heading and its own grid, and is laid out and linted like an `arch` figure.

| Field | Required | Meaning |
|---|---|---|
| `panels[]` | yes, 2 or 3 | `label` (the heading, at most 4 words), `cols` (1 to 4), `rows` (1 to 6), `nodes`, optional `groups`, `edges`, `flow`, `alt`. Nodes, groups and edges are written exactly as in `arch`. |

- A panel holds at most 6 nodes and 7 edges, and must fit a phone (445 units wide).
- Panel edges take a `label`. Step numbers and `say` are not allowed in panels (`compare-step`).
- Node ids are local to a panel, so both panels can have a node `app`.
- Give the panels the same structure (same cells for the same things). The difference is then the only thing that changes.
- One Region box or one account box in a panel is allowed here.

Output: `diagrams/svg/<id>.svg` holds the panels in one row (for Markdown, PDF and Anki), and `diagrams/svg/<id>.p1.svg`, `<id>.p2.svg` hold one panel each. On the web the panels are separate `<svg>` elements in a wrapper; they stand side by side when they fit and stack when they do not. The phone panels of the preview show the stacked form.

Lint codes: `limit-panels`, `limit-nodes`, `limit-edges`, `compare-step`, `sentence`, and every `arch` code with the prefix "panel N:".

Sample: `diagrams/src/sample-compare-multi-az-replica.json` (row 638 x 228 units; the panels stack on a phone at scale 1).

```json
{
  "id": "sample-compare-multi-az-replica", "kind": "compare", "size": "m", "sample": true,
  "title": "Multi-AZ deployment or read replica",
  "claim": "A standby DB instance is for failover, and a read replica is for read traffic.",
  "alt": "Two panels. ...",
  "panels": [
    { "label": "Multi-AZ deployment", "cols": 2, "rows": 2,
      "nodes": [
        {"id": "app", "icon": "instance", "label": "App server", "at": "A1"},
        {"id": "primary", "icon": "db-instance", "label": "Primary DB", "at": "A2"},
        {"id": "standby", "icon": "db-instance-standby", "label": "Standby DB", "at": "B2", "emph": true} ],
      "edges": [
        {"from": "app", "to": "primary", "label": "reads, writes"},
        {"from": "primary", "to": "standby", "label": "sync copy"} ] },
    { "label": "Read replica", "cols": 2, "rows": 2,
      "nodes": [
        {"id": "app", "icon": "instance", "label": "App server", "at": "A1"},
        {"id": "primary", "icon": "db-instance", "label": "Primary DB", "at": "A2"},
        {"id": "replica", "icon": "db-instance", "label": "Read replica", "at": "B2", "emph": true} ],
      "edges": [
        {"from": "app", "to": "primary", "label": "writes"},
        {"from": "app", "to": "replica", "label": "reads"},
        {"from": "primary", "to": "replica", "label": "async copy", "dashed": true} ] }
  ]
}
```

## Kind: states

A lifecycle. States sit on a grid, as `arch` nodes do, and are drawn as pills. Transitions are routed and labelled by the same router as `arch` edges.

| Field | Required | Meaning |
|---|---|---|
| `cols`, `rows` | yes | Grid size, 1 to 6 each. |
| `states[]` | yes, 2 to 8 | `id`, `label` (at most 4 words), `at` (a cell or a range). `final: true` draws a double border. `emph: true` fills the pill with the highlight colour. |
| `transitions[]` | yes, 1 to 12 | `from`, `to`, `label` (at most 3 words, required). Optional `dashed`, `emph`, `fromSide`, `toSide`. |
| `flow` | no | `down` (default) or `right`. |

- Every state needs at least one transition. No transition may leave a final state.
- Place states so that the main path runs straight down or straight to the right, and side paths use the second column.

Lint codes: `limit-states`, `limit-transitions`, `state-unlinked`, `final-leaves`, `ref-unknown`, `ref-self`, `sentence`, and the `arch` geometry codes.

Sample: `diagrams/src/sample-states-ec2-lifecycle.json` (300 x 334 units).

```json
{
  "id": "sample-states-ec2-lifecycle", "kind": "states", "size": "s", "sample": true,
  "title": "The lifecycle of an EC2 instance",
  "claim": "A stopped instance can start again, but a terminated instance is gone.",
  "alt": "A state diagram. ...",
  "cols": 2, "rows": 4, "flow": "down",
  "states": [
    {"id": "pending", "label": "pending", "at": "A1"},
    {"id": "running", "label": "running", "at": "A2", "emph": true},
    {"id": "stopping", "label": "stopping", "at": "B2"},
    {"id": "stopped", "label": "stopped", "at": "B1"},
    {"id": "shutting", "label": "shutting-down", "at": "A3"},
    {"id": "terminated", "label": "terminated", "at": "A4", "final": true}
  ],
  "transitions": [
    {"from": "pending", "to": "running", "label": "ready"},
    {"from": "running", "to": "stopping", "label": "stop"},
    {"from": "stopping", "to": "stopped", "label": "done"},
    {"from": "stopped", "to": "pending", "label": "start"},
    {"from": "running", "to": "shutting", "label": "terminate"},
    {"from": "shutting", "to": "terminated", "label": "done"}
  ]
}
```

## Kind: timeline

A horizontal axis with ticks. Above it, lanes of spans (bars from one tick to a later tick). An event is a vertical line through all lanes at one tick.

| Field | Required | Meaning |
|---|---|---|
| `ticks[]` | yes, 2 to 7 | `id`, `label` (at most 3 words). In order, left to right. |
| `lanes[]` | yes, 1 to 4 | `label` (at most 5 words) and `spans[]`. |
| span | 12 at most in the figure | `from` (tick id), `to` (a later tick id), `label` (at most 4 words, wraps to 2 lines), optional `emph`. Without `to` the span runs on past the last tick. |
| `events[]` | no, at most 3 | `at` (tick id), `label` (at most 3 words), optional `emph`. One event per tick. |
| `axis` | no | Title under the axis, for example "Object age". |

- **The axis is not to scale.** Ticks follow each other in order; the distance from one tick to the next only depends on the labels. Day 30 to Day 90 can be as wide as Day 90 to Day 365. Do not use this kind when the reader must compare lengths.
- Spans of one lane may not overlap. Use a second lane for a second thing that changes over the same time.
- An event line may not run through a lane label (`event-on-label`): shorten the lane label or move the event.
- For RPO and RTO: ticks "Last backup", "Disaster", "Service restored"; one lane with a span for the lost data and a span for the downtime; an event at "Disaster".

Lint codes: `limit-ticks`, `limit-lanes`, `limit-spans`, `limit-events`, `ref-unknown`, `ref-duplicate`, `span-order`, `span-overlap`, `event-same-tick`, `event-on-label`, `sentence`, `text-overflow`.

Sample: `diagrams/src/sample-timeline-s3-lifecycle.json` (386 x 220 units; fits a phone at scale 0.87).

```json
{
  "id": "sample-timeline-s3-lifecycle", "kind": "timeline", "size": "s", "sample": true,
  "title": "An S3 Lifecycle rule over one year",
  "claim": "A lifecycle rule moves an object to colder storage classes as it gets older, and then deletes it.",
  "alt": "A timeline of object age with ticks at day 0, day 30, day 90 and day 365. ...",
  "axis": "Object age",
  "ticks": [ {"id": "d0", "label": "Day 0"}, {"id": "d30", "label": "Day 30"},
             {"id": "d90", "label": "Day 90"}, {"id": "d365", "label": "Day 365"} ],
  "lanes": [
    {"label": "Storage class", "spans": [
      {"from": "d0", "to": "d30", "label": "S3 Standard"},
      {"from": "d30", "to": "d90", "label": "S3 Standard-IA"},
      {"from": "d90", "to": "d365", "label": "S3 Glacier Flexible Retrieval", "emph": true} ]},
    {"label": "How often it is read", "spans": [
      {"from": "d0", "to": "d30", "label": "Often"},
      {"from": "d30", "to": "d90", "label": "Rarely"},
      {"from": "d90", "to": "d365", "label": "Almost never"} ]}
  ],
  "events": [ {"at": "d365", "label": "Object expires"} ]
}
```

The day numbers in this sample are one example rule, not checked facts.

## Kind: raw

The escape hatch for a figure that no other kind can draw. You write the SVG by hand in `diagrams/src/<id>.svg`, next to a small spec. The tool does no layout. It only checks that the drawing follows the shared style sheet and the size limits, so **overlap and text width are yours to check in the screenshot**.

Spec: the common fields, plus optional `"svg": "<file name>.svg"` (default `<id>.svg`, same folder).

Rules for the SVG file:

- The root is `<svg viewBox="0 0 W H">`. W is at most 1040 and H at most 1600; lint warns when W is over the `size` budget.
- Allowed elements: `rect`, `path`, `line`, `circle`, `ellipse`, `polygon`, `polyline`, `text`, `tspan`, `g`, `use`.
- Every drawn element has a `class`, and every class comes from the shared style sheet (see the table). No `fill`, `stroke` (except `none`), `style`, `id`, `font-size` or event attributes. No `<style>`, `<script>`, `<image>`, `<defs>`.
- Allowed attributes: geometry (`x`, `y`, `x1`, `y1`, `x2`, `y2`, `cx`, `cy`, `r`, `rx`, `ry`, `width`, `height`, `d`, `points`, `dx`, `dy`), `class`, `text-anchor`, and `transform` with `translate()` only.
- An icon is `<use href="#ic-NAME" x="" y="" width="48" height="48"/>` with a name from `diagram icons --list`.
- A `<text>` holds at most 6 words. Simple shapes must lie inside the viewBox.

Classes you will use most:

| Class | Draws |
|---|---|
| `dg-nb` | A box: node fill, grey border |
| `dg-sp` | A highlighted box |
| `dg-nt` | A note box, dashed |
| `dg-nl` | Label text, 13 px, centred on `x` |
| `dg-el` | Small text, 12 px, starts at `x` |
| `dg-mt` | Small muted text, 11.5 px |
| `dg-ph` | Bold heading text, 13 px |
| `dg-e`, `dg-e-emph`, `dg-e-dash` | A line or path, highlighted, dashed |
| `dg-ah`, `dg-ah-emph` | A filled arrowhead (a `polygon`) |
| `dg-ax` | An axis or a tick |
| `dg-ll` | A light dotted guide |
| `dg-b` with `dg-bt` | A step badge (circle, r 9) and its numeral |
| `dg-g dg-g-vpc` and the other group classes | A group border |

Lint codes: `ref-missing`, `ref-xml`, `ref-root`, `raw-size`, `raw-element`, `raw-attr`, `raw-colour`, `raw-transform`, `raw-class`, `raw-use`, `raw-empty`, `icon-unknown`, `sentence`, `clip`.

Sample: `diagrams/src/sample-raw-cidr-bits.json` with `diagrams/src/sample-raw-cidr-bits.svg` (340 x 132 units).

```json
{
  "id": "sample-raw-cidr-bits", "kind": "raw", "size": "s", "sample": true,
  "title": "The two parts of a /16 CIDR block",
  "claim": "The prefix length says how many bits name the network, and the other bits number the addresses.",
  "alt": "A bar of 32 bits for the block 10.0.0.0/16. ...",
  "svg": "sample-raw-cidr-bits.svg"
}
```

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 132">
  <text class="dg-ph" x="170" y="19" text-anchor="middle">10.0.0.0/16</text>
  <rect class="dg-nb" x="10" y="34" width="158" height="48" rx="4"/>
  <rect class="dg-sp" x="172" y="34" width="158" height="48" rx="4"/>
  <text class="dg-nl" x="89" y="55">Network part</text>
  <text class="dg-nl" x="251" y="55">Host part</text>
  <line class="dg-ax" x1="10" y1="96" x2="168" y2="96"/>
  <text class="dg-mt" x="89" y="118" text-anchor="middle">16 bits, fixed</text>
</svg>
```

## Limits of each kind

| Kind | Hard limits (lint error) | It cannot draw |
|---|---|---|
| `arch` | 12 nodes, 14 edges, 2 AZs, 2 crossings | See "Not supported yet" |
| `sequence` | 5 actors, 10 messages, 3 asides; labels of 4 words | Activation bars, parallel or optional blocks, a message label on any gap but the sender's, an aside over two actors |
| `ladder` | 6 rungs; questions of 9 words and 3 lines; one outcome per rung | A question with three or more answers, an answer that leads to a second ladder, outcomes shared by two rungs |
| `compare` | 2 or 3 panels; 6 nodes and 7 edges per panel; panel width 445 | Step numbers in panels, arrows between panels, a shared legend |
| `states` | 8 states, 12 transitions, 2 crossings | A transition from a state to itself, start and end dots, states nested in a group, a second line of text in a state |
| `timeline` | 7 ticks, 4 lanes, 12 spans, 3 events | A true time scale, a span that starts between two ticks, a marker inside one lane only, a vertical layout |
| `raw` | viewBox 1040 x 1600; shared classes only | No layout help and no overlap check; gradients, rotation, own colours |

## Not supported yet

- Groups that cross each other (an Auto Scaling group over two AZ boxes).
- A node placed on a group border (an internet gateway drawn on the VPC edge). Put it in the first row inside the group.
- The small AWS corner icon of a group. The label, colour and border pattern carry the type.
- Edges that run in the lane between two nested borders. Edges use the gutter mid-line outside the border stack.
- In `arch`, the highlight ring of a node in the first or last row is cut by the canvas edge (the ring is 6 units outside the node, the margin is 5). `compare` panels and `ladder` make room for it; plain `arch` does not yet.
- Per-column widths, free text notes, and a second line of small text under a label.
- A check of labels against the glossary (no glossary data exists yet), and a check of the reading direction.
- The Zoom button and the scroll container on the web are the web app's job. The inline SVG only sets `--dg-w` so the stylesheet can hold it at scale 0.75 or more.

## For tool authors

### Module map

| Module | Job |
|---|---|
| `schema.py` | Small JSON Schema validator (standard library). |
| `layout_grid.py` | Columns, rows, group tree, border lanes, label bands, node geometry. |
| `route.py` | Candidate routes, cost, port spreading, gutter tracks, local search, edge label and badge placement. |
| `arch.py` | The `arch` kind: iterates layout and routing until gutters and group labels fit; returns a scene. |
| `textmetrics.py`, `_widths.py` | Real Arial advance widths (table generated once by `tools/helpers/gen_font_widths.py` with fontTools) with a 5% safety margin. Diagram text uses the stack "Helvetica Neue", Helvetica, Arial, sans-serif. |
| `svg.py` | `render_standalone(scene, spec, icons)`, `render_inline(scene, spec, icons)`, `inline_css()`. |
| `lint.py` | `lint_spec` (limits) and `lint_scene` (geometry). |
| `icons.py` | Download, unpack, name map, cleaning, `icons.json`, sprite, notice. |
| `pipeline.py` | `check_spec`, `check_id`, `build_one`, `caption(spec)`, the kind registry. |
| `preview.py` | Preview page, headless Chrome, `shot_file`, contact sheet. |
| `style.py` | Every size, limit, palette and the group table. |
| `shapes.py` | Shared by the other kinds: measure and place a node, edge and text items, label lint helpers, `make_room_for_rings`. |
| `layout_sequence.py`, `layout_ladder.py`, `layout_states.py`, `layout_timeline.py`, `layout_compare.py`, `layout_raw.py` | One kind each: `KIND`, `build_scene`, `lint_spec`, and where needed `lint_scene` and `caption`. Their limits are constants at the top of the file. |

### Web app contract

- `render_inline()` returns one `<svg class="dg dg-arch" ... style="--dg-w:W">` with classes only: no ids, no `<style>`, no literal colours, transparent ground. Arrowheads are polygons.
- Put the output of `diagram css` in the shell once. It binds the classes to `--dg-ink`, `--dg-muted`, `--dg-edge`, `--dg-emph`, `--dg-node`, `--dg-teal`, `--dg-pub`, `--dg-vpc`, `--dg-sg`, `--dg-asg`, `--dg-acct`, `--dg-show-light`, `--dg-show-dark`. Step numerals use `var(--dg-ground, var(--surface, #fff))`.
- Put the sprite (`diagram sprite`, also written to `diagrams/icons.svg`) in the shell once. Icons are `<use href="#ic-NAME">`. The generic line-art icons also have `#ic-NAME-dark`; the two `<use>` elements carry the classes `dg-il` and `dg-id`, which the tokens `--dg-show-light` and `--dg-show-dark` switch.
- `pipeline.caption(spec)` returns the title, claim, alt text and the step list for the figure card.

### Adding a kind

Add `saalib/diagram/layout_<name>.py` with `KIND = "<kind>"` and `build_scene(spec) -> scene`. `pipeline.py` finds it by itself. Add the kind's branch to `oneOf` in `diagram.schema.json` (a closed object schema under `$defs` with `"kind": {"const": "<kind>"}`). `lint_scene` and both renderers work on any scene.

A kind module may also define:

| Name | Job |
|---|---|
| `lint_spec(spec, icons) -> issues` | Limit checks before layout. A code that starts with `ref-` stops the check before layout. |
| `lint_scene(scene, spec) -> (issues, stats)` | Replaces `lint.lint_scene` (compare lints each panel; raw has no geometry). |
| `caption(spec) -> dict` | Replaces the default caption (sequence returns its messages as steps). |
| `WANTS_BASE_DIR = True` | `lint_spec` and `build_scene` get the folder of the spec file as one more argument (raw). |

Array maxima in the schema are loose on purpose; the lint enforces the real limit with a readable message (`limit-actors`, `limit-rungs`, ...).

### Web app contract for the other kinds

- Extra classes (`dg-ll`, `dg-nt`, `dg-nf`, `dg-sp`, `dg-ax`, `dg-ev`, `dg-mt`, `dg-evl`, `dg-ph`) are part of `diagram css`. Standalone `arch` files do not carry them, so `arch` output did not change.
- `render_inline()` of a `compare` scene returns `<div class="dg-cmp">` with one `<div class="dg-cmp-p" style="--dg-w:W">` per panel, each holding a heading `<div class="dg-cmp-h">` and an `<svg class="dg dg-arch">`. `diagram css` carries the flex rules that stack the panels. `scene["phone_w"]` is the widest panel.
- `pipeline.build_one()` returns `result["panels"]`, the paths of `<id>.p<n>.svg`. `diagram sheet` skips those files.
- `pipeline.caption(spec)` works for every kind; only `arch` and `sequence` return steps.

### Scene

```
{ "kind", "id", "w", "h",
  "groups": [{ "id", "type", "label", "x", "y", "w", "h", "label_w", "label_box", "label_pos", "label_anchor", "depth" }],
  "nodes":  [{ "id", "icon" | None, "bbox", "icon_box" | None, "box" | None, "label_box", "shapes": [rect, ...],
               "lines": [{ "text", "x", "y", "w" }], "max_text_w", "ports", "emph" }],
  "edges":  [{ "index", "from", "to", "points": [(x, y), ...], "arrow", "emph", "dashed",
               "label": { "text", "x", "y", "anchor", "box", "w" } | None,
               "badge": { "n", "cx", "cy" } | None, "sides", "no_room" }],
  "texts":  [{ "text", "x", "y", "anchor", "cls", "box" }],
  "decor":  [{ "t": "line" | "rect" | "circle" | "poly", "cls", ... }] }
```

Rectangles are `(x, y, w, h)`. `decor` holds plain shapes drawn under the edges (lifelines, the axis, ticks); the lint only checks that they are inside the canvas.

Optional node keys used by the other kinds: `rx` (corner radius of the box), `box_cls` (class of the box, default `dg-nb`), `emph_fill` (highlight by filling the box, not by a ring), `inner` (second border, for a final state), `max_lines` (default 2).

Other scene shapes: a `compare` scene has `"panels": [{ "label", "x", "y", "head_y", "scene" }]` and no nodes of its own; a `raw` scene has `"raw"` (the parsed elements) and `"icons"`. An edge whose `from` or `to` is not a node id (a sequence message ends on a lifeline) skips the "arrow ends on a node" check.

### Tests

`python3 aws-saa-book/tools/tests/run.py diagram` runs `tests/test_diagram.py` and `tests/test_diagram_kinds.py` (the six other kinds: a clean case and must-fail cases for each, the compare panel files, the raw checks, and a check that every sample spec in the book is free of errors). `test_diagram.py` covers: schema must-fail cases, limit must-fail cases, geometry must-fail cases (overlap, overflow, an edge through a node, a detached arrow, clipping, too many crossings), byte-identical output for the same spec, and a golden file (`tests/fixtures/diagram/golden-three-tier.svg`). After an intended renderer change, delete the golden file and run the tests once to record it again, then look at the samples.
