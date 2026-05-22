---
title: "Cox Regression and Its Neural Cousin"
subtitle: "Survival analysis from the classical proportional-hazards model through DeepSurv — how to estimate time-to-event when many of your observations never event at all."
date: 2026-04-07 10:00:00 -0400
category: "Machine Learning"
slug: cox-regression-and-deepsurv
excerpt: "An illustrated primer on survival analysis. Why time-to-event data is fundamentally different from regression. Censoring, hazard functions, Cox's elegant trick, and the neural extension that handles nonlinear effects."
reading_time: 14
---

Time-to-event data is one of those structures that sits unhappily inside the regression-and-classification toolkit because it isn't really either. You're asking *when will this event happen* — when will this patient die, when will this component fail, when will this customer churn — but for a substantial fraction of your data, the event simply hasn't happened yet by the time the study ends. The observation is *censored*. You know the event hadn't happened by time t, and that's all.

A regression model that treats censored points as known event times underestimates survival. A model that throws out censored points throws out most of the data. The right answer is a methodology built specifically for this structure, which is what survival analysis is. Cox regression has been the workhorse since 1972. DeepSurv extends it with neural networks for the nonlinear part. This primer walks through both.

It's monograph № 3 in the representation/methods series.

## What it covers

Eight sections, several live figures, about fifteen minutes to read.

**§1 — Why survival data is different.** The censoring problem. Why this is a genuine statistical structure, not a quirk.

**§2 — Censoring, made visible.** Live figure showing right-censoring, left-truncation, and what each one does to a naive estimator.

**§3 — The two fundamental functions.** Survival function S(t) and hazard function h(t). Their definitions, their derivatives-of-each-other relationship, the geometric intuition.

**§4 — Hazard meets survival.** Live figure showing the integral relationship between hazard rate and survival probability.

**§5 — Cox's elegant trick.** The proportional hazards assumption. Why it lets you fit a hazard model without ever specifying the baseline. The partial likelihood that makes the whole thing identifiable.

**§6 — The proportional hazards assumption.** When it holds, when it doesn't. The Schoenfeld residual test. How to fix it (stratification, time-varying covariates) when it breaks.

**§7 — DeepSurv.** The neural extension. Replacing the linear combination of covariates with a neural network output, keeping the partial-likelihood loss. When this wins over Cox, when it doesn't.

**§8 — Concordance and other metrics.** How to evaluate survival models when "accuracy" doesn't apply. The C-index. Time-dependent AUC.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/cox-regression-and-deepsurv.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
