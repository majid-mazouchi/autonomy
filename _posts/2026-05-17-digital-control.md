---
title: "Digital Control — From s to z, in Practice"
subtitle: "A working reference for the part of control engineering that lives on a microcontroller. Sampling, the z-transform, discretization, digital PID, stability, quantization, computational delay — eight sections, every plot live."
date: 2026-05-17 10:00:00 -0400
category: "Control Systems"
slug: digital-control
excerpt: "Continuous-time control theory is taught in s-domain. Real control runs at a fixed sample rate on a microcontroller, in z-domain, with finite numerical precision and a one-sample delay built in. This reference is for the gap between those two worlds — Nyquist, ZOH, Tustin, the velocity form of PID, the unit circle, fixed-point arithmetic, and the computational-delay budget that quietly decides what bandwidth you can actually achieve."
reading_time: 22
---

There is a particular gap in control engineering education between the continuous-time material you're taught in school — Bode plots, root locus, $s$-plane — and the code that ends up running on a microcontroller. The continuous theory is beautiful and stable; the embedded code is rife with sampling artifacts, quantization, integer overflow, and a stubborn one-sample computational delay that nobody warned you about. The math relating the two — bilinear transforms, the unit circle, the $z$-transform — is taught, but it tends to be taught as algebraic manipulation, not as practical engineering with consequences.

This reference is for that gap. Eight sections, each one a topic I find myself looking up over and over again when I'm writing or reviewing digital control code. Every plot below is generated live from the math: you adjust the sample rate, the controller gains, or the fixed-point word length, and the response curves redraw. The terminology is collected in sidebar glossaries so you can look up "ZOH" or "warping" without scrolling for ten minutes. Rules of thumb that took me years to internalize are stated explicitly.

## What it covers

Eight sections, about twenty-two minutes end to end — but it's designed to be reached for one section at a time when you need it.

**§ 01 — Sampling and aliasing.** The first decision, and the one whose consequences propagate the furthest. Nyquist, anti-aliasing filters, the zero-order hold, and the half-sample average delay you inherit from the DAC. With a live demo where you choose a continuous signal frequency, a sample rate, and watch it either get reconstructed cleanly or fold down to an alias.

**§ 02 — The z-transform.** What "$z$" actually represents (one-sample advance), why the unit circle is the new $j\omega$-axis, and the mapping $z = e^{sT_s}$ that links continuous frequency to digital frequency. The frequency response evaluated *on the unit circle* — and why you compute it the way you do.

**§ 03 — Discretization methods.** Three ways to turn a continuous transfer function into a discrete one: forward Euler (simple, can destabilize), backward Euler (always stable, distorts low frequencies), and Tustin / bilinear (the workhorse, with optional frequency prewarping for an exact match at one specified frequency). A live comparison: change $T_s$ and watch how the same plant looks under each method.

**§ 04 — Digital PID.** The textbook form, the velocity (incremental) form, why you almost always implement the velocity form in production code, derivative filtering, integrator anti-windup, and the bumpless-transfer trick for switching between manual and automatic modes. Every line of pseudocode includes the "if you skip this you'll regret it" notes.

**§ 05 — Stability in $z$.** The unit circle is the stability boundary. Where the poles land determines whether your system rings, decays, or blows up. Jury's test as the discrete-time analog of Routh. The discrete Lyapunov equation.

**§ 06 — Quantization and fixed-point.** What happens when your gains, signals, and accumulators have finite precision. The Q-format notation, scaling decisions, overflow, the quantization noise floor, and why your integrator drifts even when the input is exactly zero. With a slider for word length.

**§ 07 — Computational delay.** The dirty secret of digital control: the controller you implemented has *at least* one full sample of computational delay between when it reads the sensor and when its commanded output takes effect. This entry derives the phase-margin cost as a function of $f_{bw}/f_s$ and gives the rules of thumb for when you need to predict (Smith predictor, observer-based prediction) versus when you can just push the sample rate higher.

**§ 08 — Cheat sheet.** Everything above, condensed onto one page. The transforms, the discretization formulas, the PID forms, the stability criterion, the rules of thumb — laid out so you can reach for it during a code review.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/digital-control.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the reference →
  </a>
</div>

The reference lives at its own URL with a warm-paper engineering-journal layout — burnt-red accent, Fraunces display, JetBrains Mono UI. Every figure is rendered from the math in real time, so the knobs are the point.

---

← Back to [Autonomy]({{ '/' | relative_url }})
