---
title: "Reinforcement Learning for Control & Robotics — a Field Guide"
subtitle: "The methods that actually work on physical systems, the terminology that confuses everyone, and the rules of thumb that save weeks."
date: 2026-04-20 09:00:00 -0400
category: "Reinforcement Learning"
slug: rl-for-control-and-robotics-field-guide
excerpt: "A practitioner-oriented field guide to reinforcement learning for control and robotics. Start here: the RL family tree, a five-question algorithm selector, and the rules of thumb that take years to accumulate otherwise."
reading_time: 18
---

Reinforcement learning has an identity problem in engineering circles. Half the field treats it like a magic wand — sprinkle RL on a hard problem and watch it solve itself. The other half treats it like a toy — nice for games, useless on a dyno. Both views are wrong, and neither helps someone with a real control or robotics problem decide whether to reach for RL, and if so, which variant.

This is the first post in a series attempting to fix that — a working field guide to RL written from the perspective of someone who wants to actually *ship* policies onto physical systems. It's opinionated, because useful guides have to be.

## What this series covers

Seven posts. This one — the hub — lays out the map: the three architectural choices every RL algorithm makes, a quick-reference comparison of the algorithms you'll see in every paper, a five-question selector that tells you what to reach for first, and a compressed cheatsheet of the hyperparameters and traps that take years to learn. It's publishable on its own as an overview.

The six deep-dive posts below cover each topic with the math, the intuition, and an interactive demo where one makes sense. Each one can be read independently but they form a coherent arc.

1. [**Foundations — MDPs, value functions, and the Bellman equations.**]({{ '/posts/rl-foundations-mdps-value-functions-bellman/' | relative_url }}) The formalism and what it really means. The Markov assumption, reward shaping, discount factors, and why writing down the MDP correctly is 80% of the work.
2. [**Temporal difference learning, SARSA, and Q-learning.**]({{ '/posts/rl-td-sarsa-q-learning/' | relative_url }}) Bootstrapping, the TD error, on-policy vs off-policy — and why Q-learning is the algorithm that gave rise to everything modern.
3. [**Policy gradients and actor-critic.**]({{ '/posts/rl-policy-gradients-actor-critic/' | relative_url }}) REINFORCE → advantage estimation → TRPO → PPO. Where the variance comes from and what GAE does about it.
4. [**Exploration and modern deep RL — SAC, PPO, TD3, DDPG.**]({{ '/posts/rl-exploration-sac-ppo-td3-ddpg/' | relative_url }}) The four algorithms that dominate continuous control, what each one actually does, and when each one is the right call.
5. [**Model-based RL and MPC hybrids.**]({{ '/posts/rl-model-based-mpc-hybrids/' | relative_url }}) Where RL meets your existing MPC infrastructure. Learned dynamics, uncertainty-aware planning, and the hybrid architectures that work on real hardware.
6. [**Robotics in practice — sim-to-real, offline RL, and safe RL.**]({{ '/posts/rl-robotics-sim-to-real-offline-safe/' | relative_url }}) The parts no one teaches in school: domain randomization, offline policy learning, safety filters, and the difference between a policy that works in simulation and one that deploys.

The rest of this post is self-contained and delivers real value on its own — even if you never click any of the links above, you'll leave with a working taxonomy and concrete algorithmic recommendations.

## The RL family tree, without the confusion

Every RL algorithm makes three architectural choices. Once you see them, all the acronyms click into place.

### Axis 1 — Model-free vs model-based

