---
name: meshlet-forest-scene-threejs
description: "Apply three.js r187 MeshletDrawingPipeline to a real forest scene: put it on static triangle-heavy geometry (logs, terrain, stones), keep wind-animated leaves and tile-based grass out, and measure the rendered-triangle fraction. Trigger when a WebGPU forest or outdoor scene is fps-bound on submitted triangles and the foliage already has its own LOD."
---

# Meshlet pipeline on a real forest scene (three.js r187)

## Purpose

This skill reconstructs the exact workflow PerceptionCharming used to apply the three.js r187 MeshletDrawingPipeline to a Forest environment, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: apply GPU cluster culling only to the static, triangle-heavy geometry, and keep the animated and already-cheap systems on their own paths.

This is a variant of `meshlet-drawing-pipeline-threejs`, which covers the pipeline mechanics on a procedural stress-test scene (2B instanced triangles, 60 fps). This skill covers the *application* rules on a real scene: what to include, what to exclude, and what it measures. Read both: the stress-test skill for how the pipeline works, this one for where it pays.

## Source

Creator: PerceptionCharming

Source: https://www.reddit.com/r/threejs/comments/1xpdv8e/i_implemented_the_meshlet_pipeline_from_threejs/ | r/threejs post 1xpdv8e (score 28, 3 comments, all 3 retrieved) | native Reddit clip

Depth: PARTIAL — exact numbers + inclusion/exclusion rules + failure mode; no code, no cluster sizes, no profiler breakdown.

## Tools used

three.js r187, MeshletDrawingPipeline, WebGPURenderer. Scene: author's Forest environment (tree logs and branches, terrain, broken logs on the ground, stones, grass, leaves).

## AAA studio practice

