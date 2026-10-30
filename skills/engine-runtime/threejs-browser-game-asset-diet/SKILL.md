---
name: threejs-browser-game-asset-diet
description: "Ship a 3D browser game on an asset budget: measure the full model load (347 MB), cut the demo to ~45 MB with gltf-transform (Draco + WebP), load-gate by area, instance nature per chunk, generate trees from Blender Python recipes and seeds, build heroes in web workers, and step quality down automatically on low FPS. Trigger when a web game must run on unknown hardware."
---

# Browser Game Asset Diet: three.js Split-Screen Survival

## Purpose

This skill ships a 3D game in the browser on a measured asset budget, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The core method is: budget first, compress second, gate
loading third, degrade gracefully last.

## Source

Reddit, WardensOfTheWildDev (full post text + 47 comments, 2026-10-29):

- https://www.reddit.com/r/threejs/comments/1xhn0do/ - "I built a 4-player
  split-screen survival game in three.js, playable in the browser"
- Demo (45 MB, no install): https://wardensofthewild.se/play/

Evidence note: post text + comments only; no frames inspected, no code
reviewed. Performance claims are the author's (RTX 3060 dev machine);
commenter performance feedback is anecdotal. The author is a hobbyist
("not a game dev"), and his Claude Code agent did much of the building.

## Tools used

three.js; gltf-transform (Draco geometry compression, WebP textures);
Blender with Python scripts (trees from recipes + seeds); web workers
(hero building during load); Claude Code (game builder); ComfyUI
(reference art and model creation). Hardware context: author's GPU is an
RTX 3060.

## Phase 1: Measure the load, then set the budget

**Do**
1. Measure the full game's model load: 347 MB of models in this game.
2. Set the demo target: ~45 MB with no install.

**Check**
- Can you state both numbers from a measurement, not a guess?
- Does the demo open on a mid-range laptop without a loading stall?

**Why**
The budget is the headline, not a footnote. Everything downstream (what to
compress, what to gate, what to replace) is decided by the gap between the
two numbers.

## Phase 2: Compress with gltf-transform and gate what loads

**Do**
1. Run gltf-transform over the models: Draco geometry compression + WebP
   textures.
2. Load only what the first area needs; the rest streams or waits.
3. Replace the heaviest remaining models with lighter ones instead of
   compressing them harder.

**Check**
- Demo total stays near 45 MB.
- Visual loss concentrates in models the player will not inspect closely
  in the first area.

**Why**
Compression shrinks bytes; load gating shrinks the first impression. The
author did both, plus replacement: some models are cheaper to swap than to
squeeze.

## Phase 3: Instance nature per chunk; generate trees from recipes

**Do**
1. Instance all nature (trees, foliage) per chunk instead of placing unique
   meshes.
2. Generate trees from recipes and seeds via Python scripts in Blender, not
   as hand-modeled one-offs.

**Check**
- Draw calls scale with chunks, not with tree count.
- Re-running the recipe with a new seed yields a new but consistent tree.

**Why**
Recipes plus seeds make the forest regenerable, and chunk instancing keeps
it cheap. This is the LOD-from-recipe pattern: regenerate at lower fidelity
instead of decimating.

## Phase 4: Build heroes in web workers while the game loads

**Do**
1. Construct hero characters in web workers during the loading screen so
   the main thread never janks.
2. Have the heroes ready before the player can need them.

**Check**
- Loading stays smooth; the worker-built heroes arrive before first use.

**Why**
The web's main thread is the scarcest resource. Moving construction off it
is the cheapest performance win in this pipeline.

## Phase 5: Step quality down automatically on low frame rate

**Do**
1. Watch the frame rate at runtime.
2. If it stays low, drop the graphics level by itself - no settings screen
   the player has to find.

**Check**
- On a weak machine, the game finds its own playable level without user
  intervention.

**Why**
The web has no minimum spec. Automatic degradation is the portability
strategy; a settings screen is an admission of defeat.

## Phase 6: Split the screen for 1-4 players

**Do**
1. Render 1-4 viewports on one machine (split-screen couch co-op).
2. Keep the full game playable online with more players on different
   machines in the same world.

**Check**
- Decide the viewport strategy deliberately: a commenter asked "are you
  doing the four views with setScissor, and how's performance holding up?"
  (the author did not answer; verify setScissor vs multiple render targets
  in your own build).

