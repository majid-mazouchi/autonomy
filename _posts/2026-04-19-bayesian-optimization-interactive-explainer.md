---
title: "Bayesian Optimization — an Interactive Explainer"
subtitle: "Finding the best input to a black-box function when every evaluation is expensive."
date: 2026-04-19 14:00:00 -0400
category: "Machine Learning"
slug: bayesian-optimization-interactive-explainer
excerpt: "A working Bayesian optimization loop you can run in your browser. Watch Expected Improvement, UCB, and PI compete to find the minimum of a deceptive benchmark function — and read the math that makes it work."
reading_time: 16
---

Some functions are cheap to evaluate. Those are the easy ones. The interesting problems live on the other side — training a neural network, running a wind-tunnel experiment, tuning a motor controller on a dyno — where a single evaluation takes hours, costs money, and gives you one noisy number back. Classical optimization assumes you can evaluate $f(x)$ millions of times, or that you have gradients. Neither assumption holds here. You need a method that is *sample-efficient* — one that extracts as much information as possible from every measurement and uses that information to decide where to sample next. That's what Bayesian optimization does, and the demo below shows it running on a benchmark designed to trip it up.

## Two ingredients: a belief and a strategy

Every Bayesian-optimization algorithm is built from two interchangeable pieces: a **surrogate model** that represents our current belief about $f$, and an **acquisition function** that scores each candidate point by how useful evaluating it would be.

**01 · Surrogate.** A cheap statistical model fit to whatever observations we have so far. Because data is scarce, the model must express *uncertainty* — a prediction alone isn't enough; we also need to know where the model is confident and where it's guessing. By far the most common choice is a [Gaussian Process]({{ '/posts/gaussian-processes-interactive-explainer/' | relative_url }}), which gives a full posterior distribution over functions rather than a point estimate.

**02 · Acquisition.** A rule for choosing the next sample. The surrogate tells us, at each point, what we *expect* to see and how *uncertain* we are. The acquisition function combines these into a single score we can maximize cheaply. Good acquisition functions balance **exploitation** (sampling where the surrogate predicts good values) and **exploration** (sampling where the surrogate is uncertain).

> Bayesian optimization treats the choice of *where to sample next* as itself an optimization problem — one we can solve cheaply, since the acquisition function lives on the surrogate, not on the real objective.

## Interactive demo — see it run, step by step

Below is a working Bayesian-optimization loop. The objective is the **Forrester function** $f(x) = (6x-2)^2 \sin(12x - 4)$, a standard BO benchmark with a deceptive local minimum near $x = 0.15$ and a global minimum near $x = 0.76$. Pretend you don't know its shape.

The **shaded band** is the GP posterior (solid line = mean, band = ±2σ). **Gold dots** are observations. The **orange marker** shows where the acquisition function is maximized — that's the next candidate. Click *Next iteration* to evaluate at the suggested point and update the model. Or click anywhere on the upper plot to sample there manually.

<div class="bo-widget">

  <div class="bo-plot">
    <div class="bo-plot-head">
      <div class="bo-plot-label">Objective &amp; GP posterior</div>
      <div class="bo-legend">
        <span class="bo-leg"><span class="sw line-mean"></span>GP mean</span>
        <span class="bo-leg"><span class="sw fill-band"></span>±2σ</span>
        <span class="bo-leg"><span class="sw dot-obs"></span>observed</span>
        <span class="bo-leg"><span class="sw line-true"></span>true f(x)</span>
        <span class="bo-leg"><span class="sw dot-next"></span>next</span>
      </div>
    </div>
    <div class="bo-canvas-outer">
      <canvas id="objCanvas" class="bo-obj"></canvas>
      <div class="bo-tooltip" id="objTooltip"></div>
    </div>
  </div>

  <div class="bo-plot">
    <div class="bo-plot-head">
      <div class="bo-plot-label">Acquisition function &mdash; <span id="acqName">Expected Improvement</span></div>
      <div class="bo-legend">
        <span class="bo-leg"><span class="sw line-acq"></span>α(x)</span>
        <span class="bo-leg"><span class="sw dot-next"></span>argmax</span>
      </div>
    </div>
    <div class="bo-canvas-outer">
      <canvas id="acqCanvas" class="bo-acq"></canvas>
    </div>
  </div>

  <div class="bo-controls">
    <div class="bo-panel">
      <div class="bo-panel-label">Acquisition</div>
      <div class="bo-btn-group" id="acqGroup">
        <button type="button" data-acq="EI" class="active">EI</button>
        <button type="button" data-acq="UCB">UCB</button>
        <button type="button" data-acq="PI">PI</button>
      </div>
      <div class="bo-slider">
        <div class="bo-slider-label"><span>GP lengthscale ℓ</span><span class="val" id="lsVal">0.10</span></div>
        <input type="range" id="lsSlider" min="0.02" max="0.40" step="0.005" value="0.10">
      </div>
    </div>

    <div class="bo-panel">
      <div class="bo-panel-label">Parameters</div>
      <div class="bo-slider">
        <div class="bo-slider-label"><span>UCB exploration κ</span><span class="val" id="kappaVal">2.0</span></div>
        <input type="range" id="kappaSlider" min="0.1" max="5.0" step="0.1" value="2.0">
      </div>
      <div class="bo-slider">
        <div class="bo-slider-label"><span>EI / PI margin ξ</span><span class="val" id="xiVal">0.01</span></div>
        <input type="range" id="xiSlider" min="0" max="0.5" step="0.01" value="0.01">
      </div>
      <div class="bo-toggle-row">
        <span>Show true f(x)</span>
        <div class="bo-toggle on" id="trueToggle" role="button" aria-pressed="true" tabindex="0"></div>
      </div>
    </div>

    <div class="bo-panel">
      <div class="bo-panel-label">Actions</div>
      <div class="bo-action-row">
        <button type="button" class="bo-btn-primary" id="stepBtn">Next iteration →</button>
      </div>
      <div class="bo-action-row">
        <button type="button" class="bo-btn" id="auto10Btn">Run 10 steps</button>
        <button type="button" class="bo-btn" id="resetBtn">Reset</button>
      </div>
    </div>
  </div>

  <div class="bo-status">
    <div class="bo-stat"><span class="k">Iteration</span><span class="v" id="iterStat">0</span></div>
    <div class="bo-stat"><span class="k">Observations</span><span class="v" id="nObsStat">3</span></div>
    <div class="bo-stat"><span class="k">Best f*</span><span class="v best" id="bestStat">—</span></div>
    <div class="bo-stat"><span class="k">at x*</span><span class="v" id="bestXStat">—</span></div>
    <div class="bo-stat"><span class="k">Next candidate</span><span class="v next" id="nextStat">—</span></div>
    <div class="bo-stat"><span class="k">Global optimum</span><span class="v muted">−6.021 @ 0.7572</span></div>
  </div>

