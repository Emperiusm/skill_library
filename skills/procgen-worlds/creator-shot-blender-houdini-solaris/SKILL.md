---
name: creator-shot-blender-houdini-solaris
description: "Recreate a film shot end to end: model in Blender, texture in Substance Painter, light and assemble in Houdini Solaris, comp in Nuke, with bought-in vegetation, terrain, and cliffs. Trigger when a shot needs a full DCC pipeline rather than a single-tool build."
---

# The Creator Shot Recreation: Blender to Houdini Solaris to Nuke

## Purpose

This skill reconstructs the author's exact workflow, step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The shot's core method is: model in Blender, texture in Substance Painter,
light and assemble in Houdini Solaris, comp in Nuke, with bought-in
vegetation, terrain, and cliffs.

## Source

Creator: Key-Swimmer3238 (Atharva). Reddit post:
https://www.reddit.com/r/Houdini/comments/1xw7t59/the_creator_shot_recreation/
(r/Houdini post 1xw7t59, score 106, 12 comments) | 2026-11-15 scout run,
audit 1. Full breakdown linked by the author (ArtStation artwork lEraae)
returned HTTP 403 when fetched and could not be read this run.

## Tools used

Blender (modeling), Substance Painter (texturing), Houdini + Solaris
(lighting and scene assembly), Nuke (comp), Meadow toolkit (vegetation
scattering, by beatreichenbach), KTT terrains, Megascans cliffs, vegetation
assets (external).

## Phase 1: Model in Blender

**Do**
1. Model the temple, cliff base forms, and monk models in Blender.
2. Leave vegetation and Megascans cliffs as bought-in assets; do not remodel
   them.

**Check**
- The shot holds up at this scale even where the monk cloth sims are bad
  (author: "they hold up at this scale and give the shot some movement").

**Why**
- At shot scale, movement matters more than cloth correctness. Spend modeling
  effort where the camera lingers.

## Phase 2: Texture in Substance Painter

**Do**
1. Texture the modeled assets in Substance Painter.

**Check**
- Commenter 59vfx91 (the only technical critique in the thread): the temple
  "feels a little small scale, something about the wear details, the scale of
  the AO mask in the texturing don't give me the impression of a gigantic
  object. I think you need to dial the large wear back a bit and then layer
  on more subtle high res details."

**Why**
- Wear scale is scale cue. Large wear reads as a small object up close; fine
  wear reads as a gigantic object far away. (Inference from the critique,
  labeled as such.)

## Phase 3: Scatter vegetation with the Meadow toolkit

**Do**
1. Use the Meadow toolkit for vegetation scattering and quick setups
   (author's words; toolkit author beatreichenbach replied in the thread:
   "thank you for using the Meadow tool kit. I'm so happy you found it useful").

**Check**
- The cliff side with rocks and vegetation reads as one environment, not
  scattered props (beatreichenbach: "I love the way you created the cliff
  side with the rocks and the vegetation").

**Why**
- Scattering tools trade manual placement for density and variation, which is
  what sells a cliff face.

## Phase 4: Light and assemble in Houdini Solaris

**Do**
1. Assemble the scene and light it in Houdini, Solaris.
2. Bring in KTT terrains and Megascans cliffs as the large landforms.

**Check**
- Commenter 59vfx91: "It could also be partially be that the comp of it
  feels a little crunchy for how distant the object is, and therefore feels
  slightly less atmospheric than it should be."

**Why**
- Distance needs atmosphere. A distant object comped as crunchy as a near one
  breaks the scale read.

## Phase 5: Comp in Nuke

**Do**
1. Comp the shot in Nuke.

**Check**
- The comp is the step the critique targets: soften for distance, add
  atmospheric depth. No parameters were disclosed for the comp.

**Why**
- The comp is where scale is finished or broken. (Inference, labeled.)

## The human method, distilled

1. Buy the big stuff (vegetation, terrain, cliffs), build the hero stuff
   (temple, monks).
2. Let bad sims live if they hold up at shot scale and add movement.
3. Wear scale is object scale: dial large wear back, layer fine detail on top.
4. Distance needs atmosphere in the comp, or the object reads small and near.

**Depth status:** PARTIAL. Post text plus 12 comments; no parameters, no
breakdown (ArtStation link returned 403). FULL depth needs that breakdown to
become readable.
