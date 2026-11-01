---
name: godot-terrain3d-heightmap
description: "Use Terrain3D v1.1.0 for Godot 4 heightmap terrain: tessellated rendering with real shadows, decoupled coarser collision, runtime editing, no 3D tunnels by construction. Trigger when a Godot project needs runtime-editable heightmap terrain with documented render-vs-collision tradeoffs."
---

# Terrain3D v1.1.0: Heightmap Terrain for Godot 4

## Purpose

This skill applies TokisanGames' Terrain3D v1.1.0, an open-source
heightmap terrain plugin for Godot 4: **tessellated rendering with
light and shadow casting, collision on an entirely separate,
non-tessellated system, runtime-editable, but no true 3D tunnels by
construction.** Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle).

## Source

r/godot, TokisanGames, "Terrain3D v1.1.0 Released" (score 632, 30
comments, 2026-10-30):

- https://www.reddit.com/r/godot/comments/1xjrkgv/
- Native Reddit video: v.redd.it/5mj8t8ts6oyh1
- Demo videos on the author's X/Discord

Evidence note: the post has no selftext; all mechanics below are the
author's comment replies (exact wording quoted). 30 comments carry the
full technical substance. No third-party verification in this audit.

## Tools used

- Godot 4
- Terrain3D v1.1.0 (open-source heightmap terrain plugin)
- Tessellation shader producing geometry with light and shadow casting
- Collision on an entirely separate, non-tessellated system (lower
  detail than the renderer)
- Code-generated demo for procedural runtime maps

## Phase 1: Edit the heightmap

**Do**
1. Modify the heightmap's vertices or textures, including creating
   depressions or holes, at edit time or at runtime: "Terrain3D can be
   modified at runtime."
2. Do NOT design around 3D mesh tunnels: "A 3D mesh tunnel cannot be
   created out of a heightmap", a digging game punches a 2D hole into
   the heightmap, not a 3D cavity.

**Check**
- Depressions and holes render and collide; overhangs and tunnels are
  impossible by construction.

**Why**
Heightmap = 2.5D. The author is explicit about the ceiling so users
don't design around a feature that cannot exist.

## Phase 2: Render with tessellation, collide separately

**Do**
1. Rendering: "It is tessellation, which produces geometry, as you can
   see from the wire frame, and light and shadow casting."
2. Collision: "Collision runs on an entirely different system from the
   renderer. The collision shape is not tessellated at this time",
   lower detail than the first-seconds wireframe.

**Check**
- The visual mesh is dense and shadow-casting; the collision proxy is
  coarser. Test gameplay against the collision shape, not the
  wireframe.

