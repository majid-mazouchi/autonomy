---
title: "Harder Cases in Diagnosis: Multiple Faults, Intermittent Events, and Lying Sensors"
subtitle: "Three comfortable assumptions every diagnosis quietly makes — one cause, a fault that stays put, sensors that tell the truth — and what to do when each one breaks."
date: 2026-06-20 18:00:00 -0400
category: "Control Systems"
slug: harder-cases-in-diagnosis
excerpt: "The third post in the diagnosis set. The sufficiency method assumed away three hard realities, and this post tackles them head-on, in plain words. Multiple simultaneous faults: when two things are wrong at once, their symptoms add up, no single cause fits, and the leftover you can't explain is the tell — you must reason about combinations, not suspects. Intermittent faults and operating-condition coverage: 'rich enough' is not about how many readings you have but whether you captured the fault under the condition that triggers it; you don't have enough data until you've seen the event in the right corner of the operating envelope. Sensors that lie: sometimes the contradiction isn't in the system, it's in the instrument — is the gauge broken? — and the fix is redundancy, plausibility checks, and parity. With worked EV examples, figures, block diagrams, flowcharts, algorithms, practical notes, and references."
reading_time: 22
---

This is the third post in a set on disciplined diagnosis, after [Root-Cause Analysis Under Uncertain, Heterogeneous Evidence]({{ '/posts/rca-under-uncertain-heterogeneous-evidence/' | relative_url }}) and [When Is the Evidence Enough?]({{ '/posts/evidence-sufficiency-and-conflict/' | relative_url }}). Those built a method for weighing messy evidence and deciding when you have enough of it. To keep that method clean, they leaned on three assumptions — and real systems break all three.

The assumptions are easy to miss because they feel like common sense: that there is **one** fault to find, that the fault **stays put** long enough to measure, and that your **sensors tell the truth**. Drop any one and the picture changes. Two faults at once produce a symptom pattern that matches *neither* alone. An intermittent fault hides between your snapshots, so more data of the wrong kind never helps. And a lying sensor turns a healthy system into a phantom fault — or hides a real one.

This post takes the three cases one at a time, in deliberately simple language, and shows how each folds back into the sufficiency method rather than replacing it.

## What it covers

Nine sections, about twenty-two minutes.

**§ 1 — Three assumptions.** The comfortable defaults, and the symptom that each failure leaves behind.

**Part A · Multiple simultaneous faults**

**§ 2 — Symptoms add up.** Why two faults look like neither, and why the *unexplained leftover* (the coverage check from the prequel) is your early warning.

**§ 3 — Reasoning about combinations.** Generating candidate explanations from conflicts, minimal diagnoses and the parsimony trap, and taming the combinatorial blow-up — with a worked example.

**Part B · Intermittent faults & operating-condition coverage**

**§ 4 — Richness is coverage, not count.** The operating envelope, why a thousand idle logs can't diagnose a fault that only appears on a hot uphill, and capturing the event.

**§ 5 — Getting the data you actually need.** Condition-coverage checks and targeted collection — driving the system to the corner where the fault lives.

**Part C · Sensors that lie**

**§ 6 — Is the gauge broken?** Telling a sensor fault from a system fault: hardware and analytical redundancy, plausibility limits, and parity/voting.

**§ 7 — The augmented procedure.** A single flowchart folding all three cases back into the sufficiency gate.

**§ 8 — Practical notes.** Rules of thumb for the hard cases.

**§ 9 — References & further reading.** Model-based diagnosis and fault detection, with pointers.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/harder-cases-in-diagnosis.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL in the warm-paper layout of the series, with symptom-superposition and operating-envelope figures, a sensor-validation block diagram, an augmented-procedure flowchart, three algorithms, worked EV examples, practical notes, and references.

## Where it sits

The diagnosis series, in order:

**I · The core method**

1. [Root-Cause Analysis Under Uncertain, Heterogeneous Evidence]({{ '/posts/rca-under-uncertain-heterogeneous-evidence/' | relative_url }})
2. [When Is the Evidence Enough?]({{ '/posts/evidence-sufficiency-and-conflict/' | relative_url }})
3. **Harder Cases in Diagnosis** — *(this post)*

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
