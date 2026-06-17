---
title: "The Framework in Action — A Battery Fade Walkthrough"
subtitle: "Watching the human-gated agent team diagnose and forecast the battery-degradation case — and, crucially, fusing the structured fleet data with the messy pile beside it: service notes, bulletins, DTC catalogs, manuals, and a knowledge graph."
date: 2026-06-12 11:00:00 -0400
category: "Tools"
slug: framework-battery-walkthrough
excerpt: "A real-time walkthrough of the agentic RCA framework running on the battery case from Case 1. Every step is shown: what the perceiver sees, what the grounder retrieves, what the hypothesizer proposes, what the simulator returns, what the gatekeeper asks the human. The verdict (a firmware-balancing bug) is the same as Case 1's hand-done version — but the framework finds it from telemetry plus a heterogeneous documentation pile in minutes rather than hours, and surfaces both the conclusion and the evidence trail with the human in the loop at every irreversible step."
reading_time: 20
---

This is the natural follow-up to the [Agentic RCA Framework architecture monograph]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}). That post drew the architecture; this one *runs it*. The case it runs on is the battery-degradation case from [Case 1]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }}) of the five-case series — which means the ground truth is known (a firmware balancing bug in cell-pack revision v3.2.1), the synthetic data is fully reproducible, and the framework's conclusion can be graded against the case study's hand-done verdict.

What makes the walkthrough worth its own post is the *data heterogeneity* problem. The hand-done case study used only the structured telemetry (the 240-vehicle fleet CSV). Real RCA work doesn't have that luxury — the analyst has telemetry *plus* service notes, bulletins, DTC catalogs, manuals, and (if they're lucky) a knowledge graph that ties the entities together. The framework has to read across all of this, find the relevant evidence in each, and present a unified picture. The walkthrough shows exactly how that happens, agent by agent, retrieval by retrieval.

The verdict the framework reaches is the same as Case 1's — *firmware v3.2.1 cell-balancing bug, root cause confirmed, RUL forecast of 20 months if unfixed, dropping to baseline if patched* — but the *path* is different and instructive. The framework's hypothesizer surfaces the firmware hypothesis from the knowledge graph (which knows about v3.2.1's release notes mentioning balancing tweaks) before the telemetry alone would have pointed there. That's the data-fusion payoff in action.

## What it covers

Ten sections, about twenty minutes of careful reading.

**§ 1 — The setup.** The case (battery degradation in a subpopulation), the framework instance (the six-agent team), the heterogeneous data sources (telemetry CSV + service notes + bulletins + DTC catalog + knowledge graph).

**§ 2 — Perceive.** The perceiver agent ingests the telemetry. The dashboard view it builds. The signal-to-investigator handoff.

**§ 3 — Ground.** The grounder agent retrieves the relevant documents. Service notes for affected VINs. The bulletin on firmware v3.2.1. The DTC patterns. The knowledge-graph neighborhood around "battery-balancing."

**§ 4 — Hypothesize.** The hypothesizer agent generates candidate root causes. The firmware-balancing hypothesis. The cell-aging hypothesis. The thermal-management hypothesis. The convincing-impostor hypothesis (a cell vendor lot — included to demonstrate that the framework also encounters the impostors and has to refuse them).

**§ 5 — Simulate.** The simulator agent runs each hypothesis through the physics oracle (see the [Physics Sandbox]({{ '/posts/physics-sandbox-agentic-ai/' | relative_url }}) post for the underlying pattern). The hypotheses that don't match the observed telemetry are pruned.

**§ 6 — Triage.** The remaining hypotheses (the firmware bug and the cell-aging interaction) get ranked by likelihood. The framework presents both, with its confidence in each, to the gatekeeper.

**§ 7 — The first human gate.** The senior analyst sees the framework's output — two hypotheses, the evidence trail behind each, the confidence numbers. The analyst commits to the firmware-bug hypothesis. The commit is logged.

**§ 8 — Forecast.** The framework runs the prognostic models. RUL distributions under three scenarios: no fix, OTA fix in 3 months, OTA fix today.

**§ 9 — The second human gate.** The disposition decision. The analyst chooses "OTA fix today + targeted fleet outreach." The framework drafts the change request, the customer-communication template, and the fleet-action queue. The analyst reviews and authorizes.

**§ 10 — The audit trail and the next investigation.** What gets logged. How this investigation becomes training data for the framework's next investigation. The labeling-becomes-dataset loop in action.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/framework-battery-walkthrough.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the walkthrough →
  </a>
</div>

The walkthrough lives at its own URL with a warm-paper editorial layout — teal accent for the framework, plum highlight for the knowledge-graph fusion content. Each stage shows the actual agent output, retrieval results, and decision points.

## Companions

- The architecture monograph: [A Human-Gated Agentic Framework for RCA & Prognostics]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}) — the architectural reading this walkthrough demonstrates.
- The hand-done version of the same case: [Battery Degradation Case Study]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }}) — the manual analysis the framework reproduces.
- The five-case series that grounds the framework: [Battery]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }}) · [NVH]({{ '/posts/nvh-preconditioning-rca-report/' | relative_url }}) · [Manufacturing]({{ '/posts/manufacturing-rca-report/' | relative_url }}) · [Environmental]({{ '/posts/environmental-rca-report/' | relative_url }}) · [Usage]({{ '/posts/usage-rca-report/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
