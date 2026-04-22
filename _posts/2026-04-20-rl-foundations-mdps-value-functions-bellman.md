---
title: "Foundations: MDPs, Value Functions, and the Bellman Equations"
subtitle: "The discrete-time stochastic state-space model you already know, with a different name and a sign flip."
date: 2026-04-20 11:00:00 -0400
category: "Reinforcement Learning"
slug: rl-foundations-mdps-value-functions-bellman
excerpt: "Every RL algorithm starts from the same place: write down the MDP. This post covers the formalism a control engineer actually needs — state, action, reward, the discount factor, the value functions, and the Bellman recursion that runs everything from Q-learning to PPO."
reading_time: 15
---

This is the second post in my [field guide to reinforcement learning for control and robotics]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }}). The hub post laid out the map — the taxonomy, a five-question algorithm selector, the rules of thumb. This one starts filling in the detail. We begin where every RL algorithm begins: writing down the Markov Decision Process.

## What RL actually is, in one paragraph

Reinforcement learning is the study of how to make good decisions in environments where the *consequences* of those decisions unfold over time and the *best* decisions have to be learned from experience rather than derived from a known model. An agent observes its environment, picks an action, receives a reward and a new observation, and uses that signal to gradually improve its decision-making. That's the whole object. Everything in this field — Q-learning, PPO, SAC, model-based RL — is some strategy for doing that improvement well.

Every RL problem is an MDP. If you come from control, you already know this object — you just called it a discrete-time stochastic state-space model with a cost functional. The machinery is nearly identical. The differences are small but matter: RL maximizes where control minimizes, the dynamics are unknown rather than given, and the solution comes out as a *policy* rather than a closed-form control law. Once you see those three translations, the rest of the field falls into place.

## The agent-environment loop

Every RL algorithm, no matter how sophisticated, is built on one cycle that repeats forever: the agent observes, acts, and learns. The widget below shows that cycle live. Hit **play** to watch the loop run; each tick, the agent picks an action based on its current observation, the environment transitions to a new state, and a reward is emitted back. Slow it down with the speed slider to see what's happening at each step.

<div class="rl-widget rl-loop">

  <div class="rl-w-head">
    <div class="rl-w-title">Interactive — the agent-environment loop</div>
    <div class="rl-w-tag">How RL works</div>
  </div>

  <div class="rl-w-body">
    <canvas id="loopCanvas" class="rl-w-canvas" height="320"></canvas>

    <div class="rl-w-actions">
      <button type="button" class="rl-btn primary" id="loopPlay">▶ Play</button>
      <button type="button" class="rl-btn" id="loopStep">Step</button>
      <button type="button" class="rl-btn ghost" id="loopReset">Reset</button>
    </div>

    <div class="rl-w-ctrls" style="margin-top:14px;">
      <div class="rl-w-ctrl">
        <label>Speed <span class="val" id="loopSpeedVal">1.0×</span></label>
        <input type="range" id="loopSpeed" min="1" max="30" step="1" value="10">
      </div>
      <div class="rl-w-ctrl">
        <label>Step count <span class="val" id="loopSteps">0</span></label>
      </div>
      <div class="rl-w-ctrl">
        <label>Cumulative reward <span class="val" id="loopReturn">0.00</span></label>
      </div>
    </div>
  </div>

  <div class="rl-w-foot">
    The agent (left) sees an observation, picks an action, and sends it to the environment (right). The environment updates its state and returns a new observation plus a reward. Every RL algorithm is a different way to choose actions that make the cumulative reward grow.
  </div>
</div>

With the loop in mind, the formal object is what you'd expect.

## The MDP, formally

An MDP is the tuple $\mathcal{M} = \langle \mathcal{S},\, \mathcal{A},\, P,\, R,\, \gamma \rangle$ — the state space $\mathcal{S}$, the action space $\mathcal{A}$, the transition kernel $P(s' \mid s, a)$, the reward function $R(s, a)$, and the discount factor $\gamma \in [0, 1)$. That's the whole object. Every algorithm we'll cover in this series is some strategy for finding a good policy in this structure.

## The vocabulary, decoded

Here's the glossary every paper assumes you know. Reading it once unlocks 80% of the RL literature.

- **State $s_t$** is the information needed to predict the future. For a 7-DOF manipulator, this is joint angles, velocities, end-effector pose, maybe the target. The *Markov property* says $s_t$ summarizes everything relevant from history. When it's violated — partial observability, hidden modes — you either stack frames into the observation or use a recurrent policy.
- **Action $a_t$** is what the agent commands. In robotics this is almost always **continuous**: torques, velocities, or end-effector twists. This one fact rules out a huge class of classical RL methods, which I'll get to in the next post.
- **Reward $r_t = R(s_t, a_t)$** is the scalar the agent wants to maximize. In control terms, it's *negative running cost*. RL maximizes; LQR minimizes. Same math, opposite sign.
- **Policy $\pi$** is the controller. Either deterministic $a = \pi(s)$ or stochastic $a \sim \pi(\cdot \mid s)$. In deep RL it's a neural network.
- **Trajectory / rollout / episode** is a sequence $(s_0, a_0, r_0, s_1, a_1, r_1, \ldots)$ generated by running $\pi$ in the environment. Episodes end on termination — task done, fell over, time limit reached.
- **Return $G_t$** is the discounted cumulative reward from time $t$: $G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k}$. *This* is the objective the agent is actually maximizing — not the instantaneous reward.
- **Discount $\gamma$** controls how much the agent cares about the future. $\gamma = 0$ is myopic; $\gamma \to 1$ is farsighted. Mathematically it's necessary for infinite-horizon convergence; practically it's also a bias-variance knob.

