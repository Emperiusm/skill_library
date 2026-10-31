---
name: touchdesigner-generative-lexicon-press
description: "Perform text as audio-reactive typography in TouchDesigner: 25 layouts turn passages into moving compositions, sound drives movement and page changes, optional local Ollama writing partner. Trigger when a written passage needs to become a generative, sound-driven typographic performance."
---

# Generative Lexicon Press: Audio-Reactive Typography in TouchDesigner

## Purpose

This skill covers uisato's Generative Lexicon Press: a TouchDesigner
system where **written passages become moving compositions across 25
audio-reactive layouts; an optional local Ollama partner writes the
passages.** Sound drives movement, highlights, and page changes. Every
phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: **feed
a passage to the 25-layout instrument and play it with sound.**

## Source

r/vfx, uisato, "Generative Lexicon Press, generative,
audio-reactive typography for TouchDesigner" (score 20, 1 comment,
2026-10-30):

- https://www.reddit.com/r/vfx/comments/1xjgqub/
- Native Reddit video: v.redd.it/xj09h67x5myh1
- 4K walkthrough: https://www.youtube.com/watch?v=CVAS-w8300o
- Project files: Patreon and https://uisato.studio/tools

Evidence note: all facts below are the author's claims from the post
text. The one comment adds no tooling. A 4K walkthrough video exists
but is uncaptioned and was not deepened this run.

## Tools used

- TouchDesigner generative typography system
- 25 layouts; words and letters become structures, patterns, erasures,
  animated sequences
- Sound drives movement, highlights, and page changes
- Optional Writing Partner: generates new passages locally through
  Ollama (inputs: concept, writing mode, language)
- Deeply inspired by Ksawery Komputery's "Symphony in Acid", "one of
  the most amazing generative works ever created"

## Phase 1: Supply the passage

**Do**
1. Use your own written passage, or generate one locally with the
   Writing Partner: give Ollama a concept, a writing mode, and a
   language.

**Check**
- The passage reads well aloud, it will be performed, not just
  displayed.

**Why**
Local Ollama keeps the writing step private and free; the passage is
the score the layouts perform.

## Phase 2: Compose across layouts

**Do**
1. Arrange the 25 layouts into a sequence. Words and letters become
   structures, patterns, erasures, and animated sequences.
2. Adjust how each layout responds to sound: sound drives movement,
   highlights, and page changes.

**Check**
- Play the passage audio; each layout's motion, highlights, and page
  turns lock to the sound.

**Why**
The system is an instrument, not a template: the same passage plays
differently per layout and per audio input.

## What the walkthrough would add

A download plus frame review of the 4K walkthrough
(https://www.youtube.com/watch?v=CVAS-w8300o) would add: the actual
node/layout mechanics (how the 25 layouts are constructed), the audio
routing specifics (what analysis drives movement vs highlights vs page
changes), per-layout parameters, and the Writing Partner's Ollama
integration detail. The skill above covers the documented system; the
operator internals are the gap.

## The human method, distilled

1. **Name the influence precisely** ("Symphony in Acid", "one of the
   most amazing generative works ever created") so users know the
   target aesthetic.
2. **Ship the project files** (Patreon + studio site) and a 4K
   walkthrough, the product is the system, not a render.

**Depth status:** PARTIAL (author post text only; the 4K walkthrough
video exists but is uncaptioned and was not deepened this run, a
download + frame review would add the actual node/layout mechanics;
one comment, no tooling).
