---
title: "Copilot Plotting Kit — Plate Gallery"
subtitle: "A working gallery for the copilot-plotting-kit — fourteen figure skills, one style root. Every plate rendered by the kit's own scripts on synthetic data, reproducible from a module.py::function recipe."
date: 2026-06-08 23:30:00 -0400
category: "Tools"
slug: plotting-kit-gallery
excerpt: "Most data-visualization advice in 2026 has the same flaw: it tells you what a good figure looks like and stops short of telling the agent how to produce one. A Copilot skill kit can close that gap — fourteen figure skills covering matplotlib conventions, time-series telemetry, distributions, maps and 2D fields, ML insights, flows, SVG diagrams, tables, plotly interactivity, and the exec-figure polish discipline that ties them together. This is the plate gallery: every figure rendered by the kit on synthetic data, with the module.py::function recipe behind each plate."
reading_time: 12
---

This is the third post in what is becoming an unintentional series — Copilot skill kits with a working plate gallery as the documentation. The first was the [Visual Skills Showcase]({{ '/posts/visual-skills-showcase/' | relative_url }}) — twenty-six general-purpose visual skills with one live sample each. The second was the [Research Source Stack]({{ '/posts/research-source-stack/' | relative_url }}) and its harness kit. This one is narrower and deeper: fourteen *figure* skills covering the specific domain of data-visualization production — the matplotlib idioms, the time-series and telemetry conventions, the distributions-and-SPC patterns, the maps, the ML-insight figures, the flow diagrams, the table styling, the plotly interactive layer, and the exec-figure polish discipline that pulls all of it together into figures you can put in front of a VP without flinching.

The kit philosophy is the same as the previous two: each skill is a SKILL.md file (some with reference notes and reusable scripts) that lives in `.github/skills/` and teaches the agent how to produce that specific figure type *well*. The gallery is the test — every plate in this page was rendered by the kit's own scripts on synthetic data (`numpy.random.default_rng(42)`), so every figure is reproducible from its `module.py::function` recipe, and the style root is consistent across all fourteen skills (warm cream canvas, deep ink, saturated accents, units in every axis label, semantic colors that never change meaning).

The companion posts: [Skills in AI Agents]({{ '/posts/skills-in-ai-agents/' | relative_url }}) for the skill pattern in general, [VS Code Copilot, Explained]({{ '/posts/vscode-copilot-explained/' | relative_url }}) for the wiring-it-into-your-workflow story, and the [Visual Skills Showcase]({{ '/posts/visual-skills-showcase/' | relative_url }}) for the more general visual-communication kit.

## The fourteen skills

Grouped by what they produce:

**Conventions & style.** `plot-style-guide` (the style root every other skill inherits from), `matplotlib-conventions` (the object-oriented API discipline, preset sizes, direct labeling, semantic reference bands).

**Diagnostic & monitoring figures.** `diagnostics-plots` (residual plots, fault-injection traces, calibration tables), `prognostics-plots` (RUL distributions, degradation curves, confidence bands), `timeseries-telemetry` (multi-signal telemetry, downsampling, MDF/CAN-style trace plots).

**Statistical figures.** `distributions-stats` (histograms, KDEs, SPC charts, the Q-Q plots that nobody automates well).

**Spatial figures.** `maps-fields-2d` (heatmaps, contour fields, scalar fields on grids), `geo-fleet` (state-level choropleths with normalization-by-vehicles-in-operation, minimum-n greying — the example in the footer of the gallery).

**ML insight figures.** `ml-insights` (learning curves, confusion matrices, SHAP-style feature attribution, partial-dependence plots).

**Structural figures.** `flows-relations` (Sankey, alluvial, directed-graph layouts), `svg-figures` (the static-block-diagram pattern from the visual-skills kit, specialized for engineering work).

**Tabular & dashboard.** `tables-formatting` (the boring-but-essential discipline of clean tables and KPI cards), `exec-figure-polish` (the integration layer that takes a good figure and makes it executive-ready).

**Plus** `plotly-interactive` (the interactive layer — hovers, brushing, embedded JSON for blog posts).

## The gallery

The 4.6 MB gallery page is the deliverable. Every section is a plate; click any plate to see the title, the figcaption, and the underlying recipe. The plotly section is interactive.

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/plotting-kit-gallery.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the gallery →
  </a>
</div>

## Download the kit

The skill bundle is one zip — drop the skill folders into your project's `.github/skills/` directory and Copilot will pick them up. The kit also includes two ready-made agent profiles in `agents/` (`figure-critic` and `data-explorer`) you can register as Copilot custom agents.

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/copilot-plotting-kit.zip' | relative_url }}" download>copilot-plotting-kit.zip</a> — fourteen figure-skill folders + two agent profiles, 104 files, ready to drop into <code>.github/skills/</code>.</p>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
