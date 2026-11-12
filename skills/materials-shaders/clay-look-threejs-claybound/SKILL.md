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

## AAA studio practice

Handmade-material looks are a deliberate AAA choice, not a budget
fallback: the studios that ship them build the look into the
construction method, and they budget detail against the imagined
scale of the world.

- **Media Molecule, Dreams (PS4, 2020).** The whole game is a
  sculpted, clay-like look, and it started as a sculpting tool: the
  engine began as a constructive-solid-geometry sculptor (technical
  director Alex Evans calls the tight end of it the "Brick Engine"),
  and when that could not reach the painterly look art director
  Kareem Ettouney wanted, the team replaced it with a splats-based
  engine (the "BubbleBath" engine) that lets anyone reach the smoky,
  impressionistic style. The studio's stated inspiration is
  traditional media, sculpting and painting, worked without the
  technical steps getting in the way.
  (https://sickgaming.net/thread-90913.html ;
  https://www.cookandbecker.com/en/article/177/dreams-a-spectacular-multigame.html)
  The direct parallel: Claybound's "everything is clay by
  construction" is the same instinct at web scale, the look comes
  from how the meshes are built, not from a post-process. The Dreams
  lesson is the escalation rule: when the construction method cannot
  reach the look, change the method, not the art direction.
- **Nintendo / Grezzo, The Legend of Zelda: Link's Awakening
  (Switch, 2019).** Toy-like plasticine characters in a diorama
  world, with a tilt-shift effect exaggerating depth of field.
  Producer Eiji Aonuma chose the diorama style to evoke the original
  Game Boy game's "small but very vast" world, and graphic refining
  director Yoshiki Haruhana says the development vision was a
  diorama world in which Link is a roughly 10 cm figurine: the team
  balanced "the charm of a richly detailed creation" against the
  imagined scale, being "careful to avoid adding in too much detail
  beyond that."
  (https://nintendoeverything.com/graphic-refining-director-yoshiki-haruhana-on-reimagining-the-visuals-of-zelda-links-awakening/ ;
  https://nintendoeverything.com/aonuma-on-how-the-art-style-came-to-be-for-zelda-links-awakening-on-switch/)
  The direct parallel: Claybound's rule that normal-map imperfection
  scales with object size is the same scale discipline Haruhana
  describes, and the tilt-shift depth-of-field pass is the cheap
  depth cue this skill's Phase 2 does not yet use.

**Agent automation**

1. **Clay-budget manifest.** Keep `clay-budget.json` per scene:
   lights per fire (1, the author's rule), bead count per fire, and
   the on-screen-only flag per fire. A headless check counts the
   lights in the scene and fails if any fire has more than one.
2. **Weak-GPU ladder test.** Render the same fire at full beads and
   at halved beads and record both frame times in the manifest; the
   halved run is the weak-GPU acceptance render, not an afterthought.
   A halved-bead render that still reads as fire passes; one that
   does not means the bead count, not the glow core, is the problem.
3. **Scale-discipline check.** For each object, record its size and
   its normal-map imperfection scale in the manifest; flag any object
   whose imperfection scale does not grow with its size. This is the
   author's Phase 2 rule made checkable, and the Link's Awakening
   scale discipline behind it.
4. **Diorama depth pass (borrowed from Grezzo, not the author).**
   Add a tilt-shift / depth-of-field pass as a named optional step
   with its strength recorded in the manifest; keep the render with
   it on as the acceptance image and the render with it off as the
   comparison. If the pass makes the scene read as a miniature
   diorama, keep it; if it only blurs, drop it.

## The human method, distilled

1. **One light per fire, not per flame**; animate only what is on
   screen.
2. **The look is three decisions**: rounded box, noise wobble, normal-map
   imperfection scaled by size.
3. **Weak-GPU fallbacks are designed in** (drop the glow core, halve the
   beads), not patched on.

**Depth status:** PARTIAL (full post text; comments unretrievable this
run; no code, parameters, or render settings disclosed).
