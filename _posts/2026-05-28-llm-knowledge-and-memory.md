---
title: "Knowledge & Memory in Large Language Models"
subtitle: "The full account: the kinds of knowledge a model draws on, the kinds of memory it operates over, how they trade off, how an agent fuses them through a knowledge graph — and the engineering, failure modes, and governance that make it work in production."
date: 2026-05-28 10:00:00 -0400
category: "Tools"
slug: llm-knowledge-and-memory
excerpt: "There are two different questions you can ask of any LLM-powered system: where did this answer come from, and how long will the model remember it. The first is about knowledge — parametric, retrieval, tools, fine-tunes. The second is about memory — context window, episodic, semantic, procedural. They are constantly confused, and the confusion is expensive in production. This expanded field guide separates them carefully, maps the trade-offs, and walks through the agentic diagnosis loop end-to-end on a concrete EV traction-drive example."
reading_time: 35
---

There are two questions worth asking about any LLM-powered system, and they are almost always confused with each other.

The first is *where does this answer come from*. The training data baked into the model's weights, the documents it just retrieved from a vector database, the result of a tool it just called, the fine-tune it inherited last week — each of these is a different source of knowledge, with different update cadence, different cost profile, and different failure modes. Confusing them produces production bugs that are extremely hard to triage.

The second is *how long will the model remember it*. The current conversation lives in the context window and disappears when the window scrolls. Episodic memory persists across sessions but is summarized and lossy. Semantic memory is the index of facts the agent has learned. Procedural memory is the skills it knows how to apply. These trade off completely differently from each other, and the engineering of each one is its own discipline.

This field guide is the expanded version — the one that lays out both axes clearly, draws the four-quadrant map you actually need to make production decisions, and grounds it all in a single worked example: an EV traction-drive engineer trying to root-cause a current oscillation. The agent in that example threads through every knowledge source and every memory type, fusing them via a knowledge graph, and the failure mode at each step is named explicitly.

## What it covers

Two parts, fourteen sections, about thirty-five minutes.

**Part One — The Taxonomy.** What knowledge and memory actually are, and how to tell them apart.

- **§ 01 — The two questions.** Where the answer came from versus how long it'll be remembered. Why confusing them is the #1 production-bug source.
- **§ 02 — Types of knowledge sources.** Parametric (baked into weights), retrieval (vector DB, knowledge graph), tools (live API calls), fine-tune (a more recent parametric update), context (whatever's in the current prompt).
- **§ 03 — Sources at a glance.** A side-by-side table: update cadence, latency, cost, verifiability, recency.
- **§ 04 — Types of memory.** Context window (immediate), episodic (per-session, persisted), semantic (cross-session facts), procedural (skills and routines).
- **§ 05 — Memory at a glance.** Side-by-side table of the four types.

**Part Two — The Agentic Loop.** Putting the two taxonomies together to design real systems.

- **§ 06 — The map: origin × retention.** The four-quadrant diagram. Parametric × procedural is "instincts." Retrieval × episodic is "what we discussed yesterday." Tool × context is "the live API call I just made." The diagonal that matters.
- **§ 07 — Benefits, head to head.** Which combination wins for which scenario.
- **§ 08 — Which store? — decide.** The decision flowchart that engineers actually use.
- **§ 09 — The agentic diagnosis loop.** Worked example. An EV engineer reports a current oscillation on a traction inverter. The agent pulls from semantic memory (known oscillation patterns), retrieval (the inverter's recent logs), tools (live BMS state), and context (this conversation's prior turns). The flow is drawn step by step.
- **§ 10 — Skills: the procedural memory.** How procedural memory works — the "skills" pattern of progressive disclosure. Cross-references the companion "Skills in AI Agents" post.
- **§ 11 — Merging sources into knowledge.** When the model has three different answers to the same question (parametric says X, retrieval says Y, the tool says Z), how to fuse them honestly. Confidence weighting, recency bias, source attribution.
- **§ 12 — The knowledge graph as glue.** Why a knowledge graph is the right substrate for cross-source fusion. Entity resolution, relation typing, the role of grounding.
- **§ 13 — Engineering and failure modes.** What goes wrong in production. Stale embeddings. Tool-call ordering bugs. Episodic summaries that drop the wrong details. Knowledge-graph drift.
- **§ 14 — Governance.** Provenance, attribution, retention policy. The compliance questions you'll be asked sooner than you think.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/llm-knowledge-and-memory.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the expanded edition →
  </a>
</div>

The expanded edition lives at its own URL with a warm-paper editorial layout — rust accent, Newsreader display, IBM Plex Mono. Threaded throughout by the EV traction-drive diagnosis example, so the taxonomy is grounded in a concrete engineering problem instead of floating abstractly.

---

← Back to [Autonomy]({{ '/' | relative_url }})
