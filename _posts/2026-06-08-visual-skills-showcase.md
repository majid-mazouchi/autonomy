---
title: "Visual Skills Showcase — 26 Skills, 26 Live Samples"
subtitle: "A working demo reel for the copilot-visual-skills kit — every section is a sample of one skill, built exactly the way the corresponding SKILL.md tells the agent to build it. View source on any sample to see the pattern."
date: 2026-06-08 22:00:00 -0400
category: "Tools"
slug: visual-skills-showcase
excerpt: "A demo reel for a Copilot kit of 26 visual-communication skills — paper-monograph shells, interactive parameter labs, algorithm step players, flowcharts, state-machine animations, exec dashboards, three.js scenes, and a dozen more. Each section of the showcase is a working sample built directly from the corresponding SKILL.md, so you can view source to see exactly what the agent did. With the full kit downloadable as a single zip."
reading_time: 14
---

This is a different kind of post — less a written field guide than a *demo reel*. The premise is simple: when you build a Copilot skill kit for visual communication, the most honest documentation isn't a written description of what each skill does. It's a working sample, built by the same agent reading the same SKILL.md you'd be reading. Twenty-six samples, twenty-six skills, all in one scrollable page, every one of them view-source-able to see the actual pattern the agent produced.

The kit itself — `copilot-visual-skills.zip` — is the input side of this story. Each subfolder is one skill (a single SKILL.md, sometimes a reference file). Drop the kit into `.github/skills/` in any Copilot-using project, and the next time you ask the agent to "build me an interactive parameter lab," it will produce something that looks like §02 in this showcase. Ask for "an algorithm step player," it produces §03. And so on. The showcase is the test that the kit works — and the most efficient documentation of what the kit can do.

This is the companion piece to the [Skills in AI Agents]({{ '/posts/skills-in-ai-agents/' | relative_url }}) monograph (which explains the skill pattern in general), the [VS Code Copilot, Explained]({{ '/posts/vscode-copilot-explained/' | relative_url }}) field guide (which is where you'd actually wire these skills into your workflow), and the [Research Source Stack]({{ '/posts/research-source-stack/' | relative_url }}) guide (which uses a similar pattern for a different agent specialty).

## What's in the kit

Twenty-six skills, grouped by what they produce. Each section of the showcase is a working sample of the corresponding skill.

**Paper & document shells.** `paper-monograph-shell` (the warm-paper editorial layout that most posts on this site use), `paper-essay-shell`, `print-style-pdf-shell`, `html-slide-mode`.

**Interactive labs & explainers.** `interactive-parameter-labs` (sliders that drive live math), `algorithm-step-player` (step-through animations of algorithms), `interactive-flowcharts`, `state-machine-and-sequence-animations`, `interactive-tree-diagrams`, `physics-and-motion-demos`.

**Diagram & chart skills.** `svg-interactivity-layer` (turn any static SVG into a probe-able element), `exec-dashboard-figures`, `trade-study-matrices`, `data-table-figures`, `chart-grids`, `block-diagrams`, `system-architecture-diagrams`.

**3D & graphics.** `interactive-3d-surface-plots`, `3d-camera-choreography`, `three-js-scenes`, plus a vendoring guide for fully-offline 3D pages.

**Code & math presentation.** `live-code-snippets`, `math-typography`, `tex-style-equations`, `inline-glossary-callouts`, `figure-captions-and-references`.

**Plus** a couple of utility skills that show up across categories — `print-friendly-toc`, `accessibility-baseline`.

## The showcase

The 26-section live page is the deliverable. Every section runs locally with no dependencies for §§01–19 and §26; sections 20–25 (the 3D ones) optionally pull three.js r160 from CDN, and the skills include the vendoring guidance for fully-offline pages.

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/visual-skills-showcase.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the showcase →
  </a>
</div>

## Download the kit

The skill bundle is one zip — drop the unzipped folders into your project's `.github/skills/` directory and Copilot will pick them up.

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/copilot-visual-skills.zip' | relative_url }}" download>copilot-visual-skills.zip</a> — all 26 skill folders (one SKILL.md per folder), ready to drop into <code>.github/skills/</code>.</p>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
