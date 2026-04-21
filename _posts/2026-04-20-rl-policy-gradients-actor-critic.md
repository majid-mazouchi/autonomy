---
title: "Policy Gradients and Actor-Critic"
subtitle: "Push up the log-probability of actions that worked. Push down the ones that didn't. Everything else is variance reduction."
date: 2026-04-20 15:00:00 -0400
category: "Reinforcement Learning"
slug: rl-policy-gradients-actor-critic
excerpt: "From REINFORCE to PPO in one post — the policy gradient theorem, why its variance is ruinous by default, and the three tricks (baselines, critics, GAE) that make it work in practice. With an interactive 1D policy-learning widget."
reading_time: 17
---

This is Post 4 in the [field guide to reinforcement learning for control and robotics]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }}). The previous posts covered [the MDP formalism and Bellman equations]({{ '/posts/rl-foundations-mdps-value-functions-bellman/' | relative_url }}), then [how temporal-difference learning actually estimates value functions from data]({{ '/posts/rl-td-sarsa-q-learning/' | relative_url }}). Both of those were about learning *values*. This post is about learning the policy directly.

The shift of perspective matters. Value-based methods — Q-learning, DQN — learn $Q^*$ and read off a policy as $\arg\max_a Q(s, a)$. That works brilliantly with discrete actions and fails immediately with continuous ones, because you can't enumerate the `max` over $\mathbb{R}^n$. Policy-gradient methods sidestep the problem entirely: parameterize the policy directly as $\pi_\theta(a \mid s)$, and do gradient ascent on expected return. Continuous actions come for free. Stochastic policies — the kind that enable principled exploration — come for free. And the same machinery generalizes to image observations, recurrent policies, and pretty much anything else you can put a gradient through.

The catch, as with everything in RL, is variance. The policy gradient estimator is *technically* unbiased and *practically* unusable until you tame it. This post is the tour of the three tricks that do.

## The policy gradient theorem

The objective is the expected return of the policy, $J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}[G_0]$. Its gradient, remarkably, has a clean form that doesn't require differentiating through the environment dynamics:

$$ \nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta}\!\left[ \sum_{t} \nabla_\theta \log \pi_\theta(a_t \mid s_t) \cdot \Psi_t \right] $$

where $\Psi_t$ is any of: the return $G_t$, the Q-value $Q^\pi(s_t, a_t)$, or — in practice, the best choice — the advantage $A^\pi(s_t, a_t)$.

The geometric meaning is exactly what you'd want: push up the log-probability of actions whose weight $\Psi_t$ is high, push down the ones whose $\Psi_t$ is low. The `score function` $\nabla_\theta \log \pi_\theta$ is the direction in parameter space that increases the probability of the sampled action. Multiply it by how good that action turned out to be, sum over the trajectory, and you have the gradient.

This is **REINFORCE** when $\Psi_t = G_t$. It works in theory. It's unbiased. It also has variance so extreme that you can't realistically train anything harder than CartPole with it. The rest of this post is about why, and what to do about it.

## Why variance is ruinous by default

There are two separate variance problems in REINFORCE.

**First — the return itself is noisy.** $G_t$ sums many random rewards over many random transitions. Even for a good policy in a stable environment, different rollouts produce wildly different returns. The gradient estimator inherits all of that noise.

**Second — good actions can get low weight and bad actions can get high weight, purely by chance.** Imagine a policy that takes a great action at step 3 of an episode but then gets unlucky later and earns a terrible return. REINFORCE will *punish* that great action, because $G_3$ captures everything downstream. The algorithm blames each action for the entire remainder of the trajectory, regardless of whether it was actually responsible.

Modern policy gradients fix both problems with three ideas that compound nicely.

## Trick 1 — baselines

You can subtract *any* state-dependent function $b(s_t)$ from $\Psi_t$ without changing the expectation:

$$ \mathbb{E}_\pi\!\left[ \nabla_\theta \log \pi_\theta(a_t \mid s_t) \cdot b(s_t) \right] = 0 $$

