---
title: "Matching the Claude App in VS Code"
subtitle: "Why the same model can feel sharper in the chat app than in your editor — and the handful of moves that close the gap."
date: 2026-05-31 16:00:00 -0400
category: "Tools"
slug: claude-in-vscode
excerpt: "You pick the same model in VS Code that you use in the Claude app, ask a similar question, and the editor's answer feels thinner. The usual conclusion — 'the IDE version must be a weaker model' — is almost always wrong. The difference is the harness around the model: what context it sees, what tools it has, and whether it gets to plan before it acts. This short field guide is the seven-section briefing on closing the gap."
reading_time: 7
---

A small but consistent experience among engineers I talk to: the same Claude model in VS Code feels noticeably less capable than the same model in the chat app. The natural conclusion — that the editor version is some weaker variant — is almost always wrong. The model is the same; the harness around the model is not. This short field guide is the briefing on what the harness actually controls, what the three levers are that you (the user) can move, and the keep-it-by-your-keyboard checklist that closes most of the gap.

The whole piece is intentionally short. It is the working version of a conversation I've ended up having about a dozen times.

## What it covers

Seven sections, about seven minutes.

**§ 01 — It's the harness, not the model.** What "the harness" means. The system prompt, the tools, the agentic loop, the context-window management. Why two interfaces that pick the same model can produce wildly different output.

**§ 02 — The three levers you control.** What you, as the user, can actually change. Model selection. Context curation. Tool / agentic-mode selection. Everything else is the vendor's responsibility.

**§ 03 — Lever one — really run the same model.** Check the model selector. Watch for the silent fallback. Don't compare a Claude 4.5 Sonnet answer in chat to a Claude 4 Haiku answer in VS Code and conclude the IDE is worse.

**§ 04 — Lever two — feed context on purpose.** The biggest lever, and the most ignored. The chat app sees only what you paste; the IDE harness sees your project, your file, your selection — and routes them in non-obvious ways. Knowing what got included is half the battle. The practical moves: pinning files, the `@` mentions, the explicit `#file` references, the difference between "what the IDE thinks is relevant" and "what you know is relevant."

**§ 05 — Lever three — use the agentic harness, not autocomplete.** The single biggest perceived-quality jump. Ask Claude to *plan, then act* — give it a task and let it call tools — instead of treating it like a sentence-completer. Why "edit this file" is a worse instruction than "figure out what this file does, propose a change, then apply it."

**§ 06 — The keep-it-by-your-keyboard checklist.** The seven-item card. Check model. Pin relevant files. Use the agent mode. Ask for a plan first. Read the diff before accepting. Provide feedback in-stream, not after the fact. Save the working prompts as reusable instructions.

**§ 07 — References & further reading.** The relevant docs from Anthropic, GitHub, and Cursor. The handful of write-ups that have changed my own practice.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/claude-in-vscode.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the briefing →
  </a>
</div>

The briefing lives at its own URL with a warm-paper editorial layout — red accent, dek-style intro, seven concise sections.

---

← Back to [Autonomy]({{ '/' | relative_url }})
