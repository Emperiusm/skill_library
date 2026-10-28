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

## Depth status

FULL (article text).
