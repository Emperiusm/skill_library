---
name: minimax-h3-longform-documentary
description: "Generate a watchable 25-second native 1536x864 MiniMax H3 video on an RTX 3060 12 GB: Singularity V2 + DMAD 4-step LoRA at strength 1.0, initial frame + character refs + 3x3 storyboard guidance, 600 frames in one pass (~37.6 min), and the prompt discipline that fixed the motion defects (under-describe physics; 'natural, relaxed breathing' beats explicit abdominal-motion prompts). Trigger when a long H3 sequence must be watchable, not just completable, on a 12 GB card."
---

# MiniMax H3 Long-Form Documentary on a 12 GB Card

## Purpose

This skill generates a watchable 25-second MiniMax H3 video natively at
1536x864 on an RTX 3060 12 GB, step by step, so another agent can follow
the same recipe. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle). The
core method is: native resolution, one pass, and fix the prompt instead of
the render when the motion looks wrong.

## Source

Reddit, JinnTsui (full post text + 6 comments, 2026-10-29):

- https://www.reddit.com/r/comfyui/comments/1xhlut5/ - "RTX 3060 12GB -
  Finally Got a Usable 25-Second Video at Native 1536x864 (ComfyUI + H3)"

Evidence note: post text + comments; no workflow JSON inspected, so node
wiring beyond the named settings is not claimed. Same author as the
2026-10-28 snow-leopard recipe (skill `minimax-h3-native-3mp-lowvram`);
this is a distinct workflow (storyboarded long-form documentary vs native
3 MP stills), hence a variant skill. Hardware: RTX 3060 12 GB, 32 GB RAM.

## Tools used

MiniMax H3 Singularity V2; DMAD 4-step (LoRA strength 1.0); ComfyUI.
Commenter recipe: Zironic/H3-Optimizations custom node pack (memory +
sparse nodes). Hardware: RTX 3060 12 GB + 32 GB system RAM.

## Phase 1: Lock the native-generation recipe

**Do**
1. Model: MiniMax H3 Singularity V2 (not the Ref2VA V2 INT8 of the author's
   snow-leopard recipe).
2. LoRA: DMAD 4-step, strength 1.0.
3. Resolution: 1536x864 native, no upscaling; 24 FPS; 600 frames = 25 s.
4. Guide with an initial frame, character reference images, and a 3x3
   storyboard that maps to the sequence beats.

**Check**
- The entire visual sequence is one pass: "no stitched clips, cuts added
  in editing, or upscaled frames."
- The storyboard panels map to sequence beats (documentary concept here:
  two wildlife observers spot a mother cheetah with two cubs; camera
  shifts; cubs play; mother grooms both cubs).

**Why**
The author's arc: earlier generations "completed" on the 3060 but were not
watchable. Completing the generation is not the bar; a watchable result
is. Native generation preserves the detail upscaling invents.

## Phase 2: Iterate the prompt, not the settings

**Do**
1. Run full generations (the author ran three) and catalog the defects:
   inconsistent hand positions on one observer; unnatural swelling and
   twitching around the mother cheetah's abdomen; excessive ear twitching;
   camera continuity and lighting inconsistencies.
2. Fix motion defects in the prompt first. The emblematic case: describing
   the cheetah's abdominal movement too explicitly made the model
   exaggerate it into "something completely unnatural." Simplifying to
   "natural, relaxed breathing" produced a much better result.
3. Budget the time: final generation took 2256.36 s (37 min 36 s).

**Check**
- After the third generation: character consistency, animal movements,
  grooming actions, and camera transitions "finally good enough for a
  usable video."
- Replace only unnatural audio in post; the visuals stay one pass.

**Why**
Over-specifying motion invites the model to over-act it. The prompt is a
direction, not a simulation spec: under-describe the physics and the
model's prior fills in something plausible. (Inferred principle, labeled:
the author's breathing fix is the evidence.)

## Phase 3: Borrow the community's VRAM recipe when it OOMs

**Do**
1. If memory fails on longer or higher runs, try the commenter recipe
   (froschquark): the Zironic/H3-Optimizations custom node pack, memory
   node + sparse node. Reported: without it, fast OOM at start or 500+
   s/it stalls on other memory/chunk nodes; with it, 3 MP (2336x1344)
   10 s clips on a 4070 12 GB in ~13.3 min (167.52 s/it, 799 s total).
2. Consider the counter-advice: split the shot (one higher-res pass for
   the people, one for the cheetah) instead of forcing one 25 s
   generation (Support_Marmoset); try 8 steps if the result is slightly
   blurry (theOliviaRossi).

**Check**
- Verify VRAM claims on your own card before committing to a 37-minute
  generation. A commenter with a 5090 reported OOM past 20 s at 1 MP:
  "You never mentioned exactly what you did to fit that in 12 GB of
  vram" (Davikar). Treat every number as a starting point.

**Why**
The community's low-VRAM recipes are the real product here; the author's
numbers are the proof. But VRAM behavior is card- and workflow-specific.

## The human method, distilled

1. "I focused on getting an actual watchable result rather than just
   completing the generation." Completion is cheap; watchability is the
   bar.
2. Describe less to get more: the breathing fix is the emblematic example.
3. Share the settings so others can reproduce: the post is a full recipe
   (model, steps, resolution, frames, time), not a showcase.

**Depth status:** FULL (post text + 6 comments; no workflow JSON inspected).
