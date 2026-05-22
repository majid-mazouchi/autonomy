---
title: "Optimization Methods — An Interactive Reference"
subtitle: "The algorithms that fit models and minimize loss, from closed-form Least Squares to Adam — eight working sections, a glossary, and a one-page cheat sheet. Every visualization runs the real math, not a pre-baked curve."
date: 2026-05-14 10:00:00 -0400
category: "Machine Learning"
slug: optimization-methods-reference
excerpt: "Every model in machine learning, every system identification routine, every adaptive controller has an optimization problem at its core. This reference walks through the algorithms that solve them — Least Squares (closed form and recursive), gradient descent (batch, stochastic, mini-batch), the adaptive variants (momentum, RMSProp, Adam), Newton and quasi-Newton methods — with live plots driven by the actual math and a section of rules of thumb collected from years of watching loss curves."
reading_time: 24
---

If you trace any modern engineering pipeline back far enough, you find an optimization problem at its bottom: fitting a regression, identifying a plant from data, training a neural network, tuning a controller. The methods used to solve them are mostly old — Least Squares is from Gauss, gradient descent is from Cauchy — but the variants that actually run in practice (Adam, AdamW, RLS with forgetting factor, Levenberg–Marquardt) are recent enough that the textbook treatments and the working knowledge have drifted apart.

This reference is for the working knowledge. Eight algorithm families, each shown with a live visualization where you drag the learning rate or the regularization, watch the trajectory, and see why one method beats another on this particular loss landscape. The math is here too — closed-form solutions, gradient updates, convergence rates — but it's secondary to the picture. The intent is that the next time you reach for SGD with momentum vs Adam vs Newton, you have a visual memory of when each one shines and when each one fails.

## What it covers

Ten sections, about twenty-four minutes if you read straight through, much longer if you stop to play with the sliders.

**§ 01 — The optimization problem.** What we're actually doing. Loss functions, the gradient, convex vs non-convex landscapes, local vs global minima, the geometry that determines whether the problem is easy or hard.

**§ 02 — Least Squares (closed form).** The one optimization problem we can solve exactly. The normal equations, $X^\top X \beta = X^\top y$, the geometric interpretation (projection onto the column space of $X$), the QR-decomposition implementation that's actually numerically stable, and the regularized variant (Tikhonov / ridge) that fixes the singular cases.

**§ 03 — Recursive Least Squares (RLS).** The online version of LS — the bread-and-butter of adaptive identification. The covariance update, the gain vector, the forgetting factor for tracking time-varying systems, and the numerical gotchas (covariance blow-up, conditioning) that have ended more than one student project.

**§ 04 — Gradient descent.** The general-purpose hammer. Batch gradient descent, the update rule, the role of the learning rate, why the gradient is the *steepest* direction but rarely the *best* direction. Live: a 2D quadratic loss with adjustable conditioning so you can watch GD's classic zigzag pathology emerge.

**§ 05 — Stochastic and mini-batch GD.** The version of GD that actually scales. Why noise in the gradient is a feature, not a bug. Mini-batches, the linear scaling rule, how batch size trades off against generalization.

**§ 06 — Momentum, RMSProp, Adam.** The adaptive family. Momentum as a low-pass filter on the gradient (Polyak / heavy ball). RMSProp's per-coordinate learning rate. Adam as the combination of both, with the bias correction that makes it work in early iterations. Why Adam is the default for neural networks and why it isn't always the right choice for convex problems.

**§ 07 — Second-order methods.** Newton's method, the quadratic-convergence story, why nobody actually uses pure Newton. BFGS and L-BFGS as the practical quasi-Newton methods. Gauss–Newton for least-squares structure. Levenberg–Marquardt as the damped variant that interpolates between Gauss–Newton and gradient descent.

**§ 08 — Rules of thumb.** Twenty-or-so things I've found myself repeating in code reviews. Learning rate is the most important hyperparameter. If the loss explodes after one step, your LR is too high *and your gradient probably has a bug*. Adam's default $\beta_2 = 0.999$ is wrong for short training runs. Etc.

**§ 09 — Glossary.** Every term used elsewhere in the reference, defined precisely, with cross-links back to where it's used.

**§ 10 — Cheat sheet.** Every method on one page — update rule, hyperparameters, when to use it, what to watch out for. Designed to be the thing you reach for during a model-tuning session.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/optimization-methods-reference.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the reference →
  </a>
</div>

The reference lives at its own URL with a dark editorial layout — cyan accent, italic Georgia display, JetBrains Mono for code. Every visualization is computed live from the algorithm, not a pre-baked animation.

---

← Back to [Autonomy]({{ '/' | relative_url }})
