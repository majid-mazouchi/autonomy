---
title: "Feeding C to a Reasoning Machine — Parsing C Source for LLMs"
subtitle: "How to take a raw .c file and turn it into something a large language model can actually think about — explained plainly, with the alternatives laid side by side."
date: 2026-05-30 10:00:00 -0400
category: "Tools"
slug: parsing-c-for-llms
excerpt: "An LLM reads text. Source code is text. So why isn't this trivial? Because raw .c files come with a preprocessor that has to be expanded before the code is meaningful, with #include trees that span hundreds of files, with macros that change the meaning of identifiers, and with context windows that fill up in two function definitions. This working monograph walks through the full pipeline — tokens, ASTs, call graphs, slicing, summarization — and ends with the genuinely hard case: AUTOSAR generated code, which resists every standard reasoning move."
reading_time: 28
---

The naïve approach — paste the .c file into the chat — works on a 100-line example and fails on every real-world codebase you'll touch. The naïve-plus approach — paste the whole repo, let the model figure it out — fails at the context window. The pipeline that does work in production has half a dozen stages, each of which is a small choice with measurable consequences. This monograph is the working description of that pipeline.

The structure is deliberately staged from the simplest move (chopping source into tokens) up through the harder ones (building an AST, tracing the preprocessor, capturing call relationships, slicing for the context window, summarizing for display) and finally to the case that broke many of these moves at my day job: AUTOSAR-generated code, which is technically C but resists every standard parsing strategy because the meaning lives in the XML configuration files, not in the .c source.

Tap the demos in any of the chapters — they're working examples on real C code.

## What it covers

Fifteen chapters, about twenty-eight minutes of reading. The interactive demos roughly double that if you play with them.

**§ 01 — The problem in one breath.** An LLM reads text. Source code is text. So why isn't this trivial?

**§ 02 — A ladder of representations.** Raw bytes → tokens → AST → AST + symbol table → AST + symbol table + call graph → semantic slice. Each rung is a more expressive way to talk about the code, at higher engineering cost.

**§ 03 — Chopping into tokens.** The simplest level. What a tokenizer is, what `clang -E -dump-tokens` shows, and why this is sometimes enough.

**§ 04 — Building the tree.** Lifting tokens to an abstract syntax tree. The grammar, the parser, why C is a famously annoying language to parse cleanly. tree-sitter as the modern fast-enough approach. libclang for when you need a real one.

**§ 05 — The C-only landmine: the preprocessor.** Why a `.c` file is meaningless until `#include`s are expanded and macros are substituted. The two parsing strategies — pre-expansion and post-expansion — and the trade-offs of each.

**§ 06 — Capturing relationships.** Symbol tables, call graphs, type graphs. The graph data structure that lets the model answer questions like "who calls `inverter_step()`" without having the whole file in context.

**§ 07 — Slicing for the context window.** The hard part. Given the relationship graph and a question, which slices of code should we hand to the model? Function-at-a-time, called-functions-included, dataflow slices, change-set slices. Comparison and trade-offs.

**§ 08 — Showing only what matters.** Filtering and summarization. Stripping the comments that aren't relevant, collapsing macro expansions back to their source, replacing imports with summaries.

**§ 09 — How to actually hand it to the model.** The API-level details. JSON wrapping. Tool-call wiring. The difference between "pasting code" and "providing a structured snippet."

**§ 10 — The whole pipeline, end to end.** A concrete worked example. A real C file, a real question, every stage of the pipeline shown.

**§ 11 — Every method, side by side.** The comparison table. Raw paste vs. tokenizer-only vs. tree-sitter vs. libclang vs. semantic graph. Latency, accuracy, build complexity, when each one is the right choice.

**§ 12 — Practical notes — the things that bite.** The hard-won observations. Conditional compilation. Bit-fields. Function pointers. Linker scripts. The cases where the model will be confidently wrong unless you've prepared the input carefully.

**§ 13 — When the C is just an artifact: AUTOSAR.** The genuinely hard case. Many real automotive C codebases are generated from XML configuration files (RTE.c, BSW config). The C is technically the source of truth at compile time, but the *meaning* lives in the .arxml. What this does to LLM reasoning.

**§ 14 — Why AUTOSAR resists reasoning.** The deeper reason. AUTOSAR-generated C is structurally simple but semantically dense: every line refers to something in a configuration database that the model can't see. The two strategies that work (lift the .arxml to a knowledge graph; or run the model with a configuration-aware tool).

**§ 15 — References & further reading.** tree-sitter, libclang, the Clang LibTooling docs. The standard "Modern Compiler Implementation" texts. The handful of papers on neural code understanding.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/parsing-c-for-llms.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-paper editorial layout — rust accent, teal link color, Fraunces display. Interactive demos in the relevant chapters.

---

← Back to [Autonomy]({{ '/' | relative_url }})
