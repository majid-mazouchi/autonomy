---
title: "Prognostics and Health Management"
subtitle: "Reactive fault-handling tells you what just broke. Prognostics tells you what's about to."
date: 2026-04-17 10:00:00 -0400
category: "Control Systems"
slug: prognostics-health-management
excerpt: "Monograph No. 3 of the diagnostics series. Remaining Useful Life, degradation modeling, health indicators, the uncertainty question, and the maintenance scheduling that uses all of it."
reading_time: 10
---

[FDI]({{ '/posts/fault-detection-isolation/' | relative_url }}) and [FTC]({{ '/posts/fault-tolerant-control/' | relative_url }}) operate after the fact. By the time they fire, something has already changed. Prognostics asks the opposite question — *how much longer will this component keep working?* — and pushes the diagnostic story forward in time. The economic stakes are enormous: a fleet that knows which of its assets needs maintenance next week has a fundamentally different cost structure than one that doesn't.

This monograph is the third of a four-part diagnostics series:

1. [**Fault Detection and Isolation**]({{ '/posts/fault-detection-isolation/' | relative_url }})
2. [**Fault-Tolerant Control**]({{ '/posts/fault-tolerant-control/' | relative_url }})
3. **Prognostics and Health Management** (this post)
4. [**Frontiers in Diagnostics**]({{ '/posts/frontiers-in-diagnostics/' | relative_url }})

## What it covers

Six chapters plus references. About thirty-five minutes to read.

**§1 — Forward in time.** What prognostics actually predicts and why the question is harder than "estimate the time of failure." The framing that separates this field from FDI.

**§2 — Remaining Useful Life as a first-passage time.** The mathematical object underneath all of prognostics: when does a stochastic degradation process first cross a failure threshold? Brownian motion, Wiener processes, the algebra that makes RUL estimation tractable.

**§3 — Degradation modeling.** The shape of getting old. Linear, exponential, gamma-process, Wiener with drift. Which model fits which physical mechanism (wear, fatigue, corrosion, dielectric breakdown).

**§4 — Health indicators.** Squeezing many sensors into one scalar. PCA, autoencoders, physics-derived indicators. Why a good HI matters more than a good RUL estimator.

**§5 — Uncertainty — often more important than the estimate.** A point estimate of RUL without a credibility interval is worse than useless — it's actively dangerous. The uncertainty quantification techniques that make prognostics decision-grade.

**§6 — Condition-based and predictive maintenance.** Where all of this gets used. The scheduling problem on top of the prediction problem.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/prognostics-health-management.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open Monograph No. 3 →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
