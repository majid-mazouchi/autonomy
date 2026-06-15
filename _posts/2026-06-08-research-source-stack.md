---
title: "A Field Guide to Research Sources — for an Agentic Scientific Researcher"
subtitle: "Where to send the agent looking. A plain-language guide to the libraries, code shelves, and lecture halls a scientific research agent should search — and what each one is actually good for."
date: 2026-06-08 19:00:00 -0400
category: "Tools"
slug: research-source-stack
excerpt: "An AI agent that does literature surveys is only as good as the libraries it knows to search. arXiv for preprints. Semantic Scholar for citation graphs. Crossref for canonical metadata. OpenAlex for the open-graph alternative. GitHub for code. Papers With Code for benchmarks. YouTube and Spotify for lectures and conference talks. This field guide is the working tour of the source stack — what each library is actually good for, how to query it, what the rate limits look like, and the pipeline a competent research agent runs over them. With a downloadable harness kit and an MCP-builder skill bundle."
reading_time: 19
---

An AI agent that does literature surveys is only as good as the libraries it knows to look in. This sounds obvious, but the operational consequence isn't — every agent system that does any kind of research work converges on a stable set of *sources* it queries, in a stable *order*, with a stable *ranking discipline* — and the difference between an agent that produces useful surveys and one that hallucinates citations is almost entirely in this stack. The model layer matters less than you'd think; the source-stack layer matters more.

This field guide is the plain-language tour of that stack — for the engineer building an agent that does scientific literature work, the layers are arXiv (preprints), Semantic Scholar (citation graphs), Crossref (canonical metadata), OpenAlex (the open-graph alternative), GitHub (code), Papers With Code (benchmarks), YouTube and Spotify (lectures and conference talks). The guide walks through each one carefully — what it's actually good for, how to query it, what the rate limits and quotas look like, the failure modes — and then assembles them into the pipeline a competent research agent runs.

It is the practical companion to the [Skills in AI Agents]({{ '/posts/skills-in-ai-agents/' | relative_url }}) and [Knowledge & Memory in LLMs]({{ '/posts/llm-knowledge-and-memory/' | relative_url }}) monographs — those documents cover the *architecture* layer; this one is about the specific *data sources* an agent in a research domain should be wired to.

## What it covers

About nineteen minutes of reading. Designed for one-source-at-a-time reference use afterward.

**§ 01 — Papers (arXiv, Semantic Scholar, Crossref, OpenAlex).** The four sources that account for almost all serious academic-literature work. arXiv for the freshest preprints (most fields, daily updates). Semantic Scholar for the citation graph (who cites whom, who built on what). Crossref for canonical metadata (the DOI registry; the source of truth for "what this paper *is*"). OpenAlex for the open-graph alternative that's been quietly eating into the commercial scientific-graph market.

**§ 02 — Code (GitHub, Papers With Code).** GitHub for the implementations themselves. Papers With Code for the bridge between papers and the code that goes with them. The query patterns and the data-freshness considerations.

**§ 03 — Video & other (YouTube, Spotify, podcasts).** The non-paper sources that increasingly carry the most current thinking — recorded conference talks, lab seminars, working-paper-stage discussions. The transcription-and-indexing pipeline that turns these into searchable text.

**§ 04 — The pipeline.** The order an agent actually queries these in. Why papers come first, then code, then video. The deduplication step (the same paper appears in arXiv, Semantic Scholar, Crossref, and OpenAlex — only one of those should be canonical for the agent's index). The merge step.

**§ 05 — Ranking & retrieval.** Once you have results from across the stack, how do you rank them? Recency. Citation count. Author authority. Source-trust score. The ranking function that decides what gets into the agent's context window.

**§ 06 — Quotas & limits.** The rate-limit table for each source. The exponential-backoff patterns. The user-agent / contact-email discipline that keeps you on the right side of the libraries' terms of service.

**§ 07 — Failure modes.** The dozen ways this pipeline breaks. Hallucinated citations. Stale metadata. Out-of-date Papers-With-Code links. Authors with ambiguous name disambiguation. The defensive patterns.

## Downloads

The harness kit and the mcp-builder skill bundle live at the end of the field guide. Both are also linked directly here:

<div style="margin: 20px 0; font-family: 'IBM Plex Mono', monospace; font-size: 13px;">
  <p>↓ <a href="{{ '/assets/posts/research-harness.zip' | relative_url }}" download>research-harness.zip</a> — a working harness with a literature-survey skill, a person-dossier skill, a scientific-researcher agent profile, and the FastMCP server that exposes the source stack as tools.</p>
  <p>↓ <a href="{{ '/assets/posts/mcp-builder-skill.zip' | relative_url }}" download>mcp-builder-skill.zip</a> — a standalone Skill that teaches an agent how to build new MCP servers (FastMCP for Python, TypeScript SDK reference, evaluation discipline).</p>
</div>

Both kits are MIT-licensed and ready to drop into a project.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/research-source-stack.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

The field guide lives at its own URL with a warm-paper editorial layout — teal accent for papers, rust for code, gold for video. Seven sections, a downloadable harness, and the MCP-builder skill kit.

---

← Back to [Autonomy]({{ '/' | relative_url }})
