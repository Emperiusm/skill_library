---
name: threejs-forest-env-perf
description: "Ship a dense three.js forest that runs: 500 instanced trees with compute-shader frustum culling, cross-billboards at distance, alphaTest leaves instead of transparency, Claude-placed godrays, grass trails, and 5-variant footstep audio. Trigger when a real-time 3D environment needs a measured 3-4x frame-cost cut."
---

# three.js Forest Environment: Measured 3-4x Perf Recipe

## Purpose

This skill builds a dense, lively three.js forest environment and cuts
its frame cost 3-4x with measured, transferable techniques: per-instance
frustum culling in compute shaders, cross-billboards at distance,
alphaTest instead of transparency, shared materials, and AI-assisted
godray placement. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle).
The core method is: instance everything, cull per-instance on the GPU,
billboard at distance, and use cheap tests (alphaTest) instead of
expensive blending.

## Source

r/threejs, PerceptionCharming (full post text with exact numbers,
2026-10-30):

- https://www.reddit.com/r/threejs/comments/1xiqih2/update_on_the_forest_environment_i_poste

Evidence note: numbers are the author's (500 trees, draw calls, fps);
the 11 comments are feature requests with no tooling detail. No shader
source disclosed. The video was recorded on an RTX 4080 at 4K with 2x
pixel density (effectively 8K), "locked at 60fps due to my screen
refresh rate" — the headline number is display-capped.

## Tools used

three.js. Compute shaders (frustum culling). Instanced meshes (trees,
godrays, grass). Cross-billboards. alphaTest materials. Shared
materials. Claude (top-down screenshot analysis for godray placement).
Procedural audio system (ambient + footstep variants).

## Phase 1: Make it lively — animate cheaply with instancing

**Do**
1. Build 500 trees from **6 models**, each with leaves + log meshes.
2. Add subtle leaf movement, a falling-leaf system, and spores in the
   air.
