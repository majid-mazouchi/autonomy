---
title: "Listening to the Machine — Time-Series & Spectral Condition Monitoring"
subtitle: "A field guide to the indicators that turn a raw vibration signal into a diagnosis: its correlation structure, its frequency content, its impulsiveness, and where in time a transient lives."
date: 2026-06-13 09:00:00 -0400
category: "Control Systems"
slug: spectral-analysis
excerpt: "The classical bedrock of vibration-based condition monitoring. RMS, kurtosis, crest factor in the time domain. The FFT, the power spectral density, order analysis in the frequency domain. The short-time Fourier transform, wavelets, envelope analysis when the fault is transient or non-stationary. Each method drawn out from first principles, illustrated on a synthetic rolling-element bearing dataset, and paired with the runnable Python that produces every figure."
reading_time: 26
---

This is the first post in a six-part series of **VHM (Vehicle Health Monitoring) statistical-methods monographs**. Each one covers a well-defined family of techniques that engineers reach for when a signal — a vibration, a current, a temperature, a flow rate — needs to be turned into a diagnosis. The six together are the working toolkit; this one is the most classical and the place to start.

Spectral analysis is the bedrock because the vibration signature of a rotating machine is one of the most information-rich diagnostic signals an engineer ever encounters. A failing bearing produces a characteristic impulse train at a frequency set by its geometry and shaft speed. An unbalanced rotor shows up at exactly 1× shaft speed. A loose gear mesh broadcasts at the gear-mesh frequency. None of this is hidden — it's all there in the spectrum if you know how to look. The methods in this monograph are the *how to look* discipline.

The post is the natural companion to the [RCA case study series]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }}) (these methods feed the analyses), the [Optimal Control Field Guide]({{ '/posts/optimal-control-field-guide/' | relative_url }}) (which uses spectral methods for system identification), and the rest of this six-part VHM series.

## What it covers

About twenty-six minutes of careful reading.

**Time-domain indicators.** RMS, peak, kurtosis, crest factor, skewness. The four statistics that almost every CMS (condition monitoring system) computes on every block of every channel. What each one is sensitive to, what each one misses, and the famous "bearing kurtosis story" — why kurtosis is the indicator that catches incipient bearing faults that RMS misses entirely.

**Frequency-domain analysis.** The DFT, the FFT, the power spectral density. Windowing and the spectral-leakage trade-off. Resolution, zero-padding, and the difference between *seeing* a peak and *measuring* it accurately. Order analysis for rotating machinery — the trick of transforming time to angle so that fault frequencies stay put as RPM varies.

**Time-frequency analysis.** When the signal isn't stationary. The short-time Fourier transform and the time-frequency trade-off it forces. Wavelets and the multi-resolution alternative. The spectrogram as a diagnostic tool.

**Envelope analysis.** The single most important technique for bearing diagnosis. Band-pass around the resonance, rectify, low-pass, FFT. Why this sequence works, what it pulls out of the noise that the raw FFT cannot, and the discipline for choosing the right resonance band.

**A worked example.** A synthetic rolling-element bearing dataset with a known inner-race fault, run through every method above. The figures, the indicators, the diagnostic confidence at each step.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/spectral-analysis.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

The field guide lives at its own URL with a warm-cream editorial layout — rust accent for the central diagnostic story, teal for the supporting math, ochre for practical-notes sections. Interactive figures throughout; every concept illustrated on the same synthetic bearing dataset.

## Code & data

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/spectral-analysis-kit.zip' | relative_url }}" download>spectral-analysis-kit.zip</a> — the Python source for every figure plus the synthetic bearing dataset. Reproducible from a single command.</p>
</div>

## The VHM statistical-methods series

This is Post 1 of 6. The full series:

1. **Listening to the Machine** — *(this post)* — time-series and spectral analysis
2. [Reading the Residual]({{ '/posts/residual-analysis/' | relative_url }}) — model-based fault detection and isolation
3. [Catching the Change]({{ '/posts/change-detection/' | relative_url }}) — change and fault detection over time
4. [Reading the Couplings]({{ '/posts/dependence-measures/' | relative_url }}) — dependence measures
5. [Reading the Whole Machine]({{ '/posts/multivariate-monitoring/' | relative_url }}) — multivariate monitoring
6. [Reasoning Under Uncertainty]({{ '/posts/probabilistic-methods/' | relative_url }}) — probabilistic methods

---

← Back to [Autonomy]({{ '/' | relative_url }})
