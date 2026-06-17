---
title: "Tonal NVH During Battery Preconditioning — Root Cause Investigation"
subtitle: "A fleet-level acoustic complaint traced from symptom to electromagnetic mechanism: how high d-axis injection, magnetic saturation, and a structural resonance conspire to produce an audible 6th-order drone — and how to silence it."
date: 2026-06-11 16:00:00 -0400
category: "Control Systems"
slug: nvh-preconditioning-rca-report
excerpt: "Case 2 of 5. A tonal whine during battery preconditioning, reported by drivers in cold-climate fleets. The investigation traces three independent design choices — d-axis current injection for active heating, the resulting magnetic saturation in the stator iron, and a structural eigenmode of the motor mount near the 6th electrical order — that conspire to produce an audible NVH event. With synthetic data from a 320-vehicle instrumented fleet and the Python generator that reproduces it."
reading_time: 20
---

This is Case 2 of the five-part RCA series. The previous case ([battery degradation]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }})) was a software/firmware root cause — the kind of finding that resolves with an OTA. This one is the opposite end of the spectrum: an *electromagnetic-structural interaction* that is purely a physics problem, and where the fix has to come from the controller, the mechanical design, or both.

The complaint: a tonal whine during battery preconditioning in cold-climate vehicles. The investigation finds it traces to three independent design choices interacting. The active-heating mode injects current along the d-axis of the traction motor to dissipate power and warm the cells. That d-axis current pushes the stator iron into magnetic saturation, producing harmonic content at the 6th electrical order. The 6th order, in the operating-temperature band for preconditioning, happens to fall right on a structural eigenmode of the motor-mount system. The result is an audible drone that vanishes the moment preconditioning ends.

Each ingredient is innocent on its own. The combination is the lesion. This is the central pattern in NVH root-cause work — the cause is rarely "this one part is broken"; it's "these three correct choices interact in a way nobody simulated." The investigation has to find all three.

## What it covers

Twelve sections, about twenty minutes of careful reading.

**§ 1–3 — The complaint, the localization, the spectrogram.** The customer reports. The fleet-level signal. The acoustic signature that identifies it as a 6th-order phenomenon.

**§ 4–6 — The electromagnetic mechanism.** D-axis current injection in active heating. The saturation curve. Why the 6th order is the harmonic that escapes when saturation kicks in.

**§ 7–9 — The structural resonance.** The motor-mount modal analysis. The eigenmode that lives at the operational frequency band. The transfer function from electromagnetic forcing to cabin acoustic pressure.

**§ 10–11 — The mitigation strategies.** Three independent fixes, each addressing one ingredient. Reduce d-axis injection (control-side). Shift the resonance (mechanical-side). Notch-filter the 6th order (signal-side). The trade-off matrix.

**§ 12 — The validated mitigation.** Which combination of fixes actually silences the drone in the next simulation cycle.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/nvh-preconditioning-rca-report.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open Case 2 →
  </a>
</div>

The report lives at its own URL with a warm-paper engineering-document layout — petrol-blue accent, color-coded for symptom (red), mechanism (amber), mitigation (green).

## Code & data

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/nvh-rca-code-and-data.zip' | relative_url }}" download>nvh-rca-code-and-data.zip</a> — the Python generator (<code>nvh_precond_rca.py</code> + <code>nvh_prog.py</code>), the simulated 320-vehicle fleet (<code>nvh_fleet.csv</code>), and a README.</p>
</div>

## The full series

Case 2 of 5. Read the rest in order:

1. [Battery Degradation Case Study]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }}) — software / firmware
2. **Preconditioning-Mode NVH** — *(this post)* — electromagnetic / structural
3. [Module Weld Resistance]({{ '/posts/manufacturing-rca-report/' | relative_url }}) — tooling / manufacturing
4. [HV Isolation Faults]({{ '/posts/environmental-rca-report/' | relative_url }}) — environmental (condensation)
5. [Brake Rotor Corrosion]({{ '/posts/usage-rca-report/' | relative_url }}) — usage / behavior

Followed by the [agentic framework]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}) that automates the method, and its [worked walkthrough]({{ '/posts/framework-battery-walkthrough/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
