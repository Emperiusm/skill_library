---
name: per-frame-planet-geometry-clipmap
description: "Render a 1:1 Earth-scale planet from orbit to ground in one frame: compute shader rebuilds nested geometry-clipmap rings from a libnoise complex-planet stack ported to HLSL, no tiles, no streaming, camera in doubles. Trigger when building seamless planetary-scale terrain."
---

# Per-Frame Planet Geometry Clipmaps

## Purpose

This skill rebuilds a planet's terrain geometry from scratch every frame,
so the camera can fly from orbit to a beach in a single frame with no
loading, no popping, and no tile streaming. The terrain is a function,
not data: a compute shader evaluates a noise stack for exactly the
vertices the current view needs. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: delete the streaming stage entirely —
geometry is rebuilt from a function each frame.

## Source

r/proceduralgeneration, Fresh-Daikon-9408 (full post text + 41-comment
technical thread, 2026-10-29/30):

- https://www.reddit.com/r/proceduralgeneration/comments/1xiw889/a_11_earthscale_procedural_planet_from_orbit_to_a/

Evidence note: all parameters below come from the author's own comments
in the thread. The engine is a closed side project ("Right now you
cannot try it"), so there is no source to inspect; the audit is a
reconstruction of the author's stated method. No frames inspected
(native Reddit video, no captions available).

## Tools used

Custom C++ 3D engine written from scratch (started as a 2012 Unity
prototype; "No I am not using Blender anymore, this is a c++ 3D engine
from scratch"). libnoise "complex planet" example, **ported to HLSL**.
Compute shaders for per-frame vertex evaluation. Multi-layered coherent
noise: Perlin, ridged fractal (fBm), others. Double-precision camera
positioning.

## Phase 1: Start from a displaced subdivided cube

**Do**
1. Build a sphere from a subdivided cube.
2. Displace it with a single Perlin noise layer.
3. Add fractal noise (fBm, ridged) for mountains.
4. Add camera-following LOD (the author suggests quadtrees or geometry
   clipmaps as the starting lookup).
5. Move the noise evaluation into a compute shader.

**Check**
- From orbit: does the planet read as a planet with relief?
- Fly downward: does the near field resolve without popping?

**Why**
The author's own stated starter order: "1. a sphere from a subdivided
cube, displaced by one Perlin noise; 2. fractal noise (fBm, ridged) to
get mountains; 3. a level of detail that follows the camera (look up
quadtrees or clipmaps); 4. then move the noise to a compute shader."
The two walls that killed the 2012 prototype were (a) rebuilding meshes
fast enough to show both the far horizon and the ground under the
camera, and (b) floating-point precision at planetary scale. Phase 3 and
4 exist to beat exactly those two walls.

## Phase 2: Stack the noise — the terrain is a function

**Do**
1. Take libnoise's "complex planet" example as the base noise stack.
2. Port it to HLSL: multi-layered coherent noise over the whole sphere —
   Perlin, ridged fractal noises, others — for mountain ranges, plains,
   and oceans.
3. Evaluate per vertex **in the planet's fixed frame**: "you stack some
   coherent noises (perlin noise, ridged fractal noises, others) then at
   each frame you pass vertex coordinates into this stack, and it gives
   you elevated coordinates."
4. Layer forests, vegetation, snow, and sand on top of the relief.

**Check**
- Sample the author's landmark set: buttes, mesas, a gorge cut into a
  plateau, close-up rock. If everything reads as one noise look, the
  stack needs more layer variety.

**Why**
"There is no pre-generated planet." "The terrain is a function: you
give it a point on the sphere, it returns an elevation, by stacking
noise layers." Nothing is stored; everything derives from the stack.

## Phase 3: Rebuild the view's geometry every frame — no tiles

**Do**
1. Each frame, the compute shader builds **one grid**: a cube face
   centred under the camera, projected onto the sphere.
2. Structure it as **nested rings that double in size outward** — like
   geometry clipmaps on a sphere: dense near the camera, coarse far
   away. "No quadtree, no chunks. It's a single grid centred under the
   camera, with nested rings that double in size outward."
3. Each ring's vertices are evaluated on the GPU through the noise
   stack.
4. Budget: **around 700 to 1,100 rings, under a million vertices.**

**Check**
- Move the camera fast (the author: the ship can go "from the Sun to
  the Earth in a second and the terrain keeps up"). If detail lags the
  camera, the per-frame rebuild is too slow.
- Zoom continuously: there must be no popping, because "there's no tile
  to split, merge or stream."

**Why**
"Speed costs nothing that way: there's nothing to stream, so nothing
can lag." The classic planetary-engine approach (progressive streaming
and refinement of meshes) is replaced by recomputation from the
function. Deleting the stage beats optimizing it.

## Phase 4: Hold precision, kill shimmer, add detail in the pixel shader

**Do**
1. Evaluate every vertex in the planet's **fixed frame**, with the
   **camera position in doubles** to stay precise at planetary scale.
2. **Filter out noise octaves finer than the local mesh cell**, so the
   far mesh doesn't shimmer.
3. Derive normals from neighbouring vertices.
4. Add fine detail (rock, sand) **in the pixel shader, not in the mesh**.

**Check**
- Orbit view: does the far horizon shimmer? If yes, an octave is
  escaping the cell-size filter.
- Ground level: do fine surface details hold up on the coarse mesh?

**Why**
Precision and anti-aliasing are handled mathematically, not with more
geometry. The author is explicit about the remaining gap: "the
large-scale relief is still a noise stack, with no tectonic plates
behind it, so the features don't nest the way real landscapes do."
The stated next step is a **drainage pass tracing rivers and watersheds
from the relief** — already following valleys — to drive coasts,
vegetation, and clearings top-down.

## AAA studio practice

Seamless orbit-to-ground procgen planets are a shipped AAA problem,
solved three different ways — and the geometry-clipmap technique
itself is a 2004 SIGGRAPH paper with GPU production numbers that
validate the skill's budgets. Four sources:

**Hello Games / No Man's Sky (GDC 2017, Innes McKendrick): continuous
world generation, nothing stored.** The pipeline order is explicit:
**voxel-based world generation → polygonization → texturing →
population → simulation**, run continuously in real time so players
transition seamlessly from space down to interactive, populated
terrain (no level/streaming seams). Nothing is stored per-planet:
worlds are generated on arrival from a compact rule set (~300 MB of
compressed world-building data, 64-bit addressing over 18.4
quintillion planets). The team-architecture payoff is the skill's own
lesson: a ~10-person team owned universe-scale content because
procedural population (trees, creatures, flora) derived from the
same seeds as the terrain rather than being separately authored.
(Source: https://www.gamedeveloper.com/programming/video-how-continuous-world-generation-works-in-i-no-man-s-sky-i- —
Game Developer on the GDC 2017 talk; corroboration:
https://Techraptor.net/gaming/news/hello-games-introduces-hello-labs-discusses-math-and-no-mans-sky)

**Cloud Imperium / Star Citizen planet tech v4 (CitizenCon 2949):
climate-driven terrain.** v4 replaced parameter-stack + texture-
overlay terrain with **climate-driven terrain: temperature and
humidity fields decide biomes and textures**, mimicking real Earth
processes — smooth, natural biome transitions instead of authored
layer boundaries. **Orbit-to-ground continuity is a hard
requirement:** no distance fade, no texture pop-in on approach; what
you see from orbit is exactly the terrain on the ground. Artists get
a **painting tool** where painting a feature in one area
auto-propagates it to every area on the planet with matching
conditions, which massively cut planet-authoring time. One planet
(Microtech) carries six distinct biomes.
(Source: https://twinfinite.net/news/star-citizen-microtech-planet-tech-v4/ —
Twinfinite, Nov 2019; caveat: alpha.)

**Frontier Developments / Elite: Dangerous "Stellar Forge":
formation-history simulation.** Stellar Forge **simulates planetary
formation from first principles**: bodies accrete from nebulous gas
over long simulated time with chemical composition and angular
momentum, generating ~400 billion star systems — a simulation of
formation history, not a heightmap-from-noise generator. Terrain
features **nest by cause**: the game runs tectonic simulations for
surface structure, and craters reflect impacts from the formation
simulation itself. This is the production answer to the skill
author's stated gap ("features don't nest the way real landscapes
do"): nest by simulated cause, then run the drainage pass.
Real data is fused in where it exists (Hipparcos and other stellar
catalogs; known stars searchable by catalog number); pure procgen
only fills gaps beyond 2013 observation limits.
(Sources: https://procedural-generation.isaackarth.com/2015/11/23/elite-dangerous-2014-planet-generation.html —
Isaac Karth's blog summarizing Frontier's newsletter; corroboration:
https://www.polygon.com/features/2019/5/6/18525941/elite-dangerous-distant-worlds-2-exploration-galactic-mapping-project/)

**Geometry clipmaps: the 2004 paper + GPU production path.** Losasso
& Hoppe's SIGGRAPH 2004 geometry clipmaps flew interactively (60 fps)
over a **40 GB US heightmap dataset compressed 100x by a compressed
image pyramid**; decompression, synthesis, and normal-map computation
are incremental, and inter-level seams are hidden by **morphing
geometry in a transition region per level** (in the vertex shader).
The GPU Gems 2 (2005) implementation moved nearly everything to GPU
via vertex textures: a 20-billion-sample grid stored in **355 MB at
~90 fps**, vertex/index buffers reduced to small constant "footprints"
instanced across levels, CPU only handling frustum culling of blocks
(2–3x load reduction) and incremental decompression. Budgets an agent
can cite: ring/level size n must be odd (n = 2^k − 1, e.g. 255);
deactivate levels whose extent < **2.5× viewer height**, rechecked
every few frames; expected draw-call load ~6L+5 per frame (71 calls
at L=11).
(Sources: http://hhoppe.com/proj/geomclipmap/ — original paper;
https://developer.nvidia.com/gpugems/GPUGems2/gpugems2_chapter02.html —
GPU Gems 2 chapter. Marked unverified: no shipped AAA title confirmed
from these sources as using Losasso/Hoppe clipmaps; the commonly
rumored FSX adoption is unconfirmed.)

## Agent automation

**Do**
1. **Nothing-stored gate** (NMS pattern, agent design): after a
   flight session, assert no per-planet cache exists on disk —
   the byte-level check that "the terrain is a function" stayed
   true. Any written planet data fails the run.
2. **Orbit-to-ground continuity sweep** (Star Citizen hard
   requirement, agent design): script a camera sweep from orbit to
   ground over fixed altitude bands, capturing renders at each
   band; diff consecutive bands for texture pop-in or distance
   fade. Pop-in anywhere fails the sweep.
3. **Viewer-height ring budget** (GPU Gems 2, agent design): derive
   the active ring count from camera height each frame using the
   2.5× rule (deactivate rings whose extent < 2.5× viewer height),
   and log the ring count per frame. Cross-check against the
   author's stated 700–1,100-ring budget: sustained over-budget
   frames are the signal to re-tune, not to add hardware.
4. **Cause-nested feature audit on the roadmap** (Stellar Forge,
   future gate, agent design): when the author's drainage pass
   lands, assert rivers trace from valleys in the relief — a
   scripted watershed-from-relief check that features nest by
   cause, the production fix for "noise without tectonics."

**Check**
- All four run headless and exit non-zero on failure; the
  continuity sweep's altitude bands and fixture camera path are
  committed with the project.
- The ring-budget log makes frame-cost spikes attributable to
  ring count, not to guesswork.

**Why**
NMS proves the nothing-stored architecture ships; Star Citizen
proves continuity is a hard requirement, not a nice-to-have;
Stellar Forge proves features must nest by cause; and the clipmap
paper itself hands over the production budgets (2.5× viewer
height, 6L+5 draw calls, vertex-shader seam morphing). These gates
convert the skill's design claims into the same scripted
acceptance a studio would demand.

## The human method, distilled

1. **Delete the pipeline stage that hurts.** Streaming, chunking, and
   LOD-splits were the 2012 walls; the author removed the concept
   entirely ("no quadtree, no chunks") instead of optimizing it.
2. Follow the author's starter order verbatim: subdivided cube + one
   Perlin, then fBm/ridged mountains, then camera-following LOD, then
   move noise to a compute shader.
3. Read a proven base (libnoise's complex planet) instead of designing
   a noise stack from scratch.
4. State the gap plainly: noise without tectonics means features don't
   nest like real landscapes — the drainage pass is the named fix, not
   more octaves.

## Failure modes

- **Far-horizon shimmer:** a noise octave finer than the local mesh
  cell escaped filtering. Fix: re-check the octave-vs-cell cutoff.
- **Popping during zoom:** would indicate tile logic crept back in;
  the design has no tiles, so investigate the ring-boundary math.
- **Precision swimming at ground level:** camera not in doubles, or a
  vertex evaluated in the camera frame instead of the planet's fixed
  frame.
- **Everything looks like one noise type:** the stack needs layer
  variety (the author's landmark check: buttes, mesas, gorge, rock
  close-up).

**Depth status:** FULL (author post text + detailed technical answers
in a 41-comment thread; numbers are the author's: ~700-1,100 rings,
<1M vertices, doubles precision. No invented parameters.)
