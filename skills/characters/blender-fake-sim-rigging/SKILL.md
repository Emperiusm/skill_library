---
name: blender-fake-sim-rigging
description: "Rig soft-body secondary motion with Blender constraints instead of a simulation: Stretch To + Track To guide bones drive jiggle without cloth sim or blend shapes. Trigger when a rig needs cheap secondary motion for animation or game export."
---

# Fake Simulation Rigging in Blender: Stretch To + Track To

## Purpose

Build constraint-driven "fake simulations" on a character rig: deform bones
get jiggle and soft-body-style secondary motion from a Stretch To + Track To
guide-bone chain, with no cloth simulation and no blend shapes. The pattern is
cheap (constraints only), exportable to game engines, and deliberately simple
so it adapts to "pretty much anything."

## Source

Creator: u/Broad-Requirement-83

Source: https://v.redd.it/dpngmfgx9oth1 | r/3Dmodeling post 1wyclry (score
800, 42 comments) | native clip (demo, not tutorial)

Stated use case: "intended for animation and game-development workflows,
including NSFW projects." This audit reconstructs the workflow from the
author's own post text and explanatory comment. The video's core method is:
fake the simulation with constraints instead of running one.

## Tools used

Blender (bone constraints: Transform, Stretch To, Track To, Stretch). No
named plugins or versions in the evidence.

## Phase 1: Lay out the base bones

**Do**
1. Build the standard base bone chain for the character; these are the bones
   that actually drive the mesh.
2. Plan the constraint chain the author describes (author's own words):
   **"Base bone -> modifier -> constraints -> guide bone -> modifier
   (transform, location, etc.) -> constraints."**

**Check**
- Each base bone feeds through a modifier into constraints on a guide bone,
  which feeds through its own modifier into the final constraints. If the
  chain order drifts from this, the authoring logic becomes untraceable.

**Why**
The system is constraints-driven: "if this bone transforms in this way, then
this should do that" (author). The author reports spending most of their time
organizing the logic graph per bone, not adding bones.

## Phase 2: Build guide bones with Track To + Stretch

**Do**
1. Add guide bones: the bones that track targets and carry stretch.
2. Give each guide bone a **Track To** constraint (aims at its target)
   **and also the Stretch modifier** (author: the guide bones "had Track To
   and also had the Stretch modifier").

**Check**
- [inference] Move a guide bone's target: the bone should point at the target
  and elongate. Track gives direction, Stretch gives distance response.

**Why**
The Track To + Stretch pair turns a target's motion into a direction-plus-
stretch signal that the deform bones in Phase 3 consume. [inference] Without
the Stretch modifier the guide bone would only rotate, and there would be no
distance value to fake the soft-body squash.

## Phase 3: Add Stretch To with low values on the deform bones

**Do**
1. On the mesh-deforming bones, add **Stretch To** constraints pointed at the
   Phase 2 guide bones.
2. Keep Stretch To values **low** (author: "I used Stretch To with low
   values"). The author published no numeric values; start small and tune by
   eye.

**Check**
- The deform bone stretches subtly toward its guide bone. If it overshoots or
  collapses the silhouette, the value is too high. "Low values" is the
  author's only published guidance.

**Why**
Low-value Stretch To produces jiggle and secondary motion that reads as
soft-body response without enough deformation to break the silhouette. This
is the "fake simulation" the title promises: zero simulation solve, zero
blend-shape set.

## Phase 4: Drive behavior with Transform constraints

**Do**
1. Add **Transform** bone constraints so one bone's transform drives
   another's: "Everything uses Transform modifiers" (author).
2. Author the conditional logic per bone: "if this bone transforms in this
   way, then this should do that" (author). Map specific base-bone motions
   (location, rotation) to specific deform-bone responses.

**Check**
- [inference] Pose the base bones through the character's full range and
  confirm each dependent bone responds with the authored motion; adjust the
  Transform mappings where the response feels wrong.

**Why**
Transform constraints are the control layer: raw bone motion becomes
authored, repeatable secondary motion. [inference] This is what makes the
rig predictable where a real simulation would be chaotic and expensive.

## The human method, distilled

1. **Fake it with constraints, don't simulate.** Stretch To + Track To on
   guide bones gives soft-body read at zero sim cost. (author)
2. **Keep the system simple on purpose:** "The system and approach I used are
   quite simple, so with a few small adjustments, you can adapt them to
   pretty much anything." (author)
3. **Spend the time on the logic graph,** not on more bones: organizing the
   if-this-transforms-then-that mappings is the real work. (author)
4. **Low values on Stretch To** are the tuning rule of thumb; no numbers were
   published, so tune against the silhouette.
5. **What this is not:** an automated rigging stage. It fills no
   auto-rig/retarget need; it is a manual pattern for secondary motion that
   pairs well with any existing rig.

## Depth status

PARTIAL. The constraint architecture, exact constraint names, and the tuning
rule are quoted from the author's own comment; the base-bone chain order is
the author's quoted formula. Stretch To numeric values, Blender version, and
engine export path were not published. Failure modes and fixes beyond
"overshoot means too high" are [inference]; the native demo clip itself was
not reviewed (no frames extracted for v.redd.it in this pipeline).
