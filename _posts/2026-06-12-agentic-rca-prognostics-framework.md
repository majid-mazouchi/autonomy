---
title: "A Human-Gated Agentic Framework for Root-Cause & Prognostic Analysis"
subtitle: "How to replace the human analyst at the keyboard — but not the human judgment — with a closed-loop team of AI agents that finds the root cause, forecasts what happens next, and asks a person before it does anything that matters."
date: 2026-06-12 09:00:00 -0400
category: "Tools"
slug: agentic-rca-prognostics-framework
excerpt: "The architecture that ties the five-case RCA series together. A human-gated agentic framework that runs the diagnostics-and-prognostics method as a closed loop — perceive, ground, hypothesize, simulate, decide, ask — with deterministic tools where they belong, LLM agents where they earn their keep, and a human in the loop at every irreversible step. The full architecture, drawn out, with interactive block diagrams."
reading_time: 26
---

This is the post the five-case series was building toward. The cases established the *method* — abduction disciplined by partial correlation and physics, the refusal of convincing impostors, the cluster-geometry discipline, the difference between a fault-correction and a system-design accommodation. This post is the *architecture* that automates the method while keeping the human in the loop at every step that matters.

The framework is built around a tight idea: agents are bad at being the analyst, but very good at being the *junior analyst with infinite patience*. They are excellent at fetching telemetry, running scripts, generating hypotheses, simulating them, and presenting the evidence in a form the senior analyst can adjudicate. They are terrible at being the senior analyst — at *committing to a root cause* and authorizing the fix. The framework's design discipline is to keep all of the first-kind work inside the agent layer and all of the second-kind work behind a human gate. The result is a closed-loop system that does the analyst's *day* in minutes while leaving the analyst's *decisions* exactly where they belong.

This monograph is the architectural reading of the framework. It is the natural companion to the [HITL in Agentic AI]({{ '/posts/hitl-foundations/' | relative_url }}) series (this is the worked-out example of those principles in a specific domain), the [Physics Sandbox]({{ '/posts/physics-sandbox-agentic-ai/' | relative_url }}) post (the physics-oracle pattern is the simulator at the bottom of the framework), and the [Why Agentic AI Fails]({{ '/posts/why-agentic-ai-fails/' | relative_url }}) field guide (the gate placement is exactly the architecture that prevents the three classic failure modes).

## What it covers

Twelve sections, about twenty-six minutes of careful reading.

**§ 1–2 — The problem and the principle.** Why current RCA workflows are a bottleneck. Why a single super-agent fails at this task. The principle that organizes the rest of the architecture: *agents fetch and propose, humans commit*.

**§ 3–4 — The agent team.** Six specialized agents — perceiver, grounder, hypothesizer, simulator, summarizer, gatekeeper — and what each one does. The interfaces between them. The hand-off discipline.

**§ 5–6 — The tool surface.** What the agents have access to. Telemetry queries (read-only). Simulator runs (read-only). Document retrieval (read-only). The actuator layer (write, but gated). The deterministic tools that the LLM agents wrap.

**§ 7 — Memory architecture.** Short-term context (the current investigation). Long-term institutional memory (the knowledge graph of past investigations). The retrieval discipline.

**§ 8 — The gate placement.** Where the human is in the loop. The before-you-commit gate. The before-you-fix gate. The before-you-deploy gate. The audit-after-the-fact mechanism for actions that happen between gates.

**§ 9 — The closed loop.** How the framework's output feeds the next investigation. The labeling-becomes-dataset discipline. The case library that grows with use.

**§ 10 — Failure modes and mitigations.** What can go wrong. Agent hallucinations on telemetry (mitigation: physics-refereed verification). Confidence amplification across agents (mitigation: the gatekeeper's adversarial role). Specification gaming of the gate (mitigation: the interface design that surfaces optimization pressure).

**§ 11 — Where this fits in the literature.** The intellectual neighbors. Cross-references to HITL theory, agentic-AI engineering, and the broader RCA / prognostics literature.

**§ 12 — A worked walkthrough.** The pointer to the [framework battery walkthrough]({{ '/posts/framework-battery-walkthrough/' | relative_url }}), which runs this entire framework on the battery case and shows the actual outputs at each stage.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/agentic-rca-prognostics-framework.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the architecture monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-paper architecture-document layout — navy accent for the agentic-architecture motif, color-coded blocks for the six agents, interactive block diagrams throughout.

## The five case studies that ground the framework

This architecture would be unmoored without concrete examples. The five cases are the proof — each one in a different root-cause family, each one demonstrating the method this framework automates:

1. [Battery Degradation]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }}) — software / firmware
2. [Preconditioning-Mode NVH]({{ '/posts/nvh-preconditioning-rca-report/' | relative_url }}) — electromagnetic / structural
3. [Module Weld Resistance]({{ '/posts/manufacturing-rca-report/' | relative_url }}) — tooling / manufacturing
4. [HV Isolation Faults]({{ '/posts/environmental-rca-report/' | relative_url }}) — environmental
5. [Brake Rotor Corrosion]({{ '/posts/usage-rca-report/' | relative_url }}) — usage / behavior

And the [worked walkthrough]({{ '/posts/framework-battery-walkthrough/' | relative_url }}) of the framework running on Case 1.

## All-cases source bundle

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/source.zip' | relative_url }}" download>source.zip</a> — all five RCA Python generators + all five datasets in a single archive. The combined source for the entire series.</p>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
