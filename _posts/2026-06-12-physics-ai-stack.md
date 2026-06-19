---
title: "The Physics-AI Stack — Surrogates"
subtitle: "A plain-words, comprehensive guide to the physics-AI tools: what they are, how they learn, how to put them inside an agent that catches faults and predicts failures, what each one costs, the hardware you need, and a glossary for every term."
date: 2026-06-12 15:00:00 -0400
category: "Tools"
slug: physics-ai-stack
excerpt: "Some AI doesn't chat. It learns to imitate a physics simulator so closely that it answers in milliseconds what used to take a supercomputer hours. NVIDIA has built a full ladder of these tools — a fast engine at the bottom, ready-made models at the top, and the training-and-deployment machinery in between. This monograph is the plain-words tour: two ways AI can do physics, the stack rung by rung, how a surrogate is trained, the fast-versus-trustworthy trade-off, the four named products, a worked health-monitoring agent application, what's free vs paid, the hardware ladder, and a glossary for every term."
reading_time: 35
---

Most of the AI conversation in 2026 is about chat. This post is about the part of AI that doesn't chat — the part that learns to imitate a physics simulator so closely that it answers in milliseconds what used to take a supercomputer hours. The field has a name (*neural surrogates* or *AI for science*), a small set of foundational ideas, and — increasingly — a vendor stack to ship into production. NVIDIA's stack is the most-built-out version of that production tooling, and it is the practical entry point for engineers who want to actually deploy these methods rather than read about them in JMLR.

This is the natural follow-on to the [Physics Sandbox for Agentic AI]({{ '/posts/physics-sandbox-agentic-ai/' | relative_url }}) post — that one covered how to *connect* a physics simulator to an LLM agent (the simulator on the bottom, MCP in the middle, agent at the top). This one covers what happens when the simulator at the bottom is *replaced* by a learned surrogate that runs a thousand times faster. The architectural picture stays the same; the substrate underneath gets dramatically cheaper. That speedup is the difference between "the agent can hypothesis-test once per minute" and "the agent can hypothesis-test once per millisecond" — which is, in turn, the difference between a research curiosity and a production deployment.

The monograph is plain-language throughout. It assumes you know what a neural network is and roughly what a physics simulation is; it does not assume you know what a Fourier neural operator is or what NVIDIA Modulus does (we get there). The end-to-end worked example is a fault-catching, failure-forecasting health-monitoring agent — the kind of system the [agentic RCA framework]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}) was built for. The two posts read well together.

## What it covers

Ten sections plus a glossary, about thirty-five minutes of careful reading.

**§ 1 — Two ways AI can do physics.** The taxonomy. *Surrogate* models replace the simulator with a neural network. *Physics-informed* models keep the simulator and use AI to make it better (parameter inference, missing-physics discovery). The first is what the rest of the post is about; the second gets the comparison.

**§ 2 — The stack, rung by rung.** NVIDIA's stack drawn out. *Warp* (the differentiable physics engine at the bottom). *Modulus* (the training framework for neural surrogates). *PhysicsNeMo* (the model-development layer). *Earth-2* and other ready-made models (the top of the stack). What each rung does, what it's good at, when to drop down or climb up.

**§ 3 — How a surrogate is trained.** The actual recipe. Data generation from a physics simulator. The neural-operator architectures (FNO, DeepONet, GNN-based) that have won out empirically. The training loop. The cost (it's not cheap — surrogates pay their training cost back over many inference calls).

**§ 4 — Fast versus trustworthy.** The trade-off that determines whether the surrogate ships. Fast surrogate, wrong answers — useless. Trustworthy surrogate, slow training — fine, but pay-off depends on how often you call it. The calibration discipline. The acceptance criteria that real engineering teams use.

**§ 5 — The four named products.** *Modulus* — the open-source framework. *PhysicsNeMo* — the higher-level abstraction. *Warp* — the differentiable physics engine. *Earth-2* — the planetary-scale climate model. The four documents you'd read first, the four GitHub repos you'd star, the four pricing pages you'd check.

**§ 6 — A health-monitoring agent.** A worked example. A traction-motor health-monitoring agent built on this stack. The surrogate that replaces the per-vehicle electromagnetic simulation. The LLM agent that reasons against the surrogate at millisecond latency. The fault-detection and RUL-forecasting outputs. Cross-reference to the [agentic RCA framework]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}) — this is the substrate that framework runs on when the bottom-of-stack physics needs to be faster than a literal FMU.

**§ 7 — What is free, what it costs.** The pricing reality. Open-source (Modulus, Warp) — free to use, you pay in hardware and engineering time. Enterprise (NVIDIA AI Enterprise, support contracts, premium models) — annual licensing. The honest cost-comparison matrix.

**§ 8 — The hardware ladder.** What you actually need to run this stack. The H100/H200 tier (frontier surrogate training). The A100/L40 tier (production inference + smaller training). The consumer-grade tier (prototyping, education). The cloud-vs-on-prem trade-off.

**§ 9 — Glossary of terms.** Every term used in the monograph, defined in plain language. Surrogate. Neural operator. FNO. DeepONet. PINN. Physics-informed. Differentiable physics. Operator learning. The vocabulary that lets you read the recent arXiv papers without bouncing off them.

**§ 10 — References & notes.** The papers worth reading first (the original FNO paper, the DeepONet paper, the recent foundation-model-for-PDEs work). The NVIDIA documentation links. The independent voices worth following.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/physics-ai-stack.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-cream editorial layout — green-deep for the surrogate-model material, blue for the agent-application material, rust for the trade-off-cost discussion. Ten sections plus a glossary, designed for one-rung-at-a-time reference use afterward.

## Companions

- [Physics Sandbox for Agentic AI]({{ '/posts/physics-sandbox-agentic-ai/' | relative_url }}) — the architectural foundation this post extends.
- [Agentic RCA & Prognostics Framework]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}) — the agent architecture that runs on the substrate this post describes.
- [PyTorch & TensorFlow]({{ '/posts/pytorch-tensorflow/' | relative_url }}) — the underlying ML frameworks the NVIDIA stack sits on top of.
- [Neural Networks — Interactive Concepts]({{ '/posts/neural-networks-interactive-concepts/' | relative_url }}) — the basics this post assumes.

---

← Back to [Autonomy]({{ '/' | relative_url }})
