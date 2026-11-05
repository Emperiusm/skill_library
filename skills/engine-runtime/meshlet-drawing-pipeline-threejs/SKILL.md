---
name: meshlet-drawing-pipeline-threejs
description: "Render billions of instanced triangles at 60 fps in the browser with three.js r187 MeshletDrawingPipeline: split geometry into 64-triangle meshlet clusters with LOD chains, cull on the GPU per frame, and draw what survives with one indirect draw per geometry/material group. Trigger when a WebGPU scene is bottlenecked on submitted triangle count and the geometry is heavily instanced."
---

# Meshlet Cluster Culling in three.js (MeshletDrawingPipeline)

## Purpose

This skill reconstructs the MeshletDrawingPipeline stress-test workflow, step by step, so another agent can apply GPU cluster culling to a WebGPU scene the same way. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: split each geometry once into 64-triangle meshlet clusters with simplified LOD chains, then let compute shaders cull clusters before rasterization so instance count stops being the bottleneck.

## Source

- Post: "~2 billion triangles (mostly instanced) at 60 fps with the new MeshletDrawingPipeline in three.js r187" by Sara_KumoDeck — https://www.reddit.com/r/threejs/comments/1xmncnq/2_billion_triangles_mostly_instanced_at_60_fps/ (r/threejs, score 117, 15 comments)
- Live demo: https://r187-meshlet.kumodeck.app/ (hosted on KUMODeck)
- Evidence: full author writeup (2026-11-04 scout run) plus comment thread. Built with Claude Opus 5.5. Scene-generation code undisclosed; no real-phone WebGPU numbers yet.

## Tools used

