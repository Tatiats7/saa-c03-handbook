# EC2 Purchasing Options: the 30-minute cheat sheet

## The whole picture in 30 seconds

Keep two questions apart:

1. **How much do I pay per hour?** (the price axis)
2. **Is the hardware guaranteed to be there when I launch?** (the capacity axis)

Spot, Reserved Instances and Savings Plans change the price. Capacity Reservations, Capacity Blocks and Dedicated Hosts hold hardware. Only the zonal Reserved Instance does both.

Three sentences to keep in your head:

- **Discounts are billing rules, not machines.** A Reserved Instance or a Savings Plan is a rule that lowers the rate on machines you launch anyway.
- **Guarantees are always about one Availability Zone.** Nothing "regional" holds any hardware.
- **On-Demand is the reference price.** Every discount is measured against it, and every unused reservation is billed at it.

| Option | What it changes | Commitment | Can you cancel? | Saving vs On-Demand |
|---|---|---|---|---|
| On-Demand | Nothing. The baseline. | None | Stop any time | 0% |
| Spot | Price. AWS may take the machine back. | None | Any time. AWS can too. | Up to ~90% |
| Reserved Instance (RI) | Price. Zonal RIs also hold capacity. | 1 or 3 years | No. Standard RIs can be sold. | Up to ~72% |
| Savings Plan (SP) | Price | 1 or 3 years, in $/hour | Only a 7-day return for small plans | Up to ~72% (EC2 Instance), ~66% (Compute) |
| On-Demand Capacity Reservation (ODCR) | Capacity in one AZ | None, or 14 days if future-dated | Yes. Future-dated ones carry fees. | None. An SP or regional RI discounts it. |
| Capacity Block for ML | GPU capacity for a fixed window | The whole window, paid up front | Never | None. Often above On-Demand. |
| SageMaker Training Plan | Same idea, inside SageMaker | The whole plan, paid up front | Never | None |
| Dedicated Instance | Tenancy: only your account on the server | None | Stop any time | Costs more, plus $2/hour per Region |
| Dedicated Host | Tenancy: a whole server you name | None, or a 1- or 3-year Host Reservation | Release any time, unless reserved | Costs more. Pays off with your own licences. |

## The nine cards

### 1. On-Demand

**Say it in one breath.** Pay per second for what you run, stop paying when you stop, no promises either way.

**What it really is.** You launch a machine, pay per second while it runs, and pay nothing when it stops. No commitment, no upfront payment. Every other option is defined against this price.

**Use it when**
- You are still experimenting and don't know which family you will settle on.
- The work runs less than roughly 60 to 70% of the hours in a month.
- It is the first few months of a new workload, so Cost Explorer has real usage before you commit.
- It is a spike on top of a committed base.

**Don't use it when**
- The machines run all day, every day, for a year or more. That is Savings Plan money.
- The work can be interrupted and restarted. That is Spot money.

**Good**
- No exit cost. Nothing locks you in, nothing can be taken away.
- Stopped machines cost only their disks.

**Bad**
- The most expensive way to run anything steady.
- No guarantee the hardware exists when you launch. "Insufficient capacity" errors happen.

**Traps**
- Quotas, not price, are the first wall. They count vCPUs per Region. A fresh account gets 5 vCPUs for standard families and 0 for GPU families. Ask for an increase before the demo.
- Billing has a 60-second minimum, and every stop-then-start restarts it. A reboot does not.

**Works together with.** Everything. Discounts (RI, SP) lower its rate. Reservations (ODCR) hold hardware for it. Tenancy changes which server it runs on.

**Numbers to remember.** Per-second billing, 60-second minimum. Default quota: 5 vCPUs standard, 0 GPU. Commit only above roughly 60 to 70% monthly use.

**If it goes deeper:** [Guide §2](ec2-purchasing-options-guide.md#2-on-demand-the-baseline-everything-else-is-measured-against)

### 2. Spot

**Say it in one breath.** Spare machines at up to 90% off, but AWS can take them back with 2 minutes' notice.

**What it really is.** The same hardware and images as On-Demand, with one difference: AWS can interrupt the machine with a 2-minute warning when it needs the capacity back. AWS sets the price per instance type per AZ. There is no bidding any more.

**Use it when**
- The work can stop and restart: batch jobs, rendering, CI runners, big-data task nodes, ML training with checkpoints.
- Containers behind a load balancer, as the flexible layer on a committed base.

**Don't use it when**
- The work is stateful, cannot tolerate failure, or is tightly coupled across machines. Databases are the classic no.
- You need a guaranteed window. Fixed-duration Spot "blocks" no longer exist. Use ODCRs or Capacity Blocks.

**Good**
- The biggest saving available, with zero commitment.
- If AWS interrupts you in the first hour, that hour is free (Linux and Windows).
- On interruption you choose: terminate, stop, or hibernate.

**Bad**
- Any machine can vanish. Interruption rates differ by type. The Spot Instance Advisor shows 30-day averages.
- One instance type in one AZ means one tight pool can stall your whole job.

**Traps**
- Don't set a maximum price. It only gets you interrupted more.
- Don't fail over to On-Demand automatically. AWS "strongly discourages" it: it can cause more interruptions for your other Spot machines.
- The old Spot request APIs are "do not use". Use an Auto Scaling group or EC2 Fleet.
- Spot hours never count toward a Savings Plan and are never covered by an RI.
- Mac is never Spot.

**Works together with.** Nothing on the same machine: no RI, SP, ODCR or Capacity Block. In the same fleet, yes: a Savings Plan on the steady base, Spot on the burst.

**Numbers to remember.** Up to 90% off. 2-minute notice. Be flexible across 10 or more instance types and several AZs. Use the price-capacity-optimized strategy. First hour free if AWS interrupts.

**If it goes deeper:** [Guide §3](ec2-purchasing-options-guide.md#3-spot-instances-pay-much-less-accept-that-the-instance-can-be-taken-back)

### 3. Reserved Instances (RI)

**Say it in one breath.** A 1- or 3-year promise to pay for one exact machine shape, for up to 72% off. AWS now says buy Savings Plans.

**What it really is.** Not a machine. A billing rule: "any running instance matching this type, Region, tenancy and OS is billed at the lower rate". You pay every hour of the term whether anything runs or not.

Two choices define it:

- **Regional vs zonal.** Regional: any AZ in the Region, size-flexible within the family (Linux, shared tenancy only), holds no hardware. Zonal: one AZ, exact size, but it does hold capacity there. Almost everyone should buy regional.
- **Standard vs Convertible.** Standard: bigger discount, never exchanged, can be sold on the RI Marketplace. Convertible: smaller discount, can be exchanged for another family, OS or tenancy, cannot be sold.

**Use it when**
- You want capacity in one AZ bundled with the discount (zonal). Compare with ODCR plus Savings Plan first.
- You may need to sell it later, or finance wants a resellable asset (Standard only).

**Don't use it when**
- Anything else. AWS's documentation opens with "We recommend Savings Plans over Reserved Instances."

**Good**
