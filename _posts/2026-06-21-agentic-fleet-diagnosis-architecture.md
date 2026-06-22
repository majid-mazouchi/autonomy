---
title: "From Method to Product: Architecting an Agentic Fleet-Diagnosis System"
subtitle: "Nine posts built the method. This one turns it into software — a multi-agent system, with tools, memory, and humans in the loop, that diagnoses a fleet at scale without inventing its answers."
date: 2026-04-11 10:00:00 -0400
category: "Control Systems"
slug: agentic-fleet-diagnosis-architecture
excerpt: "The engineering capstone of the diagnosis series. A method is something a person follows; a product is software that runs that method at fleet scale, every day, on live data — and must be trusted under audit. This post lays out the architecture of such a tool in plain words: seven planes (data, detection, reasoning, tools, memory, runtime, human-in-the-loop) wired together by one rule — agents fetch and propose, deterministic tools verify, humans commit. We walk the always-on detection layer that turns a firehose into a ranked queue of cases; the multi-agent reasoning engine (an orchestrator over typed worker agents on a shared blackboard, not a free-form swarm); MCP-first tools with read free and write gated; five kinds of memory and the write-governance that keeps the system from poisoning itself; and the parts demos skip — evals on synthetic ground-truth fleets, guardrails, observability, cost control, multi-tenancy, and the closed loop that makes it smarter per fleet over time. With block diagrams, a diagnostic-loop flowchart, algorithms, a build path, practical notes, and references."
reading_time: 32
---

The first nine posts in this series built a *method* — how to weigh messy evidence, decide when you have enough, handle the hard cases, scale to a fleet, make it statistically honest, prove cause, push detection onto the vehicle, lay the data foundation, and prevent recurrence. A method is something a careful person follows. This post is about the next step: turning that method into a **product** — software that runs it at fleet scale, every day, on live data, for users who will stake a recall on its answer.

That last clause is the whole design problem. A fleet-diagnosis tool can trigger an over-the-air update to millions of cars, a warranty reserve, or a recall. Its output carries legal and safety weight, so the architecture is not "an LLM with some tools" — it is **a system that produces a defensible, reproducible verdict with a human on the hook for it**. Everything below follows from that.

The post is deliberately plain-spoken and practical. It is the natural companion to the single-investigation [agentic RCA framework]({{ '/posts/agentic-rca-prognostics-framework/' | relative_url }}) — that post drew the team of agents for one case; this one builds the whole product around them, at scale.

## What it covers

Eighteen sections, about thirty-two minutes, in plain language with block diagrams.

**§ 1 — From a method to a machine.** Why "trust under audit" is the rule that shapes everything, and the five principles that fall out of it.

**Part A · The planes**

**§ 2 — The whole thing in one diagram.** The seven planes and how they stack.

**§ 3 — The data plane.** From a firehose of telemetry to one clean, joined, trustworthy table.

**§ 4 — The detection plane.** Always-on, cheap monitors that turn the firehose into a ranked queue of *cases* — so the expensive agents run per case, not per datapoint.

**Part B · The reasoning engine**

**§ 5 — The agent team (not a swarm).** An orchestrator over typed worker agents on a shared blackboard, run on durable workflows.

**§ 6 — The diagnostic loop.** The whole investigation as one flowchart, with the human gates.

**§ 7 — Tools, MCP-first.** Reads free, writes gated, and the deterministic referee that stops the model inventing numbers.

**§ 8 — Memory: five kinds.** Working, episodic, semantic, procedural, long-term — and the write-governance that keeps the system from poisoning itself.

**Part C · Making it a product**

**§ 9 — Runtime &amp; cost.** Durable workflows, a budget governor, and model routing.

**§ 10 — Trust.** The hardest subsystem: evals on synthetic ground-truth fleets, guardrails, observability, and audit.

**§ 11 — The closed loop &amp; scale.** Confirmed cases feeding back, plus multi-tenancy and compliance.

**§ 12 — A build path.** MVP to product in three phases, and the risks to design against.

**Part D · From diagram to buildable**

**§ 13 — Watch one case run.** The whole system on the `P0AE0` charging code, as a swimlane: detection → orchestrator → agents → tools → human → act → verify.

**§ 14 — A reference stack.** What to buy and what to build, plane by plane.

**§ 15 — The cost model.** Back-of-envelope numbers for a million-car fleet, and why the bill stays small.

**§ 16 — Measuring it.** The eval harness in depth — synthetic ground-truth fleets, the metrics that matter (including the all-important false-recall rate), and the CI gate.

**§ 17 — Practical notes.** Field rules for building the system.

**§ 18 — References &amp; further reading.** Agents, data systems, and ML-in-production, with pointers.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/agentic-fleet-diagnosis-architecture.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL in the warm-paper layout of the series, with a master layered-architecture block diagram, data-plane and detection-plane pipelines, the agent-topology diagram, a diagnostic-loop flowchart, a memory diagram, the closed-loop figure, three algorithms, a build path, practical notes, and references.

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
9. [From Root Cause to No Cause]({{ '/posts/prevention-and-corrective-action/' | relative_url }})

**IV · Build the system**

10. **From Method to Product: Architecting an Agentic Fleet-Diagnosis System** — *(this post)*

Full map: [The Diagnosis Series index]({{ '/posts/diagnosis-series/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
