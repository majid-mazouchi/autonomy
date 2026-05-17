---
title: "The State-Space Notebook — Controllability, Observability, Observers, and Kalman Filters"
subtitle: "Five chapters on the structural properties of linear dynamical systems — from algebraic reachability tests through to the stochastic machinery Kálmán gave us in 1960."
date: 2026-05-01 10:00:00 -0400
category: "Control Systems"
slug: state-space-notebook
excerpt: "An interactive notebook on the structural properties of linear state-space systems — controllability, observability, the Kalman decomposition, Luenberger observers, and Kalman filters — with live LaTeX rendering and live trajectories you can perturb."
reading_time: 12
---

There's a clean division in classical control between *what you can do to a system* and *what you can learn about it*. Controllability says you can drive any state to any other. Observability says you can infer the entire internal state from outputs alone. Both are algebraic properties — questions you can answer with rank tests on small matrices. And from those two properties cascade everything that matters about how you can design controllers and estimators for the system.

This notebook walks through the structural properties end-to-end. It starts with the reachability tests, gets to the Kalman decomposition (which tells you exactly which parts of a system are controllable, observable, both, or neither), then builds Luenberger observers, then finishes with the Kalman filter — the stochastic-optimal observer that won Kálmán a National Medal of Science and reshaped half the engineering disciplines.

## What it covers

Five chapters, live LaTeX rendering, interactive plots in every section, about thirty minutes to read carefully.

**Chapter 1 — Controllability.** *Can you get there from here?* The controllability matrix, rank conditions, Popov-Belevitch-Hautus, and the practical question of how much control authority you have. With a live linear-system simulator where you can change A and B matrices and watch reachability change.

**Chapter 2 — Observability.** *What can you infer from what you measure?* The observability Gramian, duality with controllability, and why some states are visible from outputs while others remain forever hidden.

**Chapter 3 — Partial observability and the Kalman decomposition.** What happens when only *part* of a system is controllable or observable. The four-way decomposition into reachable/unreachable × observable/unobservable subspaces, and what each cell means for designing controllers and observers.

**Chapter 4 — The Luenberger observer.** A deterministic state estimator. How to design observer gain L by eigenvalue placement, the separation principle that lets you design controller and observer independently, and the practical guidance on how fast to make observer poles.

**Chapter 5 — The Kalman filter.** Optimality under Gaussian noise. The Riccati equation, the prediction-correction structure, and a live simulator where you can tune Q and R and watch the estimator's covariance ellipse breathe in response.

Notation: $\dot{x} = Ax + Bu,\ y = Cx$ throughout. Prerequisites: linear algebra (eigenvalues, rank, similarity transforms) and basic ODEs.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/state-space-notebook.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the notebook →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
