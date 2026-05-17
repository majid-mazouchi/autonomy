---
title: "On Filters — Analog and Digital, First-Order and Beyond"
subtitle: "From the humble RC pair to the exacting geometry of Butterworth, Chebyshev, and Elliptic — an interactive walk through the analog and digital frontiers of frequency selectivity."
date: 2026-04-25 10:00:00 -0400
category: "Control Systems"
slug: on-filters
excerpt: "A field guide to filters — what they are, why classical electrical engineering spent decades designing them, and the seven chapters that take you from RC pairs through the bilinear transform to the modern IIR archetypes."
reading_time: 10
---

A filter is, at heart, a polite machine for ignoring. It selects a band of frequencies to pass, another to suppress — and its elegance lies entirely in how gracefully it draws that line.

That's the engineering aesthetic that produced Butterworth, Chebyshev, Elliptic, and Bessel filters in the 1920s through 1950s, each with a different theory of "graceful" and a different geometric signature in the s-plane. They're still the defaults — most modern DSP code still implements them, because nobody has come up with a better way to be polite to frequencies. This primer is a tour through them, from first principles.

## What it covers

Seven chapters, live frequency-response plots, about thirty minutes to read.

**§1 — The Problem of Separation.** Why filtering is the dual of every signal-processing question. What "selecting a band" actually means in time and frequency.

**§2 — The RC Low-Pass — First Principles.** The simplest filter. Why its bode plot rolls off at -20 dB/dec exactly, where the cutoff comes from, and what the phase response is doing.

**§3 — The RC High-Pass — The Mirror Image.** The same circuit with one component swap. The lessons that generalize.

**§4 — Band-Pass — Two Poles Meet a Zero.** The geometry of a second-order resonant filter. Q factor, bandwidth, the way the poles move as you tune.

**§5 — From s-Plane to z-Plane — The Bilinear Transform.** The algebra that turns an analog filter into a digital one. Frequency warping. Why this works and where it breaks.

**§6 — The Archetypes — Butterworth, Chebyshev, Elliptic, Bessel.** Four design philosophies, four pole patterns, four characteristic responses. When to reach for each.

**§7 — A Word on IIR vs FIR.** Where the recursive vs feed-forward distinction starts to matter — group delay, numerical stability, transient response.

Every plot is live. Drag the cutoff, change the order, watch the response curve respond.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/on-filters.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
