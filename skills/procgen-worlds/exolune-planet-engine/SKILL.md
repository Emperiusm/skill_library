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
Update: https://www.reddit.com/r/proceduralgeneration/comments/1xw7j9d/from_a_moon_to_a_city_on_a_11_earthscale_planet/
(r/proceduralgeneration post 1xw7j9d, score 79, 32 comments) | 2026-11-15
scout run, audit 4. The update adds rivers, moons, precision handling, a
city layer, and a cinematic mode; phases 5-8 below come from it.

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
   glaciers, coastal cliffs — was the author's stated next step in the Nov 1
   post; rivers shipped in the Nov 15 update, phase 5 below.)

## Phase 5: Compute rivers once for the whole planet (2026-11-15 update)

**Do**
1. Compute a drainage network once for the whole planet, so every river ends
   in the sea or a lake.
2. Carve valleys and river beds per point on the GPU, like noise, so nothing
   is simulated in tiles and nothing streams.

**Check**
- Every river terminates in the sea or a lake; no river ends mid-air or in a
  dry hole. (Author's stated invariant.)

**Why**
- A global drainage network computed once cannot contradict itself across
  tile borders, because there are no tile borders.

## Phase 6: Moons that share the terrain stack (2026-11-15 update)

**Do**
1. Add three airless moons, 1,800, 700, and 260 km in radius.
2. Give them fractured highlands and impact craters in nine size bands, from
   hundreds of kilometres down to a few metres.
3. Let them share the planet's landable terrain stack, so you can land on
   each of them.

**Check**
- The video is one continuous take: a ship takes off from a moon, passes a
  second one, comes down on the planet at dawn along a snowy range, skims a
  sea of clouds, and lands at the spaceport of a small hill city. The moons
  are landable, not skyboxes.

**Why**
- Sharing the terrain stack means the moons cost a parameter set, not a
  second engine.

## Phase 7: Solve the precision problem (2026-11-15 update)

**Do**
1. Keep positions as doubles on the CPU.
2. Center the terrain mesh under the camera, so the GPU renders with small
   camera-relative floats.
3. Feed the noise absolute planet coordinates: a float only has 0.5 m steps
   at Earth radius, so use doubles in the compute shader, but GPU doubles
   are really slow, so use them close range only, and use a pair of floats
   faking a double while flying (author's words).
4. Watch for the sneakiest bug the author names: a distance stored as a
   half-float between two passes, which drew rings on the oceans seen from
   orbit.

**Check**
- No popping, no loading screen, no rings on the oceans from orbit.
- Hardware note: "RTX 4070, optimisation is touchy and still ongoing"
  (author, answering what setup runs it).

**Why**
- At Earth scale, precision is the engine. Doubles on the CPU,
  camera-relative floats on the GPU, and doubles in the compute shader only
  where they are affordable is the whole trick; a single half-float in the
  wrong pass draws rings on every ocean.

## Phase 8: Light against a real photo, add the city, shoot one take (2026-11-15 update)

**Do**
1. Tune the orbital view against the Apollo 17 Blue Marble photo.
2. Place clouds by the climate; add moonlit nights.
3. Build the city as a first game layer on top of the terrain: its pads and
   earthworks are graded into the procedural relief; the buildings are assets.
4. Render the video as one continuous take, frame by frame, in the engine's
   cinematic mode: "Yes realtime in game footage" (author).

**Check**
- The orbital view matches the Blue Marble reference; the author invites the
  test directly: "Does it make you want to play? And where does it still
  give itself away as procedural?"
- The take is continuous with no cuts, no loading, no popping.

**Why**
- A real photo is a better target than taste. If the orbit view matches Blue
  Marble, the lighting model is right even before the ground detail is finished.
- A continuous take is the proof. A cut can hide a stream, a pop, or a
  precision failure; one take cannot.

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
4. **Simulate once, evaluate per point, every frame** (2026-11-15 update):
   "The rule is the same as in 2012: the geometry the view needs is rebuilt
   every frame, and everything global, from the plates to the weather, is
   computed once at startup. Nothing is streamed, so the camera can go
   anywhere in the system in a single frame."
5. **Precision is a budget**: doubles where they are affordable, float pairs
   while flying, never a half-float between passes.
6. **One real photo beats taste as a lighting target** (Blue Marble).
7. **The one-take video is the test, not the trailer.**

**Depth status:** FULL (startup budget, boundary type list, 1:1 scale number,
GPU eval design, and the emergent peak/trench benchmarks, all from the
author; updated 2026-11-15 with rivers, moons, precision handling, the city
layer, and the cinematic mode, all from the author's update post and
comments).
