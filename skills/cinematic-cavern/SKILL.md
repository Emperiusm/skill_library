---
name: "cinematic_cavern"
description: "Build a cinematic cave/pool/waterfall scene end to end: Blender blockout, ZBrush sculpt, decimation to game mesh, Substance bake and PBR materials, Unreal export, scripted repairs, a C++ height-field water solver, player-to-water contact, Houdini waterfall source and surface, and final assembly with player-guiding contrast. Trigger when building a water-centric 3D environment, a game-ready rock/water asset pipeline, or a custom water solver."
---

# Cinematic Cavern

## Purpose

Reconstruct the exact human workflow for building a cinematic cavern scene
(pool, rocks, waterfall, live water) from blockout to final assembly, so an
agent can follow the same process on a new scene. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The core method throughout: decide, try, look at it from the
player's view, change what is wrong, verify the change.

**Source:** "Building a Cinematic Cavern in Unreal Engine | ZBrush, Houdini &
Water Physics" by KaigenInteractive (13:16). Companion code (water solver +
contact helper, C++17 teaching examples, build instructions, reference plots):
https://drive.google.com/file/d/1nSIfIvKz9vzCFxgL0HwoirCE8c1G1Ynf/view?usp=drivesdk

**Tools used:** Blender, ZBrush, Substance 3D Painter, Houdini, Unreal
Engine, Visual Studio (C++).

## When to use this skill

- Building a water-centric 3D environment (pool, waterfall, cave) for a game
  or cinematic.
- Setting up a rock/sculpt → game-mesh → PBR → engine asset pipeline.
- Writing a custom height-field water solver with player interaction.
- Authoring a Houdini waterfall (source network, particle cache, surface
  build, Alembic export).

## Prerequisites

- Blender (sculpt/blockout/scripting), ZBrush, Substance 3D Painter, Houdini,
  Unreal Engine installed.
- A C++17 toolchain for the water solver (teaching examples in the companion
  code).
- Comfort with the idea that the player's view is the final arbiter: every
  phase ends with a check from where the player will actually stand.

## Phase 1: Blockout (Blender)

**Do**
1. Lay out the scene with primitive planes. Establish the pool footprint and
   the path wrapping around it.
2. Connect the lower edge to the upper platform with stairs.
3. Mark arches to establish openings; use flat blue surfaces to mark water.

**Check**
- View from above: can you compare the positions of pool, path, and stairs?
- From the opposite side: do the arches read as openings?

**Why**
Plane shapes are enough at this stage. Get the structure working first, then
replace the simple forms with deliberate shapes. No finished rocks or
waterfall effects yet.

## Phase 2: Sculpt the rock (ZBrush)

**Do**
1. Start with a sphere. Establish the large shape first: a broad resting
   face, more weight at one end, taper the other.
2. Cut the main fractures with the **Dam Standard** brush. Follow the
   direction of a slab, vary the depth, stop some cuts before they reach the
   edge.
3. Clarify the faces beside the fractures with **H Polish**: short passes,
   then check how the light catches the surface, then move to the next plane.
   Keep the deeper breaks intact.
4. For areas needing more volume, use the build-up/cutback principle (Scott
   Spencer): build up slightly with the **Clay Tubes** brush, then knock the
   plane back with the **Trim Dynamic** brush.

**Check**
- After the base shape: check the outline from several directions BEFORE
  adding fractures.
- During fracturing: if every surface gets the same scratches, the rock
  becomes noisy. A few deliberate cuts give clearer structure. Leave broad
  quiet areas between breaks.
- During polishing: keep deep breaks intact; only clarify the planes beside
  them.

**Why**
Simple proportions give the later brushwork something solid to build on. Aim
for clear planes, varied edges, and quieter areas between the breaks.

## Phase 3: Reduce to a game mesh

**Do**
1. Keep the high sculpt untouched. (In the source video: ~932,000 faces after
   triangulation, about 1.86 million triangles.)
2. In Blender, make decimated candidates with the **Decimate** modifier (the
   video tested 20,000 and 40,000 triangle versions; kept the 20,000).
3. Compare each candidate's outline and deep breaks against the high sculpt
   from the same camera. The sampled surface difference stayed below a
   millimeter at this scale.

**Check**
- The visible shape is the deciding factor, not the measurement.
- Key rule: **a normal map can restore shading detail; it cannot restore a
  missing silhouette.**

**Why**
The silhouette must survive decimation. Shading detail can be baked back; a
lost outline cannot.

## Phase 4: UVs and bake (Substance 3D Painter)

**Do**
1. Give the reduced mesh clean UVs: check islands for overlap.
2. Keep the high sculpt aligned with the low mesh.
3. In Painter: select the **low mesh** for the project, the **high mesh** for
   baking. Set texture size to **2048**, **DirectX normals** (for Unreal).
4. Bake the mesh maps, then inspect the deep cuts and seams.

**Check**
- Fix obvious bake problems BEFORE building the material. The normal map
  carries the sculpted surface detail onto the lighter game mesh.

