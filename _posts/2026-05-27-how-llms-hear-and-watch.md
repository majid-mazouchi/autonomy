---
title: "How LLMs Hear & Watch — Sound and Video as Tokens"
subtitle: "Sound is a wiggling line. Video is a stack of pictures with a clock attached. Neither can enter a language model as-is — both get translated into the same currency as words: tokens. Here's how a waveform and a film reel become something a transformer can read."
date: 2026-05-27 10:00:00 -0400
category: "Tools"
slug: how-llms-hear-and-watch
excerpt: "The companion to 'How LLMs See an Image.' Audio is more like text than you'd expect — a 1-D signal turned into a 2-D spectrogram, sliced into patches, and tokenized. Video is audio + a frame stream, which generates token counts that can outrun the context window of even the largest models in seconds. This field guide walks through both pipelines, the engineering tricks that make video tractable (frame sampling, spatiotemporal tokens, tube embeddings, attention pooling), and the practical cost calculus."
reading_time: 20
---

If you read the companion piece "How LLMs See an Image," you already know the trick: anything that isn't text gets quietly converted into tokens — token-shaped vectors — before the language model ever sees it. The interesting question for audio and video is *how that translation works*, and what the costs and failure modes are.

Audio turns out to be closer to text than you'd expect. The model doesn't process the raw waveform; it converts to a spectrogram (audio's equivalent of a picture), slices it into time–frequency patches, and tokenizes those. From there, it's the same architecture as vision. Video is harder. A two-minute clip at 30 fps is 3,600 frames — at the per-frame cost of an image, that's enough to overflow any context window. The whole game in video is reducing the token count: sampling fewer frames, sharing tokens across time (tube embeddings), attention pooling, transcribing the audio track and dropping most of the visual.

This field guide goes through both pipelines and the cost calculus that determines what's tractable.

## What it covers

Fourteen sections, about twenty minutes of reading.

**§ 01 — The one shared trick.** Pixels, samples, frames — all roads lead to tokens. The conceptual unity that makes the rest of the guide make sense.

**§ 02 — Sound is a wave — and that's the problem.** Why you can't just hand a raw audio waveform to a transformer. The dimensionality and the temporal structure that make it intractable.

**§ 03 — The spectrogram move.** Turn sound into a picture. The short-time Fourier transform, mel filterbanks, log compression. The result is a 2-D image of time vs. frequency that vision tokenization handles natively.

**§ 04 — Two kinds of audio token.** Continuous (Whisper-style, the encoder produces float vectors) versus discrete (EnCodec, SoundStream, AudioLM — the encoder produces integer codes). When each one is appropriate.

**§ 05 — Plugging audio into the language model.** Same four architectures as vision — frozen encoder + projection, cross-attention, concatenated tokens, native multimodal. The trade-offs.

**§ 06 — Making sound back.** The reverse direction. Vocoders, autoregressive audio generation, the realtime constraint.

**§ 07 — Video = frames + time + sound.** The decomposition. Why video is so much more expensive than image-plus-audio.

**§ 08 — Sampling frames: the first economy.** The most important lever. One frame per second instead of thirty cuts the cost by 30×. The trade-off between temporal fidelity and tractability.

**§ 09 — Tokens across space and time.** Tube embeddings — the technique that treats short clips as 3-D patches (height × width × time) and produces tokens that span multiple frames. Why this is more efficient than tokenizing each frame independently.

**§ 10 — Taming the token flood.** Attention pooling, learned summary tokens (à la Perceiver), spatiotemporal compression. The full toolbox.

**§ 11 — What audio and video actually cost.** The token math, with provider-specific numbers. A 10-minute lecture is roughly 5,000 audio tokens. A 1-minute video at 1 fps is roughly 60,000 tokens. The cost difference between "transcribe-then-reason" and "watch every frame."

**§ 12 — Where hearing and watching break.** Failure modes. Overlapping speakers, music interfering with speech, low-light video, fast cuts, on-screen text that gets blurred at sampling-time.

**§ 13 — Practical notes for builders.** The decisions you'll actually make. When to transcribe-then-reason (almost always, for content where speech carries the meaning — lectures, meetings, interviews). When to actually watch the video (visual-only content, sports, demos). The cost-vs-quality knobs.

**§ 14 — References & further reading.** Whisper, AudioLM, MusicLM, the Video-LLaMA / VideoChat-style multimodal models, the Perceiver architecture. The papers that defined the field.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/how-llms-hear-and-watch.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the field guide →
  </a>
</div>

The field guide lives at its own URL with a warm-paper layout — teal accent, plum em-italic, fourteen sections. Companion to "How LLMs See an Image" — same pipeline, different modality.

---

← Back to [Autonomy]({{ '/' | relative_url }})