> **Terminology trap.** *Reward* and *return* are not the same word. Reward is one step. Return is the discounted sum over a whole trajectory. Confusing them will make every RL paper look wrong.

## The discount factor, visually

Slide $\gamma$ below and watch how the present-value weighting changes. A reward $r = 1$ received $k$ steps from now is worth $\gamma^k$ today. The cyan dashed line marks the effective planning horizon $\frac{1}{1-\gamma}$ — the time at which the weight has dropped to about 37% of its starting value.

<div class="rl-widget rl-discount">

  <div class="rl-w-head">
    <div class="rl-w-title">Interactive — the discount factor γ</div>
    <div class="rl-w-tag">Try it</div>
  </div>

  <div class="rl-w-body">
    <div class="rl-w-ctrls">
      <div class="rl-w-ctrl">
        <label>Discount γ <span class="val" id="gammaVal">0.99</span></label>
        <input type="range" id="gammaSlider" min="0" max="100" value="99">
      </div>
      <div class="rl-w-ctrl">
        <label>Horizon ≈ <span class="val" id="horizonVal">99</span> steps</label>
      </div>
      <div class="rl-w-ctrl">
        <label>Σ γᵏ = <span class="val" id="sumVal">100.0</span></label>
      </div>
    </div>
    <canvas id="gammaCanvas" class="rl-w-canvas" height="280"></canvas>
  </div>

  <div class="rl-w-foot">
    Rule of thumb · γ = 0.99 for tasks around 100 steps · γ = 0.95 for short horizons · γ → 1 demands careful reward scaling.
  </div>
</div>

### Choosing γ in practice

The effective planning horizon is approximately $\frac{1}{1 - \gamma}$. Write it on a sticky note — you'll use it every time you start a new task.

- **$\gamma = 0.99$** → horizon ≈ 100 steps. Default for most robotics tasks at 50–100 Hz control rates.
- **$\gamma = 0.95$** → horizon ≈ 20 steps. Good for short episodic tasks like reaching or grasping.
- **$\gamma = 0.999$** → horizon ≈ 1000 steps. Long-horizon locomotion. Rarely needed; hurts sample efficiency.
- **$\gamma = 1$** → only legal for strictly finite episodes with bounded reward. Otherwise the return diverges and your value estimates explode.

> **Match γ to your task horizon, not to the paper you're copying.** A locomotion paper that used $\gamma = 0.99$ at 1000 Hz was effectively looking 100 ms ahead. That same $\gamma$ at 50 Hz looks 2 seconds ahead. Different problems. People reproduce published numbers and find their agent can't learn — nine times out of ten, it's a control-rate-discount mismatch.

## Value functions

The central objects in RL are not the policy itself but the *value* of a policy — how much return you expect to collect if you follow it. There are two flavors, and the difference matters more than it looks.

$$V^\pi(s) = \mathbb{E}_\pi\!\left[\sum_{k=0}^\infty \gamma^k r_{t+k} \,\Big|\, s_t = s\right]$$

$$Q^\pi(s, a) = \mathbb{E}_\pi\!\left[\sum_{k=0}^\infty \gamma^k r_{t+k} \,\Big|\, s_t = s,\, a_t = a\right]$$

$V$ tells you *how good a state is under the current policy*. $Q$ tells you *how good it is to take action $a$ right now and then follow the policy*. That extra degree of freedom in $Q$ is what lets you improve the policy — pick the action with the highest $Q$, and you've made progress.

### The advantage function

The **advantage** is the single most useful derived quantity in modern RL:

$$A^\pi(s, a) = Q^\pi(s, a) - V^\pi(s)$$

It answers "how much better than average is this action?" Zero-mean by construction under $\pi$. Almost every modern policy-gradient method (PPO, A2C, SAC) uses advantage estimates rather than raw returns because the variance is vastly smaller. We'll derive that in the policy-gradient post.

## The Bellman equations — the recursion that runs RL

The defining property of value functions: the value at a state equals the immediate reward plus the discounted value of where you end up. Writing this recursion out gives the **Bellman expectation equation**:

$$Q^\pi(s,a) = \mathbb{E}_{s' \sim P}\!\left[ r + \gamma\, \mathbb{E}_{a' \sim \pi}[Q^\pi(s', a')] \right]$$

And for the optimal $Q^\star$, the **Bellman optimality equation**:

$$Q^\star(s,a) = \mathbb{E}_{s' \sim P}\!\left[ r + \gamma\, \max_{a'} Q^\star(s', a') \right]$$

