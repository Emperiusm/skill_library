---
name: procedural-galaxy-density-maps-unity
description: "Generate a visitable galaxy in Unity from one seed: grayscale density maps place 467M stars and billions of planets, camera-facing dust sprites, chemistry-derived planets with a zero-contradiction census, terrain as a pure function of 3D position, bit-exact cross-platform determinism, and one draw call per camera at ~400 fps. Trigger when building space-scale procedural worlds where every star must be visitable and identical on every platform. Distinct from the Blender GeoNodes variant procedural-galaxy-generator-blender."
---

# Procedural Galaxy from Density Maps in Unity

## Purpose

This skill reconstructs the exact workflow in Backbone_Labs' galaxy
generation post (r/proceduralgeneration, 2026-11-16), step by step, so
another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: one seed, density
maps for placement, bit-exact math for determinism, and one draw call
for all stars.

Related variant: `procedural-galaxy-generator-blender` (Blender
GeoNodes + shaders: point clouds for stars, volumes for the medium,
energy-preserving far-field glow). That skill is the visual/VFX route;
this skill is the runtime-game route: a galaxy the player can fly
through, where every star is visitable and identical on every
platform. Do not mix the two: this one uses density maps and
camera-facing sprites, not geometry nodes and volumes.

## Source

Creator: Backbone_Labs.

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xwugk4/467m_stars_billions_of_planets_all_from_one_seed/
(r/proceduralgeneration post 1xwugk4, score 101, 29 comments
including detailed author replies) | 2026-11-16 scout run. Space game
(exploration, resources, combat), Unity client + browser/mobile
planned, video captured straight from Unity, still in development.
Evidence: complete author post text, ~3,900 chars, with exact census
numbers + 29 comments; video is captured Unity footage; a media
download would add frames, not pipeline detail.

## Tools used

Tools used: **Unity** (Mono editor / IL2CPP / .NET runtimes);
grayscale density maps (own PNG decoder); reimplemented Unity RNG;
improved Perlin + ridged multifractal (Musgrave-style) terrain; single
GPU buffer + one draw call per camera; background-thread generation
and sorting.

## Phase 1: Place the galaxy with density maps

**Do**
1. Start from one seed. From it: 467,561,373 stars, about 4.9 billion
   planets, 8.2 billion moons, with orbits, atmospheres, chemistry,
   geology, and terrain. Nothing is stored on disk.
2. Use density maps: grayscale images of the galaxy seen from top,
   with the spiral arms already in them. One map decides where the
   stars go; three more maps decide where the dust goes. "The seed put
   each thing in his exact place." (Author, in comments.)
3. Render dust as many semi-transparent sprites in three sizes (big,
   medium, small), always facing the camera. The brighter the pixel in
   the map, the bigger and more opaque the sprite. Dark zones are just
   gaps in the maps: no dust, so you see black and loose stars.
4. When on a planet, the sky is the same galaxy seen from that place,
   not a generic skybox.

**Check**
- Census numbers, verified by walking the whole galaxy star by star
  with the same code the client uses (no extrapolating from a sample):
  467,561,373 stars; ~1 star in 100 has no planets at all; ~185
  million planets have liquid-water oceans; 1,852,531 have life;
  281,081 neutron stars; 186,578 black holes.
- "You can fly to any star, go into its system and visit any planet
  or moon, it gets generated when you arrive and anyone who goes
  there sees exactly the same thing, bit for bit."

**Why**
Maps are cheaper than math for galaxy shape: the spiral structure is
authored once into an image, and the seed does the rest. Dust as
camera-facing sprites is the same trick as the galaxy row already in
the watchlist (Blender GeoNodes galaxies), done in Unity with maps
instead of nodes.

## Phase 2: Make planets from chemistry, not random rolls

**Do**
1. Derive each planet's chemistry from the rock/metal/ice mix it
   formed from, calibrated so Earth comes out within about a point of
   its measured composition.
2. Work out the final state for every candidate surface and throw away
   the ones that contradict themselves (e.g. frozen oceans at 200 C).
3. Version 1 had "something like 16% nonsense planets"; now: "Zero
   contradictions in the census, which honestly took way longer than
   I'd like to admit."
4. Rate every world 0-10 for minerals, rare earths, energy, water,
   food, and jump fuel, plus hostility, all from its actual data. The
   world map splits the surface into 32 cells; each cell gives
   resources based on the real terrain under it (coast gives water,
   volcanic slope gives geothermal, icy moon over an ocean gives water
   and not much else).

**Check**
- The census is the check: zero self-contradicting surfaces across
  ~4.9 billion planets.
- Author's design rule, stated in comments: "when realism and fun are
  in conflict, I choose fun" — and "the most valuable stuff use to be
  on the most hostile worlds."

