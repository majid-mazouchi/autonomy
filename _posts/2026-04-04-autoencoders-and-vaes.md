---
title: "Autoencoders and Their Variational Cousin"
subtitle: "A hands-on primer on how neural networks learn to compress, reconstruct, and imagine — with live figures you can poke at."
date: 2026-04-04 10:00:00 -0400
category: "Machine Learning"
slug: autoencoders-and-vaes
excerpt: "An illustrated primer on autoencoders and variational autoencoders. The bottleneck principle, what lives in the latent space, the variational reformulation that turned an unsupervised compressor into a generative model. Six interactive figures."
reading_time: 15
---

An autoencoder is the quietly elegant idea that a neural network can teach itself something useful by attempting to reconstruct its own input through a deliberately undersized bottleneck. The constraint of having to pass everything through a low-dimensional middle layer forces the network to discover what *matters* in the data — what can be thrown away, what has to be preserved.

The variational autoencoder is the same idea with a different theory of the middle. Instead of a fixed compressed code, the bottleneck becomes a probability distribution, which turns the autoencoder from a learned compressor into a learned generator. You can sample from the latent space and decode back into new examples that look like the training data. That's the trick that powered the first wave of practical generative models, before diffusion took over.

This primer walks through both. It's monograph № 1 in a small series on representation learning.

## What it covers

Six sections, six live figures, about fifteen minutes to read.

**§1 — The core idea.** Reconstruction through a bottleneck. Why the constraint is the point.

**§2 — Anatomy of an autoencoder.** Encoder, latent, decoder. The shape of a typical implementation. What "tied weights" means and when it's used.

**§3 — The bottleneck, interactively.** A live figure showing what reconstruction quality looks like at different bottleneck widths. Drag the slider, watch the model blur its way through compression.

**§4 — What lives inside the middle?** Visualizing the learned latent space for 2D-bottleneck cases. The lattice of digit prototypes that emerges from MNIST. The intuition that does most of the work for the rest of the primer.

**§5 — Enter the Variational Autoencoder.** The reformulation. The encoder outputs a distribution, not a point. The reparameterization trick. The KL-divergence regularization term that keeps the latent space organized.

**§6 — A walk through latent space.** What sampling looks like. Linear interpolation between two encoded examples. The continuous generative behavior that makes VAEs feel like more than just compressors.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/autoencoders-and-vaes.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
