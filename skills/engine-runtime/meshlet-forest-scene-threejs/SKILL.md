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

**Check**
- Rendered-triangle fraction (~25% of ~2M) is the number that proves the culling works; fps alone would not separate culling from other changes.

**Why**
- Meshlets pay on static, triangle-heavy geometry. The inclusion list is exactly that class of geometry.

## Phase 3: Exclude what it does not help (the exclusion rule)

**Do**
1. Keep leaves OUT of the meshlet pipeline. Leaves have wind movement in a custom shader, and with meshlets "there seem to be visible glitches in leaves as the player moves." Remove meshlets from leaves.
2. Keep grass OUT. The grass runs on a tile-based rendering architecture with its own LOD system, so "it already has maximum performance. It doesn't need meshlet pipeline."
3. (Author's estimate, not measured): if meshlets ran on leaves, the gain would be 10-15%, "not a huge one," because leaves are heavy on the fragment shader and don't have that many triangles.

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
