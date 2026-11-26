---
name: blender-geometry-nodes-data-visualization
description: "Turn a real density map into a 3D bar visualization in Blender: clean the California population density 2020 map in Krita to isolated blobs on transparency, map it onto a plane with an Image Texture into a Principled BSDF, then drive a Geometry Nodes extrusion from the image (ColorRamp Pos 0.407, Multiply Value 1.550 into Offset Scale) and shade the bars with a ramp-to-bump network. DEPTH-LIMITED: no transcript; workflow reconstructed from 18 frames read firsthand plus the description snippet. Trigger when a data map must become readable 3D geometry instead of a flat heatmap."
---

# Blender Geometry Nodes Data Visualization (Census Density Map)

## Purpose

This skill turns a real density map into readable 3D bars: real data in, cleaned data through, extrusion driven by the image. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: clean the map first, map it flat, extrude by value, shade so height reads.

## Source

- Video: "Create Data Visualizations with Geometry Nodes" by Ryan King Art — https://www.youtube.com/watch?v=4wkS86ML72E (1,479.5 s, 9,323 views per scanner metadata). YouTube metadata was bot-walled and oEmbed-only, with no captions; the media was downloaded (depth-escalation download 2 of 2) and 18 frames were read firsthand. No transcript exists, so no spoken wording is quoted. Description snippet (scanner): California population map 3D animation; Krita used to edit the texture; project files sold (Gumroad/Patreon/Superhive). Scout audit 2026-11-26, audit 8.

## Tools used

Blender (Geometry Nodes, Shading workspace, Principled BSDF); Krita (texture cleanup); source map: "California population density 2020.png" from Wikipedia (United States Census source, per the on-screen file page). No Blender version stated in the evidence reviewed; do not claim one.

## Phase 1: Source a real density map

**Do**
1. Start from the Wikipedia file page "California population density 2020.png" (frame 1), showing the state outline with red density areas and a legend. Legend buckets, frame-read: 1, 5, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000.

**Check**
- The map must be the Census density map, not an artistic heatmap: the file page's source line (United States Census) is visible in frame 1. The legend gives the data scale the extrusion will follow.

**Why**
A data visualization needs real data as its input. The map's legend is the contract for what the bar heights will mean.

## Phase 2: Clean the map in Krita to isolated density blobs

**Do**
1. Open the map in Krita (frame 4 shows the Krita canvas with a checkerboard transparency background, isolated red/blue density blobs, and a selection around one region; layers panel shows "Background" and an opacity control at 100%).
2. [Inference: erase/cut the map down to the density blobs on transparency, so only the data areas remain as image content.] The exact Krita tools are not legible in the frame and are not invented here.

**Check**
- The canvas must show only the density blobs on transparency, with the surrounding map removed. Frame 4 is the check: blobs float on the checkerboard, separated from each other.

**Why**
The Geometry Nodes extrusion reads the image; anything left in the image (borders, legend, background) would extrude or colour the result. Cleaning first means the network only ever sees data.

## Phase 3: Map the image onto a plane in Blender's Shading workspace

**Do**
1. In Blender, put the cleaned image on a plane: frame 8 shows the Shading workspace with an Image Texture node ("California_p...") feeding the Base Color of a Principled BSDF, with Roughness 1.000 and Alpha 1.000 (frame-read), and the plane in the viewport showing the California map with its legend.

**Check**
- The plane must show the map correctly oriented with the legend readable, before any Geometry Nodes work. Frame 8 is that check.

**Why**
The image is both the colour source and the height source for the next phase. Getting the mapping right on a flat plane first separates "wrong image" problems from "wrong extrusion" problems.

## Phase 4: Extrude bars with Geometry Nodes, driven by the image

**Do**
1. Add a Geometry Nodes modifier to the plane (frame 12, top bar: Plane / GeometryNodes / "Data Viz" node group).
2. In the network (frame 12, frame-read): a ColorRamp node (RGB, Linear; Pos 0.407) feeds a Multiply node (Value 1.550, Clamp unchecked) whose output feeds Offset Scale / Individual on the geometry.
3. The result (frame 12 viewport and status bar, frame-read): a dense field of extruded bars over the map plane; status bar shows Verts 1,455,340 and Faces 1,533,340, i.e. the extrusion is high-poly in the viewport at this stage.

**Check**
- Bar height must follow density: the tallest bars cluster where the map is densest. The ColorRamp position (0.407) and Multiply value (1.550) are the two stated controls for that mapping; no other node values are legible in the frames reviewed and none are invented.

**Why**
The data drives the geometry: colour ramp remaps the image value, multiply scales it into height. Two numbers control the whole visualization, which is why they are the values worth recording.

## Phase 5: Shade the bars so height reads in the render

**Do**
1. Frame 14 shows a shading network for the bars: a Color Ramp (Pos 0.000) feeding a Bump node (Invert checked, Strength 0.500, Distance 0.500 px, frame-read) into a Principled BSDF (Roughness 0.500, frame-read).
2. Frame 16 shows the rendered view: red bars rising over the blue map plane, with the map's legend visible on the plane behind, shot from a low camera angle.

**Check**
- Height must read from the camera's angle, not just from above: the low render angle in frame 16 is the check that bars, colour, and map plane read together as one visualization.

**Why**
Extrusion without shading is a grey field. The ramp-to-bump step gives the bars surface variation so their height is visible in a still render, and the low camera sells the 3D-ness that a top-down view would hide.

## Endcard, not part of this workflow

Frame 17 is a different segment (an endcard/promo): "Light Colors / Geometry Nodes" showing a Christmas-lights string with a Geometry Nodes modifier panel (Light Bulb Scale 0.500, Light Spacing 0.2 m, frame-read). It demonstrates a separate modifier, not the data-visualization build. Do not merge its values into Phases 1-5.

## The human method, distilled

1. **Real data in, cleaned data through:** Census map first, Krita cleanup second, extrusion third.
2. **Two numbers drive the visualization:** ColorRamp position and Multiply value; record those, not the whole node tree.
3. **Check flat before extruding:** the mapped plane must be right before height is added.

## Depth status

DEPTH-LIMITED. No captions or transcript: YouTube metadata was bot-walled and oEmbed-only; 18 frames from a media download were read firsthand, plus the scanner's description snippet. No spoken node-by-node narration, Blender version, animation/keyframe steps, or render settings beyond the frame-read values above were recoverable, and none are invented. A transcript would add the narration and any animation steps; it would not change the frame-read values.
