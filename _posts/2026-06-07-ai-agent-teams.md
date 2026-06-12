---
title: "Building a Team of AI Agents — A Plain-Language Monograph"
subtitle: "Why one large language model is rarely enough — roles, memory, protocols, orchestration patterns, failure modes, costs, evaluation, and governance, explained like an engineering team."
date: 2026-06-07 11:00:00 -0400
category: "Tools"
slug: ai-agent-teams
excerpt: "The expanded edition of the multi-agent-systems introduction. Where the short version sketches the territory, this monograph builds it out: the four canonical roles fleshed into a working taxonomy, the memory architecture each role needs, the inter-agent protocols (MCP, A2A) that bind them, the four orchestration patterns and when each fits, the failure modes that are unique to multi-agent systems, the cost model, the evaluation discipline, and the governance practices that keep a team of agents from becoming a team of uncontrolled actors."
reading_time: 28
---

This is the long version of [Building a Team of AI Agents — Explained Simply]({{ '/posts/ai-agent-teams-explained/' | relative_url }}). Same starting point — multi-agent systems beat super-agent monoliths in production — but worked out at the level of architectural detail an engineer actually needs to ship one. Roles fleshed into a taxonomy. Memory architecture per role. The two relevant protocols (MCP and A2A) developed. Four orchestration patterns with the decision tree. Failure modes that are unique to multi-agent systems. The cost model. The evaluation discipline that distinguishes "the team converged on an answer" from "the team converged on a confident wrong answer." Governance.

The natural companions are the [Scaling Agentic AI]({{ '/posts/scaling-agentic-ai/' | relative_url }}) / [Production Playbook]({{ '/posts/production-playbook/' | relative_url }}) series for the broader production context, the [API · CLI · MCP · ADK]({{ '/posts/api-cli-mcp-adk/' | relative_url }}) post for the protocol-layer treatment, and the [Agent Frameworks]({{ '/posts/agent-frameworks/' | relative_url }}) monograph for the framework-by-framework comparison.

## What it covers

Fourteen sections, about twenty-eight minutes of careful reading.

**§ 1 — The case for a team.** The cascading-error argument, fleshed out. The math. The honest comparison to the single-agent baseline.

**§ 2 — The four canonical roles.** Planner, Doer, Tool-user, Learner — fleshed into a working taxonomy. The responsibility of each. The interface each one exposes.

**§ 3 — Memory architecture per role.** Why each role needs a *different* kind of memory. The planner needs goals and constraints. The doer needs immediate context. The tool-user needs tool documentation. The learner needs the history of what worked and didn't. Cross-reference to [Knowledge & Memory in LLMs]({{ '/posts/llm-knowledge-and-memory/' | relative_url }}).

**§ 4 — Inter-agent protocols.** MCP for agent-to-tool communication. A2A for agent-to-agent. Why standardized protocols matter once you have more than two agents.

**§ 5 — Orchestration patterns: sequential pipeline.** The simplest. A linear handoff. When this works, when it doesn't.

**§ 6 — Orchestration patterns: supervisor-worker.** The most common in production. One agent decides what to do; specialist workers do it. The handoff discipline.

**§ 7 — Orchestration patterns: parallel fan-out.** When you can decompose a task into independent sub-tasks and run them in parallel. The merge-step risk.

**§ 8 — Orchestration patterns: hierarchical.** Teams of teams. When this is the right shape and when it's over-engineering.

**§ 9 — Failure modes unique to multi-agent.** Loops between agents (A asks B asks A). Stale information (A's plan is based on B's old output). Confidence amplification (the team agrees on a wrong answer because each agent saw the others' agreement). The fixes.

**§ 10 — Cost model.** Token cost per agent. Why a team of small agents can be cheaper than one large agent, and the cases where it isn't.

**§ 11 — Evaluation for multi-agent systems.** Why eval is harder when no single agent owns the final output. The per-role metric versus the system-level metric. The eval set that catches confidence amplification.

**§ 12 — Governance & oversight.** The human-in-the-loop placement. The audit log. The kill switch. The minimum disciplines that keep a team of agents from becoming a team of uncontrolled actors.

**§ 13 — A worked example.** A real multi-agent system traced end to end. A simple software-development workflow — planner agent decomposes a feature, doer agents implement, tester agent verifies, reviewer agent gates the merge. Real code, real failure modes, real fixes.

**§ 14 — Further reading.** The papers and write-ups that have aged well. The framework documentation that's worth reading. The handful of post-mortems from teams who have shipped multi-agent systems and written honestly about it.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/ai-agent-teams.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-paper layout — terracotta-rust accent, deep teal cross-references, ochre highlights. Fourteen sections, four role chips color-coded throughout.

---

← Back to [Autonomy]({{ '/' | relative_url }})
