---
title: "Claude Code — The Ultimate Field Guide"
subtitle: "An agentic coding tool that reads your codebase, edits files, runs commands, and plugs into your dev environment. Twenty sections covering install through advanced automation — in plain words, with copy-ready examples."
date: 2026-06-01 17:00:00 -0400
category: "Tools"
slug: claude-code-field-guide
excerpt: "Claude Code is Anthropic's agentic coding tool — a CLI that reads your codebase, edits files, runs commands, and plugs into your dev environment. It is also one of those tools where the documentation tells you what every flag does without telling you which flags matter, and where the muscle memory takes a couple of weeks to build. This field guide is the working version: the install path, the everyday workflow, the slash and CLI commands you'll actually use, the CLAUDE.md memory mechanism, permissions, MCP integration, skills/hooks/agents, the keyboard shortcuts, the power moves, and the common gotchas — in twenty sections, with copy-ready examples throughout."
reading_time: 35
---

There is a phase in any new agentic tool where the documentation is technically complete and operationally useless. Every command is listed, every flag is described, every concept is defined — and you still don't know what the *workflow* looks like, which flags actually matter day-to-day, what the muscle memory is supposed to feel like after two weeks.

This field guide is the operational version. It draws on the official Anthropic documentation but organizes it around the questions you'll actually ask: how do I get this running, what does a normal session look like, when do I reach for `/clear` vs `/compact`, how do I make Claude Code remember project conventions across sessions, what's the difference between MCP and Skills, how do I run it inside a CI pipeline, what are the keyboard shortcuts I'll wish I knew on day one. Copy-ready examples throughout.

It is the natural companion to the [Matching the Claude App in VS Code]({{ '/posts/claude-in-vscode/' | relative_url }}) post — that one is about closing the perceived gap between the chat app and the IDE, this one is about getting good at the CLI variant specifically.

## What it covers

Twenty sections. About thirty-five minutes if you read straight through. Designed for one-section-at-a-time reference use.

**§ 01 — What it is.** Agentic coding in one paragraph. Why a CLI agent is a different beast from an autocomplete plugin or a chat interface. The Claude Code model selection logic.

**§ 02 — Install.** The minimal install path on macOS, Linux, and Windows (WSL). API key setup. The first-run sanity check.

**§ 03 — First session.** The five-minute orientation. Launching, asking your first question, watching Claude read your repo, your first edit, your first diff acceptance.

**§ 04 — How it thinks.** The agentic loop, plain-language. Plan → act → observe → re-plan. Why the answers are different from the chat app's answers even when the model is the same.

**§ 05 — Everyday workflow.** The session shape that experienced users converge on. When to use which command. The /clear vs /compact discipline. When to fork a new session.

**§ 06 — Slash commands.** The shortcuts inside the session. /help, /clear, /compact, /model, /init, /memory, /resume — what each one does and when you'd reach for it.

**§ 07 — CLI commands.** The command-line surface. `claude`, `claude -p`, the prompt-piping idioms, the headless mode for automation.

**§ 08 — CLI flags.** The flags that matter. Model selection (`--model`), permissions (`--allow-tools`), output format (`--output-format`), session control (`--continue`, `--resume`). With the warnings about each.

**§ 09 — CLAUDE.md memory.** The project-memory file that Claude Code reads on every session. What to put in it (conventions, dependencies, gotchas). What to leave out (anything secret, anything that changes per-developer). The discipline that makes the difference between a useful CLAUDE.md and one that just confuses the model.

**§ 10 — Permissions.** The trust model. The four permission tiers. When to grant which. The hooks that let you intercept tool calls before they execute.

**§ 11 — MCP & tools.** The Model Context Protocol. Connecting Claude Code to external services (databases, issue trackers, deployment systems). The relationship between MCP servers and built-in tools.

**§ 12 — Skills · hooks · agents.** The three customization mechanisms and what each one is for. *Skills* — markdown files that teach Claude how to do a specific task. *Hooks* — interception points in the tool-call loop. *Sub-agents* — spawning a separate agent context for a sub-task. With examples of each.

**§ 13 — Automation.** Running Claude Code non-interactively. The headless mode. Piping. The CI integration patterns. The cron-style scheduled runs.

**§ 14 — Work anywhere.** Terminal, IDE, desktop, browser. The matrix of where Claude Code runs and what feels different in each environment.

**§ 15 — Best practices.** The handful of habits that compound. Short focused prompts. Letting the agent plan before acting. Reviewing diffs before accepting. Treating CLAUDE.md as living documentation.

**§ 16 — Common gotchas.** The pitfalls that catch experienced developers. Tool-permission denials that look like model failures. Stale CLAUDE.md. Context exhaustion. Forgetting to /clear between unrelated tasks.

**§ 17 — Keyboard shortcuts.** The full table. The ones worth memorizing on day one (escape to interrupt, arrow keys for history, tab for completion).

**§ 18 — Power moves.** The advanced patterns. Parallel sub-agents. Multi-repo sessions. Custom prompt templates. The undocumented-but-stable techniques.

**§ 19 — Config & env tricks.** Environment variables. Config file locations. The settings worth tuning.

**§ 20 — References.** Links to the official Anthropic docs, the community resources, the related Claude products.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/claude-code-field-guide.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

The field guide lives at its own URL with a warm-paper editorial layout — rust accent, sticky top nav with a quick link to the official docs, twenty sections with copy-ready code examples throughout.

---

← Back to [Autonomy]({{ '/' | relative_url }})
