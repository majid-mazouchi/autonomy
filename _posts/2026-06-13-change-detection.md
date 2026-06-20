---
title: "Catching the Change — Change and Fault Detection Over Time"
subtitle: "A field guide to the tests that decide whether a signal has changed: as it streams, the moment it shifts, and afterward, what kind of change it was."
date: 2026-06-13 15:00:00 -0400
category: "Control Systems"
slug: change-detection
excerpt: "Post 3 of the VHM statistical-methods series. A fault announces itself as a change in time. The skill is deciding, from noisy data, that a change is real and not just scatter, and doing it fast enough to act. This monograph covers the online sequential tests (CUSUM, EWMA, GLR), the changepoint-localization methods, and the two-sample tests for what kind of change happened — with a live demo that lets you race the detectors and a worked case study running the whole ladder on one fault."
reading_time: 26
---

This is Post 3 of the six-part VHM statistical-methods series. The previous two posts ([spectral analysis]({{ '/posts/spectral-analysis/' | relative_url }}) and [residual analysis]({{ '/posts/residual-analysis/' | relative_url }})) covered methods that examine a signal's *content* — what it looks like, what its frequencies are, how it deviates from a model. This one is about something different: *whether* and *when* it changed.

A fault announces itself as a change in time. Pressure that was stable starts trending up. A vibration RMS that was running at 0.8 g jumps to 1.1 g. A residual that lived around zero starts walking. The diagnostic skill is deciding, from noisy data, that a change is *real* (not just scatter) and doing it *fast enough to act*. The methods in this monograph split cleanly by which question they answer: *Changing now?* (online streaming detection), *When and how big?* (retrospective localization), *What kind?* (two-sample distributional tests).

This is the post where the trade-off between *false-alarm rate* and *detection delay* becomes vivid. You can detect any change you want, instantly, if you're willing to false-alarm constantly. The art of change detection is finding the operating point on that curve that fits your application — and the methods give you the dials to do it.

## What it covers

Three groups of methods, about twenty-six minutes of careful reading.

**Online streaming detection (changing now?).** CUSUM (the cumulative-sum test, the workhorse since the 1950s). EWMA (exponentially weighted moving average — Shewhart's update). GLR (generalized likelihood ratio — the theoretically optimal but computationally heavier alternative). When each one is the right reach.

**Retrospective changepoint localization (when and how big?).** Binary segmentation. Pruned exact linear time (PELT). The information-criterion frameworks for choosing the number of changepoints when you don't know it a priori.

**Distributional change tests (what kind?).** Kolmogorov-Smirnov for general distributional shift. Wasserstein distance for "how far did the distribution move." Mann-Whitney and the rank-based alternatives for when assumptions are scarce. The discipline of choosing the right test for the question you're asking.

**Two interactive explorers.** A drag-the-changepoint demo that lets you race CUSUM, EWMA, and GLR side-by-side and see which one detects fastest. A two-sample distribution explorer that shows how each test responds to different kinds of shift.

**A worked case study.** One synthetic fault — a small step change with noise — run through every method above. The detection delays. The false-alarm trade-offs. The decision tree that picks the right method for the operational context.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/change-detection.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

## Code & data

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/change-detection-kit.zip' | relative_url }}" download>change-detection-kit.zip</a> — the Python source for every figure and explorer.</p>
</div>

## The VHM statistical-methods series

This is Post 3 of 6:

1. [Listening to the Machine]({{ '/posts/spectral-analysis/' | relative_url }}) — time-series and spectral analysis
2. [Reading the Residual]({{ '/posts/residual-analysis/' | relative_url }}) — model-based fault detection and isolation
3. **Catching the Change** — *(this post)* — change and fault detection over time
4. [Reading the Couplings]({{ '/posts/dependence-measures/' | relative_url }}) — dependence measures
5. [Reading the Whole Machine]({{ '/posts/multivariate-monitoring/' | relative_url }}) — multivariate monitoring
6. [Reasoning Under Uncertainty]({{ '/posts/probabilistic-methods/' | relative_url }}) — probabilistic methods

---

← Back to [Autonomy]({{ '/' | relative_url }})
