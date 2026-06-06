---
title: "From RAG to Context Engineering"
subtitle: "How a language model gets the right information at the right moment — starting from a fixed retrieval pipeline, then handing the steering wheel to the model itself, and finally turning context into something you deliberately design."
date: 2026-06-05 17:00:00 -0400
category: "Tools"
slug: context-engineering
excerpt: "The single most important determinant of an LLM-powered system's quality is not the model. It's what you put in the context window. This monograph walks through the three architectures the field has converged on for solving that problem — classic RAG (the pipeline retrieves, then the model writes), agentic RAG (the model decides what to retrieve, in a loop), and full context engineering (where the context window itself becomes the deliberately-designed substrate of the system) — with block diagrams, a worked example from a real engineering domain, evaluation patterns, security and cost considerations, and a decision tree for which one to build."
reading_time: 32
---

The most counterintuitive thing about LLM-powered systems is that the model itself is rarely the bottleneck. Once you're using a reasonable frontier model, the quality of your application is determined almost entirely by what you put in the context window — the retrieved documents, the previous turns, the tool-call results, the system prompt, the schemas, the few-shot examples. Get the context right and a mid-tier model often outperforms a frontier model with bad context. Get the context wrong and no amount of parameter scale will save you. This is the lesson the field has been internalizing for the past three years, and the architectures of LLM applications have evolved accordingly.

The arc goes through three distinct stages, and the names matter because the trade-offs between them are real. **Classic RAG** — Retrieval-Augmented Generation — is the original idea: a fixed pipeline retrieves relevant documents, stuffs them into the context, and the model writes a response. It works beautifully for question-answering over a static corpus and breaks the moment the question is even slightly complex. **Agentic RAG** is the next stage: instead of one retrieval step at the start, the model itself drives the retrieval, in a loop, deciding what to fetch next based on what it learned from the previous fetch. This is what most "modern" RAG systems actually are, even if they're still called RAG. **Context engineering** is the third stage and the current frontier: the realization that *every* piece of the context window is something you can design — retrieval is just one of the things going in there, alongside conversation history, tool outputs, structured state, examples, and constraints — and the discipline of engineering all of it deliberately, the way you'd engineer any other system component.

This monograph walks through all three carefully, draws the block diagrams, and runs a worked example from a real engineering domain (an EV traction-drive engineer chasing a flux-table boundary trip) through each architecture so the differences become concrete instead of conceptual. The evaluation taxonomy, the production considerations (security, cost, MCP integration), and the decision tree for which architecture to actually build for a new system are at the end.

## What it covers

Twelve sections, about thirty-two minutes of careful reading.

**§ 01 — The one idea behind all three.** What the three architectures have in common: each one is an answer to the question *"how does the right information get into the context window at the right moment?"* Once you frame it that way, the rest of the field makes sense.

**§ 02 — Anatomy of a context window.** Before we talk about how to fill it, what's actually in it. The system prompt, the conversation history, the tool definitions and tool results, the retrieved content, the few-shot examples, the structured state. The token budget that constrains all of it.

**§ 03 — Retrieval-Augmented Generation (RAG).** The classic architecture. Embed the query, search the vector store, retrieve top-k chunks, stuff them into context, generate. The pipeline is fixed; the model is downstream. Where this works (FAQ-over-docs, simple Q&A) and where it doesn't.

**§ 04 — Under the hood: retrieval, chunking & GraphRAG.** The implementation details that make or break RAG quality. Chunk sizing. Overlap. Embedding model choice. Reranking. The shift to GraphRAG (build a knowledge graph from the corpus, retrieve graph neighborhoods instead of independent chunks) and what it buys you.

**§ 05 — Agentic RAG.** The next architecture. The model decides what to retrieve, looks at what it got, decides what to retrieve next, loops until it has what it needs. The cost (more LLM calls, more latency) versus the benefit (handles multi-hop questions, follow-ups, ambiguity).

**§ 06 — Agentic search & context engineering.** The third stage. Retrieval is no longer special — it's one of many tools the model can call. The context window becomes a deliberately-engineered substrate: structured state for what's known so far, tool definitions for what can be done next, conversation history compacted in principled ways, retrieved content earning its slot the same way every other piece of context does. The discipline that emerges.

**§ 07 — Worked example: a flux-table boundary trip.** The same engineering problem (a motor controller is showing flux-table boundary trips at high load) traced through all three architectures. Classic RAG: retrieve the relevant manual sections, get a generic answer. Agentic RAG: the model retrieves the docs, then realizes it needs the recent log, then retrieves the calibration table. Context engineering: a deliberately-designed context with tools for live log inspection, structured state tracking what's been checked, and retrieval as one option among many. The latency, cost, and answer quality of each laid out explicitly.

**§ 08 — Side-by-side comparison.** The decision matrix. When classic RAG is the right answer (it sometimes is). When agentic RAG is. When you actually need full context engineering. The pricing-per-query and the latency-per-query of each, on the same workload.

**§ 09 — Evaluation & failure taxonomy.** How to tell whether your system is working. Retrieval metrics (recall@k, MRR). Generation metrics (faithfulness, answer relevance, context utilization). The dozen failure modes that show up in production and which ones each architecture is most vulnerable to.

**§ 10 — Production: security, cost, MCP.** What changes when this goes to production. Prompt injection through retrieved content. The cost calculus when agentic loops can call themselves recursively. The MCP integration story — how each architecture maps onto Model Context Protocol tool calls.

**§ 11 — Which one should you build?** The decision tree. Three questions, four paths, a recommendation for each. The honest version, with the answer "start with RAG, you probably don't need agentic" much more often than the marketing implies.

**§ 12 — Notes & references.** The relevant papers (the original RAG paper, the GraphRAG paper, the agentic RAG literature), the production write-ups (Anthropic's, Pinecone's, the LangChain blog), and the handful of independent voices that have changed my own practice.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/context-engineering.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-paper editorial layout — rust accent, color-coded chips for the three architectures, block diagrams throughout. Designed to be read once cover-to-cover when you're orienting in the field, then reached for one section at a time when you're making a specific architectural decision.

---

← Back to [Autonomy]({{ '/' | relative_url }})
