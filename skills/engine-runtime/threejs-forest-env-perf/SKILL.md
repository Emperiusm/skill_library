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
