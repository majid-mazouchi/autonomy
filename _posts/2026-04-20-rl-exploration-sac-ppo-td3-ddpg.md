---
title: "Exploration and Modern Deep RL: SAC, PPO, TD3, DDPG"
subtitle: "The exploration-exploitation trade-off, Boltzmann and bandit strategies, and the four algorithms that dominate continuous control."
date: 2026-04-20 17:00:00 -0400
category: "Reinforcement Learning"
slug: rl-exploration-sac-ppo-td3-ddpg
excerpt: "Every RL algorithm is secretly two algorithms sharing a body — one that exploits what it knows, one that explores for what it doesn't. This post covers the exploration methods that actually work and the four deep RL algorithms (SAC, PPO, TD3, DDPG) that define modern continuous control."
reading_time: 22
---

This is Post 5 in the [field guide to reinforcement learning for control and robotics]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }}), and it's the one where the theory cashes out into the algorithms you'll actually use. The previous posts built up the machinery — [MDPs and Bellman]({{ '/posts/rl-foundations-mdps-value-functions-bellman/' | relative_url }}), [TD learning]({{ '/posts/rl-td-sarsa-q-learning/' | relative_url }}), [policy gradients]({{ '/posts/rl-policy-gradients-actor-critic/' | relative_url }}). Here we assemble those pieces into **SAC, PPO, TD3, DDPG** and, along the way, settle the exploration question that every one of them has to answer.

Every RL algorithm is secretly two algorithms sharing a body: one that *exploits* what it already knows, and one that *explores* to learn more. Getting that balance wrong is the single most common failure mode I see — and the reason many "RL didn't work" stories are really "exploration didn't work" stories in disguise.

## Why exploration is genuinely hard

In a bandit, pulling an arm costs nothing beyond a suboptimal step. In a sequential problem, exploration has to *traverse a state space* to even reach the places where learning would be useful. A randomly acting humanoid will never stumble into a walking gait. A randomly acting chess engine will never reach the endgame. This is why deep RL folklore is full of environments — Montezuma's Revenge, sparse-reward manipulation, robot locomotion from scratch — where vanilla ε-greedy fails catastrophically.

The practical taxonomy of exploration methods breaks into three families:

- **Action-space noise** — perturb the chosen action (ε-greedy, Boltzmann, Gaussian, Ornstein-Uhlenbeck).
- **Parameter-space noise** — perturb the policy parameters themselves (NoisyNets, parameter-space noise, evolution strategies).
- **Intrinsic motivation** — add a bonus reward for novelty (count-based, ICM, RND, disagreement).

I'll walk through each. Then we'll watch two of them run in interactive widgets, and finish with the four deep RL algorithms you actually ship.

## ε-greedy — the blunt instrument that works

With probability $\varepsilon$ pick a uniform random action; otherwise pick the greedy one. Simple, trivially implementable, and surprisingly effective for most discrete-action problems. The standard recipe:

```python
eps = max(eps_end, eps_start - (eps_start - eps_end) * step / decay_steps)
action = argmax_a Q(s, a) if random() > eps else randint(0, n_actions)
```

Standard schedule: linear anneal from 1.0 down to 0.05 or 0.01 over the first 10% of training steps. This is exactly what DQN uses on Atari. The mechanics look crude but they succeed because the function approximator itself generalizes — you don't need to visit every state, only enough to shape the value landscape.

Where ε-greedy fails: sparse-reward long-horizon tasks where the reward is never reached by a random walk, and continuous-action problems where "random action" is not a meaningful primitive. For the second, Gaussian noise on top of a deterministic policy is the continuous analog (DDPG, TD3).

## Softmax / Boltzmann exploration

Instead of a hard greedy-random split, sample actions proportionally to a softmax of their Q-values, with a temperature $\tau$ controlling the sharpness:

$$ \pi(a \mid s) \;=\; \frac{\exp\!\bigl(Q(s,a)/\tau\bigr)}{\sum_{a'} \exp\!\bigl(Q(s,a')/\tau\bigr)} $$

The two limits tell the whole story:

- $\tau \to 0$ — probability mass collapses onto the argmax. Pure exploitation.
- $\tau \to \infty$ — distribution becomes uniform. Pure exploration.

The appeal over ε-greedy is that Boltzmann exploration *respects the Q-values*: a clearly-bad action gets almost no weight, a close-call action gets nontrivial weight. The downside is that $\tau$ is harder to tune than $\varepsilon$ because it is unitless with respect to the Q-scale — doubling all Q-values halves the effective temperature.

Slide $\tau$ below and watch the probability distribution concentrate or spread. Orange bars are the Q-values for six hypothetical actions. Blue bars are the resulting policy probabilities.