Why? Because $b$ doesn't depend on the action, so it factors out of the action expectation, and then $\mathbb{E}_{\pi}[\nabla \log \pi] = 0$ by the standard log-trick identity. Gradient unchanged, variance reduced. It's a free lunch.

The natural choice is $b(s) = V^\pi(s)$, which turns $\Psi_t$ from the raw return into something much more meaningful:

$$ A^\pi(s_t, a_t) = Q^\pi(s_t, a_t) - V^\pi(s_t) $$

The **advantage function**. It measures *how much better than average* the action was, removing the baseline "everyone gets this much just for being in this state." Now a great action that gets unlucky downstream gets its credit — because the baseline absorbs the general unluckiness of the state.

## Trick 2 — actor-critic

In REINFORCE, the weight $\Psi_t$ is a Monte Carlo return. The actor-critic idea: use a learned $V_\phi(s)$ as the baseline and estimate the advantage by bootstrapping, just like TD did for value functions.

The simplest version uses the one-step TD error directly as the advantage estimate:

$$ \hat A_t = r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t) = \delta_t $$

That's the exact same TD error from the previous post. Low variance (one-step bootstrap), some bias (because $V_\phi$ is learned). The **actor** — the policy $\pi_\theta$ — is updated by policy gradient using $\hat A_t$. The **critic** — the value function $V_\phi$ — is updated by regression to its TD target. Two networks, one shared rollout, training together.

## Trick 3 — GAE, the interpolation

One-step TD has low variance but high bias. Monte Carlo has zero bias but enormous variance. The $n$-step return from the previous post sits somewhere between. **Generalized Advantage Estimation** parameterizes the full spectrum with a single knob $\lambda$:

$$ \hat A_t^{\text{GAE}(\gamma,\lambda)} = \sum_{k=0}^{\infty} (\gamma\lambda)^k\, \delta_{t+k}, \qquad \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t) $$

GAE is an exponentially-weighted sum of TD errors over the rest of the rollout.

- $\lambda = 0$ recovers the one-step TD actor-critic.
- $\lambda = 1$ recovers the Monte Carlo advantage (with a learned baseline).
- $\lambda = 0.95$ is the near-universal choice — low enough to keep variance reasonable, high enough to propagate credit meaningfully.

GAE is the default advantage estimator in PPO, A2C, and just about every modern on-policy method. The $\lambda$ knob essentially never gets tuned; 0.95 just works.

## Watching it happen

