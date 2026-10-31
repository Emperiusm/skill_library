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

## The human method, distilled

1. **"Myself included, lol. That's why we made it, so we could have
   terrain"**, scratch-your-own-itch plugin; the author team needed
   terrain for their own game.
2. **Answer the hard question directly** (tunnels: no; collision:
   separate, coarser) instead of marketing around it.

**Depth status:** FULL (30 comments, author answers carry exact
mechanics; the post selftext is empty).
