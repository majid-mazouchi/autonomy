---
title: "Logic and Reasoning, Part II — Limits, Machines, and Problem-Solving"
subtitle: "The computational ceiling on reasoning, what it means to formalize the process, and how a machine actually solves a problem."
date: 2026-06-14 18:00:00 -0400
category: "Tools"
slug: logic-and-reasoning-part-2
excerpt: "Part 2 of 7. Part I covered how a human mind reasons. Part II asks the harder question: how much reasoning is *computable* at all? Gödel, Turing, the halting problem, complexity theory. Then how a machine actually does problem-solving in practice — search trees, heuristics, planning. The bridge from the foundations of Part I to the multi-agent systems of Part III."
reading_time: 28
---

This is Part 2 of the seven-part Logic and Reasoning field guide. Part I covered the foundations of how a *human* mind reasons. Part II asks the harder question — how much reasoning can be *formalised*, what are the theoretical limits, and how does a *machine* actually solve a problem in practice. The series is designed to be read in order; if you arrived here directly, [Part I]({{ '/posts/logic-and-reasoning-part-1/' | relative_url }}) is the right place to start.

The intellectual arc of Part II is one of the more striking in twentieth-century thought. The Hilbert program of the 1920s held that mathematics could, in principle, be fully formalised — every truth derivable mechanically from a set of axioms. The 1930s killed it. Gödel's incompleteness theorems showed any sufficiently rich formal system has true statements it cannot prove. Turing's halting problem showed there's no general procedure to decide whether an arbitrary program will finish. Complexity theory, decades later, added that even decidable problems can be intractable in practice. Knowing these limits is not pedantry — it is the foundation that prevents engineering ambitions from breaking on impossibility theorems.

The post then pivots from the limits to the *practice*: how a machine actually solves a problem given that perfection isn't on the menu. Search trees. Heuristics. Planning. The patterns that make problem-solving tractable even when the search space is astronomical.

## What it covers

About twenty-eight minutes of careful reading.

**The limits of formal reasoning.** Gödel's incompleteness theorems (with a plain-English reconstruction of the diagonal argument). Turing's halting problem. The Church-Turing thesis. What these results actually mean for engineering practice.

**Complexity theory.** P, NP, NP-complete, NP-hard. The Cook-Levin theorem in plain language. The handful of complexity classes worth knowing and the dozen that aren't.

**Problem-solving as search.** State spaces, operators, goal tests. The basic search algorithms (BFS, DFS, iterative deepening). The blind-search baseline.

**Heuristic search.** A\* and its descendants. The admissibility-and-consistency conditions that make A\* optimal. The pattern-database technique that produces strong heuristics from problem structure.

**Planning.** STRIPS. PDDL. The hierarchical-task-network alternative. Modern planners and what they can actually solve.

**Constraint satisfaction.** CSPs, backtracking, arc consistency, the constraint-propagation discipline. Why this framing turns intractable problems tractable.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/logic-and-reasoning-part-2.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open Part II →
  </a>
</div>

## The series

This is Part 2 of 7:

1. [The Foundations and the Human Mind]({{ '/posts/logic-and-reasoning-part-1/' | relative_url }})
2. **Limits, Machines, and Problem-Solving** — *(this post)*
3. [A Multi-Agent Problem-Solver]({{ '/posts/logic-and-reasoning-part-3/' | relative_url }})
4. [From a Mind to a Society of Minds]({{ '/posts/logic-and-reasoning-part-4/' | relative_url }})
5. [The Health of a Thinking System]({{ '/posts/logic-and-reasoning-part-5/' | relative_url }})
6. [The Dynamics of Thinking]({{ '/posts/logic-and-reasoning-part-6/' | relative_url }})
7. [Understanding and Comprehension]({{ '/posts/logic-and-reasoning-part-7/' | relative_url }})

---

← Back to [Autonomy]({{ '/' | relative_url }})
