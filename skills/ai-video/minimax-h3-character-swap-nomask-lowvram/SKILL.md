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

## AAA studio practice

No named AAA studio publishes seed-lottery character swaps at 0.4 MP, 8
steps; studios attack the same identity problem (keep who it is, change
what they do) with far more control points:

- **ILM FaceSwap on *Indiana Jones and the Dial of Destiny*: blending,
  never one recipe.** VFX sup Robert Weaver told befores & afters that
  FaceSwap spans "shooting a separate plate and tracking it in" all the
  way to "fully replacing the face with a CG asset." On Dial: Flux
  (proprietary IR cameras flanking the main camera) plus tracking dots and
  witness cameras for rigid tracking; a full-motion CG head built with
  Medusa (ILM/DisneyResearch|Studios) driven through the complete FACS
  expression set as a base expression library; and ML used to search
  archival Ford footage for past frames matching each shot's orientation,
  frame by frame, as an identity target. Review discipline: low-res renders
  with bounding boxes so reviewers make "informed decisions." Studio
  lesson the pack adopts wholesale: identity is a per-shot blend decision,
  not a single node.
  Source: https://80.lv/articles/see-how-industrial-light-magic-made-harrison-ford-40-years-younger?amp=1
- **Lola VFX 2.5D on *Captain Marvel* / *Avengers: Endgame*: consistency as
  the acceptance discipline.** 200+ de-aging/aging shots on *Endgame*; all
  done in 2D comp (Flame), no head cams, actors free to move. Sup Trent
  Claus: "easy to get one shot approved, but to have all the other shots
  in a sequence... be consistent is harder" — the face must read as the
  same person (e.g., Sam Jackson circa 1995) regardless of angle, lighting,
  or which artist touched the shot. Lola's rule: modify the actor's actual
  on-screen performance, treating "each and every frame like a painting."
  This is the production version of the pack's Phase 4 seed hunt: the
  acceptance is identity consistency across the whole take, not one good
  frame.
  Source: http://www.cgw.com/Publications/CGW/2019/Winter-2019/Face-Lift.aspx
- **Digital Domain Charlatan on *Free Guy*: neural face-swap as
  performance re-animation.** The studio's deep-learning renderer analyzes
  the source performance "down to the minutia," artists hand-build the new
  face, the network matches and replaces the original, and artists can then
  alter expressions. Previously used on a Super Bowl "Coach Lombardi" spot
  and the Beckham "Malaria Must Die" campaign; on *Free Guy* it re-animated
  dialogue to avoid reshoots. The studio analog of the pack's latent
  injection (Phase 5): the motion source is sacred, the face is the
  replaceable layer.
  Source: http://beforesandafters.com/2021/08/26/vfx-futures-how-a-deep-learning-renderer-was-used-to-re-animate-a-characters-lines-in-free-guy/?amp
- **Lucasfilm / *The Mandalorian* S2 Luke: deepfake as a likeness guide,
  hired from the community.** Lucasfilm's Landis Fields ran deepfake R&D as
  a likeness guide; the shipped shot used Lola's 2.5D craft over a body
  double blended with Hamill's own on-set performance, plus "The Egg" LED
  rig for high-res facial texture capture. When YouTuber Shamook's deepfake
  looked better than the studio's, Lucasfilm hired him, and his work shipped
  in *The Book of Boba Fett*.
  Sources: https://screenrant.com/mandalorian-luke-skywalker-mark-hamill-no-cgi-deepfake-look/ and https://www.starwarsnewsnet.com/2021/07/lucasfilm-hires-deepfake-making-fan.html
- **Head replacement over stunt doubles (*Terminator: Dark Fate*
  opening).** VFX sup Jeff White: the stunt-heavy opening "was to replace
  the heads." Same coverage notes Gradient Effects/Secret Lab's markerless
  approach: 180 de-aging shots in six weeks, extracting facial muscle
  movement without tracking markers — the industrial cousin of the pack's
  "skip the mask" instinct (Phase 2): fewer setup constraints, more
  algorithmic load.
  Source: https://digital.copcomm.com/i/1192296-winter-2019/23
- **Disney Research FRAN (SIGGRAPH Asia 2022): identity-safe re-aging with
  artist control as a production requirement.** A U-Net predicts per-pixel
  RGB deltas overlaid on the input so identity is preserved rather than
  regenerated, built for temporal stability across expressions, viewpoints,
  and lighting; the paper explicitly ships artist-localized control and
  fine-tuning tools, noting that is "largely important in real production
  pipelines and often overlooked in related research."
  Source: https://studios.disneyresearch.com/2022/11/30/production-Ready-Face-Re-Aging-for-Visual-Effects/

Notes on what the sources do NOT establish: no named-studio source was found
for seed management or deterministic-seed discipline in stochastic AI VFX
(the closest is thin vendor marketing urging seed/prompt/control-map/model
version tracking, labeled as such); render-farm batch sweeps specifically
for AI face generations are undocumented in public production sources. The
pack's Phase 4 seed lottery is an inference from community evidence, not a
documented studio practice.

## Agent automation

1. **Treat the seed hunt as a batch job, not a lottery.** Convert Phase 4
   into a seed sweep: JSON manifest listing the character record (identity
   carrier file, expected gender, hair, distinguishing marks), the prompt,
   and a seed range. Queue N jobs via the ComfyUI API, extract one face
   crop per output, and score each with a face-embedding distance against
   the reference crops. Keep only takes under the failure threshold (calibrate
   the threshold from one known-good take, recorded in the manifest), and
   record the winning seed. fsocietyARG's "write the number somewhere"
   becomes the manifest.
2. **Log every take.** One JSONL row per generation: seed, identity carrier,
   reference video, output path, pass/fail with the failure mode quoted
   from the commenters ("poor facial likeness", "identity drift to a
   stranger", "mouth lag"). The log is what makes a week-old "which seed
   was it" question answerable.
3. **Automate the Lola consistency check.** Lola's rule is identity
   consistency across the whole shot: extract frames at the start, middle,
   and end of each take, compute face-embedding distances between them, and
   fail the take if the spread exceeds the calibrated threshold. One good
   frame is not a passing take.
4. **Gate the start frame before spending samples (Phase 6).** Before
   queueing the seed sweep, render one frame from the Qwen Image 2.1
   start-frame trick and verify pose and background against the source.
   If the start frame is wrong, no seed will fix it.
5. **Run the failure-mode decision tree as checks, not prose.** Encode the
   failure modes as ordered checks in the agent loop: identity drift to a
   stranger → check the identity carrier actually loads (wrong/blank
   sheet = stranger output); poor facial likeness → seed sweep continues;
   mouth/body lag → verify the reference-video latent injection (Phase 5)
   is wired before sampling; out-of-sync motion → re-run with the
   reference latent as the sampler input. Stop and report which check
   failed rather than burning seeds blindly.

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
