---
title: "Practical RL Engineering: Hyperparameters, Debugging, and Silent Failures"
subtitle: "The universal defaults, the debugging order, and the traps that eat weekends — the pragmatic pages of the field guide."
date: 2026-04-20 23:00:00 -0400
category: "Reinforcement Learning"
slug: rl-practical-engineering-hyperparameters-debugging
excerpt: "The most pragmatic post in the field guide — the hyperparameters that almost always work, the order to debug a policy that won't learn, and the silent failures that cost days because nothing crashes. Keep this one near your monitor."
reading_time: 10
---

This is the practical-engineering post in the [field guide to reinforcement learning for control and robotics]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }}). Unlike the rest of the series — which walks through [MDPs]({{ '/posts/rl-foundations-mdps-value-functions-bellman/' | relative_url }}), [TD learning]({{ '/posts/rl-td-sarsa-q-learning/' | relative_url }}), [policy gradients]({{ '/posts/rl-policy-gradients-actor-critic/' | relative_url }}), [the modern toolkit]({{ '/posts/rl-exploration-sac-ppo-td3-ddpg/' | relative_url }}), [model-based methods]({{ '/posts/rl-model-based-mpc-hybrids/' | relative_url }}), and [robotics practice]({{ '/posts/rl-robotics-sim-to-real-offline-safe/' | relative_url }}) — this one is purely operational. Three lists. No math. No widgets. Keep it near your monitor.

The three lists in this post replace a lot of the folklore that RL practitioners pass between each other verbally at conferences. Most of the content I could have written 1,000 words of narrative around; I've deliberately kept them terse because when your policy isn't learning at 2 a.m., what you need is a checklist, not prose.

## Hyperparameters that almost always work

The universal deep-RL defaults. Start here; only deviate when you have evidence you should.

- **Adam lr = 3e-4** for actor, critic, and temperature. The universal deep-RL learning rate.
- **γ = 0.99** unless your task horizon is much shorter or much longer than 100 steps.
- **GAE λ = 0.95** for PPO. Essentially never tune this.
- **PPO clip = 0.2**, 10 epochs per rollout, batch size 64. The paper's defaults.
- **SAC auto-α with target entropy = −dim(A)**. Replaces a painful hyperparameter with a near-free one.
- **Polyak τ = 0.005** for all target networks.
- **Replay buffer size = 1M** for most off-policy methods.
- **Network architecture:** 2 hidden layers, 256 units, ReLU (or tanh for PPO). Rarely needs anything more exotic for proprioceptive control.

These are starting values. They win about 80% of the time without any tuning, and when they lose, the fix is almost never "find a better learning rate" — it's somewhere in the next two sections.

## Debugging when your policy doesn't learn

The order to investigate when your policy isn't learning — roughly in descending order of how often the issue lies there. Work through this list top-to-bottom; do not skip ahead. A remarkable number of "the algorithm is broken" moments turn out to be item 1 or 2.

1. **Check the reward, not the algorithm.** Log every reward component separately. Sanity-check that a hand-crafted good trajectory receives higher cumulative reward than a bad one. If it doesn't, stop — fix the reward.
2. **Normalize observations.** Running mean/std. If one observation has magnitude 1000 and another 0.01, your network is effectively ignoring the small one.
3. **Scale actions to $[-1, 1]$.** Always. Unscaled action spaces are one of the top three learning-failure causes.
4. **Verify the environment.** Run a random policy and a hand-coded policy. Confirm returns differ in the right direction. Confirm episode termination works.
5. **Test on a trivial version.** Zero out randomization, fix initial states, shrink the task. If it won't learn the easy version, nothing will fix the hard one.
6. **Check exploration.** For PPO/SAC, plot policy entropy over training. Collapse to near-zero early means premature convergence.
7. **Gradient norms.** If they explode ($>10$) or vanish ($<10^{-6}$), stop and investigate.

If you've worked through all seven and the policy still isn't learning, the problem is almost certainly in the next list — a silent failure that isn't producing any of the obvious symptoms.

## Traps that ate my weekend (and will eat yours)

The silent failures. These are the ones that cost days because nothing *crashes* — the policy just underperforms for reasons that aren't obviously wrong. Every one of these has happened to someone I know, and most of them have happened to me.

1. **Forgetting the tanh Jacobian correction in SAC.** Log-probs will be wrong, entropy estimates wrong, auto-α tuning garbage. Silent failure.
2. **Not normalizing observations.** Policy converges to a suboptimal local minimum; you blame the algorithm.
3. **Shared vs separate actor/critic networks.** For continuous control with proprioception, *separate*. Sharing hurts when the critic needs different features than the actor.
4. **Episode time limits leaking into the MDP.** Truncation ≠ termination. You need to bootstrap at timeout rather than using terminal value 0. Gymnasium gives you this signal — use it.
5. **Reward scaling mismatch across terms.** Tracking error $\mathcal{O}(1)$ + action penalty $\mathcal{O}(0.01)$ + sparse bonus $\mathcal{O}(100)$ → the sparse bonus drowns everything. Balance and normalize.
6. **Deterministic eval rollout ≠ training rollout.** Your training return looks great but eval performance is bad because noise schedules, randomization, or termination conditions differ.
7. **Running domain randomization before the policy works in nominal sim.** The policy can't learn because it can't see consistency. Train nominal first, then widen.
8. **Using $\gamma = 1$ with time limits.** Return diverges or becomes undefined; value estimates are nonsense. Use $\gamma < 1$ or proper terminal-value handling.
9. **Not logging rollout videos.** You will spend days debugging a reward function that a 10-second video would have explained instantly.

## How to use these three lists

My rough workflow when starting a new RL project, distilled from making every one of the mistakes above:

- **Before I write code**: skim the hyperparameter list. Use those defaults. Don't tune yet.
- **When the policy first trains**: skim the silent-failures list and verify I'm not hitting any of them. In particular: tanh Jacobian correction, observation normalization, truncation vs termination, reward-term scale balance. Five minutes of checking saves five days of confusion.
- **When the policy isn't learning**: work through the debugging list top to bottom. Don't skip. The most common "the algorithm doesn't work" post on forums is someone who jumped to step 7 (gradient norms) and never went back to check step 1 (the reward).

Over time the lists stop being lists and become muscle memory. Until then, they're checklists — and checklists beat memory on the kind of detail-oriented mistakes RL punishes most harshly.

---

← Back to [the field guide]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }})
