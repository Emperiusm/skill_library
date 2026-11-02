---
name: chronicle-of-gods-planet-pipeline
description: "Seeded planet generation on a cube-sphere: a fixed six-stage pipeline (crust, Voronoi plates, elevation/sea level, climate, hydrology flood-judge-carve, biomes) with biome regions as the simulation unit. Trigger when a game needs whole worlds generated from a seed with history on top."
---

# Chronicle of Gods Cube-Sphere Planet Pipeline

## Purpose

This skill reconstructs the author's exact six-stage generator, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The generator's core method is: one seed, six fixed stages run
once per world, on a cube-sphere whose tiles are grouped into biome regions —
and the history simulation then runs on regions, not tiles.

## Source

Creator: chronicleofgods (game: *Chronicle of Gods*,
https://store.steampowered.com/app/5221390/).
Reddit post: https://www.reddit.com/r/proceduralgeneration/comments/1xkggn9/four_generated_worlds_on_a_cubesphere_plates_then/
(r/proceduralgeneration post 1xkggn9, score 72, 12 comments) | 2026-11-01
scout run, audit 4.

## Tools used

The author's custom generator for the god game *Chronicle of Gods*. Surface:
**cube-sphere, six square faces with 5 km tiles**.

## Phase 1: Crust — where the continents sit

**Do**
1. From the seed, place the continents.

**Check**
- The landmass layout reads at a glance on the parchment-atlas render.

**Why**
- Everything downstream (plates, climate, realms) inherits from this one
  placement; get the continents right first.

## Phase 2: Plates — Voronoi tectonics

**Do**
1. Run **Voronoi tectonics** over the crust.
2. Where plates push together, raise **mountain ranges**; where they pull
   apart, cut **rifts**; at sea, place **trenches**.

**Check**
- Mountain chains sit on convergence boundaries; rifts on divergence.

**Why**
- Terrain features inherit from plate boundaries, so the map tells a
  geological story instead of being noise with excuses.

## Phase 3: Elevation, then solve for sea level

**Do**
1. Compute elevation from the plate features.
2. **Solve for the sea level** that partitions land from ocean.

**Check**
- Continent/ocean balance looks plausible before climate runs.

**Why**
- Sea level is a solved value, not a tuned constant; the elevation field
  decides it.

## Phase 4: Climate — temperature, moisture, rain shadows

**Do**
1. Temperature from **latitude and height**.
2. Moisture from **rain bands**, with **rain shadows behind the mountains**.

**Check**
- Wet windward, dry leeward; deserts and jungles land where the rules say.

**Why**
- Two drivers (latitude/height, rain bands) produce the whole climate;
  mountains are climate machines, not decoration.

## Phase 5: Hydrology — flood, judge, and carve

**Do**
1. **Flood** the basins, **judge** them, then **carve**: basins fill, small
   ones get culled, dry ones drain instead of staying lakes, and rivers carve
   their way out to the sea.

**Check**
- Lakes span sizes from small to inland seas. The author's hard-won tuning:
  the first settings culled every lake under a size, so every survivor was a
  huge inland sea and there were no small ones. Lowering the floor and
  letting dry basins drain fixed it — and as a side effect added rivers,
  "because a drained basin has to empty somewhere."

**Why**
- The lake-culling floor is the tuning knob that decides whether the world
  has rivers at all; hydrology is a judgment loop, not a one-shot fill.

## Phase 6: Fertility and biomes — moisture spreads, lookup decides

**Do**
1. Spread river and lake moisture into the surrounding land.
2. Assign each tile's biome by lookup on **temperature band x moisture band**.
3. Group tiles into **regions that follow the biomes**; the simulation works
   on those regions, not on single tiles.

**Check**
- Region boundaries follow biome boundaries. The parchment-atlas render
  shows four worlds, each from a seed, with the colored patches being realms
  the simulation grew on top of the terrain. Only two map layers are on in
  the author's clip (realms and their wars, fog lifted); in play only part
  of the world is visible at a time.

**Why**
- Regions are the simulation's unit of work (the mortal realms grow on top
  of the terrain as colored patches); single tiles are too fine to simulate
  history on.

## AAA studio practice

The six-stage fixed pipeline (geography -> climate -> hydrology -> biomes ->
history) is the same architecture shipped games use: Dwarf Fortress runs it
verbatim, No Man's Sky computes it continuously from one seed, and Stellar
Forge simulates formation from first principles.

