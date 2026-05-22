---
title: "Optimal Control — A Field Guide for Working Engineers"
subtitle: "From the calculus of variations to Pontryagin's minimum principle to LQR, LQG, MPC, and nonlinear trajectory optimization — with the rules of thumb, embedded-implementation notes, and tuning heuristics the textbooks tend to skip."
date: 2026-05-13 10:00:00 -0400
category: "Control Systems"
slug: optimal-control-field-guide
excerpt: "Optimal control gets taught as proofs and Riccati equations; in practice it lives or dies on tuning, discretization, conditioning, and whether your solver finishes in the sample period. This field guide walks through the theory and the practice side by side — foundations, calculus of variations, Pontryagin, Bellman/HJB, LQR, the Riccati equation, LQG/Kalman, MPC, and nonlinear methods (iLQR, DDP, SQP) — and pairs each with practical implementation notes and four live simulations."
reading_time: 32
---

There is a particular failure mode in learning optimal control where the math is taught beautifully — proofs of Pontryagin's principle, derivations of the Riccati equation, statements about dynamic programming — and then six months later you sit down to build an actual MPC controller and discover that none of that helps you tune $Q$ and $R$, none of it tells you what to do when your QP solver doesn't converge in the sample period, and none of it warned you that fixed-point arithmetic was going to make your beautifully-conditioned Riccati iteration drift.

This field guide is meant to close that gap. The theory is here, in full — calculus of variations, Pontryagin's minimum principle, Bellman's principle of optimality, the algebraic and differential Riccati equations, the separation principle, MPC stability, iLQR and DDP — but each chapter is paired with the practical questions: what to actually use, how to tune it, where it breaks, and what to do when it does. Four chapters carry live simulations: drag $Q$ and $R$ on the LQR tuner and watch the closed-loop poles slide along the eigenvalue locus; tighten the MPC horizon and see how stability margin trades against computational cost; switch between bang-bang and smooth control on a satellite reorientation problem and watch the trajectory change.

## What it covers

Ten chapters plus an appendix. About thirty-two minutes end-to-end if you read it cover to cover — but it's deliberately structured for reaching one chapter at a time.

**Ch. 01 — Foundations.** What an optimal control problem actually is. The cost functional, the dynamics constraint, the terminal cost, the running cost. The vocabulary that the rest of the field guide assumes you have.

**Ch. 02 — Calculus of variations.** The Euler–Lagrange equation, derived from first principles and then specialized to the optimal-control setting. Boundary conditions. The transversality condition. The connection to classical mechanics that gives you the intuition for why this works.

**Ch. 03 — Pontryagin's minimum principle.** The big theorem of optimal control. The Hamiltonian, the costate, the necessary conditions. Why "minimum" and not "extremum" matters when you have control constraints. The bang-bang result. Live simulation: time-optimal control of a double integrator.

**Ch. 04 — Bellman / HJB.** Dynamic programming. The principle of optimality. The Hamilton–Jacobi–Bellman PDE. The curse of dimensionality and the discrete-state finite-horizon version where DP actually works.

**Ch. 05 — LQR.** The workhorse, treated in full. The continuous- and discrete-time formulations, the cost-to-go function, $Q$ and $R$ as design knobs, infinite-horizon LQR and its closed-form, finite-horizon LQR and its time-varying gain. Interactive: drag $Q$ and $R$, watch the closed-loop poles move and the simulated step response respond.

**Ch. 06 — The Riccati equation.** The algebraic Riccati equation (ARE) and the differential Riccati equation (DRE), the iteration that solves them, numerical conditioning issues, Schur-vector methods, when iteration fails to converge and what to do about it. Live: Riccati iteration with adjustable initial condition.

**Ch. 07 — LQG and Kalman.** Adding noise: process noise in the dynamics, measurement noise in the output. The Kalman filter as the dual of LQR. The separation principle (when it holds, when it doesn't, what "doesn't" looks like in practice). LQG as the controller you get by stacking LQR and Kalman.

**Ch. 08 — MPC.** Receding horizon control in practice. The QP that runs every sample. Horizon length as a stability-vs-compute trade-off. Terminal costs and terminal sets. Soft and hard constraints. Warm starting. Stability proofs (Mayne et al.). And — this is the chapter that took me the longest — the practical bits: solver choice, fast gradient vs interior point, real-time MPC and the explicit-MPC alternative. Interactive: MPC horizon and constraint tightness vs closed-loop performance.

**Ch. 09 — Nonlinear methods.** When the dynamics are nonlinear and LQR's linearization isn't enough. iLQR (iterative LQR), DDP (differential dynamic programming), direct collocation, SQP. The trade-offs between solving the full nonlinear problem and approximating it. Convergence behavior.

**Ch. 10 — Embedded considerations.** The chapter that maps to the real problem you'll face: optimal control on an automotive-grade MCU with 100 μs per sample and fixed-point arithmetic. Discretization choice, numerical conditioning, scaling, fixed-point Q-format selection, real-time solver determinism, what to do when the solver exceeds its time budget.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/optimal-control-field-guide.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

The guide lives at its own URL with a dark editorial layout — amber accent, Fraunces display, JetBrains Mono for math and code. The four interactive simulations run live in the browser.

---

← Back to [Autonomy]({{ '/' | relative_url }})
