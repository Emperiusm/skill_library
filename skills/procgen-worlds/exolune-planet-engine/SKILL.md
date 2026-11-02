---
name: exolune-planet-engine
description: "Real-scale planet terrain: simulate plates at startup in under a second, derive terrain from boundary distance, climate from winds and relief, evaluate per point on the GPU each frame with no streaming. Trigger when a planet needs to be 1:1 scale and flyable from orbit to ground in one shot."
---

# Exolune Planet Engine

## Purpose

This skill reconstructs the author's exact technique, step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The engine's core method is: simulate plates once at startup in under a
second, then evaluate everything per point on the GPU every frame — so a
1:1-scale planet needs no streaming.

## Source

Creator: Fresh-Daikon-9408. Repo: https://github.com/exolunehq/exolune (open,
with documentation on the making).
Reddit post: https://www.reddit.com/r/proceduralgeneration/comments/1xkibsb/realscale_planet_terrain_from_plate_tectonics_and/
(r/proceduralgeneration post 1xkibsb, score 84, 12 comments) | 2026-11-01
scout run, audit 5.

## Tools used

**Exolune** (github.com/exolunehq/exolune). The author rebuilt the terrain
"from scratch" following community feedback on plate tectonics.

## Phase 1: Simulate plates at startup (< 1 s per planet)

**Do**
1. Simulate plates at startup; budget **under one second per planet**.
2. Type every boundary: **collisions, subduction trenches, rifts, ridges,
   transforms, active and passive margins**.

**Check**
- All boundary types present and typed; startup stays under the second.

**Why**
- One fast sim replaces baked heightmaps; plates are data, not assets.

## Phase 2: Derive terrain from boundary distance

**Do**
1. Compute the large forms as **profiles on the distance to the boundaries**.
2. Drive the noise detail by the **local geology**.

**Check**
- The author's emergent benchmarks on the default Earth-sized planet
  (**6,378 km radius**): highest peak **8,541 m** (a stratovolcano sitting on
  top of a mountain range); deepest point **10,539 m below sea level** (at the
  bottom of a subduction trench); about **19 km of total relief**, in the
  range of Everest (8,849 m) and the Challenger Deep (~10,935 m). The plate
  boundary profiles are calibrated on Earth's — "but nobody placed these two
  spots: they come out of the plate simulation."

**Why**
- Emergent extremes are the acceptance test: if the sim is right, Everest
  and the trench appear on their own.

## Phase 3: Climate from winds and relief

**Do**
1. Derive climate from **prevailing winds and relief**: wet windward slopes,
   rain shadows, deserts under the subtropical highs.
2. Let **vegetation, snow, and clouds** follow the climate.
3. Add **volcanism**: arcs, hotspot chains, atolls. (Erosion — river valleys,
   glaciers, coastal cliffs — is the author's stated next step.)

**Check**
- Deserts sit under the subtropical highs; vegetation tracks moisture.

**Why**
- Climate is derived, not painted; it follows the same terrain the plates
  made.

## Phase 4: Render per point on the GPU, no streaming

**Do**
1. Evaluate everything **per point on the GPU each frame**, in **double
   precision near the ground**.
2. Stream nothing: fly **from orbit down to a pebble in one shot**.

**Check**
- One continuous flight, no loading, no streaming hitches; precision holds
  at ground level.

**Why**
- (author): "One of the advantage of this rendering engine is that there is
  no loading nor streaming, so no flight speed limitation." Per-point GPU
  evaluation is what makes 1:1 scale tractable.

## AAA studio practice

No shipped title documents exolune's exact design (per-point GPU evaluation
in double precision, startup plate sim under a second) -- the closest shipped
anchors are math-evaluated planets, 64-bit coordinate spaces, tectonic-mask
terrain, and first-principles formation sims.