<div class="rl-widget rl-softmax">

  <div class="rl-w-head">
    <div class="rl-w-title">Interactive — softmax temperature explorer</div>
    <div class="rl-w-tag">Boltzmann policy</div>
  </div>

  <div class="rl-w-body">
    <div class="rl-w-ctrls">
      <div class="rl-w-ctrl">
        <label>Temperature τ <span class="val" id="tempVal">1.00</span></label>
        <input type="range" id="tempSlider" min="-2.3" max="2.3" step="0.05" value="0">
      </div>
      <div class="rl-w-ctrl">
        <label>Entropy H[π] / H_max <span class="val" id="entVal">—</span></label>
      </div>
      <div class="rl-w-ctrl">
        <label>P(argmax action) <span class="val" id="pmaxVal">—</span></label>
      </div>
    </div>

    <canvas id="softmaxCanvas" class="rl-w-canvas" height="260"></canvas>

    <div class="rl-w-actions">
      <button type="button" class="rl-btn ghost" id="randomQ">Randomize Q</button>
    </div>
  </div>

  <div class="rl-w-foot">
    Orange = Q-values. Blue = softmax probabilities. τ = 1.0 is the natural scale; τ → 0 collapses to greedy; τ → ∞ goes uniform. Entropy is normalized to log(n) so you can read off "how uniform" on the [0, 1] scale.
  </div>
</div>

## UCB, Thompson sampling, and the bandit view

Before sequential RL, there was the multi-armed bandit — an MDP with one state. All the exploration intuitions are cleaner there. The three families that matter:

- **ε-greedy** — pick greedy most of the time, random otherwise. Wastes exploration on arms it already knows are bad.
- **UCB** — "upper confidence bound," picks $\arg\max_a[\,\hat Q_a + c\sqrt{\ln t / N_a}\,]$. The bonus term boosts untried or rarely-tried actions. Provably logarithmic regret in stationary bandits, which is why theorists love it.
- **Thompson sampling** — maintain a posterior over each arm's value, draw one sample per arm, pick the arm whose sample is highest. Bayesian-optimal on average. Usually best in practice despite weaker worst-case bounds.

The widget below runs all three on the same 10-armed bandit instance. The **best arm has mean reward 1.0**; the other nine are drawn uniformly from $[0, 1)$. Each curve plots cumulative regret — how much reward each strategy gave up by not always pulling the optimum. Lower is better, and a flatter curve means the strategy has converged.

<div class="rl-widget rl-bandit">

  <div class="rl-w-head">
    <div class="rl-w-title">Interactive — exploration strategies on a 10-arm bandit</div>
    <div class="rl-w-tag">Compare</div>
  </div>

  <div class="rl-w-body">
    <div class="rl-w-ctrls">
      <div class="rl-w-ctrl">
        <label>Horizon <span class="val" id="banditHVal">500</span> pulls</label>
        <input type="range" id="banditHSlider" min="100" max="2000" step="100" value="500">
      </div>
      <div class="rl-w-ctrl">
        <label>ε (for ε-greedy) <span class="val" id="banditEps">0.10</span></label>
        <input type="range" id="banditEpsSlider" min="0" max="50" value="10">
      </div>
    </div>

    <canvas id="banditCanvas" class="rl-w-canvas" height="280"></canvas>

    <div class="rl-w-actions">
      <button type="button" class="rl-btn primary" id="banditRunBtn">▶ Run</button>
      <button type="button" class="rl-btn ghost" id="banditNewBtn">New arm set</button>
    </div>
  </div>

  <div class="rl-w-foot">
    Cumulative regret — the reward foregone by not always pulling the best arm. UCB converges with provable guarantees; Thompson is often Bayesian-optimal on average; ε-greedy is the simplest thing that works. Run it a few times on different arm sets to see how sensitive each is to the draw.
  </div>
</div>

### What the bandit teaches about deep RL exploration

These three strategies have direct analogs in deep RL:

- **ε-greedy** — used verbatim in DQN because it's trivial to implement. Wasteful, but function approximation partially hides the cost.
- **UCB** — rarely used verbatim in deep RL (no clean $N(s,a)$ with function approximation), but inspires **count-based exploration bonuses** and the PUCT formula in AlphaZero.
- **Thompson sampling** — the spiritual ancestor of **bootstrapped DQN** (maintain $K$ Q-heads trained on different bootstrap samples, pick one head per episode, act greedy wrt it).
- **Entropy regularization** — SAC's approach, where exploration is built into the *objective* rather than bolted on. Reward for being uncertain.

## Entropy regularization — exploration as part of the objective

Modern policy-gradient and actor-critic methods embed exploration directly into the objective by rewarding policy entropy:

$$ J(\pi) \;=\; \mathbb{E}_\pi\!\left[\sum_t r_t \;+\; \alpha\, H\!\bigl(\pi(\cdot \mid s_t)\bigr)\right] $$

This is what SAC does (with $\alpha$ auto-tuned to maintain a target entropy) and what PPO does (with a fixed coefficient, typically $0.0$ — $0.01$). Entropy regularization is elegant because it makes exploration an *optimization target* rather than a hack — the policy becomes as stochastic as it can be while still earning reward. On well-shaped continuous-control tasks, entropy bonus alone is enough exploration to reach state-of-the-art.

## Parameter-space noise and intrinsic motivation — the heavy weapons