Below is a minimal 1D policy-gradient demo. The agent picks a single continuous action $a \in [-5, 5]$. The environment rewards actions near some hidden target $a^*$: $r = -(a - a^*)^2$, plus a bit of noise. The policy is Gaussian with mean $\mu_\theta$ (what the curve's peak sits at) and fixed standard deviation $\sigma$ (how wide the curve is).

Click **Step** to sample an action, observe the reward, and update $\mu_\theta$ via the policy-gradient rule. Watch $\mu$ drift toward $a^*$ as rewarded actions (green dots) pull the distribution right and punished actions (orange) push it left. The **baseline toggle** switches between REINFORCE (raw reward) and an advantage-style update (reward minus a running average). The difference in variance is visible in the update sizes.

<div class="rl-widget rl-pg">

  <div class="rl-w-head">
    <div class="rl-w-title">Interactive — 1D policy gradient on a continuous action</div>
    <div class="rl-w-tag">Run it</div>
  </div>

  <div class="rl-w-body">

    <div class="rl-w-ctrls">
      <div class="rl-w-ctrl">
        <label>Target a* <span class="val" id="pgTargetVal">2.00</span></label>
        <input type="range" id="pgTarget" min="-40" max="40" step="1" value="20">
      </div>
      <div class="rl-w-ctrl">
        <label>Policy σ <span class="val" id="pgSigmaVal">1.00</span></label>
        <input type="range" id="pgSigma" min="30" max="200" step="5" value="100">
      </div>
      <div class="rl-w-ctrl">
        <label>Learning rate α <span class="val" id="pgAlphaVal">0.05</span></label>
        <input type="range" id="pgAlpha" min="1" max="20" step="1" value="5">
      </div>
      <div class="rl-w-ctrl">
        <label>Steps taken <span class="val" id="pgSteps">0</span></label>
      </div>
    </div>

    <canvas id="pgCanvas" class="rl-w-canvas" height="260"></canvas>

    <div class="rl-w-actions">
      <button type="button" class="rl-btn primary" id="pgStep">+1 step</button>
      <button type="button" class="rl-btn" id="pgRun10">+10 steps</button>
      <button type="button" class="rl-btn" id="pgRun100">+100 steps</button>
      <button type="button" class="rl-btn ghost" id="pgReset">Reset</button>
    </div>

    <div class="rl-toggle-row">
      <span>Update rule:</span>
      <div class="rl-toggle-group" id="pgMode">
        <button type="button" data-mode="reinforce" class="active">REINFORCE (raw reward)</button>
        <button type="button" data-mode="baseline">With baseline (advantage)</button>
      </div>
    </div>

    <div class="rl-stats-grid">
      <div class="rl-stat">
        <span class="k">Policy mean μ</span>
        <span class="v" id="pgMu">0.00</span>
      </div>
      <div class="rl-stat">
        <span class="k">Running avg reward (baseline)</span>
        <span class="v" id="pgBaseline">—</span>
      </div>
      <div class="rl-stat">
        <span class="k">Last update Δμ</span>
        <span class="v" id="pgDelta">—</span>
      </div>
    </div>

  </div>

  <div class="rl-w-foot">
    Curve: policy density π(a|s). Vertical line: target a*. Dots: recent samples (green = reward above baseline, orange = below). Watch the peak migrate toward the target — and note how much smaller the updates are with a baseline.
  </div>
</div>

Three things worth noticing as you play:

- **Reducing σ mid-training accelerates convergence but increases the chance of getting stuck.** That's the exploration-exploitation trade-off in continuous form. Too-wide a policy explores forever; too-narrow commits early. This is why modern methods either learn $\sigma$ (REINFORCE-style) or regularize it with entropy (SAC-style).
- **REINFORCE's updates are much larger and noisier than the baseline version.** At the same learning rate, REINFORCE will oscillate; with the baseline, the policy walks cleanly to the target. Same gradient direction; different variance.
- **Cranking α up makes REINFORCE unstable long before it breaks the baseline version.** That's the whole practical value of variance reduction: it lets you use a larger step size safely. And larger step sizes are what makes training fast.

## Stochastic vs deterministic policies

For continuous actions, $\pi_\theta(a \mid s)$ is usually a **Gaussian** — the network outputs mean $\mu(s)$ and log-standard-deviation $\log\sigma(s)$. Sampling is $a = \mu + \sigma \cdot \epsilon$ with $\epsilon \sim \mathcal{N}(0, I)$. This is what PPO, A2C, and SAC use. The log-probability of the sampled action is differentiable, so the policy gradient works cleanly.

The alternative is a **deterministic** policy $a = \mu_\theta(s)$ with noise added externally for exploration during training. This is what DDPG and TD3 use, and it leads to a different update rule — the **deterministic policy gradient** theorem — and different stability properties. We'll unpack those in the next post.

> **Terminology alert.** The entropy of a stochastic policy, $H(\pi(\cdot \mid s)) = -\mathbb{E}[\log \pi]$, measures how random it is. Adding $\beta H$ to the objective *encourages exploration* — the policy is rewarded for staying uncertain. This is the core idea of **maximum-entropy RL** and the reason SAC is so robust. Rather than picking an exploration schedule and hoping it's right, SAC treats entropy as a first-class part of the objective and lets the algorithm decide how much uncertainty to keep.

## Trust regions, clipping, and PPO

REINFORCE with a baseline and GAE gets you A2C. One more problem remains: policy-gradient updates can take steps that are *too big*, landing you at a new policy that's worse than the one you started with. The gradient is a first-order signal; far from the sampled data, it lies.

**TRPO** (Trust Region Policy Optimization) addresses this by enforcing a hard KL-divergence constraint between the old and new policies on every update. It works well but involves a constrained optimization at every step — conjugate gradients, Fisher-vector products — which is a lot of machinery.

**PPO** (Proximal Policy Optimization) is the simplification that ate the world. Instead of a hard constraint, PPO *clips* the probability ratio $r_t(\theta) = \pi_\theta(a_t \mid s_t) / \pi_{\theta_{\text{old}}}(a_t \mid s_t)$ to stay within $[1-\epsilon, 1+\epsilon]$, typically with $\epsilon = 0.2$. The clipped surrogate objective is:

$$ L^{\text{CLIP}}(\theta) = \mathbb{E}_t\!\left[ \min\!\Big( r_t(\theta)\, \hat A_t,\; \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\, \hat A_t \Big) \right] $$

If the new policy drifts too far on an advantageous action, the gradient through the `clip` branch goes to zero — the update is capped. PPO is embarrassingly simple to implement (a single `torch.clamp` call), robust to hyperparameters, and has become the de facto standard for on-policy deep RL. The algorithm selector in the [field guide]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }}) recommends PPO for most sim-heavy continuous-control tasks, and that recommendation is driven entirely by this one simplification.

