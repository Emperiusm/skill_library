---
name: clay-look-threejs-claybound
description: "Build the Claybound clay look in three.js: sculpted-mesh fire in a boil of clay beads, rounded-box blocks displaced with low-frequency noise, normal-map surface imperfection scaled by object size, and a separate deformable mesh for player-shaped clay, with weak-GPU fallbacks designed in (drop the glow core, halve the beads, one light per fire, animate only on-screen fires). Trigger when a three.js scene needs a handmade clay aesthetic with a performance budget."
---

# Clay Look in three.js (Claybound)

## Purpose

This skill reconstructs the clay look from the author's post, step by
step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The core method is: everything is
clay by construction (rounded boxes, noise displacement, normal-map
imperfection), and fire is a particle boil, not a shader.

## Source

Creator: dermosef. Reddit post:
https://www.reddit.com/r/threejs/comments/1xsolnm/update_on_the_25d_platformer_built_in_threejs/
(r/threejs post 1xsolnm, score 39, 7 comments; comments unretrievable
this run) | 2026-11-11 scout run, audit 6. Follow-up to the author's
September post
(https://www.reddit.com/r/threejs/comments/1wqbto8/claybound_a_platformer_built_in_threejs_where_the/).
Demo: https://playclaybound.com/. Steam: Claybound (app 5547840).

## Tools used

**three.js**; sculpted meshes; clay beads; normal maps; deformable mesh
(shapeable clay). No other engine or tool is named in the post; no
Blender or shader step is claimed.

## Phase 1: Make clay fire from sculpted meshes and beads

**Do**
1. Build flames from sculpted meshes in a boil of clay beads.
2. Beads rise, cool, and drop off as soot.
3. Use one light per fire, not per flame: "Takes away some of the
   vividness, but helps performance."
4. Animate only fires on screen.
5. On weak GPUs, drop the glow core and halve the beads.

**Check**
- The fire still reads as fire with one light and half the beads; the
  fallbacks are the weak-GPU test, not an afterthought.

**Why**
- Per-flame lights and always-on animation are the perf cost; the
  author's rules cap both where the player cannot see the difference.

## Phase 2: Build the clay look from rounded boxes

**Do**
1. Start every block as a rounded box with a corner radius.
2. Displace it with low-frequency noise for the wobbly silhouette.
3. Put surface imperfections in a normal map, scaled by object size.

**Check**
- The silhouette wobbles (low-frequency noise) while the surface reads
  as handmade clay (normal map); if either is missing, it reads as a
  plain box.

**Why**
- The look is three cheap decisions stacked: round the corners, wobble
  the silhouette, dirty the surface. No single step carries it.

## Phase 3: Make clay shapeable

**Do**
1. Add a separate deformable mesh driven by the player's drag, so the
   player can shape the clay directly.

**Check**
- Dragging deforms the mesh in play; the deformable mesh is separate
  from the static blocks, so shaping never breaks the level geometry.

**Why**
- Interactivity is a separate mesh because the static world and the
  shaped clay have different jobs; merging them would make one of them
  worse.

## The human method, distilled

1. **One light per fire, not per flame**; animate only what is on
   screen.
2. **The look is three decisions**: rounded box, noise wobble, normal-map
   imperfection scaled by size.
3. **Weak-GPU fallbacks are designed in** (drop the glow core, halve the
   beads), not patched on.

**Depth status:** PARTIAL (full post text; comments unretrievable this
run; no code, parameters, or render settings disclosed).
