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

## The human method, distilled

1. **Viscosity is local and temporary**: thicken for the stroke, relax
   after.
2. **Sparkle is a normal, not a mesh**: randomize, don't model.
3. **Cache time is the budget**: 8 hours means late in the schedule.

**Depth status:** PARTIAL (post text + all 12 comments; no solver
parameters, viscosity values, or node graph).
