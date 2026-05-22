---
title: "Koopman Theory — A Linear Lens for Nonlinear Worlds"
subtitle: "Every nonlinear system is secretly linear, if you agree to look at the right things. An interactive primer on the Koopman operator, from Koopman's 1931 paper through DMD, EDMD, Koopman-MPC, and the data-driven methods now powering modern model-based control."
date: 2026-05-18 10:00:00 -0400
category: "Control Systems"
slug: koopman-theory-primer
excerpt: "Nearly every dynamical system worth controlling is nonlinear. Nearly every tool we have — stability proofs, frequency analysis, MPC — is built for linear systems. Bernard Koopman's 1931 insight is the bridge: if you look at the right functions of the state instead of the state itself, even strongly nonlinear dynamics become linear. This primer walks through the operator, its modern data-driven approximations (DMD, EDMD, deep variants), and how it ends up inside today's MPC and RL pipelines."
reading_time: 25
---

A pendulum's equation of motion is nonlinear in the angle. A motor's torque equation is nonlinear once you include saturation, cogging, or back-EMF. A fluid is famously nonlinear. Yet most of the analysis and control tools we actually trust — root locus, frequency response, the LQR, Kalman filtering, linear MPC — were built for linear systems. The standard answer is to *linearize around a trim point*, with full awareness that the resulting model degrades the moment the system moves too far away from that point.

In 1931, Bernard Koopman proposed a much more radical answer: don't linearize the system, *change what you're looking at*. Instead of tracking the state itself, track scalar-valued functions *of* the state — what Koopman called *observables*. The infinite-dimensional vector space of these observables evolves under a linear operator, no matter how nonlinear the underlying system is. The trade is an honest one — you have given up the finite state dimension, but in exchange you have global, exact linearity.

For sixty years that was a beautiful mathematical fact that nobody could compute with. Then in the 2000s a data-driven approximation called Dynamic Mode Decomposition arrived, and shortly after that EDMD, deep Koopman, and the family of algorithms that lets engineers actually build a finite-dimensional linear surrogate from data. Today the operator sits underneath a substantial slice of modern model-predictive control and a growing fraction of model-based reinforcement learning.

This primer is the working tour I wish I'd had when I first encountered the idea.

## What it covers

Seven sections, about twenty-five minutes if you read the prose. Longer if you stop to play with the figures, which is the point.

**§ i — The big idea.** Change what you look at, and nonlinearity disappears. The Duffing oscillator drawn in the original state space (crooked, looping trajectories) and then in a higher-dimensional space of observables (straight lines). The geometric intuition, before any operator notation.

**§ ii — The operator.** The Koopman operator $\mathcal{K}$ as the linear object that pushes any observable forward by one time step: $\mathcal{K} \varphi = \varphi \circ F$. Why this is exactly linear, what it costs (infinite dimensionality), and the eigendecomposition that organizes everything that follows.

**§ iii — Lifting.** What an "observable" actually is, how the choice of dictionary determines the quality of your linear model, and the standard families — monomials, RBFs, Fourier, neural-network features. The geometric picture: a curved manifold of trajectories in state space becomes a flat invariant subspace in observable space.

**§ iv — DMD.** Dynamic Mode Decomposition — the algorithm that made Koopman computable. The SVD-based least-squares fit, the eigenmodes and their physical meaning (frequencies and growth rates), and the connection between DMD's spectrum and Koopman's. A live "fit a DMD model to a noisy nonlinear trajectory" demo where you can pick the rank.

**§ v — EDMD and beyond.** Extended DMD with explicit dictionaries; kernel DMD when you can't write down good features by hand; deep Koopman, where the dictionary itself is learned end-to-end by a neural network.

**§ vi — Koopman MPC.** The headline practical application: build a linear surrogate of a nonlinear plant from data, then run *linear* MPC — fast QPs, predictable convergence, real-time guarantees — over the lifted state. Korda & Mezić (2018) showed this works on real systems. The trade-offs versus nonlinear MPC and feedback linearization.

**§ vii — Koopman + RL.** The newer frontier: linear dynamics in observable space turn the value function into something with structure you can exploit, give you a model-based RL setup whose model is exact (in the limit) rather than approximate, and yield interpretable failure modes when the dictionary is too small.

**Playground.** A final interactive panel where you can pick a nonlinear vector field, choose a dictionary, fit a Koopman model, and watch the linear-prediction error grow or shrink with dictionary size.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/koopman-theory-primer.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

The primer lives at its own URL with a light editorial layout — amber and copper accents, serif body, MathJax-typeset equations, and live canvases for every figure. It is meant to be read once cover to cover and then reached for again whenever a specific term ("EDMD?", "the lifted-state trick?") needs a quick refresher.

---

← Back to [Autonomy]({{ '/' | relative_url }})