3. Add fake godrays ("fake light shafts instead of a physically
   accurate effect"); merge **all shafts into a single instanced
   mesh**; fade them when the camera gets near.
4. Place the shafts by asking Claude to "take images from top of the
   map and find gaps through trees," then place the shafts on those
   exact spots.

**Check**
- Do the shafts sit in real gaps (no shafts inside trunks)? The
  Claude-placement step is the check.
- Does foliage motion read as subtle, not windy-chaotic?

**Why**
Fake light shafts are cheap; placing them in real tree gaps sells the
effect. One instanced mesh keeps the draw calls flat. Using Claude
for placement — a planning task, not a generation task — is the
transferable trick: AI finds the gaps, the engine draws the shafts.

## Phase 2: Cut the frame cost — the measured recipe

**Do**
1. Add **frustum culling in compute shaders** so individual instances
   stop rendering when off-screen: "frustum culling to the trees in
   compute shaders which stop individual instances from rendering."
2. Add **cross-billboards for distant trees**: "after a certain
   distance, only 4 triangles are rendered per tree."
3. Switch leaf material from **transparent to alphaTest** — "made a
   huge difference."
4. Share materials across the environment to cut load time.
5. Draw-call budget: each tree type takes **2 draw calls total**
   (leaves + log across the whole environment) **plus one for the
   cross-billboard**.

**Check**
- Watch the cross-billboard switch distance ("You might see them
  switching in the video") — if the pop is visible, the switch
  distance is too close.
- Measure: the author's baseline was **8 fps on M1 Mac at max
  settings; after: 27-35 fps** depending on the area — a 3-4x
  improvement.

**Why**
Transparency sorting and per-pixel blending were the cost; alphaTest
is a single comparison. Per-instance culling and 4-triangle billboards
remove geometry the eye can't resolve anyway.

## Phase 3: Ground interaction and audio

**Do**
1. Grass bends and flattens where the player walks and slowly springs
   back, leaving a trail: "just added two spheres with camera and
   attached them to my grass system."
2. Audio: one ambient sound + footstep sounds for **mud and grass**,
   each with **5 variants selected randomly** so the same sound
   doesn't repeat.

**Check**
- Walk in a loop: does the trail fade naturally? Do footsteps avoid
  obvious repetition?

**Why**
Persistence (the trail) and variation (5 randomized variants) are the
two cheap tricks that make a loop feel alive.

## AAA studio practice

Dense forests at 60fps are a shipped AAA problem, and the production
answers validate every technique in this skill — instancing, GPU
culling, billboards, alphaTest — with studios naming the same
failure modes the skill already lists.

**Sucker Punch / Ghost of Tsushima (GDC 2021, Eric Woley): procedural
per-blade grass.** Traditional grass cards failed first: animation
tied to whole cards lacked fluidity and overdraw tanked performance
at density — so they moved to fully procedural per-blade generation.
The world is tiled with parameter textures (terrain height, material,
grass type/height); **compute shaders lay out blade positions per tile
with frustum + distance culling**; the vertex shader generates blades
from index/instance ID with **no vertex streams** (instanced indexed
draw calls), with high/low LODs and smooth transitions to kill
popping. **Unified wind:** a single 2D Perlin noise field sampled by
both CPU and GPU with minimal overhead; blade shape/animation from
cubic Bezier curves; clumping via a Voronoi algorithm modulating
height and orientation. Shadows were the expensive part: full shadow
pipelines were impractical, so they used **impostors to approximate
grass heights + screen-space shadows for fine detail**; grass height
is copied to CPU-accessible textures so gameplay physics can answer
stealth-visibility queries (stealth vs decorative grass types).
(Source: https://gist.ly/youtube-summarizer/procedural-grass-systems-in-ghost-of-tsushima-achieving-art-direction —
summary of Woley's GDC 2021 talk; cite as a summary, not the slides.)

**Guerrilla / Horizon Forbidden West (GDC 2022, James McLaren):
Deferred Texturing built for foliage.** Guerrilla built its Deferred
Texturing system primarily to accelerate foliage: the problem was
"lush jungle, lots of animated alpha-tested foliage, massive
overdraw," with animated geometry needing correct motion vectors for
TAA and motion blur. Zero Dawn's baseline is the gate this skill can
copy: **depth prepass + simple alpha-discard shader, then a
depth-equal second pass** so no pixel writes to the G-buffer more than
once. The sequel constraint forced the new system: art demanded
higher foliage density with the frame budget already full **and PS4
still a target**; the talk closes with measured performance numbers.
(Source: https://git.rayfalling.com/rayfalling/e-books/-/raw/5b55a6f4f168c88da799c8a937862cc0d9579255/%E6%B8%B8%E6%88%8F%E5%BC%95%E6%93%8E%E5%8F%8A%E5%9B%B2%E5%BD%A2%E5%AD%A6/GDC/2022/Adventures%20with%20Deferred%20Texturing%20in%20'Horizon%20Forbidden%20West'.pdf?inline=false —
McLaren's GDC 2022 slides, third-party mirror; cite with that
qualifier.)

**Ubisoft / Ghost Recon Wildlands (80 Level, 2017): cascade
vegetation + density-modulated LODs.** Two cooperating systems: a
grass system spawning patterns from terrain splatting, plus a Houdini
tool spreading bushes/trees via a "cascade" rule set (big trees spawn
medium trees spawn small trees/bushes), with density/scale/slope/
spacing, sun direction, species-per-material rules, and
inclusion/exclusion zones; roads, railways, water, and footpaths are
deleted automatically. **Density-modulated LODs:** instead of fixed
per-asset LOD distances, LOD switch points vary with local vegetation
density — in dense areas the same asset drops to its impostor LOD
sooner. **Dynamic in-engine impostors** are the final LOD, generated
inside the engine (no 3D-model/impostor mismatch), carrying multiple
channels for light direction, fake shadowing, and translucency. Asset
discipline: few species per rule, different "steps" of the same
species — natural look and memory-friendly.
(Source: https://80.lv/articles/vegetation-generation-in-ghost-recon-wildlands —
80 Level interview with technical artist Maximilien Cleda, 2017.)

**Simplygon / Microsoft (vendor, 2026): the prescribed hybrid LOD
chain.** Triangle reduction for near LODs, **billboard-cloud
impostors for the far LOD**, with trunk detection splitting trunk
(triangle-reduced) from leaves/branches (impostorized). Impostor
shading fixes: fade orthogonal planes, noise the normals, enable
**Preserve coverage** so mip levels don't vanish at distance —
directly relevant to the skill's cross-billboard distance swap.
Billboard clouds also optimize shadow rendering even at close range,
and tight-fitting impostors are generated from the alpha channel to
reduce overdraw from transparent pixels.
(Source: https://developer.microsoft.com/en-us/games/articles/2026/01/how-to-optimize-vegetation-with-simplygon/ —
Microsoft Developer blog, Jan 2026.)

## Agent automation

**Do**
1. **Card-first rejection gate** (GoT pattern, agent design): before
   writing billboard cards, assert the density target against the
   frame budget with a scripted overdraw estimate. If whole-card
   animation at target density exceeds the budget, the pipeline
   goes procedural per-blade — the GoT decision, scripted instead
   of discovered mid-production.
2. **No-double-write check** (Horizon Zero Dawn baseline, agent
   design): assert the render path uses depth prepass + alpha-discard
   with a depth-equal second pass, so foliage pixels write the
   G-buffer at most once. The skill's alphaTest choice becomes a
   render-state assertion, not just a material switch.
3. **Density-modulated LOD table** (Wildlands, agent design): measure
   local vegetation density per region and vary the cross-billboard
   switch distance with it — denser regions switch to impostors
   sooner. A scripted per-region density map drives the switch
   distances, replacing one global distance.
4. **Impostor/model match check** (Wildlands + Simplygon, agent
   design): at the switch distance, render the model and its
   impostor side by side and diff them; assert the switch is
   invisible (the skill's existing "visible pop" check becomes a
   frame-diff gate). Include the Preserve-coverage rule: assert
   mip levels survive at the farthest switch distance.

**Check**
- All four are scripts with pass/fail output; the LOD table and
  switch distances are committed data, not hand-tuned constants.
- The frame-diff baseline comes from the skill's own M1 Mac
  numbers (8 → 27–35 fps), not invented targets.

**Why**
GoT, Guerrilla, and Ubisoft all converged on the same stack —
instancing, GPU-side culling, billboard/impostor LODs, alphaTest
over transparency — and each names the failure the skill already
fears (overdraw, visible pops, model/impostor mismatch). These gates
turn the skill's measured recipe into the Wildlands-style cascade:
rules, density maps, and automated checks instead of one tuned
distance.

## The human method, distilled

1. **Measure the real bottleneck first.** 8 fps on M1 Mac at max
   settings was the baseline; the fix order was culling, billboards,
   then alphaTest.
2. **Use AI for placement, not for art.** Claude analyzed top-down
   screenshots to find tree gaps for godrays.
3. **Budget honesty.** The showcase numbers (RTX 4080, effective 8K,
   60fps) are display-capped; the meaningful numbers are the M1 Mac
   before/after.

## Failure modes

- **Visible billboard pop:** switch distance too close. Fix: push it
  out until the switch is unnoticeable.
- **AlphaTest edge harshness:** alphaTest trades smooth edges for
  speed. Fix: tune the alpha cutoff; the author accepted the trade.
- **Godrays inside geometry:** placement without gap analysis. Fix:
  the Claude top-down gap analysis step.
- **Footstep repetition:** fewer variants or no randomization. Fix: 5
  variants per surface, random selection.

**Depth status:** FULL (author's full post text with exact numbers:
500 trees, 6 models, 2 draw calls per type + 1 billboard, 4 triangles
per distant tree, 8 -> 27-35 fps on M1 Mac, 5 audio variants per
surface. No shader source disclosed.)
