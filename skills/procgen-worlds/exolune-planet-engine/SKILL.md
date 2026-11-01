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
