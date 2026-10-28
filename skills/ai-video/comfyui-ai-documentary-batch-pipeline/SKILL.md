---
name: comfyui-ai-documentary-batch-pipeline
description: "Produce short AI history documentaries end to end in batch: Claude master prompt researches with sources, builds a visual bible, and writes the script in 10-second chunks; Qwen Image 2.1 renders images in batch from prompt files; Claude QA flags bad images (hands, period errors, continuity) and rewrites only those prompts; MiniMax H3 turns approved images into 10-second clips with the image as exact first frame; Qwen3-TTS batches narration per line; RTX Video Super Resolution upscales x2 to 2K. Includes the author's hardware and per-stage timings for a 10-minute documentary. Trigger when an AI documentary or explainer needs to be produced as a repeatable batch pipeline rather than one-off generations."
---

# ComfyUI AI Documentary Batch Pipeline

## Purpose

This skill reconstructs the documentary pipeline from the author's
post, step by step, so another agent can follow the same process. Every
phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The video's core method is:
one master prompt produces a visual bible and a script in 10-second
chunks, images are batched from prompt files, Claude QA rewrites only
the bad prompts, approved images become exact first frames for
10-second clips, narration is batched per line, and everything is
upscaled x2 to 2K.

## Source

Creator: EzkaProductions. Reddit post:
https://www.reddit.com/r/comfyui/comments/1xfx5sv/automated_ai_2k_documentaries_in_comfyui_qwen/
(r/comfyui post 1xfx5sv, score 67, 12 comments) | 2026-10-27 scout run,
audit 3. Tutorial: https://www.youtube.com/watch?v=oOq5EsY6nTU (not
retrieved; nothing beyond the post and comments is claimed). This is a
different workflow from the existing MiniMax H3 long-video skills
(SelfLift, SyncTile, Chain Director): those solve multi-segment video
continuity, while this one is a full documentary production pipeline
(script to images to clips to narration to upscale).

## Tools used

**Claude** (research, visual bible, script, QA), **Qwen Image 2.1**
(batch image generation, Inspire Pack Load Prompts From Dir),
**MiniMax H3** (image-to-video), **Qwen3-TTS** (voice design + batch
TTS), **RTX Video Super Resolution** (x2 upscale).

## Phase 1: Script and prompts (Claude master prompt)

**Do**
1. Write a master prompt in Claude that researches the topic (with
   sources), builds a "visual bible" (fixed style, character, and
   location blocks so characters stay consistent), and writes the
   script in 10-second chunks.
2. Take Claude's output zip: one prompt .txt per image (positive /
   negative / name), the video prompts, and a Narration.txt.

**Check**
- Characters and locations stay consistent across chunks because the
  visual bible fixes style, character, and location blocks up front.

**Why**
- The bible is the consistency mechanism: without fixed blocks, a
  10-second-chunk script drifts shot by shot, and no later stage can
  recover it.

## Phase 2: Images in batch, then QA only the bad ones

**Do**
1. Feed Qwen Image 2.1 in batch with Load Prompts From Dir (Inspire
   Pack): one image per prompt file.
2. Upload the images back to Claude: it flags bad ones (hands, period
   errors, continuity) and rewrites only those prompts.
3. Delete the bad image, set the index, regenerate.

**Check**
- Bad images are the only ones regenerated; good images are never
  re-rolled.

**Why**
- QA-by-rewrite-only is the cost control: regenerating everything
  would multiply the 1-hour image stage, while hand-checking every
  image would cost the human the batch was meant to save. The author
  states the QA classes explicitly (hands, period errors,
  continuity), which is what makes the loop checkable.

## Phase 3: Video, narration, upscale (batch, per line, per clip)

**Do**
1. Run MiniMax H3 image-to-video: the approved image is the exact
   first frame, 10 seconds per clip, batch with an index + queue
   count.
2. Run Qwen3-TTS: voice design, save the voice, then batch TTS with
   one audio file per line.
3. Run RTX Video Super Resolution x2 on every clip, to 2K.

**Check**
- Clips are 10 seconds, first frame matches the approved image, and
  narration lines map one-to-one to audio files.

**Why**
- The batch discipline (index + queue, one file per line, x2 on every
  clip) is what makes a 10-minute documentary shippable: each stage's
  unit is fixed, so a failure is local to one image, clip, or line.

## Phase 4: Budget it (hardware and times, as stated)

**Do**
1. Run on the author's hardware: RTX 5090 laptop (24 GB VRAM, 64 GB
   RAM).
2. Budget a 10-minute documentary as: images 1 hour, video clips 4
   hours, narration 3 minutes, edition 15 minutes.

**Check**
- The video stage dominates (4 of about 5.3 hours); narration and
  editing are negligible by comparison.

**Why**
- The bottleneck is stated, not guessed: anyone adopting this pipeline
  should expect video generation, not scripting or editing, to set
  the schedule.

## The human method, distilled

1. **Bible first, chunks second**: fixed style/character/location
   blocks before any generation.
2. **Rewrite only the bad**: QA flags the failure class, only that
   prompt is rewritten and re-rolled.
3. **Approved image = exact first frame**: the image stage's output
   is the video stage's contract.
4. **Batch units are fixed**: 10-second clips, one audio file per
   line, x2 on every clip, so failures stay local.

## Failure modes and commenter notes

- **LLM QA is not human QA**: a commenter warns that an LLM judging
  frames from a render "is not going to get the QA to where it's not
  slop," and that manual sorting is still quicker than uploading a
  batch to an LLM just to check for bad hands. Treat the Claude QA
  loop as a filter, not a guarantee.
- **Claude does not have the last word**: the author's reply to the
  QA criticism; the human still approves the final images.
- **Go-local variant (untested)**: commenters suggest replacing the
  Claude step with a local LLM plus a deep-research harness, and
  trying VoxCPM instead of Qwen3-TTS. Neither is tested by the author.
- **Image settings (partial)**: the author cites "0.9 MO at 8 steps,
  scaled up to 2K" for his image settings; no fuller per-model step
  counts are claimed.

**Depth status:** FULL (full six-step pipeline, QA classes, hardware,
and timings from the post; the linked tutorial was not retrieved).
