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

## AAA studio practice

- **First-principles formation simulation is the shipped AAA galaxy
  generator (Frontier Developments, Elite: Dangerous, Stellar
  Forge).** Lead render programmer Doc Ross: generation is a
  top-down hierarchy, where "the smallest details on planets are
  informed by the results of planet-scale information generation,
  which are informed by star-system scale information, which are
  informed by galactic information," starting from "galaxy-scale
  material and age distribution functions." The one non-programmatic
  input is a top-down view of the distribution: "it ensures the
  spiral arms and galactic bulge form the correct shape." Each
  simulated planet "knows its rough classification based on how much
  mass it has, the types of materials it is made from, its volcanic
  parameters, a temperature differential of the crust, mantle and
  core, trapped gases/atmosphere, and heating from tidal effects and
  direct radiation from the parent stars"
  ([80 Level, 2018](https://80.lv/articles/generating-the-universe-in-elite-dangerous?amp=1)).
  The author's density maps are Stellar Forge's top-down distribution
  view at indie scale: the shape authored once as an image, the seed
  doing the rest. And the chemistry derivation in Phase 2 is Stellar
  Forge's formation simulation in miniature: Frontier "rolls time
  backwards toward the Big Bang, and extrapolates from there the
  composition of hundreds of thousands of celestial bodies using the
  first principles that astrophysicists believe govern our universe,"
  and validates the generator by checking it accounts for known
  exoplanets and their orbits — the same calibration idea as the
  author's "Earth comes out within about a point"
  ([Polygon, 2014](https://www.polygon.com/2014/12/4/7333709/elite-dangerous-milky-way-stellar-forge-human-cruelty)).
- **Scale needs 64-bit coordinates or a floating origin (Cloud
  Imperium Games, Star Citizen).** Digital Foundry: CIG converted the
  engine to use 64-bit coordinates "to enable solar system-sized
  game spaces — 536,870,912 times larger than a space based on 32-bit
  float coordinates," with object containers streaming in and out in
  the background "in an efficient multithreaded manner" so the player
  can travel at great speeds while keeping detail at both macro and
  micro level
  ([Digital Foundry, 2020](https://www.digitalfoundry.net/articles/digitalfoundry-2020-star-citizen-tech-focus-alpha-3-point-8)).
  The author's universe-moves-around-the-camera is the other
  standard answer to the same problem: keep coordinates near the
  origin where floats are precise. The two approaches are the
  tradeoff to record: 64-bit everywhere costs performance on some
  hardware; floating origin costs a rebase discipline.
- **Nothing stored is the Hello Games rule (No Man's Sky, GDC
  2017).** One seed number to a deterministic engine defines the
  whole universe; "there are no load times, because nothing needs to
  load, as the planets are entirely computer-generated"
  ([PlayStation.Blog, 2014](https://blog.playstation.com/archive/2014/08/26/exploring-18446744073709551616-planets-mans-sky/);
  [Polygon, GDC 2017](https://www.polygon.com/2017/3/2/14790028/no-mans-sky-was-flat-procedural-world-generation-maths)).
  Hello Games could not QA 18 quintillion planets by hand, so it
  built virtual space probes that flew around the universe, made gifs
  of the planets, and reported back
  ([Fast Company](https://www.fastcompany.com/3048667/how-4-designers-built-a-game-with-184-quintillion-unique-planets/)).
  The author's census — walking the whole galaxy star by star with
  the client code — is the probe idea applied to generation itself:
  the census is both the proof and the regression test (see
  Phase 6).

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

## Phase 6: Lock the galaxy down with regression tests

Phases 1 to 5 describe a generator whose value is that it is
bit-exact and self-checking: same seed, same galaxy, zero
contradictions, ~400 fps. Every one of those claims is a number, and
numbers that are never re-measured drift. The five checks below turn
the author's own claims into files an agent can run on every
generator change, following the Hello Games space-probe idea from
the AAA section above: the census is the QA.

**Do**
1. Write `galaxy-manifest.json` per generator version: the seed, the
   full census (467,561,373 stars; ~4.9 billion planets; 8.2 billion
   moons; ~185 million liquid-water-ocean planets; 1,852,531 with
   life; 281,081 neutron stars; 186,578 black holes), the
   contradiction count (zero), and the render budget (fps and draw
   calls per camera). Any generator change that moves a census number
   is a visible diff, not a silent drift.
2. Run the cross-platform determinism test: run the same seed on Mono
   (editor), IL2CPP, and .NET; hash every star temperature, or a
   sampled 25,000-star slice (the author's own failure scale: roughly
   7 in 25,000 stars differed before the fix). Gate: zero differing
   stars across runtimes.
3. Run the PNG-decoder regression: decode a reference density map
   with the custom decoder and with Unity import; assert the custom
   decoder is bit-identical to the source PNG and record the
   Unity-import delta (the author measured 36% of pixels changed).
   If the delta ever drops to zero, the custom decoder can be
   retired; until then it stays.
4. Run the origin-drift check: log the maximum coordinate magnitude
   the camera ever reaches during a flight test; assert it stays
   within the float-precision budget the floating-origin design
   assumes (the universe moves, the camera stays near the origin,
   Phase 5).
5. Log the render budget on every render change against the author's
   baseline: 19 fps for GameObject-per-star, ~400 fps for the single
   buffer with one draw call per camera. A change that costs fps
   without adding visible quality fails the gate.

**Check**
- `galaxy-manifest.json` exists per generator version with seed,
  census, contradiction count, fps, and draw calls.
- Zero differing stars across Mono, IL2CPP, and .NET on the same
  seed.
- The custom PNG decoder is bit-identical to the source; the
  Unity-import delta is recorded.
- The camera never drifts beyond the float-precision budget.
- Fps and draw calls per camera are logged against the 19-to-400
  baseline.

**Why**
- The census is the only feasible QA for a galaxy no one can look
  at in full. Hello Games sent probes; this generator walks the
  galaxy with its own client code. Either way, the numbers are the
  QA, and a number that is not written down cannot regress.
- "Same bits, not same algorithm" (Phase 4) is a promise about every
  layer that can silently change a value. The determinism test and
  the PNG regression are the two layers the author already caught;
  the tests exist so the next silent layer gets caught the same way.

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
