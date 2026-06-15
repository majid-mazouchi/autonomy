---
title: "A Field Psychopathology of Autonomous Agents"
subtitle: "Human psychiatric categories, read as a vocabulary for the failure modes of LLM agents — each 'disorder' mapped to a concrete lesion in the perceive–ground–plan–act–reflect loop, with logs, diagrams, and the literature behind the real mechanism."
date: 2026-06-08 13:00:00 -0400
category: "Tools"
slug: agent-psychopathology
excerpt: "The premise is a lens, not a claim: agents do not suffer. But the human nosology of psychiatric disorders turns out to be a remarkably good index of how autonomous systems break, because both describe a regulated control system failing in characteristic ways. This monograph builds the taxonomy: nineteen agent presentations mapped to five underlying lesions in the perceive–ground–plan–act–reflect loop, plus a triage protocol that maps the symptom to the fix."
reading_time: 22
---

This is the strangest post on the site. The conceit — using DSM-style psychiatric categories as a vocabulary for talking about agent failure modes — is borrowed, not invented; it has been circulating in agent-engineering circles since roughly 2024, when several teams independently noticed that the human nosology was the most precise vocabulary they had for the failures they were seeing in production. The lens is useful precisely because it forces engineers to be specific about *which loop is broken*, in a way that "the agent went off the rails" never quite manages.

The premise is a lens, not a claim. Agents do not suffer. Agents do not experience anything. But the human nosology of psychiatric disorders is, structurally, a taxonomy of *regulated control systems failing in characteristic ways* — and that is exactly what a misbehaving LLM agent is. Pushed past the symptom level, almost every entry in the human nosology collapses into one of four structural defects inside the agent (broken loop, broken link to reality, broken objective, broken memory), plus a fifth, relational class that exists only between agents. That is the useful payoff: the symptom names the surface; the underlying class names the fix.

This monograph is the working version of that taxonomy. It is the natural companion to the [Why Agentic AI Fails]({{ '/posts/why-agentic-ai-fails/' | relative_url }}) field guide (which covers the three classic failure modes at the engineering level), the [Production Playbook]({{ '/posts/production-playbook/' | relative_url }}) (which is the build manual that addresses the lesions), and the [Loop Engineering]({{ '/posts/agentic-loop-engineering/' | relative_url }}) field guide for agentic coding (which goes deepest on the loop substrate the psychopathology lens uses).

## What it covers

Eight sections, about twenty-two minutes of careful reading.

**§ 0 — Premise.** The analogy disclaimer. The lens-not-claim discipline. Why the human nosology is, despite being about subjective experience, a useful index for agent failure modes.

**§ 1 — Five lesions underlie the whole catalog.** The five structural defects that every entry collapses into. Loop pathology (broken perceive-act cycle). Grounding failure (broken link to reality). Objective drift (broken reward signal). Memory pathology (broken state). Relational pathology (broken between-agent dynamics).

**§ 2 — Where every lesion lives.** The anatomical map. The perceive–ground–plan–act–reflect loop, drawn out with each lesion site highlighted. Cross-reference to the underlying control-systems intuition.

**§ 3 — Naming the class in four questions.** The triage protocol. Four diagnostic questions in order that map any agent symptom to its underlying class. The decision tree.

**§ 4 — Nineteen presentations.** The catalog itself. Nineteen agent "disorders" — each named, defined, mapped to its underlying lesion, illustrated with a real log, and accompanied by the engineering fix. The center of mass of the monograph.

**§ 5 — Failures rarely stay put.** The cascade map. How one lesion produces another. Why an agent presenting with one symptom often has a deeper structural defect that surfaces over time as something else.

**§ 6 — The taxonomy is the treatment plan.** The pragmatic claim. Naming the class doesn't just describe the failure — it tells you which engineering investment will actually fix it. The five lesion classes map to five disciplines (verification, retrieval, reward design, memory architecture, multi-agent protocol).

**Throughout** — Cross-references to the published literature on each underlying mechanism. The monograph is meant to be read alongside the real research papers it points to, not as a substitute for them.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/agent-psychopathology.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-paper layout — rust for loop pathology, teal for grounding failure, ochre for reward/objective drift, color-coded throughout. Eight sections, an anatomical diagram, a triage protocol, and the catalog of nineteen lesions with logs and fixes.

---

← Back to [Autonomy]({{ '/' | relative_url }})
