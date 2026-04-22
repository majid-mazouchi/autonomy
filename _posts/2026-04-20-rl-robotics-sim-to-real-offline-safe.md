---
title: "Robotics in Practice: Sim-to-Real, Offline RL, and Safe RL"
subtitle: "The 70% of a successful RL project that doesn't show up in papers — reward design, domain randomization, learning from logged data, and building safety architectures that don't depend on the learner being correct."
date: 2026-04-20 21:00:00 -0400
category: "Reinforcement Learning"
slug: rl-robotics-sim-to-real-offline-safe
excerpt: "Algorithms are maybe 30% of a successful RL robotics project. The other 70% is engineering: reward design, observation and action spaces, sim-to-real, learning from logged data, and layered safety. This post is the part nobody teaches in school."
reading_time: 19
---

This is the final post in the [field guide to reinforcement learning for control and robotics]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }}). The previous six posts built up the theory and the algorithms — [MDPs]({{ '/posts/rl-foundations-mdps-value-functions-bellman/' | relative_url }}), [TD learning]({{ '/posts/rl-td-sarsa-q-learning/' | relative_url }}), [policy gradients]({{ '/posts/rl-policy-gradients-actor-critic/' | relative_url }}), [the modern toolkit]({{ '/posts/rl-exploration-sac-ppo-td3-ddpg/' | relative_url }}), [model-based RL]({{ '/posts/rl-model-based-mpc-hybrids/' | relative_url }}). None of that is what actually ships a policy.

Algorithms are maybe 30% of a successful RL robotics project. The other 70% is the engineering the papers don't cover — reward design, observation and action spaces, sim-to-real transfer, learning from logged data, and layered safety architectures. This post is that 70%.

## Reward design — the actual core skill

A working RL controller is almost always the result of 5 to 20 reward iterations, not a clever algorithm choice. If there's one thing that separates a team that ships learned policies from one that doesn't, it's reward design discipline. Everyone knows this once they've been through it a few times. No paper spends enough time on it.

### What works

- **Dense shaped rewards** that decrease smoothly with task distance. For reaching: $r = -\|x_{\text{ee}} - x_{\text{target}}\|_2$ or a scaled exponential. For tracking: negative quadratic tracking error.
- **Additive penalty terms** for action magnitude, action rate, joint limits, jerk. Each with its own coefficient. Log them separately so you can see which one is dominating at any given time.
- **Sparse success bonus** layered on top of dense shaping. Ensures the policy prefers task completion even if the shaping has local optima.
- **Normalization** — keep each term roughly $\mathcal{O}(1)$. A single misbehaving term with magnitude 1000 will dominate and produce weird policies that optimize for the wrong thing.

### What ruins policies

- **Sparse-only reward** on a hard task. Agent never sees reward; policy never moves. Use hindsight experience replay (HER) or a curriculum.
- **Reward hacking opportunities.** If standing still gives slightly positive reward, locomotion policies learn to stand still. Before blaming the algorithm, check for local optima.
- **Unscaled terms** with wildly different magnitudes.
- **Large discontinuities** — reward cliffs create gradient chaos. Prefer smooth penalties.

> **The debugging loop.** When your policy learns something weird, the first question is never "is my algorithm wrong?" It's "is my reward specifying what I think it specifies?" Log every reward term separately. Visualize rollouts. Hand-craft a trajectory you believe is good and check its cumulative reward against the policy's. If the hand-crafted trajectory doesn't score higher than what the policy is doing, the reward function is the problem, not the algorithm.

## Observation and action space design

### Observations — what to include

- **Proprioception always.** Joint positions, joint velocities, end-effector pose and velocity. This is free information the controller already has.
- **Task-relevant state** — target pose, object pose, goal representation. If you're using vision, these come from perception; if you're in sim and can use ground truth (the "privileged information" setup), use it during training and distill into a vision-only student later.
- **History / frame stacking** if dynamics are non-Markov — contact, latency, unobserved states. Two to four frames is usually enough.
- **Phase or time features** if the task is cyclic or has a time budget.
- **Do not include** anything the policy shouldn't condition on — episode-specific IDs, randomization parameters (unless you want to condition on them, which is the asymmetric actor-critic pattern).

