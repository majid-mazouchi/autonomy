---
title: "Localization, Mapping, and SLAM"
subtitle: "Where am I? What's around me? And how do I figure out both at the same time? A visual primer on the three problems that sit underneath every map-aware robot."
date: 2026-05-06 14:00:00 -0400
category: "Robotics"
slug: localization-mapping-slam
excerpt: "A visual primer on the three localization-and-mapping problems every mobile robot has to solve — pure localization, pure mapping, and the joint estimation problem (SLAM). Eight live demos covering particle filters, occupancy grids, EKF/graph SLAM, and loop closure."
reading_time: 8
---

A robot moving through a space has to answer three questions to be useful. *Where am I?* *What's around me?* And — the hardest one — *how do I figure out both at the same time, with no map and no GPS?* Those three questions correspond to three different problems with three different algorithm families: localization, mapping, and SLAM (simultaneous localization and mapping).

It took the robotics community thirty years and a remarkable amount of math to figure out that SLAM is well-posed at all. The breakthrough was the realization that localization and mapping aren't independent — the *correlations* between landmarks are what makes the joint estimation tractable. From that observation came everything: EKF SLAM in the 1990s, particle-filter SLAM in the 2000s, graph SLAM in the 2010s, and the modern visual SLAM pipelines that ship in every consumer drone and AR headset.

This primer is a tour of all of it.

## What it covers

Eight chapters, eight live demos, about thirty minutes to read.

**§1 — Three questions, three problems.** The setup. Why localization, mapping, and SLAM are different problems with different tools, and the historical reason they weren't always understood as such.

**§2 — Localization** ("Where am I?"). Three demos: particle filters (Monte Carlo localization, the workhorse of every mobile robot), Kalman localization with known landmarks, and AMCL (the adaptive variant that ROS ships).

**§3 — Mapping** ("What's around me?"). Two demos: occupancy grids (the discrete-cell representation that defines mobile robotics), and feature-based maps with known sensor poses.

**§4 — SLAM** ("Both at once"). Three demos showing the three eras: EKF SLAM with its quadratic complexity, FastSLAM with particle-per-trajectory, and graph SLAM as the modern factor-graph formulation. The math gets serious here but the figures keep it tangible.

**§5 — Loop closure: the trick that saves SLAM.** Why drift accumulates, how recognizing a place you've been before lets you correct an entire trajectory at once, and the matching algorithms (bag-of-words, learned descriptors) that make it work in practice.

**§6 — Side by side.** Visual SLAM vs LiDAR SLAM vs visual-inertial. When each one wins. The hardware-and-environment matrix that decides what you should run.

**§7 — What a real SLAM stack looks like.** ORB-SLAM3, RTAB-Map, the open-source landscape, and the engineering reality behind the academic algorithms.

**§8 — References.** Reading list — the foundational papers and books worth knowing.

Every chapter has a live demo you can interact with — drag landmarks, move the robot, watch the filter respond.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/localization-mapping-slam.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

The primer is the natural follow-on to the [path planning]({{ '/posts/path-planning-field-guide/' | relative_url }}) and [path tracking]({{ '/posts/path-tracking-arm-aerial-navigation/' | relative_url }}) posts — those covered *deciding where to go* and *how to follow the path*; this one covers *how the robot knows where it is in the first place*. Together the three of them sketch the full perception-planning-control pipeline of a mobile robot.

---

← Back to [Autonomy]({{ '/' | relative_url }})