</div>

## Gaussian processes, briefly

A Gaussian Process is a distribution over functions — any finite collection of function values is jointly Gaussian, fully specified by a mean function $m(x)$ (usually zero) and a covariance kernel $k(x, x')$.

The kernel encodes our prior about smoothness. The squared-exponential (RBF) kernel, used in the demo above, says that nearby inputs have highly correlated outputs and that correlation decays with distance on a scale set by the lengthscale $\ell$:

$$ k(x, x') = \sigma_f^2 \,\exp\!\left(-\frac{\lVert x - x'\rVert^2}{2\ell^2}\right) $$

Given observations $\mathbf{y} = [y_1, \ldots, y_n]^\top$ at inputs $X = \{x_1, \ldots, x_n\}$ with noise variance $\sigma_n^2$, the posterior at any test point $x_*$ is Gaussian with mean and variance:

$$ \mu(x_*) = \mathbf{k}_*^\top \left(K + \sigma_n^2 I\right)^{-1} \mathbf{y} $$

$$ \sigma^2(x_*) = k(x_*, x_*) - \mathbf{k}_*^\top \left(K + \sigma_n^2 I\right)^{-1} \mathbf{k}_* $$

Here $K_{ij} = k(x_i, x_j)$ and $(\mathbf{k}_*)_i = k(x_i, x_*)$. Two properties make this an ideal BO surrogate: the posterior mean **interpolates** the noise-free observations, and the posterior variance **collapses to zero** at observed points and grows smoothly away from them. That's exactly the signal an acquisition function needs. In practice you solve the linear system via Cholesky decomposition in $\mathcal{O}(n^3)$ — perfectly fine for BO, where $n$ rarely exceeds a few hundred.

## Three ways to score a candidate

Each acquisition function takes the GP posterior $\mathcal{N}(\mu(x), \sigma^2(x))$ and collapses it into a single scalar. What they differ on is *how* they weigh the two knobs — expected value and uncertainty.

### Expected Improvement (EI)

For minimization with current best $f^*$, define the improvement at $x$ as $I(x) = \max(0, f^* - f(x) - \xi)$, where $\xi \geq 0$ encourages more exploration. EI is its expected value under the GP posterior:

$$ \alpha_{\text{EI}}(x) = (f^* - \mu(x) - \xi)\,\Phi(z) + \sigma(x)\,\phi(z), \qquad z = \frac{f^* - \mu(x) - \xi}{\sigma(x)} $$

EI is self-calibrating: when $\sigma \to 0$ it reduces to pure exploitation; where $\sigma$ is large and $\mu$ is not too terrible, it favors exploration. This is why it's the default choice in most BO packages.

### Lower Confidence Bound (UCB)

The simplest possible acquisition. Pick the point with the lowest optimistic estimate of $f$ — a linear combination of the posterior mean and a scaled standard deviation:

$$ \alpha_{\text{LCB}}(x) = \mu(x) - \kappa\,\sigma(x) $$

The exploration weight $\kappa$ is the tuning knob. $\kappa = 0$ is pure greedy exploitation; large $\kappa$ becomes uncertainty-sampling. Srinivas et al. give a theoretical schedule for $\kappa$ that yields no-regret bounds.

### Probability of Improvement (PI)

Just the probability that a sample at $x$ beats the current best by at least $\xi$:

$$ \alpha_{\text{PI}}(x) = \Phi\!\left(\frac{f^* - \mu(x) - \xi}{\sigma(x)}\right) $$

Historically first, but known to under-explore — it happily picks points with microscopic improvement probability as long as *any* improvement is likely. The margin $\xi$ partially compensates. In practice EI is almost always preferred.

## The whole algorithm, in twelve lines

Everything above combines into a single loop. The outer loop queries the expensive objective; the inner optimization of the acquisition function is cheap, because it operates on the surrogate, not on $f$ itself.

```text
# Given: objective f, domain 𝒳, budget T, acquisition α

initialize D ← { (xᵢ, f(xᵢ)) } for i = 1..n₀     # e.g. Latin hypercube or random

for t = 1, 2, ..., T:
    # 1. fit / update surrogate
    GP ← fit_gp(D)

    # 2. maximize acquisition — cheap, uses only the surrogate
    x_next ← argmax over x ∈ 𝒳  of  α(x | GP, f*_D)

    # 3. query expensive objective at the chosen point
    y_next ← f(x_next)

    # 4. augment dataset
    D ← D ∪ { (x_next, y_next) }

return argmin over (x, y) ∈ D of y
```

Step 2 is the only subtle one. The acquisition function is cheap to evaluate but can be multi-modal, so practitioners use multi-start L-BFGS, DIRECT, or dense grid search on the surrogate. None of this touches the real objective.

