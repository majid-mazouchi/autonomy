---
title: "A Field Guide to Path Planning"
subtitle: "From grids and graphs through sampling, smooth curves, and optimal trajectories — the principal algorithm families a robot uses to decide where to go."
date: 2026-04-28 12:00:00 -0400
category: "Robotics"
slug: path-planning-field-guide
excerpt: "How a robot, a car, or a vacuum cleaner decides where to go and which way to get there — the principal families of path planning algorithms, with interactive figures you can touch, drag, and watch in motion."
reading_time: 5
---

Path planning is the layer that sits between perception and control. Perception tells you where things are. Control tells you how to track a reference. Path planning is the question in between: *given the world, where exactly should the reference go?* It turns out that question splits cleanly into a handful of algorithm families that have stayed remarkably stable since the late 1960s, even as the field around them has changed completely.

This monograph walks through those families. It's structured the way I wish someone had explained them to me — concrete examples first, then the algorithm, then where it shows up in production today.

## What it covers

Ten chapters. Each pairs a plain-language explanation with a live figure you can interact with — drag obstacles, click new goals, watch the planner replan in real time.

**Chapters 1–2 — The setup.** What a path actually is (configuration space, the difference between a path and a trajectory) and a family tree of the algorithms that generate them.

**Chapters 3–5 — Discrete world.** Grid-based methods. Dijkstra and A* on graphs. Potential field methods (Khatib's classic and its failure modes). Two grid-based cousins worth knowing — D* Lite for incremental replanning and JPS for blazing-fast 2D.

**Chapter 6 — Sampling.** RRT, RRT*, PRM. The methods that actually scale to high-dimensional configuration spaces, and the asymptotic-optimality story that turns RRT into RRT*.

**Chapters 7–9 — Continuous.** Dynamic Window Approach for short-horizon obstacle-aware velocity selection. Smooth curves — splines, clothoids, Bézier — that turn discrete waypoints into something a vehicle can actually drive. Frenet-frame trajectory optimization, the workhorse of self-driving lane-keeping.

**Chapter 10 — Practical selection.** The decision tree for picking among them. When grids beat sampling, when sampling beats optimization, when the right answer is to compose two of them.

Each algorithm has a worked example. The whole monograph runs in your browser with no dependencies and takes about twenty-five minutes to read.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/path-planning-field-guide.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with its own visual identity — a warm cream paper, a vermilion-and-prussian-blue palette, a full set of dedicated SVG figures. It's intentionally designed as a standalone artifact, so this post is mostly a pointer. Hit the button above and enjoy.

---

← Back to [Autonomy]({{ '/' | relative_url }})