- **Meshlets in a shipped game, in a forest (Remedy, *Alan Wake 2*).** Northlight's GPU-driven rendering pipeline: "we can now do occlusion culling down to a single-pixel precision and use everything in a scene as an occluder. This ability to only draw what is visible means that the world of AW2 has more geometric detail than we've ever shipped before. Diving a bit deeper into how it works: we also cull meshlets, in addition to the mesh. Meshlets are smaller, more optimized, groups of triangles extracted from the mesh" ([remedygames.com](https://www.remedygames.com/article/how-northlight-makes-alan-wake-2-shine)). Lead graphics programmer Tatu Aalto: "To achieve high geometric detail on rendering, it is crucial to select very accurately the geometry that contributes to the image and only draw that" ([wccftech.com](https://wccftech.com/alan-wake-2-dev-talks-integration-of-mesh-shaders-dlss-3-5-explains-work-graphs-importance-in-future-games/)). The author's forest is the same class of scene Remedy proves the pipeline on: the inclusion rule (static trunks, terrain, stones) matches Remedy's meshlet set, and the rendered-fraction metric is the same "only draw what contributes" bar.
- **Animated vegetation gets its own path (Remedy, *Alan Wake 2*).** "The expansive primordial forest environments of Alan Wake 2 are brought to life through our new shader-based vegetation system. It's based on a new skinning system that runs entirely on GPU," with "almost 300,000 bones in Cauldron Lake [game area] being processed every frame" ([remedygames.com](https://www.remedygames.com/article/how-northlight-makes-alan-wake-2-shine); bone count via [pcgamer.com](https://www.pcgamer.com/remedys-plant-bone-tech-is-just-one-of-the-reasons-alan-wake-2-is-the-best-looking-videogame-of-2023/)). This is the shipped-game version of this skill's exclusion rule: wind-animated foliage does not go through the static meshlet path; it gets a GPU skinning path. Excluding leaves is not a workaround, it is the production architecture.
- **Nanite's own limits say the same thing (Epic, SIGGRAPH 2021).** Nanite partitions every mesh into clusters of 128 triangles, and it does not support animated meshes: cluster data is static, so per-vertex animation breaks the amortization the whole system rests on. When per-instance triangle counts are low (individual grass blades, scattered pebbles), the fixed per-cluster overhead eats any theoretical benefit; the Nanite Foliage pipeline that shipped in UE 5.3 addresses this by batching foliage instances into shared clusters (secondary summary of Brian Karis et al., SIGGRAPH 2021, [unbiased-gamer.com](https://unbiased-gamer.com/the-mental-model-for-unreal-engines-nanite-virtualized-geometry-and-cluster-culling/)). The three.js pipeline's 64-triangle clusters are the same family at half the granularity, so the same two rules transfer: keep animated geometry out, and do not meshlet geometry whose per-instance triangle count cannot amortize the cluster overhead.
- **Cluster culling's production numbers, and the wind fix (Ubisoft, Frostbite).** Ubisoft's *Assassin's Creed Unity* pipeline introduced GPU-driven cluster culling in production form: 20-40% of triangles culled, 30-80% of shadow triangles culled, 10x more instances on screen than the previous generation. Wind-driven vertex animation breaks shadow caching and reprojection, because the foliage geometry is not stable frame to frame; the production fix is to bake the wind into the cluster bounds (inflate bounding boxes by the maximum vertex-offset) so culling stays conservative without re-uploading per frame ([app.cinevva.com](https://app.cinevva.com/blog/2026-05-11-foliage-overdraw), citing Haar and Aaltonen, SIGGRAPH 2015, and Wihlidal, Frostbite GDC 2016). If leaves are ever reconsidered for meshlets, the bounds-inflation test below is the first gate, not a bigger cluster size.

## Phase 1: Measure the baseline, then switch the pipeline on

**Do**
1. Run the forest without meshlets and record fps: 20-25 fps on the author's M1 Mac.
2. Enable the MeshletDrawingPipeline from three.js r187 on the scene.
3. Re-measure at the same spot: 30-35 fps.

**Check**
- Transitions are "pretty seamless" (author's words). The fps gain is ~1.4-1.5x on M1-class hardware.
- The author used the headroom to add more detail to the tree models "without worrying much about polycount."

**Why**
- Same-spot before/after fps is the only honest measurement; the author reports both numbers.

## Phase 2: Choose what the pipeline covers (the inclusion rule)

**Do**
1. Put the pipeline on: tree logs and branches, the terrain, broken logs on the ground, and stones throughout the scene.
2. Before meshlets these took up around 2M triangles total. With meshlets, the author renders only around 25% of it.
3. Agent-executable: write a per-category inclusion manifest (`meshlet-inclusion.json`) before enabling the pipeline: one row per scene category (logs, terrain, stones, leaves, grass) with the decision (include / exclude), the reason, and the per-instance triangle count. Gate: a category is included only if it is static AND its per-instance triangle count amortizes the 64-triangle cluster overhead (Nanite's rule: low per-instance counts do not pay). Every run logs submitted vs rendered triangles per frame to `meshlet-stats.jsonl`; the rendered fraction (author: ~25% of ~2M) is the acceptance metric, and a run with no fraction recorded is an incomplete measurement.

**Check**
- Rendered-triangle fraction (~25% of ~2M) is the number that proves the culling works; fps alone would not separate culling from other changes.

**Why**
- Meshlets pay on static, triangle-heavy geometry. The inclusion list is exactly that class of geometry.

## Phase 3: Exclude what it does not help (the exclusion rule)

**Do**
1. Keep leaves OUT of the meshlet pipeline. Leaves have wind movement in a custom shader, and with meshlets "there seem to be visible glitches in leaves as the player moves." Remove meshlets from leaves.
2. Keep grass OUT. The grass runs on a tile-based rendering architecture with its own LOD system, so "it already has maximum performance. It doesn't need meshlet pipeline."
3. (Author's estimate, not measured): if meshlets ran on leaves, the gain would be 10-15%, "not a huge one," because leaves are heavy on the fragment shader and don't have that many triangles.
4. Agent-executable: if leaves are ever reconsidered for meshlets, run the production wind-bounds test first (from the AAA section above): inflate each leaf cluster's bounding box by the maximum wind-vertex offset, then run the moving-camera pass and compare against the un-inflated run. Keep the exclusion unless the glitch is gone AND the rendered-fraction gain clears the author's 10-15% estimate; a still-frame pass does not count, since the failure mode only shows while moving. Record the test and its verdict in `meshlet-inclusion.json`.

**Check**
- The commenter asked the right question ("I would have thought Meshlets would be kinda useless in a scene like this, it doesn't work on leaves or grass, which is the vast majority of your geometry right?") and the author's answer is the exclusion rule above: the pipeline covers the 2M-triangle static set, not the foliage.
- The failure mode is visible while moving (camera/player motion exposes the leaf glitches), so the check is a moving-camera pass, not a still.

**Why**
- A culling pipeline cannot fix fragment-shader cost (leaves) or beat a system that already culls itself (tile-based grass LOD). Applying it there costs correctness for no speed.

## The human method, distilled

1. **Measure the same spot before and after.** 20-25 fps -> 30-35 fps on an M1 Mac is the claim; both numbers are stated.
2. **Report the rendered fraction, not just fps.** ~25% of ~2M triangles is the proof.
3. **Name what you excluded and why.** Leaves (wind-shader glitch, fragment-bound) and grass (own LOD system) are exclusions with reasons, not omissions.
4. **First iteration, stated as such.** "Also, this is the first iteration. I am sure it will get better." (author)

## Failure modes

- **Leaves glitch while moving.** Wind-animated leaves in a custom shader show visible glitches with meshlets as the player moves. Exclude leaves from the pipeline; the estimated gain there is only 10-15% anyway.
- **Grass does not need it.** Tile-based grass with its own LOD system is already at maximum performance; adding meshlets adds nothing.
- **Foliage-heavy scenes are the open question.** The stress-test skill's independent benchmark already warned that an outdoor environment (trees, 3D grasses, plants, water) "did not provide much benefit" from meshlets. This forest result agrees: the win is on the static set, not the foliage.

## Relation to the stress-test skill

- `meshlet-drawing-pipeline-threejs` (Sara_KumoDeck, Nov 4): the pipeline mechanics, the material-batch crash (give each size class its own material instance), the 16-21 s cluster-preparation cost, the WebGL2 fallback, and the cluster visualizer. Read it before wiring the pipeline.
- This skill: the application rules for a real outdoor scene. The two agree on the numbers that matter (rendered fraction, same-spot fps) and on the foliage caveat.

**Depth status:** PARTIAL (exact numbers + inclusion/exclusion rules + failure mode; no code, no cluster sizes, no profiler breakdown).
