---
name: minimax-h3-storyboard-grid-reference
description: "Steer MiniMax H3 reference-to-video through complex scenes with a 2x2 storyboard grid: GPT image 2 generates four key-frame panels (start, two progress beats, end), the grid is supplied as a reference image in ComfyUI, and the prompt addresses it shot by shot (one panel = one full-frame shot, hard cuts, real-time speed). Includes the verbatim scene-17 prompt structure and the H3 Singularity two-pass settings. Trigger when MiniMax cannot follow a complex scene from a prompt or first/last frame alone."
---

# MiniMax H3 Storyboard-Grid Reference

## Purpose

This skill reconstructs the storyboard-grid workflow from the author's
post, step by step, so another agent can follow the same process. Every
phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The video's core method is:
when a scene is too complex for MiniMax to follow from a prompt (or
even first/last frame), give it a 2x2 storyboard grid as a reference
image and prompt it shot by shot, one panel per full-frame shot, with
hard cuts between them.

## Source

Creator: Cheap_Credit_3957. Reddit post:
https://www.reddit.com/r/comfyui/comments/1xfmo04/testing_out_a_2x2_storyboard_grid_with_minimax/
(r/comfyui post 1xfmo04, score 34, 25 comments) | 2026-10-27 scout run,
audit 2. Also https://youtu.be/uMIDASXblnA. The author is the creator
of the ComfyUI Video Builder (github.com/vrgamegirl19/comfyui-vrgamedevgirl);
the grids were used only for the story scenes of a music video, with
on-stage band performances done by normal reference-to-video. This is a
different workflow from the existing SelfLift, SyncTile, Chain Director,
SAM3, no-mask LoRA, and Reference-to-Video MiniMax H3 skills: none of
those use a multi-panel storyboard grid as the keyframe language.

## Tools used

**GPT image 2** (grid generation), **MiniMax H3** (reference-to-video),
**ComfyUI Video Builder** (assembly; grids mapped as reference images
like any other reference image).

## Phase 1: Generate the grid

**Do**
1. Identify the scenes MiniMax struggles with: complex scenes that it
   cannot follow with just a prompt, and where even first/last frame
   has issues.
2. Generate a 2x2 grid with GPT image 2: 4 panels showing how the scene
   should play out. Panel 1 (top left) is the starting frame, panel 4
   (bottom right) is the ending frame, and the two middle panels show
   how the scene progresses.
3. Use grids only for story scenes that need them: the author notes
   that creating all the grids takes quite a bit of time, so a whole
   video this way is a time cost to weigh.

**Check**
- The grid reads as four key frames of one scene in reading order
  (left to right, top to bottom), not as four separate images.

**Why**
- A grid is a keyframe language the video model can actually follow:
  it shows progression, not just endpoints, which is exactly what
  first/last frame cannot express for a multi-beat gag.

## Phase 2: Prompt the grid (reference order and shot language)

**Do**
1. Supply reference images in this order: (1) the singer's character
   sheet, (2) the 2x2 storyboard grid, (3) the location image. The
   author notes the character and location refs may not even be
   needed, and plans to test the grid alone next time.
2. Give the storyboard its own subject line listing the 4 key frames
   in reading order, one panel = one full-frame shot.
3. Hand staging to the storyboard in the location line: framing,
   camera angles, and positions "follow the storyboard key frames
   exactly".
4. Open Shot 1 with "The video opens exactly on the first storyboard
   panel".
5. Open every later shot with "Hard cut, exactly like the second
   storyboard panel (top right)" (and likewise for panels 3 and 4),
   then describe that panel.
6. Keep lyric cues inside the shots where she sings.
7. Put "Everything moves at normal real-time speed" in the summary,
   so thrown or falling things do not go slow motion.
8. Describe only what is in view.

**Check**
- Each shot recreates one panel's framing, camera angle, and poses as
  one single full-frame image, with hard cuts between shots, and the
  singer's appearance is preserved from the character reference.

**Why**
- The prompt structure is the technique, not the grid alone: the
  subject line makes the grid a shot list, the "hard cut, exactly
  like" phrasing makes each panel a separate shot, and the
  real-time-speed line stops the model from turning a gag into slow
  motion.

## Phase 3: Run it (settings) and judge it

**Do**
1. Map the grids as reference images in the ComfyUI Video Builder,
   like any other reference image.
2. Run MiniMax H3 Singularity: 25 steps on pass 1, then the 8-step
   768p turbo LoRA at 4 steps and 0.35 denoise on pass 2 with the
   latent upscale model.
3. Judge against the previous attempts: the author reports it
   "worked pretty well" on scenes MiniMax was really struggling with
   using normal reference images and prompts.

**Check**
- The worked example in the post (scene 17, the pearl necklace gag,
  7.6 seconds) plays as four shots: glance at the laughing woman,
  strand snapping with pearls spraying, pearls bouncing on the parquet
  among shoes, singer's palms-up shrug as guests gather pearls, with
  lyric sync at 0.36-1.88 s and 6.1-7.2 s.

**Why**
- The grid is a control method, not a quality guarantee: it buys
  shot-by-shot fidelity for complex scenes at the cost of grid
  generation time, and the author is explicit that the trade is only
  worth it for scenes the normal path cannot handle.

## The human method, distilled

1. **Grids for hard scenes only**: prompt-only and first/last frame
   fail on multi-beat scenes; a 2x2 grid shows progression.
2. **One panel = one full-frame shot**: subject line in reading order,
   "hard cut, exactly like" per shot, staging handed to the storyboard.
3. **Real-time speed is a line, not a hope**: state it in the summary
   or falling things go slow motion.
4. **Test whether the extra refs are needed**: the author suspects the
   grid alone may suffice, and says so rather than asserting it.

## Failure modes

- **Grid generation time**: a whole video this way costs significant
  grid-generation time; reserve grids for scenes the normal path
  cannot handle.
- **Untested grid-alone variant**: whether separate character and
  location refs are needed is explicitly untested; do not claim the
  grid alone works until it is tried.
- **Aesthetic preference is not failure**: the author prefers the
  on-stage performance scenes aesthetically; that is a taste note,
  not a grid-method failure.

**Depth status:** FULL (full post text including the verbatim scene-17
prompt, reference order, and model settings; no frames reviewed, and
the grid-alone test is explicitly unrun).
