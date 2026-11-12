---
name: procedural-pnw-forest-custom-engine
description: "Build a procedural Pacific Northwest forest in a custom C++20/DirectX 12 engine: heightfield terrain with a per-tile stream-power erosion bake, rivers that carve first with the water surface following the channel, area-coverage scatter instead of dart-throwing, FFT ocean cascades, volumetric snow that keeps footprints, baked impostors with GPU culling through a compute pass feeding ExecuteIndirect, and a floating origin with a 1 km rebase. 100-115 fps on a laptop RTX 4060. Includes the author's own state check (world and renderer, no gameplay yet) and the scatter fix that stopped patchy forest edges. Trigger when terrain, erosion, scatter, or forest LOD is needed in a custom engine."
---

# Procedural PNW Forest in a Custom C++/DirectX 12 Engine

## Purpose

This skill reconstructs the procedural forest workflow from the author's post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: generate everything, hand-place nothing, and make the water obey the terrain instead of the other way around.

## Source

Creator: Devilsclub_dev. Reddit post:
https://www.reddit.com/r/proceduralgeneration/comments/1xto3nb/my_procedural_pnw_forest_six_months_apart_custom/
(r/proceduralgeneration post 1xto3nb, score 127, 26 comments) | 2026-11-12 scout run, audit 1. For a survival horror set in rural Washington. Engine is the author's own: C++20 and DirectX 12, Windows only, no Unreal or Unity. First file was June 2026.

## Tools used

Custom engine (**C++20** + **DirectX 12**, Windows only); heightfield terrain; **stream-power erosion**; **FFT ocean cascades**; volumetric snow; baked impostors; GPU culling via compute pass + **ExecuteIndirect**; **QEM LOD** for boulders; floating origin (1 km rebase).

## Phase 1: Bake the terrain with stream-power erosion

**Do**
1. Start from a heightfield. Run a stream-power erosion pass baked per tile; the ridges and valley cuts come from this pass.
2. Carve rivers into the terrain FIRST, then lay the water surface along the carved channel afterwards.

**Check**
- Water never floats above the bed or sinks under it; the channel and the surface agree by construction.
- The author states the "before" clip is from six months ago; the comparison is the same forest, six months of work apart.

**Why**
- Erosion first means the terrain already knows where water belongs. A surface laid over uneroded ground is a leak waiting to be found.

## Phase 2: Scatter by area coverage, not dart-throwing

**Do**
1. Solve scatter density by area coverage rather than dart-throwing. Every tree, rock, and boulder is placed by the generator; nothing is hand-placed.
2. Use biome bands by elevation: meadows, glades, beaches, snow by elevation, plus couloirs that deform under the player's feet.

**Check**
- Forest edges stop going patchy; the author names this as the specific fix the area-coverage solve delivered.

**Why**
- Dart-throwing gives clumps and gaps at the same density. Coverage-based scatter spends the budget where the area actually is.

## Phase 3: Water as FFT ocean cascades

**Do**
1. Render water as FFT ocean cascades, with two-term absorption for depth, ripples from footsteps, mips on the FFT targets, and LOD on the far grid.
2. Keep the snow volumetric so it keeps footprints.

**Check**
- The author reports the frame rate on a laptop RTX 4060 rose from 80-90 fps to 100-115 fps since posting the video, while working on optimisation, speed, and city generation.

**Why**
- Cascades and mip/LOD discipline are what let an FFT ocean run on a laptop GPU while the rest of the world is also being generated.

## Phase 4: Vegetation as impostors with GPU culling

**Do**
1. Build trees with variants and baked impostors. Cull on the GPU in a compute pass feeding ExecuteIndirect.
2. Understory is ferns, saplings, shrubs, and flowers; grass cards blend into mesh grass; boulders use QEM LOD.
3. Foliage is alpha cutout on polygons ("two faced", per the author's truncated comment), with wind and lighting applied.
4. Run a floating origin with a 1 km rebase; the author describes the generation as an "optimised infinity world with oceans, mountains, biomes and cities".

**Check**
- The author's own state check: "no character animation, no sound, no ai, no gameplay. its a world and a renderer, not a game yet" (commenter fripletister's summary, not disputed by the author).

**Why**
- Impostors plus GPU culling is the only way a forest this dense stays above 100 fps on a laptop. The world is the product here; gameplay comes later, in cities, per the author.

## The human method, distilled

1. Generate everything; hand-place nothing.
2. Rivers carve first, water follows. (Author's words: "rivers carve the ground first, water surface follows the channel afterwards so it never floats or sinks.")
3. Fix patchiness by changing the scatter math, not by placing more trees.
4. Optimise in public: report the fps before and after (80-90 to 100-115 on a laptop 4060).

**Depth status:** PARTIAL (full post text + 25 of 26 comments; the author's long state-of-the-world comment is truncated mid-sentence in the Arctic Shift source at "wind is rotation aroun", so the vegetation/wind detail ends there; no engine code or parameters beyond what is quoted above).
