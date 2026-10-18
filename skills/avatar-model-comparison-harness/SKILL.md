---
name: "avatar_model_comparison_harness"
description: "Evaluate lip-synced AI avatar models with a fixed-input comparison harness: same portrait plus same driving audio, one fixed prompt template, a persistent reference cell, per-cell setting labels, natural-speed full-result judging, and a named failure-mode taxonomy. Reconstructs SECourses' 38-test comparison (MiniMax H3, CodeFormer, AvatarForever, LongCat, Wan 2.2, HuMo and 10 more) across 8 panels. Trigger when benchmarking AI avatar/video models or writing an AI-vendor acceptance spec."
---

# Avatar Model Comparison Harness

## Purpose

This skill reconstructs the evaluation workflow from SECourses' "38 AI Avatar
Tests Compared: MiniMax H3 + CodeFormer, LongCat & AvatarForever" (YouTube,
72 s, r/comfyui post 1x2dxbz, 2026-10-11 scout run), step by step, so another
agent can run the same comparison on any set of avatar models. Every phase
has three parts: **Do** (the action), **Check** (how the human verifies it),
and **Why** (the principle). The workflow's core method is: fix the input
and the prompt, vary one thing at a time, judge at natural speed, name the
failure modes.

Variant note: this is NOT a generation workflow. The three existing
`minimax-h3-*` skills cover generation (character-swap with/without masking,
SelfLift long-video stitching). This skill is the evaluation harness that
decides which model/settings to use in the first place, and it doubles as a
template for AI-vendor acceptance records.

## Source

Creator: SECourses. Video: https://www.youtube.com/watch?v=aOM_YEiskLg
(72 s, 12 frames reviewed; no captions exist, so every parameter below is
read off the on-screen labels). Reddit thread:
https://www.reddit.com/r/comfyui/comments/1x2dxbz/ ("I have tested 13 AI
models and 38 different pipelines to generate lip synced AI avatars"),
6 comments. Presets ship in the author's ComfyUI ZIP as
"MiniMax H3 Lip Synch - Audio + Text Image or Video - Turbo 4 Steps
832x1248 - 261001.json" and "AvatarForever Unified Image or Text + Audio To
Long Video - 260920.json".

## Tools used

Evaluation harness (tool-agnostic). Models compared in the source run:
**MiniMax H3** (+ Turbo variant), **CodeFormer** (mouth restoration
post-pass), **AvatarForever** (Unified Image or Text + Audio To Long Video),
**LongCat Avatar 1.5** (distilled + full), **InfiniteTalk**,
**SoulX-FlashTalk 14B**, **SoulX-FlashHead Pro**, **TalkingAvatar 2.0**
(Neosapience), **LTX-2.5**, **LiveAvatar**, **EchoMimic V3 Flash Pro**,
**OmniAvatar 14B**, **Wan 2.2 Speech to Video**, **LatentSync 1.6**,
**HighSync**, **HuMo**.

## Phase 1: Fix the test inputs

**Do**
1. Choose ONE portrait image and ONE driving audio clip. Use them for every
   test without exception.
