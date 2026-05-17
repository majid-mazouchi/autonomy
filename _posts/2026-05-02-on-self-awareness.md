---
title: "On Self-Awareness — From Mind to Machine"
subtitle: "What self-awareness is, the levels and types psychologists describe, and how engineers are now teaching robots to begin doing the same thing."
date: 2026-05-02 10:00:00 -0400
category: "Robotics"
slug: on-self-awareness
excerpt: "A primer on self-awareness — the quiet but startling fact that you know there is a you — and how the question is being taken up by roboticists trying to give machines a self-model good enough to recognize themselves in a mirror."
reading_time: 11
---

Self-awareness is the quiet but startling fact that *you* know there is a *you*. It's the property that lets you predict how your body will feel if you reach for a cup, distinguish between your own movement and the world's, and recognize yourself in a mirror as something different from another person on the other side of the glass.

For most of the history of cognitive science, this was a question for psychologists and philosophers. In the last fifteen years it has also become a question for roboticists — because to do anything useful in an unstructured environment, a robot needs a working model of itself. Where its joints are. What it can reach. What's going to happen if it tries to pick something up.

This primer connects the two threads. It's structured as a tour from the psychology of the self (what we know about how human and animal self-awareness develops and is tested) to the engineering of self-modeling (what it looks like to give a machine the same capability, and how far researchers have actually gotten).

## What it covers

Nine sections, about thirty minutes to read. It's a different kind of writing than most of Autonomy — more reflective, less code-heavy — but the second half is genuinely technical and connects to the same robotics tradition the other posts cover.

**§I — Foundations.** What self-awareness is. The clean definition and the messy boundary cases. Why "knowing you exist" is harder to operationalize than it sounds.

**§II — Development.** The five levels of self-awareness from newborn to child. How they're measured. What's missing in autism, lost in some forms of dementia, present in some animals.

**§III — Types.** Public self-awareness (how you appear to others) vs private (your internal sense of self). Both matter for psychology; only one matters for most robotics.

**§IV — Method.** The mirror test. What it actually tests, what it doesn't, the species that pass it (great apes, dolphins, magpies) and the species that don't.

**§V — The Machine Turn.** Why robotics started caring about self-models in the 2000s. The connection to control theory: a good controller already needs a model of the plant; a good *autonomous* controller needs to learn that model.

**§VI — Self-Modeling.** The Lipson group's 2006 robot that learned its own morphology from random motor babble. Why this is one of the field's most underrated results.

**§VII — The Robot Mirror Test.** The 2020 Columbia experiment that gave a robot a "self" by training it to predict its own motion. Whether what it acquired counts as self-awareness — and why the answer depends entirely on how you defined the question in §I.

**§VIII — Other Aspects.** Body schema. Predictive processing. The social self. The mathematical structures that show up when you try to formalize any of these.

**§IX — Open Questions.** What's still genuinely unsolved.

Plus a references chapter — the foundational papers and books worth reading.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/on-self-awareness.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

---

← Back to [Autonomy]({{ '/' | relative_url }})
