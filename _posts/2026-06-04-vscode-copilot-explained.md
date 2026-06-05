---
title: "Coding with VS Code Copilot — The Complete Plain-English Guide"
subtitle: "Every confusing new word — instructions, prompts, skills, hooks, agents, modes, models — explained simply, with real examples you can copy and a reading list at the end."
date: 2026-06-04 10:00:00 -0400
category: "Tools"
slug: vscode-copilot-explained
excerpt: "VS Code Copilot has, over the past two years, quietly turned into the most-used AI development environment outside of dedicated tools like Cursor and Claude Code. It is also one of those products where the feature set has grown faster than the documentation can explain it — instructions, prompts, skills, hooks, agents, four chat modes, half a dozen models. This guide is the plain-English version: what each of the six building blocks actually is, when to reach for which, how to set it up in five steps, and what the gotchas are. With a complete starter kit you can copy into any new project."
reading_time: 24
---

There is a recurring pattern with mature developer tools: the feature set grows faster than the documentation, and a year later you find yourself reading official docs that describe every flag but never explain *which flags matter*. VS Code Copilot is, in 2026, firmly in that phase. Six building blocks (instructions, prompts, skills, hooks, agents, plus modes and models). Four ways to chat (ask, edits, agent, inline). Three context selectors (`#`, `@`, `/`). The official documentation is technically complete and operationally bewildering.

This guide is the plain-English fix. It is meant for the everyday developer — the one who has been writing code for years, who has used Copilot's basic autocomplete, and who now wants to understand the rest of the surface area without first reading a hundred-page manual. Every concept gets a one-paragraph definition, every feature gets a real file example, and the "which do I use when" question gets a flat decision table instead of a wall of prose.

This is the natural companion to [Matching the Claude App in VS Code]({{ '/posts/claude-in-vscode/' | relative_url }}). That post is about closing the perceived gap between the chat app and any IDE. This one zooms into the Copilot-specific surface area: the six features GitHub built into the editor and what to do with each.

## What it covers

Sixteen sections, about twenty-four minutes if you read straight through. Designed for one-section-at-a-time reference use.

**§ 01 — The big idea, in one breath.** Copilot is an AI helper that lives inside your code editor. On its own it's smart but forgetful. Every feature below is just a *way to teach it* — about your project, your rules, and your tools — so it stops guessing and starts helping properly.

**§ 02 — The 6 building blocks (with examples).** Instructions. Prompts. Skills. Hooks. Agents. Models. Each one defined in a paragraph, with a real file example next to it. The taxonomy that the rest of the guide hangs off.

**§ 03 — Which one do I use? (table).** The decision table. "I want Copilot to know my project conventions" → instructions. "I want to run the same multi-step task repeatedly" → prompt. "I want Copilot to know how to do a *thing* well" → skill. "I want to intercept tool calls" → hook. Etc.

**§ 04 — Hooks in depth.** The interception layer. When the agent is about to read a file / write a file / run a command, hooks can inspect and modify the call. Logging, secret-scrubbing, approval gates, and the dozen patterns the docs don't show.

**§ 05 — Skills in depth.** The progressive-disclosure pattern as it lives in Copilot specifically. The SKILL.md format. The trigger phrases that decide whether your skill ever gets used. The audit you should run.

**§ 06 — The 4 ways to chat.** Ask, Edits, Agent, Inline. Each one is best at a different task; using the wrong mode is the most common reason "Copilot feels weak today." Concrete examples of which mode is right for which question.

**§ 07 — Talking to it: # @ /.** The three context selectors. `#` for files. `@` for agents and participants. `/` for slash commands. The handful that you'll actually reach for daily.

**§ 08 — Where you actually work.** The surfaces. Editor inline. Side panel. Quick chat. Terminal. The matrix of where each mode is available and where they feel different.

**§ 09 — Which AI brain to pick.** The model picker. Claude 4.5 Sonnet, GPT-5, Gemini 2.5, the o-series, the smaller models. When to pick which. The cost-vs-quality knob.

**§ 10 — Setting it up (5 easy steps).** From zero to a properly configured workspace. Sign-in. Extension verification. Model selection. CLAUDE.md / `.github/copilot-instructions.md` setup. First sanity-check session.

**§ 11 — A complete starter kit.** A copy-paste-ready set of instructions, three sample prompts, two skills, and a recommended hooks file. Drop it into a new project and you have a sensible baseline.

**§ 12 — Compose, don't just organize.** The architectural argument. Most Copilot users treat instructions/prompts/skills as separate piles of text. The 10× users treat them as *composable units* — prompts that import skills, hooks that filter skill output, agents that orchestrate the whole thing. Worked example.

**§ 13 — Multi-agent orchestration.** The newest piece. Spawning sub-agents from inside a session. Parallelizing across files. The patterns that work and the ones that produce confused agents talking past each other.

**§ 14 — Shortcuts cheat-sheet.** The full keyboard table. The five worth memorizing on day one.

**§ 15 — Tricks & gotchas.** The hard-won observations. Permission denials that look like model failures. Stale instruction files. Context overflow. Forgetting that the IDE harness pre-includes files that the chat app does not.

**§ 16 — References & videos.** The relevant docs from GitHub and Microsoft. The community write-ups. The handful of YouTube channels that actually keep up with the feature releases.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/vscode-copilot-explained.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the guide →
  </a>
</div>

The guide lives at its own URL with a warm-paper editorial layout — terra-cotta accent, sixteen sections, code blocks throughout. Designed to be the document you keep open in a tab during your first month using Copilot seriously.

---

← Back to [Autonomy]({{ '/' | relative_url }})
