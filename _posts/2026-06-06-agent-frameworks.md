---
title: "The Frameworks Behind the Agents — A Field Monograph"
subtitle: "A practical tour of LlamaIndex, AutoGen / AG2, Pydantic AI, Semantic Kernel, LangGraph and CrewAI — what they are, how they're shaped, the protocols binding them, and where the field is actually heading."
date: 2026-06-06 18:00:00 -0400
category: "Tools"
slug: agent-frameworks
excerpt: "The agent-framework landscape in 2026 is crowded enough that engineers are now confidently choosing one and being wrong about the trade-offs. Six frameworks have meaningful adoption — LlamaIndex, AutoGen / AG2, Pydantic AI, Semantic Kernel, LangGraph, CrewAI — plus two protocols (MCP and A2A) that bind them. This field monograph is the careful side-by-side tour: what each framework is shaped for, the design philosophy underneath, the worked example showing how the same task looks in each one, and the honest decision tree for which to reach for in a new project."
reading_time: 30
---

The field of agent frameworks is in the noisy phase that every infrastructure category goes through right after the foundational technology stabilizes. The LLM tool-calling API was standardized in 2023. The Model Context Protocol arrived in late 2024. By 2026 there are six frameworks with serious adoption, each one shaped by its founders' priors about what agents *should* be — opinionated, multi-agent, typed, declarative, graph-shaped, role-based — and each one solving slightly different sub-problems within the same broad space. The argument about which is "the best" is mostly an argument about which of those sub-problems matters most.

This monograph is the careful side-by-side tour. It is the natural companion to the [API · CLI · MCP · ADK]({{ '/posts/api-cli-mcp-adk/' | relative_url }}) post — that one explains the *layers* of the agent stack (where APIs end and frameworks begin and protocols sit), this one zooms into the framework layer specifically and lays the six contenders out side by side. **LlamaIndex** for retrieval-heavy systems. **AutoGen / AG2** for multi-agent conversation. **Pydantic AI** for typed, validated tool-calling. **Semantic Kernel** for Microsoft-stack integration. **LangGraph** for stateful graph orchestration. **CrewAI** for role-based crews. Plus the two protocols (**MCP** and **A2A**) that increasingly bind them.

The headline finding, which the body of the monograph defends in detail: most of these frameworks are not actually competing with each other. They're optimized for different shapes of agent system, and the right question isn't "which is best" but "which shape is my system."

## What it covers

Twelve sections, about thirty minutes of careful reading.

**§ 01 — LlamaIndex.** The framework that started as a retrieval-augmented generation library and grew into a general agent framework with retrieval as its center of gravity. What it's optimized for (anything where the agent needs to search across a corpus). The data-loaders ecosystem that's its real moat.

**§ 02 — AutoGen / AG2.** Microsoft Research's multi-agent-conversation framework, recently forked / community-renamed as AG2. Designed around the assumption that hard problems are best attacked by multiple specialized agents talking to each other. The conversation-pattern abstractions. The cases where multi-agent earns its keep and the cases where it's just expensive theater.

**§ 03 — Pydantic AI.** The youngest of the six and the one that brings the most distinctive perspective. Built by the Pydantic team on the premise that LLM tool-calling should be *typed*, *validated*, and structurally guaranteed. The tight integration with Python's type system. Why this matters for production reliability.

**§ 04 — Semantic Kernel.** Microsoft's official agent-orchestration SDK. The .NET-and-C#-first design that betrays its origins. Where it earns its keep (deep Azure integration, enterprise plug-and-play, the Microsoft 365 / Copilot story). Where it doesn't (almost everywhere outside Microsoft's stack).

**§ 05 — LangChain / LangGraph.** The framework everyone has heard of. The composition story (LangChain) and the orchestration story (LangGraph) and how they fit together. Cross-reference to the [Lang Ecosystem]({{ '/posts/lang-ecosystem/' | relative_url }}) post for the deeper treatment.

**§ 06 — CrewAI.** The role-based-agents framework. Define a *crew* of agents, each with a *role* and a *goal*; let them collaborate on tasks. The Pixar-team metaphor. Where it works (well-decomposed problems with clear specialist roles), where it doesn't (anything requiring tight feedback between roles).

**§ 07 — MCP & A2A — the binding protocols.** The standardization layer underneath the frameworks. MCP (Model Context Protocol) standardizes how tools talk to LLMs. A2A (Agent-to-Agent) standardizes how agents talk to each other. Why this layer is winning — because no framework benefits from owning the protocol it speaks.

**§ 08 — Side by side.** The comparison table. Eight rows (architecture, data model, tool surface, primary language, license, hosted option, learning curve, production maturity) by six columns. The matrix the rest of the field argues about.

**§ 09 — A worked example, six ways.** The same task — research a topic, draft a summary, fact-check the summary, output a final document — built in each of the six frameworks. The actual code (or pseudocode where the full version would be too long). The line counts. The mental overhead.

**§ 10 — Which framework, when.** The decision tree. Five questions in order. The honest version, with the (rarely-stated) observation that for many problems you don't need an agent framework at all — direct SDK calls with a tool-use loop are simpler and faster.

**§ 11 — Where the field is heading.** The two-year-out forecast. Convergence on MCP / A2A at the protocol layer. Continued framework proliferation at the orchestration layer. The likely emergence of cross-framework agent runtimes (the Kubernetes of agents, if you want the analogy). The shift toward declarative agent definition (you specify *what*, the runtime decides *how*).

**§ 12 — References & further reading.** The official documentation for each framework. The handful of independent comparisons that have aged well. The papers that the framework authors cite when they're being honest about their design choices.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/agent-frameworks.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-paper layout — six color-coded accents (one per framework), gold-on-cream chrome, sticky TOC. Twelve sections with code samples and diagrams throughout.

---

← Back to [Autonomy]({{ '/' | relative_url }})
