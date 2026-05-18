---
title: "Fault-Tolerant Control"
subtitle: "Now you've found the fault. The controller still has to fly the plane, run the line, or hold the road — what changes?"
date: 2026-04-15 10:00:00 -0400
category: "Control Systems"
slug: fault-tolerant-control
excerpt: "Monograph No. 2 of the diagnostics series. Passive vs active fault-tolerant control, reference governors, graceful degradation, and the stability question during the transition itself."
reading_time: 10
---

[FDI tells you something is wrong.]({{ '/posts/fault-detection-isolation/' | relative_url }}) Fault-Tolerant Control is what the controller does about it. The question splits cleanly into two philosophies — *passive* (design once to absorb a known class of faults without ever knowing one occurred) and *active* (detect the fault, then reconfigure). Almost every working system uses some mix of both.

This monograph is the second of a four-part series on diagnostics and fault-handling:

1. [**Fault Detection and Isolation**]({{ '/posts/fault-detection-isolation/' | relative_url }})
2. **Fault-Tolerant Control** (this post)
3. [**Prognostics and Health Management**]({{ '/posts/prognostics-health-management/' | relative_url }})
4. [**Frontiers in Diagnostics**]({{ '/posts/frontiers-in-diagnostics/' | relative_url }})

## What it covers

Six chapters plus references. About thirty-five minutes to read.

**§1 — The response after the diagnosis.** Why fault-tolerance is a control problem in its own right, not just a downstream consequence of detection.

**§2 — Passive FTC.** Designed to absorb. Robust controllers, sliding modes, designed-in redundancy. The "set it and forget it" approach that ships in mass-produced systems where intelligent reconfiguration would be too expensive.

**§3 — Active FTC.** Detect, then reconfigure. The harder problem; the more powerful approach. Control allocation, online identification, reference model adaptation.

**§4 — The reference governor.** A clever trick — reshape what the *controller is asked to do* in response to the fault, rather than reshape the controller itself. Often simpler and more reliable.

**§5 — Graceful degradation.** The practical face of FTC. What ships in real automotive, aerospace, and industrial systems. Limp-home modes. Emergency stops with style.

**§6 — Stability and performance during the transition.** The hardest question. The plant is changing, the controller is reconfiguring, and you have to guarantee stability the whole time.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/fault-tolerant-control.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open Monograph No. 2 →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
