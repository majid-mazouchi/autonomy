---
title: "Twenty-Two Ideas That Shape Modern AI Systems"
subtitle: "A visual primer on the concepts every engineer working with language models keeps running into — from tokens and embeddings to guardrails and evaluation."
date: 2026-04-22 12:00:00 -0400
category: "Machine Learning"
slug: twenty-two-ideas-visual-primer
excerpt: "A 22-chapter field guide to modern AI systems — tokenization, attention, LLMs, prompting techniques, RAG, agent frameworks, MCP, and the engineering considerations around them."
reading_time: 3
---

Every few months, a new wave of acronyms lands in the AI ecosystem — MoE, RAG, ReAct, ToT, MCP — and every engineer I talk to is quietly maintaining a mental glossary trying to keep up. This post is my attempt to put mine on paper.

## What it covers

Twenty-two chapters, grouped into four parts, designed to be read end-to-end or jumped into wherever you need a refresher:

**Part One — The Substrate.** Tokenization, embeddings and vector space, attention, the large language model itself, and Mixture of Experts. What the model actually *is* before you start prompting it.

**Part Two — Prompting and Reasoning.** Few-shot / in-context learning, chain of thought, self-consistency, tree of thought, ReAct, structured outputs and function calling. The behavioral layer sitting on top of the model weights.

**Part Three — Knowledge and Retrieval.** Knowledge graphs, retrieval-augmented generation, agentic RAG. How models interact with information they don't have in their training data.

**Part Four — Agents, Tools, and Deployment.** State machines, LangGraph-style agents, agent memory, multi-agent frameworks, Model Context Protocol, the fine-tuning versus RAG versus prompting decision, evaluation, and guardrails / prompt injection. The systems engineering around shipping something that actually works in production.

Every chapter has a diagram you can read in about twenty seconds and prose that explains the thing without resorting to hand-waving. The whole piece takes roughly fifteen minutes to read.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/twenty-two-ideas.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

The visual primer lives at its own URL with its own visual identity — a darker paper, a different typographic voice, a full set of custom diagrams. It's intentionally designed as a standalone artifact, so this post is mostly a pointer. Hit the button above and enjoy.

---

← Back to [Autonomy]({{ '/' | relative_url }})