**Parameter-space noise.** Instead of perturbing actions, perturb the policy's parameters. Two variants: *parameter-space noise* (add Gaussian noise to the policy weights, held constant per rollout, scale adapted to keep action-space divergence near a target) and *NoisyNets* (replace linear layers with $y = (\mu_w + \sigma_w \odot \epsilon_w) x + (\mu_b + \sigma_b \odot \epsilon_b)$ — the network learns how much noise it needs where). Both produce *temporally consistent* exploration: the policy commits to a perturbation for a while rather than flicking randomly every step, which is crucial in environments where useful behavior requires several correlated actions in sequence.

**Intrinsic motivation.** When extrinsic reward is sparse, add a bonus for novelty. Three canonical designs worth knowing:

- **Count-based / pseudo-counts** — $r^{\text{int}}_t \propto 1/\sqrt{N(s_t)}$. Trivially correct for tabular problems; for continuous or image state, use density models to produce *pseudo-counts*.
- **ICM — Intrinsic Curiosity Module** — learn a forward model $\hat s_{t+1} = f_\phi(s_t, a_t)$ in a feature space; the intrinsic reward is the prediction error. The clever move is using an *inverse*-dynamics loss to learn the feature space, so only controllable variation gets encoded. Stops the agent from being fascinated by random TV static.
- **RND — Random Network Distillation** — fix a random target network $f_{\bar\theta}$; train a predictor $\hat f_\phi$ to match it. Prediction error on new states is the bonus. Surprisingly, this tiny idea dominated Montezuma's Revenge.

> **Be careful with the reward ratio.** Intrinsic bonuses must be scaled to a small fraction of the eventual extrinsic reward — typically $0.01\times$ to $0.1\times$ — or the agent will chase novelty forever and never solve the actual task. Common pattern: normalize the intrinsic reward by a running std, then scale by a fixed small coefficient.

## Choosing an exploration strategy, in order

1. **Is your reward dense and informative?** Use entropy regularization (SAC / PPO default) and stop thinking about it.
2. **Discrete actions, moderately shaped reward?** ε-greedy with a decay schedule — linear from 1.0 → 0.05 over 10% of training.
3. **Continuous actions, moderate shaping?** Gaussian or tanh-squashed Gaussian on the policy output (SAC does this automatically).
4. **Sparse but reachable reward?** NoisyNets or parameter-space noise for temporally consistent exploration.
5. **Sparse and hard to reach?** Add RND or ICM intrinsic bonus. Tune the coefficient carefully.
6. **Extremely sparse, long-horizon?** Consider imitation learning, curriculum, or hierarchical RL *before* touching exploration bonuses.

> **Rule of thumb.** If your agent isn't learning, first confirm that a random policy ever sees a positive reward signal. If it doesn't, you have a reward-design problem, not an exploration problem — no amount of RND will save you. Shape the reward first, bonus the exploration second.

## Modern deep RL for continuous control

With exploration squared away, the algorithms. If you're picking something for a manipulator, a mobile base, or a motor-control task, 95% of the time it's one of these four — or a model-based method that uses one of them as its policy class. Read them in order; each one fixes the prior's problems.

### DDPG — Deep Deterministic Policy Gradient

The first widely-used deep RL method for continuous control (Lillicrap et al., 2015). Think of it as "DQN with a deterministic actor." You learn a deterministic policy $\mu_\theta(s)$ and a critic $Q_\phi(s, a)$. The actor is trained by pushing $\mu$ in the direction that increases $Q$ — literally, $\nabla_\theta Q_\phi(s, \mu_\theta(s))$.

**How it works.** Replay buffer and target networks inherited from DQN. Actor loss $-\mathbb{E}_s[Q_\phi(s, \mu_\theta(s))]$ — maximize the critic's estimate. Critic loss: standard TD error, with the next action being $\mu_{\theta^-}(s')$ from the target actor. Exploration: Ornstein-Uhlenbeck or Gaussian noise added to $\mu(s)$ at runtime.

**Why you probably shouldn't use it.** DDPG is *notoriously* fragile. It overestimates Q-values catastrophically and is hypersensitive to hyperparameters, network initialization, and reward scale. Two identical runs with different seeds often diverge. Everything that makes it bad was fixed in TD3 and SAC. Use it only as a pedagogical baseline or if you have very specific reasons.

In 2026, DDPG is essentially never the right choice — TD3 is strictly better and a `git diff` away. The only reason to mention DDPG is to understand why TD3 and SAC exist.

### TD3 — Twin Delayed DDPG

Fujimoto et al. (2018) made DDPG work with three surgical fixes. Each one addresses a specific failure mode; together they produce a solid deterministic-policy baseline.

1. **Clipped double Q-learning** — train two critics $Q_{\phi_1}, Q_{\phi_2}$ and use $\min(Q_1, Q_2)$ in the target. Cures the overestimation bias that plagues DDPG.
2. **Delayed policy updates** — update the actor (and targets) every two critic updates. Lets the critic stabilize before the actor chases it.
3. **Target policy smoothing** — add clipped noise to the target action: $a' = \mu_{\theta^-}(s') + \text{clip}(\epsilon, -c, c)$. Regularizes the Q-landscape and prevents the actor from exploiting critic errors.