### Actions — scaling and parameterization

- **Normalize action bounds to $[-1, 1]$** before feeding to the environment. Always. Networks output values in this range, and an unscaled action space is the single most common "why isn't my agent learning" cause.
- **Target positions or velocities** with a low-level PD controller beats raw torque commands for most manipulators. The low-level controller handles transients; RL handles the setpoints.
- **Delta actions** — where $a_t = a_{t-1} + \Delta_\theta(s_t)$ — can stabilize learning and produce smoother rollouts, at the cost of adding previous action to your state.
- **Action smoothness regularizers** — add $\lambda \|a_t - a_{t-1}\|^2$ to the reward. Robots love this. Motors love this. Certification engineers love this.

## The sim-to-real gap

Almost all modern robotics RL is trained in simulation. The question is how to make the policy survive deployment. Four techniques, in order of increasing sophistication:

1. **System identification.** Measure your robot's actual parameters — masses, inertias, friction coefficients, actuator delays — and put them in the simulator. Don't skip this. A well-calibrated sim does half of the sim-to-real work by itself.
2. **Domain randomization.** Randomize dynamics parameters (mass, friction, damping, actuator noise) every episode during training. The policy learns a controller robust to a *distribution* of physics rather than being brittle to one specific set of parameters. Start with ±10% variation and widen until sim performance starts to degrade meaningfully — that's your headroom.
3. **Observation noise and latency.** Add Gaussian noise to observations. Drop or delay frames to match your real sensor pipeline. Policies trained without this assume perfect state estimation and fail instantly on real hardware, where everything is delayed, noisy, and occasionally missing.
4. **Asymmetric teacher-student.** Train a teacher policy with privileged information (ground-truth contact forces, true object state, full system state) that can't be observed in deployment, then distill into a student that uses only real-world-available observations. This is how ANYmal learned to traverse rough terrain, how OpenAI's Rubik's cube hand worked, and how most modern in-hand manipulation research proceeds. It's easily the most effective single technique in the sim-to-real toolkit.

> **Don't start with domain randomization.** Start with a well-calibrated sim and a dense reward. Only add randomization when your policy works in sim but fails the reality gap. Too much DR too early produces a policy that is conservatively bad at everything — it's optimized to work across a range so wide that it's exceptional at nothing.

## Offline RL and imitation learning

On a real robot, every interaction costs something: electricity, wear, a person standing by with an e-stop. If you already have demonstrations — teleoperation traces, scripted policies, data from an old controller — you want algorithms that learn from *fixed data* instead of demanding fresh rollouts. That's the offline-RL and imitation-learning regime. For robotics it's often the only economically viable regime.

### Imitation learning — supervised learning dressed as RL

If you have $(s_t, a_t)$ pairs from an expert, the simplest thing is to treat them as a supervised classification or regression problem.

**Behavioral Cloning (BC).** Fit $\pi_\theta(a \mid s)$ to maximize expert action likelihood. That's it. BC is the first thing you should try with demonstrations — it's embarrassingly simple and embarrassingly often works. Its failure mode is **compounding errors**: a small prediction error takes the agent slightly off-distribution; off-distribution states weren't in training; the next action is worse; divergence. The error growth is $\mathcal{O}(T^2)$ in rollout length $T$, which is why BC policies that look perfect in short rollouts fall apart after a few hundred real-robot steps.

**DAgger (Dataset Aggregation).** Run the current learner in the real environment. For every state it visits, query the expert for the correct action. Add those $(s, a_{\text{expert}})$ pairs to the dataset and retrain. DAgger (Ross et al., 2011) reduces the compounding-error rate from $\mathcal{O}(T^2)$ down to $\mathcal{O}(T)$ because the training distribution now covers states the learner actually reaches. The catch: DAgger needs an expert that can be queried online on arbitrary states. That's easy if the "expert" is an MPC controller you happen to want to distill into a fast neural policy — an extremely useful pattern for robotics. It's harder if the expert is a human.

