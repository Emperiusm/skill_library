---
name: flesh-dynamics-godot-soft-body-paint
description: "Add runtime soft-body flesh physics to an animated Godot character with Flesh Dynamics: paint which parts of the mesh are soft, let them jiggle, squash against colliders, and push rigid bodies back, ship one godot-cpp binary for Godot 4.3 to 4.7 built against the 4.3 API, weld seam vertices with a 26-neighbour check, and ship plain paths instead of uid:// paths. Trigger when a rigged Godot character needs localised soft-body secondary motion without building a solver."
---

# Flesh Dynamics: Soft-Body Flesh Physics in Godot (Paint Soft Regions, Runtime Solver)

## Purpose

This skill reconstructs the exact workflow Rudy_AA shows for Flesh Dynamics, a paid GDExtension addon that adds soft-body flesh physics directly to animated characters in Godot. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: paint softness onto an already-rigged, already-animated mesh, and let a native solver do the jiggle at runtime.

## Source

Creator: Rudy_AA. Post: "I made a Godot plugin that adds soft-body flesh physics directly to animated characters" — https://www.reddit.com/r/godot/comments/1y6sn3t/i_made_a_godot_plugin_that_adds_softbody_flesh/ (score 1699, 67 comments, 25 retrieved). Video: https://v.redd.it/o4stvjyqh54i1. Store page: https://frostpunchgames.itch.io/flesh-dynamics-godot. Scout audit 2026-11-28, audit 2, PARTIAL.

## Tools used

Godot 4.3 to 4.7, godot-cpp / GDExtension, Flesh Dynamics (paid addon, also available on Unity and Unreal). No stiffness, damping, paint-brush, or performance numbers are stated. No price is stated in the retrieved text; check the store page before buying. The addon does not rig or retarget; it needs a rigged, animated mesh. It does not fill the rigging/skinning/retarget gap.

## Phase 1: Paint which parts are soft

**Do**
1. Take an animated character mesh with an existing rig and animations.
2. "You paint which parts of a mesh are soft" (post text, verbatim). No brush name, falloff, or paint-value range is stated.

**Check**
- Painted regions are the ones that move in the clip (the demonstration centers on a belly). Unpainted regions stay rigid with the animation.

**Why**
Painting softness per region keeps the effect local: the animator's keyframed motion stays authoritative everywhere except where softness was painted.

## Phase 2: Run the solver at runtime

**Do**
1. At runtime the painted parts "jiggle, squash against colliders and push rigid bodies back" (post text, verbatim).

**Check**
- Squash reads against colliders in the clip, and rigid bodies react to the soft body pushing back. No frame-time or solver-iteration number is given.

**Why**
Two-way response (squash and push-back) is what separates a soft-body solver from a cosmetic jiggle bone: the soft body affects the world, not only itself.

## Phase 3: Ship one binary for Godot 4.3 to 4.7

**Do**
1. Build godot-cpp against the 4.3 API. "Building godot-cpp against the 4.3 API gave me a single DLL that loads in 4.3, 4.4, 4.5, 4.6 and 4.7. I tested each version from a fresh project." (post text, verbatim).
2. Test each version from a fresh project, not from the development project.

**Check**
- The single DLL loads in each of 4.3, 4.4, 4.5, 4.6, and 4.7. The author states all five were tested.

**Why**
Building against the oldest supported API is the compatibility decision; testing from fresh projects proves the DLL carries no development-project dependency with it. Inference, labeled: the "no hidden dependency" reading is the auditor's inference from the author's stated method.

## Phase 4: Weld split seam vertices with a 26-neighbour check

**Do**
1. Join split seam vertices by rounding positions into grid buckets.
2. Check the 26 neighbouring cells too. The edge case: "Two copies of the same corner that differ by floating-point noise can round into neighbouring cells and never get joined. On Godot's BoxMesh and CylinderMesh that tore faces apart under deformation. The fix is to check the 26 neighbouring cells too." (post text, verbatim).

**Check**
- BoxMesh and CylinderMesh no longer tear faces apart under deformation. Those two primitive meshes are the author's named repro cases.

**Why**
Floating-point noise at a seam is invisible in a static mesh and catastrophic under deformation. The weld has to be robust to noise, not merely to exact duplicates.

## Phase 5: Ship plain paths, not uid:// paths

**Do**
1. If shipping models with "Save to File", ship the plain path. "Godot 4.5+ writes that path as `uid://`. Godot 4.3 fails the import outright, and 4.4 quietly embeds the mesh instead. Ship the plain path." (post text, verbatim).

**Check**
- The model imports in 4.3 (no outright failure) and in 4.4 (no silent embedding).

**Why**
A path format that is convenient in the newest version silently breaks the oldest supported version in two different ways. The plain path is the only form that behaves the same across the range.

## Failure modes

- Painting softness onto an unrigged or unanimated mesh and expecting the addon to animate it. It operates on animated characters.
- Welding seam vertices by exact position only, then watching BoxMesh and CylinderMesh tear under deformation.
- Shipping `uid://` paths and failing imports on Godot 4.3, or silently embedding meshes on 4.4.

## The human method, distilled

1. "Upfront: this is a paid addon" (post text, verbatim). Disclosure first, before the demo.
2. Build against the oldest API in the supported range, then prove it in a fresh project per version.
3. Fix the seam case that only deformation reveals, and name the exact repro meshes.
4. Ship the path form that behaves identically across versions, not the form the newest editor writes by default.

**Depth status:** PARTIAL. The paint-softness concept, the five-version binary method, the welding fix, and the uid:// gotcha are all stated by the author with named repro cases. Solver parameters, paint controls, price, license terms, and performance numbers are unknown, and 42 of 67 comments were not retrieved. What would reach FULL: the store page's parameter list and price, or the author's answers in the unretrieved comments.
