---
name: project-prales-runtime-wilderness
description: "Generate 16 km2 of Central European wilderness at runtime in Unreal Engine 5 from a single seed: river-first terrain, whole-world hydrology, ecology-driven vegetation placement, world-hash determinism, and honest FPS reporting. Trigger when a game needs a large seeded wilderness where every plant has a reason to grow where it does."
---

# Project Prales: Runtime Wilderness Generation in UE5 (16 km2, One Seed)

## Purpose

This skill reconstructs the exact workflow haithegreat describes for
Project Prales (r/proceduralgeneration, 2026-11-09), step by step, so
another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The workflow's core method is: let the seed build the
world, let ecology place the forest, and verify with a hash.

## Source

Creator: haithegreat (Project Prales).

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xr7pia/i_built_a_runtime_generator_for_16_km%C2%B2_of_central/
(r/proceduralgeneration post 1xr7pia, score 98, 13 comments) |
2026-11-09 scout run. Full trailer:
https://www.youtube.com/watch?v=dy4c_mUn9m4.
Evidence: full author post text + 13 comments with exact placement
rules, species-by-slope mapping, and measured FPS.

## Tools used

Tools used: **Unreal Engine 5 (C++)**, **Quixel Megaplants** (free on
Fab) for tree models, **Claude Code** (assisted development).

## Phase 1: Carve terrain river-first

**Do**
1. Generate terrain from large-scale elevation patterns.
2. Carve valleys where the drainage wants to go: river-first
   heightfield, plus hills, ridges, cliffs and tors. "Cliffs are
   created through steep elevation transitions and terrain shaping."
3. Store terrain data in a grid-based node system rather than simulating
   every square meter.

**Check**
- The "world builds itself" sequence in the video draws the real
  generated data (contours, rivers, forest, trails) over the rendered
  terrain of seed 100001; the overlay must match the terrain
  underneath.
- Every number gives a different 4 x 4 km world; the same seed must
  give the same world, "tested by world hashes."

**Why**
Rivers decide the valleys, so the terrain follows the water instead of
the water being pasted onto finished terrain. A node grid keeps the
data manageable at 16 km2.

## Phase 2: Run hydrology over the whole world

**Do**
1. Compute drainage and flow accumulation across the whole world.
2. Rivers always run downhill; smaller streams merge into larger
   rivers. Add lakes, springs, and marshes where the flow says water
   collects.

**Check**
- A river that runs uphill is a bug in the drainage pass, not in the
  terrain; check flow direction before adding vegetation, since the
  forest placement reads the same moisture data.

**Why**
Hydrology is computed on the whole world at once, so a stream in one
valley and a lake in the next agree with each other; local water
features would not.

## Phase 3: Derive climate, biomes, and vegetation from the ecology

**Do**
1. Run a climate pass over sunlight, temperature, and moisture; biomes
   follow elevation, moisture, and exposure.
2. Place vegetation from that ecology, with no random scatter layers:
   "beech on the middle slopes, spruce higher up, pine on dry rocky
   ground, alder along streams." (Author comment, quoted.)
3. Open land needs a reason: marsh on wet flats, dry grass on sunny
   slopes.
4. Scatter trees with coordinate-hashed randomness, plus canopy gaps,
   edge shrubs, and deadwood from windthrow. "Same seed, same forest."
5. Add rocks, deadwood, ground cover, two isolated forest huts, and
   dirt tracks. Day and night plus dynamic weather.

**Check**
- The honest split, stated by the author: "the plant models aren't
  generated. The trees are Quixel Megaplants (free on Fab). What's
  procedural is where things grow." Do not claim generated trees; the
  generation is placement, not models.
- Check a slope by eye: the wrong tree on the wrong slope means the
  climate pass is wrong, not the scatter.

**Why**
Ecology-driven placement is the difference between a forest and a
scatter layer: every tree has a reason (slope, moisture, exposure) a
player could infer by looking at the land. Coordinate-hashed
randomness keeps it deterministic without storing a placement table.

## Phase 4: Measure performance, render the trailer offline

**Do**
1. Measure on real hardware: "around 60 FPS on Epic, 90 FPS on High
   and 120 FPS on Medium at 1080p, using a Ryzen 5 7600 and RX 6900
   XT." (Author comment.)
2. Render the trailer offline from the game, frame by frame at 4K60.
   The author is explicit that the trailer "was rendered offline at
   4K, though, so it's not representative of actual gameplay. Still
   got plenty of optimization work ahead of me!"

**Check**
- The FPS numbers are the gameplay claim; the trailer is not. Do not
  quote 4K60 as gameplay performance.

**Why**
Offline rendering buys a beautiful trailer without pretending the game
runs that way; the FPS numbers are reported separately and honestly.

## Phase 5: Build it with an AI assistant, in the right order

**Do**
1. "Claude Code helped me quite a bit throughout development. It was
   especially useful for implementing systems and working through bugs
   and glitches." (Author comment.)
2. The author's recommended study order for someone starting in this
   direction: "starting with procedural terrain generation and
   hydraulic erosion. There's a lot to learn by experimenting with
   these!"

**Check**
- Seasons (with snowy winters) are next; there is no public build yet,
  so nothing here is verified by a player.

**Why**
Terrain first, erosion second: those two systems are the foundation
the hydrology, climate, and placement passes all read from.

## AAA studio practice

