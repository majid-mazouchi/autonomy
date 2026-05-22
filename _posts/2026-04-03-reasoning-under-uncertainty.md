---
title: "Reasoning Under Uncertainty — Fault Trees, Bayesian Networks, and Ranked Hypotheses"
subtitle: "Three diagnostic-reasoning tools, explained in plain words, with things you can actually click on."
date: 2026-04-03 10:00:00 -0400
category: "Control Systems"
slug: reasoning-under-uncertainty
excerpt: "An interactive primer on the three classical tools of diagnostic reasoning — fault tree analysis, Bayesian network inference, and ranked hypotheses with priors. Three live figures grounded in motor and EV diagnostic examples."
reading_time: 9
---

A working diagnostic engineer has to do three different kinds of reasoning, often within the same hour. *Forward*: this component fails, what breaks downstream? *Backward*: this symptom appeared, what could have caused it? And *probabilistically*: given everything I know about how this fleet typically fails, which hypothesis is most worth pursuing first?

The three classical tools for these three questions are fault tree analysis, Bayesian networks, and ranked hypotheses with priors. They sit underneath every formal diagnostic workflow — aviation safety, medical differential diagnosis, vehicle service bays — and the engineer who can wield all three has a substantial advantage over the one who only knows one.

This primer is a hands-on introduction to all three, with live figures grounded in motor and EV diagnostic examples. It sits alongside the [four-part diagnostics monograph]({{ '/posts/fault-detection-isolation/' | relative_url }}) — those covered the *theory* of detection, isolation, control, and prognostics; this one covers the *reasoning* layer that wraps around all of them.

## What it covers

Six sections, three interactive figures, about thirty minutes to read.

**§1 — Fault trees: how systems fail.** The top-down view. Start with the failure you care about, decompose into the AND-gated and OR-gated combinations of lower-level events that could produce it. Live tree with toggleable nodes.

**§2 — Bayesian networks: updating beliefs from evidence.** The diagnostic engine. A network of conditional dependencies that you propagate evidence through to update posterior probabilities. Live two-symptom, three-cause network you can poke.

**§3 — Ranked hypotheses with priors: acting on what's likely.** The triage step. Given the population of failure modes you've seen before, rank the live hypotheses by posterior probability and act on the top one first. Includes the explicit cost-of-being-wrong calculation.

**§4 — How they fit together.** The unified workflow. Where each tool lives in a real diagnostic process.

**§5 — Practical notes and pitfalls.** Independence assumptions that bite. Prior elicitation problems. The base-rate fallacy that gets people in trouble.

**§6 — References.** Reading list — the foundational papers and books worth knowing.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/reasoning-under-uncertainty.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
