---
name: minimax-h3-hyperflow-6gb
description: "Run MiniMax H3 HyperFlow video generation on 6 GB VRAM in ComfyUI: 14B HyperFlow model, 6 sampling steps, no LoRA, SLA Attention and SelfLift Sampler, then ComfyUI-H3-FaceFix face refinement and RelayVSR upscaling. Trigger when a low-VRAM H3 video workflow is needed with face fixing and upscaling in one pipeline. DEPTH-LIMITED: post text only, no node settings or timings disclosed."
---

# MiniMax H3 HyperFlow 6GB Workflow (FaceFix + RelayVSR)

## Purpose

This skill runs a complete low-VRAM video pipeline in ComfyUI: fast generation, facial refinement, and upscaling. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method, as stated by the author, is: combine fast generation, facial refinement, and high-quality upscaling into one pipeline that runs on low-VRAM GPUs.

**Depth status: DEPTH-LIMITED.** This skill is built from the author's full post text only (1,605 characters). No comments, no tutorial transcript, no node settings, timings, resolutions, or workflow file were inspected. The workflow file sits behind a Google Drive link and a Civitai article; the tutorial video was not retrieved. Treat every phase below as the named-component workflow the post discloses, and verify settings against the workflow file before running it in production. This is a distinct variant from the other H3 skills in this library (Singularity V2 6GB, 4-step anime, chain director, and others): 14B HyperFlow, 6 steps, FaceFix, and RelayVSR together.

## Source

- Post: "The Ultimate MiniMax H3 Workflow for Consistent Character Text & Image-to-Video on Just 6GB VRAM!" by cgpixel23 — https://www.reddit.com/r/comfyui/comments/1y4ch10/ (score 24, 0 comments).
- Workflow links in the post: Google Drive file and https://civitai.com/articles/39700/the-ultimate-minimax-h3-workflow-for-consistent-character-text-and-image-to-video-on-just-6gb-vram ; tutorial video https://youtu.be/iexTqIBdhQ8 (not retrieved in this run; its contents are not claimed here).
- Scout audit 2026-11-25.

## Tools used

ComfyUI; MiniMax H3 HyperFlow (14B-parameter model, 6 sampling steps, no LoRA); SLA Attention and SelfLift Sampler (performance/acceleration); ComfyUI-H3-FaceFix-PixelAILabs (face detection, refinement, stitch-back); RelayVSR (video upscaling).

## Phase 1: Generate with HyperFlow at 6 steps

**Do**
1. Use the lightweight 14B-parameter HyperFlow model in ComfyUI, supporting both text-to-video and image-to-video generation.
2. Generate in 6 sampling steps, with no LoRA required.
3. Integrate SLA Attention and the SelfLift Sampler to optimise performance and accelerate generation.

**Check**
- The author's stated target is generation on 6 GB of VRAM. No generation time, resolution, or frame count is disclosed in the post, and none is invented here. Verify against the workflow file.

**Why**
Step count and model size are the VRAM levers. A 6-step workflow is what makes the rest of the pipeline (face fix + upscale) affordable on the same card.

## Phase 2: Refine faces with FaceFix

**Do**
1. Run ComfyUI-H3-FaceFix-PixelAILabs over the generated video: it analyses the video, detects problematic facial details, refines them, and stitches the improved faces back into the original video.

**Check**
- Faces are refined in place and stitched back, rather than the video being regenerated.

**Why**
Face defects are the visible failure of fast video generation. A detect-refine-stitch pass fixes the highest-visibility defect without paying for a slower generation.

## Phase 3: Upscale with RelayVSR

**Do**
1. Run RelayVSR over the refined video to produce sharper, higher-resolution results.

**Check**
- No upscale factor, target resolution, or timing is disclosed in the post. RelayVSR's own mechanism was audited in detail on 2026-11-11 (see the RelayVSR watchlist row) and is not re-derived here.

**Why**
Upscaling is kept as a separate final stage so the generation stage can stay at low VRAM and low step count. This separation is the author's stated pipeline order (generate, refine, upscale).

## The human method, distilled

1. "Combine fast generation, facial refinement, and high-quality upscaling into one complete pipeline that runs on low-VRAM GPUs." (author's stated goal, quoted)
2. Fix faces after generation; do not slow generation to fix faces.

**Depth status:** DEPTH-LIMITED (see the note at the top). A media download of the tutorial video would add spoken settings if it has captions; it would not add the workflow file itself, which sits behind the Drive/Civitai links. Do not pad this skill with settings from other H3 variants.
