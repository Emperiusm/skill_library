---
name: minimax-h3-image-native-comfyui
description: "Run MiniMax H3 Image natively in ComfyUI on day 0: one checkpoint does text-to-image and reference-image editing in 6 steps at guidance 1, with native resolutions up to 6272x2688, multi-reference editing via <Picture N> tags, and VAE anchoring for edits. Includes the commenters' P-H3-Image comparison (community fine-tune is better at small sizes, identity, and LoRA support) and the garbled-at-full-resolution failure report. Trigger when an H3 Image job needs the official native workflow, or when choosing between official H3 Image and P-H3-Image."
---

# MiniMax H3 Image, Native in ComfyUI (Day-0 Support)

## Purpose

This skill reconstructs the MiniMax H3 Image native ComfyUI workflow
from the author's post and comments, step by step, so another agent can
follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: one checkpoint does both text-to-image
and reference-image editing, natively, in 6 steps; connect images and
it is an edit workflow, leave them off and it is text-to-image.

## Source

Creator: Lexius2129. Reddit post:
https://www.reddit.com/r/comfyui/comments/1xsrnze/minimax_h3_image_is_natively_supported_in_comfyui/
(r/comfyui post 1xsrnze, score 101, 8 comments) | 2026-11-11 scout run,
audit 3. Full blog post:
https://blog.comfy.org/p/minimax-h3-image-is-now-available. Weights:
https://huggingface.co/Comfy-Org/MiniMax-H3-Image. Workflow templates:
https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_minimax_h3_image_t2i.json
and `.../image_minimax_h3_image_edit.json`.

This is a different model from the community P-H3-Image fine-tune
(skill `pruna-p-h3-image-comfyui`): official vs community, different
checkpoints, different strengths. Do not confuse the two; Phase 4 is
the comparison.

## Tools used

**ComfyUI** (latest version), **MiniMax H3 Image** checkpoint (diffusion
model + VAE + **Qwen3-VL** text encoder), **MiniMax H3 Image
Conditioning** node, **Prompt Enhancer**, Comfy-Org workflow templates
(t2i + edit JSON), **Comfy Cloud** (no-download option).
Commenter-mentioned: **P-H3-Image** (community fine-tune), **Z-Image
Turbo**, **MOSS**, **KREA2**, **RefMod**, MiniMax H3 LoRAs.

## Phase 1: Get the weights

**Do**
1. Update ComfyUI to the latest version.
2. Download the diffusion model, VAE, and Qwen3-VL text encoder from
   Hugging Face (Comfy-Org/MiniMax-H3-Image).
3. If you already run MiniMax H3 video, you already have the text
   encoder: H3 Image uses the same Qwen3-VL text encoder as the H3
   video model.
4. Or skip downloads entirely and use Comfy Cloud with the H3 Image
   template.

**Check**
- The text encoder file is the Qwen3-VL one; no second encoder download
  is needed if H3 video is already installed.

**Why**
- Shared encoder is the install win: one heavy file serves both the
  image and the video model.

## Phase 2: Text-to-image

**Do**
1. Load the MiniMax H3 Image template from the Templates panel, or the
   t2i workflow JSON from Comfy-Org/workflow_templates.
2. Leave width and height at 0 for automatic sizing: 2048x2048 for
   text-to-image.
3. Write a long, detailed prompt (up to 4096 tokens); the author says
   detailed descriptions work best, and to use the Prompt Enhancer.
4. The model is CFG-distilled and samples in 6 steps at guidance 1. No
   negative prompt.

**Check**
- Output is generated at its native size, not upscaled: 4096x4096 at
  1:1, 4736x3552 at 4:3, 5024x3360 at 3:2, 5472x3072 at 16:9, 6272x2688
  at 21:9.

**Why**
- Six steps with nothing to tune is the whole point of a distilled
  checkpoint: the workflow is load-template, write prompt, run.

## Phase 3: Reference-image editing

**Do**
1. Load the image-edit workflow JSON.
2. Connect images: `image_1` is the picture being edited; the other
   slots are references.
3. Refer to references in the prompt as `<Picture 1>`, `<Picture 2>`,
   etc.; numbering follows input order.
4. Connect the VAE when you edit, so reference images are anchored as
   latents and not only read by the text encoder.
5. Leave width and height at 0 and the output takes the size of
   `image_1`.

**Check**
- The edit keeps the identity/structure of `image_1`; the references
  change only what the prompt names.

**Why**
- Anchoring references as latents (via the VAE) is what makes the edit
  stick to the source image instead of drifting into a fresh generation.

## Phase 4: Know what the commenters say it does badly

**Do**
1. Expect the official model to be weakest where the community fine-tune
   is strongest: commenters report P-H3-Image is smaller, works at 4M
   pixels (official H3 Image has an 8M minimum, "anything below that is
   pure pixelated slop"), is uncensored, does not change identity when
   used as an edit, and has a LoRA version that "works with every
   Minimax H3 checkpoint I've tried" plus refmods and H3 LoRAs, while
   "Minimax image does none of that. Loras don't register at all."
2. Expect the official model's advantages to be upper resolution limit
   and generation speed: about 30% faster than P-H3 at 8K in one
   commenter's test.
3. Expect failure reports: one commenter gets "completely garbled"
   results at 4-20MP that "look good in preview, but not when zooming
   in to the correct resolution"; another finds results "worse than with
   Z-Image Turbo" and worse than MOSS/KREA2 at 2MP on animated character
   sheets and style consistency.

**Check**
- Judge at full zoom, not in preview; the garbled-at-full-resolution
  report is exactly the failure preview hides.
- Judge identity on edit against P-H3-Image if identity matters more
  than resolution.

**Why**
- A day-0 native integration is a distribution win, not a quality win:
  the community fine-tune is currently the better edit model by the
  commenters' own tests, and the official model's edge is speed and
  maximum size.

## The human method, distilled

1. **One checkpoint, two modes**: no images means text-to-image, images
   means edit.
2. **Six steps, guidance 1, no negative prompt**: nothing to tune.
3. **Generate at native size**; never upscale to reach it.
4. **Judge at full zoom**, and judge identity against P-H3-Image.

**Depth status:** FULL (full post text + all 8 comments; the model
itself was not run, and no generation beyond the quoted settings is
claimed).
