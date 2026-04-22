---
title: "Temporal Difference Learning, SARSA, and Q-Learning"
subtitle: "The one equation that runs every modern RL algorithm — and the one-character difference between cautious and fearless."
date: 2026-04-20 13:00:00 -0400
category: "Reinforcement Learning"
slug: rl-td-sarsa-q-learning
excerpt: "The Bellman equations say what a value function satisfies; temporal-difference learning says how to estimate it from samples. One update rule, two algorithms (SARSA and Q-learning), and a cliff-walking widget that makes on-policy vs off-policy click in 60 seconds."
reading_time: 18
---

This is Post 3 in the [field guide to reinforcement learning for control and robotics]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }}), and it picks up directly from [the foundations post]({{ '/posts/rl-foundations-mdps-value-functions-bellman/' | relative_url }}). There, we wrote down the MDP and the Bellman equations. Now comes the question that makes RL *RL*: how do you estimate value functions when you don't know the model?

The answer is **temporal-difference learning**, and it's the single most important idea that distinguishes reinforcement learning from classical dynamic programming. One update rule unlocks SARSA, Q-learning, DQN, the advantage signal in every actor-critic method, and GAE. If you understand the TD error, you understand the spine of modern RL.

## Three ways to estimate a value function

Given a policy $\pi$, there are three classical ways to compute $V^\pi(s)$. They differ in what they use as the target for each update.

