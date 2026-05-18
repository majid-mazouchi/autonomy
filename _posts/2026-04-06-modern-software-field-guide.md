---
title: "A Field Guide to Modern Software Concepts"
subtitle: "An interactive monograph in five volumes and thirty-six chapters — the vocabulary of the modern software stack, from schemas and APIs through AI tooling, retrieval, and the cloud."
date: 2026-04-06 10:00:00 -0400
category: "Tools"
slug: modern-software-field-guide
excerpt: "A 36-chapter reference monograph covering the working vocabulary of the modern software stack — JSON, APIs, regex, parsers, JSON Schema, ReAct, tokens, embeddings, RAG, BM25, Tailwind, and the rest of the practical glossary. Built as a lookup-as-you-need-it reference, not a tutorial."
reading_time: 60
---

There's a particular vocabulary that working software engineers absorb almost subconsciously over years — the half-noun, half-jargon shorthand that lets two engineers describe a complex system in three sentences. *We're going to RAG over the docs, return a JSON-Schema'd response, and stream tokens to the client via SSE.* Each of those words has a specific technical meaning, a history, and a context in which it's used correctly. Knowing them quickly is a non-trivial professional skill — every junior engineer eventually realizes that *not* knowing them is what's blocking them from following design conversations.

This field guide is the explicit form of that vocabulary. It's a 36-chapter reference, organized into five volumes, with each chapter a self-contained explanation of one concept — what it is, what problem it solves, what the working engineer needs to know about it. Built to be looked up rather than read end-to-end.

## What it covers

Five volumes, thirty-six chapters. The chapter list is too long to enumerate inline, so here are the volume summaries:

**Volume I — Foundations.** Schema, JSON, API, Parser & Parsing, Regular Expressions, JSON Mode, JSON Schema, ReAct, Tailwind, BM25 Search.

**Volume II — AI & Retrieval.** Tokens & Context Window, Embeddings, Vector Search, RAG, Retrieval Strategies, Prompt Engineering, Function Calling, Streaming.

**Volume III — Infrastructure.** Container Orchestration, Microservices, Message Queues, Caching Layers, Database Choices, Auth Patterns, Observability, Rate Limiting.

**Volume IV — Practice.** Testing Strategies, CI/CD, Feature Flags, A/B Testing, Versioning, Migrations, Monitoring, Incident Response.

**Volume V — Application.** End-to-end worked examples that tie the previous four volumes together into recognizable systems.

Each chapter is roughly 100-300 words and includes diagrams or interactive figures where they help. The intent is a *fast reference* — when someone says "we're using SSE for streaming," you can look up SSE in fifteen seconds and know what's being discussed.

The whole document is a 4,800-line standalone HTML page, so the table of contents is the way you navigate it. Sections are linkable so you can bookmark individual concepts.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/modern-software-field-guide.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