## Where it lives

The common thread across BO applications is a function you can't see inside, that returns a noisy scalar, and costs real time or real money to query.

- **Hyperparameter tuning.** Training a deep network costs hours. BO finds strong configurations in 20–50 trials instead of thousands of random ones.
- **Experimental design.** Materials discovery, chemistry, biology — any setting where each data point is a physical experiment.
- **Controller calibration.** Tuning PID, MPC, or motor-control parameters against a high-fidelity simulator or dyno where each run is slow.
- **Engineering design.** Airfoil shapes, antenna geometries, chip layouts — design variables evaluated by expensive CFD or EM solvers.
- **Robotics and policy search.** Tuning gait parameters or policy coefficients on hardware, where every rollout risks wear or damage.
- **A/B testing at scale.** Treating each experimental configuration as an expensive sample when user traffic or exposure is the bottleneck.

Bayesian optimization is the default tool whenever that query cost dominates.

---

The interactive demo above is implemented with vanilla JavaScript and the Canvas 2D API — the GP fit (RBF kernel, Cholesky solve), the three acquisition functions, and all plotting run in the browser with no external libraries. If you want to see how it's stitched together, view source on the page.

<!-- =====================================================
     Post-scoped styles for the Bayesian-optimization widget
     Reuses the blog's CSS variables (paper, ink, rule, accent)
     ===================================================== -->
