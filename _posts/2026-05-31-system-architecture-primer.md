---
title: "System Architecture Design — A Practical Primer"
subtitle: "The decisions you make early, that are expensive to change later — and how to make them well."
date: 2026-05-31 10:00:00 -0400
category: "Tools"
slug: system-architecture-primer
excerpt: "Architecture decisions are the ones you make in the first week of a project and then live with for years. This primer is the working engineer's introduction — what architecture actually is, why it matters, the principles that guide good ones (separation of concerns, single responsibility, dependency direction), the quality attributes that matter in production, the standard styles (monolith, microservices, event-driven, layered, hexagonal), the cross-cutting concerns that haunt every system, and the documenting and process habits that prevent the next reorganization from being a re-architecture."
reading_time: 16
---

There is a tax to be paid on every software project, and the question is only when. Pay it early — argue about the architecture, write the design doc, draw the boundaries — and you ship a system that's reasonable to change later. Skip it, and you ship faster for three months and then spend the next two years paying it back with interest. Most engineers I know have lived through both versions. The primer below is what I wish someone had handed me on my first project that mattered.

It is deliberately not opinionated about a specific architectural style. The right architecture for a million-rps payment system is wrong for a desktop application, which is wrong for an embedded controller. What is universal is the *vocabulary* — quality attributes, separation of concerns, dependency direction, cross-cutting concerns — and a small set of habits (write the ADR, draw the diagram, name the trade-off explicitly) that produce good architectures regardless of style.

## What it covers

Ten sections, about sixteen minutes.

**§ 01 — What architecture actually is.** The structural decisions that are hard to change later. Component boundaries. Communication patterns. Data ownership. Why "the architecture" is not "the diagram" but the rules embedded in the diagram.

**§ 02 — Why it matters.** The cost curve. Cheap changes early, expensive changes late, and why a bad early architecture compounds. The few engineering practices (small services, clean dependency direction, explicit interfaces) that flatten the curve.

**§ 03 — Core design principles.** The shortlist that survives the latest fashion. Separation of concerns. Single responsibility. Dependency Inversion. Information hiding. The Law of Demeter. Each one explained with a concrete code example of the mistake it prevents.

**§ 04 — Quality attributes — the "-ilities".** The properties you should explicitly trade off when designing. Scalability, availability, maintainability, testability, observability, security, performance. The trick is that you can't have all of them; the architecture is the codification of which ones you chose to prioritize.

**§ 05 — Common architectural styles.** The standard taxonomy. Monolith. Microservices. Event-driven. Layered. Hexagonal / ports and adapters. Pipe-and-filter. When each one is the right choice and when it's a fashion-driven mistake.

**§ 06 — Cross-cutting concerns.** The things that show up in every component and never fit cleanly. Logging. Auth. Configuration. Caching. Error handling. The handful of techniques (middleware, interceptors, aspect-oriented programming) for handling them without scattering the logic across every module.

**§ 07 — Trade-offs & reality.** The honest discussion. There is no objectively best architecture; every architecture trades one quality attribute for another. The mature practice is naming the trade-off explicitly in a decision record, not pretending you found a free lunch.

**§ 08 — Documenting the design.** ADRs (Architecture Decision Records). C4 diagrams. The README-driven design that ages well. Why the document that captures *why* you made a decision is more valuable, six months later, than the document that captures *what* the decision was.

**§ 09 — A practical process.** The end-to-end workflow. Identify the quality attributes that matter. Sketch the components. Identify the cross-cutting concerns. Draw the dependency graph. Pressure-test against the top three failure modes. Write the ADRs.

**§ 10 — Common mistakes.** The patterns that consistently produce bad architectures. Premature distributed systems. Microservices without operational maturity. Ignoring data ownership boundaries. Cargo-culting hexagonal architecture into a CRUD app. Each one with the warning signs and the recovery path.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/system-architecture-primer.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

The primer lives at its own URL with a warm-paper editorial layout — burnt-sienna accent, JetBrains Mono section labels, ten sections.

---

← Back to [Autonomy]({{ '/' | relative_url }})
