---
title: "Ten Ideas Every Control Engineer Needs"
subtitle: "An illustrated monograph on feedforward, time delay, Padé, non-minimum phase, gain scheduling, the step response, the Nichols/Nyquist/Bode trio, notch filters, the gang of six, and passivity — paired with screencasts from Brian Douglas's Control Systems in Practice series."
date: 2026-04-26 12:00:00 -0400
category: "Control Systems"
slug: ten-ideas-control-engineer
excerpt: "Ten ideas that turn up almost every time a real controller meets a real plant — feedforward, time delay, Padé approximants, non-minimum phase, gain scheduling, the step response, Nichols/Nyquist/Bode, notch filters, the gang of six, and passivity. An illustrated companion to Brian Douglas's Control Systems in Practice screencasts."
reading_time: 4
---

I keep re-watching Brian Douglas's *Control Systems in Practice* MATLAB Tech Talks. They're an unusually clear sustained treatment of practical control theory — the kind of thing a working engineer actually needs alongside a textbook — and after enough rewatches it became clear I wanted a single place where the ideas could sit side by side with figures I could push around.

This monograph is that place. Ten chapters. Each pairs a chapter of plain-language explanation with a live interactive figure, then links out to its source screencast in a companion section at the end.

## What it covers

**Chapters 1–2 — The bridge to reality.** Feedforward control (when feedback alone isn't fast enough) and why time delay turns easy control problems into difficult ones.

**Chapters 3–4 — Working with delay and weird responses.** The Padé approximant as the algebraic fix that lets transfer-function tools cope with delays, and the non-minimum-phase systems that make controllers go the wrong way before they go the right way.

**Chapters 5–6 — When linear is not enough.** Gain scheduling for plants that change with operating point, and the step response as the single most informative experiment a working engineer ever runs.

**Chapter 7 — The three diagrams.** Nichols, Nyquist, and Bode as three views of the same loop — why each one earns its keep and when to reach for which.

**Chapter 8 — Notch filters, but understood.** Reframing the notch as a band-stop seen inside-out, and why that perspective matters when you're tuning around mechanical resonances.

**Chapters 9–10 — The deep theory that pays off.** The gang of six transfer functions you actually have to look at to know if a loop is robust, and passivity as the final stability guarantee that survives nonlinearity, uncertainty, and time-variation.

Each chapter has a live figure you can interact with, a short list of where the idea shows up, and notes from the field. The whole monograph takes roughly twenty minutes to read.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/ten-ideas-control-engineer.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with its own visual identity — a darker paper, an EB Garamond body, a small set of dedicated accent colors. It's intentionally designed as a standalone artifact, so this post is mostly a pointer. Hit the button above and enjoy.

---

← Back to [Autonomy]({{ '/' | relative_url }})
