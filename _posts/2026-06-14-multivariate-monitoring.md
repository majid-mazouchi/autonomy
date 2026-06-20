---
title: "Reading the Whole Machine — Multivariate Monitoring"
subtitle: "When the diagnosis lives in the joint distribution of many sensors, the right tools are the multivariate ones: Hotelling's T², PCA-based control limits, partial least squares, and the modern auto-encoder cousins."
date: 2026-06-14 09:00:00 -0400
category: "Control Systems"
slug: multivariate-monitoring
excerpt: "Post 5 of the VHM statistical-methods series. Real machines don't fail in one signal — they fail across a joint distribution of dozens or hundreds. The classical multivariate toolkit (Hotelling's T², PCA, PLS, the SPE residual statistic) and its modern auto-encoder cousins are the methods that scale from 'monitor one sensor' to 'monitor the whole machine.' With a worked case study running the full toolkit on a synthetic powertrain dataset."
reading_time: 26
---

This is Post 5 of the six-part VHM statistical-methods series. The previous post ([dependence measures]({{ '/posts/dependence-measures/' | relative_url }})) covered the pairwise question: how do you measure the relationship between two signals? This one generalizes to N signals: how do you monitor the *joint* behavior of an entire instrumented system?

The need is obvious in practice. A modern vehicle has hundreds of telematics channels. A modern battery pack has dozens of cell-voltage measurements. A modern motor controller logs current, voltage, temperature, position, and a dozen derived signals. Monitoring each one independently — with the methods of the previous four posts — misses the most diagnostic information, which is in the *joint* deviation. The classical multivariate toolkit (Hotelling's T², PCA-based control charts, partial least squares) is the answer for moderate dimensions; the modern auto-encoder approach extends it to the high-dimensional case where N exceeds the sample count.

This is also the post where the *false-alarm-rate problem* becomes acute. If you have 100 sensors and you alarm whenever any one of them goes 3σ out, you'll false-alarm constantly even when everything is fine. The multivariate methods are the principled answer — they alarm on the joint deviation, not the marginal deviation, and the false-alarm rate is controlled by design.

## What it covers

About twenty-six minutes of careful reading.

**Hotelling's T².** The multivariate generalization of the one-sample t-test. The chi-squared distribution under the null. The control-limit calculation. When this is the right reach (low-dimensional, Gaussian-ish data) and when it isn't.

**PCA-based control charts.** The two-statistic monitoring approach. T² on the principal-component scores (changes *within* the model). SPE / Q-statistic on the residual (changes *outside* the model). Why both are needed and what each one catches.

**Partial least squares.** When you have both input variables and quality outputs. The structure that makes PLS the workhorse of pharmaceutical and chemical process monitoring. Adaptation to control-engineering applications.

**Auto-encoder anomaly detection.** The neural-network generalization. Train an auto-encoder to reconstruct healthy data; the reconstruction error is the modern SPE statistic. The bias-variance trade-off with model size. When this earns its keep over classical PCA.

**False-alarm and detection-rate analysis.** The ROC curve framework. The threshold-tuning discipline that's the difference between a useful monitor and an annoying one.

**A worked case study.** A synthetic powertrain dataset — 24 telemetry channels, one slowly-developing fault. Run every method above; show the detection time, the false-alarm rate, the isolation strength. The decision matrix that picks the right method for the data shape.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/multivariate-monitoring.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

## Code & data

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/multivariate-monitoring-kit.zip' | relative_url }}" download>multivariate-monitoring-kit.zip</a> — the Python source for every figure plus the synthetic 24-channel powertrain dataset.</p>
</div>

## The VHM statistical-methods series

This is Post 5 of 6:

1. [Listening to the Machine]({{ '/posts/spectral-analysis/' | relative_url }}) — time-series and spectral analysis
2. [Reading the Residual]({{ '/posts/residual-analysis/' | relative_url }}) — model-based fault detection and isolation
3. [Catching the Change]({{ '/posts/change-detection/' | relative_url }}) — change and fault detection over time
4. [Reading the Couplings]({{ '/posts/dependence-measures/' | relative_url }}) — dependence measures
5. **Reading the Whole Machine** — *(this post)* — multivariate monitoring
6. [Reasoning Under Uncertainty]({{ '/posts/probabilistic-methods/' | relative_url }}) — probabilistic methods

---

← Back to [Autonomy]({{ '/' | relative_url }})
