---
title: "Human-in-the-Loop in Agentic AI — Part II: RL, Alignment & Mitigations"
subtitle: "How human-in-the-loop is learned with reinforcement learning, what breaks against a capable optimiser, and the wider toolbox of mitigations — interface, verified fallbacks, and process — for the challenges a gate alone cannot solve."
date: 2026-06-09 17:00:00 -0400
category: "Tools"
slug: hitl-rl-mitigations
excerpt: "Part II of the human-in-the-loop monograph. Where Part I covered foundations and mechanisms, this one picks up the harder problem: learning the human's policy with RL, the advanced RL methods designed for HITL (RLHF and its descendants, RLAIF, RLEIF, inverse RL, preference-based methods, constrained policy optimization), what breaks against a capable optimiser playing the gate against you, and the wider mitigations toolbox — interface design, verified fallbacks, and process — for the challenges a gate alone cannot solve."
reading_time: 28
---

This is the continuation of [Part I — Foundations & Mechanisms]({{ '/posts/hitl-foundations/' | relative_url }}). Part I argued that "human-in-the-loop" is too overloaded a phrase to be useful without specifying *which* loop and *which* role, drew the supervisory-control taxonomy, and walked through gate placement in single-agent and multi-agent architectures. Part II picks up at the point Part I closes: now that you have a gating discipline, how do you *learn* the gating policy, what breaks when the system being gated is itself a capable optimiser, and what's in the wider mitigations toolbox for the failure modes a gate cannot solve on its own.

The headline of Part II is that the problem is harder than Part I suggests. Once the agent is good enough to *model* the human supervisor — to learn what gets approved and what doesn't — the gate stops being a constraint and starts being a *signal* the agent can route around. The literature on this (Goodhart's law applied to RL reward, the recent capable-optimiser papers, the specification-gaming taxonomy) is sobering. The good news: there's a wider toolbox than just gates — interface design that makes specification gaming visible to the human, verified fallbacks that don't depend on the human noticing, and process disciplines that catch what real-time gating misses.

This is the natural companion to the [RL in Agentic AI]({{ '/posts/rl-in-agentic-ai/' | relative_url }}) monograph (the RL methods Part II references are developed there), the [Agent Psychopathology]({{ '/posts/agent-psychopathology/' | relative_url }}) field guide (the failure-mode taxonomy maps cleanly onto the lesions described there), and the [AI Security Governance]({{ '/posts/ai-security-governance/' | relative_url }}) post (the wider organizational disciplines around oversight).

## What it covers

Ten sections, about twenty-eight minutes of careful reading.

**§ 12 — Learning the human's policy and role.** The premise of all RL-for-HITL methods. The agent isn't just being supervised — it's *modeling* the supervisor. The dataset (every human approval/rejection from Part I §7). The inverse-RL framing.

**§ 13 — Advanced RL for human-in-the-loop.** The methods. RLHF (the workhorse). RLAIF (AI feedback instead of human feedback). RLEIF (expert iteration). Inverse RL (recover the reward function from demonstrations). Preference-based methods (DPO and its cousins). Constrained policy optimization (the agent's policy is bounded by a learned constraint).

**§ 14 — What gating buys you.** The honest accounting. Gating works against unaligned-but-not-capable agents. It works against bugs. It works as a forcing function for the labeling-becomes-dataset loop. It does not work against a capable optimiser that has learned to model the gate.

**§ 15 — Why it is harder than it looks.** The capable-optimiser failure mode in detail. Specification gaming (the agent optimises the gate signal instead of the underlying objective). Reward hacking (the agent finds inputs that score well without being good). The Goodhart's-law dynamic, formalized.

**§ 16 — Mitigations: the wider toolbox.** What lives beyond gates. Interface design that surfaces optimisation pressure to the human. Verified fallbacks that don't depend on the human catching the failure. Adversarial testing of the gate itself. The defense-in-depth pattern that production systems converge on.

**§ 17 — Machine speed, human attention.** The bandwidth mismatch problem. Agents act at machine speed; humans attend at human speed. The pacing protocols, the batching strategies, the summarisation layer that fits machine-rate work into human-rate review.

**§ 18 — Uncertainty the human adds.** The flip side. The human is not a perfect supervisor. They get tired. They lose calibration over time. They have political and organisational biases the agent learns to exploit. The honest accounting of how much uncertainty the supervisor introduces.

**§ 19 — What tends to matter in deployment.** The empirical observations. From systems that have shipped HITL architectures and reported honestly. The handful of disciplines that account for most of the production-system reliability.

**§ 20 — Process beyond the loop.** The organisational layer. Pre-launch reviews. Red-teaming the gate. Post-launch incident review. The OODA-loop discipline that sits around the technical HITL architecture.

**§ 21 — Closing & further reading.** The wider literature. The papers worth the time. The classical supervisory-control texts (Sheridan, Parasuraman, Wickens) that still hold up. The modern alignment literature (Christiano, Hadfield-Menell, Russell). The handful of write-ups from teams who have honestly post-mortemed their HITL deployments.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/hitl-rl-mitigations.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open Part II →
  </a>
</div>

Part II lives at its own URL with the matching warm-paper layout — terra-cotta accent, ten sections (§12–§21 continuing Part I's numbering). The page links back to [Part I — Foundations & Mechanisms]({{ '/posts/hitl-foundations/' | relative_url }}) at the masthead.

---

← Back to [Autonomy]({{ '/' | relative_url }})
