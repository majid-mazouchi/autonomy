---
title: "Four Ways an Agent Touches the World — API · CLI · MCP · ADK"
subtitle: "A practical monograph on the four layers of the modern agent stack — what each acronym really is, where it sits, and how an AI agent decides which to reach for. Plus Skills and A2A, rounding out the picture."
date: 2026-06-03 10:00:00 -0400
category: "Tools"
slug: api-cli-mcp-adk
excerpt: "API, CLI, MCP, ADK — four acronyms that get used as if they were rivals competing for the same job. They aren't. They live at different layers of the same stack, and the fastest way to stop confusing them is to picture the stack from the bottom up. This field guide walks through each one carefully — what it really is, where it sits, the head-to-head matchups (MCP vs API, CLI vs MCP, MCP vs ADK), one worked example done four different ways, the grand comparison table, the timeline, the security angle, and how a real agent actually chooses among them at runtime."
reading_time: 30
---

If you have spent any time reading the 2025–26 literature on AI agents, you've encountered all four of these acronyms — usually within a few paragraphs of each other, usually with confident claims about which one is "winning," and usually with no clear explanation of how they actually relate. **API**, **CLI**, **MCP**, **ADK**. They sound like contenders in a race. They aren't. They live at *different layers of the same stack*, and the fastest way to stop confusing them is to picture that stack from the bottom up.

The bottom layer is the **API** — the universal contract that lets two pieces of software talk to each other. Above that is the **CLI** — a particular kind of API surface, designed for human typing and for shell scripting, that an agent can drive just as easily. Above that is **MCP** — the Model Context Protocol, a 2024 standardization of "how an LLM exposes itself to tools and how tools expose themselves to the LLM," sometimes called the USB-C of AI tools. And above that is **ADK** — an *Agent Development Kit*, the workshop you use to compose an agent that knows how and when to reach for the layers below. Skills and A2A round out the picture: Skills are the knowledge layer that teaches the agent *how* to use a given tool well, A2A is the protocol family that lets agents talk to each other.

This monograph is the full working tour through all of that — grounded in IBM Technology's *Think* series talks by Martin Keen, Cedric Clyburn, and Jeff Crume — with the four source videos embedded inline at the relevant sections, the head-to-head comparison matchups that the field actually argues about, and a worked example where the same simple task (book a meeting on a calendar) is done four different ways so the differences become concrete instead of conceptual.

## What it covers

Twenty sections, about thirty minutes of reading.

**§ 01–02 — Orientation.** The one-paragraph mental model. The four definitions side by side, in a single table.

**§ 03 — API — the universal contract.** What an API actually is. REST, gRPC, GraphQL. Why every layer above this is, eventually, *just* an API.

**§ 04 — CLI — the agent at the terminal.** Why CLIs are an underrated tool surface for agents. The argument parsing, the standard streams, the exit codes. Why "drive the CLI" is sometimes the right answer when a structured API doesn't yet exist.

**§ 05 — MCP — the USB-C of AI tools.** The Model Context Protocol in detail. The client-server architecture, the standard message types, the discoverability that makes it composable. Why it took over so quickly in 2024–25.

**§ 06 — ADK — the workshop for agents.** Agent Development Kits — Anthropic's, Google's, OpenAI's, and the open-source landscape. What they actually do (compose agents from LLM + tools + memory + control flow). Where they differ.

**§ 07 — Skills — teaching the agent *how*.** The knowledge layer. SKILL.md files, progressive disclosure, the description-trigger problem. Why skills are complementary to tools, not a replacement for them. Cross-links to the [Skills in AI Agents]({{ '/posts/skills-in-ai-agents/' | relative_url }}) post for the deeper treatment.

**§ 08 — A2A & the protocol zoo.** Agent-to-Agent protocols. The handful of competing standards (Google's A2A, the AgentProtocol consortium, ACP). What they're trying to solve and where the field hasn't converged yet.

**§ 09–11 — Head-to-head matchups.** The arguments the field actually has. *MCP vs API* — when MCP earns its keep and when raw API calls are cleaner. *CLI vs MCP* — what you give up by wrapping a CLI in MCP, what you gain. *MCP vs ADK* — the "infrastructure vs tooling" distinction that's easiest to muddle.

**§ 12 — One task, four ways.** A worked example. The same task — book a meeting on a calendar — implemented four different ways, with the actual code for each. The line counts and failure modes laid bare.

**§ 13 — The grand comparison table.** All five (API · CLI · MCP · ADK · Skills) on a single page, with columns for purpose, audience, discovery model, error mode, security boundary, and typical example.

**§ 14 — A short timeline.** The decade-long evolution. REST in the early 2010s. CLI-as-tool around 2018. LangChain in 2022. MCP in 2024. The ADK consolidation in 2025–26.

**§ 15 — How an agent actually chooses.** The runtime decision logic. What the LLM sees when it's deciding which surface to reach for, and how prompt engineering, schema design, and tool ordering all bias that decision.

**§ 16 — Practical engineering notes.** The hard-won field notes. Logging at the tool boundary. Timeouts. Retry policy. Idempotency. The patterns that the talks gloss over but production deployment cares deeply about.

**§ 17 — Security & the OWASP angle.** Tool-call injection. Credential exposure. The OWASP Top 10 for LLMs as applied to the tool surface specifically.

**§ 18 — Misconceptions & FAQ.** The handful of confidently-stated claims that keep circulating and are mostly wrong. "MCP replaces APIs." "You need an ADK." "Skills compete with MCP."

**§ 19–20 — The videos & references.** The four IBM *Think* talks embedded inline at the right sections. Plus the surrounding literature (Anthropic's MCP docs, Google's ADK announcement, the A2A protocol drafts).

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/api-cli-mcp-adk.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-paper editorial layout — five color-coded accent chips (one per acronym), Fraunces display, IBM Plex Mono code. The four IBM *Think* talks are embedded inline as references.

---

← Back to [Autonomy]({{ '/' | relative_url }})
