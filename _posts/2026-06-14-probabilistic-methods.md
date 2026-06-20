---
title: "Reasoning Under Uncertainty — Probabilistic Methods for Condition Monitoring"
subtitle: "Diagnosis is always a probability statement: given everything observed, how likely is each candidate fault? This monograph is the Bayesian toolkit that makes that probability statement honest."
date: 2026-06-14 12:00:00 -0400
category: "Control Systems"
slug: probabilistic-methods
excerpt: "Post 6 of the VHM statistical-methods series — and the one that ties the previous five together. Bayes' rule as the diagnostic framework. The Kalman filter and particle filter as state-estimation workhorses. Bayesian networks for structured causal reasoning. Gaussian processes for non-parametric prognosis. Bayesian model averaging for the cases where you don't trust any single model. With a worked case study fusing every previous post's signals into a single posterior over the candidate faults."
reading_time: 28
---

This is the final post in the six-part VHM statistical-methods series, and it is the one that ties the rest together. The previous five posts — [spectral]({{ '/posts/spectral-analysis/' | relative_url }}), [residual]({{ '/posts/residual-analysis/' | relative_url }}), [change detection]({{ '/posts/change-detection/' | relative_url }}), [dependence measures]({{ '/posts/dependence-measures/' | relative_url }}), [multivariate]({{ '/posts/multivariate-monitoring/' | relative_url }}) — each produced one or more diagnostic *features* (an RMS, a kurtosis, a T², a residual). This post is about what to do with those features once you have them. The answer, in the end, is Bayesian reasoning: given everything observed, what is the posterior probability of each candidate fault?

Diagnosis is always a probability statement. The classical-control engineer who reports "the bearing has failed" without a probability is, in fact, reporting "P(bearing failure | evidence) > some implicit threshold I haven't told you about." Making the threshold explicit, and the calculation principled, is the entire program of Bayesian condition monitoring. It is also the only honest way to combine multiple diagnostic features that each carry partial information, and the only way to track the *evolving belief* about system health as more evidence arrives over time.

The natural companion is the [agentic RCA framework]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}) — that framework's "hypothesizer" agent is, formally, a Bayesian posterior computer that consumes the features the methods in this series produce. The classical-control side of the same machinery is in the [Adaptive Control]({{ '/posts/adaptive-control-field-guide/' | relative_url }}) and [Optimal Control]({{ '/posts/optimal-control-field-guide/' | relative_url }}) field guides (which use these methods inside the controller rather than the diagnostic layer).

## What it covers

About twenty-eight minutes of careful reading.

**Bayes' rule and diagnostic posteriors.** The framework. Prior over fault states. Likelihood of evidence given fault. Posterior over fault states. The discipline of treating diagnosis as a posterior calculation rather than a yes/no decision.

**The Kalman filter as Bayesian state estimation.** Why the KF is the recursive Bayesian update for linear-Gaussian systems. The extended KF and unscented KF for the non-linear case. The diagnostic interpretation of the innovation sequence (cross-reference to [residual analysis]({{ '/posts/residual-analysis/' | relative_url }})).

**Particle filters.** When the linear-Gaussian assumption breaks. The sample-based representation of the posterior. The resampling discipline. When the computational cost is worth it (almost always, in modern hardware).

**Bayesian networks for fault diagnosis.** Encoding the causal structure of a system. The fault-tree-to-Bayesian-network mapping. Exact inference (when the graph is tractable). Loopy belief propagation and the Monte Carlo alternatives (when it isn't).

**Gaussian processes for prognosis.** Non-parametric Bayesian regression. The mean-and-uncertainty output that's exactly what RUL forecasting needs. The kernel choice as the modeling decision.

**Bayesian model averaging.** The honest answer to "I have three models that all fit the data but disagree about the future." Weight by posterior probability, average the forecast. The forecast that's calibrated even when no single model is right.

**A worked case study.** Take the synthetic battery dataset from [Case 1]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }}). Run every method from the previous five posts on it. Feed the features into a Bayesian network with the candidate-fault structure. Compute the posterior. Compare to the ground truth. The full closure of the series.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/probabilistic-methods.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

## Code & data

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/probabilistic-methods-kit.zip' | relative_url }}" download>probabilistic-methods-kit.zip</a> — the Python source for every figure and example, including the fully-worked Bayesian network case study.</p>
</div>

## The VHM statistical-methods series

This is Post 6 of 6 — the closing post:

1. [Listening to the Machine]({{ '/posts/spectral-analysis/' | relative_url }}) — time-series and spectral analysis
2. [Reading the Residual]({{ '/posts/residual-analysis/' | relative_url }}) — model-based fault detection and isolation
3. [Catching the Change]({{ '/posts/change-detection/' | relative_url }}) — change and fault detection over time
4. [Reading the Couplings]({{ '/posts/dependence-measures/' | relative_url }}) — dependence measures
5. [Reading the Whole Machine]({{ '/posts/multivariate-monitoring/' | relative_url }}) — multivariate monitoring
6. **Reasoning Under Uncertainty** — *(this post)* — probabilistic methods

---

← Back to [Autonomy]({{ '/' | relative_url }})
