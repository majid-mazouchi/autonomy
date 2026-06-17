---
title: "HV Isolation Faults — Environmental Root Cause Report"
subtitle: "A transient high-voltage insulation warning, clustered in coastal climates and at dawn, traced past a convincing connector-lot Pareto to its true origin: overnight condensation bridging the HV creepage path."
date: 2026-06-11 20:00:00 -0400
category: "Control Systems"
slug: environmental-rca-report
excerpt: "Case 4 of 5. An intermittent HV isolation warning, clustered geographically (coastal climates) and temporally (dawn hours). The Pareto points at a connector lot; the truth is an environmental cause — overnight condensation bridging the HV creepage path. The fix is a combination of environmental hardening and a firmware filter that suppresses dawn-hour transients. With synthetic data from 500 telematics events."
reading_time: 16
---

This is Case 4 of the five-part RCA series. After software, electromagnetic-structural, and manufacturing failure families, this one is the *environmental* family — where the cause lives in the operating environment rather than in any component or process.

The complaint: an intermittent high-voltage isolation warning from the IMD (insulation monitoring device). The warning is transient (clears itself within minutes) and clusters in two non-obvious ways: geographically (overrepresented in coastal climates) and temporally (overrepresented at dawn). The Pareto, again, points at a connector lot — and again, is wrong. The two clustering dimensions are the smoking gun: anything that clusters by both coast and dawn is almost certainly an *environmental* cause, specifically humidity-driven. The lesion is overnight condensation on the HV connector creepage path, briefly bridging insulation enough to trip the IMD, then evaporating with the morning sun.

This is also the case study where the *cluster discipline* — looking at the joint distribution of the symptom across geographic, temporal, and demographic dimensions — pays off most clearly. Pure component-lot Paretos cannot find an environmental cause; the cluster geometry can.

## What it covers

Ten sections, about sixteen minutes of careful reading.

**§ 1–2 — The intermittent warning.** What the IMD sees. The transient nature (warning clears in 3–10 minutes). The false-alarm dismissal that almost stopped the investigation.

**§ 3–4 — The two clusters.** Geographic (coastal). Temporal (dawn hours). The discipline of looking at joint distributions, not marginal ones.

**§ 5–6 — The connector-lot impostor.** The Pareto that fits the data but doesn't survive cross-validation against the cluster geometry.

**§ 7–8 — Condensation as the mechanism.** The dew-point calculation. The humidity-temperature trajectories across affected sites. The creepage-path bridging math.

**§ 9–10 — Mitigation.** Connector-seal redesign for new vehicles. A firmware filter (suppress IMD warnings during 30 min after dawn for 6 weeks per season) for the existing fleet. The validation: both approaches close the alarm rate to baseline.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/environmental-rca-report.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open Case 4 →
  </a>
</div>

The report lives at its own URL with a warm-paper engineering-document layout — sea-blue accent for the coastal-climate motif, classical RCA-report styling.

## Code & data

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/environmental-rca-code-and-data.zip' | relative_url }}" download>environmental-rca-code-and-data.zip</a> — the Python generator (<code>isolation_fault_rca.py</code>), the synthetic 500-event dataset (<code>isolation_events.csv</code>), and a README.</p>
</div>

## The full series

Case 4 of 5. Read the rest in order:

1. [Battery Degradation Case Study]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }}) — software / firmware
2. [Preconditioning-Mode NVH]({{ '/posts/nvh-preconditioning-rca-report/' | relative_url }}) — electromagnetic / structural
3. [Module Weld Resistance]({{ '/posts/manufacturing-rca-report/' | relative_url }}) — tooling / manufacturing
4. **HV Isolation Faults** — *(this post)* — environmental (condensation)
5. [Brake Rotor Corrosion]({{ '/posts/usage-rca-report/' | relative_url }}) — usage / behavior

Followed by the [agentic framework]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}) and its [worked walkthrough]({{ '/posts/framework-battery-walkthrough/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