- **Nothing on disk: planets as math (Hello Games, No Man's Sky, GDC
  2017).** "Nothing exists on disk, or in the cloud": everything visible is
  generated from math when the player arrives; a deterministic engine (single
  seed + PRNG) re-creates identical features; planets are stored as cubes and
  cast onto a sphere; the whole planet first appears as a low-detail sphere
  with detail arriving on approach, holding a 30 fps budget.
  (https://www.gamedeveloper.com/programming/video-how-continuous-world-generation-works-in-i-no-man-s-sky-i-, https://www.thesixthaxis.com/2014/06/25/crafting-the-endless-cosmos-of-no-mans-sky/)
- **64-bit coordinates + seamless macro-to-micro (Cloud Imperium, Star
  Citizen).** The engine moved to 64-bit coordinates for solar-system scale;
  planets are nested object containers streamed in the background so
  high-speed traversal has no loading screens; planet tech v4 builds biomes
  from temperature + humidity + height map, with artists placing mountain and
  ocean zones and procedural rules filling in.
  (https://www.digitalfoundry.net/articles/digitalfoundry-2020-star-citizen-tech-focus-alpha-3-point-8)
- **Tectonic masks drive terrain (Frontier Developments, Elite Dangerous:
  Horizons).** Matt Dickinson, head of technical art: "We generate these
  tectonic masks... we understand the compression of the plates, so we can
  see where they'd move together and move apart. That creates where ridges
  are formed, mountains, or trenches." 1:1-scale worlds with seamless
  space-to-surface journeys, no loading screens. Stellar Forge predicted
  Pluto's appearance before NASA's New Horizons flyby -- shipped-studio
  precedent for emergence-as-acceptance-test.
  (https://www.polygon.com/features/2015/11/20/9772708/elite-dangerous-horizons-expansion-adds-planetary-landings-on, https://www.impulsegamer.com/frontier-developments-announces-elite-dangerous-horizons/)
- **GPU-evaluated terrain density functions (Ryan Geiss, NVIDIA, GPU Gems
  3).** The terrain surface is one density function f(x,y,z); GPU marching
  cubes builds geometry at interactive framerates; LOD follows camera
  distance with popping killed via alpha-fade transitions or
  density-function erosion.
  (https://developer.nvidia.com/gpugems/gpugems3/part-i-geometry/chapter-1-generating-complex-procedural-terrains-using-gpu)
- **Honest gaps:** no shipped title documents per-point double-precision GPU
  evaluation with zero caching/streaming (NMS streams voxel detail; Star
  Citizen bakes height maps offline); no AAA anchor for a startup plate sim
  under one second.

## Agent automation

- **Emergence acceptance test:** calibrate boundary profiles on Earth, then
  assert emergent extremes land within tolerance of Everest (~8,849 m) and
  the Challenger Deep (~10,935 m) -- the test Elite ran against real Pluto
  data.
- **Determinism check:** seed -> feature hash; assert byte-identical results
  across sessions and restarts (NMS determinism design).
- **Precision audit:** compute required coordinate precision from planet
  radius + minimum feature size; verify no vertex jitter at ground level
  (Star Citizen 64-bit rationale).
- **Transition test:** log a continuous orbit-to-ground descent; assert zero
  load events and no frame-time spike above threshold (Star Citizen's
  no-loading bar); flag terrain LOD pops (GPU Gems 3 transition checks).
- **GPU-evaluation purity check:** verify the density/terrain function takes
  no per-frame CPU input beyond camera and uniforms, so terrain is
  math-evaluated, not streamed.

## The human method, distilled

1. **Calibrate on Earth, trust emergence**: boundary profiles from Earth's,
   then let the peaks and trenches surprise you.
2. **Fast startup is a feature**: plates in under a second means planets are
   disposable — generate, fly, discard.
3. **Open the repo and the docs early**: the author explicitly welcomes
   feedback and contributors.

**Depth status:** FULL (startup budget, boundary type list, 1:1 scale number,
GPU eval design, and the emergent peak/trench benchmarks, all from the
author).
