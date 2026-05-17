---
title: "Robotics, by Hand"
subtitle: "A working tour through the mathematics, mechanisms, and control loops that turn actuators into intent."
date: 2026-04-23 10:00:00 -0400
category: "Robotics"
slug: robotics-primer
excerpt: "An interactive primer on what a robot actually is — the geometry of reach, the closed-loop control underneath every motion, the sensing that lets it know what it's doing, and the terminology that quietly trips up everyone who doesn't have it memorized."
reading_time: 9
---

Robotics is one of those fields where the working terminology and the textbook terminology have drifted apart over decades. If you've ever sat in a meeting where someone said *workspace*, *reach*, *singularity*, and *Jacobian* in a single sentence, and you nodded along while making a mental note to look up half of it later — this primer is for you.

It's not a survey of robotics research. It's a working tour of the mathematics, mechanisms, and control loops that anyone reading robotics code has to internalize at some point. Concepts first, math second, demos throughout.

## What it covers

Seven chapters, all with live demos. About thirty-five minutes to read end to end.

**§1 — What is a robot?** The functional definition: a sensing-acting-deciding loop with a body. Why "robot" is such an unsatisfying word for the actual variety of things in the field.

**§2 — The geometry of reach.** Forward and inverse kinematics, the workspace, what singularities feel like, why a 6-DoF arm can reach more poses than a 7-DoF arm can reach *cleanly*.

**§3 — Closing the loop.** The control hierarchy from current loops upward. PID where it belongs, MPC where it earns its keep, and the cascade structure underneath every working robot.

**§4 — From where to how.** Planning vs control. Path vs trajectory. Why these distinctions are not pedantic.

**§5 — How robots see.** Sensors from encoders to LiDAR to cameras. The relative timescales (1 kHz, 30 Hz, 10 Hz) that drive almost every architectural decision.

**§6 — Terminology, tapped.** A glossary chapter, but with definitions explained rather than just stated. DoF, end-effector, payload, repeatability, holonomic vs nonholonomic.

**§7 — Things that bite.** The half-dozen ways a robotics project gets eaten by something that wasn't in the textbook. Singularity proximity. Sensor latency. The difference between simulated and real friction.

The demos let you drag joint angles, move targets, adjust gains, and watch the system respond.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/robotics-primer.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
