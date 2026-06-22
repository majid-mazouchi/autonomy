---
title: "From Root Cause to No Cause: Prevention and the Corrective-Action Loop"
subtitle: "Finding the cause is half the job. The other half is making sure it never comes back — feeding the fix into design, process, and test so the fault is engineered out."
date: 2026-04-11 23:00:00 -0400
category: "Control Systems"
slug: prevention-and-corrective-action
excerpt: "The closing note in the diagnosis series. The earlier posts found the cause; this one asks the harder question — how do you make sure it never happens again? Fixing the affected cars is containment, not victory; recurrence is the real failure. We walk the disciplined corrective-action loop (8D / CAPA and Deming's PDCA), separate the three actions people conflate — contain, correct, prevent — and then feed the confirmed cause backward: into the FMEA as a documented failure mode with a re-scored RPN, into the process control plan and its SPC charts, and into a poka-yoke that makes the failure physically impossible. We hunt the escape point — the test that should have caught it — add the missing test, and write the case into institutional memory so the next program inherits the fix. We run our two known causes, the firmware cold-throttle bug and the high-resistance connector lot, all the way through the loop. Plain words, worked steps, figures, algorithms, practical notes, and references."
reading_time: 22
---

This is the closing note in the diagnosis series. The earlier posts did the hard work of *finding* the cause — reasoning under uncertain evidence, judging when the evidence is enough, scaling to a fleet, and putting numbers under the method. This one starts where they end and asks the question that decides whether any of it mattered: **how do you make sure the fault never comes back?**

Fixing the cars that already failed is *containment* — necessary and urgent, but entirely backward-looking. It says nothing about the next firmware build, the next supplier lot, or the next program that reuses the same part. Recurrence is the real failure. The discipline that closes the gap is the **corrective-action loop**: contain the bleeding, remove the cause, *prevent* it from recurring, verify, and standardize — Ford's 8D, the broader CAPA framework, and Deming's PDCA wheel underneath them all. We feed our two confirmed causes — a firmware cold-throttle bug and a high-resistance connector lot — all the way through it, end to end.

We keep the running scenario from the rest of the series: a fleet of 6,000 EVs throwing one charging code (P0AE0), hiding two causes.

## What it covers

Eleven sections, about twenty-two minutes, in plain language with the steps worked out.

**Part A · The disciplined loop**

**§ 2 — The 8D / CAPA loop.** The eight steps from containment through root cause, corrective action, preventive action, verification, and standardization — laid out as a ratchet you cannot short-circuit, with the loop in pseudocode.

**§ 3 — Contain ≠ correct ≠ prevent.** The three actions people constantly conflate, drawn as a staircase: stop-the-bleeding, fix-this-batch, make-it-impossible — each reaching further forward in time.

**Part B · Feed the cause back into design & process**

**§ 4 — DFMEA / PFMEA updates.** Turning the confirmed cause into a documented failure mode with severity × occurrence × detection (RPN), and re-scoring so the number actually falls.

**§ 5 — Process control plans & SPC.** Charting the manufacturing parameter that caused it — the connector crimp force — so a drift trips before a single bad part exists.

**§ 6 — Poka-yoke / error-proofing.** Making the failure physically impossible: a keyed connector the wrong lot can't seat, a compile-time guard the firmware cast bug can't pass.

**Part C · Catch it earlier next time**

**§ 7 — The escape point.** Why validation missed it, and how adding the specific missing gate — a cold-charge HIL test, a unit test for the cast — closes the escape.

**§ 8 — Lessons-learned & institutional memory.** Wiring the case into a knowledge base, FMEA library, and design guidelines so the next program inherits the fix instead of re-suffering it.

**§ 9 — Worked example.** Both causes run all the way through the loop — 8D steps, FMEA updates, a poka-yoke each, the added test, the standardized guideline.

**§ 10 — Practical notes.** Field rules for closing the loop.

**§ 11 — References & further reading.** Quality engineering, reliability, and the lean tradition, with pointers.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/prevention-and-corrective-action.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL in the warm-paper layout of the series, with a flowchart of the eight-step loop, the contain/correct/prevent staircase, a before-and-after RPN figure, an SPC control chart on the cause, a before/after poka-yoke panel, an escape-point diagram, the knowledge loop, a worked example with two cause cards and a summary table, two algorithms, practical notes, and references.

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

6. [Proving Cause with Experiments]({{ '/posts/proving-cause-with-experiments/' | relative_url }})
7. [Diagnosis on the Vehicle]({{ '/posts/diagnosis-on-the-vehicle/' | relative_url }})
8. [The Data Plumbing Behind Fleet Diagnosis]({{ '/posts/data-plumbing-fleet-diagnosis/' | relative_url }})
9. **From Root Cause to No Cause** — *(this post)*

Full map: [The Diagnosis Series index]({{ '/posts/diagnosis-series/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
