---
title: "The Production Playbook for AI Agents — Volume II"
subtitle: "Volume I explained why agent systems fail. This volume is the build manual: the nine engineering disciplines that separate a demo from a production system."
date: 2026-06-06 19:00:00 -0400
category: "Tools"
slug: production-playbook
excerpt: "Volume I established the problem — cascading errors, super-agent bottleneck, missing verification. Volume II is the build manual: context engineering, tool surface design, orchestration patterns, observability, reliability tactics, security, evaluation, the pre-launch gate, and the ops cadence after launch. Nine disciplines, in simple words, with practical notes."
reading_time: 20
---

This is the companion piece to [Scaling Agentic AI]({{ '/posts/scaling-agentic-ai/' | relative_url }}) — if Volume I diagnosed the disease, this is the prescription. The nine engineering disciplines that separate a demo agent from one that survives in production, written as a build manual rather than a survey: each section identifies the discipline, explains the failure mode it addresses, and gives the practical pattern that works. Together with Volume I, the two-part series is meant to be the document I wish someone had handed me before I shipped my first agent system.

## What it covers

Nine disciplines, about twenty minutes of reading.

**§ 1 — Context engineering.** What goes in the prompt, in what order, with what compression. The single most important production discipline.

**§ 2 — Tool surface design.** Why the function signature you expose matters more than the model you call. Typed tools, parameter constraints, return-value discipline.

**§ 3 — Orchestration patterns.** Sequential pipeline, supervisor-worker, parallel fan-out, hierarchical. When each one is the right shape.

**§ 4 — Observability.** Tracing, logging, replay. Why you cannot debug what you cannot inspect.

**§ 5 — Reliability tactics.** Retries with exponential backoff, idempotent tool calls, deterministic checkpoints, the verify-then-commit pattern.

**§ 6 — Security & guardrails.** The threat model. Prompt injection. Excessive tool capability. The principle-of-least-privilege applied to LLM tool surfaces.

**§ 7 — Evaluation.** Building a real eval set. The metrics that matter (task success rate, time-to-success, cost-per-success) versus the ones that don't (token counts, model parameter counts).

**§ 8 — The pre-launch gate.** The checklist before you ship. Five tests that catch most of what goes wrong.

**§ 9 — Ops after launch.** The cadence. Daily review of failures. Weekly eval-set updates. Monthly model-and-tool refresh. The maintenance discipline that turns a working system into a *staying-working* system.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/production-playbook.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open Volume II →
  </a>
</div>

The playbook lives at its own URL with a warm-paper editorial layout — signal-orange agent accent, teal verification accent throughout. Volume II of the [Scaling Agentic AI]({{ '/posts/scaling-agentic-ai/' | relative_url }}) series.

---

← Back to [Autonomy]({{ '/' | relative_url }})