**Why**
Decoupling lets the renderer go dense (tessellation) while physics
stays cheap. Tessellated collision is future work ("could be
considered in the future, but not at the same level of detail").

## Phase 3: Generate at runtime from code

**Do**
1. "Look at the code generated demo if you want to procedurally
   generate maps at runtime."
2. "This is a game engine terrain editor, designed for realtime use.
   Play with the demo." (Demo videos live on the author's X/Discord.)

**Check**
- Procedural maps generate in-game, not just in the editor.

**Why**
The plugin is a realtime terrain editor first, an asset second,
runtime generation is a designed-in path, demonstrated in code.

## AAA studio practice

How AAA studios ship the same techniques (cited to named studios and
shipped titles; the Terrain3D facts above remain the Reddit-sourced
base):

1. **DICE, Frostbite 2, Battlefield 3 (GDC 2011):** "consistent use of
   hierarchies allowed us to combine high resolutions with high view
   distances." Terrain was a workflow pillar: "full in-game realtime
   editing," the GPU "offloaded by caching intermediate results in a
   procedural virtual texture," and work prioritization that allowed
   "throttling without sacrificing quality," on a "flexible streaming
   system" that worked for both FPS and driving games.
   (https://www.ea.com/frostbite/amp/news/terrain-in-battlefield-3-a-modern-complete-and-scalable-system)
2. **DICE, Johan Andersson, SIGGRAPH 2007 course chapter "Terrain
   Rendering in Frostbite Using Procedural Shader Splatting"
   (Battlefield 2 / Battlefield: Bad Company):** the central design
   tension is that heightfields are static by construction; DICE "wanted
   to be able to destroy the terrain ever since Battlefield 1942, both
   geometrically and texture-wise, but haven't had the performance or
   memory to support arbitrary geometric destruction of the
   heightfields." Culling and LOD used "a frame-to-frame coherent
   quad-tree structure where every node knows the maximum and minimum
   height of the heightfield area within the node," and close-up
   heightfield limits were handled with extra detail geometry
   ("undergrowth") rather than denser base grids.
   (https://media.contentapi.ea.com/content/dam/eacom/frostbite/files/chapter5-andersson-terrain-rendering-in-frostbite.pdf)
3. **NVIDIA, GDC 2014 ("From Terrain to Godrays," Andrei Tatarinov and
   Iain Cantlay):** terrain is "the most obvious use for Tessellation,"
   subdividing geometry and then displacing "based on a values stored in
   a texture, giving true surface displacement before lighting." This was
   already shipping in AAA titles: Metro Last Light, Batman Arkham
   Origins, and Assassin's Creed IV: Black Flag.
   (https://developer.nvidia.com/content/terrain-godrays-better-use-dx11-tessellation)
4. **EA Frostbite, GDC 2023 ("From Battlegrounds to Fairways: Terrain
   Procedural Tools," Julien Keable):** "advanced non-destructive
   GPU-based layer compositing" with "data-driven behaviors that let
   game entities affect terrain"; the layers drive material selection,
   topology, object scattering, and terrain-object integration. Used by
   five EA titles including Battlefield 2042 and EA Sports PGA Tour.
   (https://www.ea.com/technology/news/frostbite-presents-at-gdc-2023)

## Agent automation

Convert the manual checks above into agent-executable gates, keeping
Do/Check/Why. Inference labels are in parentheses.

**Gate 1: render-vs-collision parity log**
**Do**
1. Write a script that samples the collision shape at a fixed grid of
   world positions and compares each sample against the heightmap
   height plus the tessellation displacement.
2. Log the maximum divergence per sample to `terrain-parity.log`, with
   the terrain seed and tessellation settings as header fields.
**Check**
- The log's maximum divergence is under the project's configured
   threshold (pick one value and record it in the log header before the
   run).
- Re-run after any collision or tessellation setting change; fail the
   run if divergence grows.
**Why**
Terrain3D keeps a coarse, separate collision system by design, so the
parity gap is the acceptance number, not something to eyeball.
(Inference: a scripted grid sample is a valid proxy for the
playtest-driven parity check the author recommends; the
wireframe-vs-coarser-collision claim is the sourced fact.)

**Gate 2: tessellation cost gate**
**Do**
1. With tessellation off, capture triangle count and framerate at three
   camera distances (near, mid, horizon); repeat with tessellation on;
   log both runs to `terrain-cost.log`.
2. Set the camera-distance tessellation policy using whatever values the
   plugin exposes, then re-run and log again.
**Check**
- The cost delta per distance band is recorded before tuning, so a
   later change can be diffed against it.
**Why**
DICE shipped throttling and prioritization "without sacrificing
quality" as the core runtime discipline; Terrain3D's tessellated
renderer needs the same measured baseline before it can be tuned.

**Gate 3: runtime-edit smoke test**
**Do**
1. From the code-generated demo path (Phase 3), script a procedural
   map, then programmatically punch a depression and a hole at runtime
   and drive a test body through both.
2. Attempt to author a 3D tunnel, then assert that every heightfield
   column still holds exactly one height value (no multi-value columns
   exist), and log that assertion.
**Check**
- `terrain-smoke.log` shows the depression rendered, the hole collided,
   and only 2D holes were possible.
**Why**
Runtime editability is the plugin's designed-in path; the 2.5D ceiling
should be enforced by an automated assertion, not by remembering it.

## The human method, distilled

1. **"Myself included, lol. That's why we made it, so we could have
   terrain"**, scratch-your-own-itch plugin; the author team needed
   terrain for their own game.
2. **Answer the hard question directly** (tunnels: no; collision:
   separate, coarser) instead of marketing around it.

**Depth status:** FULL (30 comments, author answers carry exact
mechanics; the post selftext is empty).
