---
name: blender-character-sculpt-reference
description: "Sculpt a character in Blender against a reference image: block the head from one sphere in profile with Grab and Dyntopo, sculpt the robe with Clay Strips at 70 px and 0.500 strength, dress it with procedural fabric (Principled BSDF, metallic 0, roughness 1.0), and hard-model machined parts like a lightsaber hilt in Edit Mode. Trigger when sculpting a character in Blender, or when deciding which parts to sculpt and which to model."
---

# Blender Character Sculpt Against a Reference Image (Darth Maul)

## Purpose

This skill reconstructs the exact workflow Ryan King Art shows in "How I Created Darth Maul in Blender": block the head from a sphere, sculpt the body against a reference image, dress it with procedural fabric, and hard-model the lightsaber. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: block the head from a sphere, sculpt the body against a reference image, dress it with procedural fabric, and hard-model the lightsaber. Evidence is the description plus 12 frames read from the downloaded video; there are no captions.

## Source

Creator: Ryan King Art. Video: "How I Created Darth Maul in Blender", https://www.youtube.com/watch?v=um7W5ygC4ig (25:56, 4,283 views, uploaded 2026-11-19). Artwork: https://www.artstation.com/artwork/mO3wla. Audited in the 2026-11-20 scout run, audit 5.

## Tools used

Blender, Easy HDRI addon, procedural metal materials (author's Gumroad pack), Davinci School for Sculptors (author's course).

## When to use this skill

- Sculpting a character in Blender from a sphere blockout.
- Sculpting cloth/robes against a reference image.
- Dressing a sculpt with procedural fabric instead of modeling weave.
- Deciding which parts of a character to sculpt and which to hard-model.

## Prerequisites

- Blender (no version stated in the description).
- A reference image of the character's full pose, kept open in a second panel while sculpting.
- Easy HDRI addon for lighting (named in the description).

## Phase 1: Block the head from a sphere

**Do**
1. Start in Sculpt Mode with a sphere (Sphere.001 in the frames).
2. Work the profile in Right Orthographic with the Grab brush; Dyntopo on; unit scale 10 centimeters.

**Check**
- Frame 001 shows the head in profile: forehead, nose, chin, ear, neck, and a shoulder mass, all from the one sphere.

**Why**
The head is one mass before it is a face: profile first, features later. Dyntopo lets the topology follow the form instead of fighting a base mesh.

## Phase 2: Sculpt the body against a reference image

**Do**
1. Keep a reference image open in a second panel ("Darth Maul 2" in the frames) and sculpt the robe and torso against it.
2. Use the Clay Strips brush: Size 70 px, Strength 0.500.

**Check**
- Frame 004 shows the robe folds taking shape on the left and the full reference pose on the right; the mesh reads 47,536 verts / 47,532 faces at that point.

**Why**
The reference is the judge: the sculpt is compared against the pose continuously instead of from memory, and Clay Strips builds the cloth folds in broad passes.

## Phase 3: Dress it with procedural fabric

**Do**
1. In the Shading workspace, build the fabric material: Principled BSDF, Base Color, Metallic 0.000, Roughness 1.000, IOR 1.500, Alpha 1.000, fed by fabric texture nodes through a Mapping node (Plane.017, Pants, in the frames).

**Check**
- Frame 007 shows the node graph (fabric texture nodes into the Principled BSDF) and the material panel values.

**Why**
Cloth at this scale is a material problem, not a geometry problem: rough, non-metallic fabric with a texture-driven pattern reads as robe without modeling weave.

## Phase 4: Hard-model the lightsaber hilt

**Do**
1. Model the double-bladed hilt as hard-surface geometry in Edit Mode (Cylinder.001 in the frames), rotating sections 110 + 5 degrees along local Z to place the rings and details.

**Check**
- Frame 009 shows the hilt in wireframe with its rings and the rotation readout; the final render (frame 011) shows the red double blade ignited.

**Why**
The hilt is machined, not sculpted: Edit Mode with exact rotations is the right tool for rings and cylinders, and it is a separate discipline from the organic sculpt.

## Phase 5: Final render

**Do**
1. Present the finished character: black robe, red-and-black face with horns, double-bladed red lightsaber.

**Check**
- Frame 011 is the final render: the full figure against a dark background, saber lit.

**Why**
The render is the deliverable for a fan-art sculpt: the pose and the saber sell the character, not a turntable.

## The human method, distilled

1. One sphere, profile first: the head is a mass before it is a face.
2. Sculpt against the reference, not from memory: the reference panel stays open.
3. Cloth is a material: procedural fabric over sculpted folds.
4. Machined parts get Edit Mode: the hilt is modeled, not sculpted.

## AAA studio practice

