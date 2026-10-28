---
name: flip-local-viscosity-fake-normals
description: "Finish a Houdini FLIP shot two cheap ways: raise viscosity only where the collider moves so strokes hold their shape, then let it relax so the surface settles, and fake sparkle by randomizing the gel's normals instead of adding sparkle geometry. Budget the cache explicitly: the author's sim took around 8 hours. Trigger when a gel or fluid stroke must hold its shape, or when sparkle geometry would cost more than it is worth."
---

# FLIP Local Viscosity + Fake-Normals Sparkle

## Purpose

This skill reconstructs the technique from the author's post and
comments, step by step, so another agent can follow the same process.
Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The video's core
method is: thicken the fluid only where the collider moves, and fake
the sparkle with normals instead of geometry.

## Source

Creator: Liivaan. Reddit post:
https://www.reddit.com/r/Houdini/comments/1xdgr45/flip_sim_with_local_viscosity_changes_and_the/
(r/Houdini post 1xdgr45, score 184, 12 comments) | 2026-10-25 scout run,
audit 6.

## Tools used

**Houdini** FLIP sim (author: "a combination of a few tricks in
Houdini"). No solver, viscosity values, particle counts, or node names
disclosed; none are claimed here.

## Phase 1: Thicken locally where the collider moves

**Do**
1. Wherever the collider moves through the fluid, raise the local
   viscosity so the strokes hold their shape.
2. Let the viscosity relax back to its original value afterward, so
   the surface slowly settles.

**Check**
- Strokes must hold their shape during the pass and settle slowly
  after; a globally thick fluid would never settle, and a globally
  thin fluid would never hold a stroke.

**Why**
- Local viscosity is a time-varying material property, not a solver
  setting: thicken for the gesture, relax for the rest.

## Phase 2: Fake the sparkle with randomized normals

**Do**
1. Add no sparkle geometry.
2. Randomize the normals on the gel, so tiny patches catch the light
   at different angles as it moves.

**Check**
- Commenters confirm the read: "Those sparkles look really nice" and
  "the normals randomisation is genius." The sparkle must move with
  the surface, not sit on it as separate geometry.

**Why**
- A normal perturbation is nearly free compared to sparkle geometry,
  and it moves correctly by construction because it rides the surface.

## Phase 3: Budget the cache

**Do**
1. Budget for a long cache: the author reports "The FLIP sim took
   around 8 hours to cache."

**Check**
- 8 hours is the only performance number in the audit; no particle
  count, hardware, or resolution is disclosed, so no per-particle rate
  is derived from it.

**Why**
- A trick that costs 8 hours to cache is a finishing trick, not an
  iteration trick: run it late, not while blocking the shot.

## AAA studio practice

Production FLIP work treats viscosity as a field you paint and schedule, not a single solver value. SideFX's own FLIP documentation lists "custom fields like varying viscosity and mass-density" as a core feature of the SOP-based FLIP workflow, and notes the DOP workflow remains production-proven precisely because studios built their own networks around it. The practitioner rule from production FLIP writing is the same: FLIP fluids have no viscosity by default, so time-dependent and non-Newtonian viscosity are inputs the artist supplies, with 32-bit solves recommended for faster viscosity solves and surface visualization used to read viscous fluids. That is the formal version of this skill's Phase 1: thicken where the collider moves, relax afterward, as a time-varying attribute. The fake-normals sparkle has its own production lineage: Autodesk's Arnold flakes shader creates glitter by putting flake variation into the normal (and coat normal) layers rather than modeling sparkle geometry, and real-time sparkle research (TU Graz) treats sparkle as a view-dependent normal/noise function with explicit sparkle-size and sparkle-density parameters, implemented in a AAA title's snow scene.

- Source: http://www.sidefx.com/docs/houdini/fluid/dopversussop.html (SideFX: SOP FLIP custom fields including varying viscosity; DOP production-proven)
- Source: https://www.katexagoraris.com/super-fluids (production FLIP notes: no default viscosity, time-dependent/non-Newtonian viscosity as input, 32-bit viscosity solves, surface visualization)
- Source: https://help.autodesk.com/cloudhelp/ENU/AR-Houdini/files/tutorials/shading/arnold_for_houdini_shading_ah_Flakes_Example_html.html (Arnold flakes: glitter via flakes in the normal and coat-normal layers, not geometry)
- Source: http://diglib.cgv.tugraz.at/bitstream/handle/10.2312/sre20161209/049-054.pdf (real-time sparkle effect: view-dependent sparkle with size/density parameters, implemented in a AAA title)

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Replace the Phase 1 description with an explicit viscosity field: drive local viscosity from collider distance (an attribute ramp, not a global value), with a relaxation curve back to the base value logged per frame. The ramp parameters and the relaxation time are written into the shot notes, so the "thicken then settle" behavior is reproducible instead of hand-tuned per sim.
2. Replace the Phase 2 description with an explicit normal-noise parameter: sparkle density and normal-randomization amplitude as named values, rendered as a before/after pair (flat normals versus randomized) so the sparkle contribution is measurable, not just visible.
3. Automate the Phase 3 budget as a comparable record: log resolution, particle count, hardware, and cache hours for every run. The author's 8 hours becomes a baseline other runs can be compared against, instead of a single anecdote.
4. Gate the finishing pass on the budget log: a run that exceeds the logged baseline by a wide margin triggers a resolution or particle-count review before the cache is committed.

**Check**
- Viscosity is an attribute field with a logged relaxation curve, not a single solver value.
- Sparkle has named density and amplitude values with a before/after render pair.
- Every cache run logs resolution, particle count, hardware, and hours.
- Budget overruns trigger a review before the cache is committed.

**Why**
- A finishing trick that cannot be reproduced or budgeted is a one-off, not a pipeline step. Naming the viscosity field, the sparkle parameters, and the cache cost turns this audit's three observations into settings the next shot can reuse and the next budget can plan around.

## The human method, distilled

1. **Viscosity is local and temporary**: thicken for the stroke, relax
   after.
2. **Sparkle is a normal, not a mesh**: randomize, don't model.
3. **Cache time is the budget**: 8 hours means late in the schedule.

**Depth status:** PARTIAL (post text + all 12 comments; no solver
parameters, viscosity values, or node graph).
