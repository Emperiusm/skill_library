---
name: blender-gingerbread-house-build
description: "Build a finished gingerbread-house scene in Blender as a beginner tutorial series finale: flat-sculpted gingerbread man with one Principled BSDF, mirrored tree with ornaments, Botaniq scatter for dressing, one 20,000-instance snowfall particle pass, and a Cycles render finished in the compositor with Glare and tone. Trigger when building a small seasonal scene in Blender, or when a tutorial needs a complete model-to-composite arc with concrete settings."
---

# Blender Gingerbread House Build (Part 7 Finale)

## Purpose

This skill reconstructs the exact workflow Ryan King Art shows in Part 7 of the beginner Blender gingerbread-house tutorial series: build the house from simple modeled pieces, dress it with the Botaniq scatter library, animate one cheap particle snowfall pass, and finish the Cycles render in the compositor. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: build the house from simple modeled pieces, dress it with a scatter library, animate one cheap particle pass, and finish in the compositor. Evidence is the description timestamps plus 12 frames read from the downloaded video; there are no captions.

## Source

Creator: Ryan King Art. Video: "Part 7: How to Create a Gingerbread House in Blender (Beginner Tutorial)", https://www.youtube.com/watch?v=vDxBuMlqJ-A (39:34, 3,266 views, uploaded 2026-11-18). Tutorial playlist: https://www.youtube.com/playlist?list=PLUvm19RhcOTA. Artwork: https://www.artstation.com/artwork/xdOoE4. Audited in the 2026-11-20 scout run, audit 4.

## Tools used

Blender, Botaniq Tree and Grass Library (engon), ambientCG Wood036 texture, Poly Haven Christmas HDRI (`christmas_photo_studio_02`), Pixabay gingerbread-man vector.

## When to use this skill

- Building a small seasonal scene in Blender from simple pieces.
- Dressing a scene with a scatter library instead of modeling vegetation.
- Adding snowfall with a single particle system and no simulation.
- Finishing a Cycles render in the compositor (Glare and tone) instead of in the 3D scene.

## Prerequisites

- Blender (the series is a beginner tutorial; no version is stated in the description).
- Botaniq Tree and Grass Library installed (affiliate links in the description: Gumroad, Superhive).
- Wood texture (ambientCG Wood036) and Christmas HDRI (Poly Haven `christmas_photo_studio_02`).

## Phase 1: Dress the scene with Botaniq

**Do**
1. Open the Botaniq asset browser (engon browser): 1,413 assets, tag filters including Autumn, Drawn, Hair/Branches Masking, Photo, Spring, Summer, Variant Full, Variant Lite, Winter.
2. Set Transform selection to Ground/Random and use the Scatter and Clicker tools; object tools include Spread Objects, Make Collections Instanced, and Group Selected Objects.

**Check**
- Frame 000 shows the browser with Flower Cerastium thumbnails and the tag list; the scatter tools are visible in the left panel.

**Why**
A scatter library is how a beginner scene gets dressed vegetation without modeling every plant: pick, scatter, move on.

## Phase 2: Model the gingerbread man (1:14)

**Do**
1. Model the gingerbread man as a flat sculpted shape (Plane.045 in the frames).
2. Give it a Principled BSDF: Base Color tan gingerbread, Metallic 0, Roughness 0.400, IOR 1.500, Alpha 1.000.
3. Use Alt+S (Clear Scale) while shaping, per the on-screen overlay.

**Check**
- Frame 002 shows the man in Top Orthographic with two white eyes and a mouth, the Principled BSDF values in the panel, and the "Alt + S / Clear Scale" hint.

**Why**
One flat shape plus one material is the whole character at this scale: the icing and candy carry the read, not the geometry.

## Phase 3: Tree and decorations (13:00-22:17)

**Do**
1. Build the tree as a mirrored flat shape: Mirror modifier, Axis X, Bisect X, Flip X, Clipping on, Merge 0.001 m, Merge Distance 0.001 m (frame 004).
2. Add ornaments, a candy cane, and icing; the tree is green with blue baubles and a star (frame 006).
3. Render settings visible in frame 006 are Eevee: Emission Sampling Auto, Transparent Shadows, Bump Map Correction, Volume Sampling Multiple Importance, Render Method Dithered, Thickness Sphere, Volume Intersection Fast.

**Check**
- Frame 006 shows the finished tree against the house with the candy cane and icing in place; the Eevee settings panel is open on the right.

**Why**
Mirror once, decorate once: symmetry does half the modeling, and the decorations are separate small pieces rather than geometry in the tree itself.

## Phase 4: Snowfall particle pass (23:03)

**Do**
1. Add a particle system for snowfall: Emission Number 20000, Frame Start 1.000, Frame End 50.000, Lifetime 50.000, Lifetime Randomness 0.000.
2. Render As Object, Object: Snow, Scale 2.750, Scale Randomness 1.000.

**Check**
- Frame 008 shows the particle settings panel and the full house in Camera Perspective with the tree, fence, and candy in place.

**Why**
One particle system with a single snow object is the cheapest possible snowfall: 20,000 instances of one object, no simulation, no per-flake work.

## Phase 5: Final adjusting and compositing (27:19-33:34)

**Do**
1. Do final adjustments (27:19), then move to the Compositing workspace (33:34).
2. Render in Cycles, Device GPU Compute (frame 010).
3. In the Scene Compositor, run the image through a Glare node (Threshold 0.839 in the frame) and a "Tone Image" node group, then to the Viewer Node and Group Output.

**Check**
- Frame 010 shows the compositor node tree (Group Input, Tone Image group, Glare, Group Output) and the finished render in the Viewer Node.

**Why**
Compositing is where the render gets its finish: the modeling is done, and glow plus tone are cheaper and more controllable here than in the 3D scene.

## Phase 6: Fix the gingerbread (36:58)

**Do**
1. Fix whatever the final render shows wrong with the gingerbread (the description lists this as its own timestamped step; the fix itself is in the video, no captions).

**Check**
- The author gives the fix its own chapter, which means the render exposed something worth correcting after compositing.

**Why**
The last pass is a correction pass, not a new build: look at the finished image, fix what reads wrong, stop.

## The human method, distilled

1. Dress with a library: Botaniq scatters the vegetation so modeling stays on the hero pieces.
2. Flat shapes plus one material carry the characters.
3. Mirror once, decorate with separate small pieces.
4. One particle system, one snow object, 20,000 instances: snowfall without a simulation.
5. Finish in the compositor: Glare and tone after the render, not in the scene.

**Depth status:** PARTIAL (timestamps, resource links, and 12 frames with readable parameter values; no captions, so the spoken instructions and the exact compositing node values beyond the Glare threshold are not captured).
