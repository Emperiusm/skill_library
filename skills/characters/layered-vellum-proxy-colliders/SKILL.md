---
name: "layered_vellum_proxy_colliders"
description: "Layer hair simulations on top of cloth simulations in Houdini Vellum without intersection or tangling: simulate the cloth first, then give the hair layer simplified VDB-proxy colliders. Trigger when stacking sim layers that collide against each other."
---

# Layered Vellum Sims with VDB-Proxy Colliders

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle). The video's core
method is: layer hair simulations on top of cloth simulations by giving each sim layer
a collider matched to its scale, and when the upper layer misbehaves, simplify its
colliders before tuning the solver.

## Source

Creator: Chemical-Zebra-5469 (collab with wifi_retina)

Source: https://v.redd.it/2jhx8i9gbgsh1 | r/Houdini post 1wt8lu9 (score 101) |
native clip, "Wizard King (Collab) - Layered Simulations" (also cross-posted to
r/Simulated as https://v.redd.it/jfxmygnfcgsh1)

## Tools used

Houdini (Vellum cloth + Vellum hair), Marvelous Designer (garment authoring)

## Phase 1: Author the base garments in Marvelous Designer

**Do**
1. Build the garments (robe, pants) in Marvelous Designer and drape them on the character.
2. Export and bring the garments into Houdini as the base cloth meshes.

**Check**
- In a still pose, the garments sit on the character without interpenetration before any
  simulation runs.

**Why**
Marvelous produces clean, even-tessellation cloth that Vellum consumes directly. The
VDB-proxy trick in Phase 4 only works because the base mesh has believable volume to
preserve; garbage input gives a garbage proxy.

## Phase 2: Simulate the clothing layer (Vellum cloth)

**Do**
1. Set up Vellum cloth on the garments: these are the "cloth sims for the clothing."
2. Run the cloth pass to completion and let the garments reach their settled state.

**Check**
- The cloth settles without self-intersection blowups. Scrub the whole range: the resting
  garment shape is now the ground truth, and anything the hair layer collides against
  must match this state, not an earlier guess.

**Why**
Layered sims stack in order. The clothing defines the surface the tassels will collide
against; simulating the base first means the hair layer collides against a final answer.

## Phase 3: Layer the hair sims (Vellum hair, golden tassels)

**Do**
1. Set up Vellum hair for the tassels on top of the settled cloth layer.
2. Run the hair pass and watch specifically for the two named failure modes: tassels
   **intersecting the garment**, and tassels **getting stuck and tangling in between
   colliders**.

**Check**
- Scrub the tassel pass end to end. Any tassel passing through cloth or snagging on
  collider edges is a failure, however pretty the rest of the shot looks. Name which of
  the two failure modes you see: the fix is the same either way, but knowing which tells
  you where the collider is wrong.

**Why**
Hair-vs-cloth collision is the hard part of the stack. The raw simulated garment mesh is
too detailed and sticky to collide against. When the upper layer misbehaves, the collision
geometry is wrong, not (first) the solver settings.

## Phase 4: Replace the colliders with VDB proxies

**Do**
1. Do not touch solver parameters yet. Simplify the colliders "to serve as proxies for
   the simulated mesh underneath."
2. For each offending collider mesh (in the video: the pants), convert the mesh **to VDB
   and back**. The round-trip gives a simplified, watertight-ish mesh that preserves the
   volume the tassels must avoid while deleting the micro-detail that catches them.
3. Use the simplified mesh as the collider for the tassel simulation.
4. Re-run the tassel pass.

**Check**
- The tassels no longer intersect the garment and no longer tangle between colliders.
- The silhouette of the tassel motion still reads as colliding with the right body
  regions; if a tassel now floats visibly off a surface, the proxy is too aggressive and
  needs a finer VDB voxel size.

**Why**
A smooth proxy gives the hair solver a forgiving surface. Detail in a collider buys
nothing but snags. The VDB round-trip is a one-step simplifier: volume preserved, detail
gone, no manual retopology.

## The human method, distilled

1. **Layered sims need layered colliders.** Each simulation layer gets a collision
   surface matched to its scale, not the raw hero mesh.
2. **Proxy first, tune second.** "The biggest challenge on this project was simulating
   the tassels on top of the cloth sims because they would either intersect the garment
   or get stuck and tangle in between colliders. The solution was to simplify the
   colliders to serve as proxies for the simulated mesh underneath." When a sim layer
   misbehaves, fix the collision geometry before touching solver parameters.
3. **VDB round-trip as the simplifier.** Convert to VDB and back: one operation, volume
   preserved, detail gone.
4. **Sim in order, collide against answers.** Cloth settles first; hair collides against
   the settled result.

## Depth status

FULL (the creator's own breakdown; no node names or solver parameter values exist in the
source, and none are invented here)
