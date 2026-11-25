---
name: unity-sdf-ui-shader-batching
description: "Build Unity UI images with rounded corners, soft shadows, and shine in a single shader without breaking batching: rounded-box SDF on one quad, per-corner radii packed into UV channels, mesh grown by shadow bounds in OnPopulateMesh, materials pooled by effect settings, and the same SDF math for hit-testing. Trigger when Unity UI needs sharp rounded shapes, shadows, or shine without 9-slice sprites or a draw call per button."
---

# Unity UI: Rounded Corners, Shadows, and Shine in One Batching Shader

## Purpose

This skill replaces 9-slice sprites and per-effect materials with one shader evaluation plus pooled materials. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: replace geometry and per-effect materials with one SDF evaluation plus pooled materials, and reuse the same math for hit-testing.

## Source

- Post: "How I built rounded corners, soft shadows and shine for Unity UI in a single shader (and kept it batching)" by maglortolion — https://www.reddit.com/r/unity/comments/1y478tn/ (score 25, 4 comments, all retrieved; no technique detail in comments beyond praise). Evidence: the author's full post text (1,721 characters, all five lessons plus the GitHub link). GitHub (MIT): https://github.com/berkencami/round-ui-unity. Scout audit 2026-11-25. No shader code, Unity version, or performance measurement beyond the 20-buttons example was disclosed; none is invented here.

## Tools used

Unity (version not stated); a single custom shader; C# (`OnPopulateMesh`, `IsRaycastLocationValid`, material pooling with ref counting). No other tools named.

## Phase 1: Replace 9-slice sprites with an SDF quad

**Do**
1. Build a drop-in replacement for Unity's Image that does rounded shapes without 9-slice sprites.
2. Keep each image as a single quad. In the fragment shader, evaluate a rounded-box signed distance function (SDF) for the corners. Pack per-corner radii as 16-bit values into two floats and send them through UV channels, so no material property is needed per corner.

**Check**
- Edges stay pixel-sharp at any size; the author confirms in comments that "keeping them sharp at any size was the main goal".

**Why**
Corners as a distance evaluation, not geometry, decouple sharpness from mesh density. Packing radii into UV channels keeps the data per-image without breaking material sharing (Phase 3).

## Phase 2: Stop shadows and outlines being clipped

**Do**
1. Grow the mesh in `OnPopulateMesh` by the shadow's offset + blur + spread, because the quad was the size of the RectTransform and anything drawn outside it was cut off.
2. Draw the shadow in the shader from the same SDF, offset and softened.

**Check**
- Outline and shadow are no longer cut at the RectTransform edge.

**Why**
The mesh is the clip boundary. If the effect extends beyond the mesh, the effect must grow the mesh, not fight the clipper.

## Phase 3: Keep effects batching with pooled materials

**Do**
1. Pool materials by their effect settings with ref counting, so images with identical settings share one material and batch. Previously every image with an effect created its own material instance: 20 shadowed buttons meant 20 draw calls.
2. Animate the shine in the shader instead of writing to the material every frame.

**Check**
- Identical-settings images share one material; the draw-call count no longer scales with the button count.

**Why**
Per-instance materials are the batching failure. Pooling by settings plus in-shader animation removes both causes (distinct materials and per-frame material writes) without changing the look.

## Phase 4: Handle masking and clicks with the same math

**Do**
1. When a rounded image is itself a Mask (for example a circular avatar), keep the shape's alpha separate for alpha clipping, so it masks only the shape, not its shadow.
2. Implement `IsRaycastLocationValid` with the same rounded-box math, so clicks outside the corners or inside a ring's hole are ignored.

**Check**
- A circular avatar masks its shape without masking its shadow; clicks in a ring's hole do not register.

**Why**
One distance function for rendering, masking, and hit-testing keeps the three behaviours consistent by construction. Separate implementations would drift.

## Phase 5: Known remaining work

**Do**
1. The author's stated list: a public scripting API, and moving animated values into vertex data so tweening them does not create new materials.

**Check**
- Not yet done; stated as future work in the post, not demonstrated.

**Why**
Tweening an animated value through a material property recreates the Phase 3 problem in miniature. Vertex data is the author's planned fix, recorded here as a plan, not a result.

## The human method, distilled

1. "Corners are an SDF, not geometry." (author's heading, quoted)
2. "Effects broke batching." Fix the material model, not the effect.
3. Reuse one piece of math for rendering, masking, and clicks.
4. Grow the mesh to fit the effect; do not clip the effect to fit the mesh.

**Depth status:** FULL from the author's full post text. No shader code or Unity version was disclosed; the GitHub repository is the next evidence source for the implementation itself.