**Why**
Derived chemistry plus a contradiction filter is an acceptance test
built into the generator: nonsense is rejected at generation time, not
found by players.

## Phase 3: Terrain as a pure function of 3D position

**Do**
1. Terrain height at any point is a function of its 3D position:
   improved Perlin plus a ridged multifractal (Musgrave style), with
   every octave rotated so the mountains do not line up with the noise
   axes.
2. Small moons are not spheres: nine shape families based on real
   bodies like Phobos or Arrokoth.
3. Because terrain is a function, zoom is nearly free: the whole globe
   and a bit of coastline are the same function sampled at different
   resolution.

**Check**
- (Inference, labeled:) no numeric parameters (octave counts,
  frequencies, amplitudes) are given in the post or comments.

**Why**
A pure function needs no storage and no LOD stitching: resolution is
a sampling choice, not a data problem.

## Phase 4: Bit-exact determinism across platforms

**Do**
1. Fix the float problem: Mono in the editor does float math at double
   precision and rounds "whenever it feels like it"; IL2CPP and .NET
   round after every operation. Result: roughly 7 in 25,000 stars had
   a different temperature depending on where it ran.
2. Apply the ugly fix: an explicit `(float)` cast after every single
   operation in the generator; no `Math.Pow` or any library function
   whose last bit depends on the platform.
3. Reimplement Unity's RNG and check it draw by draw against the real
   one.
4. Read the density maps with your own PNG decoder, because Unity was
   compressing them on import and changing 36% of the pixels.
5. Run the same generator locally on every platform (Unity client,
   browser, maybe mobile); the server only keeps what players change.

**Check**
- Same seed, same galaxy, on any PC, "down to the bit." The census
  numbers are the proof: they were produced by the client code itself.
- Commenter question answered: "leave and come back and its exactly
  the same... every one of them runs the same generator locally, so
  nothing about the galaxy gets downloaded."

**Why**
"Same algorithm" is not enough; it has to be the same bits. Every
layer that can silently change a value (runtime float promotion,
library functions, texture import compression) gets replaced or
pinned.

## Phase 5: Render it — one buffer, one draw call, universe moves around the camera

**Do**
1. Drop the GameObject-per-star version (about 19 fps).
2. Put all loaded stars in a single GPU buffer drawn with one draw call
   per camera; a background thread sorts them back to front; new
   sectors generate in the background while flying.
3. Do not move the camera: the universe moves around it, so everything
   stays close to the origin where floats keep their precision.
4. Result: "From 19 to around 400 fps."

**Check**
- 19 fps before, ~400 fps after, same scene class. The origin trick is
  what makes the float budget work at galaxy scale.

**Why**
One draw call plus background generation is the only shape that fits
hundreds of millions of stars; and at that scale, float precision is a
rendering problem solved by never letting coordinates get large.

## The human method, distilled

1. Author the shape once (density maps), let the seed do the rest.
2. Derive, don't roll: chemistry from formation mix, resources from
   real terrain, calibrated so Earth comes out right.
3. Reject nonsense at generation time: work out the final state, throw
   away self-contradictions.
4. Same bits, not same algorithm: cast after every op, reimplement the
   RNG, decode your own PNGs.
5. The universe moves around the camera: keep coordinates near the
   origin where floats are precise.
6. "When realism and fun are in conflict, I choose fun."

## Failure modes

- **Float promotion across runtimes.** Mono (editor) promotes float
  math to double and rounds when it feels like it; IL2CPP/.NET round
  after every operation. ~7 in 25,000 stars differed before the fix.
  The fix is an explicit `(float)` cast after every operation, with
  no `Math.Pow` or platform-dependent library functions anywhere in
  the generator.
- **Texture import silently changing the maps.** Unity compressed the
  density maps on import and changed 36% of the pixels. Read them
  with your own PNG decoder instead.
- **RNG drift across platforms.** Unity's RNG is not guaranteed
  bit-identical everywhere; the author reimplemented it and checked it
  draw by draw against the real one.
- **GameObject-per-star.** About 19 fps. The single GPU buffer, one
  draw call per camera, and background-thread sort are what get it to
  ~400 fps.
- **Coordinates drifting from the origin.** At galaxy scale, float
  precision dies with distance. Move the universe around the camera,
  never the camera through the universe.
- **Numeric terrain parameters are unverified.** No octave counts,
  frequencies, or amplitudes are given in the post or comments; do
  not quote numbers for Phase 3 that the source does not support.

**Depth status:** FULL (complete author post text, ~3,900 chars, with
exact census numbers + 29 comments including detailed author replies;
video is captured Unity footage; a media download would add frames,
not pipeline detail).
