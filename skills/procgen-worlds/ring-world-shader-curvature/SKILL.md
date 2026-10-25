---
name: ring-world-shader-curvature
description: "Fake a ring world without building one: lay out a flat strip holding every biome, then bend space with a curved-space shader so it reads as a ring. Rendering is cheap; interaction and lighting agreement are the debts. Trigger when faking large-scale world shape with shaders, or when judging whether a shader illusion is shippable as a game world."
---

# Ring World as a Shader Illusion (Flat Strip + Curved Space)

## Purpose

This audit reconstructs the technique from the author's post and 29
comments, step by step, so another agent can follow the same process.
Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The video's core method
is: do not build the ring; bend flat space with a shader so it reads as
a ring.

## Source

Creator: k0zakinio. Reddit post:
https://www.reddit.com/r/proceduralgeneration/comments/1xcxac1/a_look_around_my_ring_world_prototype/
(r/proceduralgeneration post 1xcxac1, score 361, 29 comments) | Game:
RIDGERUNNERS (Steam app 4970370) | 2026-10-24 scout run.

## Tools used

Tools used: undisclosed engine; a curved-space shader over a flat strip
(author's description). No shader code, engine name, or parameters were
disclosed; everything below is the author's account plus commenter
proposals, labeled as such.

## Phase 1: Lay out the flat strip

**Do**
1. Build the world as a flat strip containing every biome (the author's
   original purpose: one playtest map for all biomes).
2. Keep the variant: the author liked how it turned out, so the test map
   became a map in its own right.

**Check**
- The strip reads as a ring from the player's view; the author reports
  the cost honestly: "Took a bit of work keeping it running smoothly
  with so much scenery visible at once!"

**Why**
- A shader illusion is cheaper than ring geometry, but the perf problem
  does not vanish: everything is visible at once, so the culling/LOD
  budget is the real work.

## Phase 2: Bend space in the shader

**Do**
1. Apply the curvature as a shader transformation: the landmass curves
   because the shader says so, not because the geometry is curved.
   (Author, verbatim in substance: "the curvature is all a shader
   illusion".)

**Check**
- Looking up shows the ring continuing overhead; the high FOV makes
  looking up "look a little bit strange" (commenter observation the
  author does not dispute).

**Why**
- The illusion holds exactly where the player only looks. It breaks
  exactly where the game must interact with the world (Phase 3).

## Phase 3: Accept the interaction limits (and the lighting debt)

**Do**
1. Accept that shooting, throwing, teleporting, and collision do not
   agree with the curved positions: a tree that curves up away from the
   player cannot be shot or landed on correctly by flat-space physics.
2. Defer the lighting/shadow problem explicitly: "any lighting and
   shadows would need to agree with the curved positions" (author's
   words).

**Check**
- Commenter-proposed workarounds, not author-confirmed fixes: loop
  positions with modulus arithmetic at two arbitrary edges (with the
  caveat that trajectories need the inverse of the shader's spatial
  transformation, and gravity must still integrate in linear space);
  sync a simple collider with the same curvature (commenter verdict:
  "might be more trouble than it's worth"); place a sun at the ring's
  center so any directional light does the right thing (commenter
  suggestion; the author is "deferring thinking about that").

**Why**
- A rendering illusion and a simulation must agree to be a game. This
  skill's transferable lesson is the shape of the debt: shader-space
  tricks are cheap to render and expensive to make playable, and the
  lighting/shadow agreement is a second, separate debt from the physics
  agreement.

## The human method, distilled

1. **Fake the world, pay in interaction**: curvature as a shader is a
   rendering win and a simulation IOU.
2. **Name the deferred work**: lighting/shadow agreement is explicitly
   deferred, not forgotten.
3. **Playtest maps can become maps**: a biome testbed that reads well
   earns its place as a variant.

## Failure modes

- **Interaction breaks at the curve**: shooting, throwing, teleporting,
  and collision disagree with curved positions. No author-confirmed fix
  exists; the commenter proposals above are the starting points.
- **Lighting/shadow disagreement**: deferred by the author; any take
  that ships without it is visibly wrong wherever shadows fall.
- **Not skyline fill**: this trick fakes world curvature. It is not the
  shader-driven skyline-fill pattern (unmodeled buildings as shader
  output) and must not be cited as evidence for it.

## AAA studio practice

**Do**
1. Use the shipped game version of this trick, not only the prototype version. Nintendo's Animal Crossing uses the "rolling log" world bending effect: terrain bends and rolls beneath the player so ground and sky are visible at once, a technique the producer described as chosen for the DS to show sky on the upper screen. Subway Surfers uses the same family of effect, curving the world exponentially with distance from the player. Source: https://notslot.com/tutorials/2020/04/world-bending-effect and https://www.rigormortistortoise.com/how-to-make-a-curved-world-shader-graph-subway-surfers/
2. Apply the production rules from the Curved World shader documentation: every bending effect has a pivot point (the origin for the bending algorithm, updated from a controller script, usually the player), meshes need enough vertices to bend smoothly (a 4 vertex ground plane will never bend), and meshes can disappear from early culling unless a curved world camera handling step is added. Source: https://amazing-assets.gitbook.io/curved-world/tutorial-2-little-planet-part-1
3. Automate the shader illusion as agent-executable steps, which directly address this skill's Phase 3 debts:
   - Vertex density check: script a scan of every mesh using the bend shader and flag any mesh whose vertex spacing is coarser than the bend radius tolerance (read the tolerance from the shader's curvature parameter, never invent it); subdivide flagged meshes or exclude them from bending and log the exclusion.
   - Pivot check: assert the bend pivot follows the player every frame, and that all bent materials share one bend type and bend ID; log any material that still uses a default shader (the equivalent of the original thread's unbent bullet mesh problem, where runtime spawned meshes missed the bend shader).
   - Interaction agreement check: place a test target at a known curved position, fire a test projectile in flat space, and record the miss distance; if the miss exceeds one target radius, the interaction debt is open and the feature must not ship as playable (this turns the skill's "cannot be shot correctly" warning into a measured gate).
   - Culling check: move the camera through the full FOV range and log any mesh that pops in or out; the high FOV "looks strange" observation in the original thread is the symptom this check catches.

**Check**
- Looking up shows the ring overhead with no popping, no unbending meshes, and no flat shader leftovers. Shooting, throwing, and teleporting either agree with curved positions or are explicitly disabled in curved zones, with the decision logged.
- Lighting is either agreed with curved positions or explicitly deferred in the same way the original author deferred it, never silently wrong.

**Why**
- Animal Crossing and Subway Surfers prove the trick ships, but only when the production rules are obeyed: pivot follows the player, vertices are dense enough, every material (including runtime spawned ones) uses the bend shader, and culling is handled. The prototype's debts (interaction, lighting) are exactly the places where a shipped game either pays the cost or scopes the feature down, and the checks above make that decision measurable instead of hopeful.

**Depth status:** PARTIAL (post text + 29 comments; engine, shader code,
and parameters undisclosed; commenter fixes are proposals, not
author-confirmed).
