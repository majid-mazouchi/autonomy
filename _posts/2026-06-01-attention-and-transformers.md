---
title: "Inside the Language Model — Attention & Architecture"
subtitle: "A working monograph on what a transformer actually computes — tokens, embeddings, positional encoding, scaled dot-product attention, multi-head attention, the transformer block, decoder stacking, and the training story. With live demos for every concept."
date: 2026-06-01 09:00:00 -0400
category: "Neural Networks"
slug: attention-and-transformers
excerpt: "Attention is the one mechanism that pulled neural networks out of recurrent dead-ends and into the modern era. Every modern language model — GPT, Claude, Gemini, Llama — is some variation on the original 2017 transformer. This monograph is the working tour through what a transformer actually computes: how tokens become embeddings, how positional information is added back in, what attention is doing geometrically, why we scale by √d_k, how multi-head attention factors the computation, and how the full block is assembled and stacked. Every concept comes with a live demo."
reading_time: 32
---

There is a moment in learning about transformers when everything clicks. For most people it is when they see, for the first time, that attention is just a weighted average — a *soft* lookup table where the weights are computed from the data itself. Up to that moment, "attention" sounds like magic. After that moment, it sounds like one of the more obvious ideas in machine learning, and the surprise becomes the fact that it took until 2017 for someone to combine it with positional encoding, layer normalization, and residual connections to produce a model that scaled the way the transformer scales.

This monograph is the working tour through what a transformer actually computes. The format is deliberate: math where math earns its place, demos where demos make the math obvious, and prose connecting the two. I have tried to write it so that someone with a working knowledge of linear algebra and a Python interpreter can come out the other side actually understanding the mechanism — not just having read the words "scaled dot-product attention."

It is the companion to the Neural Networks interactive primer and deep dive already on this site. Where those cover the breadth of modern NN practice, this one zooms in on the single mechanism that made modern language models possible.

## What it covers

Thirteen sections, about thirty-two minutes of reading. Longer if you stop and play with the demos, which is the point.

**§ 01 — The big picture.** Three views of the transformer in one figure: as a sequence model, as a matrix-multiplication stack, and as an information-routing graph. The vocabulary the rest of the monograph assumes.

**§ 02 — Tokens & embeddings.** The first step. Subword tokenization (BPE, SentencePiece) and what the model actually sees. The embedding matrix as a learned lookup table. Why the same word can have different embeddings in different positions (it shouldn't; see next section).

**§ 03 — Positional encoding.** The fix for the previous footnote. Sinusoidal encodings (the original 2017 idea), learned absolute positions, RoPE (the modern standard), ALiBi. The trade-offs and what each one breaks when you push beyond its training length.

**§ 04 — Attention, from scratch.** The whole derivation. Queries, keys, values. Why each token computes a Q, K, V from its own embedding. The dot product as a similarity measure. The softmax as the operation that turns similarities into weights. The weighted sum that produces the output. The full equation, derived step by step.

**§ 05 — Softmax & the √d_k scaling.** The detail that took 18 months to discover. Why we divide by the square root of the key dimension before the softmax. The variance argument. What happens (gradients vanish, training fails) if you forget.

**§ 06 — Multi-head attention.** Factoring attention into multiple parallel "heads" — what this buys you, geometrically. Why each head learns to attend to different patterns (syntactic dependencies, named entities, coreference, etc.). The concatenation and projection at the end.

**§ 07 — Anatomy of the attention block.** Putting it all together. Layer norm, the attention computation, the residual connection, dropout. The order matters (pre-norm vs post-norm). The exact matrix dimensions at every step.

**§ 08 — The transformer block.** Attention block + feedforward block + residuals + layer norms. The FFN as a per-token MLP. Why the FFN dimension is typically 4× the model dimension. The full forward pass, drawn out.

**§ 09 — Stacking & the decoder.** Why you need many of these stacked. The causal mask that makes the decoder autoregressive. The encoder-decoder distinction (and why most modern LLMs are decoder-only).

**§ 10 — Cross-attention.** The mechanism that lets the decoder look back at the encoder. The role of cross-attention in translation, in vision-language models, in retrieval-augmented generation.

**§ 11 — From logits to words.** Generation. Greedy decoding, top-k, top-p (nucleus), temperature, beam search. The trade-offs between determinism and creativity.

**§ 12 — How models are trained.** Pretraining. Next-token prediction as the universal objective. The data, the loss, the optimizer (AdamW), the schedule, the chinchilla scaling laws. The two-stage SFT → RLHF process that turns a base model into an assistant.

**§ 13 — Practical engineering notes.** The things that bite. KV-cache and why inference is fundamentally different from training. Flash attention. Speculative decoding. Quantization at inference time. The handful of optimizations that turn a research paper into a serving system.

**References & further reading.** Vaswani et al. 2017 (the original *Attention is All You Need*). The Anthropic and OpenAI technical reports. Karpathy's nano-GPT for the canonical clean implementation.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/attention-and-transformers.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-paper editorial layout — rust accent, indigo cross-references, IBM Plex Mono throughout. Every section has at least one interactive demo. Designed to be read once cover-to-cover and then reached for one section at a time as a reference.

---

← Back to [Autonomy]({{ '/' | relative_url }})
