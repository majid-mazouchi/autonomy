---
title: "Reading the Residual — Model-Based Fault Detection and Isolation"
subtitle: "When the system has a model — analytical, gray-box, or data-driven — the residual between the model's prediction and the measured reality is the most diagnostic signal an engineer has."
date: 2026-06-13 12:00:00 -0400
category: "Control Systems"
slug: residual-analysis
excerpt: "Post 2 of the VHM statistical-methods series. The residual — what the model predicted minus what actually happened — is the workhorse signal of model-based diagnosis. This monograph covers parity equations, observer-based residuals, parameter-estimation residuals, and the structured-residual discipline that lets you isolate which fault occurred from a single residual vector. With a worked example on a battery state-of-charge model and runnable Python."
reading_time: 24
---

This is Post 2 of the six-part VHM statistical-methods series. The previous post ([spectral analysis]({{ '/posts/spectral-analysis/' | relative_url }})) covered the bedrock methods that turn a raw signal into diagnostic features. This one covers what to do when you have something stronger than just a signal — when you also have a *model* of the system, and the diagnostic question becomes "where does my model and reality disagree?"

The residual — what the model predicted minus what the sensor actually measured — is one of the most diagnostic signals in engineering. A well-designed residual is *zero in the absence of a fault* and *nonzero in a fault-specific direction when a fault occurs*. The "specific direction" is the trick: a *structured residual vector* not only tells you that something is wrong, it tells you *which* component is at fault. This is the heart of model-based fault detection and isolation (FDI), and it is one of the cleanest, most powerful patterns in classical control engineering.

The post is the natural companion to the [Loop Engineering]({{ '/posts/loop-engineering/' | relative_url }}) field guide (residuals are what closed-loop systems use to know if they're tracking) and the [Adaptive Control]({{ '/posts/adaptive-control-field-guide/' | relative_url }}) field guide (parameter-estimation residuals are how adaptive controllers detect mismatch).

## What it covers

About twenty-four minutes of careful reading.

**Parity equations.** The simplest residual generator. Algebraic relationships among sensors that should hold if the system is healthy. The redundancy that lets you find a contradiction.

**Observer-based residuals.** When you have a state-space model. The Luenberger observer as a residual factory. The Kalman filter as the optimal observer when there's noise. The innovation sequence as the diagnostic signal.

**Parameter-estimation residuals.** When the fault is a parameter shift rather than a sensor or actuator. Recursive least squares as the workhorse. Detecting *which* parameter shifted from the structure of the residual.

**Structured residual design.** The discipline that turns "something is wrong" into "X is wrong." Decoupling matrices. The geometric approach. The directional-residual conditions that make isolation possible.

**Threshold setting.** Where the math meets reality. Chi-squared thresholds for the linear-Gaussian case. CUSUM and GLR for the nonparametric cases. The trade-off between false alarms and missed detections, drawn out.

**A worked example.** A battery state-of-charge model with a known sensor-bias fault. The full residual generator from first principles, the chi-squared threshold, the detection delay, and the isolation matrix.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/residual-analysis.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

## Code & data

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/residual-analysis-kit.zip' | relative_url }}" download>residual-analysis-kit.zip</a> — the Python source for every figure plus the synthetic battery dataset.</p>
</div>

## The VHM statistical-methods series

This is Post 2 of 6:

1. [Listening to the Machine]({{ '/posts/spectral-analysis/' | relative_url }}) — time-series and spectral analysis
2. **Reading the Residual** — *(this post)* — model-based fault detection and isolation
3. [Catching the Change]({{ '/posts/change-detection/' | relative_url }}) — change and fault detection over time
4. [Reading the Couplings]({{ '/posts/dependence-measures/' | relative_url }}) — dependence measures
5. [Reading the Whole Machine]({{ '/posts/multivariate-monitoring/' | relative_url }}) — multivariate monitoring
6. [Reasoning Under Uncertainty]({{ '/posts/probabilistic-methods/' | relative_url }}) — probabilistic methods

---

← Back to [Autonomy]({{ '/' | relative_url }})
