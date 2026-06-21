---
title: "Proving Cause with Experiments: Causal Inference and Staged Rollouts"
subtitle: "Observation suggests a cause; intervention proves it. How a staged software rollout becomes a randomized experiment — and how to settle causation when you can't randomize."
date: 2026-06-20 23:20:00 -0400
category: "Control Systems"
slug: proving-cause-with-experiments
excerpt: "The diagnosis series found a cause by watching: a charging code (P0AE0) concentrated in cars on firmware ≥ v5.1, pointing to a cold-throttle bug, and a v5.2 patch was proposed. But 'the curve bent after we shipped' is not proof — coincidence, seasonality, regression to the mean, and other concurrent changes can all bend a curve. This post climbs the ladder of evidence from observation to intervention. We show why adjust-and-watch is limited by the confounders you never measured; draw the causal graph (DAGs, simply) that says what to adjust for and what not to — the collider trap; then make the rollout interventional. A staged rollout, when the order is randomized, is a clean randomized experiment: treatment versus control, the difference a real causal effect (the do-operator, in plain words). When you can't randomize, two workhorses recover causation from luck — difference-in-differences across not-yet-updated cohorts with its parallel-trends assumption, and instrumental variables / natural experiments where assignment is as-good-as-random. We close with how to run it well — power, a safe ramp, guardrails, a stopping rule — and a worked proof that v5.2 fixes the firmware cluster. Plain words, worked numbers, figures, algorithms, practical notes, and references."
reading_time: 23
---

This is the seventh post in the diagnosis set, and the one that turns watching into proving. Every earlier post inferred a cause from evidence the fleet handed us. This one pushes on the world and measures what moves. The setup is the running scenario: a charging code (`P0AE0`) concentrated in cars on firmware ≥ v5.1, a cold-throttle bug diagnosed, and a v5.2 patch proposed. The obvious next step — ship it and watch the curve bend — is exactly the trap this post dismantles.

The problem is that a curve can bend for reasons that have nothing to do with your fix: coincidence, seasonality (this is a *cold*-charge fault, and spring arrives on its own schedule), regression to the mean, or any of the other changes shipping in the same week. The cure is to stop relying on a single before/after line and build a **comparison** — a group that lived through the same week without the change. We show how to construct that comparison cleanly when you can randomize, and cleverly when you can't.

We keep the running scenario from the previous posts — a fleet of 6,000 EVs, one charging code, a firmware cause already diagnosed and now to be *proven* fixed.

## What it covers

Ten sections, about twenty-three minutes, in plain language with the arithmetic shown.

**Part A · Why observation isn't proof**

**§ 2 — The limits of adjust-and-watch.** Confounders, and the unbeatable problem of the common cause you never measured — the ceiling of every observational study.

**§ 3 — Draw the causal graph.** DAGs, simply: nodes and arrows, the back-door path you must adjust for, and the collider trap you must *not* adjust for.

**Part B · Make it interventional**

**§ 4 — The staged rollout as a randomized experiment.** Assign v5.2 by coin flip and the staged rollout becomes a randomized controlled trial — treatment vs. control, a clean causal effect (the do-operator, in plain words).

**§ 5 — Difference-in-differences.** When you can't randomize: compare treated vs. not-yet-updated cohorts before and after, difference out the shared trend, and defend the parallel-trends assumption.

**§ 6 — Instrumental variables and natural experiments.** When luck assigns the treatment — rollout order, regional scheduling — and you borrow that as-good-as-random variation as an instrument.

**Part C · Run it well**

**§ 7 — Designing the experiment.** Sample size and power, a safe ramp (canary → 10% → 50% → 100%), guardrail metrics, and a stopping rule.

**§ 8 — Worked example.** A 10% randomized canary, treatment vs. control with a confidence interval, and a DiD cross-check against the not-yet-updated cohort — the estimated causal effect of v5.2.

**§ 9 — Practical notes.** Field rules for proving cause.

**§ 10 — References & further reading.** Causal inference, econometrics, and online controlled experiments, with pointers.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/proving-cause-with-experiments.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL in the warm-paper layout of the series, with a confounder graph, a confounder-vs-collider DAG panel, a randomized treatment/control split, a difference-in-differences two-line plot, an instrumental-variable path diagram, a ramp-with-guardrails figure, a worked confidence-interval box and DiD cross-check table, two algorithms, practical notes, and references.

## Where it sits

The diagnosis series, in order:

**I · The core method**

1. [Root-Cause Analysis Under Uncertain, Heterogeneous Evidence]({{ '/posts/rca-under-uncertain-heterogeneous-evidence/' | relative_url }})
2. [When Is the Evidence Enough?]({{ '/posts/evidence-sufficiency-and-conflict/' | relative_url }})
3. [Harder Cases in Diagnosis]({{ '/posts/harder-cases-in-diagnosis/' | relative_url }})

**II · At fleet scale**

4. [Fleet-Scale Root-Cause Analysis]({{ '/posts/fleet-scale-root-cause-analysis/' | relative_url }})
5. [Fleet RCA, Made Rigorous]({{ '/posts/fleet-rca-made-rigorous/' | relative_url }})

**III · Proof, foundations & prevention**

6. **Proving Cause with Experiments** — *(this post)*
7. [Diagnosis on the Vehicle]({{ '/posts/diagnosis-on-the-vehicle/' | relative_url }})
8. [The Data Plumbing Behind Fleet Diagnosis]({{ '/posts/data-plumbing-fleet-diagnosis/' | relative_url }})
9. [From Root Cause to No Cause]({{ '/posts/prevention-and-corrective-action/' | relative_url }})

Full map: [The Diagnosis Series index]({{ '/posts/diagnosis-series/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
