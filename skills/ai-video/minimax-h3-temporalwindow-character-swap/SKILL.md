---
name: minimax-h3-temporalwindow-character-swap
description: "Swap a character in long MiniMax H3 clips in ComfyUI: cut into 4-6 s segments at 1080p, keep the reference alive with TemporalWindow overlapping windows and 22-frame context continuation, stack Spark-H3 sparse attention, Spectrum forecast caching, and lightx2v turbo LoRAs, and let the h3-motion-transfer agent skill write prompts per segment and batch-run the clips. 64 s in 15 segments at 6-10 minutes each at 2.0 MP. Trigger when a character swap must survive a long clip without the reference dropping off."
---

# MiniMax H3 Character Swap for Long Clips (TemporalWindow + Agent Skill)

## Purpose

This skill reconstructs the exact workflow from wjc_5's MiniMax H3
character-swap post and tutorial, step by step, so another agent can follow
the same process. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle). The
workflow's core method is: split long clips into short segments, keep the
character reference alive across segments with overlapping windows and
context frames, and stack cheap accelerators because character swap is a
narrow task.

Variant note: this is the same tool as
`minimax-h3-character-swap-comfyui` (SAM3 + color-inversion masking,
BiggerFishy) and the same problem class as `minimax-h3-selflift-long-video`
and `minimax-h3-synctile-long-video`, but a different workflow — long-clip
segmentation with TemporalWindow + Spark-H3 + Spectrum + split SelfLift +
an agent skill that writes prompts per segment, instead of single-shot
masking. Use this skill when the clip is long; use the SAM3 skill when it is
a single short shot.

## Source

Creator: wjc_5.

Source: https://www.reddit.com/r/comfyui/comments/1xqqhxh/minimax_h3_best_remix_tool_friendly_ultrafast/
(r/comfyui post 1xqqhxh, score 97, 5 comments) | 2026-11-08 scout run.
Tutorial video: https://youtu.be/4u1gw8Swt1s (782 s, uploader jingchen573,
no captions; media downloaded this run, 12 frames reviewed).
Workflow (RunningHub): https://www.runninghub.ai/post/2117441641207402497
Agent skill: https://github.com/wjc573/h3-motion-transfer
Character Swap LoRA: https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA
Spark-H3: https://github.com/zechengtang/Spark-H3
Spectrum: https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3
TemporalWindow / SpatialTiles:
https://github.com/mo-akkakk/ComfyUI-MiniMaxH3-TemporalWindow-SpatialTiles
SelfLift Split: https://github.com/wjc573/ComfyUI-SelfLift-Split

## Tools used

Tools used: **ComfyUI**, **MiniMax H3**, **Spark-H3** (sparse attention),
**Spectrum** (forecast caching), **TemporalWindow / SpatialTiles**,
**split SelfLift**, **lightx2v Ref2VA turbo v0.1** LoRA at 1.0 + **600-step
EMA turbo LoRA** at 0.5, **akatz-ai Character Swap LoRA**,
**h3-motion-transfer agent skill** (Hermes, Claude Code, Codex).

Frame-verified node names from the downloaded tutorial: "MiniMax H3 Spark
Attention (Auto / Pinned)", "MiniMax H3 Temporal Window & Spatial Tiles",
"MiniMax H3 Low VRAM...", "MiniMax H3 CharacterSwap", "MiniMax H3 Memory
Efficient Attention", "MiniMax H3 Reference to Video", "Load LoRA",
"Load Diffusion Model", "Load CLIP". Frame-verified subtitle: "at 0.5
strength, and the softness goes away." Frame-verified editor shot: segment
stitching with the subtitle "When you want a seamless join within one shot,".

## Phase 1: Pad and frame-align the clip

**Do**
1. H3 needs a 17n+5 frame length, so pad the source clip with its last
   frame, then trim the padding (and any context guide frames) before saving.
2. Output is 24 fps and exactly as long as the input clip.

**Check**
- Output length equals input length at 24 fps; no drift from the padding.

