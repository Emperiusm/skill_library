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

## AAA studio practice

The author's three core decisions, rivers carve first, scatter by coverage, and GPU-culled impostors, are the same three decisions Ubisoft and Sucker Punch made at AAA scale, with the same justifications.

- **Ubisoft Montreal, Far Cry 5 (GDC 2018; PlayStation Blog).** The procedural pipeline built in Houdini and Houdini Engine generates freshwater networks, cliffs, and vegetation as one ecosystem: artists lay down splines for rivers, and procedural generation creates the water surface, waterside assets, and terrain texturing from the spline parameters. Biome recipes react to the physical features of the land (altitude, humidity, cliff erosion lines) to spawn appropriate assets, and the cliff tool extends its mask with a flow simulation for the erosion effect.
  (https://blog.playstation.com/2018/03/22/the-procedural-world-generation-of-far-cry-5/)
  The direct parallel: rivers-carve-first is the Far Cry 5 freshwater tool in miniature, and the biome bands by elevation are the same recipe-reacts-to-terrain rule.
- **Sucker Punch, Ghost of Tsushima (GDC 2021).** Procedural tools built the island's 40+ biomes and three million trees because hand-placement was impossible at that scale; the procedural grass system renders about 83,000 blades per frame in roughly 2.5 ms on a compute-shader pipeline, using a clumping algorithm on artist-authored parameters, Bezier-shaped blades, a per-blade hash for unique sway, and a two-tier LOD that drops three of every four blades at distance. The same wind system drives grass, trees, and bushes so the foliage matches.
  (https://gameindustrylibrary.com/documents/procedural-grass-in-ghost-of-tsushima)
  (https://blog.playstation.com/2020/07/09/crafting-the-world-of-tsushima/?ref-cat=249748)
  The direct parallel: baked impostors plus GPU culling through ExecuteIndirect is the custom-engine version of the same density-at-distance problem, and the author's fps-before/after reporting (80-90 to 100-115) is the same optimization discipline.

**Agent automation**

1. **Terrain contract.** Keep `forest-terrain.json` per world: heightfield hash, per-tile erosion-bake hash, river channel polylines, and a water-surface agreement check (sample the water height against the channel bed at N points; any point where the surface floats above or sinks below the bed fails the bake).
2. **Scatter-coverage audit.** For each biome band, record the target coverage fraction and the measured placed-instance density, plus a patchiness check (largest empty disc inside the band, in metres). A band whose largest empty disc exceeds the author's stated fix threshold is flagged for a scatter-math change, not more trees.
3. **LOD budget log.** After each optimization pass, append fps (min/median/max), instance counts, and the change made to the log, the way the author reports 80-90 to 100-115. A pass with no before/after numbers is not an optimization.
4. **Floating-origin rebase test.** Assert the 1 km rebase triggers at the documented distance and that no visible pop occurs at the rebase; log the rebase distance and any pop frames as a regression check.

**Depth status:** PARTIAL (full post text + 25 of 26 comments; the author's long state-of-the-world comment is truncated mid-sentence in the Arctic Shift source at "wind is rotation aroun", so the vegetation/wind detail ends there; no engine code or parameters beyond what is quoted above).
