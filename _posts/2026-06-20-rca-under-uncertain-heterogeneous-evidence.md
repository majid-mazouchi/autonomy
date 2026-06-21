---
title: "Root-Cause Analysis Under Uncertain, Heterogeneous Evidence"
subtitle: "A trouble code, a pile of telemetry, a few thousand lines of C, and a folder of customer complaints — none fully trustworthy. How to weigh them into one defensible cause."
date: 2026-06-20 14:00:00 -0400
category: "Control Systems"
slug: rca-under-uncertain-heterogeneous-evidence
excerpt: "The methodological companion to the five-case RCA series. Real investigations don't begin with clean synthetic data — they begin with a heap of evidence of unequal trust: a DTC and its boilerplate description, ECU source code, measurement logs, dealer and customer symptom reports, and maintenance and repair history. This monograph is the procedure for turning that heap into a root cause with a mechanism: grade every input by provenance, anchor it to one timeline and cohort, frame the question as abduction, kill the impostor correlation, let physics and code referee, fuse the surviving evidence by Bayesian weight rather than by vote, and accept a cause only on convergence — then report it with its residual uncertainty and the single test that would still overturn it."
reading_time: 32
---

The five-case [RCA series]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }}) and the [agentic framework]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}) that automates it both assume a luxury the real bay rarely affords: data clean enough to grade your own detective work. This monograph is about the other situation — the ordinary one. You have a **diagnostic trouble code** with a description that may or may not mean what it says, a few thousand lines of the **ECU's C source**, a **measurement log** of uncertain provenance, a folder of **dealer and customer symptom reports** written in plain English, and a **maintenance and repair history** that is part signal and part red herring. None of it is fully trustworthy, and each piece is untrustworthy in a *different* way.

The mistake everyone makes is to pour all of it into one pot and stir. The right procedure treats the unequal trust of the inputs as a first-class part of the method, not an afterthought. This piece lays out that procedure — eight steps — and the two layers the existing series under-specifies: **provenance grading** (knowing what each source can and cannot tell you before you use it) and **Bayesian evidence fusion** (combining sources by reliability-weighted likelihood, counting independent corroboration only, never double-counting a single cause echoed across ten complaints).

It is the natural methodological companion to [The Anatomy of a Root Cause]({{ '/posts/root-cause-analysis-battery-case-study/' | relative_url }}) (the worked battery case), [Fault Detection and Isolation]({{ '/posts/fault-detection-isolation/' | relative_url }}) (the detection layer), and the [statistical-methods series]({{ '/posts/residual-analysis/' | relative_url }}) (the techniques that turn measurements into evidence). Where those cover *technique*, this one covers *epistemics* — how to reason honestly when your evidence disagrees with itself.

## What it covers

Twelve sections, about eighteen minutes of careful reading.

**§ 1–2 — The evidence pile and the trap.** Why a real investigation is a heap of unequal sources. Why averaging them, or trusting the loudest, fails. The principle that organizes everything else: *grade before you fuse*.

**§ 3 — Provenance grading.** A trust table for the six input families — DTC, C source, telemetry, dealer/customer testimony, maintenance history, repair history — and what each can and cannot establish. The reliability weight assigned to each.

**§ 4 — Anchor to one timeline and one cohort.** Why most "clues" only become evidence once they are placed in time and population. Defining affected vs. unaffected before interpreting anything.

**§ 5 — Frame as abduction.** Hypotheses written as causal chains — root cause → mechanism → observable signature — not as correlations. If a hypothesis predicts no signature, it cannot be tested.

**§ 6 — The impostor.** Correlation that is a co-effect of the true cause. The partial-correlation gate that breaks it. Why the most convincing feature in the room is the prime suspect for being a fake.

**§ 7 — The referee.** Physics and code as the confirmers. Tracing the C path to prove the suspect logic actually executes under the recorded conditions. The simulator-of-record that must regenerate the observed signature.

**§ 8 — Fuse by weight, not by vote.** The Bayesian fusion loop: each datum updates the posterior over hypotheses, scaled by trust tier and likelihood ratio, with independence enforced so a single root cause echoed across many reports counts once.

**§ 9 — Accept on convergence.** The triangulation test. The root cause is the one mechanism that simultaneously explains the code pattern, the measurement signature, the executable path, and the population selectivity — without contradiction from the testimony.

**§ 10 — Report the mechanism with residual uncertainty.** Output is a causal chain, a confidence, and the single disconfirming test that would still overturn it — then the handoff to prognosis.

**§ 11 — Failure modes & traps.** Testimony cascades, double-counting, trusting the DTC's prose, confirming a code path that cannot execute, confound from the repair history itself.

**§ 12 — The procedure as a checklist.** The whole method on one page, runnable against any investigation.

**Part II · §§ 13–19 — The method in action.** A full worked battery case with downloadable mockup inputs — a DTC and freeze-frame, the ECU's C source carrying a signed/unsigned cold-guard bug, fleet telemetry, customer complaints, and service history. The procedure is run end to end: a master flowchart and the method as an algorithm, the evidence graded, a timeline and cohort plot, four hypothesis chains, the impostor broken by partial correlation, the bug confirmed by tracing the C path to the freeze-frame and regenerating the signature, trust-weighted fusion to a posterior, convergence on a single cause, and a remaining-useful-life forecast with and without the fix. Ten figures, two algorithms, and a downloadable input bundle.

**§§ 20–21 — Practical notes & references.** Eight field rules of thumb for working with unequal-trust evidence, and a grouped further-reading list spanning abduction, causal inference and confounding, Bayesian evidence fusion, model-based diagnosis, measurement and provenance, and root-cause-analysis practice.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/rca-under-uncertain-heterogeneous-evidence.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with the warm-paper editorial layout of the RCA series — rust accent, teal for confirmed evidence, slate for neutral text — with a provenance-grading table, evidence-fusion diagrams, the Bayesian fusion loop written out as an algorithm, and a full worked battery case (Part II) built on downloadable mockup inputs.

## Mockup inputs

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/rca-uncertain-evidence-mockup.zip' | relative_url }}" download>rca-uncertain-evidence-mockup.zip</a> — the fabricated inputs for the Part II walkthrough: <code>dtc_freeze_frame.json</code>, <code>bms_balance.c</code> (the cold-guard bug), <code>fleet_telemetry.csv</code>, <code>customer_complaints.md</code>, <code>service_history.csv</code>, and a README with the ground truth so the analysis can grade itself.</p>
</div>

## Where it sits

The diagnosis series, in order:

**I · The core method**

1. **Root-Cause Analysis Under Uncertain, Heterogeneous Evidence** — *(this post)*
2. [When Is the Evidence Enough?]({{ '/posts/evidence-sufficiency-and-conflict/' | relative_url }})
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