**Why**
Baking is where sculpt detail transfers to the game mesh. Errors baked here
propagate into everything downstream.

## Phase 5: Build the PBR material (Substance 3D Painter)

**Do**
1. Start with a rock **fill layer** using **triplanar projection**. Adjust the
   scale until the mineral detail feels right for the size of the rock (the
   video switched to a cliff texture for more irregular variation than the
   first shell material).
2. Keep the baked normal map from the sculpt.
3. Add restrained **cavity variation** and a **warm color layer**.
4. Moss goes on its **own fill layer**, so the stone remains underneath. Add
   a black mask and reveal only the upper areas where coverage is wanted.
5. Break up the moss boundary: a straight strip looks artificial. Make uneven
   patches, soften the edges, leave gaps of exposed stone.
6. Check the rock in the pool: the base should sit into the basin while the
   moss stays visible **above the waterline**.

**Check**
- Watch the broad faces while adjusting: the texture should support the
  shape, not bury it.
- Check from more than one angle before moving on.
- Compare top and sides while refining moss coverage.

**Why**
Separate layers keep materials editable. The waterline check prevents the
common mistake of moss sitting underwater.

## Phase 6: Export to the engine

**Do**
1. Export with the **Unreal Engine packed preset**: base color, a DirectX
   normal map, and one image with three data channels: **Red = ambient
   occlusion, Green = roughness, Blue = metallic**.
2. Import base color as **color data**; the normal map and packed data need
   their own correct texture settings.
3. Keep the same triangulation and scale used for the bake.
4. In the level: settle the rock's base into supporting ground, then check
   from the player's distance.

**Check**
- Wrong texture settings on the packed channels are a classic breakage
  point.
- Deliverable: a reusable game asset with a saved Painter layer stack, not
  just a rendered image.

**Why**
The packed preset is the contract between Painter and Unreal; the layer
stack is the asset, the export is just a rendering of it.

## Phase 7: Scripted repairs (Blender/Python)

**Do**
1. Stairs: write a script that calculates the step height, then moves nearby
   rock away from the walking surface. A script gives a repeatable repair.
2. Roof: keep the opening you actually want, and connect the enclosure
   around it.
- Principle: **fix the geometry first. Smoother shading will not close an
  unwanted hole or move a rock out of the player's path.** These are
  geometry problems, not shading problems.

**Why**
Code turns a one-off repair into a rule you can repeat and test.

## Phase 8: Build the pool bed

**Do**
1. The pool needs a bed that follows its footprint, or the water and the bank
   feel disconnected.
2. In the script: each sample becomes a vertex; the cell center gives the
   horizontal position; **water level minus bed depth** gives the height.
3. Only create a face when **all four corners are wet**, so the mesh never
   bridges a dry gap.
4. Blender handoff: convert centimeters to meters and reverse one horizontal
   axis. Check the handoff against the bank.

**Check**
- Verify the bed mesh against the bank geometry after the unit conversion.
  Unit and axis mistakes hide here.

**Why**
The bed is what the water solver stands on; a disconnected bed breaks the
illusion before a single wave is simulated.

## Phase 9: The water solver (C++)

The solver is a height-field model on a grid. Each cell stores two values:
**bed height** and **water depth**. Water surface height = bed height + depth.

**Do**
1. Flow decision: compare the **surface height** with the neighboring cell,
   not the depth.
2. Outgoing flow per cell = function of gravity, water available at the
   shared edge, the surface difference, and the time step. Damping reduces
   the previous flow. Sum what the cell wants to send out, compare with the
   water it contains, and use a **limiter** that scales outgoing flows when
   necessary.
3. Depth change = (incoming volume - outgoing volume) / cell area.
4. Keep "adding water" separate from "disturbing it": a spring adds volume;
   a running player mainly redistributes water already in the pool.
5. Run a closed-pool test: 600 steps, checking for negative depths and
   volume drift.

**Check**
- The teaching example: a raised section of bed with a level surface.
  Comparing **depth** alone creates a false wave (in the video's demo the
  broken result renders orange; the orange solver is a deliberately
  incorrect teaching copy). Including bed height on both sides keeps the
  surface level (green). This controlled test explains the formula;
  gameplay footage is a separate check.

**Why**
Surface height is the physical quantity that drives flow. Depth alone lies
whenever the bed is uneven.

## Phase 10: Player-to-water contact

**Do**
1. Transform the player into the pool's local coordinates.
2. Inject a disturbance only if three conditions hold: the player is over a
   **wet cell**, intersects the **water height**, and is **moving**.
3. The moving-body operation uses the player's direction and speed: pushes
   flow forward and spreads part of the disturbance sideways.
4. Convert units at the boundary: Unreal uses centimeters, the solver uses
   meters, so the wrapper converts position and velocity.
5. Resulting heights move the surface vertices; neighboring height
   differences update the normals.
6. Test the interaction in the actual level.

**Check**
- The three conditions prevent a character standing on a bridge from
  continually injecting a wake below it.
- After forcing stops, watch the wave spread and weaken in Unreal.

