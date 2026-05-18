---
title: "A Primer on CUDA — Parallel Computing on the GPU"
subtitle: "From the architectural distinction between CPU and GPU, through the thread hierarchy and memory model, to the practical concerns of warp execution, memory coalescing, and shared-memory tiling."
date: 2026-04-11 10:00:00 -0400
category: "Tools"
slug: cuda-primer
excerpt: "An interactive primer on CUDA for engineers comfortable with C but new to GPU programming. Twelve demonstrations covering thread hierarchy, memory model, warp execution, memory coalescing, shared-memory tiling, and the toolkit."
reading_time: 35
---

Once you've decided to take advantage of the GPU sitting in your machine — or in the rack you're renting — there's a moment where the abstraction breaks down and you have to actually understand what's happening on the device. CUDA is the platform that exposes that level. It's been the dominant model for general-purpose GPU computing for over a decade, and it's the substrate underneath every major deep-learning framework, every modern computer-graphics pipeline, and a lot of scientific computing besides.

This primer is the introduction I wish I'd had: deliberately operational, focused on the mental model and the practical performance concerns rather than the API surface. If you know C and you can describe what parallelism *means* in a sentence, you have the prerequisites.

## What it covers

Twelve chapters, twelve interactive demonstrations, about thirty-five minutes to read carefully.

**§I — Why a GPU at all.** The architectural distinction. Throughput vs latency. When the GPU wins and when it doesn't.

**§II — The mental model.** SIMT. The hierarchy from device → kernel → block → thread. The single picture that makes everything else make sense.

**§III — The thread hierarchy.** Grids, blocks, threads. The dimensions and indexing scheme. How to map a problem onto this structure.

**§IV — A first kernel.** The "hello world" — vector addition. Launch syntax, kernel function, device pointers, memory transfer.

**§V — The memory hierarchy.** Global, shared, constant, texture, registers. The throughput differences. Why this matters more than anything else for performance.

**§VI — Warps and SIMT execution.** What "32 threads execute together" means. Warp divergence and its cost.

**§VII — Memory coalescing.** The single most important optimization. Why thread-stride matters more than algorithmic cleverness for most kernels.

**§VIII — Shared memory and tiling.** The pattern that turns memory-bound kernels into compute-bound kernels. The matrix multiplication classic.

**§IX–XII — The rest of the working toolkit.** Streams. Atomics. Reductions. cuBLAS / cuDNN / Thrust. The CUDA ecosystem beyond hand-written kernels.

Each chapter has a live interactive demonstration where the parameters of the model can be dragged around and the behavior observed.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/cuda-primer.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
