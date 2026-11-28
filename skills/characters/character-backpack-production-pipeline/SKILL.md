---
name: character-backpack-production-pipeline
description: "Take a character backpack from ZBrush blockout through Marvelous Designer cloth simulation, Blender retopology, Maya UV unwrap, Marmoset Toolbag baking, and Substance Painter texturing to Unreal Engine look dev: one tool per stage in a fixed order, simulate cloth instead of sculpting it, and judge the asset in the engine while it is still open to improvement. Trigger when a sculpted character prop must become a production-ready game asset through the manual retopo, UV, bake, and texture chain."
---

# Character Backpack Production Pipeline (ZBrush, Marvelous Designer, Blender, Maya, Marmoset, Substance Painter, Unreal)

## Purpose

This skill reconstructs the exact workflow skillerdose shows for a production-ready game backpack for a character in Unreal Engine. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: block out in sculpt, simulate the cloth where cloth is, then run the manual production chain (retopo, UV, bake, texture) in a fixed order before judging the result in the engine.

## Source

Creator: skillerdose. Post: "Kiruna Day Pack Backpack Model I did for my Character" — https://www.reddit.com/r/3Dmodeling/comments/1y6tlj5/kiruna_day_pack_backpack_model_i_did_for_my/ (score 31, 1 comment, the only comment is AutoModerator). Video: https://v.redd.it/knk8bs1ts54i1. Scout audit 2026-11-28, audit 1, PARTIAL.

## Tools used

ZBrush (blockout), Marvelous Designer (cloth simulation), Blender (retopology, "Retopo Planes" as written by the author), Maya (UV unwrap), Marmoset Toolbag (baking), Substance Painter (texturing), Unreal Engine (look dev). No versions, polycounts, texture sizes, bake settings, or cloth parameters are stated in the post. Do not invent them.

## Phase 1: Blockout in ZBrush

**Do**
1. Build the blockout of the backpack in ZBrush. The post calls the result "Production Ready Game" and the backpack is for the author's own character in Unreal Engine.

**Check**
- The blockout reads as the backpack's large forms before any cloth detail exists. No blockout image or measurement is given in the retrieved text.

**Why**
The blockout fixes the silhouette and proportions that every later stage has to preserve. Cloth detail added before the blockout is settled would be reworked.

## Phase 2: Simulate cloth details in Marvelous Designer

**Do**
1. Import the ZBrush blockout into Marvelous Designer.
2. "Simulate the cloth details" (post text, verbatim). No garment pattern, fabric preset, or simulation setting is stated.

**Check**
- The cloth detail reads on the pack (straps, folds) in the clip.

**Why**
Cloth simulated in a cloth tool carries folds a sculpt brush would have to fake one by one. The stage order matters: simulation happens on the blockout, before retopology, so the retopo mesh follows the simulated shape rather than the other way round.

## Phase 3: Retopologize in Blender

**Do**
1. Import the simulated result into Blender.
2. Retopologize "using Retopo Planes" (post text, verbatim; the author does not expand the term, and no expansion is assumed here).

**Check**
- The retopologized mesh is the game mesh that goes forward. No triangle count, edge-flow description, or wireframe is given.

**Why**
Retopology is what makes the sculpted/simulated shape into a mesh an engine can afford. It sits after simulation and before UVs because UVs are laid out on the final topology.

## Phase 4: UV unwrap in Maya

**Do**
1. Export the retopologized model into Maya.
2. "UV Unwrap the model" (post text, verbatim). No UV layout, texel density, or seam placement is stated.

**Check**
- Unwrapped UVs ready for baking. No UV image is given.

**Why**
Baking and texturing both consume UVs, so the unwrap has to be finished before either. Moving tools at this stage (Blender to Maya) is the author's stated chain, not a recommendation; no reason for the switch is given.

## Phase 5: Bake in Marmoset Toolbag, texture in Substance Painter

**Do**
1. Export into Marmoset Toolbag "for baking" (post text, verbatim). No bake settings, map list, or resolution is stated.
2. Import into Substance Painter "for Texturing" (post text, verbatim). No material, layer, or map information is stated.

**Check**
- Baked maps carry the high-detail shape onto the game mesh; the Painter textures are the visible surface. Neither map set is shown in the retrieved text.

**Why**
Baking transfers detail from the detailed shape to the light mesh; texturing is a separate pass on top of the bake. Collapsing the two hides bake errors inside texture work.

## Phase 6: Look dev in Unreal Engine

**Do**
1. "Currently working on Look Dev in Unreal Engine and seeing if I can improve anything." (post text, verbatim). The work is in progress at the time of posting.

**Check**
- The pack judged in-engine, under game lighting, against the character it belongs to. No look-dev result is reported.

**Why**
The engine view is the only view that counts for a game asset. A pack that reads in Painter but not in Unreal is not finished.

## Failure modes

- Adding cloth detail before the blockout is settled, then reworking it after retopology.
- Texturing before baking, so bake errors hide inside texture work.
- Declaring the asset done before the in-engine look-dev pass.

## The human method, distilled

1. One tool per stage, in a fixed order: sculpt, cloth, retopo, UV, bake, texture, engine. No stage is skipped and none is reordered.
2. Simulate what is cloth instead of sculpting it.
3. Judge the asset in the engine, while it is still open to improvement, not after declaring it done.

**Depth status:** PARTIAL. The stage order and the tool at each stage are fully stated by the author in the post text. Every parameter, count, and setting is unknown. What would reach FULL: the author's answers on polycounts, texture sizes, bake settings, and the Retopo Planes method, or a breakdown post.
