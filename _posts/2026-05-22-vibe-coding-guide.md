---
title: "The Art of Vibe Coding — A Practitioner's Compendium"
subtitle: "A four-book, forty-two-chapter field manual for building software in collaboration with AI — methodically, securely, and with taste. Plus six reference appendices."
date: 2026-05-22 10:00:00 -0400
category: "Tools"
slug: vibe-coding-guide
excerpt: "AI-assisted coding has changed the daily practice of engineering in ways the older how-to books haven't caught up with. This compendium is the long version of what I've learned trying to do it well — how to think about it, what tools matter, how to plan, prompt, context-manage, debug, test, and ship in collaboration with a model — and which parts of engineering it does not (yet) change. Four books, forty-two chapters, six appendices."
reading_time: 90
---

The shift from writing code yourself to writing code in collaboration with a language model is, for most of us, the largest change in daily engineering practice since the move from desktops to web. The textbooks that taught us how to engineer well — *The Pragmatic Programmer*, *Code Complete*, *A Philosophy of Software Design* — are mostly still right, but they were written for a world where the engineer did all of the typing. The new question is what to do when *most* of the typing is no longer done by you. How do you remain responsible for code you did not directly write? How do you preserve taste, judgment, and clarity in a workflow that is constantly tempting you to accept whatever the model produces and move on? What does "good engineering" even look like in this environment?

This compendium is my attempt to write down what I've learned. It is opinionated, long, and explicitly *not* a hot take on AI coding tools — I've tried to focus on practices, principles, and habits that I expect to outlast any specific tool. The four books move from the foundational practices (how to plan, prompt, manage context, debug) through the engineering disciplines (architecture, observability, performance, dependencies, CI/CD) into the specialized topics (auth, compliance, accessibility, embedded) and finally into the human side (hiring, mentorship, ethics, teams). Six reference appendices follow.

A note on the title: "vibe coding" started as a slightly dismissive term for the new mode of working — vibes-first, intent-driven, model-collaborative. I have come around to embracing it. The good practitioners I know really do navigate this way: by feel, with taste, with a clear sense of what they're trying to build, letting the model handle the typing and reserving their judgment for the choices that matter. The compendium is structured around making that practice durable.

## What it covers

Four books, forty-two chapters, six appendices. It is a long read — about ninety minutes cover to cover — but it is built to be reached for one chapter at a time over months.

**Book the First — Foundations.** Twelve chapters covering the daily practice. What vibe coding is and isn't. The mindset shifts that make it work. The instruments (editor, CLI, browser, version control, sandboxes). Planning before coding. Tech stack choices and coding standards. Security best practices that the model will not enforce for you. The art of prompting. Managing context. Debugging with AI. Mastering version control. Testing as a practice. Putting it all together as a daily workflow.

**Book the Second — Engineering Disciplines.** Twelve chapters on the disciplines that don't change just because the model is helping. Architecture and system design. Reviewing AI-generated code. Documentation as infrastructure. Error handling and resilience. Observability. Performance and profiling. Dependencies and supply chain. Data, schemas, and migrations. CI/CD and automation. Release engineering. Working with legacy code. Team collaboration in the AI era. The long life of software.

**Book the Third — Specialized Topics.** Twelve chapters on the corners of practice where the model needs more careful supervision. AI tool orchestration. API and contract design. Authentication and authorization. Compliance, privacy, and regulated software. Provenance, licensing, and IP. Accessibility and internationalization. Specialized domains — ML, data, embedded. Building your own tools and skills. The limits of vibe coding — the things it cannot do well, and the engineering still done by humans.

**Book the Fourth — The Human Side.** Six chapters on the parts of engineering that are about other people. Hiring and interviewing in the AI era. Onboarding and mentorship. The junior engineer's path. Working with non-engineers. AI ethics and responsibility. A personal practice — how to stay good at the craft over a long career.

**Six appendices** at the end: a glossary, a checklist for production-readiness, a prompt-engineering cookbook, a daily-practice cadence, a curated reading list, and an honest "where I disagree with the popular advice" essay.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/vibe-coding-guide.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the compendium →
  </a>
</div>

The compendium lives at its own URL with a Crimson Pro / Cormorant Garamond editorial layout — old-magazine masthead, oxblood and ochre accents, generous typography, careful spacing. It is best read at desktop width. The reading list at the end is its own small bibliography.

---

← Back to [Autonomy]({{ '/' | relative_url }})
