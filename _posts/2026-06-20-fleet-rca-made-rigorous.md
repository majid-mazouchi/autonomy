---
title: "Fleet RCA, Made Rigorous: Significance, Surveillance, and Closing the Loop"
subtitle: "The numbers under the fleet method — is the split real, did you fool yourself by looking everywhere, can you catch the next one early, and did the fix actually work?"
date: 2026-04-11 22:00:00 -0400
category: "Control Systems"
slug: fleet-rca-made-rigorous
excerpt: "The rigorous companion to Fleet-Scale Root-Cause Analysis. That post showed the logic; this one puts numbers under the figures and closes the gaps. We make 'is this cohort split real?' a calculation — confidence intervals on prevalence, a chi-square test, and the Mantel–Haenszel stratified rate — and then name the trap that voids it: scanning many attributes for the best split manufactures false positives, fixed by Bonferroni/FDR and honest power. We move from reactive to proactive with control charts and CUSUM that catch a forming cluster at fifty cars instead of five thousand; handle boundaries that are gradients rather than crisp rules with logistic risk-scoring and interactions; pick the number of clusters honestly with BIC; turn the light forecast into a real one with Weibull hazards, censoring, and B10 life; quantify the remediation decision as prevented-loss vs campaign-cost against a mandatory-recall threshold; verify the fix by watching prevalence bend after the campaign; and catch phantom fleet patterns where a bad software update lights one code fleet-wide with no real fault. Plain words, worked numbers, figures, algorithms, practical notes, and references."
reading_time: 24
---

This is the rigorous follow-up to [Fleet-Scale Root-Cause Analysis]({{ '/posts/fleet-scale-root-cause-analysis/' | relative_url }}). That post built the *logic* of diagnosing a population — de-mix the mixture, let the cohort boundary name the cause, decide a campaign. But its rates and splits were illustrative round numbers, and it left several honest questions unanswered. This post answers them, with numbers you can reproduce.

Four questions drive it. **Is the split real**, or could that clean-looking cohort boundary be noise? **Did I fool myself** by scanning a dozen attributes until one looked significant? **Can I catch the next cluster early**, while it is fifty cars instead of five thousand? And **did the fix actually work** once the campaign shipped? Along the way we sharpen the soft spots — how many clusters there really are, what to do when the boundary is a gradient rather than a crisp rule, how to turn a hand-wavy forecast into a real survival curve, and how to avoid the most embarrassing fleet mistake of all: launching a recall against a fault that never existed.

We keep the running scenario from the previous post — a fleet of 6,000 EVs throwing one charging code, hiding two causes.

## What it covers

Twelve sections, about twenty-four minutes, in plain language with the arithmetic shown.

**Part A · Is it real?**

**§ 2 — Is the split real?** Confidence intervals on prevalence, a chi-square test for a cohort split, and the Mantel–Haenszel stratified rate — worked out on the numbers.

**§ 3 — The multiple-comparisons trap.** Why scanning many attributes for the best split manufactures false positives, and how Bonferroni/FDR and honest power close it.

**Part B · Better structure**

**§ 4 — How many clusters, really?** Choosing the number of sub-populations with BIC, soft assignment, and a noise tail — instead of splitting by eye.

**§ 5 — When the boundary is a gradient.** Logistic risk-scoring when risk rises smoothly, and interactions when two factors are only harmful together.

**Part C · From snapshot to stream**

**§ 6 — Catch it early.** Control charts and CUSUM on emerging code rates — the live-monitoring complement to the onset curve.

**§ 7 — A real forecast.** Weibull hazards, censoring, infant-mortality vs. wear-out, and B10 life — making the projection mean something.

**Part D · Decide and close the loop**

**§ 8 — The remediation decision, quantified.** Prevented-loss vs. campaign-cost, urgency from the forecast slope, and the mandatory-recall threshold.

**§ 9 — Verify the fix.** Watching prevalence bend down after the campaign — the fleet-scale kill-switch.

**§ 10 — Phantom fleet patterns.** When a bad over-the-air update lights one code fleet-wide with no real fault — the lying sensor, scaled to a population.

**§ 11 — Practical notes.** Field rules for rigorous fleet diagnosis.

**§ 12 — References & further reading.** Statistics, reliability, and surveillance, with pointers.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/fleet-rca-made-rigorous.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL in the warm-paper layout of the series, with worked confidence-interval and chi-square boxes, a multiple-comparisons figure, a BIC curve, a CUSUM surveillance chart, a Weibull hazard (bathtub) curve, a remediation cost-decision figure, a before/after verification curve, a phantom-vs-real panel, three algorithms, practical notes, and references.

## Where it sits

The diagnosis series, in order:

**I · The core method**

1. [Root-Cause Analysis Under Uncertain, Heterogeneous Evidence]({{ '/posts/rca-under-uncertain-heterogeneous-evidence/' | relative_url }})
2. [When Is the Evidence Enough?]({{ '/posts/evidence-sufficiency-and-conflict/' | relative_url }})
3. [Harder Cases in Diagnosis]({{ '/posts/harder-cases-in-diagnosis/' | relative_url }})

**II · At fleet scale**

4. [Fleet-Scale Root-Cause Analysis]({{ '/posts/fleet-scale-root-cause-analysis/' | relative_url }})
5. **Fleet RCA, Made Rigorous** — *(this post)*

**III · Proof, foundations & prevention**

6. [Proving Cause with Experiments]({{ '/posts/proving-cause-with-experiments/' | relative_url }})
7. [Diagnosis on the Vehicle]({{ '/posts/diagnosis-on-the-vehicle/' | relative_url }})
8. [The Data Plumbing Behind Fleet Diagnosis]({{ '/posts/data-plumbing-fleet-diagnosis/' | relative_url }})
9. [From Root Cause to No Cause]({{ '/posts/prevention-and-corrective-action/' | relative_url }})

Full map: [The Diagnosis Series index]({{ '/posts/diagnosis-series/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
