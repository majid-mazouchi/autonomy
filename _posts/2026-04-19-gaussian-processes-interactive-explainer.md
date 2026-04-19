---
title: "Gaussian Processes — an Interactive Explainer"
subtitle: "A distribution over functions, with calibrated uncertainty that grows where you haven't looked."
date: 2026-04-19 09:00:00 -0400
category: "Machine Learning"
slug: gaussian-processes-interactive-explainer
excerpt: "Click, slide, and watch the posterior update. A working intuition for Gaussian Processes — from the one-sentence definition through the Cholesky math and the honest O(n³) scaling story."
reading_time: 14
---

A Gaussian Process is one of those ideas that looks abstract on paper and clicks the moment you can actually *play* with one. The object of this post is that moment. Below is an interactive plot where the prior, the posterior, and all the kernel hyperparameters respond in real time. The prose around it tries to match what you're seeing on the screen to the math underneath — and, in the last section, to the very un-glamorous reality of the $O(n^3)$ cost that determines when GPs earn their keep.

## What is a GP, really?

<div class="callout-soft" markdown="1">

**The plain-English version.** Imagine you're trying to guess an unknown function from just a few measurements. A Gaussian Process is a principled way of saying: "*here are all the functions I think are plausible*" — and then updating that belief every time you see a new data point.

Three ideas to hold onto:

1. It's a *distribution over functions*, not over numbers. Instead of "$x = 3.2 \pm 0.5$", a GP gives you "the function could be this shape, or this one, or this one" — an infinite family of curves, each with a probability.
2. The *kernel* encodes your assumption about smoothness: points that are close in input should have similar output values. That one assumption is enough to turn a handful of measurements into a full curve with confidence bounds.
3. The magic is *calibrated uncertainty*. Near your data the GP is confident, far from it the GP is humble and the error bars grow. That honesty is what makes GPs useful for control, optimization, and diagnostics — the model tells you when not to trust it.

</div>

A one-line mental model: a GP is **linear regression with infinitely many features**, where the kernel silently handles the infinite sum for you.

## The one-sentence definition