**GAIL — Generative Adversarial Imitation Learning.** Treat imitation as a two-player game. A discriminator tries to tell apart expert transitions from learner transitions; the learner's reward is "fool the discriminator." Close cousin of inverse RL. Powerful but unstable (it inherits every issue GANs have) and sample-hungry. In practice, most production pipelines use BC plus fine-tuning rather than GAIL.

### Offline RL — reward labels, fixed data, no rollouts

Offline RL assumes you have a dataset of $(s, a, r, s')$ tuples from one or more behavior policies — possibly including low-quality ones — and no ability to collect more. The goal is to recover a policy that *outperforms* the data-generating policies, using only the reward signal.

The failure mode that defines the whole field: **distributional shift**. Vanilla off-policy methods (SAC, TD3, DQN) fail catastrophically when trained offline. The learned policy generalizes to out-of-distribution actions, the critic extrapolates optimistically on those OOD actions, and the actor happily exploits the fantasy. Every offline-RL method is, fundamentally, a technique for constraining this optimism.

**CQL — Conservative Q-Learning.** Add a regularizer to the critic loss that pushes Q-values *down* on actions not seen in the dataset and *up* on actions that are:

$$ \mathcal{L}_{\text{CQL}} \;=\; \mathcal{L}_{\text{TD}} \;+\; \alpha\!\left(\log\!\sum_a \exp Q(s,a) - \mathbb{E}_{(s,a) \sim \mathcal{D}}\!\bigl[Q(s,a)\bigr]\right) $$

The effect: learned Q-values are a lower bound on the true values for in-distribution actions, which is enough to prevent the actor from chasing hallucinations.

**IQL — Implicit Q-Learning.** Even simpler idea (Kostrikov et al., 2021): never evaluate the critic on out-of-distribution actions at all. Train a value function $V$ with an *expectile regression* loss that softly approximates the maximum over in-dataset actions, then use the advantage $A = Q - V$ as the weight in an advantage-weighted BC step. IQL avoids the whole "what does the critic think about unseen actions" question by construction, which is why it's often the strongest offline-RL baseline today.

**TD3+BC — the one-line offline fix.** Fujimoto and Gu (2021) showed that TD3 with a single additional term — a BC loss on the actor toward dataset actions — matches or beats far more complex offline methods on most benchmarks:

$$ \mathcal{L}_{\text{actor}} \;=\; -\lambda\, \mathbb{E}[Q(s, \pi(s))] \;+\; \mathbb{E}\!\bigl[(\pi(s) - a_{\text{data}})^2\bigr] $$

This is the pattern to know: if you have a working online off-policy method and need offline data, **add a BC term and a conservatism penalty**. The fancy methods are refinements of that one idea.

### The warm-start recipe that actually ships

In production robotics, the offline-plus-online pipeline that works:

1. Collect a modest dataset of human or scripted demonstrations.
2. Train a BC policy. Evaluate — sometimes you're done.
3. Deploy BC to seed a replay buffer, then run online off-policy RL (SAC or TD3) on top.
4. Mix BC loss into the RL objective at a decaying weight so you don't un-learn the demos too fast.
5. When compounding errors appear, log the failure states and re-query demonstrations there (DAgger-style).

> Ten minutes of decent demonstrations is worth several days of careful reward shaping. If you can get demos, get them *first*. Offline RL research isn't a substitute for a sensible data-collection strategy — it's a way to squeeze more out of the data you already have.

## Safe reinforcement learning

Safety in RL has two distinct meanings that are often conflated. **Safety during training** asks whether the learning process itself is allowed to violate constraints — can the robot hit the wall while it's figuring out not to? **Safety at deployment** asks whether the final policy is reliably within bounds. The methods for each are different, and choosing the wrong one is a common mistake.

### Constrained MDPs — the formal framing

Add one or more cost functions $C_i : \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ to an ordinary MDP and require their expected cumulative values stay below thresholds $d_i$:

$$ \max_\pi \;\; \mathbb{E}_\pi\!\left[\sum_t \gamma^t R(s_t, a_t)\right] \quad\text{s.t.}\quad \mathbb{E}_\pi\!\left[\sum_t \gamma^t C_i(s_t, a_t)\right] \leq d_i \;\; \forall i $$

This is a **Constrained MDP** (CMDP). For a motor-control drive, the framing writes itself: reward is torque-tracking accuracy, efficiency, and an NVH metric; cost 1 is expected time above a peak-current threshold; cost 2 is expected temperature excursion above an insulation limit; cost 3 is expected stator flux beyond demagnetization margin. Three hard things you'd never let a policy violate even once in production, but which are exactly the kind of constraints a CMDP formulation is designed to encode.

### Lagrangian methods — dualize the constraint

Introduce a Lagrange multiplier $\lambda_i \geq 0$ per constraint and solve the saddle-point problem:

$$ \mathcal{L}(\pi, \lambda) \;=\; J_R(\pi) - \sum_i \lambda_i \bigl(J_{C_i}(\pi) - d_i\bigr) $$

Alternate: maximize over $\pi$ using any RL algorithm on the effective reward $R - \sum_i \lambda_i C_i$; update each $\lambda_i$ by gradient ascent on the constraint violation. In practice this is remarkably effective — almost every strong "constrained" baseline is a Lagrangian SAC or Lagrangian PPO. The multipliers track the shadow prices of the constraints, which makes them interpretable. Failure modes: slow to converge if constraints are tight, and $\lambda$ can oscillate. Clipping $\lambda$ to $[0, \lambda_{\max}]$ and using a smaller learning rate on $\lambda$ than on the policy usually stabilizes it.

### CPO — Constrained Policy Optimization

CPO (Achiam et al., 2017) is a trust-region method for CMDPs. At each step, the policy update is constrained to a KL-ball (like TRPO), and the constraint inequality is linearized and included directly in the optimization. The effect is that *every iterate* satisfies the constraint, approximately, with high probability — not just the limit point. This matters when you can't afford training-time violations. CPO is more involved to implement than Lagrangian methods, and the approximation errors occasionally produce infeasible iterates requiring a recovery step. In practice, Lagrangian variants dominate research while CPO remains the honest theoretical reference.

### Shielding and Control Barrier Functions

The simplest form of safety: wrap the policy in a hand-coded or model-based filter that replaces unsafe actions with a known-safe alternative. Formally, you have a **safety specification** $\phi$ (a temporal-logic formula, a reachable-set computation, a barrier condition) and a **shield** $\sigma$ that projects $\pi(s)$ onto the set of actions compatible with $\phi$.

For discrete actions with a known-safe subset, this is a trivial mask on the action logits. For continuous actions, it becomes a QP that projects onto a polytope. Runtime shielding is how you get guaranteed safety at deployment — RL provides the policy, the shield provides the guarantee.

**Control Barrier Functions (CBFs)** are the continuous-time, differentiable cousin of shielding. A differentiable scalar $h(x) \geq 0$ defines the safe set. A control input $u$ is safe if it keeps the system inside that set for all future time — which reduces to a single scalar inequality enforceable via a QP:

$$ \dot h(x, u) + \alpha\bigl(h(x)\bigr) \geq 0 $$

For a control engineer, this is familiar territory. The RL integration pattern: let the policy output a *desired* action, then solve a QP to find the closest action that satisfies the CBF inequality. The policy learns in a modified environment where the shield has already prevented the worst. This is the safest known way to let RL loose on a real robot — the CBF-QP guarantees forward invariance while the policy does the learning. The caveat is that a CBF requires a differentiable model of the safety-relevant dynamics. For fast-dynamics motor control this is fine. For a humanoid on rubble, it's harder.

### Risk-sensitive RL

Standard RL optimizes *expected* return. Sometimes you care about the worst-case return — you're willing to give up a little mean performance to shrink the left tail.

- **CVaR optimization** — optimize the expected return conditional on being in the worst $\alpha\%$ of outcomes. Operationally: sort a batch of returns, drop everything above the $\alpha$-quantile, take the mean of the rest. Surprisingly effective.
- **Distributional RL** (C51, QR-DQN, IQN) — learn the full distribution of returns, not just the mean. You can then optimize any statistic of that distribution (mean, CVaR, median) for free. The distributional view also empirically improves mean performance, which is why it's one of Rainbow's seven components.
- **Robust MDPs** — optimize worst-case over a set of plausible transition models. Useful when you have uncertainty bounds on system parameters — think: robustness to variations in motor inductance or rotor inertia across a production run.

> **Motor-control tie-in.** In a PMSM or AFM drive, "safe RL" maps directly onto the existing safety architecture. Hard limits (current, flux, temperature) are CBF-style constraints, enforceable at runtime via an output-voltage saturation block that's *already* in the software. Soft limits (tracking error, NVH) become Lagrangian costs. The RL policy sits above the safety layer; nothing RL produces can bypass the hardware-backed current limit. This is the architecture that lets you use learning on safety-critical drive systems without rewriting the safety case.

### The rule that matters most

> **Do not rely on the policy to be safe. Make the environment safe.** A good safety architecture means that the worst a bug in the RL policy can do is waste time, not hardware. If a policy failure can damage a motor or a person, the policy is in the wrong architectural position — wrap it in a classical safety layer that doesn't itself depend on the learning outcome.

## Training infrastructure — what you need on day one

The last thing — the stuff you want set up *before* you start running experiments, not discovered painfully on week three:

- A vectorized environment wrapper for parallel envs — Gym/Gymnasium `VectorEnv`, Isaac Gym, Brax.
- Running observation normalization with persisted statistics (so you can resume training, and so evaluation uses training-time stats).
- TensorBoard or Weights & Biases logging of **every reward component separately**, not just the total.
- Deterministic evaluation rollouts (fixed seeds) run periodically and logged. Training return is noisy; eval return is what you trust.
- Checkpoints saved by best eval return, not just latest. Training can and will regress.
- Rollout videos auto-generated for eval. You will watch thousands of them. If you don't have them, you're debugging blind.
- Hyperparameter sweeping infrastructure — Optuna, W&B Sweeps. Even a tiny sweep beats manual tuning.

None of this is glamorous. All of it is the difference between a project that converges in two weeks and one that spins for two months on the same bug hiding in the reward function.

## Closing the series

That's the field guide. Seven posts, one hub, and roughly everything I'd want a motivated control engineer to know before starting their first RL project — and more importantly, before starting their second one, after the first one went the way first RL projects always go.

A few closing observations that compress the whole series into one page:

- **The MDP is the only hard object.** Everything else is strategy. Most RL failures trace back to a poorly-specified MDP — wrong state, wrong action space, wrong reward, wrong episode boundaries. The algorithm you chose is almost never the real problem.
- **Model-free is about wringing signal from samples. Model-based is about wringing samples from signal.** On fast simulators, you have all the samples you want, so model-free wins. On real hardware, every sample is expensive, so model-based wins. The question "which family do I reach for?" is almost completely answered by "how expensive is a rollout?"
- **SAC for expensive data, PPO for cheap data.** This single heuristic gets the algorithm choice right about 90% of the time. The other 10% is when you need a deterministic policy (TD3) or are doing sim-to-real distillation (teacher-student PPO).
- **The best RL practitioners are people who would happily ship a PID controller if it worked.** Reinforcement learning is a tool. It shines where modeling is hard, rewards are complex, or solutions are non-convex. In places where classical control already works, it usually still does. Use RL only where it adds something; measure everything against the simplest thing that could possibly work.

Thanks for reading. The interactive widgets, the math, the engineering folklore — they're all easier to internalize once. The hard part is remembering them the third time you sit down to train a policy, when it's two in the morning and the reward curve isn't moving and the temptation is to try something clever. At that point, the answer is almost never clever. It's usually to look at the reward components, watch a rollout video, and make sure the MDP is the one you thought it was.

---

← Back to [the field guide]({{ '/posts/rl-for-control-and-robotics-field-guide/' | relative_url }})
