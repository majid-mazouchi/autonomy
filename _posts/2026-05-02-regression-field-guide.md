---
title: "A Field Guide to Regression"
subtitle: "What regression is, what it isn't, which algorithm to reach for, how much data you really need, and what to do when your labels are wildly imbalanced."
date: 2026-05-02 12:00:00 -0400
category: "Machine Learning"
slug: regression-field-guide
excerpt: "An interactive reference on regression — predicting continuous numbers from data. Nine algorithm families compared, four live demos, and an honest treatment of the data and metrics questions that surround them."
reading_time: 5
---

Regression is one of those words that means something more specific than it sounds. In casual usage it gets stretched to cover anything where a model produces a number — yet every quarter someone in a meeting describes a "regression problem" that is actually a binary classification problem, because the workhorse algorithm for *that* job is called *logistic regression* and the names get tangled.

This field guide is my attempt to lay out the actual landscape — what regression is, when it's the right hammer, and which of the dozen-or-so regression algorithms you'd reach for when. There's also a primer chapter at the start that addresses the most common confusion (the 98%/2% imbalance question is almost always classification, not regression — and I explain why) before the real material starts.

## What it covers

Seven sections, four interactive demos, about twenty minutes to read.

**01 — Primer.** The regression / classification distinction, framed cleanly enough that you'll never re-confuse them. Why "logistic regression" sits on the classification side despite the name.

**02 — Types.** Linear, polynomial, regularized (ridge / lasso / elastic net), kernel-based, tree-based, neural. The mental map of where each one lives in algorithm space.

**03 — Algorithms.** Nine families compared side-by-side, with the assumptions each one makes, the data scale each one prefers, and the failure modes that ate someone's weekend.

**04 — Data.** How much data you actually need (it's less than people think for low-dimensional problems and *much* more than people think for high-dimensional ones), and what to do when you don't have enough.

**05 — Imbalance.** What imbalance means in a regression context (it doesn't show up the way it does in classification), and the techniques that actually help — quantile regression, weighted MSE, Tweedie loss for the right kinds of skew.

**06 — Metrics.** RMSE, MAE, MAPE, R², and the silent failures of each one. When to report which, and which to optimize against during training.

**07 — Decide.** A decision tree for picking among them, organized by what you actually know about your problem upfront.

Every algorithm has worked examples and four chapters have live demos you can poke at — slide hyperparameters, watch the fit respond, see how badly things break under noise.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/regression-field-guide.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

The field guide lives at its own URL with its own visual identity — a sticky topbar, a Fraunces display face, and a burnt-orange palette close enough to Autonomy's that the visual jump is small. It's intentionally designed as a standalone artifact, so this post is mostly a pointer. Hit the button above and enjoy.

---

← Back to [Autonomy]({{ '/' | relative_url }})
