---
title: "Setting Up the Jetson Orin Nano Super — A Field Report"
subtitle: "A complete walkthrough of provisioning an NVIDIA Jetson Orin Nano Super from a fresh SD card to a working AI development platform — NVMe storage, GPU-aware Docker, real Firefox, and the gotchas nobody warns you about."
date: 2026-05-08 12:00:00 -0400
category: "Tools"
slug: jetson-orin-nano-setup
excerpt: "A field report from setting up an NVIDIA Jetson Orin Nano Super for AI development. NVMe migration, swap on a 1TB drive, GPU-aware Docker, MAXN power mode, and the small handful of mistakes that cost the most time."
reading_time: 12
---

I bought a Jetson Orin Nano Super to put a competent local GPU on my desk. Eight gigabytes of unified memory, sixty-seven TOPS, the size of a paperback novel. It runs CUDA, it runs containers, it runs everything I'd want for messing around with vision models and small embodied-AI experiments without renting time from a hyperscaler. The hardware delivers. The software setup, on the other hand, took me about three hours and at least four wrong turns.

This post is the field report. It's not the official NVIDIA guide and it's not a marketing piece — it's the path I'd take if I had to do it again, with the gotchas called out so you don't lose half a day to them like I did.

## What it covers

Twelve sections, ~3 hours of work, written for the engineer who wants the platform running quickly without skipping the parts that matter for stability later.

**Sections 1–3 — The kit and the boot.** What hardware I bought and why. The fresh-flash to JetPack 6.2.2. The first-boot dance.

**Sections 4–6 — Storage, the right way.** Why you should not run on the SD card past day one. NVMe partition layout, root migration, swap configuration on the 1TB drive. The exact sequence that worked.

**Sections 7–9 — The GPU stack.** Verifying CUDA. Installing the NVIDIA Container Toolkit so Docker can see the GPU. Running a real workload (PyTorch, container pull, smoke test).

**Sections 10–12 — The desktop layer.** Real Firefox (not the Snap version). The MAXN power mode that takes the board from 25W to 67W of GPU compute. The small fixes that take the platform from "works" to "comfortable."

Each section has the actual commands I ran, the errors I hit, and what fixed them. Five photographs of the kit and the case build are included. The whole guide takes roughly twelve minutes to read; following it end-to-end takes about three hours of patient hardware-and-terminal work.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/jetson-orin-nano-setup.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the guide →
  </a>
</div>

The guide lives at its own URL with a forest-green palette and a Field Notes framing. It's the third in the small Field Notes series alongside the [Linux for Beginners]({{ '/posts/linux-for-beginners/' | relative_url }}) primer.

---

← Back to [Autonomy]({{ '/' | relative_url }})
