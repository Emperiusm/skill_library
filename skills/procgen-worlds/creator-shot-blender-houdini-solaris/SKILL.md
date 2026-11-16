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

## AAA studio practice

- **The real *The Creator* shot plates first and built VFX after (ILM, 20th Century Studios).** Director Gareth Edwards shot the plates he knew he would use, then ILM designed and executed the effects around, over, and within the live-action shots, with no previs and no tracking markers. VFX supervisor Jay Cooper's framing, via the film's production record: shoot in 360 degrees, anything could become a VFX shot. The budget discipline: spend 10 units of a 100-unit budget on the shoot and keep 90 for VFX and post ([TheWrap](https://www.thewrap.com/the-creator-visual-effects-oscar-nomination/)). The author's recreation follows the same order (model, then light, then comp) for the same reason: the plate, or the modeled shot, is fixed first; everything else serves it.
- **Build only what the shot needs, and extend the rest with paint (ILM, RenderMan).** "We were very optimized throughout the production process, making only what was needed for a shot and implying a larger world without having to build out massive environments all the time, extending things with matte painting layers when needed," said ILM VFX supervisor Charmaine Chan. For the test footage, "ILM would paint things in 2D and then project them onto simple geometry. 'It gave that illusion of parallax,' Edwards said. 'What would normally take a month to do we would do in two or three days.'" ([Pixar RenderMan, ILM on The Creator](https://prod.renderman.pixar.com/stories/renderman-at-ilm--the-creator); [TheWrap](https://www.thewrap.com/the-creator-visual-effects-oscar-nomination/)). The author's buy-the-big-stuff rule is the same discipline at indie scale: bought-in vegetation, terrain, and cliffs are the matte-painting layer; the modeled temple and monks are the "only what the shot needs" part.
- **Match the plate by making things imperfect (ILM).** "We tried to really match the plates by profiling everything and making things imperfect, including lens aberrations and noise. Our lighters were amazing at getting us beautiful renders and we also extended the fidelity of the renders with some wonderful compositing using RenderMan AOVs and LPEs in Nuke," said ILM VFX supervisor Ian Comley ([Pixar RenderMan](https://prod.renderman.pixar.com/stories/renderman-at-ilm--the-creator)). The critique the author received (comp too crunchy for the distance, needs more atmosphere) is the same failure mode in reverse: the comp did not match the plate's distance behavior.
- **Solaris is the studio answer to the author's exact handoff: light and assemble separately from modeling (SideFX, RISE).** "At RISE, Solaris has become the backbone of a USD-based pipeline, giving the team scalability and efficiency for complex projects. On Fallout, it streamlined large environments and FX by reusing caches and enabling quick shot-specific changes." USD works in layers: a base geometry layer, a lighting layer on top, variants as toggleable layers instead of duplicated scenes, and a senior lighter mapping the general scheme that is tweaked non-destructively per shot with the Light Mixer ([SideFX, Solaris](https://www.sidefx.com/products/houdini/lookdev/solaris/)). The author's Blender-to-Solaris split is the same layering idea with the modeling layer living in Blender instead of USD; the discipline to copy is that lighting never edits geometry, it layers over it.

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

## Phase 6: Apply the studio gates

The thread's only technical critique is a checklist in disguise. Turn it
into gates the agent runs before calling the shot done.

**Do**
1. Write `shot-manifest.json` for the shot: every asset, tagged bought-in
   (vegetation, terrain, cliffs) or built (temple, monks), with its source
   file. If an asset is neither tagged nor in the manifest, the shot is not
   done.
2. Run the wear-scale gate from Phase 2 as a check, not a feeling: list every
   wear/grunge layer on the hero asset with its world-space feature size;
   any wear feature larger than the fine-detail layers gets dialed back
   before the comp, per the 59vfx91 critique.
3. Run the distance-atmosphere gate from Phase 4: render the hero asset at
   its shot distance and at half that distance; the far render must read
   softer (lower contrast, more atmospheric haze) than the near render, or
   the comp fails the gate.
4. Keep the layer discipline from the Solaris section: the Blender model
   file, the Solaris lighting layer, and the Nuke comp are three separate
   files. Lighting changes never edit the model file; comp changes never
   edit the lighting file.

**Check**
- `shot-manifest.json` exists and every asset in the frame is tagged.
- No wear layer on the hero asset exceeds the fine-detail scale.
- The far render is measurably softer than the near render.
- A lighting change can be reverted without touching the model.

**Why**
- ILM's rule is "make only what was needed for a shot." A manifest is how a
  one-person pipeline proves it did that, and the two gates are the
  critique, automated, so the next shot does not repeat it.

## The human method, distilled

1. Buy the big stuff (vegetation, terrain, cliffs), build the hero stuff
   (temple, monks).
2. Let bad sims live if they hold up at shot scale and add movement.
3. Wear scale is object scale: dial large wear back, layer fine detail on top.
4. Distance needs atmosphere in the comp, or the object reads small and near.

**Depth status:** PARTIAL. Post text plus 12 comments; no parameters, no
breakdown (ArtStation link returned 403). FULL depth needs that breakdown to
become readable.
