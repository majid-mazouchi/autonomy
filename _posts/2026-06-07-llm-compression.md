---
title: "LLM Compression, Explained Simply"
subtitle: "Why running a large language model costs more than training it ever did — and how quantization, distillation, KV-cache tricks, and friends shrink the bill without (much) hurting the answers."
date: 2026-06-07 13:00:00 -0400
category: "Tools"
slug: llm-compression
excerpt: "Training a frontier LLM is a one-time cost, paid by a handful of companies. Inference is the recurring cost, paid by everyone who serves the model — and at scale, inference cost dwarfs training cost by orders of magnitude. The field of LLM compression is the engineering response: quantization, distillation, pruning, KV-cache tricks, speculative decoding, and a dozen other techniques that shrink the per-query bill without (much) hurting the output. This post is the plain-language tour of the toolkit."
reading_time: 17
---

The economics of LLM deployment have inverted what most engineers expect. Training a frontier model is a famously expensive one-time cost — hundreds of millions of dollars, six-figure GPU bills, billions of tokens. But it is paid once, by maybe a dozen companies in the world. *Inference* — running the model in production to answer queries — is the recurring cost, paid by everyone who serves the model, on every token of every conversation. At any meaningful scale, inference dwarfs training cost by orders of magnitude, and the gap is the headline reason "LLM compression" has gone from niche specialty to first-class engineering discipline in three years.

This post is the plain-language tour of the compression toolkit — quantization, distillation, pruning, KV-cache tricks, speculative decoding — and the underlying engineering question each technique answers. It is the natural companion to the [Neural Networks Deep Dive Reference]({{ '/posts/neural-networks-deep-dive/' | relative_url }}) (which covers the compression techniques at the math level) and to the [How LLMs See Images]({{ '/posts/how-llms-see-images/' | relative_url }}) / [How LLMs Hear & Watch]({{ '/posts/how-llms-hear-and-watch/' | relative_url }}) posts (which cover the *expansion* side of the same engineering problem — how much context costs in tokens).

## What it covers

About seventeen minutes of reading, organized around the techniques in roughly increasing complexity.

**§ 1 — The economics, in one breath.** Why inference cost matters more than training cost at any real scale. The token-cost math. The cloud bill that turned model compression into a board-level conversation.

**§ 2 — Quantization — the first lever.** What it means to store a weight in 8 bits instead of 16 (or 4 instead of 8). The accuracy trade-off, drawn at every precision tier. Post-training quantization (PTQ) vs quantization-aware training (QAT) and when each is the right reach.

**§ 3 — KV-cache tricks.** The single biggest engineering trick. Why the K and V values from previous tokens can be cached and reused. Why this turns long conversations from O(n²) into something closer to O(n). The cache-eviction policies that work.

**§ 4 — Distillation.** Teach a small model to imitate a big one. Why this works (the big model's softmax outputs contain more information than the discrete tokens). The trade-off curve.

**§ 5 — Pruning.** Remove weights that aren't earning their keep. Structured vs unstructured pruning. Why pruned models compress better but require careful re-training.

**§ 6 — Speculative decoding.** The trick that lets a small draft model propose tokens that a big verifier model accepts or rejects in a single forward pass. The 2-3x speedup with no quality loss, when it works.

**§ 7 — Mixture-of-experts (MoE) at inference.** A different shape of the same idea. Route each token to the small subset of experts that matter, leave the rest sleeping. The serving complexity this introduces.

**§ 8 — Flash attention.** The fused-kernel implementation of attention that drops both memory and latency. Now standard; worth understanding the principle.

**§ 9 — The stack, end-to-end.** How real production systems combine these. A 70B model becomes deployable by stacking quantization (4x), KV-cache compression (variable), distillation to a 7B base, and speculative decoding. The compound effect on cost.

**§ 10 — What to actually reach for.** The pragmatic decision tree. The handful of decisions that compound; the dozen optimization-paper techniques that don't survive contact with production.

**§ 11 — Further reading.** The relevant papers (Flash Attention, the original speculative-decoding paper, the GPTQ paper). The vendor write-ups (vLLM, TensorRT-LLM, llama.cpp documentation).

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/llm-compression.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the post →
  </a>
</div>

The post lives at its own URL with a warm-paper layout — orange accent, blue and green for the per-technique color coding. Plain-language explanations throughout.

---

← Back to [Autonomy]({{ '/' | relative_url }})
