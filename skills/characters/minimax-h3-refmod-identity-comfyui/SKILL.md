---
name: minimax-h3-refmod-identity-comfyui
description: "Generate images of your own character with MiniMax H3 in ComfyUI without LoRA training: bake identity into a RefMod file from 8 photos with RefMod custom nodes, then prompt scenes, outfits, poses, and environments. 8 steps / 6 min, 25 steps / 14 min at 1.8 MP. Trigger when doing local AI character-consistent image generation without training a LoRA."
---

# MiniMax H3 Character Identity in ComfyUI (RefMod, No LoRA Training)

## Purpose

This audit reconstructs the exact workflow from cgpixel23's tutorial post and
the comment thread, step by step, so another agent can follow the same process.
Every phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The workflow's core method is: bake
identity into a RefMod file once, then generate new scenes from prompts with
no LoRA training.

Variant note: this is the same tool family as
`minimax-h3-character-swap-comfyui` (SAM3 + color-inversion masking for video
character replacement) and `minimax-h3-character-swap-nomask-lowvram`
(Character Swap LoRA, no masking, video), but a different workflow — image
generation, identity carried by a RefMod file, no masking step, no LoRA
anywhere. Do not confuse the three: SAM3 masks and inverts, the LoRA variant
trains/loads a Character Swap LoRA, this one bakes a RefMod file.

## Source

Creator: cgpixel23 (r/comfyui post 1x6phw0, score 26, 5 comments retrieved).

Source: https://www.reddit.com/r/comfyui/comments/1x6phw0/comfyui_tutorial_refmod_minimax_h3_image/
(native Reddit video; 2026-10-16 scout run). Workflow file via Google Drive
and Civitai article (links in the post; not retrieved). Video tutorial at
https://youtu.be/-CfyYOcsnVw (metadata unretrieved: the scout's
`yt_summarize.py` failed on a missing `yt_extract.py` script in the mirror).

## Tools used

Tools used: **ComfyUI**, **RefMod custom nodes**, **MiniMax H3** (image
generation). No ComfyUI version, no node graph, no RefMod node parameters
disclosed.

## Phase 1: Prepare reference photos

**Do**
1. "Prepare **8 photos of your character**." (Author's selftext, verbatim.)

**Check**
- 8 photos collected before touching any node. The author's input count is 8;
  commenter x33storm's working range is 8-12 images (see Phase 4).

**Why**
- The RefMod file is only as good as its references. Identity is baked from
  these photos; nothing later in the workflow adds identity information.

## Phase 2: Build the RefMod file

**Do**
1. "Use the RefMod custom nodes to create a RefMod file."
2. "Load the file into the MiniMax H3 workflow."

**Check**
- The RefMod file loads as a single unit into the MiniMax H3 workflow; there
  is no per-generation retraining step.

**Why**
- One baked identity file replaces a LoRA training run: "No traditional LoRA
  training required. Create your RefMod file, load it, write your prompt, and
  start generating!" The tradeoff is unresolved in the thread — commenter
  Norcalnomadman pushed back: "In 30min you could have had a working Lora lol."
  The author did not answer. Treat RefMod-vs-LoRA as an open cost/quality
  comparison, not a settled win.

## Phase 3: Prompt the scene, generate

**Do**
1. "Enter your prompt describing the scene, outfit, pose, or environment."
2. Generate new images "while aiming to maintain your character's identity."
   The author frames it as exploration: "You can explore different scenarios,
   clothing styles, locations, and compositions while aiming to maintain your
   character's identity."

**Check**
- Author's measured costs at **1.8 megapixels**: **8 steps = 6 min**,
  **25 steps = 14 min**. (Selftext, verbatim figures.)
- Commenter x33storm's independent numbers (unverified, attributed): 15 s of
  0.8 MP at 6 steps in ~180 s on "32Gb/16Gb", using 10 images and a 30-sec
  audio clip made into RefMod; "Works scarily well, compared to WAN, LTX or
  H3 FF."
- Commenter aniki_kun's reaction to the author's numbers: "6 minutes for one
  image?" — the speed/quality tradeoff is the thread's main open question.
  Commenter menasan asked the same thing another way: "What's the benefit of
  this or is it because you don't need to make a lora?" Neither got an
  author answer.

**Why**
- Identity lives in the RefMod file; the prompt controls only the new scene.
  Steps buy quality at roughly linear time (8 steps/6 min vs 25 steps/14 min
  at 1.8 MP, author's numbers).

## Phase 4: Choose reference images well

**Do**
1. Follow commenter x33storm's reference discipline (attributed, unverified):
   "It all comes down to using the right images (and audio to clone voice),
   the token amount and resolution of images."
2. "Think around 8-12 images, keep resolution of images decent but not too
   high or low. Improves gen times and identity."
3. Note the same commenter's identity claim: "Refmod just really establishes
   the identity, better than even first frame." Treat this as one commenter's
   report, not a measured result — no comparison protocol was posted.

**Check**
- Identity holds across new scenes, outfits, and poses. If it drifts, the
  fix per the commenter is the reference set (count, resolution), not the
  prompt.

**Why**
- Reference-image choice is the quality lever, not prompt engineering. Too
  high a resolution costs generation time; too low costs identity.

## The human method, distilled

1. **Bake identity once, prompt scenes forever.** The RefMod file is the
   character; prompts are disposable.
2. **Reference images are the control surface**: 8-12 images at decent (not
   extreme) resolution.
3. **Steps buy quality at linear-ish time**: 8 steps/6 min vs 25 steps/14 min
   at 1.8 MP (author's numbers).
4. **The LoRA comparison is open**: a working LoRA takes ~30 min per the
   pushback comment; RefMod's build time was never stated. Measure both
   before claiming RefMod is cheaper.

## Failure modes

- **Slow generation.** 6 minutes for one image at 8 steps / 1.8 MP is the
  author's own number. Lower megapixels and fewer steps are the only posted
  levers (commenter: 0.8 MP at 6 steps, ~180 s).
- **Identity drift.** No fix was posted beyond the reference-image discipline
  in Phase 4. The author wrote "aiming to maintain your character's identity"
  — "aiming", not "guaranteeing".
- **No author follow-up.** The author did not answer the LoRA tradeoff, the
  speed question, or the benefit question in the retrieved comments. The
  workflow file (Drive/Civitai) and the YouTube tutorial are the remaining
  sources for node-level detail.

**Depth status:** PARTIAL (full post text + comments with exact step/time/MP
figures; no node graph, no RefMod node parameters, YouTube tutorial metadata
unretrieved due to the missing `yt_extract.py` script).
