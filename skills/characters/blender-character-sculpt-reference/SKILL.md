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

**Depth status:** PARTIAL (12 frames with readable brush settings, material values, and vertex counts, plus the description links; no captions, so the spoken sculpting instruction is not captured).