three.js r187, WebGPURenderer, `MeshletDrawingPipeline` (`three/addons/pipelines/MeshletDrawingPipeline.js`, PR #35191 by sunag); meshoptimizer (cluster building); headless browser with WebGPU for measurement.

## AAA studio practice

- **Meshlets in a shipped game (Remedy, *Alan Wake 2*).** Northlight's GPU-driven rendering pipeline: "we can now do occlusion culling down to a single-pixel precision and use everything in a scene as an occluder. This ability to only draw what is visible means that the world of AW2 has more geometric detail than we've ever shipped before. Diving a bit deeper into how it works: we also cull meshlets, in addition to the mesh. Meshlets are smaller, more optimized, groups of triangles extracted from the mesh" ([remedygames.com](https://www.remedygames.com/article/how-northlight-makes-alan-wake-2-shine)). Lead graphics programmer Tatu Aalto: "To achieve high geometric detail on rendering, it is crucial to select very accurately the geometry that contributes to the image and only draw that. When combined with GPU-based occlusion culling, mesh shaders provide a very efficient and simple framework to use GPU power where it matters" ([wccftech.com](https://wccftech.com/alan-wake-2-dev-talks-integration-of-mesh-shaders-dlss-3-5-explains-work-graphs-importance-in-future-games/)).
- **Nanite: the reference cluster design (Epic, SIGGRAPH 2021).** Brian Karis: "Nanite partitions every mesh into clusters of 128 triangles. Clusters are grouped into cluster-groups of 8–32 clusters, and each group is simplified as a unit to produce the next LOD level." The parallel LOD-selection rule: `bool render = (parent_error > threshold) && (cluster_error <= threshold);` — "Every group evaluates that expression using only local data... No sibling communication. No global sort... you dispatch one thread per group in a compute shader and the answer drops out." The error metric is "a bounding sphere plus a scalar... projected into screen space and compared against the r.Nanite.MaxPixelsPerEdge threshold (default 1.0)"; "Nanite performs ... two-pass occlusion culling" ([nanite-lumen.pdf](https://theisegoria.github.io/nanite-lumen/nanite-lumen.pdf)). The three.js pipeline's 64-triangle clusters are the same family at half the granularity (inference: the granularity choice is the author's, not from Epic).
- **GPU culling before it was cool (DICE/Frostbite, GDC 2016).** Frostbite's compute-culling deck: software Hi-Z "In Frostbite since Battlefield 3. Done on the CPU for the upcoming GPU frame. No latency"; "Draw Call Compaction (No Zero Size Draws)" — compacted indirect draws after GPU culling; "Small and inefficient draws are a problem"; batches are "Configurable subset of meshes in a scene" where "Meshes within a batch share the same shader and strides" ([slideshare, GDC 2016](https://www.slideshare.net/slideshow/optimizing-the-graphics-pipeline-with-compute-gdc-2016/59747720)). Honest gap: no AAA source states an explicit per-material meshlet-batch cap; using Frostbite's batch-by-shader-and-stride rule to justify the per-size-class material split below is inference.

## Phase 1: Build an instanced stress scene

**Do**
1. Generate the scene procedurally: the author's stress scene is a sandstone canyon with ruined temples — "noise-carved cube spheres, TSL materials", "no models or textures."
2. Favor repeated geometry: 8 rock/column shapes + the ground = ~8.3M unique triangles, placed 42,033 times as InstancedMesh. The 39,948 pebbles alone are 767M of the 1,967,478,960-triangle total.
3. Fly a low camera through the scene as the stress route.

**Check**
- The on-screen counter reads 1,967,478,960 triangles.
- Clusters are built per geometry and shared by every instance: "that's exactly the case this pipeline is good at."

**Why**
Instanced, repeated geometry is the best case for cluster sharing. A stress test should target the pipeline's strength, not a generic scene.

## Phase 2: Wire the pipeline

**Do**
1. `import { MeshletDrawingPipeline } from 'three/addons/pipelines/MeshletDrawingPipeline.js';`
2. `const meshlets = new MeshletDrawingPipeline( { occlusionCulling: true, lodThreshold: 1 } );`
3. `renderer.drawingPipeline = meshlets;` — "the same scene now draws as meshlets."
4. `await renderer.compileAsync( scene, camera );` — runs prepareAsync, which builds clusters + LODs. ("In the demo the compile goes through the RenderPipeline's scene pass, which calls the same thing.")
5. Each frame, read `meshlets.info` → `{ clusters, triangles }` actually drawn.
6. Agent-executable: adopt Nanite's local-cut rule as the LOD reference design — a monotone screen-space-error metric evaluated locally per cluster-group on the GPU (one thread per group, no global sort, the `(parent_error > threshold) && (cluster_error <= threshold)` cut), and ship a stat overlay showing LOD distribution per frame to validate it. Emit a cull-efficiency stat every run: percent of triangles actually drawn vs submitted, so the pipeline proves Remedy's bar — "only draw what contributes to the image."

**Check**
- Each geometry is split once into clusters ("meshlets") of 64 triangles plus a chain of simplified LODs, built with meshoptimizer.
- Every frame, compute shaders pick an LOD per object, cull objects and clusters against the frustum, cull clusters hidden behind others, and draw what's left with one indirect draw per geometry/material group.
- First measured frame: 26,725 clusters drawn, about 1.71M triangles — 0.087% of the scene.
- The stat overlay shows which LOD level serves each visible cluster-group; the cull-efficiency number moves in the right direction when density grows (inference: validate against the independent benchmark, do not chase the percentage itself).

**Why**
Cull on the GPU before rasterization. The `info` readout is the proof: submitted triangles, not scene triangles, are the cost.

## Phase 3: Measure against the real baseline

**Do**
1. Measure in a headless browser with WebGPU on the real GPU (author: "40-core integrated GPU"), 1440x900.
2. Compute fps as frames over the last 0.5 s; read drawn triangles from `info`.

**Check**
- Meshlets ON: 60 fps. Same spot, standard pipeline: 20 fps.
- Phone-size viewport with the CPU throttled 4x: 60 fps on a reduced 246M-triangle version.
- "I haven't tried a real phone's WebGPU yet. Numbers from real devices would be great."

**Why**
The author's own framing is "The honest breakdown": unique vs instanced triangles are different numbers, and both are stated. Always measure the same spot with the pipeline off.

## Phase 4: Survive the material-batch crash

**Do**
1. Expect this failure: "the pipeline batches objects by material, and sizes the batch by 'object count x the most meshlets any of its shapes has'. 40k pebbles sharing a material with the 12k-meshlet spires blew past the limit and crashed."
2. Fix: give each size class its own material instance.
3. Agent-executable (inference, labeled): at the offline meshoptimizer step, emit a per-material batch report — meshlet count, smallest and largest meshlet per material — and add a build-time check that warns when small-meshlet and large-meshlet shapes share one material before it can blow past the indirect-draw budget. Frostbite's rule (meshes in a batch share shader and strides) is the reference behavior, not a stated cap.

**Check**
- The crash reproduces when small-meshlet and large-meshlet shapes share a material; separate material instances per size class clear it.
- The batch report is emitted for every build; the warning fires before the crash can, not after.

**Check**
- The crash reproduces when small-meshlet and large-meshlet shapes share a material; separate material instances per size class clear it.

**Why**
Batch sizing is multiplicative in object count and max meshlets. Heterogeneous geometry under one material is the trap; the fix is a material per size class, not fewer instances.

## Phase 5: Ship the fallback and debug tools

**Do**
1. Without WebGPU, fall back to a lighter 13.5M-triangle scene drawn the normal way, show a note saying so, and disable the toggle.
2. Budget 16–21 s of cluster preparation on desktop before the first frame (show a progress bar). The API has no way to save the result: "caching it would mean rolling my own."
3. Ship an ON/OFF toggle and a "Show meshlets" button that colors every cluster so culling and LOD changes are visible while flying (WASD + Q/E or drag).

**Check**
- Independent benchmark (u/Sunspear): 29M source triangles; in one view meshlets cut submitted triangles 85% (5.6M → 860,000), but p99 frame time went 10 ms → 21 ms on a recorded route vs their "highly optimized conventional batching baseline." Meshlets win submitted-triangle count; a tuned baseline can still win frame time.
- Caveat (u/GreenCurious9895): an outdoor environment (trees, 3D grasses, plants, water) "did not provide much benefit" — unanswered in the retrieved comments. Foliage-heavy scenes are the open question.

**Why**
A stress test that only runs on the author's machine is a demo. The fallback, the toggle, and the cluster visualizer are what make it a tool others can evaluate.

## The human method, distilled

1. Build the stress test, not the demo ("I built a stress test for it").
2. Publish the honest breakdown (8.3M unique vs 1.97B instanced, both stated).
3. Measure against the real baseline (same spot, standard pipeline: 20 fps).
4. Name the failure mode and the fix (material-batch crash → per-size-class materials).
5. Ship the degradation path (WebGL2 fallback scene, disabled toggle, cluster visualizer).

**Depth status:** FULL (full author writeup with exact API, numbers, failure mode, fallback; 15 comments with one independent benchmark). Caveats: scene-generation code undisclosed; no real-phone WebGPU numbers yet.
