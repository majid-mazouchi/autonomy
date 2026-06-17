---
title: "Module Weld Resistance — Manufacturing Root Cause Report"
subtitle: "A battery-module interconnect defect traced past a convincing supplier-lot Pareto to its real origin on the production floor: weld-electrode tip wear under a lax dressing interval — and the SPC fix that closes it."
date: 2026-06-11 18:00:00 -0400
category: "Control Systems"
slug: manufacturing-rca-report
excerpt: "Case 3 of 5. Elevated tab-to-busbar weld resistance is creating thermal hotspots in finished battery modules. The Pareto chart points straight at one supplier lot — and is wrong. The true cause is a manufacturing-process drift: weld-electrode tip wear under a dressing interval that's too long. The fix is a Statistical Process Control patch that closes the drift. With synthetic data from a 600-module instrumented study."
reading_time: 18
---

This is Case 3 of the five-part RCA series. After [a software bug]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }}) and [an electromagnetic-structural interaction]({{ '/posts/nvh-preconditioning-rca-report/' | relative_url }}), this one is the *manufacturing* failure family — where the cause is on the production floor and the fix is a process-control change.

The complaint: elevated tab-to-busbar weld resistance in finished battery modules, creating thermal hotspots that fail acceptance testing. The Pareto chart, on first glance, points straight at one supplier lot of weld electrodes — a convincing story, well within the precision of the data. It is also wrong. The investigation has to refuse the easy answer and look at the actual *process* — the welding stations, the electrodes on those stations, and the maintenance interval at which the electrodes are dressed. The lesion is electrode-tip wear under a dressing interval that drifted longer than the SPC charts could catch with their current setpoint. The fix is a tightened dressing interval plus a tip-condition sensor — the kind of fix that costs almost nothing to deploy and dramatically improves yield.

This case demonstrates the manufacturing-RCA discipline that is its own subculture inside the broader RCA field. The vocabulary is different (Cp/Cpk, SPC, dressing intervals, tooling wear), but the method is the same: refuse the convincing impostor, walk the data back to the actual mechanism, validate the fix.

## What it covers

Eleven sections, about eighteen minutes of careful reading.

**§ 1–2 — The yield problem.** The acceptance-test failures. The financial pressure. The first instinct that the lot is bad.

**§ 3–4 — The Pareto and why it's wrong.** The supplier-lot chart that looks definitive. The cross-validation that breaks it. The discipline of distinguishing *correlation in the Pareto* from *causation in the process*.

**§ 5–7 — Walking the process.** The actual weld stations. The electrodes. The dressing intervals. The tip-wear curves. The data that surfaces when you stop staring at the supplier dimension and start staring at the manufacturing dimension.

**§ 8–9 — The lesion: dressing-interval drift.** The maintenance schedule that crept longer over six months. Why the SPC charts missed it. The control-chart redesign.

**§ 10–11 — The validated SPC fix.** Tightened dressing interval. Tip-condition sensor. The yield-curve recovery. The before-and-after Cpk numbers.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/manufacturing-rca-report.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open Case 3 →
  </a>
</div>

The report lives at its own URL with a warm-paper manufacturing-document layout — steel-blue accent, classical SPC-chart styling throughout.

## Code & data

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/manufacturing-rca-code-and-data.zip' | relative_url }}" download>manufacturing-rca-code-and-data.zip</a> — the Python generator (<code>weld_resistance_rca.py</code>), the synthetic 600-module dataset (<code>weld_modules.csv</code>), and a README.</p>
</div>

## The full series

Case 3 of 5. Read the rest in order:

1. [Battery Degradation Case Study]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }}) — software / firmware
2. [Preconditioning-Mode NVH]({{ '/posts/nvh-preconditioning-rca-report/' | relative_url }}) — electromagnetic / structural
3. **Module Weld Resistance** — *(this post)* — tooling / manufacturing
4. [HV Isolation Faults]({{ '/posts/environmental-rca-report/' | relative_url }}) — environmental (condensation)
5. [Brake Rotor Corrosion]({{ '/posts/usage-rca-report/' | relative_url }}) — usage / behavior

Followed by the [agentic framework]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}) and its [worked walkthrough]({{ '/posts/framework-battery-walkthrough/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
