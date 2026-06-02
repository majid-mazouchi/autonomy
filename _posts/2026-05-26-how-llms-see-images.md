---
title: "How LLMs See an Image — A Visual Field Guide"
subtitle: "Language models never read your pixels. Before a single word is predicted, a picture is quietly turned into tokens — little vectors that sit shoulder to shoulder with text. Here's how that happens, in plain language, with things you can poke."
date: 2026-05-26 10:00:00 -0400
category: "Tools"
slug: how-llms-see-images
excerpt: "There is no version of GPT-4o, Claude, or Gemini that 'looks at' an image the way you do. The model is a transformer; it reads tokens. So every image you upload is quietly turned, before the model gets to it, into a sequence of token-shaped vectors that the language model can attend to alongside text. This field guide walks through how that conversion actually works — patches, position encodings, the four standard architectures (frozen encoder, projection, cross-attention, native multimodal), what an image actually costs you in tokens, and where vision quietly breaks."
reading_time: 22
---

If you have ever uploaded a picture of a chart to Claude and asked "what does this say," and gotten back a careful, accurate answer, the question worth asking is: *how, exactly?* The model is a transformer. Transformers read tokens, which are vectors. Pixels are not vectors. Something has to translate from one to the other before the language model sees anything at all. That translation step is what this field guide is about.

The story is shorter than you'd think. An image is sliced into patches (typically 14×14 pixels). Each patch gets passed through a small vision encoder — usually a transformer of its own — which produces a token-shaped vector. Those vectors get a positional encoding so the model knows where in the picture they came from. And then they are concatenated with the text tokens and handed to the language model, which attends across all of them. That's it. Almost every modern vision-language system is some variation of this five-step pipeline.

The interesting parts are in the trade-offs. Different vendors handle dynamic resolution differently (Claude's "any-res" approach versus GPT-4o's tile-based approach versus Gemini's fixed-resolution approach). Soft tokens versus discrete tokens matters when you're combining models. The cost — measured in tokens — varies wildly between architectures and resolutions, and showing up at the API gateway with a high-resolution screenshot can cost more than a small novel.

## What it covers

Fifteen sections, about twenty-two minutes if you read straight through.

**§ 01 — The big idea, in one breath.** Pixels → patches → vectors → tokens → attention. The whole pipeline in one figure.

**§ 02 — Cutting it into patches.** Step one, almost always. The 14×14 patch convention, where it comes from (ViT), and why it works. Interactive: drag the patch size and watch the resulting grid.

**§ 03 — Giving each patch a place.** Positional encoding for images — the same problem as for text, but in 2D. The four common approaches (learned absolute, learned 2D, sinusoidal, RoPE).

**§ 04 — Four ways to plug vision in.** The taxonomy. *Frozen encoder + projection* (LLaVA, the simplest). *Cross-attention* (Flamingo, BLIP-2 — vision tokens never enter the language stream directly). *Concatenated tokens* (Idefics, Pixtral — visual tokens live alongside text in the same sequence). *Native multimodal* (GPT-4o, Gemini — trained from scratch on mixed modalities).

**§ 05 — What the model actually looks at.** Attention visualization. When you ask "what does this chart say," which patches does the model attend to? Interactive: hover a question, see the attention heatmap on the image.

**§ 06 — Soft tokens vs. discrete tokens.** Continuous vector tokens (the LLaVA/GPT-4o style) versus discretized image tokens (the Chameleon/Gemini style). The trade-off between expressiveness and the ability to generate images back.

**§ 07 — What an image actually costs.** The token math. A 512×512 image at 14×14 patches is 1369 tokens — enough for a short essay. Dynamic resolution can push this to 5000+ tokens per image. The cost breakdown across vendors.

**§ 08 — Reading high-resolution.** Dynamic tiling — the technique most vendors use to handle images bigger than the native input resolution. Claude's "any-res," GPT-4o's tiles, Gemini's down-sampling, with concrete examples of each.

**§ 09 — How Claude sees an image, concretely.** A worked example. A real screenshot, the tile decomposition, the token cost.

**§ 10 — The base64 envelope.** The practical detail of getting an image into the API. The encoding, the size constraints, the gotchas.

**§ 11 — Generating images back.** The reverse direction. Diffusion models, autoregressive image models, the role of the language model as a planner versus a renderer.

**§ 12 — Where vision quietly breaks.** Failure modes. Small text in a screenshot. Charts with rotated axis labels. Dense tables. Diagrams that depend on precise spatial relationships.

**§ 13 — Choosing an approach.** The decision tree. When to use a frozen-encoder system, when to use a native multimodal model, when OCR is still the right answer.

**§ 14 — Practical notes for builders.** Hard-won observations from production deployment. Resolution-vs-cost choices. Pre-processing tricks (cropping, contrast). What to log so you can debug.

**§ 15 — References & further reading.** ViT, LLaVA, Flamingo, BLIP-2, Chameleon, Pixtral. The papers that actually changed practice.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/how-llms-see-images.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

The field guide lives at its own URL with a warm-paper editorial layout — vermilion accent, tappable definitions throughout, fifteen sections with interactive figures wired into the relevant chapters.

---

← Back to [Autonomy]({{ '/' | relative_url }})
