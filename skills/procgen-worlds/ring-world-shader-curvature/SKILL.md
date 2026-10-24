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

**Depth status:** PARTIAL (post text + 29 comments; engine, shader code,
and parameters undisclosed; commenter fixes are proposals, not
author-confirmed).
