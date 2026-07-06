---
title: "Graph Neural Networks: A Complete Introduction"
subtitle: "How a neural network learns from data whose most important feature is who is connected to whom — the anatomy, the architectures, and where graph learning fits."
date: 2026-07-03 14:00:00 -0400
category: "Neural Networks"
slug: graph-neural-networks
excerpt: "A single, complete introduction to graph neural networks, in two parts. Part 1 (explained simply) walks the anatomy from the ground up — the input encoder, the stack of message-passing layers, the readout, and the training loop — with an interactive message-passing demo. Part 2 (a working introduction) covers the main architectures (GCN, GraphSAGE, GAT, GIN), the tasks (node, edge, and graph level), the failure modes (over-smoothing, over-squashing, limited expressiveness, scale, heterophily), and the applications to knowledge graphs and vehicle health. Every figure and simulation from both pieces is preserved."
reading_time: 24
---

A single, complete introduction to graph neural networks — the two earlier write-ups merged into one, losing none of the figures or interactive simulations. It runs in two parts: **Part 1, explained simply**, builds the anatomy (encoder → message-passing layers → readout → training); **Part 2, a working introduction**, covers the main architectures, the tasks, the failure modes, and where graph learning fits vehicle health.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/graph-neural-networks.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

Both parts live at one URL, with a jump-nav between them. Part 1 is the plain anatomy with the message-passing demo; Part 2 is the working introduction with the architecture comparisons and the message-passing sandbox.

---

← Back to [Autonomy]({{ '/' | relative_url }})
