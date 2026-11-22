---
name: minimax-h3-image-ausboss-16mp-edit-lock
description: "Put up to six characters from separate photos into one 16 MP picture with MiniMax H3 Image in ComfyUI using the AusBoss Generate + Edit v1.2 workflow: name each reference left to right, run it big, blind-test at each model's own size, and edit with Edit Lock so untouched pixels are restored, not redrawn. Trigger when a multi-reference H3 Image edit must hold identities apart at high resolution."
---

# MiniMax H3 Image: AusBoss 16 MP Multi-Character Edit + Edit Lock

## Purpose

This skill reconstructs AuzBoss's workflow for putting six characters from six photos into one 16 megapixel picture with MiniMax H3 Image in ComfyUI, including the blind test against Qwen Image 2.1 and FLUX 3 Klein and the Edit Lock mechanism that keeps edits from redrawing the untouched picture. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: run it big, name who stays, and measure honestly.

This is a variant skill: same model as `minimax-h3-image-native-comfyui` (official native ComfyUI support), different workflow (AusBoss Generate + Edit v1.2, AusBoss node pack, Edit Lock, 16 MP composition + blind test). Do not confuse the two; the native skill covers the official t2i/edit templates, this one covers the AusBoss workflow and its measurements.

## Source

- Post: "I put six characters from six photos into one 16 MP picture with MiniMax H3 Image in ComfyUI. Here is what worked and where it fell apart" by AuzBoss — https://www.reddit.com/r/comfyui/comments/1y1buim/i_put_six_characters_from_six_photos_into_one_16/ (r/comfyui post 1y1buim, score 47, 4 comments)
- Video: "I put 6 characters in one 16 megapixel picture: MiniMax H3 Image in ComfyUI" by AusBoss — https://youtu.be/GTjyJNgIG6Q (captions/metadata extraction returned metadata only; media download blocked by YouTube's bot sign-in wall, not retried; no transcript lines are quoted from the video)
- Workflow: Generate + Edit, v1.2 — https://civitai.com/models/3046048 (also on the author's Discord: https://discord.gg/RwVxY9Fuaj)
- Evidence: full post selftext + author/commenter comments, 2026-11-22 scout run, audit 4.

## Tools used

