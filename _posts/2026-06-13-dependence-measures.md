---
title: "Reading the Couplings — Dependence Measures for System Health"
subtitle: "When two signals shouldn't be coupled and become coupled, or two signals should be coupled and decouple, you've found a fault. This is the toolkit for measuring it."
date: 2026-06-13 18:00:00 -0400
category: "Control Systems"
slug: dependence-measures
excerpt: "Post 4 of the VHM statistical-methods series. A fault often shows up not in a single signal but in the relationship between two. The toolkit for measuring relationships is broader than just Pearson correlation: rank correlations for monotonic non-linearity, distance correlation and HSIC for arbitrary non-linearity, mutual information for the full distributional story, copulas for the tail dependence that matters at failure. This monograph covers them all, with the practical guidance for when to reach for which."
reading_time: 24
---

This is Post 4 of the six-part VHM statistical-methods series. The first three posts ([spectral]({{ '/posts/spectral-analysis/' | relative_url }}), [residual]({{ '/posts/residual-analysis/' | relative_url }}), [change detection]({{ '/posts/change-detection/' | relative_url }})) looked at a single signal — its frequency content, its deviation from a model, its temporal stability. This one is about *pairs* of signals. The next two ([multivariate]({{ '/posts/multivariate-monitoring/' | relative_url }}) and [probabilistic]({{ '/posts/probabilistic-methods/' | relative_url }})) generalize to N signals and full distributions.

A fault often hides between two signals. A battery cell that should track its sister cells starts drifting independently — the *coupling* breaks. A motor's current and torque, which should be linked by the motor constant, start showing a residual non-linearity — a new coupling has appeared. The pairwise diagnostic is the relationship, not the signal. The methods for measuring relationships span from the textbook (Pearson correlation) to the modern (distance correlation, HSIC, copulas) — and the choice between them is more consequential than most engineers realize.

Pearson correlation is famous for measuring linear relationships and famous for *missing* everything else. A perfectly deterministic non-linear relationship — a parabola, a circle — has Pearson correlation zero. The methods in this monograph are the answer to "what do I reach for when Pearson is hiding the dependence I need to see?"

## What it covers

About twenty-four minutes of careful reading.

**Pearson and the linear case.** What it measures, what it misses, the famous Anscombe's quartet that demonstrates why it's not enough.

**Rank correlations.** Spearman and Kendall's tau. Robust to outliers, sensitive to *monotonic* non-linearity (any rank-preserving transform). The right reach when you suspect non-linearity but believe the order is preserved.

**Distance correlation.** Székely's elegant 2007 measure that's zero if and only if two variables are independent. Catches any kind of dependence — linear, non-linear, non-monotonic. The bias-corrected estimator that makes it work on small samples.

**HSIC (Hilbert-Schmidt Independence Criterion).** The kernel-method approach to the same problem. The connection to RKHS. When the kernel choice matters.

**Mutual information.** The information-theoretic measure. The full picture (distance correlation is essentially a non-parametric approximation to mutual information). Estimation methods — k-NN, kernel density, the recent neural estimators (MINE, InfoNCE).

**Copulas.** The decoupling of marginals from joint structure. Why this matters at the tails — Gaussian copula vs. t-copula vs. Clayton vs. Gumbel — and why a Gaussian copula assumption is what made the 2008 financial crisis worse.

**A worked case study.** A battery-cell coupling problem. Pearson says everything's fine. Distance correlation says one cell has decoupled from its siblings. The diagnostic story.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/dependence-measures.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

## Code & data

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/dependence-measures-kit.zip' | relative_url }}" download>dependence-measures-kit.zip</a> — the Python source for every figure and example.</p>
</div>

## The VHM statistical-methods series

This is Post 4 of 6:

1. [Listening to the Machine]({{ '/posts/spectral-analysis/' | relative_url }}) — time-series and spectral analysis
2. [Reading the Residual]({{ '/posts/residual-analysis/' | relative_url }}) — model-based fault detection and isolation
3. [Catching the Change]({{ '/posts/change-detection/' | relative_url }}) — change and fault detection over time
4. **Reading the Couplings** — *(this post)* — dependence measures
5. [Reading the Whole Machine]({{ '/posts/multivariate-monitoring/' | relative_url }}) — multivariate monitoring
6. [Reasoning Under Uncertainty]({{ '/posts/probabilistic-methods/' | relative_url }}) — probabilistic methods

---

← Back to [Autonomy]({{ '/' | relative_url }})
