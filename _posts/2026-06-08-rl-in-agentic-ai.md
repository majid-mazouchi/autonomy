---
title: "Reinforcement Learning in Agentic AI"
subtitle: "Where reinforcement learning actually lives inside an AI agent, which algorithms do the work, and how the training loop wraps around a tool-using agent."
date: 2026-06-08 16:00:00 -0400
category: "Reinforcement Learning"
slug: rl-in-agentic-ai
excerpt: "Reinforcement learning shows up inside modern AI agents in two very different places — pre-deployment as a training method that shapes the base model, and at run-time as the policy that selects each next action. The two are constantly confused. This monograph separates them carefully, walks through the algorithms that actually do the work (PPO, GRPO, DPO and their cousins), draws the training loop as an MDP, and lays out the KL leash, the rollout harness, the credit-assignment story, and the dozen things that bite in practice."
reading_time: 28
---

Reinforcement learning is one of the few topics in modern AI engineering where the marketing and the reality have meaningfully diverged. The marketing version — "we used RL to train the model" — is so over-applied that engineers often can't tell which of two completely different things is being claimed: (a) the model was trained with RLHF as part of post-training, or (b) the deployed agent uses RL to select actions at run-time. These are different problems, with different algorithms, different cost profiles, and different failure modes. Confusing them produces a lot of bad architectural decisions.

This monograph is the careful version. It separates the two places RL lives in an agent, walks through the algorithms actually being used in 2026 (PPO and GRPO at training, run-time RL in the smaller class of systems that genuinely earn it), draws the training loop as a proper MDP, and lays out the KL-leash, rollout-harness, credit-assignment, and dozen-other practical considerations that actually decide whether your RL setup converges or thrashes.

This is the first dedicated post on this site in the **Reinforcement Learning** category, so it spends an extra paragraph or two on the foundational concepts that the rest of the category will assume. The natural companion pieces are the [Containment Control]({{ '/posts/containment-control-explained/' | relative_url }}) post (which uses RL-adjacent control-theory ideas in the multi-agent setting), the [Optimization Methods]({{ '/posts/optimization-methods-reference/' | relative_url }}) reference (which is the optimization-foundation underneath both RL training and policy gradient methods), and the [Production Playbook]({{ '/posts/production-playbook/' | relative_url }}) (which addresses RL in the broader scaling discussion).

## What it covers

Twelve sections, about twenty-eight minutes of careful reading.

**§ 01 — Two very different places RL lives.** The single most important distinction. *Training-time RL* shapes a base model (RLHF, DPO, GRPO). *Run-time RL* selects each action of a deployed agent (rare; reserved for cases that actually justify it). Why these are different problems and why confusing them costs.

**§ 02 — Should you even use RL?** The honest decision tree. The cases where supervised fine-tuning is sufficient (most of them). The cases where DPO is sufficient (most of the remainder). The narrow band where actual RL is the right reach.

**§ 03 — The agentic loop, drawn as an MDP.** The textbook Markov Decision Process — state, action, transition, reward — applied to a tool-using agent. State = conversation + tool history. Action = next token / next tool call. Reward = whatever the system gets graded on. The figure that the rest of the monograph builds on.

**§ 04 — Where the reward comes from.** The hard problem. Human ratings. Programmatic graders. Verifiable rewards from execution traces. Why "the reward function is your specification" is the line that bites every team.

**§ 05 — The algorithms, and when each earns its keep.** PPO (the workhorse, 2017–2024). DPO (the supervised-flavored alternative that side-stepped PPO's instability). GRPO (the 2024 group-relative variant that DeepSeek popularized). When each is appropriate.

**§ 06 — The training loop, and the KL leash that keeps it sane.** The forward pass through the policy. The reward computation. The gradient update. The KL divergence penalty against the reference model that prevents the trained model from drifting too far. Why every modern RL training run has a KL leash and what happens when it breaks.

**§ 07 — GRPO and exploration.** The group-relative trick. Why generating multiple candidates and ranking them within a group sidesteps the value-network problem that made PPO so finicky. The empirical evidence for GRPO from the open-weight model literature.

**§ 08 — Token masking & action spaces.** The detail nobody writes down. When the agent's "action" is "emit a token," the action space is enormous. Token masking — restricting what's valid at each step — is the difference between a trainable setup and one that thrashes.

**§ 09 — The rollout harness.** The training infrastructure. How you generate rollouts at scale, what you log, how you handle truncation, how you replay traces for debugging.

**§ 10 — Credit assignment & the horizon.** The classic RL problem in the LLM setting. Which token in a 1000-token response was responsible for the final reward? The discount factor. The advantage estimator. Why long horizons remain hard.

**§ 11 — When rewards go wrong.** Reward hacking. Specification gaming. The 2025 examples from the open literature. The defensive techniques (red-teaming the reward, adversarial evaluation, the KL leash itself as a guardrail).

**§ 12 — Practical notes & structures.** The hard-won field observations. Start with DPO, not PPO. Always log the KL. Watch the reward-mean and reward-variance together. The handful of habits that compound.

**References & further reading.** The PPO paper (Schulman 2017). The DPO paper (Rafailov 2023). The GRPO paper (Shao 2024). The Anthropic and DeepSeek technical reports. The open-source training-stack documentation (TRL, OpenRLHF, vLLM serving).

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/rl-in-agentic-ai.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-paper layout — rust accent for the agentic-AI material, teal for the algorithmic detail, ochre for the practical-notes sections. Twelve sections plus diagrams you can poke at.

---

← Back to [Autonomy]({{ '/' | relative_url }})
