---
title: "Imitation Learning — Learning by Watching"
subtitle: "How a machine can pick up a skill the same way an apprentice does — by copying a good demonstrator — and why naive copying quietly falls apart."
date: 2026-06-11 09:00:00 -0400
category: "Reinforcement Learning"
slug: imitation-learning
excerpt: "Imitation learning is the part of the machine-learning toolkit closest to how humans actually learn most skills — not from a numerical reward, but from watching someone competent and trying to do the same thing. The simple version (behavior cloning) is famously brittle because small early mistakes compound into trajectories the expert never demonstrated. The fixes (DAgger, GAIL, AIRL, expert iteration) are the rest of the field. This monograph walks through all of it — the idea, the loop, the compounding-error catch, the classical toolkit, modern scale, and where IL actually shows up in production."
reading_time: 22
---

There is a particular kind of machine learning problem where the *learning signal* the algorithm needs is not a reward and not a label — it is a demonstration. A surgeon performing a procedure. A pilot flying a maneuver. A robot operator teleoperating a pick-and-place. A spreadsheet expert reorganizing a model. The thing the human is doing is too rich to specify with a scalar reward, but rich enough that watching the demonstration is enough information for a learner to pick up the skill. This is the domain of **imitation learning**.

The simplest imitation learning algorithm — *behavior cloning* — is exactly what it sounds like. Treat the demonstrator's state-action pairs as a supervised-learning dataset. Train a model that predicts the demonstrator's action given a state. Deploy. This works embarrassingly often. And it fails — sometimes spectacularly — for a reason that's easy to state and hard to fully appreciate: small errors compound. The policy's first wrong action puts it slightly off the demonstrator's distribution. The next state it sees is one the demonstrator never showed it. Its next action is, by definition, untrained. The trajectory diverges. The fix, which the field eventually converged on, is a family of methods — DAgger, GAIL, AIRL, expert iteration — that close the loop between the demonstrator and the deployed policy in different ways. This monograph is the working tour through all of them.

It is the natural companion to the [RL in Agentic AI]({{ '/posts/rl-in-agentic-ai/' | relative_url }}) monograph (imitation learning is the *other* major paradigm for learning policies, and the two are increasingly used together), the [Generalization & Transfer]({{ '/posts/generalization-and-transfer/' | relative_url }}) field guide (imitation learning is, structurally, transfer from the demonstrator's distribution to the learner's distribution), and the [Optimization Methods Reference]({{ '/posts/optimization-methods-reference/' | relative_url }}) (which covers the supervised-learning optimization that behavior cloning rides on).

## What it covers

Ten sections, about twenty-two minutes of careful reading.

**§ 01 — The idea: show, don't reward.** What "learning from demonstration" really means. The expert-learner-environment loop, drawn out. Why this is the closest the ML toolkit comes to how humans actually learn most skills.

**§ 02 — Why bother: when copying beats rewarding.** The two-by-two matrix. Cases where you have a good reward function (use RL). Cases where you have a good demonstrator (use IL). Cases where you have both (use them together, which is what most modern systems do). Cases where you have neither (start over).

**§ 03 — The loop: what the pipeline looks like.** The actual mechanics. Demonstrator collects trajectories. Trajectories become a dataset of state-action pairs. Model trains on the dataset. Model deploys. The four-block diagram that every IL system is some variation on.

**§ 04 — The catch: small mistakes snowball.** The famous failure mode. The compounding-error argument with the actual math. Why behavior cloning's error scales like *O(εT²)* in horizon length T — quadratically, not linearly — and why this is the single most important argument in the entire field.

**§ 05 — The classic toolkit.** The methods that address compounding error. **DAgger** (dataset aggregation — query the expert on the learner's mistakes). **GAIL** (generative adversarial imitation — train a discriminator that distinguishes expert from learner trajectories). **AIRL** (recover the reward function, then run RL on it). **Expert iteration** (improve the demonstrator and the learner in lockstep).

**§ 06 — Modern imitation at scale.** What the toolkit looks like in 2026. Diffusion policies for robotics (the surprise winner of the last two years). Decision transformers for offline IL. Large-scale BC on internet-scraped data (the GPT-of-actions approach). The methods that are working at the scales that matter.

**§ 07 — Beyond action-copying.** The newer ideas. Reward learning from preferences (don't copy actions, learn what the expert *prefers*). Inverse RL as a generalization of imitation (recover the *why* behind the demonstrator's behavior). Skill discovery and hierarchical imitation. Where the field is going.

**§ 08 — Imitation, RL, and offline RL.** The positioning. IL ≠ RL, but they overlap. Offline RL ≠ IL, but they share data sources. The three-way comparison matrix. When each is the right reach.

**§ 09 — Where it actually shows up.** The production applications. Robot manipulation (most modern dexterous-manipulation systems are IL-based or IL-pretrained). Autonomous driving (Waymo's perception-to-action stack has IL throughout). Game playing (AlphaGo's first stage). Code generation (Copilot is, at one level of abstraction, behavior cloning on git history).

**§ 10 — Case study: from a slow optimum to a real-time policy.** A worked example. An optimal-control solver that runs in 100 ms is too slow for real-time deployment. Solution: collect a million state-action pairs from the optimal solver, train a neural network to imitate it, deploy the network at 1 ms. The full pipeline, the gotchas, and the result.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/imitation-learning.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

The field guide lives at its own URL with a warm-paper editorial layout — teal for the *expert*, blue for the *learner*, rust for *drift / compounding error*, amber for *the toolkit's fixes*. Ten sections, color-coded throughout.

---

← Back to [Autonomy]({{ '/' | relative_url }})