<style>
  .article-body .bo-widget {
    /* Local color variables — JS reads these via getComputedStyle */
    --c-gp-mean:  var(--ink);
    --c-band:     rgba(185, 74, 27, 0.15);
    --c-true:     rgba(74, 70, 64, 0.55);
    --c-obs:      #a86a2a;     /* warm bronze for observation dots */
    --c-next:     var(--accent);
    --c-acq:      #4d6a8f;     /* muted steel blue for acquisition curve */
    --c-acq-fill: rgba(77, 106, 143, 0.14);
    --c-grid:     rgba(74, 70, 64, 0.07);
    --c-axis:     rgba(74, 70, 64, 0.25);
    --c-tick:     var(--ink-mute);

    max-width: var(--read);
    margin: 32px auto 36px;
    background: var(--paper-2);
    border: 1px solid var(--rule);
    border-radius: 4px;
    padding: 20px;
  }

  @media (prefers-color-scheme: dark) {
    .article-body .bo-widget {
      --c-band:     rgba(224, 122, 74, 0.18);
      --c-true:     rgba(184, 176, 160, 0.45);
      --c-obs:      #d4a048;
      --c-acq:      #7aa6c9;
      --c-acq-fill: rgba(122, 166, 201, 0.16);
      --c-grid:     rgba(184, 176, 160, 0.08);
      --c-axis:     rgba(184, 176, 160, 0.25);
    }
  }

  .article-body .bo-plot { margin: 0 0 14px; }
  .article-body .bo-plot-head {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 12px;
    flex-wrap: wrap;
    margin: 0 0 8px;
    padding: 0 2px;
  }
  .article-body .bo-plot-label {
    font-family: var(--f-ui);
    font-size: .74rem;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: var(--ink-mute);
  }
  .article-body .bo-legend {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    font-family: var(--f-ui);
    font-size: .66rem;
    letter-spacing: .08em;
    text-transform: uppercase;
    color: var(--ink-mute);
  }
  .article-body .bo-leg { display: inline-flex; align-items: center; gap: 5px; }
  .article-body .bo-legend .sw { display: inline-block; }
  .article-body .bo-legend .sw.line-mean { width: 16px; height: 2px; background: var(--c-gp-mean); }
  .article-body .bo-legend .sw.line-acq  { width: 16px; height: 2px; background: var(--c-acq); }
  .article-body .bo-legend .sw.line-true { width: 16px; height: 0; border-top: 1.5px dashed var(--c-true); }
  .article-body .bo-legend .sw.fill-band { width: 16px; height: 8px; background: var(--c-band); border-radius: 1px; }
  .article-body .bo-legend .sw.dot-obs   { width: 7px; height: 7px; border-radius: 50%; background: var(--c-obs); }
  .article-body .bo-legend .sw.dot-next  { width: 7px; height: 7px; border-radius: 50%; background: var(--c-next); }

  .article-body .bo-canvas-outer {
    position: relative;
    background: var(--paper);
    border: 1px solid var(--rule);
    border-radius: 2px;
  }
  .article-body .bo-obj { display: block; width: 100%; height: 340px; cursor: crosshair; }
  .article-body .bo-acq { display: block; width: 100%; height: 150px; }

  .article-body .bo-tooltip {
    position: absolute;
    pointer-events: none;
    background: var(--ink);
    color: var(--paper);
    font-family: var(--f-ui);
    font-size: .7rem;
    letter-spacing: .04em;
    padding: 5px 9px;
    border-radius: 2px;
    opacity: 0;
    transition: opacity .12s ease;
    white-space: nowrap;
    transform: translate(0, -100%);
    z-index: 2;
  }
  .article-body .bo-tooltip.visible { opacity: 0.95; }

  .article-body .bo-controls {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 14px;
    margin: 18px 0 0;
  }
  .article-body .bo-panel {
    background: var(--paper);
    border: 1px solid var(--rule);
    border-radius: 2px;
    padding: 12px 14px;
  }
  .article-body .bo-panel-label {
    font-family: var(--f-ui);
    font-size: .68rem;
    letter-spacing: .14em;
    text-transform: uppercase;
    color: var(--ink-mute);
    margin: 0 0 10px;
  }

  .article-body .bo-btn-group {
    display: flex;
    gap: 4px;
    border: 1px solid var(--rule);
    border-radius: 2px;
    padding: 2px;
    margin: 0 0 12px;
  }
  .article-body .bo-btn-group button {
    flex: 1;
    font-family: var(--f-ui);
    font-size: .74rem;
    font-weight: 400;
    letter-spacing: .08em;
    text-transform: uppercase;
    background: transparent;
    color: var(--ink-soft);
    border: none;
    padding: 7px 4px;
    cursor: pointer;
    border-radius: 1px;
    transition: background .15s ease, color .15s ease;
  }
  .article-body .bo-btn-group button:hover { color: var(--ink); background: var(--paper-2); }
  .article-body .bo-btn-group button.active {
    background: var(--accent);
    color: var(--paper);
  }

  .article-body .bo-slider { margin: 10px 0; }
  .article-body .bo-slider-label {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-family: var(--f-ui);
    font-size: .72rem;
    letter-spacing: .03em;
    color: var(--ink-soft);
    margin: 0 0 6px;
  }
  .article-body .bo-slider-label .val {
    color: var(--ink);
    font-variant-numeric: tabular-nums;
    font-weight: 500;
  }
  .article-body .bo-widget input[type="range"] {
    -webkit-appearance: none;
    appearance: none;
    width: 100%;
    height: 3px;
    background: var(--rule);
    border-radius: 2px;
    outline: none;
    margin: 4px 0;
  }
  .article-body .bo-widget input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 15px; height: 15px;
    background: var(--accent);
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid var(--paper);
    box-shadow: 0 0 0 1px var(--accent);
  }
  .article-body .bo-widget input[type="range"]::-moz-range-thumb {
    width: 13px; height: 13px;
    background: var(--accent);
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid var(--paper);
    box-shadow: 0 0 0 1px var(--accent);
  }

  .article-body .bo-toggle-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: var(--f-ui);
    font-size: .74rem;
    color: var(--ink-soft);
    margin: 14px 0 2px;
  }
  .article-body .bo-toggle {
    width: 30px;
    height: 16px;
    background: var(--rule);
    border-radius: 8px;
    position: relative;
    cursor: pointer;
    transition: background .2s ease;
  }
  .article-body .bo-toggle::after {
    content: "";
    position: absolute;
    top: 2px; left: 2px;
    width: 12px; height: 12px;
    background: var(--paper);
    border-radius: 50%;
    transition: transform .2s ease;
    box-shadow: 0 1px 2px rgba(0,0,0,0.2);
  }
  .article-body .bo-toggle.on { background: var(--accent); }
  .article-body .bo-toggle.on::after { transform: translateX(14px); }

  .article-body .bo-action-row {
    display: flex;
    gap: 8px;
    margin-bottom: 8px;
  }
  .article-body .bo-action-row:last-child { margin-bottom: 0; }
  .article-body .bo-btn,
  .article-body .bo-btn-primary {
    flex: 1;
    font-family: var(--f-ui);
    font-size: .74rem;
    letter-spacing: .06em;
    text-transform: uppercase;
    border: 1px solid var(--rule);
    padding: 9px 10px;
    cursor: pointer;
    border-radius: 2px;
    transition: background .15s ease, color .15s ease, border-color .15s ease;
  }
  .article-body .bo-btn {
    background: transparent;
    color: var(--ink);
  }
  .article-body .bo-btn:hover {
    border-color: var(--ink-mute);
    background: var(--paper-2);
  }
  .article-body .bo-btn-primary {
    background: var(--accent);
    color: var(--paper);
    border-color: var(--accent);
    font-weight: 500;
  }
  .article-body .bo-btn-primary:hover { filter: brightness(0.93); }

  .article-body .bo-status {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
    gap: 10px;
    margin: 14px 0 0;
    padding: 14px 16px;
    background: var(--paper);
    border: 1px solid var(--rule);
    border-radius: 2px;
  }
  .article-body .bo-stat {
    display: flex;
    flex-direction: column;
    gap: 3px;
  }
  .article-body .bo-stat .k {
    font-family: var(--f-ui);
    font-size: .62rem;
    letter-spacing: .14em;
    text-transform: uppercase;
    color: var(--ink-mute);
  }
  .article-body .bo-stat .v {
    font-family: var(--f-ui);
    font-size: .95rem;
    font-weight: 500;
    font-variant-numeric: tabular-nums;
    color: var(--ink);
  }
  .article-body .bo-stat .v.best { color: var(--c-gp-mean); }
  .article-body .bo-stat .v.next { color: var(--c-next); }
  .article-body .bo-stat .v.muted { color: var(--ink-mute); font-weight: 400; }
</style>

