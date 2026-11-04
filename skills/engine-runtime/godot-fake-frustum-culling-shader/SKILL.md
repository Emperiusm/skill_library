---
name: godot-fake-frustum-culling-shader
description: "Visualize what real frustum culling removes in Godot 4: a shader that discards pixels invisible to a reference camera, camera data passed from GDScript, plus the corrections that make the fake match the engine (AABB testing, ~20% frustum pad, per-face granularity). Trigger when teaching, debugging, or demonstrating visibility culling in Godot."
---

# Godot Fake Frustum Culling Shader

## Purpose

This skill reconstructs the fake-frustum-culling visualization workflow, step by step, so another agent can show what real frustum culling removes in Godot. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: discard pixels the reference camera cannot see, then correct the fake until its errors match the real engine's errors.

## Source

- Post: "Fake frustum culling shader" by partybusiness — https://www.reddit.com/r/godot/comments/1xm802w/fake_frustum_culling_shader/ (r/godot, score 56, 13 of 14 comments retrieved)
- Evidence: post text plus the author's shader line and community corrections in the comments (2026-11-03 scout run). Native Reddit clip; the full shader was not published.

## Tools used

Godot 4 (shader language + GDScript). Test assets: statues from the Scan the World project (the author names MyMiniFactory "Cicero" 3D print, object 55952, as one of the statues he grabs "for graphical tests").

## Phase 1: Build the camera-discard shader

**Do**
1. Write a Godot shader that discards pixels not visible to a given reference camera.
2. Pass the camera data to the shader from a GDScript: the camera projection matrix and the camera transform matrix as uniforms.
3. In the shader, compute the view-space position of each pixel and discard it when it falls outside the reference camera's view. The author's version tests a single point, changing one line to: `view_pos = (camera_projection_matrix * camera_transform_matrix * MODEL_MATRIX * vec4(0.0, 0.0, 0.0, 1.0)).xyz;`

**Check**
- Statues vanish when the reference camera cannot see them. The author's own admission: "there's no performance benefit" — this is a visualization, not an optimization.
- Known failure: testing a single point makes objects disappear too soon when they are half on-screen. If your demo pops objects at the screen edge, you have this bug.

**Why**
The point is pedagogical: show what real frustum culling would remove. Per-pixel discard is the simplest correct visualization, and the failure mode (early pop) is itself the lesson of Phase 2.

## Phase 2: Correct toward real culling behavior

**Do**
1. Test against the mesh's bounds, not one point. Pass the AABB as uniforms, because it is "not directly available in the shader" (author).
2. For per-face instead of per-pixel culling, declare the varying flat: `varying flat vec3 view_pos;`
3. Internalize Godot's real rule (TheDuriel, score 12): Godot frustum-culls using the Mesh AABB, not per-vertex and not per-surface. And the frustum check "usually considers the AABB of the object, and expands the camera frustum by around 20% in all directions."

**Check**
- With AABB testing plus the frustum pad, objects disappear at the screen edge at roughly the same moment Godot itself would cull them. The one-point version pops "too soon, when they're half on-screen ... that's exactly how it works!" (TheDuriel) — meaning the early pop is what the real engine avoids by testing volumes.
- In Godot terminology: in a "mesh", a "surface" is each contiguous strip of vertices/faces that share a material; a surface is drawn at once, so per-surface is the finest granularity real culling can reach. Per-pixel discard is strictly finer than reality.

**Why**
Real engines test volumes, not points, and pad the frustum (~20%) so edge cases don't pop. The fake shader is most useful when its errors match the real engine's errors; otherwise you are demonstrating a straw man.

## The human method, distilled

1. Build the fake version to see what the real system sees.
2. When the fake disagrees with the engine, the engine's rule (AABB + ~20% frustum pad) is the spec.
3. The failure of the naive version (one-point test pops too early) is the lesson, not a bug to hide.