**Hyperparameters that matter.** Actor lr = critic lr = 3e-4, almost always. Batch size 256. Polyak τ = 0.005. Target smoothing noise 0.2, noise clip 0.5. Policy delay of 2 actor updates per 2 critic updates. Runtime exploration noise σ = 0.1 Gaussian on the action.

TD3 is a great default when you want a *deterministic* policy — for safety certification, control-theoretic analysis, or behavioral-cloning initialization. Otherwise, SAC is usually a better choice: often more sample-efficient and robust to hyperparameters.

### SAC — Soft Actor-Critic *(robotics default)*

Haarnoja et al. (2018) took the actor-critic template and added a maximum-entropy objective. The agent maximizes expected return *plus* a bonus for policy entropy:

$$ J(\pi) = \mathbb{E}_{\tau \sim \pi}\!\left[\sum_t r_t + \alpha\, H(\pi(\cdot \mid s_t))\right] $$

This single change makes SAC dramatically more robust and sample-efficient than TD3/DDPG, and it's the current default for most continuous-control robotics work.

**Why the entropy term is magical.**

- The policy is *automatically* stochastic — no hand-tuned exploration noise schedule.
- Exploration is concentrated where the agent is uncertain about action value, not blanket-random.
- The policy is multi-modal when needed: if several actions are equally good, it assigns probability to all of them.
- It smooths the value landscape, making optimization easier.

**Auto-tuning α (the critical trick).** The original SAC had a fixed $\alpha$. The v2 paper introduced *auto-tuning*: solve a constrained optimization that keeps entropy near a target $\bar H$ (typically $-\dim(A)$). This removes the single most annoying hyperparameter and makes SAC nearly tune-free across environments. **Always use auto-α.**

**Canonical hyperparameters — these usually just work:**

```python
# SAC defaults — from the paper and stable-baselines3
lr           = 3e-4      # actor, critic, alpha all the same
batch_size   = 256
gamma        = 0.99
tau          = 0.005     # Polyak averaging for target critics
buffer_size  = 1_000_000
target_entropy = -dim(A) # auto-α tuning
# Squash policy output with tanh, remember the Jacobian correction
# Use twin critics; take the min in the target
# Normalize observations; normalize or scale rewards
```

**The silent-failure gotchas.** Reward scaling has an outsized effect even with auto-α — rescale rewards to roughly unit variance. Observation normalization (running mean/std) is critical for proprioceptive observations with varying scales. Use twin critics (as in TD3); minimum over the two is the target. And — this one ate my weekend — **don't forget the tanh Jacobian correction on log-probs**, or entropy estimates and auto-α go silently to garbage.

If you're starting an RL project in continuous control and you don't have a strong reason to pick something else: **use SAC with auto-α**. It's the most forgiving algorithm and works well across a surprising range of tasks with minimal hyperparameter search.

### PPO — Proximal Policy Optimization *(simulation default)*

Schulman et al. (2017) gave us the workhorse of industrial on-policy RL. PPO is what OpenAI used for Dota, what DeepMind used for locomotion, what most robotics groups use in Isaac Gym and MuJoCo. Robust, parallelizable, and the hyperparameters transfer well across tasks.

We covered the clipped surrogate loss in [the policy-gradients post]({{ '/posts/rl-policy-gradients-actor-critic/' | relative_url }}); briefly, the update maximizes:

$$ L^{\text{CLIP}}(\theta) = \mathbb{E}_t\!\left[ \min\bigl(r_t(\theta)\hat A_t,\; \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\,\hat A_t\bigr) \right] $$

with $r_t(\theta) = \pi_\theta(a_t \mid s_t) / \pi_{\theta_{\text{old}}}(a_t \mid s_t)$ and $\epsilon = 0.2$. The clip prevents the policy from moving too far per update. That's it. No KL constraint, no conjugate gradient, just clamp the ratio and SGD.

**Why PPO is so popular.** Massively parallel — run hundreds or thousands of environments in parallel (perfect for GPU-accelerated sims like Isaac Gym), batch transitions, update. Robust to hyperparameters, so you rarely need to tune — which matters when you're iterating on reward design rather than algorithms. Strong GAE synergy, with GAE($\lambda = 0.95$) as the standard advantage estimator. No target networks, no replay buffer — simpler to implement and debug than off-policy methods.

**Canonical hyperparameters — the ones everyone uses:**

```python
lr            = 3e-4
n_steps       = 2048     # per env, per update
n_envs        = 16-4096  # more is better if you have the sim
batch_size    = 64
n_epochs      = 10       # epochs per rollout
gamma         = 0.99
gae_lambda    = 0.95
clip_range    = 0.2
ent_coef      = 0.0      # raise to 0.01 for more exploration
vf_coef       = 0.5
max_grad_norm = 0.5
# orthogonal init, tanh activations — a small but real win
```

