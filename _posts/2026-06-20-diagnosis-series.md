---
title: "The Diagnosis Series: A Reading Map"
subtitle: "Nine connected pieces, from one car's messy evidence to a fleet-wide campaign — and back around to preventing the fault entirely."
date: 2026-06-21 09:00:00 -0400
category: "Control Systems"
slug: diagnosis-series
excerpt: "An index and reading map for the nine-part diagnosis series. It is one long argument: turn untrustworthy evidence into a cause, know when you have enough to conclude, handle the hard cases, scale to a fleet, make the fleet methods statistically honest, prove cause with real experiments, push detection onto the vehicle, lay the data foundation, and close the loop with prevention. Start at the beginning or jump to the part you need."
reading_time: 4
---

This is the hub for a nine-part series on disciplined fault diagnosis — one long argument told in order, from a single vehicle's pile of untrustworthy clues all the way to a fleet-wide remediation campaign and back around to engineering the fault out for good.

## The visual map

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/diagnosis-series-index.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the series map →
  </a>
</div>

## The nine parts

**I · The core method**

1. [Root-Cause Analysis Under Uncertain, Heterogeneous Evidence]({{ '/posts/rca-under-uncertain-heterogeneous-evidence/' | relative_url }}) — grade, anchor, and fuse messy, unequal-trust clues into one defensible cause.
2. [When Is the Evidence Enough?]({{ '/posts/evidence-sufficiency-and-conflict/' | relative_url }}) — the sufficiency gate, value of information, the stopping test, and handling conflict.
3. [Harder Cases in Diagnosis]({{ '/posts/harder-cases-in-diagnosis/' | relative_url }}) — multiple faults, intermittency, and lying sensors.

**II · At fleet scale**

4. [Fleet-Scale Root-Cause Analysis]({{ '/posts/fleet-scale-root-cause-analysis/' | relative_url }}) — de-mix the mixture, let the cohort boundary name the cause, decide a campaign.
5. [Fleet RCA, Made Rigorous]({{ '/posts/fleet-rca-made-rigorous/' | relative_url }}) — significance, surveillance, forecasting, and closing the loop.

**III · Proof, foundations & prevention**

6. [Proving Cause with Experiments]({{ '/posts/proving-cause-with-experiments/' | relative_url }}) — DAGs, staged rollouts as randomized experiments, difference-in-differences, instrumental variables.
7. [Diagnosis on the Vehicle]({{ '/posts/diagnosis-on-the-vehicle/' | relative_url }}) — real-time detection at the edge, feeding the fleet pipeline.
8. [The Data Plumbing Behind Fleet Diagnosis]({{ '/posts/data-plumbing-fleet-diagnosis/' | relative_url }}) — joining, aligning, and cleaning the data that makes it all possible.
9. [From Root Cause to No Cause]({{ '/posts/prevention-and-corrective-action/' | relative_url }}) — prevention and the corrective-action loop.

**IV · Build the system**

10. [From Method to Product]({{ '/posts/agentic-fleet-diagnosis-architecture/' | relative_url }}) — the architecture of an AI-powered, multi-agent fleet-diagnosis tool: data, detection, agents, tools, memory, and the human in the loop.

## Where to start

New to the topic? Read **1 → 2 → 3** for the reasoning discipline, then **4 → 5** for fleets. Already do this work and want the sharp edges? Jump to **5** (rigor), **6** (proof), or **9** (prevention). Building the system rather than doing the analysis? Start with **8** (data) and **7** (edge).

---

← Back to [Autonomy]({{ '/' | relative_url }})
