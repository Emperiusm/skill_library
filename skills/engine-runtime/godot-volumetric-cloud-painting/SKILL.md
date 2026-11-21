---
name: godot-volumetric-cloud-painting
description: "Build a cozy Godot game about painting cloudscapes and sunsets in volumetric 3D: a cloud simulation modeled on the Nubis3 engine from Decima (Horizon games), built from SIGGRAPH papers with everything in render or compute shaders, 3D stamps now moving to simulated 3D brush strokes, with HDRI-type export planned. Trigger when building volumetric clouds or sky painting in Godot, or when deciding whether the renderer or the brushes are the fidelity gap."
---

# Godot Volumetric Cloud Painting (Sunset Painter)

## Purpose

This skill reconstructs the exact workflow SDGGame uses to build Sunset Painter, a cozy Godot game about creating cloudscapes and sunsets in volumetric 3D (essentially Tiny Glade, but you craft the sky): a cloud simulation modeled on the Nubis3 cloud engine in the Decima engine (Horizon games), built from SIGGRAPH papers, with everything in render or compute shaders except the Control-node UI. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: build the cloud renderer from the published literature first, then close the remaining gap in the brushes, not the renderer.

## Source

Creator: SDGGame. Reddit post: https://www.reddit.com/r/godot/comments/1y0h7em/ (r/godot post 1y0h7em, score 63, 6 comments). Steam: https://store.steampowered.com/app/4985820/Sunset_Painter/. Audited in the 2026-11-20 scout run, audit 2.

## Tools used

Godot, render shaders and compute shaders, SIGGRAPH papers on cloud simulation, Nubis3 cloud engine (Decima engine, Horizon games) as the model.

## When to use this skill

- Building volumetric clouds or a sky-painting game in Godot.
- Reimplementing a published cloud engine (Nubis3/Decima) instead of inventing a cloud model.
- Diagnosing whether a volumetric renderer or its input brushes are the fidelity bottleneck.
- Planning export of a painted volume (HDRI, or a renderer plugin) for use in another game.

## Prerequisites

- Godot with render-shader and compute-shader support.
- The SIGGRAPH papers on cloud simulation the author follows (no paper titles are disclosed in the post; find the Nubis3/Decima literature as the starting point).
- A voxel representation for the cloud shapes.

## Phase 1: Build the cloud simulation from SIGGRAPH papers

**Do**
1. Follow SIGGRAPH papers to create a cloud simulation similar to the Nubis3 cloud engine in the Decima engine (Horizon games).

**Check**
- *Inference:* the author names the literature and the reference engine, but no paper title, shader code, or parameter is disclosed.

**Why**
A published cloud engine is a known-good target: the author is reimplementing a proven method rather than inventing a cloud model from scratch.

## Phase 2: Keep everything in shaders

**Do**
1. Implement everything as either a render shader or a compute shader, other than the Control node UI elements.

**Check**
- The author states this as the architecture of the whole game, not one effect.

**Why**
Shaders are where volumetric work lives in Godot; keeping the simulation in shaders means the painting interaction and the rendering are the same system, not a CPU sim driving a separate renderer.

## Phase 3: Close the brush gap, not the renderer gap

**Do**
1. Treat the renderer as essentially done.
2. Work on the fidelity of the brushes themselves, which the author names as "the one thing still separating me from photorealism".
3. Accept that the renderer "is only as detailed as the underlying voxel shapes". The current version uses 3D stamps; move towards actual 3D simulated brush strokes.

**Check**
- The author judges the gap by looking at the result: the renderer is done, the brushes are not, and the voxel shapes are the resolution limit.

**Why**
Fixing the wrong layer wastes the work: more renderer polish cannot add detail the voxel shapes do not carry. The brush is the input device, and its fidelity is the product.

## Phase 4: Terrain now, props later, export next

