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

## AAA studio practice

No named AAA studio was found publishing this exact rounded-box SDF UI shader, and none is claimed here. The production anchors below are the shipped SDF standard in Unity UI and Unity's own batching guidance, plus an independent SDF UI implementation solving the same problem.

- **SDF is already Unity UI's shipped standard for crisp shapes at any size, for text.** TextMeshPro is designed around signed distance field rendering, with SDF shaders that use the distance data for outlines, underlays, and bevels, and Unity warns that pushing those effects too far pulls in neighbouring atlas data unless font padding is increased. The transferable rule is the same as Phase 1: distance data, not pixels, carries the edge, and every effect that grows the visible shape needs padding or mesh growth budgeted for it. Source: https://docs.unity3d.com/Packages/com.unity.ugui@7.0/manual/TextMeshPro/Shaders.html
- **An independent SDF UI implementation states the same problem and the same math.** Daniel Goodnow's SDF-based `UIRect` for Unity replaces sprites with a rounded-rectangle SDF evaluated in the fragment shader, using Inigo Quilez's rounded-box formulation with per-corner radii, because Unity's built-in UI has no flexible rectangle rendering and sprites are the only built-in route to rounded corners. That corroborates Phase 1's framing, while the per-corner packing, shadow growth, and pooling in this skill remain the author's own design. Source: https://danielgoodnow.com/blog/unity-sdf-ui/
- **Batching in Unity UI is a same-material, same-texture, same-depth contract, and canvas rebuilds are the other cost.** Unity's UI optimization guidance says elements batch only when they share Z value, materials, and textures, and that a single changed element dirties the whole canvas, so static and dynamic elements belong on separate canvases; it also says to remove Graphic Raycasters from non-interactive canvases and turn off Raycast Target on non-interactive elements. Phase 3's pooling satisfies the material half of that contract; splitting animated shine elements onto their own canvas and disabling raycast targets on decorative images satisfies the rest. Source: https://unity.com/how-to/unity-ui-optimization-tips?fbclid=IwAR0tYJSpcjLoRUwVAXw3-fWGUmlStILiNSonpTNdGNGr6GEqsbqOKxFCWII

**Agent automation**

Write `ui-batching-audit.json` for every UI screen that uses this shader, with: distinct effect-settings combinations, material instance count, pooled material count, and draw-call count from the Frame Debugger for that screen, before and after pooling. Fail the audit if material instance count exceeds distinct settings combinations, or if draw-call count still scales with button count after pooling. Add a scripted hit-test suite for `IsRaycastLocationValid` that probes, for one rounded rect and one ring, at least: centre, inside a corner radius, outside a corner radius, inside the ring hole, and on the ring band, and records the expected boolean per probe from the same SDF math; a probe that disagrees with the rendered shape is a bug in one of the two implementations, not a tolerance issue. Add a canvas-split check: list every canvas on the screen with its static or dynamic classification, and flag any canvas mixing a per-frame animated shine element with static text. Keep the author's Phase 5 future work (scripting API, animated values in vertex data) as open items in the audit file until implemented; do not record them as done.

## The human method, distilled

1. "Corners are an SDF, not geometry." (author's heading, quoted)
2. "Effects broke batching." Fix the material model, not the effect.
3. Reuse one piece of math for rendering, masking, and clicks.
4. Grow the mesh to fit the effect; do not clip the effect to fit the mesh.

**Depth status:** FULL from the author's full post text. No shader code or Unity version was disclosed; the GitHub repository is the next evidence source for the implementation itself.