**Related design idea (commenter, not the author):** a game puzzle where different cameras render different objects, so the player must figure out how to aim each camera to get past a room or bridge. Design idea only; no implementation discussed.

## AAA studio practice

- **Epic Games, Unreal Engine visibility culling docs (Daniel Wright, https://docs.unrealengine.com/udk/Three/VisibilityCulling.html)**: Unreal applies culling methods per primitive in order: distance culling, then view frustum culling, then precomputed occlusion culling, then dynamic occlusion culling (hardware occlusion queries). Frustum culling sits between the cheap distance tests and the expensive occlusion work. All culling is bounds-based: cull distance volumes map the diameter of each primitive's bounding sphere to a cull distance, and Unreal derives the bounding sphere from the tight geometry box. Volumes, not points, is confirmed as the engine norm. Note: no frustum padding or fudge factor appears in Unreal's approach; instead of expanding the frustum, Unreal manages popping via Cull Distance Volumes and per-primitive MaxDrawDistance.
- **Saints Row: The Third Remastered shipper on culling practice (https://krupitskas.com/posts/modern_culling_techniques/)**: "Frustum culling tests objects, usually via bounding volumes like spheres or AABBs, against the six planes of the frustum and skips anything that doesn't intersect," and it is "almost always the first pass" (or second after distance culling) in the pipeline. Names Horizon Zero Dawn as the example: big objects like mountains stay rendered even when almost outside the frustum, which is object-level culling's granularity tradeoff. Pop mitigations used in practice: dithered fade-out, aggressive LOD before the cull point, impostors. Quoted rule of thumb: "be conservative with correctness and aggressive with wasted work. A false negative just means you rendered a bit more than necessary. A false positive means something vanished in front of the player."
- **GPU-driven rendering (Vulkan guide, https://vkguide.dev/docs/gpudriven/gpu_driven_engines/)**: named shipped titles and engines: Assassin's Creed Unity (and sequels) use compute-shader culling for Paris's object counts plus building interiors; Frostbite uses it for the high geometry detail of Dragon Age Inquisition; Rainbow Six Siege for thousands of dynamic rubble objects; Doom Eternal goes all-in on bindless with fewer than 500 pipelines. A compute shader culls over 1 million objects in under 0.5 ms; Dragon Age Inquisition's pipeline goes further and culls individual triangles, writing the surviving index buffer from the culling shaders. Per-object cull bounds live in GPU buffers alongside matrices and material IDs, tested by the compute shader and compacted via atomic counter into indirect draws. The AAA direction is finer-grained GPU culling, not CPU frustum visualization.
- **Honesty flag on the 20% pad**: no AAA source confirms a fixed frustum-expansion percentage like the ~20% in TheDuriel's comment. In production, popping is managed through conservative bounds, cull-distance tuning, dithered fade, and LOD, not an explicit expanded frustum. The skill's 20% pad is a Godot-visualization convenience, not an AAA practice; keep it labeled as such.

## Agent automation

1. **Cull-moment diff gate** (bounds-granularity check): script a recorded camera sweep past the statue test scene. For each frame, run the discard logic at three granularities (single-point, per-face `varying flat`, AABB) and record the first frame each statue fully disappears in `cull-diff.json`. Diff against Godot's real cull moment for the same sweep. The single-point version must pop earlier than the engine (reproducing the documented failure); the AABB version must match within a small tolerance.
2. **No-false-negative check** (krupitskas rule): over the same sweep, assert nothing vanishes while the reference camera still sees it. False positives (late pops, conservative correctness) are acceptable; a false negative is a hard fail.
3. **Pop-visibility probe** (dithered-fade/LOD analog): at each cull boundary, capture before/after frames and pixel-diff them. If the diff spikes above a threshold without a fade, log a pop event to the report. This is the automated version of the author's "statues vanish" Check, and it is how production would catch the visual the padding heuristic hides.

**Depth status:** PARTIAL (post text + 13 comments including one line of shader code; the full shader was not published).
