---
name: soft-body-sewing-garment-glb
description: "Design garments from sewing patterns in the browser, simulate them as soft bodies on an animated mannequin, and export free GLB plus textures: set particle resolution before simulating, bake with subdivision and smoothing modifiers, retopo down for low-poly targets, and fit to a Mixamo rig for skinned export. Trigger when a game needs character clothing without a DCC cloth sim."
---

# Soft-Body Sewing Tool: Garment Design to GLB Export

## Purpose

This skill reconstructs the alterproduct soft-body sewing workflow from the
author's post and comments, step by step, so another agent can follow the same
process. Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The core method is: fit the
garment to the rig, not the rig to the garment.

## Source

Creator: Longjellyrun. Reddit post:
https://www.reddit.com/r/threejs/comments/1xtm94g/full_soft_body_simulation_with_sewing_and_free_glb_exports/
(r/threejs post 1xtm94g, score 225, 15 comments). App:
https://alterproduct.com. 2026-11-13 scout run, audit 6.

This is a distinct tool from the Blender fake-sim rigging skill
(`blender-fake-sim-rigging`): that one fakes cloth motion with constraints
inside Blender; this one is a browser garment-design tool with a real soft-body
sim and GLB export. Do not merge them.

## Tools used

**alterproduct.com** (three.js plus babylon.js web app), **Mixamo** rig
(author-side, for the planned skinned export). No sim parameters disclosed.

## Phase 1: Design the garment from sewing patterns

**Do**
1. Design garments in the browser tool from sewing pattern pieces.
2. Create textures for individual sewing pattern pieces.
3. Start from the built-in templates, which "work out of the box and are fully
   editable" (author); ask the author for more templates if the garment type
   is missing.

**Check**
- Each pattern piece carries its own texture; the pieces assemble into the
  intended garment shape.

**Why**
Sewing patterns are the real-world source of truth for clothing; designing
from them keeps the garment plausible instead of shrink-wrapped.

## Phase 2: Simulate on the mannequin

**Do**
1. Simulate the garment on a mannequin, including animated mannequins, with
   live mesh editing.
2. Set the particle resolution before starting the simulation: the author says
   "Amount of triangles depends of the setted particles resolution before
   starting simulations."

**Check**
- The drape reads correctly on the posed mannequin; adjust the particle
  resolution if the cloth is too coarse or too heavy.

**Why**
Particle resolution is the quality dial, and it has to be set before the sim
runs; it cannot be fixed after the fact.

## Phase 3: Bake and export

**Do**
1. After the bake, apply modifiers with subdivision and smoothing corrections.
2. Export with or without those modifiers, as GLB plus textures, free.
3. For low-poly targets, the author's recommended route is to generate at
   mid or high poly, then bake normals and reduce the mesh with a retopo
   algorithm (author, in comments, replying to a low-poly request).

**Check**
- The exported GLB opens with the baked drape and textures intact.

**Why**
A baked drape is a static mesh; the modifiers and the retopo step are what
make that static mesh usable at a game's poly budget.

## Phase 4: Fit it to a rig (planned, commenter-driven)

**Do**
1. Export as a static mesh (or animated pose via shape keys from the baked
   simulation) for now; the current export is "a static (or animated pose -
   shape keys animation from baked simulation) ready for blender auto rig"
   (author).
2. Next step, per the author: skinned export with weights copied from the
   nearest body verts, so the garment "would let it go straight into an
   animation, even if it loses the cloth motion" (commenter PurchaseCommercial34).
   The author confirms: "I'm already using a Mixamo rig, so this sounds
   doable. I'll look into importing Mixamo-rigged models and automatically
   fitting the garments to them."

**Check**
- A skinned export must follow the Mixamo rig's proportions; commenters ask
  for automatic adjustment "based on proportions and such of the mesh," and
  for import of already-rigged hero character models.

**Why**
A static garment is a prop; a skinned garment is a wearable. The rig is the
interface, so the tool should fit to the rig instead of asking the user to
re-rig the garment.

## The human method, distilled

1. Design from real sewing patterns, not from a shrink-wrapped mesh.
2. Set the particle resolution before simulating; it is the quality dial.
3. Bake normals and retopo down for low-poly targets instead of simulating
   at low poly.
4. Fit the garment to the existing rig (Mixamo), because that is where the
   characters already live.

## Failure modes

- **Simulating at low poly.** Low-poly sims look bad and cannot be fixed
  afterwards. Generate mid or high poly, then bake normals and retopo down.
- **Expecting a skinned export today.** The skinned export is planned, not
  shipped. What ships now is a static mesh (or shape-key pose) ready for
  Blender auto-rig.
- **Expecting sim parameters.** The author discloses no solver parameters,
  particle counts, or timings. Treat the sim as a black box with one dial:
  particle resolution.

**Depth status:** PARTIAL (full post text plus all 15 comments; the sim has no
disclosed solver parameters, particle counts, or timings, and the video itself
was not frame-reviewed).
