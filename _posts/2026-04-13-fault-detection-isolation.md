---
title: "Fault Detection and Isolation"
subtitle: "When a sensor lies, an actuator slips, or a component drifts — what does the system see, and how does it know?"
date: 2026-04-13 10:00:00 -0400
category: "Control Systems"
slug: fault-detection-isolation
excerpt: "Monograph No. 1 of a four-part series on diagnostics and fault-handling. The classical model-based methods (observers, parity, Kalman), the data-driven methods (residuals, classifiers, anomaly detection), and the hybrid frontier."
reading_time: 11
---

A control engineer's job is, at one level, the design of systems that work. At a slightly more honest level, it's the design of systems that *keep working* when something goes wrong. Sensors fail, actuators wear, components drift, the operating point shifts. Every working production system has a fault-handling layer underneath, even if it's just a watchdog timer and a graceful shutdown. The richer the fault-handling, the more capable the system can be allowed to act autonomously.

Fault Detection and Isolation (FDI) is the first piece of that fault-handling layer. Detection answers *did something go wrong?* Isolation answers *what?* Without a clean answer to both, you can't have intelligent fault response, and you can't have certifiable autonomous systems at all. This monograph is the introduction to how engineers do it.

It's the first of a four-part series:

1. **Fault Detection and Isolation** (this post)
2. [**Fault-Tolerant Control**]({{ '/posts/fault-tolerant-control/' | relative_url }}) — what to do once you've found the fault
3. [**Prognostics and Health Management**]({{ '/posts/prognostics-health-management/' | relative_url }}) — predicting the next one
4. [**Frontiers in Diagnostics**]({{ '/posts/frontiers-in-diagnostics/' | relative_url }}) — the open problems

## What it covers

Five chapters plus references. About forty minutes to read carefully.

**§1 — A system that watches itself.** The architecture of an FDI module. What "residual" means and why it's the central object of the field.

**§2 — Model-based methods.** Observers, parity equations, Kalman filters as residual generators. The classical backbone that ships in every aerospace and process-control system.

**§3 — Data-driven methods.** PCA, classifiers, anomaly detection. The methods that took over wherever a high-fidelity model wasn't available — which is, increasingly, everywhere.

**§4 — Hybrid methods.** The current frontier. Physics-informed neural networks, model-aided learning, the small toolkit that's eating both ends of the field.

**§5 — The design problems that decide everything.** Detectability, isolability, sensitivity to false alarms, robustness to operating-point change. The cross-cutting questions that decide whether a chosen method actually works on a chosen plant.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/fault-detection-isolation.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open Monograph No. 1 →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