That `max` is the *only* difference between evaluating a fixed policy and finding the best one. It's also the reason Q-learning works at all — and the reason it struggles with continuous actions, where you can't enumerate the `max` without some approximation.

> **Control engineer's decoder ring.** The Bellman equation is the discrete-time, stochastic, reward-signed analog of the Hamilton–Jacobi–Bellman PDE you've seen in optimal control. Value iteration is dynamic programming backwards from the terminal state. LQR is the closed-form solution when dynamics are linear and rewards are quadratic — in which case $V$ is a quadratic form and you recover the Riccati equation.

## Q-learning on a gridworld

Nothing makes the recursion concrete like watching it run. Below is Q-learning on a 10×8 gridworld. Start (cyan square) is bottom-left, goal (orange ★) is top-right, obstacles are the dark-grey walls. Colors show $\max_a Q(s, a)$; arrows show the greedy policy. Click **Train 100 ep** and watch the value propagate backwards from the goal, step by step.

<div class="rl-widget rl-gridworld">

  <div class="rl-w-head">
    <div class="rl-w-title">Interactive — Q-learning on a gridworld</div>
    <div class="rl-w-tag">Run it</div>
  </div>

  <div class="rl-w-body">
    <div class="rl-w-ctrls">
      <div class="rl-w-ctrl">
        <label>Learning rate α <span class="val" id="alphaVal">0.30</span></label>
        <input type="range" id="alphaSlider" min="1" max="100" value="30">
      </div>
      <div class="rl-w-ctrl">
        <label>Discount γ <span class="val" id="qgammaVal">0.95</span></label>
        <input type="range" id="qgammaSlider" min="50" max="99" value="95">
      </div>
      <div class="rl-w-ctrl">
        <label>ε-greedy <span class="val" id="epsVal">0.15</span></label>
        <input type="range" id="epsSlider" min="0" max="100" value="15">
      </div>
      <div class="rl-w-ctrl">
        <label>Episode <span class="val" id="epVal">0</span></label>
      </div>
    </div>
    <canvas id="gridCanvas" class="rl-w-canvas" height="360"></canvas>
    <div class="rl-w-actions">
      <button type="button" class="rl-btn primary" id="qTrainBtn">▶ Train 100 ep</button>
      <button type="button" class="rl-btn" id="qStepBtn">Step 1 ep</button>
      <button type="button" class="rl-btn ghost" id="qResetBtn">Reset</button>
    </div>
  </div>

  <div class="rl-w-foot">
    ε controls exploration · α controls how aggressively estimates update · γ controls how far credit propagates.
  </div>
</div>

### What the gridworld is really teaching you

Three phenomena are visible in that widget that show up in *every* RL algorithm you'll ever write:

1. **Credit propagation is slow.** Reward information flows backwards one step per update. Even on a tiny grid this takes many episodes. On a real robot with a sparse reward, this is exactly why your agent learns nothing for the first 10,000 episodes — the reward signal hasn't had time to reach the starting state yet.
2. **Exploration is not free.** Drop $\epsilon$ to 0 and the agent gets stuck following whatever wrong idea it had first. Push $\epsilon$ to 1 and it will never commit to a good path. This trade-off never goes away — modern methods (SAC, curiosity-driven exploration, parameter noise) just handle it more cleverly.
3. **α is a bias/variance knob.** Small $\alpha$ is stable but slow. Large $\alpha$ is fast but oscillates. Same story as every filter you've ever tuned.

> **Rule of thumb.** If you can write your state and action spaces down on paper and the state space is $\lesssim 10^6$, tabular methods (Q-learning, SARSA) will solve your problem faster and more reliably than any deep method. Don't reach for neural networks until the problem demands it. A lot of robotics "RL failures" are really "we used a neural net when a Q-table would have worked."

## The plan from here

You now have the vocabulary and the central recursion. The next post unpacks *how* to actually learn those value functions when you don't know the dynamics — temporal-difference learning, SARSA, and the relationship between on-policy and off-policy updates. That's where the tabular Q-learning you just watched gets its legs.

---

← Back to [the field guide]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }})