<script>
(function() {
  var objCanvas = document.getElementById('objCanvas');
  var acqCanvas = document.getElementById('acqCanvas');
  if (!objCanvas || !acqCanvas) return;
  var objCtx = objCanvas.getContext('2d');
  var acqCtx = acqCanvas.getContext('2d');

  // Pull a CSS variable from the widget scope so colors live in the stylesheet
  var widgetEl = objCanvas.closest('.bo-widget');
  function cv(name, fallback) {
    var v = getComputedStyle(widgetEl).getPropertyValue(name).trim();
    return v || fallback;
  }

  // ---------- Objective: Forrester (2008) ----------
  function forrester(x) {
    var a = 6 * x - 2;
    return a * a * Math.sin(12 * x - 4);
  }
  var X_MIN = 0, X_MAX = 1;
  var Y_MIN = -9, Y_MAX = 18;

  // ---------- Linear algebra ----------
  function choleskyDecompose(A) {
    var n = A.length;
    var L = [];
    for (var i = 0; i < n; i++) L.push(new Float64Array(n));
    for (var i2 = 0; i2 < n; i2++) {
      for (var j = 0; j <= i2; j++) {
        var sum = 0;
        for (var k = 0; k < j; k++) sum += L[i2][k] * L[j][k];
        if (i2 === j) L[i2][j] = Math.sqrt(Math.max(A[i2][i2] - sum, 1e-12));
        else L[i2][j] = (A[i2][j] - sum) / L[j][j];
      }
    }
    return L;
  }
  function forwardSub(L, b) {
    var n = L.length;
    var y = new Float64Array(n);
    for (var i = 0; i < n; i++) {
      var s = b[i];
      for (var k = 0; k < i; k++) s -= L[i][k] * y[k];
      y[i] = s / L[i][i];
    }
    return y;
  }
  function backSubLT(L, y) {
    var n = L.length;
    var x = new Float64Array(n);
    for (var i = n - 1; i >= 0; i--) {
      var s = y[i];
      for (var k = i + 1; k < n; k++) s -= L[k][i] * x[k];
      x[i] = s / L[i][i];
    }
    return x;
  }

  function rbfKernel(x1, x2, ls, sf2) {
    var d = x1 - x2;
    return sf2 * Math.exp(-0.5 * d * d / (ls * ls));
  }

  function gpFit(X, y, ls, sf2, sn2) {
    var n = X.length;
    var K = [];
    for (var i = 0; i < n; i++) K.push(new Float64Array(n));
    for (var i2 = 0; i2 < n; i2++) {
      for (var j = 0; j < n; j++) K[i2][j] = rbfKernel(X[i2], X[j], ls, sf2);
      K[i2][i2] += sn2;
    }
    var L = choleskyDecompose(K);
    var alpha = backSubLT(L, forwardSub(L, y));
    return { L: L, alpha: alpha, X: X, ls: ls, sf2: sf2 };
  }

  function gpPredict(model, Xtest) {
    var L = model.L, alpha = model.alpha, X = model.X, ls = model.ls, sf2 = model.sf2;
    var n = X.length;
    var out = [];
    for (var t = 0; t < Xtest.length; t++) {
      var xs = Xtest[t];
      var kstar = new Float64Array(n);
      for (var i = 0; i < n; i++) kstar[i] = rbfKernel(X[i], xs, ls, sf2);
      var mean = 0;
      for (var i2 = 0; i2 < n; i2++) mean += kstar[i2] * alpha[i2];
      var v = forwardSub(L, kstar);
      var vtv = 0;
      for (var i3 = 0; i3 < n; i3++) vtv += v[i3] * v[i3];
      var variance = Math.max(sf2 - vtv, 1e-10);
      out.push({ mean: mean, std: Math.sqrt(variance) });
    }
    return out;
  }

  // Standard normal pdf / cdf (Abramowitz & Stegun 7.1.26)
  function phi(z) { return Math.exp(-0.5 * z * z) / Math.sqrt(2 * Math.PI); }
  function Phi(z) {
    var a1 = 0.254829592, a2 = -0.284496736, a3 = 1.421413741;
    var a4 = -1.453152027, a5 = 1.061405429, p = 0.3275911;
    var sign = z < 0 ? -1 : 1;
    var x = Math.abs(z) / Math.sqrt(2);
    var t = 1.0 / (1.0 + p * x);
    var y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-x * x);
    return 0.5 * (1.0 + sign * y);
  }

  function acqEI(mean, std, fStar, xi) {
    if (std < 1e-9) return 0;
    var imp = fStar - mean - xi;
    var z = imp / std;
    return imp * Phi(z) + std * phi(z);
  }
  function acqUCB(mean, std, kappa) {
    // For minimization: LCB = μ - κσ; return -LCB so we can argmax
    return kappa * std - mean;
  }
  function acqPI(mean, std, fStar, xi) {
    if (std < 1e-9) return 0;
    return Phi((fStar - mean - xi) / std);
  }

  // ---------- State ----------
  var STATE = {
    obs: [],
    ls: 0.10,
    sf2: 9.0,
    sn2: 1e-4,
    acq: 'EI',
    kappa: 2.0,
    xi: 0.01,
    showTrue: true,
    iter: 0,
    nextX: null,
    grid: null,
    gpPred: null,
    acqVals: null
  };
  var GRID_N = 300;

  function buildGrid() {
    var g = new Float64Array(GRID_N);
    for (var i = 0; i < GRID_N; i++) g[i] = X_MIN + (X_MAX - X_MIN) * i / (GRID_N - 1);
    STATE.grid = g;
  }
  buildGrid();

  function seedInitial() {
    STATE.obs = [];
    var seeds = [0.08, 0.45, 0.92];
    for (var i = 0; i < seeds.length; i++) {
      var xx = seeds[i];
      STATE.obs.push({ x: xx, y: forrester(xx) });
    }
    STATE.iter = 0;
  }

  function currentBestFstar() {
    var fmin = Infinity, xmin = null;
    for (var i = 0; i < STATE.obs.length; i++) {
      var o = STATE.obs[i];
      if (o.y < fmin) { fmin = o.y; xmin = o.x; }
    }
    return { fmin: fmin, xmin: xmin };
  }

  function refit() {
    var X = STATE.obs.map(function(o) { return o.x; });
    var y = STATE.obs.map(function(o) { return o.y; });
    var model = gpFit(X, y, STATE.ls, STATE.sf2, STATE.sn2);
    var preds = gpPredict(model, STATE.grid);
    STATE.gpPred = preds;

    var fmin = currentBestFstar().fmin;
    var acq = new Float64Array(GRID_N);
    for (var i = 0; i < GRID_N; i++) {
      var m = preds[i].mean, s = preds[i].std;
      var a;
      if (STATE.acq === 'EI') a = acqEI(m, s, fmin, STATE.xi);
      else if (STATE.acq === 'UCB') a = acqUCB(m, s, STATE.kappa);
      else a = acqPI(m, s, fmin, STATE.xi);
      acq[i] = a;
    }
    STATE.acqVals = acq;

    var best = -Infinity, bi = 0;
    for (var j = 0; j < GRID_N; j++) {
      if (acq[j] > best) { best = acq[j]; bi = j; }
    }
    STATE.nextX = STATE.grid[bi];
  }

  // ---------- Canvas + transforms ----------
  var PAD_L = 48, PAD_R = 18, PAD_T = 12, PAD_B = 28;
  function resizeCanvases() {
    var dpr = window.devicePixelRatio || 1;
    [objCanvas, acqCanvas].forEach(function(cv) {
      var rect = cv.parentElement.getBoundingClientRect();
      var w = rect.width;
      var h = cv.clientHeight;
      cv.width = Math.floor(w * dpr);
      cv.height = Math.floor(h * dpr);
      cv.getContext('2d').setTransform(dpr, 0, 0, dpr, 0, 0);
    });
    draw();
  }
  function xToPx(x, w) { return PAD_L + (x - X_MIN) / (X_MAX - X_MIN) * (w - PAD_L - PAD_R); }
  function pxToX(px, w) { return X_MIN + (px - PAD_L) / (w - PAD_L - PAD_R) * (X_MAX - X_MIN); }
  function yToPxObj(y, h) { return PAD_T + (1 - (y - Y_MIN) / (Y_MAX - Y_MIN)) * (h - PAD_T - PAD_B); }

  function drawAxes(ctx, w, h, yMin, yMax) {
    var grid = cv('--c-grid', 'rgba(0,0,0,0.06)');
    var axis = cv('--c-axis', 'rgba(0,0,0,0.2)');
    var tick = cv('--c-tick', '#8a8277');

    ctx.save();
    ctx.strokeStyle = grid;
    ctx.lineWidth = 1;
    for (var t = 0; t <= 5; t++) {
      var xv = X_MIN + t / 5 * (X_MAX - X_MIN);
      var px = xToPx(xv, w);
      ctx.beginPath(); ctx.moveTo(px, PAD_T); ctx.lineTo(px, h - PAD_B); ctx.stroke();
    }
    for (var t2 = 0; t2 <= 5; t2++) {
      var yv = yMin + t2 / 5 * (yMax - yMin);
      var py = PAD_T + (1 - (yv - yMin) / (yMax - yMin)) * (h - PAD_T - PAD_B);
      ctx.beginPath(); ctx.moveTo(PAD_L, py); ctx.lineTo(w - PAD_R, py); ctx.stroke();
    }
    ctx.strokeStyle = axis;
    ctx.beginPath();
    ctx.moveTo(PAD_L, PAD_T);
    ctx.lineTo(PAD_L, h - PAD_B);
    ctx.lineTo(w - PAD_R, h - PAD_B);
    ctx.stroke();

    ctx.fillStyle = tick;
    ctx.font = '10px "DM Mono", ui-monospace, monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    for (var t3 = 0; t3 <= 5; t3++) {
      var xv2 = X_MIN + t3 / 5 * (X_MAX - X_MIN);
      ctx.fillText(xv2.toFixed(1), xToPx(xv2, w), h - PAD_B + 6);
    }
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    for (var t4 = 0; t4 <= 5; t4++) {
      var yv2 = yMin + t4 / 5 * (yMax - yMin);
      var py2 = PAD_T + (1 - (yv2 - yMin) / (yMax - yMin)) * (h - PAD_T - PAD_B);
      ctx.fillText(yv2.toFixed(1), PAD_L - 6, py2);
    }
    ctx.restore();
  }

  function drawObjectivePlot() {
    var w = objCanvas.clientWidth;
    var h = objCanvas.clientHeight;
    objCtx.clearRect(0, 0, w, h);
    drawAxes(objCtx, w, h, Y_MIN, Y_MAX);
    if (!STATE.gpPred) return;

    var g = STATE.grid;
    var p = STATE.gpPred;

    // GP ±2σ band
    objCtx.save();
    objCtx.beginPath();
    for (var i = 0; i < g.length; i++) {
      var px = xToPx(g[i], w);
      var upper = p[i].mean + 2 * p[i].std;
      var py = yToPxObj(Math.min(Math.max(upper, Y_MIN), Y_MAX), h);
      if (i === 0) objCtx.moveTo(px, py); else objCtx.lineTo(px, py);
    }
    for (var i2 = g.length - 1; i2 >= 0; i2--) {
      var px2 = xToPx(g[i2], w);
      var lower = p[i2].mean - 2 * p[i2].std;
      var py2 = yToPxObj(Math.min(Math.max(lower, Y_MIN), Y_MAX), h);
      objCtx.lineTo(px2, py2);
    }
    objCtx.closePath();
    objCtx.fillStyle = cv('--c-band', 'rgba(185,74,27,0.15)');
    objCtx.fill();
    objCtx.restore();

    // True f(x) dashed
    if (STATE.showTrue) {
      objCtx.save();
      objCtx.strokeStyle = cv('--c-true', 'rgba(74,70,64,0.5)');
      objCtx.lineWidth = 1.2;
      objCtx.setLineDash([4, 4]);
      objCtx.beginPath();
      var N = 200;
      for (var k = 0; k <= N; k++) {
        var x = X_MIN + k / N * (X_MAX - X_MIN);
        var yv = forrester(x);
        var px3 = xToPx(x, w);
        var py3 = yToPxObj(Math.min(Math.max(yv, Y_MIN), Y_MAX), h);
        if (k === 0) objCtx.moveTo(px3, py3); else objCtx.lineTo(px3, py3);
      }
      objCtx.stroke();
      objCtx.restore();
    }

    // GP posterior mean
    objCtx.save();
    objCtx.strokeStyle = cv('--c-gp-mean', '#1a1814');
    objCtx.lineWidth = 2;
    objCtx.beginPath();
    for (var i3 = 0; i3 < g.length; i3++) {
      var px4 = xToPx(g[i3], w);
      var py4 = yToPxObj(Math.min(Math.max(p[i3].mean, Y_MIN), Y_MAX), h);
      if (i3 === 0) objCtx.moveTo(px4, py4); else objCtx.lineTo(px4, py4);
    }
    objCtx.stroke();
    objCtx.restore();

    // Next-candidate vertical guide + marker
    if (STATE.nextX !== null) {
      objCtx.save();
      objCtx.strokeStyle = cv('--c-next', '#b94a1b');
      objCtx.globalAlpha = 0.38;
      objCtx.lineWidth = 1;
      objCtx.setLineDash([3, 4]);
      var pxn = xToPx(STATE.nextX, w);
      objCtx.beginPath();
      objCtx.moveTo(pxn, PAD_T);
      objCtx.lineTo(pxn, h - PAD_B);
      objCtx.stroke();
      objCtx.globalAlpha = 1;
      objCtx.setLineDash([]);

      var near = 0, bd = Infinity;
      for (var i4 = 0; i4 < g.length; i4++) {
        var d = Math.abs(g[i4] - STATE.nextX);
        if (d < bd) { bd = d; near = i4; }
      }
      var pyn = yToPxObj(Math.min(Math.max(p[near].mean, Y_MIN), Y_MAX), h);
      objCtx.fillStyle = cv('--c-next', '#b94a1b');
      objCtx.beginPath();
      objCtx.arc(pxn, pyn, 5, 0, 2 * Math.PI);
      objCtx.fill();
      objCtx.strokeStyle = cv('--paper', '#f4efe6');
      objCtx.lineWidth = 2;
      objCtx.stroke();
      objCtx.restore();
    }

    // Observations
    var xmin = currentBestFstar().xmin;
    objCtx.save();
    for (var oi = 0; oi < STATE.obs.length; oi++) {
      var o = STATE.obs[oi];
      var pxo = xToPx(o.x, w);
      var pyo = yToPxObj(Math.min(Math.max(o.y, Y_MIN), Y_MAX), h);
      var isBest = (o.x === xmin);
      objCtx.fillStyle = cv('--c-obs', '#a86a2a');
      objCtx.strokeStyle = cv('--paper', '#f4efe6');
      objCtx.lineWidth = 2;
      objCtx.beginPath();
      objCtx.arc(pxo, pyo, isBest ? 6 : 4.5, 0, 2 * Math.PI);
      objCtx.fill();
      objCtx.stroke();
      if (isBest) {
        objCtx.strokeStyle = cv('--c-obs', '#a86a2a');
        objCtx.globalAlpha = 0.45;
        objCtx.lineWidth = 1;
        objCtx.beginPath();
        objCtx.arc(pxo, pyo, 10, 0, 2 * Math.PI);
        objCtx.stroke();
        objCtx.globalAlpha = 1;
      }
    }
    objCtx.restore();
  }

  function drawAcquisitionPlot() {
    var w = acqCanvas.clientWidth;
    var h = acqCanvas.clientHeight;
    acqCtx.clearRect(0, 0, w, h);
    if (!STATE.acqVals) { drawAxes(acqCtx, w, h, 0, 1); return; }

    var minA = Infinity, maxA = -Infinity;
    for (var v = 0; v < STATE.acqVals.length; v++) {
      var val = STATE.acqVals[v];
      if (val < minA) minA = val;
      if (val > maxA) maxA = val;
    }
    if (maxA - minA < 1e-6) maxA = minA + 1e-6;
    var pad = (maxA - minA) * 0.08;
    var yMin = minA - pad, yMax = maxA + pad;
    drawAxes(acqCtx, w, h, yMin, yMax);

    var g = STATE.grid;
    // Filled area
    acqCtx.save();
    acqCtx.beginPath();
    for (var i = 0; i < g.length; i++) {
      var px = xToPx(g[i], w);
      var val2 = STATE.acqVals[i];
      var py = PAD_T + (1 - (val2 - yMin) / (yMax - yMin)) * (h - PAD_T - PAD_B);
      if (i === 0) acqCtx.moveTo(px, py); else acqCtx.lineTo(px, py);
    }
    acqCtx.lineTo(xToPx(g[g.length - 1], w), h - PAD_B);
    acqCtx.lineTo(xToPx(g[0], w), h - PAD_B);
    acqCtx.closePath();
    acqCtx.fillStyle = cv('--c-acq-fill', 'rgba(77,106,143,0.14)');
    acqCtx.fill();
    acqCtx.restore();

    // Curve
    acqCtx.save();
    acqCtx.strokeStyle = cv('--c-acq', '#4d6a8f');
    acqCtx.lineWidth = 2;
    acqCtx.beginPath();
    for (var i2 = 0; i2 < g.length; i2++) {
      var px2 = xToPx(g[i2], w);
      var val3 = STATE.acqVals[i2];
      var py2 = PAD_T + (1 - (val3 - yMin) / (yMax - yMin)) * (h - PAD_T - PAD_B);
      if (i2 === 0) acqCtx.moveTo(px2, py2); else acqCtx.lineTo(px2, py2);
    }
    acqCtx.stroke();
    acqCtx.restore();

    // argmax marker
    if (STATE.nextX !== null) {
      var bi = 0, bd = Infinity;
      for (var j = 0; j < g.length; j++) {
        var d = Math.abs(g[j] - STATE.nextX);
        if (d < bd) { bd = d; bi = j; }
      }
      var pxm = xToPx(g[bi], w);
      var vv = STATE.acqVals[bi];
      var pym = PAD_T + (1 - (vv - yMin) / (yMax - yMin)) * (h - PAD_T - PAD_B);
      acqCtx.save();
      acqCtx.strokeStyle = cv('--c-next', '#b94a1b');
      acqCtx.globalAlpha = 0.38;
      acqCtx.lineWidth = 1;
      acqCtx.setLineDash([3, 4]);
      acqCtx.beginPath();
      acqCtx.moveTo(pxm, PAD_T);
      acqCtx.lineTo(pxm, h - PAD_B);
      acqCtx.stroke();
      acqCtx.globalAlpha = 1;
      acqCtx.setLineDash([]);
      acqCtx.fillStyle = cv('--c-next', '#b94a1b');
      acqCtx.beginPath();
      acqCtx.arc(pxm, pym, 5, 0, 2 * Math.PI);
      acqCtx.fill();
      acqCtx.strokeStyle = cv('--paper', '#f4efe6');
      acqCtx.lineWidth = 2;
      acqCtx.stroke();
      acqCtx.restore();
    }
  }

  function updateStatus() {
    document.getElementById('iterStat').textContent = STATE.iter;
    document.getElementById('nObsStat').textContent = STATE.obs.length;
    var b = currentBestFstar();
    document.getElementById('bestStat').textContent = isFinite(b.fmin) ? b.fmin.toFixed(3) : '—';
    document.getElementById('bestXStat').textContent = b.xmin !== null ? b.xmin.toFixed(3) : '—';
    document.getElementById('nextStat').textContent = STATE.nextX !== null ? STATE.nextX.toFixed(3) : '—';
    var names = { EI: 'Expected Improvement', UCB: 'Lower Confidence Bound', PI: 'Probability of Improvement' };
    document.getElementById('acqName').textContent = names[STATE.acq];
  }

  function draw() { drawObjectivePlot(); drawAcquisitionPlot(); updateStatus(); }

  function stepOnce() {
    if (STATE.nextX === null) return;
    var x = STATE.nextX;
    var dup = STATE.obs.some(function(o) { return Math.abs(o.x - x) < 1e-4; });
    if (dup) return;
    STATE.obs.push({ x: x, y: forrester(x) });
    STATE.iter += 1;
    refit();
    draw();
  }
  function addManualObservation(x) {
    if (x < X_MIN || x > X_MAX) return;
    var dup = STATE.obs.some(function(o) { return Math.abs(o.x - x) < 1e-3; });
    if (dup) return;
    STATE.obs.push({ x: x, y: forrester(x) });
    STATE.iter += 1;
    refit();
    draw();
  }
  function reset() { seedInitial(); refit(); draw(); }

  document.getElementById('stepBtn').addEventListener('click', stepOnce);
  document.getElementById('resetBtn').addEventListener('click', reset);
  document.getElementById('auto10Btn').addEventListener('click', function() {
    var count = 0;
    (function runner() {
      if (count >= 10) return;
      stepOnce();
      count += 1;
      setTimeout(runner, 220);
    })();
  });

  document.querySelectorAll('#acqGroup button').forEach(function(btn) {
    btn.addEventListener('click', function() {
      document.querySelectorAll('#acqGroup button').forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
      STATE.acq = btn.dataset.acq;
      refit();
      draw();
    });
  });

  function bindSlider(id, valId, fmt, setter) {
    var s = document.getElementById(id);
    var vEl = document.getElementById(valId);
    s.addEventListener('input', function() {
      var v = parseFloat(s.value);
      setter(v);
      vEl.textContent = fmt(v);
      refit();
      draw();
    });
  }
  bindSlider('lsSlider', 'lsVal', function(v) { return v.toFixed(2); }, function(v) { STATE.ls = v; });
  bindSlider('kappaSlider', 'kappaVal', function(v) { return v.toFixed(1); }, function(v) { STATE.kappa = v; });
  bindSlider('xiSlider', 'xiVal', function(v) { return v.toFixed(2); }, function(v) { STATE.xi = v; });

  var trueToggle = document.getElementById('trueToggle');
  function toggleTrue() {
    STATE.showTrue = !STATE.showTrue;
    trueToggle.classList.toggle('on', STATE.showTrue);
    trueToggle.setAttribute('aria-pressed', String(STATE.showTrue));
    draw();
  }
  trueToggle.addEventListener('click', toggleTrue);
  trueToggle.addEventListener('keydown', function(e) {
    if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); toggleTrue(); }
  });

  // Click on objective canvas → add observation
  objCanvas.addEventListener('click', function(e) {
    var rect = objCanvas.getBoundingClientRect();
    var w = rect.width;
    var px = e.clientX - rect.left;
    var x = pxToX(px, w);
    if (x >= X_MIN && x <= X_MAX) addManualObservation(x);
  });

  // Hover tooltip
  var tooltip = document.getElementById('objTooltip');
  objCanvas.addEventListener('mousemove', function(e) {
    if (!STATE.gpPred) return;
    var rect = objCanvas.getBoundingClientRect();
    var w = rect.width;
    var px = e.clientX - rect.left;
    var x = pxToX(px, w);
    if (x < X_MIN || x > X_MAX) { tooltip.classList.remove('visible'); return; }
    var bi = 0, bd = Infinity;
    for (var i = 0; i < STATE.grid.length; i++) {
      var d = Math.abs(STATE.grid[i] - x);
      if (d < bd) { bd = d; bi = i; }
    }
    var mp = STATE.gpPred[bi];
    tooltip.textContent = 'x=' + x.toFixed(3) + '  μ=' + mp.mean.toFixed(2) + '  σ=' + mp.std.toFixed(2);
    tooltip.style.left = (px + 12) + 'px';
    tooltip.style.top = (e.clientY - rect.top - 6) + 'px';
    tooltip.classList.add('visible');
  });
  objCanvas.addEventListener('mouseleave', function() { tooltip.classList.remove('visible'); });

  // Init
  window.addEventListener('resize', resizeCanvases);
  seedInitial();
  refit();
  resizeCanvases();
})();
</script>