**Why**
Contact is a gate, not a constant: the three conditions are what keep the
water calm when the player is not actually in it.

## Phase 11: Waterfall source (Houdini)

**Do**
1. Build the source network. A box defines the spring at the lip: its width
   controls the emitting region, its position controls where the water
   begins. (Video's saved source: 4.7 units wide, center at 7.37 on the
   vertical axis.)
2. A wrangle does two jobs: break up the uniform source shape, and assign
   starting velocity. Downward motion stays dominant with smaller sideways
   variation.
3. Follow the connections into the boundary and the solver.
4. Once the motion is useful, save the particles: the file node reads a
   numbered cache, and the frame token selects the matching file as the
   timeline changes.

**Check**
- **Read the actual parameters instead of relying on node names.** (In the
  video, particle separation was 0.04 even though an older node label said 3
  and 1/2 cm.)

**Why**
Node labels drift from their values over a long project. The parameter value
is the truth.

## Phase 12: Waterfall surface (Houdini)

**Do**
1. **Particle fluid surface** builds a continuous surface around the cached
   particles. Save setup: particle separation **0.04**, voxel scale **0.75**.
2. Then: fit the lip, clip the body at the pool, calculate normals, and
   export the animated surface (Alembic).

**Check**
- Trade-off (from the creator's Houdini book): lower values give finer
  detail but cost more memory and processing time.

**Why**
Keeping the motion cache separate from the surface build lets you compare
surface reconstructions without re-running the simulation. Motion and
surface are separate problems: solve them separately.

## Phase 13: Assemble in Unreal

**Do**
1. The pool is live (the C++ solver). The waterfall combines **cached
   motion** with a **local player response**.
2. Import the Alembic as a **geometry cache**. Check its scale, orientation,
   and position. Play it to find the landing.
3. Make the falling surface and the pool read as one place: cached
   waterfall motion alongside the live pool simulation, with authored impact
   points across the landing.
4. Describe the impact with four layers: **foam, receiving crests,
   droplets, and mist**. Broken foam patches leave darker water visible
   between them.

**Check**
- Check the landing from the side as well as from the entrance.
- If the landing moves, the receiving effects must move with it.

**Why**
One place, two systems: the seam between cached and live is hidden by
authored impact, not by matching simulations.

## Phase 14: Guide the player with contrast

**Do**
1. Use contrast deliberately: bright opening, moving water, darker arches
   (Christopher Totten: "Contrast is an important factor in leading players
   through a game environment").
2. Return to the entrance and check the walking view.

**Check**
- A bright detail can attract attention **without helping the route**. If
   something pulls the eye away from the path, revisit its placement or
   intensity.

**Why**
Lighting is wayfinding. Every bright thing is a promise to the player; make
sure it promises the path.

## Phase 15: Test at player scale

**Do**
1. Run through the pool: disturbances feed into the height-field solver,
   creating waves and a wake behind the character.
2. For the waterfall: add a local response to the cached motion. The surface
   bends around the character with contact spray where the water hits.
3. Check the smaller fall under the arch.
4. Test **every reachable crossing**; watch the water settle after moving
   away.
5. Sound: the waterfall leads, with quieter drips and a few birds near the
   opening. Keep those layers below the narration while teaching.

**Check**
- Water must settle after the player leaves. If it does not, the solver or
  the contact conditions are wrong, not the art.

**Why**
Settling is the solver's acceptance test: a pool that never calms is a bug,
not a style.

## The human method, distilled

The decision habits the source video demonstrates, in the creator's own
framing:

1. **Blockout before detail.** Planes are enough to judge layout.
2. **Large shape before small detail.** Sphere first, outline from several
   directions, then fractures.
3. **Silhouette is non-negotiable.** Normal maps restore shading, never
   shape.
4. **Fix structure before shading.** Geometry problems need geometry fixes.
5. **Compare the right quantity.** Surface height, not depth. Actual
   parameters, not node names.
6. **Separate concerns.** Adding water vs. disturbing it. Motion vs. surface.
   Cached waterfall vs. live pool.
7. **Script what repeats.** A repair done by hand twice should become a
   rule.
8. **Test with a deliberately broken copy.** The orange-vs-green solver demo
   proves the formula is what fixes it.
9. **Judge from the player's view.** The walking view from the entrance is
   the final arbiter of placement, lighting, and water.
10. **AI writes, the human inspects.** AI helps write and revise the
    operations, but inspecting the result is where the design decisions
    happen.

Closing advice from the video: if you are making your own scene, start
small. Shape one rock, repair one water boundary, compare the change from
the path where the player will actually see it.

## Operating rules

- Never invent parameters: every number above comes from the source video or
  its companion code. Where the video gives a value (4.7-unit source width,
  0.04 particle separation, 0.75 voxel scale, 2048 textures, 600-step test),
  use it; where it doesn't, say so.
- The player's view is the acceptance test for every phase, not just the
  last one.
- This skill teaches a workflow, not a scene: adapt the phases to your own
  layout, keep the checks.
