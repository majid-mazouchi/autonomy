---
title: "When Is the Evidence Enough? Sufficiency and Conflict in Diagnosis"
subtitle: "How to tell whether your measurements can actually reach a conclusion — and what to do when they can't, or when they disagree with each other."
date: 2026-04-11 16:00:00 -0400
category: "Control Systems"
slug: evidence-sufficiency-and-conflict
excerpt: "The companion to Root-Cause Analysis Under Uncertain, Heterogeneous Evidence. That post showed how to weigh messy evidence into a cause; this one answers the question it left open — how do you know you have enough to conclude at all? The key idea, in plain words: sufficiency is not about how much data you have, it is about whether your data can tell your hypotheses apart. We build a sufficiency gate (discrimination, margin, coverage, robustness), show how to pick the single most useful next measurement using value of information, and handle the case everyone dreads — two trusted sources that flatly contradict each other. With a worked EV 'reduced power' example, eight figures and flowcharts, two algorithms, practical field notes, and references."
reading_time: 28
---

This is the direct sequel to [Root-Cause Analysis Under Uncertain, Heterogeneous Evidence]({{ '/posts/rca-under-uncertain-heterogeneous-evidence/' | relative_url }}). That monograph showed how to turn a messy pile of clues into a single cause. But it assumed something it never checked: that the pile was *good enough* to reach a verdict at all. Often it isn't. The measurements may not be rich enough to separate two explanations, or two sources you trust may point in opposite directions.

This post is about that gap. The central idea is simple and worth saying once in plain words: **having more data is not the same as having enough data.** A thousand readings that look identical under two rival explanations cannot tell them apart — you are not data-poor, you are *discrimination*-poor. So the real test of sufficiency is never "do I have a lot?" but "can what I have separate these hypotheses, to the confidence this decision needs?"

From that one reframe we get a practical **sufficiency gate**, a clean way to choose the **single most useful measurement to collect next**, and a disciplined way to treat **contradiction** — not as noise to average away, but as a signal that either a trusted source is wrong or the true cause is still missing from your list.

## What it covers

Ten sections, about twenty minutes, in deliberately plain language.

**§ 1 — The wrong question.** Why "do I have enough data?" is the wrong question, and what the right one is.

**§ 2 — Sufficiency is relative.** Enough for *what*? Evidence is sufficient only against a specific hypothesis set and a confidence bar set by the cost of being wrong.

**§ 3 — The sufficiency gate.** Four checks every conclusion must pass — discrimination, margin, coverage, robustness — with the gate drawn as a block diagram and written as an algorithm.

**§ 4 — Telling hypotheses apart.** Observational equivalence in plain words ("two suspects, one alibi"), and the discriminating measurement that breaks it. The EV example begins here.

**§ 5 — Which test next?** Value of information: how to rank candidate measurements by how much they would actually shrink your uncertainty, and collect the one that helps most.

**§ 6 — Margin, coverage, robustness.** The other three checks: a big enough lead, no unexplained leftovers, and a verdict that survives losing its single best clue.

**§ 7 — When sources disagree.** Contradiction as information. Why the trust hierarchy resolves most conflicts, why a clash between two high-trust sources is a provenance bug until proven otherwise, and why "nothing fits" means a missing hypothesis.

**§ 8 — Three ways to stop.** The procedure must be allowed to end in three states — Confirmed, Inconclusive, Incoherent — shown as a flowchart, and the EV example run all the way through each.

**Part II · §§ 9–11 — The math, made concrete.** The arithmetic under the figures, all reproducible by hand: a real Bayesian update with likelihood ratios and the entropy calculation that produces the "bits" of information gain; the Sequential Probability Ratio Test (Wald) as the formal "stop when it's enough," drawn as a log-likelihood-ratio random walk between two decision thresholds; and the cost-aware stopping rule — keep collecting only while the next test's value of information beats its cost — with a value-vs-cost crossing-point figure. Two more algorithms.

**§ 12 — Practical notes.** Field-tested rules of thumb.

**§ 13 — References & further reading.** The ideas behind the method, with pointers.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/evidence-sufficiency-and-conflict.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL in the warm-paper layout of the RCA series, with a sufficiency-gate block diagram, a value-of-information chart, a three-exit flowchart, a worked EV "reduced power" example, two algorithms, and a references section.

## Where it sits

The diagnosis series, in order:

**I · The core method**

1. [Root-Cause Analysis Under Uncertain, Heterogeneous Evidence]({{ '/posts/rca-under-uncertain-heterogeneous-evidence/' | relative_url }})
2. **When Is the Evidence Enough?** — *(this post)*
3. [Harder Cases in Diagnosis]({{ '/posts/harder-cases-in-diagnosis/' | relative_url }})

**II · At fleet scale**

4. [Fleet-Scale Root-Cause Analysis]({{ '/posts/fleet-scale-root-cause-analysis/' | relative_url }})
5. [Fleet RCA, Made Rigorous]({{ '/posts/fleet-rca-made-rigorous/' | relative_url }})

**III · Proof, foundations & prevention**

6. [Proving Cause with Experiments]({{ '/posts/proving-cause-with-experiments/' | relative_url }})
7. [Diagnosis on the Vehicle]({{ '/posts/diagnosis-on-the-vehicle/' | relative_url }})
8. [The Data Plumbing Behind Fleet Diagnosis]({{ '/posts/data-plumbing-fleet-diagnosis/' | relative_url }})
9. [From Root Cause to No Cause]({{ '/posts/prevention-and-corrective-action/' | relative_url }})

Full map: [The Diagnosis Series index]({{ '/posts/diagnosis-series/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
