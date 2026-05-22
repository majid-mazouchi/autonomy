---
title: "From Consensus to Containment — a Visual Monograph"
subtitle: "How a network of agents learns to agree, to follow, and finally to settle inside a territory shaped by many leaders at once. A worked illustration of Mazouchi, Tatari, Kiumarsi & Modares (2021)."
date: 2026-05-19 10:00:00 -0400
category: "Control Systems"
slug: containment-control-explained
excerpt: "A seven-act visual walkthrough of multi-agent control — from the simplest consensus problem (six agents averaging with their neighbors) to fully-heterogeneous containment, where many leaders define a moving convex hull and a graph of followers settles inside it despite each one having different dynamics, different inputs, and only local information. Every figure is interactive; every result connects back to the underlying paper."
reading_time: 28
---

This is a long one, and a personal one — it is an illustrated, interactive walk-through of a paper I co-authored with Farnaz Tatari, Bahare Kiumarsi, and Hamidreza Modares in 2021, on *Fully-Heterogeneous Containment Control of a Network of Leader-Follower Systems* ([arXiv:2004.03725](https://arxiv.org/abs/2004.03725)). The paper itself does what most engineering papers do: it states a theorem, proves it, and runs a simulation to confirm the proof. Helpful if you already know the field. Less so as a first introduction.

What I wanted to write — and what I never quite had time to write properly until now — is the version that builds up the same problem from the simplest cooperative-control setting all the way to fully-heterogeneous containment, with figures you can actually *play* with at every step. Six agents averaging on a graph. Then six agents tracking a leader. Then six agents settling inside a moving polygon defined by three leaders. Then the same problem when every agent has its own dynamics, its own input matrix, its own dimension. The math comes along for the ride, but the figures lead.

If you are working in cooperative control or multi-agent reinforcement learning, this is the on-ramp. If you have read the paper already, this is the picture-book version that makes the proof-mechanics tangible.

## What it covers

Seven acts. About twenty-eight minutes of reading; longer if you stop to drag agents around the canvas, which is encouraged.

**Act I — Consensus.** The simplest cooperative-control problem. Six agents on a connected graph, each integrating $\dot{x}_i = \sum_j a_{ij}(x_j - x_i)$. They converge exponentially to a weighted average — and the only thing that matters for the final value is the graph and the initial conditions. The graph Laplacian as the operator running the show; the three matrices ($D$, $A$, $L$) that together encode the topology.

**Act II — Leader-follower tracking.** Add a single leader whose trajectory is exogenous. Followers stop converging to a static average and start tracking the leader, with tracking error governed by the algebraic connectivity of the leader-pinning Laplacian. The shift from "agree on a number" to "follow a moving target."

**Act III — Multiple leaders.** Multiple leaders, each with their own moving trajectory. The followers no longer converge to a single point — they converge to the *convex hull* of the leaders. This is the geometry of containment, and the figure shows it explicitly: a polygon defined by leaders that moves and deforms, with followers settling inside it.

**Act IV — Heterogeneity.** The full version of the problem. Each follower has its own state dimension, its own dynamics matrix, its own input matrix. The leaders may have a different dimension still. There is no longer a single "state space" everyone lives in. The fix is the three-layer decomposition that the 2021 paper introduces — one layer per concern, designed independently and composed at the end.

**Act V — The output-regulation layer.** The bottom layer of the decomposition. Each follower's local controller solves a regulator equation that says "given the local copy of the leader trajectory I have just been handed, what input do I apply to my plant to track it." Standard output-regulation machinery, applied locally.

**Act VI — The distributed observer.** The middle layer. Each follower must reconstruct the leaders' states from local information only — its own state, its neighbors' state estimates, occasionally a leader if it's directly connected. The observer is itself a consensus-like system, running on top of the underlying graph. This is the layer that makes "fully heterogeneous" possible.

**Act VII — The reachability / NLI layer.** The top layer, and the most subtle. Each leader needs to be *reachable* from every follower via some directed path through the graph; the *normalized leader-influences* (NLIs) determine how much weight each follower assigns to each leader, and consequently where inside the convex hull it ends up. The interactive figure here lets you switch between four followers ($F_1, F_2, F_3, F_4$) and see the live NLIs change as the graph topology changes — the failure mode (Assumption 1 violated, leader unreachable) is shown explicitly.

The full reading sits on top of the original paper without replacing it — the figures are mine but the math points back to the source, with a footer citation for anyone who wants the formal version.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/containment-control-explained.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-paper, seven-act layout — Fraunces display, Crimson Pro body, JetBrains Mono for the math. Every figure is rendered live; the graph topology is interactive; the proofs are pointed to but not reproduced.

---

← Back to [Autonomy]({{ '/' | relative_url }})