AAA character work runs exactly the split this skill makes: sculpt the organic, hard-model the machined, and let the reference decide. At Santa Monica Studio, creature sculptor Luke Starkie received a simple base mesh with the general proportions from the studio, took it into ZBrush, and re-sculpted it against new concept art, refining forms and proportions before any detail work, with art director Raf Grassetti giving feedback in the loop. The studio's character-art lead, Glauco Longhi, describes the same discipline at department scale on God of War Ragnarok: a team of eight character artists working to a set bar and standards, with a pipeline for prototyping characters and enemies where each step is approved by department leads, and close work with design, tech art and animation on the pipeline. The decision rule is visible in the Kratos case: the team made a new high-detail sculpt of Kratos for Ragnarok but kept the original low-poly game mesh, because changing it would have broken facial blendshapes, UV textures and the rage animation system; instead they re-sculpted specific elements (armor, legs, beard) and baked the high-resolution detail onto the existing mesh. Character art is decisions under technical constraints, not pure sculpting.

Blender Studio's own production modeling pipeline states the same order of operations: an approved concept design is required before modeling, the organic path runs concept and deformation tests first and ends in a final topology, sculpted surface details are reprojected onto the subdivided retopology via the multiresolution modifier, and shape keys carry the sculpted animation shapes. For clothing specifically, the production standard is a two-stage pipeline: Marvelous Designer builds the garment from sewn 2D patterns and simulates the drape over the character, then the high-resolution result goes into ZBrush for the final pass, stitches, extra folds, wear and weathering. One studio pipeline description is explicit that Marvelous Designer output is "good but not final quality" and that the ZBrush refinement pass is what makes garments believable for games; the low-resolution in-game model is then built to match the high-resolution shape, with textures baked from high to low.

The AAA rule that transfers: the reference image in this skill is the indie version of the approved concept design, and the sculpt-vs-model split is the same split every studio pipeline enforces. What the skill is missing relative to production is the step after the sculpt: the Darth Maul figure is a still render, so no retopology or bake is needed, but any character that has to move needs the retopology and bake stages before it is game-ready, and cloth that has to read as tailored needs the simulation-first, sculpt-second pass rather than sculpted folds alone.

Sources:
- School of Motion, "Sculpting Creatures for 'God of War: Ragnarok' and More" (Luke Starkie: base mesh from the studio, re-sculpt against concept art, art-director feedback loop): https://schoolofmotion.com/blog/sculpting-creatures-for-god-of-war-ragnarok-and-more
- Glauco Longhi, "God of War - Ragnarok" (character-art pipeline, eight-artist team, per-step department-lead approval, prototyping pipeline): https://www.glaucolonghi.com/work/god-of-war-ragnarok-jp7s5
- Blender Studio, "Modeling" pipeline overview (approved concept required, sculpt to final topology, multires reprojection, shape keys for sculpted animation shapes): https://studio.blender.org/tools/pipeline-overview/asset-creation/modeling
- Vertex School, "Kratos in God of War Ragnarok" explainer (secondary summary: new high-detail sculpt kept on the original low-poly mesh to protect blendshapes, UVs and the rage system; armor, legs and beard re-sculpted and baked): https://www.instagram.com/reel/DfqRdikDQBg/
- ModDB, "A brief look of the character model workflow" (Marvelous Designer drape, ZBrush refinement pass, low-res in-game model matched to high-res, textures baked high-to-low): https://www.moddb.com/news/a-brief-look-of-the-character-model-workflow

### Agent automation upgrade (Do / Check / Why)
**Do**
- Add a sculpt-stage manifest `sculpt-stages.json` before starting: one entry per stage (silhouette/profile, secondary forms, detail, cloth, hard-surface parts), each with its acceptance render path. The agent may not start the detail stage until the silhouette render matches the reference silhouette.
- Add a part-type split gate at the start of the build: list every part of the character as organic (sculpt) or machined (Edit Mode), with the split written to the manifest. A part that changes type mid-build requires a manifest edit and a reason, so the split stays a decision instead of drifting.
- Add a reference-check render after each stage: the same camera angle as the reference image, side by side with the reference, saved as `stage-<n>-vs-reference.png`. The comparison is the check the skill's Phase 2 does by eye, made into a file.
- Add a fabric material record `fabric-material.json` with the Principled BSDF values (Metallic, Roughness, IOR, Alpha) and the texture-node chain, so the material is reproducible from the record instead of re-read from a screenshot.
**Check**
- Every stage has an acceptance render on disk before the next stage starts; a stage with no render is an unstarted stage.
**Why**
- The skill's method is "sculpt against the reference, not from memory", and a stage manifest with per-stage renders is that rule enforced by files: the reference comparison happens at every stage instead of only at the final render, and the part-type split stops a machined part from being sculpted by habit.

**Depth status:** PARTIAL (12 frames with readable brush settings, material values, and vertex counts, plus the description links; no captions, so the spoken sculpting instruction is not captured).
