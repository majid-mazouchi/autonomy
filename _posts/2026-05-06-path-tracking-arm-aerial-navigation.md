---
title: "Path Tracking, Arm and Aerial Navigation"
subtitle: "Now that the robot knows where it is, how does it actually get somewhere? A visual primer on the motion-control layer that sits between planning and the actuators."
date: 2026-05-06 12:00:00 -0400
category: "Robotics"
slug: path-tracking-arm-aerial-navigation
excerpt: "A visual primer on robot motion control — from path tracking on wheeled vehicles (pure pursuit, Stanley, MPC), through arm navigation (inverse kinematics, RRT-Connect), to aerial navigation (cascaded controllers, geometric tracking). Eight live demos."
reading_time: 6
---

The previous post in this neighborhood — [A Field Guide to Path Planning]({{ '/posts/path-planning-field-guide/' | relative_url }}) — covered how a robot decides *where* to go. This one picks up the next layer: given a path the planner produced, *how does the robot actually follow it?*

That's a different problem than people new to robotics often expect. A path is just a curve in space. Following it is a control problem. And it's a different control problem depending on what kind of robot you have — a wheeled vehicle has nonholonomic constraints, an arm has redundant degrees of freedom and joint limits, a quadcopter has six-DoF dynamics and underactuation. Each one gets its own family of techniques. This primer walks through all three side by side.

## What it covers

Seven sections, eight live demos, about thirty minutes to read.

**§1 — Three layers of robot motion.** The pyramid: planning (where), tracking (how), control (the actuator commands). Why each layer exists and where most engineering time actually goes.

**§2 — Path tracking** for wheeled vehicles. Four demos: pure pursuit (the classic, with its single tunable lookahead), the Stanley controller (the geometric improvement that won the DARPA Grand Challenge), kinematic MPC (the modern workhorse), and a side-by-side that shows why each one wins on different geometries.

**§3 — Arm navigation.** Two demos. The inverse kinematics question — given a desired end-effector pose, what joint angles get me there? — including the redundancy and singularity problems that make it harder than it looks. Then RRT-Connect: the sampling-based planner that turned arm motion planning from "academic" to "shipped on every modern manipulator."

**§4 — Aerial navigation.** Two demos. The cascaded controller architecture every drone runs (position → attitude → motor speeds, fast inner loop slow outer loop). Then geometric tracking on SE(3), the approach that handles aggressive maneuvers cleanly without singularities.

**§5–7 — Side by side, practical engineering notes, references.** Comparison across all three robot types. The engineering questions that actually decide algorithm choice in production. A short reading list of the papers and books worth knowing.

Every algorithm has a worked example, and the eight live demos let you drag goals, change parameters, and watch the controllers respond in real time.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/path-tracking-arm-aerial-navigation.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

The primer is a natural follow-on to the path planning field guide — same visual language, same level of technical depth, picking up exactly where the previous one left off.

---

← Back to [Autonomy]({{ '/' | relative_url }})