A **Gaussian Process** is a distribution over functions such that any finite collection of function values has a joint Gaussian distribution. It is fully specified by a mean function $m(x)$ and a covariance (kernel) function $k(x, x')$:

$$ f(x) \sim \mathcal{GP}\!\left( m(x),\; k(x, x') \right) $$

In practice we almost always set $m(x) = 0$ (after centering the data) and do all the modeling work through the kernel.

## Interactive demo

<div class="gp-widget">

  <div class="mode-bar">
    <button id="mode-prior" type="button">Prior (no data)</button>
    <button id="mode-post" class="active" type="button">Posterior (with data)</button>
    <button id="clear" type="button">Clear points</button>
    <button id="resample" type="button">Resample</button>
  </div>

  <div class="hint" id="mode-hint">Posterior: click on the plot to add (or remove) observations. The GP conditions on them — the mean threads through the points, variance collapses nearby, and stays high far away.</div>

  <canvas id="gp-canvas" width="780" height="400"></canvas>

  <div class="legend">
    <div class="item"><span class="swatch mean"></span> Posterior mean</div>
    <div class="item"><span class="swatch band"></span> 95% credible band</div>
    <div class="item"><span class="swatch sample"></span> Sampled functions</div>
    <div class="item"><span class="dot-swatch"></span> Observations</div>
  </div>

  <div class="controls">
    <div class="control">
      <label>Length scale ℓ <span class="val" id="ls-val">1.00</span></label>
      <input type="range" id="ls" min="0.1" max="3.0" step="0.05" value="1.0" />
      <p class="caption">Smoothness of sampled functions</p>
    </div>
    <div class="control">
      <label>Signal variance σ<sub>f</sub>² <span class="val" id="sf-val">1.00</span></label>
      <input type="range" id="sf" min="0.1" max="3.0" step="0.05" value="1.0" />
      <p class="caption">Vertical amplitude of functions</p>
    </div>
    <div class="control">
      <label>Noise σ<sub>n</sub> <span class="val" id="sn-val">0.10</span></label>
      <input type="range" id="sn" min="0.001" max="0.5" step="0.005" value="0.1" />
      <p class="caption">Observation noise std</p>
    </div>
    <div class="control">
      <label>Sample paths <span class="val" id="ns-val">5</span></label>
      <input type="range" id="ns" min="0" max="10" step="1" value="5" />
      <p class="caption">Number of drawn functions</p>
    </div>
  </div>

  <div class="kernel-box">
    <div class="k-label">Kernel: squared exponential (RBF)</div>
    <div class="k-eq">k(x, x') = σ<sub>f</sub>² · exp( −(x − x')² / (2ℓ²) )</div>
  </div>

</div>

## How to read the plot

### The prior

Click *Prior* and slide **Sample paths** up. Every colored curve is one function drawn from $\mathcal{GP}(0, k)$. The shaded band is the 95% credible region. Before seeing any data, the GP says "the function could be any of these."

The length scale $\ell$ controls how wiggly these samples are:

- **Small $\ell$** — nearby inputs are only weakly correlated, so samples look rough.
- **Large $\ell$** — strong correlation, so samples look smooth.

The signal variance $\sigma_f^2$ scales the vertical amplitude of the prior.

### The posterior

Click *Posterior* and then click anywhere on the plot to drop observations. Click an existing point to remove it. Two things happen:

- The **mean** curve threads through the observations (or very close, limited by the noise $\sigma_n$).
- The **uncertainty band** collapses near data points and re-opens in regions with no data.

> **Key takeaway.** This is the main selling point for GPs: *calibrated uncertainty that grows where you haven't looked*. That's exactly why they shine in sparse-data regimes like active learning, Bayesian optimization, and safe control.

## The math in three lines

Given training data $(X, y)$ with i.i.d. Gaussian noise $\sigma_n^2$, the joint distribution of the observed targets and the function value $f_*$ at a test point $x_*$ is:

$$
\begin{bmatrix} y \\ f_* \end{bmatrix}
\sim \mathcal{N}\!\left(
\begin{bmatrix} 0 \\ 0 \end{bmatrix},\;
\begin{bmatrix}
K(X,X) + \sigma_n^2 I & K(X, x_*) \\
K(x_*, X) & K(x_*, x_*)
\end{bmatrix}
\right)
$$

Conditioning on $y$ using the standard Gaussian conditioning identity gives closed-form posterior mean and variance:

$$ \mu_* = K(x_*, X) \left[ K(X,X) + \sigma_n^2 I \right]^{-1} y $$

$$ \sigma_*^2 = K(x_*, x_*) - K(x_*, X) \left[ K(X,X) + \sigma_n^2 I \right]^{-1} K(X, x_*) $$

The widget implements exactly this. For numerical stability we use a Cholesky decomposition:

```text
K + σ_n²·I = L · Lᵀ       (Cholesky, O(n³))
α = Lᵀ \ (L \ y)           (triangular solves)
μ*  = k*ᵀ · α              (mean at test point)
v   = L \ k*
σ*² = k(x*, x*) − vᵀv      (variance at test point)
```

## Common kernels

- **Squared Exponential (RBF).** Infinitely differentiable. Produces very smooth functions. Default choice, used in the demo above.
- **Matérn ($\nu = 3/2,\ 5/2$).** Controllable smoothness. Often more realistic than RBF for physical signals that are continuous but not infinitely smooth.
- **Periodic.** Encodes periodicity with a fixed period. Good for oscillatory signals like motor ripple or seasonal effects.
- **Linear.** Recovers Bayesian linear regression as a special case.
- **Sums and products.** Kernels are closed under addition and multiplication, so you can compose them — e.g. `Periodic · RBF` for a slowly-decaying oscillation.

## Hyperparameter learning

The kernel hyperparameters $\theta = \{\ell, \sigma_f, \sigma_n\}$ are typically learned by maximizing the **log marginal likelihood** of the observed data:

$$ \log p(y \mid X, \theta) = -\tfrac{1}{2}\, y^{\!\top} \!\left[K + \sigma_n^2 I\right]^{-1} y \;-\; \tfrac{1}{2} \log \!\left| K + \sigma_n^2 I \right| \;-\; \tfrac{n}{2} \log 2\pi $$

The three terms have a clean interpretation: *data fit*, *complexity penalty*, and a constant. This is the built-in Occam's razor that makes GPs elegant — overly wiggly models are penalized by the log-determinant term.

## Computational complexity

GPs are conceptually clean but computationally heavy. The cost is dominated by a single operation: inverting (or Cholesky-factorizing) the $n \times n$ kernel matrix $K + \sigma_n^2 I$, where $n$ is the number of training points.

### Exact GP — the honest numbers

| Operation | Time | Memory | What's happening |
|---|---|---|---|
| Training (one-time) | `O(n³)` | `O(n²)` | Build `K`, do Cholesky `K = LLᵀ`, solve for `α = K⁻¹y` |
| Predict mean (per test point) | `O(n)` | `O(n)` | Inner product `k*ᵀα` — cheap once `α` is cached |
| Predict variance (per test point) | `O(n²)` | `O(n)` | Triangular solve `v = L \ k*`, then `σ*² = k** − vᵀv` |
| Hyperparameter learning (per iter.) | `O(n³)` | `O(n²)` | New `θ` → rebuild `K` → redo Cholesky → gradient of log-marginal-likelihood |

> **Rule of thumb.** Exact GP is comfortable up to a few thousand points on a laptop. At $n \approx 10{,}000$ you're hitting the wall (memory for $K$ alone is roughly 800 MB in float64, and one Cholesky takes minutes). Beyond that, you need approximations.

### Why it's $O(n^3)$

The $O(n^3)$ cost comes from the Cholesky decomposition of the kernel matrix, which is the dominant numerical step. Every time hyperparameters change during training, the matrix changes, and the whole factorization has to be redone. Mean prediction at a new test point is cheap because it's just a dot product against a precomputed vector. Variance prediction is more expensive because each test point needs its own triangular solve against $L$.

### Scaling beyond exact GP

| Method | Training | Prediction | Idea |
|---|---|---|---|
| Exact GP | `O(n³)` | `O(n²)` | Full Cholesky — baseline |
| Sparse GP / FITC | `O(n·m²)` | `O(m²)` | `m` inducing points summarize `n` training points |
| SVGP (variational) | `O(m³)` per batch | `O(m²)` | Mini-batch training; scales to millions of points |
| KISS-GP / SKI | `O(n + m log m)` | `O(1)` amortized | Structured kernel interpolation on a grid |
| Local GPs | `O(k³)` per local model | `O(k²)` | Partition input space, fit a small GP per region |

Here $m$ is the number of inducing (pseudo-)points, usually $m \ll n$, and $k$ is the local neighborhood size. In practice, $m$ in the range 50–500 is common.

> **Embedded context.** For real-time control (GP-augmented MPC, for instance), even the $O(n)$ or $O(m)$ prediction cost matters. Common tricks: freeze hyperparameters offline, precompute $\alpha$, use a small fixed inducing set, or switch to a parametric approximation once the GP has been learned.

## When to reach for a GP

- **Small-to-medium data** where uncertainty quantification matters more than raw throughput (GP inference is $O(n^3)$, impractical beyond ~10k points without approximations).
- **Bayesian optimization** — GP surrogate + acquisition function (EI, UCB) for expensive black-box optimization.
- **Active learning** — pick the next query where posterior variance is highest.
- **Safe / uncertainty-aware control** — GP-augmented MPC uses the GP posterior mean to correct model mismatch and the variance to gate how aggressively the controller trusts that correction.
- **System identification and calibration** — non-parametric regression with confidence bounds that grow in extrapolation regions.
- **Diagnostics and prognostics** — detect when the current operating point is out-of-distribution relative to training data.

## Limitations to be honest about

- **Scaling.** Naïve GP is $O(n^3)$ / $O(n^2)$. Sparse variational GPs, inducing points, and structured kernels (KISS-GP, SKI) push this further.
- **High input dimensions.** Stationary kernels suffer in high-$D$ without ARD or dimensionality reduction.
- **Kernel choice matters.** A misspecified kernel gives confidently wrong uncertainty — the variance is only calibrated *given* the model.
- **Non-Gaussian likelihoods.** Classification and count data need approximations (Laplace, EP, variational).

---

The interactive demo above is implemented with vanilla JavaScript and the Canvas 2D API — Cholesky solve, posterior sampling, and kernel evaluation are all in-browser, no external libraries. View source on the page if you want to read it.

<!-- =====================================================
     Post-scoped styles for the interactive GP widget
     Reuses the blog's CSS variables (paper, ink, rule, accent)
     so it harmonizes with the warm editorial theme.
     ===================================================== -->
<style>
  .article-body .callout-soft {
    background: var(--paper-2);
    border-left: 3px solid var(--accent);
    border-radius: 0 4px 4px 0;
    padding: 18px 24px;
    margin: 28px auto;
    max-width: var(--read);
    font-size: 1rem;
  }
  .article-body .callout-soft p { margin: 0 0 12px; }
  .article-body .callout-soft p:last-child { margin-bottom: 0; }
  .article-body .callout-soft ol { padding-left: 20px; margin: 0 0 0; }
  .article-body .callout-soft li { margin: 8px 0; }

  .article-body .gp-widget {
    max-width: var(--read);
    margin: 28px auto 36px;
    background: var(--paper-2);
    border: 1px solid var(--rule);
    border-radius: 4px;
    padding: 22px;
    font-family: var(--f-body);
  }

  .article-body .gp-widget .mode-bar {
    display: flex;
    gap: 8px;
    margin: 0 0 14px;
    flex-wrap: wrap;
  }
  .article-body .gp-widget button {
    font-family: var(--f-ui);
    font-size: .74rem;
    font-weight: 400;
    letter-spacing: .08em;
    text-transform: uppercase;
    background: transparent;
    color: var(--ink);
    border: 1px solid var(--rule);
    border-radius: 2px;
    padding: 8px 12px;
    cursor: pointer;
    transition: background .15s ease, color .15s ease, border-color .15s ease;
  }
  .article-body .gp-widget button:hover {
    background: var(--paper);
    border-color: var(--ink-mute);
  }
  .article-body .gp-widget button.active {
    background: var(--accent);
    color: var(--paper);
    border-color: var(--accent);
  }

  .article-body .gp-widget .hint {
    font-family: var(--f-body);
    font-size: .92rem;
    font-style: italic;
    color: var(--ink-soft);
    margin: 0 0 14px;
    line-height: 1.5;
  }

  .article-body .gp-widget canvas#gp-canvas {
    width: 100%;
    height: auto;
    display: block;
    background: var(--paper);
    border: 1px solid var(--rule);
    border-radius: 2px;
    cursor: crosshair;
    margin: 0 0 14px;
  }

  .article-body .gp-widget .legend {
    display: flex;
    gap: 18px;
    flex-wrap: wrap;
    font-family: var(--f-ui);
    font-size: .72rem;
    letter-spacing: .08em;
    text-transform: uppercase;
    color: var(--ink-mute);
    margin: 0 0 18px;
  }
  .article-body .gp-widget .legend .item {
    display: inline-flex; align-items: center; gap: 6px;
  }
  .article-body .gp-widget .swatch { display: inline-block; width: 18px; height: 2px; }
  .article-body .gp-widget .swatch.mean { background: var(--ink); }
  .article-body .gp-widget .swatch.sample { background: var(--accent); }
  .article-body .gp-widget .swatch.band {
    height: 10px;
    background: rgba(185, 74, 27, 0.18);
    border-radius: 1px;
  }
  .article-body .gp-widget .dot-swatch {
    display: inline-block;
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--ink);
  }

  .article-body .gp-widget .controls {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 18px;
    margin: 0 0 4px;
  }
  .article-body .gp-widget .control label {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-family: var(--f-ui);
    font-size: .76rem;
    letter-spacing: .04em;
    color: var(--ink-soft);
    margin: 0 0 6px;
  }
  .article-body .gp-widget .control label .val {
    color: var(--ink);
    font-variant-numeric: tabular-nums;
    font-weight: 500;
  }
  .article-body .gp-widget .control .caption {
    font-family: var(--f-body);
    font-size: .82rem;
    font-style: italic;
    color: var(--ink-mute);
    margin: 6px 0 0;
  }

  .article-body .gp-widget input[type="range"] {
    -webkit-appearance: none;
    appearance: none;
    width: 100%;
    height: 3px;
    background: var(--rule);
    border-radius: 2px;
    outline: none;
    margin: 6px 0;
  }
  .article-body .gp-widget input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 16px; height: 16px;
    background: var(--accent);
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid var(--paper);
    box-shadow: 0 0 0 1px var(--accent);
  }
  .article-body .gp-widget input[type="range"]::-moz-range-thumb {
    width: 14px; height: 14px;
    background: var(--accent);
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid var(--paper);
    box-shadow: 0 0 0 1px var(--accent);
  }

  .article-body .gp-widget .kernel-box {
    background: var(--paper);
    border: 1px solid var(--rule);
    border-radius: 2px;
    padding: 12px 16px;
    margin: 18px 0 0;
    font-size: .9rem;
  }
  .article-body .gp-widget .kernel-box .k-label {
    font-family: var(--f-ui);
    font-size: .72rem;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: var(--ink-mute);
    margin-bottom: 6px;
  }
  .article-body .gp-widget .kernel-box .k-eq {
    font-family: var(--f-ui);
    color: var(--ink);
    font-size: .88rem;
  }

  /* Tables within the article body */
  .article-body table {
    width: 100%;
    max-width: var(--read);
    margin: 24px auto;
    border-collapse: collapse;
    font-size: .94rem;
  }
  .article-body table th,
  .article-body table td {
    text-align: left;
    padding: 10px 12px;
    border-bottom: 1px solid var(--rule);
    vertical-align: top;
  }
  .article-body table th {
    font-family: var(--f-ui);
    font-weight: 500;
    font-size: .74rem;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: var(--ink-mute);
    border-bottom: 1px solid var(--ink);
  }
  .article-body table td:first-child { font-weight: 500; }
  .article-body table code {
    background: var(--tag-bg);
    color: var(--ink);
    font-size: .86em;
  }