<!-- =====================================================
     Post-scoped styles for the RL foundations widgets
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
    letter-spacing: .16em;
    text-transform: uppercase;
    color: var(--accent);
    padding: 3px 8px;
    border: 1px solid var(--accent);
    border-radius: 2px;
  }
  .article-body .rl-w-body { padding: 20px; }

  .article-body .rl-w-ctrls {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px 22px;
    margin: 0 0 16px;
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
(function() {
  // ============================================================
  // Widget 1 — Discount factor visualization
  // ============================================================
  var gCanvas = document.getElementById('gammaCanvas');
  if (gCanvas) {
    var slider = document.getElementById('gammaSlider');
    var gammaVal = document.getElementById('gammaVal');
    var horizonVal = document.getElementById('horizonVal');
    var sumVal = document.getElementById('sumVal');
    var widget = gCanvas.closest('.rl-widget');

    function cvar(name, fallback) {
      var v = getComputedStyle(widget).getPropertyValue(name).trim();
      return v || fallback;
    }

    function resizeG() {
      var rect = gCanvas.getBoundingClientRect();
      var dpr = window.devicePixelRatio || 1;
      gCanvas.width = rect.width * dpr;
      gCanvas.height = 280 * dpr;
      gCanvas.style.height = '280px';
      gCanvas.getContext('2d').setTransform(dpr, 0, 0, dpr, 0, 0);
      drawG();
    }

    function drawG() {
      var ctx = gCanvas.getContext('2d');
      var rect = gCanvas.getBoundingClientRect();
      var W = rect.width, H = 280;
      var gamma = parseInt(slider.value) / 100;
      gammaVal.textContent = gamma.toFixed(2);
      horizonVal.textContent = gamma < 1 ? (1 / (1 - gamma)).toFixed(0) : '∞';

      var sum = 0;
      var nSteps = 150;
      for (var k = 0; k < nSteps; k++) sum += Math.pow(gamma, k);
      sumVal.textContent = sum.toFixed(1);

      var paper = cvar('--paper', '#f4efe6');
      var rule = cvar('--rule', '#c8bfae');
      var ink = cvar('--ink', '#1a1814');
      var inkMute = cvar('--ink-mute', '#8a8277');
      var accent = cvar('--accent', '#b94a1b');

      ctx.fillStyle = paper;
      ctx.fillRect(0, 0, W, H);

      var padL = 56, padR = 20, padT = 24, padB = 40;
      var plotW = W - padL - padR;
      var plotH = H - padT - padB;

      // grid
      ctx.strokeStyle = rule;
      ctx.lineWidth = 0.5;
      for (var i = 0; i <= 5; i++) {
        var y = padT + plotH * i / 5;
        ctx.beginPath();
        ctx.moveTo(padL, y);
        ctx.lineTo(W - padR, y);
        ctx.stroke();
      }

      // axis labels
      ctx.fillStyle = inkMute;
      ctx.font = '10px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = 'right';
      ctx.textBaseline = 'middle';
      for (var i2 = 0; i2 <= 5; i2++) {
        var y2 = padT + plotH * (5 - i2) / 5;
        ctx.fillText((i2 / 5).toFixed(1), padL - 8, y2);
      }
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';
      for (var k2 = 0; k2 <= nSteps; k2 += 25) {
        var x2 = padL + plotW * k2 / nSteps;
        ctx.fillText(k2, x2, H - padB + 6);
      }
      ctx.fillText('steps into future', padL + plotW / 2, H - 14);

      ctx.save();
      ctx.translate(14, padT + plotH / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('γᵏ weight', 0, 0);
      ctx.restore();

      // bars
      var nBars = 60;
      var barW = Math.max(1, plotW / nBars - 1);
      // Parse accent hex into rgb for alpha blending
      var rM = accent.match(/^#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i);
      var rgb = rM ? [parseInt(rM[1], 16), parseInt(rM[2], 16), parseInt(rM[3], 16)] : [185, 74, 27];
      for (var k3 = 0; k3 < nBars; k3++) {
        var w = Math.pow(gamma, k3);
        var x3 = padL + plotW * k3 / nBars;
        var h = plotH * w;
        var alpha = Math.max(0.25, w);
        ctx.fillStyle = 'rgba(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ',' + alpha + ')';
        ctx.fillRect(x3, padT + plotH - h, barW, h);
      }

      // horizon marker
      if (gamma < 1 && gamma > 0) {
        var hk = Math.min(1 / (1 - gamma), nBars);
        var hx = padL + plotW * hk / nBars;
        ctx.strokeStyle = ink;
        ctx.globalAlpha = 0.55;
        ctx.lineWidth = 1;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(hx, padT);
        ctx.lineTo(hx, padT + plotH);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.globalAlpha = 1;

        ctx.fillStyle = ink;
        ctx.globalAlpha = 0.75;
        ctx.textAlign = 'left';
        ctx.textBaseline = 'top';
        ctx.font = '10px "DM Mono", ui-monospace, monospace';
        ctx.fillText('1/(1−γ)', hx + 6, padT + 4);
        ctx.globalAlpha = 1;
      }
    }

    slider.addEventListener('input', drawG);
    window.addEventListener('resize', resizeG);
    setTimeout(resizeG, 50);
  }

  // ============================================================
  // Widget 2 — Gridworld Q-learning
  // ============================================================
  var gridCanvas = document.getElementById('gridCanvas');
  if (!gridCanvas) return;

  var W_GRID = 10, H_GRID = 8;
  var obstacles = new Set(['3,2','3,3','3,4','3,5','6,1','6,2','6,3','6,4','6,5','6,6']);
  var start = [0, 7], goal = [9, 0];
  var Q = {};
  var episode = 0;
  var animating = false;

  var gridWidget = gridCanvas.closest('.rl-widget');
  function gvar(name, fallback) {
    var v = getComputedStyle(gridWidget).getPropertyValue(name).trim();
    return v || fallback;
  }

  function key(x, y, a) { return x + ',' + y + ',' + a; }
  function sKey(x, y) { return x + ',' + y; }

  function resetQ() {
    Q = {};
    for (var x = 0; x < W_GRID; x++)
      for (var y = 0; y < H_GRID; y++)
        for (var a = 0; a < 4; a++)
          Q[key(x, y, a)] = 0;
    episode = 0;
    document.getElementById('epVal').textContent = '0';
    drawGrid();
  }

  var actions = [[0, -1], [1, 0], [0, 1], [-1, 0]]; // N, E, S, W

  function stepEnv(x, y, a) {
    var d = actions[a];
    var nx = x + d[0], ny = y + d[1];
    if (nx < 0 || nx >= W_GRID || ny < 0 || ny >= H_GRID || obstacles.has(sKey(nx, ny))) {
      nx = x; ny = y;
    }
    var r = -0.04;
    if (nx === goal[0] && ny === goal[1]) r = 1.0;
    return [nx, ny, r];
  }

  function runEpisode() {
    var alpha = parseInt(document.getElementById('alphaSlider').value) / 100;
    var gamma = parseInt(document.getElementById('qgammaSlider').value) / 100;
    var eps = parseInt(document.getElementById('epsSlider').value) / 100;
    var x = start[0], y = start[1];
    for (var t = 0; t < 200; t++) {
      var a;
      if (Math.random() < eps) {
        a = Math.floor(Math.random() * 4);
      } else {
        var best = -Infinity;
        for (var k = 0; k < 4; k++) {
          if (Q[key(x, y, k)] > best) { best = Q[key(x, y, k)]; a = k; }
        }
        if (a === undefined) a = Math.floor(Math.random() * 4);
      }
      var res = stepEnv(x, y, a);
      var nx = res[0], ny = res[1], r = res[2];
      var maxNext = -Infinity;
      for (var k2 = 0; k2 < 4; k2++) {
        if (Q[key(nx, ny, k2)] > maxNext) maxNext = Q[key(nx, ny, k2)];
      }
      Q[key(x, y, a)] += alpha * (r + gamma * maxNext - Q[key(x, y, a)]);
      x = nx; y = ny;
      if (x === goal[0] && y === goal[1]) break;
    }
    episode++;
    document.getElementById('epVal').textContent = episode;
  }

  function resizeGrid() {
    var rect = gridCanvas.getBoundingClientRect();
    var dpr = window.devicePixelRatio || 1;
    gridCanvas.width = rect.width * dpr;
    gridCanvas.height = 360 * dpr;
    gridCanvas.style.height = '360px';
    gridCanvas.getContext('2d').setTransform(dpr, 0, 0, dpr, 0, 0);
    drawGrid();
  }

  // Interpolate between paper color (low value) and accent color (high value)
  function valueColor(t, paperRgb, accentRgb) {
    var r = Math.round(paperRgb[0] + t * (accentRgb[0] - paperRgb[0]));
    var g = Math.round(paperRgb[1] + t * (accentRgb[1] - paperRgb[1]));
    var b = Math.round(paperRgb[2] + t * (accentRgb[2] - paperRgb[2]));
    return 'rgb(' + r + ',' + g + ',' + b + ')';
  }

  function parseHex(hex, fallback) {
    var m = hex.match(/^#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i);
    if (!m) return fallback;
    return [parseInt(m[1], 16), parseInt(m[2], 16), parseInt(m[3], 16)];
  }

  function drawGrid() {
    var ctx = gridCanvas.getContext('2d');
    var rect = gridCanvas.getBoundingClientRect();
    var W = rect.width, H = 360;

    var paper = gvar('--paper', '#f4efe6');
    var paper2 = gvar('--paper-2', '#ebe3d4');
    var rule = gvar('--rule', '#c8bfae');
    var ink = gvar('--ink', '#1a1814');
    var inkSoft = gvar('--ink-soft', '#4a4640');
    var accent = gvar('--accent', '#b94a1b');

    var paperRgb = parseHex(paper, [244, 239, 230]);
    var accentRgb = parseHex(accent, [185, 74, 27]);

    ctx.fillStyle = paper;
    ctx.fillRect(0, 0, W, H);

    var cw = Math.min(W / W_GRID, H / H_GRID);
    var offX = (W - cw * W_GRID) / 2;
    var offY = (H - cw * H_GRID) / 2;

    // find V range
    var vmin = Infinity, vmax = -Infinity;
    for (var x = 0; x < W_GRID; x++)
      for (var y = 0; y < H_GRID; y++) {
        if (obstacles.has(sKey(x, y))) continue;
        var v = -Infinity;
        for (var a = 0; a < 4; a++) {
          if (Q[key(x, y, a)] > v) v = Q[key(x, y, a)];
        }
        if (v < vmin) vmin = v;
        if (v > vmax) vmax = v;
      }
    if (vmax === vmin) vmax = vmin + 1;

    for (var x2 = 0; x2 < W_GRID; x2++)
      for (var y2 = 0; y2 < H_GRID; y2++) {
        var px = offX + x2 * cw, py = offY + y2 * cw;
        if (obstacles.has(sKey(x2, y2))) {
          // Obstacle — dark ink block
          ctx.fillStyle = inkSoft;
          ctx.fillRect(px, py, cw, cw);
        } else if (x2 === goal[0] && y2 === goal[1]) {
          // Goal
          ctx.fillStyle = accent;
          ctx.fillRect(px + 2, py + 2, cw - 4, cw - 4);
          ctx.fillStyle = paper;
          ctx.font = (cw * 0.45) + 'px Fraunces, serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText('★', px + cw / 2, py + cw / 2);
        } else {
          var v2 = -Infinity, bestA = 0;
          for (var a2 = 0; a2 < 4; a2++) {
            if (Q[key(x2, y2, a2)] > v2) { v2 = Q[key(x2, y2, a2)]; bestA = a2; }
          }
          var t = (v2 - vmin) / (vmax - vmin);
          ctx.fillStyle = valueColor(t, paperRgb, accentRgb);
          ctx.fillRect(px + 1, py + 1, cw - 2, cw - 2);

          // grid line
          ctx.strokeStyle = rule;
          ctx.lineWidth = 0.5;
          ctx.strokeRect(px + 1, py + 1, cw - 2, cw - 2);

          // arrow
          if (v2 > vmin + 0.01 * (vmax - vmin)) {
            var arrows = ['↑', '→', '↓', '←'];
            ctx.fillStyle = t > 0.5 ? paper : ink;
            ctx.font = (cw * 0.42) + 'px "DM Mono", ui-monospace, monospace';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(arrows[bestA], px + cw / 2, py + cw / 2 + 1);
          }
        }
        // start marker
        if (x2 === start[0] && y2 === start[1]) {
          ctx.strokeStyle = ink;
          ctx.lineWidth = 2;
          ctx.strokeRect(px + 3, py + 3, cw - 6, cw - 6);
        }
      }
  }

  function train(n) {
    if (animating) return Promise.resolve();
    animating = true;
    return new Promise(function(resolve) {
      var i = 0;
      function tick() {
        if (i >= n) { drawGrid(); animating = false; resolve(); return; }
        runEpisode();
        if (i % 5 === 0 || i === n - 1) drawGrid();
        i++;
        setTimeout(tick, 20);
      }
      tick();
    });
  }

  document.getElementById('alphaSlider').addEventListener('input', function(e) {
    document.getElementById('alphaVal').textContent = (e.target.value / 100).toFixed(2);
  });
  document.getElementById('qgammaSlider').addEventListener('input', function(e) {
    document.getElementById('qgammaVal').textContent = (e.target.value / 100).toFixed(2);
  });
  document.getElementById('epsSlider').addEventListener('input', function(e) {
    document.getElementById('epsVal').textContent = (e.target.value / 100).toFixed(2);
  });
  document.getElementById('qTrainBtn').addEventListener('click', function() { train(100); });
  document.getElementById('qStepBtn').addEventListener('click', function() { runEpisode(); drawGrid(); });
  document.getElementById('qResetBtn').addEventListener('click', resetQ);
  window.addEventListener('resize', resizeGrid);

  resetQ();
  setTimeout(resizeGrid, 60);
})();

/* ====================================================================
   Widget 3 — The agent-environment loop
   A didactic animation: boxes for agent/environment with arrows showing
   observation → action → reward flow. Plays as a continuous cycle.
   ==================================================================== */
(function() {
  var cv = document.getElementById('loopCanvas');
  if (!cv) return;
  var ctx = cv.getContext('2d');
  var widget = cv.closest('.rl-widget');

  function cvar(name, fallback) {
    var v = getComputedStyle(widget).getPropertyValue(name).trim();
    return v || fallback;
  }

  // Cycle phases — what's highlighted at each moment in the loop:
  // 0 = agent thinking, 1 = action flowing to env, 2 = env transitioning,
  // 3 = reward + obs flowing back to agent
  var phase = 0;
  var phaseProgress = 0;  // 0 -> 1 within current phase
  var playing = false;
  var stepCount = 0;
  var cumReward = 0;
  var lastReward = 0;
  var lastAction = '—';
  var envState = 0;  // just a visual indicator — a number that drifts
  var raf = null;
  var lastFrameTime = null;

  // Synthetic "agent + environment" for the visualization
  var actionLabels = ['right', 'up', 'left', 'down'];

  function doOneStep() {
    // Pick a "smart-ish" action that tends to push state toward 5
    // (so cumulative reward drifts up and the demo feels purposeful).
    var targetAction;
    if (envState < 4) targetAction = 1; // up
    else if (envState > 6) targetAction = 3; // down
    else targetAction = Math.floor(Math.random() * 4);

    // Add a little stochasticity so it isn't perfectly greedy
    if (Math.random() < 0.15) targetAction = Math.floor(Math.random() * 4);

    lastAction = actionLabels[targetAction];

    // Environment transition
    if (targetAction === 1) envState += 0.6 + Math.random() * 0.3;
    else if (targetAction === 3) envState -= 0.6 + Math.random() * 0.3;
    else envState += (Math.random() - 0.5) * 0.3;
    envState = Math.max(0, Math.min(10, envState));

    // Reward: higher when near 5 (the sweet spot)
    lastReward = 1 - Math.abs(envState - 5) / 5;
    lastReward = +lastReward.toFixed(2);
    cumReward += lastReward;
    stepCount++;

    document.getElementById('loopSteps').textContent = stepCount;
    document.getElementById('loopReturn').textContent = cumReward.toFixed(2);
  }

  function resetLoop() {
    phase = 0;
    phaseProgress = 0;
    stepCount = 0;
    cumReward = 0;
    lastReward = 0;
    lastAction = '—';
    envState = 5;
    document.getElementById('loopSteps').textContent = '0';
    document.getElementById('loopReturn').textContent = '0.00';
    draw();
  }

  function togglePlay() {
    playing = !playing;
    var btn = document.getElementById('loopPlay');
    btn.textContent = playing ? '❚❚ Pause' : '▶ Play';
    if (playing) {
      lastFrameTime = null;
      raf = requestAnimationFrame(tick);
    } else if (raf) {
      cancelAnimationFrame(raf);
    }
  }

  function tick(now) {
    if (!playing) return;
    if (lastFrameTime === null) lastFrameTime = now;
    var dt = (now - lastFrameTime) / 1000;
    lastFrameTime = now;

    var speed = parseInt(document.getElementById('loopSpeed').value) / 10;
    phaseProgress += dt * speed;

    while (phaseProgress >= 1) {
      phaseProgress -= 1;
      phase = (phase + 1) % 4;
      if (phase === 0) {
        // Completed a full cycle — execute one actual environment step
        doOneStep();
      }
    }

    draw();
    raf = requestAnimationFrame(tick);
  }

  function stepOnce() {
    // Single step: run the full cycle once synchronously for the action,
    // then animate through phases.
    if (playing) togglePlay();
    doOneStep();
    phase = 0;
    phaseProgress = 0;
    draw();
  }

  function resize() {
    var rect = cv.getBoundingClientRect();
    var dpr = window.devicePixelRatio || 1;
    cv.width = rect.width * dpr;
    cv.height = 320 * dpr;
    cv.style.height = '320px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    draw();
  }

  function roundRect(x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.lineTo(x + w - r, y);
    ctx.quadraticCurveTo(x + w, y, x + w, y + r);
    ctx.lineTo(x + w, y + h - r);
    ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
    ctx.lineTo(x + r, y + h);
    ctx.quadraticCurveTo(x, y + h, x, y + h - r);
    ctx.lineTo(x, y + r);
    ctx.quadraticCurveTo(x, y, x + r, y);
    ctx.closePath();
  }

  function drawArrow(x1, y1, x2, y2, color, active, progress) {
    ctx.strokeStyle = color;
    ctx.lineWidth = active ? 2.5 : 1.25;
    ctx.globalAlpha = active ? 1 : 0.35;

    // Dashed line, with a moving pulse if active
    ctx.setLineDash(active ? [] : [4, 4]);
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
    ctx.setLineDash([]);

    // Arrowhead
    var ang = Math.atan2(y2 - y1, x2 - x1);
    var ahLen = 9;
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.moveTo(x2, y2);
    ctx.lineTo(x2 - ahLen * Math.cos(ang - Math.PI / 6), y2 - ahLen * Math.sin(ang - Math.PI / 6));
    ctx.lineTo(x2 - ahLen * Math.cos(ang + Math.PI / 6), y2 - ahLen * Math.sin(ang + Math.PI / 6));
    ctx.closePath();
    ctx.fill();

    // Pulse dot traveling along the active arrow
    if (active) {
      var dotX = x1 + (x2 - x1) * progress;
      var dotY = y1 + (y2 - y1) * progress;
      ctx.beginPath();
      ctx.arc(dotX, dotY, 5, 0, 2 * Math.PI);
      ctx.fillStyle = color;
      ctx.fill();
      // halo
      ctx.beginPath();
      ctx.arc(dotX, dotY, 10, 0, 2 * Math.PI);
      ctx.globalAlpha = 0.2;
      ctx.fill();
      ctx.globalAlpha = 1;
    }

    ctx.globalAlpha = 1;
  }

  function draw() {
    var rect = cv.getBoundingClientRect();
    var W = rect.width, H = 320;

    var paper = cvar('--paper', '#f4efe6');
    var paper2 = cvar('--paper-2', '#ebe3d4');
    var rule = cvar('--rule', '#c8bfae');
    var ink = cvar('--ink', '#1a1814');
    var inkSoft = cvar('--ink-soft', '#4a4640');
    var inkMute = cvar('--ink-mute', '#8a8277');
    var accent = cvar('--accent', '#b94a1b');

    ctx.fillStyle = paper;
    ctx.fillRect(0, 0, W, H);

    // Layout: Agent box on left, Environment box on right
    var boxW = Math.min(170, (W - 80) / 2 - 30);
    var boxH = 120;
    var agentX = 40;
    var envX = W - 40 - boxW;
    var boxY = (H - boxH) / 2 - 10;

    var isAgentActive = (phase === 0);
    var isEnvActive = (phase === 2);

    // Agent box
    ctx.fillStyle = isAgentActive ? accent : paper2;
    roundRect(agentX, boxY, boxW, boxH, 6);
    ctx.fill();
    ctx.strokeStyle = isAgentActive ? accent : rule;
    ctx.lineWidth = 1.5;
    ctx.stroke();

    ctx.fillStyle = isAgentActive ? paper : ink;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '500 15px "Fraunces", Georgia, serif';
    ctx.fillText('Agent', agentX + boxW / 2, boxY + 32);

    ctx.font = '11px "DM Mono", ui-monospace, monospace';
    ctx.fillStyle = isAgentActive ? paper : inkMute;
    ctx.fillText('π(a | s)', agentX + boxW / 2, boxY + 54);

    ctx.font = '10px "DM Mono", ui-monospace, monospace';
    ctx.fillStyle = isAgentActive ? paper : inkSoft;
    ctx.fillText('last action:', agentX + boxW / 2, boxY + 82);
    ctx.font = '500 12px "DM Mono", ui-monospace, monospace';
    ctx.fillText(lastAction, agentX + boxW / 2, boxY + 98);

    // Environment box
    ctx.fillStyle = isEnvActive ? accent : paper2;
    roundRect(envX, boxY, boxW, boxH, 6);
    ctx.fill();
    ctx.strokeStyle = isEnvActive ? accent : rule;
    ctx.lineWidth = 1.5;
    ctx.stroke();

    ctx.fillStyle = isEnvActive ? paper : ink;
    ctx.font = '500 15px "Fraunces", Georgia, serif';
    ctx.fillText('Environment', envX + boxW / 2, boxY + 32);

    ctx.font = '11px "DM Mono", ui-monospace, monospace';
    ctx.fillStyle = isEnvActive ? paper : inkMute;
    ctx.fillText("P(s' | s, a)", envX + boxW / 2, boxY + 54);

    // Visual state indicator: a horizontal bar showing envState in [0,10]
    var barY = boxY + 78;
    var barX = envX + 22;
    var barW2 = boxW - 44;
    ctx.fillStyle = isEnvActive ? 'rgba(255,255,255,0.3)' : rule;
    ctx.fillRect(barX, barY, barW2, 6);
    var markerX = barX + barW2 * (envState / 10);
    ctx.fillStyle = isEnvActive ? paper : accent;
    ctx.beginPath();
    ctx.arc(markerX, barY + 3, 5, 0, 2 * Math.PI);
    ctx.fill();

    ctx.font = '10px "DM Mono", ui-monospace, monospace';
    ctx.fillStyle = isEnvActive ? paper : inkMute;
    ctx.fillText('state = ' + envState.toFixed(2), envX + boxW / 2, boxY + 100);

    // Arrows
    var arrowY1 = boxY + 30;  // top arrow (action going right)
    var arrowY2 = boxY + boxH - 30;  // bottom arrow (obs + reward coming back)

    // Top arrow: action flowing from Agent to Environment (phase 1)
    var topActive = (phase === 1);
    drawArrow(
      agentX + boxW + 8, arrowY1,
      envX - 8, arrowY1,
      accent, topActive, phaseProgress
    );

    // Top arrow labels
    ctx.fillStyle = topActive ? accent : inkMute;
    ctx.font = '500 10px "DM Mono", ui-monospace, monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'bottom';
    var midX = (agentX + boxW + envX) / 2;
    ctx.fillText('action  aₜ', midX, arrowY1 - 6);

    // Bottom arrow: observation + reward flowing back (phase 3)
    var botActive = (phase === 3);
    drawArrow(
      envX - 8, arrowY2,
      agentX + boxW + 8, arrowY2,
      accent, botActive, phaseProgress
    );

    ctx.fillStyle = botActive ? accent : inkMute;
    ctx.font = '500 10px "DM Mono", ui-monospace, monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    ctx.fillText('observation  sₜ₊₁,   reward  rₜ₊₁', midX, arrowY2 + 8);

    // Reward readout as a small colored chip under the bottom arrow
    if (stepCount > 0) {
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';
      ctx.font = '10px "DM Mono", ui-monospace, monospace';
      ctx.fillStyle = inkMute;
      ctx.fillText('last r = ' + lastReward.toFixed(2), midX, arrowY2 + 24);
    }

    // Phase label at the bottom
    var phaseLabels = [
      '1. Agent selects action based on current observation',
      '2. Action sent to environment',
      '3. Environment transitions to new state',
      '4. New observation and reward returned to agent'
    ];
    ctx.textAlign = 'center';
    ctx.textBaseline = 'bottom';
    ctx.font = 'italic 11px "Newsreader", Georgia, serif';
    ctx.fillStyle = inkSoft;
    ctx.fillText(phaseLabels[phase], W / 2, H - 12);
  }

  document.getElementById('loopPlay').addEventListener('click', togglePlay);
  document.getElementById('loopStep').addEventListener('click', stepOnce);
  document.getElementById('loopReset').addEventListener('click', resetLoop);
  document.getElementById('loopSpeed').addEventListener('input', function(e) {
    document.getElementById('loopSpeedVal').textContent = (parseInt(e.target.value) / 10).toFixed(1) + '×';
  });

  window.addEventListener('resize', resize);
  resetLoop();
  setTimeout(resize, 50);
})();
</script>
