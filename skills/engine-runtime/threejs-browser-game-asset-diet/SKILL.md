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

## The human method, distilled

1. Budget first, features second: the 347 -> 45 MB number leads the post.
2. Constraints as design: one computer -> split-screen; browser -> asset
   diet; unknown GPUs -> adaptive quality.
3. Agent builds, family playtests: Claude Code built the game, the author's
   daughters (9 and 11) found the flaws, and he committed in the thread to
   act on the feedback (reorder tutorials, Escape closes menus, boss in the
   demo). Agent velocity does not replace the feedback loop; it shortens it.

**Depth status:** FULL (post text + 47 comments; no code or frames inspected).
