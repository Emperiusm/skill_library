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
