---
title: "Logic and Reasoning, Part III — A Multi-Agent Problem-Solver"
subtitle: "The shift from a single reasoner to a team of them. How a multi-agent system decomposes a hard problem, distributes the work, and reasons collectively."
date: 2026-06-14 21:00:00 -0400
category: "Tools"
slug: logic-and-reasoning-part-3
excerpt: "Part 3 of 7. Single-agent problem-solving from Part II has a ceiling. Multi-agent problem-solving — where the work is decomposed across a team of specialised reasoners — is the modern frontier. This monograph covers the architectural patterns (blackboard, contract net, market mechanisms), the coordination protocols, and the modes of collective reasoning that emerge. The bridge from a *mind* to a *society of minds*."
reading_time: 30
---

This is Part 3 of the seven-part Logic and Reasoning field guide. Parts I and II established the foundations and limits of single-agent reasoning. This part takes the obvious next step: what happens when reasoning is spread across multiple cooperating agents? The shift is consequential — many problems that are intractable for a single agent become tractable when properly decomposed, and many problems that look identical from outside are *qualitatively different* depending on whether one agent or a team is solving them.

The natural companion is the [AI Agent Teams]({{ '/posts/ai-agent-teams/' | relative_url }}) monograph, which covers the engineering side of the same shift. This post is the theory side. The two read well together.

## What it covers

About thirty minutes of careful reading.

**Why decompose.** The complexity argument. The expertise argument. The parallelism argument. When decomposition genuinely helps and when it just adds coordination overhead for no gain.

**Architectural patterns.** Blackboard systems (a shared workspace where agents post intermediate results). Contract net (auction-based work allocation). Market mechanisms (resource pricing as the coordination signal). Hierarchical patterns (manager-worker). The matrix of when each one is the right reach.

**Coordination protocols.** Synchronous versus asynchronous. The handoff disciplines. The deadlock-and-livelock failure modes and the textbook mitigations.

**Modes of collective reasoning.** Voting. Argumentation (Dung-style). Belief revision in groups. Bayesian aggregation. The handful of formal frameworks for "what does the team conclude?"

**The communication problem.** Why getting agents to agree on a vocabulary is harder than getting them to agree on conclusions. Ontologies, schemas, and the practical answer (just standardise on a shared schema and move on).

**A worked example.** A multi-agent reasoning problem (route planning with diverse constraints from different agents) solved three ways across three architectures, with the trade-offs laid bare.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/logic-and-reasoning-part-3.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open Part III →
  </a>
</div>

## The series

This is Part 3 of 7:

1. [The Foundations and the Human Mind]({{ '/posts/logic-and-reasoning-part-1/' | relative_url }})
2. [Limits, Machines, and Problem-Solving]({{ '/posts/logic-and-reasoning-part-2/' | relative_url }})
3. **A Multi-Agent Problem-Solver** — *(this post)*
4. [From a Mind to a Society of Minds]({{ '/posts/logic-and-reasoning-part-4/' | relative_url }})
5. [The Health of a Thinking System]({{ '/posts/logic-and-reasoning-part-5/' | relative_url }})
6. [The Dynamics of Thinking]({{ '/posts/logic-and-reasoning-part-6/' | relative_url }})
7. [Understanding and Comprehension]({{ '/posts/logic-and-reasoning-part-7/' | relative_url }})

---

← Back to [Autonomy]({{ '/' | relative_url }})