MiniMax H3 Image (open weights, 33B, 6 steps, no CFG), ComfyUI 0.45 or newer, ComfyUI-AusBoss node pack (search "AusBoss" in Manager; the author's workflows "just use core nodes and my nodes", no 30 node packs). Comparison models: Qwen Image 2.1, FLUX 3 Klein. Hardware for all timings: RTX 5090.

## Phase 1: Compose six references in one pass at 16 MP

**Do**
1. Take six game characters, each from their own photo, and generate one picture with all six on one couch, in one pass at 16 MP.
2. In the prompt, name each picture, say who stands where from left to right, and tell the model each one keeps their own face, hair, and outfit.

**Check**
- Six held up for the author; nine was too many: "faces and outfits started drifting". Six is the author's measured limit on this workflow, not a model specification; test your own count before promising more.

**Why**
Naming + left-to-right ordering + per-person keep instructions is what separates identities that would otherwise bleed into each other (hair or accessories swapping between characters, the exact failure commenter AppropriateFig3632 asks about).

## Phase 2: Blind-test against the rivals at their own sizes, then at a fixed size

**Do**
1. Run a blind test against Qwen Image 2.1 and FLUX 3 Klein: ten edits on two seeds, each model at the size its own workflow ships with.
2. Score: Qwen 32, Klein 32, H3 31 out of 40 ("about even", author).
3. Re-run held to 1 MP: H3 last (25), Klein first (34). State the conclusion the author states: "the size matters a lot"; H3 "is not meant for lower mp".

**Check**
- Every comparison carries its size. A comparison that omits size is invalid for this model: the same model ranks differently at native size vs 1 MP. The commenter GrungeWerX's complaint about other creators applies here: comparing "low mp h3-image to other models when the hf/gh all clearly state its meant for higher mp" measures the wrong thing.

**Why**
A blind test with fixed edits and fixed seeds, scored, turns "H3 feels good at 16 MP" into evidence. The size split is the finding: H3's advantage is resolution + references, not raw edit quality at small sizes.

## Phase 3: Measure speed at the size you actually run

**Do**
1. At 16 MP, H3 takes about 40 seconds an edit, about 24 seconds with the Fast switch (a 2-step LoRA).
2. On the same edits, Klein took about 4 seconds and Qwen about 19 seconds, "but those are 1 to 2 MP pictures".

**Check**
- Speed claims carry their resolution. 40 s at 16 MP vs 4 s at 1-2 MP is not a 10x speed gap; it is a different job at a different size.

**Why**
The author's honest take follows from the numbers: "as an edit model on its own I would still use Qwen or Klein for quick little edits. Where H3 is different is the 16 MP size and the reference pictures." Use the fast model for quick small edits; use H3 when the job is big and multi-reference.

## Phase 4: Edit with Edit Lock so the untouched picture is restored, not redrawn

**Do**
1. Install the AusBoss node pack and use the Generate + Edit v1.2 workflow (Civitai link above; ComfyUI 0.45+).
2. For edits, use Edit Lock (author comment): stock ComfyUI "can't do it" — an edit model redraws the whole picture, so untouched parts "come back slightly zoomed, shifted and tinted pink". Edit Lock "checks the model's work at each step. anywhere that isn't really changing, it puts your original back, so only the part you're editing gets redrawn. after the decode, a second node pastes your exact pixels back and takes out the tint. no mask needed."
3. Pair Edit Lock with the "say who stays" habit: explicitly name who stays unchanged (author's example: "keep the other two people"), which took the author's test "from 1 of 12 to 12 of 12".

**Check**
- Unchanged regions return as the exact original pixels (post-decode paste), without zoom, shift, or pink tint, and without a mask. If an unchanged region drifts, Edit Lock is not wired in; the workflow is falling back to a full redraw.

**Why**
Regenerating everything guarantees drift in parts the user never asked to change. Restoring the original at each step and pasting exact pixels back after decode removes that drift by construction. No mask is needed because the check is "is this really changing", not "is this inside a painted region".

## Phase 5: Heed the license warning and the failure modes before using it

**Do**
1. Read MiniMax's terms first if in the US, EU, UK, or South Korea: the author states "MiniMax's license leaves out the US, the EU, the UK and South Korea. If you are in one of those, read their terms first."
2. Expect the stated failure modes: at 1 MP, a car removal moved the whole picture; at 16 MP on the same seed "the car went and 2 percent moved" (another seed at 16 MP still left the car in). Small faces and fine texture come out soft.

**Check**
- License: this is the author's statement about the license, not a legal review. Verify the current terms before commercial use; a workflow that cannot legally run where the user works is not a workflow for that user.
- Failures: judge edits seed by seed. A failure on one seed does not prove the prompt is wrong, and a success on one seed does not prove it is robust; the author's car-removal result changed across seeds at the same size.

**Why**
License scope and seed variance are both decided before the first paid job, not discovered during it. The blind test in Phase 2 exists to make both visible: it uses two seeds, and the author reports the seed that failed alongside the seed that worked.

## The human method, distilled

1. **Name who stays.** "Keep the other two people" fixed 1-of-12 to 12-of-12; identity preservation is a prompt instruction, not luck.
2. **Run it big.** H3's advantage lives at 16 MP; judging it at 1 MP measures the wrong thing.
3. **Blind-test at each model's own size, then at a fixed size.** Both splits are needed; either alone misleads.
4. **Preserve the untouched picture.** Edit Lock restores original pixels per step and pastes them back after decode; no mask, no drift.
5. **State the failure modes with the wins.** Nine people drift; small faces come out soft; results vary by seed; the license excludes the US, EU, UK, and South Korea per the author.

## Depth status

DEPTH-LIMITED (video) — the video could not be captioned or downloaded (bot wall, one attempt, no retry). The workflow is reconstructable from the author's unusually complete post text (benchmarks, speeds, workflow link, license warning) plus the author's comment stating the Edit Lock mechanism. What a media download would add: on-screen workflow steps and any parameters not in the post. No parameters were invented; all numbers above are author-stated for the RTX 5090.
