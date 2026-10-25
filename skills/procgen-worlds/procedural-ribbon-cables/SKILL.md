---
name: procedural-ribbon-cables
description: "Generate ribbon cables procedurally with parametric controls instead of modeling by hand. Trigger when detailing hard-surface props."
---

# Procedural Ribbon cables

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Detail procedurally: ribbon cables generated with parametric controls instead of modeled by hand.

## Source

Creator: deepak365days

Source: https://v.redd.it/v7m78fgu9eqh1 | r/proceduralgeneration post 1wkatjx

## Tools used

Tools used: Blender 3D (confirmed by the author in comments: "Blender 3D").
[inference]: the generator's node/graph internals are never stated; the
workflow below reconstructs only what the clip and comments confirm.

**Do**
1. Build the cable generator in Blender as a procedural system, so cable
   paths, lengths, and twists can be regenerated rather than hand-modeled.
2. Expose end points for post-generation adjustment: a commenter asked
   whether ends can be manually adjusted after generating, and the author
   answered "Yes" (the exact adjustment workflow is not shown).

**Check**
- Regenerate: does a fresh seed produce a new valid cable layout without
  broken ends?
- Can the ends be moved after generation without breaking the procedural
  system?

**Why**
Procedural generation earns its keep when the output stays editable. The
author's yes to end-adjustment is the main confirmed workflow property.

## Phase 1: Build the procedural cable system [inference: reconstruction]

## Phase 2: Randomized color assignment [inference: minimal reconstruction]

**Do**
1. Leave color randomization on its default: the cables are mostly red
   because the author "didn't adjusted color ramp"; the colors are random.
2. If a specific palette is needed, the author confirms the system is
   procedural and "user can change colors as per need".

**Check**
- Watch a regeneration: are colors random across cables? If a deliberate
   palette is wanted, adjust the color ramp.

**Why**
The red look is incidental (unadjusted defaults), not a design choice. In a
procedural system, unrandomized defaults read as intentional; either seed
the ramp or accept the default.

## The human method, distilled

1. **Keep generator outputs adjustable.** A procedural system that locks its
   results is just a fancy static mesh; confirmed end-adjustment is what
   makes this one a tool.
2. **Random defaults are not design decisions.** If the color ramp is
   unadjusted, say so; viewers will read intention into randomness.
3. **Expose the levers users ask about.** The thread's questions were ends,
   colors, and further modulation ("weirder and weirder sounds"); the author
   answered all three as doable.

## AAA studio practice

**Do**
1. Build cables from curves, not from hand placed meshes. SideFX documents a Houdini Cable Generator that takes a curve of high pin points and low sag points and generates sagging cables with user definable cable count, shape, and colour. Source: https://media.sidefx.com/uploads/tutorial/foundations/houdini_foundation_overview_01.pdf
2. Ship the cable tool inside the editor artists already use, the way Ubisoft did on Far Cry 5: Houdini tools (including power lines, freshwater, cliffs, and biomes) were integrated into the game editor through Houdini Engine so artists crafted the world with Houdini tools from inside their familiar editor. Source: https://blog.playstation.com/archive/2018/03/22/how-the-stunning-open-world-of-far-cry-5s-hope-county-montana-was-created
3. Automate the Blender version as explicit agent-executable steps (this converts the skill's confirmed but manual "adjustable ends" property into a testable tool):
   - Create a curve object with two endpoint empties as the control handles; drive the cable mesh from the curve with a bevel profile, so moving an endpoint re-solves the cable instead of breaking it.
   - Expose, as named parameters, cable count, sag amount, twist, and a colour ramp seed; never leave the ramp on an unadjusted default in a shipped asset (the original thread's red cables were an unadjusted default, not a design choice).
   - Write a regeneration script: move each endpoint by a fixed offset, regenerate, and assert the cable still connects both endpoints and the mesh has no zero length segments. Log the seed used for each regeneration.

**Check**
- Move an endpoint after generation: the cable must follow without manual remodelling. If it does not, the system is a static mesh with a generator story, not a procedural tool.
- Regenerate with a new seed: cable paths, lengths, and twists change; endpoint positions do not drift.

**Why**
- The AAA pattern is curve in, tool out, editor integrated. Ubisoft's Far Cry 5 team used procedural tools to remove tedious hand work so artists could focus on the world, and the Houdini cable generator shows the exact input shape (pin and sag points on a curve) that makes that work. A cable tool that cannot survive an endpoint move fails the only workflow property the original author confirmed.

## Depth status
 DEPTH-LIMITED (author confirms "Blender 3D", procedural
system, random unadjusted colors, and adjustable ends, but no node setup,
parameters, or geometry method are stated anywhere; phases above are mostly
[Inference] scaffold around those four facts)

---
