---
title: "Kalman and Particle Filters, in Plain Words"
subtitle: "The classical estimators that track a hidden state from noisy measurements — and how they relate to learned models."
date: 2026-07-01 10:00:00 -0400
category: "Neural Networks"
slug: kalman-and-particle-filters
excerpt: "The classical estimators that track a hidden state from noisy measurements. How the Kalman filter alternates predict and correct to fuse a model with data, why the extended and unscented variants exist, and how particle filters take over when the world is too nonlinear or non-Gaussian for a Kalman filter — plain words, figures, and the link to modern learned estimators."
reading_time: 14
---

The classical state estimators explained simply: how a Kalman filter tracks a hidden state through noise by predicting and correcting, when you need the extended and unscented variants, and how particle filters handle the nonlinear, non-Gaussian cases they can't.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/pinn-kalman-particle-filters.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL in the warm-paper layout, with figures and worked examples in plain words.

---

← Back to [Autonomy]({{ '/' | relative_url }})
