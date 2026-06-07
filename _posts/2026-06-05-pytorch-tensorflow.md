---
title: "PyTorch & TensorFlow — A Plain-Language Monograph"
subtitle: "The two engines behind modern artificial intelligence — explained in plain words, with practical notes, runnable examples, and a map of where each one shines."
date: 2026-06-05 21:00:00 -0400
category: "Machine Learning"
slug: pytorch-tensorflow
excerpt: "PyTorch and TensorFlow are the two frameworks that almost every modern neural network is trained on — but the differences between them, and the reasons one wins in research and the other in deployment, are surprisingly hard to find written down in plain language. This monograph is that explanation. The training loop drawn out step by step, the design philosophy of each framework laid side by side, the historical arc that produced the current state of affairs, and the practical guidance for picking one for a new project."
reading_time: 18
---

There are very few engineering questions that have produced more inconclusive arguments per square inch than *"PyTorch or TensorFlow?"* and most of those arguments would have been resolved in five minutes if both sides had stopped to agree on what each framework actually is. The frameworks are not the same shape — TensorFlow is a graph-execution engine that grew a high-level API (Keras) on top of it; PyTorch is a dynamic tensor library that grew a serving infrastructure (TorchServe, ExecuTorch) beneath it — and the "right" choice depends almost entirely on which end of that arc you care most about.

This monograph is the plain-language version of the comparison. It assumes you've heard the names, perhaps trained a small model in one of them, and want to actually understand what each framework is, why each one exists, and how to pick between them for a new project. The math underneath neural networks is *not* the focus — that's covered in the [Attention & Architecture]({{ '/posts/attention-and-transformers/' | relative_url }}) and Neural Networks posts on this site. The focus here is the engineering layer above the math: the training loop, the tensor library, the optimizer, the data loader, the deployment story.

## What it covers

Twelve sections, about eighteen minutes of reading.

**§ 01 — The big picture.** What "deep learning framework" actually means. The four jobs a framework does (autograd, tensor ops on the right hardware, optimization, data loading) and why these particular four jobs are non-trivial.

**§ 02 — A kitchen analogy.** The framework as the *kitchen* — pots, pans, a stove, a refrigerator. The model as the *recipe*. The data as the *ingredients*. Why this analogy is useful before any math shows up.

**§ 03 — What they share.** What the two frameworks have in common (which is more than the arguments suggest). Tensors, autograd, GPU/TPU acceleration, the standard set of layer types and optimizers, broadly similar Python APIs.

**§ 04 — The training loop, drawn.** The same five-step loop both frameworks compute. Forward pass → loss → backward pass → optimizer step → repeat. Drawn out with the actual code for each framework side by side.

**§ 05 — Meet PyTorch.** What PyTorch is and why researchers reach for it. Dynamic computation graphs (define-by-run). The Pythonic, debug-friendly feel. The Lightning / HuggingFace ecosystem that grew around it. The deployment story (ExecuTorch, TorchScript, ONNX) — and how it improved between 2022 and 2026.

**§ 06 — Meet TensorFlow.** What TensorFlow is and where it still wins. Static graphs (originally), Keras (the high-level API that made it usable), TF Serving, TFX, TensorFlow Lite. The production-first design that survived the framework wars and still owns much of mobile and embedded ML deployment.

**§ 07 — A short history.** How the field got here. TensorFlow 1.x (2015). PyTorch (2016). Keras as a unifier (2017). The PyTorch ascendancy in research (2018–2021). TensorFlow 2.x and the eager-mode pivot (2019). The current near-equilibrium where PyTorch dominates research and HuggingFace, TensorFlow dominates production deployment outside of research labs, and JAX is quietly eating both at the frontier.

**§ 08 — Side by side.** The comparison table the rest of the field argues about. Dynamic vs static graphs. Pythonic vs declarative. Research vs production. Eager vs graph mode. The four-cell matrix that decides which one you should reach for.

**§ 09 — Practical notes & gotchas.** The things that bite. CUDA version drift. The mixed-precision API that's slightly different in each framework. Data loader bottlenecks that nobody notices until they look at GPU utilization. The "moves between devices" pattern that catches everyone twice.

**§ 10 — JAX and the next thing.** The framework that wasn't in the picture in 2020 and now is. What JAX brings (functional purity, JIT compilation, vmap/pmap for parallelism). Where it's winning (frontier research, especially at DeepMind and Google Brain) and where it's not.

**§ 11 — Picking one for a new project.** The decision tree. Five questions in order. The honest version that admits the answer is "PyTorch, almost always, unless you have a specific reason."

**§ 12 — Further reading.** The official tutorials. The "Deep Learning with PyTorch" book. The TensorFlow Hub. The handful of YouTube channels that actually teach this well.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/pytorch-tensorflow.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-paper editorial layout — torch-orange accent for PyTorch, TF-orange for TensorFlow, twelve sections, runnable code side by side wherever the comparison earns it.

---

← Back to [Autonomy]({{ '/' | relative_url }})
