---
title: "Point-Cloud Surrogates for Aerodynamics: DoMINO"
subtitle: "How a network reads a car's shape as a cloud of points and predicts the pressure and airflow around it — one query point at a time."
date: 2026-07-06 11:10:00 -0400
category: "Machine Learning"
slug: point-cloud-surrogates-domino
excerpt: "How DoMINO (NVIDIA's Decomposable Multi-scale Iterative Neural Operator) predicts aerodynamics directly from a car's STL/point cloud. It encodes the whole geometry into a global multi-scale latent, then for any query point — on the surface or out in the air — extracts a local geometry representation and a dynamically-built computational stencil, and an aggregation network fuses global shape context with local flow into surface pressure, wall shear stress, and volume velocity/pressure. Because each point is solved locally against a shared global context, it is mesh-free and scales. Block diagram, per-point flowchart, practical notes, references, and the GM SUV validation. Part of a three-post set on CFD geometry surrogates."
reading_time: 13
---

A plain-words guide to DoMINO, NVIDIA's Decomposable Multi-scale Iterative Neural Operator. It encodes a car's whole shape into a global multi-scale latent, then for any query point extracts a local neighborhood and dynamic stencil and aggregates them into a high-fidelity flow prediction — mesh-free and scalable.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/point-cloud-surrogates-domino.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL in the warm-paper layout, with block diagrams, a flowchart, practical notes, and references in plain words. It cross-links to the other two geometry-surrogate posts and the [PhysicsNeMo field guide]({{ '/posts/physicsnemo-vehicle-field-guide/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