- **Staged pipeline, finalized elevation before climate (Bay 12 Games, Dwarf
  Fortress).** The generator seeds elevation, rainfall, temperature,
  drainage, and volcanism, then derives vegetation, places volcanoes, then
  runs an erosion and river stage: "Many fake rivers flow downward... carving
  channels in the elevation field"; lakes are grown along rivers. Climate
  reads finalized elevation only: "Now that the elevations are finalized, it
  makes adjustments to rainfall based on rain shadows... Temperatures are
  reset based on elevation and rainfall." Seeds are logged in gamelog.txt;
  rejection parameters act as automated acceptance gates -- a world that
  fails any parameter "is rejected and re-randomised."
  (https://dwarffortresswiki.org/index.php?title=World, http://dwarffortresswiki.org/index.php/Advanced_world_generation)
- **History layered strictly after geography (Dwarf Fortress).** "After
  generating the world, Dwarf Fortress will generate a history for that
  world... a giant zero-player strategy game... history is just a record of
  that"; civilizations place only where geography allows (kobold civs are
  skipped if no caves exist) -- the direct parallel to this skill's
  regions-as-history-unit.
  (https://dwarffortresswiki.org/index.php?title=World)
- **Continuous generation from one seed, cube-to-sphere (Hello Games, No
  Man's Sky, GDC 2017).** Voxel worldgen -> polygonization -> texturing ->
  population and simulation, from a single 64-bit seed; McKendrick solved
  the sphere problem by storing surface data "in a mathematical cube" and
  transposing it onto a sphere -- the same cube-sphere architecture as this
  skill. Automated debugging: "virtual space probes to fly around the
  universe, make gifs of the planets, and report back" -- scripted seed
  walkthroughs as acceptance sampling.
  (https://www.gamedeveloper.com/programming/video-how-continuous-world-generation-works-in-i-no-man-s-sky-i-, https://www.fastcompany.com/3048667/how-4-designers-built-a-game-with-184-quintillion-unique-planets/)
- **Formation simulated from first principles (Frontier Developments, Elite
  Dangerous Stellar Forge).** Systems are "formed from first principles...
  taking into account its chemical composition"; terrain runs tectonic
  simulations -- "it's not just generating heightmaps from noise"; craters
  reflect recorded impacts from the formation sim; systems regenerate
  identically every visit. Human override: pinned real bodies (e.g.
  Trappist-1) re-run the sim around them.
  (https://www.polygon.com/2014/12/4/7333709/elite-dangerous-milky-way-stellar-forge-human-cruelty, https://procedural-generation.isaackarth.com/2015/11/23/elite-dangerous-2014-planet-generation.html)
- **Honest gaps:** no named AAA title publishes Voronoi-based plate
  generation (Stellar Forge runs tectonic sims but Frontier has not published
  the method); no AAA source documents an explicit flood/judge/carve
  hydrology judgment loop (DF's is carve-first); no 80 Level article found on
  these internals.

## Agent automation

- **Determinism gate:** log the seed per world; regenerate and checksum the
  output to prove same seed -> same world (DF gamelog.txt convention; NMS
  64-bit-seed design).
- **Pipeline-order check:** assert climate and hydrology stages read the
  finalized elevation field, never a mutable intermediate (DF resets
  temperature only after elevations are finalized).
- **Rejection-parameter validation:** encode world acceptance criteria
  (mountain counts, biome coverage, river presence) as pass/fail gates that
  reject and re-randomize (DF "belt and braces" parameters).
- **Feature provenance:** tag surface features with the simulation stage
  that produced them (Stellar Forge crater = recorded impact), giving an
  audit trail from cause to visible feature.
- **Sampling probes:** scripted walkthroughs that render N random seeds and
  report the samples for review (NMS space-probe GIFs).
- **Ground-truth pinning:** pin known observations as immutable constraints;
  a validation script flags any generated world violating them before it
  proceeds downstream (Stellar Forge Trappist-1 correction).

## The human method, distilled

1. **Fixed pipeline, run once**: crust -> plates -> elevation/sea level ->
   climate -> hydrology -> biomes. Order is load-bearing.
2. **Tune the judgment loops, not the noise**: the lake floor setting decided
   the world's rivers.
3. **Ask the open question in the open**: the author asks readers who did
   rivers on a sphere whether they carved from the heightmap like this or
   routed first and cut the terrain to fit (commenter MrNotmark: route then
   carve — "much easier").
4. **Disclosure as method**: the author states the marketing text is mostly
   AI-generated (reread and reiterated many times; the Steam page took many
   hours), and that playtests start on Discord in a week or two.

**Depth status:** FULL (author's six-stage pipeline verbatim + the
lake-tuning story + the region-over-tile simulation design).
