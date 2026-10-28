---
name: ai-3d-gaussian-splats
description: "Capture, inspect, and decide on Gaussian splats: the capture to real-time rasterization pipeline, the splat-versus-mesh decision rule, and a mixed-format workflow for scenes that need both. Trigger when working with splats or choosing between splats and meshes."
---

# Gaussian Splats for 3D Creators

## Purpose

This skill treats splats as a different representation, not a different
kind of mesh: no surface, no topology, no UVs, no rig, baked lighting,
and files in the tens to hundreds of megabytes. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it),
and **Why** (the principle). The core method is: capture well, decide
by job, and mix formats where the scene demands both.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/what-is-a-gaussian-splat
- https://customuse.com/learn/gaussian-splats-vs-3d-models

## Tools used

Tools used: capture tools (phone or camera capture), COLMAP for camera
solving, splat optimization and real-time rasterization viewers and
engines. No single splat tool is prescribed by the sources.

## Phase 1: Capture and solve

**Do**
1. Capture the real-world subject with overlapping coverage from
   many angles. Splat quality is bounded by capture coverage the way
   reconstruction is bounded by reference coverage.
2. Solve cameras with COLMAP (or the capture tool's solver) so every
   view agrees on where it was taken from.
3. Optimize the splat set: prune floaters and noise, densify where
   detail demands it.

**Check**
- Is coverage complete, including the angles the camera will actually
  visit?
- Are floaters and noise pruned, or will the viewer fly through them?

**Why**
A splat is a view-dependent representation: it can only show what was
captured, from directions near where capture happened. Gaps in capture
are gaps in the scene, not defects to patch later.

## Phase 2: Inspect what you actually have

**Do**
1. Move a camera through the splat the way the audience will: orbit,
   dolly, and close-up.
2. Check for baked lighting artifacts: the splat wears the capture
   light, and relighting it is not available the way it is for a mesh.
3. Check file size against the delivery budget: tens to hundreds of
   megabytes per scene is normal for splats and must be planned for.

**Check**
- Does the splat hold up on the camera paths that matter, or only on
  the capture angles?
- Is the size budgeted for delivery, or will it arrive as a surprise?

**Why**
Splat inspection is camera-path inspection. A splat that looks perfect
from the capture angles and falls apart on the hero move was never
actually good.

## Phase 3: Decide splat versus mesh

**Do**
1. Apply the decision rule: use Gaussian splats when the input is the
   real world and you mostly want to move a camera through it. Use
   meshes when the asset must be edited, rigged, collided with, or
   relit.
2. When unsure, run a one-hour bake-off: capture the same subject
   both ways and judge each by its own destination's criteria.
3. For mixed scenes, run the six-step mixed workflow: splats for the
   real-world environment the camera moves through, meshes for
   anything that must be edited, animated, or collided with, with a
   clean handoff between the two layers.

**Check**
- Does anything in the splat layer need editing, rigging, collision,
  or relighting? If yes, it belongs in the mesh layer.
- Does anything in the mesh layer exist only to be looked at from a
  moving camera? If yes, it may belong in the splat layer.

**Why**
Splats and meshes are not competitors; they are answers to different
questions. The bake-off exists because teams keep asking the wrong
question ("which is better?") instead of the right one ("which job is
this?").

## The human method, distilled

1. Capture coverage is the budget. Uncaptured angles do not exist.
2. Inspect on the audience's camera paths, not the capture angles.
3. Splat when the input is real and the job is camera movement.
4. Mesh when the job is edit, rig, collide, or relight.
5. Mixed scenes are normal: splats for environment, meshes for
   interaction.

## AAA studio practice

Production teams using splats in real-time engines treat them as one
layer of a mixed scene, not as a replacement for meshes, and they
budget renderer engineering, not just capture quality:

- **Mixed-format scenes are the production shape.** Rotor Studios
  augmented Unreal Engine's Procedural Content Generation framework
  with Gaussian splats for rapid photorealistic environment creation
  on two global car launches, under tight budgets and deadlines, while
  keeping the rest of the pipeline in meshes
  (https://forums.unrealengine.com/t/talks-and-demos-elevating-automotive-content-integrating-ue-with-gaussian-splats-and-ai-unreal-fest-orlando-2025/2672423.rss).
  World Labs' image-blaster pipeline makes the same split explicit:
  a splat environment plus meshed props (not splatted) so objects
  collide
  (https://www.top3d.ai/learn/gaussian-splatting-playable-game-engines-2026).
  This confirms the skill's Phase 3 rule and sharpens it: the splat
  layer must never carry anything that needs collision, because
  collision comes from a mesh.
- **Splat rendering is an engineering choice, not a viewer default.**
  Moonshine Studio's Tim Chen built NanoGS, a free Unreal plugin that
  renders large splats with Nanite-style LOD clusters, screen-space
  error LOD selection, splat compaction, and GPU radix sort, because
  naive splat rendering wastes GPU memory and frame time
  (https://www.cgchannel.com/2026/03/free-plugin-nanogs-puts-nanite-style-gaussian-splatting-in-unreal-engine/).
  Magnopus' custom Unreal renderer instead uses one instanced draw
  call for all splats and reports roughly 7 million splats at 60 fps,
  with no enforced upper bound on splat count
  (https://www.magnopus.com/blog/how-i-ended-up-rendering-unlimited-gaussian-splats-in-unreal).
  The automation implication: pick the renderer by measured splat
  count and frame time, not by which plugin installed first.
- **Splats do not collide, and do not take dynamic global
  illumination.** The playable-splat assessment is blunt: you gain
  photoreal capture and lose dynamic global illumination, and splats
  render as alpha rather than a full PBR pass
  (https://www.top3d.ai/learn/gaussian-splatting-playable-game-engines-2026).
  Any scene that needs either must carry meshes alongside the splats.

**Do (automation additions, appended to the phases above)**
1. After Phase 2 inspection, generate a collision mesh from the
   splat layer (the `splat-transform --collision-mesh` pattern) and
   place it as the mesh layer's collider; never ship a walkable splat
   with no collider
   (https://www.top3d.ai/learn/gaussian-splatting-playable-game-engines-2026).
2. Write a splat manifest next to the scene: splat count, file size,
   renderer used, and measured frame time on the target hardware.
   Gate the scene on it: if the count exceeds what the chosen
   renderer holds at target frame rate, compact or re-cluster
   before shipping.
3. Automate the PLY-to-Unreal coordinate check on import: Magnopus
   documents the conversion as position (x, -z, -y) times 100 in
   Unreal units, with scale and opacity passed through a sigmoid
   (https://www.magnopus.com/blog/how-we-wrote-a-gpu-based-gaussian-splats-viewer-in-unreal-with-niagara).
   A scripted import check that verifies one known marker lands at
   the expected Unreal coordinates catches the lying-down or
   100x-off import before a human notices it.

**Check**
- Does the manifest exist, with a collider mesh present for every
  walkable splat area?
- Was the renderer chosen from measured frame time at the scene's
  actual splat count?

## Depth status

FULL (article text).
