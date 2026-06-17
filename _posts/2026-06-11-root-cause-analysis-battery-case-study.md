---
title: "The Anatomy of a Root Cause — A Battery Degradation Case Study"
subtitle: "A fleet of batteries is aging too fast. The statistics point one way, the physics another. This is how you tell a true cause from a convincing impostor."
date: 2026-06-11 14:00:00 -0400
category: "Control Systems"
slug: root-cause-analysis-battery-case-study
excerpt: "Case 1 of a five-part series on root-cause analysis in vehicle health monitoring. We follow a single anomaly — a cohort of electric vehicles losing battery health faster than the model allows — from first alarm to confirmed root cause and forward into a prognosis. Along the way we meet the central hazard of diagnostics: a feature that correlates beautifully with failure but causes nothing. The tool that rescues us is abduction, disciplined by partial correlation and ultimately by physics. With synthetic data from a 240-vehicle simulated fleet (known ground truth) and the Python generator that produces it."
reading_time: 22
---

This is Case 1 of a five-part series of worked root-cause analyses, each in a different failure family. Together they trace the **diagnostics-and-prognostics method** as it is actually practiced in vehicle health monitoring — not as a textbook flowchart, but as a discipline of *abduction* (inference to the best explanation) under the pressure of incomplete data and physical constraints. The five cases are paired with the [agentic framework]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}) that automates this method, and a [worked walkthrough]({{ '/posts/framework-battery-walkthrough/' | relative_url }}) of the framework running on this very battery case.

The battery case is first because it's the most familiar terrain — everyone working in EVs has had a version of this conversation. A subpopulation of vehicles in the fleet is losing battery state-of-health faster than the model predicts. The statistics seize on a "convincing impostor" — a feature that correlates beautifully with the degradation but is not the cause. The investigation has to get past that correlation, find the real lesion (a firmware balancing bug in a specific cell-pack revision), and then forecast forward — what's the remaining useful life of vehicles still on that firmware, and what does the trajectory look like after the OTA fix lands.

It is the natural companion to the [Optimal Control]({{ '/posts/optimal-control-field-guide/' | relative_url }}) and [Adaptive Control]({{ '/posts/adaptive-control-field-guide/' | relative_url }}) field guides on this site — those documents cover the *controllers* that run on the battery; this one covers the *diagnostic* layer that watches them.

## What it covers

Twelve sections, about twenty-two minutes of careful reading.

**§ 1–2 — The alarm and the anomaly.** A subpopulation deteriorates. The signal that wakes the analyst up. The naïve regressions that look like the answer but aren't.

**§ 3–4 — The impostor.** The convincing correlation that the entire room initially believed. Why it's wrong. The partial-correlation test that breaks it.

**§ 5–6 — Abduction and the physics gate.** Generating hypotheses honestly. The discipline of letting physics referee. The battery-aging model used as the simulator-of-record.

**§ 7–8 — The lesion identified.** Walking the data from the suspected firmware bug back through to the cell-balancing algorithm. The smoking gun in the telemetry.

**§ 9–10 — Prognosis & forecast.** What happens to the affected vehicles if the firmware is fixed today, in three months, in a year. The RUL curves with and without intervention.

**§ 11–12 — Lessons & method.** What this case teaches about the *general* method of diagnostics. The traps that catch every analyst at least once. The principles that survive being applied to the four other failure families in the series.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/root-cause-analysis-battery-case-study.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open Case 1 →
  </a>
</div>

The case study lives at its own URL with a warm-paper editorial layout — rust accent, teal supporting accent, slate for neutral text. All figures computed from a simulated 240-vehicle fleet with a known ground truth so the analysis can grade its own detective work.

## Code & data

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/battery-rca-code-and-data.zip' | relative_url }}" download>battery-rca-code-and-data.zip</a> — the Python generator (<code>battery_rca.py</code>), the simulated 240-vehicle fleet (<code>fleet.csv</code>), and a README. Reproducible from a single command.</p>
</div>

## The full series

This is Case 1 of 5. The full reading order:

1. **The Anatomy of a Root Cause** — *(this post)* — software / firmware
2. [Preconditioning-Mode NVH]({{ '/posts/nvh-preconditioning-rca-report/' | relative_url }}) — electromagnetic / structural
3. [Module Weld Resistance]({{ '/posts/manufacturing-rca-report/' | relative_url }}) — tooling / manufacturing
4. [HV Isolation Faults]({{ '/posts/environmental-rca-report/' | relative_url }}) — environmental (condensation)
5. [Brake Rotor Corrosion]({{ '/posts/usage-rca-report/' | relative_url }}) — usage / behavior

Followed by the framework that automates this method: [A Human-Gated Agentic Framework for RCA & Prognostics]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}), with a [worked walkthrough]({{ '/posts/framework-battery-walkthrough/' | relative_url }}) running it on this very case.

---

← Back to [Autonomy]({{ '/' | relative_url }})