Does the algorithm learn or use a model of the environment dynamics $P(s' \mid s, a)$?

- **Model-free** learns a value function and/or policy directly from reward signals. Simpler, more general, needs more data. *SAC, PPO, TD3, DQN.*

<div class="rl-minifig" data-concept="model-free">
  <div class="rl-minifig-head">Model-free — learn directly from the reward signal</div>
  <canvas class="rl-minifig-canvas" height="150"></canvas>
  <div class="rl-minifig-caption">The agent treats the environment as a black box. Observations and rewards flow in; actions flow out. No model of dynamics is ever built.</div>
</div>

- **Model-based** learns $\hat{P}$ and plans with it (MPC) or generates synthetic rollouts. Sample-efficient, but bias from the learned model can wreck the policy. *PILCO, MBPO, Dreamer, learned-MPC.*

<div class="rl-minifig" data-concept="model-based">
  <div class="rl-minifig-head">Model-based — learn dynamics, plan against it</div>
  <canvas class="rl-minifig-canvas" height="150"></canvas>
  <div class="rl-minifig-caption">The agent trains a dynamics model <em>f̂</em> from real experience, then rolls out imagined trajectories inside that model to plan without burning real samples.</div>
</div>

### Axis 2 — Value-based vs policy-based vs actor-critic

- **Value-based** — learn $Q^\star$ where the policy is implicitly $\arg\max_a Q$. Breaks with continuous actions. *Q-learning, DQN.*

<div class="rl-minifig" data-concept="value-based">
  <div class="rl-minifig-head">Value-based — learn Q, pick the argmax</div>
  <canvas class="rl-minifig-canvas" height="150"></canvas>
  <div class="rl-minifig-caption">The agent learns a Q-value for every discrete action at every state. The policy isn't stored — it's computed on demand as the arg-max action. As Q updates, the highlighted best action shifts.</div>
</div>

- **Policy-based** — learn $\pi$ directly by gradient ascent on expected return. Works with any action space but suffers high variance. *REINFORCE, vanilla policy gradient.*

<div class="rl-minifig" data-concept="policy-based">
  <div class="rl-minifig-head">Policy-based — learn π directly</div>
  <canvas class="rl-minifig-canvas" height="150"></canvas>
  <div class="rl-minifig-caption">The policy is a probability distribution over actions that the agent adjusts directly via gradient ascent on expected return. Works for continuous actions where an arg-max isn't meaningful.</div>
</div>

- **Actor-critic** — both. The critic ($Q$ or $V$) is used to reduce the variance of policy updates. *A2C, PPO, SAC, TD3, DDPG.* This is where everything modern lives.

<div class="rl-minifig" data-concept="actor-critic">
  <div class="rl-minifig-head">Actor-critic — one network decides, one network judges</div>
  <canvas class="rl-minifig-canvas" height="150"></canvas>
  <div class="rl-minifig-caption">The actor picks actions; the critic estimates their value. The critic's TD error becomes the signal that trains the actor — a variance-reduced advantage rather than a noisy raw return.</div>
</div>

### Axis 3 — On-policy vs off-policy

- **On-policy** algorithms can only learn from data generated by the current policy. You throw away rollouts after one gradient step. Stable but sample-inefficient. *PPO, A2C, TRPO.*

<div class="rl-minifig" data-concept="on-policy">
  <div class="rl-minifig-head">On-policy — collect, update once, discard</div>
  <canvas class="rl-minifig-canvas" height="150"></canvas>
  <div class="rl-minifig-caption">Rollouts from the current policy fill a buffer, the policy updates on them once, and the buffer empties. When the policy changes, old data is invalid.</div>
</div>

- **Off-policy** algorithms can reuse old data via a replay buffer. 10–100× more sample-efficient, but trickier to stabilize. *SAC, TD3, DDPG, DQN.*

<div class="rl-minifig" data-concept="off-policy">
  <div class="rl-minifig-head">Off-policy — replay buffer keeps everything</div>
  <canvas class="rl-minifig-canvas" height="150"></canvas>
  <div class="rl-minifig-caption">Transitions accumulate in a persistent buffer. The current policy samples random past transitions for every update, reusing experience from many past policy versions.</div>
</div>

> **For robotics specifically.** Real-robot samples are expensive. You almost always want **off-policy** (to reuse data) and **actor-critic** (to handle continuous actions). That narrows the field to SAC, TD3, DDPG, and model-based methods — which is why those four dominate the robotics literature.

<style>
  .article-body .rl-minifig {
    max-width: var(--read);
    margin: 18px auto 28px;
    background: var(--paper-2);
    border: 1px solid var(--rule);
    border-radius: 3px;
    padding: 14px 16px 10px;
  }
  .article-body .rl-minifig-head {
    font-family: var(--f-ui);
    font-size: .7rem;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: var(--accent);
    margin: 0 0 8px;
  }
  .article-body .rl-minifig-canvas {
    display: block;
    width: 100%;
    background: var(--paper);
    border: 1px solid var(--rule);
    border-radius: 2px;
  }
  .article-body .rl-minifig-caption {
    font-family: var(--f-body);
    font-size: .82rem;
    font-style: italic;
    color: var(--ink-mute);
    margin: 8px 0 0;
    line-height: 1.55;
  }
</style>

<script>
(function() {
  // ============================================================
  // Seven mini-figures for the three-axis taxonomy.
  // Each one is ~150px tall and animates continuously.
  // All share one rAF loop so they stay in sync.
  // ============================================================
  var figures = [];
  var startTime = performance.now();

  function cvar(name, fallback, el) {
    var v = getComputedStyle(el || document.documentElement).getPropertyValue(name).trim();
    return v || fallback;
  }
  function parseHex(hex, fallback) {
    var m = hex.match(/^#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i);
    if (!m) return fallback;
    return [parseInt(m[1], 16), parseInt(m[2], 16), parseInt(m[3], 16)];
  }

  function roundRect(ctx, x, y, w, h, r) {
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

  function arrow(ctx, x1, y1, x2, y2, color, pulse, phase, thickness) {
    ctx.strokeStyle = color;
    ctx.lineWidth = thickness || 1.25;
    ctx.globalAlpha = 0.5;
    ctx.setLineDash([4, 3]);
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.globalAlpha = 1;

    var ang = Math.atan2(y2 - y1, x2 - x1);
    var ahLen = 7;
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.moveTo(x2, y2);
    ctx.lineTo(x2 - ahLen * Math.cos(ang - Math.PI / 6), y2 - ahLen * Math.sin(ang - Math.PI / 6));
    ctx.lineTo(x2 - ahLen * Math.cos(ang + Math.PI / 6), y2 - ahLen * Math.sin(ang + Math.PI / 6));
    ctx.closePath();
    ctx.fill();

    if (pulse) {
      var t = phase;
      var dx = x1 + (x2 - x1) * t;
      var dy = y1 + (y2 - y1) * t;
      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.arc(dx, dy, 3.5, 0, 2 * Math.PI);
      ctx.fill();
    }
  }

  // Box with centered label. Returns {x, y, w, h, cx, cy} for edge-connecting arrows.
  function box(ctx, x, y, w, h, fill, stroke, color, label, sub, ink) {
    ctx.fillStyle = fill;
    roundRect(ctx, x, y, w, h, 4);
    ctx.fill();
    ctx.strokeStyle = stroke;
    ctx.lineWidth = 1;
    ctx.stroke();

    ctx.fillStyle = color;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '500 12px "Fraunces", Georgia, serif';
    ctx.fillText(label, x + w / 2, y + h / 2 - (sub ? 7 : 0));
    if (sub) {
      ctx.font = '9px "DM Mono", ui-monospace, monospace';
      ctx.fillStyle = ink;
      ctx.globalAlpha = 0.65;
      ctx.fillText(sub, x + w / 2, y + h / 2 + 8);
      ctx.globalAlpha = 1;
    }
    return { x: x, y: y, w: w, h: h, cx: x + w / 2, cy: y + h / 2 };
  }

  // -------------------------------------------------
  // Individual draw functions, one per concept.
  // -------------------------------------------------
  var drawers = {

    /* MODEL-FREE: Agent ↔ black-box environment, rewards flow back */
    'model-free': function(ctx, W, H, t, colors) {
      var agentX = 30, envX = W - 30 - 90;
      var boxH = 54;
      var boxY = H / 2 - boxH / 2 - 6;

      var agentFill = Math.sin(t * 1.5) > 0.6 ? colors.accent : colors.paper2;
      var agentText = agentFill === colors.accent ? colors.paper : colors.ink;
      box(ctx, agentX, boxY, 90, boxH, agentFill, agentFill === colors.accent ? colors.accent : colors.rule,
          agentText, 'Agent', 'π(a | s)', colors.ink);

      // Black-box environment with a ? inside
      ctx.fillStyle = '#3a342e';
      roundRect(ctx, envX, boxY, 90, boxH, 4);
      ctx.fill();
      ctx.strokeStyle = colors.ink;
      ctx.globalAlpha = 0.5;
      ctx.stroke();
      ctx.globalAlpha = 1;

      ctx.fillStyle = colors.paper;
      ctx.font = '500 12px "Fraunces", Georgia, serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('Environment', envX + 45, boxY + boxH / 2 - 7);
      ctx.font = '10px "DM Mono", ui-monospace, monospace';
      ctx.globalAlpha = 0.7;
      ctx.fillText('?', envX + 45, boxY + boxH / 2 + 8);
      ctx.globalAlpha = 1;

      // Top arrow: action -> env (phase 0 of cycle)
      var cycle = (t * 0.8) % 2;
      var topActive = cycle < 1;
      var topPhase = topActive ? cycle : 0;
      arrow(ctx, agentX + 90 + 4, boxY + 18, envX - 4, boxY + 18,
            colors.accent, topActive, topPhase, topActive ? 2 : 1.25);

      ctx.font = '9px "DM Mono", ui-monospace, monospace';
      ctx.fillStyle = colors.inkMute;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'bottom';
      ctx.fillText('action', (agentX + 90 + envX) / 2, boxY + 14);

      // Bottom arrow: reward + obs -> agent
      var botActive = cycle >= 1;
      var botPhase = botActive ? cycle - 1 : 0;
      arrow(ctx, envX - 4, boxY + boxH - 18, agentX + 90 + 4, boxY + boxH - 18,
            colors.accent, botActive, botPhase, botActive ? 2 : 1.25);

      ctx.textBaseline = 'top';
      ctx.fillStyle = colors.inkMute;
      ctx.fillText('obs + reward', (agentX + 90 + envX) / 2, boxY + boxH - 14);
    },

    /* MODEL-BASED: Agent, Env, Model \hat f (imagined rollouts from model) */
    'model-based': function(ctx, W, H, t, colors) {
      var boxW = 82, boxH = 48;
      var agentX = 16;
      var envX = W - 16 - boxW;
      var modelX = W / 2 - boxW / 2;
      var topY = 10;
      var botY = H - boxH - 14;

      // Agent (top-left)
      box(ctx, agentX, topY, boxW, boxH, colors.paper2, colors.rule, colors.ink, 'Agent', 'plan', colors.ink);

      // Environment (top-right)
      box(ctx, envX, topY, boxW, boxH, colors.paper2, colors.rule, colors.ink, 'Env', 'real', colors.ink);

      // Model f̂ (bottom-center) — glowing when in use
      var glow = (Math.sin(t * 2) + 1) / 2;
      var modelFill = colors.paper2;
      ctx.save();
      if (glow > 0.4) {
        ctx.shadowColor = colors.accent;
        ctx.shadowBlur = 6 * glow;
      }
      box(ctx, modelX, botY, boxW, boxH, modelFill, colors.accent, colors.accent, 'Model  f̂', 'learned', colors.ink);
      ctx.restore();

      // Real experience: Env → Agent (to train model too)
      arrow(ctx, envX, topY + boxH / 2, agentX + boxW + 4, topY + boxH / 2,
            colors.inkMute, false, 0, 1);

      // Training data: Env → Model (downward)
      arrow(ctx, envX + boxW / 2, topY + boxH + 2, modelX + boxW - 10, botY - 4,
            colors.inkMute, false, 0, 1);

      // Imagined rollouts: Model → Agent
      var cycle = (t * 1.2) % 1;
      arrow(ctx, modelX + 10, botY - 4, agentX + boxW / 2, topY + boxH + 2,
            colors.accent, true, cycle, 2);

      ctx.font = '9px "DM Mono", ui-monospace, monospace';
      ctx.fillStyle = colors.inkMute;
      ctx.textAlign = 'center';
      ctx.fillText('imagined rollouts', W / 2 - 30, H / 2 - 4);
    },

    /* VALUE-BASED: Bars of Q(s, a_i) at one state; argmax highlighted */
    'value-based': function(ctx, W, H, t, colors) {
      var n = 5;
      var labels = ['a₀', 'a₁', 'a₂', 'a₃', 'a₄'];
      // Q-values drift over time; one is the argmax
      var vals = [];
      var argmax = 0;
      var bestV = -Infinity;
      for (var i = 0; i < n; i++) {
        var base = [0.3, 0.6, 0.85, 0.55, 0.35][i];
        var wiggle = Math.sin(t * 0.8 + i * 0.7) * 0.08;
        vals.push(Math.max(0, Math.min(1, base + wiggle)));
        if (vals[i] > bestV) { bestV = vals[i]; argmax = i; }
      }

      var padL = 50, padR = 80, padT = 14, padB = 22;
      var plotW = W - padL - padR;
      var plotH = H - padT - padB;

      // Axis label
      ctx.fillStyle = colors.inkMute;
      ctx.font = '9px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = 'right';
      ctx.textBaseline = 'middle';
      ctx.fillText('Q(s, a)', padL - 6, padT + plotH / 2);

      // Baseline
      ctx.strokeStyle = colors.rule;
      ctx.lineWidth = 0.8;
      ctx.beginPath();
      ctx.moveTo(padL, padT + plotH);
      ctx.lineTo(padL + plotW, padT + plotH);
      ctx.stroke();

      var barW = plotW / n * 0.65;
      var gap = plotW / n - barW;
      for (var j = 0; j < n; j++) {
        var x = padL + (plotW / n) * j + gap / 2;
        var h = plotH * vals[j];
        ctx.fillStyle = (j === argmax) ? colors.accent : colors.paper2;
        ctx.strokeStyle = (j === argmax) ? colors.accent : colors.rule;
        ctx.lineWidth = 1;
        ctx.fillRect(x, padT + plotH - h, barW, h);
        ctx.strokeRect(x + 0.5, padT + plotH - h + 0.5, barW, h);

        ctx.fillStyle = colors.inkMute;
        ctx.font = '9px "DM Mono", ui-monospace, monospace';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'top';
        ctx.fillText(labels[j], x + barW / 2, padT + plotH + 6);
      }

      // Label the argmax
      var bx = padL + (plotW / n) * argmax + gap / 2 + barW / 2;
      ctx.strokeStyle = colors.accent;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(bx, padT + plotH - plotH * vals[argmax] - 4);
      ctx.lineTo(padL + plotW + 14, padT + plotH - plotH * vals[argmax] - 4);
      ctx.stroke();

      ctx.fillStyle = colors.accent;
      ctx.textAlign = 'left';
      ctx.textBaseline = 'middle';
      ctx.font = '500 10px "DM Mono", ui-monospace, monospace';
      ctx.fillText('argmax', padL + plotW + 18, padT + plotH - plotH * vals[argmax] - 4);
    },

    /* POLICY-BASED: Gaussian policy distribution with mean drifting toward target */
    'policy-based': function(ctx, W, H, t, colors) {
      var padL = 30, padR = 20, padT = 14, padB = 22;
      var plotW = W - padL - padR;
      var plotH = H - padT - padB;

      // Target action a*
      var target = 1.6;
      // Policy mean drifts toward target with some overshoot
      var mu = target * (1 - Math.exp(-t * 0.5)) + Math.sin(t * 1.2) * 0.08;
      var sigma = Math.max(0.35, 0.9 * Math.exp(-t * 0.25));

      // Baseline
      ctx.strokeStyle = colors.rule;
      ctx.lineWidth = 0.8;
      ctx.beginPath();
      ctx.moveTo(padL, padT + plotH);
      ctx.lineTo(padL + plotW, padT + plotH);
      ctx.stroke();

      // Axis labels (action values -3 to 3)
      ctx.fillStyle = colors.inkMute;
      ctx.font = '9px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';
      for (var a = -2; a <= 2; a++) {
        var ax = padL + (a + 2) / 4 * plotW;
        ctx.fillText(a.toString(), ax, padT + plotH + 6);
      }
      ctx.fillText('action', padL + plotW / 2, padT + plotH + 18);

      // Target line (a*)
      var tx = padL + (target + 2) / 4 * plotW;
      ctx.strokeStyle = colors.ink;
      ctx.globalAlpha = 0.6;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(tx, padT);
      ctx.lineTo(tx, padT + plotH);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.globalAlpha = 1;

      ctx.fillStyle = colors.ink;
      ctx.font = '9px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = 'left';
      ctx.textBaseline = 'top';
      ctx.fillText('a*', tx + 3, padT);

      // Gaussian curve
      var N = 120;
      var maxPdf = 1 / (sigma * Math.sqrt(2 * Math.PI));
      var accentRgb = parseHex(colors.accent, [185, 74, 27]);
      ctx.beginPath();
      for (var i = 0; i <= N; i++) {
        var av = -2 + 4 * i / N;
        var pdf = Math.exp(-0.5 * Math.pow((av - mu) / sigma, 2)) / (sigma * Math.sqrt(2 * Math.PI));
        var x = padL + (av + 2) / 4 * plotW;
        var y = padT + plotH - (pdf / maxPdf) * plotH * 0.85;
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.lineTo(padL + plotW, padT + plotH);
      ctx.lineTo(padL, padT + plotH);
      ctx.closePath();
      ctx.fillStyle = 'rgba(' + accentRgb[0] + ',' + accentRgb[1] + ',' + accentRgb[2] + ',0.2)';
      ctx.fill();

      ctx.strokeStyle = colors.accent;
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (var i2 = 0; i2 <= N; i2++) {
        var av2 = -2 + 4 * i2 / N;
        var pdf2 = Math.exp(-0.5 * Math.pow((av2 - mu) / sigma, 2)) / (sigma * Math.sqrt(2 * Math.PI));
        var x2 = padL + (av2 + 2) / 4 * plotW;
        var y2 = padT + plotH - (pdf2 / maxPdf) * plotH * 0.85;
        if (i2 === 0) ctx.moveTo(x2, y2); else ctx.lineTo(x2, y2);
      }
      ctx.stroke();

      // Mu marker
      var muX = padL + (mu + 2) / 4 * plotW;
      var muMaxY = padT + plotH - plotH * 0.85;
      ctx.fillStyle = colors.ink;
      ctx.beginPath();
      ctx.arc(muX, muMaxY, 3.5, 0, 2 * Math.PI);
      ctx.fill();

      // Label
      ctx.fillStyle = colors.accent;
      ctx.font = '500 10px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = 'left';
      ctx.textBaseline = 'middle';
      ctx.fillText('π(a | s)', padL + 4, padT + 10);
    },

    /* ACTOR-CRITIC: Actor box, Critic box, TD error flowing from critic → actor */
    'actor-critic': function(ctx, W, H, t, colors) {
      var boxW = 90, boxH = 48;
      var actorX = 18;
      var criticX = W - 18 - boxW;
      var y = (H - boxH) / 2 - 8;

      // Actor
      box(ctx, actorX, y, boxW, boxH, colors.paper2, colors.rule, colors.ink, 'Actor', 'π_θ', colors.ink);

      // Critic — pulses when it "judges"
      var judge = (Math.sin(t * 1.6) + 1) / 2;
      var critFill = judge > 0.5 ? colors.accent : colors.paper2;
      var critText = critFill === colors.accent ? colors.paper : colors.ink;
      var critInk = critFill === colors.accent ? colors.paper : colors.ink;
      box(ctx, criticX, y, boxW, boxH, critFill, critFill === colors.accent ? colors.accent : colors.rule,
          critText, 'Critic', 'V_φ / Q_φ', critInk);

      // Action arrow: Actor → Critic (top)
      var topCycle = (t * 1.2) % 1;
      arrow(ctx, actorX + boxW + 4, y + 14, criticX - 4, y + 14,
            colors.inkMute, false, 0, 1);
      ctx.fillStyle = colors.inkMute;
      ctx.font = '9px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'bottom';
      ctx.fillText('action', (actorX + boxW + criticX) / 2, y + 10);

      // TD error: Critic → Actor (bottom), accent-colored, pulsing
      var botCycle = (t * 1.2) % 1;
      arrow(ctx, criticX - 4, y + boxH - 14, actorX + boxW + 4, y + boxH - 14,
            colors.accent, true, botCycle, 2);
      ctx.fillStyle = colors.accent;
      ctx.font = '500 9px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';
      ctx.fillText('TD error  δ', (actorX + boxW + criticX) / 2, y + boxH - 10);

      // Environment note below
      ctx.fillStyle = colors.inkMute;
      ctx.font = 'italic 9px "Newsreader", serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'bottom';
      ctx.fillText('(rewards and transitions from env, not shown)', W / 2, H - 6);
    },

    /* ON-POLICY: Buffer fills, one update flash, buffer clears, repeat */
    'on-policy': function(ctx, W, H, t, colors) {
      var bufferX = W / 2 - 90;
      var bufferY = 26;
      var bufferW = 180, bufferH = 44;
      var nSlots = 8;
      var slotW = (bufferW - 10) / nSlots;

      // 3-phase cycle: fill (0..1) → update flash (1..1.4) → clear (1.4..1.5) → hold empty (1.5..2)
      var cycle = (t * 0.6) % 2.2;

      // Draw the buffer frame
      ctx.strokeStyle = colors.rule;
      ctx.lineWidth = 1;
      roundRect(ctx, bufferX, bufferY, bufferW, bufferH, 3);
      ctx.stroke();

      // Buffer label
      ctx.fillStyle = colors.inkMute;
      ctx.font = '9px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'bottom';
      ctx.fillText('rollout buffer', bufferX + bufferW / 2, bufferY - 4);

      // Fill slots based on cycle
      var filled;
      var highlight = false;
      if (cycle < 1) {
        filled = Math.floor(cycle * nSlots);
      } else if (cycle < 1.4) {
        filled = nSlots;
        highlight = true; // update flash
      } else {
        filled = 0;
      }

      for (var i = 0; i < nSlots; i++) {
        var sx = bufferX + 5 + i * slotW;
        var sy = bufferY + 5;
        var sh = bufferH - 10;
        if (i < filled) {
          ctx.fillStyle = highlight ? colors.accent : colors.paper2;
          ctx.fillRect(sx, sy, slotW - 3, sh);
          ctx.strokeStyle = highlight ? colors.accent : colors.rule;
          ctx.lineWidth = 0.5;
          ctx.strokeRect(sx + 0.25, sy + 0.25, slotW - 3, sh);
        } else {
          ctx.fillStyle = colors.paper;
          ctx.fillRect(sx, sy, slotW - 3, sh);
          ctx.strokeStyle = colors.rule;
          ctx.lineWidth = 0.5;
          ctx.setLineDash([2, 2]);
          ctx.strokeRect(sx + 0.25, sy + 0.25, slotW - 3, sh);
          ctx.setLineDash([]);
        }
      }

      // Phase label
      var phaseLabel;
      if (cycle < 1) phaseLabel = '① collect rollout from current π';
      else if (cycle < 1.4) phaseLabel = '② one gradient update';
      else phaseLabel = '③ discard — old data is stale';

      ctx.fillStyle = cycle < 1.4 && cycle > 1 ? colors.accent : colors.inkMute;
      ctx.font = 'italic 10px "Newsreader", serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';
      ctx.fillText(phaseLabel, W / 2, bufferY + bufferH + 10);
    },

    /* OFF-POLICY: Buffer accumulates to full, random sampling flashes */
    'off-policy': function(ctx, W, H, t, colors) {
      var bufferX = W / 2 - 110;
      var bufferY = 26;
      var bufferW = 220, bufferH = 44;
      var nSlots = 14;
      var slotW = (bufferW - 10) / nSlots;

      // Buffer label
      ctx.fillStyle = colors.inkMute;
      ctx.font = '9px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'bottom';
      ctx.fillText('replay buffer (persistent)', bufferX + bufferW / 2, bufferY - 4);

      // Buffer frame
      ctx.strokeStyle = colors.rule;
      ctx.lineWidth = 1;
      roundRect(ctx, bufferX, bufferY, bufferW, bufferH, 3);
      ctx.stroke();

      // Buffer fills in the first ~5 seconds of t, stays full thereafter
      var fillRatio = Math.min(1, t / 5);
      var filled = Math.floor(fillRatio * nSlots);

      // Sampling flash — two-ish random slots highlight each second
      var sampleTime = t * 1.5;
      var samplePhase = sampleTime % 1;
      var samplingActive = samplePhase < 0.3;
      // Pseudorandom indices from sampleTime integer
      var seed = Math.floor(sampleTime);
      var s1 = seed % nSlots;
      var s2 = (seed * 7 + 3) % nSlots;
      var s3 = (seed * 13 + 5) % nSlots;
      var sampled = new Set([s1, s2, s3]);

      for (var i = 0; i < nSlots; i++) {
        var sx = bufferX + 5 + i * slotW;
        var sy = bufferY + 5;
        var sh = bufferH - 10;
        if (i < filled) {
          var isSampled = samplingActive && sampled.has(i);
          ctx.fillStyle = isSampled ? colors.accent : colors.paper2;
          ctx.fillRect(sx, sy, slotW - 2, sh);
          ctx.strokeStyle = isSampled ? colors.accent : colors.rule;
          ctx.lineWidth = 0.5;
          ctx.strokeRect(sx + 0.25, sy + 0.25, slotW - 2, sh);
        } else {
          ctx.fillStyle = colors.paper;
          ctx.fillRect(sx, sy, slotW - 2, sh);
          ctx.strokeStyle = colors.rule;
          ctx.lineWidth = 0.5;
          ctx.setLineDash([2, 2]);
          ctx.strokeRect(sx + 0.25, sy + 0.25, slotW - 2, sh);
          ctx.setLineDash([]);
        }
      }

      // Phase label
      var phaseLabel = samplingActive
        ? '→ sample mini-batch (any past transition)'
        : '→ append new transition; nothing is discarded';
      ctx.fillStyle = samplingActive ? colors.accent : colors.inkMute;
      ctx.font = 'italic 10px "Newsreader", serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';
      ctx.fillText(phaseLabel, W / 2, bufferY + bufferH + 10);
    }
  };

  // -------------------------------------------------
  // Shared animation loop
  // -------------------------------------------------
  function resizeAll() {
    figures.forEach(function(fig) {
      var rect = fig.cv.getBoundingClientRect();
      var dpr = window.devicePixelRatio || 1;
      fig.cv.width = rect.width * dpr;
      fig.cv.height = 150 * dpr;
      fig.cv.style.height = '150px';
      fig.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    });
  }

  function frame() {
    var now = performance.now();
    var t = (now - startTime) / 1000;

    figures.forEach(function(fig) {
      // Skip frames for figures that aren't near the viewport (cheap optimization)
      var rect = fig.cv.getBoundingClientRect();
      if (rect.bottom < -200 || rect.top > window.innerHeight + 200) return;

      var W = rect.width, H = 150;
      // Clear
      var colors = {
        paper: cvar('--paper', '#f4efe6', fig.cv),
        paper2: cvar('--paper-2', '#ebe3d4', fig.cv),
        rule: cvar('--rule', '#c8bfae', fig.cv),
        ink: cvar('--ink', '#1a1814', fig.cv),
        inkMute: cvar('--ink-mute', '#8a8277', fig.cv),
        inkSoft: cvar('--ink-soft', '#4a4640', fig.cv),
        accent: cvar('--accent', '#b94a1b', fig.cv),
        accentDeep: cvar('--accent-deep', '#8a3412', fig.cv)
      };

      fig.ctx.fillStyle = colors.paper;
      fig.ctx.fillRect(0, 0, W, H);

      if (drawers[fig.concept]) {
        drawers[fig.concept](fig.ctx, W, H, t, colors);
      }
    });
    requestAnimationFrame(frame);
  }

  // Register all mini-figures on the page
  document.querySelectorAll('.rl-minifig').forEach(function(fig) {
    var cv = fig.querySelector('canvas');
    var concept = fig.dataset.concept;
    figures.push({ el: fig, cv: cv, ctx: cv.getContext('2d'), concept: concept });
  });

  window.addEventListener('resize', resizeAll);
  resizeAll();
  requestAnimationFrame(frame);
})();
</script>

### Quick-reference comparison

| Algorithm | Actions | On/Off | Sample eff. | Robustness |
|---|---|---|---|---|
| Q-learning | Discrete | Off | High | OK |
| DQN | Discrete | Off | Medium | OK |
| REINFORCE | Any | On | Low | Poor |
| A2C / A3C | Any | On | Low | OK |
| PPO | Any | On | Medium | **Excellent** |
| DDPG | Continuous | Off | High | Fragile |
| TD3 | Continuous | Off | High | Good |
| SAC | Continuous | Off | High | **Excellent** |
| MBPO / Dreamer | Continuous | Off (MB) | Very high | Depends on model |

## Algorithm selector

Answer five questions. Get a recommendation with reasoning. Not a substitute for experimenting — but a solid starting point that will keep you from wasting a week on the wrong family of methods.

<div class="rl-selector" markdown="0">

  <div class="rl-q" data-qname="actions">
    <div class="rl-qnum">Question 1 of 5</div>
    <div class="rl-qtext">What do your actions look like?</div>
    <div class="rl-opts">
      <button type="button" class="rl-opt" data-val="continuous">Continuous (torque, velocity, pose)</button>
      <button type="button" class="rl-opt" data-val="discrete">Discrete (modes, switches, N choices)</button>
    </div>
  </div>

  <div class="rl-q" data-qname="data">
    <div class="rl-qnum">Question 2 of 5</div>
    <div class="rl-qtext">How expensive is collecting data?</div>
    <div class="rl-opts">
      <button type="button" class="rl-opt" data-val="cheap">Fast sim (100k+ steps/sec, GPU env)</button>
      <button type="button" class="rl-opt" data-val="medium">Slow sim (real-time physics)</button>
      <button type="button" class="rl-opt" data-val="expensive">Real hardware or very slow sim</button>
    </div>
  </div>

  <div class="rl-q" data-qname="smooth">
    <div class="rl-qnum">Question 3 of 5</div>
    <div class="rl-qtext">How smooth / Markovian is the system?</div>
    <div class="rl-opts">
      <button type="button" class="rl-opt" data-val="smooth">Smooth, mostly-Markov (locomotion, flight, motor control)</button>
      <button type="button" class="rl-opt" data-val="contact">Heavy contact / partial observability / long horizons</button>
      <button type="button" class="rl-opt" data-val="vision">Image observations</button>
    </div>
  </div>

  <div class="rl-q" data-qname="det">
    <div class="rl-qnum">Question 4 of 5</div>
    <div class="rl-qtext">Do you need a deterministic policy?</div>
    <div class="rl-opts">
      <button type="button" class="rl-opt" data-val="yes">Yes (certification, control theory, interpretability)</button>
      <button type="button" class="rl-opt" data-val="no">No (stochastic is fine)</button>
    </div>
  </div>

  <div class="rl-q" data-qname="safety">
    <div class="rl-qnum">Question 5 of 5</div>
    <div class="rl-qtext">Safety constraints during training / deployment?</div>
    <div class="rl-opts">
      <button type="button" class="rl-opt" data-val="hard">Hard constraints (must not violate)</button>
      <button type="button" class="rl-opt" data-val="soft">Soft (prefer to not violate)</button>
      <button type="button" class="rl-opt" data-val="none">None / simulation only</button>
    </div>
  </div>

  <div class="rl-rec" id="rlRec">
    <div class="rl-rec-label">Recommendation</div>
    <div class="rl-rec-title" id="rlRecTitle"></div>
    <div class="rl-rec-body" id="rlRecBody"></div>
    <div class="rl-rec-alt" id="rlRecAlt"></div>
  </div>

  <div class="rl-foot">
    A starting point, not a verdict. Always A/B test against a simple baseline — random search, classic control, a hand-tuned PID — before committing.
  </div>

</div>

## Hyperparameters, debugging, and silent failures

These deserve their own post. See **[Practical RL Engineering: Hyperparameters, Debugging, and Silent Failures]({{ '/posts/rl-practical-engineering-hyperparameters-debugging/' | relative_url }})** for the universal deep-RL defaults that almost always work, the order in which to debug a policy that won't learn, and the traps that silently cost you weekends. It's the most important page in the series for practical work.

## When to stop RL and use classical control

RL is a tool, not a goal. Reach for it only when simpler methods have failed.

- **Linear-ish dynamics, quadratic cost** — use LQR. Closed-form, optimal, beats anything you'd train with RL.
- **Known nonlinear model with constraints** — use NMPC. It works, it's understood, it gives guarantees.
- **Tracking with well-modeled disturbances** — $H_\infty$ or robust MPC. RL gives you no guarantees here.
- **Tasks with decades of engineering maturity** (PID for current loops, cascaded control for drives) — *don't use RL.* RL shines where modeling is hard, rewards are complex, or the solution is non-convex. Not in places where you already have good analytical tools.

The smartest RL teams use classical control where it works and RL only where it adds something. A learned residual on top of a stabilizing controller is almost always safer and more sample-efficient than learning the whole thing end-to-end.

## Further reading, curated

- **Sutton & Barto,** *Reinforcement Learning: An Introduction* (2nd ed., 2018). The canonical textbook. Chapters 1–10 are essential; the rest is reference.
- **Spinning Up in Deep RL** — OpenAI's educational codebase. Read the essay; copy the algorithm implementations; use them as templates.
- **Stable-Baselines3 and CleanRL** — production-grade implementations you can actually extend. CleanRL for single-file reference; SB3 for real projects.
- **"The 37 Implementation Details of PPO"** (Huang et al.) — mandatory reading before writing PPO from scratch.
- **DreamerV3 and TD-MPC2** — the current state-of-the-art for "one algorithm that just works."
- **Berkeley CS285 (Levine)** — free lectures, rigorous, current.
- **Isaac Lab / Isaac Gym** — where to train robotics policies fast.

---

## Glossary of acronyms {#glossary}

Every post in this series uses a few of these. Bookmark this section — it's the single reference for the whole field guide. Acronyms are grouped by what they *are*, not alphabetically, because that's the grouping that actually helps remember them.

**Foundational concepts.**

- **MDP** — Markov Decision Process. The formal object every RL algorithm operates on. Defined as the tuple $\langle \mathcal{S}, \mathcal{A}, P, R, \gamma \rangle$.
- **POMDP** — Partially Observable MDP. An MDP where the agent sees an observation $o_t$ that is a noisy or incomplete function of the true state $s_t$.
- **CMDP** — Constrained MDP. An MDP with additional cost functions that must stay below thresholds. The formalism for safe RL.
- **TD** — Temporal Difference. The one-step bootstrap update rule that defines everything from SARSA to SAC. $\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$ is the TD error.
- **GAE** — Generalized Advantage Estimation (Schulman et al., 2016). An exponentially-weighted sum of TD errors used as the advantage signal in PPO and most on-policy methods. The standard choice of $\lambda$ is 0.95.
- **HJB** — Hamilton-Jacobi-Bellman equation. The continuous-time optimal-control PDE that the Bellman equation is the discrete-time, stochastic, reward-signed analog of.
- **MC** — Monte Carlo. Methods that estimate values by averaging complete episode returns. High variance, zero bias.
- **KL** — Kullback-Leibler divergence. Measure of how different two probability distributions are. Used to constrain how much a policy can change per update (TRPO, PPO).

**Classical / value-based algorithms.**

- **SARSA** — State-Action-Reward-State-Action. On-policy TD control algorithm named for the five things its update rule uses.
- **DQN** — Deep Q-Network (Mnih et al., 2015). The original deep RL success on Atari. Q-learning with a neural network, replay buffer, and target network.
- **Rainbow DQN** — DQN with six additional improvements (Double Q, Dueling, Prioritized Experience Replay, Noisy Nets, Distributional RL, Multi-step returns) combined.
- **UCB** — Upper Confidence Bound. Exploration strategy that picks actions by $\arg\max_a[\hat Q_a + c\sqrt{\ln t / N_a}]$. Provably logarithmic regret in bandits.
- **PUCT** — Predictor + UCB applied to Trees. The tree-search formula from AlphaZero.

**Policy-gradient and actor-critic algorithms.**

- **REINFORCE** — The original Monte-Carlo policy gradient algorithm (Williams, 1992). Named partly as an acronym: REward Increment = Nonnegative Factor × Offset Reinforcement × Characteristic Eligibility.
- **A2C** — Advantage Actor-Critic. Synchronous version of A3C.
- **A3C** — Asynchronous Advantage Actor-Critic (Mnih et al., 2016). Multi-worker on-policy actor-critic with asynchronous updates.
- **TRPO** — Trust Region Policy Optimization (Schulman et al., 2015). Policy gradient method with a hard KL-divergence constraint.
- **PPO** — Proximal Policy Optimization (Schulman et al., 2017). TRPO's first-order replacement. The clipped-ratio surrogate is its defining trick. The *simulation default*.

**Off-policy deterministic and stochastic methods.**

- **DPG** — Deterministic Policy Gradient (Silver et al., 2014). Underlying theorem for DDPG.
- **DDPG** — Deep Deterministic Policy Gradient (Lillicrap et al., 2015). First widely-used deep RL for continuous control. Fragile; use TD3 or SAC instead.
- **TD3** — Twin Delayed Deep Deterministic policy gradient (Fujimoto et al., 2018). DDPG with three stability fixes: twin critics, delayed actor updates, target policy smoothing.
- **SAC** — Soft Actor-Critic (Haarnoja et al., 2018). Actor-critic with maximum-entropy objective. The *robotics default*.
- **V-trace** — Vectorized off-policy correction used in IMPALA. Truncated importance sampling for distributed on-policy-ish learning.
- **IMPALA** — Importance-weighted Actor-Learner Architecture. Distributed actor-critic with V-trace.
- **MPO** — Maximum a Posteriori Policy Optimization. KL-regularized actor-critic from DeepMind.

**Model-based methods.**

- **MPC** — Model Predictive Control. The classical controller template; RL methods inherit or extend it.
- **MPPI** — Model Predictive Path Integral (Williams et al., 2017). Sampling-based MPC. Exp-weighted over sampled trajectories.
- **CEM** — Cross Entropy Method. Sampling-based optimization; iteratively refits a sampling distribution to top-performing samples.
- **iLQR** — iterative Linear Quadratic Regulator. Gradient-based MPC that linearizes dynamics at each step.
- **PILCO** — Probabilistic Inference for Learning COntrol (Deisenroth & Rasmussen, 2011). GP dynamics + analytic policy gradients. Absurdly sample-efficient.
- **GP** — Gaussian Process. A distribution over functions. Used as a dynamics model in PILCO; see [the GP post]({{ '/posts/gaussian-processes-interactive-explainer/' | relative_url }}) for details.
- **PETS** — Probabilistic Ensembles with Trajectory Sampling (Chua et al., 2018). Ensemble dynamics + MPC. The canonical "MPC with learned dynamics" method.
- **MBPO** — Model-Based Policy Optimization (Janner et al., 2019). Dyna-style — generate short imagined rollouts from a learned model, train SAC on real + imagined.
- **STEVE** — Stochastic Ensemble Value Expansion. Model-based variant that weighs imagined rollouts by ensemble uncertainty.
- **Dreamer / DreamerV3** (Hafner et al., 2020, 2023) — World-model RL. Latent dynamics + actor-critic trained entirely in imagination. DreamerV3 is the fixed-hyperparameter variant.
- **TD-MPC / TD-MPC2** (Hansen et al., 2022, 2024) — Hybrid of learned world model, online MPPI planning, and an amortized policy. Current SOTA on many robotics benchmarks.

**Exploration and intrinsic-motivation methods.**

- **ε-greedy** — With probability $\varepsilon$ pick a random action, else pick greedy. Simplest thing that works.
- **OU noise** — Ornstein-Uhlenbeck noise. Temporally-correlated Gaussian noise originally used in DDPG exploration. Mostly deprecated in favor of plain Gaussian.
- **NoisyNets** (Fortunato et al., 2017) — Replace linear layers with learned-noise variants. Parameter-space exploration.
- **ICM** — Intrinsic Curiosity Module (Pathak et al., 2017). Prediction-error-based exploration bonus learned via inverse-dynamics features.
- **RND** — Random Network Distillation (Burda et al., 2018). Prediction error against a fixed random network as the intrinsic reward. Dominated Montezuma's Revenge.
- **NGU / Agent57** (Badia et al., 2020) — DeepMind's exploration-rich agent that first achieved above-human on every Atari game.
- **HER** — Hindsight Experience Replay (Andrychowicz et al., 2017). Relabel failed rollouts with the state they actually reached as the goal. Crucial for goal-conditioned sparse-reward tasks.

**Imitation and offline RL.**

- **BC** — Behavioral Cloning. Supervised learning on expert $(s, a)$ pairs. First thing to try when you have demonstrations.
- **DAgger** — Dataset Aggregation (Ross et al., 2011). Iterative BC with expert queries on states the learner visits.
- **GAIL** — Generative Adversarial Imitation Learning (Ho & Ermon, 2016). Imitation as a two-player game against a discriminator.
- **IRL** — Inverse Reinforcement Learning. Infer a reward function from expert behavior, then run forward RL on it.
- **CQL** — Conservative Q-Learning (Kumar et al., 2020). Offline RL method that pushes Q-values down on out-of-distribution actions.
- **IQL** — Implicit Q-Learning (Kostrikov et al., 2021). Offline RL that avoids evaluating the critic on OOD actions by using expectile regression.
- **TD3+BC** (Fujimoto & Gu, 2021) — TD3 with an added BC loss term. Simplest offline RL that works.
- **OOD** — Out-of-distribution. Refers to actions or states the policy encounters that weren't in the training data. The central risk in offline RL.

**Safety and robustness.**

- **CPO** — Constrained Policy Optimization (Achiam et al., 2017). Trust-region CMDP solver.
- **CBF** — Control Barrier Function. Differentiable scalar $h(x) \geq 0$ defining a safe set; safety becomes a single-inequality constraint enforceable via a QP.
- **CVaR** — Conditional Value at Risk. Expected return conditional on being in the worst $\alpha\%$ of outcomes. Risk-sensitive objective.
- **QP** — Quadratic Program. The optimization problem class that CBF safety filters reduce to.

**Robotics and practical engineering.**

- **DoF / DOF** — Degree(s) of Freedom. A 7-DOF arm has seven independent joint axes.
- **PD / PID** — Proportional-Derivative / Proportional-Integral-Derivative controllers. The low-level feedback that RL setpoints often sit on top of.
- **LQR** — Linear Quadratic Regulator. Closed-form optimal control for linear dynamics and quadratic cost. The classical benchmark.
- **NMPC** — Nonlinear Model Predictive Control. MPC with nonlinear dynamics and/or costs.
- **DR** — Domain Randomization. Randomize simulator physics parameters during training to produce a policy robust to sim-to-real gap.
- **SysID** — System Identification. Measuring a real system's parameters to calibrate a simulator or model.
- **NVH** — Noise, Vibration, Harshness. Automotive acoustic/vibrational quality metric often included as a soft cost in motor-control RL.
- **PMSM** — Permanent Magnet Synchronous Motor. The dominant electric-drive topology in automotive traction.
- **AFM** — Axial Flux Motor. Alternative motor topology with axial rather than radial flux.
- **FOC** — Field Oriented Control. The classical torque-control scheme for PMSMs.
- **BLDC** — Brushless DC motor. Related topology; see [the FOC post]({{ '/posts/foc-for-bldc-motors/' | relative_url }}) if it's been written.

**Infrastructure.**

- **W&B** — Weights & Biases. Experiment tracking platform.
- **SB3** — Stable-Baselines3. Popular PyTorch RL library.
- **MuJoCo / MJX** — Multi-Joint dynamics with Contact / JAX port. Physics simulators.
- **Isaac Gym / Isaac Lab** — NVIDIA's GPU-accelerated robotics simulators.

---

## The final rule

The best RL practitioners are people who would happily ship a PID controller if it worked. RL is a tool, not a goal. Measure it against the simplest thing that could possibly work, and only keep it if it wins.

This series goes deep into the methods that do win. The foundations post is next — and it starts, as every RL post should, with writing down the MDP.

<!-- =====================================================
     Post-scoped styles for the algorithm-selector widget
     ===================================================== -->
<style>
  .article-body .rl-selector {
    max-width: var(--read);
    margin: 32px auto;
    background: var(--paper-2);
    border: 1px solid var(--rule);
    border-radius: 4px;
    padding: 22px 24px;
  }

  .article-body .rl-q {
    padding: 16px 0 20px;
    border-bottom: 1px solid var(--rule);
  }
  .article-body .rl-q:first-child { padding-top: 0; }
  .article-body .rl-q:last-of-type { border-bottom: none; padding-bottom: 4px; }

  .article-body .rl-qnum {
    font-family: var(--f-ui);
    font-size: .68rem;
    letter-spacing: .16em;
    text-transform: uppercase;
    color: var(--ink-mute);
    margin: 0 0 10px;
  }
  .article-body .rl-qtext {
    font-family: var(--f-display);
    font-weight: 500;
    font-size: 1.25rem;
    letter-spacing: -0.01em;
    line-height: 1.3;
    color: var(--ink);
    margin: 0 0 14px;
  }

  .article-body .rl-opts {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .article-body .rl-opt {
    font-family: var(--f-body);
    font-size: .95rem;
    font-weight: 400;
    text-align: left;
    background: var(--paper);
    color: var(--ink);
    border: 1px solid var(--rule);
    border-radius: 2px;
    padding: 11px 16px;
    cursor: pointer;
    transition: border-color .15s ease, color .15s ease, background .15s ease;
  }
  .article-body .rl-opt:hover {
    border-color: var(--accent);
    color: var(--accent);
  }
  .article-body .rl-opt.selected {
    background: var(--accent);
    color: var(--paper);
    border-color: var(--accent);
    font-weight: 500;
  }

  .article-body .rl-rec {
    display: none;
    margin: 24px 0 4px;
    padding: 20px 22px;
    background: var(--paper);
    border-left: 3px solid var(--accent);
    border-radius: 0 2px 2px 0;
  }
  .article-body .rl-rec.visible { display: block; }
  .article-body .rl-rec-label {
    font-family: var(--f-ui);
    font-size: .68rem;
    letter-spacing: .2em;
    text-transform: uppercase;
    color: var(--accent);
    margin: 0 0 8px;
  }
  .article-body .rl-rec-title {
    font-family: var(--f-display);
    font-weight: 500;
    font-style: italic;
    font-size: 1.75rem;
    letter-spacing: -0.01em;
    line-height: 1.1;
    color: var(--accent);
    margin: 0 0 10px;
  }
  .article-body .rl-rec-body {
    font-family: var(--f-body);
    font-size: 1rem;
    line-height: 1.65;
    color: var(--ink);
    margin: 0 0 10px;
  }
  .article-body .rl-rec-alt {
    font-family: var(--f-body);
    font-size: .9rem;
    font-style: italic;
    color: var(--ink-mute);
    margin: 0;
  }

  .article-body .rl-foot {
    font-family: var(--f-body);
    font-size: .86rem;
    font-style: italic;
    color: var(--ink-mute);
    margin: 18px 0 0;
    padding: 14px 0 0;
    border-top: 1px solid var(--rule);
    line-height: 1.55;
  }
</style>

<script>
(function() {
  var root = document.querySelector('.article-body .rl-selector');
  if (!root) return;

  var answers = {};
  var totalQuestions = root.querySelectorAll('.rl-q').length;

  root.querySelectorAll('.rl-q').forEach(function(block) {
    var qname = block.dataset.qname;
    block.querySelectorAll('.rl-opt').forEach(function(btn) {
      btn.addEventListener('click', function() {
        answers[qname] = btn.dataset.val;
        block.querySelectorAll('.rl-opt').forEach(function(b) { b.classList.remove('selected'); });
        btn.classList.add('selected');
        if (Object.keys(answers).length === totalQuestions) {
          recommend();
        }
      });
    });
  });

  function recommend() {
    var algo, reasoning, alternative;

    if (answers.actions === 'discrete') {
      algo = 'DQN (Rainbow)';
      reasoning = 'Discrete action spaces map directly to value-based methods. Rainbow DQN (Double + Dueling + Prioritized + Noisy + Distributional + Multi-step) is a strong, well-understood baseline. For very large action spaces, consider branching architectures.';
      alternative = 'Alternative: PPO with a categorical policy if you want an on-policy approach or have very large action spaces.';
    } else if (answers.safety === 'hard' || answers.data === 'expensive') {
      if (answers.smooth === 'contact' || answers.smooth === 'vision') {
        algo = 'TD-MPC2 / DreamerV3';
        reasoning = 'Expensive data plus complex dynamics calls for model-based RL. TD-MPC2 combines a learned world model with online planning (MPPI) and an amortized policy — excellent sample efficiency and handles contact well. DreamerV3 is the go-to for vision-based tasks and has fixed hyperparameters that transfer across domains.';
        alternative = 'Alternative: MBPO (SAC + model-generated rollouts) if you want a simpler pipeline with proven results.';
      } else {
        algo = 'MPC with learned dynamics (PETS / MBPO)';
        reasoning = 'Smooth, mostly-Markov dynamics with expensive data and safety concerns is the textbook case for model-based RL. PETS gives you MPC with uncertainty-aware ensemble dynamics and natural constraint handling. Bolt on a CBF safety filter for hard constraints.';
        alternative = 'Alternative: SAC with aggressive sim pre-training and domain randomization if you want a policy that runs cheaply at inference time.';
      }
    } else if (answers.data === 'cheap') {
      algo = 'PPO';
      reasoning = 'Fast sims — Isaac Gym, Brax, MuJoCo MJX — are exactly where PPO shines. Massive parallelism, robust hyperparameters that transfer across tasks, and the simpler on-policy structure makes debugging easier. The "37 implementation details" (advantage norm, obs norm, orthogonal init, reward clipping) all matter.';
      alternative = 'Alternative: SAC if you need sample efficiency for downstream real-robot fine-tuning, or if PPO tuning is getting painful.';
    } else if (answers.det === 'yes') {
      algo = 'TD3';
      reasoning = 'Deterministic policy, off-policy, strong baseline. Twin critics fix DDPG\'s overestimation; delayed updates stabilize training; target policy smoothing regularizes the critic. Known, predictable, easy to analyze — which matters for certification and control-theoretic analysis.';
      alternative = 'Alternative: SAC with very low entropy target if you want more robustness and can tolerate a near-deterministic stochastic policy.';
    } else {
      algo = 'SAC';
      reasoning = 'Continuous actions, moderate data cost, smooth dynamics, no deterministic requirement, no hard safety constraints — this is SAC\'s sweet spot. Use auto-entropy tuning, twin critics, tanh-squashed Gaussian with log-prob correction, observation normalization, and reward scaling. It will almost certainly work with default hyperparameters.';
      alternative = 'Alternative: TD3 if you hit instability you can\'t diagnose; it has fewer moving parts.';
    }

    document.getElementById('rlRecTitle').textContent = algo;
    document.getElementById('rlRecBody').textContent = reasoning;
    document.getElementById('rlRecAlt').textContent = alternative;
    var rec = document.getElementById('rlRec');
    rec.classList.add('visible');
    rec.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
})();
</script>
