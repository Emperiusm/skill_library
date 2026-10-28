---
name: ai-3d-game-optimization
description: "Ship AI assets in games on a performance budget: role-based triangle, texture, and material budgets, bake-before-reduce, ORM packing, LOD chains with transition thresholds, and collision proxies. Trigger when an AI asset needs to run in a game at frame rate."
---

# Optimize AI 3D Assets for Games

## Purpose

This skill puts AI-generated assets on a performance budget before they
reach an engine, so frame rate is decided by a plan instead of by
accident. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The core
method is: budget by role, bake before reducing, chain LODs, and prove
the result at gameplay distance.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/how-to-optimize-ai-3d-assets-for-games
- https://customuse.com/learn/what-are-lods-in-3d-game-assets

Evidence note: the optimization article's final FAQ answer was unseen;
all substantive sections were read.

## Tools used

Tools used: DCC tools (Blender, Maya) for retopology, baking, and LOD
generation; engines (Unity, Unreal) for profiling and LOD transition
testing. No single optimizer tool is prescribed by the sources; the
budget and the bake order matter more than the tool.

## Phase 1: Assign a role budget before touching the mesh

**Do**
1. Assign the asset a role and a budget tier before optimization:
   background props live in a few hundred to a couple thousand
   triangles; hero assets and characters run much higher.
2. Set the texture budget with the same discipline: 512 for background
   work, 1024 as the standard, up to 2048 for finals, 4K only for
   heroes. Worked budgets from the sources: a mobile lantern at about
   3K triangles with one 2K texture set; a crate at about 2,400
   triangles.
3. Treat any raw generator output as over budget by default: outputs
   routinely arrive in the tens or hundreds of thousands of triangles.

**Check**
- Is the budget tier written down and approved before work starts?
- A 50K-triangle prop on mobile is a budget leak, not a detail win.
  Does anything in the set match that description?

**Why**
Optimization without a budget is just reduction without a target. Role
is what makes a triangle count right or wrong: the same 3K that is
generous for a background prop is starvation for a hero.

## Phase 2: Bake before you reduce

**Do**
1. Keep the high-poly aside. Bake its detail into maps (normal, and
   the PBR set) before reducing the cage.
2. Retopologize to the budgeted low-poly cage, then verify the bake
   reads under real lighting.
3. Pack occlusion, roughness, and metallic into one ORM texture:
   ambient occlusion in R, roughness in G, metallic in B. One texture
   fetch instead of three is a real saving across a whole set.

**Check**
- Does the low-poly read like the high-poly at gameplay distance?
- Are the ORM channels in the right slots? A swapped channel is a
  silent material failure.

**Why**
Bake-before-reduce is the order that preserves detail: reduction first
destroys the surface the bake was supposed to capture. ORM packing
compounds the saving on every asset that shares the material pipeline.

## Phase 3: Build the LOD chain

**Do**
1. Generate LODs at halving ratios: 100 percent, 50 percent, 25
   percent, 12 percent. The crate example ships two LODs; the lantern
   ships LOD1 and LOD2.
2. Set transition thresholds by gameplay distance: each LOD must hold
   at the distance where it actually appears, not in a closeup
   inspection.
3. Decide the Nanite exception explicitly for Unreal work: Nanite
   changes what LODs are for, so record whether the asset uses Nanite
   or a manual chain. Never leave it ambiguous.

**Check**
- Does each LOD hold at its transition distance in the real level?
- Are transitions invisible at gameplay speed, or do they pop?

**Why**
LODs are the difference between a scene that ships and a scene that
chokes: distant assets must stop costing hero-level triangles. A chain
with no tested thresholds is a guess, not an optimization.

## Phase 4: Add collision, compression, and the pivot

**Do**
1. Add a collision proxy matched to the asset's job (a collision box
   on the crate), not the render mesh.
2. Compress textures for the target platform.
3. Move the pivot to the base so the prop sits on the floor correctly,
   and freeze transforms.

**Check**
- Does the asset sit, collide, and import at the right scale and
  orientation in the engine?
- Is the pivot where a designer expects it, not where the generator
  left it?

**Why**
Collision from the render mesh is a physics cost paid on every frame
for detail nobody collides with. Pivot and scale errors are the
cheapest failures to prevent and the most embarrassing to ship.

## Phase 5: Profile in context

**Do**
1. Drop the optimized asset into the real level with its LODs and
   compressed textures.
2. Profile at gameplay distance and up close, at the target frame
   rate, on the target hardware class.

**Check**
- Does the set hold frame rate with all optimized assets present, not
  just this one in isolation?
- If it does not, which budget tier is wrong: the asset's, or the
  scene's?

**Why**
Optimization is a scene property, not an asset property. A single asset
can pass every check and the level can still fail; the profile is the
only verdict that counts.

## The human method, distilled

1. Role first, numbers second. Budget tiers decide everything else.
2. Bake before reduce, always. Order is the technique.
3. Pack ORM. Small per-asset savings compound across a set.
4. Halve LODs, test thresholds at gameplay distance.
5. Collision proxies, never render meshes, for physics.
6. Profile the scene, not the asset.

## Depth status

FULL (article text; substantive sections read, one final FAQ answer
unseen).
