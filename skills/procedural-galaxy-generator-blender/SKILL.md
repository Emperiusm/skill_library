---
name: "procedural_galaxy_generator_blender"
description: "Build procedural galaxies in Blender with geometry nodes plus shaders: point clouds for stars, volumes for everything else, energy-preserving far-field glow, keyframed emissive flythroughs, 3D gravitational lensing meshes, dust lanes as layered volume roles (absorption/emission/particles), and instanced deep-field domains with cosmological redshift. Trigger when building deep-space VFX or procedural astronomy."
---

# Procedural Galaxy Generator in Blender (AstroDemiurge Method)

## Purpose

This audit reconstructs the method from Petrundiy2's (AstroDemiurge) r/vfx
showreel post and his technique answers across 17 comments, step by step, so
another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: point clouds for stars, volumes for
everything else, and treat the far-field glow as a separate problem from the
resolved stars. (Labelled: the exact node graph is never shown in the
source; phases below are the author's stated architecture plus the physics
constraints he names, not a copy of his ~1500-node graphs.)

## Source

Creator: Petrundiy2 (AstroDemiurge)

Source: https://www.reddit.com/r/vfx/comments/1wzzgux/ive_been_creating_a_lot_of_procedural_deep_space/
(showreel; r/vfx post 1wzzgux, score 137, 17 comments; creator answered
technique questions in the comments) | 2026-10-09 scout run. Author's
summary, verbatim: "I was working on a procedural galaxy generator for
Blender for a long time, and each galaxy preset consists of geometry nodes
and shader parts. The hardest ones contain ~1500-1600 nodes overall."
Tutorials: https://youtube.com/@astrodemiurgevfx (posted by the author in the
comments; content of the tutorials is not scraped here).

## Tools used

Tools used: **Blender** (geometry nodes + shader nodes).

## Phase 1: Structure the preset as geometry nodes + shader parts

**Do**
1. Build each galaxy preset as two coupled halves: **geometry nodes** for
   structure (spiral arms, bars, ellipticals) and **shader nodes** for the
   light behavior.
2. Expect scale: the author's hardest presets run **~1500-1600 nodes
   overall**. Plan presets in modules (arm distribution, dust lanes, halo,
   core) rather than one flat graph.

**Check**
- Each preset is a named, reusable unit; swapping a barred spiral for an
  elliptical means swapping the preset, not rewiring the scene.

**Why**
- The author calls out what he is proudest of: "I'm most proud of the setup
  for barred spiral galaxies, as well as the deep-field gravitational
  lensing (check out the ellipticals in the last flyby!)" — presets are the
  unit of reuse that makes a showreel's worth of galaxies possible.

## Phase 2: Stars as point clouds, everything else as volumes

**Do**
1. Render **stars as point clouds**; render **everything else (gas, dust,
   nebulous glow) as volumes**.