## What's actually running when you train PPO

To close the loop, here's what each training iteration looks like in practice — every modern PPO implementation is some version of this:

1. **Roll out** the current policy $\pi_{\theta_{\text{old}}}$ for $N$ steps in parallel environments; store $(s_t, a_t, r_t, \log \pi_{\theta_{\text{old}}}(a_t \mid s_t))$ for every transition.
2. **Compute the critic's value estimates** $V_\phi(s_t)$ for every state in the batch.
3. **Compute GAE advantages** $\hat A_t$ using $\gamma$ and $\lambda$, from the stored rewards and $V_\phi$.
4. **Normalize** the advantages across the batch to zero mean and unit variance (this is one of the "37 implementation details").
5. **Compute the PPO-clipped surrogate** $L^{\text{CLIP}}$ using the current policy $\pi_\theta$ against the stored $\log \pi_{\theta_{\text{old}}}$.
6. **Compute the value loss** as MSE between $V_\phi(s_t)$ and the empirical return $\hat R_t = \hat A_t + V_\phi(s_t)$.
7. **Compute the entropy bonus** $\beta H(\pi_\theta)$ to encourage exploration.
8. **Backpropagate** the combined loss $-L^{\text{CLIP}} + c_1 L^{\text{VF}} - c_2 H$ through actor and critic. Repeat for ~10 epochs over the rollout.
9. **Throw away the rollout** — it's off-policy now that $\theta$ has moved. Go back to step 1.

The policy gradient is buried in step 5. Everything else is plumbing that makes the gradient estimate usable: the rollout buffer (data collection), GAE (variance reduction), normalization (numerical stability), clipping (trust-region surrogate), the critic loss (baseline learning), and the entropy bonus (exploration). That ratio — one gradient formula to nine lines of engineering — is what the rest of this series is really about.

---

The next post steps up to the algorithms that actually dominate continuous-control papers and competitions: **SAC, TD3, DDPG**, and how they diverge from PPO by embracing off-policy learning and deterministic policies. That's where exploration, entropy regularization, and the choice of stochastic vs deterministic policies become the axes that distinguish algorithms.

← Back to [the field guide]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }})

