---
name: minimax-h3-character-swap-comfyui
description: "Swap a character in video with MiniMax H3 in ComfyUI: mask with SAM3 text prompts, invert colors inside the mask as the repaint signal, save characters as image-plus-description units, trim in-workflow, describe the finished result. RTX 4090, 3s at 0.8MP in ~2.5 minutes. Trigger when doing local AI character replacement or video inpainting."
---

# MiniMax H3 Character Swap in ComfyUI (SAM3 + Color-Inversion Masking)

## Purpose

This audit reconstructs the exact workflow from Pleasant-Living-3702's release
post and his answers across 33 comments, step by step, so another agent can
follow the same process. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle). The
workflow's core method is: describe the finished result, mask the who, invert
the mask, let the model repaint.

Variant note: this is the same tool as `resistance-sci-fi-short` (MiniMax H3)
and the same problem class as `konte-multishot-ai-video` (agentic multi-shot
AI video), but a different workflow — single-shot character replacement with
SAM3 + color-inversion masking, implemented as a ComfyUI workflow, not a
director-style short or a TypeScript DSL.

## Source

Creator: Pleasant-Living-3702 (simplified by the author from
https://civitai.red/models/2855941/minimax-h3-character-replacement)

Source: https://www.reddit.com/r/comfyui/comments/1wvff4i/super_simple_minimax_character_swap_workflow/
(native Reddit video; r/comfyui post 1wvff4i, score 146, 33 comments) |
2026-10-03 scout run. Workflow repo: https://github.com/BiggerFishy/comfyui-minimax-h3-studio
(MIT, GitHub zip; latest release adds a LoRA loader and an easier video trimmer).

## Tools used

Tools used: **ComfyUI** + **comfyui-minimax-h3-studio** workflow,
**SAM3** (text-prompted segmentation), **MiniMax H3** (video generation).

## Phase 1: Install and orient

**Do**
1. Install ComfyUI and load the comfyui-minimax-h3-studio workflow.
2. Find the main controls in the **green settings node in the middle**; the
   complicated nodes are tucked away.

**Check**
- Green settings node is visible and is where masking mode, seed, and
  megapixels live.

**Why**
- The author's design goal was plug-and-play: "I tried to make it as plug and
  play as possible." One node holds the controls a human actually touches.

## Phase 2: Save the character once

**Do**
1. Store a reference image together with a detailed character description as
   one saved unit.
2. Reload that unit whenever the character returns to a new video.

**Check**
- Switching back to an old character needs no retyping.

**Why**
- Author: "This is probably my favorite feature. Save a reference image
  together with a detailed character description, then load both again when
  you want to use that character in another video." Descriptions are the
  expensive part; caching them is the whole convenience.

## Phase 3: Trim the source video in-workflow

**Do**
1. Pick the section to edit with the built-in trimmer. Do not open an external
   editor.

**Check**
- The selected section is the only part that generates.

**Why**
- "The trimming UI could be fancier, but it works." Staying in one app keeps
  the loop tight.

## Phase 4: Mask the character with SAM3

**Do**
1. Choose a masking mode: **SAM3** (type a plain description such as "the man"
   or "the woman" into the sam3 prompt box), **Rectangle** (draw a box), or
   **No mask** (re-render the whole frame).

**Check**
- The sam3 prompt box contains a plain target description, e.g. "the man".

**Why**
- Explicit text masks beat flaky auto-description. The author tried it:
  "Originally the workflow used qwen with rules to describe the character and
  it also described the video. It worked sometimes and other times it sucked..
  I removed it because it took too long to describe the video." A Qwen
  auto-fill would need a genuinely good rule set, and "it would only know
  what you want in the sam3 box if there is only one character."

## Phase 5: Invert the mask, then generate

**Do**
1. Let the workflow **invert the colors inside the selected area before
   generation**.
2. Feed the source video (this guides mouth movements, body movement, and
   scene) and the reference image (this guides the replacement's appearance).
3. Use a character sheet as the reference when likeness is hard; the author:
   "I also found that using a character sheet is very useful."

**Check**
- The inverted-color region is exactly the character to replace; everything
  else is the motion/scene guide.

**Why**
- "This helps MiniMax replace the subject more consistently." Inversion is
  the mask made unmistakable to the model: an explicit "repaint here" signal.
  (Labelled: the author's conditioning trick, not a documented H3 feature.)

## Phase 6: Set generation parameters

**Do**
1. Start from the example settings: Seed **Fixed** for reproducibility, then
   switch Seed behavior to **Randomize** to explore variants.
2. Target megapixels: **0.8 MP** (the demo setting); try **1.0 MP** for higher
   resolution; the author does not usually go above that.
3. Leave everything else at defaults for the first run, then adjust.

**Check**
- Author's measured setup: **RTX 4090 (24 GB VRAM), 32 GB DDR5, 3-second
  video, 0.8 MP → about 2 minutes 30 seconds.**

**Why**
- Defaults-first is the fastest route to a first good take.

## Phase 7: Prompt for the finished result

**Do**
1. Write the video prompt as a description of the finished result, in detail.
   The author's working prompt: "A barn owl man wearing white polo shirt
   stands in the middle with feathers on his arms and neck, as women crowd
   around feeling him up and down."
2. Do not expect thin prompts to work: "swap the man in this video with a
   barn owl" will "probably not result in a decent gen."

**Check**
- Author's principle: "in my workflow its important to describe the finished
  result." Detailed prompts produce better results; "matching the seed
  doesn't guarantee an identical result on every setup."

**Why**
- The model fills what the prompt leaves vague; finished-result description
  is the control surface. (The author even tested the degenerate case — video
  prompt only, "the man" in the sam3 box — and "got basically the same
  result", but does not recommend relying on it.)

## The human method, distilled

1. **Mask the who, invert it, repaint.** SAM3 finds the person; color
   inversion marks the repaint zone unmistakably.
2. **Describe the finished result**, not the edit.
3. **Save characters, not prompts.** Image + description cached as a unit.
4. **Resolution is a quality lever, not a speed lever.** Cropping at the same
   0.8 MP concentrates detail on the character but makes clean re-blending
   hard; "using a high quality (resolution) video will give you back just as
   high as a resolution result already though."
5. **Expect failures; iterate.** "None of these modes are perfect. It may take
   a few attempts."

## Failure modes

- **Transitions and effects wash out.** On a TikTok multi-clip edit, "the
  edits transitions and effects like blurs and filters and flashes kinda went
  away but the character themselves stayed practically the same"; detailed
  prompts preserve them better.
- **OOM on long videos.** A 4070 Ti user runs a looping system for longer
  clips (30–40 s before OOM, 64 GB system RAM doing the caching) with a
  reusable prompt: "Replace only the original performer in <Video 1> with
  <Subject 1>. <Subject 1> is the person shown in <Picture 1> and
  <Picture 2>. <Picture 1> supplies face and identity details. <Picture 2>
  supplies full-body appearance."
- **Qwen auto-description was hit-or-miss and slow** — removed from the
  workflow; do not re-add without a solid rule set.

## AAA studio practice

How AAA film VFX does the same thing (replace the performer, keep the
motion and scene), and what to borrow.

1. **ILM FaceSwap on *Indiana Jones and the Dial of Destiny* (2023).** ILM's
   biggest de-aging project: ~100 VFX artists, 3 years, to take Harrison
   Ford from 80 to 42 for a 25-minute sequence. The pipeline: Flux, a
   proprietary system with two infrared cameras riding either side of the
   main camera; Medusa, ILM and DisneyResearch|Studios' facial-capture rig
   that reconstructs the face in full motion; a FACS expression library
   recorded from Ford as the base; machine-learning reference material from
   previous Indiana Jones films. Director James Mangold: "I could shoot
   Harrison on a Monday ... and I could see dailies by Wednesday with his
   head already replaced." The AAA form of this skill's save-the-character-
   once unit is a full expression and lighting library per performer; the
   AAA form of the trimmer + generation loop is a 2-day dailies turnaround
   per shot.
   - Source: https://80.lv/articles/see-how-industrial-light-magic-made-harrison-ford-40-years-younger?amp=1
2. **The Mandalorian's Luke: deepfake + Lola VFX 2.5D.** Jon Favreau: the
   deepfake analysis of Mark Hamill footage built "a library of expressions,
   faces, looks, and lighting scenarios" that the AI superimposed over the
   physical performer's corresponding expressions; body double Max
   Lloyd-Jones performed the movement; Lola VFX's 2.5D de-aging blended the
   performances; Hamill was also filmed in "The Egg," a lighting rig that
   captured ultra-high-res face textures with controlled lighting. Two
   lessons for this skill: (a) the reference library covers expressions AND
   lighting, not just identity; (b) the motion source and the likeness
   source stay separate all the way through, exactly like this skill's
   source-video-guides-motion / reference-image-guides-appearance split.
   - Source: https://screenrant.com/mandalorian-luke-mark-hamill-deaged-technology-deepfake-explained/
3. **AAA is hiring for exactly this ML discipline.** ILM hired YouTuber
   Shamook (2021) for his deepfake research after his video improved the
   Mandalorian Luke shot; ILM's statement: "Over the past several years ILM
   has been investing in both machine learning and A.I. as a means to
   produce compelling visual effects work." Community-developed face-swap
   tooling is on the AAA hiring track, which is where workflows like this
   skill are heading.
   - Source: https://www.thewrap.com/lucasfilms-ilm-hires-youtuber-who-improved-cgi-luke-in-the-mandalorian/

### Agent-executable automation upgrades (from AAA practice)

- **Character unit as a structured record.** Save the reference image +
  description with a JSON sidecar (character_id, lighting notes, expression
  range, prompt that produced the best take), mirroring ILM's
  expression-and-lighting library; the agent picks the right reference per
  shot from the sidecar instead of hand-picking files.
- **Per-take parameter log.** Log seed, megapixels, mask mode, and prompt
  per take in JSON (the dailies discipline); the agent reproduces or varies
  takes from the log without re-typing.
- **Mask verification before generation.** Render the inverted-color mask
  preview and have the agent assert the masked region matches the SAM3
  target (e.g. bounding-box overlap against the segmentation) before
  spending the generation; the AAA form is tracking verification before
  the expensive face-swap pass.
- **Failure modes as an executable decision tree.** Encode this skill's
  failure modes: if the source has transitions/effects, raise prompt detail
  on effects first; if the clip exceeds the OOM threshold (30-40 s on
  4070 Ti-class), auto-split into looping chunks with cached prompts. Run
  the tree before the first generation, not after the first failure.

**Depth status:** FULL (full post text + 33 comments with quoted settings,
benchmarks, and failure reports; no transcript exists for native Reddit video).