2. Write ONE prompt template and reuse it verbatim. The source template:
   `'man with glasses in a library office, 8s talking head, natural mouth
   movement, realistic skin, 0.9 / 0.7'` (0.9 = mouth-restoration fidelity,
   0.7 = blend, per the author's "OUR REFERENCE" label).
3. Judge at natural playback speed, full result, face detail visible. Do not
   slow down, do not crop to the mouth.

**Check**
- Swapping any input between runs is forbidden. If the prompt changes, the
  comparison restarts.

**Why**
Fixed inputs isolate the model and its settings as the only variable. The
source's on-screen banner states the contract: "Same portrait + driving
audio | Natural-speed playback | Full result + face detail".

## Phase 2: Anchor every panel with a reference cell

**Do**
1. Pick one configuration as "OUR REFERENCE" and put it in the top-left
   cell of every panel. Source reference: MiniMax H3 + CodeFormer, mouth
   restoration, fidelity 0.9 / blend 0.7, 832 x 1248 at 24 fps.
2. Keep the reference byte-identical across panels (re-run, do not copy the
   file, so generation variance is visible if it exists).

**Check**
- A viewer can compare any cell against the same anchor without scrolling.

**Why**
A persistent reference turns N separate tests into one comparable grid.
Without the anchor, drift between panels is invisible and every cell is
judged in a vacuum.

## Phase 3: Label every cell with its exact settings

**Do**
1. Every grid cell carries a text label: model name, variant, sampling
   steps, restoration on/off, resolution, fps. Examples from the source:
   "AvatarForever | 8-step generation | Available in our ComfyUI ZIP",
   "LongCat Avatar 1.5 | Distilled model | Original output | 832 x 1248 |
   25 fps", "LTX-2.5 | Two-pass generation | Start/end frame guidance".
2. Group cells into themed panels with a header stating the theme:
   "01 / 08 | With mouth restoration", "02 / 08 | Original model outputs",
   "03 / 08 | LTX-2.5 and LiveAvatar", "04 / 08 | MiniMax H3 generation
   settings", "05 / 08 | Lip-sync refiners and reference images",
   "06 / 08 | More avatar models", "07 / 08 | Wan 2.2 and reference-image
   variants", "08 / 08 | First-sentence samples".

**Check**
- Any cell's settings can be read without leaving the grid.

**Why**
The label IS the experiment record. A grid of unlabeled videos is a demo;
a grid of labeled videos is a dataset you can act on.

## Phase 4: Sweep the model space

**Do**
1. With mouth restoration (source panel 01): AvatarForever 8-step; LongCat
   Avatar 1.5 distilled; InfiniteTalk 8 steps (512 x 768, 25 fps);
   SoulX-FlashTalk 14B (416 x 720, 25 fps); TalkingAvatar 2.0, source aspect
   ratio.
2. Original outputs, no restoration (source panel 02): LongCat Avatar 1.5
   distilled vs full model at 20 sampling steps; InfiniteTalk 8 steps;
   SoulX-FlashTalk 14B; TalkingAvatar 2.0 at 30 steps.
3. Guided vs unguided (source panel 03): LTX-2.5 two-pass with start/end
   frame guidance vs without; LTX-2.5 4 sampling steps native-resolution;
   spoken words included in the prompt as a variable; LiveAvatar 4-step
   audio-driven (384 x 576, 25 fps).
4. More models (source panel 06): EchoMimic V3 Flash Pro audio-driven
   portrait (624 x 928, 25 fps); OmniAvatar 14B audio-driven portrait
   (400 x 720, 25 fps); SoulX-FlashHead Pro talking-head (512 x 512,
   25 fps); TalkingAvatar 2.0 default portrait at 30 steps vs with
   CodeFormer mouth restoration (480 x 832, 25 fps).
5. Reference-image variants (source panel 07): Wan 2.2 Speech to Video
   20 steps original vs CodeFormer restoration (512 x 768, 16 fps, 8.81 s,
   last frame held); MiniMax H3 with TWO reference images; AvatarForever
   4-step; LongCat Avatar 1.5 distilled + CodeFormer.
6. First-sentence samples (source panel 08): HuMo multimodal at 30 steps in
   two resolutions (512 x 768 and 736 x 1104, 25 fps, 2.44 s, last frame
   held); LongCat Avatar 1.5 with a minimal-expression prompt; Wan 2.2 at
   768 x 1152, 16 fps, 2.31 s; AvatarForever 4-step.

**Check**
- One variable changes per cell against its panel neighbors.

**Why**
A model sweep answers "which tool"; a settings sweep answers "which
configuration of the tool". You need both before you can write a
recommendation.

## Phase 5: Sweep the reference model's settings (the cost curve)

**Do**
1. MiniMax H3 Turbo at 4 sampling steps (original output), 8 steps, and 8
   steps alternate generation, all at 832 x 1248, 24 fps.
2. MiniMax H3 (non-turbo) at 95 sampling steps with turbo acceleration
   disabled, same resolution.
3. Read the cost curve: the 4-step turbo is the author's shipped preset;
   the 95-step run shows where extra steps stop paying.

**Check**
- Resolution and fps identical; only steps and acceleration vary.

**Why**
Settings matter as much as model choice. One model at five settings is five
different tools, and the cheapest acceptable setting is the one you ship.

## Phase 6: Test the refiner passes separately

**Do**
1. Base + CodeFormer mouth restoration at 4 steps (turbo).
2. Base + **LatentSync 1.6** additional lip-sync pass at guidance strength
   3, then again at 1.5.
3. Base + **HighSync** additional lip-sync pass at guidance strength 3.5.
4. Base with single-reference generation at 8 steps (no refiner).

**Check**
- The refiner panels show the same base output with the extra pass as the
  only change.

**Why**
Lip-sync quality is separable from generation quality. A cheap base model
plus a good refiner can beat an expensive base model with no refiner, so
test the refiner as its own variable.

## Phase 7: Record the failure modes, not just the winners

**Do**
1. Name every failure you see, in the cell label or a notes column:
   - Two reference images in MiniMax H3 produce **visible ghosting**.
   - Short generations hold the last frame (Wan 2.2 8.81 s, HuMo 2.44 s);
     flag "last frame held" as a duration cheat.
   - H3-class models have a ~15 s length ceiling; longer needs 5 s clips
     plus an extend workflow (source thread:
     mini_video_editor_timeline_node_for_h3_extend).
   - AvatarForever "can make even 5 minute video" (commenter CeFurkan) but
     best quality is on shorter clips.
2. State the honesty line on the record: "not a simple comparison, not an
   unbiased ranking" (the source's on-screen footer). Ship the prompts and
   presets instead of claiming objectivity.

**Check**
- The failure list is as long as it needs to be; a comparison with no
  failures named is a commercial.

**Why**
Failure modes are what an acceptance spec is made of. "What good means" is
defined by which failures are unacceptable.

## The human method, distilled

1. "Same portrait + driving audio. Natural-speed playback. Full result +
   face detail." (source banner, all panels)
2. Fix the prompt template and reuse it verbatim; the 0.9/0.7-style
   fidelity/blend values are part of the template.
3. Anchor every panel with the same reference cell.
4. Label every cell with exact settings; the label is the experiment record.
5. Sweep models, then sweep the winner's settings (the cost curve), then
   test refiners as their own variable.
6. Name the failure modes; state the honesty line; ship the reproduction
   presets.

## Acceptance-spec transfer

This harness is the field-tested shape of an AI-vendor acceptance spec:
fixed seed inputs + fixed prompt + fixed judging criteria + named failure
modes + shipped reproduction artifacts. To adapt it for a game-asset intake
(Aegis intake/, Solarempire Meshy inputs): replace the portrait/audio with
a fixed seed asset (concept image + generation prompt), keep the reference
cell, the per-cell setting labels, and the failure-mode list. The output is
an acceptance record, not an opinion.

**Depth status:** FULL (12-frame review of a labeled grid; no captions
exist and the sandbox cannot run local transcription, but the frames carry
all parameters). Inferences are labeled. Nothing invented.
