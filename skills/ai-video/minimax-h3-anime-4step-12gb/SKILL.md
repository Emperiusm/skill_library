---
name: minimax-h3-anime-4step-12gb
description: "Generate a 20-second anime video with audio in about 200 seconds on an RTX 4070 Super 12 GB: MiniMax H3 MATLOW fused INT8 ConvRot model at 4 steps with the res_multistep sampler, Comfy Kitchen Attention, BlockSparseAttention SLA at 20% keep, H3 Chunk FeedForward at 8 chunks, and sigma shift 12/3, from a single reference image, then Real-ESRGAN anime upscale to 1080p. Includes the commenter reproduction (297 s generation + 386 s upscale) and the failure modes (hands, lip-sync, drifting backgrounds) plus the character-sheet cropping fix. Trigger when fast anime-style H3 generation is needed on a 12 GB card."
---

# MiniMax H3 4-Step Anime Recipe (20 s in ~200 s on 12 GB)

## Purpose

This skill reconstructs the 4-step anime workflow from the author's post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: four sampling steps and a sparse attention stack make a 20-second anime clip cheaper than a coffee break.

## Source

Creator: Raw_Emotion_. Reddit post:
https://www.reddit.com/r/comfyui/comments/1xu3wg9/generated_a_20second_anime_video_with_audio_on_my/
(r/comfyui post 1xu3wg9, score 95, 32 comments) | 2026-11-12 scout run, audit 4.

This is a distinct recipe from the other low-VRAM H3 skills in this library: it is the 4-step MATLOW anime recipe on 12 GB, not the 6 GB Singularity V2 recipe (`minimax-h3-singularity-v2-6gb`) and not the native 3MP recipe (`minimax-h3-native-3mp-lowvram`). Do not merge them.

## Tools used

**ComfyUI**, **MiniMax H3** MATLOW fused INT8 ConvRot model, **Comfy Kitchen Attention**, **BlockSparseAttention** (SLA, 20% keep), **H3 Chunk FeedForward** (8 chunks), **Real-ESRGAN** anime upscale. Commenter-mentioned: **VideoRef** (motion transfer, planned next experiment).

## Phase 1: Run the 4-step recipe

**Do**
1. Load the MiniMax H3 MATLOW fused INT8 ConvRot model.
2. Set 4 steps with the res_multistep sampler.
3. Stack the attention: Comfy Kitchen Attention, BlockSparseAttention (SLA, 20% keep), H3 Chunk FeedForward (8 chunks).
4. Set sigma shift to 12/3.
5. Generate from a single reference image plus a detailed prompt. The author generated 481 frames at 24 fps, 960x544, in around 200 seconds.

**Check**
- Hardware for that number: RTX 4070 Super 12 GB, i5-14600K, 16 GB DDR5 RAM. The author notes the result "was done in the first go itself" (2 takes total: the first generation, then one re-run with the upscaler added).
- Commenter rguerraf reproduced it on his own rig: 297 seconds to generate, then 386 seconds for ESRGAN 2x, 11.5 minutes total. If your generation is far above ~300 seconds on a 12 GB card, the sparse attention stack is not active.

**Why**
- Four steps with a fused INT8 model is the whole speed story. The attention stack is what keeps 4 steps from falling apart into mush.

## Phase 2: Upscale with Real-ESRGAN

**Do**
1. Run Real-ESRGAN anime upscaling to 1080p. The author reports this pushed the total workflow time to around 10 minutes.

**Check**
- The posted clip has no post-processing or editing; the author posted raw output "just to demonstrate the raw output."

**Why**
- Upscaling after generation is cheaper than generating at 1080p. The 200-second generation is the headline; the upscale is the tax.

## Phase 3: Know the failure modes

**Do**
1. Expect hands and fingers to get messed up in some frames, lip-sync to be imperfect, and some camera transitions to be jarring.
2. Expect small details to drift: the author notes the notebook drawing changes and background geometry breaks down towards the end, though the volcano drawing on the notebook and the white roadside railing stay consistent across several shots.

**Check**
- Character consistency across camera angles holds (facial expressions, small details); hands and backgrounds do not. Judge the clip on those two axes separately.

**Why**
- Four steps buy speed by spending detail. The failures cluster exactly where the model has the least information: hands, lips, and backgrounds at the end of a long clip.

## Phase 4: Fix audio and character sheets with commenter tips

**Do**
1. For the tin-can audio: "Try 20 on the audio shift. I think that helps the audio tin can from some Turbos. Maybe even add 'high quality voice' in the overall_soundscape." (commenter SpaceNinjaDino)
2. For character sheets: crop every reference to just portrait, front, side, back. "When I used multiple sheets, half the gens would have character bleeds and other artifacts. When I cropped all my references to just portrait, front, side, back, all those problems went away." Do not use a detail area with zoomed-in spots. (commenter SpaceNinjaDino)
3. Next experiments, per the author: character sheets for better consistency and VideoRef for motion transfer.

**Check**
- If characters bleed into each other, the reference sheets have zoomed detail areas. Crop them to the four views and re-run.

**Why**
- The model reads whatever is in the reference. A zoomed detail area is an instruction to blend that detail into the character; four clean views are an instruction to keep the character.

## The human method, distilled

1. Four steps, fused INT8, sparse attention: speed is a settings choice, not a hardware purchase.
2. Post raw output; the speed claim is only credible if the clip is unedited.
3. Hands and backgrounds are where 4-step generation fails first; judge accordingly.

**Depth status:** FULL (full post text with exact model, steps, sampler, attention stack, chunk count, sigma shift, frame count, resolution, and runtime; 25 comments including a commenter reproduction with timings and two actionable tips).
