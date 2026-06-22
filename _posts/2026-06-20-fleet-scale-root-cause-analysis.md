---
title: "Fleet-Scale Root-Cause Analysis: One Code, a Population of Evidence"
subtitle: "When the same trouble code lights up across a whole fleet and the evidence arrives in bulk — how to diagnose a population instead of a single car."
date: 2026-04-11 20:00:00 -0400
category: "Control Systems"
slug: fleet-scale-root-cause-analysis
excerpt: "The capstone of the diagnosis set. A single car gives you one observation; a fleet gives you a distribution — and a hypothesis must now explain not just that the code fired, but how common it is, who it happened to, and when it started spreading. Those stronger constraints are a gift, but they come with a trap: the same DTC across the fleet is usually a mixture of several root causes hiding behind one code, so you must de-mix the population before you diagnose it. We work through the fleet method in plain words — cluster the batch into homogeneous sub-populations, let the cohort boundary name each cause, defend against confounding and Simpson's paradox, aggregate batched evidence in two levels without double-counting, read the prevalence and onset curves for change-points, and turn the result into a remediation scope (OTA vs. recall vs. targeted). With a worked 6,000-vehicle scenario, figures, flowcharts, block diagrams, algorithms, practical notes, and references."
reading_time: 26
---

This is the fifth and final post in the diagnosis set, after [Root-Cause Analysis Under Uncertain, Heterogeneous Evidence]({{ '/posts/rca-under-uncertain-heterogeneous-evidence/' | relative_url }}), [When Is the Evidence Enough?]({{ '/posts/evidence-sufficiency-and-conflict/' | relative_url }}), and [Harder Cases in Diagnosis]({{ '/posts/harder-cases-in-diagnosis/' | relative_url }}). Those treated a single vehicle. This one scales up: the same trouble code appears across thousands of cars, and the rest of the evidence — telemetry summaries, warranty claims, service notes, build records — arrives as one big batch.

That sounds like more of the same, but it is a different problem. With one car you have a single observation and you ask &ldquo;what broke?&rdquo; With a fleet you have a *distribution*, and a valid explanation has to account for three things at once: **how common** the failure is, **who** it happens to, and **when** it started spreading. Those extra constraints make impostors much easier to kill — but they hide a new trap, the one that catches every fleet investigation: **the same code is rarely the same cause.** A common DTC across a fleet is usually a *mixture* of several mechanisms wearing one mask, and if you diagnose the batch as a single failure you will blend two real causes into one fictitious one.

So the fleet method has a different first move — *de-mix the population* — and a different last move: turn the diagnosis into a **remediation scope** (who gets an over-the-air fix, who gets a recall, who gets nothing). In between, the cohort contrast that was a side-check on one car becomes the main engine.

## What it covers

Thirteen sections, about twenty-six minutes, in plain language.

**§ 1 — From a car to a population.** Why a fleet hypothesis must explain prevalence, stratification, and onset — and why that makes diagnosis easier, not harder.

**Part A · One code, many causes**

**§ 2 — The mixture trap.** Why one DTC across the fleet is usually several root causes, and what averaging them costs you.

**§ 3 — De-mix first.** Clustering the batch into homogeneous sub-populations and running the method per cluster, with an algorithm and a block diagram.

**Part B · The cohort contrast is the engine**

**§ 4 — Let the boundary name the cause.** Stratifying affected vs. spared by build plant, firmware, lot, and climate — and reading the split.

**§ 5 — Confounding & Simpson's paradox.** Why a fleet-level correlation can reverse inside every subgroup, and why stratification is now mandatory.

**Part C · Aggregating batched evidence**

**§ 6 — Two levels, not one.** Summarizing per vehicle first, then reasoning across vehicles — and not letting volume manufacture false confidence.

**§ 7 — Messy by default.** Heterogeneous trust, missing data, and the selection and survivorship biases that warranty batches carry.

**Part D · Time and the decision**

**§ 8 — Read the curve.** Prevalence and onset over time, and change-points that pin the cause to a production change or an OTA.

**§ 9 — From cause to campaign.** Forecasting how many more will fail, and choosing the remediation scope — OTA, recall, or targeted service.

**§ 10 — The fleet procedure.** The whole method as one flowchart, with the master algorithm.

**§ 11 — A worked scenario.** A 6,000-vehicle fleet, one charging code, two hidden causes — start to finish.

**§ 12 — Practical notes.** Field rules for population-scale diagnosis.

**§ 13 — References & further reading.** Epidemiology, reliability, mixtures, and causal inference, with pointers.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/fleet-scale-root-cause-analysis.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL in the warm-paper layout of the series, with a mixture diagram, a stratification tree, a Simpson's-paradox panel, a two-level aggregation block diagram, prevalence and onset curves, a remediation-decision figure, the fleet RCA flowchart, three algorithms, and a worked 6,000-vehicle scenario.

## Where it sits

The diagnosis series, in order:

**I · The core method**

1. [Root-Cause Analysis Under Uncertain, Heterogeneous Evidence]({{ '/posts/rca-under-uncertain-heterogeneous-evidence/' | relative_url }})
2. [When Is the Evidence Enough?]({{ '/posts/evidence-sufficiency-and-conflict/' | relative_url }})
3. [Harder Cases in Diagnosis]({{ '/posts/harder-cases-in-diagnosis/' | relative_url }})

**II · At fleet scale**

4. **Fleet-Scale Root-Cause Analysis** — *(this post)*
5. [Fleet RCA, Made Rigorous]({{ '/posts/fleet-rca-made-rigorous/' | relative_url }})

**III · Proof, foundations & prevention**

6. [Proving Cause with Experiments]({{ '/posts/proving-cause-with-experiments/' | relative_url }})
7. [Diagnosis on the Vehicle]({{ '/posts/diagnosis-on-the-vehicle/' | relative_url }})
8. [The Data Plumbing Behind Fleet Diagnosis]({{ '/posts/data-plumbing-fleet-diagnosis/' | relative_url }})
9. [From Root Cause to No Cause]({{ '/posts/prevention-and-corrective-action/' | relative_url }})

Full map: [The Diagnosis Series index]({{ '/posts/diagnosis-series/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
