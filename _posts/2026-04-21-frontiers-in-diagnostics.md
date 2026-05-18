---
title: "Frontiers in Diagnostics"
subtitle: "Where the textbooks end. The open problems of putting fault diagnosis into real fleets, real ECUs, with real data and real certification."
date: 2026-04-21 10:00:00 -0400
category: "Control Systems"
slug: frontiers-in-diagnostics
excerpt: "Monograph No. 4 of the diagnostics series. The gap between textbook FDI and deployed FDI — domain shift, certification, edge-deployment, fleet-scale digital twins, unlabeled anomaly detection, and distributed diagnosis."
reading_time: 12
---

The first three monographs in this series — [FDI]({{ '/posts/fault-detection-isolation/' | relative_url }}), [FTC]({{ '/posts/fault-tolerant-control/' | relative_url }}), [PHM]({{ '/posts/prognostics-health-management/' | relative_url }}) — covered the engineering of fault-handling as the textbooks present it. Clean models, clean problems, clean algorithms. This one covers what happens when you try to put any of it into a real production system.

It turns out the gap between textbook and fleet is enormous. The model you trained on one engine doesn't work on a different one. Your beautiful neural network won't fit in 64 KB. The regulator wants explanations for every decision. The labels you assumed don't exist. The system you're diagnosing isn't even *one* system — it's fifty computers on a CAN bus, only some of which talk to you.

This monograph is the fourth and final post in the diagnostics series, and it's a survey of the open problems that the field is actively working on:

1. [**Fault Detection and Isolation**]({{ '/posts/fault-detection-isolation/' | relative_url }})
2. [**Fault-Tolerant Control**]({{ '/posts/fault-tolerant-control/' | relative_url }})
3. [**Prognostics and Health Management**]({{ '/posts/prognostics-health-management/' | relative_url }})
4. **Frontiers in Diagnostics** (this post)

## What it covers

Eight chapters. About forty-five minutes to read.

**§1 — The gap between the textbook and the fleet.** The recurring observation that motivates everything else in the post.

**§2 — Domain adaptation.** Training here, deploying there. Why the model doesn't transfer and what to do about it. CORAL, DANN, the small set of practical techniques.

**§3 — Physics-informed neural networks.** Physics as regularizer. The hybrid approach that's eating both pure-physics and pure-data approaches.

**§4 — Explainable AI.** The certification problem. Why "the model said so" isn't an answer that survives an aerospace audit, and what counts as a decision-grade explanation.

**§5 — Edge deployment.** The 64 KB constraint. What survives when you have to fit a diagnostic model on a microcontroller alongside the control software it's monitoring.

**§6 — Digital twins at fleet scale.** When you have ten thousand identical units in the field, the per-unit model can be richer than any one engineer could maintain. The architecture and economics of fleet-scale telemetry.

**§7 — Anomaly detection without labels.** The reality: failures are rare, labels are non-existent, and you have to find faults using only the structure of normal data. SVDD, one-class methods, deep autoencoders.

**§8 — Distributed FDI.** When the "system" is fifty computers on a CAN bus. Consensus algorithms, redundant diagnosis, the new constraints that come with distribution.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/frontiers-in-diagnostics.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open Monograph No. 4 →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
