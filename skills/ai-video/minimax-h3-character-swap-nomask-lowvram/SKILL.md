---
name: minimax-h3-character-swap-nomask-lowvram
description: "Swap a character in video with MiniMax H3 + Character Swap LoRA in ComfyUI with no masking: 0.4 MP at 8 steps, runs on 6 GB VRAM. Reference-video latent injection, Qwen2.1 start-frame trick, and the wan2gp low-VRAM alternative. Trigger when doing AI character replacement on a low-VRAM card."
---

# MiniMax H3 Character Swap, No-Mask LoRA Variant (6 GB VRAM)

## Purpose

This audit reconstructs the workflow from cgpixel23's r/comfyui tutorial post
and 27 comments, step by step, so another agent can follow the same process.
Every phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The workflow's core method is:
describe the character on a sheet, skip the mask, let the LoRA repaint.

Variant note: this is the same tool as
`minimax-h3-character-swap-comfyui` (MiniMax H3 character replacement), but a
different workflow. That variant masks the target with SAM3 and inverts the
colors inside the mask as the repaint signal. This one drops masking
entirely and drives the swap with a **Character Swap LoRA** at **0.4 MP, 8
steps**, with the author's stated goal of fitting the whole thing on a
**6 GB VRAM** card (per the post title; the author's sentence describing the
VRAM figure was truncated in the scraped selftext).

## Source

Creator: cgpixel23

Source: https://www.reddit.com/r/comfyui/comments/1wzy0w2/comfyui_tutorial_character_swap_with_minimax_h3/
(native Reddit video; r/comfyui post 1wzy0w2, score 366, 27 comments) |
2026-10-09 scout run. Author's recipe, verbatim from the post text: "new
**ComfyUI workflow for video character swapping using MiniMax H3 + Character
Swap LoRA**, and the main advantage is that it works **without masking**,
which can significantly reduce VRAM usage and simplify the process. The
workflow generates at **0.4 MP in just 8 steps**, supp[truncated in source]".

## Tools used

Tools used: **ComfyUI**, **MiniMax H3** (video generation), **Character Swap
LoRA**, **Qwen3VL-32B-minimax (Q2.gguf) CLIP** (commenters ask where to
obtain it; (Labelled: dependency requested, not explained by the author)).

## Phase 1: Build the character reference (character sheet vs LoRA)

**Do**
1. Decide between two identity-carriers: a **character sheet** (a collection
   of images stored in a single `.safetensors` file, loaded into Comfy
   instead of one or more reference images or a LoRA) or a **trained
   character LoRA**.
2. For a sheet: assemble multiple images of the character (front, expressions,
   looks) into one `.safetensors` bundle.

**Check**
- One file per character loads into the workflow. Multi-character shots are
  feasible without bleeding one identity into another.

**Why**
- ImpressiveStorm8914's comparison: sheet advantages are "you only load one
  file per character, creating one takes less than a minute (unlike loras),
  they can offer greater variety (emotions, looks etc) over 1 or 2 reference
  images and character bleeding is cut down to a minimum when the characters
  so multiple characters is easy to do."

## Phase 2: Skip the mask

**Do**
1. Do not set up SAM3 or a rectangle mask. Feed the whole frame into the
   swap: the workflow has no masking step at all.

**Check**
- There is no mask node, mask prompt, or masked region in the graph.

**Why**
- Author: no masking "can significantly reduce VRAM usage and simplify the
  process." Masking costs memory for the mask pipeline and costs the human
  the fiddling of mask prompts per shot.

## Phase 3: Generate at 0.4 MP, 8 steps

**Do**
1. Set resolution to **0.4 MP**.
2. Set sampling steps to **8**.
3. Cap clip length at **5 seconds** on cards under 6 GB VRAM.

**Check**
- The render envelope on low-VRAM cards: Reckless_Venom1507's measured
  ceiling, "On less than 6gb vram u can't go beyond 5 seconds and 0.4 MP".

**Why**
- Low resolution plus few steps is what makes H3 fit on a 6 GB card at all.
  Netrezen's reaction frames the achievement: "Just surprised you can even
  run H3 on less than 8GB VRAM tbh."

## Phase 4: Hunt the seed (expect it to take many tries)

**Do**
1. Generate with the seed randomized and inspect the character identity in
   each output.
2. Keep generating until one seed works; record that seed number.

**Check**
- The identity holds across the clip and the motion still matches the
   source.

**Why**
- fsocietyARG's warning: "Seems its VERY seed dependant, i Once tried this
  same lora and after several (i mean SEVERAL) attempts i found only a
  working seed, think i wrote the number somewhere.."