**Do**
1. Let the player modify the terrain.
2. Add props and stuff later ("at some point").
3. For export, look into HDRI-type exports first, and consider turning the renderer half into a plugin "so you can export a volume and render it in another game" (the author's comment reply to a user asking whether clouds can be used in other game scenes).

**Check**
- A commenter asked directly about exporting clouds for other game scenes; the author answered with the HDRI and plugin options, not a promise.

**Why**
A cozy painting game is also a volume-authoring tool if the volume can leave the game. Export turns a toy into a pipeline stage, but only after the painting itself is good.

## The human method, distilled

1. Reimplement the literature: SIGGRAPH papers and Nubis3, not a from-scratch cloud model.
2. Everything in shaders except the UI.
3. Judge which layer is the gap: the renderer is done, the brushes are not.
4. The voxel shapes are the resolution limit; stamps now, simulated strokes next.

## AAA studio practice

This skill reimplements the reference engine directly: Nubis is Guerrilla's real-time volumetric cloud system in the Decima engine, and the Sunset Painter author's method (SIGGRAPH papers, Nubis3 as the model, everything in shaders) is the published Guerrilla method. Andrew Schneider, Guerrilla's Atmospherics Lead, presented the system in three SIGGRAPH Advances in Real-Time Rendering courses and a GDC 2022 talk. The 2015 prototype raymarched through layered 3D noise textures (mixes of Perlin and Worley noise) shaped by a weather map controlling cloud coverage, type, and rain chance, and rendered a variety of cloud types in various lighting conditions in under 2 milliseconds on the PlayStation 4. The 2017 authoring talk added what turns a prototype into a production tool: authoring cloudscapes on a regional scale, animation and transitions, integration into the atmospheric system, and a lighting-model upgrade. For Horizon Forbidden West the system was reworked as "Nubis, Evolved" so players could fly through clouds on the Sunwing mount, delivering detailed results at 1080p without temporal upscaling, with a method to mitigate temporal artifacts in fast-moving clouds and a near-zero-cost method for internal lighting effects. The 2023 "Nubis, Cubed" talk moved from the widely adopted 2.5D methods to true voxel-based clouds, solving ray-march acceleration with compressed signed distance fields, fluid-simulation-based modeling of clouds, a method to up-rez dense voxel data that avoids memory-access bottlenecks, light-sampling acceleration, and approximations for cloud-specific lighting features like dark edges and inner glow, all built in under six months.

Two Guerrilla decisions map directly onto this skill's diagnosis. First, the voxel shapes are the resolution limit: Nubis3's up-rez step exists precisely because dense voxel data is the memory bottleneck, and the author is right that brush fidelity, not renderer polish, is the gap, because the renderer's job is to faithfully render whatever voxels the brushes put down. Second, artist control stays explicit: the weather map is a deliberate control layer (coverage, type, rain chance) on top of procedural noise, so the clouds are authored, not just generated. The GDC 2022 superstorm talk adds the scaling discipline: tornadic superstorms, internal lighting and lightning were added without expensive simulations or lighting calculations, so the system could scale between current- and previous-generation PlayStation consoles.

The AAA rule that transfers: budget the cloud pass in milliseconds and the voxel data in memory before adding features, and keep an explicit authoring layer (weather map, brush strokes) above the procedural noise. The author's "renderer is done, brushes are not" judgment is the same layering Guerrilla uses: the renderer renders voxels, the authoring layer decides what voxels exist.

Sources:
- Guerrilla Games, "Nubis: Authoring Real-Time Volumetric Cloudscapes with the Decima Engine" (SIGGRAPH 2017; under 2 ms on PS4, weather-map control, Perlin-Worley noise, regional authoring): https://www.guerrilla-games.com/read/nubis-authoring-real-time-volumetric-cloudscapes-with-the-decima-engine
- Guerrilla Games, "Nubis, Evolved" (SIGGRAPH 2022; fly-through clouds, 1080p without temporal upscaling, internal lighting, temporal-artifact mitigation): https://www.guerrilla-games.com/read/nubis-evolved
- Guerrilla Games, "Nubis³" (SIGGRAPH 2023; voxel-based clouds, compressed-SDF ray-march acceleration, fluid-sim modeling, voxel up-rez): https://www.guerrilla-games.com/read/nubis-cubed
- Andrew Schneider, schneidervfx.com (talk index: SIGGRAPH 2015 prototype, SIGGRAPH 2023 course, GDC 2022 superstorms talk): https://www.schneidervfx.com/

### Agent automation upgrade (Do / Check / Why)
**Do**
- Add a cloud-pass budget log `cloud-budget.json`: per frame, the cloud pass time in milliseconds at the target resolution and the voxel-grid memory in megabytes. Fail the build if the cloud pass exceeds the budget the project sets (Guerrilla's bar is under 2 ms on PS4 hardware for the skybox pass; a Godot project should set its own number and record it, not borrow Guerrilla's).
- Add a voxel-resolution audit: record the voxel grid size and the smallest paintable feature (in world units) per brush, and fail if a brush stroke is finer than the voxel grid can represent, since that detail is silently lost.
- Add a brush-fidelity acceptance set: render the same cloud volume from three distances (ground, mid-air, close fly-through) after every brush change, and keep the renders in `brush-acceptance/` so a brush regression is visible as a diff, not a feeling.
- Add a weather-map parameter manifest `weather-map.json` recording coverage, cloud type, and rain chance per region, so the authoring layer is data the agent can diff and the renderer can read, instead of values buried in shader code.
**Check**
- The budget log shows the cloud pass time and voxel memory for the current build, and the acceptance renders exist for the latest brush version.
**Why**
- The skill's core diagnosis is a layering judgment (renderer done, brushes not), and a budget log plus acceptance renders turn that judgment into measurements: the renderer is proven done by its millisecond budget, and the brush gap is proven closed by renders at three distances instead of one look from the ground.

**Depth status:** PARTIAL (method, tools, reference engine, and the brush-vs-renderer diagnosis are disclosed; no paper titles, shader code, or parameters).
