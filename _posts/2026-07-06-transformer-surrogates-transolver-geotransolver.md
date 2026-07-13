---
title: "Transformer Surrogates for Physics: Transolver & GeoTransolver"
subtitle: "How a transformer predicts flow around a car in one shot — by grouping mesh points that share a physical state, then paying attention among the groups."
date: 2026-07-06 11:20:00 -0400
category: "Machine Learning"
slug: transformer-surrogates-transolver-geotransolver
excerpt: "Why plain self-attention chokes on a million-point mesh (quadratic cost), and how Transolver's Physics-Attention fixes it: softly assign each mesh point to one of a small fixed number of learnable 'slices' of physically-similar points, attend among the slice tokens, then scatter back — linear cost in the number of points. Then GeoTransolver makes it geometry-aware with GALE attention and a reused multi-scale geometry/boundary-condition context. Block diagram, a step-by-step flowchart, a comparison table, practical notes, and references. Part of a three-post set on CFD geometry surrogates."
reading_time: 13
---

A plain-words guide to transformer surrogates for physics. Transolver's Physics-Attention groups a mesh's millions of points into a small number of learnable 'slices' and attends among those — turning a quadratic cost into a linear one — and GeoTransolver makes it geometry-aware.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/transformer-surrogates-transolver-geotransolver.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL in the warm-paper layout, with block diagrams, a flowchart, practical notes, and references in plain words. It cross-links to the other two geometry-surrogate posts and the [PhysicsNeMo field guide]({{ '/posts/physicsnemo-vehicle-field-guide/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