**Why**
The game's origin is a constraint: "we only have one computer." Split-screen
is a design answer to hardware reality, and it is a differentiator the
comments argued about in both directions.

## AAA studio practice

- **Split the world into chunks and stream by area; the 5 MB bar is a
  distributor rule, not a preference.** Vortelli's Pizza Delivery
  (PlayCanvas, launched on Poki September 2023, 8+ million plays in its
  first year) split its open-world city into chunk islands connected by
  bridges, with trigger volumes loading the chunk ahead and unloading the
  one behind as the car crosses bridges; initial download landed at 58
  requests / 2.14 MB, below a hard 5 MB upper limit taken from a Poki talk,
  and Draco mesh compression cut download size by nearly 70%. Applied here
  (labeled: a shipped indie web game, not AAA): this is the direct
  production precedent for the skill's Phase 2 load-gating and Phase 3
  chunk instancing; validate the skill's area gates against the same test
  (initial download under budget, old area unloaded, not just compressed).
  Source: https://forum.playcanvas.com/t/vortelli-s-pizza-delivery-a-3d-open-world-driving-game/33735
- **Compress textures first, gate by area second, unload aggressively
  third.** The Ascendant Continuum WebGL optimization (Unity): texture
  compression (ETC2/DXT) cut texture memory from 200 MB to 35 MB,
  progressive loading staged UI textures (500 KB) then the current realm
  (5 MB) with other realms in the background, and Addressables unloaded old
  realm assets immediately on transition; initial load fell from 45 seconds
  to 8 seconds, and draw-call batching (materials 87 to 12, GPU instancing)
  took frame rate from 15 to 60 fps. Applied here (labeled: a production
  dev blog, not a AAA studio): the three.js recipe maps directly (KTX2/
  Basis for GPU-ready textures instead of shipping raw WebP, per-area
  manifests instead of realms, explicit dispose of the previous area
  instead of relying on GC). The automation upgrade below turns the
  per-area budget into a build-time check.
  Source: https://ascendant-continuum.web.app/blog/posts/unity-webgl-performance-from-15fps-to-60fps.html
- **Real-time shadows are a production risk on unknown hardware.**
  Vortelli's hardest launch bug: a small percentage of players saw the HUD
  over a blue void with no world loaded; the fix, suggested by another Poki
  developer, was disabling real-time shadows (planned to return as an
  optional setting). Applied here: the skill's Phase 5 automatic step-down
  should demote shadows first; on the web, shadows are a setting, not a
  feature.
  Source: https://forum.playcanvas.com/t/vortelli-s-pizza-delivery-a-3d-open-world-driving-game/33735

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Add a build-time area manifest generator: script that walks the scene
   graph, records compressed byte totals per load area (models + textures
   as served, after gltf-transform), and fails the build when any
   first-load area exceeds its budget; the Vortelli 2.14 MB discipline and
   the skill's 45 MB demo target made automatic.
2. Commit the gltf-transform recipe with the project: record the exact
   draco compression level and WebP quality per asset class in a checked-in
   config, so compression is reproducible across builds instead of
   re-invented per release.
3. Add a split-screen cost gate: measure FPS with 1, 2, 3, and 4 viewports
   and record where the automatic step-down triggers; the 4-way split is
   roughly 4x draw submission cost, so the gate must be defined against the
   worst case, not the solo case.

**Check**
- No area exceeds its byte budget at build time; compression settings are
  versioned; the step-down trigger is measured for the 4-viewport worst
  case.

**Why**
The web has no minimum spec, so the budget has to be enforced by the
build, not the author. The manifest makes the diet measurable, the recipe
makes it repeatable, and the split-screen gate makes the degrade path
honest about the hardest case the game actually ships.

## The human method, distilled

1. Budget first, features second: the 347 -> 45 MB number leads the post.
2. Constraints as design: one computer -> split-screen; browser -> asset
   diet; unknown GPUs -> adaptive quality.
3. Agent builds, family playtests: Claude Code built the game, the author's
   daughters (9 and 11) found the flaws, and he committed in the thread to
   act on the feedback (reorder tutorials, Escape closes menus, boss in the
   demo). Agent velocity does not replace the feedback loop; it shortens it.

**Depth status:** FULL (post text + 47 comments; no code or frames inspected).