2. For per-star size and luminosity variation, bias toward more randomness
   and a more organic distribution (Redd411's critique: "point star
   sizes/luminosity could use a bit more randomness and distribution bit
   more organic").

**Check**
- The star field reads as discrete points at close range; the gas and glow
  read as continuous volume, not as a star texture.

**Why**
- Petrundiy2's architecture answer: "Point clouds for stars and volumes for
  pretty much everything else". Points are the cheapest carrier for discrete
  stars; volumes carry the continuous medium.

## Phase 3: Far-field glow as a volumetric material with an energy-preserving crossfade

**Do**
1. For the galaxy seen from far away, do NOT try to instantiate the real
   star count. Drive the overall glow with a **volumetric material**.
2. As the camera approaches, **fade the background glow out while resolved
   stars fade in**, such that the **overall glow energy is preserved**.
3. (Partially implemented in the author's setup per his own note: "and this
   is partially implemented in my setup. The next task is to fade the
   background and do so in a way that it eventually transforms into
   stars.")

**Check**
- At intermediate distances, brightness neither pops nor dips: the total
  light energy stays constant through the transition.

**Why**
- Petrundiy2's physics constraint, verbatim: "The point is that the overall
  glow of a galaxy from a distance is determined by billions of stars. A
  computer is physically incapable of creating and storing such a large
  number, so the overall glow is determined by a volumetric material.
  However, as one approaches, resolved stars should appear, while the
  background fades, and ideally, the overall glow energy should be
  preserved. This is a delicate matter."

## Phase 4: Keyframe emissive brightness for flythrough realism

**Do**
1. When the camera flies into or through a galaxy, **keyframe the
   brightness of the emissive regions** over the shot.
2. Accept that getting the scaling right is the hard part; iterate on the
   keyframes against reference footage.

**Check**
- The flythrough reads as traveling through a luminous medium; brightness
  ramps feel physical rather than like a slider move.

**Why**
- drunk_kronk asked whether brightness could be procedurally controlled;
  Petrundiy2: "You definitely can fly into or through them, but I think
  you'll have to keyframe the brightness of emissive regions a bit to make
  it more realistic. The scaling of these effects are a hard part, but
  since it's procedural, you have literally infinite detail on any scale."

## Phase 5: Gravitational lensing as 3D refractive meshes

**Do**
1. Build lensing as a **real 3D effect**: spawn "a bunch of tricky
   refractive meshes" on the elliptical galaxies.
2. Scale the **strength of the effect with the size of the galaxy**.

**Check**
- Lensing distortion tracks the massive ellipticals; check the ellipticals
  in the last flyby, which the author flags as the showcase.

**Why**
- Tumbleweed_on_Fire asked "Did you do gravity lensing as 2D trick or real
  3D rays distortions rendering?" — Petrundiy2: "The gravity lensing is a 3D
  effect. I spawned a bunch of tricky refractive meshes on elliptical
  galaxies, and the strength of the effect depends on the size of the
  galaxy." Geometry-driven refraction keeps the lensing consistent as the
  camera moves, where a 2D trick would break on parallax.

## Phase 6: Deep field from instanced galaxies in filament-like domains

**Do**
1. Build the deep field by **instancing the procedural galaxy presets**
   instead of building one giant scene.
2. Scatter the instances **inside filament-like density structures** (the
   cosmic-web layout), and apply **cosmological redshift** to the distant
   instances.

**Check**
- The field reads as large-scale structure (filaments and voids), not as
  uniform random scatter; distant galaxies shift red.

**Why**
- Author: "As for the Deep Field, I instanced these procedural galaxies in
  a domain (scattering points inside filament-like density structures) and
  added the gravitational lensing effects. It also has the cosmological
  redshift effect as well." Instancing reuses the preset investment; the
  filament layout is what sells "deep field" rather than "star wallpaper".

## Phase 7: Learn from the tutorials before cloning the architecture

**Do**
1. Watch the author's tutorials at
   https://youtube.com/@astrodemiurgevfx ("Yes, I did everything you
   mentioned, and I even have a couple of tutorials on my YT channel about
   it") before attempting your own generator.
2. Treat the tutorials as the node-level source this audit cannot provide.

**Check**
- You can reproduce at least the barred-spiral preset structure from the
  tutorial before designing your own.

**Why**
- The community signal is unusually strong for a technical showreel:
  o--Cpt_Nemo--o: "I have never really ever seen accurate astro CG anywhere
  besides yours. Even in films, usually its nowhere near accurate." The
  tutorials are the author's offered path in.

## Phase 8: Dust lanes as layered volume roles (foreground / mid / background split)

**Do**
1. Give the **dust lanes their own volume role**: render dust via **volume
   absorption** (the dark lanes that cut across the warm core are absorptive
   structure, not missing geometry).
2. Render the **background stars as volume emission** — the far, unresolved
   population is emissive medium, not points.
3. Render the **foreground stars as emissive particles** — the near,
   resolved population stays discrete and emissive.
4. Check the read against elbloco80's reaction to this exact technique:
   "Beautiful filaments! Especially the dark lanes cutting across the warm
   core. Feels like a true galaxy."

**Check**
- The dark lanes read as occlusion inside the warm core (absorption doing
   the work), while background stars glow through the medium and foreground
   stars sit on top as sharp emissive points; three depth layers are
   visually separable.

**Why**
- Petrundiy2's stated construction, verbatim: "The dust is made via volume
   absorption, and the background stars are volume emission. The foreground
   stars are emissive particles." This extends Phase 2's
   "points-for-stars, volumes-for-the-medium" split into a **depth-layered
   volume recipe**: absorption for the occluding dust, emission for the
   background population, particles for the foreground.

## The human method, distilled

1. **Points for stars, volumes for the medium.** Discrete vs continuous
   gets different renderers.
2. **Billions of stars become a volumetric material.** The far-field glow
   is a shading problem, not an instancing problem.
3. **Preserve energy through the crossfade.** Resolved stars must hand off
   from the glow without a brightness pop.
4. **Keyframe what physics won't give you.** Emissive brightness on a
   flythrough is authored, not simulated.
5. **Lensing is geometry, scaled by mass.** Real refractive meshes on the
   ellipticals; strength follows galaxy size.
6. **Deep fields are instanced presets in filament domains.** Reuse the
   galaxy investment; layout sells the cosmology.
7. **Dust is an absorber, not an absence.** Dust lanes via volume absorption,
   background stars as volume emission, foreground stars as emissive
   particles — three volume roles, three depth layers. (Added 2026-10-13
   from the author's r/proceduralgeneration post
   https://www.reddit.com/r/proceduralgeneration/comments/1x3lmgz/peering_behind_the_dust_clouds_of_a_procedural/)

## Failure modes

- **Flat far-field glow.** Without the volumetric material and the
  energy-preserving crossfade, the galaxy either pops or dips as the camera
  approaches — "a delicate matter" by the author's own admission, still
  partially implemented.
- **Mechanical star fields.** Insufficient randomness in point star
  sizes/luminosity reads as artificial (Redd411's critique, from a former
  astronomy visualizer).
- **2D lensing tricks on camera moves.** A screen-space lensing cheat breaks
  on parallax; the author chose refractive meshes precisely for this.
- **Wrong scale on emissive brightness.** The author names scaling as "a
  hard part" — flythrough brightness keyframes are the iteration sink.
  (Labelled: FTL flyby optics — blue shift, star-streak rendering — were
  asked about and explicitly not addressed: "we can't move that fast
  anyways, so I didn't think about any additional effects.")

**Depth status:** FULL for the stated architecture (post text + 17 comments
with the node counts, the point-cloud/volume split, the energy-preservation
constraint, the lensing construction, and the deep-field method, all in the
author's own words); INFERENCE for any node-level detail — the exact
geometry-node and shader graphs are not shown in the source. A media
download plus the YouTube tutorials would add the actual node wiring and
parameter values.