**Implementation gotchas — the "37 details" list is real.** Advantage normalization (zero mean, unit std per batch) is non-optional. Observation normalization with running statistics is non-optional. Reward clipping or scaling to roughly $[-10, 10]$ — PPO is very sensitive to reward magnitude. Orthogonal weight init with a small gain on the policy head, gain 1 on the critic head. Value-function clipping (same clip as policy) is standard, though debatable. For vision-based RL share the network; for proprioceptive control use separate actor and critic.

If you have a fast simulator (hundreds of thousands of steps/sec), **use PPO** with many parallel envs. If you have slow data collection (real robot, expensive sim), **use SAC** for sample efficiency. This single heuristic picks the right algorithm roughly 90% of the time.

### TRPO — Trust Region Policy Optimization

Briefly, for the historical record. The predecessor to PPO — TRPO (Schulman et al., 2015) enforces a hard constraint on the KL divergence between successive policies, $D_{\text{KL}}(\pi_{\text{old}} \| \pi_\theta) \le \delta$, solved via conjugate gradient and line search. It's worth knowing for the theory (it's the algorithm that justified the "trust region" intuition) but is rarely the right production choice. Second-order optimization is complicated to implement correctly, and PPO's clip achieves similar trust-region behavior with first-order SGD. If you want hard KL constraints with modern implementations, look at *KL-regularized PPO* or *MPO*.

## At-a-glance comparison

| Algorithm | Policy | On/off-policy | Best for | Watch out for |
|---|---|---|---|---|
| **DDPG** | Deterministic | Off | Historical interest only | Use TD3 instead |
| **TD3** | Deterministic | Off | Continuous control where deterministic is required | Less robust than SAC |
| **SAC** | Stochastic (Gaussian) | Off | Real-robot data efficiency, most robotics | Tanh Jacobian correction; reward scaling |
| **PPO** | Stochastic (any) | On | Fast simulators, massive parallelism | The 37 implementation details |
| **TRPO** | Stochastic | On | Pedagogical / theoretical interest | Second-order complexity; use PPO |

## What's actually changing as you go down this list

Step back and look at what changes between algorithms. DDPG → TD3 is **three stability fixes**. TD3 → SAC is **stochastic policy plus entropy regularization**. SAC → PPO is **off-policy to on-policy** (same idea, different data regime). At each step, something specific gets addressed. You can often *anticipate* which algorithm you want by asking "which failure mode am I worried about?" rather than memorizing them.

- **Worried about Q-value overestimation?** Twin critics (TD3, SAC have these).
- **Worried about brittle hyperparameters?** Entropy regularization (SAC).
- **Worried about sample efficiency on expensive data?** Off-policy with replay (TD3, SAC).
- **Worried about massive parallelism across sims?** On-policy, no replay (PPO).
- **Need a deterministic policy for deployment?** TD3.
- **Don't know?** SAC.

---

The algorithms above handle roughly 90% of continuous-control problems you'll encounter. The remaining 10% — where dynamics are expensive to sample and you can learn a model of them — is the domain of model-based RL and MPC hybrids. That's the [next post]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }}) in the series.

← Back to [the field guide]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }})

<!-- =====================================================
     Post-scoped styles — two widgets on this page
     ===================================================== -->
<style>
  .article-body .rl-widget {
    max-width: var(--read);
    margin: 32px auto;
    background: var(--paper-2);
    border: 1px solid var(--rule);
    border-radius: 4px;
    overflow: hidden;
  }
  .article-body .rl-w-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    padding: 14px 20px;
    border-bottom: 1px solid var(--rule);
    background: var(--paper);
  }
  .article-body .rl-w-title {
    font-family: var(--f-ui);
    font-size: .78rem;
    letter-spacing: .08em;
    text-transform: uppercase;
    color: var(--ink);
  }
  .article-body .rl-w-tag {
    font-family: var(--f-ui);
    font-size: .62rem;
    letter-spacing: .14em;
    text-transform: uppercase;
    color: var(--accent);
    padding: 3px 8px;
    border: 1px solid var(--accent);
    border-radius: 2px;
    white-space: nowrap;
  }
  .article-body .rl-w-body { padding: 20px; }

  .article-body .rl-w-ctrls {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 14px 22px;
    margin: 0 0 14px;
  }
  .article-body .rl-w-ctrl label {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-family: var(--f-ui);
    font-size: .72rem;
    letter-spacing: .04em;
    color: var(--ink-soft);
    margin: 0 0 6px;
  }
  .article-body .rl-w-ctrl label .val {
    color: var(--ink);
    font-variant-numeric: tabular-nums;
    font-weight: 500;
  }
  .article-body .rl-widget input[type="range"] {
    -webkit-appearance: none;
    appearance: none;
    width: 100%;
    height: 3px;
    background: var(--rule);
    border-radius: 2px;
    outline: none;
    margin: 4px 0 0;
  }
  .article-body .rl-widget input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 15px; height: 15px;
    background: var(--accent);
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid var(--paper-2);
    box-shadow: 0 0 0 1px var(--accent);
  }
  .article-body .rl-widget input[type="range"]::-moz-range-thumb {
    width: 13px; height: 13px;
    background: var(--accent);
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid var(--paper-2);
    box-shadow: 0 0 0 1px var(--accent);
  }

  .article-body .rl-w-canvas {
    display: block;
    width: 100%;
    background: var(--paper);
    border: 1px solid var(--rule);
    border-radius: 2px;
  }

  .article-body .rl-w-actions {
    display: flex;
    gap: 8px;
    margin: 14px 0 0;
    flex-wrap: wrap;
  }
  .article-body .rl-btn {
    font-family: var(--f-ui);
    font-size: .74rem;
    letter-spacing: .06em;
    text-transform: uppercase;
    border: 1px solid var(--rule);
    padding: 9px 14px;
    cursor: pointer;
    border-radius: 2px;
    background: var(--paper);
    color: var(--ink);
    transition: background .15s ease, color .15s ease, border-color .15s ease;
  }
  .article-body .rl-btn:hover {
    border-color: var(--ink-mute);
    background: var(--paper-2);
  }
  .article-body .rl-btn.primary {
    background: var(--accent);
    color: var(--paper);
    border-color: var(--accent);
    font-weight: 500;
  }
  .article-body .rl-btn.primary:hover { filter: brightness(0.93); }
  .article-body .rl-btn.ghost {
    background: transparent;
    color: var(--ink-mute);
  }

  .article-body .rl-w-foot {
    font-family: var(--f-body);
    font-size: .86rem;
    font-style: italic;
    color: var(--ink-mute);
    padding: 12px 20px;
    border-top: 1px solid var(--rule);
    background: var(--paper);
    line-height: 1.55;
  }