</style>

<script>
(function() {
  var canvas = document.getElementById('gp-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');

  function getCSS(name) {
    return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  }

  // Warm palette that harmonizes with the blog's burnt-orange accent
  var SAMPLE_COLORS = [
    '#b94a1b', // accent — burnt orange
    '#4d6a8f', // muted steel blue
    '#6b8a3f', // olive green
    '#8a4a6b', // dusty burgundy
    '#a86a2a', // bronze
    '#3f7a6b', // teal
    '#7a4a3a', // brick
    '#5a6a4a', // moss
    '#9a6a4a', // sienna
    '#4a4a7a'  // indigo
  ];

  function resizeCanvas() {
    var dpr = window.devicePixelRatio || 1;
    var rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = 400 * dpr;
    canvas.style.height = '400px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    draw();
  }

  var W = function() { return canvas.getBoundingClientRect().width; };
  var H = function() { return 400; };
  var PAD_L = 48, PAD_R = 20, PAD_T = 20, PAD_B = 40;
  var plotW = function() { return W() - PAD_L - PAD_R; };
  var plotH = function() { return H() - PAD_T - PAD_B; };

  var X_MIN = -5, X_MAX = 5;
  var Y_MIN = -3, Y_MAX = 3;

  var N_TEST = 120;
  var xTest = [];
  for (var i = 0; i < N_TEST; i++) xTest.push(X_MIN + (X_MAX - X_MIN) * i / (N_TEST - 1));

  var mode = 'post';
  var points = [{x: -3, y: 0.5}, {x: -1, y: -0.8}, {x: 1.5, y: 1.2}, {x: 3, y: -0.3}];
  var ls = 1.0, sf = 1.0, sn = 0.1, nSamples = 5;
  var sampleSeed = 42;

  function xToPx(x) { return PAD_L + (x - X_MIN) / (X_MAX - X_MIN) * plotW(); }
  function yToPx(y) { return PAD_T + (Y_MAX - y) / (Y_MAX - Y_MIN) * plotH(); }
  function pxToX(px) { return X_MIN + (px - PAD_L) / plotW() * (X_MAX - X_MIN); }
  function pxToY(py) { return Y_MAX - (py - PAD_T) / plotH() * (Y_MAX - Y_MIN); }

  function rbf(x1, x2) {
    var d = x1 - x2;
    return sf * sf * Math.exp(-(d * d) / (2 * ls * ls));
  }

  function buildK(xs) {
    var n = xs.length;
    var K = [];
    for (var i = 0; i < n; i++) {
      K.push([]);
      for (var j = 0; j < n; j++) K[i].push(rbf(xs[i], xs[j]));
    }
    return K;
  }

  function cholesky(A) {
    var n = A.length;
    var L = [];
    for (var i = 0; i < n; i++) L.push(new Array(n).fill(0));
    for (var i2 = 0; i2 < n; i2++) {
      for (var j = 0; j <= i2; j++) {
        var s = 0;
        for (var k = 0; k < j; k++) s += L[i2][k] * L[j][k];
        if (i2 === j) {
          var v = A[i2][i2] - s;
          L[i2][j] = Math.sqrt(Math.max(v, 1e-10));
        } else {
          L[i2][j] = (A[i2][j] - s) / L[j][j];
        }
      }
    }
    return L;
  }

  function solveLower(L, b) {
    var n = L.length;
    var y = new Array(n).fill(0);
    for (var i = 0; i < n; i++) {
      var s = 0;
      for (var k = 0; k < i; k++) s += L[i][k] * y[k];
      y[i] = (b[i] - s) / L[i][i];
    }
    return y;
  }

  function solveUpper(LT, b) {
    var n = LT.length;
    var x = new Array(n).fill(0);
    for (var i = n - 1; i >= 0; i--) {
      var s = 0;
      for (var k = i + 1; k < n; k++) s += LT[i][k] * x[k];
      x[i] = (b[i] - s) / LT[i][i];
    }
    return x;
  }

  function transpose(A) {
    var n = A.length, m = A[0].length;
    var T = [];
    for (var i = 0; i < m; i++) {
      T.push([]);
      for (var j = 0; j < n; j++) T[i].push(A[j][i]);
    }
    return T;
  }

  var rngState = sampleSeed;
  function seed(s) { rngState = s; }
  function rand() {
    rngState = (rngState * 1664525 + 1013904223) % 4294967296;
    return rngState / 4294967296;
  }
  function randn() {
    var u = Math.max(rand(), 1e-10);
    var v = rand();
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
  }

  function computeGP() {
    var n = points.length;
    var mean = new Array(N_TEST).fill(0);
    var variance = new Array(N_TEST).fill(sf * sf);
    var cholPost = null;

    if (mode === 'post' && n > 0) {
      var xs = points.map(function(p) { return p.x; });
      var ys = points.map(function(p) { return p.y; });

      var Kxx = buildK(xs);
      for (var i = 0; i < n; i++) Kxx[i][i] += sn * sn;

      var L = cholesky(Kxx);
      var alpha = solveUpper(transpose(L), solveLower(L, ys));

      var Kxs = [];
      for (var i2 = 0; i2 < n; i2++) {
        Kxs.push([]);
        for (var j = 0; j < N_TEST; j++) Kxs[i2].push(rbf(xs[i2], xTest[j]));
      }

      for (var j2 = 0; j2 < N_TEST; j2++) {
        var m = 0;
        for (var i3 = 0; i3 < n; i3++) m += Kxs[i3][j2] * alpha[i3];
        mean[j2] = m;
      }

      for (var j3 = 0; j3 < N_TEST; j3++) {
        var kxs = Kxs.map(function(row) { return row[j3]; });
        var v2 = solveLower(L, kxs);
        var vv = 0;
        for (var i4 = 0; i4 < n; i4++) vv += v2[i4] * v2[i4];
        variance[j3] = Math.max(sf * sf - vv, 1e-8);
      }

      var Kss = buildK(xTest);
      var KsxT = [];
      for (var i5 = 0; i5 < N_TEST; i5++) {
        KsxT.push([]);
        for (var k = 0; k < n; k++) KsxT[i5].push(rbf(xTest[i5], xs[k]));
      }
      var Kpost = [];
      for (var i6 = 0; i6 < N_TEST; i6++) {
        Kpost.push([]);
        var vi = solveLower(L, KsxT[i6]);
        for (var j4 = 0; j4 < N_TEST; j4++) {
          var vj = solveLower(L, KsxT[j4]);
          var dot = 0;
          for (var k2 = 0; k2 < n; k2++) dot += vi[k2] * vj[k2];
          Kpost[i6].push(Kss[i6][j4] - dot + (i6 === j4 ? 1e-6 : 0));
        }
      }
      cholPost = cholesky(Kpost);
    } else {
      var Kss2 = buildK(xTest);
      for (var i7 = 0; i7 < N_TEST; i7++) Kss2[i7][i7] += 1e-6;
      cholPost = cholesky(Kss2);
    }

    return { mean: mean, variance: variance, cholPost: cholPost };
  }

  function drawSample(chol, mean) {
    var n = chol.length;
    var z = [];
    for (var i = 0; i < n; i++) z.push(randn());
    var sample = new Array(n).fill(0);
    for (var i2 = 0; i2 < n; i2++) {
      var s = 0;
      for (var k = 0; k <= i2; k++) s += chol[i2][k] * z[k];
      sample[i2] = mean[i2] + s;
    }
    return sample;
  }

  function bandFillColor() {
    // Pull the accent from the document and use it for the credible band
    var acc = getCSS('--accent') || '#b94a1b';
    // Derive an rgba from the hex so it works in both light/dark
    if (acc[0] === '#' && (acc.length === 7 || acc.length === 4)) {
      var r, g, b;
      if (acc.length === 7) {
        r = parseInt(acc.slice(1, 3), 16);
        g = parseInt(acc.slice(3, 5), 16);
        b = parseInt(acc.slice(5, 7), 16);
      } else {
        r = parseInt(acc[1] + acc[1], 16);
        g = parseInt(acc[2] + acc[2], 16);
        b = parseInt(acc[3] + acc[3], 16);
      }
      return 'rgba(' + r + ',' + g + ',' + b + ',0.18)';
    }
    return 'rgba(185,74,27,0.18)';
  }

  function draw() {
    var textCol  = getCSS('--ink')      || '#1a1814';
    var textMute = getCSS('--ink-mute') || '#8a8277';
    var rule     = getCSS('--rule')     || '#c8bfae';
    var paper    = getCSS('--paper')    || '#f4efe6';

    var w = W(), h = H();
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = paper;
    ctx.fillRect(0, 0, w, h);

    // Grid
    ctx.strokeStyle = rule;
    ctx.lineWidth = 0.5;
    ctx.setLineDash([3, 3]);
    for (var gx = Math.ceil(X_MIN); gx <= X_MAX; gx++) {
      ctx.beginPath();
      ctx.moveTo(xToPx(gx), PAD_T);
      ctx.lineTo(xToPx(gx), PAD_T + plotH());
      ctx.stroke();
    }
    for (var gy = Math.ceil(Y_MIN); gy <= Y_MAX; gy++) {
      ctx.beginPath();
      ctx.moveTo(PAD_L, yToPx(gy));
      ctx.lineTo(PAD_L + plotW(), yToPx(gy));
      ctx.stroke();
    }
    ctx.setLineDash([]);

    // Axes
    ctx.strokeStyle = textMute;
    ctx.lineWidth = 0.5;
    ctx.beginPath();
    ctx.moveTo(PAD_L, PAD_T);
    ctx.lineTo(PAD_L, PAD_T + plotH());
    ctx.lineTo(PAD_L + plotW(), PAD_T + plotH());
    ctx.stroke();

    // Labels
    ctx.fillStyle = textMute;
    ctx.font = '11px ' + getComputedStyle(document.body).fontFamily;
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    for (var gy2 = Math.ceil(Y_MIN); gy2 <= Y_MAX; gy2++) {
      ctx.fillText(gy2.toFixed(0), PAD_L - 8, yToPx(gy2));
    }
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    for (var gx2 = Math.ceil(X_MIN); gx2 <= X_MAX; gx2++) {
      ctx.fillText(gx2.toFixed(0), xToPx(gx2), PAD_T + plotH() + 8);
    }
    ctx.fillText('x', PAD_L + plotW() / 2, PAD_T + plotH() + 22);
    ctx.save();
    ctx.translate(16, PAD_T + plotH() / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('f(x)', 0, 0);
    ctx.restore();

    var r = computeGP();
    var mean = r.mean, variance = r.variance, cholPost = r.cholPost;

    // Credible band
    ctx.fillStyle = bandFillColor();
    ctx.beginPath();
    for (var i = 0; i < N_TEST; i++) {
      var std = Math.sqrt(variance[i]);
      var upper = mean[i] + 2 * std;
      var px = xToPx(xTest[i]);
      var py = yToPx(Math.min(upper, Y_MAX));
      if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    for (var i2 = N_TEST - 1; i2 >= 0; i2--) {
      var std2 = Math.sqrt(variance[i2]);
      var lower = mean[i2] - 2 * std2;
      ctx.lineTo(xToPx(xTest[i2]), yToPx(Math.max(lower, Y_MIN)));
    }
    ctx.closePath();
    ctx.fill();

    // Sampled functions
    seed(sampleSeed);
    for (var s = 0; s < nSamples; s++) {
      var sample = drawSample(cholPost, mean);
      ctx.strokeStyle = SAMPLE_COLORS[s % SAMPLE_COLORS.length];
      ctx.globalAlpha = 0.72;
      ctx.lineWidth = 1.3;
      ctx.beginPath();
      for (var i3 = 0; i3 < N_TEST; i3++) {
        var px2 = xToPx(xTest[i3]);
        var py2 = yToPx(sample[i3]);
        if (i3 === 0) ctx.moveTo(px2, py2); else ctx.lineTo(px2, py2);
      }
      ctx.stroke();
    }
    ctx.globalAlpha = 1;

    // Posterior mean
    ctx.strokeStyle = textCol;
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (var i4 = 0; i4 < N_TEST; i4++) {
      var px3 = xToPx(xTest[i4]);
      var py3 = yToPx(mean[i4]);
      if (i4 === 0) ctx.moveTo(px3, py3); else ctx.lineTo(px3, py3);
    }
    ctx.stroke();

    // Observations
    if (mode === 'post') {
      for (var pi = 0; pi < points.length; pi++) {
        var p = points[pi];
        ctx.fillStyle = textCol;
        ctx.beginPath();
        ctx.arc(xToPx(p.x), yToPx(p.y), 5, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = paper;
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }
    }

    // Mode label
    ctx.fillStyle = textMute;
    ctx.font = '11px ' + getComputedStyle(document.body).fontFamily;
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    var label = mode === 'prior'
      ? 'Prior GP · no data'
      : 'Posterior GP · ' + points.length + ' observation' + (points.length === 1 ? '' : 's');
    ctx.fillText(label, PAD_L + 8, PAD_T + 6);
  }

  canvas.addEventListener('click', function(e) {
    if (mode !== 'post') return;
    var rect = canvas.getBoundingClientRect();
    var px = e.clientX - rect.left;
    var py = e.clientY - rect.top;
    if (px < PAD_L || px > PAD_L + plotW() || py < PAD_T || py > PAD_T + plotH()) return;
    var x = pxToX(px), y = pxToY(py);

    for (var i = 0; i < points.length; i++) {
      if (Math.abs(points[i].x - x) < 0.25 && Math.abs(points[i].y - y) < 0.25) {
        points.splice(i, 1);
        draw();
        return;
      }
    }
    points.push({x: x, y: y});
    draw();
  });

  function bindSlider(id, out, fmt, setter) {
    var el = document.getElementById(id);
    var o = document.getElementById(out);
    el.addEventListener('input', function() {
      var v = parseFloat(el.value);
      setter(v);
      o.textContent = fmt(v);
      draw();
    });
  }

  bindSlider('ls', 'ls-val', function(v) { return v.toFixed(2); }, function(v) { ls = v; });
  bindSlider('sf', 'sf-val', function(v) { return v.toFixed(2); }, function(v) { sf = v; });
  bindSlider('sn', 'sn-val', function(v) { return v.toFixed(2); }, function(v) { sn = v; });
  bindSlider('ns', 'ns-val', function(v) { return v.toFixed(0); }, function(v) { nSamples = v; });

  var btnPrior = document.getElementById('mode-prior');
  var btnPost  = document.getElementById('mode-post');

  btnPrior.addEventListener('click', function() {
    mode = 'prior';
    btnPrior.classList.add('active');
    btnPost.classList.remove('active');
    document.getElementById('mode-hint').textContent =
      'Prior: no data. Functions are drawn from GP(0, k). Adjust ℓ and σ_f to see how the kernel shapes the prior distribution.';
    draw();
  });

  btnPost.addEventListener('click', function() {
    mode = 'post';
    btnPost.classList.add('active');
    btnPrior.classList.remove('active');
    document.getElementById('mode-hint').textContent =
      'Posterior: click on the plot to add (or remove) observations. The GP conditions on them — the mean threads through the points, variance collapses nearby, and stays high far away.';
    draw();
  });

  document.getElementById('clear').addEventListener('click', function() {
    points = [];
    draw();
  });

  document.getElementById('resample').addEventListener('click', function() {
    sampleSeed = Math.floor(Math.random() * 1000000);
    draw();
  });

  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();
})();
</script>
