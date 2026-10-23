---
name: ue58-gradient-animated-materials
description: "Build four gradient-driven animated materials in Unreal Engine 5.8's Material Editor (matrix-code streaks, dissolve-swap between two textures, glow-with-transition, gradient wipe) from one author-supplied gradient texture pack, with TextureSample-driven graphs and a loop-point check. Reconstructs Chapter 9 of Enrique Ventura's Materials Masterclass. Trigger when animating materials cheaply without flipbooks, Niagara, or sequencer tracks."
---

# UE 5.8 Gradient-Driven Animated Materials

## Purpose

This skill reconstructs the exact workflow from Chapter 9 ("Animation using
gradients") of Enrique Ventura's Unreal 5.8 Materials Masterclass, step by
step, so another agent can build the same four effects. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The chapter's core method is: one primitive
(a gradient texture), four shipping effects, one fixed texture pack.

Variant note: this is NOT the Chapter 8 video-in-materials recipe (Media
Player / File Media Source / SubUV flipbook). That is a separate skill. This
chapter uses gradients as the animation source instead of video.

## Source

Creator: Enrique Ventura. Video:
https://youtu.be/0Fn_lFxPBpw (41:10; no captions published).
Reddit thread: https://www.reddit.com/r/unrealengine/comments/1x2ho6b/
("Unreal 5.8 - Materials Masterclass - Chapter 9: Animation using
gradients", r/unrealengine post 1x2ho6b, 2026-10-12 scout run).
Texture pack: linked in the video description (Google Drive download).
Material names below are read from the editor tabs in 12 frames reviewed
from the downloaded video; node parameter values are not legible at
640x360, so exact constants are marked as not recovered.

## Tools used

Unreal Engine 5.8 Material Editor. Author-supplied gradient texture pack
(gradient/noise textures the four effects are built on).

## Phase 1: Set up the test scene

**Do**
1. Open the author's texture pack from the video description and import the
   gradient textures into the project.
2. Place the default checkered-cube test mesh in a simple room (the video
   uses the editor's default material-test cube on a grid floor) and, for
   the final showcase, a gallery room with framed paintings on the walls.

**Check**
- The cube renders with the default checker: the scene and lighting are sane
  before any custom material is applied.

**Why**
Every effect in the chapter is previewed first on a neutral mesh, then on
the gallery paintings. The neutral preview isolates the gradient mapping
from the scene lighting.

## Phase 2: M_MatrixCode (falling-code gradient streaks)

**Do**
1. Create a material named `M_MatrixCode`.
2. Sample the code-streak gradient texture with TextureSample nodes and drive
   the streak density along a vertical gradient, so the characters fade with
   height (frame-verified: the preview shows green falling-code streaks on a
   plane, denser at the bottom, fading upward).
3. Animate the gradient lookup over time so the streaks fall.

**Check**
- The streaks read as falling code, not static noise: motion must be visible
  on scrub.
- The vertical fade is smooth: banding means the gradient texture resolution
  is too low for the plane size.

**Why**
The vertical gradient is a 0-1 field; mapping streak opacity to it turns a
static texture into directional motion with no extra assets.

## Phase 3: M_DissolveSwap (dissolve-swap between two textures)

**Do**
1. Create a material named `M_DissolveSwap`.
2. Feed two source textures into TextureSample nodes (frame-verified: one
   holds a cat image, one a color gradient; the preview shows a Mona Lisa
   painting mid-swap).
3. Use a gradient as the dissolve mask: texels below the animated threshold
   show source A, above it source B. Animate the threshold over time.

**Check**
- At threshold 0 and 1 the output is purely source A / purely source B: any
  ghosting at the extremes means the mask math is wrong.
- The swap edge follows the gradient's shape: a linear gradient gives a
  wipe, a noisy gradient gives an organic dissolve.

**Why**
The gradient decides *where* the swap happens per texel; time decides *when*.
Separating the two is what makes one material produce both wipes and
dissolves.

## Phase 4: M_GlowWithTransition (glow cross-fade)

**Do**
1. Create the glow-transition material (editor tab reads `M_GlowWithTr...`,
   truncated in frames).
2. Feed the neon source texture plus gradient sources into TextureSample
   nodes (frame-verified: red neon cityscape, blue gradient, and cyan source
   textures wired to the material inputs; preview shows the red neon
   billboard).
3. Cross-fade the neon texture against the gradient-driven glow mask over
   time.

**Check**
- The neon areas bloom/pulse while the non-neon areas stay stable: if the
  whole image pulses, the mask is leaking into the base color.

**Why**
Masking the glow to the neon regions (via the gradient) keeps the effect
cheap and art-directable: the texture author decides what glows, the
material only animates it.

## Phase 5: Gradient wipe transition

**Do**
1. Create the transition material (editor tab reads `M_TransitionProduc...`,
   truncated in frames).
2. Use a noise/gradient source texture as the wipe field (frame-verified: a
   yellow noise/gradient texture in the TextureSample nodes; preview shows a
   gray gradient plane mid-wipe).
3. Animate a threshold across the field to wipe between two states.

**Check**
- The wipe completes fully: frozen mid-wipe frames mean the threshold range
  does not cover the field's full value range.

**Why**
Same mechanism as the dissolve-swap, applied as a full-screen or surface
transition instead of a texture blend. One technique, two use cases.

## Phase 6: The loop-point check

**Do**
1. For every animated material, scrub past the loop point and watch for a
   pop.
2. If it pops, tile the gradient and wrap the time input so the end state
   equals the start state.

**Check**
- Loop the preview for 3+ cycles: the eye catches a pop on the second
  viewing that it forgives on the first.

**Why**
Gradient animation only loops cleanly if the field tiles and time wraps.
This is the single most common defect in gradient-driven motion, and it is
always caught at the loop point, never in the middle.

## The human method, distilled

1. Teach one primitive until it yields four effects: the chapter's pedagogy
   is "one tool, many outputs", and the fixed texture pack is what makes
   the lesson reproducible for the student.
2. Name materials after the effect (`M_MatrixCode`, `M_DissolveSwap`), not
   the technique: the tab name is the documentation.

**Depth status:** PARTIAL (full media downloaded; 12 frames reviewed with
material names, TextureSample graph structure, and previews verified; no
captions exist and node parameter values are not legible at 640x360).
A local transcription plus a higher-res frame pass would recover exact
constants and reach FULL.