</style>

<script>
/* ====================================================================
   Widget 1 — Boltzmann / softmax temperature explorer
   ==================================================================== */
(function() {
  var cv = document.getElementById('softmaxCanvas');
  if (!cv) return;
  var ctx = cv.getContext('2d');
  var widget = cv.closest('.rl-widget');

  function cvar(name, fallback) {
    var v = getComputedStyle(widget).getPropertyValue(name).trim();
    return v || fallback;
  }
  function parseHex(hex, fallback) {
    var m = hex.match(/^#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i);
    if (!m) return fallback;
    return [parseInt(m[1], 16), parseInt(m[2], 16), parseInt(m[3], 16)];
  }

  var Q = [0.8, 0.2, 0.6, 0.9, 0.1, 0.4];
  var N_ACTIONS = Q.length;

  function randomizeQ() {
    for (var i = 0; i < N_ACTIONS; i++) Q[i] = Math.random();
    draw();
  }

  function softmax(qs, tau) {
    var scaled = qs.map(function(q) { return q / Math.max(tau, 1e-6); });
    var maxV = Math.max.apply(null, scaled);
    var exps = scaled.map(function(s) { return Math.exp(s - maxV); });
    var sum = exps.reduce(function(a, b) { return a + b; }, 0);
    return exps.map(function(e) { return e / sum; });
  }

  function entropy(probs) {
    var h = 0;
    for (var i = 0; i < probs.length; i++) {
      if (probs[i] > 1e-12) h -= probs[i] * Math.log(probs[i]);
    }
    return h;
  }

  function resize() {
    var rect = cv.getBoundingClientRect();
    var dpr = window.devicePixelRatio || 1;
    cv.width = rect.width * dpr;
    cv.height = 260 * dpr;
    cv.style.height = '260px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    draw();
  }

  function draw() {
    var rect = cv.getBoundingClientRect();
    var W = rect.width, H = 260;

    var paper = cvar('--paper', '#f4efe6');
    var rule = cvar('--rule', '#c8bfae');
    var ink = cvar('--ink', '#1a1814');
    var inkMute = cvar('--ink-mute', '#8a8277');
    var accent = cvar('--accent', '#b94a1b');

    // Secondary color for policy bars — steel blue to contrast warm Q bars
    var policyColor = '#4d6a8f';

    ctx.fillStyle = paper;
    ctx.fillRect(0, 0, W, H);

    var logTau = parseFloat(document.getElementById('tempSlider').value);
    var tau = Math.exp(logTau);
    document.getElementById('tempVal').textContent = tau.toFixed(2);

    var probs = softmax(Q, tau);
    var hMax = Math.log(N_ACTIONS);
    var h = entropy(probs);
    document.getElementById('entVal').textContent = (h / hMax).toFixed(2);

    var pmax = Math.max.apply(null, probs);
    document.getElementById('pmaxVal').textContent = pmax.toFixed(2);

    var padL = 40, padR = 18, padT = 20, padB = 36;
    var plotW = W - padL - padR;
    var plotH = H - padT - padB;

    // Grid
    ctx.strokeStyle = rule;
    ctx.lineWidth = 0.5;
    for (var g = 0; g <= 4; g++) {
      var gy = padT + plotH * g / 4;
      ctx.beginPath();
      ctx.moveTo(padL, gy);
      ctx.lineTo(W - padR, gy);
      ctx.stroke();
    }

    // Y-axis labels
    ctx.fillStyle = inkMute;
    ctx.font = '10px "DM Mono", ui-monospace, monospace';
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    for (var g2 = 0; g2 <= 4; g2++) {
      var yv = 1 - g2 / 4;
      var gy2 = padT + plotH * g2 / 4;
      ctx.fillText(yv.toFixed(1), padL - 6, gy2);
    }

    // Bars: for each action, draw Q (left half) and π (right half)
    var groupW = plotW / N_ACTIONS;
    var barW = groupW * 0.35;
    var gapHalf = groupW * 0.05;

    for (var a = 0; a < N_ACTIONS; a++) {
      var xCenter = padL + groupW * (a + 0.5);

      // Q bar (orange) — left
      var qH = plotH * Q[a];
      ctx.fillStyle = accent;
      ctx.fillRect(xCenter - barW - gapHalf, padT + plotH - qH, barW, qH);

      // π bar (blue) — right
      var pH = plotH * probs[a];
      ctx.fillStyle = policyColor;
      ctx.fillRect(xCenter + gapHalf, padT + plotH - pH, barW, pH);

      // Action label
      ctx.fillStyle = inkMute;
      ctx.font = '10px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';
      ctx.fillText('a' + a, xCenter, padT + plotH + 6);
    }

    // Legend
    ctx.font = '10px "DM Mono", ui-monospace, monospace';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'middle';

    var legY = H - 14;
    ctx.fillStyle = accent;
    ctx.fillRect(padL, legY - 4, 10, 8);
    ctx.fillStyle = ink;
    ctx.fillText('Q(s, a)', padL + 14, legY);

    ctx.fillStyle = policyColor;
    ctx.fillRect(padL + 80, legY - 4, 10, 8);
    ctx.fillStyle = ink;
    ctx.fillText('π(a | s)', padL + 94, legY);
  }

  document.getElementById('tempSlider').addEventListener('input', draw);
  document.getElementById('randomQ').addEventListener('click', randomizeQ);
  window.addEventListener('resize', resize);
  setTimeout(resize, 60);
})();


/* ====================================================================
   Widget 2 — 10-armed bandit: ε-greedy vs UCB vs Thompson
   ==================================================================== */
(function() {
  var cv = document.getElementById('banditCanvas');
  if (!cv) return;
  var ctx = cv.getContext('2d');
  var widget = cv.closest('.rl-widget');

  function cvar(name, fallback) {
    var v = getComputedStyle(widget).getPropertyValue(name).trim();
    return v || fallback;
  }

  var N_ARMS = 10;
  var trueMeans = [];
  function newArms() {
    trueMeans = [];
    for (var i = 0; i < N_ARMS; i++) trueMeans.push(Math.random());
    // Force the best arm to be exactly 1.0
    var k = Math.floor(Math.random() * N_ARMS);
    trueMeans[k] = 1.0;
  }
  newArms();

  function rewardFor(a) {
    return trueMeans[a] + (Math.random() - 0.5) * 0.3;
  }
  function optimum() { return Math.max.apply(null, trueMeans); }

  function runEpsGreedy(H, eps) {
    var N = new Array(N_ARMS).fill(0);
    var Q = new Array(N_ARMS).fill(0);
    var regret = [];
    var cumReg = 0;
    var opt = optimum();
    for (var t = 0; t < H; t++) {
      var a;
      if (Math.random() < eps) {
        a = Math.floor(Math.random() * N_ARMS);
      } else {
        var best = 0, bv = Q[0];
        for (var i = 1; i < N_ARMS; i++) if (Q[i] > bv) { bv = Q[i]; best = i; }
        a = best;
      }
      var r = rewardFor(a);
      N[a] += 1;
      Q[a] += (r - Q[a]) / N[a];
      cumReg += opt - trueMeans[a];
      regret.push(cumReg);
    }
    return regret;
  }

  function runUCB(H) {
    var N = new Array(N_ARMS).fill(0);
    var Q = new Array(N_ARMS).fill(0);
    var regret = [];
    var cumReg = 0;
    var opt = optimum();
    for (var t = 0; t < H; t++) {
      var a;
      if (t < N_ARMS) {
        a = t; // one of each arm first
      } else {
        var best = 0, bv = -Infinity;
        for (var i = 0; i < N_ARMS; i++) {
          var u = Q[i] + Math.sqrt(2 * Math.log(t) / N[i]);
          if (u > bv) { bv = u; best = i; }
        }
        a = best;
      }
      var r = rewardFor(a);
      N[a] += 1;
      Q[a] += (r - Q[a]) / N[a];
      cumReg += opt - trueMeans[a];
      regret.push(cumReg);
    }
    return regret;
  }

  function randn() {
    var u1 = Math.max(Math.random(), 1e-10);
    var u2 = Math.random();
    return Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
  }

  function runThompson(H) {
    // Gaussian posterior with known-ish noise
    var N = new Array(N_ARMS).fill(0);
    var sum = new Array(N_ARMS).fill(0);
    var regret = [];
    var cumReg = 0;
    var opt = optimum();
    for (var t = 0; t < H; t++) {
      var a = 0, bv = -Infinity;
      for (var i = 0; i < N_ARMS; i++) {
        var mu = N[i] > 0 ? sum[i] / N[i] : 0.5;
        var sig = N[i] > 0 ? 1 / Math.sqrt(N[i]) : 1.0;
        var sample = mu + sig * randn() * 0.5;
        if (sample > bv) { bv = sample; a = i; }
      }
      var r = rewardFor(a);
      N[a] += 1;
      sum[a] += r;
      cumReg += opt - trueMeans[a];
      regret.push(cumReg);
    }
    return regret;
  }

  var lastResults = null;

  function resize() {
    var rect = cv.getBoundingClientRect();
    var dpr = window.devicePixelRatio || 1;
    cv.width = rect.width * dpr;
    cv.height = 280 * dpr;
    cv.style.height = '280px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    if (lastResults) drawResults(lastResults);
    else drawEmpty();
  }

  function drawEmpty() {
    var rect = cv.getBoundingClientRect();
    var W = rect.width, H = 280;
    var paper = cvar('--paper', '#f4efe6');
    var inkMute = cvar('--ink-mute', '#8a8277');
    ctx.fillStyle = paper;
    ctx.fillRect(0, 0, W, H);
    ctx.fillStyle = inkMute;
    ctx.font = 'italic 13px "Newsreader", Georgia, serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('Press Run to compare strategies', W / 2, H / 2);
  }

  function drawResults(results) {
    var rect = cv.getBoundingClientRect();
    var W = rect.width, H = 280;

    var paper = cvar('--paper', '#f4efe6');
    var rule = cvar('--rule', '#c8bfae');
    var ink = cvar('--ink', '#1a1814');
    var inkMute = cvar('--ink-mute', '#8a8277');
    var accent = cvar('--accent', '#b94a1b');

    ctx.fillStyle = paper;
    ctx.fillRect(0, 0, W, H);

    var padL = 50, padR = 130, padT = 20, padB = 36;
    var plotW = W - padL - padR, plotH = H - padT - padB;

    var maxReg = 0;
    for (var r = 0; r < results.length; r++) {
      for (var i = 0; i < results[r].data.length; i++) {
        if (results[r].data[i] > maxReg) maxReg = results[r].data[i];
      }
    }
    if (maxReg === 0) maxReg = 1;
    var nSteps = results[0].data.length;

    // Grid
    ctx.strokeStyle = rule;
    ctx.lineWidth = 0.5;
    for (var g = 0; g <= 4; g++) {
      var gy = padT + plotH * g / 4;
      ctx.beginPath();
      ctx.moveTo(padL, gy);
      ctx.lineTo(W - padR, gy);
      ctx.stroke();
    }

    // Axis labels
    ctx.fillStyle = inkMute;
    ctx.font = '10px "DM Mono", ui-monospace, monospace';
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    for (var g2 = 0; g2 <= 4; g2++) {
      var y = padT + plotH * (4 - g2) / 4;
      ctx.fillText((maxReg * g2 / 4).toFixed(1), padL - 6, y);
    }
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    ctx.fillText('pulls', padL + plotW / 2, H - 14);

    ctx.save();
    ctx.translate(14, padT + plotH / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('cumulative regret', 0, 0);
    ctx.restore();

    // Curves
    for (var ri = 0; ri < results.length; ri++) {
      var res = results[ri];
      ctx.strokeStyle = res.color;
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (var j = 0; j < res.data.length; j++) {
        var x = padL + plotW * j / (nSteps - 1);
        var yy = padT + plotH - plotH * res.data[j] / maxReg;
        if (j === 0) ctx.moveTo(x, yy); else ctx.lineTo(x, yy);
      }
      ctx.stroke();

      // Legend
      ctx.fillStyle = res.color;
      ctx.fillRect(W - padR + 10, padT + ri * 24, 14, 3);
      ctx.fillStyle = ink;
      ctx.font = '11px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = 'left';
      ctx.textBaseline = 'middle';
      ctx.fillText(res.label, W - padR + 30, padT + ri * 24 + 2);
    }
  }

  document.getElementById('banditHSlider').addEventListener('input', function(e) {
    document.getElementById('banditHVal').textContent = e.target.value;
  });
  document.getElementById('banditEpsSlider').addEventListener('input', function(e) {
    document.getElementById('banditEps').textContent = (e.target.value / 100).toFixed(2);
  });

  document.getElementById('banditRunBtn').addEventListener('click', function() {
    var Hs = parseInt(document.getElementById('banditHSlider').value);
    var eps = parseInt(document.getElementById('banditEpsSlider').value) / 100;
    var accent = cvar('--accent', '#b94a1b');
    lastResults = [
      { label: 'ε-greedy', color: accent, data: runEpsGreedy(Hs, eps) },
      { label: 'UCB',      color: '#4d6a8f', data: runUCB(Hs) },
      { label: 'Thompson', color: '#6b8a3f', data: runThompson(Hs) }
    ];
    drawResults(lastResults);
  });

  document.getElementById('banditNewBtn').addEventListener('click', function() {
    newArms();
    lastResults = null;
    drawEmpty();
  });

  window.addEventListener('resize', resize);
  setTimeout(resize, 70);
})();
</script>