- Two independent testers (frogsty264371, same) report "Poor facial
  likeness", and fsocietyARG's twin reply reads as the same failure through
  a different door: "thought I was just having bad seeds."

## Phase 5: Anchor the motion with the reference-video latent

**Do**
1. Before sampling, **inject the reference video's latent into the latent
   that goes to the sampler** — the sampler starts from the reference video
   latent instead of an empty/noise latent.

**Check**
- Character motion stays in sync with the source; watch for drift where the
  new character's motions go out of sync with the original (e.g. mouth or
  body lag).

**Why**
- TurbTastic's recipe: "Have you tried injecting the reference video latent
  into the latent that's going to the sampler? That way it starts sampling
  with the reference video latent instead of an empty latent, and that can
  help to avoid drift like when they go out of sync with their motions."

## Phase 6: Choose the low-VRAM path that fits your card

**Do**
1. **6 GB or less, and it must stay inside ComfyUI:** use this workflow.
2. **Low-VRAM card and you can leave ComfyUI:** try **wan2gp** — nstern2:
   "I find that wan2gp works better for video stuff than comfyui ever does,
   especially for low vram cards."
3. **Below ~12 GB VRAM as an alternative model:** **LTX 2.5** — "It is fast
   definitely faster than 2.3 but loses the faces within a second if it has
   some movements, for talking videos it's good" (Reckless_Venom1507).
4. **Regardless of path:** build a good start frame with **Qwen Image 2.1**
   image-to-image: "start with a good starting image... image to image
   generate your character in the same pose as the original character but
   keeping the background" (nstern2). (Labelled: nstern2's personal trick,
   not demonstrated in the author's video.)

**Check**
- Start-frame check: the character is in the same pose as the source and
  the background is intact.

**Why**
- The swap only works as well as its start frame; the generation inherits
  pose and background from the first frame, so a good start frame does half
  the work before sampling begins.

## Phase 7: Know the current meta around this workflow

**Do**
1. Keep an eye on **RefMods**: Netrezen (10 upvotes): "Well, it's all about
   RefMods now really."
2. Track the community open question: "Does this mean character Loras are
   kinda dead?" (MediumRoll7047, 5 upvotes) — character sheets + RefMods are
   contesting the LoRA training slot. (Labelled: community sentiment, not a
   verified deprecation.)

**Check**
- Before committing weeks to training a character LoRA, re-check whether the
  current posts still recommend training one for your use case.

**Why**
- The tooling around H3 moves in weeks; a LoRA trained today can be
  obsolete-by-convention before the model you trained it for matters.

## The human method, distilled

1. **Drop the mask, keep the identity carrier.** No masking cuts VRAM and
   removes a fiddly step; the LoRA or sheet carries who the character is.
2. **Sheets over LoRAs when you want speed.** Under a minute to build, one
   file per character, less bleeding in multi-character shots.
3. **The seed is a lottery ticket.** Plan for several attempts; write down
   the working one.
4. **Start the sampler from the reference latent, not noise.** Motion drift
   is the failure this prevents.
5. **Resolution and length are the VRAM dials.** 5 seconds at 0.4 MP is the
   documented envelope under 6 GB.

## Failure modes

- **Identity drift to a stranger.** blimey4: "I tried it and it kept turning
  the woman into a guy wearing an orange shirt and hat. For the life of me,
  couldnt find a reference to a 'man' or 'shirt/hat' anywhere ha!"
  stonebloomers confirms the pattern: "seems like the first gen works and
  then it just ignores the swap entirely."
- **Poor facial likeness.** Reported independently twice; expect to burn
  many seeds before identity locks (Phase 4).
- **LTX 2.5 face loss on moving shots.** Loses faces within a second when
  there is movement; fine for talking-head shots (Reckless_Venom1507).
- **Qwen3VL-32B-minimax Q2.gguf (CLIP) dependency.** Commenters ask where to
  get it (Otherwise-Bar-1930); the author does not answer in the scraped
  comments. Missing or mismatched CLIP is a plausible setup blocker.
- **Mouth-sample requirement.** fallengt asks "why do you need 4 samples
  for the mouth" and whether stuffing "every facial detail" in the sheet
  works or "is it a meme" — both unanswered in the scraped comments.
  (Labelled: open questions, not resolved evidence.)

**Depth status:** FULL for the comment evidence (post text + 27 comments
with quoted recipe, parameters, failure reports, and community tricks);
LIMITED for the author's video itself (native Reddit video, no transcript
or captions scraped; the selftext recipe sentence is truncated after
"supp"). A media download would recover the exact ComfyUI node layout, the
LoRA strength and sampler settings, and the character-sheet construction.
