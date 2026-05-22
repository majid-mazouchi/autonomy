---
title: "Neural Networks — An Interactive Primer"
subtitle: "Thirteen core concepts of modern neural-network practice, each with sliders to drag, canvases to watch, and a short essentials box that says what to actually remember."
date: 2026-05-21 10:00:00 -0400
category: "Neural Networks"
slug: neural-networks-interactive-concepts
excerpt: "An interactive walkthrough of the thirteen ideas every neural-network practitioner reaches for — dataset splits, signal preprocessing, the bias–variance trade-off, gradient descent, learning-rate schedules, regularization, hyperparameter search, the training loop, MLPs, RNNs, quantization, pruning, and knowledge distillation. Each topic has live controls and a practical-essentials summary."
reading_time: 18
---

There is a particular failure mode in learning neural networks where everything looks tractable on paper — backprop is just the chain rule, an LSTM cell is six lines of math — and then you sit down with PyTorch and the loss curve does something strange and you realize you don't quite have the right *mental* picture of any of it.

This post is the one I wish I'd had at that point. Thirteen of the concepts you'll reach for over and over again — from the dataset split all the way down to a quantized model on an edge device — each presented as an interactive panel where the math is right next to a slider that demonstrates it. Drag the learning rate up and watch the loss surface diverge. Crank the dropout probability and see the validation curve catch up to the training curve. Compare INT8 vs INT4 reconstruction error on the same signal. The idea is that the *intuition* should land first; the formulas then sit on top of something you've already seen with your eyes.

## What it covers

Thirteen sections plus a concept cheat sheet at the end. About fifteen to twenty minutes if you read it; longer if you actually play with the controls, which is the point.

**Data & Evaluation.** Dataset splits — train, validation, test — with a slider that re-allocates ten thousand samples across the three buckets and recomputes the bar widths in real time. Signal preprocessing — the seven-step pipeline (anti-alias, detrend, outlier removal, smooth, normalize, feature-engineer, regime-label) drawn out as a flow with notes on each stage. The bias–variance trade-off — a model-complexity slider you can drag from underfit to overfit and watch the training and validation curves diverge.

**Training.** Gradient descent on a live loss surface — drag the learning rate and momentum and watch the trajectory either find the minimum, oscillate, or shoot off the edge. Learning-rate schedules — cosine annealing, warmup-cosine, step decay, SGDR, reduce-on-plateau, each plotted with the parameters you'd actually use. Regularization — L1, L2, dropout, early stopping — with knobs for each so you can see the validation curve respond. Hyperparameter search — grid, random, Bayesian, Hyperband — drawn with the trial-budget trade-off made explicit. The training loop itself — the seven-line PyTorch pattern that almost every real model is built around.

**Architectures.** Feedforward networks — the universal approximator, drawn out layer-by-layer with the activation choices that actually matter (ReLU, GELU, SiLU, tanh). Recurrent networks — the hidden-state recursion, why vanilla RNNs fail on long sequences, and what LSTM and GRU did about it.

**Model compression.** Quantization — FP32 → INT8 → INT4 with the actual numerical error visualized on a sample weight tensor. Pruning — unstructured vs structured, with a slider that drops weights below a magnitude threshold and shows what happens to accuracy. Knowledge distillation — temperature, soft-vs-hard targets, and why distilling a 100M-parameter teacher into a 10M-parameter student is the standard edge-deployment recipe.

**Concept cheat sheet.** The sixty-second answer for every term above, with deep-links into the long-form deep-dive reference for when you need more.

Each section also has a "Practical essentials" box at the bottom — the four or five things you'd actually want someone to remember a month later.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/neural-networks-interactive-concepts.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the interactive primer →
  </a>
</div>

The primer lives at its own URL with a dark dashboard-style layout — indigo-and-cyan accents, sticky left nav, live canvases. It pairs with the [Neural Networks — Deep Dive Reference]({{ '/posts/neural-networks-deep-dive/' | relative_url }}) post, which is the long-form companion: for every term you can click on the cheat sheet, the deep dive has the math, the variants, and the gotchas worked out at length.

---

← Back to [Autonomy]({{ '/' | relative_url }})