**Why**
- The model has a fixed frame-length arithmetic; padding absorbs it so the
  editor never sees a length change. (Author's rule, stated in the post.)

## Phase 2: Cut long clips into segments

**Do**
1. 720p (target 0.9-1.0 MP): up to about 15 s in one pass with
   TemporalWindow. Leave the window length at 6.5 s; it is per window, not
   the total length.
2. 1080p (2.0 MP): cut long videos into 4-6 s segments. Cut at natural shot
   changes and run those independently with the same character references.
3. If one shot has to be split, turn on the context switch and load the
   previous segment's output: its last 22 frames guide the start of the new
   segment, so the seam lines up.

**Check**
- The Trouble Maker stage clip in the video is 64 s, cut into 15 segments of
  about 4-6 s each. At 2.0 MP each segment took about 6-10 minutes.
- Clips cut at natural shot changes need no context; same-shot splits do.

**Why**
- Two problems motivated the split: "video references are slow, and on long
  clips the model loses the reference in the later part." Short segments
  keep the reference fresh; context frames keep the seam invisible.
  (Author's stated problems.)

## Phase 3: Stack the accelerators

**Do**
1. Enable Spark-H3 sparse attention (recent versions optimize video
   references, which fits character swap well).
2. Enable Spectrum forecast caching.
3. For speed LoRAs: lightx2v Ref2VA turbo v0.1 at 1.0 plus the 600-step EMA
   turbo LoRA at 0.5. v0.1 alone looks less greasy than v1.1 but a bit soft;
   adding the EMA LoRA fixes the softness and holds up better in motion.
4. Add akatz-ai's Character Swap LoRA to the chain.
5. Spark-H3 needs an NVIDIA RTX 30/40/50 card. If the GPU doesn't support
   Spark, Sage, or Spectrum, replace or bypass them.

**Check**
- Frame-verified: the tutorial's ComfyUI graph shows "MiniMax H3 Spark
  Attention (Auto / Pinned)" and Load LoRA nodes; subtitle confirms "at 0.5
  strength, and the softness goes away."
- The author would not stack this many accelerators for normal generation:
  "character swap is a narrow, well-defined task, so sparse attention and
  forecast caching don't cost much quality here."

**Why**
- Narrow task, cheap acceleration: the quality risk of stacking accelerators
  is bounded because the job (replace this person, keep everything else) is
  tightly defined. (Author's stated principle.)

## Phase 4: Sample in overlapping windows with split SelfLift

**Do**
1. TemporalWindow samples the clip in overlapping windows, which cuts down
   on the reference dropping off late in the clip.
2. Use the split version of SelfLift, so the low-res pass and the high-res
   refine are separate nodes that work with TemporalWindow.
3. Leave spatial tiles off in TemporalWindow; the split SelfLift nodes don't
   support it.

**Check**
- Frame-verified: the graph shows "MiniMax H3 Temporal Window & Spatial
  Tiles" as a node.
- The reference holds through the later part of long clips instead of
  dropping off (the second of the author's two motivating problems).

**Why**
- Overlapping windows re-anchor the reference repeatedly; split SelfLift
  keeps the low-res/high-res passes compatible with the windowing. (Author's
  stated mechanism.)

## Phase 5: Write prompts per segment with the agent skill

**Do**
1. For simple single-shot clips, a web LLM that can watch video is enough:
   give Gemini the prompt template, the character sheets, and the clip, tell
   it who replaces whom, and paste the output into the prompt box. Load the
   images in the workflow in the same order they were uploaded.
2. For clips with lots of cuts, use the h3-motion-transfer skill: name clips
   1, 2, 3 to run independently, or 2-1, 2-2, 2-3 so that 2-2 continues
   from 2-1's output. Point it at the folder and say who becomes which
   character. It detects hard cuts locally, writes a prompt per segment,
   shows the first one, runs everything in order (resumable if interrupted),
   then stitches the result with a side-by-side comparison and a
   per-segment check report.
3. It runs on RunningHub (CN or international site) or local ComfyUI; on
   RunningHub it uses 2.0 MP, so keep segments around 4-6 s. Built for
   Hermes; other agents (Claude Code, Codex) can use it by reading SKILL.md
   in the repo.

**Check**
- The skill shows the first prompt before running; the run is resumable;
  the final output includes the side-by-side comparison and per-segment
  check report.

**Why**
- Prompt-per-segment is the only way to keep a multi-cut clip coherent: one
  prompt for the whole clip cannot track who is where after every cut.
  (Inference, labeled: the author describes the mechanism, not this
  principle.)

## The human method, distilled

1. **Cut long videos sensibly.** Segments of 4-6 s at 1080p, 15 s max at
   720p; cut at shot changes, use context only for forced splits.
2. **Re-anchor the reference.** Overlapping windows plus 22 context frames
   stop late-clip reference loss.
3. **Stack accelerators only for narrow tasks.** Spark-H3 + Spectrum + turbo
   LoRAs are justified because character swap is tightly defined.
4. **Let the agent write prompts per segment.** One prompt per segment, first
   one shown, resumable runs, check report at the end.
5. **Watch the full tutorial before starting.** The author's own warning:
   follow the video along with the workflow "to avoid common mistakes."

## Failure modes

- **Reference drops off late in long clips** if run in one pass without
  TemporalWindow; fixed by overlapping windows (Phase 4).
- **Softness from v0.1 alone**; fixed by adding the 600-step EMA turbo LoRA
  at 0.5.
- **Spark/Sage/Spectrum unsupported on non-RTX-30/40/50 GPUs**; replace or
  bypass them (required on non-NVIDIA GPUs).
- **Spatial tiles break split SelfLift**; leave them off.

**Depth status:** FULL (full author post text + 5 comments + tutorial video
description + 12 frames from a downloaded copy with verified node names and
subtitles; no captions exist, and local transcription is unavailable in the
sandbox by design).