| Method | Target | Needs model? | Bias | Variance |
|---|---|---|---|---|
| Dynamic programming | $\mathbb{E}_\pi[R + \gamma V(S')]$ exactly | Yes — $P, R$ | **None** | **None** |
| Monte Carlo | $G_t = \sum_k \gamma^k R_{t+k+1}$ | No | **None** | **High** |
| TD(0) | $R_{t+1} + \gamma V(S_{t+1})$ | No | Some (bootstraps) | **Low** |

Dynamic programming assumes you have the model — which you almost never do in the problems RL is meant for. Monte Carlo waits for the full return of each episode before updating, which gives unbiased estimates but enormous variance. TD(0) threads the needle: it bootstraps off its *own current estimate* of $V(S_{t+1})$ instead of waiting for the actual return, accepting a little bias in exchange for huge variance reductions. You can update every step, without a model, without episode boundaries.

The TD(0) update is the centerpiece of the field:

$$ V(S_t) \;\leftarrow\; V(S_t) \;+\; \alpha \underbrace{\bigl[\, R_{t+1} + \gamma V(S_{t+1}) - V(S_t) \,\bigr]}_{\delta_t \;-\; \text{the TD error}} $$

That quantity $\delta_t$ — the **TD error** — is everywhere in RL. Actor-critic methods use it as the advantage signal. GAE is just an exponentially-weighted sum of TD errors. Policy gradients effectively scale their updates by it. If one equation had to represent modern RL, it would be this one.

> **Control engineer's decoder ring.** TD is recursive estimation applied to value functions. The TD error $\delta_t$ is the *innovation* — exactly the quantity a Kalman filter uses to correct its prediction. Bootstrapping off $V(S_{t+1})$ instead of waiting for the full return is the same move a recursive filter makes instead of batch least-squares: trade a little bias for a lot less variance.

## From TD(0) to control — SARSA

Extend TD(0) to $Q$-values instead of $V$-values, and the update becomes a control algorithm. **SARSA** stands for the five things its update uses: $(S, A, R, S', A')$.

$$ Q(S_t, A_t) \;\leftarrow\; Q(S_t, A_t) + \alpha\bigl[\, R_{t+1} + \gamma\, Q(S_{t+1}, A_{t+1}) - Q(S_t, A_t) \,\bigr] $$

Here $A_{t+1}$ is the action **actually taken** under the current behavior policy — typically $\varepsilon$-greedy with respect to $Q$. SARSA therefore learns the value of the *exploratory* policy. If the policy is risky (high $\varepsilon$), SARSA knows, and it accounts for that — it learns a $Q$ that reflects the reality of occasionally doing something random.

## Q-learning — off-policy TD control

Swap the next-action value for the *maximum* over next actions and you get Q-learning:

$$ Q(S_t, A_t) \;\leftarrow\; Q(S_t, A_t) + \alpha\bigl[\, R_{t+1} + \gamma\, \max_{a'} Q(S_{t+1}, a') - Q(S_t, A_t) \,\bigr] $$

The update target refers to the **greedy** policy, even though the data came from $\varepsilon$-greedy. That's the essence of off-policy learning: the behavior policy generating the data can differ from the target policy being evaluated. Q-learning converges to $Q^\star$ regardless of how exploratory the behavior policy is — as long as it eventually visits every state-action pair.

> **The one-character difference.** SARSA uses $Q(S', A')$. Q-learning uses $\max_{a'} Q(S', a')$. That's it. From a code perspective, the diff is one line. From a behavior perspective, it's the difference between learning a policy that respects your exploration and learning the fearless optimum.

## The cliff — on-policy vs off-policy, visibly

The classic way to see the distinction is the cliff-walking gridworld from Sutton & Barto. Start (`S`) and goal (`G`) sit at either end of row 3. The strip of cells along the bottom row between them is a cliff: step onto it and you get reward −100 and reset to start. Every other move costs −1. Both SARSA and Q-learning learn on the same data-generation policy (ε-greedy), on the same grid, with the same hyperparameters. Watch what happens to their learned *greedy* policies.

<div class="rl-widget rl-cliff">

  <div class="rl-w-head">
    <div class="rl-w-title">Interactive — SARSA vs Q-learning on the cliff</div>
    <div class="rl-w-tag">on-policy vs off-policy</div>
  </div>

  <div class="rl-w-body">
    <div class="rl-w-ctrls">
      <div class="rl-w-ctrl">
        <label>ε-greedy <span class="val" id="cwEpsVal">0.10</span></label>
        <input type="range" id="cwEps" min="0" max="0.5" step="0.01" value="0.1">
      </div>
      <div class="rl-w-ctrl">
        <label>Learning rate α <span class="val" id="cwAlphaVal">0.50</span></label>
        <input type="range" id="cwAlpha" min="0.05" max="1.0" step="0.05" value="0.5">
      </div>
      <div class="rl-w-ctrl">
        <label>Discount γ <span class="val" id="cwGammaVal">0.95</span></label>
        <input type="range" id="cwGamma" min="0.5" max="0.999" step="0.001" value="0.95">
      </div>
    </div>

    <canvas id="cliffCanvas" class="rl-w-canvas" height="340"></canvas>

    <div class="rl-w-actions">
      <button type="button" class="rl-btn primary" id="cwTrain">▶ Train 500 episodes</button>
      <button type="button" class="rl-btn" id="cwStep">+50 episodes</button>
      <button type="button" class="rl-btn ghost" id="cwReset">Reset</button>
    </div>

    <div class="rl-stats-grid">
      <div class="rl-stat">
        <span class="k">SARSA · episodes</span>
        <span class="v" id="cwSarsaEps">0</span>
      </div>
      <div class="rl-stat">
        <span class="k">SARSA · avg return (last 50)</span>
        <span class="v" id="cwSarsaR">—</span>
      </div>
      <div class="rl-stat">
        <span class="k">Q-learning · episodes</span>
        <span class="v" id="cwQEps">0</span>
      </div>
      <div class="rl-stat">
        <span class="k">Q-learning · avg return (last 50)</span>
        <span class="v" id="cwQR">—</span>
      </div>
    </div>
  </div>

  <div class="rl-w-foot">
    S = start, G = goal, red strip = cliff (−100 reward + reset). Arrows show the greedy policy learned. The line traces the greedy path from S. Watch SARSA take the long safe route while Q-learning walks the cliff edge — that's the pedagogical signature of on-policy vs off-policy.
  </div>
</div>

The interesting thing isn't that Q-learning's greedy path is shorter. It's that **SARSA's learned policy reflects the exploration policy it will actually be executing**. Under ε-greedy rollout, stepping right next to the cliff is *risky* — one random action and you fall in, losing 100. SARSA sees those falls happen, and backs up negative value into cells adjacent to the cliff. The safe long route scores higher. Q-learning, by contrast, backs up the value of the greedy policy — which *would* never step off the cliff deliberately — and ends up believing the cliff-edge path is fine, even though the agent it's training is still ε-greedy and will fall off periodically.

Crank ε up higher (say, 0.3) and the gap widens dramatically. SARSA's policy shifts further from the cliff. Q-learning's greedy path doesn't change — it still believes the edge is optimal — but the average return of the *actual* rollouts gets worse because the ε-greedy falls are more frequent.

This is the core trade-off. If your agent will deploy with exploration (or noisy actuators, or disturbances you can't perfectly model), SARSA gives you a policy that accounts for reality. If you can guarantee greedy execution at deployment, Q-learning gives you the optimum.

## On-policy vs off-policy, precisely defined

The distinction is simple but gets tangled in practice. Two policies are at play:

- **Behavior policy** $b$ — the one that generates the data (rollouts, replay-buffer entries).
- **Target policy** $\pi$ — the one whose value or performance you're trying to learn or improve.

**On-policy** methods require $b = \pi$. Each update uses data generated by the current policy and only the current policy. PPO, A2C, TRPO, and SARSA are on-policy. This is why on-policy methods throw away rollouts after one gradient step — they can't be used once the policy has changed.

**Off-policy** methods allow $b \neq \pi$. Data from any past policy (or a human demonstrator, or a scripted controller) can be reused. Q-learning, DQN, SAC, TD3, and DDPG are off-policy. This is what makes replay buffers work.

### Importance sampling — the off-policy correction

If you want to use data generated under $b$ to estimate expectations under $\pi$, the samples must be reweighted:

$$ \mathbb{E}_\pi[f(X)] \;=\; \mathbb{E}_b\!\left[\, \frac{\pi(X)}{b(X)} f(X) \,\right] $$

The ratio $\rho = \pi/b$ is the **importance sampling weight**. For a whole trajectory the weight becomes a product $\prod_t \rho_t$, whose variance explodes — which is why off-policy *Monte Carlo* is typically useless in practice.

TD-style off-policy methods (Q-learning, DQN) sidestep this almost entirely, because the max-action target doesn't depend on the behavior distribution. Off-policy policy-gradient methods — V-trace in IMPALA, Retrace, Tree-Backup — must use truncated or clipped IS ratios to keep the variance bounded. We'll see this again when we get to modern deep RL.

## n-step TD and TD(λ) — bridging Monte Carlo and TD

TD(0) bootstraps after one step. Monte Carlo waits until the episode ends. You can sit anywhere between them with the **n-step return**:

$$ G_t^{(n)} \;=\; R_{t+1} + \gamma R_{t+2} + \cdots + \gamma^{n-1} R_{t+n} + \gamma^n V(S_{t+n}) $$

Larger $n$ means less bias (more real reward, less bootstrapping) but more variance. $n \in \{3, 5, 10\}$ is a common sweet spot in deep RL — it appears explicitly in Rainbow DQN and implicitly everywhere else.

**TD(λ)** is an exponentially-weighted average over every n-step return, with weight $(1-\lambda)\lambda^{n-1}$. It's elegantly implementable online via **eligibility traces** — a vector $\mathbf{e}_t$ that remembers recently visited states:

$$ \mathbf{e}_t \;=\; \gamma\lambda\, \mathbf{e}_{t-1} + \nabla V(S_t), \qquad \mathbf{w} \;\leftarrow\; \mathbf{w} + \alpha\,\delta_t\, \mathbf{e}_t $$

Eligibility traces are beautiful. They also rarely survive into modern deep RL, which prefers fixed-$n$ returns or the closely related **GAE(λ)** advantage estimator — a TD(λ)-style sum of TD errors over the rollout, standardized across a batch. We'll derive GAE when we hit policy gradients.

## The deadly triad

Sutton and Barto coined the term for three ingredients whose combination breaks classical convergence guarantees:

1. **Function approximation** — needed for any real state space (images, continuous physics).
2. **Bootstrapping** — using current estimates in the update target (the whole point of TD).
3. **Off-policy learning** — reusing data (the whole point of replay buffers).

Each pair is safe. Combining all three — which is exactly what DQN and every off-policy deep RL method does — admits counterexamples where the value estimate diverges even in toy problems. Baird's star MDP is the canonical example: a seven-state MDP that makes tabular Q-learning with function approximation diverge to infinity with a textbook-tuned learning rate. This is why deep RL stabilization is an ongoing research program, not a solved problem.

The standard mitigations baked into DQN and its descendants:

- **Target networks** — use a slowly updated copy $Q_{\bar\theta}$ in the bootstrapping target, so $\theta$ isn't chasing its own tail.
- **Experience replay** — break temporal correlation and make the update approximately i.i.d.
- **Clipped or Huber loss** — dampen the effect of large TD errors early in training.
- **Soft updates** — Polyak-averaged target network: $\bar\theta \leftarrow \tau\theta + (1-\tau)\bar\theta$, typically $\tau = 0.005$.

> **Rule of thumb.** If you ever see your critic loss climb without bound, or your Q-values grow to $10^4$ on a problem whose returns are $\mathcal{O}(10^2)$, the deadly triad is at work. Check (in order): target-network lag, reward scaling, discount factor, and whether your replay buffer has gone stale relative to the current policy.

## What to take away

The TD error is the quantity that flows through every modern RL algorithm. Once you see it in SARSA and Q-learning, you'll see it again in actor-critic (as the advantage signal), in DQN (as the loss), in PPO (inside GAE), and in SAC (in both the critic update and the entropy-regularized policy improvement).

The SARSA / Q-learning split previews the on-policy / off-policy split that defines the rest of the field. The next post picks up policy gradients and actor-critic — where the TD error stops being a value-function update and becomes the signal that tells a neural-network policy which way to move.

---

← Back to [the field guide]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }})

<!-- =====================================================
     Post-scoped styles — reuses the rl-widget pattern
     from the Foundations post, plus cliff-specific stats
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

  .article-body .rl-stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 12px 20px;
    margin: 18px 0 0;
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
    font-size: 1rem;
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
  var cv = document.getElementById('cliffCanvas');
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

  var W = 12, H = 4;
  var START = [3, 0], GOAL = [3, 11];
  var dr = [-1, 0, 1, 0], dc = [0, 1, 0, -1];
  var ARROW = ['↑', '→', '↓', '←'];

  function isCliff(r, c) { return r === 3 && c >= 1 && c <= 10; }

  function stepEnv(r, c, a) {
    var nr = Math.max(0, Math.min(H - 1, r + dr[a]));
    var nc = Math.max(0, Math.min(W - 1, c + dc[a]));
    if (isCliff(nr, nc)) return [START[0], START[1], -100, false];
    if (nr === GOAL[0] && nc === GOAL[1]) return [nr, nc, -1, true];
    return [nr, nc, -1, false];
  }

  function makeQ() {
    var Q = [];
    for (var r = 0; r < H; r++) {
      Q[r] = [];
      for (var c = 0; c < W; c++) Q[r][c] = [0, 0, 0, 0];
    }
    return Q;
  }
  function greedy(Q, r, c) {
    var best = 0, bv = Q[r][c][0];
    for (var a = 1; a < 4; a++) if (Q[r][c][a] > bv) { bv = Q[r][c][a]; best = a; }
    return best;
  }
  function epsGreedy(Q, r, c, eps) {
    if (Math.random() < eps) return Math.floor(Math.random() * 4);
    return greedy(Q, r, c);
  }

  function runSARSA(Q, eps, alpha, gamma) {
    var r = START[0], c = START[1];
    var a = epsGreedy(Q, r, c, eps);
    var total = 0, steps = 0;
    while (steps < 200) {
      var res = stepEnv(r, c, a);
      var nr = res[0], nc = res[1], rw = res[2], done = res[3];
      total += rw; steps++;
      if (done) {
        Q[r][c][a] += alpha * (rw - Q[r][c][a]);
        break;
      } else {
        var na = epsGreedy(Q, nr, nc, eps);
        Q[r][c][a] += alpha * (rw + gamma * Q[nr][nc][na] - Q[r][c][a]);
        r = nr; c = nc; a = na;
      }
    }
    return total;
  }
  function runQ(Q, eps, alpha, gamma) {
    var r = START[0], c = START[1];
    var total = 0, steps = 0;
    while (steps < 200) {
      var a = epsGreedy(Q, r, c, eps);
      var res = stepEnv(r, c, a);
      var nr = res[0], nc = res[1], rw = res[2], done = res[3];
      total += rw; steps++;
      if (done) {
        Q[r][c][a] += alpha * (rw - Q[r][c][a]);
        break;
      } else {
        var mx = Math.max(Q[nr][nc][0], Q[nr][nc][1], Q[nr][nc][2], Q[nr][nc][3]);
        Q[r][c][a] += alpha * (rw + gamma * mx - Q[r][c][a]);
        r = nr; c = nc;
      }
    }
    return total;
  }

  var Qs = makeQ(), Qq = makeQ();
  var epsSarsa = 0, epsQ = 0;
  var retSarsa = [], retQ = [];

  function valueColor(t, paperRgb, accentRgb) {
    var r = Math.round(paperRgb[0] + t * (accentRgb[0] - paperRgb[0]));
    var g = Math.round(paperRgb[1] + t * (accentRgb[1] - paperRgb[1]));
    var b = Math.round(paperRgb[2] + t * (accentRgb[2] - paperRgb[2]));
    return 'rgb(' + r + ',' + g + ',' + b + ')';
  }

  function drawGrid(Q, originX, originY, cellW, cellH, label) {
    var paper = cvar('--paper', '#f4efe6');
    var paper2 = cvar('--paper-2', '#ebe3d4');
    var rule = cvar('--rule', '#c8bfae');
    var ink = cvar('--ink', '#1a1814');
    var inkSoft = cvar('--ink-soft', '#4a4640');
    var inkMute = cvar('--ink-mute', '#8a8277');
    var accent = cvar('--accent', '#b94a1b');

    var paperRgb = parseHex(paper, [244, 239, 230]);
    var accentRgb = parseHex(accent, [185, 74, 27]);

    // V range
    var vmax = -Infinity, vmin = Infinity;
    for (var r2 = 0; r2 < H; r2++)
      for (var c2 = 0; c2 < W; c2++) {
        if (isCliff(r2, c2) || (r2 === GOAL[0] && c2 === GOAL[1])) continue;
        var v = Math.max(Q[r2][c2][0], Q[r2][c2][1], Q[r2][c2][2], Q[r2][c2][3]);
        if (v < vmin) vmin = v;
        if (v > vmax) vmax = v;
      }
    if (!isFinite(vmax) || vmax === vmin) { vmax = 0; vmin = -20; }

    // Section label
    ctx.fillStyle = accent;
    ctx.font = '500 12px "DM Mono", ui-monospace, monospace';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillText(label.toUpperCase(), originX, originY - 18);

    for (var r = 0; r < H; r++) {
      for (var c = 0; c < W; c++) {
        var x = originX + c * cellW;
        var y = originY + r * cellH;

        if (isCliff(r, c)) {
          // Cliff — solid dark red strip. Use accent-deep if available.
          ctx.fillStyle = cvar('--accent-deep', '#8a3412');
          ctx.globalAlpha = 0.85;
          ctx.fillRect(x, y, cellW - 1, cellH - 1);
          ctx.globalAlpha = 1;
        } else if (r === GOAL[0] && c === GOAL[1]) {
          ctx.fillStyle = accent;
          ctx.fillRect(x, y, cellW - 1, cellH - 1);
        } else if (r === START[0] && c === START[1]) {
          ctx.fillStyle = paper2;
          ctx.fillRect(x, y, cellW - 1, cellH - 1);
        } else {
          var v2 = Math.max(Q[r][c][0], Q[r][c][1], Q[r][c][2], Q[r][c][3]);
          var t = (v2 - vmin) / (vmax - vmin + 1e-9);
          var tt = Math.max(0, Math.min(1, t));
          ctx.fillStyle = valueColor(tt, paperRgb, accentRgb);
          ctx.fillRect(x, y, cellW - 1, cellH - 1);
        }

        ctx.strokeStyle = rule;
        ctx.lineWidth = 0.5;
        ctx.strokeRect(x + 0.5, y + 0.5, cellW - 1, cellH - 1);

        if (r === START[0] && c === START[1]) {
          ctx.fillStyle = ink;
          ctx.font = '700 13px "DM Mono", ui-monospace, monospace';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText('S', x + cellW / 2, y + cellH / 2);
        } else if (r === GOAL[0] && c === GOAL[1]) {
          ctx.fillStyle = paper;
          ctx.font = '700 13px "DM Mono", ui-monospace, monospace';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText('G', x + cellW / 2, y + cellH / 2);
        } else if (!isCliff(r, c)) {
          var a2 = greedy(Q, r, c);
          var v3 = Math.max(Q[r][c][0], Q[r][c][1], Q[r][c][2], Q[r][c][3]);
          var tVal = (v3 - vmin) / (vmax - vmin + 1e-9);
          ctx.fillStyle = tVal > 0.5 ? paper : ink;
          ctx.font = '500 14px "DM Mono", ui-monospace, monospace';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(ARROW[a2], x + cellW / 2, y + cellH / 2 + 1);
        }
      }
    }

    // Trace greedy path from start
    var rr = START[0], cc = START[1];
    ctx.strokeStyle = ink;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(originX + cc * cellW + cellW / 2, originY + rr * cellH + cellH / 2);
    for (var s = 0; s < 30; s++) {
      var aa = greedy(Q, rr, cc);
      var nrr = Math.max(0, Math.min(H - 1, rr + dr[aa]));
      var ncc = Math.max(0, Math.min(W - 1, cc + dc[aa]));
      if (isCliff(nrr, ncc)) break;
      ctx.lineTo(originX + ncc * cellW + cellW / 2, originY + nrr * cellH + cellH / 2);
      if (nrr === GOAL[0] && ncc === GOAL[1]) break;
      rr = nrr; cc = ncc;
    }
    ctx.stroke();
  }

  function render() {
    var dpr = window.devicePixelRatio || 1;
    var rect = cv.getBoundingClientRect();
    cv.width = rect.width * dpr;
    cv.height = 340 * dpr;
    cv.style.height = '340px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    var paper = cvar('--paper', '#f4efe6');
    ctx.fillStyle = paper;
    ctx.fillRect(0, 0, rect.width, 340);

    var marginX = 14;
    var cellW = Math.floor((rect.width - marginX * 2) / W);
    var cellH = 30;

    drawGrid(Qs, marginX, 28, cellW, cellH, 'SARSA — on-policy');
    drawGrid(Qq, marginX, 28 + 4 * cellH + 46, cellW, cellH, 'Q-learning — off-policy');
  }

  function avgRet(arr) {
    if (!arr.length) return '—';
    var tail = arr.slice(-50);
    var m = 0;
    for (var i = 0; i < tail.length; i++) m += tail[i];
    return (m / tail.length).toFixed(1);
  }
  function updateStats() {
    document.getElementById('cwSarsaEps').textContent = epsSarsa;
    document.getElementById('cwQEps').textContent = epsQ;
    document.getElementById('cwSarsaR').textContent = avgRet(retSarsa);
    document.getElementById('cwQR').textContent = avgRet(retQ);
  }

  function train(N) {
    var eps = parseFloat(document.getElementById('cwEps').value);
    var alpha = parseFloat(document.getElementById('cwAlpha').value);
    var gamma = parseFloat(document.getElementById('cwGamma').value);
    for (var i = 0; i < N; i++) {
      retSarsa.push(runSARSA(Qs, eps, alpha, gamma));
      retQ.push(runQ(Qq, eps, alpha, gamma));
      epsSarsa++; epsQ++;
    }
    if (retSarsa.length > 500) retSarsa = retSarsa.slice(-500);
    if (retQ.length > 500) retQ = retQ.slice(-500);
    render(); updateStats();
  }

  function reset() {
    Qs = makeQ(); Qq = makeQ();
    epsSarsa = 0; epsQ = 0;
    retSarsa = []; retQ = [];
    render(); updateStats();
  }

  function bindSlider(id, valId, fmt) {
    var el = document.getElementById(id);
    var val = document.getElementById(valId);
    var update = function() { val.textContent = fmt ? fmt(el.value) : el.value; };
    el.addEventListener('input', update);
    update();
  }
  bindSlider('cwEps', 'cwEpsVal', function(v) { return parseFloat(v).toFixed(2); });
  bindSlider('cwAlpha', 'cwAlphaVal', function(v) { return parseFloat(v).toFixed(2); });
  bindSlider('cwGamma', 'cwGammaVal', function(v) { return parseFloat(v).toFixed(3); });

  document.getElementById('cwTrain').addEventListener('click', function() { train(500); });
  document.getElementById('cwStep').addEventListener('click', function() { train(50); });
  document.getElementById('cwReset').addEventListener('click', reset);

  window.addEventListener('resize', render);
  setTimeout(render, 50);
})();
</script>
