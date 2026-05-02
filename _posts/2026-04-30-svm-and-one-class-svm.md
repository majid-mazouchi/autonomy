---
title: "Support Vector Machines and Their One-Class Cousin"
subtitle: "Find the widest possible gap between two groups. Use a trick to make the gap curved. Then turn the same machinery inside-out, and you have an anomaly detector."
date: 2026-04-30 12:00:00 -0400
category: "Machine Learning"
slug: svm-and-one-class-svm
excerpt: "An illustrated essay on support vector machines and their one-class variant — the maximum-margin hyperplane, soft margins, the kernel trick, and the surprising move that turns a binary classifier into an anomaly detector."
reading_time: 4
---

There are a handful of ideas in classical machine learning that pay rent forever — the methods you reach for when the data is small, when the model needs to be honest about uncertainty, or when an interpretable decision boundary matters more than another point of accuracy. Support vector machines are one of those. The maximum-margin idea, the soft margin, the kernel trick — they all generalize to other algorithms, and once you internalize them you can read most of the rest of supervised learning more clearly.

The one-class variant is the surprise. Take the same machinery you used to separate two classes, change one constraint, and you have an anomaly detector that draws a tight envelope around your normal data and flags everything outside as suspicious. It's the same trick, applied inside-out.

## What it covers

A short illustrated essay — six chapters, four live figures, about fourteen minutes to read.

**Chapters 1–2 — The core idea.** Why "the widest possible gap" is the right objective, the maximum-margin hyperplane, and how support vectors get their name.

**Chapters 3–4 — When the data fights back.** Soft margins for non-separable data, slack variables, and the regularization parameter $C$ — what it does and how to feel its effect by sliding it in a live figure.

**Chapter 5 — The kernel trick.** Lifting points into higher-dimensional space without ever computing the lifted coordinates. How an RBF kernel lets a linear classifier learn arbitrarily curved boundaries, with figures comparing linear, polynomial, and RBF on the same dataset.

**Chapter 6 — The one-class twist.** Schölkopf's reformulation that turns the SVM into a density-support estimator. Why it shows up in fault detection, intrusion detection, and any place where you have lots of "normal" examples and almost no labeled anomalies.

Every chapter has an interactive figure where you can drag points, change parameters, and watch the boundary respond. The whole thing runs in your browser with no dependencies.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/svm-and-one-class-svm.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with its own visual identity — a wheat-colored paper, an EB Garamond body, and a palette of warm reds, deep greens, and ochre for the class boundaries. It's intentionally designed as a standalone artifact, so this post is mostly a pointer. Hit the button above and enjoy.

---

← Back to [Autonomy]({{ '/' | relative_url }})
