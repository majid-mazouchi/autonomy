---
title: "Friction-Brake Rotor Corrosion — Usage/Behavior Root Cause Report"
subtitle: "Brake noise and reduced initial bite, blamed at first on a rotor supplier lot — traced instead to a driving-behavior pattern: one-pedal driving leaves the friction brakes so rarely used that the rotors never scrub clean and rust accumulates."
date: 2026-06-11 22:00:00 -0400
category: "Control Systems"
slug: usage-rca-report
excerpt: "Case 5 of 5 — and the case that almost everyone gets wrong on the first pass. Brake noise and reduced initial bite in a subpopulation of EVs. The Pareto says it's a rotor lot; the truth is a driving-behavior pattern. One-pedal driving (regenerative braking does almost all the deceleration) means the friction brakes are barely used, so the rotors never scrub clean, so they rust. The fix isn't a recall — it's an automated brake-scrub cycle plus driver guidance. With synthetic data from a 500-vehicle usage-logged study."
reading_time: 17
---

This is Case 5 of the five-part RCA series — and the trickiest of the five, because it's the case where the cause is *the driver*, not the vehicle, and the engineering solution has to bend toward driver behavior rather than against it.

The complaint: brake noise and reduced initial bite from the friction brakes in a subpopulation of EVs. The Pareto, predictably, points at a rotor supplier lot. The investigation has to refuse it (again) and look at *how* the affected vehicles are being driven. The pattern, once you look for it, is clear: the affected vehicles are the ones whose drivers commit to one-pedal driving — using regenerative braking for nearly all decelerations, never touching the friction brake pedal. The rotors, never scrubbed clean by friction-brake engagement, accumulate a layer of rust. The noise and reduced bite are the rust, not a defect.

The fix is a software change, not a hardware recall. The vehicle implements a periodic *automated brake-scrub* cycle — a brief, low-pressure friction-brake engagement during low-speed coasting that wears the rust off without the driver noticing. Plus a one-time driver-education prompt suggesting an occasional manual brake use in wet weather. The combination drops the complaint rate to baseline within a quarter.

This is the *usage/behavior* RCA pattern — the cause is a legitimate, even desirable driving style, and the fix is a system-design accommodation rather than a fault-correction. It's also the case that requires the most discipline to find, because the "obvious" answer (the rotor lot) is institutionally easier than the right answer ("it's how people are driving"). 

## What it covers

Eleven sections, about seventeen minutes of careful reading.

**§ 1–2 — The complaint.** Brake noise, reduced initial bite. The customer-service signals. The first-pass engineering response.

**§ 3–4 — The rotor-lot impostor.** The Pareto fit. The cross-validation that breaks it (some vehicles in the suspect lot are fine; some outside it are not).

**§ 5–7 — The behavior dimension.** Looking at usage data alongside the symptom. The one-pedal-driving correlation that emerges when you stratify by *how often the friction brake is pressed* rather than by *which supplier lot the rotors came from*.

**§ 8–9 — The rust mechanism.** Why a never-scrubbed rotor accumulates rust faster than the design assumed. The humidity-temperature interaction that makes it worse in some climates.

**§ 10–11 — The software fix.** The automated brake-scrub cycle. The driver-education prompt. The validation: complaint rate drops to baseline within one quarter post-OTA.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/usage-rca-report.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open Case 5 →
  </a>
</div>

The report lives at its own URL with a warm-paper engineering-document layout — plum accent for the usage-behavior motif, classical RCA-report styling throughout.

## Code & data

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/usage-rca-code-and-data.zip' | relative_url }}" download>usage-rca-code-and-data.zip</a> — the Python generator (<code>brake_corrosion_rca.py</code>), the synthetic 500-vehicle dataset (<code>brake_fleet.csv</code>), and a README.</p>
</div>

## The full series

Case 5 of 5. Read the rest in order:

1. [Battery Degradation Case Study]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }}) — software / firmware
2. [Preconditioning-Mode NVH]({{ '/posts/nvh-preconditioning-rca-report/' | relative_url }}) — electromagnetic / structural
3. [Module Weld Resistance]({{ '/posts/manufacturing-rca-report/' | relative_url }}) — tooling / manufacturing
4. [HV Isolation Faults]({{ '/posts/environmental-rca-report/' | relative_url }}) — environmental (condensation)
5. **Brake Rotor Corrosion** — *(this post)* — usage / behavior

Followed by the [agentic framework]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}) that automates this method, and its [worked walkthrough]({{ '/posts/framework-battery-walkthrough/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
