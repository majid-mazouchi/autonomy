---
title: "The Paradigms of Machine Learning"
subtitle: "Six paradigms, six different theories of what it means to learn — from labels, to structure, to consequences, to demonstrations, to other agents' knowledge."
date: 2026-04-29 10:00:00 -0400
category: "Machine Learning"
slug: paradigms-of-machine-learning
excerpt: "A field guide to the six paradigms of machine learning — supervised, unsupervised, reinforcement, imitation, transfer, and the rapidly-merging boundaries between them. The mechanisms, the math, and the problems each one was built for."
reading_time: 8
---

The way most introductions to machine learning are structured, you'd think it was one discipline. It isn't. It's six or seven disciplines that share a vocabulary and not much else — the structural difference between learning a classifier from labels, finding clusters with no labels, learning to act in an environment that gives you reward signals, copying a human demonstrator, and adapting a model trained on one task to work on another is *substantial*. Each is a different theory of what "learning" means.

This primer lays the paradigms out side by side. The goal is to give you a clean mental map: when someone says "we're using deep learning here," you should be able to ask which paradigm they're using, and that question should produce a clean answer.

## What it covers

Six paradigm chapters plus comparison and context, about twenty minutes to read.

**Supervised Learning.** The default. Labels in, function out. Classification and regression. Why this paradigm gets all the attention even though it covers less than half of practical ML.

**Unsupervised Learning.** No labels, only data. Clustering, dimensionality reduction, generative modeling. The paradigm that quietly powers feature learning, anomaly detection, and the embedding-based recommendation systems we all use.

**Reinforcement Learning.** No labels, only consequences. Why this paradigm took decades to mature, why it works so well in games and so unevenly elsewhere, and the [eight-post field guide]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }}) on this site that goes much deeper.

**Imitation Learning.** Learning from demonstrations rather than labels. BC, DAgger, GAIL. Why this paradigm got large again with the rise of robot learning.

**Transfer Learning.** Reusing what a model learned about one task to do another. The single most economically important paradigm in the LLM era — fine-tuning *is* transfer learning at scale.

**Online vs Offline RL.** A short detour into the subtlety that's reshaping RL in the 2020s: does the agent get to interact with the environment, or is it stuck learning from a fixed dataset?

Plus a comparison section that lines up all six paradigms by data type, signal, application domain, and characteristic failure mode.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/paradigms-of-machine-learning.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