Project Prales' pipeline, river-first terrain, whole-world hydrology,
ecology-driven placement, one seed, hash-verified determinism, is the
same pipeline AAA open worlds run, split across two reference
implementations: Far Cry 5 does it at authoring time with nightly
rebuilds, No Man's Sky does it at runtime, continuously. Prales is
the runtime version of the Far Cry 5 recipe, which is why both
anchors matter.

- **Ubisoft Montreal, Far Cry 5: sequential tools, data handoffs,
  ecology as recipes.** Technical artist Etienne Carrier's team built
  the Hope County pipeline in Houdini with Houdini Engine inside the
  Dunia editor: procedural tools for freshwater networks, cliffs,
  biomes, fog density, and the world map. Generation ran sequentially,
  freshwater, then cliffs, then biomes, and each tool exported data
  the next one read: the freshwater pass produced a water mask the
  biome tool consumed. Biome recipes reacted to the physical features
  of the land, water proximity, altitude, cliff erosion lines, "to
  ensure coherence throughout the world," and the team reflected
  terrain humidity through the grasses and oriented grass assets on a
  wind vector map. That is Prales' Phase 2 feeding Phase 3, stated as
  a production rule: no stage reads raw noise when it can read the
  previous stage's output.
  (https://christianjmills.com/posts/procedural-tools-far-cry-5-notes/index.html)
  (https://blog.playstation.com/archive/2018/03/22/how-the-stunning-open-world-of-far-cry-5s-hope-county-montana-was-created)
- **Hello Games, No Man's Sky (GDC 2017): runtime generation as a
  continuous pipeline, nothing stored.** Innes McKendrick's GDC 2017
  talk breaks the pipeline into voxel-based world generation, then
  polygonization, then texturing, then population, then simulation,
  running continuously in real time as the player moves, so a player
  can fly from space to interactive, populated terrain without a level
  load. A single 64-bit seed defines everything about a planet, and
  nothing is stored: the same rules re-derived from the same seed
  produce the same world. Prales' "tested by world hashes" is the
  small-scale version of the same contract, and its grid-based node
  system is the same answer to the same problem (16 km2 is too much
  to simulate per square meter).
  (https://www.gamedeveloper.com/programming/video-how-continuous-world-generation-works-in-i-no-man-s-sky-i-)
- **The offline/runtime split, stated plainly.** Far Cry 5's tools ran
  as nightly builds on build machines to fully refresh the world
  daily, plus in-editor tools for on-demand generation; the shipped
  world is fixed. No Man's Sky generates at runtime and never stores
  the result. Prales chose the NMS side of that split, so its
  automation must answer the runtime question Far Cry 5 never had
  to: what is the per-frame and per-chunk generation budget, and what
  happens when the player outruns it. The FPS numbers in Phase 4 are
  the start of that answer, not the end of it.

### Agent-executable upgrades

1. **Stage-order manifest with hashes.** Keep
   `worldgen-stages.json`: one entry per stage (terrain, hydrology,
   climate, placement) recording its input data (with SHA-256 hash),
   its output data (with hash), and the seed. A stage may not run
   until its input hash matches the previous stage's output hash.
   This is the Far Cry 5 water-mask handoff made checkable: a biome
   pass running on a stale moisture map fails the gate instead of
   placing spruce on a dry ridge.
2. **World-hash regression test.** On every change to the generator,
   run the same seed (e.g. 100001) and compare the world hash against
   the stored value in `world-hashes.jsonl`. A hash change without an
   intentional generator change is a regression; a hash change with
   one is logged with the reason. Same seed, same world is a test
   that runs, not a claim in a comment.
3. **Slope-species audit.** Sample N coordinates per world (seeded
   sample, recorded in the manifest), and for each, verify the species
   placed matches the slope/moisture/exposure rule (beech on middle
   slopes, spruce higher up, pine on dry rocky ground, alder along
   streams). Log every violation with its coordinates; a violation
   means the climate pass is wrong, not the scatter, per Phase 3.
4. **FPS budget log.** Keep `perf-log.json` with FPS per quality
   preset (Epic/High/Medium) at 1080p on named hardware (Ryzen 5
   7600, RX 6900 XT), measured on the shipped build, not the editor.
   Any preset that drops below its recorded baseline fails the week.
   Offline trailer renders are logged separately and labeled
   "offline render, not gameplay" in the same file, so the two numbers
   can never be quoted interchangeably.
5. **River-direction check.** Before the vegetation pass runs, verify
   by script that every river segment flows downhill along the flow-
   accumulation map. A river that runs uphill is a drainage-pass bug;
   catch it here, before the forest placement reads the same moisture
   data and inherits the error.

## The human method, distilled

1. **Rivers first.** The drainage decides the valleys; everything else
   reads the water.
2. **Ecology, not scatter.** Every plant has a reason (slope, moisture,
   exposure); open land needs a reason too.
3. **Same seed, same world, proven by hash.** Determinism is tested,
   not asserted.
4. **Say what is procedural and what is not.** The trees are Quixel
   assets; the placement is the procedural part.
5. **Report the real FPS and label the trailer.** 60/90/120 at 1080p
   is the claim; 4K60 is an offline render.

**Depth status:** PARTIAL (full author post text + 13 comments with
exact placement rules, species-by-slope mapping, and measured FPS; no
node graph, code, or parameters beyond those quoted; plant models are
disclosed as Quixel assets, not generated; the full trailer on YouTube
was not downloaded, the run's 2-download allowance was spent on the
NodeMode and Floaters videos, and a download would add trailer frames
only, no narration is stated to exist).
