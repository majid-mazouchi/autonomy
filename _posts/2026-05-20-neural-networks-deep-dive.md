---
title: "Neural Networks — Deep Dive Reference"
subtitle: "The long-form companion to the interactive primer. Eighteen terms, worked out at length — intuition, math, variants, practical details, and the common pitfalls that go with each."
date: 2026-05-20 10:00:00 -0400
category: "Neural Networks"
slug: neural-networks-deep-dive
excerpt: "The long-form reference behind the interactive neural-networks primer. Eighteen entries — train/val/test splits, preprocessing pipelines, Savitzky–Golay smoothing, outlier methods, gradient descent and its variants, learning-rate schedules, regularization, hyperparameter search, backprop, MLPs, RNNs, quantization, pruning, knowledge distillation, and the full compression stack for edge deployment — each with the math, the gotchas, and the practical defaults."
reading_time: 35
---

The interactive primer is the picture. This is the text underneath each picture, written out as a proper reference.

For each of the eighteen terms below, the deep dive gives you four things in roughly the same order: the *intuition* in plain English, the *math* (just enough — no theorem statements, no proofs that aren't worth the space), the *variants and how they differ from each other*, and a "Traps" box at the end with the failure modes that actually show up in practice. The intent is that you'd skim the primer for the picture, and come here when you need to remember whether Savitzky–Golay's window has to be odd, or what the linear-scaling rule for batch size actually says, or whether structured pruning helps on a GPU.

## What it covers

Eighteen entries, organized into four groups. About thirty-five minutes if you read it cover-to-cover; closer to two minutes per entry if you're using it as a reference.

**Data & evaluation.** Train/validation/test splits with the failure modes that quietly inflate metrics (feature leakage, temporal leakage, group leakage). The seven-step signal-preprocessing pipeline drawn out in detail. Savitzky–Golay smoothing — the local-polynomial least-squares math, the window/order trade-off, the causal-SG variant when you can't tolerate group delay (it matters in motor-control observers). Outlier methods compared side by side — z-score, IQR, Hampel, model-based residuals. Regime grouping (binning by operating point) — why a model that looks good on aggregate RMSE can still fail catastrophically inside one temperature bin. Underfitting and overfitting, each as its own entry with the diagnostic signatures spelled out.

**Training.** Gradient descent — the update rule, mini-batch SGD, momentum, Adam, and the trade-off each one is buying. Learning rate — the most important hyperparameter, with the schedule families (cosine annealing, warmup-cosine for transformers, step decay, SGDR with warm restarts, reduce-on-plateau) and the linear-scaling rule for batch size. Regularization — L1 vs L2 (why one drives weights to zero and the other only shrinks them), dropout (why it's an ensemble approximation), early stopping (the cheapest form). Hyperparameter search — grid, random (and why it usually beats grid), Bayesian methods (TPE, GP-EI, surrogate plus acquisition), multi-fidelity methods (Hyperband, BOHB, ASHA) that cut bad trials early. Backpropagation — reverse-mode autodiff, the chain rule applied backwards through the computation graph, same complexity as the forward pass.

**Architectures.** Feedforward networks — the universal approximator, activation choices, layer-norm vs batch-norm, residual connections. Recurrent networks — hidden-state recursion, vanishing and exploding gradients, the LSTM gates, GRU as a simplification, and why transformers eventually replaced RNNs for most sequence tasks.

**Compression.** Quantization — symmetric vs asymmetric, per-tensor vs per-channel, post-training (PTQ) vs quantization-aware training (QAT), and the regimes where each one works. Pruning — magnitude-based vs gradient-based, unstructured (max compression, needs sparse hardware) vs structured (real speedup on any hardware), the prune-then-fine-tune loop. Knowledge distillation — soft targets, temperature, the dark-knowledge argument, and why student architectures don't have to match teacher architectures. The full compression stack for edge — distill → prune → quantize → deploy, and how the multipliers compound to give 50–100× total reduction on real models.

Each entry stands on its own and has its own table of contents anchor, so you can deep-link straight to "L1 vs L2" or "QAT" without scrolling.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/neural-networks-deep-dive.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the deep-dive reference →
  </a>
</div>

The reference lives at its own URL with a long-form dark layout — sticky left TOC, eighteen anchored sections, "🚨 Traps" boxes at the end of each entry. It's the companion to the [Neural Networks — An Interactive Primer]({{ '/posts/neural-networks-interactive-concepts/' | relative_url }}) post, which is the visual entry point: read the primer first if you want the intuition; come here when you need the details.

---

← Back to [Autonomy]({{ '/' | relative_url }})