<!-- =====================================================
     Post-scoped styles — same pattern as earlier RL posts
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

  .article-body .rl-toggle-row {
    display: flex;
    align-items: center;
    gap: 14px;
    flex-wrap: wrap;
    margin: 14px 0 0;
    font-family: var(--f-ui);
    font-size: .72rem;
    color: var(--ink-soft);
  }
  .article-body .rl-toggle-group {
    display: inline-flex;
    border: 1px solid var(--rule);
    border-radius: 2px;
    padding: 2px;
  }
  .article-body .rl-toggle-group button {
    font-family: var(--f-ui);
    font-size: .72rem;
    letter-spacing: .04em;
    text-transform: uppercase;
    background: transparent;
    color: var(--ink-mute);
    border: none;
    padding: 7px 12px;
    cursor: pointer;
    border-radius: 1px;
    transition: background .15s ease, color .15s ease;
  }
  .article-body .rl-toggle-group button:hover { color: var(--ink); }
  .article-body .rl-toggle-group button.active {
    background: var(--accent);
    color: var(--paper);
    font-weight: 500;
  }

  .article-body .rl-stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 12px 20px;
    margin: 14px 0 0;
    padding: 14px 16px;
    background: var(--paper);
    border: 1px solid var(--rule);
    border-radius: 2px;
  }
  .article-body .rl-stat {
    display: flex;
    flex-direction: column;
    gap: 3px;
  }
  .article-body .rl-stat .k {
    font-family: var(--f-ui);
    font-size: .62rem;
    letter-spacing: .14em;
    text-transform: uppercase;
    color: var(--ink-mute);
  }
  .article-body .rl-stat .v {
    font-family: var(--f-ui);
    font-size: .95rem;
    font-weight: 500;
    font-variant-numeric: tabular-nums;
    color: var(--ink);
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
(function() {
  var cv = document.getElementById('pgCanvas');
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

  // State
  var mu = 0.0;                // policy mean
  var baseline = null;         // running average reward
  var steps = 0;
  var recentSamples = [];      // {a, r, aboveBaseline}
  var MAX_SAMPLES = 60;
  var lastDelta = null;
  var mode = 'reinforce';

  // Target/sigma/alpha read from sliders
  function getTarget() { return parseInt(document.getElementById('pgTarget').value) / 10; }
  function getSigma()  { return parseInt(document.getElementById('pgSigma').value) / 100; }
  function getAlpha()  { return parseInt(document.getElementById('pgAlpha').value) / 100; }

  // Environment: reward = -(a - target)^2 + noise
  function rewardFor(a) {
    var target = getTarget();
    var noise = (Math.random() - 0.5) * 0.3;
    return -Math.pow(a - target, 2) + noise;
  }

  // Standard Normal sample (Box-Muller)
  function randn() {
    var u1 = Math.max(Math.random(), 1e-10);
    var u2 = Math.random();
    return Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
  }

  function step() {
    var sigma = getSigma();
    var alpha = getAlpha();

    // Sample action a ~ N(mu, sigma^2)
    var a = mu + sigma * randn();
    var r = rewardFor(a);

    // Policy-gradient weight
    var weight;
    var aboveBaseline;
    if (mode === 'reinforce') {
      weight = r;
      aboveBaseline = r > 0;
    } else {
      if (baseline === null) baseline = r;
      baseline = 0.9 * baseline + 0.1 * r;
      weight = r - baseline;
      aboveBaseline = weight > 0;
    }

    // Score function for Gaussian: d/dμ log π(a|μ,σ) = (a - μ) / σ²
    var score = (a - mu) / (sigma * sigma);
    var grad = score * weight;
    var delta = alpha * grad;

    // Clip to keep demo stable even with wild hyperparams
    delta = Math.max(-1.5, Math.min(1.5, delta));

    mu += delta;
    mu = Math.max(-5, Math.min(5, mu)); // keep in plot range

    lastDelta = delta;
    steps++;

    recentSamples.push({ a: a, r: r, above: aboveBaseline });
    if (recentSamples.length > MAX_SAMPLES) recentSamples.shift();

    updateStats();
    draw();
  }

  function multiStep(n) {
    for (var i = 0; i < n; i++) step();
  }

  function reset() {
    mu = 0;
    baseline = null;
    steps = 0;
    recentSamples = [];
    lastDelta = null;
    updateStats();
    draw();
  }

  function updateStats() {
    document.getElementById('pgSteps').textContent = steps;
    document.getElementById('pgMu').textContent = mu.toFixed(3);
    document.getElementById('pgBaseline').textContent = baseline === null ? '—' : baseline.toFixed(3);
    document.getElementById('pgDelta').textContent = lastDelta === null ? '—' :
      (lastDelta >= 0 ? '+' : '') + lastDelta.toFixed(3);
  }

  // Canvas drawing
  var A_MIN = -5, A_MAX = 5;
  var PAD_L = 44, PAD_R = 16, PAD_T = 16, PAD_B = 34;

  function resize() {
    var rect = cv.getBoundingClientRect();
    var dpr = window.devicePixelRatio || 1;
    cv.width = rect.width * dpr;
    cv.height = 260 * dpr;
    cv.style.height = '260px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    draw();
  }

  function aToX(a, W) {
    return PAD_L + (a - A_MIN) / (A_MAX - A_MIN) * (W - PAD_L - PAD_R);
  }

  function gauss(x, m, s) {
    return Math.exp(-0.5 * Math.pow((x - m) / s, 2)) / (s * Math.sqrt(2 * Math.PI));
  }

  function draw() {
    var rect = cv.getBoundingClientRect();
    var W = rect.width, H = 260;

    var paper = cvar('--paper', '#f4efe6');
    var rule = cvar('--rule', '#c8bfae');
    var ink = cvar('--ink', '#1a1814');
    var inkMute = cvar('--ink-mute', '#8a8277');
    var inkSoft = cvar('--ink-soft', '#4a4640');
    var accent = cvar('--accent', '#b94a1b');
    var accentDeep = cvar('--accent-deep', '#8a3412');

    var accentRgb = parseHex(accent, [185, 74, 27]);

    // Paint background
    ctx.fillStyle = paper;
    ctx.fillRect(0, 0, W, H);

    var plotW = W - PAD_L - PAD_R;
    var plotH = H - PAD_T - PAD_B;

    // Grid
    ctx.strokeStyle = rule;
    ctx.lineWidth = 0.5;
    ctx.setLineDash([2, 3]);
    for (var gv = A_MIN; gv <= A_MAX; gv++) {
      var gx = aToX(gv, W);
      ctx.beginPath();
      ctx.moveTo(gx, PAD_T);
      ctx.lineTo(gx, PAD_T + plotH);
      ctx.stroke();
    }
    ctx.setLineDash([]);

    // Zero line (a = 0)
    ctx.strokeStyle = rule;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(PAD_L, PAD_T + plotH);
    ctx.lineTo(W - PAD_R, PAD_T + plotH);
    ctx.stroke();

    // x-axis labels
    ctx.fillStyle = inkMute;
    ctx.font = '10px "DM Mono", ui-monospace, monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    for (var lv = A_MIN; lv <= A_MAX; lv++) {
      ctx.fillText(lv.toString(), aToX(lv, W), PAD_T + plotH + 6);
    }
    ctx.fillText('action a', PAD_L + plotW / 2, H - 14);

    // Target line (a*)
    var target = getTarget();
    var tx = aToX(target, W);
    ctx.strokeStyle = ink;
    ctx.globalAlpha = 0.75;
    ctx.lineWidth = 1.5;
    ctx.setLineDash([5, 4]);
    ctx.beginPath();
    ctx.moveTo(tx, PAD_T);
    ctx.lineTo(tx, PAD_T + plotH);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.globalAlpha = 1;

    // Target label
    ctx.fillStyle = ink;
    ctx.font = '10px "DM Mono", ui-monospace, monospace';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillText('a* = ' + target.toFixed(1), tx + 4, PAD_T + 2);

    // Policy curve π(a|μ,σ)
    var sigma = getSigma();
    var N = 200;
    var maxPdf = gauss(mu, mu, sigma);  // peak

    // Filled area under curve
    ctx.beginPath();
    for (var i = 0; i <= N; i++) {
      var a = A_MIN + (A_MAX - A_MIN) * i / N;
      var pdf = gauss(a, mu, sigma);
      var x = aToX(a, W);
      var y = PAD_T + plotH - (pdf / maxPdf) * plotH * 0.82;
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.lineTo(W - PAD_R, PAD_T + plotH);
    ctx.lineTo(PAD_L, PAD_T + plotH);
    ctx.closePath();
    ctx.fillStyle = 'rgba(' + accentRgb[0] + ',' + accentRgb[1] + ',' + accentRgb[2] + ',0.18)';
    ctx.fill();

    // Curve line
    ctx.strokeStyle = accent;
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (var i2 = 0; i2 <= N; i2++) {
      var a2 = A_MIN + (A_MAX - A_MIN) * i2 / N;
      var pdf2 = gauss(a2, mu, sigma);
      var x2 = aToX(a2, W);
      var y2 = PAD_T + plotH - (pdf2 / maxPdf) * plotH * 0.82;
      if (i2 === 0) ctx.moveTo(x2, y2); else ctx.lineTo(x2, y2);
    }
    ctx.stroke();

    // μ marker
    var mx = aToX(mu, W);
    var myPdf = gauss(mu, mu, sigma);
    var my = PAD_T + plotH - (myPdf / maxPdf) * plotH * 0.82;
    ctx.fillStyle = ink;
    ctx.beginPath();
    ctx.arc(mx, my, 4, 0, 2 * Math.PI);
    ctx.fill();
    ctx.font = '10px "DM Mono", ui-monospace, monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'bottom';
    ctx.fillText('μ = ' + mu.toFixed(2), mx, my - 6);

    // Recent sample dots along the zero line
    // Newer samples more opaque; older fade out
    for (var s = 0; s < recentSamples.length; s++) {
      var samp = recentSamples[s];
      var sx = aToX(Math.max(A_MIN, Math.min(A_MAX, samp.a)), W);
      var sy = PAD_T + plotH - 4;
      var age = (recentSamples.length - s) / recentSamples.length;
      var alpha = 0.15 + 0.75 * (1 - age);
      ctx.globalAlpha = alpha;
      ctx.fillStyle = samp.above ? '#4d7a4a' /* green */ : accentDeep;
      ctx.beginPath();
      ctx.arc(sx, sy, 3.5, 0, 2 * Math.PI);
      ctx.fill();
    }
    ctx.globalAlpha = 1;
  }

  // Bindings
  function bindSlider(id, valId, fmt) {
    var el = document.getElementById(id);
    var vEl = document.getElementById(valId);
    var update = function() { vEl.textContent = fmt ? fmt(el.value) : el.value; draw(); };
    el.addEventListener('input', update);
    update();
  }
  bindSlider('pgTarget', 'pgTargetVal', function(v) { return (parseInt(v) / 10).toFixed(2); });
  bindSlider('pgSigma', 'pgSigmaVal', function(v) { return (parseInt(v) / 100).toFixed(2); });
  bindSlider('pgAlpha', 'pgAlphaVal', function(v) { return (parseInt(v) / 100).toFixed(2); });

  document.getElementById('pgStep').addEventListener('click', function() { step(); });
  document.getElementById('pgRun10').addEventListener('click', function() { multiStep(10); });
  document.getElementById('pgRun100').addEventListener('click', function() { multiStep(100); });
  document.getElementById('pgReset').addEventListener('click', reset);

  document.querySelectorAll('#pgMode button').forEach(function(btn) {
    btn.addEventListener('click', function() {
      document.querySelectorAll('#pgMode button').forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
      mode = btn.dataset.mode;
      // Clear baseline on mode switch so it doesn't carry stale stats
      baseline = null;
      updateStats();
    });
  });

  window.addEventListener('resize', resize);
  updateStats();
  setTimeout(resize, 50);
})();
</script>
