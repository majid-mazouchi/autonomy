---
title: "Convolutional Mesh Solvers: FIGConvUNet"
subtitle: "How to run a convolutional network over a million-point car mesh without paying the cubic price — by folding 3D into stacks of 2D."
date: 2026-07-06 11:00:00 -0400
category: "Machine Learning"
slug: convolutional-mesh-solvers-figconvunet
excerpt: "Why a plain 3D convnet on a car mesh is cubic (O(N^3)) and infeasible at high resolution, and how FIGConvUNet gets a global receptive field at quadratic (O(N^2)) cost: factorized implicit grids approximate the fine 3D domain, a 2D reparameterization runs cheap 2D convolutions that still reach across the whole shape, and a U-Net gathers detail across scales. On DrivAerNet it reaches R^2 = 0.95 for drag, a 40%/70% relative/absolute MSE improvement over prior state of the art, validated from the Ahmed body (~100k points) to DrivAerNet (~1M points). Block diagram, a 3D-into-2D flowchart, a comparison with DoMINO and Transolver, notes, and references. Part of a three-post set on CFD geometry surrogates."
reading_time: 11
---

A plain-words guide to FIGConvUNet — NVIDIA's Factorized Implicit Global Convolution U-Net. It approximates a high-resolution 3D domain with factorized implicit grids and runs global convolutions by re-expressing the 3D grid as stacks of cheap 2D planes, dropping the cost from cubic to quadratic.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/convolutional-mesh-solvers-figconvunet.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL in the warm-paper layout, with block diagrams, a flowchart, practical notes, and references in plain words. It cross-links to the other two geometry-surrogate posts and the [PhysicsNeMo field guide]({{ '/posts/physicsnemo-vehicle-field-guide/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
