---
name: minimax-h3-reference-video-character-swap
description: "Swap a character in video with MiniMax H3's Reference-to-Video workflow in ComfyUI: source footage supplies motion and performance, Krea 2 and Qwen Image supply the replacement character's references, no motion capture. Local on RTX 5070 Ti. Watch for smearing in fast motion and missing facial detail in wide shots. Trigger when replacing a performer in video without mocap, or when setting acceptance criteria for a character-swap take."
---

# MiniMax H3 Reference-to-Video Character Swap in ComfyUI

## Purpose

This audit reconstructs the workflow from the author's post and comments,
step by step, so another agent can follow the same process. Every phase
has three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The video's core method is: keep the
source video's motion and performance, replace the person and the
environment with AI-generated ones, no motion capture.

Variant note: this is the same tool as
`minimax-h3-character-swap-comfyui` (SAM3 + color-inversion masking) and
`minimax-h3-character-swap-nomask-lowvram`, but a different workflow:
Reference-to-Video with generated character references, not masked
repainting. Do not merge them; the failure modes and the reference
pipeline differ. It is also distinct from the SyncTile long-video and
SelfLift stitching recipes (different problem: one swap, not long-video
continuity).

## Source

Creator: Time-Ad-7720. Reddit post:
https://www.reddit.com/r/comfyui/comments/1xcxdz5/i_tried_ai_character_swapping_with_minimax_h3_in/
(r/comfyui post 1xcxdz5, score 79, 7 comments) | Tutorial + downloadable
workflow + assets (linked in the post; page itself not retrieved this
run, so no settings are claimed from it):
https://www.kaziahmed.net/kazitorials/minimax-character-swap | 2026-10-24
scout run.

## Tools used

Tools used: **ComfyUI**, **MiniMax H3 Reference-to-Video workflow**,
**Krea 2** and **Qwen Image** (character-reference generation). Local
hardware: **RTX 5070 Ti**.

## Phase 1: Pick the source and the replacement

**Do**
1. Take an existing video as the motion source.
2. Generate the replacement character's references with Krea 2 and Qwen
   Image (author's stated tools for this step).

**Check**
- The reference reads as the intended character before any video is
  generated; the source video's performance is the thing being preserved.

**Why**
- Motion source and likeness source stay separate: the source footage
  supplies movement, the generated references supply appearance. (Same
  split as the SAM3 character-swap skill, different mechanism.)

## Phase 2: Run Reference-to-Video in ComfyUI

**Do**
1. Run MiniMax H3's Reference-to-Video workflow in ComfyUI locally
   (author runs it on an RTX 5070 Ti).
2. Swap the character and, if wanted, the environment, while keeping the
   movements and performance from the source footage.
3. Iterate with prompt engineering and workflow adjustments (author's
   words: "Getting better results through prompt engineering and workflow
   adjustments").

**Check**
- The output keeps the source performance; the character and environment
  are the new ones. The author is explicit that this is still
  experimental: "Still experimenting with consistency, motion accuracy,
  and generation performance."

**Why**
- Author's stated goal: character animation and indie filmmaking without
  traditional animation or motion-capture pipelines.

## Phase 3: Watch for the two known failure modes

**Do**
1. Check fast-motion sections for smearing.
2. Check wide shots for facial detail loss.

**Check**
- Author, answering "What have your biggest challenges been?":
  "Smearing in fast motion, and lack of facial details in wide shots."
  (Verbatim; these are the author's own words, not a reviewer's.)

**Why**
- These two checks are the acceptance test for any take from this
  workflow until the author reports otherwise. They transfer directly
  into an intake acceptance spec: a character-swap take should be
  checked on exactly these two measurements.

## The human method, distilled

1. **No mocap setup required** (author's words): source footage is the
   motion capture.
2. **References are generated, not photographed**: Krea 2 + Qwen Image
   supply the character references.
3. **Iterate on prompts and workflow settings**, not on capture hardware.

## Failure modes

- **Smearing in fast motion** (author-reported).
- **Missing facial detail in wide shots** (author-reported).
- **Multi-person swaps are unanswered**: the thread's question ("Can you
  replace two fighting persons at the same time?") has only an unverified
  commenter claim in reply (see below), not an author-confirmed answer.

## Commenter claims (unverified, labeled)

- DaLyon92x claims a "brand new swap lora, facerefine second stage and
  supports up to 3 people in one render", "tested and verified at 16gb+
  vram", entered in a Comfy challenge. The creator has not tried it:
  "I haven't tried it yet, will check and report back."
- switch2stock suggests ComfyUI-MAINodes
  (github.com/matlowai/ComfyUI-MAINodes) "for fast paced" work. Same
  status: suggested, not creator-confirmed.

**Depth status:** PARTIAL (full post text + all 7 comments; the tutorial
page's workflow, assets, and settings were not retrieved, and the native
clip has no captions).

## AAA studio practice

Reference-to-video swapping is the low-budget cousin of a practice AAA/VFX houses run at full scale: keep the captured performance, replace the appearance, and supervise rather than re-animate. On The Irishman, ILM built Flux, which combined on-set HDRI and LIDAR capture to solve camera, lighting, and colour data and then deformed digital doubles frame by frame to match the captured performances, with no facial animator in the credits because the director did not want the performances changed; ILM additionally ran an AI Face Finder over a reference library of the actors at target ages as a sanity check on rendered shots. DNEG's Brahma division acquired Metaphysic (the team behind widely circulated AI face-swap demonstrations) to build a unified AI-driven content capability, and Pinscreen's neural-rendering face work was used for de-aging across multiple seasons of Manifest, where consistency over long-form storytelling, not a single good frame, was the requirement. The transferable discipline is the same in all three cases: the reference library is curated and permissioned, the source performance is never re-animated, and consistency is checked across a sequence, not a still.

- Source: https://thehollywoodfeature.com/how-ai-de-aging-digital-face-replacement-vfx-works/
- Source: https://vitrina.ai/blog/impact-of-ai-on-special-effects-in-film-tv/
- Source: https://fliphtml5.com/kolectiv/ulvm/ (Pinscreen/Manifest account; secondary summary, treat its figures as reported, not verified)

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Before generating, build a reference pack and freeze it: every reference image used, its generator (Krea 2 / Qwen Image), and the character traits it is meant to pin (face, hair, costume, proportions). A swap whose references change mid-iteration cannot be debugged.
2. Automate the two author-reported failure checks as a shot list, not a vibe check: extract frames from (a) the fastest-motion 2 seconds of the source and (b) the widest shot in the take, and inspect exactly those frames for smearing and facial-detail loss before accepting any take.
3. Log every take with: source clip, reference-pack version, prompt version, and pass/fail on both checks. A take without that row is not a candidate for delivery, however good it looks in a thumbnail.

**Check**
- Fast-motion frames: no smearing on hands, face, or costume edges.
- Wide-shot frames: facial detail still reads; if it does not, the take fails even if close-ups pass.
- Reference pack is versioned and unchanged between the accepted take and any re-render of it.

**Why**
- ILM's and DNEG's lesson is that appearance replacement is a sequence-consistency problem with a curated reference library, not a per-frame beauty problem. The two failure modes the author reports (smearing, wide-shot detail loss) are exactly where sequence consistency breaks first, so they become the automated gate.
