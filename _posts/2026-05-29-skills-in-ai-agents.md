---
title: "Skills in AI Agents — A Practical Monograph"
subtitle: "A short, illustrated tour of the folder that taught your agent a new trick — its anatomy, its loading rules, and the design choices that decide whether it ever gets used."
date: 2026-05-29 10:00:00 -0400
category: "Tools"
slug: skills-in-ai-agents
excerpt: "A 'skill' is the most underrated primitive in agent design: a folder of files — a SKILL.md, some examples, maybe a script — that tells the agent how to do one thing well. The folder is unspectacular; the design choices behind it are where AI agents either get good at a task or fail at it. This monograph is the working tour: anatomy, progressive disclosure, the description-trigger problem, how the agent loop actually picks which skill to invoke, the audit you should run, and the skill-vs-tool-vs-MCP boundary that confuses everyone."
reading_time: 14
---

There is a particular kind of folder that has quietly become one of the most important primitives in agent design: a directory with a `SKILL.md` at the root, maybe a few example files, occasionally a script or two. Anthropic ships them with Claude Code, OpenAI's Agents SDK has its own version, and any agent framework worth using is converging on something equivalent. The pattern is simple. The design choices behind it are where AI agents either get good at a task or fail at it.

This monograph is the working tour. The anatomy of a skill — what files matter, what order they're read in, what the model actually sees. *Progressive disclosure* — the technique that lets a single skill grow from a 50-token preview to a 5,000-token deep dive without exploding the context window. The description-trigger problem: how to write the `description` field in the front-matter so the agent actually invokes the skill when it should, and doesn't when it shouldn't. The audit you should run against every skill in your repo. And the conceptual boundary — skill versus tool versus MCP server — that confuses almost everyone the first time they encounter it.

## What it covers

Eleven sections plus a worked example, about fourteen minutes.

**§ I — The idea, in one page.** What a skill is. The folder pattern. Why this approach won over alternatives (function-only tools, monolithic system prompts, RAG-only approaches).

**§ II — Anatomy of a skill.** The required files. `SKILL.md` front-matter and body. Example files. Scripts. Reference materials. What the loader actually reads when.

**§ III — Progressive disclosure.** The technique that makes skills scale. The model sees the description first (cheap, maybe 30 tokens). If the skill is relevant, it loads the SKILL.md body (a few hundred tokens). If it needs more, it follows the in-skill references to deeper documents. The token economy that lets you have a hundred skills loaded at once.

**§ IV — Skills in the wider agent loop.** Where the skill sits in the agent's run. The system prompt, the available-skills list, the trigger phase, the load phase, the act phase.

**§ V — How an agent picks a skill.** The selection logic. Description match. Required-files match. The model's own preferences. The failure modes (selecting the wrong skill, selecting no skill, selecting a skill but then ignoring it).

**§ VI — Writing a description that triggers.** The single most important skill-design decision. The eight characteristics of a description that gets invoked at the right time: specific triggers, negative cases, illustrative phrases, etc. With examples of good and bad descriptions side by side.

**§ VII — The skill audit.** The end-to-end test you should run against your skill library. Spot-check the descriptions. Test that the trigger phrases actually trigger. Test that off-topic queries don't trigger. Measure load latency. Find the duplicates.

**§ VIII — Skills vs. tools vs. MCP.** The boundary that confuses everyone. A *tool* is a function the model can call. A *skill* is a folder of instructions and examples. An *MCP server* is a tool provider that runs out-of-process. They are complementary, not interchangeable, and most agents need all three.

**§ IX — A worked example: the PDF skill.** Step by step. How a skill that fills a PDF form is structured. The SKILL.md content. The example PDFs and corresponding outputs. The Python script that does the fill operation. Why each file exists.

**§ X — Build your first skill, by hand.** The minimum viable skill, end to end. A `SKILL.md` with the right description, one example, a clear instruction. The fifteen-minute version that gets you past the first hurdle.

**§ XI — Skill composition.** The harder question. Can skills call other skills? When should they? The architectural patterns that work (skill-as-router, skill-as-library) and the ones that don't (deep skill nesting).

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/skills-in-ai-agents.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-paper editorial layout — burgundy accent, eleven illustrated sections, six interactive figures.

---

← Back to [Autonomy]({{ '/' | relative_url }})
