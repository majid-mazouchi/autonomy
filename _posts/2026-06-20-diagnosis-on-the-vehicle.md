---
title: "Diagnosis on the Vehicle: Real-Time Fault Detection at the Edge"
subtitle: "Everything so far happened at an analyst's desk. But the first diagnostician is the ECU — detecting faults in real time, on tiny compute, under a strict false-alarm budget."
date: 2026-06-20 23:40:00 -0400
category: "Control Systems"
slug: diagnosis-on-the-vehicle
excerpt: "The whole diagnosis series, until now, has been offline — an analyst with logs. But the first diagnostician is the car itself. This post drops down to the edge, where an ECU decides to set a code in a few milliseconds, with a few kilobytes, no labels, and a hard rule that it must not cry wolf. We build the on-board detector from model-based observers and residuals, layer the cheap limit and plausibility checks beneath them, and add lightweight on-vehicle anomaly detection. Then we meet the two forces that shape every edge decision: a punishing false-alarm budget that demands debouncing and fault maturation, and the ISO 26262 / ASIL safety regime that keeps edge diagnosis bounded and auditable. Finally we close the loop — the car emits a DTC, freeze-frame, and snapshot that feed the offline fleet RCA pipeline, and fleet RCA tunes the detector's thresholds and ships them back by OTA. Worked throughout on one fault: charging code P0AE0, a high-resistance charge connector, caught by the car itself."
reading_time: 22
---

So far, this whole diagnosis series has lived at an analyst's desk — logs, a workstation, the full history of a car or a fleet, and time to think. But the very first diagnostician is the vehicle itself. Long before charging code `P0AE0` reaches a fleet database, an *electronic control unit* decided to set it: in a few milliseconds, with a few kilobytes of RAM, with no labels and no second chances, under a hard rule that it must *not* cry wolf. This post drops down to that edge and builds the on-board detector from the ground up, then connects it back to the offline methods of the rest of the series.

It is the on-vehicle complement to [Fault Detection and Isolation]({{ '/posts/fault-detection-isolation/' | relative_url }}), which laid out the theory of residuals and isolation. Here we put that theory under the constraints of real embedded hardware — and we follow one fault all the way through: a high-resistance charge connector that sets `P0AE0`, caught by the car itself and handed up to the fleet pipeline.

## What it covers

Ten sections, about twenty-two minutes, in plain language with diagrams and worked logic.

**Part A · How a vehicle detects its own faults**

**§ 2 — Model-based observers & residuals.** A model predicts a signal from the others; the residual is measured − predicted; threshold it to flag a fault. Parity relations and the Kalman/Luenberger observer in plain words, with a residual-monitor algorithm.

**§ 3 — Limit, plausibility & rate checks.** The cheap first line — range, stuck-at, and impossible-rate checks — running every loop beneath the model.

**§ 4 — Edge ML.** Lightweight on-vehicle anomaly detection: a tiny autoencoder trained on healthy data, and the four walls it lives in — memory, latency, no labels, drift (and OTA updates).

**Part B · The constraints that shape it**

**§ 5 — The false-alarm budget & debouncing.** Why on-board must be conservative, the real cost of a false MIL, and fault-maturation counters that store a code only after it trips N times under set-conditions.

**§ 6 — Safety & certification.** ISO 26262 / ASIL, determinism, freedom from interference, and auditability — why edge diagnosis is bounded where cloud ML is free.

**Part C · Edge meets cloud**

**§ 7 — The closed loop.** On-board detection emits a DTC, freeze-frame, and snapshot up to the fleet pipeline; fleet RCA tunes the thresholds and ships them back by OTA — the detector improves itself.

**§ 8 — Worked example.** Detecting the high-resistance connector on-board: an observer on charge voltage, a residual that grows under high current, maturation over several charges, then `P0AE0` stored with a freeze-frame that seeds the fleet de-mix.

**§ 9 — Practical notes.** Field rules for diagnosis at the edge.

**§ 10 — References & further reading.** Fault diagnosis, estimation, functional safety, and embedded ML, with pointers.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/diagnosis-on-the-vehicle.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL in the warm-paper layout of the series, with an observer/residual block diagram, an edge-ML pipeline figure, a debounce/maturation counter trace, the edge↔cloud closed-loop diagram, two algorithms, a worked `P0AE0` example in verdict cards, practical notes, and references.

## Where it sits

The diagnosis series, in order:

**I · The core method**

1. [Root-Cause Analysis Under Uncertain, Heterogeneous Evidence]({{ '/posts/rca-under-uncertain-heterogeneous-evidence/' | relative_url }})
2. [When Is the Evidence Enough?]({{ '/posts/evidence-sufficiency-and-conflict/' | relative_url }})
3. [Harder Cases in Diagnosis]({{ '/posts/harder-cases-in-diagnosis/' | relative_url }})

**II · At fleet scale**

4. [Fleet-Scale Root-Cause Analysis]({{ '/posts/fleet-scale-root-cause-analysis/' | relative_url }})
5. [Fleet RCA, Made Rigorous]({{ '/posts/fleet-rca-made-rigorous/' | relative_url }})

**III · Proof, foundations & prevention**

6. [Proving Cause with Experiments]({{ '/posts/proving-cause-with-experiments/' | relative_url }})
7. **Diagnosis on the Vehicle** — *(this post)*
8. [The Data Plumbing Behind Fleet Diagnosis]({{ '/posts/data-plumbing-fleet-diagnosis/' | relative_url }})
9. [From Root Cause to No Cause]({{ '/posts/prevention-and-corrective-action/' | relative_url }})

Full map: [The Diagnosis Series index]({{ '/posts/diagnosis-series/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
