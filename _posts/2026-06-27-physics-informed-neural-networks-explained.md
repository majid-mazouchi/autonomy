---
title: "Physics-Informed Neural Networks: A Complete Introduction"
subtitle: "A neural network that learns from your data and from the equations of physics at the same time — the intuition, the interactive sims, and where it earns its keep."
date: 2026-06-27 10:00:00 -0400
category: "Neural Networks"
slug: physics-informed-neural-networks
excerpt: "A single, complete introduction to physics-informed neural networks, in two parts. Part 1 (in plain words) builds the idea from the ground up — the mass-on-a-spring intuition, how physics becomes part of the loss, a live PINN training in your browser, probing the residual, discovering a hidden parameter, and the residual as a fault detector. Part 2 (a working introduction) turns to the harder edges — forward and inverse problems, the failure modes (unbalanced loss terms, spectral bias, stiff and multi-scale systems, leaky soft constraints), and why PINNs fit prognostics and vehicle health monitoring so well. Every figure and interactive simulation from both pieces is preserved."
reading_time: 34
---

A single, complete introduction to physics-informed neural networks (PINNs) — the two earlier write-ups merged into one, losing none of the figures or interactive simulations. It runs in two parts: **Part 1, in plain words**, builds the intuition and lets you train a PINN live in the browser; **Part 2, a working introduction**, covers the forward and inverse problems, the failure modes, and the vehicle-health fit.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/physics-informed-neural-networks.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

Both parts live at one URL, with a jump-nav between them. Part 1 is the plain-words explainer with the in-browser training demo; Part 2 is the working introduction with the failure-mode sandboxes and the PHM/VHM discussion.

---

← Back to [Autonomy]({{ '/' | relative_url }})
